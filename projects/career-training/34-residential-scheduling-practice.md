---
module: 34
title: "Residential Scheduling Practice: Lookahead Planning and Recovery Logic"
discipline: ["scheduling", "project-management", "field-execution", "planning"]
audience: "Residential GCs and superintendents managing live job schedules"
status: reference
created: 2026-06-27
tags: [career-training, scheduling, last-planner-system, lookahead, constraint-management, recovery-planning, residential-pm]
estimated-reading-time: 4 hours
---

# Residential Scheduling Practice: Lookahead Planning and Recovery Logic

> **Purpose.** Every residential GC superintendent runs a schedule in their head and on a calendar. Most operate from gut feel and field experience. This module teaches the one practice that separates GCs with predictable delivery from those who scramble to meet deadlines: the 3-week lookahead schedule paired with a constraint-identification process. Coupled with systematic recovery planning, this discipline eliminates the crisis meetings that plague residential projects.

> **Distinction from Module 03.** Module 03 teaches CPM scheduling theory and industrial project execution. This module teaches the week-to-week, field-facing discipline a residential superintendent actually uses to keep a job on track. It assumes the master schedule already exists; it teaches how to operate within it.

---

## Table of Contents

1. [Why Master Schedules Fail in the Field](#1-why-master-schedules-fail-in-the-field)
2. [The 3-Week Lookahead Format and Cadence](#2-the-3-week-lookahead-format-and-cadence)
3. [Last Planner System Principles and Constraint Identification](#3-last-planner-system-principles-and-constraint-identification)
4. [Weekly Coordination and the Constraint Log](#4-weekly-coordination-and-the-constraint-log)
5. [Recovery Planning: Acceleration, Phasing, and Resource Addition](#5-recovery-planning-acceleration-phasing-and-resource-addition)
6. [Documentation and Schedule Change Orders](#6-documentation-and-schedule-change-orders)
7. [Field Reporting Integration](#7-field-reporting-integration)
8. [Templates and Tools](#8-templates-and-tools)

---

## 0. Mental Model — The Lookahead Is Your Operating Schedule

Most residential GCs maintain two schedules: the master schedule (often created during bidding) and the field reality. The field reality is what the superintendent remembers, what trades are actually scheduled, and what the owner sees. When these diverge, one of two things happens: the master schedule is abandoned as irrelevant, or it's maintained separately and ignored by the team actually building.

The **3-week lookahead is the bridge.** It is detailed enough to drive weekly decisions, but updated frequently enough to remain accurate. A master schedule is a contract document. A lookahead is an operational tool. A superintendent who maintains a living lookahead and updates it every Friday knows exactly what needs to happen next week, what constraints must be removed before trades can proceed, and what the recovery options are if something slips.

The business case for this discipline:
- **Schedule predictability:** Projects that hit their schedules attract repeat clients and reduce financing costs.
- **Trade coordination:** Each sub knows when they're called, what preconditions must be met, and what they're expected to deliver.
- **Problem visibility:** Constraints bubble up a week in advance instead of causing a crisis on Monday.
- **Owner communication:** You can tell the owner on Monday what's happening next week and explain any changes before they become surprises.

---

## 1. Why Master Schedules Fail in the Field

### 1.1 The Reality Gap

A typical residential master schedule is created during pre-construction planning. It reflects the bid-phase assumptions about:
- Material delivery timing
- Trade availability and crew sizes
- Weather and site conditions
- Inspection and approval timing
- Design decisions and clarifications

By week four of construction, half these assumptions are wrong. Materials arrive late. A trade that was available for month three is now booked through month four. Weather delays framing. Inspections are backlogged. The owner changed the kitchen finishes.

The superintendent who relies solely on the master schedule is working from fiction.

### 1.2 The Constraint Problem

A constraint is any condition that must be satisfied before a trade can begin or complete their work. On a residential project, examples include:
- **Procurement:** Roofing truss delivery; cabinet shop completion
- **Previous trade:** Framing must be complete before rough MEP; rough MEP must pass inspection before drywall
- **Inspections:** Framing rough cannot close to drywall until framing inspection is passed
- **Approvals:** Kitchen cabinet installation cannot begin until cabinet submittals are approved
- **External conditions:** Rebar must be delivered; pool deck can't pour until soil compaction tests are passed

The master schedule lists these dependencies in abstract. The lookahead identifies them in concrete terms for the specific three weeks ahead: "Cabinet delivery date is 4/22; approval of final samples needed by 4/12."

A superintendent who does not run a constraint log week-to-week discovers constraints too late. "Why isn't electrical starting?" "The permit for the electrical upgrade wasn't issued." Two-week delay. The constraint was known 30 days prior; it just wasn't being actively tracked.

---

## 2. The 3-Week Lookahead Format and Cadence

### 2.1 Why 3 Weeks?

A 3-week window is the minimum lookahead horizon for residential trades:
- Most material orders can be placed within 3 weeks (some long-lead items require earlier action).
- Inspection slots are typically available within 7–14 days (gives two attempts if first fails).
- Trade crews can be called in (a trade booked out 6+ weeks in advance often slips or cancels).
- Owner decisions can be accelerated (not always possible, but 3 weeks is usually enough time).

A 1-week lookahead is too short; problems you can't solve in the next week cascade forward. A 6-week lookahead becomes too abstract to be useful; circumstances change weekly.

### 2.2 The Lookahead Format

A 3-week lookahead identifies every activity scheduled in those three weeks, its preconditions, and whether the preconditions are satisfied.

**Minimum data per activity:**
- Activity name (Framing, Rough Electrical, etc.)
- Scheduled start and end dates
- Assigned trade/crew
- Specific scope (which areas if applicable)
- Key preconditions (what must be complete before this work starts)
- Status: Ready, Constrained, or At-Risk
- Owner/GC actions required

**Sample 3-Week Lookahead for weeks 10–12 of a residential project:**

| Activity | Scheduled | Duration | Trade | Scope | Preconditions | Status | Constraint |
|---|---|---|---|---|---|---|---|
| Concrete slab prep & pour | 4/10–4/12 | 3 days | GC + concrete sub | Main residence slab | (1) Forms set & measured; (2) Rebar complete; (3) Subgrade compacted | Ready | None — forms done; rebar approved |
| Rough plumbing (DWV/supply) | 4/13–4/20 | 6 days | Plumbing sub | Main residence | (1) Underslab plumbing passed; (2) Slab cured 7 days; (3) Framing complete | Constrained | Framing not complete until 4/18; plumbing starts 4/13 — conflict. Reschedule plumbing to 4/19 start. |
| Framing completion | 4/15–4/18 | 4 days | Framing crew (phase 2) | Master + guest | (1) Preliminary rough passed; (2) Materials on site | At-Risk | Soffit lumber special order; delivery promised 4/14 but not confirmed. ACTION: GC to confirm delivery by 4/11. |
| Framing rough inspection | 4/18 | 1 day | AHJ | Main building | (1) Framing complete; (2) Inspector called 48 hrs prior | Ready | None — confirm inspector call 4/16. |
| Rough electrical | 4/21–4/27 | 5 days | Electrician | Main building | (1) Framing rough passed; (2) Panel location marked; (3) Load calc complete | Ready | None — panel location approved; load calc submitted. |
| Pool deck — soil compaction test | 4/12 | 1 day | Soils / test lab | Pool area | (1) Fill material placed; (2) Test lab scheduled | Constrained | Fill material delivery late (scheduled 4/8, now promised 4/10). Reschedule test to 4/13. |

### 2.3 Update Cadence

The lookahead is updated and reissued every Friday at 4:00 PM for the following three weeks (rolling window). Every superintendent, every key sub, and the owner receive the updated lookahead before they leave Friday. This practice:
- Ensures everyone sees the same schedule.
- Gives the team the weekend to think about constraints.
- Provides a clear picture for Monday morning (no ambiguity about what's happening).

**Friday update protocol:**
1. GC superintendent reviews the week just completed. Log any slippage, constraint removals, or changes to forecast.
2. Update the lookahead with new information (material deliveries confirmed, inspection dates, trade availability).
3. Flag any activity that was scheduled in the past week but did not occur — why?
4. Identify all constraints for the following three weeks. Assign an owner to each: GC action, sub responsibility, owner decision, etc.
5. Issue via email to owner, all subs, and project team. Include a cover email highlighting key decisions or risks.

---

## 3. Last Planner System Principles and Constraint Identification

### 3.1 Last Planner System Overview

The **Last Planner System (LPS)** is a production control method that reverses traditional planning: instead of a scheduler creating a detailed schedule and pushing it down to crews, the crews (the "last planners") commit to what they can realistically complete in the week ahead. This alignment between planning and execution dramatically improves on-time performance.

Core principle: **Only schedule work that is "ready" — all preconditions satisfied.**

LPS is particularly powerful on residential projects because the number of trades and handoff points creates natural constraint accumulation.

### 3.2 The Constraint Identification Discipline

Every Thursday, the superintendent and all key subs participate in a 30-minute **constraint-clearance meeting.** The purpose is to identify and address every barrier to the work scheduled for the following 3 weeks.

**Constraint meeting agenda:**

1. **Review prior week performance.** What was scheduled last week? What was actually completed? Why were there gaps?
2. **Examine the next 3 weeks activity-by-activity.** For each activity, the responsible trade answers: "Can you be ready to start on [date]?" If no, what's missing?
3. **Identify the constraint.** For every "no," identify the specific blocker: "Roofing trusses not delivered" vs. "We're waiting for the inspector" vs. "Owner hasn't approved the finish selection."
4. **Assign action and owner.** Who is responsible for removing the constraint? What is the deadline?
5. **Reschedule or escalate.** If the constraint cannot be removed by the start date, reschedule the activity. If the constraint is a critical path item, escalate to the PM/GC owner.

**Sample constraint log entry:**

| Week | Activity | Constraint | Owner | Deadline | Status | Resolution |
|---|---|---|---|---|---|---|
| 10–12 | Rough plumbing start | Framing completion runs to 4/18, plumbing scheduled 4/13 | GC | 4/11 | Open | Framing crew adding labor; revised completion 4/16. Plumbing rescheduled to 4/17. |
| 10–12 | Pool deck soil test | Fill material delivery not confirmed | GC | 4/9 | Open | Material supplier confirms delivery 4/10. Test rescheduled to 4/13. |
| 10–12 | Electrical rough start | Electrician not yet quoted | GC | 4/14 | Closed | Quote received 4/6; electrician booked for 4/21 start. |

### 3.3 Participation and Accountability

The constraint clearance must include the **decision-makers:** not just the foreman or project manager, but the sub owner or crew leader who can commit the crew to a date. A general sub foreman cannot commit the commercial electrician's time; the electrical sub owner must be present.

**Attendees:**
- GC superintendent (chair)
- GC project manager
- Sub owners/crew leads for framing, mechanical, electrical, plumbing
- Owner (optional but recommended)

If a critical sub cannot attend, the constraint meeting notes their absence and their commitments are assumed at-risk.

---

## 4. Weekly Coordination and the Constraint Log

### 4.1 The Constraint Log as Your Primary Tool

The constraint log is a simple spreadsheet maintained throughout the project. It is the truth record of what's blocking progress and what the GC is doing to clear it.

**Minimum columns:**
- Constraint ID (C-001, C-002, etc.)
- Activity affected (which work is waiting?)
- Constraint description (what specifically is missing?)
- Owner (GC, Sub A, Owner, Supplier, AHJ)
- Target removal date (when must this be resolved for the schedule to work?)
- Status (Open, In Progress, Resolved, Rescheduled)
- Action taken
- Actual resolution date
- Root cause (if applicable, for lessons learned)

**Why this matters:** A superintendent maintaining a constraint log is making the invisible visible. Every week, the log shows the team what's in the way and who's responsible. This creates accountability. An owner who sees "Permit for electrical upgrade — Target 4/12 — Status: Overdue — Responsibility: AHJ" knows they have a problem that needs escalation.

### 4.2 Daily Coordination for the Week Ahead

Monday morning meeting (15 minutes):
- Review the week's schedule: what's starting today?
- Any changes from Friday's lookahead? (Material arrived early, trade called off, inspection scheduled)
- Identify any same-day constraints: "What do you need from me before you start?"

Daily stand-up (5–10 minutes, late afternoon):
- What was actually completed today vs. scheduled?
- What's blocking tomorrow?
- Any decisions needed before tomorrow's work?

This daily micro-coordination catches problems within 24 hours, not the following week.

---

## 5. Recovery Planning: Acceleration, Phasing, and Resource Addition

### 5.1 When Recovery Is Needed

A recovery is triggered when an activity slips to the point that it threatens the scheduled completion date. Recovery decisions are rarely ideal; the superintendent is choosing among imperfect options.

**Recovery triggers:**
- A critical-path activity is more than 3–5 days behind schedule.
- A non-critical activity has consumed its float and now threatens critical path.
- The owner's deadline is in jeopardy.

### 5.2 Recovery Options

**Option 1: Acceleration — Add Labor or Shift to Overtime**

Add crew size or shift to 10-hour days. Cost: $1,500–$5,000/week in labor premium (overtime premium + supervision cost).

**Preconditions:**
- The work is labor-constrained, not material or sequence constrained.
- Crew addition doesn't create coordination chaos (overcrowding).
- The sub has labor available.

**Best for:** Framing slippage, rough MEP, finish work.

**Example:** Framing is 4 days behind due to unexpected structural modifications. Add 2 additional carpenters at premium rate. Cost: ~$3,000. Schedule recovery: 3 days. Net: 1-day schedule compression at acceptable cost.

**Option 2: Phasing — Resequence Work**

Reorganize trade sequence to parallelize work that was planned serially. Example: Start rough electrical while rough plumbing is still ongoing, if coordination can be managed.

Cost: $0–$2,000 (coordination overhead).

**Preconditions:**
- The trades can physically work in the same space.
- Inspection requirements don't mandate sequence (rough MEP must pass before drywall).
- No safety or quality compromise.

**Best for:** Situations where float exists in related activities.

**Example:** Rough plumbing and electrical were planned sequentially (plumbing 4/13–4/20, electrical 4/21–4/27). Compressed schedule allows electrical to start on 4/18 once rough plumbing completes its water supply rough-in. Risk: coordination and inspection conflicts. Benefit: 3-day schedule recovery with no cost premium.

**Option 3: Add Resources or Equipment**

Deploy a second crew, rent equipment (crane, lift), or shift procurement strategy. Cost: highly variable.

**Example:** Concrete cure is delaying framing. Options: (a) Rent temporary heating enclosure to accelerate curing. Cost: $1,200. Recovery: 2–3 days. (b) Switch to fast-set concrete additive; higher material cost. Cost: $800–$1,200. Recovery: 1–2 days.

**Option 4: Accept the Delay and Extend Project Duration**

Notify owner, adjust completion date, and revise financials. Cost: extended general conditions (superintendent, site overhead, insurance).

**Preconditions:**
- Owner accepts the new date.
- Contract allows schedule adjustment (check your GMP/T&M provisions).
- No owner penalty clause for late delivery.

**Best for:** When the delay is force majeure (weather, major permitting delay, owner-caused condition).

### 5.3 Selecting a Recovery Strategy

Create a recovery options matrix:

| Option | Cost | Schedule Recovery | Risk | Preconditions | Recommendation |
|---|---|---|---|---|---|
| Add labor (framing) | $3,000 | 3 days | Low | Sub has crew | First choice — low risk |
| Parallelize electrical/plumbing | $500 | 3 days | Medium | Coordination feasible | Second choice if coordination can be managed |
| Temporary heating (concrete) | $1,200 | 2 days | Low | Equipment available | Accept if delay > 5 days |
| Extend schedule | $8,000+ (4-week GC) | 0 recovery | Low | Owner agrees | Only if acceleration cost exceeds extension cost |

Present this matrix to the owner. Let them decide: do you want to spend $3,000 for acceleration, or extend 4 weeks and eat the $8,000 general condition cost?

### 5.4 Documentation When Recovery Involves Cost

Any recovery option that has a cost implication must be documented as a potential change order or contract amendment:
- Acceleration labor premium: COR (Change Order Request)
- Extended general conditions from owner-caused delay: COR and schedule adjustment
- Owner decision to extend vs. accelerate: written owner directive with cost implications

This prevents disputes: "We accelerated at your request; the cost is $3,000." vs. "Why did labor costs spike?"

---

## 6. Documentation and Schedule Change Orders

### 6.1 Schedule Impact as a Change Order Element

When a constraint or issue extends the project completion date, the cost impact is real — extended general conditions. This must be documented.

**Example scenario:**
- Original schedule: 120 days, completion 7/15/2025.
- Electrical permit delayed (AHJ); framing inspection delayed 10 days.
- New completion date: 7/25/2025 (10-day extension).
- General conditions cost (GC superintendent + PM + site overhead + equipment): $2,000/week.
- Cost impact: $2,000 × 1.4 weeks = $2,800 in extended GC.

This $2,800 is a legitimate cost to recover via change order — documented and submitted when the delay is confirmed.

### 6.2 "Delay Impact" vs. "Defective Condition" Disputes

When a trade delays and you must accelerate to compensate, clarify the cost category:
- **Delay caused by sub defect/non-performance:** Sub pays for acceleration (backcharge).
- **Delay caused by owner condition/decision:** Owner pays via change order.
- **Delay caused by force majeure or both parties:** Negotiate shared cost.

Document the cause: "Framing delay due to owner-directed structural changes = owner pays $3,000 acceleration cost" vs. "Framing delay due to crew availability (sub issue) = sub absorbs acceleration cost."

---

## 7. Field Reporting Integration

### 7.1 The Daily Log as Schedule Feedback

The daily field report must capture actual vs. scheduled progress for every activity. This data feeds the Friday lookahead update.

**Minimum daily log data:**
- Date and weather
- Trades on site and crew size
- Work completed (by activity and trade)
- Work interrupted or rescheduled (why?)
- Deliveries received
- Inspections completed or rescheduled
- Decisions made or escalated
- Constraints resolved or new constraints identified

**Sample daily log entry:**

> **4/15/2025 — Friday**
> 
> **Weather:** 72°F, clear. No weather delays.
> 
> **Crew on site:**
> - Framing: 6 carpenters + foreman (frames; 85% complete)
> - Rough plumbing: 2 plumbers (DWV lines, main building)
> 
> **Work completed:**
> - Framing: Master bedroom and guest room wall framing; ridge beam set; need one more day for collar ties and blocking.
> - Rough plumbing: DWV main stack and kitchen/bathrooms supply.
> 
> **Schedule vs. actual:**
> - Framing scheduled to complete 4/18 — on track.
> - Rough plumbing scheduled to start 4/19 after framing rough inspection — ahead of schedule; plumbing 85% done.
> 
> **Constraints removed:**
> - Soffit lumber delivery confirmed for 4/14 — received on time; no schedule impact.
> 
> **New constraints:**
> - Plumbing inspection not yet called. Plumbing sub will call on 4/18 for 4/21 inspection. (Status: OK)
> 
> **Decisions/escalations:**
> - Owner approval needed on kitchen cabinet final finish by 4/16 (cabinet install scheduled 5/10).

This daily log becomes the source data for the Friday lookahead. The superintendent can see exactly where the schedule was kept.

---

## 8. Templates and Tools

### 8.1 Weekly 3-Week Lookahead Template

Create in Excel or Google Sheets; distribute every Friday by 5:00 PM.

```
PROJECT: [Name]
WEEK ENDING: [Date]
3-Week Window: [Week 1] to [Week 3]

LOOKAHEAD SUMMARY:
[Brief narrative of key activities and constraints for the 3 weeks]

ACTIVITY DETAIL TABLE:
| Activity | Start | End | Duration | Trade | Scope | Preconditions | Status | Constraint | Owner Action |
|---|---|---|---|---|---|---|---|---|---|
| [Activity name] | [Date] | [Date] | [Days] | [Sub] | [Description] | [What must be done first?] | Ready / Constrained / At-Risk | [If constrained, what?] | [Who is responsible for clearing?] |

CONSTRAINT LOG:
[See Section 8.2]

OWNER DECISIONS REQUIRED THIS WEEK:
- [Decision item 1] — Deadline [Date]
- [Decision item 2] — Deadline [Date]

UPCOMING MILESTONE DATES:
- [Milestone] — [Date] — Status: On track / At risk / Delayed
```

### 8.2 Constraint Log Template

Maintain as a separate rolling spreadsheet:

```
CONSTRAINT LOG — [Project]

| Constraint ID | Activity | Constraint Description | Owner | Target Removal | Status | Resolution | Root Cause |
|---|---|---|---|---|---|---|---|
| C-001 | Rough electrical | Electrician not quoted | GC | 4/14 | Closed | Quote received 4/6 | Procurement delay |
| C-002 | Pool deck soil test | Fill material delivery not confirmed | GC | 4/9 | Open | Confirmed delivery 4/10; test rescheduled to 4/13 | Supplier delay |
| C-003 | Cabinet install | Owner approval of finish | Owner | 4/16 | Open | Pending owner decision | Design decision |
```

### 8.3 Recovery Options Analysis Template

Use when a slip is threatening schedule:

```
RECOVERY ANALYSIS — [Project]
DATE: [Date]
ACTIVITY AT RISK: [Activity name]
CURRENT SLIPPAGE: [X] days behind schedule
CRITICAL PATH IMPACT: Yes / No — [Description if yes]

OPTION A: [Acceleration / Phasing / Resources]
- Description: [What specifically?]
- Cost: $[Amount]
- Schedule recovery: [Days]
- Risk: [Low / Medium / High] — [Why?]
- Preconditions: [What must be true for this to work?]
- Recommendation: [Yes / No / Conditional]

OPTION B: [Alternative]
[Same format]

OPTION C: [Alternative]
[Same format]

OWNER DECISION REQUIRED: Which option, or combination?
Cost impact: [Change order amount if applicable]
Schedule impact: [New completion date if applicable]
```

---

**Cross-reference:** Module 03 (Industrial Construction PM, Scheduling, and Safety) for CPM theory and critical-path concepts; Module 07 (Residential GC: Scope, Trades, and People Management) for field coordination context; Module 29 (Dispute Resolution, Claims, and Delay Management) for documenting delay claims; Module 32 (Change Order Management) for pricing schedule extensions and acceleration costs.

**Key resources:**
- Lean Construction Institute — Last Planner System training: leanconstruction.org
- Project Management Institute (PMI) — Schedule management: pmi.org
- Association for Construction Industry Research and Learning (ACIRL) — Production control methods
