---
title: "Seedwarden Monthly Metrics Checklist"
date: 2026-04-27
status: ready-to-use
cadence: first-Monday-of-month
estimated-time: 90 minutes
tags: [seedwarden, analytics, monthly-review, operator-runbook]
---

# Seedwarden Monthly Metrics Checklist

**When to run**: First Monday of each month, using prior month's data.  
**Estimated time**: 90 minutes total.  
**Tools required**: Etsy Seller Dashboard, Kit (ConvertKit) dashboard, a spreadsheet or the Jupyter notebook at `analytics/dashboard-template.ipynb`.  
**Output**: Updated metrics log (append to this document's Monthly Data Log section), plus any action items for the coming month.

---

## Pre-Work: Export Data (15 minutes)

Before starting the analysis, pull three exports. Do this at the start of the session — exports can take a few minutes to generate.

**Etsy exports:**

- [ ] Shop Manager > Finances > Payment Account > Download Statement — select prior calendar month, download CSV. Save as `analytics/data/etsy_orders_YYYY-MM.csv`.
- [ ] Shop Manager > Stats > select prior month > export (or manually record from the Stats dashboard). Capture: total views per listing, total favorites per listing, traffic sources breakdown (search organic vs. Etsy ads vs. social). Save as `analytics/data/etsy_listing_stats_YYYY-MM.csv`.
- [ ] Etsy Ads dashboard: record total ad spend, total ad-attributed revenue, and ROAS for the month. Note in the Monthly Data Log below.

**Kit exports:**

- [ ] Kit > Subscribers > Export > CSV. Save as `analytics/data/kit_subscribers_YYYY-MM.csv`. This file captures: email, subscribed date, tags, open count, total send count.
- [ ] Kit > Reports > select prior month. Manually record: Email 1 open rate (welcome sequence), newsletter average open rate, newsletter average CTR, welcome sequence Email 5 coupon redemption count (cross-reference with Etsy coupon usage report).

---

## Section 1: Revenue Analysis (15 minutes)

### 1.1 Monthly Revenue Summary

Record in the Monthly Data Log:

- [ ] Gross revenue (month)
- [ ] Net revenue (after Etsy fees: gross x 0.905 minus $0.25 per order)
- [ ] Number of orders
- [ ] Number of unique buyers
- [ ] Average order value (gross revenue / orders)
- [ ] Bundle revenue as % of total revenue (sum revenue from all 5 bundle listings / total revenue)

**Target benchmark (6-month mark):** $600–$1,200 gross/month.  
**Target benchmark (12-month mark):** $1,500–$3,000 gross/month.

Action if below target: Check which specific listings had zero orders this month. If a previously converting listing dropped to zero, check whether its ranking in Etsy search changed (use eRank or Marmalead for ranking data). If a listing consistently underperforms, flag it for listing update (cover image, title test, or tags revision).

### 1.2 Month-over-Month and Year-over-Year

- [ ] Calculate MoM revenue change (%). For months 1–12, MoM comparison is the primary trend signal.
- [ ] Starting Month 13 (May 2027), calculate year-over-year comparison for each month.
- [ ] Note whether the current month falls within a seasonal peak (Jan–Apr = spring; Jul–Sep = preservation; Nov–Dec = gift). Evaluate performance relative to seasonal expectation, not just prior month.

### 1.3 Revenue by Product

From the Etsy CSV export, aggregate revenue by listing name:

- [ ] Identify the top 3 revenue-generating listings this month. Compare to last month's top 3. Any new entrant to the top 3 should be featured in next month's newsletter and considered for Etsy ads if not already running.
- [ ] Calculate each listing's revenue share of total. Any listing below 1% revenue share with above 100 views this month is a conversion problem — flag for listing review.
- [ ] Record bundle revenue vs. individual product revenue breakdown.

---

## Section 2: Cohort and Repeat Purchase Analysis (20 minutes)

### 2.1 New vs. Returning Buyers

From the Etsy orders CSV, identify unique buyer emails:

- [ ] Count buyers who appear for the first time this month (new buyers).
- [ ] Count buyers who appeared in prior months and ordered again this month (returning buyers).
- [ ] Calculate repeat buyer rate: returning buyers / total unique buyers x 100. Target: 20%+ at 6-month mark, 25%+ at 12-month mark.

Note: Etsy does provide a "repeat customer" tag in some CSV formats. If unavailable, cross-reference buyer email against prior months' exports manually (feasible up to ~50 buyers/month; above that, use the SQL queries in `cohort-analysis-template.sql`).

### 2.2 Cohort Health Check

For any cohort that is now 90 days old (i.e., acquired 3 months ago):

- [ ] What is that cohort's 90-day second-purchase rate? Count buyers from that acquisition month who have placed a second order in the trailing 90 days.
- [ ] Record in Monthly Data Log under "Cohort 90-day rates."
- [ ] Compare to target: 20% within 90 days. If below 15%, the post-purchase email sequence needs diagnosis — check whether the Day 7 cross-sell email is actually being delivered (check Kit automation logs for the "purchased" tag trigger).

### 2.3 Seasonal Cohort Tracking

- [ ] If this is July, August, or September: what is the preservation season cohort size (buyers acquired this month) compared to the same month last year (if applicable)?
- [ ] If this is November or December: note what percentage of this month's bundles vs. individual products were sold. A bundle % above 50% confirms the holiday gift cohort dynamics described in growth-metrics-framework.md.
- [ ] If this is January, February, or March: note which planning products (Zone Calendar, Survival Garden Plans, 12-Month Planner) are driving new buyer acquisition. These are the spring planning cohort entry points.

---

## Section 3: Email List Health (20 minutes)

### 3.1 List Size and Growth Rate

From Kit dashboard or subscriber export:

- [ ] Total active subscribers (end of month)
- [ ] New subscribers this month (from Kit's subscriber report or count of subscribed_at in CSV within the reporting month)
- [ ] Unsubscribes this month (from Kit's unsubscribe report)
- [ ] Net subscriber growth: new minus unsubscribes
- [ ] MoM growth rate %: net growth / prior month end total

**Target benchmark (6-month mark):** 400–600 subscribers.  
**Target benchmark (12-month mark):** 1,200–2,000 subscribers.

Action if growth is stagnant (net growth below 30/month at the 6-month mark): Audit lead magnet promotion. Is the lead magnet link currently in TikTok/Instagram bio? Is there a dedicated Pinterest pin for the lead magnet page? Has the lead magnet been promoted in the newsletter within the past 8 weeks?

### 3.2 Engagement Metrics

From Kit's Reports section:

- [ ] Welcome sequence Email 1 open rate (for subscribers acquired this month)
- [ ] Welcome sequence Email 5 coupon redemption count (cross-reference against Etsy coupon report)
- [ ] Weekly newsletter average open rate for the month
- [ ] Weekly newsletter average click-through rate (CTR)
- [ ] Monthly unsubscribe rate: total unsubscribes / total active list start-of-month x 100

**Healthy benchmarks:**

| Metric | Healthy | Action if below |
|---|---|---|
| Email 1 open rate | 45%+ | Check spam; test subject line variant |
| Email 5 coupon redemption | 8%+ | Revise product recommendation in Email 4 |
| Newsletter open rate | 28%+ | Test subject line formula; reduce send frequency |
| Newsletter CTR | 3%+ | Align product spotlight to current season |
| Monthly unsubscribe rate | Below 0.5% | Review promotional send frequency; audit content relevance |

### 3.3 Subscriber Health Distribution

From the Kit CSV export, run the open rate health tier classification (cold / marginal / engaged per the SQL in `cohort-analysis-template.sql`, or manually filter the CSV):

- [ ] Count subscribers in each health tier (open_rate below 15% = cold; 15–30% = marginal; 30%+ = engaged)
- [ ] If cold subscribers exceed 25% of list: trigger or verify that Automation 4 (win-back) is running and correctly targeting the cold segment
- [ ] If engaged subscribers are below 40% of list: reduce send frequency on broadcast campaigns until engagement improves

### 3.4 Behavioral Tag Segment Counts

From Kit subscriber tags:

- [ ] Count: seed-saver tagged subscribers
- [ ] Count: city-grower tagged subscribers
- [ ] Count: preservationist tagged subscribers
- [ ] Count: purchased tagged subscribers (anyone who has made an Etsy purchase and been tagged)
- [ ] Count: vip tagged subscribers (two or more purchases)

Record in Monthly Data Log. Segment mix should shift seasonally: city-grower and seed-saver tags should grow fastest in Jan–Apr; preservationist tags in Jul–Sep.

---

## Section 4: Advertising and Paid Channel Analysis (10 minutes)

### 4.1 Etsy Internal Ads

From Shop Manager > Marketing > Etsy Ads:

- [ ] Total ad spend (month)
- [ ] Total ad-attributed revenue (month)
- [ ] ROAS: revenue / spend
- [ ] CPC (average cost per click) — available in Etsy Ads dashboard
- [ ] Which 3 listings had the highest ad ROAS? These are scale candidates.
- [ ] Which listings had ROAS below 1.5 for two consecutive months? These are pause candidates.

**Action thresholds:**
- ROAS above 2.5 for 30+ days: increase daily budget by 25–50%
- ROAS between 1.5–2.5: maintain, no change
- ROAS below 1.5 after 45 days: pause the listing ad, fix listing quality (images, title), then restart
- ROAS below 1.0 after 21 days: pause immediately, listing has a conversion problem

### 4.2 Pinterest and Social Referral Traffic

From Etsy Stats > Traffic Sources:

- [ ] Pinterest referral clicks (month) — listed under "Other" or "Social" in Etsy Stats
- [ ] Social media referral total
- [ ] Direct traffic (bookmarks, direct URL) — indicates returning visitors

From Pinterest Business Analytics (if running Pinterest ads):

- [ ] Pinterest monthly views (end of month)
- [ ] Pinterest outbound clicks (to Etsy)
- [ ] Pinterest ad ROAS (if ads running)

---

## Section 5: Product Listing Health Audit (10 minutes)

This section is a quick pass, not a deep review. The goal is to catch any listing degradation early.

### 5.1 Conversion Rate Scan

For each listing, calculate: orders / views x 100 = conversion rate.

- [ ] Flag any listing with views above 100 and conversion rate below 1%. These need investigation.
- [ ] Confirm the top-3 converting listings (by conversion rate, not just revenue). These are the "proven listings" for ad targeting.
- [ ] If any listing hit zero orders this month despite 50+ views, check: Was it deactivated? Did Etsy change its ranking?

### 5.2 New Review Count

From Shop Manager > Reviews:

- [ ] Total reviews received this month
- [ ] Running total of all reviews (cumulative)
- [ ] Average star rating

**Target:** 20–40 total reviews by 6-month mark, 80–150 by 12-month mark.

If review count is below pace: verify that the post-purchase email sequence is running. The Day 21 review request email (Automation 2, Email 3) is the primary driver. If Zapier or manual tagging is not capturing all buyers, some buyers are not entering the post-purchase sequence and therefore never receive the review request.

---

## Section 6: Monthly Data Log

Append a new row to this table every month. Archive previous months here rather than deleting.

| Month | Gross Revenue | Net Revenue | Orders | Unique Buyers | AOV | Bundle % | Email Subs | Open Rate | Newsletter CTR | Repeat Buyer Rate | Email 5 Redemptions | Etsy Ad ROAS | Total Reviews |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| YYYY-MM | $000 | $000 | 0 | 0 | $0 | 0% | 0 | 0% | 0% | 0% | 0 | 0.0 | 0 |

---

## Section 7: Actions Arising

After completing Sections 1–6, record concrete actions for the coming month. Use this format:

**Priority 1 — Immediate (this week):**
- [action] — [specific trigger that flagged it]

**Priority 2 — This month:**
- [action] — [context]

**Priority 3 — Watch list (no action yet):**
- [observation to monitor]

### Example action log entry (May 2026 review):

**Priority 1:**
- Update Zone Calendar listing title to include "2026 Seed Starting Schedule" — spring planning search term, listing getting views but below 1% conversion.
- Verify Automation 2 (post-purchase) is firing — only 2 reviews received, 12 buyers this month, suggesting review request email not reaching all buyers.

**Priority 2:**
- Begin building Pinterest boards for preservation season (July content plan needs pins live by June 15).
- Draft July "Preservation Season Launch" broadcast email — send scheduled for July 6.

**Priority 3:**
- Watch: Companion Planting Chart views dropped 40% from last month. Could be seasonal (spring planning window narrowing) or could be a ranking change. Check again in June.

---

## Appendix: Seasonal Action Triggers

Use this reference to ensure the right actions are taken at the right time each year, regardless of which month's checklist you are completing.

| Month | Seasonal Action |
|---|---|
| January | Update Zone Calendar listing title to include current year. Update welcome sequence P.S. to mention spring planning products. Increase Etsy ad spend on planning products. |
| February | Feature Seed Starting Kit and Heirloom Guide in newsletter. Run spring planting broadcast campaign (first week of February). |
| March | Run Pinterest promoted pins on Container Blueprint and Companion Planting Chart. |
| April | Feature Hot Sauce Guide and Anti-Catalog. Begin mid-season troubleshooting content. |
| May | Review all Phase 1 data for first full month. Identify top-3 converting products for ad scaling. |
| June | Draft July preservation broadcast email. Begin Pinterest preservation board creation. |
| July | Send Preservation Season Launch broadcast campaign (first week). Feature Fermented Harvest and Harvest Preservation in all channels. |
| August | Peak preservation content. Feature Meat/Fish Preservation. Back-to-school educational positioning for Food Sovereignty Guide. |
| September | Feature Seed Saving Manual for end-of-season seed saving. Fall Seed Saving broadcast campaign (third week). |
| October | All bundle listings updated with gift-ready titles and descriptions by October 15. Pinterest gift guide board created. Begin hunting season content. |
| November | Black Friday sale configured in Etsy by November 20 (25% off, 4-day window). Send Black Friday announcement email Thanksgiving morning. |
| December | Send "Homesteading Gift Guide" newsletter December 3. December 22: last-minute gift email to full list. Increase Etsy ad budget 50% on all bundle listings. |

---

*Prepared: 2026-04-27. Cross-references: growth-metrics-framework.md, email-automation-blueprint.md, cohort-analysis-template.sql, dashboard-template.ipynb.*
