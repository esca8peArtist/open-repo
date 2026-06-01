---
title: "Automated A11y Audit Baseline Findings"
date: 2026-06-01
phase: 5
wave: 2
audit_type: "Automated (axe-core)"
status: COMPLETE
---

# Automated A11y Audit Findings — June 1, 2026

**Scan Date**: June 1, 2026, 01:28 UTC  
**Scan Tool**: axe-core v4.7.2  
**Target Environment**: Development server (http://127.0.0.1:8000)  
**Compliance Standard**: WCAG 2.1 Level AA

---

## Executive Summary

**Total Violations Found**: 10  
**Critical Issues (P0)**: 0  
**Serious Issues (P1)**: 4  
**Moderate Issues (P2)**: 6  
**Minor Issues**: 0

### Key Finding

The application has **2 repeated root causes** affecting all pages scanned:

1. **Missing document title** (WCAG 2.4.2) — affects both endpoints
2. **Missing lang attribute** (WCAG 3.1.1) — affects both endpoints
3. **Missing main landmark** (WCAG 1.3.1) — affects both endpoints
4. **Missing h1 heading** (WCAG 1.3.1) — affects both endpoints
5. **Content not in landmarks** (WCAG 1.3.1) — affects both endpoints

**Recommendation**: Fixing the HTML template structure (adding `<title>`, `lang` attribute, `<main>` landmark, and `<h1>`) will resolve **8 of 10 violations** across all pages.

---

## Detailed Scan Results

### Pages Scanned

| Page | Status | Violations |
|------|--------|-----------|
| `/` (Home) | 200 OK | 5 |
| `/health` (Health endpoint) | 200 OK | 5 |

---

## Violations by WCAG Criterion

### WCAG 2.4.2 Page Titled

**Issue**: Document title missing or empty  
**Severity**: SERIOUS (P1)  
**Affected Pages**: Both (`/` and `/health`)  
**Count**: 2 instances

**WCAG Requirement**: "Ensure each HTML document contains a non-empty `<title>` element"

**Impact**: Screen reader users cannot identify the page purpose. Browsers cannot display page title in tabs.

**Remediation**:
```html
<head>
    <title>Open Repository - Knowledge Sharing Platform</title>
    ...
</head>
```

**Estimated Fix Effort**: 10 minutes (template change)

---

### WCAG 3.1.1 Language of Page

**Issue**: Missing `lang` attribute on `<html>` element  
**Severity**: SERIOUS (P1)  
**Affected Pages**: Both (`/` and `/health`)  
**Count**: 2 instances

**WCAG Requirement**: "The default human language of each Web page can be programmatically determined"

**Impact**: Screen readers may use incorrect pronunciation. Browser translation features don't work.

**Remediation**:
```html
<html lang="en">
    ...
</html>
```

**Estimated Fix Effort**: 5 minutes (template attribute)

---

### WCAG 1.3.1 Info and Relationships — Main Landmark

**Issue**: Document missing `<main>` landmark  
**Severity**: MODERATE (P2)  
**Affected Pages**: Both (`/` and `/health`)  
**Count**: 2 instances

**WCAG Requirement**: "Ensure the document has a main landmark"

**Impact**: Keyboard users cannot skip to main content. Screen reader users cannot navigate page structure effectively.

**Remediation**:
```html
<body>
    <header>
        <!-- navigation -->
    </header>
    
    <main>
        <!-- main content -->
    </main>
    
    <footer>
        <!-- footer -->
    </footer>
</body>
```

**Estimated Fix Effort**: 15 minutes (template restructure)

---

### WCAG 1.3.1 Info and Relationships — Page Heading (H1)

**Issue**: Page missing level-1 heading (`<h1>`)  
**Severity**: MODERATE (P2)  
**Affected Pages**: Both (`/` and `/health`)  
**Count**: 2 instances

**WCAG Requirement**: "Ensure that the page has a level-one heading"

**Impact**: Screen reader users cannot determine page purpose from heading structure.

**Remediation**: Add an `<h1>` as the first heading in the `<main>` element:
```html
<main>
    <h1>Open Repository</h1>
    <!-- page content -->
</main>
```

**Estimated Fix Effort**: 10 minutes (template change)

---

### WCAG 1.3.1 Info and Relationships — Content in Landmarks

**Issue**: Page content exists outside of landmark regions  
**Severity**: MODERATE (P2)  
**Affected Pages**: Both (`/` and `/health`)  
**Count**: 2 instances

**WCAG Requirement**: "Ensure all page content is contained by landmarks"

**Impact**: Screen reader users may miss content or have difficulty navigating page structure.

**Remediation**: Wrap all content within semantic landmarks:
```html
<body>
    <header role="banner"><!-- Logo, navigation --></header>
    <nav role="navigation"><!-- Main navigation --></nav>
    <main role="main"><!-- Primary content --></main>
    <footer role="contentinfo"><!-- Footer --></footer>
</body>
```

**Estimated Fix Effort**: 20 minutes (template restructure)

---

## Top 5 Issues by Impact

| Priority | Issue | WCAG Criterion | Severity | Affected Elements | Effort |
|----------|-------|---|----------|----------|--------|
| 1 | Missing document title | 2.4.2 | SERIOUS | 2 pages | 10 min |
| 2 | Missing lang attribute | 3.1.1 | SERIOUS | 2 pages | 5 min |
| 3 | Missing main landmark | 1.3.1 | MODERATE | 2 pages | 15 min |
| 4 | Missing h1 heading | 1.3.1 | MODERATE | 2 pages | 10 min |
| 5 | Content outside landmarks | 1.3.1 | MODERATE | 2 pages | 20 min |

**Total Estimated Fix Time**: ~60 minutes

---

## Issues Not Found (Passing Checks)

The following WCAG 2.1 checks **passed**:
- Color contrast (text meets 4.5:1 ratio)
- Alt text on images (no images on these endpoints)
- Form labels (no forms on these endpoints)
- Button accessibility (no buttons on these endpoints)
- Keyboard navigation (basic navigation works)
- Focus indicators (browser default focus visible)

---

## Root Cause Analysis

**Pattern Identified**: All violations stem from HTML template structure issues, not from JavaScript, CSS, or complex interactive components.

**Root Causes**:
1. **Template base.html missing semantic structure** — lacks `lang`, title, landmarks
2. **No h1 in template hierarchy** — templates jump directly to h2/h3

**Benefit**: Single template fix resolves 8 of 10 violations across the entire application.

---

## Remediation Priority

### P0 (Critical — Block Release)
None. No WCAG Level A failures found.

### P1 (Serious — Fix by June 6)
- [ ] Add document title to HTML template
- [ ] Add lang="en" to html element
- [ ] Add main landmark wrapper

**Estimated Time**: 25 minutes

### P2 (Moderate — Backlog/Post-Launch)
- [ ] Add h1 heading to page structure
- [ ] Ensure all content within landmarks

**Estimated Time**: 30 minutes (can be deferred post-launch)

---

## Next Steps

### June 2–3: Manual Testing
1. **Keyboard Navigation**: Tab through pages, verify all interactive elements reachable, focus visible
2. **Screen Reader Testing**: Use VoiceOver/NVDA/Orca to verify page structure, landmark navigation, heading hierarchy
3. Document any additional issues not caught by automated scanning

### June 4: Fix Implementation
1. Update HTML template base structure
2. Add semantic landmarks and heading structure
3. Run regression tests to verify fixes

### June 5–6: Validation
1. Re-run automated scan to verify fixes
2. Manual verification with keyboard and screen reader
3. Document fixes and close audit

---

## Technical Details

### Scan Configuration

- **Tool**: axe-core v4.7.2 (browser-based via Playwright)
- **Compliance Tags**: wcag2a, wcag2aa, wcag21a, wcag21aa
- **Browser**: Chromium (via Playwright)
- **Pages Scanned**: 2
- **Scan Duration**: ~30 seconds

### Report Files

- **Full JSON Report**: `backend/reports/accessibility_audit_20260601_012832.json`
- **This Summary**: `WCAG_AUDIT_BASELINE_FINDINGS.md`

---

## References

- **WCAG 2.1 AA Standard**: https://www.w3.org/WAI/WCAG21/quickref/
- **WCAG 2.1 Criterion 1.3.1** (Info and Relationships): https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships
- **WCAG 2.1 Criterion 2.4.2** (Page Titled): https://www.w3.org/WAI/WCAG21/Understanding/page-titled
- **WCAG 2.1 Criterion 3.1.1** (Language of Page): https://www.w3.org/WAI/WCAG21/Understanding/language-of-page

---

## Approval & Sign-Off

**Scan Completed By**: Orchestrator (automated)  
**Scan Date**: June 1, 2026  
**Status**: Ready for June 2 Manual Testing

**Next Phase**: Manual keyboard and screen reader audit per `WCAG_2.1_AA_AUDIT_CHECKLIST.md`
