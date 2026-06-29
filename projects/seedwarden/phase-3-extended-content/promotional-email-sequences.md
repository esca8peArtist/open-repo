---
title: "Phase 3 Promotional Email Sequences — Tier Transitions + Seasonal Campaigns"
date: 2026-06-28
version: 1.0
status: production-ready
sprint-window: August 4 – December 31, 2026 (sustained engagement post-launch)
cross-references:
  - PHASE_3_BUNDLE_LAUNCH_EMAIL_SEQUENCES.md (launch email voice reference)
  - PHASE_3_LAUNCH_MARKETING_CALENDAR.md (base calendar and automation setup)
  - SEASONAL_PRICING_AND_PROMOTION_MODEL.md (Q4 pricing and promotion model)
  - KIT_EMAIL_LAUNCH_SEQUENCE.md (Kit automation setup reference)
  - phase-3-extended-content/landing-page-copy.md (CTA links and bundle copy)
---

# Phase 3 Promotional Email Sequences

**How to use**: This document contains copy-paste email templates organized by trigger type. Each sequence has automation logic notes — the trigger condition, segmentation rule, and send timing. Load into Kit as automations (not broadcasts), except where noted as "broadcast."

**Voice note**: All templates use the same educational-first voice as PHASE_3_BUNDLE_LAUNCH_EMAIL_SEQUENCES.md. No urgency manufacturing. No scarcity framing. The reader is an educated grower or practitioner who buys on information quality, not pressure.

**Compliance**: All health claim language uses "traditionally used for," "research suggests," or "clinical evidence supports." No disease treatment claims. FTC-compliant throughout.

**Automation platform**: All sequences are written for Kit (ConvertKit). Tag logic, trigger conditions, and segment references use Kit conventions. Adapt for Mailchimp or Klaviyo as needed — automation logic translates directly.

---

## SEQUENCE 1 — Free-to-Paid Transition (Lead Magnet Subscribers)

**Trigger**: Subscriber downloads free lead magnet (e.g., "5 Medicinal Herbs for Beginners" PDF or equivalent free guide)
**Segment**: New subscribers who have not purchased any bundle within 14 days of opt-in
**Sequence length**: 5 emails over 14 days
**Goal**: First purchase — any individual bundle ($20–$22)
**Kit tag to apply on download**: `lead-magnet-downloaded`
**Kit tag that pauses sequence**: `bundle-purchased` (any bundle)

---

### Email 1 — Welcome + Free Guide Delivery
**Send timing**: Immediately on opt-in (automation trigger)
**Subject**: "Your free guide — and why we wrote it the way we did"
**Preview text**: "The herb guide that explains the why, not just the what."

---

Hi there,

Your free guide is attached (or available at [LINK]).

Here is why we wrote it the way we did: most herb guides give you a list. This one gives you the framework underneath the list. You will find out why harvest timing changes therapeutic concentration — and why that means your store-bought dried herbs may be significantly less potent than the label implies.

That context is not a sales pitch. It is the information we wish we had when we started growing medicinal herbs.

Over the next two weeks, we will send you three more short notes covering things the free guide does not have space for: the distinction between acute remedies and long-term tonics, why Latin binomials matter even for home growers, and how to build a simple medicine cabinet from four herbs.

If you have a question about anything in the free guide — or about a herb you are already growing — hit reply. We read every response.

Seedwarden

---

**Automation note**: Attach or link the lead magnet PDF. Confirm delivery before sequence continues.

---

### Email 2 — Education: The Acute vs. Tonic Distinction
**Send timing**: Day 3 after opt-in
**Subject**: "The distinction that changes how every herb works"
**Preview text**: "Using a tonic when you need an acute remedy is why most herb protocols fail."

---

Hi there,

One concept from the Seedwarden guides that changes how you use every herb:

**Acute remedies**: Used at the onset of a specific symptom, for a short period (7–14 days). They act quickly. Echinacea at the first sign of upper respiratory symptoms. Valerian for an acute insomnia night. Peppermint for acute digestive cramping. These are fast-acting responses to a specific, temporary situation.

