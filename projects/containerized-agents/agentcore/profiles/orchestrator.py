"""
Enterprise orchestrator — coordinates multiple AgentInstances via Redis pub/sub.
Only active on Tier 4 hardware with Profile 6.

Architecture
------------
- One orchestrator AgentInstance (qwen3:72b) receives enterprise requests.
- Sub-agents (qwen2.5:7b-instruct) listen on dedicated Redis channels for tasks.
- The orchestrator decomposes requests → dispatches tasks → awaits results →
  synthesises a final coherent response.
- Tasks that are independent of each other are dispatched in parallel via
  asyncio.gather() over parallel_dispatch().

Redis channel conventions
-------------------------
  agentcore:bus:enterprise          — broadcast / orchestrator listens here
  agentcore:bus:task:{task_id}      — per-task result channel (sub-agent publishes)
"""
from __future__ import annotations

import asyncio
import json
import logging
import uuid
from typing import TYPE_CHECKING

import redis.asyncio as redis

from agentcore.models import ChannelMessage

if TYPE_CHECKING:
    from agentcore.core.agent import AgentInstance

logger = logging.getLogger(__name__)

_RESULT_CHANNEL_PREFIX = "agentcore:bus:task:"
_DEFAULT_TASK_TIMEOUT = 60  # seconds to wait for a sub-agent result


