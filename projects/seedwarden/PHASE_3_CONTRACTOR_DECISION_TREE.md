---
title: "Phase 3 Contractor Decision Tree — Go/No-Go Framework, Backup Roster Activation, and Solo Fallback Procedures"
date: 2026-06-05
version: 1.0
status: production-ready
hard-contractor-deadline: June 17, 2026 EOD
solo-fallback-activation: June 15, 2026 EOD (if 0 confirmed contractors)
phase-3-start: June 22, 2026
solo-fallback-window: June 22 – September 24, 2026 (9 weeks at 12 hrs/week)
cross-references:
  - PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md (search channels, vetting rubric, rate benchmarking)
  - PHASE_3_CRITICAL_PATH_ANALYSIS_JUNE22_JULY13.md (writing schedule, upload dates)
  - PHASE_3_PRODUCTION_SPRINT_RISK_REGISTER.md (contractor dropout risk, mid-sprint procedure)
  - PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md (scope options, bundle word counts)
tags: [seedwarden, phase-3, contractor, decision-tree, go-no-go, solo-fallback, contingency]
---

# Phase 3 Contractor Decision Tree

**Prepared**: June 5, 2026
**Purpose**: Explicit branching logic for every contractor-related decision between now (June 5) and sprint launch (June 22). Covers the initial go/no-go, backup roster escalation triggers, solo fallback activation, mid-sprint dropout procedure, and scheduling logistics for each scenario.

---

## Document Overview

This document answers five questions:

1. Do we have a contractor? When and how do we make that call?
2. If early response is weak, what escalation actions fire and when?
3. If we have only one candidate but they are priced above ceiling, what happens?
4. What triggers the transition from contractor model to solo fallback?
5. If a contractor drops mid-sprint, what is the exact recovery procedure?

Every branch below is a deterministic decision — there are no "use your judgment" nodes. Each node has a threshold, a date, and an action.

---

## Primary Decision Tree

