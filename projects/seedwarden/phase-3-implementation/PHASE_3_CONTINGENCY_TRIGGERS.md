---
title: "Phase 3 Contingency Triggers — Failure Mode Response Playbooks"
date: 2026-05-21
version: 1.0
status: execution-ready
phase: Phase 3 execution prep
cross-references:
  - PHASE_3_IMPLEMENTATION_CHECKLIST_MATRIX.md
  - PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md (v6.0)
  - PHASE_3_SECOND_WRITER_CANDIDATE_PROFILES.md
  - PHASE_3_GOLDENSEAL_SOURCING_COMPARISON.md
tags: [seedwarden, phase-3, contingency, risk, playbook]
---

# Phase 3 Contingency Triggers
## Failure Mode Response Playbooks

**Prepared**: May 21, 2026
**Purpose**: For each failure mode, this document defines the trigger condition, the immediate response, and the recovery path. No new decisions are required during execution — every failure mode resolves to a pre-defined action.

---

## How to Use This Document

When a problem occurs during execution:
1. Find the matching failure mode below
2. Verify the trigger condition is met
3. Execute the response steps in sequence
4. Log the trigger date and response action in WORKLOG.md

If a failure mode is not listed here, log it in WORKLOG.md and note whether it affects a zero-float dependency. Apply the following triage rule: if it affects writing, treat it as critical; if it affects photography or design only, it is non-critical (both tracks have extensive float).

---

## Failure Mode 1: Writer Unavailable After Hire (Combinations 3, 4, 7, 8, 9, 10)

**Trigger condition**: A confirmed second writer cancels, becomes unresponsive for 48+ hours during the sprint, or delivers content that fails the FTC or contraindication accuracy review with no viable revision path.

### Scenario A: Writer Cancels Before Sprint Start (Before June 22)

**Trigger**: Writer notifies cancellation or is unresponsive for 48 hours after June 1 deposit.

**Immediate response** (within 24 hours of trigger):
- [ ] Log cancellation in WORKLOG.md with date
- [ ] If cancellation before June 15 and scope was Option B: activate Option C solo (Combination 6) immediately; no pre-sprint timeline changes
- [ ] If cancellation between June 15 and June 22: activate Option C solo; confirm 3–4 hrs/day writing availability; all supplier orders and design work continue unchanged
- [ ] Send 1-sentence internal note: "Sprint scope reduced to Option C (3 bundles solo). Upload dates June 29, July 6, July 13 remain unchanged."

**Backup writer list** (contact in this priority order):
1. AHG directory RH with education activity listed who did not receive the original offer — check the outreach log from May 30 for second-choice candidates
2. Chestnut School partnerships@chestnutherbs.com — request urgent referral; explain 2-week timeline constraint
3. Herbal Academy partnerships@theherbalacademy.com — same request
4. Upwork posting with CITES test and FTC test as mandatory screening questions (post immediately; deadline 48 hours for applications)

**If no backup writer found within 48 hours**: Confirm Option C solo permanently. The June 22 sprint start date is the absolute constraint — no writer can be onboarded after June 18 with adequate briefing time.

### Scenario B: Writer Delivers Below-Threshold Content During Sprint

**Trigger**: Writer delivers a bundle draft that fails the contraindication accuracy review (herb-drug interactions missing or incorrect), fails the FTC compliance check, or contains factual errors in species identification or cultivation guidance.

**Immediate response**:
- [ ] Log failure details in WORKLOG.md: bundle, failure category (FTC / contraindication / accuracy), date received, date reviewed
- [ ] Do not upload any bundle until the failure is resolved
- [ ] Return the draft to the writer with specific corrections marked, citing the Critical Path Appendix A mandatory language; allow 24-hour revision turnaround
- [ ] If revision still fails: user rewrites the failing sections; deduct revision time from any final payment held pending completion
- [ ] If contraindication content is unfixable by the writer and the user cannot complete it within the sprint float window: defer the affected bundle to post-sprint; activate the post-sprint upload fallback dates (Immunity July 20, Digestive August 3 are already built into the plan)

