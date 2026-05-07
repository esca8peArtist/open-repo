---
title: "Phase 2 Customer Success & Retention Framework"
date: 2026-05-07
status: production-ready
scope: Phase 1→Phase 2 conversion modeling, customer segmentation, retention mechanics, Phase 3 go/no-go decision tree, dashboard designs, escalation logic
launch-date: 2026-05-30
phase-2-expansion-date: 2026-07-14 (approx. Day 45 post-launch)
phase-3-decision-date: 2026-07-29 (Day 60 checkpoint)
references:
  - phase-2-analytics-strategy.md (data architecture, cohort definitions, dashboard templates)
  - phase-2-buyer-retention-lifecycle-strategy.md (6-campaign email system, LTV model)
  - customer-cohort-analysis-framework.md (segment definitions, per-cohort messaging)
  - phase-3-decision-framework.md (Option A/B/C/D decision tree)
  - financial-sustainability-model.md (unit economics, break-even model)
  - analytics/monthly-metrics-checklist.md (operator runbook)
---

# Phase 2 Customer Success & Retention Framework

**Purpose**: Consolidate Phase 2 success measurement into a single decision-driving document.
This is not a supplement to the analytics or email system documents — it is the command layer
above them. It answers four questions that no other document answers directly: Which Phase 1
buyers are most likely to adopt Phase 2 products? How do we keep them? When do we trigger Phase
3? And what does "success" unambiguously mean at each checkpoint?

**Operating principle**: Real-time measurement from Day 1, not retrospective analysis after
the fact. Automated escalation, not a checklist the operator has to remember to check. Decision
clarity at every gate — no ambiguous "monitor and decide" language.

**Audience**: Anya, solo operator. Every framework, threshold, and trigger below is designed to
be operated by one person using Google Sheets, Kit, and Etsy Shop Manager. No engineering
required.

---

## Part 1: Phase 1 to Phase 2 Conversion Prediction Model

### 1.1 Baseline: What Phase 1 Tells Us

Phase 1 closed with 47 orders, $1,341 gross revenue, 2.24% conversion rate, and an average
order value of $28.54. Repeat purchase rate was approximately 14.9% at the 30-day mark. No
post-purchase email system existed — every buyer who did not return left without any retention
attempt.

These numbers are the prediction baseline. The question the model answers is: given what a
Phase 1 buyer purchased, how likely are they to buy a Phase 2 product within 60 days of the
Phase 2 launch?

### 1.2 Conversion Prediction Rules (Simple If/Then Model)

The model uses first-purchase product type as the primary predictor of Phase 2 adoption.
Secondary predictors are order depth (single guide vs. multi-guide) and cohort signal
(survey response or product-inferred). These rules are actionable immediately from the
existing LTV tracker without any statistical modeling.

**Rule Set 1: Product-to-Phase-2 Mapping**

Apply this to every Phase 1 buyer in the LTV tracker. For each buyer, identify their first
product and assign a Phase 2 adoption probability tier.

| First Purchase (Phase 1) | Predicted Phase 2 Product | Adoption Probability | Reasoning |
|---|---|---|---|
| Wild Edibles Quick Reference | Native Plants Regional Guide, Medicinal Herbs guide | High (35–50%) | Forager cohort: sequential botanical exploration path |
| Zone Calendar (any zone) | Adjacent zone bundle, Seed Saving Field Manual | High (30–45%) | Planning-to-execution project logic; natural next step |
| Seed Saving Field Manual | Companion Planting Chart, preservation guides | High (30–45%) | Homesteader project cadence; one action enables the next |
| Native Plants (regional guide) | Wild Edibles guide, endangered species guide | High (30–45%) | Botanical collector pattern; expands species depth |
| Hunting/Fishing Manual | Meat/Fish Preservation Manual | High (35–50%) | Direct sequential pairing; harvest-then-preserve logic |
| Any single guide at $14–22 | 3-guide bundle at 15% discount | Medium (20–30%) | Premium intent buyers have lower price resistance |
| Companion Planting Chart ($5–8) | Zone Calendar, seed saving guide | Medium (18–28%) | Entry-level price point; may convert to mid-tier next |
| Bundle (3+ guides, first order) | Additional bundle or premium guide | Medium (15–25%) | Bundle buyers are value-motivated; need new angle, not just more product |
| Any single guide at $5–9 | Any single guide (same price tier or adjacent) | Lower (10–18%) | Price-sensitive segment; second purchase requires active incentive |
| Gift season purchase (mobile, Nov–Dec) | No Phase 2 prediction — gift buyer window | Low (3–8%) | Gift buyer LTV ceiling is $55–60; Phase 2 adoption rare without gift window |

**How to use this table:**
1. Open the LTV tracker (`analytics/data/customer-ltv-tracker.csv`)
2. For each Phase 1 buyer with `first_order_date` before 2026-05-30, look up their
   `order_1_products` value
3. Assign a probability tier (High / Medium / Lower / Low) to a new column `phase2_adoption_tier`
4. Sum each tier: this gives you the predicted Phase 2 buyer pool before launch day

**Expected Phase 2 adoption from 47 Phase 1 buyers (modeled estimate):**
- High tier (approximately 12–15 buyers at 35–45% adoption): 4–7 Phase 2 purchases
- Medium tier (approximately 18–22 buyers at 18–28% adoption): 3–6 Phase 2 purchases
- Lower/Low tier (approximately 10–15 buyers at 3–18% adoption): 0–2 Phase 2 purchases

Total predicted Phase 2 purchases from Phase 1 base: 7–15 buyers, contributing $210–$450
in revenue at Phase 1 AOV ($28.54). These are baseline recoveries before new acquisition.

