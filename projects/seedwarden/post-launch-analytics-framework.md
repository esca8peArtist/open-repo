---
title: "Post-Launch Analytics Framework — Phase 1 Tracking Architecture"
created: 2026-05-05
last_updated: 2026-05-05
session: 733 (extended: Item 50)
status: activate-at-launch
cross-references:
  - customer-cohort-analysis-framework.md
  - google-analytics-integration-guide.md
  - etsy-ga4-event-tracking.md
  - analytics/monthly-metrics-checklist.md
  - analytics/cohort-analysis-template.sql
  - customer-retention-tracker.csv
---

# Post-Launch Analytics Framework

**Purpose**: Define the full data architecture that activates when Phase 1 goes live. This document covers what data flows where, what the Etsy API can and cannot provide, how GA4 complements the gaps, how customers get assigned to cohorts, what success looks like by month, and which metric thresholds trigger Phase 2 decisions.

**Scope**: Day 0 through Month 6. Phase 2 metrics scaling is covered in the Phase 2 decision gates section below.

---

## 1. Data Source Reality: What Etsy Actually Exposes

Before designing pipelines, operators need an accurate picture of what Etsy's API and dashboard actually provide. The gap between what sellers assume is available and what is actually accessible via the API is significant.

### 1.1 Etsy Open API v3 — Available Data

The Etsy Open API v3 (current as of October 2024 general release) provides programmatic access to the following data categories that are useful for Seedwarden analytics:

**Order / Receipt data** (endpoint: `GET /v3/application/shops/{shop_id}/receipts`)

Requires OAuth2 with `transactions_r` scope. Fields returned per receipt:
- `receipt_id` — unique order identifier
- `buyer_user_id` — Etsy user ID (not email; see note below)
- `buyer_email` — requires separate commercial access approval from Etsy; not available by default
- `created_timestamp` — order creation time (UTC unix timestamp)
- `grandtotal` / `subtotal` / `total_price` — order financials
- `country_iso` — buyer country (2-letter ISO code)
- `state` — buyer state (US orders)
- `is_paid` — boolean
- `coupon_code` — applied coupon if any
- `message_from_buyer` — optional gift message field, useful for identifying gift buyer cohort

**Transaction data** (endpoint: `GET /v3/application/shops/{shop_id}/transactions`)

One transaction per listing per order. Fields:
- `transaction_id`
- `listing_id` — maps to your product
- `title` — listing title at time of purchase
- `quantity`
- `price` — per-unit price object (amount + divisor + currency)
- `create_timestamp`

**Listing data** (endpoint: `GET /v3/application/listings/{listing_id}`)

- `listing_id`, `title`, `description`, `price`
- `views` — cumulative lifetime view count. This is a single integer, not a time-series. No daily or weekly breakdown is available via API.
- `num_favorers` — cumulative favorites count

**Rate limits**: 10,000 requests per 24-hour period; 10 requests per second. A daily pull of all receipts + transactions for a shop with under 500 orders/month requires fewer than 100 requests and is well within limits.

### 1.2 What the Etsy API Cannot Provide

