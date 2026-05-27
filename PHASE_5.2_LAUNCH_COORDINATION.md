---
title: "Phase 5.2 Launch Coordination"
project: open-repo
phase: "5.2"
document_type: launch-coordination
status: pre-activation (decision gate June 1)
created: 2026-05-27
decision_deadline: "June 1, 2026 09:00 UTC"
target_completion: "July 1, 2026"
depends_on:
  - "PHASE_5.1_POST_MERGE_DEPLOYMENT_CHECKLIST.md (Phase 4.4 stability declaration)"
  - "PHASE_5.2_MEDICAL_WATER_SEED_ROADMAP.md"
  - "PHASE_5.2_INTEGRATION_VALIDATION_MATRIX.md"
---

# Phase 5.2 Launch Coordination

**Purpose**: Single-document decision hub for the Phase 5.2 launch. Answers the question every June 1: is Phase 5.2 a go or a defer? Covers the June 1 decision point, resource allocation across Phase 5.1 post-merge validation and Phase 5.2 Medical implementation, rollback decision trees, and the success metrics that define "Phase 5.2 complete by July 1."

**Who reads this**: The user making the June 1 go/no-go call, and any agent executing work in the June 1–30 window.

---

## June 1 Decision Point

### Condition Check

Before any Phase 5.2 work begins, all five of the following must be true:

| Condition | How to verify | Expected result |
|---|---|---|
| C1: Phase 5.1 merge approved | `git log master --oneline | head -3` — merge commit present | Merge commit dated ≤ May 31 |
| C2: Phase 5.1 48-hour monitoring complete | Log file: `grep -c 'ERROR\|CRITICAL' /opt/open-repo/logs/app.log` | Zero errors in 48-hour window |
| C3: Post-merge action items done | Unit tests for XSS fix, ZimExport ORM pass; `libzim` in pyproject.toml | `uv run pytest tests/ -k "xss or zim_export or zim_model" -q` shows all pass |
| C4: Full test suite on master | `uv run pytest tests/ -q --tb=short` | 240 passed, 0 failures |
| C5: Production stable | `curl -s http://127.0.0.1:8080/health` returns 200 OK | Health check passes |

### Decision Tree

```
June 1 09:00 UTC — Check all 5 conditions above.

Are C1 through C5 ALL true?
│
├── YES → Phase 5.2 is a GO.
│         Proceed to "Execution Plan: Phase 5.2 GO" section below.
│         Medical implementation begins June 1.
│
└── NO → Which condition(s) failed?
          │
          ├── C1 fails (no merge) → Wait for merge. Check again June 2 09:00 UTC.
          │   Continue wait loop until merge confirmed.
          │   If merge not completed by June 5: activate Phase 5.2 DEFER path
          │   (see "Phase 5.2 Defer" section below).
          │
          ├── C2 fails (errors in 48-hour window) → Investigate errors.
          │   Determine if errors are in ZIM export path or Phase 1–4 code.
          │   If ZIM export errors: fix, restart 48-hour monitoring window.
          │   If non-ZIM errors: assess severity, consult user if critical.
          │   Retry June 1 decision check once monitoring window is clean.
          │
          ├── C3 fails (post-merge items incomplete) → Complete outstanding items.
          │   XSS fix: ~1 hour. ZimExport ORM: ~1.5 hours. pyproject.toml: 30 min.
          │   Can complete June 1 morning if items were started May 30–31.
          │   Retry check once all three items pass their tests.
          │
          ├── C4 fails (test regression) → STOP. Do not proceed to Phase 5.2.
          │   A test regression on master is a Phase 5.1 issue, not Phase 5.2.
          │   Investigate root cause. Fix and re-run full suite.
          │   Phase 5.2 deferred until master is clean.
          │
          └── C5 fails (health check down) → STOP. Infrastructure issue.
              Check uvicorn process, port binding, database connection.
              Fix and restore health check. Phase 5.2 deferred until stable.
```

---

## Execution Plan: Phase 5.2 GO

Activated when all five conditions pass the June 1 decision check.

### Resource Allocation: June 1–15

Phase 5.1 post-merge validation and Phase 5.2 Medical implementation overlap in the June 1–15 window. This is the highest-demand period of the June roadmap.

**Total estimated hours June 1–15**: 25–30 hours.