### 1.3 Order Depth as Secondary Predictor

Bulk buyers (defined as 5+ guides in a single Phase 1 order) behave differently from
single-guide buyers in ways that affect Phase 2 adoption.

**Bulk buyer (5+ guides, single order) characteristics:**
- Cohort inference: Almost exclusively Prepper or Forager
- Phase 2 adoption behavior: Lower adoption probability for Phase 2 (they already own
  most of the available catalog) but higher adoption of any genuinely new content — endangered
  species guides, medicinal herb guides, or phase-specific deep-dive products they could not
  have bought in Phase 1
- Recommended Phase 2 approach: Do not recommend bundles (they have a bundle). Recommend
  the one or two products they provably do not own yet, by name, in the cross-zone upsell
  email (Campaign 3). Personalization here is critical — a generic bundle recommendation
  will not convert a buyer who already bought the bundle

**Single-guide buyer at $20+ characteristics:**
- Phase 2 adoption probability: 25–35% (higher than bulk buyers because their "collection"
  is not complete)
- Recommended Phase 2 approach: Bundle introduction at 15% discount. The framing should
  emphasize completion of a system, not acquisition of more guides.

**Single-guide buyer at under $10 characteristics:**
- Phase 2 adoption probability: 10–18% (lower; price point indicates cost sensitivity)
- Recommended Phase 2 approach: Demonstrate value before making an offer. Campaign 2
  (Content Deepening) is more important for this segment than Campaign 3 (Upsell).
  The Campaign 5 seasonal win-back is the most realistic Phase 2 conversion vehicle
  for this segment — catching them at a high-motivation moment.

### 1.4 Kit Email Subscriber vs. Non-Subscriber Conversion Differential

The largest Phase 2 adoption driver is whether the Phase 1 buyer entered the Kit email
funnel. Based on industry benchmarks for post-purchase email sequences at comparable LTV:

- Phase 1 buyer who completed the welcome email sequence: Phase 2 adoption rate 2–3x
  higher than non-subscriber (estimated 30–45% adoption vs. 12–18%)
- Phase 1 buyer who received no email (not in Kit): Phase 2 adoption is entirely dependent
  on organic Etsy re-discovery

**Action**: Before Phase 2 launch (by May 28), check which Phase 1 buyers appear in the
Kit subscriber export. Flag the non-subscribers in the LTV tracker (`kit_subscriber = no`).
These buyers receive no Phase 2 lifecycle email — their re-engagement path is the
quarterly win-back (Campaign 5) only, which fires September 1 at the earliest.

---

## Part 2: Customer Segmentation Model

### 2.1 Five Segments: Characteristics, LTV Estimates, and Retention Risk

The four cohorts from `customer-cohort-analysis-framework.md` remain the primary segmentation
layer. Phase 2 adds a fifth: the Herbalist segment, activated by new medicinal herb guide
content. Below is a refined Phase 2 version of each segment with realistic LTV estimates
grounded in Phase 1 actuals and the lifecycle campaign model.

**Segment 1: High-Intent Forager**

Characteristics:
- Purchases: Wild edibles, native plants, regional guides, multi-guide orders in botanical
  categories
- Engagement depth: High email open rates (target 40%+), clicks on ecosystem content
- Geographic concentration: Pacific Northwest (Zones 7–8), Northeast (Zones 5–6),
  Upper Midwest (Zones 4–5)
- Purchase pattern: 2–4 purchases per year driven by seasonal foraging windows
- Typical entry order: $28–$40 (multi-guide or premium single guide)

LTV estimate — Phase 2:
- Without lifecycle campaigns: $28–$35 (near Phase 1 AOV; one-time purchase)
- With Campaign 1–3 active: $50–$70 (second purchase via cross-zone upsell within 45 days)
- With Campaign 6 VIP track (3+ purchases): $90–$120 (seasonal botanical collector pattern)
- 12-month LTV target: $60–$80

Retention risk factors:
- Low risk of churn if content remains botanically specific and zone-accurate
- Churn signal: Email open rate drops below 30% two sends in a row (content is no longer
  novel or relevant)
- Churn response: Introduce a new botanical category or endangered species angle; shift
  from general foraging tips to species-level identification content

**Segment 2: Survival Prepper**

Characteristics:
- Purchases: High-volume single orders (5+ guides), survival garden plans, hunting/fishing
  and preservation pairing
- Engagement depth: Lower email engagement than foragers (preppers are action-oriented,
  not content-curious); respond to urgency and scarcity framing
- Geographic distribution: More uniform nationally; rural overrepresentation
- Purchase pattern: 1–2 large purchases per year (bulk-buy mentality)
- Typical entry order: $50–$80 (bundle or multi-guide)

LTV estimate — Phase 2:
- Without lifecycle campaigns: $50–$80 (near first-order value; low repeat without trigger)
- With Campaign 4 event-triggered re-engagement: $70–$100 (seasonal or news-triggered
  win-back generates a second bulk purchase at similar value to first)
- With Campaign 5 fall seasonal send: $90–$110 (September fall prep content converts
  at 8–12% for this cohort at the right moment)
- 12-month LTV target: $75–$100

Retention risk factors:
- High churn risk if follow-up content is too botanical or lifestyle-oriented
- Churn signal: No email open within 21 days of purchase (typical prepper pattern)
- Churn response: Campaign 4 event-triggered email is the primary retention vehicle;
  fire it on news events or fall prep window rather than waiting for Day 45

**Segment 3: Homesteader (Largest Cohort)**

Characteristics:
- Purchases: Seed saving, zone calendars, companion planting, preservation guides — incremental
  acquisition project by project
