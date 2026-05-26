---
title: "Google Sheets Template — Phase 1 Unified Monitoring"
created: 2026-05-27
version: 1.0
status: production-ready
scope: >
  Complete Google Sheets setup guide for unified Domain 56 + Domain 39 monitoring.
  Includes exact column schemas, copy-paste formulas, and a CSV import template.
  The Bitly short link creation process is documented here alongside sheet setup.
setup_time_estimate: "45–60 minutes (one-time)"
weekly_maintenance_time: "5 minutes"
---

# Google Sheets Template — Phase 1 Unified Monitoring

**Create this spreadsheet before May 28.** The setup below is the complete specification — follow it in order and you will have a fully functional dashboard within 60 minutes.

---

## Step 1: Create the Spreadsheet

Open Google Sheets (sheets.google.com) and create a new blank spreadsheet.

**Title**: `Phase 1 Impact Dashboard — Domain 56 + Domain 39`

**Sharing**: Click Share (top right) > Change to "Anyone with the link" > Set to Viewer > Copy link. Paste this link into CHECKIN.md under the heading: `Dashboard URL: [paste here]`

**Create 7 tabs** by clicking the + button at the bottom of the screen:
1. `Contacts`
2. `Gist_Views`
3. `Replies`
4. `Adoptions`
5. `Constituencies`
6. `Checkpoints`
7. `Synthesis_Log`

---

## Step 2: Contacts Tab — Exact Column Schema

Copy this header row into Row 1 of the Contacts tab:

```
Contact_ID | Full_Name | Organization | Domain | Constituency | Tier | Email | Send_Date | Delivery_Status | Open_Date | Click_Date | Reply_Date | Reply_Category | Engagement_Score | Tier2_Candidate | Day_to_Open | Day_to_Click | Day_to_Reply | Referral_Made | Notes
```

**Pre-populated contact rows** — copy these 16 rows into the Contacts tab starting at Row 2:

| Contact_ID | Full_Name | Organization | Domain | Constituency | Tier | Email | Notes |
|-----------|-----------|-------------|--------|-------------|------|-------|-------|
| C001 | Partnership for Public Service | Partnership for Public Service | Domain 56 | Civil Service Reform | Tier 1 | [verify before send] | Civil service reform org. Primary Domain 56 audience. |
| C002 | Government Accountability Project | Government Accountability Project | Domain 56 | Civil Rights / Rule of Law | Tier 1 | [verify before send] | Whistleblower protection. |
| C003 | AFGE | American Federation of Government Employees | Domain 56 | Federal Employee Union | Tier 1 | [verify before send] | Federal employee union. Direct Domain 56 constituency. |
| C004 | Protect Democracy | Protect Democracy | Domain 56 | Civil Rights / Rule of Law | Tier 1 | [verify before send] | Rule-of-law litigation org. |
| C005 | NTEU | National Treasury Employees Union | Domain 56 | Federal Employee Union | Tier 1 | [verify before send] | Federal employee union. |
| C006 | Volcker Alliance | Volcker Alliance | Domain 56 | Civil Service Reform | Tier 2 | volcker@volckeralliance.org | Good government / civil service reform. May 28 Tier 2 send. |
| C007 | Democracy Forward | Democracy Forward | Domain 56 | Civil Rights / Rule of Law | Tier 2 | info@democracyforward.org | Litigation org. May 28 Tier 2 send. Priority contact. |
| C008 | CREW | Citizens for Responsibility and Ethics in Washington | Domain 56 | Watchdog / Media | Tier 2 | citizensforethics.org/contact (form) | Contact form submission. May 28. |
| C009 | Government Executive | Government Executive | Domain 56 | Watchdog / Media | Tier 2 | editors@govexec.com | Op-ed pitch format. May 28. Response window: 10 days. |
| C010 | Brookings Governance Studies | Brookings Institution | Domain 56 | Academic | Tier 3 | [verify before send] | Send by June 7 regardless of Tier 2 response. |
| C011 | NAPA | National Academy of Public Administration | Domain 56 | Academic | Tier 3 | [verify before send] | Send by June 7. H.R. 492 markup window. |
| C012 | Georgetown CCF | Georgetown University Center for Children and Families | Domain 39 | Healthcare Policy | Tier 1 | childhealth@georgetown.edu | CRITICAL: use childhealth@ not ccf@. Send May 30. Highest-value D39 contact. |
| C013 | National Health Law Program | National Health Law Program | Domain 39 | Healthcare Policy | Tier 1 | info@healthlaw.org | Litigation-oriented healthcare org. Send May 30. |
| C014 | Brennan Center for Justice | Brennan Center for Justice | Domain 39 | Civil Rights / Rule of Law | Tier 1 | kennardl@brennan.law.nyu.edu | Democracy + healthcare intersection. Send June 1. |
| C015 | Institute for Responsive Government | Institute for Responsive Government | Domain 39 | Healthcare Policy | Tier 1 | info@responsivegov.org | Healthcare + civic engagement. Send June 1. |
| C016 | Black Mamas Matter Alliance | Black Mamas Matter Alliance | Domain 39 | Maternal Health | Tier 1 | info@blackmamasmatter.org | Maternal health advocacy. Send June 2–3. |

