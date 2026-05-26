---
title: "June Resource Allocation — Phase 6 vs. Competing Project Demands"
project: systems-resilience
phase: 6
status: DECISION-READY — June 1 input required
created: 2026-05-26
version: 1
purpose: "Resource contention matrix + 3 contingency scenarios for Phase 6 activation decision"
decision_window: 2026-06-01
---

# June Resource Allocation: Phase 6 vs. Competing Projects

> **Lead finding**: Phase 6 (Domains 60–65, 22–28 hrs/week for 12 weeks) can run in parallel with stockbot and open-repo without collision if the Phase 6 research agent is dedicated and Wave 2 author onboarding is deferred to August 1. The only genuine resource contention point is Orchestrator coordination bandwidth during the June 1–15 multi-project ramp window. Three contingency scenarios are documented below with go/no-go thresholds.

---

## 1. Competing Resource Demands: June–August 2026

### Active Projects With June Demands

| Project | June Scope | Peak Window | Agent Type | Weekly Hours |
|---|---|---|---|---|
| **Phase 6 (Domains 60–65)** | 6-domain research ramp | June 1–August 30 | Research agent (dedicated) | 22–28 |
| **Stockbot Phase 2** | Multi-ticker Jetson deployment (AMZN/JPM) | June 1–15 deployment + June 20+ training | Stockbot subagent | 15–20 |
| **Open-repo Phase 5.2** | OPDS + API gateway implementation (12–17 hrs) | June 1–15 | Engineering subagent | 10–15 |
| **Resistance-research Phase 2** | May 28 re-synthesis routing + Domain 56/39 distribution | May 28–June 15 | Research agent | 8–12 |
| **Phase 5 Wave 2 publication** | Wave 1 publishing + Wave 2 author onboarding (if approved) | June 1–10 publication | Orchestrator | 15–20 (compressed) |

### Orchestrator Coordination Load

The Orchestrator is the common bottleneck. June 1–15 has the highest expected Orchestrator demand:

- June 1: Phase 6 activation decision (this document)
- June 1–5: Phase 5 Wave 1 publication preparation
- June 1–5: Stockbot multi-ticker deployment (SSH dependency)
- June 1–5: Open-repo Phase 5.2 kickoff (user decision on OPDS/API path)
- May 28–June 5: Resistance-research synthesis outcome routing + distribution execution

**Estimated Orchestrator load June 1–15**: 25–35 coordination hrs (above sustainable 20 hrs/week)

---

## 2. Resource Contention Matrix

### Contention Type: Agent Capacity

Phase 6 research requires a **dedicated research agent**. The key question is whether this conflicts with resistance-research, which also uses a research agent.

| Resource | Phase 6 Need | Competing Need | Conflict Risk | Mitigation |
|---|---|---|---|---|
| Research agent (general) | Phase 6 Domains 60–62 (June 1–July 15) | Resistance-research Domain 56/39 distribution (May 28–June 15) | **MEDIUM** — overlap June 1–15 | Stagger: Domain 56/39 is 3–5 day sprint; Phase 6 can wait until June 5 ramp |
| Engineering subagent | None | Stockbot deployment + open-repo | None | No conflict |
| Orchestrator coordination | Phase 6 activation setup (June 1–5, ~10 hrs) | All active projects peak simultaneously | **HIGH** (June 1–10) | Stagger: Phase 6 setup June 3–5 (after June 1 decision + Wave 1 publication) |
| User attention/decisions | June 1 approval meeting | Open-repo Phase 5.2 path, stockbot outcome verification | **MEDIUM** | Batch decisions: single June 1 decision session covering all 4 pending items |

### Contention Type: Research Context Overlap

Domain 60 (International Coordination) has potential overlap with resistance-research Domains 57/58 (geopolitical fragmentation, institutional legitimacy). This is not a conflict — it is an asset. Domain 57's sourcing on international institutional failure (BRICS, NATO withdrawal) directly informs Domain 60's coordination failure analysis.

**Recommendation**: Assign Domain 60 to the same research agent handling resistance-research Domain 57 follow-on work, or brief Phase 6 agent on Domain 57 findings before Domain 60 production begins.

---

## 3. Three Contingency Scenarios

### Scenario A: Full Phase 6 Activation (Preferred)

**Conditions**: User approves June 1. Stockbot Jetson reachable. Resistance-research synthesis routes to STRONG or MODERATE.

**Resource plan**:
- June 1–5: Orchestrator-heavy (stockbot deployment + open-repo kickoff + resistance synthesis routing). Phase 6 agent preparation only (no production writing).
- June 5–August 30: Phase 6 dedicated research agent (Domains 60+62 parallel, Week 1). Stockbot and open-repo running independently.
- Phase 5 Wave 2 author: Deferred to August 1. No June contention.

**Weekly capacity model**:
```
June 1–15 (Peak):
  Orchestrator coordination:  18 hrs/week (batched decisions resolve by June 5)
  Phase 6 research agent:     20 hrs/week (ramp; full capacity from June 10)
  Stockbot subagent:          15 hrs/week (Jetson deployment, training reactivation)
  Open-repo subagent:         12 hrs/week (OPDS + API gateway)
  Resistance-research agent:  10 hrs/week (synthesis routing + distribution sprint)
  TOTAL:                      75 hrs/week (sustainable with 3–4 parallel agents)

June 16–August 30 (Steady state):
  Phase 6 research agent:     25 hrs/week (full production, 2 domains in parallel)
  Stockbot subagent:          10 hrs/week (monitoring, validation)
  Orchestrator coordination:  8 hrs/week
  TOTAL:                      43 hrs/week (well within capacity)
```

