"""
AgentInstance — wraps the OpenAI Agents SDK pointed at Ollama's OpenAI-compatible API.

Each AgentConfig gets one AgentInstance (cached in AgentRegistry).
Supports synchronous (complete-at-once) and streaming (SSE-friendly) chat modes.
"""
from __future__ import annotations

import asyncio
import logging
import time
import uuid
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any

from openai import AsyncOpenAI

from agentcore.config import Settings
from agentcore.metrics import ACTIVE_SESSIONS, CHAT_DURATION, CHAT_REQUESTS, LLM_TOKENS
from agentcore.models import AgentConfig, ChatResponse, Message, MessageRole, TaskPipeline

if TYPE_CHECKING:
    from agentcore.core.dispatcher import ToolDispatcher
    from agentcore.core.pipeline import PipelineEngine

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Conversation persistence helpers
# ---------------------------------------------------------------------------


class ConversationStore:
    """
    Thin async wrapper around the conversations/messages tables.

    All methods swallow database errors so that a DB outage never prevents
    the chat from working — failures are logged as warnings only.

    Uses the same SQLAlchemy async engine pattern as AgentRegistry so that
    the driver (asyncpg) and connection pool are consistent across the app.
    """

    def __init__(self, postgres_url: str) -> None:
        self._postgres_url = postgres_url
        self._engine: Any = None

    async def _get_engine(self) -> Any:
        """Lazily create and cache the async engine."""
        if self._engine is not None:
            return self._engine
        try:
            from sqlalchemy.ext.asyncio import create_async_engine

            self._engine = create_async_engine(
                self._postgres_url,
                pool_pre_ping=True,
                pool_size=3,
                max_overflow=5,
            )
        except Exception as exc:
            logger.warning("ConversationStore: failed to create DB engine: %s", exc)
            return None
        return self._engine

    async def create_conversation(
        self,
        agent_profile: str,
        channel: str = "web",
        metadata: dict | None = None,
    ) -> str | None:
        """
        Insert a new row in the conversations table and return its UUID string.
        Returns None if the insert fails.
        """
        engine = await self._get_engine()
        if engine is None:
            return None
        try:
            from sqlalchemy import text

            conversation_id = str(uuid.uuid4())
            sql = text(
                """
                INSERT INTO conversations (id, agent_profile, channel, metadata)
                VALUES (:id, :agent_profile, :channel, :metadata::jsonb)
                """
            )
            import json

            async with engine.begin() as conn:
                await conn.execute(
                    sql,
                    {
                        "id": conversation_id,
                        "agent_profile": agent_profile,
                        "channel": channel,
                        "metadata": json.dumps(metadata or {}),
                    },
                )
            return conversation_id
        except Exception as exc:
            logger.warning("ConversationStore: failed to create conversation: %s", exc)
            return None

    async def ensure_conversation(
        self,
        conversation_id: str | None,
        agent_profile: str,
        channel: str = "web",
        metadata: dict | None = None,
    ) -> str | None:
        """
        Return conversation_id unchanged if provided (trusting the caller that
        it exists in the DB), or create a new conversation row and return its id.
        """
        if conversation_id:
            return conversation_id
        return await self.create_conversation(agent_profile, channel, metadata)

    async def save_message(
        self,
        conversation_id: str,
        role: str,
        content: str,
        tokens_used: int | None = None,
        model: str | None = None,
        metadata: dict | None = None,
    ) -> None:
        """
        Insert one row into the messages table.
        Silently logs and returns if the DB is unavailable.
        """
        engine = await self._get_engine()
        if engine is None:
            return
        try:
            from sqlalchemy import text
            import json

            sql = text(
                """
                INSERT INTO messages
                    (id, conversation_id, role, content, tokens_used, model, metadata)
                VALUES
                    (:id, :conversation_id, :role, :content,
                     :tokens_used, :model, :metadata::jsonb)
                """
            )
            async with engine.begin() as conn:
                await conn.execute(
                    sql,
                    {
                        "id": str(uuid.uuid4()),
                        "conversation_id": conversation_id,
                        "role": role,
                        "content": content,
                        "tokens_used": tokens_used,
                        "model": model,
                        "metadata": json.dumps(metadata or {}),
                    },
                )
        except Exception as exc:
            logger.warning(
                "ConversationStore: failed to save %s message to conversation %s: %s",
                role,
                conversation_id,
                exc,
            )

    async def close(self) -> None:
        """Dispose the connection pool."""
        if self._engine is not None:
            await self._engine.dispose()


