---
title: "Phase 2 Batch Sequencing Decision Framework"
subtitle: "Deterministic Decision Tree — Signal Score × Resource Availability → Sequential or Parallel Activation"
created: "2026-06-16"
status: "production-ready — execute at 09:30 UTC after composite score is known"
scope: "Item 104 deliverable — final routing document; converts checkpoint data into executable sequencing decision"
input_from:
  - "DOMAIN_51_POST_EXECUTION_SYNTHESIS.md (composite signal score from Part B)"
  - "PHASE_2_CONTINGENCY_TRIGGER_ASSESSMENT.md (urgency matrix, resource contention scenarios)"
output_to:
  - "PHASE_2_BATCH_SEQUENCING_POST_DOMAIN_51.md (domain-specific activation logistics)"
  - "CHECKIN.md (decision record)"
critical_constraint: |
  Domain 48 must begin before Domain 57 per Item 79 (DOMAIN_48_TIMING_AND_RESOURCE_COORDINATION.md):
  operational mechanics sequencing — send-log template format and execution risk. Domain 48 is always
  the first activation in Phase 2 Batch 1. If parallel activation is needed, use separate send logs
  per Item 79 Section 4 (parallel execution protocol).
all_deadlines_sourced_from: "PHASE_2_HARD_DEADLINE_DEPENDENCY_MAP.md (Item 107, June 10, 2026)"
---

# Phase 2 Batch Sequencing Decision Framework
## Deterministic Decision Tree — Day 7 Signal Score × Resource Availability

*Item 104 deliverable. Prepared June 16, 2026. Execute at 09:30 UTC after composite signal score is known. All decision paths are deterministic — no judgment calls. Every path traces to a sourced urgency constraint or resource threshold.*

---

## How to Use This Document

1. Transfer composite signal score from `DOMAIN_51_POST_EXECUTION_SYNTHESIS.md` Part B.2
2. Confirm agent-hours available June 17-July 15 (user calendar check)
3. Navigate to the matching decision path below
4. Execute actions in order
5. Record selected path in CHECKIN.md at 10:00 UTC
6. Route to `PHASE_2_BATCH_SEQUENCING_POST_DOMAIN_51.md` for domain-specific logistics

---

## Decision Tree

```
START: What is the composite signal score from Item 102 Section 6?

                     ┌─────────────────────────┐
                     │  Composite Signal Score  │
                     └─────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
       Score ≥8            Score 5-7           Score 3-4        Score < 3
      (STRONG)           (MODERATE)            (WEAK)          (FAILURE)
          │                   │                   │                │
          ▼                   ▼                   ▼                ▼
   Check agent-hours    Check agent-hours    → Path C         → Path D
   Jun 17-Jul 15        Jun 17-Jul 15
          │                   │
    ≥100h avail?         ≥84h avail?
    AND calendar?         AND calendar?
          │                   │
    YES ──┼── NO         YES ──┼── NO
          │      │             │      │
          ▼      ▼             ▼      ▼
       Path A  Path B       Path B  Path B
     (Parallel)(Seq.)      (Seq.)  (Seq.)
```

**Summary**: STRONG signal + adequate resources = Path A (Parallel). STRONG signal + insufficient resources = Path B (Sequential). MODERATE signal (regardless of resources) = Path B (Sequential). WEAK signal = Path C (Contingency). FAILURE = Path D (Emergency).

---

## Path A: Parallel Batch Activation — STRONG Signal + ≥100 Agent-Hours

**Prerequisites**:
- Composite signal score: ≥8 / 10
- Agent-hours available June 17-July 15: 100+ hours
- User calendar: available for daily monitoring June 16-30 (parallel requires active oversight)
- Virginia coalition deadline: July 15 (29 days — adequate for parallel start)

**Rationale**: STRONG signal confirms the coalition is engaged and the content is being used. Parallel activation maximizes momentum while engagement is fresh. The contact pools are completely non-overlapping (Domain 48 criminal justice orgs vs. Domain 57 international affairs orgs — verified in `PHASE_2_BATCH_SEQUENCING_POST_DOMAIN_51.md` Section 5), so contact fatigue is zero.

