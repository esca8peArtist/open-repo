"""
Twilio setup helpers — used by the first-boot setup wizard (Step 4).

All functions are async-safe and run synchronous Twilio API calls in a
thread executor so they don't block the wizard's asyncio event loop.

These helpers validate credentials and configure phone number webhooks
before the TwilioSMSChannel is started. Any failures here are surfaced
as human-readable error strings rather than raw exceptions so the wizard
UI can display clear feedback to the operator.
"""

from __future__ import annotations

import asyncio
import logging

logger = logging.getLogger(__name__)


async def validate_credentials(
    account_sid: str,
    auth_token: str,
) -> tuple[bool, str]:
    """Validate Twilio credentials by fetching the account resource.

    Makes a real API call to api.twilio.com. Returns immediately if the
    credentials are malformed (wrong format) without hitting the network.

    Args:
        account_sid: Twilio Account SID (starts with "AC").
        auth_token:  Twilio Auth Token (32-char hex string).

    Returns:
        Tuple ``(is_valid, message)`` where:
        - ``is_valid`` is True if the credentials are accepted.
        - ``message`` is the Twilio account friendly name on success,
          or a human-readable error description on failure.
    """
    account_sid = account_sid.strip()
    auth_token = auth_token.strip()

    if not account_sid.startswith("AC") or len(account_sid) != 34:
        return False, "Account SID must be 34 characters starting with 'AC'"

    if len(auth_token) != 32:
        return False, "Auth Token must be a 32-character hexadecimal string"

    try:
        result = await asyncio.get_running_loop().run_in_executor(
            None, _sync_validate_credentials, account_sid, auth_token
        )
        return result
    except Exception as exc:
        logger.exception("Unexpected error validating Twilio credentials: %s", exc)
        return False, f"Unexpected error: {exc}"


def _sync_validate_credentials(
    account_sid: str, auth_token: str
) -> tuple[bool, str]:
    """Synchronous Twilio account validation — runs in thread executor."""
    from twilio.base.exceptions import TwilioRestException
    from twilio.rest import Client

    try:
        client = Client(account_sid, auth_token)
        account = client.api.accounts(account_sid).fetch()
        return True, account.friendly_name or account_sid
    except TwilioRestException as exc:
        if exc.status == 401:
            return False, "Authentication failed — check Account SID and Auth Token"
        return False, f"Twilio API error: {exc.msg}"
    except Exception as exc:
        return False, f"Network error: {exc}"


async def validate_phone_number(
    account_sid: str,
    auth_token: str,
    phone_number: str,
) -> tuple[bool, str]:
    """Check that a phone number is on the Twilio account and SMS-capable.

    Args:
        account_sid:  Twilio Account SID.
        auth_token:   Twilio Auth Token.
        phone_number: Phone number to check in E.164 format (+12025551234).

    Returns:
        Tuple ``(is_valid, description)`` where:
        - ``is_valid`` is True if the number is found and SMS-capable.
        - ``description`` is a human-readable capability summary on success
          (e.g. "SMS ✓, Voice ✓, MMS ✓") or an error message on failure.
    """
    phone_number = phone_number.strip()
    if not phone_number.startswith("+"):
        return False, "Phone number must be in E.164 format (e.g. +12025551234)"

    try:
        result = await asyncio.get_running_loop().run_in_executor(
            None,
            _sync_validate_phone_number,
            account_sid,
            auth_token,
            phone_number,
        )
        return result
    except Exception as exc:
        logger.exception("Unexpected error validating Twilio phone number: %s", exc)
        return False, f"Unexpected error: {exc}"


def _sync_validate_phone_number(
    account_sid: str, auth_token: str, phone_number: str
) -> tuple[bool, str]:
    """Synchronous phone number check — runs in thread executor."""
    from twilio.base.exceptions import TwilioRestException
    from twilio.rest import Client

    try:
        client = Client(account_sid, auth_token)
        numbers = client.incoming_phone_numbers.list(
            phone_number=phone_number, limit=1
        )
        if not numbers:
            return (
                False,
                f"Phone number {phone_number} not found on this Twilio account",
            )

        num = numbers[0]
        caps = num.capabilities or {}
        parts: list[str] = []
        if caps.get("sms"):
            parts.append("SMS ✓")
        else:
            parts.append("SMS ✗")
        if caps.get("voice"):
            parts.append("Voice ✓")
        if caps.get("mms"):
            parts.append("MMS ✓")

        if not caps.get("sms"):
            return False, f"Number {phone_number} is not SMS-capable: {', '.join(parts)}"

        return True, ", ".join(parts)

    except TwilioRestException as exc:
        return False, f"Twilio API error: {exc.msg}"
    except Exception as exc:
        return False, f"Network error: {exc}"


async def configure_webhook(
    account_sid: str,
    auth_token: str,
    phone_number: str,
    webhook_url: str,
) -> bool:
    """Set the inbound SMS webhook URL on a Twilio phone number.

    Updates the phone number resource's sms_url and sms_method fields.
    Called by the wizard after the AgentCore server URL is confirmed.

    Args:
        account_sid:  Twilio Account SID.
        auth_token:   Twilio Auth Token.
        phone_number: Twilio phone number in E.164 format.
        webhook_url:  Full public URL for the SMS webhook endpoint
                      (e.g. "https://agent.example.com/webhook/sms").

    Returns:
        True if the webhook was configured successfully, False otherwise.
    """
    try:
        result = await asyncio.get_running_loop().run_in_executor(
            None,
            _sync_configure_webhook,
            account_sid,
            auth_token,
            phone_number,
            webhook_url,
        )
        return result
    except Exception as exc:
        logger.exception("Unexpected error configuring Twilio webhook: %s", exc)
        return False


def _sync_configure_webhook(
    account_sid: str,
    auth_token: str,
    phone_number: str,
    webhook_url: str,
) -> bool:
    """Synchronous webhook configuration — runs in thread executor."""
    from twilio.base.exceptions import TwilioRestException
    from twilio.rest import Client

    try:
        client = Client(account_sid, auth_token)
        numbers = client.incoming_phone_numbers.list(
            phone_number=phone_number, limit=1
        )
        if not numbers:
            logger.error(
                "configure_webhook: phone number %s not found", phone_number
            )
            return False

        numbers[0].update(sms_url=webhook_url, sms_method="POST")
        logger.info(
            "Configured SMS webhook: number=%s url=%s", phone_number, webhook_url
        )
        return True

    except TwilioRestException as exc:
        logger.error("Twilio API error configuring webhook: %s", exc.msg)
        return False
    except Exception as exc:
        logger.error("Error configuring Twilio webhook: %s", exc)
        return False
