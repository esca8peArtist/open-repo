---
title: "Wave 2 Domain Sequencing Framework"
project: systems-resilience
phase: 6
wave: 2
status: PRODUCTION-READY — June 15 deployment
created: 2026-06-04
revised: 2026-06-04
execution_period: 2026-06-20 to 2026-07-25
scope_assumption: "5–7 domains, 2 domains/week × 3 weeks cadence"
non_negotiable_anchors:
  - "June 20 Wave 2 onboarding start"
  - "June 27 T+7 first-draft checkpoint"
  - "July 4–5 first publication readiness gate"
cross_references:
  - PHASE_6_WAVE_2_ACTIVATION_CHECKLIST.md
  - RESOURCE_CONTENTION_MITIGATION_JUNE_15_30.md
  - PHASE_5_WAVE_1_RECRUITMENT_PREFLIGHT_CHECKLIST.md
word_count: ~1,800
---

# Wave 2 Domain Sequencing Framework
## Parallel vs. Sequential Execution, Dependency Analysis, and Critical Path

**Prepared**: June 4, 2026 (production deployment)
**Execution window**: June 20–July 25, 2026
**Scope**: 5–7 Phase 6 Wave 2 domains (drawn from Phase 3 community-scale production-ready set)
**Cadence**: 2 domains/week × 3 weeks active research, T+7 first-draft checkpoint, T+14 publication readiness gate

---

## Part 1: Wave 2 Scope Definition

### Domain Pool: Phase 3 Community-Scale Production-Ready

Phase 3 completed 5 community-scale domains that are research-ready and scoped for Wave 2 authorship:

| Domain | Research Foundation | Priority | Wave 1 Dependency |
|--------|--------------------|-----------|--------------------|
| **Governance and Democratic Coordination** | Phase 3 governance research complete | P1 — Critical (all other domains reference it) | Requires Phase 5 Wave 1 Governance domain published |
| **Food Systems and Agricultural Continuity** | Phase 3 food systems research complete | P1 — Critical (practical continuity anchor) | Requires Phase 5 Wave 1 Food domain published |
| **Information Resilience and Off-Grid Communication** | Phase 3 info research complete | P2 — High | Requires Phase 5 Wave 1 Info Infrastructure published |
| **Community Security and Conflict De-escalation** | Phase 3 security research complete | P2 — High | Requires Phase 5 Wave 1 Security domain published |
| **Scaling Pathways and Inter-Community Federation** | Phase 3 scaling research complete | P3 — Medium (Phase 7 prep dependency) | Requires Phase 5 Wave 1 Scaling domain published |

Two additional expansion domains may be added if 6–7 author slots fill:

| Domain | Research Foundation | Priority | Status |
|--------|--------------------|-----------|----|
| **Ecosystem Restoration and Climate Adaptation** | Phase 4b agricultural intensification research | P3 | Add if ≥6 authors confirmed |
| **Institutional Learning and Constitutional Adaptation** | Phase 5 Wave 2 conflict resolution research | P3 | Add if 7 authors confirmed |

**Default scope**: 5 domains (P1 + P2), matching the 5-author recruitment target. Expansion to 6–7 domains is contingent on author roster size confirmed June 15.

---

## Part 2: Sequencing Logic — Parallel vs. Sequential

### Recommended: 3 Parallel Author Tracks (Staggered by Priority)

Wave 2 runs 3 simultaneous tracks with a dependency-gated start condition:

**Track 1 — Governance** (begins June 20, unconstrained)

Governance is the highest-priority domain and has the fewest inter-domain dependencies (it establishes the terminology and coordination framework that all other domains reference). Governance starts June 20 regardless of other Track status.

**Track 2 — Food Systems + Information Resilience** (begins June 20, jointly)

Both domains have independent research foundations (Phase 3) and independent Phase 5 Wave 1 dependencies that will be published by June 19. Both can begin in parallel with Track 1. Governance domain does not need to be published before Food or Information research begins — they only cross-reference Governance for terminological alignment, not for foundational content.

**Track 3 — Security + Scaling** (begins June 24, 4-day stagger)

Security and Scaling both depend on Governance and Food domains for framing (e.g., Security conflict de-escalation references Governance coordination structures; Scaling federation models reference Food domain supply network analysis). A 4-day stagger allows Track 1 and Track 2 authors to post their T+3 outlines (June 23), which Track 3 authors read before beginning their own outlines.

**Resource model**: 3–5 simultaneous authors (Track 1: 1 author, Track 2: 2 authors, Track 3: 2 authors), 1 orchestrator coordinating.

---

## Part 3: Dependency Analysis

### Does Wave 2 Depend on Wave 1 Publication?

**Yes, but gated by domain, not by the entire Wave 1 corpus.**

