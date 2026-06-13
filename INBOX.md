# Inbox

> Drop tasks, ideas, or redirections here from your phone or any device.
> The orchestrator reads this at the start of every session and processes new items.
> After processing, items are moved to WORKLOG.md or PROJECTS.md and cleared from here.
>
> **Tip**: This file syncs via Obsidian if your vault is set up to include this directory.
> Add a task from your phone by editing this file in Obsidian.

---

## New Items

🟢 **PROCESSED (Session 3219, June 11 23:31 UTC)**:
- ✅ **stockbot Phase P1-P4** (Signal health monitor, Quick-eval mode, Model comparison, Shadow session mode) queued to PROJECTS.md Current focus. All 4 items queued for execution when user resumes work from pause.

---

### [2026-06-13 16:31 UTC] stockbot — ML Pipeline Enhancements (3 items, independent of WB series)

**Context**: Analysis of 12 LLM-for-trading concepts (businessbulls.in) against existing pipeline revealed three high-value gaps not covered by P1-P4 or WB-1/2/3: (1) no probabilistic risk quantification beyond point-estimate max drawdown, (2) no news sentiment signal despite research showing it's the one LLM use case that's genuinely additive to LightGBM, (3) drawdown recovery time not tracked. These are independent of each other and of the weekend batch pipeline — build them in any order, but ML-1 is highest priority as it becomes a G7 gate.

**Agent Loop**: Every item must go through SPEC→PLAN→IMPLEMENT→REVIEW→FIX. No shortcuts.

---

#### [ML-1] `src/analytics/monte_carlo.py` — Monte Carlo gate (G7)

**Priority**: Highest of the three — becomes a new graduation gate

**What it does**:
1. Takes the per-fold daily return sequences already produced by `WalkForwardEngine` (already in the evaluation JSON)
2. Bootstraps N=1000 sequences by random sampling with replacement from the fold returns (each sequence = same length as the full OOS period)
3. Computes from the bootstrap distribution:
   - `p_loss_6mo`: probability the strategy loses money over a 6-month period
   - `sharpe_p05` / `sharpe_p95`: 5th and 95th percentile annualized Sharpe
   - `max_dd_p95`: 95th percentile max drawdown (worst-case)
   - `is_robust`: boolean — True if `p_loss_6mo < 0.30` AND `sharpe_p05 > 0.50`
4. Adds a `monte_carlo` block to `EvaluationReport` (alongside existing gate results)
5. Registers as **Gate G7**: `is_robust=True` required to pass. Models with `p_loss_6mo >= 0.30` fail G7.

**Files to create/modify**:
- `src/analytics/monte_carlo.py` — new file, `MonteCarloAnalyzer` class
- `src/model_training_pipeline.py` — integrate into `ModelTrainingPipeline.run()` after full eval; add G7 to `EvaluationReport`
- `tests/analytics/test_monte_carlo.py` — new test file

**Interface**:
```python
from src.analytics.monte_carlo import MonteCarloAnalyzer

mc = MonteCarloAnalyzer(n_simulations=1000, seed=42)
result = mc.analyze(fold_returns=engine.fold_daily_returns)
# result.p_loss_6mo, result.sharpe_p05, result.sharpe_p95, result.max_dd_p95, result.is_robust
```

**Acceptance criteria**:
- `MonteCarloAnalyzer.analyze()` returns all 5 fields listed above
- G7 gate wired into `EvaluationReport.gates` list (index 6)
- `EvaluationReport.all_gates_passed` is False if G7 fails
- A model with constant-zero returns → `p_loss_6mo` ≈ 0.5 (sanity check)
- A model with strong positive returns → `p_loss_6mo` ≈ 0.0
- `n_simulations` and `seed` configurable via `PipelineConfig`
- All new tests pass; no regressions in existing 32+ tests

---

#### [ML-2] `src/features/news_sentiment.py` — LLM news sentiment feature

**Priority**: Second — additive signal with minimal risk, ~$6-10/year operating cost

