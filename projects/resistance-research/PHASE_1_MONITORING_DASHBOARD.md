---
title: "Phase 1 Monitoring Dashboard — Production SOP"
created: 2026-05-26
version: 1.0
status: production-ready
scope: >
  Complete operating manual for Phase 1 post-distribution monitoring. Covers Google Sheets
  setup, Gist view tracking, reply triage, weekly synthesis, and Day 7/14/30 checkpoints.
  Solo-operator-friendly. No external tools beyond Google Sheets required.
word_count: ~3800
companion_files:
  - phase-1-monitoring-sheets-template.csv
  - phase-1-monitoring-decision-trees.md
  - PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md
  - PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE.md
  - PHASE_1_DECISION_TREES.md
  - DISTRIBUTION_GIST_URLS.md
first_weekly_synthesis_target: "June 4, 2026 (Day 7 checkpoint)"
weekly_time_budget: "15-20 minutes"
---

# Phase 1 Monitoring Dashboard — Production SOP

**Version 1.0 — May 26, 2026**

**Lead finding**: You need four numbers — Bitly total clicks, reply count, Score 3+ reply rate, and constituency engagement count — to run every checkpoint decision in Phase 1. This SOP tells you exactly where to find those numbers, how to record them, and what to do when the numbers arrive. If you follow this document and nothing else, you can run the Day 7 checkpoint on June 4 in under 20 minutes.

Domain 56 distribution begins May 28. Domain 39 distribution begins May 30 (June 1 HHS deadline). Day 7 checkpoint: June 4-5. Day 14 checkpoint: June 11-12. Day 30 checkpoint: June 27-28.

---

## Part 1: Google Sheets Setup (One-Time, ~45 Minutes)

### 1.1 Create the Spreadsheet

Open Google Sheets. Create a new blank spreadsheet. Title it: `Phase 1 Impact Dashboard — May 28, 2026`

Set sharing: click Share > Change to anyone with the link > Viewer. Copy the share URL. Paste it into CHECKIN.md under a new heading "Dashboard URL."

Add six sheets using the names below (click the + tab at the bottom):
1. `Contacts` — master contact log
2. `Gist Views` — weekly Bitly click tracking
3. `Replies` — reply triage and scoring
4. `Adoptions` — confirmed adoption signal log
5. `Constituencies` — aggregated per-constituency metrics
6. `Checkpoints` — checkpoint decision log (append-only)

### 1.2 Build the Contacts Sheet

Copy the headers from the CSV template (`phase-1-monitoring-sheets-template.csv`) into Row 1. The columns are:

| Col | Header | Instructions |
|-----|--------|--------------|
| A | Contact_ID | C001, C002, C003 — pre-filled in CSV template |
| B | Full_Name | Last, First |
| C | Organization | Institution name |
| D | Domain | Domain 56 / Domain 39 / (future domains) |
| E | Constituency | Law School / Imm Legal Aid / Civil Rights / Academic / Faith / Labor / Mutual Aid |
| F | Tier | Tier 1 / Tier 2 / Tier 3 |
| G | Email | Verified send address |
| H | Send_Date | Date the email was sent (fill when sent) |
| I | Delivery_Status | Delivered / Bounced / OOO / Unknown |
| J | Open_Date | Date first click detected via Bitly — leave blank until confirmed |
| K | Click_Date | Date contact clicked through to Gist — leave blank until confirmed |
| L | Reply_Date | Date first non-OOO reply received |
| M | Reply_Category | Implementation Signal / Critique-Objection / Data Request / General Question / No Reply |
| N | Engagement_Score | 0 = no contact; 1 = OOO only; 2 = polite ack; 3 = substantive; 4 = forward/collab request; 5 = citation/adoption |
| O | Tier2_Candidate | YES / blank — flag when Engagement Score is 3+ |
| P | Day_to_Open | Formula: =IF(J2="","",J2-H2) |
| Q | Day_to_Click | Formula: =IF(K2="","",K2-H2) |
| R | Day_to_Reply | Formula: =IF(L2="","",L2-H2) |
| S | Notes | Free text |

