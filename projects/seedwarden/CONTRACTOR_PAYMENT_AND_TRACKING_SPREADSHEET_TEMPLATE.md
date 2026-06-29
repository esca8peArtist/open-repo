---
title: "Contractor Payment and Tracking Spreadsheet Template — Q3 Launch"
date: 2026-06-29
version: 1.0
status: production-ready
format: Pre-populated Google Sheets schema (CSV import block included)
sprint-window: July 5 – August 17, 2026
instructions: >
  1. Copy the CSV block below and paste into Google Sheets (import as CSV or paste into Sheet1, cell A1).
  2. Add contractor names in the [Name] rows once hires are confirmed (July 4–5).
  3. Update weekly every Monday with delivery status, review results, and payment confirmations.
  4. Share read-only with Logistics Coordinator for Monday check-in reference.
cross-references:
  - CONTRACTOR_HIRING_TIMELINE_AND_RUBRIC.md (hire dates, payment methods)
  - CONTRACTOR_ONBOARDING_PLAYBOOK.md (payment triggers per quality gate)
  - CONTRACTOR_COMMUNICATION_TEMPLATES.md (payment notification templates)
  - PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md (performance summary metrics)
---

# Contractor Payment and Tracking Spreadsheet Template

**Purpose**: Single source of truth for all contractor deliverables, payment milestones, review statuses, and FTC compliance checkpoints. Update every Monday. Share updated version with Logistics Coordinator for same-day check-in email.

---

## Schema Overview

| Column | Type | Update Frequency | Notes |
|---|---|---|---|
| Contractor Name | Text | Once (at hire) | Must match contract signature exactly |
| Role | Select | Once (at hire) | Photographer / Writer #1 / Writer #2 / Herbalist / Coordinator / Social Media Manager |
| Deliverable Description | Text | Once (at onboarding) | One row per milestone deliverable |
| Deliverable Due Date | Date | Once (per contract) | YYYY-MM-DD format; explicit dates only |
| Delivered Date (ACTUAL) | Date | On delivery | Same day contractor submits; leave blank until then |
| Review Status | Select | Within 24h of delivery | NOT STARTED / PENDING / APPROVED / REVISION REQUESTED / REVISION SUBMITTED / APPROVED (after revision) |
| Payment Milestone | Text | Once (at onboarding) | Milestone 1 (50%) / Milestone 2 (50%) — or 33/33/34 for Herbalist |
| Payment Due Date | Date | Once (per contract) | Typically same day as approval trigger |
| Amount Due | Currency | Once (per contract) | Dollar amount for this milestone |
| Payment Sent Date (ACTUAL) | Date | On dispatch | Date you initiated payment (Venmo send, PayPal, etc.) |
| Payment Method | Text | Once (per contractor) | Venmo / PayPal / Zelle / ACH / Wire |
| FTC Disclosure Date | Date | Post-launch | Date content goes live; N/A for internal roles (Herbalist, Coordinator) |
| Performance Notes | Text | As needed | Quality observations, revision context, escalation notes |

---

## CSV Template (Ready to Import)

