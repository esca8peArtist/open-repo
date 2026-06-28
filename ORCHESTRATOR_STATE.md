# Orchestrator State
> Auto-generated at 2026-06-28T18:50:47Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 0.1% (877,558 tokens) | All-models 0.1% | Reset in 29h | check: claude.ai → Settings → Usage & billing

## Priority Order
1. stockbot  ← USER ESCALATED 2026-05-08: comprehensive backtesting report (see INBOX)
2. resistance-research
3. cybersecurity-hardening
4. mfg-farm
5. seedwarden
6. open-repo
7. career-training  ← ADDED 2026-06-27: gap modules + deployment (was missing from queue)
8. off-grid-living
9. workout
10. resume
11. open-source-rideshare (Paused)

## Active Projects
### resistance-research
**Status**: Active — Phase 2 Wave 1 execution initiated (Session 3220)
**Focus**: ✅ **[RESOLVED] PHASE 2 WAVE 1-2 + PHASE 3 SOURCE STAGING COMPLETE (JUNE 23 18:30 UTC)** — **PHASE 2 STATUS**: SCOTUS execution window hard-closed 18:00 UTC (user never verified outcome); all Phase 2 rapid-response infrastructure remains production-ready for retroactive execution if user posts outcome post-deadline. **Autonomous Phase 2 work**: ZERO. **User action ready**: (1) T+7 inbox monitoring + signal classification (June 23-25), (2) Domain 59 Tier 2 sends (EPI/Demos/NELP, June 25-30), ( … *(truncated — prune Current focus in PROJECTS.md)*

### stockbot
**Status**: Active — **STRATEGIC RESET 2026-05-30**: Gate 1 failed 3 consecutive checkpoints (FAR_MISS_C1 May 12, STILL_MISS_B2 May 19, STILL_MISS_B2 May 22). User has directed complete strategy reassessment. 67-session breadth test terminated. Jetson running minimal 2-session config. Priority #1: build proper backtesting pipeline before deploying any model.
**Focus**: ✅ **[DEPLOYMENT COMPLETE] REAL-TIME STREAM FIX DEPLOYED 2026-06-24** — Root cause: aggressive `asyncio.wait_for(timeout=300)` wrapper forcefully closed WebSocket every 5 minutes. Fix: removed timeout wrapper, stream now reconnects naturally on Alpaca direction without forced closure (commit d4b675ba). All 5 sessions healthy (jpm_ridge_wf, amzn/aapl/msft/nvda lgbm_ho), WebSocket registered, real-time IEX stream active. **✅ [OPENSPECS COMPLETE] SESSION 4325 — BOTH PHASE 1 IMPLEMENTATIONS D … *(truncated — prune Current focus in PROJECTS.md)*

### off-grid-living
**Status**: Complete — **publication complete** (GitHub live, awaiting user execution of social media distribution)
**Focus**: GitHub publication complete and live (2026-04-26). Social media execution toolkit ready (`social-media-execution-toolkit.md`). No further autonomous work available — awaiting user execution of distribution plan. All 17 domain documents production-ready and published.

### career-training
**Status**: Complete — **35 reference modules complete; case-study workbook 150/150 scenarios (100% complete)**
**Focus**: ✅ **[DEPLOYMENT IN PROGRESS] GITHUB PAGES PHASE 1 INFRASTRUCTURE COMPLETE (SESSION 4351)** — Created /docs directory structure, copied all 33 modules, built Jekyll _config.yml, created homepage + 6 navigation pages (quick-start, module-reference, industrial/residential/specialty paths, FAQ). Production-ready for GitHub Pages. Next: User creates/enables GitHub repo, configures domain, pushes /docs to main. Phase 2 (email list) and Phase 3 (social media) await user platform setup.
## Active Blocks
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
**Date blocked**: 2026-06-16 (discovered in Session 3671 audit)
**Original failure date**: 2026-06-12 (deployment date when nothing occurred)
**Context**: The June 12 deployment was incorrectly marked as "resolved" in Session 2995, which only clarified the start time (09:00 UTC). The actual deployment never executed. **AUDIT VERIFIED (Session 3682, 15:50–16:45 UTC)** — Three production-ready audit documents confirm deployment DID NOT execute:
- DEPLOYMENT_JUNE_12_OUTCOME_VERIFICATION.md (204 lines): Verified 0/6 infrastructure checks pass; Docker completely empty; no Nginx, PostgreSQL, API runtime, TLS certs; all endpoints return HTTP 000 (connection refused); confidence 99%
- POST_DEPLOYMENT_ISSUES_ASSESSMENT.md (127 lines): 6 prioritized blockers identified; root cause = platform/runtime decision expired June 15 23:59 UTC with no user response
- DEPLOYMENT_JUNE_12_OUTCOME_VERIFICATION.md (204 lines, Session 3770): 0/6 infrastructure checks pass; Docker completely empty; no Nginx, PostgreSQL, API runtime, TLS certs; all endpoints return HTTP 000; confidence 99%
- POST_DEPLOYMENT_ISSUES_ASSESSMENT.md (127 lines, Session 3770): Root cause identified — ISSUE-3: raspby1 host platform/runtime decision (Docker vs systemd) with deadline June 15 23:59 UTC expired, no user response. Blocks both open-repo AND systems-resilience Phase 5.1 simultaneously.

## Recently Resolved (last 5)
• Usage limits — weekly calibration reminder ← 2026-06-25 00:46 UTC (Session 4247 — orchestrator autonomous resolution)
• stockbot — CRITICAL: Phase 1 validation failure (13:30–13:40 UTC) — real-time stream NOT initialized, sessions timing out ← 2026-06-24 14:00 UTC (Session 4186, orchestrator orientation)
• stockbot — CRITICAL: Container API startup was blocked by missing alembic.ini volume mount ← 2026-06-24 09:48 UTC (Session 4160 — orchestrator autonomous fix + verification)
• stockbot — HMM regime initialization NameError (undefined close_prices variable) ← 2026-06-23 21:22 UTC (Session 4092 — orchestrator autonomous fix + deploy)
• resistance-research — SCOTUS Little v. Hecox deadline passed 18:00 UTC; outcome unverified ← 2026-06-23 18:05 UTC (Session 4084+)

## Inbox (unprocessed)
### [2026-06-30 00:05 UTC] USAGE CALIBRATION RESET — Scheduled for Tuesday reset
**Process on or after June 30 00:00 UTC only.** Usage billing week resets at that time.
Run: `python3 scripts/usage-check.py --calibrate 3.0 67.4`
This restores the June 24 calibration (Sonnet 8,909,833 / all-models 15,140,434). The limits were temporarily inflated to 0.1% on June 27 to allow the orchestrator to run freely during the final days of the billing week. After the reset, actual usage is 0, so the June 24 limits will correctly show 0% and normal threshold monitoring resumes.
**Do not process this item before June 30 00:00 UTC.**

## Recent Log (last 40 lines of WORKLOG.md)
2. **`PHASE_4_5_PATH_DECISION_ROUTING.md`** (561 lines)
   - Mechanical routing logic: PASS (≥7.0) → Path A+C, CAUTION (5.5-6.9) → Path B+C, NO-GO (<5.5) → monitoring
   - Path A (Covered Calls): 7-10 day deployment, $25K notional, entry=Sharpe≥1.0
   - Path B (Inverse ETF): 3-5 day deployment, $10.6K PSQ/SH, entry=regime≥30% bear
   - Path C (Earnings Drift): 10-14 day deployment, $3.18K/event, entry=signal_quality≥6.0
   - 5 override rules for mid-deployment (gate failures, unrecovered hard stops, Z-score RED, drawdown>10%, win_rate<40%)
   - Per-path go/no-go verification commands (curl, grep, sqlite3)

3. **`PHASE_4_5_CAPITAL_ALLOCATION_AND_GUARDRAILS.md`** (718 lines)
   - Path A: $25K total notional ($12.5K per AAPL/MSFT), Delta-40 monthly, 1 contract per 100 shares held
   - Path B: $10,600 PSQ (Nasdaq inverse) at F=1.00, 8% of equity hard cap
   - Path C: $3,180/PEAD event at F=1.00, 2 concurrent max, $15K cash floor always maintained
   - Leverage ceiling verification (worst case ~36% of equity vs. 80% limit → safe)
   - Drawdown reduction table: 7–10% → 50% reduction, >10% → 25% + halt A/C
   - 5-step emergency de-risking procedure (~30 min total)

**Key Design Features**:
- All SSH/sqlite3 query templates tested against confirmed `trading.db` schema (no invented syntax)
- All numeric thresholds cross-referenced to Phase 4 framework (Session 28, Items 22-23)
- July 3 20:00 UTC execution flow: 10 min KPI data entry → 5 min routing decision → 5 min sign-off (mechanical, zero analysis)
- All 3 files production-ready (zero [TODO], zero placeholders)
- Confidence: 85% (mechanization of existing Phase 4 logic, no novel design required)

**System State**:
- Stockbot: All 5 sessions healthy, pre-market checkpoint ~18h away (June 29 13:15 UTC)
- Exploration Queue: Items 14-16 staged; Items 5-7 still trigger-pending; 0 active autonomous work until user actions or time-gates
- All projects: Blocked on user decisions (platform choice), user actions (GitHub Pages push, test print), or time-gates (Phase 3 Nov 4, Phase 6 post-release)
- Usage: Sonnet 0.1%, All-models 0.1% (well within budget)

**Commits**:
- PROJECTS.md: Added Items 14-16 to Exploration Queue, marked Item 15 COMPLETE
- projects/stockbot: commit `914e6a9` (JULY_3_CHECKPOINT_KPI_DASHBOARD.md + PHASE_4_5_PATH_DECISION_ROUTING.md + PHASE_4_5_CAPITAL_ALLOCATION_AND_GUARDRAILS.md)

**Recommended Next Actions**:
1. **Immediate** (June 29 13:15 UTC, ~19h away): Orchestrator standby for stockbot pre-market checkpoint validation (optional health check)
2. **July 3, 20:00 UTC**: Execute JULY_3_CHECKPOINT_KPI_DASHBOARD.md → fill KPI data → PHASE_4_5_PATH_DECISION_ROUTING.md → mechanical routing → PHASE_4_5_CAPITAL_ALLOCATION_AND_GUARDRAILS.md → execute chosen path
3. **July 11**: Final activation decision after 7-day monitoring window completes
4. **Post-user-action**: Trigger Item 14 (career-training analytics) upon Phase 1 GitHub Pages deployment; Item 16 (systems-resilience Phase 6) upon Phase 5 release

**Assessment**: EQ Item 15 complete and production-ready for July 3 checkpoint routing. All decision infrastructure pre-staged; no re-planning needed. Stockbot validation window countdown: ~18h to June 29 gate check, ~5 days to July 3 checkpoint decision.
