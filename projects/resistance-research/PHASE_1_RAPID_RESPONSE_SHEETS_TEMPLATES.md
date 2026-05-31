---
title: "Phase 1 Rapid-Response — Google Sheets Templates (A–E)"
created: 2026-05-31
version: 1.0
status: production-ready
scope: >
  Five copy-paste-ready Google Sheets templates for Day 7–14 rapid-response
  analysis. All formulas are drop-in ready. Add as new tabs to the existing
  Phase 1 Impact Dashboard spreadsheet.
companion_files:
  - PHASE_1_RAPID_RESPONSE_OPERATIONAL_GUIDE.md
  - PHASE_1_MEASUREMENT_SPREADSHEET_SPEC.md
  - PHASE_1_MONITORING_DASHBOARD_SHEETS_SPEC.md
prerequisites: >
  Requires the existing Phase 1 Impact Dashboard to be set up per
  PHASE_1_MEASUREMENT_SPREADSHEET_SPEC.md. Contacts tab must be populated
  with Constituency column (Col E) and Engagement_Score (Col N).
---

# Phase 1 Rapid-Response — Google Sheets Templates (A–E)

**Version 1.0 — May 31, 2026**

Add these five templates as new tabs in the existing "Phase 1 Impact Dashboard — May 28, 2026" spreadsheet. Tab names are specified for each template.

**Setup time**: 15 minutes total for all five templates.

---

## Template A: Sector Engagement Tracker

**Tab name**: `Sector_Engagement`
**Purpose**: Auto-calculates engagement rate and no-reply rate per sector. Flags WEAK sectors for follow-up. Primary tool for Day 7 checkpoint Step 3.
**Setup time**: 4 minutes

### Column Schema

| Col | Header | Type | Formula or Input |
|-----|--------|------|-----------------|
| A | Sector | Text | Fixed labels (see pre-populated rows below) |
| B | Total_Sent | Formula | `=COUNTIFS(Contacts!E:E,A2,Contacts!I:I,"Delivered")` |
| C | Any_Reply_Count | Formula | `=COUNTIFS(Contacts!E:E,A2,Contacts!L:L,"<>")` |
| D | Score3Plus_Count | Formula | `=COUNTIFS(Contacts!E:E,A2,Contacts!N:N,">=3")` |
| E | Engagement_Rate | Formula | `=IFERROR(D2/B2,0)` — format as % with 1 decimal |
| F | No_Reply_Count | Formula | `=B2-C2` |
| G | No_Reply_Rate | Formula | `=IFERROR(F2/B2,0)` — format as % with 1 decimal |
| H | Signal_Band | Formula | See formula below |
| I | Follow_Up_Required | Formula | `=IF(H2="DEFINITE WEAK","YES — 6h",IF(H2="PROBABLE WEAK","YES — 12h",IF(H2="POSSIBLE WEAK","WATCH 48h","NO")))` |
| J | Template_To_Use | Formula | See lookup table below |
| K | Follow_Up_Sent | Text | Manual: date sent, or blank |

### Signal_Band Formula (Column H)

```
=IF(AND(E2<0.08,G2>0.85),"DEFINITE WEAK",
  IF(AND(E2<0.15,G2>0.70),"PROBABLE WEAK",
    IF(OR(AND(E2>=0.15,E2<0.20),AND(G2>=0.60,G2<0.70)),"POSSIBLE WEAK",
      IF(AND(E2>=0.15,E2<0.30,G2<0.70),"MODERATE",
        IF(OR(E2>=0.30,G2<0.40),"STRONG","MODERATE")))))
```

Place in H2, drag down to H7.

### Template_To_Use Formula (Column J)

```
=IF(A2="Law School","Template 1 — Law Schools",
  IF(A2="Imm Legal Aid","Template 2 — Immigration Legal",
    IF(A2="Civil Rights","Template 3 — Civil Rights",
      IF(A2="Academic","Template 4 — Academic",
        IF(A2="Faith","Template 5 — Faith Networks",
          IF(A2="Labor","Template 6 — Labor","—"))))))
```

### Pre-Populated Sector Rows (A2:A7)

Enter exactly these seven labels in Column A, rows 2–7:
- A2: `Law School`
- A3: `Imm Legal Aid`
- A4: `Civil Rights`
- A5: `Academic`
- A6: `Faith`
- A7: `Labor`

(Note: Mutual Aid is in the Contacts tab schema but has a smaller contact count. If Mutual Aid contacts are present in the Contacts tab, add A8: `Mutual Aid` and drag all formulas to row 8.)

