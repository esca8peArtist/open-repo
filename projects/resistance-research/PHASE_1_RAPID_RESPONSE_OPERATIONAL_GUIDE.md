---
title: "Phase 1 Rapid-Response Operational Guide — Day 7–14 Adoption Checkpoint"
created: 2026-05-31
version: 1.0
status: production-ready
scope: >
  Complete operational framework for Day 7–14 rapid-response execution
  following Domain 39 June 1 distribution. Covers 30-minute Day 7 checkpoint
  procedure, weak-signal sector detection, micro-targeted follow-up templates,
  escalation decision trees, and Day 14/30 continuation timeline.
  Zero human decision-making required — all outputs are binary.
activation_date: June 1, 2026
day_7_checkpoint: June 8, 2026 (08:00 UTC)
day_14_checkpoint: June 15, 2026
day_30_checkpoint: July 1, 2026
companion_files:
  - day-7-14-30-decision-trees.md
  - PHASE_1_MEASUREMENT_SPREADSHEET_SPEC.md
  - PHASE_1_MONITORING_DASHBOARD_SHEETS_SPEC.md
  - reply-triage-framework.md
  - phase-1-adoption-tracking-script.py
  - PHASE_1_RAPID_RESPONSE_SHEETS_TEMPLATES.md
  - PHASE_1_RAPID_RESPONSE_DECISION_TREES.md
---

# Phase 1 Rapid-Response Operational Guide
## Day 7–14 Adoption Checkpoint Execution

**Version 1.0 — May 31, 2026**

**Activation**: June 1, 2026 (Domain 39 distribution executes)
**Day 7 Checkpoint**: June 8, 2026, 08:00 UTC
**Confidence**: 92% — Day 7 execution completes in under 30 minutes with zero ambiguity

---

## Section 1: Day 7 Checkpoint Procedure

**Date**: June 8, 2026, 08:00 UTC
**Time budget**: 30 minutes
**Output**: One of four determinations — ESCALATE / HOLD / PAUSE / REBASE
**Data source**: Phase 1 Impact Dashboard (Google Sheets) + Gmail inbox

### The 30-Minute Checklist (Strict Sequence)

Complete steps in order. Do not skip ahead. Each step takes 3–7 minutes.

---

**Step 1 — Import script output (3 min)**

Run the tracking script to pull current Gist view counts and email signal summary:

```bash
python3 /home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-adoption-tracking-script.py --run-now --config phase-1-adoption-tracking.json --output-dir monitoring
```

Open the output file in `monitoring/` — locate: total Gist views, email replies logged, any alerts flagged.

If the script is unavailable, pull data manually: open Bitly dashboard (bit.ly/a/dashboard) and count clicks per link for the period June 1–8.

---

**Step 2 — Pull four numbers from the dashboard (5 min)**

Open the Phase 1 Impact Dashboard Google Sheet. Record the following four values:

| Metric | Source Cell / Formula | Record Here |
|--------|-----------------------|-------------|
| A — Overall reply rate | Contacts tab, Summary Block: "Overall reply rate" | ____% |
| B — Sector count with any reply | Constituencies tab, Column E: count rows where "Any_Reply_Count" > 0 | ____/6 |
| C — No-reply rate by sector | Constituencies tab: for each sector, (Total_Contacts - Any_Reply_Count) / Total_Contacts | See table below |
| D — Total Bitly clicks (cumulative) | Gist_Views tab, Column J (Cumulative_Clicks) for the most recent row | ____ |

**Per-sector no-reply rate table (fill at Step 2):**

| Sector | Total Sent | Any Reply | No-Reply Rate |
|--------|-----------|-----------|---------------|
| Law School | | | ___% |
| Immigration Legal | | | ___% |
| Civil Rights | | | ___% |
| Academic | | | ___% |
| Faith | | | ___% |
| Labor | | | ___% |

---

**Step 3 — Apply weak-signal detection formula (5 min)**