**Tonics**: Used consistently over months to build systemic resilience. Effect accumulates. Ashwagandha for cortisol and stress resilience needs a 2–3 month minimum to show measurable results. Astragalus for immune tone needs to start 8–12 weeks before the season you want protection from. Chaste tree berry for hormonal cycle support needs 3–6 months.

The mistake: using a tonic as an acute remedy (two capsules of ashwagandha tonight will not help your sleep tonight). Or using an acute remedy as a tonic (echinacea every day for prevention is not how the herb works and is not supported by the research).

This distinction is the first thing we cover in every Phase 3 bundle — because it determines whether your protocol will work before you start it.

The bundles go much deeper on this. The full Phase 3 series is available on Etsy: [ETSY_COLLECTION_LINK]

The most common entry point is whichever health area is most pressing for you right now: Women's Health, Sleep, Immunity, Respiratory, or Digestive.

Seedwarden

---

**Automation note**: Track clicks on [ETSY_COLLECTION_LINK]. Subscribers who click but do not purchase within 48 hours proceed to Email 3. Subscribers who purchase: apply `bundle-purchased` tag and pause this sequence; move to SEQUENCE 3 (Bundle-to-Full-Collection).

---

### Email 3 — Education: Why Latin Binomials Matter
**Send timing**: Day 6 after opt-in
**Subject**: "There are three species of echinacea. They are not interchangeable."
**Preview text**: "The common name 'chamomile' covers two plants with different phytochemistry."

---

Hi there,

One practical reason Latin names matter even if you never plan to use them socially:

**German chamomile (Matricaria chamomilla)** and **Roman chamomile (Chamaemelum nobile)** are both called "chamomile." They are different plants. German chamomile is higher in apigenin — the compound responsible for its anti-inflammatory and calming effects. Roman chamomile is higher in bisabolol — with different applications and a different flavor profile.

If you buy "chamomile" without knowing which species it is, you do not know what you bought.

This matters at three points:
- When you buy seeds or transplants (you want M. chamomilla for tea; C. nobile is more often used in aromatherapy)
- When you buy dried herb (the two species have different potency profiles)
- When you read a study — because most of the clinical research on chamomile's effects uses German chamomile, not Roman

We cover the species distinction for every herb in the Phase 3 guides — including the three echinacea species (purpurea, angustifolia, pallida), which have different alkylamide concentrations and different evidence profiles.

The Respiratory Health bundle covers the echinacea species distinction in full. $20 on Etsy: [RESPIRATORY_ETSY_LINK]

All five bundles are available individually: [ETSY_COLLECTION_LINK]

Seedwarden

---

**Automation note**: Personalize Etsy link recommendation based on subscriber tag if possible (e.g., if tagged `interest-sleep`, link to Sleep bundle). Kit's conditional content blocks can handle this if interest tags were set at opt-in.

---

### Email 4 — Social Proof: Community Testimonial
**Send timing**: Day 9 after opt-in
**Subject**: "What Maria figured out about sourcing Black Cohosh"
**Preview text**: "She was an experienced gardener. The conservation section was new to her."

---

Hi there,

A note from a reader in Pennsylvania, Zone 6:

"I am an experienced gardener but a complete beginner with medicinal herbs. I downloaded the Women's Health bundle first because I have been dealing with perimenopause symptoms for two years. The section on Black Cohosh alone changed how I think about sourcing. I had no idea it was a species with declining wild populations. Now I have a cultivated source and a planting plan for next spring."

— Maria T., Zone 6, Pennsylvania

[NAME PLACEHOLDER — replace with real testimonial when collected. See PHASE_3_TESTIMONIAL_COLLECTION_STRATEGY.md for process.]

Maria's response is what the guides are designed to produce: not just "I learned what this herb does" but "I now understand the sourcing context, the conservation status, and the growing plan that follows from that."

That shift — from herb user to herb grower — is what the Seedwarden series is built around.

If you are curious about the Women's Health bundle, it is available on Etsy at $22: [WOMENS_HEALTH_ETSY_LINK]

