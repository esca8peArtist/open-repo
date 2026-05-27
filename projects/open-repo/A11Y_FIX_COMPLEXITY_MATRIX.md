---
title: "A11y Fix Complexity Matrix — open-repo Phase 5.2 Wave 2"
project: open-repo
phase: "5.2"
wave: 2
candidate: 3-A11y
status: ready-for-execution
execution_window: "June 1–6, 2026"
created: 2026-05-27
---

# A11y Fix Complexity Matrix
## open-repo Phase 5.2 Wave 2

**Purpose**: Before the audit begins, provide effort estimates and risk classifications for each category of WCAG fix. Engineers use this matrix to scope work during the June 1–6 window without waiting for the full audit findings.

**How to use this matrix**:
1. Run the audit (June 1–2) — identify which issue types exist
2. Cross-reference each finding's category with this matrix to get effort and risk estimates
3. Build the P0 fix queue for June 3–4 and P1 queue for June 5–6
4. Use the risk column to decide which fixes need QA review or designer input

---

## Fix Complexity Estimation Matrix

The master reference table. Issue types are listed by category. Effort ranges assume a single engineer working with the existing open-repo codebase.

| Issue Type | Category | Effort Estimate | Risk Level | Notes |
|------------|----------|----------------|------------|-------|
| Add `lang` attribute to `<html>` | Semantic markup | 0.25 hrs | Very low | Single one-line fix in `base.html` |
| Add alt text to images (batch, 10–30 images) | Screen reader | 1–3 hrs | Low | Requires content judgment for descriptive text; ~5 min/image |
| Add alt text to images (batch, 50+ images) | Screen reader | 4–8 hrs | Low | If ZimWriter pipeline change needed, add 2 hrs for template fix |
| Fix heading hierarchy (template-level) | Screen reader | 1–2 hrs | Low | Change h-levels in ZIM writer template; run ZIM rebuild to verify |
| Add `aria-label` to icon buttons | Screen reader | 1–2 hrs | Low | Identify all icon buttons; add `aria-label` attribute per element |
| Add `aria-live` region for dynamic content | Screen reader | 1–3 hrs | Low-Medium | Must verify screen reader announces correctly after implementation |
| Add `aria-label` to duplicate `<nav>` elements | Semantic markup | 0.5 hrs | Very low | `<nav aria-label="Primary">` and `<nav aria-label="Secondary">` |
| Add `<label for=...>` to form inputs | Form | 1–3 hrs | Low | One label per input; must verify `id` matches `for` attribute |
| Add `autocomplete` attributes to auth forms | Form | 0.5 hrs | Very low | `autocomplete="username"`, `"current-password"`, `"email"` |
| Wrap radio groups in `<fieldset>/<legend>` | Form | 1–2 hrs | Low | Requires template change + CSS update if styled inline |
| Associate error messages with fields (`aria-describedby`) | Form | 2–4 hrs | Medium | Requires JavaScript validation change; test error announcement |
| Mark required fields (`required` attribute or visual indicator) | Form | 0.5–1 hr | Low | Add `required` to inputs; add `*` to label with `aria-label="required"` |
| Fix keyboard trap in modal | Keyboard | 2–4 hrs | Medium | Focus management; requires testing with keyboard-only navigation |
| Add skip navigation link | Keyboard | 1 hr | Low | Add `<a href="#main" class="skip-link">Skip to main content</a>` |
| Fix tab order (DOM reordering) | Keyboard | 2–6 hrs | Medium | May require DOM restructuring; CSS visual order ≠ DOM order |
| Fix keyboard activation on custom components | Keyboard | 2–6 hrs | Medium | Replace `<div onclick>` with `<button>` or add `keydown` handler |
| Fix focus visibility — add focus ring CSS | Keyboard | 1–2 hrs | Low | Add `:focus-visible` CSS; verify contrast ≥ 3:1 |
| Update footer link color (contrast) | Color contrast | 0.5–1 hr | Low-Medium | Verify new color works visually; check with designer if brand color |
| Update placeholder text color (contrast) | Color contrast | 0.5 hrs | Very low | Single CSS variable change; verify 4.5:1 |
| Update error message color (contrast) | Color contrast | 0.5 hrs | Very low | Change #F44336 to #C62828 or darker red; verify ratio ≥ 4.5:1 |
| Update focus ring color (contrast) | Color contrast | 0.5 hrs | Low | `:focus { outline-color: [color] }` — verify 3:1 vs. adjacent colors |
| Overhaul color design system | Color contrast | 6–16 hrs | High | Only if systematic palette failure; requires designer input and review |
| Add database index for OPDS query | Performance | 0.5–1 hr | Low | Write Alembic migration; apply; measure response time improvement |
| Implement lazy loading for images | Performance | 2–4 hrs | Low-Medium | Add `loading="lazy"` to images; test visual impact |
| Implement asset optimization / bundling | Performance | 4–8 hrs | Medium | May affect CSS/JS build pipeline; potential regression risk |
| Add `<caption>` and `<th>` to data tables | Semantic markup | 1–2 hrs | Low | Structural HTML change per table; low rendering risk |
| Replace `<div>` nav with `<nav>` landmark | Semantic markup | 0.5–1 hr | Low | Tag change only; CSS selectors may need updating |
| Add `<main>` landmark | Semantic markup | 0.5 hrs | Very low | Wrap primary content in `<main>` |
| Fix multiple `<h1>` (dedup to one) | Semantic markup | 0.5–1 hr | Low | Restructure page template; demote duplicate h1s to h2 |
| ZimWriter: add alt text generation pipeline | Screen reader | 3–6 hrs | Medium | Code change in `zim_writer.py`; must rebuild test ZIM; run ZIM tests |

