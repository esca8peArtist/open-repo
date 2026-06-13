#!/bin/bash
# No set -e: this is a long-running daemon loop where non-zero exits from
# subcommands (e.g. usage-check.py exit 2 = paused gate) are expected and
# must not kill the orchestrator.

# Ensure local bin is on PATH (needed when running via systemd service)
export PATH="$HOME/.local/bin:$PATH"

WORKSPACE="$HOME/dev/SuperClaude_Framework"
PROMPT_FILE="$WORKSPACE/.claude/orchestrator-prompt.md"
LOG_FILE="$WORKSPACE/orchestrator.log"
MAX_TURNS=80
PAUSE_BETWEEN_SESSIONS=300       # 5 min between sessions (normal post-session pause)
SUMMARY_INTERVAL=7200            # 2 hour summary interval
SESSION_TIMEOUT=5400             # 90 min max per session — kill if hung
DAILY_NOTIFY_HOUR=16             # 4pm local time for daily blocked + check-in digest
DAILY_NOTIFY_MARKER="$WORKSPACE/.last-daily-notify"

# Orchestrator runs on Haiku (cheap orientation + delegation).
# Subagents (stockbot, rideshare, etc.) run on Sonnet per their agent definitions.
ORCHESTRATOR_MODEL="claude-haiku-4-5-20251001"

cd "$WORKSPACE"
[ -f "$HOME/.claude_env" ] && source "$HOME/.claude_env"

echo "[$(date)] Orchestrator starting." | tee -a "$LOG_FILE"

# Only notify Discord on startup if we're not already in a usage pause.
# When paused, all Discord is suppressed until the billing week resets.
if [ ! -f "$WORKSPACE/USAGE_PAUSE" ] && [ -n "$DISCORD_WEBHOOK_URL" ]; then
  START_MSG="**[Claude] Orchestrator started** — $(date -u '+%a %b %-d %H:%M UTC')"
  curl -s -H "Content-Type: application/json" \
    -d "{\"content\":\"$START_MSG\"}" \
    "$DISCORD_WEBHOOK_URL" > /dev/null 2>&1 || true
fi

# Returns seconds until next Tuesday 00:00 UTC (billing reset), minimum 60s.
secs_until_reset() {
  python3 -c "
from datetime import datetime, timedelta, timezone
now = datetime.now(timezone.utc)
days_back = (now.date().weekday() - 1) % 7
next_tuesday = now.date() - timedelta(days=days_back) + timedelta(weeks=1)
reset = datetime(next_tuesday.year, next_tuesday.month, next_tuesday.day, tzinfo=timezone.utc)
print(max(60, int((reset - now).total_seconds())))
"
}

send_summary() {
  [ -z "$DISCORD_WEBHOOK_URL" ] && return

  python3 - "$WORKSPACE/CHECKIN.md" "$WORKSPACE/BLOCKED.md" "$DISCORD_WEBHOOK_URL" <<'PYEOF'
import sys, json, re, subprocess
from pathlib import Path

checkin_file, blocked_file, webhook = sys.argv[1], sys.argv[2], sys.argv[3]

def get_recent_session(path):
    try:
        text = Path(path).read_text(encoding="utf-8", errors="replace")
        # Match the first (most recent) Since Last Check-in heading and its body
        # Body ends at the next same-level heading or ---
        m = re.search(
            r'## Since Last Check-in \(([^)]+)\)[^\n]*\n(.*?)(?=\n## Since Last Check-in|\n---|\Z)',
            text, re.DOTALL
        )
        if not m:
            return "No recent session found"
        session_id = m.group(1).strip()
        body = m.group(2).strip()
        # Pull up to 4 bullet lines (-, ✅, 🔍, ⚠, etc.) skipping sub-headings
        bullets = []
        for line in body.splitlines():
            s = line.strip()
            if s and not s.startswith('#') and (s[0] in '-•' or s[0] in '✅🔍⚠️🟢🔴'):
                # Strip markdown bold/italic and leading markers
                clean = re.sub(r'\*+([^*]+)\*+', r'\1', s.lstrip('-• '))
                bullets.append(clean[:120])
            if len(bullets) >= 4:
                break
        result = f"**{session_id}**"
        if bullets:
            result += "\n" + "\n".join(f"• {b}" for b in bullets)
        return result
    except Exception as e:
        return f"(error: {e})"

def get_active_blocks(path):
    try:
        text = Path(path).read_text(encoding="utf-8", errors="replace")
        m = re.search(r'## Active Blocks\n(.*?)(?=\n## |\Z)', text, re.DOTALL)
        if not m:
            return "None"
        content = m.group(1)
        # Strip full auto-generated blocks (e.g. calibration reminder) — they have
        # their own weekly notification path and clutter the 2hr session summary.
        content = re.sub(r'<!-- AUTO:\w+:START -->.*?<!-- AUTO:\w+:END -->', '', content, flags=re.DOTALL)
        content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL).strip()
        if not content:
            return "None"
        titles = re.findall(r'### (.+?)(?:\n|$)', content)
        return "\n".join(f"• {t}" for t in titles[:5]) if titles else "None"
    except Exception as e:
        return f"(error: {e})"

