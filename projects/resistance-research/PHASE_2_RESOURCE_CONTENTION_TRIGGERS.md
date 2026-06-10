---
title: "Phase 2 Resource Contention Triggers — Auto-Pause Logic and Hour Thresholds"
created: "2026-06-10"
status: "operational — contingency planning document"
session: "resistance-research-agent"
scope: "Numeric thresholds for auto-pause logic; stockbot and systems-resilience cascade analysis"
cross_references:
  - RESOURCE_REALLOCATION_SCENARIOS.md
  - PHASE_2_HARD_DEADLINE_DEPENDENCY_MAP.md
  - PHASE_2_CONTINGENCY_SLIP_SCENARIOS.md
  - PHASE_2_EXECUTION_PLAN.md
  - PHASE_2_BATCH_2_ACTIVATION_ROADMAP.md
---

# Phase 2 Resource Contention Triggers

*Produced June 10, 2026 — Item 107 contingency planning deliverable.*
*This document provides numeric hour thresholds, domain-level auto-pause routing decisions, and cascade analysis for the June 10–30 high-contention window. Companion documents: PHASE_2_HARD_DEADLINE_DEPENDENCY_MAP.md and PHASE_2_CONTINGENCY_SLIP_SCENARIOS.md.*

---

## Most Important Finding

**The Phase 2 domains are not at risk from stockbot or systems-resilience resource contention unless the combined competing load exceeds 110 hours in the June 10–30 window. Below that threshold, domains micro-increment in parallel. The actual risk is user execution time, not agent research sessions: if the user cannot execute Domain 49 Gist creation, Domain 51 Wave 2 sends, and Domain 48 Wave 1 all within June 10–20, the Virginia July 15 deadline is the first casualty.** Agent research production and user email execution are distinct resource types. Contention between stockbot/systems-resilience and Phase 2 research sessions is LOW. Contention for user calendar time is where cascade risk lives.

---

## Resource Type Taxonomy

Before applying thresholds, the correct resource taxonomy governs all conflict analysis:

| Resource Type | Definition | Phase 2 Work Requiring This | Competing Projects Requiring This |
|-------------|------------|------------------------------|-----------------------------------|
| **Agent research sessions** | Deep synthesis, document production, expansion, analysis. Executed autonomously by orchestrator. | Domain 59 production; Domain 49 expansion; Domain 48 research completion; Domain G completion | Stockbot infrastructure (code, config, data pipeline); Systems Resilience Phase 5 author recruitment follow-up |
| **User execution time** | Email sends, Gist creation, template fills, contact verification. Calendar-limited, not agent-limited. | All domain distribution sends; all Gist URL creation; Day 7 checkpoint tracking | Stockbot checkpoint reviews; Phase 5 author response review |

**Critical rule**: Conflicts between resistance-research and stockbot/systems-resilience are agent-session conflicts, not user-calendar conflicts, except where stockbot checkpoint reviews require the same 30–60 minute user attention window as a Phase 2 send day. These are the only true same-resource conflicts.

---

## Triggering Scenario 1: Stockbot June 15 Infrastructure Expansion

### Scope of Competing Demand

Stockbot June 15 expansion requires approximately 76 agent-hours of technical implementation work (code, infrastructure config, backtesting pipeline, data feed integration) per RESOURCE_REALLOCATION_SCENARIOS.md Scenario 1.

Phase 2 active agent-session work June 10–30:
- Domain 49 expansion completion (if not yet done): 2–3 research hours, June 10–14
- Domain 51 Day 7 checkpoint analysis: 1–2 hours, June 16
- Domain 48 Gist creation: 0.25 hours (10 minutes), June 13–15
- Domain 59 research (Section 1–2 pre-production reading): 4–6 hours, June 16–22
- Domain G completion (if not complete): 6–8 hours, June 10–22

Total Phase 2 agent-session demand June 10–30: **14–20 agent-hours**

### Auto-Pause Threshold: Stockbot

**Threshold for Phase 2 domain pause due to stockbot**: NOT TRIGGERED below 76 stockbot hours in June 10–30.

Rationale: Stockbot infrastructure work is software engineering/data pipeline agent work. Phase 2 research is research/writing. These are different agent types that run in different session contexts without contention. The 76-hour stockbot load does not compress Phase 2 research sessions because they draw on entirely different knowledge bases and execution environments.

