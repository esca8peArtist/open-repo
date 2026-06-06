---
title: "Phase 3 Comprehensive Risk Register — Production Sprint Risk Mitigation Playbook"
date: 2026-06-05
version: 1.1
status: production-ready
sprint-window: June 22 – August 3, 2026 (contractor model) | June 22 – September 24, 2026 (solo fallback)
decision-deadline: June 15, 2026 EOD (contractor go/no-go)
cross-references:
  - PHASE_3_PRODUCTION_SPRINT_RISK_REGISTER.md (predecessor risk register v1.0)
  - PHASE_3_CONTRACTOR_DECISION_TREE.md (contractor lifecycle decision tree)
  - PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md (search channels, vetting rubric)
  - PHASE_3_CRITICAL_PATH_ANALYSIS_JUNE22_JULY13.md (critical path, upload dates)
  - PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md (9-week solo timeline — companion doc)
  - PHASE_3_CONTRACTOR_DECISION_ESCALATION_FRAMEWORK.md (June 15 go/no-go tree — companion doc)
tags: [seedwarden, phase-3, risk-register, mitigation, contractor, production, sprint, escalation]
---

# Phase 3 Comprehensive Risk Register
## Production Sprint Risk Mitigation Playbook

**Prepared**: June 5, 2026
**Scope**: 8 risks spanning contractor lifecycle, content production, image sourcing, scope integrity, compliance, scheduling, and solo fallback decision. This register consolidates and deepens the June 5 risk inventory in PHASE_3_PRODUCTION_SPRINT_RISK_REGISTER.md with per-risk detection procedures, weekly checkpoint criteria, escalation triggers, and three-tier mitigation actions (pre-launch, in-sprint, post-sprint).

**Risk scoring methodology**:
- Probability (P): percentage likelihood of occurrence during June 5 – September 24 window
- Impact (I): CRITICAL = launch date or practitioner revenue ceiling affected; HIGH = upload date or content quality floor affected; MEDIUM = schedule slip or cost increase without launch impact; LOW = absorbed by float
- Composite priority = P × I category; CRITICAL impact risks receive daily monitoring regardless of P

**Review schedule**: Day 1 (June 22), Day 3 pace gate (June 24), Day 8 Women's Health upload (June 29), Day 15 Respiratory upload (July 6), Day 18 FTC review (July 9), Day 22 sprint close (July 13), solo fallback Week 2 (July 5), Week 3 (July 12), Week 5 (July 26).

---

## Risk Register Summary

| # | Risk Name | P | I | Composite | Critical Path Touch | Detection Method | Escalation Threshold |
|---|---|---|---|---|---|---|---|
| 1 | Contractor Dropout | 15% | CRITICAL | HIGH priority | Yes — Respiratory/Immunity/Digestive delivery | 3-day email silence | Day 1 of silence: follow-up; Day 3: assume dropout |
| 2 | Image Sourcing Delay | 20% | HIGH | HIGH priority | No — 5-14 day float | June 21 image audit pass/fail | 0 images per bundle confirmed by June 21 EOD |
| 3 | Women's Health Scope Creep | 10% | CRITICAL | HIGH priority | Yes — zero float; June 29 upload | Section word count >110% target | Day 2 checkpoint: activate scope freeze |
| 4 | Contraindication Research Gaps | 10% | HIGH | MEDIUM priority | Partial — FTC review at D18 | Peer review flags; self-edit pass | Any unverified Tier 2 interaction |
| 5 | Payment Delays | 5% | MEDIUM | LOW priority | No | Invoice 5+ days past acceptance | Contractor sends payment follow-up |
| 6 | Scope Expansion Mid-Sprint | 20% | MEDIUM | MEDIUM priority | Indirect | New bundle request during sprint | Any new bundle concept raised during June 22–July 13 |
| 7 | Deadline Compression Week 2–3 | 15% | HIGH | HIGH priority | Yes — Immunity and Sleep upload dates | Day 14 word count vs. 75% threshold | Either bundle <75% target at July 5 EOD |
| 8 | Solo Fallback Decision Cascade | 20% | HIGH | HIGH priority | Yes — all Phase 3 upload dates | June 10 pipeline assessment | 0 qualified candidates June 10 EOD |

---

## Risk 1: Contractor Dropout

**Probability**: 15%
**Impact**: CRITICAL
**Composite**: High priority — daily monitoring from contract signing

**Description**: A confirmed contractor becomes unresponsive or explicitly withdraws during the sprint (June 22 – August 1). Primary causes: health emergency, competing engagement accepted simultaneously, scope misalignment discovered after sprint begins, rate dispute triggered by revision feedback. The 15% figure reflects typical freelance dropout rates (10–20%) for 4–6 week engagements; herbalist writers who have invested in credentials self-select for commitment, moderating this downward.

**Critical path impact**: Direct. The contractor writes Respiratory (3,600w, due July 1), Immunity (3,800w, due July 8), and Digestive (3,600w, due July 20). Dropout before July 1 requires user absorption of all three bundles, cascading all upload dates 7–28 days.

### Detection Procedure

**Daily (June 22 – August 1)**:
- Check email inbox for contractor communication. Log last contact date in WORKLOG.md.
- Entry format: "[Date] — Contractor last contact: [date/description]. Silent days: [n]."

**Day 1 of 3-day silence**:
- Send: "Checking in on [bundle] progress — status update?" Log: "Day 1 silence. Follow-up sent."

**Day 2 of 3-day silence**:
- Send second email AND attempt phone contact if number provided in contract.
- Log: "Day 2 silence. Second contact attempt."

**Day 3 of 3-day silence (trigger confirmed)**:
- Assume dropout. Do not wait for further response.
- Log: "[Date] — Contractor assumed dropout. Mid-sprint recovery activated immediately."
- Begin mid-sprint recovery (see Mitigation Actions).

**At each scheduled delivery date (July 1, July 8, July 20)**:
- If draft not received AND no communication explaining delay: treat as Day 1 of silence protocol, not a separate process. The silence clock may already be at Day 2 or 3.

### Weekly Checkpoint Criteria

| Checkpoint | Date | What to Check | Pass Threshold | Fail Action |
|---|---|---|---|---|
| Pre-sprint | June 21 | Contract signed, deposit paid, briefing package delivered | All three confirmed | Escalate contractor search immediately; solo fallback within 24 hours if no candidate |
| Sprint D1 | June 22 | Briefing call completed; contractor confirms Respiratory start | Written confirmation of start | Flag: monitor daily with no gap |
| D3 Pace Gate | June 24 | Email contractor: word count on Respiratory? | 800+ words by D3 | Below 800: flag; not crisis yet but watch |
| D7 | June 28 | Respiratory first draft received? | Draft in inbox | Not received, no communication: activate silence protocol immediately |
| D15 | July 6 | Immunity draft on track per July 8 delivery date | Written confirmation July 3–4 | No confirmation by July 4: Day 1 silence protocol |
| D22 | July 13 | Digestive in progress; Immunity revision complete | Written status update | Silence: Day 1 protocol |

### Escalation Criteria

- 3-day silence at any point: assume dropout, begin recovery immediately
- Delivery date missed without prior communication: same as Day 3 silence
- Contractor explicitly withdraws: move to recovery same day, do not negotiate for continuation unless dropout reason is verifiable and scope is >50% remaining
- Re-engagement after dropout: only if verifiable reason (documented illness), >50% scope remaining, and new delivery dates do not compress FTC review below 48 hours per bundle

### Mitigation Actions

**Pre-launch (prevention)**:
- Contract dropout clause: "Milestones paid only for delivered and accepted work. Unused milestones cancelled. Advance deposit non-refundable." Explicit.
- Require phone number and emergency contact in contract.
- Maintain a Tier B runner-up candidate on standby through July 1. Contact within 24 hours of dropout confirmation.
- Briefing package delivered June 13–14 (pre-sprint) so contractor has 8 days of prep before writing begins.

