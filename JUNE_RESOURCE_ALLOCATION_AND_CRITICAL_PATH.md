# June 1–July 15 Resource Allocation and Critical Path Analysis

**Document status**: Item 32 orchestrator-level pre-staging, May 22 10:30 UTC | Confidence: High

This document integrates post-May-22-checkpoint decisions with resource constraints to determine the June 1–July 15 execution path for systems-resilience, open-repo, and stockbot.

---

## Executive Summary: Three Scenarios

| Scenario | Trigger | Stockbot Path | Systems-Resilience Path | Open-Repo Path | Resource Conflict | Recommended |
|----------|---------|---|---|---|---|---|
| **A: Lever B PASS** | May 22 20:00 UTC checkpoint outcome is Lever B activation success | Gate 2 multi-ticker expansion GO (June 1–15: expand to 2–3 new tickers, train models) | Phase 5 Hybrid (Wave 1 pub Jun 1–5, Phase 6 framework Jun 5–15, Wave 2 author Jun 10+) | Phase 5.1 production (Jun 5–10 validation, Jun 15 deploy) | MEDIUM (stockbot author hours overlap Phase 5 Wave 2) | Strategic parallel if stocks trading is secondary priority |
| **B: Lever B FAIL + Option B1** | May 22 20:00 UTC outcome is Lever B fails; escalate to covered-call overlay | Rapid revert (May 22–23: Lever A restore, verify 2-session state) + Option B1 options infrastructure (Gaps 1+2+4, 17 hrs, Jun 1–10) | Phase 5 Hybrid unchanged (research is independent) | Phase 5.1 production unchanged | LOW (options work is isolated from Wave 2) | All projects proceed in parallel; no contention |
| **C: Checkpoint delayed or decision pending** | May 22 20:00 UTC checkpoint is inconclusive or user decision awaited | Defer stockbot Gate 2 to June 5 decision window; maintain current 2-session live trading | Phase 5 Hybrid unchanged | Phase 5.1 production unchanged | LOW (stockbot is idle, not consuming author hours) | Default for caution; enables all other work to proceed |

---

## Scenario A: Lever B PASS (Gate 2 Expansion GO)

**Trigger**: May 22 checkpoint outcome is Lever B HMM regime masking successful (both AAPL sessions show improved exit timing and position accuracy).

**Stockbot work** (Jun 1–15):
- June 1–3: Verify Lever B state on production (ensure config is committed, no drift)
- June 3–5: Identify 2 new ticker candidates from Phase 3 framework (MSFT, NVDA, or per ranking)
- June 5–10: Train models for new tickers (2 sessions × 2 tickers = 4 new sessions, 4 new models)
  - Estimate: 20 hours research + model selection; 40 hours backtest/validation; total ~60 hours
- June 10–15: Deploy new sessions to Jetson; validate multi-ticker portfolio behavior (Edge cases: correlation clustering, drawdown thresholds, capital reallocation)
  - Estimate: 16 hours deployment + testing
- **Total stockbot effort June 1–15**: ~76 hours

**Author capacity required**:
- Stockbot model training / backtesting: 40 hours (concentrated Jun 5–10)
- Systems-resilience Wave 2 writing: 80 hours (spread Jun 10–Jul 10, but 40 hours in Jun)
- **Conflict**: Both need substantial author hours in June. If author capacity is 20–30 hrs/week (100–120 hrs/month):
  - June: 40 hrs stockbot + 40 hrs Wave 2 = 80 hours, fits in 100–120 hrs monthly capacity (20% reserve)
  - July: 30 hrs Wave 2 polish + 20 hrs Phase 6 = 50 hours, ample capacity
  - **Resolution**: Feasible if author sustains 20 hrs/week both projects; medium fatigue risk from context-switching

**Systems-resilience path**:
- Phase 5 Hybrid sequence unchanged (Wave 1 publication Jun 1–5, Phase 6 framework Jun 5–15, Wave 2 author Jun 10–Jul 10)
- No dependency on stockbot; research is independent

