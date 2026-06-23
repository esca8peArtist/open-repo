# Phase 4 Immediate Execution Plan — June 24–30 2026

**Status**: Ready for activation upon June 24 validation PASS  
**Baseline config**: 5-session deployment (JPM ridge_wf + 4× lgbm_ho on AMZN/AAPL/MSFT/NVDA)  
**Account equity**: $106,000 (Alpaca paper)  
**Current deployment**: 5% per session × 5 sessions = 25% total = $26,500  
**Cash buffer**: 75% = $79,500

---

## Executive Decision Tree

```
VALIDATION RESULT (June 24 20:00 UTC outcome)
│
├─ PASS (≥3 sessions non-HOLD, regime initialized, ≥1 trade executed)
│  └─ IMMEDIATE PATH SELECTION (user decision, typically <5 min)
│     ├─ Path A (Covered Calls): income overlay on existing equity positions
│     ├─ Path B (Inverse ETF): hedging via PSQ/SH, requires thermal verification
│     ├─ Path C (Earnings Drift): event-driven positions on earnings days
│     └─ COMBINATION (A + C recommended): parallel implementation no thermal dependency
│
├─ CAUTION (2 sessions non-HOLD, regime OK, but signal confidence low)
│  └─ HOLD DECISION: Continue monitoring 5-session config (June 25–26)
│     └─ If gap resolves by June 26 18:00 UTC: proceed to Phase 4
│     └─ If gap persists: escalate to NO-GO path
│
└─ NO-GO (<2 sessions passing, regime=None, order errors)
   └─ ROOT-CAUSE FIX: Disable HMM masking, diagnostic logging (June 25)
      └─ Re-implement & re-validate (June 26–27)
      └─ Phase 4 deferred to June 28–July 1
```

---

## Phase 4 Path A: Covered Calls Overlay

### A1. Overview

**What it does**: Write short call options against existing long equity positions (start with AAPL, expand to MSFT/AMZN/JPM). Collects premium income without increasing capital at risk — the equity position is the collateral.

**Example trade**:
- Own 100 AAPL shares (held from equity session)
- Sell 1 call contract (100 shares covered) at delta-40 strike (~5-8% OTM)
- Collect $400–600 premium per month
- If AAPL stays below strike: keep premium, continue holding shares
- If AAPL called away: shares sold at strike price (limited upside, no loss)

**Capital requirement**: $0 new capital (uses existing equity positions as collateral)  
**Expected monthly income**: +$500–1,500 (conservative, per PHASE_4_OPTIONS_FRAMEWORK.md)  
**Risk**: Opportunity cost if equity rallies >8% and shares are called away

### A2. Readiness Checklist (Before Implementation)

- [ ] Verify Alpaca account has Level 1 options approval (`alpaca.markets/account/options`)
- [ ] Confirm equity positions exist: check `GET /api/sessions/aapl_lgbm_ho_001/positions` → ≥100 AAPL shares held
- [ ] Read PHASE_4_RISK_CONFIGURATION_PLAYBOOK.md Section 2 (guardrails A1–A3)
- [ ] Review architecture gaps: Gap 1 (option_positions table), Gap 4 (naked-call prevention) — **must be implemented before live**

### A3. Implementation Steps (June 24–27, ~11.5h total)

**Critical path**: Gap 1 → Gap 4 → Gap 2 → (Gap 3 + Gap 5 parallel)

| Step | Gap | Task | Hours | Timeline | Owner |
|------|-----|------|-------|----------|-------|
| 1 | Gap 1 | Create `option_positions` DB table | 1h | June 24 21:00–22:00 UTC | Agent |
| 2 | Gap 4 | Implement naked-call prevention guardrail A1 | 3h | June 24 22:00–01:00 UTC (next day) | Agent |
| 3 | Gap 4 | Wire guardrail A1 into pre-order validation | 1h | June 25 01:00–02:00 UTC | Agent |
| 4 | Unit test | Test A1 (SELL blocked when calls uncovered) | 1h | June 25 02:00–03:00 UTC | Agent |
| 5 | Gap 2 | Implement `OptionsLiveSession` class | 4h | June 25 08:00–12:00 UTC | Agent |
| 6 | Gap 3 + 5 | Greeks logging + delta aggregation (parallel) | 3h | June 25 12:00–15:00 UTC | Agent |
| 7 | Integration | Deploy to Jetson, test on paper account | 2h | June 25 15:00–17:00 UTC | Agent |
| 8 | Paper trade | Write 5–10 covered call cycles on AAPL | 3–5 days | June 25–29 | Live |
| 9 | Go/no-go | Review paper trading results; if Sharpe ≥1.5, approve live | — | June 28 18:00 UTC | User |

