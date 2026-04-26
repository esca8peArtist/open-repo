"""
FastAPI router exposing validation endpoints.

Routes:
  GET  /api/validation/hardware           — HardwareInfo as JSON
  POST /api/validation/benchmark          — run LLM benchmark, return BenchmarkResult
  GET  /api/validation/health             — SystemHealth as JSON
  GET  /api/validation/compatibility/{tier} — compatible profiles for the given tier
"""
from __future__ import annotations

import logging
from dataclasses import asdict
from typing import Any

from fastapi import APIRouter, HTTPException, Path, Query

from agentcore.validation.compatibility import (
    COMPATIBILITY_MATRIX,
    get_compatible_profiles,
    get_compatibility_warnings,
    select_optimal_model,
)
from agentcore.validation.hardware import detect_hardware, run_benchmark
from agentcore.validation.health import run_all_health_checks, check_internet_connectivity

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/validation", tags=["validation"])


def _serialise(obj: Any) -> Any:
    """Recursively convert dataclasses and Enums to JSON-safe dicts."""
    import dataclasses
    from enum import Enum

    if dataclasses.is_dataclass(obj) and not isinstance(obj, type):
        return {k: _serialise(v) for k, v in dataclasses.asdict(obj).items()}
    if isinstance(obj, Enum):
        return obj.value
    if isinstance(obj, list):
        return [_serialise(i) for i in obj]
    if isinstance(obj, dict):
        return {k: _serialise(v) for k, v in obj.items()}
    return obj


# ---------------------------------------------------------------------------
# GET /api/validation/hardware
# ---------------------------------------------------------------------------


@router.get("/hardware", summary="Detect hardware specifications")
async def get_hardware() -> dict:
    """Detect and return hardware specifications of the host machine.

    Includes RAM, VRAM, CPU, GPU, TPM availability, free storage, and
    the detected hardware tier (1–4).
    """
    try:
        info = await detect_hardware()
        return _serialise(info)
    except Exception as exc:
        logger.exception("Hardware detection failed: %s", exc)
        raise HTTPException(status_code=500, detail=f"Hardware detection failed: {exc}") from exc


# ---------------------------------------------------------------------------
# POST /api/validation/benchmark
# ---------------------------------------------------------------------------


@router.post("/benchmark", summary="Run LLM inference benchmark")
async def post_benchmark(
    ollama_url: str = Query(
        default="http://ollama:11434",
        description="Base URL of the Ollama instance to benchmark against.",
    ),
) -> dict:
    """Run a quick LLM inference benchmark and return performance metrics.

    Uses the smallest available model (3 iterations, median result).
    Also returns the detected hardware tier and compatible profiles.
    """
    try:
        result = await run_benchmark(ollama_url=ollama_url)
        return _serialise(result)
    except Exception as exc:
        logger.exception("Benchmark failed: %s", exc)
        raise HTTPException(status_code=500, detail=f"Benchmark failed: {exc}") from exc


# ---------------------------------------------------------------------------
# GET /api/validation/health
# ---------------------------------------------------------------------------


@router.get("/health", summary="Run all service health checks")
async def get_health() -> dict:
    """Run health checks for all services concurrently and return aggregated results.

    Services checked: Ollama, Open WebUI, PostgreSQL, Redis, ChromaDB, AgentCore API.
    Overall status is the worst individual status (DOWN > DEGRADED > OK).
    """
    try:
        system_health = await run_all_health_checks()
        return _serialise(system_health)
    except Exception as exc:
        logger.exception("Health check aggregation failed: %s", exc)
        raise HTTPException(status_code=500, detail=f"Health check failed: {exc}") from exc


# ---------------------------------------------------------------------------
# GET /api/validation/compatibility/{tier}
# ---------------------------------------------------------------------------


@router.get("/compatibility/{tier}", summary="Get compatible profiles for a hardware tier")
async def get_compatibility(
    tier: int = Path(..., ge=1, le=4, description="Hardware tier (1–4)"),
    profile_id: int | None = Query(
        default=None,
        description="Optional: also return warnings for a specific profile selection.",
    ),
) -> dict:
    """Return the profiles that can run on the given hardware tier.

    Optionally, if ``profile_id`` is provided, also returns compatibility
    warnings and the optimal model selection for that profile/tier combo.
    """
    profiles = get_compatible_profiles(tier)
    response: dict = {
        "tier": tier,
        "compatible_profiles": _serialise(profiles),
    }

    if profile_id is not None:
        warnings = get_compatibility_warnings(tier, profile_id)
        optimal_model = select_optimal_model(profile_id, tier)
        response["selected_profile_id"] = profile_id
        response["warnings"] = warnings
        response["optimal_model"] = optimal_model

    return response


# ---------------------------------------------------------------------------
# GET /api/validation/internet
# ---------------------------------------------------------------------------


@router.get("/internet", summary="Check internet connectivity")
async def get_internet_connectivity() -> dict:
    """Return whether the host machine has internet connectivity."""
    online = await check_internet_connectivity()
    return {"online": online}
