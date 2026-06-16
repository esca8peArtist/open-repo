---
title: "Phase 3 Contractor Daily Tracking Checklist — June 15–17 Decision Window"
date: 2026-06-16
version: 1.0
status: production-ready
decision-window: June 15–17, 2026
hard-deadline: June 17, 2026 23:00 UTC
run-checklist-at: 12:00 UTC daily
cross-references:
  - PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md (vetting rubric 100-point scale, Tier definitions, Item 94)
  - PHASE_3_CONTRACTOR_DECISION_ESCALATION_FRAMEWORK.md (Gate 4/5 go/no-go logic)
  - UPWORK_RESPONSE_AUTO_ROUTING_RULES.md (auto-routing matrix — companion doc, Item 111)
  - CONTRACTOR_DROPOUT_CONTINGENCY_ACTIVATION.md (post-hire dropout recovery, Item 111)
  - PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md (9-week solo schedule, Item 97)
tags: [seedwarden, phase-3, contractor, daily-tracking, upwork, decision-gate, June-15-17]
---

# Phase 3 Contractor Daily Tracking Checklist
## June 15–17 Upwork Response Window — Four-Section Daily Log

**Purpose**: Real-time tracking of contractor search status during the 3-day final decision window. Run this checklist once daily at **12:00 UTC** (before all escalation deadlines). Each day produces four completed log sections. On June 17, the checklist drives the final GO/CONDITIONAL/ESCALATE routing decision.

**How to use**: Copy each day's log block into WORKLOG.md after completing the checks. Do not estimate — fill in actual counts only.

---

## Instructions

Run this checklist daily at **12:00 UTC** on June 15, June 16, and June 17.

Before running the checklist, open:
1. Upwork job posting (posted ~June 5–6): check new proposals tab and new messages tab
2. Email inbox: check for replies from AHG directory outreach, Herbal Academy, Chestnut School, Toptal
3. Contractor tracking log in WORKLOG.md (Section 6, PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md)

Each section takes approximately 10–15 minutes. Total daily checklist time: 30–45 minutes.

---

## Day 1 — June 15, 2026 (12:00 UTC)

### Section 1A — Upwork Response Polling

**What to check**: Open Upwork job posting. Navigate to "Proposals" tab. Count and categorize all proposals received to date.

| Metric | Count | Notes |
|---|---|---|
| Total proposals received (all time) | ___ | Running total since job posted |
| New proposals since June 14 12:00 UTC | ___ | Today's delta |
| Proposals with screening questions answered | ___ | Required before rubric scoring |
| Proposals with no screening question answers | ___ | Skip — do not review without answers |
| Direct messages (inbox) — new since June 14 | ___ | Includes non-Upwork channel replies |

**Tier classification of all screened proposals** (apply vetting rubric from PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md Section 2 before classifying):

| Tier | Definition | Count Today |
|---|---|---|
| Tier A | Vetting score ≥80 AND availability ≥20 hrs/week confirmed | ___ |
| Tier B-High | Vetting score 70–79 AND availability ≥20 hrs/week | ___ |
| Tier B-Low | Vetting score 70–79 AND availability 10–19 hrs/week | ___ |
| Tier C | Vetting score <70 OR availability <10 hrs/week | ___ |
| Unscored (pending rubric review) | Proposals received but not yet scored | ___ |

**Non-Upwork channel responses** (email/direct):

| Channel | Responses Since Launch | Screened? | Score |
|---|---|---|---|
| AHG directory outreach | ___ | Y / N | ___ |
| Herbal Academy partnerships | ___ | Y / N | ___ |
| Chestnut School referral | ___ | Y / N | ___ |
| Toptal match | ___ | Y / N | ___ |

---

### Section 1B — Response Scoring Log (June 15)

For each candidate scored today, complete one row. Use the 100-point rubric from PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md Section 2.

| Candidate Name | Channel | Credential (max 20) | Portfolio (max 20) | Contraindication Rigor (max 25) | Deadline Commit (max 15) | Scope Consistency (max 12) | Preferred Qualifiers (max 8) | **Total /100** | Availability hrs/wk | Interview Scheduled? |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |

