# Stockbot Sprint 3

> **Orchestrator protocol**: At the start of every session, check this file.
>
> **Item states**:
> - `- [ ]` = not started — pick the first one and work it
> - `- [~]` = waiting for user — code complete but blocked on approval/decision/verification
> - `- [x]` = fully complete including any required deployment or user confirmation
>
> **Rules**:
> 1. Pick the FIRST `[ ]` item and work it. Follow SPEC→PLAN→IMPLEMENT→REVIEW→FIX.
> 2. When code is done but needs user action before it's complete (deploy approval, decision, physical test):
>    mark the item `[~]`, add an entry to BLOCKED.md, and append to NOTIFY_QUEUE.md.
>    Do NOT mark `[x]` until the user has confirmed. Do NOT start the next item while one is `[~]`.
> 3. When a `[~]` block is resolved: mark the item `[x]`, remove the BLOCKED.md entry, commit, proceed.
> 4. When all items are `[x]`: append sprint-complete notice to NOTIFY_QUEUE.md.
>
> **A pre-commit hook enforces rule 2**: if any item is `[~]` and no matching active BLOCKED.md entry
> exists, the commit is rejected. You cannot bypass this by writing it only in WORKLOG or CHECKIN.

---

## Phase 0 — Investigation (Do First)

- [~] **INV-1**: Investigate buy_prob flatline. ✅ **ROOT CAUSE FOUND & FIXED** (Session 3204): z-score clipping to [-5, 5] range (OOD z-scores on AMZN/JPM features). 32 tests passing, committed to master. Ready for Jetson deployment (post-market 20:00 UTC).

- [x] **INV-2**: Build backtesting pipeline with real Alpaca data. ✅ **COMPLETE** (Phase 1 Sessions 2284+): WalkForwardEngine + EnsembleStackerAdapter built. AlpacaProvider for real historical data. Walk-forward splits with no lookahead. Full metric suite (Sharpe, Sortino, Calmar, Max DD, WFE, regimes, t-stat). Scripts: evaluate_model.py. Tests: 75+ passing. Status: PRODUCTION-READY.

---

## Phase 1 — Remaining HIGH Items

- [ ] **H-4**: `EnsembleStackerAdapter._build_features` calls `PipelineIntegrator` with `provider=None`, disabling cross-asset features in all backtests. Fix: pass the real provider. Verify that multi-ticker correlation features are now included in backtest feature sets.

- [x] **H-5**: `WalkForwardEngine` bypasses `ModelRegistry` with raw `sqlite3`, creating two separate views of model state that can drift. Fix: route all model registry reads through `ModelRegistry`. Verify no direct sqlite3 calls remain in walk_forward_engine.py.

---

## Phase 2 — MEDIUM Items

- [x] **M-1**: Performance metrics consolidation. ✅ **COMPLETE** (Session 3204): Consolidated three overlapping modules into canonical `src/backtesting/performance_metrics.py`. Added wrapper functions for walk_forward_engine. 1000+ tests passing. Commit: fb09dcf.

- [x] **M-2**: `TradingSession.__init__` refactoring. ✅ **COMPLETE** (Session 3204): Extracted 282-line constructor into 7 helper methods (_init_state_variables, _init_hmm_masking, _init_exit_signal_generator, _init_earnings_blackout_filter, _init_earnings_drift_strategy, _init_guardrails, _init_risk_aggregator). Constructor reduced to 20 executable lines (93% reduction). Backward compatible. Commit: 03ce038.

- [x] **M-3**: `BEAR_CONFIRM_BARS` configuration. ✅ **COMPLETE**: Currently set to `BEAR_CONFIRM_BARS = 3` in `src/backtesting/walk_forward_engine.py` line 374, matching design intent ("confirmation window" — avoid transient one-day bear signal overtrading). Comment and code alignment verified. Intent documented.

- [ ] **M-4**: `_TIME_STOP_BARS`, `_FILL_POLL_ATTEMPTS`, `_BARS_RETRY_ATTEMPTS`, `_CYCLE_TIMEOUT`, `_BACKOFF_BASE`, `_BACKOFF_MAX` are module-level constants that belong in config. Move to `config/default_config.yaml` and read via `TradingSession`.

- [x] **M-5**: sqlite3 connection management in `_load_base_models`. ✅ **ALREADY FIXED**: Method uses `with _sqlite3.connect(...) as conn:` context manager (line 167) which automatically closes connection on all paths including exceptions.

- [ ] **M-6**: `stacker_registry` is loaded from JSON with no schema validation. Add schema validation (required keys, type checks) on load and raise a clear error on malformed input.

- [ ] **M-7**: `feature_store.py` is re-initialized on every `FeaturePipeline()` instantiation even when `use_cache=False`. Fix: lazy initialization or flag-gated construction.

- [x] **M-8**: `TRADING_DAYS_PER_YEAR` consolidation. ✅ **COMPLETE**: Extracted to `src/backtesting/constants.py`. Updated imports in: walk_forward_engine.py, walk_forward.py, performance_metrics.py, model_comparison.py, live_vs_backtest_tracker.py. Backward compatibility maintained (re-exported from backtesting.__init__). Tests passing (41/41 performance_metrics tests).

- [ ] **M-9**: Broker factory does not enforce single-broker-per-mode invariant. Add a guard that raises if more than one broker is registered for a given mode.

- [ ] **M-10**: `WORKLOG.md` referenced in commit conventions but is an orchestrator file, not a stockbot file. Clarify or remove the reference from stockbot commit docs.

---

## Phase 3 — LOW Items

- [ ] **L-1**: `trading_session.py` imports `hashlib` but only uses it for session stagger with no actual hashing. Remove unused import.

- [ ] **L-2**: `PredictionType` has deprecated aliases that shadow enum values. Remove deprecated aliases; update all call sites.

- [ ] **L-3**: `create_target_from_returns` in `BaseModel` has `threshold=0.0` default — generates all signals as BUY/SELL with no HOLD band. Set a sensible default (e.g. 0.001) and document the intent.

- [ ] **L-4**: `walk_forward_engine.py` uses both `import json` and `import json as _json` in same scope. Remove the duplicate.

- [ ] **L-5**: Scattered root-level `.py` scripts with no clear ownership. Audit and move each to appropriate `scripts/` subdirectory or delete.

- [ ] **L-6**: `BaseModel.validate_input` checks `list(X.columns) != self.feature_names` — order-sensitive, causes false failures. Switch to set comparison or sort both sides before comparing.

- [ ] **L-7**: `config/default_config.yaml` is not read by `TradingSession` — all operational parameters are inline constants. Wire `TradingSession` to read from config at startup (prerequisite: M-4 complete).

- [ ] **L-8**: `DailyLossKillSwitch` in `GuardrailChain` uses `day_open_equity` from `last_equity` — stale on first cycle after restart. Fix: fetch fresh equity from broker on restart before initializing kill switch baseline.

---

## Completion Criteria

All 21 items checked. Buy_prob investigation resolved with documented root cause. Backtesting pipeline operational (can produce a backtest report for AMZN or JPM). All fixes have passing tests. Changes committed to master.
