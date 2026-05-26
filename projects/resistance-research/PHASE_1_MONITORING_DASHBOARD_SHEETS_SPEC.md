---
title: "Phase 1 Impact Monitoring Dashboard — Google Sheets Specification"
created: 2026-05-26
version: 1.0
status: production-ready
scope: >
  Complete column-by-column specification for all 7 tabs of the Phase 1 Impact
  Dashboard Google Spreadsheet. Includes data types, validation rules, formula
  strings, and cross-sheet references. Use this as the authoritative schema when
  building or auditing the sheet.
companion_files:
  - PHASE_1_MONITORING_DASHBOARD.md
  - reply-triage-framework.md
  - gist-view-tracking-protocol.md
  - day-7-14-30-decision-trees.md
  - weekly-synthesis-template.md
  - phase-1-monitoring-sheets-template.csv
spreadsheet_title: "Phase 1 Impact Dashboard — May 28, 2026"
sharing: Anyone with link — Viewer
---

# Phase 1 Impact Monitoring Dashboard — Google Sheets Specification

**Version 1.0 — May 26, 2026**

This document is the authoritative reference for building the Google Sheets dashboard. Build the spreadsheet before May 27 evening so it is ready for the Domain 56 send on May 28.

Seven tabs, in order:
1. Contacts
2. Gist Views
3. Replies
4. Adoptions
5. Constituencies
6. Checkpoints
7. Network Map

---

## Tab 1: Contacts

**Purpose**: Master contact log. One row per contact. Updated each time a contact takes any action (send, reply, click).

**Row 1**: Headers (freeze this row)
**Rows 2–17**: Pre-populate from `phase-1-monitoring-sheets-template.csv` (16 contacts)
**Rows 18+**: Reserve for future contacts

### Column Schema

| Col | Header | Data Type | Allowed Values / Format | Notes |
|-----|--------|-----------|------------------------|-------|
| A | Contact_ID | Text | C001–C999 | Pre-filled. Never change after initial entry. |
| B | Full_Name | Text | Last, First OR Organization short name | Use org name for orgs without an individual contact |
| C | Organization | Text | Institution full name | |
| D | Domain | Text | Domain 56 / Domain 39 / Domain 42 | Add new values as new domains are distributed |
| E | Constituency | Text | Law School / Imm Legal Aid / Civil Rights / Academic / Faith / Labor / Mutual Aid | Use exactly these seven values — required for COUNTIFS in Constituencies tab |
| F | Tier | Text | Tier 1 / Tier 2 / Tier 3 | |
| G | Email | Text | Valid email address | |
| H | Send_Date | Date | YYYY-MM-DD | Fill on the date the email is sent |
| I | Delivery_Status | Text | Delivered / Bounced / OOO / Unknown / Opted Out | Update within 48h of send |
| J | Open_Date | Date | YYYY-MM-DD | Fill when Bitly confirms click from outreach window. Leave blank until confirmed. |
| K | Click_Date | Date | YYYY-MM-DD | Same as Open_Date for current tracking approach |
| L | Reply_Date | Date | YYYY-MM-DD | Fill with date of FIRST substantive non-OOO reply |
| M | Reply_Category | Text | Implementation Signal / Critique-Objection / Data Request / General Question / Partnership / Opt-Out / No Reply | Match categories in reply-triage-framework.md |
| N | Engagement_Score | Integer | 0 / 1 / 2 / 3 / 4 / 5 | 0 = no contact; 5 = confirmed adoption. See scoring decision tree in reply-triage-framework.md |
| O | Tier2_Candidate | Text | YES / blank | Set to YES when Engagement_Score >= 3 |
| P | Day_to_Open | Formula | `=IF(J2="","",J2-H2)` | Auto-calculates. Shows integer days from send to first click. |
| Q | Day_to_Click | Formula | `=IF(K2="","",K2-H2)` | Same calculation — alias for Day_to_Open in current setup |
| R | Day_to_Reply | Formula | `=IF(L2="","",L2-H2)` | Auto-calculates. Shows integer days from send to first reply. |
| S | Notes | Text | Free text | Record any context: forwarding mentions, specific claims, quotes |