```csv
Contractor Name,Role,Deliverable Description,Deliverable Due Date,Delivered Date (ACTUAL),Review Status,Payment Milestone,Payment Due Date,Amount Due,Payment Sent Date (ACTUAL),Payment Method,FTC Disclosure Date (Post-Launch),Performance Notes
[Name],Photographer,Deposit — contract signature,2026-07-05,,NOT STARTED,Milestone 1 (50%),2026-07-05,$700.00,,,N/A,
[Name],Photographer,Women's Health set (5 images),2026-07-07,,NOT STARTED,Quality Gate 1,2026-07-07,$0.00,,,2026-07-06,Milestone 2 triggers on final set approval
[Name],Photographer,Respiratory Health set (5 images),2026-07-14,,NOT STARTED,Quality Gate 2,2026-07-14,$0.00,,,2026-07-06,
[Name],Photographer,Sleep & Nervines set (5 images),2026-07-21,,NOT STARTED,Quality Gate 3,2026-07-21,$0.00,,,2026-07-13,
[Name],Photographer,Immunity Support set (5 images) — FINAL,2026-07-28,,NOT STARTED,Milestone 2 (50%),2026-07-28,$700.00,,,2026-07-20,Release on final set approval after revisions complete
[Name],Writer #1,Deposit — contract signature,2026-07-05,,NOT STARTED,Milestone 1 (50%),2026-07-05,$475.00,,,N/A,Women's Health bundle
[Name],Writer #1,Women's Health manuscript draft (3600-3800 words),2026-07-21,,NOT STARTED,Quality Gate 1,2026-07-21,$0.00,,,2026-07-06,Mandatory: TSH named contraindication; damiana verbatim statement; FTC compliant
[Name],Writer #1,Women's Health manuscript — all revisions complete — FINAL,2026-07-26,,NOT STARTED,Milestone 2 (50%),2026-07-26,$475.00,,,2026-07-06,Release on herbalist feedback incorporated and final approved
[Name],Writer #2,Deposit — contract signature,2026-07-05,,NOT STARTED,Milestone 1 (33%),2026-07-05,$347.00,,,N/A,Respiratory + Sleep bundles
[Name],Writer #2,Respiratory Health manuscript draft (3200-3500 words),2026-07-17,,NOT STARTED,Quality Gate 1,2026-07-21,$0.00,,,2026-07-06,Mandatory: E. angustifolia At-Risk; elderberry toxicity; echinacea autoimmune
[Name],Writer #2,Respiratory manuscript approved,2026-07-21,,NOT STARTED,Milestone 2 (33%),2026-07-21,$347.00,,,2026-07-06,Payment on Respiratory approval
[Name],Writer #2,Sleep & Nervines manuscript draft + all revisions — FINAL,2026-08-07,,NOT STARTED,Milestone 3 (34%),2026-08-07,$356.00,,,2026-07-13,Mandatory: valerian CNS named; passionflower MAOI named; sedative disclaimer verbatim
[Name],Herbalist,Deposit — contract signature,2026-07-07,,NOT STARTED,Milestone 1 (33%),2026-07-07,$280.00,,,N/A,4-bundle review
[Name],Herbalist,Women's Health review (inline + summary email),2026-07-11,,NOT STARTED,Review delivery,2026-07-11,$0.00,,,N/A,Forward notes to Writer #1 within 24h of receipt
[Name],Herbalist,Respiratory review (inline + summary email),2026-07-18,,NOT STARTED,Review delivery,2026-07-18,$0.00,,,N/A,
[Name],Herbalist,Women's Health + Respiratory reviews complete,2026-07-21,,NOT STARTED,Milestone 2 (33%),2026-07-21,$280.00,,,N/A,Payment on both reviews received and approved
[Name],Herbalist,Sleep & Nervines review (inline + summary email),2026-07-25,,NOT STARTED,Review delivery,2026-07-25,$0.00,,,N/A,
[Name],Herbalist,Immunity Support review + all feedback consolidated — FINAL,2026-08-07,,NOT STARTED,Milestone 3 (34%),2026-08-07,$290.00,,,N/A,CITES Goldenseal verification mandatory
[Name],Coordinator,Deposit + orientation call complete,2026-07-05,,NOT STARTED,Milestone 1 (50%),2026-07-05,$450.00,,,N/A,
[Name],Coordinator,7-week coordination complete (check-ins + Etsy + email + dashboard),2026-08-17,,NOT STARTED,Milestone 2 (50%),2026-08-17,$450.00,,,N/A,All 4 bundles live; tracker updated; campaigns sent
[Name],Social Media Manager,Deposit + orientation call complete,2026-07-05,,NOT STARTED,Milestone 1 (50%),2026-07-05,$400.00,,,N/A,
[Name],Social Media Manager,7-week social calendar executed + final performance report — FINAL,2026-08-17,,NOT STARTED,Milestone 2 (50%),2026-08-17,$400.00,,,2026-08-17,All 4 launch weeks executed; FTC compliance maintained
```

---

## Pre-Populated Sample Rows (With Example Data)

Use this to verify your import formatting before replacing with actual contractor data:

