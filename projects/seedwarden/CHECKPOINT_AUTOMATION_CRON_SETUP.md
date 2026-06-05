---
title: "Checkpoint Automation Cron Setup — Track B Day 3/7/14"
created: 2026-06-05
item: 85
status: production-ready
purpose: >
  Step-by-step cron schedule, environment variable setup, notification routing,
  and .env file reference for TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py.
references:
  - TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py (the script this document configures)
  - CONTINGENCY_TRIGGER_DECISION_TREE.md (thresholds and runbooks)
  - TRACK_B_MONITORING_AUTOMATION_FRAMEWORK.md (manual metric collection procedures)
---

# Checkpoint Automation Cron Setup
## Track B Day 3 / 7 / 14 Post-Launch Checkpoints

**Script**: `TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py`
**Machine**: raspby1 (Raspberry Pi 5, 100.70.184.84) — same machine as the orchestrator
**User account**: awank
**Working directory**: `/home/awank/dev/SuperClaude_Framework/projects/seedwarden/`
**Output directory**: `/home/awank/dev/SuperClaude_Framework/projects/seedwarden/CHECKPOINT_REPORTS/`

---

## 1. Checkpoint Schedule

| Checkpoint | Date | UTC Time | Purpose |
|------------|------|----------|---------|
| Day 3 | June 7, 2026 | 09:00 UTC | Early pulse — catch critical failures before they compound |
| Day 7 | June 11, 2026 | 10:00 UTC | Channel velocity — Phase 2 scope decision |
| Day 14 | June 18, 2026 | 11:00 UTC | Full 14-day review — Phase 2 expansion go/no-go |

Times are staggered (09:00 / 10:00 / 11:00) to avoid any cron collision and to give the
previous checkpoint's report 60+ minutes of buffer before the next day's check.

---

## 2. Environment Variable Setup

### 2a. Required variables

These must be set for the live API calls to work. Missing required variables cause the
script to exit with an error (not silently skip).

| Variable | Source | Description |
|----------|--------|-------------|
| `CAMPAIGN_MONITOR_API_KEY` | Campaign Monitor > Account > API Keys | API key for all CM calls |
| `GIST_URL` | GitHub — full public URL of Zone Card Gist | e.g. `https://gist.github.com/esca8peArtist/db0b1798b5b70ff988367982176dc49d` |

### 2b. Optional variables (modules silently skip if absent)

| Variable | Source | Description |
|----------|--------|-------------|
| `CAMPAIGN_MONITOR_CAMPAIGN_ID_EMAIL1` | CM campaign URL | Campaign ID for Email 1 broadcast |
| `CAMPAIGN_MONITOR_CAMPAIGN_ID_EMAIL2` | CM campaign URL | Campaign ID for Email 2 broadcast |
| `CAMPAIGN_MONITOR_CAMPAIGN_ID_EMAIL3` | CM campaign URL | Campaign ID for Email 3 broadcast |
| `CAMPAIGN_MONITOR_CAMPAIGN_ID_EMAIL4` | CM campaign URL | Campaign ID for Email 4 broadcast |
| `CAMPAIGN_MONITOR_CAMPAIGN_ID_EMAIL5` | CM campaign URL | Campaign ID for Email 5 broadcast |
| `CAMPAIGN_MONITOR_LIST_ID` | CM > Lists | Subscriber list ID |
| `GIST_BASELINE_VIEWS` | Manually recorded at Day 0 | View count on June 4 at launch (default 0) |
| `ETSY_API_KEY` | Etsy Developer Portal | Etsy v3 API key |
| `ETSY_SHOP_ID` | Etsy shop URL or Shop Manager | Numeric shop ID |
| `KIT_API_KEY` | Kit Creator > Settings > API | Kit API secret key |
| `KIT_FORM_ID` | Kit > Landing Pages > form URL | Numeric form/landing page ID |
| `DISCORD_WEBHOOK_URL` | Discord channel settings | Webhook URL for checkpoint notifications |
| `LAUNCH_DATE` | Hardcoded default 2026-06-04 | Override if launch date slipped |
| `CHECKPOINT_REPORTS_DIR` | Default: `projects/seedwarden/CHECKPOINT_REPORTS` | Override output directory |

### 2c. Where to find Campaign Monitor campaign IDs

After sending a broadcast in Campaign Monitor, the campaign ID appears in the URL of the
report page:
```
https://app.createsend.com/reports/campaign/{CAMPAIGN_ID}/
```
Copy the hex string after `/campaign/` — that is the campaign ID. Store it in the
corresponding `CAMPAIGN_MONITOR_CAMPAIGN_ID_EMAIL{N}` variable.

---

## 3. .env File Setup

All environment variables should be stored in `~/.claude_env` on raspby1. This file is
sourced by the automation script at startup. It is never committed to git.

### 3a. Example `.env` file

Create the file:
```bash
nano ~/.claude_env
```

Paste and fill in the values:

