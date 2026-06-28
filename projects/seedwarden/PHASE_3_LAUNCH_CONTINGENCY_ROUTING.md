---
title: "Phase 3 Launch Contingency Routing — Response Scenarios, Timeline Paths, and Kill-Switch Criteria"
date: 2026-06-28
version: 1.0
status: production-ready
decision-window: June 28–July 5, 2026
finish-lines:
  best-case: July 13, 2026
  moderate-case: July 15–17, 2026
  worst-case: July 20+, 2026
  no-go: Mid-August 2026 (solo) or October restart (Q4 pause)
kill-switch-date: July 5, 2026
cross-references:
  - CONTRACTOR_ONBOARDING_AUTOMATION_LOGIC.md (ACCEPT/CONDITIONAL/ESCALATE routing)
  - WEEK_1_ONBOARDING_CHECKLIST.md (Day 1–7 execution)
  - PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md (9-week solo timeline and cascade logic)
  - PHASE_3_CONTRACTOR_DECISION_TREE.md (original go/no-go framework)
  - PHASE_3_CRITICAL_PATH_ANALYSIS_JUNE22_JULY13.md (bundle writing schedule, upload dates)
tags: [seedwarden, phase-3, launch, contingency, routing, timeline, kill-switch]
---

# Phase 3 Launch Contingency Routing

**Prepared**: June 28, 2026
**Purpose**: Explicit routing logic for each Phase 3 launch scenario based on contractor response patterns arriving today. Maps from contractor response count to timeline path to finish line. Every scenario includes specific actions, updated milestone dates, and the revenue impact of each outcome. The kill-switch criteria are pre-authorized — they activate automatically when trigger conditions are met.

---

## Decision Context: The Slip Has Already Happened

Phase 3 was planned to launch June 22. It did not. The June 22 launch date has slipped. As of June 28, the operative question is not "will we hit June 22" — it is "which of the four paths below do we execute, and what is the new finish line."

This document does not re-litigate the June 22 slip. It routes forward from the current date with the contractor response data arriving today.

---

## Scenario 1 — Best-Case: 3–5 Contractors ACCEPT by June 28 EOD

### Trigger Condition
Three or more contractors (minimum: 1 photographer + 1 writer) return unambiguous ACCEPT responses on June 28 before 23:59 UTC.

### Immediate Actions (June 28–29)

1. Route all ACCEPT responses through `CONTRACTOR_ONBOARDING_AUTOMATION_LOGIC.md` Section 2 immediately — do not batch responses for a morning review. Process each ACCEPT as it arrives.
2. Send contracts same-day for all ACCEPT responses. Target signatures: June 29 by 12:00 UTC.
3. Deliver onboarding kits June 29 (Day 1 per `WEEK_1_ONBOARDING_CHECKLIST.md`).
4. Schedule all Day 2 check-in calls for June 30.
5. Set the Monday full-team sync for June 30 or July 1 (Day 2–3 of engagement).

### Revised Sprint Timeline

| Event | Date | Notes |
|---|---|---|
| Contracts signed | June 29 | All ACCEPT contractors; deposits paid by July 1 |
| Onboarding kits delivered | June 29 | Per `WEEK_1_ONBOARDING_CHECKLIST.md` Day 1 |
| Day 2 check-in calls | June 30 | 15 min per contractor |
| First Day 5 samples due | July 3 | Writer outlines + photographer session start |
| Respiratory first draft due (writer) | July 8 | Aligns with M2 payment date |
| Session 1 photography approved | July 8 | Aligns with M2 payment date |
| Full team kick-off (Day 7) | July 5–6 | First Monday team sync |
| Immunity first draft due | July 15 | Aligns with M3 payment date |
| Digestive final draft + all revisions | July 27 | Aligns with M4 payment date |
| Phase 3 finish line | July 13 | All bundles live; Women's Health already live from earlier upload |

### Why July 13 is the Best-Case Finish Line