**In-sprint (recovery)**:
- Dropout before July 1: user absorbs Respiratory immediately. Solo cascade schedule from PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md activates. Upload dates cascade: Respiratory July 13, Sleep August 3, Immunity August 17, Digestive September 24.
- Dropout after July 1 but before July 8: user performs revision pass on delivered Respiratory draft (2–4 hours). Immunity and Digestive shift to solo pace. Immunity uploads July 27; Digestive uploads August 17.
- Do not source a replacement contractor after July 8 — insufficient onboarding time for remaining scope.
- Payment on dropout: forfeit unused milestones. If partial draft delivered, assess quality; pay partial milestone only if draft is publishable after user revision.

**Post-sprint (learning)**:
- Log the dropout reason and any early warning signals missed. Add to contractor vetting rubric: weight communication responsiveness in the interview scoring.

**Ownership**: User. Monitor daily. Activate recovery without deliberation at Day 3 silence.

---

## Risk 2: Image Sourcing Delay

**Probability**: 20%
**Impact**: HIGH
**Composite**: High priority pre-sprint; medium in-sprint (float absorbs most scenarios)

**Description**: Studio photography (dried herbs flat-lay, June 17–21) is delayed by supplier delivery slip, AND no CC-licensed alternatives are pre-staged. The two-failure condition is the actual risk — either failure alone is recoverable because Wikimedia Commons CC-BY-SA sources cover all 14 sprint species. A 20% probability reflects MRH delivery delays (~15–25% in peak periods) combined with the risk of incomplete pre-staging.

**Critical path impact**: Indirect. Photography has 5–14 days of float per bundle. The image sourcing risk becomes critical only if CC pre-staging was not completed before June 21 AND studio photography is delayed. Slot 1 (cover hero image) is the only image with a hard upload-day dependency.

### Detection Procedure

**June 18 (Day 3 after MRH order)**:
- Check Mountain Rose Herbs order status. Confirm tracking number in inbox.
- If no tracking: email MRH order support with order number. Request tracking within 24 hours.
- Log: "June 18 — MRH order status: [confirmed shipped / not yet shipped — follow-up sent]."

**June 21 EOD — Pre-sprint image audit**:
- Open PHOTO_ATTRIBUTION_LOG.md.
- Verify: at least 1 CC-licensed image per bundle confirmed with attribution text.
- Any bundle with 0 images: run Wikimedia Commons sourcing sprint (30 minutes per bundle maximum).
- Log: "June 21 — Image audit: [bundle list confirmed / bundle list needing sourcing]."

**Each upload day (June 29, July 6, July 13)**:
- 5-minute check: Slot 1 image uploaded and thumbnail crops correctly (170×135px) before scheduling listing.

### Weekly Checkpoint Criteria

| Checkpoint | Date | What to Check | Pass Threshold | Fail Action |
|---|---|---|---|---|
| Pre-sprint | June 21 | CC images per bundle logged in PHOTO_ATTRIBUTION_LOG.md | 1+ confirmed per bundle | Source Wikimedia immediately (30 min per bundle) |
| MRH order | June 18–19 | Shipping confirmation received | Tracking number in inbox | Place Frontier Co-op emergency order same day |
| Women's Health upload | June 29 | Slot 1 image uploaded | Thumbnail renders correctly | Switch to confirmed CC image; studio photo added in listing update within 2 weeks |
| Respiratory upload | July 6 | Same | Same | Same |
| Sleep upload | July 13 | Same | Same | Same |

### Escalation Criteria

- MRH not shipped by June 19: Frontier Co-op emergency order same day. Expected delivery June 24–26. Photography shifts to Sprint Days 2–4 (June 23–25). Zero impact on June 29 Women's Health upload.
- Both MRH and Frontier Co-op delayed beyond June 25: activate full CC-only mode. All listing images sourced from Wikimedia Commons and iNaturalist. Pre-planned fallback — all 14 species have verified CC-BY-SA sources. Activate without hesitation.
- Goldenseal image: source cultivated specimen from University of Michigan Herbarium records or USDA PLANTS database. Verify CC license before logging. Do not photograph wild specimens.

### Mitigation Actions

**Pre-launch**:
- Pre-stage Wikimedia Commons CC-BY-SA images for all 14 species before June 21. Log filenames, URLs, photographer, license, and attribution text in PHOTO_ATTRIBUTION_LOG.md. This is the single action that eliminates this risk entirely.
- CC sourcing procedure per bundle: commons.wikimedia.org/wiki/Special:Search → "[Species name] medicinal" → filter CC-BY-SA → confirm 1 full-plant habit photo + 1 leaf/flower close-up per bundle.
- MRH order placed June 15. Stage Frontier Co-op account (free, no minimum) before June 15 as backup.

**In-sprint**:
- If studio photography complete: supplement CC images with studio flat-lays in Slots 2–3 (intended production plan).
- If studio not complete by upload date: publish with CC images in all slots. Add studio images via listing update within 2 weeks. Etsy listing updates do not reset review count or listing age.

**Post-sprint**:
- Log all CC attributions used in final PHOTO_ATTRIBUTION_LOG.md. Archive studio photos taken for v1.1 listing upgrades.

**Ownership**: User. Pre-staging is a pre-sprint action (30-minute per bundle, completable June 7–21). In-sprint monitoring is 5 minutes per upload day.

---

## Risk 3: Women's Health Scope Creep

**Probability**: 10%
**Impact**: CRITICAL
**Composite**: High priority — zero float; daily monitoring June 22–28

**Description**: The Women's Health bundle expands beyond its defined word count during Days 1–3, consuming pace buffer and pushing the June 24 pace gate and June 29 upload date. This is the highest-severity execution risk of the sprint because Women's Health has zero float: PDF export must be complete by June 28, upload at June 29 9–10am ET. A 2-day slip cascades all subsequent upload dates.

The 10% probability reflects: scope creep on the first bundle of a writing sprint is common when the structural template is being built for the first time. The Black Cohosh conservation sidebar (150-word hard limit) and Vitex invasive-species framing are the two highest-risk expansion points.

**Critical path impact**: Direct. Women's Health is the critical path anchor (zero float). A 2-day slip = Respiratory slips from July 6 to July 8, Sleep from July 13 to July 15.

### Detection Procedure

**End of each writing session (Days 1–3)**:
- Word count check per section. Compare against section targets in PHASE_3_BUNDLE_CONTENT_OUTLINE_DETAILED.md.
- Entry format: "[Date] — WH session: Black Cohosh [X]w (target 700). Vitex [Y]w (target 600). Total doc: [Z]w."
- If any section >110% target: scope freeze immediate. Note excess content in "v1.1 expansion notes" file.

**Day 2 checkpoint (June 23 EOD)**:
- Target: 1,200+ words (Black Cohosh + Red Clover complete or nearly complete).
- Below 900 words: Day 3 must produce 1,600 words to hit pace gate. Flag elevated risk in WORKLOG.md. Do not compress Day 3 with other tasks.

**Day 3 pace gate (June 24 EOD)**:
- Log: "D3 pace gate — Women's Health: [X] words. Gate: 2,500. Status: [PASS / FAIL]."
- FAIL: activate Option C immediately. Do not attempt to recover within the 5-bundle sprint.

### Escalation Criteria (Day 2 Checkpoint)

The Day 2 checkpoint is the critical escalation point — two days before the formal pace gate. If Women's Health is below 1,200 words at June 23 EOD:
1. Remove all non-writing tasks from June 24 schedule. No supplier coordination, no photography, no email before writing is complete.
2. Apply scope compression to Vitex (600w → 400w) and Red Clover (400w → 250w) to reclaim writing pace. The compression content becomes v1.1 expansion.
3. Write the Black Cohosh conservation sidebar in a separate document section; hard-stop at 165 words; paste into main document.