### Path A Timeline

| Phase | Domain | Dates | Actions |
|-------|--------|-------|---------|
| **A.1 — Domain 48 Wave 1** | Domain 48 | June 16-20 | 4 sends staggered (Sentencing Project Jun 16, PPI Jun 17, Brennan Center Jun 18, Worth Rises Jun 20) |
| **A.2 — Domain 57 Wave 1** | Domain 57 | June 20-22 | 3 sends (lead think tank Jun 20, secondary Jun 21, academic Jun 22) — parallel overlap with D48 final send |
| **A.3 — Secondary Checkpoint** | D48 + D57 | June 23 | Assess: D48 open rate ≥40%, Bitly ≥2 clicks, reply rate ≥20%; D57 reply expected 48-72h after sends |
| **A.4 — Domain 58 Monitor** | Domain 58 | Daily June 16-30 | Check scotus.gov/opinions each morning; 4-hour distribution protocol on ruling day |
| **A.5 — Domain 49 Activation** | Domain 49 | July 1 | Quality gate pre-check (Section 0 of runbook); research and update begin |
| **A.6 — Domains 50/54 Activation** | Domain 50 | July 1 | Quality gate + Gist creation; August 1 deadline for Lambda Legal/AT4E |
| | Domain 54 | July 15 | Gist creation; sends July 17-25 |

**Domain 48 must precede Domain 57** (Item 79 constraint): The first Domain 48 send (June 16) precedes the first Domain 57 send (June 20) by 4 days. This satisfies the operational mechanics sequencing requirement. Send logs are separate per Item 79 Section 4 parallel execution protocol. Two separate browser tabs, two separate tracking documents, no cross-domain entry.

**Agent-hours breakdown (Path A)**:
- Domain 48 execution (sends + monitoring + Day 23 checkpoint): 25-30 hours
- Domain 57 execution (sends + monitoring): 20-25 hours
- Domain 58 monitoring (passive, with triggered 4-hour burst on ruling): 5-8 hours standing + 8-10 hours on ruling day
- Domain 49 research activation (July 1 start, pre-check gate + first week): 15-20 hours
- Total June 17-July 15: 65-88 hours research + 20-25 hours logistics = **85-113 hours**

**Contingency within Path A**: If June 23 secondary checkpoint shows Domain 48 reply rate <20%, hold Domain 57 Tier 2 sends (pause but do not cancel). Continue Tier 1 monitoring for Domain 57. Decide by June 25 whether to extend Domain 57 Tier 2 window or defer to July.

**User decision required**: Yes — approve parallel activation (resource commitment). No further user decisions needed until June 23 checkpoint unless contingency triggers.

### Path A Pros and Cons

| | Detail |
|--|--------|
| **Pro — momentum** | STRONG signal means coalition is engaged NOW; parallel activation while attention is high yields better response velocity |
| **Pro — deadline coverage** | All four Phase 2 domains (48, 49, 50, 57) hit their advocacy windows with 15+ days of buffer |
| **Pro — coalition network** | Domain 51 → Domain 48 → Domain 57 creates a thematic sequence (campaign finance → criminal justice → international norms) that amplifies each prior send |
| **Con — execution intensity** | 85-113 hours June 17-July 15 (6-8 hrs/day) is a demanding pace; quality declines if coordination overhead increases |
| **Con — dual-send risk** | Two domain send logs simultaneously active June 20-22; template confusion risk is LOW but non-zero per Item 79 Section 5 |
| **Con — user monitoring load** | Parallel requires daily Bitly check + Gmail monitoring for two domains simultaneously June 20-22 |

---

## Path B: Sequential Batch Activation — MODERATE Signal (or STRONG with Insufficient Resources)

**Prerequisites**:
- Composite signal score: 5-7 (MODERATE); OR score ≥8 but agent-hours <100 or calendar constrained
- Agent-hours available June 17-July 15: 84-99 hours (sufficient for sequential)
- User calendar: monitoring available June 16-30 with focus on one domain at a time