```
TODAY (June 5)
  |
  +-- Action: Launch full outreach (AHG directory, Chestnut, Herbal Academy, Upwork)
  |   Per PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md Section 5
  |
JUNE 8 — FIRST RESPONSE CHECK
  |
  +-- Q: How many substantive replies received from all channels?
          (Substantive = screening question answers submitted or interview request)
          |
          0 replies
          +-- Action: Escalate immediately
          |   - Re-send AHG outreach to second-tier contacts (specialty: Respiratory, Digestive)
          |   - Contact Toptal intake NOW (toptal.com — 48-72 hr match turnaround)
          |   - Post secondary Upwork listing with revised framing (more specific bundle descriptions)
          |   - Email Herbal Academy partnerships for referral (if not already done)
          |   - Log in WORKLOG.md: "June 8 — 0 contractor responses. Escalation activated."
          |   Go to JUNE 10 checkpoint.
          |
          1-3 replies
          +-- Action: Score all respondents on vetting rubric (Section 2, Sourcing Strategy doc)
          |   - Schedule interviews for any candidate scoring 75+
          |   - Hold candidates scoring 60-74 pending interview
          |   - Reject candidates below 60; log reason
          |   Go to JUNE 10 checkpoint.
          |
          4+ replies
          +-- Proceed with scoring and interview scheduling immediately.
          |   No escalation needed. Go to JUNE 10 checkpoint.

JUNE 10 — CANDIDATE QUALITY CHECK
  |
  +-- Q: Do we have at least 1 Tier A candidate (vetting score 75+, interviewed)?
          |
          YES: 1+ Tier A candidates available
          +-- Q: Is their quote within budget ($1,000-$1,350; up to $1,500 ceiling for RH AHG + clinical)?
                  |
                  YES: Quote within budget
                  +-- Action: Prepare contract. Offer by June 12 EOD.
                  |   Target: Signed contract + deposit paid by June 12.
                  |   Go to JUNE 12 checkpoint.
                  |
                  NO: Quote is $1,501-$2,000
                  +-- Action: Attempt negotiation (see Over-Budget Protocol below)
                  |   If negotiation succeeds by June 12: proceed to contract.
                  |   If negotiation fails: go to OVER-BUDGET ESCALATION branch.
                  |
                  NO: Quote is $2,001+
                  +-- Action: Do not negotiate. Decline respectfully.
                  |   Log in WORKLOG.md: "Candidate [name] — rate $[X], declined."
                  |   Move to next candidate or trigger escalation.
          |
          NO: 0 Tier A candidates (no one above 75, or no respondents)
          +-- Action: Escalate — Tier B candidate review
          |   - Review all 60-74 scored candidates for interview
          |   - Expand AHG directory outreach (15 new contacts, filter: any clinical specialty)
          |   - Toptal match should arrive by now; review immediately
          |   Log in WORKLOG.md: "June 10 — No Tier A candidates. Tier B review + expanded search."
          |   Go to JUNE 12 checkpoint.

JUNE 12 — CONTRACT DEADLINE (TARGET)
  |
  +-- Q: Is a contract signed and deposit paid?
          |
          YES
          +-- Action: Deliver full briefing package by June 14.
          |   Contractor confirmed. Go to JUNE 17 confirmation check.
          |
          NO — Tier A candidate in negotiation
          +-- Action: Give 48-hour response window. Final offer by June 14.
          |   If accepted June 13-14: sign, pay deposit. Proceed.
          |   If rejected or no response by June 14: decline. Move to Tier B or solo fallback.
          |
          NO — Tier B candidate (60-74) is best available
          +-- Q: Does Tier B candidate pass all disqualifying conditions? (FTC test, credential, availability)
                  |
                  YES: All disqualifying conditions pass
                  +-- Action: Accept Tier B candidate with enhanced oversight protocol
                  |   (See Enhanced Oversight Protocol below)
                  |   Proceed to contract, adjusted supervision requirements.
                  |
                  NO: Any disqualifying condition fails
                  +-- Action: Do not hire. Solo fallback is safer than a contractor
                      who cannot write FTC-compliant contraindication content.
                      Go to SOLO FALLBACK ACTIVATION branch.

JUNE 14 — FINAL CANDIDATE WINDOW
  |
  +-- Q: Contract signed within 48 hours?
          |
          YES: Contract signed June 13-14
          +-- Briefing package delivery: June 15.
          |   Proceed to sprint. No further escalation needed.
          |   Go to JUNE 17 confirmation check.
          |
          NO: Still negotiating or no candidate
          +-- Action: Final escalation round
          |   - Email all pending Upwork proposals not yet reviewed
          |   - Call Toptal client manager for status update
          |   - Email AHG member services directly for referral assistance
          |   - Set hard personal deadline: sign by June 15 EOD or activate solo fallback
          |   Log in WORKLOG.md: "June 14 — No contract. Final escalation round. 
          |   Solo fallback activates June 15 EOD if no signature."

JUNE 15 — SOLO FALLBACK THRESHOLD
  |
  +-- Q: Is a contract signed?
          |
          YES: Contract signed today
          +-- Accept. Deliver briefing package same day (compressed).
          |   Contractor has 7 days before sprint start — minimum acceptable onboarding.
          |   Brief them on June 22 call first thing. Monitor daily for week 1.
          |
          NO: 0 contractors confirmed by June 15 EOD
          +-- ACTIVATE SOLO FALLBACK IMMEDIATELY
              Log in WORKLOG.md: "June 15 EOD — Solo fallback activated. 
              No contractor confirmed. 12 hrs/week solo model, June 22 – Sept 24."
              Per SOLO FALLBACK ACTIVATION section below.

JUNE 17 — HARD CONTRACTOR DEADLINE
  |
  +-- If contract signed (any date June 5-17): Contractor confirmed. Sprint proceeds as planned.
  |
  +-- If no contract signed by June 17 EOD:
          Solo fallback is active (activated June 15 or now).
          Do not accept a contractor after June 17.
          Rationale: A contractor engaged with fewer than 5 days before sprint launch has
          insufficient time for briefing, onboarding, and sprint Day 1 alignment. The
          risk of misalignment on contraindication standards is higher than the risk of
          solo sprint.
          Log: "June 17 — Hard deadline passed. Solo fallback confirmed. 
          No contractor engagement after this date."
```

---

## Over-Budget Protocol

**Trigger**: Tier A candidate quotes $1,501–$2,000 for the 3-bundle scope.

**Step 1 — Negotiation attempt (June 10–12)**

