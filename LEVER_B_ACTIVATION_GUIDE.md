# Lever B HMM Activation Guide — May 22 Checkpoint Critical Fix

**Created**: 2026-05-19
**Target**: Jetson (100.120.18.84)
**Deadline**: May 22 13:30 UTC market open
**Estimated time**: 5 minutes

---

## The Problem

The Lever B HMM regime masking code is **deployed and ready** on Jetson (`/opt/stockbot/src/ml/hmm_signal_masker.py`), but the configuration file `/opt/stockbot/config/active-sessions-2session.json` is missing the critical `strategy_params` block that activates it.

**Without this activation**, the May 22 checkpoint will measure Lever A behavior (same configuration as May 19 that failed with STILL_MISS_B2 outcome).

---

## Quick Fix (5 minutes)

### Option 1: Automated Fix Script (Recommended)

Copy and paste this into an SSH session on Jetson:

```bash
#!/bin/bash
set -e

CONFIG_FILE="/opt/stockbot/config/active-sessions-2session.json"
BACKUP_FILE="/opt/stockbot/config/active-sessions-2session.json.backup.$(date +%s)"

echo "[$(date)] Starting Lever B activation..."
echo "[$(date)] Backing up config to $BACKUP_FILE"
cp "$CONFIG_FILE" "$BACKUP_FILE"

echo "[$(date)] Adding strategy_params to both AAPL sessions..."

# Python script to inject strategy_params into both sessions
python3 << 'PYTHON_EOF'
import json
from pathlib import Path

CONFIG_FILE = Path("/opt/stockbot/config/active-sessions-2session.json")

# Read current config
with open(CONFIG_FILE) as f:
    config = json.load(f)

# Add strategy_params to each session if not present
for session in config.get("sessions", []):
    if "strategy_params" not in session:
        session["strategy_params"] = {}
    
    # Ensure these flags are set
    session["strategy_params"]["hmm_regime_masking"] = True
    session["strategy_params"]["hmm_observe_mode"] = True
    session["strategy_params"]["hmm_min_fit_bars"] = 60
    session["strategy_params"]["hmm_suppress_buy_in_bear"] = True

# Write back with pretty formatting
with open(CONFIG_FILE, "w") as f:
    json.dump(config, f, indent=2)

print("[✓] Config updated with strategy_params")
PYTHON_EOF

echo "[$(date)] Verifying config syntax..."
python3 -m json.tool "$CONFIG_FILE" > /dev/null && echo "[✓] JSON valid"

echo "[$(date)] Restarting Docker container..."
docker restart stockbot

echo "[$(date)] Waiting 5 seconds for container startup..."
sleep 5

echo "[$(date)] Verifying health endpoint..."
max_retries=10
attempt=0
while [ $attempt -lt $max_retries ]; do
    if curl -s http://localhost:8000/api/health | grep -q '"status"'; then
        echo "[✓] Health check passed"
        curl -s http://localhost:8000/api/health | python3 -m json.tool
        echo "[$(date)] Lever B activation COMPLETE ✓"
        exit 0
    fi
    attempt=$((attempt + 1))
    echo "[$(date)] Retry $attempt/$max_retries..."
    sleep 1
done

echo "[✗] Health check failed after $max_retries retries"
exit 1
```

Save this as a shell script and run it:
```bash
chmod +x /tmp/activate_lever_b.sh
/tmp/activate_lever_b.sh
```

### Option 2: Manual Step-by-Step (if automation fails)

#### Step 1: Connect via SSH
```bash
ssh ubuntu@100.120.18.84
# Enter your password or SSH key
```

#### Step 2: Backup config
```bash
cp /opt/stockbot/config/active-sessions-2session.json \
   /opt/stockbot/config/active-sessions-2session.json.backup.$(date +%s)
```

#### Step 3: Edit config
```bash
nano /opt/stockbot/config/active-sessions-2session.json
```

Press Ctrl+V and paste the corrected JSON below (see "Exact Config Changes" section)

Or use sed to add the fields programmatically:

```bash
python3 << 'EOF'
import json

with open("/opt/stockbot/config/active-sessions-2session.json") as f:
    config = json.load(f)

for session in config["sessions"]:
    session["strategy_params"] = {
        "hmm_regime_masking": True,
        "hmm_observe_mode": True,
        "hmm_min_fit_bars": 60,
        "hmm_suppress_buy_in_bear": True
    }

with open("/opt/stockbot/config/active-sessions-2session.json", "w") as f:
    json.dump(config, f, indent=2)

print("✓ Config updated")
EOF
```

#### Step 4: Verify JSON syntax
```bash
python3 -m json.tool /opt/stockbot/config/active-sessions-2session.json > /dev/null && echo "✓ Valid"
```

#### Step 5: Restart container
```bash
docker restart stockbot
```

#### Step 6: Wait 5 seconds
```bash
sleep 5
```

#### Step 7: Verify health
```bash
curl http://localhost:8000/api/health
```

Expected output: `{"status":"ok","sessions":2}`

---

## Exact Config Changes

### Current Config (Missing strategy_params)

See `/home/awank/dev/SuperClaude_Framework/projects/stockbot/active-sessions-2session.json`

### Fixed Config (With strategy_params)

