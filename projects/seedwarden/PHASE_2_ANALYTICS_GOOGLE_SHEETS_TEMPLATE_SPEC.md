---
title: Phase 2 Analytics Google Sheets Template — Detailed Specifications
status: production-ready
date: 2026-05-15
scope: Complete sheet layouts, column definitions, formulas, and data-entry instructions
---

# Phase 2 Analytics Google Sheets Template Specifications

This document specifies the exact layout, formulas, and data-entry instructions for all 7 sheets in your tracking spreadsheet.

**File name**: `Seedwarden Phase 2 Analytics — May 30–June 30`

**Location**: Save to Google Drive and share with yourself for phone access.

---

## Sheet 1: Daily Dashboard

**Purpose**: Single daily snapshot capturing all key metrics (5 minutes to fill each morning).

**Structure**: Each row represents one day (May 30 — June 30).

### Column Definitions

| Column | Header | Source | Formula/Instructions |
|---|---|---|---|
| A | Date | Manual | Enter as MM/DD (e.g., 05/30) |
| B | Day of Week | Formula | `=TEXT(DATE(2026,5,30),"dddd")` |
| C | Kit Signups (cumulative) | Kit Dashboard | Go to Kit home > Subscribers counter. Enter the total number shown. |
| D | Kit Signups (new today) | Formula | `=C2-C1` (difference from yesterday) |
| E | Etsy Total Orders (cumulative) | Etsy Shop Manager | Go to Orders, filter by "May 30 onward", count total orders. |
| F | Etsy New Orders (today) | Formula | `=E2-E1` |
| G | Etsy Revenue (cumulative $) | Etsy Shop Manager | Filter orders, sum order totals. |
| H | Etsy Revenue (today $) | Formula | `=G2-G1` |
| I | Avg Order Value (today $) | Formula | `=IF(F2=0,0,H2/F2)` |
| J | Email Open Rate (%) | Kit Emails tab | Go to Kit > Emails > launch broadcast. Enter % shown (e.g., 35 for 35%) |
| K | Email Click Rate (%) | Kit Emails tab | Same as J, click rate instead of open rate |
| L | IG Followers (cumulative) | Instagram Insights | Check profile or Insights > Followers. Enter total. |
| M | IG Followers (new today) | Formula | `=L2-L1` |
| N | IG Engagement (today) | Manual | Likes + comments on all IG posts published that day. Sum them. |
| O | TikTok Followers (cumulative) | TikTok Analytics | Check Creator Center > Analytics > Followers. Enter total. |
| P | TikTok Followers (new today) | Formula | `=O2-O1` |
| Q | TikTok Views (cumulative) | TikTok Analytics | Check Analytics > Overview > Video Views. Enter total (all-time, not just today). |
| R | TikTok Views (new today) | Formula | `=Q2-Q1` |
| S | Pinterest Followers (cumulative) | Pinterest Analytics | Check Analytics > Overview > Followers. Enter total. |
| T | Pinterest Followers (new today) | Formula | `=S2-S1` |
| U | Pinterest Monthly Viewers | Pinterest Analytics | Check Analytics > Overview > Monthly Viewers (updates with 14-day lag). |
| V | Decision Status | Manual | GREEN / YELLOW / RED (see Launch-Day Checkpoints in Setup Guide) |
| W | Notes | Manual | Any issues, anomalies, or actions taken (optional). |

### Sample Data (May 30–June 2)

```
Date | DoW | Kit Cumul | Kit New | Etsy Cumul | Etsy New | Revenue $ | Revenue Today | AOV | Email Open | Email Click | IG Foll | IG New | IG Engage | TikTok Foll | TikTok New | TikTok Views | TikTok Today | PIN Foll | PIN New | PIN Monthly | Status | Notes
05/30 | Fri | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 120 | 0 | 0 | 85 | 0 | 0 | 0 | 450 | 0 | — | — | Pre-launch baseline
05/30 | Fri | 8 | 8 | 2 | 2 | 47.50 | 47.50 | 23.75 | 28 | 4 | 122 | 2 | 12 | 87 | 2 | 145 | 145 | 455 | 5 | — | GREEN | Checkpoint 1 passed
05/31 | Sat | 12 | 4 | 4 | 2 | 95.00 | 47.50 | 23.75 | 32 | 6 | 125 | 3 | 8 | 91 | 4 | 289 | 144 | 460 | 5 | — | GREEN | Steady growth
06/01 | Sun | 15 | 3 | 5 | 1 | 120.50 | 25.50 | 25.50 | 35 | 7 | 128 | 3 | 5 | 95 | 4 | 412 | 123 | 465 | 5 | — | YELLOW | Lower Sat-Sun engagement expected
06/02 | Mon | 18 | 3 | 7 | 2 | 170.25 | 49.75 | 24.88 | 38 | 8 | 131 | 3 | 10 | 99 | 4 | 521 | 109 | 470 | 5 | — | GREEN | Recovery Monday
```

