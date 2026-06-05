---
title: "Phase 1 Impact Measurement Dashboard — Domain 51 / Wave 1 Foundation"
subtitle: "Google Sheets Blueprint for June 9 Wave 1 Monitoring and T+7 Decision Gate"
created: "2026-06-05"
item: "Exploration Queue Item 84"
status: "production-ready"
wave_1_execution: "June 9, 2026 09:00 AM UTC"
t7_checkpoint: "June 16–18, 2026"
phase_2_gate: "T+7 determines Phase 2 batch activation"
cross_references:
  - PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md
  - PHASE_2_SEQUENTIAL_ACTIVATION_STRATEGY.md
  - DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md
  - domain-51-send-templates.md
  - DAILY_SIGNAL_LOG_ENTRY_GUIDE.md
  - T7_CHECKPOINT_DECISION_AUTOMATION.md
---

# Phase 1 Impact Measurement Dashboard — Domain 51 / Wave 1
## Google Sheets Blueprint: 7-Sheet Structure, Formulas, and Example Data

*Prepared June 5, 2026. Production-ready for copy before June 9 Wave 1 execution. This is the operational measurement infrastructure for the 5-checkpoint evaluation cycle: T+3 / T+7 / T+14 / T+30 / T+45.*

---

## Zero-Setup Instructions

**Time required**: 20 minutes to copy and pre-populate before June 9.

1. Open Google Sheets: sheets.new
2. Rename the default tab "Sheet1" to "Daily Signal Log"
3. Add 6 more sheets with names exactly as listed below
4. Copy the column headers and example rows from each section into the corresponding sheet
5. Paste the formula templates (no modification needed — they reference sheet names as written here)
6. Set sharing: Share > "Anyone with the link" > "Viewer" — copy the URL to CHECKIN.md
7. Begin entering data on June 9 after each send

**No macros. No Apps Script. No add-ons. All formulas use standard Google Sheets functions.**

**Sheet tab order (left to right)**:
1. Daily Signal Log
2. Email Analytics
3. Engagement Classification
4. Decision Checkpoint Record
5. Cumulative Summary
6. Contingency Trigger Log
7. Phase 2 Batch Readiness Matrix

---

## Sheet 1: Daily Signal Log

**Purpose**: The primary data entry sheet. One row per contact event (send, reply, bounce, follow-up). Fill in manually as events occur. This is the source table that drives all formulas in Sheets 3, 4, and 5.

**Rule**: Enter a row every time something happens with any of the 5 organizations. No formula entry required on this sheet — it is fill-in only.

### Column Structure

| Col | Header | Data Type | Allowed Values / Format |
|-----|--------|-----------|-------------------------|
| A | Date | Date | MM/DD/YYYY |
| B | Organization | Text | CLC / Issue One / Common Cause CA / LWV CA / Clean Money |
| C | Tier | Text | A / B / C |
| D | Event_Type | Text | SEND / REPLY / BOUNCE / OOO / FOLLOW_UP / GIST_CLICK / NOTE |
| E | Signal_Code | Text | STRONG / MODERATE / WEAK / PENDING / N/A |
| F | Contact_Name | Text | Named individual if known; "Unknown" if general inbox |
| G | Channel | Text | EMAIL / GIST / PHONE / OTHER |
| H | Notes | Text | Free text — verbatim quote, observation, or context |

### Pre-Populated Header Row (copy this exactly into Row 1)

```
Date | Organization | Tier | Event_Type | Signal_Code | Contact_Name | Channel | Notes
```

### Example Data Rows

