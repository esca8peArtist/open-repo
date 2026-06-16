---
title: "Upwork Response Auto-Routing Rules — Deterministic Decision Matrix for All Contractor Response Combinations"
date: 2026-06-16
version: 1.0
status: production-ready
decision-window: June 15–17, 2026
cross-references:
  - PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md (vetting rubric 100-point scale, rate benchmarks, Item 94)
  - PHASE_3_CONTRACTOR_DAILY_TRACKING_CHECKLIST.md (daily log, T1–T9 trigger checks, Item 111)
  - CONTRACTOR_DROPOUT_CONTINGENCY_ACTIVATION.md (post-hire dropout recovery, Item 111)
  - PHASE_3_CONTRACTOR_DECISION_ESCALATION_FRAMEWORK.md (Gate 4/5 logic, Over-Budget Protocol)
  - PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md (solo fallback 9-week schedule, Item 97)
tags: [seedwarden, phase-3, contractor, routing-rules, decision-matrix, upwork, accept-conditional-escalate]
---

# Upwork Response Auto-Routing Rules
## Deterministic If-Then Logic for All Contractor Response Combinations

**Purpose**: This document eliminates all judgment calls from the contractor hiring decision. Every possible combination of Tier A count, average vetting score, and weekly availability maps to exactly one outcome: ACCEPT, CONDITIONAL, or ESCALATE. Use this matrix in conjunction with the daily tracking checklist (June 15–17) and the escalation fallback sequence.

**When to use**: After completing each section of the daily tracking checklist, look up the matching row in the 27-row decision matrix (Section 2) to determine your routing outcome. Do not deviate from the matrix outcome — the logic is pre-authorized.

---

## Section 1 — Decision Framework Architecture

### Three Primary Outcomes

**ACCEPT**: Hire the best Tier A candidate immediately. Score ≥80 on the 100-point rubric (Item 94), availability ≥20 hrs/week confirmed in writing, rate within $1,000–$1,350 budget. Deliver briefing package same day.

**ACCEPT-IMMEDIATE**: Subset of ACCEPT. Score ≥80 AND availability ≥20 hrs/week AND start date confirmed on or before June 22. Execute contract same day, no waiting for June 17 checklist. This is the preferred outcome on any day June 15–17.

**CONDITIONAL**: One or more qualifying conditions met at borderline threshold (score 70–79, or availability 10–19 hrs/week, or rate $1,351–$1,500). Requires a 30-minute evaluation call before making an offer. See Section 3 for CONDITIONAL evaluation steps.

**ESCALATE**: No qualifying candidate or all candidates below threshold. Activate escalation channel sequence: Herbal Academy → Toptal → Solo Fallback. See Section 4 for the escalation sequence with copy-paste emails.

### Three Evaluation Dimensions

**Dimension 1 — Tier A Count**: Number of candidates scoring ≥80 on the 100-point vetting rubric (Item 94). A score of ≥80 meets the preferred threshold from Item 94 Section 2 ("75–100: proceed to interview; qualified lead"). The ACCEPT threshold is set at ≥80 (above the 75-point minimum for interview consideration) to ensure the auto-routing produces hires with margin above the disqualification boundary.

**Dimension 2 — Average Score**: Average vetting score across ALL candidates in the pipeline (Tier A + Tier B), not only those interviewed. Used to assess pipeline health when Tier A count is 0.

**Dimension 3 — Availability ≥20 hrs/week**: Confirmed weekly availability for the June 22 – August 1 sprint. The 20-hour minimum supports the 3-bundle contractor scope: approximately 31–37 total writing hours across 5 weeks = ~6–7 hours per week average, with peak weeks at 10–12 hours. A 20-hour ceiling provides 2× headroom over average pace. Availability below 20 hrs/week does not automatically disqualify but routes to CONDITIONAL.

---

## Section 2 — 27-Row Decision Matrix

**Format**: Each row represents one possible combination of the three evaluation dimensions. Read across to find the routing outcome.

**Column headers**:
- Tier A Count: How many candidates score ≥80 with availability ≥20 hrs/week
- Avg Score: Average vetting score across all candidates in pipeline
- Availability Best Candidate: Weekly hours available per best candidate
- Outcome: ACCEPT / ACCEPT-IMMEDIATE / CONDITIONAL / ESCALATE
- Priority Action: What to do within 2 hours of this determination

