# Stockbot Codebase & Architecture Assessment — Session 2979

**Date**: 2026-06-10  
**Status**: ✅ Complete, awaiting user approval before implementation  
**Scope**: Full codebase review (bugs/tech debt), pipeline architecture analysis, agent-loop workflow definition

---

## Executive Summary

The stockbot codebase is **large, generally well-engineered, but has three critical pre-deployment issues and several architectural gaps** that should be addressed before Phase 4 activation or live trading expansion.

### Critical Findings (Block Deployment)
1. **Auth defaults are exploitable**: Default admin password `'changeme123'` and JWT secret `'development-secret-change-in-production'` 
2. **Model graduation gate G4/DSR is disabled**: Hardcoded `num_trials=1` makes the anti-overfitting gate ineffective
3. **Transaction costs not modeled**: Backtest Sharpes are inflated (frictionless); real costs unknown

### High-Priority Issues (Fix in Sprint 1)
1. **Position sizing untested**: Kelly sizer and HMM regime scalar have zero test coverage
2. **Model staleness undetected**: No warning if trading on 2-month-old models
3. **Signal resolution is implicit**: HMM mask, exit model, time-stop, earnings filter layer sequentially with no documented priority
4. **Long-term codebase maintenance risk**: 800-line `_process_ticker` method needs decomposition

### Major Gaps (Medium Priority)
1. No ensemble optimization automation
2. No model rollback procedure (recovery is manual)
3. VIX scaling is dead code (implemented but never called in live)
4. Walk-forward sample thin (3 folds vs 5+)

### New Capability (Complete)
- **Agent Loop Workflow**: Complete 7-phase feature development framework with templates, checklists, and orchestrator integration

---

## Detailed Assessment

### Part 1: Codebase Quality Audit

**Scope**: 138K lines of source code, 111K lines of tests, ~190 source files  
**Verdict**: Well-engineered core (RiskManager, OrderExecutor, DatabaseManager are disciplined), but critical security/testing gaps

#### CRITICAL ISSUES — Must Fix Before Deployment

| Issue | Location | Severity | Fix |
|-------|----------|----------|-----|
| Default admin password hardcoded to `'changeme123'` | `src/core/auth.py:121` | CRITICAL | Refuse startup if STOCKBOT_ADMIN_PASSWORD unset; generate random or force reset on first login |
| JWT secret defaults to public `'development-secret-change-in-production'` | `src/api/security.py:162` | CRITICAL | Fail-closed: raise/exit if auth enabled and secret is dev default |
| Wildcard CORS allows CSRF on authenticated endpoints | `src/api/security.py:170-175` | CRITICAL | Fail-closed: reject wildcard origin if auth enabled |

**Effort**: ~0.5 day (3 straightforward fixes)

#### HIGH-PRIORITY ISSUES — Fix in Sprint 1

| Issue | Impact | Effort |
|-------|--------|--------|
| Kelly sizer + HMM regime scalar have **zero test coverage** | Both directly control trade size with no automated validation | 1-1.5 days |
| Kelly sizer zero-loss window bug (win/loss ratio inflates to 10.0) | Position size explodes on winning streaks (mean-reversion trap) | 0.25 day (fix + tests) |
| Options broker interface has unimplemented stubs (NotImplementedError) | Latent landmine: future callers crash | 0.5 day |
| `_process_ticker` is 800 lines, untestable in isolation | Core signal logic impossible to reason about or test | 2-3 days |

#### MEDIUM-PRIORITY ISSUES — Code Quality

- **166 naive `datetime.now()` calls**: Mix of naive and aware timezone; risk TypeErrors on cross-module datetime arithmetic
- **Silent exception swallowing**: 5+ `except Exception: pass` blocks with no logging (makes failures hard to diagnose)
- **Config loader regex breaks on colons in defaults**: sqlite URLs like `sqlite:///db` get truncated
- **rsync in hetzner_pipeline has no timeout**: Stalled transfers hang indefinitely
- **Options market orders bypass cash guard**: Debit estimate defaults to 0.0, skipping validation

