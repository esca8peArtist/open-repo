---
title: "Seedwarden Monthly KPI Dashboard"
subtitle: "12-Metric Tracking Checklist with Decision Logic"
date: 2026-04-28
status: production-ready
cadence: first-Monday-of-each-month
estimated-time: 80 minutes
tags: [seedwarden, kpi, dashboard, monthly-review, decision-rules]
---

# Seedwarden Monthly KPI Dashboard
**12 Metrics | Decision Logic for Every Alert | Run Monthly from May 2026**

**When to run**: First Monday of each month using prior month's complete data.
**Estimated time**: 80 minutes.
**Tools required**: Etsy Seller Dashboard (CSV export), Kit (ConvertKit) dashboard, Pinterest Business Analytics, spreadsheet.
**Output**: Completed Monthly Scorecard row (append to the log at the bottom), plus Actions Arising.

---

## Pre-Run Setup (5 minutes)

Pull these exports before starting. They take a few minutes to generate — start them first.

- [ ] Etsy > Shop Manager > Finances > Payment Account > Download Statement (prior month CSV)
- [ ] Etsy > Shop Manager > Stats > prior month (record manually or export if available)
- [ ] Kit > Subscribers > Export CSV
- [ ] Kit > Reports > prior month open rates and CTR (record manually)
- [ ] Pinterest Business Analytics > prior month (outbound clicks and saves)

---

## Metric 1: Blended Conversion Rate

**Definition**: Total orders placed / Total listing views across all listings × 100

**How to calculate**: From Etsy Stats, record total visits for each listing. Sum all listing visits = total views denominator. Divide total orders (from Payment Account CSV, count unique orders) by total views.

**Healthy range**: 0.8–2.5%
**Alert threshold**: Below 0.5%
**Action if below 0.5%**: Open the 5 listings with the highest view count this month. For each: check that cover image is a mockup (not a white background), check that the title includes the primary keyword in the first 40 characters, check that tags match buyer-language search terms (not internal category labels). Identify the listing with the highest views and lowest conversion — fix that one first.

| Month | Views | Orders | Conversion Rate | Status |
|-------|-------|--------|----------------|--------|
| May 2026 | | | | |
| Jun 2026 | | | | |
| Jul 2026 | | | | |
| Aug 2026 | | | | |
| Sep 2026 | | | | |
| Oct 2026 | | | | |

---

## Metric 2: Average Order Value (AOV)

**Definition**: Gross revenue / Total number of orders

**How to calculate**: Sum all gross revenue from the Etsy Payment Account CSV. Divide by the count of orders in the same period.

**Healthy range**: $14–$35
**Alert threshold**: Below $12
**Action if below $12**: AOV below $12 means very few bundle sales. Check bundle listing views: if bundles have fewer than 10 views, add a "bundle available" line to the description of the 5 highest-selling individual products. If bundles have views but no conversions, audit the bundle cover image and headline — buyers may not understand the value.

**Target progression**: $14 (M1) → $18 (M3) → $22 (M6, as bundle share grows)

| Month | Gross Revenue | Orders | AOV | Status |
|-------|--------------|--------|-----|--------|
| May 2026 | | | | |
| Jun 2026 | | | | |
| Jul 2026 | | | | |

---

## Metric 3: Repeat Buyer Rate

**Definition**: Number of buyers who have placed more than one lifetime order (across all months) / Total unique buyers this month × 100

**How to calculate**: From the Etsy Payment Account CSV, pull all buyer email addresses. Cross-reference against prior months' CSV exports. Count buyers who appear in more than one month's data = repeat buyers. Divide by this month's total unique buyer count.

**Healthy range**: 15–25% by Month 3
**Alert threshold**: Below 8% by Month 3
**Action if below 8% at Month 3**: Diagnose the post-purchase email sequence in Kit. Check: (1) Is the "purchased" behavioral tag being applied? (2) Is Automation 2 (post-purchase sequence) sending? (3) Check the Day 7 cross-sell email — open it and verify the product recommendation is relevant to what the buyer purchased. If the sequence is not running for all buyers, the root cause is likely the Zapier integration (if using) or manual tag application not covering all purchases.