### Tier A = 1 or more (preferred zone)

| Row | Tier A Count | Avg Score | Availability (best candidate) | Outcome | Priority Action |
|---|---|---|---|---|---|
| 1 | ≥1 | ≥80 | ≥20 hrs/week AND start ≤ June 22 | **ACCEPT-IMMEDIATE** | Sign contract today. Deliver briefing package same day. |
| 2 | ≥1 | ≥80 | ≥20 hrs/week AND start June 23–29 | **ACCEPT** | Sign contract. Note: contractor misses Women's Health bundle (user-written regardless). Valid hire. |
| 3 | ≥1 | ≥80 | ≥20 hrs/week AND start July 1+ | **CONDITIONAL** | Evaluate: contractor only covers Immunity + Digestive at this start date. Still worth hiring if score is high. 30-min call to confirm exact start. |
| 4 | ≥1 | 75–79 | ≥20 hrs/week AND start ≤ June 22 | **ACCEPT** | Score is above interview threshold (≥75 per Item 94). No disqualifying conditions met. Hire. |
| 5 | ≥1 | 75–79 | ≥20 hrs/week AND start June 23–29 | **ACCEPT** | Same as Row 4 with start caveat. Valid hire. |
| 6 | ≥1 | 75–79 | 10–19 hrs/week | **CONDITIONAL** | Availability is marginal. 30-min call to assess: can they commit to peak weeks (10–12 hrs) within their 10–19 hr ceiling? If yes: hire with milestone dates adjusted. |
| 7 | ≥1 | 75–79 | <10 hrs/week | **ESCALATE** | Insufficient availability for 3-bundle scope. Decline this candidate. Search continues. |
| 8 | ≥2 | ≥80 | ≥20 hrs/week (multiple) | **ACCEPT-IMMEDIATE** | Multiple qualified candidates: hire highest scorer. Log second candidate as backup. |
| 9 | ≥2 | Mixed: 1 at ≥80, others below 70 | ≥20 hrs/week (top candidate) | **ACCEPT** | Hire the ≥80 candidate. The pipeline average is brought down by weak candidates. Focus on top score. |

### Tier A = 0, Tier B present (score 70–79)

| Row | Tier A Count | Avg Score | Availability (best candidate) | Outcome | Priority Action |
|---|---|---|---|---|---|
| 10 | 0 | 70–79 (best score) | ≥20 hrs/week AND start ≤ June 22 | **CONDITIONAL** | Best candidate is Tier B-High. 30-min evaluation call before offer. If interview adds confidence: hire. |
| 11 | 0 | 70–79 (best score) | ≥20 hrs/week AND start June 23–29 | **CONDITIONAL** | Same as Row 10 with start caveat. 30-min call required. |
| 12 | 0 | 70–79 (best score) | 10–19 hrs/week | **CONDITIONAL** | Both score and availability are borderline. Two conditional flags: evaluate both in the call. Route to ESCALATE if either cannot be resolved. |
| 13 | 0 | 70–79 (best score) | <10 hrs/week | **ESCALATE** | Score is borderline AND availability is insufficient. Do not hire. Escalate to Herbal Academy. |
| 14 | 0 | 70–74 (best score) | ≥20 hrs/week | **CONDITIONAL (borderline)** | Score is in the 60–74 range per Item 94 ("brief screening call before full interview"). If all five disqualifying conditions are absent: proceed to 15-min screening call. Do not make an offer without the call. |
| 15 | 0 | 70–74 (best score) | 10–19 hrs/week | **ESCALATE** | Score is at lower threshold AND availability is marginal. Combined risk too high. Escalate. |
| 16 | 0 | 70–74 (best score) | <10 hrs/week | **ESCALATE** | Score is lower threshold AND availability is insufficient. Escalate immediately. |

### Tier A = 0, Tier B below 70 or no candidates