**Open-repo path**:
- Phase 5.1 activation unchanged (validation Jun 5–10, production deployment Jun 15)
- No dependency on stockbot

**Critical path**:
1. Jun 1: User approves Wave 1 publication + stockbot Gate 2 expansion GO
2. Jun 1–5: Wave 1 published; stockbot candidates identified
3. Jun 5–10: Phase 6 framework completed; stockbot models trained
4. Jun 10–15: Wave 2 author begins; new sessions deployed; Phase 5.1 moved to production
5. Jun 20: Phase 6 framework validated; Phase 5.1 stable
6. Jul 10: Wave 2 draft completed; stockbot expanded state verified
7. Jul 15: Wave 2 + Phase 6 published jointly

**Risk assessment**: MEDIUM
- Author must sustain dual-track effort (stockbot + Wave 2) Jun 5–10 without dropping either
- Stockbot model training might reveal issues (Gaps in new-ticker feature engineering) → debugging delays Wave 2 author
- Contingency: If stockbot training reveals >10 hours of unexpected work, defer Wave 2 start to Jun 15 (slip both projects by 1 week)

---

## Scenario B: Lever B FAIL + Option B1 (Covered-Call Overlay)

**Trigger**: May 22 checkpoint outcome shows Lever B HMM regime masking did NOT improve exit timing; positions still held past h+10; Lever A revert required + Option B1 (covered-call overlay exploration).

**Stockbot work** (May 22–Jun 10):
- May 22–23 (emergency): Lever A revert + verification (1–2 hours; commands in BLOCKED.md)
- May 23–31: Post-revert stability validation (ensure 2-session state is stable and profitable)
  - Estimate: 8 hours automated monitoring + manual spot-checks
- June 1–3: Option B1 decision (covered-call overlay feasibility analysis)
  - Is adding call-writing to AAPL position worth the complexity? Decision framework in `GATE_2_CONTINGENCY_ARCHITECTURE.md`
  - Estimate: 4 hours analysis + decision
- June 3–10: If Option B1 approved, implement Gaps 1+2+4 (database persistence, signal integration, naked-call prevention guardrail)
  - Estimate: 17 hours implementation + testing
- **Total stockbot effort May 22–Jun 10**: ~30 hours (concentrated May 22–23 emergency + Jun 3–10 implementation)

**Author capacity required**:
- Stockbot Option B1 implementation: 17 hours (concentrated Jun 3–10, afternoons)
- Systems-resilience Wave 2 writing: 80 hours (Jun 10–Jul 10, primary focus)
- **Conflict**: LOW. Stockbot implementation is 17 hours over 1 week (spread mornings/afternoons); Wave 2 author can focus on Wave 2 work.

**Systems-resilience path**:
- Phase 5 Hybrid unchanged; no dependencies on stockbot

**Open-repo path**:
- Phase 5.1 activation unchanged

**Critical path**:
1. May 22–23: Lever A revert + stabilization
2. May 23–31: Validation period (no user decisions needed)
3. Jun 1: User approves Wave 1 publication + decides on Option B1 (covered calls yes/no)
4. Jun 1–5: Wave 1 published; Phase 6 framework started
5. Jun 3–10: If Option B1 approved, implement Gaps 1+2+4 (parallel to Wave 2 prep)
6. Jun 10–15: Wave 2 author begins; Phase 5.1 validation
7. Jul 10: Wave 2 draft completed; Option B1 (if implemented) has 3+ weeks runtime for validation
8. Jul 15: Wave 2 + Phase 6 published

**Risk assessment**: LOW
- Stockbot emergency revert is low-risk (Lever A is proven code path)
- Option B1 implementation (17 hours) does not conflict with Wave 2 work
- If Option B1 fails mid-implementation (June 5), can defer to July 1 without delaying Wave 2

---