**Timeline recovery**:
- Respiratory revision failure: Respiratory upload slips from July 1–2 to July 6–7 (identical to solo path); no practitioner tier impact
- Immunity revision failure: Immunity slips from July 15 to July 20 (identical to solo path); practitioner tier delays from July 10 to July 15
- Digestive revision failure: Digestive slips from July 22 to August 3 (identical to solo path)

**In all revision failure cases**: The fallback dates align exactly with Option A/C solo timelines — there is no catastrophic outcome; the result is equivalent to having chosen Option A or C solo from the beginning.

### Scenario C: Writer Becomes Unresponsive Mid-Sprint (48+ Hours)

**Trigger**: Writer does not respond to review requests or delivery check-ins for 48+ hours during the sprint.

**Immediate response**:
- [ ] Send one final email and one SMS/WhatsApp if available; allow 24 hours
- [ ] If still no response after 24 hours: declare the writer engagement terminated; log in WORKLOG.md
- [ ] User assumes writing responsibility for any incomplete bundles
- [ ] Apply Option C or Option A solo sprint steps from PHASE_3_IMPLEMENTATION_CHECKLIST_MATRIX.md for the affected bundles
- [ ] Withhold any unpaid payment milestones; document for potential contract enforcement
- [ ] If the terminated bundle was Respiratory and sprint is in Week 1: user can absorb Respiratory at 12–14 additional hours; this keeps the July 6–7 Respiratory upload intact if pace is confirmed at the June 24 gate

---

## Failure Mode 2: Goldenseal Sourcing Delayed (Path 1 Orders)

**Trigger condition**: Goldenseal nursery order placed by June 8 has not shipped by June 15 (Path 1 only); or supplier stock is unavailable at time of order attempt.

### Response — June 7 EOD (Pre-emptive)

This is a zero-float pre-emptive check, not a reactive trigger.

- [ ] June 7 EOD: verify order confirmation email from Prairie Moon or Strictly Medicinal has been received
- [ ] If no confirmation received: email media@ncbg.unc.edu and media@mobot.org immediately (same day, June 7 EOD); activate Path 2 in parallel while waiting for supplier response
- [ ] Log the parallel activation in WORKLOG.md

### Response — Triggered by Supplier Non-Shipment (June 15)

- [ ] Day 0 (June 15): order status shows no shipment confirmation → switch to Path 2 immediately; do not wait
- [ ] Same day: confirm 3+ Wikimedia Commons CC-BY-SA images for *Hydrastis canadensis* are already staged in PHOTO_ATTRIBUTION_LOG.md (they should be from the June 1–7 research window)
- [ ] If CC images are not yet researched: spend 1–2 hours on Wikimedia Commons immediately; log filenames and attribution strings
- [ ] Email media@ncbg.unc.edu if not already done; note in email that this is a time-sensitive educational use request
- [ ] Log Path 2 switch in WORKLOG.md: date triggered, original supplier, reason, CC images confirmed

### Response — Supplier Stock Unavailable at Order Time (June 8)

- [ ] Prairie Moon stock unavailable: immediately try Strictly Medicinal Seeds (strictlymedicinalseeds.com); confirm cultivated stock
- [ ] Strictly Medicinal also unavailable: activate Path 2 immediately; log in WORKLOG.md; proceed with Wikimedia CC
- [ ] Do not spend more than 30 minutes on supplier alternatives on June 8 — the writing sprint (June 22) is more important than resolving the photo path

### Path 2 Timeline Slippage Beyond June 21

If neither NCBG nor MOBOT has responded and Wikimedia CC images have not been researched by June 21:

- [ ] Spend 2 hours on June 21 completing Wikimedia Commons *Hydrastis canadensis* research; this is the pre-sprint zero-float deadline
- [ ] If NC Botanical Garden email response comes after June 21: add the higher-resolution images to the guide when received; they do not gate the sprint start
- [ ] Immunity cover design (June 29) uses the best Wikimedia CC image available at that date; NC Botanical Garden response can upgrade the image before the July 20 upload

**Writing is unaffected by this failure mode at any stage.** Goldenseal sourcing affects photography only.

---

## Failure Mode 3: Design Assets Late (Photos or Illustrations)

**Trigger condition**: Canva cover design for any bundle is not complete by its scheduled date, or Mountain Rose Herbs dried herb photography session cannot be completed before June 21.