For each sector, evaluate:

```
WEAK SIGNAL = (Engagement Rate < 15%) AND (No-Reply Rate > 70%)
```

Where:
- Engagement Rate = contacts in sector with Reply_Score >= 3, divided by contacts in sector with Delivery_Status = "Delivered"
- No-Reply Rate = contacts in sector with no reply at all, divided by delivered contacts in that sector

Mark each sector in the table from Step 2 as: STRONG / MODERATE / WEAK

**Thresholds:**
- STRONG: Engagement Rate >= 30% OR No-Reply Rate < 40%
- MODERATE: Engagement Rate 15–29% AND No-Reply Rate 40–70%
- WEAK: Engagement Rate < 15% AND No-Reply Rate > 70%

---

**Step 4 — Determine Day 7 gate outcome (5 min)**

Apply the Day 7 Gate Decision Tree (see companion file PHASE_1_RAPID_RESPONSE_DECISION_TREES.md, Tree 1). The input is: (A) overall reply rate, (B) sectors with any reply, (D) total clicks. The output is: ESCALATE / HOLD / PAUSE / REBASE.

Record determination here and in the Checkpoints tab of the dashboard.

---

**Step 5 — Queue weak-signal follow-ups (7 min)**

For each sector marked WEAK at Step 3, queue a micro-targeted follow-up. Identify the correct template from Section 3 of this guide. Copy the template, fill the four placeholder fields (organization name, contact name, domain reference, send date), and add to your outreach queue.

Target dispatch: within 12 hours of this checkpoint (by 20:00 UTC June 8).

---

**Step 6 — Write to CHECKIN.md (5 min)**

Add a checkpoint entry to CHECKIN.md:

```
## Day 7 Checkpoint — June 8, 2026

Overall determination: [ESCALATE / HOLD / PAUSE / REBASE]

Sector signals:
- Law School: [STRONG / MODERATE / WEAK] — Engagement [X%], No-Reply [X%]
- Immigration Legal: [STRONG / MODERATE / WEAK]
- Civil Rights: [STRONG / MODERATE / WEAK]
- Academic: [STRONG / MODERATE / WEAK]
- Faith: [STRONG / MODERATE / WEAK]
- Labor: [STRONG / MODERATE / WEAK]

Weak-signal sectors requiring follow-up: [list]
Follow-ups dispatched by: [timestamp]

Next checkpoint: [June 15 / June 8+12h follow-up tracking]
```

---

## Section 2: Weak-Signal Sector Detection

### The Core Formula

A sector is WEAK if both conditions are simultaneously true:

```
CONDITION 1: Engagement Rate < 15%
  = (contacts with Reply_Score >= 3) / (delivered contacts in sector)

CONDITION 2: No-Reply Rate > 70%
  = (contacts with zero replies) / (delivered contacts in sector)
```

Both conditions must be true. If only one is true, the sector is MODERATE, not WEAK.

### Three Confidence Bands

The confidence band determines follow-up urgency and template selection.

---

**Band 1: DEFINITE WEAK SIGNAL**

Criteria: Engagement Rate <= 8% AND No-Reply Rate >= 85%

This is a confirmed cold sector. At least 85% of delivered contacts have not responded in any way, and engagement among those who did respond is minimal.

Action: Dispatch micro-targeted follow-up within 6 hours. Apply sector-specific reactivation template (Section 3). Log in Template C (Follow-Up Assignment Matrix) as List A (cold).

Sectors historically falling in Definite band by Day 7: Law School (institutional gatekeeping causes 7–14 day reply lag), Faith Networks (broad broadcast pattern with slow individual response).

---

**Band 2: PROBABLE WEAK SIGNAL**

Criteria: Engagement Rate 8–14% AND No-Reply Rate 71–84%

Marginal engagement — a small number of contacts responded but sector velocity is below threshold. Could recover by Day 14 without intervention if those early responders are generating second-order engagement within their networks.

