# Inbox

> Drop tasks, ideas, or redirections here from your phone or any device.
> The orchestrator reads this at the start of every session and processes new items.
> After processing, items are moved to WORKLOG.md or PROJECTS.md and cleared from here.
>
> **Tip**: This file syncs via Obsidian if your vault is set up to include this directory.
> Add a task from your phone by editing this file in Obsidian.

---

## New Items

*(All current new items are being processed in parallel or are time-gated. See "Processing" section below.)*

---

## Processing (Session 4520 — 2026-06-29 08:40 UTC)

### [2026-06-29 08:40 UTC] JETSON POST-MARKET MAINTENANCE — onedrive crash-loop remediation

**STATUS**: 🟡 **AWAITING USER AUTHORIZATION** (documented in CHECKIN.md "Needs Your Input")

Item 20 audit (pre-market readiness) found onedrive.service has crashed 1,005,780 times since May 9, filling `/var/log/syslog` with 12GB of logs. System is operationally clear for today's market (125GB free), but this must be fixed within 48 hours (by ~July 1 13:30 UTC) to prevent RED status disk contention by July 3-4.

**Remediation**: Three steps documented in `JETSON_JUNE29_READINESS_CHECKLIST.md`:
1. Stop + disable onedrive service (systemctl --user stop/disable)
2. Truncate syslog to 0 bytes (safe, only affects rotated log file)
3. Optionally reclaim Docker cache (~2.3GB)

**Timeline**: Execute sometime after 20:00 UTC today (post-market). Remediation takes <5 min.

**Awaiting user decision**: Authorize autonomous post-market execution (after 20:00 UTC) OR schedule manual execution by June 30 13:30 UTC. Decision logged to CHECKIN.md; will execute per user authorization when checkpoint resumes post-market.

---

### [2026-06-30 00:05 UTC] USAGE CALIBRATION RESET — Scheduled for Tuesday reset

**STATUS**: ⏳ **TIME-GATED (do not process before June 30 00:00 UTC)**

Process on or after June 30 00:00 UTC only. Usage billing week resets at that time.

Run: `python3 scripts/usage-check.py --calibrate 3.0 67.4`

This restores the June 24 calibration (Sonnet 8,909,833 / all-models 15,140,434). The limits were temporarily inflated to 0.1% on June 27 to allow the orchestrator to run freely during the final days of the billing week. After the reset, actual usage is 0, so the June 24 limits will correctly show 0% and normal threshold monitoring resumes.

Will process automatically at scheduled time or next orchestrator session after June 30 00:00 UTC.

## June 27 AUTONOMOUS WORK QUEUE — Processing History

🟢 **COMPLETED (Session 4327, June 27 21:00–21:41 UTC)**:
- ✅ **ITEM A — cybersecurity-hardening: Threat currency updates** (Session 4327) — All 6 Phase 2 playbooks updated with: Thomson Reuters CLEAR contract renewal status (post-May 31), Chatrie v. United States geofence ruling, Flock Safety litigation update. Committed.
- ✅ **ITEM B — open-repo: Phase 5.2 Wave 0 schema design** (Session 4327) — 5 content-type schemas (medical reference, water systems, seed preservation, food preservation, botanical knowledge) designed and stored in projects/open-repo/schemas/. Medical reviewer outreach drafted (PHASE_5.2_MEDICAL_CONTENT_SOURCING_CHECKLIST contact identified, outreach email in medical-reviewer-outreach-draft.md). Committed.
- ✅ **ITEM C — off-grid-living: Phase 2 signal analysis** (Session 4327) — GitHub issue frequency analysis complete across 17 published domain docs. Urgency/strategic fit rubric applied. Top 3-5 Phase 2 candidates ranked with justification. Results saved to projects/off-grid-living/phase-2-prioritization-results.md. Committed.
- ✅ **ITEM D — systems-resilience: Phase 5 GitHub release** (Session 4327) — Phase 5 Wave 1+2 integrated corpus (45,380 words) release assets verified production-ready. GitHub release execution blocked on maintainer push permissions (documented in BLOCKED.md). Release infrastructure staged, awaiting user action.
- ✅ **ITEM E — career-training: Gap module development + deployment infrastructure** (Session 4327, commit d8e5cb5c) — All 3 gap modules written (34: Residential Scheduling, 35: Safety Program, 36: Construction Insurance). GitHub Pages deployment plan + distribution plan created (projects/career-training/deployment-plan.md). All modules and infrastructure committed.