## Scenario C: Checkpoint Delayed or Decision Pending (Caution)

**Trigger**: May 22 20:00 UTC checkpoint does not complete on schedule (infrastructure issue, user request) or outcome is inconclusive (requires additional analysis to decide Lever A revert vs B1 escalation).

**Stockbot work** (June 1–15):
- June 1–5: Maintain current 2-session live trading (AAPL lgbm_ho + AAPL ridge_wf)
- June 5: User provides checkpoint decision + Gate 2 direction
- June 5–15: Execute decision (Lever A only, Option B1, or Lever B re-attempt)
  - Estimate: 0 hours if Lever A only; 17 hours if Option B1 implementation; 40 hours if Lever B re-attempt
  
**Systems-resilience path**:
- Phase 5 Hybrid unchanged; checkpoint delay has no impact

**Open-repo path**:
- Phase 5.1 activation unchanged; independent of stockbot

**Critical path**:
1. Jun 1–5: User checkpoint review + Gate 2 decision
2. Jun 5 onwards: Execute Gate 2 decision (option A/B/C)
3. Jun 1–5 parallel: Wave 1 publication + Phase 6 framework (proceeds regardless of stockbot)
4. Jun 10–15: Wave 2 author begins (proceeds regardless of stockbot decision)
5. Jul 15: Wave 2 + Phase 6 published

**Risk assessment**: LOW
- All non-stockbot projects proceed unaffected
- Stockbot decision delay is 1 week, no cascading impact
- Best path if uncertainty exists; provides additional analysis time

---

## Resource Allocation Framework

### June 1–15 Author Capacity Model

Assume 1 primary author available:
- **Typical capacity**: 25–30 hours/week (100–120 hours/month)
- **Committed capacity**: 20 hours/week minimum (80 hours/month) for Wave 2 writing

| Project | June Hours | July Hours | Author | Notes |
|---------|---|---|---|---|
| **Scenario A: Lever B PASS** | | | | |
| — Stockbot (model training + backtest) | 40 | 0 | Model-focused dev | Concentrated Jun 5–10; backtest automation |
| — Wave 2 writing (Waves 2 outline + draft) | 40 | 50 | Primary author | Jun 10+ start; distributed Jun 10–Jul 10 |
| — Phase 6 editorial integration | 30 | 10 | Editor/secondary | Jun 5–15 framework; Jul final polish |
| — Wave 1 publication | 15 | 0 | Editor | Jun 1–5, minimal; publication support |
| **Total** | **125 hours** | **60 hours** | **2 people (1 primary + 1 editor)** | **Feasible if author >20 hrs/week** |
| | | | | |
| **Scenario B: Lever B FAIL + Option B1** | | | | |
| — Stockbot (Option B1 Gaps implementation) | 17 | 10 | Stockbot dev | Jun 3–10 + validation; low conflict with Wave 2 |
| — Wave 2 writing | 40 | 50 | Primary author | Uninterrupted; full focus |
| — Phase 6 editorial | 30 | 10 | Editor | Concurrent, low impact |
| — Wave 1 publication | 15 | 0 | Editor | Minimal |
| **Total** | **102 hours** | **70 hours** | **2 people** | **Low contention; stockbot doesn't block Wave 2** |
| | | | | |
| **Scenario C: Caution (Decision Pending)** | | | | |
| — Stockbot (idle; maintenance only) | 5 | 0 | Ops | Live trading monitoring; low effort |
| — Wave 2 writing | 40 | 50 | Primary author | Uninterrupted focus |
| — Phase 6 editorial | 30 | 10 | Editor | Concurrent |
| — Wave 1 publication | 15 | 0 | Editor | Minimal |
| **Total** | **90 hours** | **60 hours** | **1–2 people** | **Lowest contention; recommended if uncertain** |

