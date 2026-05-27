---
title: "Phase 1 Measurement Spreadsheet Spec"
created: 2026-05-27
version: 1.0
status: production-ready
scope: >
  Complete schema for the 7-sheet Google Sheets tracking dashboard. Column definitions,
  data types, formulas, example rows, automated calculations, and permission model.
  Designed for a solo non-technical operator to set up in under 30 minutes.
word_count: ~1500
companion_files:
  - PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE.md
  - PHASE_1_MEASUREMENT_SYSTEM.md
  - PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md
setup_time: "25 minutes one-time; see Section 7"
---

# Phase 1 Measurement Spreadsheet Spec

**Version 1.0 — May 27, 2026**

This document specifies the complete schema for the Phase 1 tracking dashboard as a Google Sheet. PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE.md established the seven-sheet structure; this document fills in the gaps: precise column widths, validation rules, example data rows showing real patterns, and the automated calculations that remove manual arithmetic from the weekly check. A non-technical user should be able to replicate this from scratch in under 30 minutes using this spec.

The sheet exists in your personal Google account (wanka95@gmail.com). Sharing: "Anyone with the link can view." Post the URL in CHECKIN.md under "Dashboard URL" before the first wave send.

---

## Sheet 1: Contacts

**Tab name**: `Contacts`
**Row count at setup**: 45 data rows (one per Tier 1 contact) + 1 header row + 1 summary row at top

### Column Definitions

| Col | Header | Type | Width | Validation |
|-----|--------|------|-------|------------|
| A | Contact_ID | Text | 60 | Format C001–C045; auto-increment |
| B | Full_Name | Text | 160 | Last, First |
| C | Organization | Text | 200 | Institution name verbatim |
| D | Constituency | Text | 140 | Dropdown: Law School / Imm Legal Aid / Civil Rights / Academic / Faith / Labor / Mutual Aid |
| E | Email | Text | 200 | Verified address |
| F | Wave_Sent | Date | 80 | MM/DD/YYYY |
| G | Delivery_Status | Text | 100 | Dropdown: Delivered / Bounced / OOO / Unknown |
| H | First_Reply_Date | Date | 80 | Leave blank until reply |
| I | Reply_Score | Number | 60 | 1–5 only; blank if no reply |
| J | Referral_Source | Text | 160 | Name of person who referred this contact to us |
| K | Referral_Made | Text | 160 | Name of person/org this contact referred Phase 1 to |
| L | Adoption_Signal | Text | 300 | Free text; leave blank until confirmed |
| M | Adoption_Date | Date | 80 | Date signal confirmed |
| N | Survey_Sent | Date | 80 | Date Day 30 survey sent |
| O | Survey_Response | Text | 300 | Verbatim or "No response" |
| P | Notes | Text | 300 | Anything notable |

### Summary Row Formulas (Row 1, above headers)

Place these labels in column A, formulas in column B of the summary area:

```
Total contacts:             =COUNTA(A3:A200)-COUNTBLANK(A3:A200)
Delivered:                  =COUNTIF(G3:G200,"Delivered")
Bounced:                    =COUNTIF(G3:G200,"Bounced")
Any reply:                  =COUNTA(H3:H200)-COUNTBLANK(H3:H200)
Reply rate (any):           =IFERROR((COUNTA(H3:H200)-COUNTBLANK(H3:H200))/COUNTIF(G3:G200,"Delivered"),0)
Score 3+ replies:           =COUNTIF(I3:I200,">=3")
Score 3+ rate:              =IFERROR(COUNTIF(I3:I200,">=3")/COUNTIF(G3:G200,"Delivered"),0)
Total referrals made:       =COUNTA(K3:K200)-COUNTBLANK(K3:K200)
Adoption signals logged:    =COUNTA(L3:L200)-COUNTBLANK(L3:L200)
```

Format Score 3+ rate and Reply rate cells as percentage with 1 decimal place.

### Example Rows (showing real data patterns)

| C001 | Smith, Heather | Harvard Law School | Law School | hsmith@law.harvard.edu | 05/28/2026 | Delivered | 06/02/2026 | 3 | | | | | | | Forwarded to election law clinic coordinator |
| C002 | Johnson, Marcus | NILC | Imm Legal Aid | mjohnson@nilc.org | 05/28/2026 | Delivered | | | | | | | | | No reply as of Day 7 |
| C003 | Rivera, Elena | ACLU National | Civil Rights | erivera@aclu.org | 05/28/2026 | Bounced | | | | | | | | | Old address; check ACLU staff directory |

