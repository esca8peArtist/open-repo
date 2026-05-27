---
title: "A11y Audit Findings Report — open-repo Phase 5.2 Wave 2"
project: open-repo
phase: "5.2"
wave: 2
candidate: 3-A11y
status: TEMPLATE — fill in during audit (June 1–6, 2026)
audit_target: "WCAG 2.1 Level AA"
auditor: "[Name]"
audit_date: "[Date of audit, e.g. 2026-06-01]"
report_version: "1.0 — baseline"
created: 2026-05-27
---

# A11y Audit Findings Report
## open-repo Phase 5.2 Wave 2

**Audit date**: [Fill in]
**Auditor**: [Name]
**Tools used**: axe-core [version], Lighthouse [version], WAVE, manual screen reader (Orca/NVDA)
**Compliance target**: WCAG 2.1 Level AA
**Scope**: All HTML surfaces served by open-repo backend at `http://127.0.0.1:8000`

**Summary**: [Fill in after audit — e.g., "27 violations found: 3 P0 (Level A), 12 P1 (Level AA), 12 P2. P0 fixes complete by June 4. P1 fixes complete by June 6."]

---

## Part 1: Baseline Audit Findings

*Fill in each table during the June 1–2 audit phase. One table per WCAG category.*
*Columns: Issue (description), WCAG Rule (success criterion ID), Severity (P0/P1/P2), Count (number of affected elements), Examples (up to 3 element selectors or URLs)*

### Category 1: Keyboard Navigation

| Issue | WCAG Rule | Severity | Count | Examples |
|-------|-----------|----------|-------|---------|
| [e.g., Tab focus skips main navigation] | 2.1.1 (A) | P0 | [N] | [`nav > ul > li:first-child a`] |
| [e.g., Modal dialog has keyboard trap — cannot exit with Esc] | 2.1.2 (A) | P0 | [N] | [`#search-modal`] |
| [e.g., Focus indicator missing on custom button component] | 2.4.7 (AA) | P1 | [N] | [`.btn-icon`, `.tag-chip`] |
| [e.g., Tab order does not match visual layout] | 1.3.2 (A) | P0 | [N] | [Sidebar renders after main in DOM but displays first] |
| | | | | |

**Category 1 total**: [X] violations ([Y] P0, [Z] P1, [W] P2)

### Category 2: Screen Reader Compatibility

| Issue | WCAG Rule | Severity | Count | Examples |
|-------|-----------|----------|-------|---------|
| [e.g., Icon buttons missing aria-label] | 4.1.2 (A) | P0 | [N] | [`button.close-btn`, `button.share-icon`] |
| [e.g., Images in ZIM articles missing alt text] | 1.1.1 (A) | P0 | [N] | [~42 images across 15 articles; `article img:not([alt])`] |
| [e.g., Heading jumps from h1 to h3 in article template] | 1.3.1 (A) | P0 | [N] | [ZIM article template: h1 (title) → h3 (section)] |
| [e.g., Dynamic search results not announced via aria-live] | 4.1.3 (AA) | P1 | [N] | [`#search-results` — no aria-live region] |
| [e.g., Navigation landmark missing aria-label — two <nav> elements] | 1.3.1 (A) | P0 | [N] | [Primary nav and secondary nav both unlabeled] |
| | | | | |

**Category 2 total**: [X] violations ([Y] P0, [Z] P1, [W] P2)

### Category 3: Color Contrast

