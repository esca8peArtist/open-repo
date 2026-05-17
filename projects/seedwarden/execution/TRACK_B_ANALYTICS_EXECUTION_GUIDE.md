---
title: "Track B Analytics Execution Guide — Complete Setup"
prepared: 2026-05-17
status: production-ready — copy-paste ready for pre-launch setup
scope: Google Sheets dashboard, Discord daily alerts, GA4 custom dimensions/metrics
sources:
  - TRACK_B_ANALYTICS_SETUP_GOOGLE_SHEETS.md (Sheets template, formulas, tabs)
  - TRACK_B_ANALYTICS_SETUP_DISCORD_AND_GA4.md (Discord webhooks, GA4 dimensions/metrics)
---

# Track B Analytics Execution Guide

**Purpose**: Consolidated guide for all analytics infrastructure setup. Three systems:
1. Google Sheets (15 min) — Daily metrics dashboard
2. Discord (10 min) — Automated daily alerts
3. GA4 (15 min) — Custom dimensions, metrics, audiences

**When to complete**: By May 25 (5 days before launch). All systems must be ready before May 30 09:00am UTC.

**Time estimate**: 45–60 minutes total for all three systems.

---

# System 1: Google Sheets Dashboard (15–20 min)

## Step 1: Create the Google Sheet

1. Go to https://sheets.google.com
2. Click the "+" button (Blank spreadsheet)
3. Click "Untitled spreadsheet" at the top
4. Rename it: `Seedwarden Phase 2 Analytics Dashboard`
5. You now have one default sheet labeled "Sheet1"

## Step 2: Create All 5 Tabs

At the bottom of the spreadsheet, you'll see the sheet tab area. Create all 5:

1. Right-click "Sheet1" > Rename > Type: `Daily Metrics` > OK
2. Click "+" icon next to tab > Add new sheet
   - Name: `Weekly Summary`
3. Click "+" again > Add new sheet
   - Name: `Monthly Cohort Performance`
4. Click "+" again > Add new sheet
   - Name: `KPI Summary`
5. Click "+" again > Add new sheet
   - Name: `Raw Data Log`

You should now have 5 tabs visible at the bottom.

## Step 3: Tab 1 — Daily Metrics Headers

Click the "Daily Metrics" tab. In Row 1, enter these column headers (A through J):

```
A: Date
B: Etsy Orders
C: Etsy Revenue ($)
D: TikTok Views
E: TikTok Engagement
F: Instagram Reach
G: Instagram Engagement
H: Pinterest Impressions
I: Email Subscribers (total)
J: Notes
```

**Optional formatting**:
- Select Row 1 > Format > Bold
- Select Row 1 > Format > Alternating colors (light green or gray theme)
- View > Freeze > 1 row (keeps headers visible when scrolling)

## Step 4: Create Date Column (May 30 to June 30)

In cell A2, type:
```
2026-05-30
```

In cell A3, type:
```
=A2+1
```

