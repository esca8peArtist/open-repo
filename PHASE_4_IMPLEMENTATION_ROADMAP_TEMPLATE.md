# Phase 4 Implementation Roadmap Template

**Purpose**: 7–14 day daily milestone timeline for each Phase 4 path (Covered Calls / Inverse ETF / Earnings Drift).

**Status**: Pre-filled template with non-decision sections; user fills critical decision points and approval gates.

**Usage**: Select winning path(s) from PHASE_4_OUTCOMES_DECISION_MATRIX.md (June 24 20:00 UTC). Copy relevant roadmap section below. Update approval date (day 9–10) based on paper trading results.

---

## Path A: Covered Calls Overlay — 11–15 Day Roadmap

**Timeline**: June 24–July 7 (code + paper trading) → July 5–10 (go-live decision)

**Ownership**: Claude Code Agent (code) + User (go-live approval)

### Phase A1: Code Implementation (June 24–25, Days 1–2)

| Day | Date | Milestone | Deliverable | Owner | Go/No-Go Gate |
|-----|------|-----------|-------------|-------|--------------|
| 1 | June 24 21:00–22:00 UTC | Gap 1: Create `option_positions` DB table | `projects/stockbot/database/stockbot.db` updated; table schema with columns: `id, session_id, ticker, contract_spec, premium_collected, assignment_price` | Agent | ☐ Schema valid + indices created |
| 1 | June 24 22:00–23:30 UTC | Gap 4a: Implement naked-call prevention guardrail (Guard A1) | `src/stockbot/guards/covered_call_guard.py` (1,200 lines): `check_uncovered_calls()` validates equity position ≥ call contract qty before SELL order submission | Agent | ☐ Unit tests pass (12 test cases) |
| 2 | June 25 00:00–01:00 UTC | Gap 4b: Wire A1 into pre-order validation | Modify `src/stockbot/trading_session.py::_validate_order()` to call `covered_call_guard.check_uncovered_calls()` before `alpaca_client.submit_order()` | Agent | ☐ 5 integration tests pass |
| 2 | June 25 01:00–02:00 UTC | Unit test A1 | Test case: attempt SELL call with 0 equity position → guard blocks → order not submitted | Agent | ☐ Test passes (SELL blocked as expected) |
| 2 | June 25 02:00–03:00 UTC | Gap 2: Implement `OptionsLiveSession` class | `src/stockbot/models/options_live_session.py` (2,500 lines): extends `TradingSession` for options-specific signal generation, Greeks logging, premium tracking | Agent | ☐ Constructor + 6 core methods pass unit tests |

**Commitment Gate (Day 2, 03:00 UTC)**: All code complete; all tests passing; ready for integration testing.

### Phase A2: Integration & Testing (June 25, Days 2–3)

| Day | Date | Milestone | Deliverable | Owner | Go/No-Go Gate |
|-----|------|-----------|-------------|-------|--------------|
| 2 | June 25 08:00–12:00 UTC | Gap 3: Greeks logging + delta aggregation | Implement `src/stockbot/analytics/greeks_tracker.py` (1,000 lines): per-contract Greeks (delta, gamma, theta, vega); delta aggregation across portfolio | Agent | ☐ 8 unit tests pass; Greeks correctly logged to DB |
| 2 | June 25 12:00–15:00 UTC | Integration test (Gaps 1–5 together) | Spin up test container; simulate market session; execute covered call write flow: (1) detect AAPL position, (2) generate options signal, (3) construct SELL call order, (4) A1 validates, (5) order submitted, (6) Greeks logged | Agent | ☐ Full flow executes without error; no naked calls created |
| 3 | June 25 15:00–17:00 UTC | Deploy to Jetson (paper account) | `docker build -t stockbot-v4.3 -f Dockerfile.jetson .` → Push to Jetson → Restart container; validate `/api/health` returns 5 sessions active (5 equity + 1 options overlay) | Agent | ☐ Container healthy; all sessions reporting on Alpaca API |

**Integration Gate (Day 3, 17:00 UTC)**: Code integration complete; Jetson deployment successful; ready for paper trading.

### Phase A3: Paper Trading Validation (June 25–29, Days 3–7)

