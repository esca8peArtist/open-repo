"""
Service health checks.

Used by: setup wizard step 11, dashboard status bar, /api/health endpoint.
"""
from __future__ import annotations

import asyncio
import logging
import subprocess
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional

import httpx

logger = logging.getLogger(__name__)

# Service URLs — all use Docker Compose service names as hostnames
_OLLAMA_URL = "http://ollama:11434"
_OPEN_WEBUI_URL = "http://open-webui:3000"
_CHROMADB_URL = "http://chromadb:8000"
_AGENTCORE_URL = "http://agentcore:8080"
_POSTGRES_HOST = "postgres"
_POSTGRES_PORT = "5432"
_REDIS_URL = "redis://redis:6379"
_CONNECTIVITY_CHECK_URL = "https://cloudflare.com"

# Module-level start time for uptime calculation
_module_start = time.monotonic()


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------


class HealthStatus(Enum):
    OK = "ok"
    DEGRADED = "degraded"
    DOWN = "down"
    UNKNOWN = "unknown"


@dataclass
class ServiceHealth:
    name: str
    status: HealthStatus
    latency_ms: float
    message: str
    details: dict = field(default_factory=dict)


@dataclass
class SystemHealth:
    overall: HealthStatus
    services: list[ServiceHealth]
    timestamp: str
    uptime_seconds: float


# ---------------------------------------------------------------------------
# Individual service checks
# ---------------------------------------------------------------------------


async def check_ollama() -> ServiceHealth:
    """GET /api/tags — healthy if 200 and at least one model available."""
    t0 = time.monotonic()
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(f"{_OLLAMA_URL}/api/tags")
        latency = (time.monotonic() - t0) * 1000

        if resp.status_code != 200:
            return ServiceHealth(
                name="ollama",
                status=HealthStatus.DOWN,
                latency_ms=round(latency, 1),
                message=f"HTTP {resp.status_code}",
            )

        models = resp.json().get("models", [])
        if not models:
            return ServiceHealth(
                name="ollama",
                status=HealthStatus.DEGRADED,
                latency_ms=round(latency, 1),
                message="No models loaded",
                details={"model_count": 0},
            )

        return ServiceHealth(
            name="ollama",
            status=HealthStatus.OK,
            latency_ms=round(latency, 1),
            message=f"{len(models)} model(s) available",
            details={"model_count": len(models), "models": [m.get("name") for m in models[:5]]},
        )
    except httpx.ConnectError:
        latency = (time.monotonic() - t0) * 1000
        return ServiceHealth(
            name="ollama",
            status=HealthStatus.DOWN,
            latency_ms=round(latency, 1),
            message="Connection refused",
        )
    except httpx.TimeoutException:
        latency = (time.monotonic() - t0) * 1000
        return ServiceHealth(
            name="ollama",
            status=HealthStatus.DOWN,
            latency_ms=round(latency, 1),
            message="Timed out",
        )
    except Exception as exc:
        latency = (time.monotonic() - t0) * 1000
        return ServiceHealth(
            name="ollama",
            status=HealthStatus.UNKNOWN,
            latency_ms=round(latency, 1),
            message=str(exc),
        )


async def check_open_webui() -> ServiceHealth:
    """GET /health — healthy if 200."""
    t0 = time.monotonic()
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(f"{_OPEN_WEBUI_URL}/health")
        latency = (time.monotonic() - t0) * 1000

        if resp.status_code == 200:
            return ServiceHealth(
                name="open_webui",
                status=HealthStatus.OK,
                latency_ms=round(latency, 1),
                message="OK",
            )
        return ServiceHealth(
            name="open_webui",
            status=HealthStatus.DOWN,
            latency_ms=round(latency, 1),
            message=f"HTTP {resp.status_code}",
        )
    except httpx.ConnectError:
        latency = (time.monotonic() - t0) * 1000
        return ServiceHealth(
            name="open_webui",
            status=HealthStatus.DOWN,
            latency_ms=round(latency, 1),
            message="Connection refused",
        )
    except httpx.TimeoutException:
        latency = (time.monotonic() - t0) * 1000
        return ServiceHealth(
            name="open_webui",
            status=HealthStatus.DOWN,
            latency_ms=round(latency, 1),
            message="Timed out",
        )
    except Exception as exc:
        latency = (time.monotonic() - t0) * 1000
        return ServiceHealth(
            name="open_webui",
            status=HealthStatus.UNKNOWN,
            latency_ms=round(latency, 1),
            message=str(exc),
        )