| Date | Organization | Tier | Event_Type | Signal_Code | Contact_Name | Channel | Notes |
|------|--------------|------|------------|-------------|--------------|---------|-------|
| 06/09/2026 | CLC | A | SEND | PENDING | Erin Chlopak | EMAIL | Template Email 4 sent to echlopak@campaignlegalcenter.org — 16:00 UTC |
| 06/09/2026 | Issue One | A | SEND | PENDING | Nick Penniman | EMAIL | Template Email 5 sent to info@issueone.org — 17:30 UTC |
| 06/11/2026 | Common Cause CA | B | SEND | PENDING | Darius Kemp | EMAIL | Template Email 1 sent to dkemp@commoncause.org — 16:00 UTC |
| 06/11/2026 | LWV CA | B | SEND | PENDING | Jenny Farrell | EMAIL | Template Email 2 sent to lwvc@lwvc.org — 16:30 UTC |
| 06/11/2026 | Clean Money | C | SEND | PENDING | Trent Lange | EMAIL | Template Email 3 sent to info@CAclean.org — 17:00 UTC |
| 06/11/2026 | CLC | A | GIST_CLICK | STRONG | Unknown | GIST | Bitly showed 3 clicks within 24h of CLC send — likely Chlopak team opened |
| 06/12/2026 | Issue One | A | REPLY | STRONG | Nick Penniman | EMAIL | "Shared with our research team — your AI PAC section is new to us" — forwarding signal confirmed |
| 06/14/2026 | Common Cause CA | B | OOO | WEAK | Darius Kemp | EMAIL | Auto-reply: Kemp OOO until June 16, alternate contact Sarah Morris cc'd |
| 06/15/2026 | LWV CA | B | REPLY | MODERATE | Jenny Farrell | EMAIL | "Received, forwarding to our policy team for review" — non-committal but positive routing signal |
| 06/16/2026 | Clean Money | C | NOTE | WEAK | Unknown | EMAIL | No reply, no bounce — 5 days post-send, marking WEAK at T+5 |

### Signal Code Entry Rules

Enter PENDING on every SEND row. Update to STRONG / MODERATE / WEAK when the outcome is known. See DAILY_SIGNAL_LOG_ENTRY_GUIDE.md for the complete decision tree for each organization.

Do not change a Signal_Code once set to STRONG or MODERATE. If a contact escalates (e.g., OOO then substantive reply), add a new row rather than editing the existing one — the new row's Signal_Code takes precedence.

---

## Sheet 2: Email Analytics

**Purpose**: Per-organization tracking of email delivery metrics and Bitly/Gist engagement. Data here comes from your email client (bounce notification, reply receipt) and Bitly dashboard. Update weekly — takes 5 minutes.

**Data sources**:
- Open rate %: Not directly measurable without a campaign platform. Use Bitly click data as a proxy — each Gist click represents a confirmed reader. If using Campaign Monitor or Mailchimp for any sends, enter open rates directly.
- Click rate %: Bitly clicks on the Domain 51 Gist short link, divided by confirmed sends to that organization.
- Gist URL: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372 (confirmed live June 5, 2026)

### Column Structure

| Col | Header | Data Type | Notes |
|-----|--------|-----------|-------|
| A | Organization | Text | 5 orgs + one "TOTAL" summary row |
| B | Contact_Email | Text | Verified send address |
| C | Template_Sent | Text | Email 1 / Email 2 / Email 3 / Email 4 / Email 5 |
| D | Send_Date | Date | Actual send date |
| E | Delivery_Status | Text | Delivered / Bounced / Unknown |
| F | Bounce_Reason | Text | Leave blank if delivered; enter bounce code if bounced |
| G | Gist_Clicks_Week1 | Number | Bitly clicks attributable to this org in Days 1–7 |
| H | Gist_Clicks_Week2 | Number | Bitly clicks in Days 8–14 |
| I | Gist_Clicks_Total | Formula | =G+H (extend as weeks pass) |
| J | Est_Open_Rate_Pct | Number | Manual estimate: 100 if reply confirmed, 50 if Gist click but no reply, 0 if no signal |
| K | Reply_Received | Text | YES / NO |
| L | Reply_Date | Date | Date of first reply |
| M | Campaign_Monitor_Link | Text | Paste Campaign Monitor or Bitly dashboard link for this org if available |
| N | Notes | Text | Any anomalies in delivery or engagement |

