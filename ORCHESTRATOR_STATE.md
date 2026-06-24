# Orchestrator State
> Auto-generated at 2026-06-24T11:44:21Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 1.7% (148,444 tokens) | All-models 48.1% | Reset in 132h | check: claude.ai → Settings → Usage & billing

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
**Focus**: ✅ **[DEPLOYMENT LIVE + MONITORING FRAMEWORK READY FOR JUNE 24 VALIDATION WINDOW (SESSION 3921)]** — **Status Summary (June 23 01:45 UTC)**: Deployment LIVE on Jetson since June 22 23:06:20 UTC. 5-session config running (JPM ridge_wf + AMZN lgbm_ho + AAPL lgbm_ho + MSFT lgbm_ho + NVDA lgbm_ho). Monitoring framework complete: VALIDATION_WINDOW_MONITORING_LOG.md (17KB, 5-session protocol), pre-market checklist (6 gates, all executable from Pi via SSH), dashboard specs (4 files, 60KB total). **J … *(truncated — prune Current focus in PROJECTS.md)*

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
• stockbot — CRITICAL: Container API startup was blocked by missing alembic.ini volume mount ← 2026-06-24 09:48 UTC (Session 4160 — orchestrator autonomous fix + verification)
• stockbot — HMM regime initialization NameError (undefined close_prices variable) ← 2026-06-23 21:22 UTC (Session 4092 — orchestrator autonomous fix + deploy)
• resistance-research — SCOTUS Little v. Hecox deadline passed 18:00 UTC; outcome unverified ← 2026-06-23 18:05 UTC (Session 4084+)
• stockbot — CRITICAL: June 16 market validation FAILED (signal dropout, 13:30-20:00 UTC validation window) ← 2026-06-16 14:09 UTC (Session 3676 — orchestrator autonomous fix + test)
• stockbot — June 16 validation window with 5-session expanded configuration ← 2026-06-16 17:34 UTC (Session 3XX — orchestrator verification)

## Inbox (unprocessed)
(none currently)

## Recent Log (last 40 lines of WORKLOG.md)

### Validation Window Phase 0 Execution Summary (10:05 UTC)

**Pre-market gates ready** (execute at exactly 13:15 UTC):
1. SSH Access & Docker Container Running — `docker ps | grep stockbot`
2. API Health Endpoint — `curl -s http://100.120.18.84:8000/api/health`
3. All 5 Sessions Initialized — `curl -s http://100.120.18.84:8000/api/sessions/status`
4. Market Clock Synchronized — `curl -s http://100.120.18.84:8000/api/market/clock`
5. Alpaca API Connectivity — Check logs for 401/403 errors
6. HMM Regime Initialization — Check logs for regime != None on all 5 sessions

**Success criteria**: All 6 gates PASS → GO decision for Phase 1-3 validation
**Failure criteria**: Any gate FAIL → NO-GO, escalate to user immediately

**Phase 1** (13:30 UTC): Signal emergence check (3 checks, ~10 min)
**Phase 2** (13:30–20:00 UTC): Continuous monitoring (Z-drift every 30 min, P&L every 60 min)
**Phase 3** (20:00 UTC): Post-market summary (4 final checks, ~30 min)

**Orchestrator Standing By**: Ready to execute Phase 0 at 13:15 UTC UTC. All commands copy-paste ready from JUNE24_VALIDATION_MONITORING_CHECKLIST.md.


## Session 4164 (2026-06-24 10:28 UTC) — ORCHESTRATOR — **VALIDATION WINDOW READINESS + PRE-MARKET WAKEUP SCHEDULING**

**Initiated**: 2026-06-24 10:28 UTC (standing-by continuation, 1h 44m to pre-market gates at 12:12 UTC)

**Status**: ✅ **JETSON VERIFIED HEALTHY — CONTINUING STANDBY FOR PRE-MARKET GATES AT 12:12 UTC** — Quick readiness re-check completed at 10:28 UTC after Session 4163 continued standing-by orientation. Jetson Docker container fully operational (up 44 minutes, healthy status). All 5 trading sessions initialized, last cycled 09:46 UTC, zero consecutive failures, API responding correctly with "trading_stalled" status (expected outside market hours). Code freeze maintained. Zero new INBOX items, Exploration Queue stable, all blocks user-action-dependent. Autonomous work: ZERO (correct by design for validation window standby).

**Work Completed**:
1. ✅ **Jetson Health Check** (10:28 UTC):
   - Docker container: ✅ HEALTHY (44 min uptime)
   - API health endpoint: ✅ RESPONDING (status: "trading_stalled", sessions: 5, no consecutive failures)
   - All 5 sessions verified: jpm_ridge_wf_001, amzn_lgbm_ho_001, aapl_lgbm_ho_001, msft_lgbm_ho_001, nvda_lgbm_ho_001
   - Last cycle timestamps: 09:46 UTC (all sessions synchronized)
   - SSH connectivity: ✅ OK
   - No new changes since Session 4163

**Orchestrator Posture**:
✅ **STANDING BY FOR PRE-MARKET GATES AT 12:12 UTC** — All infrastructure verified operational. Next scheduled action: Phase 0 pre-market health checks (6 SSH gates) at 12:12 UTC (1h 44m from now). Will execute gates 1-4 (Docker/API/sessions/clock), then continue Phase 1-3 monitoring through 20:00 UTC market close. Validation window timeline confirmed production-ready.

---