async def check_postgres() -> ServiceHealth:
    """Run pg_isready via subprocess. Healthy if exit code 0."""
    t0 = time.monotonic()
    try:
        result = await asyncio.get_running_loop().run_in_executor(
            None,
            lambda: subprocess.run(
                ["pg_isready", "-h", _POSTGRES_HOST, "-p", _POSTGRES_PORT],
                capture_output=True,
                timeout=5,
            ),
        )
        latency = (time.monotonic() - t0) * 1000
        detail_text = (result.stdout.decode().strip() or result.stderr.decode().strip() or "OK")

        if result.returncode == 0:
            return ServiceHealth(
                name="postgres",
                status=HealthStatus.OK,
                latency_ms=round(latency, 1),
                message=detail_text,
                details={"returncode": result.returncode},
            )
        return ServiceHealth(
            name="postgres",
            status=HealthStatus.DOWN,
            latency_ms=round(latency, 1),
            message=detail_text,
            details={"returncode": result.returncode},
        )
    except FileNotFoundError:
        latency = (time.monotonic() - t0) * 1000
        return ServiceHealth(
            name="postgres",
            status=HealthStatus.UNKNOWN,
            latency_ms=round(latency, 1),
            message="pg_isready not found in PATH",
        )
    except Exception as exc:
        latency = (time.monotonic() - t0) * 1000
        return ServiceHealth(
            name="postgres",
            status=HealthStatus.UNKNOWN,
            latency_ms=round(latency, 1),
            message=str(exc),
        )


async def check_redis() -> ServiceHealth:
    """PING via redis.asyncio. Healthy if PONG."""
    t0 = time.monotonic()
    try:
        import redis.asyncio as aioredis

        client = await aioredis.from_url(_REDIS_URL, encoding="utf-8", decode_responses=True)
        try:
            pong = await asyncio.wait_for(client.ping(), timeout=5.0)
            latency = (time.monotonic() - t0) * 1000

            if pong:
                return ServiceHealth(
                    name="redis",
                    status=HealthStatus.OK,
                    latency_ms=round(latency, 1),
                    message="PONG",
                )
            return ServiceHealth(
                name="redis",
                status=HealthStatus.DEGRADED,
                latency_ms=round(latency, 1),
                message="Unexpected PING response",
            )
        finally:
            await client.aclose()

    except ImportError:
        latency = (time.monotonic() - t0) * 1000
        return ServiceHealth(
            name="redis",
            status=HealthStatus.UNKNOWN,
            latency_ms=round(latency, 1),
            message="redis package not installed",
        )
    except (ConnectionRefusedError, OSError):
        latency = (time.monotonic() - t0) * 1000
        return ServiceHealth(
            name="redis",
            status=HealthStatus.DOWN,
            latency_ms=round(latency, 1),
            message="Connection refused",
        )
    except asyncio.TimeoutError:
        latency = (time.monotonic() - t0) * 1000
        return ServiceHealth(
            name="redis",
            status=HealthStatus.DOWN,
            latency_ms=round(latency, 1),
            message="Timed out",
        )
    except Exception as exc:
        latency = (time.monotonic() - t0) * 1000
        return ServiceHealth(
            name="redis",
            status=HealthStatus.UNKNOWN,
            latency_ms=round(latency, 1),
            message=str(exc),
        )


async def check_chromadb() -> ServiceHealth:
    """GET /api/v1/heartbeat — healthy if nanosecond heartbeat present."""
    t0 = time.monotonic()
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(f"{_CHROMADB_URL}/api/v1/heartbeat")
        latency = (time.monotonic() - t0) * 1000

        if resp.status_code != 200:
            return ServiceHealth(
                name="chromadb",
                status=HealthStatus.DOWN,
                latency_ms=round(latency, 1),
                message=f"HTTP {resp.status_code}",
            )

        body = resp.json()
        nanosecond_heartbeat = body.get("nanosecond heartbeat") or body.get("nanosecond_heartbeat")
        if nanosecond_heartbeat is not None:
            return ServiceHealth(
                name="chromadb",
                status=HealthStatus.OK,
                latency_ms=round(latency, 1),
                message="Heartbeat OK",
                details={"nanosecond_heartbeat": nanosecond_heartbeat},
            )
        return ServiceHealth(
            name="chromadb",
            status=HealthStatus.DEGRADED,
            latency_ms=round(latency, 1),
            message="Heartbeat field missing from response",
            details={"body": body},
        )
    except httpx.ConnectError:
        latency = (time.monotonic() - t0) * 1000
        return ServiceHealth(
            name="chromadb",
            status=HealthStatus.DOWN,
            latency_ms=round(latency, 1),
            message="Connection refused",
        )
    except httpx.TimeoutException:
        latency = (time.monotonic() - t0) * 1000
        return ServiceHealth(
            name="chromadb",
            status=HealthStatus.DOWN,
            latency_ms=round(latency, 1),
            message="Timed out",
        )
    except Exception as exc:
        latency = (time.monotonic() - t0) * 1000
        return ServiceHealth(
            name="chromadb",
            status=HealthStatus.UNKNOWN,
            latency_ms=round(latency, 1),
            message=str(exc),
        )


