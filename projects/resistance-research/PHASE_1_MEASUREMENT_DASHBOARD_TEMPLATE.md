---
title: "Phase 1 Impact Measurement Dashboard Template — Domain 51 Wave 1"
subtitle: "Google Sheets Blueprint for June 2026 Measurement and T+7 Decision Gate"
created: "2026-06-05"
updated: "2026-06-14"
version: 2.0
status: production-ready
scope: >
  Google Sheets dashboard template for Domain 51 Phase 1 impact tracking. 7-sheet structure
  with formulas, data entry procedures, Bitly integration, and June 17-18 T+7 decision gate.
  Reflects June 14 execution reality: Wave 1 sends pending; T+7 checkpoint June 17-18.
wave_1_window: "June 14-15, 2026 (execute immediately)"
t7_checkpoint: "June 17-18, 2026"
contacts_covered: 5
organizations: "CLC / Issue One / Common Cause CA / LWV CA / Clean Money Action Fund"
companion_files:
  - DAILY_SIGNAL_LOG_ENTRY_GUIDE.md
  - T7_CHECKPOINT_DECISION_AUTOMATION.md
  - DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md
  - PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md
setup_time: "20 minutes one-time; 10 minutes/week ongoing"
---

# Phase 1 Impact Measurement Dashboard Template
## Domain 51 Wave 1 — Google Sheets Blueprint

**Version 2.0 — Updated June 14, 2026**

**Situation as of June 14**: Wave 1-2 emails have not yet been sent. The June 17-18 T+7 checkpoint date is fixed. If emails go out June 14-15, T+7 falls on June 21-22. If the checkpoint is treated as calendar-fixed (June 17-18) regardless of send date, the data window is compressed but still valid for making a go/caution/no-go Phase 2 routing decision. Use June 17-18 as the earliest checkpoint; use June 21-22 as the standard T+7 window if sends execute June 14-15.

**Dashboard purpose**: Single source of truth for the five Domain 51 contacts across the Wave 1-2 outreach cycle. All Phase 2 domain activation decisions read from this dashboard. The dashboard is read-only for the orchestrator; only the user enters data.

**Permission model**: Create the sheet in your personal Google account (wanka95@gmail.com). Set sharing to "Anyone with the link can view." Copy the share URL to CHECKIN.md under the heading "Wave 1 Dashboard URL." Do not grant edit access to external parties.

**Zero-setup time**: 20 minutes to build and pre-populate before first send.

---

## Sheet Tab Order (left to right)

1. Daily Signal Log
2. Email Analytics
3. Engagement Classification
4. Decision Checkpoint Record
5. Cumulative Summary
6. Contingency Trigger Log
7. Phase 2 Batch Readiness Matrix

Create exactly these 7 tabs with these exact names. Formulas reference sheet names as written here — any variation will break cross-sheet lookups.

---

## Sheet 1: Daily Signal Log

**Purpose**: Primary data entry sheet. One row per contact event (send, reply, bounce, OOO, Gist click). Fill in manually as events occur. This is the source table for all formulas in Sheets 3, 4, and 5. Never delete or edit past rows — append only.

**When to enter a row**: Every external event. Sends, replies, bounces, Gist click spikes, OOO messages, follow-up sends. Do not log internal actions (drafting, file edits, calendar reminders).

### Column Structure

| Col | Header | Data Type | Allowed Values |
|-----|--------|-----------|----------------|
| A | Date | Date | MM/DD/YYYY |
| B | Organization | Text | CLC / Issue One / Common Cause CA / LWV CA / Clean Money |
| C | Tier | Text | A / B / C |
| D | Event_Type | Text | SEND / REPLY / BOUNCE / OOO / FOLLOW_UP / GIST_CLICK / NOTE |
| E | Signal_Code | Text | STRONG / MODERATE / WEAK / PENDING / N/A |
| F | Contact_Name | Text | Named individual or "Unknown" if general inbox |
| G | Channel | Text | EMAIL / GIST / PHONE / OTHER |
| H | Notes | Text | Free text — verbatim quote, observation, or context |

### Header Row (paste into Row 1 exactly)

```
Date | Organization | Tier | Event_Type | Signal_Code | Contact_Name | Channel | Notes
```

### Pre-Staged Send Rows (paste into Rows 2-6 before first send; update Signal_Code when outcome known)