| Row | Tier A Count | Avg Score | Availability (best candidate) | Outcome | Priority Action |
|---|---|---|---|---|---|
| 17 | 0 | 60–69 (best score) | Any | **ESCALATE** | Score is below Item 94 interview threshold. Per Item 94: "Do not proceed. Log rejection reason." |
| 18 | 0 | <60 (best score) | Any | **ESCALATE** | Score is disqualifying range per Item 94 ("Below 60: Do not proceed"). Escalate immediately. |
| 19 | 0 | No scores (no screened proposals) | N/A | **ESCALATE** | No candidates have passed the screening question gate. Escalate all channels simultaneously. |

### Bonus scenarios — rate and timeline complications

| Row | Scenario | Tier A Count | Rate | Outcome | Priority Action |
|---|---|---|---|---|---|
| 20 | Rate above budget: single Tier A candidate at $1,351–$1,500 | 1 | $1,351–$1,500 | **CONDITIONAL** | Activate Over-Budget Protocol: offer fourth-bundle framing at $1,350 plus Sleep right-of-first-offer. If accepted: ACCEPT. If rejected: negotiate reduced scope (Respiratory + Digestive at $700–$800). |
| 21 | Rate above ceiling: single Tier A candidate at $1,501–$2,000 | 1 | $1,501–$2,000 | **CONDITIONAL (tight)** | Over-Budget Protocol Step 1 (fourth-bundle framing). If not resolved by June 14: ESCALATE to NO-GO. |
| 22 | Rate above ceiling: $2,001+ | Any | $2,001+ | **ESCALATE** | Decline immediately. Do not attempt negotiation above $2,000. Economics do not support this rate. |
| 23 | Multiple Tier A candidates all above ceiling | ≥2 | All ≥$1,501 | **CONDITIONAL** | Negotiate with all simultaneously. First to accept $1,350 (with fourth-bundle framing) gets the contract. |
| 24 | Tier A candidate: start date confirmed July 1 or later | ≥1 | Within budget | **CONDITIONAL** | A July 1+ start means contractor covers Immunity + Digestive only. Evaluate whether 2-bundle contract at proportional rate ($700–$900) is worth it. See Section 3 CONDITIONAL evaluation steps. |
| 25 | Toptal match received, score not yet assessed | N/A | Varies | **CONDITIONAL** | Toptal pre-vetting is general writing quality, not herbalism credential depth. Apply full Item 94 rubric. Score before routing. |
| 26 | All channels exhausted, no responses | 0 | N/A | **ESCALATE → SOLO** | Activate solo fallback immediately per PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md. Log: "ESCALATE → SOLO FALLBACK activated [date]." |
| 27 | Contract signed, June 18–19 dropout detected | N/A | N/A | **See CONTRACTOR_DROPOUT_CONTINGENCY_ACTIVATION.md** | 4-hour detection window, solo fallback activation procedure. |

---

## Section 3 — CONDITIONAL Evaluation Steps

When the matrix routes to CONDITIONAL, execute these steps before making an offer. Total time: 30–45 minutes.

### Step 1: Pre-Call Scoring Verification (10 minutes)

Before scheduling the evaluation call, re-check the candidate's vetting rubric score with specific attention to:

1. **Contraindication Rigor sub-score** (max 25 pts): This sub-score is the strongest predictor of sprint performance. A candidate with a total score of 72 but a Contraindication Rigor sub-score of 20 (near maximum) is safer to hire than a candidate with a total of 76 and a Contraindication Rigor sub-score of 8. If Contraindication Rigor sub-score is <15: route to ESCALATE regardless of total score.

2. **Deadline Commitment sub-score** (max 15 pts): Any score <10 on this sub-score means the candidate has not confirmed availability in writing without hedging. Do not proceed to offer without written confirmation.

3. **Disqualifying conditions check**: Confirm none of the five disqualifying conditions are present (see Item 94, Section 2). If any disqualifying condition is present: route to ESCALATE immediately. Do not proceed to the evaluation call.

### Step 2: 30-Minute Evaluation Call

Ask these four questions on the call. Each has a pass/fail determination.

**Q1: Availability confirmation** — "Can you confirm in writing, after this call, that you are available for 20+ hours per week from June 22 through August 1?"
- PASS: "Yes, I can confirm." (written confirmation follows same day)
- FAIL: "Probably" / "I think so" / "It depends on other projects" → route to ESCALATE

