---
title: "Domain 38/40 Contingency Decision Tree — Wave 2 Escalation, Timing, and Scope Logic"
created: 2026-05-30
purpose: "Pre-built decision tree for Wave 2 execution based on Domain 39 response data at T+24h, T+72h, and T+168h gates. All thresholds are numeric and actionable. No judgment required at execution time — navigate to matching row, execute action."
primary_gate: "June 4, 2026 — Domain 39 T+72h response count"
secondary_gate: "June 8, 2026 — Domain 39 T+168h response count (if June 4 result was borderline)"
escalation_threshold: "≥5 unique contacts responding to Domain 39 by T+72h → Escalate Wave 2 scope"
planned_threshold: "2–4 unique contacts → Proceed as planned"
reduction_threshold: "<2 unique contacts → Reduce to Tier A only; hold Tier B/C in contingency"
timing_acceleration: "If Domain 39 momentum declining after June 8 → Accelerate Domain 38/40 first batch to June 15 (no wait)"
parallel_execution_trigger: "Domain 39 T+168h ≥5 contacts → Parallel execution authorized (Domain 38 June 15–20 + Domain 40 June 18–22 simultaneously active)"
co_messaging_threshold: "≥3 unique contacts receiving both Domain 39 and Domain 40 content → send joint synthesis email July 1–10"
status: execution-ready
cross_references:
  - domain-38-execution-timeline.md
  - domain-40-execution-timeline.md
  - domains-38-40-contact-stratification.md
  - DISTRIBUTION_EXECUTION_LOG.md
---

# Domain 38/40 Contingency Decision Tree
## Wave 2 Escalation, Timing, and Scope Logic — Pre-Built for June 2 Assessment

*This decision tree is fully pre-built. At each gate date, read the Domain 39 unique contact count, navigate to the matching row, and execute the listed action. No planning required. All thresholds are numeric. "Strong response" and "weak response" are not used — only specific counts.*

---

## Part 1: Gate Structure Overview

Wave 2 planning has three assessment gates. Each gate requires reading one number (Domain 39 unique contacts responding) and applying the matching action row. The gates are cumulative — each later gate either confirms or updates the action from the prior gate.

| Gate | Date | Trigger | Decision |
|---|---|---|---|
| Gate 0 | June 2, 13:00 UTC | Domain 39 T+24h | Delivery confirmation only; no scope decision |
| Gate 1 | June 4, 13:00 UTC | Domain 39 T+72h | Primary scope decision: Escalate / Planned / Reduce |
| Gate 2 | June 8, 13:00 UTC | Domain 39 T+168h | Confirm or revise Gate 1 decision; timing acceleration check |
| Gate 3 | June 15–22 | Domain 38/40 Tier A response data | Wave 2 independent escalation check |

**Important**: Gate 1 (June 4) is the primary decision gate. Gates 2 and 3 can only maintain or escalate — they do not reduce scope below what Gate 1 established (a contact already sent to cannot be "un-sent").

---

## Part 2: Gate 0 — June 2 (T+24h Delivery Confirmation)

### 2.1 What to Check at Gate 0

Domain 39 executes June 1, 13:00–14:00 UTC. T+24h = June 2, 13:00 UTC.

At Gate 0, check:
- [ ] Any bounce-back email notifications? Log any delivery failures.
- [ ] Any out-of-office replies? Note staff changes, find updated contacts.
- [ ] Any substantive responses (unexpectedly fast)? Log in DISTRIBUTION_EXECUTION_LOG.md; these count toward Gate 1.
- [ ] All 15–20 Domain 39 sends confirmed sent? (Verify against send log.)

### 2.2 Gate 0 Decision Matrix

| Condition | Action |
|---|---|
| All sends confirmed; no delivery failures | No action required. Proceed to Gate 1 (June 4). |
| 1–3 bounce-backs | Find updated contacts within 24 hours; re-send to corrected addresses before June 4 (so re-sends count at Gate 1). |
| ≥4 bounce-backs (delivery problem) | Do not wait for Gate 1. Audit contact list immediately. Run delivery self-test from send account. Note in DISTRIBUTION_EXECUTION_LOG.md as "Delivery Problem — Audit Required." This does not cancel Gate 1 — Gate 1 still runs June 4 with whatever data is available. |
| 1+ substantive responses already (within 24 hours) | Log as Score 3+ in DISTRIBUTION_EXECUTION_LOG.md. This is an early positive signal but does NOT trigger Gate 1 early. Wait for full T+72h count before scope decision. |

