---
title: "Phase 1 Tracking Spreadsheet — Full Specification"
project: cybersecurity-hardening
created: 2026-05-09
status: production-ready
executor: Anya
cross-references:
  - docs/phase-1-launch-runbook.md
  - TIER1_OUTREACH_PREPARED.md
  - engagement-scoring-template.csv
---

# Phase 1 Tracking Spreadsheet — Full Specification

**Purpose**: Authoritative tracking of all Tier 1 contacts across the email send and response lifecycle. This specification defines every column, formula, and sheet in the Google Sheet you create before Day 1.

**File name**: "Phase 1 Outreach Tracker — [launch date]"
**Tool**: Google Sheets (free; shareable if needed)

---

## Sheet 1: Tier_1_Contacts

This is the primary data entry sheet. One row per contact.

### Column Definitions

| Column | Type | Notes |
|--------|------|-------|
| A: Organization | Text | Full organization name (e.g., "National Immigration Law Center") |
| B: Category | Dropdown | 1A (legal aid) / 1B (community) / 1C (mutual aid) |
| C: Contact Name | Text | Named individual if available; "General Inbox" if sending to info@ |
| D: Contact Email | Text | Full email address; note if using web form instead |
| E: Delivery Method | Dropdown | Email / Web Form / Dual (Email+Form) / Signal |
| F: Template Used | Dropdown | 1A / 1B / 1C |
| G: Wave | Number | 1 = Day 1 named contacts; 2 = Day 3 regional 1A; 3 = Day 4 named 1B; 4 = Day 5 regional 1B; 5 = Day 6-7 1C |
| H: Date Sent | Date | Date of initial outreach send (YYYY-MM-DD) |
| I: Time Sent | Time | Local time of send (HH:MM) |
| J: Bitly Click | Dropdown | Yes / No / Unknown (update from Bitly dashboard daily) |
| K: Bitly Click Date | Date | Date Bitly first recorded a click correlated to this contact's open window (estimated) |
| L: Response Received | Dropdown | Yes / No |
| M: Response Date | Date | Date of first response received |
| N: Response Type | Dropdown | Engagement / Acknowledgment / Declination / OOO / Bounce |
| O: Follow-Up Sent | Dropdown | Yes / No / N/A |
| P: Follow-Up Date | Date | Date of follow-up send (Template R2) |
| Q: Follow-Up Response | Dropdown | Yes / No |
| R: Status | Dropdown | Pending / Sent / Bounced / Opened / Clicked / Replied / Closed-Positive / Closed-Negative |
| S: Amplification Signal | Dropdown | None / Forwarded-Network / Referred-Contact / Media-Mention |
| T: Estimated Amplification Reach | Number | Estimated people reached via amplification (enter 0 if no signal) |
| U: Notes | Text | Free text — interest level, requested follow-up, org constraints, personalization notes |

### Pre-Populated Day 1 Rows

Enter these five rows before Day 1 with all static fields (columns A–G) pre-filled. Columns H–U fill during execution.

| Row | Organization | Category | Contact Name | Email | Method | Template | Wave |
|-----|-------------|----------|-------------|-------|--------|----------|------|
| 2 | National Immigration Law Center (NILC) | 1A | General Inbox | info@nilc.org | Dual | 1A | 1 |
| 3 | CLINIC — Catholic Legal Immigration Network | 1A | General Inbox | national@cliniclegal.org | Email | 1A | 1 |
| 4 | RAICES Texas | 1A | Thaís Silva-Marques | communications@raicestexas.org | Email | 1A | 1 |
| 5 | Immigrant Legal Resource Center (ILRC) | 1A | Kemi Bello | kbello@ilrc.org | Email | 1A | 1 |
| 6 | National Lawyers Guild (NLG) | 1A | General Inbox | massdef@nlg.org | Email | 1A | 1 |

Rows 7+ fill as you research and add regional contacts on Days 2–7.

### Status Dropdown Logic

Use the Status column as your primary at-a-glance tracker:

- **Pending**: Researched but not yet sent
- **Sent**: Email sent, no response yet, no known bounce
- **Bounced**: Delivery failure notification received
- **Opened**: Bitly click confirmed (proxy for email open)
- **Clicked**: Same as Opened (Bitly click is the primary indicator)
- **Replied**: Any response received (use Response Type for classification)
- **Closed-Positive**: Engagement or Acknowledgment response; follow-up complete
- **Closed-Negative**: Declination received; no further contact

---

## Sheet 2: Weekly_Rollup

Auto-calculated summary sheet. Build this using COUNTIF and AVERAGEIF formulas referencing Sheet 1.

### Columns

| Column | Formula | Notes |
|--------|---------|-------|
| A: Week | Manual | "Week 1 (Days 1-7)", "Week 2 (Days 8-14)", "Week 3 (Days 15-21)" |
| B: Total Sent | `=COUNTIF(Tier_1_Contacts!H:H,"<>"&"")` for the week range | Count of rows with a send date in that week |
| C: Total Bounced | COUNTIF on Response Type = "Bounce" | |
| D: Total Bitly Clicks | COUNTIF on Bitly Click = "Yes" | |
| E: Total Replied | COUNTIF on Response Received = "Yes" | |
| F: Engagement Count | COUNTIF on Response Type = "Engagement" | |
| G: Acknowledgment Count | COUNTIF on Response Type = "Acknowledgment" | |
| H: Declination Count | COUNTIF on Response Type = "Declination" | |
| I: Bounce Rate | `=D/B` formatted as % | Target: <15% |
| J: Click Rate | `=E/B` formatted as % | Target: >30% |
| K: Reply Rate | `=F/B` formatted as % | Target: >10% |
| L: Engagement Rate | `=G/B` formatted as % | Target: >3% |
| M: Avg Response Time (hours) | AVERAGEIF on rows with Response Date | Estimated from Date Sent + Time Sent vs. Response Date |