Add the pre-populated contacts from the CSV template. Domain 56 contacts are rows 2-12 (11 contacts). Domain 39 contacts are rows 13-17 (5 contacts).

**Auto-calculation rows** — add these formulas in a pinned summary block at the top (rows 2 rows above your data, or in a separate "Summary" area):

```
Total contacts sent:        =COUNTA(H2:H200)-COUNTBLANK(H2:H200)
Confirmed delivered:        =COUNTIF(I2:I200,"Delivered")
Total replies:              =COUNTA(L2:L200)-COUNTBLANK(L2:L200)
Overall reply rate:         =Total replies / Confirmed delivered
Score 3+ count:             =COUNTIF(N2:N200,">=3")
Score 3+ rate:              =Score 3+ count / Confirmed delivered
Tier 2 candidates:          =COUNTIF(O2:O200,"YES")
Avg day-to-open:            =AVERAGE(P2:P200)
Avg day-to-reply:           =AVERAGE(R2:R200)
Engagement velocity:        =Total replies / (TODAY()-MIN(H2:H200))
```

The `Engagement velocity` figure is replies per calendar day since first send. Target at Day 7: >0.3 (at least 2 replies in first 7 days).

### 1.3 Build the Gist Views Sheet

Headers in Row 1:

| Col | Header |
|-----|--------|
| A | Week_Number |
| B | Week_End_Date |
| C | Domain56_Clicks |
| D | Domain39_Clicks |
| E | DRP_Proposal_Clicks |
| F | DRP_Summary_Clicks |
| G | LitigationTracker_Clicks |
| H | Other_Links_Clicks |
| I | Total_Clicks_This_Week |
| J | Cumulative_Clicks |
| K | Delta_vs_Prior_Week |
| L | Spike_Flag |
| M | Spike_Notes |

Formula for Column I: `=SUM(C2:H2)`
Formula for Column J: `=IF(A2=1,I2,J1+I2)`
Formula for Column K: `=IF(A2=1,"—",I2-I1)`
Formula for Column L: `=IF(MAX(C2:H2)>=5,"SPIKE","")`

**Weekly targets** (record in a note or frozen row):
- Week 1 (by June 4): 15+ total clicks
- Week 2 (by June 11): 25+ cumulative
- Week 4 (by June 25): 50+ cumulative
- Week 8 (by July 23): 100+ cumulative

### 1.4 Build the Replies Sheet

This sheet is separate from the Contacts sheet — it is a per-reply log (one row per reply received, not per contact). Some contacts may reply multiple times.

| Col | Header |
|-----|--------|
| A | Reply_ID |
| B | Contact_ID |
| C | Organization |
| D | Reply_Date |
| E | Reply_Category |
| F | Engagement_Score |
| G | Key_Content |
| H | Action_Required |
| I | Escalation_Flag |
| J | Disposition |

For Reply Category definitions and the triage decision tree, see Part 3 of this SOP.

### 1.5 Build the Adoptions Sheet

| Col | Header |
|-----|--------|
| A | Signal_ID |
| B | Date_Detected |
| C | Organization |
| D | Constituency |
| E | Signal_Type |
| F | Domains_Referenced |
| G | Evidence_Source |
| H | Verification_Status |
| I | People_Reached_Est |
| J | Network_Event |
| K | Description |

Verification status values: Confirmed / Probable / Unconfirmed.

**Day 60 threshold formula** (add below the data):
```
=IF(COUNTIF(H2:H200,"Confirmed")>=15,"DAY 60 TARGET MET","Confirmed: "&COUNTIF(H2:H200,"Confirmed")&" of 15")
=IF(SUM(I2:I200)>=100,"PEOPLE REACHED TARGET MET","Reached: "&SUM(I2:I200)&" of 100")
```

### 1.6 Build the Constituencies Sheet

Seven data rows, one per constituency. One header row.

| Col | Header |
|-----|--------|
| A | Constituency |
| B | Total_Contacts |
| C | Confirmed_Delivered |
| D | Any_Reply_Count |
| E | Score3Plus_Count |
| F | Score3Plus_Rate |
| G | Day7_Status |
| H | Day30_Strong |
| I | Day30_Moderate |
| J | Adoption_Signals |
| K | Status_Note |

