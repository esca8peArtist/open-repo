---
title: "Contractor Response Tracking Template"
subtitle: "Google Sheets + Markdown Log for All 11 Contractors — June 22–28"
date: 2026-06-22
version: 1.0
status: ready-to-use
format: Google Sheets structure (below) + Markdown fallback
user-action-required: YES — set up Google Sheet immediately after sending emails (June 23)
tags: [seedwarden, phase-3, response-tracking, scoring, decision-support]
---

# Contractor Response Tracking Template

**Prepared**: June 22, 2026  
**Purpose**: Centralized log for tracking all contractor responses, responses dates, availability, budget fit, and scoring during the June 22–28 decision window.  
**Format**: Google Sheets template (recommended for real-time scoring, formulas, conditional formatting) + Markdown fallback (if Google Sheets unavailable)  
**Update frequency**: Daily, June 24–28 (or as responses arrive)  

---

## Google Sheets Setup

### Sheet Structure

**Create a new Google Sheet** with this structure. Save as: `Seedwarden Phase 3 — Contractor Response Tracking [June 22-28]`

**Share**: Shared with yourself (read-only backup) + optional backup email account for disaster recovery

**Columns (A–L)**:

```
A: Email Track
B: Contractor Organization
C: Contact Name
D: Role
E: Email Address
F: Send Date (from CONTRACTOR_OUTREACH_SEND_LOG.md)
G: Response Date
H: Response Status
I: Fit Score (1–5 scale)
J: Budget Fit (1–5 scale)
K: Availability Confirmed (Y/N)
L: Overall Weighted Score
M: Final Rank
N: Selection Status
O: Notes
```

---

### Column Definitions & Formulas

#### A: Email Track
**Type**: Text (reference)  
**Values**: A1, A2, A3, A4, A5, B1, B2, B3, C1, C2, C3  
**Formula**: (none — manual entry)  
**Example**: `A1`

---

#### B: Contractor Organization
**Type**: Text  
**Description**: Company or institutional name (e.g., "Wild About Here", "Upwork")  
**Formula**: (none — manual entry from PHASE_3_OUTREACH_TEMPLATES_PREFILLED.md)  
**Example**: `Wild About Here`

---

#### C: Contact Name
**Type**: Text  
**Description**: Individual contractor name  
**Formula**: (none — manual entry)  
**Example**: `Kriss MacDonald`

---

#### D: Role
**Type**: Dropdown (pre-fill options)  
**Options**: Photographer | Writer | Habitat Specialist | Platform (Upwork/Thumbtack)  
**Formula**: (none)  
**Example**: `Photographer`

---

#### E: Email Address
**Type**: Text  
**Description**: Recipient email address (or "Thumbtack Job #123" for platforms)  
**Formula**: (none — manual entry from PHASE_3_OUTREACH_TEMPLATES_PREFILLED.md)  
**Example**: `wildabouthere.com/contact`

---

#### F: Send Date
**Type**: Date  
**Description**: Date the email was sent (from CONTRACTOR_OUTREACH_SEND_LOG.md)  
**Formula**: (none — manual entry)  
**Example**: `6/22/2026`

---

#### G: Response Date
**Type**: Date  
**Description**: Date the contractor responded (leave blank if no response by June 28)  
**Formula**: (none — manual entry as responses arrive)  
**Example**: `6/24/2026`  
**If no response**: Leave blank or enter `6/28/2026` (deadline cutoff)

---

#### H: Response Status
**Type**: Dropdown (pre-fill options)  
**Options**:  
- `PENDING` (no response yet)
- `RECEIVED — ENTHUSIASTIC` (responded positively, all info provided)
- `RECEIVED — CLARIFICATION NEEDED` (interested but has questions)
- `RECEIVED — NEUTRAL` (responded but non-committal)
- `NO RESPONSE` (deadline passed, no reply)
- `DECLINED` (explicitly said no)
- `SCHEDULED — INFO CALL` (agreed to phone conversation for details)
- `BACKUP OUTREACH SENT` (second-round outreach to backup candidate)

**Formula**: (none — manual entry based on email response)  
**Example**: `RECEIVED — ENTHUSIASTIC`

---

#### I: Fit Score (1–5 Scale)
**Type**: Number  
**Range**: 1–5, where:  
- **5** = Exceptional portfolio/experience match; clear alignment with Phase 3 needs
- **4** = Strong portfolio/experience match; good alignment
- **3** = Acceptable portfolio/experience; some gaps but manageable
- **2** = Weak portfolio/experience; significant gaps
- **1** = Poor match; not suitable unless desperate