| Date | Organization | Tier | Event_Type | Signal_Code | Contact_Name | Channel | Notes |
|------|--------------|------|------------|-------------|--------------|---------|-------|
| [send date] | CLC | A | SEND | PENDING | Erin Chlopak | EMAIL | Email 4 sent to echlopak@campaignlegalcenter.org |
| [send date] | Issue One | A | SEND | PENDING | Nick Penniman | EMAIL | Email 5 sent to info@issueone.org |
| [send date] | Common Cause CA | B | SEND | PENDING | Darius Kemp | EMAIL | Email 1 sent to dkemp@commoncause.org |
| [send date] | LWV CA | B | SEND | PENDING | Jenny Farrell | EMAIL | Email 2 sent to lwvc@lwvc.org |
| [send date] | Clean Money | C | SEND | PENDING | Trent Lange | EMAIL | Email 3 sent to info@CAclean.org |

Fill in [send date] with the actual date each email is sent. Replace PENDING with STRONG / MODERATE / WEAK when the outcome is known. See DAILY_SIGNAL_LOG_ENTRY_GUIDE.md for the complete per-organization decision tree.

### Signal Code Entry Rules

- Enter PENDING on every SEND row
- Do not edit a row once Signal_Code is set to STRONG or MODERATE — add a new row instead
- If a contact escalates after initial WEAK (e.g., OOO then substantive reply), add a new row; annotate the escalation in column H
- GIST_CLICK rows: enter MODERATE as Signal_Code (click confirms delivery but not substantive engagement)
- NOTE rows: enter N/A as Signal_Code (informational only)

---

## Sheet 2: Email Analytics

**Purpose**: Per-organization email delivery metrics and Bitly/Gist engagement. Update weekly — 5 minutes. This sheet provides the raw click data that feeds Sheet 5 Row 12 (Gist Total Clicks).

**Gist URL for Domain 51**: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372 (confirmed live June 5, 2026 — verify accessibility before first send)

**Bitly setup**: Before sending, shorten the Gist URL at bitly.com. Use the custom back-half `domain51-d51` or similar. Bitly free tier tracks up to 10 links, 30 days of click history, no scripts needed. Log in weekly and read click counts.

### Column Structure

| Col | Header | Data Type | Notes |
|-----|--------|-----------|-------|
| A | Organization | Text | 5 orgs + one TOTAL row |
| B | Contact_Email | Text | Verified send address |
| C | Template_Sent | Text | Email 1 / 2 / 3 / 4 / 5 |
| D | Send_Date | Date | Actual send date |
| E | Delivery_Status | Text | Delivered / Bounced / Unknown |
| F | Bounce_Reason | Text | Leave blank if delivered |
| G | Gist_Clicks_Week1 | Number | Bitly clicks, Days 1-7 post-send |
| H | Gist_Clicks_Week2 | Number | Bitly clicks, Days 8-14 |
| I | Gist_Clicks_Total | Formula | =G+H |
| J | Est_Open_Rate_Pct | Number | 100 if reply confirmed, 50 if Gist click only, 0 if no signal |
| K | Reply_Received | Text | YES / NO |
| L | Reply_Date | Date | Date of first reply |
| M | Notes | Text | Anomalies, bounce codes, alternate addresses tried |

### Pre-Populated Organization Rows (copy into Rows 2-7)

| Organization | Contact_Email | Template | Send_Date | Delivery_Status | Bounce_Reason | Gist_W1 | Gist_W2 | Gist_Total | Est_Open_% | Reply? | Reply_Date | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CLC | echlopak@campaignlegalcenter.org | Email 4 | | | | | | =G2+H2 | | | | Backup: info@campaignlegal.org |
| Issue One | info@issueone.org | Email 5 | | | | | | =G3+H3 | | | | |
| Common Cause CA | dkemp@commoncause.org | Email 1 | | | | | | =G4+H4 | | | | Backup: ca@commoncause.org |
| LWV CA | lwvc@lwvc.org | Email 2 | | | | | | =G5+H5 | | | | |
| Clean Money | info@CAclean.org | Email 3 | | | | | | =G6+H6 | | | | Verify at yesfairelections.org day-of |
| **TOTAL** | | | | =COUNTIF(E2:E6,"Delivered") | | =SUM(G2:G6) | =SUM(H2:H6) | =SUM(I2:I6) | =AVERAGE(J2:J6) | =COUNTIF(K2:K6,"YES") | | |

### Bitly Click Integration