**Total pre-paper-trade effort**: 15h (can compress to 12h with aggressive parallelization)

### A4. Paper Trading Metrics (June 25–29)

Monitor these during paper trading:

| Metric | Target | Alert if |
|--------|--------|----------|
| Call completion rate | >80% of attempted writes succeed | <70% |
| Naked-call violations | 0 | ≥1 |
| Assignment events | 0–1 (expected for 5–10 cycles) | >2 (early pattern) |
| Average premium collected | $300–500 per month simulation | <$200 (low premium) |
| Paper Sharpe (call cycles only) | ≥1.5 | <1.0 |

### A5. Live Deployment Approval Gate (June 28 or June 29)

**Go-live criteria**:
- ☐ 10+ paper call cycles completed without naked-call violations
- ☐ Average premium collected ≥$300/cycle (annualized: >$3,600)
- ☐ Sharpe on closed cycles ≥1.5
- ☐ All guardrails A1, A3 tested and passing
- ☐ Container restarts persist option_positions table correctly

**If approved**: Expand to MSFT/AMZN/JPM starting June 30  
**If rejected**: Root-cause analysis; retry June 30–July 5

### A6. Expansion Schedule (Post-Approval)

| Ticker | Delta | Expiration | Cycles per Month | Timeline |
|--------|-------|-----------|------------------|----------|
| AAPL | 0.40 | Monthly (4th Fri) | 1 | June 25–29 (paper) → June 30+ (live) |
| MSFT | 0.40 | Monthly | 1 | June 30–July 7 (live) |
| AMZN | 0.40 | Monthly | 1 | July 1–7 (live) |
| JPM | 0.40 | Monthly | 1 | July 2–7 (live) |

---

## Phase 4 Path B: Inverse ETF Hedge Session (PSQ or SH)

### B1. Overview

**What it does**: Add a 6th trading session that holds PSQ (inverse Nasdaq-100) or SH (inverse S&P 500) long positions **only when HMM regime = bear**. Provides portfolio delta hedging without options complexity.

**Example trade**:
- HMM regime = Bull: No position (session idle)
- HMM regime = Bear (probability >60%): Enter PSQ long position (5% of session capital)
- HMM regime returns to Bull/Sideways: Auto-exit PSQ position
- Effect: Negative correlation during bear markets reduces portfolio drawdown by 8–15%

**Capital requirement**: $0 new capital (uses existing account)  
**Expected annual value**: +$2,000–8,000 (2–8% via drawdown reduction, not direct alpha)  
**Thermal requirement**: SC1148 cooler must be installed; Pi 5 maxes out at 5 sessions without it

### B2. Readiness Checklist (Before Implementation)

- [ ] Verify SC1148 cooler installed on Jetson (`ssh awank@100.120.18.84 "ls -la /sys/class/thermal/thermal_zone*"` should show multiple zones)
- [ ] Confirm thermal budget: run `bash scripts/thermal-stress-test.sh 6` — if peak temp <75°C, proceed; if >80°C, delay until cooler operational
- [ ] Read PHASE_4_RISK_CONFIGURATION_PLAYBOOK.md Section 3 (guardrails B1–B3)
- [ ] Review HMM regime integration: B1 requires regime_change callback wiring

### B3. Implementation Steps (June 24–July 1, ~6h total)

**Not a critical path** — can run in parallel with Path A or C.

| Step | Gap | Task | Hours | Timeline | Owner |
|------|-----|------|-------|----------|-------|
| 1 | B1 | Implement `InverseETFSession` class + B1 auto-exit | 2h | June 25 16:00–18:00 UTC | Agent |
| 2 | B2 | Implement guardrail B2 (max notional cap) | 1h | June 25 18:00–19:00 UTC | Agent |
| 3 | B3 | Implement guardrail B3 (whipsaw prevention, 2-bar hold) | 0.5h | June 25 19:00–19:30 UTC | Agent |
| 4 | Unit test | Test B1 (auto-exit on regime change), B2 (size cap), B3 (whipsaw) | 1.5h | June 26 08:00–09:30 UTC | Agent |
| 5 | Deploy | Deploy to Jetson; run in shadow mode (order_submission: false) | 1h | June 26 09:30–10:30 UTC | Agent |
| 6 | Paper trade | Run shadow mode 3–5 trading days (observe regime cycles) | 3–5 days | June 26–July 1 | Live |
| 7 | Go/no-go | Review shadow logs; if portfolio Sharpe >2.0, approve live | — | July 1 18:00 UTC | User |