Column G values: PASS / MONITOR / FAIL
Column H and I values: YES / NO

**Constituency-level formula example (Law School row)**:
```
Total contacts:         =COUNTIF(Contacts!E:E,"Law School")
Confirmed delivered:    =COUNTIFS(Contacts!E:E,"Law School",Contacts!I:I,"Delivered")
Any replies:            =COUNTIFS(Contacts!E:E,"Law School",Contacts!L:L,"<>")
Score 3+ count:         =COUNTIFS(Contacts!E:E,"Law School",Contacts!N:N,">=3")
Score 3+ rate:          =Score3Plus_Count / Confirmed_Delivered
```

Repeat for all 7 constituencies.

**Phase 2 trigger formulas** (add at bottom of sheet):
```
Constituencies passing Day30 Strong:  =COUNTIF(H2:H8,"YES")
STRONG trigger:  =IF(COUNTIF(H2:H8,"YES")>=4,"STRONG — ACTIVATE PHASE 2 NOW","Not yet: "&COUNTIF(H2:H8,"YES")&" of 4 needed")
MODERATE trigger: =IF(COUNTIF(I2:I8,"YES")>=3,"MODERATE — ACTIVATE DOMAIN 39 NOW","Not yet")
```

### 1.7 Build the Checkpoints Sheet

Append-only. Never edit past rows.

| Col | Header |
|-----|--------|
| A | Checkpoint_Date |
| B | Checkpoint_Type |
| C | Overall_Reply_Rate |
| D | Score3Plus_Rate |
| E | Constituencies_Strong |
| F | Cross_Org_References |
| G | Adoption_Signals |
| H | Determination |
| I | Action_Taken |
| J | Notes |

Determination values: HOLD / MONITOR / ESCALATE (Day 7) or STRONG / MODERATE / WEAK / FAILURE (Day 30/60).

---

## Part 2: Gist View Tracking Protocol

### 2.1 What You Are Tracking

GitHub Gist does not expose view count data via its public API. The measurement proxy is Bitly click data: each Gist URL has a corresponding Bitly short link, and Bitly records clicks each time someone follows the link.

The Gist URLs and their corresponding Bitly short links:

| Document | Gist URL | Bitly Short Link |
|----------|----------|-----------------|
| Domain 56 (Civil Service) | https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f | Create at bit.ly — back-half: drp-d56 |
| Domain 39 (Healthcare) | https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b | Create at bit.ly — back-half: drp-d39 |
| DRP Proposal | https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 | Create at bit.ly — back-half: drp-2026 |
| Executive Summary | https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4 | Create at bit.ly — back-half: drp-summary |
| Litigation Tracker | https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0 | Create at bit.ly — back-half: drp-litigation |

**If Bitly short links do not yet exist**: Go to bitly.com, create a free account (or log in), and for each Gist URL above, create a short link with the back-half listed. This takes 5 minutes total, one-time. The back-half (drp-d56, etc.) is your custom identifier.

Use the Bitly short links — not the raw Gist URLs — in your outreach emails. This ensures all clicks are tracked.

### 2.2 Weekly Snapshot Process

Run this every Monday, starting June 2 (or the Monday after your first send, whichever comes first). Budget: 5 minutes.

**Step 1**: Go to bitly.com and log in.

**Step 2**: For each tracked link, click the link name and record the "Total clicks" figure for the past 7 days. Bitly free tier shows weekly click totals in the link detail view.

**Step 3**: Enter the numbers in the Gist Views sheet — one row per week. Fill columns C through H with click counts for each link. The Total, Cumulative, and Delta columns auto-calculate.

**Step 4**: Check the Spike Flag column. If it shows SPIKE (any link had 5+ clicks in the weekly period), add a note in column M: which link spiked, what date the spike likely occurred, and whether it correlates with a send date.