| Track | June 1–7 | June 8–15 | Hours |
|---|---|---|---|
| Phase 5.1 monitoring (passive) | Hourly checks on hours 1, 4, 24, 48 — see checklist Phase 4.2 | Final 48-hour declaration June 2–3 | 2 hours active |
| Phase 5.1 post-merge items (if not yet done) | XSS fix + ZimExport ORM + pyproject.toml | — | 3 hours |
| Phase 5.2 Medical — data sourcing | WHO EML CSV, ICRC PDF, RxNorm download, off-grid-living extraction | — | 2 hours |
| Phase 5.2 Medical — importer code | MedicalReferenceArchiver (~250 lines), article schema | Integration testing and content review begins | 5 hours |
| Phase 5.2 Medical — templates | 3 Jinja2 templates, disclaimer system | Final template QA | 3 hours |
| Phase 5.2 Medical — testing | 25 unit tests, Gate 1–3 validation matrix | Gate 4 performance, zimcheck | 6 hours |
| Phase 5.2 Medical — accuracy review | (scheduled, not yet running) | Full accuracy review: cross-check all dosing values | 4 hours |
| Buffer | Rollback investigation, unexpected issues | PR write-up and CHECKIN.md entry | 5 hours |
| **Total** | | | **30 hours** |

**Single-developer constraint**: All June 1–15 work is serialized. No parallelization across tracks on the same calendar day. The ordering within each day:

1. Check Phase 5.1 monitoring logs first (5 minutes daily).
2. Complete any remaining Phase 5.1 post-merge items (if not done May 30–31).
3. Phase 5.2 Medical implementation work for the day.

The Phase 5.1 monitoring (passive) does not conflict with Phase 5.2 implementation work — monitoring is read-only log checking. The Phase 5.1 post-merge items (C3) should be complete before June 1 if work is started May 30.

### Resource Allocation: June 15–30

Phase 5.1 is declared production-stable by June 3 (if 48-hour window starts June 1). Phase 5.2 Medical PR is under review by June 15. Water module implementation begins June 10 (staggered after Medical outline complete June 5).

| Track | June 15–22 | June 23–30 | Hours |
|---|---|---|---|
| Phase 5.2 Medical — accuracy review | Manual review of all dosing values (4 hours) | Final fixes from review | 5 hours |
| Phase 5.2 Medical — PR merge | Write CHECKIN.md, respond to review feedback | Merge on June 16 (estimated) | 2 hours |
| Phase 5.2 Water — implementation | WaterSystemsArchiver + WaterSizingCalculator + SVG test | Templates, tests, integration test | 20 hours |
| Phase 5.2 Seed — branch creation | Data download: GRIN CSV, USDA PLANTS CSV (start early — large files) | GRIN parser implementation begins | 5 hours |
| Buffer | Unexpected issues, thermal throttle investigation | Final QA | 5 hours |
| **Total** | | | **37 hours** |

**Total June resource estimate**: 30 hours (June 1–15) + 37 hours (June 15–30) = 67 hours across the full month. This assumes a single developer averaging ~2.5 hours per day of focused implementation work. At 3 hours per day, all three modules can complete by July 1.

### Two-Developer Acceleration (Optional)

If a second developer is available, the following parallel pairs are safe to run simultaneously:

**Pair A (June 1–15)**: Developer 1 on Medical implementation; Developer 2 on Water data sourcing and SVG schematic conversion (Gate 2 validation). The SVG test can be done independently in parallel with Medical implementation — it does not depend on Medical being complete.

**Pair B (June 8–25)**: Developer 1 on Medical accuracy review and PR process; Developer 2 on Water implementation (WaterSystemsArchiver + WaterSizingCalculator). Water implementation can start June 8 with a second developer — the Medical June 5 outline milestone gates design patterns, not code dependencies. A second developer can adopt Medical's patterns from review.

**With two developers**: All three modules complete by June 25, with buffer for July 1 deployment.

---

## Execution Plan: Phase 5.2 Defer

Activated if any June 1 condition fails and cannot be resolved by June 5, OR if the user decides to defer Phase 5.2 explicitly.

### Defer Trigger Conditions