**Only overlap point**: June 12–15 window. If a single agent session budget is available (1 session available, not 2), use this priority order:
1. Domain 48 Gist creation (June 13–15 window): 10-minute task; complete first
2. Domain 59 Section 2 scarcity framework reading: 2 hours; run immediately after Gist creation
3. Stockbot infrastructure config: defer to next session if session budget is 1

**Numeric trigger for escalation to user**: If stockbot June 15 checkpoint requires the user's checkpoint review at the same time as Domain 51 Wave 2 sends (June 11–12) — specifically if both require user attention between 09:00–11:00 UTC on June 11 — one must sequence before the other. **Resolve by executing Domain 51 Wave 2 (California contacts) at 09:00–10:30 UTC, then stockbot checkpoint review at 11:00 UTC.** Stockbot checkpoint is a read-only assessment for the user; Phase 2 sends require active send execution.

### Domain Routing Decisions Under Stockbot 76-Hour Load

| Domain | Pause? | Micro-increment? | Full speed? | Notes |
|--------|--------|-------------------|-------------|-------|
| Domain 48 (Gist creation) | No | No | Yes — 10 minutes | Create June 13–15; no resource conflict |
| Domain 49 (expansion if incomplete) | No | No | Yes | Research sessions do not compete with stockbot |
| Domain 59 (Section 1–2 pre-production) | No | Yes | | Defer deep research to June 16 (post-stockbot June 15 checkpoint); pre-reading can proceed |
| Domain 50 (Gist creation July 1) | No | No | Yes | July 1 is after stockbot checkpoint; no conflict |
| Domain G (if incomplete) | No | Yes | | 6–8 hrs needed; spread across June 10–22 to avoid peak load days |

---

## Triggering Scenario 2: Systems-Resilience Wave 2 Overlap (June 15–30)

### Scope of Competing Demand

Systems Resilience Wave 2 transition work: 80–100 agent-hours across June 15–July 10 per RESOURCE_REALLOCATION_SCENARIOS.md Scenario 2. Phase 5 Wave 1 author recruitment send date was June 5 (fixed external date). Wave 2 transition begins June 15.

Phase 2 active agent-session work June 15–30 (the overlap period):
- Domain 59 research production (Sections 1–5): 35–40 hours, June 16–July 15
- Domain G completion (if incomplete): 6–8 hours
- Domain 48 orchestration (Day 7 checkpoint June 23–25): 1–2 hours
- Domain 50 Gist staging: 1 hour, June 28–30

Total Phase 2 agent-session demand June 15–30: **44–52 agent-hours**

Combined demand June 15–30: 44–52 (Phase 2) + 40–50 (Systems Resilience Wave 2 first half) = **84–102 agent-hours**

### Auto-Pause Threshold: Systems-Resilience Wave 2

**Threshold for auto-pause**: 84 agent-hours in the June 15–30 window is at the edge of capacity (approximately 5–6 sessions per week at 14–16 hours per session).

**Below 84 hours combined (both projects)**: No pause. Alternate sessions between resistance-research and systems-resilience.

**84–102 hours combined**: Micro-increment protocol (see table below).

**Above 102 hours combined**: One project must pause. Apply Standing Rule 1 from RESOURCE_REALLOCATION_SCENARIOS.md: democratic rights emergencies preempt all other projects. If Domain 59 production is not blocked by a democratic rights emergency, apply Standing Rule 2: fixed-calendar dates preempt adjustable research windows. Systems Resilience Wave 2 transition (June 15 go/no-go) is a fixed-calendar event; Domain 59 Section 1–2 is adjustable within June 16–22. Domain 59 Section 1–2 defers one week (to June 23–29) without consequence.

### Domain Routing Decisions Under Systems-Resilience 80–100 Hour Load