Open the negotiation with the fourth-bundle framing from the Sourcing Strategy document:

"Our current budget for the three-bundle scope is $1,000–$1,350. However, we are planning a fourth bundle — Sleep and Nervines — in early August on the same timeline and format. If you are open to a three-bundle contract at $1,350 now, with first right of offer on the fourth bundle at your standard rate, would that work?"

Expected outcome: Candidates who quote above ceiling because they underestimated the scope often come back within ceiling when the total engagement value is higher. Candidates who quote above ceiling due to rate structure (minimum engagement fee, platform pricing) will not.

**Step 2 — Scope reduction offer (if Step 1 fails)**

If the candidate is not flexible on total rate: offer a reduced scope.

"Would you be willing to take the Respiratory and Digestive bundles at $700–$800 total, with the Immunity bundle reserved for the user? That reduces your scope to approximately 7,200 words."

This is viable: Immunity is the highest-risk bundle (Goldenseal CITES, Ashwagandha thyroid) and benefits most from user-controlled writing. Respiratory and Digestive are lower-risk for delegation. If the candidate accepts this reduced scope, adjust the sprint writing plan: user writes Women's Health, Immunity, and Sleep; contractor writes Respiratory and Digestive.

**Step 3 — Walk away threshold**

If the candidate will not accept any offer at or below $1,500 total: decline. Log the interaction and move to the next candidate. A contractor at $2,000+ shifts the project economics significantly — at that rate, the hybrid model savings over solo (estimated at $600–$900 in time value) are eliminated.

---

## Solo Fallback Activation Criteria

**Activates when**: 0 confirmed contractors by June 15 EOD (primary) or June 17 EOD (hard final).

**What it means**: The user writes all five bundles at 12 hours per week across a compressed 9-week timeline (June 22 – September 24) rather than the original 4–5 week contractor-assisted sprint.

### Solo Fallback Schedule

| Week | Dates | Bundle Focus | Hrs/Week | Upload Target |
|---|---|---|---|---|
| 1 | June 22–28 | Women's Health writing: Days 1-6 | 12 | — |
| 2 | June 29–July 5 | Women's Health final + Respiratory start | 12 | June 29: Women's Health LIVE |
| 3 | July 6–12 | Respiratory writing | 12 | — |
| 4 | July 13–19 | Respiratory final + Sleep start | 12 | July 13: Respiratory LIVE |
| 5 | July 20–26 | Sleep writing | 12 | July 20: Immunity (if pre-written) |
| 6 | July 27–Aug 2 | Sleep final + Immunity start | 12 | Aug 3: Sleep LIVE |
| 7 | Aug 3–9 | Immunity writing | 12 | — |
| 8 | Aug 10–16 | Immunity final + Digestive start | 12 | Aug 17: Immunity LIVE |
| 9 | Aug 17–Sep 24 | Digestive writing + final | 12 | Sep 24: Digestive LIVE |

**Key differences vs. contractor model**:
- Women's Health June 29 upload date is preserved — this is the critical revenue event and has zero flex
- Respiratory slips from July 6 to July 13 (7-day delay vs. contractor model)
- Sleep slips from July 13 to August 3 (21-day delay)
- Immunity slips from July 20 to August 17 (28-day delay)
- Digestive slips from August 3 to September 24 (52-day delay — extended to accommodate 12 hrs/week pace)
- Total elapsed time: 14 weeks vs. 6 weeks with contractor — 9 weeks of additional calendar time at reduced daily intensity

**Revenue impact of solo fallback**: The extended timeline delays Respiratory, Sleep, and Immunity listings by 7–28 days each. At estimated baseline of 3–8 organic Etsy views/day with 3–5% conversion on a $20–$22 price point, a 21-day slip on Respiratory represents approximately $25–$75 in delayed revenue. This is not a catastrophic financial impact — the solo fallback is a quality and sustainability trade-off, not a revenue emergency.

**The 12 hrs/week ceiling is non-negotiable**: Do not attempt to accelerate beyond 12 hours per week in the solo model. The contractor search showed that the original sprint pace (5+ hours/day, 6 days/week) was the constraint that motivated contractor sourcing. The solo fallback is explicitly designed for sustainable pace — compressing it recreates the same overload that made a contractor attractive.

---

## Backup Roster Activation Triggers

