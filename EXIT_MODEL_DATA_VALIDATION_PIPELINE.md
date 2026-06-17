# Exit Model Data Validation Pipeline

**Session**: 3816 (June 17 19:35 UTC)  
**Purpose**: Validation checklist and procedures to ensure data quality before Phase 3b training.  
**Gate responsibility**: Orchestrator validates before Stage A training (once 50 AAPL round trips accumulated, ~July 5).  

---

## Pre-Training Validation Checklist

### 1. Data Completeness & Schema Validation

**Objective**: Confirm all required fields are present and correctly formatted.

#### 1.1 Trade Record Structure
```sql
-- Verify schema: all required columns present in trades table
SELECT 
  COUNT(*) as total_trades,
  COUNT(DISTINCT ticker) as unique_tickers,
  COUNT(CASE WHEN entry_timestamp IS NOT NULL THEN 1 END) as with_entry_ts,
  COUNT(CASE WHEN exit_timestamp IS NOT NULL THEN 1 END) as with_exit_ts,
  COUNT(CASE WHEN realized_pnl IS NOT NULL THEN 1 END) as with_pnl,
  COUNT(CASE WHEN shares IS NOT NULL THEN 1 END) as with_shares
FROM trades
WHERE ticker = 'AAPL'
  AND entry_timestamp >= date('2026-06-18')
  AND status = 'CLOSED';

-- Expected: All counts should equal total_trades for closed AAPL trades post-June-18
```

**Pass Criteria**: 
- ✅ COUNT(*) >= 50 (minimum dataset for Stage A)
- ✅ COUNT with_entry_ts == COUNT(*) (no null entry timestamps)
- ✅ COUNT with_exit_ts == COUNT(*) (no null exit timestamps)
- ✅ COUNT with_pnl == COUNT(*) (all trades have realized_pnl)
- ✅ COUNT with_shares > 0 for all rows (no zero-share trades)

---

#### 1.2 HMM Regime Logging
```sql
-- Verify regime labels logged at exits
SELECT 
  COUNT(DISTINCT session_id) as unique_sessions,
  COUNT(CASE WHEN exit_regime IS NOT NULL THEN 1 END) as exits_with_regime,
  COUNT(CASE WHEN exit_regime IS NULL THEN 1 END) as exits_without_regime
FROM trades
WHERE ticker = 'AAPL'
  AND entry_timestamp >= date('2026-06-18')
  AND status = 'CLOSED';

-- Check regime value distribution
SELECT exit_regime, COUNT(*) as count
FROM trades
WHERE ticker = 'AAPL' AND status = 'CLOSED'
GROUP BY exit_regime;

-- Expected: 
-- - exits_with_regime == total exits (100% coverage)
-- - exit_regime IN (0, 1, 2) only (quiet, normal, volatile)
```

**Pass Criteria**:
- ✅ All exits have regime labels (exits_without_regime == 0)
- ✅ Regime values are in valid set {0, 1, 2}
- ✅ Regime distribution is non-trivial (not all same regime)

---

### 2. Timestamp & Duration Validation

**Objective**: Confirm entries/exits occur during market hours and durations are realistic.

#### 2.1 Market Hours Check
```python
# Market hours: 13:30–20:00 UTC (09:30–16:00 ET)
MARKET_OPEN = 13 * 60 + 30  # minutes since midnight UTC
MARKET_CLOSE = 20 * 0  # 20:00 UTC end

def validate_market_hours(entry_time_utc, exit_time_utc):
    """
    Check entries and exits occur during market hours.
    Allow 5-min pre-market window (13:25–13:30).
    """
    entry_minutes = entry_time_utc.hour * 60 + entry_time_utc.minute
    exit_minutes = exit_time_utc.hour * 60 + exit_time_utc.minute
    
    entry_ok = (MARKET_OPEN - 5) <= entry_minutes <= (20 * 60)
    exit_ok = MARKET_OPEN <= exit_minutes <= (20 * 60)
    
    assert entry_ok, f"Entry {entry_time_utc} outside market hours"
    assert exit_ok, f"Exit {exit_time_utc} outside market hours"
    
    return True
```

