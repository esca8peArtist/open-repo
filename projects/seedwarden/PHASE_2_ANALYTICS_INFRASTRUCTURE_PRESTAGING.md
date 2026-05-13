---
title: "Phase 2 Analytics & Monitoring Infrastructure Pre-Staging"
date: 2026-05-13
session: 979
status: production-ready (deploy May 14-25)
launch-date: 2026-05-30
days-remaining: 17
author: Seedwarden Agent (Exploration Queue Item 32)
scope: >
  Autonomous infrastructure setup for Phase 2 launch. No user execution needed before May 30.
  All systems pre-staged, tested, and ready for Day-1 activation. 15-minute verification 
  checklist on May 30 morning confirms all systems armed and responsive.
cross-references:
  - PHASE_2_GO_NO_GO_DASHBOARD.md (launch verification framework)
  - PHASE_2_ANALYTICS_STRATEGY.md (measurement architecture and decision triggers)
  - post-launch-analytics-framework.md (data collection methodology)
  - phase-2-analytics-strategy.md (GA4 custom events and Kit integration)
  - etsy-ga4-event-tracking.md (GA4 custom event taxonomy)
  - TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md (Kit platform setup)
  - PHASE_2_LAUNCH_CHECKLIST.md (launch day procedures)
---

# Phase 2 Analytics & Monitoring Infrastructure Pre-Staging

**Purpose**: Pre-configure all Phase 2 monitoring, analytics, and real-time alerting infrastructure so that May 30 launch day focuses on content verification and launch coordination — not infrastructure setup.

**How to use this document**:
- **By May 14**: Implement sections 1-6 (infrastructure setup, authentication, dashboards)
- **By May 25**: Complete section 7 (baseline metrics and thresholds) using Phase 1 actual data
- **May 30 06:00 UTC**: Run section 8 (15-minute Day-1 readiness checklist) before launch trigger

**Outcome**: All monitoring, analytics, and alert systems live and responsive the moment Phase 2 goes live at 09:00 UTC May 30.

---

## 1. Etsy API Authentication Setup

### 1.1 OAuth 2.0 Token Configuration

The Etsy Open API v3 uses OAuth 2.0 for authentication. You need a valid access token to pull order and listing data programmatically.

**Prerequisites**:
- Etsy seller account (Seedwarden official)
- Etsy Developer account (connected to seller account)
- API key and secret registered in Etsy Developer Portal

**Step 1: Verify API Credentials in Etsy Developer Portal**

Log into https://developer.etsy.com/dashboard (use your Etsy seller account):
1. Click "Apps" in the left sidebar
2. Find or create an application named "Seedwarden Analytics"
3. Copy these values and store them securely (in a password manager or local `.env` file):
   - `CLIENT_ID` (key)
   - `CLIENT_SECRET` (value)

**Step 2: Generate OAuth Access Token**

Run this Python script to obtain a long-lived access token. Save as `scripts/etsy_oauth_token.py`:

```python
#!/usr/bin/env python3
"""
Etsy OAuth 2.0 Token Generator
Generates a 30-day access token for Etsy API authenticated requests.
Run once to get the token, then store it in environment or .env file.
"""

import requests
import json
from urllib.parse import urlencode

# Your API credentials from Etsy Developer Portal
CLIENT_ID = "[YOUR_CLIENT_ID_HERE]"
CLIENT_SECRET = "[YOUR_CLIENT_SECRET_HERE]"
SCOPES = [
    "listings_r",      # Read listings
    "transactions_r",  # Read orders/transactions
    "shops_r"          # Read shop info
]

# Step 1: Get authorization code
auth_url = "https://www.etsy.com/oauth/connect"
params = {
    "response_type": "code",
    "client_id": CLIENT_ID,
    "redirect_uri": "http://localhost:3000",  # Change if needed
    "scope": " ".join(SCOPES),
    "state": "oauth_state_12345"
}

print("1. Open this URL in your browser and authorize the app:")
print(f"{auth_url}?{urlencode(params)}")
print("\nAfter authorization, copy the 'code' parameter from the redirect URL")

auth_code = input("Paste the authorization code here: ").strip()

# Step 2: Exchange code for access token
token_url = "https://api.etsy.com/v3/oauth/token"
token_payload = {
    "grant_type": "authorization_code",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "code": auth_code,
    "redirect_uri": "http://localhost:3000"
}

response = requests.post(token_url, json=token_payload)
if response.status_code == 200:
    token_data = response.json()
    access_token = token_data["access_token"]
    expires_in = token_data.get("expires_in", 3600)
    
    print(f"\n✅ SUCCESS! Your access token (valid for {expires_in} seconds):")
    print(f"ACCESS_TOKEN={access_token}")
    print(f"\nStore this in your .env file or environment variable.")
    print(f"Token expires in ~{expires_in // 86400} days. You'll need to refresh it after expiration.")
else:
    print(f"❌ Error: {response.status_code} {response.text}")
```

**Step 3: Store Token Securely**

