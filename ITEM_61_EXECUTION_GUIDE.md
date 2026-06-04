# Item 61: Post-Market Daily Analysis — Execution Guide

**Scheduled Execution Time**: 20:00 UTC (market close) on 2026-06-04

**Status**: Production-ready (Session 2789 verified)

---

## Quick Start

```bash
# Navigate to stockbot directory
cd /home/awank/dev/SuperClaude_Framework/projects/stockbot

# Execute post-market analysis
uv run python scripts/post_market_daily_analysis.py
```

**Expected runtime**: 10-15 seconds (database queries only)

---

## What Item 61 Does

Post-market daily analysis script captures a structured snapshot after market close.

### Analysis Sections (8 total)

1. **Signals** — BUY/SELL signal counts by ticker for today
2. **Fills** — Executed orders (symbol, side, qty, price, time, PnL)
3. **Gate 1 Metrics** — Round trips, Sharpe proxy, MDD%, Calmar ratio (since May 5)
4. **Positions** — Open positions summary (count, ticker, qty, unrealized PnL)
5. **Errors** — Trading log errors/warnings for today
6. **Metrics Computation** — Per-trade PnL analysis, Sharpe calculation, drawdown analysis
7. **Log Output** — JSON record appended to `logs/post_market_daily.jsonl`
8. **Discord Notification** — Optional summary message to Discord webhook (if URL set)

### Current Session Configuration

- **Session 1**: JPM ridge_wf (conservative, all-weather, 88/100 signal quality)
- **Session 2**: AMZN lgbm_ho (momentum + volume, 80/100 signal quality)
- **Mode**: PAPER trading (paper trading validation phase, June 4-30)

---

## Pre-Execution Checklist

- ✅ Database exists: `projects/stockbot/stockbot.db` (verified)
- ✅ Script is executable: `scripts/post_market_daily_analysis.py` (verified)
- ✅ Log directory exists: `projects/stockbot/logs/` (auto-created if missing)
- ✅ Discord webhook optional (set `STOCKBOT_DISCORD_WEBHOOK_URL` env if desired)
- ✅ Python environment ready: `uv run` available (verified)

---

## Expected Output

### Console Output (Human-Readable Report)

```
--- Daily Post-Market Analysis [2026-06-04] ---

--- Signals ---
  BUY signals:  N
  SELL signals: N
  By ticker: {details}

--- Fills ---
  JPM: X fills, avg price $Y, total PnL $Z
  AMZN: A fills, avg price $B, total PnL $C

--- Gate 1 Metrics (since 2026-05-05) ---
  Confirmed round trips: N
  Total P&L: $X.XX
  Win rate: Y%
  Sharpe proxy: Z.ZZ
  Max drawdown: A%
  Calmar ratio: B.BB

--- Open Positions ---
  Active count: N
  Total unrealized: $X.XX
  Position details...

--- Log Health ---
  Errors: N
  Warnings: M
```

### Log File Output

```
logs/post_market_daily.jsonl ← one JSON record appended
```

Example record:
```json
{
  "generated_at": "2026-06-04T20:10:00+00:00",
  "trade_date": "2026-06-04",
  "signals_today": {...},
  "fills_today": [...],
  "gate1_metrics": {...},
  "open_positions": {...},
  "errors_today": {...}
}
```

---

## Post-Execution Decision Framework

After executing Item 61, analyze the Gate 1 metrics:

| Metric | Target | Status |
|--------|--------|--------|
| Round trips | ≥5 confirmed | GO/CAUTION/NO-GO |
| Sharpe proxy | ≥2.0 | GO/CAUTION/NO-GO |
| Win rate | ≥60% | GO/CAUTION/NO-GO |
| Max drawdown | ≤15% | GO/CAUTION/NO-GO |

**Overall Gate 1 Status**:
- **GO**: All metrics pass (proceed with Phase 2 planning)
- **CAUTION**: 2-3 metrics marginal (monitor June 5-6, reassess)
- **NO-GO**: Multiple failures (diagnostic needed, escalate)

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Database not found | Verify `/opt/stockbot/database/` exists on Jetson (Session 2745 fix) |
| Import errors | Run `make dev` to ensure dependencies installed |
| Jetson SSH timeout | Check Jetson at 100.120.18.84 is online (check Docker logs) |
| Discord webhook fails silently | Set `--no-discord` flag to skip and focus on analysis |
| No trades for today | Normal if market closed early; script handles gracefully |

---

## Related Analysis

- **Gate 1 Root Cause Analysis** (Session 2789): Signal infrastructure breakdown diagnosis
- **IEX vs SIP Comparison** (Session 2789): Feed deployment strategy (maintain IEX June, upgrade SIP July)
- **June 2 Market-Open Audit** (Session 2556): JPM ridge_wf 88/100, AMZN lgbm_ho 80/100

---

## Next Steps (Post-Item-61)

1. **Execute Item 61** at 20:00 UTC → analyze Gate 1 metrics
2. **Day 1-2 Monitoring** (June 5-6) → track signal quality, thermal status, fills
3. **Day 7 Checkpoint** (June 11) → reassess trading viability, Gate 1 pass/fail decision
4. **Phase 2 Launch Decision** (June 15+) → based on Gate 1 outcome + Exploration Queue feedback

---

**Session**: 2789 (2026-06-04 17:10–20:00 UTC)  
**Prepared by**: Orchestrator  
**Status**: ✅ Production-ready for 20:00 UTC execution