**Step 5**: Cross-reference spike timing. If a spike occurs 24-72 hours after an email send date, that is a confirmed click-through from your outreach. If a spike occurs without a corresponding send (organic traffic), flag it as an organic amplification event in the Notes column of the Checkpoints sheet.

### 2.3 Documenting View Metrics

Each weekly snapshot goes in one row of the Gist Views sheet. After entering the row, add a brief note to WORKLOG.md: date, week number, total clicks, delta, and any spike observations. This creates a searchable history without requiring manual review of the spreadsheet.

Example WORKLOG note format:
```
[Date] — Gist Views Week [N]: [X] total clicks ([+Y] vs prior week). 
[Link name] spike [date] — [correlation with send / organic]. 
Cumulative: [Z] clicks since launch.
```

### 2.4 Trigger Thresholds — Escalation Criteria

These thresholds require immediate response, not deferred action:

| Condition | Action |
|-----------|--------|
| Week 1 total clicks < 5 with confirmed email delivery | Check Bitly short link integrity. Confirm the short link in your email resolves to the correct Gist. Re-test by clicking the link yourself and verifying it increments in Bitly. |
| Week 1 total clicks < 15 (but 5 or more) | MONITOR status. No immediate action. Check again at Day 14. |
| Week 1 total clicks >= 15 | HOLD status. Normal trajectory. Continue to Day 30. |
| Any week with 0 clicks after week 2 | ESCALATE. Traffic has dropped to zero — investigate whether Gist became private, Bitly link broke, or organic interest has lapsed. |
| Organic spike (spike with no corresponding send) | Flag as amplification event. Check referring sources in Bitly if available. Note the referring organization if identifiable. |
| Week 4 cumulative < 30 | Below target. Add note to CHECKIN.md. Consider resend to non-responders. |
| Week 4 cumulative >= 50 | On track for Day 30 threshold. No action needed. |

**Messaging adjustment trigger**: If cumulative clicks at Day 14 are below 20 AND reply count is below 2, the outreach messaging may need adjustment. This is the trigger to review the subject line and opening paragraph of your email. Do not resend with identical messaging — see Part 4 (Failure Recovery) of the decision trees document.

---

## Part 3: Reply Triage Framework

### 3.1 The Five Reply Categories

Every reply you receive — from Day 1 through Day 60 — gets assigned to one of these five categories. The category determines what you do next.

**Category 1: Implementation Signal**

Definition: The contact expresses intent to incorporate Phase 1 materials into their work, explicitly requests permission to adapt content, asks for a version suitable for their specific use case, or states that they have already begun using the framework.

Indicators: "We'd like to include this in our clinic curriculum," "Can we adapt the model brief language?," "I've forwarded this to our policy team," "We're incorporating this into our training program," "I'd like to discuss using this as a foundation for our upcoming report."

Engagement Score: 4-5.

What to do: Same-day response. Thank the contact, confirm permission to use and adapt (you have granted it), offer to connect by phone if they want to discuss application to their specific context. Record in Adoptions sheet. Flag the contact as Tier 2 Candidate in the Contacts sheet. If this is your first Score 5 response, add an EARLY SIGNAL note to CHECKIN.md.

**Category 2: Critique or Objection**

Definition: The contact raises a substantive objection to a claim, methodology, framing, or conclusion in the Phase 1 materials. This is not a hostile reply — it is an intellectually engaged reply that challenges the content.

Indicators: "I think your framing of [X] overstates the threat," "The comparative evidence from [country] doesn't actually support the claim in Section [Y]," "Your sourcing on [Z] relies too heavily on advocacy organizations rather than peer-reviewed research," "I'm skeptical of the causal claim in Domain [N]."

Engagement Score: 3 (substantive engagement, even if critical).

What to do: Respond within 48 hours. Acknowledge the critique specifically (not generically). Do not be defensive. Either concede the point (if valid) or provide your supporting evidence. The goal is continued engagement — a critique is more valuable than silence. Record the critique in the Replies sheet under Key_Content. If the same critique appears from 3 or more contacts, it is a systematic signal — see the 30%+ critique escalation threshold below.

**Category 3: Data Request**

