---
title: "Contractor Payment and Deliverable Tracker — Q3 Launch (Item 46)"
date: 2026-06-29
version: 1.0
status: production-ready
sprint-window: July 5 – August 17, 2026
instructions: >
  Import the CSV section below into Google Sheets (paste into cell A1; use
  Data > Split text to columns, delimiter comma). Update every Monday morning
  before sending check-in emails. One row per deliverable milestone.
  Do not leave cells blank if work is pending — use "PENDING" or "NOT STARTED"
  so blanks always mean "data missing."
cross-references:
  - CONTRACTOR_SELECTION_TIMELINE_AND_RUBRIC.md (hire timeline, final roster)
  - CONTRACTOR_ONBOARDING_CHECKLIST.md (payment triggers, milestone definitions)
  - CONTRACTOR_COMMUNICATION_TEMPLATES.md (payment notification templates)
  - CONTRACTOR_DROPOUT_CONTINGENCY_ACTIVATION.md (contingency row instructions)
---

# Contractor Payment and Deliverable Tracker — Q3 Launch

**Purpose**: Single source of truth for all 6 contractors' deliverables, approval status, and payment milestones. Update weekly (Monday 9am ET). Share with Logistics Coordinator for weekly check-in execution.

**Payment structure summary**:
- Photographer: 50% on hire / 50% on final image set approved
- Writers: 50% on hire / 50% on final manuscript approved after revisions
- Herbalist: 33% on hire / 33% on first two reviews approved / 34% on final review complete
- Coordinator: 50% on hire / 50% on project close
- Social Media Manager: 50% on hire / 50% on project close

**Upwork fee note**: Posted rates are gross amounts. Contractors net approximately 80% after Upwork's service fee (20% on first $500 with a new client). The amounts in this tracker reflect the gross amount you pay — Upwork handles the fee deduction on the contractor's end.

**FTC disclosure tracking**: All photographer and writer deliverables that go live on Etsy or in email campaigns require a post-launch FTC disclosure date logged. Internal-only roles (Herbalist, Coordinator) are N/A.

---

## Google Sheets Setup Instructions

