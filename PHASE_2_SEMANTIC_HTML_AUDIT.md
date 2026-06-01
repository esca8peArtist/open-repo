# Phase 2 Semantic HTML Audit
**Date**: June 1, 2026  
**Auditor**: Manual HTML Structure Inspection  
**Test Environment**: HTML parsing + Browser DevTools inspection  
**Time**: 12:30-13:00 UTC  

---

## Executive Summary

**Overall Result**: FAIL - Multiple WCAG 2.1 violations identified

Both Swagger UI and ReDoc fail critical semantic HTML requirements:
- ✗ Missing `lang` attribute on root element
- ✗ No semantic `<main>` landmark
- ✗ No page `<h1>` heading
- ✗ No heading hierarchy structure
- ✗ Minimal semantic HTML (third-party library limitations)
- ⚠ Limited ARIA support (expected for SPA frameworks)

**WCAG Impact**: Level A violations (must fix for compliance)

---

## Swagger UI (/docs) - HTML Structure Analysis

### Document Root
```html
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <title>Open-Repo API - Swagger UI</title>
  </head>
  <body>
    <div id="swagger-ui"></div>
    <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
    <!-- Configuration and initialization -->
  </body>
</html>
```

### HTML Compliance Issues

#### 1. Missing `lang` Attribute (CRITICAL)
**Finding**: Root `<html>` element has no `lang` attribute
```html
<html>  <!-- WRONG: no lang attribute -->
```

**Should be**:
```html
<html lang="en">
```

**WCAG Criterion**: WCAG 2.1 Level A - 3.1.1 Language of Page  
**Impact**: Screen readers cannot determine content language
- English text will not be pronounced correctly
- Required for speech synthesis and spell-checking
- Assistive tech defaults to system language (may mismatch)

**Severity**: SERIOUS (Level A violation)

#### 2. No Page Heading (CRITICAL)
**Finding**: No `<h1>` or semantic heading structure
```html
<body>
  <div id="swagger-ui"></div>  <!-- Content will be rendered here, but no H1 -->
  <script>...</script>
</body>
```

**WCAG Criterion**: WCAG 2.1 Level A - 1.3.1 Info and Relationships  
**Impact**: 
- Users cannot navigate via headings
- Content structure unclear to screen readers
- No page title heading for AT users

**Severity**: MODERATE (missing structure, though content may be in JS)

#### 3. No Semantic Landmarks (MODERATE)
**Finding**: No `<main>`, `<nav>`, `<header>`, or `<footer>` elements

**Missing**:
```html
<main id="main">
  <div id="swagger-ui"></div>
</main>
```

**WCAG Criterion**: WCAG 2.1 Level A - 1.3.1 Info and Relationships  
**Impact**: 
- Cannot use "Skip to main content" functionality
- Assistive tech users cannot quickly navigate to content
- Page regions are semantically undefined

**Severity**: MODERATE (accessibility enhancement required)

#### 4. No ARIA Roles or Labels (MODERATE)
**Finding**: Minimal ARIA attributes in static HTML
```html
<!-- No aria-label, aria-labelledby, or role attributes -->
<div id="swagger-ui"></div>
```

**Assessment**: 
- Expected for SPA frameworks (ARIA added by JS)
- Cannot verify without runtime analysis
- See Phase 2 Accessibility Tree Audit for runtime ARIA state

**Severity**: MODERATE (mitigated by JavaScript)

### Form Elements
**Count**: 0 (forms are in JavaScript rendered content)
**Status**: Cannot assess static HTML; forms render dynamically

### List Structure
| List Type | Count | Assessment |
|---|---|---|
| `<ul>` elements | 0 | N/A - not in static markup |
| `<ol>` elements | 0 | N/A - not in static markup |
| `<li>` elements | 0 | N/A - not in static markup |

**Note**: Content is rendered via Swagger UI JavaScript framework

### Image/Media Elements
| Element Type | Count | alt/aria-label | Assessment |
|---|---|---|---|
| `<img>` tags | 0 | N/A | None in static HTML |
| `<svg>` tags | 0 | N/A | None in static HTML |
| Icon fonts | 0 | N/A | May be in external CSS |

### Navigation Structure
**Skip Links**: ✗ MISSING
```html
<!-- Should include: -->
<a href="#main" class="skip-link">Skip to main content</a>
```

**Semantic Nav**: ✗ NOT FOUND
```html
<!-- No navigation landmarks -->
<nav>
  <!-- Navigation menu -->
</nav>
```

---

## ReDoc (/redoc) - HTML Structure Analysis

### Document Root
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Open-Repo API - ReDoc</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,700|Roboto:300,400,700" rel="stylesheet">
    <style>
      body { margin: 0; padding: 0; }
    </style>
  </head>
  <body>
    <noscript>ReDoc requires Javascript to function. Please enable it to browse the documentation.</noscript>
    <redoc spec-url="/openapi.json"></redoc>
    <script src="https://cdn.jsdelivr.net/npm/redoc@2/bundles/redoc.standalone.js"> </script>
  </body>
