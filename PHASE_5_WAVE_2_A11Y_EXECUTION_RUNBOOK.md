---
title: "Phase 5 Wave 2 A11y Audit Execution Runbook"
project: open-repo
phase: 5
wave: 2
candidate: 3-A11y
execution_window: "June 1–6, 2026"
status: READY FOR JUNE 1 ACTIVATION
created: 2026-05-31
---

# Phase 5 Wave 2: A11y Audit Execution Runbook
## June 1–6, 2026

**Status**: All infrastructure ready. This runbook can be executed autonomously OR with user guidance.

**Time estimate**: 18–36 hours over 6 days
- June 1 (4h): Environment setup + automated scanning
- June 2–3 (8h): Manual keyboard + screen reader testing  
- June 4 (4h): Document findings + triage
- June 5–6 (4–12h): Fix P0 issues + write regression tests

---

## Prerequisites (Check Before June 1)

### 1. Environment Setup

#### 1.1 Python Dependencies
From `projects/open-repo/backend/`, install dev dependencies:

```bash
cd projects/open-repo/backend
uv pip install playwright pytest-playwright httpx
uv run playwright install chromium
```

**Verify**:
```bash
python3 -c "import playwright; print(f'Playwright {playwright.__version__} OK')"
```

#### 1.2 Node.js Dependencies (Optional but Recommended)
For standalone axe-core CLI audits (faster than browser-based):

```bash
npm install -D axe-core axe-puppeteer puppeteer
# Or install globally for easy CLI access
npm install -g axe-puppeteer
```

**Verify**:
```bash
npx axe --version
```

#### 1.3 Copy Test Files
From project root:

```bash
# Copy A11y test templates into backend/tests/
# (If not already present)
ls projects/open-repo/backend/tests/test_a11y_*.py
```

#### 1.4 Start Dev Server
In one terminal, keep the dev server running throughout the audit:

```bash
cd projects/open-repo/backend
uv run uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

**Verify** (in another terminal):
```bash
curl -s http://127.0.0.1:8000/api/exports/health | jq .
# Should return {"status": "ok", ...}
```

---

## June 1: Environment Setup + Automated Scanning (4 hours)

### Task 1.1: Dependency Installation (30 min)

```bash
cd projects/open-repo/backend

# Install browser testing dependencies
uv pip install playwright pytest-playwright

# Install Playwright browser
uv run playwright install chromium

# Verify
uv run pytest --version
```

**Success criteria**: `pytest --version` shows ≥7.4.0, Playwright browser installed

### Task 1.2: Start Dev Server (10 min ongoing)

Keep this running in a dedicated terminal:

```bash
cd projects/open-repo/backend
uv run uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
# Runs until explicitly stopped
```

**Success criteria**: Server logs show "Application startup complete"

### Task 1.3: Run Automated axe-core Scan (90 min)

#### Option A: Browser-based via pytest (Recommended for CI Integration)

```bash
cd projects/open-repo/backend

# Run the axe-core test suite
TEST_BASE_URL=http://127.0.0.1:8000 \
  uv run pytest tests/test_a11y_axecore.py -v -m accessibility --tb=short

# Generates JSON report in reports/accessibility_audit_<timestamp>.json
```

**Expected output**:
```
tests/test_a11y_axecore.py::test_axe_core_home_page PASSED
tests/test_a11y_axecore.py::test_axe_core_admin_page PASSED
tests/test_a11y_axecore.py::test_axe_core_health_endpoint PASSED
============ 3 passed in 12.34s =============
```

#### Option B: CLI-based via axe-puppeteer (Faster for Quick Scans)

```bash
# Requires npm packages from prerequisites

cd projects/open-repo
npx axe http://127.0.0.1:8000 \
  --tags wcag2a,wcag2aa,wcag21a,wcag21aa \
  --reporter json > /tmp/axe_report.json

# View results
jq '.violations | length' /tmp/axe_report.json  # Count violations
jq '.violations[].impact | group_by(.) | map({level: .[0], count: length})' /tmp/axe_report.json
```

**Expected output**: JSON report with violations grouped by impact level (critical, serious, moderate, minor)

### Task 1.4: Generate Initial Findings Summary (60 min)

Create `WCAG_AUDIT_BASELINE_FINDINGS.md`:

```bash
# Run both automated tools and compile results
cat > /tmp/audit_summary.md << 'EOF'
# Automated Audit Findings — June 1, 2026