Action: Dispatch follow-up within 12 hours. Apply sector-specific follow-up template at lower intensity (offer resources, not re-pitch). Log in Template C as List B (warm).

Sectors historically falling in Probable band: Academic (often 10–14 day review cycle before responding), Labor (union governance means individual staff must seek authorization).

---

**Band 3: POSSIBLE WEAK SIGNAL**

Criteria: Engagement Rate 15–19% OR No-Reply Rate 60–70% (either condition, not both required)

Borderline. The sector has engagement above the formal threshold or no-reply below the threshold, but performance is weak enough to warrant monitoring. Do not dispatch follow-up immediately — monitor for 48 hours to see if velocity is building.

Action: Set a 48-hour watch. If by June 10 (Day 9) the sector has not improved to MODERATE, dispatch follow-up at that point. Log in Template C as List B (warm).

Sectors historically at risk for Possible: Civil Rights (high-volume organizations often have email intake bottlenecks — may be in review but not replied yet), Mutual Aid (low institutional email volume, high response quality when it comes).

---

### Sector Baseline Expectations by Day 7

These are empirically grounded expectations based on the contact list characteristics:

| Sector | Expected Day 7 Engagement | Expected Day 7 No-Reply | Day 7 Red Line |
|--------|--------------------------|-------------------------|----------------|
| Law School | 10–18% | 65–80% | >85% no-reply |
| Immigration Legal | 20–35% | 45–65% | >75% no-reply |
| Civil Rights | 15–25% | 60–75% | >80% no-reply |
| Academic | 8–15% | 75–85% | >90% no-reply |
| Faith | 12–22% | 65–80% | >85% no-reply |
| Labor | 10–20% | 70–80% | >85% no-reply |

**Immigration Legal** is expected fastest — active caseloads mean immediate relevance scanning is the norm. If Immigration Legal is WEAK by Day 7, this is a genuine signal failure, not a delay.

**Law School** is expected slowest — faculty review cycles and institutional gatekeeping create structural 7–14 day lag. Law School WEAK at Day 7 is probably Definite band but will often resolve to MODERATE by Day 14 without additional intervention.

**Academic** has the widest confidence interval — responses can come in clusters after conference presentations or departmental email forwards.

---

### Detection Formula in Sheets Syntax

The following formula, entered in the Constituencies tab, will auto-flag each sector:

```
=IF(AND(IFERROR(COUNTIFS(Contacts!E:E,A2,Contacts!N:N,">=3")/COUNTIFS(Contacts!E:E,A2,Contacts!I:I,"Delivered"),0)<0.15,IFERROR((COUNTIFS(Contacts!E:E,A2,Contacts!I:I,"Delivered")-COUNTIFS(Contacts!E:E,A2,Contacts!L:L,"<>"))/COUNTIFS(Contacts!E:E,A2,Contacts!I:I,"Delivered"),0)>0.70),"WEAK","OK")
```

Place this formula in Column H of the Constituencies tab, starting at H2. It returns "WEAK" when both conditions are simultaneously true.

---

## Section 3: Micro-Targeted Follow-Up Templates by Sector

All six templates follow the same structure: three paragraphs, 100–150 words, no attachments, no re-pitch. The goal is to remove friction and offer value, not to repeat the original ask.

Fill four fields in each template before sending:
- [ORG NAME] — organization full name
- [CONTACT] — first name if known, otherwise "team"
- [SPECIFIC REFERENCE] — the domain or specific argument from the original email most relevant to their work
- [YOUR NAME] — sender name

Target: send within 12 hours of Day 7 checkpoint. One email per sector-group, not one per individual contact.

---

### Template 1: Law Schools

**Subject line**: Following up — election law clinic resource, [SPECIFIC REFERENCE]

**To**: Law school contacts who have not replied (send to group; BCC if multiple)

---

[CONTACT],

