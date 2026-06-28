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

## 3. Last Planner System Principles and Constraint Identification (EXPANDED)

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

### 3.4 Advanced Constraint Management — Distinguishing Between Activity Constraints and Process Constraints

Not all constraints are created equal. A residential superintendent must learn to distinguish between:

**Activity constraints** are preconditions to a specific activity:
- Material delivery (cabinet delivery for cabinet installation)
- Inspection clearance (framing rough inspection required before drywall)
- Trade availability (electrician booked and committed for week 6)
- Owner decision (kitchen finish selection required before cabinet shop drawings)

**Process constraints** are systemic barriers that affect multiple activities or schedule efficiency:
- Inspection bottleneck (building department can only schedule 2 inspections per week; you have 4 needed)
- Permit delays (mechanical permit not issued; holding up rough mechanical start)
- Weather impact (rainy month pushes outdoor work contingency weeks; shifts all downstream work)
- Resource allocation (GC superintendent is oversubscribed across 3 projects; cannot provide adequate daily coordination)

**Activity constraints are removed through specific action:** Call the supplier, accelerate the approval, confirm the electrician, get the owner decision.

**Process constraints require systemic solutions:** Early permit applications, pre-planning with the AHJ to understand inspection cadence, contingency planning for weather, GC staffing decisions.

A superintendent who addresses only activity constraints will find new constraints constantly surfacing. A superintendent who identifies and removes process constraints stays ahead of the schedule.

**Example:** 
- Activity constraint: "Framing rough inspection not yet called; framing crew on site but waiting."
- Root cause analysis: "The superintendent called the AHJ on Tuesday; no availability until Friday."
- Surface response (activity-level fix): "Call AHJ earlier (Monday) to get Thursday slot."
- Process-level response (systemic fix): "Coordinate with AHJ at project kickoff to understand inspection schedule. Request early time slots (7:00 AM if available). Build a 2-week contingency into framing schedule in case of inspection delays."

### 3.5 Constraint Removal Strategies — Beyond Rescheduling

When a constraint cannot be removed by the scheduled date, the superintendent has four primary strategies:

**Strategy 1 — Acceleration of the Constraining Item**

Example: Cabinet delivery scheduled for 4/22, but cabinet approval is delayed. Strategies to accelerate cabinet delivery:
- Expedite the owner approval process (call owner directly; request decision within 48 hours instead of 10 days).
- Request cabinet shop to expedite fabrication (+$500–$1,500 in expedite fee; possible if you can prove design is finalized).
- Identify an alternate cabinet source with faster delivery (risky; different design/quality).
- Phase cabinet installation (install kitchen first week of availability; install bathrooms second week from alternate source).

**Strategy 2 — Rescheduling the Dependent Activity (Float-Burning)**

If a constraint cannot be removed, and the dependent activity is not on the critical path, reschedule the activity and consume available float:
- Cabinet delivery: 4/22 → 5/6 (2-week delay).
- Cabinet installation: 5/10–5/18 → 5/20–5/28 (8-day slide).
- If flooring was scheduled 5/28–6/4, and float allows, reschedule flooring to 6/11–6/18 (no schedule impact to final completion).

**Strategy 3 — Parallel Path Development (Value Engineering)**

If rescheduling is not possible (no float available), create a parallel path of work:
- Cabinet installation blocked by delayed cabinet delivery.
- Meanwhile, other finish work (painting, electrical fixture install, plumbing fixture install) can proceed in non-cabinet areas.
- Cabinet installation happens as soon as cabinets arrive; final punch list items occur afterward.
- This maintains schedule momentum while the constraining item is being resolved.

**Strategy 4 — Escalation and Owner Acceptance of Schedule Change**

If none of the above are feasible, accept the schedule impact and formally notify the owner:
- Cabinet delay pushes final completion from 7/15 to 7/29 (14 days late).
- Issue a written notice to owner: "Due to cabinet delay beyond our control (supplier backlog), final completion will be delayed to [date]. We are implementing recovery options [A, B, C]. If approved, we can mitigate to [recovery date]."
- Negotiate cost implications (owner penalty, extended general conditions).
- Document the notice and owner's response (acceptance or counter-proposal).

