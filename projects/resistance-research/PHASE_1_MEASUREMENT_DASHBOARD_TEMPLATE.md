---
title: "Phase 1 Measurement Dashboard Template"
created: 2026-05-26
version: 1.0
status: production-ready
scope: >
  Google Sheets dashboard template for Phase 1 impact tracking. 7-sheet structure
  with formulas, permission model, and weekly update checklist.
word_count: ~1400
companion_files:
  - PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md
  - PHASE_1_DECISION_TREES.md
  - PHASE_1_IMPACT_MEASUREMENT_INFRASTRUCTURE.md
  - DISTRIBUTION_GIST_URLS.md
setup_time: "45 minutes one-time; 15 minutes/week ongoing"
---

# Phase 1 Measurement Dashboard Template

**Version 1.0 — May 26, 2026**

This document specifies the exact structure of the Google Sheets dashboard used to track Phase 1 adoption and impact. It is organized as 7 named sheets. Build the dashboard once before Wave 1 sends and update it weekly. The dashboard is the single source of truth for Phase 2 go/no-go decisions — the checkpoints in PHASE_1_DECISION_TREES.md read from it directly.

**Permission model**: Create the sheet in your personal Google account (wanka95@gmail.com). Set sharing to "Anyone with the link can view." The orchestrator reads the URL and reports findings back to CHECKIN.md. Do not grant edit access to external parties.

---

## Sheet 1: Master Contact Log

**Purpose**: One row per Tier 1 contact. Tracks outreach status, reply score, and adoption signals for all 45 contacts.

**Column structure**:

| Column | Header | Data Type | Notes |
|--------|--------|-----------|-------|
| A | Contact_ID | Text | Format: C001 through C045 |
| B | Full_Name | Text | Last, First |
| C | Organization | Text | Institution name |
| D | Constituency | Text | One of: Law School / Imm Legal Aid / Civil Rights / Academic / Faith / Labor / Mutual Aid |
| E | Email | Text | Verified contact email |
| F | Wave_Sent | Date | Date the initial email was sent |
| G | Delivery_Status | Text | Delivered / Bounced / OOO / Unknown |
| H | First_Reply_Date | Date | Leave blank until reply received |
| I | Reply_Score | Number 1-5 | 1=OOO only; 2=Polite ack; 3=Substantive; 4=Forward/collab request; 5=Citation/formal adoption |
| J | Referral_Source | Text | Name of contact who referred this person (if applicable) |
| K | Referral_Made | Text | Name of person/org this contact referred Phase 1 to |
| L | Adoption_Signal | Text | Brief description of adoption event if any |
| M | Adoption_Signal_Date | Date | Date adoption event was detected |
| N | Survey_Sent | Date | Date Day 30 survey was sent |
| O | Survey_Response | Text | Verbatim response or "No response" |
| P | Notes | Text | Free text for anything notable |

**Auto-calculations (enter these formulas in a summary row at top of sheet)**:

```
Total contacts:           =COUNTA(A2:A1000)-1
Delivery confirmed:       =COUNTIF(G2:G1000,"Delivered")
Bounce count:             =COUNTIF(G2:G1000,"Bounced")
Adjusted sent count:      =Delivery confirmed
Total replies:            =COUNTA(H2:H1000)-COUNTBLANK(H2:H1000)
Reply rate (all):         =Total replies / Adjusted sent count
Score 3+ replies:         =COUNTIF(I2:I1000,">=3")
Score 3+ rate:            =Score 3+ replies / Adjusted sent count
Total referrals made:     =COUNTA(K2:K1000)-COUNTBLANK(K2:K1000)
Adoption signals:         =COUNTA(L2:L1000)-COUNTBLANK(L2:L1000)
```

**Constituent-specific reply rates (add for each constituency)**:

```
Law School reply rate (Score 3+):
  =COUNTIFS(D2:D1000,"Law School",I2:I1000,">=3") / COUNTIFS(D2:D1000,"Law School",G2:G1000,"Delivered")

[Repeat this formula pattern for each of the 7 constituencies]
```

