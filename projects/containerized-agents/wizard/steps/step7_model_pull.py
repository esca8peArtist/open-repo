"""
Step 7 — Model pull: download recommended Ollama models with SSE progress stream.
"""
from __future__ import annotations

import asyncio
import json
import logging
import subprocess
from typing import AsyncGenerator

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse, StreamingResponse
from fastapi.templating import Jinja2Templates

from wizard.config import OLLAMA_URL, PROFILE_MODELS, TOTAL_STEPS
from wizard.state import get_state, save_state

router = APIRouter()
templates = Jinja2Templates(directory="wizard/templates")
logger = logging.getLogger(__name__)


def _models_for_profile(profile_id: int | None) -> list[str]:
    """Return the list of models to pull for the selected profile."""
    if profile_id is None:
        return ["qwen2.5:7b-instruct", "nomic-embed-text"]
    return PROFILE_MODELS.get(profile_id, ["qwen2.5:7b-instruct", "nomic-embed-text"])


@router.get("/step/7", response_class=HTMLResponse)
async def get_step7(request: Request) -> HTMLResponse:
    state = get_state()
    if not state.models_to_pull:
        state.models_to_pull = _models_for_profile(state.selected_profile)
        save_state(state)
    return templates.TemplateResponse(
        "step7.html",
        {
            "request": request,
            "state": state,
            "current_step": 7,
            "total_steps": TOTAL_STEPS,
            "step_title": "Model Download",
        },
    )


async def _pull_model_sse(model: str) -> AsyncGenerator[str, None]:
    """Run `ollama pull <model>` and stream stdout lines as SSE events."""
    yield f"data: {json.dumps({'model': model, 'status': 'pulling', 'detail': 'Starting…'})}\n\n"
    try:
        proc = await asyncio.create_subprocess_exec(
            "ollama", "pull", model,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT,
        )
        assert proc.stdout is not None
        async for raw_line in proc.stdout:
            line = raw_line.decode("utf-8", errors="replace").strip()
            if line:
                yield f"data: {json.dumps({'model': model, 'status': 'progress', 'detail': line})}\n\n"
        await proc.wait()
        if proc.returncode == 0:
            yield f"data: {json.dumps({'model': model, 'status': 'done'})}\n\n"
        else:
            yield f"data: {json.dumps({'model': model, 'status': 'error', 'detail': f'Exit code {proc.returncode}'})}\n\n"
    except FileNotFoundError:
        yield f"data: {json.dumps({'model': model, 'status': 'error', 'detail': 'ollama not found — is it installed?'})}\n\n"
    except Exception as exc:
        logger.exception("Model pull failed for %s", model)
        yield f"data: {json.dumps({'model': model, 'status': 'error', 'detail': str(exc)})}\n\n"


@router.get("/step/7/stream")
async def model_pull_stream(request: Request) -> StreamingResponse:
    """SSE stream — pulls all pending models one at a time and reports progress."""
    state = get_state()
    models = [m for m in state.models_to_pull if m not in state.models_pulled]

    async def generate() -> AsyncGenerator[str, None]:
        nonlocal state
        for model in models:
            pulled_ok = False
            async for event in _pull_model_sse(model):
                yield event
                try:
                    payload = json.loads(event[len("data: "):].strip())
                    if payload.get("status") == "done":
                        pulled_ok = True
                except Exception:
                    pass

            if pulled_ok:
                state = get_state()
                if model not in state.models_pulled:
                    state.models_pulled.append(model)
                    save_state(state)

        yield f"data: {json.dumps({'status': 'all_done'})}\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@router.post("/step/7")
async def post_step7(request: Request) -> RedirectResponse:
    state = get_state()
    if 7 not in state.completed_steps:
        state.completed_steps.append(7)
    state.current_step = 8
    save_state(state)
    return RedirectResponse("/step/8", status_code=303)