**Rubric scoring quick reference** (from Item 94, PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md):
- Credential: AHG RH = 20 pts | ND/MD botanical = 18 pts | Chestnut Professional = 16 pts | Herbal Academy Adv+Clinical = 12 pts | No verifiable credential = 0 pts (DISQUALIFYING)
- Portfolio: Published guide with contraindications + Latin binomials + evidence citations = 20 pts | Blog clinical depth = 14 pts | General wellness = 6 pts | None = 0 pts (DISQUALIFYING)
- Contraindication Rigor: FTC test correct + CITES test correct = 25 pts | FTC correct, CITES partial = 18 pts | FTC partial, CITES correct = 15 pts | Partial both = 8 pts | Fails either = 0 pts (FTC fail DISQUALIFYING)
- Deadline Commitment: Written confirmation, no hedging = 15 pts | Minor caveats = 10 pts | "Probably available" = 3 pts | Unavailable = 0 pts (DISQUALIFYING)
- Scope Consistency: Similar scope prior project cited = 12 pts | Shorter similar = 8 pts | None comparable = 3 pts
- Preferred Qualifiers: All three (Etsy/digital, clinical practice, references) = 8 pts | Two = 5 pts | One = 2 pts | None = 0 pts

**Disqualifying conditions** — immediate elimination regardless of total score:
- Cannot name any CITES Appendix II plant or explain cultivation sourcing implications
- Fails FTC test (rewriting "may help prevent" instead of evidence-tier framing is a fail)
- No verifiable credential
- Unavailable any part of June 22 – August 1 sprint window
- No published sample with species-specific contraindication content

---

### Section 1C — Escalation Trigger Status (June 15)

Check each trigger against current pipeline status. Circle or enter YES/NO.

| Trigger | Threshold | Current Status | Trigger Fires? |
|---|---|---|---|
| T1 — Tier A count | Tier A count = 0 → escalate immediately | Tier A count: ___ | YES / NO |
| T2 — Average score | Average score of all Tier A/B candidates <75 → expand search | Avg score: ___ | YES / NO |
| T3 — Availability | All candidates <20 hrs/week → flag; sole acceptable candidate must be ≥20 hrs | All ≥20 hrs? Y/N | YES / NO |
| T4 — Interview pipeline | No interviews scheduled AND no Tier A candidate → escalate Herbal Academy referral today | Interviews sched: ___ | YES / NO |
| T5 — Rate ceiling | Any candidate quoting ≥$1,501 → activate Over-Budget Protocol | Any over $1,500? Y/N | YES / NO |
| T6 — Upwork total responses | Total proposals <2 by June 15 12:00 UTC → escalate Herbal Academy email today | Total proposals: ___ | YES / NO |
| T7 — Toptal activation | No responses from Upwork or direct channels by June 15 → confirm Toptal intake called | Toptal activated? Y/N | YES / NO |
| T8 — Contract signed | No signed contract by June 15 EOD → Gate 4 solo fallback threshold crossed | Signed? Y/N | YES / NO |
| T9 — Hard deadline | No signed contract by June 17 23:00 UTC → solo fallback confirmed, no contractor | [Check June 17 only] | N/A today |

**Threshold sources**: T1–T4 from PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md Section 2 vetting rubric; T5 from Over-Budget Protocol (PHASE_3_CONTRACTOR_DECISION_TREE.md); T6–T7 escalation thresholds from PHASE_3_CONTRACTOR_DECISION_ESCALATION_FRAMEWORK.md Section 3; T8–T9 from Gate 4/5 decision tree.

---

### Section 1D — June 15 Summary

| Field | Entry |
|---|---|
| Total candidates in pipeline | ___ |
| Tier A candidates (score ≥80, avail ≥20h) | ___ |
| Tier B candidates (score 70–79) | ___ |
| Interviews completed today | ___ |
| Interviews scheduled (upcoming) | ___ |
| Offers made today | ___ |
| Contracts signed | ___ |
| Action taken today | |
| Auto-routing outcome (from UPWORK_RESPONSE_AUTO_ROUTING_RULES.md) | ACCEPT / CONDITIONAL / ESCALATE |
| Solo fallback trajectory? | YES / NO / BORDERLINE |
| Next checkpoint | June 16, 12:00 UTC |

