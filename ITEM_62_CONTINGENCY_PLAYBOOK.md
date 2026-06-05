# Item 62 Contingency Playbook

**Purpose**: Automated contingency routing for June 5 pre-market checklist (13:00 UTC)

**Timeline**: 
- 13:00 UTC: Run `scripts/stockbot_june5_premarket_check.sh`
- 13:05 UTC: Run `scripts/execute_item_62_contingency.sh`
- 13:30 UTC: Market open (contingency path executes)

---

## Overview

Item 62 pre-market checklist evaluates 4 gates:
1. **Gate 1**: Container Health (docker ps)
2. **Gate 2**: Session Status (Docker logs for activity)
3. **Gate 3**: WebSocket Stability (connection errors)
4. **Gate 4**: Alpaca API Connectivity (credential validation)

Output: GO / CAUTION / NO-GO

**Routing**:
- **GO** → Normal trading with monitoring
- **CAUTION** → Trading with enhanced monitoring + decision gates
- **NO-GO** → Immediate escalation and rollback

---

## Path 1: GO Decision

### When This Applies
- All 4 gates PASS, OR
- 3 gates PASS + Gate 2 (Session Status) returns CAUTION

### Execution
```bash
# Pre-market verification (13:15 UTC)
# - Docker container running
# - Sessions sleeping until 13:15 UTC wake signal
# - Jetson SSH responsive
# - Discord webhook active

# Market open (13:30 UTC)
# - Sessions begin trading normally
# - Monitor for 2 hours (13:30-15:30 UTC)
```

### Monitoring Checklist
See `ITEM_62_GO_MONITORING_CHECKLIST.md` for hourly checks:
- Early watch (13:30-14:30 UTC): Confirm signals generating
- Mid-watch (14:30-15:30 UTC): Confirm no error spikes

### Escalation Triggers (pause if 2+ occur)
1. **WebSocket errors**: 2+ in any 15-minute window
2. **Alpaca API failures**: 401/403 authentication errors
3. **Zero signals**: Both sessions idle >30 min (confirm data feed)
4. **Fill rate anomaly**: >50% deviation from expected
5. **Large loss**: Single trade P&L loss >$500
6. **Drawdown spike**: >2% in single session

### If Escalation Triggered
1. Check Docker logs: `ssh awank@100.120.18.84 'docker logs stockbot --tail 100'`
2. Diagnose root cause (see below)
3. If fixable in <15 min: Fix and resume monitoring
4. If not: Post diagnosis to CHECKIN.md for user guidance

### Daily Close Analysis (20:00 UTC)
```bash
scripts/post_market_analysis_june5.sh
```

This script:
- Queries Alpaca fills for the day
- Analyzes database metrics
- Computes signal quality score
- Outputs GO/CAUTION/NO-GO for June 6

---

## Path 2: CAUTION Decision

### When This Applies
- 3 gates PASS (not counting Gate 2 CAUTION)
- OR 2 gates PASS + 1 CAUTION + 1 FAIL (but not Gate 1 or 4)

### Execution
```bash
# Same market open (13:30 UTC)
# BUT with enhanced monitoring mode:
# - Check interval: every 15 min (vs normal hourly)
# - Decision gates at 14:30 / 17:00 / 19:00 UTC
# - Escalation threshold: 1 anomaly (vs normal 2)
```

### Three Decision Gates

**Gate 1 @ 14:30 UTC (1 hour post-open)**
- Check: Alpaca API + WebSocket stability
- Pass criteria: No WebSocket errors, API responsive, first signals generated
- If FAIL: Move to NO-GO path

**Gate 2 @ 17:00 UTC (3.5 hours post-open)**
- Check: Fill rate + P&L trajectory
- Pass criteria: Fills >50% of expected, no session-specific failures, drawdown <2%
- If FAIL: Hold and prepare NO-GO

**Gate 3 @ 19:00 UTC (evening pre-close)**
- Check: Daily summary
- Pass criteria: ≥10 total fills, no cascading errors, normal P&L range
- If FAIL: Halt trading; execute NO-GO path

See `ITEM_62_CAUTION_MONITORING_CHECKLIST.md` for details.

### Anomaly Detection (every 15 min)

**WARN Threshold** (1 anomaly):
- WebSocket error
- Session lag >5 min
- Signal runaway (>5 BUY without SELL)
- Fill slip >2%
- DB sync lag >10 min

**Action**: Log and monitor; escalate if persists across 2 checks

**CRITICAL Threshold** (2+ anomalies or any FAIL):
- Immediate NO-GO path execution
- Discord alert to user

---

## Path 3: NO-GO Decision

### When This Applies
- Gate 1 (Container Health) FAILS, OR
- Gate 4 (Alpaca API) FAILS, OR
- 2 or fewer gates PASS

### Automatic Escalation

```bash
# Orchestrator automatically executes:
# 1. Discord alert to user
# 2. BLOCKED.md entry created (stockbot — Pre-Market Checklist Failed)
# 3. CHECKIN.md updated with "Needs Your Input" entry
# 4. Log written to ITEM_62_CONTINGENCY_EXECUTION_LOG.md
```

### User Action Required
1. Review `JUNE_5_PREMARKET_CHECK_RESULTS.md` for failing gate(s)
2. Diagnose root cause:
   - **Container not running**: SSH to Jetson, `docker restart stockbot`
   - **Sessions inactive**: Check active-sessions.json configuration
   - **WebSocket errors**: Restart container, check Alpaca subscription status
   - **Alpaca API fails**: Verify credentials in `/opt/stockbot/.env`
   - **SSH unreachable**: Check Tailscale connection, Jetson power status