**Total pre-paper-trade effort**: 6h

### B4. Thermal Check (Critical Gate)

```bash
# Before deploying 6th session:
ssh awank@100.120.18.84 "bash scripts/thermal-stress-test.sh 6"

# Expected output:
# Peak temp (5 sessions): XX°C
# Peak temp (6 sessions): XX°C ← must be <75°C; if >80°C, DO NOT deploy
```

**IF thermal check fails**: Delay Path B until SC1148 installed or pursue Path A + C instead.

### B5. Paper Trading Metrics (June 26–July 1)

Monitor during shadow mode:

| Metric | Target | Alert if |
|--------|--------|----------|
| Regime cycles observed | ≥1 bull→bear transition | 0 (insufficient data) |
| Auto-exit accuracy | 100% (exits on regime change) | <100% (logic bug) |
| Max hedge notional | <25% of equity notional | ≥30% (exceeds guardrail) |
| Whipsaw events | <2 (regime flips 2+ times rapidly) | ≥3 |
| Portfolio Sharpe (6 sessions combined) | >2.0 | <1.8 (no hedge benefit) |

### B6. Live Deployment Approval Gate (July 1)

**Go-live criteria**:
- ☐ SC1148 cooler installed and thermal test passes (<75°C with 6 sessions)
- ☐ 3–5 days of shadow mode shows regime cycling and proper auto-exit behavior
- ☐ Portfolio Sharpe on combined (5 equity + 1 hedge) >2.0
- ☐ All guardrails B1–B3 tested and passing

**If approved**: Enable live order submission for 6th session July 2  
**If thermal check fails**: Defer to Path A + C (no cooler dependency)

---

## Phase 4 Path C: Earnings Drift Strategy (PEAD)

### C1. Overview

**What it does**: Enter positions on earnings day (T) for AAPL/MSFT/NVDA/JPM/AMZN, exit on T+20 calendar days. Exploits post-earnings-announcement drift (PEAD) — the empirical tendency for stocks to drift in the direction of earnings surprise for 2–4 weeks post-announcement.

**Example trade**:
- June 26: AAPL reports earnings, model generates BUY signal
- June 26: Enter PEAD position (2–5% of account) with tag="PEAD_EXEMPT"
- June 27–July 16: Hold position; exit if profit >+2%, loss >-1.5%, or T+20 reached
- June 30: MSFT reports, enter 2nd PEAD position (max 3 concurrent)

**Capital requirement**: $0 new capital (uses existing account)  
**Expected annual value**: +$500–1,500 (base case, 20 earnings events/year)  
**Seasonality**: Earnings clustered in 4 windows (Jan/Apr/Jul/Oct) — validation requires actual earnings events

### C2. Readiness Checklist (Before Implementation)

- [ ] Read PHASE_4_RISK_CONFIGURATION_PLAYBOOK.md Section 4 (guardrails C1–C4)
- [ ] Review earnings calendar integration: Alpaca earnings calendar endpoint available, no API cost
- [ ] Confirm `earnings_blackout_enabled: true` in session config (existing feature)
- [ ] Understand PEAD timing: next AAPL earnings likely late July; JPM typically mid-July

### C3. Implementation Steps (June 24–27, ~9h total)

**Fastest path** — can be ready by June 25 evening for deployment.

| Step | Gap | Task | Hours | Timeline | Owner |
|------|-----|------|-------|----------|-------|
| 1 | DB | Create `pead_positions` table in trading.db | 1h | June 24 21:00–22:00 UTC | Agent |
| 2 | C1 | Implement earnings blackout exemption tag (PEAD_EXEMPT) | 1h | June 24 22:00–23:00 UTC | Agent |
| 3 | C2 | Implement per-event drawdown limit (-1.5%) in PEADSession | 1h | June 25 00:00–01:00 UTC | Agent |
| 4 | C3 | Implement concurrent PEAD position cap (max 3) | 1h | June 25 01:00–02:00 UTC | Agent |
| 5 | C4 | Implement earnings date staleness check | 1h | June 25 02:00–03:00 UTC | Agent |
| 6 | Backtest | Backtest on 2020–2026 historical earnings (120 events) | 2–3h | June 25 08:00–11:00 UTC | Agent |
| 7 | Deploy | Deploy to Jetson; ready for first earnings event | 1h | June 25 11:00–12:00 UTC | Agent |
| 8 | Wait | Wait for next earnings event (likely JPM mid-July) | — | June 25–July 15 | — |
| 9 | Paper trade | Monitor first 5–10 earnings events; track T+20 outcomes | 4–12 weeks | July onwards | Live |

