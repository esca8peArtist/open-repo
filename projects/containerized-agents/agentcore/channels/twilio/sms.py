"""
Twilio SMS channel for AgentCore.

Optional add-on — requires the customer to provide their own Twilio account
credentials. Requires internet. Degrades gracefully when offline.

Architecture:
  - Outbound: uses Twilio Python helper library (synchronous calls offloaded
    to a thread executor to avoid blocking the asyncio event loop).
  - Inbound: webhook-driven via FastAPI router. Twilio POSTs to
    /webhook/sms when a message is received on the configured number.
  - Security: every inbound webhook is validated using Twilio's X-Twilio-Signature
    header; spoofed or replayed requests are rejected with HTTP 403.

SMS character limit is 160 chars per segment (GSM-7 encoding). Longer
messages are split automatically and sent as multiple segments (Twilio
handles concatenation on the recipient's handset for most carriers).
"""

from __future__ import annotations

import asyncio
import logging
from typing import Any, Callable, Coroutine

from fastapi import APIRouter, Form, Header, HTTPException, Request, Response
from fastapi.responses import PlainTextResponse
from twilio.request_validator import RequestValidator
from twilio.rest import Client

from ..base import BaseChannel, ChannelMessage

logger = logging.getLogger(__name__)

# Twilio recommends keeping SMS segments at ≤160 GSM-7 characters.
# We use a slightly conservative limit to account for UCS-2 encoding overhead.
_SMS_SEGMENT_LENGTH = 160

# TwiML response for inbound SMS (empty body — reply sent via outbound API).
_TWIML_EMPTY = '<?xml version="1.0" encoding="UTF-8"?><Response></Response>'


