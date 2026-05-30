---
title: "Phase 1 Adoption Tracking Deployment Guide"
created: 2026-05-30
status: production-ready
scope: "Setup, deployment, and operation of automated Phase 1 adoption tracking"
timeline: "Deploy by May 31 23:59 UTC (June 1 distribution start)"
---

# Phase 1 Adoption Tracking Deployment Guide

**Version 2.0 — May 30, 2026**

This guide provides step-by-step instructions for deploying the Phase 1 adoption tracking automation on Raspberry Pi or any Linux system. The system collects GitHub Gist view counts and email monitoring data weekly, with fully autonomous operation after setup.

---

## Quick Start (5 minutes)

### Prerequisites
- Python 3.10+ (`python3 --version`)
- Bash shell
- GitHub account with access to Phase 1 Gist URLs

### Setup

```bash
# Navigate to the adoption tracking directory
cd /path/to/phase-1-adoption

# Run setup script
bash phase-1-adoption-tracking-setup.sh

# Configure your tracking targets
# Edit adoption-tracking-config.json with:
# - github_username: Your GitHub account name
# - github_gist_ids: List of Gist IDs to monitor

# Test the script
python3 phase-1-adoption-tracking-script.py

# Schedule weekly collection (Monday 09:00 UTC)
crontab -e
# Add: 0 9 * * 1 cd /path/to/phase-1-adoption && python3 phase-1-adoption-tracking-script.py
```

Expected output:
- `logs/adoption-tracking.log` — Execution log
- `data/gist-view-tracking.json` — Persistent view count tracking
- `data/email-replies.json` — Email reply summaries (if Gmail enabled)

---

## Full Deployment (15–20 minutes)

### 1. Directory Structure

After setup, your `phase-1-adoption/` directory contains:

```
phase-1-adoption/
├── phase-1-adoption-tracking-script.py    # Main tracking automation
├── phase-1-adoption-tracking-setup.sh     # Setup automation
├── oauth2_login.py                        # Gmail OAuth2 helper
├── adoption-tracking-config.json          # Your configuration (auto-created)
├── adoption-tracking-config.json.template # Config template
├── data/                                   # Persistent state (auto-created)
│   ├── gist-view-tracking.json            # Gist view counts
│   └── email-replies.json                 # Email reply summaries
└── logs/                                   # Log files (auto-created)
    └── adoption-tracking.log              # Weekly execution log
```

### 2. Install Dependencies

#### Minimal Installation (Gist tracking only)

```bash
python3 -m pip install requests
```

#### Full Installation (with Gmail monitoring)

```bash
python3 -m pip install requests google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

#### Raspberry Pi (if you get permission errors)

```bash
python3 -m pip install --user requests google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

Verify installation:

```bash
python3 -c "import requests; print('✓ requests installed')"
python3 -c "import google.auth; print('✓ Google Auth installed')" 2>/dev/null || echo "Note: Google libraries optional"
```

### 3. Configure Tracking Targets

Edit `adoption-tracking-config.json`:

```json
{
  "github_username": "resistance-research-org",
  "github_gist_ids": [
    "2dec7fd03b08ab5b41c55d402f44c261",
    "2869da6eaeb15a47246ade3bbbc4a3f4"
  ],
  "organization_contacts": [
    {
      "name": "Brennan Center for Justice",
      "email": "contact@brennancenter.org",
      "sector": "think-tank"
    }
  ],
  "gmail_enabled": false,
  "gmail_credentials_path": "./credentials.json",
  "log_dir": "./logs",
  "data_dir": "./data"
}
```

**Field descriptions:**

| Field | Type | Description |
|-------|------|-------------|
| `github_username` | string | Your GitHub username (for analytics) |
| `github_gist_ids` | array | List of Gist IDs to track (extract from Gist URL: `gist.github.com/username/ID`) |
| `organization_contacts` | array | Contact list for attribution (name, email, sector) |
| `gmail_enabled` | boolean | Enable Gmail API monitoring (requires oauth2_login.py) |
| `gmail_credentials_path` | string | Path to credentials.json from Google Cloud Console |
| `log_dir` | string | Directory for adoption-tracking.log |
| `data_dir` | string | Directory for persistent JSON state files |

### 4. How to Get Gist IDs

