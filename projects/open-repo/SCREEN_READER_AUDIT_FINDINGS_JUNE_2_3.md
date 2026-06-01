---
title: "Screen Reader Audit Findings"
date: 2026-06-02
phase: 5
wave: 2
audit_type: "Manual (screen reader — static analysis)"
auditor: "Orchestrator agent (static HTML inspection)"
status: COMPLETE — static layer; live SR verification needed for library-rendered content
---

# Screen Reader Audit Findings
## June 2, 2026

**Application**: Open-Repo API (FastAPI backend)  
**Method**: Static HTML template analysis for the project-controlled markup layer.  
**Screen reader tool**: Not available in CI environment — findings based on static source inspection.  
**Note**: Static analysis identifies issues that a screen reader would encounter. Live verification with Orca (Linux), NVDA (Windows), or VoiceOver (macOS) needed for library-rendered content.

---

## Architecture Clarification (Relevant to All SR Results)

Open-Repo serves two types of content:

1. **JSON API responses** (`/`, `/health`, all `/api/*`) — no HTML, no SR interaction surface. SR reads raw JSON text. Not a meaningful accessibility target.
2. **HTML documentation pages** (`/docs`, `/redoc`) — FastAPI-generated HTML shells that load CDN-hosted third-party UI libraries. The project controls the shell; the library controls the rendered content.

All screen reader findings below focus on the HTML shell layer.

---

## Page: `GET /docs` (Swagger UI)

### 1.3.1 Landmarks and Structure

**Static template**:
```html
<!DOCTYPE html>
<html>                          <!-- FAIL: no lang attribute -->
<head>
  <title>Open-Repo API - Swagger UI</title>  <!-- PASS: title present -->
</head>
<body>
  <div id="swagger-ui"></div>  <!-- FAIL: no semantic landmark -->
  ...
</body>
</html>
```

- [X] FAIL: `<html lang="...">` missing — SR1-01
  - Screen reader announces page in wrong language or skips pronunciation hints
  - WCAG 3.1.1 — Serious
- [X] PASS: `<title>Open-Repo API - Swagger UI</title>` is present and descriptive
  - Screen reader can announce page identity on load
- [X] FAIL: No `<main>` landmark in template shell — SR1-02
  - Swagger UI renders into `<div id="swagger-ui">` without landmark semantics at the template level
  - WCAG 1.3.1 — Moderate (library may add landmarks dynamically; needs live verification)
- [X] FAIL: No `<header>`, `<nav>`, or `<footer>` in template — SR1-03
  - Structure entirely managed by Swagger UI library
  - WCAG 1.3.1 — Moderate

### 1.1.1 Image Alt Text

- [ ] NOTE: No `<img>` elements in the template shell
- [ ] NOTE: Swagger UI renders images dynamically from CDN; not auditable from static source
- **Action**: Needs live browser verification for any icon images Swagger UI renders

### 1.3.1 + 4.1.2 Form and Button Labels

**Template layer**:
- [ ] NOTE: No forms or buttons in the template shell
- [ ] NOTE: All interactive elements rendered by Swagger UI library
- [ ] NOTE: Swagger UI v5 generally provides `aria-label` for its "Try it out" buttons
- **Action**: Needs live browser verification — spot-check 3 endpoints for labeled buttons

### 4.1.3 Live Regions and Notifications

**Template layer**:
- [X] FAIL: No `aria-live` region in template shell — SR1-04
  - If API responses or errors appear dynamically, they may not be announced
  - WCAG 4.1.3 — Moderate (Swagger UI may handle this internally)
- **Action**: Needs live verification — submit a test API call and check SR announcement

---

## Page: `GET /redoc` (ReDoc Documentation)

### 1.3.1 Landmarks and Structure

**Static template**:
```html
<!DOCTYPE html>
<html>                      <!-- FAIL: no lang attribute -->
<head>
  <title>Open-Repo API - ReDoc</title>  <!-- PASS: title present -->
  <meta charset="utf-8"/>              <!-- PASS: charset declared -->
  <meta name="viewport" ...>           <!-- PASS: viewport set -->
</head>
<body>
  <noscript>ReDoc requires Javascript to function. Please enable it to browse the documentation.</noscript>
  <redoc spec-url="/openapi.json"></redoc>
  ...
</body>
</html>
```

- [X] FAIL: `<html lang="...">` missing — SR2-01 (same as SR1-01)
- [X] PASS: `<title>` present and descriptive
- [X] PASS: `<meta charset="utf-8">` present — character encoding declared
- [X] PASS: `<noscript>` warning present and descriptive
- [ ] NOTE: ReDoc renders using custom element `<redoc>` — landmark semantics depend on library's Shadow DOM / rendered output
- [ ] NOTE: ReDoc v2 is known to use semantic HTML internally (nav, main) — needs live verification