This prevents disputes: the owner was informed of the risk and had the opportunity to request acceleration; the delay is documented and defensible.

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

## 6. Documentation and Schedule Change Orders (EXPANDED)

### 6.1 Schedule Impact as a Change Order Element

When a constraint or issue extends the project completion date, the cost impact is real — extended general conditions. This must be documented.

**Example scenario:**
- Original schedule: 120 days, completion 7/15/2025.
- Electrical permit delayed (AHJ); framing inspection delayed 10 days.
- New completion date: 7/25/2025 (10-day extension).
- General conditions cost (GC superintendent + PM + site overhead + equipment): $2,000/week.
- Cost impact: $2,000 × 1.4 weeks = $2,800 in extended GC.

This $2,800 is a legitimate cost to recover via change order — documented and submitted when the delay is confirmed.

### 6.1.1 General Conditions Cost and Schedule Extension Calculation

When a project extends beyond the planned completion date, the GC incurs **extended general conditions** — the cost of keeping the superintendent, management, insurance, and site overhead active for the extra time.

**Typical extended general conditions costs (residential project):**

| Item | Typical Monthly Cost |
|---|---|
| GC superintendent salary (salary + overhead allocation) | $4,000–$8,000 |
| GC project manager (portion of time on project) | $1,500–$3,000 |
| Site equipment (temporary utilities, fence, office trailer) | $500–$1,500 |
| Insurance (GL, builders risk, umbrella — prorated) | $500–$1,500 |
| Site cleanup and maintenance | $300–$800 |
| **Total monthly extended general conditions** | **$6,800–$14,800** |

**Example calculation:**
- Original contract: $500,000, 120-day schedule, GC general conditions budget: $45,000 (9% of contract).
- Per-day general conditions cost: $45,000 ÷ 120 = $375/day.
- Schedule extends 14 days (due to owner-caused delays).
- Extended general conditions cost: 14 days × $375/day = $5,250.
- Change order issued to owner for $5,250 (schedule extension).

**Critical documentation:** The GC must document the root cause of the delay (owner decision, permit delay, sub non-performance, force majeure) to support the change order request. Without documentation, the owner may dispute the cost.

### 6.2 "Delay Impact" vs. "Defective Condition" Disputes

When a trade delays and you must accelerate to compensate, clarify the cost category:
- **Delay caused by sub defect/non-performance:** Sub pays for acceleration (backcharge).
- **Delay caused by owner condition/decision:** Owner pays via change order.
- **Delay caused by force majeure or both parties:** Negotiate shared cost.

Document the cause: "Framing delay due to owner-directed structural changes = owner pays $3,000 acceleration cost" vs. "Framing delay due to crew availability (sub issue) = sub absorbs acceleration cost."

### 6.3 Change Order Language for Schedule-Related Impacts

**Sample contract language for schedule-related change orders:**

> **Owner Responsibility for Schedule Delays.** In the event that Owner causes a delay in the Work (including, but not limited to: delays in providing approvals, submittals, or material selections; owner-directed changes in scope or sequencing; delays caused by owner-directed permits or inspections), Contractor shall be entitled to a schedule extension and a change order for the cost of extended general conditions.
>
> **Extended General Conditions Cost.** If the Project is delayed due to Owner-caused conditions, Contractor shall be entitled to additional compensation for extended general conditions, calculated as the per-day cost of general conditions ($[amount] per day) multiplied by the number of days of delay. General conditions include, but are not limited to: superintendent and management salary, site overhead, insurance, and temporary utilities.
>
> **Cost of Acceleration.** If Contractor elects to accelerate the Work to mitigate a delay, and such acceleration is required due to Owner-caused delay, Contractor shall be entitled to reimbursement of acceleration costs (including labor premium, equipment rental, and overtime), documented with supporting invoices.

