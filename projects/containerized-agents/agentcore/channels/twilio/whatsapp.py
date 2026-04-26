"""
Twilio WhatsApp channel for AgentCore.

Extends TwilioSMSChannel — uses the same Twilio account and credentials.
WhatsApp messages are sent by prefixing both the from- and to-numbers with
"whatsapp:" in the Twilio API call, and the inbound webhook URL is
/webhook/whatsapp (separate from SMS so both channels can be active
simultaneously).

Supports:
  - Text messages with basic Markdown-lite formatting (bold, italic).
  - Media messages (images, documents) via send_media().

Prerequisites:
  - Twilio WhatsApp Sandbox (for testing) or an approved WhatsApp Business
    number (for production). Configure at:
    https://www.twilio.com/console/sms/whatsapp
"""

from __future__ import annotations

import logging
from typing import Any

from fastapi import APIRouter, Form, Header, HTTPException, Request, Response
from fastapi.responses import PlainTextResponse

from .sms import TwilioSMSChannel, _split_sms, _TWIML_EMPTY

logger = logging.getLogger(__name__)

# WhatsApp message character limit (much higher than SMS).
_WHATSAPP_MAX_LENGTH = 4096

# WhatsApp address prefix required by Twilio API.
_WA_PREFIX = "whatsapp:"


class TwilioWhatsAppChannel(TwilioSMSChannel):
    """WhatsApp channel built on top of the Twilio SMS infrastructure.

    Inherits all lifecycle management from TwilioSMSChannel.
    Overrides send_message() to apply the "whatsapp:" prefix and
    registers a separate /webhook/whatsapp endpoint.
    """

    channel_name = "whatsapp"

    # ------------------------------------------------------------------
    # Outbound messaging
    # ------------------------------------------------------------------

    async def send_message(
        self,
        recipient_id: str,
        text: str,
        **kwargs: Any,
    ) -> bool:
        """Send a WhatsApp text message via Twilio.

        Applies basic Markdown-lite formatting:
          ``*bold*``     → WhatsApp bold
          ``_italic_``   → WhatsApp italic
          ``~strikethrough~`` → WhatsApp strikethrough
          `` ```code``` `` → WhatsApp monospace

        Long messages are split into multiple WhatsApp messages.

        Args:
            recipient_id: Destination phone in E.164 or "whatsapp:+1…" format.
            text:         Message body. May contain Markdown-lite formatting.

        Returns:
            True if all segments sent successfully, False otherwise.
        """
        # Ensure numbers have the whatsapp: prefix.
        to = _ensure_wa_prefix(recipient_id)

        # Apply Markdown-lite formatting.
        formatted = _format_whatsapp(text)

        # Delegate to parent send_message with normalised to-address.
        # We override _outbound_from_number() to add the prefix for the
        # from-number, so the parent send_message() uses that automatically.
        return await super().send_message(to, formatted, **kwargs)

    async def send_media(
        self,
        recipient_id: str,
        media_url: str,
        caption: str = "",
    ) -> bool:
        """Send an image or document via WhatsApp.

        The media must be publicly accessible at media_url. Twilio fetches
        it and delivers it to the recipient's WhatsApp client.

        Args:
            recipient_id: Destination phone (E.164 or whatsapp: prefixed).
            media_url:    Publicly reachable URL of the media file.
            caption:      Optional caption text shown below the media.

        Returns:
            True on success, False on failure.
        """
        import asyncio

        if not self._running or self._client is None:
            logger.error("WhatsApp channel is not running — cannot send media")
            return False

        to = _ensure_wa_prefix(recipient_id)
        from_ = self._outbound_from_number()

        loop = asyncio.get_running_loop()
        try:
            await loop.run_in_executor(
                None,
                self._sync_send_media,
                from_,
                to,
                media_url,
                caption,
            )
            return True
        except Exception as exc:
            logger.error("Failed to send WhatsApp media to %s: %s", recipient_id, exc)
            return False

    def _sync_send_media(
        self, from_: str, to: str, media_url: str, caption: str
    ) -> None:
        """Synchronous media send — runs in thread executor."""
        assert self._client is not None
        kwargs: dict[str, Any] = {
            "from_": from_,
            "to": to,
            "media_url": [media_url],
        }
        if caption:
            kwargs["body"] = caption
        msg = self._client.messages.create(**kwargs)
        logger.debug("Sent WhatsApp media sid=%s to=%s url=%s", msg.sid, to, media_url)

    # ------------------------------------------------------------------
    # Overrides
    # ------------------------------------------------------------------

    def _outbound_from_number(self) -> str:
        """Return from-number with whatsapp: prefix."""
        return _ensure_wa_prefix(self.phone_number)

    async def _register_webhook(self, webhook_url: str) -> None:
        """WhatsApp uses its own webhook URL (/webhook/whatsapp)."""
        # Replace the SMS webhook URL with the WhatsApp-specific one.
        wa_webhook_url = webhook_url.replace("/webhook/sms", "/webhook/whatsapp")
        await super()._register_webhook(wa_webhook_url)

    # ------------------------------------------------------------------
    # FastAPI webhook router
    # ------------------------------------------------------------------

    def get_webhook_router(self) -> APIRouter:
        """Return a FastAPI APIRouter with the /webhook/whatsapp endpoint."""
        router = APIRouter()
        channel = self

        @router.post("/webhook/whatsapp", response_class=PlainTextResponse)
        async def whatsapp_webhook(
            request: Request,
            x_twilio_signature: str = Header(default="", alias="X-Twilio-Signature"),
            From: str = Form(default=""),
            To: str = Form(default=""),
            Body: str = Form(default=""),
            MessageSid: str = Form(default=""),
            NumSegments: str = Form(default="1"),
            NumMedia: str = Form(default="0"),
            AccountSid: str = Form(default=""),
            MediaUrl0: str = Form(default=""),
            MediaContentType0: str = Form(default=""),
        ) -> Response:
            """Receive an inbound WhatsApp message from Twilio."""
            form_params = {
                "From": From,
                "To": To,
                "Body": Body,
                "MessageSid": MessageSid,
                "NumSegments": NumSegments,
                "NumMedia": NumMedia,
                "AccountSid": AccountSid,
            }
            request_url = str(request.url)

            if not channel.validate_signature(request_url, form_params, x_twilio_signature):
                logger.warning(
                    "Invalid Twilio signature for WhatsApp webhook from %s", request.client
                )
                raise HTTPException(status_code=403, detail="Invalid Twilio signature")

            if not From:
                return PlainTextResponse(content=_TWIML_EMPTY, media_type="text/xml")

            # Strip whatsapp: prefix from sender for the ChannelMessage sender_id.
            sender_phone = From.replace(_WA_PREFIX, "")
            body_text = Body.strip()

            # If no text but media is present, treat as a media message.
            if not body_text and MediaUrl0:
                body_text = f"[Media: {MediaContentType0 or 'attachment'} — {MediaUrl0}]"

            if not body_text:
                return PlainTextResponse(content=_TWIML_EMPTY, media_type="text/xml")

            from ..base import ChannelMessage

            channel_msg = ChannelMessage(
                channel=channel.channel_name,
                sender_id=sender_phone,
                content=body_text,
                metadata={
                    "message_sid": MessageSid,
                    "to": To,
                    "num_segments": NumSegments,
                    "num_media": NumMedia,
                    "media_url": MediaUrl0,
                    "media_content_type": MediaContentType0,
                    "account_sid": AccountSid,
                },
            )

            try:
                reply_text = await channel.router(channel_msg)
            except Exception as exc:
                logger.exception(
                    "Agent router error for WhatsApp from %s: %s", sender_phone, exc
                )
                reply_text = "Sorry, I encountered an error. Please try again."

            await channel.send_message(sender_phone, reply_text)

            return PlainTextResponse(content=_TWIML_EMPTY, media_type="text/xml")

        return router


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------