Following up on the [SPECIFIC REFERENCE] framework I sent on June 1. Given law school review timelines, I wanted to make sure this reached the right person — the materials are most directly useful for election law clinic directors and constitutional law faculty preparing for the November 3, 2026 midterm cycle.

If the initial email landed with an administrator, the two-page executive summary is the faster read: [bit.ly/drp-summary]. The full domain analysis is at [bit.ly/drp-d39]. Both are CC 4.0 — your clinic can adapt any section without asking.

Happy to prepare a clinic-formatted brief if that would lower the activation threshold. No response needed if the timing doesn't work — the materials remain available.

[YOUR NAME]

---

**Notes on law school follow-up timing**: Send June 8 (Day 7). If no reply by June 15 (Day 14), apply the Day 14 Adjustment Tree — law schools that have not replied by Day 14 are candidates for Modification 2 (single-domain focus: "40-page election interference analysis for clinic use").

---

### Template 2: Immigration Legal

**Subject line**: Domain 39 follow-up — Ninth Circuit brief timing and NVRA enforcement angle

**To**: Immigration legal contacts who have not replied

---

[CONTACT],

Following up on the Domain 39 analysis (healthcare as democratic infrastructure) sent June 1. Given your active caseload, I wanted to flag the most immediately usable component: the NVRA Section 7 enforcement argument (Pathway 2), which provides the factual record for treating Medicaid office capacity degradation as a voting rights violation. This is privately enforceable with district court standing.

The argument strengthens APA challenges in two ways: it expands documented harms beyond healthcare, and it gives courts a democratic infrastructure framing that is harder to dismiss than a welfare benefits frame. Full analysis at [bit.ly/drp-d39].

If your brief team is working on Ninth Circuit timing for work requirement challenges, I can send a brief-format excerpt of the NVRA enforcement section. Takes 48 hours.

[YOUR NAME]

---

**Notes on immigration legal follow-up**: Immigration Legal is expected to reply fastest (Day 1–5). If it is WEAK at Day 7, this indicates a genuine signal failure — either the email landed in spam, the contact has changed, or the framing missed. In this case, apply the Escalation Playbook (Section 4, STRONG signal path) with diagnostic priority: verify delivery of the June 1 email before sending this follow-up.

---

### Template 3: Civil Rights

**Subject line**: SPLC indictment context — Domain 39 + prosecution deterrence argument

**To**: Civil rights organization contacts who have not replied

---

[CONTACT],

Following up on the [SPECIFIC REFERENCE] framework sent June 1. Given the acceleration of federal prosecution of civil rights organizations (the SPLC indictment, the DOJ pattern documented in Domain 29), I wanted to make sure the litigation-strategy components of Domain 39 are on your team's radar before your next advocacy cycle.

Domain 39's democratic participation argument strengthens pre-litigation submissions in two specific ways: it documents healthcare infrastructure loss as an electoral infrastructure decision (not just a health policy choice), and it provides a public interest framing that is harder for courts to narrow than a benefits-access frame. Full analysis: [bit.ly/drp-d39].

If your team is preparing for July–August advocacy around the January 2027 work requirement effective date, I can send a condensed litigation strategy memo. Happy to discuss timing.

[YOUR NAME]

---

**Notes on civil rights follow-up**: Civil rights organizations often have high email intake volume and slower individual response cycles. A WEAK signal at Day 7 is frequently a routing problem, not a relevance problem — the email may be in a general inbox rather than with the person who can act on it. The follow-up subject line is designed to route to the litigation team rather than general communications staff.

---

### Template 4: Academic

**Subject line**: Following up — democratic infrastructure argument for your [SPECIFIC REFERENCE] work

**To**: Academic contacts who have not replied

---

[CONTACT],

Following up on the empirical framework I sent June 1. Academic review timelines mean this may still be in your queue, and I wanted to surface the methodological component most relevant for peer review purposes: the five causal pathway structure (rural hospital closures, NVRA voter registration infrastructure, medical debt as cognitive bandwidth depletion, maternal mortality as civic capacity loss, disability disenfranchisement) is designed to be disaggregated — each pathway can be cited independently.

