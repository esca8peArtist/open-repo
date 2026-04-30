---
title: "Bundle A/B Test Plan — Phase 2, Months 1–3"
date: 2026-04-30
status: production-ready
context: Operationalizes PHASE_2_BUNDLE_STRATEGY.md into testable experiments with decision criteria
references: PHASE_2_BUNDLE_STRATEGY.md, financial-sustainability-model.md, bundle-listings.md
---

# Bundle A/B Test Plan — Phase 2, Months 1–3

## Executive Summary

This document operationalizes the Phase 2 bundle strategy into three sequential A/B tests spanning May–July 2026, with explicit success metrics and decision criteria. The tests are designed to generate actionable Phase 1 data about buyer bundle behavior across seasonal contexts.

**Key constraint**: Etsy does not support native A/B testing of listing variants, so tests are sequential (one bundle live at a time, each with a 4-week observation window). This provides directional data across seasonal contexts, not simultaneous controlled experiments.

**Test timeline**:
- **Month 1 (May 1–31)**: Spring Forager Bundle test vs. control
- **Month 2 (June 1–30)**: Harvest Season Bundle launch + seasonal tracking
- **Month 3 (July 1–31)**: Harvest Season Bundle pricing test ($28 → $25)

**Decision gate**: After Month 1, if Spring Forager Bundle data is negative, pause bundle strategy and investigate. After Month 3, make permanent bundle pricing/strategy decision based on cumulative data.

---

## Part 1: Month 1 Test — Spring Forager Bundle A/B Test

### Test Design

**Control group** (baseline): Wild Edibles Quick Reference Guide ($18) and Zone-by-Zone Seed Starting Calendar ($7) listed individually. These two products exist as separate Etsy listings with standard product photography and descriptions.

**Test group**: Spring Forager Bundle at $22 (the two products above combined). The bundle has a dedicated Etsy listing with:
- Title: "Spring Forager Bundle — $22 (Saves $3)"
- Description follows the pricing psychology framework (PHASE_2_BUNDLE_STRATEGY.md Part 3): lead with dollar savings, not percentage
- Both products are listed individually alongside the bundle — no removal of the control condition
- Bundle listing uses the same lifestyle photos as the individual product listings (requires photo shoot completion; see Track B blockers)

### Success Metrics

**Primary metrics** (track daily):
- **Bundle listing page views** — baseline expectation: 2–4% of total Wild Edibles + Zone Calendar combined views
- **Bundle listing conversion rate** — success threshold: ≥3% (i.e., 3+ purchases per 100 bundle views)
- **Individual product conversion rate** — success threshold: no decline vs. pre-test baseline (week of April 21–27; capture via Etsy analytics export)

**Secondary metrics** (track daily):
- **Cannibalization signal**: If individual product conversions drop >15% during test period, the bundle is stealing volume from individual sales rather than driving incremental purchases
- **Average order value (AOV) from bundle buyers**: success threshold: ≥$22 (the bundle price). If buyers purchase the bundle + other items, AOV exceeds $22 and the bundle is a cart multiplier
- **Bundle buyers who purchased both products individually in previous months**: if >10% of bundle buyers also own individual copies, the test has a "double-buyer" problem (pricing is not optimized)

### Data Collection

**Etsy analytics** (automated export, weekly):
- List view count (by listing)
- Conversion count (by listing)
- Conversion rate (Etsy-calculated, %)
- Average order value (by listing)
- Buyer geography (to identify cohort-specific patterns)

