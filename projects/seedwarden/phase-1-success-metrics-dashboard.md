---
title: "Phase 1 Success Metrics Dashboard"
subtitle: "Daily and Weekly Tracking Framework for Launch Through Month 1 Decision Gate"
prepared: 2026-05-05
status: activate-at-launch
phase: Phase 1 launch (May 2026) through Month 1 conversion review
cross-references:
  - post-launch-analytics-framework.md (data source architecture)
  - endangered-species-market-analysis.md (baseline and benchmark source)
  - customer-cohort-analysis-framework.md (cohort definitions)
  - concurrent-track-execution-plan.md (Track A and Track B success metrics)
  - etsy-seo-market-research.md (Etsy algorithm and conversion context)
  - email-list-building-playbook.md (email benchmark source)
word_count: ~2300
---

# Phase 1 Success Metrics Dashboard

**Purpose**: This document is the single-source tracking reference for Phase 1 performance from Day 1 of Etsy launch through the Month 1 decision gate (~June 5, 2026, assuming a May 5 launch). It defines what to measure, how often, from which source, what success looks like, and which numbers trigger an immediate course correction.

This is a no-software dashboard. Every metric in this document can be tracked in a single Google Sheet or Excel workbook with no plugins, no API connections, and no paid tools. Formulas are specified where needed.

---

## Section 1: Tier 1 Metrics — Daily Tracking

Tier 1 metrics are checked every day during the first four weeks. Check takes approximately 8 minutes: 3 minutes for Etsy Stats, 2 minutes for Kit dashboard, 3 minutes to update the spreadsheet. Do not skip days during Week 1 — the first 7 days of Etsy listing data are the highest-signal window for detecting listing copy and SEO problems.

**Data sources for Tier 1 (manual reads, no API required)**:
- Etsy Stats: Shop Manager > Stats > This Week (set to "Daily" view)
- Kit dashboard: Broadcasts > Automations > Welcome Sequence
- These are the only two dashboard logins required for daily tracking.

---

### 1.1 Views Per Listing (Daily)

**Definition**: Number of times a listing page was opened by a unique visitor. Source: Etsy Stats dashboard, per-listing breakdown. Note that Etsy's API exposes only a cumulative view count per listing (a single integer, not a time series) — daily view tracking must be done from the Etsy Stats dashboard manually. Record the daily delta (today's cumulative minus yesterday's cumulative).

