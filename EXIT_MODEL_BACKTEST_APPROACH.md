# Exit Model Backtest & Training Approach

This document describes how to train, validate, and deploy the separate
exit model implemented in `src/models/exit_model.py` and
`src/models/exit_signal_generator.py`.

## Context

The entry stacker (LightGBM ensemble) was trained to predict forward
returns and consistently produces near-zero SELL confidence in live
trading. Every exit since Lever A has been a forced h+10 time-stop.

The separate exit model is a binary classifier trained specifically on
the question *"given I'm in a position, should I exit now?"* — using
historical round trips as supervised examples.

## Training data flow

```
sqlite database  --(query)-->  list of round trips  --(helper)-->  (X, y)  --(fit)-->  ExitModel  --(save)-->  ./models/exit_<ticker>.pkl
```

### 1. Extract completed round trips from the database

Each round trip is a BUY paired with the next SELL on the same ticker /
strategy / mode. The schema lives in `src/database/schema.py`:

```python
from src.database.schema import Trade, TradeAction
from src.database.db_manager import DatabaseManager

def extract_round_trips(ticker, strategy_name, mode):
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
                continue  # still open
            round_trips.append({
                "ticker": buy.ticker,
                "entry_time": buy.timestamp,
                "entry_price": float(buy.fill_price or buy.price),
                "exit_time": sell.timestamp,
                "exit_price": float(sell.fill_price or sell.price),
            })
    return round_trips
```

### 2. Fetch the OHLCV history for each ticker

Use the Alpaca provider (mandatory per the Data Source Policy memory):

```python
from src.data.alpaca_provider import get_shared_provider

provider = get_shared_provider()
bars_by_ticker = {}
for ticker in {rt["ticker"] for rt in round_trips}:
    # Cover at least 30 days BEFORE the earliest entry so we have enough
    # history for the 21-bar feature window and 14-bar ADX/RSI.
    bars_by_ticker[ticker] = provider.get_bars(ticker, start=..., end=...)
```

### 3. Build (X, y) and train

```python
from src.models.exit_model import (
    ExitModel,
    prepare_training_data_from_trades,
)

X, y, meta = prepare_training_data_from_trades(
    round_trips=round_trips,
    bars_by_ticker=bars_by_ticker,
    h10_horizon=10,
)
print(meta)
# {'n_trades': 87, 'n_samples': 612, 'positive_rate': 0.41, 'warnings': []}

model = ExitModel(name=f"exit_{ticker}", backend="gradient_boosting")
results = model.fit(X, y)
model.save(f"/var/stockbot/models/exit_{ticker}")
```

## Minimum training-data requirements

| Metric | Minimum | Recommended |
| --- | --- | --- |
| Round trips per ticker | 50 | 100+ |
| Bars per round trip (avg) | 4 | 8+ |
| Positive label rate | 0.10 | 0.20 - 0.50 |
| Date span | 6 months | 12 months+ |

The 50-trade minimum is set by the variance of the label distribution:
fewer than ~50 trades produces fewer than ~200 labelled bars after
accounting for the 21-bar warmup, which is too sparse for a 200-tree
gradient booster to generalise beyond the training set.

`prepare_training_data_from_trades` logs the positive-rate; if it is
below 0.05 or above 0.95 the model will be effectively constant and
should NOT be deployed. Re-train when more diverse round trips become
available.

## Validation methodology

### Holdout split

Split round trips chronologically (NOT random) into 70% train / 30%
test by `entry_time`. Pass only the train split to
`prepare_training_data_from_trades`; build a separate `(X_test, y_test)`
from the test split using the same helper.

Then run a **synthetic backtest** with the trained exit model:

1. For each test-set round trip, walk the bars between entry and the
   *original* exit and query `model.predict_exit_probability` on each
   bar.
2. The first bar with `P(exit) >= threshold` is the model-driven exit.
3. If no bar crosses the threshold, the original h+10 exit is used
   (this is the backstop behaviour live).

### Key metric

The headline metric is **average net P&L per trade** with the exit
model enabled vs. disabled, on the same set of trades:

```
ΔPnL = mean(pnl_with_exit_model) - mean(pnl_without_exit_model)
```

A positive ΔPnL with `p < 0.05` (paired t-test across trades) is the
minimum bar for promotion to live.

Secondary metrics:

| Metric | Healthy range |
| --- | --- |
| Sharpe (gross, daily) | >= 0.6 |
| Maximum drawdown | <= entry-only baseline + 2 pp |
| Average hold-days | strictly less than 10 (otherwise the model is just learning the time-stop) |
| Voluntary-exit rate | > 50% of trades (otherwise the time-stop still dominates) |

### Sweep the threshold

The default 0.60 threshold is a starting point. Grid-search
`{0.50, 0.55, 0.60, 0.65, 0.70, 0.75}` on the holdout set and pick the
one that maximises ΔPnL **subject to** voluntary-exit rate > 0.50. The
chosen threshold becomes the per-session `exit_model_threshold` in
`active-sessions-*.json`.

## Deployment

Once a model passes validation:

1. Save artefacts to a versioned path:
   `/var/stockbot/models/exit_<ticker>_<YYYYMMDD>.pkl`
   (the matching `.meta.json` is written automatically).

2. Add three keys to the session's `strategy_params`:

   ```json
   "strategy_params": {
     "hmm_regime_masking": true,
     "exit_model_enabled": true,
     "exit_model_threshold": 0.60,
     "exit_model_path": "/var/stockbot/models/exit_AAPL_20260801"
   }
   ```

3. Restart the session. The trading session logs
   `Exit model loaded from <path>` on boot when the model is wired in,
   and per-cycle indicators include `exit_model_probability` and
   `exit_model_threshold`.

4. Monitor the first 10 sessions for `voluntary_exits_today` >= 1 — if
   zero voluntary exits fire over a week, the threshold is probably too
   high; re-run the threshold sweep.

## Re-training cadence

| Trigger | Action |
| --- | --- |
| +25 new round trips since last train | Re-train and validate |
| Strategy parameters change (h horizon, position sizing) | Re-train |
| Sharp regime shift (HMM bear regime sustained 60+ bars) | Re-train |
| Voluntary-exit rate drops below 0.30 over 30 days | Re-train or revert threshold |

## Failure modes & safety

- **Untrained model loaded by mistake**: `ExitModel.predict_exit_probability`
  returns 0.0 unconditionally. The h+10 time-stop still fires. No
  silent regression.
- **Model file missing**: `ExitSignalGenerator.from_config` logs a
  WARNING and constructs a disabled generator. Session continues with
  legacy behaviour.
- **Prediction raises**: caught in `trading_session.py`; the failure is
  logged but the cycle continues. Time-stop still fires.
- **Single-class training set**: `ExitModel.fit` logs a WARNING; the
  predictor returns 0 for the missing class. Effectively neutralises
  the model.