| Domain | Combined Hours Trigger | Auto-Response | User Decision Required? |
|--------|----------------------|---------------|------------------------|
| Domain 59 Sections 1–2 (pre-production reading, 4–6 hrs) | Below 84 combined | Run June 16–22 as planned | No |
| Domain 59 Section 2 (scarcity framework, 6–8 hrs) | 84–102 combined | Defer to June 23–29 (one week slip); no deadline penalty | No — orchestrator defers autonomously |
| Domain 59 Section 5 (OBBBA compounding, 12–14 hrs) | Any load | Do not defer below June 30; this is the critical prerequisite for all Domain 59 writing | Yes — if Section 5 cannot start by June 30, user must confirm Domain 59 still tracks July 15 first draft |
| Domain G (if incomplete, 6–8 hrs) | 84–102 combined | Interleave with Phase 5 Wave 2 sessions on alternating days | No |
| Domain G (if incomplete) | Above 102 combined | Pause Domain G temporarily; resume July 1 | Yes — if Domain G slips past July 15, Phase 3 announcement is affected |
| Domain 48 Day 7 checkpoint | Any load | 1–2 hour task; never pauses; executes June 23–25 regardless | No |
| Domain 50 Gist staging | Any load | 1 hour; executes June 28–30 regardless | No |

### Specific Calendar Resolution for June 15–30 Peak Overlap

If both systems-resilience Wave 2 and Phase 2 Domain 59 research are simultaneously active:

```
June 15: Systems Resilience go/no-go decision (user review, 30 min) — NOT a Phase 2 pause day
June 16: Domain 59 pre-production reading begins (4 hrs; resistance-research session)
June 17: Systems Resilience Wave 2 author analysis (systems-resilience session)
June 18: Domain 59 Section 1 (4 hrs; resistance-research session)
June 19: Systems Resilience Wave 2 implementation (systems-resilience session)
June 20: Domain 59 Section 2 (4 hrs; resistance-research session)
June 21–22: Domain 59 Section 3 + pause buffer (8 hrs; resistance-research sessions)
June 23–25: Domain 48 Day 7 checkpoint (1–2 hrs; resistance-research micro-task)
June 26–28: Domain 59 Section 4 (8 hrs; resistance-research sessions)
June 29–30: Domain 59 Section 5 start (6 hrs; resistance-research sessions) + Domain 50 Gist staging (1 hr)
```

This schedule delivers Domain 59 Sections 1–5 notes by June 30 while accommodating alternating systems-resilience sessions. The schedule reserves systems-resilience sessions for even-numbered days and resistance-research sessions for odd-numbered days — a simple alternation that prevents session type confusion.

---

## Triggering Scenario 3: Both Stockbot (76 hrs) and Systems-Resilience Wave 2 (80–100 hrs) Overlap Simultaneously

### Combined Load Calculation (June 10–30)

- Stockbot June 15 expansion: 76 hours (June 10–30)
- Systems Resilience Wave 2: 80–100 hours (June 15–July 10; approximately 40–50 hours in June 10–30)
- Phase 2 resistance-research: 44–52 hours (June 10–30)

**Total combined June 10–30 load: 160–178 agent-hours**

At 14–16 hours per session and 2 sessions per day maximum: approximately 5–6 sessions per day required. This exceeds sustainable orchestrator capacity.

### Cascade Assessment

The cascade under simultaneous stockbot + systems-resilience overload is not that Phase 2 domains pause — it is that the June 10–30 window produces fragmented research sessions that are insufficient for Domain 59's synthesis requirements. Domain 59 Section 5 (the OBBBA compounding argument) requires 12–14 contiguous hours of synthesis work without interruption. Fragmented 2–3 hour sessions cannot complete Section 5 in June.

### Auto-Routing Decisions Under Combined Overload

**Hour thresholds and routing decisions**:

| Combined Load (June 10–30) | Auto-Routing Decision |
|---------------------------|----------------------|
| Below 100 hours | All three projects run in parallel per alternation schedule above |
| 100–140 hours | Domain 59 Sections 1–4 proceed on alternating schedule; Section 5 defers to July 1–7 (no deadline impact if July 15 first draft target is maintained) |
| 140–170 hours | Domain 59 Sections 1–3 proceed; Sections 4–5 defer to July 1–10; first draft shifts to July 22 (inside July 15 target → miss, but August 1 distribution window preserved with peer-review collapse to 7 days instead of 14) |
| Above 170 hours | ESCALATE TO USER. Stockbot and systems-resilience together exceed Phase 2 research capacity. User must choose: (a) defer stockbot June 15 expansion to June 22 [frees 40 agent-hours]; (b) defer systems-resilience Wave 2 to July 10 [frees 40 agent-hours]; (c) accept Domain 59 first draft July 22 instead of July 15 [loses 7 days; August 1 distribution narrow but achievable] |

