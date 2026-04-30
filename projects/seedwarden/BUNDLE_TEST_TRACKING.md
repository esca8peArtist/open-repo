---
title: "Bundle Test Tracking — Weekly Export Workflow and Manual Log"
date: 2026-04-30
status: production-ready
context: Data collection infrastructure for BUNDLE_A_B_TEST_PLAN.md
references: BUNDLE_A_B_TEST_PLAN.md, BUNDLE_TEST_DATA.csv, BUNDLE_TEST_ANALYSIS.md
---

# Bundle Test Tracking
## Weekly Export Workflow and Manual Log Template

**Purpose**: This document tells you exactly how to collect data each week during the May–July 2026 bundle tests. It is a repeating procedure — run it every Sunday evening and takes 12–18 minutes. It feeds data into BUNDLE_TEST_DATA.csv, which feeds the decisions in BUNDLE_TEST_ANALYSIS.md.

---

## Weekly Export Procedure

Run this every Sunday evening. The Etsy analytics window resets Monday morning, so Sunday evening is the last complete day of each tracking week.

**Time required**: 12–18 minutes per week.

### Step 1: Log Into Etsy Seller Dashboard (1 minute)

- Go to etsy.com/your/shops/me/dashboard
- Click "Stats" in the left sidebar
- You are now in the Etsy Stats panel

### Step 2: Set the Date Range (2 minutes)

- In the Stats panel, click the date picker (top right of the stats area)
- Set: From = Monday of the current week, To = Sunday of the current week (today)
- The panel will show data for the 7-day window

If you are capturing the pre-test baseline (April 21–27), set From = April 21, To = April 27 before the bundle goes live on May 1. Do this baseline export on April 30 before midnight.

### Step 3: Pull Per-Listing Stats (6–8 minutes)

For each listing you are tracking this week, do the following:

**3a. Navigate to listing-level stats:**
- In the Stats panel, scroll down to "Listings" table
- Find the listing by name (Spring Forager Bundle, Wild Edibles Guide, Zone Calendar, Harvest Season Bundle, etc.)
- Click the listing name to open listing-level detail

**3b. Record these six values:**

| Field | Where to Find It | Column in CSV |
|---|---|---|
| Impressions | Etsy Stats > Listings > this listing | Impressions |
| Views (listing page views) | Same panel, "Views" column | Views |
| Clicks (external — optional) | Same panel if shown | Clicks |
| Orders (conversions) | Same panel, "Orders" column | Conversions |
| Revenue | Same panel, "Revenue" column | Revenue |
| Conversion Rate | Etsy calculates this: Orders / Views | Conversion_Rate_Pct |

**3c. Calculate AOV:**
- AOV = Revenue / Conversions
- If Conversions = 0 for the week, leave AOV blank (do not enter zero — it will skew averages)
- If Conversions = 0, write "0 sales" in the Notes column

**3d. Repeat for each listing being tracked this week.**

Listings to track each month:

| Month | Listings to Track |
|---|---|
| Pre-test (Apr 21–27) | Wild Edibles Guide, Zone Calendar |
| Month 1 (May) | Spring Forager Bundle, Wild Edibles Guide, Zone Calendar |
| Month 2 (June) | Harvest Season Bundle, Fermented Harvest Handbook, Harvest Preservation Field Manual, Grow Your Own Hot Sauce |
| Month 3 (July) | Harvest Season Bundle (price changes July 15) |

### Step 4: Enter Data Into BUNDLE_TEST_DATA.csv (3–5 minutes)

- Open `/home/awank/dev/SuperClaude_Framework/projects/seedwarden/BUNDLE_TEST_DATA.csv`
- Find the pre-populated row matching this week's date range and listing name
- Fill in the six values: Impressions, Views, Clicks, Conversions, Revenue, AOV, Conversion_Rate_Pct
- Add any relevant observation to the Notes column

**Notes column usage** — write a brief note any week where:
- A metric moves more than 20% from prior week
- You made a listing change (title, description, photos, price)
- Etsy had a platform outage or sale event
- You ran a social media post that directly promoted this listing
- You got an unusual review or buyer message about the bundle

### Step 5: Write This Week's Decision Log Entry (2–3 minutes)

After filling the CSV, open the Manual Log section below and write one entry for the current week. Use the template provided. This takes 2–3 minutes and is the most valuable part of the process — it forces a weekly read of the data rather than just data collection.

---

## Cannibalization Check (Run Every Week in Month 1)

This check takes 2 minutes and must be done every week during the Spring Forager Bundle test. It detects the most important risk: the bundle cannibalizing individual product sales.

**Formula:**

```
Individual Wild Edibles conversions this week
divided by
Individual Wild Edibles conversions in the April 21–27 baseline
```

