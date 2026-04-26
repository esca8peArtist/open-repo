"""
AgentCore Setup Wizard
======================
Runs on port 8888. Auto-starts on first boot via agentcore-wizard.service.
Disables itself by writing /opt/agentcore/.wizard-complete when step 12 completes.

Usage:
    uvicorn wizard.app:app --host 0.0.0.0 --port 8888
    # or via Makefile:
    make wizard
"""
from __future__ import annotations

import logging
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import uvicorn

from wizard.config import WIZARD_COMPLETE_MARKER, WIZARD_HOST, WIZARD_PORT
from wizard.steps import ALL_ROUTERS

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Application factory
# ---------------------------------------------------------------------------

app = FastAPI(
    title="AgentCore Setup Wizard",
    description="First-boot configuration wizard for AgentCore edge AI agents.",
    version="1.0.0",
    docs_url=None,   # hide API docs from end users
    redoc_url=None,
)

# Static files and templates
_WIZARD_DIR = Path(__file__).parent
app.mount("/static", StaticFiles(directory=str(_WIZARD_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(_WIZARD_DIR / "templates"))

# Register all step routers
for _router in ALL_ROUTERS:
    app.include_router(_router)


# ---------------------------------------------------------------------------
# Root redirect
# ---------------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def root(request: Request) -> RedirectResponse:
    """Redirect to current wizard step (or dashboard if already complete)."""
    if WIZARD_COMPLETE_MARKER.exists():
        from wizard.config import DASHBOARD_URL
        return RedirectResponse(DASHBOARD_URL, status_code=302)

    from wizard.state import get_state
    state = get_state()
    return RedirectResponse(f"/step/{state.current_step}", status_code=302)


# ---------------------------------------------------------------------------
# Startup guard
# ---------------------------------------------------------------------------

@app.on_event("startup")
async def check_already_setup() -> None:
    """Log a warning if the wizard is started after setup was already completed."""
    if WIZARD_COMPLETE_MARKER.exists():
        logger.warning(
            "Wizard-complete marker exists at %s — setup was already completed. "
            "Redirecting all requests to agent dashboard.",
            WIZARD_COMPLETE_MARKER,
        )


# ---------------------------------------------------------------------------
# Global 404 / fallback
# ---------------------------------------------------------------------------

@app.exception_handler(404)
async def not_found_handler(request: Request, exc: Exception) -> HTMLResponse:
    return templates.TemplateResponse(
        "base.html",
        {
            "request": request,
            "error": "Page not found.",
            "current_step": 0,
            "total_steps": 12,
            "step_title": "Not Found",
        },
        status_code=404,
    )


# ---------------------------------------------------------------------------
# Entry point (used by `make wizard`)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    uvicorn.run(
        "wizard.app:app",
        host=WIZARD_HOST,
        port=WIZARD_PORT,
        reload=False,
        log_level="info",
    )