```csv
Contractor Name,Role,Deliverable Description,Deliverable Due Date,Delivered Date (ACTUAL),Review Status,Payment Milestone,Payment Due Date,Amount Due,Payment Sent Date (ACTUAL),Payment Method,FTC Disclosure Date (Post-Launch),Performance Notes
"Sarah Chen",Photographer,Deposit — contract signature,2026-07-05,2026-07-05,APPROVED,Milestone 1 (50%),2026-07-05,$700.00,2026-07-05,Venmo,N/A,Contract signed July 5; deposit sent same day
"Sarah Chen",Photographer,Women's Health set (5 images),2026-07-07,2026-07-07,APPROVED,Quality Gate 1,2026-07-07,$0.00,,Venmo,2026-07-06,"All 5 images; warm lighting excellent; white balance consistent; file naming correct"
"Sarah Chen",Photographer,Respiratory Health set (5 images),2026-07-14,2026-07-14,APPROVED,Quality Gate 2,2026-07-14,$0.00,,Venmo,2026-07-06,Color consistency matches Women's Health set; props on-aesthetic
"Sarah Chen",Photographer,Sleep & Nervines set (5 images),2026-07-21,2026-07-22,REVISION REQUESTED,Quality Gate 3,2026-07-23,$0.00,,Venmo,2026-07-13,"Two images with cold color cast; resubmitted Jul 23; approved Jul 23"
"Sarah Chen",Photographer,Immunity Support set (5 images) — FINAL,2026-07-28,2026-07-28,APPROVED,Milestone 2 (50%),2026-07-28,$700.00,2026-07-28,Venmo,2026-07-20,All 20 images complete and approved; goldenseal props confirmed cultivated-source
"Marcus Webb","Writer #1",Deposit — contract signature,2026-07-05,2026-07-05,APPROVED,Milestone 1 (50%),2026-07-05,$475.00,2026-07-05,PayPal,N/A,
"Marcus Webb","Writer #1","Women's Health manuscript draft (3600-3800 words)",2026-07-21,2026-07-21,REVISION REQUESTED,Quality Gate 1,2026-07-23,$0.00,,PayPal,2026-07-06,"Lemon balm thyroid named correctly; damiana statement verbatim correct. Revision: red clover contraindication table incomplete — add hormone therapy interaction detail. Revised Jul 23."
"Marcus Webb","Writer #1","Women's Health manuscript — all revisions complete — FINAL",2026-07-26,2026-07-26,APPROVED,Milestone 2 (50%),2026-07-26,$475.00,2026-07-26,PayPal,2026-07-06,Herbalist feedback from Dr. White incorporated; all mandatory elements verified; approved
"Priya Nair","Writer #2",Deposit — contract signature,2026-07-05,2026-07-05,APPROVED,Milestone 1 (33%),2026-07-05,$347.00,2026-07-05,Zelle,N/A,
"Priya Nair","Writer #2","Respiratory Health manuscript draft (3200-3500 words)",2026-07-17,2026-07-17,APPROVED,Quality Gate 1,2026-07-21,$0.00,,Zelle,2026-07-06,"Strong echinacea two-species treatment; E. angustifolia At-Risk flag present; elderberry toxicity warning correct; FTC clean"
"Priya Nair","Writer #2",Respiratory manuscript approved,2026-07-21,2026-07-21,APPROVED,Milestone 2 (33%),2026-07-21,$347.00,2026-07-21,Zelle,2026-07-06,Herbalist review feedback incorporated; payment released
"Priya Nair","Writer #2","Sleep & Nervines manuscript draft + all revisions — FINAL",2026-08-07,2026-08-07,APPROVED,Milestone 3 (34%),2026-08-07,$356.00,2026-08-07,Zelle,2026-07-13,"Valerian CNS section strong; passionflower MAOI named correctly; Silexan distinction clear; sedative disclaimer verbatim"
"Dr. Adrian White",Herbalist,Deposit — contract signature,2026-07-07,2026-07-07,APPROVED,Milestone 1 (33%),2026-07-07,$280.00,2026-07-07,PayPal,N/A,
"Dr. Adrian White",Herbalist,"Women's Health review (inline + summary email)",2026-07-11,2026-07-11,APPROVED,Review delivery,2026-07-11,$0.00,,PayPal,N/A,"Flagged red clover hormone therapy interaction specificity; damiana evidence-tier framing confirmed; actionable inline comments"
"Dr. Adrian White",Herbalist,"Respiratory review (inline + summary email)",2026-07-18,2026-07-18,APPROVED,Review delivery,2026-07-18,$0.00,,PayPal,N/A,"Echinacea autoimmune wording approved; elderberry sambunigrin language adequate; E. angustifolia conservation language confirmed"
"Dr. Adrian White",Herbalist,"Women's Health + Respiratory reviews complete",2026-07-21,2026-07-21,APPROVED,Milestone 2 (33%),2026-07-21,$280.00,2026-07-21,PayPal,N/A,Both reviews received and incorporated; payment released
"Dr. Adrian White",Herbalist,"Sleep & Nervines review (inline + summary email)",2026-07-25,2026-07-25,APPROVED,Review delivery,2026-07-25,$0.00,,PayPal,N/A,"Valerian CNS list complete; passionflower MAOI confirmed; lavender Silexan distinction verified"
"Dr. Adrian White",Herbalist,"Immunity Support review + all feedback consolidated — FINAL",2026-08-07,2026-08-07,APPROVED,Milestone 3 (34%),2026-08-07,$290.00,2026-08-07,PayPal,N/A,"Goldenseal CITES Appendix II language confirmed; ashwagandha thyroid interaction verified; CYP450 substrate list complete"
"Elena Rodriguez",Coordinator,Deposit + orientation call complete,2026-07-05,2026-07-05,APPROVED,Milestone 1 (50%),2026-07-05,$450.00,2026-07-05,Venmo,N/A,Kickoff call July 6 9am; Kit and Etsy access confirmed
"Elena Rodriguez",Coordinator,"7-week coordination complete (check-ins + Etsy + email + dashboard)",2026-08-17,2026-08-17,APPROVED,Milestone 2 (50%),2026-08-17,$450.00,2026-08-17,Venmo,N/A,"All 7 Monday check-ins completed; 4 bundle Etsy listings live; all email campaigns sent on schedule; tracker updated weekly throughout"
"Diego Alvarez","Social Media Manager",Deposit + orientation call complete,2026-07-05,2026-07-05,APPROVED,Milestone 1 (50%),2026-07-05,$400.00,2026-07-05,PayPal,N/A,
"Diego Alvarez","Social Media Manager","7-week social calendar executed + final performance report — FINAL",2026-08-17,2026-08-17,APPROVED,Milestone 2 (50%),2026-08-17,$400.00,2026-08-17,PayPal,2026-08-17,"All 4 launch weeks executed; avg engagement rate 4.2%; 847 Etsy link clicks from social; FTC compliance maintained; no escalations"
```