- Engagement depth: Highest sustained email engagement of any cohort; highest newsletter
  open rates; seasonal content resonates strongly
- Geographic concentration: Vermont, Tennessee, Pacific NW, coastal California
- Purchase pattern: 2–4 purchases per year at 30–60 day intervals (project-driven cadence)
- Typical entry order: $18–$30 (one or two targeted guides per project phase)

LTV estimate — Phase 2:
- Without lifecycle campaigns: $35–$50 (natural repeat rate; homesteaders return on
  their own schedule)
- With Campaign 1–3 active and seasonal newsletter: $55–$75 (cross-zone upsell succeeds
  because homesteaders think in systems — the next guide is always the natural project step)
- With Campaign 6 VIP track: $90–$130 (highest 12-month LTV of any cohort through
  incremental, project-paced repeat purchasing)
- 12-month LTV target: $70–$100

Retention risk factors:
- Lowest churn risk of all cohorts; homesteaders are loyal if content stays practical
- Churn signal: Repeat purchase interval extends from 45 days to 90+ days (project stalled
  or no new project trigger)
- Churn response: Seasonal content that names the next project ("fall preservation window
  starts September 1 — here's what to prepare now")

**Segment 4: Gift Buyer**

Characteristics:
- Purchases: Premium single guides, bundles, any high-visual-value product in a gift window
- Engagement depth: Very low email engagement; opens gift-specific seasonal emails only
- Geographic distribution: Urban concentration; higher-income demographics
- Purchase pattern: 1–2 purchases per year tied to gifting occasions (Mother's Day, holiday)
- Typical entry order: $25–$40 (gift price point; presentable product)

LTV estimate — Phase 2:
- Without lifecycle campaigns: $25–$35 (single gift purchase; no return unless gifting
  occasion recurs)
- With Campaign 5 seasonal gift sends (May 15, November 15): $50–$65 (second gift
  purchase on next occasion — this is the primary retention mechanism for this cohort)
- 12-month LTV target: $45–$60

Retention risk factors:
- High churn risk by definition; gift buyers are occasion-driven, not product-driven
- Churn signal: No open on three consecutive seasonal sends
- Churn response: Annual-only sends from Campaign 5 sunset rule; do not attempt content
  relationship with gift buyers — the gifting occasion email is the only appropriate touchpoint

**Segment 5: Herbalist / Medicinal (New in Phase 2)**

Characteristics:
- Purchases: Medicinal herb guides, themed herb bundles (Women's Health, Respiratory,
  Immunity, Sleep, Digestive from Phase 3 roadmap), practitioner-oriented reference material
- Engagement depth: Highest click-through rate on medicinal content; researches before
  buying; highest time-on-listing
- Geographic concentration: Nationwide; slight concentration in herbalism-active cities
  (Asheville, Portland, Boulder, Brooklyn, Austin)
- Purchase pattern: Collector/researcher pattern — 3–5 purchases per year; builds a complete
  reference library
- Typical entry order: $20–$40 (medicinal herb guide or themed bundle)

LTV estimate — Phase 2:
- Without lifecycle campaigns: $40–$60 (strong initial purchase; returns if content quality
  is high)
- With Campaign 1–3 and medicinal-specific content deepening: $75–$100 (3+ purchases
  within 90 days common among practitioner-level herbalists)
- With Campaign 6 VIP track and Phase 3 practitioner bundles ($120–$180): $130–$200+
  (highest LTV ceiling of any segment if Phase 3 practitioner tier launches)
- 12-month LTV target: $90–$130

Retention risk factors:
- Churn risk if medicinal content is too generic or sends foraging tips to a practitioner
- Churn signal: No click on medicinal-category content links within first 3 emails
- Churn response: Immediately personalize to herbalist depth — species-level preparation
  content, dosage context, sourcing ethics. Generic botanical content will not retain this cohort

### 2.2 Cohort Identification Confidence Levels

Not every buyer will complete the post-purchase survey. The LTV tracker should record
confidence level alongside the cohort assignment.

| Confidence Level | Source | Notes |
|---|---|---|
| High | Post-purchase survey response | Buyer self-identified; overrides product inference |
| Medium | Product purchased + email click behavior | Two signals aligned; reliable for targeting |
| Low | Product purchased only, no survey | Single signal; use for targeting but watch for contradicting behavior |
| Unknown | No survey, no behavioral signal yet | Assign to general newsletter; reclassify at 30-day email behavior review |

The "Unknown" category should fall below 15% of the buyer base by Day 30. If it exceeds 20%
at Day 30, the post-purchase survey delivery mechanism is not reaching buyers — check the
Kit automation and Etsy order confirmation CTA.

### 2.3 Segment LTV Comparison Summary

| Segment | 30-Day LTV | 90-Day LTV | 12-Month LTV | Phase 3 Upside |
|---|---|---|---|---|
| High-Intent Forager | $28–$40 | $50–$70 | $60–$80 | Endangered species guides, regional deep-dives |
| Survival Prepper | $50–$80 | $70–$100 | $75–$100 | Preservation derivatives, Master Preserver bundle |
| Homesteader | $18–$30 | $55–$75 | $70–$100 | Seed Library System, Homestead Skills Roadmap |
| Gift Buyer | $25–$40 | $30–$45 | $45–$60 | Holiday gift bundles ($62 Expanded Homesteader Set) |
| Herbalist | $20–$40 | $75–$100 | $90–$130 | Phase 3 practitioner bundles ($120–$180) |

**Prioritization implication**: Herbalist and Homesteader have the highest 12-month LTV and
the highest Phase 3 upside. Acquisition spend (time on content, SEO, Pinterest pinning) should
shift toward these two cohorts by Month 2 if their combined share reaches 40%+ of buyers.

---

## Part 3: Retention Mechanics Hypothesis

### 3.1 Why Customers Stay: Four Drivers

The following are the primary retention drivers for Seedwarden's buyer base, ranked by
expected impact. These are hypotheses to validate with Phase 2 data, not confirmed facts.

**Driver 1: Seasonal content relevance (highest impact)**

Hypothesis: Buyers return when content is seasonally specific to their zone and activity.
The "next-step" foraging or homesteading action is the most reliable re-purchase trigger
because it matches the buyer's natural activity cycle rather than Seedwarden's sales calendar.

Measurement: Track which email sends correlate with Etsy order spikes in the 48 hours
following delivery. If fall seed-saving content drives re-purchases, this validates the
seasonal driver hypothesis.

Validation threshold: If 3 or more consecutive seasonal emails (Campaign 2 or newsletter)
each correlate with a measurable order spike (2x above daily average on the same day or
next day), seasonal content is confirmed as the primary retention driver. Invest accordingly:
seasonal newsletters become the highest-priority content work.

**Driver 2: Content depth and specificity (second highest impact)**

Hypothesis: Buyers who receive genuinely useful botanical content stay subscribed and return.
Generic "gardening tips" content will not retain foragers or herbalists. Zone-specific,
species-level content with practical application will.

Measurement: Compare email click rates between generic content emails and zone-specific
content emails. If zone-specific emails generate 2x+ higher click rates, content depth is
a confirmed retention driver.

**Driver 3: Email nurture cadence (moderate impact)**

Hypothesis: The 6-campaign lifecycle sequence maintains purchase intent between natural
buying windows. Without it, the average interval between purchases is 60–90 days (natural
project cadence); with it, that interval compresses to 30–45 days.

Measurement: Compare 30-day repeat purchase rate for Kit subscribers vs. non-subscribers
(buyers who did not join the email list). If subscriber repeat rate is 2x+ non-subscriber
rate at 30 days, email nurture is confirmed as a significant driver.

**Driver 4: Community identity (lower initial impact, grows over time)**

Hypothesis: Buyers who identify with the "forager/homesteader/herbalist" identity framing in
Seedwarden's content develop brand loyalty that outlasts any single product purchase. The VIP
track naming ("Herbalist Inner Circle" / "Seed Keeper's Guild") is designed to activate this.

Measurement: Tracked only through VIP engagement retention (target 60%+ of VIP subscribers
opening in any 30-day window) and NPS/voice-of-customer survey feedback. Community identity
is the hardest driver to measure quantitatively but generates the highest LTV ceiling.

### 3.2 What Drives Repeat Purchases

Repeat purchases at Seedwarden follow three observable patterns:

**Pattern A: Project-step purchasing (Homesteader, Herbalist)**
Buyer completes one project (plants Zone 7 spring garden using Zone Calendar), sees the
natural next step (seed saving at harvest), buys the Seed Saving Field Manual. Each purchase
enables the next. The email cross-sell (Campaign 3) should surface this connection explicitly:
"You used the Zone Calendar to plan your spring garden. Here's what comes next in your harvest."

**Pattern B: Seasonal window purchasing (Forager, Prepper)**
Buyer returns when a seasonal foraging or preservation window opens. The spring morel window,
fall mushroom season, harvest preservation season — these are external triggers the buyer
feels regardless of whether Seedwarden sends an email. The email's job is to be in the inbox
when the window opens, not to create the motivation.

**Pattern C: Collection-completion purchasing (Forager, Herbalist)**
Some buyers are building a reference library. They buy one zone guide, then want adjacent
zones. They buy the wild edibles guide, then want the medicinal guide for the same ecosystem.
The bundle recommendations in Campaign 3 serve this pattern directly.

### 3.3 Cross-Sell Opportunities by Phase 2 Product

The following pairings are the highest-confidence cross-sell opportunities available at
Phase 2 launch. All are based on logical product complementarity, not speculative upselling.

| Phase 1 Purchase | Phase 2 Cross-Sell | Timing | Mechanism |
|---|---|---|---|
| Wild Edibles Quick Reference | Medicinal Herbs guide (same ecosystem) | Day 15 (Campaign 3) | Forager-to-herbalist pathway |
| Zone Calendar | Seed Saving Field Manual | Day 15 (Campaign 3) | Planning-to-execution project step |
| Seed Saving Field Manual | Preservation guides (dehydrating, fermentation) | Day 30 (Campaign 3 Email 3.2) | Saved seeds → preserved harvest |
| Native Plants Regional Guide | Endangered species guide for same region | Day 15 (Campaign 3) | Botanical collector pattern |
| Hunting/Fishing Manual | Meat/Fish Preservation Manual | Day 7 (Campaign 2 content + Day 15 upsell) | Sequential activity pairing |
| Any Zone guide | Adjacent zone bundle (next zone up/down) | Day 21 (Campaign 3 Email 3.1) | Geographic expansion |
| Companion Planting Chart | Zone Calendar | Day 15 (Campaign 3) | Chart requires zone-specific context to use fully |

---

## Part 4: Phase 3 Go/No-Go Decision Tree

### 4.1 Decision Gate Structure

Phase 3 (Women's Health bundle launch + Tier 2 wholesaling) triggers on Day 60 metrics
(approximately July 29, 2026). The evaluation window is Day 45–60 post-Phase-2-launch.
There are four scenarios, each with a specific go/no-go outcome and action plan.

The four scenarios are not discrete outcomes — they are points on a spectrum. Match the
actual Day 60 data to the scenario that fits most closely.

### Scenario 1: High Growth

**Trigger conditions (all three must be met):**
- Phase 2 conversion rate at Day 60: above 8% Phase 1→Phase 2 conversion AND new buyer
  conversion rate above 2.5%
- Repeat purchase rate at Day 60: above 18% (of all Phase 2 buyers making a second purchase)
- Phase 2 cohort size: 100+ unique buyers by Day 60

**Decision: Full Phase 3 GO — launch Women's Health bundle AND initiate Tier 2 wholesaling**

Timeline:
- September 2026: Women's Health themed bundle launch (medicinal herb themed bundles from
  `phase-3-medicinal-herbs-strategy.md`)
- September 2026: Begin Tier 2 wholesale outreach to law school libraries, union organizations,
  herbalism schools (per `B2B_DISTRIBUTION_STRATEGY.md` Tier 2 targets)

Specific actions:
1. Begin Women's Health bundle development August 1 (7-week lead time to September launch)
2. Draft Tier 2 outreach template using `phase-3-cohort-messaging.md` wholesale framing
3. Increase Kit email cadence for Herbalist segment to 2x/month starting August 1
4. Accelerate Phase 3 product development to Option C (aggressive) timeline per
   `phase-3-decision-framework.md`

Revenue expectation: $2,800–$3,800/month gross by October 2026

### Scenario 2: Steady Growth

**Trigger conditions (two of three must be met):**
- Phase 2 conversion rate at Day 60: 4–8% Phase 1→Phase 2 AND new buyer rate 1.5–2.5%
- Repeat purchase rate at Day 60: 10–18%
- Phase 2 cohort size: 50–100 unique buyers by Day 60

**Decision: Standard Phase 3 GO — Women's Health bundle launch, Tier 2 wholesaling on hold**

Timeline:
- September 2026: Women's Health bundle launch (same target date as Scenario 1)
- Tier 2 wholesale deferred to November 2026 pending Day 90 cohort size check

Specific actions:
1. Begin Women's Health bundle development August 1 (same timing as Scenario 1)
2. Hold Tier 2 wholesale outreach; run Day 90 check (October 29) to see if cohort reaches 75+
3. Continue standard Phase 3 Option B execution per `phase-3-decision-framework.md`
4. Prioritize highest-LTV segments (Herbalist and Homesteader) for acquisition content in
   July–August

Revenue expectation: $1,800–$2,500/month gross by October 2026

### Scenario 3: Churn Risk

**Trigger conditions (any one of the following):**
- Repeat purchase rate at Day 60: below 8%
- Phase 2 conversion rate (Phase 1 base): below 4%
- Cohort size below 50 unique buyers at Day 60 despite active Phase 2 launch

**Decision: Phase 3 CONDITIONAL — diagnose retention failure before committing Phase 3 resources**

Timeline:
- September 2026 Women's Health launch: delayed to November pending Day 90 recovery check
- Tier 2 wholesale: on hold indefinitely until repeat rate crosses 10%

Specific diagnosis protocol (execute within 48 hours of detecting Churn Risk signals):

Step 1: Check Kit automation — are all 6 campaigns firing correctly? Test the end-to-end
sequence with a new test subscriber. If Campaign 1 is not sending within 2 hours of purchase,
the tag automation has failed. Fix immediately.

Step 2: Segment churn by cohort — which specific cohort is not returning? A low aggregate
repeat rate often masks one healthy cohort and one failing cohort. Use the LTV tracker to
calculate repeat rate per cohort tag.

Step 3: Check product quality signals — are any Phase 2 products receiving under 1% conversion
rate after 200+ views? Under-converting products drag the overall repeat rate because new
buyers from those listings have a weaker product-market fit.

Step 4: Check email deliverability — SPF/DKIM configured? Is Kit sending from a custom domain?
If 30%+ of Kit sends are going to spam, the lifecycle campaign is reaching zero buyers despite
being technically "active."

Day 90 recovery check (October 29): If repeat rate has reached 10%+ by Day 90, initiate Phase
3 development with compressed timeline (Women's Health bundle by December 2026). If still
below 8%, defer Phase 3 to Q1 2027.

### Scenario 4: Explosive Growth

**Trigger conditions (early signal, visible by Day 30):**
- Phase 2 is producing 5+ orders per day within the first 14 days of launch
- Kit is growing by 10+ subscribers per day
- Repeat purchase rate visible at Day 14 (buyers making second purchase before Day 14 post-
  first-purchase — rare but a powerful loyalty signal)

**Decision: Immediate Phase 3 acceleration — compress timeline, consider contractor support**

This scenario requires real-time response, not waiting for Day 60. If explosive growth signals
appear in the first two weeks, the following actions activate immediately:

Immediate actions (within 72 hours of detecting signal):
1. Increase Kit email frequency for all segments to maximum weekly cadence
2. Activate Etsy Ads at $5/day minimum on the top-3 converting Phase 2 listings
3. Begin Women's Health bundle content development immediately (target August 15 launch
   instead of September)
4. Activate referral program (Campaign 2 referral credit mechanism) to capitalize on
   word-of-mouth momentum

Contractor trigger: If order processing + email management + product development work exceeds
20 hours/week, identify one task to outsource (most likely: social media content or mockup
production). This threshold should be assessed at Day 21.

Revenue expectation: $4,000–$6,000/month gross by October 2026

### 4.2 Automated Day 30 / Day 45 / Day 60 Checkpoint Alerts

These three checkpoints do not require the operator to remember to check. They are built into
the weekly dashboard review cadence but flagged explicitly here so the cadence is unmistakable.

**Day 30 Checkpoint (June 29, 2026)**

Metrics to pull and record:
- Total Phase 2 orders to date
- Repeat purchase rate (buyers from Phase 1 or early Phase 2 who made a second purchase)
- Kit subscriber count
- Top-selling Phase 2 product
- Cohort distribution (% of buyers per cohort tag in Kit)

Alert thresholds triggering escalation to user:
- Total orders below 20 by Day 30: run the under-performance diagnosis in Part 4.2 of
  `phase-2-analytics-strategy.md` (traffic vs. conversion problem diagnostic)
- Repeat rate below 5% at Day 30: check Kit automation immediately (see Churn Risk protocol)
- Kit subscriber count below 30 at Day 30: the landing page / lead magnet funnel has a
  problem; check Kit landing page is live, UTM parameters are on all links

**Day 45 Checkpoint (July 14, 2026)**

This checkpoint coincides approximately with the planned Phase 2 expansion date. Metrics:
- Total orders (cumulative)
- Phase 2 cohort size (unique buyers)
- Repeat purchase rate (30-day cohort: buyers from June 1–29 who re-purchased in July)
- Bundle attach rate (% of orders containing bundles)

Alert thresholds:
- Cohort size below 40 unique buyers at Day 45: Phase 2 expansion should wait until Day 60
  data arrives before committing new product development resources
- Bundle attach rate below 5%: the bundle recommendation logic in Campaign 3 is not
  converting; audit the bundle-to-first-purchase product pairings in Section 3.3

**Day 60 Checkpoint (July 29, 2026) — Primary Go/No-Go Gate**

This is the Phase 3 decision date. Pull all metrics from the analytics dashboard, match to
the four Scenarios above, and make the Phase 3 call. Decision must be recorded in WORKLOG.md
with the reasoning within 48 hours of July 29.

---

## Part 5: NPS and Voice-of-Customer Mechanics

### 5.1 Survey Schedule and Delivery

Three NPS survey touchpoints are designed to capture customer voice at the moments when
feedback is most honest and actionable.

**Day 7 Survey (post first-purchase follow-up)**

Delivery: Campaign 1 Email 2 includes a link to a 2-question Google Form.
Questions:
1. "How satisfied are you with your purchase so far? (1–10 rating)"
2. "What would make this guide more useful for you? (one-line free text)"

Purpose: Catch product quality issues early — if a guide has confusing navigation, incorrect
zone information, or missing content, the Day 7 response catches it before negative reviews
compound. A score below 7 on the first question triggers a personal reply within 24 hours.

**Day 30 NPS Survey (retention health check)**

Delivery: Newsletter inclusion — a single embedded rating question at the bottom of the first
full newsletter (approximately Day 28–35 post-launch).
Question: "How likely are you to recommend Seedwarden to someone who forages, gardens, or
grows food? (0–10)"

NPS calculation: Promoters (9–10) minus Detractors (0–6), divided by total responses.
Target: NPS above 40 by Day 60.
If NPS falls below 20: the product or brand is not resonating. Conduct 3–5 direct phone or
video calls with buyers to diagnose before Phase 3 launch.

**Day 60 Feedback Prompt (Phase 3 readiness signal)**

Delivery: Campaign 4 re-engagement email (Day 45–60 cohort) includes a "what would you
want next?" question.
Question: "If Seedwarden published one more guide next month, what would it be?" (Free text)

Purpose: This is the voice-of-customer input for Phase 3 product sequencing. Aggregate
responses monthly. If 3+ responses name the same topic or product type, that topic becomes
a priority signal for Phase 3 Tier 1. Do not make product decisions based on fewer than
3 matching responses — individual requests are not market signals.

### 5.2 Escalation Logic for Survey Responses

Day 7 survey score below 6: Escalate to user immediately. Send a personal reply within 24 hours
acknowledging the issue. If the same issue is mentioned by 3+ buyers in the first week, the guide
has a quality problem that requires a product update before further marketing investment.

Day 30 NPS below 20: Escalate to user for qualitative research sprint. The problem is not
answerable through quantitative data at this point — direct buyer conversations are required.
Schedule 3–5 calls within 14 days. Document findings in WORKLOG.md.

Day 60 "what would you want next?" responses naming the same product 3+ times: Escalate to
user as a Phase 3 priority input. Cross-reference with the existing Phase 3 product roadmap
(`phase-3-product-specifications.json`). If the requested product is already in the pipeline,
accelerate it. If it is not, add it to the Phase 3 Tier 1 consideration list.

---

## Part 6: Dashboard Designs

### 6.1 Weekly Dashboard (30 minutes, every Sunday evening)

The weekly dashboard in `phase-2-analytics-strategy.md` Part 3.2 is the operational template.
The version below is the customer success layer — the additional metrics specific to Phase 1
to Phase 2 conversion progress and retention health. Record in the Google Sheet "Weekly" tab
as additional columns alongside the standard weekly metrics.

```
SEEDWARDEN WEEKLY CUSTOMER SUCCESS CHECK — Week of [DATE]
=========================================================
DATA SOURCES: Etsy orders CSV, Kit subscriber export, LTV tracker

PHASE 1→PHASE 2 CONVERSION PROGRESS
  Phase 1 buyers who made a Phase 2 purchase this week:   ___  (cumulative: ___ )
  Phase 1 buyers contacted by Kit automation:            ___  (have `purchased` tag in Kit)
  Phase 1 buyers not yet in Kit:                         ___  (check manually against LTV tracker)

RETENTION SIGNALS
  Weekly repeat purchase count:                          ___  (any second+ purchase this week)
  Campaign 1 open rate (buyers who purchased this week): ___%  (target: 40%+)
  Campaign 3 click-to-purchase rate (active in sequence):___%  (target: 1-2%)
  Email churn (unsubscribes this week):                  ___  (alert if > 3 in one week)

COHORT HEALTH
  Segment with highest order volume this week:           ___
  Segment with lowest email engagement this week:        ___  (investigate if 2 weeks consecutive)
  Unknown cohort % this week:                           ___%  (target: below 20%)

ESCALATION FLAGS (check any that apply)
  [ ] Repeat purchase rate below 5% for 2 consecutive weeks → check Kit automation
  [ ] Unknown cohort % above 25% → review post-purchase survey delivery
  [ ] 0 Phase 1 buyers have converted to Phase 2 yet (by Day 21) → Campaign 3 timing audit
  [ ] NPS survey response with score below 6 → personal reply required within 24 hours
```

### 6.2 Monthly Dashboard (2 hours, first Monday of each month)

The full monthly template is in `phase-2-analytics-strategy.md` Part 3.3. Add the following
customer success blocks to the monthly deep-dive:

```
SEEDWARDEN MONTHLY CUSTOMER SUCCESS DEEP DIVE — [MONTH YEAR]
=============================================================
DATA SOURCES: LTV tracker (updated this session), Kit CSV export, Etsy stats CSV

BLOCK A: PHASE 1→PHASE 2 CONVERSION TRACKING
  Phase 1 buyer count (buyers with first_order_date < 2026-05-30):  ___
  Phase 1 buyers who made a Phase 2 purchase (any date):            ___
  Phase 1→Phase 2 conversion rate:                                  ___% (target by Day 60: 8%+)
  Top Phase 2 product purchased by Phase 1 buyers:                  ___
  Phase 1 buyers with `kit_subscriber = yes`:                       ___
  Phase 1 buyers with `kit_subscriber = no` (at-risk):              ___

BLOCK B: SEGMENT LTV PROGRESS
  (From LTV tracker — filter by cohort_tag)

  Segment          | Count | Avg LTV | 30d Repeat% | 60d Repeat% | Target LTV
  Forager          |       | $       | %           | %           | $60-80
  Prepper          |       | $       | %           | %           | $75-100
  Homesteader      |       | $       | %           | %           | $70-100
  Gift Buyer       |       | $       | %           | %           | $45-60
  Herbalist        |       | $       | %           | %           | $90-130
  Unknown          |       | $       | —           | —           | Reclassify

  Highest-LTV segment this month: ___
  Segment farthest below LTV target: ___ → check if their lifecycle emails are firing

BLOCK C: RETENTION MECHANICS VALIDATION
  Seasonal content driver test (from last 4 newsletter sends):
    Did any email send correlate with 2x+ order spike within 48 hours? YES / NO
    If YES, which email topic: ___
    → This topic should recur in next month's content calendar

  Email nurture driver test:
    Kit subscriber 30d repeat rate: ___%
    Non-subscriber (Etsy-only) 30d repeat rate: ___% (estimate from LTV tracker non-Kit buyers)
    Differential: ___x (target: 2x+ advantage for subscribers)
    If below 1.5x differential: the email sequence content needs revision; Kit advantage
    is not materializing. Audit Campaign 2 content relevance first.

BLOCK D: PHASE 3 READINESS SCORE
  Evaluate at end of Month 1 and Month 2 (Days 30 and 60).
  Score out of 6 criteria:

  [ ] Criterion 1: Total orders ≥ 50 by Day 60                      PASS / FAIL
  [ ] Criterion 2: Gross revenue ≥ $1,000 in Month 2                PASS / FAIL
  [ ] Criterion 3: Phase 1→Phase 2 conversion rate ≥ 8%             PASS / FAIL
  [ ] Criterion 4: Repeat purchase rate ≥ 10% at Day 60             PASS / FAIL
  [ ] Criterion 5: Kit subscribers ≥ 80 by Day 60                   PASS / FAIL
  [ ] Criterion 6: NPS ≥ 40 (Day 30 survey data)                    PASS / FAIL

  Score: ___ / 6
  Phase 3 recommendation based on score:
    6/6: Scenario 1 (High Growth) → Full Phase 3 GO
    4–5/6: Scenario 2 (Steady Growth) → Standard Phase 3 GO
    2–3/6: Scenario 3 (Churn Risk) → Conditional GO, diagnose first
    0–1/6: Scenario 4 not applicable; fundamental issue — pause Phase 3 entirely
```

### 6.3 Quarterly Dashboard (3 hours, beginning of each quarter: Oct 1, Jan 1, Apr 1)

The quarterly review is a higher-altitude evaluation: is the business on the 12-month LTV
trajectory it needs to be? Is Phase 3 generating the revenue that justifies continued
development investment?

```
SEEDWARDEN QUARTERLY REVIEW — [QUARTER YEAR]
=============================================
DATA SOURCES: All monthly data logs + LTV tracker cumulative view

SECTION 1: COHORT LTV vs. 12-MONTH TARGET
  (Compare actual LTV-to-date against the 12-month LTV targets from Part 2.2)

  Are Homesteader and Herbalist segments on track for $70–$100 and $90–$130 targets?
    Actual Homesteader LTV (to date): $___  | Annualized projection: $___
    Actual Herbalist LTV (to date): $___    | Annualized projection: $___
  If either segment is more than 30% below annualized target: escalate to user for
  cohort-specific content audit.

SECTION 2: PHASE 3 PERFORMANCE REVIEW (if Phase 3 is live)
  Women's Health bundle conversion rate: ___% (target: 1.5%+)
  Tier 2 wholesale revenue (if active): $___/month
  Phase 3 product count live: ___
  New Phase 3 cohort (Herbalist sub-segments): ___ buyers

SECTION 3: SEASONAL PATTERN VALIDATION
  Spring peak (March–May): Did orders lift 20%+ vs. prior winter baseline?  YES / NO
  Fall peak (September–October): Did orders lift 25%+ vs. prior summer baseline?  YES / NO
  Holiday gift window (November–December): Did bundles reach 35%+ of revenue?  YES / NO
  If any seasonal lift failed to materialize: investigate whether content calendar was
  aligned with the seasonal window or whether a channel went dark during the peak period.

SECTION 4: ANNUAL CADENCE PLANNING
  Next quarter's seasonal windows: ___
  Top 2 highest-LTV segments to prioritize in next quarter's content: ___
  Phase 3 product development decisions for next quarter: ___
  Escalation items requiring user decision: ___
```

---

## Part 7: Escalation Logic

### 7.1 Who Owns Phase 2 Success Metrics

Anya owns all Phase 2 success metrics. The framework below defines which signals require
immediate attention and which can be reviewed on the weekly cadence.

The escalation hierarchy has three levels:

**Level 1: Immediate escalation (same-day response required)**
- Day 7 NPS score below 6 from any buyer
- Campaign 1 (post-purchase email) not firing within 24 hours of confirmed order
- Any negative Etsy review (1–2 stars) — personal response required within 24 hours
- Zero orders for 5+ consecutive days after Day 7 post-launch

**Level 2: Weekly dashboard escalation (review at next Sunday session, not before)**
- Campaign open rate below trigger thresholds for 2+ consecutive weeks
- Repeat purchase rate below 5% at Day 30
- Cohort distribution showing one segment above 55% (Scenario D in `phase-3-decision-framework.md`)
- Kit subscriber growth flat (fewer than 5 new subscribers in any week after Week 2)

**Level 3: Monthly review decision point (not urgent — review at first-Monday session)**
- Segment LTV below target trajectory (will not compound to a crisis within 30 days)
- Phase 3 readiness score calculation
- Seasonal content calendar alignment for next 60 days
- Pricing or bundle structure reconsideration

### 7.2 Automated Alert Checklist (Weekly Sunday Review)

Print or bookmark this checklist. Run it at every Sunday dashboard session. The goal is
to catch Level 1 issues before they become crises and confirm Level 2 issues are being tracked.

```
SUNDAY ESCALATION CHECKLIST
============================
LEVEL 1 CHECKS (5 minutes):
  [ ] Any NPS/survey response with score < 6 received this week?
      YES → personal reply drafted and sent this week? [ ] YES [ ] NO
  [ ] Any 1-2 star Etsy review posted this week?
      YES → response drafted? [ ] YES [ ] NO
  [ ] Did Kit automation send Campaign 1 to all new buyers within 24 hours?
      To verify: check Kit > Sequences > Campaign 1 > Activity; count this week's new buyers
      vs. Kit sends. If mismatch: activate manual Option B tag assignment immediately.
  [ ] Were there any days this week with zero orders AND 100+ listing views?
      YES → listing quality problem (not traffic). Do not increase posting volume this week.
      Fix listing (cover image, pricing, description hook) before next Sunday.

LEVEL 2 CHECKS (10 minutes):
  [ ] Campaign 1 open rate this week: ___% (alert if below 30% for 2nd consecutive week)
  [ ] Repeat purchase count this week: ___ (alert if 0 for 2nd consecutive week beyond Day 21)
  [ ] New Kit subscribers this week: ___ (alert if below 3 for 2nd consecutive week)
  [ ] Email unsubscribes this week: ___ (alert if 4+ unsubscribes in a single week)
  [ ] Phase 1→Phase 2 conversion progress: ___ of ___ predicted Phase 2 buyers have converted

PHASE 3 STATUS (2 minutes):
  [ ] Day 30 checkpoint complete? (if applicable)  [ ] YES [ ] NO → complete now
  [ ] Day 45 checkpoint complete? (if applicable)  [ ] YES [ ] NO → complete now
  [ ] Day 60 Phase 3 decision recorded in WORKLOG.md?  [ ] YES [ ] NO → must complete by July 31
```

### 7.3 Decision Cadence Summary

| Cadence | Format | Time Required | Primary Decision |
|---|---|---|---|
| Daily (Days 1–14) | 5-minute Etsy Shop Manager check | 5 min | Catch anomalies; verify Kit automation |
| Daily (Days 15–30) | Mon/Wed/Fri check only | 5 min | Same as above, reduced frequency |
| Weekly | Sunday dashboard (Sheets) | 30 min | Escalation check, cohort health, email performance |
| Monthly | First-Monday deep dive | 2 hours | LTV tracking, Phase 3 readiness score, cohort adjustment |
| Day 60 specific | Phase 3 go/no-go evaluation | 45 min | Match data to Scenario 1/2/3/4; record decision |
| Quarterly | Broader pattern review | 3 hours | Annual LTV trajectory, seasonal validation, Phase 3 assessment |

---

*Prepared: 2026-05-07. This document is the command layer for Phase 2 customer success. For
implementation of the underlying systems referenced throughout, see: `phase-2-analytics-strategy.md`
(data architecture and dashboard templates), `phase-2-buyer-retention-lifecycle-strategy.md`
(6-campaign email system), `customer-cohort-analysis-framework.md` (segment definitions),
`phase-3-decision-framework.md` (Phase 3 Options A/B/C/D), `analytics/monthly-metrics-checklist.md`
(monthly operator runbook).*