Bitly provides daily click counts per link in the dashboard (bitly.com/a/dashboard). No API or script required. Weekly procedure:
1. Log in to Bitly
2. Click the Domain 51 short link
3. Select "Clicks" tab, set date range to "Last 14 days"
4. Sum clicks for Days 1-7 and enter in column G; sum Days 8-14 in column H
5. Check for single-day spikes (5+ clicks in one day) — these indicate a specific reader or forwarded link

**Spike detection**: A single-day spike of 5+ clicks means someone forwarded your link to a group. Cross-reference the spike date with your send dates. If the spike occurs 24-72 hours after a send, it confirms delivery and click-through to a team, not just an individual.

---

## Sheet 3: Engagement Classification

**Purpose**: One row per organization. Aggregates signal codes from Sheet 1 into a per-contact engagement status. Formula-driven — do not manually enter data except in column A (Organization) and B (Tier).

### Column Structure

| Col | Header | Formula / Type | Notes |
|-----|--------|----------------|-------|
| A | Organization | Text | Static — enter once |
| B | Tier | Text | Static — A, B, or C |
| C | Latest_Signal_Code | Formula | Most recent non-PENDING signal from Sheet 1 |
| D | STRONG_Count | Formula | Count of STRONG signals for this org |
| E | MODERATE_Count | Formula | Count of MODERATE signals for this org |
| F | WEAK_Count | Formula | Count of WEAK signals for this org |
| G | Status | Formula | Confirmed / Considering / Pass / Pending |
| H | Last_Updated | Formula | Most recent date from Sheet 1 for this org |
| I | Notes | Text | Qualitative context — enter manually when relevant |

### Static Rows (pre-populate columns A and B)

| A — Organization | B — Tier |
|---|---|
| CLC | A |
| Issue One | A |
| Common Cause CA | B |
| LWV CA | B |
| Clean Money | C |

### Formula Templates (paste into the appropriate columns, row 2 = CLC)

**Column C — Latest Signal Code** (most recent non-PENDING signal for this org):
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

**Column G — Status**:
```
=IF(D2>=1,"Confirmed",IF(E2>=1,"Considering",IF(F2>=1,"Pass","Pending")))
```

Logic: Any STRONG signal = Confirmed. No STRONG but MODERATE present = Considering. Only WEAK = Pass. No signals = Pending.

**Column H — Last Updated**:
```
=IFERROR(
  TEXT(MAX(FILTER('Daily Signal Log'!A:A,'Daily Signal Log'!B:B=A2)),"MM/DD/YYYY"),
"No events")
```

### Example State After T+7 (MODERATE scenario)

| Organization | Tier | Latest_Signal | STRONG | MODERATE | WEAK | Status |
|---|---|---|---|---|---|---|
| CLC | A | STRONG | 2 | 0 | 0 | Confirmed |
| Issue One | A | STRONG | 1 | 1 | 0 | Confirmed |
| Common Cause CA | B | MODERATE | 0 | 1 | 1 | Considering |
| LWV CA | B | MODERATE | 0 | 1 | 0 | Considering |
| Clean Money | C | WEAK | 0 | 0 | 1 | Pass |

In this scenario: B4 in Sheet 5 = 3 STRONG signals → MODERATE determination → conditional Phase 2 approval.

---

## Sheet 4: Decision Checkpoint Record

**Purpose**: Permanent audit trail of each formal checkpoint assessment. Append-only — never edit past rows. This is what you look at to reconstruct the decision history.

**Checkpoints for Domain 51 Wave 1**:
- T+3: June 17-18 (3 days after June 14-15 send) — delivery confirmation only
- T+7: June 21-22 (7 days after June 14-15 send) — Phase 2 gate decision
- T+14: June 28-29 — calibration, late reply assessment
- T+30: July 14-15 — full engagement assessment
- T+45: July 29-30 — campaign integration confirmation

**If sends go out earlier (before June 14)**: Adjust all checkpoint dates by the actual Wave 1 send date. The June 17-18 calendar date is treated as the earliest T+7 regardless.

### Column Structure