---

## Sheet 2: Weekly Rollup

**Purpose**: Aggregate daily data into weekly summaries for pattern recognition.

**Structure**: One row per week (Week 1 = May 30–Jun 6, Week 2 = Jun 7–13, etc.).

### Column Definitions

| Column | Header | Data Source | Formula/Instructions |
|---|---|---|---|
| A | Week | Manual | "Week 1 (May 30–Jun 6)" |
| B | Kit Subscribers (end of week) | Daily Dashboard | Value from Friday of that week in Daily Dashboard, column C |
| C | Kit Weekly Gain | Formula | `=(B2-B1)` or refer to Daily Dashboard |
| D | Top Zone Tag | Manual | Review Kit > Automation > Subscribers > Tags. Enter which zone-X has most subscribers. |
| E | Top Zone Subscriber Count | Manual | Count of subscribers in that zone. |
| F | Etsy Orders (week total) | Daily Dashboard | `=SUM(Daily!F2:F8)` (sum of new orders that week) |
| G | Etsy Revenue (week total $) | Daily Dashboard | `=SUM(Daily!H2:H8)` (sum of daily revenue that week) |
| H | Avg Order Value (weekly) | Formula | `=IF(F2=0,0,G2/F2)` |
| I | Top Product (this week) | Manual | Check Etsy Shop Manager > Listings > "orders" column. Enter which product had most orders. |
| J | Top Product Orders | Manual | Order count for that product. |
| K | Email 3 Click Rate (avg) | Manual | Kit > Emails > [Email 3]. Enter average % click rate for that week. |
| L | IG Followers (start of week) | Daily Dashboard | Value from Friday of previous week |
| M | IG Followers (end of week) | Daily Dashboard | Value from Friday of this week |
| N | IG Followers Gained | Formula | `=M2-L2` |
| O | TikTok Followers (start) | Daily Dashboard | Value from Friday of previous week |
| P | TikTok Followers (end) | Daily Dashboard | Value from Friday of this week |
| Q | TikTok Followers Gained | Formula | `=P2-O2` |
| R | Pinterest Monthly Viewers | Daily Dashboard | Value from Friday of this week (note: 14-day lag) |
| S | Week Status | Manual | GREEN / YELLOW / RED (all daily statuses GREEN = week GREEN; mix = YELLOW, etc.) |
| T | Decision | Manual | Text summary. E.g., "Strong launch week, email engagement above target" |

### Sample Data

```
Week | Kit Sub (EOW) | Kit Gain | Top Zone | Top Zone Count | Etsy Orders | Etsy Revenue | AOV | Top Product | Top Orders | Email3 Click | IG Start | IG End | IG Gain | TikTok Start | TikTok End | TikTok Gain | Pinterest Viewers | Status | Decision
Week 1 (May 30–Jun 6) | 65 | 65 | zone-5 | 18 | 12 | 285.50 | 23.79 | Herb Garden | 3 | 12 | 120 | 145 | 25 | 85 | 110 | 25 | 1200 | GREEN | Launch week exceeded all targets. Zone-5 (urban apartment gardeners) is primary cohort.
Week 2 (Jun 7–13) | 95 | 30 | zone-5 | 28 | 18 | 432.75 | 24.04 | Seed Saving | 4 | 14 | 145 | 170 | 25 | 110 | 138 | 28 | 2150 | GREEN | Momentum sustained. Seed Saving product emerging as secondary top performer.
Week 3 (Jun 14–20) | 118 | 23 | zone-5 | 35 | 22 | 525.50 | 23.89 | Preservation Tech | 5 | 16 | 170 | 195 | 25 | 138 | 162 | 24 | 3100 | YELLOW | Subscriber growth slowing slightly. Email engagement still strong. Consider content boost midweek.
Week 4 (Jun 21–27) | 150 | 32 | zone-6 | 42 | 25 | 597.00 | 23.88 | Seed Saving | 6 | 17 | 195 | 225 | 30 | 162 | 190 | 28 | 4200 | GREEN | Content boost worked. Zone-6 (suburban) gaining. Consistent product mix.
```