**Total pre-deployment effort**: 7–9h  
**Timeline to first live trade**: June 25 (ready), but waits for next earnings event (next ~2–4 weeks)

### C4. Backtest Validation (June 25 08:00–11:00 UTC)

Run historical PEAD backtest to validate strategy:

```bash
uv run python scripts/pead_backtest.py --tickers AAPL MSFT NVDA JPM AMZN \
  --start-date 2020-01-01 --end-date 2026-06-24 \
  --entry-signal-type lgbm_ho --exit-days 20 \
  --output-file /tmp/pead_backtest_2020_2026.json
```

**Expected backtest metrics** (from PHASE_4_OPTIONS_FRAMEWORK.md):
- Hit rate: 50–60% (>50% = good)
- Avg win: +1.5%
- Avg loss: -0.8%
- Net expectancy: +0.42% per event
- Sharpe: >1.0 on historical data

**Gate**: If backtest Sharpe <0.8, revisit strategy before live deployment.

### C5. Paper Trading Metrics (July onwards, 5–10 earnings events)

Monitor first PEAD trades:

| Metric | Target | Alert if |
|--------|--------|----------|
| Entry execution | 100% (all signals executed) | <90% |
| Early exits (±2% / ±1.5%) | <30% (most hold to T+20) | >50% |
| Win rate | >50% (align with backtest) | <40% |
| Avg win | +1.0% to +1.5% | <+0.5% |
| Avg loss | -0.5% to -0.8% | <-1.0% |
| Max concurrent | ≤3 | >3 (violates guardrail) |

### C6. Live Deployment Approval Gate (July/August)

**Go-live criteria**:
- ☐ Backtest Sharpe ≥0.8 on 2020–2026 data
- ☐ 5–10 paper PEAD trades completed with win rate ≥50%
- ☐ All guardrails C1–C4 tested and passing
- ☐ User confidence ≥80% in strategy logic

**If approved**: Continue live PEAD trading; scale position size if Sharpe >1.2  
**If rejected**: Review feature engineering or entry timing; retry next earnings season

---

## Combined Path Recommendation: A + C (Parallel, June 24–30)

**Why A + C together** (from PHASE_4_OPTIONS_FRAMEWORK.md):
- **No thermal dependency**: Both use existing 5 sessions; no 6th session required
- **No wait-time conflict**: Path A validates quickly (5–10 cycles); Path C backtest + deploy ready by June 25
- **Complementary income**: Path A = monthly premium (~$500–1,500/mo); Path C = event-driven (~$40–125/event)
- **Combined expected value**: +$1,000–2,500/month (A + C) vs. single-path +$500–1,500/month

### Combined Schedule

| Date | Path A | Path C | Parallel? |
|------|--------|--------|-----------|
| June 24 | Validation PASS → decision | Validation PASS → decision | Yes |
| June 24 21:00–01:00 UTC | Gap 1 (DB) + Gap 4 (guardrails) | Gap 1 (DB) + C1–C5 (guardrails) | **Yes (parallel agents)** |
| June 25 01:00–12:00 UTC | Gap 2 + Gap 3/5 + integration test | C4 backtest + deploy | **Yes** |
| June 25 15:00+ | Paper trade AAPL (live) | Ready for first earnings event | **Yes** |
| June 25–29 | Paper trade 5–10 cycles | Monitor for first earnings (likely JPM mid-July) | **Yes** |
| June 28 | Go/no-go decision (Sharpe ≥1.5 on paper) | Already deployed; waiting for event | Sequential |
| June 30+ | Expand to MSFT/AMZN/JPM | Continue monitoring | **Yes** |

### Capital Allocation (A + C Combined)