**SQL Validation**:
```sql
-- Find entries/exits outside market hours
SELECT 
  id, entry_timestamp, exit_timestamp,
  STRFTIME('%H:%M', entry_timestamp) as entry_time,
  STRFTIME('%H:%M', exit_timestamp) as exit_time
FROM trades
WHERE (CAST(STRFTIME('%H', entry_timestamp) AS INTEGER) < 13 
       OR (CAST(STRFTIME('%H', entry_timestamp) AS INTEGER) == 13 
           AND CAST(STRFTIME('%M', entry_timestamp) AS INTEGER) < 25))
  OR CAST(STRFTIME('%H', exit_timestamp) AS INTEGER) > 20;

-- Expected: empty result (no entries/exits outside 13:25–20:00 UTC)
```

**Pass Criteria**:
- ✅ 0 entries before 13:25 UTC
- ✅ 0 exits after 20:00 UTC
- ✅ All entries/exits occur on valid trading days (Mon–Fri, not FOMC/holiday)

---

#### 2.2 Hold Duration Realism
```python
def validate_hold_durations(trades_df):
    """
    Check hold durations are realistic:
    - Min: 5 minutes (algorithmic minimum)
    - Max: 6.5 hours per session (market open boundary)
    - Median: 30–90 minutes (typical intraday trade)
    """
    trades_df['hold_duration_minutes'] = \
        (trades_df['exit_timestamp'] - trades_df['entry_timestamp']).dt.total_seconds() / 60
    
    min_hold = trades_df['hold_duration_minutes'].min()
    max_hold = trades_df['hold_duration_minutes'].max()
    median_hold = trades_df['hold_duration_minutes'].median()
    
    assert min_hold >= 5, f"Min hold {min_hold} min < 5 min threshold"
    assert max_hold <= 6.5 * 60, f"Max hold {max_hold} min > 6.5h session boundary"
    assert 30 <= median_hold <= 120, f"Median hold {median_hold} min outside expected 30–120m"
    
    return {
        'min_hold': min_hold,
        'max_hold': max_hold,
        'median_hold': median_hold,
        'p25_hold': trades_df['hold_duration_minutes'].quantile(0.25),
        'p75_hold': trades_df['hold_duration_minutes'].quantile(0.75),
    }
```

**Pass Criteria**:
- ✅ Min hold ≥ 5 minutes
- ✅ Max hold ≤ 6.5 hours (session boundary, no overnight positions)
- ✅ Median hold 30–120 minutes (typical intraday pattern)
- ✅ Interquartile range (p25–p75) 15–90 minutes (reasonable variance)

---

### 3. Price & PnL Data Integrity

**Objective**: Confirm prices match execution records and PnL calculations are correct.

#### 3.1 Price Consistency
```python
def validate_price_data(trades_df, quote_cache):
    """
    Cross-check entry/exit prices against historical quotes.
    Allows ±0.5% slippage from market price (normal for orders).
    """
    for idx, trade in trades_df.iterrows():
        # Get market quote at entry timestamp
        entry_quote = quote_cache.get(
            ticker=trade['ticker'],
            timestamp=trade['entry_timestamp']
        )
        exit_quote = quote_cache.get(
            ticker=trade['ticker'],
            timestamp=trade['exit_timestamp']
        )
        
        # Entry price should be close to market (within 0.5%)
        if entry_quote:
            entry_slippage = abs(trade['entry_price'] - entry_quote['mid']) / entry_quote['mid']
            assert entry_slippage <= 0.005, \
                f"Entry slippage {entry_slippage:.2%} exceeds 0.5%"
        
        # Exit price should be close to market (within 1%, account for holding time)
        if exit_quote:
            exit_slippage = abs(trade['exit_price'] - exit_quote['mid']) / exit_quote['mid']
            assert exit_slippage <= 0.01, \
                f"Exit slippage {exit_slippage:.2%} exceeds 1%"
    
    return True
```