| Day | Date | Milestone | Metric Target | Go/No-Go Gate | Notes |
|-----|------|-----------|----------------|--------------|-------|
| 3–7 | June 25–29 | Write 5–10 covered call cycles on AAPL | Call completion rate >80%; 0 naked-call violations; avg premium $300–500/cycle | ☐ All metrics hit OR ☐ Investigate outlier | Monitor daily via dashboard; alert on any naked-call guard violation |
| 3–7 | June 25–29 | Track assignment events | 0–1 assignments expected (5–10 cycles = ~10–20% probability of exercise) | ☐ Assignments within range | Early assignment patterns can indicate higher IV or upcoming dividend |
| 3–7 | June 25–29 | Sharpe on closed cycles | ≥1.5 on paper trading sample | ☐ Sharpe ≥1.5 OR ☐ Investigate | By day 7 (June 29), must have ≥3 complete cycles for statistical validity |

**Paper Trading Gate (Day 7, June 29 17:00 UTC)**: ≥5 complete cycles; Sharpe ≥1.5; 0 guard violations → **APPROVE live deployment** OR ≥3 cycles with Sharpe <1.0 → **HOLD for diagnostics**.

### Phase A4: Go/No-Go Decision (June 28–29, Days 4–5)

| Criteria | Pass | Fail | Decision |
|----------|------|------|----------|
| **Paper cycle count** | ≥10 cycles completed | <5 cycles | If <5: extend paper trading through June 30 |
| **Naked-call violations** | 0 | ≥1 | If ≥1: root-cause guard logic; fix + re-test before go-live |
| **Sharpe on paper** | ≥1.5 | <1.0 | If <1.0: investigate entry/exit timing; may retrain model before live |
| **Guard reliability** | 100% of naked calls blocked | <100% | If <100%: HOLD live; debug guard logic |
| **User confidence** | ≥80% | <80% | User must explicitly confirm comfortable with live deployment |

**User Decision Form** (June 28 18:00 UTC):

```
[ ] I have reviewed the 5–10 paper trading cycles
[ ] Sharpe ≥1.5 observed on paper
[ ] 0 naked-call violations detected
[ ] I am ≥80% confident in live deployment
[ ] Approved to proceed with live covered call trading starting __________ (date)
```

**Live Deployment Gate (June 28 or June 29)**: If all 4 boxes checked → deploy to live Alpaca. If any unchecked → extend paper trading or escalate.

### Phase A5: Live Expansion (June 30–July 7, Days 6–13)

| Day | Date | Ticker | Expansion Step | Approval Gate | Notes |
|-----|------|--------|-----------------|--------------|-------|
| 6 | June 30 | AAPL | Live trading begins on AAPL (approved June 28–29) | ☐ First 5 live cycles execute successfully | Monitor Greeks; track realized premiums vs. paper baseline |
| 7 | July 1 | MSFT | Expand to MSFT; write first call cycle (if >100 shares held) | ☐ MSFT position ≥100 shares; first call written without error | Stagger expansions (1 per day) to manage operational complexity |
| 8 | July 2 | AMZN | Expand to AMZN; write first call cycle | ☐ AMZN position ≥100 shares | Check equity position balances from overnight positions |
| 9 | July 3 | JPM | Expand to JPM; write first call cycle | ☐ JPM position ≥100 shares | JPM typically highest IV → best premiums |
| 10 | July 4 | — | Monitor only (July 4 = US Independence Day, markets closed) | ☐ Container steady; no errors overnight | Day off; prepare weekly monitoring dashboard |
| 11–13 | July 5–7 | All 4 tickers | Continuous monitoring; 2–4 cycles per ticker per month | ☐ Portfolio Greeks neutral; no unplanned assignments | Final go-live decision: if all 4 tickers healthy by July 7, Phase A fully live |

**Expansion Gate (July 7, 18:00 UTC)**: If all 4 tickers performing (Sharpe ≥1.5, 0 errors, premium collection on track) → **Phase A fully live**. If 1+ ticker showing issues (Sharpe <1.0, premium <$200/cycle) → **keep live but reduce position size** or **hold expansion pending fix**.

