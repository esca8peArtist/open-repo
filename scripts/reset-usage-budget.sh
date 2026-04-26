#!/bin/bash
# reset-usage-budget.sh
# Runs every Tuesday at 08:00 UTC (09:00 BST) after the plan resets.
# Crontab: 0 8 * * 2
#
# What it does:
#   1. Clears the 80% pause gate and override file (new week = fresh start)
#   2. Clears the usage-monitor threshold state (so alerts fire again from 10%)
#   3. Runs usage-check.py to confirm the new week shows ~0% (verifies reset happened)
#   4. Adds a calibration reminder to BLOCKED.md (prompts user to re-verify limits)
#   5. Commits BLOCKED.md and sends Discord summary

set -e

WORKSPACE="$HOME/dev/SuperClaude_Framework"
LOG_FILE="$WORKSPACE/orchestrator.log"
[ -f "$HOME/.claude_env" ] && source "$HOME/.claude_env"

cd "$WORKSPACE"
git checkout master >> "$LOG_FILE" 2>&1 || true

echo "[$(date)] reset-usage-budget.sh: Tuesday plan reset triggered." | tee -a "$LOG_FILE"

# ── 1. Clear pause and override files ────────────────────────────────────────
rm -f "$WORKSPACE/USAGE_PAUSE" "$WORKSPACE/USAGE_PAUSE_OVERRIDE"
echo "[$(date)] Cleared USAGE_PAUSE and USAGE_PAUSE_OVERRIDE." | tee -a "$LOG_FILE"

# ── 2. Clear usage-monitor threshold state ────────────────────────────────────
rm -f "$WORKSPACE/.usage-monitor-state.json"
echo "[$(date)] Cleared usage-monitor state (thresholds will re-arm)." | tee -a "$LOG_FILE"

# ── 3. Verify reset ───────────────────────────────────────────────────────────
echo "[$(date)] Usage at reset time (should be ~0%):" | tee -a "$LOG_FILE"
python3 "$WORKSPACE/scripts/usage-check.py" | tee -a "$LOG_FILE" || true
USAGE_LINE=$(python3 "$WORKSPACE/scripts/usage-check.py" --checkin 2>/dev/null \
             || echo "usage-check unavailable")

# ── 4. Add calibration reminder to BLOCKED.md ────────────────────────────────
TODAY=$(date +%Y-%m-%d)
python3 - <<PYEOF
from pathlib import Path
import re, sys

blocked = Path("$WORKSPACE/BLOCKED.md")
text = blocked.read_text()
today = "$TODAY"
workspace = "$WORKSPACE"

reminder = f"""
### Usage limits — weekly calibration reminder
**Date added**: {today} (auto-added by reset-usage-budget.sh each Tuesday)
**Context**: Plan limits reset today. Token limits in usage-check.py are calibrated estimates — they drift over time as plan allocation changes. Verify against the actual UI percentages.
**What I need**: Check claude.ai → Settings → Usage & billing. Note the current Sonnet % and All-models %. Run: \`python3 scripts/usage-check.py --calibrate <sonnet_pct> <all_pct>\`
**Verify with**: \`python3 scripts/usage-check.py --json | python3 -c "import json,sys; d=json.load(sys.stdin); print('limits look calibrated' if d['pct']['sonnet'] < 3 else 'CALIBRATE: usage not near 0% after reset')"\`
**Resolution**:
"""

# Remove any previous weekly calibration reminder (replace, don't stack)
text = re.sub(
    r'\n### Usage limits — weekly calibration reminder.*?(?=\n### |\n## Resolved|\Z)',
    '',
    text,
    flags=re.DOTALL
)

# Insert at top of Active Blocks section
if "## Active Blocks" in text:
    text = text.replace("## Active Blocks\n", f"## Active Blocks\n{reminder}")
else:
    text += reminder

blocked.write_text(text)
print("Calibration reminder added to BLOCKED.md.")
PYEOF

# ── 5. Commit and notify ──────────────────────────────────────────────────────
git add BLOCKED.md
git commit -m "chore(orchestrator): Tuesday reset — clear usage pause + add calibration reminder

Weekly automated reset:
- USAGE_PAUSE and USAGE_PAUSE_OVERRIDE cleared
- usage-monitor state reset (10% alerts re-arm)
- Calibration reminder added to BLOCKED.md

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>" \
  >> "$LOG_FILE" 2>&1 || echo "[$(date)] Nothing to commit." | tee -a "$LOG_FILE"

if [ -n "$DISCORD_WEBHOOK_URL" ]; then
  MSG="✅ **[Claude] Weekly plan reset complete**\nPause gate cleared. Usage monitor re-armed (alerts from 10%).\n$USAGE_LINE\nCalibration reminder added to BLOCKED.md — check claude.ai → Settings → Usage & billing."
  curl -s -H "Content-Type: application/json" \
    -d "{\"content\":\"$(echo "$MSG" | sed 's/"/\\"/g')\"}" \
    "$DISCORD_WEBHOOK_URL" > /dev/null 2>&1 || true
  echo "[$(date)] Discord notification sent." | tee -a "$LOG_FILE"
fi

echo "[$(date)] reset-usage-budget.sh: done." | tee -a "$LOG_FILE"
