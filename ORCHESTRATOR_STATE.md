# Orchestrator State
> Auto-generated at 2026-05-13T10:20:09Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 17.7% (1,581,577 tokens) | All-models 30.0% | Reset in 134h | check: claude.ai → Settings → Usage & billing

## Priority Order
1. stockbot  ← USER ESCALATED 2026-05-08: comprehensive backtesting report (see INBOX)
2. resistance-research
3. cybersecurity-hardening
4. mfg-farm
5. seedwarden
6. open-repo
7. off-grid-living
8. workout
9. resume
10. open-source-rideshare (Paused)

## Active Projects
### mfg-farm
**Status**: Active — ready to prototype
**Focus**: Test print execution pending (user action required). All pre-print deliverables complete — designs (`modrun_rail.py`, `modrun_clip.py`), listing copy, supplier scorecard, production cost model. **Blocking gate**: user to execute test print at 0.20mm layer height, PLA+, 3 walls, 220–225°C — evaluate snap-arm FDM_TOLERANCE (1.4mm is highest-risk feature). Post-print: Etsy listing + supplier negotiation (all materials ready in project dir).
**Blocked**: Test print (user action required — see focus above)

### resistance-research
**Status**: Active — Phase 1-5 COMPLETE, **36-Domain Diagnostic Framework + Phase 2 Expansion COMPLETE** (Sessions 502-524, Session 907) — Core proposal architecture complete, completeness assessment done, all 35+ domain documents verified production-ready, distribution infrastructure finalized (Session 520), April-May 2026 domain updates + tracker maintenance current (Sessions 521, 524, 876, 907)
**Focus**: Session 967: 41+ domains production-ready, Phase 1+2 COMPLETE, **all Phase 2 cross-references integrated** (Session 967). Three Phase 2 domains added (Domains 48-50, Sessions 964-967): Domain 48 (Surveillance Capitalism & Electoral Manipulation, June 12 FISA deadline), Domain 49 (Callais VRA Redistricting Emergency, five states in special sessions May 2026), Domain 50 (Healthcare-Democracy Nexus, June 1 HHS rule deadline). Cross-reference integration complete (Domains 1, 31, 33 updated with Call … *(truncated — prune Current focus in PROJECTS.md)*

### cybersecurity-hardening
**Status**: Active — **TIER 1, 2, 3 DISTRIBUTION PREP + TIER 2 MESSAGING TEMPLATES COMPLETE** (Sessions 465, 497, 499), ready for user execution
**Focus**: Phase 2 Scenario Playbooks complete (all 4 playbooks updated through May 2026 threat intel). Phase 1 Tier 1 infrastructure ready (25 contacts verified, 7-week timeline). User approval needed for Phase 1 Tier 1 launch + Day 1 send date. Tier 2 messaging templates + distribution prep complete and staged. All materials production-ready.
**Blocked**: User approval for Phase 1 launch + Day 1 send date

### stockbot
**Status**: Active — **2-session Jetson-only architecture (AAPL lgbm_ho + AAPL ridge_wf)**. Reduced from 67 sessions. 19 positions closing May 5 13:30 UTC open. AAPL (108 shares, +$924 unrealized) stays open.
**Focus**: **May 14 20:00 UTC checkpoint T-35h — Gate 2 readiness verified.** FAR_MISS_C1 confirmed (May 12 checkpoint). AAPL h+10 exit scheduled May 14 13:30 UTC. Expected outcome: NEAR-MISS B1. All pre-checkpoint items verified by code audit (no live Alpaca calls): checkpoint script functional (`scripts/may14_checkpoint_query_alpaca.py`, 383 lines), HMM regime scalar committed and tested (`src/ml/hmm_regime_scalar.py`, 46 tests passing), vol scalar integration complete (25 tests passing), Gate 2 guide  … *(truncated — prune Current focus in PROJECTS.md)*

### seedwarden
**Status**: Active — Track A BLOCKED (2 user actions, see `TRACK_A_BLOCKER_RESOLUTION.md`); **Track B CLEAR — May 30 launch target**; **Phase 3 assets COMPLETE (7 files verified, June 22 – July 13 execution)**
**Focus**: Phase 2 readiness audit complete — Track B is GO for May 30. Three user gates remain (social accounts, Canva Brand Kit, Kit email account — 30-60 min each, all materials staged). Track A has 2 open blockers: (1) 3 tag corrections on Companion Planting Chart, Survival Garden Regional Plans, Zone-by-Zone Calendar (15 min, copy-paste from `TRACK_A_BLOCKER_RESOLUTION.md`) and (2) Etsy account verification + Etsy Payments connection (10 min user action + 1-5 day Etsy processing). Decision deadlin … *(truncated — prune Current focus in PROJECTS.md)*
**Blocked**: Tag corrections + Etsy account verification (user action, Track A only). Track B has no blockers.

### open-repo
**Status**: Active — Phase 4 COMPLETE, **PR #1 open, awaiting review/merge** (Session 486: 2026-04-26)
**Focus**: **PR #1 OPEN** (2026-04-26): https://github.com/esca8peArtist/open-repo/pull/1

### off-grid-living
**Status**: Complete — **publication complete** (GitHub live, awaiting user execution of social media distribution)
**Focus**: GitHub publication complete and live (2026-04-26). Social media execution toolkit ready (`social-media-execution-toolkit.md`). No further autonomous work available — awaiting user execution of distribution plan. All 17 domain documents production-ready and published.

### workout
**Status**: Active
**Focus**: `comprehensive-plan.md` (1,053 lines) complete — covers all 3 equipment tiers (no equipment, bands, full gym) × multiple frequencies (3/4/5/6 days), with full exercise libraries, progression systems, calisthenics skill ladders, and mobility protocols. Awaiting user review and selection.

### mom-projects
**Status**: Active
**Focus**: —

### career-training
**Status**: Complete — **35 reference modules complete; case-study workbook 150/150 scenarios (100% complete)**
**Focus**: Session 977 (2026-05-13): **FINAL COMPLETION — 106 → 150 scenarios (100% of target)**
## Active Blocks
### mfg-farm — Test print execution (user action required)
**Date blocked**: 2026-05-13
**Context**: All pre-print deliverables are complete: ModRun cable clip designs (`modrun_rail.py`, `modrun_clip.py`), Etsy listing copy, supplier scorecard, production cost model. Test print is required to evaluate snap-arm tolerance (1.4mm is highest-risk feature) and validate design before production scale.
**What I need**: Execute single test print with specifications: 0.20mm layer height, PLA+, 3 walls, 220–225°C. Evaluate snap-arm clearance (FDM_TOLERANCE target) and report whether clip function is acceptable.
**Verify with**: `ls -la projects/mfg-farm/test-print-results/` — should contain test-print-evaluation.md with pass/fail decision
**Resolution**: [leave blank]
---

## State Drift Warnings
⚠️ STALE FOCUS: open-source-rideshare — focus references Session 407 (573 sessions ago); prune Current focus in PROJECTS.md
## Recently Resolved (last 5)
• mom-projects — Discord user ID not set; mom's messages not being routed ← 2026-05-13 (02:08 UTC)
• stockbot — DB sync script missing on Jetson; checkpoint query returns wrong results ← 2026-05-13 (Session 957, 00:28 UTC)
• stockbot — May 12 Checkpoint: Critical Architecture Mismatch (options vs equity trading) ← 2026-05-12 (Session 951, 22:05 UTC)
• stockbot — Jetson disk at 87% (29 GB free remaining) ← 2026-05-12 (Session 941, 19:45 UTC)
• Usage limits — weekly calibration reminder ← 2026-05-12 (Session 939, 19:02 UTC)

## Inbox (unprocessed)
*(no new items)*

## Recent Log (last 40 lines of WORKLOG.md)
### Dependencies Resolved

None — this was a research + documentation item with no code/schema dependencies.

### Next Steps for User / Orchestrator

**Immediate (May 13)**:
- [ ] Read `jetson-infrastructure-readiness-assessment.md` Part 4 (pre-checkpoint checklist)
- [ ] Execute May 13 baseline checks (thermal idle, memory idle, disk space, network)

**May 14 Morning**:
- [ ] Execute Part 4 final pre-checkpoint verification (10 items, ~15 min)

**May 14 Evening (after checkpoint)**:
- [ ] Execute Part 5 post-checkpoint validation (~20 min)
- [ ] Review hardware report
- [ ] If PASS: proceed to live trading prep
- [ ] If FAIL: diagnose + apply recovery actions

### Exploration Queue Status

**Exploration Queue Item COMPLETED**: `stockbot: Jetson Hardware Resilience & Live Trading Infrastructure Readiness Assessment` (Exploration Queue item, estimated 2-3 hrs, completed in ~1.5 hrs)

**Queue items VERIFIED COMPLETE (Sessions 956–978)**:
- ✅ Domain 42 outreach prioritization (May 28 DEA deadline work)
- ✅ seedwarden Phase 2 social growth strategy (May 13)
- ✅ career-training practice scenarios (150/150 complete)

**Queue items ACTIVE (no completion status found)**:
- stockbot: Multi-Ticker Position Sizing Framework (3-4 hrs)
- resistance-research: Phase 2 Expansion Domains 38-40 (4-5 hrs)
- cybersecurity-hardening: Phase 2 Distribution Sequencing (3-4 hrs)
- mfg-farm: Batch 2 Product Selection & Demand Research (2-3 hrs)
- [8+ others, see PROJECTS.md Exploration Queue section for full list]

**Recommendation for Session 980+**: If projects remain blocked on user decisions, prioritize:
1. **stockbot: Multi-Ticker Position Sizing & Risk Aggregation Framework** (3-4 hrs, high Gate 2 value)
2. **resistance-research: Phase 2 Expansion Domains 38-40 Research** (4-5 hrs, can execute in parallel with Phase 1 launch)
3. **cybersecurity-hardening: Phase 2 Distribution Sequencing** (3-4 hrs, high institutional impact)
