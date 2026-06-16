---
title: "Contractor Dropout Contingency Activation — Post-Hire Detection, Solo Fallback Activation, and Phase 4 Cascade"
date: 2026-06-16
version: 1.0
status: production-ready
activation-scenario: Contractor confirmed June 17, drops June 18–19
detection-window: 4 hours from first missed signal
solo-sprint-window: July 1 – September 24, 2026 (revised, if dropout pre-launch) OR June 22 – September 24 (if dropout post-launch-start)
cross-references:
  - PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md (9-week solo schedule, cascade triggers, Item 97)
  - PHASE_3_CONTRACTOR_DECISION_TREE.md (mid-sprint dropout procedure, payment on dropout)
  - PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md (contractor tracking log format, Item 94)
  - UPWORK_RESPONSE_AUTO_ROUTING_RULES.md (initial hiring routing, Item 111)
  - PHASE_3_CONTRACTOR_DAILY_TRACKING_CHECKLIST.md (June 15–17 tracking, Item 111)
tags: [seedwarden, phase-3, contractor, dropout, contingency, solo-fallback, phase-4-cascade]
---

# Contractor Dropout Contingency Activation
## Post-Hire Detection, 2–3 Hour Activation Sequence, and Phase 4 Cascade

**Scenario**: A contractor is hired on June 17 (or earlier in the June 15–17 window), confirms a June 22 sprint start date, then goes silent or explicitly drops on June 18 or June 19.

**Purpose**: This document removes all ambiguity from the post-hire dropout response. Every step is timed and sequenced. The activation sequence completes in 2–3 hours from detection. No user deliberation is required — the procedure runs deterministically from detection to solo fallback confirmation.

---

## Section 1 — Dropout Detection (Step 0)

### Detection Signal 1: Email Silence

If the contractor was hired June 17 and has not replied to the briefing package delivery email by:
- **June 18 10:00 UTC**: Send a check-in email (Section 2, Step 1).
- **June 18 14:00 UTC**: If no response to the check-in: assume dropout confirmed. Begin Step 2.

### Detection Signal 2: Explicit Dropout Message

If the contractor sends an email on June 18 or June 19 stating they cannot continue (illness, double-booking, scope concern, personal emergency):
- Do NOT reply immediately.
- Read the email in full.
- Determine if the dropout is:
  - **Permanent** (cannot complete any part of the engagement) → begin Step 1 immediately (clarification question is still required)
  - **Partial** (can complete one bundle but not all three) → evaluate partial engagement. If partial scope is Respiratory only (one bundle, $300–$400): evaluate whether partial hire is worth it given coordination overhead. Default: decline partial and activate full solo fallback.

### Detection Signal 3: No-Show at Briefing Package Confirmation

If the contractor was expected to confirm receipt of the briefing package by June 18 09:00 UTC and has not done so by June 18 12:00 UTC: treat as Detection Signal 1 (email silence). Begin Step 1 at June 18 12:00 UTC.

### Detection Window

From first detection signal to dropout confirmed: **maximum 4 hours**.

```
[Detection signal fires] → 15-min clarification window → [14:00 UTC if no response] → Dropout confirmed
```

---

## Section 2 — Activation Sequence (2–3 Hours Total)

### Step 1 — Clarification Question (15 minutes | June 18 10:00–10:15 UTC)

**Send this email immediately upon detecting Signal 1 or Signal 2**:

**Subject**: Seedwarden sprint — quick check-in

**To**: [contractor email]

> [Name],
>
> I wanted to check in quickly — I sent the briefing package yesterday and wanted to make sure you received it. Could you confirm receipt and let me know if you have any questions before our June 22 briefing call?
>
> If anything has changed on your end regarding availability or the project timeline, please let me know as soon as possible — we need to know by [14:00 UTC today] so we can adjust our planning if needed.
>
> [Your name]

**Clock starts**: From the moment this email is sent, the confirmation window runs until 14:00 UTC June 18.

---

