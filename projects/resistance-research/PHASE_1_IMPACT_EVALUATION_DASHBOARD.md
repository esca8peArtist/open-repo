---
title: "Phase 1 Impact Evaluation — Real-Time Coalition Response Dashboard"
created: 2026-06-06
version: 1.0
status: production-ready
scope: >
  Real-time engagement tracking infrastructure for the June 10–17 Phase 1 distribution
  window. Google Sheets template (copy-paste ready with formulas), operational instructions,
  7-day constituency view, daily metrics, auto-calculated velocity signals, and threshold
  alert system. Designed to enable mid-course corrections June 11–12 rather than waiting
  for the June 17 Day 7 analysis.
companion_files:
  - PHASE_1_IMPACT_EVALUATION_ROUTING.md
  - PHASE_1_IMPACT_EVALUATION_INTEGRATION.md
  - PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md
  - PHASE_1_MONITORING_DASHBOARD_SHEETS_SPEC.md
  - DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md
word_count: ~2800
---

# Phase 1 Impact Evaluation — Real-Time Coalition Response Dashboard

**Version 1.0 — June 6, 2026**

**Lead finding**: The existing Day 7 checkpoint framework (PHASE_1_DAY_7_CHECKPOINT_DECISION_TREE.md) is built for snapshot analysis at the end of the window. What is missing is the intra-week visibility layer: a live dashboard you can open on June 11 morning and know within 90 seconds whether Domain 39's law school constituency is tracking toward HOLD or ESCALATE before you have to make a June 12 decision. This document builds that layer — a Google Sheets dashboard that refreshes with 5 minutes of manual entry per day and surfaces go/no-go signals in real time.

---

## 1. What This Dashboard Does That the Existing Infrastructure Does Not

The existing infrastructure (PHASE_1_MONITORING_DASHBOARD_SHEETS_SPEC.md, PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE.md) is a weekly batch system. It collects, it organizes, and it feeds the Day 7 checkpoint — but it does not alert you at 9 AM on June 11 that your law school open rate is tracking at 18% and you have a 36-hour window to intervene before the best-response window closes.

This dashboard adds three capabilities to the existing stack:

**1. Daily velocity tracking**: Cumulative metrics updated each morning. You see the running trend, not just the end-of-week snapshot.

**2. Threshold alert cells**: Google Sheets conditional formatting that turns a cell red or green based on whether you are on track for STRONG, MODERATE, or WEAK at Day 7. No manual interpretation needed — the sheet tells you the status.

**3. Intra-window decision triggers**: Pre-calculated formulas that fire routing recommendations when engagement crosses thresholds, not when you happen to run the Day 7 checkpoint script.

This dashboard is a complement to the existing stack, not a replacement. The adoption-tracking-script.py continues as the authoritative post-hoc verification layer. This sheet is the real-time operational view.

---

## 2. Google Sheets Dashboard — Structure Overview

**Spreadsheet title**: `Phase 1 Real-Time Impact Dashboard — June 2026`

**Create at**: Google Sheets (sheets.google.com) → New → Blank spreadsheet

**Sharing**: Anyone with link can view. Do not grant edit access to external parties.

**Tabs** (7 tabs, in order):
1. `DAILY_SIGNALS` — primary operational view; updated each morning
2. `CONSTITUENCY_TRACKER` — 7-day per-constituency engagement view
3. `GIST_VELOCITY` — Bitly click tracking with hourly/daily velocity
4. `REPLY_LOG` — per-reply scoring with auto-calculated composite signals
5. `THRESHOLDS` — reference tab with all threshold definitions and alert formulas
6. `ALERTS` — auto-calculated alert board; one row per active alert
7. `INTEGRATION` — reconciliation zone linking this sheet to adoption-tracking-script.py outputs

---

## 3. Tab 1: DAILY_SIGNALS — Complete Schema

**Purpose**: Single-row-per-day summary from June 10 through June 17. Updated each morning before 10 AM. This is the primary operational view — open this tab for a status check.

### Column Schema

