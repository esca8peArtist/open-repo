"""FastAPI application factory."""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import init_db, close_db
from app.routes import router
from app import __version__


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage app lifecycle (startup/shutdown)."""
    # Startup
    try:
        await init_db()
        print(f"Open-Repo API v{__version__} started")
    except Exception as e:
        print(f"Open-Repo API v{__version__} started (DB init skipped: {e})")
    yield
    # Shutdown
    try:
        await close_db()
    except Exception:
        pass
    print("Open-Repo API shutdown")


def create_app() -> FastAPI:
    """Create and configure FastAPI application."""
    app = FastAPI(
        title="Open-Repo API",
        description="Open-Repo MVP Backend - Federated Knowledge Network",
        version=__version__,
        lifespan=lifespan,
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # For MVP; restrict in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    app.include_router(router)

    # Root endpoint
    @app.get("/")
    async def root():
        return {
            "name": "Open-Repo API",
            "version": __version__,
            "docs": "/docs",
            "health": "/health",
        }

    return app


if __name__ == "__main__":
    import uvicorn

    app = create_app()
    uvicorn.run(app, host="127.0.0.1", port=8000)