async def check_agentcore_api() -> ServiceHealth:
    """GET /api/health on ourselves. Healthy if version field is returned."""
    t0 = time.monotonic()
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(f"{_AGENTCORE_URL}/api/health")
        latency = (time.monotonic() - t0) * 1000

        if resp.status_code != 200:
            return ServiceHealth(
                name="agentcore_api",
                status=HealthStatus.DOWN,
                latency_ms=round(latency, 1),
                message=f"HTTP {resp.status_code}",
            )

        body = resp.json()
        version = body.get("version")
        if version:
            return ServiceHealth(
                name="agentcore_api",
                status=HealthStatus.OK,
                latency_ms=round(latency, 1),
                message=f"v{version}",
                details={"version": version, "status": body.get("status")},
            )
        return ServiceHealth(
            name="agentcore_api",
            status=HealthStatus.DEGRADED,
            latency_ms=round(latency, 1),
            message="Version field missing from /api/health response",
        )
    except httpx.ConnectError:
        latency = (time.monotonic() - t0) * 1000
        return ServiceHealth(
            name="agentcore_api",
            status=HealthStatus.DOWN,
            latency_ms=round(latency, 1),
            message="Connection refused",
        )
    except httpx.TimeoutException:
        latency = (time.monotonic() - t0) * 1000
        return ServiceHealth(
            name="agentcore_api",
            status=HealthStatus.DOWN,
            latency_ms=round(latency, 1),
            message="Timed out",
        )
    except Exception as exc:
        latency = (time.monotonic() - t0) * 1000
        return ServiceHealth(
            name="agentcore_api",
            status=HealthStatus.UNKNOWN,
            latency_ms=round(latency, 1),
            message=str(exc),
        )


# ---------------------------------------------------------------------------
# Aggregated health check
# ---------------------------------------------------------------------------


def _aggregate_status(services: list[ServiceHealth]) -> HealthStatus:
    """Compute overall status from individual service results.

    Rules:
    - Any DOWN service → overall DOWN
    - Any DEGRADED service (no DOWN) → overall DEGRADED
    - All OK or UNKNOWN → OK
    """
    statuses = {s.status for s in services}
    if HealthStatus.DOWN in statuses:
        return HealthStatus.DOWN
    if HealthStatus.DEGRADED in statuses:
        return HealthStatus.DEGRADED
    return HealthStatus.OK


async def run_all_health_checks() -> SystemHealth:
    """Run all service health checks concurrently via asyncio.gather.

    Overall status:
    - OK if all services are OK
    - DEGRADED if any service is DEGRADED (but none are DOWN)
    - DOWN if any service is DOWN
    """
    check_fns = [
        check_ollama(),
        check_open_webui(),
        check_postgres(),
        check_redis(),
        check_chromadb(),
        check_agentcore_api(),
    ]

    results = await asyncio.gather(*check_fns, return_exceptions=True)

    services: list[ServiceHealth] = []
    for item in results:
        if isinstance(item, Exception):
            logger.warning("Health check raised an exception: %s", item)
            services.append(
                ServiceHealth(
                    name="unknown",
                    status=HealthStatus.UNKNOWN,
                    latency_ms=0.0,
                    message=str(item),
                )
            )
        else:
            services.append(item)  # type: ignore[arg-type]

    overall = _aggregate_status(services)
    uptime = round(time.monotonic() - _module_start, 1)
    timestamp = datetime.now(timezone.utc).isoformat()

    return SystemHealth(
        overall=overall,
        services=services,
        timestamp=timestamp,
        uptime_seconds=uptime,
    )


# ---------------------------------------------------------------------------
# Internet connectivity
# ---------------------------------------------------------------------------


async def check_internet_connectivity() -> bool:
    """HEAD request to a reliable endpoint. Returns True if online."""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.head(_CONNECTIVITY_CHECK_URL)
            return resp.status_code < 500
    except Exception:
        return False
