---
title: Looker Studio Dashboard Specification — Optional Advanced Analytics
status: production-ready
date: 2026-05-15
scope: Complete dashboard layout for real-time analytics visualization
trigger: Activate if tracking exceeds 200 orders/month (Phase 2 success milestone)
---

# Looker Studio Dashboard Specification

**What is Looker Studio?** Free Google tool for data visualization. Replaces manual Google Sheets with auto-updating dashboards connected to GA4, Etsy, and Kit APIs.

**When to use this?** Optional. Use if you want live dashboards during May 30–June 30. If manual Google Sheets work fine, skip this and stick with Sheets.

**Setup time**: 60–90 minutes (one-time, then fully automated)

---

## Dashboard Overview

You'll create **1 master dashboard with 4 tabs**:

1. **Live Metrics** — Real-time counters (Kit subscribers, Etsy orders, email opens)
2. **Traffic Sources** — GA4 data (which channels drive traffic)
3. **Product Performance** — Which products convert best
4. **Week-over-Week Trends** — Growth velocity and decision gates

---

## Tab 1: Live Metrics

**Purpose**: Glanceable dashboard for daily decision-making (Checkpoints 1 & 2).

### Layout

```
┌─────────────────────────────────────────────────────────────┐
│                   PHASE 2 LAUNCH — LIVE STATUS              │
│                                                              │
│ ┌─────────────┐  ┌──────────────┐  ┌─────────────┐         │
│ │ Kit Subs    │  │ Etsy Orders  │  │ Etsy Revenue│         │
│ │     12      │  │      2       │  │   $47.50    │         │
│ │ (+12 today) │  │ (+2 today)   │  │ (+$47 today)│         │
│ └─────────────┘  └──────────────┘  └─────────────┘         │
│                                                              │
│ ┌─────────────┐  ┌──────────────┐  ┌─────────────┐         │
│ │ Email Open  │  │ Email Click  │  │ Status      │         │
│ │    28%      │  │      4%      │  │   GREEN     │         │
│ │  (today)    │  │  (today)     │  │ (all metrics│         │
│ └─────────────┘  └──────────────┘  └─────────────┘         │
│                                       passing)              │
│                                                              │
│ DECISION GATE: Checkpoint 1 PASS (12:05pm)                 │
│ Next checkpoint: 9:00pm (Checkpoint 2)                     │
└─────────────────────────────────────────────────────────────┘
```

### Data Source Connections

**Scorecard 1: Kit Signups**
- Data source: Kit API (manual export to sheet, then import)
- Metric: SUM of all Kit form submissions
- Dimension: Date
- Default date range: May 30–Jun 30
- Update frequency: 6-hour manual or real-time if Kit webhook available

**Scorecard 2: Etsy Orders**
- Data source: Etsy API (via Google Sheets CSV export)
- Metric: COUNT of unique orders
- Dimension: Date
- Filter: "Date >= May 30"
- Update frequency: 12-hour manual (check Etsy Shop Manager)

**Scorecard 3: Revenue**
- Data source: Etsy CSV (same as orders)
- Metric: SUM of order totals
- Dimension: Date

**Scorecard 4: Email Open Rate**
- Data source: Kit API / Google Sheets
- Metric: (Open count / Send count) × 100
- Dimension: Email broadcast name
- Update frequency: 2-hour (manual from Kit dashboard)

**Scorecard 5: Email Click Rate**
- Data source: Kit API
- Metric: (Click count / Send count) × 100

**Scorecard 6: Status Indicator**
- Data source: Formula in Google Sheet
- Metric: IF logic gate (see Weekly Rollup in Sheets Spec for logic)
- Logic: ≥5 of 7 metrics at target = GREEN; 3–4 = YELLOW; <3 = RED

---

## Tab 2: Traffic Sources (GA4)

**Purpose**: Understand which channels drive Kit signups, Etsy traffic, and revenue.

### Layout

```
┌──────────────────────────────────────────────────┐
│          TRAFFIC SOURCES — MAY 30–JUN 30        │
│                                                 │
│ ┌──────────────────────────────────────────────┐│
│ │ Sessions by Source/Medium (Pie Chart)        ││
│ │                                              ││
│ │    Kit Email (45%)  ▓▓▓▓▓▓▓                 ││
│ │    Instagram (20%)  ▓▓▓                     ││
│ │    TikTok (18%)     ▓▓▓                     ││
│ │    Etsy Search (10%)▓▓                      ││
│ │    Pinterest (5%)   ▓                       ││
│ │    Direct (2%)      ▓                       ││
│ └──────────────────────────────────────────────┘│
│                                                 │
│ ┌──────────────────────────────────────────────┐│
│ │ Conversions by Source (Table)                ││
│ │                                              ││
│ │ Source       │ Sessions │ Conversions │ Rate ││
│ │ Kit Email    │  127     │     8      │ 6.3% ││
│ │ Instagram    │   45     │     2      │ 4.4% ││
│ │ TikTok       │   38     │     1      │ 2.6% ││
│ │ Pinterest    │   12     │     0      │ 0.0% ││
│ └──────────────────────────────────────────────┘│
└──────────────────────────────────────────────────┘
```