**Criteria by role**:
- **Photographers**: Portfolio quality, previous herb/botanical work, flat-lay composition style match
- **Writers**: Published work quality, field guide experience, medicinal herb knowledge
- **Habitat Specialists**: Botanical expertise, native plant/ecology knowledge, educational communication style

**Source for scoring**: Use contractor's response email + PHASE_3_CONTRACTOR_SELECTION_SCORECARD.md Portfolio Fit (×0.35) guidance

**Formula**: (none — manual entry after response received)  
**Example**: `4`

---

#### J: Budget Fit (1–5 Scale)
**Type**: Number  
**Range**: 1–5, where:  
- **5** = Budget well below track ceiling (good negotiation room)
- **4** = Budget at lower end of track ceiling
- **3** = Budget at mid-range of track ceiling
- **2** = Budget at upper end of track ceiling
- **1** = Budget exceeds ceiling; requires significant negotiation

**Track ceilings** (from PHASE_3_CONTRACTOR_SELECTION_SCORECARD.md):
- Photographers: $150–$350/session (up to $500 for licensing bundles)
- Writers: $400–$900 per chapter (up to $1,500 for major contributors)
- Habitat specialists: $400–$900 flat-rate contribution

**Formula**: (none — manual entry based on response email)  
**Example**: `4`

---

#### K: Availability Confirmed (Y/N)
**Type**: Dropdown (Y/N)  
**Description**: Does contractor confirm they are available July 1–August 1?  
**Y** = Confirmed available (in their response email or confirmation call)  
**N** = Not yet confirmed, or unclear  

**Formula**: (none — manual entry)  
**Example**: `Y`

---

#### L: Overall Weighted Score
**Type**: Formula (calculated automatically)  
**Description**: Composite score combining Fit, Budget Fit, Availability, and Success Probability (from PHASE_3_CONTRACTOR_SELECTION_SCORECARD.md)  
**Formula**:  
```
= (I * 0.35) + (J * 0.20) + (IF(K="Y", 5, 3) * 0.30) + (3 * 0.15)
```

**Explanation**:
- I (Fit Score) × 0.35 = Portfolio Fit weight
- J (Budget Fit) × 0.20 = Budget weight
- IF(K="Y", 5, 3) × 0.30 = Availability weight (5 if confirmed, 3 if not)
- 3 × 0.15 = Success Probability (use baseline 3/5 for all respondents, adjust if response quality suggests higher/lower success)

**Threshold interpretation**:
- **8.0–10.0**: Hire immediately
- **7.0–7.9**: Hire (good fit)
- **5.5–6.9**: Conditional hire (if role gap or top candidates decline)
- **Below 5.5**: Pass (poor fit)

**Example**: `(4 * 0.35) + (4 * 0.20) + (5 * 0.30) + (3 * 0.15) = 1.4 + 0.8 + 1.5 + 0.45 = 4.15`

---

#### M: Final Rank
**Type**: Formula (auto-rank by score)  
**Description**: Rank all contractors by Overall Weighted Score (Column L), highest to lowest  
**Formula**:  
```
= RANK(L, L$2:L$12, 0)
```
(Assumes rows 2–12 contain the 11 contractors; adjust row range if needed)

**Result**: 1 = highest score, 11 = lowest score

**Example**: `1`

---

#### N: Selection Status
**Type**: Dropdown (pre-fill options)  
**Options**:
- `SELECTED` (hired for this role)
- `BACKUP` (selected as backup in case primary declines)
- `WAITLIST` (considered but not selected)
- `DECLINED` (not pursuing further)
- `PENDING DECISION` (awaiting final scoring/decision)

**Formula**: (none — manual entry)  
**When to fill**: June 28, 8am–11am (during final decision phase)  
**Example**: `SELECTED`

---

#### O: Notes
**Type**: Text  
**Description**: Free-form field for any additional information during the response tracking window  
**Examples**:
- `Responded with portfolio link — excellent flat-lay style`
- `Asked for scope clarification; sent follow-up June 25`
- `Requested higher rate ($450/session); within negotiation range`
- `No response by June 27 6pm; activated backup candidate`
- `Contacted via LinkedIn after email bounced; re-sent June 23`
- `Declined due to July 1–August 1 conflict; recommend for Phase 4`

