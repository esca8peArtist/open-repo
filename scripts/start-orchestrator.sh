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
  local checkin_content blocked_content msg

  # Extract "Since Last Check-in" section from CHECKIN.md (first 600 chars)
  checkin_content=$(awk '/## Since Last Check-in/{found=1; next} found && /^---/{exit} found{print}' \
    "$WORKSPACE/CHECKIN.md" 2>/dev/null | head -20 | tr '\n' ' ' | cut -c1-600)

  # Extract active blocks from BLOCKED.md (first 400 chars)
  blocked_content=$(awk '/## Active Blocks/{found=1; next} found && /^## Resolved/{exit} found{print}' \
    "$WORKSPACE/BLOCKED.md" 2>/dev/null | grep -v '^$' | head -10 | tr '\n' ' ' | cut -c1-400)

  [ -z "$checkin_content" ] && checkin_content="(nothing yet)"
  [ -z "$blocked_content" ] && blocked_content="None"

  msg="**[Claude 2hr Update]**\n**Recent work:** ${checkin_content}\n**Blocked:** ${blocked_content}"

  curl -s -H "Content-Type: application/json" \
    -d "{\"content\":\"$(echo "$msg" | sed 's/"/\\"/g')\"}" \
    "$DISCORD_WEBHOOK_URL" > /dev/null 2>&1 || true
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

LAST_SUMMARY=$(date +%s)

while true; do
  # ── Pre-session: ensure we're on master ───────────────────────────────────
  # This is the structural guard against branch drift. The orchestrator may end
  # a session on a feature branch; forcing master here means every session
  # starts clean and all orchestration file commits land on master.
  git -C "$WORKSPACE" checkout master >> "$LOG_FILE" 2>&1 || true

  # ── Pre-session: generate compact state file ──────────────────────────────
  echo "[$(date)] Generating orchestrator state..." | tee -a "$LOG_FILE"
  bash "$WORKSPACE/scripts/generate-orchestrator-state.sh" >> "$LOG_FILE" 2>&1 || true

  # ── Pre-session: pause/budget gate ────────────────────────────────────────
  # Use 'if' form so set -e doesn't kill the script when usage-check exits 1
  if USAGE_CHECK=$(python3 "$WORKSPACE/scripts/usage-check.py" --check 2>&1); then
    echo "[$(date)] Usage gate: OK. Starting Claude session..." | tee -a "$LOG_FILE"
  else
    echo "[$(date)] Usage gate: $USAGE_CHECK — skipping session." | tee -a "$LOG_FILE"
    echo "[$(date)] Next check in ${PAUSE_BETWEEN_SESSIONS}s..." | tee -a "$LOG_FILE"
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