If Women's Health is not your primary interest, start with whichever bundle matches your most pressing health area: [ETSY_COLLECTION_LINK]

Seedwarden

---

**Automation note**: Replace testimonial placeholder with real testimonial from the collection process. If no testimonial is yet available, the placeholder framing is credible — leave as is and update later. Do not fabricate specific details.

---

### Email 5 — Soft Offer + Bundle Recommendation
**Send timing**: Day 14 after opt-in
**Subject**: "Which Seedwarden guide is right for you?"
**Preview text**: "A simple framework for choosing where to start."

---

Hi there,

You have been on the list for two weeks. This is the last email in the welcome series — and the most direct one.

If you have not downloaded a bundle yet, here is the framework for choosing where to start:

**If you are dealing with sleep or nervous system issues**: Start with Sleep & Nervines ($20). It covers the acute vs. tonic distinction in depth and includes the timing guidance (valerian 30 minutes before bed, not at dinner) that makes the protocol work.

**If you are growing or sourcing for immune support**: Start with Immunity Support ($22). It is the most seasonally relevant guide for anyone entering fall, and the astragalus tonic protocol needs to start 8 weeks before the season you want protection from.

**If respiratory health or lung support is your primary concern**: Start with Respiratory Health ($20). The elecampane and mullein coverage alone is worth the price for anyone who grows or sources for respiratory support.

**If hormonal health, menopause, or cycle support is your focus**: Start with Women's Health ($22). It is the most specialized guide in the series and the one with the most plant conservation depth.

**If digestion is your entry point**: Start with Digestive Support ($20). It connects your kitchen herbs to your medicinal herb practice — and shows how ginger, peppermint, and fennel are more effective when you understand their mechanisms.

**If you are a practitioner, student, or educator**: The Practitioner Tier ($120) includes Women's Health, Respiratory Health, and Immunity Support plus a Cross-Bundle Integration Reference with contraindication mapping and herb-herb synergies.

All guides are available on Etsy: [ETSY_COLLECTION_LINK]

If you have questions before purchasing — what the guide covers, whether it applies to your zone, what level of prior herb knowledge is assumed — reply to this email.

Seedwarden

---

**Automation note**: After Email 5, tag subscriber `welcome-series-complete`. If no purchase within 7 days of Email 5, tag `warm-non-purchaser` and enroll in the monthly educational newsletter (non-promotional). Do not continue sending promotional sequences to non-purchasers beyond 21 days — list health degrades with oversending.

---

## SEQUENCE 2 — Bundle Upgrade (Bundle-to-Full-Collection)

**Trigger**: Subscriber purchases any single bundle
**Segment**: Single-bundle purchasers (tag: `bundle-purchased`, exclude `practitioner-tier-purchased` and `collection-purchased`)
**Sequence length**: 3 emails over 21 days
**Goal**: Second bundle purchase or Practitioner Tier upgrade
**Kit tag to apply on trigger**: `bundle-upgrade-sequence-active`
**Kit tag that pauses sequence**: `practitioner-tier-purchased` OR second `bundle-purchased` tag applied

---

### Upgrade Email 1 — Companion Bundle
**Send timing**: Day 7 after first bundle purchase
**Subject**: "The guide that pairs with [BUNDLE NAME YOU PURCHASED]"
**Preview text**: "One herb appears in both — understanding its two different applications changes how you use it."

---

Hi there,

You downloaded [BUNDLE NAME]. This is the companion guide that builds on it.

[CONDITIONAL BLOCK — use the pairing that matches the purchased bundle]

**If Women's Health purchased**:
The companion is Sleep & Nervines. The hormonal cycle directly affects sleep quality — the follicular and luteal phases have different sleep disruption patterns, and different herbs respond better to each phase. The Sleep guide covers the nervine and adaptogenic side of what Women's Health introduces in Part 4.

→ Sleep & Nervines: $20 [SLEEP_ETSY_LINK]