**Gate 0 time required**: 15 minutes.

---

## Part 3: Gate 1 — June 4, 13:00 UTC (T+72h Primary Scope Decision)

### 3.1 What to Count at Gate 1

Count **unique contacts** who responded with **Score 2 or higher** between June 1 13:00 UTC (send time) and June 4 13:00 UTC (72 hours later).

**Score definitions (use these; do not invent new classifications)**:

| Score | Description | Count toward Gate 1? |
|---|---|---|
| 5 | Contact cites the domain in published work, testimony, or public statement | Yes |
| 4 | Contact requests a follow-up call, meeting, or additional materials | Yes |
| 3 | Contact sends substantive reply engaging with content (asks a question, provides feedback, shares with a colleague) | Yes |
| 2 | Contact confirms receipt and indicates they will read or share | Yes |
| 1 | Generic acknowledgment ("thank you for sending this") with no indication of engagement | No — does not count |
| 0 | No response | No |

**Unique contacts**: If the same organization sends two replies from two staff members, count as 1 unique contact. If two different organizations each send one reply, count as 2 unique contacts.

### 3.2 Gate 1 Decision Matrix — Domain 38/40 Scope

#### Row A: ≥5 Unique Contacts (Score 2+) — ESCALATE

| Parameter | Action |
|---|---|
| **Domain 38 Tier scope** | Full: Tier A (June 15–20) + Tier B (June 21–July 10) + Tier C (July 1–15) + **Tier D immediately** (activate public channels June 15–18, parallel to Tier A sends) |
| **Domain 40 Tier scope** | Full: Tier A (June 18–22) + Tier B (June 23–July 10) + Tier C (June 23–July 20) + **Tier D immediately** (activate June 23) |
| **Joint email list** | Activate: Identify 15–20 contacts receiving both Domain 39 and Domain 40; draft joint synthesis email; send July 1–10 (see Part 6) |
| **Media outreach** | Escalate: Pitch Tier C media (TechPolicy.Press, Lawfare, Votebeat) June 15–16, parallel to Tier A sends (1 week earlier than planned baseline) |
| **Domain 38 send window** | No change: June 15–20 as planned |
| **Domain 40 send window** | No change: June 18–22 as planned |
| **Note in DISTRIBUTION_EXECUTION_LOG.md** | "Gate 1: ESCALATE. Domain 39 T+72h = [N] unique contacts (Score 2+). Full Tier scope confirmed for both domains. Tier D activated June 15." |

#### Row B: 2–4 Unique Contacts (Score 2+) — PLANNED

| Parameter | Action |
|---|---|
| **Domain 38 Tier scope** | Planned: Tier A (June 15–20) + Tier B (June 21–July 10) + Tier C (July 1–15). Tier D begins July 15–August 2. |
| **Domain 40 Tier scope** | Planned: Tier A (June 18–22) + Tier B (June 23–July 10) + Tier C (June 23–July 20). Tier D begins June 23. |
| **Joint email list** | Conditional: Activate only if any Domain 39 contacts are also in Domain 40 Tier A list (verify before June 8). If overlap exists, draft joint synthesis email; hold until both domains have Tier A sends complete (July 1 earliest). |
| **Media outreach** | Proceed as scheduled: Tier C media week of July 1–7 |
| **Domain 38 send window** | No change: June 15–20 |
| **Domain 40 send window** | No change: June 18–22 |
| **Note in DISTRIBUTION_EXECUTION_LOG.md** | "Gate 1: PLANNED. Domain 39 T+72h = [N] unique contacts (Score 2+). Planned Tier scope confirmed." |

#### Row C: <2 Unique Contacts (Score 2+) — REDUCE