| Col | Header | Data Type | Formula / Notes |
|-----|--------|-----------|-----------------|
| A | Day_Number | Integer | 1 through 8 (Day 1 = June 10) |
| B | Date | Date | YYYY-MM-DD |
| C | Cumulative_Bitly_Clicks | Integer | Running total from all Bitly links (manual entry from Bitly dashboard) |
| D | Daily_Bitly_Delta | Formula | `=IF(A2=1,C2,C2-C1)` — clicks added today vs. yesterday |
| E | Clicks_Per_Hour | Formula | `=ROUND(D2/24,2)` — daily delta divided by 24 hours |
| F | Total_Replies | Integer | Running total of replies received at any score (manual count from Gmail) |
| G | New_Replies_Today | Formula | `=IF(A2=1,F2,F2-F1)` |
| H | Score3_Plus_Replies | Integer | Running total Score 3+ replies only (manual count) |
| I | Score3_Plus_Today | Formula | `=IF(A2=1,H2,H2-H1)` |
| J | Open_Rate_Estimate | Decimal | Manual entry: (confirmed opens or clicks / total sent) — update when new data arrives; enter as decimal (0.42 = 42%) |
| K | Bounces_Total | Integer | Running total bounced emails (manual entry from Gmail) |
| L | Threshold_Status | Formula | See Section 4 for formula |
| M | Phase2_Signal | Formula | See Section 5 for formula |
| N | Notes | Text | Free text — unusual activity, spikes, out-of-pattern signals |

### Pre-Populated Rows (copy these into A2:B9)

```
Row 2:  1  | 2026-06-10
Row 3:  2  | 2026-06-11
Row 4:  3  | 2026-06-12
Row 5:  4  | 2026-06-13
Row 6:  5  | 2026-06-14
Row 7:  6  | 2026-06-15
Row 8:  7  | 2026-06-16
Row 9:  8  | 2026-06-17
```

### Summary Block (paste into rows 11–20 below data)

```
Row 11:  Label: "7-Day Cumulative Clicks"
Row 11:  Formula: =MAX(C2:C9)

Row 12:  Label: "7-Day Total Replies"
Row 12:  Formula: =MAX(F2:F9)

Row 13:  Label: "7-Day Score 3+ Replies"
Row 13:  Formula: =MAX(H2:H9)

Row 14:  Label: "Peak Clicks/Hour"
Row 14:  Formula: =MAX(E2:E9)

Row 15:  Label: "Open Rate (Latest)"
Row 15:  Formula: =INDEX(J2:J9,MATCH(MAX(A2:A9),A2:A9,0))

Row 16:  Label: "Day 7 Status"
Row 16:  Formula: =INDEX(L2:L9,MATCH(7,A2:A9,0))

Row 17:  Label: "Bounces"
Row 17:  Formula: =MAX(K2:K9)

Row 18:  Label: "EARLY PHASE 2 SIGNAL?"
Row 18:  Formula: =IF(COUNTIF(M2:M9,"ACTIVATE")>0,"YES — CHECK PHASE2_SIGNAL COLUMN","No early trigger")
```

---

## 4. Threshold Status Formula (Column L)

This is the core real-time alert. It produces one of five status values per day:

```
=IF(C2="","PENDING",
  IF(K2>=3,"CONTACT_VERIFY",
    IF(AND(C2>=15,H2>=2),"HOLD",
      IF(AND(C2>=15,H2<2),"MONITOR_REPLIES",
        IF(AND(C2>=5,C2<15),"MONITOR_CLICKS",
          IF(AND(C2<5,F2>=1),"MONITOR_DELIVERY",
            "ESCALATE"))))))
```

**Status definitions**:
- `PENDING` — No data entered yet for this day
- `CONTACT_VERIFY` — 3+ bounces detected; verify delivery before any other action
- `HOLD` — On track (15+ cumulative clicks AND 2+ Score 3+ replies); Phase 1 proceeding normally
- `MONITOR_REPLIES` — Click velocity strong but reply count low; check inbox, may be late openers
- `MONITOR_CLICKS` — Some clicks but below target; monitor for next 24 hours before escalating
- `MONITOR_DELIVERY` — Replies without corresponding clicks; possible Bitly link issue in emails
- `ESCALATE` — Below all thresholds; requires immediate diagnosis

### Conditional Formatting for Column L

Apply these rules in order (Format > Conditional formatting > Add rule):
- Text is exactly `HOLD` → Background: #34A853 (green), text: white
- Text is exactly `MONITOR_REPLIES` → Background: #FBBC04 (amber), text: black
- Text is exactly `MONITOR_CLICKS` → Background: #FBBC04 (amber), text: black
- Text is exactly `MONITOR_DELIVERY` → Background: #FF6D00 (orange), text: white
- Text is exactly `ESCALATE` → Background: #EA4335 (red), text: white
- Text is exactly `CONTACT_VERIFY` → Background: #7B0D1E (dark red), text: white

