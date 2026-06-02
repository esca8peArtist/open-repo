---
title: "Phase 1 Weekly Measurement Templates — Weeks 2-4"
created: 2026-06-02
version: 1.0
status: production-ready
scope: >
  Google Sheets formulas, automated trending analysis, and Week 2-4 synthesis templates.
  Designed for a solo non-technical operator. Copy-paste formulas throughout.
  No manual arithmetic after initial setup.
companion: "PHASE_1_MEASUREMENT_SPREADSHEET_SPEC.md (full schema), PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md (Week-N template)"
week_1_template: "PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md — use for Week 1 and all subsequent weeks"
---

# Phase 1 Weekly Measurement Templates — Weeks 2-4

**Scope**: Google Sheets formula reference for automated trending analysis, plus annotated guidance for interpreting Weeks 2-4 data patterns relative to Phase 2 Domain 58/59 activation decisions.

**Week 1 template**: Use `PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md` for all synthesis work. This document covers the *formulas* that automate the underlying arithmetic and the *interpretation frameworks* for Weeks 2-4 that differ from Week 1.

---

## Part 1: Complete Google Sheets Formula Reference

These formulas belong in your `Phase 1 Impact Dashboard — June 2026` spreadsheet. All formulas reference the canonical 7-tab structure. Enter them once; they auto-update as you add data.

---

### Tab 1 — Contacts: Summary Block Formulas

Place labels in Column A, formulas in Column B (Row 1 area, above the header row):

```
Total contacts:        =COUNTA(A3:A200)-COUNTBLANK(A3:A200)
Delivered:             =COUNTIF(G3:G200,"Delivered")
Bounced:               =COUNTIF(G3:G200,"Bounced")
OOO (pending):         =COUNTIF(G3:G200,"OOO")
Any reply:             =COUNTA(H3:H200)-COUNTBLANK(H3:H200)
Reply rate:            =IFERROR((COUNTA(H3:H200)-COUNTBLANK(H3:H200))/COUNTIF(G3:G200,"Delivered"),0)
Score 3+ replies:      =COUNTIF(I3:I200,">=3")
Score 3+ rate:         =IFERROR(COUNTIF(I3:I200,">=3")/COUNTIF(G3:G200,"Delivered"),0)
Score 4+ replies:      =COUNTIF(I3:I200,">=4")
Score 5 replies:       =COUNTIF(I3:I200,"=5")
Referrals made:        =COUNTA(K3:K200)-COUNTBLANK(K3:K200)
Adoption signals:      =COUNTA(L3:L200)-COUNTBLANK(L3:L200)
Tier 2 candidates:     =COUNTIF(N3:N200,"Tier2")
```

Format Reply rate and Score 3+ rate as percentages with 1 decimal place: select cell > Format > Number > Percent.

---

### Tab 2 — Gist_Views: Weekly Click Tracking and Trend Formulas

**Header row (Row 1)**:
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

**Row formulas** (enter in Row 2, drag down for each new week):

Column I (Total_Week):
```
=SUM(C2:H2)
```

Column J (Cumulative — running total):
```
=SUM($I$2:I2)
```

Column K (Spike_Flag — any single link >= 5 clicks):
```
=IF(MAX(C2:H2)>=5,"FLAG","")
```

**Weekly target reference block** (place in columns N-O, Row 1):

| N | O |
|---|---|
| Week | Cumulative Target |
| 1 | 15 |
| 2 | 25 |
| 4 | 50 |
| 8 | 100 |

**Target tracking formula** (place below the data, labeled):
```
Week N target:           =IFERROR(VLOOKUP(MAX(A2:A100),N2:O10,2,FALSE),"N/A")
Current cumulative:      =MAX(J2:J100)
On target?:              =IF(MAX(J2:J100)>=IFERROR(VLOOKUP(MAX(A2:A100),N2:O10,2,FALSE),0),"ON TARGET","BELOW — "&(IFERROR(VLOOKUP(MAX(A2:A100),N2:O10,2,FALSE),0)-MAX(J2:J100))&" clicks behind")
```

**Week-over-week trend formula** (add labeled row below data):
```
Click delta (latest vs. prior week):   =IFERROR(INDEX(I2:I100,MATCH(MAX(A2:A100),A2:A100,0))-INDEX(I2:I100,MATCH(MAX(A2:A100)-1,A2:A100,0)),"First week")
Trend direction:                        =IF(IFERROR(INDEX(I2:I100,MATCH(MAX(A2:A100),A2:A100,0))-INDEX(I2:I100,MATCH(MAX(A2:A100)-1,A2:A100,0)),1)>0,"ACCELERATING","DECLINING")
```