**Q2: Contraindication depth spot-check** — "Without looking anything up, can you tell me: what is Ashwagandha's relevant interaction with thyroid medications, and how would you frame it for a practitioner-grade educational guide?"
- PASS: Names thyroid hormone system (TSH/T3/T4) interaction, mentions withanolide mechanism, correctly distinguishes from a drug interaction claim
- FAIL: Cannot name the mechanism, says "I'd need to research that" → route to ESCALATE

**Q3: Scope walk-through** — "The Immunity bundle requires a Goldenseal section with a CITES Appendix II cultivation sourcing sidebar. Can you tell me how you would approach that section — what primary sources and what specific framing?"
- PASS: Mentions NatMed Pro or Memorial Sloan Kettering Integrative Medicine database, distinguishes CITES trade restriction from cultivation sourcing message, mentions United Plant Savers
- FAIL: "I'd Google it" or single-source answer → route to ESCALATE on contraindication rigor

**Q4: Rate resolution** — (Only ask if rate is the conditional factor)
- For Over-Budget candidates: "We can offer $1,350 for the three-bundle scope with first right of offer on a fourth bundle (Sleep and Nervines) in August at the same per-bundle rate. Does that work?"
- PASS: Accepts $1,350 for three bundles
- FAIL: Refuses → route to ESCALATE

### Step 3: Post-Call CONDITIONAL → Final Route

After the evaluation call:
- PASS on all 4 questions → upgrade to ACCEPT
- FAIL on any question → route to ESCALATE
- PASS on Q1–Q3, FAIL on Q4 (rate only) → attempt reduced scope offer ($700–$800 for Respiratory + Digestive; user writes Immunity). If accepted: ACCEPT reduced scope. If rejected: ESCALATE.

---

## Section 4 — ESCALATE Sequence (Copy-Paste Ready)

When the matrix routes to ESCALATE, execute this sequence in order. Do not skip to Toptal before contacting Herbal Academy.

### Escalation Step 1 — June 16 12:00 UTC: Contact Herbal Academy

**Trigger condition**: T6 fires (qualified responses <2 by June 16 12:00 UTC) OR matrix row 17–19 or 26.

**Subject**: Urgent — Medicinal herbalist writer referral, June 22 start

**To**: partnerships@theherbalacademy.com

**Body**:
> We are producing a practitioner-grade medicinal herbs educational guide series and need a writer to begin June 22. We are specifically seeking Advanced + Clinical Herbal Medicine program graduates or instructors with demonstrable contraindication writing experience (herb-drug interactions, FTC-compliant evidence framing, CITES species awareness).
>
> Project scope: three herb bundles (Respiratory, Immunity, Digestive — approximately 11,000 words total), June 22 – August 1, $1,000–$1,350 flat rate with milestone payments.
>
> Could you refer us to any instructors or senior alumni with current availability? We are making a final hiring decision by June 17 EOD and would be grateful for any introductions you can make today or tomorrow.
>
> Thank you, Seedwarden

**Expected response window**: 4–8 hours. If no response by June 17 08:00 UTC: proceed to Step 2.

---

### Escalation Step 2 — June 17 08:00 UTC: Activate Toptal Fallback

**Trigger condition**: T9a fires (Tier A count <1 at 08:00 UTC June 17) OR no Herbal Academy referral received.

**Method**: Go to toptal.com/hire → fill out client intake form with the following spec:

> **Title**: Medicinal Herbalist Writer — Practitioner-Grade Herb Guides
> **Description**: Three educational herb bundles (Respiratory, Immunity, Digestive), ~11,000 words, June 22 – August 1 sprint. Writer must have verifiable herbalist credentials (AHG RH, ND, or clinical herbal certification), demonstrated contraindication writing experience (herb-drug interaction tables from primary sources), and FTC-compliant health language background. Budget: $1,000–$1,350 flat rate.
> **Specialization**: Medical herbalist writer with clinical contraindication experience

**Expected Toptal match turnaround**: 48–72 hours (standard). By June 17 at 08:00 UTC, Toptal was activated earlier in the search window. Check for any pending Toptal match presentation.