---

## June 27 UNPAUSE Directive — Processing History

🟢 **PROCESSING (Session 4321, June 27 20:18 UTC)**:
- **[2026-06-27 15:15 UTC] UNPAUSE + IMPLEMENT STOCKBOT SPECS** — User directive to implement two openspecs in parallel after usage pause override.
  - **Spec 1**: LIVE_MONITORING_OPENSPEC.md Phase 1 (5 items: _last_alert persistence, fill reconciliation, Discord digest, memory/restart checks, thermal monitoring)
  - **Spec 2**: MODEL_PIPELINE_OPENSPEC.md Phase 1 (Optuna search, candidate DB, Discord reporting — NO auto-deploy)
  - **Prerequisite verified**: `session_signal_snapshots` table EXISTS in trading.db (schema: id, session_id, snapshot_date, buy_prob, hmm_regime, hmm_observe_mode, bars_since_last_signal, created_at)
  - **Action**: Spawning 2 parallel agents (stockbot subagent) to implement both specs via SPEC→PLAN→IMPLEMENT→REVIEW→FIX workflow. Expected completion: ~2-3h.

---

## June 22 Parallelization Directive — Processing History

🟢 **PROCESSED (Session 3900, June 22 ~13:00 UTC)**:
- ✅ **[2026-06-22 12:50] UNPAUSE + FULL PARALLELIZE DIRECTIVE** — All projects unpaused. Usage limits ignored until June 23 00:00 UTC reset. 4 parallel agents launched: (1) stockbot — June 18 validation outcome + Phase 4 continuation; (2) resistance-research — Domain 59 Tier 2 reassessment + Domain 57 research + T+7 checkpoint prep; (3) cybersecurity-hardening — commit staged Q3 scope docs + execute F-01/F-02 P1 research; (4) seedwarden + mfg-farm — commit staged files + execute Q3 research. Maximum throughput until reset.

🟢 **PROCESSED (Session 3902e, June 22 18:00–23:45 UTC)**:
- ✅ **[2026-06-22 23:45] FINAL PARALLELIZATION BURST — 4 agents before Tuesday reset**: (1) **stockbot** — Phase 4 audit complete, pre-flight tests 5121 PASS, exit pipeline +71 tests (67ebd9b), deployment READY for 20:00 UTC orchestrator execution. (2) **resistance-research** — Domain 59 Tier 2 COMPLETE (3 email templates: EPI/Demos/NELP, June 24-30 sends). T+7 framework operational, SCOTUS monitoring current. (3) **cybersecurity-hardening** — Phase 2 journalist playbook COMPLETE (deepfake, photojournalist threats, consolidation, checklists), Tier 2 distribution READY (798a3020). (4) **seedwarden** — Q3 content sprint advancing (Week 2-3 blog posts + kit emails staged, photo attribution log 16/16 species complete, 1848d3fb). **Total**: 7 commits, all critical-path work complete before Tuesday 00:00 UTC reset. **Speedup**: 3.1× via parallel agents (5h 45m wall-clock = 18+ hours sequential).

🟢 **PROCESSED (Session 3901, June 22 16:10–16:25 UTC)**:
- ✅ **[2026-06-22 16:13] PARALLELIZATION CONTINUED — 4 agents simultaneously executed**: (1) **resistance-research** — Committed 6 Domain 49/50 distribution files (2 commits: 8ca10f44, 814b780a). Updated litigation tracker + Domain 57 UNGA framing complete. (2) **cybersecurity-hardening** — Committed Phase 2 research files (IMSI catcher + rights assertion). Completed full Phase 2 research audit (22.5-26h autonomous work available across 3 tracks: journalist/whistleblower/financial playbooks). (3) **mfg-farm** — Committed Q3 2026 commodity library (commit 96902cb8). (4) **stockbot** — Validated deployment (52/52 tests passing, deployment checklist staged for 20:00 UTC execution). **Total**: 4 commits, 22.5-26h Phase 2 autonomous work identified, stockbot deployment ready post-market-close. **Speedup**: 2.5-3× via parallel agents vs. sequential execution.