---

### Tab 3 — Replies: Entry and Auto-Fill

**Header row**:
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

**Auto-fill Constituency from Contacts tab** (Column F, Row 2 — drag down to F200):
```
=IFERROR(VLOOKUP(B2,Contacts!A:D,4,FALSE),"")
```

**Data validation rules**:
- Column E (Reply_Type): Dropdown — `OOO,Ack,Question,Forward,Adoption,Referral,Decline`
- Column D (Reply_Score): Number validation — between 1 and 5
- Column J (Follow_Up_Required): Dropdown — `Yes,No,Sent`

**Reply summary block** (place to the right, columns M-N):

| Label | Formula |
|-------|---------|
| Total replies logged | `=COUNTA(A2:A200)-COUNTBLANK(A2:A200)` |
| Score 3+ replies | `=COUNTIF(D2:D200,">=3")` |
| Score 4+ replies | `=COUNTIF(D2:D200,">=4")` |
| Score 5 replies | `=COUNTIF(D2:D200,"=5")` |
| Forwards stated | `=COUNTIF(E2:E200,"Forward")` |
| Pending follow-ups | `=COUNTIF(J2:J200,"Yes")` |
| By constituency — Law School | `=COUNTIFS(F2:F200,"Law School",D2:D200,">=3")` |
| By constituency — Imm Legal Aid | `=COUNTIFS(F2:F200,"Imm Legal Aid",D2:D200,">=3")` |
| By constituency — Civil Rights | `=COUNTIFS(F2:F200,"Civil Rights",D2:D200,">=3")` |
| By constituency — Academic | `=COUNTIFS(F2:F200,"Academic",D2:D200,">=3")` |
| By constituency — Faith | `=COUNTIFS(F2:F200,"Faith",D2:D200,">=3")` |
| By constituency — Labor | `=COUNTIFS(F2:F200,"Labor",D2:D200,">=3")` |
| By constituency — Mutual Aid | `=COUNTIFS(F2:F200,"Mutual Aid",D2:D200,">=3")` |

These constituency-level Score 3+ counts are the primary inputs for the Day 7 Phase 2 activation checks (Domain 58: Law School + Civil Rights + Imm Legal Aid; Domain 59: Labor + Mutual Aid + Academic).

---

### Tab 4 — Adoptions: Registry and Gate Calculations

**Header row**:
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

**Data validation**:
- Column E (Signal_Type): Dropdown — `Curriculum,Litigation Toolkit,Policy Brief,Training Module,Governance Doc,Citation,Other`
- Column G (Evidence_Source): Dropdown — `Reply Email,Survey,Web Detection,PACER,Direct Confirmation`
- Column H (Verification): Dropdown — `Confirmed,Probable,Unconfirmed`
- Column J (Network_Event): Dropdown — `YES,NO`

**Automated summary block** (place below data):

| Label | Formula |
|-------|---------|
| Confirmed adoptions | `=COUNTIF(H2:H200,"Confirmed")` |
| Probable adoptions | `=COUNTIF(H2:H200,"Probable")` |
| Total signals | `=COUNTA(A2:A200)-COUNTBLANK(A2:A200)` |
| Est. people reached | `=SUM(I2:I200)` |
| Network events | `=COUNTIF(J2:J200,"YES")` |
| Day 60 adoption gate | `=IF(COUNTIF(H2:H200,"Confirmed")>=15,"THRESHOLD MET","Need "&(15-COUNTIF(H2:H200,"Confirmed"))&" more confirmed")` |
| Day 60 people gate | `=IF(SUM(I2:I200)>=100,"THRESHOLD MET","Need "&(100-SUM(I2:I200))&" more people reached")` |

---

### Tab 5 — Constituencies: Decision-Facing View

This tab has 7 fixed rows (one per constituency) plus formula columns. It is the sheet you read during all checkpoint reviews.

**Enter these 7 fixed labels in Column A, Rows 2-8**:
```
Row 2: Law School
Row 3: Imm Legal Aid
Row 4: Civil Rights
Row 5: Academic
Row 6: Faith
Row 7: Labor
Row 8: Mutual Aid
```

**Column formulas** (enter in Row 2; drag down through Row 8 for each):