---

## Per-Category Fix Patterns

### Category 1: Keyboard Navigation

**Typical effort**: 2–8 hours per distinct issue type
**Risk**: Low to Medium (depends on whether DOM restructuring is required)
**QA needed**: Yes — keyboard-only navigation must be manually retested after each fix

**Fix patterns in this codebase**:

**Pattern 1 — Replace `<div onclick>` with `<button>`** (most common keyboard fix):
```html
<!-- Before (not keyboard accessible) -->
<div class="btn-icon" onclick="closeModal()">✕</div>

<!-- After (keyboard accessible; Enter + Space both work) -->
<button class="btn-icon" aria-label="Close modal" onclick="closeModal()">✕</button>
```

**Pattern 2 — Add skip navigation link** (first fix to do; very low risk):
```html
<!-- Add as first child of <body> in base.html -->
<a href="#main-content" class="skip-link">Skip to main content</a>
<style>
  .skip-link {
    position: absolute;
    top: -40px;
    left: 0;
    background: #000;
    color: #fff;
    padding: 8px;
    z-index: 9999;
    transition: top 0.2s;
  }
  .skip-link:focus { top: 0; }
</style>
```

**Pattern 3 — Fix focus trap in modal**:
```javascript
// Trap focus inside modal while open
function trapFocus(modal) {
  const focusable = modal.querySelectorAll(
    'a[href], button:not([disabled]), input, select, textarea, [tabindex="0"]'
  );
  const first = focusable[0];
  const last = focusable[focusable.length - 1];
  modal.addEventListener('keydown', (e) => {
    if (e.key !== 'Tab') return;
    if (e.shiftKey) {
      if (document.activeElement === first) { e.preventDefault(); last.focus(); }
    } else {
      if (document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });
}
```

**Regression test**: Run `uv run pytest tests/test_a11y_axecore.py -v -k "keyboard"` after each fix.

---

### Category 2: Screen Reader

**Typical effort**: 1–6 hours per issue type (1–3 hrs for markup changes; 3–6 hrs for pipeline changes)
**Risk**: Low for markup-only fixes; Medium if ZimWriter pipeline must be modified
**QA needed**: Manual screen reader verification after all fixes (Orca/NVDA; ~30 minutes)

**Fix patterns in this codebase**:

**Pattern 1 — Add alt text to icon buttons**:
```html
<!-- Before -->
<button class="share-btn"><img src="share.svg"></button>

<!-- After -->
<button class="share-btn" aria-label="Share this article">
  <img src="share.svg" alt="" aria-hidden="true">  <!-- decorative; aria-hidden hides from SR -->
</button>
```

**Pattern 2 — ZimWriter alt text generation** (pipeline fix, medium complexity):
```python
# In app/services/export/zim_writer.py
# Find: HTML normalization / sanitization step
# Add alt text preservation + fallback generation

def _normalize_image(self, img_tag) -> str:
    """Normalize an <img> tag, ensuring alt text is present."""
    src = img_tag.get("src", "")
    alt = img_tag.get("alt")

    if alt is None:
        # Try to get alt from surrounding figure caption
        parent = img_tag.parent
        caption = None
        if parent and parent.name == "figure":
            figcaption = parent.find("figcaption")
            if figcaption:
                caption = figcaption.get_text(strip=True)
        # Fallback: derive from filename
        if not caption:
            filename = src.split("/")[-1].rsplit(".", 1)[0]
            caption = filename.replace("-", " ").replace("_", " ").title()
        alt = caption

    img_tag["alt"] = alt
    return str(img_tag)
```

**Pattern 3 — Add aria-live for search results**:
```html
<!-- Search results container: add role and aria-live -->
<div id="search-results" role="region" aria-live="polite" aria-label="Search results">
  <!-- Results injected here by JavaScript -->
</div>
```

**Regression test**: `uv run pytest tests/test_a11y_axecore.py -v -k "screen_reader or image_alt or aria"` after fixes.

---

### Category 3: Color Contrast

**Typical effort**: 0.5–4 hours per issue (simple color changes: 0.5 hrs; design system overhaul: up to 16 hrs)
**Risk**: Low-Medium — color changes are low-risk technically but may affect brand identity; flag designer if any brand-color element changes
**QA needed**: Designer review if any primary brand colors are changed. Automated re-check via axe-core `color-contrast` rule.

**Fix patterns in this codebase**:

**Pattern 1 — Update footer link color (most common fix)**:
```css
/* Before: 2.85:1 on white — fails */
footer a { color: #9E9E9E; }

/* After: 5.74:1 on white — passes AA */
footer a { color: #6D6D6D; }
```