### Pre-Populated Rows (all 5 organizations)

| Organization | Contact_Email | Template_Sent | Send_Date | Delivery_Status | Bounce_Reason | Gist_Clicks_Week1 | Gist_Clicks_Week2 | Gist_Clicks_Total | Est_Open_Rate_Pct | Reply_Received | Reply_Date | Campaign_Monitor_Link | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CLC | echlopak@campaignlegalcenter.org | Email 4 | 06/09/2026 | | | | | =G2+H2 | | | | | |
| Issue One | info@issueone.org | Email 5 | 06/09/2026 | | | | | =G3+H3 | | | | | |
| Common Cause CA | dkemp@commoncause.org | Email 1 | 06/11/2026 | | | | | =G4+H4 | | | | | |
| LWV CA | lwvc@lwvc.org | Email 2 | 06/11/2026 | | | | | =G5+H5 | | | | | |
| Clean Money | info@CAclean.org | Email 3 | 06/11/2026 | | | | | =G6+H6 | | | | | |
| **TOTAL** | | | | =COUNTIF(E2:E6,"Delivered") delivered | | =SUM(G2:G6) | =SUM(H2:H6) | =SUM(I2:I6) | =AVERAGE(J2:J6) | =COUNTIF(K2:K6,"YES") | | | |

### Bitly API Integration Note (optional)

If you set up a Bitly free account and shorten the Gist URL before June 9, Bitly provides a dashboard showing clicks by day and approximate geographic source. No API key or script required — log in weekly, read numbers, enter in columns G and H. The Bitly free tier tracks up to 10 links with 30 days of history.

If you do not use Bitly, use the Gist view count as a proxy: GitHub shows total Gist views in the Gist header. Record the view count on June 9 (pre-send baseline) and again each Monday — the delta is the engagement signal. Enter delta in column G.

---

## Sheet 3: Engagement Classification

**Purpose**: One row per organization. Aggregates signal codes from Sheet 1 (Daily Signal Log) into a per-contact engagement status. Formula-driven — do not enter data here manually except in column H (Tier_Assignment).

### Column Structure

| Col | Header | Formula / Data Type | Notes |
|-----|--------|---------------------|-------|
| A | Organization | Text | Static — enter once |
| B | Tier | Text | Static — A, B, or C |
| C | Latest_Signal_Code | Formula | Most recent non-PENDING signal from Sheet 1 |
| D | STRONG_Count | Formula | Count of STRONG signals for this org |
| E | MODERATE_Count | Formula | Count of MODERATE signals for this org |
| F | WEAK_Count | Formula | Count of WEAK signals for this org |
| G | Status | Formula | Confirmed / Considering / Pass — derived from signal counts |
| H | Tier_Assignment | Text | Manual override if needed — leave blank to use formula |
| I | Last_Updated | Formula | Most recent date from Sheet 1 for this org |
| J | Notes | Text | Any qualitative context |

### Row Setup (pre-populate organization names in column A)

| A — Organization | B — Tier |
|---|---|
| CLC | A |
| Issue One | A |
| Common Cause CA | B |
| LWV CA | B |
| Clean Money | C |

### Formula Templates

Paste these into the appropriate columns (adjust row numbers as needed — Row 2 = CLC, Row 3 = Issue One, etc.):

**Column C — Latest Signal Code** (most recent non-PENDING code for this org):
```
=IFERROR(
  INDEX(
    'Daily Signal Log'!E:E,
    MATCH(2,1/((A2='Daily Signal Log'!B:B)*('Daily Signal Log'!E:E<>"PENDING")*('Daily Signal Log'!E:E<>"")),1)
  ),
"PENDING")
```
*Note: This is an array formula in Google Sheets. Enter with Ctrl+Shift+Enter or use the simpler FILTER version below.*

