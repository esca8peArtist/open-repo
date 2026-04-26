"""
Integration tests for Telegram and Twilio channel setup, teardown, and messaging.
"""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from agentcore.channels.base import ChannelMessage

try:
    from agentcore.channels.telegram.bot import TelegramChannel, _split_message
    _TELEGRAM_AVAILABLE = True
except ImportError:
    _TELEGRAM_AVAILABLE = False
    TelegramChannel = None  # type: ignore[assignment,misc]
    _split_message = None  # type: ignore[assignment]

try:
    from agentcore.channels.twilio.sms import TwilioSMSChannel, _split_sms
    _TWILIO_AVAILABLE = True
except ImportError:
    _TWILIO_AVAILABLE = False
    TwilioSMSChannel = None  # type: ignore[assignment,misc]
    _split_sms = None  # type: ignore[assignment]

pytestmark_telegram = pytest.mark.skipif(
    not _TELEGRAM_AVAILABLE, reason="python-telegram-bot not installed"
)
pytestmark_twilio = pytest.mark.skipif(
    not _TWILIO_AVAILABLE, reason="twilio not installed"
)


# ===========================================================================
# TelegramChannel — setup / teardown
# ===========================================================================


@pytest.mark.skipif(not _TELEGRAM_AVAILABLE, reason="python-telegram-bot not installed")
class TestTelegramChannelLifecycle:
    @pytest.mark.asyncio
    async def test_start_stop_lifecycle(self):
        """TelegramChannel.start() / stop() must complete without raising."""

        async def _dummy_router(msg: ChannelMessage) -> str:
            return "reply"

        channel = TelegramChannel(
            bot_token="fake:TOKEN",
            agent_id="test-agent",
            message_router=_dummy_router,
        )

        # Mock the Application to avoid real Telegram API calls
        mock_app = MagicMock()
        mock_app.initialize = AsyncMock()
        mock_app.start = AsyncMock()
        mock_updater = MagicMock()
        mock_updater.start_polling = AsyncMock()
        mock_updater.stop = AsyncMock()
        mock_app.updater = mock_updater
        mock_app.stop = AsyncMock()
        mock_app.shutdown = AsyncMock()
        mock_app.add_handler = MagicMock()
        mock_app.bot = MagicMock()

        with patch("agentcore.channels.telegram.bot.Application") as mock_builder:
            mock_builder.builder.return_value.token.return_value.build.return_value = mock_app
            await channel.start()

        assert channel._running is True

        await channel.stop()
        assert channel._running is False

    @pytest.mark.asyncio
    async def test_double_start_is_idempotent(self):
        """Calling start() twice must not raise or create duplicate polling tasks."""

        async def _dummy_router(msg: ChannelMessage) -> str:
            return "reply"

        channel = TelegramChannel(
            bot_token="fake:TOKEN",
            agent_id="test-agent",
            message_router=_dummy_router,
        )
        channel._running = True  # Simulate already started

        # Should log a warning and return without error
        await channel.start()
        assert channel._running is True

    @pytest.mark.asyncio
    async def test_stop_when_not_running_is_safe(self):
        """Calling stop() on a channel that was never started must not raise."""

        async def _dummy_router(msg: ChannelMessage) -> str:
            return "reply"

        channel = TelegramChannel(
            bot_token="fake:TOKEN",
            agent_id="test-agent",
            message_router=_dummy_router,
        )
        # Should not raise
        await channel.stop()


# ===========================================================================
# TelegramChannel — send_message
# ===========================================================================


