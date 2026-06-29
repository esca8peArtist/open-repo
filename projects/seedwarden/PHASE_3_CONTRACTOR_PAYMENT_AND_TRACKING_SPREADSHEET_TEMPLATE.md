---
title: "Phase 3 Contractor Payment and Tracking Spreadsheet Template"
date: 2026-06-29
version: 1.0
status: production-ready
format: CSV (import to Google Sheets, Excel, or Airtable)
sprint-window: June 29 – August 10, 2026
instructions: |
  1. Copy the CSV table below
  2. Paste into Google Sheets or Excel
  3. Add new rows for each contractor (photographer, writers, specialists, coordinator)
  4. Update weekly as deliverables are received and payments are made
  5. Use for tracking deliverable dates, payment status, approvals, and FTC compliance
cross-references:
  - PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md (summary metrics per contractor)
  - PHASE_3_CONTRACTOR_ONBOARDING_CHECKLIST.md (payment schedule details)
  - PHASE_3_CONTRACTOR_COMMUNICATION_TEMPLATES.md (payment notification templates)
---

# Phase 3 Contractor Payment and Tracking Spreadsheet Template

**Purpose**: Track all contractor deliverables, payments, and approvals in a single, updatable spreadsheet. Update weekly (Mondays) with delivery status, quality gate results, and payment confirmations.

**Columns explained**:
- **Contractor Name**: Full name (as listed on contract)
- **Role**: Photographer / Writer #1 / Writer #2 / Herbalist / Coordinator
- **Weekly Deliverables**: What they're delivering (Session 1 images, Respiratory draft, etc.)
- **Deliverable Due Date**: When item is due (week-by-week, explicit dates)
- **Delivered Date [ACTUAL]**: When contractor actually submitted (update on receipt)
- **Review Status**: PENDING / APPROVED / REVISION REQUESTED / REVISION SUBMITTED / APPROVED
- **Payment Milestone**: Milestone 1–4 (25% increments, except coordinator who may be hourly)
- **Payment Due Date**: When payment is due per contract terms (typically same day as approval)
- **Amount Due**: $ (25% of total contract, varies by contractor)
- **Payment Sent Date [ACTUAL]**: When you sent payment (update on dispatch)
- **Payment Method**: Venmo / PayPal / Zelle / ACH / Other
- **FTC Disclosure Date**: When content goes live (use for post-launch compliance tracking)
- **Notes**: Any revisions, delays, quality issues, or contractor communication

---

## CSV Template (Ready to Import)

```csv
Contractor Name,Role,Weekly Deliverables,Deliverable Due Date,Delivered Date [ACTUAL],Review Status,Payment Milestone,Payment Due Date,Amount Due,Payment Sent Date [ACTUAL],Payment Method,FTC Disclosure Date [POST-LAUNCH],Notes
[Name],Photographer,Session 1 (5 images - Respiratory),2026-07-05,,,Milestone 1 (25%),2026-07-05,$375.00,,Venmo,,
[Name],Photographer,Session 2 (5 images - Immunity),2026-07-12,,,Milestone 2 (25%),2026-07-12,$375.00,,Venmo,,
[Name],Photographer,Session 3 (5 images - Digestive),2026-07-24,,,Milestone 3 (25%),2026-07-24,$375.00,,Venmo,,
[Name],Photographer,Final handoff (all 15 images approved),2026-08-10,,,Milestone 4 (25%),2026-08-10,$375.00,,Venmo,,
[Name],Writer #1,Respiratory bundle (3600 words),2026-07-08,,,Milestone 1 (25%),2026-07-08,$337.50,,PayPal,,
[Name],Writer #1,Immunity bundle (3800 words),2026-07-15,,,Milestone 2 (25%),2026-07-15,$337.50,,PayPal,,
[Name],Writer #1,Digestive bundle + revisions (3600 words),2026-08-03,,,Milestone 3 (25%),2026-08-03,$337.50,,PayPal,,
[Name],Writer #1,Final approval (all bundles clean),2026-08-10,,,Milestone 4 (25%),2026-08-10,$337.50,,PayPal,,
[Name],Writer #2,Respiratory recipes (8-10 recipes),2026-07-08,,,Milestone 1 (25%),2026-07-08,$150.00,,Zelle,,
[Name],Writer #2,Immunity recipes (8-10 recipes),2026-07-15,,,Milestone 2 (25%),2026-07-15,$150.00,,Zelle,,
[Name],Writer #2,Digestive recipes + revisions (8-10 recipes),2026-08-03,,,Milestone 3 (25%),2026-08-03,$150.00,,Zelle,,
[Name],Writer #2,Final approval (all recipes clean),2026-08-10,,,Milestone 4 (25%),2026-08-10,$150.00,,Zelle,,
[Name],Herbalist,Respiratory + Immunity review (3000-5000 words),2026-07-15,,,Milestone 1 (33%),2026-07-15,$200.00,,PayPal,,
[Name],Herbalist,Digestive review + consolidated feedback (2000-3000 words),2026-08-03,,,Milestone 2 (33%),2026-08-03,$200.00,,PayPal,,
[Name],Herbalist,Final sign-off (all reviews complete),2026-08-10,,,Milestone 3 (34%),2026-08-10,$200.00,,PayPal,,
[Name],Coordinator,Weekly check-ins (Week 1-6),2026-08-10,,,Weekly Payment,2026-08-10,$1600.00,,Venmo,,
```