The original contractor sprint had a July 13 finish line (from the June 22 start). The June 28 start pushes this by 6 calendar days but does not push the finish line by the same amount because:
- Week 1 onboarding (June 29–July 5) overlaps with writer draft work starting July 1
- The Respiratory bundle upload was planned for July 6 in the original sprint — it is now July 13 in the best-case
- The Digestive bundle (last) was planned for August 3 in the original sprint — it is now late July (M4 handoff July 27 → Digestive upload August 3 unchanged)

The July 13 finish line applies to the last upload before the August 3 Digestive — meaning Women's Health, Respiratory, Immunity, and Sleep are all live by July 13. Digestive remains August 3.

### Revenue Impact (Best-Case)

Relative to the original June 22 plan: approximately 3 weeks of delayed live catalog. At estimated 3–8 organic Etsy views/day per listing with 3–5% conversion at $20–$22, a 3-week slip on the full catalog represents approximately $60–$180 in delayed first-3-weeks revenue. This is not a project-level financial impact — it is a delay, not a loss.

The July 13 catalog (4 bundles live) activates the practitioner tier ($120–$150 clinical library) if AHG reviewer is confirmed. That tier is not time-sensitive to the June 22 slip.

---

## Scenario 2 — Moderate-Case: 2–3 ACCEPT + 2–3 CONDITIONAL by June 28 EOD

### Trigger Condition
Two or three contractors send ACCEPT responses, and two or three contractors send CONDITIONAL responses that are not immediately resolvable.

### Immediate Actions (June 28–29)

1. Route ACCEPT responses immediately (same as Scenario 1).
2. Route CONDITIONAL responses through `CONTRACTOR_ONBOARDING_AUTOMATION_LOGIC.md` Section 3 — classify each condition and begin resolution same day.
3. Schedule clarification calls for all CONDITIONAL contractors by June 29 18:00 UTC. Do not let clarification calls push past June 30.
4. Onboard ACCEPT contractors beginning June 29 (Day 1). Do not wait for CONDITIONAL contractors to resolve before onboarding the ACCEPT group.
5. Set hard deadline for CONDITIONAL resolution: June 30 EOD.

### CONDITIONAL Resolution Window

**June 29 (clarification calls)**: Resolve conditions via 15-minute calls. Most CONDITIONAL responses resolve in one call if the condition is rate, tool access, or scope clarification.

**June 30 EOD**: Final CONDITIONAL conversion deadline. Any CONDITIONAL contractor who has not confirmed by June 30 23:59 UTC is reclassified to ESCALATE and backup activation begins.

**Partial team dynamics**: Running Day 1 onboarding for ACCEPT contractors while clarification calls are in progress for CONDITIONAL contractors is intentional. The ACCEPT group does not wait for the CONDITIONAL group — they begin writing and shooting June 29 regardless. If a CONDITIONAL contractor converts to ACCEPT on June 30, their Day 1 is June 30 and their schedule compresses by 1 day — this is the cost of the CONDITIONAL delay, not a reason to delay the ACCEPT group.

### Revised Sprint Timeline (Moderate-Case)

| Event | ACCEPT contractors | CONDITIONAL (resolves June 30) |
|---|---|---|
| Day 1 onboarding | June 29 | June 30 |
| Day 2 check-in | June 30 | July 1 |
| Day 5 first sample | July 3 | July 4 |
| Respiratory first draft | July 8 | July 10 (2-day slip from 1-day start delay) |
| Immunity first draft | July 15 | July 17 |
| Digestive final | July 27 | July 28 |
| All bundles live finish line | July 13 (ACCEPT group) | July 15–17 (CONDITIONAL group) |

**Overall Moderate-Case Finish Line: July 15–17**

The 2-day slip per CONDITIONAL contractor is manageable and does not cascade to Digestive upload (August 3 buffer absorbs it). If only 1 photographer and 1 writer are in the CONDITIONAL group and both resolve June 30: the finish line is July 15. If 2 writers are CONDITIONAL and both resolve June 30: July 17.