This language ensures that if an owner delay extends the schedule, the GC is compensated for the extended general conditions cost, rather than absorbing it.

---

## 7. Field Reporting Integration (EXPANDED)

### 7.0 Why Daily Reporting Matters for Schedule Management

The lookahead schedule is only as accurate as the information feeding it. If the superintendent is updating the Friday lookahead based on memory or rough notes, errors and misalignments accumulate. A **systematic daily log** is the source of truth that prevents this drift.

**Three critical functions of daily reporting:**

1. **Schedule tracking:** Compares actual progress to planned progress. "Framing scheduled to be 60% complete; actually 55% complete — 5 days behind plan."

2. **Constraint identification:** Captures new barriers that emerged during the day. "Electrical rough box placement has conflict with HVAC duct location; must resolve before electrical installation."

3. **Decision documentation:** Records owner decisions, approval dates, and changes. "Owner approved kitchen cabinet finish at site meeting on 4/15. Cabinet shop drawings can now be submitted."

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

### 7.2 Digital vs. Paper Logs — Best Practices

**Paper logs (traditional):**
- Advantages: No tech required; can be handwritten quickly on site.
- Disadvantages: Hard to search, version control is manual, prone to loss.

**Digital logs (phone/tablet app or cloud-based):**
- Advantages: Searchable, automatically uploaded, shared with team, can include photos.
- Disadvantages: Requires connectivity on site (may not exist in all locations).

