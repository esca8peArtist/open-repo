# Stockbot Sprint 3

> **Orchestrator protocol**: At the start of every session, check this file.
> If any item is unchecked `- [ ]`, work on the FIRST unchecked item immediately — do NOT
> wait for user direction between items. Follow SPEC→PLAN→IMPLEMENT→REVIEW→FIX for each.
> When an item is complete, check it off, commit, and start the next one in the same session
> if usage budget permits. Only stop if you hit a genuine block requiring user input.
>
> **BLOCKED means**: anything where you cannot proceed without user action — including deployment approval,
> a decision between two implementation approaches, or a test result you need the user to verify physically.
> "Waiting for approval" is a block. "Needs user decision" is a block. Mentioning it only in WORKLOG is NOT enough.
>
> When blocked: (1) add entry to BLOCKED.md with What I need + Verify with fields, (2) append `- [ ] [stockbot] <title> — <what you need>` to NOTIFY_QUEUE.md pending section. Do NOT continue to next sprint item until the block is resolved.
> When sprint complete: append `- [ ] [stockbot] Sprint 3 complete — all 21 items done. Ready for Sprint 4 direction.` to NOTIFY_QUEUE.md.

---

## Phase 0 — Investigation (Do First)

- [x] **INV-1**: Investigate buy_prob flatline. Both AMZN and JPM sessions have returned `buy_prob=0.0000, action=HOLD` for every cycle since June 1 (10+ days, 0 trades). Determine root cause: is this a model issue (models never trained to produce buy signals on current data), a feature issue (features not correctly computed post-Sprint-2 fixes), a threshold issue, or a data issue? Query the database, inspect session logs, run a manual prediction. Produce a 1-page diagnosis with root cause and fix recommendation.

- [ ] **INV-2**: Build backtesting pipeline with real Alpaca data (strategic reset top priority). Implement per `docs/COMPREHENSIVE_BACKTESTING_SYNTHESIS_REPORT.md`. Goal: be able to run a backtest on AMZN/JPM and see whether the models _should_ be generating buy signals given the last 60 days of price data. This is the diagnostic tool needed to evaluate all future model changes.

---

## Phase 1 — Remaining HIGH Items

- [ ] **H-4**: `EnsembleStackerAdapter._build_features` calls `PipelineIntegrator` with `provider=None`, disabling cross-asset features in all backtests. Fix: pass the real provider. Verify that multi-ticker correlation features are now included in backtest feature sets.

- [x] **H-5**: `WalkForwardEngine` bypasses `ModelRegistry` with raw `sqlite3`, creating two separate views of model state that can drift. Fix: route all model registry reads through `ModelRegistry`. Verify no direct sqlite3 calls remain in walk_forward_engine.py.

---

## Phase 2 — MEDIUM Items

- [ ] **M-1**: Three separate performance metric calculation modules with overlapping functionality (`walk_forward_engine.py`, `walk_forward.py`, and a third). Consolidate into a single canonical module. Update all callers.

- [ ] **M-2**: `TradingSession.__init__` is 270+ lines. Extract component initialization into private helper methods (`_init_data_providers`, `_init_models`, `_init_risk`, etc.). No behavior change — pure structural refactor.

- [ ] **M-3**: `BEAR_CONFIRM_BARS` is set to 1 (immediate exit) but the comment says "confirmation window". Determine correct value from model training data and document the intent explicitly.

- [ ] **M-4**: `_TIME_STOP_BARS`, `_FILL_POLL_ATTEMPTS`, `_BARS_RETRY_ATTEMPTS`, `_CYCLE_TIMEOUT`, `_BACKOFF_BASE`, `_BACKOFF_MAX` are module-level constants that belong in config. Move to `config/default_config.yaml` and read via `TradingSession`.

- [ ] **M-5**: `_load_base_models` in `EnsembleStackerAdapter` opens a raw sqlite3 connection but never closes it on exception. Fix: use context manager or explicit finally block.

- [ ] **M-6**: `stacker_registry` is loaded from JSON with no schema validation. Add schema validation (required keys, type checks) on load and raise a clear error on malformed input.

- [ ] **M-7**: `feature_store.py` is re-initialized on every `FeaturePipeline()` instantiation even when `use_cache=False`. Fix: lazy initialization or flag-gated construction.

- [ ] **M-8**: `TRADING_DAYS_PER_YEAR = 252` defined separately in `walk_forward_engine.py` and `walk_forward.py`. Extract to a shared constants module.

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
