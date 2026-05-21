---
title: Phase 2 Analytics & Success Metrics Tracker — Complete Setup
version: 1.0
date: 2026-05-21
status: production-ready
deadline: May 29 setup, May 30 launch-day activation
time-to-complete: 30 minutes (May 29)
owner: Seedwarden operator
cross-references:
  - PHASE_2_ANALYTICS_GOOGLE_SHEETS_TEMPLATE_SPEC.md (7-sheet column specs)
  - PHASE_2_ANALYTICS_INFRASTRUCTURE_PRESTAGING.md (API scripts)
  - phase-2-analytics-strategy.md (cohort logic)
  - etsy-ga4-event-tracking.md (GA4 custom event schema)
  - PHASE_2_ANALYTICS_SETUP_GUIDE.md (prior walkthrough)
---

# Phase 2 Analytics & Success Metrics Tracker

## Purpose

This document is the single authoritative setup reference for Phase 2 analytics. It replaces
the need to reference multiple prior documents. On May 29 you run through the 5-step procedure
in Section 5. On May 30 launch day you open the Google Sheet and start recording. All decision
thresholds, formulas, and API connection details you need are here.

**Launch goal**: Real-time dashboard visibility within 2 hours of first sales on May 30.

---

## Section 1: Overview

### Why This Matters

Phase 2 (May 30 – June 22) introduces wildflower, native plants, and ecosystem guides. Without
instrumented analytics from Day 1 you will not know which product is driving revenue, which
traffic channel is converting, or whether Phase 3 expansion criteria are being met. Retrofit
analytics after launch is always worse — baseline data is gone, early cohort behavior is lost,
and the first decision gate (Phase 3 go/no-go) arrives June 30 with no data to anchor it.

### What This System Provides

- **Daily visibility** (5 minutes/morning): order count, revenue, conversion rate, new signups
- **Weekly pattern detection** (10 minutes/Sunday): cohort mix, channel performance, trend alerts
- **Monthly synthesis** (30 minutes/June 30): scored Phase 3 go/no-go decision with 23 metrics
- **Anomaly triggers**: automated thresholds that flag problems before they compound

### Scope of the 23 Core Metrics

These are the only metrics that matter for Phase 2 decisions. Everything else is noise.

| Cadence | Count | Metrics Summary |
|---|---|---|
| Daily | 10 | Orders, revenue, AOV, conversion rate, cart abandonment proxy, refund flag, review count, repeat buyer %, session count, bounce rate proxy |
| Weekly | 15 | All daily + acquisition source breakdown, 7-day retention, 14-day retention, 30-day retention, repeat purchase rate, cohort AOV, guide-specific CVR, guide cross-sell %, seasonal variation index |
| Monthly synthesis | 23 | All weekly + Phase 3 trigger metrics (cohort size thresholds, LTV by cohort, bundle %, email list health, social velocity, zone distribution) |

---

## Section 2: Google Sheets Template Specification

### Overview

One Google Sheet. Seven tabs. Created once; used daily May 30 – June 30.

**File name**: `Seedwarden Phase 2 Analytics — May 30–June 30`

Create it at https://sheets.google.com. Share with yourself on mobile (File > Share > your email).

### Tab 1: Daily Dashboard

**Purpose**: Single daily snapshot. 5 minutes per morning. One row per day (May 30 – June 30).

| Col | Header | Source | Formula or Entry |
|---|---|---|---|
| A | Date | Manual | MM/DD format (e.g. 05/30) |
| B | Day | Formula | `=TEXT(DATE(2026,LEFT(A2,2),RIGHT(A2,2)),"ddd")` |
| C | Etsy Orders Cumul | Etsy Shop Manager | Running total of all orders since launch |
| D | Etsy Orders Today | Formula | `=C2-C1` |
| E | Revenue Cumul ($) | Etsy Shop Manager | Running total revenue |
| F | Revenue Today ($) | Formula | `=E2-E1` |
| G | AOV Today ($) | Formula | `=IF(D2=0,0,F2/D2)` |
| H | Listing Views Cumul | Etsy Stats | Running total views across all listings |
| I | Views Today | Formula | `=H2-H1` |
| J | Conversion Rate (%) | Formula | `=IF(I2=0,0,D2/I2*100)` |
| K | Refund Count | Etsy Shop Manager | Manual: count refunds processed today |
| L | Reviews Received | Etsy Shop Manager | Manual: count new reviews today |
| M | Repeat Buyers Today | Manual | How many orders today are from prior buyers |
| N | Kit Signups Cumul | Kit Dashboard | Running subscriber total |
| O | Kit Signups Today | Formula | `=N2-N1` |
| P | GA4 Sessions Today | GA4 Realtime | Manual from GA4 Reports > Acquisition |
| Q | Bounce Rate (%) | GA4 | Manual from GA4 Reports > Engagement (updated next day) |
| R | Status | Manual | GREEN / YELLOW / RED per Section 7 thresholds |
| S | Notes | Manual | Any anomaly, action taken, or context |

**Row 2 is the May 29 baseline** (filled the night before launch with starting counts).
**Row 3 is May 30** (first launch day).

### Tab 2: Weekly Analysis

**Purpose**: Aggregate daily rows into weekly summaries. One row per week. 10 minutes Sunday.