| Month | Repeat Buyers | Unique Buyers | Repeat Rate | Status |
|-------|--------------|---------------|------------|--------|
| May 2026 | | | | |
| Jun 2026 | | | | |
| Jul 2026 | | | | |

---

## Metric 4: Email Signup Rate

**Definition**: New Kit subscribers acquired this month / New Etsy buyers this month × 100

**How to calculate**: From Kit subscriber CSV, count subscribers with `subscribed_at` date in the prior calendar month = new subscribers. From Etsy CSV, count unique buyer emails in the month = new Etsy buyers. Divide.

**Note**: Not all Etsy buyers will become email subscribers — they would need to see the lead magnet CTA in the PDF they downloaded and opt in separately. A rate above 20% indicates the CTA placement is working. Below 10% indicates the CTA is not visible or compelling.

**Healthy range**: 20–35%
**Alert threshold**: Below 10%
**Action if below 10%**: (1) Verify the lead magnet CTA is present on the final page of the top-5 selling PDFs with a direct link to the Kit signup form. (2) Verify the Kit form link is live. (3) Consider adding the lead magnet to the Etsy listing description ("get our free [X] by signing up at [link]"). (4) Check whether the free lead magnet is linked from the Etsy shop announcement.

| Month | New Kit Subscribers | New Etsy Buyers | Signup Rate | Status |
|-------|--------------------|-----------------|-----------  |--------|
| May 2026 | | | | |
| Jun 2026 | | | | |
| Jul 2026 | | | | |

---

## Metric 5: Pinterest Saves per Top Product

**Definition**: Total Etsy listing saves attributed to Pinterest for each product (from Etsy Stats > Traffic Sources breakdown per listing)

**How to calculate**: In Etsy Stats, select each listing individually. Check Traffic Sources for "Pinterest" or "Social" as the referral source. Record the number of saves/clicks from Pinterest for the top 3 listings.

**Healthy range**: 5+ Pinterest-attributed saves per top listing per month
**Alert threshold**: Below 2 saves across all listings for the month
**Action if below 2**: Pinterest indexing is either incomplete or pins have no traction. Check: (1) Are the 63 pins from the batch-build plan live and published (not drafts)? (2) Do pins have keyword-rich descriptions? (3) Are pins on public boards with keyword-rich board names? (4) Has it been less than 30 days since pins were published? Pinterest takes 30–90 days to index new pins — patience is appropriate in Month 1.

**Note**: Pinterest analytics for saves require Pinterest Business account, which must be set up and connected to the Etsy shop URL.

| Month | Top Product Saves (Pinterest) | Total Pinterest-Referral Saves | Status |
|-------|-------------------------------|-------------------------------|--------|
| May 2026 | | | |
| Jun 2026 | | | |
| Jul 2026 | | | |

---

## Metric 6: Pinterest Outbound Clicks to Etsy

**Definition**: Total clicks from Pinterest pins to the Etsy shop (tracked via Pinterest Business Analytics > Outbound Clicks, or via Etsy Stats > Traffic Sources)

**How to calculate**: Pinterest Business Analytics > Audience > Outbound Clicks (set to the prior calendar month). Cross-check against Etsy Stats > Traffic Sources > "Pinterest" row.

**Healthy range**: 25+ clicks/month by Month 2, 75+ by Month 3
**Alert threshold**: Below 10 clicks by Month 2
**Action if below 10 by Month 2**: (1) Create 3 additional pin variants for the top-converting Etsy product. (2) Check whether the existing pins link directly to the Etsy listing (not to the shop home page — listing links outperform shop home links by 2–3x in click rate). (3) Promote one pin with a $10 test spend using Pinterest Ads to verify the audience exists before investing further in organic.

