---
title: "June 9 Sample Data — Domain 51 Wave 1 Dashboard"
subtitle: "10 Mock Entries Demonstrating Daily Signal Log Entry Format"
created: "2026-06-05"
item: "Exploration Queue Item 84 — Optional Deliverable"
status: "production-ready"
purpose: >
  Demonstrates correct entry format for each event type across the 5 target organizations.
  Copy the column headers into Sheet 1 (Daily Signal Log) before June 9.
  Use these rows to verify formulas before first live data entry.
cross_references:
  - PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE_DOMAIN51.md
  - DAILY_SIGNAL_LOG_ENTRY_GUIDE.md
---

# June 9 Sample Data
## 10 Mock Entries — Daily Signal Log Format Demonstration

*These are synthetic entries showing one plausible scenario for the first 7 days of Wave 1. They are designed to let you verify that all Sheet 1 formulas and cross-sheet references work correctly before live data entry begins. Delete all sample rows once you have confirmed formula output — do not mix sample data with live data.*

---

## Pre-Entry Verification Step

Before copying sample rows into the sheet, confirm the column order in Row 1 of Sheet 1 is exactly:

```
A: Date | B: Organization | C: Tier | D: Event_Type | E: Signal_Code | F: Contact_Name | G: Channel | H: Notes
```

Then paste the 10 sample rows below into rows 2–11. With sample data in place, go to Sheet 5 (Cumulative Summary) and verify:
- Cell B4 (Total STRONG Signals) = 2
- Cell B5 (Total MODERATE Signals) = 3
- Cell B6 (Total WEAK Signals) = 1
- Cell B14 (T7 Gate Status) = "MODERATE — CONDITIONAL APPROVAL"

If those values match, the formulas are working correctly. Clear rows 2–11 and begin live data entry on June 9.

---

## Sample Rows (copy into Sheet 1, rows 2–11)

| Date | Organization | Tier | Event_Type | Signal_Code | Contact_Name | Channel | Notes |
|---|---|---|---|---|---|---|---|
| 06/09/2026 | CLC | A | SEND | PENDING | Erin Chlopak | EMAIL | Template Email 4 sent to echlopak@campaignlegalcenter.org — 09:00 UTC. Bitly-shortened Gist link embedded. |
| 06/09/2026 | Issue One | A | SEND | PENDING | Nick Penniman | EMAIL | Template Email 5 sent to info@issueone.org — 09:30 UTC. Bitly-shortened Gist link embedded. |
| 06/11/2026 | Common Cause CA | B | SEND | PENDING | Darius Kemp | EMAIL | Template Email 1 sent to dkemp@commoncause.org — 09:00 UTC. Second wave per DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md Wave 2. |
| 06/11/2026 | LWV CA | B | SEND | PENDING | Jenny Farrell | EMAIL | Template Email 2 sent to lwvc@lwvc.org — 09:30 UTC. |
| 06/11/2026 | Clean Money | C | SEND | PENDING | Trent Lange | EMAIL | Template Email 3 sent to info@CAclean.org — 10:00 UTC. |
| 06/10/2026 | CLC | A | GIST_CLICK | MODERATE | Unknown | GIST | Bitly registered 2 clicks on the Domain 51 short link 25 hours after CLC send. Location: Washington DC. Probable Chlopak or team member. |
| 06/11/2026 | Issue One | A | REPLY | STRONG | Nick Penniman | EMAIL | "Your 200-day FEC enforcement shutdown count is new to us — the full enforcement gap is documented nowhere else. Sharing with our policy director and our ReFormers Caucus team. Would you be available for a 20-minute call next week?" Forward to policy director confirmed. Call request confirmed. STRONG. |
| 06/12/2026 | CLC | A | REPLY | STRONG | Erin Chlopak | EMAIL | "The AI PAC formation timeline is exactly the gap in our enforcement analysis. We had OpenAI but not Anthropic. Our brief team is reviewing. Is this citable as a primary source?" Novel data engagement confirmed. Brief team routing confirmed. STRONG. |
| 06/14/2026 | Common Cause CA | B | OOO | MODERATE | Darius Kemp | EMAIL | Auto-reply: Kemp OOO June 12–16. Named alternate: "For ballot campaign inquiries please contact Sarah Morris, smorris@commoncause.org." Named alternate identified — upgrade from generic OOO to MODERATE. |
| 06/15/2026 | LWV CA | B | REPLY | MODERATE | Jenny Farrell | EMAIL | "Received — forwarding to our Voter Services Committee for the June 18 meeting agenda. We evaluate external research quarterly." Routing to named committee confirmed but no explicit use commitment. MODERATE. |

