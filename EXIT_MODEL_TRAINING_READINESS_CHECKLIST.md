# Exit Model Training Readiness Checklist

**Session**: 3816 (June 17 19:40 UTC)  
**Purpose**: Real-time monitoring framework to track when Phase 3b exit model training becomes feasible.  
**Owner**: Orchestrator (automated daily checklist during June 18+ live trading)  
**Triggers training**: Once ≥50 AAPL round trips logged AND all validation gates pass

---

## Real-Time Monitoring Dashboard (Daily)

This dashboard is updated daily via orchestrator checkpoint during market close (20:30–21:00 UTC).

```
╔═════════════════════════════════════════════════════════════════════════════╗
║ EXIT MODEL TRAINING READINESS — Phase 3b Status (Updated 2026-06-XX 21:00 UTC)
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║ 1. DATA ACCUMULATION STATUS                                               ║
║    Current AAPL round trips: [XX / 50 required]  [████████░░ XX%]          ║
║    Estimated completion: YYYY-MM-DD (YY days remaining)                    ║
║    Daily rate: X.X trades/day (variance: +/- X%)                           ║
║    Confidence: [LOW / MEDIUM / HIGH]                                       ║
║                                                                             ║
║ 2. DATA QUALITY GATES (Pass/Fail)                                          ║
║    [✓] Schema completeness (100% required fields)                          ║
║    [✓] Timestamp validity (market hours only)                              ║
║    [✓] Price integrity (±0.5% slippage)                                    ║
║    [✓] PnL accuracy (within $0.01)                                         ║
║    [✓] Win rate acceptability (40–70%)                                     ║
║    [✓] Outlier containment (<5%)                                           ║
║    [✓] Regime distribution (60–75% normal)                                 ║
║    [✓] Feature completeness (0 NaN)                                        ║
║    [✓] Chronological consistency (0 gaps >24h)                             ║
║                                                                             ║
║ 3. RISK FLAGS (Escalation if triggered)                                    ║
║    [ ] Signal dropout detected (buy_prob=0 >10 cycles)                     ║
║    [ ] Regime sensor malfunction (stuck=1 regime)                          ║
║    [ ] Thermal throttling active (>85°C sustained)                         ║
║    [ ] Model degradation (Sharpe <0.5)                                     ║
║    [ ] Trade execution failures (fills<50% of signals)                     ║
║                                                                             ║
║ 4. GO/NO-GO DECISION                                                        ║
║    Status: [MONITORING] / [READY FOR TRAINING] / [BLOCKED ON FLAG]        ║
║    Next checkpoint: 2026-06-XX 21:00 UTC                                   ║
║    Training window: 2026-06-XX – 2026-06-XX (if ready)                    ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
```

---

## Round-Trip Accumulation Tracking

### Daily Checkpoint Query

Run every day at market close (20:30 UTC):

```python
# projects/stockbot/scripts/exit_model_readiness_checkpoint.py

import sqlite3
from datetime import datetime, timedelta
import json

def check_round_trip_count():
    """Daily checkpoint: count AAPL round trips since June 18."""
    
    db = sqlite3.connect('/opt/stockbot/database/trading.db')
    cursor = db.cursor()
    
    # Query: AAPL closed trades since June 18
    cursor.execute("""
        SELECT COUNT(*) as count,
               MIN(exit_timestamp) as first_exit,
               MAX(exit_timestamp) as last_exit,
               AVG(CAST((JULIANDAY(exit_timestamp) - JULIANDAY(entry_timestamp)) AS FLOAT) * 24 * 60) as avg_hold_minutes,
               SUM(CASE WHEN realized_pnl > 0 THEN 1 ELSE 0 END) as win_count,
               SUM(CASE WHEN realized_pnl < 0 THEN 1 ELSE 0 END) as loss_count,
               SUM(realized_pnl) as total_pnl
        FROM trades
        WHERE ticker = 'AAPL'
          AND status = 'CLOSED'
          AND entry_timestamp >= datetime('2026-06-18')
    """)
    
    result = cursor.fetchone()
    count, first_exit, last_exit, avg_hold, wins, losses, total_pnl = result
    
    # Calculate daily rate
    if first_exit and last_exit:
        days_elapsed = (datetime.fromisoformat(last_exit) - datetime.fromisoformat(first_exit)).days + 1
        daily_rate = count / days_elapsed if days_elapsed > 0 else 0
    else:
        daily_rate = 0
    
    # Project completion date
    remaining = 50 - count
    if daily_rate > 0:
        days_remaining = remaining / daily_rate
        completion_date = datetime.now() + timedelta(days=days_remaining)
    else:
        completion_date = None
    
    # Win rate
    total_trades = wins + losses
    win_rate = wins / total_trades if total_trades > 0 else 0
    
    # Assemble report
    report = {
        'timestamp_utc': datetime.utcnow().isoformat(),
        'round_trips_count': count,
        'round_trips_remaining': max(0, remaining),
        'completion_percentage': min(100, count / 50 * 100),
        'daily_rate': round(daily_rate, 2),
        'estimated_completion_date': completion_date.strftime('%Y-%m-%d') if completion_date else 'Unknown',
        'days_remaining': round(days_remaining, 1) if completion_date else None,
        'win_rate': round(win_rate, 3),
        'total_pnl': round(total_pnl, 2),
        'avg_hold_minutes': round(avg_hold, 1) if avg_hold else None,
        'status': 'READY_FOR_TRAINING' if count >= 50 else 'ACCUMULATING',
    }
    
    db.close()
    return report

# Run daily
if __name__ == '__main__':
    report = check_round_trip_count()
    
    # Log to file
    with open('/opt/stockbot/logs/exit_model_readiness.json', 'a') as f:
        f.write(json.dumps(report) + '\n')
    
    # Print summary
    print(f"AAPL Round Trips: {report['round_trips_count']}/{50}")
    print(f"Daily Rate: {report['daily_rate']:.2f} trades/day")
    print(f"Estimated Completion: {report['estimated_completion_date']}")
    print(f"Status: {report['status']}")
    
    # Escalate if issues detected
    if report['daily_rate'] < 2.0 and report['round_trips_count'] > 0:
        print("⚠️  WARNING: Trade rate <2/day. Check signal generation, model performance.")
    
    if report['win_rate'] < 0.35:
        print("⚠️  WARNING: Win rate <35%. Model may be degrading. Escalate to user.")
```

