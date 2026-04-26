"""
Step 11 — Health check: verify all services are up before going live.
"""
from __future__ import annotations

import asyncio
import json
import logging
import subprocess
from typing import AsyncGenerator

import httpx

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse, StreamingResponse
from fastapi.templating import Jinja2Templates

from wizard.config import TOTAL_STEPS
from wizard.state import get_state, save_state

router = APIRouter()
templates = Jinja2Templates(directory="wizard/templates")
logger = logging.getLogger(__name__)


async def _check_http(name: str, url: str, timeout: float = 5.0) -> tuple[str, bool, str]:
    """Return (name, ok, detail)."""
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            resp = await client.get(url)
        ok = resp.status_code < 400
        return name, ok, f"HTTP {resp.status_code}"
    except httpx.ConnectError:
        return name, False, "Connection refused"
    except httpx.TimeoutException:
        return name, False, "Timed out"
    except Exception as exc:
        return name, False, str(exc)


async def _check_postgres() -> tuple[str, bool, str]:
    """Use pg_isready via subprocess."""
    try:
        result = await asyncio.get_running_loop().run_in_executor(
            None,
            lambda: subprocess.run(
                ["pg_isready", "-h", "postgres", "-p", "5432"],
                capture_output=True,
                timeout=5,
            ),
        )
        ok = result.returncode == 0
        detail = result.stdout.decode().strip() or result.stderr.decode().strip() or "OK"
        return "postgres", ok, detail
    except FileNotFoundError:
        return "postgres", False, "pg_isready not found"
    except Exception as exc:
        return "postgres", False, str(exc)


async def run_health_checks() -> dict[str, dict]:
    """Check all services; return dict keyed by service name."""
    http_checks = [
        ("ollama", "http://ollama:11434/api/tags"),
        ("open_webui", "http://open-webui:3000/health"),
        ("agentcore", "http://agentcore:8080/health"),
        ("chromadb", "http://chromadb:8000/api/v1/heartbeat"),
    ]

    tasks = [_check_http(name, url) for name, url in http_checks]
    tasks.append(_check_postgres())  # type: ignore[arg-type]

    results_raw = await asyncio.gather(*tasks, return_exceptions=True)
    results: dict[str, dict] = {}
    for item in results_raw:
        if isinstance(item, Exception):
            logger.warning("Health check raised: %s", item)
            continue
        name, ok, detail = item
        results[name] = {"ok": ok, "detail": detail}

    return results


@router.get("/step/11", response_class=HTMLResponse)
async def get_step11(request: Request) -> HTMLResponse:
    state = get_state()
    return templates.TemplateResponse(
        "step11.html",
        {
            "request": request,
            "state": state,
            "current_step": 11,
            "total_steps": TOTAL_STEPS,
            "step_title": "Health Check",
        },
    )


@router.get("/step/11/stream")
async def health_check_stream(request: Request) -> StreamingResponse:
    """SSE stream — runs health checks and emits results as they arrive."""

    async def generate() -> AsyncGenerator[str, None]:
        results = await run_health_checks()
        all_ok = all(v["ok"] for v in results.values())

        state = get_state()
        state.health_check_results = results
        state.health_check_passed = all_ok
        save_state(state)

        for name, info in results.items():
            yield f"data: {json.dumps({'service': name, 'ok': info['ok'], 'detail': info['detail']})}\n\n"
            await asyncio.sleep(0.05)

        yield f"data: {json.dumps({'status': 'done', 'all_ok': all_ok})}\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@router.post("/step/11")
async def post_step11(request: Request) -> RedirectResponse:
    state = get_state()
    if 11 not in state.completed_steps:
        state.completed_steps.append(11)
    state.current_step = 12
    save_state(state)
    return RedirectResponse("/step/12", status_code=303)