## Scan Results Summary

| Tool | Pages Scanned | Violations Found | P0 (Critical) | P1 (Serious) | P2 (Moderate/Minor) |
|------|---|---|---|---|---|
| axe-core (browser) | 3 | [N] | [N] | [N] | [N] |
| axe-puppeteer (CLI) | 1 | [N] | [N] | [N] | [N] |

## Top 5 Issues by Impact

1. **[Issue Title]** — P[0-2], [# affected elements]
2. **[Issue Title]** — P[0-2], [# affected elements]
3. **[Issue Title]** — P[0-2], [# affected elements]
4. **[Issue Title]** — P[0-2], [# affected elements]
5. **[Issue Title]** — P[0-2], [# affected elements]

## Next Steps

Manual testing begins June 2 per `WCAG_2.1_AA_AUDIT_CHECKLIST.md`.
EOF

# Copy to project
cp /tmp/audit_summary.md projects/open-repo/WCAG_AUDIT_BASELINE_FINDINGS.md
```

---

## June 2–3: Manual Keyboard & Screen Reader Testing (8 hours)

### Setup Checklist

- [ ] Dev server still running (check Task 1.2 terminal)
- [ ] Read `WCAG_2.1_AA_AUDIT_CHECKLIST.md` (Section 1: Keyboard Navigation)
- [ ] Optional: Install screen reader (NVDA on Windows, Orca on Linux, VoiceOver on macOS)
- [ ] Disable mouse/trackpad for keyboard-only testing

### Task 2.1: Keyboard Navigation Audit (4 hours)

From `WCAG_2.1_AA_AUDIT_CHECKLIST.md` Section 1, test each criterion:

#### 2.1.1 Tab Order
1. Open http://127.0.0.1:8000 in Firefox
2. Disconnect/disable mouse
3. Press Tab repeatedly, document:
   - Which elements receive focus?
   - Does focus follow reading order (top-to-bottom, left-to-right)?
   - Are there unexpected gaps (focusable elements skipped)?
4. Repeat for `/admin/`, `/api/exports/health`

#### 2.1.2 Focus Visibility
1. Tab through each page again
2. For every focused element, verify:
   - Is focus indicator visible (outline, ring, or highlight)?
   - Can you see the focus from 3 feet away?
   - Does focus indicator have ≥3:1 contrast vs. background?
3. Document elements missing visible focus

#### 2.1.3 Keyboard Operation
1. For each interactive element (button, link, input, select):
   - Can it be activated with Tab+Enter?
   - Can buttons be activated with Tab+Space?
   - Can select elements be navigated with arrow keys?
2. Test any modals, dropdowns, carousels:
   - Can focus be trapped inside (expected) or escape (bug)?
   - Do arrow keys operate carousel/slider?

**Output file**: `KEYBOARD_AUDIT_FINDINGS_JUNE_2_3.md`

Template:
```markdown
# Keyboard Navigation Audit Findings

## Page: / (Home)

### 2.1.1 Tab Order
- [ ] PASS: Tab reaches all interactive elements
- [ ] PASS: Tab order matches visual reading order
- [ ] PASS: No keyboard traps
- [ ] FAIL: [Specific issue] — [selector], [steps to reproduce]

### 2.1.2 Focus Visibility  
- [ ] PASS: All focused elements have visible focus indicator
- [ ] FAIL: [Element] missing focus indicator — [selector]
- [ ] FAIL: [Element] focus contrast [ratio] < 3:1 — [color values]

### 2.1.3 Keyboard Operation
- [ ] PASS: All buttons activate with Enter + Space
- [ ] PASS: All links activate with Enter
- [ ] PASS: Modals/dropdowns operate correctly with Tab/Esc/arrows
- [ ] FAIL: [Component] does not respond to [key] — [selector], [expected vs. actual]

## Page: /admin/
[Repeat structure above]

## Summary
- PASS: [X] criteria
- FAIL: [Y] criteria (P0: [a], P1: [b], P2: [c])
```

### Task 2.2: Screen Reader Audit (4 hours)

Choose one: NVDA (Windows), Orca (Linux), VoiceOver (macOS)

#### VoiceOver (macOS) Setup
```bash
# Enable VoiceOver
# System Preferences → Accessibility → VoiceOver → Enable
# Or: Cmd + F5

# Start/stop VoiceOver in a test
# VO + U to open rotor (navigate by headings, links, landmarks)
# VO + Home to go to start of page
# VO + End to go to end
```

#### Screen Reader Test Protocol

For each page (/, /admin/), test:

1. **Page landmarks** (WCAG 1.3.1)
   - Does VoiceOver announce `<main>`, `<nav>`, `<aside>` landmarks?
   - Does each page have exactly one `<main>` landmark?
   - Are navigation regions labeled uniquely?

2. **Heading structure** (WCAG 1.3.1)
   - Use rotor to view heading hierarchy
   - Do headings start at h1?
   - Are there jumps (e.g., h1 → h3)?
   - Does each section have a heading?

3. **Image alt text** (WCAG 1.1.1)
   - For every image, does VoiceOver announce alt text?
   - Is alt text descriptive (not "image" or filename)?
   - Are decorative images marked `alt=""` or with `aria-hidden="true"`?

4. **Form labels** (WCAG 1.3.1 + 4.1.2)
   - Does each input have an associated label (announced by SR)?
   - Are required fields marked (`<span aria-label="required">`)?
   - Are validation messages tied to inputs (`aria-describedby`)?

5. **Interactive element labels** (WCAG 4.1.2)
   - Do icon buttons have aria-label or visible text?
   - Do links have descriptive text (not "click here")?
   - Are button states announced (pressed, expanded, disabled)?

6. **Live regions** (WCAG 4.1.3)
   - When search results load, does SR announce "X results found"?
   - Are notifications/alerts announced without page reload?

**Output file**: `SCREEN_READER_AUDIT_FINDINGS_JUNE_2_3.md`

Template:
```markdown
# Screen Reader Audit Findings

## Tool Used: [VoiceOver / NVDA / Orca]

## Page: / (Home)

### 1.3.1 Landmarks & Structure
- [ ] PASS: `<main>` landmark present and uniquely labeled
- [ ] PASS: All `<nav>` regions have unique aria-label
- [ ] PASS: Heading hierarchy h1 → h2 → h3 (no jumps)
- [ ] FAIL: [Landmark/heading issue] — [details]

### 1.1.1 Image Alt Text
- [ ] PASS: All images have descriptive alt text
- [ ] PASS: Decorative images marked `alt=""` or `aria-hidden`
- [ ] FAIL: [N] images missing alt text — [src examples]
- [ ] FAIL: [N] images have non-descriptive alt ("button", "photo") — [examples]

### 1.3.1 + 4.1.2 Form & Button Labels
- [ ] PASS: All inputs have associated labels
- [ ] PASS: Required fields marked
- [ ] PASS: Icon buttons have aria-label or text
- [ ] FAIL: [N] inputs missing labels — [name/id examples]
- [ ] FAIL: [N] icon buttons unlabeled — [class/selector examples]

### 4.1.3 Live Regions & Notifications
- [ ] PASS: Dynamic content announced via aria-live
- [ ] PASS: Validation errors announced immediately
- [ ] FAIL: Search results not announced on load — [element selector]

## Page: /admin/
[Repeat structure above]

## Summary
- PASS: [X] tests
- FAIL: [Y] tests (P0: [a], P1: [b], P2: [c])
```

---

## June 4: Findings Triage & Documentation (4 hours)

### Task 4.1: Consolidate All Findings (90 min)

Merge automated + keyboard + screen reader findings into one master document:

```bash
# Create master findings
cat > projects/open-repo/WCAG_AUDIT_CONSOLIDATED_FINDINGS_JUNE_4.md << 'EOF'
# Consolidated WCAG 2.1 AA Audit Findings — June 4, 2026

## Overview
- Automated audit (axe-core): [N] issues found
- Keyboard audit (manual): [N] issues found  
- Screen reader audit (manual): [N] issues found
- **Total unique issues: [N]**

## Severity Breakdown
- **P0 (WCAG Level A failure)**: [N] issues — must fix before release
- **P1 (WCAG Level AA failure)**: [N] issues — fix by June 6
- **P2 (Best practice / enhancement)**: [N] issues — backlog

## Issues by WCAG Criterion

### 1.1.1 Non-text Content (Images, Icons)
[Table of findings with issue, severity, count, examples]

### 1.3.1 Info & Relationships (Landmarks, Headings, Labels, Lists)
[Table of findings]

### 1.4.3 Contrast (Minimum)
[Table of findings]

### 2.1.1 Keyboard Access
[Table of findings]

### 2.4.7 Focus Visible
[Table of findings]

### 3.1.1 Language of Page
[Table of findings]

### 4.1.2 Name, Role, Value
[Table of findings]

### 4.1.3 Status Messages
[Table of findings]

## Remediation Roadmap

### P0 Fixes (Blocking — Due June 5)
1. [Issue X] — [fix method] — estimated 30 min
2. [Issue Y] — [fix method] — estimated 1 hour
...

**Total P0 effort: [hours]**

### P1 Fixes (Important — Due June 6)  
1. [Issue A] — [fix method] — estimated 20 min
2. [Issue B] — [fix method] — estimated 45 min
...

**Total P1 effort: [hours]**

### P2 Fixes (Backlog)
[List with estimated effort]

EOF

```

### Task 4.2: Severity Triage (60 min)

For each issue, assign severity:

**P0 (Block Release)**:
- WCAG Level A failure
- Examples: missing alt text on key images, keyboard trap, heading hierarchy broken, form labels missing
- Affects: >1% of users

**P1 (Must Fix This Window)**:
- WCAG Level AA failure  
- Examples: contrast < 4.5:1, focus indicator missing, aria-live region missing, status message not announced
- Affects: >5% of users or critical use case

**P2 (Backlog)**:
- WCAG Level AAA or best practice
- Examples: text resize to 200%, enhanced contrast, animation can be disabled
- Nice-to-have, not blocking

### Task 4.3: Fix Complexity Assessment (90 min)

For each P0 + P1 issue, estimate effort using `A11Y_FIX_COMPLEXITY_MATRIX.md`:

```markdown
| Issue | WCAG | Severity | Fix Type | Complexity | Estimate | File/Component |
|-------|------|----------|----------|-----------|----------|---|
| [Alt text missing from ZIM img] | 1.1.1 | P0 | Content/Template | Low | 2h | app/templates/zim_article.html |
| [Contrast #999 on #fff] | 1.4.3 | P1 | CSS | Low | 30m | app/static/style.css line 247 |
| [Heading h1→h3 jump] | 1.3.1 | P0 | Markup | Low | 1h | app/templates/base.html |
| [Modal focus trap missing] | 2.1.1 | P0 | JavaScript | Medium | 3h | app/static/modal.js |
| [Form label missing] | 4.1.2 | P0 | Markup | Low | 30m | app/templates/search.html |
```

---

## June 5–6: Fixes + Regression Tests (4–12 hours)

### Task 5.1: Fix P0 Issues (2–6 hours)

For each P0 issue in estimated severity order:

1. **Create feature branch**: `git checkout -b fix/a11y-p0-<issue-shortname>`
2. **Apply fix** per `A11Y_FIX_COMPLEXITY_MATRIX.md` remediation guidance
3. **Test fix**:
   ```bash
   # If markup fix:
   uv run pytest tests/test_a11y_dom_semantics.py -v -k <specific-test>
   
   # If CSS/contrast fix:
   uv run pytest tests/test_a11y_contrast.py -v
   
   # Manual verification:
   # — Keyboard test the fixed element
   # — Screen reader test if it affects SR-visible content
   ```
4. **Commit**: `git commit -m "fix(a11y): [issue title] — P0 WCAG 1.x.x"`
5. **Repeat** for next P0 issue

**Success criteria**: All P0 issues fixed, manual verification passed

### Task 5.2: Fix P1 Issues (1–4 hours)

Same process as Task 5.1, but for P1 severity:

```bash
git checkout -b fix/a11y-p1-<issue-shortname>
# ... apply fix ... test ... commit ...
```

**Success criteria**: All P1 issues fixed, manual verification passed

### Task 5.3: Write Regression Tests (1–2 hours)

Create automated tests for fixed issues to prevent future regressions:

```python
# Add to tests/test_a11y_regression.py

def test_form_labels_associated(browser_page):
    """All input elements have associated <label> (WCAG 1.3.1)"""
    page = browser_page
    page.goto("http://127.0.0.1:8000/")
    
    # Find all inputs without associated labels
    inputs = page.query_selector_all("input[id]:not(input[type='hidden'])")
    for inp in inputs:
        input_id = inp.get_attribute("id")
        # Verify a matching <label for="..."> exists
        label = page.query_selector(f'label[for="{input_id}"]')
        assert label is not None, f"<input id={input_id}> missing <label for='{input_id}'>"


def test_heading_hierarchy_no_jumps(browser_page):
    """Heading hierarchy h1→h2→h3 with no jumps (WCAG 1.3.1)"""
    page = browser_page
    page.goto("http://127.0.0.1:8000/")
    
    headings = page.query_selector_all("h1, h2, h3, h4, h5, h6")
    prev_level = 1
    for heading in headings:
        current_level = int(heading.evaluate("el => el.tagName[1]"))
        # Allow jump down multiple levels, but not up more than 1
        if current_level > prev_level:
            assert current_level <= prev_level + 1, \
                f"Heading jump: h{prev_level} → h{current_level} (expected h{prev_level} or h{prev_level+1})"
        prev_level = current_level
```

Run new tests:
```bash
uv run pytest tests/test_a11y_regression.py -v
```

---

## Deliverables (Due End of Day June 6)

### Required Documents

1. **`WCAG_AUDIT_BASELINE_FINDINGS.md`** (generated June 1)
   - Automated scan results summary

2. **`KEYBOARD_AUDIT_FINDINGS_JUNE_2_3.md`** (completed June 3)
   - Manual keyboard navigation test results per `WCAG_2.1_AA_AUDIT_CHECKLIST.md` Section 1

3. **`SCREEN_READER_AUDIT_FINDINGS_JUNE_2_3.md`** (completed June 3)
   - Manual screen reader test results

4. **`WCAG_AUDIT_CONSOLIDATED_FINDINGS_JUNE_4.md`** (delivered June 4)
   - Consolidated findings, triage, and remediation roadmap

5. **`A11Y_REGRESSION_TESTS.py`** (delivered June 6)
   - Pytest suite for automated A11y regression detection

### Git Commits

- Feature branches: `fix/a11y-p0-*`, `fix/a11y-p1-*` (one per issue)
- Merge to `main` after fixes pass manual verification
- Commit message format: `fix(a11y): [issue] — P[0-1] WCAG 1.x.x`

### Success Criteria

- [ ] All P0 issues fixed (100% pass)
- [ ] All P1 issues fixed (100% pass)
- [ ] Manual verification passed (keyboard + screen reader tests)
- [ ] Regression tests written and passing
- [ ] Findings consolidated in `WCAG_AUDIT_CONSOLIDATED_FINDINGS_JUNE_4.md`
- [ ] All files committed to `main` by EOD June 6

---

## Contingency Procedures

### If Manual Testing Reveals >30 P0 Issues

**Response**: Triage to identify root causes. Common patterns:
- Missing template landmark? Fix template once (affects all pages)
- CSS contrast issue? One CSS rule fix (affects all matching elements)
- Heading hierarchy? Fix in base.html (affects all pages)

**Benefit of consolidation**: Fixing one root cause often fixes 5–10 reported issues.

### If Findings Exceed June 6 Window

**Response**: Deploy P0 fixes (blocking); defer P1 to June 10–15 as post-deployment follow-up. Post-deployment P1 fixes do not block user release.

### If axe-core Flags False Positives

**Response**: Mark in `KNOWN_VIOLATIONS` set in `test_a11y_axecore.py`, document reason, plan fix for next cycle:

```python
# In test_a11y_axecore.py
KNOWN_VIOLATIONS = {
    "some-axe-rule-that-we-disagree-with"  # reason: custom ARIA pattern
}
```

---

## Reference

- **WCAG 2.1 AA Standard**: https://www.w3.org/WAI/WCAG21/quickref/
- **Checklist**: `WCAG_2.1_AA_AUDIT_CHECKLIST.md` (this project)
- **Fix Guidance**: `A11Y_FIX_COMPLEXITY_MATRIX.md` (this project)
- **Test Suite Setup**: `A11Y_AUTOMATED_TEST_SUITE.md` (this project)

---

## Sign-Off

**Status**: Ready for June 1 activation  
**Next step**: Begin Task 1.1 (dependency installation) on June 1, 08:00 UTC

Prepared: 2026-05-31 by orchestrator  
Approved for execution: [User signature / orchestrator autonomous execution]