| Col | Header | Formula |
|---|---|---|
| A | Week | Manual: "W1 May 30–Jun 6" |
| B | Orders (week) | `=SUMIF(Daily!A:A,">="&DATE(2026,5,30),Daily!D:D)` adjusted per week range |
| C | Revenue (week $) | Analogous SUMIF on Daily!F |
| D | AOV (week) | `=IF(B2=0,0,C2/B2)` |
| E | Conversion Rate (%) | `=IF(SUMIF(weekly views)=0,0,(B2/SUMIF(weekly views))*100)` |
| F | Acquisition Source Top | Manual from Etsy Stats > Traffic |
| G | Top Guide by Orders | Manual from Etsy Stats > Listings |
| H | Guide Cross-Sell (%) | Manual: orders with 2+ guides / total orders × 100 |
| I | Kit Signups (week) | `=SUMIF(Daily!A:A, week range, Daily!O:O)` |
| J | 7-Day Retention (%) | Cohort Tracking tab lookup |
| K | 14-Day Retention (%) | Cohort Tracking tab lookup |
| L | 30-Day Retention (%) | Cohort Tracking tab lookup |
| M | Repeat Purchase Rate (%) | `=COUNTIF(Cohort!D:D,"Y")/COUNTA(Cohort!A:A)*100` |
| N | Cohort AOV — Forager | Manual from Cohort Tracking |
| O | Cohort AOV — Homesteader | Manual from Cohort Tracking |
| P | Seasonal Variation Index | Formula: `=(B2-AVERAGE(B$2:B$5))/AVERAGE(B$2:B$5)*100` — % deviation from 4-week avg |
| Q | Week Status | GREEN / YELLOW / RED |
| R | Decision Notes | Manual summary of what you learned and next action |

### Tab 3: Monthly Synthesis

**Purpose**: June 30 go/no-go scorecard. 23 metrics. One completion session.

This tab has a fixed layout — one metric per row, with columns for target, result, and pass/fail.

| Row | Metric Group | Metric | Target | Result (fill Jun 30) | Pass? |
|---|---|---|---|---|---|
| 2 | Revenue | Total gross revenue | $700+ | | Y/N |
| 3 | Revenue | AOV (month avg) | $20+ | | Y/N |
| 4 | Revenue | Bundle revenue % | 15%+ | | Y/N |
| 5 | Revenue | Refund rate | <3% | | Y/N |
| 6 | Orders | Total orders | 46+ | | Y/N |
| 7 | Orders | Conversion rate (avg) | 1.5%+ | | Y/N |
| 8 | Orders | Phase 3 trigger: cohort size | >500 total sessions | | Y/N |
| 9 | Cohort | Forager cohort % of buyers | 20-25% | | Y/N |
| 10 | Cohort | Homesteader cohort % | 30-35% | | Y/N |
| 11 | Cohort | Forager 30-day repeat rate | 25%+ | | Y/N |
| 12 | Cohort | Phase 3 trigger: conversion rate | >8% listing CVR on top guide | | Y/N |
| 13 | Cohort | Phase 3 trigger: AOV threshold | >$45 for 2+ guide orders | | Y/N |
| 14 | Cohort | Phase 3 trigger: repeat rate | >12% 30-day | | Y/N |
| 15 | Products | Star products identified | 2+ | | Y/N |
| 16 | Products | Cross-sell rate | 15%+ | | Y/N |
| 17 | Products | Phase 1 repeat purchase rate | 35%+ | | Y/N |
| 18 | Email | Kit total subscribers | 200+ | | Y/N |
| 19 | Email | Welcome Email 1 open rate | 45%+ | | Y/N |
| 20 | Email | Newsletter avg open rate | 28%+ | | Y/N |
| 21 | Email | Revenue/subscriber proxy | $0.10+ | | Y/N |
| 22 | Social | IG follower total | 400+ | | Y/N |
| 23 | Social | Social combined velocity | 3+/day new followers avg | | Y/N |
| 24 | Ops | Zero critical failures (0 wrong files, 0 payment errors) | Pass | | Y/N |

**Score row** (Row 26):
```
=COUNTIF(F2:F24,"Y") & "/23 — " & IF(COUNTIF(F2:F24,"Y")>=20,"PHASE 3 OPTION B APPROVED",IF(COUNTIF(F2:F24,"Y")>=16,"PHASE 3 OPTION A APPROVED","PHASE 3 DEFERRED"))
```

**Decision thresholds**:
- 20-23 criteria pass: Phase 3 Option B approved — full expansion, Sep 2026
- 16-19 pass: Phase 3 Option A — reduced scope, 2-3 products
- Under 16: Phase 3 deferred — continue Phase 2 optimization through Sep

### Tab 4: Cohort Tracking

**Purpose**: Track customer acquisition by source and measure retention curves over time.

| Col | Header | Notes |
|---|---|---|
| A | Entry Date | Date of first purchase or Kit signup |
| B | Source | "Kit Email", "Instagram", "TikTok", "Pinterest", "Etsy Search", "Direct" |
| C | Cohort Size | Count of buyers from this source on this date |
| D | Phase 1 Repeat? | Y if buyer has a prior Phase 1 purchase |
| E | Orders W1 | Purchases in Week 1 (by Jun 6) |
| F | Revenue W1 ($) | Total revenue Week 1 |
| G | AOV W1 | `=IF(E2=0,0,F2/E2)` |
| H | Active at 7 Days | Count still in funnel at Day 7 |
| I | Active at 14 Days | Count still in funnel at Day 14 |
| J | Active at 30 Days | Count still in funnel at Day 30 |
| K | 7-Day Retention (%) | `=IF(C2=0,0,H2/C2*100)` |
| L | 14-Day Retention (%) | `=IF(C2=0,0,I2/C2*100)` |
| M | 30-Day Retention (%) | `=IF(C2=0,0,J2/C2*100)` |
| N | Orders Month-End | Total purchases by Jun 30 |
| O | Revenue Month-End ($) | Total revenue by Jun 30 |
| P | LTV Estimate | `=O2` |
| Q | Top Product | Which product this cohort bought most |
| R | Cohort Tag | Forager / Prepper / Homesteader / GiftBuyer |
| S | Notes | Qualitative observations |

