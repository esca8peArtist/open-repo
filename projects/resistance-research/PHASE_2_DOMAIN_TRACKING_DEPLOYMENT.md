# Phase 2 Domain Tracking Automation — Deployment Guide

**Version**: 1.0  
**Date**: June 2, 2026  
**Status**: Production-ready — deploy immediately

---

## Overview

Four domain-specific monitoring classes integrated into the Phase 1 adoption-tracking
infrastructure. All monitors run in parallel via `ThreadPoolExecutor`, independent of
the existing Phase 1 Gist-polling workflow.

| Monitor | Domain | Polling | Alert Channel | Priority |
|---------|--------|---------|---------------|----------|
| Domain58SCOTUSMonitor | Trump v. Barbara ruling | 14 min | Discord | CRITICAL |
| Domain39HHSTracker | HHS healthcare guidance | 60 min | Discord + Slack | HIGH |
| Domain40ElectionMonitor | Election / deepfake events | 240 min | Discord | MEDIUM |
| Domain2CoalitionEmailRouter | Phase 2 email routing | 60 min | CHECKIN.md | MEDIUM |

---

## File Locations

```
projects/resistance-research/
├── src/
│   ├── phase_2_domain_trackers.py          # Unified module (4 wrapper classes + parallel runner)
│   └── monitors/
│       ├── __init__.py
│       ├── scotus_opinion_monitor.py        # Domain 58 — Trump v. Barbara
│       ├── hhs_guidance_monitor.py          # Domain 39 — HHS healthcare
│       ├── election_events_monitor.py       # Domain 40 — election/deepfake
│       └── coalition_email_router.py        # Phase 2 email tagging
├── phase-1-adoption/
│   ├── phase-1-adoption-tracking-script.py # Phase 1 + Phase 2 orchestrator (updated v2.1)
│   ├── adoption-tracking-config.json       # Shared config
│   └── data/
│       ├── scotus-monitor-state.json       # SCOTUS monitor persistence
│       ├── email-router-state.json         # Email router persistence
│       └── phase2-run-*.json               # Per-run combined logs
├── tests/
│   ├── test_monitors.py                    # Existing monitor unit tests
│   └── test_phase2_integration.py          # Phase 2 integration test suite (new)
└── PHASE_2_DOMAIN_TRACKING_DEPLOYMENT.md  # This file
```

---

## Prerequisites

### 1. Python dependencies

```bash
pip install requests
# Optional for RSS parsing:
pip install feedparser
# Required for email routing:
pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### 2. Environment variables

Set in `~/.bashrc` or `~/.zshrc`:

```bash
# Required for all Discord alerts
export DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/YOUR_ID/YOUR_TOKEN"

# Optional — per-monitor webhook overrides
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/YOUR_SLACK_WEBHOOK"

# Optional — raises GitHub API from 60 to 5000 req/hr
export GITHUB_TOKEN="your_github_pat"

# Optional — raises FEC API from 20 to 1000 req/hr
export FEC_API_KEY="your_fec_api_key"

# Required only if using email router
export GMAIL_CREDENTIALS_JSON="/path/to/credentials.json"
```

### 3. Discord webhook setup

1. Create a Discord server (or use existing one)
2. Create a channel: `#domain-alerts`
3. Channel Settings > Integrations > Webhooks > New Webhook
4. Copy URL → set as `DISCORD_WEBHOOK_URL`

---

## Configuration File

Edit `phase-1-adoption/adoption-tracking-config.json`:

```json
{
  "github_token": "YOUR_PAT",
  "github_username": "esca8peArtist",

  "scotus_discord_webhook": "https://discord.com/api/webhooks/...",
  "scotus_polling_interval_minutes": 14,

  "hhs_discord_webhook": "https://discord.com/api/webhooks/...",
  "hhs_slack_webhook": "https://hooks.slack.com/...",
  "hhs_polling_interval_minutes": 60,

  "election_discord_webhook": "https://discord.com/api/webhooks/...",
  "election_polling_interval_minutes": 240,

  "gmail_enabled": true,
  "gmail_credentials": "/home/user/.config/gmail/credentials.json",
  "gmail_label": "phase-1-responses",
  "email_lookback_hours": 168,
  "email_polling_interval_minutes": 60,

  "phase1_start_date": "2026-05-28"
}
```