---

## Path B: Inverse ETF Hedge Session — 8–15 Day Roadmap

**Timeline**: June 25–July 2 (code + thermal verification) → July 1 (go-live decision)

**Ownership**: Claude Code Agent (code) + User (thermal verification + go-live approval)

**CRITICAL GATE**: SC1148 cooler thermal test must pass <75°C with 6 sessions BEFORE code implementation begins.

### Phase B0: Thermal Verification (June 24–25, Pre-Day 0)

| Checkpoint | Command | Expected Output | Go/No-Go | Action if Fail |
|-----------|---------|-----------------|----------|----------------|
| **Cooler Installation** | `ssh awank@100.120.18.84 "ls -la /sys/class/thermal/thermal_zone*"` | >2 thermal zones visible | ☐ PASS / ☐ FAIL | Install SC1148 or defer Path B to July |
| **Baseline 5-session temp** | `bash scripts/thermal-stress-test.sh 5 --duration 30` | Peak <72°C | ☐ PASS / ☐ FAIL | Acceptable; proceed |
| **6-session stress test** | `bash scripts/thermal-stress-test.sh 6 --duration 30` | Peak <75°C | ☐ PASS / ☐ FAIL | **CRITICAL**: If peak >75°C, do not deploy Path B. Defer or skip. |

**Thermal Decision Gate (June 25 08:00 UTC)**:
- ✅ If 6-session test <75°C → **PROCEED to code implementation**
- ❌ If 6-session test >80°C → **BLOCK Path B; recommend Path A + C instead**
- ⚠️ If 6-session test 75–80°C → **CAUTION; delay Path B to July; monitor cooler performance**

---

### Phase B1: Code Implementation (June 25–26, Days 1–2)

| Day | Date | Milestone | Deliverable | Owner | Go/No-Go Gate |
|-----|------|-----------|-------------|-------|--------------|
| 1 | June 25 16:00–18:00 UTC | B1a: Implement `InverseETFSession` class | `src/stockbot/models/inverse_etf_session.py` (1,500 lines): 6th session, regime-dependent entry/exit, PSQ/SH ticker selection logic, auto-exit on regime change | Agent | ☐ Constructor + `on_regime_change()` callback pass unit tests |
| 1 | June 25 18:00–19:00 UTC | B1b: Implement guardrail B2 (max notional cap) | `check_notional_cap()` in same file: prevent hedge notional from exceeding 25% of portfolio equity | Agent | ☐ 6 unit tests pass; cap enforced correctly |
| 1 | June 25 19:00–19:30 UTC | B3: Implement whipsaw prevention (2-bar hold) | `check_whipsaw_protection()`: after regime flip, require 2 consecutive bars in new regime before re-entering | Agent | ☐ 4 unit tests pass; whipsaw protection blocks spurious entries |
| 2 | June 26 08:00–09:30 UTC | Unit test all guardrails (B1–B3) | Full integration test: regime Bull → Bear → Bull transition; verify entry/exit timing and notional cap enforcement | Agent | ☐ All 12 unit tests pass |
| 2 | June 26 09:30–10:30 UTC | Deploy to Jetson (shadow mode) | Container restart with 6 sessions; PSQ/SH session initialized; `order_submission: false` (shadow mode, no real orders) | Agent | ☐ Container healthy; 6 sessions active on API; shadow mode confirmed |

**Implementation Gate (Day 2, 10:30 UTC)**: Code complete; Jetson shadow deployment ready.

### Phase B2: Paper Trading (Shadow Mode) — June 26–July 1, Days 2–8