---

## 5. Phase 2 Signal Formula (Column M)

This column fires an early Phase 2 activation recommendation when engagement crosses thresholds within the 7-day window — before the Day 7 checkpoint.

```
=IF(H2>=1,
  IF(CONSTITUENCY_TRACKER!C2>=2,"ACTIVATE",
    IF(CONSTITUENCY_TRACKER!F2>=1,"ACTIVATE",
      IF(CONSTITUENCY_TRACKER!I2>=1,"ACTIVATE",
        "BUILDING"))),
  "WAIT")
```

**Note**: This formula references CONSTITUENCY_TRACKER tab columns. See Section 7 for the CONSTITUENCY_TRACKER schema. The formula requires:
- At least 1 Score 3+ reply overall (H column in DAILY_SIGNALS)
- At least one constituency crossing its early-activation threshold (see CONSTITUENCY_TRACKER)

**Status values**:
- `WAIT` — No Score 3+ replies yet; Phase 2 sequencing on hold
- `BUILDING` — Score 3+ replies exist but no constituency has crossed early-activation threshold
- `ACTIVATE` — Early Phase 2 activation trigger fired; see PHASE_1_IMPACT_EVALUATION_ROUTING.md for routing

---

## 6. Tab 2: CONSTITUENCY_TRACKER — Complete Schema

**Purpose**: 7-day × 7-constituency engagement matrix. One row per constituency, one column per day. Updated in parallel with DAILY_SIGNALS. This is the fastest way to see which constituencies are responding and which are lagging.

### Row Setup (pre-populate rows 2–8)

| Row | Constituency | Day7_Target_Score3Plus | Day7_Minimum_Signal | Phase2_Primary_Domain |
|-----|-------------|----------------------|--------------------|-----------------------|
| 2 | Law School | 2 | 1 click OR 1 reply | Domain 58 |
| 3 | Imm Legal Aid | 1 | 1 click OR 1 reply | Domain 58 |
| 4 | Civil Rights | 2 | 1 click OR 1 reply | Domain 58 |
| 5 | Academic | 1 | 1 click OR 1 reply | Domain 59 |
| 6 | Faith | 1 | 1 click OR 1 reply | Domain 39 extension |
| 7 | Labor | 1 | 1 click OR 1 reply | Domain 59 |
| 8 | Mutual Aid | 1 | 1 click OR 1 reply | Domain 59 |

### Column Schema (Days 1–7 tracking)

| Col | Header | Data Type | Notes |
|-----|--------|-----------|-------|
| A | Constituency | Text | Pre-populated (see above) |
| B | Day7_Target | Integer | Pre-populated Score 3+ target |
| C | D1_Score3 | Integer | Day 1 (June 10) Score 3+ reply count from this constituency (manual entry) |
| D | D2_Score3 | Integer | Day 2 (June 11) |
| E | D3_Score3 | Integer | Day 3 (June 12) |
| F | D4_Score3 | Integer | Day 4 (June 13) |
| G | D5_Score3 | Integer | Day 5 (June 14) |
| H | D6_Score3 | Integer | Day 6 (June 15) |
| I | D7_Score3 | Integer | Day 7 (June 16/17 checkpoint) |
| J | Cumulative_Score3 | Formula | `=SUM(C2:I2)` |
| K | Any_Signal | Formula | `=IF(SUM(C2:I2)>0,"YES","NO")` — any Score 3+ at any point in window |
| L | Target_Met | Formula | `=IF(J2>=B2,"MET","NOT YET: "&J2&"/"&B2)` |
| M | Early_Trigger_Day | Formula | `=IF(COUNTIF(C2:I2,">0")=0,"",MATCH(TRUE,MMULT(TRANSPOSE(N(C2:I2>0)),ROW(C2:I2)^0)>0,0))` — returns first day a signal appeared; array formula requires Ctrl+Shift+Enter |
| N | Status | Formula | `=IF(K2="YES",IF(L2="MET","STRONG","BUILDING"),"NO SIGNAL")` |
| O | Phase2_Ready | Formula | `=IF(AND(K2="YES",J2>=1),"STAGE PHASE 2","HOLD")` |

### Summary Row (Row 10 below data)

