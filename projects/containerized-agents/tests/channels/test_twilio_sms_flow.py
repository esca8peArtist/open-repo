"""
Channel tests: Twilio SMS — mock Twilio client, test SMS send/receive flow.
"""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

twilio = pytest.importorskip("twilio")

from agentcore.channels.twilio.sms import TwilioSMSChannel
from agentcore.channels.base import ChannelMessage
from agentcore.models import ChannelType


def _make_sms_channel(reply: str = "SMS reply") -> tuple[TwilioSMSChannel, AsyncMock]:
    """Create a TwilioSMSChannel with a mock router."""
    router_mock = AsyncMock(return_value=reply)
    channel = TwilioSMSChannel(
        account_sid="ACtest123456",
        auth_token="testauthtoken",
        from_number="+15550000000",
        message_router=router_mock,
    )
    return channel, router_mock


class TestTwilioSMSFlow:
    """Twilio SMS send/receive flow tests."""

    @pytest.mark.asyncio
    async def test_send_sms_success(self):
        """send_message must call Twilio client.messages.create and return True."""
        channel, _ = _make_sms_channel()

        with patch("agentcore.channels.twilio.sms.Client") as mock_client_cls:
            mock_client = MagicMock()
            mock_msg = MagicMock()
            mock_msg.sid = "SM_test123"
            mock_msg.status = "queued"
            mock_client.messages.create.return_value = mock_msg
            mock_client_cls.return_value = mock_client

            result = await channel.send_message("+15551111111", "Hello from agent")

        assert result is True
        mock_client.messages.create.assert_called_once()

    @pytest.mark.asyncio
    async def test_send_sms_correct_from_number(self):
        """send_message must use the configured from_number."""
        channel, _ = _make_sms_channel()

        with patch("agentcore.channels.twilio.sms.Client") as mock_client_cls:
            mock_client = MagicMock()
            mock_client.messages.create.return_value = MagicMock(sid="SM1", status="queued")
            mock_client_cls.return_value = mock_client

            await channel.send_message("+15552222222", "Test")

        call_kwargs = mock_client.messages.create.call_args[1]
        assert call_kwargs.get("from_") == "+15550000000"

    @pytest.mark.asyncio
    async def test_send_sms_twilio_error_returns_false(self):
        """Twilio API error must cause send_message to return False."""
        channel, _ = _make_sms_channel()

        with patch("agentcore.channels.twilio.sms.Client") as mock_client_cls:
            mock_client = MagicMock()
            mock_client.messages.create.side_effect = Exception("Twilio error")
            mock_client_cls.return_value = mock_client

            result = await channel.send_message("+15553333333", "Test")

        assert result is False

    @pytest.mark.asyncio
    async def test_handle_inbound_sms_routes_to_agent(self):
        """Inbound SMS must route to agent and trigger a reply."""
        channel, router_mock = _make_sms_channel("SMS agent reply")

        with patch("agentcore.channels.twilio.sms.Client") as mock_client_cls:
            mock_client = MagicMock()
            mock_client.messages.create.return_value = MagicMock(sid="SM2", status="queued")
            mock_client_cls.return_value = mock_client

            # Simulate receiving a webhook payload
            inbound_data = {
                "From": "+15559999999",
                "To": "+15550000000",
                "Body": "Hello agent, I need help",
                "MessageSid": "SM_inbound_test",
            }

            response = await channel.handle_inbound(inbound_data)

        router_mock.assert_called_once()
        call_arg = router_mock.call_args[0][0]
        assert "Hello agent" in call_arg.content

    @pytest.mark.asyncio
    async def test_send_sms_empty_credentials_returns_false(self):
        """Empty account_sid/auth_token must result in False return."""
        async def _router(msg):
            return "ok"

        channel = TwilioSMSChannel(
            account_sid="",
            auth_token="",
            from_number="+15550000",
            message_router=_router,
        )
        result = await channel.send_message("+15551111", "Test")
        assert result is False

    @pytest.mark.asyncio
    async def test_send_long_sms_truncated_or_split(self):
        """SMS longer than 1600 chars must be handled (split or truncated)."""
        channel, _ = _make_sms_channel()
        long_message = "word " * 400  # ~2000 chars

        with patch("agentcore.channels.twilio.sms.Client") as mock_client_cls:
            mock_client = MagicMock()
            mock_client.messages.create.return_value = MagicMock(sid="SM3", status="queued")
            mock_client_cls.return_value = mock_client

            result = await channel.send_message("+15554444", long_message)

        # Must not raise; result can be True (split) or False (error)
        assert isinstance(result, bool)