| Col | Header | Data Type | Notes |
|-----|--------|-----------|-------|
| A | Checkpoint_Date | Date | Actual date assessment was run |
| B | Checkpoint_Label | Text | T+3 / T+7 / T+14 / T+30 / T+45 |
| C | Days_Since_Wave1 | Formula | =A2-[actual send date] |
| D | STRONG_Signals | Number | Count from Sheet 5, Row B4, at time of assessment |
| E | MODERATE_Signals | Number | Count from Sheet 5, Row B5 |
| F | WEAK_Signals | Number | Count from Sheet 5, Row B6 |
| G | Confirmed_Count | Number | Count from Sheet 3, Column G, "Confirmed" |
| H | Determination | Text | STRONG / MODERATE / WEAK — per T7_CHECKPOINT_DECISION_AUTOMATION.md thresholds |
| I | Phase_2_Action | Text | Explicit action triggered (e.g., "Domain 48 prep begins July 1") |
| J | Decision_Branch | Text | Branch taken in T7_CHECKPOINT_DECISION_AUTOMATION.md |
| K | Notes | Text | Anomalies, caveats, root-cause if WEAK |

### Pre-Staged Checkpoint Rows

Paste these into rows 2-6 with dates adjusted to actual send date:

| Checkpoint_Date | Label | Days | STRONG | MODERATE | WEAK | Confirmed | Determination | Phase_2_Action | Branch | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| [send+3] | T+3 | | | | | | | Delivery confirmation only | | |
| [send+7] | T+7 | | | | | | | See T7_CHECKPOINT_DECISION_AUTOMATION.md | | |
| [send+14] | T+14 | | | | | | | Late reply assessment | | |
| [send+30] | T+30 | | | | | | | Full engagement assessment | | |
| [send+45] | T+45 | | | | | | | Campaign integration check | | |

### Notes for T+3 Assessment (delivery confirmation)

At T+3, the only question is: did the emails reach inboxes?
- Check for bounce-back notifications in sent mail
- Check Bitly click count (any clicks at all = delivery confirmed)
- If CLC or Issue One bounced: re-send to backup address immediately (see Email Analytics sheet)
- If Zero clicks AND zero replies AND no bounces: spam filter likely — check with a test send

---

## Sheet 5: Cumulative Summary

**Purpose**: The primary decision-facing dashboard. Read this sheet during checkpoint assessments. All numbers are formula-driven from Sheet 1 — no manual entry needed after formulas are installed.

**The single number that drives the T+7 decision**: Cell B4 (Total STRONG Signals) and Cell B14 (T7 Gate Status). Read B14 first. See T7_CHECKPOINT_DECISION_AUTOMATION.md for routing logic.

### Metrics Table (Rows 2-14)

| Row | A — Metric | B — Formula (Current_Value) | C — T7 Target | D — T30 Target |
|-----|-----------|------------------------------|---------------|----------------|
| 2 | Total Contacts Reached | =COUNTIF('Daily Signal Log'!D:D,"SEND") | 5 | 5 |
| 3 | Confirmed Delivered | =COUNTIFS('Daily Signal Log'!D:D,"SEND",'Daily Signal Log'!E:E,"<>WEAK") | 5 | 5 |
| 4 | Total STRONG Signals | =COUNTIF('Daily Signal Log'!E:E,"STRONG") | 2 | 4 |
| 5 | Total MODERATE Signals | =COUNTIF('Daily Signal Log'!E:E,"MODERATE") | 1 | 2 |
| 6 | Total WEAK Signals | =COUNTIF('Daily Signal Log'!E:E,"WEAK") | — | — |
| 7 | Confirmed Orgs | =COUNTIF('Engagement Classification'!G:G,"Confirmed") | 1 | 3 |
| 8 | Considering Orgs | =COUNTIF('Engagement Classification'!G:G,"Considering") | 1 | 1 |
| 9 | Pass / No Response | =COUNTIF('Engagement Classification'!G:G,"Pass") | — | — |
| 10 | Response Rate % | =B7/B2 | 20% | 60% |
| 11 | STRONG Signal Rate % | =B4/B2 | 40% | 80% |
| 12 | Gist Total Clicks | =SUM('Email Analytics'!I:I) | 5 | 20 |
| 13 | Days Since First Send | =TODAY()-MIN(FILTER('Daily Signal Log'!A:A,'Daily Signal Log'!D:D="SEND")) | — | — |
| 14 | T7 Gate Status | =IF(B4>=4,"STRONG — ACTIVATE PHASE 2",IF(B4>=2,"MODERATE — CONDITIONAL APPROVAL","WEAK — DEFER AND DIAGNOSE")) | ≥4 STRONG | — |

### Status Column (Column E) Formulas