### Data Source

- **Data source**: Google Analytics 4
- **Dimensions**: utm_source, utm_medium
- **Metrics**: Sessions, Conversions, Conversion Rate
- **Date range**: May 30–Jun 30 (adjustable)
- **Required setup**: GA4 property linked to Looker Studio (Admin > Linked sources > GA4)

### Connection Steps

1. **Open Looker Studio**: https://lookerstudio.google.com
2. **Create new report** > Connect to GA4
3. **Select your Seedwarden GA4 property**
4. **Add chart**: Pie chart
   - Dimension: utm_source
   - Metric: Sessions
   - Sort by Sessions descending
5. **Add table**: Comparison table
   - Dimensions: utm_source, utm_medium
   - Metrics: Sessions, Conversions, Conversion Rate
   - Sort by Conversions descending

---

## Tab 3: Product Performance

**Purpose**: Track which Phase 2 products drive the most revenue and conversions.

### Layout

```
┌──────────────────────────────────────────────────┐
│         PRODUCT PERFORMANCE — MAY 30–JUN 30     │
│                                                 │
│ ┌──────────────────────────────────────────────┐│
│ │ Orders by Product (Horizontal Bar Chart)     ││
│ │                                              ││
│ │ Herb Garden         ▓▓▓▓▓ 5 orders          ││
│ │ Seed Saving Manual  ▓▓▓▓ 4 orders           ││
│ │ Preservation Tech   ▓▓▓ 3 orders            ││
│ │ Drying Techniques   ▓ 1 order               ││
│ │ Root Cellaring      ▓ 1 order               ││
│ └──────────────────────────────────────────────┘│
│                                                 │
│ ┌──────────────────────────────────────────────┐│
│ │ Revenue & Conversion by Product (Table)      ││
│ │                                              ││
│ │ Product            │ Views │ Orders │ Conv % ││
│ │ Herb Garden        │ 65    │ 5      │ 7.7%  ││
│ │ Seed Saving Manual │ 142   │ 4      │ 2.8%  ││
│ │ Preservation Tech  │ 98    │ 3      │ 3.1%  ││
│ │ Drying Techniques  │ 23    │ 1      │ 4.3%  ││
│ │ Root Cellaring     │ 18    │ 1      │ 5.6%  ││
│ └──────────────────────────────────────────────┘│
└──────────────────────────────────────────────────┘
```

### Data Source

- **Data source**: Etsy API (via Google Sheets export)
- **Dimensions**: Product name
- **Metrics**: Orders, Revenue, Conversion Rate, Views
- **Filters**: Date >= May 30

### Connection Steps

1. **Export Etsy data to Google Sheets** (manually from Shop Manager > Listings)
2. **Create columns**: Product | Views | Orders | Revenue | Conv Rate
3. **In Looker Studio**: Connect Google Sheet as data source
4. **Create bar chart**:
   - Dimension: Product name
   - Metric: Orders
   - Sort by Orders descending
5. **Create table**:
   - Dimensions: Product name
   - Metrics: Views, Orders, Revenue, Conversion Rate

---

## Tab 4: Week-over-Week Trends

**Purpose**: Spot growth patterns and make decision-gate calls.

### Layout

```
┌──────────────────────────────────────────────────┐
│      GROWTH TRENDS & DECISION GATES MAY 30+     │
│                                                 │
│ ┌──────────────────────────────────────────────┐│
│ │ Kit Subscriber Growth (Line Chart)           ││
│ │                                              ││
│ │ Subs │                                  ▓▓▓  ││
│ │      │                           ▓▓▓▓▓▓▓▓   ││
│ │      │                    ▓▓▓▓▓▓▓             ││
│ │      │             ▓▓▓▓▓▓                    ││
│ │  0   └──────────────────────────────────────┤ ││
│ │      May30 Jun1 Jun3 Jun5 Jun7 Jun9 Jun11 │ ││
│ │                                    (trending) ││
│ │ Target: 200+ by Jun 30                       ││
│ │ Current pace: 30/week (180 by Jun 30)       ││
│ │ Status: ⚠️  YELLOW — needs acceleration     ││
│ └──────────────────────────────────────────────┘│
│                                                 │
│ ┌──────────────────────────────────────────────┐│
│ │ Decision Gate Progress (Scorecard Table)     ││
│ │                                              ││
│ │ Gate | Metric | Target | Current | Status  ││
│ │ Week 1| Kit subs | 65+ | 65 ✓ | PASS     ││
│ │ Week 1| Email open | 40%+ | 35% ✗ | WATCH ││
│ │ Week 1| Orders | 4+ | 5 ✓ | PASS         ││
│ │ Week 1| IG followers | 150+ | 145 ✗ | NEAR ││
│ │ Jun 30| Kit subs | 200+ | est. 180 | WATCH ││
│ │ Jun 30| Conv rate | 2%+ | est. 2.3% ✓ | PASS ││
│ └──────────────────────────────────────────────┘│
└──────────────────────────────────────────────────┘
```

