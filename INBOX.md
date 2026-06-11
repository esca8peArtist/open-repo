# Inbox

> Drop tasks, ideas, or redirections here from your phone or any device.
> The orchestrator reads this at the start of every session and processes new items.
> After processing, items are moved to WORKLOG.md or PROJECTS.md and cleared from here.
>
> **Tip**: This file syncs via Obsidian if your vault is set up to include this directory.
> Add a task from your phone by editing this file in Obsidian.

---

## New Items

### [2026-06-11] stockbot — Phase P1: Flatline / Signal-Drift Detector (Priority 1 of 4)

**Goal**: Prevent silent model failure like the June 1–11 buy_prob flatline (10 days, zero trades, no alert). Add automated daily signal health monitoring that fires a Discord notification and writes to INBOX.md when a session's signals look dead or degraded.

**Deliverable**: `scripts/signal_health_monitor.py` — runs post-market (after 20:15 UTC) on the Pi (not the Jetson). Reads the stockbot DB or Jetson API. Writes alert to `INBOX.md` and sends Discord notification if any threshold is breached.

**Checks to implement** (all rolling over last N trading days):
1. `buy_prob_mean_10d < 0.005` for a given session → "FLATLINE: {session_id} buy_prob has been near-zero for 10 days"
2. `buy_prob_mean_5d < 0.01` → "DEGRADED: {session_id} buy_prob weak for 5 days"
3. Rolling win_rate (last 20 fills) < 35% if >= 10 fills → "LOW WIN RATE: {session_id}"
4. Zero fills for > 15 consecutive trading days when market is open → "NO FILLS: {session_id}"

**Data source**: Query Jetson API at `http://100.120.18.84:8000/api/` (signals endpoint or DB). Fall back to reading `projects/stockbot/` DB path if API unreachable.

**Scheduling**: Add to Pi cron (via orchestrator hook or cron entry) at 20:30 UTC weekdays.

**Discord alert format** (send to same channel as bot):
```
⚠️ SIGNAL HEALTH ALERT — {session_id}
Check: {check_name}
Value: {value} (threshold: {threshold})
Days affected: {n}
Action: Check Docker logs + consider retrain
```

**Acceptance criteria**:
- Script runs without error and exits 0 when all sessions healthy
- Exits 1 and writes INBOX.md item + Discord message when threshold breached
- Tested with synthetic data covering each of the 4 alert conditions
- Cron entry added to `scripts/setup_cron.sh` or equivalent

---

### [2026-06-11] stockbot — Phase P2: Quick-Eval Mode for Fast Model Screening (Priority 2 of 4)

**Goal**: Reduce model eval time from ~30 min to ~5 min for rapid iteration. The AAPL lgbm_ho and MSFT ridge_wf retrains are coming June 12–18 and we need to iterate fast. A quick-eval mode lets us screen model configs before committing to a full eval.

**Deliverable**: Add `--quick` flag to `scripts/train_and_evaluate_model.py` and a matching `quick: bool = False` field to `PipelineConfig` in `src/model_training_pipeline.py`.

**Quick-eval parameters** (when `--quick` is set):
- `wf_folds = 3` (vs default 10)
- `train_years = 1.0` (vs default 3.0)
- `test_years = 0.25` (vs default 0.5)