### Step 2 — Dropout Confirmed (Immediately at 14:00 UTC if no response | or upon explicit dropout message)

**If no response by 14:00 UTC**: Dropout is confirmed. Do not send another email. Do not wait past 14:00 UTC.

**If explicit dropout message received before 14:00 UTC**: Dropout confirmed at message receipt time.

**Immediately upon dropout confirmation**:

1. Open PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md — this is now the operative plan.
2. Open WORKLOG.md — log the dropout (Section 5, this document).
3. Proceed to Step 3 within 30 minutes.

---

### Step 3 — Activate Solo Fallback (30 minutes | June 18, within 1 hour of dropout confirmation)

**Determine whether the dropout occurs BEFORE or AFTER Phase 3 launch (June 22)**:

#### Scenario A: Dropout Before June 22 Launch (June 18–21)

This is the scenario described in the task context. Dropout is confirmed June 18–19, before the sprint launch.

**Key decision**: If dropout is detected before June 22, **do NOT launch Phase 3 on June 22**.

Rationale: The sprint was planned around a contractor covering 3 bundles. If the contractor drops before launching, the Phase 3 solo fallback requires reconfiguring for a 9-week solo window. Launching June 22 under a misaligned plan creates pace and quality risk. Instead:
- Delay Phase 3 launch to **July 1** (revised 9-week window: July 1 – September 24)
- This gives 12 additional days to confirm sprint preparation is complete (CC images, Canva palette, content outlines, attribution log)
- Women's Health upload shifts from June 29 to **July 6** (one week delay — the sole concession to the pre-launch dropout)

**Revised solo sprint schedule (Scenario A — dropout before June 22)**:

| Week | Dates | Bundle Focus | Hours/week | Upload Target |
|---|---|---|---|---|
| 1 | July 1–7 | Women's Health writing (Days 1–7) | 12 | — |
| 2 | July 8–14 | Women's Health final + Respiratory start | 12 | July 6 (end of Week 1): Women's Health LIVE |
| 3 | July 15–21 | Respiratory writing | 12 | — |
| 4 | July 22–28 | Respiratory final + Sleep start | 12 | July 20: Respiratory LIVE |
| 5 | July 29–Aug 4 | Sleep writing | 12 | — |
| 6 | Aug 5–11 | Sleep final + Immunity start | 12 | Aug 10: Sleep LIVE |
| 7 | Aug 12–18 | Immunity writing | 12 | — |
| 8 | Aug 19–25 | Immunity final + Digestive start | 12 | Aug 24: Immunity LIVE |
| 9 | Aug 26–Sep 24 | Digestive writing + final + export | Variable | Sep 24: Digestive LIVE |

**Phase 4 cascade (Scenario A)**:
- Phase 4 start: October 1 (same as standard solo fallback; +79 days vs. contractor model July 14 start)
- Phase 4 Wave 1 launch: November 1 (was August 1 under contractor model)
- Phase 4 Wave 2 launch: December 1 (was August 31)
- Phase 5 start: February 1, 2027 (was November 1, 2026)

**Women's Health critical path note**: The June 29 upload date is the zero-float node of Phase 3. Under Scenario A (July 1 launch), Women's Health uploads July 6 — one week delayed. This 7-day slip on Women's Health is the sole unavoidable consequence of the pre-launch dropout. All subsequent upload dates shift proportionally by 7 days from the standard solo fallback schedule.

#### Scenario B: Dropout After June 22 Launch (Sprint Already Running)

If the contractor drops after June 22 but before any bundle is delivered (June 22–July 1):
- The contractor has the briefing package but has produced nothing.
- User absorbs the full 3-bundle contractor scope into the solo sprint.
- Activate standard PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md upload dates (Respiratory July 13, Sleep August 3, Immunity August 17, Digestive September 24).
- Women's Health June 29 is not affected (user-written in all models).
- **Do NOT delay the sprint launch** — writing is already underway.

