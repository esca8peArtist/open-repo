---
title: "Phase 3 Contractor Payment Tracking — Google Sheets Template with FTC Disclosure Checkpoints"
date: 2026-06-29
version: 1.0
status: production-ready
sprint-window: July 1 – August 10, 2026
format: Google Sheets import template (CSV structure with instructions)
cross-references:
  - PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md (milestone summary)
  - PHASE_3_CONTRACTOR_ONBOARDING_CHECKLIST.md (payment trigger events)
  - PHASE_3_CONTRACTOR_COMMUNICATION_TEMPLATES.md (payment notification templates)
  - PHASE_3_CONTRACTOR_SELECTION_RUBRIC.md (contractor rate benchmarks)
---

# Phase 3 Contractor Payment Tracking

**Purpose**: Maintain a single, auditable record of all contractor deliverables, payment milestones, and FTC disclosure dates across 6 roles and 6 weeks of production.

**Update cadence**: Every Monday (9am ET, during coordinator check-in) and immediately upon each delivery or payment event.

**FTC compliance checkpoint**: Before releasing any bundle for Etsy listing, verify the FTC Disclosure Date column is populated for all content contractors (Photographer, Writer 1, Writer 2, Writer 3). Internal roles (Herbalist Consultant, Coordinator) are marked N/A.

---

## Google Sheets Setup Instructions

1. Open a new Google Sheet and name it: "Phase 3 Contractor Payment and Tracking"
2. In Sheet 1 (rename to "Tracking"), paste the CSV template below starting at cell A1
3. Format row 1 as header (bold, light blue background)
4. Set column widths: Name (160px), Role (120px), Deliverables (250px), Dates (120px), Status (180px), Amounts (100px), Method (100px), FTC Date (130px), Notes (300px)
5. Create Sheet 2 and rename to "Summary" — use the summary template at the bottom of this document
6. Share Sheet 1 with read-only access to Coordinator (they update the tracking sheet; you review)
7. Enable "Notify on changes" for cell edits (Tools > Notification rules)

---

## Column Definitions

| Column | Format | When to Update | Notes |
|---|---|---|---|
| Contractor Name | First Last | Once at hire | Must match signed contract |
| Role | Select: Photographer / Writer 1 / Writer 2 / Writer 3 Clinical / Herbalist Consultant / Coordinator | Once at hire | |
| Deliverable | Human-readable description | Once at onboarding | One row per deliverable |
| Deliverable Due Date | YYYY-MM-DD | Once at onboarding | From contract terms |
| Delivered Date [ACTUAL] | YYYY-MM-DD or blank | Same day as delivery | Leave blank until received |
| Review Status | NOT STARTED / PENDING / APPROVED / REVISION REQUESTED / REVISION SUBMITTED / APPROVED AFTER REVISION | Within 24h of delivery | Update same day as review |
| Payment Milestone | Milestone 1–4 (25%) or Milestone 1–3 (33/33/34) or Weekly | Once at onboarding | |
| Payment Due Date | YYYY-MM-DD | Once at onboarding | Per contract milestone trigger |
| Amount Due | $XXX.XX | Once at onboarding | 25% of total for most roles |
| Payment Sent Date [ACTUAL] | YYYY-MM-DD or blank | Same day as payment dispatch | Log when initiated, not when received |
| Payment Method | Venmo / PayPal / Zelle / ACH / Wire | Once at hire | Standardize across all milestones per contractor |
| FTC Disclosure Date | YYYY-MM-DD or N/A | After Etsy launch | Date content goes live; verify disclosure present within 30 days |
| Notes | Free text | As needed | Revisions, delays, quality flags, communication notes |

---

## CSV Template (Import to Google Sheets)