**Baseline context**: For a new Etsy digital product shop in a homesteading or survival niche with no external promotion, organic search typically delivers 3–10 views per listing per day in Weeks 1–2 (based on etsy-seo-market-research.md competitive analysis and the OntarioTactical analog at 143 sales after launch — that shop's trajectory implies 15–25 daily views at the run-rate point where 143 sales had accumulated). A listing with strong keyword matching and a well-optimized title can reach 20–50 views per day organically within 2 weeks. Pinterest traffic adds volume but takes 7–30 days to materialize.

**Success thresholds**:

| Timeframe | Threshold | Interpretation |
|---|---|---|
| Day 1–3 | ≥5 views/listing/day (average across all 6) | Etsy has indexed the listing; search visibility confirmed |
| Week 1 total | ≥50 views per listing (cumulative, any single listing) | Minimum viable search exposure; weak but expected for a new shop |
| Week 2 | ≥100 views/week across all listings combined | Normal new-shop organic trajectory |
| Month 1 | ≥200 views on at least 1 listing | Indicates at least one listing is resonating with Etsy's algorithm |

**Failure trigger — act immediately**:
- Fewer than 20 cumulative views per listing after 7 days: this is a listing copy or SEO problem, not a traffic or marketing problem. Check that all 13 tags are entered correctly, title first 40 characters contain the primary search term, and the listing category is correctly set. Compare your title against top-performing listings in the same category using Etsy search directly.
- Zero views on any listing after 48 hours: indicates a potential indexing failure. Renew the listing manually (Shop Manager > Listings > Renew) and wait 24 hours. If still zero after renewal, check that the listing is published (not draft) and that the shop is set to Active.

**7-Day Rolling Average Formula** (for the spreadsheet):
```
=AVERAGE(D2:D8)    [where column D is daily views for that listing]
```
Track the 7-day rolling average alongside the raw daily number. A rising rolling average in Week 2 versus Week 1 is a strong positive signal even if individual day counts fluctuate.

---

### 1.2 Email Signups (Daily Cumulative)

**Definition**: New Kit subscribers per day. Source: Kit dashboard > Subscribers > Added Today. Also visible in Kit's "Growth" graph.

**Baseline context**: Email opt-in rates for a cold landing page (no existing social following) typically run 0.5–2% of visitors. The Zone Quick-Start Card lead magnet is projected at 25–35% conversion on a warm audience (Etsy buyers clicking a link in a listing) but much lower for cold social traffic. The email-list-building-playbook.md projects 100–150 subscribers by end of Month 1 assuming steady Etsy traffic and one social platform active.

**Success thresholds**:

| Timeframe | Threshold | Interpretation |
|---|---|---|
| Week 1 | ≥10 email signups | Opt-in mechanism is functioning; at least one traffic source is sending clicks |
| Week 2 | ≥30 email signups cumulative | Organic Etsy traffic is converting to email at a healthy rate |
| Week 2 hard target | ≥100 email signups cumulative | Aspirational target — achievable only with active social or Reddit promotion |
| Month 1 | ≥50 email signups total (minimum) | Below this indicates either no mention of lead magnet in listings, or Kit landing page is broken |

**Failure trigger**:
- Fewer than 5 signups after 14 days: the email capture mechanism is broken or invisible. Verify that the Kit landing page URL is correct in all Etsy listing descriptions. Test the form yourself using a secondary email. If the page is live and working, the problem is visibility — add the landing page URL as the first link in every listing description.

---

### 1.3 Landing Page Conversion Rate (Daily)

**Definition**: Email signups / Kit landing page unique visitors, expressed as a percentage. Source: Kit dashboard (subscriber count) combined with GA4 (sessions to the Kit landing page URL). Note that if all traffic reaches Kit via direct URL share (not via a tracked link), GA4 will show "direct" traffic and you will need to estimate visits from Kit's built-in form analytics.

**Calculation**: If Kit shows 30 signups and your estimate of landing page visitors is 150, conversion rate = 30/150 = 20%.

**Baseline benchmarks** (from email-list-building-playbook.md and industry data):
- Generic email capture landing pages: 5–12% conversion
- Niche-specific lead magnet pages with personalization (zone-specific card): 25–35%
- No personalization, generic offer: 8–15%

**Success threshold**:
- ≥15% conversion on Kit landing page (measured after 50+ visits): the Zone Quick-Start Card offer is resonating
- ≥25% conversion: strong performance; scale traffic to this page aggressively

**Failure trigger**:
- Below 5% conversion after 100 visits: rewrite the landing page headline and description. The offer is not communicating its specific value. Test alternative headlines (e.g., "Get your exact planting dates for [Zone] — free" vs. "Free Zone Quick-Start Card for Zone [X] growers").

---

### 1.4 Product-Specific Conversion Rate (Tracked Separately by Product)

**Definition**: Orders / Views for each individual listing. This is not directly visible in Etsy's dashboard as a rate — you must calculate it manually: (total orders for that listing) / (total views for that listing) expressed as a percentage.

**Why track separately**: The two product categories — zone cards (lower price point, $5–$8) and guides (higher price point, $10–$18) — are expected to convert at different rates. Zone cards and the companion planting chart should convert higher (lower price, faster decision) but produce lower revenue per conversion. Guides should convert lower but produce higher revenue per sale.

**Baseline benchmarks** (from Etsy SEO research and post-launch-analytics-framework.md):
- Industry average for Etsy digital product listings: 1–3% conversion
- Well-optimized listing with 20+ reviews: 3–5%
- New listing, no reviews: 0.5–1.5% expected

**Success thresholds by product tier**:

| Product | Price | Week 4 Conversion Target | Month 1 Target |
|---|---|---|---|
| Companion Planting Chart | $5 | ≥1.5% | ≥2.5% |
| Food Sovereignty Starter Guide | $8 | ≥1.0% | ≥1.8% |
| Anti-Catalog: 30 Heirlooms | $10 | ≥0.8% | ≥1.5% |
| Seed Saving Field Manual | $14 | ≥0.8% | ≥1.5% |
| Apartment Plant Catalog | $14 | ≥0.8% | ≥1.5% |
| Survival Garden Regional Plans | $18 | ≥0.5% | ≥1.0% |

**Failure trigger**:
- Any listing with over 100 views and zero sales: this listing has a specific conversion problem. Check that the mockup image is loading correctly, that the price is appropriate for the product, and that the description clearly states what the buyer receives. A listing with views but no sales is almost always a trust problem (mockup doesn't match buyer expectation) or a clarity problem (buyer doesn't know what they're getting).
- Overall shop conversion below 0.5% after Month 1: do not proceed with Track B paid promotion. Fix the conversion mechanism first. The Phase 2 Gate A advertising threshold is 2.5% conversion on qualifying listings — spending on ads at 0.5% conversion is not recoverable.

---

### 1.5 Customer Acquisition Cost (CAC)

**Definition**: Total money spent to acquire one paying customer. At Phase 1 launch, the primary costs are the Etsy listing fee ($0.20/listing) and any Etsy Ads spend (not recommended until Gate A triggers). Time cost is tracked separately as human hours, not dollar cost, for solo operators.

**Phase 1 calculation** (organic-only):
- Total spend in Month 1: 6 listings × $0.20 = $1.20 Etsy listing fees + any ad spend (should be $0 in Phase 1)
- CAC (organic) = $1.20 / total Month 1 orders
- At 20 orders: CAC = $0.06. At 5 orders: CAC = $0.24. Both are exceptional for digital products.

**Track B parallel spend** (if Canva Pro is purchased for pin production): $15/month. If Track B drives 10 email signups that convert to 2 sales, Track B CAC = $15/2 = $7.50. This is still well below the threshold for profitability at $8–$18 average order value.

**Failure trigger**: There is no CAC failure trigger in organic Phase 1 because fixed costs are near zero. CAC becomes a critical metric when paid advertising begins (Gate A or Gate D). Log it now to establish the baseline.

---

## Section 2: Tier 2 Metrics — Weekly Tracking

Tier 2 metrics are checked once per week, on Monday morning, covering the prior week's data. The weekly check takes approximately 20–30 minutes including the Etsy Stats manual read and Kit export.

---

### 2.1 Customer Lifetime Value (LTV) by Cohort

**Definition**: Average total revenue attributed to a single customer from first purchase to date. At Month 1, this is effectively average order value for a new customer with no repeat purchase history. LTV becomes meaningful when the 90-day window has passed (August 2026 for May buyers).

**Week-by-week LTV tracking formula**:
```
LTV_current = (Total revenue / Total unique buyers)
LTV_at_90_days = (Revenue from repeat purchases by Month-1 cohort) / (Month-1 unique buyer count)
```

**Baseline targets** (from endangered-species-market-analysis.md cohort LTV estimates):
- High-Intent Forager cohort: projected $65–$130/year LTV
- Survival Prepper cohort: projected $50–$90/year LTV
- Homesteader cohort: projected $40–$80/year LTV
- Gift Buyer cohort: projected $25–$45/year (single purchase, low repeat)

Track which product each buyer purchased first. At Month 3, you will have enough data to see whether first-product affects LTV — that data informs both catalog prioritization and email sequence targeting.

---

### 2.2 Repeat Purchase Rate

**Definition**: Percentage of buyers who make a second purchase within any tracked window. Track at 30-day, 60-day, and 90-day intervals starting from the first purchase date.

**Month 1 target**: Not measurable in Month 1 (too early for repeat purchases). Begin tracking at the end of Month 2 using the customer-retention-tracker.csv structure.

**Month 3 target** (from post-launch-analytics-framework.md): 12% minimum, 18–25% target for 90-day second-purchase rate.

**Week 4 early signal**: If any buyer places a second order within the first 30 days, flag them immediately. This is an exceptionally high-signal data point — they are a confirmed high-LTV customer. Tag them in Kit as `repeat_buyer_early` and add to the priority email segment for new guide launches.

---

### 2.3 Cohort Retention

**Definition**: What percentage of buyers from Week 1 are still purchasing by Week 4, Month 2, and Month 3. This is the cohort-based view of repeat purchase rate — tracking a specific group of buyers (the "May 2026 cohort") over time rather than tracking all buyers at one snapshot.

**Setup**: When the first orders come in, record each buyer's Etsy user ID and first purchase date in customer-analytics.csv. Assign an inferred cohort (per post-launch-analytics-framework.md Section 3). At Month 2, check how many of the May cohort have made a second purchase.

**Target for May 2026 cohort at 90 days (August)**: ≥12% second-purchase rate (minimum), ≥20% (target).

---

### 2.4 Product Affinity Analysis

**Definition**: Which products are purchased together in the same order, or sequentially across orders. Source: Etsy API transaction data (listing_id per receipt). This becomes meaningful when you have 40+ orders.

**Week 4 minimum threshold**: If fewer than 40 orders have arrived, skip this metric — sample size is too small. If 40+ orders exist, run a simple frequency count: for every order containing more than one listing, note the pair. The top-3 pairs are your first bundle candidates.

**Practical shortcut for Month 1**: Instead of SQL queries, maintain a manual tally column in customer-analytics.csv: "Second listing purchased (if any)." Sort by this column monthly and the affinity pattern will be visible.

---

### 2.5 Segment Concentration

**Definition**: What percentage of revenue comes from a single product or cohort. High concentration (one product driving over 60% of revenue) is a risk signal — if that listing's ranking drops, revenue drops with it.

**Month 1 target**: No single listing should drive more than 50% of total revenue. If one listing is dominating, accelerate uploads of Phase 2 products to distribute the revenue base.

**Cohort concentration**: If more than 70% of buyers come from a single cohort (e.g., all buyers are Survival Preppers), the marketing reach is too narrow. Diversify content to reach secondary cohorts.

---

## Section 3: Success Thresholds Summary

| Metric | Minimum Acceptable | Target | Time Frame |
|---|---|---|---|
| Views per listing (cumulative) | 20 views | 50 views | End of Week 1 |
| Email signups (cumulative) | 10 signups | 50 signups | End of Week 1 |
| Email signups (cumulative) | 30 signups | 100 signups | End of Week 2 |
| Overall shop conversion rate | 0.5% | 2–3% | End of Month 1 |
| Any paying orders | 1 order | 5 orders | End of Week 2 |
| Total Month 1 orders | 10 orders | 20–40 orders | End of Month 1 |
| Email open rate (welcome sequence) | 30% | 45%+ | First email batch |
| Kit landing page conversion | 8% | 25–35% | After 50 visits |
| 90-day repeat purchase rate | 12% | 18–25% | August 2026 |

---

## Section 4: Failure Triggers and Immediate Response Protocol

The following trigger conditions require same-day action — do not wait for the next scheduled review.

**Trigger 1: Views below 20 per listing at Day 7**
- Root cause hypothesis: listing copy or SEO problem, not traffic
- Immediate action: Re-examine every tag for the affected listing against Etsy's 20-character limit. Open Etsy search for your primary keyword and compare your title format to the top 3 results. Renew the listing to force re-indexing.
- Do not increase ad spend. Views below threshold means the listing is not being served to the right searches — ads will waste budget on an unoptimized listing.

**Trigger 2: Email opt-in below 1% on Kit landing page (after 100+ visits)**
- Root cause hypothesis: landing page copy is not communicating the specific value of the lead magnet
- Immediate action: Rewrite the headline to be hyper-specific (e.g., "Know your exact last frost date for Zone 6a? Get your Zone 6a Quick-Start Card — free"). Reduce the number of fields to first name + email only (remove zone dropdown temporarily). Test the simpler form for one week before testing other changes.

**Trigger 3: Zero orders after 14 days with 100+ total views**
- Root cause hypothesis: views are arriving but listings are not converting — trust, price, or clarity problem
- Immediate action: Check that all mockup images are loading at full quality (reupload if compressed). Verify that the price is competitive (compare against the top 10 Etsy results for your primary keyword). Add social proof language to listing descriptions if reviews do not yet exist ("crafted for growers in Zones 4–9").

**Trigger 4: Kit welcome sequence open rate below 25% on first email**
- Root cause hypothesis: email is landing in spam, or subject line is not compelling
- Immediate action: Check Kit's spam score for the welcome email. Test the subject line: "Your Zone Quick-Start Card is here" is expected to perform at 35–45% open rate for a confirmed opt-in. If below 25%, check sender authentication (SPF/DKIM) in Kit settings.

**Trigger 5: Any listing disappears from Etsy search (zero views for 5+ consecutive days after initial indexing)**
- Root cause hypothesis: Etsy algorithm downrank due to a compliance issue or tag problem
- Immediate action: Review listing for any tags that might trigger Etsy's policy filters. Renew the listing. If disappearance persists after renewal, check Etsy's seller policy email inbox for any listing-specific notices.

---

## Section 5: Dashboard Template — Google Sheets Format

Create one sheet with three tabs: Daily, Weekly, and Monthly.

### Daily Tab — Columns (one row per day)

| Column | Data to Enter | Formula Notes |
|---|---|---|
| A: Date | Today's date | Manual |
| B: Listing 1 Views (Cumulative) | From Etsy Stats | Manual |
| C: Listing 1 Views (Daily Delta) | Today minus yesterday | =B3-B2 |
| D–M: Repeat for Listings 2–6 | Same pattern | |
| N: Total Daily Views (all listings) | Sum of daily deltas | =SUM(C3,E3,G3,I3,K3,M3) |
| O: 7-Day Rolling Avg Views | Rolling average | =AVERAGE(N3:N9) — copy down |
| P: Kit Subscribers (Cumulative) | From Kit dashboard | Manual |
| Q: New Signups Today | Today minus yesterday | =P3-P2 |
| R: Orders (Cumulative) | From Etsy Payment Account | Manual |
| S: New Orders Today | Today minus yesterday | =R3-R2 |
| T: Revenue (Cumulative $) | From Etsy Payment Account | Manual |
| U: Anomaly Flag | Auto-flag formula | =IF(OR(C3<2,Q3=0),"CHECK","OK") |

**Anomaly flag logic**: The flag in column U fires if daily views for Listing 1 drop below 2 OR no new signups occurred. Extend the formula to cover all listings and signups for a comprehensive daily check.

### Weekly Tab — Columns (one row per week)

| Column | Data to Enter | Notes |
|---|---|---|
| A: Week Number | Week 1, 2, 3, 4 | Manual |
| B: Total Views (All Listings) | Sum from Daily tab | =SUM(Daily!N:N) filtered by date |
| C: Conversion Rate % | Manual calc | Orders / Views × 100 |
| D: Email Signups (Cumulative) | From Kit | Manual |
| E: Open Rate (Welcome Email 1) | From Kit Broadcasts | Manual |
| F: Revenue (Gross $) | From Etsy | Manual |
| G: Revenue (Net, ~82%) | After Etsy fees | =F×0.82 |
| H: Avg Order Value | Revenue / Orders | =F/[order count] |
| I: Top-Converting Listing | Name of listing | Manual — highest conversion rate this week |
| J: Weakest Listing | Name of listing | Manual — lowest views this week |
| K: Decision Checkpoint | Proceed / Optimize / Stop | See Section 6 |

### Monthly Tab — Decision Summary (Month 1 only)

One row. Columns:
- Total orders, total revenue, net revenue, overall conversion rate, email list size, top traffic source, cohort distribution (% of orders per cohort), repeat purchase count (0 expected in Month 1), go/no-go for Track B Phase 2 acceleration.

---

## Section 6: Decision Checkpoints

### Week 2 Checkpoint (Day 14)

**Check all three questions**:
1. Has at least one listing received 50+ views? If yes: listing SEO is working. If no: tag and title audit required before proceeding.
2. Are there at least 10 email signups? If yes: email capture is functioning. If no: verify Kit landing page is linked from listings.
3. Has at least 1 sale occurred? If yes: proceed normally. If no: initiate listing conversion audit (mockup quality, price comparison, description clarity).

**Decision outputs**:
- All three YES: proceed with Phase 1 as planned. Begin Track B parallel execution on schedule.
- Any NO: pause Track B expansion. Focus all available time on the failing metric before splitting resources.

### Month 1 Decision Gate (~June 5, 2026)

**Metric thresholds for Phase 2 progression** (from post-launch-analytics-framework.md Gate B/C):
- Orders ≥ 20: Phase 1 baseline validated. Continue uploading Phase 2 backlog products.
- Conversion rate ≥ 2%: listing quality is strong. Proceed to evaluate Etsy Ads (Gate A).
- Email list ≥ 50 subscribers: email infrastructure validated. Begin Phase 2 email sequences.
- Any single listing conversion rate ≥ 2.5%: this listing is the anchor. Prioritize photography investment and bundle inclusion for this product.

**If conversion rate is below 1% at Month 1**: Do not proceed to paid promotion. Do not expand Track B. Run a focused listing optimization sprint (rewrite top-1 listing title and description, test a new mockup image, add a second mockup variant showing interior pages). Reassess at Week 6.

---

## Section 7: Baseline Calculations

**Etsy benchmark basis**: The OntarioTactical analog (143 sales, 29 reviews, 5.0 stars, estimated 6–12 month accumulation in a comparable digital niche) implies approximately 12–24 sales per month at a stable run rate for a well-tagged Etsy digital shop. Seedwarden's Month 1 minimum target of 20 orders matches the lower end of this benchmark adjusted for a zero-review starting point.

**Email benchmark basis**: The email-list-building-playbook.md projects 100–150 subscribers in Month 1 for a Zone Quick-Start Card lead magnet with active social traffic. Without active social, organic Etsy click-through to the Kit page will yield fewer subscribers — the 50-subscriber minimum is set at the organic-only floor.

**Conversion rate benchmark basis**: The post-launch-analytics-framework.md Month 1 target of 2.0–2.5% conversion is sourced from Etsy's own published statistics on digital product listings and the comparable competitor data in etsy-seo-market-research.md. The minimum of 1.5% represents survival-level performance for a new-shop listing without reviews. Performance below 1% after 200 views indicates a listing-quality problem that must be resolved before any traffic investment.

**CAC benchmark basis**: At $0 ad spend, CAC is negligible for organic digital product sales. The relevant threshold enters when Etsy Ads begin (Gate A: $5/day = $150/month). At a 2.5% conversion rate and $28 AOV, CPA via Etsy Ads should not exceed $20 per order. If CPA exceeds AOV, pause ads and audit listing conversion before increasing budget.

---

*Cross-references: `post-launch-analytics-framework.md` (full data architecture), `customer-cohort-analysis-framework.md` (cohort assignment logic), `etsy-ga4-event-tracking.md` (GA4 event schema), `concurrent-track-execution-plan.md` (Track A and Track B success metrics), `email-list-building-playbook.md` (email benchmark source).*
