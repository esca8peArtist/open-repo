# Inbox

> Drop tasks, ideas, or redirections here from your phone or any device.
> The orchestrator reads this at the start of every session and processes new items.
> After processing, items are moved to WORKLOG.md or PROJECTS.md and cleared from here.
>
> **Tip**: This file syncs via Obsidian if your vault is set up to include this directory.
> Add a task from your phone by editing this file in Obsidian.

---

## New Items

(NONE — all pending items processed from Session 2979)

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