**If Toptal match arrives June 17**: Apply full Item 94 vetting rubric. Route match to the 27-row matrix (Rows 24–25 apply to Toptal candidates). If match scores ≥75 and availability ≥20 hrs/week: ACCEPT. Budget note: Toptal adds 10–15% fee above contractor rate. A contractor quoting $1,200 through Toptal = $1,320–$1,380 true cost. Adjust offer accordingly: quote the contractor $1,175 maximum to stay within $1,350 ceiling after Toptal fees.

---

### Escalation Step 3 — June 17 15:00 UTC: Activate Solo Fallback (if no contractor)

**Trigger condition**: T8 fires (no signed contract by this point) AND Toptal match not yet received or not qualifying.

**Action**: Log solo fallback activation in WORKLOG.md.

**WORKLOG entry**:
```
SOLO FALLBACK ACTIVATED — June 17 [time] UTC
Reason: No qualified contractor confirmed within June 5–17 search window.
Pipeline summary: Total evaluated: [X]. Tier A: [X]. Best score: [X]/100.
Activation: PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md — 9-week solo sprint June 22 – September 24 at 12 hrs/week.
Phase 4 start: October 1, 2026 (shifted from July 14).
Phase 4 Wave 1 launch: November 1, 2026 (shifted from August 1).
Phase 5 start: February 1, 2027 (shifted from November 1, 2026).
No contractor engagement after June 17 23:00 UTC.
```

**Immediate actions on solo fallback activation**:
1. Stop all contractor outreach — do not respond to new proposals after 23:00 UTC June 17
2. Update Phase 4 planning dates per the WORKLOG entry above
3. Confirm sprint preparation is complete: CC images (14 species pre-staged), Canva palette loaded, attribution log complete, content outlines finalized for all 5 bundles
4. Set weekly monitoring cadence in WORKLOG.md for the 9-week solo sprint (Friday entries)

---

## Section 5 — Email Templates (Copy-Paste Ready)

### Template A — ACCEPT-IMMEDIATE Offer Email

**Subject**: Medicinal herb writer engagement — offer, June 22 start

**To**: [candidate email]

> [Name],
>
> Based on your proposal and screening question responses, we would like to offer you the Seedwarden Phase 3 writing engagement.
>
> Scope: Three medicinal herb bundles — Respiratory Health, Immunity Support, and Digestive Support — approximately 11,000 words total. Full content outlines, FTC Quick Reference, CITES sidebar verbatim text, and attribution log template will be delivered in a briefing package upon contract signing.
>
> Rate: $[amount] flat rate, paid across four milestones: 25% on signing, 25% on Respiratory first draft delivery (July 1 target), 25% on Immunity first draft delivery (July 8 target), 25% on Digestive final draft completion (July 20 target).
>
> Sprint window: June 22 – August 1. Sprint Day 1 briefing call: June 22, [time] ET (1 hour).
>
> To proceed: please confirm acceptance of this offer by replying to this email. I will send the contract and deposit invoice within 24 hours of your confirmation.
>
> Looking forward to working together on this project.
>
> Seedwarden

---

### Template B — CONDITIONAL Evaluation Call Request

**Subject**: Seedwarden writer role — 30-minute evaluation call request

**To**: [candidate email]

