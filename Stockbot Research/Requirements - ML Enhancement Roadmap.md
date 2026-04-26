# Requirements — ML Enhancement Roadmap

**Project:** Stockbot ML Enhancement  
**Date:** 2026-03-23  
**Status:** Draft  

---

## Section 1: ML Model Improvements

### R1 — Log-Returns as Prediction Target

**Requirement:** Replace raw price prediction everywhere in the pipeline with log-returns as the prediction target.

**Rationale:**
- Log-returns are stationary, normally distributed, and additive across time periods — properties that raw prices lack.
- Models trained on raw prices learn spurious trends and fail to generalize out-of-sample.
- Log-returns allow cross-asset comparison and are the standard target in quantitative finance.

**Scope:**
- All model training pipelines must compute `log(P_t / P_{t-1})` as the target variable before fitting.
- Forward return labels (e.g., 1-day, 5-day) must be log-return differences, not price differences.
- Data loaders, preprocessing transforms, and label constructors must be updated.
- Any existing raw-price targets must be deprecated and removed.

**Acceptance Criteria:**
- Training data labels are log-returns (verified by unit test).
- Model outputs represent predicted log-returns, not price levels.
- Documentation updated to reflect target definition.

---

### R2 — Walk-Forward Cross-Validation with 5-Day Embargo

**Requirement:** Replace k-fold cross-validation with walk-forward (time-series) cross-validation that enforces a 5-trading-day embargo between the training set end and the validation set start.

**Rationale:**
- K-fold cross-validation allows look-ahead bias when applied to time-series data.
- A 5-day embargo prevents information leakage from overlapping return windows and autocorrelated features.
- Walk-forward CV produces realistic out-of-sample estimates that reflect actual deployment conditions.

**Scope:**
- Implement a `WalkForwardCV` class that yields `(train_idx, val_idx)` splits in temporal order.
- Embargo is enforced by dropping `embargo_days=5` trading days from the beginning of each validation fold.
- Minimum training window: configurable (default 252 trading days).
- Step size: configurable (default 21 trading days / 1 month).
- Replace all existing `KFold`, `StratifiedKFold`, and `cross_val_score` calls.

**Acceptance Criteria:**
- No validation sample has a timestamp within 5 trading days of the training set end.
- Splits are always in chronological order (no shuffling).
- Unit tests verify embargo enforcement and fold ordering.

---

### R3 — LightGBM Model Support

**Requirement:** Add LightGBM as a supported model in the model registry, alongside the existing Random Forest and Gradient Boosting implementations.

**Rationale:**
- LightGBM trains significantly faster than scikit-learn's GradientBoostingClassifier on tabular financial data.
- It supports native handling of categorical features and missing values.
- Its leaf-wise growth strategy often produces better IC than depth-wise trees on financial datasets.

**Scope:**
- Implement a `LightGBMModel` class wrapping `lightgbm.LGBMRegressor` / `LGBMClassifier`.
- Expose key hyperparameters: `n_estimators`, `learning_rate`, `num_leaves`, `max_depth`, `min_child_samples`, `subsample`, `colsample_bytree`, `reg_alpha`, `reg_lambda`.
- Register in `ModelRegistry` under the key `"lightgbm"`.
- Expose in `dashboard_api.py` model selection endpoint.
- Add `lightgbm` to `requirements.txt`.

**Acceptance Criteria:**
- `ModelRegistry.get("lightgbm")` returns a configured LightGBM estimator.
- Model trains on the standard feature matrix and produces log-return predictions.
- Integration test confirms LightGBM appears in the dashboard model dropdown.

---

### R4 — Information Coefficient as Primary Evaluation Metric

**Requirement:** Replace MDI/permutation importance as the primary model evaluation metric with Information Coefficient (IC), defined as the Spearman rank correlation between predicted and actual log-returns.

**Rationale:**
- IC directly measures the monotonic relationship between model predictions and realized returns, which is the quantity that matters for alpha generation.
- Spearman rank correlation is robust to outliers and non-normality in return distributions.
- IC is the industry-standard metric for quantitative signal evaluation.