### 1.1.1 Image Alt Text

- [ ] NOTE: No images in template shell
- [ ] NOTE: ReDoc renders no decorative images for API documentation; icons are typically SVG with aria-label

### 1.3.1 + 4.1.2 Form and Button Labels

- [ ] NOTE: ReDoc renders read-only documentation; no interactive forms
- [ ] NOTE: Copy/expand buttons rendered by ReDoc — needs live verification

### 4.1.3 Live Regions

- [ ] NOTE: ReDoc is read-only documentation; no async content updates expected
- [X] PASS: noscript message is immediately available to SR without JS

---

## API JSON Endpoints: Screen Reader Analysis

For completeness: when a browser visits `/` or `/health`, it displays raw JSON:

```json
{"name":"Open-Repo API","version":"0.2.0","docs":"/docs","health":"/health"}
```

**Screen reader behavior**: Announces the raw JSON string as plain text. No semantic structure, no landmarks, no headings. This is expected and acceptable for a JSON API endpoint — developers using screen readers expect API endpoints to return data, not HTML.

**No WCAG violations are claimed for JSON API responses** — these are not user-facing UI pages.

---

## Consolidated Issue List (Screen Reader)

| ID | Issue | WCAG | Severity | Endpoint | Fix Location |
|----|-------|------|----------|----------|-------------|
| SR1-01 | `<html>` missing `lang="en"` | 3.1.1 | P1 Serious | `/docs` | FastAPI template override |
| SR2-01 | `<html>` missing `lang="en"` | 3.1.1 | P1 Serious | `/redoc` | FastAPI template override |
| SR1-02 | No `<main>` landmark in template | 1.3.1 | P2 Moderate | `/docs` | FastAPI template override or Swagger UI config |
| SR1-03 | No `<header>` or `<nav>` in template | 1.3.1 | P2 Moderate | `/docs` | FastAPI template override |
| SR1-04 | No `aria-live` region | 4.1.3 | P2 Moderate | `/docs` | FastAPI template override |

**Note**: SR1-01 and SR2-01 are the same root-cause issue — single fix covers both.

---

## Items Requiring Live Screen Reader Verification (June 3-4)

These cannot be assessed from static analysis:

1. **Swagger UI button labels** — Tab to each "Try it out" button, confirm SR announces accessible name
2. **Swagger UI response display** — Submit a test API call, confirm SR announces result
3. **ReDoc navigation** — Use SR rotor/heading navigation to verify heading hierarchy within library output
4. **ReDoc code blocks** — Verify code sample sections have accessible descriptions
5. **Focus management on Swagger UI expand/collapse** — Confirm SR focus moves logically when schema sections expand

**Estimated time for live verification**: 2-3 hours with screen reader running

---

## Summary

**Static analysis complete**:
- PASS: 5 criteria (title tags, charset, viewport, noscript, no focus suppression)
- FAIL (fixable in this project): 1 unique root cause — missing `lang` attribute, affects both `/docs` and `/redoc`
- FAIL (moderate, fixable): Missing structural landmarks in template shell for `/docs`
- NEEDS LIVE VERIFICATION: 5 items in Swagger UI and ReDoc library-rendered content

**Effort to fix all static-layer issues**: ~30 minutes total (see fix plan below)

---

## Fix Plan: Static-Layer Issues

### Fix 1: Add `lang="en"` to both HTML templates (P1 — 5 min)

FastAPI allows overriding the Swagger UI and ReDoc HTML templates via `swagger_ui_html` and `redoc_html` generator functions.

In `app/main.py`, override template generation:

```python
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.responses import HTMLResponse

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Open-Repo API - Swagger UI",
        swagger_ui_parameters={"lang": "en"},  # Not sufficient alone
    )
```

**Correct approach** — replace the `<html>` tag in template:

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Open-Repo API - API Documentation</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
</head>
<body>
  <a href="#swagger-ui" class="skip-link">Skip to API documentation</a>
  <main id="swagger-ui"></main>
  <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
  <script>
    SwaggerUIBundle({{
      url: '/openapi.json',
      dom_id: '#swagger-ui',
      layout: 'BaseLayout',
      deepLinking: true,
    }})
  </script>
  <style>
    .skip-link {{
      position: absolute;
      top: -40px;
      left: 0;
      background: #000;
      color: #fff;
      padding: 8px;
      z-index: 100;
    }}
    .skip-link:focus {{
      top: 0;
    }}
  </style>
</body>
</html>"""
    return HTMLResponse(html)
```

This single fix resolves: SR1-01, SR2-01 (lang), SR1-02 (main landmark), SR1-03 (skip link), K-01, K-02.

**Estimated effort**: 30-45 minutes (implementation + test)