### Photography Session Slip

**Photography has 12 days of float from its June 20 planned window to July 2 without impacting July 13 launch.**

- [ ] If Mountain Rose Herbs order not received by June 20: use Wikimedia Commons CC-BY-SA for all flat-lay bundle shots; studio session is a quality upgrade, not a launch requirement
- [ ] If photography session cannot happen before sprint start (June 22): all photography moves to post-sprint; Wikimedia and iNaturalist CC images cover 100% of species needs at launch quality
- [ ] Log photography slip in WORKLOG.md; confirm CC alternatives are staged

**Launch window slippage for a single bundle due to cover design delay**:

- [ ] If any cover design exceeds 1.5 hours at the scheduled date: simplify to a color block header with bold typography; this is confirmed launch-viable from Phase 2 precedent
- [ ] If cover is not complete 48 hours before the scheduled upload: use Google Docs PDF export as the fallback; the guide body content is the primary purchase driver for practitioner buyers
- [ ] Each cover has 3–4 days of individual float before the July 3 design lock — a single cover being 1–2 days late does not affect the upload date
- [ ] If the design lock date (July 3) passes with an incomplete cover: freeze all other completed covers; produce the missing cover with a simplified design in under 1 hour

**Launch window slippage calculation** (2 weeks per bundle):

If a cover is not complete at the time of the scheduled upload and the Google Docs fallback is not acceptable to the user, the upload slides by the next available upload slot (7-day Etsy spacing). The impact is:

| Bundle | Scheduled | 1-slot slip | 2-slot slip |
|---|---|---|---|
| Women's Health | June 29 | July 6 | July 13 |
| Respiratory | July 6 | July 13 | July 20 |
| Sleep | July 13 | July 20 | July 27 |
| Immunity | July 20 | July 27 | August 3 |
| Digestive | August 3 | August 10 | August 17 |

**A 1-slot slip in Women's Health (to July 6) delays the practitioner tier from July 15 to July 22.** This is the most consequential single slip. All other bundle slips do not affect the practitioner tier date.

### Canva Brand Kit Not Loaded by June 21

- [ ] If Canva Brand Kit (Phase 3 hex codes) is not loaded by June 21: load it on June 22 sprint Day 1 (15 minutes); this is the latest acceptable date
- [ ] If hex codes were never confirmed by June 15: the production hex codes from Critical Path Section 4 lock automatically. Load them on June 21.
- [ ] Design cannot start until Brand Kit is loaded. If not loaded by June 23 (cover session Day 2): all covers compress into June 24–27 window; they have sufficient float to absorb this.

---

## Failure Mode 4: Contraindication Review Identifies Gaps

**Trigger condition**: During the FTC compliance review (sprint Day 18, July 9) or a practitioner peer review, a mandatory warning, herb-drug interaction, or species accuracy issue is identified that cannot be resolved within the standard revision buffer (1.5–2 hours per bundle).

### Severity Classification

**Level 1 — Routine gap**: A FTC-compliant phrasing rewrite is needed; no clinical content change required.
- Response: Apply Appendix A Quick Reference rewrites; complete within 2 hours; no upload delay

**Level 2 — Content gap**: A contraindication interaction is missing (e.g., Valerian + benzodiazepine interaction not mentioned, or Lemon Balm TSH caution absent).
- Response: Insert the mandatory warning from Critical Path Appendix A; this requires < 30 minutes; no upload delay
- If the gap is discovered by a peer reviewer before upload: thank the reviewer, make the addition, send revised PDF to reviewer for confirmation

**Level 3 — Accuracy error**: A species claim, dosage statement, or conservation status is factually incorrect.
- Response: Correct the error before upload — no exceptions; hold the upload until corrected
- If the error is in a mandatory section (CITES sidebar, Ashwagandha thyroid warning, Vitex pregnancy contraindication): the correction is required regardless of upload timeline impact
- Timeline extension: up to 48 hours per Level 3 error; log in WORKLOG.md; shift subsequent upload dates by the delay amount if needed