Verify: Enter `#6D6D6D` on white at [https://webaim.org/resources/contrastchecker/](https://webaim.org/resources/contrastchecker/). Expected ratio: 5.74:1. Pass for normal text (≥4.5:1).

**Pattern 2 — Fix red error message color**:
```css
/* Before: #F44336 on white = 3.99:1 — fails */
.error-message { color: #F44336; }

/* After: #C62828 on white = 6.1:1 — passes AA */
.error-message { color: #C62828; }
```

**Pattern 3 — Fix placeholder text contrast**:
```css
/* Before: #BDBDBD on white = 1.73:1 — fails */
input::placeholder { color: #BDBDBD; }

/* After: #757575 on white = 4.60:1 — passes AA */
input::placeholder { color: #757575; }
```

**Contrast ratio quick reference for common replacements**:

| Before (failing) | Ratio on white | Replacement | Ratio on white |
|-----------------|----------------|-------------|----------------|
| #9E9E9E (gray) | 2.85:1 | #767676 | 4.54:1 |
| #BDBDBD (light gray) | 1.73:1 | #757575 | 4.60:1 |
| #F44336 (Material red) | 3.99:1 | #C62828 (darker red) | 6.10:1 |
| #90CAF9 (light blue) | 1.67:1 | #1565C0 (dark blue) | 7.57:1 |
| #A5D6A7 (light green) | 1.59:1 | #2E7D32 (dark green) | 7.09:1 |

**Regression test**: `uv run pytest tests/test_a11y_axecore.py::test_axe_color_contrast_body_text -v` after each color fix.

---

### Category 4: Semantic Markup

**Typical effort**: 1–3 hours per issue type (structural HTML changes are low-risk)
**Risk**: Low — HTML structural changes do not affect Python/API logic
**QA needed**: Run DOM semantics test suite; spot-check with WAVE browser extension

**Fix patterns in this codebase**:

**Pattern 1 — Add `lang` attribute** (always do this first; 5 minutes):
```html
<!-- In app/templates/base.html, line 1 -->
<!-- Before: -->
<html>

<!-- After: -->
<html lang="en">
```

**Pattern 2 — Add `<main>` landmark**:
```html
<!-- In base.html, wrap primary content -->
<body>
  <header>...</header>
  <nav>...</nav>
  <main id="main-content">  <!-- id enables skip-link target -->
    {% block content %}{% endblock %}
  </main>
  <footer>...</footer>
</body>
```

**Pattern 3 — Fix data table headers**:
```html
<!-- Before: table with no headers -->
<table class="export-list">
  <tr><td>Open-Repo Full</td><td>English</td><td>22 MB</td></tr>
</table>

<!-- After: table with caption and scoped headers -->
<table class="export-list">
  <caption>Available ZIM Exports</caption>
  <thead>
    <tr>
      <th scope="col">Name</th>
      <th scope="col">Language</th>
      <th scope="col">Size</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Open-Repo Full</td><td>English</td><td>22 MB</td></tr>
  </tbody>
</table>
```

**Regression test**: `uv run pytest tests/test_a11y_dom_semantics.py -v` after each semantic fix.

---

### Category 5: Performance

**Typical effort**: 2–8 hours depending on root cause
**Risk**: Medium — database and caching changes require testing for correctness regressions
**QA needed**: Re-run OPDS smoke tests and existing test suite after any database change; run `uv run pytest tests/ -v` for full regression

**Fix patterns in this codebase**:

**Pattern 1 — Add database index for OPDS performance** (most likely fix):

Create a new Alembic migration:
```bash
cd projects/open-repo/backend
alembic revision --autogenerate -m "add_index_zim_exports_current_status"
```

Edit the generated migration file:
```python
def upgrade() -> None:
    op.create_index(
        "ix_zim_exports_current_status",
        "zim_exports",
        ["is_current", "status"],
    )

def downgrade() -> None:
    op.drop_index("ix_zim_exports_current_status", table_name="zim_exports")
```

Apply: `alembic upgrade head`

**Pattern 2 — Add caching headers to OPDS endpoints** (if response time is SLA-driven):
```python
# In app/api/v1/opds.py
from fastapi.responses import Response

@router.get("/entries")
async def get_entries_feed(...) -> Response:
    ...
    xml_bytes = generator.generate_acquisition_feed()
    return Response(
        content=xml_bytes,
        media_type="application/atom+xml",
        headers={"Cache-Control": "public, max-age=3600"},
    )
```

**Regression test**: `uv run pytest tests/test_a11y_opds_smoke.py -v` after performance fixes.

---

## P0/P1/P2 Severity Thresholds

### P0 — WCAG AA Blocking (Fix Before Release)

**Definition**: The issue completely prevents a user from accessing content or performing a task.

**Threshold criteria** (any one of these = P0):
- User cannot navigate the page with keyboard alone (keyboard trap, unreachable interactive element)
- Screen reader announces nothing meaningful for an interactive element
- Image has no alt text on a page where images convey primary information
- Form cannot be completed without a mouse
- Programmatic structure is absent (no page language, no headings, no landmarks)
- Content cannot be accessed by any assistive technology

**Example P0s in this project**:
- `<html>` missing `lang` attribute (screen reader cannot determine language)
- Icon button with no `aria-label` and no visible text
- Form input with no associated `<label>` (screen reader cannot identify the field)
- Keyboard trap inside a modal component

**Fix commitment**: All P0 issues fixed by **Day 3** (June 4) of the audit window. Zero P0 issues at production release.

---

### P1 — High User Impact (Fix Within Audit Window)

**Definition**: The issue significantly degrades the user experience for users relying on assistive technology, but does not completely prevent access.

**Threshold criteria** (any one of these = P1):
- Color contrast fails WCAG AA (4.5:1 for normal text, 3:1 for large text)
- Focus indicator is present but not sufficiently visible (fails 3:1 contrast threshold)
- Dynamic content updates are not announced to screen readers
- Error messages are present but not associated with specific fields
- Heading structure has skips but page is still navigable by headings
- OPDS endpoint exceeds 2-second SLA

**Example P1s in this project**:
- Footer links at 2.85:1 contrast (gray on white)
- `aria-live` region missing on search results
- Placeholder text at 1.73:1 contrast

**Fix commitment**: All P1 issues fixed by **Day 5** (June 6) of the audit window. P1 issues at release are acceptable only with written exception, time-bound to Phase 6 backlog.

---

### P2 — Nice-to-Have Improvements (Phase 6 Backlog)

**Definition**: The issue improves accessibility beyond WCAG AA requirements (often WCAG AAA), or addresses aesthetic/preference improvements.

**Threshold criteria**:
- WCAG AAA criterion (e.g., 7:1 enhanced contrast ratio)
- Cognitive accessibility enhancements (plain language, reading level)
- Pronunciation guidance for abbreviations
- Context help for complex forms
- Performance improvements beyond the 2-second SLA (e.g., targeting <1 second)

**Example P2s**:
- Enhanced contrast ratio to 7:1 (AAA) for users with severe low vision
- `<abbr title="...">` for medical abbreviations in ZIM content
- Simplified language review for non-expert users

**Fix commitment**: No fix deadline in Phase 5.2. Add to Phase 6 backlog. Track in `A11Y_AUDIT_FINDINGS_REPORT_TEMPLATE.md` Part 3 P2 backlog table.

---

## Prioritization Rules

### Rule 1: Fix P0 First, Sequence by User Count

When multiple P0 issues exist, fix in order of user impact:
1. Issues affecting ALL users on ALL pages (e.g., missing `<html lang>`, missing `<main>` landmark)
2. Issues affecting ALL users on HIGH-TRAFFIC pages (keyboard trap on main navigation)
3. Issues affecting SPECIFIC USERS on specific pages (icon button without label on admin page)

### Rule 2: Batch Similar P1 Fixes

Color contrast fixes are often batch-fixable in a single CSS change. Identify all contrast failures before making CSS edits — fixing the palette once (Pattern 3 in Category 3) resolves multiple P1 issues simultaneously.

### Rule 3: P0 Fixes Must Not Introduce New P0s

Every P0 fix must be followed by a targeted axe-core scan of the modified page before committing. A fix that accidentally introduces a new P0 (e.g., incorrect `aria-label` that is more confusing than no label) is worse than the original issue.

**After every P0 fix**:
```bash
uv run pytest tests/test_a11y_axecore.py::test_axe_no_critical_violations -v
```

### Rule 4: Flag Design-Affecting Fixes Before Implementing

Any fix that changes colors visible to all users, restructures the visual layout of the page, or modifies the font/heading visual hierarchy should be flagged to the designer (if applicable) before merging.

In open-repo's current phase, there is no separate designer — the engineer makes these decisions. In that case, use the contrast ratio quick-reference table in Category 3 and choose the darkest compliant value to avoid under-shooting.

### Rule 5: ZimWriter Fixes Require ZIM Rebuild

Any fix that modifies `app/services/export/zim_writer.py` templates (e.g., adding alt text generation, fixing heading structure in ZIM articles) requires:
1. Code change in `zim_writer.py`
2. Re-run the ZimWriter test suite: `uv run pytest tests/ -k "zim" -v`
3. Manual verification: rebuild a test ZIM and open in Kiwix to verify rendered HTML

This makes ZimWriter fixes take ~1 hour more than equivalent template fixes.

---

## Risk Mitigation

### Fixes That Require QA Review

| Fix Type | QA Required | Reason |
|----------|-------------|--------|
| Modal focus management changes | Yes | Focus trap bugs are subtle; requires keyboard-only testing by a second reviewer |
| CSS color palette changes | Yes (if brand colors affected) | Visual regression check; screenshot before/after |
| DOM restructuring (reorder elements for tab order) | Yes | Visual layout may shift; existing CSS selectors may break |
| ZimWriter template changes | Yes | Requires ZIM rebuild and Kiwix rendering verification |
| JavaScript validation changes (error messages) | Yes | Error state behavior must be manually tested in all error scenarios |

### Fixes That Require Designer Input

| Fix Type | Designer Input Required | Reason |
|----------|------------------------|--------|
| Any color change to a named brand color | Yes | Brand consistency; confirm replacement is acceptable |
| Heading visual hierarchy change | Optional | If h1–h6 font sizes are redesigned for both semantics and aesthetics |
| Focus ring redesign | Optional | Focus ring color and width affect overall UI appearance |

**In Phase 5.2 (no separate designer)**: Engineer makes these decisions. Document the rationale in the commit message. Err on the side of accessibility over visual preference.

### Regression Test Matrix

After all P0 and P1 fixes are complete, run the full regression check:

```bash
cd projects/open-repo/backend

# A11y regression (all categories)
uv run pytest tests/test_a11y_axecore.py \
               tests/test_a11y_dom_semantics.py \
               tests/test_a11y_opds_smoke.py \
               -v --tb=short

# Full test suite (regression for non-a11y tests)
uv run pytest tests/ -v --tb=short

# Expected: All 318 existing tests still passing + new a11y tests passing
```

---

## Effort Budget Summary

Using P-level totals from the audit findings, estimate total fix time:

| Category | Avg P0 fixes | Avg effort/fix | Total P0 | Avg P1 fixes | Avg effort/fix | Total P1 |
|----------|-------------|---------------|----------|-------------|---------------|----------|
| Keyboard | 1–3 | 2–4 hrs | 3–12 hrs | 1–2 | 1–2 hrs | 1–4 hrs |
| Screen Reader | 2–4 | 1–3 hrs | 2–12 hrs | 1–2 | 1–2 hrs | 1–4 hrs |
| Color Contrast | 0–1 | 0.5 hrs | 0–0.5 hrs | 2–5 | 0.5–1 hr | 1–5 hrs |
| Semantic Markup | 1–3 | 0.5–1 hr | 0.5–3 hrs | 0–1 | 1–2 hrs | 0–2 hrs |
| Form | 1–3 | 1–2 hrs | 1–6 hrs | 1–2 | 0.5–1 hr | 0.5–2 hrs |
| Performance | 0–1 | 0.5–1 hr | 0–1 hr | 0–1 | 1–3 hrs | 0–3 hrs |
| **Total estimate** | | | **7–34 hrs P0** | | | **4–20 hrs P1** |

**Realistic Phase 5.2 scope**: Based on a typical first-audit of a small web application (one developer, no legacy accessibility debt), expect:
- 3–7 P0 issues: 4–8 hours to fix
- 5–12 P1 issues: 4–8 hours to fix
- Total remediation: **8–16 hours** within the June 1–6 window

This aligns with the task brief estimate of "P0 fixes 1–3 hours (if simple CSS/ARIA)." Simple CSS/ARIA projects land at 4–8 hours; projects requiring ZimWriter pipeline changes or modal JavaScript refactoring land at the higher end.

---

## Sources

- [WCAG 2.1 — W3C Recommendation](https://www.w3.org/TR/WCAG21/)
- [WebAIM Color Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [axe-core GitHub — Deque Systems](https://github.com/dequelabs/axe-core)
- [WAVE Evaluation Tool](https://wave.webaim.org/)
- [WCAG 2.1 AA Compliance Guide — WebAbility 2026](https://www.webability.io/blog/wcag-2-1-aa-the-standard-for-accessible-web-design)
- [Level Access — WCAG Checklist for ADA Title II](https://www.levelaccess.com/resources/benchmark-ada-title-ii-compliance-the-must-have-wcag-checklist/)
- [Accessible.org — WCAG Checklist 2.1 AA](https://accessible.org/wcag/)