| Col | Header | Formula |
|-----|--------|---------|
| B | Total_Contacts | `=COUNTIF(Contacts!D:D,A2)` |
| C | Delivered | `=COUNTIFS(Contacts!D:D,A2,Contacts!G:G,"Delivered")` |
| D | Any_Reply | `=COUNTIFS(Contacts!D:D,A2,Contacts!I:I,">0")` |
| E | Score3Plus | `=COUNTIFS(Contacts!D:D,A2,Contacts!I:I,">=3")` |
| F | Score3Plus_Rate | `=IFERROR(E2/C2,0)` |
| K | Adoptions | `=COUNTIFS(Adoptions!D:D,A2,Adoptions!H:H,"Confirmed")` |
| L | People_Reached | `=SUMIF(Adoptions!D:D,A2,Adoptions!I:I)` |
| M | Network_Events | `=COUNTIFS(Adoptions!D:D,A2,Adoptions!J:J,"YES")` |

Format Column F as percentage with 1 decimal place.

**Manual columns** (fill during checkpoint reviews):
- Column G: Day7_Status (PASS / MONITOR / FAIL)
- Column H: Day14_Status (ON TRACK / MONITOR / BELOW BASELINE)
- Column I: Day30_Strong (YES / NO)
- Column J: Day30_Moderate (YES / NO)
- Column N: Status_Note (free text)

**Overall gate formulas** (Row 9, below constituency data):

| Label | Formula |
|-------|---------|
| Constituencies at Day30 Strong | `=COUNTIF(I2:I8,"YES")` |
| Phase 2 STRONG trigger | `=IF(COUNTIF(I2:I8,"YES")>=4,"STRONG — ACTIVATE PHASE 2","Below STRONG: "&COUNTIF(I2:I8,"YES")&"/4 required")` |
| Phase 2 MODERATE trigger | `=IF(COUNTIF(J2:J8,"YES")>=3,"MODERATE — ACTIVATE D39","Below MODERATE: "&COUNTIF(J2:J8,"YES")&"/3 required")` |

---

### Tab 6 — Checkpoints: Append-Only Log

One row per formal checkpoint. Do not edit past rows.

**Header row**:
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

All values entered manually at checkpoint time. Source each value from the Contacts, Constituencies, and Adoptions tabs at the moment of assessment.

---

### Tab 7 — Synthesis_Log: Weekly Summary Entries

One row per weekly synthesis. Updated manually after each Monday synthesis.

**Header row**:
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

**Auto-check formula** for whether the week's data has been entered (place labeled in a separate area):
```
Weeks with data:    =COUNTA(A2:A100)-COUNTBLANK(A2:A100)
Expected weeks:     =INT((TODAY()-DATE(2026,5,28))/7)+1
Weeks missing:      =MAX(0,INT((TODAY()-DATE(2026,5,28))/7)+1-(COUNTA(A2:A100)-COUNTBLANK(A2:A100)))
```

---

## Part 2: Week 2 Guidance (June 8-15)

### What changes at Week 2

Week 1 is the initial open rate window. Most recipients who are going to open and click do so in the first 3-5 days. Week 2 shows whether there is a secondary wave (internal forwarding within organizations) or whether activity has plateaued.

**Key Week 2 questions**:
- Is click velocity declining, flat, or still growing? (Gist_Views tab, delta formula)
- Have any contacts replied who were silent in Week 1? (Contacts tab, Any_Reply)
- Is there any Spike_Flag in Gist_Views this week? If yes, which link? Does it correlate with any reply from that constituency?
- Did any OOO contacts (Week 1 Score 1) return and send a substantive reply?

### Week 2 threshold interpretation

| Metric | Week 2 Cumulative | Interpretation |
|--------|------------------|----------------|
| Gist clicks >= 25 | 25+ total | On track for Day 30 MODERATE or STRONG |
| Gist clicks 15-24 | 15-24 total | MONITOR — reply rate must compensate |
| Gist clicks < 15 | < 15 total | ESCALATE — delivery diagnostic needed |
| Score 3+ replies >= 3 cumulative | — | Strong leading indicator for Day 30 MODERATE |
| Score 4+ reply in Week 2 | — | Pre-activate Phase 2 staging if domain-specific constituency |
| Zero new replies Week 2 with confirmed delivery | — | Apply framing revision (Modification 2) before Week 3 |

### Week 2 specific actions

**If clicks are declining (Week 2 total < Week 1 total)**:
This is normal. Interpret as the initial wave completing. The question is the floor: any week with 0 clicks and 0 replies after Week 3 is a signal to diagnose delivery or reframe.