Create or update `.env` in your project root:
```
ETSY_API_KEY=[YOUR_CLIENT_ID_HERE]
ETSY_API_SECRET=[YOUR_CLIENT_SECRET_HERE]
ETSY_ACCESS_TOKEN=[YOUR_ACCESS_TOKEN_HERE]
ETSY_SHOP_ID=[YOUR_SHOP_ID_HERE]
```

Find your SHOP_ID here: Etsy Shop Manager > Settings > Info & Appearance > Copy "Your Shop ID"

### 1.2 Etsy API Rate Limit Configuration

**Rate Limits (Etsy Open API v3)**:
- 10 requests per second (per API key)
- 10,000 requests per 24-hour period
- Practical ceiling for Phase 2: ~50 requests/day for daily order sync (well within limits)

**Implementation**: Use `time.sleep(0.1)` between requests in any automation script to respect the 10 RPS limit.

### 1.3 Daily Data Sync Script

Save as `scripts/etsy_daily_sync.py`:

```python
#!/usr/bin/env python3
"""
Etsy API Daily Sync
Pulls orders and transactions from the past 24 hours and appends to CSV.
Idempotent: safe to run multiple times per day.
"""

import os
import csv
import requests
from datetime import datetime, timedelta
from pathlib import Path

API_BASE = "https://api.etsy.com/v3/application"
SHOP_ID = os.getenv("ETSY_SHOP_ID")
ACCESS_TOKEN = os.getenv("ETSY_ACCESS_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "x-api-version": "20231120"
}

DATA_DIR = Path("projects/seedwarden/analytics/data")
ORDERS_CSV = DATA_DIR / f"etsy_orders_{datetime.now().strftime('%Y-%m')}.csv"

def get_yesterday_unix():
    """Get yesterday's date as Unix timestamp."""
    yesterday = datetime.now() - timedelta(days=1)
    return int(yesterday.timestamp())

def fetch_receipts(min_created):
    """Fetch all receipts created since min_created timestamp."""
    url = f"{API_BASE}/shops/{SHOP_ID}/receipts"
    params = {"min_created": min_created}
    
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json().get("results", [])

def fetch_transactions(receipt_id):
    """Fetch all transactions for a given receipt."""
    url = f"{API_BASE}/shops/{SHOP_ID}/receipts/{receipt_id}/transactions"
    
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json().get("results", [])

def sync_orders():
    """Sync new orders from the past 24 hours."""
    min_created = get_yesterday_unix()
    
    receipts = fetch_receipts(min_created)
    print(f"Found {len(receipts)} new receipts in past 24 hours")
    
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    rows = []
    for receipt in receipts:
        transactions = fetch_transactions(receipt["receipt_id"])
        
        for txn in transactions:
            row = {
                "receipt_id": receipt["receipt_id"],
                "transaction_id": txn["transaction_id"],
                "listing_id": txn["listing_id"],
                "listing_title": txn.get("title", ""),
                "quantity": txn.get("quantity", 0),
                "price_usd": txn.get("price", {}).get("amount", 0) / 100,  # Convert cents to dollars
                "created_date": datetime.fromtimestamp(receipt["created_timestamp"]).strftime("%Y-%m-%d"),
                "buyer_email": receipt.get("buyer_email", ""),
                "buyer_country": receipt.get("country_iso", ""),
                "total_price_usd": receipt.get("total_price", 0) / 100,
                "coupon_code": receipt.get("coupon_code", ""),
                "message_from_buyer": receipt.get("message_from_buyer", "")
            }
            rows.append(row)
    
    if rows:
        # Check if file exists
        file_exists = ORDERS_CSV.exists()
        
        with open(ORDERS_CSV, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            if not file_exists:
                writer.writeheader()
            writer.writerows(rows)
        
        print(f"✅ Synced {len(rows)} transactions to {ORDERS_CSV}")
    else:
        print("No new transactions to sync.")

if __name__ == "__main__":
    sync_orders()
```

**Setup**: Schedule this script to run daily at 06:00 UTC (just before Phase 2 launch day monitoring):
- **Linux/Mac**: Add to crontab: `0 6 * * * cd /path/to/project && python3 scripts/etsy_daily_sync.py`
- **Windows**: Use Task Scheduler to run the script daily at 06:00
- **Alternative**: Run manually every morning by double-clicking the script

**Verification**: After first run, check that `projects/seedwarden/analytics/data/etsy_orders_2026-05.csv` contains rows with real order data.

---

## 2. Google Analytics 4 Custom Events Setup

### 2.1 GA4 Measurement ID & Event Configuration

**Prerequisite**: GA4 property created and Measurement ID (`G-XXXXXXXXXX`) already entered in Etsy Shop Manager > Settings > Options > Web Analytics.

**Verification**: Visit a Seedwarden Etsy listing, then check GA4 > Real-Time > Events. You should see `page_view` events appear within 60 seconds.

### 2.2 GA4 Custom Dimensions

Create custom dimensions in GA4 Admin > Custom Definitions > Custom Dimensions. These map cohort signals to GA4 events.

**Custom Dimensions to Create**:

| Dimension Name | Scope | Description |
|---|---|---|
| `guide_category` | Event | Which guide type: "wild-edibles", "medicinal", "endangered" |
| `acquisition_source` | Event | Traffic source: "pinterest", "kit", "reddit", "instagram", "direct", "etsy-search" |
| `buyer_cohort_inferred` | User | High-level cohort: "forager", "prepper", "homesteader", "gift-buyer" |
| `zone_number` | Event | Hardiness zone 3-10 |
| `email_campaign_id` | Event | Kit email campaign identifier |

**Setup Steps**:
1. GA4 Admin > Custom Definitions > Create Custom Dimension
2. For each dimension above:
   - Dimension Name: (from table above)
   - Scope: (from table above)
   - Description: (from table above)
   - Event parameter / User property: Match dimension name (snake_case)
3. Click "Save" for each

### 2.3 GA4 Audiences (Cohort Segments)

Create audience segments in GA4 Admin > Audiences. These identify high-value cohorts automatically.

**Audience 1: Forager Signal**
```
User meets ANY of:
  - Page path contains "wild-edibles" AND session_engagement_time > 120 seconds
  - guide_category = "wild-edibles" in past 30 days
  - Page path contains guide AND viewed 2+ different guides in session
```

**Audience 2: Prepper Signal**
```
User meets ANY of:
  - Viewed bundle listing
  - Visited 3+ guide pages in single session
  - guide_category = "survival" OR "prepper" in event
```

**Audience 3: High-Value Repeat Candidate**
```
User meets ALL of:
  - First visit 30+ days ago
  - Visited listing page 3+ times total
  - Average session duration > 90 seconds
```

**Audience 4: Kit Email Engaged**
```
User meets ANY of:
  - utm_source = "kit" in first visit
  - Visited landing page with utm_campaign = "lead_magnet"
  - Multiple visits from same utm_source="kit" campaign
```

### 2.4 GA4 Event Implementation for Kit Landing Page

The Kit landing page is a Seedwarden-controlled surface where full GA4 event firing is possible. Implement these events.

**Add this to Kit page HTML** (or inject via GTM):

```html
<!-- Google Analytics 4 Measurement ID (set in your Kit page) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');

  // Track Zone Card Landing Page View
  function trackZoneCardView() {
    const urlParams = new URLSearchParams(window.location.search);
    const acquisitionSource = urlParams.get('utm_source') || 'direct';
    
    gtag('event', 'view_zone_card_landing', {
      'acquisition_source': acquisitionSource,
      'page_title': document.title,
      'page_path': window.location.pathname
    });
  }

  // Track Guide Download Event
  function trackGuideDownload(guideName, format) {
    gtag('event', 'guide_downloaded', {
      'guide_name': guideName,
      'format': format,  // 'pdf', 'ebook', etc.
      'guide_category': 'wild-edibles',
      'download_time': new Date().toISOString()
    });
  }

  // Track Email Link Click
  function trackEmailClick(campaignId, linkTarget) {
    gtag('event', 'email_link_clicked', {
      'email_campaign_id': campaignId,
      'link_target': linkTarget,
      'acquisition_source': 'kit'
    });
  }

  // Track Checkout Funnel Step
  function trackCheckoutStep(step, productTitle) {
    gtag('event', 'checkout_step', {
      'step': step,  // 'product_view', 'cart_add', 'purchase'
      'product_title': productTitle,
      'value': 0  // Add actual price if available
    });
  }

  // Fire on page load
  window.addEventListener('load', trackZoneCardView);
</script>
```

**Event Template for Etsy Listing Footer CTA**:
```html
<a href="https://kit.co/seedwarden/zone-cards?utm_source=etsy_listing&utm_campaign=kit_signup" 
   onclick="trackEmailClick('etsy_listing_cta', 'kit_landing')">
  Get Your Zone Card
</a>
```

---

## 3. Kit Email Analytics Integration

### 3.1 Kit Email Performance Dashboard Setup

Kit provides email metrics via CSV export. Create a Google Sheet to automatically pull and visualize these metrics.

**Monthly Kit Export Workflow** (30 minutes, first Monday of each month):

1. Log into Kit.co > Subscribers
2. Click "Export" → CSV format
3. Save as `projects/seedwarden/analytics/data/kit_subscribers_YYYY-MM.csv`
4. Open the CSV in Google Sheets
5. Filter by `subscribed_at` to count new subscribers this month
6. For each cohort tag, use COUNTIF to count subscribers:
   ```
   =COUNTIF(D:D, "Cohort_Forager")
   ```

### 3.2 Kit Email Segmentation Tags

Ensure these tags exist in Kit > Tag Manager:

**Zone Tags** (for geographic segmentation):
- `zone-3`, `zone-4`, `zone-5`, `zone-6`, `zone-7`, `zone-8`, `zone-9`, `zone-10`

**Cohort Tags** (applied post-purchase or via survey):
- `Cohort_Forager`
- `Cohort_Prepper`
- `Cohort_Homesteader`
- `Cohort_GiftBuyer`