session_summary = get_recent_session(checkin_file)
blocks = get_active_blocks(blocked_file)

msg = f"**[Claude 2hr Update]**\n{session_summary}\n\n**Blocked:** {blocks}"
payload = json.dumps({"content": msg})

result = subprocess.run(
    ["curl", "-s", "-w", "\n%{http_code}", "-H", "Content-Type: application/json",
     "-d", payload, webhook],
    capture_output=True, text=True, timeout=15
)
http_code = result.stdout.strip().split("\n")[-1]
if not http_code.startswith("2"):
    print(f"Discord summary failed: HTTP {http_code}", file=sys.stderr)
PYEOF
}

send_daily_digest() {
  [ -z "$DISCORD_WEBHOOK_URL" ] && return

  python3 - "$WORKSPACE/BLOCKED.md" "$WORKSPACE/CHECKIN.md" "$DISCORD_WEBHOOK_URL" <<'PYEOF'
import sys, json, re, subprocess
from datetime import date, datetime, timezone
from pathlib import Path

blocked_file, checkin_file, webhook = sys.argv[1], sys.argv[2], sys.argv[3]

def get_blocks_with_age(path):
    try:
        text = Path(path).read_text(encoding="utf-8", errors="replace")
        m = re.search(r'## Active Blocks\n(.*?)(?=\n## |\Z)', text, re.DOTALL)
        if not m:
            return "No active blocks."
        content = m.group(1)
        content = re.sub(r'<!-- AUTO:\w+:START -->.*?<!-- AUTO:\w+:END -->', '', content, flags=re.DOTALL)
        content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL).strip()
        if not content:
            return "No active blocks."
        blocks = re.split(r'\n(?=### )', content)
        lines = []
        for block in blocks:
            block = block.strip()
            if not block:
                continue
            title_m = re.search(r'### (.+)', block)
            date_m = re.search(r'\*\*Date blocked\*\*:\s*(\d{4}-\d{2}-\d{2})', block)
            need_m = re.search(r'\*\*What I need\*\*:\s*(.+?)(?=\n\*\*|\Z)', block, re.DOTALL)
            title = title_m.group(1) if title_m else "?"
            if date_m:
                d = date.fromisoformat(date_m.group(1))
                age = (date.today() - d).days
                age_str = f"({age}d)" if age > 0 else "(today)"
            else:
                age_str = ""
            need = need_m.group(1).strip()[:120].replace('\n', ' ') if need_m else ""
            lines.append(f"• **{title}** {age_str}")
            if need:
                lines.append(f"  → {need}")
        return "\n".join(lines) if lines else "No active blocks."
    except Exception as e:
        return f"(error: {e})"

def get_checkin_summary(path):
    try:
        text = Path(path).read_text(encoding="utf-8", errors="replace")
        m = re.search(
            r'## Since Last Check-in \(([^)]+)\)[^\n]*\n(.*?)(?=\n## Since Last Check-in|\n---|\Z)',
            text, re.DOTALL
        )
        if not m:
            return "No recent check-in found."
        session_id = m.group(1).strip()
        body = m.group(2).strip()
        bullets = []
        for line in body.splitlines():
            s = line.strip()
            if s and not s.startswith('#') and (s[0] in '-•' or s[0] in '✅🔍⚠️🟢🔴'):
                clean = re.sub(r'\*+([^*]+)\*+', r'\1', s.lstrip('-• '))
                bullets.append(clean[:120])
            if len(bullets) >= 5:
                break
        result = f"**{session_id}**"
        if bullets:
            result += "\n" + "\n".join(f"• {b}" for b in bullets)
        return result
    except Exception as e:
        return f"(error: {e})"