| Day | Date | Milestone | Metric Target | Go/No-Go Gate | Notes |
|-----|------|-----------|----------------|--------------|-------|
| 2–8 | June 26–July 1 | Observe regime cycles (shadow mode) | ≥1 bull→bear transition observed | ☐ Regime transition logged | If no regime cycle, add note for re-evaluation |
| 2–8 | June 26–July 1 | Verify auto-exit on regime change | 100% exit accuracy (all exits happen within 1 bar of regime flip) | ☐ Auto-exit logic verified | Each regime flip = 1 entry + 1 exit; check all exited correctly |
| 2–8 | June 26–July 1 | Max hedge notional | <25% of portfolio equity at all times | ☐ Notional cap never exceeded | Monitor `position_size_pct * equity` throughout |
| 2–8 | June 26–July 1 | Whipsaw detection | <2 false entries (rapid regime flips back-and-forth) | ☐ Whipsaw < 2 events | 2+ whipsaws = guard needs tuning; may retrain before live |
| 2–8 | June 26–July 1 | Combined portfolio Sharpe (5 equity + 1 hedge) | >2.0 on shadow period | ☐ Sharpe >2.0 OR ☐ Investigate | Calculate: 6-session combined Sharpe = (weighted avg returns) / (combined volatility) |

**Paper Trading Gate (July 1, 18:00 UTC)**: If all metrics pass → **APPROVE live deployment**. If Sharpe <1.8 or whipsaw >2 → **Hold for diagnostics; delay live to July 8+**.

### Phase B3: Go/No-Go Decision (June 26–July 1, Days 2–8)

| Criteria | Pass | Fail | Decision |
|----------|------|------|----------|
| **Thermal test (pre-code)** | <75°C with 6 sessions | >80°C | HARD BLOCK: Do not deploy Path B |
| **Regime cycle observed** | ≥1 bull→bear cycle | None observed | Insufficient data; extend shadow mode to July 5 |
| **Auto-exit accuracy** | 100% | <95% | Root-cause exit timing logic; fix + re-test |
| **Whipsaw events** | <2 | ≥3 | Adjust `_HOLD_BARS=3` (currently 2); re-evaluate |
| **Portfolio Sharpe** | >2.0 | <1.8 | Investigate: may indicate hedge is too large or regime-detection needs tuning |
| **User confidence** | ≥75% | <75% | User must explicitly confirm before live go-ahead |

**User Decision Form** (July 1 18:00 UTC):

```
[ ] Thermal test confirmed <75°C on June 25
[ ] Shadow mode ran 3–5 trading days without error
[ ] Portfolio Sharpe >2.0 observed
[ ] ≥1 regime cycle observed (hedge demonstrated value)
[ ] 0 whipsaw protection violations
[ ] I am ≥75% confident in live deployment
[ ] Approved to proceed with live inverse ETF hedge starting __________ (date)
```

**Live Deployment Gate (July 1 or July 2)**: If all 6 boxes checked → enable live order submission for 6th session. If any unchecked → extend shadow mode or escalate.

### Phase B4: Live Deployment (July 2+, Day 9+)

| Day | Date | Milestone | Approval Gate | Notes |
|-----|------|-----------|--------------|-------|
| 9+ | July 2+ | Enable live order submission for 6th session | ☐ First hedge entry executed successfully | Monitor PSQ/SH position size; confirm <25% of portfolio equity |
| 9+ | July 2+ | Monitor regime cycles in live environment | ☐ Auto-exit executes on next regime flip | Measure exit slippage vs. shadow mode baseline |
| 10+ | July 3+ | Continuous hedge monitoring | ☐ Portfolio Sharpe remains >2.0 | If portfolio Sharpe drops <1.8, investigate or pause 6th session |

---

## Path C: Earnings Drift (PEAD) Strategy — 2–10 Day Roadmap

**Timeline**: June 24–25 (code + backtest) → June 25 (deploy ready) → event-driven go-live

**Ownership**: Claude Code Agent (code + backtest) + User (earnings calendar monitoring + go-live approval)

### Phase C1: Code Implementation (June 24–25, Days 1–2)