**If Respiratory Health purchased**:
The companion is Immunity Support. Echinacea appears in both guides — as an aerial-part respiratory support herb in Respiratory, and as a root-based immune activator in Immunity. Understanding both applications of the same plant changes how you grow and prepare it.

→ Immunity Support: $22 [IMMUNITY_ETSY_LINK]

**If Sleep & Nervines purchased**:
The companion is Women's Health. Licorice root and motherwort — two herbs in Women's Health — have documented nervous system and hormonal effects that connect directly to the sleep quality issues covered in your Sleep guide. The cross-reference is explicit in Part 1 of Women's Health.

→ Women's Health: $22 [WOMENS_HEALTH_ETSY_LINK]

**If Immunity Support purchased**:
The companion is Respiratory Health. The season that demands your immune protocol (fall) is the same season where respiratory support herbs are most relevant. Both guides use echinacea; they cover different species applications and preparation methods. Together, they cover the complete upper respiratory and immune protocol.

→ Respiratory Health: $20 [RESPIRATORY_ETSY_LINK]

**If Digestive Support purchased**:
The companion is Immunity Support. Gut health and immune function are directly connected (70% of the immune system is gut-associated lymphoid tissue). The herbs in Digestive (calendula, licorice, chamomile) support gut integrity, which is foundational to the immune protocol in Immunity Support.

→ Immunity Support: $22 [IMMUNITY_ETSY_LINK]

[END CONDITIONAL BLOCK]

If you have questions about whether the companion guide covers your specific interest area, reply here.

Seedwarden

---

**Automation note**: Kit conditional content blocks handle the pairing logic if purchase tags are bundle-specific (e.g., `womens-health-purchased`, `respiratory-purchased`). If tagging is only `bundle-purchased` without specificity, this email requires manual segmentation or a simpler version without conditionals.

---

### Upgrade Email 2 — Practitioner Tier Pitch (for practitioners/students/educators)
**Send timing**: Day 14 after first bundle purchase
**Subject**: "If you are using these guides in a practice or teaching context, there is a tier for that"
**Preview text**: "The Cross-Bundle Integration Reference maps contraindications across 24 herbs — built for clinical use."

---

Hi there,

A follow-up question: are you using the Seedwarden guides in a practice, teaching, or education context?

If so, the Practitioner Tier may be a more appropriate fit than individual bundles.

The Practitioner Tier includes:
- Women's Health ($22 value)
- Respiratory Health ($20 value)
- Immunity Support ($22 value)
- Cross-Bundle Integration Reference (exclusive — not available separately)

The Cross-Bundle Integration Reference is the piece that makes the Practitioner Tier valuable for clinical and education use. It maps:
- Which herbs appear in multiple bundles with different applications (echinacea, ginger, licorice root — all appear twice)
- Herb-herb synergy combinations (which herbs enhance each other in a formula context)
- Contraindication index across all 24 herbs (fast reference before a patient appointment or student assignment)
- Complete Latin name index with family, common name, and page references across all three guides

This is the document that replaces the 30–45 minutes of pre-appointment synthesis from PDR for Herbal Medicines and individual monographs. One reference, pre-synthesized.

**Practitioner Tier price**: $120 (saves $44 vs. individual bundles). If you have already purchased one bundle, the credit applies informally — there is no formal trade-in, but the math is: $120 total vs. $64 (all three individually) plus the integration reference at no extra cost.

Educator volume licensing available for group classroom use (10+ learner contexts). Contact us for pricing.

[PRACTITIONER_TIER_ETSY_LINK]

Not a practitioner or educator? Skip this one — the individual bundles are the right fit for home growers.

Seedwarden

---

**Automation note**: This email converts best with subscribers tagged `herbalism-student`, `practitioner`, or `educator` at opt-in. If interest tags were not set, send to all single-bundle purchasers — the "Not a practitioner or educator? Skip this one" line explicitly releases non-relevant subscribers without creating friction.

---

### Upgrade Email 3 — Complete Collection Offer
**Send timing**: Day 21 after first bundle purchase
**Subject**: "One more note — and then we stop sending upgrade emails"
**Preview text**: "The complete Phase 3 series is five guides covering 40+ herbs."

