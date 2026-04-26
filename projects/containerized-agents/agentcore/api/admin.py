"""
Admin endpoints — runtime management and diagnostics.

All admin routes require the X-API-Key header.

Routes:
    POST /api/admin/reload           — reload agent registry from database
    GET  /api/admin/status           — full system status snapshot
    GET  /api/admin/agents/instances — list which agents have live instances
    POST /api/admin/connectivity     — force a connectivity check and return result
    POST /api/admin/routing/rebuild  — rebuild the message router's routing table
"""
from __future__ import annotations

import logging
import platform
import sys
import time
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Request, status

from agentcore import __version__

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/admin", tags=["admin"])

_process_start = time.monotonic()


# ---------------------------------------------------------------------------
# Auth dependency
# ---------------------------------------------------------------------------


async def _require_api_key(request: Request) -> None:
    settings = request.app.state.settings
    provided = request.headers.get("X-API-Key", "")
    if not provided or provided != settings.api_secret_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing API key.")


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------


@router.post("/reload", dependencies=[Depends(_require_api_key)])
async def reload_registry(request: Request):
    """
    Reload all agent configurations from PostgreSQL.

    Existing in-flight requests are not interrupted.  New requests after this
    call will use the freshly loaded configs.
    """
    registry = request.app.state.registry
    await registry.reload()
    agents = await registry.list_agents()
    logger.info("Admin reload triggered — %d agents loaded", len(agents))
    return {
        "status": "ok",
        "agents_loaded": len(agents),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@router.get("/status", dependencies=[Depends(_require_api_key)])
async def system_status(request: Request):
    """
    Return a comprehensive system status snapshot.

    Includes:
    - AgentCore version and uptime
    - Number of loaded agents and live instances
    - Python/platform info
    - Connectivity status
    - Settings summary (no secrets)
    """
    settings = request.app.state.settings
    registry = request.app.state.registry
    dispatcher = getattr(request.app.state, "dispatcher", None)

    agents = await registry.list_agents()
    live_instance_count = len(registry._instances)

    # Connectivity (non-blocking, use cached result)
    online: bool | None = None
    if dispatcher is not None:
        try:
            online = await dispatcher.is_online()
        except Exception:
            online = None

    return {
        "status": "ok",
        "version": __version__,
        "uptime_seconds": round(time.monotonic() - _process_start, 1),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "python_version": sys.version,
        "platform": platform.platform(),
        "agents": {
            "total_configured": len(agents),
            "live_instances": live_instance_count,
        },
        "connectivity": {
            "online": online,
            "check_url": settings.connectivity_check_url,
        },
        "settings": {
            "ollama_base_url": settings.ollama_base_url,
            "agentcore_host": settings.agentcore_host,
            "agentcore_port": settings.agentcore_port,
            "hardware_tier": settings.hardware_tier,
            "max_concurrent_requests": settings.max_concurrent_requests,
            "request_timeout": settings.request_timeout,
        },
    }


@router.get("/agents/instances", dependencies=[Depends(_require_api_key)])
async def list_live_instances(request: Request):
    """
    List agent IDs that currently have warm (in-memory) AgentInstance objects.
    Useful for capacity planning and debugging.
    """
    registry = request.app.state.registry
    return {
        "live_instances": list(registry._instances.keys()),
        "count": len(registry._instances),
    }


@router.post("/connectivity", dependencies=[Depends(_require_api_key)])
async def check_connectivity(request: Request):
    """
    Force a fresh internet connectivity check (bypasses the 30-second cache).
    Returns the result and updates the cached status.
    """
    dispatcher = getattr(request.app.state, "dispatcher", None)
    if dispatcher is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="ToolDispatcher not available.",
        )

    dispatcher.invalidate_connectivity_cache()
    online = await dispatcher.is_online()

    return {
        "online": online,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@router.post("/routing/rebuild", dependencies=[Depends(_require_api_key)])
async def rebuild_routing(request: Request):
    """
    Rebuild the message router's (channel, sender_id) -> agent_id routing table.

    Call this after updating agent channel configurations.
    """
    router_obj = getattr(request.app.state, "message_router", None)
    if router_obj is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="MessageRouter not available.",
        )

    await router_obj.rebuild_routing_table()
    return {
        "status": "ok",
        "routes": len(router_obj._routing_table),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
