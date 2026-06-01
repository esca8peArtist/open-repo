"""FastAPI application factory."""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse

from app.database import init_db, close_db
from app.routes import router
from app.api.v1.export import router as export_router
from app.api.v1.opds import router as opds_router
from app import __version__
from app.a11y_docs import get_swagger_ui_html, get_redoc_html


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
        # Disable automatic docs setup so we can use our custom accessibility-enhanced versions
        docs_url=None,
        redoc_url=None,
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
    app.include_router(export_router)
    app.include_router(opds_router)

    # Root endpoint
    @app.get("/")
    async def root():
        return {
            "name": "Open-Repo API",
            "version": __version__,
            "docs": "/docs",
            "health": "/health",
        }

    # Override documentation endpoints with accessibility-enhanced versions
    @app.get("/docs", include_in_schema=False)
    async def swagger_ui_html(req: Request) -> HTMLResponse:
        """Serve Swagger UI documentation with accessibility enhancements."""
        root_path = req.scope.get("root_path", "").rstrip("/")
        openapi_url = root_path + app.openapi_url
        oauth2_redirect_url = app.swagger_ui_oauth2_redirect_url
        if oauth2_redirect_url:
            oauth2_redirect_url = root_path + oauth2_redirect_url
        return get_swagger_ui_html(
            openapi_url=openapi_url,
            title=f"{app.title} - Swagger UI",
            oauth2_redirect_url=oauth2_redirect_url,
            init_oauth=app.swagger_ui_init_oauth,
            swagger_ui_parameters=app.swagger_ui_parameters,
        )

    @app.get("/redoc", include_in_schema=False)
    async def redoc_html(req: Request) -> HTMLResponse:
        """Serve ReDoc documentation with accessibility enhancements."""
        root_path = req.scope.get("root_path", "").rstrip("/")
        openapi_url = root_path + app.openapi_url
        return get_redoc_html(
            openapi_url=openapi_url,
            title=f"{app.title} - ReDoc"
        )

    return app


# Create app instance for uvicorn
app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
