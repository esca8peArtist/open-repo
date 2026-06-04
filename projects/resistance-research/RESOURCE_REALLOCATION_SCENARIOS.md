---
title: "Resource Reallocation Scenarios — Phase 2 Batch 2 vs. Other Project Conflicts"
created: "2026-06-03"
status: "production-ready"
session: "Resistance Research Agent — Phase 2 Batch 2 planning"
cross_references:
  - PHASE_2_BATCH_2_ACTIVATION_ROADMAP.md
  - ORCHESTRATOR_STATE.md
  - projects/systems-resilience/PHASE_5_WAVE_1_AUTHOR_RECRUITMENT_RUNBOOK.md
---

# Resource Reallocation Scenarios

*Phase 2 Batch 2 vs. Competing Projects — Conflict Mitigation Matrix*
*Resistance Research Agent — June 3, 2026*

---

## Three-Scenario Summary

The brief asked for three specific scenarios covering the June conflict window (stockbot June 15 expansion, est. 76 hrs; systems-resilience Wave 2, est. 80–100 hrs; Phase 2 Batch 2 active domains). Summary:

| Scenario | Description | June Agent-Hours | Risk | Recommended? |
|----------|-------------|-----------------|------|-------------|
| **A** | All parallel — Phase 2 Batch 2 + stockbot June 15 + systems-resilience Wave 2 run simultaneously | ~240+ hrs combined | High-load; requires daily sessions; user must approve | **Yes, if session budget permits** |
| **B** | Stockbot deferred to June 20 — Phase 2 Batch 2 and systems-resilience Wave 2 run June 3–15; stockbot begins June 15 | ~160–180 hrs June peak reduced | Medium; stockbot loses 5 backtesting days | **Yes, preferred if budget is constrained** |
| **C** | Phase 2 condensed to 51+57 only — Domain 49, 48, 50, 54 deferred; stockbot and systems-resilience run as planned | ~80–100 hrs resistance-research deprioritized | Domain 49 redistricting cascade may miss June primary window | **No — Domain 49 has a hard redistricting window; condensing is only acceptable if stockbot has a higher-priority external deadline** |

**Recommendation**: Scenario B. Defer stockbot June 15 to June 20; execute Phase 2 Batch 2 (Domains 49 + 51) June 3–12 as the first priority; systems-resilience Wave 2 transition (June 10 onward) runs in parallel because it requires different session types.

---

## Resource Types in Play

This project uses two distinct resource types. Conflicts only arise within the same resource type.

| Resource Type | What It Covers | Who Controls It |
|-------------|---------------|----------------|
| **Agent research sessions** | Deep research, document production, expansion, analysis | Orchestrator allocates; user approves session assignments |
| **User execution time** | Email sends, Gist creation, template fills, contact verification | User calendar; estimated in hours-per-task |

Conflicts between resistance-research and stockbot/systems-resilience are agent-session conflicts only. The user's email execution work is independent of those projects.

---

## Scenario 1: Phase 2 Batch 2 vs. Stockbot June 15 Infrastructure Expansion

**Conflict type**: Agent session allocation
**Stockbot need**: Infrastructure expansion checkpoint June 15; estimated 76 hours of technical implementation work (code, infrastructure config, backtesting pipeline, data feed integration)
**Phase 2 Batch 2 need**: Domain 49 expansion research (3–4 agent-hours, June 3–10); Domain 51 distribution execution (1–2 agent-hours, June 9–12); Domain 50 Gist prep (1 agent-hour, July 1)

**Total Phase 2 Batch 2 early-June load**: approximately 8–10 agent-hours across June 3–15
**Total stockbot June 15 load**: approximately 76 agent-hours

**Conflict assessment**: LOW for early June; MEDIUM for June 12–15. These are different agent types for most tasks. Stockbot infrastructure work is software engineering / data pipeline agent work. Domain research and distribution is research/writing. They can run in different sessions without contention. The only conflict point is June 12–15 when both have active work.

**Resolution**: No reallocation needed in principle. Sequence Domain 49 expansion in resistance-research sessions (June 3–10). Stockbot infrastructure work runs in dedicated stockbot sessions. If a single session budget is available in the June 12–15 overlap window, prioritize Domain 49 Gist send over stockbot June 15 prep because: (1) redistricting cascade is time-limited to June primary filing deadlines; (2) stockbot June 15 checkpoint is a go/no-go gate, not a hard-deadline with external consequences if slipped to June 22.

