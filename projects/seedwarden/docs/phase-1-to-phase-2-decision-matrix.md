---
title: "Seedwarden Phase 1 to Phase 2 Decision Matrix"
subtitle: "Explicit Go/No-Go Criteria with Numeric Thresholds"
date: 2026-04-28
status: production-ready
review-dates: [2026-06-01, 2026-07-01, 2026-08-01]
tags: [seedwarden, phase-1, phase-2, decision-matrix, go-no-go, gates]
---

# Seedwarden Phase 1 to Phase 2 Decision Matrix
**Three Decision Gates | May–August 2026**

**Purpose**: This document specifies the exact numeric criteria for authorizing Phase 2 (lifestyle photography sprint + iStock investment) and Phase 3 (product expansion) based on Phase 1 launch data. Every decision threshold is numeric. No judgment calls.

**How to use**: Check this document on the first Monday of each month after Phase 1 launches. Record the current values for each metric. Compare to thresholds. The decision rule is stated in the gate — follow it.

---

## Gate 1: Month 1 Check (June 1, 2026)

**Data window**: May 2026 (first 30 days of Phase 1 live on Etsy).

**Decision question**: Is Phase 1 showing minimum viable traction?

### Required Metrics to Collect (June 1)

Pull from Etsy Seller Dashboard Stats and Payment Account export for May 2026.

| Metric | How to Pull | May 2026 Actual | Gate Threshold |
|--------|------------|----------------|----------------|
| Total orders | Etsy Payment Account CSV — count rows | | ≥20 = Green; 10–19 = Yellow; <10 = Red |
| Blended conversion rate | Total orders / Total listing views × 100 | | ≥0.8% = Green; 0.5–0.79% = Yellow; <0.5% = Red |
| Any 5-star reviews received | Etsy > Shop > Reviews > count | | ≥3 = Green; 1–2 = Yellow; 0 = Red |
| Number of listings with ≥1 sale | From Payment Account CSV, count distinct listing titles | | ≥8 = Green; 4–7 = Yellow; <4 = Red |

### Gate 1 Decision Rules

**All Green (all 4 metrics at Green):**
Proceed to Gate 1 pass. Authorize: Phase 2 lifestyle photography planning. Begin 63-pin Pinterest batch build. Email list promotion is the Month 2 priority.

**Mixed (any Yellow, no Red):**
Continue monitoring. Do not change anything. Phase 2 planning proceeds at no cost (writing briefs, sourcing Canva templates). Do not spend any money on Phase 2 (no iStock credits, no tools upgrade). Check Gate 2 in July.

**Any Red:**
Hold Phase 2. Execute the listing audit protocol below before Gate 2.

### Listing Audit Protocol (triggered if Gate 1 is Red)

Run within 72 hours of Gate 1 Red.

Step 1: Identify the 5 listings with the highest view count in May.
Step 2: For each of those 5 listings, answer:
  - Does the cover image show the PDF content on a device or as a flat-lay? (Yes = pass, No = fix this week)
  - Does the listing title include a buyer-language keyword in the first 40 characters? (Yes = pass, No = rewrite title this week)
  - Is the price within $2–$3 of the median competitor price for that keyword on Etsy? (Check eRank or Marmalead)
  - Does the listing description include a cross-sell bundle mention? (Yes = pass, No = add one paragraph)

Step 3: Fix all failing items for the top-5 listings within 5 business days.
Step 4: Record the pre-fix and post-fix state. Track whether conversion rate improves in the following 2 weeks.

---

## Gate 2: Month 2 Check (July 1, 2026)

**Data window**: May + June 2026 cumulative (first 60 days).

**Decision question**: Does the data support authorizing the Phase 2 lifestyle photography investment?

### Required Metrics to Collect (July 1)

| Metric | How to Pull | Cumulative M1+M2 Actual | Gate Threshold |
|--------|------------|------------------------|----------------|
| Cumulative total orders | Etsy Payment Account CSV — count all orders May–June | | ≥50 = Green; 30–49 = Yellow; <30 = Red |
| Blended conversion rate (M2) | June orders / June views × 100 | | ≥1.0% = Green; 0.7–0.99% = Yellow; <0.7% = Red |
| Email subscriber count | Kit subscriber CSV — count all subscribers | | ≥80 = Green; 40–79 = Yellow; <40 = Red |
| Repeat buyer rate | Returning buyers / Total unique buyers × 100 (cumulative) | | ≥15% = Green; 8–14% = Yellow; <8% = Red |
| AOV trend (M1 vs. M2) | M2 AOV minus M1 AOV | | Positive = Green; Flat = Yellow; Negative = Red |
| Any Phase 2 product in top-3 revenue | Does any of the 5 high-ticket products ($16–$22) rank in the top 3 by revenue? | | Yes = Green; No = Yellow |

### Gate 2 Decision Rules