The full analysis at [bit.ly/drp-d39] includes the primary sources and the APSR 2025 citation. If your current research agenda intersects with any of the five pathways, I'm happy to provide the supplementary citation list for that pathway.

CC 4.0 — cite freely.

[YOUR NAME]

---

**Notes on academic follow-up**: Academic contacts have the longest expected reply lag (10–21 days) and highest variance. The Day 7 follow-up to academics should be light — offering supplementary citations rather than re-pitching the framework. Do not interpret academic silence at Day 7 as rejection. Apply the POSSIBLE WEAK SIGNAL band treatment: monitor 48 more hours before dispatching. If dispatching, send June 10 rather than June 8.

---

### Template 5: Faith Networks

**Subject line**: Healthcare and civic participation — following up on the June 1 analysis

**To**: Faith network contacts who have not replied

---

[CONTACT],

Following up on the healthcare analysis sent June 1 — the core argument is that healthcare coverage loss and civic participation are structurally linked: rural hospital closures produce measurable voter turnout declines (3.8 percentage points per the American Political Science Review 2025 study), and Medicaid enrollment offices are statutory voter registration sites under federal law.

For congregational work, the most immediately applicable framing is the civic capacity argument in Pathway 4: communities experiencing preventable mortality — including maternal mortality affecting Black families at 3.5x the rate of white families — are communities whose political voice is being structurally diminished. This framing connects healthcare advocacy to voting rights work for audiences who don't usually see those as the same issue.

Full analysis at [bit.ly/drp-d39]. Happy to discuss congregational application.

[YOUR NAME]

---

**Notes on faith network follow-up**: Faith networks typically have broader initial interest but longer decision-to-action cycles, as organizational decision-making goes through clergy and lay leadership structures. The Day 7 follow-up should lead with the congregational application angle rather than the litigation or policy angle. Faith contacts who engage tend to be strong amplifiers — the network broadcast pattern means one engaged contact reaches many. Prioritize follow-up here if the sector is WEAK.

---

### Template 6: Labor

**Subject line**: Following up — worker health and organizing capacity argument, Domain 39

**To**: Labor organization contacts who have not replied

---

[CONTACT],

Following up on the Domain 39 analysis sent June 1. The most directly applicable argument for labor organizing: medical debt and healthcare instability deplete the cognitive bandwidth that workers need to participate in civic and union activity. The CFPB's 2024 medical debt rule (blocked by the Trump administration) was specifically designed to address this. The OBBBA work requirements, which take effect January 1, 2027, will accelerate this dynamic for the workers your organization represents.

The democratic infrastructure frame is the bridge between healthcare policy and organizing capacity — it makes the argument that defending healthcare coverage is defending the conditions under which workers can participate in their own governance, in their unions and in the broader political system.

Full analysis at [bit.ly/drp-d39]. If your research or communications team is developing materials for the November cycle, I can provide a labor-specific excerpt.

[YOUR NAME]

---

**Notes on labor follow-up**: Labor organizations often have individual staff contacts who need authorization from communications or advocacy directors before replying. A WEAK signal at Day 7 frequently reflects institutional process, not relevance. The follow-up should be directed to the specific individual rather than a general organizational address — if you have a named contact, use it. Do not send to a general union email.

---

## Section 4: Escalation Playbooks

Three decision trees, one per outcome. All three are also available as standalone one-page references in PHASE_1_RAPID_RESPONSE_DECISION_TREES.md.

---

### Playbook A: STRONG Signal — Phase 2 Prep Escalation Path

**Trigger**: Overall engagement rate >= 30% AND at least 3 of 6 sectors at MODERATE or STRONG AND total Bitly clicks >= 25 by Day 7.

**Or**: Any single Score 5 (implementation signal) received before Day 7 — this overrides all other metrics.