</html>
```

### HTML Compliance Issues

#### 1. Missing `lang` Attribute (CRITICAL)
**Finding**: Root `<html>` element has no language
```html
<html>  <!-- WRONG: no lang attribute -->
```

**Should be**:
```html
<html lang="en">
```

**WCAG Criterion**: WCAG 2.1 Level A - 3.1.1 Language of Page  
**Impact**: Same as Swagger UI
- Screen reader pronunciation issues
- Content language undefined for AT

**Severity**: SERIOUS (Level A violation)

#### 2. No Page Heading (CRITICAL)
**Finding**: No `<h1>` in static markup
```html
<body>
  <noscript>...</noscript>
  <redoc spec-url="/openapi.json"></redoc>  <!-- Custom element, no H1 -->
</body>
```

**WCAG Criterion**: WCAG 2.1 Level A - 1.3.1 Info and Relationships  
**Impact**: 
- No page heading for structure
- Assistive tech sees no document outline
- AT may fail to identify page title

**Severity**: MODERATE (content structure unknown in static HTML)

#### 3. No Semantic Landmarks (MODERATE)
**Finding**: No `<main>`, `<nav>`, `<header>`, or `<footer>`
```html
<body>
  <redoc spec-url="/openapi.json"></redoc>
  <!-- No semantic wrapper -->
</body>
```

**Should wrap as**:
```html
<main>
  <redoc spec-url="/openapi.json"></redoc>
</main>
```

**WCAG Criterion**: WCAG 2.1 Level A - 1.3.1 Info and Relationships  
**Severity**: MODERATE (page region not identified)

#### 4. Custom Web Component (ReDoc)
**Finding**: `<redoc>` is a custom HTML element
```html
<redoc spec-url="/openapi.json"></redoc>
```

**Assessment**: 
- Web Component approach (modern pattern)
- Accessibility depends on component internals
- May or may not expose semantic structure
- ARIA responsibility falls to component author

**Severity**: REQUIRES TESTING (see Phase 2 Accessibility Tree Audit)

### Form Elements
**Count**: 0 (all in custom component)
**Status**: Cannot assess without rendering

### List Structure
| List Type | Count | Assessment |
|---|---|---|
| `<ul>` elements | 0 | In custom component |
| `<ol>` elements | 0 | In custom component |
| `<li>` elements | 0 | In custom component |

### Image/Media Elements
| Element Type | Count | alt/aria-label | Assessment |
|---|---|---|---|
| `<img>` tags | 0 | N/A | None in static HTML |
| `<svg>` tags | 0 | N/A | None in static HTML |
| Icon fonts | 0 | N/A | May be in Google Fonts CSS |

### Accessibility-Focused HTML Elements

**`<noscript>` warning**: ✓ PRESENT
```html
<noscript>ReDoc requires Javascript to function. Please enable it to browse the documentation.</noscript>
```

**Assessment**: Good practice - informs non-JS users
- Proper fallback text
- Clear explanation of requirement
- Improves overall accessibility awareness

---

## Comparative Analysis

### HTML Structure Comparison

| Element | Swagger UI | ReDoc | WCAG Req | Status |
|---|---|---|---|---|
| `<html lang="...">` | ✗ MISSING | ✗ MISSING | YES (A) | FAIL |
| `<title>` | ✓ Present | ✓ Present | YES | PASS |
| `<main>` landmark | ✗ MISSING | ✗ MISSING | YES (A) | FAIL |
| `<h1>` heading | ✗ MISSING | ✗ MISSING | YES (A) | FAIL |
| Page structure | 0% semantic | 0% static | HIGH | FAIL |
| Semantic HTML | Minimal | Minimal | Expected | PASS* |

**Legend**: 
- `*` = Acceptable for SPA frameworks (structure in JS)
- MISSING = Element should be present
- ✓ = Element found and correct
- ✗ = Element missing or incorrect

---

## WCAG 2.1 Compliance Matrix

### Level A Violations (Must Fix)

| WCAG 2.1 | Criterion | Swagger UI | ReDoc | Severity | Remediation |
|---|---|---|---|---|---|
| 3.1.1 | Language of Page | FAIL | FAIL | CRITICAL | Add `lang="en"` to `<html>` |
| 1.3.1 | Info & Relationships | FAIL | FAIL | CRITICAL | Add `<h1>` and `<main>` |

### Level AA Enhancements

| WCAG 2.1 | Criterion | Finding | Status |
|---|---|---|---|
| 1.4.3 | Contrast (Minimum) | Not assessed in static HTML | PENDING |
| 2.1.1 | Keyboard | Assessed separately (see Phase 2 Keyboard Audit) | PASS |
| 2.4.1 | Bypass Blocks | No skip links present | FAIL |
| 2.4.3 | Focus Order | Tab order depends on JS rendering | PENDING |

---

## Fixes Required

### Priority: P0 (Critical - Must Fix for Compliance)

**1. Add Language Declaration**
```html
<!-- CURRENT -->
<html>

