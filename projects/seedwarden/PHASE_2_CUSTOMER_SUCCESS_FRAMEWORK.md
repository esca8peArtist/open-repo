---
title: "Phase 2 Customer Success & Retention Framework"
version: "3.0"
date: 2026-05-09
status: production-ready
scope: >
  Phase 1→Phase 2 conversion modeling (three-tier prediction), customer segmentation
  with Phase 1 sizing, retention mechanics and seasonal calendar, automated Phase 3
  go/no-go criteria (September 2026 women's health decision), analytics dashboard design
launch-date: 2026-05-30
phase-3-primary-decision-date: 2026-09-01
references:
  - phase-2-analytics-strategy.md
  - phase-2-customer-success-framework.md (v2.0 — command layer; this document is the planning layer)
  - phase-2-buyer-retention-lifecycle-strategy.md
  - customer-cohort-analysis-framework.md
  - phase-3-decision-framework.md
  - financial-sustainability-model.md
  - phase-2-analytics-dashboard-schema.json
word-count: ~2500
---

# Phase 2 Customer Success & Retention Framework

**Purpose**: This document addresses the one question the v2.0 framework does not answer
directly: *how do we maximize the percentage of Phase 1 customers who buy Phase 2 products?*
Conversion velocity — not list growth — is the Phase 2 success metric. Every section here
is written from that lens.

**Context at the time of writing**:
- Phase 1 closed: 47 orders, $1,341 gross, 2.24% conversion, ~14.9% 30-day repeat rate
- Phase 2 launches May 30, 2026 — 21 days from today
- Endangered species guides (forager, prepper, medicinal tiers) are ready for production
- Phase 3 (women's health tier) decision date is September 1, 2026 — 4 months post-launch
- No post-purchase email system existed in Phase 1; Kit automation is the central new tool

**Operating principle**: Every metric named here has an action attached to it. No monitoring
without a response protocol. No threshold without a consequence.

---

## Section 1: Phase 1 to Phase 2 Conversion Modeling

### 1.1 Why Conversion Velocity Is the Right Metric

List growth is easy to measure and easy to fake. A 500-person email list with 2% purchase
rate contributes $280 in revenue at $28 AOV. A 100-person list with a 15% purchase rate
contributes $420 — from a smaller audience, with lower acquisition cost. Phase 2 success
is the rate at which Phase 1 buyers and early Phase 2 subscribers convert to paid customers,
not the volume of people in the funnel.

The Phase 1 baseline gives a real denominator: 47 buyers. Every prediction model below
operates against that 47-buyer pool. The question is not "how many new people can we reach"
but "how many of the 47 who already trusted this store once can we earn a second purchase from."

Phase 1 repeat rate was 14.9% at 30 days — meaning approximately 7 buyers returned within a
month of their first purchase, with no email follow-up at all. That is the unmanaged baseline.
With Kit automation active in Phase 2, the target is to double that: 25-30% repeat within 45
days for buyers who enter the email funnel.

### 1.2 Three-Tier Conversion Prediction Model

Apply this model to every Phase 1 buyer in the LTV tracker before May 30. Classify each buyer
into Tier A, B, or C. These tiers determine which buyers receive priority Kit follow-up and how
the cross-sell sequence is personalized.

**Tier A: High Phase 2 Likelihood (predicted 35–50% conversion)**

Buyer profile: Purchased a guide that has a clear "next product" in the Phase 2 catalog, OR
purchased multiple guides in one order (indicating catalog appetite), OR purchased in a product
category where Phase 2 adds direct depth.

Qualifying purchase combinations from Phase 1:
- Wild Edibles Quick Reference → Phase 2 cross-sell is Medicinal Herbs guide (same ecosystem)
- Zone Calendar (any zone) → Phase 2 cross-sell is Seed Saving Field Manual or adjacent zone guide
- Seed Saving Field Manual → Phase 2 cross-sell is any preservation guide (dehydrating, fermentation)
- Native Plants Regional Guide → Phase 2 cross-sell is endangered species guide for same region
- Hunting/Fishing Manual → Phase 2 cross-sell is Meat/Fish Preservation Manual
- Any multi-guide order (3+ guides in one transaction) → Phase 2 cross-sell is premium themed bundle

Estimated Phase 1 Tier A buyers: approximately 12–16 of the 47 (27–34% of base).

Predicted Phase 2 revenue from Tier A at 40% conversion and $30 avg: $144–$192 from returning
buyers before any new customer acquisition begins.

**Tier B: Medium Phase 2 Likelihood (predicted 18–28% conversion)**

Buyer profile: Single-guide buyer at $14–22 price point, or bundle buyer who purchased broadly
without a clear "next product" anchor. Demonstrated purchase intent but no obvious adjacent need.

Qualifying purchase combinations from Phase 1:
- Any single guide at $14–22 with no obvious Phase 2 companion → needs a bundle angle (15% discount)
- Companion Planting Chart alone → needs Zone Calendar to use the chart fully
- Any bundle (3+ guides) bought in Phase 1 → already owns broad catalog; needs genuinely new content
- First purchase was a low-engagement category (entry price point, $5–9) plus one other guide

Estimated Phase 1 Tier B buyers: approximately 18–22 of the 47 (38–47% of base).

Tier B is the largest segment. These buyers need the most deliberate email sequence — Campaign 2
(Content Deepening) is the primary vehicle, not Campaign 3 (Upsell). Demonstrate value before
making an offer.

**Tier C: Low Phase 2 Likelihood (predicted 3–12% conversion)**

Buyer profile: Single-occasion gift buyer, or single entry-price guide with no behavioral signals,
or buyer with no Kit email subscription (no email touch point available at all).

Qualifying purchase combinations:
- Mobile device purchase during holiday window (November–December 2025 gift season)
- Single guide under $10 with no repeat or no email subscription
- Any buyer whose `kit_subscriber` field in the LTV tracker is "no" — they have zero email
  touchpoints; Phase 2 adoption is entirely dependent on organic Etsy re-discovery

Estimated Phase 1 Tier C buyers: approximately 9–15 of the 47 (19–32% of base).

Tier C is not abandoned — the Campaign 5 seasonal win-back (September 1) is the realistic
conversion vehicle, catching them at a fall foraging or preservation motivation window.

**Predicted total Phase 2 purchases from 47 Phase 1 buyers (pre-new acquisition):**

| Tier | Estimated Buyers | Conversion Rate | Predicted Purchases | Revenue at $30 AOV |
|------|-----------------|-----------------|---------------------|---------------------|
| A    | 12–16           | 35–50%          | 4–8                 | $120–$240           |
| B    | 18–22           | 18–28%          | 3–6                 | $90–$180            |
| C    | 9–15            | 3–12%           | 0–2                 | $0–$60              |
| **Total** | **47**     | **15–34%**      | **7–16**            | **$210–$480**       |

These numbers are a floor, not a ceiling. New Phase 2 customer acquisition is additive to
this base. The 7–16 returning purchases represent revenue that should materialize in the
first 45 days purely from relationships already established in Phase 1.

### 1.3 Prediction Accuracy and Confidence Intervals

The model above is grounded in behavioral logic, not historical purchase data from Seedwarden
specifically (Phase 1 had too few buyers to run statistical modeling). The confidence interval
is approximately plus-or-minus 40% on the conversion rate estimates per tier — meaning Tier A
could land anywhere from 21% to 70% depending on email sequence performance.

Narrow the interval after Day 30 data: at the first monthly review, compare actual Tier A
conversion to predicted. If actual is above predicted, widen the Tier B conversion target. If
actual is below predicted, audit whether those buyers entered the Kit automation funnel.

The single largest variable in the model is Kit email coverage. Tier A buyers who never
joined the email list perform like Tier C buyers in practice. Check kit_subscriber status for
every Phase 1 buyer before May 30.

---

## Section 2: Customer Segmentation

### 2.1 Four Customer Types and Phase 1 Size Estimates

Phase 1's 47 orders distribute across four customer types based on available product and
timing signals. These are inference-based estimates; the post-purchase survey in Phase 2 will
produce confirmed segmentation.

**Foragers (20–25% of Phase 1 buyers = 9–12 buyers)**

Identifying actions: Purchased wild edibles, native plants, or multi-guide botanical orders.
High session duration on listing pages. Geographic concentration in Pacific Northwest and
Northeast (inferred from shipping data if available in Etsy order export).

What they look like in the LTV tracker: first_product contains "wild edibles," "native plants,"
or "foraging." order_1_products shows 2+ guides in a single transaction.

Phase 2 adoption likelihood: Tier A. These buyers have the clearest next product. The
endangered species guides in production now are exactly the catalog extension a forager wants.

**Preppers (15–20% of Phase 1 buyers = 7–9 buyers)**

Identifying actions: Purchased 5+ guides in a single order, or bought the hunting/fishing
manual, or purchased a survival garden or all-guides bundle. Single large transaction.

What they look like in the LTV tracker: order_1_value is the highest of any Phase 1 buyer
segment — likely $50–$80+. order_1_products contains 5+ items or includes "survival" or
"hunting" in the product names.

Phase 2 adoption likelihood: Tier B. Preppers already bought broadly; they need genuinely
new content (endangered species guides, medicinal herbs). Generic bundle re-promotion will
not convert this cohort.

**Homesteaders (30–35% of Phase 1 buyers = 14–16 buyers)**

Identifying actions: Purchased seed saving, zone calendar, companion planting, or preservation
guides — often in sequential single-guide purchases rather than bulk orders. Repeat purchase
pattern if they appear more than once in the 47 orders.

What they look like in the LTV tracker: first_product is often a planning or technique guide
($18–$30). Any buyer who placed more than one Phase 1 order is almost certainly a homesteader.

Phase 2 adoption likelihood: Split Tier A/B. Homesteaders with a clear next project (bought
seed saving field manual, obvious next step is dehydrating or fermentation) are Tier A.
Homesteaders who purchased broadly and may not have a clear next project are Tier B.

**Gift Buyers (15–20% of Phase 1 buyers = 7–9 buyers)**

Identifying actions: Single high-visual-value guide, mobile purchase, purchased in October–
December 2025 window, no email subscription, no repeat purchase signal.

What they look like in the LTV tracker: first_order_date falls in Q4 2025. kit_subscriber
is "no" (most likely). order_1_products is a single guide priced $20–$35 (gift-range).
No order_2 entry.

Phase 2 adoption likelihood: Tier C. Gift buyers are occasion-driven. Without a gifting
occasion trigger (Father's Day, holiday), they will not return unprompted. The Campaign 5
October seasonal send is the primary vehicle.

### 2.2 Using Segments Operationally

The segment determines which Kit email sequence the buyer enters and which Phase 2 products
get featured in their cross-sell. The LTV tracker cohort_tag field drives this routing.

Buyers without a confirmed cohort tag stay on the general newsletter until their behavior
reveals a classification signal — typically by the first email click-through (clicking botanical
content signals forager; clicking preservation signals homesteader). Target: fewer than 15% of
buyers in "Unknown" status by Day 30.

---

## Section 3: Phase 2 Retention Mechanics

### 3.1 What Drives Repeat Purchases

Four drivers operate in roughly descending order of impact for the Seedwarden buyer base:

**Driver 1: Seasonal content relevance.** Buyers return when a season-specific action is
imminent. The spring morel window, summer preservation peak, fall seed saving — these are
external motivations the buyer already has. The email's job is to be present at that moment
with the right product. A well-timed seasonal email outperforms a generic promotional email
by a factor of 2–4x in click-through rate at comparable list size.

**Driver 2: Content depth and specificity.** Generic "gardening tips" content loses foragers
and herbalists within 2 emails. Zone-specific, species-level content builds trust and keeps
these high-LTV segments engaged. Measure this by tracking click rates on zone-specific emails
versus general botanical emails — if zone-specific generates 2x+ higher CTR, invest accordingly.

**Driver 3: Post-purchase email cadence.** The 6-campaign lifecycle sequence (documented in
phase-2-buyer-retention-lifecycle-strategy.md) maintains purchase intent between natural buying
windows. Without it, the average interval between purchases is 60–90 days. With Campaign 3
(cross-zone upsell at Day 15) running, the target is to compress that to 30–45 days for Tier A
and B buyers.

**Driver 4: Community identity framing.** Buyers who identify with the "forager" or "seed
keeper" label develop retention patterns that outlast any product. This driver takes 90+ days
to confirm quantitatively but manifests early as high VIP email open rates (target 60%+) and
repeat purchase intervals below 30 days.

### 3.2 Email Engagement Expectations by Segment

| Segment       | Welcome Seq Open Rate | Newsletter Open Rate | CTR Target | Unsubscribe Alert |
|---------------|----------------------|---------------------|------------|-------------------|
| Forager       | 45–60%               | 30–40%              | 4–6%       | >1.5% any send    |
| Prepper       | 30–40%               | 20–28%              | 2–4%       | >2% any send      |
| Homesteader   | 45–55%               | 32–42%              | 4–7%       | >1.5% any send    |
| Gift Buyer    | 25–35%               | 15–22%              | 1–2%       | >3% any send      |
| Herbalist     | 50–65%               | 35–45%              | 5–8%       | >1.5% any send    |

Prepper unsubscribe tolerance is higher because this cohort opens less frequently but purchases
in higher-value bursts. A 2% unsubscribe on a prepper-targeted email does not necessarily
indicate content failure — it may indicate the segment is self-selecting. Watch whether the
unsubscribers were buyers or non-buyers before acting.

Gift Buyer email volume should be low-frequency by design: two sends per year maximum (May for
Father's Day, November for holiday). Attempting a content relationship with gift buyers results
in high unsubscribes and degrades the list health metric.

### 3.3 Product Adoption Patterns That Drive Phase 3 Purchasing

Which Phase 2 bundle drives the most repeat buyers? This is the key Phase 3 sequencing signal.
Based on product logic, not yet confirmed with data:

- Buyers who purchase the Medicinal Herbs guide in Phase 2 are the most likely Phase 3
  Women's Health tier customers. This is a direct product-to-product path. Track how many
  medicinal herb buyers exist in the Phase 2 cohort by Day 45 — that number forecasts the
  addressable audience for September Women's Health.

- Buyers who purchase endangered species guides are building a reference library. They are the
  highest collectors in the cohort. Phase 3 expansion of that series (more species, more regions)
  will convert at high rates for this sub-segment.

- Buyers who purchase seed saving plus any preservation guide are confirmed homesteaders on a
  project completion arc. They are the Phase 3 Seed Library System audience — a product not
  yet in production but clearly demanded by this pattern.

### 3.4 Cohort Repeat Rate Targets

| Segment     | 30-Day Repeat Target | 90-Day Repeat Target | Alert: Below |
|-------------|---------------------|----------------------|--------------|
| Tier A core | 25–35%              | 40–55%               | 15% at Day 45|
| Tier B core | 12–20%              | 25–35%               | 8% at Day 45 |
| Tier C      | 2–8%                | 5–12%                | N/A (watch)  |

If Tier A repeat rate is below 15% at Day 45, the Kit cross-sell sequence (Campaign 3) is not
reaching these buyers or is not converting. Audit in this order: (1) Are Tier A buyers tagged
in Kit? (2) Is Campaign 3 firing at Day 15? (3) Is the product featured in Campaign 3 the
right cross-sell for this buyer's first product?

### 3.5 Seasonal Content Calendar

The seasonal calendar is the single highest-leverage operational tool. It aligns content
effort with the buyer's natural motivation peak, which reduces the persuasion cost of every
marketing action.

| Month         | Primary Season Signal     | Featured Cohort     | Product Focus                              |
|---------------|--------------------------|---------------------|--------------------------------------------|
| June 2026     | Spring foraging active    | Forager             | Wild edibles, native plants, regional guides|
| July 2026     | Summer preservation peak  | Homesteader         | Fermentation, dehydrating, seed saving     |
| August 2026   | Late summer harvest       | Homesteader/Prepper | Preservation manuals, bulk guide bundles   |
| September 2026| Fall foraging — ginseng peak | Forager/Herbalist| Medicinal herbs, ginseng identification    |
| October 2026  | Seed saving season        | Homesteader         | Seed saving, Zone Calendar, winter planning|
| November 2026 | Gift season opens         | Gift Buyer          | Bundles, premium single guides, gift sets  |
| December 2026 | Peak gift window          | Gift Buyer          | Holiday bundles, expanded homesteader set  |
| January 2027  | New Year resolutions       | Homesteader/Herbalist| Medicinal guides, women's health tier     |
| April 2027    | Spring foraging preparation| Forager/Homesteader | Spring regional guides, edibles content   |

**September = ginseng season.** This is the single most predictable forager-and-herbalist
revenue spike in the annual calendar. American ginseng identification and sustainable
harvesting is a high-search-volume topic in September in the eastern and midwestern US.
If the medicinal herbs guide covers ginseng, a September 1 broadcast to the Forager and
Herbalist segments is the highest-ROI email of the year. Plan this content now.

**Cohort analysis — early vs. late adopters.** Buyers who purchase in Week 1 (May 30–June 6)
are self-selecting as engaged followers who saw the launch content. They have higher baseline
engagement and repeat rates than Month 1 buyers who discovered the store through Etsy organic
search. Do not use Week 1 cohort data as the norm — wait for 45-day data before setting
segment-level targets. The Week 1 cohort will over-perform by 15–25% compared to the steady-
state cohort.

---

## Section 4: Automated Go/No-Go Criteria for Phase 3 Launch

### 4.1 Context: September 2026 Phase 3 Decision

Phase 3 launches the women's health medicinal tier — themed herb bundles and practitioner
reference products targeting herbalists, midwives, and wellness practitioners. This is a
distinct product line that requires content development (estimated 7–10 weeks lead time),
not just a listing addition.

Decision date: September 1, 2026. Phase 2 launched May 30. That gives exactly 94 days of
live data before the Phase 3 decision must be made.

The women's health tier specifically requires a confirmed Herbalist segment in the Phase 2
buyer base — because that segment is the primary addressable audience. A strong Homesteader
cohort is not sufficient justification for Phase 3; it is a Herbalist-specific gate.

### 4.2 Go Threshold (High Confidence Phase 3 Is Viable)

All three conditions must be met by the Day 60 data pull (July 29, 2026):

1. Phase 2 overall conversion rate: above 15% of Phase 1 buyer base (8+ of 47 buyers have
   made a Phase 2 purchase)
2. Repeat purchase rate at Day 60: above 25% of all Phase 2 buyers
3. Herbalist segment confirmed: at least 15% of all Phase 2 buyers carry the Herbalist/
   Medicinal cohort tag, AND average LTV for that segment is above $40

If all three conditions are met: begin Women's Health bundle content development August 1,
target September 15 launch on Etsy. Initiate practitioner outreach (herbalism schools, doula
networks, wellness studios) using the B2B distribution strategy templates.

Revenue expectation with Go decision: Women's Health tier should add $800–$1,400/month by
December 2026 if launched in September.

### 4.3 Conditional Threshold (Wait or Iterate)

Two of three conditions are met, but one is missing. The most likely combination:
- Conversion and repeat rate are on track, but the Herbalist segment has not materialized
  (meaning medicinal herb guide content did not attract a distinct medicinal buyer persona)

If this pattern appears: Phase 3 Women's Health launch is delayed to January 2027 (aligning
with New Year health motivation window). The August–December window becomes the Herbalist
acquisition phase — more medicinal herb content, ginseng season send, and a winter wellness
newsletter theme to build the segment before launching the product.

Alternative conditional pattern: Herbalist segment exists but repeat rate is 15–25% (below 25%
Go threshold). This indicates the email sequence is working but the purchase cycle is slower
than modeled. Launch Phase 3 at reduced scope: two themed bundles instead of the full five-
bundle practitioner line. Validate demand before committing to full development.

Conditional action for either pattern: set next checkpoint for October 1, 2026. Make final
Phase 3 decision then with 4 additional months of data.

### 4.4 No-Go Threshold (Pause Phase 3, Troubleshoot Phase 2)

Any one of these conditions triggers a Phase 3 pause:

1. Phase 2 conversion below 8% of Phase 1 buyer base at Day 60 (fewer than 4 returning buyers
   in 60 days — the base is failing to activate)
2. Overall repeat purchase rate below 10% at Day 60 (buyers are not returning regardless of
   segment)
3. Herbalist segment below 8% of buyers AND no medicinal herb guide appears in the top 5
   products by revenue (the market signal for medicinal content is absent)

A No-Go does not mean Phase 3 is cancelled. It means Phase 2 product-market fit is unclear
and launching Phase 3 on top of an unconsolidated Phase 2 would split execution focus with
no data foundation.

**No-Go actions by condition:**

If conversion below 8%: the Phase 1 buyer relationship is not translating to Phase 2. Check
whether Kit automation reached Phase 1 buyers (kit_subscriber status). If fewer than 50% of
Phase 1 buyers are in Kit, the email system simply didn't reach them — fix the Etsy thank-you
CTA and re-run Campaign 1 for any Phase 1 buyer who joins in July or August.

If repeat rate below 10%: this is a product resonance issue more than a funnel issue. Buyers
are seeing Phase 2 products and not returning. Pull the weekly product performance data —
which listings have high views but low conversion? Those listings need cover image and
description revision before anything else.

If Herbalist signal absent: pivot the September 2026 launch from Women's Health to a Forager
or Homesteader tier that Phase 2 data has already validated. The endangered species series
expansion (which foragers will buy) or the Seed Library System (which homesteaders will buy)
are lower-risk September launches with existing cohort demand signals.

---

## Section 5: Analytics Dashboard Design

### 5.1 Metric Layers by Review Cadence

**Daily metrics (5-minute check, Etsy Shop Manager app):**
- Revenue today (vs. 7-day rolling average)
- Orders today
- Conversion rate today (if Etsy shows it — otherwise compute weekly)
- New Kit subscribers (from Kit dashboard)

Daily tracking catches anomalies — a viral post driving a revenue spike, a listing that went
dark in search. Daily data is not for decision-making; it is for anomaly detection only. Do
not adjust strategy from a single day's numbers.

**Weekly metrics (30 minutes, Sunday evening, Google Sheets):**
- Repeat purchase rate (count buyers who placed 2+ orders in the rolling 30-day window)
- Cohort mix (% of weekly orders per cohort tag — use Kit tag data)
- Top product by revenue this week (vs. last week)
- Email funnel: Campaign 1 open rate, Campaign 3 click rate, newsletter open rate
- Phase 1→Phase 2 conversion progress (cumulative: how many of the 47 have converted)

**Monthly metrics (2 hours, first Monday, Google Sheets deep dive):**
- Customer LTV by segment (from LTV tracker — manually updated with the month's Etsy orders)
- Churn rate by segment (subscribers who unsubscribed this month / total subscribers per segment)
- Seasonal trend analysis (did the month's dominant product align with the seasonal calendar?)
- Email engagement by cohort (open rate, CTR, unsubscribe rate per Kit cohort tag)
- Phase 3 readiness score (5-point checklist, scored each month from Day 30 onward)

### 5.2 Automation Alert Rules

These are threshold-based triggers that produce a specific response without waiting for the
weekly review. Build these as conditional formatting rules in the Google Sheets Daily tab, or
set Kit automation alerts where the platform supports them.

**Day 7 alert**: If cumulative Phase 2 orders at Day 7 are below 5, trigger the following:
(1) verify all listings are active in Etsy Shop Manager; (2) check whether the Phase 2 launch
email broadcast was delivered successfully in Kit; (3) run one social post that day featuring
the most visually compelling Phase 2 product. Do not adjust pricing within the first 7 days.

**Day 21 alert**: If Phase 1-to-Phase 2 conversion rate is below 5% at Day 21 (fewer than
3 of 47 returning buyers), trigger a Kit automation review: are Phase 1 buyers receiving
Campaign 3 (the cross-sell email)? If they are not in Kit, they cannot receive it. Manually
tag any Phase 1 buyer who has made contact via Etsy messages or reviews — add them to Kit
and fire Campaign 1 manually.

**Day 30 alert**: If overall 30-day repeat rate is below 10%, this is an early Churn Risk
signal. Open the LTV tracker and filter for Tier A buyers specifically. If Tier A repeat rate
is also below 10%, the cross-sell sequence has a product alignment problem. If Tier A repeat
rate is above 20% but overall is pulled down by Tier C, the problem is cohort mix (too many
low-intent buyers in the launch wave). Diagnose before adjusting.

**Day 30 monthly report**: Generate the monthly dashboard (Section 5.1 monthly layer) on
June 29. This is the first baseline report — it establishes the trajectory for the Day 45
and Day 60 Phase 3 decisions. File as `analytics/data/monthly-report-2026-06.md`.

### 5.3 Dashboard Platforms

**Google Sheets (launch through Month 3 minimum):**
All dashboard work described above runs in Google Sheets. The tool supports SUMIF, COUNTIF,
AVERAGEIF, and VLOOKUP — sufficient for all cohort LTV calculations, repeat rate computation,
and segment mix analysis at Phase 2 scale (under 200 orders/month). No pipeline required —
Etsy and Kit both export CSV, which Google Sheets imports directly.

**Upgrade trigger for Looker Studio:** Monthly orders above 200 sustained for 2 months, OR
manual CSV import time exceeds 45 minutes per week. At that point, the Etsy-to-Sheets
connector via Zapier (approximately $30/month) feeds Looker Studio automatically. The manual
workflow is not worth engineering effort below that threshold.

**Jupyter notebook (analytics/ directory):** The existing `analytics/dashboard-template.ipynb`
and `analytics/cohort-analysis-template.sql` are available for monthly deep-dive LTV analysis
when the LTV tracker exceeds 150 rows. Use `uv run python` as required by project CLAUDE.md —
never bare `python` invocations.

---

*Prepared: 2026-05-09, Session — this is the planning-layer document. The command-layer
document with full 6-campaign email system, Day 1 launch activation checklist, and Scenario
1/2/3/4 go/no-go protocol is `phase-2-customer-success-framework.md` (v2.0). The two documents
are complementary: this document answers "how do we predict and model Phase 2 success"; the
v2.0 document answers "what do we do operationally each day, week, and month."*

*Cross-references: `phase-2-analytics-strategy.md` (data architecture), `phase-2-buyer-retention-lifecycle-strategy.md`
(6-campaign email sequences), `customer-cohort-analysis-framework.md` (segment definitions),
`phase-3-decision-framework.md` (Options A/B/C/D), `analytics/monthly-metrics-checklist.md`
(monthly operator runbook).*
