# Phase 1 Adoption Tracking — Deployment & Operations Guide

**Purpose**: Automated weekly monitoring of Phase 1 adoption signals (Gist views, email replies, citation events).

**Activation**: Activate on Day 0 of Wave 1 distribution. Estimated setup: 90-120 minutes one-time; 20-30 minutes/week thereafter.

---

## Part 1 — One-Time Setup (90-120 minutes)

### 1.1 Create Monitoring Directory

```bash
mkdir -p projects/resistance-research/monitoring/logs
mkdir -p projects/resistance-research/monitoring/weekly-summaries
mkdir -p projects/resistance-research/monitoring/citations
```

### 1.2 Python Dependencies

```bash
pip install requests google-auth gspread google-auth-httplib2 google-auth-oauthlib
```

Or from requirements.txt:

```bash
pip install -r projects/resistance-research/phase-1-adoption-tracking-requirements.txt
```

### 1.3 GitHub Personal Access Token

1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Scopes needed: `gist` (read access to Gist analytics)
4. Save the token securely (will not be shown again)

### 1.4 Gmail OAuth Credentials

1. Go to Google Cloud Console: https://console.cloud.google.com
2. Create a new project (or use existing)
3. Enable the Gmail API: Search "Gmail API" → Enable
4. Create OAuth 2.0 credentials:
   - Type: "Desktop application"
   - Download credentials as JSON → save as `gmail-oauth-credentials.json`
5. Place file in `projects/resistance-research/` (not committed; add to .gitignore)

**First run only**: Script will open browser for OAuth consent. Approve access. Token saved locally for future runs.

### 1.5 Google Sheets Service Account (Optional)

For automatic Sheets updates, create a service account:

1. Go to Google Cloud Console → "Service Accounts"
2. Create new service account → download JSON key
3. Share your tracking spreadsheet with the service account email
4. Place JSON at `projects/resistance-research/google-sheets-service-account.json`
5. Set `TRACKING_SPREADSHEET_ID` in config (see Part 1.7)

**Without service account**: Skip Sheets sync; use manual spreadsheet updates instead.

### 1.6 Configuration File

Copy the template and fill in your credentials:

```bash
cp projects/resistance-research/phase-1-adoption-tracking-config.json.template \
   projects/resistance-research/phase-1-adoption-tracking.json
```

Edit `phase-1-adoption-tracking.json`:

```json
{
  "github_token": "ghp_abc123...",
  "github_username": "your-github-username",
  "gmail_credentials": "/path/to/projects/resistance-research/gmail-oauth-credentials.json",
  "sheets_credentials": "/path/to/projects/resistance-research/google-sheets-service-account.json",
  "spreadsheet_id": "1A2B3C4D5E6F7G8H9I0J..."
}
```

**Security**: Do NOT commit `.json` credential files to git. Add to `.gitignore`:

```bash
echo "projects/resistance-research/*credentials*.json" >> .gitignore
echo "projects/resistance-research/token.json" >> .gitignore
```

### 1.7 Pre-Launch Verification

```bash
# Test GitHub token
python3 -c "
import json, requests
config = json.load(open('projects/resistance-research/phase-1-adoption-tracking.json'))
headers = {'Authorization': f'token {config[\"github_token\"]}'}
resp = requests.get('https://api.github.com/user', headers=headers)
print('GitHub auth:', 'OK' if resp.status_code == 200 else f'FAILED ({resp.status_code})')
"

# Test Gmail setup
python3 projects/resistance-research/phase-1-adoption-tracking-script.py --run-now --config projects/resistance-research/phase-1-adoption-tracking.json 2>&1 | head -20

# Verify log directory is writable
touch projects/resistance-research/logs/test.log && rm projects/resistance-research/logs/test.log && echo "Logs: OK"
```

---

## Part 2 — Scheduling Weekly Runs

### 2.1 Cron Job Setup (Recommended)

Schedule the script to run every Monday at 08:00 AM UTC (offset from measurement checkpoint):

```bash
# Print recommended crontab entry
python3 projects/resistance-research/phase-1-adoption-tracking-script.py --schedule-weekly

# Expected output:
# Add this line to your crontab (crontab -e):
# 0 8 * * 1 /usr/bin/python3 /full/path/to/phase-1-adoption-tracking-script.py --run-now --config /full/path/to/phase-1-adoption-tracking.json
```

Add the cron entry:

```bash
crontab -e
# Paste the line from above
# Save and exit (Ctrl+X, then Y, then Enter in nano)
```

Verify cron job:

```bash
crontab -l | grep phase-1-adoption
```

### 2.2 Manual Trigger (for testing)

Run immediately without waiting for scheduled time:

```bash
python3 projects/resistance-research/phase-1-adoption-tracking-script.py --run-now
```