**Level 4 — Systemic gap**: Multiple bundles have the same pattern of FTC or contraindication errors (e.g., all bundles use unqualified health claims that need systematic rewriting).
- Response: Activate a dedicated review day (use Float Day 1 on July 12, or extend post-sprint buffer)
- If all 5 bundles require systematic revision and it cannot be completed before the July 13 sprint close: upload Women's Health and Respiratory on schedule (these will have been reviewed earliest); hold Sleep until Level 4 correction is complete; maximum delay to Sleep upload is July 20 (Immunity's original date)

### Escalation to Practitioner Network

If a Level 3 error in a safety-critical section (Goldenseal CITES sidebar, Ashwagandha thyroid warning, Passionflower MAOI note, Valerian CNS interaction) cannot be self-verified:

- [ ] Email the practitioner contact identified during the peer review outreach window; provide the specific passage and ask for accuracy confirmation; request response within 24 hours
- [ ] If no response within 24 hours: hold that specific bundle's upload until confirmed; other bundles upload on schedule
- [ ] Use the practitioner response as a credibility signal in the Etsy listing description once the review is confirmed

**This escalation process should be pre-established during sprint Week 1 by contacting the practitioner reviewer early** (Women's Health peer reviewer contacted by June 22; Immunity peer reviewer contacted by July 2). Early outreach means the relationship exists before a Level 3 trigger occurs.

---

## Failure Mode 5: Affiliate Partner Issues

**Trigger condition**: An affiliate partner (influencer, practitioner, or co-marketing contact) requests changes to bundle content, commission structure, or messaging after affiliate agreement is signed; or a bundle content change is required post-launch that affects affiliate messaging.

### Scenario A: Affiliate Requests Content Change After Launch

- [ ] Log the request in WORKLOG.md: affiliate name, bundle, requested change, date received
- [ ] Classify the request: (a) factual correction — implement immediately; (b) marketing preference — evaluate against practitioner accuracy standard; (c) FTC-related — implement if the affiliate is correct; reject if the requested change introduces an unqualified health claim
- [ ] Notify the affiliate of the decision within 72 hours; if content is updated, send them the revised listing URL

### Scenario B: Commission Structure Dispute

- [ ] Review the original affiliate agreement logged in WORKLOG.md
- [ ] Native Etsy coupon code structure (15% discount, 10–20% revenue share via PayPal) is verbal/informal for Phase 3 — enforce based on WORKLOG.md record
- [ ] If dispute cannot be resolved within 48 hours: deactivate the specific coupon code; offer the affiliate a replacement code with the corrected terms
- [ ] Do not adjust list prices to resolve affiliate disputes — list price integrity is a non-negotiable anchor for the practitioner tier perception

### Scenario C: Bundle Cover Scope Change Required Post-Launch

A post-launch v1.1 update (e.g., Goldenseal specimen photography upgrade) affects the cover image.

- [ ] Update the Canva file and re-export the PDF
- [ ] Update the Etsy listing description: add "Now includes original botanical photography" or equivalent
- [ ] Notify active affiliates by email: "Bundle [name] has been updated to version 1.1. Your affiliate link/coupon code is unchanged."
- [ ] No commission adjustment required for cover image updates

### Scenario D: Messaging Revision Required by Affiliate (Practitioner Reviewer)

If an AHG RH reviewer requests that a health claim in the listing description be rephrased:

- [ ] This request has priority — implement within 24 hours
- [ ] Apply FTC Quick Reference language from Critical Path Appendix A
- [ ] Update both the Etsy listing description and the PDF interior if the claim appears in both
- [ ] Re-export the PDF and update the Etsy file; buyers who purchased before the update receive the updated file automatically via Etsy's file replacement system

---

## Failure Mode 6: Phase 2 Gates Drop Below Threshold

**Trigger condition**: Forager cohort conversion drops below 20% or native plants conversion drops below 1.5% during the June 20 pre-sprint gate check. (Both gates are currently cleared with margin as of May 21.)

### Single Gate Drop

- [ ] If one gate drops: continue all pre-sprint preparation (sourcing, photography, design); hold upload authorization for Women's Health only
- [ ] Recheck the dropped gate on June 22 (sprint start day)
- [ ] If recovered by June 22: authorize Women's Health upload for June 29 as planned
- [ ] If still below threshold on June 22: delay Women's Health upload to July 13 (7 days after Respiratory if Respiratory was uploaded June 29 as a fallback; however, Women's Health is the higher-priority first upload — hold it rather than upload Respiratory first)
- [ ] Continue writing sprint regardless of gate status; writing is not gated on upload authorization

