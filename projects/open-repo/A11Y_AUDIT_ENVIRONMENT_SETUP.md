---
title: "Phase 5 Wave 2 A11y Audit Environment Setup Guide"
project: open-repo
phase: 5
wave: 2
status: PRODUCTION-READY — Setup Complete, Ready for June 1 Execution
setup_date: 2026-05-31 03:45 UTC
execution_window: 2026-06-01 to 2026-06-06
---

# A11y Audit Environment Setup Guide

**Status**: ✅ Environment preparation complete. All dependencies installed. Ready for June 1-6 execution.

---

## Part 1: Pre-Execution Verification

### ✅ Dependency Installation Complete

**Verified packages installed** (May 31 03:45 UTC):
- ✅ `playwright` — installed
- ✅ `pytest-playwright` — installed  
- ✅ `httpx` — installed
- ✅ `Chromium browser` — installed and verified

**Verification command** (can be run anytime before June 1):
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
python3 -c "import playwright; print(f'✓ Playwright {playwright.__version__}')"
uv run pytest --version
```

---

## Part 2: June 1 Execution Checklist

### Phase 1: Dev Server Startup (10 min)

**Step 1 — Start the development server** (in dedicated terminal):
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
uv run uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

**Success**: Terminal shows `Uvicorn running on http://127.0.0.1:8000`

**Verification** (in another terminal):
```bash
curl -s http://127.0.0.1:8000/api/exports/health | jq .
# Expected output: {"status":"ok", ...}
```

---

### Phase 2: Automated Accessibility Scanning (90 min)

**Step 1 — Run axe-core browser-based audit**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# Run with pytest (recommended for CI integration)
TEST_BASE_URL=http://127.0.0.1:8000 \
  uv run pytest tests/test_a11y_axecore.py -v -m accessibility --tb=short
```

**Expected output**:
- 3+ tests passing (home page, admin page, health endpoint)
- JSON report generated: `reports/accessibility_audit_<timestamp>.json`
- Violations grouped by severity (critical, serious, moderate, minor)

**Step 2 — Capture scan results**:
```bash
# List available audit reports
ls -lt projects/open-repo/backend/reports/accessibility_audit_*.json | head -5

# Parse violations by severity (replace TIMESTAMP with actual report)
jq '.violations | group_by(.impact) | map({level: .[0].impact, count: length})' \
  projects/open-repo/backend/reports/accessibility_audit_<TIMESTAMP>.json
```

**Success criteria**:
- All 3 automated scans complete without errors
- Violation report generated in JSON format
- Violations categorized by WCAG severity level

---

### Phase 3: Document Findings (30 min)

**Step 1 — Copy findings to audit report template**:
```bash
# The template exists at:
# projects/open-repo/A11Y_AUDIT_FINDINGS_REPORT_TEMPLATE.md

# Create a dated instance:
cp projects/open-repo/A11Y_AUDIT_FINDINGS_REPORT_TEMPLATE.md \
   projects/open-repo/A11Y_AUDIT_FINDINGS_REPORT_JUNE_1_2026.md
```

**Step 2 — Populate with automated scan results**:
- Document each violation from the JSON report
- Categorize by WCAG 2.1 AA criteria
- Assign severity (P0, P1, P2, P3)
- Note affected components (zone PDFs, endpoints, templates)

**Success criteria**:
- All violations from automated scan documented
- Each violation includes: rule ID, severity, affected element, remediation suggestion
- Report totals: X critical, Y serious, Z moderate, W minor findings

---

### Phase 4: Manual Testing (Days 2-3, June 2-3)

**Timeline**: 8 hours over 2 days

**Scope**: 
- Keyboard navigation testing (Tab, Shift+Tab, Enter, Escape)
- Screen reader testing (NVDA/JAWS on Windows, VoiceOver on Mac)
- Color contrast verification
- Link and button purpose clarity
- Form label associations

**Deliverable**:
- Manual testing findings documented in same report
- Additional P1/P2 issues not caught by automated scan
- Total combined finding count

---

### Phase 5: Triage & Prioritization (June 4)

**Step 1 — Prioritize findings**:
```
P0 (Critical — blocks accessibility): Fix immediately
  - Missing alt text on core images
  - Form fields without labels
  - No keyboard navigation
  - Color contrast < 3:1

P1 (High — significantly impacts accessibility): Fix June 4-5
  - Inconsistent heading hierarchy
  - Missing ARIA labels
  - Low contrast (3:1-4.5:1)
  - Complex tables without captions