| Day | Date | Milestone | Deliverable | Owner | Go/No-Go Gate |
|-----|------|-----------|-------------|-------|--------------|
| 1 | June 24 21:00–22:00 UTC | C1 DB: Create `pead_positions` table | `projects/stockbot/database/stockbot.db`: columns: `id, session_id, ticker, entry_date, entry_price, tag='PEAD_EXEMPT', exit_date, exit_price, realized_pnl` | Agent | ☐ Schema created; indices on entry_date, tag |
| 1 | June 24 22:00–23:00 UTC | C2: Implement earnings blackout exemption tag | Modify `src/stockbot/guards/earnings_guard.py`: check `tag='PEAD_EXEMPT'` before blocking on earnings-day SELL signals | Agent | ☐ 6 unit tests pass; PEAD_EXEMPT bypasses earnings blackout |
| 2 | June 25 00:00–01:00 UTC | C3: Implement per-event drawdown limit | `check_pead_drawdown()`: auto-exit if event P&L < -1.5% (per-trade, not portfolio-level) | Agent | ☐ 4 unit tests pass; drawdown limit enforced |
| 2 | June 25 01:00–02:00 UTC | C4: Implement concurrent position cap | `check_pead_concurrent()`: max 3 simultaneous PEAD positions; new PEAD signal blocked if ≥3 open | Agent | ☐ 5 unit tests pass; position cap enforced |
| 2 | June 25 02:00–03:00 UTC | C5: Implement earnings date staleness check | `check_earnings_freshness()`: earnings dates from Alpaca API; warn if data >7 days old | Agent | ☐ 3 unit tests pass; staleness check works |

**Commitment Gate (Day 2, 03:00 UTC)**: All code complete; all tests passing.

### Phase C2: Backtest Validation (June 25, Days 2–3)

| Day | Date | Milestone | Command | Target Metric | Go/No-Go Gate |
|-----|------|-----------|---------|----------------|--------------|
| 2 | June 25 08:00–11:00 UTC | Backtest on 2020–2026 earnings | `uv run python scripts/pead_backtest.py --tickers AAPL MSFT NVDA JPM AMZN --start-date 2020-01-01 --end-date 2026-06-24 --exit-days 20 --output-file /tmp/pead_backtest_2020_2026.json` | Hit rate 50–60%; Sharpe ≥0.8; Win rate ≥50% | ☐ Sharpe ≥0.8 OR ☐ Investigate model |
| 2 | June 25 11:00–12:00 UTC | Analyze backtest results | Parse JSON output; extract: hit_rate, sharpe, avg_win, avg_loss, max_drawdown, win_rate | If any metric poor (Sharpe <0.8, win_rate <45%), investigate feature drift | ☐ Results reviewed + documented |
| 3 | June 25 12:00–13:00 UTC | Document backtest findings | Create `PEAD_BACKTEST_RESULTS_2020_2026.md` (1–2 KB): hit rate, Sharpe, regime breakdown, seasonal patterns | Report ready for user review | ☐ Report filed + user notified |

**Backtest Gate (June 25 11:00 UTC)**:
- ✅ If Sharpe ≥0.8 → **APPROVE deployment**
- ❌ If Sharpe <0.8 → **HOLD for diagnostics**; investigate feature engineering or entry signals

### Phase C3: Deploy & Integration (June 25, Day 3)

| Day | Date | Milestone | Deliverable | Owner | Go/No-Go Gate |
|-----|------|-----------|-------------|-------|--------------|
| 3 | June 25 13:00–14:00 UTC | Deploy to Jetson | Rebuild container with PEAD code; restart stockbot; verify `/api/health` returns 5 sessions healthy | Agent | ☐ Container healthy; 5 sessions active; PEAD tables created |
| 3 | June 25 14:00–15:00 UTC | Verify earnings calendar integration | Query Alpaca earnings endpoint: `GET /data/v1/corporate_actions/earnings` for next 30 days | Check for AAPL, MSFT, NVDA, JPM, AMZN earnings | ☐ Earnings data fetched successfully; next event identified |
| 3 | June 25 15:00–16:00 UTC | Ready for first earnings event | Document: next earnings date, expected entry date, expected T+20 exit date | Entry logic staged; waiting for earnings event | ☐ Timeline documented; ready to trade |

**Deployment Gate (June 25 16:00 UTC)**: Code deployed; earnings calendar accessible; **ready for first earnings event** (likely JPM mid-July).

### Phase C4: Event-Driven Execution (June 25 onwards, Days 3+)

