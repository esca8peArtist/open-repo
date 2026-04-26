"""
Step 9 — Hardware validation: benchmark the hardware and confirm profile compatibility.
"""
from __future__ import annotations

import asyncio
import json
import logging
import time

import httpx

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from wizard.config import OLLAMA_URL, PROFILE_DISPLAY, TOTAL_STEPS
from wizard.state import get_state, save_state

router = APIRouter()
templates = Jinja2Templates(directory="wizard/templates")
logger = logging.getLogger(__name__)


def _detect_ram_gb() -> float:
    """Read total RAM from /proc/meminfo."""
    try:
        with open("/proc/meminfo") as f:
            for line in f:
                if line.startswith("MemTotal:"):
                    kb = int(line.split()[1])
                    return round(kb / 1_048_576, 1)
    except Exception:
        pass
    return 0.0


def _ram_to_tier(ram_gb: float) -> int:
    """Map RAM to hardware tier (1–4)."""
    if ram_gb >= 64:
        return 4
    elif ram_gb >= 24:
        return 3
    elif ram_gb >= 16:
        return 2
    return 1


async def benchmark_hardware() -> dict:
    """
    Run a quick LLM inference benchmark via Ollama to measure tokens/second.
    Uses the smallest available model for the benchmark to keep it fast.
    """
    ram_gb = _detect_ram_gb()
    tier = _ram_to_tier(ram_gb)

    # Probe Ollama for available models
    benchmark_model: str | None = None
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(f"{OLLAMA_URL}/api/tags")
            if resp.status_code == 200:
                models = resp.json().get("models", [])
                # Prefer smallest model for benchmark speed
                for m in models:
                    name = m.get("name", "")
                    if "phi4-mini" in name or "phi" in name:
                        benchmark_model = name
                        break
                if not benchmark_model and models:
                    benchmark_model = models[0].get("name")
    except Exception:
        pass

    tokens_per_second = 0.0
    if benchmark_model:
        try:
            payload = {
                "model": benchmark_model,
                "prompt": "Hello, what is 2+2?",
                "stream": False,
                "options": {"num_predict": 20},
            }
            start = time.monotonic()
            async with httpx.AsyncClient(timeout=60.0) as client:
                resp = await client.post(f"{OLLAMA_URL}/api/generate", json=payload)
            elapsed = time.monotonic() - start
            if resp.status_code == 200:
                data = resp.json()
                eval_count = data.get("eval_count", 0)
                if elapsed > 0 and eval_count > 0:
                    tokens_per_second = round(eval_count / elapsed, 1)
        except Exception as exc:
            logger.warning("Benchmark request failed: %s", exc)

    profile_id = get_state().selected_profile or 1
    min_ram = PROFILE_DISPLAY.get(profile_id, {}).get("min_ram_gb", 8)
    compatible = ram_gb >= min_ram or ram_gb == 0.0  # 0 means unknown — don't block

    return {
        "ram_gb": ram_gb,
        "tier": tier,
        "tokens_per_second": tokens_per_second,
        "benchmark_model": benchmark_model or "none",
        "compatible": compatible,
        "min_ram_required": min_ram,
    }


@router.get("/step/9", response_class=HTMLResponse)
async def get_step9(request: Request) -> HTMLResponse:
    state = get_state()
    profile_display = PROFILE_DISPLAY.get(state.selected_profile or 1, {})
    return templates.TemplateResponse(
        "step9.html",
        {
            "request": request,
            "state": state,
            "profile_display": profile_display,
            "current_step": 9,
            "total_steps": TOTAL_STEPS,
            "step_title": "Hardware Validation",
        },
    )


@router.post("/api/benchmark")
async def run_benchmark() -> JSONResponse:
    """Run the hardware benchmark and store results in wizard state."""
    result = await benchmark_hardware()
    state = get_state()
    state.hardware_tier_detected = result["tier"]
    state.benchmark_score = result["tokens_per_second"]
    state.profile_compatible = result["compatible"]
    state.ram_gb = result["ram_gb"]
    save_state(state)
    return JSONResponse(result)


@router.post("/step/9")
async def post_step9(request: Request) -> RedirectResponse:
    state = get_state()
    if 9 not in state.completed_steps:
        state.completed_steps.append(9)
    state.current_step = 10
    save_state(state)
    return RedirectResponse("/step/10", status_code=303)