**Best practice — hybrid approach:**
- GC superintendent writes a brief daily log on paper (15–20 minutes at end of day).
- Superintendent (or office staff) transcribes or uploads to a digital platform (Google Sheet, Procore daily log, or Excel) same evening or next morning.
- Digital version is shared with owner, subs, and PM.
- Cloud-based platform allows team to see daily progress in real-time and flag issues immediately (don't wait for Friday lookahead).

### 7.3 Frequency and Timing of Daily Logs

**Minimum frequency:** One comprehensive log per day, written by the GC superintendent.

**Timing:** End of business day (4:00–5:00 PM), while the day is fresh in memory.

**Content review:** The PM or project owner reviews the daily log same evening (if digital) or first thing next morning (if paper). Any issues or questions are flagged same-day or early next day, not waiting for the Friday lookahead.

**Weekly synthesis:** The Friday lookahead is synthesized from 5 days of daily logs, plus Friday's constraint-clearance meeting. The lookahead is not created in a vacuum; it's built on the daily reporting data.

### 7.4 Critical Daily Log Elements — What to Never Miss

**Weather and external conditions:**
- Record date, time, and weather conditions (clear, rain, extreme heat).
- Note any weather-related work stoppages: "Rain from 2:00–4:00 PM; framing crew moved inside to interior framing; exterior work lost 2 hours."

**Crew on site by trade:**
- "Framing: 6 carpenters + foreman" (names optional but helpful; at minimum, count and hours).
- "Electrical: 2 electricians, 4-hour shift" (if partial day, note the reason: "Inspections ran late; electrician crew called off at noon").

**Progress by activity:**
- "Framing: Master and guest room wall framing 95% complete; soffit framing 40% complete (started today; soffit lumber arrived on time day 35)."
- Track percentage complete, not just "work occurred."

**Changes from planned schedule:**
- "Rough plumbing: Scheduled for day 20–22, but not yet started due to framing delay. Rescheduled to day 24–26."
- Document when activities shift and why.

**Deliveries and inspections:**
- "Soffit lumber: Received day 35 per schedule. Condition: good; all bundles counted."
- "Framing rough inspection: Not yet called. Inspector availability constrained to 2 slots per week. Estimated inspection day 50."

**Decisions and approvals:**
- "Owner meeting: Kitchen finish selections finalized (owner approved at site visit). Cabinet shop drawings can now be submitted."
- "Permit status: Electrical upgrade permit still pending AHJ review. Follow-up call scheduled 4/18."

**Issues and constraints:**
- "Issue: HVAC duct location conflicts with framing soffit. Meeting scheduled 4/16 with MEP sub and framing foreman to resolve routing."
- "Constraint: Cabinet delivery still on target for 4/22. Approval of final finishes required by 4/12 to meet this date."

**Safety notes (if safety program is active):**
- "Toolbox talk: Fall protection (all framing crew present, 10 minutes)."
- "Incident: Minor cut on framing crew member; first aid applied on site; worker continued work."

**Time tracking (useful for future projects):**
- "Framing: 6 carpenters × 8 hours = 48 carpenter-hours; 95% of scope complete = 48 hours for remaining 5% scope = total estimated 50 carpenter-hours."
- This data becomes the basis for estimating labor on future projects.

---

### 7.5 Using Daily Logs for Schedule Recovery and Problem Prevention

**Real-time detection of slippage:**
A superintendent who reads the daily logs early in the week can identify schedule drift before it becomes a crisis. Example:
- Day 20 (Monday): Daily log shows framing at 65% instead of planned 70%. Difference: 5 percentage points = about 1 day of slippage.
- Day 24 (Friday): Projected framing completion is now day 55 instead of planned day 50. Slippage is 5 days, growing.
- By detecting this early (day 20), the superintendent has a week to analyze the root cause and develop a recovery plan (before the problem is irreversible).

**Constraint escalation:**
If the daily log on day 15 says "Cabinet approval still pending; owner decision needed by day 18 to meet cabinet delivery date day 35," the PM can call the owner on day 16 and escalate the approval. Waiting until day 20 to escalate means it's too late.

**Documentation for disputes:**
If an owner later claims that the GC delayed the project, the daily logs provide a factual record of progress, decisions, and constraints. "Here's what happened: Week 3, owner changed the scope; documented in daily log day 17. Week 4, cabinet approvals delayed; documented day 22–24. Week 8, electrical rough inspection delayed due to AHJ availability; documented day 43. These external factors, not GC performance, caused the 2-week schedule slip."

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

---

## Case Study 1: Framing Delay and Recovery — Residential 6-Month New Build

**Project context:**
- 3,200 sq ft residential new build, $780,000 contract.
- Scheduled completion: October 31, 2024.
- Critical path: Foundation (month 1) → Framing (month 2–3) → MEP rough-in (month 3–4) → Closeout (month 5–6).
- Owner penalty for late completion: $500/day after October 31.

**The problem:**
Week 8 of 16: Framing is scheduled to complete on day 50. Daily logs show framing at 65% complete on day 45, and the framing crew is now reporting they will not finish until day 55 — 5 days late.

Root cause: Soffit lumber was delayed (delivered day 36 instead of day 26), and soffit installation is on the critical path before rough inspection. Additionally, an owner-directed change (addition of a vaulted ceiling in the great room) added 3 days of unplanned framing labor.

**What the superintendent knew (from the lookahead and constraint log):**
- Day 35: Soffit lumber constraint identified; target removal date day 33 — marked "at-risk." Lumber supplier confirmed delivery day 36.
- Day 40: Vaulted ceiling change requested by owner. Change order prepared. Scope added 60 carpenter-hours (approximately 3 extra days). GC requested written owner confirmation before proceeding; received day 42.
- Day 43: Framing crew meets with GC superintendent. Crew confirms: "We can recover the soffit delay (1 day) by removing non-critical blocking and speeding soffit installation. But the vaulted ceiling change is adding 3 days, uncompensated."

**Recovery decision (day 43):**
The superintendent analyzes options:
1. **Acceleration option A:** Add 2 carpenters for 5 days at overtime rate.
   - Cost: 10 hours × 2 people × $65/hr (premium over standard rate) = $1,300
   - Recovery: 3 days
   - Net impact: Completes day 52, instead of day 55. Still 2 days late.

2. **Acceleration option B:** Extend framing crew to 10-hour days (one crew, no additions).
   - Cost: 5 days × 10 hours × 2 people × $15/hr (overtime premium) = $1,500
   - Recovery: Approximately 2 days
   - Net impact: Completes day 53, still 3 days late.

3. **Phasing option:** Start rough electrical on day 48 while framing soffit continues (days 48–52).
   - Cost: Coordination overhead ~$300; minimal direct cost
   - Risk: Electrician and framing in same space; potential rework if framing changes
   - Potential recovery: 3–4 days, if coordination can be managed without safety issues.

4. **Resource addition:** Deploy two additional crews from allied trades on day 46.
   - Cost: High; crews may not be available on short notice
   - Recovery: Uncertain; adding labor mid-project creates coordination chaos

**The superintendent's decision:**
Implement option 3 (phasing) combined with modest acceleration (9-hour days instead of 8):
- Electrical to start day 48 (4 days early), contingent on electrician's availability and GC's ability to manage coordination.
- Framing to shift to 9-hour days (not full 10-hour overtime, but incremental acceleration).
- Cost: Coordination overhead ~$300 + accelerated labor premium ~$800 = ~$1,100.
- Recovery potential: 4 days total, if electrical/framing coordination can be managed.

**Owner communication (day 43):**
Written communication to owner:
> "Framing is currently tracking 5 days behind schedule due to (1) soffit lumber delay (1 day), and (2) your vaulted ceiling change (3 days). We are implementing a recovery plan: (a) starting rough electrical early (day 48) to parallelize work; (b) extending framing hours to 9 per day. Estimated recovery: 4 days. Revised framing completion: day 51, which puts final close-out substantially on track for October 31 (4-day buffer remains). Cost impact: $1,100 (coordination and incremental labor). Recommend written approval before we proceed with accelerated schedule."

Owner approves same-day.

**Execution (days 44–52):**
- Electrical crew confirms availability for day 48 start.
- GC superintendent coordinates daily at 7:00 AM stand-up: electrician and framing crews review work areas to avoid conflicts.
- Day 48–52: Electrician rough-in proceeding simultaneously with framing soffit. Minor rework required on day 49 (electrician had to move one box location due to framing interference — 1 hour delay).
- Day 51: Framing inspection called and passed.
- Day 52: Electrical continues while remaining loose ends are cleanup-only.

**Actual outcome:**
- Framing completion: Day 51 (4-day recovery achieved; 1 day earlier than recovery plan).
- Final project completion: November 2 (2 days late; owner charged $1,000 penalty for two days).
- But: Without the recovery plan, final completion would have been November 5 (5 days late; $2,500 penalty).
- Recovery plan saved owner $1,500 in penalties; cost the GC $1,100 in acceleration — **net value to GC: $400 in reduced penalty payment, plus relationship preservation with owner.**

**Key lessons:**
1. **Constraint identification early is critical.** The soffit delay was flagged 14 days in advance. This gave the superintendent time to develop recovery options.
2. **Owner changes must be quantified immediately.** The vaulted ceiling change was scope addition; the GC priced it and included the schedule impact in the recovery plan.
3. **Phasing and coordination can be as effective as adding labor.** Option 3 (electrical start early) saved more cost than pure acceleration.
4. **Written communication protects relationships.** Owner approved the plan; there were no surprises. When the 2-day penalty was assessed, the owner understood it was their change, not GC failure.

---

## Case Study 2: Constraint Identification Failure — Residential 4-Month Remodel

**Project context:**
- $320,000 kitchen and second-floor renovation, 16-week schedule.
- Kitchen remodel path: Demolition (week 1–2) → Framing/MEP rough (week 3–4) → Rough inspections (week 5) → Drywall/MEP finishing (week 6–7) → Cabinets/counters (week 8–9) → Finishes (week 10–12) → Closeout (week 13–16).
- Critical path item: Cabinet fabrication and installation (8-week lead time from shop drawing approval to delivery).

**The problem:**
Week 3 (mid-project): Cabinets are scheduled to arrive week 9. The superintendent has not yet sent cabinet shop drawings to the owner for approval. The owner is on vacation until week 4, and the design selections (colors, finishes) have not been finalized.

The cabinet lead time is 8 weeks from approved shop drawings. Today is day 15 of the project. The deadline to approve shop drawings to meet the week 9 delivery is day 35 (7 weeks out). If approvals are delayed by 3 weeks (plausible, given owner vacation and selection decisions), cabinet delivery slips to week 12 — exactly when cabinets should be installed. This creates a 3-week delay in cabinet install, which delays all finish work, pushing closeout past the owner's deadline.

**What the superintendent did NOT do (constraint management failure):**
- No lookahead was created identifying cabinet approval as a constraint.
- No constraint-clearance meeting occurred at the start of the project to flag that selections needed to be finalized before shop drawings could be prepared.
- No written notice was sent to the owner identifying the cabinet lead time risk.

**The superintendent's response when the problem surfaced (week 5):**
By the time the delay became obvious (week 5), it was too late to implement recovery. The superintendent then:
1. Pushed the cabinet shop for a 6-week lead time instead of 8 weeks (not achievable, per the shop).
2. Accelerated drywall work to buy time (doesn't help if cabinets aren't installed yet).
3. Contacted the owner requesting expedited selections (owner was busy; selections took 2 additional weeks).

**Actual outcome:**
- Cabinet drawings submitted day 50 (instead of optimal day 35).
- Approvals received day 60 (instead of day 35).
- Cabinet delivery: week 13 (instead of week 9).
- Cabinet install could not start until week 13; finish work cascaded late.
- Final completion: 4 weeks behind schedule.
- Owner penalty: $8,000 (4 weeks × $2,000/week late fee).
- GC absorbed the penalty; no change order was submitted (relationship damage).

**Comparison to Case Study 1:**
In Case Study 1, the soffit delay was identified 14 days in advance, and recovery was orchestrated in time. In Case Study 2, the cabinet constraint was never identified, and recovery became impossible.

**Lessons:**
1. **Constraint identification must happen before construction starts or within the first week.** A constraint-clearance meeting during pre-construction would have identified cabinet approvals as the first-priority owner decision.
2. **Owner decisions are constraints.** Cabinet selection approvals are owner decisions, and the superintendent must drive them early — not wait for the owner to volunteer.
3. **The first Monday lookahead is your control point.** If the first 3-week lookahead identifies 8 critical owner decisions needed before week 5, you have the leverage to get them made.
4. **Long-lead items require backwards planning.** Cabinet delivery week 9 requires approvals week 1–2 to create a 7-week lead-time buffer. The GC must communicate this to the owner before contract signature.

---

## Case Study 3: Effective Recovery Through Resource Addition and Parallel Phasing — Commercial Tenant Fit-Out

**Project context:**
- $1.2M commercial tenant fit-out, 14-week critical path.
- Owner needs occupancy by 4/30/2024 (hard deadline; lease starts 5/1).
- Critical path: Structural (weeks 1–3) → MEP rough (weeks 4–6) → Drywall (weeks 7–8) → Finishes (weeks 9–11) → Closeout (weeks 12–14).
- Structural contractor is a critical single-source dependency.

**The problem:**
Week 4: Structural contractor reports that steel delivery is delayed one week (week 4 instead of week 3). This pushes structural completion to week 4 instead of week 3, which cascades to push MEP start from week 4 to week 5. MEP rough is a 3-week activity; MEP completion would slip from week 6 to week 7. Drywall cannot start until MEP is complete, so drywall shifts from week 7–8 to week 8–9. Finishes (weeks 9–11) shift to weeks 10–12. Closeout (weeks 12–14) shifts to weeks 13–15. **Final completion: May 7 — 7 days late. Owner occupancy delayed; lease penalties.**

**Recovery analysis (week 4):**
The GC superintendent and PM analyze options:

**Option 1: Acceleration via labor increase on structural.**
Not applicable — structural is material-constrained, not labor-constrained.

**Option 2: MEP parallelization.**
Review structural design: Are there areas where MEP can be rough-in before structural is 100% complete?
- Structural includes steel frame installation (weeks 1–3) and then concrete pour and cure (week 4).
- MEP rough can start on week 4, after steel is installed but while concrete is curing.
- If MEP starts day 1 of week 4 instead of day 1 of week 5, MEP gains 5 days.
- Risk: MEP crews must coordinate around concrete pour and cure activities; potential rework if layout changed.

**Option 3: Drywall parallelization.**
- Drywall typically cannot start until MEP rough is complete (code requirement: MEP must be inspected before concealment).
- However, drywall can start on one section (e.g., office perimeter) while MEP rough completes on other areas (e.g., core MEP).
- If drywall starts on day 1 of week 8 (one week early) on sections with MEP already inspected, drywall gains 5 days.
- Risk: Crew coordination; potential MEP rework if drywall obstructs later rough-in.

**Option 4: Add second drywall crew.**
- Drywall is 2 weeks of work; adding a second crew can compress to 1.5 weeks (assuming coordination can be managed).
- Cost: ~$8,000 (second crew labor premium for partial week).
- Recovery: 3–4 days.

**Option 5: Accept 1-week delay; negotiate with owner.**
- Owner penalty: 1 week = $15,000+ (lease penalty, additional GC overhead, potential sublet losses).
- Cost to recover 1 week via options 2+3+4: ~$12,000 (coordination overhead ~$2,000, MEP acceleration ~$3,000, drywall crew addition ~$7,000).
- Value: Saves ~$3,000 in owner penalties, plus preserves owner relationship.

**Decision:**
Implement combined strategy: MEP parallelization (gain 5 days) + drywall parallelization (gain 5 days) + drywall crew addition (gain 3 days) = 13 days recovery, which exceeds the 7-day target delay.
Cost: ~$12,000
Expected outcome: Final completion May 2–3 (1–2 days late; acceptable to owner vs. 7 days late).

**Execution (weeks 4–11):**
- Week 4: MEP starts as scheduled (steel is in; concrete cure proceeds). Coordination meetings daily (7:00 AM) between structural and MEP leads.
- Week 5: MEP continues; structural concrete completes. MEP rough inspection requested for day 35 (week 5 end).
- Week 8: Drywall starts on office perimeter zones (MEP already inspected) while MEP rough completes on core zones.
- Week 8: Second drywall crew mobilizes mid-week; two crews now running (different zones).
- Week 9: MEP rough inspection passes; remaining MEP rough-in by second sub crew continues parallel to drywall.
- Week 10: Drywall 85% complete (ahead of original week 8 target due to parallelization and second crew).
- Weeks 11–12: Finishes (painting, flooring, fixture install) proceed.
- Week 12 (original week 14 schedule): Closeout activities begin.
- Final completion: May 2 (target met, 1 day early buffer remaining).

**Actual outcome:**
- Project completed May 1 (exactly on deadline for May 1 occupancy).
- Owner occupancy commenced as planned; no lease penalties.
- Cost of recovery: $12,000.
- Value delivered: Prevented owner penalties (~$15,000+), preserved owner relationship (repeat business likely), and achieved on-time delivery.
- **Net business value: ~$3,000–$5,000 in cost avoidance plus relationship/reputation value.**

**Lessons:**
1. **Parallelization is often more effective than pure acceleration.** By starting MEP early (parallel to concrete cure) and drywall early (parallel to MEP rough-in on other zones), the GC recovered 10 days at moderate cost.
2. **Second crew addition is most effective on discrete, easily parallelizable work** (like drywall). Bringing in a second framing crew mid-project is chaos; a second drywall crew can work independent zones.
3. **Daily coordination meetings are essential when parallelizing risk.** The daily 7:00 AM stand-up between structural, MEP, and GC ensured that activities stayed aligned and rework was minimized.
4. **Present the recovery plan to the owner proactively.** The GC met with the owner in week 4, explained the delay risk, presented the recovery plan, and requested owner authorization. The owner appreciated the transparency and approved the plan. This prevented surprise delays later.

---

## Case Study 4: Scheduling Discipline in Extreme Conditions — Residential New Build During Supply Chain Crisis

**Project context:**
- $650,000 residential new build, originally planned for 6-month duration (April–September 2021).
- Project affected by extreme 2021 supply chain disruptions (lumber surge, appliance unavailability, electrical equipment delays).
- Superintendent with exceptional lookahead discipline manages the schedule with systematic constraint management.

**The challenge:**
Standard residential scheduling assumes 2–4 week material lead times. In 2021, material lead times were 12–16 weeks for:
- Lumber (price surge; mills backlogged)
- Appliances (HVAC, water heater, range — 14-week waits)
- Electrical equipment (breaker panels, switches — 10-week waits)
- Structural engineer review (civil/structural design stamping — 6-week review backlogs)

**The superintendent's response:**
Rather than accept a 12-month schedule, the superintendent implemented an aggressive 14-week lookahead and constraint management discipline:

**Week 0 (pre-construction, 16 weeks before framing):**
- Constraint-clearance meeting with owner and all major subs identifies 18 critical long-lead items.
- Superintendent creates a "reverse schedule" working backwards from final completion: What is the latest date to procure/approve each item?
- Material delivery dates set as "due by" dates; items are ordered 16–18 weeks early.
- Owner required to approve selections and finalize design 18 weeks prior to installation need.

**Weekly discipline (weeks 1–20):**
- Every Friday: Updated 3-week lookahead issued identifying constraint status.
- Specific example from week 2 lookahead:
  - "HVAC unit delivery due 4/15 (week 6) — current status: order placed 2/1, delivery confirmed. Constraint: NONE."
  - "Appliance final selections due 3/10 (week 2) — current status: waiting for owner kitchen meeting. Constraint: Owner kitchen meeting must occur by 3/5. Assigned to PM. Escalation if not complete by 3/5."
  - "Electrical panel installation planned week 8 — panel delivery due week 6. Current status: order submitted 1/15 for 14-week delivery (due 4/15); confirmed with supplier. Constraint: NONE."

**Results:**
- Despite supply chain chaos that caused 2–4 month delays on other residential projects in the area, this project maintained a 6-month schedule.
- Key: Front-loaded all long-lead material orders and owner decisions to weeks 0–4, before construction began.
- Frame completion: Week 12 (per schedule).
- Final completion: September 15 (scheduled September 30; 2-week early buffer).
- Owner delivered on-time.
- GC reputation in market: "The only builder who delivered on schedule in 2021."

**Lessons:**
1. **In constrained supply environments, the lookahead horizon extends beyond 3 weeks.** A 6-week or 12-week lookahead is appropriate for projects with long-lead materials.
2. **Reverse scheduling is a powerful tool.** Working backwards from final completion date to identify "must-have-by" dates for each constraint (material, approval, inspection) ensures nothing is missed.
3. **Constraint management is most effective when it includes owner decisions early.** The superintendent forced owner selection decisions into weeks 0–4, preventing the cascade of delays that affected other builders.
4. **Weekly discipline compounds over time.** Updating the lookahead every Friday, maintaining a constraint log, and escalating overdue items prevents the slow accumulation of delays.

---

**Cross-reference:** Module 03 (Industrial Construction PM, Scheduling, and Safety) for CPM theory and critical-path concepts; Module 07 (Residential GC: Scope, Trades, and People Management) for field coordination context; Module 29 (Dispute Resolution, Claims, and Delay Management) for documenting delay claims; Module 32 (Change Order Management) for pricing schedule extensions and acceleration costs.

**Key resources:**
- Lean Construction Institute — Last Planner System training: leanconstruction.org
- Project Management Institute (PMI) — Schedule management: pmi.org
- Association for Construction Industry Research and Learning (ACIRL) — Production control methods