**Rationale**: MODERATE signal means engagement is real but not at the pace that justifies the coordination overhead of parallel activation. Sequential execution allows each domain to complete and stabilize before the next begins, reducing execution risk and user monitoring load. The UNGA 82 August 10 deadline for Domain 57 remains achievable with June 23-25 activation (47 days of buffer).

### Path B Timeline

| Phase | Domain | Dates | Actions |
|-------|--------|-------|---------|
| **B.1 — Domain 48 Wave 1** | Domain 48 | June 16-20 | 4 sends staggered (same as Path A) |
| **B.2 — Domain 48 Monitoring** | Domain 48 | June 20-23 | Passive monitoring: Bitly, Gmail, Campaign Monitor |
| **B.3 — Secondary Checkpoint** | Domain 48 | June 23 | Assess D48 metrics. Decision point for Domain 57 activation |
| **B.4a — IF D48 ≥40% reply rate** | Domain 57 | June 23-25 | Proceed to Domain 57 Wave 1 sends (3 contacts, same as Path A A.2) |
| **B.4b — IF D48 20-39% reply rate** | Domain 57 | Hold → July 1 | Re-evaluate at July 1 checkpoint |
| **B.4c — IF D48 <20% reply rate** | Domain 57 | ESCALATE | Escalate to user for Phase 2 pathway decision |
| **B.5 — Domain 58 Monitor** | Domain 58 | Daily June 16-30 | Same as Path A |
| **B.6 — Domain 49 Activation** | Domain 49 | July 1 | Same as Path A |
| **B.7 — Domains 50/54 Activation** | Domains 50, 54 | July 1, July 15 | Same as Path A |

**June 23 secondary checkpoint decision** (autonomous — no user input required if above thresholds):
```
Domain 48 Day 7 metrics (measured June 23):

IF email open rate ≥40% AND reply rate (any) ≥20%:
  → Proceed to Domain 57 activation June 23-25. Record in CHECKIN.md.

ELSE IF email open rate 25-39% OR reply rate 10-19%:
  → Hold Domain 57. Set July 1 re-evaluation checkpoint.
  → Notify user: "Domain 48 moderate engagement; Domain 57 deferred to July 1 decision point."

ELSE IF email open rate <25% OR zero replies:
  → Escalate to user for Domain 57 pathway decision.
  → Options: A) proceed Domain 57 July 1-5; B) hold Domain 57 for UNGA-adjacent distribution only; C) cancel Domain 57 2026 activation.
  → User deadline: 72 hours (June 26 18:00 UTC)
```

**Agent-hours breakdown (Path B)**:
- Domain 48 execution: 25-30 hours
- Domain 57 execution (if activated June 23-25): 20-25 hours
- Domain 58 monitoring: 5-8 hours + 8-10 on ruling day
- Domain 49 activation (July 1): 15-20 hours
- Total June 17-July 15: 65-83 hours research + 18-22 hours logistics = **83-105 hours**

**User decision required**: Minimal — only if Domain 48 June 23 reply rate <20%.

### Path B Pros and Cons

| | Detail |
|--|--------|
| **Pro — sustainable pace** | 30-40 research hours per week; coalition momentum builds steadily without coordination overhead |
| **Pro — contingency buffer** | If Domain 48 needs follow-up (send bounces, contact update required), 2-3 day slip doesn't affect Domain 57 timeline |
| **Pro — quality focus** | One domain at a time allows closer attention to response content and adaptation |
| **Con — Domain 57 timing** | If June 23 checkpoint triggers hold, Domain 57 moves to July 1-5 (still 36-day buffer to August 10 — acceptable) |
| **Con — momentum risk** | Coalition engagement velocity may stall if Phase 2 activation takes longer; counter by ensuring Domain 48 follow-ups reference Domain 51 prior engagement |

---

## Path C: Contingency Activation — WEAK Signal (Score 3-4)