### Timeline Slip Management (Moderate-Case)

If the July 15–17 finish line is still within Q2 calendar tolerance (it is — Q2 ends June 30, so this is early Q3, not a Q3 slide):
- Maintain all milestone dates as above
- Communicate the 2-day slip to the CONDITIONAL contractors explicitly on the clarification call: "Because of the 1-day delay in your start date, your Respiratory draft is due July 10 instead of July 8. Everything else adjusts by 2 days. That is the timeline I am committing to work with."
- Log the adjusted dates in `PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md`

If any CONDITIONAL contractor converts to ACCEPT after July 1 (not resolved by June 30 as required):
- Their schedule slips by 2 days per day of delay beyond June 30
- A July 2 start means Respiratory due July 12, Immunity due July 19, finish line July 17–19
- This is still within the July 20 worst-case finish line and does not trigger the kill-switch

### Revenue Impact (Moderate-Case)

Best-case finish line was July 13. Moderate-case finish line is July 15–17. The 2–4 day delta is negligible at the revenue scale of Phase 3 listings. No meaningful revenue impact relative to best-case. The more important variable is whether 3 bundles are live by July 15 for practitioner tier eligibility — they are, assuming Respiratory, Immunity, and Sleep all launch before July 15.

---

## Scenario 3 — Worst-Case: 1–2 ACCEPT Only (No Useful CONDITIONAL or ESCALATE Resolving)

### Trigger Condition
Only 1 or 2 contractors send ACCEPT responses by June 28 EOD, and all CONDITIONAL contractors fail to resolve by June 30 EOD.

The minimum viable contractor team is: 1 photographer + 1 writer. If 1 photographer accepts and 1 writer accepts: proceed with that team. All uncontracted bundles and tracks go to solo fallback.

### Immediate Actions

1. Onboard the accepting contractors beginning June 29 (Day 1) per `WEEK_1_ONBOARDING_CHECKLIST.md`.
2. Simultaneously activate Toptal intake (Step 1 from ESCALATE pathway in `CONTRACTOR_ONBOARDING_AUTOMATION_LOGIC.md` Section 4).
3. Post Upwork emergency listings for the uncovered tracks.
4. Activate solo fallback for the uncovered bundles starting June 29.
5. Set the July 3 EOD hard decision gate: if no additional contractor is confirmed by July 3, the solo fallback covers all uncontracted scope with no further escalation.

### Solo Fallback Integration

Per `PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md`, the solo fallback is fully operable from June 29. In the worst-case scenario, the hybrid model (1–2 contractors + solo fallback for the rest) means:

- Contractor(s) cover their specific track deliverables on the revised schedule
- User covers all uncontracted bundles at the 12 hrs/week solo pace
- The solo fallback and the contractor track run in parallel without conflict

**Example hybrid load** (1 photographer + 1 writer accepting):
- Photographer covers: Sessions 1–3 (all 3 bundles)
- Writer covers: Respiratory + Immunity (2 bundles)
- User writes: Digestive (solo fallback, starting July 3 per the solo fallback Week 6 schedule)
- Net outcome: Women's Health + Respiratory + Immunity live by July 20; Digestive live August 3–10

### Toptal + Upwork Gap Filling

If Toptal match arrives by July 3 (48–72 hour turnaround from June 29 intake):
- Score the Toptal candidate immediately (vetting rubric from `PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md`)
- If score 75+: engage immediately with compressed onboarding (3-day kit delivery, no Day 2 call — go directly to Day 5 sample within 72 hours)
- If score 60–74: engage with enhanced oversight protocol (user reviews every section before contractor proceeds to the next)
- If score below 60: decline; solo fallback covers the gap

A July 3 Toptal contractor start means:
- First draft Respiratory: July 13 (10 days vs. 8 days for a June 29 start)
- All bundles live finish line: July 20–24

### Revised Finish Line (Worst-Case)

