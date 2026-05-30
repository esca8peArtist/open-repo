---
title: "Adoption Tracking Deployment Guide"
created: 2026-05-30
status: production-ready
scope: "Setup, configuration, and deployment of automated Phase 1 adoption tracking"
timeline: "May 31 23:59 UTC deadline (June 1 08:00 UTC distribution start)"
---

# Adoption Tracking Deployment Guide

**Version 1.0 — May 30, 2026**

This guide provides step-by-step instructions for deploying the Phase 1 adoption tracking automation script on the Jetson Pi (or any Linux system). The script collects GitHub Gist view counts weekly and integrates with email monitoring and Google Sheets for adoption signal tracking.

---

## Quick Start (5 minutes)

### 1. Install Script

```bash
# Copy script to your scripts directory
cp phase-1-adoption-tracking.py /path/to/resistance-research/scripts/
chmod +x /path/to/resistance-research/scripts/phase-1-adoption-tracking.py

# Verify installation
python3 /path/to/resistance-research/scripts/phase-1-adoption-tracking.py --help
```

### 2. Initialize Data Files

```bash
cd /path/to/resistance-research/scripts
python3 phase-1-adoption-tracking.py --init-csv
# Creates: scripts/data/gist-views.csv
```

### 3. Run First Collection (Test)

```bash
cd /path/to/resistance-research/scripts
python3 phase-1-adoption-tracking.py --run-now
# Should complete with summary output (may show ZERO_VIEWS if no activity yet)
```

### 4. Schedule Weekly Runs

```bash
# View cron entry
python3 /path/to/resistance-research/scripts/phase-1-adoption-tracking.py --schedule-weekly

# Add to crontab (runs every Monday at 08:00 AM)
crontab -e
# Paste the line from --schedule-weekly output
```

**Expected output after scheduling:**
```
0 8 * * 1 /usr/bin/python3 /path/to/resistance-research/scripts/phase-1-adoption-tracking.py --run-now
```

**Verify cron is configured:**
```bash
crontab -l | grep adoption-tracking
```

---

## Full Setup (15–20 minutes)

### Step 1: Install Dependencies

#### Minimal Installation (Gist views only)

```bash
pip3 install requests
```

#### Full Installation (with Gmail and Google Sheets)

```bash
pip3 install requests google-auth-oauthlib google-auth-httplib2 gspread google-auth
```

#### Jetson Pi (Ubuntu-based) Installation

If pip3 install fails due to permissions:

```bash
python3 -m pip install --user requests google-auth-oauthlib google-auth-httplib2 gspread google-auth
```

Verify installation:

```bash
python3 -c "import requests; print('✓ requests installed')"
python3 -c "import gspread; print('✓ gspread installed')" 2>/dev/null || echo "Note: Google libraries optional"
```

### Step 2: Create Configuration File

Create `phase-1-adoption-tracking.json` in the scripts directory:

```json
{
  "github_username": "your-github-username",
  "gmail_credentials": "/path/to/gmail-credentials.json",
  "gmail_manual_log": "/path/to/scripts/data/email-replies-manual.csv",
  "sheets_credentials": "/path/to/sheets-credentials.json",
  "spreadsheet_id": "your-google-sheets-id",
  "gist_views_csv": "/path/to/scripts/data/gist-views.csv",
  "email_log_csv": "/path/to/scripts/data/email-replies.csv"
}
```

**Note**: If you only have Gist view tracking (no Gmail/Sheets), only populate `github_username`:

```json
{
  "github_username": "your-github-username"
}
```

### Step 3: Configure GitHub Access

The script uses public Gist analytics URLs (no authentication required). Gist analytics are accessible via:

```
https://gist.github.com/{username}/{gist_id}/analytics
```

**Verify access:**

```bash
python3 -c "
import requests
response = requests.get('https://gist.github.com/your-github-username/test-gist-id/analytics')
print(f'Status: {response.status_code}')
"
```

If you see 404, the Gist ID or username is incorrect.

### Step 4: Configure Email Monitoring (Optional)