**WORKLOG entry** (paste into WORKLOG.md after completing):
```
CONTRACTOR DAILY LOG — June 15 12:00 UTC
Tier A: [X] | Tier B: [X] | Total pipeline: [X]
Triggers fired: [list T-numbers or NONE]
Action: [what was done]
Auto-routing: [ACCEPT / CONDITIONAL / ESCALATE]
```

---

## Day 2 — June 16, 2026 (12:00 UTC)

### Section 2A — Upwork Response Polling

**CRITICAL THRESHOLD TODAY**: If total qualified responses (Tier A + Tier B-High) < 2 by 12:00 UTC June 16, **contact Herbal Academy partnerships@theherbalacademy.com immediately with escalation request** (see email templates in UPWORK_RESPONSE_AUTO_ROUTING_RULES.md Section 4).

| Metric | Count | Notes |
|---|---|---|
| Total proposals received (all time) | ___ | Running total |
| New proposals since June 15 12:00 UTC | ___ | Today's delta |
| Proposals with screening questions answered | ___ | |
| New direct-channel replies since June 15 | ___ | |

**Tier classification update** (add to June 15 counts):

| Tier | Count Yesterday | New Today | Total |
|---|---|---|---|
| Tier A (≥80 score, ≥20 hrs/week) | ___ | ___ | ___ |
| Tier B-High (70–79, ≥20 hrs/week) | ___ | ___ | ___ |
| Tier B-Low (70–79, 10–19 hrs/week) | ___ | ___ | ___ |
| Tier C (<70 or <10 hrs/week) | ___ | ___ | ___ |
| Unscored | ___ | ___ | ___ |

---

### Section 2B — Response Scoring Log (June 16)

Score any new candidates received since June 15 check. Add rows as needed.

| Candidate Name | Channel | Score /100 | Availability hrs/wk | Start Date Confirmed? | Interview Scheduled? | Status |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |

**June 16 escalation window**: If score ≥80 AND availability ≥20 hrs/week AND start date ≤ June 22: route to ACCEPT-IMMEDIATE (do not wait for June 17 checklist).

---

### Section 2C — Escalation Trigger Status (June 16)

| Trigger | Threshold | Current Status | Trigger Fires? | Action Required |
|---|---|---|---|---|
| T1 — Tier A count | Tier A count = 0 | Tier A: ___ | YES / NO | If YES: expand AHG outreach + confirm Toptal |
| T2 — Average score | Avg score <75 across all candidates | Avg: ___ | YES / NO | If YES: apply CONDITIONAL routing |
| T3 — Availability | All candidates <20 hrs/week | All ≥20? Y/N | YES / NO | If YES: flag for CONDITIONAL |
| T4 — Interview pipeline | No interviews completed | Interviews done: ___ | YES / NO | If YES: schedule emergency 30-min calls today |
| T5 — Rate ceiling | Any candidate ≥$1,501 | Over ceiling? Y/N | YES / NO | If YES: Over-Budget Protocol |
| **T6 — CRITICAL: Total qualified responses** | **<2 qualified responses by 12:00 UTC** | **Total qual: ___** | **YES / NO** | **If YES: email Herbal Academy NOW** |
| T7 — Toptal match | Toptal match not yet received | Match received? Y/N | YES / NO | If YES: review Toptal candidate immediately |
| T8 — Contract signed | No contract signed → Gate 4 threshold passed | Signed? Y/N | YES / NO | If YES: confirm solo fallback trajectory |