**Scenario A (all parallel, 240+ hrs June)**: Run Domain 49 (June 3–10) and stockbot June 15 prep (June 3–15) simultaneously across different sessions. Total June agent-session demand: approximately 85 hours combined. This is feasible given separate session types and different complexity profiles.

**Scenario B (stockbot deferred to June 20)**: If agent budget is compressed, defer stockbot June 15 to June 20. Domain 49 and Domain 51 execute June 3–12 as planned. Stockbot infrastructure work begins June 15 with June 20 as the revised checkpoint. Loss: 5 days of backtesting pipeline operation.

**Scenario C (Phase 2 condensed to 51+57)**: If both stockbot and systems-resilience are simultaneously competing for the same sessions, condense Phase 2 Batch 2 to the two time-constrained domains only: Domain 51 (July 1 hard deadline) and Domain 57 (August 10 anchor). Domain 49 distribution is deferred to June 15–20 (post-stockbot checkpoint). Domain 48 holds until late June.

**Contingency if budget forces a choice**: Defer Domain 49 expansion from June 3–6 to June 7–10 (one-week compression). Domain 49 Gist creation moves from June 7 to June 11. First distribution wave: June 12–15. This preserves all core redistricting advocacy windows.

---

## Scenario 2: Phase 2 Batch 2 vs. Systems Resilience Wave 2 Transition (June 10–July 10)

**Conflict type**: Agent session allocation
**Systems Resilience need**: Phase 5 Wave 1 author recruitment execution (June 5 send date, June 15 09:00 UTC go/no-go decision); Wave 2 transition work (June 10–July 10 window); estimated 80–100 agent-hours across 30 days
**Phase 2 Batch 2 need**: Domain 49 expansion (June 3–10) + Domain 51 distribution (June 9–12); estimated 8–10 agent-hours in early June

**Conflict assessment**: MEDIUM for June 3–15; LOW for June 15–July 10.

The June 3–15 window has the most concentration: Domain 49 expansion + Domain 51 sends + Phase 5 Wave 1 send + June 15 go/no-go. All four are active simultaneously. After June 15, systems-resilience Wave 2 and resistance-research distribution activity separate into different calendar windows (Domain 50 July 1, Domain 54 July 15–30 vs. systems-resilience Wave 2 July work).

**Resolution — Sequencing for June 3–15**:
- **June 3–4**: Domain 49 expansion (resistance-research) + Phase 5 final prep (systems-resilience) run in parallel if separate sessions are available
- **June 5**: Phase 5 Wave 1 send date (systems-resilience fixed; takes priority)
- **June 6–10**: Domain 49 expansion completion (resistance-research)
- **June 9–12**: Domain 51 distribution sends (user execution, not agent sessions)
- **June 15**: Both stockbot checkpoint and systems-resilience Wave 2 go/no-go

If agent session budget is limited to one session per day: June 3 = Domain 49 expansion start, June 4 = Phase 5 send prep, June 5 = Phase 5 sends, June 6–8 = Domain 49 completion. Domain 51 sends are user execution, not agent sessions — they run in parallel with any agent work.

**Resolution — Sequencing for June 15–July 10 (Wave 2)**:
Systems-resilience Wave 2 (80–100 hours) and resistance-research distribution (Domain 50 Gist July 1, Domain 54 July 15–30: combined 4–6 agent-hours) are easily accommodated in alternating sessions. No conflict.

**Scenario A (all parallel, 240+ hours June)**: June 3–15 total demand across all three projects: approximately 90–110 agent-hours. This requires 6–8 active sessions over 12 days — achievable with daily sessions but at the upper bound of orchestrator capacity. User should approve this load in advance.

**Scenario B (stockbot deferred to June 20)**: Domain 49 + Domain 51 + Phase 5 complete by June 12; stockbot June 15 deferred to June 20; systems-resilience Wave 2 begins June 15. Reduces peak June load by approximately 20 hours.

**Scenario C (Phase 2 condensed to 51+57 only)**: If orchestrator is bandwidth-limited, execute only Domain 51 (July 1 hard deadline) and Domain 57 (August 10 anchor) from Phase 2 Batch 2 in June. Domain 49 distributes June 20+ (post-stockbot). Domain 48 and Domain 50 Gist work hold until July. This reduces June resistance-research load to approximately 4–5 agent-hours.

**Contingency if Phase 5 recruitment generates high response volume**: Systems Resilience author response monitoring (June 5–15) is light work (2–3 agent-hours across 10 days). It does not prevent Domain 49 expansion from running in parallel.

---

