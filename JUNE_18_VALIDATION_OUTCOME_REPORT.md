# June 18 Validation Outcome Report

**Validation Window**: 2026-06-18 13:30–20:00 UTC (market open/close)  
**Report Generated**: [TO BE FILLED]  
**Validation Duration**: 6.5 hours  

---

## Executive Summary

**Overall Verdict**: [PASS / CAUTION / FAIL — TO BE DETERMINED]

### Key Metrics at a Glance
- **Sessions Active**: [N/5 sessions generating signals]
- **Signal Health**: [% sessions with non-zero buy_prob]
- **HMM Regime Status**: [Priming success / regime initialization status]
- **Order Execution**: [N trades executed, N errors]
- **Critical Errors**: [0 / summary if >0]

---

## Per-Session Performance

### AAPL lgbm_ho
- **Buy Probability**: [range from Docker logs]
- **Trades Executed**: [count]
- **Signal Quality**: [OK / ISSUES]
- **Regime Status**: [initialized / None / other]
- **Notes**: [any anomalies]

### MSFT lgbm_ho
- **Buy Probability**: [range from Docker logs]
- **Trades Executed**: [count]
- **Signal Quality**: [OK / ISSUES]
- **Regime Status**: [initialized / None / other]
- **Notes**: [any anomalies]

### NVDA lgbm_ho
- **Buy Probability**: [range from Docker logs]
- **Trades Executed**: [count]
- **Signal Quality**: [OK / ISSUES]
- **Regime Status**: [initialized / None / other]
- **Notes**: [any anomalies]

### JPM ridge_wf
- **Buy Probability**: [range from Docker logs]
- **Trades Executed**: [count]
- **Signal Quality**: [OK / ISSUES]
- **Regime Status**: [initialized / None / other]
- **Notes**: [any anomalies]

### AMZN lgbm_ho
- **Buy Probability**: [range from Docker logs]
- **Trades Executed**: [count]
- **Signal Quality**: [OK / ISSUES]
- **Regime Status**: [initialized / None / other]
- **Notes**: [any anomalies]

---

## Critical Health Checks

### HMM Regime Detection
- **HMM Priming Success**: [YES / NO]
- **Time to Prime**: [minutes after market open]
- **Regime Values at Window Close**: [regime values for each session]
- **Priming Fragility Events**: [0 / summary if >0]

### Order ID Idempotency
- **Duplicate Order Errors**: [count from logs]
- **Alpaca Rejection Rate**: [0% / N%]
- **Order Execution Success Rate**: [%]
- **Idempotency Issues**: [NONE / summary]

### Infrastructure Stability
- **Container Health**: [healthy / crashed / degraded]
- **Database Errors**: [0 / summary if >0]
- **Alpaca API Errors**: [count by error code]
- **Market Clock Synchronization**: [OK / ISSUES]

---

## Option A Fix Validation

### HMM Three-Layer Warmup (Session 3825)
- ✅ **Layer 1 (90-bar feed)**: [SUCCESS / FAILURE]
- ✅ **Layer 2 (direct refit)**: [SUCCESS / FAILURE]
- ✅ **Layer 3 (bulk_update fallback)**: [SUCCESS / FAILURE]
- **Evidence**: [Docker log excerpts showing successful priming or failure mode]
- **Confidence in Fix**: [%]

### Order ID Idempotency (Session 3825)
- **Stable ID Generation**: [WORKING / ISSUES]
- **Database Persistence**: [WORKING / ISSUES]
- **Retry Behavior**: [CORRECT / ISSUES]
- **Confidence in Fix**: [%]

---

## Comparison to Baseline Expectations

**Expected Behavior** (from OPTION_A_VALIDATION_CHECKLIST.md):
- ✅ Regime initialized within 5 minutes of market open
- ✅ All 5 sessions generating buy_prob > 0 within first 30 min
- ✅ <5 duplicate order errors across all sessions
- ✅ >3 sessions executing at least 1 trade during window

**Actual Behavior**:
- [PASS / CAUTION / FAIL]
- [Description of how actual matched or diverged from expectations]