### Summary Block Formulas (pin above data or in a separate named range)

Add these in a frozen summary block at the top of the sheet, or in a sidebar notes area:

```
Total contacts sent:        =COUNTA(H2:H200)-COUNTBLANK(H2:H200)
Confirmed delivered:        =COUNTIF(I2:I200,"Delivered")
Total replies:              =COUNTA(L2:L200)-COUNTBLANK(L2:L200)
Overall reply rate:         =Total replies / Confirmed delivered
Score 3+ count:             =COUNTIF(N2:N200,">=3")
Score 3+ rate:              =COUNTIF(N2:N200,">=3") / COUNTIF(I2:I200,"Delivered")
Tier 2 candidates:          =COUNTIF(O2:O200,"YES")
Avg day-to-open:            =AVERAGEIF(P2:P200,"<>")
Avg day-to-reply:           =AVERAGEIF(R2:R200,"<>")
Engagement velocity:        =(COUNTA(L2:L200)-COUNTBLANK(L2:L200)) / (TODAY()-MIN(H2:H200))
```

The `Engagement velocity` figure is replies per calendar day since the first send. Minimum target at Day 7: 0.3 (at least 2 replies in the first 7 days across all contacts).

### Conditional Formatting Rules

- Column N (Engagement_Score): Cell color green for values 4–5, yellow for 3, no fill for 0–2.
- Column I (Delivery_Status): Red fill for "Bounced", orange for "Unknown".
- Column O (Tier2_Candidate): Green fill for "YES".

---

## Tab 2: Gist Views

**Purpose**: Weekly Bitly click snapshot. One row per week. Never edit past rows — append only.

**Row 1**: Headers (freeze)
**Row 2**: Week 1 data (starting June 2)

### Column Schema

| Col | Header | Data Type | Allowed Values / Format | Notes |
|-----|--------|-----------|------------------------|-------|
| A | Week_Number | Integer | 1, 2, 3, … | Sequential starting from first send week |
| B | Week_End_Date | Date | YYYY-MM-DD (Sunday) | Record the Sunday closing the tracking week |
| C | Domain56_Clicks | Integer | 0+ | Bitly weekly clicks for bit.ly/drp-d56 |
| D | Domain39_Clicks | Integer | 0+ | Bitly weekly clicks for bit.ly/drp-d39 |
| E | DRP_Proposal_Clicks | Integer | 0+ | Bitly weekly clicks for bit.ly/drp-2026 |
| F | DRP_Summary_Clicks | Integer | 0+ | Bitly weekly clicks for bit.ly/drp-summary |
| G | LitigationTracker_Clicks | Integer | 0+ | Bitly weekly clicks for bit.ly/drp-litigation |
| H | Other_Links_Clicks | Integer | 0+ | Any additional Bitly links created |
| I | Total_Clicks_This_Week | Formula | `=SUM(C2:H2)` | Auto-calculates |
| J | Cumulative_Clicks | Formula | `=IF(A2=1,I2,J1+I2)` | Running total from Week 1 |
| K | Delta_vs_Prior_Week | Formula | `=IF(A2=1,"—",I2-I1)` | Shows weekly change; negative indicates declining velocity |
| L | Spike_Flag | Formula | `=IF(MAX(C2:H2)>=5,"SPIKE","")` | SPIKE if any single link had 5+ clicks |
| M | Spike_Notes | Text | Free text | Date of spike, likely cause, whether correlated with send |

### Weekly Targets (add as a frozen reference row or note)

| Week | End Date | Cumulative Target | Status Threshold |
|------|----------|------------------|-----------------|
| 1 | June 1 | 15+ | Below 5 = ESCALATE; 5–14 = MONITOR; 15+ = HOLD |
| 2 | June 8 | 30+ | Below 10 cumulative = FAILURE_IMMINENT |
| 3 | June 15 | 45+ | |
| 4 | June 22 | 60+ | Below 30 = add note to CHECKIN.md |
| 8 | July 20 | 100+ | By Day 60 checkpoint |

### Bitly Link Registry (paste into a note on this tab)