## Scenario 3: Phase 2 Batch 2 vs. Phase 2 Domain 39 Response Monitoring

**Conflict type**: User execution time (both require user action)
**Domain 39 need**: Day 7 (June 8) monitoring checkpoint; Day 14 (June 15) checkpoint; user captures engagement signals
**Domain 51 need**: June 9–12 email sends (3 user hours)

**Conflict assessment**: LOW. These are sequential in the same week. Domain 39 monitoring (June 8) is passive — log engagement signals, assess threshold. Domain 51 sends (June 9–12) begin after the June 8 checkpoint. No same-day competition.

**Resolution**: June 8 = check Domain 39 signals (30 minutes). June 9 = Domain 51 sends begin. This is the intended sequence per the monitoring framework.

**If Day 7 Domain 39 assessment is STRONG**: Adds 15 minutes for noting that Phase 2 is green-lit, but does not add workload.
**If Day 7 Domain 39 assessment is WEAK**: Adds 30 minutes for contingency protocol review (DOMAIN_39_MONITORING_AND_PHASE_2_ACTIVATION.md contingency section). Still does not delay Domain 51 sends; Domain 51 has a hard July 1 deadline independent of Domain 39 signal.

---

## Scenario 4: Multiple Simultaneous Hard Deadlines (Worst Case)

**Trigger conditions**: If all of the following occur simultaneously in June 2026:
- Alabama or Tennessee redistricting litigation requires emergency amicus support
- SAVE Act passes Senate (requiring immediate Domain 50 activation)
- California Fair Elections Act qualification challenged (requiring Domain 51 emergency distribution)
- Stockbot June 15 checkpoint fails and requires infrastructure repair work

**Conflict assessment**: HIGH — four simultaneous urgent items.

**Resolution priority under resource compression**:

| Priority | Domain/Item | Why Top Priority |
|---------|------------|-----------------|
| 1 | Domain 50 emergency activation (SAVE Act) | Trans voter disenfranchisement before November 2026 is irreversible if SAVE Act passes |
| 2 | Domain 49 redistricting emergency (litigation support) | Maps are being drawn in real time; delays cost actual seats |
| 3 | Domain 51 CA distribution | Hard July 1 deadline; CA campaign infrastructure needs materials |
| 4 | Stockbot infrastructure repair | Financial / tracking consequence but no democratic-rights consequence |

**Resource reallocation under worst case**: Pause stockbot June 15 expansion prep (defer to June 22); execute resistance-research domains in the order above. Notify user via CHECKIN.md flag.

---

## Scenario 5: Phase 2 Batch 2 vs. Systems Resilience Phase 5 Wave 2 Sequencing (July)

**Conflict type**: Agent session allocation (July)
**Systems Resilience need**: Phase 5 Wave 2 author recruitment prep (July timeline)
**Phase 2 Batch 2 need**: Domain 50 Gist creation and Lambda Legal/AT4E send (July 1); Domain 54 preparation (July 15–30)

**Conflict assessment**: LOW-MEDIUM. July has adequate calendar spread to accommodate both. Domain 50 distribution (July 1) and Domain 54 distribution (July 15) are each 1–2 agent-hours. Phase 5 Wave 2 recruitment is similar scope. They can run in alternating sessions.

**Resolution**: Odd-week sessions (July 1, 15) = resistance-research distribution. Even-week sessions = systems-resilience Phase 5 follow-up. No reallocation needed unless a phase 5 author response requires same-day intensive follow-up work.

---

## Standing Rules for Reallocation

1. **Democratic rights emergencies preempt all other projects.** A new redistricting ruling, a trans voter suppression law passed, or a court emergency in an active case described in these domains is automatically the highest priority.

2. **Fixed calendar dates preempt adjustable research windows.** Phase 5 June 5 author send date is fixed. Domain 49 expansion is adjustable within a June 3–12 window. Give fixed-date items priority.

3. **User execution work is not agent-session work.** Email sends do not compete with agent research production. They compete with user time. Check user calendar for conflicts, not session budget.

4. **Domain 50 SAVE Act trigger is an override.** If the SAVE Act passes the Senate at any time before November 2026, execute Domain 50 distribution immediately regardless of any other active queue item. The trans voter suppression stack analysis is the primary advocacy document for Senate SAVE Act opposition from voting rights organizations. This override is hard-coded.

5. **Never defer Domain 49 redistricting past June 15.** Filing deadlines for 2026 primary maps are the binding constraint. Any distribution occurring after mid-June is too late to influence emergency litigation filing windows.

---

*Prepared June 3, 2026.*