```
Row 10, Col J:  =COUNTIF(K2:K8,"YES")  [Label: "Constituencies with any signal"]
Row 10, Col L:  =COUNTIF(L2:L8,"MET")  [Label: "Constituencies meeting target"]
Row 11:  =IF(J10>=4,"STRONG SIGNAL — PHASE 2 ACCELERATION",IF(J10>=3,"MODERATE — PHASE 2 ON SCHEDULE",IF(J10>=2,"MONITOR — CHECK WEAK CONSTITUENCIES",IF(J10>=1,"EARLY — ACTIVE MONITORING","NO SIGNAL — DIAGNOSE DELIVERY"))))
```

### Conditional Formatting for Column N

- Text is `STRONG` → green background
- Text is `BUILDING` → amber background
- Text is `NO SIGNAL` → red background

---

## 7. Tab 3: GIST_VELOCITY — Bitly Click Tracking

**Purpose**: Daily Bitly click log with velocity calculations per domain. Enables spike detection and hourly velocity reporting.

### Column Schema

| Col | Header | Data Type | Notes |
|-----|--------|-----------|-------|
| A | Date | Date | YYYY-MM-DD |
| B | Domain39_Clicks | Integer | Daily clicks on bit.ly/drp-d39 |
| C | Domain51_Clicks | Integer | Daily clicks on Domain 51 Bitly link |
| D | Domain56_Clicks | Integer | Daily clicks on bit.ly/drp-d56 |
| E | DRP_Proposal_Clicks | Integer | Daily clicks on bit.ly/drp-2026 |
| F | Other_Clicks | Integer | Any additional Bitly links |
| G | Daily_Total | Formula | `=SUM(B2:F2)` |
| H | Cumulative_Total | Formula | `=IF(ROW()=2,G2,H1+G2)` |
| I | Velocity_3Day_Avg | Formula | `=IF(ROW()<4,"",AVERAGE(G2:G(ROW()-2)))` — 3-day rolling average |
| J | Spike_Flag | Formula | `=IF(G2>=5,"SPIKE — LOG CAUSE","")` |
| K | Spike_Notes | Text | If SPIKE: record which link spiked, probable cause (email send day? organic amplification?) |

### Velocity Thresholds Reference Block (paste into rows 12–18)

```
Row 12:  24h Post-Send Target: 3+ clicks per domain link
Row 13:  48h Post-Send Target: 5+ clicks per domain link
Row 14:  Day 7 Cumulative Target (all links): 15+ total clicks
Row 15:  STRONG signal velocity: >2 clicks/hour in first 24h post-send
Row 16:  MODERATE signal velocity: 0.5–2 clicks/hour first 24h
Row 17:  WEAK signal velocity: <0.5 clicks/hour first 24h (less than 12 clicks in 24h)
Row 18:  Organic amplification signal: click spike >5 on a day with no send activity
```

### Domain-Specific Bitly Links (paste into rows 20–26 for reference)

| Domain | Bitly Short Link | Full Gist URL |
|--------|-----------------|---------------|
| Domain 39 (Healthcare) | bit.ly/drp-d39 | https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b |
| Domain 51 (Campaign Finance) | bit.ly/domain51-campaign-finance | https://gist.github.com/esca8peArtist/[D51-ID] |
| Domain 56 (Civil Service) | bit.ly/drp-d56 | https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f |
| DRP Full Proposal | bit.ly/drp-2026 | https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 |
| DRP Executive Summary | bit.ly/drp-summary | https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4 |

---

## 8. Tab 4: REPLY_LOG — Per-Reply Scoring

**Purpose**: One row per reply received. Feeds DAILY_SIGNALS and CONSTITUENCY_TRACKER through manual column H (Score 3+ count) updates. This is the source-of-truth for reply scoring.

### Column Schema