These gaps are confirmed as of the Etsy Open API v3 documentation and community discussions (etsy/open-api GitHub issues #1304, #1386, last updated November 2024):

| Data Point | Status | Workaround |
|---|---|---|
| Daily views per listing | Not available via API | Pull from Etsy Stats dashboard manually; export CSV monthly |
| Favorite activity by time period | Not available via API | Manual dashboard read; note cumulative `num_favorers` delta month-over-month |
| Etsy search keywords that led to listing | Not available | Etsy Stats dashboard only (no API export); record manually monthly |
| Traffic source breakdown (Etsy search vs. social vs. direct) | Not available via API | Etsy Stats dashboard only |
| Cart abandonment data | Not available | No abandonment tracking available anywhere |
| Customer geographic data below state level | Not available | State + country is the finest granularity |

**Key implication**: The analytics stack must treat the Etsy API as a reliable order feed (transactional data only) and treat the Etsy Stats dashboard as a manual monthly read for traffic and listing performance data. Attempting to build automated stats pulls will fail.

### 1.3 GA4 + Etsy: What Can Actually Be Tracked

Etsy supports GA4 tracking natively for Etsy shop pages. The integration is configured via Shop Manager > Settings > Options > Web Analytics by entering your GA4 Measurement ID (`G-XXXXXXXXXX`). However, the integration has documented limitations:

**What fires reliably on Etsy via GA4**:
- Page views on individual listing pages (Etsy runs the GA4 tag when a listing is opened)
- Session and traffic source data (organic search, social referrals, direct)
- User country / city / device (collected via GA4's automatic parameters)

**What does not fire reliably on Etsy via GA4**:
- Purchase events — Etsy does not fire the GA4 `purchase` event on its checkout pages. Transaction data cannot be collected through the GA4 integration on Etsy itself.
- Add-to-cart events — not exposed
- Checkout funnel steps — not exposed

**Practical consequence for Seedwarden**: GA4 on Etsy is a traffic measurement tool, not a transaction measurement tool. Use GA4 to understand what channels drive traffic to listings and what listing pages attract the most views. Use the Etsy API and Etsy Dashboard as the source of truth for all purchase data.

**Where GA4 provides full ecommerce tracking**: Any page you control outside of Etsy (a landing page, a lead magnet page, an email opt-in page, or if you ever migrate to a standalone storefront). Kit (ConvertKit) email click events can also feed GA4 via UTM parameters on outbound links.

---

## 2. Data Architecture: How the Pieces Connect

```
TRAFFIC SOURCES                DATA CAPTURE LAYER              ANALYSIS LAYER
Pinterest → UTM link ──────→ GA4 (traffic only)  ──────────→ GA4 Explore reports
Email → UTM link     ──────→ GA4 (traffic only)              (sessions, sources, devices)
Etsy organic search  ──────→ GA4 (sessions on               ┌─ customer-analytics.csv
Reddit / organic     ──────→  listing pages)                 │  (individual order log)
Direct              ──────→                                  │
                                                             │
Etsy order placed   ──────→ Etsy API v3 (daily pull) ──────→ analytics/data/etsy_orders_YYYY-MM.csv
                             receipts + transactions          │  (cohort-analysis-template.sql)
                                                             │
Etsy Stats dashboard ──────→ Manual monthly export ─────────→ analytics/data/etsy_listing_stats_YYYY-MM.csv
(views, favorites,                                           │
 search keywords)                                           │
                                                             │
Kit subscriber tags  ──────→ Kit CSV export (monthly) ──────→ analytics/data/kit_subscribers_YYYY-MM.csv
                             open/click data                 │
                                                             ▼
                                                     customer-retention-tracker.csv
                                                     (monthly cohort rollup)
                                                             │
                                                             ▼
                                                     analytics/dashboard-template.ipynb
                                                     (monthly review visualization)
```

### Daily Automated Pull (Etsy API)

Run once per day, within the 10,000/day rate limit:

1. `GET /v3/application/shops/{shop_id}/receipts?min_created=yesterday_unix` — new orders in the last 24 hours
2. For each new receipt, `GET /v3/application/shops/{shop_id}/transactions?receipt_id={id}` — items in the order
3. Write results to `analytics/data/etsy_orders_YYYY-MM.csv` (append mode)

This pull requires an OAuth token for the Seedwarden Etsy account. Set it up once via the Etsy Developer Portal, store the access token securely, and use a cron job or a free-tier automation service (Zapier, Make) to run the pull daily.

### Monthly Manual Reads (First Monday of Each Month)

Per the protocol in `analytics/monthly-metrics-checklist.md`:
1. Etsy Stats dashboard: record views, favorites, traffic source breakdown, top search keywords. Log into `analytics/data/etsy_listing_stats_YYYY-MM.csv`.
2. Kit subscriber export: download CSV, save to `analytics/data/kit_subscribers_YYYY-MM.csv`.

---

## 3. Customer Cohort Definitions

Four cohorts are defined in `customer-cohort-analysis-framework.md`. This section specifies the precise signal logic used to assign each new customer to a cohort from API-available data alone (no survey required for initial classification).

### Signal Logic (API-derivable, applied to each order)

| Cohort | Primary Signal | Secondary Signal | Confidence |
|---|---|---|---|
| High-Intent Forager | 2+ individual guide listings in one order | Repeat purchase within 90 days | High if both; Medium if primary only |
| Survival Prepper | Bundle listing purchased OR 5+ individual guides in one order | `message_from_buyer` absent (transactional, not gift) | High if bundle; Medium if volume |
| Homesteader | Medicinal guide purchased alongside edibles or native plants guide | Geographic state in VT, TN, OR, WA, ID, MT, NC, KY | Medium (confirm via survey) |
| Gift Buyer | Single guide purchased in May, Nov, or Dec | `message_from_buyer` non-empty (gift message present) | High if message present; Medium if seasonal only |

### Cohort Assignment Protocol

1. Infer cohort from API signals at time of order (above logic)
2. Send post-purchase survey to all customers Day 5 after order creation (via Kit automation)
3. If survey response received: override inferred cohort with survey response if they conflict
4. Record final cohort in `customer-analytics.csv` and `customer-retention-tracker.csv`

A fifth cohort ("Educator / Institutional") is expected to emerge in Month 3–6 if library or school orders appear. Do not force-fit these into the four cohorts; flag them in the notes column for future analysis.

---

## 4. UTM Tracking Schema

All outbound links from Kit emails and social posts to Etsy listings must carry UTM parameters. This is the primary way GA4 can attribute traffic sources.

**Standard naming convention** (all lowercase, underscores not hyphens):

| Source | Medium | Campaign | Example |
|---|---|---|---|
| `kit` | `email` | `welcome_sequence_e1` through `e5` | Kit welcome emails |
| `kit` | `email` | `newsletter_YYYY_MM` | Monthly newsletter |
| `kit` | `email` | `broadcast_[topic]` | One-off broadcast |
| `pinterest` | `organic_pin` | `[guide_slug]_pin` | Pinterest pin links |
| `pinterest` | `paid_pin` | `[campaign_name]` | Pinterest ads (Phase 2) |
| `instagram` | `bio_link` | `bio_linktree` | Bio link |
| `instagram` | `story` | `[guide_slug]_story` | Story swipe-ups |
| `reddit` | `community_post` | `r_foraging_[month]` | Reddit posts |

Append to any Etsy listing URL:
```
https://www.etsy.com/listing/{listing_id}?utm_source=kit&utm_medium=email&utm_campaign=welcome_sequence_e3
```

GA4 will capture these parameters as traffic source dimensions. Even though the purchase event won't fire on Etsy, you can measure how many sessions from each UTM source occur before a purchase by cross-referencing GA4 session dates with Etsy order dates in the monthly analysis.

---

## 5. Success Metrics by Month

### Month 1 (May 2026 — Launch Baseline)

**Purpose**: Establish baseline. Do not optimize yet; collect clean data.

| Metric | Minimum | Target | Source |
|---|---|---|---|
| Orders | 20 | 40–60 | Etsy API |
| Unique buyers | 18 | 35–55 | Etsy API |
| Average order value | $22 | $28–35 | Etsy API |
| Conversion rate | 1.5% | 2.0–2.5% | Etsy Stats dashboard |
| Repeat buyer rate | n/a (too early) | — | — |
| Email subscribers acquired | 50 | 100–150 | Kit |
| Email 1 open rate | 35% | 45%+ | Kit |
| Top traffic source | Etsy organic | Etsy organic | GA4 |
| Survey responses received | 5 | 15+ | Typeform / Kit |

**Month 1 failure condition**: Fewer than 20 orders after 30 days of live listings means a listing quality problem, not an analytics problem. Check Etsy search ranking before any analytics action.

### Month 3 (July 2026 — Viability Checkpoint)

**Purpose**: Confirm the business is viable and cohort structure is accurate. This is the first point at which Phase 2 decisions should be considered.

| Metric | Minimum | Target | Source |
|---|---|---|---|
| Cumulative orders | 80 | 150–250 | Etsy API |
| Repeat buyer rate | 12% | 18–25% | Etsy API + analytics/cohort-analysis-template.sql |
| Conversion rate | 1.8% | 2.5%+ | Etsy Stats |
| AOV | $28 | $32–40 | Etsy API |
| Email list size | 200 | 400–600 | Kit |
| Newsletter open rate | 28% | 35%+ | Kit |
| Cohort assignments complete | 60% of customers | 80%+ of customers | customer-analytics.csv |
| 90-day second-purchase rate | 12% | 20%+ | customer-retention-tracker.csv |

**Month 3 failure condition**: If repeat buyer rate is below 12% at 90 days, the post-purchase email sequence has a delivery or content problem. Check Kit automation logs before any product or pricing changes.

### Month 6 (October 2026 — Phase 2 Trigger Point)

**Purpose**: Decide whether to activate paid ads, launch new guides, or expand to endangered/medicinal species. Full criteria in Section 6 below.

| Metric | Minimum | Target | Source |
|---|---|---|---|
| Cumulative orders | 300 | 500–700 | Etsy API |
| Repeat buyer rate | 18% | 25%+ | Etsy API |
| AOV | $32 | $38–50 | Etsy API |
| Email list size | 600 | 1,000–1,500 | Kit |
| LTV by cohort calculated | All 4 cohorts | — | customer-retention-tracker.csv |
| Cross-guide substitution data available | 60+ repeat buyers | — | cohort-analysis-template.sql Section 5.2 |
| Top-3 converting listings identified | Confirmed | — | Etsy Stats + monthly-metrics-checklist.md |

---

## 6. Phase 2 Decision Gates

These are the specific metric thresholds that justify activating each Phase 2 initiative. Do not activate Phase 2 components prematurely; the gates protect against spending resources before organic proof exists.

### Gate A: Etsy Internal Ads Activation

**Question**: When does organic conversion justify paid ad spend?

**Trigger conditions** (all three must be met):
1. Conversion rate on at least 3 listings is 2.5%+ for two consecutive months
2. Those listings have received 200+ organic views each in the prior month (proves search discoverability)
3. AOV is $28+ (ensures first-order payback even at $0.40–$0.60 CPC)

**Why these thresholds**: Etsy ads amplify existing conversion; they do not fix a broken listing. A listing converting at 2.5%+ will likely maintain that rate at higher traffic volumes. At $28 AOV and Etsy's standard 6.5% transaction fee, net revenue per order is approximately $25.60. At $0.50 CPC and a 2.5% conversion rate, cost per acquisition is $20 — profitable on first order even before any repeat purchase.

**Starting budget**: $5/day per qualifying listing. Scale to $10/day if ROAS exceeds 2.5 after 30 days.

**Source queries**: `analytics/monthly-metrics-checklist.md` Section 4.1; `cohort-analysis-template.sql` Section 7.2.

### Gate B: New Guide Launch

**Question**: Which underserved cohorts have highest LTV potential?

**Trigger conditions** (any one):
1. A cohort's 90-day second-purchase rate exceeds 25% but you have fewer than 3 products targeting that cohort — demand exceeds supply
2. A cohort's LTV at 6 months is 40%+ higher than another cohort's, but the high-LTV cohort accounts for fewer than 15% of orders — underserved, high-value segment
3. A recurring theme appears 5+ times in `message_from_buyer` or survey free-text that maps to an unaddressed use case (e.g., "wild mushrooms" or "urban foraging" mentioned repeatedly but no dedicated guide exists)

**Production timeline from trigger to launch**: 8–10 weeks (guide writing, design, mockup, listing creation). Do not trigger Gate B unless the 8-week production timeline can begin within 2 weeks of the trigger date.

### Gate C: Endangered / At-Risk Species Expansion

**Question**: How much repeat purchase volume justifies the design investment?

**Trigger conditions** (all three must be met):
1. Total cumulative orders exceed 400 (proves the base audience exists)
2. Repeat buyer rate is 20%+ at Month 6 (proves buyers return — the core audience for premium specialty content)
3. "Appalachian Medicinals" or "at-risk plant" topics appear in 3+ survey free-text responses (proves active interest, not just a hypothesis)

**Investment required**: Estimated 6–8 weeks for photo sourcing + guide writing + legal review per the `endangered-species-candidate-list.md` roadmap. Minimum order volume of 400 ensures the launch list is large enough to reach 80+ buyers with the launch email, which is the break-even point for the design investment.

### Gate D: Paid External Ads (Pinterest Ads, Instagram Ads)

**Trigger conditions** (all three must be met):
1. Kit email list exceeds 800 subscribers (ensures retargeting audience is meaningful)
2. Pinterest organic pins are driving 50+ outbound clicks/month to Etsy (proves platform already has an audience before spending)
3. Etsy conversion rate is 2.5%+ (ensures the destination converts paid traffic)

**Starting test**: $150/month Pinterest ad budget targeting "wild edibles" and "foraging guide" keywords. Run for 60 days. Calculate ROAS using Etsy order volume during campaign weeks vs. pre-campaign baseline weeks. Gate D is only justified if Gate A (Etsy ads) is already active and profitable.

---

## 7. Implementation Timeline

### Day 0–3 (Launch Week)

- [ ] Etsy listings go live
- [ ] Enter GA4 Measurement ID in Etsy Shop Manager > Settings > Options > Web Analytics
- [ ] Confirm GA4 Realtime shows visitors when you open a listing page yourself
- [ ] Verify all Kit welcome sequence emails are armed and triggering (test with a dummy subscriber)
- [ ] Confirm Kit "purchased" tag automation is active (Zapier or manual tagging on Day 1 orders)

### Day 4–7 (First Week Monitoring)

- [ ] Run first Etsy API pull manually (or via automation): save to `analytics/data/etsy_orders_2026-05.csv`
- [ ] Add first orders to `customer-analytics.csv` with inferred cohort from API signals
- [ ] Check GA4 for traffic source breakdown: what channels are sending first visitors?
- [ ] Note any listings with 0 views after 7 days — these may have search indexing issues

### Week 2–4 (First Month)

- [ ] First post-purchase surveys return (Day 5 after launch, first batch of survey responses expected Day 12)
- [ ] Update `customer-analytics.csv` with survey cohort assignments
- [ ] At end of Month 1: run monthly-metrics-checklist.md for the first time
- [ ] Pull Etsy Stats dashboard manually; log into `analytics/data/etsy_listing_stats_2026-05.csv`
- [ ] Begin `customer-retention-tracker.csv` — add all Month 1 buyers as the first cohort

### Month 2–3 (First Cohort Aging)

- [ ] Run `cohort-analysis-template.sql` Section 2 (cohort retention table) for the first time using Month 1 buyer data
- [ ] First 90-day second-purchase window opens for May buyers in August — watch for Gate A/B signals
- [ ] Publish first seasonal campaign to High-Intent Forager segment (per `customer-cohort-analysis-framework.md`)

### Month 4–6 (Phase 2 Evaluation)

- [ ] Run Phase 2 gate checks (Section 6 above) at Month 4, 5, and 6 reviews
- [ ] If Gate A triggers: configure Etsy Ads for top-3 converting listings
- [ ] If Gate B triggers: begin guide production for highest-LTV underserved cohort
- [ ] Update `customer-retention-tracker.csv` with 90-day cohort performance for all cohorts born in Months 1–3

---

## 8. Measurement Cadence: Daily, Weekly, Monthly Runbook

This section defines exactly what to measure, when to measure it, and where to log it. Follow this cadence from Day 1 without exception; gaps in early-phase data cannot be reconstructed retroactively.

### Daily (Every Morning, ~10 Minutes)

**Source**: Etsy Shop Manager dashboard (not API — the dashboard updates within a few hours of activity; the API pull runs automatically via automation).

| Check | What to Look For | Alarm Condition | Action If Alarmed |
|---|---|---|---|
| New orders overnight | Count and total value | 0 orders for 3+ consecutive days after Week 1 | Check listing status (active/deactivated), check Etsy search visibility |
| New listing views | Total shop views (dashboard home) | View count drops >40% from prior day baseline | Check for search ranking change; note any Etsy algorithm announcements |
| GA4 Realtime | Active users, top sources | 0 active users mid-day weekday | GA4 ID may have been reset; re-verify Shop Manager > Web Analytics setting |
| Kit: email signups | New subscribers in last 24h | 0 signups after first week | Check opt-in form embed; check welcome sequence trigger |

**Daily log**: Keep a running notes file (even a plain text file on your desktop) recording: `date | orders | views | email_signups | notes`. This becomes the raw input for weekly review. No spreadsheet required in Week 1.

### Weekly (Monday Morning, ~30–45 Minutes)

**Source**: Etsy Stats dashboard (Traffic tab), GA4 (Acquisition report), Kit dashboard.

| Metric | Pull From | Log To | Week 1 Baseline | Week 4 Target |
|---|---|---|---|---|
| Total orders this week | Etsy API or Shop Manager | customer-analytics.csv (add new rows) | 5–15 | 10–25 |
| Top 3 listings by views | Etsy Stats > Traffic > Listing views | analytics/data/etsy_listing_stats_YYYY-MM.csv | Note all | Track week-over-week |
| Top traffic source | GA4 > Acquisition > Traffic acquisition | Monthly data log | Etsy organic | Etsy organic + Kit email |
| Kit email open rate | Kit dashboard > Broadcasts & Automations | Monthly data log | Welcome e1: 45%+ | Newsletter: 30%+ |
| Cohort assignments | customer-analytics.csv — count blank `final_cohort` rows | customer-analytics.csv | All blank (no surveys yet) | 60%+ assigned by Week 3 |
| Phase 2 gate proximity | Review gate thresholds (Section 6) | Gate Tracker in customer-retention-tracker.csv | All gates: not triggered | Watch Gate A after Week 6 |

**Weekly review question**: Is the conversion rate trajectory improving? Calculate: `(orders this week) / (listing views this week)` as a rough indicator. Etsy Stats calculates this more accurately on its Traffic tab, but the weekly manual calculation catches trends faster.

### Monthly (First Monday of Each Month, ~90 Minutes)

**Source**: All systems — comprehensive monthly close.

**Step 1: Pull Etsy API data** (or verify automated pull completed)
- Confirm `analytics/data/etsy_orders_YYYY-MM.csv` is complete for the closing month
- Verify order count matches what Etsy Shop Manager shows for the month (any discrepancy = investigate API pull)

**Step 2: Etsy Stats manual read**
- Navigate to Etsy Stats > Traffic (filter by closing month)
- Record: total visits, total orders, conversion rate, top 5 listings by views, top 5 search keywords, traffic source breakdown (% from Etsy search, social, direct, other)
- Save to `analytics/data/etsy_listing_stats_YYYY-MM.csv`

**Step 3: GA4 monthly export**
- GA4 > Reports > Acquisition > Traffic acquisition — export session data by source/medium
- GA4 > Reports > Engagement > Pages and screens — top 10 listing pages by views
- Note any anomalies (unexpected traffic spike from a specific referral, an unusual country)

**Step 4: Kit subscriber snapshot**
- Kit dashboard > Subscribers — record total count, new this month, unsubscribed this month
- Kit > Broadcasts — record open rate and click rate for each campaign sent
- Download subscriber CSV; save to `analytics/data/kit_subscribers_YYYY-MM.csv`

**Step 5: Cohort rollup**
- Update `customer-retention-tracker.csv` — add month row, calculate retention rates for cohorts aging out of Month 1, 2, 3
- For each cohort, calculate 90-day second-purchase rate using `customer-analytics.csv` data

**Step 6: Phase 2 gate check**
- For each gate in Section 6, compare current values against thresholds
- Update the PHASE_2_GATE_TRACKER section of customer-retention-tracker.csv with current values and statuses

**Monthly review questions** (answer each in writing, even briefly):
1. Did conversion rate improve, decline, or hold this month? Why?
2. Which cohort is showing the strongest repeat purchase signal? Does this match the hypothesis from `customer-cohort-analysis-framework.md`?
3. Which traffic channel sent the most high-quality sessions (longest session duration, lowest bounce)?
4. Is any single listing driving >40% of total orders? If yes, that's concentration risk — diversify proactively.
5. Are any Phase 2 gates within one month of triggering?

---

## 9. Failure Analysis: Signals, Root Causes, and Contingency Actions

Underperformance has specific causes that require different responses. Use this section before taking any reactive action. Do not change prices, listings, or ad strategy without first diagnosing the root cause using this framework.

### Failure Scenario 1: Low Views (Listings Not Being Found)

**Signal**: Top listings receiving fewer than 50 views per week by Week 3.

**Root cause diagnosis**:
- Check Etsy Stats > Traffic > Search keywords. If the primary keywords show zero impressions, the listing is not being indexed for those terms — review listing title and tags for keyword alignment.
- Check if listings are active and visible (Shop Manager > Listings > Active). A deactivated listing shows 0 views.
- Check Etsy search directly: search your own primary keywords in an incognito window. Do your listings appear on page 1 or 2? If not, you have a search ranking problem.

**Contingency actions** (in order):
1. **Week 1–2**: Refresh listing titles — front-load the highest-volume keyword in the first 40 characters. Etsy's search algorithm weights title-start keywords more heavily.
2. **Week 2–3**: Add 5–10 new tags using EverBee or eRank to identify underutilized medium-competition keywords that competitors are ranking for.
3. **Week 3+**: If views remain below 30/week on any listing, consider reducing that listing's price by $2–3 temporarily to improve price-competitiveness in search results (lower price can improve position on Etsy search).
4. **Month 2**: If no improvement after listing revision, pause that listing and test a new listing for the same product with a completely different title, description structure, and photo set.

**What not to do**: Do not launch Etsy ads on a low-view listing. Ads amplify discoverability only if organic search is partially working; they cannot substitute for zero organic indexing.

### Failure Scenario 2: Views Without Conversions (Listing Quality Problem)

**Signal**: Listings receiving 200+ views per month but converting below 1.0%.

**Root cause diagnosis**:
- High views, low conversion is a listing content problem — the customer arrives, looks, and decides not to buy.
- Most common causes: (a) price is above perceived value, (b) photos do not communicate the product's depth/quality, (c) description does not answer the buyer's top question ("what exactly will I get?"), (d) no reviews yet (social proof gap).

**Contingency actions** (in order):
1. **Immediately**: Add a preview image showing the table of contents or a sample page spread. Buyers of digital guides need to see the content depth before committing.
2. **Week 1 of diagnosis**: Rewrite the first 100 words of the description to directly answer: "Who is this for?" and "What will you learn?" — lead with specifics, not marketing language.
3. **Week 2**: If you have early buyers, message them directly asking for a review. A listing with 5+ reviews converts at approximately 2x the rate of a listing with 0 reviews.
4. **Week 3**: Test a $2 price reduction on the lowest-converting listing. If conversion improves materially (>0.5 percentage points), the price was the blocker.
5. **Month 2**: If conversion is still below 1.5% after the above, consider replacing the primary listing photo with a lifestyle/context image rather than a flat product shot.

**Benchmark context**: Average Etsy conversion rate is approximately 1–3% (per Etsy's published seller data and independent ecommerce benchmarks). For digital products, 2–4% is achievable once social proof exists. Below 1% after 30 days of live listing is underperformance; below 0.5% after 60 days requires structural revision.

### Failure Scenario 3: Low Repeat Purchase Rate (Retention Problem)

**Signal**: Month 3 second-purchase rate below 12% (minimum threshold defined in Section 5).

**Root cause diagnosis**:
- Repeat purchase failure usually has one of three causes: (a) the post-purchase email sequence is not triggering or is underperforming (check Kit automation logs first), (b) the product was purchased as a one-time gift (gift buyer cohort requires different strategy), (c) the product catalog is too thin to sustain repeat interest.

**Contingency actions** (by cause):

A. Email sequence failure — check Kit > Automations > [Post-Purchase Welcome] — is the sequence active and triggering? Open rate below 20% on Email 1 means a deliverability issue; check spam folder placements. Subject line A/B test if open rate is 20–35%.

B. Gift buyer cohort dominance — if Month 1–3 data shows >30% gift buyers (identified by seasonal purchase pattern and single purchase), the repeat rate will structurally underperform because gift buyers are one-and-done by design. The correct response is to shift acquisition toward forager and homesteader cohorts, not to try to convert gift buyers into repeat buyers.

C. Thin catalog — if a high-intent forager has bought all 3 relevant guides and there is nothing left to buy, they cannot repeat. Gate B (new guide launch) exists precisely to address this. If repeat rate is low and Gate B conditions are met, trigger new guide production.

### Failure Scenario 4: Revenue Plateau (Scale Ceiling Reached Organically)

**Signal**: Monthly order count stabilizes at 40–60 for 3 consecutive months without growth.

**Root cause diagnosis**:
- Organic plateau typically occurs when Etsy search ranking has stabilized and the listing's natural audience has been largely reached. At this point, you need external traffic to grow.

**Contingency actions**:
1. Check if Gate A (Etsy internal ads) is triggered — if conversion rate is 2.5%+ on qualifying listings, Etsy ads are the most capital-efficient next step.
2. If Gate A is not met, investigate why conversion is below 2.5% (use Failure Scenario 2 diagnosis above) before spending on ads.
3. If Gate A is triggered, start $5/day Etsy ads on top 3 listings. Watch ROAS for 30 days.
4. If Etsy ads ROAS is below 1.5 after 30 days, the listing's organic conversion is not strong enough to monetize paid traffic. Return to listing quality work before scaling.

### Failure Scenario 5: Sudden Order Drop (External Shock)

**Signal**: Order volume drops >50% week-over-week with no corresponding listing change.

**Root cause diagnosis**:
- Check if any listing was removed, suspended, or restricted by Etsy (check Shop Manager > Listings for any flags or notices)
- Check Etsy Status page (status.etsy.com) for platform outages
- Check if a major social platform has changed its algorithm (e.g., Pinterest distribution change)
- Check if a competitor has launched a significantly lower-priced alternative in the same niche

**Contingency actions**:
1. If listings are flagged: contact Etsy seller support immediately. Include proof of original content. Respond within 48 hours to minimize suspension duration.
2. If platform outage: wait 24–48 hours; no action needed.
3. If Pinterest algorithm shift: increase Reddit and email volume as interim traffic sources.
4. If competitor undercut pricing: do not panic-reduce price. Instead, differentiate on quality signals — add more photos, improve description detail, actively solicit reviews from current customers.

---

## 10. Cannibalization and Cross-Guide Substitution Framework

When a customer buys Guide A, does that reduce the probability of buying Guide B? This is distinct from cross-sell (where A increases B's probability). Cannibalization analysis is only meaningful once 60+ repeat buyers exist, which is expected around Month 4–5.

**Method**: Use `cohort-analysis-template.sql` Section 5.2 (cross-sell flow query). For each (first_product, second_product) pair, calculate:
- buyer_count: how many buyers made this transition
- conditional_probability: buyer_count / total_buyers_who_bought_first_product

**Substitution signal**: If Guides A and B have similar content (e.g., "Wild Edibles Northeast" and "Wild Edibles Pacific Northwest") and the transition probability from A → B is below 5% while the transition probability from A to an unrelated guide (e.g., "Medicinal Plants") is above 15%, then A and B are likely serving the same need for different geographies — not substitutes at the individual buyer level. Buyers in Oregon will not buy the Northeast guide; they are geographic complements, not cannibalistic substitutes.

**True cannibalization signal**: If an individual buyer purchases Guide A and then does not purchase Guide B despite being in the same geographic segment that typically buys both — and if this pattern holds for 10+ buyers — then A and B may be substitutes. In this case, bundling them as a discounted set is the recommended response, not removing one.

**Quarterly review**: Run the cross-sell flow query each quarter starting Month 4. Document results in WORKLOG.md under the review session.

---

*Cross-references: `customer-cohort-analysis-framework.md` (full cohort profiles and messaging), `etsy-ga4-event-tracking.md` (GA4 event schema), `customer-retention-tracker.csv` (individual customer log and monthly cohort rollup), `analytics/cohort-analysis-template.sql` (SQL queries), `analytics/monthly-metrics-checklist.md` (monthly operator runbook).*
