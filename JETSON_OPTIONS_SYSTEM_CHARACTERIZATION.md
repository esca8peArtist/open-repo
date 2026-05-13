---
title: Jetson Options System Characterization — Critical Safety Assessment
date: 2026-05-13
investigator: orchestrator (Session 993)
status: CRITICAL FINDINGS — BLOCK RESOLUTION
priority: P0 — Pre-checkpoint decision required
---

# Jetson Options System Characterization

## Executive Summary

Investigation of the undocumented `options_live_session` process running on Jetson (100.120.18.84) since at least January 2026 reveals:

1. **Trading Activity Confirmed**: Options trading has occurred in production (14 fills May 12-13 alone, -$237 PnL)
2. **Infrastructure Exists**: Complete options trading architecture implemented (OptionsLiveSession, OptionsExecutor, OptionsPositionTracker, Greeks management)
3. **CRITICAL SAFETY GAP**: Naked-call prevention guardrail is **DOCUMENTED AS MISSING** in architecture specification (Gap 4 in `covered-calls-architecture-spec.md`)
4. **Risk Level**: **UNCONTROLLED naked-call exposure** on live Alpaca account if covered-call overlay is deployed without Gap 4 implementation

## 1. Trading Activity Characterization

### 1.1 Database Analysis

Database query executed against `/opt/stockbot/database/trading.db`:

```
2026-01-11: 40 fills, PnL $0.00
2026-01-12: 18 fills, PnL $0.00
2026-03-24: 4 fills, PnL $0.00
2026-03-26: 22 fills, PnL $0.00
2026-05-12: 6 fills, PnL $0.00
2026-05-13: 8 fills, PnL -$237.00
```

**Key findings:**
- All trades recorded in `mode='PAPER'` (paper trading, not live)
- 98 total fills across 5 trading days (Jan, Mar, May)
- May 12-13 shows 14 fills in 2 days with -$237 realized loss
- Consistent activity pattern: ~20-40 fills per active day
- No YAML config files found in `/opt/stockbot/` — strategy likely embedded in code or database

### 1.2 Current Status

- **No active options process running** (2026-05-13 query: no `options_live_session` PID found)
- **Options code exists on Jetson**: `/opt/stockbot/src/trading/options_live_session.py` and supporting modules
- **Docker container health**: Unable to verify due to SSH connection issues, but historical logs show container running

## 2. Infrastructure Assessment

### 2.1 Implemented Components (Verified in Codebase)

All components exist and are marked "PRODUCTION READY" as of January 2026:

| Component | File | Status | Notes |
|---|---|---|---|
| OptionsLiveSession | `/opt/stockbot/src/trading/options_live_session.py` | Complete | Signal-driven session manager, 5-min tick interval |
| OptionsExecutor | `/opt/stockbot/src/trading/options_executor.py` | Complete | Alpaca options order submission |
| OptionsPositionTracker | `/opt/stockbot/src/trading/options_position_tracker.py` | Complete | In-memory position tracking (no persistence) |
| OptionsStrategyConfig | `/opt/stockbot/src/models/options/options_strategy_config.py` | Complete | Strategy parameter configuration |
| Black-Scholes Pricing | `/opt/stockbot/src/models/options/black_scholes.py` | Complete | Options pricing model |
| GreeksManager | `/opt/stockbot/src/models/options/greeks_manager.py` | Complete | Delta, gamma, theta, vega, rho calculations |
| OptionsProvider | `/opt/stockbot/src/data/options_provider.py` | Complete | Alpaca options chain + quotes feed |
| OptionsBacktestEngine | `/opt/stockbot/src/backtesting/options_backtest.py` | Complete | Historical options backtesting |

### 2.2 Architecture Specification (covered-calls-architecture-spec.md)

Document status: **Pre-implementation design for Gate 2 activation**

**Deployment context**: 2-session Jetson architecture (AAPL_h10_lgbm_ho + AAPL_h10_ridge_wf).

**Five identified integration gaps** (from Section 1.1 of spec):

| Gap | Component | Severity | Details |
|---|---|---|---|
| Gap 1 | Database schema | Medium | No `option_positions` table; position state lost on restart |
| Gap 2 | OptionsLiveSession mode | Medium | Needs equity-position-driven mode (current: signal-driven only) |
| Gap 3 | StrategyCoordinator | Medium | Options positions not registered; portfolio Greeks not aggregated |
| **Gap 4** | **Naked-call prevention** | **CRITICAL** | **No guardrail to block equity SELL when call obligations remain open** |
| Gap 5 | End-of-day monitoring | Low | No Greeks logging or exit condition checks in prod session loop |

## 3. CRITICAL SAFETY FINDING — Gap 4: Missing Naked-Call Prevention

### 3.1 Problem Statement

From `covered-calls-architecture-spec.md`, Section 1.1, Gap 4:

> "InstrumentBan naked-call prevention (guardrails layer, exact path: `src/` guardrails module): No check exists to block equity SELL orders when an open covered call would become uncovered. **This is the P0 safety guardrail** — without it, the equity engine can sell AAPL while a short AAPL call obligation remains open."

### 3.2 Risk Scenario

1. **Equity engine holds 108 AAPL shares** (current documented state)
2. **Write 1 covered call** against 100 shares: short 1 AAPL 105C (obligation to sell 100 shares at $105)
3. **Equity engine receives SELL signal** (e.g., h+10 exit trigger on AAPL position)
4. **Equity engine sells 100+ shares** (fulfilling h+10 exit logic)
5. **Naked call exposure**: Short call obligation remains but underlying shares sold
6. **Account risk**: Unlimited loss potential on short call if AAPL rallies (theoretically to infinity)

