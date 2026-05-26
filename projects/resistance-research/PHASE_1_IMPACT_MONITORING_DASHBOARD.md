---
title: "Phase 1 Impact Monitoring Dashboard — Tab Schema Reference"
created: 2026-05-27
version: 1.0
status: production-ready
scope: >
  Schema documentation for the three dashboard tabs built in the May 27 pre-testing
  session: Replies, Constituencies, and Checkpoints. Covers column definitions,
  formulas, allowed values, and usage examples. Companion to
  PHASE_1_MONITORING_DASHBOARD_SHEETS_SPEC.md (full 7-tab spec) and
  PHASE_1_MONITORING_DASHBOARD.md (operational SOP).
integration:
  - PHASE_1_DECISION_TREES.md — Day 7/14/30 logic feeds Checkpoints tab
  - reply-triage-framework.md — triage results populate Replies tab
  - post-synthesis-contingency-execution-playbooks.md — all contingency paths draw on checkpoint data
---

# Phase 1 Impact Monitoring Dashboard — Tab Schema Reference

**Version 1.0 — May 27, 2026**

This document specifies the three dashboard tabs that were confirmed as setup gaps in the May 26 infrastructure verification: Replies, Constituencies, and Checkpoints. Each section provides the full column schema, formula strings, allowed values, and a worked usage example. These tabs coordinate with each other and with the existing Contacts and Adoptions tabs — cross-sheet references are noted inline.

For the complete 7-tab schema (including Contacts, Gist Views, Adoptions, and Network Map), see `PHASE_1_MONITORING_DASHBOARD_SHEETS_SPEC.md`. For the operational runbook (weekly synthesis process, Bitly tracking, Part 3 triage protocols), see `PHASE_1_MONITORING_DASHBOARD.md`.

---

## Replies Sheet

**Purpose**: Per-reply log. One row per reply received, in chronological order. A single contact who replies three times generates three rows. This is separate from the Contacts tab, which holds one row per contact at that contact's highest score. The Replies tab is the raw record; the Contacts tab holds the aggregate.

**Append-only.** Never edit or delete past rows. Enter rows as replies arrive.

**Row 1**: Headers (freeze this row in Google Sheets)
**Row 2+**: One row per reply, in the order replies are received

### Column Schema

| Col | Header | Data Type | Allowed Values | Notes |
|-----|--------|-----------|----------------|-------|
| A | Reply_ID | Text | R001, R002, R003, ... | Assign sequentially as replies arrive. Never reuse an ID. |
| B | Contact_ID | Text | C001–C999 | Cross-reference to Contacts tab Column A. If a contact replies twice, both rows carry the same Contact_ID. |
| C | Date | Date | YYYY-MM-DD | Date the reply landed in your inbox, not the date you processed it. |
| D | Score | Integer | 1 / 2 / 3 / 4 / 5 | Engagement score assigned per reply-triage-framework.md. 1 = OOO or perfunctory; 5 = confirmed adoption. See scoring tree in that document. |
| E | Category | Text | positive / neutral / unsure / negative | Top-level sentiment classification applied after the reply-triage five-category score. See Category Definitions below. |
| F | Key_Content | Text | Free text — 1–3 sentences | Direct quote or close paraphrase of the most important content in the reply. If quoting, use quotation marks. |
| G | Notes | Text | Free text | Follow-up commitments made, FAQ topics surfaced, referral mentions ("forwarded to X"), data requests, action items, or any context not captured in Key_Content. |

### Category Definitions

The Category column applies a four-way classification on top of the five-category triage system in `reply-triage-framework.md`. The mapping is:

| Category value | Meaning | Triage category equivalents |
|----------------|---------|----------------------------|
| positive | Contact expresses interest, intent to adopt, or enthusiasm | Implementation Signal (Cat 1), Partnership (Cat 5 equivalent) |
| neutral | Contact asks questions, requests data, or acknowledges without indicating direction | Data Request (Cat 3), General Question (Cat 4) |
| unsure | Reply is ambiguous — could be interest or polite deflection; insufficient signal to classify | Any reply where intent is unclear after reading twice |
| negative | Contact declines, raises substantive objection, requests removal, or expresses skepticism | Critique-Objection (Cat 2), Opt-Out |

