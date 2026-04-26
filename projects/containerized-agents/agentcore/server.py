"""
AgentCore — main FastAPI application and uvicorn entrypoint.

Run via Makefile:
    make agentcore

Or directly:
    uv run python -m agentcore.server

Startup sequence:
    1. Load Settings from environment / .env
    2. Initialise PostgreSQL engine (AgentRegistry)
    3. Initialise Redis client
    4. Register built-in tools with ToolDispatcher
    5. Warm the AgentRegistry (load all active agent configs)
    6. Build the MessageRouter routing table
    7. Bind all active channels (Telegram, etc.)
    8. Start uvicorn

Shutdown sequence (SIGTERM / SIGINT):
    1. Stop all channels gracefully (drain in-flight messages)
    2. Drain Redis queues
    3. Close PostgreSQL pool
    4. Exit
"""
from __future__ import annotations

import asyncio
import logging
import sys
import time
import uuid
from contextlib import asynccontextmanager
from pathlib import Path
from typing import AsyncIterator

import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, Response
from fastapi.staticfiles import StaticFiles
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

from agentcore.logging_config import configure_logging
from agentcore.metrics import HTTP_DURATION, HTTP_REQUESTS

import chromadb

from agentcore import __version__
from agentcore.api.agents import router as agents_router
from agentcore.api.admin import router as admin_router
from agentcore.api.chat import router as chat_router
from agentcore.api.health import router as health_router
from agentcore.dashboard.router import router as dashboard_router
from agentcore.validation.api import router as validation_router
from agentcore.config import get_settings
from agentcore.core.dispatcher import ToolDispatcher, register_builtin_tools
from agentcore.mcp.registry import MCPToolRegistry
from agentcore.core.pipeline import PipelineEngine
from agentcore.core.registry import AgentRegistry
from agentcore.routing.message_router import MessageRouter

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Module-level app reference — set by create_app(), used by get_chroma_client()
# ---------------------------------------------------------------------------
_app: "FastAPI | None" = None


def get_chroma_client() -> chromadb.AsyncHttpClient:
    """Return the ChromaDB async client stored in app.state.

    Must only be called after the FastAPI lifespan has started (i.e. after
    the app has fully initialised).  Raises RuntimeError if called before
    the lifespan has run (e.g. at module import time).
    """
    if _app is None:
        raise RuntimeError(
            "get_chroma_client() called before the FastAPI app was created. "
            "Ensure create_app() has been called."
        )
    client: chromadb.AsyncHttpClient | None = getattr(_app.state, "chroma_client", None)
    if client is None:
        raise RuntimeError(
            "get_chroma_client() called before the lifespan has initialised the ChromaDB client. "
            "The app may still be starting up."
        )
    return client


