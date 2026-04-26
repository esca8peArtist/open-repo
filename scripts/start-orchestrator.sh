#!/bin/bash
set -e

# Ensure local bin is on PATH (needed when running via systemd service)
export PATH="$HOME/.local/bin:$PATH"

WORKSPACE="$HOME/dev/SuperClaude_Framework"
PROMPT_FILE="$WORKSPACE/.claude/orchestrator-prompt.md"
LOG_FILE="$WORKSPACE/orchestrator.log"
MAX_TURNS=80
PAUSE_BETWEEN_SESSIONS=300       # 5 min between sessions
SUMMARY_INTERVAL=7200            # 2 hour summary interval
SESSION_TIMEOUT=5400             # 90 min max per session — kill if hung

# Orchestrator runs on Haiku (cheap orientation + delegation).
# Subagents (stockbot, rideshare, etc.) run on Sonnet per their agent definitions.
ORCHESTRATOR_MODEL="claude-haiku-4-5-20251001"

cd "$WORKSPACE"
[ -f "$HOME/.claude_env" ] && source "$HOME/.claude_env"

echo "[$(date)] Orchestrator starting." | tee -a "$LOG_FILE"

[ -n "$DISCORD_WEBHOOK_URL" ] && curl -s -H "Content-Type: application/json" \
  -d "{\"content\":\"[Claude] Orchestrator starting on Pi\"}" \
  "$DISCORD_WEBHOOK_URL" > /dev/null 2>&1 || true

send_summary() {
  [ -z "$DISCORD_WEBHOOK_URL" ] && return

  # Use Python for safe content extraction, truncation, and JSON encoding
  python3 - "$WORKSPACE/CHECKIN.md" "$WORKSPACE/BLOCKED.md" "$DISCORD_WEBHOOK_URL" <<'PYEOF'
import sys, json, re, subprocess
from pathlib import Path

checkin_file, blocked_file, webhook = sys.argv[1], sys.argv[2], sys.argv[3]

def extract_section(path, header_re):
    try:
        text = Path(path).read_text(encoding="utf-8", errors="replace")
        m = re.search(header_re, text)
        if not m:
            return "(not found)"
        start = m.end()
        # Stop at next --- or ## heading
        end_m = re.search(r'\n(---|\#\#)', text[start:])
        section = text[start: start + end_m.start()] if end_m else text[start:]
        # Truncate safely at character boundary
        return section.strip()[:600]
    except Exception as e:
        return f"(error reading: {e})"

checkin = extract_section(checkin_file, r'## Since Last Check-in')
blocked = extract_section(blocked_file, r'## Active Blocks')
if not blocked.strip():
    blocked = "None"

msg = f"**[Claude 2hr Update]**\n**Recent work:** {checkin}\n**Blocked:** {blocked}"
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

# Background watchdog: fires summary every 2hrs regardless of session state
summary_watchdog() {
  while true; do
    sleep "$SUMMARY_INTERVAL"
    if [ -n "$DISCORD_WEBHOOK_URL" ]; then
      send_summary
    fi
  done
}

# Start the summary watchdog in the background
summary_watchdog &
WATCHDOG_PID=$!
trap "kill $WATCHDOG_PID 2>/dev/null; exit" EXIT INT TERM

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
    echo "[$(date)] Usage gate: PAUSED (80% gate). $USAGE_CHECK" | tee -a "$LOG_FILE"
    echo "[$(date)] To override: touch $WORKSPACE/USAGE_PAUSE_OVERRIDE" | tee -a "$LOG_FILE"
    sleep "$PAUSE_BETWEEN_SESSIONS"
    continue
  else
    echo "[$(date)] Usage gate: THROTTLED. $USAGE_CHECK" | tee -a "$LOG_FILE"
    sleep "$PAUSE_BETWEEN_SESSIONS"
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

  # Auto-deploy to Jetson if orchestrator flagged it ready
  if [ -f "$WORKSPACE/DEPLOY_READY" ]; then
    echo "[$(date)] DEPLOY_READY flag found — deploying to Jetson..." | tee -a "$LOG_FILE"
    rm -f "$WORKSPACE/DEPLOY_READY"
    bash "$WORKSPACE/scripts/deploy-to-jetson.sh" >> "$LOG_FILE" 2>&1 || true
  fi

  sleep "$PAUSE_BETWEEN_SESSIONS"
done