**Pass Criteria**:
- ✅ Entry price ±0.5% of market bid/ask midpoint at entry time
- ✅ Exit price ±1% of market bid/ask midpoint at exit time (allows holding-time drift)
- ✅ No negative prices or zero prices

---

#### 3.2 PnL Calculation Correctness
```python
def validate_pnl_calculations(trades_df):
    """
    Verify realized_pnl = (exit_price - entry_price) * shares
    """
    trades_df['calculated_pnl'] = \
        (trades_df['exit_price'] - trades_df['entry_price']) * trades_df['shares']
    
    trades_df['pnl_error'] = \
        abs(trades_df['realized_pnl'] - trades_df['calculated_pnl'])
    
    # Allow $0.01 rounding error per trade
    max_acceptable_error = 0.01
    
    assert (trades_df['pnl_error'] <= max_acceptable_error).all(), \
        f"PnL errors exceed ${max_acceptable_error}: \n{trades_df[trades_df['pnl_error'] > max_acceptable_error]}"
    
    return {
        'total_pnl': trades_df['realized_pnl'].sum(),
        'mean_pnl_per_trade': trades_df['realized_pnl'].mean(),
        'std_pnl_per_trade': trades_df['realized_pnl'].std(),
        'win_rate': (trades_df['realized_pnl'] > 0).sum() / len(trades_df),
        'profit_factor': trades_df[trades_df['realized_pnl'] > 0]['realized_pnl'].sum() / \
                        -trades_df[trades_df['realized_pnl'] < 0]['realized_pnl'].sum(),
    }
```

**Pass Criteria**:
- ✅ All PnL calculations match within $0.01 rounding
- ✅ Total PnL > $0 (positive expectancy, at minimum)
- ✅ Win rate 40–70% (confirms trades are real, not trivial)
- ✅ Profit factor (winning $ / losing $) > 1.0

---

### 4. Outlier & Anomaly Detection

**Objective**: Identify trades with unusual characteristics for manual review.

#### 4.1 Single-Trade Outliers
```python
def detect_outliers(trades_df):
    """
    Flag trades with extreme PnL, durations, or prices.
    Thresholds: ±5x median or beyond 3-sigma.
    """
    outliers = []
    
    # PnL outliers
    median_pnl = trades_df['realized_pnl'].median()
    pnl_iqr = trades_df['realized_pnl'].quantile(0.75) - trades_df['realized_pnl'].quantile(0.25)
    extreme_pnl = trades_df[
        (trades_df['realized_pnl'] > median_pnl + 5 * pnl_iqr) |
        (trades_df['realized_pnl'] < median_pnl - 5 * pnl_iqr)
    ]
    if len(extreme_pnl) > 0:
        outliers.append(('extreme_pnl', extreme_pnl))
    
    # Duration outliers (hold time beyond 4 sigma)
    trades_df['hold_minutes'] = (trades_df['exit_timestamp'] - trades_df['entry_timestamp']).dt.total_seconds() / 60
    hold_mean = trades_df['hold_minutes'].mean()
    hold_std = trades_df['hold_minutes'].std()
    extreme_hold = trades_df[
        (trades_df['hold_minutes'] > hold_mean + 4 * hold_std) |
        (trades_df['hold_minutes'] < hold_mean - 4 * hold_std)
    ]
    if len(extreme_hold) > 0:
        outliers.append(('extreme_hold_duration', extreme_hold))
    
    # Price outliers (entry/exit >5% off median)
    entry_median = trades_df['entry_price'].median()
    extreme_entry = trades_df[
        abs(trades_df['entry_price'] - entry_median) > 0.05 * entry_median
    ]
    if len(extreme_entry) > 0:
        outliers.append(('extreme_entry_price', extreme_entry))
    
    return outliers
```

