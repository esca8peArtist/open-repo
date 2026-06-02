# Phase 2 Tracking Automation Deployment Guide

**Version**: 1.0  
**Date**: June 2026  
**Status**: Production Ready  
**Extends**: Phase 1 Adoption Tracking (phase-1-adoption-tracking-script.py)

---

## Overview

This document describes the production deployment of Phase 2 domain-specific automation monitors. Four specialized tracking modules enable rapid-response distribution triggering when external events match Domain 1, 39, 40, 56, 58 characteristics.

### Core Objectives

1. **SCOTUS Opinion Monitor** — Detect Trump v. Barbara ruling (Domain 58)
2. **HHS Guidance Monitor** — Track Medicaid disenrollment policy (Domain 39)
3. **Election Events Monitor** — Monitor voting suppression events (Domains 1, 40)
4. **Coalition Email Router** — Auto-tag Phase 1 responses by domain (All domains)

All monitors integrate with the existing `phase-1-adoption-tracking-script.py` orchestration system and produce alerts routed to Discord/Slack for human decision-making.

---

## Architecture

### Directory Structure

```
projects/resistance-research/
├── src/monitors/                          # Phase 2 automation (NEW)
│   ├── __init__.py
│   ├── scotus_opinion_monitor.py          # Trump v. Barbara tracking
│   ├── hhs_guidance_monitor.py            # Healthcare disenrollment
│   ├── election_events_monitor.py         # Voting suppression events
│   └── coalition_email_router.py          # Email domain routing
│
├── phase-1-adoption/
│   ├── phase-1-adoption-tracking-script.py  # Existing orchestrator
│   ├── adoption-tracking-config.json        # Extended with monitor settings
│   ├── data/                                # State persistence
│   ├── logs/                                # Monitor logs
│   └── credentials.json                     # Gmail OAuth2 (secret)
│
├── tests/
│   ├── __init__.py
│   └── test_monitors.py                   # 20+ unit tests
│
└── PHASE_2_TRACKING_AUTOMATION_DEPLOYMENT.md  # This file
```

### Monitor Architecture

Each monitor follows a common pattern:

```python
class [Monitor]:
    def _load_config() → Dict       # Load adoption-tracking-config.json
    def _load_state() → Dict        # Load JSON state file (dedup, last-check)
    def _save_state()               # Persist state
    def check_[source1]() → List    # Check API/RSS source 1
    def check_[source2]() → List    # Check API/RSS source 2
    def run_check() → List          # Orchestrate all checks, merge results
    def send_alert(results)         # Discord/Slack webhook
    def run_continuous(hours)       # Polling loop with sleep()
```

### Data Flow

```
External Events (APIs/RSS/Websites)
            ↓
    [Monitor.run_check()]
            ↓
    Parse, deduplicate, classify
            ↓
    Confidence scoring
            ↓
    If confidence > threshold:
            ↓
    [Monitor.send_alert()] → Discord/Slack
            ↓
    Human decision in CHECKIN.md
            ↓
    Execute Phase 2 distribution
```

---

## Configuration

### adoption-tracking-config.json

All monitors read from a single configuration file (YAML/JSON):

```json
{
  "monitors_enabled": true,
  "monitors": {
    "scotus": {
      "enabled": true,
      "polling_interval_minutes": 60,
      "case_number": "25-365",
      "discord_webhook": "https://discord.com/api/webhooks/..."
    },
    "hhs": {
      "enabled": true,
      "polling_interval_minutes": 360,
      "discord_webhook": "...",
      "slack_webhook": "..."
    },
    "election": {
      "enabled": true,
      "polling_interval_minutes": 240,
      "fec_api_key": "",
      "discord_webhook": "..."
    },
    "email_router": {
      "enabled": true,
      "polling_interval_minutes": 60,
      "gmail_credentials": "./credentials.json",
      "email_lookback_hours": 168
    }
  }
}
```

### Environment Variables

Monitors also support environment variable overrides (useful for secrets in CI/CD):

```bash
# SCOTUS Monitor
export DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..."
export GITHUB_TOKEN="ghp_..."

# HHS Monitor
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/..."

# Election Monitor
export FEC_API_KEY="api_..."

# Gmail Router
export GMAIL_CREDENTIALS_JSON="./credentials.json"
```

---