3. Respond in CHECKIN.md with:
   - Root cause identified
   - Fix applied (if possible)
   - New target time for retry, OR
   - Decision to defer (if issue complex)

### No Automatic Market Entry
- Market opens 13:30 UTC
- Container NOT activated; sessions sleeping
- Trading halted until user approval + orchestrator reruns Item 62

---

## Diagnosis Guide

### Gate 1: Container Health FAILS

**Symptoms**: `docker ps` shows no stockbot container

**Quick fixes**:
```bash
# Check container status
ssh awank@100.120.18.84 'docker ps -a | grep stockbot'

# Restart if stopped
ssh awank@100.120.18.84 'docker restart stockbot'

# Check logs if restart fails
ssh awank@100.120.18.84 'docker logs stockbot --tail 50'
```

**Root causes**:
- Jetson power cycled (check uptime)
- Container exited (check logs for OOMKill, exit code)
- Docker daemon not responding (rare; restart Docker)

---

### Gate 2: Session Status CAUTION

**Symptoms**: `docker logs stockbot --since 1h | grep "Session.*001" | wc -l` returns <4

**Meaning**: Sessions not cycling normally (expected 2-4 cycles/hour)

**Quick fixes**:
- This is informational; CAUTION is acceptable
- If CRITICAL (0 cycles): Check if market is open, sessions sleeping, or actual error

---

### Gate 3: WebSocket Stability CAUTION/FAIL

**Symptoms**: `docker logs stockbot --since 30m | grep "connection limit exceeded\|WebSocket.*error"`

**Quick fixes**:
```bash
# Restart container to reset WebSocket connections
ssh awank@100.120.18.84 'docker restart stockbot'

# Check Alpaca subscription status
ssh awank@100.120.18.84 'curl -s -H "APCA-API-KEY-ID: KEY" https://paper-api.alpaca.markets/v2/account | jq .account_number'
```

**Root causes**:
- Alpaca subscription limit reached (upgrade required)
- Local network instability
- Container needs restart

---

### Gate 4: Alpaca API FAILS

**Symptoms**: API curl returns 401 Unauthorized or connection timeout

**Quick fixes**:
```bash
# Verify credentials are correct
ssh awank@100.120.18.84 'grep "^ALPACA_API_KEY" /opt/stockbot/.env'

# Test API with known-good request
ssh awank@100.120.18.84 <<EOF
ALPACA_KEY=\$(grep "^ALPACA_API_KEY_ID=" /opt/stockbot/.env | cut -d= -f2)
curl -s -H "APCA-API-KEY-ID: \$ALPACA_KEY" https://paper-api.alpaca.markets/v2/account
EOF

# If credentials wrong: Update .env and restart container
```

**Root causes**:
- API credentials expired or incorrect
- Alpaca account suspended
- Network connectivity issue (check `ping paper-api.alpaca.markets`)

---

## Escalation Chain

If no quick fix available:

1. **15:00 UTC**: Post to CHECKIN.md with diagnosis
2. **16:00 UTC**: User responds with guidance or defer decision
3. **Next session**: Retry Item 62 at new target time

---

## Files Created by Contingency Paths

**GO Path**:
- `ITEM_62_GO_MONITORING_CHECKLIST.md` — Hourly monitoring tasks
- `JUNE_5_POSTMARKET_ANALYSIS.md` — Daily close analysis (created at 20:00 UTC)

**CAUTION Path**:
- `ITEM_62_CAUTION_MONITORING_CHECKLIST.md` — 15-min monitoring + 3 decision gates

**NO-GO Path**:
- Entry added to `BLOCKED.md`
- Entry added to `CHECKIN.md` under "Needs Your Input"
- `ITEM_62_CONTINGENCY_EXECUTION_LOG.md` — Execution log

All paths:
- `ITEM_62_CONTINGENCY_EXECUTION_LOG.md` — Updated with path decision and timestamp

---

## Example Timeline (GO Path)

```
13:00 UTC — Run Item 62 pre-market checklist
  ↓
13:05 UTC — Parse results, route to GO path
  ↓
13:15 UTC — Pre-market verification (container, sessions, SSH, webhook)
  ↓
13:30 UTC — Market open, sessions begin trading
  ↓
13:30-14:30 UTC — Early watch (signals generating?)
  ↓
14:30-15:30 UTC — Mid watch (error spikes?)
  ↓
15:30-20:00 UTC — Normal monitoring (hourly checks)
  ↓
20:00 UTC — Run post-market analysis
  ↓
20:15 UTC — Publish analysis results, determine June 6 decision
```

---

## Execution

**To execute immediately after Item 62 pre-market script completes**:

```bash
cd /home/awank/dev/SuperClaude_Framework

# Run Item 62 pre-market checklist (13:00 UTC)
bash scripts/stockbot_june5_premarket_check.sh

# Run contingency router immediately after (13:05 UTC)
bash scripts/execute_item_62_contingency.sh

# For GO path: run post-market analysis at 20:00 UTC
bash scripts/post_market_analysis_june5.sh
```

**For CAUTION path**: Manually execute decision gates at 14:30, 17:00, 19:00 UTC per checklist

**For NO-GO path**: Automatic escalation (no additional user action until CHECKIN.md response)
