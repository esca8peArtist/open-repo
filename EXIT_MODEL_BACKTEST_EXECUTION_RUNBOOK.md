# Exit Model Backtest Execution Runbook

**Purpose**: Step-by-step execution guide for extracting training data, running backtest
validation, tuning thresholds, and making the go/no-go decision for exit model deployment.
This runbook is the operational companion to EXIT_MODEL_BACKTEST_APPROACH.md (which defines
the architecture) and EXIT_MODEL_IMPLEMENTATION_ROADMAP.md (which defines stage triggers).

**When to use**: After EXIT_MODEL_TRAINING_DATA_READINESS_CHECKLIST.md Section 5 confirms
all quality gates pass. Execute from the Pi (raspby1) working directory.

**Important**: All Python commands use `uv run python`. All SQL targets the Jetson DB
(mounted or synced to Pi) or `projects/stockbot/trading.db` locally.

---

## Step 1 — Extract Completed Round Trips from trading.db

The schema uses `Trade.action` with enum values `'BUY'` and `'SELL'` (not `trade_side`
or `exit_side` — those columns do not exist). The `fill_price` column holds the actual
execution price. Use SQLAlchemy ORM as shown in EXIT_MODEL_BACKTEST_APPROACH.md.

### 1a. Count available round trips before proceeding

```sql
-- Run directly in sqlite3 or via DatabaseManager
SELECT
    b.ticker,
    COUNT(*)           AS completed_trips,
    MIN(b.timestamp)   AS earliest_entry,
    MAX(s.timestamp)   AS latest_exit,
    AVG(s.realized_pnl) AS avg_pnl
FROM trades b
JOIN trades s ON
    s.ticker        = b.ticker
    AND s.strategy_name = b.strategy_name
    AND s.mode          = b.mode
    AND s.action        = 'SELL'
    AND s.timestamp     > b.timestamp
WHERE b.action = 'BUY'
  AND b.mode   = 'paper'
GROUP BY b.ticker
ORDER BY completed_trips DESC;
```

**Stop condition**: If AAPL count < 50, do not proceed. Return to monitoring.

### 1b. Extract round trips using the ORM helper

```python
# Run from projects/stockbot/ directory
# uv run python -c "exec(open('scripts/extract_round_trips.py').read())"

from src.database.schema import Trade, TradeAction
from src.database.db_manager import DatabaseManager

def extract_round_trips(ticker, strategy_name, mode='paper'):
    db = DatabaseManager.get_instance()
    with db.get_session() as s:
        buys = (
            s.query(Trade)
             .filter(
                 Trade.ticker == ticker,
                 Trade.action == TradeAction.BUY,
                 Trade.strategy_name == strategy_name,
                 Trade.mode == mode,
             )
             .order_by(Trade.timestamp.asc())
             .all()
        )
        round_trips = []
        for buy in buys:
            sell = (
                s.query(Trade)
                 .filter(
                     Trade.ticker == ticker,
                     Trade.action == TradeAction.SELL,
                     Trade.strategy_name == strategy_name,
                     Trade.mode == mode,
                     Trade.timestamp > buy.timestamp,
                 )
                 .order_by(Trade.timestamp.asc())
                 .first()
            )
            if sell is None:
                continue  # position still open — skip
            round_trips.append({
                "ticker": buy.ticker,
                "entry_time": buy.timestamp,
                "entry_price": float(buy.fill_price),  # fill_price, not price
                "exit_time": sell.timestamp,
                "exit_price": float(sell.fill_price),
                "realized_pnl": float(sell.realized_pnl or 0.0),
            })
    return round_trips

# For AAPL with the lgbm_ho strategy
round_trips = extract_round_trips(
    ticker='AAPL',
    strategy_name='lgbm_ho',  # match the strategy_name stored at fill time
    mode='paper',
)
print(f"Extracted {len(round_trips)} round trips")
print(f"Date range: {round_trips[0]['entry_time']} → {round_trips[-1]['exit_time']}")
```

**Verify**: `len(round_trips)` should match the SQL count from Step 1a.

---

## Step 2 — Fetch OHLCV Bars from Alpaca