```
Row 2:  =IF(B2>=C2,"THRESHOLD MET","ON TRACK")
Row 3:  =IF(B3>=C3,"THRESHOLD MET","BELOW TARGET")
Row 4:  =IF(B4>=C4,"THRESHOLD MET",IF(B4>=1,"ON TRACK","BELOW TARGET"))
Row 7:  =IF(B7>=C7,"THRESHOLD MET",IF(B7>=1,"ON TRACK","BELOW TARGET"))
Row 10: =IF(B10>=0.2,"THRESHOLD MET",IF(B10>=0.1,"ON TRACK","BELOW TARGET"))
Row 14: =B14  [this is the gate text — formula in B14 already includes full text]
```

### Per-Organization Signal Block (Rows 16-22)

Add this table below the main metrics block for the per-org breakdown used at T+7:

| Row | A — Organization | B — STRONG | C — MODERATE | D — WEAK | E — Status |
|-----|---|---|---|---|---|
| 16 | [Header] | STRONG | MODERATE | WEAK | Status |
| 17 | CLC | =COUNTIFS('Daily Signal Log'!B:B,"CLC",'Daily Signal Log'!E:E,"STRONG") | =COUNTIFS('Daily Signal Log'!B:B,"CLC",'Daily Signal Log'!E:E,"MODERATE") | =COUNTIFS('Daily Signal Log'!B:B,"CLC",'Daily Signal Log'!E:E,"WEAK") | ='Engagement Classification'!G2 |
| 18 | Issue One | [same pattern] | | | ='Engagement Classification'!G3 |
| 19 | Common Cause CA | [same pattern] | | | ='Engagement Classification'!G4 |
| 20 | LWV CA | [same pattern] | | | ='Engagement Classification'!G5 |
| 21 | Clean Money | [same pattern] | | | ='Engagement Classification'!G6 |
| 22 | TOTAL | =SUM(B17:B21) | =SUM(C17:C21) | =SUM(D17:D21) | =B14 |

**Reading the per-org block at T+7**: Row 22 Column B is the same as Cell B4. Row 22 Column E shows the gate status. The per-org rows tell you which specific organizations produced the STRONG signals — this determines which social proof you can use in Phase 2 outreach templates.

---

## Sheet 6: Contingency Trigger Log

**Purpose**: Alert tracking for pre-defined contingency thresholds. Log a row when a contingency threshold is crossed, even if no action is immediately taken. This sheet is the paper trail for any non-standard events.

### Column Structure

| Col | Header | Notes |
|-----|--------|-------|
| A | Alert_Date | Date threshold was crossed |
| B | Checkpoint_Context | T+3 / T+7 / T+14 / T+30 / T+45 |
| C | Trigger_Name | Name of the contingency (from pre-populated list below) |
| D | Root_Cause | Infrastructure gap / Messaging gap / Timing issue / Org unavailable |
| E | Escalation_Action | Explicit action taken |
| F | Resolution_Date | Date issue was resolved or trigger closed |
| G | Status | Open / Resolved / Accepted |

### Pre-Populated Trigger Reference

Copy these rows as static reference data; update column G when triggered:

| Trigger_Name | Condition | Default Escalation_Action |
|---|---|---|
| CLC Bounce | echlopak@campaignlegalcenter.org bounces | Re-send immediately to info@campaignlegal.org; update Email Analytics Delivery_Status |
| Issue One No Gist Click by T+3 | Zero Bitly clicks from Issue One by Day 3 | Re-test Gist URL accessibility; confirm email link is clickable (not raw text) |
| CA Wave Zero Response by T+7 | No signal from Common Cause CA, LWV CA, or Clean Money by Day 7 | Send Wave 3 follow-up to Common Cause CA; see DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md Section 4 |
| Clean Money Email Invalid | info@CAclean.org bounces | Log "verification required"; do not delay other sends; verify at yesfairelections.org |
| T+7 WEAK Determination | STRONG signal count <2 at T+7 | Defer Phase 2 batch; run root-cause; retain Domain 51/59 monitoring |
| Gist URL Inaccessible | HTTP error on Gist URL | Check GitHub status; if >30 min outage, prepare PDF fallback and re-send |
| Phase 2 Trigger Conflict | STRONG T+7 but no execution bandwidth | Note constraint; move activation to next available window; do not drop the signal |

### Example Completed Row

