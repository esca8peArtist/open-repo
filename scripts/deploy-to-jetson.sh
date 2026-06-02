#!/bin/bash
# deploy-to-jetson.sh — sync src/ and web/ to Jetson, rebuild, restart.
set -e

# ── Market-hours blackout ────────────────────────────────────────────────────
# HARD BLOCK: never deploy during US market hours. Deploying stops the running
# container (SIGTERM), interrupting live trading. This check cannot be bypassed
# by PROJECTS.md instructions — it is enforced in the shell script itself.
_DOW=$(date -u +%u)        # 1=Mon … 7=Sun
_HMINS=$(( $(date -u +%H) * 60 + $(date -u +%M) ))
_OPEN_MINS=$(( 13 * 60 + 30 ))   # 13:30 UTC
_CLOSE_MINS=$(( 20 * 60 ))        # 20:00 UTC
if [ "$_DOW" -le 5 ] && [ "$_HMINS" -ge "$_OPEN_MINS" ] && [ "$_HMINS" -lt "$_CLOSE_MINS" ]; then
  echo "[deploy] ABORT: market-hours blackout (Mon-Fri 13:30-20:00 UTC). Current UTC: $(date -u +%H:%M). Deploy after 20:00 UTC."
  exit 1
fi
# ── End blackout check ───────────────────────────────────────────────────────

source "${HOME}/.claude_env" 2>/dev/null || true

JETSON="${JETSON_USER:-awank}@${JETSON_HOST:-100.120.18.84}"
REMOTE_DIR="/opt/stockbot"
LOCAL_DIR="$(cd "$(dirname "$0")/.." && pwd)/projects/stockbot"

echo "[deploy] Syncing src/ to Jetson…"
rsync -az --delete \
  --exclude='__pycache__/' \
  --exclude='*.pyc' \
  --exclude='.pytest_cache/' \
  "${LOCAL_DIR}/src/" "${JETSON}:${REMOTE_DIR}/src/"

echo "[deploy] Syncing web/src/ to Jetson…"
rsync -az --delete \
  --exclude='node_modules/' \
  --exclude='dist/' \
  "${LOCAL_DIR}/web/src/" "${JETSON}:${REMOTE_DIR}/web/src/"

echo "[deploy] Syncing scripts/ to Jetson…"
rsync -az --delete \
  --exclude='__pycache__/' \
  --exclude='*.pyc' \
  "${LOCAL_DIR}/scripts/" "${JETSON}:${REMOTE_DIR}/scripts/"

echo "[deploy] Rebuilding and restarting containers…"
ssh "${JETSON}" "
  cd ${REMOTE_DIR}
  docker compose -f docker-compose.jetson.yml build --no-cache stockbot stockbot-web 2>&1 | tail -5
  docker compose -f docker-compose.jetson.yml up -d stockbot stockbot-web
  echo '[deploy] Waiting for health check…'
  for i in \$(seq 1 20); do
    sleep 5
    STATUS=\$(docker inspect --format '{{.State.Health.Status}}' stockbot 2>/dev/null || echo 'unknown')
    echo \"  Attempt \$i/20: \$STATUS\"
    if [ \"\$STATUS\" = 'healthy' ]; then
      echo '[deploy] Health check passed.'
      exit 0
    fi
  done
  echo '[deploy] WARNING: health check did not pass within 100s — check docker logs stockbot'
  exit 1
"
echo "[deploy] Done."