---

Hi there,

This is the last email in the bundle upgrade series. After this, you will hear from us through the monthly educational newsletter — not upgrade prompts.

One final note: the complete Phase 3 series is five guides covering 40+ medicinal herbs.

If you have purchased one guide and are considering the others, the full set — purchased individually — is $104. There is no bulk discount at this tier (individual bundles are already priced to reflect full production cost). The Practitioner Tier ($120) is the only bundled offer, and it includes the Cross-Bundle Integration Reference.

If $104 for the complete set is outside your current budget, the most practical approach is to buy guides by health priority — start with the area that is most relevant to you right now, then add as budget allows.

The order that most readers find useful: start with Immunity or Women's Health (highest-demand, most complete coverage), then add Sleep or Respiratory depending on your second priority area, then Digestive.

All five guides: [ETSY_COLLECTION_LINK]

Practitioner Tier: [PRACTITIONER_TIER_ETSY_LINK]

Thank you for being part of the Seedwarden community.

Seedwarden

---

**Automation note**: After Email 3, tag `upgrade-sequence-complete`. Add to monthly newsletter if not already enrolled. Do not re-enroll in any upgrade sequence unless a major new product launches.

---

## SEQUENCE 3 — Seasonal Campaign: Pre-Fall Immunity Protocol (August 1–September 30)

**Trigger**: Broadcast to all subscribers who have NOT purchased Immunity Support bundle (tag: `NOT immunity-purchased`)
**Send type**: Broadcast (not automation — send once to the segment, timed to seasonal relevance)
**Campaign window**: Send in first week of August; repeat campaign in first week of September if not purchased
**Goal**: Immunity Support bundle purchase

---

### Seasonal Email A — August (Pre-Fall Entry)
**Send date**: August 4 (first Monday after Phase 3 launch period)
**Subject**: "Pre-fall immune prep starts now — not in October"
**Preview text**: "The herbs that build long-term immune tone take 8–12 weeks. August is the window."

---

Hi there,

Astragalus root takes 8–12 weeks of daily use before immune tone builds to a measurable level. Ashwagandha needs 8 weeks at minimum before cortisol response studies show adaptation. Elderberry syrup does not build immunity — it reduces symptom duration when illness starts. These are three different things.

The most common immunity mistake: starting the long-term tonic herbs in November, when respiratory illness season has already arrived. That is 8–12 weeks too late.

Pre-fall immune preparation starts in August.

**The Seedwarden Immunity Support bundle** covers exactly this protocol:
- Which herbs are rapid-response (echinacea, ginger, garlic — use at symptom onset)
- Which are long-term tonic (astragalus, ashwagandha — start now, build through the season)
- When to start astragalus broth for October protection
- How to layer these herbs without overlap or excess

It also covers the sourcing ethics of goldenseal (CITES Appendix II — wild harvest is not responsible) and the pesticide contamination in Chinese astragalus imports (and what certifications to look for).

Eight herbs. Cultivation, harvest, preparation, and safety.

**$22 on Etsy**: [IMMUNITY_ETSY_LINK]

August is the window. If you start reading this week and start your protocol within two weeks, you will be in protective range by October.

Seedwarden

---

**Automation note**: Apply tag `immunity-seasonal-email-A-sent`. Suppress from sending Seasonal Email B (September) if `immunity-purchased` tag is applied between August and September sends.

---

### Seasonal Email B — September (Season Urgency)
**Send date**: September 1 (Labor Day timing — if subscriber has not yet purchased Immunity bundle)
**Subject**: "September is the last window for full fall immune prep"
**Preview text**: "8 weeks from now is late October. That is when you want to be protected."

---

Hi there,

Eight weeks from the first of September is late October — the first respiratory illness season in most of North America.

If you started an astragalus tonic protocol two weeks ago, you will be at partial protective level by then. If you start today, you will reach it by late October. If you wait until November, the season will have already started.

We sent a note about this in August. If you missed it: the Immunity Support bundle covers which herbs build long-term immune tone (start now) versus which respond to acute symptoms (use when sick).