**If a Score 1 OOO contact returned and sent a substantive reply**:
Re-score. Upgrade Delivery_Status in Contacts tab to "Delivered" and log the reply in Replies tab with the actual reply date (not the OOO date).

**If you received a Score 4 reply from a Law School or Civil Rights contact**:
This is a Domain 58 early signal. Flag in CHECKIN.md. Pull Domain 58 contact list from `DOMAIN_58_CONTACT_VERIFICATION.md`. Stage Domain 58 outreach for the Day 14-21 window.

**If you received a Score 4 reply from a Labor or Mutual Aid contact**:
This is a Domain 59 early signal. Flag in CHECKIN.md. Pull Domain 59 contact list from `domain-59-send-templates.md`. Verify Domain 59 Gist accessible: https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba

### Week 2 Day 14 checkpoint (June 14-15)

Day 14 is a mid-course correction gate. It is the last low-cost intervention point before the Day 30 full determination.

**Day 14 data to pull**:
- Cumulative Bitly clicks (all links): Gist_Views tab, Cumulative column
- Score 3+ reply rate: Contacts tab, Score 3+ rate summary cell
- Constituency-level signal counts: Constituencies tab, Columns E (Score3Plus) and F (Score3Plus_Rate)

**Day 14 gate**:

| Cumulative clicks | Score 3+ replies | Day 14 determination |
|------------------|------------------|---------------------|
| >= 25 | >= 2 | ON TRACK — proceed to Day 30 |
| >= 25 | 0-1 | MONITOR — reply signal weak; consider follow-up email to Score 2 contacts |
| 10-24 | >= 2 | MONITOR — clicks lagging but reply quality good; Day 30 MODERATE still achievable |
| 10-24 | 0-1 | BELOW BASELINE — apply Modification 2 (framing revision) before any new sends |
| < 10 with confirmed delivery | any | ESCALATE — delivery diagnostic; do not send new emails until resolved |

**Modification 2 (framing revision)** — apply if BELOW BASELINE at Day 14:
Review sent emails. The healthcare framing may need adjustment. Specific modification: send a brief follow-up (2-3 sentences maximum) referencing a new development since June 1 (e.g., any HHS OBBBA guidance movement, any Medicaid court ruling). Subject line: "One update since my June 1 email — [one-line development]." This follow-up anchors the outreach to current events and creates a second open opportunity without requiring recipients to acknowledge they did not engage the first time.

---

## Part 3: Week 3 Guidance (June 15-22)

### What Week 3 tells you

By Week 3, the initial open window is fully closed. New activity at Week 3 is either:
- Secondary wave (internal forwarding within recipient organizations)
- Delayed engagement from very busy contacts
- Organic discovery (someone shared the Gist link outside the original send list)

A Week 3 Spike_Flag (any single link >= 5 clicks in one day) that does not correlate with any outreach you sent is a positive organic signal — note it in Synthesis_Log and check whether any new email comes in from a non-contacted organization.

### Week 3 Phase 2 readiness assessment

By Week 3, you have enough data to assess Phase 2 readiness with moderate confidence.

**Run this assessment on June 22 (Day 21)**:

Pull from Constituencies tab:
- How many constituencies have Score 3+ rate > 0%? (Column F > 0)
- How many constituencies have at least 1 Score 3+ reply? (Column E >= 1)
- How many constituencies have a Confirmed or Probable adoption logged? (Column K >= 1)

**Phase 2 readiness matrix**:

| Constituencies with Score 3+ | Adoptions logged | Week 3 assessment |
|-----------------------------|-----------------|-------------------|
| 4+ | 1+ | STRONG trajectory — Day 30 STRONG is achievable |
| 3-4 | 0-1 | MODERATE trajectory — Domain 39 launch confirmed; Domain 58/59 stage |
| 2-3 | 0 | MONITOR — Day 30 MODERATE achievable if replies convert |
| 0-2 | 0 | WEAK trajectory — apply Modification 3; review contact quality |

**Modification 3 (contact list expansion)** — apply if WEAK at Week 3:
Pull the Tier 2 contact list from `phase-2-preparation/` directory. Identify 5-10 contacts in constituencies showing zero signal. Prepare personalized outreach referencing any Score 3+ replies received as social proof. Do not send until Day 30 determination confirms MONITOR or better.

---

## Part 4: Week 4 Guidance (June 22-29) and Day 30 Checkpoint

