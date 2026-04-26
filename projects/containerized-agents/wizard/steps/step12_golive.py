"""
Step 12 — Go live.

Writes the wizard-complete marker, enables the agentcore systemd service,
generates a QR code for the local URL, and redirects to the agent dashboard.
"""
from __future__ import annotations

import base64
import io
import logging
import subprocess

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from wizard.config import DASHBOARD_URL, TOTAL_STEPS, WIZARD_COMPLETE_MARKER
from wizard.state import WizardState, get_state, save_state

router = APIRouter()
templates = Jinja2Templates(directory="wizard/templates")
logger = logging.getLogger(__name__)


def _generate_qr_b64(url: str) -> str:
    """Return a base64-encoded PNG of a QR code for *url*, or empty string on error."""
    try:
        import qrcode
        from PIL import Image

        qr = qrcode.QRCode(box_size=6, border=2)
        qr.add_data(url)
        qr.make(fit=True)
        img: Image.Image = qr.make_image(fill_color="black", back_color="white")
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        return base64.b64encode(buf.getvalue()).decode("ascii")
    except Exception as exc:
        logger.warning("QR generation failed: %s", exc)
        return ""


async def complete_setup(state: WizardState) -> None:
    """Write the completion marker and start agentcore.service."""
    try:
        WIZARD_COMPLETE_MARKER.parent.mkdir(parents=True, exist_ok=True)
        WIZARD_COMPLETE_MARKER.touch(exist_ok=True)
        logger.info("Wizard complete marker written to %s", WIZARD_COMPLETE_MARKER)
    except OSError as exc:
        logger.warning("Could not write wizard-complete marker: %s", exc)

    # Enable and start agentcore.service (no-op if not running under systemd)
    try:
        subprocess.run(
            ["systemctl", "enable", "--now", "agentcore.service"],
            check=False,
            timeout=10,
            capture_output=True,
        )
    except FileNotFoundError:
        logger.info("systemctl not available — skipping service enable (Docker mode)")
    except Exception as exc:
        logger.warning("Failed to enable agentcore.service: %s", exc)

    state.local_url = DASHBOARD_URL
    state.setup_complete = True
    save_state(state)


@router.get("/step/12", response_class=HTMLResponse)
async def get_step12(request: Request) -> HTMLResponse:
    state = get_state()
    if not state.setup_complete:
        await complete_setup(state)
        state = get_state()

    qr_b64 = _generate_qr_b64(state.local_url)
    return templates.TemplateResponse(
        "step12.html",
        {
            "request": request,
            "state": state,
            "qr_b64": qr_b64,
            "dashboard_url": state.local_url,
            "current_step": 12,
            "total_steps": TOTAL_STEPS,
            "step_title": "Go Live",
        },
    )


@router.post("/step/12")
async def post_step12(request: Request) -> RedirectResponse:
    state = get_state()
    if not state.setup_complete:
        await complete_setup(state)
    if 12 not in state.completed_steps:
        state.completed_steps.append(12)
    save_state(state)
    return RedirectResponse("/complete", status_code=303)


@router.get("/complete", response_class=HTMLResponse)
async def get_complete(request: Request) -> HTMLResponse:
    state = get_state()
    qr_b64 = _generate_qr_b64(state.local_url)
    return templates.TemplateResponse(
        "complete.html",
        {
            "request": request,
            "state": state,
            "qr_b64": qr_b64,
            "dashboard_url": state.local_url,
        },
    )