| Short Link | Full Gist URL | Back-half |
|-----------|--------------|-----------|
| bit.ly/drp-d56 | https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f | drp-d56 |
| bit.ly/drp-d39 | https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b | drp-d39 |
| bit.ly/drp-2026 | https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 | drp-2026 |
| bit.ly/drp-summary | https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4 | drp-summary |
| bit.ly/drp-litigation | https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0 | drp-litigation |

---

## Tab 3: Replies

**Purpose**: Per-reply log. One row per reply received, regardless of contact. A single contact who replies three times generates three rows. This is separate from the Contacts tab (which carries one row per contact and the highest/latest score).

**Row 1**: Headers (freeze)
**Row 2+**: One row per reply, appended in chronological order

### Column Schema

| Col | Header | Data Type | Allowed Values / Format | Notes |
|-----|--------|-----------|------------------------|-------|
| A | Reply_ID | Text | R001, R002, R003, … | Assign sequentially as replies arrive |
| B | Contact_ID | Text | C001–C999 | Cross-reference to Contacts tab Column A |
| C | Organization | Text | Free text | Pull from Contacts tab for consistency |
| D | Reply_Date | Date | YYYY-MM-DD | Date reply received in inbox |
| E | Reply_Category | Text | Implementation Signal / Critique-Objection / Data Request / General Question / Partnership / Opt-Out | Use exactly these values — must match Contacts!M |
| F | Engagement_Score | Integer | 0–5 | Score assigned per reply-triage-framework.md |
| G | Key_Content | Text | Free text — 1–3 sentences | Direct quote or close paraphrase of most important part of the reply |
| H | Action_Required | Text | Yes / No | YES if a response is required from you |
| I | Escalation_Flag | Text | ESCALATE / blank | ESCALATE if Score 4–5 or if a pattern trigger is met (see reply-triage-framework.md Section: Escalation Thresholds) |
| J | Disposition | Text | Responded / Pending / No-Action-Needed / Referred-to-User | Updated when response is sent or action taken |
| K | Notes | Text | Free text | Record any context not captured in Key_Content: follow-up commitments, FAQ topics extracted, referral mentions |

### Aggregate Formulas (add in a summary block below the data or in a sidebar)

```
Total replies logged:         =COUNTA(A2:A200)-COUNTBLANK(A2:A200)
Implementation Signals (Cat 1): =COUNTIF(E2:E200,"Implementation Signal")
Critique rate:                =COUNTIF(E2:E200,"Critique-Objection") / (COUNTA(A2:A200)-COUNTBLANK(A2:A200))
Score 3+ total:               =COUNTIF(F2:F200,">=3")
Escalation flags:             =COUNTIF(I2:I200,"ESCALATE")
Pending responses:            =COUNTIF(J2:J200,"Pending")
```

**Critique rate alert**: If `=COUNTIF(E2:E200,"Critique-Objection") / (COUNTA(A2:A200)-COUNTBLANK(A2:A200))` exceeds 0.30 in any rolling 14-day window, add a note to CHECKIN.md: "Critique rate above 30% — messaging review needed."

---

## Tab 4: Adoptions

**Purpose**: Confirmed and probable adoption signal log. One row per adoption event. An adoption event is any externally observable instance of Phase 1 materials being incorporated into practice, cited publicly, or forwarded into a new organization's pipeline.

**Row 1**: Headers (freeze)
**Row 2+**: Append-only. Never delete rows.

### Column Schema

| Col | Header | Data Type | Allowed Values / Format | Notes |
|-----|--------|-----------|------------------------|-------|
| A | Signal_ID | Text | A001, A002, … | Sequential |
| B | Date_Detected | Date | YYYY-MM-DD | Date you learned of the adoption event |
| C | Organization | Text | Institution name | |
| D | Constituency | Text | Same 7 values as Contacts!E | |
| E | Signal_Type | Text | Implementation / Referral / Citation / Partnership / Collaboration Request / Training Incorporation | Use these values consistently |
| F | Domains_Referenced | Text | Domain 56 / Domain 39 / multiple | Which Phase 1 domains are referenced in the adoption |
| G | Evidence_Source | Text | Email quote / URL / Call notes / Reply text | Where the evidence for this adoption was found |
| H | Verification_Status | Text | Confirmed / Probable / Unconfirmed | Confirmed = direct statement or published evidence; Probable = strong indirect evidence; Unconfirmed = initial indication only |
| I | People_Reached_Est | Integer | 0+ | Estimated downstream reach of this adoption (e.g., a clinic with 30 students = 30) |
| J | Network_Event | Text | YES / blank | YES if this adoption was triggered by a referral from another contact (not your direct outreach) |
| K | Description | Text | Free text — 2–5 sentences | Brief description of what was adopted, by whom, and how it is being used |