### Data Sources

**Line Chart: Subscriber Growth**
- Dimension: Date
- Metric: Kit subscriber count
- Date range: May 30–Jun 30

**Scorecard Table: Decision Gate Progress**
- Data source: Google Sheets (Weekly Rollup tab)
- Columns: Gate name | Target | Current | Status
- Update frequency: Weekly (Sunday)

### Connection Steps

1. **Create date-based metric export** (daily Kit subscriber snapshots to Google Sheet)
2. **In Looker Studio**: Connect to Google Sheet
3. **Create line chart**:
   - Dimension: Date
   - Metric: SUM of subscriber count
   - Trend line: Add trend to show pace toward Jun 30 target
4. **Create table**:
   - Data source: Google Sheet (Weekly Rollup)
   - Columns: Date | Kit Subs | Orders | Decision | Status
   - Conditional formatting: GREEN for PASS, YELLOW for WATCH, RED for FAIL

---

## Optional: Real-Time Broadcast Widget

If Kit allows webhook integration:

```
┌─────────────────────────────┐
│ EMAIL BROADCAST LIVE STATUS │
│                             │
│ Launch Broadcast (Live)     │
│ Sent: May 30, 12:00pm       │
│ Opens: 28% (↑4% in last hr) │
│ Clicks: 4% (↑1% in last hr) │
│ Delivered: 100% (65/65)     │
│ Bounces: 0                  │
│                             │
│ Next email: Jun 2, 9:00am   │
└─────────────────────────────┘
```

**Setup**: Kit Webhook → Google Sheets → Looker Studio (advanced)

---

## Migration Path: Sheets → Looker Studio

**Phase 2 (May 30–Jun 30)**: Use manual Google Sheets
- Simpler setup
- Works without API integration
- Familiar interface

**Phase 3 (if >200 orders/month)**: Upgrade to Looker Studio
- Real-time dashboards
- Automated data pull
- Professional presentation to investors/partners

---

## Implementation Checklist

**If implementing Looker Studio (optional)**:

- [ ] Verify GA4 property is connected to Looker Studio (Admin > Linked sources)
- [ ] Export Etsy data to Google Sheet (manual, weekly)
- [ ] Export Kit data to Google Sheet (manual, daily)
- [ ] Create data sheet with Product | Views | Orders | Revenue columns
- [ ] Create Looker Studio report with 4 tabs
- [ ] Add filters for date range (May 30–Jun 30)
- [ ] Test that charts update when source data changes
- [ ] Share dashboard with yourself (for phone access)
- [ ] Bookmark dashboard for daily morning checks

**If sticking with Google Sheets (recommended for now)**:

- [ ] Create 7-sheet Google Sheets template (per PHASE_2_ANALYTICS_GOOGLE_SHEETS_TEMPLATE_SPEC.md)
- [ ] Add formulas for auto-calculation
- [ ] Set up daily data-entry process (5 min/day)
- [ ] Set reminders for Sunday weekly rollup
- [ ] Bookmark sheet on phone

---

## Troubleshooting

**Problem**: Looker Studio doesn't show GA4 data
**Solution**: Check that GA4 property is linked in Admin > Linked sources. If not, add it manually.

**Problem**: Etsy data not updating in Looker Studio
**Solution**: Looker Studio only connects to Google Sheets, not Etsy API directly. You'll need to export Etsy data to Sheets manually (weekly), then create a Looker chart on top of that.

**Problem**: Charts show no data for May 30
**Solution**: Make sure data source has data for that date. Check date filter in chart settings.

---

## Summary

- **Sheets approach** (recommended for May 30–Jun 30): Simple, manual, sufficient for decision-making
- **Looker Studio approach** (optional, if Phase 3 approved): Professional dashboards, real-time, better for stakeholder visibility

Pick the approach that fits your workflow. You can always upgrade to Looker Studio later.

---

**Next steps**: Implement PHASE_2_ANALYTICS_SETUP_GUIDE.md (5 steps, 30 min) for May 30 readiness.
