---
title: "Phase 2 Analytics and KPI Setup — May 9–30 and Post-Launch"
date: 2026-05-09
status: production-ready
scope: Analytics configuration steps, KPI tracking template, GA4 event setup, post-launch measurement framework
deadline: 2026-05-30
references:
  - TRACK_B_LAUNCH_DAY_OPERATIONS_GUIDE.md (7-metric KPI dashboard, checkpoint criteria)
  - phase-2-analytics-strategy.md (full analytics architecture)
  - phase-2-analytics-dashboard-template.csv (tracking spreadsheet)
  - google-analytics-integration-guide.md (GA4 setup reference)
  - etsy-ga4-event-tracking.md (Etsy-to-GA4 tracking)
  - phase-2-post-launch-analytics-framework.md (post-launch analysis)
---

# Phase 2 Analytics and KPI Setup
## Configuration Steps, Tracking Templates, and Post-Launch Measurement

**Prepared**: May 9, 2026
**Purpose**: Ensure analytics infrastructure is ready before May 30 launch so every metric
on launch day is attributable, comparable, and actionable. Setup that happens after launch
misses the baseline data that makes everything else meaningful.

---

## Part 1: Pre-Launch Setup (Complete Before May 25)

### 1.1 Google Analytics 4 — Confirm Configuration

**Check these before May 25:**

- [ ] GA4 property is active for Seedwarden (property ID recorded in WORKLOG.md)
- [ ] `utm_source`, `utm_medium`, `utm_campaign` parameters are tracked as default dimensions
- [ ] "Sessions by source/medium" report is accessible (Acquisition > Traffic Acquisition)

**Etsy limitation**: Etsy does not natively embed GA4 tracking scripts. All Etsy traffic in GA4
comes from UTM parameters appended to your Etsy store links in email and social posts.
Without UTMs, Etsy traffic appears as "direct" or "referral" — unattributable.

**UTM parameter standards for Phase 2** (use these exactly in all links):

| Source | Medium | Campaign | Example |
|---|---|---|---|
| Kit email — launch broadcast | `email` | `phase2-launch-broadcast` | `utm_source=kit&utm_medium=email&utm_campaign=phase2-launch-broadcast` |
| Kit email — zone card CTA | `email` | `phase2-launch-broadcast-zonecard` | `utm_source=kit&utm_medium=email&utm_campaign=phase2-launch-broadcast-zonecard` |
| Instagram bio link | `social` | `phase2-instagram-bio` | `utm_source=instagram&utm_medium=social&utm_campaign=phase2-instagram-bio` |
| TikTok bio link | `social` | `phase2-tiktok-bio` | `utm_source=tiktok&utm_medium=social&utm_campaign=phase2-tiktok-bio` |
| Pinterest bio link | `social` | `phase2-pinterest-bio` | `utm_source=pinterest&utm_medium=social&utm_campaign=phase2-pinterest-bio` |
| Pinterest pin — product | `social` | `phase2-pinterest-pin` | `utm_source=pinterest&utm_medium=social&utm_campaign=phase2-pinterest-pin` |

**Where to add UTMs**: Every link in every Kit email, every link in social bios, every link
in Pinterest pin descriptions. Not needed for organic Etsy (Etsy search traffic cannot carry UTMs).

---

### 1.2 Kit Analytics — Configure Before May 25

Kit provides native analytics for email sequences. Confirm these are visible in Kit dashboard:

- [ ] "Subscribers" counter on Kit home page (total + weekly growth)
- [ ] Automation analytics: open rate, click rate per email in the welcome sequence
- [ ] Broadcast analytics: delivery rate, open rate, click rate (will be used May 30)
- [ ] Tag analytics: subscriber count per tag (zone-3 through zone-10, seed-saver, city-grower, preservationist)

**Record these as baseline before May 30 launch broadcast sends:**
- Total confirmed subscribers at 11:59am May 30 (before broadcast opens)
- Zone distribution: how many subscribers per zone tag

This baseline is what you compare against post-launch Kit growth.

---

### 1.3 Etsy Analytics — Confirm Access

Etsy Shop Manager provides:
- Listing views per product
- Favorites per product
- Orders per listing
- Traffic sources (Search, Direct, Other — Etsy does not show external referrers)

**Record these as baseline on May 29 (the day before launch):**

Go to Etsy Shop Manager > Analytics > Listings. For each of the 21 Phase 2 products,
record the current view count. This establishes the "before Phase 2 launch" baseline.
Enter these numbers in `phase-2-analytics-dashboard-template.csv` under "Pre-launch baseline."

**Why this matters**: Without a pre-launch baseline, you cannot measure the lift Phase 2 creates.
A product with 140 views at launch and 155 views a week later gained 15 views — but only if
you recorded 140 as the baseline. Etsy does not provide historical snapshots retroactively.

---

### 1.4 Social Platform Analytics — Confirm Access