---

## Sheet 3: Monthly Synthesis

**Purpose**: Complete June 30 analysis for Phase 2→Phase 3 gate decision.

**Structure**: Single row (all data, 1 day — June 30). This is your go/no-go scorecard.

### Column Definitions & Success Targets

| Metric | Target | Measurement | Decision Threshold | Formula/Source |
|---|---|---|---|---|
| **KPI 1: Kit Subscriber Growth** | 200+ total | Kit Dashboard > Subscribers | ≥200: +5 pts | `=Value from Daily Dashboard, June 30` |
| **KPI 2: Email Revenue per Subscriber** | $0.10+ per sub | Cumulative Etsy revenue / Kit subscriber count | Email $ ÷ Kit subs ≥ $0.10: +5 pts | `=G[June 30] / C[June 30]` (Daily Dashboard columns) |
| **KPI 3: Etsy Listing Conversion Rate** | 2%+ | (Total Etsy orders) ÷ (Total listing views from Etsy analytics) × 100 | ≥2%: +5 pts | Manual calculation: divide total May 30–Jun 30 orders by total views in Etsy Analytics |
| **KPI 4: Instagram Follower Growth** | 400+ total | Instagram Insights > Followers | ≥400: +5 pts | Check Instagram Insights on June 30 |
| **KPI 5: Products with CTR Lift vs Phase 1** | 5+ products | Etsy Analytics > Listings > Order count for each product | ≥5 products with orders: +5 pts | Review Etsy listings; count how many have June orders |
| **KPI 6: Phase 1 Repeat Purchase Rate** | 35%+ of Phase 1 buyers | Cross-reference Phase 1 buyer emails with June orders | ≥35%: +5 pts | Manual: check Etsy orders; identify repeat customers from Phase 1 |
| **KPI 7: Social Engagement Velocity** | Consistent growth | Avg daily follower gain across IG + TikTok | ≥3/day combined: +5 pts | `=(IG Week 4 gain + TikTok Week 4 gain) ÷ 7 days` |

### Decision Scorecard (June 30)

| KPI | Target | June 30 Result | Pass? (Y/N) | Points |
|---|---|---|---|---|
| Kit subscribers | 200+ | [N] | Y/N | +5 / 0 |
| Email revenue/sub | $0.10+ | $[N] | Y/N | +5 / 0 |
| Etsy listing conversion | 2%+ | [%] | Y/N | +5 / 0 |
| Instagram followers | 400+ | [N] | Y/N | +5 / 0 |
| Products with orders | 5+ | [N] | Y/N | +5 / 0 |
| Repeat purchase rate | 35%+ | [%] | Y/N | +5 / 0 |
| Social velocity | 3+/day | [N]/day | Y/N | +5 / 0 |
| **TOTAL SCORE** | — | **[SCORE]/35** | — | — |

### Phase 2→Phase 3 Gate Decision

**Score ≥30 (6/7 KPIs pass)**: **PHASE 3 OPTION B APPROVED**
- Green light for full premium tier launch (Sep 2026)
- Proceed with Phase 3 product development + affiliate program
- Budget: 40 hours professional content + 10 hours affiliate setup

**Score 25–29 (5/7 KPIs pass)**: **PHASE 3 OPTION A APPROVED** (Conservative)
- Proceed with premium tier but reduce scope (2–3 products instead of 5)
- Budget: 20 hours product development + 5 hours affiliate setup
- Revisit full Phase 3 in Dec 2026 if Phase 2 growth accelerates

**Score <25 (≤4/7 KPIs pass)**: **PHASE 3 DEFERRED**
- Continue Phase 2 optimization (3–6 additional months)
- Investigate underperforming channels (which KPI failed?)
- Reconvene in Sep 2026 for Phase 3 decision

---

## Sheet 4: Cohort Tracking

**Purpose**: Build repeatable customer profiles and measure Phase 1→Phase 2 repeat purchase rate.

**Structure**: One row per customer cohort (usually one row = one Kit signup day or source).

### Column Definitions