If Women's Health is below 2,500 words at June 24 EOD (formal pace gate failure):
- Log "D3 pace gate FAILED — Option C activated." Activate immediately — do not attempt recovery.
- Under Option C: Women's Health, Respiratory, Sleep proceed as planned. Immunity and Digestive defer to post-sprint.
- The pace gate failure is not a sprint cancellation. It is a scope correction with zero impact on the June 29 Women's Health upload.

### Mitigation Actions

**Pre-launch**:
- Section word targets written at the top of each Day 1–3 writing session document (not a mental note — a typed header).
- Black Cohosh conservation sidebar written in a dedicated file section. Hard-stop at 165 words regardless of incomplete thoughts.
- FTC Quick Reference and contraindication register open in browser tabs every writing session. Do not open additional database tabs during sessions — research is pre-compiled.

**In-sprint**:
- Scope freeze on first 110% overage. Move excess content to "v1.1 expansion notes." This is correct; the discomfort of cutting is the mitigation working.
- Scope compression cascade: Vitex 600w → 400w (remove invasive-species regional detail to a single sentence). Red Clover 400w → 250w (limit to isoflavone framing + forager edibility crossover note). These compressions preserve the core clinical content.

**Post-sprint**:
- v1.1 expansion notes from all compressed sections become the Phase 3 post-launch update list. Review at sprint retrospective July 13.