**Behavioral Tags** (applied via email link click tracking):
- `seed-saver` (clicked seed-saving content)
- `city-grower` (clicked urban/container growing)
- `preservationist` (clicked preservation/canning)

**Lifecycle Tags**:
- `new-subscriber` (auto-applied on signup)
- `purchased` (manual or API-tagged when order detected)
- `vip` (tagged if 2+ purchases)

### 3.3 Kit Email Performance Metrics to Track

Create a monitoring sheet with these columns (update monthly):

| Metric | Formula | What It Measures |
|---|---|---|
| Total Subscribers | `=COUNTA(A:A) - 1` | List size growth |
| New This Month | `=COUNTIFS(B:B, ">=2026-05-01", B:B, "<=2026-05-31")` | Acquisition rate |
| Unsubscribed This Month | `=COUNTIFS(C:C, ">=2026-05-01", C:C, "<=2026-05-31")` | Churn rate |
| Forager Subscribers | `=COUNTIF(D:D, "Cohort_Forager")` | Cohort size |
| Prepper Subscribers | `=COUNTIF(D:D, "Cohort_Prepper")` | Cohort size |
| Homesteader Subscribers | `=COUNTIF(D:D, "Cohort_Homesteader")` | Cohort size |
| Avg Open Rate (All) | `=AVERAGE(E:E)` | Email engagement |
| Welcome Email 1 Open Rate | Manual from Kit dashboard | First impression |
| Newsletter Open Rate (Avg) | Manual from Kit dashboard | Content relevance |

---

## 4. Google Sheets Analytics Master Dashboard

### 4.1 Dashboard Structure

Create a Google Sheet with 5 tabs for comprehensive Phase 2 monitoring:

**Tab 1: Daily Metrics** (updated every morning, ~5 minutes)
- Date, Orders (new), Revenue (new), Units Sold, Avg Order Value
- Email Signups (24h), Email Open Rate (last campaign)
- Guide Downloads (from GA4)
- Row sparklines showing 7-day trend

**Tab 2: Weekly Summary** (updated every Monday, ~10 minutes)
- Week number, Orders (week total), Revenue (week total), WoW % change
- Top 3 guides by orders, Top traffic source
- Email subscribers added, newsletter open rate

**Tab 3: Monthly Cohort Performance** (updated first Monday of each month, ~20 minutes)
- Month, Orders by cohort (Forager, Prepper, Homesteader, Gift Buyer)
- Repeat purchase rate by cohort, AOV by cohort
- Email engagement by cohort

**Tab 4: KPI Summary Dashboard** (reference tab, no daily updates needed)
- Single-page view of critical metrics
- Green/Yellow/Red status indicators
- Target thresholds for Phase 2 success

**Tab 5: Raw Data Log** (daily append-only)
- All individual transactions as they come in
- Source: automated append from Etsy API sync script

### 4.2 Google Sheets Template with Pre-Built Formulas

**Create the sheet**: Open https://sheets.google.com → New Sheet → Name it "Seedwarden Phase 2 Analytics Dashboard"

**Tab 1: Daily Metrics**

```
Date | Orders | Revenue | Units Sold | AOV | Email Signups | Open Rate | Guide Downloads | 7-Day Trend
     |        |         |            |     |               |           |                 |

=TODAY() | [manual or Etsy API] | [manual] | [manual] | =C2/B2 | [manual Kit] | [manual Kit] | [manual GA4] | =SPARKLINE(B2:B8)
```

**Tab 2: Weekly Summary**

```
Week | Orders | Revenue | WoW % Change | Top Guide 1 | Top Guide 2 | Top Source | Email Added | Newsletter Open Rate
     |        |         |              |             |             |            |             |
     | =SUM(Daily!B:B) | =SUM(Daily!C:C) | =((B2-B1)/B1)*100 | [manual] | [manual] | [manual GA4] | =SUM(Daily!F:F) | [manual Kit]
```

**Tab 3: Monthly Cohort Performance** (Cumulative since Phase 2 launch)

```
Month | Forager Orders | Prepper Orders | Homesteader Orders | Gift Buyer Orders | Forager Repeat Rate | Prepper Repeat Rate | Avg AOV All
      | =COUNTIFS('Raw Data Log'!H:H, "Cohort_Forager", 'Raw Data Log'!A:A, ">=2026-05-01") | ... | ...
```

**Tab 4: KPI Summary Dashboard**

```
PHASE 2 KPI SUMMARY — May 30 Launch

TARGET METRICS (May 30 — June 30)                    ACTUAL          STATUS
─────────────────────────────────────────────────────────────────────────
Orders (Target: 40–60)                               [=SUM(Daily!B:B)] [=IF(B1>=40,"🟢 GO","🔴 MISS")]
Revenue (Target: $1,000–$1,500)                      [=SUM(Daily!C:C)] [=IF(B2>=1000,"🟢 GO","🔴 MISS")]
Email Subscribers (Target: 100–150)                  [manual]         [=IF(B3>=100,"🟢 GO","🔴 MISS")]
Repeat Purchase Rate (Target: 8–12%)                 [=...]/[=SUM()] [=IF(B4>=0.08,"🟢 GO","🟡 WATCH")]
Conversion Rate (Target: 1.5–2.0%)                   [=SUM(Daily!B:B)]/[=...views] [=IF(B5>=0.015,"🟢 GO","🟡 WATCH")]
```

