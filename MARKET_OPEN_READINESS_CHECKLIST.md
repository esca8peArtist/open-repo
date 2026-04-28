# Market Open Readiness Checklist
**Date**: 2026-04-28  
**Market Open**: 13:30 UTC (8h 14min from 05:15 UTC)  
**Status**: Pre-Market Verification Required

## Engine Restart Requirements
- [ ] **CRITICAL**: Run `.venv/bin/python scripts/run_live_trading.py` from `projects/stockbot/`
- [ ] Engine load: 11-ticker portfolio (AAPL, MSFT, GOOGL, AMZN, NVDA, TSLA, META, NFLX, JNJ, PG, UNH)
- [ ] Monitor: Open AAPL position (36 shares @ $271.04)
- [ ] Verify: Position loaded from database without Mock errors

## Code Readiness Verification (All COMPLETE)
✅ **Feature count bug** (Session 560): Ensemble stacker feature count fixed (61 features with 1d_ prefix)
✅ **Market-aware idle sleep** (Session 552): Skip cycles when market_closed=False; min 60s floor
✅ **Ticker enforcement guard** (Session 552): Verify model ticker matches session ticker (case-insensitive)
✅ **Daily Discord summary** (Session 552): Post-market at 20:00 UTC (once per calendar day, idempotent)
✅ **Discord position notifications** (Session 562): On every trade execution (BUY/SELL, quantity, price, P&L)
✅ **Real-time CRITICAL alerts** (Session 559): 7 alert types with 5-min throttling (circuit breaker, drawdown, position move, prediction error, regime shift, Sharpe drop)

## Environment Variables Required
- `PYTHONPATH=/home/awank/dev/SuperClaude_Framework/projects/stockbot`
- `STOCKBOT_AUTH_ENABLED=false` (paper trading mode)
- `STOCKBOT_DISCORD_WEBHOOK_URL` — position notifications webhook
- `STOCKBOT_DISCORD_ALERT_WEBHOOK_URL` — CRITICAL alerts webhook (optional but recommended)

## Pre-Market Checklist (Execute at 13:15 UTC, 15 min before open)
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/stockbot
.venv/bin/python scripts/run_live_trading.py > /tmp/stockbot_live.log 2>&1 &
```

**Verification** (5 min after start):
1. Tail `/tmp/stockbot_live.log` — look for "Engine initialized" and "Loading positions from database"
2. Check no Mock-related errors in position loading
3. Verify dashboard accessible at `http://localhost:8000/dashboard` (if dashboard enabled)
4. Confirm 11 strategies loaded for 11 tickers
5. Confirm open AAPL position displayed (36 shares @ 271.04)

## Market Open Monitoring (13:30–20:00 UTC)
1. **13:30 UTC**: Market open — expect first cycle execution
2. **14:00 UTC**: Check for multi-ticker signals firing (should see 2-5 initial signals across portfolio)
3. **14:30 UTC**: First potential SELL execution on AAPL (if technical setup aligns with model predictions)
4. **15:00 UTC**: Check Discord notifications firing on trade execution
5. **20:00 UTC**: Verify daily summary Discord message fires post-market
6. **24h Review**: Check P&L, win rate, Sharpe ratio; compare to training metrics

## Post-Market Verification (After 20:00 UTC)
1. Engine still running? (check process)
2. Daily summary message fired? (check Discord channel)
3. All positions closed or held correctly? (check database)
4. No unhandled exceptions in logs?
5. Ready for next trading day?

## Critical Issues to Watch
- **Mock object errors**: Indicates test contamination — restart required
- **Feature shape mismatch**: Indicates ensemble stacker mismatch — restart with clean env
- **HOLD signal on all tickers**: Feature count issue not fully resolved
- **Drawdown >20%**: Triggers CRITICAL alert; circuit breaker at 3 consecutive losses

## Notes
- All code tested and verified in Session 560-562
- Unit tests: 209 passing, 0 regressions
- Integration tests: Monitor first market day for real data edge cases
- Dashboard UI mockup ready for Phase 2 enhancement (Session 551)
- Performance attribution framework ready for post-trade analysis (Session 542)

---
**Prepared by**: Orchestrator Session 563  
**Ready for user execution**: 2026-04-28 13:15 UTC
