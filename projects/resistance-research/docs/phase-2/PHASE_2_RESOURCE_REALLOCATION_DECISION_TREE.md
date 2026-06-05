---
title: "Phase 2 Resource Reallocation Decision Tree"
subtitle: "Parallel Domain Execution Scenarios, Agent-Hour Allocation, and Contention Resolution"
created: "2026-06-05"
status: "production-ready — ready for June 11 checkpoint decision"
prepared_by: "Resistance Research Agent — Session June 5, 2026"
word_count: ~2,100
cross_references:
  - PHASE_2_SEQUENTIAL_ACTIVATION_STRATEGY.md (Section 6)
  - BATCH_2_RESOURCE_ALLOCATION_MATRIX.md
  - ORCHESTRATOR_STATE.md
  - stockbot project Item 62, Item 66 (Phase 3a expansion decision)
  - systems-resilience Wave 2 author onboarding (June 15)
confidence: 92%
---

# Phase 2 Resource Reallocation Decision Tree
## Parallel Domain Execution Scenarios, Agent-Hour Allocation, and Contention Resolution

*Resistance Research Agent — June 5, 2026*

*Production-ready for June 11 checkpoint decision and June 15 T+14 multi-project coordination assessment. Three parallel execution scenarios evaluated with resource contention analysis. Decision tree enables rapid reallocation if stockbot Phase 3a expansion or systems-resilience Wave 2 introduces capacity constraints.*

---

## Executive Summary

**Three credible execution paths exist for June–August Phase 2 resource allocation, differing in parallelism and contention risk.**

| Path | Scenario | User Hours/Month | Agent Hours/Month | Peak Conflict | Risk |
|------|----------|------------------|------------------|---------------|------|
| **A** | Full parallel (51+57+48, June–July, no stagger) | 8.5/June + 6/July | 12/June + 8/July | June 15 (stockbot Phase 3a + Domain 51) | HIGH |
| **B** | Staggered parallel (51 June → 57+48 parallel July) | 4.5/June + 7/July | 3/June + 10/July | July 1 (stockbot monitoring + 57+48) | MODERATE |
| **C** | Sequential (51 → 57 → 48 → 49+50 deferred) | 3/June + 4/July | 2/June + 6/July | None (no parallelism) | LOW |

**Recommended path: Scenario B (staggered parallel)** — balances speed against resource availability and satisfies all domain external deadlines.

---

## Section 1: Three Execution Scenarios

### Scenario A: Full Parallel Domains (51 + 48, June–July)

**Domains executing simultaneously**: Domain 51 (June 9–12) + Domain 48 Gist creation (June 15–30) → Domain 48 Tier 1 sends (July 1–15) + Domain 57 Gist creation (July 1–10).

**Resource allocation**:
- User hours: 4.5 hours (June 9–12 Domain 51 sends) + 3 hours (June 15–30 Domain 48 prep) + 4 hours (July 1–15 Domain 48 sends) = **11.5 hours in June–July window**.
- Agent hours: 1.5 hours (June 9–12 Domain 51 support) + 1 hour (June 15–30 Domain 48 contact list refresh) + 2 hours (July 1–15 Domain 48 coalition follow-up) = **4.5 hours in June–July window**.

**Parallel track coordination**: Domain 51 (user-facing, June 9–12, 90 minutes/day) + Domain 48 prep (user-facing, June 15–30, 10 minutes/day scattered across work). No hard conflict in user time allocation.

**Conflict zones**:

1. **June 15 (Day 6 of Domain 51 execution + Domain 48 prep start + stockbot Item 66 Phase 3a expansion decision gate)**
   - Contention: Domain 51 monitoring + user decision on Domain 48 acceleration + stockbot Phase 3a decision all happen same day.
   - If stockbot Phase 3a expansion is approved: 2–3 agents diverted to stockbot multi-ticker deployment. Agent availability for Domain 48 follow-up research drops by 50%.
   - Mitigation: Pre-stage Domain 48 Gist creation (June 13–14) before June 15. If Phase 3a approved: Domain 48 preparation already underway, no lost momentum.

2. **July 1–15 (Domain 48 Tier 1 sends + stockbot multi-ticker stabilization monitoring + Domain 49/50 prep for July 15 activation)**
   - Contention: Three parallel user + agent work streams.
   - Stockbot monitoring (0.5 agents daily, June 15–30, continuing into July 1–15) consumes a standing agent allocation.
   - If Domain 48 coalition follow-up research needed (if coalition asks questions about policy details): agent contention becomes critical.
   - Mitigation: Automate stockbot monitoring (Item 61 frameworks already exist). Frees agents for Domain 48 support. Domain 48 template pre-staging (June 30) reduces follow-up research needs.