**Scope:**
- Implement `information_coefficient(y_pred, y_true)` → float using `scipy.stats.spearmanr`.
- Implement `ic_ir(ic_series)` → float (IC mean / IC std, analogous to Sharpe ratio of IC).
- Report per-fold IC and IC-IR in walk-forward CV output.
- IC must be displayed in the model evaluation dashboard panel.
- Existing accuracy/RMSE metrics may be retained as secondary metrics but IC is primary.

**Acceptance Criteria:**
- IC is computed and logged for every model evaluation.
- IC-IR is computed across folds and reported.
- Unit tests verify IC = 1.0 for perfect monotonic predictions and IC ≈ 0.0 for random predictions.

---

### R5 — SHAP Feature Importance

**Requirement:** Replace MDI (Mean Decrease in Impurity) and permutation importance with SHAP (SHapley Additive exPlanations) values for feature importance analysis.

**Rationale:**
- MDI is biased toward high-cardinality and continuous features in tree models.
- Permutation importance is slow and unstable on correlated features.
- SHAP provides theoretically grounded, consistent, and locally interpretable feature attributions.

**Scope:**
- Integrate `shap` library into model evaluation pipeline.
- Compute `shap.TreeExplainer` for tree-based models (RF, GB, LightGBM).
- Compute mean absolute SHAP values per feature as global importance.
- Store SHAP summary plot data as output artifact.
- Expose top-N SHAP features in dashboard model evaluation panel.
- Add `shap` to `requirements.txt`.

**Acceptance Criteria:**
- SHAP values computed for all tree-based models after training.
- Feature importance ranking based on mean |SHAP| values is displayed in dashboard.
- Unit test verifies SHAP values sum to prediction (consistency property).

---

### R6 — GARCH(1,1) Volatility Forecasting Module

**Requirement:** Implement a GARCH(1,1) volatility forecasting module that outputs a 1-step-ahead conditional volatility forecast, usable as both a feature in model training and as an input to position sizing.

**Rationale:**
- GARCH captures volatility clustering — a well-documented stylized fact in financial returns.
- A conditional volatility forecast is more accurate than realized volatility windows for sizing.
- Integrating GARCH vol as a feature can improve model predictions in high-vol regimes.

**Scope:**
- Implement `GARCHVolatilityModel` class using `arch` library (`arch.univariate.GARCH`).
- Fit GARCH(1,1) on training log-returns; produce 1-step-ahead vol forecast.
- Output: `sigma_t` (conditional standard deviation, annualized).
- Module must be fittable in walk-forward fashion (no look-ahead).
- Add `arch` to `requirements.txt`.
- Wire `sigma_t` as a named feature (`garch_vol_1d`) in the feature pipeline.
- Wire `sigma_t` as an input to position sizing (see R14 / R21).

**Acceptance Criteria:**
- GARCH(1,1) fits without errors on 252+ days of log-returns.
- `sigma_t` is produced for each out-of-sample period in walk-forward CV.
- Unit test verifies sigma_t > 0 and is finite for valid return series.

---

### R7 — Macro Features Integration

**Requirement:** Integrate three macroeconomic features — VIX percentile rank (20-day rolling), T10Y2Y yield spread, and federal funds rate — into the feature pipeline via the existing FRED client.

**Rationale:**
- Macro regime context (risk-on/off, yield curve inversion, monetary policy stance) provides alpha-relevant information orthogonal to price/volume features.
- The existing FRED client already handles data fetching; this requirement wires it into the feature pipeline.

**Scope:**
- **VIX Percentile Rank (20-day):** Compute percentile rank of current VIX level within its 20-day rolling window. Series: `VIXCLS`. Range: [0, 1].
- **T10Y2Y Yield Spread:** 10-year minus 2-year Treasury yield spread. Series: `T10Y2Y`. Units: percentage points.
- **Federal Funds Rate:** Effective federal funds rate. Series: `FEDFUNDS`. Units: percent.
- All three features must be aligned to trading dates (forward-filled for non-trading days).
- Add features as named columns: `vix_pct_rank_20d`, `t10y2y_spread`, `fed_funds_rate`.
- Wire into `feature_selector.py` and include in default feature set.