**Formulas for calculated columns** — enter in Row 2, then copy down through Row 20:
- Column P (Day_to_Open): `=IF(J2="","",J2-H2)`
- Column Q (Day_to_Click): `=IF(K2="","",K2-H2)`
- Column R (Day_to_Reply): `=IF(L2="","",L2-H2)`

**Auto-calculation summary block** — enter these formulas in Rows 22–31 (two rows below your data):

| Row | Label | Formula |
|-----|-------|---------|
| 22 | Total contacts sent | `=COUNTA(H2:H20)-COUNTBLANK(H2:H20)` |
| 23 | Confirmed delivered | `=COUNTIF(I2:I20,"Delivered")` |
| 24 | Total replies | `=COUNTA(L2:L20)-COUNTBLANK(L2:L20)` |
| 25 | Overall reply rate | `=I24/I23` (format as percentage) |
| 26 | Score 3+ count | `=COUNTIF(N2:N20,">=3")` |
| 27 | Score 3+ rate | `=I26/I23` (format as percentage) |
| 28 | Tier 2 candidates | `=COUNTIF(O2:O20,"YES")` |
| 29 | Avg day-to-reply | `=AVERAGE(R2:R20)` |
| 30 | Engagement velocity | `=I24/MAX(1,(TODAY()-MIN(H2:H20)))` |
| 31 | Cross-org references | `=COUNTA(S2:S20)-COUNTBLANK(S2:S20)` |

---

## Step 3: Gist_Views Tab — Exact Column Schema

Row 1 headers:

```
Week_Number | Week_End_Date | D56_Clicks | D39_Clicks | DRP_Proposal_Clicks | DRP_Summary_Clicks | Other_Clicks | Total_This_Week | Cumulative | Delta_vs_Prior | Spike_Flag | Spike_Notes
```

**Formulas** (enter in Row 2, copy down through Row 20):
- Column H (Total_This_Week): `=SUM(C2:G2)`
- Column I (Cumulative): `=IF(A2=1,H2,I1+H2)`
- Column J (Delta_vs_Prior): `=IF(A2=1,"—",H2-H1)`
- Column K (Spike_Flag): `=IF(MAX(C2:G2)>=5,"SPIKE","")`

**Weekly targets** (freeze these in Row 1 as a note or in a separate frozen row):
- Week 1 (by June 4): 15+ total clicks
- Week 2 (by June 11): 25+ cumulative
- Week 4 (by June 25): 50+ cumulative
- Week 8 (by July 23): 100+ cumulative

---

## Step 4: Replies Tab — Exact Column Schema

Row 1 headers:

```
Reply_ID | Contact_ID | Organization | Reply_Date | Reply_Category | Engagement_Score | Key_Content | Action_Required | Escalation_Flag | Disposition
```

Values for Reply_Category: `Implementation Signal / Critique-Objection / Data Request / General Question / OOO Only`

Values for Escalation_Flag: `YES / blank` (YES if this reply triggers any escalation action from REPLY_TRIAGE_FRAMEWORK.md)

Values for Disposition: `Responded / Pending / No Action Required`

---

## Step 5: Adoptions Tab — Exact Column Schema

Row 1 headers:

```
Signal_ID | Date_Detected | Organization | Constituency | Signal_Type | Domains_Referenced | Evidence_Source | Verification_Status | People_Reached_Est | Network_Event | Description
```

Values for Signal_Type: `Curriculum Integration / Litigation Use / Policy Brief Citation / Training Integration / Public Comment Citation / Media Coverage / Referral / Governance Integration`