blocks = get_blocks_with_age(blocked_file)
checkin = get_checkin_summary(checkin_file)
now_str = datetime.now().strftime("%a %b %-d %H:%M")

msg = (
    f"**[Claude Daily Digest — {now_str}]**\n\n"
    f"**Blocked (waiting on you):**\n{blocks}\n\n"
    f"**Last session:**\n{checkin}"
)
payload = json.dumps({"content": msg})
result = subprocess.run(
    ["curl", "-s", "-w", "\n%{http_code}", "-H", "Content-Type: application/json",
     "-d", payload, webhook],
    capture_output=True, text=True, timeout=15
)
http_code = result.stdout.strip().split("\n")[-1]
if not http_code.startswith("2"):
    print(f"Discord daily digest failed: HTTP {http_code}", file=sys.stderr)
PYEOF
}

# Background watchdog: fires summary every 2hrs, but silent while usage-paused.
summary_watchdog() {
  while true; do
    sleep "$SUMMARY_INTERVAL"
    if [ -n "$DISCORD_WEBHOOK_URL" ] && [ ! -f "$WORKSPACE/USAGE_PAUSE" ]; then
      send_summary
    fi
  done
}

# Daily digest watchdog: fires once at 4pm with full blocks + check-in.
daily_digest_watchdog() {
  while true; do
    sleep 300  # check every 5 minutes
    CURRENT_HOUR=$(date +%H)
    TODAY=$(date +%Y-%m-%d)
    LAST_DATE=$(cat "$DAILY_NOTIFY_MARKER" 2>/dev/null || echo "")
    if [ "$CURRENT_HOUR" -eq "$DAILY_NOTIFY_HOUR" ] && [ "$TODAY" != "$LAST_DATE" ]; then
      if [ -n "$DISCORD_WEBHOOK_URL" ] && [ ! -f "$WORKSPACE/USAGE_PAUSE" ]; then
        send_daily_digest
        echo "$TODAY" > "$DAILY_NOTIFY_MARKER"
        echo "[$(date)] Daily digest sent." >> "$LOG_FILE"
      fi
    fi
  done
}

# Start watchdogs in the background
summary_watchdog &
WATCHDOG_PID=$!
daily_digest_watchdog &
DAILY_WATCHDOG_PID=$!
trap "kill $WATCHDOG_PID $DAILY_WATCHDOG_PID 2>/dev/null; exit" EXIT INT TERM