| Parameter | Action |
|---|---|
| **Domain 38 Tier scope** | Reduced: **Tier A only** (June 15–20). Stage Tier B contacts in draft folder but do not send until Gate 2 (June 8) reassessment. Tier C hold. Tier D hold. |
| **Domain 40 Tier scope** | Reduced: **Tier A only** (June 18–22). Same Tier B/C/D hold. |
| **Send dates** | No change: Tier A proceeds June 15 and June 18 regardless of response count. Reduction is scope, not date. |
| **Contact quality review** | Required: Before June 15 Tier A sends begin, re-verify all 16 Domain 38 and 15 Domain 40 Tier A contacts. Confirm delivery addresses. If <2 Domain 39 replies, check whether a delivery problem is the cause (check bounce-backs, spam folder indicators). |
| **Framing review** | Required: Re-read first 3 Domain 38 and first 3 Domain 40 email templates. Verify EU enforcement hook is prominent. Verify PNAS study finding appears in first 2 sentences of Domain 40 emails. If Domain 39 emails used a weak hook (generic policy framing instead of specific deadline), revise Domain 38/40 hooks before June 15 send. |
| **Joint email list** | Hold: Do not activate joint email. Reassess at Gate 2. |
| **Note in DISTRIBUTION_EXECUTION_LOG.md** | "Gate 1: REDUCE. Domain 39 T+72h = [N] unique contacts (Score 2+). Tier A only for both domains. Tier B/C/D staged but held pending Gate 2." |

#### Row D: 0 Unique Contacts AND ≥3 Bounce-Backs (Score 2+) — DELIVERY PROBLEM

| Parameter | Action |
|---|---|
| **Immediate action** | Do not proceed to June 15 Domain 38 send until delivery audit is complete. |
| **Audit steps** | (1) Send test email from outreach account to a personal email. Confirm inbox delivery, not spam. (2) Check if Domain 39 sends were marked as spam by checking send account's spam folder. (3) Verify Domain 39 contact email addresses against original verification list. (4) Check if any contacts' organizations have changed staff or email domains since the contact list was compiled. |
| **If delivery problem confirmed** | Delay Domain 38 Tier A send by 72 hours (to June 18). Use delay window to fix delivery issue. Continue Domain 40 Tier A as scheduled (June 18 or later). |
| **If no delivery problem found (0 responses, 0 bounces)** | Proceed with Row C (REDUCE). The absence of responses is content or audience issue, not delivery failure. |
| **Note** | Row D is a special case of Row C. Apply Row C scope decisions plus the delivery audit. |

---

## Part 4: Gate 2 — June 8, 13:00 UTC (T+168h Confirmation and Timing Acceleration)

### 4.1 What to Count at Gate 2

Count unique contacts who responded with Score 2+ between June 1 13:00 UTC and June 8 13:00 UTC (168 hours = 7 days).

Gate 2 is a confirmation gate. It can only confirm or upgrade the Gate 1 decision — it cannot downgrade.

### 4.2 Gate 2 Decision Matrix

#### If Gate 1 was ESCALATE and Gate 2 response count ≥8:

**Super-escalation**: Domain 38/40 have momentum from Domain 39. Consider:
- Accelerating Tier B sends to start June 16 (overlap with Tier A completion rather than waiting until June 21)
- Expanding joint email list to 25–30 contacts (not just 15–20)
- Pitching Substack guest posts to The Markup and The Lever in June (earlier than planned)

**Timing acceleration trigger**: If any Domain 39 contact (Score 3+) has expressed interest in Domain 38 or Domain 40 content specifically, send them Domain 38 or 40 directly on June 15 (add them to Tier A batch if not already there).

#### If Gate 1 was PLANNED and Gate 2 response count ≥5:

**Upgrade to ESCALATE**: Apply all Row A (ESCALATE) actions. Tier D activates immediately. Joint email list activates. Media outreach moves to week of June 15–20.

**Note in DISTRIBUTION_EXECUTION_LOG.md**: "Gate 2 upgrade: Gate 1 was PLANNED (3 contacts), Gate 2 is ESCALATE (5 contacts). Activating Tier D and joint email list."

#### If Gate 1 was PLANNED and Gate 2 response count 2–4 (same as Gate 1):

**Confirm PLANNED**: No changes. Proceed with planned Tier scope.