### Day 60 Target Formulas (add below data)

```
=IF(COUNTIF(H2:H200,"Confirmed")>=15,"DAY 60 TARGET MET","Confirmed: "&COUNTIF(H2:H200,"Confirmed")&" of 15")
=IF(SUM(I2:I200)>=100,"PEOPLE REACHED TARGET MET","Reached: "&SUM(I2:I200)&" of 100")
```

---

## Tab 5: Constituencies

**Purpose**: Aggregated metrics per constituency. Seven data rows — one per constituency. Used to determine whether the Day 30 STRONG threshold is met (4 of 7 constituencies at strong threshold). Formulas pull from Contacts tab.

**Row 1**: Headers (freeze)
**Rows 2–8**: One row per constituency (do not add rows)
**Row 10+**: Summary formulas below data rows

### Column Schema

| Col | Header | Data Type | Allowed Values / Format | Notes |
|-----|--------|-----------|------------------------|-------|
| A | Constituency_Name | Text | Law School / Imm Legal Aid / Civil Rights / Academic / Faith / Labor / Mutual Aid | Use exactly these values — must match Contacts!E for COUNTIFS to work |
| B | Contact_IDs | Text | Comma-separated list | e.g., "C001, C004, C006" — manual reference for auditability |
| C | Total_Contacts | Formula | `=COUNTIF(Contacts!E:E,A2)` | Auto-counts from Contacts tab |
| D | Confirmed_Delivered | Formula | `=COUNTIFS(Contacts!E:E,A2,Contacts!I:I,"Delivered")` | Auto-counts delivered contacts in this constituency |
| E | Any_Reply_Count | Formula | `=COUNTIFS(Contacts!E:E,A2,Contacts!L:L,"<>")` | Count of contacts in this constituency who replied at all |
| F | Score3Plus_Count | Formula | `=COUNTIFS(Contacts!E:E,A2,Contacts!N:N,">=3")` | Count of contacts in this constituency with Engagement_Score >= 3 |
| G | Score3Plus_Rate | Formula | `=IFERROR(F2/D2,"")` | Score3Plus_Count / Confirmed_Delivered |
| H | Day7_Status | Text | PASS / MONITOR / FAIL | Fill manually at Day 7 checkpoint: PASS if at least 1 Score 3+ reply; MONITOR if 0 replies but 1+ Bitly clicks; FAIL if 0 signals |
| I | Day30_Strong | Text | YES / NO | Fill manually at Day 30 checkpoint: YES if constituency has 3+ Score 3+ replies OR 1 Score 5 reply |
| J | Day30_Moderate | Text | YES / NO | Fill manually at Day 30: YES if constituency has 1–2 Score 3+ replies |
| K | Adoption_Signals | Formula | `=COUNTIFS(Adoptions!D:D,A2,Adoptions!H:H,"Confirmed")` | Count of confirmed adoption signals from this constituency |
| L | Status_Note | Text | Free text | Notes at checkpoint review: who responded, what they said, trend assessment |

### Pre-Populated Constituency Rows

Enter these 7 rows in A2:A8:
1. Law School
2. Imm Legal Aid
3. Civil Rights
4. Academic
5. Faith
6. Labor
7. Mutual Aid

### Phase 2 Trigger Formulas (add in rows 10–12 below data)