The dependency rule is: Wave 2 research on Domain X can begin once the Phase 5 Wave 1 domain that X directly extends is **peer-reviewed and in final draft** (publication can follow while Wave 2 is in progress). Wave 2 authors can cite a finalized-draft Wave 1 domain as "expected publication [date]" — they do not need to wait for the live URL.

| Wave 2 Domain | Required Wave 1 Status | Start Condition |
|---------------|----------------------|-----------------|
| Governance | Phase 5 Wave 1 Governance: final draft | June 19 EOD |
| Food Systems | Phase 5 Wave 1 Food: final draft | June 19 EOD |
| Information Resilience | Phase 5 Wave 1 Info Infrastructure: final draft | June 19 EOD |
| Community Security | Phase 5 Wave 1 Security: final draft | June 19 EOD |
| Scaling Pathways | Phase 5 Wave 1 Scaling: final draft | June 19 EOD |

If any Wave 1 domain is **not in final draft by June 19**, the corresponding Wave 2 domain start is deferred by up to 5 days (to June 25) while the Wave 1 domain completes review. If the Wave 1 domain is not finalized by June 25, the Wave 2 domain drops to the July 1 deferred cohort.

### Cross-Domain Dependencies Within Wave 2

| Domain | Must Read (but not wait for) |
|--------|------------------------------|
| Information Resilience | Governance outline (T+3, June 23) for coordination terminology |
| Community Security | Governance outline (T+3, June 23) + Food outline for supply interdependencies |
| Scaling Pathways | Governance T+3 outline + Food T+3 outline + Security T+3 outline |
| Ecosystem Restoration (if added) | Food Systems T+7 draft (June 27) — needs food production framing |
| Institutional Learning (if added) | Governance T+7 draft (June 27) — needs governance evolution framing |

**Practical implication**: Track 3 authors (Security + Scaling) read Track 1+2 T+3 outlines before finalizing their own outlines. This is a read-only dependency — Track 3 does not wait for Track 1+2 first drafts, only outlines.

---

## Part 4: Critical Path Analysis

### Minimum Timeline: June 20 → Publication

The minimum viable timeline for Wave 2 → publication is as follows:

| Milestone | Date | Condition |
|-----------|------|-----------|
| T+0 Kickoff | June 20 | All R-gates green (PHASE_6_WAVE_2_ACTIVATION_CHECKLIST.md Part 1) |
| T+3 Outline submission | June 23 | All 5 authors submit domain outlines |
| T+4 Orchestrator outline review | June 24 | Orchestrator reviews and approves/revises all outlines |
| T+7 First-draft checkpoint | June 27 | **Non-negotiable**: 50% draft, Sections 1–2 narrative-complete |
| T+10 Full first draft | June 30 | All sections complete, citations verified |
| T+12 Peer review feedback | July 2 | Peer reviewers return structured feedback |
| T+14 Revision complete | July 4 | Authors submit revised drafts |
| T+15 Publication readiness gate | July 5 | Orchestrator go/no-go: research complete, peer-reviewed, integration-ready |
| T+20–35 Publication | July 10–25 | Staged publication (2 domains/week) |

**Total critical path for 5-domain Wave 2**: 20–35 days from June 20 kickoff, depending on publication staging pace.

**Wave 3 start condition**: July 5 publication readiness gate met. If gate met on July 5, Wave 3 can begin July 7–10. If gate slips to July 12, Wave 3 begins July 14–15 (1-week slip, within acceptable range for Phase 7 pilot October 15 deadline).

---

## Part 5: Resource Contention Windows

### June 9–15: Overlap with Stockbot Expansion + Resistance-Research Batch 2

This window is the **pre-Wave 2 preparation period** — Wave 2 recruiting, source library assembly, and onboarding kit finalization. Resource contention is highest here because all three initiatives are active:

- **Stockbot expansion**: week 1–2 of June 11–30 expansion (76 total hours; peak June 11–18 at ~15 hrs/week orchestrator coordination).
- **Resistance-research Batch 2**: June 9+ execution, ~60 total hours over 3 weeks, peak June 9–15 (~20 hrs research agent, ~8 hrs orchestrator coordination).
- **Wave 2 pre-work**: author recruitment follow-up (confirming acceptances, sending onboarding kits), source library assembly, domain outline drafting (~15 hrs total June 9–15).

**Mitigation**: Source library assembly and domain outline preparation are batchable (can be done in 2–3 focused sessions June 9–12, before stockbot and Batch 2 reach peak demand). Author recruitment follow-up is low-overhead (email/Matrix, 1–2 hrs total). No orchestrator conflict expected beyond June 12 orchestrator load reaching 12–14 hrs/day — see RESOURCE_CONTENTION_MITIGATION_JUNE_15_30.md for scenario routing.