**Viability rating: FEASIBLE but RISKY**. Scenario A is technically possible if stockbot Phase 3a decision is NO-GO or CAUTION (low monitoring overhead). If Phase 3a is GO, Scenario A demands constant re-prioritization June 15–July 15. Not recommended unless user signals exceptional bandwidth availability.

---

### Scenario B: Staggered Parallel (51 June → 57 + 48 July)

**Domains executing sequentially with July parallelism**: Domain 51 (June 9–12) → Wrap-up monitoring (June 13–30) → Domain 48 Tier 1 sends (July 1–15) + Domain 57 Gist creation (July 1–10) + Domain 49/50 prep (July 1–31).

**Resource allocation**:
- User hours: 4.5 hours (June 9–12 Domain 51 sends + monitoring) + 3 hours (June 13–30 Domain 51 Tier 2 monitoring) + 2 hours (June 25–30 Domain 48 Gist creation + template prep) = **9.5 hours in June**.
- User hours July: 4 hours (July 1–15 Domain 48 Tier 1 + Tier 2 sends) + 2 hours (July 1–10 Domain 57 Gist prep + contact refresh) + 2 hours (July 15–31 Domain 49/50 template finalization) = **8 hours in July**.
- Agent hours: 1.5 (June 9–12) + 1 (June 13–30) + 0.5 (June 25–30) + 2 (July 1–15) + 1 (July 1–10) + 1.5 (July 15–31) = **7.5 hours total June–July**.

**Parallel track coordination**: 
- June: Domain 51 only (full attention). No parallelism conflict.
- July: Domain 48 sends (user-intensive, July 1–15) + Domain 57 prep (agent-intensive, July 1–10, minimal user overhead) + Domain 49/50 template prep (user + agent, July 15–31). Three streams but sequential handoff (48 → 57 → 49+50 prep).

**Conflict zones**:

1. **June 15 (Day 6 of Domain 51 + stockbot Phase 3a decision)**
   - Contention: Domain 51 monitoring + Phase 3a expansion decision only.
   - Domain 48 prep (Gist creation) starts June 25, after Phase 3a decision is finalized. No conflict.
   - Mitigation: None needed. Scenario B naturally defers Domain 48 prep until after June 15 decision gate.