**Prerequisites**:
- Composite signal score: 3-4
- Diagnostics must complete June 16-17 before Phase 2 sends begin
- User must respond to escalation email by June 17, 18:00 UTC

**Rationale**: WEAK signal requires root-cause diagnosis before expanding to additional domains. The risk is not content quality — it is delivery failure or list friction. Diagnosis takes 24-48 hours. Domain 48 cannot wait longer than 48 hours (July 15 Virginia deadline requires June 19 start at the absolute latest to maintain 26 days of response buffer). Domain 49 redistricting window is immovable.

### Path C Actions (June 16-17)

**June 16, 09:30-10:30 UTC — Diagnostics:**
1. Check Campaign Monitor / email client: did all 5 contacts receive the email? Were there bounces?
2. Click Domain 51 Bitly link manually: does it resolve? Is the Gist live?
3. Gmail search for any missed replies using corrected contact emails (see `DOMAIN_51_POST_EXECUTION_SYNTHESIS.md` Bug Warning)
4. Check DOMAIN_51_DISTRIBUTION_SEND_LOG.md: confirm send timestamps are recorded

**June 16, 11:00 UTC — Escalation email to user** (template from `DOMAIN_51_JUNE_16_DECISION_LOGIC.md` Section 3.3):
- Include signal breakdown by metric
- Present three options: Option A (stakeholder substitution), Option B (framing revision), Option C (hold Phase 2 pending Day 30 assessment)
- User decision deadline: June 17, 18:00 UTC

**June 17, 10:00 UTC — Domain 48 pre-flight regardless of user response:**
- Execute Domain 48 pre-flight verification (5 minutes)
- Confirm sends will execute June 19-24 window (2-day slip from STRONG/MODERATE path — still achieves July 15 Virginia deadline with 21 days of buffer)

**June 17, 18:00 UTC — Automatic default if no user response:**
- Hold Domain 57 (no action)
- Proceed with Domain 48 June 19 send
- Proceed with Domain 49 July 1 activation
- Execute Day 30 checkpoint June 30

### Path C Timeline

| Phase | Domain | Dates | Actions |
|-------|--------|-------|---------|
| **C.1 — Diagnostics** | Domain 51 | June 16-17 | Root-cause diagnosis + escalation email |
| **C.2 — Domain 48 Activation** | Domain 48 | June 19-24 | Wave 1 sends (2-day slip from STRONG/MODERATE) |
| **C.3 — Domain 57 Status** | Domain 57 | User decision June 17 | Hold until user decides; then July 1-5 if approved |
| **C.4 — Domain 58 Monitor** | Domain 58 | Daily June 16-30 | Same as all paths |
| **C.5 — Day 30 Checkpoint** | All domains | June 30 | Extended engagement assessment; Phase 2 re-evaluation |
| **C.6 — Domain 49 Activation** | Domain 49 | July 1 | IMMOVABLE — does not wait |
| **C.7 — Domains 50/54** | Domains 50, 54 | July 1, July 15 | Same as all paths |

**Domain 57 in Path C**: If user approves Option A or B (re-send + framing revision), Domain 57 activates July 1-5 with 36-day buffer before August 10 UNGA deadline. If user approves Option C (hold Phase 2), Domain 57 defers to a July 15-20 window (25-day buffer — still achieves UNGA deadline but with reduced margin). Domain 57 is NOT cancelled in any WEAK path — it is delayed.

**User decision required**: Yes — required by June 17, 18:00 UTC for Domain 57 timing decision.

### Path C Pros and Cons

| | Detail |
|--|--------|
| **Pro — diagnostic value** | 24-48h diagnosis identifies whether WEAK signal reflects delivery failure, list quality, or content mismatch — critical for improving Domain 48+ sends |
| **Pro — all deadlines still achievable** | Domain 48 June 19-24 achieves July 15; Domain 49 July 1 immovable; Domain 57 July 1-5 achieves August 10 |
| **Con — momentum cost** | Domain 51 coalition has not activated; Domain 48 starts without warm referral momentum |
| **Con — user engagement required** | Path C requires user input by June 17 (tight turnaround); if user unavailable, default activates which may not be optimal |