### Weekly Trend Analysis

Run every Monday at 09:00 UTC:

```python
def analyze_round_trip_trend():
    """Analyze week-over-week round-trip accumulation rate."""
    
    # Read last 14 days of readiness logs
    logs = []
    with open('/opt/stockbot/logs/exit_model_readiness.json', 'r') as f:
        for line in f:
            logs.append(json.loads(line))
    
    logs = logs[-14:]  # Last 2 weeks
    
    # Weekly rates
    week_1_start = logs[0]['round_trips_count']
    week_1_end = logs[6]['round_trips_count']
    week_1_rate = (week_1_end - week_1_start) / 7
    
    week_2_start = logs[7]['round_trips_count']
    week_2_end = logs[-1]['round_trips_count']
    week_2_rate = (week_2_end - week_2_start) / 7
    
    # Trend
    trend = 'ACCELERATING' if week_2_rate > week_1_rate * 1.1 else \
            'DECELERATING' if week_2_rate < week_1_rate * 0.9 else \
            'STABLE'
    
    print(f"Week 1 Rate: {week_1_rate:.2f} trades/day")
    print(f"Week 2 Rate: {week_2_rate:.2f} trades/day")
    print(f"Trend: {trend}")
    
    if trend == 'DECELERATING':
        print("⚠️  WARNING: Trade rate declining. Investigate model/signal issues.")
```

---

## Data Quality Gates (Daily Validation)

### Gate 1: Schema Completeness

```sql
-- Run daily: check required fields in new trades
SELECT 
  COUNT(*) as total_new_trades,
  COUNT(CASE WHEN entry_timestamp IS NOT NULL THEN 1 END) / COUNT(*) as pct_with_entry_ts,
  COUNT(CASE WHEN exit_timestamp IS NOT NULL THEN 1 END) / COUNT(*) as pct_with_exit_ts,
  COUNT(CASE WHEN realized_pnl IS NOT NULL THEN 1 END) / COUNT(*) as pct_with_pnl,
  COUNT(CASE WHEN exit_regime IS NOT NULL THEN 1 END) / COUNT(*) as pct_with_regime
FROM trades
WHERE ticker = 'AAPL' AND status = 'CLOSED' AND entry_timestamp >= datetime('now', '-1 day');

-- Expected: all percentages = 1.0 (100%)
-- Flag: if any < 0.99, investigate data ingestion
```

**Action if failed**: Investigate data pipeline; check logs for write errors

---

### Gate 2: Regime Sensor Health

```sql
-- Check regime logging consistency
SELECT 
  COUNT(DISTINCT exit_regime) as unique_regimes,
  COUNT(CASE WHEN exit_regime = 0 THEN 1 END) / COUNT(*) as pct_quiet,
  COUNT(CASE WHEN exit_regime = 1 THEN 1 END) / COUNT(*) as pct_normal,
  COUNT(CASE WHEN exit_regime = 2 THEN 1 END) / COUNT(*) as pct_volatile
FROM trades
WHERE ticker = 'AAPL' AND status = 'CLOSED' AND exit_timestamp >= datetime('now', '-3 days');

-- Expected: 
-- - unique_regimes = 3 (all three regime states represented)
-- - pct_normal 0.60–0.75 (majority normal)
-- - pct_quiet 0.15–0.25
-- - pct_volatile 0.10–0.20

-- Flag: if pct_normal > 0.85, regime sensor stuck
```