**Ownership**: User (Women's Health is user-written in all scenarios). Self-managed daily monitoring.

---

## Risk 4: Contraindication Research Gaps

**Probability**: 10%
**Impact**: HIGH
**Composite**: Medium priority — embedded detection reduces probability significantly

**Description**: A published bundle contains a missing or inaccurate contraindication — a drug interaction, pregnancy safety statement, or pediatric caution — discovered by a peer reviewer or practitioner buyer after the guide is live. This creates FTC liability, potential tort exposure, and reputational damage with the practitioner audience.

The 10% probability is low because of the pre-compiled FTC Quick Reference and mandatory contraindication register in PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md Appendix A. However, the Immunity bundle (Ashwagandha thyroid interaction, Goldenseal herb-drug interactions) and Sleep bundle (Valerian GABA-pathway potentiation, Passionflower MAOI interaction) carry the highest gap risk due to multi-pathway interaction profiles.

**Critical path impact**: Partial. The D18 FTC compliance review (July 9) is embedded in the sprint schedule. Post-launch discovery requires immediate listing update and PDF re-export (24–48 hour window).

### Detection Procedure

**Every writing session**:
- FTC Quick Reference table (PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md Appendix A) open in browser tab.
- Every therapeutic action claim checked against evidence tier before session ends.
- Every contraindication section cross-checked against NatMed Pro or MSK Integrative Medicine database before self-edit pass.

**Self-edit pass (per bundle)**:
- Order: contraindication sections first (highest liability), then evidence-tier language in therapeutic claims, then structural coherence.
- The mandatory contraindication register — Vitex (pregnancy, dopaminergic), Ashwagandha (thyroid axis, pregnancy), Valerian (CNS depressants, benzodiazepines), Passionflower (MAOI), Lemon Balm (TSH reduction, hypothyroidism) — is pasted verbatim, not paraphrased, into each relevant bundle.

**D18 FTC compliance review (July 9)**:
- Priority order: Women's Health → Immunity → Sleep → Respiratory → Digestive.
- Women's Health and Immunity are non-deferrable (highest FTC risk profiles).
- Respiratory and Digestive may defer to post-launch v1.1 if float is consumed, but only after critical bundles pass.

**Contractor bundle review (contractor model)**:
- User reviews all contractor-written contraindication content before releasing milestone payment.
- Immunity bundle: Ashwagandha thyroid warning must name the specific mechanism (withanolide activity on thyroid hormone axis) and must not use "generally safe" without qualification. Goldenseal CITES sidebar must be verbatim, not paraphrased.
- No contractor-written contraindication content is published without user sign-off.

### Escalation Criteria

- Any contraindication panel for Tier 2 or Tier 3 species that cannot be confirmed by two independent database sources: escalate to AHG peer reviewer or AANP directory naturopath for that specific section. Do not publish unverified Tier 2 contraindications.
- Post-launch identification of any contraindication error (by any source): update guide PDF within 24 hours, re-export, update Etsy listing immediately. Do not wait for scheduled review.
- Severe scenario (missed MAOI interaction for Passionflower in a sold guide): suspend listing immediately. Contact AHG reviewer for guidance on correction. This scenario is unlikely given the pre-compiled register but receives zero-delay treatment.

### Mitigation Actions

**Pre-launch**:
- Complete contraindication pre-compilation for all 14 sprint species before June 22 using NatMed Pro (primary) and MSK Integrative Medicine (cross-check). Log all interactions in species database with source URL and access date.
- Mandatory contraindication register for 5 highest-risk species compiled in Appendix A. Verbatim paste — no paraphrase.

**In-sprint**:
- FTC Quick Reference open every session. Not optional, not a sometimes-action.
- Contractor-submitted contraindication panels reviewed by user before milestone payment released.

**Post-sprint**:
- v1.1 update list: any Respiratory or Digestive sections deferred from D18 review are prioritized in the first post-sprint update.

**Ownership**: User retains final approval on all contraindication content — user-written and contractor-written.

---

## Risk 5: Payment Delays

**Probability**: 5%
**Impact**: MEDIUM
**Composite**: Low priority — simple calendar-based prevention

**Description**: A milestone payment to the contractor is delayed past the agreed date due to platform processing issues, banking delays, or user oversight. Creates contractor distrust, potential work stoppage, and relationship damage. The 5% probability is low because payment milestones are triggered by specific deliverable events.

**Critical path impact**: None directly — but work stoppage from payment non-receipt converts a MEDIUM risk to a de facto contractor dropout (Risk 1).

### Detection Procedure

**After each bundle draft is accepted**:
- Log immediately in WORKLOG.md: "[Date] — [Bundle] draft accepted. Milestone [2/3/4] payment due within 3 business days."
- Set calendar reminder for 3 business days after acceptance.
- If reminder fires and payment not sent: send immediately.

### Escalation Criteria

- 5 days past acceptance without payment: contact contractor proactively with payment confirmation and delay explanation. Do not wait for contractor to escalate. A credentialed contractor who is not paid on time has professional options that are more disruptive than a proactive explanation.

### Mitigation Actions

**Pre-launch**:
- Contract specifies payment window: "Milestones paid within 3 business days of written acceptance of each bundle draft." Contractual, not informal.
- Confirm payment method (PayPal, Wise, Upwork escrow) is funded and operational before contract signing. Stage the full contract amount ($1,000–$1,350) in the payment account before sprint Day 1.

**In-sprint**:
- Calendar reminder system: set on acceptance, not on delivery. Delivery ≠ acceptance; review may take 1–2 days.

**Ownership**: User. 3-business-day calendar reminder prevents this risk entirely.

---

## Risk 6: Scope Expansion Mid-Sprint

**Probability**: 20%
**Impact**: MEDIUM
**Composite**: Medium priority — self-enforced defer policy eliminates production impact

**Description**: A new bundle concept, product variant, or add-on is proposed or seems attractive during the sprint (June 22 – July 13) based on positive early sales data or herbalist outreach conversations. Adding scope mid-sprint without a formal decision process diverts writing time from committed bundles.

The 20% probability reflects sprint momentum patterns: positive Women's Health Etsy discovery creates pressure to add content; herbalist conversations surface bundle ideas that feel urgent. Both are normal. Both require the same response.

**Critical path impact**: Indirect. Scope expansion consumes writing time from committed bundles, which can push Women's Health (zero float) or Respiratory/Sleep (3–7 days float) into cascade territory.

### Detection Procedure

- Any new bundle concept raised during the sprint window: log the idea in WORKLOG.md immediately. Entry format: "[Date] — Scope expansion idea: [concept]. Deferred to Phase 4 queue." 30 seconds. No deliberation during sprint.

### Escalation Criteria

**Exception to defer policy** (all three must be true simultaneously):
1. The addition is a variant of an existing committed bundle (not a new species scope)
2. It requires fewer than 4 hours of additional writing time
3. It does not change any upload date

Example passing the exception: "Practitioner FAQ" appendix to Women's Health (same species, same FTC frame, 30–60 minutes). Example failing: "Digestive Health — Advanced Formulations" guide (new species scope).

### Mitigation Actions

**Pre-launch**:
- Log the defer policy in WORKLOG.md before June 22: "Phase 3 scope is fixed at 5 bundles. Any new bundle concept during the sprint is deferred to the Phase 4 queue. Policy active June 22 – July 13."

**In-sprint**:
- Maintain a running Phase 4 queue list. All deferred ideas go here — they are not dismissed, only deferred. The Phase 4 queue review at July 13 sprint retrospective determines which deferred ideas become Phase 4 scope.

**Post-sprint**:
- Review Phase 4 queue at sprint retrospective. Best ideas are scheduled; the remainder are archived.

**Ownership**: User. Self-enforced defer policy. No external monitoring needed.

---

## Risk 7: Deadline Compression Week 2–3

**Probability**: 15%
**Impact**: HIGH
**Composite**: High priority — Day 14 checkpoint is the formal escalation gate

**Description**: The Immunity + Sleep writing window (June 29 – July 5, Sprint Week 2) runs behind pace, compressing the July 5 milestone and creating risk on the July 6 Respiratory upload and July 13 Sleep upload. This is structurally distinct from Women's Health scope creep (Risk 3): it reflects Week 2's dual-track pressure — writing new bundles while simultaneously managing Women's Health promotion and Canva cover design.

**Critical path impact**: Yes — Immunity and Sleep are critical path items in the contractor sprint (Days 11–20). In solo fallback, this risk manifests as Week 3–4 compression.

### Detection Procedure

**July 2 EOD early warning (D11)**:
- Count Immunity words. Target: 2,500+ by July 2 (Goldenseal CITES sidebar should be drafting).
- Below 2,000: log "D11 early warning — Immunity at [X] vs. 2,500 target. Float Day 1 risk elevated."

**July 5 EOD formal checkpoint (D14)**:
- Count both Immunity and Sleep words.
- Pass threshold: Immunity 3,800 words (self-edited); Sleep 3,500 words (self-edited).
- Log: "D14 checkpoint — Immunity: [X] (target 3,800). Sleep: [X] (target 3,500). Status: [ON TRACK / BEHIND — cascade activated]."
- Below 75% on either bundle: activate scope reduction cascade immediately.

### Escalation Criteria

**Below 75% on either bundle at July 5 EOD**:
1. First reduction: Immunity — compress Echinacea section (Immunity-specific framing → condensed 300-word cross-reference to Respiratory bundle). Saves 500–600 words without losing clinical content.
2. Second reduction: Sleep — compress Lavender (second occurrence; reference Women's Health version) to 150 words. Saves 200–250 words.
3. Third reduction: If still behind after 1 and 2 — confirm Digestive deferral to August 3 (already the planned date; this is a schedule confirmation, not a new deferral). No Digestive acceleration in Week 3.

**Float Day 1 (July 12) activation**: Float Day 1 is reserved for Week 2–3 overruns. If Week 2 is behind: Float Day 1 consumed by Immunity or Sleep completion. July 13 Sleep upload proceeds from Float Day 1 completion the prior day.

### Mitigation Actions

**Pre-launch**:
- Schedule Women's Health promotional activities (email broadcast, Instagram, AHG responses) in the afternoon or evening of June 29 — not the morning. Morning of June 29 is Immunity writing start. Upload Women's Health at 9–10am ET, return to writing, handle promotion after 12pm.
- Canva cover sessions for Immunity and Sleep (June 29–30): 30-minute maximum per session. If over 30 minutes: switch to placeholder cover (existing template + color swap). Do not sacrifice writing time for cover polish.

**In-sprint**:
- Daily word count log in WORKLOG.md during Weeks 2–3: "[Date] — [Bundle]: [X] words. Session target: [Y]. Cumulative gap: [Z]." 5 minutes at end of each session.

**Post-sprint**:
- v1.1 expansion notes for any compressed sections (Immunity Echinacea cross-reference, Sleep Lavender reference) become a post-launch listing update.

**Ownership**: User. Float Day 1 is the primary structural mitigation; scope reduction cascade is the recovery action.

---

## Risk 8: Solo Fallback Decision Cascade

**Probability**: 20%
**Impact**: HIGH
**Composite**: High priority — proactive activation before June 15 is better than reactive activation

**Description**: No contractor is confirmed by June 15 EOD, triggering the solo fallback model. The risk is not the solo model itself — it is decision delay that allows the fallback to be triggered reactively at June 15 rather than proactively at June 10–12, leaving insufficient mental and operational preparation time before the June 22 sprint start.

The 20% probability reflects the challenge of finding a qualified herbalist writer with clinical contraindication depth, within a 12-day search window, at $1,000–$1,350. Based on AHG directory response rates and Upwork screening filter effectiveness, an empty qualified-candidate pipeline at this budget in 12 days is a realistic scenario.

**Critical path impact**: Yes — solo fallback shifts Respiratory from July 6 to July 13, Sleep from July 13 to August 3, Immunity from July 20 to August 17, Digestive from August 3 to September 24. Phase 4 start shifts from July 14 to October 1.

### Detection Procedure

**June 8 (Day 3 of search)**:
- Assess replies received across all channels. Log: "June 8 — Replies: [X]. Passed screening: [Y]. Interviews scheduled: [Z]."
- 0 replies: activate escalation (expand AHG second-tier contacts, activate Toptal, post revised Upwork listing, email Herbal Academy partnerships).

**June 10 (Day 5 of search)**:
- Assess pipeline honestly. Log: "June 10 — Pipeline: [X] candidates, [Y] passed screening, [Z] interviews scheduled. Trajectory: [On track / At risk / Solo fallback likely]."
- If 0 candidates have passed screening questions: solo fallback trajectory is confirmed. Begin mental shift to solo planning now — 12 days before sprint start.

**June 12 (Day 7 of search)**:
- No contract signed AND no interview scheduled with a passing candidate: log "June 12 — Solo fallback trajectory confirmed. Activating June 15 per decision tree."
- Do not wait for June 15 if pipeline is empty at June 12. Activate solo fallback June 12 if the case is clear — 3 additional days of sprint preparation are more valuable than 3 additional days of an empty search.

**June 15 EOD (Formal activation)**:
- No contract signed → activate solo fallback.
- Log: "June 15 EOD — Solo fallback activated. Sprint scope: 5 bundles, 12 hrs/week, June 22 – September 24."
- Stop contractor search. Do not run both planning tracks simultaneously.

### Escalation Criteria

- 0 qualified candidates at June 10: activate solo fallback on June 12 rather than June 15. The 3-day advantage in sprint preparation is worth more than the marginal probability of a qualified candidate emerging in days 8–10 of the search.
- Only 1 response by June 12 at above-ceiling rate ($1,500+): pursue Over-Budget Protocol (see PHASE_3_CONTRACTOR_DECISION_TREE.md Section: Over-Budget Protocol). If negotiation fails by June 14, activate solo fallback June 14.
- 2+ qualified responses by June 13: proceed to contract. Solo fallback concern is resolved.

### Mitigation Actions

**Pre-launch (parallel preparation)**:
- All solo-sprint preparation is identical to contractor-sprint preparation: pre-stage CC images, load Canva palette, complete attribution log, finalize content outlines for all 5 bundles. Complete this regardless of contractor search outcome. If contractor is engaged, the preparation cost is zero. If solo fallback activates, the preparation is already done.

**In-sprint (if solo fallback is active)**:
- Sprint pace is 12 hours per week — not 5 hours per day. Do not attempt to accelerate beyond 12 hours per week. The solo fallback is designed for sustainable pace across 9 weeks. Compressing it recreates the overload that motivated contractor sourcing.
- Revenue impact: ~$100–$200 in delayed first-month revenue across Respiratory, Sleep, and Immunity vs. contractor model. Not a catastrophic outcome.
- Full solo timeline detailed in PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md.

**Post-sprint**:
- Retrospective: document which search channels produced qualified leads vs. which were empty. Update contractor vetting approach for any future engagement (Phase 4 guide projects, Phase 5 API documentation).

**Ownership**: User. Activate proactively if pipeline is empty by June 12. Do not wait for June 15 if the trajectory is clear.

---

---

## Solo-Fallback-Specific Risks (Risks 9–13)

The following five risks apply only when solo fallback is active (no contractor confirmed by June 15 EOD). They are not monitored under the contractor model. If a contractor is engaged and performing, skip this section.

**Risk register update date**: June 6, 2026. These risks are added to v1.0 of this register to complete the Item 97 solo fallback risk assessment.

---

## Risk 9: User 12-Hr/Week Commitment Failure

**Probability**: 25%
**Impact**: CRITICAL
**Composite**: High priority — the solo fallback model collapses entirely if the 12-hr/week commitment cannot be sustained

**Description**: The user is unable to sustain 12 hours per week of writing, editing, and admin across the 9-week sprint (June 22 – September 24). Causes include: competing professional obligations that expand unexpectedly, health issues, burnout onset earlier than Week 6 (see Risk 10), or underestimation of the writing effort per session when confronted with the actual word count targets.

The 25% probability is the highest in this register for a reason: 108 hours of writing-equivalent work across 9 weeks is a significant time commitment, and the discipline required to protect 12 hours of writing per week against competing demands is routinely underestimated before a sprint begins. The probability is elevated relative to contractor dropout (15%) because commitment failure is user-controlled rather than externally triggered — it is a self-discipline and calendar-management risk rather than an external failure.

**Impact is CRITICAL** because there is no fallback from the solo fallback. If the contractor model is not available and the user cannot maintain pace, Phase 3 extends indefinitely. Unlike contractor dropout (which has a defined recovery: absorb scope + cascade dates), user pace failure has no defined recovery except timeline extension.

**Critical path impact**: Direct. A single week of 0 hours (vacation, illness, competing deadline) is recoverable — the 9-week schedule has no built-in float, but individual weeks running light (8–9 hours) do not cascade immediately. A second consecutive week below 6 hours activates the scope reduction cascades. Two weeks below 4 hours each is a sprint suspension scenario.

### Detection Procedure

**Every Friday (weekly check-in log)**:
- Log in WORKLOG.md: "[Week X, Date] — Hours this week: [X]. Cumulative hours: [Y]. On-track (12 hrs/week pace): [Yes / No — [gap] hours behind]."
- Entry takes 3 minutes. The act of logging creates accountability to a weekly target.

**Week 1 baseline (June 22–28)**:
- The first week's hour count sets the pace expectation. If Week 1 is below 9 hours: log "Week 1 below target. Diagnosing: [schedule conflict / underestimated task time / other]. Corrective action: [specific]."
- A Week 1 shortfall is the best time to detect commitment failure — not Week 4.

**Cumulative hour tracking**:
- By end of Week 2 (July 5): 24 cumulative hours expected. If below 18: pace failure is likely, not incidental.
- By end of Week 4 (July 19): 48 cumulative hours expected. If below 36: scope compression is required immediately regardless of which cascade is formally triggered.

### Escalation Criteria

**Week 1 below 9 hours**: Diagnose cause. One-time adjustment to Week 2 is acceptable. Log corrective action.

**Week 2 cumulative below 18 hours**: Activate Cascade 2 scope review (is Respiratory on track for July 13?). Log: "Week 2 pace shortfall — cumulative hours [X] vs. 24 expected. Cascade 2 review activated."

**Two consecutive weeks below 8 hours**: Sprint is at structural risk. Review the 9-week timeline against remaining scope. If Respiratory upload July 13 is at risk: user must decide between (a) protecting the next two weeks for sprint recovery, or (b) formally extending the solo timeline by 2 weeks across all remaining bundles.

**Three consecutive weeks below 8 hours (sprint suspension threshold)**: Log in WORKLOG.md: "Sprint suspension assessed [Date]. Consecutive light weeks: [X]. Remaining scope: [bundles + word count]. Decision: [Extend timeline / Resume with reduced scope / Pause Phase 3]." This is the only escalation that requires a user decision rather than an automatic cascade — because the cause may be a temporary external constraint (illness, job change, travel) that will resolve, or a permanent constraint that requires a Phase 3 scope revision.

### Mitigation Actions

**Pre-sprint (commitment design)**:
- Before June 22, block the weekly writing schedule in the user's calendar. Specific: 2 writing blocks of 3 hours each (Monday and Wednesday evenings, or Saturday + Sunday mornings — whatever fits the user's schedule), plus 1 admin block of 2 hours (Friday afternoon), plus 1 monitoring block of 1 hour (any day). Total: 9 writing + 2 admin + 1 monitoring = 12 hours. If these blocks cannot be placed before June 22, the solo fallback cannot proceed.
- Share the weekly schedule commitment with one person (partner, colleague, or accountability contact) before sprint Day 1. External accountability increases follow-through rate.

**In-sprint (pace recovery)**:
- If a week runs short (below 9 hours) due to a one-time conflict: make up the gap in the following week by adding one additional writing session. Do not carry gaps forward — they compound.
- If pace is structurally below target (consistent weekly shortfall): do not try to recover by adding hours. Instead, activate the appropriate cascade and extend the timeline. A 2-week extension of Phase 3 is a much better outcome than an 8-week sprint that produces 3 incomplete bundles.

**Post-sprint**:
- Log the actual hours per week vs. target in the sprint retrospective. This data is valuable for Phase 4 planning — it reveals the true sustainable writing pace for this project and user.

**Ownership**: User only. No external monitoring is possible. Self-accountability system + calendar blocking are the only pre-sprint mitigations.

---

## Risk 10: Burnout and Quality Degradation

**Probability**: 20%
**Impact**: HIGH
**Composite**: High priority — most likely to manifest in Weeks 6–7, which is the Immunity writing window

**Description**: 108 hours of writing-equivalent work across 9 weeks at 12 hrs/week is a sustained creative output commitment. Week 6 (late July) is the historically high-burnout point in writing sprints of this length: the novelty of the project has worn off, the end is not yet visible, and the material complexity is at its peak (Immunity bundle: Goldenseal CITES, Ashwagandha multi-pathway mechanism, Berberine evidence-tier complexity). Quality degradation manifests as: shortcutting contraindication research (using "commonly considered safe" instead of cited source), reduced self-edit rigor, and declining specificity in evidence-tier language.

**Impact is HIGH** (not CRITICAL) because quality degradation is detectable in the self-edit pass and correctable before publication. The risk is a higher revision burden in Weeks 7–8, not an uncorrectable published error.

**Critical path impact**: Partial. Quality degradation that reaches publication affects FTC exposure (if therapeutic claims lose evidence-tier framing) and practitioner credibility (if contraindications are incomplete). The D18 FTC review (July 9 in contractor sprint; approximately September 8 in solo sprint) is the final catch before publication.

### Detection Procedure

**Self-edit quality signal (per bundle)**:
- After each self-edit pass: log in WORKLOG.md: "[Bundle] self-edit quality signal: [Green (found <3 issues) / Yellow (3–7 issues) / Red (8+ issues, or found a missing mandatory contraindication)]."
- A "Red" self-edit signal is not a crisis — it is the self-edit working correctly. It indicates the draft was written under pace pressure. Resolve before FTC review.
- Two consecutive "Red" self-edit signals (e.g., Immunity and Sleep both Red) indicate burnout-related quality decline. Log and activate mitigation.

**Week 5 quality checkpoint (July 26 EOD, concurrent with pace checkpoint)**:
- Read 500 words of the Immunity bundle (the Ashwagandha section) aloud. Is the evidence-tier language specific and source-cited, or general and hedged?
- If the section reads "Ashwagandha is commonly used to support stress response and is generally well-tolerated" with no mechanism or source citation: quality degradation is active. The contraindication register must be present and verbatim, not paraphrased.

**Optional professional editor check (Week 5)**:
- If Week 5 quality signals are Yellow or Red: consider a 1-hour consultation with a professional editor or AHG peer reviewer to review the Immunity bundle draft. This is not a paid editing service — it is a phone call asking: "Does this read like a practitioner-grade guide or a general wellness summary?" A peer reviewer from the pre-sprint recruitment campaign would be appropriate. Cost: $0 if the relationship is established; $50–$100 for a brief paid consultation.

### Escalation Criteria

**Two consecutive Red self-edit signals**: Schedule a 2-day writing break before the next bundle starts. This is not optional. Log: "[Date] — Burnout signal: two consecutive Red self-edits. 2-day break before [next bundle] start. No writing [date 1] and [date 2]." A 2-day break in a 9-week sprint does not cascade dates — the schedule has daily flexibility even if it has no weekly float.

**Week 5 evidence-tier quality failure**: Activate the Week 5 optional editor check described above before beginning Immunity export. Do not publish Immunity if the Ashwagandha section fails the read-aloud test.

**Phase 3 quality floor definition**: The minimum acceptable quality for any published bundle is: every contraindication is source-cited (not paraphrased), every therapeutic claim uses correct evidence-tier language (not "shown to treat" or "cures"), and every CITES-flagged species has the sidebar present. Below this floor: do not publish. Extend the timeline rather than publish a substandard bundle.

### Mitigation Actions

**Pre-sprint (burnout prevention)**:
- Schedule one full non-writing day per week before June 22. This is structural. The 12-hr/week model requires one full off day per week — not an option. Log it in the calendar next to the writing blocks.
- Plan a 2-day voluntary break in Week 5 or Week 6 (schedule flexibility allows this — it only shifts Week 6 tasks by 2 days within the same week). Knowing the break is coming reduces the "infinite sprint" feeling that drives burnout.

**In-sprint (quality maintenance)**:
- Read the mandatory contraindication register aloud at the start of each Immunity and Sleep writing session. 5 minutes. This is not research — it is rehearsal. Hearing the specific mechanism language (withanolide activity on thyroid hormone axis) keeps the specificity standard active in working memory during the session.
- Do not edit and write in the same session. If the session goal is writing: write. If the session goal is self-edit: edit only. Mixing the two modes under pace pressure drives quality decline.

**Post-sprint**:
- Log the self-edit quality signals for all 5 bundles in the sprint retrospective. This reveals which species or topics drove the most quality pressure — useful for Phase 4 writing scope planning.

**Ownership**: User. Burnout prevention is pre-sprint structural (calendar blocking); burnout detection is in-sprint self-monitoring (weekly quality log).

---

## Risk 11: Image Sourcing Becomes Blocking (Solo Model Elevated Probability)

**Probability**: 30%
**Impact**: HIGH
**Composite**: High priority — elevated from the contractor model's 20% because the user is solely responsible for both image sourcing and all writing

**Description**: In the contractor model, image sourcing is a parallel task — the user sources images while the contractor writes content. In the solo model, both tasks compete for the same 12 hours per week. The risk is that image sourcing (Mountain Rose Herbs delivery, Wikimedia Commons pre-staging, photography session) consumes writing time during Weeks 1–2, delaying Women's Health below the June 24 pace gate.

The 30% probability is elevated because: (a) solo model image tasks are not offloaded to a parallel agent, (b) the pre-sprint photography window (June 17–21) is 5 days before sprint Day 1 — any photography delay bleeds directly into Week 1 writing time if it is not resolved by June 21, and (c) the Wikimedia Commons pre-staging (30 minutes per bundle × 5 bundles = 2.5 hours) is easy to defer and easy to forget.

**Impact is HIGH** because image sourcing blocking in Week 1 threatens Women's Health pace and the June 29 upload date — the zero-float event that anchors the entire solo sprint.

### Detection Procedure

**June 18 (supplier check)**:
- Mountain Rose Herbs order status: tracking number confirmed? If not: email MRH support same day. Log: "June 18 — MRH order: [tracking confirmed / follow-up sent]."

**June 21 EOD (pre-sprint image audit)**:
- Open PHOTO_ATTRIBUTION_LOG.md. Confirm: 1 CC-licensed image per bundle confirmed with attribution text.
- Any bundle with 0 confirmed images: run Wikimedia sourcing sprint immediately (30 minutes per bundle maximum).
- Log: "June 21 — Image audit: [X of 5 bundles confirmed]. [Bundles needing sourcing: list]."
- If any bundle still has 0 images after the June 21 sourcing sprint: this is a Day 1 task (June 22 first 30 minutes before writing begins). Not a cascade trigger — a pre-writing task.

**Week 1 daily check (June 22–28)**:
- Has any image sourcing task consumed more than 1 hour of writing time this week? If yes: log the hour diversion. If image sourcing has consumed more than 2 hours in Week 1: activate full CC-only mode for all remaining bundles immediately. No more photography preparation until Women's Health is uploaded June 29.

### Escalation Criteria

**MRH not shipped by June 19**: Frontier Co-op emergency order same day. Photography shifts to Sprint Days 2–4 (June 23–25). Zero impact on June 29 Women's Health upload — the photography session is for Etsy listing enhancement, not a publication requirement.

**Both MRH and Frontier Co-op delayed past June 25**: Activate full CC-only mode for all 5 bundles. All listing images sourced from Wikimedia Commons and iNaturalist. This is a pre-planned fallback — all 14 species have verified CC-BY-SA sources. Activate without deliberation and return writing time to Week 1.

**Image sourcing consuming 3+ hours of Week 1 writing time**: Activate CC-only mode for all 5 bundles regardless of supplier delivery status. The writing pace cannot absorb 3+ hours of image work during Women's Health production. Photography is the quality upgrade; CC images are the floor. Activate the floor and protect the writing.

**Solo model rule**: Image sourcing time in Weeks 1–3 comes exclusively from the 1-hour monitoring budget, not from writing or admin time. If image sourcing needs more than 1 hour in a given week, it is deferred to the following week or replaced with CC-only images. Writing hours are protected.

### Mitigation Actions

**Pre-sprint (eliminates the risk)**:
- Complete Wikimedia Commons CC-BY-SA pre-staging for all 14 species before June 21. One 2.5-hour session (30 minutes per bundle × 5 bundles). Log all filenames, URLs, photographers, licenses, and attribution texts in PHOTO_ATTRIBUTION_LOG.md. When this is done, image sourcing becomes a quality enhancement activity (studio photos = upgrade over CC floor), not a production requirement. The risk drops from HIGH to LOW.
- This is the single most important pre-sprint action for solo fallback image risk mitigation.

**In-sprint**:
- Solo model rule (above): image sourcing from 1-hour monitoring budget only.
- If CC pre-staging was not completed by June 21: do it on Sprint Day 1 morning, before Women's Health writing begins. 2.5 hours, done. Then begin Women's Health writing. The June 24 pace gate applies from Day 1 regardless — this is the correct order of priorities.

**Post-sprint**:
- Log actual image sourcing hours per week. This data is valuable for Phase 4 habit photo planning (18 species × 30 min per species = 9 hours of pre-staging in Phase 4).

**Ownership**: User. Pre-sprint CC pre-staging eliminates this risk. The risk is active only if pre-staging was not completed by June 21.

---

## Risk 12: Scope Drift — Additional Bundles Requested Mid-Sprint

**Probability**: 15%
**Impact**: MEDIUM
**Composite**: Medium priority — self-enforced defer policy eliminates production impact if applied consistently

**Description**: During the solo sprint (June 22 – September 24), a new bundle concept is proposed or seems compelling based on early Etsy analytics, practitioner outreach conversations, or AHG Symposium (August 14–16) feedback. In the solo model, any mid-sprint scope addition is more damaging than in the contractor model: there is no contractor absorbing scope, and the 12-hr/week ceiling has no slack. Even a "quick" additional bundle (2,500 words) represents at least 2.5 weeks of solo writing time at the 9-hr/week writing pace — not 2 or 3 extra hours.

The 15% probability reflects: AHG Symposium (August 14–16) is the highest-risk scope expansion event. Herbalist practitioner feedback at the Symposium often surfaces specific needs ("I wish you had a guide specifically on nervines for pediatric anxiety" or "an allergy guide would be huge") that feel like immediate opportunities. They are Phase 4 scope, not Phase 3 scope.

**Impact is MEDIUM** because the defer policy completely eliminates production impact if applied — the risk is in the moment of psychological pressure to act, not in any technical constraint.

### Detection Procedure

**Trigger**: Any new bundle concept raised during June 22 – September 24.

**Immediate response**:
1. Log in WORKLOG.md: "[Date] — Scope expansion idea: [concept]. Deferred to Phase 4 queue. No evaluation until September 24 retrospective."
2. This takes 30 seconds. No deliberation during the sprint. The act of logging — with the date, the concept, and the word "Deferred" — is the entire detection and response procedure.

**AHG Symposium specific (August 14–16)**:
- Expect 2–4 bundle ideas to surface from practitioner conversations.
- Pre-write the response in WORKLOG.md before the Symposium: "AHG Symposium [Date] — all new bundle concepts from this event are deferred to Phase 4. Log below." Then list them during the event.
- Do not act on any Symposium bundle ideas before September 24. This is a pre-authorized decision, not a per-idea judgment call.

### Escalation Criteria

**Exception to defer policy** (identical to contractor model — all three must be true simultaneously):
1. The addition is a variant of an existing committed bundle (not a new species scope)
2. It requires fewer than 4 hours of additional writing time
3. It does not change any upload date

**Solo model additional condition**: The exception applies only if the current week is on pace (cumulative hours within 2 hours of target). If pace is behind, no exceptions regardless of the quality of the idea.

**If exception is claimed**: Log the three conditions explicitly in WORKLOG.md before acting. This friction is intentional — if writing out the three conditions feels cumbersome, the exception does not qualify.

### Mitigation Actions

**Pre-sprint**:
- Log the defer policy in WORKLOG.md before June 22 (identical to contractor model): "Phase 3 scope is fixed at 5 bundles (Women's Health, Respiratory, Immunity, Sleep, Digestive). Any new bundle concept during the sprint is deferred to the Phase 4 queue. Policy active June 22 – September 24."
- Maintain a running Phase 4 queue. Ideas go there — they are not dismissed. The queue review at the September 24 sprint retrospective is the first point at which deferred ideas are evaluated.

**In-sprint**:
- AHG Symposium pre-logging (described in Detection Procedure above).
- If the defer policy feels in conflict with a genuinely urgent market opportunity: log the idea in the Phase 4 queue AND assess whether it can be executed entirely within existing Week 9 extended window (August 17 – September 24) without affecting the Digestive upload. If it can (e.g., a 1-page practitioner FAQ appended to the Women's Health listing, not a new bundle): apply the exception criteria.

**Post-sprint**:
- Review the Phase 4 queue at the sprint retrospective. The best-ranked ideas from the sprint become Phase 4 scope. AHG Symposium ideas specifically should be compared against Phase 4 revenue projections to prioritize by market pull.

**Ownership**: User. Self-enforced defer policy. No external monitoring needed.

---

## Risk 13: Technical and Publishing Delays

**Probability**: 10%
**Impact**: MEDIUM
**Composite**: Medium priority — known recovery procedures exist for all scenarios

**Description**: PDF export failure, Etsy listing scheduling error, Canva export issues, or website formatting problems delay the publication of a bundle past its upload date. In the contractor model, the user has 4–5 upload events over 6 weeks (1 per week); in the solo model, the user has 5 upload events over 14 weeks with less schedule density — but each upload is still a technical process with multiple failure points.

The 10% probability reflects: Canva PDF export issues (incorrect bleed, font substitution) occur in approximately 10–15% of first-run exports. Etsy listing scheduling errors (wrong price tier, incorrect file attachment) occur in approximately 5% of first-time listings on a new listing type. PDF accessibility issues (corrupted hyperlinks, incorrect page ordering) occur rarely but require a full re-export.

**Impact is MEDIUM** because technical failures are recoverable within 24–48 hours in all scenarios. No technical failure has ever permanently prevented a listing upload — the risk is delay, not cancellation.

**Critical path impact**: Women's Health is the only upload where a technical failure has CRITICAL impact — a 48-hour recovery on June 29 pushes Women's Health to July 1, which breaks the zero-float constraint. All other bundle upload dates have 3–7 days of soft buffer in the solo model before they affect the next bundle's pace.

### Detection Procedure

**Dry-run publications (pre-scheduled)**:
- Week 1 (June 22–28): dry-run the full export-to-Etsy workflow using a test PDF. Specifically: export a 5-page test document from Canva → verify PDF renders in all readers → upload to a private/unlisted Etsy draft listing → confirm thumbnail and file download work. This takes 45 minutes. If the workflow has an error, discovering it June 22–28 (not June 29) is worth 45 minutes.
- Week 3 (July 6–12): second dry-run using the Respiratory PDF. This is not optional for the Respiratory bundle — it is the first full export from the bundle template.
- Week 8 (August 10–16): third dry-run using Immunity PDF. By this point the workflow is internalized, but the Immunity bundle is the highest-complexity export (Goldenseal CITES sidebar, multi-species contraindication register) and warrants a pre-upload check.

**Export checklist (per bundle, day before upload)**:
The export checklist lives in the existing PHASE_3_PRODUCTION_LAUNCH_CHECKLIST.md. The solo model adds one item: "PDF renders correctly in Acrobat Reader AND in a mobile PDF reader (iOS Files app or Google Drive PDF viewer) before scheduling the listing."

**June 29 Women's Health upload specific**:
- The export must be complete by June 28 EOD (the day before). This gives a 1-day buffer for any technical issue discovered on the night of June 28. If export is not complete by June 28 EOD: this is not a technical failure — it is a pace failure (Risk 9 or Risk 3). Diagnose the correct risk.
- If export is complete June 28 but a technical issue is discovered during the June 29 upload attempt: resolve within 2 hours. If unresolvable in 2 hours: publish with the best available PDF and update the listing within 48 hours. Do not delay the listing by more than 24 hours for a formatting issue.

### Escalation Criteria

**Canva export failure (font substitution or bleed error)**:
- First response: re-export using "Flatten PDF" option in Canva. Resolves 70% of font substitution issues.
- Second response: if re-export fails, export as PNG × page and reassemble using a free PDF assembler (Smallpdf, ILovePDF). Time: 20–30 minutes. This is a slower process but produces a correct PDF.
- Third response: if PNG-to-PDF assembly produces a file above Etsy's 20MB limit: compress using PDF compressor. Then upload.

**Etsy listing error (wrong file attached)**:
- Etsy listing files can be replaced without resetting the listing. Edit the listing → upload the correct file → save. The listing does not go back to draft status. Resolution: 5 minutes.

**Etsy scheduling failure (listing not visible at scheduled time)**:
- Check listing status: is it in "scheduled" or "active" state? If scheduled but not yet active: wait until the scheduled time. Etsy scheduling delays are typically 0–15 minutes.
- If listing is showing as "draft" when it should be active: manually activate from the listing manager. This is a 2-minute action.

### Mitigation Actions

**Pre-sprint**:
- Dry-run the full export-to-Etsy workflow before June 22 using a test document. This eliminates the highest-probability technical failure (first-export errors) before it can affect Women's Health.
- Confirm Etsy seller account status and all payment settings are active before June 22. A suspended or limited Etsy account on June 29 is a CRITICAL technical failure with no same-day resolution.

**In-sprint**:
- Three dry-run export sessions (Weeks 1, 3, 8) as described in Detection Procedure.
- Export each bundle 1 day before the upload date (Day 6 of the writing week, not Day 7). This gives a 1-day buffer for technical recovery.

**Post-sprint**:
- Log all technical issues encountered during the sprint in the retrospective. Canva-specific issues are particularly worth documenting — they tend to recur across exports with the same template.

**Ownership**: User. Pre-sprint dry run and 1-day export buffer eliminate the majority of technical risk.

---

## Updated Risk Register Summary (13 Risks)

| # | Risk Name | P | I | Composite | Model | Escalation Threshold |
|---|---|---|---|---|---|---|
| 1 | Contractor Dropout | 15% | CRITICAL | HIGH | Contractor only | 3-day email silence |
| 2 | Image Sourcing Delay | 20% | HIGH | HIGH | Both | 0 images per bundle by June 21 EOD |
| 3 | Women's Health Scope Creep | 10% | CRITICAL | HIGH | Both | Section word count >110% target |
| 4 | Contraindication Research Gaps | 10% | HIGH | MEDIUM | Both | Unverified Tier 2 interaction |
| 5 | Payment Delays | 5% | MEDIUM | LOW | Contractor only | Invoice 5+ days past acceptance |
| 6 | Scope Expansion Mid-Sprint | 20% | MEDIUM | MEDIUM | Both | Any new bundle concept raised |
| 7 | Deadline Compression Week 2–3 | 15% | HIGH | HIGH | Both | Either bundle <75% target at July 5 EOD |
| 8 | Solo Fallback Decision Cascade | 20% | HIGH | HIGH | Pre-sprint | 0 qualified candidates June 10 EOD |
| 9 | User 12-Hr/Week Commitment Failure | 25% | CRITICAL | HIGH | Solo only | Week 2 cumulative below 18 hours |
| 10 | Burnout and Quality Degradation | 20% | HIGH | HIGH | Solo only | Two consecutive Red self-edit signals |
| 11 | Image Sourcing Blocking (Solo) | 30% | HIGH | HIGH | Solo only | 3+ hours of Week 1 writing time consumed by images |
| 12 | Scope Drift — Additional Bundles | 15% | MEDIUM | MEDIUM | Solo only | Any new bundle concept raised during sprint |
| 13 | Technical and Publishing Delays | 10% | MEDIUM | MEDIUM | Both | Export or Etsy failure on upload day |

**Solo fallback monitoring priority**: Risks 9, 10, and 11 are the highest-probability risks in the solo model. Risk 9 (commitment failure) is detected weekly. Risk 10 (burnout) is detected per-bundle self-edit. Risk 11 (image sourcing blocking) is eliminated by pre-sprint CC pre-staging.

---

## Critical Path Escalation Map

Women's Health (Days 1–3) is the only activity in Phase 3 with zero float. All escalation decisions during June 22–24 flow through Women's Health status.

```
June 22 (D1) — Sprint begins
  |
  Check: Women's Health writing started?
  YES → monitor daily
  NO  → CRITICAL: remove all non-writing tasks immediately
  |
June 23 EOD (D2) — Day 2 Checkpoint
  |
  Check: WH word count 1,200+ words?
  YES → on track; standard monitoring continues
  NO  → ESCALATION:
          • Remove all non-writing tasks from June 24
          • Apply scope compression (Vitex 600→400w, Red Clover 400→250w)
          • Conservation sidebar hard-stop 165 words
          • No new database tabs opened; use pre-compiled references only
  |
June 24 EOD (D3) — Formal Pace Gate
  |
  Check: WH word count 2,500+ words?
  YES → Pace gate PASS; Risk 3 resolved; sprint proceeds 5-bundle
  NO  → Pace gate FAIL: activate Option C immediately
          • Log "D3 pace gate FAILED — Option C activated"
          • Immunity and Digestive deferred to post-sprint
          • Women's Health, Respiratory, Sleep proceed; upload dates preserved
  |
June 29 (D8) — Women's Health Upload
  |
  NO-FAIL PATH: Women's Health uploads at 9-10am ET → Revenue begins
  |
July 5 (D14) — Week 2 Checkpoint
  |
  Check: Immunity 3,800w + Sleep 3,500w (both self-edited)?
  YES → Sprint on track
  NO  → Below 75% on either: activate scope reduction cascade
          (see Risk 7 Escalation Criteria)
```

---

## Register Review Schedule

| Checkpoint | Date | Priority Risks | Review Action |
|---|---|---|---|
| Pre-sprint | June 21 | All 8 | Pre-staging confirmation; log status for all 8 |
| Sprint D1 | June 22 | 1, 2, 3 | Contractor confirmed active; images staged; scope freeze policy logged |
| D2 Checkpoint | June 23 | 3 | Women's Health word count; Day 2 escalation criteria |
| D3 Pace Gate | June 24 | 3, 7 | WH word count; pace gate pass/fail logged |
| D8 WH Upload | June 29 | 2, 4 | Slot 1 image uploaded; FTC pass before upload |
| D14 Week 2 | July 5 | 7, 1 | Immunity + Sleep word counts; contractor status |
| D15 Respiratory Upload | July 6 | 1, 4 | Contractor delivered Respiratory?; Echinacea At-Risk sidebar present |
| D18 FTC Review | July 9 | 4 | All bundles reviewed; Women's Health + Immunity non-deferrable |
| D22 Sprint Close | July 13 | All | Final log entry; retrospective; Phase 4 transition |
| Solo Week 2 | July 5 | 7, 8 | Respiratory draft in progress; 2,500w target by July 5 (solo) |
| Solo Week 3 | July 12 | 7 | Respiratory uploaded July 13; Sleep draft 2,000+ words |
| Solo Week 5 | July 26 | 7 | Sleep draft near complete; Immunity in full velocity |

---

*Prepared: June 5, 2026. Version 1.1 (June 6, 2026 — Risks 9–13 solo-fallback-specific risks added; updated summary table to 13 risks). Companion documents: PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md (9-week solo timeline v1.1, scope reduction cascades, Section 6b consolidated checkpoint criteria), PHASE_3_CONTRACTOR_DECISION_ESCALATION_FRAMEWORK.md (June 15 go/no-go decision tree, Phase 3→Phase 4 timeline impact). Cross-references: PHASE_3_PRODUCTION_SPRINT_RISK_REGISTER.md (predecessor v1.0, original 8 risks), PHASE_3_CONTRACTOR_DECISION_TREE.md, PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md, PHASE_3_CRITICAL_PATH_ANALYSIS_JUNE22_JULY13.md.*