**T6 June 16 escalation email** (send immediately if T6 fires):
> Subject: Urgent — Medicinal herbalist writer referral needed by June 17
> To: partnerships@theherbalacademy.com
> Body: "We are searching for a medicinal herbalist writer to begin a practitioner-grade guide project June 22. The ideal candidate holds Advanced + Clinical program credentials and has writing experience in contraindication research. We are offering $1,000–$1,350 flat rate for 11,000 words across three bundles (Respiratory, Immunity, Digestive), June 22 – August 1 sprint. Could you refer us to any instructors or senior program alumni with current availability? We need to confirm by June 17 EOD."

---

### Section 2D — June 16 Summary

| Field | Entry |
|---|---|
| Total candidates in pipeline | ___ |
| Tier A candidates (score ≥80, avail ≥20h) | ___ |
| Interviews completed (cumulative) | ___ |
| Offers made (cumulative) | ___ |
| Contracts signed | ___ |
| T6 escalation sent? (if triggered) | YES / NO / NOT TRIGGERED |
| Toptal match reviewed? | YES / NO / PENDING |
| Action taken today | |
| Auto-routing outcome | ACCEPT / CONDITIONAL / ESCALATE |
| Solo fallback trajectory | YES / NO / BORDERLINE |
| Next checkpoint | June 17, 08:00 UTC (early check) + 12:00 UTC (full checklist) |

**WORKLOG entry**:
```
CONTRACTOR DAILY LOG — June 16 12:00 UTC
Tier A: [X] | Tier B: [X] | Total pipeline: [X]
Triggers fired: [list T-numbers or NONE]
T6 Herbal Academy escalation: [SENT / NOT TRIGGERED]
Action: [what was done]
Auto-routing: [ACCEPT / CONDITIONAL / ESCALATE]
```

---

## Day 3 — June 17, 2026 — TWO CHECKS

**Run a brief early check at 08:00 UTC** (Sections 3A-Early only) and the full checklist at **12:00 UTC**. June 17 is the hard contractor deadline.

### Section 3A-Early — June 17, 08:00 UTC (Early Check Only)

**CRITICAL THRESHOLD**: If Tier A count = 0 at 08:00 UTC June 17, **activate Toptal fallback immediately**.

| Metric | Status at 08:00 UTC |
|---|---|
| Tier A candidates confirmed | ___ |
| Any contract signed or offer accepted? | YES / NO |
| New responses overnight (since June 16 12:00 UTC) | ___ |
| **T9a — If <1 Tier A response by 08:00 UTC June 17: activate Toptal fallback** | TRIGGERED / NOT TRIGGERED |

**T9a Toptal activation email** (send immediately if triggered):
> Subject: Urgent placement request — medicinal herbalist writer, June 22 start
> To: toptal.com/hire (contact form) or account manager
> Body: "We need a medicinal herbalist writer to begin a practitioner guide project June 22. The candidate must have verifiable herbalist credentials (AHG RH or equivalent), demonstrated contraindication writing experience (herb-drug interaction tables), and FTC-compliant health language background. Scope: 11,000 words, three bundles, June 22 – August 1. Budget: $1,000–$1,350 flat. We need a match presented by June 17 15:00 UTC to evaluate today."

---

### Section 3A — Upwork Response Polling (June 17, 12:00 UTC)

| Metric | Count | Notes |
|---|---|---|
| Total proposals received (all time) | ___ | |
| New since June 16 12:00 UTC | ___ | |
| Total with screening questions answered | ___ | |
| New direct channel replies since June 16 | ___ | |

**Final Tier classification** (cumulative totals):

| Tier | Total Count | Best Score in Tier | Availability (best) |
|---|---|---|---|
| Tier A (≥80, ≥20 hrs/week) | ___ | ___ | ___ hrs/wk |
| Tier B-High (70–79, ≥20 hrs/week) | ___ | ___ | ___ hrs/wk |
| Tier B-Low (70–79, 10–19 hrs/week) | ___ | ___ | ___ hrs/wk |
| Tier C (<70 or <10 hrs/week) | ___ | ___ | ___ hrs/wk |

---

### Section 3B — Response Scoring Log (June 17)

Score any candidates not yet scored from prior days. This is the final scoring opportunity.

| Candidate Name | Channel | Score /100 | Availability hrs/wk | Start Date | Rate | Decision |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |

---

### Section 3C — Final Escalation Trigger Status (June 17)

| Trigger | Threshold | Final Status | Triggered? | Action |
|---|---|---|---|---|
| T1 — Tier A count | Tier A = 0 → solo fallback | Tier A: ___ | YES / NO | Log solo fallback activation |
| T2 — Average score | Avg <75 → CONDITIONAL or ESCALATE routing | Avg: ___ | YES / NO | See routing matrix |
| T3 — Availability | All <20 hrs/week → CONDITIONAL | All ≥20? Y/N | YES / NO | See routing matrix |
| T6 — Response count | <2 qualified → Herbal Academy already escalated | Herbal Acad sent? Y/N | DONE / N/A | Confirm |
| T7 — Toptal | No match received by 12:00 UTC | Match received? Y/N | YES / NO | If no match: solo fallback |
| **T8 — Contract signed** | **No contract by June 17 23:00 UTC → solo fallback confirmed** | **Signed? Y/N** | **YES / NO** | **Final gate** |
| **T9 — Hard deadline** | **23:00 UTC June 17 — no contractor accepted after this** | **[Check at 23:00]** | **YES / NO** | **Log outcome** |

---

### Section 3D — June 17 Final Summary and Decision

| Field | Entry |
|---|---|
| Total candidates evaluated (3-day window) | ___ |
| Best candidate: name | |
| Best candidate: score /100 | ___ |
| Best candidate: availability hrs/wk | ___ |
| Best candidate: rate | $___ |
| Best candidate: start date confirmed | ___ |
| Contract signed? | YES / NO |
| Contract signed date/time | ___ UTC |
| **Final auto-routing outcome** | **ACCEPT / CONDITIONAL / ESCALATE** |
| Solo fallback activated? | YES / NO |
| Phase 4 start date (confirmed) | July 14 (contractor) OR October 1 (solo) |

**June 17 WORKLOG entry** (mandatory — paste into WORKLOG.md by 23:00 UTC):
```
CONTRACTOR DECISION LOG — June 17 23:00 UTC
Gate: Gate 5 (Hard Contractor Deadline)
3-day window summary:
  Total evaluated: [X] | Tier A: [X] | Tier B: [X]
  Best score: [X]/100 | Best availability: [X] hrs/wk
Contract signed: [YES → name, date, rate] OR [NO → solo fallback]
Final decision: [ACCEPT / CONDITIONAL / ESCALATE / SOLO FALLBACK]
Phase 4 start: [July 14 / October 1]
Next action: [Brief contractor June 22 OR activate PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md]
```

---

## Tier Definitions Quick Reference

These definitions cross-reference PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md Section 2 (Item 94 vetting rubric):

| Tier | Score Range | Availability | Route |
|---|---|---|---|
| **Tier A** | ≥80 /100 | ≥20 hrs/week | ACCEPT (if start ≤June 22) or ACCEPT-IMMEDIATE |
| **Tier B-High** | 70–79 /100 | ≥20 hrs/week | CONDITIONAL — evaluate interview performance |
| **Tier B-Low** | 70–79 /100 | 10–19 hrs/week | CONDITIONAL — reduced scope option only |
| **Tier C** | <70 /100 | Any | ESCALATE — do not hire |
| **Disqualified** | Any score | Any | REJECT — disqualifying condition triggered |

---

*Prepared: June 16, 2026. Version 1.0. Item 111 deliverable. Cross-references: PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md (Item 94 — vetting rubric 100-point scale, Tier definitions, rate benchmarks $1,000–$1,350); PHASE_3_CONTRACTOR_DECISION_ESCALATION_FRAMEWORK.md (Gate 4/5 go/no-go logic); UPWORK_RESPONSE_AUTO_ROUTING_RULES.md (auto-routing decision matrix, companion document); CONTRACTOR_DROPOUT_CONTINGENCY_ACTIVATION.md (post-hire dropout recovery); PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md (Item 97 — 9-week solo schedule, Phase 4 October 1 start).*