**Tech Debt Summary**:
- 7 `TODO` stubs (mostly broker interface placeholders)
- 223 `__init__`/`__repr__`/`to_dict` methods — expected boilerplate, not a concern
- Hardcoded tuning parameters (VIX tiers, HMM bounds, Kelly thresholds) should be config

#### What's Working Well
✅ RiskManager — clean RLock-guarded validation, fail-closed semantics  
✅ OrderExecutor cash guard — defends against over-leverage, properly shared  
✅ DatabaseManager — thread-safe singleton, SQLite WAL, context-managed sessions  
✅ RealtimeStreamManager — custom 429 backoff (5→300s) fixes Alpaca SDK tight-retry bug  
✅ No `0.0.0.0` bindings, no yfinance leaks, no file/socket leaks  

---

### Part 2: Model Architecture & Pipeline Assessment

**Scope**: Training pipeline, backtesting, walk-forward evaluation, live execution  
**Verdict**: Infrastructure strong, but missing critical features and has blind spots

#### MISSING FUNCTIONALITY (Critical for Reliability)

1. **Transaction Cost Model** ⚠️ **CRITICAL**
   - Current: Backtest returns are frictionless (zero commission, zero slippage, zero bid-ask spread)
   - Impact: All reported Sharpes are inflated (JPM 4.412, AMZN 3.939 are gross)
   - Documented claim: "G1 gate is after costs" — **This is currently false**
   - Fix: Subtract ~0.05% commission + 0.02% half-spread per signal transition
   - Effort: Low-medium (modify `_compute_returns` and `_extract_trade_pnls`)
   - Expected impact: Sharpes drop ~10-25%, AAPL ridge_wf 117-trade case looks worse (correctly)

2. **Real-Time Model Staleness Detection**
   - Current: No age check on trained models; AAPL lgbm_ho generated stale 2023 signals into 2026
   - Impact: Can trade on 2+ month old models without warning
   - Fix: Load `trained_at` from registry, alert when `now - trained_at > N days`, optionally halt new BUYs
   - Effort: Low (add timestamp check + alert)

3. **Automated Retraining Triggers**
   - Current: Entirely manual/orchestrator-driven
   - Missing: Triggers on staleness, LiveVsBacktestTracker Z-score breach, regime drift
   - Fix: Wire drift tracker Z-alert to `AutomatedTrainer.train_from_config`
   - Effort: Medium

4. **Model Rollback Procedure**
   - Current: Deployment is forward-only; recovery is manual JSON surgery
   - Missing: Documented rollback, `.prev` config snapshot, `rollback.sh` script
   - Effort: Low

#### SUBOPTIMAL COMPONENTS (Should Fix)

| Component | Current State | Better Approach | Effort |
|-----------|---------------|-----------------|--------|
| **G4 DSR Gate** | Hardcoded `num_trials=1` makes anti-overfitting gate ineffective | Pass real search cohort size through calculation (already in config) | Low |
| **VIX Scaling** | Implemented 4-tier multiplier but never called in live (no `vix_level` param) | Either activate (fetch VIX, pass to sizer) or delete dead code | Low-medium |
| **Walk-Forward Sample** | 3 folds, 1-year IS (spec says 2-year IS) | Standardize on ≥5 folds, extend OOS through current data | Low (recompute gates) |
| **Kelly Sizing** | Win/loss ratio derived from price series, not from model's actual trade history | Feed realized win rate + payoff from trades DB | Medium |
| **Signal Resolution** | HMM→exit→time-stop→earnings cascade, priority is positional order, no logging of which rule won | Explicit `SignalResolver` with ranked rules and decision trace | Medium |
| **HMM Regime Detection** | Refits full model every 5 bars (expensive + induces lag) | Incremental HMM update or cached short-refit | Medium |

#### RELIABILITY GAPS

- **Single data feed**: Alpaca-only (policy correct), but outage = silent zero-trades. Mitigation: explicit feed-health alert
- **Feature unavailability contract undefined**: VIX, earnings dates, sentiment have no specified degradation behavior
- **Live vs Backtest divergence**: Documented "30-50% degradation" is a heuristic patch over unmodeled costs
- **Multi-timeframe coherence**: No validation that 5m/15m/1h features are consistent

