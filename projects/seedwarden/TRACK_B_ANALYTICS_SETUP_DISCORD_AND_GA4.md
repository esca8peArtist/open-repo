---
title: "Track B Analytics Setup — Discord Alerts + GA4 Tracking"
prepared: 2026-05-17
status: production-ready — copy-paste ready for pre-launch setup
source: PHASE_2_ANALYTICS_INFRASTRUCTURE_PRESTAGING.md (Sections 2 and 5)
scope: Discord webhook for daily alerts + GA4 custom dimensions and metrics for May 30 launch
---

# Track B Analytics Setup — Discord Alerts + GA4 Tracking

**Purpose**: Two-part setup guide.
- Part 1: Discord webhook to receive daily Seedwarden metrics alerts
- Part 2: GA4 custom dimensions and metrics for zone card and cohort tracking

**When to complete**: By May 25. Both setups take under 30 minutes combined.

---

# Part 1 — Discord Daily Alerts

## What You Are Building

A Discord channel named `#analytics-alerts` that receives an automated daily summary at
20:00 UTC every day during the May 30–June 30 launch period. The alert is sent by the
`scripts/discord_daily_alert.py` script, which runs on a cron schedule.

**Alert content** (daily, 20:00 UTC):
- Orders today
- Revenue today
- AOV today
- Any anomaly flags (order drop, revenue drop, email unsubscribe spike)

---

## Discord Setup Steps

### Step 1 — Identify or Create the Seedwarden Discord Server

If you have an existing Seedwarden Discord server, use it. If not:

