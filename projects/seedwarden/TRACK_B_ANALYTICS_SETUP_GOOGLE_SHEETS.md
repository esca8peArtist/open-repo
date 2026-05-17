---
title: "Track B Analytics Setup — Google Sheets Dashboard"
prepared: 2026-05-17
status: production-ready — copy-paste ready for Gate 3 execution
source: PHASE_2_ANALYTICS_INFRASTRUCTURE_PRESTAGING.md (Section 4)
scope: Create Google Sheets dashboard for May 30–June 30 daily metrics tracking
---

# Track B Analytics Setup — Google Sheets Dashboard

**Purpose**: Step-by-step setup guide to create the Seedwarden Phase 2 analytics dashboard
in Google Sheets. Complete this before May 30. Estimated time: 30–45 minutes.

**Goal**: A single Google Sheet with daily tracking for orders, revenue, social reach, and
email growth across May 30–June 30. One row per day. Formulas pre-built. Shared and ready
for daily operator input.

---

## Overview: What You Are Building

**Sheet name**: "Seedwarden Phase 2 Analytics Dashboard"

**Tabs** (create all 5):
1. Daily Metrics — one row per day, May 30 to June 30
2. Weekly Summary — rolled-up weekly totals with WoW % change
3. Monthly Cohort Performance — buyer cohort breakdown
4. KPI Summary Dashboard — one-page green/yellow/red status view
5. Raw Data Log — append-only transaction log from etsy_daily_sync.py output

**Primary use tab**: Tab 1 (Daily Metrics) — updated every morning in ~5 minutes.

---

## Step 1 — Create the Google Sheet

1. Go to https://sheets.google.com
2. Click the "+" (Blank) button to create a new spreadsheet
3. Click "Untitled spreadsheet" at the top and rename it: "Seedwarden Phase 2 Analytics Dashboard"
4. You should now have one tab at the bottom labeled "Sheet1"

---

## Step 2 — Create All 5 Tabs

At the bottom of the sheet, rename and add tabs:

1. Right-click "Sheet1" > Rename > type "Daily Metrics"
2. Click the "+" icon to add a new tab > Rename > "Weekly Summary"
3. Add tab > Rename > "Monthly Cohort Performance"
4. Add tab > Rename > "KPI Summary"
5. Add tab > Rename > "Raw Data Log"

---

## Step 3 — Tab 1: Daily Metrics Column Headers

Click on the "Daily Metrics" tab. In Row 1, enter these headers (one per column, A through J):

| Column | Header |
|--------|--------|
| A | Date |
| B | Etsy Orders |
| C | Etsy Revenue ($) |
| D | TikTok Views |
| E | TikTok Engagement |
| F | Instagram Reach |
| G | Instagram Engagement |
| H | Pinterest Impressions |
| I | Email Subscribers (total) |
| J | Notes |

**Formatting (optional but recommended)**:
- Select Row 1 > Format > Text > Bold
- Select Row 1 > Format > Alternating colors (choose a light green or gray theme)
- Freeze Row 1: View > Freeze > 1 row (so headers stay visible when scrolling)

---

## Step 4 — Create the Date Column (May 30 to June 30)

In cell A2, type the launch date:
```
2026-05-30
```

In cell A3, type:
```
=A2+1
```

Select cell A3. Copy it (Ctrl+C or Cmd+C). Then select A4 through A33 (that covers all 32 days
from May 30 to June 30). Paste (Ctrl+V or Cmd+V).

Verify: A2 = 2026-05-30, A33 = 2026-06-30. You should have 32 rows of dates.

**Format the date column**: Select A2:A33 > Format > Number > Date (choose YYYY-MM-DD format
for consistency with the etsy_daily_sync.py output).

---

## Step 5 — Pre-Fill Formulas for Average Order Value

In an empty column to the right of your main data (column K), add a derived metric:

**Column K header**: AOV (Avg Order Value)

In cell K2, enter:
```
=IF(B2>0, C2/B2, 0)
```

Copy K2 down to K33.

This calculates average order value per day (Revenue / Orders). Shows $0 on days with no orders
rather than a divide-by-zero error.

---

## Step 6 — Rolling 7-Day Average Formulas