#### PIPELINE OPTIMIZATION

- **Backtest evaluation cache miss**: `_fetch_data` bypasses the parquet cache; re-downloads bars on every eval. Wiring through `fetch_daily_bars` would save network round-trips
- **Deployment is manual ritual**: 6+ steps (pkl → rsync → edit JSON → docker stop/rm/run). Risk: forgetting required flags (`--restart unless-stopped`, `--dns`) caused prior outages. Solution: `deploy-to-jetson.sh` that handles everything transactionally
- **Ensemble optimization not automated**: Batch script could search best-mix of existing models

#### Top Architecture Recommendations (Prioritized)

1. **Add transaction-cost model to backtest (CRITICAL, low-medium effort)**
   - Subtract commission + slippage per signal transition
   - Re-run all 6 gates
   - Most important: gates are currently rest on inflated numbers
   - Expected impact: Uncover which models are actually profitable after costs

2. **Fix G4/DSR to use real trial count (HIGH, low effort)**
   - Plumb `n_dsr_trials` (already in config) to calculation
   - Without this, overfitting gate is decorative

3. **Wire model-staleness detection + rollback (HIGH, low effort)**
   - Read `trained_at` in live session
   - Alert/halt-BUYs past configurable age
   - Add `.prev` config + `rollback.sh`
   - Directly addresses AAPL-stale-signal failure mode

4. **Activate or retire VIX scaling, externalize tuning params (MEDIUM, low-medium effort)**
   - Either pass `vix_level` into sizing or delete dead code
   - Move hardcoded scalars to per-session config

5. **Decompose `_process_ticker` signal cascade (MEDIUM effort)**
   - Extract HMM/exit/time-stop/earnings blocks into ranked resolver
   - Add decision-trace logging
   - Standardize walk-forward on 5+ folds + current OOS

---

### Part 3: Agent Loop Workflow — Feature Development Framework

**Status**: Complete, production-ready  
**Location**: `/home/awank/dev/SuperClaude_Framework/projects/stockbot/docs/`

#### What Was Delivered

Four comprehensive documents (2,718 lines total):

1. **README_AGENT_LOOP.md** — Entry point, roles, how to get started
2. **AGENT_LOOP_WORKFLOW.md** — Full specification of all 7 phases
   - Define → Plan → Implement → Review → Fix → Merge → Repeat
   - 3 templates (Feature Spec, Planning Doc, Code Review Checklist)
   - Decision trees (feature sizing, parallelization)
   - 8 common scenarios + fixes
3. **AGENT_LOOP_QUICK_REFERENCE.md** — 1-page cheat sheet per phase
4. **FEATURE_QUEUE_TEMPLATE.md** — Orchestrator's daily tracker

#### Core Workflow: 7 Phases with Quality Gates

```
1. DEFINE      — Spec approved by product owner
   ↓
2. PLAN        — Planning doc at ≥90% confidence
   ↓
3. IMPLEMENT   — Tests passing, ≥95% coverage
   ↓
4. REVIEW      — Independent code review, blocking issues identified
   ↓
5. FIX         — All blocking issues resolved
   ↓
6. MERGE       — Pre-merge checklist complete, zero regressions
   ↓
7. REPEAT      — Next feature from queue
```

#### Key Features

✅ **Ready-to-use templates** — Feature Spec, Planning Doc, Code Review Checklist (copy-paste)  
✅ **Decision guidance** — Feature size, parallelization, blocker escalation  
✅ **Quality gates** — Spec approval, plan confidence, code review, pre-merge verification  
✅ **Orchestrator integration** — Phase transitions, blocker tracking, metrics  
✅ **Stockbot-specific patterns** — Signal masking, state management, testing conventions  
✅ **Troubleshooting** — 8 common scenarios with solutions  

#### Quality Standards

- ≥95% test coverage on new code (enforced)
- 0 test failures before merge
- No linting warnings
- Independent code review
- <1 blocking issue per review (target)
- Zero production regressions