```
Row 10, Label: "Constituencies at Day30_Strong:"
Row 10, Formula: =COUNTIF(I2:I8,"YES")

Row 11, Label: "STRONG trigger:"
Row 11, Formula: =IF(COUNTIF(I2:I8,"YES")>=4,"STRONG — ACTIVATE PHASE 2 NOW","Not yet: "&COUNTIF(I2:I8,"YES")&" of 4 needed")

Row 12, Label: "MODERATE trigger:"
Row 12, Formula: =IF(COUNTIF(J2:J8,"YES")>=3,"MODERATE — ACTIVATE DOMAIN 39 NOW","Not yet: "&COUNTIF(J2:J8,"YES")&" of 3 needed")
```

---

## Tab 6: Checkpoints

**Purpose**: Append-only log of all checkpoint decisions. One row per checkpoint run. Never edit past rows. This is the audit trail of all Phase 1 go/no-go decisions.

**Row 1**: Headers (freeze)
**Row 2**: Day 7 checkpoint (~June 4–5)
**Row 3**: Day 14 checkpoint (~June 11–12, only if Day 7 = MONITOR)
**Row 4**: Day 30 checkpoint (~June 27–28)
**Row 5**: Day 60 checkpoint (~July 27–28)

### Column Schema

| Col | Header | Data Type | Allowed Values / Format | Notes |
|-----|--------|-----------|------------------------|-------|
| A | Checkpoint_Date | Date | YYYY-MM-DD | Actual date checkpoint was run |
| B | Checkpoint_Type | Text | Day 7 / Day 14 / Day 30 / Day 60 / Pre-Day-30 Score 5 Override / Pre-Day-30 Score 4 Cluster | "Override" entries are added when an early-trigger condition fires before the scheduled checkpoint |
| C | Overall_Reply_Rate | Decimal | 0.00–1.00 (e.g., 0.31 = 31%) | (Total replies with score 1+) / (Confirmed delivered) at time of checkpoint |
| D | Score3Plus_Rate | Decimal | 0.00–1.00 | (Count of Score 3+ replies) / (Confirmed delivered) |
| E | Constituencies_Strong | Integer | 0–7 | Count of constituencies with Day30_Strong = YES (or Day7 equivalent PASS) |
| F | Cross_Org_References | Integer | 0+ | Count of confirmed or probable referral events in Adoptions tab at this checkpoint date |
| G | Adoption_Signals | Integer | 0+ | Count of Confirmed adoption signals in Adoptions tab at this checkpoint date |
| H | Determination | Text | HOLD / MONITOR / ESCALATE / CONTACT_VERIFY / CONTINUE_MONITOR / FAILURE_IMMINENT / STRONG / MODERATE / WEAK / ASSESS / FAILURE / MOVEMENT / PARTIAL / BELOW_TARGET | Use exact values from day-7-14-30-decision-trees.md |
| I | Action_Taken | Text | Free text — 1–3 sentences | What action was executed after this determination (e.g., "Domain 39 distribution sent June 28", "Modification 2 framing revision applied") |
| J | Notes | Text | Free text | Any observations that don't fit the metric columns: unexpected contacts, delivery anomalies, external events that affected results |

### Pre-Checkpoint Checklist

Before entering any checkpoint row, pull these four numbers from the dashboard:
- (A) Score 3+ reply rate from Contacts tab summary block
- (B) Constituencies_Strong count from Constituencies tab Row 10
- (C) Cross-org references from Adoptions tab (count rows where Signal_Type = "Referral" and Verification_Status = "Confirmed" or "Probable")
- (D) Confirmed adoption signals from Adoptions tab (count rows where Verification_Status = "Confirmed")

Run the appropriate decision tree from `day-7-14-30-decision-trees.md`. Record the output determination in Column H. Record the action in Column I. Then write the same determination to CHECKIN.md.

---

## Tab 7: Network Map

**Purpose**: Tracks second-order network connections — contacts who were referred by Tier 1 contacts, or organizations that learned of the framework through forwarding rather than your direct outreach. Feeds the "Cross_Org_References" metric used in Day 30 checkpoint.

**Row 1**: Headers (freeze)
**Row 2+**: One row per network event

### Column Schema