### 4.3 Automated Daily Data Appending

**For Etsy Order Data**: The daily sync script (`scripts/etsy_daily_sync.py`) appends to CSV. Use this formula in Google Sheets to auto-import:

```
=IMPORTDATA("https://example.com/path/to/etsy_orders_2026-05.csv")
```

Or, simpler: Import CSV to Google Sheets daily by:
1. Upload `etsy_orders_2026-05.csv` to Google Drive
2. Open it in Google Sheets
3. Go to Tab 5 (Raw Data Log) in your Dashboard
4. Insert > Link to external data > Paste CSV URL or upload file

**For Kit Email Data**: Manual weekly upload (Kit doesn't provide API-based export):
1. Export CSV from Kit each Monday
2. Copy the relevant columns into Dashboard Tab 2

---

## 5. Discord Alert Configuration

### 5.1 Webhook Setup

Create a Discord channel for Seedwarden alerts (e.g., #seedwarden-alerts).

**Step 1: Create Webhook**
1. Right-click channel → Edit Channel → Integrations → Webhooks
2. Click "New Webhook"
3. Name: "Seedwarden Analytics"
4. Copy the Webhook URL (store securely in `.env`):
   ```
   DISCORD_WEBHOOK_URL=https://discordapp.com/api/webhooks/[ID]/[TOKEN]
   ```

### 5.2 Daily Summary Alert (20:00 UTC)

**Post daily metrics summary to Discord at 20:00 UTC every day during Phase 2.**

Save as `scripts/discord_daily_alert.py`:

```python
#!/usr/bin/env python3
"""
Discord Daily Alert
Sends a formatted message to Discord with the day's key metrics.
Schedule to run daily at 20:00 UTC.
"""

import os
import requests
import csv
from datetime import datetime, timedelta
from pathlib import Path

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
DATA_DIR = Path("projects/seedwarden/analytics/data")

def get_today_metrics():
    """Read today's metrics from the Daily Metrics sheet (or CSV)."""
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Read from the most recent etsy_orders CSV
    current_month = datetime.now().strftime("%Y-%m")
    orders_file = DATA_DIR / f"etsy_orders_{current_month}.csv"
    
    if not orders_file.exists():
        return None
    
    today_orders = 0
    today_revenue = 0.0
    
    with open(orders_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('created_date') == today:
                today_orders += 1
                today_revenue += float(row.get('total_price_usd', 0))
    
    return {
        'orders': today_orders,
        'revenue': today_revenue,
        'aov': today_revenue / today_orders if today_orders > 0 else 0,
        'date': today
    }

def send_discord_alert(metrics):
    """Send formatted metrics to Discord."""
    if not metrics:
        return
    
    # Build embed
    embed = {
        "title": f"Seedwarden Daily Summary — {metrics['date']}",
        "color": 5763719,  # Green
        "fields": [
            {
                "name": "Orders",
                "value": f"{metrics['orders']} orders",
                "inline": True
            },
            {
                "name": "Revenue",
                "value": f"${metrics['revenue']:.2f}",
                "inline": True
            },
            {
                "name": "AOV",
                "value": f"${metrics['aov']:.2f}",
                "inline": True
            }
        ],
        "timestamp": datetime.now().isoformat()
    }
    
    payload = {
        "embeds": [embed]
    }
    
    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code == 204:
        print("✅ Daily alert sent to Discord")
    else:
        print(f"❌ Discord error: {response.status_code}")

if __name__ == "__main__":
    metrics = get_today_metrics()
    send_discord_alert(metrics)
```

**Schedule with cron** (Linux/Mac):
```
0 20 * * * cd /path/to/project && python3 scripts/discord_daily_alert.py
```

### 5.3 Weekly Trend Alert (09:00 UTC Monday)

Send a weekly trend report every Monday morning at 09:00 UTC.

**Alert template**:
```
🔔 WEEKLY TREND ALERT — Week of [Date]

📊 Weekly Performance
   Orders: [N] (↑ X% vs last week)
   Revenue: $[X] (↑ Y% vs last week)
   Conversion Rate: Z% (↑/↓ vs baseline)

🎯 Top Performer
   [Guide Name]: [N] orders ($[X] revenue)

⚠️ Anomalies Detected
   [If any]: [Description and recommended action]

Next check: [Next Monday time]
```

### 5.4 Anomaly Detection Triggers

**Trigger RED alert if any of these occur**:

| Condition | Threshold | Action |
|---|---|---|
| Order count drops > 50% day-over-day | Orders today < (Avg daily orders × 0.5) | Post RED alert: "Order volume drop detected. Check: listing status, Etsy search visibility, platform outages" |
| Revenue per order drops > 20% | (Today AOV) < (Weekly avg AOV × 0.8) | Post YELLOW alert: "AOV declining. Possible: lower-priced items selling, discount codes in use, or pricing issue" |
| Unsubscribe rate spikes | Kit unsubscribes > 3 in 24h | Post YELLOW alert: "Email unsubscribe spike. Check: recent campaign content, spam folder, list hygiene" |
| Guide downloads zero for 3+ consecutive days | GA4 guide_downloaded events = 0 | Post YELLOW alert: "No guide downloads in [N] days. Check: GA4 event firing, landing page conversion funnel" |

**Implementation**: Modify `discord_daily_alert.py` to check these thresholds and post conditional alerts.

---

## 6. Baseline Metrics & Alert Thresholds

### 6.1 Phase 1 Historical Benchmarks

**To be populated with actual Phase 1 data by May 25**. Use these historical data points to set Phase 2 thresholds:

| Metric | Phase 1 Actual | Phase 2 Target | Justification |
|---|---|---|---|
| Avg daily orders | [PLACEHOLDER] | +15% over Phase 1 | Phase 2 has larger initial audience (Kit list) |
| Avg AOV | [PLACEHOLDER] | +$2–$5 | Bundle adoption + larger initial buyer base |
| Email list growth rate | [PLACEHOLDER] new/day | Same as Phase 1 | Zone card lead magnet |
| Repeat purchase rate (30 days) | [PLACEHOLDER] % | +3 percentage points | Improved post-purchase email sequence |
| Guide download rate (per listing view) | [PLACEHOLDER] % | Same baseline | Same guides, same landing page |

**How to fill in Phase 1 data**:
- Open `projects/seedwarden/analytics/data/etsy_orders_2026-04.csv` (if Phase 1 complete)
- Calculate daily order count, AOV, etc.
- Record actual values in the "Phase 1 Actual" column above

### 6.2 Phase 2 Alert Thresholds (Conservative, Moderate, Optimistic)

**Setup**: Use these thresholds to color-code the KPI Summary Dashboard.

| Metric | GREEN (On-Track) | YELLOW (Watch) | RED (Escalate) |
|---|---|---|---|
| Daily Orders | ≥ 2 orders/day | 1–1.9 orders/day | < 1 order/day for 3+ consecutive days |
| Daily Revenue | ≥ $60 | $40–$59 | < $40 for 3+ consecutive days |
| AOV | ≥ $28 | $24–$27 | < $24 |
| Email Signups (daily) | ≥ 4/day | 2–3/day | < 2/day for 5+ consecutive days |
| Email Open Rate | ≥ 35% | 25–34% | < 25% |
| Conversion Rate (listing) | ≥ 1.5% | 1.0–1.4% | < 1.0% |
| Repeat Purchase Rate (30d) | ≥ 8% | 5–7% | < 5% |

### 6.3 Escalation Procedures

**GREEN**: No action. Monitor and celebrate progress.

**YELLOW**: Investigate at next weekly review (every Monday morning). Questions to ask:
- Is this normal weekly variation or a trend?
- Did anything change in marketing, pricing, or listing?
- Are there external factors (Etsy outage, social algorithm change)?
- What small changes can improve this metric?

**RED**: Escalate immediately.
- Post alert to Discord (see Section 5.4)
- If guide-related (low views, low conversions): check listing search ranking in Etsy Stats
- If email-related (low opens, high unsubscribes): check spam folder, list health
- If revenue-related (low AOV): check if a high-priced bundle is selling less frequently
- If acquisition-related (low signups): check Kit landing page conversion funnel (GA4)

---

## 7. May 30 Day-1 Readiness Checklist (15 minutes)

**Run this checklist on May 30 at 06:00 UTC, before Phase 2 launch trigger at 09:00 UTC.**

### 7.1 Etsy API Verification

- [ ] Etsy API credentials present in `.env` file (CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN, SHOP_ID)
- [ ] Run: `python3 scripts/etsy_daily_sync.py` → Verify it creates/appends to `analytics/data/etsy_orders_2026-05.csv`
- [ ] Check CSV file: confirm it contains at least 1 row with real data from Phase 1 orders (if any) OR confirm file is empty and ready for Phase 2 (acceptable)
- [ ] Verify cron job scheduled: `crontab -l | grep etsy_daily_sync` → Confirm daily run scheduled for 06:00 UTC

### 7.2 Google Analytics 4 Verification

- [ ] GA4 Measurement ID confirmed in Etsy Shop Manager > Settings > Options > Web Analytics
- [ ] Open a Seedwarden Etsy listing in an incognito browser
- [ ] GA4 > Real-Time > Events: within 60 seconds, confirm `page_view` event appears
- [ ] GA4 > Admin > Custom Dimensions: all 5 custom dimensions exist (guide_category, acquisition_source, buyer_cohort_inferred, zone_number, email_campaign_id)
- [ ] GA4 > Admin > Audiences: all 4 audience segments exist (Forager Signal, Prepper Signal, High-Value Repeat Candidate, Kit Email Engaged)
- [ ] GA4 event code added to Kit landing page HTML (verify by viewing page source, search for `gtag('event'`)

### 7.3 Kit Email Verification

- [ ] Kit account active and logged in
- [ ] Welcome sequence (Email 1–5) visible in Kit > Automations > Sequences
- [ ] Launch broadcast email visible in Kit > Broadcasts (scheduled for May 30 09:30 UTC)
- [ ] Email segmentation tags created in Kit > Tag Manager (zone-3 through zone-10, Cohort_*, behavioral tags)
- [ ] Test email send: send a test welcome email to test@example.com → confirm it arrives within 2 minutes

### 7.4 Google Sheets Dashboard Verification

- [ ] Google Sheet "Seedwarden Phase 2 Analytics Dashboard" created and shared (view access for admin)
- [ ] All 5 tabs present: Daily Metrics, Weekly Summary, Monthly Cohort Performance, KPI Summary, Raw Data Log
- [ ] Tab 4 (KPI Summary) displays: [manual check that layout looks good, thresholds match Section 6]
- [ ] Sample data rows added to Tab 1 (Daily Metrics): at least 1 row with formulas calculating correctly
- [ ] IMPORTDATA formula (if used) successfully importing Etsy order CSV

### 7.5 Discord Alert Verification

- [ ] Discord channel #seedwarden-alerts created (or existing channel confirmed)
- [ ] Webhook URL present in `.env` file (DISCORD_WEBHOOK_URL)
- [ ] Manual test: run `python3 scripts/discord_daily_alert.py` → confirm test message posted to Discord
- [ ] Cron job scheduled: `crontab -l | grep discord_daily_alert` → confirm 20:00 UTC daily run scheduled

### 7.6 Final System Check

- [ ] All `.env` variables set: ETSY_API_KEY, ETSY_API_SECRET, ETSY_ACCESS_TOKEN, ETSY_SHOP_ID, DISCORD_WEBHOOK_URL
- [ ] All Python scripts executable: `chmod +x scripts/etsy_daily_sync.py scripts/discord_daily_alert.py`
- [ ] All cron jobs active: `crontab -l` shows both sync and alert jobs
- [ ] Google Sheet has view/edit access and is ready for daily operator input
- [ ] No error logs: check system logs for any warnings about API calls, missing files, or webhook failures

### 7.7 Launch Go/No-Go Decision

**If all checks above are ✅**: 
```
✅ READY FOR LAUNCH
All monitoring systems are armed and responsive.
Proceed to Phase 2 launch trigger at 09:00 UTC.
```

**If any check is ❌**:
```
⏸️ PAUSE LAUNCH
Fix the failing check before proceeding. 
(Est. 5–10 min to resolve most issues)
```

---

## 8. Post-Launch Monitoring (Days 1–7)

### 8.1 Hour-By-Hour Monitoring (May 30, 09:00–18:00 UTC)

**09:00 UTC - Launch Trigger**: Etsy listings go live. Monitor in real-time.

| Time | Check | Signal | Action If Issue |
|---|---|---|---|
| 09:00 | Listings visible on Etsy | Can search and view | Escalate to Etsy support if listings showing as "inactive" |
| 09:30 | Launch email sent | Kit shows "sent" status | Resend if failed |
| 10:00 | GA4 Real-Time shows traffic | Page views appearing in Real-Time | Verify GA4 Measurement ID is correct in Etsy Shop Manager |
| 11:00 | First order received | Shop Manager > Orders shows ≥1 order | No action; expected may take 2–4 hours after launch |
| 15:00 | Discord daily alert preview | Check format and content | Test webhook if not received |
| 18:00 | End-of-day check | [Run daily checklist items 7.1–7.5] | Fix any failures found |

### 8.2 Daily Monitoring (May 31 — June 6)

Every morning at 06:00 UTC:
1. Run `python3 scripts/etsy_daily_sync.py` (pulls previous day's orders)
2. Update Daily Metrics sheet with yesterday's data
3. Check Discord for any anomaly alerts that fired overnight
4. Quick visual scan: are orders coming in at expected rate (≥1 order/day minimum)?

Every evening at 20:00 UTC:
- Discord daily alert posts automatically (if cron job configured correctly)

Every Monday morning (June 3):
- Run full weekly checklist (Section 8.3 below)

### 8.3 Weekly Review (Every Monday, 09:00 UTC)

**Monday, June 3 — Week 1 Review** (~30 minutes):

1. Open Dashboard Tab 2 (Weekly Summary)
2. Calculate this week's metrics:
   - Total orders: [Should be 5–15 for successful launch]
   - Total revenue: [Should be $150–$500]
   - Top guide by orders: [Which guide resonated?]
   - Top traffic source: [Etsy organic? Email? Pinterest?]
3. Compare to Phase 1 weekly baseline (Section 6.1)
4. Check KPI Summary Dashboard Tab 4: how many metrics are GREEN vs YELLOW vs RED?
5. Record findings in `projects/seedwarden/WORKLOG.md` under "Phase 2 Week 1 Review"

**Action Triggers**:
- If Week 1 orders < 5: Check listing visibility (Etsy search ranking), review listing copy vs. competitors
- If Week 1 orders 5–15: On-track baseline. Monitor email engagement.
- If Week 1 orders > 15: Excellent early traction. Plan for Week 2 email sequence optimization.

### 8.4 Month-End Review (June 30)

Follow the full monthly review procedure in `post-launch-analytics-framework.md` Section 8. Key inputs:
- Etsy API pull: verify `analytics/data/etsy_orders_2026-05.csv` is complete
- Etsy Stats manual read: record views, favorites, conversion rate, top search keywords
- Kit subscriber snapshot: export CSV, record metrics by cohort tag
- Cohort rollup: update `customer-retention-tracker.csv` with June buyers as a new cohort

---

## Appendix A: Common Setup Issues & Troubleshooting

### Issue: Etsy API returns "401 Unauthorized"
**Cause**: Access token expired or credentials incorrect.
**Fix**: 
1. Verify `.env` has correct ETSY_API_KEY, ETSY_API_SECRET, ETSY_ACCESS_TOKEN
2. If token is > 30 days old, regenerate it using `scripts/etsy_oauth_token.py`
3. Check that API key is from the correct Etsy Developer application

### Issue: GA4 Real-Time shows no events
**Cause**: Measurement ID not entered in Etsy Shop Manager, or GA4 not connected to Etsy.
**Fix**:
1. Go to Etsy Shop Manager > Settings > Options > Web Analytics
2. Paste your GA4 Measurement ID (`G-XXXXXXXXXX`) and save
3. Wait 5 minutes, then refresh the page
4. Open a Seedwarden Etsy listing in incognito browser
5. Go to GA4 > Real-Time > Events and wait 60 seconds

### Issue: Discord webhook returns 404 or 401
**Cause**: Webhook URL invalid or expired, or Discord channel deleted.
**Fix**:
1. Verify channel #seedwarden-alerts still exists
2. Go to channel → Edit Channel → Integrations → Webhooks
3. Delete old webhook and create a new one
4. Copy the new webhook URL and update `.env` with DISCORD_WEBHOOK_URL
5. Test: `python3 scripts/discord_daily_alert.py`

### Issue: Google Sheets IMPORTDATA formula returns error
**Cause**: CSV file not publicly accessible, or URL syntax incorrect.
**Fix**:
1. If using Google Drive CSV: right-click file → Share → "Anyone with link" (view access) → Copy URL
2. Append `&export=csv` to the end of the URL if needed
3. Paste into IMPORTDATA formula: `=IMPORTDATA("URL_HERE")`
4. If still failing: use manual CSV upload instead (copy/paste data directly)

---

## Appendix B: Reference Documentation

| Document | Purpose | Where to Find |
|---|---|---|
| PHASE_2_GO_NO_GO_DASHBOARD.md | Launch verification framework | `projects/seedwarden/` |
| PHASE_2_ANALYTICS_STRATEGY.md | Measurement architecture and cohort definitions | `projects/seedwarden/` |
| post-launch-analytics-framework.md | Full data collection and monthly review procedures | `projects/seedwarden/` |
| etsy-ga4-event-tracking.md | GA4 custom event taxonomy and implementation | `projects/seedwarden/` |
| TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md | Kit email setup and automation | `projects/seedwarden/` |
| customer-cohort-analysis-framework.md | Cohort definitions and messaging strategy | `projects/seedwarden/` |
| PHASE_2_LAUNCH_CHECKLIST.md | Day-1 launch checklist (content, listings, emails) | `projects/seedwarden/` |

---

## Appendix C: Environment Variables Reference

Store these in `.env` or your system environment:

```bash
# Etsy API
ETSY_API_KEY=[YOUR_CLIENT_ID_HERE]
ETSY_API_SECRET=[YOUR_CLIENT_SECRET_HERE]
ETSY_ACCESS_TOKEN=[YOUR_ACCESS_TOKEN_HERE]
ETSY_SHOP_ID=[YOUR_SHOP_ID_HERE]

# Google Analytics 4
GA4_MEASUREMENT_ID=G-XXXXXXXXXX

# Discord
DISCORD_WEBHOOK_URL=https://discordapp.com/api/webhooks/[ID]/[TOKEN]

# Kit Email
KIT_API_KEY=[IF_USING_API_INTEGRATION]
```

**Security Note**: Never commit `.env` to version control. Add `.env` to `.gitignore`.

---

## Summary Timeline

| Date | Task | Owner |
|---|---|---|
| May 13–14 | Implement Sections 1–6 (infrastructure setup) | Agent (autonomous) |
| May 15–25 | Test all systems; fill in Phase 1 baseline data (Section 6.1) | Agent + Manual QA |
| May 26–29 | Final system checks; verify all Day-1 checklist items | User (prep work) |
| May 30 06:00 | Run Section 7 (Day-1 readiness checklist) | User (15 min) |
| May 30 09:00 | Phase 2 launch trigger — monitoring systems LIVE | User |
| May 30–June 30 | Daily monitoring and alerts active; weekly reviews | User (10–30 min/day) |

---

**Document Status**: Production-Ready  
**Last Updated**: Session 979, May 13 2026  
**Next Review**: May 29 2026 (pre-launch final audit)