---

## Example Rows (Pre-Populated Sample Contractors)

```csv
Contractor Name,Role,Weekly Deliverables,Deliverable Due Date,Delivered Date [ACTUAL],Review Status,Payment Milestone,Payment Due Date,Amount Due,Payment Sent Date [ACTUAL],Payment Method,FTC Disclosure Date [POST-LAUNCH],Notes
"Sarah Chen",Photographer,"Session 1 (5 images - Respiratory)",2026-07-05,2026-07-05,APPROVED,Milestone 1 (25%),2026-07-05,$350.00,2026-07-05,Venmo,2026-07-15,"Warm lighting excellent; one image slightly soft focus but within acceptable range"
"Sarah Chen",Photographer,"Session 2 (5 images - Immunity)",2026-07-12,2026-07-12,APPROVED,Milestone 2 (25%),2026-07-12,$350.00,2026-07-12,Venmo,2026-07-25,"Color consistency perfect; style matches reference aesthetic"
"Sarah Chen",Photographer,"Session 3 (5 images - Digestive)",2026-07-24,2026-07-25,REVISION REQUESTED,Milestone 3 (25%),2026-07-26,$350.00,,Venmo,2026-08-08,"Two images have cold color cast; resubmitted for white balance correction. Revision approved 2026-07-26."
"Sarah Chen",Photographer,"Final handoff (all 15 images approved)",2026-08-10,2026-08-10,APPROVED,Milestone 4 (25%),2026-08-10,$350.00,2026-08-10,Venmo,2026-08-15,"All 15 images in Canva folders; attribution log complete"
"Marcus Webb",Writer #1,"Respiratory bundle (3600 words)",2026-07-08,2026-07-08,APPROVED,Milestone 1 (25%),2026-07-08,$300.00,2026-07-08,PayPal,2026-07-15,"Strong herbalism knowledge; all species + contraindications present; FTC language clean"
"Marcus Webb",Writer #1,"Immunity bundle (3800 words)",2026-07-15,2026-07-15,REVISION REQUESTED,Milestone 2 (25%),2026-07-16,$300.00,,PayPal,2026-07-25,"Goldenseal CITES sidebar needs minor expansion; revised and approved 2026-07-16"
"Marcus Webb",Writer #1,"Digestive bundle + revisions (3600 words)",2026-08-03,2026-08-03,APPROVED,Milestone 3 (25%),2026-08-03,$300.00,2026-08-03,PayPal,2026-08-10,"Final revision notes incorporated; all herbalist feedback addressed; clean for launch"
"Marcus Webb",Writer #1,"Final approval (all bundles clean)",2026-08-10,2026-08-10,APPROVED,Milestone 4 (25%),2026-08-10,$300.00,2026-08-10,PayPal,2026-08-15,"Deliverables archived; contract closed"
"Jade Moreno",Writer #2,"Respiratory recipes (8-10 recipes)",2026-07-08,2026-07-08,APPROVED,Milestone 1 (25%),2026-07-08,$200.00,2026-07-08,Zelle,2026-07-15,"10 recipes delivered; all have metric + US measurements; tone is encouraging; dosage present"
"Jade Moreno",Writer #2,"Immunity recipes (8-10 recipes)",2026-07-15,2026-07-15,APPROVED,Milestone 2 (25%),2026-07-15,$200.00,2026-07-15,Zelle,2026-07-25,"9 recipes; includes elder syrup + tincture focus; age-appropriate dosing noted"
"Jade Moreno",Writer #2,"Digestive recipes + revisions (8-10 recipes)",2026-08-03,2026-08-03,APPROVED,Milestone 3 (25%),2026-08-03,$200.00,2026-08-03,Zelle,2026-08-10,"10 recipes; fermented tonics included; all revisions on tone and sourcing implemented"
"Jade Moreno",Writer #2,"Final approval (all recipes clean)",2026-08-10,2026-08-10,APPROVED,Milestone 4 (25%),2026-08-10,$200.00,2026-08-10,Zelle,2026-08-15,"Deliverables archived"
"Dr. Adrian White",Herbalist,"Respiratory + Immunity review (3000-5000 words)",2026-07-15,2026-07-15,APPROVED,Milestone 1 (33%),2026-07-15,$266.67,2026-07-15,PayPal,N/A,"Detailed review notes; flagged Ashwagandha + benzodiazepine interaction; CITES language verified"
"Dr. Adrian White",Herbalist,"Digestive review + consolidated feedback (2000-3000 words)",2026-08-03,2026-08-03,APPROVED,Milestone 2 (33%),2026-08-03,$266.67,2026-08-03,PayPal,N/A,"Final review complete; all conservation flags addressed; turmeric bioavailability note added"
"Dr. Adrian White",Herbalist,"Final sign-off (all reviews complete)",2026-08-10,2026-08-10,APPROVED,Milestone 3 (34%),2026-08-10,$266.66,2026-08-10,PayPal,N/A,"Contract closed; feedback successfully integrated into all three bundles"
"Elena Rodriguez",Coordinator,"Weekly check-ins (Week 1-6)",2026-08-10,2026-08-10,APPROVED,Weekly Payment,2026-08-10,"$1,600.00",2026-08-10,Venmo,N/A,"6 weeks of Monday check-ins completed; dashboard updated weekly; no escalations needed; Etsy coordination smooth"
```