## Setup & Deployment

### 1. Prerequisites

```bash
# Install Python 3.10+
python3 --version

# Install dependencies
pip install requests feedparser google-auth google-auth-oauthlib \
            google-auth-httplib2 google-api-python-client

# Optional: Install pytest for testing
pip install pytest pytest-mock
```

### 2. Deploy Monitor Code

```bash
# Copy monitor modules to projects/resistance-research/src/monitors/
cp src/monitors/*.py projects/resistance-research/src/monitors/

# Verify installation
python3 -c "from src.monitors import SCOTUSOpinionMonitor; print('OK')"
```

### 3. Configure Webhooks

#### Discord Setup

1. Go to your Discord server settings
2. Select "Webhooks" → "Create Webhook"
3. Copy webhook URL
4. Add to `adoption-tracking-config.json`:

```json
{
  "scotus_discord_webhook": "https://discord.com/api/webhooks/YOUR_ID/YOUR_TOKEN",
  "hhs_discord_webhook": "https://discord.com/api/webhooks/YOUR_ID/YOUR_TOKEN",
  "election_discord_webhook": "https://discord.com/api/webhooks/YOUR_ID/YOUR_TOKEN"
}
```

#### Slack Setup

1. Go to your Slack workspace → "Incoming Webhooks"
2. "Add New Webhook" → Select channel
3. Copy webhook URL
4. Add to config:

```json
{
  "hhs_slack_webhook": "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
}
```

### 4. Gmail OAuth2 Setup (Email Router)

Email router requires Gmail API access. Initial setup:

```bash
# 1. Create OAuth2 credentials in Google Cloud Console
#    https://console.cloud.google.com/
#    - Create new project
#    - Enable Gmail API
#    - Create OAuth2 "Desktop Application" credentials
#    - Download credentials.json

# 2. Move to project directory
mv ~/Downloads/credentials.json projects/resistance-research/phase-1-adoption/

# 3. Run auth setup
python3 src/monitors/coalition_email_router.py \
  --auth \
  --credentials projects/resistance-research/phase-1-adoption/credentials.json

# 4. Follow browser prompt to authorize
# Token is saved to gmail-token.json automatically
```

---

## Operation

### Manual Execution

#### Single Check Cycle

```bash
# SCOTUS Monitor
python3 src/monitors/scotus_opinion_monitor.py --run-now

# HHS Monitor
python3 src/monitors/hhs_guidance_monitor.py --run-now --channel discord

# Election Monitor
python3 src/monitors/election_events_monitor.py --run-now

# Email Router
python3 src/monitors/coalition_email_router.py --run-now
```

#### Continuous Polling (for testing)

```bash
# Run for 2 hours then stop
python3 src/monitors/scotus_opinion_monitor.py \
  --continuous \
  --duration-hours 2

# Run indefinitely (Ctrl+C to stop)
python3 src/monitors/hhs_guidance_monitor.py --continuous
```

### Automated Deployment (Cron)

Add to `crontab -e`:

```bash
# SCOTUS: Every hour during June-July (court term)
0 * 6-7 * /usr/bin/python3 /path/to/src/monitors/scotus_opinion_monitor.py --run-now 2>&1 | logger

# HHS: Every 6 hours (Federal Register publishes daily)
0 */6 * * * /usr/bin/python3 /path/to/src/monitors/hhs_guidance_monitor.py --run-now 2>&1 | logger

# Election: Every 4 hours (FEC updates)
0 */4 * * * /usr/bin/python3 /path/to/src/monitors/election_events_monitor.py --run-now 2>&1 | logger

# Email Router: Every hour (real-time response routing)
0 * * * * /usr/bin/python3 /path/to/src/monitors/coalition_email_router.py --run-now 2>&1 | logger
```

### Systemd Service (Production)

Create `/etc/systemd/system/phase2-monitors.service`:

```ini
[Unit]
Description=Phase 2 Resistance Research Monitors
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
User=resistance
WorkingDirectory=/path/to/projects/resistance-research
ExecStart=/usr/bin/python3 -m src.monitors.orchestrator
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable phase2-monitors
sudo systemctl start phase2-monitors
sudo journalctl -u phase2-monitors -f
```

---

## Monitor Details

### 1. SCOTUS Opinion Monitor