Each Phase 1 distribution email includes a Gist URL like:
```
https://gist.github.com/resistance-research-org/2dec7fd03b08ab5b41c55d402f44c261
```

Extract the last part: `2dec7fd03b08ab5b41c55d402f44c261`

Add all canonical Gist IDs to `github_gist_ids` in config.json.

### 5. Test the Script

```bash
cd /path/to/phase-1-adoption
python3 phase-1-adoption-tracking-script.py
```

**Expected output:**

```
2026-05-30 12:34:56 [INFO] ======================================
2026-05-30 12:34:56 [INFO] Phase 1 Adoption Tracking — Weekly Collection
2026-05-30 12:34:56 [INFO] ======================================
2026-05-30 12:34:56 [INFO] [1/2] Polling Gist view counts...
2026-05-30 12:34:57 [INFO] Gist 2dec7fd0: 0 comments/engagement signals
2026-05-30 12:34:57 [INFO] [2/2] Checking email replies...
2026-05-30 12:34:57 [INFO] Gmail monitoring disabled (not configured)
2026-05-30 12:34:57 [INFO] ======================================
2026-05-30 12:34:57 [INFO] Collection complete
```

Check logs:

```bash
tail -20 logs/adoption-tracking.log
cat data/gist-view-tracking.json | python3 -m json.tool | less
```

### 6. Schedule Weekly Collection

Gist view counts are collected every **Monday at 09:00 UTC**. This timing allows 6 days post-send for initial adoption signals.

#### Add to crontab:

```bash
crontab -e

# Add this line (replace /path/to with actual path):
0 9 * * 1 cd /path/to/phase-1-adoption && python3 phase-1-adoption-tracking-script.py
```

#### Verify cron is configured:

```bash
crontab -l | grep adoption-tracking
```

Expected output:
```
0 9 * * 1 cd /path/to/phase-1-adoption && python3 phase-1-adoption-tracking-script.py
```

#### Check cron logs (if available):

```bash
# macOS
log stream --predicate 'eventMessage contains "adoption"'

# Linux (systemd)
journalctl -u cron | tail -20

# Linux (syslog)
tail -20 /var/log/syslog | grep adoption
```

---

## GitHub Gist Tracking

### How Gist View Counts Work

- **Cumulative views**: GitHub API returns total comments on each Gist (proxy for engagement)
- **Weekly delta**: Calculate `views_this_week - views_last_week` to measure new engagement
- **Baseline**: First fetch establishes initial view count; future weeks compare against this

### Interpreting View Count Signals

| Views/Week | Signal | Interpretation |
|-----------|--------|-----------------|
| 0 | No engagement | Distribution email not opened or not accessed |
| 1–20 | Minimal interest | Individual engagement; not yet organizational |
| 20–50 | Emerging interest | Document circulating within organization |
| 50+ | Strong adoption signal | Active use; likely shared internally |

### Adding New Gists to Tracking

1. Get the Gist ID from its URL
2. Edit `adoption-tracking-config.json`
3. Add ID to `github_gist_ids` array
4. Script will include it in next weekly run

Example:
```json
"github_gist_ids": [
  "2dec7fd03b08ab5b41c55d402f44c261",
  "NEW-GIST-ID-HERE"
]
```

### GitHub API Rate Limits

- **Public Gist views**: 60 requests per hour (no authentication required)
- **When rate limit hit**: Script logs warning, skips this cycle, retries next week
- **Recovery**: Automatic after 1 hour

If you see:
```
[WARNING] GitHub API rate limit hit (60 req/hour)
```

Wait 1 hour before running the script again, or modify your polling interval.

---

## Gmail Email Monitoring (Optional)

### Setup Gmail API

**Step 1: Create Google Cloud Project**

1. Visit https://console.cloud.google.com
2. Create a new project (name: "Phase 1 Adoption Tracking")
3. Enable the Gmail API (Search → "Gmail API" → Enable)

**Step 2: Create OAuth2 Credentials**

1. Go to: Credentials (left sidebar)
2. Create credentials → OAuth 2.0 Client ID
3. Application type: "Desktop app"
4. Download as JSON

**Step 3: Configure Email Monitoring**

Place `credentials.json` in the `phase-1-adoption/` directory:

```bash
cp ~/Downloads/client_secret_*.json ./credentials.json
```

Run OAuth2 login helper:

```bash
python3 oauth2_login.py
```

