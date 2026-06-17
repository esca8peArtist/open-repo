# Exit Model Training Data Readiness Checklist

**Purpose**: Continuous monitoring framework to determine when the exit model training
data threshold has been crossed and Phase 3b activation is viable. Run this checklist
at every post-market review (20:00 UTC) and before any Phase 3b decision.

**Trigger for Phase 3b**: 50+ completed AAPL round trips in `trading.db`.

---

## Section 1 — Cumulative Round-Trip Counter

Run against `trading.db` on Jetson (100.120.18.84) or the local Pi copy at `/opt/stockbot/database/trading.db`.

### 1.1 Per-Ticker Round-Trip Count

A completed round trip is a BUY that has a corresponding SELL with a later timestamp on the
same ticker and strategy. The schema uses `Trade.action` with values `'BUY'` and `'SELL'`
(see `src/database/schema.py` TradeAction enum). There is no `trade_side` or `exit_side`
column — use `action`.

```sql
-- Completed round trips per ticker (mode='paper' for current Phase 3)
SELECT
    b.ticker,
    COUNT(*) AS completed_round_trips
FROM trades b
WHERE b.action = 'BUY'
  AND b.mode = 'paper'
  AND EXISTS (
      SELECT 1 FROM trades s
      WHERE s.ticker       = b.ticker
        AND s.strategy_name = b.strategy_name
        AND s.mode          = b.mode
        AND s.action        = 'SELL'
        AND s.timestamp     > b.timestamp
  )
GROUP BY b.ticker
ORDER BY completed_round_trips DESC;
```

### 1.2 Phase Gate Mapping

| Round Trips (AAPL) | Gate Status  | Action                                 |
|--------------------|--------------|----------------------------------------|
| 0–24               | ACCUMULATING | No exit model work; continue live data |
| 25–49              | APPROACHING  | Pre-stage training scripts; review data quality |
| 50–99              | STAGE A READY | Train baseline exit model (see Roadmap) |
| 100–149            | STAGE B READY | Multivariate feature discovery         |
| 150+               | STAGE C READY | Ensemble exit model with regime weights |

### 1.3 Current Count (update daily)

| Date | AAPL | MSFT | JPM | AMZN | NVDA | Total |
|------|------|------|-----|------|------|-------|
| 2026-06-17 | ___ | ___ | ___ | ___ | ___ | ___ |

---

## Section 2 — Data Quality Gates

Before training, all completed round trips must pass each quality gate. A single FAIL
blocks training; investigate and remediate before proceeding.

### 2.1 Fill Price Accuracy (±0.01 threshold vs. mid-market)

Compares `fill_price` against expected mid-market price at execution time. A systematic
deviation > $0.01 indicates slippage measurement error or data feed latency.

```sql
-- Trades with suspicious fill prices (deviation from price field > $0.05)
SELECT
    id, ticker, action, timestamp,
    price              AS order_price,
    fill_price         AS actual_fill,
    ABS(fill_price - price) AS fill_deviation
FROM trades
WHERE mode = 'paper'
  AND ABS(fill_price - price) > 0.05
ORDER BY fill_deviation DESC
LIMIT 20;
```

**Gate**: Fewer than 5% of fills with deviation > $0.01. If threshold exceeded: audit
`AlpacaBroker._on_fill()` callback for timestamp misalignment.

### 2.2 Exit Timing Consistency

Valid exits must fall within 5–120 minutes of entry. Exits outside this window indicate
either a time-stop malfunction or a data integrity issue.

```sql
-- Round trips with exit timing outside 5-120 minute baseline
SELECT
    b.id       AS buy_id,
    b.ticker,
    b.timestamp AS entry_time,
    s.timestamp AS exit_time,
    CAST((julianday(s.timestamp) - julianday(b.timestamp)) * 1440 AS INTEGER)
                AS hold_minutes
FROM trades b
JOIN trades s ON
    s.ticker        = b.ticker
    AND s.strategy_name = b.strategy_name
    AND s.mode          = b.mode
    AND s.action        = 'SELL'
    AND s.timestamp     > b.timestamp
WHERE b.action = 'BUY'
  AND b.mode  = 'paper'
HAVING hold_minutes < 5 OR hold_minutes > 120
ORDER BY hold_minutes;
```

