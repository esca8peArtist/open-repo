# Domain 58 Trump v. Barbara SCOTUS Monitor Deployment

**Status**: Production-ready (June 1, 2026)  
**Scope**: Autonomous monitoring for Trump v. Barbara (No. 25-365) Supreme Court ruling  
**Timeline**: Active June 1 – July 31, 2026 (court term)  
**Business value**: Enables instant Domain 58 distribution upon ruling issuance (currently manual)

---

## Overview

Automates detection of the Trump v. Barbara ruling across three independent sources:
1. **SCOTUS.gov** — official Supreme Court opinions API
2. **SCOTUSBlog** — real-time legal commentary
3. **NARF Tribal Supreme Court Project** — specialized tribal law tracking

Upon ruling detection:
- Sends Discord alert with ruling links and next-step checklist
- Activates Domain 58 rapid-response workflow  
- Records ruling date and outcome sources for decision routing
- Integrates with existing `phase-1-adoption-tracking-script.py` infrastructure

---

## Installation

### 1. Verify Dependencies

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/resistance-research
python3 -c "import requests; print('OK')" || pip install requests
```

### 2. Set Environment Variables

```bash
# Add to ~/.bashrc or ~/.zshrc (for persistence across sessions)
export DISCORD_WEBHOOK_URL="YOUR_DISCORD_WEBHOOK_URL"
export GITHUB_TOKEN="your_github_token"  # Optional, for announcement Gist updates

# Reload shell
source ~/.bashrc
```

**Where to get DISCORD_WEBHOOK_URL**:
- Create a Discord server channel for SCOTUS monitoring
- Server Settings → Webhooks → New Webhook
- Copy the webhook URL
- Paste as `DISCORD_WEBHOOK_URL` above

### 3. Verify Script Permissions

```bash
chmod +x /home/awank/dev/SuperClaude_Framework/projects/resistance-research/scripts/domain-58-scotus-monitor.py
```

### 4. Create Logs Directory

```bash
mkdir -p /home/awank/dev/SuperClaude_Framework/projects/resistance-research/scripts/logs
```

---

## Testing

### Quick Test (Run Immediately)

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/resistance-research
python3 scripts/domain-58-scotus-monitor.py --run-now
```

**Expected output**:
```
2026-06-01 14:35:22 [INFO] === Domain 58 SCOTUS Monitor started (Trump v. Barbara) ===
2026-06-01 14:35:23 [INFO] Checking for Trump v. Barbara ruling (Case No. 25-365)
2026-06-01 14:35:24 [INFO] ⏳ No ruling detected yet. Last check: 2026-06-01T14:35:22...
2026-06-01 14:35:24 [INFO] === Domain 58 Ruling Detection Complete ===
```

**If ruling were detected** (when issued):
```
2026-06-01 14:35:23 [INFO] ✅ RULING DETECTED! Confirmed on 3 source(s)
2026-06-01 14:35:24 [INFO] ✅ Discord alert sent successfully
2026-06-01 14:35:24 [INFO] Activating Domain 58 rapid-response workflow...
2026-06-01 14:35:24 [INFO] ✅ Rapid-response activated. State file: ...
```

### Verify Discord Webhook Works

```bash
curl -X POST "$DISCORD_WEBHOOK_URL" \
  -H 'Content-Type: application/json' \
  -d '{"content":"🧪 Test message from domain-58-scotus-monitor.py"}'
```

Should see message appear in Discord channel within 1 second.

---

## Deployment to Production

### Option A: Hourly Monitoring via Cron (Recommended)

Add to crontab for hourly checks during court term (June-July):

```bash
crontab -e

# Add this line:
0 * * 6-7 /usr/bin/python3 /home/awank/dev/SuperClaude_Framework/projects/resistance-research/scripts/domain-58-scotus-monitor.py --run-now

# Save and exit
```

**Explanation**:
- `0 *` = at the top of every hour
- `* * 6-7` = June (month 6) and July (month 7) only
- Runs at 00:00, 01:00, 02:00, ..., 23:00 UTC every day

**Verify cron is active**:
```bash
crontab -l | grep domain-58-scotus-monitor
```

### Option B: Systemd Timer (If Cron Not Available)