| Month | Pinterest Outbound Clicks | MoM Change | Status |
|-------|--------------------------|------------|--------|
| May 2026 | | — | |
| Jun 2026 | | | |
| Jul 2026 | | | |

---

## Metric 7: Top-3 Listing Revenue Concentration

**Definition**: Revenue from the 3 highest-revenue listings this month / Total gross revenue × 100

**How to calculate**: From Etsy Payment Account CSV, aggregate revenue by listing title. Identify top 3. Sum top-3 revenue. Divide by total gross revenue.

**Healthy range**: 30–50% (healthy concentration without over-dependence)
**Alert threshold (high)**: Above 70% (dangerous over-dependence on 3 listings — one ranking change tanks the store)
**Alert threshold (low)**: Below 20% (revenue is too dispersed — no clear winners to scale with ads)
**Action if above 70%**: Begin investing mockup and title work in listings currently ranked 4–10 by views. The goal is to develop a second tier of converting listings before the top-3 listings decline.
**Action if below 20% and revenue is acceptable**: This is actually a healthy sign of catalog diversity. No action needed unless overall conversion rate is low.

| Month | Top-3 Revenue | Total Revenue | Concentration % | Status |
|-------|--------------|---------------|----------------|--------|
| May 2026 | | | | |
| Jun 2026 | | | | |
| Jul 2026 | | | | |

---

## Metric 8: Listing Health Score

**Definition**: Number of listings where conversion rate ≥ 0.8% (over the prior 30 days, minimum 50 views) / Total listings with ≥ 50 views × 100

**How to calculate**: Pull views and orders per listing from Etsy Stats. Calculate conversion rate per listing. Count how many have ≥ 50 views AND ≥ 0.8% conversion rate. Divide by total listings with ≥ 50 views. Note: In Month 1, most listings may not have 50 views yet — flag as N/A and track from Month 2 onward.

**Healthy range**: 30%+ of listings meeting the conversion threshold
**Alert threshold**: Below 15%
**Action if below 15%**: Run systematic listing triage: for each listing with ≥ 50 views and <0.5% conversion, check the cover image (is it a mockup showing the content?), title (does it include the primary buyer search term in the first 40 characters?), and price (is it competitive for the keyword category?). Fix the worst-performing listing each week.

| Month | Listings ≥50 Views | Listings ≥0.8% Conv | Health Score | Status |
|-------|--------------------|--------------------|-------------|--------|
| May 2026 | | | | |
| Jun 2026 | | | | |
| Jul 2026 | | | | |

---

## Metric 9: Review Accumulation Rate

**Definition**: Cumulative review count at end of each month

**How to calculate**: Etsy > Shop Manager > Reviews > All Reviews. Count total reviews received (star rating and text). Record cumulative count.

**Target trajectory**: M1: 3+, M2: 10+, M3: 20+, M6: 50+, M12: 120+
**Alert threshold**: Zero reviews at cumulative 20+ sales
**Action if zero reviews at 20+ sales**: (1) Verify Automation 2 (post-purchase email sequence) is running in Kit — specifically that the Day 21 review request email is being sent. (2) Check whether the "purchased" behavioral tag is being applied to buyers. (3) Manually send a review request to the first 5–10 buyers using Etsy Messages: "Hi — if you had a chance to use [product name], I'd really appreciate a quick review. It helps other buyers find the guide."

**Note on review strategy**: Do not ask for a specific star rating. Etsy's policies prohibit requesting only positive reviews. "Honest review" language is compliant and more trustworthy.

| Month | New Reviews | Cumulative Reviews | Avg Star Rating | Status |
|-------|-------------|-------------------|----------------|--------|
| May 2026 | | | | |
| Jun 2026 | | | | |
| Jul 2026 | | | | |

---

## Metric 10: Net Revenue per Order

**Definition**: (Gross revenue − Etsy transaction fee − Etsy payment processing fee) / Total orders