---

## Sheet 2: Gist_Views

**Tab name**: `Gist_Views`
**Purpose**: Weekly Bitly click tracking per Gist link

### Column Definitions

| Col | Header | Type | Notes |
|-----|--------|------|-------|
| A | Week_Number | Integer | 1 = May 28–June 3; increment each Monday |
| B | Week_End_Date | Date | Sunday of that week |
| C | DRP_Proposal_Clicks | Integer | bit.ly/drp-2026 weekly clicks |
| D | DRP_Summary_Clicks | Integer | bit.ly/drp-summary weekly clicks |
| E | DRP_Litigation_Clicks | Integer | bit.ly/drp-litigation weekly clicks |
| F | Domain37_Clicks | Integer | Domain 37 Gist short link |
| G | Domain56_Clicks | Integer | https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f short link |
| H | Domain39_Clicks | Integer | https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b short link |
| I | Total_Week | Formula | =SUM(C2:H2) — auto-calculates |
| J | Cumulative | Formula | =SUM($I$2:I2) — running total |
| K | Spike_Flag | Formula | =IF(MAX(C2:H2)>=5,"FLAG","") |
| L | Spike_Notes | Text | Manual: which link, which day, possible cause |

### Bitly Tracking Note

GitHub does not expose anonymous Gist view counts via API. Bitly free tier provides weekly and daily click counts per short link. The weekly check (Monday morning) reads the previous 7 days from the Bitly dashboard. For Domain 56 and Domain 39 Gists, create Bitly short links before the first send and embed those short links (not the raw GitHub Gist URLs) in all outreach emails.

If a Bitly account is not yet created: go to bit.ly, create a free account under wanka95@gmail.com, and create one custom short link per Gist. Custom back-halves (e.g., bit.ly/drp-d56) make the dashboard entries self-documenting.

**Fallback if Bitly is not set up before May 28**: Use the raw Gist URL in emails, then set up Bitly in the first week and note that Week 1 click data is unavailable. Begin Bitly tracking from Week 2. Do not let a missing Bitly account delay the May 28 send.

### Target Clicks by Week

| Week | Cumulative Target | Status if Below |
|------|-------------------|-----------------|
| 1 | 15 | MONITOR |
| 2 | 25 | MONITOR if 10-24; ESCALATE if <10 |
| 4 | 50 | WEAK signal if below |
| 8 | 100 | Below target — user decision required |

### Example Data Row (Week 1 strong performance)

| 1 | 06/03/2026 | 4 | 7 | 2 | 3 | 5 | 2 | 23 | 23 | FLAG | Domain 56 spike June 1 — aligns with Domain 39 June 1 send |

---

## Sheet 3: Replies

**Tab name**: `Replies`
**Purpose**: One row per substantive reply. Supplement to the score column in Contacts; captures reply content for trend analysis.

### Column Definitions

| Col | Header | Type | Notes |
|-----|--------|------|-------|
| A | Reply_ID | Text | R001, R002, etc. |
| B | Contact_ID | Text | Cross-ref to Contacts sheet |
| C | Reply_Date | Date | |
| D | Reply_Score | Number | 1–5 |
| E | Reply_Type | Text | Dropdown: OOO / Ack / Question / Forward / Adoption / Referral / Decline |
| F | Constituency | Text | Auto-fill from Contacts via VLOOKUP (see formula below) |
| G | Domain_Referenced | Text | Which domain(s) they mentioned, if any |
| H | Forward_Target | Text | If they forwarded — to whom / what organization |
| I | Adoption_Statement | Text | Verbatim quote if they stated intent to use |
| J | Follow_Up_Required | Text | Dropdown: Yes / No / Sent |
| K | Notes | Text | Free text |

### Auto-Fill Formula for Constituency (Column F)

```
=IFERROR(VLOOKUP(B2,Contacts!A:D,4,FALSE),"")
```

Place this in F2 and drag down. It pulls the constituency label from the Contacts sheet based on Contact_ID match.

### Example Rows

| R001 | C001 | 06/02/2026 | 3 | Question | Law School | Domain 29 | | | Yes | "What's your methodology for identifying prosecutorial weaponization patterns?" |
| R002 | C007 | 06/03/2026 | 4 | Forward | Imm Legal Aid | Domain 29, Domain 37 | CLINIC (Catholic Immigration) | "Plan to share with our amicus brief team" | Yes | Strong signal — CLINIC not on Tier 1 list; potential network event |
| R003 | C022 | 06/05/2026 | 1 | OOO | Labor | | | | No | Auto-reply; no human follow-up |