@pytest.mark.skipif(not _TELEGRAM_AVAILABLE, reason="python-telegram-bot not installed")
class TestTelegramSendMessage:
    @pytest.mark.asyncio
    async def test_send_message_returns_false_when_not_started(self):
        """send_message must return False if the channel hasn't been started."""

        async def _dummy_router(msg: ChannelMessage) -> str:
            return "reply"

        channel = TelegramChannel(
            bot_token="fake:TOKEN",
            agent_id="test",
            message_router=_dummy_router,
        )
        result = await channel.send_message("123456", "Hello")
        assert result is False

    @pytest.mark.asyncio
    async def test_send_message_splits_long_text(self):
        """Messages longer than max_message_length must be split into multiple sends."""
        async def _dummy_router(msg: ChannelMessage) -> str:
            return "reply"

        channel = TelegramChannel(
            bot_token="fake:TOKEN",
            agent_id="test",
            message_router=_dummy_router,
            max_message_length=20,
        )
        channel._running = True

        mock_bot = AsyncMock()
        mock_bot.send_message = AsyncMock()
        mock_app = MagicMock()
        mock_app.bot = mock_bot
        channel.app = mock_app

        long_text = "This is a very long message that will need to be split into multiple parts."
        await channel.send_message("123456", long_text)

        # Should have been called more than once
        assert mock_bot.send_message.call_count >= 2

    def test_allowed_chat_ids_restriction(self):
        """When allowed_chat_ids is set, non-allowed IDs must be rejected."""

        async def _dummy_router(msg: ChannelMessage) -> str:
            return "reply"

        channel = TelegramChannel(
            bot_token="fake:TOKEN",
            agent_id="test",
            message_router=_dummy_router,
            allowed_chat_ids=[111, 222],
        )

        assert channel._is_allowed(111) is True
        assert channel._is_allowed(222) is True
        assert channel._is_allowed(999) is False

    def test_no_restriction_when_allowed_chat_ids_empty(self):
        """When allowed_chat_ids is empty (default), all IDs are allowed."""

        async def _dummy_router(msg: ChannelMessage) -> str:
            return "reply"

        channel = TelegramChannel(
            bot_token="fake:TOKEN",
            agent_id="test",
            message_router=_dummy_router,
        )

        assert channel._is_allowed(999) is True
        assert channel._is_allowed(0) is True


# ===========================================================================
# TelegramChannel — inbound parsing
# ===========================================================================


@pytest.mark.skipif(not _TELEGRAM_AVAILABLE, reason="python-telegram-bot not installed")
class TestTelegramInboundParsing:
    @pytest.mark.asyncio
    async def test_handle_inbound_parses_update(self):
        """handle_inbound must convert a Telegram Update dict to ChannelMessage."""
        from telegram import Update

        async def _dummy_router(msg: ChannelMessage) -> str:
            return "reply"

        channel = TelegramChannel(
            bot_token="fake:TOKEN",
            agent_id="test",
            message_router=_dummy_router,
        )

        # Use a real Update dict format (minimal)
        update_dict = {
            "update_id": 1000,
            "message": {
                "message_id": 1,
                "date": 1709000000,
                "chat": {"id": 123456, "type": "private"},
                "from": {"id": 123456, "first_name": "Test", "is_bot": False},
                "text": "Hello bot!",
            },
        }

        mock_bot = MagicMock()
        mock_app = MagicMock()
        mock_app.bot = mock_bot
        channel.app = mock_app

        with patch("telegram.Update.de_json") as mock_de_json:
            mock_update = MagicMock()
            mock_update.effective_message.text = "Hello bot!"
            mock_update.effective_message.chat_id = 123456
            mock_update.effective_message.caption = None
            mock_update.effective_message.from_user.to_dict.return_value = {}
            mock_update.effective_message.chat.to_dict.return_value = {}
            mock_update.effective_message.message_id = 1
            mock_update.effective_message.date = None
            mock_update.update_id = 1000
            mock_de_json.return_value = mock_update

            msg = await channel.handle_inbound(update_dict)

        assert msg.channel == "telegram"
        assert msg.sender_id == "123456"
        assert msg.content == "Hello bot!"


# ===========================================================================
# TwilioSMSChannel — setup / teardown
# ===========================================================================


