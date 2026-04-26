# Task List — Implementation

**Project:** Stockbot ML Enhancement  
**Date:** 2026-03-23  
**Status:** Active  

---

> **Legend:** `[ ]` = Not started · `[x]` = Complete · `[~]` = In progress · `[!]` = Blocked  
> **Priority:** P0 = Do first (foundation) · P1 = Core improvements · P2 = Enhancements · P3 = Nice to have

---

## Phase 1: Foundation (P0 — Do First)

These tasks are prerequisites for all subsequent phases. Nothing in Phases 2–5 should be started until Phase 1 is complete.

| Task | File(s) | Req | Priority | Status |
|------|---------|-----|----------|--------|
| Create LightGBM model class | `src/models/lightgbm_model.py` | R3 | P0 | [ ] |
| Add log-returns target transformation | `src/ml/log_returns.py` | R1 | P0 | [ ] |
| Walk-forward CV with 5-day embargo | `src/ml/walk_forward_cv.py` | R2 | P0 | [ ] |
| IC + Sharpe + IC-IR metrics module | `src/ml/model_metrics.py` | R4 | P0 | [ ] |
| Add lightgbm, arch, shap, hmmlearn to requirements | `requirements.txt` | R3/R5/R6/R9 | P0 | [ ] |
| Register LightGBM in ModelRegistry + dashboard_api.py | `src/models/__init__.py`, `dashboard_api.py` | R3 | P0 | [ ] |

### Phase 1 Notes

- `log_returns.py` must provide a transform compatible with scikit-learn's `FunctionTransformer` interface so it can be inserted into any pipeline.
- `walk_forward_cv.py` must implement a scikit-learn-compatible CV splitter (yielding `(train_idx, val_idx)` tuples) with embargo enforcement.
- `model_metrics.py` is the shared metrics module; all phases that report IC or Sharpe draw from it.
- `requirements.txt` additions: `lightgbm>=4.0`, `arch>=6.0`, `shap>=0.44`, `hmmlearn>=0.3`.

---

## Phase 2: Core Improvements (P1)

Depends on Phase 1 being complete (walk-forward CV, log-returns, metrics module must exist).

| Task | File(s) | Req | Priority | Status |
|------|---------|-----|----------|--------|
| GARCH(1,1) volatility module | `src/ml/garch_volatility.py` | R6 | P1 | [ ] |
| Wire economic_features.py to feature pipeline | `src/api/feature_selector.py` | R7 | P1 | [ ] |
| SHAP integration in model evaluation | `src/ml/model_metrics.py` | R5 | P1 | [ ] |
| GARCH vol as feature in training pipeline | `src/api/dashboard_api.py` | R6 | P1 | [ ] |

### Phase 2 Notes

- `garch_volatility.py` must expose a walk-forward-compatible API: `fit(train_returns)` → `forecast()` → `sigma_t`.
- `feature_selector.py` wiring: VIX percentile rank (20-day), T10Y2Y, fed funds rate — aligned to trading dates, FRED-sourced, 1-day lagged.
- SHAP: add `compute_shap_importance(model, X)` function to `model_metrics.py`; call after every model fit.
- GARCH vol feature name: `garch_vol_1d`; wire as a named column in the feature DataFrame before model training.

---

## Phase 3: Novel Ideas (E → F → A → B → C → D)

Ordered by priority. Novel E is P1; F, A, B are P2; C, D are P3.

| Task | File(s) | Req | Priority | Status |
|------|---------|-----|----------|--------|
| Earnings call LLM scorer (Novel E) | `src/ml/earnings_scorer.py` | R11 | P1 | [ ] |
| Cross-asset momentum module (Novel F) | `src/ml/cross_asset_momentum.py` | R12 | P2 | [ ] |
| HMM regime detector (Novel A) | `src/ml/regime_detector.py` | R9 | P2 | [ ] |
| Dynamic Kelly sizer (Novel B) | `src/ml/kelly_sizer.py` | R14 | P2 | [ ] |
| LLM formulaic alpha generator (Novel C) | `src/ml/llm_alpha_generator.py` | R15 | P3 | [ ] |
| Order flow imbalance timing (Novel D) | `src/ml/order_flow_timing.py` | R16 | P3 | [ ] |

### Phase 3 Notes

- **Novel E (Earnings scorer):** Requires Claude API key in environment. Mock Claude API in tests. Output features: `ec_confidence_score`, `ec_specificity_score`, `ec_hedging_score`, `ec_composite_score`. Point-in-time alignment is critical — align strictly to earnings announcement date.
- **Novel F (Cross-asset momentum):** Universe: SPY, EFA, BND, GLD, VNQ. 12-1 month momentum, monthly rebalance, daily forward-fill. Output: 5 rank features + `xasset_regime` + `xasset_equity_weight`.
- **Novel A (HMM regime detector):** `hmmlearn.hmm.GaussianHMM`, `n_components=3`. Output: `[p_bull, p_bear, p_sideways]` at each timestep. Feeds into Novel B and Phase 4 ensemble.
- **Novel B (Kelly sizer):** Depends on GARCH vol (Phase 2) and VIX percentile rank (Phase 2). Formula: `position_size = 0.25 * (signal_confidence / sigma_t^2) * (1 - vix_pct_rank)`, capped at `max_position`.
- **Novel C (LLM alpha gen):** Candidate retention: IC > 0.02 AND IC-IR > 0.3. Retained factors added to optional feature set.
- **Novel D (OFI timing):** Requires Level 2 order book data. Gate: only active when a daily directional signal exists. Multi-level: top 5 price levels.