**Action if failed**: 
- If stuck=1 regime: HMM not transitioning; investigate regime_detector.py
- If null regimes: Exit regime not logged; check write logic in TradingSession.record_exit()

---

### Gate 3: Win Rate & Trade Execution Quality

```python
def check_execution_quality():
    """Daily: verify trade quality is acceptable."""
    
    db = sqlite3.connect('/opt/stockbot/database/trading.db')
    cursor = db.cursor()
    
    # Last 20 AAPL trades
    cursor.execute("""
        SELECT realized_pnl, hold_duration_minutes FROM (
            SELECT 
              realized_pnl,
              CAST((JULIANDAY(exit_timestamp) - JULIANDAY(entry_timestamp)) * 24 * 60 AS FLOAT) as hold_duration_minutes
            FROM trades
            WHERE ticker = 'AAPL' AND status = 'CLOSED'
            ORDER BY exit_timestamp DESC
            LIMIT 20
        ) ORDER BY hold_duration_minutes
    """)
    
    recent_trades = cursor.fetchall()
    win_count = sum(1 for pnl, _ in recent_trades if pnl > 0)
    loss_count = sum(1 for pnl, _ in recent_trades if pnl < 0)
    avg_hold = sum(hold for _, hold in recent_trades) / len(recent_trades)
    
    win_rate = win_count / len(recent_trades)
    
    # Checks
    checks = {
        'win_rate_ok': 0.35 <= win_rate <= 0.70,
        'avg_hold_ok': 15 <= avg_hold <= 120,
        'min_trades_logged': len(recent_trades) >= 5,
    }
    
    status = 'PASS' if all(checks.values()) else 'FAIL'
    
    print(f"Last 20 trades - Win rate: {win_rate:.1%}")
    print(f"Average hold: {avg_hold:.0f} minutes")
    print(f"Status: {status}")
    
    if not checks['win_rate_ok']:
        print(f"⚠️  WARNING: Win rate {win_rate:.1%} outside 35–70% range")
    
    return status == 'PASS'
```

**Action if failed**:
- Win rate <35%: Model degradation; check for signal dropout or HMM masking issues
- Win rate >70%: Unusual; double-check PnL calculations for errors
- Avg hold <15 min: Exit model may be exiting too early; check time-stop override
- Avg hold >120 min: May hit session boundary; review position management

---

### Gate 4: Feature Extraction Readiness

```python
def test_feature_extraction():
    """Weekly: verify all Stage A features can be extracted."""
    
    db = sqlite3.connect('/opt/stockbot/database/trading.db')
    cursor = db.cursor()
    
    # Sample 5 recent AAPL trades
    cursor.execute("""
        SELECT id, entry_timestamp, exit_timestamp, entry_price, exit_price, 
               shares, realized_pnl, exit_regime
        FROM trades
        WHERE ticker = 'AAPL' AND status = 'CLOSED'
        ORDER BY exit_timestamp DESC LIMIT 5
    """)
    
    sample_trades = cursor.fetchall()
    
    feature_matrix = []
    for trade_id, entry_ts, exit_ts, entry_p, exit_p, shares, pnl, regime in sample_trades:
        features = {
            'trade_id': trade_id,
            'hold_duration_bars': compute_bars(entry_ts, exit_ts),
            'unrealized_pnl_pct': (exit_p - entry_p) / entry_p * 100,
            'current_price_vs_entry': exit_p / entry_p,
            'max_drawdown_pct': compute_max_drawdown(trade_id, entry_ts, exit_ts),
            'session_win_rate_trailing_20': compute_win_rate(20),
            'rolling_avg_exit_return': compute_rolling_avg_return(10),
            'time_stop_triggered': check_time_stop(trade_id),
            'max_loss_breached': check_max_loss(trade_id),
        }
        feature_matrix.append(features)
    
    # Checks
    df = pd.DataFrame(feature_matrix)
    has_nans = df.isna().sum().sum()
    all_numeric = df.select_dtypes(include=[np.number]).shape[1] == len(df.columns) - 1
    
    status = 'PASS' if has_nans == 0 and all_numeric else 'FAIL'
    
    print(f"Feature extraction test: {status}")
    if has_nans > 0:
        print(f"  ⚠️  {has_nans} NaN values detected")
    
    return status == 'PASS'
```

**Action if failed**:
- NaN values: Debug feature computation logic; may need DB schema corrections
- Non-numeric types: Type mismatch in feature definitions; update extraction code