Values for Verification_Status: `Confirmed / Probable / Unconfirmed`

**Day 60 progress formulas** (add below data rows):

```
=COUNTIF(H2:H100,"Confirmed")                            [confirmed adoption count]
=IF(COUNTIF(H2:H100,"Confirmed")>=15,"DAY 60 TARGET MET","Confirmed: "&COUNTIF(H2:H100,"Confirmed")&"/15")
=SUM(I2:I100)                                            [total people reached estimate]
=IF(SUM(I2:I100)>=100,"PEOPLE TARGET MET","Reached: "&SUM(I2:I100)&"/100")
```

---

## Step 6: Constituencies Tab — Exact Column Schema

Seven data rows, one per constituency. Row 1 headers:

```
Constituency | Total_Contacts | Confirmed_Delivered | Any_Reply_Count | Score3Plus_Count | Score3Plus_Rate | Day7_Status | Day30_Strong | Day30_Moderate | Adoption_Signals | Status_Note
```

**Constituency rows** (enter these labels in Column A, Rows 2–8):
1. Civil Service Reform
2. Federal Employee Union
3. Civil Rights / Rule of Law
4. Watchdog / Media
5. Healthcare Policy
6. Maternal Health
7. Academic

Values for Day7_Status: `PASS / MONITOR / FAIL`
Values for Day30_Strong and Day30_Moderate: `YES / NO`

**Cross-constituency formulas** (for each row, substitute the constituency name):

For Civil Service Reform (Row 2):
```
Total contacts:        =COUNTIF(Contacts!D:D,"Civil Service Reform")
Confirmed delivered:   =COUNTIFS(Contacts!D:D,"Civil Service Reform",Contacts!I:I,"Delivered")
Any replies:           =COUNTIFS(Contacts!D:D,"Civil Service Reform",Contacts!L:L,"<>")
Score 3+ count:        =COUNTIFS(Contacts!D:D,"Civil Service Reform",Contacts!N:N,">=3")
Score 3+ rate:         =E2/C2
```
Repeat for all 7 constituencies substituting the constituency name.

**Phase 2 trigger formulas** (add below Row 8):
```
=COUNTIF(H2:H8,"YES")                                             [constituencies passing Day30 Strong]
=IF(COUNTIF(H2:H8,"YES")>=4,"STRONG — ACTIVATE PHASE 2","Not yet: "&COUNTIF(H2:H8,"YES")&"/4 needed")
=IF(COUNTIF(I2:I8,"YES")>=3,"MODERATE — ACTIVATE DOMAIN 39 TIER 2","Not yet: "&COUNTIF(I2:I8,"YES")&"/3 needed")
```

---

## Step 7: Checkpoints Tab — Exact Column Schema

**Append-only** — never edit past rows.

Row 1 headers:

```
Checkpoint_Date | Checkpoint_Type | Overall_Reply_Rate | Score3Plus_Rate | Constituencies_Strong | Cross_Org_References | Adoption_Signals | Determination | Action_Taken | Notes
```

Values for Checkpoint_Type: `Day 7 (D56) / Day 7 (D39) / Day 14 / Day 30 / Day 45 (extended) / Day 60`

Values for Determination: `HOLD / MONITOR / ESCALATE` (Day 7) or `STRONG / MODERATE / WEAK / FAILURE` (Day 30/60)

Pre-populate with your scheduled checkpoint dates (fill Checkpoint_Date column):
- Row 2: June 4, 2026 (Day 7 — D56)
- Row 3: June 8, 2026 (Day 7 — D39)
- Row 4: June 11, 2026 (Day 14)
- Row 5: June 27, 2026 (Day 30)

---

## Step 8: Synthesis_Log Tab — Exact Column Schema

Row 1 headers:

```
Week_Number | Date_Range | D56_Days_Since_Send | D39_Days_Since_Send | D56_Clicks_This_Week | D39_Clicks_This_Week | Total_Replies_This_Week | Total_Replies_Cumulative | Score3Plus_This_Week | Tier2_Candidates | Confirmed_Adoptions | Cross_Org_Refs | Key_Findings | Problem_Signals | Decision_Prompt_Status
```

Values for Decision_Prompt_Status: `YES-ESCALATE / NOT YET / NEEDS INPUT`

Fill one row per week starting the week of June 2.

---

## Step 9: Bitly Link Creation

