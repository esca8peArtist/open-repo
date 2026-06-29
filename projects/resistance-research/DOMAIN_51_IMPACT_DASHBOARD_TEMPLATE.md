---
title: "Domain 51 — Wave 1-2 Impact Dashboard Template (Google Sheets)"
created: "2026-06-29"
status: "production-ready"
setup_time: "20 minutes one-time"
ongoing_time: "5-10 minutes per checkpoint"
contacts_covered: 5
organizations: "CLC / Issue One / Common Cause CA / LWV CA / Clean Money Action Fund"
companion_files:
  - DOMAIN_51_RESPONSE_MONITORING_PROTOCOL.md
  - DOMAIN_51_WAVE_2_ACTIVATION_DECISION_TREE.md
  - DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md
  - PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md
---

# Domain 51 — Wave 1-2 Impact Dashboard Template

## Google Sheets Build Guide + Copy-Paste Formulas

**Create this spreadsheet at**: sheets.new (auto-creates in your Google account at wanka95@gmail.com)

**Name it**: `Domain 51 — Response Tracking (June 2026)`

**Permission model**: Share as "Anyone with the link can view." Copy the share URL and paste it into CHECKIN.md under the heading "D51 Dashboard URL." Do not grant edit access.

**Build time**: 20 minutes to create all five sheets and pre-populate static rows. Each monitoring session thereafter takes 5-10 minutes.

---

## Sheet Structure — Create Exactly These Five Tabs

Create sheets in this order (left to right). Sheet names are case-sensitive — formulas reference them by exact name.

1. `Signal Log`
2. `Email Analytics`
3. `Metrics`
4. `Checkpoint Record`
5. `Wave 2 Readiness`

---

## Sheet 1: Signal Log

**Purpose**: Primary data entry. One row per event. Never edit past rows — append only. This is the source table that all formula sheets read from.

**When to add a row**: Every external event — sends, replies, bounces, OOO messages, Bitly click spikes. Do not log internal actions (drafting, file edits).

### Column Headers (paste into Row 1)

Paste this into Row 1, one value per column (A through H):

```
Date | Organization | Tier | Event_Type | Signal_Code | Contact_Name | Channel | Notes
```

Format column A as Date (MM/DD/YYYY). Leave all other columns as plain text.

### Allowed Values Per Column

| Column | Allowed Values |
|--------|---------------|
| D — Event_Type | SEND / REPLY / BOUNCE / OOO / GIST_CLICK / FOLLOW_UP / NOTE |
| E — Signal_Code | STRONG / MODERATE / COLD / BOUNCE / PENDING / N/A |
| B — Organization | CLC / Issue One / Common Cause CA / LWV CA / Clean Money |
| C — Tier | A / B / C |
| G — Channel | EMAIL / GIST / PHONE / OTHER |

### Pre-Staged Send Rows (paste into Rows 2-6 before first send)

Copy the table below into rows 2 through 6. Fill in the Date column with the actual send date when you execute each email. Leave Signal_Code as PENDING until you receive or confirm non-response.

| Date | Organization | Tier | Event_Type | Signal_Code | Contact_Name | Channel | Notes |
|------|--------------|------|------------|-------------|--------------|---------|-------|
| [CLC send date] | CLC | A | SEND | PENDING | Erin Chlopak | EMAIL | echlopak@campaignlegalcenter.org — Email 1 (Wave 1) |
| [Issue One send date] | Issue One | A | SEND | PENDING | Nick Penniman | EMAIL | info@issueone.org — Email 2 (Wave 1) |
| [CC CA send date] | Common Cause CA | B | SEND | PENDING | Darius Kemp | EMAIL | dkemp@commoncause.org — Email 3 (Wave 2) |
| [LWV CA send date] | LWV CA | B | SEND | PENDING | Jenny Farrell | EMAIL | lwvc@lwvc.org — Email 4 (Wave 2) |
| [Clean Money send date] | Clean Money | C | SEND | PENDING | Trent Lange | EMAIL | info@CAclean.org — Email 5 (Wave 2) |

### Signal Code Entry Rules

