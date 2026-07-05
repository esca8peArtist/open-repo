---
title: "Phase 3 Contractor Operational Handbook — Sync, Attribution, Approval, Escalation"
date: 2026-07-04
version: 1.0
status: production-ready
sprint-window: July 12 – August 10, 2026
cross-references:
  - PHASE_3_CONTRACTOR_ONBOARDING_FINAL.md (onboarding checklist, escalation triggers)
  - PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md (tracking grid, budget)
  - PHASE_3_CONTRACTOR_COMMUNICATION_TEMPLATES.md (all email templates)
  - PHASE_3_CONTRACTOR_PAYMENT_TRACKING.md (payment milestones, FTC compliance log)
  - PHASE_3_LAUNCH_MARKETING_CALENDAR.md (bundle launch dates, email send dates)
  - assets/phase-3-medicinal-herbs/PHOTO_ATTRIBUTION_LOG.md (photo licensing records)
---

# Phase 3 Contractor Operational Handbook

**Purpose**: Defines how Seedwarden manages 6 active contractors day-to-day from contract signature through final handoff. Covers weekly sync schedule, communication protocols, photo attribution log maintenance, content approval workflow, and escalation procedures.

**Who uses this**: The user (project lead) and the logistics coordinator. Both should read this before Week 1 check-ins begin.

---

## 1. Weekly Sync Schedule

### Fixed Weekly Events

| Day | Time (ET) | Event | Who | Format |
|---|---|---|---|---|
| Monday | 9:00am | Coordinator sends weekly check-in email to all contractors | Coordinator | Async email — Template 2, PHASE_3_CONTRACTOR_COMMUNICATION_TEMPLATES.md |
| Tuesday | EOD (5pm) | Contractors reply to check-in with status update | Contractors | Email reply |
| Wednesday | 9:00am | Coordinator compiles and sends weekly status summary to project lead | Coordinator | Short email: one paragraph per contractor |
| Wednesday | 12:00pm | Project lead reviews summary and flags any escalation items | Project lead | Email to coordinator if action needed |
| Friday | varies | Bundle delivery or approval review window (typically the day deliverables arrive) | Project lead | Async review, reply same day |
| Friday | varies | Etsy listing uploads (once a bundle is fully approved) | Coordinator | Etsy upload per PHASE_3_LAUNCH_MARKETING_CALENDAR.md |

### Weekly Check-In Email Content

The coordinator sends Template 2 from PHASE_3_CONTRACTOR_COMMUNICATION_TEMPLATES.md to each contractor individually (not a group email). Fill in:
- Last week: what was expected vs. what was delivered (on-time / delivered [date] / not yet received)
- This week: primary deliverable due and due date
- Resources: link to relevant brief or reference doc in shared drive
- Blockers: open invitation to flag issues
- Payment status: current milestone status

Contractors are expected to reply by EOD Tuesday. If no reply by Tuesday 5pm ET, the coordinator sends a brief follow-up: "Hi [NAME], please send your status reply for this week's check-in when you have a moment today."

### Async Video Protocol

For complex feedback that would take more than one email to convey (e.g., a manuscript requires structural reorganization, or a photo session has aesthetic alignment issues), use async video:
- Record a 3–5 minute Loom or similar screencast walking through the specific issue
- Share the link in the feedback email alongside the written numbered points
- Do not require a video reply — contractors may respond via email
- Async video is especially useful for writer feedback (can show specific passages) and photographer feedback (can mark up images)

Use async video only when written feedback alone would be insufficient. Do not use it as a substitute for clearly numbered written feedback.

### Communication Channels by Purpose

| Channel | Use Case | Response Expectation |
|---|---|---|
| Email | All official communication: offers, contracts, check-ins, feedback, payment confirmations | 24-hour response during active weeks |
| Shared Drive | Deliverable delivery, file exchange, reference materials | No response required — just upload |
| DocuSign / HelloSign | Contract signature only | 24–48 hours from send |
| Loom (async video) | Complex feedback requiring visual walkthrough | Acknowledgment within 24 hours |
| Phone / Sync Call | Only for escalation issues that cannot be resolved asynchronously | Schedule same day if urgent |

