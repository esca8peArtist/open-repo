"""FastAPI application factory."""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from app.database import init_db, close_db
from app.routes import router
from app.api.v1.export import router as export_router
from app.api.v1.opds import router as opds_router
from app import __version__


# WCAG 2.1 AA compliant HTML templates for API documentation pages.
# Fixes: WCAG 3.1.1 (lang attribute), 2.4.1 (skip link), 1.3.1 (main landmark).
_DOCS_SKIP_LINK_CSS = """
  <style>
    .a11y-skip-link {
      position: absolute;
      top: -40px;
      left: 0;
      background: #000;
      color: #fff;
      padding: 8px 16px;
      z-index: 10000;
      text-decoration: none;
      font-family: sans-serif;
    }
    .a11y-skip-link:focus {
      top: 0;
    }
  </style>"""


def _swagger_ui_html(openapi_url: str, title: str, oauth2_redirect_url: str) -> str:
    """Return WCAG 2.1 AA compliant Swagger UI HTML.

    Adds: lang attribute (WCAG 3.1.1), skip link (WCAG 2.4.1),
    main landmark (WCAG 1.3.1), and charset declaration.
    """
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
  <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">
  {_DOCS_SKIP_LINK_CSS}
</head>
<body>
  <a href="#swagger-ui-main" class="a11y-skip-link">Skip to API documentation</a>
  <main id="swagger-ui-main" aria-label="API Documentation">
    <div id="swagger-ui"></div>
  </main>
  <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
  <script>
    SwaggerUIBundle({{
      url: '{openapi_url}',
      dom_id: '#swagger-ui',
      layout: 'BaseLayout',
      deepLinking: true,
      showExtensions: true,
      showCommonExtensions: true,
      oauth2RedirectUrl: '{oauth2_redirect_url}',
      presets: [
        SwaggerUIBundle.presets.apis,
        SwaggerUIBundle.SwaggerUIStandalonePreset
      ]
    }})
  </script>
</body>
</html>"""


def _redoc_html(openapi_url: str, title: str) -> str:
    """Return WCAG 2.1 AA compliant ReDoc HTML.

    Adds: lang attribute (WCAG 3.1.1), skip link (WCAG 2.4.1),
    main landmark (WCAG 1.3.1), and charset declaration.
    """
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">
  {_DOCS_SKIP_LINK_CSS}
</head>
<body>
  <a href="#redoc-main" class="a11y-skip-link">Skip to API documentation</a>
  <main id="redoc-main" aria-label="API Reference Documentation">
    <noscript>
      ReDoc requires JavaScript to function. Please enable it to browse the documentation.
    </noscript>
    <redoc spec-url="{openapi_url}"></redoc>
  </main>
  <script src="https://cdn.jsdelivr.net/npm/redoc@2/bundles/redoc.standalone.js"></script>
</body>
</html>"""


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
    # Disable FastAPI's built-in docs routes so we can serve our own
    # WCAG-compliant versions (lang attribute, skip link, main landmark).
    app = FastAPI(
        title="Open-Repo API",
        description="Open-Repo MVP Backend - Federated Knowledge Network",
        version=__version__,
        lifespan=lifespan,
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

    # WCAG 2.1 AA compliant documentation pages.
    # Replaces FastAPI's default /docs and /redoc with accessible equivalents.
    @app.get("/docs", include_in_schema=False)
    async def swagger_ui_html():
        """Swagger UI documentation with WCAG 2.1 AA compliance.

        Fixes applied vs. FastAPI default:
        - WCAG 3.1.1: <html lang="en"> attribute
        - WCAG 2.4.1: Skip-to-main-content link
        - WCAG 1.3.1: <main> landmark wrapping content
        - Added <meta charset="utf-8">
        """
        return HTMLResponse(
            _swagger_ui_html(
                openapi_url="/openapi.json",
                title="Open-Repo API - API Documentation",
                oauth2_redirect_url="/docs/oauth2-redirect",
            )
        )

    @app.get("/redoc", include_in_schema=False)
    async def redoc_html():
        """ReDoc documentation with WCAG 2.1 AA compliance.

        Fixes applied vs. FastAPI default:
        - WCAG 3.1.1: <html lang="en"> attribute
        - WCAG 2.4.1: Skip-to-main-content link
        - WCAG 1.3.1: <main> landmark wrapping content
        - Added <meta charset="utf-8">
        """
        return HTMLResponse(
            _redoc_html(
                openapi_url="/openapi.json",
                title="Open-Repo API - API Reference",
            )
        )

    return app


# Create app instance for uvicorn
app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
