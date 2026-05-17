---
title: "Track B Analytics Implementation Checklist — Step-by-Step Execution"
prepared: 2026-05-17
status: production-ready — execute each section in <15 min per platform
deadline: Complete by May 25 (all 3 platforms)
sources:
  - TRACK_B_ANALYTICS_SETUP_GOOGLE_SHEETS.md (full Google Sheets setup guide)
  - TRACK_B_ANALYTICS_SETUP_DISCORD_AND_GA4.md (Discord + GA4 setup guide)
  - PHASE_2_ANALYTICS_INFRASTRUCTURE_PRESTAGING.md (script source code)
---

# Track B Analytics Implementation Checklist

**Purpose**: Break down the three analytics setup guides into timed, step-by-step
implementation blocks. Each section is designed to complete in under 15 minutes.
Total time across all three platforms: 40–50 minutes.

**Execution order**:
1. Google Sheets — 15 min (do first, no prerequisites)
2. Discord Webhook — 10 min (do second, requires Discord account)
3. GA4 Custom Dimensions — 15 min (do last, requires GA4 already linked to Etsy)

**Hard deadline**: All three complete by May 25. GA4 custom dimensions need 24–48 hours
to begin populating in standard reports — set up by May 25, not May 28.

---

# Section 1 — Google Sheets Dashboard (15 min)

**Direct URL**: https://sheets.google.com
**Account**: Log in with wanka95@gmail.com
**End result**: 1 spreadsheet, 5 tabs, formulas loaded, shared

---

## Step 1.1 — Create and Name the Sheet (1 min)

1. Go to https://sheets.google.com
2. Click the "+" (Blank) button
3. Click "Untitled spreadsheet" at the top
4. Type exactly: `Seedwarden Phase 2 Analytics Dashboard`
5. Press Enter

Checkpoint: Tab bar at bottom shows "Sheet1"

---

## Step 1.2 — Create All 5 Tabs (2 min)

1. Right-click "Sheet1" at the bottom > Rename > type `Daily Metrics` > press Enter
2. Click the "+" icon at the bottom right > new tab appears > rename it `Weekly Summary`
3. Click "+" again > rename > `Monthly Cohort Performance`
4. Click "+" again > rename > `KPI Summary`
5. Click "+" again > rename > `Raw Data Log`

Checkpoint: 5 tabs visible at bottom in this order: Daily Metrics | Weekly Summary | Monthly Cohort Performance | KPI Summary | Raw Data Log

---

## Step 1.3 — Daily Metrics Column Headers (2 min)

Click the "Daily Metrics" tab. Click cell A1. Enter each header — press Tab to move right:

Copy-paste this into A1 (paste as plain text — Google Sheets will split by tab):

| Cell | Type this |
|------|-----------|
| A1 | Date |
| B1 | Etsy Orders |
| C1 | Etsy Revenue ($) |
| D1 | TikTok Views |
| E1 | TikTok Engagement |
| F1 | Instagram Reach |
| G1 | Instagram Engagement |
| H1 | Pinterest Impressions |
| I1 | Email Subscribers (total) |
| J1 | Notes |

After entering headers:
- Select Row 1 (click the "1" row number on the left)
- Click Format > Text > Bold
- Click View > Freeze > 1 row

Checkpoint: Row 1 is bold, frozen, shows 10 column headers

---

## Step 1.4 — Date Column (2 min)

Click cell A2. Type:
```
2026-05-30
```
Press Enter.

Click cell A3. Type:
```
=A2+1
```
Press Enter.

Click cell A3 again. Press Ctrl+C (copy).
Click cell A4. Hold Shift and click cell A33. Press Ctrl+V (paste).

Format the date column:
- Select A2:A33 (click A2, hold Shift, click A33)
- Format > Number > More Formats > More date and time formats
- Type: `YYYY-MM-DD` in the format box > Apply

Checkpoint: A2 = 2026-05-30, A33 = 2026-06-30 (32 rows of dates)

---

## Step 1.5 — Derived Metric Formulas (3 min)

**Column K — Average Order Value**

Click cell K1. Type: `AOV (Avg Order Value)` > press Enter

Click cell K2. Copy-paste this formula:
```
=IF(B2>0, C2/B2, 0)
```
Press Enter. Click K2 again. Copy (Ctrl+C). Select K3:K33. Paste (Ctrl+V).