Do not use Slack, Discord, or other real-time messaging platforms for this project unless the coordinator and project lead agree to add one. All deliverable-related communication must be in email for record-keeping.

---

## 2. Communication Protocols by Scenario

### New Deliverable Arrives

1. Coordinator logs receipt in PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md: received date, status (Received — Under Review).
2. Project lead reviews against quality gate checklist within 24 hours (photography) or 48 hours (manuscripts, clinical sections).
3. Project lead sends either:
   - Approval email: "Approved. Milestone [N] payment sent ($[AMOUNT])." — use Template 3A (praise) if quality exceeded expectations
   - Correction email: numbered list of specific issues, revision deadline, what is working well — use Template 3B
4. Coordinator updates dashboard: Review Status to Approved or Revision Requested.
5. If approved: Coordinator logs payment sent date in PHASE_3_CONTRACTOR_PAYMENT_TRACKING.md.

### Contractor Submits Revision

1. Project lead reviews revision within 24 hours.
2. If revision resolves all issues: send approval + payment.
3. If issues remain: send second correction email — shorter, focused only on unresolved items. Give a second 48-hour revision window.
4. If issues remain after second revision (third submission): project lead escalates — see Section 5 (Escalation Procedures).

### Contractor Asks a Question Outside Check-In

Respond within 24 hours. If the question requires a scope interpretation (e.g., "Should I cover Elderflower or only Elderberry?"), answer in writing so the response is on record. Log any scope decisions in WORKLOG.md.

### Contractor Flags a Blocker

A blocker is any issue the contractor cannot resolve without input from the project lead: missing reference documents, unclear deliverable spec, specimen logistics failure, database access problem.

Protocol:
1. Respond within 4 hours during weekdays (not 24 hours — blockers stall deliverables).
2. Resolve or provide a workaround. If the blocker cannot be resolved same day, give the contractor an explicit revised delivery date in writing.
3. Log the blocker in WORKLOG.md: date, contractor, issue, resolution, new delivery date if applicable.

---

## 3. Photo Attribution Log Maintenance

### Purpose

The Photo Attribution Log (`assets/phase-3-medicinal-herbs/PHOTO_ATTRIBUTION_LOG.md`) tracks licensing for all Wikimedia Commons, iNaturalist CC-BY, and direct-permission photos used in published guide PDFs. It is also the source of truth for the attribution page printed at the back of each bundle.

Phase 3 uses two categories of photos:
1. **Seedwarden-contracted photographer photos**: Owned outright under work-for-hire. No attribution page entry required for Etsy publication. Log in the dashboard as "Work-for-hire — no external attribution."
2. **Pre-staged Wikimedia / iNaturalist photos**: Previously sourced by agent sessions. These require attribution in the guide PDF. Attribution strings are pre-populated in PHOTO_ATTRIBUTION_LOG.md for most species.

### Coordinator Responsibilities for Attribution

Each Friday (when a bundle is approved and ready for Etsy upload):
- [ ] Open PHOTO_ATTRIBUTION_LOG.md and locate the species in the bundle being uploaded
- [ ] Verify every image used in that bundle has a confirmed row: Source URL, Photographer/Uploader, License, Attribution String — no blank fields
- [ ] For any blank field: hold the upload; alert project lead to complete the attribution before the listing goes live
- [ ] For contracted photographer images: log "Work-for-hire — Seedwarden, [DATE OF CONTRACT]" in the Attribution String field and "Owned" in the License field

### Attribution String Format (for PDF attribution page)

**Wikimedia Commons image**:
`Photo: [Photographer name or uploader username], Wikimedia Commons, [License]. URL: [full Commons file page URL]`

**iNaturalist image**:
`Photo: [Observer name], iNaturalist observation #[observation ID], [License]. URL: [full observation URL]`