The complete guide is $22 on Etsy: [IMMUNITY_ETSY_LINK]

This is the last seasonal prompt we will send before fall arrives.

Seedwarden

---

**Automation note**: This is a one-time resend to August non-purchasers only. Do not send to new subscribers who joined after August 1 without sending Email A first — Email B assumes prior exposure. Apply tag `immunity-seasonal-email-B-sent` after send.

---

## SEQUENCE 4 — Seasonal Campaign: Winter Prep (October–November)

**Trigger**: Broadcast to all subscribers. Send regardless of prior purchase status — the framing shifts to "complete your collection" for existing customers and "start now" for non-customers.
**Send type**: Broadcast
**Campaign window**: October 1 and November 1 (two sends, spaced 30 days)
**Goal**: Any bundle purchase from non-customers; Complete Collection or Practitioner Tier from existing single-bundle customers

---

### Winter Prep Email A — October
**Send date**: October 1
**Subject**: "October is when the value of your herb knowledge pays off"
**Preview text**: "Growers who read Immunity Support in August are 4 weeks into their protocol now."

---

Hi there,

October is the dividend month for herb growers who prepared in August.

Growers who read the Immunity Support bundle in August started their astragalus protocol in August or September. They have now been on long-term immune support for 4–8 weeks — entering fall with their tonic herbs building. Growers who waited until October to read the guide are starting their protocol 4–8 weeks behind schedule.

This is not a scarcity note. These guides are permanent products and will be available in November too.

But the preparation window is real. And October is the last month where reading the Immunity or Respiratory bundles gives you time to build and preserve a winter supply.

**If you have not read the Immunity or Respiratory bundles**: now is the moment that gives you meaningful preparation time. Together, they cover the herbs for seasonal defense and upper respiratory support — cultivation to use, sourced from a garden you grow.

Immunity Support ($22) + Respiratory Health ($20) = $42: [ETSY_COLLECTION_LINK]

**If you have read one or two bundles**: the complete Phase 3 set is five guides for $104. October is when reading the remaining guides gives you the most practical seasonal return.

**If you have the complete set**: the winter preservation and storage protocols in Digestive, Immunity, and Respiratory apply directly to what you have harvested this fall. The guides are year-round references.

Seedwarden

---

**Automation note**: Apply tag `winter-prep-email-A-sent`. Track clicks by existing customers vs. non-customers to calibrate messaging in Email B.

---

### Winter Prep Email B — November
**Send date**: November 1
**Subject**: "November herb prep: what to start now, what you have missed, what still matters"
**Preview text**: "Some preparations are still timely. Some windows are closed. Here is the honest map."

---

Hi there,

November honestly: what herb prep is still timely, and what windows have closed.

**Still timely in November**:
- Tinctures in progress: if you started valerian, echinacea, or elderberry tinctures in September or October, they are ready to strain now or soon. Shake daily. Strain at 4–6 weeks.
- Astragalus tonic protocol: you are now 8+ weeks behind the August start. But starting in November still gives you 4 weeks of building before December — better than not starting.
- Dried herb purchases from responsible suppliers: if you did not grow your own this year, now is the time to stock up before Q4 demand raises prices on elderberry and echinacea.
- Reading the guides: the cultivation and preparation knowledge is year-round. Reading now means planting correctly next spring.

**Windows that have closed in most zones**:
- Aerial herb harvest (frost has occurred in zones 4–6)
- Root harvest (ground is hardening in zones 4–5)
- Fresh herb tinctures (plants are dormant; no fresh material available)

**What still makes sense**: stocking the reference library that changes how you approach next growing season. The Phase 3 series is five guides, $104 individually.

Immunity Support ($22) [IMMUNITY_ETSY_LINK]
Respiratory Health ($20) [RESPIRATORY_ETSY_LINK]
Sleep & Nervines ($20) [SLEEP_ETSY_LINK]
Women's Health ($22) [WOMENS_HEALTH_ETSY_LINK]
Digestive Support ($20) [DIGESTIVE_ETSY_LINK]