> [Name],
>
> Thank you for your proposal and screening question responses. We would like to schedule a 30-minute evaluation call to discuss the project scope in more detail before moving to a formal offer.
>
> The call will cover: availability confirmation for the June 22 – August 1 sprint, a brief conversation about contraindication research approach (specifically for the Immunity bundle's Ashwagandha and Goldenseal sections), and rate finalization if needed.
>
> Please reply with your availability for a 30-minute call in the next 24 hours. We are making a final hiring decision by June 17 EOD.
>
> Seedwarden

---

### Template C — ESCALATE: Decline (Non-Qualifying Candidate)

**Subject**: Re: Medicinal herb writer — Seedwarden

**To**: [candidate email]

> [Name],
>
> Thank you for your proposal and for taking the time to answer our screening questions. After reviewing your submission, we have decided to move forward with a candidate whose background more closely matches our contraindication research requirements for this specific project.
>
> We appreciate your interest in the project and wish you well in your other work.
>
> Seedwarden

---

### Template D — Over-Budget Protocol (Negotiation Offer)

**Subject**: Re: Medicinal herb writer — revised proposal

**To**: [candidate email]

> [Name],
>
> Thank you for your proposal. Your background and screening responses meet our clinical accuracy standard for this project.
>
> Our budget for the three-bundle scope (Respiratory, Immunity, Digestive) is $1,000–$1,350. We are also planning a fourth bundle — Sleep and Nervines (Valerian, Passionflower, Lemon Balm, Lavender, approximately 3,500 words) — in early August on the same timeline and format.
>
> We would like to offer: $1,350 for the three-bundle scope now, with first right of offer on the fourth bundle at your standard rate for a similar scope. Would that work for you?
>
> We need to finalize our contractor selection by June 15, so please let us know by June 14 EOD.
>
> Seedwarden

---

### Template E — Offer with Counter-Counter (Reduced Scope)

**Subject**: Re: Medicinal herb writer — adjusted scope offer

**To**: [candidate email]

> [Name],
>
> We appreciate your consideration of our project. If the three-bundle rate does not work within our budget, we would like to propose an adjusted scope: Respiratory Health and Digestive Support bundles only (approximately 7,200 words, two bundles) at $700–$800 flat rate.
>
> Under this arrangement, the Immunity Support bundle would remain with our primary writer. The delivery schedule and milestone structure would be the same: deposit on signing, Respiratory milestone July 1, Digestive final July 20.
>
> Please let us know if this adjusted scope is workable. We need a decision by June 14 EOD.
>
> Seedwarden

---

## Section 6 — ACCEPT-IMMEDIATE Fast Path

When the matrix routes to ACCEPT-IMMEDIATE (Row 1 or Row 8), execute this sequence same day:

**Step 1** (within 1 hour): Send Template A offer email.
**Step 2** (upon candidate confirmation, same day): Send contract draft. Include:
- Work-for-hire clause (Seedwarden retains all IP on delivery)
- Confidentiality clause (no public disclosure before launch)
- Milestone payment schedule (25%/25%/25%/25%)
- Delivery dates: Respiratory July 1, Immunity July 8, Digestive July 20
- Revision clause: one revision cycle per bundle at no additional charge
**Step 3** (within 24 hours of contract confirmation): Send briefing package.
- Full content outlines for all three bundles
- FTC Quick Reference (evidence-tier framing, hedging language to avoid)
- CITES sidebar verbatim text (Goldenseal — pre-drafted)
- Attribution log template
- Export specs (PDF format, Canva template reference)
**Step 4** (June 22): Sprint Day 1 briefing call (1 hour). Cover CITES sidebar, FTC framing, Goldenseal CITES cultivation message, Ashwagandha thyroid framing, Etsy audience context.

**WORKLOG entry for ACCEPT-IMMEDIATE**:
```
CONTRACTOR ACCEPT-IMMEDIATE — [date] [time] UTC
Candidate: [name] | Channel: [Upwork/AHG/etc.]
Score: [X]/100 | Availability: [X] hrs/week | Start: [date]
Rate: $[amount] flat (within $1,000–$1,350 budget)
Contract signed: [date]
Deposit paid: $[amount] on [date]
Briefing package delivered: [date]
Phase 4 start: July 14 (contractor model active)
```

---

*Prepared: June 16, 2026. Version 1.0. Item 111 deliverable. Cross-references: PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md (Item 94 — vetting rubric 100-point scale, Tier definitions, rate benchmarks $1,000–$1,350 target, $1,500 ceiling); PHASE_3_CONTRACTOR_DAILY_TRACKING_CHECKLIST.md (T1–T9 trigger status checks); CONTRACTOR_DROPOUT_CONTINGENCY_ACTIVATION.md (Row 27 dropout scenario); PHASE_3_CONTRACTOR_DECISION_ESCALATION_FRAMEWORK.md (Over-Budget Protocol, Gate 4/5 go/no-go logic); PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md (Item 97 — solo fallback activation, Phase 4 October 1 start, Phase 5 February 1 2027 start).*