**July 20+** — exact date depends on:
- Whether Toptal or Upwork fills the coverage gap and on what date
- How many bundles are in solo vs. contractor coverage
- Whether the Day 5 sample gate passes cleanly or requires a revision cycle

At July 20, all 5 bundles are live (assuming Digestive August 3 from the contractor timeline, not the solo September 24 from the pure solo fallback). The August 3 Digestive upload is preserved in the worst-case scenario because the worst-case still has at least 1 writer covering 2 bundles — Digestive is covered solo but starts writing July 6, not July 30.

### Revenue Impact (Worst-Case)

Relative to best-case (July 13): approximately 7-day slip in full catalog. At the same view/conversion estimate, this represents approximately $30–$90 in delayed revenue across the delay window. Not a project-level impact.

The more significant financial signal in the worst-case is whether the practitioner tier ($120–$150 clinical library) can still activate on schedule. The practitioner tier requires 3 bundles live — Respiratory, Immunity, and Women's Health. Under the worst-case scenario, Women's Health is already live (from the June 29 women's health upload) and Respiratory + Immunity are live by July 20. The practitioner tier activates July 20–22.

---

## Scenario 4 — No-Go: Zero ACCEPT Responses

### Trigger Condition
No contractor responds with an ACCEPT by June 28 EOD, all CONDITIONAL contractors fail to resolve by June 30 EOD, and Toptal / Upwork ESCALATE search yields no viable candidates by July 3 EOD.

### Solo Fallback: Confirmed Operative Plan

Per `PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md` Section 6, solo fallback activates when no contractor is confirmed by the hard decision gate (in the current timeline: July 3 EOD).

Log in WORKLOG.md: "July 3 EOD — Solo fallback confirmed. Zero contractor acceptances. No contractor engagement after this date. 5-bundle solo sprint activating per PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md."

### Solo Fallback 9-Week Timeline (from June 29 start)

| Week | Dates | Bundle Focus | Upload Target |
|---|---|---|---|
| 1 | June 29–July 5 | Women's Health writing (Days 1–7) | — |
| 2 | July 6–12 | Women's Health final + Respiratory start | July 6: Women's Health LIVE |
| 3 | July 13–19 | Respiratory writing | — |
| 4 | July 20–26 | Respiratory final + Sleep start | July 20: Respiratory LIVE |
| 5 | July 27–Aug 2 | Sleep writing | — |
| 6 | Aug 3–9 | Sleep final + Immunity start | Aug 10: Sleep LIVE |
| 7 | Aug 10–16 | Immunity writing | — |
| 8 | Aug 17–23 | Immunity final + Digestive start | Aug 24: Immunity LIVE |
| 9 | Aug 24–Sep 30 | Digestive writing + final + export | Sep 30: Digestive LIVE |

**Note**: This schedule shifts the original solo fallback dates by 1 week because the sprint start date has moved from June 22 to June 29. All upload targets shift by 7 days accordingly.

**Phase 3 completion under solo fallback: early October 2026**

### Revenue Impact (No-Go / Solo)

Relative to best-case (July 13 finish): approximately 11 additional weeks to full catalog. At $20/bundle and 3–5 sales/week per listing:
- Women's Health (July 6 solo vs. June 29 contractor): 1-week delay, ~$10–$25 delayed revenue
- Respiratory (July 20 solo vs. July 6 contractor): 2-week delay, ~$20–$50 delayed revenue per week live
- Sleep / Immunity / Digestive: similar proportional delays

**Total delayed revenue relative to best-case**: approximately $200–$500 across the July–September window. This is foregone timing, not lost revenue — all bundles launch eventually at the same price point.

The more significant downstream impact is Phase 4: a solo Phase 3 completing October 2026 pushes Phase 4 (botanical ID guides, expanded medicinal catalog) to November 2026 Wave 1 launch vs. August 2026 in the contractor model. Per `PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md` Section 5, this represents approximately $4,800–$5,200 in foregone Phase 4 Wave 1 and Wave 2 revenue across the August–October delay window.

---

## Kill-Switch: Pause Phase 3 to Q4

### Activation Criteria

The kill-switch is not a performance threshold — it is a role coverage threshold. Phase 3 requires a minimum viable contractor team to proceed on the contractor model. If that minimum is not met by July 5, and the solo fallback is not viable due to user capacity constraints, the kill-switch is the correct decision.

**Kill-switch activates when ALL of the following are true simultaneously**:

1. Fewer than 50% of essential roles confirmed by July 5 EOD
   - Essential roles: 1+ photographer AND 1+ writer
   - If only a photographer is confirmed but no writer: essential coverage fails (50% of essential role types met, but writing is the primary production bottleneck)
   - If only a writer is confirmed but no photographer: partial go — writer begins June 29; photography sourced from Wikimedia Commons CC for Phase 3 launches; kill-switch does NOT activate

2. Toptal and Upwork emergency searches (activated June 29) have yielded no viable candidates by July 5

3. Solo fallback is assessed as not viable for the user (explicit user decision — not an automatic assessment)

**If only condition 1 is met but conditions 2 and 3 are not**: Do not activate the kill-switch. Activate solo fallback instead.

**The kill-switch requires a conscious user decision.** It does not activate automatically. When conditions 1–3 are all true, the kill-switch option is presented; the user decides.

### Kill-Switch Execution

**If the kill-switch is activated (decision made by July 5 EOD)**:

1. Log in WORKLOG.md: "July 5 — Kill-switch activated. Phase 3 paused to Q4 restart (October 2026). Essential role coverage below 50% by July 5 deadline. Solo fallback assessed as not viable. Phase 4 planning unaffected."

2. Stop all contractor outreach. Do not continue running a contractor search after the kill-switch.

3. Preserve all Phase 3 production assets:
   - All content outlines, FTC Quick Reference, CITES verbatim text, Canva templates, CC image attribution log — archived, not deleted
   - Women's Health bundle (already written if June 29 start was achieved): archive in `phase-3/women-s-health-archive/` — do not upload if the kill-switch fires before the Women's Health upload date

4. Set Phase 3 Q4 restart date: October 1, 2026
   - Phase 3 Q4 restart uses the same assets, same contractor outreach channels, same pricing structure
   - Q4 contractor search window: September 1–15, 2026
   - Q4 sprint start: October 1, 2026
   - Q4 finish line: November 15, 2026 (6-week sprint with contractor support)

5. Do not pause Phase 4 planning. Phase 4 botanical ID guide research and competitor analysis are independent of Phase 3 launch status.

### What Is NOT a Kill-Switch Trigger

These conditions are serious but do not justify pausing Phase 3 to Q4:
- Phase 3 launch slipping from June 22 to July 1 — a slip is not a pause
- Only 1 photographer and 1 writer confirmed — this is worst-case, not no-go
- Solo fallback running longer than expected — the solo fallback is a viable path, not a failure mode
- Revenue projections revised downward — pricing uncertainty does not affect content production

The kill-switch is specifically for the case where Phase 3 cannot proceed at all — not for the case where it proceeds more slowly or with less contractor support than planned.

---

## Summary — Scenario Routing Table

| Scenario | Trigger | Finish Line | Kill-Switch | Revenue Impact |
|---|---|---|---|---|
| Best-case | 3–5 ACCEPT by June 28 EOD | July 13 | Not triggered | Minimal (~$60–$180 delayed) |
| Moderate-case | 2–3 ACCEPT + CONDITIONAL resolves by June 30 | July 15–17 | Not triggered | Negligible (2–4 days vs. best-case) |
| Worst-case | 1–2 ACCEPT only; Toptal/Upwork fills gap | July 20+ | Not triggered | ~$30–$90 delayed vs. best-case |
| No-go | Zero ACCEPT; solo fallback operative | October 2026 | Not triggered (solo covers it) | ~$200–$500 delay + Phase 4 cascade |
| Kill-switch | <50% essential roles + solo not viable by July 5 | November 2026 (Q4 restart) | ACTIVATED | Full Phase 3 revenue deferred to Q4 |

---

## Routing Decision Flowchart

```
June 28 EOD — Count ACCEPT responses
  |
  +-- 3+ ACCEPT responses (including 1+ photographer + 1+ writer)
  |   +-- SCENARIO 1: Best-case. Proceed. Finish line July 13.
  |
  +-- 2–3 ACCEPT + 2–3 CONDITIONAL
  |   +-- Schedule clarification calls June 29
  |   +-- June 30 EOD: CONDITIONAL resolution deadline
  |       |
  |       All CONDITIONAL resolve to ACCEPT
  |       +-- SCENARIO 2: Moderate-case. Finish line July 15–17.
  |       |
  |       1+ CONDITIONAL do not resolve
  |       +-- Check: is 1+ photographer AND 1+ writer in the ACCEPT set?
  |           YES: SCENARIO 3 (worst-case, hybrid). Finish line July 20+.
  |           NO: ESCALATE pathway → Toptal/Upwork → July 3 gate
  |
  +-- 1–2 ACCEPT or zero ACCEPT
      +-- ESCALATE pathway: Toptal intake June 29, Upwork listing June 29
      +-- Solo fallback activates June 29 (parallel track)
      +-- July 3 EOD: hard decision gate
          |
          Toptal/Upwork yield confirmed contractor(s)
          +-- SCENARIO 3: Worst-case hybrid. Finish line July 20+.
          |
          No confirmed contractors by July 3 EOD
          +-- SCENARIO 4: No-go. Solo fallback confirmed. Finish line October 2026.
          |
          User assesses solo fallback as not viable
          +-- KILL-SWITCH EVALUATION:
              <50% essential roles AND no Toptal/Upwork candidates AND solo not viable?
              YES: Kill-switch. Phase 3 to Q4. Restart October 1.
              NO: Continue solo fallback regardless.
```

---

## Communication Templates for Each Scenario

### Scenario 1 and 2 — Internal log entry (WORKLOG.md)

```
## Phase 3 Contractor Response Assessment — June 28
ACCEPT responses: [count] — [Names]
CONDITIONAL responses: [count] — [Names, conditions]
ESCALATE (no response): [count] — [Names]
Routing: SCENARIO [1/2/3/4]
Finish line: [date]
Kill-switch: Not triggered / Evaluation pending
Next action: [First action by [date/time]]
```

### Scenario 3 or 4 — User notification (if applicable)

If you need to brief a collaborator or advisor on the scenario:

"Phase 3 contractor responses came in on June 28. We received [X] ACCEPT, [Y] CONDITIONAL, and [Z] no-responses. Routing: [Scenario]. Current finish line: [date]. [If Scenario 3: Toptal intake submitted June 29; Upwork listing live; solo fallback running in parallel.] [If Scenario 4: Solo fallback is the operative plan; all 5 bundles at 12 hrs/week through October.] No action needed from you at this time."

### Kill-switch notification (only if activated)

"Phase 3 is being paused to Q4 restart (October 1). Essential role coverage (1+ photographer + 1+ writer) was not confirmed by the July 5 deadline. Toptal and Upwork searches yielded no viable candidates. All Phase 3 assets are archived and production-ready for the Q4 restart. Phase 4 planning continues on schedule. Phase 3 Q4 contractor search begins September 1."

---

*Prepared: June 28, 2026. This document is operative as of June 28 EOD when contractor responses are due. Cross-references: CONTRACTOR_ONBOARDING_AUTOMATION_LOGIC.md (ACCEPT/CONDITIONAL/ESCALATE routing logic), WEEK_1_ONBOARDING_CHECKLIST.md (Day 1–7 execution on confirmation), PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md (solo fallback timeline and cascade logic), PHASE_3_CONTRACTOR_DECISION_TREE.md (original June 5 go/no-go framework). Version 1.0.*