**Gate**: Zero exits under 5 minutes (sub-threshold signal churn). Exits over 120 minutes
are expected when the h+10 time-stop fires on low-volatility days — flag for context but
do not block training.

### 2.3 PnL Calculation Correctness

Reconcile `realized_pnl` on SELL records against the independently computed fill-based P&L.
Discrepancies of more than $0.10 per trade indicate a position-sizing or fee calculation bug.

```sql
-- PnL reconciliation: compare stored realized_pnl vs. computed from fills
SELECT
    s.id,
    s.ticker,
    s.timestamp            AS exit_time,
    s.realized_pnl         AS stored_pnl,
    (s.fill_price - b.fill_price) * b.qty AS computed_pnl,
    ABS(s.realized_pnl - (s.fill_price - b.fill_price) * b.qty) AS pnl_discrepancy
FROM trades s
JOIN trades b ON
    b.ticker        = s.ticker
    AND b.strategy_name = s.strategy_name
    AND b.mode          = s.mode
    AND b.action        = 'BUY'
    AND b.timestamp     < s.timestamp
WHERE s.action = 'SELL'
  AND s.mode   = 'paper'
  AND s.realized_pnl IS NOT NULL
HAVING pnl_discrepancy > 0.10
ORDER BY pnl_discrepancy DESC;
```

**Gate**: Fewer than 2% of trades with discrepancy > $0.10. If threshold exceeded: check
`PortfolioManager.close_position()` fee handling and qty tracking.

### 2.4 Null Fill Price Check

```sql
SELECT COUNT(*) AS null_fill_count
FROM trades
WHERE mode = 'paper'
  AND fill_price IS NULL;
```

**Gate**: Zero null fill prices. Any null blocks training — fix at source before extracting
training data.

---

## Section 3 — Minimum Viable Dataset Assessment

Thresholds sourced from `EXIT_MODEL_BACKTEST_APPROACH.md` Section "Minimum training-data
requirements" and the variance analysis documented there (50 trades → ~200 labelled bars,
minimum viable for 200-tree gradient booster).

### 3.1 Dataset Size Matrix

| Stage | Min Trades | Min Labelled Bars | Date Span | Model Type |
|-------|-----------|-------------------|-----------|------------|
| A (baseline) | 50 | 200 | 1+ month | Decision tree / logistic regression |
| B (multivariate) | 100 | 400 | 2+ months | Random forest |
| C (ensemble) | 150 | 600 | 3+ months | Ensemble with regime weights |

### 3.2 Positive Label Rate Check

After running `prepare_training_data_from_trades()`, inspect `meta['positive_rate']`.
The function already logs this; check the log output or capture `meta` directly.

| Positive Rate | Status | Action |
|--------------|--------|--------|
| < 0.05 | BLOCK  | Near-constant labels; model will be trivially constant. Wait for more diverse data. |
| 0.05–0.10 | CAUTION | Possible class imbalance; use `class_weight='balanced'` in ExitModel init. |
| 0.10–0.50 | GOOD | Proceed normally. |
| 0.50–0.95 | CAUTION | Time-stop may be firing too late; review h+10 logic. |
| > 0.95 | BLOCK  | Near-constant; model will trivially predict exit-always. |

### 3.3 Bars per Trade Check

Average intra-trade bars (from `meta['n_samples'] / meta['n_trades']`) should be >= 4.
Below 4, features that rely on a 4-bar lookback (trailing drawdown proxy, momentum)
are computed on incomplete windows.

---

## Section 4 — Bias Detection Checklist

Exit model training data collected during a short live window will inherit biases from
the specific market regime active during that window. These biases can cause the model
to over-fit regime-specific patterns and degrade in regime transitions.

### 4.1 Seasonal Clustering

```sql
-- Distribution of completed round trips by day of week
SELECT
    STRFTIME('%w', timestamp) AS dow,  -- 0=Sun, 1=Mon, ..., 5=Fri
    COUNT(*) AS trips
FROM trades
WHERE action = 'BUY'
  AND mode = 'paper'
  AND EXISTS (
      SELECT 1 FROM trades s2
      WHERE s2.ticker = trades.ticker AND s2.action = 'SELL'
        AND s2.timestamp > trades.timestamp
  )
GROUP BY dow
ORDER BY dow;
```