---

## Sheet 2: Gist View Log

**Purpose**: Weekly tracking of Bitly click counts for each distributed Gist document.

**Column structure**:

| Column | Header | Notes |
|--------|--------|-------|
| A | Week_Number | 1, 2, 3, etc. from Wave 1 send date |
| B | Week_End_Date | Sunday of that week |
| C | DRP_Proposal_Clicks | Bitly clicks for bit.ly/drp-2026 (Democratic Renewal Proposal) |
| D | DRP_Summary_Clicks | Bitly clicks for bit.ly/drp-summary (Executive Summary) |
| E | DRP_Litigation_Clicks | Bitly clicks for bit.ly/drp-litigation (Litigation Tracker) |
| F | DRP_FA_Clicks | Bitly clicks for bit.ly/drp-fa (First Amendment Tracker) |
| G | Domain37_Clicks | Bitly clicks for Domain 37 Gist short link |
| H | Domain56_Clicks | Bitly clicks for Domain 56 Gist short link |
| I | Total_Clicks_Week | =SUM(C:H) for that row |
| J | Cumulative_Clicks | Running sum of Total_Clicks_Week |
| K | Spike_Flag | "YES" if any single link had 5+ clicks in one day; blank otherwise |
| L | Spike_Notes | Free text: which link, what date, possible cause |

**Spike detection formula (in Column K)**:
```
=IF(MAX(C2:H2)>=5,"YES","")
```
Note: This formula checks whether any single link value in that week is 5 or more. To detect single-day spikes, you will need to check Bitly daily view at the Bitly dashboard and note manually — Bitly free tier does not export daily granularity to a webhook, only cumulative.

**Target clicks by week**:
- Week 1: 15+ total clicks (minimum viable engagement)
- Week 2: 25+ cumulative
- Week 4: 50+ cumulative (30-day milestone)
- Week 8: 100+ cumulative (60-day milestone)

---

## Sheet 3: Adoption Signal Registry

**Purpose**: Formal log of every confirmed adoption event. This is the primary evidence base for Phase 2 solicitation and for the Day 60 checkpoint assessment.

**Column structure**:

| Column | Header | Notes |
|--------|--------|-------|
| A | Signal_ID | Format: AS001, AS002, etc. |
| B | Date_Detected | Date the signal was confirmed |
| C | Organization | Organization name |
| D | Constituency | One of 7 constituencies |
| E | Signal_Type | Curriculum / Litigation Toolkit / Policy Brief / Training Module / Governance Document / Citation / Other |
| F | Domain(s) Referenced | Which Phase 1 domain(s) are being adopted |
| G | Evidence_Source | Reply email / Survey response / Web detection / PACER search / Direct contact |
| H | Verification_Status | Confirmed / Probable / Unconfirmed |
| I | People_Reached | Estimated number of people trained/exposed through this adoption event |
| J | Network_Event | YES if this adoption triggered outreach to a new organization; blank if not |
| K | Description | 1-2 sentence description of the adoption |

**Auto-calculations (summary row)**:

```
Total confirmed adoptions:      =COUNTIF(H2:H1000,"Confirmed")
Total probable adoptions:       =COUNTIF(H2:H1000,"Probable")
Total people reached (est.):    =SUM(I2:I1000)
Network events triggered:       =COUNTIF(J2:J1000,"YES")
```

**Day 60 threshold check**:
```
=IF(COUNTIF(H2:H1000,"Confirmed")>=15,"DAY 60 THRESHOLD MET","Below threshold: "&COUNTIF(H2:H1000,"Confirmed")&" of 15 required")
=IF(SUM(I2:I1000)>=100,"PEOPLE REACHED THRESHOLD MET","Below threshold: "&SUM(I2:I1000)&" of 100 required")
```

---

## Sheet 4: Constituency-Aggregated Metrics

**Purpose**: One row per constituency. The decision-facing view — this is what you look at during checkpoint reviews.

**Row structure (one row per constituency, 7 rows total)**:

| Column | Header | Notes |
|--------|--------|-------|
| A | Constituency | Law School / Imm Legal Aid / Civil Rights / Academic / Faith / Labor / Mutual Aid |
| B | Total_Contacts | Pull from Master Contact Log |
| C | Confirmed_Delivered | Pull from Master Contact Log |
| D | Any_Reply_Count | Replies at any score |
| E | Score3Plus_Count | Substantive replies (Score 3+) |
| F | Score3Plus_Rate | =E/C |
| G | Day7_Status | PASS / MONITOR / FAIL (see thresholds in PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 4) |
| H | Day30_Strong | YES / NO — did constituency meet its Day 30 strong threshold? |
| I | Day30_Moderate | YES / NO — did constituency meet its Day 30 moderate threshold? |
| J | Adoption_Signals | Count from Adoption Signal Registry |
| K | People_Reached | Sum from Adoption Signal Registry |
| L | Network_Events | Count from Adoption Signal Registry |
| M | Status_Note | Free text: key developments for this constituency |

**Constituency aggregate formulas (example for Law Schools — repeat pattern for each)**:

```
Total contacts:        =COUNTIF('Master Contact Log'!D:D,"Law School")
Confirmed delivered:   =COUNTIFS('Master Contact Log'!D:D,"Law School",'Master Contact Log'!G:G,"Delivered")
Score 3+ count:        =COUNTIFS('Master Contact Log'!D:D,"Law School",'Master Contact Log'!I:I,">=3")
Score 3+ rate:         =Score 3+ count / Confirmed delivered
Adoption signals:      =COUNTIFS('Adoption Signal Registry'!D:D,"Law School",'Adoption Signal Registry'!H:H,"Confirmed")
```

**Overall gate formula (bottom of sheet)**:
```
Constituencies passing Day30 Strong:   =COUNTIF(H2:H8,"YES")
Phase 2 STRONG trigger:                =IF(COUNTIF(H2:H8,"YES")>=4,"STRONG - ACTIVATE PHASE 2","Below STRONG threshold")
Phase 2 MODERATE trigger:              =IF(COUNTIF(I2:I8,"YES")>=3,"MODERATE - ACTIVATE DOMAIN 39","Below MODERATE threshold")
```

---

## Sheet 5: Engagement Timeline

**Purpose**: Day-by-day log for Weeks 1-8. Used for trajectory analysis and spike detection.

**Column structure**:

| Column | Header | Notes |
|--------|--------|-------|
| A | Date | Calendar date |
| B | Day_Number | Days since Wave 1 send |
| C | New_Replies_Today | Count of new replies received on this date |
| D | Reply_Scores_Today | Comma-separated list of scores (e.g., "3,2,4") |
| E | Gist_Clicks_Today | Manual entry from Bitly dashboard (2-min daily check during Weeks 1-2) |
| F | Referrals_Detected | Count of new referral events |
| G | Adoption_Events | Count of new adoption signals |
| H | Notes | Any notable events (spike, OOO cluster, etc.) |