**Acceptance Criteria:**
- All three features are present in the feature matrix for any date with sufficient history.
- No look-ahead bias in feature construction (FRED data lagged by 1 business day).
- Unit tests verify alignment, dtype, and absence of NaN after warmup period.

---

## Section 2: Ensemble Enhancements

### R8 — Walk-Forward Stacking with Non-Negative ElasticNet Meta-Learner

**Requirement:** Implement walk-forward stacking where base model out-of-fold predictions are used to train a non-negative ElasticNet meta-learner.

**Rationale:**
- Standard stacking allows look-ahead bias when stacking predictions are generated on training data.
- Walk-forward stacking generates stacking features only from models trained on prior data, eliminating this bias.
- Non-negative ElasticNet ensures the meta-learner produces interpretable, positive-weight combinations of base models.

**Scope:**
- Meta-learner: `ElasticNet` with `positive=True`, `l1_ratio` and `alpha` tuned via inner CV.
- Base models: RF, GB, LightGBM (all registered models).
- Stacking features: each base model's out-of-fold log-return predictions.
- Meta-learner is retrained at each walk-forward step using all prior stacking data.
- Ensemble output replaces raw base model predictions as the default prediction.

**Acceptance Criteria:**
- Meta-learner weights are all non-negative.
- Walk-forward stacking IC >= best single base model IC (on held-out test set).
- Unit test verifies no future data in stacking features.

---

### R9 — 3-State HMM Regime Detection

**Requirement:** Implement a 3-state Hidden Markov Model (bull/bear/sideways) with soft posterior mixing weights that condition ensemble model outputs.

**Rationale:**
- Financial markets exhibit distinct return-generating regimes that are not captured by a single unconditional model.
- Soft (probabilistic) regime mixing avoids discontinuous portfolio behavior at regime boundaries.
- HMM posterior probabilities provide a principled basis for continuous ensemble weighting.

**Scope:**
- Implement `RegimeDetector` class using `hmmlearn.hmm.GaussianHMM` with `n_components=3`.
- States: bull (high mean, low vol), bear (negative mean, high vol), sideways (near-zero mean, moderate vol).
- Input features: log-returns, realized volatility (20-day), T10Y2Y spread.
- Output: posterior probability vector `[p_bull, p_bear, p_sideways]` at each timestep.
- State labels are assigned post-hoc by inspecting estimated means.
- Add `hmmlearn` to `requirements.txt`.
- Posteriors are used as mixing weights in regime-conditional ensemble (see R13).

**Acceptance Criteria:**
- HMM fits on 252+ days of return data without degeneracy (no state probability collapsing to 0).
- Posterior probabilities sum to 1.0 at each timestep.
- State ordering is consistent (bull state has highest estimated mean).
- Unit test verifies fit stability across random seeds.

---

### R10 — CPCV with Probability of Backtest Overfitting Reporting

**Requirement:** Implement Combinatorial Purged Cross-Validation (CPCV) and report the Probability of Backtest Overfitting (PBO) for all backtested strategies.

**Rationale:**
- Standard walk-forward CV produces a single backtest path, which may be cherry-picked.
- CPCV generates multiple backtest paths by combinatorially varying the train/test split, enabling overfitting detection.
- PBO quantifies the probability that observed backtest performance exceeds live performance by chance.

**Scope:**
- Implement `CPCVSplitter` generating combinatorial train/test splits as described in Lopez de Prado (2018).
- Parameters: `n_splits` (default 6), `n_test_splits` (default 2).
- Compute Sharpe ratio for each backtest path.
- Compute PBO as the fraction of simulated paths where the selected strategy underperforms the median.
- Report PBO alongside IC and IC-IR in model evaluation output.
- PBO > 0.5 triggers a warning in the dashboard.