**Action**: Review flagged trades for data integrity issues. If outliers are legitimate (e.g., post-news spike), keep; if corrupted, exclude from Stage A training.

**Pass Criteria**:
- ✅ ≤5% of trades flagged as outliers (allows some legitimate extremes)
- ✅ Outliers are documented and explainable (market shock, news event, etc.)

---

#### 4.2 Regime-Conditional Validation
```python
def validate_regime_distribution(trades_df):
    """
    Confirm regimes are reasonably distributed.
    Expect: Normal regime 60–75%, Quiet 15–25%, Volatile 10–20%
    """
    regime_counts = trades_df['exit_regime'].value_counts(normalize=True)
    
    # Quiet=0, Normal=1, Volatile=2
    expected = {
        0: (0.15, 0.25),  # Quiet: 15–25%
        1: (0.60, 0.75),  # Normal: 60–75%
        2: (0.10, 0.20),  # Volatile: 10–20%
    }
    
    for regime, (min_pct, max_pct) in expected.items():
        actual_pct = regime_counts.get(regime, 0.0)
        assert min_pct <= actual_pct <= max_pct, \
            f"Regime {regime} at {actual_pct:.1%}, expected {min_pct:.1%}–{max_pct:.1%}"
    
    return regime_counts
```

**Pass Criteria**:
- ✅ Normal regime 60–75% of exits
- ✅ Quiet regime 15–25%
- ✅ Volatile regime 10–20%
- ✅ No single regime >85% (indicates possible regime sensor failure)

---

### 5. Feature Extraction & Availability

**Objective**: Confirm all Stage A features can be extracted from database state.

#### 5.1 Feature Extraction Test
```python
def extract_stage_a_features(trades_df, quote_cache):
    """
    Extract all 8 Stage A features for model training.
    Returns DataFrame with features as columns.
    """
    features = []
    
    for idx, trade in trades_df.iterrows():
        feature_row = {
            'trade_id': trade['id'],
            'hold_duration_bars': compute_bars(trade['entry_timestamp'], trade['exit_timestamp']),
            'unrealized_pnl_pct': (trade['exit_price'] - trade['entry_price']) / trade['entry_price'] * 100,
            'current_price_vs_entry': trade['exit_price'] / trade['entry_price'],
            'max_drawdown_pct': compute_max_drawdown_pct(trade, quote_cache),
            'session_win_rate_trailing_20': compute_win_rate_last_20(trade, trades_df),
            'rolling_avg_exit_return': compute_rolling_avg_return(trade, trades_df, window=10),
            'time_stop_triggered': check_time_stop(trade),
            'max_loss_breached': check_max_loss(trade),
        }
        features.append(feature_row)
    
    return pd.DataFrame(features)
```

**Pass Criteria**:
- ✅ All features extractable for 100% of trades
- ✅ No NaN values in feature matrix
- ✅ Feature distributions reasonable (no constant features)

---

### 6. Time-Series Validation

**Objective**: Confirm data is chronologically ordered and has no gaps.

#### 6.1 Chronological Order & Gaps
```python
def validate_chronological_order(trades_df):
    """
    Confirm trades are in time order with no large gaps.
    """
    trades_df_sorted = trades_df.sort_values('exit_timestamp')
    
    # Check monotonicity
    assert (trades_df_sorted['exit_timestamp'].diff().dt.total_seconds() >= 0).all(), \
        "Trades not in chronological order"
    
    # Check for multi-day gaps
    time_gaps = trades_df_sorted['exit_timestamp'].diff().dt.total_seconds() / 3600  # hours
    max_gap = time_gaps.max()
    
    assert max_gap <= 24, \
        f"Large gap detected: {max_gap:.1f} hours (expected max 24h between sessions)"
    
    return {
        'total_trades': len(trades_df),
        'date_range': f"{trades_df['exit_timestamp'].min()} to {trades_df['exit_timestamp'].max()}",
        'max_gap_hours': max_gap,
        'trading_days': len(trades_df['exit_timestamp'].dt.date.unique()),
    }
```