| Milestone | Expected Date | Trigger | Action | Go/No-Go Gate |
|-----------|--------------|---------|--------|--------------|
| **First earnings event** | JPM: ~July 15–17 | JPM Q2 earnings released (after-hours or pre-market) | Enter PEAD position (2–5% of account); tag='PEAD_EXEMPT' | ☐ Position entered; tag verified |
| **T+1 through T+19** | July 16–Aug 5 | Position open | Monitor P&L daily; alert if >-1.5% drawdown (auto-exit) | ☐ P&L tracked; no unexpected exits |
| **T+20 exit** | Aug 5 | Automatic exit trigger | Position auto-closes at market open T+20 | ☐ Exit executed; realized P&L recorded |
| **Event 2** | MSFT: ~July 24–26 | MSFT Q3 earnings released | Enter 2nd PEAD position | ☐ Position entered; max 3 concurrent enforced |
| **Events 3–5** | Aug + Sept | Continue PEAD trading | Monitor 5–10 total events before go-live approval | ☐ All 5–10 events completed |

**Live Approval Gate (August, after 5–10 events)**:

| Criteria | Pass | Fail | Decision |
|----------|------|------|----------|
| **Event count** | ≥5 completed | <5 | Insufficient data; extend to 10 events (September) |
| **Win rate** | ≥50% | <50% | Below backtest; investigate entry timing or signal quality |
| **Avg win** | +1.0% to +1.5% | <+0.5% | Premium too small; may need position size adjustment |
| **Avg loss** | -0.5% to -0.8% | <-1.0% | Loss limits working; no issues detected |
| **Max concurrent** | ≤3 | >3 | Position cap violation; fix guardrail logic |

**User Approval Form** (August, after 5+ events):

```
[ ] ≥5 PEAD events completed successfully
[ ] Win rate ≥50% observed
[ ] Average win +0.8% to +1.5%
[ ] Average loss -0.5% to -0.8%
[ ] Max concurrent positions never exceeded 3
[ ] I am ≥80% confident in continued PEAD trading
[ ] Approved to continue PEAD strategy at full position size
```

**Phase C Completion**: PEAD strategy approved for continuous operation in Phase 4 (ongoing through 2026).

---

## Combined Path (A + C) — Parallel Execution Roadmap

**If validation = PASS and both Path A score ≥7.5 AND Path C score ≥7.5, execute A + C in parallel.**

### Parallel Timeline (June 24–30)

| Date | Path A | Path C | Parallel? | Owner |
|------|--------|--------|-----------|-------|
| June 24 20:00–20:30 | Validation analysis | Validation analysis | **YES** (same analysis) | User |
| June 24 21:00–01:00 | Gap 1 + Gap 4 implementation (4h) | DB + C1–C5 implementation (4h) | **YES (parallel agents)** | 2 agents |
| June 25 01:00–12:00 | Gap 2 + Gap 3/5 + integration (9h) | C4 backtest + C5 staleness (4h) | **YES** | 2 agents |
| June 25 12:00–17:00 | Deploy Jetson (2h) + prep paper | Deploy Jetson (1h) + stage earnings | **YES** | Parallel; then sync |
| June 25 17:00+ | Paper trade AAPL (live) | Ready for event (standby) | **Sequential (A active, C waiting)** | A: active; C: monitor |
| June 25–29 | 5–10 covered call cycles | Monitor for first earnings event | **Parallel observation** | Both running |
| June 28 | Go/no-go decision (Sharpe ≥1.5) | Ready (waiting for JPM earnings ~July 15) | **Sequential decision** | User approval |
| June 30+ | Expand to MSFT/AMZN/JPM | Continue monitoring | **Parallel** | Both in production |

**Parallel Work Allocation**:
- **Agent 1**: Path A implementation (Gaps 1–5, full integration, Jetson deployment)
- **Agent 2**: Path C implementation (DB, guardrails C1–C5, backtest, Jetson integration)
- Both agents run concurrently; combined wall-clock time: 11.5h (vs. 18h sequential)

**Coordination Checkpoints**:
- June 25 12:00 UTC: Sync Jetson deployments (both agents report container status)
- June 25 17:00 UTC: Validate both A and C active on Jetson (health check confirms both)
- June 28 18:00 UTC: User approves both A (paper test) and C (standby) for their respective timelines

---

## Risk Mitigation & Escalation Triggers

### Path A Escalation Triggers

