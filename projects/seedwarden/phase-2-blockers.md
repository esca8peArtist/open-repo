---
title: "Seedwarden Phase 2 — Blockers Register"
created: 2026-04-30
last_updated: 2026-04-30
session: 662
status: active — 2 blockers open, 1 advisory
cross-references:
  - phase-2-execution-log.md (mockup sourcing status)
  - pin-production-schedule.md (scheduling tool and timeline)
  - phase-2-mockup-sourcing-inventory.md (slug reference)
---

# Phase 2 Blockers Register

This file tracks active blockers, advisories, and resolved items for Phase 2. A blocker is anything that stops a specific action from proceeding. An advisory is a discrepancy or risk that does not stop work but must be resolved before downstream steps.

Update this file when a blocker is resolved or a new one is identified.

---

## Active Blockers

### BLOCKER-01 — Canva Brand Kit Not Configured

**Type**: User action required
**Impact**: Blocks all pin template builds and all batch pin production
**Downstream impact**: Delays Week 1 pin launch until resolved

**What is blocked**:
- All 9 master template builds in Canva (`phase-2-canva-pin-production-checklist.md` Section 2)
- All batch pin production sessions (Section 3)
- Pinterest native scheduler setup (no pins to schedule yet)

**Resolution required**:
- User logs into Canva at canva.com
- Navigates to Brand Hub > Create a Brand Kit
- Adds 6 hex colors, 3 fonts, and logo — exact specifications in `phase-2-canva-pin-production-checklist.md` Section 1.1
- Estimated time to resolve: 30 minutes

**What is NOT blocked by this**:
- Stock image sourcing sprint (iStock, Pexels, Wikimedia) — no Canva dependency
- Physical shoot scheduling and props acquisition
- `assets/stock-raw/` directory staging
- Compositing stock images (uses Canva, but compositing workflow is separate from pin templates and can use Brand Kit colors once configured)

**Status**: OPEN as of 2026-04-30
**Resolution date**: Pending user action

---

### BLOCKER-02 — Lifestyle Photography Not Started (Slots 4–5)

**Type**: Production dependency
**Impact**: Blocks Template 3 lifestyle flat-lay pins (10 pins) and Template 5 photo-background carousel variants
**Downstream impact**: Full 50–60 pin library cannot complete until lifestyle images exist; however, 30–40 pins (Templates 1, 2, 4, and carousel covers) are buildable without lifestyle images

**What is blocked**:
- Template 3 pins (lifestyle flat-lay) for all 21 products
- Photo-background variant of Template 2 educational pins
- Photo-background variant of Template 5 carousel covers
- Etsy slot 4 and slot 5 uploads for all 21 products

**Partial resolution path**:
- Cluster D stock sourcing (4 products, 8 images) unblocks 5 lifestyle flat-lay pins first
- Physical shoots (Clusters C, A, B) unblock remaining 15 products in sequence

**Resolution schedule** (per `pin-production-schedule.md` Part B):
- Cluster D stock images: Week 2 (May 7–13)
- Cluster C physical shoot: Week 2 (May 7–13) — requires props on hand
- Clusters A + B physical shoot: Week 3 (May 14–20)
- All 42 lifestyle images complete: Week 4 (May 21–27)

**Status**: OPEN — structural dependency, resolves on rolling basis as each cluster completes

---

## Advisories (Non-Blocking)

### ADVISORY-01 — Slug Inconsistency: Hunting Manual

**Type**: Documentation discrepancy
**Impact**: Low — does not block any current work; must be resolved before final file exports

**Description**: The search string in `phase-2-mockup-sourcing-inventory.md` (and some sections of `phase-2-mockup-production-plan.md`) references the slug as `hunting-fishing-trapping-manual`. The actual mockup files in `projects/seedwarden/mockups/` use the slug `hunting-fishing-trapping-field-manual` (with `-field-` in the slug).

Verified actual filename in mockups directory:
- `hunting-fishing-trapping-field-manual-mockup.png` ✓
- `hunting-fishing-trapping-field-manual_interior.png` ✓
- `hunting-fishing-trapping-field-manual_phone.png` ✓

**Correct slug**: `hunting-fishing-trapping-field-manual`

**Resolution required before**: Compositing and exporting slot 4 and 5 images. The staged source files must use the correct slug to match the naming convention: `hunting-fishing-trapping-field-manual-source-1.jpg`, `hunting-fishing-trapping-field-manual-slot4.jpg`, etc.

**No document edits required now** — the sourcing inventory search strings are still valid; only the output filename convention is affected. Record the correct slug at compositing time.

**Status**: OPEN — advisory only, non-blocking

---

## Resolved Blockers

No blockers resolved yet. This section will populate as production proceeds.

---

## Blocker Summary Table

| ID | Description | Type | Blocks | Status |
|----|-------------|------|--------|--------|
| BLOCKER-01 | Canva Brand Kit not configured | User action | All pin template builds and batch sessions | OPEN |
| BLOCKER-02 | Lifestyle photos not yet produced | Production dependency | Template 3 + photo-background Template 2/5 pins; all Etsy slot 4/5 uploads | OPEN |
| ADVISORY-01 | Slug inconsistency — Hunting Manual | Documentation | Output filename at compositing time | OPEN |