Definition: The contact asks for additional data, sources, updated statistics, or a version of the materials in a different format (slides, a summary brief, a version adapted for a non-specialist audience, a Spanish-language version).

Indicators: "Do you have updated figures on [metric]?," "Can you send me the underlying sources for the claim on page [N]?," "Do you have a version of this that would be accessible for non-lawyers?," "Is there a slide deck?"

Engagement Score: 3.

What to do: Respond within 48 hours. Provide the requested data or format if readily available (the sources section of each Gist document is citable). If the request is for a new format (slides, a brief), note it in the Key_Content column and add it to your Phase 1 materials wish list — this is a signal that the format is the friction point, not the content. If multiple contacts request the same format, prioritize creating it.

**Category 4: General Question**

Definition: The contact asks a question about the framework — what it is, who produced it, how it can be used — without expressing intent to adopt or raising a specific critique.

Indicators: "What is the intended use of this framework?," "Is this peer-reviewed?," "Who is behind this project?," "Can you tell me more about your background?," "What's the publication status of this work?"

Engagement Score: 2.

What to do: Respond within 72 hours. Answer the question directly and concisely. Close with a single follow-up question that invites the contact to describe their current work and whether the framework could be relevant to it. Do not pitch — let them indicate interest. If they ask about peer review status, the honest answer is that the framework is independently produced research and has not been through formal peer review; it draws on peer-reviewed sources throughout and welcomes expert critique.

**Category 5: No Reply**

Definition: No reply by the target date. This is the most common outcome and is not a failure signal unless it persists beyond the checkpoint thresholds.

What to do: No immediate action. Track the contact in the No Reply category in the Contacts sheet. At Day 14, if no reply and no Bitly click detected from the outreach window, apply the MONITOR protocol. At Day 30, if still no engagement, this contact feeds the WEAK calculation.

### 3.2 Category Decision Tree

When a reply arrives, run this check in order:

```
REPLY RECEIVED
      |
      v
Does the reply contain any of these phrases?
  - "incorporate," "use," "adapt," "curriculum," "training," "brief," "clinic"
  - "forwarded," "shared with," "passed to"
  - "we are / we plan to / we would like to"
      |
   YES -> Category 1: Implementation Signal
          Engage same-day. Record in Adoptions.
      |
      v
Does the reply challenge a specific claim, methodology, or conclusion?
      |
   YES -> Category 2: Critique/Objection
          Respond within 48 hours. Record critique in Replies.
      |
      v
Does the reply request additional data, sources, or a different format?
      |
   YES -> Category 3: Data Request
          Respond within 48 hours.
      |
      v
Does the reply ask a general question about the framework?
      |
   YES -> Category 4: General Question
          Respond within 72 hours.
      |
      v
Is the reply an out-of-office autoresponse only?
      |
   YES -> Score 1. No action. Note OOO return date and
          check for reply after that date.
      |
      v
Is the reply a polite acknowledgment with no specific engagement?
      |
   YES -> Score 2. Category 4. Respond within 72 hours
          with a brief follow-up question.
```

### 3.3 Escalation Threshold: 30% Critique Rate

If 30% or more of your replies in any 14-day window fall into Category 2 (Critique/Objection), this is a Phase 1 messaging pivot signal.

**What 30% critique rate means in practice**: If you have 10 replies and 3 or more are critiques, the content or framing of your pitch is generating resistance rather than adoption interest. This does not mean the research is wrong — it means the framing may be misaligned with the audience's priors.

**Response to 30%+ critique rate**:
1. Add a note to CHECKIN.md: "Critique rate [X]% — messaging review needed."
2. Review the specific critiques. Identify whether they cluster around a theme (a single claim, a framing choice, a data source).
3. If the critiques cluster: revise the outreach email to address the critique directly in the opening paragraph ("Some colleagues have raised questions about [X] — here is how I am thinking about that...").
4. Do not revise the Phase 1 research documents in response to email critiques without careful consideration — revising the underlying materials is a higher-stakes decision than revising the pitch.
5. If critiques are substantive and valid, flag in CHECKIN.md under "Needs Your Input" with the specific claims being challenged.