Create `/etc/systemd/system/domain-58-scotus-monitor.timer`:

```ini
[Unit]
Description=Domain 58 SCOTUS Monitor (Trump v. Barbara)
After=network-online.target
Wants=network-online.target

[Timer]
OnBootSec=5min
OnUnitActiveSec=1h
AccuracySec=1s

[Install]
WantedBy=timers.target
```

Create `/etc/systemd/system/domain-58-scotus-monitor.service`:

```ini
[Unit]
Description=Domain 58 SCOTUS Ruling Detection
After=network.target

[Service]
Type=oneshot
User=awank
WorkingDirectory=/home/awank/dev/SuperClaude_Framework/projects/resistance-research
ExecStart=/usr/bin/python3 scripts/domain-58-scotus-monitor.py --run-now
StandardOutput=journal
StandardError=journal
Environment="DISCORD_WEBHOOK_URL=YOUR_WEBHOOK_URL"
Environment="GITHUB_TOKEN=your_token"

[Install]
WantedBy=multi-user.target
```

Enable:
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now domain-58-scotus-monitor.timer
sudo systemctl status domain-58-scotus-monitor.timer
```

---

## Operational Procedures

### Daily Health Check

```bash
# Check last 10 monitoring runs
tail -20 /home/awank/dev/SuperClaude_Framework/projects/resistance-research/scripts/logs/scotus-monitor.log

# View current state
cat /home/awank/dev/SuperClaude_Framework/projects/resistance-research/scripts/domain-58-scotus-state.json
```

### When Ruling is Detected

**Monitor will automatically**:
1. ✅ Send Discord alert (3 sources + next steps)
2. ✅ Create `domain-58-rapid-response-ACTIVATED.json` state file
3. ✅ Log ruling date and sources to `scotus-monitor.log`

**You must then**:
1. Check Discord notification (includes Docket URL and source links)
2. Open `domain-58-rapid-response-checklist.md` in `/home/awank/dev/SuperClaude_Framework/projects/resistance-research/exploration/`
3. Follow Steps 0-1 to verify ruling (read majority opinion summary)
4. Answer Q1-Q2 to determine outcome branch (A/B/B-Hybrid/C)
5. Execute corresponding edits in `domains/domain-58-tribal-sovereignty.md`
6. Activate distribution via `domain-58-execution-checklist.md`

**Timeline**: 15 minutes (verify ruling) + 30 minutes (edit domain document) + 45 minutes (send distribution) = 90 minutes total to deployment

---

## Monitoring State File

Monitor maintains state in `scripts/domain-58-scotus-state.json`:

```json
{
  "last_check": "2026-06-01T14:35:22.123456",
  "ruling_found": false,
  "ruling_date": null,
  "ruling_url": null,
  "alerts_sent": 0
}
```

**Once ruling is detected**:
```json
{
  "last_check": "2026-07-15T09:32:44.654321",
  "ruling_found": true,
  "ruling_date": "2026-07-15T09:00:00.000000",
  "ruling_sources": ["SCOTUS.gov", "SCOTUSBlog", "NARF Tracker"],
  "alerts_sent": 1
}
```

Monitor will skip subsequent checks once `ruling_found: true` (no duplicate alerts).

---

## Integration with Phase 1 Adoption Tracking

**Current**: `phase-1-adoption-tracking-script.py` monitors:
- GitHub Gist views (Domain 39-40 engagement)
- Gmail replies (adoption tracking)
- Google Sheets updates (contact log)

**Extension**: Trump v. Barbara monitor adds:
- SCOTUS opinion polling (ruling detection)
- Discord alerts (breaking news)
- Domain 58 workflow activation

**Workflow**:
1. Domain 39-40 distribution starts June 1 (user send)
2. Phase 1 adoption tracking starts June 3 (measurement)
3. Trump v. Barbara monitor runs continuously (June-July, hourly)
4. If ruling issues before Phase 1 Day 30 checkpoint (June 30):
   - Monitor alerts immediately
   - Domain 58 rapid-response activates
   - User executes Domain 58 distribution in parallel with Phase 1 measurement
5. Phase 2 sequencing decision (June 30, Day 30 checkpoint):
   - Domain 39 engagement metrics determine Phase 2 timeline
   - Domain 58 ruling (if issued) determines immediate activation path

---

## Troubleshooting

### Monitor Not Running

Check cron is active:
```bash
crontab -l
ps aux | grep domain-58-scotus-monitor
```

Check environment variables:
```bash
echo $DISCORD_WEBHOOK_URL
```

If missing, export in crontab environment:
```bash
crontab -e