| Column | Header | Data Source | Formula/Instructions |
|---|---|---|---|
| A | Cohort Start Date | Manual | Date when cohort started (e.g., May 30, May 31, Jun 1) |
| B | Cohort Source | Manual | "Kit Email", "Instagram", "TikTok", "Pinterest", "Etsy Search", or "Direct" |
| C | Initial Cohort Size | Manual | Number of Kit signups from that source on that date |
| D | Phase 1 Repeat Buyer? | Manual | Y/N (are these people Phase 1 buyers?) |
| E | Orders in Week 1 | Manual | How many purchases did this cohort make by Week 1 (Jun 6)? |
| F | Revenue in Week 1 | Manual | Total $ from Week 1 orders from this cohort |
| G | Avg Order Value (Cohort) | Formula | `=F2/E2` (if E2>0, else blank) |
| H | Orders by Month End | Manual | Total purchases by June 30 |
| I | Revenue by Month End | Manual | Total $ by June 30 |
| J | Lifetime LTV (estimate) | Formula | `=I2` (assumes June 30 end; adjust if you do Jul/Aug tracking) |
| K | Top Product Purchased | Manual | Which product did this cohort buy most? |
| L | Notes | Manual | E.g., "Zone-5 urban cohort showing strong repeat purchase", etc. |

### Sample Data

```
Cohort Date | Cohort Source | Initial Size | Phase 1 Repeat? | Week 1 Orders | Week 1 Revenue | AOV | Month-End Orders | Month-End Revenue | LTV | Top Product | Notes
05/30 | Kit Email | 8 | Y(5) N(3) | 2 | 47.50 | 23.75 | 4 | 95.00 | 95.00 | Herb Garden | Phase 1 buyers converting well. New buyers slower.
05/31 | Instagram | 4 | N | 1 | 23.50 | 23.50 | 3 | 70.50 | 70.50 | Seed Saving | Strong Instagram→Seed Saving connection. High intent.
06/01 | TikTok | 3 | N | 0 | 0 | — | 1 | 24.99 | 24.99 | Preservation Tech | Lower conversion, but strong engagement. Younger cohort profile.
```

---

## Sheet 5: Product Performance

**Purpose**: Identify star performers and underperformers for Phase 3 decisions.

**Structure**: One row per product.

### Column Definitions

| Column | Header | Data Source | Formula/Instructions |
|---|---|---|---|
| A | Product Name | Etsy Listings | Copy exact name from Etsy |
| B | Launch Tier | Manual | "Phase 1" or "Phase 2" |
| C | Pre-Launch Views (May 29) | Etsy | From baseline recording on May 29 |
| D | Month-End Views (Jun 30) | Etsy Analytics | Go to Listings, check view count on June 30 |
| E | Views Gained | Formula | `=D2-C2` |
| F | Pre-Launch Favorites (May 29) | Etsy | From May 29 baseline |
| G | Month-End Favorites (Jun 30) | Etsy Analytics | Check Listings, favorite count on June 30 |
| H | Favorites Gained | Formula | `=G2-F2` |
| I | Orders (May 30–Jun 30) | Etsy Shop Manager | Filter orders, count by product |
| J | Revenue (total) | Etsy Shop Manager | Sum order totals for this product |
| K | Conversion Rate | Formula | `=I2/D2*100` (Orders ÷ Views × 100) |
| L | Price | Etsy Listings | Current price (e.g., $14.99) |
| M | Stars (1–5) | Manual | 5⭐ = star product (top 3 orders), 3⭐ = average, 1⭐ = underperformer |
| N | Phase 3 Status | Manual | "Expand", "Maintain", "Archive", or "Investigate" |
| O | Notes | Manual | E.g., "Phase 1 product performing, no lift from Phase 2", etc. |

### Sample Data

```
Product | Phase | Views (Start) | Views (End) | Views Gained | Favs (Start) | Favs (End) | Favs Gained | Orders | Revenue | Conv Rate | Price | Stars | Phase 3 | Notes
Herb Garden Guide | Phase 1 | 120 | 185 | 65 | 8 | 14 | 6 | 5 | 74.95 | 2.7% | 14.99 | 5⭐ | Expand | Strong Phase 2 lift. Top performer. Expand to deluxe version.
Seed Saving Manual | Phase 2 | 0 | 142 | 142 | 0 | 12 | 12 | 4 | 59.96 | 2.8% | 14.99 | 5⭐ | Expand | Immediate traction. Fast conversion. Phase 2 success.
Preservation Tech | Phase 2 | 0 | 98 | 98 | 0 | 7 | 7 | 3 | 44.97 | 3.1% | 14.99 | 5⭐ | Maintain | Small audience, high conversion. Keep in catalog.
Drying Techniques | Phase 1 | 95 | 118 | 23 | 6 | 8 | 2 | 1 | 14.99 | 0.8% | 14.99 | 1⭐ | Investigate | Low conversion despite Phase 2 promotion. Check description/photos.
```

