# June 24 Validation Outcome Report

**Validation window**: 2026-06-24 13:30–20:00 UTC  
**Sessions**: jpm_ridge_wf_001, amzn_lgbm_ho_001, aapl_lgbm_ho_001, msft_lgbm_ho_001, nvda_lgbm_ho_001  
**Deployment context**: HMM timestamp fix deployed June 22 23:06 UTC (Session 4087), container running with corrected bar timestamp passing  
**Report filled**: 2026-06-24 post-market (20:15 UTC)  

---

## Executive Summary

**Overall verdict**: [**PASS** / **CAUTION** / **NO-GO**]

**Key finding**: [One sentence summary of validation outcome — e.g., "All 5 sessions generated non-HOLD signals by 15:00 UTC; regime initialized Bull/Bear/Sideways across portfolio; 3 trades executed; no regime flips or order errors detected."]

---

## 1. Validation Results Summary

### 1.1 Success Criteria Pass/Fail

| Criterion | Threshold | Result | Status |
|-----------|-----------|--------|--------|
| Signal generation | ≥3 of 5 sessions with ≥1 non-HOLD signal by 20:00 UTC | ___ sessions passed | ☐ PASS / ☐ FAIL |
| Regime initialization | All 5 sessions report regime ≠ None | ___ sessions initialized | ☐ PASS / ☐ FAIL |
| Buy probability restoration | ≥1 session with buy_prob > 0.4 | Max buy_prob: ___ | ☐ PASS / ☐ FAIL |
| Order execution (idempotency) | 0 credential errors, 0 duplicate order IDs | Error count: ___ | ☐ PASS / ☐ FAIL |
| Z-score drift (Day 1) | Day 1 Z between -0.5 and +0.5 (expected ~0.0) | Z-score range: ___ to ___ | ☐ PASS / ☐ FAIL |
| Model alignment | Predicted return signs match action (BUY→+, SELL→−) | Alignment rate: __% | ☐ PASS / ☐ FAIL |
| HMM regime stability | No regime resets (None→Bull→None cycles) | Flips per session: ___ | ☐ PASS / ☐ FAIL |
| WebSocket stability | Zero "Stream not fully initialized" errors after 13:45 UTC | Count: ___ | ☐ PASS / ☐ FAIL |

**Aggregate verdict**: [___ / 8 criteria passed]

---

## 2. Per-Session Signal Health

| Session | Ticker | Model | Signals (BUY/SELL/HOLD) | Regime (final) | buy_prob (final) | Health Score | Verdict |
|---------|--------|-------|----------------------|----------------|-----------------|-------------|---------|
| jpm_ridge_wf_001 | JPM | ridge_wf | ___/___/___ | [Bull/Bear/Sideways/None] | ___ | ___/6 | ☐ PASS / ☐ FAIL |
| amzn_lgbm_ho_001 | AMZN | lgbm_ho | ___/___/___ | [Bull/Bear/Sideways/None] | ___ | ___/6 | ☐ PASS / ☐ FAIL |
| aapl_lgbm_ho_001 | AAPL | lgbm_ho | ___/___/___ | [Bull/Bear/Sideways/None] | ___ | ___/6 | ☐ PASS / ☐ FAIL |
| msft_lgbm_ho_001 | MSFT | lgbm_ho | ___/___/___ | [Bull/Bear/Sideways/None] | ___ | ___/6 | ☐ PASS / ☐ FAIL |
| nvda_lgbm_ho_001 | NVDA | lgbm_ho | ___/___/___ | [Bull/Bear/Sideways/None] | ___ | ___/6 | ☐ PASS / ☐ FAIL |
| **PORTFOLIO** | — | — | ___/___/___ | — | avg: ___ | — | — |

**Health score components** (0–6 scale):
- Regime ≠ None: +1 point
- buy_prob present: +1 point
- buy_prob ≥ threshold: +1 point
- Status = active: +1 point
- ≥1 trade executed: +1 point
- Zero 40010001 errors: +1 point

