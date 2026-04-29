# Market Session Monitoring Checklist — April 29, 2026

> Created 2026-04-29 Session 633 for live market validation of 11-ticker ensemble stacker portfolio.
> Use at monitoring checkpoints: 14:00 UTC (1h in), 16:00 UTC (mid-market), 20:15 UTC (post-market close).

---

## Context

**Session Goal**: Validate feature count fix (Session 560) by observing actual trade generation during first live market session since engine restart (Session 622, 03:31 UTC).

**Expected Activity Baseline**: 11-ticker portfolio at 0.17–2 trades/month/ticker = 2–22 aggregate trades/month. Single-day probability: ~10–15% chance of ≥1 signal, ~60% ensemble chance across all 11 tickers.

**Critical Question**: Will engine generate ≥1 trade today? (Validates feature pipeline fix from Session 560)

**Success Criteria** (need ≥3 of 6):
1. ✅ Engine wakes at 13:15 UTC (market-aware sleep logic)
2. ⏳ Sessions begin cycle execution at 13:30 UTC (no shutdown errors)
3. ⏳ Signals generated for ≥1 ticker (validates feature pipeline)
4. ⏳ Alpaca order submissions logged (validates API integration)
5. ⏳ Discord summary posted at 20:00 UTC (validates notification system)
6. ⏳ No 401 auth errors or critical log entries

---

## Checkpoint 1: 14:00 UTC (1 hour into market)

**Timeline**: 13:30–14:00 UTC market open.

### A. Engine Health Check

```bash
# Command: check engine process status
ps aux | grep -E "launch_stacker_sessions|run_live_trading" | grep -v grep
```

**Success Criteria**:
- [ ] Process running (non-zero PID)
- [ ] Memory usage < 15% (normal is 8–10%)
- [ ] No shutdown/crash signals

**Log**: Record PID and memory usage in checkpoint log.

### B. Signal Generation Check

```bash
# Command: check for signal log entries in last 30 minutes
tail -200 projects/stockbot/logs/trading_20260429.log | \
  grep -E "signal|SIGNAL|predicted|prediction|confidence" | \
  head -20
```

**Success Criteria**:
- [ ] ≥1 signal log entry per ticker (11 tickers expected)
- [ ] No ERROR or exception messages in signal section
- [ ] Confidence scores logged (verify feature pipeline producing output)

**Log**: Record number of signals per ticker. Example:
```
AAPL: 3 signal checks, 0 signals (threshold not met)
GOOGL: 3 signal checks, 1 signal (confidence 0.72)
...
```

### C. Alpaca Connection Check

```bash
# Command: verify Alpaca auth + API calls
tail -100 projects/stockbot/logs/trading_20260429.log | \
  grep -iE "alpaca|auth|401|403|order" | \
  head -10
```

**Success Criteria**:
- [ ] No 401 (Unauthorized) or 403 (Forbidden) errors
- [ ] At least 1 "account balance" or "position" API call log
- [ ] No auth exceptions

**Log**: Record any auth-related messages verbatim.

### D. Critical Error Check

```bash
# Command: scan for ERROR/CRITICAL messages
tail -500 projects/stockbot/logs/trading_20260429.log | \
  grep -iE "ERROR|CRITICAL|exception|traceback" | \
  head -10
```

**Success Criteria**:
- [ ] No ERROR messages (INFO, WARNING acceptable)
- [ ] No tracebacks or stack traces
- [ ] If warnings present, note context (e.g., "Warning: insufficient cash" is acceptable during backtest, not during live)

**Log**: If any errors, record full line + timestamp.

### E. Checkpoint Summary

**Metric**: Early signal generation validation

**Pass Criteria**: ≥3 of 4 checks pass
- [ ] Engine running + stable memory
- [ ] Signals logged (≥1 signal per ticker attempting)
- [ ] Alpaca connection clean (no auth errors)
- [ ] No critical errors in logs

**Decision Tree**:
- **PASS**: Proceed to 16:00 checkpoint. Continue monitoring.
- **FAIL (critical errors)**: Investigate in BLOCKED.md. Possible recovery: check live.log for error details, restart if needed.
- **FAIL (no signals)**: Expected at this point (0.17–2/month rate). Continue to 16:00. Re-assess at 20:15.

---

## Checkpoint 2: 16:00 UTC (mid-market, 2.5h into session)