**Formula**: (none)

---

## Pre-Filled Baseline Data

### Initialize Sheet with All 11 Contractors (June 22, after emails sent)

| Email Track | Organization | Contact Name | Role | Email Address | Send Date | Response Date | Response Status | Fit Score | Budget Fit | Availability Confirmed | Overall Weighted Score | Final Rank | Selection Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 | Wild About Here | Kriss MacDonald | Photographer | wildabouthere.com/contact | 6/22/2026 | [Pending] | PENDING | — | — | — | — | — | PENDING DECISION | — |
| A2 | Emma TS Robinson Photography | Emma TS Robinson | Photographer | info@emmatsrobinson.co.uk | 6/22/2026 | [Pending] | PENDING | — | — | — | — | — | PENDING DECISION | — |
| A3 | Thumbtack (Platform) | [Photographer from platform] | Photographer | Thumbtack Job #1 | 6/22/2026 | [Pending] | PENDING | — | — | — | — | — | PENDING DECISION | Awaiting bids |
| A4 | PGPA Directory | [Photographer 1] | Photographer | [TBD from search] | 6/22/2026 | [Pending] | PENDING | — | — | — | — | — | PENDING DECISION | Directory search result |
| A5 | Upwork (Platform) | [Photographer from platform] | Photographer | Upwork Job Post | 6/22/2026 | [Pending] | PENDING | — | — | — | — | — | PENDING DECISION | Awaiting proposals |
| B1 | [Rebecca Lexa] | Rebecca Lexa | Writer | [Email TBD] | 6/22/2026 | [Pending] | PENDING | — | — | — | — | — | PENDING DECISION | Naturalist author |
| B2 | LearningHerbs | Emily Han | Writer | [Email TBD] | 6/22/2026 | [Pending] | PENDING | — | — | — | — | — | PENDING DECISION | Wild Remedies co-author |
| B3 | [Adrian White] | Adrian White | Writer | [Email TBD] | 6/22/2026 | [Pending] | PENDING | — | — | — | — | — | PENDING DECISION | Clinical herbalist |
| C1 | Yale University | Arthur Haines | Habitat Specialist | [Email TBD] | 6/22/2026 | [Pending] | PENDING | — | — | — | — | — | PENDING DECISION | Flora Novae Angliae author |
| C2 | Conservation Board Network | [Habitat Specialist 1] | Habitat Specialist | [TBD via referral] | 6/22/2026 | [Pending] | PENDING | — | — | — | — | — | PENDING DECISION | Network referral search |
| C3 | [Backup Habitat Specialist] | [Name TBD] | Habitat Specialist | [Email TBD] | 6/22/2026 | [Pending] | PENDING | — | — | — | — | — | PENDING DECISION | Backup candidate |

---

## Daily Update Routine (June 24–28)

### Each Morning (9am)