**Full Green-Light (4 or more metrics at Green, none at Red):**
Authorize Phase 2 lifestyle photography sprint. Proceed:
- Execute the physical photography sessions (Clusters A/B/C per `PHASE2_PHOTOGRAPHY_EXECUTION_PLAN.md`)
- Authorize iStock credit purchase for the 6 stock-photo products (priority order: Livestock Manual > Hunting/Trapping > Meat/Fish Preservation > Survival Garden > Native Plants)
- Begin Phase 3 product development in parallel (preservation derivatives, regional listings)
- Upgrade ConvertKit to Creator plan ($25/month) if list is above 500 subscribers

**Conditional Yellow (majority Yellow, no Red):**
Proceed with Phase 2 physical photography (zero cash cost — just time). Do NOT purchase iStock credits yet. Do NOT upgrade ConvertKit if not already on paid plan. Phase 3 development begins for zero-cost items only (writing preservation guide derivatives, creating regional listing copy).

**Red (any single metric at Red):**
Hold all Phase 2 cash expenditure. Continue Phase 2 zero-cost prep work (photography prop sourcing, Canva mockup templates). Diagnose the Red metric using the protocol table below.

### Red Metric Diagnostic Table

| Red Metric | Most Likely Cause | Diagnostic Action | Fix |
|-----------|------------------|-------------------|-----|
| Cumulative orders <30 | Low listing visibility | Check Etsy Stats: which listings have views but no orders? | Fix cover images and titles on lowest-converting high-traffic listings |
| Conversion rate <0.7% | Listing quality problem | Audit the same 5 listings as Gate 1 protocol; check if mockup images are primary image (position 1) | Regenerate mockup for the 3 worst-converting listings; test new cover image |
| Email subscribers <40 | Lead magnet CTA not visible | Is the Kit signup link on the final page of the top-3 selling PDFs? | Add CTA to PDFs; add signup mention to listing description |
| Repeat rate <8% | Post-purchase sequence not running | In Kit, check Automation 2 triggers | Verify "purchased" tag application; manually tag last 10 buyers |
| AOV declining | Bundle not being discovered | Are bundles appearing in "you may also like"? | Add explicit bundle upsell to top-5 individual listing descriptions |
| No high-ticket product in top-3 | Positioning or tag mismatch | Check keyword ranking of the 5 high-ticket products in eRank | Rewrite title of lowest-ranking high-ticket product; update tags to match buyer-language |

---

## Gate 3: Month 3 Check (August 1, 2026)

**Data window**: May + June + July 2026 cumulative (first 90 days).

**Decision question**: Does Phase 1 validate full Phase 3 expansion and Year 1 trajectory?

### Required Metrics to Collect (August 1)

| Metric | How to Pull | Cumulative M1–M3 Actual | Gate Threshold |
|--------|------------|------------------------|----------------|
| Cumulative total orders | Etsy Payment Account CSV — count all May–July orders | | ≥100 = Green; 60–99 = Yellow; <60 = Red |
| Repeat customer rate | Returning buyers / Total unique buyers | | ≥15% = Green; 10–14% = Yellow; <10% = Red |
| Email list size | Kit subscriber CSV | | ≥150 = Green; 80–149 = Yellow; <80 = Red |
| Top-3 product identification | Which 3 listings generate ≥60% of revenue? Are they identified? | | Clear top-3 = Green; Ambiguous = Yellow |
| Pinterest referral clicks | Monthly Pinterest outbound clicks in July (Etsy Stats) | | ≥50 clicks = Green; 20–49 = Yellow; <20 = Red |
| M3 monthly gross revenue | July gross revenue | | ≥$180 = Green; $100–$179 = Yellow; <$100 = Red |

### Gate 3 Decision Rules

**Full Green (5 or more metrics at Green):**
Full Phase 3 expansion authorized.
- Launch preservation derivatives (P3-01 through P3-04) on schedule per `docs/phase-3-product-expansion-roadmap.md`
- Launch all 14 regional listing variants (Survival Garden and Native Plants) in the same window
- Authorize Phase 3 social media sprint (TikTok/Instagram/Pinterest active posting per `PHASE2_TO_PHASE3_TRANSITION.md`)
- Record the top-3 products by conversion rate — these are the ad-ready listings (add to Etsy Ads at $1/day each)

**Conditional Yellow (majority Yellow, no critical Red):**
Phase 3 expansion proceeds with lower-risk items only:
- Regional listing variants (P3-05 through P3-18) proceed — zero development cost, existing PDFs, new keyword surfaces only
- Hold new-content preservation derivatives (P3-01 through P3-04) until Gate 3 trajectory improves
- Continue social media organic (no paid ad spend in Phase 3)

**Red (M3 gross revenue <$100 OR cumulative orders <60):**
Phase 3 expansion paused. Full diagnostic required.
- Return to Gate 1 listing audit protocol
- Do not create new products — optimize existing products first
- Target: bring the 5 lowest-converting high-view listings to ≥0.8% conversion before adding new SKUs
- Re-check readiness in Month 4 using the same Gate 3 metrics