# Add at the top:
DISCORD_WEBHOOK_URL=YOUR_WEBHOOK_URL
GITHUB_TOKEN=your_token

# Then add the job
0 * * 6-7 /usr/bin/python3 /path/to/domain-58-scotus-monitor.py --run-now
```

### Discord Alerts Not Sending

Test webhook manually:
```bash
curl -X POST "$DISCORD_WEBHOOK_URL" \
  -H 'Content-Type: application/json' \
  -d '{"content":"Test"}'
```

If 401/403 error:
- Webhook may have expired → regenerate in Discord server settings
- Check DISCORD_WEBHOOK_URL is copied completely (no extra spaces)

### Monitor Says "No Ruling" When Ruling Issued

Possible causes:
1. SCOTUS.gov website changed format → grep patterns may need updating
2. SCOTUSBlog site blocked → check requests library working (`python3 -c "import requests; print(requests.get('https://www.scotusblog.com').status_code)"`)
3. NARF tracker unreachable → check network

Manual verification:
```bash
# Visit these manually to verify ruling was issued:
open https://www.supremecourt.gov/opinions/slipopinion/
open https://www.scotusblog.com/case-files/cases/trump-v-barbara/
open https://sct.narf.org/
```

---

## Performance & Resource Usage

**CPU**: <1% per check (lightweight HTTP requests)  
**Memory**: ~20-30 MB Python process (requests library)  
**Network**: 3 HTTP requests × ~50KB = ~150KB per hourly check  
**Storage**: State file <1 KB, logs ~100 KB/week during active monitoring

**Cost**: Negligible. Requests library uses minimal resources. Discord webhook free-tier unlimited.

---

## Runbook: When Ruling Issues

**T+0 minutes**: Monitor detects ruling → sends Discord alert  
**T+5 minutes**: You receive Discord notification in Slack/Teams integration  
**T+15 minutes**: Execute `domain-58-rapid-response-checklist.md` Steps 0-1  
**T+45 minutes**: Finish domain edits per rapid-response checklist  
**T+90 minutes**: Domain 58 distribution active (parallel with Phase 1 measurement)

**Discord alert includes**:
- ✅ Links to ruling (SCOTUS.gov, SCOTUSBlog, NARF)
- ✅ Direct link to `domain-58-rapid-response-checklist.md`
- ✅ Docket URL for SCOTUS case page
- ✅ Next-step instructions

---

## Success Criteria

✅ **Installed**: Cron job active, environment variables set  
✅ **Tested**: Manual `--run-now` runs without errors  
✅ **Discord verified**: Test message appears in Discord  
✅ **Monitoring active**: Hourly checks logged (watch `scotus-monitor.log`)  
✅ **Ruling detected**: When issued (June-July), alert appears <1 min after ruling drops  
✅ **Domain 58 ready**: Rapid-response checklist and distribution templates documented

---

## Deactivation (After Court Term Ends)

Once ruling is issued and Domain 58 distributed:

```bash
# Remove from cron
crontab -e
# Delete the line with domain-58-scotus-monitor
```

Or:

```bash
# If using systemd
sudo systemctl disable domain-58-scotus-monitor.timer
```

Monitor state file is preserved for reference. Domain 58 rapid-response workflow is now complete.

---

## Appendix: Source URLs

**SCOTUS Official**: https://www.supremecourt.gov/opinions/slipopinion/  
**Trump v. Barbara Docket**: https://www.supremecourt.gov/docket/25-365  
**SCOTUSBlog Case Page**: https://www.scotusblog.com/case-files/cases/trump-v-barbara/  
**NARF Tribal Supreme Court Project**: https://sct.narf.org/  

All sources polled hourly (June-July 2026 during Supreme Court term).