**Acceptance Criteria:**
- CPCV generates `C(n_splits, n_test_splits)` unique backtest paths.
- PBO is in [0, 1].
- Unit test verifies split counts and purging/embargo correctness.

---

## Section 3: Novel Feature Systems

*Priority order: E → F → A → B → C → D*

---

### R11 (Novel E) — Earnings Call LLM Scoring

**Requirement:** Score CEO/CFO language in earnings call transcripts for confidence, specificity, and hedging using the Claude API, and output the score as a feature with 1-day and 5-day forward return signals.

**Rationale:**
- Earnings call language contains soft information not captured in financial statements.
- LLM scoring of executive communication quality has demonstrated alpha in academic literature.
- Claude API provides state-of-the-art language understanding for financial text.

**Scope:**
- Implement `EarningsCallScorer` class in `src/ml/earnings_scorer.py`.
- Input: raw earnings call transcript text (sourced from existing data pipeline or manual upload).
- Scoring dimensions:
  - **Confidence:** directness, absence of qualifiers, affirmative language (0–1 scale).
  - **Specificity:** quantitative claims, named targets, concrete timelines (0–1 scale).
  - **Hedging:** forward-looking disclaimers, uncertainty language, passive constructions (0–1 scale, lower = less hedging = more bullish signal).
- Claude API prompt: structured extraction with rubric, output parsed as JSON.
- Output features: `ec_confidence_score`, `ec_specificity_score`, `ec_hedging_score`, `ec_composite_score`.
- Compute 1-day and 5-day forward log-return means by quartile of composite score (signal validation).
- Scores are point-in-time (aligned to earnings announcement date) and excluded from pre-announcement windows.

**Acceptance Criteria:**
- Scorer produces all four output features for any transcript.
- Features are aligned to earnings date with no look-ahead.
- Backtested IC of composite score vs. 1-day and 5-day forward returns is reported.
- Unit test mocks Claude API and verifies JSON parsing and score bounds.

---

### R12 (Novel F) — Cross-Asset Momentum Module

**Requirement:** Rank SPY, EFA, BND, GLD, VNQ by 12-1 month momentum and output a regime signal and allocation weights for cross-asset context.

**Rationale:**
- Cross-asset momentum (trend-following across asset classes) is one of the most robust and persistent factors in finance.
- The relative strength of equities vs. bonds vs. commodities encodes macro regime information useful for single-stock models.

**Scope:**
- Implement `CrossAssetMomentum` class in `src/ml/cross_asset_momentum.py`.
- Universe: SPY (US equity), EFA (international equity), BND (US bonds), GLD (gold), VNQ (real estate).
- Momentum: 12-month total return minus 1-month total return (12-1 momentum, log-return version).
- Ranking: rank assets 1–5 by momentum score at each monthly rebalance date.
- Output features:
  - `xasset_spy_rank`, `xasset_efa_rank`, `xasset_bnd_rank`, `xasset_gld_rank`, `xasset_vnq_rank` (1 = best).
  - `xasset_regime`: categorical label (`risk_on` / `risk_off` / `defensive`) based on top-ranked asset.
  - `xasset_equity_weight`: allocation weight for equity assets (normalized momentum score).
- Data sourced via existing price data client; monthly rebalance with daily forward-fill.

**Acceptance Criteria:**
- Ranks are computed correctly with no look-ahead.
- `xasset_regime` transitions are smooth (no same-day flip-flop).
- Unit test verifies rank invariance under monotonic transformations of returns.

---

### R13 (Novel A) — Regime-Conditional Ensemble

**Requirement:** Use HMM posterior probabilities (from R9) as continuous mixing weights across model outputs, replacing hard regime switching.

**Rationale:**
- Hard regime switching creates discontinuous portfolio behavior and is sensitive to misclassification at boundaries.
- Continuous mixing (soft switching) blends model outputs proportionally to regime probability, producing smoother signals.