All four monitors share the same config file. If `scotus_discord_webhook` is missing,
they fall back to `DISCORD_WEBHOOK_URL` from the environment.

---

## First-Time Setup

### Step 1: Verify configuration

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-adoption
python3 phase-1-adoption-tracking-script.py --check-config
```

Expected output: all rows marked `[OK]` except optional Gmail/Bitly entries.

### Step 2: Gmail OAuth2 authentication (email router only)

```bash
python3 ../src/phase_2_domain_trackers.py --auth-gmail
```

This opens a browser. Complete the OAuth2 flow. Token is saved to
`phase-1-adoption/gmail-token.json` and reused on subsequent runs.

If running headlessly (Raspberry Pi, server), use the `oauth2_login.py` helper:

```bash
python3 phase-1-adoption/oauth2_login.py
```

### Step 3: Run a single parallel check

```bash
# Phase 2 monitors only
python3 ../src/phase_2_domain_trackers.py --run-now

# Phase 1 + Phase 2 together
python3 phase-1-adoption-tracking-script.py --run-all
```

### Step 4: Verify Discord alert reaches channel

The SCOTUS monitor will log "No ruling found; case still pending" — this is correct
until the ruling is issued. Check Discord for a test embed (only fires on actual
ruling detection).

To trigger a test alert without a real ruling, temporarily set:
```python
monitor._monitor.state["ruling_found"] = False
```
in a Python shell, then call `monitor.run_once()` against a patched response.

---

## Cron Setup

### Option A: Comprehensive (recommended)

Runs Phase 1 + Phase 2 together weekly. SCOTUS also on its own 14-minute schedule.

```bash
crontab -e
```

Add:

```cron
# Phase 1 + Phase 2 full suite — every Monday 09:00 UTC
0 9 * * 1 /usr/bin/python3 /home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-adoption/phase-1-adoption-tracking-script.py --run-all >> /home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-adoption/logs/cron.log 2>&1

# SCOTUS sub-15-minute polling — every 14 minutes, 24/7
*/14 * * * * /usr/bin/python3 /home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-adoption/phase-1-adoption-tracking-script.py --run-phase2 >> /home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-adoption/logs/cron-phase2.log 2>&1
```

The `--run-phase2` cron also runs HHS, election, and email monitors at their own
intervals — the script only calls each monitor's `run_once()` when its interval
has elapsed since the last check (tracked in the state JSON files).

### Option B: Standalone phase2 trackers (if Phase 1 already scheduled)

```cron
# Phase 2 only — 14-minute master tick
*/14 * * * * /usr/bin/python3 /home/awank/dev/SuperClaude_Framework/projects/resistance-research/src/phase_2_domain_trackers.py --run-now >> /home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-adoption/logs/cron-phase2.log 2>&1
```

### Verify cron installation

```bash
crontab -l | grep adoption
```

---

## Alert Routing

### Discord embed structure

**SCOTUS ruling (CRITICAL)**:
- Color: Red (#E74C3C)
- Title: `DOMAIN 58 IMMEDIATE: Trump v. Barbara Ruling Issued`
- Fields: Case, Ruling Date, Source, Confidence, Opinion URL, Distribution Routing
- CHECKIN.md: Written automatically

**HHS guidance (IMMEDIATE / DECISION_REQUIRED)**:
- Color: Blue (domain_39 direct) / Orange (domain_39_adjacent)
- Title: `DOMAIN 39 IMMEDIATE` or `DOMAIN 39 DECISION REQUIRED`
- CHECKIN.md: Written for direct domain_39 hits only

**Election/deepfake events**:
- Color: Red
- Title: `DOMAIN 40 DEEPFAKE ALERT` or `DOMAIN 40 POSSIBLE TRIGGER`
- CHECKIN.md: Written for deepfake-keyword items only

**Coalition email tags**:
- No Discord alert (Gmail tagging is silent)
- CHECKIN.md: Routing report appended on each tagged batch

### CHECKIN.md integration

All urgent alerts are appended under new `##` headings (never overwrite).
Check `CHECKIN.md` daily during active distribution windows (June–December 2026).