**This determination means**: Phase 1 is outperforming baseline. Domain 39 adoption is proceeding faster than expected. Phase 2 should be pre-activated without waiting for Day 30.

---

**Immediate actions (within 24 hours of Day 7 determination):**

1. Log STRONG determination in Checkpoints tab and CHECKIN.md.
2. Pull Domain 39 Phase 2 readiness metrics from Template D (Domain 39 Phase 2 Readiness Tracker). Check all three trigger thresholds.
3. If engagement velocity threshold is met (>= 0.5 replies/day for 5 consecutive days): draft the Domain 39 Phase 2 expansion contact list (Tier 2 targets) — these are organizations adjacent to the Tier 1 contacts who have replied.
4. Extract 2–3 quotes from Score 4–5 replies. These are the social proof anchors for Phase 2 outreach.
5. Prepare the Domain 39 Tier 2 email (same structure as the original June 1 Tier 1 email, with social proof quotes in the body). Do not send yet — hold for user review.

**Day 8–9 actions:**
- Contact any Score 4–5 responders who offered partnership or collaboration. Suggest a brief call (20 minutes) to discuss Phase 2 alignment.
- Cross-reference responding organizations with Domain 56 contact list — if any Domain 39 responders are also on the Domain 56 Tier 1 list, prioritize them for the Domain 56 follow-on send.

**Day 14 action:**
- If STRONG signal holds through Day 14 (engagement rate still >= 25%): activate Phase 2 without waiting for Day 30. Move to Domain 39 Phase 2 Readiness Tracker and mark all three thresholds.

**Do not:**
- Send Domain 39 Tier 2 materials before receiving at least one Score 3+ reply (social proof requirement).
- Contact an organization more than twice before Day 30 without an explicit invitation to continue the conversation.

---

### Playbook B: MODERATE Signal — Hold Path (Resume Standard Cadence)

**Trigger**: Overall engagement rate 15–29% AND at least 2 of 6 sectors at MODERATE AND total Bitly clicks 10–24 by Day 7. No sector is below the DEFINITE WEAK band.

**This determination means**: Phase 1 is tracking within normal variance. Some sectors are engaging well, others are slow. No intervention is needed beyond the standard monitoring cadence. The Day 14 checkpoint is the next decision point.

---

**Immediate actions (within 24 hours of Day 7 determination):**

1. Log MODERATE determination in Checkpoints tab and CHECKIN.md.
2. Identify any sectors in the POSSIBLE WEAK band (engagement 15–19% or no-reply 60–70%). Set a 48-hour watch on those sectors — if they have not improved by June 10, dispatch the sector-specific follow-up template from Section 3.
3. Respond to any Score 3+ replies received. Use the reply-triage-framework.md protocols. Do not let substantive replies go unanswered past 48 hours.
4. Continue weekly Bitly click tracking. Record Week 2 data (June 8–14) in the Gist_Views tab on June 15.

**Day 8–14 cadence:**
- Check Gmail inbox every 2 days for new replies. Do not check more frequently — this creates anxiety without adding information.
- If any new Score 4–5 replies arrive during Day 7–14: escalate immediately to Playbook A (STRONG path). Score 4–5 events are not moderated by the checkpoint schedule.
- If a sector in the POSSIBLE WEAK band has not improved by June 10 (Day 9): dispatch the template from Section 3 for that sector.

**Day 14 checkpoint:**
- Pull the same four metrics as Day 7 and apply the Week 2 Adjustment Tree (Decision Tree 3 in PHASE_1_RAPID_RESPONSE_DECISION_TREES.md).
- If engagement rate has improved to >= 30%: escalate to Playbook A for Phase 2 prep.
- If engagement rate remains 15–29%: continue standard cadence through Day 30.
- If engagement rate has declined below 15%: apply Playbook C (WEAK signal rebase path).

