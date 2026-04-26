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
USAGE_JSON=$(python3 "$WORKSPACE/scripts/usage-check.py" --json 2>/dev/null || echo '{}')
# Human-readable summary
echo "$USAGE_JSON" | python3 -c "
import json,sys
d = json.load(sys.stdin)
p = d.get('pct', {})
u = d.get('usage', {})
h = d.get('hours_until_reset', '?')
print(f'  Sonnet: {p.get(\"sonnet\",\"?\"):.1f}% ({u.get(\"sonnet_output\",0):,} tokens)')
print(f'  All-models: {p.get(\"all_models\",\"?\"):.1f}%')
print(f'  Reset in {h:.0f}h')
" 2>/dev/null || echo "  (usage-check unavailable)" | tee -a "$LOG_FILE"
# Checkin line
USAGE_LINE=$(echo "$USAGE_JSON" | python3 -c "
import json,sys
d = json.load(sys.stdin)
p = d.get('pct', {})
u = d.get('usage', {})
h = d.get('hours_until_reset', 0)
flag = '🔴' if max(p.get('sonnet',0), p.get('all_models',0)) >= 90 else '🟡' if max(p.get('sonnet',0), p.get('all_models',0)) >= 75 else '🟢'
print(f\"{flag} Usage: Sonnet {p.get('sonnet',0):.1f}% ({u.get('sonnet_output',0):,} tokens) | All-models {p.get('all_models',0):.1f}% | Reset in {h:.0f}h\")
" 2>/dev/null || echo "usage-check unavailable")

# ── 4. Add calibration reminder to BLOCKED.md ────────────────────────────────
TODAY=$(date +%Y-%m-%d)
python3 - <<PYEOF
from pathlib import Path
import re, sys, os

blocked = Path("$WORKSPACE/BLOCKED.md")
text = blocked.read_text()
today = "$TODAY"

reminder = f"""
<!-- AUTO:CALIBRATION:START -->
### Usage limits — weekly calibration reminder
**Date blocked**: {today} (auto-added each Tuesday by reset-usage-budget.sh)
**Context**: Plan limits reset today. Token limits in usage-check.py are calibrated estimates that drift over time. Verify against actual UI percentages.
**What I need**: Check claude.ai → Settings → Usage & billing. Run: \`bash scripts/verify-calibration.sh <sonnet_pct> <all_pct>\`
**Verify with**: \`bash scripts/verify-calibration.sh\`
**Resolution**:
<!-- AUTO:CALIBRATION:END -->
"""

# Remove any previous weekly calibration reminder (replace, don't stack)
text = re.sub(
    r'\n?<!-- AUTO:CALIBRATION:START -->.*?<!-- AUTO:CALIBRATION:END -->',
    '',
    text,
    flags=re.DOTALL
)

# Insert at top of Active Blocks, before any existing ### entries
insert_point = text.find("## Active Blocks\n") + len("## Active Blocks\n")
if "## Active Blocks\n" in text:
    text = text[:insert_point] + reminder + "\n" + text[insert_point:]
else:
    text += reminder

tmp = blocked.with_suffix(".tmp")
tmp.write_text(text)
os.replace(tmp, blocked)
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
  python3 - "$DISCORD_WEBHOOK_URL" "$USAGE_LINE" <<'PYEOF'
import sys, json, subprocess
webhook, usage_line = sys.argv[1], sys.argv[2]
msg = (f"✅ **[Claude] Weekly plan reset complete**\n"
       f"Pause gate cleared. Usage monitor re-armed (alerts from 10%).\n"
       f"{usage_line}\n"
       f"Calibration reminder added to BLOCKED.md — check claude.ai → Settings → Usage & billing.")
payload = json.dumps({"content": msg})
result = subprocess.run(
    ["curl", "-s", "-w", "\n%{http_code}", "-H", "Content-Type: application/json",
     "-d", payload, webhook],
    capture_output=True, text=True, timeout=15
)
http_code = result.stdout.strip().split("\n")[-1]
if not http_code.startswith("2"):
    print(f"Discord notification failed: HTTP {http_code}", file=sys.stderr)
PYEOF
  echo "[$(date)] Discord notification sent." | tee -a "$LOG_FILE"
fi

echo "[$(date)] reset-usage-budget.sh: done." | tee -a "$LOG_FILE"