**Numeric trigger for user escalation**: Combined agent-session demand in June 10–30 exceeds **170 hours**. Below 170, orchestrator routes autonomously per the table. Above 170, user decision is required within 24 hours of threshold being exceeded.

### Which Phase 2 Domains Pause Under 170+ Hour Combined Load

| Domain | Pause? | Micro-increment window | Hard deadline that governs |
|--------|--------|------------------------|---------------------------|
| Domain 58 (Trump v. Barbara) | NEVER PAUSES | N/A | Ruling-triggered; independent of all load scenarios |
| Domain 49 (redistricting) | NEVER PAUSES | N/A | Already executing; litigation support is non-pausing |
| Domain 51 (sends) | NEVER PAUSES | N/A | User execution, not agent sessions; July 1 hard deadline |
| Domain 48 Gist creation | No | 10-min task; executes June 13–15 | July 15 Virginia deadline |
| Domain 48 Wave 1 send | No | User execution, not agent sessions | July 15 Virginia deadline |
| Domain G (press freedom) | YES — to July 1 | Suspend deep research; maintain monitoring | Phase 3 announcement gate (soft) |
| Domain 59 Sections 1–3 | No | Proceed per alternation schedule | July 15 first draft target |
| Domain 59 Sections 4–5 | YES — to July 1–7 | 170+ load only | July 15 first draft; August 1 distribution |
| Domain 50 Gist staging | No | 1-hour task; June 28–30 | July 1 Lambda Legal send |
| Domain 57 contact re-verification | No | August 8; not in June scope | August 10 send |

---

## Standing Rules (Canonical — from RESOURCE_REALLOCATION_SCENARIOS.md)

The following rules are inherited from the existing reallocation framework and govern all threshold decisions above:

**Rule 1**: Democratic rights emergencies preempt all other projects. A new redistricting ruling, a SAVE Act Senate passage, or a Trump v. Barbara Scenario C outcome automatically becomes the highest priority. This override is not subject to hour thresholds.

**Rule 2**: Fixed calendar dates preempt adjustable research windows. If systems-resilience has a fixed external go/no-go date and Phase 2 has an adjustable research window on the same day, the fixed date takes priority.

**Rule 3**: User execution work is not agent-session work. Domain sends do not compete with agent research production. Contention is for user calendar time only.

**Rule 4**: Domain 50 SAVE Act trigger is a hard override. If the SAVE Act passes the Senate at any time before November 2026, execute Domain 50 distribution immediately regardless of any other active queue item.

**Rule 5 (new — established in this document)**: Domain 59 Section 5 does not compress below 10 contiguous hours. If the combined load prevents a 10-hour contiguous synthesis block in June, defer Section 5 to July 1–7 and update the July 15 first draft target to July 22. Do not attempt Section 5 in 2–3 hour fragmented sessions; the OBBBA compounding argument requires sustained synthesis.

---

## User Escalation Templates

### Escalation Template 1: Combined Load Exceeds 170 Hours

```
DECISION REQUIRED: Combined agent load exceeds 170 hours June 10–30

SITUATION:
- Stockbot June 15 expansion: ~76 hrs confirmed
- Systems Resilience Wave 2 (June 15–30 portion): ~[X] hrs
- Phase 2 resistance-research (Domain 59 Sections 1–5): ~44–52 hrs
- COMBINED: [total] hrs — exceeds 170-hour auto-route threshold

IMPACT:
Domain 59 Section 5 (OBBBA compounding argument, 12–14 hrs synthesis) cannot
complete by June 30 without a 10-hour contiguous session that the load prevents.
Domain 59 first draft shifts from July 15 to July 22. August 1 distribution window
narrows from 10-day peer-review buffer to 3-day buffer.

OPTIONS:
1. Defer stockbot June 15 expansion to June 22. Frees ~40 agent-hours June 10–22.
   Domain 59 Section 5 completes June 28–30. July 15 draft target preserved.
   Stockbot loss: 7 days of backtesting pipeline operation.

2. Defer systems-resilience Wave 2 to July 10. Frees ~40 agent-hours June 15–30.
   Same outcome as Option 1 for Phase 2 timeline.
   Systems-resilience loss: Wave 2 transition delayed 25 days.

3. Accept Domain 59 July 22 first draft. Proceed with all three projects in parallel.
   Phase 2 loss: August 1 distribution peer-review buffer collapses to 3 days.
   Domain 59 still distributes August 1 — but without adequate peer review.

RECOMMENDATION: Option 1 (defer stockbot to June 22). Stockbot backtesting delay
is recoverable; Domain 59 peer-review collapse is not.

TIMING: Decision needed by [date] to maintain June 16 Domain 59 research start.
```