**Simpler version using FILTER (recommended for Google Sheets)**:
```
=IFERROR(
  INDEX(
    FILTER('Daily Signal Log'!E:E,
           ('Daily Signal Log'!B:B=A2)*('Daily Signal Log'!E:E<>"PENDING")*('Daily Signal Log'!E:E<>"")),
    ROWS(
      FILTER('Daily Signal Log'!E:E,
             ('Daily Signal Log'!B:B=A2)*('Daily Signal Log'!E:E<>"PENDING")*('Daily Signal Log'!E:E<>""))
    )
  ),
"PENDING")
```

**Column D — STRONG Count**:
```
=COUNTIFS('Daily Signal Log'!B:B,A2,'Daily Signal Log'!E:E,"STRONG")
```

**Column E — MODERATE Count**:
```
=COUNTIFS('Daily Signal Log'!B:B,A2,'Daily Signal Log'!E:E,"MODERATE")
```

**Column F — WEAK Count**:
```
=COUNTIFS('Daily Signal Log'!B:B,A2,'Daily Signal Log'!E:E,"WEAK")
```

**Column G — Status** (Confirmed / Considering / Pass):
```
=IF(D2>=1,"Confirmed",IF(E2>=1,"Considering",IF(F2>=1,"Pass","Pending")))
```

Logic: Any STRONG signal = Confirmed. No STRONG but at least one MODERATE = Considering. Only WEAK signals = Pass. No signals yet = Pending.

**Column I — Last Updated**:
```
=IFERROR(
  MAX(
    FILTER('Daily Signal Log'!A:A,
           'Daily Signal Log'!B:B=A2)
  ),
"No events")
```

### Example State After T+7 (June 16)

| Organization | Tier | Latest_Signal_Code | STRONG_Count | MODERATE_Count | WEAK_Count | Status |
|---|---|---|---|---|---|---|
| CLC | A | STRONG | 2 | 0 | 0 | Confirmed |
| Issue One | A | STRONG | 1 | 1 | 0 | Confirmed |
| Common Cause CA | B | MODERATE | 0 | 1 | 1 | Considering |
| LWV CA | B | MODERATE | 0 | 1 | 0 | Considering |
| Clean Money | C | WEAK | 0 | 0 | 1 | Pass |

---

## Sheet 4: Decision Checkpoint Record

**Purpose**: Permanent log of each formal checkpoint assessment. Append-only — do not edit past rows. This is the audit trail for Phase 2 go/no-go decisions.

**Checkpoints**: T+3 (June 12), T+7 (June 16–18), T+14 (June 23–25), T+30 (July 9–11), T+45 (July 24–26)

### Column Structure

| Col | Header | Data Type | Notes |
|-----|--------|-----------|-------|
| A | Checkpoint_Date | Date | Actual date assessment was run |
| B | Checkpoint_Label | Text | T+3 / T+7 / T+14 / T+30 / T+45 |
| C | Days_Since_Wave1 | Number | =A-DATE(2026,6,9) |
| D | STRONG_Signals_Total | Number | Count from Sheet 5 at time of assessment |
| E | MODERATE_Signals_Total | Number | Count from Sheet 5 at time of assessment |
| F | WEAK_Signals_Total | Number | Count from Sheet 5 at time of assessment |
| G | Confirmed_Count | Number | Orgs with Confirmed status from Sheet 3 |
| H | Overall_Determination | Text | STRONG / MODERATE / WEAK — per T7_CHECKPOINT_DECISION_AUTOMATION.md thresholds |
| I | Phase_2_Action | Text | Explicit action triggered by this determination |
| J | Decision_Tree_Branch | Text | Branch path taken in T7_CHECKPOINT_DECISION_AUTOMATION.md |
| K | Notes | Text | Anomalies, caveats, contextual factors |

### Decision Logic Notes (enter in column K at each checkpoint)