### Decision Trigger Row

At the bottom of the Weekly_Rollup sheet, add a decision row with conditional formatting:

| Trigger | Condition | Formatting |
|---------|-----------|------------|
| Reply rate below warning | Reply Rate < 5% | Red background |
| Reply rate acceptable | Reply Rate 5–10% | Yellow background |
| Reply rate strong | Reply Rate > 10% | Green background |
| Click rate low | Click Rate < 15% | Orange background — subject line review needed |
| Bounce rate high | Bounce Rate > 15% | Red background — stop sends, investigate contact list |

---

## Sheet 3: Response_Log

Detailed log of every response received. One row per response event.

### Columns

| Column | Notes |
|--------|-------|
| A: Date Received | Date of response |
| B: Organization | From which org |
| C: Contact Name | Who responded |
| D: Response Type | Engagement / Acknowledgment / Declination / OOO / Bounce |
| E: Response Summary | 1–3 sentence summary of what they said |
| F: Action Required | What you need to do (Reply / Log OOO / Research Alternate / None) |
| G: Action Due Date | When the action needs to be completed |
| H: Action Completed | Checkbox or Yes/No |
| I: Amplification Potential | High (asked about sharing) / Medium (general interest) / Low (passive ack) / None |
| J: Phase 2 Candidate | Yes / No / Maybe (for Tier 2 outreach nomination) |
| K: Full Response Text | Paste the response text for reference |

---

## Sheet 4: Amplification_Tracker

Dedicated tracking for network amplification events (the highest-value Phase 1 outcome).

### Columns

| Column | Notes |
|--------|-------|
| A: Date Detected | When you observed the amplification signal |
| B: Source Organization | Which Tier 1 contact is the origin |
| C: Signal Type | Forwarded-Network / Referred-Contact / Media-Mention / Bitly-Spike |
| D: Channel | Where the amplification happened (mailing list / Signal group / social media / press coverage) |
| E: Estimated Reach | Estimated number of people reached |
| F: Evidence | URL, screenshot description, or contact who reported it |
| G: Follow-Up Action | What to do (reach out to new contacts, track press coverage, etc.) |
| H: Bitly Click Impact | Did Bitly clicks spike on this date? |

---

## Sheet 5: Dashboard

High-level KPI view for quick status checks. All values pull from Sheets 1–4 via formulas.

### KPI Cards (build as large cells with prominent formatting)

| KPI | Formula Source |
|-----|---------------|
| Total Sent (all waves) | COUNT of non-empty Date Sent column |
| Current Reply Rate | Replies / Sent formatted as % |
| Engagement Rate | Engagement responses / Sent |
| Total Bitly Clicks | COUNT of Bitly Click = "Yes" |
| Amplification Events | COUNT of rows in Amplification_Tracker |
| Days Since Launch | TODAY() - [launch date cell] |
| Days Remaining (Week 3) | 21 - [days since launch] |
| Phase 2 Candidates | COUNT of Phase 2 Candidate = "Yes" in Response_Log |

### Progress Indicators

Add two visual progress bars using a SPARKLINE formula or conditional formatting:

1. **Send Progress**: Total Sent / Target (50–60 contacts) — fills green as sends accumulate
2. **Reply Rate Status**: Current Reply Rate vs. 10% target — red if <5%, yellow if 5–10%, green if >10%

### Decision Status

One cell that displays the current Phase 2 status based on the reply rate trigger:

```
=IF(K_reply_rate>0.1, "GO — Trigger Phase 2 outreach", IF(K_reply_rate>0.05, "WAIT — Re-engagement campaign before Phase 2", "INVESTIGATE — Review messaging and delivery"))
```

---

## Formulas Reference

### Reply Rate (overall)
```
=COUNTIF(Tier_1_Contacts!L:L,"Yes") / COUNTA(Tier_1_Contacts!H:H)
```

### Click Rate (overall)
```
=COUNTIF(Tier_1_Contacts!J:J,"Yes") / COUNTA(Tier_1_Contacts!H:H)
```

### Bounce Rate
```
=COUNTIF(Tier_1_Contacts!N:N,"Bounce") / COUNTA(Tier_1_Contacts!H:H)
```

### Average Response Time (hours)
Requires numeric representation of dates + times. Simplest approach: enter dates as YYYY-MM-DD in Date Sent and Response Date columns, then:
```
=AVERAGE(Tier_1_Contacts!M:M - Tier_1_Contacts!H:H) * 24
```
This gives hours between send date and response date (ignoring time within day — sufficient for a 21-day campaign).

### Phase 2 Candidate Count
```
=COUNTIF(Response_Log!J:J,"Yes")
```

---

## Maintenance Schedule

| Frequency | Action | Time Required |
|-----------|--------|--------------|
| After each send | Update H, I columns for sent rows | 2 min/send |
| Daily at 12:00 PM | Check for bounces and responses; update J, L, M, N columns | 10–15 min |
| Daily (evening) | Check Bitly dashboard; update J column | 5 min |
| Weekly (Day 7, 14, 21) | Complete Weekly_Rollup sheet; assess KPIs | 15 min |
| When amplification detected | Add row to Amplification_Tracker | 5 min |
| Day 21 | Full campaign close-out; export spreadsheet as PDF | 20 min |

**Total ongoing overhead**: ~15–20 min/day during the active 21-day window. Most of this is inbox monitoring (which you would do anyway) rather than spreadsheet entry.