When in doubt, use `unsure`. Do not force a classification. The `unsure` category is a legitimate data point — a cluster of unsure replies in a single constituency is itself a signal worth noting in the weekly synthesis.

### Aggregate Formulas

Add these in a frozen summary block below the header row or in a sidebar named range. Replace `A2:A200` ranges with the actual data range as the sheet grows.

```
Total replies logged:     =COUNTA(A2:A200)-COUNTBLANK(A2:A200)
Score 3+ total:           =COUNTIF(D2:D200,">=3")
Score 3+ rate:            =COUNTIF(D2:D200,">=3") / (COUNTA(A2:A200)-COUNTBLANK(A2:A200))
Positive category count:  =COUNTIF(E2:E200,"positive")
Negative category count:  =COUNTIF(E2:E200,"negative")
Critique rate:            =COUNTIF(E2:E200,"negative") / (COUNTA(A2:A200)-COUNTBLANK(A2:A200))
Unsure count:             =COUNTIF(E2:E200,"unsure")
```

**Critique rate alert**: If the critique rate formula exceeds 0.30 at any point in a rolling 14-day window, add a note to CHECKIN.md: "Critique/negative rate above 30% — messaging review needed." See `PHASE_1_MONITORING_DASHBOARD.md` Part 3.3 for the response protocol.

### Usage Example

The following shows three rows from a hypothetical Week 1 data entry:

| Reply_ID | Contact_ID | Date | Score | Category | Key_Content | Notes |
|----------|------------|------|-------|----------|-------------|-------|
| R001 | C003 | 2026-06-01 | 5 | positive | "We are incorporating the Domain 56 governance framework into our constitutional law clinic curriculum starting in the fall term." | Escalated to user same-day. Entry added to Adoptions tab as A001. Tier2_Candidate set to YES in Contacts tab. |
| R002 | C007 | 2026-06-02 | 3 | negative | "I think the causal claim in Section 3 overstates the evidence — the comparative cases don't cleanly support the conclusion." | Responded within 48 hours with source citations. Specific claim: merit system protections section. Check if same critique appears from 2 more contacts. |
| R003 | C011 | 2026-06-03 | 2 | neutral | "Thanks for sending this. Could you tell me more about the publication status and whether it's been through peer review?" | General question. Responded within 72 hours. Replied with honest answer re: independent research. Asked one follow-up question about their current work area. |

---

## Constituencies Sheet

**Purpose**: Aggregated metrics per constituency. Seven data rows fixed — one per constituency. Used to determine whether the Day 30 STRONG threshold is met (4 of 7 constituencies at strong). All formula columns pull live from the Contacts tab; no manual entry is needed except for the manually-assessed Day30_Strong column.

**Row 1**: Headers (freeze)
**Rows 2–8**: One row per constituency. Pre-populate Column A before any contacts are entered.
**Rows 10–12**: Phase 2 trigger formulas (below data).

Do not add rows to this sheet. There are exactly seven constituencies.

### Pre-Populated Constituency Names (Column A, Rows 2–8)

Enter these values exactly — spelling and capitalization must match the Constituency column in the Contacts tab or all COUNTIFS formulas will fail silently:

1. Law School
2. Imm Legal Aid
3. Civil Rights
4. Academic
5. Faith
6. Labor
7. Mutual Aid

### Column Schema

| Col | Header | Data Type | Formula / Allowed Values | Notes |
|-----|--------|-----------|--------------------------|-------|
| A | Constituency_Name | Text | See pre-populated list above | Must match Contacts!E exactly. Do not vary spelling. |
| B | Contact_IDs | Text | Comma-separated list, e.g. "C001, C004, C006" | Manual reference only — enter once when setting up the sheet. Used for human auditing, not by any formula. |
| C | Score_Max | Formula | `=MAXIFS(Contacts!N:N,Contacts!E:E,A2)` | Highest Engagement_Score achieved by any contact in this constituency. Updates automatically as scores are entered in Contacts tab. |
| D | Day30_Strong | Text | YES / NO | Fill manually at Day 30 checkpoint. YES if this constituency has 3 or more Score 3+ replies OR at least 1 Score 5 reply. See decision rule below. |
| E | Notes | Text | Free text | Checkpoint observations: which contacts responded, what they said, trajectory assessment since Day 7. Update at each checkpoint, prepending the checkpoint date to each new note. |