---

## Monitoring Windows

| Monitor | Active Window | Rationale |
|---------|--------------|-----------|
| SCOTUS (Domain 58) | June 1 – July 31, 2026 | Court term; ruling expected late June–early July |
| HHS (Domain 39) | June 1 – December 31, 2026 | Active Medicaid unwinding and comment windows |
| Election (Domain 40) | June 1 – November 4, 2026 | Pre-midterm election protection window |
| Email Router | Ongoing | Always active while Phase 2 distribution running |

---

## State Files

Each monitor persists state to prevent duplicate alerts:

| File | Monitor | Key Fields |
|------|---------|------------|
| `data/scotus-monitor-state.json` | Domain 58 | `ruling_found`, `ruling_date`, `alerts_sent` |
| `data/hhs-monitor-state.json` | Domain 39 | `items_seen[]`, `alerts_sent` |
| `data/election-monitor-state.json` | Domain 40 | `items_seen[]`, `alerts_sent` |
| `data/email-router-state.json` | Coalition | `messages_processed`, `messages_tagged` |
| `data/phase2-run-*.json` | Combined | Per-run summary for all 4 monitors |

To reset a monitor (e.g., re-test alert), delete its state file:
```bash
rm /home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-adoption/data/scotus-monitor-state.json
```

---

## Testing

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/resistance-research

# Existing monitor unit tests
python3 -m pytest tests/test_monitors.py -v

# Phase 2 integration tests
python3 -m pytest tests/test_phase2_integration.py -v

# All tests
python3 -m pytest tests/ -v
```

---

## Troubleshooting

**SCOTUS monitor not detecting ruling**:
- Check `logs/scotus_monitor.log` for HTTP errors
- Verify `supremecourt.gov` is reachable: `curl -I https://www.supremecourt.gov/`
- Confirm `ruling_found` is `false` in state file (not stuck True from prior run)

**HHS monitor returning no results**:
- Federal Register API requires no key (public); check for HTTP 429 (rate limit)
- Verify `hhs-monitor-state.json` not overflowing (trimmed at 200 items automatically)

**Election monitor returning no results**:
- FEC API has low public rate limit; set `FEC_API_KEY` for higher quota
- Election Protection RSS may change URL; check `election_monitor.log`

**Email router not tagging**:
- Run `--auth-gmail` to refresh expired OAuth2 token
- Verify Gmail label `phase-1-responses` exists in inbox
- Check `coalition_email_router.log` for API errors

**Discord alerts not arriving**:
- Verify `DISCORD_WEBHOOK_URL` is set: `echo $DISCORD_WEBHOOK_URL`
- Test webhook: `curl -X POST $DISCORD_WEBHOOK_URL -H "Content-Type: application/json" -d '{"content":"test"}'`
- Check that webhook channel has not been deleted or permissions changed

---

## Reference Files

- `DOMAIN_58_TRUMP_V_BARBARA_RAPID_RESPONSE.md` — Post-ruling distribution checklist
- `DOMAIN_39_MONITORING_AND_PHASE_2_ACTIVATION.md` — HHS guidance response routing
- `domain-40-surveillance-capitalism-electoral-manipulation.md` — Domain 40 research
- `COALITION_MANAGEMENT_PLAYBOOK.md` — Email routing triage procedures
- `CHECKIN.md` — Live alert feed (check daily)
- `phase-1-adoption/logs/` — All monitor logs