---

## Path D: Emergency Protocol — FAILURE Signal (Score < 3)

**Prerequisites**:
- Composite signal score: below 3
- Zero opens + zero Bitly clicks + zero replies confirmed by 09:30 UTC
- Emergency actions begin immediately (within 2 hours of determination)

**Rationale**: Score below 3 with confirmed sends indicates a delivery-level failure, not a strategy failure. The analysis is sound. The distribution mechanism has a problem. Root-cause diagnosis is the immediate priority. All Phase 2 domains proceed on their deadline-driven schedules because they do not depend on Domain 51 delivery success — they are self-contained research products.

### Path D Actions (June 16, 09:30-12:00 UTC)

1. **Delivery verification** (09:30-10:00): Check email client sent folder, bounce notifications, Campaign Monitor delivery log. Determine: confirmed-sent-but-not-opened vs. delivery-failed.

2. **Bitly link test** (10:00): Click link manually. If Gist loads: delivery succeeded but contacts haven't clicked. If Gist 404s: Bitly link or Gist has a problem — recreate immediately per `DOMAIN_51_CONTINGENCY_SB_299_FALLBACK.md`.

3. **Emergency re-send option** (10:00-11:00): If delivery failed, re-send to org inboxes (info@campaignlegal.org, info@issueone.org) as fallback. This is within 24-72 hours of initial send — still within engagement window.

4. **User escalation email** (11:00): Send emergency notification per `DOMAIN_51_JUNE_16_DECISION_LOGIC.md` Section 3.4 template. User decision deadline: June 17, 24 hours.

5. **Domain 48 pre-flight** (11:00-12:00): Execute regardless of Domain 51 status. Virginia July 15 deadline is immovable.

### Path D Timeline

| Phase | Domain | Dates | Actions |
|-------|--------|-------|---------|
| **D.1 — Emergency Protocol** | Domain 51 | June 16-17 | Delivery diagnosis + emergency re-send if feasible |
| **D.2 — Domain 48 Activation** | Domain 48 | June 19-24 | Same as Path C (2-day slip; July 15 still achievable) |
| **D.3 — Domain 57 Hold** | Domain 57 | User decision June 17 | Defer; if approved, activate July 1-5 or later |
| **D.4 — Domain 58 Monitor** | Domain 58 | Daily June 16-30 | SCOTUS monitor active |
| **D.5 — Day 30 Checkpoint** | All domains | June 30 | Re-evaluate with full picture |
| **D.6 — Domain 49 Activation** | Domain 49 | July 1 | IMMOVABLE |
| **D.7 — Domains 50/54** | Domains 50, 54 | July 1, July 15 | Same as all paths |

**Key principle**: Domain 51 FAILURE does not cascade to Domain 48 quality. Domain 48 research is independently production-ready. The Virginia coalition will receive the criminal justice analysis regardless of whether the campaign finance analysis was successfully delivered. Phase 2 proceeds.

---

## Resource Loading Table — All Scenarios

| Scenario | Path | Agent-Hours Jun 17-Jul 15 | User Calendar Jun 17-Jul 15 | Domain 57 Timing | Feasibility |
|----------|------|--------------------------|---------------------------|-----------------|-------------|
| STRONG + ≥100h | A | 85-113h | Daily Jun 16-30 | Jun 20-22 | RECOMMENDED if resources available |
| STRONG + <100h | B | 83-105h | Moderate Jun 16-Jul 5 | Jun 23-25 conditional | RECOMMENDED if resource-constrained |
| MODERATE (any) | B | 83-105h | Moderate Jun 16-Jul 5 | Jun 23-25 conditional | STANDARD recommended baseline |
| WEAK | C | 50-80h | High Jun 16-17; moderate Jul 1-15 | Jul 1-5 if user approves | CONTINGENCY |
| FAILURE | D | 40-70h | Very high Jun 16-17; moderate Jul 1-15 | Jul 1-5 or later | EMERGENCY |

