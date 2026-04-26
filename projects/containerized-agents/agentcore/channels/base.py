"""
Base channel interface for AgentCore communication channels.

All channel implementations (Telegram, Twilio SMS/WhatsApp, etc.) must
subclass BaseChannel and implement the abstract methods defined here.

AgentCore's message router discovers registered channels, calls start() on
each at startup, and stop() at graceful shutdown. Inbound messages are
normalised to ChannelMessage before being dispatched to the agent.
"""

from __future__ import annotations

import abc
from dataclasses import dataclass, field
from typing import Any


# ---------------------------------------------------------------------------
# Message model
# ---------------------------------------------------------------------------


@dataclass
class ChannelMessage:
    """Normalised inbound message from any channel.

    Attributes:
        channel:    Channel identifier — "telegram", "sms", "whatsapp".
        sender_id:  Unique ID for the sender within that channel.
                    For Telegram this is the integer chat_id (as string).
                    For SMS/WhatsApp this is the E.164 phone number.
        content:    The text content of the message (after any transcription).
        metadata:   Channel-specific raw data preserved for advanced handlers.
    """

    channel: str
    sender_id: str
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Base channel
# ---------------------------------------------------------------------------


class BaseChannel(abc.ABC):
    """Abstract base class for all AgentCore communication channels.

    Subclasses must set `channel_name` as a class-level attribute and
    implement all abstract methods.

    Attributes:
        channel_name:       Unique lowercase identifier for this channel.
        requires_internet:  True if the channel cannot operate fully offline.
    """

    channel_name: str = ""
    requires_internet: bool = True

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    @abc.abstractmethod
    async def start(self) -> None:
        """Start the channel (polling loop, webhook registration, etc.).

        Should be non-blocking — long-running work must run as a background
        asyncio task. Raises on unrecoverable configuration errors.
        """

    @abc.abstractmethod
    async def stop(self) -> None:
        """Stop the channel and clean up all resources.

        Must be safe to call even if start() has not been called or has
        failed. Should not raise.
        """

    # ------------------------------------------------------------------
    # Messaging
    # ------------------------------------------------------------------

    @abc.abstractmethod
    async def send_message(
        self,
        recipient_id: str,
        text: str,
        **kwargs: Any,
    ) -> bool:
        """Send an outbound message.

        Args:
            recipient_id:  Channel-specific recipient identifier.
            text:          Plain-text message body.
            **kwargs:      Channel-specific options (e.g. parse_mode, media).

        Returns:
            True on success, False on failure (channel should log details).
            Must never raise — callers treat False as a soft degradation.
        """

    @abc.abstractmethod
    async def handle_inbound(self, raw_payload: dict[str, Any]) -> ChannelMessage:
        """Parse a raw inbound payload into a normalised ChannelMessage.

        Args:
            raw_payload:  Channel-specific raw data (Update dict, Twilio
                          form params, etc.).

        Returns:
            A populated ChannelMessage ready for the agent router.
        """