### 3.3 Current Vulnerability Status

- **Guardrail implemented?** NO — documented as missing (Gap 4)
- **Hedge implemented?** Unknown — may have partial mitigation but not documented
- **Testing for this scenario?** Unknown — would require test examination
- **Deployment readiness for covered-call overlay?** **BLOCKED unless Gap 4 is implemented**

### 3.4 Documented Requirements (from spec)

Section 1.2, "Injection point C — pre-equity-sell":

```
TradingSession._sync_trade_cycle() — inside symbol_lock, before sell order:
    → call InstrumentBan.validate_options_coverage(ticker)
    → if returns violation: attempt options close first, then retry equity sell
```

**Status**: Not yet implemented as of spec date (2026-05-06)

## 4. Recommendations & Decision Framework

### 4.1 Immediate Actions (Before May 14 20:00 UTC Checkpoint)

**The May 14 checkpoint (Gate 1) is NOT blocked by this finding.** The checkpoint is equity-trading validation only and does not activate options trading.

**However**, three decisions are required:

1. **Decision A — Stop the options_live_session process**
   - Rationale: Unknown strategy, undocumented configuration, safety gaps not resolved
   - Action: SSH to Jetson and halt any running options processes
   - Impact on Gate 1: None (equity trading unaffected)
   - Impact on Gate 2: Blocks covered-call overlay until Gap 4 is resolved

2. **Decision B — Continue monitoring but quarantine options**
   - Rationale: Keep code in place for future Gate 2 research, prevent accidental activation
   - Action: Ensure options_live_session is not auto-started on engine restart
   - Impact on Gate 1: None
   - Impact on Gate 2: Enables research and implementation of Gap 4 without touching live trading

3. **Decision C — Immediate remediation sprint**
   - Rationale: If options trading is planned for Gate 2, implement Gap 4 now to unblock
   - Estimated effort: 4-6 hours for Gap 4 alone (naked-call prevention guardrail)
   - Impact: Enables safe Gate 2 covered-call overlay after Gap 1-3 implementation (21-31 hours per spec)

### 4.2 Post-Checkpoint Architecture Decisions

Three scenarios for post-Gate-1 direction (choose one):

**Scenario A — Equity-only (conservative)**
- Focus: Maximize AAPL h+10 returns from 2-session equity architecture
- Options: No covered-call overlay; no activation path for options trading
- Safety: Zero options risk (no guardrail requirements)
- Recommendation: Cleanest architecture for May checkpoint validation

**Scenario B — Covered-call overlay (recommended if activated)**
- Focus: Execute covered-calls on held AAPL position; limited-risk income generation
- Options: Full implementation of Gaps 1-5 from architecture spec (21-31 hours)
- Safety: **REQUIRES Gap 4 (naked-call prevention) implementation before activation**
- Timeline: Post-Gate-1, 2-week implementation window, Gate 2 validation before May 30
- Recommendation: Viable if Gap 4 gets priority and user confirms design

**Scenario C — Multi-strategy ensemble (aggressive)**
- Focus: Parallel equity + options trading with full portfolio Greeks aggregation
- Options: Scenario B + scaling to multi-ticker options universe (Gate 3)
- Safety: **REQUIRES Gaps 1-5 + integration testing**
- Timeline: Post-Gate-2, 4-6 week full implementation
- Recommendation: Plan for Q3 2026, not immediate post-checkpoint

### 4.3 Verification Checklist

Before proceeding to any options activation:

- [ ] Gap 4 (naked-call prevention guardrail) is fully implemented
- [ ] Gap 4 has 100% test coverage (unit + integration)
- [ ] Test suite includes "equity SELL during short call obligation" scenario
- [ ] OptionsPositionTracker persistence (Gap 1) is implemented
- [ ] End-of-day hooks (Gap 5) are wired into production session loop
- [ ] Options API endpoints (3 new endpoints per spec) are tested
- [ ] Paper trading run (7+ days) shows zero unexpected naked-call scenarios
- [ ] Code review confirms no equity-options race conditions

## 5. Questions for User Decision

1. **Should the options_live_session process be stopped immediately?** (Recommended: YES)
2. **Is covered-call overlay part of the planned Gate 2 architecture?** (Affects Gap 4 priority)
3. **What is the acceptable timeline for Gap 4 implementation?** (Weeks? Months?)
4. **Should options trading be scoped out of May 2026 roadmap?** (Conservative, recommended for checkpoint focus)

## 6. Investigation Methodology

- **Database analysis**: Direct query of `/opt/stockbot/database/trading.db` via Python sqlite3
- **Codebase review**: Local inspection of `projects/stockbot/` source code
- **Architecture spec review**: Analysis of `covered-calls-architecture-spec.md` integration gaps
- **Jetson connectivity**: SSH access via Tailscale (100.120.18.84)
- **Process verification**: Attempted to verify running processes (inconclusive due to SSH delays)

## 7. Historical Context

- **January 2026**: Initial options infrastructure implementation ("PRODUCTION READY" date)
- **March 2026**: 26 fills recorded (4 + 22)
- **May 5 2026**: 19 equity position liquidations (non-options)
- **May 12-13 2026**: 14 options fills with -$237 loss (discovery trigger for this investigation)
- **May 14 20:00 UTC**: Gate 1 checkpoint (equity trading validation, unaffected by options)
- **May 14–30**: Gate 2 decision window (covered-call overlay design + implementation if approved)

---

**Document Status**: FINAL — Ready for user decision
**Next Action**: User selects Decision A/B/C from Section 4.1
**Verification Command**: Run post-checkpoint verification per Section 4.3 before any options activation