```
Contractor Name,Role,Deliverable,Deliverable Due Date,Delivered Date [ACTUAL],Review Status,Payment Milestone,Payment Due Date,Amount Due,Payment Sent Date [ACTUAL],Payment Method,FTC Disclosure Date,Notes
[Name],Photographer,Deposit — contract signature,2026-07-01,,,Milestone 1 (25%),2026-07-01,$[25% of total],,,[payment method],,
[Name],Photographer,Session 1 — 5 images Respiratory,2026-07-05,,,Milestone 2 (25%),2026-07-05,$[25% of total],,,[payment method],,
[Name],Photographer,Session 2 — 5 images Immunity,2026-07-12,,,Milestone 3 (25%),2026-07-12,$[25% of total],,,[payment method],,
[Name],Photographer,Session 3 — 5 images Digestive + final handoff,2026-07-24,,,Milestone 4 (25%),2026-07-24,$[25% of total],,,[payment method],,
[Name],Writer 1,Deposit — contract signature,2026-07-01,,,Milestone 1 (25%),2026-07-01,$[25% of total],,,[payment method],,
[Name],Writer 1,Respiratory bundle — 3600 words,2026-07-08,,,Milestone 2 (25%),2026-07-08,$[25% of total],,,[payment method],,
[Name],Writer 1,Immunity bundle — 3800 words,2026-07-15,,,Milestone 3 (25%),2026-07-15,$[25% of total],,,[payment method],,
[Name],Writer 1,Digestive bundle + all revisions,2026-08-03,,,Milestone 4 (25%),2026-08-03,$[25% of total],,,[payment method],,
[Name],Writer 2,Deposit — contract signature,2026-07-01,,,Milestone 1 (25%),2026-07-01,$[25% of total],,,[payment method],,
[Name],Writer 2,Respiratory recipes — 8-10 recipes,2026-07-08,,,Milestone 2 (25%),2026-07-08,$[25% of total],,,[payment method],,
[Name],Writer 2,Immunity recipes — 8-10 recipes,2026-07-15,,,Milestone 3 (25%),2026-07-15,$[25% of total],,,[payment method],,
[Name],Writer 2,Digestive recipes + all revisions,2026-08-03,,,Milestone 4 (25%),2026-08-03,$[25% of total],,,[payment method],,
[Name],Writer 3 Clinical,Deposit — contract signature,2026-07-01,,,Milestone 1 (25%),2026-07-01,$[25% of total],,,[payment method],,
[Name],Writer 3 Clinical,Respiratory clinical section,2026-07-08,,,Milestone 2 (25%),2026-07-08,$[25% of total],,,[payment method],,
[Name],Writer 3 Clinical,Immunity clinical section,2026-07-15,,,Milestone 3 (25%),2026-07-15,$[25% of total],,,[payment method],,
[Name],Writer 3 Clinical,Digestive clinical section + revisions,2026-08-03,,,Milestone 4 (25%),2026-08-03,$[25% of total],,,[payment method],,
[Name],Herbalist Consultant,Deposit — contract signature,2026-07-01,,,Milestone 1 (33%),2026-07-01,$[33% of total],,,[payment method],N/A,
[Name],Herbalist Consultant,Respiratory + Immunity reviews,2026-07-15,,,Milestone 2 (33%),2026-07-15,$[33% of total],,,[payment method],N/A,
[Name],Herbalist Consultant,Digestive review + consolidated feedback,2026-08-03,,,Milestone 3 (34%),2026-08-03,$[34% of total],,,[payment method],N/A,
[Name],Coordinator,Deposit — contract signature,2026-07-01,,,Milestone 1 (25%),2026-07-01,$[25% of total],,,[payment method],N/A,
[Name],Coordinator,Weeks 1-2 check-ins + Etsy coordination,2026-07-12,,,Milestone 2 (25%),2026-07-12,$[25% of total],,,[payment method],N/A,
[Name],Coordinator,Weeks 3-4 check-ins + email campaigns,2026-07-26,,,Milestone 3 (25%),2026-07-26,$[25% of total],,,[payment method],N/A,
[Name],Coordinator,Weeks 5-6 + final handoff,2026-08-10,,,Milestone 4 (25%),2026-08-10,$[25% of total],,,[payment method],N/A,
```

---

## Pre-Filled Example (With Sample Contractor Names)