Add two rolling average columns for TikTok Views and Email Subscribers.

**Column L header**: TikTok 7-Day Avg
**Column M header**: Email Subs 7-Day Avg

In cell L2:
```
=IF(ROW()-1<7, AVERAGE($D$2:D2), AVERAGE(D2:OFFSET(D2,-6,0)))
```

In cell M2:
```
=IF(ROW()-1<7, AVERAGE($I$2:I2), AVERAGE(I2:OFFSET(I2,-6,0)))
```

Copy L2 down to L33 and M2 down to M33.

**How these work**: For the first 6 days (before a full week of data), the formula averages
all available days. From Day 7 onward, it averages the trailing 7 days. This prevents #DIV/0!
errors in the first week of tracking.

---

## Step 7 — Tab 2: Weekly Summary Setup

Click the "Weekly Summary" tab. Enter these headers in Row 1:

| Column | Header |
|--------|--------|
| A | Week |
| B | Orders (total) |
| C | Revenue (total) |
| D | WoW Orders % Change |
| E | WoW Revenue % Change |
| F | Top Guide |
| G | Top Traffic Source |
| H | Email Subscribers Added |
| I | Notes |

In A2 through A6, enter: Week 1, Week 2, Week 3, Week 4, Week 5

**Revenue formula** (manual entry recommended for this tab — simpler and more reliable
than cross-tab SUMIF for a 5-week period):
- Enter B2 through B6 manually each Monday morning with the week's total from Tab 1
- Enter C2 through C6 manually with the week's revenue total

**WoW % Change formulas**:

In D3 (Week 2 onwards):
```
=IF(B2>0, ((B3-B2)/B2)*100, 0)
```
Copy D3 down to D6.

In E3:
```
=IF(C2>0, ((C3-C2)/C2)*100, 0)
```
Copy E3 down to E6.

These show the percentage change in orders and revenue week-over-week. A positive number
means growth; negative means decline.

---

## Step 8 — Tab 4: KPI Summary Dashboard

Click the "KPI Summary" tab. This is a one-page status dashboard. No daily edits needed —
update it weekly.

Set up this layout starting in Row 1:

**Row 1**: Type "SEEDWARDEN PHASE 2 — KPI SUMMARY" (merged across A1:F1, bold, 14pt font)
**Row 2**: Type "Period: May 30 – June 30, 2026" (A2)

Leave Row 3 blank as a spacer.

**Rows 4–11 — KPI table**:

| Col A | Col B | Col C | Col D |
|-------|-------|-------|-------|
| METRIC | TARGET | ACTUAL | STATUS |
| Total Orders (31 days) | 40–60 | [link to Daily Metrics sum] | [formula] |
| Total Revenue (31 days) | $1,000–$1,500 | [link to Daily Metrics sum] | [formula] |
| Email Subscribers Gained | 100–150 | [manual entry] | [formula] |
| Avg Daily Orders | 1.5–2.0/day | [formula] | [formula] |
| Email Open Rate | 35%+ | [manual from Kit] | [formula] |
| TikTok 7-Day Avg Views | 500+ | [from Tab 1 col L] | [formula] |
| Pinterest Impressions (total) | 10,000+ | [sum from Tab 1 col H] | [formula] |

**Actual column formulas**:

For Total Orders (C5), enter:
```
=SUM('Daily Metrics'!B2:B33)
```

For Total Revenue (C6):
```
=SUM('Daily Metrics'!C2:C33)
```

For Avg Daily Orders (C8):
```
=IFERROR(SUM('Daily Metrics'!B2:B33)/COUNTA('Daily Metrics'!A2:A33),0)
```

For Pinterest total (C10):
```
=SUM('Daily Metrics'!H2:H33)
```

**Status column formulas** (enter in D5 through D11 — adjust ranges to match your row numbers):

For Total Orders status (D5):
```
=IF(C5>=40, "ON TRACK", IF(C5>=25, "WATCH", "BEHIND"))
```

For Total Revenue status (D6):
```
=IF(C6>=1000, "ON TRACK", IF(C6>=600, "WATCH", "BEHIND"))
```

