"""Step 1 — Welcome: choose language, name the agent."""
from __future__ import annotations

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from wizard.config import LANGUAGES, TOTAL_STEPS
from wizard.state import get_state, save_state

router = APIRouter()
templates = Jinja2Templates(directory="wizard/templates")


@router.get("/step/1", response_class=HTMLResponse)
async def get_step1(request: Request) -> HTMLResponse:
    state = get_state()
    return templates.TemplateResponse(
        "step1.html",
        {
            "request": request,
            "state": state,
            "languages": LANGUAGES,
            "current_step": 1,
            "total_steps": TOTAL_STEPS,
            "step_title": "Welcome",
        },
    )


@router.post("/step/1")
async def post_step1(
    request: Request,
    language: str = Form("en"),
    agent_name: str = Form(...),
) -> RedirectResponse:
    state = get_state()
    state.language = language.strip()
    state.agent_name = agent_name.strip()
    if 1 not in state.completed_steps:
        state.completed_steps.append(1)
    state.current_step = 2
    save_state(state)
    return RedirectResponse("/step/2", status_code=303)