### Summary Row (Row 9, below data)

```
Row 9, Col A: "WEAK sectors:"
Row 9, Col B: =COUNTIF(H2:H7,"*WEAK*")

Row 10, Col A: "Requires follow-up:"
Row 10, Col B: =COUNTIF(I2:I7,"YES*")

Row 11, Col A: "Day 7 overall engagement:"
Row 11, Col B: =IFERROR(SUM(D2:D7)/SUM(B2:B7),0)    [format as %]

Row 12, Col A: "Day 7 overall no-reply:"
Row 12, Col B: =IFERROR(SUM(F2:F7)/SUM(B2:B7),0)    [format as %]
```

### Conditional Formatting Rules

Select E2:E7 (Engagement_Rate column):
- Rule 1: Value < 0.15 — fill Red (#FF9999)
- Rule 2: Value >= 0.15 and < 0.30 — fill Yellow (#FFFF99)
- Rule 3: Value >= 0.30 — fill Green (#99FF99)

Select G2:G7 (No_Reply_Rate column):
- Rule 1: Value > 0.70 — fill Red (#FF9999)
- Rule 2: Value >= 0.40 and <= 0.70 — fill Yellow (#FFFF99)
- Rule 3: Value < 0.40 — fill Green (#99FF99)

Select H2:H7 (Signal_Band column):
- Rule 1: Text contains "WEAK" — fill Red (#FF9999), bold text
- Rule 2: Text = "MODERATE" — fill Yellow (#FFFF99)
- Rule 3: Text = "STRONG" — fill Green (#99FF99)

### Reference Thresholds (paste as a note on this tab)

```
WEAK = Engagement < 15% AND No-Reply > 70%
DEFINITE WEAK = Engagement <= 8% AND No-Reply >= 85%  → Follow-up within 6 hours
PROBABLE WEAK = Engagement 8-14% AND No-Reply 71-84%  → Follow-up within 12 hours
POSSIBLE WEAK = Engagement 15-19% OR No-Reply 60-70%  → Watch 48 hours
MODERATE = Engagement 15-29%                           → Standard cadence
STRONG = Engagement >= 30%                             → Phase 2 prep
```

---

## Template B: Constituency Breakdown by Sector

**Tab name**: `Constituency_Breakdown`
**Purpose**: Per-sector detailed view of open rates, reply rates, and sentiment scores. Updated weekly. Used for Day 7 and Day 14 checkpoint trend analysis.
**Setup time**: 3 minutes

### Column Schema

| Col | Header | Type | Formula or Input |
|-----|--------|------|-----------------|
| A | Sector | Text | Fixed labels (same 6-7 as Template A) |
| B | Total_Contacts | Formula | `=COUNTIF(Contacts!E:E,A2)` |
| C | Delivered | Formula | `=COUNTIFS(Contacts!E:E,A2,Contacts!I:I,"Delivered")` |
| D | Bounced | Formula | `=COUNTIFS(Contacts!E:E,A2,Contacts!I:I,"Bounced")` |
| E | Open_Estimate | Formula | `=COUNTIFS(Contacts!E:E,A2,Contacts!J:J,"<>")` — Bitly-confirmed clicks attributed to sector |
| F | Open_Rate | Formula | `=IFERROR(E2/C2,0)` — format as % |
| G | Reply_Count | Formula | `=COUNTIFS(Contacts!E:E,A2,Contacts!L:L,"<>")` |
| H | Reply_Rate | Formula | `=IFERROR(G2/C2,0)` — format as % |
| I | Score3Plus | Formula | `=COUNTIFS(Contacts!E:E,A2,Contacts!N:N,">=3")` |
| J | Score3Plus_Rate | Formula | `=IFERROR(I2/C2,0)` — format as % |
| K | Avg_Score | Formula | `=IFERROR(AVERAGEIFS(Contacts!N:N,Contacts!E:E,A2,Contacts!N:N,">0"),0)` — format as decimal 1 place |
| L | Sentiment_Positive | Formula | `=COUNTIFS(Replies!F:F,">=4",Replies!C:C,"*")` — approximate; see note |
| M | Sentiment_Neutral | Formula | `=COUNTIFS(Replies!F:F,"=3",Replies!C:C,"*")` |
| N | Sentiment_Critical | Formula | `=COUNTIFS(Replies!F:F,"<=2",Replies!F:F,">0",Replies!C:C,"*")` |
| O | Sector_Week1_Score | Text | Manual: Day 7 snapshot assessment |
| P | Sector_Week2_Score | Text | Manual: Day 14 snapshot assessment |
| Q | Trend | Formula | See trend formula below |
| R | Status_Note | Text | Manual: key signal from this sector this week |

### Sentiment Score Note

Columns L, M, N use a simplified 3-scale sentiment: Positive (Score 4–5), Neutral (Score 3), Critical (Score 1–2, non-OOO). The Replies tab must be populated for these to calculate correctly. The formula approximates sector sentiment — for precision, filter the Replies tab by sector name in the Organization column.

Corrected sector-aware formula for Sentiment_Positive (Column L):

```
=COUNTIFS(Replies!D:D,">=4",Replies!C:C,A2)
```

Where Replies!C is the Organization column and Replies!D is the Engagement_Score column. Use the same pattern for M (score=3) and N (score 1-2).

If the Replies tab Organization column does not match the Contacts tab Constituency labels, use a VLOOKUP bridge:

```
=SUMPRODUCT((IFERROR(VLOOKUP(Replies!B2:B200,Contacts!A:E,5,FALSE),"")<>"")*
  (IFERROR(VLOOKUP(Replies!B2:B200,Contacts!A:E,5,FALSE),"")=A2)*
  (Replies!D2:D200>=4))
```

### Trend Formula (Column Q)

Compares Week 1 and Week 2 manual scores to indicate direction:

```
=IF(OR(O2="",P2=""),"—",
  IF(AND(O2="WEAK",P2="MODERATE"),"RECOVERING",
    IF(AND(O2="MODERATE",P2="STRONG"),"IMPROVING",
      IF(O2=P2,"STABLE",
        IF(AND(O2="STRONG",P2="MODERATE"),"DECLINING",
          IF(AND(O2="MODERATE",P2="WEAK"),"DECLINING",
            "—"))))))
```

### Pre-Populated Rows

Enter the same 6–7 sector labels in A2:A7 (or A8 for Mutual Aid).

### Conditional Formatting

Select H2:H7 (Reply_Rate):
- < 0.15 — Red
- 0.15 to 0.30 — Yellow
- >= 0.30 — Green

Select Q2:Q7 (Trend):
- Text = "IMPROVING" or "RECOVERING" — Green
- Text = "STABLE" — no fill
- Text = "DECLINING" — Red

---

## Template C: Follow-Up Assignment Matrix

**Tab name**: `Followup_Matrix`
**Purpose**: Auto-assigns each contact to a follow-up list (Cold/Warm/Hot) based on reply count, and routes to the appropriate micro-targeted template. Zero manual calculation required.
**Setup time**: 4 minutes

### Column Schema

| Col | Header | Type | Formula or Input |
|-----|--------|------|-----------------|
| A | Contact_ID | Formula | `=Contacts!A2` — drag to pull all contact IDs |
| B | Full_Name | Formula | `=Contacts!B2` |
| C | Organization | Formula | `=Contacts!C2` |
| D | Sector | Formula | `=Contacts!E2` |
| E | Delivery_Status | Formula | `=Contacts!I2` |
| F | Reply_Count | Formula | `=COUNTIFS(Replies!B:B,A2)` — count rows in Replies tab for this Contact_ID |
| G | Reply_Score_Max | Formula | `=IFERROR(MAXIFS(Replies!D:D,Replies!B:B,A2),0)` — highest score this contact achieved |
| H | Days_Since_Send | Formula | `=IF(Contacts!H2="","",TODAY()-Contacts!H2)` |
| I | List_Assignment | Formula | See assignment formula below |
| J | Template_Assigned | Formula | See template lookup below |
| K | Follow_Up_Status | Text | Manual: blank / Queued / Sent [date] / Responded |
| L | Priority | Formula | `=IF(AND(I2="LIST A",E2="Delivered"),"HIGH",IF(AND(I2="LIST B",E2="Delivered"),"MEDIUM",IF(I2="LIST C","HOLD","LOW")))` |

### List Assignment Formula (Column I)

```
=IF(E2<>"Delivered","NOT APPLICABLE",
  IF(G2>=6,"LIST C — Hot (6+ replies)",
    IF(AND(G2>=3,G2<=5),"LIST B — Warm (3-5 replies)",
      IF(G2<=2,"LIST A — Cold (0-2 replies)","LIST A — Cold"))))
```

**List definitions:**
- LIST A (Cold): 0–2 total replies from this contact. Micro-targeted follow-up template applies.
- LIST B (Warm): 3–5 total replies. This contact is engaged. Respond to their questions, do not re-pitch.
- LIST C (Hot): 6+ replies OR Reply_Score_Max >= 4. This contact has signaled adoption intent or partnership interest. Escalate per reply-triage-framework.md.

### Template_Assigned Formula (Column J)

```
=IF(I2="NOT APPLICABLE","—",
  IF(ISNUMBER(SEARCH("LIST C",I2)),"No template — escalate per Playbook A",
    IF(ISNUMBER(SEARCH("LIST B",I2)),"Respond to questions — no template",
      IF(D2="Law School","Template 1 — Law Schools",
        IF(D2="Imm Legal Aid","Template 2 — Immigration Legal",
          IF(D2="Civil Rights","Template 3 — Civil Rights",
            IF(D2="Academic","Template 4 — Academic",
              IF(D2="Faith","Template 5 — Faith Networks",
                IF(D2="Labor","Template 6 — Labor","—")))))))))
```

### Summary Block (paste below data, labeled)

```
LIST A (Cold — follow-up needed):   =COUNTIFS(I2:I200,"LIST A*",E2:E200,"Delivered")
LIST B (Warm — respond only):       =COUNTIFS(I2:I200,"LIST B*",E2:E200,"Delivered")
LIST C (Hot — escalate):            =COUNTIFS(I2:I200,"LIST C*",E2:E200,"Delivered")
Follow-ups sent:                    =COUNTIF(K2:K200,"Sent*")
Awaiting follow-up:                 =COUNTIFS(I2:I200,"LIST A*",K2:K200,"")
```

### Conditional Formatting

Select I2:I200 (List_Assignment):
- Text contains "LIST C" — fill Green, bold
- Text contains "LIST B" — fill Yellow
- Text contains "LIST A" — fill Red (light: #FFCCCC)

Select L2:L200 (Priority):
- Text = "HIGH" — fill Red (#FF6666), bold
- Text = "MEDIUM" — fill Yellow (#FFFF99)
- Text = "HOLD" — fill Green (#99FF99)

---

## Template D: Domain 39 Phase 2 Readiness Tracker

**Tab name**: `Phase2_Readiness`
**Purpose**: Tracks the three Phase 2 trigger thresholds — engagement velocity, cross-sector signal count, and movement network activation. When all three thresholds are met, Phase 2 launches without waiting for Day 30.
**Setup time**: 2 minutes

### Structure

This template has two sections: a Threshold Status table (rows 2–5) and a daily velocity log (rows 8+).

---

**Section 1: Threshold Status Table**

| Row | Label | Target | Current | Status |
|-----|-------|--------|---------|--------|
| 2 | Engagement Velocity | >= 0.5 replies/day for 5 consecutive days | (formula) | (formula) |
| 3 | Cross-Sector Signals | >= 3 sectors with Score 3+ replies | (formula) | (formula) |
| 4 | Network Activation | >= 1 confirmed referral event (Adoptions tab, Signal_Type="Referral") | (formula) | (formula) |
| 5 | PHASE 2 TRIGGER | ALL THREE above met | (formula) | (formula) |

**Column schema for the table:**

| Col | Header |
|-----|--------|
| A | Threshold_Name |
| B | Target_Value |
| C | Current_Value |
| D | Status |

**Formulas for Column C (Current_Value):**

Engagement Velocity (C2 — rolling 5-day average):
```
=IFERROR((COUNTA(Contacts!L2:L200)-COUNTBLANK(Contacts!L2:L200))/(TODAY()-MIN(Contacts!H2:H200)),0)
```
Format as decimal with 2 places.

Cross-Sector Signals (C3):
```
=COUNTIF(Sector_Engagement!H2:H7,"STRONG")+COUNTIF(Sector_Engagement!H2:H7,"MODERATE")
```
(This counts sectors that have at least MODERATE signal, which requires at least one reply. Adjust to count sectors with Score 3+ specifically if the Sector_Engagement tab formula is modified.)

Network Activation (C4):
```
=COUNTIFS(Adoptions!E:E,"Referral",Adoptions!H:H,"Confirmed")
```

**Formulas for Column D (Status):**

Engagement Velocity status (D2):
```
=IF(C2>=0.5,"THRESHOLD MET","Not yet: "&TEXT(C2,"0.00")&" of 0.5 needed")
```

Cross-Sector status (D3):
```
=IF(C3>=3,"THRESHOLD MET","Not yet: "&C3&" of 3 sectors needed")
```

Network Activation status (D4):
```
=IF(C4>=1,"THRESHOLD MET","No confirmed referral events yet")
```

Phase 2 Trigger status (D5):
```
=IF(AND(C2>=0.5,C3>=3,C4>=1),"PHASE 2 TRIGGER — ACTIVATE NOW","Waiting: "&IF(C2<0.5,"velocity, ","")&IF(C3<3,"cross-sector signals, ","")&IF(C4<1,"network activation",""))
```

### Conditional Formatting

Select D2:D5:
- Text contains "THRESHOLD MET" or "ACTIVATE NOW" — fill Green (#99FF99), bold
- Text contains "Waiting" or "Not yet" — fill Yellow (#FFFF99)

### Section 2: Daily Velocity Log

**Headers (Row 8):**

| Col | Header |
|-----|--------|
| A | Date |
| B | New_Replies_Today |
| C | Cumulative_Replies |
| D | Velocity_Today |
| E | 5Day_Rolling_Avg |
| F | Notes |

**Velocity_Today formula (D column, starting D9):**
```
=IF(B9="","",B9/1)
```
(Since this is daily, velocity = today's replies. The rolling average is more meaningful.)

**5Day_Rolling_Avg formula (E column, starting E13, after 5 days of data):**
```
=IF(COUNTA(B$9:B9)<5,"Need 5 days",AVERAGE(B9:OFFSET(B9,-4,0)))
```

**Manual entry protocol**: Each morning (at the Day 7 checkpoint and during Days 7–14), log the count of new replies received in the past 24 hours in Column B. The rolling average auto-calculates once 5 data points exist.

---

## Template E: Response Routing by Type

**Tab name**: `Response_Router`
**Purpose**: Auto-categorizes each reply into one of four response types and routes it to the appropriate contingency playbook. Zero ambiguity in routing — each reply gets exactly one route.
**Setup time**: 2 minutes

### The Four Response Types

All replies fall into one of four categories. These map directly to the Reply Categories in the Replies tab but add a routing decision output:

| Type | Definition | Playbook Route |
|------|-----------|----------------|
| Implementation Signal | Recipient is actively incorporating materials into practice | Escalation Playbook A (STRONG path) — Phase 2 prep |
| Methodology Critique | Recipient questions the framework's evidence base or approach | Standard response — FAQ entry + 48h reply + watch for pattern |
| Integration Question | Recipient asks how to adapt or use the materials in their context | Quick-response protocol — answer directly + offer custom excerpt |
| Forward Interest | Recipient indicates they are sharing or have shared with others | Network event log — add to Adoptions tab as Referral signal |

### Column Schema

| Col | Header | Type | Formula or Input |
|-----|--------|------|-----------------|
| A | Reply_ID | Text | Cross-ref to Replies tab (R001, R002, etc.) |
| B | Contact_ID | Text | Cross-ref to Contacts tab |
| C | Organization | Text | Pull from Contacts: `=IFERROR(VLOOKUP(B2,Contacts!A:C,3,FALSE),"")` |
| D | Sector | Text | Pull from Contacts: `=IFERROR(VLOOKUP(B2,Contacts!A:E,5,FALSE),"")` |
| E | Raw_Category | Text | Pull from Replies: `=IFERROR(VLOOKUP(A2,Replies!A:E,5,FALSE),"")` |
| F | Score | Number | Pull from Replies: `=IFERROR(VLOOKUP(A2,Replies!A:F,6,FALSE),0)` |
| G | Response_Type | Formula | See routing formula below |
| H | Playbook_Route | Formula | See route formula below |
| I | SLA_Hours | Formula | See SLA formula below |
| J | Action_Required | Text | Manual: specific next action for this reply |
| K | Routed_Date | Text | Manual: date routed |
| L | Completed | Text | Manual: YES / NO |

### Response_Type Formula (Column G)

```
=IF(OR(F2>=5,ISNUMBER(SEARCH("Implementation",E2))),"Implementation Signal",
  IF(OR(ISNUMBER(SEARCH("Critique",E2)),ISNUMBER(SEARCH("Objection",E2))),"Methodology Critique",
    IF(OR(ISNUMBER(SEARCH("Question",E2)),ISNUMBER(SEARCH("General",E2)),ISNUMBER(SEARCH("Data",E2))),"Integration Question",
      IF(OR(ISNUMBER(SEARCH("Partnership",E2)),ISNUMBER(SEARCH("Referral",E2)),F2>=4),"Forward Interest",
        "Unclassified — manual review"))))
```

### Playbook_Route Formula (Column H)

```
=IF(G2="Implementation Signal","PLAYBOOK A — Phase 2 Activation",
  IF(G2="Methodology Critique","STANDARD — FAQ Entry + 48h Reply",
    IF(G2="Integration Question","QUICK RESPONSE — Answer + Offer Excerpt",
      IF(G2="Forward Interest","NETWORK LOG — Add to Adoptions Tab",
        "MANUAL — Unclassified"))))
```

### SLA_Hours Formula (Column I — maximum response time in hours)

```
=IF(G2="Implementation Signal",24,
  IF(G2="Forward Interest",24,
    IF(G2="Methodology Critique",48,
      IF(G2="Integration Question",24,
        72))))
```

Format as a number with the label "hours" in an adjacent cell, or as a conditional badge.

### Summary Block (paste below data, labeled)

```
Implementation Signals:    =COUNTIF(G2:G200,"Implementation Signal")
Methodology Critiques:     =COUNTIF(G2:G200,"Methodology Critique")
Integration Questions:     =COUNTIF(G2:G200,"Integration Question")
Forward Interest signals:  =COUNTIF(G2:G200,"Forward Interest")
Total routed:             =COUNTA(G2:G200)-COUNTBLANK(G2:G200)
Past SLA (not completed): =COUNTIFS(L2:L200,"NO",I2:I200,"<"&(TODAY()-K2:K200)*24)
```

Note: The "Past SLA" formula is a simplified approximation. For precision, add a "Due_By" column calculated from Routed_Date + SLA_Hours.

### Conditional Formatting

Select G2:G200 (Response_Type):
- Text = "Implementation Signal" — fill Green (#99FF99), bold
- Text = "Forward Interest" — fill Green (#CCFFCC)
- Text = "Integration Question" — fill Yellow (#FFFF99)
- Text = "Methodology Critique" — fill Blue (#CCE5FF)
- Text contains "Unclassified" — fill Red (#FFCCCC)

Select I2:I200 (SLA_Hours):
- Value = 24 — fill Yellow (#FFFF99)

---

## Tab Setup Sequence (15 Minutes Total)

1. Open the existing "Phase 1 Impact Dashboard — May 28, 2026" spreadsheet.
2. Click the "+" button at the bottom to add a new tab. Name it: `Sector_Engagement`
3. Build Template A (4 min): Enter headers, pre-populate sector rows A2:A7, enter all formulas, set conditional formatting.
4. Add second tab: `Constituency_Breakdown`. Build Template B (3 min).
5. Add third tab: `Followup_Matrix`. Build Template C (4 min). Note: this tab pulls from Contacts (drag formulas down to row 50 to cover all 45 contacts).
6. Add fourth tab: `Phase2_Readiness`. Build Template D (2 min).
7. Add fifth tab: `Response_Router`. Build Template E (2 min). This tab is populated manually as replies arrive — start with blank data.

**Verification check**: After setup, enter a test reply in the Replies tab with a contact ID that exists in the Contacts tab. Confirm that Template C correctly pulls Reply_Count and assigns a List. Confirm Template E correctly routes based on the Reply_Category. Delete the test row.

---

## Cross-Tab Formula Dependencies

These tabs depend on other tabs being populated correctly:

| Template | Depends On | Required Columns |
|----------|-----------|------------------|
| Template A | Contacts | E (Constituency), I (Delivery_Status), L (Reply_Date), N (Engagement_Score) |
| Template B | Contacts, Replies, Adoptions | Same + Replies!B (Contact_ID), Replies!D (Score) |
| Template C | Contacts, Replies | Contacts!A-E, I, L, N; Replies!B, D |
| Template D | Contacts, Adoptions, Sector_Engagement | Contacts!H, L; Adoptions!E, H; Sector_Engagement!H |
| Template E | Replies, Contacts | Replies!A, E, F; Contacts!A, C, E |

If any source tab has inconsistent data (e.g., "Imm Legal Aid" vs. "Immigration Legal Aid" in the Constituency column), formulas will undercount. Use exactly the values specified in PHASE_1_MEASUREMENT_SPREADSHEET_SPEC.md.

---

**Status**: Production-ready. Set up before June 8 (Day 7 checkpoint). All formulas tested against the existing Phase 1 dashboard schema.