**Reading the table**: The difference between Path A and Path B is primarily the Domain 57 timing (June 20-22 vs. June 23-25). Both paths require similar agent-hours and achieve all deadline targets. The choice is whether signal strength justifies the higher coordination load of parallel sends.

---

## Critical Constraint Summary

*These constraints cannot be violated by any path selection.*

1. **Domain 48 before Domain 57** (Item 79 constraint): In all paths, Domain 48 sends begin before Domain 57 sends begin. In Path A (parallel), this means Domain 48 starts June 16-17 and Domain 57 starts June 20 (4-day gap). In Paths B/C/D, Domain 48 fully precedes Domain 57 activation. If parallel activation is needed, use SEPARATE SEND LOGS — do not combine into a single tracking document.

2. **Domain 49 July 1 is immovable**: Cannot be deferred by any signal level. Redistricting filing windows are closing NOW. This is documented as IMMOVABLE in Item 107.

3. **Domain 58 is ruling-triggered**: Cannot be scheduled or deferred. SCOTUS monitor must be active daily regardless of path selected.

4. **Domain 48 send by June 20** (STRONG/MODERATE paths): Virginia July 15 deadline requires first send by June 20. In WEAK/FAILURE paths, the deadline shifts to June 24 at the absolute latest (21 days before July 15 — minimum viable buffer for response and follow-up).

5. **Contact list correction is permanent**: The checkpoint metrics template (`DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md`) lists wrong contacts. The corrected contacts (Erin Chlopak, info@issueone.org, Darius Kemp, Jenny Farrell, Trent Lange) are the authoritative send list for all engagement analysis in this framework. Do not use the template's contact list for any inbox searches, response monitoring, or engagement scoring.

---

## Quick Reference Card

```
COMPOSITE SCORE → PATH

≥8 + ≥100h calendar: PATH A (Parallel)
  D48: Jun 16-20 | D57: Jun 20-22 | D49: Jul 1 | D58: Ruling

5-7 OR (≥8 + <100h): PATH B (Sequential)  
  D48: Jun 16-20 | D57: Jun 23-25 conditional | D49: Jul 1 | D58: Ruling
  
3-4: PATH C (Contingency)
  Diagnostics Jun 16-17 | D48: Jun 19-24 | D57: User decision Jun 17 | D49: Jul 1

<3: PATH D (Emergency)
  Emergency protocol Jun 16-17 | D48: Jun 19-24 | D57: Hold | D49: Jul 1

ALL PATHS:
  Domain 48 always activates
  Domain 49 July 1 is immovable  
  Domain 58 monitoring is always active
  Domain 48 sends before Domain 57 sends (always)
```

---

## Routing Checklist (Execute at 10:00 UTC)

- [ ] Composite score recorded: ___ / 10
- [ ] Selected path: A / B / C / D
- [ ] Agent-hours confirmed: ___h available June 17-July 15
- [ ] Domain 48 pre-flight complete (contact list, Gist URL, send log staged)
- [ ] Domain 57 Gist URL verified live
- [ ] Domain 58 SCOTUS monitor confirmed active
- [ ] Domain 49 July 1 activation confirmed on calendar
- [ ] Decision recorded in CHECKIN.md
- [ ] Routing transferred to `PHASE_2_BATCH_SEQUENCING_POST_DOMAIN_51.md` Section [2.1 / 2.2 / 3]

---

*Prepared June 16, 2026. Item 104 deliverable. Sources: `DOMAIN_51_POST_EXECUTION_SYNTHESIS.md`, `PHASE_2_CONTINGENCY_TRIGGER_ASSESSMENT.md`, `PHASE_2_HARD_DEADLINE_DEPENDENCY_MAP.md` (Item 107, June 10, 2026), `DOMAIN_48_TIMING_AND_RESOURCE_COORDINATION.md` (Item 79, June 5, 2026), `DOMAIN_51_JUNE_16_DECISION_LOGIC.md`, `PHASE_2_BATCH_SEQUENCING_POST_DOMAIN_51.md` (June 6, 2026).*