class AgentInstance:
    """
    A live, stateful handle to one configured agent.

    The instance holds:
    - An AsyncOpenAI client pointed at Ollama's /v1 endpoint
    - The AgentConfig record it was created from
    - A reference to the shared ToolDispatcher (injected post-construction)
    """

    def __init__(self, config: AgentConfig, settings: Settings) -> None:
        self.config = config
        self.settings = settings

        # Point the OpenAI SDK at Ollama's OpenAI-compatible REST endpoint.
        # Ollama accepts any non-empty string as the API key.
        self.client = AsyncOpenAI(
            base_url=f"{settings.ollama_base_url}/v1",
            api_key="ollama",
            timeout=settings.ollama_timeout,
        )

        self._dispatcher: ToolDispatcher | None = None
        self._pipeline_engine: PipelineEngine | None = None

        # In-memory conversation history keyed by session_id.
        self._sessions: dict[str, list[dict]] = {}

        # PostgreSQL persistence for conversations and messages.
        self._store = ConversationStore(settings.postgres_url)

        logger.info("AgentInstance created: %s (model=%s)", config.name, config.model)

    # ------------------------------------------------------------------
    # Dependency injection
    # ------------------------------------------------------------------

    def set_dispatcher(self, dispatcher: ToolDispatcher) -> None:
        self._dispatcher = dispatcher

    def set_pipeline_engine(self, engine: PipelineEngine) -> None:
        self._pipeline_engine = engine

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _get_session(self, session_id: str) -> list[dict]:
        """Return (and create if missing) the message history for a session."""
        if session_id not in self._sessions:
            self._sessions[session_id] = [
                {"role": "system", "content": self.config.system_prompt}
            ]
        return self._sessions[session_id]

    def _append_message(self, session_id: str, role: str, content: str) -> None:
        history = self._get_session(session_id)
        history.append({"role": role, "content": content})

    def _build_tools_schema(self) -> list[dict]:
        """
        Build the OpenAI tool-call schema from this agent's enabled ToolConfig list.
        The actual execution is delegated to ToolDispatcher.dispatch().
        """
        schema: list[dict] = []
        for tool_cfg in self.config.tools:
            if not tool_cfg.enabled:
                continue
            schema.append(
                {
                    "type": "function",
                    "function": {
                        "name": tool_cfg.name,
                        "description": tool_cfg.description or tool_cfg.name,
                        "parameters": tool_cfg.config.get("parameters", {"type": "object", "properties": {}}),
                    },
                }
            )
        return schema

    async def _process_tool_calls(self, tool_calls: list, session_id: str) -> str:
        """
        Execute all tool_calls returned by the model and return the combined
        tool-result messages as a formatted string (also appended to history).
        """
        if self._dispatcher is None:
            return ""

        results: list[str] = []
        for tc in tool_calls:
            import json

            fn = tc.function
            try:
                args = json.loads(fn.arguments) if fn.arguments else {}
            except Exception:
                args = {}

            logger.debug("Tool call: %s(%s)", fn.name, args)
            result = await self._dispatcher.dispatch(fn.name, args)

            # Append tool result to conversation so the model can read it
            self._get_session(session_id).append(
                {
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": str(result.get("output", result)),
                }
            )
            results.append(str(result.get("output", result)))

        return "\n".join(results)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    async def chat(
        self,
        message: str,
        session_id: str,
        stream: bool = True,
        conversation_id: str | None = None,
    ) -> ChatResponse:
        """
        Run a complete (non-streaming) chat turn.

        The method handles tool calls transparently: if the model returns tool
        calls, they are dispatched and a second LLM pass is made with the
        results injected.  The final assistant message is returned.

        If conversation_id is provided the turn is appended to that existing
        PostgreSQL conversation record.  If omitted a new conversation is
        created automatically.  DB errors are logged as warnings and never
        prevent the chat from completing.
        """
        agent_id_str = str(self.config.id)
        start_time = time.monotonic()
        start_ms = int(start_time * 1000)
        ACTIVE_SESSIONS.inc()
        status = "success"
        total_tokens = 0

        try:
            # Resolve (or create) a conversation record in PostgreSQL.
            conv_id = await self._store.ensure_conversation(
                conversation_id,
                agent_profile=self.config.profile.value,
                channel="web",
            )

            self._append_message(session_id, "user", message)
            history = self._get_session(session_id)
            tools = self._build_tools_schema()

            # Persist the incoming user message.
            if conv_id:
                await self._store.save_message(conv_id, "user", message)

            max_tool_rounds = 5  # prevent infinite tool loops
            final_content = ""

            for _round in range(max_tool_rounds):
                kwargs: dict = {
                    "model": self.config.model,
                    "messages": history,
                }
                if tools:
                    kwargs["tools"] = tools
                    kwargs["tool_choice"] = "auto"

                response = await self.client.chat.completions.create(**kwargs)
                choice = response.choices[0]
                round_tokens = response.usage.total_tokens if response.usage else 0
                total_tokens += round_tokens

                if choice.finish_reason == "tool_calls" and choice.message.tool_calls:
                    # Append assistant's tool-call message to history
                    history.append(choice.message.model_dump(exclude_none=True))
                    await self._process_tool_calls(choice.message.tool_calls, session_id)
                    # Continue loop — let the model see tool results
                    continue

                # Regular assistant reply
                final_content = choice.message.content or ""
                self._append_message(session_id, "assistant", final_content)
                break
            else:
                # Exceeded max tool rounds — return whatever the last response was
                logger.warning("Agent %s exceeded max tool rounds for session %s", self.config.id, session_id)
                final_content = final_content or "I encountered a problem completing that request."

            # Persist the assistant reply.
            if conv_id:
                await self._store.save_message(
                    conv_id,
                    "assistant",
                    final_content,
                    tokens_used=total_tokens or None,
                    model=self.config.model,
                )

            duration_ms = int(time.monotonic() * 1000) - start_ms

            return ChatResponse(
                message=final_content,
                agent_id=self.config.id,
                session_id=session_id,
                tokens_used=total_tokens,
                model=self.config.model,
                duration_ms=duration_ms,
            )

        except Exception:
            status = "error"
            raise

        finally:
            elapsed = time.monotonic() - start_time
            CHAT_REQUESTS.labels(agent_id=agent_id_str, status=status).inc()
            CHAT_DURATION.labels(agent_id=agent_id_str).observe(elapsed)
            if total_tokens:
                LLM_TOKENS.labels(agent_id=agent_id_str, direction="total").inc(total_tokens)
            ACTIVE_SESSIONS.dec()

    async def chat_stream(
        self,
        message: str,
        session_id: str,
        conversation_id: str | None = None,
    ) -> AsyncIterator[str]:
        """
        Streaming chat turn.  Yields text delta chunks as they arrive from Ollama.
        Tool calls are handled transparently: the stream pauses, tools are dispatched,
        then streaming resumes with the follow-up LLM call.

        conversation_id semantics are identical to chat(): provide an existing
        PostgreSQL conversations.id to append, or omit to create a new one.
        """
        agent_id_str = str(self.config.id)
        start_time = time.monotonic()
        ACTIVE_SESSIONS.inc()
        stream_status = "success"

        try:
            # Resolve (or create) a conversation record in PostgreSQL.
            conv_id = await self._store.ensure_conversation(
                conversation_id,
                agent_profile=self.config.profile.value,
                channel="web",
            )

            self._append_message(session_id, "user", message)
            history = self._get_session(session_id)
            tools = self._build_tools_schema()

            # Persist the incoming user message.
            if conv_id:
                await self._store.save_message(conv_id, "user", message)

            max_tool_rounds = 5
            collected_tool_calls: dict[int, dict] = {}

            for _round in range(max_tool_rounds):
                kwargs: dict = {
                    "model": self.config.model,
                    "messages": history,
                    "stream": True,
                }
                if tools:
                    kwargs["tools"] = tools
                    kwargs["tool_choice"] = "auto"

                full_content = ""
                collected_tool_calls = {}
                finish_reason = None

                async with await self.client.chat.completions.create(**kwargs) as stream:
                    async for chunk in stream:
                        delta = chunk.choices[0].delta if chunk.choices else None
                        if delta is None:
                            continue

                        finish_reason = chunk.choices[0].finish_reason

                        # Accumulate tool-call fragments
                        if delta.tool_calls:
                            for tc_delta in delta.tool_calls:
                                idx = tc_delta.index
                                if idx not in collected_tool_calls:
                                    collected_tool_calls[idx] = {
                                        "id": tc_delta.id or "",
                                        "type": "function",
                                        "function": {"name": "", "arguments": ""},
                                    }
                                if tc_delta.function:
                                    if tc_delta.function.name:
                                        collected_tool_calls[idx]["function"]["name"] += tc_delta.function.name
                                    if tc_delta.function.arguments:
                                        collected_tool_calls[idx]["function"]["arguments"] += tc_delta.function.arguments
                            continue

                        # Stream text content to caller
                        if delta.content:
                            full_content += delta.content
                            yield delta.content

                if finish_reason == "tool_calls" and collected_tool_calls:
                    import json

                    # Build a proper tool_calls list for history
                    tool_calls_list = list(collected_tool_calls.values())
                    history.append(
                        {
                            "role": "assistant",
                            "content": full_content or None,
                            "tool_calls": tool_calls_list,
                        }
                    )

                    # Dispatch tools
                    if self._dispatcher:
                        for tc in tool_calls_list:
                            fn = tc["function"]
                            try:
                                args = json.loads(fn["arguments"]) if fn["arguments"] else {}
                            except Exception:
                                args = {}
                            result = await self._dispatcher.dispatch(fn["name"], args)
                            history.append(
                                {
                                    "role": "tool",
                                    "tool_call_id": tc["id"],
                                    "content": str(result.get("output", result)),
                                }
                            )
                    continue  # Second pass with tool results

                # Normal completion — persist assistant reply to PostgreSQL.
                if full_content:
                    self._append_message(session_id, "assistant", full_content)
                    # Estimate token count from character length (approx 4 chars/token)
                    estimated_tokens = len(full_content) // 4
                    if estimated_tokens:
                        LLM_TOKENS.labels(agent_id=agent_id_str, direction="total").inc(estimated_tokens)
                    if conv_id:
                        await self._store.save_message(
                            conv_id,
                            "assistant",
                            full_content,
                            model=self.config.model,
                        )
                break

        except Exception:
            stream_status = "error"
            raise

        finally:
            elapsed = time.monotonic() - start_time
            CHAT_REQUESTS.labels(agent_id=agent_id_str, status=stream_status).inc()
            CHAT_DURATION.labels(agent_id=agent_id_str).observe(elapsed)
            ACTIVE_SESSIONS.dec()

    async def run_pipeline(self, pipeline: TaskPipeline) -> TaskPipeline:
        """Execute a multi-step task pipeline using the injected PipelineEngine."""
        if self._pipeline_engine is None:
            pipeline.status = pipeline.status.FAILED
            pipeline.error = "No pipeline engine configured"
            return pipeline
        return await self._pipeline_engine.execute(pipeline, self)

    def clear_session(self, session_id: str) -> None:
        """Remove a session's conversation history from the in-memory cache."""
        self._sessions.pop(session_id, None)

    def get_session_messages(self, session_id: str) -> list[Message]:
        """Return conversation history for a session as Message objects."""
        history = self._sessions.get(session_id, [])
        messages: list[Message] = []
        for m in history:
            role_str = m.get("role", "user")
            try:
                role = MessageRole(role_str)
            except ValueError:
                role = MessageRole.USER
            messages.append(Message(role=role, content=m.get("content") or ""))
        return messages
