# Exit Model Feature Candidates

**Session**: 3816 (June 17 19:32 UTC)  
**Scope**: Pre-stage exit model training infrastructure. Phase 3 requires 50+ AAPL round trips before training can begin (expected July 1-5 contingent on June 18 validation).  
**Value**: Enables Phase 3b training within 48h once data accumulates. De-risks timeline by front-loading feature engineering.  

---

## Feature Candidate Set

All features are derived from existing signal strategies and state variables in the codebase.

### Category 1: Temporal Position State (Lookback Window Features)

These features capture the age and history of the position from decision-making perspective.

| Feature | Definition | Source | Rationale | Data Type |
|---------|-----------|--------|-----------|-----------|
| **hold_duration_bars** | Number of bars since position entry (BUY timestamp to current bar) | trades.timestamp | Core exit signal: how long held | Integer |
| **hold_duration_minutes** | Minutes elapsed since position entry | trades.timestamp | Continuous time proxy | Float |
| **bars_since_last_signal** | Bars since last signal in this session | trading_session.signals_log | Signal staleness; regime tracking | Integer |
| **signal_recency_decay** | Exponential decay of signal recency (e^(-hold_duration_bars/50)) | Derived | Smooth time window | Float [0,1] |

---

### Category 2: Price Momentum & Return Metrics (Current State)

These features measure current market conditions and unrealized position state.

| Feature | Definition | Source | Rationale | Data Type |
|---------|-----------|--------|-----------|-----------|
| **current_unrealized_pnl** | Current unrealized P&L at current price vs entry price | Alpaca positions + last fill | Exit trigger: profitability state | Float ($) |
| **unrealized_pnl_pct** | Unrealized P&L as % of position cost basis | Alpaca positions + trades | Normalized return | Float (%) |
| **current_price_vs_entry** | Current price / entry price ratio | Alpaca quotes + trades | Price movement direction | Float (ratio) |
| **bars_with_positive_pnl** | Count of bars with unrealized_pnl > 0 since entry | Intrabar snapshots | Profitability window | Integer |
| **max_drawdown_from_entry** | Max price decline from highest price since entry | Intrabar bars | Downside capture | Float ($) |
| **max_drawdown_pct_from_entry** | Max drawdown as % of peak | Intrabar bars | Normalized drawdown | Float (%) |

---

### Category 3: Regime & Market Structure (Masker + Adapter State)

These features capture the market regime classification used by HMM masker and adaptive signaling.

| Feature | Definition | Source | Rationale | Data Type |
|---------|-----------|--------|-----------|-----------|
| **current_hmm_regime** | Current HMM regime state (0=quiet, 1=normal, 2=volatile) | HMMRegimeScalar | Regime-conditional exit thresholds | Categorical |
| **regime_dwell_time_bars** | Bars spent in current regime | HMMRegimeScalar.regime_history | Regime stability; exit momentum | Integer |
| **regime_transition_probability** | Estimated probability of regime switch in next N bars | HMMRegimeScalar fit parameters | Forward-looking regime risk | Float [0,1] |
| **volatility_regime** | Intrabar volatility estimate (realized vol last 20 bars) | bars OHLC | Exit confidence; slippage risk | Float (annualized %) |

---

### Category 4: Win Rate & Signal Quality (Historical Context)

These features summarize the session's historical performance trajectory.

| Feature | Definition | Source | Rationale | Data Type |
|---------|-----------|--------|-----------|-----------|
| **session_win_rate_ytd** | Year-to-date win rate for this ticker + model combo | trades.realized_pnl | Historical success rate | Float [0,1] |
| **session_win_rate_trailing_20** | Win rate over last 20 closed trades | trades.realized_pnl | Recent performance trend | Float [0,1] |
| **rolling_avg_hold_duration** | Average hold duration over last 10 trades | trades.timestamp | Typical exit timing | Integer (bars) |
| **rolling_avg_exit_return** | Average realized return per trade (last 10 exits) | trades.realized_pnl | Expected exit magnitude | Float (%) |
| **consecutive_wins** | Current consecutive winning trades | trades.realized_pnl | Momentum clustering | Integer |
| **consecutive_losses** | Current consecutive losing trades | trades.realized_pnl | Drawdown clustering | Integer |

---

### Category 5: Market Microstructure & Volatility Surface (Alpaca Data)

These features capture market conditions and instrument-specific characteristics.

| Feature | Definition | Source | Rationale | Data Type |
|---------|-----------|--------|-----------|-----------|
| **bid_ask_spread_bps** | Current bid-ask spread in basis points | Alpaca quotes | Liquidity; slippage cost | Float |
| **dollar_volume_ma20** | 20-bar moving average of dollar volume | Alpaca bars | Liquidity baseline | Float ($) |
| **current_dollar_volume_pct** | Current bar dollar volume as % of 20-bar MA | Alpaca bars | Relative activity | Float (%) |
| **price_vs_52w_low** | Current price / 52-week low ratio | Alpaca historical | Support distance | Float (ratio) |
| **price_vs_52w_high** | Current price / 52-week high ratio | Alpaca historical | Resistance distance | Float (ratio) |
| **atr_14_bars** | 14-bar Average True Range | Alpaca bars OHLC | Volatility magnitude | Float ($) |

---

### Category 6: Position-Specific Exit Rules (Hard Constraints)

These are deterministic exit conditions that override probabilistic models.