---

## Go/No-Go Summary Table

This is the single-page reference for the three gates. Print or bookmark this for monthly reviews.

| Gate | Date | Go Threshold | No-Go Threshold | Decision |
|------|------|-------------|----------------|---------|
| **Gate 1** | June 1, 2026 | ≥20 sales in May | <10 sales in May | Green: proceed Phase 2 planning. Red: listing audit first. |
| **Gate 2** | July 1, 2026 | ≥50 cumulative sales | <30 cumulative sales | Green: full Phase 2 photography sprint. Red: hold cash spend. |
| **Gate 3** | August 1, 2026 | ≥100 cumulative sales + ≥15% repeat rate | <60 cumulative sales OR <10% repeat rate | Green: full Phase 3 expansion. Red: optimize before expanding. |

---

## Investment Authorization Summary

Each gate authorizes a specific set of actions. Nothing in Phase 2 or Phase 3 requires authorization before the relevant gate is passed.

| Investment Item | Authorization Gate | Cash Cost | Time Cost |
|----------------|------------------|-----------|-----------|
| Phase 2 physical photography sessions (time only) | Gate 2 Yellow or Green | $0 | 2–3 days |
| iStock credits for 6 stock-photo products | Gate 2 Full Green only | $48–$150 | 4–6 hours sourcing |
| ConvertKit Creator plan upgrade | Gate 2 Green + >500 subscribers | $25/month | 0 |
| Phase 3 regional listing variants (14 listings) | Gate 3 Yellow or Green | $2.80 listing fees | 19 hours |
| Phase 3 new-content preservation guides (4 products) | Gate 3 Full Green only | $0.80 listing fees | 22 hours dev |
| Etsy Ads activation on top-3 converting listings | Gate 3 Green, top-3 identified | $1–$3/day per listing | 1 hour setup |
| Phase 3 social media active sprint (TikTok + IG) | Gate 3 Green | $0–$100/month (optional tools) | 5–10 hours/week |

---

## Contingency: What If Phase 1 Significantly Underperforms?

If Gate 3 (August 1) shows cumulative orders below 40 and conversion rate below 0.5%, something structural is wrong. The contingency protocol:

**Step 1 — Diagnosis (Week 1 after Gate 3 Red):**
- Pull eRank or Marmalead data on the top 5 keywords for the top 5 listings. Are those listings appearing in search at all?
- Check whether any listings were deactivated by Etsy (intellectual property flag, policy issue, or payment account hold)
- Verify the Etsy shop policies are complete and the shop announcement is visible

**Step 2 — Reset (Week 2):**
- Deactivate the 5 lowest-performing listings (free up algorithm weight for better performers)
- Rewrite titles and tags on the 5 highest-potential listings using exact keyword phrases verified in eRank
- Regenerate mockup images for the 3 products with the best content-to-conversion potential (Companion Planting Chart, Seed Saving Field Manual, Harvest Preservation)

**Step 3 — Relaunch (Week 3):**
- Re-activate deactivated listings with improved copy
- Publish 10 new Pinterest pins specifically for the 3 reformed listings
- Send a launch announcement to the email list (even if small — 10–40 subscribers)

**Step 4 — Recheck (Week 6 after Step 3):**
If conversion rate has not improved to ≥0.5% with the reformed listings after 6 weeks: the issue may be product-market fit at the content level, not listing quality. At that point, conduct a structured survey of 5–10 people in the target audience (post in r/homesteading, r/gardening, or foraging Facebook groups) to understand whether the product descriptions match buyer expectations.

---

## Reference: Phase 2 and Phase 3 Prerequisites

For completeness, the prerequisites from other documents that must be true regardless of gate outcomes:

**Phase 2 Photography Prerequisites (from `PHASE2_PHOTOGRAPHY_EXECUTION_PLAN.md`):**
- Etsy account verification complete (user action required)
- Phase 1 tag corrections applied (user action required)
- At least 7 days of live listing data available before deciding photography priority order
- Physical photography props available: wooden cutting board or butcher block, neutral fabric/linen, small potted herb

**Phase 3 Product Prerequisites (from `docs/phase-3-product-expansion-roadmap.md`):**
- Phase 1 is live (Etsy account verified, at least 21 products published)
- At least 30 days of Phase 1 conversion data (needed to identify which keyword categories are converting)
- Native Plants Regional Guide PDF confirmed at 4.91 MB (Etsy-compliant) — verified in Session 560, confirmed compliant
- Wild-edibles habit photo set confirmed complete (18/18) — confirmed in Session 560

---

*Document complete. Review dates: June 1, July 1, August 1, 2026. Cross-references: `docs/phase-1-revenue-roadmap.md`, `docs/kpi-dashboard.md`, `data/90-day-forecast.csv`, `PHASE2_PHOTOGRAPHY_EXECUTION_PLAN.md`, `docs/phase-3-product-expansion-roadmap.md`.*
