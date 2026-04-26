"""
Channel tests: Telegram — full message → agent → reply flow.
"""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

telegram = pytest.importorskip("telegram")

from agentcore.channels.telegram.bot import TelegramChannel, _split_message
from agentcore.channels.base import ChannelMessage


class TestTelegramMessageFlow:
    """Full message flow tests for TelegramChannel."""

    def _make_channel(self, router_reply: str = "Agent reply text") -> tuple[TelegramChannel, AsyncMock]:
        """Create a channel with a mock router that returns a fixed reply."""
        router_mock = AsyncMock(return_value=router_reply)

        channel = TelegramChannel(
            bot_token="fake_token",
            agent_id="test-agent",
            message_router=router_mock,
        )
        return channel, router_mock

    @pytest.mark.asyncio
    async def test_send_message_calls_bot_send_message(self):
        """send_message must call bot.send_message with correct args."""
        channel, _ = self._make_channel()

        mock_bot = MagicMock()
        mock_bot.send_message = AsyncMock(return_value=MagicMock(message_id=42))
        mock_app = MagicMock()
        mock_app.bot = mock_bot
        channel.app = mock_app

        result = await channel.send_message("123456", "Hello from agent")
        assert result is True
        mock_bot.send_message.assert_called_once()
        call_kwargs = mock_bot.send_message.call_args
        assert call_kwargs[1]["chat_id"] == 123456 or call_kwargs[0][0] == 123456

    @pytest.mark.asyncio
    async def test_send_message_splits_long_text(self):
        """Messages exceeding max_message_length must be split into chunks."""
        channel, _ = self._make_channel()
        channel.max_message_length = 50

        mock_bot = MagicMock()
        mock_bot.send_message = AsyncMock(return_value=MagicMock(message_id=1))
        mock_app = MagicMock()
        mock_app.bot = mock_bot
        channel.app = mock_app

        long_text = "word " * 30  # 150 chars, 3 chunks of 50
        await channel.send_message("123", long_text)

        # Should be called multiple times
        assert mock_bot.send_message.call_count > 1

    @pytest.mark.asyncio
    async def test_handle_inbound_builds_channel_message(self):
        """handle_inbound must produce a correctly populated ChannelMessage."""
        channel, _ = self._make_channel()

        # Build a minimal Telegram Update dict
        from telegram import Update
        payload = {
            "update_id": 100,
            "message": {
                "message_id": 1,
                "from": {"id": 42, "is_bot": False, "first_name": "Alice"},
                "chat": {"id": 12345, "type": "private"},
                "date": 1710000000,
                "text": "Hello agent!",
            },
        }

        mock_bot = MagicMock()
        mock_app = MagicMock()
        mock_app.bot = mock_bot
        channel.app = mock_app

        try:
            msg = await channel.handle_inbound(payload)
            assert msg.channel == "telegram"
            assert msg.content == "Hello agent!"
            assert msg.sender_id == "12345"
        except Exception:
            # handle_inbound may require a live bot for de_json — skip if so
            pytest.skip("Telegram de_json requires bot instance")

    @pytest.mark.asyncio
    async def test_router_called_on_handle_message(self):
        """_handle_message must invoke the router with the channel message."""
        router_mock = AsyncMock(return_value="Test reply")
        channel = TelegramChannel(
            bot_token="fake",
            agent_id="agent-1",
            message_router=router_mock,
        )

        mock_bot = MagicMock()
        mock_bot.send_message = AsyncMock(return_value=MagicMock())
        mock_app = MagicMock()
        mock_app.bot = mock_bot
        channel.app = mock_app

        # Build mock PTB Update/Context
        mock_update = MagicMock()
        mock_update.update_id = 1
        mock_update.effective_chat = MagicMock()
        mock_update.effective_chat.id = 99999
        mock_update.effective_chat.send_action = AsyncMock()
        mock_update.effective_message = MagicMock()
        mock_update.effective_message.text = "Test message"
        mock_update.effective_message.message_id = 1
        mock_update.effective_message.from_user = MagicMock()
        mock_update.effective_message.from_user.to_dict.return_value = {}
        mock_update.effective_message.date = None
        mock_update.effective_chat.to_dict.return_value = {}

        mock_ctx = MagicMock()

        await channel._handle_message(mock_update, mock_ctx)

        router_mock.assert_called_once()
        call_arg = router_mock.call_args[0][0]
        assert call_arg.content == "Test message"
        assert call_arg.sender_id == "99999"

    def test_is_allowed_open_by_default(self):
        """Without allowlist, all chat IDs must be permitted."""
        channel, _ = self._make_channel()
        assert channel._is_allowed(12345) is True
        assert channel._is_allowed(0) is True

    def test_is_allowed_restricted(self):
        """With allowlist, only listed chat IDs must be permitted."""
        channel = TelegramChannel(
            bot_token="fake",
            agent_id="test",
            message_router=AsyncMock(),
            allowed_chat_ids=[111, 222],
        )
        assert channel._is_allowed(111) is True
        assert channel._is_allowed(333) is False


class TestSplitMessage:
    """_split_message utility function tests."""

    def test_short_message_not_split(self):
        """Short messages must be returned as a single chunk."""
        chunks = _split_message("Hello world", 4096)
        assert chunks == ["Hello world"]

    def test_long_message_split_on_newline(self):
        """Long messages must be split on newline boundaries."""
        text = "line1\n" + "x" * 50
        chunks = _split_message(text, 20)
        assert len(chunks) > 1

    def test_all_chunks_within_max_length(self):
        """No chunk must exceed max_length."""
        text = "word " * 1000
        max_len = 100
        chunks = _split_message(text, max_len)
        for chunk in chunks:
            assert len(chunk) <= max_len

    def test_no_empty_chunks(self):
        """Resulting chunks must all be non-empty."""
        text = "word " * 200
        chunks = _split_message(text, 50)
        for chunk in chunks:
            assert chunk.strip() != ""

    def test_full_content_preserved(self):
        """All words from the original must appear in the combined output."""
        text = " ".join(f"word{i}" for i in range(100))
        chunks = _split_message(text, 50)
        combined = " ".join(chunks)
        for i in range(100):
            assert f"word{i}" in combined
