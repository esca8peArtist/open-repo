"""
MessageRouter — routes inbound ChannelMessages to the correct AgentInstance.

Responsibilities:
- Map (channel, sender_id) pairs to agent configurations
- Enforce per-channel priority (voice/web > telegram > sms)
- Use Redis queues for async channels (SMS, Telegram) to decouple delivery
- Handle rate limiting at the routing layer
- Maintain session continuity across messages from the same sender

Priority model:
    HIGH   — voice, web chat (synchronous; callers block for response)
    NORMAL — Telegram (polling/webhook; near-real-time expected)
    LOW    — SMS, WhatsApp (async; best-effort delivery)
"""
from __future__ import annotations

import asyncio
import logging
from enum import IntEnum
from typing import TYPE_CHECKING, Any

from agentcore.channels.base import ChannelMessage
from agentcore.models import ChannelType

if TYPE_CHECKING:
    from agentcore.core.agent import AgentInstance
    from agentcore.core.registry import AgentRegistry

logger = logging.getLogger(__name__)


class ChannelPriority(IntEnum):
    HIGH = 1
    NORMAL = 2
    LOW = 3


# Default priority mapping by channel type
_CHANNEL_PRIORITY: dict[ChannelType, ChannelPriority] = {
    ChannelType.VOICE: ChannelPriority.HIGH,
    ChannelType.WEB: ChannelPriority.HIGH,
    ChannelType.TELEGRAM: ChannelPriority.NORMAL,
    ChannelType.SMS: ChannelPriority.LOW,
    ChannelType.WHATSAPP: ChannelPriority.LOW,
}

# Simple rate limit: max N messages per sender per minute
_DEFAULT_RATE_LIMIT = 30  # messages per minute


class _RateLimiter:
    """Token-bucket rate limiter per sender_id, held entirely in memory."""

    def __init__(self, limit: int, window_seconds: int = 60) -> None:
        self._limit = limit
        self._window = window_seconds
        self._counts: dict[str, list[float]] = {}

    def is_allowed(self, key: str) -> bool:
        import time

        now = time.monotonic()
        window_start = now - self._window
        bucket = [t for t in self._counts.get(key, []) if t > window_start]
        if len(bucket) >= self._limit:
            return False
        bucket.append(now)
        self._counts[key] = bucket
        return True


