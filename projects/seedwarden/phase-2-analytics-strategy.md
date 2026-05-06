---
title: "Phase 2 Analytics and Cohort Segmentation Strategy"
date: 2026-05-06
session: 833
status: pre-launch design — do not implement dashboards yet
scope: Data architecture, cohort segmentation, dashboard templates, decision triggers
launch-date: 2026-05-30
references:
  - TRACK_B_FINAL_EXECUTION_GUIDE.md (Phase 2 timeline and launch sequence)
  - phase-3-product-expansion-roadmap.md (Phase 3 decision logic and cohort gates)
  - customer-cohort-analysis-framework.md (segment definitions and per-cohort messaging)
  - phase-2-post-launch-analytics-framework.md (measurement architecture)
  - etsy-ga4-event-tracking.md (GA4 custom event schema and audience definitions)
  - analytics/monthly-metrics-checklist.md (monthly operator runbook)
  - etsy-analytics-template.csv (historical data sample)
---

# Phase 2 Analytics and Cohort Segmentation Strategy

**Purpose**: Design the complete analytics infrastructure for the May 30, 2026 Phase 2 launch.
This document covers data collection, cohort segmentation, dashboard templates, and decision
triggers. The goal is Day 1 data accuracy so that every product, pricing, and expansion decision
from June onward is driven by evidence rather than assumption.

**Who this is for**: Anya, operating the store solo. All templates and frameworks are designed
for execution in Google Sheets or a lightweight dashboard tool — not enterprise infrastructure.
No engineering work is required. Every mechanism here can be operated by one person in the time
windows specified.

**What this is not**: Implementation instructions. The dashboards and tracking infrastructure
described here must be set up before May 30. This document tells you what to build, what to
measure, why each metric matters, and what action each measurement should trigger.

---

## Part 1: Data Source Integration

### 1.1 Etsy API — What Is Available and What to Do With It

Etsy's Open API v3 provides access to order data, listing stats, and financial transactions. At
Phase 2 scale (under 300 orders/month), manual daily exports are sufficient. Automated API pulls
are worth the setup time only after monthly orders exceed 100.

**Available via Etsy API v3 or Dashboard export:**

| Data Point | Source | Granularity | What It Tells You |
|---|---|---|---|
| Order count | Shop Manager > Orders | Per order | Total demand volume |
| Revenue per order | Shop Manager > Orders | Per order | AOV, bundle adoption |
| Revenue per listing | Shop Manager > Stats | Per listing, monthly | Which products earn |
| Views per listing | Shop Manager > Stats | Per listing, daily | Traffic quality |
| Conversion rate | Stats (derived: orders/visits) | Per listing, monthly | Messaging quality |
| Favorites | Shop Manager > Stats | Per listing | Buying intent signal |
| Traffic source breakdown | Shop Manager > Stats | Monthly aggregate | Which channel drives buyers |
| Geographic distribution | Shop Manager > Orders | Per order (city/state) | Regional cohort concentration |
| Repeat customer flag | Order history (email match) | Per buyer | Retention signal |
| Search terms that led to views | Stats > Search terms | Top 20 monthly | SEO performance |

**Not available via Etsy API:**
- Individual buyer demographics (age, income, gender)
- Abandoned cart data in real time
- Competitor listing performance
- Individual buyer browsing sessions on Etsy's marketplace

**API rate limits (Etsy Open API v3):**
- 10 requests per second per API key
- Daily quota not publicly published; practical ceiling for a solo operator doing automated
  daily pulls is well under any documented limit
- At Phase 2 scale, manual CSV exports from Shop Manager are lower friction than API integration
  and produce identical data. Use the API only if you build a Python automation script that
  runs daily and appends to the tracking spreadsheet

**Recommended Etsy data collection workflow (Phase 2, pre-automation):**
- Every Sunday morning: open Shop Manager > Stats, manually record the 7 metrics listed in the
  Weekly Dashboard template (Part 3.2 below) into the Google Sheet
- First of each month: export the full payment statement CSV and listing stats CSV, save to
  `projects/seedwarden/analytics/data/etsy_orders_YYYY-MM.csv`
- Cumulative customer list: maintain one sheet tab per month with each order as a row, buyer
  email as the key for repeat customer identification

**Python client option (implement in Month 2 if weekly data pull becomes a time burden):**
The `etsy-open-api-sdk` Python client (unofficial) supports listing and receipt endpoints.
A 40-line script can pull orders placed since the last run and append them to a CSV. Cost: one
afternoon of setup. Reference the cohort-analysis-template.sql in `analytics/` — the SQL
queries there assume a similarly structured flat file as input.

---

### 1.2 GA4 Custom Events — What to Track, Where, and How

GA4 fires on Etsy listing pages via the Shop Manager integration, but with significant constraints.
The existing `etsy-ga4-event-tracking.md` contains the full custom event schema. The following
summarizes what to prioritize for Phase 2 launch.

**GA4 hard constraints (cannot be changed):**
- GA4 fires only on individual listing pages, not Etsy search results or the Etsy homepage
- Purchase events cannot be captured by GA4 on Etsy. All transaction data comes from Etsy's
  own reporting
- No custom JavaScript injection is possible on Etsy listings

**What GA4 gives you that Etsy Stats does not:**
- Traffic source detail by channel (distinguishes Pinterest vs. Instagram vs. Reddit vs. direct)
- Device type per channel (mobile vs. desktop per source)
- Session duration on listing pages (proxy for content engagement)
- New vs. returning visitor distinction per listing
- Geographic detail down to city level
- Cohort-inferred signals from UTM campaign parameters

**GA4 setup actions required before May 30:**

1. Confirm GA4 Measurement ID is entered in Etsy Shop Manager > Settings > Web Analytics
2. Create the 6 custom dimensions in GA4 Admin > Custom Definitions (see etsy-ga4-event-tracking.md
   Section 2 for exact field names — these are case-sensitive)
3. Create the 5 audience segments in GA4 Admin > Audiences (Forager Signal, Prepper Signal,
   Homesteader Signal, Gift Buyer Signal, High-Value Repeat Candidate)