Seedwarden

---

**Automation note**: Apply tag `winter-prep-email-B-sent`. After November, shift promotional email cadence to Q4 seasonal model (see SEASONAL_PRICING_AND_PROMOTION_MODEL.md for Q4-A through Q4-E bundle launch sequences). Do not repromote Q3 bundles in December — focus shifts to gift and Q4 seasonal content.

---

## SEQUENCE 5 — Practitioner Tier: Back-to-School Push (August–September)

**Trigger**: Broadcast to subscribers tagged `herbalism-student`, `practitioner`, or `educator`
**Send type**: Broadcast — send August 11, with follow-up send September 8 for non-purchasers
**Segment**: Interest-tagged subscribers who have NOT purchased Practitioner Tier
**Goal**: Practitioner Tier purchase ($120)

---

### Practitioner Email A — August
**Send date**: August 11
**Subject**: "Herbalism school starts this month. This is the reference library your program will not provide."
**Preview text**: "Three guides + a cross-bundle integration reference, built for students who want practitioner-depth content."

---

Hi there,

September herbalism cohorts are starting now or in the coming weeks. The coursework will give you the framework. What most programs do not provide: a practitioner-depth reference that covers 24 herbs from cultivation through clinical safety.

The Seedwarden Practitioner Tier was built for this use case.

Three full guides:
- Women's Health — 8 herbs, cycle support, hormone balance, reproductive vitality
- Respiratory Health — 8 herbs, airways, expectorants, demulcents, seasonal prep
- Immunity Support — 8 herbs, rapid-response vs. long-term tonic, seasonal protocol

Plus a Cross-Bundle Integration Reference that maps:
- Which herbs appear across guides with different applications (echinacea in both Respiratory and Immunity — different plant parts, different preparation methods, different evidence profiles)
- Herb-herb synergy combinations
- Contraindication index across all 24 herbs
- Complete Latin name index for fast reference

This is not an introductory guide. It is the reference you bring to your second or third year of study — when your instructors start assigning primary sources and you need a synthesis document that has already done the cross-referencing.

**$120 on Etsy** — less than one clinical herbalism textbook, and significantly more actionable: [PRACTITIONER_TIER_ETSY_LINK]

Educator volume licensing available for classroom use (10+ learners). Contact us.

Seedwarden

---

### Practitioner Email B — September (non-purchaser resend)
**Send date**: September 8 (if Practitioner Tier not purchased after August 11 email)
**Subject**: "Two weeks into fall semester — still building your reference library?"
**Preview text**: "The contraindication mapping alone saves 45 minutes per patient appointment."

---

Hi there,

Two weeks into fall semester. If you are still building your reference library, a note from a clinical herbalist in Colorado who uses the Practitioner Tier:

"I have been compiling cross-herb contraindication information manually from PDR for Herbal Medicines for years. The Cross-Bundle Integration Reference in the Practitioner Tier is the first consumer-facing document that does this synthesis for 24 herbs in one place. It changed my pre-appointment prep time meaningfully."

— Dr. Sarah K., clinical herbalist, Colorado [PLACEHOLDER — replace with real testimonial]

The Practitioner Tier is $120. It includes Women's Health, Respiratory Health, Immunity Support, and the Cross-Bundle Integration Reference — exclusively available in this tier.

[PRACTITIONER_TIER_ETSY_LINK]

After September, the academic framing of this email shifts to a general practitioner pitch. If you are in a fall program, this month is when this purchase makes the most practical sense.

Seedwarden

---

**Automation note**: Apply tag `practitioner-back-to-school-sequence-complete` after Email B. Non-purchasers receive standard monthly newsletter. Do not re-enroll in practitioner sequence until Phase 4 Practitioner Advanced launch.

---

## Monthly Educational Newsletter — Non-Promotional Nurture

**Trigger**: All subscribers — enrolled after welcome series completes or after upgrade sequence completes
**Send type**: Monthly broadcast on the first Monday of each month
**Goal**: List health, community engagement, Phase 4 awareness-building
**Tone**: Pure education. No CTA required. Optional Etsy link at the footer only.