**Capacity verdict**:
- **Scenario A**: 125 hours in June requires 2 people or author >25 hrs/week. Feasible but stressful.
- **Scenario B**: 102 hours in June is comfortable for 2 people at 20–25 hrs/week each.
- **Scenario C**: 90 hours in June is sustainable; lowest risk.

**Recommendation**: Scenario B or C preferred. Scenario A feasible only if author capacity >25 hrs/week is confirmed.

---

## Post-Checkpoint Decision Tree

### May 22 20:00 UTC Checkpoint Outcome

```
┌─ Checkpoint complete at 20:00 UTC
│
├─ LEVER B ACTIVATED ✅
│  ├─ Both AAPL sessions (lgbm_ho + ridge_wf) show Lever B behavior ✓
│  └─ → Scenario A: Gate 2 expansion GO
│     └─ Jun 1 user decision: Approve 2–3 new ticker expansion?
│        ├─ YES → Allocate 40 hrs stockbot Jun 5–10; 80 hrs Wave 2 Jun 10–Jul 10
│        └─ NO → Defer expansion to June 15; Wave 2 author gets full focus Jun 1+
│
├─ LEVER B FAILED ❌ (exit timing still poor)
│  ├─ Sessions reverted to Lever A (2-session, AAPL only)
│  └─ → Scenario B: Option B1 (covered-call overlay) exploration
│     └─ Jun 1 user decision: Implement Option B1?
│        ├─ YES → Allocate 17 hrs stockbot Jun 3–10 (Gaps 1+2+4 implementation)
│        ├─ NO → Defer to July 15; stockbot idle in June
│        └─ MAYBE → Defer decision to Jun 5; allocate 4 hrs Jun 1–5 for deeper analysis
│
└─ CHECKPOINT DELAYED (TBD)
   └─ → Scenario C: Caution
      └─ Jun 1: Maintain 2-session status quo
      └─ Jun 5: Revisit checkpoint decision + Gate 2 direction
```

### Recommended Decision Points (User Input Needed Jun 1)

1. **Wave 1 publication approval**
   - User decision: Is Wave 1 production-ready for public release?
   - Impact: Enables Wave 2 author context (Wave 1 is already public); no delay

2. **Stockbot Gate 2 direction** (determined by May 22 outcome, but user confirms scope)
   - If Lever B PASS: Approve new-ticker expansion? (Yes/No/Defer to Jun 15)
   - If Lever B FAIL: Approve Option B1 covered-call implementation? (Yes/No/Defer)
   - Impact: Determines stockbot author hours Jun 1–15 (0 to 60 hours range)

3. **Author availability confirmation**
   - Confirm Wave 2 primary author is committed Jun 1–Jul 10 (80+ hours needed)
   - Confirm stockbot developer (if Gate 2 expansion approved) available Jun 5–10 (40 hours)
   - Impact: Determines feasibility of parallel projects

4. **Phase 5.1 + 5.2 activation GO**
   - User approval: Merge feature branch; proceed to Phase 5.1 activation?
   - Impact: Activates June 5–15 validation window; triggers Phase 5.2 kickoff Jun 15

---

## Critical Path Summary (All Scenarios)

| Milestone | Date | Scenario A | Scenario B | Scenario C | Owner |
|-----------|------|-----------|-----------|-----------|-------|
| **May 22 20:00 UTC** | May 22 | Checkpoint outcome (PASS/FAIL) | Checkpoint outcome | Checkpoint decision | Orchestrator |
| **Wave 1 publication decision** | Jun 1 | User approves | User approves | User approves | User |
| **Stockbot Gate 2 direction** | Jun 1 | Expansion GO | Option B1 yes/no | Decision pending | User |
| **Wave 2 author onboarded** | Jun 1 | Confirm ready | Confirm ready | Confirm ready | Manager |
| **Wave 1 published** | Jun 5 | DONE | DONE | DONE | Editor |
| **Phase 6 framework complete** | Jun 15 | DONE | DONE | DONE | Editor |
| **Stockbot expansion deployed** (A only) | Jun 15 | 4 new sessions live | N/A | N/A | Stockbot dev |
| **Option B1 Gaps implemented** (B only) | Jun 10 | N/A | DONE | N/A | Stockbot dev |
| **Phase 5.1 in production** | Jun 15 | DONE | DONE | DONE | Ops |
| **Wave 2 draft complete** | Jul 10 | DONE | DONE | DONE | Author |
| **Wave 2 + Phase 6 published** | Jul 15 | DONE | DONE | DONE | Editor |
| **Phase 5.2 (Medical) implementation GO** | Jun 15 | IF capacity | If capacity | If capacity | Manager |