4. Verify events are firing: after entering the GA4 ID, open a Seedwarden Etsy listing in a
   browser, then check GA4 > Real-Time > Events — you should see `page_view` appear within
   60 seconds

**Zone-view tracking on the Kit landing page:**
The Kit zone-card landing page is the one Seedwarden-controlled surface where full GA4 custom
events can fire. Implement these two events on the Kit landing page:

- `view_zone_card_landing` — fires on page load; parameter: `acquisition_source` (from utm_source)
- `lead_magnet_signup` — fires on form submission; parameters: `acquisition_source`, `inferred_cohort`

These two events give you a conversion funnel: visits to the landing page vs. signups, segmented
by traffic source. This is the primary pre-purchase conversion funnel metric for Phase 2.

**UTM parameter convention (use consistently across all links):**

| Source | UTM Template |
|---|---|
| Instagram bio link | `?utm_source=instagram&utm_medium=social&utm_campaign=phase2_launch` |
| TikTok bio link | `?utm_source=tiktok&utm_medium=social&utm_campaign=phase2_launch` |
| Pinterest pin | `?utm_source=pinterest&utm_medium=pin&utm_campaign=[pin-slug]` |
| Email broadcast | `?utm_source=kit&utm_medium=email&utm_campaign=[email-name]` |
| Etsy listing footer CTA | `?utm_source=etsy_listing&utm_medium=product&utm_campaign=kit_signup` |

Apply these parameters to every outbound link from Day 1. Without UTM parameters on all links,
GA4 will attribute traffic as "direct" and the channel-by-channel picture will be meaningless.

---

### 1.3 Kit (Email Platform) — Cohort Exports and Segmentation

Kit is the primary cohort intelligence layer during Phase 2. Every behavioral signal captured
in Kit's tag system feeds the segmentation decisions in Part 2 of this document.

**Tags active at Phase 2 launch (from phase-2-kit-email-setup.md):**

Zone tags (8): `zone-3`, `zone-4`, `zone-5`, `zone-6`, `zone-7`, `zone-8`, `zone-9`, `zone-10`
Cohort tags (4): `Cohort_Forager`, `Cohort_Prepper`, `Cohort_Homesteader`, `Cohort_GiftBuyer`
Behavioral tags (3): `seed-saver`, `city-grower`, `preservationist`
Lifecycle tags (3): `new-subscriber`, `purchased`, `vip` (two or more purchases)

**How cohort tags are applied:**
- Primary assignment: post-purchase survey response (Day 1 order confirmation email)
- Fallback inference: product purchased determines likely cohort (wild-edibles guide buyer →
  `Cohort_Forager`; all-guides or bundle buyer → `Cohort_Prepper`)
- Behavioral confirmation: Email 3 and Email 4 click-tracking links apply `seed-saver`,
  `city-grower`, or `preservationist` tags based on what the subscriber clicks

**Monthly Kit export workflow (30 minutes, first Monday of each month):**
1. Kit > Subscribers > Export > CSV — save as `analytics/data/kit_subscribers_YYYY-MM.csv`
2. Open the CSV in Google Sheets; filter by `subscribed_at` to count new subscribers this month
3. Count subscribers per cohort tag: use COUNTIF on the tags column for each cohort tag value
4. Calculate open rate per cohort by filtering subscribers by tag and averaging their open_rate values
5. Record in the Monthly Data Log (Part 3.3 below)

**What Kit data tells you that Etsy does not:**
- Which messaging angles resonate with which cohort (by click behavior in Emails 3 and 4)
- Which subscribers are engaged vs. cold (open rate tracking)
- How many subscribers have converted to buyers (purchased tag)
- Zone distribution of the subscriber base (useful for planning seasonal zone-specific content)

---

### 1.4 Manual LTV Tracking — High-Ticket Spreadsheet

The customer LTV spreadsheet is the connective tissue between Etsy order data and Kit subscriber
data. At Phase 2 scale it is maintained manually — the extra friction of maintaining it is worth
it because it is the only place where individual customer lifetime value is tracked across
multiple purchases.

**File**: `projects/seedwarden/analytics/data/customer-ltv-tracker.csv`

**Columns to maintain:**

| Column | Source | Notes |
|---|---|---|
| `buyer_email` | Etsy order CSV | Primary key for repeat purchase matching |
| `first_order_date` | Etsy order | Cohort entry date |
| `first_product` | Etsy order | First entry product determines initial cohort inference |
| `cohort_tag` | Kit export or survey | Survey response overrides product-inferred cohort |
| `order_1_date` | Etsy order | |
| `order_1_value` | Etsy order | |
| `order_1_products` | Etsy order | Comma-separated product names |
| `order_2_date` | Etsy order | Blank if no repeat purchase |
| `order_2_value` | Etsy order | |
| `order_2_products` | Etsy order | |
| `order_3_date` | Etsy order | |
| `order_3_value` | Etsy order | |
| `ltv_to_date` | Formula: sum of all order values | `=SUM(order_1_value, order_2_value, order_3_value)` |
| `days_to_repeat` | Formula | `=order_2_date - order_1_date` (if order_2 exists) |
| `ltv_90d` | Formula | Sum of orders within 90 days of first_order_date |
| `kit_subscriber` | Kit export | `yes` / `no` — email match between Etsy and Kit |
| `notes` | Manual | Any qualitative observations from Etsy messages or reviews |

**Monthly update workflow (20 minutes):**
1. Open the Etsy orders CSV for the month
2. For each order: check if the buyer email already exists in the LTV tracker
3. If existing: add the new order as order_2 or order_3; recalculate LTV
4. If new: add a new row; classify cohort from product purchased or survey response
5. Update `ltv_90d` for any buyer whose first order was 90 days ago this month

**High-ticket flag:** Any buyer with LTV above $50 gets a `vip` tag in Kit. This is the
segment to watch most carefully — these buyers have demonstrated willingness to spend and are
the primary target for Phase 3 bundle upsells and seasonal campaigns.