---

## Column Definitions & How to Use

### Contractor Name
**Format**: First Last  
**Update**: Once (at hire)  
**Notes**: Must match contract signature exactly for payment clarity

---

### Role
**Format**: Select one: Photographer / Writer #1 / Writer #2 / Herbalist / Coordinator  
**Update**: Once (at hire)  
**Notes**: Used for sorting and role-specific tracking

---

### Weekly Deliverables
**Format**: Human-readable description (e.g., "Session 1 (5 images - Respiratory)")  
**Update**: Once (at onboarding)  
**Notes**: One row per deliverable; allows granular tracking across 6 weeks

**Examples**:
- Photographer: "Session 1 (5 images)", "Session 2 (5 images)", "Session 3 (5 images)"
- Writer #1: "Respiratory draft (3600 words)", "Immunity draft (3800 words)", "Digestive draft + revisions"
- Writer #2: "Respiratory recipes (8-10)", "Immunity recipes (8-10)", "Digestive recipes (8-10)"
- Herbalist: "Respiratory + Immunity review", "Digestive review", "Final consolidation"
- Coordinator: "Weekly check-ins (Weeks 1-6)"

---

### Deliverable Due Date
**Format**: YYYY-MM-DD (e.g., 2026-07-05)  
**Update**: Once (at onboarding; per contract terms)  
**Notes**: Set explicit dates from contract; no ambiguous "end of week" language

**Typical schedule**:
- Photographer Session 1: Jul 5
- Writer #1 Respiratory: Jul 8
- Writer #2 Respiratory: Jul 8
- Photographer Session 2: Jul 12
- Writer #1 Immunity: Jul 15
- Writer #2 Immunity: Jul 15
- Herbalist reviews (Respiratory + Immunity): Jul 15
- Photographer Session 3: Jul 24
- Writer #1 Digestive + revisions: Aug 3
- Writer #2 Digestive + revisions: Aug 3
- Herbalist Digestive review: Aug 3
- Final approvals: Aug 10

---

### Delivered Date [ACTUAL]
**Format**: YYYY-MM-DD or empty if not yet delivered  
**Update**: Upon delivery (same day contractor submits)  
**Notes**: Leave blank until delivery; update when files arrive in shared folder or email

**Timing note**: If contractor delivers before due date, note [EARLY]. If late, note [LATE — by X days].

---

### Review Status
**Format**: Select from list:
- `NOT STARTED` — Work not yet received
- `PENDING` — Received; under review
- `APPROVED` — Passed quality gate; payment ready
- `REVISION REQUESTED` — Quality issues found; specific feedback sent
- `REVISION SUBMITTED` — Contractor resubmitted after revision request
- `APPROVED (after revision)` — Revision approved; payment ready