### Score_Max Formula Detail

`=MAXIFS(Contacts!N:N,Contacts!E:E,A2)`

This formula returns the maximum value in the Engagement_Score column (Contacts!N) among all rows where the Constituency column (Contacts!E) matches the constituency name in Column A of this row. When no contacts in the constituency have any score entered, it returns 0.

**For the Law School row (Row 2)**: `=MAXIFS(Contacts!N:N,Contacts!E:E,"Law School")`

The formula self-populates across all seven rows if you use the cell reference A2 (and drag down). Verify after setup: temporarily enter a score in the Contacts tab for a test row and confirm Score_Max updates.

### Day30_Strong Decision Rule

At the Day 30 checkpoint, review the Replies tab and Contacts tab data for each constituency. Then set Day30_Strong manually:

- **YES**: The constituency has 3 or more contacts with Score >= 3 in the Contacts tab, OR at least 1 contact with Score = 5 in any row of the Replies tab.
- **NO**: Neither condition is met.

This is a manual assessment, not a formula, because it requires judgment about reply quality. The Score_Max column (Column C) gives you the ceiling — if Score_Max < 3 for a constituency, Day30_Strong is automatically NO without needing to check individual replies.

### Phase 2 Trigger Formulas (Rows 10–12)

Add these in rows 10 through 12, below the seven data rows. Use two columns: one for a text label, one for the formula.

```
Row 10 — Constituencies at Day30_Strong YES:
  =COUNTIF(D2:D8,"YES")

Row 11 — STRONG trigger:
  =IF(COUNTIF(D2:D8,"YES")>=4,
    "STRONG — ACTIVATE PHASE 2 NOW",
    "Not yet: "&COUNTIF(D2:D8,"YES")&" of 4 needed")

Row 12 — MODERATE trigger:
  =IF(COUNTIF(D2:D8,"YES")>=2,
    "MODERATE — ACTIVATE DOMAIN 39 NOW",
    "Not yet: "&COUNTIF(D2:D8,"YES")&" of 2 needed")
```

The STRONG trigger (4 of 7 constituencies at Day30_Strong YES) is the primary Phase 2 go signal. If Row 11 returns "STRONG — ACTIVATE PHASE 2 NOW," execute the same-day protocol in `PHASE_1_DECISION_TREES.md` Section: Day 30 Immediate Actions.

### Usage Example

The following shows the Constituencies sheet at the Day 30 checkpoint after a moderate-engagement scenario:

| Constituency_Name | Contact_IDs | Score_Max | Day30_Strong | Notes |
|-------------------|-------------|-----------|--------------|-------|
| Law School | C001, C002, C003 | 5 | YES | C001 (Georgetown) confirmed adoption June 1. C002 replied with critique. C003 no reply. Strong driven by single Score 5. |
| Imm Legal Aid | C004, C005 | 3 | NO | C004 replied with data request (Score 3). C005 no reply. Only 1 of 2 at Score 3; need 3 to qualify for YES under 3+ rule. |
| Civil Rights | C006, C007 | 3 | NO | C007 critique reply (Score 3). No implementation signals. |
| Academic | C008, C009 | 0 | NO | Zero replies. Zero clicks detected in Bitly for outreach window. Flag for Day 37 follow-up. |
| Faith | C010 | 2 | NO | OOO reply June 1. No substantive reply yet. |
| Labor | C011 | 2 | NO | Polite acknowledgment. No scoring interest. |
| Mutual Aid | C012 | 4 | NO | Score 4 — forwarded to network. No confirmed adoption. 1 of 3 needed for YES under 3+ rule. |

Row 10: 1 (only Law School at YES)
Row 11: "Not yet: 1 of 4 needed" — MODERATE path applies
Row 12: "Not yet: 1 of 2 needed" — review at Day 37

---

## Checkpoints Sheet

**Purpose**: Append-only audit log of all Phase 1 checkpoint decisions. One row per checkpoint run. Never edit or delete past rows — this is the permanent record of go/no-go determinations that all contingency playbooks reference.

