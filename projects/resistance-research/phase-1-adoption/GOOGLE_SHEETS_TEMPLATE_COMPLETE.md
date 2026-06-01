---
title: "Phase 1 Google Sheets Template — Complete Instantiation Guide"
created: 2026-06-03
scope: "Full 7-tab template with copy-paste formulas, validation rules, and setup instructions"
status: production-ready
setup_time: "20-25 minutes"
companion: "PHASE_1_MEASUREMENT_SPREADSHEET_SPEC.md (schema reference)"
---

# Phase 1 Google Sheets Template — Complete Instantiation Guide

**Setup time**: 20-25 minutes (one-time)
**Account**: wanka95@gmail.com
**Title**: `Phase 1 Impact Dashboard — June 2026`

This document provides all formulas, validation rules, and data structures in copy-paste format. After setup, all arithmetic is autonomous — you only enter raw data.

---

## Quick Setup (before entering any data)

1. Create Google Sheet at sheets.google.com (account: wanka95@gmail.com)
2. Title: `Phase 1 Impact Dashboard — June 2026`
3. Create 7 tabs by double-clicking tab names and typing:
   - `Contacts`
   - `Gist_Views`
   - `Replies`
   - `Adoptions`
   - `Constituencies`
   - `Checkpoints`
   - `Synthesis_Log`
4. Share: top-right Share button > "Anyone with the link" > Viewer
5. Copy share URL > paste in CHECKIN.md under "Dashboard URL"

---

## Tab 1: Contacts

**Purpose**: One row per outreach contact. The primary operational ledger.

### Header Row (Row 2)

Enter these labels in Row 2, columns A through P:

```
A: Contact_ID
B: Full_Name
C: Organization
D: Constituency
E: Email
F: Wave_Sent
G: Delivery_Status
H: First_Reply_Date
I: Reply_Score
J: Referral_Source
K: Referral_Made
L: Adoption_Signal
M: Adoption_Date
N: Survey_Sent
O: Survey_Response
P: Notes
```

### Summary Block (Row 1, Columns A-B)

Enter labels in Column A, formulas in Column B:

| Row | Column A (label) | Column B (formula) |
|-----|------------------|--------------------|
| 1 | Total contacts | `=COUNTA(A3:A200)-COUNTBLANK(A3:A200)` |

Add a second summary block to the right (columns D-E, row 1) for easy scanning:

| Row | Column D (label) | Column E (formula) |
|-----|------------------|--------------------|
| 1 | Delivered | `=COUNTIF(G3:G200,"Delivered")` |
| — | Bounced | `=COUNTIF(G3:G200,"Bounced")` |
| — | Any reply | `=COUNTA(H3:H200)-COUNTBLANK(H3:H200)` |
| — | Reply rate | `=IFERROR((COUNTA(H3:H200)-COUNTBLANK(H3:H200))/COUNTIF(G3:G200,"Delivered"),0)` |
| — | Score 3+ replies | `=COUNTIF(I3:I200,">=3")` |
| — | Score 3+ rate | `=IFERROR(COUNTIF(I3:I200,">=3")/COUNTIF(G3:G200,"Delivered"),0)` |
| — | Total referrals made | `=COUNTA(K3:K200)-COUNTBLANK(K3:K200)` |
| — | Adoption signals logged | `=COUNTA(L3:L200)-COUNTBLANK(L3:L200)` |

Format the two rate cells as "Percentage" with 1 decimal place:
- Select cell > Format > Number > Percent

### Data Validation Rules

**Column D (Constituency)** — Dropdown:
- Select D3:D200 > Data > Data validation > Criteria: "List of items"
- Enter: `Law School,Imm Legal Aid,Civil Rights,Academic,Faith,Labor,Mutual Aid`

**Column G (Delivery_Status)** — Dropdown:
- Select G3:G200 > Data > Data validation > List of items
- Enter: `Delivered,Bounced,OOO,Unknown`

**Column I (Reply_Score)** — Number:
- Select I3:I200 > Data > Data validation > Number > Between 1 and 5
- Check "Show warning" (allows blanks)

### Initial Data Entry