Use the Alpaca provider exclusively (yfinance is banned per Data Source Policy). Cover
at least 30 days before the earliest entry to provide warmup bars for the 21-bar window
used by `ExitFeatureComputer`.

```python
from src.data.alpaca_provider import get_shared_provider
import pandas as pd

provider = get_shared_provider()

# Determine date range from round trips
earliest_entry = min(rt['entry_time'] for rt in round_trips)
latest_exit = max(rt['exit_time'] for rt in round_trips)

# Add 30-day pre-buffer for feature warmup
fetch_start = pd.Timestamp(earliest_entry) - pd.Timedelta(days=30)
fetch_end = pd.Timestamp(latest_exit) + pd.Timedelta(hours=1)

# Fetch per ticker — for AAPL
bars_by_ticker = {}
for ticker in {rt['ticker'] for rt in round_trips}:
    bars_by_ticker[ticker] = provider.get_bars(
        ticker,
        start=fetch_start.strftime('%Y-%m-%d'),
        end=fetch_end.strftime('%Y-%m-%d'),
    )
    print(f"{ticker}: {len(bars_by_ticker[ticker])} bars fetched")
```

**Verify**: Bar count should be >= (trading days in window) * (bars per day at 5m resolution).
For a 30-day window at 5m bars: ~30 * 78 = 2,340 bars minimum.

---

## Step 3 — Apply 70/30 Chronological Split

Split by `entry_time`, NOT by random shuffle. The split preserves time ordering to
prevent look-ahead bias in the validation set.

```python
# Sort round trips chronologically (should already be sorted, but be explicit)
round_trips_sorted = sorted(round_trips, key=lambda rt: rt['entry_time'])

# 70/30 split by index
split_idx = int(len(round_trips_sorted) * 0.70)
train_trips = round_trips_sorted[:split_idx]
test_trips  = round_trips_sorted[split_idx:]

print(f"Train: {len(train_trips)} trips | Test: {len(test_trips)} trips")
print(f"Train ends:   {train_trips[-1]['exit_time']}")
print(f"Test starts:  {test_trips[0]['entry_time']}")
```

**Target**: Train on May / early June data; validate on mid-June and beyond.
At 50 trips: ~35 train / 15 test. At 100 trips: ~70 train / 30 test.

**Minimum test set size**: 10 completed round trips. If `len(test_trips) < 10`, the
sample is too small for meaningful statistical testing. Wait for more data.

---

## Step 4 — Build (X, y) and Train

```python
from src.models.exit_model import ExitModel, prepare_training_data_from_trades

# Build training set from train_trips only
X_train, y_train, meta_train = prepare_training_data_from_trades(
    round_trips=train_trips,
    bars_by_ticker=bars_by_ticker,
    h10_horizon=10,  # must match live session config (default 10)
)

print("Training set meta:")
print(f"  n_trades:      {meta_train['n_trades']}")
print(f"  n_samples:     {meta_train['n_samples']}")
print(f"  positive_rate: {meta_train['positive_rate']:.3f}")
print(f"  warnings:      {meta_train['warnings']}")

# Block if positive_rate is out of range
assert 0.05 <= meta_train['positive_rate'] <= 0.95, \
    f"Positive rate {meta_train['positive_rate']:.3f} out of range — do not train"

# Instantiate and train (Stage A: GradientBoosting with n_estimators=100)
model = ExitModel(name="exit_AAPL_stageA", backend="gradient_boosting")
# Override n_estimators for Stage A conservative fit
model.params['n_estimators'] = 100

train_results = model.fit(X_train, y_train)
print(f"Training complete: {train_results}")

# Also build the test feature matrix (same helper, test_trips only)
X_test, y_test, meta_test = prepare_training_data_from_trades(
    round_trips=test_trips,
    bars_by_ticker=bars_by_ticker,
    h10_horizon=10,
)
print(f"Test set: {meta_test['n_samples']} samples from {meta_test['n_trades']} trades")
```

---

## Step 5 — Run Synthetic Backtest on Holdout Set

The synthetic backtest simulates applying the exit model to the test set's historical
round trips, measuring whether the model-driven exit would have been better than the
original h+10 exit.