| Alert_Date | Context | Trigger_Name | Root_Cause | Escalation_Action | Resolution_Date | Status |
|---|---|---|---|---|---|---|
| 06/14/2026 | Pre-send | CA Wave Zero Response by T+7 | Sends not yet executed — timing slip from June 9 | All 5 sends executed June 14-15; T+7 window shifts to June 21-22 | 06/15/2026 | Resolved |

---

## Sheet 7: Phase 2 Batch Readiness Matrix

**Purpose**: The T+7 decision output sheet. One row per Phase 2 domain. Updated at T+7 based on the Sheet 5 Row 14 determination. This is the go/no-go activation record for Phase 2.

**When to fill this in**: At T+7 checkpoint, after reading Sheet 5 Row 14 determination. Update column F (T7_Activation_Status) and column K (Notes) for each domain.

### Column Structure

| Col | Header | Notes |
|-----|--------|-------|
| A | Domain | Domain name and number |
| B | Research_Status | COMPLETE / IN PROGRESS |
| C | External_Deadline | Hard deadline for distribution |
| D | Coalition_Network | Primary target organizations |
| E | Wave1_Signal_Relevance | HIGH / MEDIUM / LOW — does D51 signal predict this domain's reception? |
| F | T7_Activation_Status | ACTIVATE / CONDITIONAL / DEFER / STANDBY |
| G | Activation_Trigger | What signal level activates this domain |
| H | If_STRONG | Action on STRONG determination |
| I | If_MODERATE | Action on MODERATE determination |
| J | If_WEAK | Action on WEAK determination |
| K | Notes | Current status and next steps (update at T+7) |

### Pre-Populated Domain Rows

| Domain | Status | Deadline | Coalition | Signal_Relevance | T7_Status | Trigger |
|---|---|---|---|---|---|---|
| Domain 59 — Economic Precarity / CTC | COMPLETE | 06/30/2026 | CBPP, ITEP, NWLC, MomsRising, AFL-CIO | MEDIUM | ACTIVATE | Already executing; T+7 does not gate this domain |
| Domain 51 — Campaign Finance | COMPLETE | 07/01/2026 | CLC, Issue One, Common Cause CA, LWV CA, Clean Money | HIGH | EXECUTING | This IS Wave 1; monitoring continues |
| Domain 48 — Criminal Justice / Civic Exclusion | COMPLETE | 08/01/2026 | M4BL, Sentencing Project, Brennan Center, Worth Rises, NAACP LDF | LOW | CONDITIONAL | STRONG: prep June 25. MODERATE: prep July 1. WEAK: defer to July 15 |
| Domain 49 — Environmental Justice | COMPLETE | 08/15/2026 | Climate Justice Alliance, WE ACT, Earthjustice, IEN | LOW | CONDITIONAL | STRONG: prep July 1. MODERATE: prep July 15. WEAK: defer to August |
| Domain 50 — LGBTQ+ Rights | COMPLETE | 08/01/2026 | Lambda Legal, AT4E, GLSEN, HRC, PFLAG National | LOW | CONDITIONAL | STRONG: prep July 1. MODERATE: prep July 15. WEAK: prep July 15 mandatory (hard deadline) |
| Domain 57 — Multilateral Withdrawal | COMPLETE | 08/10/2026 | HRW, Amnesty, CFR, Senate Foreign Relations staff | LOW | STANDBY | Fixed August 10 regardless of T+7 |
| Domain 58 — Tribal Sovereignty | COMPLETE | Ruling-triggered | NARF, NCAI, Tribal Law and Policy Institute, IEN | LOW | STANDBY | Trump v. Barbara ruling triggers; independent of T+7 |

### T+7 Decision Routing Instructions

At T+7, read Sheet 5 Row 14, then update column F and K for each domain:

**If STRONG (B4 ≥ 4 in Sheet 5)**:
- Domain 48: F = "ACTIVATE"; K = "Gist creation begins [send+11]; Tier 1 sends [send+25 through send+35]"
- Domain 49: F = "ACTIVATE — PREP"; K = "Preparation begins [send+17]"
- Domain 50: F = "ACTIVATE — PREP"; K = "Preparation begins [send+17]; August 1 deadline immoveable"
- Add social proof row: compile 2-3 sentence summary of STRONG replies for Phase 2 templates

**If MODERATE (B4 = 2-3 in Sheet 5)**:
- Domain 48: F = "CONDITIONAL"; K = "Prep begins [send+17] per standard Path B; use confirmed Phase 1 responses as social proof"
- Domain 49: F = "CONDITIONAL"; K = "Prep begins [send+31]; compile social proof first"
- Domain 50: F = "ACTIVATE — PREP"; K = "Prep begins [send+31] regardless; August 1 does not flex"