| Component | Allocation | Details |
|-----------|-----------|---------|
| Equity sessions (5 current) | 25% of $106K = $26,500 | 5% per session (unchanged) |
| Path A (covered calls on AAPL) | $0 new (uses existing AAPL position) | Overlay, no capital req. |
| Path C (PEAD positions) | 2–5% per event, max 3 concurrent = $6,360–15,900 | From remaining $79,500 buffer |
| **Total deployed** | 25% + 2.5–7.5% = 27.5–32.5% | Maintains 67.5–72.5% cash buffer |
| **Leverage ceiling** | 80% of account | Still well within limit |

---

## Phase 4 Path B (Alternative): Inverse ETF Hedge + SC1148 Verification

**Use this path IF**:
- ☐ User has installed or plans to install SC1148 cooler
- ☐ Thermal test confirms <75°C with 6 sessions
- ☐ User prefers risk reduction (drawdown hedge) over income generation

**Timeline**: Same as Path A/C, but adds 1–2h thermal verification before proceeding.

**Recommendation**: Run Path B in parallel with Path A (not C) if thermal check passes, or defer Path B to July after confirming cooler stability.

---

## Decision Matrix Summary

| Path | Status | Effort | Timeline | Expected Value | Thermal Dep? | Start Date |
|------|--------|--------|----------|-----------------|-------------|-----------|
| **A (Covered Calls)** | ✅ Ready | 11.5h | June 24–28 (paper) → June 30 (live) | +$500–1,500/mo | No | June 24 21:00 |
| **B (Inverse ETF)** | ✅ Ready | 6h | June 25–July 1 (paper) → July 2 (live) | +$2,000–8,000/yr | **Yes (SC1148)** | June 25 (if thermal OK) |
| **C (Earnings Drift)** | ✅ Ready | 7–9h | June 24–25 (deploy) → wait for event | +$500–1,500/yr | No | June 24 21:00 |

**Recommended for June 24 PASS outcome**: **A + C (immediate, no thermal wait)**  
**Add B later** (July) if thermal verification passes

---

## Contingency: If June 24 Validation = CAUTION

If 2 sessions passed but validation is CAUTION (signal confidence <0.6), **hold Phase 4 expansion** and instead:

1. Continue monitoring 5-session config through June 25–26
2. Run diagnostic analysis on why only 2 sessions generated signals
3. If gap resolves by June 26 18:00 UTC: expedited re-validation June 27, Phase 4 start June 27–28
4. If gap persists: escalate to NO-GO contingency path (disable HMM masking, observe mode)

---

## Contingency: If June 24 Validation = NO-GO

If validation fails completely (regime=None, <2 sessions passing), **Phase 4 is blocked** pending root-cause fix:

1. **June 25 morning**: File root cause in BLOCKED.md
2. **June 25 08:00–16:00 UTC**: Root-cause analysis + fix implementation (Session 4089, orchestrator)
3. **June 25 16:00–17:00 UTC**: Test on sandbox environment
4. **June 25 18:00 UTC**: Deploy fix to Jetson
5. **June 27 13:30–20:00 UTC**: Expedited re-validation (3-day window to stabilize before weekend)
6. **June 28–30**: Phase 4 implementation IF re-validation passes
7. **July 1**: Go-live decision for Phase 4 (delayed by ~1 week)

---

## Execution Tracking Template

### User Decision Log (June 24 20:00–21:00 UTC)

- [ ] Validation verdict confirmed: [**PASS** / **CAUTION** / **NO-GO**]
- [ ] Phase 4 path selected: [☐ A / ☐ B / ☐ C / ☐ A+C / ☐ A+B / ☐ Hold]
- [ ] Expected go-live date: _________
- [ ] Notes: _______

### Implementation Status (update during June 24–30)

| Path | Step | Status | Completed | Owner | Notes |
|------|------|--------|-----------|-------|-------|
| A | Gap 1 (DB) | ☐ Not started / ☐ In progress / ☐ Done | — | — | — |
| A | Gap 4 (guardrails) | ☐ Not started / ☐ In progress / ☐ Done | — | — | — |
| A | Integration test | ☐ Not started / ☐ In progress / ☐ Done | — | — | — |
| C | Backtest | ☐ Not started / ☐ In progress / ☐ Done | — | — | — |
| C | Earnings calendar | ☐ Not started / ☐ In progress / ☐ Done | — | — | — |

---

*Template created: 2026-06-23 (Session proactive prep)*  
*Activated: 2026-06-24 post-validation*  
*Reference files*: PHASE_4_OPTIONS_FRAMEWORK.md, PHASE_4_RISK_CONFIGURATION_PLAYBOOK.md, PHASE_4_CAPITAL_ALLOCATION_FRAMEWORK.md