For Email Subscribers status (D7 — manual entry in C7):
```
=IF(C7>=100, "ON TRACK", IF(C7>=60, "WATCH", "BEHIND"))
```

**Color-coding the STATUS column** (optional but makes it scannable in 3 seconds):
- Select D5:D11 > Format > Conditional formatting
- "Text contains" ON TRACK > fill color: light green (#B7E1CD)
- "Text contains" WATCH > fill color: light yellow (#FFEEBA)
- "Text contains" BEHIND > fill color: light red (#F4CCCC)

---

## Step 9 — Tab 5: Raw Data Log Headers

Click "Raw Data Log." Enter these headers in Row 1 (matching the etsy_daily_sync.py CSV output):

| Column | Header |
|--------|--------|
| A | created_date |
| B | receipt_id |
| C | transaction_id |
| D | listing_title |
| E | quantity |
| F | price_usd |
| G | total_price_usd |
| H | coupon_code |
| I | buyer_country |

Data in this tab comes from `scripts/etsy_daily_sync.py`. To import:
- Option A: Run the script locally, open the generated CSV, copy rows and paste into Row 2 onward
- Option B: If CSV is in Google Drive, use `=IMPORTDATA("DRIVE_CSV_URL")` in cell A1
  (replace DRIVE_CSV_URL with the shared link from Google Drive, append `&export=csv` if needed)

---

## Step 10 — Share the Sheet

1. Click "Share" (top right corner)
2. In "Add people and groups," enter: wanka95@gmail.com — set to "Editor"
3. Under "General access," set to "Anyone with the link" > "Viewer"
4. Click "Copy link" — save this URL in `WORKLOG.md` and in `.env` as `GOOGLE_SHEET_URL=`

---

## Step 11 (Optional) — Growth Trajectory Chart

Create a visual chart showing email subscriber growth over 30 days.

1. Click the "Daily Metrics" tab
2. Select columns A (Date) and I (Email Subscribers total) — hold Ctrl/Cmd and click both column headers
3. Click Insert > Chart
4. In the Chart editor, Chart type = Line chart
5. Under "Data range," confirm it uses A1:A33 and I1:I33
6. Customize > Chart title: "Email Subscriber Growth — May 30 to June 30"
7. Move the chart to an empty area of the sheet or to the KPI Summary tab

This chart updates automatically as you enter daily subscriber counts in column I.

---

## Summary Checklist

- [ ] Google Sheet created and named "Seedwarden Phase 2 Analytics Dashboard"
- [ ] All 5 tabs created: Daily Metrics, Weekly Summary, Monthly Cohort Performance, KPI Summary, Raw Data Log
- [ ] Daily Metrics: 10 column headers in Row 1
- [ ] Date column filled from 2026-05-30 to 2026-06-30 (32 rows)
- [ ] AOV formula in column K
- [ ] 7-day rolling average formulas in columns L (TikTok) and M (Email Subs)
- [ ] Weekly Summary: headers, week labels, WoW % formulas
- [ ] KPI Summary: target/actual/status table with conditional formatting
- [ ] Raw Data Log: headers matching etsy_daily_sync.py output
- [ ] Sheet shared with wanka95@gmail.com (Editor) and "Anyone with link" (Viewer)
- [ ] Sheet URL saved in WORKLOG.md
- [ ] (Optional) Line chart showing email subscriber growth

---

## Day-of-Launch Data Entry Procedure (May 30 morning)

On May 30 before 09:00 UTC:
1. Open the sheet to Tab 1 (Daily Metrics)
2. Confirm Row 2 shows 2026-05-30 in column A
3. Leave all data columns blank — data entry starts at end of day (after orders come in)
4. On the evening of May 30 (or May 31 morning): fill in Day 1 data across columns B–J

Refer to `PHASE_2_ANALYTICS_INFRASTRUCTURE_PRESTAGING.md` Section 7 for the full Day-1
readiness checklist and the hour-by-hour monitoring schedule on launch day.

---

*Source: PHASE_2_ANALYTICS_INFRASTRUCTURE_PRESTAGING.md Section 4. Prepared 2026-05-17.*
*Also reference: PHASE_2_ANALYTICS_GOOGLE_SHEETS_TEMPLATE_SPEC.md for the full template schema.*