#### If Gate 1 was REDUCE and Gate 2 response count ≥2:

**Upgrade to PLANNED**: Release Tier B from hold. Tier B sends begin June 21 as originally scheduled. Tier C begins July 1 as scheduled.

**Note**: This upgrade from REDUCE to PLANNED is the most common Gate 2 outcome. The 72-hour window is often too short for academic and policy organization response cycles. The 7-day window captures more responses.

#### If Gate 1 was REDUCE and Gate 2 response count <2 (still 0–1):

**Confirm REDUCE**: Tier B and Tier C remain on hold. Tier A proceeds June 15–22 as scheduled. Reassess after Domain 38/40 Gate 3 (June 22–29).

### 4.3 Timing Acceleration Decision

**Timing acceleration trigger** (independent of response count):

If Domain 39 response momentum shows the following pattern after June 8:
- Response count on June 4 (T+72h) was higher than response count would project at June 8 (T+168h) — i.e., replies concentrated in days 1–3 and tapering — this indicates momentum is declining.

**Acceleration action**: If Domain 39 momentum is declining after June 8, do not wait for Domain 39 T+168h responses to plateau. Proceed with Domain 38/40 Tier A as scheduled (June 15/18). No acceleration of send dates is needed — they are already June 15/18. "Acceleration" in this context means: do not add delays. Keep the June 15/18 dates firm.

**If Domain 39 momentum is still building after June 8** (responses still arriving at T+120h–T+168h, not just early): This is a positive signal. Proceed with planned June 15/18 dates. In the Domain 38/40 emails, note any Domain 39 organizational responses as social proof: "Our companion analysis on healthcare access as democratic infrastructure has generated interest from [organizations if publicly citable] — this analysis on AI regulatory capture extends that framework."

---

## Part 5: Gate 3 — June 22–29 (Domain 38/40 Independent Assessment)

### 5.1 Wave 2 Is Now Independent

By June 22, Domain 38 Tier A is complete and Domain 40 Tier A is complete. Wave 2 is no longer contingent on Domain 39 data — it has its own response data. Gate 3 is a Wave 2-only assessment.

**Count at Gate 3**: Unique Domain 38 Tier A contacts responding Score 2+ (by June 22). Unique Domain 40 Tier A contacts responding Score 2+ (by June 25, 72 hours after last send June 22).

### 5.2 Gate 3 Decision Matrix

#### Domain 38 Gate 3 (check June 22–25)

| Domain 38 Replies (Score 2+, T+72h) | Action |
|---|---|
| ≥4 | Escalate: Tier D activates June 23–25; media pitches June 23; Tier B begins June 21 as planned |
| 2–3 | Planned: Tier B June 21–July 10; Tier C July 1–15 |
| 1 | Monitor: Proceed with Tier B; audit first 5 email templates for framing clarity |
| 0 | Review: Check delivery; consider alternative hook (switch from EU enforcement to preemption EO); do not cancel Tier B |

#### Domain 40 Gate 3 (check June 25–29)

| Domain 40 Replies (Score 2+, T+72h from June 22 last send) | Action |
|---|---|
| ≥3 | Escalate: Full Tier D campaign begins June 23–25 (already in progress if following planned timeline); joint synthesis email draft begins July 1 |
| 1–2 | Planned: Tier B June 23–July 10; Tier C June 23–July 20 |
| 0 | Monitor: Check delivery; PNAS hook may need to be in the first sentence (move it up if currently in paragraph 2 of emails) |

#### Domain 38/40 Combined Gate 3 Check (June 25–29)

| Combined Replies (Domain 38 + Domain 40, Score 2+) | Action |
|---|---|
| ≥6 combined | Joint synthesis email: Draft and send July 1–10 (see Part 6 for content) |
| 3–5 combined | Joint email conditional: Draft July 1–10 only if ≥2 contacts are eligible for joint message (receiving both domains) |
| <3 combined | Standard: No joint email yet; proceed with individual domain follow-ups |

---

## Part 6: Domain 39 / Domain 40 Co-Messaging Logic

### 6.1 Topic Interdependency Analysis