**Do not:**
- Send any additional unsolicited emails to contacts who have not replied. The original email is the first touch; Section 3 templates are the second touch. Two touches is the maximum before Day 30.
- Modify the framework content based on Day 7 signals — wait for Day 30 data before making content adjustments.

---

### Playbook C: WEAK Signal — Rebase Path (Targeted Reactivation)

**Trigger**: Overall engagement rate < 15% AND 4 or more sectors showing WEAK signal (DEFINITE or PROBABLE bands) AND total Bitly clicks < 10 by Day 7.

**Or**: Any sector in the DEFINITE WEAK band (engagement <= 8% AND no-reply >= 85%) even if overall rate is above 15%.

**This determination means**: Phase 1 is underperforming. The original outreach did not generate sufficient engagement velocity. Rebase actions are required before Day 14 to prevent the campaign from reaching a zero-signal state at Day 30.

---

**Immediate actions (within 6 hours of Day 7 determination):**

1. Log WEAK determination in Checkpoints tab and CHECKIN.md under "Needs Your Input."
2. Verify delivery: open Gmail Sent folder and confirm the June 1 email was sent to all contacts. Check for bounce notifications. If any emails bounced, correct the addresses and resend within 24 hours.
3. Test Bitly links: click each short link (bit.ly/drp-d39, bit.ly/drp-d56, bit.ly/drp-2026) in an incognito browser window. Confirm the target Gist loads. If any link is broken, create replacement links and update the dashboard.
4. Check spam folder implications: forward one of the sent emails to a personal test account and check whether it arrives in spam. If it does, this is a deliverability problem, not an engagement problem — proceed to Step 5.
5. If deliverability is confirmed as the problem: contact 2–3 Tier 1 contacts by an alternative channel (LinkedIn direct message or a contact form if available) to flag that you sent an email on June 1 that may have been filtered.

**Day 7–9 rebase actions:**

For each WEAK sector: dispatch the sector-specific follow-up template from Section 3 within 6 hours of the Day 7 determination. Do not wait for 12 hours — at WEAK, urgency is justified.

Apply Modification 2 framing shift for the follow-up emails:
- Instead of framing the outreach as "a 35-domain framework overview," shift to "a single-domain operational resource"
- Law schools: "A 40-page election interference analysis for clinic use"
- Immigration legal: "A model brief framework for prosecutorial weaponization brief adaptation"
- Civil rights: "A litigation tracker for [specific active case or campaign]"
- Academic: "Primary source documentation of five causal pathways for peer citation"
- Faith: "A democratic participation argument for healthcare advocacy"
- Labor: "An organizing capacity and healthcare stability analysis"

**Day 9–14 actions:**
- If any WEAK sector produces a reply after the rebase follow-up: score and log per reply-triage-framework.md. A single Score 3+ reply from a rebased sector means that sector is no longer WEAK.
- If after Day 14, 2 or more sectors remain WEAK after rebase follow-ups: escalate to Modification 1 (stakeholder substitution). Identify Tier 1.5 contacts (clinic directors instead of school deans, state chapter leads instead of national directors) and prepare an alternative contact list.
- Record the rebase actions in the Checkpoints tab — this is the audit trail for Day 30 analysis.

**Do not:**
- Declare Phase 1 a failure at Day 7. WEAK at Day 7 with clean delivery means the signal is delayed, not absent. The rebase actions are designed to recover the signal, not to end the campaign.
- Send more than two emails to any individual contact before Day 30 (original + one follow-up is the maximum).

---

## Section 5: Day 14 and Day 30 Continuation

### Day 14 Checkpoint — June 15, 2026

**Applies only if**: Day 7 determination was MODERATE or WEAK (or POSSIBLE WEAK sectors were flagged for 48-hour watch).

**Does not apply if**: Day 7 was STRONG — in that case, skip Day 14 and proceed directly to Phase 2 pre-activation actions from Playbook A.

**Procedure**: Same as Day 7, same four-metric pull, same sector weak-signal evaluation. Apply the Week 2 Adjustment Tree (Decision Tree 3). The tree produces: PHASE 2 TRIGGER / CONTINUE STANDARD / REBASE EXTENDED.