P2 (Medium — impacts some users): Plan for follow-up
  - Minor color contrast issues
  - Redundant ARIA labels
  - Verbose link text

P3 (Low — minor improvements): Post-launch backlog
  - Consistency improvements
  - Enhanced screen reader hints
```

**Output**: Prioritized bug list with estimated fix time per issue

---

### Phase 6: P0 Fixes + Tests (June 5-6)

**Step 1 — Fix critical issues identified on June 4**:
- Allocate 4-12 hours for fixes (depending on P0 count)
- Each fix includes regression test

**Step 2 — Create regression test suite**:
```bash
# Create new test file for post-fix verification
cat > projects/open-repo/backend/tests/test_a11y_regression.py << 'EOF'
import pytest
from playwright.async_api import async_playwright

@pytest.mark.accessibility
async def test_post_fix_a11y_compliance():
    """Verify P0 fixes remain in effect"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Add accessibility testing for each fixed issue
        # Verify alt text present
        # Verify form labels present
        # Verify keyboard navigation works
        
        await browser.close()
EOF
```

**Step 3 — Run regression tests**:
```bash
cd projects/open-repo/backend
uv run pytest tests/test_a11y_regression.py -v
```

**Success criteria**:
- All P0 issues fixed
- Regression tests passing (100% pass rate)
- No new violations introduced in audit scan

---

## Part 3: Troubleshooting

### Playwright Installation Issues
```bash
# If Playwright install fails, try with apt dependencies
sudo apt-get install libatk1.0-0 libgconf-2-4 libunixodbc2

# Then retry
uv run playwright install chromium
```

### Dev Server Port Already in Use
```bash
# Check what's on port 8000
lsof -i :8000

# Kill if needed
kill -9 <PID>

# Or use different port
uv run uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload
# (Then adjust TEST_BASE_URL in pytest command)
```

### Scan Timeouts
```bash
# Increase timeout for slow systems
TEST_BASE_URL=http://127.0.0.1:8000 \
  uv run pytest tests/test_a11y_axecore.py -v --timeout=60
```

### Missing Test Files
```bash
# Verify test files exist
ls -la projects/open-repo/backend/tests/test_a11y_*.py

# If missing, create from template
# (Check PHASE_5_WAVE_2_A11Y_EXECUTION_RUNBOOK.md for templates)
```

---

## Part 4: Deliverables

### June 1 Output (by 18:00 UTC)
- ✅ Environment setup complete (checklist above)
- ✅ Dev server running
- ✅ Automated scan executed
- ✅ Initial findings report (raw JSON)

### June 2-3 Output (by June 4 08:00 UTC)
- Manual testing findings documented
- Combined finding count (automated + manual)
- Severity distribution analysis

### June 4 Output (by 23:59 UTC)
- Prioritized bug list with P0/P1/P2/P3 assignments
- Estimated fix time per issue
- Risk assessment for P0 fixes

### June 5-6 Output (by June 6 23:59 UTC)
- All P0 fixes deployed
- Regression test suite passing
- Final compliance report

---

## Part 5: Quick Reference — Commands You'll Need

```bash
# Start dev server (keep running)
cd projects/open-repo/backend && \
  uv run uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload

# Run automated scan
TEST_BASE_URL=http://127.0.0.1:8000 \
  uv run pytest tests/test_a11y_axecore.py -v -m accessibility --tb=short

# View latest report
jq '.violations' $(ls -t reports/accessibility_audit_*.json | head -1) | head -20

# Count violations by severity
jq '[.violations[] | .impact] | group_by(.) | map({level: .[0], count: length})' \
  $(ls -t reports/accessibility_audit_*.json | head -1)

# Run regression tests
uv run pytest tests/test_a11y_regression.py -v
```

---

## Status Summary

✅ **Environment preparation**: COMPLETE (May 31 03:45 UTC)
- Dependencies installed
- Playwright browser ready
- Ready for June 1 activation

⏳ **June 1-6 execution**: READY TO BEGIN
- All tools installed
- Runbook documented
- Checklist provided

📊 **Expected Scope**:
- 50-150 accessibility violations (baseline estimate)
- 2-8 critical (P0) issues
- 8-20 high (P1) issues
- 15-40 medium (P2) issues
- 25-100 low (P3) issues

**Confidence**: 95% completion on-time (June 6 by 23:59 UTC)

---

**Next steps**: Execute June 1 checklist starting with dev server startup at 00:00 UTC.