Domain 39 (healthcare access as democratic infrastructure) and Domain 40 (surveillance capitalism and electoral manipulation) share a core co-messaging argument:

**The data pipeline**: Healthcare data flows from Medicaid enrollment records → state voter registration databases (via NVRA) → DOJ voter file collection program → commercial data broker appending → AI-generated voter suppression targeting in battleground counties.

This is not theoretical. Domain 40 Section 1.2 documents that the DOJ's voter file collection MOU requires states to share complete voter registration files including "information related to public assistance" — which includes Medicaid enrollment status. Domain 39 documents that the OBBBA creates Medicaid coverage losses, which changes enrollment status, which flows into the voter data infrastructure Domain 40 traces.

**The joint message**: "The same federal policy that reduces Medicaid enrollment also changes the voter data used to target digital suppression content. OBBBA creates the coverage loss; the DOJ voter file program collects the enrollment change; commercial data brokers append behavioral and location data; AI-generated suppression content targets the resulting population. We've documented each step in the chain."

### 6.2 Joint Email Eligibility Criteria

A contact is eligible for a joint Domain 39/40 synthesis email if **all three** of the following are true:
1. The contact has received Domain 39 (June 1 send or follow-up)
2. The contact is in the Domain 40 contact list (Tier A or Tier B)
3. The contact's work explicitly touches both healthcare data policy and electoral/voter data policy

**Pre-identified joint-eligible contacts** (15 contacts; send joint synthesis email July 1–10 if Gate 1 = ESCALATE, or July 15–20 if Gate 1 = PLANNED):

| Organization | Domain 39 Connection | Domain 40 Connection | Joint Email Window |
|---|---|---|---|
| Brennan Center — Democracy Program | NVRA enforcement; healthcare access argument | DOJ voter file MOU; FEC paralysis | July 1–5 (14+ days after both sends) |
| ACLU | Medicaid work requirements; disability voter participation | Electoral surveillance; DOJ voter file suit | July 1–5 |
| National Disability Rights Network | PAVA elimination; disability voter turnout | Disability status in commercial targeting data | July 5–10 |
| Center on Budget and Policy Priorities | Medicaid coverage losses | Medicaid enrollment in voter file data | July 10–15 |
| Democracy Docket | NVRA litigation (if Domain 39 follow-up sent) | DOJ voter file cases; election litigation | July 1–5 |
| Protect Democracy | Healthcare democracy framing | Deepfake electoral deployment | July 5–10 |
| EFF | Healthcare data privacy | Surveillance capitalism and digital rights | July 5–10 |
| Georgetown Center for Children and Families | CHIP/children's Medicaid | Children's data in commercial surveillance pipeline | July 10–15 |
| Voting Rights Lab | NVRA state-level enforcement | State election administration; voter file governance | July 5–10 |
| Common Cause | Healthcare access and voter participation | Election protection and data broker targeting | July 5–10 |
| Institute for Responsive Government | NVRA under-enforcement | Not currently in Domain 40 list; add as Tier B | July 10–15 |
| National Health Law Program | Medicaid litigation | Healthcare data in voter file collection | July 15 |
| Georgetown CCF | Domain 39 Tier 1 contact | Healthcare data privacy | July 15 |
| CBPP | Healthcare policy | OBBBA/voter file data intersection | July 15 |
| KFF | Healthcare research | Healthcare data in voter suppression analysis | July 15 |

### 6.3 Joint Synthesis Email Template

**Subject line**: "Healthcare data to voter suppression: the complete pipeline — connecting Domain 39 and Domain 40"

**Opening paragraph**: "The February 2026 PNAS study found targeted digital voter suppression ads reduced turnout 1.86% in exposed populations, with non-white voters in minority-majority battleground counties receiving these ads at 4x the rate of white voters. What we didn't send you in the Domain 39 email on June 1 is what connects your healthcare advocacy work to that study: Medicaid enrollment status flows into the voter data infrastructure that fuels this targeting."

**Second paragraph**: Describe the three-step data pipeline (OBBBA → NVRA enrollment → DOJ voter file collection → commercial data broker appending → AI suppression targeting). Cite Domain 39 Section 5 (healthcare democracy argument) and Domain 40 Section 1.2 (DOJ voter file MOU).

