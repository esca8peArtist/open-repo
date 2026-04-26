"""
Step 4 — Communication channels.

Validates Telegram bot token and Twilio credentials inline via AJAX before
the user can advance to the next step.
"""
from __future__ import annotations

import logging

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from wizard.config import TOTAL_STEPS
from wizard.state import get_state, save_state

router = APIRouter()
templates = Jinja2Templates(directory="wizard/templates")
logger = logging.getLogger(__name__)


@router.get("/step/4", response_class=HTMLResponse)
async def get_step4(request: Request) -> HTMLResponse:
    state = get_state()
    return templates.TemplateResponse(
        "step4.html",
        {
            "request": request,
            "state": state,
            "current_step": 4,
            "total_steps": TOTAL_STEPS,
            "step_title": "Communication Channels",
        },
    )


@router.post("/api/validate/telegram")
async def validate_telegram(token: str = Form(...)) -> JSONResponse:
    """AJAX endpoint — validate a Telegram bot token."""
    try:
        from agentcore.channels.telegram.setup import validate_bot_token

        valid, message = await validate_bot_token(token.strip())
    except ImportError:
        # agentcore not available yet — do a minimal format check
        token_stripped = token.strip()
        valid = bool(token_stripped) and ":" in token_stripped
        message = "@your_bot" if valid else "Token format invalid — expected '123456:ABC-DEF…'"
    return JSONResponse({"valid": valid, "message": message})


@router.post("/api/validate/twilio")
async def validate_twilio(
    account_sid: str = Form(...),
    auth_token: str = Form(...),
    phone: str = Form(""),
) -> JSONResponse:
    """AJAX endpoint — validate Twilio credentials (and optionally a phone number)."""
    try:
        from agentcore.channels.twilio.setup import validate_credentials, validate_phone_number

        valid, message = await validate_credentials(account_sid.strip(), auth_token.strip())
        phone_valid: bool | None = None
        phone_message: str = ""
        if valid and phone.strip():
            phone_valid, phone_message = await validate_phone_number(
                account_sid.strip(), auth_token.strip(), phone.strip()
            )
    except ImportError:
        sid = account_sid.strip()
        valid = sid.startswith("AC") and len(sid) == 34
        message = "Credentials look valid (offline check)" if valid else "Account SID must start with 'AC' (34 chars)"
        phone_valid = None
        phone_message = ""

    return JSONResponse(
        {
            "valid": valid,
            "message": message,
            "phone_valid": phone_valid,
            "phone_message": phone_message,
        }
    )


@router.post("/step/4")
async def post_step4(
    request: Request,
    telegram_token: str = Form(""),
    telegram_enabled: str = Form(""),
    twilio_account_sid: str = Form(""),
    twilio_auth_token: str = Form(""),
    twilio_phone: str = Form(""),
    twilio_enabled: str = Form(""),
    whatsapp_enabled: str = Form(""),
    voice_calls_enabled: str = Form(""),
) -> RedirectResponse:
    state = get_state()
    state.telegram_token = telegram_token.strip()
    state.telegram_enabled = telegram_enabled == "on"
    state.twilio_account_sid = twilio_account_sid.strip()
    state.twilio_auth_token = twilio_auth_token.strip()
    state.twilio_phone = twilio_phone.strip()
    state.twilio_enabled = twilio_enabled == "on"
    state.whatsapp_enabled = whatsapp_enabled == "on"
    state.voice_calls_enabled = voice_calls_enabled == "on"

    # If Telegram is enabled, attempt to register bot commands (non-blocking)
    if state.telegram_enabled and state.telegram_token:
        try:
            from agentcore.channels.telegram.setup import set_bot_commands

            await set_bot_commands(state.telegram_token)
        except Exception as exc:
            logger.warning("set_bot_commands failed (non-fatal): %s", exc)

    if 4 not in state.completed_steps:
        state.completed_steps.append(4)
    state.current_step = 5
    save_state(state)
    return RedirectResponse("/step/5", status_code=303)