| Col | Header | Data Type | Notes |
|-----|--------|-----------|-------|
| A | Reply_ID | Text | R001, R002, R003… sequential |
| B | Date_Received | Date | YYYY-MM-DD |
| C | Organization | Text | Sending organization |
| D | Constituency | Text | One of 7 constituency values |
| E | Domain | Text | Which Phase 1 domain was mentioned in their reply |
| F | Reply_Type | Text | OOO / Acknowledgment / Substantive / Forward / Adoption |
| G | Score | Integer | 1–5 per scoring system |
| H | Score3_Flag | Formula | `=IF(G2>=3,"YES","")` |
| I | Early_Phase2_Trigger | Formula | `=IF(AND(G2>=3,OR(D2="Law School",D2="Imm Legal Aid",D2="Civil Rights")),"D58 SIGNAL",IF(AND(G2>=3,OR(D2="Labor",D2="Mutual Aid",D2="Academic")),"D59 SIGNAL",""))` |
| J | Action_Required | Text | YES / NO — whether a response is needed |
| K | Response_Sent | Text | YES / NO / PENDING |
| L | Key_Quote | Text | Direct quote or close paraphrase of most important sentence in reply |
| M | Routing_Note | Text | What routing decision this reply informs (see PHASE_1_IMPACT_EVALUATION_ROUTING.md) |
| N | Follow_Up_Tier | Text | HIGH / MEDIUM / LOW — determines template tier for follow-up (see PHASE_1_IMPACT_EVALUATION_ROUTING.md Section 3) |

### Aggregate Summary (paste into rows below data, starting at Row 102)

```
Row 102:  Total replies:                =COUNTA(A2:A100)-COUNTBLANK(A2:A100)
Row 103:  Score 3+ count:               =COUNTIF(G2:G100,">=3")
Row 104:  Score 4+ count:               =COUNTIF(G2:G100,">=4")
Row 105:  Score 5 (adoption):           =COUNTIF(G2:G100,5)
Row 106:  D58 signals:                  =COUNTIF(I2:I100,"D58 SIGNAL")
Row 107:  D59 signals:                  =COUNTIF(I2:I100,"D59 SIGNAL")
Row 108:  Pending responses:            =COUNTIF(K2:K100,"PENDING")
Row 109:  High-engagement orgs (5+ interactions flagged): =COUNTIF(N2:N100,"HIGH")
Row 110:  Law School Score 3+:          =COUNTIFS(D2:D100,"Law School",H2:H100,"YES")
Row 111:  Imm Legal Aid Score 3+:       =COUNTIFS(D2:D100,"Imm Legal Aid",H2:H100,"YES")
Row 112:  Civil Rights Score 3+:        =COUNTIFS(D2:D100,"Civil Rights",H2:H100,"YES")
Row 113:  Academic Score 3+:            =COUNTIFS(D2:D100,"Academic",H2:H100,"YES")
Row 114:  Faith Score 3+:               =COUNTIFS(D2:D100,"Faith",H2:H100,"YES")
Row 115:  Labor Score 3+:               =COUNTIFS(D2:D100,"Labor",H2:H100,"YES")
Row 116:  Mutual Aid Score 3+:          =COUNTIFS(D2:D100,"Mutual Aid",H2:H100,"YES")
```

---

## 9. Tab 5: THRESHOLDS — Reference Definitions

**Purpose**: A static reference tab. Never updated with data. Contains all threshold definitions for the June 10–17 window, pre-calculated from the existing PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md baseline data.

### Section A: 24-Hour Thresholds (check June 11 morning for June 10 send)

| Signal | Strong (>50% alert) | Moderate | Weak (<10% alert) |
|--------|---------------------|----------|-------------------|
| Email open rate | >50% in first 24h | 25–50% | <10% in first 24h |
| Bitly clicks (per domain link, 24h) | 5+ clicks | 2–4 clicks | 0–1 clicks |
| Reply count (any score) | 2+ replies | 1 reply | 0 replies |

### Section B: 7-Day Thresholds (Day 7 checkpoint targets for June 10 send)

| Metric | Strong | Moderate | Weak | Failure |
|--------|--------|----------|------|---------|
| Email open rate | ≥50% | 30–49% | 20–29% | <20% |
| Cumulative Bitly clicks (all links) | ≥15 | 8–14 | 3–7 | 0–2 |
| Total Score 3+ replies | ≥5 | 2–4 | 1 | 0 |
| Constituencies with any signal | 5–7 of 7 | 3–4 of 7 | 1–2 of 7 | 0 of 7 |
| Network/referral events | ≥2 | 1 | 0 with replies | 0 |

### Section C: Domain-Specific Baselines