**Third paragraph**: "We've documented each step of the chain in two analyses — Domain 39 (healthcare access as democratic infrastructure) and Domain 40 (surveillance capitalism and electoral manipulation). Both are available at [Domain 39 Gist URL] and [Domain 40 Gist URL]. If there is a specific part of this pipeline your organization is already working on, we'd welcome a conversation about where the research can be most useful."

**Closing**: Gist URLs for both domains. No additional ask beyond reading/sharing.

---

## Part 7: Domain 38/40 Timing Interdependency Rules

### 7.1 Mandatory Stagger Rules (Do Not Override)

These stagger rules are mandatory. Violating them risks contact fatigue and inbox flooding at organizations receiving multiple sends in the same week.

| Contact | Domain 38 Send | Domain 40 Send | Minimum Gap | Maximum Risk if Violated |
|---|---|---|---|---|
| Brennan Center | June 17 (Domain 38) | June 18 (Domain 40) | 24 hours | Medium: different teams; different hooks; 1-day gap is manageable |
| Protect Democracy | June 15 (Domain 38) | June 19 (Domain 40) | 3 days | Medium: same contact form; different subject lines; 4-day gap is acceptable |
| ACLU | June 19 (Domain 38) | June 22 (Domain 40) | 3 days | Medium: different framing; 3-day gap acceptable |
| EFF | June 15 (Domain 38, Tier A) | June 23 (Domain 40, Tier B) | 7 days | Low: EFF receives high-volume policy outreach; 8-day gap creates clean separation |

**Exception rule**: If any of the above contacts responds to Domain 38 with Score 3+ within 48 hours of the Domain 38 send, you may accelerate Domain 40 send to the same contact — but only if the Domain 40 email is explicitly framed as a follow-up: "Following up on my email about AI regulatory capture — the related analysis on electoral implications of the same regulatory vacuum is at [Domain 40 Gist URL]." This converts the potential overlap into an explicit cross-domain connection.

### 7.2 Sequential vs. Parallel Execution Decision

The task brief asks whether Domain 38 and Domain 40 should run sequentially or in parallel, and recommends staggered starts (Domain 38 June 15, Domain 40 June 18–20).

**Recommendation: Parallel with 3-day stagger**. The stagger is the execution plan. Parallel execution is defined as both Tier A sequences being active simultaneously (Domain 38 running June 15–20; Domain 40 running June 18–22; overlap June 18–20). This is not a conflict — it requires approximately 30 additional minutes per day on overlap days (sending 2 batches instead of 1).

**Sequential execution** (Domain 40 starts only after Domain 38 completes June 20) is only warranted if:
- Capacity is genuinely limited to single domain per week (e.g., sender can only manage 3 emails per day, not 5–6)
- A technical delivery problem is detected with Domain 38 sends that requires resolution before Domain 40 begins

In all other cases, parallel execution with staggered starts is the correct approach. It creates maximum November 3 lead time for Domain 40 while maintaining contact fatigue protection for shared organizations.

---

## Part 8: Full Decision Tree Quick Reference

### 8.1 Complete Decision Tree — All Gates