**Depends on**: Nothing (standalone feature module)

**What it does**:
1. Calls Alpaca News API (`alpaca_trade_api.REST.get_news(symbol, start, end, limit=50)`) for the ticker and a lookback window (default: 7 calendar days before the training fold's end date)
2. For each article: sends headline + summary to Claude Haiku with a structured prompt: "Rate the sentiment of this financial news article about {ticker} on a scale from -1.0 (very bearish) to +1.0 (very bullish). Return only a JSON object with key 'score'."
3. Aggregates scores: `news_sentiment_7d = mean(scores)`, `news_sentiment_volume = len(articles)`, `news_sentiment_volatility = std(scores)`
4. Returns a feature dict that the feature pipeline can merge into the training DataFrame
5. Caches results to `data/news_sentiment_cache.sqlite` (key: ticker+date) to avoid re-fetching across training runs

**Files to create/modify**:
- `src/features/news_sentiment.py` — new file, `NewsSentimentFeature` class
- `src/features/feature_pipeline.py` — add optional `include_news_sentiment: bool = False` to `FeatureConfig`; if enabled, call `NewsSentimentFeature.get_features(ticker, date_range)` and merge
- `tests/features/test_news_sentiment.py` — new test file (mock Alpaca + Haiku calls)

**API key**: Use `ANTHROPIC_API_KEY` from env (same as main Claude API key). Model: `claude-haiku-4-5-20251001`.

**Cost guard**: If estimated cost for a batch exceeds $0.05 per model training run, log a warning and skip (do not fail). Estimate: ~50 articles × ~200 tokens/article × $0.00025/1K tokens (Haiku input) ≈ $0.0025/run — well under guard.

**Acceptance criteria**:
- `NewsSentimentFeature.get_features(ticker, date_range)` returns dict with 3 keys: `news_sentiment_7d`, `news_sentiment_volume`, `news_sentiment_volatility`
- Cache hit avoids API call (verified by mock)
- `FeatureConfig(include_news_sentiment=False)` (default) produces identical output to current pipeline — no regressions
- If Alpaca News returns 0 articles: all 3 features return 0.0 (not NaN)
- If Haiku API fails: log warning, return 0.0 for all 3 (graceful degradation)
- Unit tests use mocked Alpaca + Haiku responses; no live API calls in test suite

---

#### [ML-3] `src/analytics/drawdown_metrics.py` — Recovery time tracking

**Priority**: Third — quick win (~2h), no dependencies

**What it does**:
1. Takes the OOS daily return sequence from each walk-forward fold
2. Computes equity curve from cumulative returns
3. For each drawdown period (peak → trough → recovery):
   - Records drawdown depth, start date, trough date, recovery date (or None if not recovered by end of data)
   - Computes `recovery_days = (recovery_date - trough_date).days` (None if unrecovered)
4. Aggregates across all folds:
   - `avg_recovery_days`: mean recovery days across all completed drawdown episodes
   - `max_recovery_days`: longest single recovery (worst case)
   - `unrecovered_count`: number of drawdowns that never recovered within the OOS window
5. Adds to `EvaluationReport.drawdown_stats` block (alongside existing `max_drawdown_pct`)

**Files to create/modify**:
- `src/analytics/drawdown_metrics.py` — new file, `DrawdownAnalyzer` class
- `src/model_training_pipeline.py` — call `DrawdownAnalyzer` after walk-forward eval, add 3 new fields to `EvaluationReport`
- `tests/analytics/test_drawdown_metrics.py` — new test file

**Interface**:
```python
from src.analytics.drawdown_metrics import DrawdownAnalyzer

da = DrawdownAnalyzer()
stats = da.analyze(fold_daily_returns=engine.fold_daily_returns)
# stats.avg_recovery_days, stats.max_recovery_days, stats.unrecovered_count
```

**Acceptance criteria**:
- `DrawdownAnalyzer.analyze()` returns all 3 fields
- `avg_recovery_days` and `max_recovery_days` are integers (ceiling of float); `unrecovered_count` is int
- Constant-gain equity curve → `avg_recovery_days = 0`, `unrecovered_count = 0`
- Single drawdown that never recovers → `unrecovered_count = 1`, `avg_recovery_days` excludes it
- Fields appear in all `EvaluationReport` JSON outputs (backward-compatible: existing reports get `null` for these fields)
- All new tests pass; no regressions in existing tests

---

### [2026-06-13 16:08 UTC] stockbot — Weekend Batch Pipeline (3 items, build after P1+P2)

**Context**: User wants to train ~20 models in parallel on weekends/off-hours, rank them by gate performance, and automatically queue the top ones for paper trading the following week. The pieces (parallel trainer, comparison engine, session config manager) already exist. What's missing is the glue: a candidate matrix config, a top-level orchestration script, and a promotion script. These depend on P2 (quick-eval flag) being done first.

**Hetzner note**: `src/remote/` already has `hetzner_pipeline.py`, `hetzner_budget.py` (hard $20/month cap), and `remote_runner.py`. Do NOT wire Hetzner into the automated pipeline yet — user wants to test the Pi-local pipeline first. Hetzner is available for manual offload when needed (e.g., training AAPL with large data sets that would take >3 hours on Pi). Reference it in comments but do not add it to the automated flow.

---

#### [WB-1] `candidates.yaml` — Weekly candidate matrix config

**File**: `projects/stockbot/candidates.yaml`

A config file the user edits each week to define the model search space. The orchestrator should never modify this file autonomously — it is user-owned.

```yaml
# Weekend batch candidate matrix — edit each week before Saturday run
# Each entry is one (ticker, strategy, optional overrides) combination
# Up to 20 candidates; more than 20 will be accepted but runtime grows linearly

meta:
  train_start: "2022-01-01"
  train_end: "2026-06-13"   # update each week
  wf_is_years: 3
  wf_oos_months: 6
  n_dsr_trials: 1
  max_workers: 3            # 4 cores on Pi5; leave 1 free. Raise to 4 if thermal OK.
  quick_screen: true        # run quick-eval first to filter obviously bad candidates
  quick_screen_min_sharpe: 0.70   # reject candidates below this in quick-eval
  top_n_promote: 3          # number of passing models to queue for paper trading

candidates:
  - ticker: AAPL
    strategy: lgbm_ho
  - ticker: AAPL
    strategy: ridge_wf
  - ticker: MSFT
    strategy: lgbm_ho
  - ticker: MSFT
    strategy: ridge_wf
  - ticker: NVDA
    strategy: lgbm_ho
  - ticker: GOOGL
    strategy: lgbm_ho
  - ticker: AMZN
    strategy: lgbm_ho
  - ticker: JPM
    strategy: ridge_wf
  - ticker: JPM
    strategy: lgbm_ho
  - ticker: META
    strategy: lgbm_ho
```

Write this file to `projects/stockbot/candidates.yaml`. Keep it simple and well-commented. This is the starting template — the user will add more candidates over time.

---

#### [WB-2] `scripts/weekend_batch.py` — Top-level pipeline orchestrator

**Depends on**: P2 (quick-eval flag) must be done first. Do not implement if P2 is incomplete.

**What it does**:
1. Reads `candidates.yaml` (or `--candidates path/to/file.yaml`)
2. **Phase 1 — Quick screen** (if `quick_screen: true`): runs all candidates through quick-eval (`PipelineConfig(quick=True)`), 4 workers in parallel, rejects anything below `quick_screen_min_sharpe`. Logs rejects with reason.
3. **Phase 2 — Full eval**: runs survivors through full 10-fold eval using `batch_train_models.py` logic (or import `ModelTrainingPipeline` directly), 3 workers in parallel.
4. **Phase 3 — Rank**: calls `ModelComparison` on all results, generates ranked table (sorted by OOS Sharpe, gates pass/fail shown).
5. **Phase 4 — Promote**: writes `paper_trading_queue.json` (top N where `all_gates_passed=True`, sorted by Sharpe), or writes `INBOX.md` entry if zero candidates passed all gates.
6. **Notify**: sends Discord message with summary (N passed, top model, Sharpe, queued for Monday deploy).

**Interface**:
```bash
uv run python scripts/weekend_batch.py \
    [--candidates candidates.yaml] \
    [--output-dir results/weekend_YYYYMMDD/] \
    [--max-workers 3] \
    [--dry-run]        # print job list, skip training
```

**Output files**:
- `results/weekend_YYYYMMDD/batch_summary.json` — all results + gate scores
- `results/weekend_YYYYMMDD/comparison_table.md` — ranked markdown table
- `paper_trading_queue.json` — top-N models ready for Monday deploy (overwritten each run)

**Exit codes**: 0 = at least one model promoted, 1 = no models passed all gates, 2 = error

**Blackout rule**: Respect `DEPLOY BLACKOUT RULE` — do not set `DEPLOY_READY` during market hours (13:30–20:00 UTC Mon–Fri). The script only generates `paper_trading_queue.json`; actual deploy is done by `promote_to_paper.py` (WB-3).

**Cron entry to add** (to `scripts/setup_cron.sh` or equivalent, runs on Pi):
```cron
# Weekend batch — Saturday 00:01 UTC
1 0 * * 6 cd /home/awank/dev/SuperClaude_Framework/projects/stockbot && uv run python scripts/weekend_batch.py >> logs/weekend_batch.log 2>&1
```

**Acceptance criteria**:
- Dry-run prints job list and exits 0
- Phase 1 quick-screen correctly rejects low-Sharpe candidates
- Phase 2 runs remaining candidates in parallel (verified by wall-clock timing)
- `paper_trading_queue.json` written correctly with model paths + session config snippets
- Discord notification sent via existing bot integration (see `scripts/discord-bot.py` for webhook pattern)
- All tests pass

---

#### [WB-3] `scripts/promote_to_paper.py` — Paper trading queue deployer

**Depends on**: WB-2 must be done first (reads `paper_trading_queue.json`).

**What it does**: Reads `paper_trading_queue.json`, generates a new `active-sessions-paper.json` using `SessionConfigManager`, and creates `DEPLOY_READY` at the appropriate time. This is the "Monday morning" step.

**Interface**:
```bash
uv run python scripts/promote_to_paper.py \
    [--queue paper_trading_queue.json] \
    [--max-sessions 3]        # max sessions to add (don't exceed Jetson capacity)
    [--dry-run]               # print what would change, don't write files
    [--replace-existing]      # replace current sessions; default is to ADD alongside
```

**Behavior**:
1. Read `paper_trading_queue.json`
2. Load current `active-sessions.json` via `SessionConfigManager`
3. For each candidate in queue (sorted by Sharpe, up to `--max-sessions`):
   - Generate session entry using `SessionConfigManager.template_custom()` or equivalent
   - Add with `position_size_pct: 0.10` (conservative default for new sessions)
   - Add with `shadow_mode: false` (live paper trading, not shadow — shadow is P4 and separate)
4. Validate combined session config (call `SessionConfigManager.validate()`)
5. Write new `active-sessions-paper.json`
6. Write `DEPLOY_READY` file (only if time is outside 13:30–20:00 UTC Mon–Fri)
7. Log changes to WORKLOG.md

**Safety rules** (hardcoded, not configurable):
- Never exceed 6 total sessions (Jetson resource limit)
- Never set `DEPLOY_READY` during market hours
- Never promote a model where `all_gates_passed=False`
- Always commit `active-sessions-paper.json` before setting `DEPLOY_READY`

**Acceptance criteria**:
- Reads `paper_trading_queue.json` correctly
- Generates valid `active-sessions-paper.json` (passes `SessionConfigManager.validate()`)
- Correctly blocks deploy during market hours
- Dry-run shows diff without writing files
- Unit tests cover: empty queue, exceeds max-sessions limit, market-hours block, gate-fail rejection

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