Enter one row per contact from:
- `execution/domain-39-contact-list.md` (Domain 39 contacts)
- `execution/domain-56-email-template.md` (Domain 56 contacts)

Fill columns:
- A: Contact_ID (C001, C002, etc.)
- B: Full_Name (Last, First)
- C: Organization
- D: Constituency (select from dropdown)
- E: Email
- F: Wave_Sent (date you sent to this person: 05/28/2026 or 06/01/2026)
- G: Delivery_Status = "Unknown" initially (change to "Delivered" after confirmed; "Bounced" if bounce notification received)
- All other columns: leave blank initially

---

## Tab 2: Gist_Views

**Purpose**: Weekly click tracking per Bitly short link.

### Header Row (Row 1)

```
A: Week_Number
B: Week_End_Date
C: D56_Civil_Service
D: D39_Healthcare
E: D59_Economic
F: D58_Tribal
G: Full_Proposal
H: Other
I: Total_Week
J: Cumulative
K: Spike_Flag
L: Spike_Notes
```

### Row 2 Formulas (fill for each weekly data row)

Column I (Total_Week): `=SUM(C2:H2)`
Column J (Cumulative): `=SUM($I$2:I2)` (running total — copy down each week)
Column K (Spike_Flag): `=IF(MAX(C2:H2)>=5,"FLAG","")`

### Weekly Target Reference Block (add to the right, columns N-O)

Enter this reference table starting at N1:

| Col N (Week) | Col O (Cumulative Target) |
|---|---|
| Week | Cumulative Target |
| 1 | 15 |
| 2 | 25 |
| 4 | 50 |
| 8 | 100 |

### Important Note on Data Source

GitHub API does not expose Gist view counts. Pull weekly click data manually from:
- bitly.com > Sign in > Analytics > select each link > "Last 7 days"

If Bitly was not set up before the June 1 send: leave Week 1 blank and note "No Bitly data — tracking starts Week 2" in the Spike_Notes column.

### Example Week 1 Row

| 1 | 06/07/2026 | 8 | 4 | 0 | 0 | 3 | 0 | 15 | 15 | | First week — Domain 56 and 39 only active |

---

## Tab 3: Replies

**Purpose**: One row per substantive reply received.

### Header Row

```
A: Reply_ID
B: Contact_ID
C: Reply_Date
D: Reply_Score
E: Reply_Type
F: Constituency
G: Domain_Referenced
H: Forward_Target
I: Adoption_Statement
J: Follow_Up_Required
K: Notes
```

### Auto-Fill Formula (Column F)

In F2, enter:
```
=IFERROR(VLOOKUP(B2,Contacts!A:D,4,FALSE),"")
```

Drag this formula down through F200. It pulls the constituency label from the Contacts tab automatically.

### Data Validation

**Column E (Reply_Type)** — Dropdown:
- Select E2:E200 > Data validation > List of items
- Enter: `OOO,Ack,Question,Forward,Adoption,Referral,Decline`

**Column D (Reply_Score)** — Number:
- Data validation > Number > Between 1 and 5

**Column J (Follow_Up_Required)** — Dropdown:
- List of items: `Yes,No,Sent`

### Entry Protocol

Enter one row immediately when a reply is scored. Do not batch — real-time entry keeps the Constituencies tab accurate.

Reply_ID format: R001, R002, R003...

---

## Tab 4: Adoptions

**Purpose**: Registry of confirmed and probable organizational adoption events.

### Header Row

```
A: Signal_ID
B: Detected_Date
C: Organization
D: Constituency
E: Signal_Type
F: Domain_Refs
G: Evidence_Source
H: Verification
I: People_Reached
J: Network_Event
K: Description
```

### Data Validation

**Column E (Signal_Type)** — Dropdown:
`Curriculum,Litigation Toolkit,Policy Brief,Training Module,Governance Doc,Citation,Other`

**Column G (Evidence_Source)** — Dropdown:
`Reply Email,Survey,Web Detection,PACER,Direct Confirmation`

**Column H (Verification)** — Dropdown:
`Confirmed,Probable,Unconfirmed`

**Column J (Network_Event)** — Dropdown:
`YES,NO`

### Automated Summary Block (add below data, labeled)