Based on Phase 1 historical data from Domains 56, 39, and 42 distributions (May–June 2026):
- Law school faculty: typical reply window 3–7 days; 40–60% substantive reply rate when relevant
- Immigration legal aid: reply window 1–5 days; especially fast if active litigation pending
- Civil rights organizations: reply window 5–10 days; national directors slower than state directors
- Academic/policy researchers: reply window 7–14 days; Score 3+ in first 7 days is a strong signal
- Faith coalitions: reply window 5–10 days; lower baseline (~30% reply rate) but high adoption when engaged
- Labor unions: reply window 3–7 days; training calendar dependency; ask about upcoming training cycles
- Mutual aid networks: reply window 1–7 days (local coordinators faster than national umbrellas)

### Section D: Alert Firing Thresholds

Pre-calculated values for the ALERTS tab formulas:

| Alert Name | Condition | Response Required |
|-----------|-----------|-------------------|
| STRONG_24H | Open rate >50% in first 24h OR 3+ replies on Day 1 | Note in CHECKIN.md; prepare Phase 2 staging |
| WEAK_24H | 0 clicks AND 0 replies at 24h with confirmed delivery | Check spam filters; re-examine Bitly links in sent emails |
| BOUNCE_ALERT | 3+ bounces detected | Pause; verify delivery before any new sends |
| SPIKE_ORGANIC | Click spike on a day with no send activity | Log referring source; note in Network Map |
| SCORE5_OVERRIDE | Any Score 5 reply received | Immediate Phase 2 pre-activation — see ROUTING doc |
| SCORE4_CLUSTER | 2+ Score 4 replies in Days 1–7 | Pre-Day-30 strong signal — stage Phase 2 |

---

## 10. Tab 6: ALERTS — Auto-Calculated Alert Board

**Purpose**: A live alert board. Each row represents one alert condition. Formulas auto-detect when conditions are met. Check this tab first each morning before updating DAILY_SIGNALS.

### Column Schema

| Col | Header | Data Type | Notes |
|-----|--------|-----------|-------|
| A | Alert_Name | Text | Pre-populated (see below) |
| B | Condition | Text | Pre-populated description of what triggers this alert |
| C | Status | Formula | ACTIVE / CLEAR based on real-time data |
| D | Fired_Date | Formula | First date this alert was active |
| E | Routing_Action | Text | Pre-populated — what to do when this fires |

### Pre-Populated Alert Rows (copy rows 2–9)

**Row 2 — STRONG_24H**
```
A2: STRONG_24H
B2: Open rate >50% in first 24h OR Day 1 replies >= 3
C2: =IF(OR(DAILY_SIGNALS!J2>0.5,DAILY_SIGNALS!F2>=3),"ACTIVE","CLEAR")
D2: =IF(C2="ACTIVE",DAILY_SIGNALS!B2,"")
E2: Note in CHECKIN.md. Prepare Phase 2 staging (Domain 58/59). No action required yet.
```

**Row 3 — WEAK_24H**
```
A3: WEAK_24H
B3: 0 clicks AND 0 replies at end of Day 1 (confirmed send)
C3: =IF(AND(DAILY_SIGNALS!C2=0,DAILY_SIGNALS!F2=0,DAILY_SIGNALS!B2<>""),"ACTIVE","CLEAR")
D3: =IF(C3="ACTIVE",DAILY_SIGNALS!B2,"")
E3: Check Bitly links in sent emails. Verify delivery. Run manual spam-filter test to 2 contacts.
```

**Row 4 — BOUNCE_ALERT**
```
A4: BOUNCE_ALERT
B4: 3 or more total bounces detected
C4: =IF(MAX(DAILY_SIGNALS!K2:K9)>=3,"ACTIVE","CLEAR")
D4: =IF(C4="ACTIVE",INDEX(DAILY_SIGNALS!B2:B9,MATCH(3,DAILY_SIGNALS!K2:K9,1)),"")
E4: Pause all sends. Identify bounced addresses. Find corrections. Restart Day 7 clock.
```

**Row 5 — ORGANIC_SPIKE**
```
A5: ORGANIC_SPIKE
B5: Click spike (5+) on a day without a scheduled send
C5: =IF(COUNTIF(GIST_VELOCITY!J2:J9,"SPIKE*")>0,"ACTIVE","CLEAR")
D5: =IF(C5="ACTIVE",INDEX(GIST_VELOCITY!A2:A9,MATCH("SPIKE*",GIST_VELOCITY!J2:J9,0)),"")
E5: Log in Network Map tab. Note which link spiked. Identify referral source if possible.
```

