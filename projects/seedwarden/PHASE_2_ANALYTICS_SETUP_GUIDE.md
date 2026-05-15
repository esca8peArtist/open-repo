---
title: Phase 2 Analytics Setup Guide — Complete Walkthrough
status: production-ready
date: 2026-05-15
scope: 5-step end-to-end setup for May 30 launch analytics visibility
time_estimate: 30 minutes
deadline: 2026-05-25
---

# Phase 2 Analytics Setup Guide

**Purpose**: Production-ready analytics infrastructure for May 30 launch. This guide walks you through setup in 5 steps (30 minutes total). All steps must complete by **May 25** to capture May 29 baseline data before launch.

---

## Prerequisites

**You will need:**
- Google account (for Sheets and GA4)
- Etsy Shop Manager access (admin role)
- Kit dashboard access (admin or analyst role)
- Optional: Looker Studio account (free, for advanced dashboards)

**Files you'll reference:**
- `phase-2-analytics-kpi-setup.md` — baseline KPI targets and measurement framework
- `PHASE_2_ANALYTICS_GOOGLE_SHEETS_TEMPLATE_SPEC.md` — detailed sheet layouts and formulas
- `etsy_ga4_kit_analytics_bridge.py` — Python script for automated data pulls (requires API credentials)

---

## Step 1: Verify Google Analytics 4 Configuration (10 minutes)

### 1.1 Check GA4 Property Exists

1. **Login to Google Analytics**: https://analytics.google.com
2. **Select your property**: Look for "Seedwarden" or your analytics property name in the left sidebar
3. **Navigate to Admin** (bottom left icon)
   - Property > Data Streams
   - Confirm you see a web data stream with your domain (seedwarden.com or similar)
   - Record the **Measurement ID** (format: `G-XXXXXXXXXX`) — you'll use this in Kit setup

### 1.2 Enable Required Dimensions and Metrics

1. **In Admin > Custom definitions**, verify these are enabled:
   - **utm_source** (traffic source — Kit, Instagram, TikTok, Pinterest, etc.)
   - **utm_medium** (medium — email, social, referral)
   - **utm_campaign** (campaign name — phase2-launch-broadcast, etc.)

   If any are missing, add them:
   - Click **Custom dimensions** > **Create custom dimension**
   - Name: `utm_source`, Parameter: `utm_source`, Scope: Event
   - Repeat for `utm_medium`, `utm_campaign`

2. **Verify built-in Reports**: Admin > Reports > Life cycle
   - Confirm you see "Acquisition > Traffic Acquisition" report
   - This is where you'll track incoming traffic by source/medium post-launch

### 1.3 Set Up GA4 Data API Access (for automated pulls)

**Important for automation**: If you want the Python script (`etsy_ga4_kit_analytics_bridge.py`) to auto-fetch GA4 data, you'll need API credentials.

1. **Go to Admin > Service accounts**
2. **Create a new service account** (or use an existing one):
   - Name: "Seedwarden-Analytics-API"
   - Grant role: Viewer
3. **Create a JSON key**: Download the credentials file and save it as `projects/seedwarden/config/ga4-credentials.json`

**For now, optional** — you can manually pull GA4 data until the script is configured.

---

## Step 2: Configure Kit Analytics Integration (5 minutes)

### 2.1 Connect GA4 to Kit Landing Page

1. **Login to Kit**: https://kit.com
2. **Go to Settings > Integrations > Analytics**
3. **Enable Google Analytics 4**:
   - Paste your **Measurement ID** from Step 1.3
   - Click **Connect**
   - Kit will add GA4 tracking to your landing page automatically

### 2.2 Verify Kit Analytics Dashboard

1. **Go to Kit home page** (Dashboard tab)
2. **Check you see**:
   - Subscribers counter (top of page)
   - Recent conversion events
   - Email open/click rates (under "Emails" section)

3. **Create a bookmark** to this page — you'll check it daily after May 30.

### 2.3 Set Up Kit Automation Tags (5 minutes)

Kit should already have tags for your zones (zone-3, zone-4, ..., zone-10, seed-saver, etc.). Verify:

1. **Go to Automation > Tags**
2. **Confirm these tags exist**:
   - `zone-3`, `zone-4`, `zone-5`, `zone-6`, `zone-7`, `zone-8`, `zone-9`, `zone-10`
   - `seed-saver`, `city-grower`, `preservationist`