@pytest.mark.skipif(not _TWILIO_AVAILABLE, reason="twilio not installed")
class TestTwilioChannelLifecycle:
    @pytest.mark.asyncio
    async def test_start_initialises_client(self):
        """TwilioSMSChannel.start() must initialise the Twilio Client."""

        async def _dummy_router(msg: ChannelMessage) -> str:
            return "reply"

        channel = TwilioSMSChannel(
            account_sid="ACfake123",
            auth_token="fake_auth_token",
            phone_number="+15550000001",
            agent_id="test-agent",
            message_router=_dummy_router,
        )

        with patch("agentcore.channels.twilio.sms.Client") as mock_client_class:
            with patch("agentcore.channels.twilio.sms.RequestValidator") as mock_validator:
                await channel.start()

        assert channel._running is True
        assert channel._client is not None

    @pytest.mark.asyncio
    async def test_stop_clears_client(self):
        """TwilioSMSChannel.stop() must clear the Twilio client."""

        async def _dummy_router(msg: ChannelMessage) -> str:
            return "reply"

        channel = TwilioSMSChannel(
            account_sid="ACfake123",
            auth_token="fake_auth_token",
            phone_number="+15550000001",
            agent_id="test-agent",
            message_router=_dummy_router,
        )

        with patch("agentcore.channels.twilio.sms.Client"):
            with patch("agentcore.channels.twilio.sms.RequestValidator"):
                await channel.start()
                await channel.stop()

        assert channel._running is False
        assert channel._client is None

    @pytest.mark.asyncio
    async def test_stop_without_start_is_safe(self):
        """Calling stop() before start() must not raise."""

        async def _dummy_router(msg: ChannelMessage) -> str:
            return "reply"

        channel = TwilioSMSChannel(
            account_sid="ACfake123",
            auth_token="fake_auth",
            phone_number="+15550000001",
            agent_id="test-agent",
            message_router=_dummy_router,
        )
        await channel.stop()  # Must not raise


# ===========================================================================
# TwilioSMSChannel — inbound / outbound
# ===========================================================================


@pytest.mark.skipif(not _TWILIO_AVAILABLE, reason="twilio not installed")
class TestTwilioSMSMessaging:
    @pytest.mark.asyncio
    async def test_handle_inbound_parses_form_payload(self):
        """handle_inbound must convert a Twilio form POST payload to ChannelMessage."""

        async def _dummy_router(msg: ChannelMessage) -> str:
            return "reply"

        channel = TwilioSMSChannel(
            account_sid="ACtest",
            auth_token="test_auth",
            phone_number="+15550000001",
            agent_id="agent-1",
            message_router=_dummy_router,
        )

        payload = {
            "From": "+15550000002",
            "To": "+15550000001",
            "Body": "Order status?",
            "MessageSid": "SM_TEST_123",
            "NumSegments": "1",
            "NumMedia": "0",
            "AccountSid": "ACtest",
        }

        msg = await channel.handle_inbound(payload)

        assert msg.sender_id == "+15550000002"
        assert msg.content == "Order status?"
        assert msg.channel == "sms"
        assert msg.metadata["message_sid"] == "SM_TEST_123"

    @pytest.mark.asyncio
    async def test_send_message_when_not_running_returns_false(self):
        """send_message when channel is not running must return False."""

        async def _dummy_router(msg: ChannelMessage) -> str:
            return "reply"

        channel = TwilioSMSChannel(
            account_sid="ACtest",
            auth_token="test",
            phone_number="+15550000001",
            agent_id="test",
            message_router=_dummy_router,
        )
        result = await channel.send_message("+15550000002", "Hello")
        assert result is False

    def test_signature_validation_rejects_bad_signature(self):
        """validate_signature with wrong signature must return False."""

        async def _dummy_router(msg: ChannelMessage) -> str:
            return "reply"

        channel = TwilioSMSChannel(
            account_sid="ACtest",
            auth_token="test_auth_token",
            phone_number="+15550000001",
            agent_id="test",
            message_router=_dummy_router,
        )

        # Set up the validator via mock
        mock_validator = MagicMock()
        mock_validator.validate.return_value = False
        channel._validator = mock_validator

        result = channel.validate_signature(
            request_url="https://example.com/webhook/sms",
            params={"From": "+1555", "Body": "test"},
            signature="bad_signature",
        )
        assert result is False

    def test_signature_validation_accepts_correct_signature(self):
        """validate_signature with a correct signature must return True."""

        async def _dummy_router(msg: ChannelMessage) -> str:
            return "reply"

        channel = TwilioSMSChannel(
            account_sid="ACtest",
            auth_token="test_auth_token",
            phone_number="+15550000001",
            agent_id="test",
            message_router=_dummy_router,
        )

        mock_validator = MagicMock()
        mock_validator.validate.return_value = True
        channel._validator = mock_validator

        result = channel.validate_signature(
            request_url="https://example.com/webhook/sms",
            params={"From": "+1555", "Body": "test"},
            signature="correct_signature",
        )
        assert result is True