```bash
# ============================================================
# Seedwarden Track B Checkpoint Automation — Environment Config
# ~/.claude_env
# NEVER commit this file to git — it contains API credentials.
# ============================================================

# --- Campaign Monitor ---
CAMPAIGN_MONITOR_API_KEY=your_campaign_monitor_api_key_here

# Campaign IDs (one per email in the welcome sequence)
# Find in CM: Campaign Report URL > /reports/campaign/{ID}/
CAMPAIGN_MONITOR_CAMPAIGN_ID_EMAIL1=
CAMPAIGN_MONITOR_CAMPAIGN_ID_EMAIL2=
CAMPAIGN_MONITOR_CAMPAIGN_ID_EMAIL3=
CAMPAIGN_MONITOR_CAMPAIGN_ID_EMAIL4=
CAMPAIGN_MONITOR_CAMPAIGN_ID_EMAIL5=
CAMPAIGN_MONITOR_LIST_ID=

# --- GitHub Gist ---
# Full public URL of the Zone Card Gist
GIST_URL=https://gist.github.com/esca8peArtist/db0b1798b5b70ff988367982176dc49d
# View count at launch (Day 0, June 4). Record manually from Gist page.
GIST_BASELINE_VIEWS=0

# --- Etsy ---
ETSY_API_KEY=your_etsy_api_key_here
# Find shop ID in Etsy URL: etsy.com/shop/{shop_name} -> Shop Manager -> shop numeric ID
ETSY_SHOP_ID=

# --- Kit Creator (ConvertKit) ---
KIT_API_KEY=your_kit_api_key_here
# Find form ID in Kit: Landing Pages -> click form -> URL contains /forms/{ID}
KIT_FORM_ID=

# --- Notification ---
# Discord webhook URL (optional — leave blank to skip)
DISCORD_WEBHOOK_URL=

# --- Overrides ---
# Uncomment and set if launch date changes from default 2026-06-04
# LAUNCH_DATE=2026-06-04
```

### 3b. Permissions

The `.claude_env` file contains API credentials. Lock its permissions to owner-only:
```bash
chmod 600 ~/.claude_env
```

---

## 4. Cron Job Definitions

### 4a. Add to crontab

Open the crontab editor:
```bash
crontab -e
```

Paste these three lines (copy exactly, including the env-file path):

```cron
# Seedwarden Track B — Day 3 checkpoint (June 7, 09:00 UTC)
0 9 7 6 * cd /home/awank/dev/SuperClaude_Framework/projects/seedwarden && /home/awank/.local/bin/uv run python TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py --day 3 --env-file ~/.claude_env >> /tmp/seedwarden_checkpoint_day3.log 2>&1

# Seedwarden Track B — Day 7 checkpoint (June 11, 10:00 UTC)
0 10 11 6 * cd /home/awank/dev/SuperClaude_Framework/projects/seedwarden && /home/awank/.local/bin/uv run python TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py --day 7 --env-file ~/.claude_env >> /tmp/seedwarden_checkpoint_day7.log 2>&1

# Seedwarden Track B — Day 14 checkpoint (June 18, 11:00 UTC)
0 11 18 6 * cd /home/awank/dev/SuperClaude_Framework/projects/seedwarden && /home/awank/.local/bin/uv run python TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py --day 14 --env-file ~/.claude_env >> /tmp/seedwarden_checkpoint_day14.log 2>&1
```

**Cron field reference**: `minute hour day-of-month month day-of-week`

| Field | Day 3 | Day 7 | Day 14 |
|-------|-------|-------|--------|
| Minute | 0 | 0 | 0 |
| Hour (UTC) | 9 | 10 | 11 |
| Day of month | 7 | 11 | 18 |
| Month | 6 (June) | 6 (June) | 6 (June) |
| Day of week | * (any) | * (any) | * (any) |

### 4b. Verify crontab

```bash
crontab -l
```

You should see all three lines. Confirm the dates and times are correct.

### 4c. Verify uv path

The cron job uses the full path to `uv`. Confirm it is correct:
```bash
which uv
# Expected: /home/awank/.local/bin/uv
```

If the path differs, update the crontab lines accordingly.

---

## 5. Error Handling and Notification

### 5a. Log files

Each checkpoint writes two output files:

1. **Console log** (stdout + stderr from cron):
   - Day 3: `/tmp/seedwarden_checkpoint_day3.log`
   - Day 7: `/tmp/seedwarden_checkpoint_day7.log`
   - Day 14: `/tmp/seedwarden_checkpoint_day14.log`

2. **Markdown checkpoint report** (written by the script):
   - Located in `projects/seedwarden/CHECKPOINT_REPORTS/`
   - Filename: `checkpoint-day{N}-{YYYY-MM-DD}.md`
   - Example: `checkpoint-day3-2026-06-07.md`

Check the log file after each checkpoint run:
```bash
cat /tmp/seedwarden_checkpoint_day3.log
```

### 5b. Discord notification (optional)

If `DISCORD_WEBHOOK_URL` is set in `~/.claude_env`, the script posts a summary to the
Discord channel after each checkpoint. The notification includes:

- Checkpoint day and date
- Overall status (GO / CAUTION / NO-GO)
- Key metric values
- Recommended action (one sentence)
- Link to the full markdown report path