---

## Part 2: Cohort Segmentation Strategy

### 2.1 The Four Core Segments and Their Phase 2 Signals

The four cohort definitions are fully specified in `customer-cohort-analysis-framework.md`. For
Phase 2 analytics purposes, the key addition is a tracking layer that measures whether actual
buyer behavior matches the pre-launch hypotheses.

**Cohort 1: High-Intent Forager (expected: 20–25% of buyers)**

Phase 2 signal indicators:
- Purchases: Wild Edibles Guide, Native Plants Regional Guide, or Medicinal Plants guide as
  first purchase
- Zone distribution: over-represented in Zone 6–8 (Pacific Northwest, Northeast, Upper Midwest)
- Session behavior: GA4 session duration above 120 seconds on wild-edibles or medicinal listing
- Email behavior: high click rate on botanical content in newsletter; clicked Email 3 seed-saving
  link
- AOV: $25–$60 (multi-guide orders or premium single guides)

Phase 2 hypothesis to validate: Forager cohort will over-index in Pacific Northwest and
Northeast geography. If California and Texas are as prominent as Oregon in the forager segment,
the geographic assumption in the messaging strategy needs revision.

**Cohort 2: Survival Prepper (expected: 15–20% of buyers)**

Phase 2 signal indicators:
- Purchases: Survival Garden Regional Plans, Hunting/Fishing Manual, Meat/Fish Preservation
  Manual, or any bundle with 5+ guides
- Single-order high value: most likely to buy 6+ guides in one transaction
- Email behavior: responds to event-triggered messaging (economic or weather news context)
- Zone distribution: more geographically uniform than forager cohort; slight rural concentration
- AOV: $45–$100+ (highest of the four cohorts)

Phase 2 hypothesis to validate: Prepper cohort has the highest per-order value but lowest
lifetime engagement (fewer but larger purchases). If repeat purchase rate for preppers exceeds
20% at 90 days, the messaging strategy should shift toward building a content relationship rather
than treating them as a one-time bulk buyer.

**Cohort 3: Homesteader (expected: 30–35% of buyers — largest cohort)**

Phase 2 signal indicators:
- Purchases: Seed Saving Field Manual, Zone Calendar, Companion Planting Chart, or preservation
  guides — bought incrementally rather than in bulk
- Repeat purchase pattern: 2–4 purchases at 30–60 day intervals (project-driven cadence)
- Email behavior: high open rate on newsletter; clicked Email 4 seed-saving or food-sovereignty
  link; responds to seasonal content about gardening cycles
- Zone distribution: concentrated in homesteading-dense regions (Vermont, Tennessee, Pacific NW,
  coastal California)
- AOV: $15–$45 per order; highest 12-month LTV through repeat purchasing

Phase 2 hypothesis to validate: Homesteader repeat purchase rate should exceed 25% at 90 days.
If it falls below 15%, the post-purchase email sequence is not reaching this cohort effectively
or the cross-sell product suggestion is misaligned with their next natural project step.

**Cohort 4: Gift Buyer (expected: 15–20% of buyers; peaks October–December)**

Phase 2 signal indicators:
- Purchases: any bundle listing, or a single guide priced above $20 as a solo purchase
- Session behavior: mobile device, session duration under 90 seconds, purchased without return
  visit; GA4 Gift Buyer Signal segment (mobile + short session in gift-window months)
- No repeat purchase within 60 days (single-occasion behavior)
- Traffic source: Pinterest gift guides, Instagram lifestyle posts, Etsy holiday browse