**Weekly summary formula (add to bottom of each week's data)**:
```
Week reply rate:    =SUM(C[week start]:C[week end]) / [adjusted sent count]
Week 1 benchmark:  =IF(SUM(C2:C8)/[sent]>=0.1,"Week 1 baseline met","Below Week 1 baseline")
```

---

## Sheet 6: Decision Checkpoint Log

**Purpose**: Permanent record of each checkpoint assessment. Do not edit past entries — append only.

**Column structure**:

| Column | Header | Notes |
|--------|--------|-------|
| A | Checkpoint_Date | Actual date assessment was run |
| B | Checkpoint_Type | Day 7 / Day 30 / Day 60 / Ad Hoc |
| C | Overall_Reply_Rate | Calculated at time of assessment |
| D | Score3Plus_Rate | Calculated at time of assessment |
| E | Constituencies_Passing_Strong | Count of 7 |
| F | Cross_Org_References | Count at time of assessment |
| G | Adoption_Signals | Count at time of assessment |
| H | People_Reached | Estimate at time of assessment |
| I | Determination | STRONG / MODERATE / WEAK / TOO_EARLY / FAILURE |
| J | Phase_2_Decision | Action taken: e.g., "Domain 39 activated," "Hold pattern," "Extension to Day 90" |
| K | Notes | Context, anomalies, caveats |

---

## Sheet 7: Network Map

**Purpose**: Visual tracking of the referral network. Updated whenever a referral event is detected.

**Column structure**:

| Column | Header | Notes |
|--------|--------|-------|
| A | Referral_ID | Format: NW001, NW002, etc. |
| B | Source_Organization | Who made the referral |
| C | Source_Contact | Individual if known |
| D | Source_Constituency | Original constituency of source |
| E | Referred_Organization | Who was referred |
| F | Referred_Constituency | Constituency of referred party |
| G | Domain_Referenced | Which domain prompted the referral |
| H | Date_Detected | When referral was first detected |
| I | Confirmation_Status | Confirmed (referred org contacted us) / Probable (source mentioned it) / Unconfirmed |
| J | Second_Hop | YES if the referred org then referred to a third org |

**Network multiplier formula**:
```
Total referral events:       =COUNTA(A2:A1000)-1
Cross-constituency referrals:=COUNTIF(D2:D1000,"<>"&E2:E1000)  [note: use SUMPRODUCT for this]
Network multiplier rate:     =Total referral events / [initial Tier 1 contacts sent]
```

---

## Weekly Update Checklist (15 minutes total)

Run this checklist every Monday morning during Phase 1 active tracking period (Weeks 1-8):

**Step 1 — Email review (5 minutes)**
- Check Gmail label `phase1-outreach/replies/` for any new replies since last Monday
- Score each reply (1-5) and enter in Master Contact Log Column I
- If any reply contains a referral mention, add to Network Map sheet
- If any reply contains an adoption statement, add to Adoption Signal Registry

**Step 2 — Bitly click pull (3 minutes)**
- Log in to bitly.com/a/dashboard
- Record weekly click count for each of the 5-6 tracked links
- Enter in Gist View Log Sheet, Column C through H
- Calculate weekly total (Column I) and cumulative (Column J)
- Set spike flag if any link had a 5+ click day

**Step 3 — Web monitoring sweep (4 minutes)**
- Check Google Alerts inbox (label: `phase1-alerts`) for any new mentions
- If alert found: verify, score, enter in Adoption Signal Registry if confirmed
- Check regulations.gov for Domain 39 and Domain 42 comment dockets — any new comments citing framework vocabulary?
- Check SSRN author alerts for any Tier 1 academic contacts who uploaded new papers this week

**Step 4 — Dashboard update (3 minutes)**
- Update Constituency-Aggregated Metrics sheet auto-calculations (refresh by re-entering formulas if needed)
- Update Engagement Timeline sheet with this week's summary
- If any checkpoint date has passed, add row to Decision Checkpoint Log with current determination

**Total time**: 15 minutes per week.

---

## One-Time Setup Checklist (45 minutes)

Complete before Wave 1 sends:

1. Create Google Sheet titled "Phase 1 Impact Dashboard — [start date]"
2. Add 7 sheets using the names above
3. Build Master Contact Log with all 45 contacts from DISTRIBUTION_OUTREACH_CONTACTS.md
4. Set sharing to "Anyone with the link can view" — copy the share URL to CHECKIN.md
5. Set up Bitly links for each Gist (PHASE_1_IMPACT_MEASUREMENT_INFRASTRUCTURE.md Section 1.1)
6. Set up Gmail labels (PHASE_1_IMPACT_MEASUREMENT_INFRASTRUCTURE.md Section 1.2)
7. Set up 3 Google Alerts (see Section 3.3 of PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md)
8. Enter all 45 contacts in Master Contact Log (30 minutes — can be done in parallel with email drafting)
9. Add the share URL to CHECKIN.md under "Dashboard URL" heading