Add these below your last data row (leave 5 blank rows as buffer, then enter):

| Label | Formula |
|-------|---------|
| Confirmed adoptions | `=COUNTIF(H2:H200,"Confirmed")` |
| Probable adoptions | `=COUNTIF(H2:H200,"Probable")` |
| People reached (est.) | `=SUM(I2:I200)` |
| Network events | `=COUNTIF(J2:J200,"YES")` |
| Day 60 adoption gate | `=IF(COUNTIF(H2:H200,"Confirmed")>=15,"THRESHOLD MET","Need "&(15-COUNTIF(H2:H200,"Confirmed"))&" more")` |
| Day 60 people gate | `=IF(SUM(I2:I200)>=100,"THRESHOLD MET","Need "&(100-SUM(I2:I200))&" more")` |

---

## Tab 5: Constituencies

**Purpose**: Decision-facing view. One row per constituency (7 rows). Read during checkpoint reviews.

### Header Row

```
A: Constituency
B: Total_Contacts
C: Delivered
D: Any_Reply
E: Score3Plus
F: Score3Plus_Rate
G: Day7_Status
H: Day14_Status
I: Day30_Strong
J: Day30_Moderate
K: Adoptions
L: People_Reached
M: Network_Events
N: Status_Note
```

### Fixed Labels in Column A (rows 2-8)

Enter exactly:
```
A2: Law School
A3: Imm Legal Aid
A4: Civil Rights
A5: Academic
A6: Faith
A7: Labor
A8: Mutual Aid
```

### Formulas for Rows 2-8 (all relative to A2 — adjust row number)

Column B: `=COUNTIF(Contacts!D:D,A2)`
Column C: `=COUNTIFS(Contacts!D:D,A2,Contacts!G:G,"Delivered")`
Column D: `=COUNTIFS(Contacts!D:D,A2,Contacts!I:I,">0")`
Column E: `=COUNTIFS(Contacts!D:D,A2,Contacts!I:I,">=3")`
Column F: `=IFERROR(E2/C2,0)` — format as Percentage (1 decimal)
Column G: Manual entry. PASS / MONITOR / FAIL (fill at Day 7 checkpoint)
Column H: Manual entry. ON TRACK / MONITOR / BELOW BASELINE (fill at Day 14)
Column I: Manual entry. YES / NO (fill at Day 30 checkpoint)
Column J: Manual entry. YES / NO (fill at Day 30)
Column K: `=COUNTIFS(Adoptions!D:D,A2,Adoptions!H:H,"Confirmed")`
Column L: `=SUMIF(Adoptions!D:D,A2,Adoptions!I:I)`
Column M: `=COUNTIFS(Adoptions!D:D,A2,Adoptions!J:J,"YES")`
Column N: Manual entry. Free text.

### Overall Gate Formulas (Row 10, below the 7 constituency rows)

Add labels in column A (rows 10-12), formulas in column B:

| Row | A (label) | B (formula) |
|-----|-----------|-------------|
| 10 | Constituencies at Day30 Strong | `=COUNTIF(I2:I8,"YES")` |
| 11 | Phase 2 STRONG trigger | `=IF(COUNTIF(I2:I8,"YES")>=4,"STRONG — ACTIVATE PHASE 2","Below STRONG: "&COUNTIF(I2:I8,"YES")&" of 4 required")` |
| 12 | Phase 2 MODERATE trigger | `=IF(COUNTIF(J2:J8,"YES")>=3,"MODERATE — ACTIVATE D39","Below MODERATE: "&COUNTIF(J2:J8,"YES")&" of 3 required")` |

---

## Tab 6: Checkpoints

**Purpose**: Append-only log of formal checkpoint assessments. Do not edit past rows.

### Header Row

```
A: Assessment_Date
B: Checkpoint_Type
C: Overall_Reply_Rate
D: Score3Plus_Rate
E: Constituencies_Strong
F: Cross_Org_Refs
G: Confirmed_Adoptions
H: People_Reached
I: Determination
J: Phase2_Decision
K: Notes
```

### Data Validation

**Column B (Checkpoint_Type)** — Dropdown:
`Day 7,Day 14,Day 30,Day 60,Ad Hoc`

