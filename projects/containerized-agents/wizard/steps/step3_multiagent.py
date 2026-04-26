"""Step 3 — Multi-agent setup: add additional profiles and allocate resources."""
from __future__ import annotations

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from wizard.config import PROFILE_DISPLAY, TOTAL_STEPS
from wizard.state import get_state, save_state

router = APIRouter()
templates = Jinja2Templates(directory="wizard/templates")


@router.get("/step/3", response_class=HTMLResponse)
async def get_step3(request: Request) -> HTMLResponse:
    state = get_state()
    # Build list of profiles not already selected as primary
    all_profiles = [
        {"id": i, "icon": meta["icon"], "tagline": meta["tagline"], "min_ram_gb": meta["min_ram_gb"]}
        for i, meta in PROFILE_DISPLAY.items()
        if i != state.selected_profile
    ]
    return templates.TemplateResponse(
        "step3.html",
        {
            "request": request,
            "state": state,
            "all_profiles": all_profiles,
            "current_step": 3,
            "total_steps": TOTAL_STEPS,
            "step_title": "Multi-Agent Setup",
        },
    )


@router.post("/step/3")
async def post_step3(request: Request) -> RedirectResponse:
    form = await request.form()
    state = get_state()

    # Collect checked additional_profiles
    additional = []
    resource_alloc: dict[str, int] = {}
    for key, val in form.multi_items():
        if key == "additional_profiles":
            try:
                additional.append(int(val))
            except ValueError:
                pass
        elif key.startswith("cpu_"):
            profile_id = key[4:]
            try:
                resource_alloc[f"cpu_{profile_id}"] = int(val)
            except ValueError:
                pass
        elif key.startswith("ram_"):
            profile_id = key[4:]
            try:
                resource_alloc[f"ram_{profile_id}"] = int(val)
            except ValueError:
                pass

    state.additional_profiles = additional
    state.resource_allocation = resource_alloc
    if 3 not in state.completed_steps:
        state.completed_steps.append(3)
    state.current_step = 4
    save_state(state)
    return RedirectResponse("/step/4", status_code=303)
