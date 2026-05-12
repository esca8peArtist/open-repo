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
# Strips HTML comment markers (<!-- ... -->) so auto-generated block wrappers
# like AUTO:CALIBRATION don't appear as literal text in the state file.
BLOCKED_SECTION=$(awk '/^## Active Blocks/{found=1; next} found && /^## Resolved/{exit} found{print}' \
  "$WORKSPACE/BLOCKED.md" 2>/dev/null | \
  python3 -c "
import sys, re
text = sys.stdin.read()
text = re.sub(r'<!--[^>]*-->', '', text)
text = re.sub(r'\n{3,}', '\n\n', text)
lines = [l for l in text.splitlines() if l.strip()]
print('\n'.join(lines[:30]))
" 2>/dev/null || true)
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
    if [ -n "$current_focus" ]; then
      focus_truncated=$(echo "$current_focus" | cut -c1-500)
      if [ ${#current_focus} -gt 500 ]; then
        focus_truncated+=" … *(truncated — prune Current focus in PROJECTS.md)*"
      fi
      PROJECT_SUMMARIES+="**Focus**: $focus_truncated\n"
    fi
    [ -n "$current_blocked" ] && [ "$current_blocked" != "—" ] && PROJECT_SUMMARIES+="**Blocked**: $current_blocked\n"
    PROJECT_SUMMARIES+="\n"
    current_project=""
  fi
done < "$WORKSPACE/PROJECTS.md"

# ── State drift validator: cross-check PROJECTS.md Blocked on: vs BLOCKED.md ──
# Also detects stale "Current focus" text (references session numbers ≥15 behind current)
DRIFT_WARNINGS=$(python3 - "$WORKSPACE/PROJECTS.md" "$WORKSPACE/BLOCKED.md" "$WORKSPACE/CHECKIN.md" <<'PYEOF'
import re, sys
from pathlib import Path

projects_text = Path(sys.argv[1]).read_text(errors="replace")
blocked_text = Path(sys.argv[2]).read_text(errors="replace")
checkin_text = Path(sys.argv[3]).read_text(errors="replace") if len(sys.argv) > 3 and Path(sys.argv[3]).exists() else ""

# Active block titles from BLOCKED.md
active_m = re.search(r'## Active Blocks\n(.*?)(?=\n## |\Z)', blocked_text, re.DOTALL)
active_titles = set()
if active_m:
    for t in re.findall(r'### (.+)', active_m.group(1)):
        active_titles.add(t.lower())

# Current session number from most recent CHECKIN entry
cur_m = re.search(r'Session (\d+)', checkin_text)
current_session = int(cur_m.group(1)) if cur_m else 0

warnings = []

# 1. Blocked on: drift — PROJECTS.md claims blocked but no matching BLOCKED.md entry
for m in re.finditer(r'### (.+?)\n.*?\*\*Blocked on\*\*: (.+)', projects_text, re.DOTALL):
    project = m.group(1).strip()
    blocked_val = m.group(2).strip()
    if blocked_val in ('—', 'None', ''):
        continue
    has_block = any(project.lower() in t for t in active_titles)
    if not has_block:
        warnings.append(f"⚠️ DRIFT: {project} has 'Blocked on: {blocked_val[:80]}' in PROJECTS.md but no matching entry in BLOCKED.md Active Blocks — stale or missing block entry")

# 2. Stale focus — Current focus references a session number ≥15 sessions behind current
if current_session > 0:
    for m in re.finditer(r'### (.+?)\n(.*?)(?=\n### |\Z)', projects_text, re.DOTALL):
        project = m.group(1).strip()
        focus_m = re.search(r'\*\*Current focus\*\*: (.{1,500})', m.group(2))
        if not focus_m:
            continue
        refs = [int(s) for s in re.findall(r'Session (\d+)', focus_m.group(1))]
        if refs:
            staleness = current_session - max(refs)
            if staleness >= 15:
                warnings.append(f"⚠️ STALE FOCUS: {project} — focus references Session {max(refs)} ({staleness} sessions ago); prune Current focus in PROJECTS.md")

print('\n'.join(warnings) if warnings else '')
PYEOF
)

# ── Recent resolutions from BLOCKED.md Resolved Archive ──────────────────────
RESOLVED_RECENT=$(python3 - "$WORKSPACE/BLOCKED.md" <<'PYEOF'
import re, sys
from pathlib import Path

text = Path(sys.argv[1]).read_text(errors="replace")
archive_m = re.search(r'## Resolved Archive\n(.*?)(?=\n## |\Z)', text, re.DOTALL)
if not archive_m:
    print('*(none in archive)*')
    sys.exit(0)

blocks = re.split(r'\n(?=### )', archive_m.group(1))
entries = []
for block in blocks:
    block = block.strip()
    if not block:
        continue
    title_m = re.search(r'### (.+)', block)
    resolved_m = re.search(r'\*\*Date resolved\*\*:\s*(.+?)(?:\n|$)', block)
    if title_m and resolved_m:
        entries.append(f"• {title_m.group(1).strip()} ← {resolved_m.group(1).strip()}")

print('\n'.join(entries[:5]) if entries else '*(none in archive)*')
PYEOF
)
[ -z "$RESOLVED_RECENT" ] && RESOLVED_RECENT="*(none in archive)*"

# ── Weekly maintenance task: inject into INBOX if 7+ days since last prune ────
PRUNE_MARKER="$WORKSPACE/.last-prune-task"
TODAY=$(date +%Y-%m-%d)
LAST_PRUNE=$(cat "$PRUNE_MARKER" 2>/dev/null || echo "1970-01-01")
DAYS_SINCE=$(python3 -c "
from datetime import date
d = date.fromisoformat('$LAST_PRUNE')
print((date.today() - d).days)
" 2>/dev/null || echo "999")

if [ "$DAYS_SINCE" -ge 7 ]; then
  python3 - "$WORKSPACE/INBOX.md" <<'PYEOF'
import sys, fcntl, os
from datetime import datetime
from pathlib import Path

inbox = Path(sys.argv[1])
entry = f"- [WEEKLY-MAINTENANCE] Prune PROJECTS.md: trim each project's 'Current focus' to ≤2 paragraphs / 500 chars. Review quiescent projects (workout, off-grid-living, resume, open-repo) — pause any with no active work this week. Archive any BLOCKED.md Resolved Archive entries older than 30 days.\n"
lock_path = inbox.with_suffix(".lock")
with open(lock_path, "w") as lock:
    fcntl.flock(lock, fcntl.LOCK_EX)
    content = inbox.read_text(errors="replace")
    if "WEEKLY-MAINTENANCE" not in content:
        content = content.replace("## New Items\n", f"## New Items\n{entry}", 1)
        inbox.write_text(content)
        print("[generate-state] Weekly maintenance task injected into INBOX.md")
PYEOF
  echo "$TODAY" > "$PRUNE_MARKER"
fi

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
$([ -n "$DRIFT_WARNINGS" ] && printf '\n## State Drift Warnings\n%s\n' "$DRIFT_WARNINGS")
## Recently Resolved (last 5)
$RESOLVED_RECENT

## Inbox (unprocessed)
$INBOX_ITEMS

## Recent Log (last 40 lines of WORKLOG.md)
$RECENT_LOG
HEREDOC

echo "[$(date)] ORCHESTRATOR_STATE.md generated ($(wc -l < "$OUTPUT") lines)"