### Day 30 Full Checkpoint (June 27-28)

The Day 30 checkpoint drives all Phase 2 sequencing decisions. Run this on June 27 or 28.

**Step 1: Run the script**:
```bash
python3 /home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-adoption/phase-1-adoption-tracking-script.py --day30-report
```

**Step 2: Pull the four gate values from Google Sheets**:

| Gate | Value | Source |
|------|-------|--------|
| A: Score 3+ reply rate | [X%] | Contacts tab, Score 3+ rate summary cell |
| B: Constituencies at strong threshold | [X of 7] | Constituencies tab, COUNTIF(I2:I8,"YES") formula |
| C: Cross-organizational references | [X] | Synthesis_Log tab, cumulative network events |
| D: Confirmed adoptions | [X] | Adoptions tab, Confirmed adoptions formula |

**Step 3: Apply the Day 30 determination**:

| Determination | Conditions |
|--------------|-----------|
| STRONG | A >= 50% AND B >= 4 AND C >= 3 AND D >= 2 |
| MODERATE | A >= 25% AND B >= 2 AND (C >= 1 OR D >= 1) — not STRONG |
| WEAK | A >= 10% but below MODERATE thresholds |
| ASSESS | Any engagement signals but below WEAK thresholds |
| FAILURE | Zero Score 3+ replies, zero confirmed adoptions, zero organic signals |

**Step 4: Apply Phase 2 sequencing per determination**:

**STRONG**:
- Domain 39 expansion: launch Tier 2 contacts immediately
- Domain 56: launch Tier 2 immediately
- Domain 58 (Tribal Sovereignty): activate Weeks 5-8
- Domain 59 (Economic Precarity): activate Weeks 5-8
- Social proof: use any Score 4-5 replies as social proof in Domain 58/59 outreach

**MODERATE**:
- Domain 39: launch to Tier 2 contacts (Domain 39 launch is non-negotiable at MODERATE or better)
- Domain 56: hold to Day 37 (one additional week)
- Domain 58: stage for Day 60 activation (conditional on constituency-level signal)
- Domain 59: stage for Day 60 activation (conditional on constituency-level signal)

**WEAK**:
- Domain 39: launch only if at least one constituency is at MODERATE or better
- Domain 56: hold
- Domain 58/59: hold pending recovery modifications
- Apply Modifications 1-3 before any new sends (see PHASE_1_MEASUREMENT_SYSTEM.md)

**ASSESS**:
- Review contact quality — 48-hour hold before any sends
- Check for delivery issues (bounce rate, spam filtering)
- Pull any Score 3+ replies and verify they were logged correctly
- Decision: user input required (see CHECKIN.md "Needs Your Input")

**FAILURE**:
- 48-hour user decision window
- No outreach until delivery confirmed and framing revised
- Update CHECKIN.md "Needs Your Input" immediately

---

## Part 5: Trending Analysis — Automated Formula Addendum

Add this block to a new tab called `Trend_Analysis` for a summary dashboard view. This tab is optional but useful if you want a single-page view of trajectory.

### Tab: Trend_Analysis

**Structure** (labels in Column A, values in Column B):

| Label | Formula |
|-------|---------|
| Days since first send | `=TODAY()-DATE(2026,5,28)` |
| Weeks elapsed | `=INT((TODAY()-DATE(2026,5,28))/7)` |
| Current cumulative clicks | `=MAX(Gist_Views!J:J)` |
| Click target this week | `=IFERROR(VLOOKUP(INT((TODAY()-DATE(2026,5,28))/7)+1,Gist_Views!N:O,2,FALSE),"See target table")` |
| Clicks vs. target | `=MAX(Gist_Views!J:J)-IFERROR(VLOOKUP(INT((TODAY()-DATE(2026,5,28))/7)+1,Gist_Views!N:O,2,FALSE),0)` |
| On target? | `=IF(MAX(Gist_Views!J:J)>=IFERROR(VLOOKUP(INT((TODAY()-DATE(2026,5,28))/7)+1,Gist_Views!N:O,2,FALSE),0),"YES","NO — "&ABS(MAX(Gist_Views!J:J)-IFERROR(VLOOKUP(INT((TODAY()-DATE(2026,5,28))/7)+1,Gist_Views!N:O,2,FALSE),0))&" clicks behind")` |
| Total replies received | `=COUNTA(Contacts!H3:H200)-COUNTBLANK(Contacts!H3:H200)` |
| Score 3+ replies | `=COUNTIF(Contacts!I3:I200,">=3")` |
| Score 3+ rate | `=IFERROR(COUNTIF(Contacts!I3:I200,">=3")/COUNTIF(Contacts!G3:G200,"Delivered"),0)` |
| Confirmed adoptions | `=COUNTIF(Adoptions!H2:H200,"Confirmed")` |
| Days to Day 30 | `=MAX(0,DATE(2026,6,28)-TODAY())` |
| Days to Day 60 | `=MAX(0,DATE(2026,7,28)-TODAY())` |
| Phase 2 STRONG gate | `=IF(COUNTIF(Constituencies!I2:I8,"YES")>=4,"STRONG ACHIEVED","Need "&(4-COUNTIF(Constituencies!I2:I8,"YES"))&" more constituency STRONG")` |
| Phase 2 MODERATE gate | `=IF(COUNTIF(Constituencies!J2:J8,"YES")>=3,"MODERATE ACHIEVED","Need "&(3-COUNTIF(Constituencies!J2:J8,"YES"))&" more constituency MODERATE")` |