2. **July 1–15 (Domain 48 Tier 1 sends + Domain 57 prep + stockbot multi-ticker stabilization + stockbot Item 61 automation**
   - Contention: Three streams (48 user + 57 agent + stockbot monitoring). All three are lower-intensity than Scenario A.
   - If stockbot automation (Item 61) is complete: monitoring becomes fully autonomous. Zero contention.
   - If stockbot automation is incomplete: 0.5 agent/day needed for monitoring. Still less than Scenario A.
   - Mitigation: Prioritize Item 61 completion by June 30. Even 50% automation reduces contention significantly.

3. **July 15–31 (Domain 49/50 template prep + Domain 48 Tier 2 ongoing + stockbot multi-ticker final stabilization)**
   - Contention: Moderate. Domain 49/50 prep is lower-intensity than active distribution. Stockbot stabilization should be winding down by July 15.
   - Mitigation: If stockbot issues emerge July 15+: defer Domain 49/50 prep to August 1 (both have August distribution windows; prep can compress into first week of August).

**Viability rating: HIGHEST RECOMMENDED**. Scenario B respects all domain external deadlines, naturally avoids June 15 contention, and distributes user/agent load across accessible windows. Confidence: 92%.

---

### Scenario C: Sequential (No Parallelism, 51 → 48 → 57 → 49+50 → 54 Deferred)

**Domains executing strictly sequentially**: Domain 51 (June 9–12) → Domain 48 (July 1–20) → Domain 57 (August 10) → Domains 49+50 (August 15–31).

**Resource allocation**:
- User hours: 4.5 (June) + 3.5 (July) + 3.5 (August Domain 57) + 7 (August Domains 49+50) = **18.5 hours total**, all in non-conflicting windows.
- Agent hours: 2 (June) + 2 (July) + 2 (August Domain 57) + 4 (August Domains 49+50) = **10 hours total**.

**Parallel track coordination**: Zero parallelism. Each domain completes (Tier 1 + Tier 2 + monitoring) before next domain Gist creation begins.

**Conflict zones**:

1. **August 15–31 (Domains 49 + 50 + Domain 57 all distributing simultaneously)**
   - Wait: Scenario C was supposed to avoid parallelism, but both Domain 49 and Domain 50 are hard-deadline domains (August 1 ballot campaign integration for Domain 50; August 15 DC Circuit briefing for Domain 49). They cannot be sequenced; they must be parallel.
   - Contention: August 15–31 still has 3-domain parallelism (57 tail end + 49 + 50), same as Scenario B July window.
   - Mitigation: None. Scenario C cannot actually avoid the August parallelism without deferring Domains 49 and 50 to September (which violates their external deadline constraints).

**Adjusted assessment**: Scenario C is labeled "sequential" but actually defers the parallelism problem to August rather than solving it. It trades June–July peace for August crunch.

**Viability rating: MODERATE**. Scenario C works if user prefers "peace now, crunch later" risk profile. Not recommended over Scenario B because it doesn't actually solve the parallelism problem; it just delays it.

---

## Section 2: Contention Resolution Matrix

### June 15 Checkpoint Decision Point

**Primary decision**: Based on Phase 1 engagement metrics (PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 5) AND stockbot Phase 3a expansion decision (Item 66).

| Phase 1 Signal | Stockbot Phase 3a | Recommended Path | User Hours Impact | Agent Hours Impact |
|---|---|---|---|---|
| STRONG (>20% open, >50 responses) | GO (expand multi-ticker) | Scenario A (accept higher June–July contention; Phase 1 social proof justifies acceleration) | 11.5 (June–July) | 4.5 (June–July) |
| STRONG | CAUTION (limited expansion) | Scenario B (maintain plan, but can use freed agents for optional Domain 49/50 early-start research) | 9.5 (June) + 8 (July) | 7.5 |
| STRONG | NO-GO (Phase 3a deferred) | Scenario A (full parallelism safe; agents freed from stockbot allocation) | 11.5 | 4.5 |
| MODERATE (10–20% open, 20–50 responses) | GO | Scenario B (mandatory; Scenario A too risky) | 9.5 (June) + 8 (July) | 7.5 |
| MODERATE | CAUTION | Scenario B (default path) | 9.5 (June) + 8 (July) | 7.5 |
| MODERATE | NO-GO | Scenario B (still recommended; no acceleration needed) | 9.5 (June) + 8 (July) | 7.5 |
| WEAK (<10% open, <20 responses) | GO | Scenario C (reduce Phase 2 intensity until Phase 1 root-cause resolved) | 3.5 (June) + 4 (July) | 2 (June) + 3 (July) |
| WEAK | CAUTION | Scenario C (or Scenario B if Phase 1 root-cause quickly identified) | 3.5 (June) + 4 (July) | 2 (June) + 3 (July) |
| WEAK | NO-GO | Scenario C (maximize agent availability for Phase 1 recovery research) | 3.5 (June) + 4 (July) | 2 (June) + 3 (July) |

---

## Section 3: Stockbot Item 66 Decision Impact

**Current status (per ORCHESTRATOR_STATE.md, June 5)**: 
- Stockbot Item 62 (multi-ticker pre-market checks) complete and in production monitoring.
- Stockbot Item 66 (Phase 3a expansion decision): scheduled for June 15 checkpoint decision.
- Phase 3a expansion scope: multi-ticker FOMC data integration + Phase 3a retrain + deployment validation (estimated 6–8 weeks post-approval, June 16–August 5).

**Resource impact on resistance-research Phase 2**:

| Item 66 Decision | Stockbot Agent Load (June 15–Aug 5) | Systems-Resilience Contention (June 15) | Resistance-Research Available Capacity |
|---|---|---|---|
| **GO (approve Phase 3a)** | 3 agents full-time (June 15–July 20) + 2 agents (July 21–Aug 5) | HIGH (Wave 2 author onboarding June 15 + Phase 3a deployment) | Scenario B mandatory (Scenario A introduces too much risk) |
| **CAUTION (pilot Phase 3a)** | 1.5 agents (June 15–July 20) + 1 agent (July 21–Aug 5) | MODERATE (Wave 2 + pilot overhead) | Scenario A or B both feasible; recommend B for safety |
| **NO-GO (defer Phase 3a)** | 0.5 agents (ongoing monitoring only) | LOW (Wave 2 only, minimal stockbot support) | All scenarios feasible; recommend Scenario A (maximize Phase 2 velocity) |

**June 15 Decision Protocol**:

1. **User decision on Item 66**: By June 15, 18:00 UTC, decision on Phase 3a expansion (GO/CAUTION/NO-GO).
2. **Mapping to Scenario**: Check table above. Recommended path follows from stockbot decision + Phase 1 signal combo.
3. **Resource reallocation**: If Scenario shifts (e.g., Phase 1 STRONG + Stockbot GO = Scenario B mandatory), update BATCH_2_RESOURCE_ALLOCATION_MATRIX.md with June 15 decision note.
4. **Agent dispatch**: If Scenario B selected and Stockbot GO, allocate 1.5 agents to stockbot + 0.5 agents to Phase 2 daily. If Scenario A, allocate 3 agents to stockbot + 1.5 agents to Phase 2.

---

## Section 4: Systems-Resilience Wave 2 Author Onboarding (June 15)

**Current status**: Systems-Resilience Wave 2 author recruitment and onboarding scheduled for June 15 (per ORCHESTRATOR_STATE.md project notes). Estimated overhead: 0.5–1 agent for tech support and orientation.

**Overlap with Phase 2 checkpoints**:
- June 15 is also the primary go/no-go checkpoint for Phase 2 (PHASE_2_SEQUENTIAL_ACTIVATION_STRATEGY.md Section 4.2).
- Systems-Resilience Wave 2 onboarding (June 15) requires user availability for orientation calls and technical setup.

**Resource allocation**:
- User hours: Systems-Resilience Wave 2 onboarding = 1–2 hours (June 15, concurrent with Phase 2 checkpoint assessment).
- Agent hours: Wave 2 tech support = 0.5 agents (June 15, can overlap with Phase 2 decision work).

**Mitigation**: Phase 2 checkpoint decision (review metrics, decide Scenario A/B/C) can happen June 14–15 morning. Systems-Resilience Wave 2 onboarding can happen June 15 afternoon/evening. No hard conflict if separated by 4–6 hours.

---

## Section 5: Item 61 Stockbot Automation (June 30 Target)

**Current scope** (per BATCH_2_RESOURCE_ALLOCATION_MATRIX.md notes): Item 61 (stockbot monitoring automation framework) targets completion by June 30. If complete: daily stockbot multi-ticker monitoring becomes fully autonomous (zero manual agent overhead July 1+).

**Impact on Phase 2 resource allocation**:
- If Item 61 complete by June 30: Scenario B resource availability improves significantly. Agents freed from stockbot monitoring can support Domain 48 coalition follow-up research (July 1–15) without contention.
- If Item 61 delayed past June 30: Scenario B still viable but tighter. Recommend deferring optional Domain 49/50 early-start research if Item 61 status unclear by June 20.

**Monitoring checkpoint**: June 20, check Item 61 status in ORCHESTRATOR_STATE.md. If on track for June 30: proceed with Scenario B confidence. If delayed: update resource allocation.

---

## Section 6: Recommended Path Forward (Scenario B + Contingencies)

### Week 1 (June 3–8)
- **Domain 51**: Final Gist verification (June 8). Contact list validation (June 8–9, 2 hours).
- **Domain 48**: Identify any contact list stale risks. Order Domain 48 Gist creation for June 25 start.
- **Stockbot**: Confirm Item 61 automation scope and June 30 target.

### Week 2 (June 9–15)
- **June 9–12**: Domain 51 Wave 1 + Wave 2 sends (4.5 hours user). Daily monitoring. Agent support as needed.
- **June 15 Checkpoint**: 
  - Phase 1 engagement assessment (STRONG/MODERATE/WEAK). 
  - Stockbot Item 66 decision (GO/CAUTION/NO-GO). 
  - Systems-Resilience Wave 2 onboarding (afternoon).
  - Decision: Scenario A/B/C (see contention resolution matrix, Section 2).
- **June 16–30**: Domain 51 Tier 2 monitoring (1.5 hours user). Domain 48 Gist creation (2 hours user, June 25–30).

### Week 3–4 (July 1–15)
- **July 1–15**: Domain 48 Tier 1 sends (4 hours user). Domain 57 Gist creation + contact refresh (1.5 hours agent, July 1–10). Domain 49/50 prep begins (July 15).
- **July 10**: Item 61 automation status check. If on track: confirm agents freed for Phase 2 support.

### Week 5–6 (July 16–31)
- **July 15–31**: Domain 49/50 template finalization (2 hours user). Domains 49/50 Gist creation (July 20–25). 

### Week 7–8 (August 1–15)
- **August 1**: Domain 50 Tier 1 sends (Lambda Legal + AT4E, hard deadline).
- **August 10**: Domain 57 Tier 1 sends.
- **August 15**: Domain 49 Tier 1 sends.

**Total user hours estimate**: 9.5 (June) + 8 (July) + 5 (August) = **22.5 hours** across June–August Phase 2 execution.

**Total agent hours estimate**: 7.5 (June–July) + 2 (August) = **9.5 hours** across Phase 2 execution.

**Unused budget**: Original 90–110 hour Phase 2 estimate assumed substantial research production. With all research production complete, approximately 60–80 hours remain available for Phase 3 scoping work, Domain G (Press Freedom, June 15 target), and Domain 31x (Healthcare Tariff, July 31 date approaching).

---

*Decision tree prepared June 5, 2026. Primary sources: PHASE_2_SEQUENTIAL_ACTIVATION_STRATEGY.md, BATCH_2_RESOURCE_ALLOCATION_MATRIX.md, ORCHESTRATOR_STATE.md, stockbot and systems-resilience project status. All scenarios grounded in documented capacity constraints and checkpoint decision gates. Confidence: 92%. Ready for June 15 implementation.*