**Interpretation**:
- Green zone (≥4.0): Session passed all core criteria
- Yellow zone (2.0–3.9): Session functional but with warnings
- Red zone (<2.0): Session failed core functionality

---

## 3. Regime Classification & Stability

| Session | Ticker | Regime at 13:45 UTC | Regime at 20:00 UTC | # Regime Flips | Flip Rate | Status |
|---------|--------|--------------------|--------------------|---------------|-----------|--------|
| jpm_ridge_wf_001 | JPM | [Bull/Bear/Sideways/None] | [Bull/Bear/Sideways/None] | ___ | ___/hr | ☐ OK / ☐ ALERT |
| amzn_lgbm_ho_001 | AMZN | [Bull/Bear/Sideways/None] | [Bull/Bear/Sideways/None] | ___ | ___/hr | ☐ OK / ☐ ALERT |
| aapl_lgbm_ho_001 | AAPL | [Bull/Bear/Sideways/None] | [Bull/Bear/Sideways/None] | ___ | ___/hr | ☐ OK / ☐ ALERT |
| msft_lgbm_ho_001 | MSFT | [Bull/Bear/Sideways/None] | [Bull/Bear/Sideways/None] | ___ | ___/hr | ☐ OK / ☐ ALERT |
| nvda_lgbm_ho_001 | NVDA | [Bull/Bear/Sideways/None] | [Bull/Bear/Sideways/None] | ___ | ___/hr | ☐ OK / ☐ ALERT |

**Regime churn alert threshold**: >4 flips/hour per session = ALERT  
**Expected behavior**: Regime should initialize by 13:45 UTC and remain stable throughout market hours (1–2 flips max as market conditions shift).

---

## 4. Trade Execution & P&L Summary

### 4.1 Trade Execution Log

| Time (UTC) | Session | Ticker | Action | Qty | Fill Price | Entry/Exit | Realized P&L | Status |
|------------|---------|--------|--------|-----|-----------|-----------|------------|--------|
| ___ | ___ | ___ | BUY/SELL | ___ | ___ | Entry | — | ☐ Filled / ☐ Pending |
| ___ | ___ | ___ | SELL | ___ | ___ | Exit | $___ | ☐ Closed / ☐ Open |

**Summary**:
- Total trades executed: ___
- Total round-trips completed: ___
- Winning trades: ___
- Losing trades: ___
- Win rate: ___%

### 4.2 Daily P&L Summary

| Session | Ticker | Realized P&L | Unrealized P&L | Total P&L | Notes |
|---------|--------|-------------|----------------|-----------|-------|
| jpm_ridge_wf_001 | JPM | $___ | $___ | $___ | |
| amzn_lgbm_ho_001 | AMZN | $___ | $___ | $___ | |
| aapl_lgbm_ho_001 | AAPL | $___ | $___ | $___ | |
| msft_lgbm_ho_001 | MSFT | $___ | $___ | $___ | |
| nvda_lgbm_ho_001 | NVDA | $___ | $___ | $___ | |
| **PORTFOLIO** | — | $___ | $___ | $___ | |

**Target**: ~$2,500–$3,500 portfolio daily P&L (conservative estimate, 2-3% of $106K equity)

---

## 5. Z-Score Drift Analysis (Day 1 Baseline)

**Note**: Day 1 Z-scores are baseline establishment only. Statistical significance requires ≥5 trading days. Expected: Z ≈ 0.0 ± 0.5 for first day.

```bash
# Run post-market to extract drift logs:
uv run python /opt/stockbot/scripts/query_drift_logs.py --days 1 --json
```