**Column L — TikTok 7-Day Rolling Average**

Click cell L1. Type: `TikTok 7-Day Avg` > press Enter

Click cell L2. Copy-paste:
```
=IF(ROW()-1<7, AVERAGE($D$2:D2), AVERAGE(D2:OFFSET(D2,-6,0)))
```
Press Enter. Copy L2. Select L3:L33. Paste.

**Column M — Email Subs 7-Day Rolling Average**

Click cell M1. Type: `Email Subs 7-Day Avg` > press Enter

Click cell M2. Copy-paste:
```
=IF(ROW()-1<7, AVERAGE($I$2:I2), AVERAGE(I2:OFFSET(I2,-6,0)))
```
Press Enter. Copy M2. Select M3:M33. Paste.

Checkpoint: Columns K, L, M have headers and formulas down to row 33. Cells show "0" (expected — no data yet)

---

## Step 1.6 — KPI Summary Tab (3 min)

Click the "KPI Summary" tab.

**Row 1**: Click A1. Type: `SEEDWARDEN PHASE 2 — KPI SUMMARY`
- Select A1:F1 > Format > Merge cells > Merge all
- Format > Text > Bold, 14pt font

**Row 2**: Click A2. Type: `Period: May 30 – June 30, 2026`

**Row 4 — Table headers** (click A4 and enter each, Tab to move right):
```
METRIC    TARGET    ACTUAL    STATUS
```

**Rows 5–11 — KPI rows** (enter manually in Column A):

| Row | A (Metric) | B (Target) |
|-----|------------|------------|
| 5 | Total Orders (31 days) | 40–60 |
| 6 | Total Revenue (31 days) | $1,000–$1,500 |
| 7 | Email Subscribers Gained | 100–150 |
| 8 | Avg Daily Orders | 1.5–2.0/day |
| 9 | Email Open Rate | 35%+ |
| 10 | TikTok 7-Day Avg Views | 500+ |
| 11 | Pinterest Impressions (total) | 10,000+ |

**Column C (Actual) formulas** — click each cell and paste:

C5:
```
=SUM('Daily Metrics'!B2:B33)
```

C6:
```
=SUM('Daily Metrics'!C2:C33)
```

C8:
```
=IFERROR(SUM('Daily Metrics'!B2:B33)/COUNTA('Daily Metrics'!A2:A33),0)
```

C10:
```
=IFERROR(OFFSET('Daily Metrics'!L2, COUNTA('Daily Metrics'!A2:A33)-1, 0), 0)
```

C11:
```
=SUM('Daily Metrics'!H2:H33)
```

Note: C7 and C9 are manual entry (email stats come from Kit and are entered weekly).

**Column D (Status) formulas**:

D5:
```
=IF(C5>=40, "ON TRACK", IF(C5>=25, "WATCH", "BEHIND"))
```

D6:
```
=IF(C6>=1000, "ON TRACK", IF(C6>=600, "WATCH", "BEHIND"))
```

D7:
```
=IF(C7>=100, "ON TRACK", IF(C7>=60, "WATCH", "BEHIND"))
```