**Required before May 28.** Takes 5 minutes at bitly.com (free account is sufficient).

**Links to create**:

| Back-Half to Use | Gist URL to Shorten |
|-----------------|---------------------|
| `drp-d56` | https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f |
| `drp-d39` | https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b |
| `drp-2026` | https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 |
| `drp-summary` | https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4 |

**Process for each link**:
1. Go to app.bitly.com > Create Link
2. Paste the Gist URL
3. Click "Edit back-half" and enter the back-half from the table above
4. Save
5. Click the new short link yourself — verify it resolves to the correct Gist
6. Check the Bitly dashboard: your test click should appear within 2–5 minutes

**Optional per-recipient links for Domain 56 Tier 2 sends (May 28)**:

| Back-Half | Recipient |
|-----------|-----------|
| `d56-volcker` | Volcker Alliance (May 28) |
| `d56-demfwd` | Democracy Forward (May 28) |
| `d56-crew` | CREW (May 28) |
| `d56-govexec` | Government Executive (May 28) |

Per-recipient links let you see exactly which organization clicked through. All four link to the same Domain 56 Gist. Optional but recommended for the highest-value contacts.

**Record all created Bitly links here**:

```
drp-d56:      https://bit.ly/drp-d56          [created: _____________]
drp-d39:      https://bit.ly/drp-d39          [created: _____________]
drp-2026:     https://bit.ly/drp-2026         [created: _____________]
drp-summary:  https://bit.ly/drp-summary      [created: _____________]
d56-volcker:  https://bit.ly/d56-volcker      [created: _____________] (optional)
d56-demfwd:   https://bit.ly/d56-demfwd       [created: _____________] (optional)
d56-crew:     https://bit.ly/d56-crew         [created: _____________] (optional)
d56-govexec:  https://bit.ly/d56-govexec      [created: _____________] (optional)
```

---

## Final Verification Checklist (Complete by May 27 Evening)

- [ ] Spreadsheet created with correct title
- [ ] All 7 tabs created with exact names
- [ ] 16 contacts in Contacts tab (or from CSV template import)
- [ ] Auto-calculation formulas working (test: manually enter a dummy value in H2, verify I22 increments)
- [ ] Gist_Views tab headers in place with formulas
- [ ] Share link set to "Anyone with link — Viewer"
- [ ] Dashboard URL pasted into CHECKIN.md
- [ ] drp-d56 Bitly link created and tested
- [ ] drp-d39 Bitly link created and tested
- [ ] Bitly links confirmed working (counter increments on test click)
- [ ] Domain 56 email templates updated to use drp-d56 Bitly link (not raw Gist URL)
- [ ] Google Alerts created (3 alerts per Section 1.8 of PHASE_1_IMPACT_MONITORING_DASHBOARD.md)
- [ ] June 4, June 8, June 11, June 27 checkpoints in calendar

---

## Quick Formula Reference Card

Print or keep this open during data entry:

```
-- CONTACTS TAB --
Day_to_Open:      =IF(J2="","",J2-H2)
Day_to_Click:     =IF(K2="","",K2-H2)
Day_to_Reply:     =IF(L2="","",L2-H2)
Reply rate:       =COUNTA(L2:L20)/COUNTIF(I2:I20,"Delivered")
Score 3+ rate:    =COUNTIF(N2:N20,">=3")/COUNTIF(I2:I20,"Delivered")
Velocity:         =COUNTA(L2:L20)/MAX(1,(TODAY()-MIN(H2:H20)))

-- GIST_VIEWS TAB --
Total this week:  =SUM(C2:G2)
Cumulative:       =IF(A2=1,H2,I1+H2)
Delta:            =IF(A2=1,"—",H2-H1)
Spike flag:       =IF(MAX(C2:G2)>=5,"SPIKE","")

-- ADOPTIONS TAB --
Confirmed count:  =COUNTIF(H2:H100,"Confirmed")
Target check:     =IF(COUNTIF(H2:H100,"Confirmed")>=15,"MET","")

-- CONSTITUENCIES TAB --
Phase 2 trigger:  =IF(COUNTIF(H2:H8,"YES")>=4,"STRONG — ACTIVATE","Not yet")
```

---

*The CSV template for bulk import is at `projects/resistance-research/phase-1-monitoring-sheets-template.csv` in the root resistance-research directory. That template has the same 16 contacts pre-populated and can be imported directly into Google Sheets via File > Import > Upload.*