### Trigger 1: No Tier A Responses by June 10

**What fires**: Expand AHG directory outreach from initial 15 contacts to all RH members listing education or writing in their profile (estimated 30–50 members). Activate Toptal if not already done. Post secondary Upwork listing.

**Who owns it**: User. Log activation in WORKLOG.md with date.

### Trigger 2: Only 1 Response, Quote Above $1,500

**What fires**: Over-Budget Protocol (Section above). Simultaneously expand outreach to NAMA, IHA, and Herbal Academy general alumni — broaden the search while negotiating with the sole respondent.

**Decision point**: Can the negotiation close within 48 hours (by June 12)? If yes: proceed. If no: activate backup search in parallel.

### Trigger 3: Only Tier B Candidates Available (60–74 Score) by June 12

**What fires**: Accept the best available Tier B candidate with Enhanced Oversight Protocol, OR activate solo fallback if all Tier B candidates fail any disqualifying condition.

**Enhanced Oversight Protocol for Tier B Contractors**:
- User reviews all contraindication content before the contractor proceeds to the next section (not just at draft delivery)
- User approves the Goldenseal CITES sidebar verbatim text before the contractor writes the surrounding cultivation content
- One additional revision cycle is built into the contract at no extra charge for the first bundle
- Delivery dates are tightened by 2 days each to allow for additional review time (Respiratory delivers June 29 instead of July 1; Immunity July 6 instead of July 8)

### Trigger 4: Contractor Drops Mid-Sprint

**See Mid-Sprint Dropout Procedure section below.**

---

## Mid-Sprint Dropout Procedure

**Detection signal**: Email silence for 3 consecutive days during the sprint (see Risk Register). Or: contractor explicitly notifies of inability to continue.

**Immediate actions (Day 1 of detection)**:

1. Contact contractor by email AND phone (if number was provided in contract)
2. Email subject line: "Seedwarden sprint — urgent response needed within 24 hours"
3. If no response within 24 hours: assume dropout. Begin recovery steps.

**Recovery steps — if dropout occurs before Respiratory first draft delivered (before July 1)**:

The user absorbs the Respiratory bundle into the sprint schedule. The solo fallback schedule above (minus the Women's Health bundle, which is already in progress or complete) activates from the dropout date forward.

Upload date cascade on Respiratory dropout before July 1:
- Respiratory: delay by 7–10 days from original July 6–7 target → July 13–17
- Sleep: delay by 7 days → July 20
- Immunity: delay by 7 days → July 27
- Digestive: delay by 7 days → August 10

**Recovery steps — if dropout occurs after Respiratory first draft delivered (after July 1)**:

The Respiratory bundle draft is recoverable. The user performs the revision pass on the delivered Respiratory draft (estimated 2–4 hours). Immunity and Digestive shift to solo fallback.

Upload date cascade on dropout after July 1:
- Respiratory: no delay if draft delivered; revision adds 2 days to upload → July 8
- Immunity: shifts to user-written, solo pace → July 27
- Digestive: shifts to user-written, solo pace → August 17

**Payment on dropout**:

- If dropout occurs before first bundle draft delivered: forfeit the initial 25% deposit is the user's recovery. Do not pay the remaining milestones.
- If dropout occurs after Respiratory draft delivered: pay the Respiratory milestone (25%). Withhold remaining 50%.
- Contract must include: "If contractor is unable to complete the engagement for any reason, milestones are paid only for delivered and accepted work. Advance deposits are non-refundable. Remaining milestones are cancelled."

**Legal procedure**: If the contractor refuses refund of a deposit paid for undelivered work: the contract work-for-hire clause and the milestone payment schedule define the terms. Most herbalist writers are not going to dispute a $250–$340 deposit. Do not escalate to legal action unless the amount exceeds $500 and the contractor is unresponsive for 14 days.

---

## Contingency Payment Logistics

### Milestone Payment Schedule (Standard)

| Milestone | Trigger | Amount (at $1,200 total) | Payment Method |
|---|---|---|---|
| Deposit | Contract signed | $300 (25%) | Direct transfer or PayPal; or Upwork escrow if platform |
| Milestone 2 | Respiratory first draft delivered and accepted | $300 (25%) | Same method |
| Milestone 3 | Immunity first draft delivered and accepted | $300 (25%) | Same method |
| Milestone 4 | Digestive final draft + all revisions complete | $300 (25%) | Same method |

**Accepted** means: the draft has been reviewed by the user and is approved to proceed to the next stage. Do not release a milestone payment for a draft that has not passed the FTC Quick Reference check — that check is the minimum acceptance gate for each bundle.

### Rush Premium Logic

If the contractor is signed late (June 15–17) and must begin writing with less than one week of prep time before the June 22 sprint launch: offer a $50–$100 rush premium on the Milestone 4 payment (final payment) if all three bundles are delivered on the original schedule. This is not a rate increase — it is a back-loaded incentive for on-time delivery under compressed onboarding. Frame it as: "If all three bundles are delivered by [original dates], we will add $75 to the final milestone as a quality and punctuality bonus."

### International Contractor Payment

If the best available candidate is based outside the US (common for AHG-credentialed herbalists in Canada, UK, and Australia): use PayPal (standard), Wise (lower fees for international transfer), or Upwork's international payment system. Do not use wire transfer for amounts below $500 — the fees erode the project's economics.

---

## Decision Summary Table

| Date | Decision | Trigger | Action |
|---|---|---|---|
| June 8 | Escalation check | 0 replies → escalate; 1+ replies → score and interview | Per Primary Decision Tree |
| June 10 | Tier A availability check | 0 Tier A → Tier B review + expanded search; 1+ Tier A → offer | Per Primary Decision Tree |
| June 10 | Over-budget check | Quote $1,501-$2,000 → negotiate; $2,001+ → decline | Over-Budget Protocol |
| June 12 | Contract target | Signed → briefing; Not signed → final escalation | Per Primary Decision Tree |
| June 14 | Negotiation close | Accepted → sign; Rejected → final escalation round | Per Primary Decision Tree |
| June 15 | Solo fallback threshold | No contract signed EOD → activate solo fallback | Solo Fallback Activation |
| June 17 | Hard deadline | No contract → solo fallback confirmed; no contractor after this date | Hard Contractor Deadline |
| Sprint (ongoing) | Dropout detection | 3 days email silence → contact; 24 hrs no response → assume dropout | Mid-Sprint Dropout Procedure |

---

## Scheduling Logistics — Both Scenarios

### With Contractor

**June 22 (Sprint Day 1)**: 1-hour briefing call. Cover: content outline for Respiratory bundle (Day 1 start), FTC Quick Reference framing (especially Echinacea evidence-tier language), Goldenseal CITES sidebar verbatim (read together on the call), Etsy audience context (practitioner-grade, not general wellness), and revision procedure.

**June 24 (D3)**: User checks in with contractor by email. Request: word count status on Respiratory bundle. Threshold: Respiratory should be at 1,000+ words by June 24 EOD if writing began June 22. If below 800 words: flag early. Not yet a crisis, but worth noting for the June 28 delivery expectation.

**June 28 (D7)**: Respiratory first draft due. User reviews the draft within 48 hours. Specifically check: Echinacea two-species comparison (E. purpurea vs. E. angustifolia distinction must be accurate), raw elderberry toxicity note (sambunigrin must be named), UpS At-Risk sidebar for Echinacea angustifolia (present or absent?). If any of these three items is absent or inaccurate: return for revision before releasing Milestone 2 payment.

**July 8 (D17)**: Immunity first draft due. Check: Goldenseal CITES sidebar verbatim present? Ashwagandha thyroid warning framed correctly (not as drug interaction but as herb-hormone-system interaction)? Berberine framing uses evidence-tier language?

**July 20**: Digestive final draft due. FTC check: Dandelion and Ginger sections must not contain direct digestive disease claims without evidence-tier qualification. Check Ginger section specifically for the nausea RCT evidence framing (gingerol/shogaol mechanism, RCT evidence on chemotherapy-induced nausea — appropriate evidence tier vs. overclaiming).

### Without Contractor (Solo Fallback)

The solo fallback schedule in the Solo Fallback Activation section above is the operative plan. Key differences from the contractor sprint:

- No briefing call or external review on June 22
- Daily writing pace is 12 hours per week total (approximately 1.7 hours/day average, or 2.5–3 hours on 4 active writing days + 1 admin day)
- The pace gate that applied in the original sprint (Women's Health must be 2,500 words by June 24) still applies — it preserves the June 29 Women's Health upload regardless of model
- All other upload dates shift per the Solo Fallback Schedule above

**Solo fallback week-level focus and checkpoints**:

The 12 hrs/week budget is split: 9 hours writing + 2 hours admin + 1 hour monitoring (Etsy analytics, email outreach). This ratio is enforced weekly, not daily — some days will be heavier writing (3+ hours), some will be lighter (admin only). The key metric is cumulative weekly hours logged in WORKLOG.md, not daily hours.

Week 1–2 checkpoint (July 5): Women's Health uploaded June 29. Respiratory draft in progress (target: 2,500 words by July 5). If below 1,800 words by July 5, adjust Week 3 to prioritize Respiratory completion over Immunity start.

Week 3–4 checkpoint (July 19): Respiratory uploaded July 13. Sleep draft in progress (target: 2,000+ words by July 19). Immunity outline confirmed and first section drafted.

Week 5–6 checkpoint (August 2): Sleep draft near completion. Immunity writing in full velocity. If either bundle is behind by 25%+ at this checkpoint, apply scope compression to the weaker bundle (reduce the species count by one, deferring the dropped species to a post-sprint v1.1 update).

Week 7–9 closure: Immunity uploads August 17. Digestive completes September 24. At this stage the sprint is in a comfortable solo cadence — the urgency of the June 22 launch is behind, and quality per bundle matters more than pace.

---

## FAQ: Decisions That Feel Ambiguous

**Q: A candidate emerges with excellent credentials but wants $1,600 and will not negotiate. The search closes June 14. Do we hire them?**

No. The $1,500 hard ceiling exists for a specific reason: above that rate, the hybrid model economics erode relative to solo fallback. At $1,600, the contractor is costing approximately $250 more than the ceiling, which represents roughly 3 additional hours of user writing time at a reasonable time-value. The solo fallback at 12 hrs/week is a viable alternative — not a catastrophe. Do not break the ceiling for a single candidate.

**Q: We find a great candidate on June 16 — one day before the hard deadline. Should we rush to sign?**

Yes, if the candidate passes the vetting rubric (75+ score) and has confirmed June 22 availability. A June 16 contract signing gives 6 days of onboarding before sprint Day 1. This is tight but workable: deliver the briefing package June 16, hold a 30-minute phone orientation June 19, and reserve the full 1-hour briefing for June 22. Do not skip the June 22 briefing even for a late-sign contractor — the Goldenseal CITES sidebar and FTC framing must be covered in person (or by video) before writing begins.

**Q: We are in the solo fallback and a strong candidate contacts us July 1, unsolicited. Do we engage?**

No. The July 1 date is past the June 17 hard deadline. The Respiratory bundle is already in user writing as of June 22. A contractor engaged July 1 would overlap with user-written Respiratory content, create a revision conflict, and have only Immunity and Digestive to write. At that point, the contractor value is primarily time savings on 2 bundles ($700–$900 for Immunity + Digestive) vs. the onboarding cost and coordination overhead. Make this call based on the specific candidate's score and your energy state at that point in the sprint — it is a borderline case, not a clear yes or no.

**Q: The contractor delivers the Respiratory bundle with a missing Echinacea angustifolia At-Risk sidebar. What happens to the milestone payment?**

Hold Milestone 2 payment until the revision is delivered. The contract revision clause allows one revision cycle per bundle. The At-Risk sidebar is a mandatory content requirement listed in the briefing package — its absence is a contractor error, not a scope misunderstanding. Email the contractor: "The Echinacea angustifolia United Plant Savers At-Risk sidebar (approximately 150 words) is missing from the draft. This is a required section per the briefing package. Please add before we can release this milestone." If the revision is delivered within 48 hours: release payment. If not: flag as a quality signal for the remaining bundles.

---

*Prepared: June 5, 2026. Cross-references: PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md (search channels, vetting rubric), PHASE_3_CRITICAL_PATH_ANALYSIS_JUNE22_JULY13.md (bundle writing schedule, upload dates), PHASE_3_PRODUCTION_SPRINT_RISK_REGISTER.md (contractor dropout risk, Risk 1 mitigation). Version 1.0.*