1. Copy the CSV block below (from the header row through the last data row, including all blank cells)
2. Open Google Sheets → New spreadsheet
3. Name: `Seedwarden Q3 Contractor Tracking`
4. Click cell A1 → Paste
5. Select column A through column M → Data → Split text to columns → delimiter: Comma
6. Bold the header row; set header background to light gray (#f3f3f3)
7. Set column widths: A=150px, B=120px, C=200px, D=100px, E=100px, F=150px, G=120px, H=100px, I=80px, J=100px, K=100px, L=120px, M=200px
8. Add dropdown validation to column F (Review Status): NOT STARTED, PENDING, APPROVED, REVISION REQUESTED, REVISION SUBMITTED, APPROVED (AFTER REVISION)
9. Share with Logistics Coordinator (Editor access); share with you (Owner)
10. Enable notification on any edit to column F (to track status changes in real time)

---

## CSV Template

```csv
Contractor Name,Role,Deliverable,Deliverable Due Date,Delivered Date (ACTUAL),Review Status,Payment Milestone,Payment Due Date,Amount Due (Gross),Payment Sent Date (ACTUAL),Payment Method,FTC Disclosure Date (Post-Launch),Notes
[Name],Photographer,"Women's Health images — 5 images (lemon balm / red clover / damiana flat-lay)",2026-07-07,,NOT STARTED,Milestone 1 — 50% (on hire),2026-07-05,$700.00,,,[FTC: goes live July 6 Etsy upload],
[Name],Photographer,"Respiratory images — 5 images (elderberry / mullein / echinacea / thyme flat-lay)",2026-07-14,,NOT STARTED,Milestone 2 — included in 50% final,[On final approval],$0.00,,,N/A — interim deliverable,
[Name],Photographer,"Sleep & Nervines images — 5 images (valerian / passionflower / lemon balm / lavender)",2026-07-21,,NOT STARTED,Milestone 2 — included in 50% final,[On final approval],$0.00,,,N/A — interim deliverable,
[Name],Photographer,"Immunity Support images — 5 images (echinacea / ashwagandha / elderberry / goldenseal); CITES-compliant goldenseal props required",2026-07-28,,NOT STARTED,Milestone 2 — 50% (all 20 images approved),2026-07-28,$700.00,,,[FTC: goes live July 27 Etsy upload],
[Name],Women's Health Writer,"Women's Health manuscript draft — 3600-3800 words (lemon balm / red clover / damiana); damiana limited-evidence statement required",2026-07-21,,NOT STARTED,Milestone 1 — 50% (on hire),2026-07-05,$475.00,,,N/A — interim milestone,
[Name],Women's Health Writer,"Women's Health manuscript — final approved after revisions; all FTC language confirmed; contraindication table complete",2026-07-26,,NOT STARTED,Milestone 2 — 50% (on final approval),2026-07-26,$475.00,,,[FTC: goes live June 29 Etsy listing],
[Name],Respiratory & Sleep Writer,"Respiratory Health manuscript draft — 3200-3500 words (elderberry / mullein / echinacea / thyme); echinacea At-Risk flag required; elderberry toxicity warning required",2026-07-17,,NOT STARTED,Milestone 1 — 33% (on hire),2026-07-05,$347.00,,,N/A — interim milestone,
[Name],Respiratory & Sleep Writer,"Respiratory Health manuscript — approved after revisions",2026-07-21,,NOT STARTED,Milestone 2 — 33% (Respiratory approved),2026-07-21,$347.00,,,[FTC: goes live July 6 Etsy listing],
[Name],Respiratory & Sleep Writer,"Sleep & Nervines manuscript draft — 3200-3500 words (valerian / passionflower / lemon balm / lavender); valerian CNS interaction required; passionflower MAOI required",2026-07-28,,NOT STARTED,Milestone 2 — included above,,,$0.00,,,N/A — interim,
[Name],Respiratory & Sleep Writer,"Sleep & Nervines manuscript — final approved; all revisions complete",2026-08-07,,NOT STARTED,Milestone 3 — 34% (final approval),2026-08-07,$356.00,,,[FTC: goes live July 13 Etsy listing],
[Name],Herbalist Consultant,"Women's Health review notes — 1500-2500 words; lemon balm TSH flag; damiana interaction; phytoestrogen framing",2026-07-11,,NOT STARTED,Milestone 1 — 33% (on hire),2026-07-05,$280.00,,,N/A — internal review,
[Name],Herbalist Consultant,"Respiratory Health review notes — echinacea two-species distinction; elderberry sambunigrin; echinacea autoimmune contraindication",2026-07-18,,NOT STARTED,Milestone 2 — 33% (first two reviews approved),2026-07-21,$280.00,,,N/A — internal review,
[Name],Herbalist Consultant,"Sleep & Nervines review notes — valerian CNS depressant list; passionflower MAOI/SSRI; lavender Silexan distinction",2026-07-25,,NOT STARTED,Milestone 2 — included above,,,N/A,,,N/A — internal review,
[Name],Herbalist Consultant,"Immunity Support review notes — ashwagandha thyroid interaction; goldenseal CITES confirmation; goldenseal CYP450 interactions",2026-08-07,,NOT STARTED,Milestone 3 — 34% (all reviews complete),2026-08-14,$290.00,,,N/A — internal review,
[Name],Logistics Coordinator,"Week 1 status report — all 5 contractor check-ins sent; delays flagged; tracker updated",2026-07-08,,NOT STARTED,Milestone 1 — 50% (on hire),2026-07-05,$450.00,,,N/A — internal,
[Name],Logistics Coordinator,"Project close — all bundles live; final tracker updated; all check-in emails sent through Aug 17",2026-08-17,,NOT STARTED,Milestone 2 — 50% (project close),2026-08-17,$450.00,,,N/A — internal,
[Name],Social Media Manager,"Week 1 — 5-7 posts live across Instagram / Pinterest / Facebook; FTC-compliant captions; no unqualified health claims",2026-07-11,,NOT STARTED,Milestone 1 — 50% (on hire + Week 1 complete),2026-07-11,$400.00,,,N/A — disclosure embedded in posts,
[Name],Social Media Manager,"Project close — all 4 launch weeks complete; final metrics delivered; all posts archived",2026-08-17,,NOT STARTED,Milestone 2 — 50% (project close),2026-08-17,$400.00,,,N/A — disclosure embedded in posts,
[CONTINGENCY],Contingency / Backup Contractor,"Fallback activation — add row if any primary contractor is replaced; log replacement date and reason",,,,,,,,,Solo fallback content from Q3_MEDICINAL_BUNDLES_COMPLETION_TRACKER.md activates if <5 contractors deliver by bundle upload date
```

---

## Column Definitions

### Contractor Name
Format: First Last (exactly as on signed contract). Fill once at hire.

### Role
Select from: Photographer / Women's Health Writer / Respiratory & Sleep Writer / Herbalist Consultant / Logistics Coordinator / Social Media Manager / Contingency

### Deliverable
Human-readable description. Include: what it is, approximate scope, any mandatory content requirements. One row per milestone, not one row per week.

### Deliverable Due Date
Format: YYYY-MM-DD. Set from contract. No "end of week" language — use explicit dates.

### Delivered Date (ACTUAL)
Format: YYYY-MM-DD. Fill on the day delivery arrives (email received, file in Drive, etc.). Leave blank if not yet delivered. Annotate [EARLY] or [LATE — X days] if notable.

### Review Status
Options (use as dropdown):
- NOT STARTED: Work not yet due or received
- PENDING: Received; under review
- APPROVED: Passed quality gate; payment can release
- REVISION REQUESTED: Specific feedback sent; waiting for resubmission
- REVISION SUBMITTED: Contractor resubmitted; under second review
- APPROVED (AFTER REVISION): Revision passed; payment can release

Update within 24 hours of delivery. Never leave PENDING for more than 48 hours.

### Payment Milestone
Label: "Milestone 1 — [%] (trigger)" (e.g., "Milestone 1 — 50% (on hire)"). Fill once at contract. Update to "PAID" when payment confirmed.

### Payment Due Date
Format: YYYY-MM-DD. Set from contract. Same day as approval trigger where possible.

### Amount Due (Gross)
Dollar amount for this milestone. Gross (before Upwork fee deduction on contractor's end). Sum of all milestones = total contract value.

### Payment Sent Date (ACTUAL)
Format: YYYY-MM-DD. Fill when you initiate payment (Venmo send, PayPal transaction, bank transfer). Do not wait for contractor receipt confirmation to log this.

### Payment Method
Options: Upwork / Venmo / PayPal / Zelle / ACH / Wire. One method per contractor for all milestones.

### FTC Disclosure Date (Post-Launch)
Format: YYYY-MM-DD (date content goes live on Etsy or email). Enter "N/A" for internal-only roles (Herbalist, Coordinator). Fill after each bundle goes live. Used for 30-day FTC compliance review.

### Notes
Free text. 1–3 sentences. Log: quality issues, revision details, late delivery reason, any exceptions to standard process. Examples:
- "Draft 1 approved without revision; ahead of schedule; strong lemon balm contraindication section"
- "Session 1 images: white balance issue on images 2–3; resubmitted July 8; approved July 8"
- "Late 1 day; contractor notified 2 days early; reason: shipping delay on props; no cascade impact"

---

## Weekly Update Protocol (Monday, 9:00am ET)

1. Open spreadsheet
2. For each contractor with an active delivery window:
   - Check email and Google Drive for new submissions
   - If received: fill "Delivered Date (ACTUAL)"; set "Review Status" to PENDING
   - Review within 48 hours; update "Review Status" to APPROVED or REVISION REQUESTED
   - If approved: set "Payment Due Date" (same day); confirm payment sent; fill "Payment Sent Date"
   - Fill Notes column with any context
3. Send updated spreadsheet link to Logistics Coordinator for Monday check-in
4. Archive previous week's version (File > Download > XLSX; save as `Q3_Contractor_Tracking_YYYY-MM-DD.xlsx`)

---

## FTC Disclosure Checkpoints (Post-Launch)

At the time each bundle goes live on Etsy or in an email campaign, complete the following:

**Photographer**:
- [ ] All images are original work — no third-party copyright images incorporated without license
- [ ] If stock images or reference images were used in prop styling: confirm no copyright concerns
- [ ] Model release on file for any person visible in images: yes / N/A
- [ ] Images confirmed copyright-cleared for commercial use: confirmed by [DATE]

**Writers (Women's Health, Respiratory & Sleep)**:
- [ ] All therapeutic claims use evidence-tier framing — no unqualified "cures/prevents/treats" language: confirmed by [DATE]
- [ ] Contraindication sections present and accurate: herbalist review signed off on [DATE]
- [ ] No endangered species recommended for wild-harvest: confirmed by [DATE]
- [ ] Goldenseal sourcing language specifies cultivated-only: confirmed by [DATE]
- [ ] Damiana section includes explicit limited-evidence statement: confirmed by [DATE]

**Social Media Manager**:
- [ ] #ad on all sponsored or affiliate promotional posts: confirmed by [DATE]
- [ ] No posts recommend wild-harvest of any At-Risk or CITES-listed species: confirmed by [DATE]
- [ ] No unqualified health claims in any published caption: spot-checked and confirmed by [DATE]

**Herbalist Consultant**:
- [ ] Review notes confirm no claims in the manuscript exceed documented evidence: signed off on [DATE]
- [ ] CITES language for goldenseal reviewed and confirmed: signed off on [DATE]

---

## Status Dashboard (Second Sheet — Optional)

Create a second Google Sheets tab called "Status Summary" with this structure:

| Contractor | Role | Total Contract (Gross) | Total Paid | M1 | M2 | M3 | M4 | % Complete |
|---|---|---|---|---|---|---|---|---|
| [Name] | Photographer | $1,400 | | NOT PAID | NOT PAID | — | — | 0% |
| [Name] | Women's Health Writer | $950 | | NOT PAID | NOT PAID | — | — | 0% |
| [Name] | Resp. & Sleep Writer | $1,050 | | NOT PAID | NOT PAID | NOT PAID | — | 0% |
| [Name] | Herbalist Consultant | $850 | | NOT PAID | NOT PAID | NOT PAID | — | 0% |
| [Name] | Logistics Coordinator | $900 | | NOT PAID | NOT PAID | — | — | 0% |
| [Name] | Social Media Manager | $800 | | NOT PAID | NOT PAID | — | — | 0% |
| **TOTAL** | — | **$5,950** | **$0** | — | — | — | — | **0%** |

Update "Total Paid" by summing the "Payment Sent Date (ACTUAL)" rows that have been filled. Update M1/M2/M3/M4 status to "PAID [date]" as payments confirm.

**Total Q3 contractor budget: $5,950 gross**. Net cost to project after Upwork fee deductions on contractor side is $5,950 (you pay the gross; Upwork deducts their fee from the contractor's payout — your cost does not change).

---

## Contingency Row

If any primary contractor is replaced, add a row immediately below their last row:

Format: `[Backup Name], [BACKUP — replaces ORIGINAL NAME], [same deliverable description], [original due date], [actual delivery date], ...`

Note in the Notes column: `Activated [DATE] — [reason: dropout / quality failure / unavailability]. Primary contractor paid $[X] for work completed before replacement. Backup contractor rate $[Y] for remaining scope.`

Contingency pool reference: See CONTRACTOR_DROPOUT_CONTINGENCY_ACTIVATION.md for the full activation sequence and backup contact list.

Fallback content: If fewer than 5 contractors are delivering on schedule and a bundle upload date is at risk, activate solo fallback content from Q3_MEDICINAL_BUNDLES_COMPLETION_TRACKER.md. Note activation in tracker.

---

## Archival and Records

End of project (August 17, 2026):
- [ ] All milestone rows have "Payment Sent Date (ACTUAL)" filled
- [ ] All rows show APPROVED or APPROVED (AFTER REVISION) in Review Status
- [ ] Status Dashboard shows 100% for all contractors
- [ ] Final file saved as: `Q3_Contractor_Tracking_FINAL_2026-08-17.xlsx`
- [ ] One copy stored in: `Google Drive > Seedwarden > Operations > Q3 2026 > Contractor Records`
- [ ] All signed contracts, payment receipts, and model releases (if any) archived in same folder