Output appears in:
- stdout (terminal)
- `projects/resistance-research/logs/adoption-tracking.log` (log file)
- `projects/resistance-research/monitoring/week-[DATE]-summary.md` (Markdown report)

---

## Part 3 — Understanding Output

### 3.1 Weekly Summary File

Auto-generated each run as `monitoring/week-[DATE]-summary.md`:

```markdown
# Weekly Adoption Summary — May 20, 2026

## Gist View Counts
- **full_proposal**: 47 views
- **executive_summary**: 23 views
- ...

## Email Replies
Total replies: 3

- **From**: jane@brennancenter.org
  **Subject**: Question about Domain 6
  **Snippet**: We're interested in using the judicial independence analysis...

## ⚠️ Alerts Triggered
- ENGAGEMENT_STALL

## Errors
(none)
```

### 3.2 Log File

Check `projects/resistance-research/logs/adoption-tracking.log` for detailed execution logs:

```
2026-05-20 08:00:15 [INFO] ============================================================
2026-05-20 08:00:15 [INFO] PHASE 1 ADOPTION TRACKING — Weekly Collection
2026-05-20 08:00:15 [INFO] Timestamp: 2026-05-20T08:00:15.xxx
2026-05-20 08:00:15 [INFO] ============================================================
2026-05-20 08:00:16 [INFO] [1/3] Fetching Gist view counts...
2026-05-20 08:00:18 [INFO] Fetched Gist 2dec7fd... metadata: 0 comments
2026-05-20 08:00:19 [INFO] [2/3] Fetching recent email replies...
2026-05-20 08:00:21 [INFO] Searching Gmail with query: after:2026/05/13
2026-05-20 08:00:22 [INFO] Found 3 messages
```

### 3.3 JSON Output (stdout)

When run with `--run-now`, outputs complete JSON to stdout:

```json
{
  "timestamp": "2026-05-20T08:00:15.123456",
  "gist_views": {
    "full_proposal": {
      "gist_id": "2dec7fd03b08ab5b41c55d402f44c261",
      "cumulative_views": 47,
      "fetched_at": "2026-05-20T08:00:18.xxx"
    },
    ...
  },
  "email_replies": [
    {
      "id": "abc123",
      "from": "jane@brennancenter.org",
      "subject": "Question about Domain 6",
      "date": "Mon, 20 May 2026 15:30:00 +0000",
      "snippet": "We're interested in using the judicial independence analysis..."
    }
  ],
  "leading_alerts": [],
  "errors": []
}
```

---

## Part 4 — Manual Spreadsheet Updates

If not using Sheets sync, manually update your tracking spreadsheet weekly:

### 4.1 Gist View Log (Sheet 3)

Copy cumulative view counts from weekly summary:

| week_1_cumulative | week_1_delta | spike_flag |
|-------------------|--------------|------------|
| 47 | 47 | NO |
| 23 | 23 | NO |

### 4.2 Master Contact Log (Sheets 1)

Update `gist_views_d7` and `engagement_score` columns based on:

- **Gist views >0**: `engagement_score >= 1`
- **Email reply received**: `engagement_score >= 2`
- **Multiple signals**: `engagement_score >= 3`

Use the Engagement Score Rubric from `phase-1-adoption-tracking-automation.md` Part 2.

### 4.3 Citation Log (Sheet 4)

Add any citations detected through Google Alerts:

| date_detected | citing_org | document_title | attribution_confidence |
|---------------|-----------|----------------|----------------------|
| 2026-05-20 | Brennan Center | "Judicial Independence Brief" | High |

---

## Part 5 — Troubleshooting

### "GitHub token invalid"

```
✗ Failed to fetch analytics for Gist 2dec7fd...: 401 Unauthorized
```

**Fix**: Check GitHub token in `phase-1-adoption-tracking.json`. Regenerate if needed at https://github.com/settings/tokens.

### "Gmail credentials not found"

```
✗ Gmail authentication failed: [Errno 2] No such file or directory: '/path/to/gmail-oauth-credentials.json'
```

**Fix**: Create OAuth credentials (Part 1.4) and update `phase-1-adoption-tracking.json` path.

### "Gist views at 0 after sending"

This is normal for the first 24 hours. Views update daily. Check again in 48 hours. If still zero after 7 days:

1. Verify Gist URLs in outreach emails are correct
2. Check if URL is broken: open `https://gist.github.com/[username]/[GIST_ID]` manually
3. Test with direct email: send yourself the Gist URL to confirm email isn't filtering it

### "No email replies detected"

Normal for Day 0-7. Check again at Day 14+. If zero by Day 28:

1. Confirm outreach email account is configured in Gmail OAuth
2. Run `--run-now` with debug output: `python3 ... 2>&1 | grep -i email`
3. Check spam folder manually for bounces or misdirected replies