**Retention curve summary** (add below the data rows, at row 50+):
```
7-day avg retention:  =AVERAGE(K2:K40)
14-day avg retention: =AVERAGE(L2:L40)
30-day avg retention: =AVERAGE(M2:M40)
```

### Tab 5: Product Performance

**Purpose**: Per-guide metrics for Phase 3 product decisions. One row per product.

| Col | Header | Source | Formula |
|---|---|---|---|
| A | Product Name | Etsy Listings | Exact title |
| B | Phase | Manual | "Phase 1" or "Phase 2" |
| C | Price ($) | Etsy | Current price |
| D | Views (May 29 baseline) | Etsy Stats | Record May 29 |
| E | Views (Jun 30) | Etsy Stats | Record Jun 30 |
| F | Views Gained | Formula | `=E2-D2` |
| G | Favorites (May 29) | Etsy Stats | Record May 29 |
| H | Favorites (Jun 30) | Etsy Stats | Record Jun 30 |
| I | Favorites Gained | Formula | `=H2-G2` |
| J | Orders | Etsy Shop Manager | Count by product Jun 30 |
| K | Revenue ($) | Etsy Shop Manager | Sum by product |
| L | Conversion Rate (%) | Formula | `=IF(E2=0,0,J2/E2*100)` |
| M | Cross-Sell Count | Manual | How many of this product's buyers also bought another guide |
| N | Refunds | Etsy | Count refunds for this product |
| O | Avg Review (stars) | Etsy | Average star rating |
| P | Classification | Manual | Star / Workhorse / Anchor / Dog / Hidden Gem |
| Q | Phase 3 Action | Manual | Expand / Maintain / Archive / Investigate |
| R | Notes | Manual | |

**Classification guide** (add to a notes cell in Tab 5):
- Star: top 3 in revenue AND CVR above 1.5%
- Workhorse: consistent orders, steady CVR, not top 3
- Anchor: high views, low conversion — investigate listing quality
- Dog: fewer than 5 orders and CVR below 1% after 30+ days
- Hidden Gem: few orders but strong reviews and low refund rate — promote more

### Tab 6: Acquisition ROI

**Purpose**: Cost-per-acquisition by channel. Informs paid ad decisions.

| Col | Header | Formula/Source |
|---|---|---|
| A | Channel | Kit Email / Instagram Organic / TikTok Organic / Pinterest Organic / Etsy Search / Instagram Ads |
| B | Signups | Manual (from Kit tag counts or campaign UTM data) |
| C | Orders | Manual (from Etsy "how did they find you" or UTM attribution) |
| D | Revenue ($) | Manual |
| E | Ad Spend ($) | Manual (0 for organic channels) |
| F | Cost per Signup ($) | `=IF(B2=0,"N/A",E2/B2)` |
| G | Cost per Order ($) | `=IF(C2=0,"N/A",E2/C2)` |
| H | LTV per Customer ($) | `=IF(C2=0,"N/A",D2/C2)` |
| I | ROI (%) | `=IF(E2=0,"Organic",((D2-E2)/E2)*100)` |
| J | ROAS | `=IF(E2=0,"Organic",D2/E2)` |
| K | Channel Status | Scale / Optimize / Pause / Monitor |

**Paid ads trigger** (note cell at Tab 6 bottom):
If organic Kit Email channel delivers ROAS "Organic" and 15+ orders, hold on paid ads.
If total monthly orders drop below 25 for 2 consecutive weeks, activate Instagram Ads at
$5/day budget. Pause any ad with ROAS below 1.5 after 21 days. Scale any ad with ROAS above
2.5 by 25-50% budget increase.

**Looker Studio upgrade trigger** (note cell):
If total orders exceed 200/month, set up Looker Studio with Etsy API connector and GA4 connector
for automated dashboard refresh. Until then, Google Sheets is sufficient.

### Tab 7: Go/No-Go Decision Log

**Purpose**: Chronological record of every major go/no-go decision with rationale. Non-negotiable
documentation for Phase 3 planning — if something goes wrong, this log tells you what was decided
and why.

| Col | Header |
|---|---|
| A | Date |
| B | Time |
| C | Decision Name |
| D | Type (GO / NO-GO / ESCALATE / CONTINGENCY) |
| E | Primary Metric |
| F | Metric Value |
| G | Target |
| H | Status (PASS / FAIL / WATCH) |
| I | Action Taken |
| J | Outcome (filled 1-7 days later) |

**Pre-populate these rows on May 29**:

| Date | Time | Decision | | | Target | | | |
|---|---|---|---|---|---|---|---|---|
| 05/30 | 12:05pm | Checkpoint 1 — broadcast sent | | Kit Signups | ≥3 by T+5 min | | | |
| 05/30 | 9:00pm | Checkpoint 2 — end of Day 1 | | Etsy Orders | ≥1 | | | |
| 06/06 | 10:00am | Week 1 go/no-go | | Orders + Revenue | ≥5 orders, ≥$75 | | | |
| 06/30 | 6:00pm | Phase 3 gate decision | | Monthly Synthesis score | 20+/23 | | | |

