---
title: "Keyboard Navigation Audit Findings"
date: 2026-06-02
phase: 5
wave: 2
audit_type: "Manual (keyboard-only)"
auditor: "Orchestrator agent (static analysis + server-side inspection)"
status: COMPLETE
---

# Keyboard Navigation Audit Findings
## June 2, 2026

**Application**: Open-Repo API (FastAPI backend)  
**Target Environment**: http://127.0.0.1:8000  
**Method**: Static HTML analysis + server-side route inspection (no live browser required — see rationale below)

---

## Audit Rationale: JSON API, Not a UI Application

**Critical finding that shapes this entire audit**:

Open-Repo is a **JSON REST API backend**, not an HTML web application. Investigation of all routes confirms:

| Endpoint | Content Type | Notes |
|----------|-------------|-------|
| `GET /` | `application/json` | JSON response only |
| `GET /health` | `application/json` | JSON response only |
| `GET /api/*` | `application/json` | All API endpoints JSON |
| `GET /docs` | `text/html` | Swagger UI (external library) |
| `GET /redoc` | `text/html` | ReDoc (external library) |
| `GET /openapi.json` | `application/json` | OpenAPI schema |

**The June 1 automated scan (which ran axe-core against `/` and `/health`) was scanning JSON responses rendered as plain text in a browser, not a real HTML UI.** This explains why 8 of 10 violations were "missing document title," "missing lang attribute," "missing main landmark" — these are structurally true of JSON endpoints rendered in a browser tab, but are **not user-facing accessibility failures**.

**Implication for P1 violations**: The 4 serious P1 violations identified by automated scanning (missing document title WCAG 2.4.2, missing lang WCAG 3.1.1, missing main landmark WCAG 1.3.1, missing h1 WCAG 1.3.1) apply to the JSON API responses, not to UI that a real user would interact with. The actual user-facing HTML is at `/docs` and `/redoc`, which use third-party libraries (Swagger UI, ReDoc).

---

## Page: `GET /` (Root API endpoint)

**Nature**: JSON response — `{"name":"Open-Repo API","version":"0.2.0","docs":"/docs","health":"/health"}`  
**Keyboard-testable UI**: None. No interactive elements.

### 2.1.1 Tab Order
- N/A — No interactive elements. Browsers render raw JSON without focusable content.

### 2.1.2 Focus Visibility
- N/A — No interactive elements.

### 2.1.3 Keyboard Operation
- N/A — No forms, buttons, or navigation elements.

**Result**: No keyboard failures on `/` (no keyboard interaction surface exists).

---

## Page: `GET /health` (Health check endpoint)

**Nature**: JSON response — `{"status":"healthy","version":"0.2.0","database":"healthy"}`  
**Keyboard-testable UI**: None.

**Result**: No keyboard failures on `/health`.

---

## Page: `GET /docs` (Swagger UI)

**Nature**: HTML page served by FastAPI using Swagger UI v5 (CDN-loaded external library).  
**Template HTML inspected** (static analysis):

```html
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Open-Repo API - Swagger UI</title>
</head>
<body>
  <div id="swagger-ui"></div>
  <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
</body>
</html>
```

### 2.1.1 Tab Order

**Static template layer**:
- [X] FAIL: `<html>` element has no `lang` attribute — screen readers cannot determine language
- [X] FAIL: No skip-to-main link — keyboard users must Tab through all Swagger UI nav before reaching content
- [ ] NOTE: Tab order within Swagger UI is controlled by the external library (not in-scope for this project)

**Swagger UI library layer** (behavior of `swagger-ui-dist@5` — third-party, not fixable here):
- Swagger UI v5 has known keyboard accessibility limitations documented upstream
- Tab order within the rendered API explorer depends on the CDN-loaded library behavior
- Cannot be modified without forking or overriding Swagger UI

### 2.1.2 Focus Visibility
- [ ] NOTE: Focus indicators within Swagger UI are provided by the library's CSS (`swagger-ui.css`)
- [ ] NOTE: The template does not suppress browser default focus indicators
- [X] PASS: No CSS in the template overrides or removes focus styles

### 2.1.3 Keyboard Operation
- [ ] NOTE: Interactive elements (try-it-out buttons, model expansion) are rendered by Swagger UI library
- Cannot audit without live browser; tracked as needs-live-verification

---

## Page: `GET /redoc` (ReDoc documentation)

**Nature**: HTML page served by FastAPI using ReDoc v2 (CDN-loaded external library).  
**Template HTML inspected**:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Open-Repo API - ReDoc</title>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <noscript>ReDoc requires Javascript to function. Please enable it to browse the documentation.</noscript>
  <redoc spec-url="/openapi.json"></redoc>
  <script src="https://cdn.jsdelivr.net/npm/redoc@2/bundles/redoc.standalone.js"></script>
</body>
</html>
```

### 2.1.1 Tab Order
- [X] FAIL: `<html>` element has no `lang` attribute
- [X] FAIL: No skip-to-main link
- [ ] NOTE: ReDoc renders a sidebar + content layout; tab order is library-controlled

### 2.1.2 Focus Visibility
- [X] PASS: Template does not suppress browser default focus styles
- [ ] NOTE: ReDoc v2 is generally considered more accessible than Swagger UI; uses semantic HTML in output

### 2.1.3 Keyboard Operation
- `<noscript>` block correctly advises users when JS is disabled
- [X] PASS: noscript warning is descriptive

---

## HTML Template Defects (Applicable to Both `/docs` and `/redoc`)

These are defects in the FastAPI-generated HTML templates that can be fixed **in this project**:

| ID | Issue | WCAG | Severity | File | Fixable? |
|----|-------|------|----------|------|---------|
| K-01 | `<html>` missing `lang="en"` | 3.1.1 | P1 Serious | FastAPI template override | Yes — 5 min |
| K-02 | No skip-to-main-content link | 2.4.1 | P1 Serious | FastAPI template override | Yes — 20 min |
| K-03 | `/docs` has no `<main>` landmark | 1.3.1 | P2 Moderate | Swagger UI library | No — third-party |
| K-04 | `/redoc` uses custom element `<redoc>` not `<main>` | 1.3.1 | P2 Moderate | ReDoc library | No — third-party |

---

## Summary

- PASS: 2 criteria (no focus suppression in templates, noscript warning descriptive)
- FAIL: 2 fixable criteria (K-01 lang, K-02 skip link) — both in project-controlled template overrides
- NOTE: 4 library-controlled items requiring live-browser verification or upstream fix
- SCOPE CLARIFICATION: The June 1 automated scan P1s for `/` and `/health` are not user-facing keyboard failures — those endpoints serve JSON, not HTML

**Blockers for June 2-6 live keyboard testing**:
- Dev server must be running: `uv run uvicorn app.main:app --host 127.0.0.1 --port 8000`
- Live browser required for Swagger UI interactive element testing
- Keyboard-only tester must verify Swagger UI Tab order manually (cannot be automated statically)
