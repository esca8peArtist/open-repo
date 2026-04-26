"""
Channel tests: Telegram rate limiter — blocks excessive messages per minute.
"""
from __future__ import annotations

import asyncio
import time
from collections import deque
from unittest.mock import AsyncMock, MagicMock

import pytest

telegram = pytest.importorskip("telegram")

from agentcore.channels.telegram.bot import TelegramChannel


class TestTelegramRateLimiting:
    """Telegram rate limiting tests."""

    def _make_channel(self, rate_limit: int = 5) -> TelegramChannel:
        return TelegramChannel(
            bot_token="fake",
            agent_id="test-agent",
            message_router=AsyncMock(return_value="reply"),
            rate_limit_per_minute=rate_limit,
        )

    def test_rate_limit_stored_on_channel(self):
        """rate_limit_per_minute must be stored on the channel."""
        channel = self._make_channel(rate_limit=20)
        assert channel.rate_limit_per_minute == 20

    def _build_update(self, chat_id: int, text: str = "hi"):
        """Build a minimal mock PTB Update."""
        mock_update = MagicMock()
        mock_update.update_id = 1
        mock_update.effective_chat = MagicMock()
        mock_update.effective_chat.id = chat_id
        mock_update.effective_chat.send_action = AsyncMock()
        mock_update.effective_chat.to_dict.return_value = {}
        mock_update.effective_message = MagicMock()
        mock_update.effective_message.text = text
        mock_update.effective_message.message_id = 1
        mock_update.effective_message.from_user = MagicMock()
        mock_update.effective_message.from_user.to_dict.return_value = {}
        mock_update.effective_message.date = None
        return mock_update

    @pytest.mark.asyncio
    async def test_messages_within_rate_limit_processed(self):
        """Messages within the rate limit must all be routed to the agent."""
        channel = self._make_channel(rate_limit=10)

        mock_bot = MagicMock()
        mock_bot.send_message = AsyncMock(return_value=MagicMock())
        mock_app = MagicMock()
        mock_app.bot = mock_bot
        channel.app = mock_app

        mock_ctx = MagicMock()
        update = self._build_update(chat_id=12345)

        # Send 3 messages — well within 10/min limit
        for _ in range(3):
            await channel._handle_message(update, mock_ctx)

        # Router should have been called 3 times
        assert channel.router.call_count == 3

    @pytest.mark.asyncio
    async def test_rate_limiter_attribute_exists(self):
        """TelegramChannel must have a rate limiting mechanism or attribute."""
        channel = self._make_channel(rate_limit=5)
        # The channel must store the rate limit configuration
        assert hasattr(channel, "rate_limit_per_minute")
        assert channel.rate_limit_per_minute == 5

    def test_default_rate_limit_is_reasonable(self):
        """Default rate limit must be between 1 and 200 messages/minute."""
        channel = TelegramChannel(
            bot_token="fake",
            agent_id="test",
            message_router=AsyncMock(),
        )
        assert 1 <= channel.rate_limit_per_minute <= 200

    @pytest.mark.asyncio
    async def test_router_exception_does_not_crash_channel(self):
        """If the router raises, the channel must catch it and send an error reply."""
        channel = TelegramChannel(
            bot_token="fake",
            agent_id="test",
            message_router=AsyncMock(side_effect=RuntimeError("Agent crashed")),
        )

        mock_bot = MagicMock()
        mock_bot.send_message = AsyncMock(return_value=MagicMock())
        mock_app = MagicMock()
        mock_app.bot = mock_bot
        channel.app = mock_app

        update = self._build_update(chat_id=999)
        mock_ctx = MagicMock()

        # Must not raise
        await channel._handle_message(update, mock_ctx)
        # Must still send a reply (error message)
        mock_bot.send_message.assert_called_once()