If the result is less than 0.85 (i.e., conversions dropped more than 15%), you have a cannibalization signal. Do not wait until end-of-month to check this.

Same calculation for Zone Calendar.

**Example:**
- Baseline (April 21–27): Wild Edibles = 5 conversions, Zone Calendar = 3 conversions
- Week of May 1–7: Wild Edibles = 3 conversions, Zone Calendar = 2 conversions
- Wild Edibles ratio: 3/5 = 0.60 — cannibalization signal (drop >15%)
- Zone Calendar ratio: 2/3 = 0.67 — cannibalization signal
- Action: Flag in notes column, escalate to BUNDLE_TEST_ANALYSIS.md decision framework

---

## Etsy Analytics Export: Known Limitations

These are things Etsy's stats panel does not show natively. Document workarounds here.

**Limitation 1: Etsy does not export individual listing stats as a clean CSV.**
Workaround: Manually transcribe values from the Stats panel into BUNDLE_TEST_DATA.csv. The manual entry process is the intended workflow — Etsy's export function is for overall shop performance, not per-listing detail at the weekly level.

**Limitation 2: Conversion Rate shown by Etsy is visits-based, not impressions-based.**
Note: The BUNDLE_A_B_TEST_PLAN.md uses "views" as the denominator for conversion rate. Etsy Stats shows the same metric labeled as "Conversion Rate" in their UI. Use Etsy's native calculation — do not recalculate.

**Limitation 3: Etsy stats update with a 24–48 hour lag.**
Action: When exporting on Sunday evening, data for Saturday may not be final. This is acceptable — the weekly trend matters more than the single-day precision.

**Limitation 4: Etsy does not show returning-buyer data per listing.**
Workaround: If a buyer purchases both the bundle and an individual product in the same order (double-buyer problem), this appears as two separate line items in your Etsy orders list. Review the orders list manually once per month for the first two months to spot any double-buy patterns.

---

## Manual Log Template

Copy and paste one entry per week. Fill in values after completing the data export.

---

### Week of [DATE RANGE]

**Phase**: [Pre-test / Month 1 Week X / Month 2 Week X / Month 3 Control / Month 3 Test]

**Key metrics this week:**

| Listing | Views | Conv | Conv Rate | Revenue | AOV |
|---|---|---|---|---|---|
| [Listing name] | | | | | |
| [Listing name] | | | | | |
| [Listing name] | | | | | |

**Cannibalization check (Month 1 only):**
- Wild Edibles this week / baseline = [ratio] — [OK / FLAG]
- Zone Calendar this week / baseline = [ratio] — [OK / FLAG]

**Observations:**
[2–3 sentences on anything notable this week — traffic spike, social post that drove views, unusual buyer behavior, listing change made, etc.]

**Decision:** [Continue / Investigate / Escalate to BUNDLE_TEST_ANALYSIS.md]

---

## Completed Weekly Log Entries

Add entries below in reverse chronological order (newest at top).

---

### Pre-test Baseline — Week of April 21–27, 2026

**Phase**: Pre-test baseline

**Key metrics this week:**

| Listing | Views | Conv | Conv Rate | Revenue | AOV |
|---|---|---|---|---|---|
| Wild Edibles Quick Reference Guide | | | | | |
| Zone-by-Zone Seed Starting Calendar | | | | | |

**Cannibalization check**: N/A (bundle not yet live)

**Observations:**
[Capture April 30 before midnight. This is the only baseline window. If missed, use the most recent 7-day period available in Etsy Stats as the proxy baseline and note the date range in the Notes column of the CSV.]

**Decision:** N/A — baseline capture only. Bundle goes live May 1.

---

## Monthly Data Summary Template

At the end of each month, compute these totals before reading BUNDLE_TEST_ANALYSIS.md decisions. Copy the template once per month.

---

### Monthly Summary — [MONTH YEAR]

**Total bundle conversions (month):** [sum of all Conversion cells for this bundle across all weeks]

**Total bundle revenue (month):** [sum of Revenue cells]

**Average bundle conversion rate (month):** [average of weekly Conversion_Rate_Pct values]

**Individual product total conversions (month):**
- [Product 1 name]: [total]
- [Product 2 name]: [total]

**Individual product conversion rates vs. baseline:**
- [Product 1]: [month avg] vs. [baseline rate] = [delta]
- [Product 2]: [month avg] vs. [baseline rate] = [delta]

**Cannibalization verdict:** [No signal / Mild signal / Strong signal — explain]

**Seasonal/external factors this month that may affect data:**
[Note any Etsy platform-wide sales events, your social media volume, email list growth, external traffic spikes]

**Hand off to:** BUNDLE_TEST_ANALYSIS.md — [which decision gate applies]

---