**Update**: After each quality gate review (typically within 24 hours of delivery)  
**Notes**: Update same day as delivery to maintain momentum

**Example progression**:
1. Jul 5: Photographer submits Session 1 → Status: `PENDING`
2. Jul 5 (4 hours later): You review → Status: `APPROVED` (if pass) or `REVISION REQUESTED` (if issues)
3. If revision: Jul 6 contractor resubmits → Status: `REVISION SUBMITTED`
4. Jul 6 (2 hours later): You review revision → Status: `APPROVED (after revision)`
5. Jul 6 (same day): Payment sent → Status: `APPROVED` (payment confirms)

---

### Payment Milestone
**Format**: "Milestone 1 (25%)" through "Milestone 4 (25%)"  
**Exception**: Coordinator may be "Weekly" or "Flat $[AMOUNT]"  
**Update**: Once (at contract) and update status column as paid

**Standard schedule** (all contractors except coordinator):
- Milestone 1 (25%): On contract signature
- Milestone 2 (25%): On first deliverable approval
- Milestone 3 (25%): On second/third deliverable approval (varies by role)
- Milestone 4 (25%): On final handoff and revisions complete

---

### Payment Due Date
**Format**: YYYY-MM-DD  
**Update**: Once (per contract terms)  
**Notes**: Typically same day as approval/milestone trigger

**Example** (Photographer):
- Milestone 1 due: 2026-07-01 (contract signature)
- Milestone 2 due: 2026-07-05 (Session 1 approval)
- Milestone 3 due: 2026-07-12 (Session 2 approval)
- Milestone 4 due: 2026-08-10 (final handoff)

---

### Amount Due
**Format**: $XXX.XX (25% of total contract, except herbalist/coordinator)  
**Update**: Once (at contract)  
**Notes**: Keep all milestone amounts visible for reconciliation

**Calculation**:
- If photographer contract is $1,400 total: Each milestone = $350
- If writer contract is $1,200 total: Each milestone = $300
- Herbalist (33/33/34 split) differs slightly on 4th milestone
- Coordinator: Either hourly ($40–60/hr × 40–50 hours) or flat ($1,600–2,000)

---

### Payment Sent Date [ACTUAL]
**Format**: YYYY-MM-DD or empty if not yet sent  
**Update**: On payment dispatch (same day as approval, per contract)  
**Notes**: This is confirmation of when you actually sent payment

**Important**: Do not wait for payment delivery confirmation; log when you initiate payment (Venmo send, PayPal transaction, bank transfer initiation).

---

### Payment Method
**Format**: Venmo / PayPal / Zelle / ACH / Wire / Other  
**Update**: Once (per contractor contract)  
**Notes**: Standardize per contractor (same method for all 4 milestones)

---

### FTC Disclosure Date [POST-LAUNCH]
**Format**: YYYY-MM-DD (date content goes live on Etsy/email/social) or "N/A" for internal roles (herbalist, coordinator)  
**Update**: Post-launch (after bundles are published)  
**Notes**: Used for FTC compliance tracking; all creator-generated content (photographer, writers) must have disclosure date logged

**FTC requirement**: 30 days post-launch, ensure all disclosures are present on live content (e.g., photographer byline, FTC language in email/Etsy descriptions).

---

### Notes
**Format**: Free text (1–3 sentences)  
**Update**: As needed (quality issues, revisions, delays, communication notes)  
**Examples**:
- "Session 1 approved with minor note: image 3 has slight color cast but within acceptable range"
- "Respiratory draft approved; herbalist review flagged Ashwagandha + benzodiazepine interaction; writer revising"
- "2 days late but quality excellent; approved for payment 2026-07-07"
- "Revision submitted; recheck color consistency across images; re-approved 2026-07-13"
- "Coordinator flagged Etsy upload on Jul 22; no blockers"

---

## Weekly Update Protocol

**Every Monday (9am ET)**:

1. [ ] Open spreadsheet
2. [ ] For each contractor with active delivery window:
   - [ ] Check for new deliverables (check email, shared drive, Upwork)
   - [ ] If delivered: Update "Delivered Date [ACTUAL]" and "Review Status" to "PENDING"
   - [ ] Review quality (use gates from PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md)
   - [ ] Update "Review Status" to "APPROVED" or "REVISION REQUESTED"
   - [ ] If approved: Update "Payment Sent Date [ACTUAL]" once payment is dispatched