Now copy this formula down:
1. Select A3
2. Copy (Ctrl+C or Cmd+C)
3. Select range A4:A33 (that's 30 more rows after A3)
4. Paste (Ctrl+V)

Verify: A2 = 2026-05-30, A33 = 2026-06-30 (32 total days).

**Format as dates**: Select A2:A33 > Format > Number > Date > Choose YYYY-MM-DD format.

## Step 5: Add Derived Metrics (Column K: AOV)

In cell K1, type the header:
```
AOV (Avg Order Value)
```

In cell K2, type this formula:
```
=IF(B2>0, C2/B2, 0)
```

This calculates average order value (Revenue / Orders). It shows 0 on days with no orders
to avoid divide-by-zero errors.

Copy K2 down to K33:
1. Select K2
2. Copy
3. Select K3:K33
4. Paste

## Step 6: Add Rolling Averages (Columns L & M)

These columns track 7-day rolling averages.

**Column L header** (L1):
```
TikTok 7-Day Avg
```

**L2 formula**:
```
=IF(ROW()-1<7, AVERAGE($D$2:D2), AVERAGE(D2:OFFSET(D2,-6,0)))
```

**Column M header** (M1):
```
Email Subs 7-Day Avg
```

**M2 formula**:
```
=IF(ROW()-1<7, AVERAGE($I$2:I2), AVERAGE(I2:OFFSET(I2,-6,0)))
```

Copy both L2 and M2 down to row 33.

**Why these formulas work**: For the first 6 days, they average all available data.
From Day 7 onward, they average the trailing 7 days. This prevents errors in the first week.

## Step 7: Tab 2 — Weekly Summary

Click the "Weekly Summary" tab. In Row 1, add these headers:

```
A: Week
B: Orders (total)
C: Revenue (total)
D: WoW Orders % Change
E: WoW Revenue % Change
F: Top Guide
G: Top Traffic Source
H: Email Subscribers Added
I: Notes
```

In A2 through A6, type:
```
A2: Week 1
A3: Week 2
A4: Week 3
A5: Week 4
A6: Week 5
```

**Week-over-week formulas** (for tracking percentage change):

In D3 (Week 2 onwards), type:
```
=IF(B2>0, ((B3-B2)/B2)*100, 0)
```

In E3, type:
```
=IF(C2>0, ((C3-C2)/C2)*100, 0)
```

Copy D3 down to D6 and E3 down to E6.

**Note**: Columns B (Orders) and C (Revenue) are updated manually each Monday morning
from the Daily Metrics tab. This is simpler and more reliable than cross-sheet formulas.

## Step 8: Tab 4 — KPI Summary Dashboard

Click the "KPI Summary" tab. Build this layout:

**Row 1** (merge A1:F1, bold, 14pt font):
```
SEEDWARDEN PHASE 2 — KPI SUMMARY
```

**Row 2** (A2):
```
Period: May 30 – June 30, 2026
```

Leave Row 3 blank.

**Rows 4–11 — KPI table**:

| Col A | Col B | Col C | Col D |
|-------|-------|-------|-------|
| METRIC | TARGET | ACTUAL | STATUS |
| Total Orders (31 days) | 40–60 | [formula] | [formula] |
| Total Revenue (31 days) | $1,000–$1,500 | [formula] | [formula] |
| Email Subscribers Gained | 100–150 | [manual entry] | [formula] |
| Avg Daily Orders | 1.5–2.0/day | [formula] | [formula] |
| Email Open Rate | 35%+ | [manual from Kit] | [formula] |
| TikTok 7-Day Avg Views | 500+ | [from Daily tab] | [formula] |
| Pinterest Impressions | 10,000+ | [formula] | [formula] |

**ACTUAL column formulas**:

C5 (Total Orders):
```
=SUM('Daily Metrics'!B2:B33)
```

C6 (Total Revenue):
```
=SUM('Daily Metrics'!C2:C33)
```

C8 (Avg Daily Orders):
```
=IFERROR(SUM('Daily Metrics'!B2:B33)/COUNTA('Daily Metrics'!A2:A33),0)
```

C10 (Pinterest Impressions):
```
=SUM('Daily Metrics'!H2:H33)
```

**STATUS column formulas** (D5 onwards):

D5 (Total Orders status):
```
=IF(C5>=40, "ON TRACK", IF(C5>=25, "WATCH", "BEHIND"))
```

D6 (Total Revenue status):
```
=IF(C6>=1000, "ON TRACK", IF(C6>=600, "WATCH", "BEHIND"))
```

D7 (Email Subscribers status):
```
=IF(C7>=100, "ON TRACK", IF(C7>=60, "WATCH", "BEHIND"))
```

**Color-code STATUS column** (optional but highly recommended):
1. Select D5:D11
2. Format > Conditional formatting
3. Add 3 rules:
   - Text contains "ON TRACK" → fill: light green (#B7E1CD)
   - Text contains "WATCH" → fill: light yellow (#FFEEBA)
   - Text contains "BEHIND" → fill: light red (#F4CCCC)

## Step 9: Tab 5 — Raw Data Log

Click the "Raw Data Log" tab. Enter these headers in Row 1:

```
A: created_date
B: receipt_id
C: transaction_id
D: listing_title
E: quantity
F: price_usd
G: total_price_usd
H: coupon_code
I: buyer_country
```

**Data source**: Rows 2+ are populated by the `scripts/etsy_daily_sync.py` script.
See TRACK_B_ANALYTICS_SETUP_GOOGLE_SHEETS.md Step 9 for CSV import options.

## Step 10: Share the Sheet

1. Click "Share" (top right)
2. In "Add people and groups," type: `wanka95@gmail.com`
3. Set permission to: "Editor"
4. Under "General access," click "Anyone with the link" > set to "Viewer"
5. Click "Copy link"
6. **Save this URL** — you'll need it in Step 11

## Step 11: Document and Test

1. Open the sheet in a browser
2. Verify all 5 tabs are present and labeled correctly
3. Click on "Daily Metrics" tab and confirm:
   - Row 1 has headers A–J
   - Column A has dates from 2026-05-30 to 2026-06-30
   - Columns K, L, M have headers and formulas (no errors)
4. Click "KPI Summary" and verify:
   - Merged title row in A1:F1
   - Table structure is readable
   - No #REF! or #DIV/0! errors

**Save the sheet URL** in WORKLOG.md (see Part 4 below).

---

# System 2: Discord Daily Alerts (10 min)

## Step 1: Identify or Create Seedwarden Discord Server

If you have an existing Seedwarden Discord server, proceed to Step 2.

If not, create one:
1. Go to https://discord.com (desktop or web)
2. Click "+" icon in left sidebar (Add a Server)
3. Click "Create My Own" > "For me and my friends"
4. Server name: `Seedwarden Operations`
5. Click "Create"

## Step 2: Create the #analytics-alerts Channel

1. In your Discord server, right-click "Text Channels" category (or click "+" next to it)
2. Click "Create Channel"
3. Channel name: `analytics-alerts`
4. Channel type: Text
5. Description (optional): "Automated daily metrics from etsy_daily_sync.py"
6. Click "Create"

## Step 3: Create the Webhook

1. Right-click `#analytics-alerts` channel
2. Click "Edit Channel"
3. In left menu, click "Integrations"
4. Click "Webhooks"
5. Click "New Webhook"
6. Webhook name: `Seedwarden Analytics`
7. (Optional) Upload the seedwarden_logo_1.png as webhook avatar
8. Click "Copy Webhook URL"
9. Save this URL — you'll need it in Step 4

The webhook URL looks like:
```
https://discord.com/api/webhooks/NUMBERS/ALPHANUMERIC_STRING
```

## Step 4: Store the Webhook URL in .env

In the project root directory (`/home/awank/dev/SuperClaude_Framework`), create or edit the `.env` file:

```bash
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/[PASTE_THE_URL_HERE]
```

**Security**: Confirm `.env` is in `.gitignore` (it should be by default).

## Step 5: Test the Webhook

To verify the webhook works, run the test script:

```bash
cd /home/awank/dev/SuperClaude_Framework
uv run python scripts/discord_daily_alert.py
```

Within 5 seconds, you should see a formatted embed message appear in `#analytics-alerts`.

**If you see an error**:
- 404 Not Found: Webhook URL is wrong or channel was deleted. Go back to Discord, recreate
  the webhook, and copy the URL again.
- 401 Unauthorized: The token in the URL is incorrect. Try a fresh copy.
- No output: Check that `DISCORD_WEBHOOK_URL` is set in `.env` and readable.

## Step 6: Schedule the Cron Job

Both scripts (`etsy_daily_sync.py` and `discord_daily_alert.py`) run on a cron schedule.

Open your crontab:
```bash
crontab -e
```

Add these two lines:
```
0 6  * * * cd /home/awank/dev/SuperClaude_Framework && uv run python scripts/etsy_daily_sync.py >> /tmp/etsy_sync.log 2>&1
0 20 * * * cd /home/awank/dev/SuperClaude_Framework && uv run python scripts/discord_daily_alert.py >> /tmp/discord_alert.log 2>&1
```

**Time explanation**:
- `0 6 * * *` = 06:00 UTC daily (Etsy sync runs first)
- `0 20 * * *` = 20:00 UTC daily (Discord alert runs after data is collected)

Save and exit. Verify:
```bash
crontab -l | grep discord_daily_alert
```

You should see the line you added.

## Step 7: Document the Setup

In WORKLOG.md, add an entry:
```
Discord webhook created [DATE]: #analytics-alerts channel, Seedwarden Operations server.
Webhook URL (redacted): https://discord.com/api/webhooks/[REDACTED]/[REDACTED]
Stored in .env as DISCORD_WEBHOOK_URL.
Test run confirmed [DATE] — embed message appeared in channel.
Cron jobs scheduled: etsy_daily_sync at 06:00 UTC, discord_daily_alert at 20:00 UTC.
```

---

# System 3: GA4 Custom Dimensions & Metrics (15 min)

## Step 1: Verify GA4 Connection to Etsy

1. Go to Etsy Shop Manager > Settings > Options > Web Analytics
2. Confirm a GA4 Measurement ID (looks like `G-XXXXXXXXXX`) is entered
3. Copy this ID — you'll need it later
4. Open a Seedwarden Etsy listing in an incognito browser
5. Go to GA4 > Reports > Real-Time > Events
6. Wait 60 seconds and look for `page_view` events

If no events appear: GA4 is not connected. Re-enter the Measurement ID in Etsy Shop Manager
and wait 5 minutes before retesting.

## Step 2: Create GA4 Custom Dimensions

Navigate to: GA4 Admin (gear icon, bottom left) > Property > Custom Definitions > Custom Dimensions

Click "Create custom dimensions" (you'll create all 5 in one flow or one-by-one):

### Dimension 1: zone_number
| Field | Value |
|-------|-------|
| Dimension name | zone_number |
| Scope | Event |
| Description | Hardiness zone (3–10) from zone card landing page URL parameter |
| Event parameter | zone_number |

Click Save. Note the dimension ID shown — record it in WORKLOG.md.

### Dimension 2: guide_category
| Field | Value |
|-------|-------|
| Dimension name | guide_category |
| Scope | Event |
| Description | Guide type viewed: wild-edibles, medicinal, endangered, seed-saving, preservation |
| Event parameter | guide_category |

### Dimension 3: acquisition_source
| Field | Value |
|-------|-------|
| Dimension name | acquisition_source |
| Scope | Event |
| Description | Traffic source: pinterest, kit, reddit, instagram, direct, etsy-search |
| Event parameter | acquisition_source |

### Dimension 4: buyer_cohort_inferred
| Field | Value |
|-------|-------|
| Dimension name | buyer_cohort_inferred |
| Scope | User |
| Description | Cohort inferred from behavior: forager, prepper, homesteader, gift-buyer |
| User property | buyer_cohort_inferred |

**Note**: Scope is "User" not "Event" for this one.

### Dimension 5: email_campaign_id
| Field | Value |
|-------|-------|
| Dimension name | email_campaign_id |
| Scope | Event |
| Description | Kit email campaign identifier — maps to which email drove the visit |
| Event parameter | email_campaign_id |

## Step 3: Create GA4 Custom Metrics

Navigate to: GA4 Admin > Custom Definitions > Custom Metrics > "Create custom metric"

### Metric 1: Email Signup Rate
| Field | Value |
|-------|-------|
| Metric name | Email Signup Rate |
| Scope | Event |
| Description | Percentage of landing page visitors who complete email signup form |
| Event parameter | email_signup_rate |
| Unit of measurement | Standard |

### Metric 2: Etsy CTR
| Field | Value |
|-------|-------|
| Metric name | Etsy CTR |
| Scope | Event |
| Description | Click-through rate from zone card to Etsy listing |
| Event parameter | etsy_ctr |
| Unit of measurement | Standard |

### Metric 3: Product View Depth
| Field | Value |
|-------|-------|
| Metric name | Product View Depth |
| Scope | Event |
| Description | Number of distinct product pages viewed in session (higher = higher intent) |
| Event parameter | product_view_depth |
| Unit of measurement | Standard |

### Metric 4: Email Open Rate
| Field | Value |
|-------|-------|
| Metric name | Email Open Rate |
| Scope | Event |
| Description | Percentage of Kit emails opened — imported from Kit weekly export |
| Event parameter | email_open_rate |
| Unit of measurement | Standard |

### Metric 5: Social Referral Value
| Field | Value |
|-------|-------|
| Metric name | Social Referral Value |
| Scope | Event |
| Description | Estimated revenue from social-referred sessions that convert to Etsy click |
| Event parameter | social_referral_value |
| Unit of measurement | Currency |

## Step 4: Document All IDs

After creating each dimension and metric, GA4 assigns an internal ID. Go to GA4 Admin > Custom Definitions
and record all IDs in WORKLOG.md:

```
GA4 Custom Dimensions:
  zone_number          — ID: [fill in after creation]
  guide_category       — ID: [fill in]
  acquisition_source   — ID: [fill in]
  buyer_cohort_inferred — ID: [fill in]
  email_campaign_id    — ID: [fill in]

GA4 Custom Metrics:
  Email Signup Rate    — ID: [fill in]
  Etsy CTR             — ID: [fill in]
  Product View Depth   — ID: [fill in]
  Email Open Rate      — ID: [fill in]
  Social Referral Value — ID: [fill in]
```

## Step 5: GA4 Event Tracking Code (Kit Landing Page)

Add this code to the Kit landing page `<head>` section. Replace `G-XXXXXXXXXX` with your
actual GA4 Measurement ID from Step 1:

```html
<!-- GA4 Tracking — Seedwarden Zone Card Landing Page -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');

  // Fire on page load: track zone card landing page visit
  window.addEventListener('load', function() {
    const params = new URLSearchParams(window.location.search);
    const zone = params.get('zone') || 'unknown';
    const source = params.get('utm_source') || 'direct';
    const campaign = params.get('utm_campaign') || 'none';

    gtag('event', 'view_zone_card_landing', {
      'zone_number': zone,
      'acquisition_source': source,
      'email_campaign_id': campaign
    });
  });

  // Call this when email signup form is submitted
  function trackEmailSignup(zone, source) {
    gtag('event', 'email_signup_complete', {
      'zone_number': zone,
      'acquisition_source': source,
      'guide_category': 'zone-card'
    });
  }

  // Call this when visitor clicks through to Etsy
  function trackEtsyClick(productTitle, source) {
    gtag('event', 'etsy_click', {
      'guide_category': productTitle,
      'acquisition_source': source
    });
  }
</script>
```

**In Kit**: Page Builder > Settings > Custom Code > Head Code > Paste the above block.

## Step 6: Create GA4 Audiences (Optional but Recommended)

Navigate to: GA4 Admin > Audiences > "New audience"

### Audience 1: Forager Signal
Name: `Forager Signal`
Condition: User meets ANY of:
- Page path contains "wild-edibles" AND session engagement > 120 seconds
- guide_category dimension = "wild-edibles" in past 30 days
- User viewed 2+ distinct guide pages in one session

### Audience 2: Prepper Signal
Name: `Prepper Signal`
Condition: User meets ANY of:
- Visited a bundle listing page
- Visited 3+ guide pages in one session
- guide_category dimension = "survival"

### Audience 3: High-Value Repeat Candidate
Name: `High-Value Repeat Candidate`
Condition: User meets ALL of:
- First visit 30+ days ago
- Visited listing page 3+ times total
- Average session duration > 90 seconds

### Audience 4: Kit Email Engaged
Name: `Kit Email Engaged`
Condition: User meets ANY of:
- utm_source = "kit" in first session
- Visited landing page with utm_campaign = "lead_magnet"
- Multiple visits from utm_source = "kit"

---

# Verification Checklist (Complete by May 25)

## Google Sheets
- [ ] Sheet created and named "Seedwarden Phase 2 Analytics Dashboard"
- [ ] All 5 tabs present: Daily Metrics, Weekly Summary, Monthly Cohort Performance, KPI Summary, Raw Data Log
- [ ] Daily Metrics: 10 headers (A–J) + 3 derived metric columns (K–M)
- [ ] Date column: 2026-05-30 through 2026-06-30 (32 rows)
- [ ] All formulas in place (AOV, 7-day averages, week-over-week % change)
- [ ] KPI Summary: 7 KPI rows with target/actual/status columns
- [ ] Status column: conditional formatting applied (green/yellow/red)
- [ ] Sheet URL saved in WORKLOG.md

## Discord
- [ ] #analytics-alerts channel created in Discord server
- [ ] Webhook "Seedwarden Analytics" created and authorized
- [ ] Webhook URL stored in .env as DISCORD_WEBHOOK_URL
- [ ] Manual test run completed: `uv run python scripts/discord_daily_alert.py`
- [ ] Test message appeared in #analytics-alerts channel
- [ ] Cron jobs added: both etsy_daily_sync (06:00 UTC) and discord_daily_alert (20:00 UTC)
- [ ] Cron verification: `crontab -l | grep discord_daily_alert` shows entry
- [ ] Webhook URL (redacted) logged in WORKLOG.md

## GA4
- [ ] GA4 Measurement ID confirmed in Etsy Shop Manager
- [ ] Real-Time page_view events confirmed (incognito browser test)
- [ ] All 5 custom dimensions created
- [ ] All 5 custom metrics created
- [ ] All dimension/metric IDs recorded in WORKLOG.md
- [ ] GA4 event tracking code added to Kit landing page
- [ ] (Optional) All 4 audiences created

**If any item unchecked**: Do not proceed to May 30 launch. Tag blockers in WORKLOG.md and
contact user for resolution.

---

# Daily Monitoring Checklist (May 30–June 30)

## Each Morning (06:00–07:00 UTC)
- [ ] Etsy sync script has run (check `/tmp/etsy_sync.log` for no errors)
- [ ] New data rows have appeared in Google Sheets Raw Data Log tab

## Each Evening (20:00–21:00 UTC)
- [ ] Discord alert arrived in #analytics-alerts channel
- [ ] Alert shows today's orders, revenue, and AOV
- [ ] No anomaly flags in the alert (if any, investigate immediately)

## Each Monday Morning
- [ ] Update Weekly Summary tab with week's totals
- [ ] Calculate week-over-week % changes
- [ ] Review KPI Summary status (green/yellow/red)
- [ ] Document any anomalies or wins in WORKLOG.md

## Each Week (Friday EOD)
- [ ] Review all three analytics systems
- [ ] Compare performance to targets (KPI Summary dashboard)
- [ ] Update PROJECTS.md with weekly metrics summary
- [ ] Plan adjustments for following week if needed

---

# Troubleshooting

**Discord webhook 404**: Webhook was deleted or URL is wrong. Recreate webhook in Discord
and update DISCORD_WEBHOOK_URL in .env.

**GA4 shows no Real-Time events**: GA4 Measurement ID not correctly entered in Etsy Shop Manager.
Re-enter and wait 5 minutes.

**Custom dimensions not in GA4 reports**: Newly created dimensions take 24–48 hours to appear
in standard reports. They appear in Real-Time > Event parameters within minutes of first event.

**discord_daily_alert.py reports no data**: etsy_daily_sync.py must run first (at 06:00 UTC).
Confirm both cron jobs exist and CSV file path is correct.

**Formulas in Google Sheets show #REF! errors**: Check that all sheet tab names match exactly
(capitalization matters). Rebuild the formula if needed.

---

# Time Estimate Summary

| System | Setup | Testing | Total |
|--------|-------|---------|-------|
| Google Sheets | 12 min | 3 min | 15 min |
| Discord | 8 min | 2 min | 10 min |
| GA4 | 13 min | 2 min | 15 min |
| **TOTAL** | | | **40 min** |

---

*Sources: TRACK_B_ANALYTICS_SETUP_GOOGLE_SHEETS.md, TRACK_B_ANALYTICS_SETUP_DISCORD_AND_GA4.md.
Consolidated 2026-05-17. All formulas and configuration options copy-verified against source documents.*