### 3.4 Cross-Organizational Reference Detection

When a reply contains the phrase "I forwarded this to," "I shared this with," or "I passed this along to [person or organization]," record it as a network event:

- Record in Contacts sheet: Column K (Referral_Made) — the name of the person or organization referred to
- Enter a row in the Adoptions sheet: Signal_Type = "Referral," Network_Event = YES, Verification_Status = Probable (until the referred party contacts you)
- When the referred party contacts you: update Verification_Status to Confirmed

Three cross-organizational references confirmed is one of the STRONG Day 30 threshold criteria. Track every referral mention, even tentative ones.

---

## Part 4: Weekly Synthesis Template

Run this once per week, starting the week of June 2. Budget: 15-20 minutes per week. Fill in the bracketed sections with your observations.

---

### Weekly Phase 1 Synthesis — Week [N]

**Date range**: [Monday date] through [Sunday date]
**Day count since first send**: Day [X] through Day [Y]
**Domains in distribution**: [Domain 56 / Domain 39 / other]

---

**RUNNING METRICS** (auto-fill from dashboard)

| Metric | This Week | Cumulative |
|--------|-----------|------------|
| Contacts sent | — | [total from Contacts sheet] |
| Confirmed delivered | — | [from Contacts sheet] |
| Gist clicks (all links) | [from Gist Views sheet, current week column] | [cumulative column] |
| Replies received | [new replies this week] | [total to date] |
| Overall reply rate | — | [total replies / delivered] |
| Score 3+ replies | [new this week] | [total to date] |
| Score 3+ rate | — | [Score3+ count / delivered] |
| Category 1 (Implementation) | [count this week] | [total] |
| Category 2 (Critique) | [count this week] | [total] |
| Critique rate | [Cat 2 / total replies this week] | — |
| Tier 2 candidates | — | [from Contacts sheet] |
| Confirmed adoptions | — | [from Adoptions sheet] |

---

**KEY FINDINGS** [fill in your observations — 3-5 bullet points]

- [What happened this week that was most significant?]
- [Which contacts responded and what did they say?]
- [What patterns are you seeing across replies?]
- [Any organic amplification events — clicks with no send correlation?]
- [Any unexpected organizations or individuals making contact?]

---

**ENGAGEMENT PATTERNS — what's working** [fill in, 2-4 bullet points]

- [Which constituency or domain is getting the strongest response?]
- [Which framing, subject line, or approach is generating the most Category 1/2 replies?]
- [Are certain types of contacts (senior faculty vs. staff attorneys, etc.) responding faster?]
- [Is the Gist click rate correlating with reply rate, or are there clicks with no follow-up replies?]

---

**PROBLEM SIGNALS — what needs adjustment** [fill in, or write "None detected this week"]

- [Any delivery failures or bounces?]
- [Any constituencies with zero engagement for 2+ weeks?]
- [Critique rate above 30%?]
- [Gist click velocity declining (delta negative this week vs. last week)?]
- [Any contacts who replied negatively or asked to be removed?]

---

**TIER 2 CANDIDATES — who to contact next** [fill in, or write "No new candidates this week"]

- [List any contacts who reached Score 3+ this week]
- [For each candidate: what they said, what domain they engaged with, what the natural follow-up would be]
- [Note any referred parties who have now made contact]

---