---

## Section 3: Daily/Weekly/Monthly Formulas

### Daily Metric Calculations

All formulas assume Daily Dashboard tab with headers in Row 1 and May 29 baseline in Row 2.

**New orders today** (difference from cumulative — safest method):
```
=IF(ROW()=2, 0, C3-C2)
```
where C = Etsy Orders Cumul. The ROW()=2 check prevents a negative value on the baseline row.

**Average order value (today)**:
```
=IF(D3=0, 0, F3/D3)
```
where D = Orders Today, F = Revenue Today.

**Conversion rate (daily)**:
```
=IF(I3=0, "—", TEXT(D3/I3*100,"0.0")&"%")
```
where I = Views Today, D = Orders Today.

**Repeat buyer rate (rolling, based on Cohort tab)**:
```
=COUNTIF(Cohort!D:D,"Y")/MAX(1,COUNTA(Cohort!A:A)-1)*100
```

**Cart abandonment proxy** (no direct Etsy API data — use this approximation):
```
Favorites without order = (Favorites Gained today) - (Orders Today)
```
This is imprecise but directionally useful. A ratio above 10:1 (10 favorites per order) suggests
a listing is attracting interest but not converting — investigate price, description, or photos.

**Refund rate (rolling)**:
```
=IF(C_orders_cumul=0,0,(SUM(K$2:K_today)/C_orders_cumul)*100)
```
where K = Refund Count column. Alert threshold: above 3%.

**GA4 bounce rate proxy**: Pull from GA4 > Reports > Engagement > Pages and Screens. Set date to
yesterday, filter by etsy.com listing pages, read "Bounce rate" column. Manual entry daily.

### Weekly Metric Calculations

**Weekly orders from Daily data**:
```
=SUMPRODUCT((Daily!A$3:A$33>=DATE_START)*(Daily!A$3:A$33<=DATE_END)*Daily!D$3:D$33)
```
Replace DATE_START and DATE_END with the week's start and end as DATE() formulas.

Simpler alternative if you know the row range (Week 1 = rows 3-9 in Daily):
```
=SUM(Daily!D3:D9)    (orders)
=SUM(Daily!F3:F9)    (revenue)
=SUM(Daily!O3:O9)    (Kit signups)
```

**Week-over-week change (%)**:
```
=IF(B_prev_week=0,"N/A",((B_this_week-B_prev_week)/B_prev_week)*100)
```

**Cohort AOV** (Forager example):
```
=AVERAGEIF(Cohort!R:R,"Forager",Cohort!G:G)
```
where R = Cohort Tag, G = AOV W1.

**Guide cross-sell rate (weekly)**:
Manually check Etsy Shop Manager > Orders for this week. Count orders that contain 2+ different
guide listings. Divide by total orders for the week. Record as %.
Formula: `=M_crossell_count / B_orders_week * 100`

**Seasonal variation index** (compares this week to running average):
```
=IF(COUNT(B$2:B2)<2,"—",((B_this_week-AVERAGE(B$2:B2))/MAX(1,AVERAGE(B$2:B2)))*100)
```
Values above +30% suggest a spike (viral post, featured listing). Values below -30% suggest
a trough (investigate platform issue or external factor).

**7-day retention** (from Cohort Tracking tab):
```
=AVERAGEIF(Cohort!A:A,">="&(DATE_START-7),Cohort!K:K)
```
where K = 7-Day Retention %. This averages the 7-day retention rate for cohorts who entered
in the prior week.

### Monthly Metric Calculations

**Total gross revenue (month)**:
```
=SUM(Daily!F3:F33)
```

**Monthly AOV**:
```
=IF(SUM(Daily!D3:D33)=0,0,SUM(Daily!F3:F33)/SUM(Daily!D3:D33))
```

**Phase 1 repeat purchase rate**:
Manual calculation. From Etsy orders CSV:
1. List all buyer emails from Phase 1 (pre-May 30) purchases
2. Cross-reference against Jun 1-30 order emails
3. Rate = (count of matching emails) / (total Phase 1 unique buyers) × 100

**Bundle revenue %**:
```
=SUMIF(Product!A:A,"*Bundle*",Product!K:K) / SUM(Product!K:K) * 100
```
where Product!A = Product Name, Product!K = Revenue.

**Email revenue per subscriber proxy**:
```
=SUM(Daily!F3:F33) / MAX(1, Daily!N33)
```
where N33 = Kit Signups Cumul on June 30.

**Phase 3 trigger: conversion rate on top guide**:
Find the product with the highest CVR in Tab 5 (Product Performance). If that CVR exceeds 8%,
the Phase 3 trigger fires. Formula: `=MAX(Product!L:L)` — if result >= 8, Phase 3 trigger active.

**Phase 3 trigger: AOV for multi-guide orders**:
In the Cohort Tracking tab, filter for cohorts where N (Orders Month-End) / C (Cohort Size) > 1.
Calculate average O (Revenue Month-End) / N (Orders). If that number exceeds $45, trigger fires.

---

## Section 4: API Connection Details

### Etsy API — Endpoints and Authentication

**Registration**: https://developer.etsy.com — create an app called "Seedwarden Analytics".

**Auth type**: OAuth 2.0. Required scopes:
- `listings_r` — read listing data (views, titles, prices)
- `transactions_r` — read orders and receipts
- `shops_r` — read shop-level stats

**Key endpoints** (Etsy Open API v3, base URL: `https://api.etsy.com/v3/application`):