**Etsy fee structure**:
- Transaction fee: 6.5% of sale price
- Payment processing: 3% + $0.25 per order
- Effective take-home: ~88.7% of sale price minus $0.25 per order

**Example**: $14.00 sale → $0.91 transaction fee → $0.42 + $0.25 processing = $1.58 total fees → net = $12.42 (88.7%)

**Healthy range**: $12–$30 net per order (corresponding to $14–$34 gross AOV)
**Alert threshold**: Below $10 net per order sustained for 2+ months
**Action if below $10**: Usually means low-AOV product mix or a refund event. Check (1) whether the low-price products ($5 Companion Chart, $7 Planner) are dominating orders without any bundle attachment — if so, add stronger bundle upsells. (2) Check for any chargebacks or refund disputes in the Etsy Payment Account. (3) If refunds are above 2% of orders, check whether the listing descriptions accurately describe what buyers receive.

| Month | Gross Revenue | Total Orders | Etsy Fees | Net Revenue | Net per Order | Status |
|-------|--------------|-------------|-----------|-------------|--------------|--------|
| May 2026 | | | | | | |
| Jun 2026 | | | | | | |
| Jul 2026 | | | | | | |

---

## Metric 11: Email Welcome Sequence Open Rate (Email 1)

**Definition**: Percentage of new subscribers in the prior month who opened Email 1 of the welcome sequence

**How to calculate**: Kit > Automations > [Welcome Sequence] > Email 1 > Open Rate. Filter to subscribers who received it within the prior calendar month.