Phase 2 hypothesis to validate: May 30 launch falls near the June gift window (Father's Day).
If gift buyer signals (short mobile sessions, bundle purchases) appear in the first two weeks,
launch-week social content should be adjusted to include gift positioning language earlier than
the planned October push.

---

### 2.2 By-Zone Segmentation: Which Zones Attract Which Cohorts

The zone-card lead magnet creates a natural segmentation dimension that no competitor captures.
Track zone distribution monthly in the Kit subscriber export.

**Expected zone-to-cohort correlation (hypothesis, validate with data):**

| Zone | Primary Region | Expected Dominant Cohort | Reasoning |
|---|---|---|---|
| Zone 3–4 | Northern Midwest, Canada border | Prepper / Homesteader | Short growing season drives food storage emphasis |
| Zone 5–6 | Great Lakes, Mid-Atlantic, Pacific NW highlands | Homesteader / Forager | Broad growing season; active homesteading community density |
| Zone 7 | Pacific NW lowlands, Upper South | Forager / Homesteader | Mild climate supports diverse foraging; established PNW foraging culture |
| Zone 8 | Pacific Coast, Southeast | Forager / Gift Buyer | Year-round foraging; higher urban population = gift buyer density |
| Zone 9–10 | California, Deep South, Hawaii | Gift Buyer / Forager | Urban concentration; less traditional homesteading; garden-as-hobby framing |

**How to track zone-cohort correlation:**
Monthly, cross-reference Kit subscriber zone tag with Kit subscriber cohort tag. Calculate
the percentage of Zone X subscribers who also carry each cohort tag. A meaningful correlation
exists when one cohort tag is present in 40%+ of a zone's subscribers. Record in the Monthly
Data Log.

**Action trigger if zone-cohort data contradicts the hypothesis:**
If Zone 9–10 subscribers are predominantly `Cohort_Homesteader` rather than `Cohort_GiftBuyer`,
the newsletter content plan for those zones should de-emphasize gift positioning and add more
practical cultivation content (container growing, raised-bed cultivation in warm climates).

---

### 2.3 Cross-Project Segmentation: ModRun Buyers, Phase 1 Buyers, New Phase 2 Buyers

Phase 2 introduces new products and the Kit email system simultaneously. Three buyer populations
coexist starting May 30:

**Segment A: Returning Phase 1 Buyers**
Definition: Buyers who purchased a Phase 1 Etsy listing before May 30 and appear in the Etsy
order history. These buyers have already demonstrated purchase intent.

Tracking method: In the LTV tracker, flag all buyers with `first_order_date` before 2026-05-30
as `phase=1`. When Phase 2 launches, any second purchase from these buyers confirms the
cross-sell model is working.

Priority action for this segment: The post-purchase email sequence should fire for these buyers
if they subscribed to Kit via the Etsy thank-you message CTA. Check in Week 2 that Phase 1
buyers are in the Kit automation funnel.

**Segment B: New Phase 2 Buyers (first purchase on or after May 30)**
Definition: Any buyer whose `first_order_date` is 2026-05-30 or later.

Tracking method: Filter the LTV tracker by `first_order_date >= 2026-05-30`. These buyers
entered through Phase 2 acquisition channels (social media, Pinterest, the Kit landing page).
Their cohort distribution should reflect Phase 2's content emphasis — zone-specific content
and the forager/homesteader audience that the zone cards attract.

**Segment C: Kit Subscribers Who Have Not Yet Purchased (pre-customers)**
Definition: Subscribers in Kit without the `purchased` tag.

These are the highest-opportunity segment in Phase 2. They opted in for the zone card lead
magnet, completed (or are progressing through) the welcome sequence, and have not yet purchased.
Email 5 (SEEDWARDEN15 coupon) is the primary conversion mechanism for this segment.

Tracking method: Monthly, export Kit subscribers and filter for those without `purchased` tag.
Measure this count month-over-month. If this count is growing but the `purchased` tag count
is flat, the welcome sequence is building a list but not converting it — the Email 4 and Email
5 content needs revision.

**Segment D: ModRun Cross-Over Buyers (if applicable)**
If the project context includes buyers from the ModRun project who have been introduced to
Seedwarden through cross-promotion, tag them in Kit as `source=modrun` at time of subscription.
Track their cohort classification and 90-day conversion rate separately. Their product
preferences may differ from buyers who discovered Seedwarden through botanical content.

---

### 2.4 Seasonal Cohorts: How to Read the Launch Window

**Early Adopter Cohort (May 30 – June 30, 2026)**
These are buyers who find the store in the first 30 days. They are disproportionately driven
by social media launch content and existing email list awareness. They are not a random sample
of the eventual buyer population — they skew toward engaged followers who saw the launch posts.

Do not over-weight early adopter cohort data for Phase 3 product decisions. Wait for the 60-day
mark (July 30) before using cohort distribution to drive Phase 3 sequencing. The first two weeks
of launch data will over-represent forager and homesteader cohorts who follow botanical content
accounts, and under-represent the gift buyer cohort which primarily enters through Etsy search
and Pinterest discovery.

**Summer Preservation Peak Cohort (July – September 2026)**
These buyers arrive through Etsy organic search for canning, fermentation, and preservation
keywords. They skew homesteader and prepper. They are the cohort most responsive to Phase 3's
preservation derivative products. Signal: if preservation product revenue exceeds 25% of monthly
total in July, this cohort is activating and the Phase 3 preservation batch should launch on
schedule per the July 1 date in the Phase 3 roadmap.

**Holiday Gift Cohort (October – December 2026)**
These buyers arrive primarily through Pinterest gift guides and Etsy holiday browse. They are
the cohort with the highest single-transaction AOV and the lowest repeat purchase rate. The
October 15 Expanded Homesteader Gift Set ($62) launch is gated on this cohort's presence.
Signal: any month from October onward where bundles exceed 35% of revenue confirms the gift
buyer cohort is active.

---

## Part 3: Dashboard Design

### 3.1 Daily Dashboard (10 minutes)

**Tool**: Google Sheets with a "Daily" tab. Or Etsy Shop Manager app on your phone.
**When**: Morning check, 8–10am, every day for the first 30 days. Then Monday / Wednesday /
Friday only after data patterns are established.
**Purpose**: Catch anomalies before they compound. Not a decision-making session — just
a signal check.

**Daily Dashboard Template:**

```
SEEDWARDEN DAILY CHECK — [DATE]
================================================
Source: Etsy Shop Manager > Stats (today's view)

Orders today:              ___  (7-day avg: ___)
Revenue today:             $__  (7-day avg: $___)
Top product today:         ___
Conversion rate (today):   ___% (target: ≥1.5%)

Kit sign-ups today:        ___  (from Kit dashboard)
Total Kit subscribers:     ___

Any errors today?          [ ] Wrong product delivered  [ ] Negative review  [ ] Payment issue
================================================
SIGNAL:
  Revenue >200% of avg  → ☐ Check for viral social post / investigate source
  Revenue <30% of avg   → ☐ Check Etsy search ranking; is listing still active?
  0 orders, 50+ views   → ☐ Conversion problem; check listing images and price
  Kit sign-ups = 0      → ☐ Verify Kit landing page is still live
```

**What daily data tells you:**
- Revenue anomalies: a sudden spike often corresponds to a social post performing. Log the post
  and time — this is content intelligence for future posting
- Sustained low conversion (below 1% for 3+ consecutive days): the listing has a problem, not
  traffic. Do not increase social posting volume to compensate — fix the listing first
- Kit sign-up spikes: cross-reference with what was posted or pinned that day. This tells you
  which content type drives email subscribers vs. which drives Etsy buyers (they are different)

---

### 3.2 Weekly Dashboard (30 minutes, every Sunday)

**Tool**: Google Sheets "Weekly" tab. Populate manually from Etsy Stats and Kit dashboard.
**When**: Sunday evening, after the week's data has settled.
**Purpose**: Identify trends before they harden into problems.

**Weekly Dashboard Template:**

```
SEEDWARDEN WEEKLY REVIEW — Week of [DATE]
================================================
SECTION 1: SALES VELOCITY

              | This Week | Last Week | 4-Wk Avg | Trend
Orders        |           |           |          |
Revenue       | $         | $         | $        |
AOV           | $         | $         | $        |
Units sold    |           |           |          |

SECTION 2: PRODUCT PERFORMANCE (top 5 this week)

Product                | Orders | Revenue | % of Total | vs Last Wk
                       |        | $       | %          |
                       |        | $       | %          |
                       |        | $       | %          |
                       |        | $       | %          |
                       |        | $       | %          |
Other (all remaining)  |        | $       | %          |

SECTION 3: COHORT MIX (inferred from products sold + survey responses received)

Cohort        | % of Orders | Avg AOV | Repeat (90d) | vs Target
Forager       | %           | $       | %            | target 20-25%
Prepper       | %           | $       | %            | target 15-20%
Homesteader   | %           | $       | %            | target 30-35%
Gift Buyer    | %           | $       | %            | target 15-20%
Unknown       | %           | $       | —            | should be <20%

SECTION 4: EMAIL FUNNEL

Kit subscribers (end of week):    ___
New sign-ups this week:           ___
Email 1 open rate (this cohort):  ___% (target: 45%+)
Email 5 redemptions this week:    ___
Newsletter open rate (last send): ___% (target: 28%+)

SECTION 5: CHANNEL PERFORMANCE (from Etsy Stats > Traffic Sources)

Channel            | Sessions | % of Total
Etsy organic       |          |
Social referral    |          |
Direct             |          |
Other              |          |

================================================
WEEKLY QUESTIONS:
1. Which product drove the most growth this week?
   → Can it be paired with another product to increase AOV?

2. Which cohort is underrepresented vs. target?
   → Is this seasonal (expected) or a messaging gap?

3. Is AOV trending up (bundling working) or flat (single-guide preference)?
   → If flat after 4 weeks: add "frequently bought together" copy to top 3 listings

4. Did any launch-week social content correlate with an Etsy or Kit spike?
   → Log the content and timing for future replication
```

---

### 3.3 Monthly Dashboard (2 hours, first Monday of each month)

**Tool**: The existing `analytics/monthly-metrics-checklist.md` is the operator runbook for
this session. The template below is a supplementary summary layer that captures the Phase 2-
specific cohort and decision-trigger metrics that the existing checklist does not yet include.

**Monthly Dashboard Template (Phase 2 additions):**

```
SEEDWARDEN MONTHLY DEEP DIVE — [MONTH YEAR]
================================================
DATA SOURCES:
  Etsy: Shop Manager > Finances CSV + Stats CSV (export before starting)
  Kit: Subscribers CSV + Reports dashboard
  LTV tracker: customer-ltv-tracker.csv (update before starting)

BLOCK 1: REVENUE SUMMARY
  Gross revenue:          $___   | MoM change: ___% | vs target: ___
  Net revenue:            $___   (gross × 0.905 − $0.25 × orders)
  Orders:                 ___    | MoM change: ___%
  Unique buyers:          ___
  AOV:                    $___   | target: $15-20 (Phase 2 M1); $22-28 (M3+)
  Bundle revenue %:       ___% of total (target: 15%+ by Month 3)
  Phase 1 buyer repeat %: ___% (returning buyers from before May 30)

BLOCK 2: COHORT LTV ANALYSIS
  (From LTV tracker — filter by cohort_tag)

  Cohort        | Buyers | Avg LTV (to date) | 30d Repeat % | 90d Repeat % | Target 90d
  Forager       |        | $                 | %            | %            | 25-35%
  Prepper       |        | $                 | %            | %            | 15-25%
  Homesteader   |        | $                 | %            | %            | 18-25%
  Gift Buyer    |        | $                 | %            | %            | 3-8%

  Acquisition cost proxy:
    If running Etsy Ads: Ad spend / new buyers from ads = $___/buyer
    If social-only: estimate 0 (acquisition is organic)

BLOCK 3: PRODUCT CATEGORIZATION (rate each product this month)
  Classification guide:
    Star    = high sales + high margin (top 3 in revenue, above 1.5% CVR)
    Workhorse = steady sales, reliable (not top 3 but consistent month-over-month)
    Anchor  = drives traffic but lower margin (high views, below-avg CVR)
    Dog     = low sales + low conversion (<5 orders, <1% CVR after 30+ days)
    Hidden Gem = low orders but high customer satisfaction (strong reviews, low refund rate)

  Product               | Orders | Revenue | CVR% | Classification | Action
  [List top 10 products]

BLOCK 4: SEASONAL PATTERN CHECK
  Month [X] falls in season: [ ] Spring planning  [ ] Preservation  [ ] Holiday gift  [ ] Off-season
  Expected seasonal lift: ___% above baseline (see phase-3-product-expansion-roadmap.md Section 7)
  Actual performance vs. seasonal expectation: above / at / below

  Zone distribution this month (from Kit subscriber export):
    Top 3 zones by subscriber count: Zone ___, Zone ___, Zone ___
    Zone-cohort correlation: Zone ___  → dominant cohort is ___

BLOCK 5: EMAIL LIST HEALTH
  Total active subscribers:     ___   | target (M1): 50+; (M3): 200+
  New subscribers this month:   ___
  Net growth (new − unsubs):    ___
  MoM growth rate:              ___%

  Email 1 open rate:            ___% | target: 45%+ | alert: <30%
  Newsletter avg open rate:     ___% | target: 28%+ | alert: <22%
  Newsletter avg CTR:           ___% | target: 3%+  | alert: <2%
  Monthly unsubscribe rate:     ___% | healthy: <0.5%
  Email 5 coupon redemptions:   ___

  Behavioral tag counts:
    seed-saver: ___ | city-grower: ___ | preservationist: ___ | purchased: ___ | vip: ___

BLOCK 6: PHASE 3 READINESS SCORING
  (Score at end of each month; Phase 3 gate requires 5/6 criteria to pass by Month 2)

  [ ] ≥50 orders in 30 days                      PASS / FAIL: ___
  [ ] ≥$600 gross revenue in 30 days             PASS / FAIL: ___
  [ ] ≥1 "Star" product identified               PASS / FAIL: ___
  [ ] ≥2 cohorts each >20% of buyers             PASS / FAIL: ___
  [ ] ≥5% repeat purchase rate at 30 days        PASS / FAIL: ___
  [ ] <2% operational error rate                 PASS / FAIL: ___

  Phase 3 recommendation: GO / CONDITIONAL / NO-GO

ACTIONS ARISING:
  Priority 1 (this week): ___
  Priority 2 (this month): ___
  Priority 3 (watch list): ___
================================================
```

---

## Part 4: Decision Triggers

### 4.1 Revenue Underperformance Triggers

**Trigger: Daily revenue below 30% of 4-week rolling average for 3+ consecutive days**
Action: Check Etsy search ranking first. Open Seedwarden's top-performing listing in an
incognito browser and search its primary keyword. If it does not appear on page 1, the listing
has dropped in search ranking — this is not a traffic issue, it is an algorithmic issue.
Response: Check whether Etsy made algorithm changes (eRank or Marmalead will flag these).
Add 5 fresh tags using currently trending long-tail keywords. Update the listing description's
first paragraph. Do not pause paid ads during diagnosis — the traffic data is needed to distinguish
traffic drop from conversion drop.

**Trigger: Monthly revenue below $300 (first month) or below $600 (months 2–3)**
Action: This is the Phase 3 No-Go signal from the readiness scoring framework. Before drawing
conclusions: (1) is the revenue shortfall driven by views or by conversion? If views are high
(1,000+ per listing) but orders are low (<10), the problem is conversion (messaging, pricing,
or mockup quality). If views are low (<200 per listing), the problem is visibility (SEO, traffic
source, social media not driving clicks). Each diagnosis has a different response — do not apply
the wrong fix.

**Trigger: Etsy Ads ROAS below 1.5 for any listing after 21 days**
Action: Pause the ad for that listing immediately. The listing has a conversion problem that
paid traffic will not solve. Fix the listing (cover image, description opening, price) and
restart ads after 14 days of organic-only testing shows improvement.

**Trigger: Etsy Ads ROAS above 2.5 for 30+ days**
Action: Increase the daily budget for that listing by 25–50%. This is a scale signal, not a
maintenance signal.

---

### 4.2 Cohort Imbalance Triggers

**Trigger: Conservation-conscious buyers (Forager cohort) below 15% of total buyers at 60 days**
Signal: The botanical content and zone-card lead magnet are not attracting the forager cohort
at the expected rate. The most likely cause is messaging tone — the social content may be
skewing too far toward survival/prepper language and not enough toward botanical precision.

Action: Review the last 30 days of social posts and email content. If fewer than 30% of posts
have specific botanical content (species names, identification features, foraging ethics), add
two pieces of forager-specific content per week for the next 30 days. Check whether the Kit
sign-up form page copy leads with zone-specific content (which attracts homesteaders and
foragers) or with general gardening language (which attracts preppers and homesteaders but not
foragers).

**Trigger: Homesteader cohort above 50% of buyers at 60 days**
Signal: The content and product mix is resonating strongly with homesteaders but may be
under-serving foragers and preppers. This is not a bad outcome — homesteaders have the highest
12-month LTV — but it creates seasonal revenue concentration risk (homesteader purchasing
peaks in spring and fall, creating off-season troughs).

Action: Maintain homesteader content cadence but begin seeding two forager-specific pieces
per month into the newsletter and social calendar. This diversifies acquisition without
disrupting what is working.

**Trigger: Gift buyer cohort above 40% of buyers in October–December**
Signal: The gift positioning is working strongly but may be cannibalizing the year-round buyer
acquisition. If gift buyers represent more than 40% of the October–December total, the
non-gift months will be significantly lower in revenue.

Action: No corrective action needed — gift buyer seasonal concentration is expected and is
financially advantageous. Ensure Phase 3 gift products (Expanded Homesteader Gift Set at $62)
are live by October 15 to capture the peak.

---

### 4.3 Zone Saturation Triggers

A zone is "saturated" when the marginal return on zone-specific content decreases — meaning
additional zone cards, zone-specific social posts, or zone newsletter sections produce declining
subscriber or revenue growth from that zone.

**How to detect zone saturation:**
Monthly, plot new Kit subscribers by zone. Saturation signal: a zone's subscriber growth has
been flat or declining for 2 consecutive months despite active content promotion, AND that zone
already has more than 15% of total subscribers.

**Zone saturation action:**
Do not stop producing content for a saturated zone — existing subscribers in that zone are
still valuable, and seasonal content keeps them engaged. Instead, shift the acquisition focus
(social posts, Pinterest pins, paid promotion if applicable) toward zones that are growing
faster or are under-represented in the subscriber base.

**Zone gap signal:**
If Zones 3–4 (Northern states) represent less than 10% of subscribers at 90 days, this is a
geographic acquisition gap. Zones 3–4 are high-interest for homesteaders and preppers (short
growing season drives food preservation behavior). Create 2–3 Zone 3–4 specific Pinterest pins
and one newsletter section addressing short-season gardening challenges. Measure subscriber
growth from those zones in the following 30-day period.

---

### 4.4 Email Automation Underperformance Triggers

**Open rate below 25% on welcome sequence Email 1:**
This is a deliverability problem, not a content problem. Email 1 is sent immediately after
sign-up — it has the highest open rate of any email in the sequence by design (the subscriber
just signed up and wants the zone card). If Email 1 open rate is below 25%, check three things:
(1) SPF and DKIM DNS records are correctly configured in Kit (the setup requires these to be
active before significant volume); (2) the "From" email address uses a custom domain (not Gmail);
(3) the subject line "Your Zone [X] Quick-Start Card is ready" is not triggering spam filters.

**Click rate below 5% across the welcome sequence:**
The zone card download link click in Email 1 should generate 60–80% clicks (subscribers opened
the email specifically to get the card). The 5% threshold refers to the behavioral tracking
links in Emails 3 and 4. If click rate on those links is below 5%, the content hook in those
emails is not compelling the reader to explore further. Revise the Email 3 seed-saving story
to be more specific: instead of a general framing, name the exact mistake (the paper towel
germination error) and make the link's anchor text the specific technique, not a generic "click
here."

**Unsubscribe rate above 2% on any single email in the welcome sequence:**
A 2%+ unsubscribe on a single email means something in that email is misaligned with subscriber
expectations. The most common cause: Email 4 (catalog introduction) feels too promotional too
early. Revise Email 4 to lead with an additional educational story and move the catalog
introduction to the email's second half. The framing shift from "here is what I built" to "let
me show you how this system fits together" reduces the promotional feeling without removing the
catalog reference.

**Weekly newsletter open rate below 22% for 3 consecutive sends:**
Below 22% sustained over three weeks indicates list health degradation, not just a bad week.
Cause is typically one of three things: send frequency is too high (weekly is too much for this
audience — test bi-weekly for 4 weeks); subject line formula is predictable and subscribers
have stopped opening; or cold subscribers are dragging the average down without triggering
the win-back automation.

Action sequence: First, check the cold subscriber percentage (open rate below 15%). If cold
subscribers exceed 25% of the list, trigger the win-back automation immediately — cold
subscribers who do not re-engage after 3 emails should be removed. Second, test one subject
line revision for the next send (replace generic botanical topic with a specific seasonal
urgency hook). Third, if bi-weekly frequency reduces the open rate further, return to weekly
with a revised subject line approach.

---

## Part 5: Implementation Tools

### 5.1 Tool Recommendation: Google Sheets (Primary)

For Phase 2 at the projected scale (under 200 buyers/month, one operator), Google Sheets is
the correct tool. The reasons to stay in Sheets rather than adopting Looker Studio or Data Studio:

- **No data pipeline required**: Etsy and Kit both export CSV. Google Sheets imports CSV
  natively. Looker Studio and Data Studio require either a live connector or a programmatic data
  pipeline — both add setup complexity that is not justified at Phase 2 scale.
- **All formulas work offline**: The LTV tracker, cohort summary, and monthly dashboard can all
  be built with standard spreadsheet formulas (SUMIF, COUNTIF, AVERAGEIF, VLOOKUP). No database
  or API dependency.
- **Version control is manual but adequate**: Save a snapshot of the analytics spreadsheet as
  `analytics/seedwarden-analytics-YYYY-MM.xlsx` on the first of each month before updating it.
  This preserves a historical record without requiring version control tooling.

**When to upgrade to Looker Studio:**
Looker Studio is worth the setup time when: (1) monthly orders exceed 300 and manual CSV
import takes more than 30 minutes per week; (2) you want automated daily dashboard refresh
rather than manual Sunday updates; or (3) you want to share a read-only dashboard with a
collaborator. The Etsy → Google Sheets connector and Kit → Sheets connector via Zapier
(approximately $30/month) would feed Looker Studio automatically at that point.

**When to use the Jupyter notebook:**
The `analytics/dashboard-template.ipynb` notebook already exists in the project. Use it for
the monthly deep-dive cohort LTV calculations when the manual spreadsheet formulas become
unwieldy (more than 150 rows in the LTV tracker). The notebook's SQL queries from
`analytics/cohort-analysis-template.sql` can be run against the CSV exports directly.

---

### 5.2 Etsy API Python Client — Setup Reference

Do not set this up before Phase 2 launch. Set it up in Month 2 if weekly manual data entry
exceeds 45 minutes.

**What the script does:**
A 50-line Python script using the `requests` library (no SDK required) authenticates against
the Etsy Open API v3, queries the `/application/shops/{shop_id}/receipts` endpoint, and appends
new orders to the LTV tracker CSV. The Etsy Open API v3 requires OAuth 2.0 — the setup takes
approximately 90 minutes the first time.

**Practical setup reference:**
- Register an application at `https://www.etsy.com/developers/register`
- Use scopes: `transactions_r` (read receipts), `listings_r` (read listing data)
- Callback URL for local testing: `http://localhost:8080`
- After authentication, the access token is stored locally; the script exchanges it for fresh
  tokens as needed
- Rate limit: 10 requests/second. A daily pull of 30 days of orders runs in under 5 seconds

**Recommended script output:** Append to `analytics/data/etsy_orders_YYYY-MM.csv` with the
same column structure as the manual CSV export so formulas in the LTV tracker spreadsheet
require no changes.

---

### 5.3 GA4 JSON Export Workflow

GA4's standard export for reporting is via the GA4 UI (Explore or Reports). For monthly
reporting, manual export is sufficient.

**Monthly GA4 export steps (15 minutes):**
1. GA4 > Reports > Acquisition > Traffic acquisition
   - Set date range: prior calendar month
   - Export as CSV: saves session count and engagement rate by source/medium
2. GA4 > Reports > Engagement > Pages and screens
   - Filter: `page_location` contains `etsy.com/listing`
   - Export as CSV: saves views and engagement rate per listing page
3. GA4 > Admin > Data API > Export to BigQuery (optional, only if you activate BigQuery)

**What to do with the GA4 export:**
Cross-reference the listing pages by session volume against the Etsy Stats listing views.
GA4 will show lower numbers than Etsy Stats because GA4 only captures sessions from users
who have not blocked tracking. The ratio (GA4 sessions / Etsy views) should be stable month
over month. If it drops suddenly, a significant portion of new traffic may be bot traffic or
from a population with high tracking opt-out rates.

---

### 5.4 Kit API and Manual Export Scheduling

Kit's free tier does not include a public API. All Kit data collection during Phase 2 is via
manual CSV export from the Kit dashboard.

**Kit monthly export checklist:**
- [ ] Kit > Subscribers > Export > All subscribers > CSV
  - Save as `analytics/data/kit_subscribers_YYYY-MM.csv`
  - Columns to use: email, subscribed_at, tags, open_count, sent_count, click_count
- [ ] Kit > Reports > Sequences > Seedwarden Welcome
  - Screenshot or manually record: Email 1–5 open rates and click rates
- [ ] Kit > Reports > Broadcasts
  - Record: open rate, click rate, unsubscribe count for each broadcast sent this month
- [ ] Kit > Automations > check that all automations show "Live" status and have no errors

**Kit API (if you upgrade to Creator plan at $25/month):**
Creator plan includes API access. The Kit API supports subscriber listing, tag management, and
sequence reporting. A short script can automate the monthly export. At Phase 2 subscriber counts
(under 500), manual export takes 5 minutes and API setup is not worth the time investment.

---

## Part 6: Implementation Checklist (Before May 30)

The items below must be operational on launch day so that Day 1 data is captured correctly.
Each item references the document that contains full setup instructions.

### Analytics Infrastructure Setup (Complete by May 28)

- [ ] GA4 Measurement ID entered in Etsy Shop Manager > Settings > Web Analytics
  - Verify by checking GA4 Real-Time > Events after opening any Seedwarden listing
- [ ] GA4 custom dimensions registered (6 dimensions per etsy-ga4-event-tracking.md Section 2)
- [ ] GA4 audience segments created (5 segments per etsy-ga4-event-tracking.md Section 4)
- [ ] UTM parameters on all outbound links — Instagram bio, TikTok bio, Pinterest profile, Kit
  landing page, all Etsy listing footer CTAs
- [ ] Kit cohort survey is live in the Day 1 post-purchase email (order confirmation)
- [ ] Kit cohort tags are created: `Cohort_Forager`, `Cohort_Prepper`, `Cohort_Homesteader`,
  `Cohort_GiftBuyer` (per phase-2-kit-email-setup.md)
- [ ] Google Sheets analytics workbook created with tabs: Daily, Weekly, Monthly, LTV Tracker,
  Monthly Data Log

### Baseline Data Collection (May 30 — Launch Day)

- [ ] Record launch day baseline metrics at 9:00am before any posts go live:
  - Etsy listing views (starting count per listing)
  - Kit subscriber count
  - GA4 active users (Real-Time view)
- [ ] Record end-of-day May 30 metrics in the Daily tab
- [ ] First weekly review scheduled for Sunday June 7

### First Month Milestones

- [ ] Week 1 (June 7): First weekly dashboard review; confirm cohort survey responses are arriving
- [ ] Day 14 (June 13): Check whether Phase 1 buyers are entering Kit post-purchase sequence
- [ ] Day 30 (June 30): First monthly deep dive; run Phase 3 readiness score
- [ ] Day 30: Update LTV tracker with all orders from June; calculate 30-day repeat rate
- [ ] Day 30: Check cohort distribution against expectations; flag any imbalance for July content

---

## Part 7: Sample Metrics and Baseline Expectations

The following table establishes the expected ranges for Phase 2 Month 1, based on the historical
data in `etsy-analytics-template.csv` (which shows actual May 2026 performance: 47 orders,
$1,341 gross, 2.24% conversion rate, 14.9% repeat rate).

**Phase 2 Month 1 (May 30 – June 30, 2026) — Expected Ranges:**

| Metric | Conservative | Target | Stretch | Source of Expectation |
|---|---|---|---|---|
| Total orders | 25–45 | 46–70 | 71–100 | Phase 1 template data (47 orders in M1) |
| Gross revenue | $400–$700 | $700–$1,200 | $1,200–$2,000 | Phase 1 $1,341 gross M1 |
| Conversion rate | 1.0–1.5% | 1.5–2.5% | 2.5–3.5% | Phase 1 2.24%; target maintains or improves |
| AOV | $14–$20 | $20–$30 | $30–$40 | Phase 1 $28.51 AOV; Phase 2 bundles pull up |
| Kit sign-ups | 20–50 | 50–100 | 100–200 | New funnel; estimate from landing page CVR 25–35% |
| Email 1 open rate | 35–45% | 45–60% | 60%+ | Benchmark for welcome emails with fresh lists |
| Repeat rate (30d) | 5–10% | 10–20% | 20%+ | Phase 1 14.9%; Phase 2 adds post-purchase sequence |
| Bundle % of revenue | 0–10% | 10–20% | 20–30% | Phase 2 introduces first bundle push via email |
| Social referral % | 5–15% | 15–25% | 25–35% | Phase 2 adds active social presence for first time |

**Week 4 Checkpoint Targets (from TRACK_B_FINAL_EXECUTION_GUIDE.md Section 5):**

| Metric | Target | Source |
|---|---|---|
| Instagram followers | 150+ | Instagram Insights |
| Pinterest monthly views | 2,000+ | Pinterest Analytics |
| TikTok followers | 100+ | TikTok Analytics |
| Email subscribers | 50+ | Kit dashboard |
| Welcome email open rate | 40%+ | Kit email analytics |
| Etsy listing views (all) | 200+ | Etsy Shop Stats |

**Phase 3 Gate Metrics (by Day 60, approximately July 30):**

| Criterion | Pass | Fail | Action if Fail |
|---|---|---|---|
| Orders in 60 days | ≥80 total | <60 | Fix listing quality before Phase 3 development |
| Gross revenue (M2) | ≥$1,000 | <$600 | Pause Phase 3 content; do regional listings only |
| Cohort diversity | ≥2 cohorts >20% each | Only 1 cohort dominant | Adjust messaging mix; do not adjust product plan yet |
| Repeat rate (60d) | ≥15% | <10% | Audit post-purchase email delivery; verify Kit automation |
| Email list | ≥80 subscribers | <50 | Increase Kit landing page CTA visibility in Etsy listings |
| Star product | ≥1 product at ≥1.5% CVR | All below 1.5% | Prioritize listing optimization over new product development |

---

*Prepared: 2026-05-06. Session 833. This document is the analytics design layer for Phase 2
launch. For implementation of specific systems referenced here, see:
`etsy-ga4-event-tracking.md` (GA4 schema), `phase-2-kit-email-setup.md` (Kit configuration),
`analytics/monthly-metrics-checklist.md` (monthly operator runbook), `customer-cohort-analysis-framework.md`
(cohort definitions and messaging strategy), `phase-3-product-expansion-roadmap.md` (Phase 3
decision logic once data arrives).*
