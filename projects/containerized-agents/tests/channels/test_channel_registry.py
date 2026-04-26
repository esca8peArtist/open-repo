"""
Channel registry tests: BaseChannel start/stop lifecycle, multiple channels.
"""
from __future__ import annotations

from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from agentcore.channels.base import BaseChannel, ChannelMessage


# ---------------------------------------------------------------------------
# Concrete test implementations of BaseChannel
# ---------------------------------------------------------------------------


class FakeChannel(BaseChannel):
    """Minimal concrete channel for lifecycle testing."""

    channel_name = "fake"
    requires_internet = True

    def __init__(self):
        self.started = False
        self.stopped = False
        self.sent_messages: list[tuple[str, str]] = []

    async def start(self) -> None:
        self.started = True

    async def stop(self) -> None:
        self.stopped = True

    async def send_message(self, recipient_id: str, text: str, **kwargs: Any) -> bool:
        self.sent_messages.append((recipient_id, text))
        return True

    async def handle_inbound(self, raw_payload: dict[str, Any]) -> ChannelMessage:
        return ChannelMessage(
            channel=self.channel_name,
            sender_id=raw_payload.get("from", "unknown"),
            content=raw_payload.get("text", ""),
        )


class FaultyChanelThatFailsStart(BaseChannel):
    """Channel that raises on start()."""

    channel_name = "faulty"
    requires_internet = True

    async def start(self) -> None:
        raise RuntimeError("Connection refused")

    async def stop(self) -> None:
        pass  # stop is always safe

    async def send_message(self, recipient_id: str, text: str, **kwargs: Any) -> bool:
        return False

    async def handle_inbound(self, raw_payload: dict[str, Any]) -> ChannelMessage:
        return ChannelMessage(channel=self.channel_name, sender_id="", content="")


class OfflineChannel(BaseChannel):
    """Channel that declares it does NOT require internet."""

    channel_name = "local_bus"
    requires_internet = False

    async def start(self) -> None:
        pass

    async def stop(self) -> None:
        pass

    async def send_message(self, recipient_id: str, text: str, **kwargs: Any) -> bool:
        return True

    async def handle_inbound(self, raw_payload: dict[str, Any]) -> ChannelMessage:
        return ChannelMessage(channel=self.channel_name, sender_id="local", content="msg")


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestBaseChannelLifecycle:
    """Start / stop lifecycle tests for BaseChannel subclasses."""

    @pytest.mark.asyncio
    async def test_start_sets_started_flag(self):
        """start() must be callable and mark the channel as started."""
        ch = FakeChannel()
        assert ch.started is False
        await ch.start()
        assert ch.started is True

    @pytest.mark.asyncio
    async def test_stop_sets_stopped_flag(self):
        """stop() must be callable after start()."""
        ch = FakeChannel()
        await ch.start()
        await ch.stop()
        assert ch.stopped is True

    @pytest.mark.asyncio
    async def test_stop_safe_without_start(self):
        """stop() must not raise even if start() was never called."""
        ch = FakeChannel()
        await ch.stop()  # must not raise
        assert ch.stopped is True

    @pytest.mark.asyncio
    async def test_faulty_start_raises(self):
        """Channels with unrecoverable config errors must raise on start()."""
        ch = FaultyChanelThatFailsStart()
        with pytest.raises(RuntimeError, match="Connection refused"):
            await ch.start()

    @pytest.mark.asyncio
    async def test_faulty_stop_is_safe(self):
        """stop() on a channel that failed to start must not raise."""
        ch = FaultyChanelThatFailsStart()
        await ch.stop()  # must not raise

    @pytest.mark.asyncio
    async def test_channel_name_attribute(self):
        """channel_name must be set on concrete subclasses."""
        ch = FakeChannel()
        assert ch.channel_name == "fake"

    @pytest.mark.asyncio
    async def test_requires_internet_attribute(self):
        """requires_internet must reflect the channel's online requirement."""
        online_ch = FakeChannel()
        offline_ch = OfflineChannel()
        assert online_ch.requires_internet is True
        assert offline_ch.requires_internet is False


class TestBaseChannelMessaging:
    """send_message and handle_inbound tests."""

    @pytest.mark.asyncio
    async def test_send_message_returns_true_on_success(self):
        """send_message must return True on success."""
        ch = FakeChannel()
        result = await ch.send_message("user-123", "Hello!")
        assert result is True

    @pytest.mark.asyncio
    async def test_send_message_records_outbound(self):
        """send_message must dispatch the correct text to the correct recipient."""
        ch = FakeChannel()
        await ch.send_message("recipient-1", "First message")
        await ch.send_message("recipient-2", "Second message")
        assert ("recipient-1", "First message") in ch.sent_messages
        assert ("recipient-2", "Second message") in ch.sent_messages

    @pytest.mark.asyncio
    async def test_handle_inbound_returns_channel_message(self):
        """handle_inbound must return a ChannelMessage with correct fields."""
        ch = FakeChannel()
        payload = {"from": "user-abc", "text": "incoming message"}
        msg = await ch.handle_inbound(payload)
        assert isinstance(msg, ChannelMessage)
        assert msg.sender_id == "user-abc"
        assert msg.content == "incoming message"
        assert msg.channel == "fake"

    @pytest.mark.asyncio
    async def test_handle_inbound_missing_fields_default_gracefully(self):
        """handle_inbound must handle missing payload fields gracefully."""
        ch = FakeChannel()
        msg = await ch.handle_inbound({})
        assert isinstance(msg, ChannelMessage)
        assert msg.sender_id == "unknown"
        assert msg.content == ""

    @pytest.mark.asyncio
    async def test_faulty_channel_send_returns_false(self):
        """send_message must return False (not raise) when channel is broken."""
        ch = FaultyChanelThatFailsStart()
        result = await ch.send_message("someone", "hello")
        assert result is False


class TestMultiChannelRegistry:
    """Simulate a simple channel registry managing multiple channels."""

    @pytest.mark.asyncio
    async def test_start_all_channels(self):
        """Starting all channels in a registry must call start on each."""
        channels: list[BaseChannel] = [FakeChannel(), OfflineChannel()]
        for ch in channels:
            await ch.start()

        fake_ch = channels[0]
        assert isinstance(fake_ch, FakeChannel)
        assert fake_ch.started is True

    @pytest.mark.asyncio
    async def test_stop_all_channels_on_shutdown(self):
        """Stopping all channels must call stop() on each without raising."""
        channels: list[BaseChannel] = [FakeChannel(), OfflineChannel()]
        for ch in channels:
            await ch.start()
        # Simulate graceful shutdown
        for ch in channels:
            await ch.stop()

        fake_ch = channels[0]
        assert isinstance(fake_ch, FakeChannel)
        assert fake_ch.stopped is True

    @pytest.mark.asyncio
    async def test_channel_message_metadata(self):
        """ChannelMessage must carry arbitrary metadata."""
        msg = ChannelMessage(
            channel="telegram",
            sender_id="chat_12345",
            content="Hello",
            metadata={"update_id": 999, "msg_id": 42},
        )
        assert msg.metadata["update_id"] == 999
        assert msg.metadata["msg_id"] == 42
