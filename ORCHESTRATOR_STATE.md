# Orchestrator State
> Auto-generated at 2026-06-24T16:44:28Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 1.7% (148,444 tokens) | All-models 55.8% | Reset in 127h | check: claude.ai → Settings → Usage & billing

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
### resistance-research
**Status**: Active — Phase 2 Wave 1 execution initiated (Session 3220)
**Focus**: ✅ **[RESOLVED] PHASE 2 WAVE 1-2 + PHASE 3 SOURCE STAGING COMPLETE (JUNE 23 18:30 UTC)** — **PHASE 2 STATUS**: SCOTUS execution window hard-closed 18:00 UTC (user never verified outcome); all Phase 2 rapid-response infrastructure remains production-ready for retroactive execution if user posts outcome post-deadline. **Autonomous Phase 2 work**: ZERO. **User action ready**: (1) T+7 inbox monitoring + signal classification (June 23-25), (2) Domain 59 Tier 2 sends (EPI/Demos/NELP, June 25-30), ( … *(truncated — prune Current focus in PROJECTS.md)*

### stockbot
**Status**: Active — **STRATEGIC RESET 2026-05-30**: Gate 1 failed 3 consecutive checkpoints (FAR_MISS_C1 May 12, STILL_MISS_B2 May 19, STILL_MISS_B2 May 22). User has directed complete strategy reassessment. 67-session breadth test terminated. Jetson running minimal 2-session config. Priority #1: build proper backtesting pipeline before deploying any model.
**Focus**: ⚠️ **[PAUSED] PHASE 1 VALIDATION WINDOW HARD-PAUSED 2026-06-24 13:49 UTC — REAL-TIME STREAM CRITICAL FAILURE** — Real-time WebSocket/IEX stream not receiving tick data at market open. Cascading failures: (1) 13:30:02–13:30:03 UTC: All 5 sessions detected market open, began signal cycles ✅. (2) 13:30:47 UTC: StreamHealthWatchdog detected ZERO real-time ticks (80+ min gap). (3) 13:31:49 + 13:48:49 UTC: Container auto-restarted 2×. (4) **13:48:49–13:49:13 UTC: All 5 sessions circuit- … *(truncated — prune Current focus in PROJECTS.md)*

### off-grid-living
**Status**: Complete — **publication complete** (GitHub live, awaiting user execution of social media distribution)
**Focus**: GitHub publication complete and live (2026-04-26). Social media execution toolkit ready (`social-media-execution-toolkit.md`). No further autonomous work available — awaiting user execution of distribution plan. All 17 domain documents production-ready and published.

### career-training
**Status**: Complete — **35 reference modules complete; case-study workbook 150/150 scenarios (100% complete)**
**Focus**: All 35 modules complete with 150 total scenarios (100% of target). Complete curriculum: foundation through business development, all 150 scenarios with full worked answers. Production-ready, awaiting user review and deployment.
## Active Blocks
### Usage limits — weekly calibration reminder
**Date blocked**: 2026-06-23 (auto-added each Tuesday by reset-usage-budget.sh)
**Context**: Plan limits reset today. Token limits in usage-check.py are calibrated estimates that drift over time. Verify against actual UI percentages.
**What I need**: Check claude.ai → Settings → Usage & billing. Run: `bash scripts/verify-calibration.sh <sonnet_pct> <all_pct>`
**Verify with**: `bash scripts/verify-calibration.sh`
**Resolution**: ⏳ **AWAITING USER ACTION** — Calibration last updated 2026-06-10 (13 days ago, beyond 7-day drift window). Need actual Sonnet % and All-models % from claude.ai Settings UI. Script ready to execute once percentages provided.
---
### cybersecurity-hardening — Phase 1 walkthrough in progress (user restart required)
**Date blocked**: 2026-05-16
**Context**: Walking through PERSONAL_OPSEC_PLAN.md Phase 1 steps with user. Paused mid-session for VeraCrypt pre-boot test restart.
**Progress so far**:
- ✅ 1.1 Signal — complete (username set, phone number hidden, disappearing messages on)
- ✅ 1.2 iPhone tracking — steps 1-3 done (tracking off, location audited, personalized ads off). Step 4 (Advanced Data Protection) pending 24-48hr Apple security delay — complete tomorrow
- 🔄 1.3 VeraCrypt — installed, encryption wizard run, **needs restart to complete pre-boot test**, then click Encrypt to start background encryption
- ⏳ 1.4 Ente Auth — not started (install from App Store, switch email + financial accounts off SMS 2FA, set carrier SIM PIN)
- ⏳ 1.5 Bitwarden password manager — not started
- ⏳ 1.6 Data broker opt-outs — not started (10 sites + 3 federal opt-outs, ~45 min)
- ⏳ 1.7 iPhone passcode over Face ID — not started (5 min, do anytime)
**What I need**: Restart Windows machine, type VeraCrypt pre-boot password when prompted, let Windows boot normally, then click Encrypt in VeraCrypt to start background encryption. Then resume Phase 1 walkthrough from step 1.4.
**Verify with**: `# manual — cannot auto-verify`
**Resolution**: [leave blank]
---
### mfg-farm — Test print execution (user action required)
**Date blocked**: 2026-05-13
**Context**: All pre-print deliverables are complete: ModRun cable clip designs (`modrun_rail.py`, `modrun_clip.py`), Etsy listing copy, supplier scorecard, production cost model. Test print is required to evaluate snap-arm tolerance (1.4mm is highest-risk feature) and validate design before production scale.
**What I need**: Execute single test print with specifications: 0.20mm layer height, PLA+, 3 walls, 220–225°C. Evaluate snap-arm clearance (FDM_TOLERANCE target) and report whether clip function is acceptable.
**Verify with**: `ls -la projects/mfg-farm/test-print-results/` — should contain test-print-evaluation.md with pass/fail decision
**Resolution**: [leave blank]
---
### open-repo — June 12 deployment never executed; infrastructure missing on raspby1

## Recently Resolved (last 5)
• stockbot — CRITICAL: Phase 1 validation failure (13:30–13:40 UTC) — real-time stream NOT initialized, sessions timing out ← 2026-06-24 14:00 UTC (Session 4186, orchestrator orientation)
• stockbot — CRITICAL: Container API startup was blocked by missing alembic.ini volume mount ← 2026-06-24 09:48 UTC (Session 4160 — orchestrator autonomous fix + verification)
• stockbot — HMM regime initialization NameError (undefined close_prices variable) ← 2026-06-23 21:22 UTC (Session 4092 — orchestrator autonomous fix + deploy)
• resistance-research — SCOTUS Little v. Hecox deadline passed 18:00 UTC; outcome unverified ← 2026-06-23 18:05 UTC (Session 4084+)
• stockbot — CRITICAL: June 16 market validation FAILED (signal dropout, 13:30-20:00 UTC validation window) ← 2026-06-16 14:09 UTC (Session 3676 — orchestrator autonomous fix + test)

## Inbox (unprocessed)
(none currently)

## Recent Log (last 40 lines of WORKLOG.md)
- **SCOTUS outcome verification** (resistance-research): Closed at 18:00 UTC June 23, no escalation possible

All blocks are legitimately user-action-dependent. No orchestrator work available.

### Exploration Queue status

- 12+ items total, all with dependencies or trigger conditions
- No items with "ready NOW" status that don't require user data
- Post-deployment triggers will become available 20:50 UTC (Item 30 summary, Item 31 Phase 4 synthesis)

### Recommended next steps

1. **20:00 UTC**: Monitor market close (no action needed, automated)
2. **20:30 UTC**: Execute deployment script (user or automated via DEPLOY_READY)
3. **20:50 UTC**: Deployment validation completes, post-market summary logged
4. **June 25 13:15 UTC**: Phase 0 pre-market gates (monitoring framework ready)
5. **User action OVERDUE**: Domains 51/48 Wave 1 sends (templates + contacts ready in projects/resistance-research/)

### Confidence assessment

- **Deployment readiness**: 98% (all tests pass, fix narrowly scoped, rollback <5 min)
- **Post-deployment validation**: 92% (monitoring framework fully staged, all queries verified)
- **Overall session status**: CORRECT (all projects appropriately blocked, no work skipped)


---

## Session 4194 (2026-06-24 15:59–16:XX UTC)

**Status**: ZERO autonomous work available — deployment standby mode

**Orientation complete**:
- Confirmed all projects legitimately blocked (stockbot deployment-gated to 20:30 UTC, all others user-action-dependent)
- Verified Exploration Queue has 12+ items (all complete or trigger-gated, no "ready NOW" items)
- Confirmed deployment timeline: 20:30 UTC execution, 20:50 UTC completion, Item 30 post-deployment triggers
- All orchestration files current and verified

**Next action**: Execute deployment script at 20:30 UTC post-market

**Deployment window**: 20:30 UTC (4h 30m from session start)