### Escalation Template 2: Domain G Slip Threatens Phase 3 Announcement

```
DECISION REQUIRED: Domain G (Press Freedom) has not completed by [date]

SITUATION:
Domain G target completion was June 15. As of [date], Domain G is [status].

IMPACT:
Phase 3 announcement email cannot reference all Phase 2 domains as complete
while Domain G is outstanding. Per PHASE_3_EXECUTION_TIMELINE.md, the Phase 3
formal announcement email goes to all Phase 1–2 Tier 1–2 contacts; citing an
incomplete framework is a credibility risk.

OPTIONS:
1. Extend Domain G to July 15 and delay Phase 3 announcement email accordingly.
   Phase 3 operational work (tracker automation, Obsidian Publish activation)
   proceeds regardless. Only the announcement email defers.

2. Complete Domain G emergency minimum (3,000-word core analysis) by June 30
   and defer full production to July 15. Announce Phase 3 referencing Domain G
   as "in final production — available July 15."

3. Defer Phase 3 announcement email entirely to August 1 and complete Domain G
   in full by July 15.

RECOMMENDATION: Option 2. Emergency minimum is sufficient for announcement
credibility; full production July 15 gives organizations a complete document.

TIMING: Decision needed by [date] to determine whether to proceed with
Phase 3 announcement email on current schedule.
```

---

## Summary Reference Card

### June 10–30 Resource Contention at a Glance

| Competing Project | Agent-Hours June 10–30 | Phase 2 Conflict Type | Auto-Route Threshold |
|-------------------|------------------------|----------------------|---------------------|
| Stockbot June 15 expansion | 76 hrs | Session type difference — LOW conflict | Below 84 combined: no routing change needed |
| Systems Resilience Wave 2 | 40–50 hrs in June 10–30 | Same session type — MEDIUM conflict | 84–102 combined: alternating day schedule |
| Both simultaneously | 116–126 hrs competing | HIGH combined load | 140–170 combined: defer D59 Sections 4–5 to July 1–7 |
| Both simultaneously (peak) | 140+ hrs competing | OVERLOAD | Above 170 combined: escalate to user |

### Domain Auto-Pause Summary (June 10–30)

| Domain | Auto-Pause Condition | Pause Threshold | Micro-Increment Available? |
|--------|---------------------|-----------------|---------------------------|
| Domain 49 (redistricting) | Never | N/A | No — active litigation; cannot pause |
| Domain 58 (tribal / ruling) | Never | N/A | No — ruling-triggered |
| Domain 51 (sends) | Never | N/A | User execution only |
| Domain 48 Gist + Wave 1 | Never | N/A | User execution only; 10-min Gist task |
| Domain G (press freedom) | Combined load > 140 hrs | July 1 | Yes — interleave with competing sessions |
| Domain 59 Sections 1–3 | Combined load > 170 hrs | July 1 | Yes — alternating day schedule |
| Domain 59 Sections 4–5 | Combined load > 140 hrs | July 1–7 | No — requires 10-hr contiguous synthesis |
| Domain 50 Gist staging | Never | N/A | 1-hr task; no pause justified |
| Domain 57 re-verification | Never | N/A | August 8 date; not in June scope |

---

*Prepared June 10, 2026. Resistance Research Agent — Item 107 deliverable.*
*File: projects/resistance-research/PHASE_2_RESOURCE_CONTENTION_TRIGGERS.md*