The Discord webhook format is a POST to:
```
POST {DISCORD_WEBHOOK_URL}
Content-Type: application/json
{"content": "..."}
```

To add Discord notification support to the script, add this function call at the end of
`CheckpointOrchestrator.run()` and ensure `requests` is installed:

```python
def _notify_discord(self, result: dict) -> None:
    webhook_url = self.env.get("DISCORD_WEBHOOK_URL", "")
    if not webhook_url or not HAS_REQUESTS:
        return
    decision = result["decision"]
    message = (
        f"**Track B Day {self.checkpoint_day} Checkpoint**\n"
        f"Status: **{decision['overall_status']}**\n"
        f"Action: {decision.get('recommended_action', '')[:200]}\n"
        f"Report: `{result.get('report_path', 'not written')}`"
    )
    try:
        requests.post(
            webhook_url,
            json={"content": message},
            timeout=10,
        )
    except Exception as exc:
        print(f"  [Discord] notification failed: {exc}", file=sys.stderr)
```

### 5c. Exit codes

The script returns deterministic exit codes — useful for chaining with other cron jobs
or monitoring systems:

| Exit code | Meaning |
|-----------|---------|
| 0 | GO — all thresholds met |
| 1 | CAUTION — some metrics below threshold but not critical |
| 2 | NO-GO — one or more critical metrics failed |
| 3 | Unknown error |

Check exit code after manual run:
```bash
uv run python TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py --day 3 --dry-run; echo "Exit: $?"
```

---

## 6. Manual Metric Override (Hybrid Mode)

Some metrics cannot be retrieved via API (Kit email open rates, Instagram reach, Twitter
mentions, Reddit upvotes, influencer response count). These can be passed as CLI flags to
supplement the automated API data.

### 6a. Hybrid run example

Run after manually checking the Kit dashboard, Instagram Insights, and email:

```bash
uv run python TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py \
  --day 3 \
  --env-file ~/.claude_env \
  --email-open-rate 22.5 \
  --kit-subscribers 14 \
  --influencer-responses 1 \
  --instagram-reach 340 \
  --twitter-mentions 0 \
  --reddit-upvotes 18
```

Manual overrides take precedence over any API-fetched values for the same metric.

### 6b. Full manual mode (no API calls)

For cases where API credentials are not yet configured:

```bash
uv run python TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py \
  --day 3 \
  --dry-run \
  --email-open-rate 18.0 \
  --gist-views 45 \
  --etsy-orders 0 \
  --kit-subscribers 8 \
  --influencer-responses 0
```

`--dry-run` mode skips live API calls. The manual overrides still apply to the decision
engine, producing a real GO/CAUTION/NO-GO result.

---

## 7. Pre-Launch Verification (Run Before Day 3)

Before the Day 3 cron fires, verify that the setup is working end-to-end:

### Step 1: Dry run test
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/seedwarden
uv run python TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py --day 3 --dry-run
```

Expected output: console summary with dummy metrics and a report file in
`CHECKPOINT_REPORTS/checkpoint-day3-{today}.md`.

### Step 2: Unit tests
```bash
uv run python TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py --test
```

Expected: all 21 unit tests pass.

### Step 3: Verify report file
```bash
ls -la /home/awank/dev/SuperClaude_Framework/projects/seedwarden/CHECKPOINT_REPORTS/
cat /home/awank/dev/SuperClaude_Framework/projects/seedwarden/CHECKPOINT_REPORTS/checkpoint-day3-*.md
```

### Step 4: Credential validation (when API keys are ready)
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/seedwarden
uv run python TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py \
  --day 3 \
  --env-file ~/.claude_env \
  --dry-run  # remove --dry-run to test live API calls
```

---

## 8. Idempotency Notes

The script is safe to run multiple times for the same checkpoint day. Running Day 3
twice produces the same report (second run overwrites first with the same filename).
API calls are read-only — no data is modified on Campaign Monitor, GitHub, Etsy, or Kit.

The only side effect is the markdown report file in `CHECKPOINT_REPORTS/` being
overwritten. If you need to preserve multiple runs for the same day, rename the report
file before re-running:
```bash
mv CHECKPOINT_REPORTS/checkpoint-day3-2026-06-07.md \
   CHECKPOINT_REPORTS/checkpoint-day3-2026-06-07-run1.md
```

---

## 9. Post-Checkpoint Actions

After each automated run, the user should:

1. Review the markdown report in `CHECKPOINT_REPORTS/`
2. Check the log file in `/tmp/seedwarden_checkpoint_day{N}.log` for any API errors
3. For any NO-GO scenario, open `CONTINGENCY_TRIGGER_DECISION_TREE.md` and execute
   the matching runbook (< 15 minutes per scenario)
4. Log the checkpoint decision in `WORKLOG.md` (status, metrics, action taken)
5. Update `GIST_BASELINE_VIEWS` in `~/.claude_env` if starting a new tracking window

---

*Document version: 1.0 — June 5, 2026 (Item 85)*
*Script: TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py*
*References: CONTINGENCY_TRIGGER_DECISION_TREE.md, TRACK_B_MONITORING_AUTOMATION_FRAMEWORK.md*