---

## Sheet 4: Adoptions

**Tab name**: `Adoptions`
**Purpose**: Formal registry of confirmed and probable adoption events. This sheet drives the Day 30 and Day 60 checkpoint calculations.

### Column Definitions

| Col | Header | Type | Notes |
|-----|--------|------|-------|
| A | Signal_ID | Text | AS001, AS002, etc. |
| B | Detected_Date | Date | |
| C | Organization | Text | |
| D | Constituency | Text | One of 7 |
| E | Signal_Type | Text | Dropdown: Curriculum / Litigation Toolkit / Policy Brief / Training Module / Governance Doc / Citation / Other |
| F | Domain_Refs | Text | Which domains adopted |
| G | Evidence_Source | Text | Dropdown: Reply Email / Survey / Web Detection / PACER / Direct Confirmation |
| H | Verification | Text | Dropdown: Confirmed / Probable / Unconfirmed |
| I | People_Reached | Integer | Estimate of how many people trained/exposed |
| J | Network_Event | Text | Dropdown: YES / NO |
| K | Description | Text | 1–2 sentences |

### Automated Summary Calculations (add below data, labeled)

```
Confirmed adoptions:     =COUNTIF(H2:H200,"Confirmed")
Probable adoptions:      =COUNTIF(H2:H200,"Probable")
People reached (est.):   =SUM(I2:I200)
Network events:          =COUNTIF(J2:J200,"YES")

Day 60 adoption gate:    =IF(COUNTIF(H2:H200,"Confirmed")>=15,"THRESHOLD MET","Need "&(15-COUNTIF(H2:H200,"Confirmed"))&" more")
Day 60 people gate:      =IF(SUM(I2:I200)>=100,"THRESHOLD MET","Need "&(100-SUM(I2:I200))&" more")
```

### Example Row

| AS001 | 06/08/2026 | NILC | Imm Legal Aid | Litigation Toolkit | Domain 29 | Reply Email | Probable | 12 | NO | NILC staff attorney stated intent to adapt model brief language for pending Ninth Circuit amicus |

---

## Sheet 5: Constituencies

**Tab name**: `Constituencies`
**Purpose**: Decision-facing view. One row per constituency (7 rows). This is the sheet you read during checkpoint reviews.

### Column Definitions

| Col | Header | Formula/Type | Notes |
|-----|--------|--------------|-------|
| A | Constituency | Text | Fixed labels |
| B | Total_Contacts | Formula | =COUNTIF(Contacts!D:D,A2) |
| C | Delivered | Formula | =COUNTIFS(Contacts!D:D,A2,Contacts!G:G,"Delivered") |
| D | Any_Reply | Formula | =COUNTIFS(Contacts!D:D,A2,Contacts!I:I,">0") |
| E | Score3Plus | Formula | =COUNTIFS(Contacts!D:D,A2,Contacts!I:I,">=3") |
| F | Score3Plus_Rate | Formula | =IFERROR(E2/C2,0) — format as % |
| G | Day7_Status | Text | Manual: PASS / MONITOR / FAIL per Section 4 thresholds |
| H | Day14_Status | Text | Manual: ON TRACK / MONITOR / BELOW BASELINE |
| I | Day30_Strong | Text | Manual: YES / NO |
| J | Day30_Moderate | Text | Manual: YES / NO |
| K | Adoptions | Formula | =COUNTIFS(Adoptions!D:D,A2,Adoptions!H:H,"Confirmed") |
| L | People_Reached | Formula | =SUMIF(Adoptions!D:D,A2,Adoptions!I:I) |
| M | Network_Events | Formula | =COUNTIFS(Adoptions!D:D,A2,Adoptions!J:J,"YES") |
| N | Status_Note | Text | Free text: key developments |

### Overall Gate Formulas (row below the 7 constituency rows)

```
Constituencies at Day30 Strong:    =COUNTIF(I2:I8,"YES")
Phase 2 STRONG trigger:            =IF(COUNTIF(I2:I8,"YES")>=4,"STRONG — ACTIVATE PHASE 2","Below STRONG: "&COUNTIF(I2:I8,"YES")&" of 4 required")
Phase 2 MODERATE trigger:          =IF(COUNTIF(J2:J8,"YES")>=3,"MODERATE — ACTIVATE D39","Below MODERATE: "&COUNTIF(J2:J8,"YES")&" of 3 required")
```