while true; do
  # ── Pre-session: ensure we're on master ───────────────────────────────────
  # This is the structural guard against branch drift. The orchestrator may end
  # a session on a feature branch; forcing master here means every session
  # starts clean and all orchestration file commits land on master.
  git -C "$WORKSPACE" checkout master >> "$LOG_FILE" 2>&1 || true

  # ── Pre-session: warn if usage-monitor is stale (cron may be dead) ────────
  MONITOR_LAST_RUN="$WORKSPACE/.usage-monitor-last-run"
  if [ -f "$MONITOR_LAST_RUN" ]; then
    LAST_RUN=$(cat "$MONITOR_LAST_RUN")
    LAST_EPOCH=$(python3 -c "from datetime import datetime,timezone; print(int(datetime.fromisoformat('$LAST_RUN').timestamp()))" 2>/dev/null || echo 0)
    NOW_EPOCH=$(date +%s)
    AGE=$(( NOW_EPOCH - LAST_EPOCH ))
    if [ "$AGE" -gt 5400 ]; then
      echo "[$(date)] WARNING: usage-monitor last ran ${AGE}s ago — cron may be dead." | tee -a "$LOG_FILE"
    fi
  fi

  # ── Pre-session: generate compact state file ──────────────────────────────
  echo "[$(date)] Generating orchestrator state..." | tee -a "$LOG_FILE"
  bash "$WORKSPACE/scripts/generate-orchestrator-state.sh" >> "$LOG_FILE" 2>&1 || true

  # ── Pre-session: pause/budget gate ────────────────────────────────────────
  # Exit codes from usage-check.py --check:
  #   0 = proceed normally
  #   1 = over 90% budget — hard throttle, sessions blocked
  #   2 = paused at 80% by usage-monitor — user can override via USAGE_PAUSE_OVERRIDE
  USAGE_CHECK=$(python3 "$WORKSPACE/scripts/usage-check.py" --check 2>&1)
  USAGE_EXIT=$?

  if [ "$USAGE_EXIT" -eq 0 ]; then
    echo "[$(date)] Usage gate: OK. Starting Claude session..." | tee -a "$LOG_FILE"
  elif [ "$USAGE_EXIT" -eq 2 ]; then
    RESET_SECS=$(secs_until_reset)
    echo "[$(date)] Usage gate: PAUSED (80% gate). Polling every 5min until unpaused or Tuesday reset (${RESET_SECS}s). $USAGE_CHECK" | tee -a "$LOG_FILE"
    echo "[$(date)] To override: touch $WORKSPACE/USAGE_PAUSE_OVERRIDE" | tee -a "$LOG_FILE"
    # Notify Discord once when entering pause — sentinel prevents repeated pings each poll cycle
    PAUSE_NOTIFIED="$WORKSPACE/.pause-discord-notified"
    if [ ! -f "$PAUSE_NOTIFIED" ] && [ -n "$DISCORD_WEBHOOK_URL" ]; then
      USAGE_PCT=$(python3 "$WORKSPACE/scripts/usage-check.py" --json 2>/dev/null \
        | python3 -c "import json,sys; r=json.load(sys.stdin); print(f\"{max(r['pct']['sonnet'],r['pct']['all_models']):.0f}\")" 2>/dev/null || echo "80+")
      RESET_H=$(( RESET_SECS / 3600 ))
      curl -s -H "Content-Type: application/json" \
        -d "{\"content\":\"⏸️ **[Claude] Orchestrator self-paused** — usage at ${USAGE_PCT}% (80% gate). Sessions held until Tuesday reset (~${RESET_H}h) or manual override.\nOverride: \`touch $WORKSPACE/USAGE_PAUSE_OVERRIDE\`\"}" \
        "$DISCORD_WEBHOOK_URL" > /dev/null 2>&1 || true
      touch "$PAUSE_NOTIFIED"
      echo "[$(date)] Sent Discord pause notification." | tee -a "$LOG_FILE"
    fi
    # Poll every 5 minutes so recalibration or PAUSE_FILE deletion takes effect quickly
    while true; do
      sleep 300
      python3 "$WORKSPACE/scripts/usage-check.py" --check > /dev/null 2>&1
      [ $? -ne 2 ] && break
    done
    rm -f "$PAUSE_NOTIFIED"  # clear sentinel so next pause triggers a fresh notification
    continue
  else
    RESET_SECS=$(secs_until_reset)
    echo "[$(date)] Usage gate: THROTTLED (90%+). Polling every 5min until Tuesday reset (${RESET_SECS}s). $USAGE_CHECK" | tee -a "$LOG_FILE"
    # Poll every 5 minutes rather than one long sleep
    while true; do
      sleep 300
      python3 "$WORKSPACE/scripts/usage-check.py" --check > /dev/null 2>&1
      [ $? -eq 0 ] && break
    done
    continue
  fi

  # ── Run session ───────────────────────────────────────────────────────────
  # Orchestrator uses Haiku for cheap orientation/delegation.
  # Worker subagents (stockbot, rideshare, etc.) use Sonnet per their agent definitions.
  timeout "$SESSION_TIMEOUT" "$HOME/.local/bin/claude" \
    --dangerously-skip-permissions \
    --max-turns "$MAX_TURNS" \
    --model "$ORCHESTRATOR_MODEL" \
    -p "$(cat "$PROMPT_FILE")" 2>&1 | tee -a "$LOG_FILE"
  EXIT_CODE=${PIPESTATUS[0]}

  if [ "$EXIT_CODE" -eq 124 ]; then
    echo "[$(date)] WARNING: Session killed after ${SESSION_TIMEOUT}s timeout (hung session)." | tee -a "$LOG_FILE"
    [ -n "$DISCORD_WEBHOOK_URL" ] && curl -s -H "Content-Type: application/json" \
      -d "{\"content\":\"⚠️ [Claude] Orchestrator session timed out after 90min and was restarted. Check BLOCKED.md.\"}" \
      "$DISCORD_WEBHOOK_URL" > /dev/null 2>&1 || true
  fi

  echo "[$(date)] Session ended. Pausing ${PAUSE_BETWEEN_SESSIONS}s..." | tee -a "$LOG_FILE"

  # ── Post-session: return to master ────────────────────────────────────────
  git -C "$WORKSPACE" checkout master >> "$LOG_FILE" 2>&1 || true

  # ── Post-session: verify CHECKIN.md was updated ────────────────────────────
  # Timeout-killed sessions (124) didn't commit — skip the warning for those.
  if [ "$EXIT_CODE" -ne 124 ]; then
    CHECKIN_IN_LAST=$(git -C "$WORKSPACE" show --name-only --format="" HEAD 2>/dev/null | grep -c "CHECKIN.md" || echo "0")
    if [ "$CHECKIN_IN_LAST" -eq 0 ]; then
      echo "[$(date)] WARNING: CHECKIN.md not in last commit — orchestrator may have skipped check-in step." | tee -a "$LOG_FILE"
      if [ -n "$DISCORD_WEBHOOK_URL" ] && [ ! -f "$WORKSPACE/USAGE_PAUSE" ]; then
        curl -s -H "Content-Type: application/json" \
          -d "{\"content\":\"⚠️ [Claude] Session ended but CHECKIN.md was not updated — orchestrator skipped the check-in step.\"}" \
          "$DISCORD_WEBHOOK_URL" > /dev/null 2>&1 || true
      fi
    fi
  fi

  # ── Post-session: notify Discord when all unpaused projects are idle ─────────
  # Fires once when the orchestrator first reports no actionable work remaining.
  # Clears automatically when the next session produces real commits.
  if [ "$EXIT_CODE" -ne 124 ]; then
    LAST_MSG=$(git -C "$WORKSPACE" log -1 --format="%s" 2>/dev/null || echo "")
    ALL_WORK_NOTIFIED="$WORKSPACE/.all-work-discord-notified"
    if echo "$LAST_MSG" | grep -qiE "no autonomous work|all autonomous work.*complete|standing by for user|no work available"; then
      if [ ! -f "$ALL_WORK_NOTIFIED" ] && [ -n "$DISCORD_WEBHOOK_URL" ] && [ ! -f "$WORKSPACE/USAGE_PAUSE" ]; then
        curl -s -H "Content-Type: application/json" \
          -d "{\"content\":\"✅ **[Claude] All available work complete** — orchestrator is standing by. No actionable items remain on active projects. Add tasks to INBOX.md or check CHECKIN.md for details.\"}" \
          "$DISCORD_WEBHOOK_URL" > /dev/null 2>&1 || true
        touch "$ALL_WORK_NOTIFIED"
        echo "[$(date)] Sent Discord all-work-complete notification." | tee -a "$LOG_FILE"
      fi
    else
      # Work was done this session — reset sentinel so the next idle period re-notifies
      rm -f "$ALL_WORK_NOTIFIED"
    fi
  fi

  # Auto-deploy to Jetson if orchestrator flagged it ready
  if [ -f "$WORKSPACE/DEPLOY_READY" ]; then
    echo "[$(date)] DEPLOY_READY flag found — deploying to Jetson..." | tee -a "$LOG_FILE"
    rm -f "$WORKSPACE/DEPLOY_READY"
    # Commit the deletion so Claude sessions don't see "D DEPLOY_READY" in git
    # status and mistakenly restore the flag, causing a redeploy loop.
    git -C "$WORKSPACE" add DEPLOY_READY >> "$LOG_FILE" 2>&1 || true
    git -C "$WORKSPACE" commit -m "chore: consumed DEPLOY_READY — deployment triggered" >> "$LOG_FILE" 2>&1 || true
    bash "$WORKSPACE/scripts/deploy-to-jetson.sh" >> "$LOG_FILE" 2>&1 || true
  fi

  sleep "$PAUSE_BETWEEN_SESSIONS"
done