3. **Check subscriber count per tag**:
   - Go to Automation > Subscribers
   - Filter by tag to see how many subscribers fall into each category
   - **Record these baseline counts** (you'll need them May 29)

---

## Step 3: Create Google Sheets Tracking Template (10 minutes)

### 3.1 Create a New Google Sheet

1. **Go to Google Sheets**: https://sheets.google.com
2. **Create new > Blank spreadsheet**
3. **Name it**: `Seedwarden Phase 2 Analytics — May 30–June 30`
4. **Share it** with yourself on your phone (File > Share > yourself@gmail.com)

### 3.2 Create the 7 Tracking Sheets

In the same spreadsheet, create these 7 sheets (tab names):

1. **Daily Dashboard** — captures every metric once per day
2. **Weekly Rollup** — aggregates daily data into weekly summaries
3. **Monthly Synthesis** — 30-day analysis + decision gate
4. **Cohort Tracking** — which customers bought what, when
5. **Product Performance** — individual product metrics
6. **Acquisition ROI** — cost per acquisition by channel
7. **Go/No-Go Decision Log** — all major go/no-go decisions + rationale

Detailed specifications for each sheet are in `PHASE_2_ANALYTICS_GOOGLE_SHEETS_TEMPLATE_SPEC.md`.

### 3.3 Add Formulas (if comfortable with Google Sheets)

If you're familiar with Sheets, add formulas to:
- **Daily Dashboard**: `=QUERY()` to pull data from other sheets
- **Weekly Rollup**: `=SUMIF()` and `=AVERAGE()` to aggregate daily data
- **Monthly Synthesis**: `=IF()` statements to highlight go/no-go decisions

If formulas are unfamiliar, leave cells blank for now — you can fill them manually each morning.

---

## Step 4: Set Up Etsy Baseline Recording (5 minutes on May 29)

**Do this on May 29, the day before launch** (not before):

1. **Go to Etsy Shop Manager**: https://www.etsy.com/your/shops/me/shop-home
2. **Click Analytics** (left sidebar)
3. **Go to Listings** view
4. **For each of the 21 Phase 2 products, record**:
   - Product name
   - View count (as of 11:59pm May 29)
   - Favorite count
   - Current sales (if any)

5. **Enter these baseline numbers into your Google Sheet** under "Daily Dashboard" > "May 29 Baseline" rows

**Why now?** Etsy does not provide historical data snapshots retroactively. Without a May 29 baseline, you cannot measure the lift Phase 2 creates.

---

## Step 5: Set Up Social Media Baselines & Verify Links (5 minutes on May 29)

**Do this on May 29, the day before launch**:

### 5.1 Record Follower Baselines

| Platform | Where to Check | Baseline Recording |
|---|---|---|
| Instagram | Profile > Insights > Followers | Record total follower count at 11:59pm May 29 |
| TikTok | Creator Center > Analytics > Overview | Record total follower count at 11:59pm May 29 |
| Pinterest | Analytics > Overview | Record total followers at 11:59pm May 29 |

### 5.2 Verify UTM Parameters in All Links

Before May 30, check that all links in your social bios and Kit email have UTM parameters:

**Kit email links should look like:**
```
https://kit.com/seedwarden?utm_source=kit&utm_medium=email&utm_campaign=phase2-launch-broadcast
```

**Instagram bio link should look like:**
```
https://kit.com/seedwarden?utm_source=instagram&utm_medium=social&utm_campaign=phase2-instagram-bio
```

**TikTok bio link should look like:**
```
https://kit.com/seedwarden?utm_source=tiktok&utm_medium=social&utm_campaign=phase2-tiktok-bio
```

If any links are missing UTMs, add them now (before May 30).

---

## Launch-Day Operations (May 30)

### Timeline

- **10:00am**: Launch complete. Begin tracking (see **Launch-Day Checkpoints** below).
- **12:05pm**: Kit broadcast sends. First major checkpoint (Checkpoint 1).
- **6:00pm**: Mid-afternoon check. Escalate if needed.
- **9:00pm**: Final daily checkpoint (Checkpoint 2 — major go/no-go decision).

### Launch-Day Checkpoints

**Checkpoint 1 (12:05pm — T+5 minutes after broadcast)**

Check these metrics:
- Kit signups ≥3 ✓
- Instagram post live ✓
- TikTok videos live ✓
- Etsy orders ≥0 (any orders confirm traffic) ✓

**Decision rule**: All four ✓ = GREEN (proceed normally). Any ✗ = escalate to Contingency A (see Launch Day Guide).

**Checkpoint 2 (9:00pm — T+12 hours)**

Check these metrics (record in Daily Dashboard):
- Kit signups: ≥12 total
- Email open rate: >25%
- Etsy orders: 5–12 total
- Social combined engagement: 20+ (likes + comments + views across IG + TikTok + Pinterest)

**Decision rule**:
- GREEN (5+ of 7 metrics at target): continue normally, proceed to Week 1
- YELLOW (3–4 metrics at target): escalated monitoring, check every 4 hours
- RED (<3 metrics at target OR 0 orders): pause, investigate, potentially activate Contingency B

---

## Post-Launch Operations (June 1–30)

### Daily Metrics (5 minutes, every morning)

Every morning through June 30, fill in your Daily Dashboard:

| Metric | Source | How to Find |
|---|---|---|
| Kit new signups | Kit Dashboard | Home > Subscribers (compare to yesterday) |
| Etsy orders | Etsy Shop Manager > Orders | Filter by May 30 onward |
| Email open rate | Kit > Emails > launch broadcast | % opened from yesterday's sends |
| Instagram followers | Instagram Insights | Followers counter |
| TikTok followers | TikTok Analytics > Overview | Followers counter |
| Pinterest monthly viewers | Pinterest Analytics > Overview | Wait 14 days for data |

**Escalation triggers** (act immediately if any occur):
- Email open rate < 15% for 2 consecutive sends
- 0 Etsy orders after 100+ listing views
- Kit landing page receives 0 signups for 24+ hours
- Any social platform shows 0 new followers for 5 consecutive days despite posting

### Weekly Rollup (Sundays, 10 minutes)

Every Sunday, summarize the week in your Weekly Rollup sheet:

```
Week of [date]:
- Kit total subscribers: [N] (+[N] this week)
- Top zone: [zone-X] ([N] subscribers)
- Etsy orders: [N] orders, $[revenue]
- Top product: [product-name] ([orders] orders)
- Email 3 click rate: [%]
- Instagram followers: [total] (+[N] this week)
- TikTok followers: [total] (+[N] this week)
- Decision: [GREEN / YELLOW / RED] — [reason]
```

Also log this in `projects/seedwarden/WORKLOG.md`.

### Monthly Synthesis (June 30)

On June 30, pull these final metrics for the Phase 2→Phase 3 gate decision:

| Metric | Target | Result | Pass? |
|---|---|---|---|
| Kit subscribers | 200+ | [N] | ✓/✗ |
| Email revenue per subscriber | ≥$0.10 | $[N] | ✓/✗ |
| Etsy listing conversion rate | 2%+ | [%] | ✓/✗ |
| Instagram followers | 400+ | [N] | ✓/✗ |
| Products with CTR lift | 5+ | [N] | ✓/✗ |
| Phase 1→Phase 2 repeat purchase rate | 35%+ | [%] | ✓/✗ |

**Decision**: If ≥5 metrics pass → Phase 3 Option B approved. If 3–4 → Phase 3 Option A or partial. If <3 → investigate before Phase 3.

---

## Optional: Automated Data Pulls (Looker Studio)

If you want an automated dashboard instead of manual Google Sheets:

1. **Create a Looker Studio report**: https://lookerstudio.google.com
2. **Connect GA4** (built-in connector)
3. **Connect Etsy** (requires API key) and **Kit** (requires API key)
4. **Use the dashboard spec** in `LOOKER_STUDIO_DASHBOARD_SPEC.md` to add panels

This is optional — Google Sheets tracking is sufficient for May 30–June 30.

---

## Automation Script (Optional)

If you want to automate daily data pulls, use the provided Python script:

```bash
cd projects/seedwarden
python etsy_ga4_kit_analytics_bridge.py --date 2026-06-01
```

This script:
1. Pulls yesterday's Etsy order data from Etsy API
2. Pulls GA4 traffic data
3. Pulls Kit subscriber data
4. Outputs a CSV ready to paste into your Daily Dashboard

Requires setup (API keys in `config/etsy-api-key.txt`, GA4 credentials, Kit API token). See script comments for setup instructions.

---

## Troubleshooting

### Problem: GA4 not showing traffic

**Solution**: Check that UTM parameters are in all links. GA4 tracks `utm_source` / `utm_medium` / `utm_campaign` — without these, traffic appears as "direct" and is not attributable.

Test: Append `?utm_source=test&utm_medium=email&utm_campaign=test` to a link and click it. Check GA4 Realtime report (Analytics > Realtime) — you should see the click appear within 10 seconds.

### Problem: Kit subscriber count not updating

**Solution**: Kit updates the subscriber counter every few minutes, but analytics take 24 hours to finalize. If you don't see new subscribers reflected immediately, wait 1 hour and refresh.

### Problem: Etsy orders not showing in Shop Manager

**Solution**: Orders can take 15–30 minutes to appear in Etsy after purchase. Refresh every 5 minutes during launch day. If an order doesn't appear within 1 hour, check your payment processing (may indicate Etsy payment gateway issue).

### Problem: Social follower counts not updating

**Solution**: Follower counts update with 30-minute lag on Instagram and TikTok, 24-hour lag on Pinterest. Check Instagram Insights instead of the profile follower badge for real-time counts.

---

## Success Criteria

By May 25, all 5 steps should be complete:

- [ ] Step 1: GA4 property verified, Measurement ID recorded
- [ ] Step 2: GA4 connected to Kit, Kit tags verified
- [ ] Step 3: Google Sheet created with 7 tabs
- [ ] Step 4: Baseline recording scheduled for May 29
- [ ] Step 5: Baseline recording scheduled for May 29, UTM links verified

By May 29, before launch:

- [ ] All Etsy listing view counts recorded (baseline)
- [ ] All social follower counts recorded (baseline)
- [ ] Kit subscriber count and zone distribution recorded (baseline)
- [ ] Google Sheet bookmarked on phone and desktop
- [ ] Discord or Slack reminder set for May 30 12:05pm (Checkpoint 1)

---

**Questions?** See `phase-2-analytics-kpi-setup.md` for detailed KPI definitions and success targets. See `TRACK_B_LAUNCH_DAY_OPERATIONS_GUIDE.md` for launch-day decision logic.

**Next**: On May 30, follow the Launch-Day Operations timeline above. Post-launch: daily 5-minute metric checks through June 30, then final synthesis on June 30 for Phase 2→Phase 3 gate decision.