**Contracted (work-for-hire)**:
`Photo: Seedwarden Phase 3 production, [year]. All rights reserved.`

**Direct permission**:
`Photo: [Photographer name], [Institution], used with written permission, [date received].`

### Pre-Staged Attribution Status (from prior agent sessions)

All 14 species in Bundles 1–5 have Wikimedia Commons habit image sources confirmed with license. The following items still require user verification before download or PDF inclusion:

| Species | Outstanding Action |
|---|---|
| Lavender | Verify Wikimedia File:Lavandula_angustifolia_002.JPG shows full shrub habit vs. inflorescence — check file page before download |
| Lemon Balm | Verify File:02014_Melissa_officinalis.JPG shows full bushy mound vs. close-up |
| Ashwagandha | Verify File:Withania_somnifera.jpg shows full plant habit vs. close-up |
| Passionflower flower | Verify license on file page for File:Passiflora_incarnata_flower.jpg before use |
| Echinacea angustifolia | USDA source is 330×220px — supplement with iNaturalist CC-BY image at higher resolution |
| Dandelion root | Root image not pre-staged — sourcing needed (see PHOTO_ATTRIBUTION_LOG.md Bundle 5) |
| Ginger rhizome | User must verify license on File:Zingiber_officinale_fresh_rhizome.JPG |

Once the contracted photographer delivers Session 1–3 images and they are approved, the contractor's images replace the pre-staged Wikimedia images for the production flat-lay and lifestyle shots. The Wikimedia botanical habit images remain in the body of the educational guide text.

---

## 4. Content Approval Workflow

### Who Reviews What

| Content Type | Primary Reviewer | Secondary Reviewer | Standard |
|---|---|---|---|
| Educational manuscript (Writer 1) | Project lead | Herbalist Consultant (after first draft) | Quality gate checklist, Section 2 of PHASE_3_CONTRACTOR_ONBOARDING_FINAL.md |
| Recipe sections (Writer 2) | Project lead | No secondary (recipe format is self-evident) | Quality gate checklist |
| Clinical sections (Writer 3) | Project lead | Herbalist Consultant (concurrent with manuscript review) | Evidence grading, mandatory warnings checklist |
| Photography (Photographer) | Project lead | No secondary | Visual and technical quality gate |
| Herbalist review notes | Project lead | No secondary | Completeness check only — content authority is the herbalist |
| Dashboard and logistics (Coordinator) | Project lead | No secondary — coordinator audits themselves via checklist | Weekly check-in confirms |

### Feedback Template Structure

All feedback emails follow this structure, whether praise or correction:

1. Open with one specific observation (positive or neutral) — e.g., "The Echinacea section handles the two-species distinction clearly."
2. Numbered list of issues to resolve (if any). Each issue: describe the exact problem, describe the exact fix.
3. What is working well (even in correction emails — acknowledge what landed).
4. Revision due date (48 hours for writers; 24 hours for photographers; none needed if approval).

Never use vague evaluations: "This isn't quite right" or "The tone is off" are not actionable. Name the specific sentence, section, image, or format element.

### Revision Cycle Limits

| Role | Maximum Revision Rounds Included | What Happens if Exceeded |
|---|---|---|
| Photographer | 2 reshoot requests per session | Third reshoot is billable at agreed per-session rate; negotiate in writing before authorizing |
| Writer 1 | 3 revision rounds per manuscript | Fourth round negotiated separately; reduce scope before adding rounds |
| Writer 2 | 2 revision rounds per recipe section | Third round negotiated |
| Writer 3 | 3 revision rounds per clinical section | Same as Writer 1 |
| Herbalist | No revision limit on review notes (notes are advisory, not creative) | N/A |

### FTC Pre-Approval Check (Pre-Etsy Upload Gate)