| Trigger | Action | Timeline |
|---------|--------|----------|
| Guard A1 blocks legitimate SELL (false positive) | Debug `check_uncovered_calls()` logic; adjust position check | <2 hours; fix before next cycle |
| Sharpe <1.0 on first 3 paper cycles | Pause paper trading; investigate entry/exit timing | <4 hours; resume if tuning helps |
| Assignment event on first 3 cycles | Normal for covered calls; monitor frequency | Document + continue |
| Any naked-call violation (guard failure) | IMMEDIATE HALT; root-cause + deploy fix before next cycle | CRITICAL |

### Path B Escalation Triggers

| Trigger | Action | Timeline |
|---------|--------|----------|
| Thermal test >75°C (critical) | HARD BLOCK; do not proceed with Path B | Immediate; defer to July |
| Whipsaw >2 events in first week | Increase `_HOLD_BARS` from 2 to 3; re-evaluate | <24 hours; resume if improved |
| Portfolio Sharpe <1.8 (hedge underperforming) | Investigate regime-detection accuracy; may need HMM tuning | <48 hours; escalate if persists |
| Auto-exit failure (regime flip but position held) | CRITICAL; debug exit trigger logic; fix + re-test | <2 hours; HALT if not fixed |

### Path C Escalation Triggers

| Trigger | Action | Timeline |
|---------|--------|----------|
| Backtest Sharpe <0.8 | Hold deployment; investigate PEAD model features | <48 hours; retry with feature tuning |
| First 3 events win rate <40% | Below 50% backtest threshold; investigate entry signal quality | <2 weeks; adjust position size or pause |
| Concurrent position limit violated (>3 open) | CRITICAL; review guardrail logic; HALT if unfixable | Immediate |
| Earnings calendar data stale (>7 days old) | Warn user; verify Alpaca API connectivity | <24 hours; manually fetch if needed |

---

## Success Criteria (End of 14 Days)

### Path A Success
- ✅ ≥10 paper covered call cycles completed
- ✅ 0 naked-call violations (guard 100% effective)
- ✅ Sharpe ≥1.5 on paper cycles
- ✅ ≥3 live cycles on AAPL (if approved June 28)
- ✅ Expansion to MSFT/AMZN underway (if approved June 28–30)

### Path B Success
- ✅ Thermal test <75°C confirmed pre-code
- ✅ ≥1 regime cycle observed in shadow mode
- ✅ Auto-exit 100% accurate (no failed exits)
- ✅ Portfolio Sharpe >2.0 (5 equity + 1 hedge combined)
- ✅ Live deployment approved & running (if approved July 1–2)

### Path C Success
- ✅ Backtest Sharpe ≥0.8 on 2020–2026 data
- ✅ Code deployed & earnings calendar accessible
- ✅ Ready for first earnings event (monitoring for JPM ~mid-July)
- ✅ ≥1 live PEAD event completed by mid-August
- ✅ ≥5 events completed with win rate ≥50% by end of August

### Combined A + C Success
- ✅ Both paths' individual success criteria met
- ✅ No conflicts or resource contention (parallel execution independent)
- ✅ Combined portfolio income: +$1,000–2,500/month (A) + +$500–1,500/year (C)
- ✅ Capital deployment: 27–33% (within 80% leverage ceiling)
- ✅ User approval obtained for both paths' go-live gates

---

## References

- **PHASE_4_OUTCOMES_DECISION_MATRIX.md** — Path selection logic; pre-filled scores
- **PHASE_4_IMMEDIATE_EXECUTION_PLAN.md** — Strategic overview; capital allocation; contingency scenarios
- **JUNE_24_VALIDATION_OUTCOME_DATA_SHEET.md** — User-fill validation metrics
- **VALIDATION_SUCCESS_METRICS_CHECKLIST.md** — Numeric success criteria (13:15–20:00 UTC June 24)

---

*Template created: 2026-06-24 (Session 4113, orchestrator autonomous prep)*  
*Status: PRODUCTION-READY — copy-paste safe; user fills decision gates and approval dates*  
*Update frequency: Daily during implementation (6/24–7/7); weekly during paper trading (7/8+)*