def _ensure_wa_prefix(number: str) -> str:
    """Ensure a phone number string has the 'whatsapp:' prefix.

    Idempotent — safe to call on already-prefixed strings.
    """
    number = number.strip()
    if not number.startswith(_WA_PREFIX):
        return f"{_WA_PREFIX}{number}"
    return number


def _format_whatsapp(text: str) -> str:
    """Apply WhatsApp Markdown-lite formatting to text.

    Converts standard Markdown markers to WhatsApp-compatible equivalents:
      **bold** or __bold__  →  *bold*
      *italic* or _italic_  →  _italic_  (unchanged, already compatible)
      ~~strikethrough~~     →  ~strikethrough~
      `code`                →  ```code```

    Note: WhatsApp formatting is applied server-side; the conversion here
    ensures double-asterisk Markdown bold is converted to single-asterisk
    WhatsApp bold, which is the most common mismatch.

    Args:
        text: Input text, optionally with Markdown formatting.

    Returns:
        Text with WhatsApp-compatible formatting markers.
    """
    import re

    # **bold** → *bold*
    text = re.sub(r"\*\*(.+?)\*\*", r"*\1*", text)
    # __bold__ → *bold*
    text = re.sub(r"__(.+?)__", r"*\1*", text)
    # ~~strikethrough~~ → ~strikethrough~
    text = re.sub(r"~~(.+?)~~", r"~\1~", text)
    # ```code block``` — already WhatsApp-compatible, leave as-is.

    return text