```
Contractor Name,Role,Deliverable,Deliverable Due Date,Delivered Date [ACTUAL],Review Status,Payment Milestone,Payment Due Date,Amount Due,Payment Sent Date [ACTUAL],Payment Method,FTC Disclosure Date,Notes
Jordan Kim,Photographer,Deposit — contract signature,2026-07-01,2026-07-01,APPROVED,Milestone 1 (25%),2026-07-01,$350.00,2026-07-01,Venmo,N/A (deposit),Contract signed 2026-07-01; deposit sent same day
Jordan Kim,Photographer,Session 1 — 5 images Respiratory,2026-07-05,2026-07-05,APPROVED,Milestone 2 (25%),2026-07-05,$350.00,2026-07-05,Venmo,2026-07-15,Warm lighting excellent; all 5 images pass resolution and color checks
Jordan Kim,Photographer,Session 2 — 5 images Immunity,2026-07-12,,NOT STARTED,Milestone 3 (25%),2026-07-12,$350.00,,Venmo,2026-07-25,
Jordan Kim,Photographer,Session 3 — 5 images Digestive + final handoff,2026-07-24,,NOT STARTED,Milestone 4 (25%),2026-07-24,$350.00,,Venmo,2026-08-08,
Marcus Webb,Writer 1,Deposit — contract signature,2026-07-01,2026-07-01,APPROVED,Milestone 1 (25%),2026-07-01,$300.00,2026-07-01,PayPal,N/A (deposit),Contract signed 2026-07-01
Marcus Webb,Writer 1,Respiratory bundle — 3600 words,2026-07-08,,NOT STARTED,Milestone 2 (25%),2026-07-08,$300.00,,PayPal,2026-07-15,
Marcus Webb,Writer 1,Immunity bundle — 3800 words,2026-07-15,,NOT STARTED,Milestone 3 (25%),2026-07-15,$300.00,,PayPal,2026-07-25,
Marcus Webb,Writer 1,Digestive bundle + all revisions,2026-08-03,,NOT STARTED,Milestone 4 (25%),2026-08-03,$300.00,,PayPal,2026-08-10,
Jade Moreno,Writer 2,Deposit — contract signature,2026-07-01,2026-07-01,APPROVED,Milestone 1 (25%),2026-07-01,$200.00,2026-07-01,Zelle,N/A (deposit),Contract signed 2026-07-01
Jade Moreno,Writer 2,Respiratory recipes — 8-10 recipes,2026-07-08,,NOT STARTED,Milestone 2 (25%),2026-07-08,$200.00,,Zelle,2026-07-15,
Jade Moreno,Writer 2,Immunity recipes — 8-10 recipes,2026-07-15,,NOT STARTED,Milestone 3 (25%),2026-07-15,$200.00,,Zelle,2026-07-25,
Jade Moreno,Writer 2,Digestive recipes + all revisions,2026-08-03,,NOT STARTED,Milestone 4 (25%),2026-08-03,$200.00,,Zelle,2026-08-10,
Dr. Adrian White,Writer 3 Clinical,Deposit — contract signature,2026-07-01,2026-07-01,APPROVED,Milestone 1 (25%),2026-07-01,$312.50,2026-07-01,PayPal,N/A (deposit),Contract signed 2026-07-01; FTC and CITES screening confirmed
Dr. Adrian White,Writer 3 Clinical,Respiratory clinical section,2026-07-08,,NOT STARTED,Milestone 2 (25%),2026-07-08,$312.50,,PayPal,2026-07-15,
Dr. Adrian White,Writer 3 Clinical,Immunity clinical section,2026-07-15,,NOT STARTED,Milestone 3 (25%),2026-07-15,$312.50,,PayPal,2026-07-25,
Dr. Adrian White,Writer 3 Clinical,Digestive clinical section + revisions,2026-08-03,,NOT STARTED,Milestone 4 (25%),2026-08-03,$312.50,,PayPal,2026-08-10,
Rebecca Lexa,Herbalist Consultant,Deposit — contract signature,2026-07-01,2026-07-01,APPROVED,Milestone 1 (33%),2026-07-01,$200.00,2026-07-01,PayPal,N/A,Contract signed 2026-07-01; AHG credentials verified
Rebecca Lexa,Herbalist Consultant,Respiratory + Immunity reviews,2026-07-15,,NOT STARTED,Milestone 2 (33%),2026-07-15,$200.00,,PayPal,N/A,
Rebecca Lexa,Herbalist Consultant,Digestive review + consolidated feedback,2026-08-03,,NOT STARTED,Milestone 3 (34%),2026-08-03,$204.00,,PayPal,N/A,
Elena Rodriguez,Coordinator,Deposit — contract signature,2026-07-01,2026-07-01,APPROVED,Milestone 1 (25%),2026-07-01,$400.00,2026-07-01,Venmo,N/A,Contract signed 2026-07-01; Kit and Etsy access confirmed
Elena Rodriguez,Coordinator,Weeks 1-2 check-ins + Etsy coordination,2026-07-12,,NOT STARTED,Milestone 2 (25%),2026-07-12,$400.00,,Venmo,N/A,
Elena Rodriguez,Coordinator,Weeks 3-4 check-ins + email campaigns,2026-07-26,,NOT STARTED,Milestone 3 (25%),2026-07-26,$400.00,,Venmo,N/A,
Elena Rodriguez,Coordinator,Weeks 5-6 + final handoff,2026-08-10,,NOT STARTED,Milestone 4 (25%),2026-08-10,$400.00,,Venmo,N/A,
```