1. Open Discord (desktop or web: https://discord.com)
2. Click the "+" icon in the left sidebar (Add a Server)
3. Click "Create My Own" > "For me and my friends"
4. Server name: "Seedwarden Operations" (or any name — this is private)
5. Click "Create"

### Step 2 — Create the #analytics-alerts Channel

1. In your Discord server, right-click the "Text Channels" category (or click the "+" next to it)
2. Click "Create Channel"
3. Channel type: Text
4. Channel name: `analytics-alerts` (Discord lowercases and removes spaces automatically — type it as shown)
5. Description (optional): "Automated daily metrics from etsy_daily_sync.py + discord_daily_alert.py"
6. Click "Create Channel"

### Step 3 — Create the Webhook

1. Right-click the `#analytics-alerts` channel > "Edit Channel"
2. In the left menu, click "Integrations"
3. Click "Webhooks"
4. Click "New Webhook"
5. Webhook name: `Seedwarden Analytics`
6. (Optional) Upload a small Seedwarden logo as the webhook avatar
7. Click "Copy Webhook URL" — this is the URL you need
8. Click "Save"

The webhook URL looks like this:
```
https://discord.com/api/webhooks/1234567890123456789/abcdefghij_EXAMPLE_TOKEN_HERE
```

### Step 4 — Store the Webhook URL

Add the webhook URL to your `.env` file in the project root:

```
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/[YOUR_ID]/[YOUR_TOKEN]
```

**Security note**: Never commit `.env` to git. Confirm `.env` is in `.gitignore` before saving.

### Step 5 — Test the Webhook

Run the daily alert script manually to confirm the webhook works:

```bash
cd /path/to/seedwarden/project
python3 scripts/discord_daily_alert.py
```

You should see a formatted embed message appear in `#analytics-alerts` within 5 seconds.

If you see an error:
- "404 Not Found": the webhook URL is wrong or the channel was deleted. Re-create the webhook
  and copy the URL again.
- "401 Unauthorized": the token in the URL is incorrect. Go back to Discord > Integrations >
  Webhooks and copy the URL fresh.
- No output at all: check that `DISCORD_WEBHOOK_URL` is set in your `.env` and that the script
  can read it (`import os; print(os.getenv("DISCORD_WEBHOOK_URL"))`)

### Step 6 — Schedule the Cron Job

On Linux/Mac, add the cron entry:

```bash
crontab -e
```

Add this line:
```
0 20 * * * cd /absolute/path/to/project && python3 scripts/discord_daily_alert.py >> /tmp/discord_alert.log 2>&1
```

Replace `/absolute/path/to/project` with the actual path (e.g., `/home/awank/dev/SuperClaude_Framework`).

Save and exit. Verify the cron job is saved:
```bash
crontab -l | grep discord_daily_alert
```

You should see the line you just added. The alert will fire automatically at 20:00 UTC daily
starting May 30.

### Step 7 — Document the Webhook URL

Log the webhook URL (redacted for security) in WORKLOG.md:
```
Discord webhook created [DATE]: #analytics-alerts channel, Seedwarden Operations server.
URL stored in .env as DISCORD_WEBHOOK_URL. Test confirmed [DATE].
```

---

## Monitoring Script Reference

**`scripts/discord_daily_alert.py`**
- Reads from `projects/seedwarden/analytics/data/etsy_orders_YYYY-MM.csv`
- Calculates today's orders, revenue, and AOV
- Sends a Discord embed to DISCORD_WEBHOOK_URL
- Full source code in `PHASE_2_ANALYTICS_INFRASTRUCTURE_PRESTAGING.md` Section 5.2

**`scripts/etsy_daily_sync.py`**
- Pulls yesterday's orders from Etsy API
- Appends rows to the monthly CSV file
- Must run before discord_daily_alert.py each day (run at 06:00 UTC, alert at 20:00 UTC)
- Full source code in `PHASE_2_ANALYTICS_INFRASTRUCTURE_PRESTAGING.md` Section 1.3

**Cron order** (both jobs together in crontab):
```
0 6  * * * cd /absolute/path/to/project && python3 scripts/etsy_daily_sync.py >> /tmp/etsy_sync.log 2>&1
0 20 * * * cd /absolute/path/to/project && python3 scripts/discord_daily_alert.py >> /tmp/discord_alert.log 2>&1
```

---

# Part 2 — Google Analytics 4 (GA4) Setup

## What You Are Building

Custom dimensions and metrics in GA4 that allow tracking of:
- Which hardiness zone card pages drive traffic
- Which cohort (forager, prepper, homesteader) a visitor belongs to
- Email campaign effectiveness
- Key conversion metrics (email signup rate, Etsy click-through rate, etc.)

---

## Prerequisite Verification

Before creating custom dimensions, confirm GA4 is connected to the Seedwarden Etsy shop:

1. Go to Etsy Shop Manager > Settings > Options > Web Analytics
2. Confirm a GA4 Measurement ID (`G-XXXXXXXXXX`) is entered and saved
3. Open a Seedwarden Etsy listing in an incognito/private browser window
4. In GA4 > Reports > Real-Time > Events: wait 60 seconds and confirm `page_view` events appear

If no events appear: the Measurement ID is not correctly connected. Re-enter it in Etsy Shop
Manager and wait 5 minutes before retesting.

---

## GA4 Custom Dimension Setup

Create these 5 custom dimensions in GA4. Each takes about 2 minutes.

**Navigation path**: GA4 Admin (gear icon, bottom left) > Property > Custom Definitions > Custom Dimensions > "Create custom dimensions"

### Custom Dimension 1 — Zone ID

| Field | Value |
|-------|-------|
| Dimension name | zone_number |
| Scope | Event |
| Description | Hardiness zone of the visitor (3–10), derived from zone card landing page URL parameter |
| Event parameter | zone_number |

Click "Save." Note the dimension ID assigned by GA4 (shown in the Custom Dimensions list
after saving) — record it in WORKLOG.md.

### Custom Dimension 2 — Guide Category

| Field | Value |
|-------|-------|
| Dimension name | guide_category |
| Scope | Event |
| Description | Which guide type the visitor viewed: wild-edibles, medicinal, endangered, seed-saving, preservation |
| Event parameter | guide_category |

### Custom Dimension 3 — Acquisition Source

| Field | Value |
|-------|-------|
| Dimension name | acquisition_source |
| Scope | Event |
| Description | Traffic source: pinterest, kit, reddit, instagram, direct, etsy-search |
| Event parameter | acquisition_source |

### Custom Dimension 4 — Buyer Cohort (Inferred)

| Field | Value |
|-------|-------|
| Dimension name | buyer_cohort_inferred |
| Scope | User |
| Description | High-level cohort signal inferred from browsing behavior: forager, prepper, homesteader, gift-buyer |
| User property | buyer_cohort_inferred |

Note: Scope is "User" not "Event" for this dimension.

### Custom Dimension 5 — Email Campaign ID

| Field | Value |
|-------|-------|
| Dimension name | email_campaign_id |
| Scope | Event |
| Description | Kit email campaign identifier — maps to which email in the welcome sequence drove the visit |
| Event parameter | email_campaign_id |

---

## GA4 Custom Metrics Setup

Create these 5 custom metrics. Path: GA4 Admin > Custom Definitions > Custom Metrics > "Create custom metric"

### Custom Metric 1 — Email Signup Rate

| Field | Value |
|-------|-------|
| Metric name | Email Signup Rate |
| Scope | Event |
| Description | Percentage of landing page visitors who complete the email signup form |
| Event parameter | email_signup_rate |
| Unit of measurement | Standard |

### Custom Metric 2 — Etsy CTR

| Field | Value |
|-------|-------|
| Metric name | Etsy CTR |
| Scope | Event |
| Description | Click-through rate from zone card landing page to Etsy listing |
| Event parameter | etsy_ctr |
| Unit of measurement | Standard |

### Custom Metric 3 — Product View Depth

| Field | Value |
|-------|-------|
| Metric name | Product View Depth |
| Scope | Event |
| Description | Number of distinct product/listing pages viewed in a single session — higher values indicate higher purchase intent |
| Event parameter | product_view_depth |
| Unit of measurement | Standard |

### Custom Metric 4 — Email Open Rate

| Field | Value |
|-------|-------|
| Metric name | Email Open Rate |
| Scope | Event |
| Description | Percentage of Kit emails opened — imported from Kit weekly export data |
| Event parameter | email_open_rate |
| Unit of measurement | Standard |

### Custom Metric 5 — Social Referral Value

| Field | Value |
|-------|-------|
| Metric name | Social Referral Value |
| Scope | Event |
| Description | Estimated revenue value of social-referred sessions (sessions originating from Instagram, TikTok, or Pinterest that convert to Etsy click) |
| Event parameter | social_referral_value |
| Unit of measurement | Currency |

---

## Document All Custom Dimension and Metric IDs

After creating each dimension and metric, GA4 assigns an internal ID (visible in the Custom
Definitions list). These IDs are needed when implementing the GA4 tracking code.

Record these IDs in WORKLOG.md immediately after creation:

```
GA4 Custom Dimensions:
  zone_number          — ID: [fill in]
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

---

## GA4 Event Tracking Code (Kit Landing Page)

Add this code to the `<head>` section of the Kit zone card landing page. This fires the
custom dimension events when a visitor lands on the page.

Replace `G-XXXXXXXXXX` with the actual GA4 Measurement ID:

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

**How to add to Kit page**: Kit landing pages allow custom HTML/CSS injection. In Kit:
Page Builder > Settings > Custom Code > Head Code > paste the above block.

---

## GA4 Audience Setup (4 Cohort Segments)

After creating custom dimensions, set up these 4 audiences. Path: GA4 Admin > Audiences > "New audience"

### Audience 1 — Forager Signal
Name: "Forager Signal"
Condition: User meets ANY of:
- Page path contains "wild-edibles" AND session engagement time > 120 seconds
- guide_category dimension = "wild-edibles" in past 30 days
- User viewed 2+ distinct guide pages in a single session

### Audience 2 — Prepper Signal
Name: "Prepper Signal"
Condition: User meets ANY of:
- Visited a bundle listing page
- Visited 3+ guide pages in a single session
- guide_category dimension = "survival" in any event

### Audience 3 — High-Value Repeat Candidate
Name: "High-Value Repeat Candidate"
Condition: User meets ALL of:
- First visit 30+ days ago
- Visited a listing page 3+ times total
- Average session duration > 90 seconds

### Audience 4 — Kit Email Engaged
Name: "Kit Email Engaged"
Condition: User meets ANY of:
- utm_source = "kit" in first session
- Visited landing page with utm_campaign = "lead_magnet"
- Multiple visits from utm_source = "kit"

---

## Setup Verification Checklist

Complete this before May 30:

**Discord**:
- [ ] #analytics-alerts channel created in Discord server
- [ ] Webhook URL created, named "Seedwarden Analytics"
- [ ] Webhook URL stored in .env as DISCORD_WEBHOOK_URL
- [ ] Manual test: discord_daily_alert.py ran without error, message appeared in channel
- [ ] Cron job scheduled: `crontab -l | grep discord_daily_alert` shows entry
- [ ] Webhook URL (redacted) logged in WORKLOG.md

**GA4**:
- [ ] GA4 Measurement ID confirmed in Etsy Shop Manager Web Analytics
- [ ] Real-time page_view events confirmed (incognito browser test)
- [ ] All 5 custom dimensions created (zone_number, guide_category, acquisition_source, buyer_cohort_inferred, email_campaign_id)
- [ ] All 5 custom metrics created (Email Signup Rate, Etsy CTR, Product View Depth, Email Open Rate, Social Referral Value)
- [ ] All dimension/metric IDs recorded in WORKLOG.md
- [ ] GA4 event code added to Kit landing page HTML (verify by viewing page source, search for `gtag('event'`)
- [ ] All 4 audiences created (Forager Signal, Prepper Signal, High-Value Repeat Candidate, Kit Email Engaged)

---

## Troubleshooting Reference

**Discord webhook 404 error**: Channel or webhook was deleted. Re-create webhook in Discord channel settings and update DISCORD_WEBHOOK_URL in .env.

**GA4 shows no Real-Time events**: GA4 Measurement ID not entered in Etsy Shop Manager, or wrong ID. Check Etsy Shop Manager > Settings > Options > Web Analytics.

**Custom dimensions not appearing in GA4 reports**: Newly created dimensions take 24–48 hours to populate in standard reports. They will appear in Real-Time > Event parameters within minutes of the first event firing.

**discord_daily_alert.py reports no data**: The etsy_daily_sync.py script must run first (at 06:00 UTC) to populate the CSV before the alert script reads it at 20:00 UTC. Confirm both cron jobs exist and that the CSV file is being written to the correct path.

Full troubleshooting for all systems: `PHASE_2_ANALYTICS_INFRASTRUCTURE_PRESTAGING.md` Appendix A.

---

*Source: PHASE_2_ANALYTICS_INFRASTRUCTURE_PRESTAGING.md Sections 2 and 5. Prepared 2026-05-17.*