**Manual tracking** (post-purchase follow-up, optional):
- Bundle buyer post-purchase survey: "What was the primary reason you chose the bundle?" (options: convenience, savings, both guides seemed useful together, wasn't sure which one I needed)
- Individual buyer intent: Do buyers who purchase the Zone Calendar separately mention foraging in their purchase notes or follow-up purchases?

**Date range for analytics**:
- Pre-test baseline (control period): April 21–27, 2026 (final week before bundle launch)
- Test period (bundle live): May 1–31, 2026 (full month)
- Post-test period (optional comparison): June 1–15, 2026 (if comparing against post-test individual sales when bundle is still live)

### Decision Criteria

**Success case** (proceed with bundle strategy):
- Bundle conversion rate ≥3% AND
- Individual product conversion rates do not decline >10% AND
- No cannibalization signal (individual conversions are maintained or increase)
- → **Action**: Keep Spring Forager Bundle live. Plan Harvest Season Bundle launch for June 1 as scheduled.

**Ambiguous case** (conversion met, but AOV signals cannibalization):
- Bundle converts at 3%+ but individual product conversions drop 10–15% AND
- AOV does not increase (bundle does not drive secondary purchases)
- → **Action**: Bundle is stealing volume from individual sales. Do NOT launch Harvest Season Bundle in June. Instead, run a 2-week pause test: remove bundle listing and measure if individual sales revert to baseline. If yes, reduce bundle discount from $3 to $1–2 (e.g., $24 instead of $22) and retry in Month 2.

**Failure case** (do not proceed):
- Bundle conversion <3% OR
- Individual product conversions decline >15% OR
- Clear cannibalization with declining AOV
- → **Action**: Remove Spring Forager Bundle listing immediately. Do NOT launch Harvest Season Bundle in June. Write post-mortem analysis: "Why did the bundle fail?" (pricing, seasonal timing, product pairing, or photography/description gap). Investigate root cause before proceeding to Phase 2.5 bundle experiments.

---

## Part 2: Month 2 — Harvest Season Bundle Launch + Seasonal Tracking

### Launch Timeline

**June 1, 2026**: Harvest Season Bundle goes live ($28, $10 off individual total of $38).

**No active A/B test in June** — this bundle launches on seasonal timing, not test-driven timing. June is too early in the cumulative data collection period to have a clean comparative baseline. However, use June as an opportunity to verify the bundle listing is functional and to establish a seasonal baseline for preservation category revenue.

### Observational Tracking (Not a Statistical Test)

**Track preservation category revenue** (three products: Fermented Harvest Handbook $13 + Preservation Field Manual $15 + Hot Sauce Guide $10):

**May baseline**: Total preservation category revenue (sum of three individual products). If Phase 1 is live with lifestyle photos, this is the clean seasonal starting point.

**June performance**: Total preservation category revenue with Harvest Season Bundle live.

**Decision rule — seasonal demand validation**:
- If June preservation revenue exceeds May by >30% (seasonality-adjusted), the seasonal demand hypothesis is validated and the bundle is visible/valuable to buyers
- If June ≈ May (flat, <10% difference), seasonal demand may not exist or the bundle is not surfacing it — plan pricing test (below) with skepticism; consider whether the bundle description/title is capturing search interest

**Why this is not a formal test**: The bundle launching itself may drive June revenue changes independent of true seasonal demand. By Month 3, when we do the pricing test, we will have a full 8-week baseline (May + June) to compare against.

### Decision Checkpoint (End of Month 2)

**Go/no-go decision on pricing test**:
- If June preservation revenue > May by 30%+: proceed with Month 3 pricing test as planned
- If June preservation revenue ≈ May (flat): proceed with pricing test anyway (a lower price may stimulate demand), but set a higher bar for the test success threshold (40%+ increase in unit volume at the lower price to justify revenue parity)

---

## Part 3: Month 3 — Harvest Season Bundle Pricing Test

### Test Design

**Week 1–2 of July (July 1–14)**: Harvest Season Bundle at $28 (control baseline).

**Week 3–4 of July (July 15–31)**: Harvest Season Bundle at $25 (test price). Both weeks are included in the same month for easier analytics extraction.

**Rationale**: Testing price on a defined product (three-product bundle) with 8 weeks of prior data (May + June) available for comparison. This is the most actionable price test in the first 90 days because the product is stable and historical context is available.

### Success Metrics

**Primary metric**: Total bundle revenue (units × price) at $25 vs. $28.

- **$28 price performance** (July 1–14): Record unit sales and total revenue
  - Example: 8 units sold at $28 = $224 revenue
- **$25 price performance** (July 15–31): Record unit sales and total revenue
  - Example: 12 units sold at $25 = $300 revenue

**Unit elasticity calculation**:
- Percent change in units: (12 − 8) / 8 = 50% increase
- Percent change in price: (25 − 28) / 28 = −10.7% decrease
- Price elasticity: 50% / 10.7% = 4.7 (unit demand is elastic — a 10% price drop yields 50% more units)
- Revenue direction: $224 → $300 is a revenue increase, so lower price captures more total revenue

**Secondary metrics**:
- **Total preservation category revenue at $25 vs. $28**: Does the lower bundle price drive higher volume in related categories (buyers buying the bundle + other preservation guides)?
- **AOV of bundle buyers at $25 vs. $28**: Is the average order value maintained, or do $25 buyers spend less than $28 buyers?

### Decision Criteria

**Success case** ($25 is the optimal price):
- Units sold at $25 increase >30% vs. $28 (e.g., 8 units → 12+ units) AND
- Total revenue at $25 exceeds revenue at $28 (e.g., $300 > $224) AND
- AOV of bundle buyers is maintained or increases
- → **Action**: Change permanent bundle price to $25. Leave live through end of Phase 2. Plan Phase 3 strategy update with $25 as the baseline.

**Parity case** (both prices perform similarly):
- Units sold at $25 increase <20% vs. $28 (e.g., 8 units → 9 units) AND
- Total revenue at $25 ≈ $28 (within ±5%, e.g., $240 vs. $224)
- → **Action**: Keep bundle price at $28 (higher revenue per transaction). The price is optimized. If anything, test a $29 or $30 price in Phase 3 to capture even higher revenue with minimal volume loss.

**Failure case** ($28 is the optimal price):
- Units sold at $25 increase but not enough to offset the lower price (e.g., 8 units → 10 units, revenue $250 vs. $224 = only $26 more)
- OR total revenue at $25 drops vs. $28
- OR AOV of $25 buyers is significantly lower (buyers are less engaged, less likely to add secondary purchases)
- → **Action**: Keep bundle price at $28. If demand feels soft at $28, investigate bundle description/title/visibility rather than lowering price further.

---

## Part 4: Data Collection Infrastructure

### Etsy Analytics Export Workflow

**Weekly exports** (every Sunday):
1. Log into Etsy Seller Dashboard
2. Navigate to **Stats** → **Sales**
3. Filter by listing (Spring Forager Bundle, then Harvest Season Bundle, then individual products)
4. Export by listing for the week (CSV)
5. Paste results into **BUNDLE_TEST_DATA.csv** (created below)

**Data to capture per listing, per week**:
- Listing name
- Views (page views)
- Conversions (purchase count)
- Conversion rate (%)
- Revenue
- Average order value
- Date range

### Tracking File: BUNDLE_TEST_DATA.csv

**Create file**: `/home/awank/dev/SuperClaude_Framework/projects/seedwarden/BUNDLE_TEST_DATA.csv`

**Headers**:
```
Week,Listing_Name,Views,Conversions,Conversion_Rate,Revenue,AOV,Notes
```

**Example rows**:
```
2026-04-21 to 04-27,Wild Edibles Guide,145,5,3.4%,$90,$18,Pre-test baseline
2026-04-21 to 04-27,Zone Calendar,87,3,3.4%,$21,$7,Pre-test baseline
2026-05-01 to 05-07,Spring Forager Bundle,32,1,3.1%,$22,$22,Test launch week
2026-05-01 to 05-07,Wild Edibles Guide,121,4,3.3%,$72,$18,Individual performance during test
```

**Update frequency**: Weekly, every Sunday evening. Use this file to generate weekly decision summaries.

### Weekly Decision Summary (Template)

**Week of May 1–7** (Month 1 Test Week 1):
- Bundle conversion: 3.1% ✓ on target
- Individual Wild Edibles conversions: 3.3% (baseline was 3.4%, acceptable variance)
- Cannibalization signal: None detected
- AOV impact: Bundle buyers purchasing both at once; no secondary cart items yet
- **Decision**: Continue test as planned.

---

## Part 5: Post-Test Analysis and Handoff

### Month 1 Post-Test Report (Due June 1)

**If success**: "Spring Forager Bundle passed all success criteria. Recommend keeping bundle live through end of Phase 2. Proceed with Harvest Season Bundle launch as scheduled."

**If failure**: "Spring Forager Bundle did not meet success threshold [specify which metric failed]. Root cause analysis: [pricing | seasonal timing | product pairing | photography gap]. Recommendation: [retry with adjustment | remove bundle | investigate before Month 2]."

### Month 3 Post-Test Report (Due August 1)

**If $25 succeeds**: "Harvest Season Bundle pricing optimized at $25. Recommend expanding bundle strategy in Phase 3 with the three bundles as permanent offerings."

**If $28 remains optimal**: "Harvest Season Bundle performs best at $28. Consider testing $29–30 in Phase 3 to further optimize revenue."

### Cumulative Phase 2 Bundle Summary (Delivered after Month 3)

**Document**: `/home/awank/dev/SuperClaude_Framework/projects/seedwarden/PHASE_2_BUNDLE_TEST_RESULTS.md`

Contents:
- Executive summary of all three tests
- Cohort-specific insights (which bundle types drove which customer segments?)
- Revenue impact (% change in total revenue from bundles vs. individual products)
- Recommendations for Phase 3 bundle strategy
- List of any new bundle hypotheses to test in Phase 3

---

## Appendix: Success Threshold Calibration

These thresholds are based on Etsy digital product benchmarks and Seedwarden's financial-sustainability-model.md baseline assumptions.

**3% bundle conversion rate baseline**: Etsy digital product conversion rates average 2–4%. A 3% conversion on a new bundle listing is at the healthy upper end. If a bundle does not reach 3%, it is underperforming relative to similar-price Etsy digital listings.

**$22 AOV on Spring Forager Bundle**: The bundle itself is $22. If a buyer purchases the bundle and nothing else, AOV = $22. If AOV exceeds $22, the bundle is a cart multiplier (it drives secondary purchases).

**30% revenue increase for seasonal signal**: A 30% increase in preservation category revenue from May to June is a clear signal that seasonal demand exists and is being captured. Anything less than 20% requires investigation: Is the bundle visible? Are buyers searching for these terms in June?

**30% unit elasticity threshold for pricing**: If a $3 price cut (12% decrease) yields a 30%+ increase in unit sales, the price cut captures more total revenue. This threshold accounts for natural variance in Etsy sales (some weeks are higher-demand than others) while still identifying a clear price signal.

---

## Timeline Checklist

**April 30, 2026 (Today)**:
- ✓ Bundle A/B Test Plan created and committed
- ✓ BUNDLE_TEST_DATA.csv template ready for May 1 launches

**May 1, 2026**:
- [ ] Spring Forager Bundle listing created on Etsy
- [ ] Bundle description updated with pricing psychology framing
- [ ] First analytics export captures April 21–27 baseline (Wild Edibles + Zone Calendar)
- [ ] BUNDLE_TEST_DATA.csv tracking begins

**May 8, 2026**:
- [ ] First weekly data entry (May 1–7)
- [ ] Weekly decision summary written

**May 31, 2026**:
- [ ] Final May analytics export and data entry
- [ ] Month 1 Post-Test Report completed
- [ ] Decision made: proceed or pivot?

**June 1, 2026** (if Month 1 succeeds):
- [ ] Harvest Season Bundle listing created on Etsy
- [ ] June baseline tracking begins

**June 30, 2026**:
- [ ] Final June analytics export
- [ ] Seasonal demand analysis completed
- [ ] Decision: proceed with pricing test?

**July 1–14, 2026**:
- [ ] Harvest Season Bundle at $28 (control week)
- [ ] Daily unit sales tracked manually

**July 15–31, 2026**:
- [ ] Harvest Season Bundle price changed to $25
- [ ] Daily unit sales tracked manually

**August 1, 2026**:
- [ ] Month 3 Post-Test Report completed
- [ ] Permanent pricing decision made
- [ ] Cumulative Phase 2 Bundle Test Results summary written

---

## Notes for Implementation

**Photography dependency**: All bundle listings require lifestyle photos (Track B blocker 02). If photos are not available by May 1, use high-quality product-shot imagery as fallback. The bundle concept still works without lifestyle photos, but conversion rates will be lower than the benchmarks in this plan.

**Etsy listing variant strategy**: Consider using Etsy listing variants (if available in the jurisdiction) rather than separate bundle listings. Variants allow one product page to show multiple price points without creating new listings. If variants are available by May 1, use them for the pricing test (Part 3) instead of separate listings.

**Rollback plan**: If at any point a bundle test fails catastrophically (conversion rate <1%, immediate buyer complaints), remove the bundle listing and revert to individual product pricing. No downside to removing a bundle; focus on improving bundle product pairing or description before retrying.