---

## Sheet 6: Checkpoints

**Tab name**: `Checkpoints`
**Purpose**: Append-only log of each formal checkpoint assessment. Do not edit past rows.

### Column Definitions

| Col | Header | Type | Notes |
|-----|--------|------|-------|
| A | Assessment_Date | Date | Actual date run |
| B | Checkpoint_Type | Text | Day 7 / Day 14 / Day 30 / Day 60 / Ad Hoc |
| C | Overall_Reply_Rate | Percent | Calculated at assessment time |
| D | Score3Plus_Rate | Percent | Calculated at assessment time |
| E | Constituencies_Strong | Integer | Count of 7 passing strong threshold |
| F | Cross_Org_Refs | Integer | Referral events at assessment time |
| G | Confirmed_Adoptions | Integer | From Adoptions sheet |
| H | People_Reached | Integer | From Adoptions sheet |
| I | Determination | Text | STRONG / MODERATE / WEAK / TOO_EARLY / FAILURE |
| J | Phase2_Decision | Text | Action taken |
| K | Notes | Text | Context, anomalies |

---

## Sheet 7: Synthesis_Log

**Tab name**: `Synthesis_Log`
**Purpose**: Weekly synthesis entries (from PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md). One row per weekly synthesis. This replaces the "Engagement Timeline" tab from PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE.md with a higher-level view more appropriate for solo operator use.

### Column Definitions

| Col | Header | Type | Notes |
|-----|--------|------|-------|
| A | Week_Number | Integer | 1 = May 28 – June 3 |
| B | Synthesis_Date | Date | Date synthesis was run |
| C | Gist_Views_Week | Integer | Total Bitly clicks this week |
| D | Gist_Views_Cumulative | Integer | Running total from Gist_Views sheet |
| E | New_Replies | Integer | Count of new replies this week |
| F | Score3Plus_New | Integer | New Score 3+ replies this week |
| G | Adoption_Events_New | Integer | New Probable or Confirmed events this week |
| H | Tier2_Candidates | Text | Names of any contacts showing Score 4-5 signals suitable for Tier 2 social proof |
| I | Risk_Signals | Text | Any concerns flagged this week |
| J | Decision_Status | Text | HOLD / MONITOR / ESCALATE / ACTIVATE |
| K | Next_Actions | Text | 1-3 specific actions before next synthesis |

---

## Permission Controls

**What the solo operator can do**:
- Edit all sheets at any time
- Add new rows to any sheet
- Change formulas to fix calculation errors
- Change Determination cells in Checkpoints sheet after re-evaluation

**What requires external data** (cannot be auto-calculated from the sheet alone):
- Bitly click counts (must be pulled from bitly.com/a/dashboard)
- Reply scores (requires reading each reply email and applying the 5-level scale)
- Adoption verification status (requires external confirmation beyond the original email thread)
- People_Reached estimates (requires reasonable judgment about organization size / training capacity)
- Web detection events (requires Google Alerts monitoring and occasional manual SSRN or PACER check)

**External data that does not feed the sheet**:
- Raw email open rates (Gmail does not provide these; Bitly clicks are the proxy)
- Forwarding chain data beyond one hop (you can see when someone says "I forwarded this" but cannot track the downstream click)
- Organic social media mentions (captured in Google Alerts only if content is indexed)

---

## 30-Minute Setup Checklist

Complete before Wave 1 sends (May 28):

1. Create Google Sheet titled: `Phase 1 Impact Dashboard — May 28, 2026`
2. Rename the 7 default sheet tabs: Contacts, Gist_Views, Replies, Adoptions, Constituencies, Checkpoints, Synthesis_Log
3. Build Contacts sheet: enter 45 contacts from DISTRIBUTION_OUTREACH_CONTACTS.md; set Column D dropdown validation (7 constituency values); set Column G dropdown validation (4 delivery status values) — time: 20 minutes
4. Add summary row formulas to Contacts sheet — time: 3 minutes
5. Build Gist_Views header row and target-click reference table — time: 2 minutes
6. Set sharing to "Anyone with the link can view"
7. Copy share URL and paste in CHECKIN.md under "Dashboard URL"

Total: approximately 25-30 minutes, parallelizable with email template personalization.