# ---------------------------------------------------------------------------
# Lifespan (startup / shutdown)
# ---------------------------------------------------------------------------


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """FastAPI lifespan context manager — runs startup then yields, then shutdown."""
    settings = get_settings()
    app.state.settings = settings

    # ------------------------------------------------------------------
    # 1. ToolDispatcher
    # ------------------------------------------------------------------
    dispatcher = ToolDispatcher(
        connectivity_check_url=settings.connectivity_check_url,
        cache_ttl=settings.connectivity_cache_ttl,
    )
    register_builtin_tools(dispatcher)
    logger.info("ToolDispatcher initialised with %d built-in tools", len(dispatcher.list_tools()))

    # ------------------------------------------------------------------
    # 1b. MCP Tool Registry — registers all profile tools and attaches to dispatcher
    # ------------------------------------------------------------------
    mcp_registry = MCPToolRegistry()
    mcp_registry.register_all_tools()
    dispatcher.set_mcp_registry(mcp_registry)
    app.state.mcp_registry = mcp_registry
    app.state.dispatcher = dispatcher
    logger.info(
        "MCPToolRegistry initialised with %d tools — attached to ToolDispatcher",
        len(mcp_registry.list_tool_names()),
    )

    # ------------------------------------------------------------------
    # 2. PipelineEngine
    # ------------------------------------------------------------------
    pipeline_engine = PipelineEngine()
    app.state.pipeline_engine = pipeline_engine

    # ------------------------------------------------------------------
    # 3. Redis
    # ------------------------------------------------------------------
    redis_client = None
    try:
        import redis.asyncio as aioredis

        redis_client = await aioredis.from_url(
            settings.redis_url,
            encoding="utf-8",
            decode_responses=True,
        )
        await redis_client.ping()
        app.state.redis = redis_client
        logger.info("Redis connected: %s", settings.redis_url)
    except Exception as exc:
        logger.warning("Redis unavailable (%s) — async queuing will use asyncio tasks.", exc)
        app.state.redis = None

    # ------------------------------------------------------------------
    # 3b. ChromaDB client
    # ------------------------------------------------------------------
    chroma_client = chromadb.AsyncHttpClient(
        host=settings.chroma_host,
        port=settings.chroma_port,
    )
    app.state.chroma_client = chroma_client
    logger.info(
        "ChromaDB client initialised: %s:%d",
        settings.chroma_host,
        settings.chroma_port,
    )

    # ------------------------------------------------------------------
    # 4. AgentRegistry (PostgreSQL)
    # ------------------------------------------------------------------
    registry = AgentRegistry(settings)
    registry.set_dispatcher(dispatcher)
    registry.set_pipeline_engine(pipeline_engine)
    await registry.start()
    app.state.registry = registry

    # ------------------------------------------------------------------
    # 5. MessageRouter
    # ------------------------------------------------------------------
    message_router = MessageRouter(registry=registry, redis_client=redis_client)
    await message_router.rebuild_routing_table()
    app.state.message_router = message_router

    # ------------------------------------------------------------------
    # 6. Channels (started after registry is warm)
    # ------------------------------------------------------------------
    channels: list = []
    app.state.channels = channels

    # --- Telegram ---
    if settings.telegram_bot_token:
        try:
            from agentcore.channels.telegram.bot import TelegramChannel

            _allowed_ids: list[int] = []
            if settings.telegram_allowed_chat_ids.strip():
                _allowed_ids = [
                    int(x.strip())
                    for x in settings.telegram_allowed_chat_ids.split(",")
                    if x.strip()
                ]

            telegram_ch = TelegramChannel(
                bot_token=settings.telegram_bot_token,
                agent_id=settings.telegram_agent_id,
                message_router=message_router.route,
                allowed_chat_ids=_allowed_ids,
            )
            await telegram_ch.start()
            channels.append(telegram_ch)
            logger.info("Telegram channel started (agent_id=%s)", settings.telegram_agent_id)
        except Exception as exc:
            logger.error("Failed to start Telegram channel: %s", exc)

    # --- Twilio SMS ---
    if settings.twilio_account_sid and settings.twilio_auth_token and settings.twilio_sms_phone_number:
        try:
            from agentcore.channels.twilio.sms import TwilioSMSChannel

            sms_ch = TwilioSMSChannel(
                account_sid=settings.twilio_account_sid,
                auth_token=settings.twilio_auth_token,
                phone_number=settings.twilio_sms_phone_number,
                agent_id=settings.twilio_agent_id,
                message_router=message_router.route,
                webhook_base_url=settings.twilio_webhook_base_url,
            )
            await sms_ch.start()
            channels.append(sms_ch)
            app.include_router(sms_ch.get_webhook_router())
            logger.info(
                "Twilio SMS channel started (number=%s, agent_id=%s)",
                settings.twilio_sms_phone_number,
                settings.twilio_agent_id,
            )
        except Exception as exc:
            logger.error("Failed to start Twilio SMS channel: %s", exc)

    # --- Twilio WhatsApp ---
    if settings.twilio_account_sid and settings.twilio_auth_token and settings.twilio_whatsapp_phone_number:
        try:
            from agentcore.channels.twilio.whatsapp import TwilioWhatsAppChannel

            wa_ch = TwilioWhatsAppChannel(
                account_sid=settings.twilio_account_sid,
                auth_token=settings.twilio_auth_token,
                phone_number=settings.twilio_whatsapp_phone_number,
                agent_id=settings.twilio_agent_id,
                message_router=message_router.route,
                webhook_base_url=settings.twilio_webhook_base_url,
            )
            await wa_ch.start()
            channels.append(wa_ch)
            app.include_router(wa_ch.get_webhook_router())
            logger.info(
                "Twilio WhatsApp channel started (number=%s, agent_id=%s)",
                settings.twilio_whatsapp_phone_number,
                settings.twilio_agent_id,
            )
        except Exception as exc:
            logger.error("Failed to start Twilio WhatsApp channel: %s", exc)

    logger.info(
        "AgentCore v%s started — %d agents loaded, %d channels active",
        __version__,
        len(await registry.list_agents()),
        len(channels),
    )

    # ------------------------------------------------------------------
    # Yield — server is running
    # ------------------------------------------------------------------
    yield

    # ------------------------------------------------------------------
    # Shutdown
    # ------------------------------------------------------------------
    logger.info("AgentCore shutting down…")

    # Stop channels (drain in-flight messages)
    stop_tasks = [asyncio.create_task(ch.stop()) for ch in channels]
    if stop_tasks:
        await asyncio.gather(*stop_tasks, return_exceptions=True)

    # Close registry (database pool)
    await registry.stop()

    # Close Redis
    if redis_client is not None:
        await redis_client.aclose()

    # Close ChromaDB client (httpx session inside AsyncHttpClient)
    try:
        await chroma_client.clear_system_cache()
    except Exception:
        pass  # best-effort; AsyncHttpClient has no explicit close method

    logger.info("AgentCore shutdown complete.")