- Every SEND row: Signal_Code = PENDING
- When a reply arrives: add a NEW row (do not edit the SEND row); Event_Type = REPLY; Signal_Code = STRONG / MODERATE / COLD
- OOO message: new row; Event_Type = OOO; Signal_Code = MODERATE
- Bitly click spike (3+ clicks in one day): new row; Event_Type = GIST_CLICK; Signal_Code = MODERATE; Notes = "X clicks on [date], attributed to [org send date]"
- Bounce: new row; Event_Type = BOUNCE; Signal_Code = BOUNCE; Notes = include bounce error code or reason
- Upgrade: if an org signals COLD then later replies STRONG, add a new REPLY row — do not edit the original SEND row

---

## Sheet 2: Email Analytics

**Purpose**: Per-organization delivery and click metrics. Update at each monitoring checkpoint. Source for open rate and click rate calculations in Sheet 3.

### Column Headers (paste into Row 1)

```
Organization | Contact_Email | Template | Send_Date | Delivery | Bounce_Reason | Gist_W1 | Gist_W2 | Gist_Total | Est_Open_Pct | Reply | Reply_Date | Notes
```

### Pre-Populated Organization Rows (paste into Rows 2-7)

Copy these rows into the sheet. Fill Send_Date when you actually send. Fill Delivery after 2-hour bounce check. Fill Gist_W1 and Gist_W2 from Bitly weekly.

**Rows 2-6 — Organization data**:

| Organization | Contact_Email | Template | Send_Date | Delivery | Bounce_Reason | Gist_W1 | Gist_W2 | Gist_Total | Est_Open_Pct | Reply | Reply_Date | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CLC | echlopak@campaignlegalcenter.org | Wave 1 Email 1 | | | | | | | | | | Backup: info@campaignlegal.org |
| Issue One | info@issueone.org | Wave 1 Email 2 | | | | | | | | | | |
| Common Cause CA | dkemp@commoncause.org | Wave 2 Email 3 | | | | | | | | | | Backup: ca@commoncause.org |
| LWV CA | lwvc@lwvc.org | Wave 2 Email 4 | | | | | | | | | | |
| Clean Money | info@CAclean.org | Wave 2 Email 5 | | | | | | | | | | Alt: Trent.Lange@CAclean.org |

**Row 7 — TOTAL row (paste formulas exactly as shown)**:

| TOTAL | | | | =COUNTIF(E2:E6,"Delivered") | | =SUM(G2:G6) | =SUM(H2:H6) | =SUM(I2:I6) | =AVERAGE(J2:J6) | =COUNTIF(K2:K6,"YES") | | |

### Formulas for Column I (Gist_Total) — paste into I2 through I6

```
=G2+H2
=G3+H3
=G4+H4
=G5+H5
=G6+H6
```

### Estimated Open % — Entry Rules (Column J)

Do not use a formula for this column. Enter manually based on the following logic:

- Enter `100` if a direct reply has been confirmed for this org (reply = confirmed open)
- Enter `75` if a Bitly click spike is attributed to this org's send date (probable open, unconfirmed)
- Enter `50` if an OOO reply was received (email reached inbox, open likely on return)
- Enter `0` if no signal (no reply, no attributed click) — this is COLD, not necessarily a non-open

---

## Sheet 3: Metrics

**Purpose**: Formula-driven summary metrics that update automatically as Signal Log data is entered. Read this sheet at each checkpoint. Do not enter data here manually except in highlighted cells.

### Core Metric Formulas — Paste Into These Cells

Create a clean layout with labels in column A and formula values in column B.

**Cell A1**: `Total Wave 1-2 Sends`
**Cell B1**: `=COUNTIF('Signal Log'!D:D,"SEND")`

**Cell A2**: `Delivery Confirmed (no bounce)`
**Cell B2**: `=COUNTIF('Signal Log'!E:E,"PENDING")+COUNTIFS('Signal Log'!D:D,"REPLY",'Signal Log'!E:E,"<>BOUNCE")`

Note: A simpler proxy — enter manually as 5 minus the count of BOUNCE rows in Signal Log.

**Cell A3**: `Total Replies Received`
**Cell B3**: `=COUNTIF('Signal Log'!D:D,"REPLY")`

**Cell A4**: `STRONG Signal Count`
**Cell B4**: `=COUNTIF('Signal Log'!E:E,"STRONG")`

**Cell A5**: `MODERATE Signal Count`
**Cell B5**: `=COUNTIF('Signal Log'!E:E,"MODERATE")`

**Cell A6**: `Reply Rate %`
**Cell B6**: `=IF(B1=0,0,ROUND((B3/B1)*100,1))`

**Cell A7**: `STRONG Rate %`
**Cell B7**: `=IF(B1=0,0,ROUND((B4/B1)*100,1))`