If the contractor drops after Respiratory first draft delivered (July 1–July 8):
- Respiratory bundle draft is recoverable. User performs revision pass (estimated 2–4 hours).
- Immunity and Digestive shift to solo fallback.
- Upload date cascade: Respiratory July 8 (revised), Immunity July 27, Digestive August 17.
- Per PHASE_3_CONTRACTOR_DECISION_TREE.md: hold Milestone 2 (Respiratory payment) until revision is confirmed.

---

### Step 4 — Document (Within 1 hour of Step 3)

Log the dropout in WORKLOG.md using this format:

```
CONTRACTOR DROPOUT LOG — [Date] [Time] UTC
===============================================
Detection signal: [email silence by 14:00 UTC / explicit dropout message at (time)]
Contractor name: [name]
Channel hired through: [Upwork / AHG / direct]
Contract signed: [date]
Deposit paid: $[amount] on [date]
Dropout date confirmed: [date] [time] UTC

Dropout reason (if provided): [verbatim from email, or "no response"]
Partial engagement offered? [YES: [scope offered] — ACCEPTED / DECLINED] | [NO]

Dropout phase: [Before June 22 launch (Scenario A)] OR [After June 22 launch (Scenario B)]

Sprint plan activated: PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md
Solo sprint window: [July 1 – Sep 24 (Scenario A)] OR [June 22 – Sep 24 (Scenario B)]
Women's Health upload: [July 6 (Scenario A)] OR [June 29 (Scenario B)]
Respiratory upload: [July 20 (Scenario A)] OR [July 13 (Scenario B)]

Payment action: [Deposit forfeited (no deliverables received)] OR [Milestone 2 held pending revision (Respiratory draft received)]

Phase 4 impact:
  Phase 4 start: October 1, 2026
  Phase 4 Wave 1 launch: November 1, 2026
  Phase 4 Wave 2 launch: December 1, 2026
  Phase 5 start: February 1, 2027
```

---

### Step 5 — Notify (Within 2 hours of dropout confirmation)

Send the pre-drafted user notification (below) as an internal note or message to the project log. This step captures the Phase 4 adjusted timeline and revised sprint plan in a single document for future reference.

**Pre-drafted internal notification** (fill in brackets):

```
PHASE 3 SPRINT UPDATE — [Date] [Time] UTC
==========================================

Contractor dropout confirmed at [time] UTC on [date].

Reason: [if provided] / [No response received by 14:00 UTC June 18]

Sprint plan: Solo fallback activated. 9-week solo schedule per
PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md (Item 97).

Launch date: [June 22 (Scenario B)] OR [July 1 (Scenario A — dropout before launch)]

Upload schedule:
  Women's Health: [June 29 (Scenario B)] OR [July 6 (Scenario A)]
  Respiratory: [July 13 (Scenario B)] OR [July 20 (Scenario A)]
  Sleep: [August 3 (Scenario B)] OR [August 10 (Scenario A)]
  Immunity: [August 17 (Scenario B)] OR [August 24 (Scenario A)]
  Digestive: September 24 (both scenarios)

Phase 4 adjusted timeline:
  Phase 4 start: October 1, 2026 (+79 days vs. contractor model)
  Wave 1 launch: November 1, 2026
  Wave 2 launch: December 1, 2026
  Phase 5 start: February 1, 2027

Women's Health critical path: [INTACT — June 29 (Scenario B)] OR [7-day slip — July 6 (Scenario A)]

Payment resolution:
  Deposit: $[amount] — [Forfeited / Refund requested per contract terms]
  Milestone 2: [Held pending Respiratory revision] OR [Not paid — no deliverables]

No further contractor search. Solo fallback is now the confirmed Phase 3 model.
12 hrs/week pace. Non-negotiable ceiling.
```

---

## Section 3 — Phase 4 Cascade Impact Table

This table consolidates the full Phase 4 timeline impact for both paths and both scenarios. Reference this table when updating downstream planning assumptions.

### Path A: Contractor Model (Reference — not activated if dropout occurs)

