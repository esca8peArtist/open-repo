"""
Step 10 — License binding.

For OS image SKU: generates hardware fingerprint and binds via TPM.
For Docker Compose SKU: user pastes a license key.
Delegates to agentcore/licensing/wizard_step.py API endpoints via httpx.
"""
from __future__ import annotations

import logging

import httpx

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from wizard.config import AGENTCORE_URL, TOTAL_STEPS
from wizard.state import get_state, save_state

router = APIRouter()
templates = Jinja2Templates(directory="wizard/templates")
logger = logging.getLogger(__name__)


async def _call_license_api(path: str, payload: dict) -> dict:
    """POST to the agentcore licensing API. Returns parsed JSON dict."""
    url = f"{AGENTCORE_URL}{path}"
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(url, json=payload)
        return resp.json()
    except httpx.ConnectError:
        return {"success": False, "error": "Cannot reach AgentCore service. Is it running?"}
    except Exception as exc:
        logger.exception("License API call failed: %s", exc)
        return {"success": False, "error": str(exc)}


async def _get_license_status() -> dict:
    """GET current license status from agentcore."""
    url = f"{AGENTCORE_URL}/wizard/license/status"
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(url)
        return resp.json()
    except Exception:
        return {"bound": False, "type": "unlicensed", "status": "unknown", "tier": 0, "reason": "Service unreachable"}


@router.get("/step/10", response_class=HTMLResponse)
async def get_step10(request: Request) -> HTMLResponse:
    state = get_state()
    license_status = await _get_license_status()
    return templates.TemplateResponse(
        "step10.html",
        {
            "request": request,
            "state": state,
            "license_status": license_status,
            "current_step": 10,
            "total_steps": TOTAL_STEPS,
            "step_title": "License Binding",
        },
    )


@router.post("/api/license/bind-tpm")
async def bind_tpm() -> JSONResponse:
    """Trigger TPM-based license binding (OS image SKU)."""
    result = await _call_license_api("/wizard/license/bind", {"license_key": None})
    if result.get("success"):
        state = get_state()
        state.license_type = "tpm"
        state.license_bound = True
        state.license_tier = result.get("tier", 0)
        save_state(state)
    return JSONResponse(result)


@router.post("/api/license/bind-key")
async def bind_key(license_key: str = Form(...)) -> JSONResponse:
    """Submit a license key (Docker Compose SKU)."""
    result = await _call_license_api("/wizard/license/bind", {"license_key": license_key.strip()})
    if result.get("success"):
        state = get_state()
        state.license_type = "key"
        state.license_bound = True
        state.license_tier = result.get("tier", 0)
        save_state(state)
    return JSONResponse(result)


@router.post("/step/10")
async def post_step10(request: Request) -> RedirectResponse:
    state = get_state()
    if 10 not in state.completed_steps:
        state.completed_steps.append(10)
    state.current_step = 11
    save_state(state)
    return RedirectResponse("/step/11", status_code=303)