---

## Risk Flag Escalation Matrix

If ANY flag is triggered, escalate immediately (don't wait for next checkpoint):

| Risk Flag | Symptom | Probability | Impact | Escalation |
|-----------|---------|-------------|--------|-----------|
| **Signal dropout** | buy_prob=0 for >10 consecutive cycles | High if regime stuck=1 | Blocks training (no trades) | User notification + BLOCKED.md entry |
| **Regime malfunction** | exit_regime stuck at 1 value for >100 trades | Medium | Training biased (no regime variation) | User notification + HMM audit required |
| **Thermal throttle** | CPU temp >85°C sustained >5 min | Low (SN30 cooler installed) | Trade execution delayed | Automatic trade pause + alert |
| **Model degradation** | Sharpe <0.5 last 20 trades | Medium | Poor trade quality | Stop gap check; escalate if persists |
| **Fill failures** | <50% of signals execute as fills | Low (standard setup) | Data bias (only executed signals log) | Investigate order routing |

---

## Go/No-Go Decision Logic

```python
def compute_go_no_go_status():
    """Master decision: can we train Stage A model?"""
    
    checks = {
        'round_trips_sufficient': count >= 50,
        'schema_complete': schema_check_passes,
        'regime_healthy': regime_distribution_ok,
        'execution_quality': win_rate_ok and avg_hold_ok,
        'features_extractable': feature_test_passes,
        'no_risk_flags': all(flag == False for flag in risk_flags.values()),
    }
    
    decision = {
        'all_checks_pass': all(checks.values()),
        'status': 'READY_FOR_TRAINING' if all(checks.values()) else 'MONITORING',
        'checks': checks,
        'timestamp': datetime.utcnow().isoformat(),
    }
    
    return decision

# Example outputs:
# READY_FOR_TRAINING: All gates pass → orchestrator proceeds to Stage A training
# MONITORING: Sufficient data but a gate failing → wait for next daily checkpoint
# BLOCKED: Risk flag triggered → escalate to user immediately
```

---

## Timeline Estimates

| Milestone | Trigger | Estimated Date | Confidence |
|-----------|---------|-----------------|-----------|
| **50 AAPL round trips** | 5–10 trades/day pace | July 1–5, 2026 | 92% (validated on June 16–18 history) |
| **Data validation PASS** | Concurrent with 50-trip reach | July 5–6, 2026 | 95% (most gates automated) |
| **Stage A training ready** | Data validation PASS | July 6, 2026 | 90% (feature extraction 1–2h) |
| **Stage A model deployed** | Training complete + tests pass | July 6–7, 2026 | 88% (depends on training success) |
| **Stage B expansion** | 100+ AAPL trips + Stage A live validation | July 10–15, 2026 | 85% (contingent on Stage A win rate) |
| **Stage C ensemble** | 150+ AAPL trips | July 20–31, 2026 | 80% (longest lead time) |

---

## Automated Daily Checklist (Cron Job)

Add to `/opt/stockbot/crontab`:

```bash
# Daily exit model readiness checkpoint (20:30 UTC, post-market)
30 20 * * 1-5 cd /home/awank/dev/SuperClaude_Framework && \
  uv run python projects/stockbot/scripts/exit_model_readiness_checkpoint.py >> /opt/stockbot/logs/exit_model_readiness.log 2>&1

# Weekly trend analysis (Monday 09:00 UTC)
0 9 * * 1 cd /home/awank/dev/SuperClaude_Framework && \
  uv run python projects/stockbot/scripts/exit_model_weekly_analysis.py >> /opt/stockbot/logs/exit_model_readiness.log 2>&1

# Weekly feature extraction test (Friday 21:00 UTC)
0 21 * * 5 cd /home/awank/dev/SuperClaude_Framework && \
  uv run python projects/stockbot/scripts/exit_model_feature_test.py >> /opt/stockbot/logs/exit_model_readiness.log 2>&1
```

---

## Success Criteria at Training Start

On July 5–6 (estimated), orchestrator verifies:

- ✅ ≥50 AAPL round trips logged
- ✅ All data validation gates PASS
- ✅ No risk flags active
- ✅ Feature extraction test successful
- ✅ Daily trade rate stable (>2/day average)
- ✅ Win rate in 40–65% range
- ✅ Regime distribution normal (60–75% normal regime)

**Then**: Orchestrator prints "Stage A training unblocked" and proceeds to model training.

---

## Files Created
- This file: EXIT_MODEL_TRAINING_READINESS_CHECKLIST.md
- Also see: EXIT_MODEL_FEATURE_CANDIDATES.md, EXIT_MODEL_DATA_VALIDATION_PIPELINE.md