**Scope:**
- Implement `RegimeConditionalEnsemble` in `src/models/ensemble_models.py`.
- Input: per-regime model predictions (one RF/GB/LightGBM ensemble per regime, trained on regime-filtered data) + HMM posterior `[p_bull, p_bear, p_sideways]`.
- Output: `mixed_prediction = p_bull * pred_bull + p_bear * pred_bear + p_sideways * pred_sideways`.
- Regime-specific models are trained on data weighted by regime posterior (not hard-filtered).
- HMM posteriors must be computed from prior-period data only (no look-ahead).

**Acceptance Criteria:**
- Mixed prediction is a convex combination (weights sum to 1, all non-negative).
- IC of regime-conditional ensemble >= IC of unconditional ensemble on held-out test.
- Unit test verifies mixing weight constraints.

---

### R14 (Novel B) — Dynamic Kelly Position Sizing

**Requirement:** Chain GARCH vol forecast × VIX percentile rank adjustment × signal confidence into a fractional Kelly (0.25×) position size.

**Rationale:**
- Static position sizing ignores time-varying risk; Kelly criterion provides a principled volatility-adjusted size.
- Fractional Kelly (0.25×) reduces risk of ruin from estimation error.
- Layering VIX percentile rank as a regime scaler reduces exposure during high-uncertainty periods.

**Scope:**
- Implement `DynamicKellySizer` in `src/ml/kelly_sizer.py`.
- Inputs:
  - `sigma_t`: GARCH conditional volatility forecast (annualized).
  - `vix_pct_rank`: VIX 20-day percentile rank (from R7).
  - `signal_confidence`: predicted IC or model confidence score.
- Formula:
  1. Raw Kelly fraction: `f* = signal_confidence / sigma_t^2`
  2. VIX scaler: `vix_scaler = 1 - vix_pct_rank` (reduces size as VIX rank rises).
  3. Fractional Kelly: `position_size = 0.25 * f* * vix_scaler`
  4. Cap at `max_position` (configurable, default 5% of portfolio).
- Output: scalar position size as fraction of portfolio.

**Acceptance Criteria:**
- Position size is in [0, max_position] for all valid inputs.
- Position size decreases monotonically as `vix_pct_rank` increases (holding other inputs constant).
- Position size decreases as `sigma_t` increases.
- Unit tests verify formula correctness and boundary behavior.

---

### R15 (Novel C) — LLM Formulaic Alpha Generation

**Requirement:** Use the Claude API to generate novel factor candidates as mathematical transformations of price, volume, and fundamental data; systematically backtest candidates.

**Rationale:**
- The search space of formulaic alpha factors is vast; LLM-guided generation can surface non-obvious transformations faster than manual research.
- Systematic backtesting with IC evaluation prevents overfitting through rigorous out-of-sample testing.

**Scope:**
- Implement `LLMAlphaGenerator` in `src/ml/llm_alpha_generator.py`.
- Claude API prompt: describe available data fields (OHLCV, fundamental ratios, macro), request mathematical factor expressions in Python-evaluable string format.
- Candidate filter: expression must be parseable as a pandas/numpy operation on the feature DataFrame.
- Backtesting: compute IC of each candidate factor vs. 1-day and 5-day forward returns using walk-forward CV.
- Retention criteria: IC > 0.02 and IC-IR > 0.3 (configurable thresholds).
- Output: ranked list of retained factors with IC, IC-IR, and expression string.
- Retained factors are added to the feature pipeline as optional features.

**Acceptance Criteria:**
- Generator produces at least 10 candidate expressions per run.
- Backtesting pipeline handles exceptions from invalid expressions gracefully.
- Unit test mocks Claude API and verifies expression parsing and IC computation.

---

### R16 (Novel D) — Order Flow Imbalance Timing

**Requirement:** Implement a multi-level Order Flow Imbalance (OFI) signal for intraday entry timing after a daily directional signal has been generated.

**Rationale:**
- Daily signals indicate direction but not optimal entry timing within the day.
- OFI measures the imbalance between buy-initiated and sell-initiated volume at multiple price levels, providing a real-time entry quality signal.