class EnterpriseOrchestrator:
    """
    Coordinates multiple AgentInstances via Redis pub/sub.

    Usage
    -----
    orchestrator = EnterpriseOrchestrator(
        orchestrator_agent=orch_instance,
        subagents=[cs_instance, sales_instance],
        redis_client=redis_client,
    )
    response = await orchestrator.handle_request(channel_message)
    """

    def __init__(
        self,
        orchestrator_agent: "AgentInstance",
        subagents: list["AgentInstance"],
        redis_client: redis.Redis,
    ) -> None:
        self.orchestrator = orchestrator_agent
        # Index sub-agents by their configured name for fast lookup.
        self.subagents: dict[str, AgentInstance] = {
            a.config.name: a for a in subagents
        }
        self.redis = redis_client
        self.bus_channel: str = (
            self.orchestrator.config.metadata.get(
                "redis_bus_channel", "agentcore:bus:enterprise"
            )
        )

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    async def handle_request(self, message: ChannelMessage) -> str:
        """
        Handle a complex enterprise request end-to-end.

        Steps:
        1. Pass the incoming message to the orchestrator LLM with a
           decomposition instruction.  The orchestrator produces a JSON
           plan: a list of {"agent": str, "task": str} objects.
        2. Dispatch independent tasks to sub-agents in parallel via
           parallel_dispatch().
        3. Inject all results back into the orchestrator's context and
           ask it to synthesise a final answer.

        Falls back to a direct orchestrator reply if plan parsing fails
        (e.g. simple questions that don't require sub-agents).
        """
        session_id = message.session_id

        # --- Step 1: Decompose ---
        decompose_prompt = (
            f"USER REQUEST: {message.content}\n\n"
            "You must decide whether this request requires one or more sub-agents "
            "or can be answered directly.\n"
            "If sub-agents are needed, respond with a JSON array of tasks:\n"
            '  [{"agent": "<agent_name>", "task": "<specific_task_description>"}, ...]\n'
            "Available agents: " + ", ".join(self.subagents.keys()) + "\n"
            "If you can answer directly without delegation, respond with:\n"
            '  {"direct": true, "answer": "<your answer>"}'
        )

        plan_response = await self.orchestrator.chat(decompose_prompt, session_id)
        plan_text = plan_response.message.strip()

        # --- Try to parse the plan ---
        try:
            plan = json.loads(plan_text)
        except json.JSONDecodeError:
            # Not valid JSON — orchestrator answered directly (or model wrapped in prose).
            # Return as-is; this handles simple questions gracefully.
            logger.info(
                "Orchestrator returned non-JSON plan for session %s — treating as direct answer.",
                session_id,
            )
            return plan_text

        # Direct answer (no sub-agent delegation needed)
        if isinstance(plan, dict) and plan.get("direct"):
            return plan.get("answer", plan_text)

        # --- Step 2: Parallel dispatch ---
        if not isinstance(plan, list) or not plan:
            logger.warning(
                "Orchestrator plan for session %s was not a non-empty list; direct answer fallback.",
                session_id,
            )
            return plan_text

        tasks: list[tuple[str, str]] = [
            (item["agent"], item["task"])
            for item in plan
            if isinstance(item, dict) and "agent" in item and "task" in item
        ]

        if not tasks:
            return plan_text

        logger.info(
            "Dispatching %d sub-tasks for session %s: %s",
            len(tasks),
            session_id,
            [(a, t[:60]) for a, t in tasks],
        )

        sub_results = await self.parallel_dispatch(tasks, session_id=session_id)

        # --- Step 3: Synthesise ---
        synthesis_parts = [f"Original request: {message.content}\n\nSub-agent results:"]
        for (agent_name, task), result in zip(tasks, sub_results):
            synthesis_parts.append(f"\n[{agent_name}] Task: {task}\nResult: {result}")
        synthesis_parts.append(
            "\nUsing the above sub-agent results, provide a clear, concise, "
            "final response to the user. Do not repeat all the raw data — "
            "synthesise the key points."
        )
        synthesis_prompt = "\n".join(synthesis_parts)

        final_response = await self.orchestrator.chat(synthesis_prompt, session_id)
        return final_response.message

    async def dispatch_to_subagent(
        self, agent_name: str, task: str, context: dict, session_id: str | None = None
    ) -> str:
        """
        Send a task to a named sub-agent and await its response.

        Prefer direct in-process call when the sub-agent instance is available
        in self.subagents.  Falls back to Redis pub/sub for agents running in
        separate processes / containers.

        Args:
            agent_name:  Name matching the sub-agent's AgentConfig.name.
            task:        Natural-language task description.
            context:     Arbitrary key/value context forwarded to the sub-agent.
            session_id:  Conversation session ID; auto-generated if omitted.

        Returns:
            Sub-agent's text response, or an error string on failure.
        """
        sid = session_id or str(uuid.uuid4())

        # In-process dispatch (preferred — no Redis round-trip overhead)
        agent = self.subagents.get(agent_name)
        if agent is not None:
            context_str = (
                "\n".join(f"{k}: {v}" for k, v in context.items()) if context else ""
            )
            full_task = f"{task}\n\nContext:\n{context_str}" if context_str else task
            try:
                response = await agent.chat(full_task, sid)
                return response.message
            except Exception as exc:
                logger.error("In-process sub-agent '%s' error: %s", agent_name, exc)
                return f"[ERROR] {agent_name} failed: {exc}"

        # Out-of-process dispatch via Redis pub/sub
        task_id = str(uuid.uuid4())
        logger.info(
            "Sub-agent '%s' not in-process — dispatching via Redis (task_id=%s).",
            agent_name,
            task_id,
        )
        await self._publish_task(agent_name, task_id, task, context)
        result = await self._await_result(task_id, timeout=_DEFAULT_TASK_TIMEOUT)
        if result is None:
            logger.error(
                "Timeout waiting for sub-agent '%s' result (task_id=%s).",
                agent_name,
                task_id,
            )
            return f"[TIMEOUT] {agent_name} did not respond within {_DEFAULT_TASK_TIMEOUT}s."
        return result

    async def parallel_dispatch(
        self,
        tasks: list[tuple[str, str]],
        session_id: str | None = None,
    ) -> list[str]:
        """
        Dispatch multiple (agent_name, task) pairs in parallel.

        Uses asyncio.gather() so all sub-agents run concurrently.  Results are
        returned in the same order as the input tasks list.

        Args:
            tasks:       List of (agent_name, task_description) tuples.
            session_id:  Shared session ID base; each sub-task gets its own suffix.

        Returns:
            List of result strings, one per task, in input order.
        """
        base_sid = session_id or str(uuid.uuid4())

        async def _dispatch_one(idx: int, agent_name: str, task: str) -> str:
            sub_sid = f"{base_sid}:sub{idx}"
            return await self.dispatch_to_subagent(
                agent_name, task, context={}, session_id=sub_sid
            )

        coroutines = [
            _dispatch_one(idx, agent_name, task)
            for idx, (agent_name, task) in enumerate(tasks)
        ]
        results: list[str] = await asyncio.gather(*coroutines, return_exceptions=False)
        return results

    # ------------------------------------------------------------------
    # Redis helpers
    # ------------------------------------------------------------------

    async def _publish_task(
        self,
        agent_name: str,
        task_id: str,
        task: str,
        context: dict | None = None,
    ) -> None:
        """
        Publish a task to the Redis enterprise bus.

        Payload schema:
        {
          "task_id":    "<uuid>",
          "agent_name": "<target agent name>",
          "task":       "<task description>",
          "context":    {...},
          "result_channel": "agentcore:bus:task:<task_id>"
        }
        """
        payload = json.dumps(
            {
                "task_id": task_id,
                "agent_name": agent_name,
                "task": task,
                "context": context or {},
                "result_channel": f"{_RESULT_CHANNEL_PREFIX}{task_id}",
            }
        )
        try:
            await self.redis.publish(self.bus_channel, payload)
            logger.debug("Published task %s to channel '%s'.", task_id, self.bus_channel)
        except Exception as exc:
            logger.error("Redis publish failed for task %s: %s", task_id, exc)

    async def _await_result(
        self, task_id: str, timeout: int = _DEFAULT_TASK_TIMEOUT
    ) -> str | None:
        """
        Wait for a sub-agent to publish its result on the per-task Redis channel.

        The sub-agent is expected to PUBLISH to:
            agentcore:bus:task:{task_id}
        with a JSON payload:
            {"task_id": "<uuid>", "result": "<text result>", "error": null | "..."}

        Returns the result string, or None on timeout.
        """
        result_channel = f"{_RESULT_CHANNEL_PREFIX}{task_id}"
        pubsub = self.redis.pubsub()
        try:
            await pubsub.subscribe(result_channel)
            loop = asyncio.get_running_loop()
            deadline = loop.time() + timeout

            async for raw_message in pubsub.listen():
                if loop.time() > deadline:
                    logger.warning(
                        "Timeout reached waiting for task %s on channel '%s'.",
                        task_id,
                        result_channel,
                    )
                    return None

                if raw_message.get("type") != "message":
                    continue

                try:
                    data = json.loads(raw_message["data"])
                except (json.JSONDecodeError, TypeError):
                    logger.warning("Malformed message on '%s': %s", result_channel, raw_message)
                    continue

                if data.get("task_id") != task_id:
                    continue  # not our message

                if data.get("error"):
                    logger.error(
                        "Sub-agent returned error for task %s: %s",
                        task_id,
                        data["error"],
                    )
                    return f"[ERROR] {data['error']}"

                return data.get("result", "")

            return None  # pubsub exhausted without matching message

        except asyncio.TimeoutError:
            return None
        finally:
            try:
                await pubsub.unsubscribe(result_channel)
                await pubsub.close()
            except Exception:
                pass

    # ------------------------------------------------------------------
    # Audit logging
    # ------------------------------------------------------------------

    async def audit_log(
        self,
        action: str,
        actor: str,
        details: dict,
    ) -> None:
        """
        Write an audit log entry to Redis (as a stream event).

        A separate consumer (e.g. a PostgreSQL writer) drains this stream.
        Stream key: agentcore:audit

        Args:
            action:  Short action identifier (e.g. "task_dispatched", "escalation").
            actor:   User or agent name responsible for the action.
            details: Arbitrary key-value details for the event.
        """
        entry = {
            "action": action,
            "actor": actor,
            "details": json.dumps(details),
        }
        try:
            await self.redis.xadd("agentcore:audit", entry)
            logger.debug("Audit log: action=%s actor=%s", action, actor)
        except Exception as exc:
            logger.error("Failed to write audit log entry: %s", exc)