class TwilioSMSChannel(BaseChannel):
    """Twilio SMS channel.

    Inbound messages arrive via Twilio webhook (POST /webhook/sms).
    Outbound messages are sent through the Twilio REST API.

    Args:
        account_sid:    Twilio Account SID.
        auth_token:     Twilio Auth Token (also used for signature validation).
        phone_number:   Twilio phone number in E.164 format (+1…).
        agent_id:       AgentCore agent identifier.
        message_router: Async callable ``(ChannelMessage) -> str`` that
                        processes a message and returns the reply text.
        webhook_base_url: Public base URL where Twilio can reach this server.
    """

    channel_name = "sms"
    requires_internet = True

    def __init__(
        self,
        account_sid: str,
        auth_token: str,
        phone_number: str,
        agent_id: str,
        message_router: Callable[[ChannelMessage], Coroutine[Any, Any, str]],
        *,
        webhook_base_url: str = "",
        rate_limit_per_minute: int = 10,
    ) -> None:
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.phone_number = phone_number  # E.164: "+12025551234"
        self.agent_id = agent_id
        self.router = message_router
        self.webhook_base_url = webhook_base_url.rstrip("/")
        self.rate_limit_per_minute = rate_limit_per_minute

        self._client: Client | None = None
        self._validator: RequestValidator | None = None
        self._running = False

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    async def start(self) -> None:
        """Initialise the Twilio client and (optionally) register the webhook URL.

        SMS is webhook-driven — there is no polling loop to start. This method
        initialises the REST client and records the webhook URL on the Twilio
        phone number so Twilio knows where to POST inbound messages.
        """
        logger.info(
            "Starting Twilio SMS channel (number=%s, agent_id=%s)",
            self.phone_number,
            self.agent_id,
        )
        self._client = Client(self.account_sid, self.auth_token)
        self._validator = RequestValidator(self.auth_token)
        self._running = True

        if self.webhook_base_url:
            webhook_url = f"{self.webhook_base_url}/webhook/sms"
            try:
                await self._register_webhook(webhook_url)
            except Exception as exc:
                # Non-fatal — operator can set webhook manually in Twilio console.
                logger.warning(
                    "Could not auto-register SMS webhook URL %s: %s", webhook_url, exc
                )

        logger.info("Twilio SMS channel started")

    async def stop(self) -> None:
        """Stop the channel. Twilio webhooks are stateless so no teardown required."""
        if not self._running:
            return
        self._running = False
        self._client = None
        self._validator = None
        logger.info("Twilio SMS channel stopped")

    async def _register_webhook(self, webhook_url: str) -> None:
        """Set the SMS webhook URL on the Twilio phone number.

        Runs the synchronous Twilio API call in a thread executor.
        """
        assert self._client is not None
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self._sync_register_webhook, webhook_url)

    def _sync_register_webhook(self, webhook_url: str) -> None:
        """Synchronous webhook registration — runs in thread executor."""
        assert self._client is not None
        # Find the phone number resource on the account.
        numbers = self._client.incoming_phone_numbers.list(
            phone_number=self.phone_number, limit=1
        )
        if not numbers:
            logger.warning(
                "Phone number %s not found on Twilio account — cannot auto-register webhook",
                self.phone_number,
            )
            return

        numbers[0].update(sms_url=webhook_url, sms_method="POST")
        logger.info("Registered SMS webhook: %s", webhook_url)

    # ------------------------------------------------------------------
    # Outbound messaging
    # ------------------------------------------------------------------

    async def send_message(
        self,
        recipient_id: str,
        text: str,
        **kwargs: Any,
    ) -> bool:
        """Send an SMS to recipient_id via Twilio.

        Messages longer than 160 characters are sent as multiple SMS segments.
        Each segment is sent sequentially to preserve ordering.

        Args:
            recipient_id: Destination phone number in E.164 format (+1…).
            text:         Message body.

        Returns:
            True if all segments were sent successfully, False otherwise.
        """
        if not self._running or self._client is None:
            logger.error("SMS channel is not running — cannot send message")
            return False

        from_number = self._outbound_from_number()
        segments = _split_sms(text, _SMS_SEGMENT_LENGTH)
        loop = asyncio.get_running_loop()

        all_ok = True
        for segment in segments:
            try:
                await loop.run_in_executor(
                    None,
                    self._sync_send,
                    from_number,
                    recipient_id,
                    segment,
                )
            except Exception as exc:
                logger.error(
                    "Failed to send SMS to %s: %s", recipient_id, exc
                )
                all_ok = False

        return all_ok

    def _sync_send(self, from_: str, to: str, body: str) -> None:
        """Synchronous Twilio message creation — runs in thread executor."""
        assert self._client is not None
        msg = self._client.messages.create(body=body, from_=from_, to=to)
        logger.debug("Sent SMS sid=%s to=%s", msg.sid, to)

    def _outbound_from_number(self) -> str:
        """Return the E.164 from-number (overridden by WhatsApp subclass)."""
        return self.phone_number

    # ------------------------------------------------------------------
    # Inbound message parsing
    # ------------------------------------------------------------------

    async def handle_inbound(self, raw_payload: dict[str, Any]) -> ChannelMessage:
        """Parse a Twilio webhook POST body into a ChannelMessage.

        Twilio sends form-encoded data. The relevant fields are:
            From   — sender's E.164 phone number
            Body   — message text
            To     — our Twilio number
            MessageSid — unique message identifier

        Args:
            raw_payload: Dict of Twilio webhook form fields.

        Returns:
            Normalised ChannelMessage.
        """
        sender = raw_payload.get("From", "")
        body = raw_payload.get("Body", "")
        message_sid = raw_payload.get("MessageSid", "")
        to_number = raw_payload.get("To", "")

        return ChannelMessage(
            channel=self.channel_name,
            sender_id=sender,
            content=body,
            metadata={
                "message_sid": message_sid,
                "to": to_number,
                "num_segments": raw_payload.get("NumSegments", "1"),
                "num_media": raw_payload.get("NumMedia", "0"),
                "account_sid": raw_payload.get("AccountSid", ""),
            },
        )

    # ------------------------------------------------------------------
    # Security
    # ------------------------------------------------------------------

    def validate_signature(
        self,
        request_url: str,
        params: dict[str, str],
        signature: str,
    ) -> bool:
        """Validate the X-Twilio-Signature header on an inbound webhook request.

        Twilio computes an HMAC-SHA1 signature over the full request URL and
        sorted POST parameters using the Auth Token as the key. This prevents
        spoofed / replayed requests.

        Args:
            request_url: Full URL Twilio posted to (must match exactly).
            params:      Dict of POST body key-value pairs.
            signature:   Value of the X-Twilio-Signature header.

        Returns:
            True if the signature is valid, False otherwise.
        """
        if self._validator is None:
            logger.error("validate_signature called before channel was started")
            return False
        return self._validator.validate(request_url, params, signature)

    # ------------------------------------------------------------------
    # FastAPI webhook router
    # ------------------------------------------------------------------

    def get_webhook_router(self) -> APIRouter:
        """Return a FastAPI APIRouter with the /webhook/sms endpoint.

        The router should be included in the AgentCore FastAPI app:

            app.include_router(sms_channel.get_webhook_router())

        The endpoint validates the Twilio signature before processing
        the inbound message. Invalid or spoofed requests receive HTTP 403.
        """
        router = APIRouter()
        channel = self  # capture self for closure

        @router.post("/webhook/sms", response_class=PlainTextResponse)
        async def sms_webhook(
            request: Request,
            x_twilio_signature: str = Header(default="", alias="X-Twilio-Signature"),
            From: str = Form(default=""),
            To: str = Form(default=""),
            Body: str = Form(default=""),
            MessageSid: str = Form(default=""),
            NumSegments: str = Form(default="1"),
            NumMedia: str = Form(default="0"),
            AccountSid: str = Form(default=""),
        ) -> Response:
            """Receive an inbound SMS from Twilio."""
            # Validate Twilio signature.
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
                    "Invalid Twilio signature for SMS webhook from %s", request.client
                )
                raise HTTPException(status_code=403, detail="Invalid Twilio signature")

            if not From or not Body.strip():
                # Ignore empty or system messages.
                return PlainTextResponse(content=_TWIML_EMPTY, media_type="text/xml")

            channel_msg = await channel.handle_inbound(form_params)

            try:
                reply_text = await channel.router(channel_msg)
            except Exception as exc:
                logger.exception("Agent router error for SMS from %s: %s", From, exc)
                reply_text = "Sorry, I encountered an error. Please try again."

            # Send reply via outbound API (not TwiML) to support multi-segment replies.
            await channel.send_message(From, reply_text)

            # Return empty TwiML — reply already sent via REST API.
            return PlainTextResponse(content=_TWIML_EMPTY, media_type="text/xml")

        return router


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------


def _split_sms(text: str, max_length: int = _SMS_SEGMENT_LENGTH) -> list[str]:
    """Split text into SMS-sized segments.

    Splits on word boundaries where possible to avoid cutting mid-word.

    Args:
        text:       Full message text.
        max_length: Maximum characters per segment.

    Returns:
        List of non-empty segments.
    """
    if len(text) <= max_length:
        return [text]

    segments: list[str] = []
    remaining = text

    while len(remaining) > max_length:
        split_at = remaining.rfind(" ", 0, max_length)
        if split_at == -1:
            split_at = max_length
        segments.append(remaining[:split_at].rstrip())
        remaining = remaining[split_at:].lstrip()

    if remaining:
        segments.append(remaining)

    return [s for s in segments if s]