### June 20–30: Wave 2 First-Draft Window + Stockbot Expansion Peak

This is the highest-intensity Wave 2 period (T+0 through T+10). It overlaps with:

- **Stockbot expansion**: June 20–30 is the validation and live-trading initialization phase (~10 hrs/week orchestrator coordination, lower than June 11–18).
- **Wave 2 orchestration**: June 20–30 requires ~25–35 hrs orchestrator time (author support, outline reviews, T+7 checkpoint assessment, peer reviewer coordination).
- **Wave 1 publication finalization**: June 20–25 includes final publication staging and distribution announcements for Phase 5 Wave 1 corpus (~10–15 hrs orchestrator).

**Total June 20–30 estimated orchestrator load**: 45–60 hrs/week. This exceeds sustainable ~35 hrs/week capacity. See RESOURCE_CONTENTION_MITIGATION_JUNE_15_30.md for scenario A (full parallel) vs. Scenario C (stockbot-first, Wave 2 throttled) resolution.

---

## Part 6: Escalation Triggers

### Trigger 1: Wave 1 Falls More Than 1 Week Behind Schedule

**Definition**: Any Phase 5 Wave 1 domain is not in final draft by June 22 (3-day slip) OR not peer-reviewed by June 25 (10-day slip from target June 15).

**Impact on Wave 2 timeline**:

- 3-day slip (final draft June 22): Wave 2 corresponding domain deferred from June 20 to June 24 start. T+7 checkpoint moves from June 27 to July 1. T+14 full draft moves from July 4 to July 8. Publication readiness gate moves from July 5 to July 9. Net impact: 4-day slip to publication readiness.

- 1-week slip (final draft June 26): Wave 2 corresponding domain deferred to July 1 start. T+7 checkpoint July 8. T+14 full draft July 15. Publication readiness gate July 16. Net impact: 11-day slip to publication readiness.

- 2-week slip (final draft July 3): Wave 2 corresponding domain deferred to July 8 start. T+7 checkpoint July 15. T+14 full draft July 22. Publication readiness gate July 23. Net impact: 18-day slip. **Phase 7 pilot recruitment pressure begins** (needs published corpus by July 25).

**Escalation action** if 2-week slip detected: user decision required on whether to (a) accept Phase 7 pilot delay or (b) reduce Wave 2 scope (publish 3 of 5 domains by July 15, defer 2 domains to August).

### Trigger 2: T+7 First-Draft Checkpoint Missed by an Author

**Definition**: An author does not submit a 50% draft by June 27 EOD (or July 1 for Track 3 deferred domains).

**Response within 24 hours of detection**:

1. Orchestrator contacts author in Matrix domain room + email. Determine: (a) blocked by a question or scope issue (resolvable same day), (b) behind on research (may catch up with 2-day extension), or (c) overcommitted (cannot meet June 30 full-draft deadline).
2. If (a) or (b): grant 2-day extension to June 29. Track 3 domains adjust accordingly. No Publication readiness gate impact if full draft arrives June 30 as scheduled.
3. If (c): scope reduction conversation. Reduce target from 5,000–7,000 words to 3,000–4,000 words (Tier C path). Adjust peer review dates. If author confirms they cannot deliver a 3,000-word first draft by July 2, activate backup assignment (peer mentor takes over outline; orchestrator completes prose pass).

**June 27 checkpoint is non-negotiable as a signal check** — a 0% response by June 27 is a recruitment failure that requires immediate action, not a 1-week extension.

---

## Part 7: Recommendation Summary

The Wave 2 sequencing recommendation is **3 parallel tracks with a 4-day stagger for Track 3**, running June 20–July 5 for the research sprint, followed by a 2-domain/week publication staging cadence July 5–25. This approach:

- Respects all Phase 5 Wave 1 publication dependencies without waiting for the full corpus to be published.
- Maximizes parallelism (3 tracks simultaneously) without exceeding orchestrator coordination capacity (5 authors is the verified ceiling from Phase 5 Wave 1 experience).
- Achieves the first publication readiness gate July 5 (T+15), enabling Phase 7 pilot recruitment to begin July 7–10.
- Preserves 1-week of buffer before the July 15 absolute Phase 7 milestone, accommodating a 1-week slip to Wave 2 if needed without downstream cascade.

Escalation to Scenario B or C (from RESOURCE_CONTENTION_MITIGATION_JUNE_15_30.md) defers Wave 2 Track 3 to July 1 but does not affect Tracks 1 and 2. The non-negotiable anchors — June 20 start and June 27 T+7 checkpoint — hold in all scenarios except a full Wave 2 deferral (which requires explicit user decision).
