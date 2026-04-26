#!/bin/bash
# generate-orchestrator-state.sh
# Generates a compact ORCHESTRATOR_STATE.md before each autonomous session.
# Reads the 5 source files and distills only what the orchestrator needs per session.
# This means the orchestrator reads ONE compact file instead of 5 large raw files,
# saving 60-70% on file-read token overhead.

set -e

WORKSPACE="${CLAUDE_WORKSPACE:-$HOME/dev/SuperClaude_Framework}"
OUTPUT="$WORKSPACE/ORCHESTRATOR_STATE.md"
SCRIPTS="$WORKSPACE/scripts"

cd "$WORKSPACE"

GENERATED_AT=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# ── INBOX cleanup: delete comment blocks older than 7 days ────────────────────
python3 - "$WORKSPACE/INBOX.md" <<'PYEOF'
import re, sys, os
from pathlib import Path
from datetime import datetime, timedelta, timezone

inbox = Path(sys.argv[1])
text = inbox.read_text(errors="replace")
cutoff = datetime.now(timezone.utc) - timedelta(days=7)

def is_old_comment(block):
    # Try to find a date in the comment header line: <!-- Processed YYYY-MM-DD ... -->
    m = re.search(r'(\d{4}-\d{2}-\d{2})', block.split('\n')[0])
    if not m:
        return False
    try:
        d = datetime.fromisoformat(m.group(1)).replace(tzinfo=timezone.utc)
        return d < cutoff
    except ValueError:
        return False

# Remove comment blocks that are old enough to delete
cleaned = re.sub(r'<!--.*?-->', lambda m: '' if is_old_comment(m.group(0)) else m.group(0), text, flags=re.DOTALL)

if cleaned != text:
    tmp = inbox.with_suffix(".tmp")
    tmp.write_text(cleaned)
    os.replace(tmp, inbox)
    removed = text.count('<!--') - cleaned.count('<!--')
    print(f"[INBOX cleanup] Removed {removed} comment block(s) older than 7 days.")
PYEOF

# ── Usage check one-liner ──────────────────────────────────────────────────────
USAGE_LINE=$(python3 "$SCRIPTS/usage-check.py" --checkin 2>/dev/null || echo "⚠️ usage-check unavailable")

# ── Active blocks (Active Blocks section only) ─────────────────────────────────
BLOCKED_SECTION=$(awk '/^## Active Blocks/{found=1; next} found && /^## Resolved/{exit} found{print}' \
  "$WORKSPACE/BLOCKED.md" 2>/dev/null | grep -v '^\s*$' | head -30)
[ -z "$BLOCKED_SECTION" ] && BLOCKED_SECTION="*No active blocks.*"

# ── INBOX new items (skip HTML comment blocks — those are already processed) ───
INBOX_ITEMS=$(python3 - "$WORKSPACE/INBOX.md" <<'PYEOF'
import re, sys
from pathlib import Path
text = Path(sys.argv[1]).read_text(errors="replace")
m = re.search(r'## New Items\n(.*?)(?=\n## |\Z)', text, re.DOTALL)
section = m.group(1) if m else ""
section = re.sub(r'<!--.*?-->', '', section, flags=re.DOTALL)
lines = [l for l in section.split('\n') if l.strip() and not l.strip().startswith('<!--') and l.strip() != '---']
print('\n'.join(lines[:20]) if lines else '*(no new items)*')
PYEOF
)
[ -z "$INBOX_ITEMS" ] && INBOX_ITEMS="*(no new items)*"

# ── Priority order + active project summaries from PROJECTS.md ────────────────
# Extract priority list
PRIORITY_LIST=$(awk '/^## Priority Order/{found=1; next} found && /^---/{exit} found{print}' \
  "$WORKSPACE/PROJECTS.md" 2>/dev/null | grep -v '^\s*$' | head -15)

# Extract each active project's name, status, and current focus (skip Archived/Paused)
PROJECT_SUMMARIES=""
while IFS= read -r line; do
  if [[ "$line" =~ ^###\  ]]; then
    current_project="$line"
    current_status=""
    current_focus=""
    current_blocked=""
  elif [[ "$line" =~ ^\*\*Status\*\*: ]]; then
    current_status="${line#**Status**: }"
    if [[ "$current_status" == *"Archived"* ]] || [[ "$current_status" == *"Paused"* ]]; then
      current_project=""  # skip this project
    fi
  elif [[ "$line" =~ ^\*\*Current\ focus\*\*: ]]; then
    current_focus="${line#**Current focus**: }"
  elif [[ "$line" =~ ^\*\*Blocked\ on\*\*: ]]; then
    current_blocked="${line#**Blocked on**: }"
  elif [[ "$line" == "---" ]] && [ -n "$current_project" ] && [ -n "$current_status" ]; then
    PROJECT_SUMMARIES+="$current_project\n"
    PROJECT_SUMMARIES+="**Status**: $current_status\n"
    [ -n "$current_focus" ] && PROJECT_SUMMARIES+="**Focus**: $(echo "$current_focus" | cut -c1-300)\n"
    [ -n "$current_blocked" ] && [ "$current_blocked" != "—" ] && PROJECT_SUMMARIES+="**Blocked**: $current_blocked\n"
    PROJECT_SUMMARIES+="\n"
    current_project=""
  fi
done < "$WORKSPACE/PROJECTS.md"

# ── Recent WORKLOG (last 40 lines) ────────────────────────────────────────────
RECENT_LOG=$(tail -40 "$WORKSPACE/WORKLOG.md" 2>/dev/null || echo "(WORKLOG not found)")

# ── Write ORCHESTRATOR_STATE.md ───────────────────────────────────────────────
cat > "$OUTPUT" << HEREDOC
# Orchestrator State
> Auto-generated at $GENERATED_AT — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
$USAGE_LINE

## Priority Order
$PRIORITY_LIST

## Active Projects
$(printf '%b' "$PROJECT_SUMMARIES")
## Active Blocks
$BLOCKED_SECTION

## Inbox (unprocessed)
$INBOX_ITEMS

## Recent Log (last 40 lines of WORKLOG.md)
$RECENT_LOG
HEREDOC

echo "[$(date)] ORCHESTRATOR_STATE.md generated ($(wc -l < "$OUTPUT") lines)"