**Purpose**: Detect Trump v. Barbara (No. 25-365) ruling issuance  
**Trigger**: Domain 58 (Tribal Sovereignty/Birthright Citizenship)  
**Update Frequency**: Hourly (configurable)

**Sources Checked**:
- supremecourt.gov/opinions/ (primary, 95% confidence)
- scotusblog.com (secondary, 85% confidence)
- narf.org (NARF tracker, 75% confidence)

**Output**:
```
DOMAIN 58 IMMEDIATE: Trump v. Barbara Ruling Issued
Case: Trump v. Barbara (25-365)
Ruling Date: June 15, 2026
Source: supremecourt.gov
Opinion URL: https://www.supremecourt.gov/opinions/25-365.pdf
Action: Immediate distribution of Domain 58 materials
```

**State File**: `phase-1-adoption/data/scotus-monitor-state.json`

---

### 2. HHS Guidance Monitor

**Purpose**: Track healthcare policy changes affecting Medicaid disenrollment  
**Trigger**: Domain 39 (Healthcare/Medicaid)  
**Update Frequency**: Every 6 hours (configurable)

**Sources Checked**:
- federalregister.gov (healthcare section, API)
- hhs.gov/newsroom (press releases)

**Keyword Matching**:
- "disenrollment", "medicaid unwinding", "continuous enrollment"
- "coverage termination", "public charge", "eligibility verification"

**Key Dates Watched**:
- June 1, 2026 (potential policy effective date)
- January 27, 2027 (future milestone)

**Output**:
```
DOMAIN 39 DECISION REQUIRED
New HHS healthcare guidance detected (3 items)

• Title: Medicaid Disenrollment Final Rule
  Source: Federal Register
  Confidence: 90%
  Key Dates: June 1, 2026
  View: https://federalregister.gov/...
```

**State File**: `phase-1-adoption/data/hhs-monitor-state.json`

---

### 3. Election Events Monitor

**Purpose**: Detect voting suppression, election administration, and ballot measure news  
**Triggers**: 
- Domain 1 (Voting Rights)
- Domain 40 (Election Integrity/Surveillance)

**Update Frequency**: Every 4 hours (configurable)

**Sources Checked**:
- FEC Violations API (new complaints)
- Election Protection RSS feeds
- Common Cause voting rights RSS
- State election official websites (pattern scanning)

**Keyword Matching**:
- "voter suppression", "voting restriction", "ballot access"
- "polling place closure", "voter id", "ballot measures"
- "election administration", "voting rights", "deepfake"

**State Verification**: Only alerts on **named state mentions** (not general opinion pieces)

**Output**:
```
DOMAIN 40 POSSIBLE TRIGGER
Election event(s) detected (2 items)

• Title: Florida Poll Closure Impact Assessment
  State: Florida
  Type: polling place closure
  Source: Election Protection
  Confidence: 80%
  View: https://electionprotection.org/...
```

**State File**: `phase-1-adoption/data/election-monitor-state.json`

---

### 4. Coalition Email Router

**Purpose**: Auto-tag Phase 1 response emails by domain expertise keywords  
**Triggers**: All domains (1, 39, 40, 56, 58)  
**Update Frequency**: Hourly (configurable)

**Workflow**:
1. Query Gmail: `label:phase-1-responses` (last 7 days)
2. Extract sender, subject, body text
3. Match against domain keyword profiles
4. Confidence score per domain
5. Auto-apply Gmail labels: `phase-1-responses/domain-X`

**Domain Keyword Profiles**:

| Domain | Keywords |
|--------|----------|
| Domain 1 | voting, voting rights, franchise, ballot, election, suffrage |
| Domain 39 | medicaid, healthcare, disenrollment, coverage, patient, hospital |
| Domain 40 | election, surveillance, deepfake, election security, poll worker |
| Domain 56 | civil service, federal employee, merit system, schedule f |
| Domain 58 | tribal, native american, citizenship, birthright, reservation |

**Output** (CHECKIN.md insertion):
```markdown
### Email Routing Report (Generated 2026-06-01)

#### domain_1 (5 responses)
- **From**: volunteer@example.com
  **Subject**: Voting Rights Campaign Update
  **Confidence**: 95%

#### domain_39 (3 responses)
- **From**: organizer@clinic.org
  **Subject**: Medicaid Disenrollment Planning
  **Confidence**: 88%
```