---

## Part 6 — Monitoring Checklist (Weekly)

Every Monday after the script runs (or manually weekly):

- [ ] Read weekly summary file: `monitoring/week-[DATE]-summary.md`
- [ ] Check for alert flags (engagement stall, zero views, zero replies)
- [ ] Review email replies — respond within 48 hours per Part 4 templates in `phase-1-adoption-tracking-automation.md`
- [ ] Update Master Contact Log with new engagement scores
- [ ] Update Gist View Log with new cumulative counts
- [ ] Log any citations detected manually via Google Alerts
- [ ] Check logs for errors: `tail -30 logs/adoption-tracking.log`

---

## Part 7 — Integration with Phase 1 Operator's Guide

This script automates **Part 3** (Data Collection Methods) of `phase-1-adoption-tracking-automation.md`:

| Method | Script Feature | Manual Fallback |
|--------|---|---|
| Gist View Tracking (3.1) | ✅ Automated (weekly) | View `https://gist.github.com/[user]/[ID]/analytics` |
| Email Reply Monitoring (3.2) | ✅ Automated (weekly) | Check outreach email account daily |
| Google Alerts (3.3) | ⚠️ Manual setup only | Review Google Alerts folder weekly |
| Google Scholar Alerts (3.4) | ⚠️ Manual setup only | N/A (low volume) |
| CourtListener Monitoring (3.5) | ⚠️ Manual setup only | Check CourtListener weekly |
| LegiScan API (3.6) | ⚠️ Manual setup only | Check state legislative sites manually |
| Secondary Distribution (3.7) | ⚠️ Manual only | Monthly site searches |
| Overton.io (3.8) | ⚠️ Manual only | Monthly Overton searches (Month 4+) |

**Script focus**: Automates the two highest-friction data sources (Gist analytics + email monitoring). Other methods remain manual but are documented in the Operator's Guide.

---

## Part 8 — Running the Script for the First Time

### Pre-Flight Checklist

- [ ] Configuration file created: `phase-1-adoption-tracking.json`
- [ ] GitHub token valid
- [ ] Gmail OAuth credentials downloaded
- [ ] Monitoring directory created: `projects/resistance-research/monitoring/`
- [ ] Python dependencies installed
- [ ] Credentials files added to `.gitignore`

### Initial Test Run

```bash
cd /path/to/SuperClaude_Framework

# Run the script manually (test)
python3 projects/resistance-research/phase-1-adoption-tracking-script.py --run-now

# Expected output:
# 1. Console messages (INFO/WARNING/ERROR)
# 2. JSON summary to stdout
# 3. New file: monitoring/week-[DATE]-summary.md
# 4. Log entries in logs/adoption-tracking.log

# Verify success
cat projects/resistance-research/logs/adoption-tracking.log | tail -10
cat projects/resistance-research/monitoring/week-*.md
```

### Schedule for Future Runs

```bash
# Add cron job
python3 projects/resistance-research/phase-1-adoption-tracking-script.py --schedule-weekly
# Copy the output line
crontab -e
# Paste the line
```

---

## Part 9 — Maintenance & Extensions

### Monthly: Review and Archive

Each month, move completed weekly summaries to archive:

```bash
mkdir -p projects/resistance-research/monitoring/archive/$(date +%Y-%m)
mv projects/resistance-research/monitoring/week-*.md projects/resistance-research/monitoring/archive/$(date +%Y-%m)/
```

### Quarterly: Rotate Credentials

GitHub tokens and Gmail OAuth tokens have expiration dates. Before expiration:

1. Generate new GitHub token (same process as Part 1.3)
2. Gmail tokens auto-refresh (no action needed)
3. Update `phase-1-adoption-tracking.json` with new token

### Extension: Add Citation Alerts

To auto-detect citations, enable and configure these optional monitoring sources:

**Google Alerts** (Part 3.3 of Operator's Guide):
```bash
# Once configured at news.google.com/alerts, the script can parse alerts
# Extend EmailReplyMonitor.get_recent_replies() to filter for alert emails
```

**CourtListener** (Part 3.5 of Operator's Guide):
```bash
# Add CourtListenerMonitor class using free API
# https://www.courtlistener.com/api/
```

---

## Questions & Support

Refer to the companion documents:

- **Conceptual framework**: `phase-1-adoption-tracking-automation.md` (Parts 1-6)
- **Spreadsheet schema**: `adoption-automation-infrastructure.md`
- **Contact list**: `DISTRIBUTION_OUTREACH_CONTACTS.md`
- **Success criteria**: `phase-1-adoption-tracking-automation.md` Part 7

---

**Last updated**: 2026-05-30  
**Script version**: 1.0  
**Python version required**: 3.8+