**CHECKPOINT STATUS** (check only if a checkpoint falls in this week's date range)

[ ] Day 7 checkpoint: Run decision tree in `phase-1-monitoring-decision-trees.md`
[ ] Day 14 checkpoint: Run mid-cycle review (see decision trees)
[ ] Day 30 checkpoint: Run full decision tree — Phase 2 go/no-go determination

---

**DECISION PROMPT**

Based on this week's data: Should we escalate to Tier 2 outreach?

- [ ] YES — [which contacts / which domain / what is the trigger evidence]
- [ ] NOT YET — [what signal or threshold is still pending]
- [ ] NEEDS INPUT — [describe what you observed and what decision you are unable to make alone]

If YES: Pull the relevant Tier 2 contact list from DOMAIN_56_TIER2_SEND_GUIDE.md or DOMAIN_39_DISTRIBUTION_STRATEGY.md and execute within 48 hours.

---

*Estimated completion time: 15-20 minutes. If this is taking longer, the raw data entry is the bottleneck — simplify by filling only the Running Metrics table and Key Findings section. The narrative sections are useful but not critical for checkpoint decisions.*

---

## Part 5: Pre-Testing Checklist (Run Before May 27 Evening)

Complete these steps before the first Domain 56 send on May 28:

**Google Sheets** (20 minutes):
- [ ] Create spreadsheet titled "Phase 1 Impact Dashboard — May 28, 2026"
- [ ] Add 6 sheets with correct names (Contacts, Gist Views, Replies, Adoptions, Constituencies, Checkpoints)
- [ ] Import or manually enter the 16 contacts from the CSV template
- [ ] Verify all column headers match the schema in Part 1
- [ ] Add auto-calculation formulas in Contacts and Gist Views sheets
- [ ] Set sharing to "Anyone with link can view" — copy share URL to CHECKIN.md

**Bitly links** (10 minutes):
- [ ] Create Bitly account or log in at bitly.com
- [ ] Create short link for Domain 56 Gist (back-half: drp-d56)
- [ ] Create short link for Domain 39 Gist (back-half: drp-d39)
- [ ] Create short link for DRP Proposal (back-half: drp-2026) if not already created
- [ ] Test each short link: click it and confirm it resolves to the correct Gist
- [ ] Check Bitly dashboard: confirm click count incremented (you should see 1 click per test)
- [ ] Replace Gist URLs in Domain 56 and Domain 39 email templates with Bitly short links

**Google Alerts** (5 minutes):
- [ ] Set alert for: "35-domain democratic renewal framework"
- [ ] Set alert for: "democratic renewal framework" healthcare OR litigation OR elections
- [ ] Set alert for your name or handle if using one
- [ ] Set delivery: once a week digest, to your Gmail
- [ ] Create Gmail label "phase1-alerts" and filter alerts into it

**Day 7 checkpoint prep** (2 minutes):
- [ ] Mark June 4 in your calendar as "Day 7 checkpoint — run decision tree"
- [ ] Mark June 11 as "Day 14 mid-cycle check"
- [ ] Mark June 27 as "Day 30 checkpoint — Phase 2 go/no-go"
- [ ] Add `phase-1-monitoring-decision-trees.md` to a bookmarked folder for quick access on checkpoint dates

---

## Part 6: Quick-Reference Contacts and Document Map

**Domain 56 distribution**: 11 contacts — see `execution/domain-56-contact-list.md` for emails and org details. Templates in `execution/domain-56-email-template.md`. Send guide: `DOMAIN_56_TIER2_SEND_GUIDE.md`.

**Domain 39 distribution**: 5 contacts — Georgetown CCF (childhealth@georgetown.edu), NHeLP (info@healthlaw.org), Brennan Center (kennardl@brennan.law.nyu.edu), IRG (info@responsivegov.org), Black Mamas Matter (info@blackmamasmatter.org). Send schedule: May 30 (Georgetown + NHeLP), June 1 (Brennan + IRG), June 2-3 (Black Mamas Matter). Hard stop: June 1 HHS deadline.

**Decision thresholds reference**: See `phase-1-monitoring-decision-trees.md` for numeric thresholds at each checkpoint.

**Phase 2 activation criteria**: See `PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md` Section 5 for STRONG/MODERATE/WEAK definitions. Day 30 STRONG requires: 50%+ Score 3+ reply rate, 4+ constituencies meeting their strong threshold, 3+ cross-org references, 2+ confirmed adoptions.

**Failure recovery**: If Day 30 is WEAK — do not extend same approach. Apply 3-modification protocol from `PHASE_1_DECISION_TREES.md` (stakeholder substitution, framing revision, channel shift).

**Post-synthesis contingency**: If synthesis runs on May 28, outcome routes to `post-synthesis-contingency-execution-playbooks.md`. TOO_EARLY staging: `TOO_EARLY_CONTINGENCY_STAGING_MAY26.md`.