**Scope:**
- Implement `OrderFlowImbalance` in `src/ml/order_flow_timing.py`.
- Input: Level 2 order book data (bid/ask sizes at top N levels) or intraday trade data with aggressor flag.
- OFI formula: `OFI = sum_i (bid_size_i_delta - ask_size_i_delta)` across N order book levels.
- Multi-level: aggregate OFI across top 5 price levels.
- Signal: use daily direction signal as gate; enter only when OFI confirms direction (OFI > threshold for long, OFI < -threshold for short).
- Output: `ofi_signal` (1 = enter, 0 = wait, -1 = avoid).
- Data sourced from broker Level 2 feed or historical reconstruction (configurable source).

**Acceptance Criteria:**
- OFI computed correctly from bid/ask delta sequences.
- Signal gates are only active after a daily directional signal exists.
- Unit test verifies OFI = 0 for balanced order flow and OFI > 0 for buy-dominated flow.

---

## Section 4: Brokerage/Execution Layer

### R17 — PDT Rule Enforcement

**Requirement:** Track round-trip trades per 5-day rolling window and warn or block new trades if the account balance is below $25,000.

**Rationale:**
- FINRA Pattern Day Trader rules restrict accounts below $25K to 3 round-trips in a 5-day window.
- Violation results in a 90-day trading restriction; automated enforcement prevents regulatory risk.

**Scope:**
- Implement `PDTTracker` in `src/trading/pdt_tracker.py`.
- Track all round-trip trades (open + close of same security, same day) in a 5-trading-day sliding window.
- If account equity < $25,000: warn at 2 round-trips, block at 3 round-trips.
- If account equity >= $25,000: PDT rules do not apply (institutional threshold).
- Integration with order executor: `PDTTracker.check_order(order)` returns `(allowed: bool, reason: str)`.
- Configurable: `pdt_warning_threshold`, `pdt_block_threshold`, `account_equity`.

**Acceptance Criteria:**
- Block is triggered on the 4th round-trip in 5 days when account < $25K.
- Warning is triggered on the 3rd round-trip.
- Unit tests cover edge cases: exact 5-day window boundary, account equity at $25K threshold.

---

### R18 — T+2 Settlement Tracking

**Requirement:** Track T+2 settlement for cash accounts and block same-day reuse of unsettled proceeds.

**Rationale:**
- Cash accounts cannot use proceeds from a sale until settlement (T+2 for equities).
- Trading on unsettled funds results in a "good faith violation" and potential account restriction.

**Scope:**
- Implement `SettlementTracker` in `src/trading/settlement_tracker.py`.
- Track all sale transactions with settlement date = trade_date + 2 business days.
- Maintain "settled cash" and "unsettled cash" balances separately.
- Block buy orders that would require unsettled cash.
- Integration with order executor: `SettlementTracker.available_cash(date)` returns settled balance only.
- Configurable: `account_type` (`cash` / `margin`); margin accounts exempt from T+2 blocking.

**Acceptance Criteria:**
- Cash from a sale on day T is not available until day T+2 (business days).
- Weekends and market holidays are handled correctly.
- Unit test verifies settlement date computation and balance blocking.

---

### R19 — Full Transaction Cost Model in Backtests

**Requirement:** Incorporate a full transaction cost model into backtests, including bid-ask spread, commission, and market impact (square-root model for large orders).

**Rationale:**
- Backtests ignoring transaction costs systematically overstate performance.
- Market impact is especially significant for larger orders and must be modeled separately from spread/commission.

**Scope:**
- Implement `ExecutionSimulator` in `src/backtesting/execution_simulator.py`.
- Components:
  - **Bid-ask spread:** `spread_cost = 0.5 * spread_bps * notional` (configurable spread_bps, default 5 bps).
  - **Commission:** flat per-trade or per-share, configurable (default $0.005/share, min $1).
  - **Market impact:** `impact_cost = impact_factor * sigma * sqrt(order_size / ADV)` (square-root model; configurable `impact_factor`, default 0.1).
