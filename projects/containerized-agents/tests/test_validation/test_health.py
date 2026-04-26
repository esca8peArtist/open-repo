"""
Tests for agentcore.validation.health

All httpx and subprocess calls are mocked so the suite runs without
any live services.
"""
from __future__ import annotations

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from agentcore.validation.health import (
    HealthStatus,
    ServiceHealth,
    SystemHealth,
    _aggregate_status,
    check_agentcore_api,
    check_chromadb,
    check_ollama,
    check_open_webui,
    check_postgres,
    check_redis,
    check_internet_connectivity,
    run_all_health_checks,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_response(status_code: int, json_body: dict | None = None) -> MagicMock:
    resp = MagicMock(spec=httpx.Response)
    resp.status_code = status_code
    resp.json.return_value = json_body or {}
    return resp


def _async_client_ctx(response: MagicMock):
    """Return an async context manager that yields a mock client."""
    client = MagicMock()
    client.get = AsyncMock(return_value=response)
    client.head = AsyncMock(return_value=response)
    ctx = MagicMock()
    ctx.__aenter__ = AsyncMock(return_value=client)
    ctx.__aexit__ = AsyncMock(return_value=False)
    return ctx


# ---------------------------------------------------------------------------
# _aggregate_status
# ---------------------------------------------------------------------------


class TestAggregateStatus:
    def _svc(self, status: HealthStatus) -> ServiceHealth:
        return ServiceHealth(name="x", status=status, latency_ms=0, message="")

    def test_all_ok(self):
        services = [self._svc(HealthStatus.OK)] * 3
        assert _aggregate_status(services) == HealthStatus.OK

    def test_one_degraded(self):
        services = [self._svc(HealthStatus.OK), self._svc(HealthStatus.DEGRADED)]
        assert _aggregate_status(services) == HealthStatus.DEGRADED

    def test_down_wins_over_degraded(self):
        services = [
            self._svc(HealthStatus.DEGRADED),
            self._svc(HealthStatus.DOWN),
            self._svc(HealthStatus.OK),
        ]
        assert _aggregate_status(services) == HealthStatus.DOWN

    def test_unknown_treated_as_ok(self):
        services = [self._svc(HealthStatus.OK), self._svc(HealthStatus.UNKNOWN)]
        assert _aggregate_status(services) == HealthStatus.OK


# ---------------------------------------------------------------------------
# check_ollama
# ---------------------------------------------------------------------------


class TestCheckOllama:
    @pytest.mark.asyncio
    async def test_healthy_with_models(self):
        resp = _make_response(200, {"models": [{"name": "qwen2.5:7b"}, {"name": "phi4-mini"}]})
        with patch("agentcore.validation.health.httpx.AsyncClient", return_value=_async_client_ctx(resp)):
            result = await check_ollama()
        assert result.status == HealthStatus.OK
        assert result.details["model_count"] == 2

    @pytest.mark.asyncio
    async def test_degraded_no_models(self):
        resp = _make_response(200, {"models": []})
        with patch("agentcore.validation.health.httpx.AsyncClient", return_value=_async_client_ctx(resp)):
            result = await check_ollama()
        assert result.status == HealthStatus.DEGRADED

    @pytest.mark.asyncio
    async def test_down_http_error(self):
        resp = _make_response(500)
        with patch("agentcore.validation.health.httpx.AsyncClient", return_value=_async_client_ctx(resp)):
            result = await check_ollama()
        assert result.status == HealthStatus.DOWN

    @pytest.mark.asyncio
    async def test_down_connection_refused(self):
        client = MagicMock()
        client.get = AsyncMock(side_effect=httpx.ConnectError("refused"))
        ctx = MagicMock()
        ctx.__aenter__ = AsyncMock(return_value=client)
        ctx.__aexit__ = AsyncMock(return_value=False)
        with patch("agentcore.validation.health.httpx.AsyncClient", return_value=ctx):
            result = await check_ollama()
        assert result.status == HealthStatus.DOWN
        assert "refused" in result.message.lower()

    @pytest.mark.asyncio
    async def test_down_timeout(self):
        client = MagicMock()
        client.get = AsyncMock(side_effect=httpx.TimeoutException("timed out"))
        ctx = MagicMock()
        ctx.__aenter__ = AsyncMock(return_value=client)
        ctx.__aexit__ = AsyncMock(return_value=False)
        with patch("agentcore.validation.health.httpx.AsyncClient", return_value=ctx):
            result = await check_ollama()
        assert result.status == HealthStatus.DOWN


# ---------------------------------------------------------------------------
# check_open_webui
# ---------------------------------------------------------------------------


class TestCheckOpenWebui:
    @pytest.mark.asyncio
    async def test_healthy(self):
        resp = _make_response(200, {"status": "ok"})
        with patch("agentcore.validation.health.httpx.AsyncClient", return_value=_async_client_ctx(resp)):
            result = await check_open_webui()
        assert result.status == HealthStatus.OK

    @pytest.mark.asyncio
    async def test_down_503(self):
        resp = _make_response(503)
        with patch("agentcore.validation.health.httpx.AsyncClient", return_value=_async_client_ctx(resp)):
            result = await check_open_webui()
        assert result.status == HealthStatus.DOWN


# ---------------------------------------------------------------------------
# check_postgres
# ---------------------------------------------------------------------------


class TestCheckPostgres:
    @pytest.mark.asyncio
    async def test_healthy(self):
        mock_proc = MagicMock()
        mock_proc.returncode = 0
        mock_proc.stdout = b"postgres:5432 - accepting connections\n"
        mock_proc.stderr = b""

        async def fake_executor(_exec, fn):
            return mock_proc

        loop = asyncio.get_running_loop()
        with patch.object(loop, "run_in_executor", side_effect=fake_executor):
            result = await check_postgres()

        assert result.status == HealthStatus.OK

    @pytest.mark.asyncio
    async def test_down_nonzero_exit(self):
        mock_proc = MagicMock()
        mock_proc.returncode = 2
        mock_proc.stdout = b""
        mock_proc.stderr = b"no response\n"

        async def fake_executor(_exec, fn):
            return mock_proc

        loop = asyncio.get_running_loop()
        with patch.object(loop, "run_in_executor", side_effect=fake_executor):
            result = await check_postgres()

        assert result.status == HealthStatus.DOWN

    @pytest.mark.asyncio
    async def test_unknown_pg_isready_missing(self):
        async def fake_executor(_exec, fn):
            raise FileNotFoundError("pg_isready not found")

        loop = asyncio.get_running_loop()
        with patch.object(loop, "run_in_executor", side_effect=fake_executor):
            result = await check_postgres()

        assert result.status == HealthStatus.UNKNOWN
        assert "pg_isready" in result.message


# ---------------------------------------------------------------------------
# check_redis
# ---------------------------------------------------------------------------


class TestCheckRedis:
    @pytest.mark.asyncio
    async def test_healthy_pong(self):
        """When redis returns PONG, check_redis must return HealthStatus.OK."""
        mock_client = AsyncMock()
        mock_client.ping = AsyncMock(return_value=True)
        mock_client.aclose = AsyncMock()

        # aioredis is imported locally inside check_redis() so it cannot be patched
        # as a module-level attribute. The _check_redis_with_mock helper patches via
        # create=True and overrides _REDIS_URL to avoid real network connections.
        result = await _check_redis_with_mock(mock_client)

        assert result.status == HealthStatus.OK

    @pytest.mark.asyncio
    async def test_down_import_error(self):
        """When redis package is not installed, check_redis returns UNKNOWN."""
        with patch.dict("sys.modules", {"redis": None, "redis.asyncio": None}):
            # Simulate ImportError by patching the import inside the function
            with patch("builtins.__import__", side_effect=_selective_import_error):
                result = await check_redis()
        # If redis isn't importable it should be UNKNOWN
        assert result.status in (HealthStatus.UNKNOWN, HealthStatus.DOWN)


def _selective_import_error(name, *args, **kwargs):
    if "redis" in name:
        raise ImportError(f"No module named '{name}'")
    import builtins
    return builtins.__import__(name, *args, **kwargs)


async def _check_redis_with_mock(mock_client) -> ServiceHealth:
    """Helper that patches redis.asyncio.from_url directly.

    check_redis() uses ``import redis.asyncio as aioredis`` inside the function
    body, so the import pulls from sys.modules at call time.  We patch the
    ``from_url`` attribute on the already-imported module object so that our
    mock client is returned without a real network connection.
    """
    try:
        import redis.asyncio as aioredis_real
    except ImportError:
        return ServiceHealth(
            name="redis", status=HealthStatus.UNKNOWN, latency_ms=0, message="redis not installed"
        )

    # Patch from_url on the real module object (already in sys.modules) and
    # override _REDIS_URL so there is no accidental connection to a real server.
    with patch.object(aioredis_real, "from_url", AsyncMock(return_value=mock_client)):
        with patch("agentcore.validation.health._REDIS_URL", "redis://localhost:6379"):
            return await check_redis()


# ---------------------------------------------------------------------------
# check_chromadb
# ---------------------------------------------------------------------------


class TestCheckChromadb:
    @pytest.mark.asyncio
    async def test_healthy_heartbeat(self):
        resp = _make_response(200, {"nanosecond heartbeat": 1234567890})
        with patch("agentcore.validation.health.httpx.AsyncClient", return_value=_async_client_ctx(resp)):
            result = await check_chromadb()
        assert result.status == HealthStatus.OK
        assert result.details.get("nanosecond_heartbeat") == 1234567890

    @pytest.mark.asyncio
    async def test_degraded_missing_heartbeat_field(self):
        resp = _make_response(200, {"some_other_field": True})
        with patch("agentcore.validation.health.httpx.AsyncClient", return_value=_async_client_ctx(resp)):
            result = await check_chromadb()
        assert result.status == HealthStatus.DEGRADED

    @pytest.mark.asyncio
    async def test_down_503(self):
        resp = _make_response(503)
        with patch("agentcore.validation.health.httpx.AsyncClient", return_value=_async_client_ctx(resp)):
            result = await check_chromadb()
        assert result.status == HealthStatus.DOWN


# ---------------------------------------------------------------------------
# check_agentcore_api
# ---------------------------------------------------------------------------


class TestCheckAgentcoreApi:
    @pytest.mark.asyncio
    async def test_healthy_version_returned(self):
        resp = _make_response(200, {"version": "0.1.0", "status": "ok"})
        with patch("agentcore.validation.health.httpx.AsyncClient", return_value=_async_client_ctx(resp)):
            result = await check_agentcore_api()
        assert result.status == HealthStatus.OK
        assert "0.1.0" in result.message

    @pytest.mark.asyncio
    async def test_degraded_no_version_field(self):
        resp = _make_response(200, {"status": "ok"})  # missing "version"
        with patch("agentcore.validation.health.httpx.AsyncClient", return_value=_async_client_ctx(resp)):
            result = await check_agentcore_api()
        assert result.status == HealthStatus.DEGRADED

    @pytest.mark.asyncio
    async def test_down_404(self):
        resp = _make_response(404)
        with patch("agentcore.validation.health.httpx.AsyncClient", return_value=_async_client_ctx(resp)):
            result = await check_agentcore_api()
        assert result.status == HealthStatus.DOWN


# ---------------------------------------------------------------------------
# run_all_health_checks — aggregation logic
# ---------------------------------------------------------------------------


class TestRunAllHealthChecks:
    @pytest.mark.asyncio
    async def test_all_ok_returns_ok(self):
        ok = ServiceHealth("x", HealthStatus.OK, 1.0, "ok")

        with patch("agentcore.validation.health.check_ollama", return_value=ok), \
             patch("agentcore.validation.health.check_open_webui", return_value=ok), \
             patch("agentcore.validation.health.check_postgres", return_value=ok), \
             patch("agentcore.validation.health.check_redis", return_value=ok), \
             patch("agentcore.validation.health.check_chromadb", return_value=ok), \
             patch("agentcore.validation.health.check_agentcore_api", return_value=ok):
            result = await run_all_health_checks()

        assert result.overall == HealthStatus.OK
        assert len(result.services) == 6

    @pytest.mark.asyncio
    async def test_one_down_returns_down(self):
        ok = ServiceHealth("x", HealthStatus.OK, 1.0, "ok")
        down = ServiceHealth("ollama", HealthStatus.DOWN, 5000.0, "refused")

        with patch("agentcore.validation.health.check_ollama", return_value=down), \
             patch("agentcore.validation.health.check_open_webui", return_value=ok), \
             patch("agentcore.validation.health.check_postgres", return_value=ok), \
             patch("agentcore.validation.health.check_redis", return_value=ok), \
             patch("agentcore.validation.health.check_chromadb", return_value=ok), \
             patch("agentcore.validation.health.check_agentcore_api", return_value=ok):
            result = await run_all_health_checks()

        assert result.overall == HealthStatus.DOWN

    @pytest.mark.asyncio
    async def test_degraded_no_down_returns_degraded(self):
        ok = ServiceHealth("x", HealthStatus.OK, 1.0, "ok")
        deg = ServiceHealth("redis", HealthStatus.DEGRADED, 100.0, "slow")

        with patch("agentcore.validation.health.check_ollama", return_value=ok), \
             patch("agentcore.validation.health.check_open_webui", return_value=ok), \
             patch("agentcore.validation.health.check_postgres", return_value=ok), \
             patch("agentcore.validation.health.check_redis", return_value=deg), \
             patch("agentcore.validation.health.check_chromadb", return_value=ok), \
             patch("agentcore.validation.health.check_agentcore_api", return_value=ok):
            result = await run_all_health_checks()

        assert result.overall == HealthStatus.DEGRADED

    @pytest.mark.asyncio
    async def test_exception_in_check_becomes_unknown(self):
        ok = ServiceHealth("x", HealthStatus.OK, 1.0, "ok")

        with patch("agentcore.validation.health.check_ollama", side_effect=RuntimeError("oops")), \
             patch("agentcore.validation.health.check_open_webui", return_value=ok), \
             patch("agentcore.validation.health.check_postgres", return_value=ok), \
             patch("agentcore.validation.health.check_redis", return_value=ok), \
             patch("agentcore.validation.health.check_chromadb", return_value=ok), \
             patch("agentcore.validation.health.check_agentcore_api", return_value=ok):
            result = await run_all_health_checks()

        unknown_services = [s for s in result.services if s.status == HealthStatus.UNKNOWN]
        assert len(unknown_services) >= 1

    @pytest.mark.asyncio
    async def test_result_has_timestamp_and_uptime(self):
        ok = ServiceHealth("x", HealthStatus.OK, 1.0, "ok")

        with patch("agentcore.validation.health.check_ollama", return_value=ok), \
             patch("agentcore.validation.health.check_open_webui", return_value=ok), \
             patch("agentcore.validation.health.check_postgres", return_value=ok), \
             patch("agentcore.validation.health.check_redis", return_value=ok), \
             patch("agentcore.validation.health.check_chromadb", return_value=ok), \
             patch("agentcore.validation.health.check_agentcore_api", return_value=ok):
            result = await run_all_health_checks()

        assert result.timestamp  # non-empty ISO string
        assert result.uptime_seconds >= 0


# ---------------------------------------------------------------------------
# check_internet_connectivity
# ---------------------------------------------------------------------------


class TestCheckInternetConnectivity:
    @pytest.mark.asyncio
    async def test_online(self):
        resp = _make_response(200)
        ctx = _async_client_ctx(resp)
        with patch("agentcore.validation.health.httpx.AsyncClient", return_value=ctx):
            online = await check_internet_connectivity()
        assert online is True

    @pytest.mark.asyncio
    async def test_offline_connect_error(self):
        client = MagicMock()
        client.head = AsyncMock(side_effect=httpx.ConnectError("no route"))
        ctx = MagicMock()
        ctx.__aenter__ = AsyncMock(return_value=client)
        ctx.__aexit__ = AsyncMock(return_value=False)
        with patch("agentcore.validation.health.httpx.AsyncClient", return_value=ctx):
            online = await check_internet_connectivity()
        assert online is False