**T+3 Decision Notes (June 12)** — purpose is delivery confirmation, not signal assessment:
- Were all 5 sends confirmed delivered (no bounce)?
- Did Bitly show any clicks in 72 hours post-send?
- Action threshold: if CLC or Issue One bounced, re-send to info@campaignlegal.org immediately

**T+7 Decision Notes (June 16–18)** — the Phase 2 gate:
- STRONG if ≥4 STRONG signals across all 5 organizations (see T7_CHECKPOINT_DECISION_AUTOMATION.md)
- MODERATE if 2–3 STRONG signals
- WEAK if <2 STRONG signals
- Action: enter the Phase_2_Action in column I

**T+14 Decision Notes (June 23–25)** — calibration checkpoint:
- Are late replies coming in from Tier B contacts (Common Cause CA, LWV CA)?
- Do Gist view counts show sustained engagement or one-time open?

**T+30 Decision Notes (July 9–11)** — full engagement assessment:
- Overall reply rate from all 5 orgs
- Tier 2 contact activation decision (see Section 6, DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md)

**T+45 Decision Notes (July 24–26)** — campaign integration confirmation:
- Has any California contact integrated the research into campaign materials?
- Is Domain 51 research appearing in any public CA Fair Elections Act materials?

### Pre-Populated Checkpoint Dates (enter in column A)

| Date | Label |
|------|-------|
| 06/12/2026 | T+3 |
| 06/16/2026 | T+7 |
| 06/23/2026 | T+14 |
| 07/09/2026 | T+30 |
| 07/24/2026 | T+45 |

---

## Sheet 5: Cumulative Summary

**Purpose**: The primary decision-facing dashboard. Read this sheet when running checkpoint assessments. All numbers are formula-driven from Sheet 1 (Daily Signal Log) — no manual entry needed after setup.

### Column Structure

| Col | Header | Formula | Notes |
|-----|--------|---------|-------|
| A | Metric | Text | Static label |
| B | Current_Value | Formula | Auto-updating |
| C | T7_Target | Number | Static threshold |
| D | T30_Target | Number | Static threshold |
| E | Status | Formula | ON TRACK / BELOW TARGET / THRESHOLD MET |

### Metrics Table (enter in rows 2 through 14)

| Row | Metric | Formula (Column B) | T7 Target | T30 Target |
|-----|--------|--------------------|-----------|------------|
| 2 | Total Contacts Reached | =COUNTIF('Daily Signal Log'!D:D,"SEND") | 5 | 5 |
| 3 | Confirmed Delivered | =COUNTIFS('Daily Signal Log'!D:D,"SEND",'Daily Signal Log'!E:E,"<>WEAK") | 5 | 5 |
| 4 | Total STRONG Signals | =COUNTIF('Daily Signal Log'!E:E,"STRONG") | 2 | 4 |
| 5 | Total MODERATE Signals | =COUNTIF('Daily Signal Log'!E:E,"MODERATE") | 1 | 2 |
| 6 | Total WEAK Signals | =COUNTIF('Daily Signal Log'!E:E,"WEAK") | — | — |
| 7 | Confirmed Orgs (Status=Confirmed) | =COUNTIF('Engagement Classification'!G:G,"Confirmed") | 1 | 3 |
| 8 | Considering Orgs (Status=Considering) | =COUNTIF('Engagement Classification'!G:G,"Considering") | 1 | 1 |
| 9 | Pass / No Response Orgs | =COUNTIF('Engagement Classification'!G:G,"Pass") | — | — |
| 10 | Response Rate % | =B7/B2 | 20% | 60% |
| 11 | STRONG Signal Rate % | =B4/B2 | 40% | 80% |
| 12 | Gist Total Clicks (all orgs) | =SUM('Email Analytics'!I:I) | 5 | 20 |
| 13 | Days Since Wave 1 | =TODAY()-DATE(2026,6,9) | — | — |
| 14 | T7 Gate Status | =IF(B4>=4,"STRONG",IF(B4>=2,"MODERATE","WEAK")) | ≥4 = STRONG | — |