---

## Summary Sheet Template (Sheet 2)

Copy this table into Sheet 2 of your Google Sheets file. Update manually each week.

| Contractor | Role | Total Contract | Deposit Sent | M2 Paid | M3 Paid | M4 Paid | Total Paid | Outstanding | % Paid |
|---|---|---|---|---|---|---|---|---|---|
| [Name] | Photographer | $1,400 | | | | | $0 | $1,400 | 0% |
| [Name] | Writer 1 | $1,200 | | | | | $0 | $1,200 | 0% |
| [Name] | Writer 2 | $800 | | | | | $0 | $800 | 0% |
| [Name] | Writer 3 Clinical | $1,250 | | | | | $0 | $1,250 | 0% |
| [Name] | Herbalist Consultant | $604 | | | N/A | | $0 | $604 | 0% |
| [Name] | Coordinator | $1,600 | | | | | $0 | $1,600 | 0% |
| **TOTAL** | | **$6,854** | | | | | **$0** | **$6,854** | **0%** |

---

## FTC Disclosure Compliance Checkpoints

FTC disclosure compliance requires two separate actions: (1) correct evidence-tier language in the content before launch, and (2) confirmation that disclosures are present and accurate on live listings within 30 days of launch.

### Pre-Launch FTC Checkpoint (Before Each Bundle Goes Live on Etsy)

Run for each content bundle before the Etsy listing is published:

**Photographer images** (Respiratory, Immunity, Digestive):
- [ ] Images do not contain any text overlays making health claims
- [ ] Image captions or Etsy listing text credits photographer appropriately (if byline negotiated)
- [ ] No sponsored-content language required (photography is product imagery, not influencer content)

**Writer 1 manuscript** (Respiratory, Immunity, Digestive):
- [ ] Final pass confirms zero unqualified therapeutic claims ("prevents," "cures," "treats" without qualifier)
- [ ] All evidence-tier claims correctly framed ("Research suggests," "Traditionally used for," "May support")
- [ ] CITES Goldenseal sidebar present and verbatim in Immunity bundle
- [ ] All UpS At-Risk conservation flags present for Black Cohosh, Echinacea angustifolia
- [ ] Safety disclaimers present in bundle introduction

**Writer 2 recipes** (Respiratory, Immunity, Digestive):
- [ ] Safety disclaimer present on every recipe ("intended to support general wellness; not a substitute for professional medical advice")
- [ ] No unqualified efficacy claims in recipe introductions or headings
- [ ] Dosage guidance includes appropriate age qualifiers

**Writer 3 Clinical sections** (Respiratory, Immunity, Digestive):
- [ ] All drug interaction warnings present and evidence-cited
- [ ] Evidence grading present for all species
- [ ] Pregnancy and breastfeeding column complete for all species
- [ ] No unqualified efficacy claims in clinical sections

