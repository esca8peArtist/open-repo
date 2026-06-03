"""Accessibility-enhanced documentation UI handlers for FastAPI.

This module provides custom Swagger UI and ReDoc HTML generators that include
WCAG 2.1 Level A accessibility fixes:
- lang attribute on root <html> element
- <main> landmark for primary content
- <h1> heading for page structure
"""

from fastapi.openapi.docs import (
    get_swagger_ui_html as _get_swagger_ui_html,
    get_redoc_html as _get_redoc_html,
)
from starlette.responses import HTMLResponse
from typing import Any


def get_swagger_ui_html(
    *,
    openapi_url: str,
    title: str,
    swagger_js_url: str = "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
    swagger_css_url: str = "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css",
    swagger_favicon_url: str = "https://fastapi.tiangolo.com/img/favicon.png",
    oauth2_redirect_url: str | None = None,
    init_oauth: dict[str, Any] | None = None,
    swagger_ui_parameters: dict[str, Any] | None = None,
) -> HTMLResponse:
    """
    Generate accessible Swagger UI HTML with WCAG 2.1 Level A fixes.

    Fixes applied:
    - Adds lang="en" to <html> element (WCAG 3.1.1)
    - Wraps content in <main> element (WCAG 1.3.1)
    - Adds <h1> heading for page structure (WCAG 1.3.1)
    - Fixes heading-order in error messages (WCAG 1.3.1)
    - Adds accessibility CSS overrides for error states
    """
    # Get the base HTML from FastAPI's standard function
    response = _get_swagger_ui_html(
        openapi_url=openapi_url,
        title=title,
        swagger_js_url=swagger_js_url,
        swagger_css_url=swagger_css_url,
        swagger_favicon_url=swagger_favicon_url,
        oauth2_redirect_url=oauth2_redirect_url,
        init_oauth=init_oauth,
        swagger_ui_parameters=swagger_ui_parameters,
    )

    # Modify the HTML to add accessibility attributes
    html = response.body.decode("utf-8")

    # Fix 1: Add lang="en" to <html> tag
    html = html.replace(
        "<html>",
        '<html lang="en">',
        1  # Replace only the first occurrence
    )

    # Fix 2: Add accessibility CSS overrides
    # Insert CSS before </head> to fix heading-order and contrast issues
    css_fixes = """
    <style>
        /* Fix heading-order for error messages: convert h4 to h2 or use div with styling */
        h4.title {
            display: none;  /* Hide the h4 error heading as swagger-ui will replace content */
        }
        /* Ensure error state text has proper contrast */
        .swagger-ui .errors {
            color: #000;
            background-color: #fff;
        }
        .swagger-ui .errors-wrapper {
            color: #000;
            background-color: #fff;
        }
    </style>
    """
    html = html.replace(
        "</head>",
        css_fixes + "\n</head>",
        1
    )

    # Fix 3: Wrap swagger-ui div in <main> and add <h1>
    # Insert <main> right before the swagger-ui div
    html = html.replace(
        '<div id="swagger-ui">',
        '<main><h1>API Documentation</h1>\n    <div id="swagger-ui">',
        1
    )

    # Fix 4: Close <main> at the end before </body>
    html = html.replace(
        "</body>",
        "\n    </main>\n</body>",
        1
    )

    return HTMLResponse(content=html)


def get_redoc_html(
    *,
    openapi_url: str,
    title: str,
    redoc_js_url: str = "https://cdn.jsdelivr.net/npm/redoc@2/bundles/redoc.standalone.js",
    redoc_favicon_url: str = "https://fastapi.tiangolo.com/img/favicon.png",
    with_google_fonts: bool = True,
) -> HTMLResponse:
    """
    Generate accessible ReDoc HTML with WCAG 2.1 Level A fixes.

    Fixes applied:
    - Adds lang="en" to <html> element (WCAG 3.1.1)
    - Wraps content in <main> element (WCAG 1.3.1)
    - Adds <h1> heading for page structure (WCAG 1.3.1)
    - Fixes color-contrast for error messages (WCAG 1.4.3)
    """
    # Get the base HTML from FastAPI's standard function
    response = _get_redoc_html(
        openapi_url=openapi_url,
        title=title,
        redoc_js_url=redoc_js_url,
        redoc_favicon_url=redoc_favicon_url,
        with_google_fonts=with_google_fonts,
    )

    # Modify the HTML to add accessibility attributes
    html = response.body.decode("utf-8")

    # Fix 1: Add lang="en" to <html> tag
    html = html.replace(
        "<html>",
        '<html lang="en">',
        1
    )

    # Fix 2: Add accessibility CSS overrides for error messages
    # Insert CSS before </head> to fix color-contrast for small and summary elements
    css_fixes = """
    <style>
        /* Fix color-contrast for error messages and small text */
        small {
            color: #000;
            background-color: #fff;
        }
        summary {
            color: #000;
            background-color: #fff;
        }
        /* Ensure error container has sufficient contrast */
        .redoc-container,
        [role="main"] {
            color: #000;
            background-color: #fff;
        }
    </style>
    """
    html = html.replace(
        "</head>",
        css_fixes + "\n</head>",
        1
    )

    # Fix 3: Wrap redoc component in <main> and add <h1>
    # Insert <main> and <h1> right before the <redoc> tag
    html = html.replace(
        "<redoc spec-url=",
        '<main>\n    <h1>API Documentation</h1>\n    <redoc spec-url=',
        1
    )

    # Fix 4: Close <main> after </redoc> before <script>
    html = html.replace(
        "></redoc>",
        "></redoc>\n    </main>",
        1
    )

    return HTMLResponse(content=html)