### Status Column Formulas

```
Row 2:  =IF(B2>=C2,"THRESHOLD MET","ON TRACK")
Row 4:  =IF(B4>=C4,"THRESHOLD MET",IF(B4>=1,"ON TRACK","BELOW TARGET"))
Row 7:  =IF(B7>=C7,"THRESHOLD MET",IF(B7>=1,"ON TRACK","BELOW TARGET"))
Row 10: =IF(B10>=0.2,"THRESHOLD MET",IF(B10>=0.1,"ON TRACK","BELOW TARGET"))
Row 14: =IF(B4>=4,"STRONG — PHASE 2 ACTIVATE",IF(B4>=2,"MODERATE — CONDITIONAL APPROVAL","WEAK — DEFER PHASE 2"))
```

### Constituency-Level Summary Block (rows 16–22)

Add a second table below the main metrics block for per-organization signal breakdown:

| Row | Organization | Formula: STRONG | Formula: MODERATE | Formula: WEAK | Formula: Status |
|-----|---|---|---|---|---|
| 17 | CLC | =COUNTIFS('Daily Signal Log'!B:B,"CLC",'Daily Signal Log'!E:E,"STRONG") | =COUNTIFS('Daily Signal Log'!B:B,"CLC",'Daily Signal Log'!E:E,"MODERATE") | =COUNTIFS('Daily Signal Log'!B:B,"CLC",'Daily Signal Log'!E:E,"WEAK") | ='Engagement Classification'!G2 |
| 18 | Issue One | (...same pattern...) | | | |
| 19 | Common Cause CA | (...same pattern...) | | | |
| 20 | LWV CA | (...same pattern...) | | | |
| 21 | Clean Money | (...same pattern...) | | | |
| 22 | **TOTAL** | =SUM(C17:C21) | =SUM(D17:D21) | =SUM(E17:E21) | =B14 |

---

## Sheet 6: Contingency Trigger Log

**Purpose**: Alert tracking for pre-defined contingency thresholds. Log a row when a contingency threshold is crossed — even if no action is immediately taken.

### Column Structure

| Col | Header | Data Type | Notes |
|-----|--------|-----------|-------|
| A | Alert_Date | Date | Date threshold was crossed |
| B | Checkpoint_Context | Text | T+3 / T+7 / T+14 / T+30 / T+45 |
| C | Trigger_Name | Text | Name of the specific contingency (see pre-populated list below) |
| D | Root_Cause_Diagnosis | Text | Infrastructure gap / Messaging gap / Timing issue / Organization unavailable |
| E | Escalation_Action | Text | Explicit action taken |
| F | Resolution_Date | Date | Date issue was resolved or trigger closed |
| G | Status | Text | Open / Resolved / Accepted (accepted = aware, no action needed) |

### Pre-Populated Trigger Reference (enter as static rows, update Status when triggered)

| Trigger_Name | Condition | Default Escalation_Action |
|---|---|---|
| CLC Bounce | echlopak@campaignlegalcenter.org bounces | Re-send immediately to info@campaignlegal.org; note in Daily Signal Log |
| Issue One No Gist Click by T+3 | Zero Bitly clicks from Issue One by June 12 | Check if Gist URL is accessible; re-test at gist.github.com; consider follow-up |
| CA Wave Zero Response by T+7 | No signal from Common Cause CA, LWV CA, or Clean Money by June 16 | Send Wave 3 follow-up to Common Cause CA per Section 4, DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md |
| Clean Money Email Invalid | info@CAclean.org bounces | Log "verification required"; do not delay other sends; investigate on June 12 |
| T+7 WEAK Determination | STRONG signal count <2 at T+7 | Defer Phase 2 batch activation; re-plan per T7_CHECKPOINT_DECISION_AUTOMATION.md WEAK path |
| Gist URL Inaccessible | HTTP error at gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372 | Check GitHub status; if >30 min outage, prepare PDF fallback; log in this sheet |
| Phase 2 Trigger Conflict | STRONG T+7 but Phase 2 activation bandwidth not available | Note resource constraint; move activation to next available window; do not drop signal |