| Feature | Definition | Source | Rationale | Data Type |
|---------|-----------|--------|-----------|-----------|
| **time_stop_triggered** | Is position at time-stop exit threshold (h+10 for AAPL)? | trades.timestamp vs current time | Hard exit gate | Boolean |
| **max_loss_pct_breached** | Has position hit max loss % threshold (e.g., -5%)? | trades.entry_price vs current_price | Risk cutoff | Boolean |
| **max_profit_pct_breached** | Has position hit max profit % threshold (e.g., +10%)? | trades.entry_price vs current_price | Profit taking | Boolean |
| **position_age_exceeds_session_max** | Position age > max allowed (e.g., 6.5h session max) | trades.timestamp vs session duration | Session boundary | Boolean |

---

### Category 7: Feature Interaction & Composite Features (Derived)

These features combine multiple dimensions for non-linear exit patterns.

| Feature | Definition | Source | Rationale | Data Type |
|---------|-----------|--------|-----------|-----------|
| **roi_per_holding_hour** | (unrealized_pnl_pct) / (hold_duration_minutes / 60) | Derived | ROI velocity; diminishing returns pattern | Float (% per hour) |
| **win_rate_weighted_by_magnitude** | (winning_trades_sum_return) / (total_trades_count) | trades.realized_pnl | Quality-weighted performance | Float (%) |
| **drawdown_recovery_buffer** | unrealized_pnl_pct - max_drawdown_pct | Derived | Downside resilience | Float (percentage points) |
| **volatility_adjusted_hold_time** | hold_duration_bars / volatility_regime | Derived | Time-normalized-by-vol | Float |
| **regime_exit_confidence** | (regime_dwell_time > median) AND (win_rate > 60%) | Derived | Regime stability score | Float [0,1] |

---

## Feature Selection Strategy for Training

### Stage A (50 AAPL trips, ~150 bars of data, July 1-5)
Start with **high-confidence baseline** (low variance, well-grounded in signal logic):
- hold_duration_bars
- unrealized_pnl_pct
- current_price_vs_entry
- max_drawdown_pct_from_entry
- session_win_rate_trailing_20
- rolling_avg_exit_return
- time_stop_triggered
- max_loss_pct_breached

**Model**: Logistic regression or decision tree (simple, interpretable, low overfitting risk)  
**Target**: Exit probability = f(features above)  
**Threshold**: Default exit_model_threshold: 0.60 (60% confidence required)  

### Stage B (100+ AAPL trips, ~300 bars, July 10-15)
Expand with **secondary features** for multivariate discovery:
- Add: current_hmm_regime, volatility_regime, bid_ask_spread_bps, price_vs_52w_high/low
- Add interactions: roi_per_holding_hour, drawdown_recovery_buffer, regime_exit_confidence
- Upgrade model: Random forest or XGBoost (capture non-linearities)
- Feature importance analysis to prune weak features

### Stage C (150+ AAPL trips, ~450 bars, July 20-31)
Full ensemble with **interaction terms**:
- Regime-conditional feature sets (separate models for quiet/normal/volatile regimes)
- Ticker-specific tuning (MSFT, NVDA adapt from AAPL base)
- Temporal cross-validation to detect concept drift
- Deploy with monitoring dashboards (win rate, hold time, drawdown)

---

## Data Quality Gates

Before training, validate:

1. **Timestamp consistency**: All trades have BUY + SELL pairs with matching realized_pnl
2. **Price integrity**: Entry price matches order.price; current price is real-time quote
3. **PnL correctness**: realized_pnl = (exit_price - entry_price) * shares
4. **Outlier detection**: Max single-trade loss/gain within ±10x median (flag for investigation)
5. **Regime labeling**: HMM regime logged at every exit (no null values)
6. **Feature completeness**: Zero NaN values in feature matrix before training

---

## Success Criteria for Stage A

✅ Feature matrix prepared with ≥50 AAPL round trips  
✅ All 8 Stage A features extracted and validated  
✅ Logistic regression baseline trained (AUC-ROC ≥0.65 on training set)  
✅ Cross-validation fold consistency checked (no wild variance across folds)  
✅ exit_model_threshold tuned to maximize Sharpe on backtest subset  
✅ Deployed to active-sessions.json with exit_model_enabled: true  
✅ Paper trading live monitoring shows positive ROI on exits (vs no-exit baseline)  

---

## Timeline & Dependencies

| Milestone | Date | Dependency | Owner |
|-----------|------|-----------|-------|
| **Data accumulation starts** | June 18 | June 18 validation PASS/PROCEED | Orchestrator/Jetson |
| **50 AAPL trips reached** | ~July 1-3 | 5-10 trades/day cadence (validated) | Jetson trading engine |
| **Stage A training ready** | July 5 | 50 trips + clean labels | Orchestrator |
| **Stage A model deployed** | July 5-6 | Testing complete, no regressions | Orchestrator |
| **Stage B expansion** | July 10-15 | 100+ trips accumulated | Orchestrator |
| **Stage C ensemble** | July 20-31 | 150+ trips + multivariate signals | Orchestrator |

---

## Risk Mitigations

**Risk**: Feature data incomplete (null regime, missing quotes)  
→ **Mitigation**: Validate on sample of 10 trades before full training; gate 1 checks completeness

**Risk**: Overfitting to AAPL specifically; poor transfer to MSFT/NVDA  
→ **Mitigation**: Stage B tests feature importance; feature selection strategy includes cross-ticker validation in Stage C

**Risk**: Exit model degrades live performance (worse than "hold to time-stop" baseline)  
→ **Mitigation**: Shadow mode in July; compare exit_model ROI vs baseline before Stage B expansion; automatic rollback if Sharpe drops >10%

---

## Files Created
- This file: EXIT_MODEL_FEATURE_CANDIDATES.md
- (Next): EXIT_MODEL_DATA_VALIDATION_PIPELINE.md
- (Next): EXIT_MODEL_TRAINING_READINESS_CHECKLIST.md