See `/home/awank/dev/SuperClaude_Framework/active-sessions-2session-LEVER-B-READY.json`

### What Changed

For EACH session, added this block:

```json
"strategy_params": {
  "hmm_regime_masking": true,
  "hmm_observe_mode": true,
  "hmm_min_fit_bars": 60,
  "hmm_suppress_buy_in_bear": true
}
```

**Key flags**:
- `hmm_regime_masking: true` — ACTIVATES Lever B
- `hmm_observe_mode: true` — Log-only mode (watch behavior before enforcement)
- `hmm_min_fit_bars: 60` — Warm-up bars before regime detection activates
- `hmm_suppress_buy_in_bear: true` — Don't open new positions in Bear regime

---

## Validation

### Quick Health Check
```bash
ssh ubuntu@100.120.18.84 'curl -s http://localhost:8000/api/health'
```

Expected: `{"status":"ok","sessions":2}`

### Full Status Check
```bash
ssh ubuntu@100.120.18.84 'docker logs stockbot 2>&1 | tail -20 | grep -E "(regime|HMM|Lever)"'
```

Expected: Recent logs should show HMM initialization and regime detection activity.

### Config Verification
```bash
ssh ubuntu@100.120.18.84 'python3 -c "import json; c=json.load(open(\"/opt/stockbot/config/active-sessions-2session.json\")); s=c[\"sessions\"][0]; print(\"hmm_regime_masking:\", s.get(\"strategy_params\", {}).get(\"hmm_regime_masking\"))"'
```

Expected: `hmm_regime_masking: True`

---

## Fallback: If SSH Access is Still Unavailable

If the orchestrator's SSH key still isn't authorized, you have two options:

**Option A**: Add orchestrator's public key to Jetson authorized_keys:

```bash
# On your machine with Jetson access
cat ~/.ssh/orchestrator_pub_key.txt >> ~/.ssh/authorized_keys
```

**Option B**: Use your own SSH credentials (not orchestrator):

```bash
ssh your_username@100.120.18.84
# Then run the automated fix script above
```

Once you have SSH access, the fix takes 5 minutes.

---

## Post-Activation Timeline

| Time | Action |
|------|--------|
| **May 22 13:30 UTC** | Market open; sessions begin trading with Lever B active (observe mode) |
| **May 22 20:00 UTC** | Checkpoint execution; queries Alpaca for AAPL SELL fills |
| **May 22-23** | Monitor logs for `[HMMSignalMasker]` regime detection activity |
| **May 26** | Effectiveness assessment checkpoint (first real P&L impact measurable) |

---

## May 22 Checkpoint Execution

Once activation is complete, the May 22 checkpoint will execute automatically at 20:00 UTC:

```bash
cd /home/awank/dev/SuperClaude_Framework
uv run python projects/stockbot/scripts/may22_checkpoint_query_alpaca.py
```

Exit codes:
- `0` — PASS (at least 1 AAPL SELL filled)
- `1` — STILL_MISS_B2 (zero AAPL sells; Lever B insufficient)
- `2` — FAR_MISS (infrastructure failure)
- `3` — ERROR (API or script error)

---

## Troubleshooting

### Docker Container Won't Start After Config Change

**Problem**: `docker restart stockbot` hangs or fails

**Solution**:
```bash
docker logs stockbot  # Check logs for errors
docker stop stockbot
docker start stockbot  # Try starting (don't restart)
```

### Health Check Fails

**Problem**: `curl http://localhost:8000/api/health` returns 502 or hangs

**Solution**:
```bash
docker logs stockbot 2>&1 | tail -50  # Check for startup errors
# If timeout occurs, wait another 10 seconds and retry
sleep 10
curl http://localhost:8000/api/health
```

### Config Syntax Error

**Problem**: JSON parse errors when editing

**Solution**:
```bash
# Restore from backup
cp /opt/stockbot/config/active-sessions-2session.json.backup.* \
   /opt/stockbot/config/active-sessions-2session.json

# Verify backup is valid
python3 -m json.tool /opt/stockbot/config/active-sessions-2session.json

# Try automated Python injection again (safer than manual editing)
python3 << 'EOF'
import json
with open("/opt/stockbot/config/active-sessions-2session.json") as f:
    config = json.load(f)
for session in config["sessions"]:
    session["strategy_params"] = {
        "hmm_regime_masking": True,
        "hmm_observe_mode": True,
        "hmm_min_fit_bars": 60,
        "hmm_suppress_buy_in_bear": True
    }
with open("/opt/stockbot/config/active-sessions-2session.json", "w") as f:
    json.dump(config, f, indent=2)
print("✓ Config fixed")
EOF
```

---

## Files Changed on Jetson

- `/opt/stockbot/config/active-sessions-2session.json` — Modified (backup created first)
- `/opt/stockbot/config/active-sessions-2session.json.backup.<timestamp>` — Backup of original

---

## Contact & Status

Once SSH access is provided, this fix takes 5 minutes to execute. The user or orchestrator can then run the May 22 checkpoint query to verify Lever B is operational.

**Pre-requisite**: SSH access to `ubuntu@100.120.18.84` (either via orchestrator key authorization or user credentials)

---

**Last Updated**: 2026-05-19
**Session**: 1341 (Autonomous Orchestrator)