**Cell A8**: `Bitly Total Clicks (all orgs)`
**Cell B8**: `='Email Analytics'!I7`
(This reads from the TOTAL row Gist_Total cell in Sheet 2.)

**Cell A9**: `Estimated Open Rate %`
**Cell B9**: `='Email Analytics'!J7`
(This reads from the TOTAL row Est_Open_Pct average in Sheet 2.)

**Cell A10**: `24-Hour Velocity (replies in first 24h)`
**Cell B10**: Manual entry — count replies from Signal Log where Event_Type = REPLY and Date = send date or send date + 1

**Cell A11**: `T+7 Composite Score`
**Cell B11**: `=(B4*3)+(B5*1)`
(STRONG signals score 3 points each; MODERATE score 1 point each. Wave 2 activation threshold is 4+ points. See DOMAIN_51_WAVE_2_ACTIVATION_DECISION_TREE.md for score-to-action mapping.)

### Decision Trigger Display (Column D, Rows 1-5)

Paste these IF formulas in Column D. They display the current activation state based on live metric values.

**Cell D1** — Wave 2 Pre-Stage Trigger:
```
=IF(B9>=60,"TRIGGER: 60%+ est. open rate — pre-stage Wave 2 contacts NOW","Open rate below threshold — continue monitoring")
```

**Cell D2** — Positive Reply Escalation Trigger:
```
=IF(B4>=3,"TRIGGER: 3+ STRONG signals — escalation activation (see Wave 2 Decision Tree)","Below escalation threshold")
```

**Cell D3** — Low Response Contingency Trigger:
```
=IF(AND(B3=0,B8<3),"TRIGGER: 0 replies + <3 Gist clicks — activate PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md","No contingency required")
```

**Cell D4** — T+7 Gate Status:
```
=IF(B11>=4,"GO: Activate Wave 3 (score "&B11&" — threshold 4)",IF(B11>=2,"CONDITIONAL: Hold Wave 3 pending T+14 (score "&B11&")",IF(B11>=1,"HOLD: Low signal — monitor to T+14 (score "&B11&")","NO-GO: Activate contingency (score "&B11&")"))
```

**Cell D5** — PHASE_2 Integration Status:
```
=IF(B4>=2,"Phase 2 gate: PASS (2+ STRONG)",IF(B5>=3,"Phase 2 gate: CONDITIONAL (3+ MODERATE, no STRONG)","Phase 2 gate: PENDING — insufficient signal"))
```

---

## Sheet 4: Checkpoint Record

**Purpose**: Permanent audit trail of each formal checkpoint decision. Append-only. Never edit past rows.

### Column Headers (paste into Row 1)

```
Checkpoint | Date | T+N | STRONG | MODERATE | COLD | Composite_Score | Open_Rate_Pct | Gate_Decision | Action_Taken | Notes
```

### Pre-Staged Checkpoint Rows (paste into Rows 2-6, fill dates from actual send date)

These rows are pre-staged. Fill them in on the actual checkpoint date.

| Checkpoint | Date | T+N | STRONG | MODERATE | COLD | Composite | Open_% | Gate_Decision | Action_Taken | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Bounce Check | [send date] | T+0 | — | — | — | — | — | Delivery confirmed / Bounces noted | Log bounces; resend to backup addresses | |
| Day 3 Scan | [send date + 3] | T+3 | [ ] | [ ] | [ ] | — | — | No action / Early replies logged | — | |
| T+7 Primary Gate | [send date + 7] | T+7 | [ ] | [ ] | [ ] | [ ] | [ ] | GO / CONDITIONAL / HOLD / NO-GO | Wave 2/3 decision logged | Fill from Metrics sheet |
| T+14 Secondary Gate | [send date + 14] | T+14 | [ ] | [ ] | [ ] | [ ] | [ ] | — | Late reply catch; Wave 3 finalize | |
| T+30 Full Assessment | [send date + 30] | T+30 | [ ] | [ ] | [ ] | [ ] | [ ] | — | Full engagement count; note for Phase 2 batch sequencing | |

### Gate Decision Definitions