This will:
1. Open your browser for Gmail API authorization
2. Create `token.json` (saved session credentials)
3. Print next steps

**Step 4: Enable in Config**

Edit `adoption-tracking-config.json`:

```json
{
  "gmail_enabled": true,
  "gmail_credentials_path": "./credentials.json"
}
```

### How Email Monitoring Works

The script searches your Gmail inbox for:
- **Label**: "Phase1Responses" (you must create this label)
- **Date range**: June 1 — July 1, 2026
- **Content**: Any reply to Phase 1 distribution emails

**Setup Gmail label:**

1. Gmail inbox → Create label → "Phase1Responses"
2. Set up filter: `from:(org_contact_email)` → Apply label "Phase1Responses"

### Gmail API Token Expiration

Gmail tokens expire periodically. If you see:

```
[ERROR] Gmail API 401: Token expired
```

**Recovery:**

```bash
rm token.json
python3 oauth2_login.py
# Re-run the script
python3 phase-1-adoption-tracking-script.py
```

### Email Reply Data

Weekly email summaries are saved to `data/email-replies.json`:

```json
{
  "last_check": "2026-06-07T09:00:00",
  "recent_replies": [
    {
      "from": "director@organization.org",
      "subject": "Re: Phase 1 Distribution",
      "date": "Wed, 4 Jun 2026 14:32:00",
      "snippet": "Thank you for sharing. We are very interested in..."
    }
  ]
}
```

---

## Weekly Review Workflow

### Every Monday at 09:00 UTC:

The script automatically:
1. Fetches Gist view counts
2. Monitors email replies
3. Logs results to `adoption-tracking.log`
4. Persists data in JSON files

### Manual Review (5–10 minutes):

After automatic collection, review:

```bash
# View latest logs
tail -30 logs/adoption-tracking.log

# Check Gist view counts
cat data/gist-view-tracking.json | python3 -m json.tool

# Check email replies (if Gmail enabled)
cat data/email-replies.json | python3 -m json.tool | head -50
```

### Metrics to Track Manually

For each organization, note:

| Metric | Data Source | Example |
|--------|-------------|---------|
| View count | `gist-view-tracking.json` | Week 1: 0, Week 2: 15, Week 3: 23 (delta: +8) |
| Email reply | `email-replies.json` | "Re: Phase 1 Distribution" from director@org.org |
| Published output | Web search | "resistance-research.org/analysis/..." |
| Secondary distribution | Email/social monitoring | "We shared this with..." |

### Data Interpretation

**Strong adoption signals (trigger Phase 2 escalation):**
- View count delta >50/week
- Email replies from 30%+ of Tier 1 contacts
- Published documents citing framework
- Secondary distribution detected

**Weak signals (continue monitoring):**
- View count <20/week
- 0–5 email replies in Week 1–2
- No secondary distribution

**Failure signals (escalate to stakeholders):**
- View count declining week-over-week
- Email bounces (hard failures)
- Unsubscribe requests
- Explicit rejections

---

## Troubleshooting

### GitHub API Issues

**Problem**: `GitHub API rate limit hit (60 req/hour)`

```
[WARNING] GitHub API rate limit hit (60 req/hour). Retrying next week.
```

**Solution**:
- Wait 1 hour before next run
- Or adjust Gist IDs list to reduce requests
- Standard polling is Monday 09:00 UTC (1 req per Gist ID)

---

### Gmail API Issues

**Problem**: `Gmail API 401: Token expired`

```
[ERROR] Gmail API 401: Token expired
```

**Solution**:
```bash
rm token.json
python3 oauth2_login.py
# Re-run script
python3 phase-1-adoption-tracking-script.py
```

---

**Problem**: `label:Phase1Responses returns 0 results`

**Solution**:
1. Create label in Gmail: Settings → Labels → Create new label
2. Name it exactly: `Phase1Responses` (case-sensitive)
3. Set up filter to auto-apply label to Phase 1 replies

---

**Problem**: `Failed to load credentials: No such file`

**Solution**:
```bash
# Verify credentials.json exists
ls -la ./credentials.json

# If missing, download from Google Cloud Console
# Place in: /path/to/phase-1-adoption/credentials.json
```

---

### Cron Issues

**Problem**: Cron job not executing

**Troubleshooting:**