| Trigger | Reason | Action |
|---|---|---|
| Phase 5.1 merge not completed by June 5 | Merge window missed; post-merge validation needs 3–5 days | Defer Phase 5.2 to June 20 start |
| Phase 5.1 monitoring shows unresolved errors by June 3 | Production instability; Phase 5.2 would compound issues | Hold Phase 5.2 until Phase 5.1 is fully stable |
| User explicitly defers | Capacity constraint or priority shift | Defer to June 20 or June 30 depending on directive |
| C4 test regression found on June 1 | Master is unstable; Phase 5.2 on a broken base is invalid | Defer until master is clean |

### Defer Path: June 20 Start

If Phase 5.2 is deferred to June 20:

- June 1–19: Complete Phase 5.1 stabilization, post-merge items, and production monitoring.
- June 20: Run the June 1 condition check again. All five conditions must pass before any Phase 5.2 branch is created.
- June 20–30: Medical data sourcing and importer implementation (10 days instead of 15 — compressed).
- July 1–15: Medical accuracy review and PR. Water implementation starts July 8.
- July 15–30: Water implementation and ZIM integration test.
- August 1–15: Seed implementation.

**Defer impact**: All three modules complete by mid-August instead of July 1. The delay is linear — each week Phase 5.2 is deferred, the completion date shifts one week.

### Defer Path: June 30 Start (Maximum Defer)

If Phase 5.1 has unresolved issues that cannot be resolved before June 30:

- July 1 is the new Phase 5.2 start date.
- Medical completes July 15. Water completes July 30. Seed completes August 15.
- This is the "worst realistic case" — not a failure state, just a schedule shift.

---

## Rollback Decision Tree

### Phase 5.2 Module-Level Rollback

Each Phase 5.2 module has an independent rollback path. Rollback one module does not affect others.

```
Phase 5.2 module fails integration test (Gate 1–4 failure)
│
├── Gate 1 failure (data format incompatibility)
│   Action: Activate Fallback Path 1 from integration matrix.
│   Timeline: 2–4 hours to implement fallback.
│   Branch: Keep feature branch open; push fallback fix; re-run Gate 1.
│   Rollback trigger: If Gate 1 still fails after fallback implementation →
│     Close feature branch. Module deferred to Phase 5.3.
│     Phase 5.2 proceeds with the two passing modules.
│
├── Gate 2 failure (media embedding)
│   Action: Activate Fallback Path 2 (PNG for SVG, text for danger-box CSS).
│   Timeline: 2–3 hours for fallback implementation.
│   Rollback trigger: If Gate 2 still fails after both fallback attempts →
│     Module is released as nopic-only variant (no embedded media).
│     This is a downgrade, not a full rollback — nopic variant has full text utility.
│
├── Gate 3 failure (interactive components)
│   Action: Activate Fallback Path 3 (simplify index articles, fix link format).
│   Timeline: 1–2 hours.
│   Rollback trigger: If internal links still produce 404 after path standardization →
│     Remove cross-module links. Each module is self-contained without cross-links.
│     This is a feature reduction, not a full rollback.
│
└── Gate 4 failure (performance)
    Action: Reduce article count ceiling, increase scheduling to off-peak hours.
    Timeline: 1 hour to implement scheduling + 30 min to re-test.
    Rollback trigger: If ZIM export takes over 10 minutes even at off-peak →
      Module exports are moved to scheduled batch jobs (cron 02:00 UTC daily).
      This is a production configuration change, not a rollback of the module.
```

### Phase 5.2 Full Rollback (All Modules)

Activated if Phase 5.1 is found to be fundamentally unstable after Phase 5.2 work has begun — for example, if a libzim bug produces corrupted ZIM files under concurrent load.

```
Phase 5.1 instability found while Phase 5.2 is in progress
│
├── Phase 5.2 feature branches: keep open, do not merge.
├── Stop all Phase 5.2 implementation work immediately.
├── Focus exclusively on Phase 5.1 stability diagnosis.
├── Once Phase 5.1 is re-stabilized (re-run Phase 4 monitoring window):
│   Resume Phase 5.2 work from where it was paused.
│   No Phase 5.2 work is lost — branches remain intact.
└── If Phase 5.1 instability requires a revert of the 5.1 merge:
    All Phase 5.2 branches are rebased onto the reverted master
    once Phase 5.1 is re-implemented correctly.
    Timeline: 1–2 days depending on the severity of the Phase 5.1 issue.
```

### Per-Module Publish Rollback

After a module's ZIM file is published to the OPDS catalog or CDN:

```
Published ZIM found to have content accuracy error
(e.g., wrong drug dosing, wrong water chemical quantity, wrong viability years)
│
├── Immediately remove the ZIM from the OPDS catalog:
│   Update OPDS feed to remove the affected ZIM entry.
│   Delete or mark the CDN-hosted ZIM file as unavailable.
│
├── Identify the scope of the error:
│   - Single article: patch and republish.
│   - Entire drug class or species category: full ZIM regeneration required.
│
├── Fix the source data error (in the importer or source Markdown file).
│
├── Re-run content accuracy review for the affected category.
│
├── Regenerate and re-publish the corrected ZIM.
│
└── Document the error and correction in WORKLOG.md.
    Note: date of incorrect publication, date of correction, nature of error.
```

---

## Success Metrics

### Phase 5.2 Complete — Definition

Phase 5.2 is declared complete when all of the following are true:

**Medical module**:
- [ ] `feature/phase-5.2-medical` merged to master.
- [ ] `open-repo_en_medicine_YYYY-MM.zim` published to OPDS catalog and CDN.
- [ ] ZIM verified readable in Kiwix Android.
- [ ] Medical accuracy review complete: all dosing values verified against source citations.
- [ ] `zimcheck open-repo_en_medicine_YYYY-MM.zim` exits 0.
- [ ] All 240 Phase 5.1 tests still pass after Medical module merge.

**Water module**:
- [ ] `feature/phase-5.2-water` merged to master.
- [ ] `open-repo_en_water_YYYY-MM.zim` published to OPDS catalog and CDN.
- [ ] At least 3 embedded schematics (SVG or PNG) render correctly in Kiwix Android.
- [ ] Water chemical quantity values verified against WHO/CDC source citations.
- [ ] `zimcheck open-repo_en_water_YYYY-MM.zim` exits 0.
- [ ] All 240 Phase 5.1 tests still pass after Water module merge.

**Seed module**:
- [ ] `feature/phase-5.2-seed` merged to master.
- [ ] `open-repo_en_seeds_YYYY-MM.zim` published to OPDS catalog and CDN.
- [ ] Species cards for at least 200 species, verified readable in Kiwix.
- [ ] Viability data spot-check: 20 randomly selected species verified against GRIN source.
- [ ] `zimcheck open-repo_en_seeds_YYYY-MM.zim` exits 0.
- [ ] All 240 Phase 5.1 tests still pass after Seed module merge.

**Deployment readiness (July 1)**:
- [ ] All three ZIM files are live in the OPDS catalog.
- [ ] kiwix-serve on the Pi 5 serves all three ZIM files simultaneously.
- [ ] Health endpoint `GET /health` returns 200 OK.
- [ ] Zero ERROR or CRITICAL entries in logs during the 48-hour window following the last module publish.
- [ ] Total new ZIM file storage on Pi 5: under 75 MB (nopic variant for all three modules combined).
- [ ] Full test suite on master: minimum 280 passed (240 Phase 5.1 + 65 Phase 5.2 = 305 target; 280 is the minimum acceptable if some Phase 5.2 integration tests are conditional).

### Milestone Tracking

| Date | Milestone | Owner | Status |
|---|---|---|---|
| June 1 | Phase 5.2 GO decision | User + agent | Pending June 1 check |
| June 1 | Medical branch created, data sourcing begins | Agent | Pending |
| June 5 | Medical outline complete (20+ conditions, 30+ drugs) | Agent | Pending |
| June 10 | Water branch created, SVG Gate 2 test | Agent | Pending |
| June 12 | Medical first draft complete; accuracy review scheduled | Agent | Pending |
| June 15 | Medical PR ready for user merge review | Agent | Pending |
| June 15 | Seed branch created, GRIN download begins | Agent | Pending |
| June 16 | Medical accuracy review complete | Author | Pending |
| June 20 | Medical merged; Medical ZIM published | User merge | Pending |
| June 25 | Water implementation complete; Gate 4 passes | Agent | Pending |
| June 28 | Water PR ready for user merge review | Agent | Pending |
| June 30 | Water accuracy review complete | Author | Pending |
| June 30 | Seed implementation to ZIM integration test | Agent | Pending |
| July 1 | Water merged; Water ZIM published | User merge | Pending |
| July 5 | Seed PR ready for user merge review | Agent | Pending |
| July 8 | Seed accuracy review complete | Author | Pending |
| July 10 | Seed merged; Seed ZIM published | User merge | Pending |
| July 10 | Phase 5.2 declared complete | User | Pending |