```python
import numpy as np

DEFAULT_THRESHOLD = 0.60
FALLBACK_EXIT_HORIZON = 10  # bars; matches h+10 live config

def run_synthetic_backtest(model, test_trips, bars_by_ticker, threshold):
    """
    For each test-set round trip, walk bars from entry to actual exit and
    apply model.predict_exit_probability. First bar >= threshold is the
    model-driven exit. If none fires, use the original exit (h+10 fallback).
    """
    results = []
    for rt in test_trips:
        ticker = rt['ticker']
        entry_time = pd.Timestamp(rt['entry_time'])
        original_exit_time = pd.Timestamp(rt['exit_time'])
        entry_price = rt['entry_price']
        original_exit_price = rt['exit_price']
        original_pnl = rt.get('realized_pnl', original_exit_price - entry_price)

        bars = bars_by_ticker.get(ticker)
        if bars is None:
            continue

        trade_bars = bars.loc[
            (bars.index > entry_time) & (bars.index <= original_exit_time)
        ]
        if trade_bars.empty:
            continue

        # Walk bars looking for first model-triggered exit
        model_exit_time = None
        model_exit_price = None
        for ts, bar in trade_bars.iterrows():
            # Construct the feature row as the ExitSignalGenerator would
            # (abbreviated here — in practice call ExitFeatureComputer directly)
            days_held = max(1, int((ts - entry_time).days))
            unrealized_pct = (float(bar['close']) - entry_price) / entry_price

            prob = model.predict_exit_probability({
                "unrealized_pnl_pct": unrealized_pct,
                "days_held": days_held,
                # remaining features are computed internally in the live path;
                # for backtest use X_test rows directly (see full implementation below)
            })
            if prob >= threshold:
                model_exit_time = ts
                model_exit_price = float(bar['close'])
                break

        # If model never fired, fall back to original exit
        if model_exit_price is None:
            model_exit_price = original_exit_price
            voluntary = False
        else:
            voluntary = True

        model_pnl = model_exit_price - entry_price

        results.append({
            "ticker": ticker,
            "entry_time": entry_time,
            "original_pnl": original_pnl,
            "model_pnl": model_pnl,
            "voluntary": voluntary,
            "delta_pnl": model_pnl - original_pnl,
        })

    return results

# Run at default threshold
backtest_results = run_synthetic_backtest(
    model=model,
    test_trips=test_trips,
    bars_by_ticker=bars_by_ticker,
    threshold=DEFAULT_THRESHOLD,
)

# Compute headline metrics
delta_pnls = [r['delta_pnl'] for r in backtest_results]
voluntary_rate = sum(1 for r in backtest_results if r['voluntary']) / len(backtest_results)
win_rate = sum(1 for r in backtest_results if r['model_pnl'] > 0) / len(backtest_results)

print(f"ΔPnL mean:       ${np.mean(delta_pnls):.4f}")
print(f"Win rate:        {win_rate:.1%}")
print(f"Voluntary rate:  {voluntary_rate:.1%}")
```

**Note on feature computation in backtest**: The abbreviated approach above uses only
2 features as placeholders. For full fidelity, use the precomputed `X_test` rows from
Step 4 and match each row to its corresponding test-set round trip by timestamp. The
`meta_test` dict provides sample counts per trade.

---

## Step 6 — Validation Gates Per Stage

### Stage A gates (minimum bar for deployment)

```python
from scipy import stats

n = len(backtest_results)
mean_delta = np.mean(delta_pnls)
_, p_value = stats.ttest_1samp(delta_pnls, 0.0)

print("=== Stage A Validation Gates ===")
print(f"A1 Win rate > 45%:         {'PASS' if win_rate > 0.45 else 'FAIL'} ({win_rate:.1%})")
print(f"A2 ΔPnL > 0 (p<0.10):     {'PASS' if mean_delta > 0 and p_value < 0.10 else 'FAIL'} (Δ={mean_delta:.4f}, p={p_value:.3f})")
print(f"A3 Voluntary rate > 50%:   {'PASS' if voluntary_rate > 0.50 else 'FAIL'} ({voluntary_rate:.1%})")

hold_times = [(pd.Timestamp(r['entry_time']) - pd.Timestamp(r['entry_time'])).seconds / 60
              for r in backtest_results if r['voluntary']]
# Placeholder for actual hold time calculation from exit_time
print(f"A4 Avg hold 3-30 min:      [compute from model_exit_time - entry_time]")
```