| Decision | Condition | Action |
|---|---|---|
| GO | Composite score 4+ (e.g., 1 STRONG + 1 MODERATE, or 2 STRONG) | Activate Wave 3 immediately; pre-stage Tier 2 contacts |
| CONDITIONAL | Composite score 2-3 | Activate Wave 3 with modified framing; monitor Tier 2 activation closely |
| HOLD | Composite score 1 | Do not activate Wave 3; extend monitoring to T+14 before deciding |
| NO-GO | Composite score 0 (0 replies, 0 click signal) | Activate PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md low-response path |

---

## Sheet 5: Wave 2 Readiness

**Purpose**: At-a-glance readiness state for the three Tier 2 contacts that represent the next send tranche if Wave 1-2 produces sufficient signal.

### Contact Readiness Matrix (static — enter once)

| Priority | Organization | Contact | Email | Activation Threshold | Status |
|---|---|---|---|---|---|
| T2-1 | True North Research | Lisa Graves | lisa@truenorthresearch.org | Composite score 4+ OR 1 STRONG from CLC/Issue One | DORMANT |
| T2-2 | UCLA Safeguarding Democracy (Rick Hasen) | Rick Hasen | rhasen@law.ucla.edu | Composite score 4+ | DORMANT |
| T2-3 | Demos | Taifa Smith Butler | info@demos.org | Composite score 2+ (CONDITIONAL or above) | DORMANT |

Update the Status column at T+7 checkpoint based on Gate Decision from Sheet 4:
- GO → update all three Status cells to ACTIVATE
- CONDITIONAL → update T2-1 and T2-2 to ACTIVATE; T2-3 to HOLD
- HOLD → all three remain DORMANT; re-evaluate at T+14
- NO-GO → all remain DORMANT; consult PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md

### Activation Timeline Tracker (update at T+7)

| Contact | Activation Status | Target Send Date | Actual Send Date | Reply Status |
|---|---|---|---|---|
| Lisa Graves (True North) | DORMANT | — | | |
| Rick Hasen (UCLA) | DORMANT | — | | |
| Taifa Smith Butler (Demos) | DORMANT | — | | |

---

## Setup Checklist (20 Minutes Total)

Complete this before executing Wave 1 sends.

- [ ] Open sheets.new → name the spreadsheet "Domain 51 — Response Tracking (June 2026)"
- [ ] Create 5 tabs with exact names: Signal Log, Email Analytics, Metrics, Checkpoint Record, Wave 2 Readiness
- [ ] Paste column headers into Row 1 of each sheet
- [ ] Pre-populate organization rows in Signal Log (Rows 2-6) and Email Analytics (Rows 2-6)
- [ ] Paste TOTAL row into Row 7 of Email Analytics
- [ ] Paste all formulas into Sheet 3 (Metrics) — verify D4 shows "GO / CONDITIONAL / HOLD / NO-GO" format by entering test values
- [ ] Paste checkpoint rows into Sheet 4 — fill in dates from today's send date
- [ ] Paste contact rows into Sheet 5 (Wave 2 Readiness)
- [ ] Shorten Gist URL to bit.ly/d51-research (or similar) at bitly.com
- [ ] Set share permission to "Anyone with link can view"
- [ ] Copy share URL → paste into CHECKIN.md under "D51 Dashboard URL"
- [ ] Replace Gist URL in all email templates with the Bitly short link

---

## Integration with Contingency Framework

**If T+7 composite score = 0 (NO-GO)**:
The D3 cell in Metrics will display: "TRIGGER: 0 replies + <3 Gist clicks — activate PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md"

Open PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md. Today's date determines the branch:
- If before July 8: Branch A (accelerated send sequence, T+7 gate suspended)
- If July 9-14: Branch B (mid-legislative framing, Wave 3 unconditional)
- If July 15+: Branch C (full-scale activation, all Tier 2-3 unconditional)

**If T+7 composite score = 4+ (GO)**:
The D2 or D4 cell in Metrics will display: "GO: Activate Wave 3"
Open DOMAIN_51_WAVE_2_ACTIVATION_DECISION_TREE.md and follow the HIGH RESPONSE branch.

**If T+7 open rate estimate ≥ 60% (D1 trigger)**:
Pre-stage Wave 2 Tier 2 contacts even if formal activation has not been triggered yet. "Pre-stage" means: confirm contact emails are current, draft the subject lines, and be ready to execute within 48 hours of the T+7 GO decision.

---

*Produced June 29, 2026. Build the spreadsheet before executing Wave 1. All formulas have been verified for Google Sheets syntax. Update on each monitoring date per DOMAIN_51_RESPONSE_MONITORING_PROTOCOL.md.*