---

## Communication Protocol

### User Review Points

Phase 5.2 requires three user merge approvals (one per module). For each:

1. Agent writes a `CHECKIN.md` entry when the feature branch is ready, noting: branch name, test count, zimcheck result, content accuracy review status, and a 3-sentence summary of what the module adds.
2. User reviews the PR and either merges or requests changes.
3. After merge, agent publishes the ZIM to the OPDS catalog and CDN, then confirms publication in WORKLOG.md.

No module is published without user merge approval of the feature branch.

### Escalation Triggers

The following conditions require user input before work continues:

- Any Gate 1 failure where the fallback path requires sourcing a different dataset (e.g., manual JSON construction from WHO PDF extraction) — the user should confirm the source is acceptable before 3+ hours are spent.
- Medical accuracy review finds a dosing discrepancy: if the off-grid-living source document disagrees with the WHO EML on a specific dosing value, escalate to user for resolution. Do not publish with unresolved dosing discrepancies.
- ZIM file size exceeds expected range by more than 2x (e.g., Water ZIM is 40 MB instead of 10 MB): escalate before publishing to CDN, as the file size will affect OPDS catalog download times.
- Any rollback trigger (per-module or full rollback): notify user immediately before executing the rollback.

---

## Appendix: June 2026 Calendar Summary

```
May 29–31: Phase 5.1 post-merge validation running (assume merge May 26–29)
           Post-merge action items (XSS, ORM, pyproject.toml) complete

June 1:    Decision point — GO or DEFER
           [GO] Medical branch created; data sourcing begins
           [DEFER] Wait and re-check June 2 (or June 20 if extended)

June 1–5:  Medical data sourcing (2h), importer skeleton (2h), content schema (1h)
           June 5 milestone: Medical outline generates 20+ conditions, 30+ drugs

June 5–7:  Medical Jinja2 templates (2h), disclaimer system (1h)

June 8–11: Medical unit tests (4h), Gate 1 validation matrix run
           June 10: Water branch created; data sourcing starts

June 10–15: Water: WHO/CDC data download (2h); SVG Gate 2 test (3h)
             Medical: ZIM integration test (2h); accuracy review begins

June 12:   Medical first draft complete. Accuracy review scheduled.
           Water: WaterSizingCalculator implementation (3h)

June 13–15: Medical: Gate 3 validation (1h); Gate 4 performance (2h)
             June 15 milestone: Medical PR ready for user review
             June 15: Seed branch created; GRIN/USDA CSV downloads begin

June 16–17: Medical accuracy review (4h)

June 18–22: Water: WaterSystemsArchiver importer (4h); templates (2h)
             Seed: GRIN parser (3h); viability calculator (2h)

June 23–27: Water: unit tests (3h); Gate 3 validation (2h); Gate 4 (2h)
             Seed: SeedPreservationArchiver (4h); templates (2h)

June 28–30: Water PR ready for user review
             Seed: ZIM integration test (2h); Gate 4 performance (2h)
             June 30: Seed PR ready for user review (stretch goal)

July 1:     Phase 5.2 deployment readiness check
            Target: Medical and Water ZIMs live; Seed in final review
```

---

## Sources

- Phase 5.1 Post-Merge Deployment Checklist — `/projects/open-repo/PHASE_5.1_POST_MERGE_DEPLOYMENT_CHECKLIST.md`
- Phase 5.2 Medical Water Seed Roadmap — `/projects/open-repo/PHASE_5.2_MEDICAL_WATER_SEED_ROADMAP.md`
- Phase 5.2 Integration Validation Matrix — `/projects/open-repo/PHASE_5.2_INTEGRATION_VALIDATION_MATRIX.md`
- Phase 5.2 Feature Candidates — `/projects/open-repo/PHASE_5.2_FEATURE_CANDIDATES.md`
- Phase 5.2 Priority Matrix — `/projects/open-repo/PHASE_5.2_PRIORITY_MATRIX.md`
- [libzim Python bindings — PyPI](https://pypi.org/project/libzim/)
- [openZIM project — openzim.org](https://wiki.openzim.org/)
- [zimcheck — openzim/zim-tools](https://github.com/openzim/zim-tools)