### Both Gates Drop Simultaneously

- [ ] Hold all uploads; continue pre-sprint work (no incremental cost)
- [ ] Recheck both gates July 1
- [ ] If both recovered by July 1: authorize uploads with adjusted dates (Women's Health July 13, Respiratory July 20, Sleep July 27)
- [ ] Practitioner tier delayed to July 29 under this scenario
- [ ] Full library delayed from August 3 to approximately September 3
- [ ] 90-day revenue estimate from the new July 13 start: approximately $2,400–2,800 for Option C (same absolute revenue, window shifts by 2 weeks)

---

## Failure Mode 7: Etsy Account Issue

**Trigger condition**: Etsy account receives a policy violation notice, listing removal, or payment hold that prevents upload on a scheduled date.

- [ ] Log the notice in WORKLOG.md: date received, listing affected, reason stated
- [ ] Do not upload additional listings until the existing issue is resolved
- [ ] If the issue is a content policy flag (health claim): apply FTC Quick Reference rewrites immediately; resubmit the listing within 24 hours
- [ ] If the issue is a payment hold: contact Etsy seller support via chat (not email — chat is faster); resolution typically within 24–72 hours; hold all uploads during the hold period
- [ ] If resolution takes more than 72 hours: prepare listings in draft form; upload on the next available day after resolution; apply the standard 7-day spacing from the resolution date forward

---

## Contingency Trigger Summary — Quick Reference

| Trigger | Condition | Response Time | Primary Action |
|---|---|---|---|
| Writer cancels before Jun 22 | Writer unresponsive 48 hrs or cancels | Within 24 hrs | Activate Option C solo; scope reduces, dates intact |
| Writer content fails review | FTC or contraindication accuracy fails | Within 24 hrs of review | Send revision notes; 24-hr turnaround; fallback to solo if unfixable |
| Writer unresponsive mid-sprint | 48 hrs unresponsive | Within 24 hrs | Declare terminated; user assumes bundle; apply solo sprint steps |
| Goldenseal order not shipped Jun 15 | No shipment confirmation | Same day | Switch to Path 2; confirm CC images; log in WORKLOG.md |
| Goldenseal supplier unavailable Jun 8 | No cultivated stock at order time | Within 30 min | Try backup supplier; if unavailable, activate Path 2 |
| Photo session cannot happen pre-sprint | Mountain Rose Herbs delayed or schedule conflict | Before Jun 22 | All photography moves post-sprint or to CC; launch unaffected |
| Cover design exceeds 1.5 hrs | Single cover taking too long | During design session | Simplify to color block; Google Docs fallback |
| Contraindication Level 1–2 gap | Found during FTC review | Within 2 hrs | Apply Appendix A mandatory language; no upload delay |
| Contraindication Level 3 error | Factual error in mandatory section | Before upload | Correct before upload; up to 48-hr delay per bundle |
| Contraindication Level 4 (systemic) | Multiple bundles affected | Float Day 1 | Use Float Day 1; hold Sleep if needed; max delay to Jul 20 |
| Affiliate content dispute | Post-launch change request | Within 72 hrs | Classify and respond per Scenario A–D |
| Single Phase 2 gate drops | Below 20% or 1.5% | Jun 20 check | Hold WH upload; recheck Jun 22; continue sprint |
| Both Phase 2 gates drop | Both below threshold | Jun 20 check | Hold all uploads; recheck Jul 1; full dates shift 2 weeks |
| Etsy policy violation | Notice received | Within 24 hrs | Apply FTC rewrites; resubmit; hold all uploads until resolved |
| Jun 24 pace gate fails | WH below 2,500 words EOD | Same day | Activate Option C (if on A): no date changes; pace pressure drops |

---

*Version 1.0 — May 21, 2026. All trigger thresholds and recovery paths derived from PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md v6.0 risk register and PHASE_3_SECOND_WRITER_CANDIDATE_PROFILES.md Section 7.*
