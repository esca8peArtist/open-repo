"""
Offline tests: Telegram and Twilio offline failures must not crash the agent.
"""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

telegram = pytest.importorskip("telegram")

from agentcore.channels.telegram.bot import TelegramChannel
from agentcore.channels.base import ChannelMessage
from agentcore.models import ChannelType


class TestTelegramOfflineDegradation:
    """Telegram must not crash the agent when it cannot reach Telegram servers."""

    def _make_channel(self) -> TelegramChannel:
        async def _router(msg: ChannelMessage) -> str:
            return "test reply"

        return TelegramChannel(
            bot_token="1234567890:FAKE_TOKEN",
            agent_id="test-agent",
            message_router=_router,
        )

    @pytest.mark.asyncio
    async def test_send_message_offline_returns_false_not_raise(self):
        """send_message must return False (not raise) when Telegram is unreachable."""
        channel = self._make_channel()

        # Simulate app being initialized but bot failing
        mock_bot = MagicMock()
        mock_bot.send_message = AsyncMock(side_effect=Exception("Network unreachable"))
        mock_app = MagicMock()
        mock_app.bot = mock_bot
        channel.app = mock_app

        result = await channel.send_message("123456", "Hello")
        assert result is False

    @pytest.mark.asyncio
    async def test_send_message_before_start_returns_false(self):
        """send_message before start() must return False."""
        channel = self._make_channel()
        # app is None (channel not started)
        assert channel.app is None
        result = await channel.send_message("123456", "Hi")
        assert result is False

    @pytest.mark.asyncio
    async def test_invalid_recipient_id_returns_false(self):
        """Non-integer recipient_id must return False without raising."""
        channel = self._make_channel()
        mock_app = MagicMock()
        channel.app = mock_app

        result = await channel.send_message("not-an-int", "Hello")
        assert result is False

    @pytest.mark.asyncio
    async def test_transcribe_audio_offline_returns_none(self):
        """_transcribe_audio must return None when STT endpoint is unreachable."""
        channel = self._make_channel()

        import httpx
        with patch("httpx.AsyncClient.post", side_effect=httpx.ConnectError("offline")):
            result = await channel._transcribe_audio(b"\x00\x01\x02", fmt="ogg")

        assert result is None

    @pytest.mark.asyncio
    async def test_stop_before_start_no_exception(self):
        """Calling stop() before start() must not raise."""
        channel = self._make_channel()
        await channel.stop()  # Should complete without exception

    def test_is_allowed_empty_list_allows_all(self):
        """With empty allowed_chat_ids, all chats must be allowed."""
        channel = self._make_channel()
        assert channel._is_allowed(12345) is True
        assert channel._is_allowed(0) is True
        assert channel._is_allowed(-1) is True

    def test_is_allowed_restrictive_list_blocks_unknown(self):
        """When allowed_chat_ids is set, unknown IDs must be blocked."""
        async def _router(msg):
            return "ok"

        channel = TelegramChannel(
            bot_token="fake",
            agent_id="test",
            message_router=_router,
            allowed_chat_ids=[111, 222],
        )
        assert channel._is_allowed(111) is True
        assert channel._is_allowed(333) is False


class TestTwilioOfflineDegradation:
    """Twilio offline failures must be handled gracefully."""

    @pytest.mark.asyncio
    async def test_twilio_send_sms_offline_returns_error(self):
        """SMS send failure must return an error result, not raise."""
        from agentcore.channels.twilio.sms import TwilioSMSChannel

        async def _router(msg):
            return "ok"

        channel = TwilioSMSChannel(
            account_sid="ACtest",
            auth_token="authtoken",
            from_number="+15550000",
            message_router=_router,
        )

        with patch("agentcore.channels.twilio.sms.Client") as mock_client_cls:
            mock_client = MagicMock()
            mock_client.messages.create.side_effect = Exception("Network unreachable")
            mock_client_cls.return_value = mock_client

            result = await channel.send_message("+15551111", "Test message")

        assert result is False

    @pytest.mark.asyncio
    async def test_twilio_channel_handles_missing_credentials(self):
        """Missing Twilio credentials must result in graceful error, not crash."""
        from agentcore.channels.twilio.sms import TwilioSMSChannel

        async def _router(msg):
            return "ok"

        channel = TwilioSMSChannel(
            account_sid="",  # missing
            auth_token="",   # missing
            from_number="+15550000",
            message_router=_router,
        )

        result = await channel.send_message("+15551111", "Test")
        assert result is False