class MessageRouter:
    """
    Routes inbound ChannelMessages to the appropriate AgentInstance.

    Usage:
        router = MessageRouter(registry)
        response_text = await router.route(channel_message)
    """

    def __init__(
        self,
        registry: AgentRegistry,
        redis_client: Any | None = None,
        rate_limit: int = _DEFAULT_RATE_LIMIT,
    ) -> None:
        self._registry = registry
        self._redis = redis_client
        self._rate_limiter = _RateLimiter(rate_limit)

        # Mapping: (channel_type, sender_id) -> agent_id
        # Populated from agent configs at startup and updated dynamically.
        self._routing_table: dict[tuple[str, str], str] = {}

        # Session continuity: sender_key -> session_id
        self._sessions: dict[str, str] = {}

        # In-flight async tasks for LOW priority channels
        self._background_tasks: set[asyncio.Task] = set()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    async def route(self, message: ChannelMessage) -> str:
        """
        Route a ChannelMessage to the appropriate agent and return response text.

        For HIGH priority channels: waits synchronously for the response.
        For NORMAL/LOW priority channels: queues via Redis (or asyncio Task if
        Redis is unavailable) and returns an acknowledgement string immediately.
        """
        rate_key = f"{message.channel}:{message.sender_id}"
        if not self._rate_limiter.is_allowed(rate_key):
            logger.warning("Rate limit exceeded for %s", rate_key)
            return "Too many messages. Please slow down."

        priority = _CHANNEL_PRIORITY.get(ChannelType(message.channel), ChannelPriority.NORMAL)

        if priority == ChannelPriority.HIGH:
            # Synchronous path — caller blocks for full response
            return await self._process_message(message)

        # Async path — push to Redis queue or background task
        if self._redis is not None:
            await self._enqueue_redis(message, priority)
        else:
            task = asyncio.create_task(self._process_message(message))
            self._background_tasks.add(task)
            task.add_done_callback(self._background_tasks.discard)

        return "Message received. Reply incoming shortly."

    async def rebuild_routing_table(self) -> None:
        """
        Rebuild the (channel, sender_id) -> agent_id routing table from
        all active agent configs.

        Called at startup and whenever agent configs are modified.
        """
        agents = await self._registry.list_agents()
        table: dict[tuple[str, str], str] = {}

        for cfg in agents:
            for channel_cfg in cfg.channels:
                if not channel_cfg.enabled:
                    continue
                # Each channel config may specify a set of allowed sender_ids.
                # An empty list means "catch-all" — represented by the wildcard "*".
                sender_ids: list[str] = channel_cfg.config.get("sender_ids", ["*"])
                for sid in sender_ids:
                    key = (channel_cfg.channel_type.value, sid)
                    table[key] = cfg.id

        self._routing_table = table
        logger.info("Routing table rebuilt — %d routes", len(table))

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    async def _process_message(self, message: ChannelMessage) -> str:
        """Find the agent, resolve the session, call agent.chat(), return text."""
        try:
            agent = await self._get_agent_for_channel(
                message.channel, message.sender_id
            )
            if agent is None:
                logger.warning(
                    "No agent found for channel=%s sender=%s",
                    message.channel,
                    message.sender_id,
                )
                return "No agent is configured to handle this channel."

            session_id = self._get_or_create_session(message.channel, message.sender_id)
            response = await agent.chat(message.content, session_id=session_id, stream=False)
            return response.message

        except Exception as exc:
            logger.exception("Error processing message from %s/%s: %s", message.channel, message.sender_id, exc)
            return "An error occurred while processing your message. Please try again."

    async def _get_agent_for_channel(
        self, channel: str, sender_id: str
    ) -> AgentInstance | None:
        """
        Look up the agent that should handle a message from (channel, sender_id).

        Lookup order:
        1. Exact match (channel, sender_id)
        2. Wildcard match (channel, "*")
        3. First active agent as fallback (single-agent setups)
        """
        # Exact match
        agent_id = self._routing_table.get((channel, sender_id))
        if agent_id is None:
            # Wildcard match
            agent_id = self._routing_table.get((channel, "*"))

        if agent_id is not None:
            return await self._registry.get_agent(agent_id)

        # Fallback: return the first active agent (common in single-agent setups)
        all_agents = await self._registry.list_agents()
        for cfg in all_agents:
            if cfg.active:
                return await self._registry.get_agent(cfg.id)

        return None

    def _get_or_create_session(self, channel: str, sender_id: str) -> str:
        """Return a stable session_id for a (channel, sender_id) pair."""
        import uuid

        key = f"{channel}:{sender_id}"
        if key not in self._sessions:
            self._sessions[key] = str(uuid.uuid4())
        return self._sessions[key]

    async def _enqueue_redis(self, message: ChannelMessage, priority: ChannelPriority) -> None:
        """Push a ChannelMessage onto a Redis priority queue for async processing."""
        import json

        queue_name = f"agentcore:queue:{priority.name.lower()}"
        payload = json.dumps(
            {
                "channel": message.channel,
                "sender_id": message.sender_id,
                "content": message.content,
                "session_id": message.session_id,
                "metadata": message.metadata,
            }
        )
        try:
            await self._redis.lpush(queue_name, payload)
            logger.debug("Enqueued message to %s", queue_name)
        except Exception as exc:
            logger.error("Failed to enqueue message to Redis: %s", exc)
            # Fallback to background task
            task = asyncio.create_task(self._process_message(message))
            self._background_tasks.add(task)
            task.add_done_callback(self._background_tasks.discard)