**Pass Criteria**:
- ✅ Trades in chronological order
- ✅ No gaps >24 hours (max gap between sessions)
- ✅ Trading days ~20–23 per month (reasonable for June 18+)

---

## Execution Workflow (Orchestrator)

Once 50 AAPL round trips accumulated (~July 5):

```bash
# Step 1: Load trades data
sqlite3 /opt/stockbot/database/trading.db \
  "SELECT * FROM trades WHERE ticker='AAPL' AND status='CLOSED' AND entry_timestamp >= '2026-06-18' ORDER BY exit_timestamp;" \
  > /tmp/aapl_trades.csv

# Step 2: Run validation pipeline
cd /home/awank/dev/SuperClaude_Framework/projects/stockbot
uv run python -c "
import pandas as pd
import sys
sys.path.insert(0, '/home/awank/dev/SuperClaude_Framework/projects/stockbot/src')

# Load trades
trades = pd.read_csv('/tmp/aapl_trades.csv', parse_dates=['entry_timestamp', 'exit_timestamp'])

# Run validations
print('=== Data Completeness ===')
print(f'Total trades: {len(trades)}')
print(f'With entry_ts: {trades[\"entry_timestamp\"].notna().sum()}')
print(f'With exit_ts: {trades[\"exit_timestamp\"].notna().sum()}')
print(f'With pnl: {trades[\"realized_pnl\"].notna().sum()}')

print('\\n=== Regime Distribution ===')
print(trades['exit_regime'].value_counts(normalize=True))

print('\\n=== Hold Duration ===')
trades['hold_minutes'] = (trades['exit_timestamp'] - trades['entry_timestamp']).dt.total_seconds() / 60
print(f'Min: {trades[\"hold_minutes\"].min():.1f} min')
print(f'Max: {trades[\"hold_minutes\"].max():.1f} min')
print(f'Median: {trades[\"hold_minutes\"].median():.1f} min')

print('\\n=== PnL Statistics ===')
print(f'Total PnL: \${trades[\"realized_pnl\"].sum():.2f}')
print(f'Win rate: {(trades[\"realized_pnl\"] > 0).sum() / len(trades):.1%}')
print(f'Avg trade: \${trades[\"realized_pnl\"].mean():.2f}')
"

# Step 3: If all checks pass, proceed to feature extraction & training
# Step 4: If any check fails, investigate and document issues before proceeding
```

---

## Success Criteria Summary

**ALL** of the following must be true before proceeding to Stage A training:

- ✅ ≥50 AAPL trades in database with status='CLOSED'
- ✅ 100% of trades have entry_timestamp, exit_timestamp, realized_pnl, shares
- ✅ 100% of exits have regime labels (exit_regime IN {0, 1, 2})
- ✅ All entries during 13:25–16:00 ET (US hours, not UTC)
- ✅ All exits during 13:30–20:00 UTC
- ✅ Hold durations 5 min to 6.5 hours (no overnight positions)
- ✅ Median hold 30–120 minutes
- ✅ PnL calculations within $0.01 rounding
- ✅ Win rate 40–70%
- ✅ Outliers ≤5% of trades (documented and explainable)
- ✅ Regime distribution: Normal 60–75%, Quiet 15–25%, Volatile 10–20%
- ✅ All Stage A features extractable (0 NaN)
- ✅ Trades in chronological order
- ✅ No gaps >24 hours between sessions

**If any check FAILS**: Investigate root cause, document issue, and delay training until resolved. Examples:
- Missing regime labels → HMM sensor malfunction; needs diagnostic
- Regime all one value → HMM not transitioning; needs recalibration
- Win rate <40% → Model degradation; requires model audit before proceeding

---

## Files Created
- This file: EXIT_MODEL_DATA_VALIDATION_PIPELINE.md
- (Next): EXIT_MODEL_TRAINING_READINESS_CHECKLIST.md