---

## Phase 4 Execution Recommendation

### Recommendation
**[IMMEDIATE EXPANSION / STAGED EXPANSION / CONTINGENCY PATH]**

### Reasoning
- **Option A fixes validated**: [% confidence]
- **Risk assessment**: [LOW / MEDIUM / HIGH]
- **Market readiness**: [READY / NEEDS WORK]
- **Timeline constraint**: [Phase 4 gates open / gates blocked]

### Next Steps (Approved Action)
1. [User decision: which Phase 4 path based on validation outcome]
2. [Orchestrator will execute this path immediately upon approval]
3. [Timeline for Phase 4 launch]

---

## Audit Trail

### Data Sources
- Docker logs: `docker logs stockbot --since 2026-06-18T13:30:00 | grep -E "buy_prob|regime|REFIT|order_error|trade"`
- Database: Trades table entries for 2026-06-18
- Jetson metrics: Disk, CPU, memory during market hours
- Alpaca API logs: Order submission and execution records

### Confidence Assessment
- **HMM Warmup Fix**: [% confidence this fix is sound]
- **Order Idempotency Fix**: [% confidence this fix is sound]
- **Overall Verdict Confidence**: [% confidence in PASS / CAUTION / FAIL judgment]

### Known Fragilities
- [List any observed edge cases or near-failures that need monitoring]
- [Any degradation that occurred but was within acceptable bounds]
- [Recommendations for Phase 4 monitoring]

---

## Decision Framework for Phase 4

### If PASS (≥4 sessions healthy, <5 errors, regime initialized)
**Action**: [IMMEDIATE EXPANSION per Phase 4 Immediate Execution Plan]
- File: `PHASE_4_IMMEDIATE_EXECUTION_PLAN.md` (execute immediately)
- Timeline: Phase 4 launch within 2 hours of validation window close
- Capital allocation: [per PHASE_4_CAPITAL_ALLOCATION_MODEL.md]

### If CAUTION (2-3 sessions healthy, 5-10 errors, regime patchy)
**Action**: [STAGED EXPANSION with monitoring]
- File: `PHASE_4_OPTIONS_FRAMEWORK.md` — select Staged scenario
- Risks: [which fragilities need additional monitoring]
- Contingency trigger: [if X happens, shift to contingency path]

### If FAIL (≤1 session healthy, >10 errors, regime never initializes)
**Action**: [CONTINGENCY PATH — investigate, delay Phase 4]
- Analysis: [what went wrong differently from Session 3825 assumptions]
- Next investigation: [what should be checked/debugged]
- Timeline: [when to retry validation]

---

## Notes for Phase 4 Planning

**Capital Deployment Window**: Once Phase 4 is approved, capital allocation per `PHASE_4_CAPITAL_ALLOCATION_MODEL.md` will determine:
- Expansion speed (immediate all 5 → 6-session config)
- Risk posture (conservative entry limits vs. normal)
- Monitoring intensity (hourly reviews vs. daily)

**Live Trading Readiness**: This validation determines whether the system is ready to:
- Add AAPL ridge_wf (currently shadow mode only)
- Expand to NVDA, GOOGL, AMZN sessions (4→7 sessions)
- Increase position size limits (from 5% to 8% per guidelines)

**Contingency Fallback**: If validation fails:
- Jetson engine remains healthy for continued observation
- No automatic rollback (Phase 4 just doesn't launch)
- Manual debugging window after validation closure

---

## Appendix: Validation Window Timeline

- **13:30 UTC**: Market open — all 5 sessions begin trading cycles
- **14:15 UTC**: Discord alert — HMM priming checkpoint (should show regime initialization)
- **14:30 UTC**: First 1-hour mark — assess signal quality across all sessions
- **18:00 UTC**: Mid-window checkpoint — verify sustained signal health
- **20:00 UTC**: Market close — final metrics, stop monitoring, prepare verdict
- **20:15 UTC**: Orchestrator post-validation analysis begins (Item 5 Exploration Queue)

---

**Report Status**: [PENDING VALIDATION WINDOW EXECUTION]