**Overall June 1–Jul 15 critical path**: Wave 1 publication (earliest) → Phase 6 framework (mid-June gate) → Wave 2 completion (July 10) → Joint publication (July 15)

**Stockbot is critical path only in Scenario A** (Gate 2 expansion delays Wave 2 author by 5–10 days if training reveals issues). **Scenarios B and C have stockbot as separate track** (no impact on Wave 2).

---

## Recommendation for June 1 Planning Session

### Pre-Decision Checklist (May 22 evening)

- [ ] Checkpoint outcome received and documented
- [ ] Lever A vs B status confirmed (or decision deferred to Jun 5)
- [ ] All three scenario decision trees reviewed by user
- [ ] Author/developer capacity confirmed for chosen scenario

### Decision Inputs Needed from User

1. **Wave 1 publication**: Approved for public release? (Y/N)
2. **Stockbot Gate 2 expansion** (if Lever B PASS): Yes / No / Defer to Jun 15?
3. **Option B1 covered-calls** (if Lever B FAIL): Yes / No / Defer?
4. **Capacity confirmation**: Can primary author sustain 20 hrs/week Wave 2 Jun 1–Jul 10?

### Contingency Trigger

If by June 10:
- Stockbot model training reveals >20 hours unexpected work → defer Phase 5 Wave 2 to July 1
- Phase 6 framework validation reveals content gaps → extend framework by 1 week, compress Wave 2 timeline
- Author becomes unavailable → defer Wave 2 to July 15; publish Phase 6 July 20
- Phase 5.1 production deployment reveals P0 bugs → delay Phase 5.2 by 1 week; rollback if necessary

---

## Appendix: Detailed Hour Estimates

### Scenario A: Stockbot Expansion (76 hours)

- Candidate identification + ranking (3 hrs)
- Feature engineering for new tickers (12 hrs)
- Model training (both new tickers, both HMM regimes): 20 hrs
- Backtesting (4 new sessions, 250–500 training bars each): 16 hrs
- Validation + edge case testing: 8 hrs
- Deployment to Jetson + config staging: 6 hrs
- Live monitoring + minor fixes: 11 hrs
- **Total**: 76 hours

### Scenario B: Option B1 Gaps Implementation (17 hours)

- Gap 1 (database persistence): 4 hrs
- Gap 2 (OptionsLiveSession mode overlay): 6 hrs
- Gap 4 (naked-call prevention guardrail): 5 hrs
- Testing + integration: 2 hrs
- **Total**: 17 hours (concentrated Jun 3–10)

### Systems-Resilience: Phase 5 Hybrid (120 hours)

- Wave 1 publication: 15 hrs
- Phase 6 editorial (combine 3 research documents): 30 hrs
- Wave 2 author writing (outline → draft): 75 hrs
  - Distributed Jun 10–Jul 10 (40 hrs in Jun, 35 hrs in Jul)
- **Total**: 120 hours

### Open-Repo: Phase 5.1 Activation (21 hours)

- Pre-merge verification: 4 hrs
- Merge + rebase (if needed): 2 hrs
- Post-merge validation: 6 hrs
- Staging deployment: 3 hrs
- Production deployment + monitoring: 6 hrs
- **Total**: 21 hours (concentrated Jun 1–15)
