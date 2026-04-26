#!/bin/bash
# reset-usage-budget.sh
# Runs after each Tuesday plan reset to lower the session budget caps
# back to sustainable levels and recalibrate token limits from the usage-check report.
# Scheduled via crontab: 0 8 * * 2 (Tuesdays at 08:00 UTC = 09:00 BST)

set -e

WORKSPACE="$HOME/dev/SuperClaude_Framework"
LOG_FILE="$WORKSPACE/orchestrator.log"
[ -f "$HOME/.claude_env" ] && source "$HOME/.claude_env"

cd "$WORKSPACE"
git checkout master

echo "[$(date)] reset-usage-budget.sh: weekly reset triggered." | tee -a "$LOG_FILE"

# ── Lower session budget caps ─────────────────────────────────────────────────
python3 - <<'PYEOF'
import re
from pathlib import Path

projects = Path("PROJECTS.md")
text = projects.read_text()

text = re.sub(
    r'(- \*\*Weekly session budget:) \d+\*\*.*',
    r'\1 40**  ← reset to sustainable level after weekly plan reset',
    text
)
text = re.sub(
    r'(- \*\*Daily session budget:) \d+\*\*.*',
    r'\1 10**  ← reset to sustainable level after weekly plan reset',
    text
)
projects.write_text(text)
print("Budget caps reset: weekly=40, daily=10")
PYEOF

# ── Show token usage summary ──────────────────────────────────────────────────
echo "[$(date)] Token usage at reset time:" | tee -a "$LOG_FILE"
python3 "$WORKSPACE/scripts/usage-check.py" | tee -a "$LOG_FILE" || true

# ── Commit the change ─────────────────────────────────────────────────────────
git add PROJECTS.md
git commit -m "chore(orchestrator): weekly reset — lower session budgets to 40/10

Automated post-reset: weekly=200→40, daily=50→10.
Run reset-usage-budget.sh every Tuesday after plan resets.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>" || echo "Nothing to commit."

# ── Discord notification ──────────────────────────────────────────────────────
if [ -n "$DISCORD_WEBHOOK_URL" ]; then
  USAGE_LINE=$(python3 "$WORKSPACE/scripts/usage-check.py" --checkin 2>/dev/null || echo "usage-check unavailable")
  MSG="**[Claude] Weekly plan reset — budgets restored**\nSession caps: weekly=40, daily=10 (were 200/50).\n$USAGE_LINE"
  curl -s -H "Content-Type: application/json" \
    -d "{\"content\":\"$(echo "$MSG" | sed 's/"/\\"/g')\"}" \
    "$DISCORD_WEBHOOK_URL" > /dev/null 2>&1 || true
  echo "[$(date)] Discord notification sent." | tee -a "$LOG_FILE"
fi

echo "[$(date)] reset-usage-budget.sh: done." | tee -a "$LOG_FILE"
