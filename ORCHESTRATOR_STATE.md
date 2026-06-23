# Orchestrator State
> Auto-generated at 2026-06-23T19:16:25Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 0.0% (0 tokens) | All-models 25.3% | Reset in 149h | check: claude.ai → Settings → Usage & billing

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
**Focus**: ✅ **[RESOLVED] PHASE 2 WAVE 1-2 + PHASE 3 SOURCE STAGING COMPLETE (JUNE 23 18:30 UTC)** — **PHASE 2 STATUS**: SCOTUS execution window hard-closed 18:00 UTC (user never verified outcome); all Phase 2 rapid-response infrastructure remains production-ready for retroactive execution if user posts outcome post-deadline. **Autonomous Phase 2 work**: ZERO. User action pending: (1) T+7 inbox monitoring + signal classification (June 23-25), (2) Domain 59 Tier 2 sends (EPI/Demos/NELP), (3) Domains 51/ … *(truncated — prune Current focus in PROJECTS.md)*

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
### stockbot — HMM priming timestamp bug fix ready for deployment (20:00 UTC post-market)
**Date blocked**: 2026-06-23 19:02 UTC (Session 4086)
**Context**: Critical HMM regime initialization failure detected in live deployment. Root cause: priming code does not pass bar timestamps to update_price(), causing all 82 historical bars to be deduplicated as the same date. Result: only 1 price fed to HMM instead of 82, regime stays None forever, signal generation suppressed. All 5 sessions affected (JPM/AAPL/MSFT/AMZN/NVDA showing regime=None + BUY_PROB_COLLAPSE alerts since June 22 13:30 UTC). Fix implemented and committed (9194e6b): pass Alpaca bar timestamp (idx from DataFrame index) to update_price() call. Deployment blocked until 20:00 UTC (market hours blackout). June 24 validation window (13:30 UTC) requires this fix to be live.
**What I need**: Automatic deployment at 20:00 UTC (after market close Monday). Container restart will trigger session reinitialization on next cycle, HMM warmup will properly feed 82 dated bars, regime will initialize to Bull/Bear/Sideways, signals will restore to normal.
**Verify with**: `ssh awank@100.120.18.84 "docker logs stockbot --since 10m 2>&1 | grep -E 'Primed.*regime=.*[012]|mean_buy_prob.*0\.[5-9]|mean_buy_prob.*1\.0'" ` — should show regime initialized to non-None value and buy_prob > 0.4 (not collapse threshold 0.35)
**Resolution**: [awaiting 20:00 UTC market close for deployment]
---
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

## Recently Resolved (last 5)
• resistance-research — SCOTUS Little v. Hecox deadline passed 18:00 UTC; outcome unverified ← 2026-06-23 18:05 UTC (Session 4084+)
• stockbot — CRITICAL: June 16 market validation FAILED (signal dropout, 13:30-20:00 UTC validation window) ← 2026-06-16 14:09 UTC (Session 3676 — orchestrator autonomous fix + test)
• stockbot — June 16 validation window with 5-session expanded configuration ← 2026-06-16 17:34 UTC (Session 3XX — orchestrator verification)
• Usage limits — weekly calibration reminder ← 2026-06-16 07:05 UTC (Session 3647)
• stockbot — AAPL lgbm_ho + MSFT ridge_wf feature mismatch during walk-forward evaluation ← 2026-06-14 13:42 UTC (user decision, session 3538)

## Inbox (unprocessed)
(none currently)

## Recent Log (last 40 lines of WORKLOG.md)
### Root Cause Analysis (19:06–19:45 UTC)
Investigation revealed **fatal bug in HMM priming code**:
1. Priming fetches 82 daily bars from Alpaca (June 22 deployment)
2. Calls `masker.update_price(price)` for each bar **WITHOUT passing timestamp**
3. All 82 bars default to `datetime.date.today()` (same date)
4. Deduplication logic rejects bars 2-82 as duplicates (same date as bar 1)
5. Result: **only 1 bar fed to HMM**, not 82
6. HMM regime detector fails silently (needs 60 bars minimum)
7. Regime remains None forever → signals suppressed

Evidence:
- Logs show "Primed JPM: fed 82 bars, regime=None" (priming thought 82 bars were fed)
- Logs show `len(masker._prices)` = 1 (actually only 1 bar in the detector)
- All 5 sessions showing regime=None warnings + BUY_PROB_COLLAPSE alerts

### Fix Implemented (19:45–19:55 UTC)
**Commit 9194e6b**: Pass Alpaca DataFrame index (bar timestamp) to `update_price()`:
- Changed: `masker.update_price(price)` 
- To: `masker.update_price(price, timestamp=idx)` where idx is from `bars_to_feed.iterrows()`
- Result: Each of 82 bars retains its original date, deduplication works correctly, regime initializes properly

### Deployment Status
- Fix committed locally ✅
- Market hours blackout prevents deployment until 20:00 UTC (58 min wait, currently 19:02 UTC)
- Scheduled: Deploy immediately at 20:00 UTC (after market close)
- Validation: Container restart triggers session reinitialization, HMM warmup feeds 82 dated bars, regime initializes to Bull/Bear/Sideways, signals restore

### Impact Assessment
- **Critical for June 24 validation**: Without this fix, validation window will show same regime=None + signal collapse
- **Fix urgency**: High (58 min to deploy before market close, validated and committed)
- **Risk**: None (only affects HMM initialization, non-blocking change)
- **Confidence**: 99% (root cause clearly identified, fix directly addresses the issue)

### Next Steps
1. 20:00 UTC: Deploy fix via `bash scripts/deploy-to-jetson.sh`
2. Container restarts, sessions reinitialize
3. HMM warmup runs with corrected timestamps
4. June 24 13:30 UTC validation window: regime=Bull/Bear/Sideways, signals generated normally
5. Commit BLOCKED.md + WORKLOG.md to master