```bash
# Check crontab is configured
crontab -l | grep adoption

# Verify script path is absolute (not relative)
# Example WRONG: cd ~/phase-1-adoption
# Example RIGHT: cd /home/user/phase-1-adoption

# Check cron daemon is running
systemctl status cron  # Linux
launchctl list | grep cron  # macOS

# Test script directly
cd /path/to/phase-1-adoption
python3 phase-1-adoption-tracking-script.py

# Check file permissions
ls -la phase-1-adoption-tracking-script.py
# Should show: -rwxr-xr-x (executable)
```

---

**Problem**: Logs show script ran but no data was collected

**Troubleshooting:**

```bash
# Check adoption-tracking-config.json is valid JSON
python3 -m json.tool adoption-tracking-config.json

# Verify Gist IDs are correct
# Format: lowercase hex string, 32 characters
# Invalid: "GIST123" or "gist-123"

# Test script with verbose output
python3 phase-1-adoption-tracking-script.py
```

---

## Data Interpretation

### Phase 1 Success Criteria (per design document)

**Minimum threshold for Phase 2 escalation:**
- ≥3 organizations reach adoption level 2+ within 6 months
- Adoption across ≥2 institutional sectors
- At least 1 organization with published output referencing framework

### Adoption Levels

| Level | Name | Evidence | Examples |
|-------|------|----------|----------|
| 0 | No engagement | Sent; no signal | — |
| 1 | Awareness | Receipt/reply/views >3 | Email reply "thanks"; 50+ Gist views |
| 2 | Reference | Framework appears in published output | Blog post, report, webpage |
| 3 | Operational | Used in active casework/testimony | Court filing, legislation, testimony |
| 4 | Coalition | Org distributes to own networks | Forwarded to 5+ member organizations |

### Vocabulary Attribution (Advanced)

Before distribution, run baseline searches for these Phase 1 markers:

- "NVRA quiet period"
- "appellate capture"
- "pattern-and-practice enforcement escalation"
- "fiscal authority bypass"

Post-distribution, any document using these phrases (published after org contact) = vocabulary adoption.

---

## Operational Timeline

### Pre-Distribution (May 31)
- [ ] Run setup script
- [ ] Configure adoption-tracking-config.json
- [ ] Test script: `python3 phase-1-adoption-tracking-script.py`
- [ ] Schedule cron job

### Week 1 (June 1–7)
- [ ] Distribution waves execute
- [ ] Monday June 3: First automated collection (script records 0 views if no activity yet)
- [ ] Manual review: Check logs, verify script executed

### Week 2–4 (June 8 — July 1)
- [ ] Weekly script execution every Monday 09:00 UTC
- [ ] Manual review: Track view count deltas, email replies
- [ ] Update Master Contact Log in Google Sheets with signals

### Month 2–3 (July 2 — August 31)
- [ ] Monthly adoption level reviews
- [ ] Identify Phase 2 candidates (adoption level ≥2)
- [ ] Plan Phase 2 escalation (research/amplification waves)

---

## Advanced: Custom Polling Intervals

By default, the script runs **Monday 09:00 UTC**. To change:

```bash
crontab -e

# Example: Run daily at 08:00
0 8 * * * cd /path/to/phase-1-adoption && python3 phase-1-adoption-tracking-script.py

# Example: Run every 6 hours
0 */6 * * * cd /path/to/phase-1-adoption && python3 phase-1-adoption-tracking-script.py

# Example: Run twice per week (Monday & Thursday)
0 9 * * 1,4 cd /path/to/phase-1-adoption && python3 phase-1-adoption-tracking-script.py
```

**Warning**: Increasing polling frequency increases GitHub API request count. Stay within 60 req/hour limit.

---

## Support & Documentation

**Design document**: `execution/phase-1-adoption-tracking-automation.md`
**Main tracking script**: `phase-1-adoption-tracking-script.py`
**Setup automation**: `phase-1-adoption-tracking-setup.sh`
**Config template**: `adoption-tracking-config.json.template`

For questions about framework adoption definition, attribution methodology, or Phase 2 escalation criteria, see:
- `adoption-automation-infrastructure.md` — Full schema and calculations
- `adoption-tracking-dashboard-spec.md` — Citation monitoring setup
- `post-distribution-tracking.md` — Sector pathways and decision trees

---

**Last updated**: May 30, 2026  
**Status**: Production-ready for June 1 activation