Before any bundle listing goes live on Etsy, the project lead must confirm:
- [ ] Educational manuscript: no unqualified claims ("prevents," "cures," "treats") remain
- [ ] Recipe section: FTC-compliant safety disclaimer present on every recipe
- [ ] Clinical section: all efficacy claims evidence-tier framed
- [ ] Herbalist flags: all flagged claims addressed in revision
- [ ] Etsy listing description: FDA disclaimer present ("This guide is for educational purposes. Statements have not been evaluated by the FDA. Not intended to diagnose, treat, cure, or prevent any disease.")
- [ ] Attribution log: complete, no blank fields for any image used in this bundle

Log the FTC pre-approval check date and confirmer in PHASE_3_CONTRACTOR_PAYMENT_TRACKING.md for each bundle before uploading.

### Bundle Upload Sequence

When a bundle is fully approved and FTC-checked:

1. Coordinator receives approval confirmation from project lead via email.
2. Coordinator prepares Etsy listing: title, description (from approved manuscript), images (from approved photography and pre-staged Wikimedia), price, tags, PDF file attached.
3. Coordinator previews the draft listing and sends screenshot to project lead for final visual check.
4. Project lead replies: "Approved to go live" or provides specific changes (do not upload without explicit approval).
5. Coordinator publishes listing and sends Etsy URL to project lead.
6. Project lead sends launch email via Kit (Template from PHASE_3_BUNDLE_LAUNCH_EMAIL_SEQUENCES.md) within 2 hours of listing going live.
7. Coordinator logs upload date in PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md.

Do not publish any listing without explicit written approval from the project lead. "Looks fine" is not sufficient — the explicit phrase "Approved to go live" is required.

---

## 5. Escalation Procedures

### Escalation Tiers

**Tier 1 — Coordinator handles, no project lead required**:
- Contractor replies to check-in 6–12 hours late (business hours)
- Deliverable arrives without a submission message (coordinator requests confirmation of FTC self-review)
- Minor shared drive access issue (wrong folder, missing permissions)

**Tier 2 — Coordinator alerts project lead within 2 hours**:
- Contractor 24+ hours late on any deliverable
- Deliverable fails a quality gate for the first time
- Contractor requests a scope change or rate adjustment
- Attribution log has a blank field blocking an upload

**Tier 3 — Project lead contacts contractor directly, same day**:
- Deliverable fails a quality gate for the second time on the same revision
- Contractor is unreachable for 24+ hours (no email reply, no shared drive activity)
- Contractor requests contract cancellation or discloses a personal conflict that threatens the timeline
- Contractor violates confidentiality (discussing project publicly before launch)

**Tier 4 — Terminate and activate contingency**:
- Contractor unreachable for 48+ hours with no resolution
- Second quality gate failure and contractor refuses to revise further
- Contractor discloses a material misrepresentation (false credential, plagiarized portfolio)
- Contractor violates FTC agreement in delivered content and refuses to remediate

### Tier 3–4 Escalation Scripts

**Tier 3 — Direct project lead contact (phone or email)**:

> "Hi [NAME], this is [YOUR NAME] from Seedwarden. I am reaching out directly because [SPECIFIC ISSUE — e.g., 'the revision on the Immunity manuscript has been outstanding for 72 hours' / 'you have not responded to the coordinator's check-in in 48 hours']. I need a status update today so I can protect the July [DATE] upload timeline. If there is a blocker I can help with, please let me know now. If I do not hear back by [TIME TODAY], I will need to make alternative arrangements. Thanks."

**Tier 4 — Termination email**:

> "Hi [NAME], I am ending our Phase 3 contract as of [DATE] due to [SPECIFIC REASON]. Under the terms of our agreement:
> - Milestones 1–[N] have been paid ($[AMOUNT] total). These are not subject to refund.
> - Milestone [N+1] (pending delivery of [DELIVERABLE]) will not be paid as that deliverable has not been received / has not passed quality review after two revision rounds.
> - All deliverables received to date remain property of Seedwarden.
> - Your confidentiality obligations remain in effect per the signed contract.
>
> I am sorry this did not work out. I wish you well."