Choose one of two approaches:

#### Option A: Manual Email Log (Recommended for Jetson Pi)

This is simpler and requires no API credentials.

**Setup (5 minutes):**

1. Create `scripts/data/email-replies-manual.csv`:

```csv
date,from_email,from_name,subject,snippet,reply_type
2026-05-31,contact@institution.org,Jane Doe,RE: Framework distribution,Thanks for the framework - interesting approach to ...,substantive
2026-06-01,policy@think-tank.org,John Smith,Quick question on Domain 29,Could you clarify the litigation tracker methodology...,question
```

2. Update config to point to this file:

```json
{
  "gmail_manual_log": "/path/to/scripts/data/email-replies-manual.csv"
}
```

3. **Weekly routine**: Copy new replies to the CSV file each Monday morning (or hourly if rapid response is needed).

**Template for manual entries:**

| Field | Example | Notes |
|-------|---------|-------|
| date | 2026-05-31 | YYYY-MM-DD format |
| from_email | jane@harvard.edu | Contact's email |
| from_name | Jane Doe | Contact's name |
| subject | RE: Framework distribution | Email subject line |
| snippet | Thanks for sending this - particularly interested in ... | First 100 chars of reply |
| reply_type | substantive / question / forward / thanks-no-action | Category (optional) |

#### Option B: Gmail API (For automated email monitoring)

This requires OAuth credentials from Google Cloud.

**Setup (10–15 minutes):**