**If WEAK (B4 ≤ 1 in Sheet 5)**:
- Domain 48: F = "DEFER"; K = "Defer to [send+31]; conduct template revision before any sends"
- Domain 49: F = "DEFER"; K = "Defer to August; D.C. Circuit window stays open"
- Domain 50: F = "CONDITIONAL — MANDATORY"; K = "Defer preferred but August 1 deadline requires prep by [send+31] regardless"
- All domains: Log "T+7 WEAK Determination" in Sheet 6 Contingency Trigger Log

---

## One-Time Setup Procedure (20 minutes before first send)

1. Open sheets.new in Google Sheets
2. Rename the default tab to "Daily Signal Log"
3. Add 6 more tabs with exact names (right-click tab to rename or add):
   - Email Analytics
   - Engagement Classification
   - Decision Checkpoint Record
   - Cumulative Summary
   - Contingency Trigger Log
   - Phase 2 Batch Readiness Matrix
4. Copy each column header row (Row 1) from the sections above into the corresponding sheet
5. Pre-populate Email Analytics with the 5 organization rows (copy from this document)
6. Pre-populate Engagement Classification with 5 organization rows in columns A and B
7. Paste all formulas from the Formula Templates sections
8. Pre-populate Phase 2 Batch Readiness Matrix with the 7 domain rows
9. Pre-stage the 5 SEND rows in Daily Signal Log with [send date] placeholders
10. Set sharing: Share > "Anyone with the link" > "Viewer" — copy URL to CHECKIN.md

**Verification test**: Enter one test row in Daily Signal Log (Date: today, Org: CLC, Tier: A, Event_Type: SEND, Signal_Code: PENDING). Confirm Sheet 3 Row 2 shows "PENDING" and Sheet 5 Row 2 shows "1". Delete the test row after confirming.

---

## Weekly Update Checklist (10 minutes per week)

Run every Monday during Weeks 1-6 post-send:

**Step 1 — Email review (4 minutes)**
- Check Gmail for new replies from any of the 5 organizations
- Score each reply using DAILY_SIGNAL_LOG_ENTRY_GUIDE.md decision tree
- Enter in Daily Signal Log with correct Signal_Code
- If reply contains referral mention: note in column H

**Step 2 — Bitly click pull (3 minutes)**
- Log in to bitly.com, select Domain 51 link
- Record weekly click total in Email Analytics columns G or H
- Set spike flag if any single day had 5+ clicks

**Step 3 — Web monitoring (2 minutes)**
- Check Google Alerts for any mentions of Domain 51 research vocabulary
- Check for any new Gist access (GitHub authenticated view count if available)

**Step 4 — Dashboard update (1 minute)**
- Confirm Sheet 5 formulas are auto-calculating (they should be — no manual refresh needed)
- If any checkpoint date has passed, add row to Decision Checkpoint Record

**Total time**: 10 minutes per week.

---

## Bitly Campaign URL Integration

For each organization, creating a separate Bitly link (with different custom back-halves) allows you to attribute clicks to specific contacts. This is optional but improves signal precision:

| Organization | Suggested Bitly Back-Half | Purpose |
|---|---|---|
| CLC | d51-clc | Attribute CLC click-throughs |
| Issue One | d51-i1 | Attribute Issue One clicks |
| Common Cause CA | d51-ccca | Attribute CA ballot coalition clicks |
| LWV CA | d51-lwvca | Attribute LWV CA clicks |
| Clean Money | d51-cm | Attribute Clean Money clicks |
| General (all) | d51-main | Use in any publication or secondary distribution |

If you use per-organization links, update Email Analytics Column B with the specific Bitly link used, and update columns G and H with that organization's click data only. Sheet 5 Row 12 formula (`=SUM('Email Analytics'!I:I)`) will sum all links automatically.

---

*Version 2.0 — Updated June 14, 2026. Reflects June 14 execution state (Wave 1 sends pending). T+7 checkpoint June 17-18 per task specification, or June 21-22 if sends execute June 14-15. Sources: PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md, DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md (June 5 verification), DAILY_SIGNAL_LOG_ENTRY_GUIDE.md (June 5), T7_CHECKPOINT_DECISION_AUTOMATION.md.*