| Endpoint | Method | What It Returns |
|---|---|---|
| `/shops/{shop_id}/receipts` | GET | All orders; filter with `min_created` Unix timestamp |
| `/shops/{shop_id}/receipts/{receipt_id}/transactions` | GET | Line items for an order |
| `/shops/{shop_id}/listings/active` | GET | All active listings with prices and stats |
| `/shops/{shop_id}/stats` | GET | Shop-level stats (views, visits) |

**Rate limits**: 10 requests/second. Daily quota is not published but well above Phase 2 needs.
Use `time.sleep(0.1)` between calls in any automation script.

**Where to find your Shop ID**: Etsy Shop Manager > Settings > Info & Appearance > Shop ID field.

**Access token refresh**: Tokens are valid for approximately 3600 seconds (1 hour) with a refresh
token valid for 90 days. The daily sync script in `PHASE_2_ANALYTICS_INFRASTRUCTURE_PRESTAGING.md`
handles this automatically. If you get a 401 Unauthorized error, the access token has expired —
run `scripts/etsy_oauth_token.py` to regenerate.

**Manual alternative** (no API): Etsy Shop Manager > Stats exports a CSV via the "Download CSV"
button in the Stats section. This is sufficient for Phase 2 — use the API script only if manual
downloads exceed 30 minutes per week.

### GA4 — Custom Event Schema and Audience Creation

**Measurement ID location**: GA4 Admin > Data Streams > your stream > Measurement ID (G-XXXXXXX).
**Entry point in Etsy**: Etsy Shop Manager > Settings > Options > Web Analytics > paste Measurement ID.

**Custom dimensions to create** (GA4 Admin > Custom Definitions > Custom Dimensions):

| Dimension Name | Scope | Event Parameter Name |
|---|---|---|
| guide_category | Event | guide_category |
| acquisition_source | Event | acquisition_source |
| buyer_cohort_inferred | User | buyer_cohort_inferred |
| zone_number | Event | zone_number |
| email_campaign_id | Event | email_campaign_id |

**Four GA4 audiences to create** (GA4 Admin > Audiences):

Audience 1 — Forager Signal:
```
Page path contains "wild-edibles" AND session engagement time > 120 seconds
OR guide_category = "wild-edibles" in past 30 days
```

Audience 2 — Prepper Signal:
```
Visited bundle listing
OR visited 3+ guide pages in a single session
```

Audience 3 — High-Value Repeat Candidate:
```
First visit 30+ days ago
AND visited listing page 3+ times total
AND average session duration > 90 seconds
```

Audience 4 — Kit Email Engaged:
```
utm_source = "kit" on first visit
OR multiple visits from utm_campaign containing "phase2"
```

**Verification test** (run this May 28):
Open a Seedwarden Etsy listing in a private/incognito browser. Go to GA4 > Real-Time > Events.
Within 60 seconds you should see a `page_view` event appear. If it does not appear, the
Measurement ID is not correctly entered in Etsy Shop Manager.

**GA4 limitations on Etsy**: You cannot fire custom JavaScript events on Etsy listing pages.
GA4 captures page views and session data only. For custom event firing (guide download tracking,
email click tracking), you can only do this on your Kit landing page.