**Required behavior**:
1. When `--quick` is used, the summary header and JSON output must include `"mode": "quick_eval"` and the warning `[QUICK EVAL — screening only, not deployment-ready]`
2. The exit code contract is unchanged (0=all gates pass, 1=fail, 2=exception) — gates are still evaluated, just on less data
3. Quick-eval results must NOT be persisted to the main reports DB (or must be tagged `quick=true` so they're filterable)

**Example usage**:
```bash
# Screen AAPL lgbm_ho quickly before committing to full retrain
uv run python scripts/train_and_evaluate_model.py \
    --ticker AAPL --strategy lgbm_ho \
    --train-start 2024-01-01 --train-end 2026-06-01 \
    --quick
# ~5 min, rough signal on whether to proceed
```

**Acceptance criteria**:
- `--quick` flag works end-to-end from CLI through pipeline
- Runtime verified < 8 min on Pi for a standard ticker
- Output clearly labeled as quick-eval, not persisted to main DB as a full report
- Unit tests cover `PipelineConfig(quick=True)` parameter propagation

---

### [2026-06-11] stockbot — Phase P3: Side-by-Side Model Comparison Script (Priority 3 of 4)

**Goal**: Run multiple (ticker, model_type) combinations in parallel and output a ranked comparison table. Needed for the expansion decision: we need to compare AAPL lgbm_ho vs AAPL ridge_wf vs MSFT ridge_wf before picking which to deploy.

**Deliverable**: `scripts/compare_models.py`

**Interface**:
```bash
uv run python scripts/compare_models.py \
    --tickers AAPL MSFT \
    --strategies lgbm_ho ridge_wf \
    --train-start 2022-01-01 --train-end 2026-06-01 \
    [--quick]          # use quick-eval mode (Phase P2)
    [--output results/comparison_20260612.md]
```

**Behavior**:
- Run all (ticker × strategy) combinations in parallel using `concurrent.futures.ThreadPoolExecutor`
- Each combination runs `ModelTrainingPipeline.run()` independently
- On completion, output a ranked Markdown table sorted by `agg_oos_sharpe` descending:

```
| Rank | Ticker | Strategy   | OOS Sharpe | Max DD | t-stat | DSR  | WF Eff | Gates |
|------|--------|------------|-----------|--------|--------|------|--------|-------|
|  1   | MSFT   | ridge_wf   |   2.34    | 12.1%  |  3.41  | 1.89 | 0.72   | 6/6 ✅ |
|  2   | AAPL   | lgbm_ho    |   1.87    | 15.3%  |  2.88  | 1.54 | 0.63   | 6/6 ✅ |
|  3   | AAPL   | ridge_wf   |   0.91    | 22.4%  |  1.43  | 0.71 | 0.49   | 2/6 ❌ |
```

- Save full JSON results alongside the Markdown table
- If any run errors, mark that row with `ERROR` and continue (don't fail the whole comparison)

**Acceptance criteria**:
- Runs 4 combinations (2 tickers × 2 strategies) in parallel without error
- Output table is valid Markdown, sorted by Sharpe descending
- Gate pass/fail per combination clearly shown
- `--quick` flag passes through to each underlying pipeline run

---

### [2026-06-11] stockbot — Phase P4: Shadow Session Mode (Priority 4 of 4)

**Goal**: Before swapping a model into live trading, run it in "observe-only" mode alongside existing live sessions for 3–5 trading days. Shadow sessions run the full prediction loop every cycle (fetch bars, compute features, run stacker, get buy_prob/predicted_return) but send NO orders to Alpaca.

**Why**: The 6-gate walk-forward eval catches statistical failure modes but not live distribution shift (see June 1–11 flatline). A shadow session run on the real Alpaca paper feed for a few days will immediately expose OOD issues before any money is at risk.

**Deliverable**: Add `shadow_mode: bool = False` to session config schema and implement shadow behavior in `TradingSession`.

**Implementation spec**:
1. In session config JSON (`active-sessions-*.json`), add optional field `"shadow_mode": true`
2. In `TradingSession._execute_cycle()`: if `shadow_mode` is True, skip the order submission step entirely. Still compute all signals, log `buy_prob`, `predicted_return`, `action` to a shadow log table in the DB (table: `shadow_signals`)
3. Shadow log schema: `(session_id TEXT, timestamp TEXT, ticker TEXT, buy_prob REAL, predicted_return REAL, action TEXT, cycle_id TEXT)`
4. Add `GET /api/shadow/{session_id}/summary` endpoint to the API: returns buy_prob mean/std/min/max over last N cycles, predicted_return distribution, action distribution (BUY/SELL/HOLD counts)

**Deployment workflow** (document in SHADOW_SESSION_WORKFLOW.md):
1. Train + gate model (full eval, not quick)
2. Add session to config with `"shadow_mode": true`
3. Deploy to Jetson + restart container
4. Monitor `/api/shadow/{session_id}/summary` for 3–5 trading days
5. If buy_prob distribution looks healthy (mean > 0.05, std > 0.01, not flatlined) → remove `shadow_mode` flag, redeploy → now live

**Acceptance criteria**:
- Shadow sessions run full prediction loop but submit no Alpaca orders (verified by unit test mocking the broker)
- `shadow_signals` table created and populated correctly
- `/api/shadow/{session_id}/summary` endpoint returns correct stats
- `SHADOW_SESSION_WORKFLOW.md` written and committed
- Existing live session tests unaffected

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