---

## Part 6: Weekly Synthesis Instructions — Weeks 2-4 Differences

The base synthesis template is `PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md`. Sections 1-6 are identical each week. What changes in Weeks 2-4:

### Week 2 (Section 13 — Overall Assessment)
- Replace "On Track / Below Track / Accelerating / Concerning" with a specific Phase 2 readiness statement
- Add: "Day 14 checkpoint runs [date]. Pre-staging Domain 58: [YES/NO]. Pre-staging Domain 59: [YES/NO]."

### Week 3 (Section 10 — Checkpoint Decision, if Day 14 ran this week)
- Fill Day 14 checkpoint section with full gate data
- Document any framing revisions applied (Modification 2)
- Document Phase 2 staging decisions

### Week 4 (Section 10 — Day 30 Checkpoint)
- Fill Day 30 checkpoint section with all four gate values
- Document full Phase 2 sequencing decision
- Flag any urgent CHECKIN.md items

**File naming convention** (save each Monday synthesis as):
```
monitoring/phase-1-week-[N]-synthesis-[YYYY-MM-DD].md
```

Example:
```
monitoring/phase-1-week-2-synthesis-2026-06-15.md
monitoring/phase-1-week-3-synthesis-2026-06-22.md
monitoring/phase-1-week-4-synthesis-2026-06-29.md
```

---

## Part 7: Expected Signal Patterns by Week

Reference baseline for calibrating whether your results are above, at, or below median for cold institutional outreach:

| Metric | Week 1 | Week 2 | Week 3 | Week 4 (Day 30) |
|--------|--------|--------|--------|-----------------|
| Cumulative Bitly clicks | 5-25 | 15-35 | 20-45 | 25-60 |
| Score 3+ replies cumulative | 1-5 | 3-7 | 4-9 | 5-12 |
| Score 3+ rate | 2-11% | 7-16% | 9-20% | 11-27% |
| Constituencies with any signal | 1-4 | 2-5 | 3-6 | 3-7 |
| Confirmed adoptions | 0 | 0-1 | 0-2 | 1-3 |

These ranges are based on cold institutional outreach benchmarks adjusted for the contact quality in the Phase 1 Tier 1 list (academics, legal aid directors, civil rights policy staff — higher engagement rate than a general advocacy list). If your results are consistently in the upper half of each range, the contact list quality is high and Phase 2 STRONG is achievable. If results are consistently below these ranges with confirmed delivery, the framing or contact quality needs review.

---

## Reference Files

| File | Purpose |
|------|---------|
| `PHASE_1_MEASUREMENT_SPREADSHEET_SPEC.md` | Full schema spec and column definitions |
| `PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md` | Monday synthesis template (Week 1 and all subsequent) |
| `phase-1-adoption/GOOGLE_SHEETS_TEMPLATE_COMPLETE.md` | 7-tab instantiation guide with initial data entry |
| `phase-1-adoption/WEEK_1_DATA_COLLECTION_FRAMEWORK.md` | Day 1-7 checklist, reply triage, scoring calibration |
| `PHASE_1_DAY_7_CHECKPOINT_DECISION_TREE.md` | Day 7 + Phase 2 Domain 58/59 activation logic |
| `PHASE_1_MEASUREMENT_SYSTEM.md` | Adoption scale definitions and Day 30/60 full criteria |
| `CHECKIN.md` | Escalation target for all urgent alerts and Phase 2 decisions |