**Row 6 — SCORE5_OVERRIDE**
```
A6: SCORE5_OVERRIDE
B6: Any Score 5 (adoption) reply received
C6: =IF(COUNTIF(REPLY_LOG!G2:G100,5)>0,"ACTIVE","CLEAR")
D6: =IF(C6="ACTIVE",INDEX(REPLY_LOG!B2:B100,MATCH(5,REPLY_LOG!G2:G100,0)),"")
E6: IMMEDIATE PHASE 2 PRE-ACTIVATION. See ROUTING doc Section 2.1. Do not wait for Day 7 checkpoint.
```

**Row 7 — SCORE4_CLUSTER**
```
A7: SCORE4_CLUSTER
B7: 2 or more Score 4 replies in Days 1-7
C7: =IF(COUNTIF(REPLY_LOG!G2:G100,4)>=2,"ACTIVE","CLEAR")
D7: =IF(C7="ACTIVE","See REPLY_LOG for dates","")
E7: Pre-Day-30 strong signal. Stage Domain 58/59 outreach. Confirm at Day 14 before sending.
```

**Row 8 — WEAK_DAY3**
```
A8: WEAK_DAY3
B8: Cumulative clicks <5 by end of Day 3 (June 12)
C8: =IF(AND(DAILY_SIGNALS!A4=3,DAILY_SIGNALS!C4<5),"ACTIVE","CLEAR")
D8: =IF(C8="ACTIVE",DAILY_SIGNALS!B4,"")
E8: Mid-course intervention window. Apply Modification 2 (framing revision) before any Day 4+ sends.
```

**Row 9 — STRONG_TRAJECTORY**
```
A9: STRONG_TRAJECTORY
B9: Cumulative clicks >=10 AND Score 3+ replies >=2 by Day 4
C9: =IF(AND(DAILY_SIGNALS!C5>=10,DAILY_SIGNALS!H5>=2),"ACTIVE","CLEAR")
D9: =IF(C9="ACTIVE",DAILY_SIGNALS!B5,"")
E9: Phase 1 on strong trajectory. Confirm Day 7 determination will be HOLD or STRONG. Begin Phase 2 prep.
```

### Conditional Formatting for Column C

- Text is `ACTIVE` → Background: #EA4335 (red) for rows 3–4, 8; #34A853 (green) for rows 2, 6, 7, 9; #FBBC04 (amber) for row 5
- Text is `CLEAR` → No fill

---

## 11. Tab 7: INTEGRATION

This tab is documented in PHASE_1_IMPACT_EVALUATION_INTEGRATION.md. It serves as the reconciliation zone between this real-time dashboard and the adoption-tracking-script.py post-hoc outputs.

---

## 12. Operational Instructions — Daily Routine (June 10–17)

### Morning Update Protocol (8–10 minutes each morning, 09:00–09:10 local time)

**Step 1: Bitly check (3 minutes)**
1. Open Bitly.com → login → click each Phase 1 domain link
2. Record yesterday's daily click total for each link in GIST_VELOCITY tab (one new row per day)
3. Update Column C (Cumulative_Bitly_Clicks) in DAILY_SIGNALS with new running total