**Healthy range**: 45%+ (first email in a welcome sequence receives highest open rates — if it's below 45%, it usually means a deliverability or subject line problem)
**Alert threshold**: Below 30%
**Action if below 30%**: (1) Test subject line: the current subject line may be triggering spam filters or not compelling enough. Write two alternatives and A/B test the next 20 subscribers. (2) Send a test email to a personal Gmail and a Protonmail — check if it lands in spam. (3) Verify the from-name is recognizable: "Seedwarden" is cleaner than a generic "noreply" sender. (4) Reduce Email 1 to a single CTA — if the email has 5 links and 3 asks, it may be triggering spam scoring.

**Secondary metric**: Email 5 coupon redemption rate (SEEDWARDEN15 coupon). Target: 8%+ of subscribers who receive Email 5. Check in Etsy Coupons report.

| Month | New Subs | Email 1 Open Rate | Email 5 Coupon Redemptions | Status |
|-------|---------|------------------|--------------------------|--------|
| May 2026 | | | | |
| Jun 2026 | | | | |
| Jul 2026 | | | | |

---

## Metric 12: Bundle Revenue Share

**Definition**: Revenue from bundle listings (Apartment Grower $32, Food Sovereignty $30, Regional Self-Sufficiency $28, Preservation $38, Homesteader's Complete $50) / Total gross revenue × 100

**How to calculate**: From Etsy Payment Account CSV, filter orders by listing title matching any of the 5 bundle names. Sum their revenue. Divide by total gross revenue.

**Healthy range**: 20–35% by Month 3 (bundles are a significant revenue driver but not dominant)
**Alert threshold**: Below 10% by Month 3
**Action if below 10% at Month 3**: Bundles are not being discovered. Check (1) whether bundle listings have their own mockup images (each bundle needs its own cover image, not a reuse from an individual product). (2) Add "see full bundle at [link]" to the description of the top-3 individual products. (3) In the Kit Day 7 post-purchase cross-sell email, is a bundle the specific recommendation? If the email recommends only individual products, upgrade the email to feature the relevant bundle.

**Positive signal**: Bundle revenue share above 35% by Month 6 is a good sign that cross-sell and email are working. At that point, invest in creating additional bundle variants.

| Month | Bundle Revenue | Total Revenue | Bundle Share % | Status |
|-------|---------------|---------------|---------------|--------|
| May 2026 | | | | |
| Jun 2026 | | | | |
| Jul 2026 | | | | |

---

## Monthly Scorecard (Append Each Month)

Copy this row and fill in after each monthly review. This is the master log.

| Month | Views | Orders | Conv % | AOV | Gross Rev | Net Rev | Repeat % | Email Subs | Email Open % | Pinterest Clicks | Reviews (Cumul) | Bundle % | Top-3 Conc % | Listing Health Score |
|-------|-------|--------|--------|-----|-----------|---------|---------|------------|-------------|-----------------|----------------|---------|-------------|---------------------|
| May 2026 | | | | | | | | | | | | | | |
| Jun 2026 | | | | | | | | | | | | | | |
| Jul 2026 | | | | | | | | | | | | | | |
| Aug 2026 | | | | | | | | | | | | | | |
| Sep 2026 | | | | | | | | | | | | | | |
| Oct 2026 | | | | | | | | | | | | | | |
| Nov 2026 | | | | | | | | | | | | | | |
| Dec 2026 | | | | | | | | | | | | | | |
| Jan 2027 | | | | | | | | | | | | | | |
| Feb 2027 | | | | | | | | | | | | | | |
| Mar 2027 | | | | | | | | | | | | | | |
| Apr 2027 | | | | | | | | | | | | | | |

---

## Alert Summary Reference

**Red Alerts (act same week):**

| Alert | Threshold | Action |
|-------|-----------|--------|
| Conversion rate | <0.5% blended | Audit top-5 highest-view listings: cover image, title keywords, price |
| Zero reviews at 20+ sales | 0 reviews | Verify Automation 2 running; manually message recent buyers |
| Email open rate | <30% Email 1 | Subject line A/B test + spam deliverability check |
| Net revenue per order | <$10 for 2 months | Check refunds; add bundle upsells to low-AOV listings |

**Yellow Alerts (act within current month):**

| Alert | Threshold | Action |
|-------|-----------|--------|
| AOV | <$12 for 2 months | Add bundle mention to top 5 individual listing descriptions |
| Pinterest outbound clicks | <10 by Month 2 | Create 3 additional pin variants; verify pins link to listings (not shop home) |
| Repeat buyer rate | <8% by Month 3 | Diagnose Kit Automation 2; verify post-purchase sequence is firing for all buyers |
| Bundle revenue share | <10% by Month 3 | Add bundle recommendations to top-3 individual listings; upgrade Day 7 email |
| Top-3 concentration | >70% | Invest mockup work in listings ranked 4–10 by views |

**Green Signals (accelerate):**

| Signal | Threshold | Action |
|--------|-----------|--------|
| Any listing conversion rate | >3% for 30 days | Add to Etsy Ads at $1/day; test paid amplification |
| Pinterest outbound clicks | >100/month | Create 3 additional pin variants for the top-traffic product |
| Repeat buyer rate | >25% by Month 3 | Segment VIP cohort; create early-access email for Phase 3 products |
| Email signup rate | >35% | Scale lead magnet promotion; test a second lead magnet |

---

## Seasonal Alert Calendar

Use this to avoid misreading normal seasonal patterns as KPI failures.

| Month | Expected Pattern | Do Not Treat as Alert |
|-------|-----------------|----------------------|
| May–Jun | Low absolute revenue; algorithm establishing rankings | Low gross revenue in M1–M2 is expected |
| July–Sep | Traffic and revenue spike from preservation searches | High view counts are expected; watch conversion rate, not just volume |
| Oct–Dec | Bundle sales increase; holiday gift cohort active | High bundle share in Q4 is correct, not a problem |
| Jan–Apr | Spring planning peak; Zone Calendar and Seed Starting Kit leading | Low preservation product sales in this window are expected |

---

*Document complete. Cross-references: `docs/phase-1-revenue-roadmap.md`, `phase-1-to-phase-2-decision-matrix.md`, `data/90-day-forecast.csv`, `analytics/monthly-metrics-checklist.md`, `marketing/growth-metrics-framework.md`, `marketing/email-automation-blueprint.md`.*