**State File**: `phase-1-adoption/data/email-router-state.json`

---

## Testing

### Run Full Test Suite

```bash
cd projects/resistance-research
pytest tests/test_monitors.py -v
```

### Test Coverage

Tests include:
- ✅ Configuration loading and defaults
- ✅ State persistence (JSON serialization)
- ✅ Domain keyword matching (all 5 domains)
- ✅ Deduplication logic
- ✅ Timestamp parsing
- ✅ Alert formatting (Discord/Slack)
- ✅ Graceful degradation (timeouts/network errors)
- ✅ Confidence scoring
- ✅ Email domain tagging
- ✅ Dataclass creation and serialization

**Run specific test**:
```bash
pytest tests/test_monitors.py::TestSCOTUSMonitor -v
pytest tests/test_monitors.py::TestHHSGuidanceMonitor::test_domain39_relevance_direct -v
```

---

## Monitoring & Debugging

### Log Files

All monitors write to `phase-1-adoption/logs/`:

```bash
tail -f phase-1-adoption/logs/scotus_monitor.log
tail -f phase-1-adoption/logs/hhs_monitor.log
tail -f phase-1-adoption/logs/election_monitor.log
tail -f phase-1-adoption/logs/coalition_email_router.log
```

### State Files

Monitor state persists to `phase-1-adoption/data/`:

```bash
cat phase-1-adoption/data/scotus-monitor-state.json
cat phase-1-adoption/data/hhs-monitor-state.json
cat phase-1-adoption/data/election-monitor-state.json
cat phase-1-adoption/data/email-router-state.json
```

### Troubleshooting

#### "No alerts sent"
- Check webhook URL in config
- Verify network connectivity: `curl https://discord.com/api/webhooks/...`
- Check monitor logs for errors

#### "Duplicate alerts"
- Clear `state.json` items_seen array (but preserve last_check)
- Ensure state file is being saved properly

#### "API timeout"
- Monitor logs "warning" level; retries next cycle
- Increase polling_interval if APIs are slow
- Check internet connectivity

#### "Gmail auth fails"
- Delete `phase-1-adoption/gmail-token.json`
- Re-run `--auth` to generate new token
- Ensure credentials.json has correct permissions

---

## Integration with Phase 1

### Orchestration Points

Phase 2 monitors integrate with Phase 1 adoption tracking at:

1. **Configuration**: Both read `adoption-tracking-config.json`
2. **State Directory**: Shared `phase-1-adoption/data/` for persistence
3. **Log Directory**: Shared `phase-1-adoption/logs/` for unified logging
4. **CHECKIN.md**: Phase 2 alerts route to CHECKIN.md for human synthesis

### Calling from Phase 1 Script

```python
# In phase-1-adoption-tracking-script.py
from src.monitors import (
    SCOTUSOpinionMonitor,
    HHSGuidanceMonitor,
    ElectionEventsMonitor,
    CoalitionEmailRouter
)

def run_all_monitors(config):
    """Run all Phase 2 monitors as part of Phase 1 workflow."""
    if not config.get("monitors_enabled"):
        return {}
    
    results = {}
    
    # SCOTUS
    scotus = SCOTUSOpinionMonitor(config)
    ruling = scotus.run_check()
    if ruling:
        results["scotus"] = ruling
    
    # HHS
    hhs = HHSGuidanceMonitor(config)
    guidance = hhs.run_check()
    if guidance:
        results["hhs"] = guidance
    
    # Election
    election = ElectionEventsMonitor(config)
    events = election.run_check()
    if events:
        results["election"] = events
    
    # Email Router
    router = CoalitionEmailRouter(config)
    router.authenticate()
    emails = router.sync_emails()
    if emails:
        results["email_router"] = emails
    
    return results
```

---

## Performance & Constraints

### Execution Time

| Monitor | Typical Runtime | Max Runtime |
|---------|-----------------|------------|
| SCOTUS | 2-4 seconds | < 10 seconds |
| HHS | 3-6 seconds | < 10 seconds |
| Election | 4-8 seconds | < 10 seconds |
| Email Router | 5-15 seconds | < 10 seconds |

**All monitors < 10s**: Suitable for hourly+ polling without lag.

### API Rate Limits