| Milestone | Date |
|---|---|
| Phase 3 Women's Health live | June 29, 2026 |
| Phase 3 sprint close (all 5 bundles) | August 3, 2026 |
| Phase 4 start (botanical ID guides) | July 14, 2026 (concurrent with late Phase 3) |
| Phase 4 Wave 1 launch (9 guides) | August 1, 2026 |
| Phase 4 Wave 2 launch (9 guides) | August 31, 2026 |
| Phase 5 start (API/SDK, multi-format) | November 1, 2026 |
| Q2 2027 market launch | April 2027 |

### Path B: Solo Fallback (Activated on contractor dropout)

#### Scenario B (dropout after June 22 launch start)

| Milestone | Date | Delta vs. Contractor |
|---|---|---|
| Phase 3 Women's Health live | June 29, 2026 | +0 days |
| Phase 3 Respiratory live | July 13, 2026 | +7 days |
| Phase 3 Sleep live | August 3, 2026 | +21 days |
| Phase 3 Immunity live | August 17, 2026 | +28 days |
| Phase 3 Digestive live (sprint close) | September 24, 2026 | +52 days |
| Phase 4 start | October 1, 2026 | +79 days |
| Phase 4 Wave 1 launch | November 1, 2026 | +92 days |
| Phase 4 Wave 2 launch | December 1, 2026 | +92 days |
| Phase 5 start | February 1, 2027 | +92 days |
| Q2 2027 market launch | May 2027 | +30 days |

#### Scenario A (dropout before June 22, revised July 1 launch)

| Milestone | Date | Delta vs. Contractor |
|---|---|---|
| Phase 3 Women's Health live | July 6, 2026 | +7 days |
| Phase 3 Respiratory live | July 20, 2026 | +14 days |
| Phase 3 Sleep live | August 10, 2026 | +28 days |
| Phase 3 Immunity live | August 24, 2026 | +35 days |
| Phase 3 Digestive live (sprint close) | September 24, 2026 | +52 days |
| Phase 4 start | October 1, 2026 | +79 days |
| Phase 4 Wave 1 launch | November 1, 2026 | +92 days |
| Phase 4 Wave 2 launch | December 1, 2026 | +92 days |
| Phase 5 start | February 1, 2027 | +92 days |
| Q2 2027 market launch | May 2027 | +30 days |

**Key finding**: Scenario A vs. Scenario B differ only in Women's Health (7-day slip) and Respiratory (7-day slip). Phase 4 start date is October 1 in both scenarios — the pre-launch vs. post-launch dropout distinction does not change the Phase 4 cascade.

**Revenue impact** (solo fallback vs. contractor, from PHASE_3_CONTRACTOR_DECISION_ESCALATION_FRAMEWORK.md Section 4):
- Phase 3 delayed bundles: approximately $195–$864 in delayed first-month revenue
- Phase 4 delayed launch: approximately $10,514 in foregone revenue across August–October 2026 delay window
- **Total impact**: approximately $10,700–$11,400 in foregone or delayed revenue. This is foregone revenue (shifted to Nov 2026 – Jan 2027), not lost revenue — content is not destroyed, only delayed.

---

## Section 4 — Scope Implications: Women's Health Critical Path

**Women's Health bundle is critical path in both contractor and solo models.**

In every scenario, Women's Health is user-written. The contractor scope covers Respiratory, Immunity, and Digestive. Women's Health upload (June 29 under contractor model, July 6 under Scenario A solo, June 29 under Scenario B solo) is the zero-float node of Phase 3.

**Scope note (from PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md Section 1)**:
- Women's Health establishes the 8-section structural template that transfers to all subsequent bundles
- Women's Health investment in the template pays forward in Weeks 2–9 of the solo sprint
- Women's Health FTC compliance pass and contraindication register format are the source of truth for all subsequent bundles
- The June 29 (or July 6 in Scenario A) upload date has zero flex in either model

**Implication for dropout timing**: A contractor dropout detected on June 18 (Scenario A) delays Women's Health by 7 days (June 29 → July 6). This is the only unavoidable consequence. A contractor dropout detected June 22 or later (Scenario B) does not delay Women's Health at all — the user is already writing it.