---

## Signal Code Verification Table

After pasting sample rows, verify these counts appear in Sheet 5 (Cumulative Summary):

| Metric | Expected Value | Sheet 5 Cell |
|---|---|---|
| Total Contacts Reached (SEND rows) | 5 | B2 |
| Total STRONG Signals | 2 | B4 |
| Total MODERATE Signals | 3 | B5 |
| Total WEAK Signals | 0 | B6 |
| Confirmed Orgs (Status=Confirmed) | 2 | B7 |
| Considering Orgs (Status=Considering) | 2 | B8 |
| Pass / No Response Orgs | 0 | B9 |
| T7 Gate Status | MODERATE — CONDITIONAL APPROVAL | B14 |

Note: Row B14 shows MODERATE because B4 = 2 (below the ≥4 threshold for STRONG). This is the expected scenario if only Tier A organizations have responded by Day 7 and Tier B/C remain at MODERATE or PENDING.

---

## What This Sample Scenario Represents

This sample depicts a typical MODERATE outcome at T+7:

**Day 1–2 (June 9–10)**: Both Tier A sends go out on time. CLC shows early Gist click signal within 24 hours, confirming the email reached at least one reader.

**Day 3 (June 11)**: Tier B and Tier C sends go out (Wave 2 per the contact stratification plan). Issue One returns a STRONG reply — the FEC enforcement timeline is novel data to them, they forward to policy director and request a call.

**Day 4 (June 12)**: CLC's Erin Chlopak replies with a STRONG signal — the AI PAC formation timeline is new to their litigation team.

**Day 5–6 (June 13–14)**: Darius Kemp is OOO but leaves a named alternate (MODERATE — not a dead end). LWV CA's Jenny Farrell routes to the Voter Services Committee (MODERATE — positive routing but no commitment).

**Day 7 (June 15–16)**: No signal yet from Clean Money. LWV CA reply arrived June 15. T+7 checkpoint runs June 16.

**At T+7 checkpoint**: B4 = 2 (CLC and Issue One are STRONG). B14 = "MODERATE — CONDITIONAL APPROVAL." Per T7_CHECKPOINT_DECISION_AUTOMATION.md, this is the MODERATE (low end) sub-variant. Phase 2 preparation begins on standard timeline: Domain 48 Gist creation July 1, Domain 49/50 preparation July 15. Domain 51 Tier 2 contacts activate June 19–30 window. T+14 check (June 23) monitors for Common Cause CA conversion after Kemp returns June 16.

---

## Entry Format Notes for Live Data

**Date format**: Use MM/DD/YYYY throughout. Google Sheets will auto-format to the regional default — if it changes to YYYY-MM-DD or another format, that is acceptable as long as date math in Sheet 5 (Row 13: Days Since Wave 1) still calculates correctly. Verify with this formula: `=TODAY()-DATE(2026,6,9)` should return the number of days since June 9.

**Organization spelling**: Must match exactly across all sheets. Use these exact strings:
- `CLC` (not "Campaign Legal Center")
- `Issue One` (not "IssueOne")
- `Common Cause CA` (not "Common Cause California")
- `LWV CA` (not "League of Women Voters CA")
- `Clean Money` (not "Clean Money Action Fund")

The cross-sheet COUNTIFS formulas in Sheets 3, 5 depend on exact string matching. A typo in column B will cause the formula to miss that row in its count.

**Signal Code sequence for a SEND that later gets a reply**: Enter the SEND row first with PENDING. When the reply arrives, add a new row with the reply date, REPLY Event_Type, and the correct Signal_Code. Do not edit the original SEND row's Signal_Code — PENDING should remain on all SEND rows. The Sheet 3 formula picks up the most recent non-PENDING code.

**When to add a NOTE row**: Add a NOTE row for any observation that is relevant to the outcome but not itself a signal — for example, "Verified Gist URL accessible June 8" or "Confirmed Bitly tracking is active by self-clicking short link." Use Signal_Code: N/A on NOTE rows.

---

*Prepared June 5, 2026. For use with PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE_DOMAIN51.md and DAILY_SIGNAL_LOG_ENTRY_GUIDE.md.*