---

## Sheet 6: Acquisition ROI

**Purpose**: Calculate cost-per-acquisition by channel (email, social, organic).

**Structure**: One row per acquisition channel.

**Note**: This sheet assumes you have cost data. If you're not tracking ad spend, focus on organic (email + social) instead.

### Column Definitions

| Column | Header | Data Source / Formula | Instructions |
|---|---|---|---|
| A | Channel | Manual | "Kit Email", "Instagram Ads", "TikTok Organic", "Pinterest Organic", "Etsy Search", "Direct" |
| B | Cohort Size (Signups) | Daily Dashboard | How many Kit signups from this channel over May 30–Jun 30? |
| C | Orders from Channel | Manual | How many Etsy orders came from this source? (Check Etsy "How did they find you?") |
| D | Revenue from Channel ($) | Manual | Total revenue from orders from this channel |
| E | Cost (if applicable) | Manual | Ad spend if you're running paid ads. Organic channels: enter 0. |
| F | Cost per Signup | Formula | `=E2/B2` (if B2>0, else blank) |
| G | Cost per Order | Formula | `=E2/C2` (if C2>0, else blank) |
| H | LTV (Revenue per Customer) | Formula | `=D2/C2` (if C2>0, else blank) |
| I | ROI | Formula | `=((D2-E2)/E2)*100` (if E2>0, else "organic") |
| J | Channel Status | Manual | "Scale", "Optimize", "Pause", or "Monitor" |

### Sample Data

```
Channel | Signups | Orders | Revenue | Cost | Cost/Signup | Cost/Order | LTV | ROI | Status
Kit Email (Organic) | 65 | 22 | 330.68 | 0 | 0.00 | 0.00 | 15.03 | Organic | Scale
Instagram Organic | 18 | 6 | 89.94 | 0 | 0.00 | 0.00 | 14.99 | Organic | Optimize (low conversion)
TikTok Organic | 12 | 3 | 44.97 | 0 | 0.00 | 0.00 | 14.99 | Organic | Monitor (new cohort)
Pinterest Organic | 8 | 2 | 29.98 | 0 | 0.00 | 0.00 | 14.99 | Organic | Monitor
Etsy Search | 0 | 8 | 119.92 | 0 | — | 0.00 | 14.99 | Organic | Scale (no signup required, direct discovery)
Instagram Ads (if added) | — | — | — | 150.00 | — | — | — | — | TBD
```

---

## Sheet 7: Go/No-Go Decision Log

**Purpose**: Track every major decision (go/no-go checkpoints, deployment gates, contingencies) with date and rationale.

**Structure**: Chronological log of decisions.

### Column Definitions

| Column | Header | Notes |
|---|---|---|
| A | Date | Decision date (e.g., 05/30) |
| B | Time | Time of decision (e.g., 12:05pm) |
| C | Decision | Gate name (e.g., "Checkpoint 1", "Week 1 Go/No-Go", "Phase 3 Gate") |
| D | Decision Type | GO / NO-GO / ESCALATE / CONTINGENCY |
| E | Primary Metric | Which metric drove the decision? (e.g., "Kit Signups", "Email Open Rate") |
| F | Metric Value | Value of that metric (e.g., 8, 28%, 5 orders) |
| G | Target | What was the target? (e.g., "≥3", ">25%", "≥4") |
| H | Status | PASS / FAIL / WATCH |
| I | Action Taken | What did you do as a result? (e.g., "Continued normal schedule", "Activated Contingency A", "Paused social posting for 2h") |
| J | Outcome (Recorded Later) | How did the action work out? (recorded 1–7 days later) |

### Sample Data

```
Date | Time | Decision | Type | Primary Metric | Value | Target | Status | Action | Outcome (Later)
05/30 | 12:05pm | Checkpoint 1 | GO | Kit Signups | 8 | ≥3 | PASS | Proceed with Checkpoint 2 | ✓ Checkpoint 1 goal exceeded
05/30 | 09:00pm | Checkpoint 2 | GO | Etsy Orders | 2 | ≥1 | PASS | Continue normal schedule | ✓ Orders exceeded 5 by week-end
06/06 | 10:00am | Week 1 Go/No-Go | GO | All 7 KPIs | 6/7 | 5/7 | PASS | Proceed to Week 2 normally | ✓ Week 2 momentum sustained
06/30 | 06:00pm | Phase 3 Gate | GO | Score | 32/35 | 30/35 | PASS | Approve Phase 3 Option B | ✓ Phase 3 development begins July 1
```