1. **Check inbox** for new contractor responses
2. **For each new response**:
   - [ ] Log Response Date (today's date)
   - [ ] Update Response Status (choose from dropdown)
   - [ ] Read response email carefully
   - [ ] Fill Fit Score (1–5)
   - [ ] Fill Budget Fit (1–5)
   - [ ] Fill Availability Confirmed (Y/N)
   - [ ] Add Notes (anything worth remembering)
   - [ ] Overall Weighted Score auto-calculates; verify formula result looks reasonable
3. **If clarification is needed**:
   - [ ] Reply to contractor within 24 hours (use PHASE_3_COMMUNICATION_TEMPLATES.md for clarification email)
   - [ ] Update Notes: "Clarification requested: [question]. Awaiting response."
   - [ ] Update Response Status: `RECEIVED — CLARIFICATION NEEDED`
   - [ ] Set follow-up reminder for June 26 (if no response by then, escalate to backup)
4. **If "no" or declining**:
   - [ ] Update Response Status: `DECLINED`
   - [ ] Update Selection Status: `DECLINED`
   - [ ] If this was a top-tier candidate (score ≥7.0 or critical role), trigger backup outreach same day (June 24, 25, or 26 depending on when decline arrives)
5. **Review overall progress**:
   - [ ] Count responses received (vs. 11 total)
   - [ ] Identify response rate by role (photographers, writers, habitat specialists)
   - [ ] Check if any role is empty (e.g., zero photographer responses)

---

### Each Evening (6pm)

- **Review daily responses** and update Overall Weighted Score
- **Sort by Final Rank** (highest scores at top)
- **Identify front-runners**: Top 3–5 by score (should mostly be scores ≥7.0)
- **Note any tie scores** (if Fit Score 4.15 and Fit Score 4.10, decide tiebreaker: availability, budget fit, or response enthusiasm)
- **Monitor response rate**: Target is 50–70% by June 26 EOD (if below 30% by June 25, prepare to activate backups June 27)

---

### June 27 (Cool Window) — Noon Update

- **Note any new responses** from late responders
- **Re-score if needed** (new info may change Availability Confirmed from N → Y)
- **Check backup candidate needs**: If top 5 candidates don't collectively cover all three roles (photographer, writer, habitat specialist), send backup outreach by 1pm
- **Activate backups only for critical gaps** (not just to replace a single medium-fit candidate)

---

### June 28 (Decision Day) — 8am Update

- **Hard cutoff**: Stop adding new responses after 8am
- **Final scoring**: Calculate Overall Weighted Score for all respondents
- **Rank all contractors** from highest to lowest score
- **Decision window (8am–11am)**:
  - [ ] Select top 3–5 contractors (ensure role coverage: 1+ photographer, 1+ writer, 1+ habitat specialist)
  - [ ] For each selected contractor, update Selection Status: `SELECTED`
  - [ ] For each backup candidate, update Selection Status: `BACKUP`
  - [ ] For each waitlisted candidate, update Selection Status: `WAITLIST`
  - [ ] For each rejected candidate, update Selection Status: `DECLINED`

---

## Google Sheets Conditional Formatting Rules

### Visual Scoring Guide

**Set up conditional formatting in Column L (Overall Weighted Score)** to color-code scores:

| Score Range | Color | Meaning |
|---|---|---|
| 8.0–10.0 | Green | Hire immediately |
| 7.0–7.9 | Blue | Good fit, hire |
| 5.5–6.9 | Yellow | Conditional hire |
| Below 5.5 | Red | Poor fit, pass |

**Setup steps**:
1. Select Column L (Overall Weighted Score)
2. Go to Format → Conditional Formatting
3. Add rule: `Custom formula is` → `=L2>=8` → Green fill
4. Add rule: `Custom formula is` → `=AND(L2>=7, L2<8)` → Blue fill
5. Add rule: `Custom formula is` → `=AND(L2>=5.5, L2<7)` → Yellow fill
6. Add rule: `Custom formula is` → `=L2<5.5` → Red fill

---

### Availability Tracking

**Set up conditional formatting in Column K (Availability Confirmed)** to highlight confirmed vs. pending:

| Status | Color | Meaning |
|---|---|---|
| Y | Green | Available, can proceed |
| N | Orange | Not yet confirmed, follow up needed |
| [blank] | Gray | Not yet responded |

**Setup steps**:
1. Select Column K
2. Go to Format → Conditional Formatting
3. Add rule: `Cell is exactly` → `Y` → Green fill
4. Add rule: `Cell is exactly` → `N` → Orange fill

---

## Sample Tracking Scenarios

### Scenario A: All Respond with High Scores (Best Case)

By June 26 EOD, you receive:

| Email Track | Contact Name | Response Status | Fit Score | Budget Fit | Availability Confirmed | Overall Score | Rank | Selection Status |
|---|---|---|---|---|---|---|---|---|
| A1 | Kriss MacDonald | RECEIVED — ENTHUSIASTIC | 5 | 4 | Y | 8.50 | 1 | SELECTED |
| A3 | [Upwork photographer] | RECEIVED — ENTHUSIASTIC | 4 | 5 | Y | 8.20 | 2 | SELECTED |
| B2 | Emily Han | RECEIVED — ENTHUSIASTIC | 5 | 3 | Y | 7.90 | 3 | SELECTED |
| B1 | Rebecca Lexa | RECEIVED — CLARIFICATION NEEDED | 5 | 2 | N | [Hold pending response] | — | PENDING |
| A2 | Emma TS Robinson | RECEIVED — NEUTRAL | 5 | 3 | N | 6.50 | 7 | WAITLIST |
| C1 | Arthur Haines | RECEIVED — CLARIFICATION NEEDED | 5 | 2 | N | [Hold pending response] | — | PENDING |
| C2 | [Conservation Board referral] | NO RESPONSE | — | — | — | — | — | WAITLIST |
| A4 | [PGPA photographer] | RECEIVED — ENTHUSIASTIC | 4 | 4 | Y | 7.65 | 4 | SELECTED |
| B3 | Adrian White | RECEIVED — ENTHUSIASTIC | 4 | 4 | Y | 7.75 | 5 | BACKUP |
| A5 | [Thumbtack photographer] | RECEIVED — NEUTRAL | 3 | 5 | Y | 6.90 | 8 | WAITLIST |
| C3 | [Backup habitat specialist] | PENDING | — | — | — | — | — | PENDING |

**Decision by June 28**: Select A1 (photographer), A3 (photographer backup), B2 (writer), A4 (photographer), C1 (habitat specialist, pending clarification by June 26). If clarification doesn't arrive, move B3 from BACKUP to SELECTED in the habitat role.

---

### Scenario B: Mixed Responses (Some High, Some Medium, Some No-Response)

By June 27 EOD:

| Email Track | Contact Name | Response Status | Fit Score | Budget Fit | Availability Confirmed | Overall Score | Rank | Selection Status |
|---|---|---|---|---|---|---|---|---|
| A1 | Kriss MacDonald | RECEIVED — ENTHUSIASTIC | 5 | 4 | Y | 8.50 | 1 | SELECTED |
| B2 | Emily Han | RECEIVED — CLARIFICATION NEEDED | 4 | 3 | N | [Hold pending response] | — | PENDING |
| A3 | [Upwork photographer] | NO RESPONSE | — | — | — | — | — | WAITLIST |
| C1 | Arthur Haines | RECEIVED — NEUTRAL | 4 | 2 | N | 5.85 | 9 | WAITLIST |
| B1 | Rebecca Lexa | NO RESPONSE | — | — | — | — | — | WAITLIST |
| A2 | Emma TS Robinson | RECEIVED — ENTHUSIASTIC | 5 | 3 | Y | 7.95 | 2 | SELECTED |
| A4 | [PGPA photographer] | RECEIVED — CLARIFICATION NEEDED | 4 | 4 | N | [Hold pending response] | — | PENDING |
| B3 | Adrian White | RECEIVED — ENTHUSIASTIC | 4 | 4 | Y | 7.75 | 3 | SELECTED |
| C2 | [Conservation Board referral] | BACKUP OUTREACH SENT | — | — | — | — | — | PENDING |
| A5 | [Thumbtack photographer] | RECEIVED — NEUTRAL | 3 | 5 | Y | 6.90 | 8 | WAITLIST |
| C3 | [Backup habitat specialist] | PENDING | — | — | — | — | — | PENDING |

**Decision by June 28**: 
1. Select A1 (photographer rank 1), A2 (photographer rank 2), B3 (writer rank 3)
2. For habitat specialist: Unclear. C1 scored 5.85 (below threshold). C2 backup outreach sent June 27; if any response arrives by June 28 10am, score and select. If no response, either negotiate with C1 (accept lower fit for July 1 start) or defer habitat work to Phase 4 and proceed with 2 roles only.
3. Wait for A4 clarification by June 28 noon. If clarification improves score ≥7.0 and confirms availability, make them photographer backup. Otherwise, demote to waitlist.

---

## Markdown Fallback (If Google Sheets Unavailable)

If Google Sheets is down or inaccessible, use this Markdown table as backup:

### June 24–28 Response Log

```markdown
## Contractor Response Log — June 22–28, 2026

Last updated: [TODAY'S DATE] [TIME]

| Track | Name | Role | Send Date | Response Date | Status | Fit | Budget | Avail | Score | Rank | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 | Kriss MacDonald | Photographer | 6/22 | 6/24 | ENTHUSIASTIC | 5 | 4 | Y | 8.50 | 1 | Excellent portfolio match |
| A2 | Emma TS Robinson | Photographer | 6/22 | 6/26 | ENTHUSIASTIC | 5 | 3 | Y | 7.95 | 2 | Bronze Medal RHS; needs UK payment coordination |
| A3 | Upwork | Photographer | 6/22 | 6/24 | NO RESPONSE | — | — | — | — | — | Job posted; awaiting proposals |
| A4 | PGPA | Photographer | 6/22 | 6/25 | CLARIFICATION | 4 | 4 | N | [HOLD] | — | Asked about turnaround time; awaiting response |
| A5 | Thumbtack | Photographer | 6/22 | 6/25 | NEUTRAL | 3 | 5 | Y | 6.90 | — | Interested but unclear on flat-lay experience |
| B1 | Rebecca Lexa | Writer | 6/22 | [NONE] | NO RESPONSE | — | — | — | — | — | Known author; may still respond by 6/28 |
| B2 | Emily Han | Writer | 6/22 | 6/24 | CLARIFICATION | 4 | 3 | N | [HOLD] | — | Interested; asked if we could delay to Aug 1 start |
| B3 | Adrian White | Writer | 6/22 | 6/24 | ENTHUSIASTIC | 4 | 4 | Y | 7.75 | 3 | Clinician + published author; FTC/CITES compliant |
| C1 | Arthur Haines | Habitat | 6/22 | 6/26 | NEUTRAL | 4 | 2 | N | 5.85 | — | Yale botanist; schedule unclear, may conflict |
| C2 | Conservation Board | Habitat | 6/22 | [NONE] | NO RESPONSE | — | — | — | — | — | Backup outreach sent 6/27 |
| C3 | [Backup] | Habitat | 6/22 | [PENDING] | PENDING | — | — | — | — | — | No response yet; check 6/28 morning |
```

---

## Post-Decision: Handoff Files

After June 28 EOD decision is complete, pass this information to:

1. **CONTRACTOR_SELECTION_DECISION_LOG.md** (new file)
   - Document final selection: who hired, for which role, final score
   - Include reasoning for each hire (why this candidate vs. others)
   - Include backup plan (if primary declines, hire backup)

2. **PHASE_3_COMMUNICATION_TEMPLATES.md**
   - Use offer letter template to send formal offers to selected contractors (sent evening of June 28)

3. **PHASE_3_CONTRACTOR_DAILY_TRACKING_CHECKLIST.md**
   - Transition to daily contractor coordination (June 29–August 1)
   - Log milestone submissions, approvals, payment processing

---

## Useful Formulas Reference

If building your own Google Sheets, use these formulas:

**Count responses received**:
```
=COUNTIF(H:H, "RECEIVED*") + COUNTIF(H:H, "ENTHUSIASTIC") + COUNTIF(H:H, "NEUTRAL") + COUNTIF(H:H, "DECLINED")
```

**Count by role**:
```
=COUNTIFS(D:D, "Photographer", H:H, "RECEIVED*")
=COUNTIFS(D:D, "Writer", H:H, "RECEIVED*")
=COUNTIFS(D:D, "Habitat Specialist", H:H, "RECEIVED*")
```

**Count confirmed available**:
```
=COUNTIF(K:K, "Y")
```

**Average fit score (among respondents only)**:
```
=AVERAGEIF(I:I, ">0", I:I)
```

**Identify highest scorer**:
```
=MAX(L:L)
```

---

## Support & Troubleshooting

**Q: What if a contractor takes days to respond (no response June 24–26, but responds June 27)?**  
A: Log normally. Treat as "cool window" response. Score and rank. If score ≥7.0, still consider for hiring. Late response doesn't penalize score (response timing is tracked but not weighted).

**Q: What if two contractors have identical scores (e.g., both 7.50)?**  
A: Use tiebreaker criteria:
1. Availability Confirmed (Y > N)
2. Budget Fit (lower budget = more room for negotiation)
3. Response enthusiasm (ENTHUSIASTIC > NEUTRAL > CLARIFICATION NEEDED)
4. Send date (earlier send = higher priority if tied)

**Q: Can I change the weighted formula to emphasize availability over portfolio fit?**  
A: Yes. Adjust weights in Column L formula, e.g., (I * 0.25) + (J * 0.20) + (IF(K="Y", 5, 3) * 0.40) + (3 * 0.15). Document rationale in Notes.

**Q: What if the top-scorer has a potential issue (e.g., "enthusiastic but budget is a bit high, haven't confirmed availability yet")?**  
A: Do not select based on raw score alone. Use June 28 decision window to reconcile concerns:
1. Send clarification email June 26 asking for budget flexibility + availability confirmation
2. If no response by June 28 9am, make decision with incomplete info (pro: high fit score; con: missing availability/budget clarity)
3. Document decision reasoning in CONTRACTOR_SELECTION_DECISION_LOG.md

---

**Status**: Ready to use starting June 23 (set up immediately after emails sent on June 22)  
**Next step**: Use CONTRACTOR_SELECTION_TIMELINE.md to understand response windows + when to score each tier of responses