**Conditional formatting on D5:D11**:
- Select D5:D11
- Format > Conditional formatting
- Rule 1: "Text contains" `ON TRACK` > fill: light green (#B7E1CD)
- Click "Add another rule" > "Text contains" `WATCH` > fill: light yellow (#FFEEBA)
- Click "Add another rule" > "Text contains" `BEHIND` > fill: light red (#F4CCCC)
- Click Done

Checkpoint: KPI Summary shows 7 metric rows, targets, formula cells, and color-coded status column

---

## Step 1.7 — Raw Data Log Tab Headers (1 min)

Click the "Raw Data Log" tab. Click A1. Enter these headers (Tab between each):

```
created_date    receipt_id    transaction_id    listing_title    quantity    price_usd    total_price_usd    coupon_code    buyer_country
```

Checkpoint: 9 headers in Row 1 of Raw Data Log tab

---

## Step 1.8 — Share the Sheet (1 min)

1. Click "Share" (top right, blue button)
2. In "Add people and groups" field: type `wanka95@gmail.com` > set role to "Editor" > click Send
3. Click "Change to anyone with the link" under "General access" > set to "Viewer"
4. Click "Copy link"
5. Save the URL in WORKLOG.md under "Analytics: Google Sheets Dashboard URL"

Checkpoint: Sheet shared with wanka95@gmail.com (Editor) and link copied

---

## Google Sheets Complete Checklist

- [ ] Sheet created: "Seedwarden Phase 2 Analytics Dashboard"
- [ ] 5 tabs: Daily Metrics, Weekly Summary, Monthly Cohort Performance, KPI Summary, Raw Data Log
- [ ] Daily Metrics: 10 headers (A–J), date column A2:A33 (2026-05-30 to 2026-06-30), AOV/7-day avg formulas in K–M
- [ ] KPI Summary: 7 metric rows, target column, actual formulas, status formulas, conditional formatting
- [ ] Raw Data Log: 9 headers matching etsy_daily_sync.py output
- [ ] Shared with wanka95@gmail.com (Editor), link-sharing enabled (Viewer)
- [ ] URL saved in WORKLOG.md

**Time to complete Steps 1.1–1.8**: 15 minutes

---

# Section 2 — Discord Webhook (10 min)

**Platform URL**: https://discord.com
**End result**: #analytics-alerts channel live, webhook URL stored in .env, manual test passed

---

## Step 2.1 — Create or Access Discord Server (2 min)

If you already have a Discord server to use, skip to Step 2.2.

1. Go to https://discord.com (or open the desktop app)
2. Click the "+" icon in the left sidebar
3. Click "Create My Own" > "For me and my friends"
4. Server name: `Seedwarden Operations`
5. Click "Create"

Checkpoint: Server appears in left sidebar

---

## Step 2.2 — Create #analytics-alerts Channel (1 min)

1. In your Discord server, click the "+" icon next to "Text Channels"
2. Channel type: Text
3. Channel name: `analytics-alerts` (lowercase, no spaces — Discord applies this automatically)
4. Click "Create Channel"

Checkpoint: `#analytics-alerts` appears under Text Channels

---

## Step 2.3 — Create the Webhook (2 min)

1. Right-click `#analytics-alerts` > "Edit Channel"
2. In the left sidebar of the channel settings, click "Integrations"
3. Click "Webhooks"
4. Click "New Webhook"
5. Webhook name: `Seedwarden Analytics`
6. Click "Copy Webhook URL" (saves it to clipboard)
7. Click "Save"

The URL format looks like:
```
https://discord.com/api/webhooks/1234567890123456789/abcdefghij_TOKEN_HERE
```

Checkpoint: Webhook URL is in your clipboard — paste it somewhere temporary before proceeding

---

## Step 2.4 — Store Webhook URL in .env (2 min)

Open the project .env file (or create it if it does not exist):
Path: `/home/awank/dev/SuperClaude_Framework/.env`

Add this line (replace with your actual webhook URL):
```
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/[YOUR_ID]/[YOUR_TOKEN]
```

Verify `.env` is in `.gitignore`:
```bash
grep ".env" /home/awank/dev/SuperClaude_Framework/.gitignore
```
Expected output: `.env` or `*.env`

If `.env` is NOT in `.gitignore`: add it before saving. The webhook token must not be committed.

Checkpoint: .env file contains DISCORD_WEBHOOK_URL line, .env is in .gitignore

---

## Step 2.5 — Manual Test (2 min)

Run the test from the project root:
```bash
cd /home/awank/dev/SuperClaude_Framework && uv run python scripts/discord_daily_alert.py
```

Expected result: A formatted embed message appears in `#analytics-alerts` within 5 seconds.

Troubleshooting:
- "404 Not Found": webhook URL is wrong or channel was deleted — re-create webhook, copy URL fresh
- "401 Unauthorized": token in URL is incorrect — go to Discord > Channel Settings > Integrations > Webhooks, copy URL again
- No output: run `uv run python -c "import os; print(os.getenv('DISCORD_WEBHOOK_URL'))"` to confirm the .env variable is loading

Checkpoint: Message appears in #analytics-alerts

---

## Step 2.6 — Schedule the Cron Jobs (1 min)

Open crontab:
```bash
crontab -e
```

Add these two lines (replace path with actual project path):
```
0 6  * * * cd /home/awank/dev/SuperClaude_Framework && uv run python scripts/etsy_daily_sync.py >> /tmp/etsy_sync.log 2>&1
0 20 * * * cd /home/awank/dev/SuperClaude_Framework && uv run python scripts/discord_daily_alert.py >> /tmp/discord_alert.log 2>&1
```

Save and exit. Verify:
```bash
crontab -l | grep discord_daily_alert
```
Expected: the 20:00 line appears

Checkpoint: Both cron jobs visible with `crontab -l`

---

## Step 2.7 — Log in WORKLOG.md (30 sec)

Add this entry to `projects/seedwarden/WORKLOG.md`:
```
Discord analytics webhook created [DATE]: #analytics-alerts channel in Seedwarden Operations server.
Webhook name: Seedwarden Analytics. URL stored in .env as DISCORD_WEBHOOK_URL. Manual test passed [DATE].
Cron jobs scheduled: etsy_daily_sync.py at 06:00 UTC, discord_daily_alert.py at 20:00 UTC.
```

---

## Discord Complete Checklist

- [ ] Seedwarden Operations Discord server exists (or existing server used)
- [ ] `#analytics-alerts` channel created (Text type)
- [ ] Webhook created: name "Seedwarden Analytics", URL copied
- [ ] DISCORD_WEBHOOK_URL added to .env file
- [ ] .env confirmed in .gitignore (not committed to git)
- [ ] Manual test passed: message appeared in #analytics-alerts
- [ ] Cron jobs scheduled: etsy_daily_sync 06:00 UTC, discord_daily_alert 20:00 UTC
- [ ] WORKLOG.md entry added (redacted URL)

**Time to complete Steps 2.1–2.7**: 10 minutes

---

# Section 3 — GA4 Custom Dimensions and Metrics (15 min)

**Direct URL**: https://analytics.google.com
**Account**: Log in with wanka95@gmail.com
**End result**: 5 custom dimensions, 5 custom metrics, 4 audiences, GA4 code snippet ready

---

## Step 3.1 — Verify GA4 is Connected to Etsy (2 min)

1. Go to Etsy Shop Manager: https://www.etsy.com/your/account/
2. Navigate: Settings > Options > Web Analytics
3. Confirm your GA4 Measurement ID (`G-XXXXXXXXXX`) is present and saved

**Incognito test** (30 sec):
1. Open a private/incognito browser window
2. Navigate to any live Seedwarden Etsy listing URL
3. In GA4 (regular window): Reports > Real-time > Events
4. Wait 60 seconds — confirm `page_view` events appear

If no events appear: the Measurement ID is not connected. Re-enter it in Etsy Shop Manager
and wait 5 minutes before retesting. Do not proceed to Steps 3.2–3.4 until this test passes.

Checkpoint: page_view events visible in GA4 Real-time within 60 sec of visiting listing

---

## Step 3.2 — Create 5 Custom Dimensions (6 min — ~70 sec each)

**Navigation path**: GA4 Admin (gear icon, bottom left) > Property column > Custom Definitions > Custom Dimensions > "Create custom dimension"

Create each dimension using the values in the table below. After saving each, GA4 shows
a confirmation — note the assigned ID in WORKLOG.md.

**Dimension 1 — Zone Number**

| Field | Value |
|-------|-------|
| Dimension name | zone_number |
| Scope | Event |
| Description | Hardiness zone of visitor (3–10), from zone card landing page URL parameter |
| Event parameter | zone_number |

Click Save.

**Dimension 2 — Guide Category**

| Field | Value |
|-------|-------|
| Dimension name | guide_category |
| Scope | Event |
| Description | Guide type: wild-edibles, medicinal, endangered, seed-saving, preservation |
| Event parameter | guide_category |

Click Save.

**Dimension 3 — Acquisition Source**

| Field | Value |
|-------|-------|
| Dimension name | acquisition_source |
| Scope | Event |
| Description | Traffic source: pinterest, kit, reddit, instagram, direct, etsy-search |
| Event parameter | acquisition_source |

Click Save.

**Dimension 4 — Buyer Cohort (Inferred)**

| Field | Value |
|-------|-------|
| Dimension name | buyer_cohort_inferred |
| Scope | User (not Event — use the dropdown) |
| Description | Cohort inferred from browsing: forager, prepper, homesteader, gift-buyer |
| User property | buyer_cohort_inferred |

Click Save.

**Dimension 5 — Email Campaign ID**

| Field | Value |
|-------|-------|
| Dimension name | email_campaign_id |
| Scope | Event |
| Description | Kit email campaign ID — maps email in welcome sequence to the visit |
| Event parameter | email_campaign_id |

Click Save.

Checkpoint: Custom Definitions > Custom Dimensions list shows 5 entries

Record dimension IDs in WORKLOG.md (copy from the Custom Dimensions list):
```
GA4 Custom Dimensions created [DATE]:
  zone_number          — ID: [fill in after creation]
  guide_category       — ID: [fill in]
  acquisition_source   — ID: [fill in]
  buyer_cohort_inferred — ID: [fill in]
  email_campaign_id    — ID: [fill in]
```

---

## Step 3.3 — Create 5 Custom Metrics (5 min — ~60 sec each)

**Navigation path**: GA4 Admin > Property > Custom Definitions > Custom Metrics > "Create custom metric"

**Metric 1 — Email Signup Rate**

| Field | Value |
|-------|-------|
| Metric name | Email Signup Rate |
| Scope | Event |
| Description | % of landing page visitors who complete the email signup form |
| Event parameter | email_signup_rate |
| Unit of measurement | Standard |

Click Save.

**Metric 2 — Etsy CTR**

| Field | Value |
|-------|-------|
| Metric name | Etsy CTR |
| Scope | Event |
| Description | Click-through rate from zone card landing page to Etsy listing |
| Event parameter | etsy_ctr |
| Unit of measurement | Standard |

Click Save.

**Metric 3 — Product View Depth**

| Field | Value |
|-------|-------|
| Metric name | Product View Depth |
| Scope | Event |
| Description | Number of distinct product pages viewed in a single session |
| Event parameter | product_view_depth |
| Unit of measurement | Standard |

Click Save.

**Metric 4 — Email Open Rate**

| Field | Value |
|-------|-------|
| Metric name | Email Open Rate |
| Scope | Event |
| Description | % of Kit emails opened — imported from Kit weekly export data |
| Event parameter | email_open_rate |
| Unit of measurement | Standard |

Click Save.

**Metric 5 — Social Referral Value**

| Field | Value |
|-------|-------|
| Metric name | Social Referral Value |
| Scope | Event |
| Description | Estimated revenue from social-referred sessions converting to Etsy click |
| Event parameter | social_referral_value |
| Unit of measurement | Currency |

Click Save.

Checkpoint: Custom Metrics list shows 5 entries

Record metric IDs in WORKLOG.md:
```
GA4 Custom Metrics created [DATE]:
  Email Signup Rate    — ID: [fill in]
  Etsy CTR             — ID: [fill in]
  Product View Depth   — ID: [fill in]
  Email Open Rate      — ID: [fill in]
  Social Referral Value — ID: [fill in]
```

---

## Step 3.4 — GA4 Event Tracking Code for Kit Landing Page (2 min)

Copy the code block below. In Kit: Page Builder > Settings > Custom Code > Head Code > paste entire block.

Replace `G-XXXXXXXXXX` with your actual GA4 Measurement ID (find it in GA4 Admin > Property Settings > Measurement ID).

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

**Verification**: After adding to Kit page, view the page source in a browser (Ctrl+U or Cmd+U).
Search for `gtag('event'`. Confirm the block appears in the `<head>` section.

Checkpoint: Code block added to Kit landing page head, visible in page source

---

## Step 3.5 — Create 4 GA4 Audiences (5 min — ~75 sec each)

**Navigation path**: GA4 Admin > Property > Audiences > "New audience"

**Audience 1 — Forager Signal**
Name: `Forager Signal`
Build condition (AND/OR logic in GA4 audience builder):
- Condition: User meets ANY of these:
  - Page path contains `wild-edibles` AND Session engagement time > 120 (seconds)
  - Event: guide_category = `wild-edibles` (in past 30 days)
  - Event count: page_view where page_path contains "guide" > 2 per session

Click Save and Publish.

**Audience 2 — Prepper Signal**
Name: `Prepper Signal`
Condition: User meets ANY of these:
  - Page path contains `bundle` or `survival`
  - Event count: page_view on distinct guide pages > 3 per session
  - Event: guide_category = `survival`

Click Save and Publish.

**Audience 3 — High-Value Repeat Candidate**
Name: `High-Value Repeat Candidate`
Condition: User meets ALL of these:
  - First visit: more than 30 days ago
  - Session count: 3 or more total
  - Average session duration: greater than 90 seconds

Click Save and Publish.

**Audience 4 — Kit Email Engaged**
Name: `Kit Email Engaged`
Condition: User meets ANY of these:
  - First touch: utm_source = `kit`
  - Event: Page path contains `utm_campaign=lead_magnet`
  - Session count from utm_source = `kit`: 2 or more

Click Save and Publish.

Checkpoint: Audiences list shows 4 entries (plus any GA4 default audiences)

---

## GA4 Complete Checklist

- [ ] GA4 Measurement ID confirmed in Etsy Shop Manager > Web Analytics
- [ ] Real-time page_view events confirmed (incognito browser test, 60 sec wait)
- [ ] 5 custom dimensions created: zone_number, guide_category, acquisition_source, buyer_cohort_inferred, email_campaign_id
- [ ] 5 custom metrics created: Email Signup Rate, Etsy CTR, Product View Depth, Email Open Rate, Social Referral Value
- [ ] All 10 dimension/metric IDs recorded in WORKLOG.md
- [ ] GA4 event code added to Kit landing page head section
- [ ] Kit landing page source verified: `gtag('event'` block present in `<head>`
- [ ] 4 audiences created: Forager Signal, Prepper Signal, High-Value Repeat Candidate, Kit Email Engaged

**Time to complete Steps 3.1–3.5**: 15 minutes

---

# Section 4 — Weekly Operations: Reading the Analytics (5 min/week)

**When**: Every Monday morning, 5–10 minutes.

## Monday Morning Analytics Review Procedure

**Google Sheets** (3 min):
1. Open "Seedwarden Phase 2 Analytics Dashboard" > Daily Metrics tab
2. Enter previous week's data for rows corresponding to that week's dates:
   - Column B (Etsy Orders): pull from Etsy Shop Manager > Stats > Orders
   - Column C (Etsy Revenue): pull from Etsy Shop Manager > Stats > Revenue
   - Column D (TikTok Views): pull from TikTok Studio > Analytics > Video Views
   - Column F (Instagram Reach): pull from Instagram Insights > Reach
   - Column H (Pinterest Impressions): pull from Pinterest Analytics > Impressions
   - Column I (Email Subscribers): pull from Kit > Subscribers > Total count
3. Switch to KPI Summary tab — review color-coded status column. Any "BEHIND" flags need action.

**Discord** (1 min):
- Scroll through `#analytics-alerts` for the past week
- Flag any days with zero orders (should trigger investigation)

**Kit** (1 min):
- Kit > Reports > Sequences > "Seedwarden Welcome" > Open Rate
- Enter this value in Google Sheets KPI Summary C9 (Email Open Rate row)
- Target: 35%+. Below 30%: check sender domain SPF/DKIM. Below 20%: check spam score.

---

## Troubleshooting Reference

**Discord 404 error**: Webhook was deleted. Re-create in Discord channel settings, update .env.

**GA4 no Real-Time events**: Measurement ID missing or wrong in Etsy Shop Manager. Re-enter.

**Custom dimensions not in reports**: Newly created dimensions take 24–48 hours to populate
in standard reports. They appear in Real-Time > Event parameters within minutes of first event.

**discord_daily_alert.py shows no data**: etsy_daily_sync.py must run first (06:00 UTC cron).
Check that the CSV path is correct: `projects/seedwarden/analytics/data/etsy_orders_YYYY-MM.csv`.
Verify the CSV exists: `ls /home/awank/dev/SuperClaude_Framework/projects/seedwarden/analytics/data/`

**Google Sheets formula errors (#REF!, #VALUE!)**: Usually caused by pasting the formula without
selecting the correct cell first. Delete the cell content and re-paste the formula from this file.

**Cron job not running**: Run `crontab -l` to verify entries exist. Run `grep discord /tmp/discord_alert.log`
to see last run output. If log is empty, cron has not fired yet — verify system time with `date -u`.

---

*Sources: TRACK_B_ANALYTICS_SETUP_GOOGLE_SHEETS.md (full Sheets guide),
TRACK_B_ANALYTICS_SETUP_DISCORD_AND_GA4.md (Discord + GA4 guide).
Condensed into step-by-step timed blocks on 2026-05-17. Target: <15 min per platform.*
