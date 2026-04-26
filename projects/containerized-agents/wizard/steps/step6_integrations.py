"""Step 6 — Integration setup: CalDAV calendar and email (SMTP/IMAP)."""
from __future__ import annotations

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from wizard.config import TOTAL_STEPS
from wizard.state import get_state, save_state

router = APIRouter()
templates = Jinja2Templates(directory="wizard/templates")


@router.get("/step/6", response_class=HTMLResponse)
async def get_step6(request: Request) -> HTMLResponse:
    state = get_state()
    return templates.TemplateResponse(
        "step6.html",
        {
            "request": request,
            "state": state,
            "current_step": 6,
            "total_steps": TOTAL_STEPS,
            "step_title": "Integrations",
        },
    )


@router.post("/step/6")
async def post_step6(
    request: Request,
    caldav_url: str = Form(""),
    caldav_username: str = Form(""),
    caldav_password: str = Form(""),
    smtp_host: str = Form(""),
    smtp_port: int = Form(587),
    email_user: str = Form(""),
    email_password: str = Form(""),
) -> RedirectResponse:
    state = get_state()
    state.caldav_url = caldav_url.strip()
    state.caldav_username = caldav_username.strip()
    state.caldav_password = caldav_password
    state.smtp_host = smtp_host.strip()
    state.smtp_port = smtp_port
    state.email_user = email_user.strip()
    state.email_password = email_password
    if 6 not in state.completed_steps:
        state.completed_steps.append(6)
    state.current_step = 7
    save_state(state)
    return RedirectResponse("/step/7", status_code=303)