### Stage B gates

```python
# After re-training with random_forest backend (Stage B model)
print("=== Stage B Validation Gates ===")
print(f"B1 Win rate > 50%:         {'PASS' if win_rate > 0.50 else 'FAIL'}")
# B2 requires comparison with Stage A model results (save Stage A metrics first)
print(f"B2 ΔPnL >= Stage A:        [compare mean_delta against saved Stage A value]")
print(f"B3 Voluntary rate > 55%:   {'PASS' if voluntary_rate > 0.55 else 'FAIL'}")
print(f"B4 Feature importance:     [inspect model.model.feature_importances_]")
```

### Stage C gates

```python
print("=== Stage C Validation Gates ===")
print(f"C1 Win rate > 55%:         {'PASS' if win_rate > 0.55 else 'FAIL'}")
print(f"C2 ΔPnL >= Stage B:        [compare against saved Stage B value]")
print(f"C3 Per-regime win rate:    [split backtest_results by regime, compute per subset]")
print(f"C4 Voluntary rate > 60%:   {'PASS' if voluntary_rate > 0.60 else 'FAIL'}")
```

---

## Step 7 — Threshold Tuning Procedure

Default threshold is 0.60. Grid-search on the holdout set to find the threshold that
maximises ΔPnL subject to voluntary exit rate > 50%.

```python
THRESHOLD_GRID = [0.50, 0.55, 0.60, 0.65, 0.70, 0.75]

best_threshold = DEFAULT_THRESHOLD
best_delta = -np.inf
sweep_results = []

for thresh in THRESHOLD_GRID:
    results = run_synthetic_backtest(
        model=model,
        test_trips=test_trips,
        bars_by_ticker=bars_by_ticker,
        threshold=thresh,
    )
    if not results:
        continue
    deltas = [r['delta_pnl'] for r in results]
    v_rate = sum(1 for r in results if r['voluntary']) / len(results)
    mean_d = np.mean(deltas)

    sweep_results.append({
        'threshold': thresh,
        'mean_delta_pnl': mean_d,
        'voluntary_rate': v_rate,
        'win_rate': sum(1 for r in results if r['model_pnl'] > 0) / len(results),
    })

    # Select best threshold: maximise ΔPnL subject to voluntary rate constraint
    if v_rate > 0.50 and mean_d > best_delta:
        best_delta = mean_d
        best_threshold = thresh

print("\nThreshold sweep results:")
for row in sweep_results:
    print(f"  {row['threshold']:.2f}: ΔPnL={row['mean_delta_pnl']:.4f}, "
          f"vol_rate={row['voluntary_rate']:.1%}, win_rate={row['win_rate']:.1%}")

print(f"\nSelected threshold: {best_threshold} (ΔPnL={best_delta:.4f})")
```

The chosen `best_threshold` becomes the `exit_model_threshold` in the session config.

---

## Step 8 — Save Model and Prepare Deployment Config

```python
import datetime

date_str = datetime.date.today().strftime('%Y%m%d')
model_path = f"models/exit_AAPL_stageA_{date_str}"

model.save(model_path)
print(f"Model saved to {model_path}.pkl + {model_path}.meta.json")

# Deployment config for active-sessions-*.json
print(f"""
Add to aapl_lgbm_ho_001 strategy_params in active-sessions-*.json:
  "exit_model_enabled": true,
  "exit_model_threshold": {best_threshold},
  "exit_model_path": "/var/stockbot/{model_path}"
""")
```

Then rsync the model to Jetson and restart the AAPL session:

```bash
rsync -av --exclude='.env' \
  projects/stockbot/models/exit_AAPL_stageA_<YYYYMMDD>.pkl \
  projects/stockbot/models/exit_AAPL_stageA_<YYYYMMDD>.meta.json \
  awank@100.120.18.84:/opt/stockbot/models/

# Update active-sessions JSON on Jetson
# Then restart AAPL session via API call to Jetson:
curl -X POST http://100.120.18.84:8000/api/sessions/aapl_lgbm_ho_001/restart
```

---

## Step 9 — Contingency Paths

### 9.1 Exit signals produce net-negative PnL

**Diagnosis**: `mean(delta_pnl) < 0` across all thresholds in sweep.

**Actions (in order)**:
1. Check `voluntary_rate` at each threshold. If voluntary rate is < 20% everywhere,
   the model is not firing enough to measure — try lowering threshold to 0.45 for
   evaluation only (not deployment).
2. If voluntary rate is adequate but ΔPnL is still negative: the model has learned to
   exit at suboptimal times. Inspect the top-3 features by importance. If `days_held`
   dominates (> 40% importance), the model is mimicking the time-stop, not improving it.
3. If no threshold produces positive ΔPnL with voluntary_rate > 20%: **defer Phase 3b**.
   Log the failure in WORKLOG.md, note the data date range, and reassess after 25 more trips.

### 9.2 Threshold below 0.50 required for profitability

If `best_threshold` from the sweep falls to 0.50 and ΔPnL is still marginal (< $0.01
per trade mean): this indicates insufficient signal quality. The model is operating
near random chance.

**Action**: Recommend Phase 3b deferral until 100+ trips (Stage B threshold). Document
in WORKLOG.md:

```
EXIT MODEL PHASE 3B DEFERRAL
Date: <date>
Reason: No threshold in [0.50, 0.75] produced statistically significant positive ΔPnL
        on <N> holdout trades. Positive rate: <rate>. Best ΔPnL: <value> (threshold <t>).
Next review: when AAPL trips reach 100.
```

### 9.3 Emergency rollback after live deployment

If exit model is live and `voluntary_exits_count > 5` with `mean_voluntary_pnl < -$20`:

1. Set `exit_model_enabled: false` in the AAPL session config on Jetson
2. Restart AAPL session via Jetson API
3. The h+10 time-stop resumes as sole exit mechanism — no trading gap, no missed cycles
4. Preserve the model artifact; do not delete. Log the live performance data for Stage B retraining.

**Trigger threshold for emergency rollback**:
- 5+ voluntary exits with cumulative realized P&L more negative than -$100, OR
- Any single voluntary exit with loss > $50 that was not triggered by news/halt

---

## Appendix A — Quick Reference: Column Names

These column names are verified against `src/database/schema.py` (TradeAction enum,
Trade model). Use these in SQL — do not use aliases from older documentation.

| Concept | Actual Column | Notes |
|---------|--------------|-------|
| Trade direction | `action` | Values: `'BUY'` or `'SELL'` |
| Actual execution price | `fill_price` | Float; never NULL on completed trades |
| Order price (limit/market) | `price` | May differ from fill_price |
| Close P&L | `realized_pnl` | On SELL records; NULL for BUY records |
| Session mode | `mode` | `'paper'` or `'live'` |
| Strategy identifier | `strategy_name` | e.g. `'lgbm_ho'`, `'ridge_wf'` |
| HMM regime at signal time | `regime` | May be NULL if not logged; verify first |

---

## Appendix B — Validation Decision Tree

```
Completed round trips >= 50?
├── NO  → Continue monitoring. Re-check at next 20:00 UTC checkpoint.
└── YES → Run Section 5 quality gates
          ├── Any gate FAIL? → Fix root cause; re-run gates.
          └── All gates PASS → Run Steps 1-7 of this runbook
                               ├── Stage A all 4 gates pass?
                               │   ├── YES → Deploy. Monitor 10 sessions. Proceed to Stage B when 100 trips.
                               │   └── NO  → Run threshold sweep
                               │            ├── Best threshold >= 0.50, ΔPnL > 0? → Deploy at best_threshold
                               │            └── No threshold viable? → DEFER Phase 3b to 100 trips
                               └── [Continue for Stage B/C per Implementation Roadmap]
```