---

## Section 5 — Recovery Path: What Changes If Dropout Detected Before June 22

**Do NOT launch Phase 3 on June 22 if dropout detected before June 22.**

The June 22 launch date is tied to the contractor-assisted model's sprint structure. Under the solo fallback, launching June 22 means all solo fallback bundles are written on the original (compressed) contractor timeline — the same pace overload that motivated contractor sourcing.

**Instead**:
1. Pause until July 1.
2. Use June 18–30 (12 days) for sprint preparation:
   - Confirm all 14 CC botanical images are staged in Canva
   - Complete the content outline reviews for all 5 bundles
   - Run the FTC Quick Reference preparation for each bundle
   - Complete the CITES sidebar verbatim pre-draft for Goldenseal (Immunity bundle)
   - Update the attribution log template for solo-model sourcing
3. Launch July 1 with the revised 9-week schedule (Scenario A above).
4. Women's Health uploads July 6 — one week after the original June 29 date.

**What does NOT change**: Phase 4 start remains October 1. The solo fallback sprint window ends September 24 in both scenarios. No revenue is permanently lost — all bundles still launch, just 7 days later in Scenario A.

---

## Section 6 — Payment Resolution on Dropout

### If dropout occurs before any deliverable is received (June 18–19, no bundles written)

Per PHASE_3_CONTRACTOR_DECISION_TREE.md (Mid-Sprint Dropout Procedure, payment section):

**Deposit ($300 — 25% of $1,200 example contract)**: Per standard contractor agreement, deposits for work-for-hire engagements that terminate before any deliverable is received may be subject to refund or forfeiture depending on contract terms. The recommended contract language is: "If contractor is unable to complete the engagement for any reason, milestones are paid only for delivered and accepted work. Advance deposits are non-refundable."

**Action**:
- If deposit was paid and contract includes non-refundable deposit language: forfeit. Log amount in WORKLOG dropout entry.
- If contract does NOT include explicit non-refundable language: send one polite refund request email (see Template F below). Do not escalate beyond one email unless deposit exceeds $500.
- Legal escalation threshold: $500 minimum, 14 days of non-response after refund request.

### If dropout occurs after Respiratory first draft delivered (after July 1)

- Milestone 2 (Respiratory, 25%): **Hold** until user completes revision pass and accepts the draft. Per PHASE_3_CONTRACTOR_DECISION_TREE.md: "Pay Milestone 2 only after Respiratory draft is reviewed and accepted."
- Milestones 3 and 4 (Immunity, Digestive): Cancelled. Do not pay.
- If the Respiratory draft is unusable (passes none of the FTC check gates on contraindication review): hold Milestone 2 as well and treat as a partial dropout.

### Template F — Deposit Refund Request (if applicable)

**Subject**: Re: Seedwarden writing engagement — deposit refund request

**To**: [contractor email]

> [Name],
>
> I was sorry to hear that you are unable to continue with the Seedwarden project. As the engagement ended before any work was delivered, I would like to request a refund of the deposit paid on [date] in the amount of $[amount].
>
> Please confirm refund within 7 days. Thank you for your time.
>
> [Your name]

---

*Prepared: June 16, 2026. Version 1.0. Item 111 deliverable. Cross-references: PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md (Item 97 — 9-week solo schedule, scope reduction cascades, Phase 4 October 1 start date, Phase 5 February 1 2027 start, Women's Health June 29 zero-float node); PHASE_3_CONTRACTOR_DECISION_TREE.md (mid-sprint dropout detection, payment on dropout, 3-day silence detection); PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md (Item 94 — contractor tracking log format, vetting rubric); UPWORK_RESPONSE_AUTO_ROUTING_RULES.md (Item 111 — Row 27 dropout scenario, initial hiring routing); PHASE_3_CONTRACTOR_DECISION_ESCALATION_FRAMEWORK.md (revenue impact analysis — $10,700–$11,400 total impact quantification).*