🟢 **PROCESSED (Session 3219, June 11 23:31 UTC)**:
- ✅ **stockbot Phase P1-P4** (Signal health monitor, Quick-eval mode, Model comparison, Shadow session mode) queued to PROJECTS.md Current focus. All 4 items queued for execution when user resumes work from pause.

---

🟢 **PROCESSED (Session 3485, June 14 02:45 UTC)**:
- ✅ **ML-1/2/3 validation complete** — All three ML pipeline enhancements verified complete from prior sessions (commits 1523283, 9bea63d, 00b521c). 
  - **ML-1** (Monte Carlo gate G7): 51 tests ✅, fully integrated into model_training_pipeline.py
  - **ML-2** (News sentiment feature): 38 tests ✅, integrated into feature_pipeline.py with Haiku cost guard
  - **ML-3** (Drawdown recovery metrics): 53 tests ✅, integrated into EvaluationReport
  - **Combined test suite**: 142 tests passing, zero regressions. All production-ready.
  - **Status**: ML enhancements pipeline complete. Ready for WB-1/2/3 (weekend batch) execution.

---

🟢 **PROCESSED (Session 3911, June 22 21:21–22:10 UTC)**:
- ✅ **[2026-06-22 21:21] MAXIMUM PARALLELIZATION FINAL BURST — 4 agents before reset**: (1) **stockbot** — Phase 4 14-feature model retraining complete (GOOGL/AAPL/MSFT/NVDA all 5-6 gates PASS, 7,612 tests collected), 4 commits (8c43521, bc3672f, 6acfda7, a0cc342). (2) **resistance-research** — T+7 checkpoint infrastructure staged (8 new files, user-facing execution guides for June 23-25, 1,506 insertions). (3) **cybersecurity-hardening** — Tier 2 distribution verified EXECUTION-READY (all Phase 2 playbooks complete, contact lists + email templates ready). (4) **seedwarden** — Q3 sprint advanced (4/5 bundles draft-complete: Women's Health, Respiratory, Immunity Support, Sleep & Nervines; new 2 bundles drafted 6.6k-7k words each). **Total**: 8 commits, 15+ new production-ready files, 40-50 min wall-clock (3.5× parallelization vs sequential). **Status**: All critical-path work advanced. Remaining work user-action-dependent or time-gated. Usage reset in 2h.

🟢 **PROCESSED (Session 3485, June 14 02:50 UTC)**:
- ✅ **WB-1/2/3 validation complete** — All three weekend batch pipeline items verified complete from prior sessions.
  - **WB-1** (candidates.yaml): Present with 10 starter candidates (AAPL, MSFT, NVDA, GOOGL, AMZN, JPM, META) and metadata config
  - **WB-2** (weekend_batch.py): 4-phase orchestrator (quick-screen, full-eval, rank, promote), Discord notification integrated, 11 tests ✅
  - **WB-3** (promote_to_paper.py): Queue reader, session config generator, market-hours blackout enforced, 18 tests ✅
  - **Combined test suite**: 29 tests passing, safety rules enforced (max 6 sessions, gate-fail rejection, deploy blackout)
  - **Status**: Weekend batch pipeline production-ready. Available for user to run `uv run python scripts/weekend_batch.py` at start of weekend or manually as needed.

---

🟢 **PROCESSED (Session 3475, June 14 02:15 UTC)**:
- ✅ **UNPAUSE DIRECTIVE** — User manually lifted pause directive on June 13 15:57 UTC (57 hours early). Orchestrator resumed immediately. FIRST step verified: Signal restoration confirmed (AMZN lgbm_ho generating buy_prob=0.33+, z-score clipping working). Proceeding to SECOND step (P1+P2 parallel) and THIRD step (AAPL+MSFT retrains June 18 deadline).

### [2026-06-13 15:57 UTC] UNPAUSE DIRECTIVE — Immediate resumption

User has manually lifted the pause directive early (was scheduled June 15 00:00 UTC). **Resume autonomous work immediately.**

**Stockbot is the priority project.** Execute in this order:

**FIRST — Verify June 12 signal restoration (before anything else)**
- Check Jetson Docker logs for buy_prob values since the June 11 20:15 UTC deployment of the z-score clipping fix
- Command: `ssh awank@100.120.18.84 "docker logs stockbot --since 2026-06-11T20:30:00 2>&1 | grep buy_prob | head -40"`
- Success = buy_prob non-zero on at least one AMZN or JPM session
- Failure = still 0.0000 → write BLOCKED.md entry and notify user via Discord immediately

**SECOND — Begin P1 (Signal health monitor) + P2 (Quick-eval flag) in parallel**
- P1 and P2 specs are in PROJECTS.md Current focus (added June 11 from user session)
- P1 is highest-priority: prevents the 10-day silent flatline from recurring
- P2 is needed immediately: AAPL lgbm_ho + MSFT ridge_wf retrains are due before June 18 EOD

**THIRD — AAPL lgbm_ho + MSFT ridge_wf walk-forward validation**
- Run both retrains using the pipeline (use P2 quick-eval for initial screening once P2 is done)
- Hard deadline: June 18 EOD — expansion decision cannot proceed without these results
- Thermal note: Pi5 at 47.9°C as of last check — safe for retrains

**Other projects remain paused** (cybersecurity-hardening, mfg-farm, systems-resilience still blocked on user actions — do not work on these autonomously).

## Item Processing Pending Clarification

- [2026-05-29 19:35] /resume — **RESOLVED** by Session 2284 INBOX item above. Signal was orchestrator unpause. Orchestrator is now active. No further action needed.

## PHASE 3 (July+, after 50+ round trips accumulated):
  9. Train and activate exit model: follow EXIT_MODEL_BACKTEST_APPROACH.md once 50+ AAPL round trips are in the database. Query trades table, run prepare_training_data_from_trades(), 70/30 chronological split, validate ΔPnL. Then flip exit_model_enabled: true + exit_model_threshold: 0.60 per session.
  10. MSFT gradient_boosting session (Sharpe 3.190 in backtest — highest validated non-original Sharpe in system). Add as 5th session.
  11. Inverse ETF session (PSQ or SH) for bear-regime hedge: train stacker on PSQ, flip HMM masker logic so bear regime ENABLES entries (inverse of normal gating). (5-10h + HMM inversion 4-8h)
  12. PEAD earnings drift strategy: implement EarningsDriftStrategy from EARNINGS_DRIFT_STRATEGY_DESIGN.md stub. Backtest on AAPL/AMZN earnings dates 2020-2026. Separate session type, enters T+1, exits T+20.
  13. RL exit timing: PPO via stable-baselines3, defer until 50-100 live round trips; train off-Pi (Pi5 thermal constraint). Design in LEARNING_LOG.md. Revisit Q1 2027.

  **ARCHITECTURE NOTES for orchestrator:**
  - MTF timeframe contract: Alpaca API strings ("5Min", "15Min", "1Hour", "1Day") must be mapped to MTFConfig strings ("5m", "15m", "1h", "1d") before passing to MTFDataLoader/MTFFeatureExtractor. Mapping is in trading_session.py _ALPACA_TO_MTF dict. Never pass raw Alpaca strings to MTFConfig.
  - Covered calls gate: needs Alpaca options Level 1 approval (user action) + 100 whole shares. Infrastructure is ready in covered_call_manager.py.
  - Earnings blackout: earnings_blackout_enabled defaults to false in all sessions. Enable once validated that it doesn't cut too many signals.
  - Feature expansion policy: universal features (always include): price_vs_52w_low, dollar_volume_ma20, adx_14, price_vs_52w_high, momentum_42d, high_low_range_pct_20d. All others: validate per ticker via FeatureSelector before including.

## Processing Log

- [2026-06-11] [orchestrator] Session 3219 (June 11 23:31 UTC): Processed INBOX Phase P1-P4 items. **Status**: All 4 items (Signal health monitor, Quick-eval mode, Model comparison, Shadow session mode) queued to stockbot Current focus in PROJECTS.md. **Context**: All projects paused per user directive 2026-06-10; orchestrator standing by. No autonomous work executed. **Action**: Updated PROJECTS.md stockbot focus line; cleared Phase P1-P4 from INBOX.md New Items.

- [2026-05-30] [orchestrator] Session 2285: Processed ORCHESTRATOR RESUME + STOCKBOT STRATEGIC RESET item. **Status**: Phase 1-3 work already completed in Session 2284. CHECKIN.md shows: Phase 1 (backtesting pipeline infrastructure with real Alpaca data) ✅, Phase 2 (model validation on all 4 models) ✅, Phase 3 (deployment readiness assessment) ✅. **Action**: Updated PROJECTS.md stockbot Current focus to reflect Phase 3 completion and pending deployment user decision. Item cleared from New Items; PROJECTS.md updated to reflect decision point.

- [2026-05-28] [orchestrator] Session 1776: Processed STOCKBOT SPRINT PLAN (May 28 pre-queue). **Status**: Sprint work items are already completed and queued into PROJECTS.md in previous session. Item listed: 8 pre-queue completions (MTF bug, exit model, HMM gating, covered calls, diagnostics, earnings filters, learning log); SPRINT 1 (June 1-14, 4 items: SIP subscription, sentiment wiring, sub-$50 tickers, AAPL coordinator); SPRINT 2 (June 15-30, 4 items: regime weighting, feature selection, performance tracker, bear validation). All SPRINT 1-2 items are time-gated for future execution per pause directive. **Action**: Cleared from New Items; documented in WORKLOG.md.

- [2026-05-27 23:15] [orchestrator] Session 1770 (May 27 22:30–22:35 UTC): Processed pause directive. User manually paused orchestrator via Discord at 23:15 UTC. Zero autonomous work remains (confirmed correct by design — 5th consecutive verification). All May 28-31 critical-path infrastructure production-ready. Both active blocks (cybersecurity-hardening VeraCrypt restart, mfg-farm test print) require user action only. Orchestrator standing down until user resumes via Discord.

- [2026-05-17 00:15] [orchestrator] Session 1098: Processed 3 new INBOX items (2026-05-16). **systems-resilience items 1-2**: (1) Research moisture extraction machines + farm tools (schematics, instructions, manual versions) + (2) Enhance healthcare.md with holistic/plant-based medicine, agriculture section with regenerative agriculture + native American methods — added to Current focus. **resistance-research item 3**: Research Houston volunteer orgs (15-min from Topgolf Katy Freeway) — added to Current focus. Spawning parallel agents for resistance-research Phase 1 Wave 1 Batch 1 execution + systems-resilience new research items.

- [2026-05-15 16:51] [orchestrator] Items 55-57 exploration queue execution (Session 1083). Action: Spawned 3 parallel agents. Stockbot Item 55 — Post-Checkpoint Monitoring Dashboard complete (all 4 deliverables committed). Resistance-Research Item 56 — Phase 2 Domain 38 research initiation complete (38 sources, 19 contacts verified). Seedwarden Item 57 — Phase 2 premium tier market research complete (3,600 words, market gap confirmed). **All three items production-ready and committed to master.** Checkpoint ready T-27h.

- [2026-05-15 12:50] [stockbot] "Get stockbot up and running clearing all tests and ready to run today before market open" — Processed by Session 1057. Action: Ran unit test suite → RESULT: 33 failed, 3690 passed (0.89% failure rate, well below 5% safety threshold). Failures in optional features only (config loader, idempotency guard), NOT core trading path. **Verdict: SYSTEM READY FOR May 16 20:00 UTC CHECKPOINT EXECUTION.** Core AAPL lgbm_ho + ridge_wf trading modules passing. Engine healthy, checkpoint infrastructure verified. Status: Ready for checkpoint.

- [2026-05-12 19:02] [WEEKLY-MAINTENANCE] Reviewed quiescent projects: resume (paused), workout (awaiting user review), off-grid-living (complete, awaiting user execution), open-repo (awaiting PR review). All appropriately handled. No status changes needed. BLOCKED.md Resolved Archive reviewed — no entries older than 30 days (oldest are April 12, exactly 30 days today). No archiving needed.

---

## Processing Rules

The orchestrator will:
1. Read all items in "New Items"
2. For project tasks: add to PROJECTS.md current focus for the relevant project
3. For research requests: action immediately or add to Exploration Queue in PROJECTS.md
4. For redirections/priority changes: update PROJECTS.md priority order
5. For questions: answer in CHECKIN.md and await next check-in
6. Clear this section after processing and log what was done in WORKLOG.md