### Example Completed Row

| Alert_Date | Checkpoint_Context | Trigger_Name | Root_Cause_Diagnosis | Escalation_Action | Resolution_Date | Status |
|---|---|---|---|---|---|---|
| 06/12/2026 | T+3 | CA Wave Zero Response by T+7 | Timing issue — Darius Kemp OOO | OOO noted; monitoring for June 16 return; Wave 3 follow-up standing by | — | Open |

---

## Sheet 7: Phase 2 Batch Readiness Matrix

**Purpose**: The T+7 decision output. One row per Phase 2 domain. Updated at T+7 checkpoint using the determination from Sheet 5, Row 14. This is the go/no-go activation sheet for Phase 2.

**When to fill this in**: Complete at T+7 checkpoint (June 16–18) based on Sheet 5 determination and PHASE_2_SEQUENTIAL_ACTIVATION_STRATEGY.md routing.

### Column Structure

| Col | Header | Data Type | Notes |
|-----|--------|-----------|-------|
| A | Domain | Text | Domain name |
| B | Research_Status | Text | COMPLETE / IN PROGRESS |
| C | External_Deadline | Date | Hard deadline for distribution |
| D | Coalition_Network | Text | Primary target organizations |
| E | Wave1_Signal_Relevance | Text | Does Domain 51 Wave 1 signal predict this domain's reception? HIGH / MEDIUM / LOW |
| F | T7_Activation_Status | Text | ACTIVATE / CONDITIONAL / DEFER / STANDBY |
| G | Activation_Trigger | Text | What signal level activates this domain |
| H | If_STRONG | Text | Action on STRONG determination |
| I | If_MODERATE | Text | Action on MODERATE determination |
| J | If_WEAK | Text | Action on WEAK determination |
| K | Notes | Text | Current status and next steps |

### Pre-Populated Rows (all Phase 2 domains)

| Domain | Research_Status | External_Deadline | Coalition_Network | Wave1_Signal_Relevance | T7_Activation_Status | Activation_Trigger |
|---|---|---|---|---|---|---|
| Domain 59 — Economic Precarity / CTC | COMPLETE | 06/30/2026 | CBPP, ITEP, NWLC, MomsRising, AFL-CIO | MEDIUM — different constituency (economic policy vs. democracy orgs) | ACTIVATE | Already executing; T+7 does not gate this domain |
| Domain 51 — Campaign Finance / Dark Money | COMPLETE | 07/01/2026 | CLC, Issue One, Common Cause CA, LWV CA, Clean Money | HIGH — this IS Wave 1 | EXECUTING | Wave 2 CA sends June 11; monitoring continues |
| Domain 48 — Criminal Justice / Civic Exclusion | COMPLETE | 08/01/2026 | M4BL Policy Table, Sentencing Project, Brennan Center, Worth Rises, NAACP LDF | LOW — entirely different network | CONDITIONAL | STRONG: prep begins June 25. MODERATE: prep begins July 1. WEAK: defer to July 15 |
| Domain 49 — Environmental Justice | COMPLETE | 08/15/2026 | Climate Justice Alliance, WE ACT, Earthjustice, IEN | LOW — different network | CONDITIONAL | STRONG: prep July 1. MODERATE: prep July 15. WEAK: defer to August |
| Domain 50 — LGBTQ+ Rights | COMPLETE | 08/01/2026 | Lambda Legal, AT4E, GLSEN, HRC, PFLAG National | LOW — different network | CONDITIONAL | STRONG: prep July 1. MODERATE: prep July 15. WEAK: prep July 15 regardless (hard deadline) |
| Domain 57 — Multilateral Withdrawal | COMPLETE | 08/10/2026 | HRW, Amnesty International, CFR, Senate Foreign Relations staff | LOW — international policy network | STANDBY | Fixed August 10 send regardless of T+7 determination |
| Domain 58 — Tribal Sovereignty | COMPLETE | Ruling-triggered | NARF, NCAI, Tribal Law and Policy Institute, IEN | LOW — rapid-response trigger | STANDBY | Trump v. Barbara ruling; independent of T+7 |