| Col | Header | Data Type | Allowed Values / Format | Notes |
|-----|--------|-----------|------------------------|-------|
| A | Event_ID | Text | N001, N002, … | Sequential |
| B | Date_Detected | Date | YYYY-MM-DD | When you learned of the connection |
| C | Source_Contact_ID | Text | C001–C999 | The Tier 1 contact who made the referral |
| D | Source_Organization | Text | Institution name | |
| E | Referred_To | Text | Name or organization of the referred party | May be unknown — enter "Unknown" if a spike indicates forwarding but you don't yet know who received it |
| F | Referred_Domain | Text | Domain 56 / Domain 39 / Other | Which document was forwarded |
| G | Evidence | Text | "Reply quote" / "Bitly spike [date]" / "New contact email from [Org]" | What evidence confirms the referral |
| H | Verification_Status | Text | Confirmed / Probable / Unconfirmed | Confirmed if the referred party contacts you directly |
| I | Referred_Party_Reply | Text | YES / NO / Pending | Did the referred party reply to you? |
| J | Notes | Text | Free text | Any follow-up context |

### Cross-Reference to Adoptions

When a network event results in a confirmed adoption from the referred party, link it:
- Create a row in Adoptions tab with Signal_Type = "Referral" and Network_Event = YES
- In the Adoptions row, reference the Network Map Event_ID in the Description column

---

## Setup Verification Checklist

Run this before May 27 evening:

**Sheet structure** (5 minutes):
- [ ] Spreadsheet created with title: "Phase 1 Impact Dashboard — May 28, 2026"
- [ ] 7 tabs present with exact names: Contacts, Gist Views, Replies, Adoptions, Constituencies, Checkpoints, Network Map
- [ ] Sharing set to "Anyone with link can view"
- [ ] Share URL copied to CHECKIN.md

**Contacts tab** (15 minutes):
- [ ] Row 1 headers match Column Schema above
- [ ] All 16 contacts imported from phase-1-monitoring-sheets-template.csv
- [ ] Sample row (row 18 in CSV) deleted
- [ ] Summary formulas verified (test: enter a Send_Date in Column H for C001; confirm velocity formula updates)
- [ ] Column E values match exactly: no spelling variation from the seven allowed constituency values

**Gist Views tab** (5 minutes):
- [ ] Headers match Column Schema above
- [ ] Bitly link registry pasted in a tab note or a cell below the data area
- [ ] Test: enter dummy Week 1 data; confirm Total_Clicks_This_Week, Cumulative_Clicks, and Delta formulas calculate correctly

**Replies tab** (5 minutes):
- [ ] Headers match Column Schema above (including Notes in Column K)
- [ ] Test: enter one dummy reply row; confirm Escalation_Flag and Disposition columns accept the allowed values

**Constituencies tab** (10 minutes):
- [ ] Rows 2–8 pre-populated with the 7 constituency names (exact values)
- [ ] Contact_IDs column manually populated for each constituency
- [ ] COUNTIF formulas verified: C2 should equal total contacts with "Law School" in Contacts!E

**Checkpoints tab** (2 minutes):
- [ ] Headers in place, rows empty, ready for Day 7 entry on June 4–5

**Network Map tab** (2 minutes):
- [ ] Headers in place, rows empty

---

## Schema Cross-Reference Map

Fields that must match exactly between tabs (spelling and case-sensitive):

| Field | Contacts | Replies | Constituencies | Adoptions |
|-------|----------|---------|----------------|-----------|
| Contact_ID | Col A | Col B | — (Col B list) | — |
| Constituency | Col E | — | Col A | Col D |
| Engagement_Score | Col N | Col F | — (via formula) | — |
| Reply_Category | Col M | Col E | — | — |
| Verification_Status | — | — | — | Col H |

Consistency in the Constituency field is the most failure-prone point. If you enter "Immigration Legal Aid" in some rows and "Imm Legal Aid" in others, the COUNTIFS formulas in the Constituencies tab will undercount. Use exactly: Law School / Imm Legal Aid / Civil Rights / Academic / Faith / Labor / Mutual Aid.

---

**Status**: Production-ready. Build the spreadsheet before May 27 evening. First data entry: Domain 56 send date (May 28) in Contacts!H for all 11 Domain 56 contacts.