### Post-Launch FTC Checkpoint (30 Days After Each Bundle Launches)

| Bundle | Launch Date | 30-Day Check Date | Reviewer | Status |
|---|---|---|---|---|
| Respiratory | [TBD] | [Launch + 30 days] | User | [ ] |
| Immunity | [TBD] | [Launch + 30 days] | User | [ ] |
| Digestive | [TBD] | [Launch + 30 days] | User | [ ] |

**30-Day review actions**:
- [ ] Check Etsy listing description for any therapeutic claims that evolved during the launch period (social media comments, customer Q&A responses)
- [ ] Confirm Etsy listing still includes educational disclaimer (if included at launch)
- [ ] Confirm any social media posts using bundle content include appropriate FTC language (#ad if paid promotion, source attributions for claims)
- [ ] Log review completion date in Notes column of tracking sheet

---

## Weekly Update Protocol

**Every Monday (9am ET)**:

1. Open tracking sheet (Sheet 1)
2. For each contractor with active deliverables in the current week:
   - Check shared drive and email for new deliveries
   - If delivered: Update "Delivered Date [ACTUAL]" and set Review Status to "PENDING"
   - Review within 24 hours per quality gate checklist (PHASE_3_CONTRACTOR_ONBOARDING_CHECKLIST.md)
   - Update Review Status to "APPROVED" or "REVISION REQUESTED"
   - If approved: Dispatch payment same day; update "Payment Sent Date [ACTUAL]"
3. Update Summary Sheet (Sheet 2) totals
4. Share updated sheet with Coordinator
5. Archive weekly snapshot: File > Download > CSV; rename "Phase3-Tracking-YYYY-MM-DD.csv"; save to project archive

---

## Payment Reconciliation Checklist

**End of each week**:
- [ ] Total amount sent matches sum of all "Payment Sent Date [ACTUAL]" entries in tracking sheet
- [ ] Cross-reference against Venmo, PayPal, Zelle, or bank statement
- [ ] Flag any discrepancies (duplicate payment, wrong amount, missed milestone)
- [ ] Confirm all receipts or confirmation numbers are logged in Notes column

**End of project (August 10)**:
- [ ] Total paid across all contractors: $__________
- [ ] Matches total contract budget (±10% variance acceptable; flag if outside this range)
- [ ] All "Review Status" cells show APPROVED or APPROVED AFTER REVISION (no PENDING)
- [ ] All FTC Disclosure Dates populated for content roles (Photographer, Writer 1, Writer 2, Writer 3)
- [ ] Archive final sheet: "Phase3-Contractor-Tracking-FINAL-2026-08-10.csv"

---

## Budget Alert Triggers

Log in WORKLOG.md and pause before acting if any of the following occur:

| Trigger | Threshold | Action |
|---|---|---|
| Any single contractor exceeds contracted rate | More than 10% over | Hold; do not pay; review scope before approving |
| Total contractor spend approaches | $6,000 | Review remaining milestones; confirm budget headroom |
| Contractor requests scope expansion mid-sprint | Any amount | Hold; log; confirm budget before agreeing |
| Payment sent to wrong contractor or wrong method | Any | Contact payment platform; document in Notes; escalate |

---

## Notes for User

- Replace all [Name] and $[amount] placeholders with actual contractor names and rates after hiring is complete
- Keep original signed contracts separate from this spreadsheet — the spreadsheet is a tracking tool, not a legal document
- Payment proof: Keep screenshots or export confirmations from Venmo, PayPal, Zelle for all transactions; log confirmation numbers in Notes column
- If using Upwork for any contractor, Upwork escrow handles payment — adjust milestone labels accordingly ("Upwork milestone 1" vs. direct Venmo milestone)
- FTC compliance is the user's legal responsibility; this sheet provides checkpoints, not legal counsel

*Prepared: June 29, 2026. Activate on first contract signature. Update weekly every Monday. Archive final version August 10, 2026.*