### T+7 Decision Routing (enter at checkpoint)

At T+7, read Sheet 5 Row 14 determination, then update column F and column K for each domain:

**If STRONG (≥4 STRONG signals)**:
- Domain 48: Update F8 to "ACTIVATE"; enter "Gist creation begins June 25, Tier 1 sends July 10–20" in K8
- Domain 49: Update F9 to "ACTIVATE — PREP"; enter "Preparation begins July 1" in K9
- Domain 50: Update F10 to "ACTIVATE — PREP"; enter "Preparation begins July 1; August 1 deadline immoveable" in K10

**If MODERATE (2–3 STRONG signals)**:
- Domain 48: Update F8 to "CONDITIONAL"; enter "Prep begins July 1 per Path B; use confirmed Phase 1 responses as social proof" in K8
- Domain 49: Update F9 to "CONDITIONAL"; enter "Prep begins July 15; compile social proof from confirmed responders first" in K9
- Domain 50: Update F10 to "ACTIVATE — PREP"; enter "Prep begins July 15 regardless; August 1 deadline does not flex" in K10

**If WEAK (<2 STRONG signals)**:
- Domain 48: Update F8 to "DEFER"; enter "Defer to July 15; conduct template revision before any sends" in K8
- Domain 49: Update F9 to "DEFER"; enter "Defer to August; D.C. Circuit window stays open" in K9
- Domain 50: Update F10 to "CONDITIONAL — MANDATORY"; enter "Defer preferred but August 1 deadline requires prep by July 15 regardless of engagement signal" in K10
- ALL domains: Enter in Sheet 6 Contingency Trigger Log: Trigger_Name "T+7 WEAK Determination"; Escalation_Action "Root-cause analysis: infrastructure vs. messaging gap; retain Domain 51 CA Wave 2 monitoring"

---

## One-Time Setup Sequence (complete before June 9)

1. Create sheet at sheets.new — 20 minutes total
2. Create 7 tabs with exact names: Daily Signal Log / Email Analytics / Engagement Classification / Decision Checkpoint Record / Cumulative Summary / Contingency Trigger Log / Phase 2 Batch Readiness Matrix
3. Copy column headers into Row 1 of each sheet exactly as specified above
4. Pre-populate Email Analytics with the 5 organization rows (already filled in above — copy directly)
5. Pre-populate Engagement Classification with 5 organization rows (A and B columns only; formulas go in C–I)
6. Pre-populate Decision Checkpoint Record with the 5 checkpoint dates
7. Pre-populate Phase 2 Batch Readiness Matrix with the 7 domain rows
8. Paste all formulas — test formula D4 in Cumulative Summary: it should return 0 before any data is entered in Sheet 1
9. Set sharing to "Anyone with the link can view" — paste URL into CHECKIN.md under "Wave 1 Dashboard URL"
10. On June 9 at 09:00 UTC: enter first SEND rows in Daily Signal Log — the dashboard is live

**Verification test before first send**: Enter one test row in Daily Signal Log (Date: today, Organization: CLC, Tier: A, Event_Type: SEND, Signal_Code: PENDING). Confirm that Sheet 3 Row 2 shows "PENDING" in column C and Sheet 5 Row 2 shows "1" in column B. Delete the test row after confirming.

---

*Prepared June 5, 2026. References: PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md (commit 8435be7f), PHASE_2_SEQUENTIAL_ACTIVATION_STRATEGY.md (commit 4f032d8d), DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md (June 5 verification), domain-51-send-templates.md.*
