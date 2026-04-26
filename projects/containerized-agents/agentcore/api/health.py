"""
Health-check endpoints.

GET /health       — lightweight liveness probe (no auth required)
GET /api/health   — same, under the /api prefix for consistency
"""
from __future__ import annotations

import time
from datetime import datetime, timezone

from fastapi import APIRouter, Request

from agentcore import __version__

router = APIRouter(tags=["health"])

# Record the time this module was first imported (proxy for process start time)
_start_time = time.monotonic()


def _uptime_seconds() -> float:
    return time.monotonic() - _start_time


@router.get("/health")
@router.get("/api/health")
async def health(request: Request):
    """
    Liveness probe.  Returns 200 OK as long as the process is alive.
    Includes basic status of downstream services if the app state is available.
    """
    state = request.app.state

    # Build dependency status — each entry is True/False/None (None = not configured)
    deps: dict[str, str] = {}

    # Registry (PostgreSQL)
    registry = getattr(state, "registry", None)
    if registry is not None:
        deps["postgres"] = "ok" if registry._engine is not None else "unavailable"
    else:
        deps["postgres"] = "unconfigured"

    # Redis
    redis_client = getattr(state, "redis", None)
    if redis_client is not None:
        try:
            await redis_client.ping()
            deps["redis"] = "ok"
        except Exception:
            deps["redis"] = "unavailable"
    else:
        deps["redis"] = "unconfigured"

    return {
        "status": "ok",
        "version": __version__,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "uptime_seconds": round(_uptime_seconds(), 1),
        "dependencies": deps,
    }