| Session | Ticker | Z-Score | Band | Status | Notes |
|---------|--------|---------|------|--------|-------|
| jpm_ridge_wf_001 | JPM | ___ | ☐ GREEN (<2.0) / ☐ YELLOW (2.0–3.0) / ☐ RED (>3.0) | ☐ OK / ☐ MONITOR | Day 1 baseline |
| amzn_lgbm_ho_001 | AMZN | ___ | ☐ GREEN / ☐ YELLOW / ☐ RED | ☐ OK / ☐ MONITOR | Day 1 baseline |
| aapl_lgbm_ho_001 | AAPL | ___ | ☐ GREEN / ☐ YELLOW / ☐ RED | ☐ OK / ☐ MONITOR | Day 1 baseline |
| msft_lgbm_ho_001 | MSFT | ___ | ☐ GREEN / ☐ YELLOW / ☐ RED | ☐ OK / ☐ MONITOR | Day 1 baseline |
| nvda_lgbm_ho_001 | NVDA | ___ | ☐ GREEN / ☐ YELLOW / ☐ RED | ☐ OK / ☐ MONITOR | Day 1 baseline |

**Interpretation**:
- **GREEN** (|Z| < 2.0): Session performing within expected range
- **YELLOW** (2.0–3.0): Monitor closely; minor performance drift
- **RED** (>3.0): Auto-pause triggered; assess before resuming

---

## 6. Intraday Drawdown & Risk

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Peak portfolio equity | $___ | — | — |
| Trough portfolio equity | $___ | — | — |
| Max intraday drawdown | __% | <5% OK / 5–8% WARN / >10% HARD STOP | ☐ OK / ☐ WARN / ☐ HARD STOP |
| Largest single-session DD | __% (ticker: ___) | <10% per session | ☐ OK / ☐ ALERT |
| Sessions simultaneously in DD | ___ | 0–1 OK / 2–3 MONITOR / ≥4 ESCALATE | ☐ OK / ☐ MONITOR / ☐ ESCALATE |

---

## 7. Alerts & Anomalies

| Time (UTC) | Alert ID | Type | Severity | Session | Resolved? | Notes |
|------------|----------|------|----------|---------|-----------|-------|
| ___ | [e.g., BUY_PROB_COLLAPSE] | Signal Health | [Critical/Warning/Info] | ___ | ☐ Yes / ☐ No | ___ |

**Total critical alerts fired**: ___  
**Alert resolution status**: ☐ All resolved / ☐ ___ pending investigation

---

## 8. Model Alignment Check

**Question**: Do predicted_return signs align with action (BUY→positive, SELL→negative, HOLD→neutral)?

| Session | Ticker | BUY Alignment | SELL Alignment | HOLD Alignment | Avg Alignment | Status |
|---------|--------|--------------|----------------|----------------|---------------|--------|
| jpm_ridge_wf_001 | JPM | __% | __% | __% | __% | ☐ OK / ☐ OFF |
| amzn_lgbm_ho_001 | AMZN | __% | __% | __% | __% | ☐ OK / ☐ OFF |
| aapl_lgbm_ho_001 | AAPL | __% | __% | __% | __% | ☐ OK / ☐ OFF |
| msft_lgbm_ho_001 | MSFT | __% | __% | __% | __% | ☐ OK / ☐ OFF |
| nvda_lgbm_ho_001 | NVDA | __% | __% | __% | __% | ☐ OK / ☐ OFF |

**Target**: ≥75% alignment across all sessions

---

## 9. Comparison to Baseline Expectations

**Backtest baseline** (from model validation):
- AAPL lgbm_ho: Sharpe 2.230, MaxDD 6.7%, win rate ~58%
- MSFT lgbm_ho: Sharpe 1.573, MaxDD 6.54%, win rate ~52%
- NVDA lgbm_ho: Sharpe 2.926, MaxDD 12.7%, win rate ~61%
- AMZN lgbm_ho: Sharpe 3.939, MaxDD 6.3%, win rate ~65%
- JPM ridge_wf: Sharpe 4.412, MaxDD 2.4%, win rate ~71%

**Live vs Backtest**:

| Session | Ticker | Backtest Sharpe | Live Sharpe (est.) | Delta | Status |
|---------|--------|-----------------|-------------------|-------|--------|
| jpm_ridge_wf_001 | JPM | 4.412 | ___ | ___ | ☐ OK / ☐ DRIFT |
| amzn_lgbm_ho_001 | AMZN | 3.939 | ___ | ___ | ☐ OK / ☐ DRIFT |
| aapl_lgbm_ho_001 | AAPL | 2.230 | ___ | ___ | ☐ OK / ☐ DRIFT |
| msft_lgbm_ho_001 | MSFT | 1.573 | ___ | ___ | ☐ OK / ☐ DRIFT |
| nvda_lgbm_ho_001 | NVDA | 2.926 | ___ | ___ | ☐ OK / ☐ DRIFT |

**Interpretation**: Large negative drift (live < backtest by >0.5) indicates model performance degradation. Investigate feature drift or market regime shift.

---

## 10. Root Cause Analysis (If NO-GO)

**IF verdict = NO-GO**, complete this section:

### 10.1 Symptom

[Describe what failed — e.g., "HMM regime remained None throughout market hours", "WebSocket connection errors", "Order execution blocked"]

### 10.2 Evidence

[List 3–5 specific log lines, database queries, or metrics that confirm the failure]

### 10.3 Likely Root Cause

[One paragraph explaining the probable cause]

### 10.4 Recommended Fix & Timeline

[Outline the code change or infrastructure fix needed, estimated hours, and next validation window date]

---

## 11. Phase 4 Decision & Execution Path

### 11.1 Decision Matrix

| Outcome | Verdict | Phase 4 Path | Timeline |
|---------|---------|-------------|----------|
| **PASS** | ≥3 sessions non-HOLD, regime initialized, ≥1 trade executed | Activate Phase 4 (Path A/B/C) | Immediate (June 24 21:00 UTC) |
| **CAUTION** | 2 sessions non-HOLD, regime OK, but <1 trade OR signal confidence <0.6 | Hold at 5-session expansion; monitor 48–72h; micro-position Tier 2 | June 25–26 decision gate |
| **NO-GO** | <2 sessions passing, regime=None, order errors detected | Disable HMM masking; observe mode 24–48h; diagnostic logging | June 25 contingency session |

### 11.2 Verdict & Recommendation

**Verdict**: [**PASS** / **CAUTION** / **NO-GO**]

**Recommendation**: [Copy from decision matrix row above, customize with specific conditions observed]

### 11.3 Phase 4 Execution Path (If PASS)

**Selected path(s)**: [☐ Path A (Covered Calls) / ☐ Path B (Inverse ETF) / ☐ Path C (Earnings Drift) / ☐ Combination]

**Capital allocation**: 
- Current deployed: 5 sessions × 5% = 25% of $106K equity = $26,500
- Remaining cash buffer: 75% = $79,500
- Phase 4 expansion budget: [______] (specify allocation per path)
- New total deployed (post-Phase 4): __% of account

**Deployment timing** (if PASS):
- Phase 4 code implementation: [Immediate / June 25–26 / June 27+]
- Paper trading window: [Specify dates, typically 5–20 trading days]
- Go-live decision gate: [Specify date, typically 1–2 weeks post-paper-test]

**Risk gating**:
- Order-size cap maintained: 5% per session ✓
- Drawdown monitor: 10% portfolio-level hard stop ✓
- Leverage ceiling: 80% of account equity ✓

---

## 12. Risk Flags & Monitoring Adjustments

| Flag | Trigger | Current Status | Action |
|------|---------|----------------|--------|
| Signal dropout | 0 non-HOLD signals for >30 min | ☐ Active / ☐ Triggered / ☐ Resolved | Monitor logs for "SIGNAL_DROPOUT" |
| Regime churn | >4 regime flips per session per hour | ☐ Active / ☐ Triggered / ☐ Resolved | Check HMM input data (bars) for corruption |
| Drawdown sustained | >10% on any session | ☐ Active / ☐ Triggered / ☐ Resolved | Review market conditions; assess exit strategy |
| Model drift | Live Sharpe < backtest by >0.5 | ☐ Active / ☐ Triggered / ☐ Resolved | Schedule retraining or investigate feature shift |
| WebSocket errors | 406 / 401 / 403 errors after 13:45 UTC | ☐ Active / ☐ Triggered / ☐ Resolved | Check Alpaca API account limits; may need multiplexing |