**Step 2: Gmail reply audit (4 minutes)**
1. Open Gmail → search: `label:phase1-outreach/replies after:YYYY/MM/DD` (use yesterday's date)
2. Score each new reply using the 5-level scale
3. Add new rows to REPLY_LOG tab; enter Score, Constituency, Domain
4. Update Column F (Total_Replies) and Column H (Score3_Plus_Replies) in DAILY_SIGNALS

**Step 3: Alert board check (1 minute)**
1. Open ALERTS tab
2. Note any newly fired alerts (status changed from CLEAR to ACTIVE since yesterday)
3. If any alert is ACTIVE: follow the Routing_Action in Column E immediately
4. If SCORE5_OVERRIDE or BOUNCE_ALERT is ACTIVE: update CHECKIN.md before closing the sheet

**Step 4: Status note (1 minute)**
1. Enter one-line status note in Column N of today's DAILY_SIGNALS row
2. If Threshold_Status column shows anything other than HOLD or PENDING: note the specific observation

**Total: 8–10 minutes per day.**

### Checkpoint Protocol — Day 7 (June 17)

On June 17, the standard morning update feeds directly into the Day 7 checkpoint analysis. After completing the morning update:

1. Open PHASE_1_DAY_7_CHECKPOINT_DECISION_TREE.md
2. Pull three numbers from this dashboard: (a) Cumulative_Bitly_Clicks from DAILY_SIGNALS Row 9; (b) Total_Replies; (c) Bounces_Total
3. Use Day_7_Status cell (DAILY_SIGNALS Row 17) as a pre-calculated starting point
4. Run Part 1 of the decision tree (the dashboard has already done the click/bounce thresholds)
5. For constituency-level analysis: open CONSTITUENCY_TRACKER and read the Status column (Column N) for each of the 7 rows — this feeds Part 2 (Phase 2 Domain 58/59 activation)
6. Run the adoption-tracking-script.py --day7-report for the post-hoc verification layer

---

## 13. Pre-Population for June 10 Send

Before the June 10 send, complete the following pre-population steps (15 minutes):

**DAILY_SIGNALS tab**:
- Populate rows A2:B9 with day numbers and dates (pre-filled in this spec, Section 3)
- Set Column C–K values to blank for all rows (data fills in daily)
- Verify formulas in D, E, G, I, L, M columns are working by entering test data in Row 2 (C=5, F=1, H=1, K=0), confirm L shows HOLD, then clear test data

**CONSTITUENCY_TRACKER tab**:
- Rows 2–8 pre-populated with constituency names, targets, and primary domain assignments (see Section 6)
- Columns C–I start blank; data fills in daily as replies arrive
- Verify formulas in J, K, L, N, O columns

**THRESHOLDS tab**:
- All content is static — copy from Section 9 above; no data entry required

**ALERTS tab**:
- Rows 2–9 pre-populated with alert conditions and formulas (see Section 10)
- Verify Column C formulas update correctly by entering a test Score 5 in REPLY_LOG!G2, confirm SCORE5_OVERRIDE shows ACTIVE, then clear test data

**GIST_VELOCITY tab**:
- Enter the Bitly link registry from Section 7 into a notes block below the data area
- Leave data rows blank until June 10 evening (first data entry: June 10 click totals)

**REPLY_LOG tab**:
- Leave data rows blank until first reply received

---

## 14. Expected Data Pattern — June 10–17 Window

Based on Phase 1 historical data from Domains 56 and 39 (May–June 2026 distributions):

**Days 1–2 (June 10–11)**: Primary engagement window for recipients who act immediately. Expect 40–60% of total 7-day clicks to arrive in this window. Law schools and immigration legal aid contacts with active cases tend to click and reply quickly. If Day 2 cumulative clicks are below 5, that is an early warning — investigate by Day 3.

**Days 3–5 (June 12–14)**: Secondary engagement window. Contacts who received the email but deferred reading it. Also the window for replies from contacts who discuss the materials with colleagues before responding. Score 3+ replies tend to cluster in this window. If no Score 3+ replies by Day 5, the trajectory is MONITOR (not yet ESCALATE).

**Days 6–7 (June 15–17)**: Late engagement and organic amplification window. Contacts who forward the email to colleagues. Bitly spikes in this window with no corresponding send activity = organic amplification. Reply velocity typically drops in this window — this is normal and does not indicate declining engagement.

**Open rate floor**: Below 20% open rate by Day 7 warrants investigation (deliverability issue) regardless of other metrics. Above 40% open rate by Day 7 is strong; above 60% is exceptional for cold outreach.

---

## 15. Key Difference From Existing Infrastructure — Summary

| Capability | Existing (Weekly Batch) | This Dashboard (Real-Time) |
|-----------|------------------------|---------------------------|
| Engagement visibility | Day 7, Day 30, Day 60 snapshots | Daily cumulative + velocity |
| Alert system | Manual review at checkpoint | Auto-firing alert cells |
| Phase 2 signal detection | End-of-window analysis | Intra-window early trigger |
| Constituency tracking | Aggregate at checkpoint | Per-constituency daily view |
| Mid-course correction window | Day 7 (7-day lag) | Day 3 (3-day intervention window) |
| Time to status check | 15–20 minutes at checkpoint | 90 seconds (open sheet, check ALERTS tab) |
| Integration with script | Primary data source | Complement; script is post-hoc verifier |

The critical difference: if Domain 39's law school constituency shows 0 signals by Day 3 (June 12), this dashboard surfaces that as a WEAK alert at 9 AM on June 12 — giving you a 36-hour intervention window before the best-response window for late openers closes. The existing weekly batch system would surface this as a Day 7 finding on June 17, when the intervention window has passed.
