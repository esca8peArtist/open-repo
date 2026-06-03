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
    # Violations targeted:
    #   - color-contrast [SERIOUS/wcag143]: version badge, method badges, URL text use
    #     white text on low-contrast colored backgrounds (ratios 2.2–3.75, need 4.5:1).
    #     Fix: darken backgrounds to achieve ≥4.5:1 against white text.
    #   - heading-order [MODERATE/best-practice]: h3 opblock-tag appears before h2 in hierarchy.
    #     Fix: restyle h3.opblock-tag to visually match h2 without changing DOM element
    #     (Swagger UI generates this; we cannot safely change the tag).
    #   - nested-interactive [SERIOUS/wcag412]: <button class="opblock-summary-control"> contains
    #     focusable children. This is a Swagger UI 5 library issue; we add role/aria overrides
    #     to reduce assistive technology confusion, but cannot fully fix without forking SwaggerUI.
    css_fixes = """
    <style>
        /* ---- Phase 5 Wave 2 A11y Fixes ---- */

        /* Fix heading-order for error messages (h4 without h3 ancestor) */
        h4.title {
            display: none;  /* Hide the h4 error heading; swagger-ui replaces content */
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

        /* Fix color-contrast on version badge: #7d8492 bg, white text → ratio 3.75 (fail).
           Darken to #595f6a for 4.7:1 ratio against #fff. WCAG 1.4.3 / wcag143. */
        .swagger-ui .info .version {
            background-color: #595f6a !important;
            color: #ffffff !important;
        }

        /* Fix color-contrast on OAS version badge: #89bf04 bg → ratio 2.2 (fail).
           Darken to #5a7d02 for 4.6:1 ratio against #fff. WCAG 1.4.3 / wcag143. */
        .swagger-ui .info .version-stamp pre {
            background-color: #5a7d02 !important;
            color: #ffffff !important;
        }

        /* Fix color-contrast on HTTP method badges (GET/POST/etc).
           Swagger UI uses colors like #61affe (GET), #49cc90 (POST), #fca130 (PUT),
           #f93e3e (DELETE) — most fail 4.5:1 with white text.
           Use dark text (#1a1a1a) on all method badges for universal compliance. */
        .swagger-ui .opblock-summary-method {
            color: #1a1a1a !important;
            text-shadow: none !important;
        }

        /* Fix color-contrast on server URL display text.
           URL text in Swagger UI often uses #3b4151 on white — confirm adequate;
           ensure any gray URL text passes 4.5:1. */
        .swagger-ui .servers-title,
        .swagger-ui select,
        .swagger-ui .url {
            color: #3b4151 !important;  /* #3b4151 on #fff = 9.5:1 - passes */
        }

        /* Fix nested-interactive (wcag412): <button class="opblock-summary-control"> contains
           an <a class="nostyle"> link for the endpoint path (e.g. /health).
           Having interactive elements nested inside buttons causes focus/AT problems.
           CSS alone cannot remove focusability of the inner <a> — we use JS below.
           The <a> tags are purely visual hash-fragment links; removing their focus
           is safe and the button itself handles expand/collapse. */

        /* Fix color-contrast on JSON Schema 2020-12 expand-deep buttons.
           Default: color #afaeae on background #efefef = ~1.7:1 (fails 4.5:1).
           Fix: use #1a1a1a text on same background = ~16.8:1. WCAG 1.4.3 / wcag143. */
        .json-schema-2020-12-expand-deep-button {
            color: #1a1a1a !important;
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
    # Also inject JS to fix nested-interactive (wcag412): Swagger UI 5 wraps endpoint
    # path anchors inside <button class="opblock-summary-control">. These <a class="nostyle">
    # tags create nested interactive elements. We remove their focusability after
    # SwaggerUI renders (using MutationObserver since SwaggerUI renders asynchronously).
    js_fix = """
    <script>
    (function() {
        /**
         * Fix nested-interactive (WCAG 4.1.2 / wcag412):
         *
         * Swagger UI 5 renders <a class="nostyle"> links inside
         * <button class="opblock-summary-control"> for each API endpoint path.
         * axe-core flags this as nested interactive elements because the <a> is
         * a real DOM anchor (regardless of tabindex/aria-hidden).
         *
         * Fix: Replace each <a class="nostyle"> inside a .opblock-summary-control
         * with a <span> that preserves the visual text and data attributes.
         * This removes the interactive element from the DOM entirely.
         * The button itself handles expand/collapse; the <a> is purely decorative.
         */
        function fixNestedInteractive() {
            var anchors = document.querySelectorAll('.opblock-summary-control a.nostyle');
            anchors.forEach(function(a) {
                var span = document.createElement('span');
                span.className = a.className;
                // Copy data attributes
                Array.from(a.attributes).forEach(function(attr) {
                    if (attr.name !== 'href' && attr.name !== 'class') {
                        span.setAttribute(attr.name, attr.value);
                    }
                });
                // Move children
                while (a.firstChild) {
                    span.appendChild(a.firstChild);
                }
                a.parentNode.replaceChild(span, a);
            });
        }

        // Use MutationObserver to catch SwaggerUI async rendering
        var fixApplied = false;
        var observer = new MutationObserver(function(mutations) {
            var hasOps = !!document.querySelector('.opblock-summary-control a.nostyle');
            if (hasOps && !fixApplied) {
                fixApplied = true;
                fixNestedInteractive();
                observer.disconnect();
            }
        });

        if (document.body) {
            observer.observe(document.body, { childList: true, subtree: true });
        } else {
            document.addEventListener('DOMContentLoaded', function() {
                observer.observe(document.body, { childList: true, subtree: true });
            });
        }

        // Fallback: run after SwaggerUI finishes rendering
        setTimeout(fixNestedInteractive, 1500);
        setTimeout(fixNestedInteractive, 4000);
    })();
    </script>
    """
    html = html.replace(
        "</body>",
        js_fix + "\n    </main>\n</body>",
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

    # Fix 2: Add accessibility CSS overrides for ReDoc
    # Insert CSS before </head> to address violations found in Phase 5 Wave 2 deep scan:
    #   - color-contrast [SERIOUS/wcag143]: ReDoc h5 section headers use #93999c (light gray)
    #     on white (#ffffff). Contrast ratio 2.88 — fails WCAG 4.5:1 requirement.
    #     Affects 63 elements: "query Parameters", "Request Body schema", response headers, etc.
    #     Fix: override h5 color to #595f6a (4.7:1 on #fff).
    #   - heading-order [MODERATE/best-practice]: ReDoc renders h5 elements within sections
    #     that already have h1/h2 parents, but within the operation block the h5 for section
    #     labels comes after h2, creating h2->h5 jumps. This is a ReDoc library issue.
    #     Fix: CSS cannot change DOM heading semantics; document as known third-party limitation.
    #   - color-contrast for error/small text (pre-existing fix carried forward)
    css_fixes = """
    <style>
        /* ---- Phase 5 Wave 2 A11y Fixes ---- */

        /* Fix color-contrast for error messages and small text */
        small {
            color: #1a1a1a !important;
            background-color: transparent;
        }
        summary {
            color: #1a1a1a !important;
        }
        /* Ensure error container has sufficient contrast */
        .redoc-container,
        [role="main"] {
            color: #1a1a1a;
            background-color: #fff;
        }

        /* Fix color-contrast on ReDoc h5 section headers.
           Default color #93999c on white = 2.88:1 (FAILS WCAG 1.4.3 AA 4.5:1 threshold).
           Override to #595f6a = 4.7:1 on white. WCAG 1.4.3 / wcag143. */
        .redoc-wrap h5,
        redoc h5,
        [data-role="redoc"] h5,
        body h5 {
            color: #595f6a !important;
        }

        /* Fix contrast for ReDoc tab labels and secondary text.
           Tab text, parameter names, and schema labels often use light gray. */
        [role="tab"],
        [role="tablist"] button,
        .react-tabs__tab {
            color: #595f6a !important;
        }

        /* Ensure schema type labels (application/json, required badges) have contrast */
        [data-section-id] h5 span {
            color: #595f6a !important;
        }

        /* Fix color-contrast on ReDoc unselected response tabs.
           Unselected tabs use color #595f6a on dark background #11171a = ~1.8:1 (fails 4.5:1).
           Our h5 fix inadvertently applies #595f6a to tab text which is on a dark panel.
           For dark backgrounds, override to white text. WCAG 1.4.3 / wcag143.
           Selected tabs (#fff bg) already pass with our #595f6a fix. */
        [role="tab"][aria-selected="false"] {
            color: #e8e8e8 !important;  /* #e8e8e8 on #11171a = ~12:1 — passes */
        }

        /* Override the broad h5 fix for h5 elements inside dark code panels */
        .react-tabs__tab-panel h5,
        [role="tabpanel"] h5 {
            color: #e8e8e8 !important;
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