---

## How to Use These Sheets Together

### Daily Workflow (5 minutes per day)

1. **Open Daily Dashboard**
2. **Enter date** (column A)
3. **Collect metrics** from Kit, Etsy, Instagram, TikTok, Pinterest
4. **Fill columns B–U** (most have formulas; you only enter the source data)
5. **Record decision** in column V (GREEN / YELLOW / RED)
6. **Repeat next day**

### Weekly Workflow (10 minutes on Sunday)

1. **Open Weekly Rollup sheet**
2. **Enter week dates** (column A)
3. **Formulas auto-pull** data from Daily Dashboard (do NOT re-enter)
4. **Manually add context** (Top Zone, Top Product, Notes)
5. **Log to WORKLOG.md** with summary

### June 30 Workflow (30 minutes, end of month)

1. **Open Monthly Synthesis sheet**
2. **Pull each of the 7 KPI values** from Daily Dashboard (June 30 row) and external sources
3. **Fill the Decision Scorecard**
4. **Formulas calculate total score**
5. **Read the decision** at the bottom (APPROVED / DEFERRED)
6. **Document in CHECKIN.md** for next session planning

---

## Formulas Quick Reference

If you want to set up formulas yourself, here are the most useful ones:

### Daily Dashboard Formulas

```
Cumulative-to-Daily (new items today):
=C2-C1  (if C2 is cumulative, C1 is yesterday's cumulative, then C2-C1 = today's new)

Average Order Value:
=IF(F2=0, 0, H2/F2)  (Revenue ÷ Orders; if 0 orders, show 0)
```

### Weekly Rollup Formulas

```
Sum daily data into weekly totals:
=SUM(Daily!F2:F8)  (sum column F rows 2–8 from Daily Dashboard sheet)

Calculate growth:
=M2-L2  (end of week minus start of week)
```

### Cohort Tracking Formulas

```
LTV (Lifetime Value):
=I2  (revenue by month end)

Repeat Purchase Rate:
=(COUNT of Phase 1 buyers who also bought in Jun) / (Total Phase 1 buyers) * 100
```

---

## Best Practices

1. **Fill source metrics only** — let formulas calculate derived metrics (don't manually enter totals)
2. **Record May 29 baseline** — before any traffic, so you can measure lift
3. **Check daily by 10:00am** — capture metrics while fresh
4. **Escalate immediately** — if any metric hits a red flag (email open rate <15%, 0 orders for 24h, etc.), act same day
5. **Review weekly** — every Sunday, spend 10 min on Weekly Rollup to spot trends
6. **Decide by June 30** — use Monthly Synthesis scorecard, not gut feeling

---

## Common Data Entry Mistakes

**❌ Don't**: Manually sum rows (e.g., enter "12" in "Total Orders")
**✓ Do**: Let formulas calculate (=SUM(F2:F8))

**❌ Don't**: Estimate metrics ("about 50 followers")
**✓ Do**: Copy exact numbers from source (Instagram Insights shows 47, enter 47)

**❌ Don't**: Skip May 29 baseline
**✓ Do**: Spend 30 min on May 29 recording all starting numbers

**❌ Don't**: Wait until month-end to record baselines
**✓ Do**: Record each day so you can see trends

---

## Next Steps

1. **Create this spreadsheet on Google Drive** (File > New > Spreadsheet)
2. **Create the 7 sheet tabs** (right-click sheet tabs to add)
3. **Add column headers** (copy from this document)
4. **Add formulas** (use Quick Reference above, or leave blank if formulas are unfamiliar)
5. **Share with yourself** (File > Share > your email)
6. **Bookmark on phone** (for launch-day accessibility)
7. **Do May 29 baseline recording** (save 30 min that day)
8. **Launch May 30** (start Daily Dashboard entries at 10:00am)

---

**Questions?** See `PHASE_2_ANALYTICS_SETUP_GUIDE.md` for walkthrough. See `phase-2-analytics-kpi-setup.md` for KPI definitions.