### Template Structure (copy-paste, customize monthly)

**Subject line template**: "[Month] Herb Calendar: [specific seasonal topic]"

*Examples*:
- "August Herb Calendar: the window for your last aerial harvest"
- "September Herb Calendar: root harvest season opens"
- "October Herb Calendar: what experienced foragers find in late fall"

---

**Body template**:

Hi there,

[MONTH TOPIC INTRO — 2-3 sentences connecting to the season or a specific plant event in the herb garden]

**This month in the herb garden** (zones 4–6):

[BULLET LIST — 5-7 specific, actionable items for the current month. Examples: harvest timing, preservation tasks, seed collection windows, planting dates, specific plant care notes]

**One herb to know this month**:

[HERB NAME (Latin binomial)] — [3-5 sentences: what it does, when to harvest or plant it this month, one fact that changes how you use or source it]

**From the Phase 3 guides**:

[1-2 sentences pointing to relevant bundle content for the month without being promotional. Example: "The Immunity Support bundle covers the astragalus tonic protocol in detail — including harvest timing and dosing by zone."]

Questions about what you are growing? Reply to this email.

Seedwarden

---

[FOOTER: Links to all five Etsy bundles — text links only, no images. "Full Phase 3 series available on Etsy: [ETSY_COLLECTION_LINK]"]

---

**Automation note**: Monthly newsletter is the long-term list health mechanism. It keeps the list warm without promotional pressure, reduces unsubscribes, and ensures that when Phase 4 launches, the list is receptive. Do not monetize the newsletter beyond the footer link. Open rates on educational newsletters are consistently 10–15 percentage points higher than promotional emails — this is the list quality investment.

---

## Automation Logic Summary

| Sequence | Trigger | Length | Goal | Pause Condition |
|---|---|---|---|---|
| 1: Free-to-Paid | Lead magnet download | 5 emails / 14 days | First bundle purchase | `bundle-purchased` tag |
| 2: Bundle Upgrade | First bundle purchase | 3 emails / 21 days | Second bundle or Practitioner Tier | `practitioner-tier-purchased` or 2nd `bundle-purchased` |
| 3: Pre-Fall Immunity | Broadcast, August + September | 2 sends | Immunity bundle | `immunity-purchased` tag |
| 4: Winter Prep | Broadcast, October + November | 2 sends | Any bundle or complete set | N/A (broadcast) |
| 5: Practitioner Back-to-School | Broadcast, August + September | 2 sends | Practitioner Tier | `practitioner-tier-purchased` |
| Monthly Newsletter | Ongoing, enrolled after sequences complete | Monthly | List health | Unsubscribe only |

---

## Customization Checklist (before each send)

- [ ] Replace all [BRACKETS] with live values (Etsy links, dates, names)
- [ ] Replace all testimonial [PLACEHOLDERS] with real testimonials if available (see PHASE_3_TESTIMONIAL_COLLECTION_STRATEGY.md)
- [ ] Test send to your own inbox at least 24 hours before scheduled send
- [ ] Verify all Etsy links are live (not draft) before send
- [ ] Confirm Kit automation tags are applied correctly (spot-check one test subscriber)
- [ ] Check subject line preview text renders correctly on mobile (Kit preview tool)
- [ ] Confirm FTC-compliant language throughout — no "treats," "cures," or disease diagnosis claims

---

*Prepared: June 28, 2026. All templates are FTC-compliant and use the same educational-first voice as PHASE_3_BUNDLE_LAUNCH_EMAIL_SEQUENCES.md. Automation logic is written for Kit (ConvertKit) but translates directly to Mailchimp, Klaviyo, or ActiveCampaign. Testimonial placeholder language throughout — replace with real testimonials when collected per the Testimonial Collection Strategy. Q4 seasonal campaigns (November gift bundles, holiday stress relief) are out of scope for this document — see SEASONAL_PRICING_AND_PROMOTION_MODEL.md for Q4-A through Q4-E launch sequences.*