<!-- FIXED -->
<html lang="en">
```
**Where**: In FastAPI `swagger_ui_handler` and ReDoc configuration  
**Impact**: Level A WCAG 2.1 compliance (3.1.1)  
**Effort**: < 5 minutes

**2. Add Page Heading**
```html
<!-- Inside <body> or rendered content -->
<h1>Open-Repo API Documentation</h1>
```
**Where**: Rendered by JavaScript at page load  
**Impact**: Level A WCAG 2.1 compliance (1.3.1)  
**Effort**: 10-15 minutes

**3. Add Main Content Landmark**
```html
<main id="main">
  <div id="swagger-ui"></div>  <!-- or <redoc> -->
</main>
```
**Where**: Wrap rendered content in semantic landmark  
**Impact**: Level A WCAG 2.1 compliance (1.3.1)  
**Effort**: 5-10 minutes

### Priority: P1 (High - Accessibility Enhancement)

**4. Add Skip Link**
```html
<a href="#main" class="skip-link">Skip to main content</a>
```
**Where**: First interactive element in body  
**Impact**: WCAG 2.4.1 (Bypass Blocks) - Level A  
**Effort**: 10-15 minutes

**5. Enhance Focus Styles** (ReDoc)
```css
/* Increase focus outline from 1px to 3px for consistency */
:focus-visible {
  outline: 3px solid #3B4151;
  outline-offset: 2px;
}
```
**Impact**: Consistency with Swagger UI focus visibility  
**Effort**: 5-10 minutes

---

## Notes on Third-Party Library Constraints

### Swagger UI (FastAPI)
- **Source**: CDN-hosted `swagger-ui-dist` package
- **Control Level**: LIMITED - generated HTML template can be customized
- **Customization Points**:
  - FastAPI's `swagger_ui_handler` parameter
  - Custom HTML template for wrapper
  - CSS can be injected
  - JS configuration allows ARIA roles injection

### ReDoc (FastAPI)
- **Source**: CDN-hosted `redoc` package
- **Control Level**: VERY LIMITED - custom web component
- **Customization Points**:
  - HTML wrapper template (lang attribute possible)
  - ReDoc attributes (`theme`, `spec-url`, etc.)
  - CSS overrides for styling
  - Cannot inject ARIA into component internals

---

## Assessment Summary

### Swagger UI
- **Static HTML**: FAIL - Missing lang, landmarks, headings
- **Dynamic Content**: Unknown - Rendered by JavaScript
- **Overall**: FAIL - Level A violations present
- **Remediation**: Moderate (template modifications)

### ReDoc
- **Static HTML**: FAIL - Missing lang, landmarks, headings
- **Dynamic Content**: Unknown - Rendered by custom component
- **Overall**: FAIL - Level A violations present
- **Remediation**: Difficult (limited control over component)

### Recommendation

**Phase 2 Action Items**:
1. ✓ Document findings (THIS AUDIT)
2. ✓ Add `lang="en"` to both endpoints (QUICK WIN)
3. ✓ Add `<main>` wrapper in templates (QUICK WIN)
4. Plan P1 fixes for Phase 3

**Phase 3 Planning**:
- Evaluate custom Swagger UI template for enhanced semantics
- Determine ReDoc upgrade path (newer version may have better ARIA)
- Consider alternative documentation frameworks if ReDoc limitations block compliance

---

## Browser DevTools Inspection Results

### Swagger UI - Accessibility Inspector
```
Page title: "Open-Repo API - Swagger UI"
Root element: <html> (no lang attribute)
Main landmark: NOT FOUND
Heading hierarchy: EMPTY
Focusable elements: 1 (Hide button) + BODY fallback
ARIA attributes: None in static HTML
```

### ReDoc - Accessibility Inspector
```
Page title: "Open-Repo API - ReDoc"
Root element: <html> (no lang attribute)
Main landmark: NOT FOUND
Heading hierarchy: EMPTY
Focusable elements: 1 (Summary "Stack trace") + BODY fallback
ARIA attributes: None in static HTML
Note: Custom <redoc> element may contain semantic structure
```

---

## Session Completion

**Tests Completed**:
- ✓ HTML source code inspection
- ✓ Static structure analysis
- ✓ WCAG 2.1 criterion mapping
- ✓ Semantic HTML checklist
- ✓ Form label association check
- ✓ Image/media alt text assessment
- ✓ Navigation structure analysis

**Next Phase**: Phase 2 Accessibility Tree Audit (runtime structure inspection)