**Kit landing page GA4 events** (add to Kit page source via Kit's custom code/embed feature):
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');

  // Fire on landing page load
  window.addEventListener('load', function() {
    const src = new URLSearchParams(window.location.search).get('utm_source') || 'direct';
    gtag('event', 'view_zone_card_landing', { acquisition_source: src });
  });
</script>
```

Replace `G-XXXXXXXXXX` with your actual Measurement ID.

### Kit Integration — Email Acquisition Tracking

**Kit API availability**: Kit's free tier does not include API access. All Kit data collection
is manual CSV export until you upgrade to Creator plan ($25/month).

**Monthly Kit export** (first Monday of each month, 5 minutes):
1. Kit > Subscribers > Export > All subscribers > CSV
2. Save as `/projects/seedwarden/analytics/data/kit_subscribers_YYYY-MM.csv`
3. Columns you will use: email, subscribed_at, tags, open_count, sent_count, click_count

**Tags that must exist in Kit > Tag Manager before May 30**:

Zone tags: `zone-3`, `zone-4`, `zone-5`, `zone-6`, `zone-7`, `zone-8`, `zone-9`, `zone-10`

Cohort tags: `Cohort_Forager`, `Cohort_Prepper`, `Cohort_Homesteader`, `Cohort_GiftBuyer`

Behavioral tags: `seed-saver`, `city-grower`, `preservationist`

Lifecycle tags: `new-subscriber`, `purchased`, `vip`

**Automation triggers to verify**:
- New subscriber → applies `new-subscriber` tag → triggers Welcome Sequence (Emails 1-5)
- Email 3 link click → applies behavioral tag (`seed-saver`, `city-grower`, or `preservationist`)
- Manual tag: after each Etsy order, apply `purchased` tag to the matching subscriber email
- Manual tag: after 2+ purchases, apply `vip` tag

**UTM parameters on all outbound links** (verify every link before May 30):

| Surface | UTM Template |
|---|---|
| Instagram bio | `?utm_source=instagram&utm_medium=social&utm_campaign=phase2_launch` |
| TikTok bio | `?utm_source=tiktok&utm_medium=social&utm_campaign=phase2_launch` |
| Pinterest pins | `?utm_source=pinterest&utm_medium=pin&utm_campaign=[pin-slug]` |
| Kit broadcast | `?utm_source=kit&utm_medium=email&utm_campaign=phase2-launch-broadcast` |
| Etsy listing footer CTA | `?utm_source=etsy_listing&utm_medium=product&utm_campaign=kit_signup` |

Without these UTM parameters, all traffic appears as "direct" in GA4 and you cannot attribute
signups or orders to their source channel.

---

## Section 5: User Setup Procedure (May 29, ~30 minutes)

Run these 5 steps on May 29. Total time: 30 minutes. You do not need to finish all at once —
Steps 1-3 can be done any time before May 29, Steps 4-5 must happen on May 29.

### Step 1: Connect Etsy to GA4 (5 minutes — do by May 25)

1. Log into GA4: https://analytics.google.com
2. Go to Admin (gear icon, bottom left)
3. Note your **Measurement ID** — format is `G-XXXXXXXXXX` — write it down
4. Go to Etsy Shop Manager: https://www.etsy.com/your/shops/me/shop-home
5. Settings > Options > Web Analytics
6. Paste your Measurement ID and click Save
7. Verify: open a Seedwarden listing in an incognito tab, then check GA4 > Real-Time > Events
   for a `page_view` event within 60 seconds

If no event appears: double-check the Measurement ID was pasted without spaces. Wait 5 minutes
and try again before assuming a configuration problem.

**Enable required custom dimensions** (GA4 Admin > Custom Definitions):
Create all 5 custom dimensions listed in Section 4. This takes about 5 minutes.

### Step 2: Connect GA4 to Kit (5 minutes — do by May 25)

1. Log into Kit: https://kit.com (or app.kit.com)
2. Settings > Integrations > Analytics
3. Enable Google Analytics 4
4. Paste your Measurement ID and click Connect
5. Verify: check that Kit's confirmation shows "Connected" status

Also add the Kit landing page GA4 event script (Section 4) to your Kit page via Kit's
Settings > Landing Page > Custom Code section if available, or via Kit's embedded HTML block.

### Step 3: Create the Google Sheet (10 minutes — do by May 27)

1. Go to https://sheets.google.com > New > Blank spreadsheet
2. Name it exactly: `Seedwarden Phase 2 Analytics — May 30–June 30`
3. Create 7 tabs by right-clicking the bottom tab bar and selecting "Insert sheet":
   - Tab 1: `Daily Dashboard`
   - Tab 2: `Weekly Analysis`
   - Tab 3: `Monthly Synthesis`
   - Tab 4: `Cohort Tracking`
   - Tab 5: `Product Performance`
   - Tab 6: `Acquisition ROI`
   - Tab 7: Decision Log
4. For each tab, add the column headers from Section 2 (copy directly from this document)
5. Add formulas to derived columns (marked "Formula" in Section 2 column tables)
6. Share with yourself on mobile: File > Share > type your phone email > Send
7. Bookmark on your phone browser for launch-day access

**Shortcut if formulas feel complex**: Leave formula cells blank for now. Start with manual
entry for every column on May 30. Add formulas in Week 2 once you understand the data flow.
The information matters more than the automation.

### Step 4: Record May 29 Baselines (10 minutes — must happen May 29)

This step must happen on May 29, the night before launch. Etsy does not allow retroactive
baseline snapshots.

**From Etsy Shop Manager > Stats** (filter to today, May 29):
- Record total views on each active listing — paste into Product Performance tab, column D
- Record total favorites on each listing — paste into column G
- Record total orders to date — paste into Daily Dashboard Row 2, column C
- Record total revenue to date — paste into Daily Dashboard Row 2, column E

**From Kit Dashboard**:
- Record total subscriber count — paste into Daily Dashboard Row 2, column N
- Screenshot the tag distribution (Subscribers > Tags) for baseline reference

**From Instagram, TikTok, Pinterest**:
- Record follower counts on all three platforms in your notes (not in the tracker — these
  aren't in scope for the core 23 metrics, but useful context)

**Label Row 2 in Daily Dashboard**: Enter "05/29 Baseline" in column A, and enter 0 in all
"today" delta columns (D, F, G, I, O) since nothing has happened yet.

### Step 5: Template Walkthrough (5 minutes — do this reading now)

Before May 30 morning, familiarize yourself with each tab:

**Daily Dashboard** — you will open this every morning. Enter the date (column A). Then open
Etsy Shop Manager and Kit side by side. Enter cumulative totals in the source columns (C, E, H,
N). Formulas calculate the deltas automatically. Enter Status (R) and Notes (S). Time: 5 minutes.

**Weekly Analysis** — you will fill this every Sunday. The heavy formula work pulls from Daily
Dashboard. You only need to manually enter: Top Source (F), Top Guide (G), and Notes (R). Time:
10 minutes.

**Monthly Synthesis** — fill once on June 30. Go through each of the 23 rows in order. Most
values come directly from the last row of Daily Dashboard or from the Product Performance tab.
Time: 30 minutes.

**Cohort Tracking** — update whenever you notice a new acquisition pattern (a social post drove
a burst of signups, or a new buyer source appeared). Update at minimum every Sunday. Time:
5 minutes per update.

**Product Performance** — fill the baselines on May 29 (Step 4). Update on June 30. Optionally
spot-check the top 3 products mid-month. Time: 15 minutes on June 30.

**Acquisition ROI** — update weekly when you do Weekly Analysis. If you are not running paid
ads, this tab requires only 5 minutes per week. If paid ads are active, review this tab before
any budget decision.

**Decision Log** — pre-populate the four key checkpoint rows (listed in Section 2). Fill in
results and actions at the time of each checkpoint. Never wait to record a decision — document
it while the context is fresh.

---

## Section 6: Interpretation Guide

### What Each Daily Metric Means

**Etsy Orders Today**: The most important daily number. Target range Week 1: 1-3/day. Below 0
for 3 consecutive days triggers RED status.

**Revenue Today**: Directly tied to AOV and order volume. If revenue is flat but orders are
rising, someone is buying lower-priced items — investigate whether bundles are being seen.

**AOV Today**: Target $20+. If AOV drops below $15, single-guide purchases are dominant.
Consider adding a "frequently bought with" note in listing descriptions pointing to a second
guide.

**Conversion Rate (%)**: Orders / Views. Target 1.5%. Below 1.0% for 3 consecutive days means
the listing has a content or pricing problem, not a traffic problem. Do not increase social
posting to compensate — fix the listing.

**Refund Count**: Anything above 1 per 50 orders warrants investigation. Common cause: wrong
file delivered (wrong zone for the zone-card buyer). Check the most recent order's download
file manually.

**Kit Signups Today**: How many new subscribers joined the email list. This is your pre-purchase
pipeline. If this drops to 0 for 3+ days while Etsy views are normal, check that the Kit
landing page link in your listing descriptions is working.

**GA4 Sessions**: Contextual — helps explain spikes and troughs in Etsy data. A GA4 session
spike without an order spike means traffic quality is low (wrong audience clicking through).

**Bounce Rate**: GA4 measures this as sessions with no engagement event. High bounce (above
70%) on listing pages means the listing page is not matching visitor expectations. Check the
first listing image — it is doing the most work in attracting the right buyers.

### How to Spot Problems Early

**Pattern: Orders high, Revenue low**
- Cause: Lower-priced single guides are selling, bundles are not
- Action: Add bundle cross-sell language to the top-selling individual guide's description

**Pattern: Views high, Orders zero**
- Cause: The listing is appearing in search but not converting
- Action: Check the main listing image (is it clear and professional?), the title (does it
  match search intent?), and the price (is it within the normal range for this product type?)
- This is not a traffic problem. More social posts will not fix it.

**Pattern: Kit signups spiking, Etsy orders flat**
- Cause: Email list is growing but email-to-purchase conversion is low
- Action: Check that Email 5 (SEEDWARDEN15 coupon) is sending correctly. Verify the coupon
  code works on Etsy. Consider adding a limited-time urgency line to Email 4.

**Pattern: Conversion rate steady, Revenue declining**
- Cause: Fewer people are finding the listings (views are down)
- Action: Check Etsy search ranking by searching your primary keyword in incognito. If your
  listings dropped from page 1, update listing tags with 3-5 trending long-tail keywords.

**Pattern: AOV spike on a single day**
- Cause: One buyer purchased multiple guides in one order (bundle or multi-item cart)
- Action: Log the products in the Decision Log as a cross-sell win. Consider adding "bought
  together" language to both listings.

### When to Escalate (RED Status)

Immediately escalate (move to RED, investigate same day) if:
- 0 orders for 3 consecutive days while views are above 30/day
- Email open rate below 15% on 2 consecutive sends
- Kit signups = 0 for 24+ hours
- Any refund where the buyer reports receiving the wrong file
- Etsy listing shows as "inactive" (check Shop Manager > Listings > all statuses)

Do not escalate (YELLOW is fine) if:
- Orders are lower on weekends (expected — homesteader audience shops Sunday evening, peaks Tuesday-Thursday)
- Kit signups are flat for 2-3 days following a strong burst (normal — burst was from a single post)
- Pinterest monthly viewers are flat (14-day data lag; early numbers are always understated)

---

## Section 7: Decision Triggers

### Go/No-Go Thresholds Per Metric

These thresholds are set based on Phase 1 data (47 orders, $1,341 gross, 2.24% CVR) and adjusted
for Phase 2's expanded product catalog and email acquisition funnel.

**Daily thresholds** (from Section 6 status logic):

| Metric | GREEN | YELLOW | RED |
|---|---|---|---|
| Orders/day | 2+ | 1-1.9 | 0 for 3+ consecutive days |
| Revenue/day | $50+ | $30-$49 | Below $30 for 3+ consecutive days |
| AOV | $22+ | $16-$21 | Below $16 |
| Conversion rate (%) | 1.5%+ | 1.0-1.4% | Below 1.0% for 3+ days |
| Kit signups/day | 4+ | 2-3 | 0 for 3+ consecutive days |
| Refund rate (%) | Below 2% | 2-4% | Above 4% |

**Weekly thresholds**:

| Metric | GREEN | YELLOW | RED |
|---|---|---|---|
| Orders (week) | 14+ | 7-13 | Below 7 |
| Revenue (week) | $350+ | $175-$349 | Below $175 |
| Email open rate (%) | 35%+ | 25-34% | Below 25% |
| 7-day retention (%) | 25%+ | 15-24% | Below 15% |
| New Kit signups (week) | 15+ | 8-14 | Below 8 |

**Phase 3 expansion triggers** (all must fire on June 30 for Phase 3 Option B approval):
1. Cohort size: total unique sessions in June must exceed 500
2. Conversion rate trigger: top guide's CVR must exceed 8%
3. AOV trigger: average order value on 2-guide orders must exceed $45
4. Repeat rate trigger: 30-day repeat purchase rate must exceed 12%

If all four fire: Phase 3 Option B approved. Proceed with full expansion.
If 2-3 fire: Phase 3 Option A (conservative, 2-3 guides, reduced scope).
If 0-1 fire: Phase 3 deferred. Continue Phase 2 optimization.

### Launch Day Checkpoint Rules (May 30)

**Checkpoint 1 (12:05pm — T+5 minutes after Kit broadcast)**

Check these 4 signals. All 4 must be green:
- Kit broadcast shows "sent" status in Kit > Broadcasts
- Kit signups: 3+ new signups since 10:00am
- Etsy: at least 1 listing view has occurred today (any view)
- Your own: verify that the Kit landing page loads correctly in a browser

All 4 green = proceed normally to Checkpoint 2.
Any red = investigate that specific system immediately (do not wait for Checkpoint 2).

**Checkpoint 2 (9:00pm — end of Day 1)**

Record in Decision Log and Daily Dashboard:
- Kit signups total (≥12 total by end of day = GREEN)
- Email open rate (>25% = GREEN)
- Etsy orders (≥1 = GREEN; ≥5 = excellent)
- Social combined engagement (20+ likes/comments across IG + TikTok today = GREEN)

Decision rules:
- 4/4 metrics green: continue normally, run Week 1 plan
- 2-3 metrics green: elevated monitoring every 4 hours for 48 hours, no plan changes yet
- 1 or fewer metrics green: pause new social posts, diagnose root cause, check contingency playbook

### Phase 2 Mid-Point Check (June 15)

On June 15, pull Weekly Analysis Weeks 1-2 and evaluate:

| Criterion | Pass threshold | If failing |
|---|---|---|
| Orders pace (Jun 1-15) | 20+ total | Review listing SEO; consider Etsy Ads at $5/day |
| Email list growth | 80+ subscribers | Add CTA to Etsy thank-you message; post more zone card content |
| Top cohort identified | One cohort >35% of buyers | Review messaging mix |
| At least 1 star product | CVR above 2% | Prioritize that product in all social posts |

If 3/4 pass: on track, continue as planned.
If 2/4 pass: make targeted adjustments (listed in the "if failing" column above) and re-check June 22.
If 1/4 pass: activate contingency plan — open `LAUNCH_CONTINGENCY_PLAYBOOKS.md` and follow the
Phase 2 underperformance protocol.

### Phase 3 Final Gate (June 30)

Complete the Monthly Synthesis tab and count the score. Decision is automatic based on the score
formula in Tab 3 (Section 2 above).

Document the decision in Tab 7 (Decision Log). Whatever the outcome, record:
- Score achieved
- Top 3 metrics that passed cleanly
- Top 2 metrics that failed or came close
- Decision: Phase 3 Option B / Option A / Deferred
- Next action and target date

The June 30 analysis feeds directly into the Phase 3 planning session. If Phase 3 is approved,
the Phase 3 production timeline in `PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md` activates on
July 1. If deferred, the contingency protocol in `phase-2-contingency-playbook.md` takes over.

---

## Appendix A: Quick Launch Day Reference (May 30)

Print or screenshot this section for launch day use.

```
LAUNCH DAY CHECKLIST — MAY 30, 2026
================================
Before 10:00am:
  [ ] Open Google Sheet — Daily Dashboard — enter 05/30 in Row 3, Col A
  [ ] Verify Kit broadcast is scheduled for 12:00pm
  [ ] Check all Etsy listings show as Active in Shop Manager
  [ ] Confirm GA4 Realtime shows Seedwarden traffic

12:05pm — CHECKPOINT 1:
  [ ] Kit broadcast status = "Sent"
  [ ] Kit signups ≥ 3
  [ ] Etsy listings showing views
  [ ] Kit landing page loads correctly
  ALL 4 PASS → proceed | Any FAIL → investigate immediately

End of day (9:00pm) — CHECKPOINT 2:
  [ ] Record in Daily Dashboard (Row 3): all cumulative totals
  [ ] Record in Decision Log: Checkpoint 2 result
  Kit signups total:   ___ (target ≥12)
  Email open rate:     ___ (target >25%)
  Etsy orders:         ___ (target ≥1, excellent ≥5)
  Social engagement:   ___ (target 20+ combined)

4/4 targets = GREEN | 2-3 = YELLOW (monitor hourly tomorrow) | 1/4 = RED
```

---

## Appendix B: File References

All supporting documents referenced in this guide:

| File | Purpose |
|---|---|
| `PHASE_2_ANALYTICS_GOOGLE_SHEETS_TEMPLATE_SPEC.md` | Expanded column definitions with sample data |
| `PHASE_2_ANALYTICS_INFRASTRUCTURE_PRESTAGING.md` | Etsy OAuth scripts and Discord alert automation |
| `phase-2-analytics-strategy.md` | Cohort logic and decision trigger deep-dives |
| `etsy-ga4-event-tracking.md` | GA4 custom event taxonomy |
| `LOOKER_STUDIO_DASHBOARD_SPEC.md` | Optional Looker upgrade (trigger: 200+ orders/month) |
| `LAUNCH_CONTINGENCY_PLAYBOOKS.md` | What to do if metrics go RED on launch day |
| `PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md` | Phase 3 planning document (activated if Phase 3 approved Jun 30) |
| `customer-cohort-analysis-framework.md` | Full cohort definitions and messaging per segment |
| `analytics/etsy_ga4_kit_analytics_bridge.py` | Python automation script for daily data pulls |

---

*Version 1.0. Produced May 21, 2026. This document supersedes prior setup guides for the purpose of May 29-30 execution. All 23 Phase 3 trigger metrics and formulas are production-ready.*