# ---------------------------------------------------------------------------
# FastAPI application
# ---------------------------------------------------------------------------


def create_app() -> FastAPI:
    """Factory that constructs and returns the FastAPI application."""
    global _app

    # Configure structured logging first so all subsequent log output is
    # formatted correctly (JSON in production, plain-text in local dev).
    configure_logging()

    settings = get_settings()

    app = FastAPI(
        title="AgentCore",
        description=(
            "Lightweight real-time event-driven orchestration layer for containerized AI agents. "
            f"Exposed at http://agent.local:{settings.agentcore_port}/api"
        ),
        version=__version__,
        lifespan=lifespan,
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
    )

    # ------------------------------------------------------------------
    # CORS — allow the local web UI (Open WebUI on port 80/443) and any
    # local admin panel.  In production these origins should be tightened.
    # ------------------------------------------------------------------
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://agent.local",
            "https://agent.local",
            "http://localhost",
            "http://localhost:3000",
            "http://127.0.0.1",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # ------------------------------------------------------------------
    # X-Request-ID — propagate or generate a unique request identifier.
    # Stored in request.state.request_id and echoed in the response header.
    # ------------------------------------------------------------------
    @app.middleware("http")
    async def request_id_middleware(request: Request, call_next):
        request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
        request.state.request_id = request_id
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response

    # ------------------------------------------------------------------
    # Prometheus HTTP instrumentation — record method, path, and status
    # for every request.  The /metrics path itself is excluded to avoid
    # self-referential cardinality explosion.
    # ------------------------------------------------------------------
    @app.middleware("http")
    async def prometheus_middleware(request: Request, call_next):
        path = request.url.path
        method = request.method
        start = time.monotonic()
        try:
            response = await call_next(request)
            status_code = str(response.status_code)
        except Exception:
            status_code = "500"
            raise
        finally:
            if path != "/metrics":
                elapsed = time.monotonic() - start
                HTTP_REQUESTS.labels(method=method, path=path, status=status_code).inc()
                HTTP_DURATION.labels(method=method, path=path).observe(elapsed)
        return response

    # ------------------------------------------------------------------
    # Concurrency limiter — enforce max_concurrent_requests
    # ------------------------------------------------------------------
    _semaphore: asyncio.Semaphore | None = None

    @app.middleware("http")
    async def concurrency_limiter(request: Request, call_next):
        nonlocal _semaphore
        if _semaphore is None:
            _semaphore = asyncio.Semaphore(settings.max_concurrent_requests)

        # Health checks bypass the semaphore
        if request.url.path in ("/health", "/api/health"):
            return await call_next(request)

        if not _semaphore._value:  # type: ignore[attr-defined]
            return JSONResponse(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                content={"detail": "Server is at maximum capacity. Please retry shortly."},
            )

        async with _semaphore:
            return await call_next(request)

    # ------------------------------------------------------------------
    # Global exception handler
    # ------------------------------------------------------------------
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.exception("Unhandled exception: %s", exc)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": "An unexpected error occurred. Check server logs for details."},
        )

    # ------------------------------------------------------------------
    # Prometheus metrics scrape endpoint
    # ------------------------------------------------------------------
    @app.get("/metrics", include_in_schema=False)
    async def metrics_endpoint():
        data = generate_latest()
        return Response(content=data, media_type=CONTENT_TYPE_LATEST)

    # ------------------------------------------------------------------
    # Routers
    # ------------------------------------------------------------------
    app.include_router(health_router)
    app.include_router(agents_router)
    app.include_router(chat_router)
    app.include_router(admin_router)
    app.include_router(dashboard_router)
    app.include_router(validation_router)

    # ------------------------------------------------------------------
    # Static files for the dashboard (CSS, JS)
    # Mounted after all routers so /dashboard/static/* is resolved first.
    # ------------------------------------------------------------------
    _dashboard_static = Path(__file__).parent / "dashboard" / "static"
    app.mount(
        "/dashboard/static",
        StaticFiles(directory=str(_dashboard_static)),
        name="dashboard-static",
    )

    # Store reference so get_chroma_client() can locate app.state at runtime.
    _app = app
    return app


# Singleton app instance — referenced by uvicorn and importable by tests
app = create_app()


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------


def main() -> None:
    """Run AgentCore with uvicorn.  Called by `make agentcore`."""
    settings = get_settings()

    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        stream=sys.stdout,
    )

    uvicorn.run(
        "agentcore.server:app",
        host=settings.agentcore_host,
        port=settings.agentcore_port,
        reload=False,  # use --reload flag explicitly for dev
        log_level=settings.log_level.lower(),
        # Performance tuning — libuv loop is measurably faster for I/O-heavy workloads
        loop="uvloop",
        # Use multiple workers only on Tier 3/4 hardware; single-worker on Tier 1/2
        workers=1 if settings.hardware_tier <= 2 else 4,
    )


if __name__ == "__main__":
    main()