---

## Column Usage Guide

### Review Status — Valid Values

| Status | Meaning |
|---|---|
| NOT STARTED | Work not yet received; delivery window not yet open |
| PENDING | Received; under review (update within 24h of delivery) |
| APPROVED | Passed quality gate; payment ready to release |
| REVISION REQUESTED | Quality issues found; specific feedback sent to contractor |
| REVISION SUBMITTED | Contractor resubmitted after revision request |
| APPROVED (after revision) | Revision passed; payment ready to release |

Update same day as delivery to maintain momentum. Do not leave PENDING for more than 24 hours.

### FTC Disclosure Date

- Photographer, Writers, Social Media Manager: enter the date the content goes live on Etsy/email/social
- Herbalist, Coordinator: enter N/A (internal roles; content not published under their name)
- For FTC audit trail: 30 days post-launch, confirm all live content has appropriate disclosures (FTC-compliant language in Etsy listings, #ad where required in social posts, photographer byline handling documented)

### Performance Notes — Examples

- "Session 1 approved; image 3 has slight warm cast but within range. On-time delivery."
- "Respiratory draft approved; herbalist flagged echinacea autoimmune wording — writer revised in 24h."
- "2 days late on Sleep draft; communicated delay in advance; quality excellent on receipt."
- "Revision submitted; recheck color consistency; re-approved Jul 23."
- "BACKUP activated Jul 18 — original contractor medical leave; Tier 2 writer onboarded same day."

---

## Weekly Update Protocol (Every Monday, 9am ET)

1. Open spreadsheet in Google Sheets
2. For each contractor with an active delivery window:
   - Check for new deliverables (email, shared Drive, Upwork message)
   - If delivered: update "Delivered Date (ACTUAL)" and set Review Status to PENDING
   - Complete quality gate review (see CONTRACTOR_ONBOARDING_PLAYBOOK.md quality gate section)
   - Update Review Status to APPROVED or REVISION REQUESTED
   - If approved: log Payment Sent Date on same day payment is dispatched
3. Add performance notes for any delays, escalations, or quality observations
4. Share updated sheet with Coordinator for Monday check-in email
5. Archive prior week's version (download as CSV with date stamp)

---

## FTC Review Checklist (Post-Launch)

Run this 30 days after each bundle goes live on Etsy.

**Photographer content**:
- [ ] All 20 images live in Etsy listings (confirm listing IDs)
- [ ] No photographer byline in listings unless separately negotiated
- [ ] Goldenseal prop sourcing documented in project records

**Writer content**:
- [ ] All therapeutic claims in live Etsy descriptions use evidence-tier framing (no unqualified claims)
- [ ] Damiana limited-evidence statement present in Women's Health listing description
- [ ] Named contraindications (TSH, MAOI, CNS, CITES) present in relevant listing descriptions

**Social Media Manager content**:
- [ ] All promotional posts have #ad where applicable
- [ ] No unqualified health claims in any post text
- [ ] All posts with Etsy product links include FTC-compliant promotional language

**Herbalist sign-off**:
- [ ] Herbalist review notes confirm FTC compliance across all four bundles (on file in shared Drive)

---

## Payment Budget Reconciliation

### Total Q3 Contractor Budget

| Role | Milestone 1 | Milestone 2 | Milestone 3 | Total |
|---|---|---|---|---|
| Photographer | $700 | $700 | — | $1,400 |
| Writer #1 (Women's Health) | $475 | $475 | — | $950 |
| Writer #2 (Respiratory + Sleep) | $347 | $347 | $356 | $1,050 |
| Herbalist Consultant | $280 | $280 | $290 | $850 |
| Logistics Coordinator | $450 | $450 | — | $900 |
| Social Media Manager | $400 | $400 | — | $800 |
| **TOTAL** | **$2,652** | **$2,652** | **$646** | **$5,950** |

### Running Reconciliation Checklist

Run at end of each week:

- [ ] Total "Amount Due" for all milestones paid so far: $___________
- [ ] Match against Venmo/PayPal/bank statement history for the same period
- [ ] Flag any discrepancy (unpaid milestone, wrong amount, duplicate)
- [ ] Confirm all "Payment Sent Date (ACTUAL)" entries have corresponding receipts

Run at project close (August 17):

- [ ] Total paid to all contractors: $___________
- [ ] Target: $5,950 gross
- [ ] All "Payment Sent Date (ACTUAL)" cells populated (no blanks in paid milestones)
- [ ] All "Review Status" cells show APPROVED or APPROVED (after revision) — no pending revisions
- [ ] Archive final spreadsheet: filename `Phase3_Contractor_Tracking_FINAL_2026-08-17.csv`

---

## Status Dashboard Summary (Second Sheet — Optional)

Create a second Google Sheet tab named "Summary" with the following manual table. Update when milestones are paid.

| Contractor | Role | Total Contract | Milestone 1 | Milestone 2 | Milestone 3 | Total Paid | % Complete |
|---|---|---|---|---|---|---|---|
| [Name] | Photographer | $1,400 | — | — | — | $0 | 0% |
| [Name] | Writer #1 | $950 | — | — | — | $0 | 0% |
| [Name] | Writer #2 | $1,050 | — | — | — | $0 | 0% |
| [Name] | Herbalist | $850 | — | — | — | $0 | 0% |
| [Name] | Coordinator | $900 | — | — | — | $0 | 0% |
| [Name] | Social Media Mgr | $800 | — | — | — | $0 | 0% |
| **TOTAL** | — | **$5,950** | — | — | — | **$0** | **0%** |

Replace "—" with PAID, PENDING, or N/A as milestones are reached. Update % Complete column as payments are made.

---

## Import Instructions

**Google Sheets (recommended)**:
1. Copy the CSV block above (from "Contractor Name" header row through last data row)
2. Open Google Sheets → Create new spreadsheet
3. Name: `Phase 3 Contractor Payment & Tracking — Q3 2026`
4. Click cell A1 → File → Import → Paste data → select "comma" as separator → import
5. Format header row: bold, light gray fill (#f3f3f3)
6. Freeze row 1 (View → Freeze → 1 row)
7. Set column widths: Contractor (150px), Role (120px), Deliverable (250px), Dates (110px), Status (180px), Notes (300px)
8. Add data validation to Review Status column: restrict to valid values listed above
9. Share with Coordinator (read-only access)

**Excel**:
1. Copy CSV block
2. Open Excel → New workbook → Data tab → From Text/CSV → paste
3. Delimiter: Comma
4. Format as Table (Insert → Table)
5. Save as `.xlsx`; share via OneDrive or email attachment weekly

**Contingency row format (if backup contractor activated)**:
- Add new row immediately below original contractor row
- Contractor Name: `[BACKUP] [Name]`
- Notes: `BACKUP — replaced [original contractor name] on [date] due to [reason]. Contract value: $[amount]. Scope: [reduced/full].`