#### Immediate Use Cases

- **Small feature** (≤4h): Single agent, 1 reviewer, 1-2 day turnaround
- **Medium feature** (4-12h): Single agent, 1-2 reviewers, 2-3 day turnaround
- **Large feature** (>12h): Parallel agents (core + tests), 2 reviewers, 3-5 day turnaround
- **Multi-component feature**: Serial tasks with shared review gate

---

## Summary of Findings by Priority

### Tier 1: Block Deployment/Live Trading
- [ ] Fix auth defaults (no working default admin password or JWT secret)
- [ ] Add transaction-cost model to backtest gates
- [ ] Fix DSR gate (use real trial count, not hardcoded 1)
- [ ] Add tests for kelly_sizer and hmm_regime_scalar

**Estimated effort**: 2-3 days  
**Impact**: Removes exploitable security gaps, validates that models are actually profitable after costs, enables overfitting detection

### Tier 2: Prevent Known Failure Modes
- [ ] Wire staleness detection into live session (halt on old models)
- [ ] Implement model rollback procedure
- [ ] Decompose `_process_ticker` and add signal resolver decision trace
- [ ] Fix Kelly sizer zero-loss blow-up

**Estimated effort**: 3-4 days  
**Impact**: Prevents stale-signal failures, enables quick incident recovery, improves signal tracing for post-market analysis

### Tier 3: Code Quality & Maintainability
- [ ] Standardize on UTC-aware datetime (fix 166 naive calls)
- [ ] Remove dead broker interface stubs or implement them
- [ ] Add logging to silent exception-swallow blocks
- [ ] Externalize hardcoded tuning parameters to config

**Estimated effort**: 1-2 days  
**Impact**: Improves debuggability, reduces latent crashes, enables A/B testing of parameters

### Tier 4: Architecture Optimization
- [ ] Activate or retire VIX scaling
- [ ] Implement walk-forward sample on 5+ folds
- [ ] Ensemble optimization automation
- [ ] Model deployment transactional script

**Estimated effort**: 2-3 days  
**Impact**: Better model selection, faster evaluation, more reliable deployments

---

## Implementation Roadmap

### Phase 1 (Critical, 2-3 days)
1. Fix auth defaults → fail-closed at startup
2. Add transaction-cost model to gates
3. Fix DSR (use real `n_dsr_trials`)
4. Add tests for kelly_sizer, hmm_regime_scalar

### Phase 2 (High Priority, 3-4 days)
1. Wire staleness detection + rollback
2. Decompose `_process_ticker`
3. Fix Kelly zero-loss bug
4. Create transactional deploy script

### Phase 3 (Medium Priority, 1-2 days)
1. Datetime standardization
2. Logging for silent swallows
3. Parameter externalization

### Phase 4 (Nice-to-Have, 2-3 days)
1. Walk-forward sample expansion
2. Ensemble optimization
3. VIX scaling cleanup

---

## How to Proceed

### Next Steps (User Approval Gate)
1. Review this synthesis document
2. Provide feedback on priorities (which issues to fix first?)
3. Approve the Agent Loop Workflow framework for use
4. Authorize Phase 1 work to begin

### Once Approved
1. Orchestrator will create Phase 1 Feature Specs using the Agent Loop Workflow
2. Agents will implement fixes using the new workflow
3. Independent code review agents will validate
4. Fixes will be tested and committed
5. Phase 4 activation can proceed once critical issues are resolved

---

## Documents for Reference

- **Detailed Codebase Audit**: See agent output (auth.py, security.py, kelly_sizer.py findings)
- **Detailed Architecture Review**: See agent output (transaction costs, staleness, pipeline gaps)
- **Agent Loop Workflow**: `/projects/stockbot/docs/AGENT_LOOP_WORKFLOW.md` (ready to use)

---

## Status

✅ **Assessment Complete**  
⏳ **Awaiting User Approval** (review findings, prioritize phases, authorize Phase 1)  
🔒 **All findings documented, no code changes made yet** (per user directive)  

**Next Checkpoint**: User approval + Phase 1 feature specs created