3. [ ] Add weekly notes (any delays, escalations, communication)
4. [ ] Share updated version with Coordinator for Monday check-in email
5. [ ] Archive previous week's version (for audit trail)

---

## Reconciliation Checklist (Monthly)

**End of each week**:

- [ ] Total "Amount Due" for all milestones paid so far: $___________
- [ ] Match against actual Venmo/PayPal/bank statement history
- [ ] Flag any discrepancies (unpaid milestone, wrong amount, etc.)
- [ ] Confirm all "Payment Sent Date [ACTUAL]" entries have corresponding receipts

**End of project (Aug 10)**:

- [ ] Total paid to all contractors: $___________
- [ ] Verify against total contract budget
- [ ] All "Payment Sent Date [ACTUAL]" populated
- [ ] All "Review Status" shows "APPROVED" (no pending revisions)
- [ ] Archive final spreadsheet for records

---

## Backup / Archival

**Weekly backup**:
- [ ] Download as CSV or Excel file (File > Download)
- [ ] Save to shared drive with date stamp: `PHASE_3_Contractor_Tracking_YYYY-MM-DD.xlsx`
- [ ] Keep last 4 weeks of backups for audit trail

**End of project**:
- [ ] Final version saved with all milestone payments logged
- [ ] Filename: `PHASE_3_Contractor_Tracking_FINAL_2026-08-10.xlsx`
- [ ] Store in project archive folder

---

## Tips for Accuracy

1. **Don't leave cells blank unless pending**: Use "N/A" or "TBD" to distinguish "not yet known" from "empty by mistake"
2. **Update same day**: Review and log deliveries the day they arrive, not later in the week
3. **Use dates consistently**: Always YYYY-MM-DD format for sorting and clarity
4. **Notes capture context**: Brief note on every entry (why revision? why early? any issues?) helps future reference
5. **Payment confirmation**: Log only after you've initiated payment (Venmo send, PayPal transaction, etc.), not after contractor confirms receipt

---

## Import Instructions (Google Sheets)

1. Copy the CSV template above (from "Contractor Name" header through last data row)
2. Open Google Sheets → Create new spreadsheet
3. Name: `Phase 3 Contractor Payment & Tracking`
4. Paste CSV data into Sheet1, starting at cell A1
5. Format header row (bold, light gray background)
6. Set column widths: Contractor Name (20px), Role (12px), Deliverables (25px), Dates (15px), Status (18px), etc.
7. Share with read-only access to stakeholders (you, coordinator, optional: external advisor)
8. Enable comment notifications for tracking updates

---

## Import Instructions (Excel)

1. Copy CSV template
2. Open Excel → Paste Special → Text to Columns (Data tab)
3. Delimiter: Comma
4. Format as table (Insert → Table)
5. Add filters (Data → AutoFilter)
6. Save as `.xlsx` and share via OneDrive or email weekly

---

## Status Dashboard Summary (Optional)

If you prefer a high-level summary, create a second sheet (Status Summary) with:

| Contractor | Role | Total Contract | Total Paid | Milestone 1 | Milestone 2 | Milestone 3 | Milestone 4 | % Complete |
|---|---|---|---|---|---|---|---|---|
| Sarah Chen | Photographer | $1,400 | $1,400 | PAID | PAID | PAID | PAID | 100% |
| Marcus Webb | Writer #1 | $1,200 | $900 | PAID | PENDING | PENDING | PENDING | 25% |
| Jade Moreno | Writer #2 | $800 | $400 | PAID | PENDING | PENDING | PENDING | 50% |
| Dr. Adrian White | Herbalist | $800 | $533 | PAID | PAID | PENDING | — | 67% |
| Elena Rodriguez | Coordinator | $1,600 | $1,600 | PAID | PAID | PAID | PAID | 100% |
| **TOTAL** | — | **$5,800** | **$4,833** | — | — | — | — | **83%** |

This summary updates automatically if you use formulas to pull from the main tracking sheet.

---

## Notes for User

- **Keep original contract**: This spreadsheet is a tracking tool, not a legal document. Retain all signed contracts for reference.
- **Payment proof**: Keep receipts or screenshots of all Venmo, PayPal, bank transfer confirmations for audit trail.
- **Communication log**: Cross-reference this spreadsheet with PHASE_3_CONTRACTOR_COMMUNICATION_TEMPLATES.md (weekly check-ins, revision requests) for complete project record.
- **Contingency tracking**: If you activate a backup contractor, add a new row to the spreadsheet and note "BACKUP — replaced [original contractor name] on [date] due to [reason]"