**Risk level**: LOW. Timeline: Phase 6 complete August 30.

---

### Scenario B: Phase 6 Deferred 3 Weeks (Stockbot Priority)

**Conditions**: Stockbot Jetson SSH still unreachable June 1. Multi-ticker deployment requires intensive June 1–21 Orchestrator + stockbot agent support to diagnose and resolve Jetson connectivity, deploy AMZN/JPM configuration, and validate model outputs.

**Resource plan**:
- June 1–21: Stockbot recovery takes Orchestrator priority. Phase 6 agent does Domain 60 source library build and research outline (20–25 pre-production hours) but no full production writing.
- June 22–August 30: Phase 6 full production (10 weeks remaining; achievable at 25 hrs/week for 6 domains if Domains 60+62 are partially done).
- Phase 5 Wave 2 author: Deferred to September 1 (pushed back by 4 weeks vs. Scenario A).

**Impact on Phase 6**:
- 3-week delay shifts completion from August 30 to September 20.
- Domain 65 (Institutional Learning, latest dependency) finishes September 15 instead of August 10.
- Distribution package assembly: October 1 instead of September 1.

**Risk level**: MEDIUM. Primary risk: if Jetson remains unreachable beyond June 21, stockbot recovery consumes further Orchestrator bandwidth.

**Trigger threshold**: If Jetson SSH unreachable on June 1 morning, activate Scenario B automatically. No user decision required.

---

### Scenario C: Phase 6 Deferred to September (Maximum Stability)

**Conditions**: User elects to prioritize (1) stockbot Phase 2 full stabilization through July 31, (2) Phase 5 Wave 2 author cycle June 10–July 10, and (3) resistance-research Phase 2 distribution June 1–July 15 before Phase 6 activation.

**Resource plan**:
- June 1–July 31: Stockbot Phase 2 + Phase 5 Wave 2 + resistance-research Phase 2 run fully.
- August 1: Phase 5 Wave 2 author completes. Resistance-research Phase 2 enters monitoring phase.
- September 1–November 30: Phase 6 Domains 60–65 (12-week intensive, identical resource model to Scenario A but shifted 3 months).

**Trade-offs**:
- Advantages: No June resource collision. Full Phase 5 Wave 2 and stockbot Phase 2 complete before Phase 6 starts. Cleaner project handoffs.
- Disadvantages: Phase 6 publication delayed to November–December 2026. Seasonal misalignment (November release reduces impact window). Domains 60–65 are not time-sensitive but the organizational relationships they establish (UNDRR, regional networks) have better engagement in spring.

**Risk level**: LOW (execution risk). MEDIUM (strategic risk from 3-month delay to macro-domain research that anchors future phases).

**Trigger condition**: User explicitly selects defer. Not activated automatically.

---

## 4. Critical Path Analysis

Across all three scenarios, the critical path for Phase 6 is:

```
User June 1 decision
    → Phase 6 research agent briefed on Domain 60 scope (2 hrs)
    → Domain 60 + Domain 62 parallel production start (June 3–5 or June 22 per scenario)
    → Domain 60 outline + sources delivered by June 15 (checkpoint)
    → Domain 60 full draft by June 29 (checkpoint)
    → Domain 60 final by July 8 (critical; enables Domain 65 to start with full international framing)
    → Domains 61, 63, 64 parallel July 1–August 1
    → Domain 65 (Institutional Learning, integrates all) July 22–August 10
    → Phase 6 integration document August 1–August 30
```

**Bottleneck domain**: Domain 65 (Institutional Learning). It cannot reach final quality until Domains 60–64 are substantially complete. If Domain 60 slips, Domain 65 slips by the same amount, and the entire Phase 6 completion slides.

**Parallelization opportunity**: Domains 60 and 62 have no shared dependencies and can be assigned to separate research agents in the same session. This is the single highest-leverage parallel execution opportunity in the Phase 6 timeline — it saves 2–3 weeks.

---

## 5. Resource Allocation Recommendation

**Recommended**: Scenario A (Full Phase 6 Activation June 1)

The Orchestrator load spike in June 1–10 is real but manageable because:
1. Resistance-research synthesis routing is a 3–5 day sprint, not an extended campaign.
2. Stockbot deployment is stockbot-subagent-driven once SSH is restored; Orchestrator overhead is low after the first session.
3. Open-repo Phase 5.2 is engineering-only (no research agent contention).

The cost of deferring Phase 6 (Scenario B or C) is primarily strategic: the macro-institutional research in Domains 60–65 establishes frameworks that will inform Phase 7+ operationalization work. Each month of delay is a month of compounding opportunity cost.

**If user selects Scenario A**: The first Phase 6 production task is Domain 60 International Coordination, which has the largest source library and sets the framing for Domains 61 and 65. Begin June 3–5 (after June 1 decision session).

**If user selects Scenario B or C**: The pre-production work documented in this session (Domain 60 source library, onboarding brief) remains production-ready and requires no rework at activation.

---

*Confidence assessment: High on resource hour estimates (extrapolated from Phase 5 Wave 1+2 actual performance; Wave 1 was 14.6K words in approximately 18–22 hours of production). High on Orchestrator load model (based on active project state as of May 26 ORCHESTRATOR_STATE.md). Medium on Scenario B timeline (Jetson situation is a wildcard; 3-week estimate could extend if hardware issue requires physical intervention). Low confidence on Wave 2 author availability — this is a user-gated variable not yet confirmed.*