**Flag**: If >60% of trips cluster on 1–2 days of the week, the model will learn
day-of-week patterns rather than genuine exit signals. Accept as known limitation
at Stage A; include `day_of_week` as a feature at Stage B to make the bias explicit.

### 4.2 Regime-Dependent Patterns

Query the HMM regime logged with each trade:

```sql
SELECT
    regime,
    COUNT(*) AS trips,
    AVG(realized_pnl) AS avg_pnl
FROM trades s
JOIN trades b ON
    b.ticker = s.ticker AND b.strategy_name = s.strategy_name
    AND b.mode = s.mode AND b.action = 'BUY' AND b.timestamp < s.timestamp
WHERE s.action = 'SELL' AND s.mode = 'paper'
  AND s.realized_pnl IS NOT NULL
GROUP BY regime;
```

**Flag**: If fewer than 2 of the 3 HMM regimes (bull / sideways / bear) are represented
in the training set, the model cannot learn regime-conditional exit behaviour.
Recommendation: do not add `regime` as a feature at Stage A; activate regime weighting
at Stage B only after all three regimes appear in the data.

### 4.3 Volatility-Regime Specific Patterns

Cross-reference VIX percentile with trade dates. If all trades occurred during low-VIX
(< 20th percentile) or high-VIX (> 80th percentile) periods, the model's threshold
calibration will not generalise. Document the VIX range at training time and revalidate
after the first major volatility regime shift.

**Flag at deployment**: If live VIX deviates > 10 points from the training-period VIX
mean, issue advisory to re-examine threshold before relying on voluntary exits.

### 4.4 Ticker Concentration

```sql
SELECT ticker, COUNT(*) AS trips
FROM trades
WHERE action = 'BUY' AND mode = 'paper'
  AND EXISTS (SELECT 1 FROM trades s WHERE s.ticker = trades.ticker
              AND s.action = 'SELL' AND s.timestamp > trades.timestamp)
GROUP BY ticker;
```

For Phase 3b, the exit model is trained per ticker (one model for AAPL, one for MSFT,
etc.). Ensure at least 50 trips per ticker before training that ticker's model.
Cross-ticker transfer is not supported in the current ExitModel implementation.

---

## Section 5 — Minimum Viable Dataset Assessment: Go/No-Go Summary

Before pulling the trigger on Phase 3b training, fill in this table:

| Criterion | Threshold | Actual Value | Pass/Fail |
|-----------|-----------|-------------|-----------|
| AAPL completed round trips | >= 50 | ___ | ___ |
| Fill price null count | 0 | ___ | ___ |
| Fill deviation > $0.01 rate | < 5% | ___ | ___ |
| Positive label rate | 0.05–0.95 | ___ | ___ |
| Avg bars per trade | >= 4 | ___ | ___ |
| Distinct HMM regimes in data | >= 2 | ___ | ___ |
| Date span | >= 1 month | ___ | ___ |

**Decision**: ALL criteria Pass → proceed to EXIT_MODEL_IMPLEMENTATION_ROADMAP.md Stage A.
Any Fail → hold; address root cause and re-assess at next 20:00 UTC checkpoint.

---

## Section 6 — Success Criteria Thresholds

These thresholds gate promotion from backtest validation to live deployment.
See EXIT_MODEL_BACKTEST_EXECUTION_RUNBOOK.md for measurement procedures.

| Metric | Minimum (Stage A) | Target (Stage B/C) | Notes |
|--------|-------------------|--------------------|-------|
| Exit win rate (voluntary exits profitable) | > 45% | > 55% | Voluntary exits only, not time-stops |
| Average hold time | 3–30 min | 5–25 min | Below 3 min = noise; above 30 min = approaching h+10 |
| Realistic slippage | < 0.02% per trade | < 0.015% | Paper account fill quality baseline |
| Voluntary exit rate | > 50% of trades | > 65% | If < 50%, threshold probably too high |
| ΔPnL (exit model vs. baseline) | > 0 with p < 0.10 | > 0 with p < 0.05 | Paired t-test on holdout set |

**Slippage note**: 0.02% of a $50K AAPL position = $10/trade. Current paper fills are
showing ±$0.01 deviation on $180–$230 stocks, implying ~0.005% slippage — well within
threshold. Revalidate on first 10 live sessions after exit model activation.