---

## Phase 4: Ensemble Enhancements (P2)

Depends on Phase 3 (HMM regime detector must exist for regime-conditional ensemble).

| Task | File(s) | Req | Priority | Status |
|------|---------|-----|----------|--------|
| Regime-conditional ensemble mixing | `src/models/ensemble_models.py` | R13 | P2 | [ ] |
| Walk-forward stacking implementation | `src/ml/walk_forward_stacking.py` | R8 | P2 | [ ] |
| CPCV + PBO calculation | `src/ml/walk_forward_cv.py` | R10 | P2 | [ ] |

### Phase 4 Notes

- **Regime-conditional ensemble:** `mixed_prediction = p_bull * pred_bull + p_bear * pred_bear + p_sideways * pred_sideways`. Regime-specific models trained with soft sample weights (posterior probabilities), not hard-filtered subsets.
- **Walk-forward stacking:** Meta-learner is `ElasticNet(positive=True)`. Base models: RF, GB, LightGBM. Stacking features are out-of-fold predictions only.
- **CPCV + PBO:** Add `CPCVSplitter` class to `walk_forward_cv.py`. PBO > 0.5 triggers dashboard warning. Default: `n_splits=6`, `n_test_splits=2`.

---

## Phase 5: Brokerage / Execution (P2–P3)

Can proceed in parallel with Phase 4. PDT and settlement tracking are P2 (regulatory risk). Cost model and order types are P2. UI is P3.

| Task | File(s) | Req | Priority | Status |
|------|---------|-----|----------|--------|
| PDT rule tracker | `src/trading/pdt_tracker.py` | R17 | P2 | [ ] |
| T+2 settlement tracker | `src/trading/settlement_tracker.py` | R18 | P2 | [ ] |
| Full transaction cost model | `src/backtesting/execution_simulator.py` | R19 | P2 | [ ] |
| MOC + TWAP order support | `src/trading/order_executor.py` | R20 | P2 | [ ] |
| Kelly + vol-scaled position sizing (live/paper) | `src/trading/position_sizer.py` | R21 | P2 | [ ] |
| Expose risk_manager params in API | `src/api/dashboard_api.py` | R22 | P2 | [ ] |
| Wire backtesting to frontend API | `src/api/dashboard_api.py` | R19 | P2 | [ ] |
| Settings UI for execution params | `web/src/pages/` | R22 | P3 | [ ] |

### Phase 5 Notes

- **PDT tracker:** 5-trading-day rolling window. Block at 3rd round-trip when account equity < $25K. Integrate with `order_executor.py` via `check_order()` call before submission.
- **Settlement tracker:** Separate `settled_cash` and `unsettled_cash` balances. Only applies to `account_type = "cash"`. Business day calendar must handle weekends + market holidays.
- **Transaction cost model:** Three components — spread (5 bps default), commission ($0.005/share, min $1), market impact (`0.1 * sigma * sqrt(size/ADV)`). Apply to every backtest fill.
- **MOC orders:** Submit before 15:45 ET; fill at official close. **TWAP:** trigger when `order_size > 0.005 * ADV`; split into `ceil(order_size / (0.001 * ADV))` child orders, equally spaced 9:30–15:30.
- **Position sizer (live/paper):** Call `DynamicKellySizer` before every order. Inputs updated daily (GARCH vol, VIX pct rank). Paper trading uses same logic with simulated portfolio value.
- **Risk manager API:** Endpoints `GET /api/risk-settings` and `POST /api/risk-settings`. Parameters persisted to config file. Invalid values return HTTP 422. No restart required for changes to take effect.
- **Backtest API wiring:** Backtest results (IC, Sharpe, PBO, cost-adjusted returns) must be accessible via dashboard API endpoint before frontend integration.
- **Settings UI:** Display and allow editing of all risk_manager parameters listed in R22. Include validation (range checks, type checks) in frontend.

---

## Dependency Map

```
Phase 1 (Foundation)
  └── Phase 2 (Core Improvements)
        ├── Phase 3 (Novel Ideas)
        │     └── Phase 4 (Ensemble Enhancements)
        └── Phase 5 (Brokerage/Execution) ← can start after Phase 1
```

- Phase 5 can be started independently after Phase 1, in parallel with Phases 2–4.
- Within Phase 3, Novel A (HMM) must be complete before Phase 4's regime-conditional ensemble.
- Novel B (Kelly sizer) depends on Phase 2's GARCH vol module.

---

## Tech Debt Register

| Item | Severity | Notes |
|------|----------|-------|
| K-fold CV calls to replace | High | Must be replaced before any model evaluation is trusted |
| Raw price prediction targets | High | Any model trained on raw prices produces biased estimates |
| MDI importance still in use | Medium | Replace with SHAP after Phase 2 |
| No transaction costs in backtest | High | All historical Sharpe figures are inflated until R19 is complete |
| risk_manager.py hardcoded params | Medium | Operational risk; address in Phase 5 |

---

## Review Checklist

Before marking any task complete:

- [ ] Unit tests written and passing (`uv run pytest`)
- [ ] No look-ahead bias in feature construction (date alignment verified)
- [ ] Walk-forward CV used (not k-fold)
- [ ] Log-returns used as target (not raw prices)
- [ ] IC reported for all model evaluations
- [ ] SHAP importance computed (Phase 2+)
- [ ] Transaction costs applied in backtests (Phase 5+)
- [ ] PDT and settlement checks wired for live/paper orders (Phase 5+)
- [ ] Conventional commit message used
- [ ] No secrets or credentials committed

---

*End of Task List*