1. **Create Google Cloud project:**
   - Go to [console.cloud.google.com](https://console.cloud.google.com)
   - Create new project: "Phase1 Adoption Tracking"
   - Enable "Gmail API" in Library
   - Create OAuth 2.0 credentials (Desktop app)
   - Download JSON credentials file

2. **Save credentials file:**

```bash
cp ~/Downloads/credentials.json /path/to/scripts/gmail-credentials.json
```

3. **Update config:**

```json
{
  "gmail_credentials": "/path/to/scripts/gmail-credentials.json"
}
```

4. **Authenticate (one-time):**

```bash
python3 phase-1-adoption-tracking.py --run-now
# First run will open browser for OAuth authentication
# Grant permission when prompted
# Token is saved automatically for future runs
```

### Step 5: Configure Google Sheets Sync (Optional)

This integrates tracking data with your Google Sheets dashboard.

**Setup (10 minutes):**

1. **Create Google Sheets service account:**
   - Go to [console.cloud.google.com](https://console.cloud.google.com)
   - Create service account: "adoption-tracking-sync"
   - Generate JSON key
   - Save to: `/path/to/scripts/sheets-credentials.json`

2. **Share Google Sheet with service account:**
   - Open your adoption tracking Google Sheet
   - Share with the service account email (from JSON file)
   - Give Editor access

3. **Get Spreadsheet ID:**
   - Open your Google Sheet
   - Copy ID from URL: `https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/edit`

4. **Update config:**

```json
{
  "sheets_credentials": "/path/to/scripts/sheets-credentials.json",
  "spreadsheet_id": "your-spreadsheet-id-here"
}
```

### Step 6: Test Configuration

```bash
cd /path/to/scripts

# Verify config is readable
python3 -c "import json; json.load(open('phase-1-adoption-tracking.json'))"
echo "✓ Config valid"

# Run test collection
python3 phase-1-adoption-tracking.py --run-now

# Check logs
tail -f logs/adoption-tracking.log
```

**Expected output:**

```
2026-05-30 14:35:22 [INFO] ======================================================================
2026-05-30 14:35:22 [INFO] PHASE 1 ADOPTION TRACKING — Weekly Collection
2026-05-30 14:35:22 [INFO] [1/3] Fetching Gist view counts...
2026-05-30 14:35:23 [INFO] Fetching views for full_proposal...
2026-05-30 14:35:24 [INFO] Gist 2dec7fd0: 24 views
2026-05-30 14:35:25 [INFO] [2/3] Fetching recent email replies...
2026-05-30 14:35:26 [INFO] [3/3] Checking leading-indicator alerts...
2026-05-30 14:35:26 [INFO] Weekly collection complete
2026-05-30 14:35:26 [INFO]   Gists tracked: 4
2026-05-30 14:35:26 [INFO]   Email replies: 2
2026-05-30 14:35:26 [INFO]   Alerts triggered: 0
```

### Step 7: Schedule Weekly Runs

#### Option A: Cron (Recommended)

```bash
# View cron schedule command
python3 phase-1-adoption-tracking.py --schedule-weekly

# Add to crontab
crontab -e
# Paste the suggested line and save

# Verify it was added
crontab -l | grep adoption-tracking
```

**Example cron entry:**

```bash
# Run every Monday at 08:00 AM
0 8 * * 1 /usr/bin/python3 /path/to/scripts/phase-1-adoption-tracking.py --run-now
```

#### Option B: Systemd Timer (Alternative)

Create `/etc/systemd/system/adoption-tracking.service`:

```ini
[Unit]
Description=Phase 1 Adoption Tracking
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
User=youruser
WorkingDirectory=/path/to/scripts
ExecStart=/usr/bin/python3 /path/to/scripts/phase-1-adoption-tracking.py --run-now

[Install]
WantedBy=multi-user.target
```

Create `/etc/systemd/system/adoption-tracking.timer`:

```ini
[Unit]
Description=Phase 1 Adoption Tracking (Weekly)

[Timer]
OnCalendar=Mon *-*-* 08:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable adoption-tracking.timer
sudo systemctl start adoption-tracking.timer

# Verify
sudo systemctl status adoption-tracking.timer
sudo systemctl list-timers adoption-tracking.timer
```

---

## Data Files Reference

### Gist Views CSV

Location: `scripts/data/gist-views.csv`

**Columns:**
- `timestamp`: When the view count was fetched
- `gist_label`: Label from CANONICAL_GISTS (full_proposal, executive_summary, etc.)
- `gist_id`: GitHub Gist ID
- `cumulative_views`: Total view count at fetch time
- `week_number`: ISO week number (1-52)
- `notes`: Free text for anomalies

**Example:**

```csv
timestamp,gist_label,gist_id,cumulative_views,week_number,notes
2026-05-30T08:15:42.123456,full_proposal,2dec7fd03b08ab5b41c55d402f44c261,24,22,
2026-05-30T08:16:02.234567,executive_summary,2869da6eaeb15a47246ade3bbbc4a3f4,18,22,
```

### Email Replies CSV (Manual)

Location: `scripts/data/email-replies-manual.csv`

**Columns (if using manual log):**
- `date`: YYYY-MM-DD
- `from_email`: Sender's email address
- `from_name`: Sender's name
- `subject`: Email subject line
- `snippet`: First 100 chars of reply
- `reply_type`: substantive / question / forward / thanks-no-action / other

**Update weekly:** Each Monday morning, add any new replies received since the last run.

### Summary Output

Location: `monitoring/adoption-summary-YYYY-MM-DD.md`

Auto-generated after each run. Contains:
- Gist view counts for the week
- Email replies received
- Any alerts triggered
- Error log

---

## Monitoring and Maintenance

### Weekly Checklist

**Every Monday morning (before 8:00 AM if using cron):**

1. **Check last week's summary:**
   ```bash
   cat monitoring/adoption-summary-$(date -d 'last monday' +%Y-%m-%d).md
   ```

2. **If using manual email log:**
   - Check your outreach email inbox
   - Copy new substantive replies to `scripts/data/email-replies-manual.csv`

3. **Verify cron ran (if scheduled):**
   ```bash
   tail -100 /var/log/syslog | grep adoption-tracking
   # or check logs directly
   tail -50 scripts/logs/adoption-tracking.log
   ```

### Alert Response

**If alert: ZERO_VIEWS**
- Verify Gist URLs are accessible: `curl https://gist.github.com/{username}/{gist_id}`
- Check if outreach emails were delivered (verify bounce rate)

**If alert: ZERO_REPLIES**
- This is expected in Week 1. Check again at Day 7 and Day 14.
- If still zero at Day 14: investigate delivery issues or distribution quality

**If script fails to run:**
- Check cron logs: `sudo tail -50 /var/log/syslog | grep cron`
- Check script logs: `tail -50 scripts/logs/adoption-tracking.log`
- Verify config file path is correct in cron entry

### Troubleshooting

| Problem | Diagnosis | Fix |
|---------|-----------|-----|
| Script not executing on schedule | Check cron: `crontab -l` | Verify cron entry exists; check system time is correct (`date`) |
| "Gist 0 views" always showing | GitHub analytics page scraping failed | Verify script can reach gist.github.com; check HTML structure hasn't changed |
| Gmail API fails with auth error | Credentials expired or invalid | Re-run `--run-now` to refresh OAuth token; or regenerate credentials |
| Permission denied on CSV files | File ownership issue | `chmod 644 scripts/data/*.csv` |
| "ModuleNotFoundError: No module named 'requests'" | Dependencies not installed | Run `pip3 install requests` |

---

## Production Deployment Checklist

Before June 1 08:00 UTC execution:

- [ ] Python 3.10+ installed on Jetson Pi
- [ ] Dependencies installed: `pip3 install requests`
- [ ] Configuration file created: `phase-1-adoption-tracking.json`
- [ ] CSV files initialized: `--init-csv`
- [ ] First test run succeeded: `--run-now`
- [ ] Cron entry verified: `crontab -l | grep adoption-tracking`
- [ ] Logs directory exists and is writable: `ls -la scripts/logs/`
- [ ] Email monitoring configured (Gmail API OR manual log template created)
- [ ] Google Sheets sync configured (if desired) with test update
- [ ] Monitoring summary directory created: `mkdir -p monitoring/`

---

## Integration with Phase 1 Measurement Dashboard

The script populates tracking data suitable for manual import into the Phase 1 Measurement Dashboard (Google Sheets):

**Weekly import workflow:**

1. Run script Monday morning (automatic via cron)
2. Open summary: `monitoring/adoption-summary-$(date +%Y-%m-%d).md`
3. Copy Gist view counts → **Gist View Log** sheet (columns C–H)
4. Copy email replies → **Master Contact Log** sheet (columns H–I)
5. Update **Engagement Timeline** sheet with day-by-day summary

For full automation, configure Google Sheets credentials (Step 5 above) to enable direct sync.

---

## Jetson Pi Specific Notes

### Path Configuration

If running on Jetson Pi (100.70.184.84):

```bash
# Check Python version
python3 --version  # Should be 3.10+

# Install pip if needed
sudo apt-get update
sudo apt-get install python3-pip

# Install script dependencies
python3 -m pip install --user requests google-auth-oauthlib gspread

# Create scripts directory if it doesn't exist
mkdir -p ~/resistance-research/scripts/logs
mkdir -p ~/resistance-research/scripts/data
```

### Cron on Jetson Pi

Jetson Pi uses standard Linux cron. Verify it's running:

```bash
sudo systemctl status cron
# If not running:
sudo systemctl start cron
sudo systemctl enable cron
```

### Network/Internet Access

The script requires outbound HTTPS access:
- `gist.github.com` (Gist analytics pages)
- `gmail.googleapis.com` (if using Gmail API)
- `sheets.googleapis.com` (if using Sheets sync)

Verify connectivity:

```bash
curl -I https://gist.github.com
curl -I https://www.googleapis.com
```

---

## Support and Next Steps

**For errors or issues:**
1. Check `scripts/logs/adoption-tracking.log`
2. Verify config file: `cat phase-1-adoption-tracking.json`
3. Run manual test: `python3 phase-1-adoption-tracking.py --run-now`

**For feature requests:**
- Gist view spike detection
- Automated email to orchestrator on critical alerts
- Integration with Telegram/Slack notifications

**For June 1 execution:**
- Verify script is running (check logs for last Monday's run)
- Confirm data files have entries
- Prepare manual email log with early adopter replies if any