**Column I (Determination)** — Dropdown:
`STRONG,MODERATE,WEAK,TOO_EARLY,FAILURE,HOLD,MONITOR,ESCALATE,ASSESS`

### Entry Rules

- One row per checkpoint assessment
- Pull Columns C, D, E, F, G, H from formulas in other tabs at the time of assessment
- Never modify a row after it is entered — this is an immutable audit log
- If you re-run a checkpoint (e.g., revised data), add a new row; do not overwrite

### Example Row (Day 7 HOLD)

| 06/08/2026 | Day 7 | 9.5% | 4.8% | 0 | 1 | 0 | 0 | HOLD | Domain 39 active | 23 clicks, 4 replies including Score 4 from NILC |

---

## Tab 7: Synthesis_Log

**Purpose**: One row per completed weekly synthesis. Captures weekly state for historical reference.

### Header Row

```
A: Week_Number
B: Synthesis_Date
C: Gist_Views_Week
D: Gist_Views_Cumulative
E: New_Replies
F: Score3Plus_New
G: Adoption_Events_New
H: Tier2_Candidates
I: Risk_Signals
J: Decision_Status
K: Next_Actions
```

### Data Validation

**Column J (Decision_Status)** — Dropdown:
`HOLD,MONITOR,ESCALATE,ACTIVATE`

### Formula Shortcuts (for columns C and D)

Column C links to Gist_Views tab for that week's total:
`=IFERROR(INDEX(Gist_Views!I:I,MATCH(A2,Gist_Views!A:A,0)),0)`

Column D (cumulative):
`=IFERROR(INDEX(Gist_Views!J:J,MATCH(A2,Gist_Views!A:A,0)),0)`

Or enter manually from the Gist_Views tab if simpler.

### Entry Schedule

Enter one row each Monday after completing the weekly synthesis:
- Week 1: June 8, 2026
- Week 2: June 15, 2026
- Week 4: June 29, 2026 (Day 30 checkpoint)
- Week 8: July 27, 2026 (Day 60 checkpoint)
- Weeks 3, 5, 6, 7: optional (recommended)

---

## Permission Controls

This sheet is for solo operator use (wanka95@gmail.com). No co-editors needed.

**What you can always do**:
- Edit any cell at any time
- Add rows to any tab
- Fix formula errors
- Change Determination values after re-evaluation

**What requires external data** (cannot be auto-calculated):
- Bitly click counts (pull manually from bitly.com)
- Reply scores (human judgment from reading emails)
- Adoption verification (requires external confirmation)
- People_Reached estimates (reasonable judgment about org size)

**What is fully autonomous** (no user input after initial setup):
- All COUNTIF/COUNTIFS formulas in Contacts summary
- All VLOOKUP formulas in Replies tab (Constituency auto-fill)
- All Constituencies tab formulas (B through F, K through M)
- Cumulative totals in Gist_Views (column J)
- Spike_Flag column in Gist_Views
- Gate formulas in Constituencies rows 10-12

---

## Verification After Setup

Run these checks after completing the 7-tab setup:

1. Enter one test row in Contacts (any contact) and verify:
   - Column D dropdown shows 7 options
   - Column G dropdown shows 4 delivery status options
   - Column I validation rejects values outside 1-5

2. Enter one row in Replies and verify:
   - Column F auto-fills with constituency from Contacts (VLOOKUP working)
   - Column D dropdown works

3. Check Constituencies tab:
   - Column B shows total contacts per constituency (should be >0 for at least some)
   - Formulas show 0 or blank, not errors (#REF, #N/A)

4. Enter one row in Adoptions and verify:
   - Summary block below calculates correctly

If any formula returns an error, check that:
- Tab names are spelled exactly as specified (case-sensitive)
- Header rows are in Row 1 (not Row 2) for Contacts (summary), Row 2 for data
- Column letters match the specification

---

## Sharing and Access

Share settings (set once, never change):
- Access: Anyone with the link
- Role: Viewer (not Editor — protects against accidental edits from other devices)

Post the dashboard URL in CHECKIN.md:
```
## Dashboard URL
[paste Google Sheets share URL here]
```

This enables the system to reference it in future planning documents.