**Row 1**: Headers (freeze)
**Row 2**: Day 7 checkpoint (target: June 4–5)
**Row 3**: Day 14 checkpoint (June 11–12, only if Day 7 = MONITOR)
**Row 4**: Day 30 checkpoint (June 27–28)
**Row 5**: Day 60 checkpoint (July 27–28)
**Row 6+**: Pre-checkpoint override rows if an early trigger fires (Score 5 override or Score 4 cluster)

### Column Schema

| Col | Header | Data Type | Allowed Values | Notes |
|-----|--------|-----------|----------------|-------|
| A | Date | Date | YYYY-MM-DD | Actual date the checkpoint was run, not the target date. |
| B | Checkpoint_Type | Text | Day7 / Day14 / Day30 / Day60 / Pre-Day30-Score5 / Pre-Day30-Score4-Cluster | Use exact values. Pre-Day30 rows are appended when an early trigger fires before the scheduled checkpoint — they do not replace the scheduled checkpoint row. |
| C | Determination | Text | See allowed values below by checkpoint type | The output classification from the decision tree. Use exact values from `PHASE_1_DECISION_TREES.md`. |
| D | Metric_A | Decimal | 0.00–1.00 | Score 3+ reply rate at time of checkpoint: (count of Contacts with Engagement_Score >= 3) / (Confirmed_Delivered). Example: 0.31 = 31%. Pull from Contacts tab summary block. |
| E | Metric_B | Integer | 0–7 | Constituencies meeting strong threshold: count of Day30_Strong = YES in Constituencies tab at checkpoint time. At Day 7, use count of constituencies with at least 1 Score 3+ reply as the equivalent measure. |
| F | Metric_C | Integer | 0+ | Cross-organizational references: count of rows in Adoptions tab where Signal_Type = "Referral" AND Verification_Status = "Confirmed" or "Probable". |
| G | Metric_D | Integer | 0+ | Confirmed adoption signals: count of rows in Adoptions tab where Verification_Status = "Confirmed". |
| H | Notes | Text | Free text | Delivery anomalies, external context (news events that affected timing), unexpected contacts, or any observation not captured in the metric columns. |

### Determination Allowed Values by Checkpoint Type

**Day7**:
- `HOLD` — 15+ Bitly clicks AND 2+ replies. Normal trajectory. Continue to Day 30 without intervention.
- `MONITOR` — 5–14 clicks OR 0–1 replies with confirmed delivery. Check again at Day 14.
- `ESCALATE` — 0–4 clicks with confirmed delivery, OR 3+ email bounces. Run delivery diagnostic within 24 hours.
- `CONTACT_VERIFY` — 3 or more bounces. Pull BATCH_1_CONTACT_VERIFICATION.md, re-check addresses, resend to corrected addresses, restart Day 7 clock.

**Day14**:
- `HOLD` — On track. Score 3+ rate improving week-over-week. No action.
- `CONTINUE_MONITOR` — Engagement below target but not zero. Review framing options.
- `FAILURE_IMMINENT` — Cumulative Bitly clicks below 10 AND reply count 0–1 AND no constituency has any Score 3+ engagement. Apply messaging revision protocol.

**Day30**:
- `STRONG` — Score 3+ rate >= 50%, AND 4+ constituencies at Day30_Strong, AND 3+ cross-org references, AND 2+ confirmed adoptions. Activate Phase 2 same day.
- `MODERATE` — Score 3+ rate 30–49%, OR 3+ constituencies strong, OR 1+ cross-org reference, OR 1+ confirmed adoption. Activate Domain 39. Hold Domain 56 to Day 37.
- `WEAK` — Score 3+ rate below 20%, AND fewer than 2 constituencies strong, AND 0 cross-org references. Apply 3-modification failure recovery protocol.
- `ASSESS` — Results fall between MODERATE and WEAK thresholds. Do not activate Phase 2. Run Day 37 supplemental checkpoint.
- `FAILURE` — Score 3+ rate below 10%, AND 0 cross-org references, AND 0 confirmed adoptions, AND zero Gist clicks in Weeks 3–4. Full contingency review. Add to CHECKIN.md under "Needs Your Input."

**Day60**:
- `MOVEMENT` — 15+ confirmed adoption signals AND 100+ people reached estimate.
- `PARTIAL` — 5–14 confirmed adoptions OR 50–99 people reached.
- `BELOW_TARGET` — Fewer than 5 confirmed adoptions AND fewer than 50 people reached.