Log termination in PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md. Immediately activate the Tier 2 or Tier 3 candidate from the application pool (PHASE_3_HIRING_SELECTION_FRAMEWORK.md Section 1, Contingency row).

### Contingency Coverage by Role

| Role | Primary Contingency | Secondary Contingency |
|---|---|---|
| Photographer | Tier 2 candidate from Upwork application pool | Post to Thumbtack; extend session timeline by 1 week |
| Writer 1 | Split educational content between remaining writers | Reduce scope: 6 species per bundle (not 7–8); reduce to 3,200 words |
| Writer 2 | Absorb recipes into Writer 1 scope (negotiate additional rate) | Reduce to 6 recipes per bundle |
| Writer 3 | Project lead completes clinical sections using NatMed Pro directly | External herbalist consultant takes on clinical review at expanded rate |
| Herbalist | Project lead reviews using NatMed Pro + UpS; defer to internal review | Defer herbalist review to post-launch (reduces pre-launch safety confidence) |
| Coordinator | Project lead absorbs check-ins and Etsy uploads; reduce email cadence | Post to Upwork for emergency coordinator (3-week contract, higher rate) |

### Conflict Resolution for Non-Escalation Disputes

If a contractor disputes a revision request ("I believe the Echinacea section is correct as written"):
1. Do not argue over email. Acknowledge their perspective: "I understand you have a different read on this. Let me explain the specific concern more precisely."
2. Cite the source of the standard being applied (e.g., "The NatMed Pro monograph on Echinacea angustifolia classifies the UpS At-Risk status as 'conservation concern' — this is why the sidebar language is required per our content brief").
3. If dispute continues: escalate to the herbalist consultant for binding adjudication. The herbalist's ruling on content accuracy disputes is final.
4. If the dispute is about format (not accuracy): project lead's determination is final. Log the decision in WORKLOG.md so it does not recur.

---

## 6. Dashboard Update Protocol

The coordinator updates PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md every Monday after receiving check-in replies, and immediately after any payment milestone event.

**Columns to update each Monday**:
- Weekly Progress Grid: status for the just-completed week (ON TRACK / AT RISK / BEHIND / DELIVERED / APPROVED)
- Any note about a delivery that was late, a quality gate pass/fail, or an escalation event

**Columns to update immediately on payment events**:
- Budget Tracking section: Milestone Paid [ACTUAL] for the relevant contractor, date, method

**Columns to update immediately on hire events**:
- Master Register: Hire Date [ACTUAL], Contract Signed [ACTUAL], Deposit Sent [ACTUAL]

The coordinator does not have permission to modify the Budget Alerts section or the Screening Criteria section. Those are project lead only.

---

## 7. End-of-Sprint Closeout Protocol

At project completion (August 10):

1. Coordinator sends final status report to project lead: all 6 contractors' deliverable status, all payment milestones confirmed paid, all Etsy listings live (or upload date logged).
2. Project lead confirms receipt and sends "Contract Complete" email to each contractor (Template 5, PHASE_3_CONTRACTOR_COMMUNICATION_TEMPLATES.md).
3. Coordinator removes Etsy store admin access from coordinator account (downgrade to viewer or remove).
4. Coordinator removes Kit email editor access from coordinator account.
5. Archive all deliverables in project shared drive with date-stamped folder (format: "Phase3-Archive-[DATE]").
6. Project lead logs Phase 4 contractor interest in WORKLOG.md for each of the 6 contractors (response to Template 5 question about future collaboration).
7. Update PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md: all rows marked COMPLETE.

**Retention of records**:
- Contracts: keep indefinitely (work-for-hire IP chain of custody)
- Payment confirmations: keep 3 years (tax records)
- Deliverables: keep indefinitely (used in ongoing Etsy listings)
- Contractor contact info: may be retained for Phase 4 outreach unless contractor requests removal

---

*Prepared: July 4, 2026. Activate at contract signature for first Phase 3 contractor. Coordinator begins Monday check-ins on July 14 (Week 1 of production). Dashboard update protocol active from first hire.*