- Total cost applied to each simulated trade fill.
- Returns: net fill price (slippage-adjusted) and total cost breakdown per trade.
- Integration: `ExecutionSimulator` wraps all backtest order fills.

**Acceptance Criteria:**
- Total cost > 0 for all non-zero orders.
- Market impact scales as sqrt of order_size/ADV.
- Unit test verifies cost components independently and combined.
- Backtest performance metrics (Sharpe, IC) computed on net-of-cost returns.

---

### R20 — MOC Order Support and TWAP for Large Orders

**Requirement:** Support Market-on-Close (MOC) order type and implement TWAP execution for orders exceeding 0.5% of Average Daily Volume.

**Rationale:**
- MOC orders reduce execution risk for end-of-day strategies by guaranteeing close price execution.
- TWAP reduces market impact for large orders by spreading execution across the trading day.

**Scope:**
- Implement MOC order type in `src/trading/order_executor.py`.
- MOC orders: submitted before market close cutoff (configurable, default 15:45 ET); fill at official closing price.
- TWAP: if `order_size > 0.005 * ADV`, split into N equal child orders distributed evenly across the trading session.
  - N = `ceil(order_size / (0.001 * ADV))` (1 child per 0.1% ADV).
  - Child orders submitted at equal intervals from 9:30 to 15:30 ET.
- TWAP fill prices averaged across child order fills.
- Both order types must integrate with the transaction cost model (R19).

**Acceptance Criteria:**
- MOC orders fill at close price with correct latency.
- TWAP triggers for orders > 0.5% ADV.
- Unit test verifies child order count formula and time distribution.

---

### R21 — Kelly + Vol-Scaled Position Sizing in Live/Paper Trading

**Requirement:** Apply Dynamic Kelly position sizing (from R14) in both live and paper trading modes.

**Rationale:**
- Consistent position sizing methodology between backtest, paper, and live trading is essential for realistic performance comparison.
- Kelly + vol-scaling enforces risk discipline automatically.

**Scope:**
- Integrate `DynamicKellySizer` (R14) into `src/trading/position_sizer.py`.
- Position sizer called before every order submission (live and paper).
- Inputs sourced in real-time: GARCH vol (from R6 model, updated daily), VIX percentile rank (from R7, updated daily), signal confidence (from model output).
- Output position size capped by `max_position_pct` (from risk_manager settings).
- Paper trading uses same sizer with simulated portfolio value.

**Acceptance Criteria:**
- Position sizer is called for every order in live and paper modes.
- Size output is within configured bounds for all test scenarios.
- Unit test verifies sizer output matches manual formula calculation.

---

### R22 — Expose Risk Manager Parameters in Settings UI

**Requirement:** Expose existing `risk_manager.py` parameters (max position size, kill switch thresholds, etc.) in the settings UI via the dashboard API.

**Rationale:**
- Risk parameters currently require code edits to change; this creates operational risk and slows response to market conditions.
- A settings UI allows authorized users to adjust risk parameters without a deployment.

**Scope:**
- Audit `risk_manager.py` for all configurable parameters:
  - `max_position_size_pct` (max single position as % of portfolio).
  - `max_portfolio_drawdown_pct` (kill switch threshold).
  - `max_daily_loss_pct` (intraday kill switch).
  - `max_sector_concentration_pct` (sector limit).
  - `max_correlation_threshold` (portfolio correlation limit).
- Expose via `GET /api/risk-settings` and `POST /api/risk-settings` endpoints in `dashboard_api.py`.
- Settings persisted to config file (not hardcoded).
- Frontend settings page displays and allows editing all parameters with validation (range checks).
- Changes take effect on next order evaluation (no restart required).

**Acceptance Criteria:**
- All listed parameters readable and writable via API.
- Invalid values (e.g., max_position_size_pct > 100) rejected with 422.
- Unit test verifies read/write round-trip and validation.

---

*End of Requirements Document*