---

## 13. Next Steps

### If PASS:
1. ☐ Update WORKLOG.md with "Validation PASS" entry
2. ☐ Update PROJECTS.md Current Focus to reflect June 24 PASS outcome
3. ☐ Read PHASE_4_IMMEDIATE_EXECUTION_PLAN.md (select A/B/C path)
4. ☐ Initiate Phase 4 path implementation (target start June 24 21:00 UTC)
5. ☐ Archive this report to `/projects/stockbot/reports/VALIDATION_REPORTS/` for historical record

### If CAUTION:
1. ☐ Update WORKLOG.md with "Validation CAUTION — [specific gaps]" entry
2. ☐ Hold Phase 4 expansion; continue monitoring current 5-session config
3. ☐ Schedule diagnostic session for June 25–26 to investigate gaps
4. ☐ If gap resolves by June 26 18:00 UTC, schedule expedited re-validation for June 27
5. ☐ If gap persists, escalate to NO-GO path on June 27 morning

### If NO-GO:
1. ☐ Update WORKLOG.md with "Validation NO-GO — [root cause]" entry
2. ☐ File root cause in BLOCKED.md with recommended fix + ETA
3. ☐ Disable HMM masking (set `hmm_observe_mode: true`) in session config
4. ☐ Deploy diagnostic logging for 24–48h (Session 4, June 25)
5. ☐ Schedule root-cause fix + re-implementation for June 26–27
6. ☐ Plan expedited re-validation for June 28 or July 1

---

## Appendix: Post-Market Diagnostic Commands

Run these after 20:00 UTC to populate the sections above:

```bash
# Container health
ssh awank@100.120.18.84 "docker ps --filter name=stockbot --format 'table {{.Names}}\t{{.Status}}'"

# Session count
ssh awank@100.120.18.84 "curl -s http://100.120.18.84:8000/health | python3 -m json.tool"

# Non-HOLD signal count
ssh awank@100.120.18.84 "docker logs stockbot --since '2026-06-24T13:30:00Z' 2>&1 | grep 'signal generated' | grep -v HOLD | wc -l"

# Buy probability max
ssh awank@100.120.18.84 "docker logs stockbot --since '2026-06-24T13:30:00Z' 2>&1 | grep 'buy_prob=' | grep -oP 'buy_prob=[\d.]+' | sort -t= -k2 -n | tail -1"

# Trades today
ssh awank@100.120.18.84 "sqlite3 /opt/stockbot/database/stockbot.db \"SELECT COUNT(*) FROM trades WHERE DATE(timestamp) = '2026-06-24';\""

# Realized P&L by session
ssh awank@100.120.18.84 "sqlite3 /opt/stockbot/database/stockbot.db \"SELECT session_id, ticker, SUM(realized_pnl) as total_pnl FROM trades WHERE DATE(timestamp) = '2026-06-24' GROUP BY session_id ORDER BY ticker;\""

# Regime history (sample — AAPL)
ssh awank@100.120.18.84 "docker logs stockbot --since '2026-06-24T13:30:00Z' 2>&1 | grep 'AAPL.*regime=' | head -20"

# Z-score drift (all sessions, last 1 day)
uv run python /opt/stockbot/scripts/query_drift_logs.py --days 1 --json
```

---

*Template created: 2026-06-23 (Session proactive prep)*  
*Filled: 2026-06-24 post-market (user execution post-validation)*  
*Reference files*: VALIDATION_WINDOW_MONITORING_LOG.md, PHASE_4_IMMEDIATE_EXECUTION_PLAN.md, VALIDATION_SUCCESS_METRICS_CHECKLIST.md