```
DOMAIN 39 EXECUTES JUNE 1, 13:00 UTC
         |
         v
GATE 0 — JUNE 2, 13:00 UTC (T+24h)
         |
   Delivery check only — no scope decision
         |
         v
GATE 1 — JUNE 4, 13:00 UTC (T+72h)
         |
         +----- N ≥ 5 unique contacts -----> ESCALATE (Row A)
         |                                   Full Tier scope + Tier D immediate
         |                                   Joint email list activated
         |                                   Media outreach June 15–16
         |
         +----- N = 2,3,4 contacts --------> PLANNED (Row B)
         |                                   Tier A + B + C as scheduled
         |                                   Tier D June 23 (Domain 40), July 15 (Domain 38)
         |                                   Joint email conditional on overlap check
         |
         +----- N = 0,1 contacts ----------> REDUCE (Row C)
                                             Tier A only
                                             Tier B/C staged but held
                                             Contact quality review required
                                             Gate 2 reassessment June 8
                                             |
GATE 2 — JUNE 8, 13:00 UTC (T+168h)         |
         |                                   |
         +----- If REDUCE at Gate 1:         |
         |      N ≥ 2 by June 8 -----------> Upgrade to PLANNED
         |      N < 2 by June 8 -----------> Confirm REDUCE; Tier A only
         |
         +----- If PLANNED at Gate 1:
         |      N ≥ 5 by June 8 -----------> Upgrade to ESCALATE
         |      N = 2–4 by June 8 ---------> Confirm PLANNED
         |
         +----- If ESCALATE at Gate 1:
                N ≥ 8 by June 8 -----------> Super-escalate: Tier B start June 16
                N ≥ 5 by June 8 -----------> Confirm ESCALATE
                                             |
DOMAIN 38 TIER A — JUNE 15–20               |
DOMAIN 40 TIER A — JUNE 18–22               |
         |                                   |
GATE 3 — JUNE 22–29 (WAVE 2 INDEPENDENT)    |
         |
   Count Domain 38 replies (≥4: escalate; 2–3: planned; 1: monitor; 0: review)
   Count Domain 40 replies (≥3: escalate; 1–2: planned; 0: monitor)
   Count combined (≥6: joint email July 1–10; 3–5: joint email conditional; <3: no joint email)
```

### 8.2 Actions by Outcome

#### ESCALATE Action List (complete by June 15)
- [ ] Tier D activated: Reddit posts June 15 (Domain 38) and June 23 (Domain 40) — both use EU enforcement hook
- [ ] Media pitches staged: TechPolicy.Press (June 15), Votebeat (June 23)
- [ ] Joint email list verified: Identify all 15 pre-identified joint-eligible contacts; draft joint synthesis email (see Part 6.3); send July 1–10
- [ ] Social proof language added to Tier B emails: "Domain 39 healthcare analysis has generated interest from [org if citable]"
- [ ] Domain 38 Tier B send window moved up to June 21 (no change — already the planned date)
- [ ] Domain 40 Tier B send window confirmed June 23 (no change)

#### PLANNED Action List (complete by June 15)
- [ ] Verify all 16 Domain 38 and 15 Domain 40 Tier A email templates are pre-filled with Gist URLs
- [ ] Confirm June 15 Domain 38 first batch is staged in draft folder
- [ ] Confirm June 18 Domain 40 first batch is staged in draft folder
- [ ] Log "Gate 1: PLANNED" in DISTRIBUTION_EXECUTION_LOG.md
- [ ] Set calendar reminder for Gate 3 (June 22–29)

#### REDUCE Action List (complete by June 14)
- [ ] Re-verify all Tier A contact addresses (complete by June 12)
- [ ] Review and revise email templates if Domain 39 framing review suggests hook weakness
- [ ] Stage Tier B contacts in draft folder labeled "HOLD — pending Gate 2"
- [ ] Log "Gate 1: REDUCE" in DISTRIBUTION_EXECUTION_LOG.md
- [ ] Set calendar reminder for Gate 2 (June 8) reassessment
- [ ] Proceed with Tier A sends June 15/18 as planned (scope reduction does not affect send date)

---

## Part 9: Response Logging Protocol

All responses to Domain 38 and Domain 40 outreach must be logged within 24 hours of receipt in DISTRIBUTION_EXECUTION_LOG.md. The log entry format:

```
Date received: [UTC timestamp]
Domain: [38 or 40]
Contact: [Name, Organization]
Score: [1–5]
Summary: [1–2 sentence description of response content]
Follow-up required: [Yes/No — if Yes, deadline and action]
Counted toward Gate [1/2/3]: [Yes/No]
```

Responses that arrive after Gate 1 (June 4) still count toward Gate 2 (June 8) and Gate 3 (June 22–29). No response data is discarded. Log everything.

---

*Contingency decision tree created May 30, 2026. All thresholds are numeric. All actions are specific. No judgment required at execution time beyond reading the response count and navigating to the matching row. Cross-references: domain-38-execution-timeline.md, domain-40-execution-timeline.md, domains-38-40-contact-stratification.md, DISTRIBUTION_EXECUTION_LOG.md.*
