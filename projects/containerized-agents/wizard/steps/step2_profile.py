"""Step 2 — Profile selection: pick one of 6 agent profiles."""
from __future__ import annotations

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from wizard.config import PROFILE_DISPLAY, TOTAL_STEPS
from wizard.state import get_state, save_state

router = APIRouter()
templates = Jinja2Templates(directory="wizard/templates")


def _build_profile_list() -> list[dict]:
    """Return profiles merged with display metadata (no agentcore import required at boot)."""
    try:
        from agentcore.profiles import get_all_profiles

        configs = get_all_profiles()
        profiles = []
        for i, cfg in enumerate(configs, start=1):
            display = PROFILE_DISPLAY.get(i, {})
            profiles.append(
                {
                    "id": i,
                    "name": cfg.name,
                    "profile_enum": cfg.profile.value if hasattr(cfg.profile, "value") else str(cfg.profile),
                    "model": cfg.model,
                    "icon": display.get("icon", "🤖"),
                    "tagline": display.get("tagline", cfg.name),
                    "use_cases": display.get("use_cases", []),
                    "min_ram_gb": display.get("min_ram_gb", 8),
                    "recommended_tier": display.get("recommended_tier", 1),
                }
            )
        return profiles
    except Exception:
        # Fall back to display-only metadata if agentcore is not installed yet
        return [
            {
                "id": i,
                "name": meta["tagline"],
                "profile_enum": meta["tagline"].lower().replace(" ", "_"),
                "model": "—",
                "icon": meta["icon"],
                "tagline": meta["tagline"],
                "use_cases": meta["use_cases"],
                "min_ram_gb": meta["min_ram_gb"],
                "recommended_tier": meta["recommended_tier"],
            }
            for i, meta in PROFILE_DISPLAY.items()
        ]


@router.get("/step/2", response_class=HTMLResponse)
async def get_step2(request: Request) -> HTMLResponse:
    state = get_state()
    profiles = _build_profile_list()
    return templates.TemplateResponse(
        "step2.html",
        {
            "request": request,
            "state": state,
            "profiles": profiles,
            "current_step": 2,
            "total_steps": TOTAL_STEPS,
            "step_title": "Profile Selection",
        },
    )


@router.post("/step/2")
async def post_step2(
    request: Request,
    profile_id: int = Form(...),
) -> RedirectResponse:
    state = get_state()
    state.selected_profile = profile_id
    if 2 not in state.completed_steps:
        state.completed_steps.append(2)
    state.current_step = 3
    save_state(state)
    return RedirectResponse("/step/3", status_code=303)