| Platform | Analytics Location | Key Metrics to Track |
|---|---|---|
| Instagram | Professional Dashboard > Insights | Reach, impressions, profile visits, follows gained |
| TikTok | Creator Dashboard > Analytics | Views, profile visits, follows, average watch time |
| Pinterest | Pinterest Analytics > Overview | Impressions, saves, link clicks, outbound clicks |

**Record follower count for all three platforms on May 29 at 11:59am.** This is the pre-launch
baseline. Compare against June 6 and June 30 counts.

---

## Part 2: Launch-Day KPI Tracking (May 30)

### 2.1 The 7 KPIs to Track Every 6 Hours

From `TRACK_B_LAUNCH_DAY_OPERATIONS_GUIDE.md` Part 2. Use this format to log each checkpoint:

**Tracking sheet template** (duplicate this row for each checkpoint):

```
Date/Time | Kit Signups | IG Engagement | TikTok Views | Pinterest Saves | Etsy Orders | Email Open Rate | Supplier Status
```

**Checkpoint times on May 30:**
- 9:00am (baseline before any traffic)
- 12:05pm (5 minutes after broadcast sends)
- 2:00pm (post-Instagram/TikTok)
- 6:00pm (mid-afternoon check)
- 9:00pm (Checkpoint 2 — major go/no-go decision)

**Checkpoint 1 (12:00pm) decision rule:**
- Kit submissions ≥3, Instagram ≥1 post live, TikTok ≥10 views, Etsy orders ≥0 → GREEN (proceed)
- Any metric = 0 → Contingency A (see Launch Day Guide)

**Checkpoint 2 (9:00pm — T+12h) decision rule:**
```
GREEN  (5+ of 7 metrics at target): proceed normally
YELLOW (3–4 metrics at target): escalated monitoring, 4h intervals
RED    (<3 metrics at target OR 0 orders): pause and investigate
```

Target values for T+12h:
- Kit signups: 12+
- Email opens: >25%
- Etsy orders: 5–12
- Social engagement (combined): 20+

---

### 2.2 Google Sheets Tracking Template

Create this spreadsheet on May 28 and bookmark it on both phone and desktop:

**Sheet 1: Launch Day Log**

| Column | Header | Notes |
|---|---|---|
| A | Timestamp | "9:00am May 30", "12:05pm May 30", etc. |
| B | Kit Signups (cumulative) | Kit Dashboard > Subscribers |
| C | Instagram Posts Live | Count of posts published |
| D | Instagram Engagement | Likes + comments total |
| E | TikTok Videos Live | Count of videos published |
| F | TikTok Views (cumulative) | All videos combined |
| G | Pinterest Pins Live | Count of pins posted |
| H | Pinterest Saves (cumulative) | All pins combined |
| I | Etsy Orders (cumulative) | Shop Manager > Orders |
| J | Etsy Revenue ($) | Order total cumulative |
| K | Email Open Rate (%) | Kit Broadcasts > launch broadcast |
| L | Email Click Rate (%) | Kit Broadcasts > launch broadcast |
| M | Supplier Confirmed | Yes/No/Pending |
| N | Notes | Any issues, anomalies, actions taken |

**Sheet 2: Baseline vs. Launch Comparison**

| Column | Header |
|---|---|
| A | Product name |
| B | Pre-launch views (May 29) |
| C | Week 1 views (June 6) |
| D | Week 1 favorites |
| E | Week 1 orders |
| F | Week 1 conversion rate |
| G | Revenue |
| H | Vs. Phase 1 baseline |

---

## Part 3: Post-Launch Measurement Framework (June 1–30)

### 3.1 Daily Metrics Log (5 minutes each morning)

Every morning through June 30, open your tracking sheet and fill in:

| Metric | Source | Decision Threshold |
|---|---|---|
| New Kit subscribers (yesterday) | Kit Dashboard | Below 5/day by Week 3 = social content issue |
| Email opens (yesterday's sequence sends) | Kit Analytics | Below 20% = subject line issue |
| Etsy orders (yesterday) | Etsy Shop Manager > Orders | 0 orders for 3+ consecutive days = investigate |
| Instagram followers (cumulative) | IG Insights | Weekly target: +50 by Week 2, +100 by Week 4 |
| TikTok followers (cumulative) | TikTok Analytics | Weekly target: +40 by Week 2, +80 by Week 4 |
| Pinterest monthly viewers | Pinterest Analytics | 2-week lag; check every 7 days |

**Escalation triggers (same-day action required):**
- Email open rate falls below 15% for 2 consecutive sends
- 0 Etsy orders after 100+ listing views (conversion problem)
- Kit landing page stops receiving submissions (bio link broken or page down)
- Any platform shows 0 new followers for 5 consecutive days despite posting

---

### 3.2 Weekly KPI Rollup (Sunday evenings through June 30)

Log these each Sunday in `WORKLOG.md`:

```
Week of [date]:
- Kit subscribers: [total] (added [N] this week)
- Top zone tag: [zone-N] ([count] subscribers)
- Etsy orders: [N] orders, $[revenue] revenue
- Top product: [product-slug] ([orders] orders)
- Email 3 click rate (seed-saver tag trigger): [%]
- Instagram followers: [total] (gained [N] this week)
- TikTok followers: [total] (gained [N] this week)
- Pinterest monthly viewers: [N]
- Decision: [GREEN / YELLOW / RED] + one sentence of rationale
```

---

### 3.3 Week 1 Success Targets (by June 6)

These are the minimum thresholds. Meeting all of them confirms Phase 2 launch is healthy:

| Metric | Target | Minimum Acceptable | Source |
|---|---|---|---|
| Kit subscriber count | 65+ | 50+ | Kit dashboard |
| Welcome email open rate | 40%+ | 30% | Kit Analytics — Email 1 |
| Email 3 click rate | 15%+ | 8% | Kit Analytics — primary high-intent signal |
| Etsy orders (Phase 2 attributable) | 4+ | 1+ | Etsy Shop Manager > Orders |
| Instagram followers | 150+ | 75+ | Instagram Insights |
| Pinterest monthly viewers | 2,000+ | 500+ | Pinterest Analytics |
| TikTok followers | 100+ | 40+ | TikTok Analytics |

**Attribution note**: "Phase 2 attributable" orders are any orders from May 30 onward. Etsy
does not separate Phase 1 and Phase 2 products — all orders count. Track which products are
ordered to understand whether Phase 2 catalog expansion drives net-new revenue or cannibalizes
Phase 1 products.

---

### 3.4 30-Day Conversion Analysis (June 30)

The June 30 analysis is the Phase 2→Phase 3 gate. Pull these numbers and compare to targets:

| Metric | Target | What It Measures |
|---|---|---|
| Kit subscriber count | 200+ | Social bio conversion rate + organic Kit discovery |
| Etsy listing conversion rate | 2%+ (from Phase 1 baseline) | Lifestyle image impact |
| Revenue from email sequence | ≥1 order per 10 subscribers | Email 5 coupon design validity |
| Instagram followers | 400+ | Organic social growth rate |
| Products with measurable CTR lift vs. Phase 1 | 5+ | Lifestyle image ROI validation |
| Phase 1→Phase 2 repeat purchase rate | 35%+ of Phase 1 buyers | Core cohort satisfaction signal |

**Decision framework**: If all 6 metrics hit target → Phase 3 Option B (Standard) is approved.
If 3–5 hit target → Phase 3 Option A (Conservative) or partial Phase 3. If fewer than 3 →
investigate before committing Phase 3 resources.

Full decision tree: `phase-3-decision-framework.md`.

---

### 3.5 What To Track In Customer-Analytics.csv

The `customer-analytics.csv` file is the long-term conversion tracking record. On each order:

| Field | What to Record | Source |
|---|---|---|
| order_date | YYYY-MM-DD | Etsy Shop Manager |
| product_slug | e.g., seed-saving-field-manual | Etsy listing |
| price | $ | Etsy order |
| buyer_type | phase1-repeat / phase2-new / unknown | Cross-reference with Phase 1 order history |
| traffic_source | kit-email / social-organic / etsy-search / direct | Etsy "How did they find you" + UTM |
| coupon_used | SEEDWARDEN15 / none | Etsy order details |
| zone_tag | zone-5 / etc. or unknown | Kit subscriber record if email purchaser |

This record is what powers the June 30 cohort analysis and the July 30 repeat-purchase check.

---

## Part 4: Analytics Gaps and What Requires User Action

These analytics configurations require platform logins — they cannot be pre-configured by the agent:

| Setup Step | Platform | Time | Deadline | Blocks |
|---|---|---|---|---|
| Create Google Sheets tracking template (Sheets 1 and 2) | Google Sheets | 20 min | May 28 | Launch-day monitoring |
| Connect GA4 to Kit landing page (Kit > Settings > Integrations > GA4) | Kit | 15 min | May 25 | Cross-platform attribution |
| Verify UTM parameters are landing in GA4 (send test click, check Realtime report) | GA4 | 10 min | May 25 | Confirms tracking is working |
| Record May 29 baseline: all 21 Etsy listing view counts | Etsy | 30 min | May 29 | Attribution baseline |
| Record May 29 baseline: follower counts on all 3 platforms | Instagram/TikTok/Pinterest | 5 min | May 29 | Growth measurement |
| Record May 29 baseline: Kit subscriber count and zone distribution | Kit | 5 min | May 29 | Email list growth measurement |
| Create launch-day tracking folder for screenshots | Google Drive or local | 5 min | May 29 | Backup if dashboard has latency |

---

*Prepared: 2026-05-09. Analytics must be configured before May 25 — not May 29. Any setup that
happens after launch misses the baseline that makes post-launch comparison valid. See
`phase-2-analytics-strategy.md` for the full 90-day analytics architecture.*