**Timeline**: 13:30–16:00 UTC (2.5 hours of trading).

### A. Order Submission Check

```bash
# Command: look for order submission logs
tail -300 projects/stockbot/logs/trading_20260429.log | \
  grep -iE "submit|place.*order|order.*placed|order.*sent" | \
  head -15
```

**Success Criteria**:
- [ ] ≥1 order submission log (validates API integration)
- [ ] Order details logged (ticker, side BUY/SELL, quantity, price)
- [ ] No "failed" or "error" messages in order submissions

**Log**: Record each order:
```
AAPL: BUY order submitted, qty=10, limit=$273
GOOGL: No orders submitted yet
...
```

### B. Position Table Updates Check

```bash
# Command: verify positions table modifications
tail -200 projects/stockbot/logs/trading_20260429.log | \
  grep -iE "position|INSERT|UPDATE.*positions|trade.*executed" | \
  head -10
```

**Success Criteria**:
- [ ] Position INSERT/UPDATE logs present
- [ ] Trade execution logs (on_trade_executed) logged
- [ ] No database errors (SQLException, constraint violations)

**Log**: Record position updates with timestamp + action.

### C. Performance Metrics Check (optional)

```bash
# Command: check recent cycle metrics
tail -150 projects/stockbot/logs/trading_20260429.log | \
  grep -iE "cycle|iteration|round.*trip|P.L|sharpe" | \
  head -5
```

**Success Criteria**:
- [ ] Cycle metrics calculated
- [ ] No NaN or calculation errors
- [ ] P&L tracking per position

**Log**: Record any performance metrics seen.

### D. Critical Error Check (re-run)

```bash
# Command: double-check for errors in 16:00 window
tail -500 projects/stockbot/logs/trading_20260429.log | \
  grep -iE "ERROR|CRITICAL|exception" | \
  tail -5
```

**Success Criteria**:
- [ ] No new critical errors since 14:00
- [ ] No auth/API errors

**Log**: Record any new errors.

### E. Checkpoint Summary

**Metric**: Order submission + position updates validation

**Pass Criteria**: ≥2 of 3 checks pass
- [ ] ≥1 order submitted to Alpaca
- [ ] Position table updated with trade
- [ ] No critical new errors

**Decision Tree**:
- **PASS**: Excellent. Engine is executing orders. Proceed to 20:15 checkpoint.
- **FAIL (no orders yet)**: Still within baseline probability. Wait for 20:15.
- **FAIL (critical errors)**: Investigate + document in BLOCKED.md.

---

## Checkpoint 3: 20:15 UTC (post-market close, 6.75h since open)

**Timeline**: 13:30–20:00 UTC (full market close at 20:00). Checkpoint runs 15 minutes post-close.

### A. Discord Notification Check

```bash
# Command: verify Discord summary was sent
tail -100 projects/stockbot/logs/trading_20260429.log | \
  grep -iE "discord|webhook|notification|summary|post" | \
  head -10
```

**Success Criteria**:
- [ ] Discord webhook POST logged at ~20:00 UTC
- [ ] Summary contains: signals/ticker, orders, trades, mode, strategy
- [ ] No webhook errors (400, 403, 500)

**Log**: Record Discord post timestamp + content if visible in logs.

### B. Daily Trade Count + P&L

```bash
# Command: extract daily summary
tail -200 projects/stockbot/logs/trading_20260429.log | \
  grep -iE "daily|summary|total.*trade|round.*trip|net.*P.L" | \
  head -15
```

**Success Criteria**:
- [ ] Total trade count logged (BUY + SELL legs counted)
- [ ] Round trip count (complete trades, e.g., BUY→SELL pairs)
- [ ] Daily P&L calculated

**Log**: Record summary metrics:
```
Total trades: 2 (1 BUY + 1 SELL of AAPL)
Round trips: 0 (AAPL BUY still open)
Daily P&L: Floating P&L calculation
```

### C. Per-Ticker Signal Summary

```bash
# Command: extract signal generation per ticker for day
tail -400 projects/stockbot/logs/trading_20260429.log | \
  grep -E "AAPL|GOOGL|NVDA|AMZN|META|JPM|XOM|JNJ|UNH|TSLA" | \
  grep -iE "signal|prediction|confidence" | \
  awk '{print $1, $3}' | sort | uniq -c
```

**Success Criteria**:
- [ ] Signal attempts logged for each ticker
- [ ] Confidence scores recorded
- [ ] At least 1 signal generated (validates feature fix)

