---
title: "Phase 3 Production Sprint Risk Register — 8 Quantified Risks with Detection, Escalation, and Mitigation Procedures"
date: 2026-06-05
version: 1.0
status: production-ready
review-schedule: June 22 (sprint Day 1), June 24 (D3 pace gate), June 29 (D8 Women's Health upload), July 6 (D15 Respiratory upload), July 13 (D22 sprint close)
sprint-window: June 22 – August 3, 2026 (primary sprint to July 13; post-sprint uploads to Aug 3)
cross-references:
  - PHASE_3_CRITICAL_PATH_ANALYSIS_JUNE22_JULY13.md (pace gate, upload dates, float)
  - PHASE_3_CONTRACTOR_DECISION_TREE.md (contractor dropout recovery, solo fallback)
  - PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md (backup roster, vetting rubric)
  - PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md (v8.0 — FTC Quick Reference, CITES sidebar, contraindication requirements)
  - PHASE_3_LAUNCH_RISK_REGISTER.md (v1.0 May 21 — earlier risk inventory for cross-reference)
tags: [seedwarden, phase-3, risk-register, sprint, production, mitigation, contractor, FTC, contraindication]
---

# Phase 3 Production Sprint Risk Register

**Prepared**: June 5, 2026
**Scope**: 8 risks covering contractor lifecycle, content production, image sourcing, scope management, compliance, and scheduling. Each risk is quantified by probability and impact, with specific detection thresholds, detection procedures, escalation criteria, mitigation actions, and ownership.

**Risk scoring methodology**:
- Probability (P): percentage likelihood of occurrence during the sprint window
- Impact (I): CRITICAL = launch date or revenue ceiling affected; HIGH = upload date or quality floor affected; MEDIUM = schedule slip or cost increase; LOW = minor inconvenience, absorbed by float
- Composite rating: P × I category determines priority order for monitoring

---

## Risk Register Summary

| # | Risk Name | P | I | Composite | Owner | Detection Method | Current Status |
|---|---|---|---|---|---|---|---|
| 1 | Contractor Dropout | 15% | CRITICAL | P-LOW × I-CRITICAL | User | Email silence >3 days | Monitor from contract signing |
| 2 | Image Sourcing Delay | 20% | HIGH | P-MEDIUM × I-HIGH | User | Missed day-level checkpoints | Pre-staging complete before June 22 |
| 3 | Women's Health Scope Creep | 10% | CRITICAL | P-LOW × I-CRITICAL | User | Word count overage >10% | Scope freeze by Day 2 checkpoint |
| 4 | Contraindication Research Gaps | 10% | HIGH | P-LOW × I-HIGH | User + Contractor | Peer review red flags | FTC Quick Reference pre-compiled |
| 5 | Payment Delays | 5% | MEDIUM | P-VERY-LOW × I-MEDIUM | User | Invoice past due 5 days | Contract milestone terms pre-set |
| 6 | Scope Expansion Mid-Sprint | 20% | MEDIUM | P-MEDIUM × I-MEDIUM | User | New bundle requests | Defer-to-Phase-4 policy established |
| 7 | Deadline Compression Week 2–3 | 15% | HIGH | P-LOW × I-HIGH | User | Day 14 checkpoint word count <75% | Float days preserved |
| 8 | Solo Fallback Decision Cascade | 20% | HIGH | P-MEDIUM × I-HIGH | User | Contractor unavailable by June 15 | Decision tree active (see companion doc) |

---

## Risk 1: Contractor Dropout

**Probability**: 15%  
**Impact**: CRITICAL  
**Description**: The contractor confirms and begins writing, then becomes unresponsive or explicitly withdraws during the sprint window (June 22 – August 1). This risk applies from contract signing through the final bundle delivery.

The 15% probability reflects: typical freelance dropout rates for 4–6 week engagements are 10–20%; medicinal herb writing projects have a slightly lower dropout rate than general freelance because the candidate pool self-selects for commitment level. However, health emergencies, competing engagements, and scope misalignment are the primary causes.

### Trigger Thresholds

- **Passive detection trigger**: Contractor has not replied to any communication for 3 consecutive calendar days during the sprint
- **Active dropout**: Contractor explicitly communicates inability to continue
- **Deadline miss without communication**: Contractor does not deliver a promised bundle draft on the agreed date AND has not communicated any delay

### Detection Procedure

**Daily (Sprint Days 1–14)**: Review email inbox for contractor communications. Log last contact date in WORKLOG.md.

**Automated tracking**: Note the date of the contractor's last reply in the contractor tracking log. If the last reply date is 3 or more days ago AND you have sent at least 1 follow-up in that window: activate the detection response below.

**Detection response — Day 1 of 3-day silence**:
1. Send email: "Checking in on [bundle name] progress — where are you with the draft?"
2. Note in WORKLOG.md: "[Date] — Day 1 of contractor silence. Follow-up sent."

**Detection response — Day 2 of 3-day silence**:
1. Send second email AND attempt phone contact if number was provided in contract
2. Note: "[Date] — Day 2 of contractor silence. Second contact attempt."

**Detection response — Day 3 of 3-day silence (trigger confirmed)**:
1. Assume dropout. Do not wait for further response.
2. Log in WORKLOG.md: "[Date] — Contractor assumed dropout. Mid-sprint recovery activated."
3. Begin Mid-Sprint Dropout Procedure immediately (see Mitigation Actions below).

### Escalation Criteria

**Escalate to full recovery mode** (do not wait for confirmation): When 3-day silence threshold is crossed. The cost of waiting a 4th day for confirmation is higher than the cost of beginning recovery a day early if the contractor returns.

**Re-engage contractor**: If contractor returns after dropout is declared and offers to complete remaining work — evaluate case-by-case. Accept only if: (a) the contractor's reason is verifiable (documented illness, family emergency), (b) the remaining work is more than 50% of contracted scope, and (c) the new delivery date does not compress the FTC review and export window below 48 hours. Do not re-engage a contractor who dropped due to scope misalignment or rate dispute.

### Mitigation Actions

**Pre-sprint (prevention)**:
- Include explicit dropout clause in contract: "If contractor is unable to complete the engagement, milestone payments are paid only for delivered and accepted work. Unused milestones are cancelled with no additional payment."
- Require contractor to provide a phone number and emergency contact method at contract signing
- Maintain the backup roster list: any candidates who scored 60+ on the vetting rubric but were not selected. If the primary contractor drops, contact backup roster within 24 hours of dropout confirmation.
- Maintain one candidate on standby offer (Tier B candidate who was runner-up) through July 1 — the first critical delivery date.

**Mid-sprint recovery (if dropout confirmed)**:
Per PHASE_3_CONTRACTOR_DECISION_TREE.md Mid-Sprint Dropout Procedure:
- If dropout occurs before July 1 (Respiratory first draft): user absorbs Respiratory; upload dates cascade as defined in the Decision Tree document
- If dropout occurs after July 1: user performs revision pass on delivered Respiratory draft; Immunity and Digestive shift to solo pace
- Do not attempt to source a replacement contractor after July 8 — insufficient onboarding time for the remaining scope

**Ownership**: User. Monitor daily. Activate recovery without delay when threshold is crossed.

---

## Risk 2: Image Sourcing Delay

**Probability**: 20%  
**Impact**: HIGH  
**Description**: Photography or Wikimedia Commons / iNaturalist image sourcing falls behind the schedule required to populate Etsy listing image slots before upload dates. Specifically: dried herb studio photography session (June 17–21) is delayed by supplier delivery slip, and no CC-licensed alternatives are pre-staged.

The 20% probability reflects: Mountain Rose Herbs order delays occur in approximately 15–25% of orders during peak periods; photography session delays due to scheduling or equipment issues occur in approximately 20% of self-managed studio sessions. The two-failure condition (supplier delay AND no CC pre-staging) is the actual risk — either failure alone is recoverable.

### Trigger Thresholds

- **Supplier detection trigger**: Mountain Rose Herbs order not shipped by June 19 (4 days after June 15 order date, which is 2 days past the normal 3–5 business day window)
- **Photography detection trigger**: No studio session completed and no CC-licensed images confirmed for any bundle by June 21 EOD
- **Upload impact trigger**: Etsy listing image Slot 1 (cover hero image) is not populated by the upload date for any bundle

### Detection Procedure

**June 18 (Day 3 after MRH order)**:
- Check Mountain Rose Herbs order status online or by email
- If tracking confirms shipment: no action needed. Expected delivery June 17–21.
- If no tracking number: email Mountain Rose Herbs order support with order number. Request tracking within 24 hours.
- Log in WORKLOG.md: "June 18 — MRH order status checked. [Tracking: confirmed / Not yet shipped — follow-up sent]."

**June 21 EOD — Pre-sprint image audit**:
- Open the photo attribution log (PHOTO_ATTRIBUTION_LOG.md)
- Confirm: at least 1 image per bundle is confirmed with CC license and attribution text
- If any bundle has 0 images confirmed: activate the Wikimedia sourcing sprint (30 minutes maximum — per-bundle sourcing is fast with the search procedure below)
- Log: "June 21 — Image audit complete. Bundles confirmed: [list]. Bundles needing CC sourcing: [list]."

**Day-level checkpoints during sprint (June 22 – July 13)**:
- Every upload day (June 29, July 6, July 13): verify Slot 1 image is uploaded and thumbnail crops correctly at 170×135px before scheduling the listing. This is a 5-minute check, not a new task.

### Escalation Criteria

**Escalate to Frontier Co-op emergency order**: If Mountain Rose Herbs order has not shipped by June 19 AND delivery by June 22 is not confirmed. Frontier Co-op order placed same day, June 19. Frontier ships 3–5 business days — delivery June 24–26. Photography session shifts to Sprint Days 2–4 (June 23–25). Zero impact on June 29 Women's Health upload.

**Escalate to full CC-only mode**: If both Mountain Rose Herbs and Frontier Co-op orders are delayed beyond June 25. At this point, all listing images are sourced from Wikimedia Commons and iNaturalist. This is the pre-planned fallback — all 14 species have verified CC-BY-SA sources. Activate this without hesitation.

### Mitigation Actions

**Pre-sprint (prevention)**:
- Pre-stage Wikimedia Commons CC-BY-SA images for all 14 species before June 21. Log filenames and attribution text in PHOTO_ATTRIBUTION_LOG.md. This converts the image sourcing risk from a production blocker to a quality upgrade — studio photos are better than CC images, but CC images are publication-ready.
- CC sourcing procedure (30 minutes per bundle):
  1. Go to commons.wikimedia.org/wiki/Special:Search
  2. Search: "[Species name] medicinal" — filter to images with CC-BY-SA license
  3. For each bundle, confirm: 1 full-plant habit photo + 1 leaf/flower close-up
  4. Log: filename, URL, photographer, license, attribution text
- The Wikimedia Commons CC-BY-SA image for Goldenseal (at-risk; photography of wild specimens is problematic) should be the cultivated specimen from University of Michigan Herbarium records or the USDA PLANTS database — verify CC license before logging.

**In-sprint (recovery)**:
- If studio photography is complete: supplement CC images with studio flat-lays in Etsy image Slots 2–3. This is the intended production plan.
- If studio photography is not complete by upload date: publish listing with CC images in all slots. Add studio images as a listing update within 2 weeks of upload. Etsy allows listing image updates without resetting the listing or losing reviews.

**Ownership**: User. Pre-staging is a pre-sprint action; in-sprint monitoring is a 5-minute daily check.

---

## Risk 3: Women's Health Scope Creep

**Probability**: 10%  
**Impact**: CRITICAL  
**Description**: The Women's Health bundle — the critical path anchor of the sprint — expands beyond its defined word count and species scope during Days 1–3 writing, consuming pace buffer and pushing the June 24 pace gate and June 29 upload date.

This is a CRITICAL impact risk because Women's Health has zero float: it must be complete by June 28 (PDF export QA) and uploaded by June 29 (10am ET). A 2-day slip on Women's Health cascades to all subsequent upload dates.

The 10% probability reflects: scope creep on the first bundle of a writing sprint is common, especially when the writer is developing the structural template for the first time. The Black Cohosh conservation sidebar and Vitex invasive-species framing are the two most likely expansion points — both have more content depth than the word budget allocates.

### Trigger Thresholds

- **Detection trigger**: Women's Health word count exceeds 110% of the target for any section by end of the session in which that section is written
  - Black Cohosh target: 700 words (conservation sidebar: 150 words max). Trigger: >770 words OR sidebar >165 words
  - Vitex target: 600 words. Trigger: >660 words
  - Total guide target: 3,400–3,600 words. Trigger: >3,960 words before self-edit pass begins
- **Pace gate trigger**: Women's Health below 2,500 words at June 24 EOD (from PHASE_3_CRITICAL_PATH_ANALYSIS doc — this is the existing pace gate, not a new threshold)

### Detection Procedure

**End of each writing session (Days 1–3)**:
- Word count check: select all text in the current section, check count in word processor
- Compare against section word budget in PHASE_3_BUNDLE_CONTENT_OUTLINE_DETAILED.md
- If overage detected: note in WORKLOG.md and apply scope freeze before starting next section

**June 24 EOD (D3) — Formal Pace Gate**:
- Count total Women's Health document words
- Log in WORKLOG.md: "D3 pace gate — Women's Health word count: [X]. Gate: 2,500. Status: [PASS / FAIL]."
- If FAIL: activate Option C immediately. Do not attempt to recover within Option A.

### Escalation Criteria

**Scope freeze activation**: When any single section exceeds 110% of its target, the scope for that section is frozen. Do not continue expanding that section. Move to the next section. The expansion content becomes a "v1.1 additions" note at the bottom of the writing file.

**Option C activation**: If Women's Health is below 2,500 words at June 24 EOD (indicating that scope creep on early sections consumed the pace rather than advancing word count overall). This is counterintuitive — scope creep often reduces word count by consuming writing time on research rather than prose.

### Mitigation Actions

**Prevention (Sprint Day 1 and 2)**:
- Write section targets at the top of each session: "Today: Black Cohosh (700w target, sidebar 150w max). Stop at 770 words regardless of incomplete thoughts — note what is missing for v1.1."
- The conservation sidebar (Black Cohosh) is the single highest-risk expansion point. Write the sidebar in a separate document section. Hard-stop at 165 words. Paste into main document when complete.
- Do not research additional contraindication sources mid-session. The FTC Quick Reference and NatMed Pro contraindication pre-compilation from pre-sprint prep are the sources for the sprint. Do not open additional database tabs during writing sessions.

**Recovery (if scope freeze is triggered)**:
- Cut any section that has exceeded its budget to the word target. Move excess content to a "v1.1 expansion notes" file. This does not feel good in the moment; it is correct.
- Use the scope-reduction cascade: Vitex can be compressed to 400 words (from 600) by removing the invasive-species regional detail to a single sentence. Red Clover can be compressed to 250 words (from 400) by limiting it to isoflavone framing and forager edibility crossover note. These compressions preserve the core clinical content.

**Ownership**: User (and contractor for the Women's Health bundle — but Women's Health is user-written in the recommended scope split). Monitoring is self-managed daily.

---

## Risk 4: Contraindication Research Gaps

**Probability**: 10%  
**Impact**: HIGH  
**Description**: A published bundle guide is found to contain a missing or inaccurate contraindication — a drug interaction, pregnancy safety statement, or pediatric caution — that a peer reviewer identifies after the guide is live on Etsy. This creates FTC liability, potential tort exposure, and reputational damage with the practitioner audience.

The 10% probability is low because of the pre-compiled FTC Quick Reference and the mandatory contraindication register in the critical path document. However, the Immunity bundle (Ashwagandha thyroid interaction, Goldenseal herb-drug interactions) and the Sleep bundle (Valerian GABA-pathway interactions, Passionflower MAOI interaction) carry the highest probability of a gap because their interaction profiles are complex and multi-pathway.

### Trigger Thresholds

- **Self-detection trigger**: During the FTC compliance review pass (D18, July 9), a therapeutic claim is found that reads as a direct disease treatment claim without evidence-tier qualification
- **Peer review trigger**: An AHG reviewer returns a written comment identifying a missing contraindication or an inaccurate safety statement
- **Post-launch detection**: A practitioner buyer contacts Seedwarden (via Etsy message or email) identifying a contraindication error
- **Internal review red flag**: During self-edit pass of any bundle, the writer identifies a contraindication section that does not cite a specific primary source — "generally considered safe for most adults" without a citation is a red flag

### Detection Procedure

**Embedded in writing (every session)**:
- FTC Quick Reference table (from PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md Appendix A) is open in a browser tab during all writing sessions
- Every therapeutic action claim is checked against the evidence tier before the writing session ends
- Every contraindication section is cross-checked against NatMed Pro or Memorial Sloan Kettering database before the self-edit pass

**Self-edit pass (included in writing schedule)**:
- Every bundle includes a self-edit pass as the final writing day activity (see PHASE_3_CRITICAL_PATH_ANALYSIS_JUNE22_JULY13.md writing calendar)
- Self-edit focuses first on contraindication sections (highest liability), second on evidence-tier language in therapeutic claims, third on structural coherence

**D18 FTC compliance review (July 9)**:
- Priority order: Women's Health → Immunity → Sleep → Respiratory → Digestive
- Women's Health and Immunity cannot be deferred — they carry the highest FTC risk
- Respiratory and Digestive can be deferred to post-launch v1.1 if float is consumed, but only after the critical bundles pass

**Peer review integration**:
- If an AHG reviewer is confirmed before sprint: their written comments are reviewed within 48 hours of receipt. Any flagged contraindication gap is corrected before the affected bundle goes live.
- If reviewer comments arrive after a bundle is already live (e.g., Women's Health is live before the reviewer responds): update the guide PDF, re-export, and update the Etsy listing. Notify the reviewer that their correction has been incorporated.

### Escalation Criteria

**Escalate to expert review** (beyond self-check): If a contraindication panel for any Tier 2 or Tier 3 species cannot be confirmed by two independent database sources, escalate to the AHG peer reviewer or AANP directory naturopath for that specific section. Do not publish unverified Tier 2 contraindications.

**Escalate to immediate listing update** (post-launch): If a contraindication error is identified after a bundle is live — by any source — update the guide PDF within 24 hours, re-export, and update the Etsy listing. Do not wait for the next scheduled review. Prioritize Women's Health (Vitex pregnancy contraindication, Black Cohosh menopausal interaction with estrogen therapy) and Sleep (Valerian with benzodiazepines, Passionflower with MAOIs).

**Escalate to listing suspension** (severe scenario): If a peer reviewer identifies a contraindication error that could cause direct patient harm (e.g., an omitted MAOI interaction for Passionflower in a guide already sold to a practitioner who prescribed it), suspend the listing immediately and contact the reviewer for guidance on the correction. This scenario is unlikely given the pre-compiled contraindication register but must be treated as a zero-delay response.

### Mitigation Actions

**Pre-sprint**:
- Complete the contraindication pre-compilation for all 14 sprint species before June 22. Use NatMed Pro (primary) and MSK Integrative Medicine database (cross-check). Log all interactions in the species database with source URL and access date.
- The mandatory contraindication register from PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md Appendix A covers the five highest-risk interactions:
  - Vitex: avoid during pregnancy; may interact with dopaminergic drugs
  - Ashwagandha: thyroid hormone system interaction; avoid in hyperthyroidism; pregnancy caution
  - Valerian: potentiates CNS depressants including benzodiazepines and alcohol
  - Passionflower: MAOI interaction — do not combine with MAO inhibitor drugs
  - Lemon Balm: TSH (thyroid-stimulating hormone) reduction possible; caution in hypothyroidism
- This register must be pasted verbatim into each relevant bundle, not paraphrased. Paraphrasing introduces inaccuracy.

**In-sprint (contractor oversight)**:
- If a contractor is writing the Immunity bundle: user reviews the Ashwagandha thyroid warning and Goldenseal CITES sidebar before approving the Milestone 3 payment. Specifically: the Ashwagandha thyroid warning must name the specific interaction (withanolide activity on thyroid hormone axis) and must not use the phrase "generally safe" without qualification.
- Contractor-submitted contraindication panels are not published without user review.

**Ownership**: User for all user-written bundles. User retains final approval authority on all contractor-written bundles. No contraindication content is published without user sign-off.

---

## Risk 5: Payment Delays

**Probability**: 5%  
**Impact**: MEDIUM  
**Description**: A payment milestone to the contractor is delayed past the agreed date due to platform processing issues, banking delays, or user oversight. This creates contractor distrust, potential work stoppage, and relationship damage.

The 5% probability is low because payment milestones are triggered by specific deliverable events (draft received), which gives the user 24–48 hours to process the payment after reviewing the draft.

### Trigger Thresholds

- **Detection trigger**: A milestone payment is 5 calendar days past the date the deliverable was accepted
- **Contractor detection**: Contractor sends a payment follow-up email

### Detection Procedure

**After each bundle draft is accepted (reviewed and approved)**:
- Immediately log in WORKLOG.md: "[Date] — Respiratory/Immunity/Digestive draft accepted. Milestone [2/3/4] payment due within 3 business days."
- Set a calendar reminder for 3 business days after acceptance
- If reminder fires and payment has not been sent: send immediately

### Escalation Criteria

**5 days past due**: Contact the contractor proactively with the payment confirmation and explanation of the delay. Do not wait for the contractor to escalate. A practitioner-credentialed contractor who is not paid on time has professional options (stopping work, platform dispute) that are more disruptive than a proactive explanation.

### Mitigation Actions

**Contract specification**: Include the payment window in the contract: "Milestones are paid within 3 business days of written acceptance of each bundle draft." This converts the payment timeline from an informal expectation to a contractual obligation — which is in the user's interest, not just the contractor's.

**Payment pre-staging**: Before sprint Day 1, confirm that the payment method (PayPal, Wise, Upwork escrow) is funded and operational. A payment failure due to a depleted PayPal balance is avoidable. Stage the full contract amount ($1,000–$1,350) in the payment account before the contract is signed.

**Ownership**: User. Simple monitoring with a calendar reminder system.

---

## Risk 6: Scope Expansion Mid-Sprint

**Probability**: 20%  
**Impact**: MEDIUM  
**Description**: During the sprint, a new bundle concept (a sixth bundle, a bundle variant, or an add-on product) is proposed or seems attractive based on early sales data. Adding scope mid-sprint without a formal decision process diverts writing time from committed bundles and risks missing upload dates.

The 20% probability reflects the pattern of sprint momentum: positive Women's Health sales (if early Etsy discovery is good) create pressure to add content. Herbalist outreach conversations during the sprint may surface bundle ideas that feel urgent. Both are normal and both are scope expansion risks.

### Trigger Thresholds

- **Detection trigger**: Any new bundle concept or product addition is considered during the sprint window (June 22 – July 13)
- **Automatic defer**: Any new bundle concept triggers the defer-to-Phase-4 policy below before discussion proceeds

### Detection Procedure

**At the moment of trigger**: Log the idea in WORKLOG.md with date: "Scope expansion idea: [concept]. Deferred to Phase 4 queue. Date: [X]."

This takes 30 seconds. The act of logging the idea creates a record that it was considered (not dismissed), while enforcing the defer policy without debate.

### Escalation Criteria

**Exception to defer policy**: A scope addition is considered mid-sprint only if it meets all three of the following: (1) it is a variant of an existing committed bundle (not a new species scope), (2) it requires less than 4 hours of additional writing time, and (3) it does not change any upload date. Example: adding a "Practitioner FAQ" appendix to the Women's Health guide — same species, same FTC frame, 30–60 minutes of writing. This is acceptable mid-sprint. A new "Digestive Health — Advanced Formulations" guide is not.

### Mitigation Actions

**Pre-sprint policy establishment**: Log the defer-to-Phase-4 policy in WORKLOG.md before June 22: "Phase 3 scope is fixed at 5 bundles (Women's Health, Respiratory, Immunity, Sleep, Digestive). Any new bundle concept arising during the sprint is deferred to the Phase 4 queue. This policy applies from June 22 through July 13."

**Phase 4 queue**: Maintain a running list of deferred ideas. Review the list at the July 13 sprint retrospective. The best ideas from this list become the Phase 4 scope — they are not lost, only deferred.

**Ownership**: User. Self-enforced defer policy. No external monitoring needed.

---

## Risk 7: Deadline Compression Week 2–3

**Probability**: 15%  
**Impact**: HIGH  
**Description**: The Immunity + Sleep writing window (June 29 – July 5, Sprint Week 2) runs behind pace, compressing the July 5 milestone (both bundles complete and self-edited) and creating risk on the July 6 Respiratory upload and July 13 Sleep upload.

This is distinct from Women's Health scope creep (Risk 3) and contractor dropout (Risk 1). It reflects the structural challenge of Week 2: the sprint pace is 5 hours/day of writing while simultaneously managing Women's Health promotion (email broadcast June 29, Instagram and Pinterest content, AHG outreach responses) and Canva cover design (Immunity and Sleep covers due June 29–30).

### Trigger Thresholds

- **Day 14 checkpoint (July 5 EOD)**: Word count check for both Immunity and Sleep bundles
  - Immunity target by July 5: 3,800 words, self-edited
  - Sleep target by July 5: 3,500 words, self-edited
  - Detection trigger: Either bundle is below 75% of its target (Immunity <2,850 words; Sleep <2,625 words) at July 5 EOD
- **Mid-week early warning (July 2–3)**: If Immunity writing is behind by 500+ words at July 2 EOD (Goldenseal section not yet started), the July 5 milestone is at risk

### Detection Procedure

**July 2 EOD early warning check**:
- Count Immunity words
- Immunity should be 2,500+ words by July 2 (D11) — the Goldenseal CITES sidebar + cultivation section should be drafting
- If below 2,000: log in WORKLOG.md: "D11 early warning — Immunity at [X] words vs. 2,500 target. Float Day 1 risk elevated."

**July 5 EOD formal checkpoint**:
- Count both Immunity and Sleep words
- Log: "D14 checkpoint — Immunity: [X] words (target 3,800). Sleep: [X] words (target 3,500). Status: [ON TRACK / BEHIND — cascade activated]."

### Escalation Criteria

**Below 75% on either bundle at July 5 EOD**: Activate scope reduction cascade immediately.

**Scope reduction cascade (ordered)**:
1. First reduction: Immunity bundle — compress Echinacea section (reduce from Immunity-specific framing to a condensed 300-word cross-reference to Respiratory bundle). Saves 500–600 words of writing without losing clinical content.
2. Second reduction: Sleep bundle — compress Lavender section (second occurrence; reference Women's Health version) to 150 words. Saves 200–250 words.
3. Third reduction: If still behind after 1 and 2 — defer Digestive bundle entirely to post-sprint (August 3 was already the target; this is not a new deferral, just confirmation).

**Float Day 1 (July 12) activation**:
Float Day 1 exists precisely for Week 2–3 overruns. If Week 2 runs behind:
- Float Day 1 is consumed by writing (Immunity or Sleep completion)
- The July 13 Sleep upload proceeds from Float Day 1 completion the day before
- Float Day 2 (July 13 afternoon) handles any remaining Sleep PDF export QA

### Mitigation Actions

**Pre-sprint protection**:
- Schedule Women's Health promotional activities (email broadcast, social posts, AHG responses) in the late afternoon or evening of June 29 — not the morning. Morning writing time on June 29 (D8) is the Immunity writing start. Upload Women's Health in the 9–10am ET window, then return to writing, then handle promotion in the afternoon.
- Canva cover sessions for Immunity and Sleep (June 29–30) are scheduled for 30-minute windows maximum. If a cover session exceeds 30 minutes: switch to the placeholder cover (existing template with color swap) and finish later. Do not sacrifice writing time for cover polish.

**In-sprint monitoring**:
- Daily word count log in WORKLOG.md during Weeks 2–3. 5 minutes at end of each session: "[Date] — [Bundle]: [X] words. Session target: [Y]. Cumulative gap: [Z]."

**Ownership**: User. Float Day 1 is the primary structural mitigation.

---

## Risk 8: Solo Fallback Decision Cascade

**Probability**: 20%  
**Impact**: HIGH  
**Description**: No contractor is confirmed by the June 15 EOD threshold, triggering the solo fallback model. The risk is not the solo model itself — it is the decision delay that allows the solo fallback to be triggered at the last moment rather than proactively, leaving insufficient time to mentally and operationally shift from a contractor-assisted sprint to a solo 12 hrs/week model.

The 20% probability reflects the difficulty of finding a qualified herbalist writer with the contraindication depth required, within the 12-day search window, at the $1,000–$1,350 budget. Based on AHG directory response rates and the Upwork screening filter, an unqualified candidate pool at this budget in a 12-day window is a realistic scenario.

### Trigger Thresholds

- **June 15 EOD**: No contract signed → solo fallback activates
- **June 17 EOD**: Hard deadline — no contractor engagement after this date regardless of status
- **Early trigger (user preemption)**: If by June 10 the search has produced 0 qualified candidates (no one has passed the screening questions), the user may elect to activate solo fallback immediately rather than waiting for June 15. This is a sound decision — every day of solo fallback clarity before June 22 is a day of better sprint preparation.

### Detection Procedure

**June 10 (Day 5 of search)**:
- Assess candidate pipeline honestly: How many candidates have passed screening questions? How many interviews are scheduled?
- Log in WORKLOG.md: "June 10 — Candidate pipeline: [X] candidates, [Y] passed screening, [Z] interviews scheduled. Trajectory: [On track for contract by June 12 / At risk — escalation needed / Solo fallback likely]."

**June 12 (Day 7 of search)**:
- If no contract signed AND no interview scheduled with a passing candidate: log "June 12 — Solo fallback trajectory confirmed. Activating June 15 per Decision Tree."
- Begin mental shift to solo planning NOW — the sprint begins in 10 days.

**June 15 EOD (Formal activation)**:
- Log: "June 15 EOD — Solo fallback activated. Sprint scope: 5 bundles, 12 hrs/week, June 22 – September 24. Per PHASE_3_CONTRACTOR_DECISION_TREE.md Solo Fallback Schedule."

### Escalation Criteria

**Proactive activation** (before June 15): If the candidate pipeline is empty and no escalation action has produced a lead by June 12, activate solo fallback on June 12 rather than waiting. The 3 additional days are better spent on sprint preparation (pre-staging Wikimedia images, completing the attribution log, loading Canva palette) than on a contractor search that is unlikely to close.

**Do not activate solo fallback and continue contractor search simultaneously**: The two approaches require different sprint planning mindsets. Once solo fallback is activated, stop the contractor search. The exception is if a Tier A candidate emerges unsolicited after activation but before June 17 — in that case, review their vetting score and make a one-time go/no-go call per the Decision Tree.

### Mitigation Actions

**Pre-sprint (parallel preparation)**:
- Regardless of contractor search outcome, complete all solo-sprint preparation before June 22: pre-stage CC images, load Canva palette, complete attribution log, finalize content outlines for all 5 bundles. This preparation is identical whether a contractor is engaged or not.
- Solo fallback requires no additional materials that are not already prepared for the contractor-assisted sprint.

**Cognitive preparation**:
- If solo fallback activates, the sprint pace is 12 hours per week — not 5 hours per day. This is a deliberate pace reduction from the contractor-assisted model. The total content produced is the same; the timeline is longer (9 weeks vs. 4–5 weeks). Acknowledge this trade-off explicitly in WORKLOG.md on activation day.

**Revenue context**:
- The solo fallback delays Respiratory by 7 days, Sleep by 21 days, and Immunity by 28 days vs. the contractor-assisted model. At $20–$22 per bundle and estimated 3–8 organic views/day with 3–5% conversion, the revenue impact of the solo fallback vs. contractor model is approximately $100–$200 in delayed first-month revenue. This is the cost of a 12-day search that did not produce a qualified contractor. It is not a catastrophic outcome.

**Ownership**: User. Activate proactively if pipeline is empty by June 12.

---

## Register Review Schedule

This register is a living document. Review at each sprint checkpoint and update the "Current Status" column.

| Checkpoint | Date | Review Scope |
|---|---|---|
| Pre-sprint | June 21 | All 8 risks — pre-staging confirmation |
| Sprint Day 1 | June 22 | Risk 1 (contractor active), Risk 2 (images staged), Risk 3 (scope freeze ready) |
| D3 Pace Gate | June 24 | Risk 3 (Women's Health scope), Risk 7 (pace) |
| D8 Women's Health Upload | June 29 | Risk 2 (images confirmed), Risk 4 (FTC pass confirmed before upload) |
| D14 Week 2 Checkpoint | July 5 | Risk 7 (Immunity and Sleep word counts), Risk 1 (contractor status) |
| D15 Respiratory Upload | July 6 | Risk 1 (contractor delivered Respiratory?), Risk 4 (Echinacea At-Risk sidebar present) |
| D18 FTC Review | July 9 | Risk 4 (all bundles reviewed) |
| D22 Sprint Close | July 13 | All risks — final log entry and retrospective |

---

*Prepared: June 5, 2026. Cross-references: PHASE_3_CRITICAL_PATH_ANALYSIS_JUNE22_JULY13.md (pace gate, upload dates, float inventory), PHASE_3_CONTRACTOR_DECISION_TREE.md (dropout recovery, solo fallback procedures), PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md (vetting rubric, backup roster), PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md (FTC Quick Reference, contraindication register, CITES sidebar verbatim). Version 1.0.*