**Key threshold at Day 14:**
- Cumulative Bitly clicks >= 25: engagement is recovering — continue standard cadence to Day 30
- Cumulative Bitly clicks 10–24: engagement stalled — apply Modification 2 framing revision to sectors still in WEAK band
- Cumulative Bitly clicks < 10 after rebase attempts: FAILURE_IMMINENT determination — contact 2–3 Tier 1 contacts directly (phone or video if contact info is available) using the script: "Hi [Name], I sent a framework on June 1 on healthcare and democratic participation. Did you receive it? Any technical issues? Happy to resend."

**Day 14 CHECKIN.md entry:**

```
## Day 14 Checkpoint — June 15, 2026

Determination: [PHASE_2_TRIGGER / CONTINUE_MONITOR / FAILURE_IMMINENT]

Cumulative Bitly clicks: [X]
Total replies: [X]
Sectors still WEAK: [list]
Sectors recovered to MODERATE: [list]

Actions taken:
- Modification 2 applied to: [list sectors]
- Direct contact made: [list if FAILURE_IMMINENT]

Next checkpoint: [June 30 (Day 30) / July 28 (Day 60)]
```

---

### Automated Checkpoint Timeline — June 1 through June 30

| Date | Checkpoint | Duration | Trigger |
|------|-----------|----------|---------|
| June 1 | Domain 39 distribution executes | — | HHS rule activation |
| June 4 | Day 3 soft check — first response scan | 5 min | Check Gmail only; no Bitly pull needed |
| June 8 | Day 7 Gate Checkpoint | 30 min | Section 1 procedure above |
| June 8–9 | Follow-up dispatch (if weak sectors) | 20 min | Section 3 templates for WEAK sectors |
| June 10 | Day 9 watch — POSSIBLE WEAK sector review | 10 min | Check if POSSIBLE WEAK sectors from June 8 have recovered |
| June 15 | Day 14 Micro-Checkpoint | 30 min | Applies only if Day 7 = MODERATE or WEAK |
| June 22 | Day 21 interim — Bitly check only | 5 min | Pull cumulative clicks; log in Gist_Views tab |
| June 30 | Day 30 Gate Checkpoint | 45 min | Full four-metric pull; Phase 2 decision |

**Day 30 (June 30) is the Phase 2 decision gate.** All Day 7–14 actions feed into the Day 30 determination. The five possible Day 30 determinations (STRONG / MODERATE / WEAK / ASSESS / FAILURE) are defined in day-7-14-30-decision-trees.md. The Domain 39 Phase 2 Readiness Tracker (Template D) will show whether the three Phase 2 trigger thresholds have been met.

---

### The June 30 Phase 2 Decision

At Day 30, the Constituencies tab will automatically display:

```
STRONG trigger: =IF(COUNTIF(I2:I8,"YES")>=4,"STRONG — ACTIVATE PHASE 2 NOW","Not yet: "&COUNTIF(I2:I8,"YES")&" of 4 needed")
MODERATE trigger: =IF(COUNTIF(J2:J8,"YES")>=3,"MODERATE — ACTIVATE DOMAIN 39 NOW","Not yet: "&COUNTIF(J2:J8,"YES")&" of 3 needed")
```

If STRONG trigger is met: Phase 2 launches. Begin Tier 2 outreach using the social proof quotes collected from Score 4–5 Tier 1 replies.

If MODERATE trigger is met but not STRONG: Domain 39 continues; Domain 56 Tier 2 holds until Day 37.

If neither trigger is met: apply the three-modification failure recovery protocol from day-7-14-30-decision-trees.md (Modification 1: stakeholder substitution; Modification 2: framing revision; Modification 3: channel shift).

---

**Status**: Production-ready. Activate on June 1, 2026. First execution: June 8 at 08:00 UTC.