**Log**: Record signal count per ticker:
```
AAPL: 30 signals attempted, 1 generated (confidence 0.68)
GOOGL: 30 signals attempted, 0 generated
NVDA: 30 signals attempted, 1 generated (confidence 0.52)
...
```

### D. Regime Indicators (if HMM enabled)

```bash
# Command: check HMM regime detection
tail -200 projects/stockbot/logs/trading_20260429.log | \
  grep -iE "regime|hmm|vol.*scalar" | \
  tail -10
```

**Success Criteria**:
- [ ] Regime transitions logged (if enabled)
- [ ] Volatility scalar applied
- [ ] No regime calculation errors

**Log**: Record regime state transitions during day.

### E. Engine Shutdown Check

```bash
# Command: verify engine gracefully shutdown at market close
tail -50 projects/stockbot/logs/trading_20260429.log | \
  grep -iE "market.*close|shutdown|sleeping|sleep" | \
  tail -3
```

**Success Criteria**:
- [ ] Graceful shutdown at 20:00 UTC (market-aware sleep)
- [ ] No forced exit/crash messages
- [ ] Process still running (ready for next market open)

**Log**: Record shutdown sequence.

### F. Final Critical Error Check

```bash
# Command: final scan for errors in full day logs
grep -i "ERROR\|CRITICAL\|exception" projects/stockbot/logs/trading_20260429.log | \
  wc -l
```

**Success Criteria**:
- [ ] ≤ 5 error messages total (some warnings/info misclassified as errors acceptable)
- [ ] No unrecovered exceptions
- [ ] No auth failures

**Log**: Record total error count.

### G. Post-Market Summary

**Metric**: Full day validation

**Pass Criteria**: ≥4 of 5 checks pass
- [ ] Discord notification posted
- [ ] Trade count + P&L logged
- [ ] ≥1 signal generated (validates feature fix from Session 560)
- [ ] No critical errors
- [ ] Graceful shutdown

**Decision Tree**:
- **PASS (≥3 success criteria met)**: Validation successful. Engine ready for May 12 checkpoint. Document findings in WORKLOG.md. Update PROJECTS.md Gate 1 assessment.
- **FAIL (critical errors / no signals)**: Investigate root cause. Document in BLOCKED.md if unrecoverable. May need Session 634 investigation.

---

## Data Logging Format

For each checkpoint, log findings to: `/tmp/stockbot_monitoring_session_633.txt`

```
=== CHECKPOINT 1: 14:00 UTC ===
Engine: Running (PID 1202130, 9% memory)
Signals: AAPL=0, GOOGL=1, NVDA=0, AMZN=0, META=0, JPM=0, XOM=0, JNJ=0, UNH=0, TSLA=0
Alpaca: No auth errors
Critical Errors: 0
Status: PASS (3/4 criteria)

=== CHECKPOINT 2: 16:00 UTC ===
Orders: GOOGL BUY 10 @ $175.50 submitted
Positions: 1 position created/updated
Errors: 0 new
Status: PASS (2/3 criteria)

=== CHECKPOINT 3: 20:15 UTC ===
Discord: Posted at 20:00 UTC
Trades: 1 GOOGL BUY (still open), 0 round trips
Signals: 2 total (GOOGL, NVDA)
Shutdown: Graceful at 20:00 UTC, process running
Status: PASS (4/5 criteria)

RECOMMENDATION: Engine validation successful. Ready for May 12 Gate 1 checkpoint.
```

---

## Post-Monitoring Actions

**After 20:15 UTC checkpoint**:

1. **If PASS**: 
   - Update PROJECTS.md `Current focus` section with today's results
   - Add entry to CHECKIN.md `Since Last Check-in`
   - Continue monitoring through May 12 checkpoint (Gate 1 assessment)

2. **If FAIL (critical errors)**:
   - Write block to BLOCKED.md
   - Investigate root cause (Session 634 if needed)

3. **Always**:
   - Commit monitoring findings to WORKLOG.md
   - Prepare May 1 checkpoint assessment (2-3 market sessions collected)

---

*Created*: 2026-04-29 12:15 UTC — Session 633  
*Purpose*: Structured monitoring for multi-ticker portfolio validation  
*Success Target*: ≥3/6 overall criteria pass → Engine ready for May 12 Gate 1 checkpoint