| Issue | WCAG Rule | Severity | Count | Examples |
|-------|-----------|----------|-------|---------|
| [e.g., Footer links: #9E9E9E on #FFFFFF = 2.85:1, fails AA] | 1.4.3 (AA) | P1 | [N] | [`footer a { color: #9E9E9E }` — needs ≥4.5:1] |
| [e.g., Placeholder text: #BDBDBD on #FFFFFF = 1.73:1, fails] | 1.4.3 (AA) | P1 | [N] | [`input::placeholder { color: #BDBDBD }`] |
| [e.g., Error message: #F44336 on #FFFFFF = 3.99:1, fails] | 1.4.3 (AA) | P1 | [N] | [`.error-msg { color: #F44336 }` — use #C62828 for 6.1:1] |
| [e.g., Focus ring color: #90CAF9 on white = 2.0:1, fails 3:1 minimum] | 1.4.11 (AA) | P1 | [N] | [`:focus { outline-color: #90CAF9 }`] |
| | | | | |

**Category 3 total**: [X] violations ([Y] P0, [Z] P1, [W] P2)

### Category 4: Semantic Markup

| Issue | WCAG Rule | Severity | Count | Examples |
|-------|-----------|----------|-------|---------|
| [e.g., `<html>` element missing lang attribute] | 3.1.1 (A) | P0 | [1] | [`<html>` in base.html — add lang="en"] |
| [e.g., Form input missing associated label] | 1.3.1 (A) | P0 | [N] | [`<input id="search" type="text">` — no matching `<label for="search">`] |
| [e.g., Data table has no <caption> or <th> headers] | 1.3.1 (A) | P0 | [N] | [`table.export-list` — no headers or caption] |
| [e.g., Navigation not wrapped in <nav> landmark] | 1.3.1 (A) | P0 | [N] | [`<div class="nav-bar">` — should be `<nav>`] |
| [e.g., Multiple <h1> elements on admin page] | 1.3.1 (A) | P0 | [N] | [`/admin/` — 3 h1 elements found] |
| | | | | |

**Category 4 total**: [X] violations ([Y] P0, [Z] P1, [W] P2)

### Category 5: Form Accessibility

| Issue | WCAG Rule | Severity | Count | Examples |
|-------|-----------|----------|-------|---------|
| [e.g., Required fields not marked with required attribute or asterisk] | 3.3.2 (A) | P0 | [N] | [Admin create-user form: email field required but not marked] |
| [e.g., Error messages not associated with specific fields] | 3.3.1 (A) | P0 | [N] | [Error text placed above form, not adjacent to failing input] |
| [e.g., No autocomplete on username/email fields] | 1.3.5 (AA) | P1 | [N] | [Login form inputs — add autocomplete="username", "current-password"] |
| [e.g., Radio button group not wrapped in fieldset/legend] | 1.3.1 (A) | P0 | [N] | [Export format selector: 3 radio buttons, no fieldset] |
| | | | | |

**Category 5 total**: [X] violations ([Y] P0, [Z] P1, [W] P2)

### Category 6: Performance / Load Time

| Issue | WCAG Rule | Severity | Count | Examples |
|-------|-----------|----------|-------|---------|
| [e.g., OPDS /entries endpoint: 3.1s response (SLA: <2s)] | N/A (SLA) | P1 | [1] | [`GET /opds/v2/entries` — measured 3.1s avg over 5 runs] |
| [e.g., Admin page LCP: 4.2s (target: <3s)] | N/A (Lighthouse) | P2 | [1] | [Lighthouse reports LCP=4.2s on /admin/] |
| [e.g., Render-blocking CSS on main page] | N/A (Lighthouse) | P2 | [N] | [Lighthouse: "Eliminate render-blocking resources"] |
| | | | | |

**Category 6 total**: [X] violations ([Y] P0, [Z] P1, [W] P2)

---

## Part 2: Baseline vs. Post-Fix Comparison

*Fill in Part 2 column on June 5–6 after P0 and P1 fixes are complete.*

### Before / After Summary

| Category | Before (Baseline) P0 | Before P1 | Before P2 | After P0 | After P1 | After P2 |
|----------|---------------------|-----------|-----------|----------|----------|----------|
| 1. Keyboard Navigation | [X] | [X] | [X] | 0 | [X] | [X] |
| 2. Screen Reader | [X] | [X] | [X] | 0 | [X] | [X] |
| 3. Color Contrast | [X] | [X] | [X] | 0 | 0 | [X] |
| 4. Semantic Markup | [X] | [X] | [X] | 0 | 0 | [X] |
| 5. Form Accessibility | [X] | [X] | [X] | 0 | 0 | [X] |
| 6. Performance | [X] | [X] | [X] | N/A | [X] | [X] |
| **Total** | **[X]** | **[X]** | **[X]** | **0** | **[X]** | **[X]** |

### axe-core Pass Count (Before vs. After)

| Metric | Baseline (June 1) | Post-P0 Fixes (June 4) | Post-P1 Fixes (June 6) |
|--------|-------------------|------------------------|------------------------|
| axe-core violations (critical) | [N] | 0 (target) | 0 (target) |
| axe-core violations (serious) | [N] | 0 (target) | 0 (target) |
| axe-core violations (moderate) | [N] | [N] | ≤ 3 (target) |
| Lighthouse accessibility score | [N]/100 | [N]/100 | ≥ 90/100 (target) |

---

## Part 3: Fix Status Tracking

### P0 Fixes — Target: Complete by Day 3 (June 4)

| # | Issue (from Part 1) | Fix Description | Status | Commit | Notes |
|---|---------------------|----------------|--------|--------|-------|
| P0-01 | [Fill in — e.g., html lang missing] | Add `lang="en"` to `<html>` in base.html | [ ] Pending / [ ] In Progress / [x] Done | [commit hash] | |
| P0-02 | [Fill in] | | | | |
| P0-03 | [Fill in] | | | | |
| P0-04 | [Fill in] | | | | |
| P0-05 | [Fill in] | | | | |

### P1 Fixes — Target: Complete by Day 5 (June 6)

| # | Issue (from Part 1) | Fix Description | Status | Commit | Notes |
|---|---------------------|----------------|--------|--------|-------|
| P1-01 | [Fill in — e.g., footer link contrast] | Update footer CSS color from #9E9E9E to #6D6D6D | [ ] Pending / [ ] In Progress / [x] Done | | Designer review needed |
| P1-02 | [Fill in] | | | | |
| P1-03 | [Fill in] | | | | |
| P1-04 | [Fill in] | | | | |
| P1-05 | [Fill in] | | | | |

### P2 Fixes — Backlog (Phase 6)

| # | Issue | Backlog Item | Target Phase |
|---|-------|-------------|-------------|
| P2-01 | [Fill in — e.g., enhanced contrast 7:1] | CSS theming enhancement | Phase 6 |
| P2-02 | [Fill in] | | Phase 6 |
| P2-03 | [Fill in] | | Phase 6 |

---

## Part 4: Root Cause Analysis

*Complete this section per category. Explain why the issue exists structurally, not just symptomatically.*

### Category 1: Keyboard Navigation — Root Cause

[Fill in. Example: "Keyboard navigation failures on icon buttons are caused by the project using `<div>` elements with JavaScript `onclick` handlers instead of native `<button>` elements. Native buttons receive keyboard focus and respond to Enter/Space by default; divs do not. Root cause: CSS component library does not enforce semantic button usage in its icon variant."]

**Structural fix required**: [e.g., "Update `btn-icon` component to use `<button>` instead of `<div>`. Add ESLint rule `jsx-a11y/interactive-supports-focus` to prevent regression."]

### Category 2: Screen Reader Compatibility — Root Cause

[Fill in. Example: "Missing alt text on ZIM article images originates from the image import pipeline in `zim_writer.py`. When articles are scraped from source content, the `<img>` tags are copied without processing the `alt` attribute from the source. If the source has alt text, it is dropped during HTML normalization. If the source lacks alt text, no fallback is generated."]

**Structural fix required**: [e.g., "Modify `zim_writer.py`'s HTML sanitization step to: (1) preserve existing alt attributes from source content; (2) generate fallback alt text from the image filename or surrounding caption text if source alt is absent."]

### Category 3: Color Contrast — Root Cause

[Fill in. Example: "Color contrast failures in footer links and placeholder text are caused by the CSS design system using material design's default gray palette (#9E9E9E, #BDBDBD) without accessibility review. These grays look acceptable visually on high-contrast monitors but fail 4.5:1 WCAG AA on calibrated displays and fail on devices with reduced contrast settings."]

**Structural fix required**: [e.g., "Replace the three-tone gray palette with an accessibility-reviewed palette. Each gray value needs a corresponding dark variant that achieves 4.5:1 on white. Add a palette constraint table in design tokens so future designers can select from only compliant colors."]

### Category 4: Semantic Markup — Root Cause

[Fill in. Example: "The `<html lang>` attribute was omitted from `base.html` because the project templating system does not include it in the boilerplate. The form label association gaps exist because form components were built with visual design as primary constraint, without pairing `<label for=...>` to input `id` attributes."]

**Structural fix required**: [e.g., "Add `lang=\"en\"` to base.html immediately (one-line fix). Create a template linting rule using BeautifulSoup in `tests/test_a11y_dom_semantics.py` that catches unlabeled form inputs as a CI gate (already scaffolded in `A11Y_AUTOMATED_TEST_SUITE.md`)."]

### Category 5: Form Accessibility — Root Cause

[Fill in. Example: "Error messages are generated client-side by a JavaScript validation library that injects errors at the top of the form as a list, not adjacent to the offending field. WCAG 3.3.1 requires errors to be described in text (met) but also recommends they be associated with the specific field (not met). The radio button fieldset gap is due to the group being rendered by a custom component that wraps inputs in a styled `<div>` but omits the semantic `<fieldset>/<legend>` wrapper."]

**Structural fix required**: [e.g., "Update validation to inject error text as `aria-describedby` on the target input. Update the radio group component to use `<fieldset>/<legend>`."]

### Category 6: Performance — Root Cause

[Fill in. Example: "The OPDS `/entries` endpoint exceeds the 2-second SLA because the OPDSGenerator queries `zim_exports` without an index on `(is_current, status)`. On a database with 50+ export rows, the sequential scan takes 2.8s. Solution: add composite index in the next Alembic migration."]

**Structural fix required**: [e.g., "Add Alembic migration: `CREATE INDEX ix_zim_exports_current_status ON zim_exports(is_current, status);`"]

---

## Part 5: Remediation Evidence

*Fill in for each fix as it is completed. Link to the commit, include the before/after code snippet, and add screenshot proof where visual change occurred.*

### P0-01 Fix Evidence: [Issue Name]

**Commit**: `[git commit hash or PR link]`
**Files changed**: `[e.g., app/templates/base.html line 3]`

Before:
```html
<html>
```

After:
```html
<html lang="en">
```

**Verification**: `uv run pytest tests/test_a11y_dom_semantics.py::test_html_lang_attribute -v` → PASSED

---

### P0-02 Fix Evidence: [Issue Name]

**Commit**: `[git commit hash or PR link]`
**Files changed**: `[file path(s)]`

Before:
```html
<!-- Before code snippet here -->
```

After:
```html
<!-- After code snippet here -->
```

**Verification**: [Test command and result]

---

*(Add one block per P0 fix)*

---

### P1-01 Fix Evidence: [Issue Name]

**Commit**: `[git commit hash or PR link]`
**Files changed**: `[file path(s)]`

Before (contrast ratio: [X]:1):
```css
/* Before CSS snippet */
```

After (contrast ratio: [Y]:1):
```css
/* After CSS snippet */
```

**Verification**: WebAIM checker result: [ratio] on [URL]. Screenshot: [path to screenshot if applicable]

---

*(Add one block per P1 fix)*

---

## Part 6: Verification Section

### Re-Audit Results (June 6)

Run the following commands after all P0 and P1 fixes are merged:

```bash
# 1. axe-core re-audit
uv run pytest tests/test_a11y_axecore.py -v -m accessibility
# Expected: 0 critical/serious violations

# 2. OPDS smoke tests
uv run pytest tests/test_a11y_opds_smoke.py -v
# Expected: all pass, all response times < 2s

# 3. DOM semantics tests
uv run pytest tests/test_a11y_dom_semantics.py -v
# Expected: all pass

# 4. Lighthouse accessibility score
npx lighthouse http://127.0.0.1:8000 \
  --only-categories=accessibility \
  --chrome-flags="--headless --no-sandbox" \
  --output json --output-path reports/lighthouse_post_fix.json
# Expected: accessibility score ≥ 90/100
```

### Re-Audit Summary Table

| Metric | Baseline | Target | Post-Fix Actual | Pass? |
|--------|----------|--------|-----------------|-------|
| axe-core critical violations | [N] | 0 | [Fill in] | |
| axe-core serious violations | [N] | 0 | [Fill in] | |
| axe-core moderate violations | [N] | ≤ 3 | [Fill in] | |
| Lighthouse accessibility score | [N]/100 | ≥ 90 | [Fill in]/100 | |
| OPDS /root.xml response time | [Xs] | < 2s | [Fill in]s | |
| OPDS /entries response time | [Xs] | < 2s | [Fill in]s | |
| DOM semantics tests passing | [N]/[Total] | [Total]/[Total] | [Fill in] | |

### Regression Prevention

The following tests are now part of the standard CI pipeline and will catch regressions:

- `tests/test_a11y_axecore.py` — axe-core zero-violation gate (added to GitHub Actions)
- `tests/test_a11y_dom_semantics.py` — structural markup gate (added to test suite)
- `tests/test_a11y_opds_smoke.py` — OPDS SLA gate (added to pre-deployment checks)
- Lighthouse CI threshold: `accessibility` score ≥ 0.9 in `lighthouserc.js`

**Regression test commands (run any time)**:
```bash
uv run pytest tests/test_a11y_axecore.py tests/test_a11y_dom_semantics.py tests/test_a11y_opds_smoke.py -v
```

---

## Appendix: Audit Command Reference

```bash
# Full automated audit (all tools)
cd projects/open-repo/backend

# axe-core via pytest
uv run pytest tests/test_a11y_axecore.py -v -m accessibility --tb=short

# OPDS smoke tests
uv run pytest tests/test_a11y_opds_smoke.py -v

# DOM semantics
uv run pytest tests/test_a11y_dom_semantics.py -v

# Lighthouse batch
./scripts/run_lighthouse_batch.sh

# Pa11y CLI scan (supplement)
pa11y --standard WCAG2AA --reporter json http://127.0.0.1:8000 > reports/pa11y_baseline.json

# WAVE: open in browser
# Navigate to: https://wave.webaim.org/ → enter http://127.0.0.1:8000
```