**Pre-Day30 overrides**:
- `Pre-Day30-Score5` — First Score 5 reply received before Day 30. Run immediate activation protocol.
- `Pre-Day30-Score4-Cluster` — 3 or more Score 4 replies within any 7-day window before Day 30. Review Phase 2 readiness within 48 hours.

### Pre-Checkpoint Data Pull

Before entering any checkpoint row, pull these four numbers and enter them in Columns D–G:

1. **Metric_A** (Score 3+ rate): From Contacts tab summary block — formula `=COUNTIF(N2:N200,">=3") / COUNTIF(I2:I200,"Delivered")`.
2. **Metric_B** (constituencies strong): From Constituencies tab Row 10 formula, or count manually at Day 7.
3. **Metric_C** (cross-org references): Count rows in Adoptions tab where Signal_Type = "Referral" AND Verification_Status is "Confirmed" or "Probable". There is no auto-formula for this — count manually.
4. **Metric_D** (confirmed adoptions): Count rows in Adoptions tab where Verification_Status = "Confirmed".

Then run the decision tree in `PHASE_1_DECISION_TREES.md` for the appropriate checkpoint type. Record the output determination in Column C. Record the action you took in the Notes column. Copy the determination to CHECKIN.md.

### Usage Example

The following shows the Checkpoints sheet after Day 7 and Day 30 have been run:

| Date | Checkpoint_Type | Determination | Metric_A | Metric_B | Metric_C | Metric_D | Notes |
|------|-----------------|---------------|----------|----------|----------|----------|-------|
| 2026-06-04 | Day7 | HOLD | 0.18 | 1 | 0 | 0 | 20 Bitly clicks Week 1 (above 15 threshold). 3 replies total — C001 Score 5, C007 Score 3, C011 Score 2. Delivery confirmed for all 11 Domain 56 contacts. Metric_A at 0.18 (2 of 11 at Score 3+). |
| 2026-06-01 | Pre-Day30-Score5 | Pre-Day30-Score5 | 0.09 | 0 | 0 | 0 | C001 (Georgetown Law) replied Day 4 with confirmed adoption signal. Escalated to user same day. Adoptions tab A001 created. Phase 2 pre-activation planning initiated. Day 30 checkpoint still on schedule — this row is supplemental. |
| 2026-06-28 | Day30 | MODERATE | 0.36 | 1 | 1 | 1 | 5 of 11 Domain 56 contacts at Score 3+. Only Law School constituency at Day30_Strong YES. One cross-org referral from C001 to Yale Law (Probable — no direct contact yet). One confirmed adoption (C001). Domain 39 activated June 28. Domain 56 Tier 2 outreach deferred to Day 37 per MODERATE protocol. |

---

## Integration Notes

**Replies tab feeds Contacts tab**: After scoring a reply in the Replies tab, update the corresponding contact's Engagement_Score in Contacts tab Column N. If this reply produces a higher score than the contact's previous score, update to the new score. The Contacts tab holds the ceiling score; the Replies tab holds the full history.

**Constituencies tab pulls from Contacts tab**: The Score_Max formula in Column C is live — it updates automatically whenever Contacts!N changes. Day30_Strong (Column D) is the only manual field and is set once at the Day 30 checkpoint.

**Checkpoints tab pulls from all other tabs**: Metric_A comes from the Contacts summary block. Metric_B comes from the Constituencies trigger formula. Metrics_C and D come from manual counts in the Adoptions tab. The Checkpoints tab does not have any live formula connections — it is a snapshot record, not a live dashboard.

**Decision tree connection**: Each Determination value in the Checkpoints tab corresponds to a named branch in `PHASE_1_DECISION_TREES.md`. The column uses the exact string values from that document so that future sessions can grep for determination values without ambiguity.

**Contingency playbook connection**: All post-synthesis contingency playbooks (`post-synthesis-contingency-execution-playbooks.md`, `TOO_EARLY_CONTINGENCY_STAGING_MAY26.md`) assume the Checkpoints tab is populated. If a contingency session opens and the tab is empty, the playbook cannot determine which activation branch applies. Populate the Checkpoints tab before or immediately after each checkpoint decision — not retrospectively.