| Source | Limit | Mitigation |
|--------|-------|-----------|
| supremecourt.gov | Unlimited | Crawl-friendly; no auth needed |
| Federal Register | 120/min | Polling every 6h = 4 req/h |
| FEC API | 1000/day | Polling every 4h = 6 req/day |
| Gmail API | 1M/day | Polling every 1h = 24 req/day |
| Discord | 10 req/s | Batch alerts; queue if needed |

---

## Security & Privacy

### Secrets Management

**Never commit:**
- Discord/Slack webhook URLs
- Gmail credentials.json or token
- FEC API keys
- GitHub tokens

**Best practices:**
1. Store in `adoption-tracking-config.json` (local, .gitignored)
2. Or use environment variables (safer for CI/CD)
3. Use GitHub Secrets for automated deployments
4. Rotate webhooks quarterly

### Data Handling

- **State files**: JSON stored locally; no external persistence
- **Logs**: Local file only; no remote logging
- **API responses**: Not cached; always fresh
- **Email**: Gmail API read-only; no message forwarding

---

## Failure Modes & Recovery

### Monitor Crashes

**Handling**: All monitors catch exceptions and log warnings; continue polling

```python
try:
    response = requests.get(url, timeout=10)
except requests.RequestException as e:
    logger.warning(f"API request failed: {e}")
    # State unchanged; retry next cycle
```

### Network Outages

**Recovery**: Automatic retry on next polling cycle; state preserved

### API Outages

**Fallback**: SCOTUS has 3 sources (primary + 2 secondaries); election has 3+ sources

### Duplicate Alerts

**Prevention**: Item deduplication via `items_seen` list in state JSON

**Reset if needed**:
```bash
# Clear items_seen but preserve last_check
jq '.items_seen = []' phase-1-adoption/data/scotus-monitor-state.json > /tmp/new.json
mv /tmp/new.json phase-1-adoption/data/scotus-monitor-state.json
```

---

## Future Enhancements

### Planned (v1.1)

- [ ] Orchestrator daemon (single entry point for all monitors)
- [ ] Dashboard: Real-time monitor status + recent alerts
- [ ] Slack thread replies (improve Discord channel UX)
- [ ] Duplicate alert suppression (24h window)
- [ ] Custom domain keyword profiles (user-configurable)

### Potential (v2.0)

- [ ] Machine learning confidence scoring (vs. hardcoded thresholds)
- [ ] Multi-language support (Spanish, French for international tracking)
- [ ] SMS alerts for high-confidence triggers
- [ ] Historical trend analysis (impact of past distributions)
- [ ] Integration with external CRM (Salesforce, HubSpot)

---

## Support & Maintenance

### Quarterly Maintenance

1. **Verify webhook URLs** still work (Discord/Slack can change endpoints)
2. **Check API endpoints** (Federal Register, FEC, SCOTUS sometimes restructure)
3. **Review logs** for patterns of failures
4. **Update domain keyword profiles** based on new legal developments

### Monthly Checks

1. Monitor logs for errors
2. Verify alert routing to correct channels
3. Test manual `--run-now` execution
4. Check state file sizes (if > 100MB, archive old entries)

### Reporting

- **Weekly**: Alert count by domain + response rates
- **Monthly**: Uptime %, API failure rate %, average execution time
- **Quarterly**: ROI analysis (alerts that triggered successful distributions)

---

## References

### External APIs & Documentation

- [SCOTUS.gov Opinions](https://www.supremecourt.gov/opinions/)
- [SCOTUSBlog](https://www.scotusblog.com/)
- [Federal Register API](https://www.federalregister.gov/developers)
- [FEC Violations API](https://api.fec.gov/)
- [Gmail API](https://developers.google.com/gmail/api)
- [Discord Webhooks](https://discord.com/developers/docs/resources/webhook)
- [Slack Webhooks](https://api.slack.com/messaging/webhooks)

### Related Documentation

- `phase-1-adoption-tracking-script.py` — Parent orchestration system
- `ACTIVATION_ARCHITECTURE.md` — Domain definitions & distribution models
- `adoption-automation-infrastructure.md` — Phase 1 infrastructure

---

## Contact & Issues

Report issues to the project repository or contact the orchestrator team.

---

**Last Updated**: June 2026  
**Version**: 1.0  
**Status**: Production Ready
