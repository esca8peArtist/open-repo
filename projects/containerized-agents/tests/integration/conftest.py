"""
Integration test fixtures.

Provides:
- docker_compose_file: points pytest-docker at docker-compose.test.yml
- wait_for_postgres / wait_for_redis / wait_for_chromadb: health-poll fixtures
- Environment variable setup so agentcore.config.Settings resolves correctly
- Cache clearing for get_settings() on setup and teardown

Prerequisites:
  Docker must be running and `pytest-docker` must be installed.
  Run integration tests with:
      pytest -m integration
"""
from __future__ import annotations

import os
import time
from pathlib import Path

import httpx
import pytest

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

_PROJECT_ROOT = Path(__file__).parent.parent.parent
_COMPOSE_FILE = _PROJECT_ROOT / "docker-compose.test.yml"

# ---------------------------------------------------------------------------
# Service coordinates (must match docker-compose.test.yml port bindings)
# ---------------------------------------------------------------------------

POSTGRES_HOST = "localhost"
POSTGRES_PORT = 5432
POSTGRES_USER = "test"
POSTGRES_PASSWORD = "test"
POSTGRES_DB = "testdb"

REDIS_HOST = "localhost"
REDIS_PORT = 6379

CHROMA_HOST = "localhost"
CHROMA_PORT = 8000

OLLAMA_HOST = "localhost"
OLLAMA_PORT = 11434


# ---------------------------------------------------------------------------
# docker_compose_file — consumed by pytest-docker
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    """Return the path to the docker-compose file for pytest-docker."""
    return str(_COMPOSE_FILE)


@pytest.fixture(scope="session")
def docker_compose_project_name():
    """Use a fixed project name so containers are easily identifiable."""
    return "agentcore_integration_tests"


# ---------------------------------------------------------------------------
# Service health-poll helpers
# ---------------------------------------------------------------------------


def _poll(fn, *, timeout: int = 60, interval: float = 1.0, label: str = "service") -> None:
    """Repeatedly call fn() until it returns True or timeout is exceeded."""
    deadline = time.monotonic() + timeout
    last_exc: Exception | None = None
    while time.monotonic() < deadline:
        try:
            if fn():
                return
        except Exception as exc:
            last_exc = exc
        time.sleep(interval)
    msg = f"Timed out waiting for {label} to become healthy"
    if last_exc:
        msg += f": {last_exc}"
    raise TimeoutError(msg)


# ---------------------------------------------------------------------------
# Environment variable + cache management
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session", autouse=True)
def integration_env(docker_services):
    """
    Set environment variables pointing to the live test containers and clear
    the get_settings() LRU cache so tests pick up the new values.

    docker_services is provided by pytest-docker and ensures that containers
    are up before this fixture runs.
    """
    from agentcore.config import get_settings

    postgres_url = (
        f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
        f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )

    os.environ["POSTGRES_URL"] = postgres_url
    os.environ["REDIS_URL"] = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
    os.environ["CHROMA_HOST"] = CHROMA_HOST
    os.environ["CHROMA_PORT"] = str(CHROMA_PORT)
    os.environ["CHROMA_URL"] = f"http://{CHROMA_HOST}:{CHROMA_PORT}"
    os.environ["OLLAMA_BASE_URL"] = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}"
    os.environ["API_SECRET_KEY"] = "integration-test-secret-key-strong"
    os.environ["AGENTCORE_BASE_URL"] = "http://localhost:8080"
    os.environ["UPDATE_PUBLIC_KEY_HEX"] = ""

    get_settings.cache_clear()

    yield

    # Teardown: reset cache so subsequent test sessions start clean
    get_settings.cache_clear()


# ---------------------------------------------------------------------------
# Wait fixtures — each polls the corresponding service health endpoint
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def wait_for_postgres(docker_services, integration_env):
    """Block until PostgreSQL accepts connections."""

    def _check() -> bool:
        import asyncpg  # type: ignore
        import asyncio

        async def _ping():
            conn = await asyncpg.connect(
                host=POSTGRES_HOST,
                port=POSTGRES_PORT,
                user=POSTGRES_USER,
                password=POSTGRES_PASSWORD,
                database=POSTGRES_DB,
                timeout=3,
            )
            await conn.close()

        asyncio.get_event_loop().run_until_complete(_ping())
        return True

    _poll(_check, timeout=60, label="postgres")
    return {
        "host": POSTGRES_HOST,
        "port": POSTGRES_PORT,
        "user": POSTGRES_USER,
        "password": POSTGRES_PASSWORD,
        "database": POSTGRES_DB,
        "url": os.environ["POSTGRES_URL"],
    }


@pytest.fixture(scope="session")
def wait_for_redis(docker_services, integration_env):
    """Block until Redis responds to PING."""

    def _check() -> bool:
        import redis  # type: ignore

        client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, socket_connect_timeout=3)
        return client.ping()

    _poll(_check, timeout=30, label="redis")
    return {"host": REDIS_HOST, "port": REDIS_PORT, "url": os.environ["REDIS_URL"]}


@pytest.fixture(scope="session")
def wait_for_chromadb(docker_services, integration_env):
    """Block until ChromaDB's heartbeat endpoint returns 200."""

    def _check() -> bool:
        r = httpx.get(
            f"http://{CHROMA_HOST}:{CHROMA_PORT}/api/v1/heartbeat",
            timeout=3.0,
        )
        return r.status_code == 200

    _poll(_check, timeout=60, label="chromadb")
    return {
        "host": CHROMA_HOST,
        "port": CHROMA_PORT,
        "url": os.environ["CHROMA_URL"],
    }


@pytest.fixture(scope="session")
def wait_for_ollama_stub(docker_services, integration_env):
    """Block until the Ollama stub server is responding."""

    def _check() -> bool:
        r = httpx.get(
            f"http://{OLLAMA_HOST}:{OLLAMA_PORT}/health",
            timeout=3.0,
        )
        return r.status_code == 200

    _poll(_check, timeout=60, label="ollama-stub")
    return {
        "host": OLLAMA_HOST,
        "port": OLLAMA_PORT,
        "url": os.environ["OLLAMA_BASE_URL"],
    }
