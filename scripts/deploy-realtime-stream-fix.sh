#!/bin/bash

# Deploy June 24 realtime stream timeout fix to Jetson
# Usage: bash deploy-realtime-stream-fix.sh
# Run at 20:30 UTC after market close (20:00 UTC)

set -e

# Configuration
JETSON_USER="awank"
JETSON_IP="100.120.18.84"
STOCKBOT_REMOTE_DIR="/opt/stockbot"
LOCAL_STOCKBOT_DIR="/home/awank/dev/SuperClaude_Framework/projects/stockbot"
DEPLOYMENT_LOG="/tmp/deploy-realtime-stream-fix-$(date +%s).log"

echo "=========================================="
echo "Deploying Real-Time Stream Fix to Jetson"
echo "=========================================="
echo "Time: $(date -u '+%Y-%m-%d %H:%M:%S UTC')"
echo "Target: $JETSON_IP"
echo "Log: $DEPLOYMENT_LOG"
echo ""

# Function to run command on Jetson
jetson_exec() {
    ssh -o ConnectTimeout=10 -o StrictHostKeyChecking=no "$JETSON_USER@$JETSON_IP" "$1" 2>&1
}

# Function to log message
log_msg() {
    echo "[$(date -u '+%H:%M:%S')] $1" | tee -a "$DEPLOYMENT_LOG"
}

# Step 1: Pre-flight checks
log_msg "=== STEP 1: PRE-FLIGHT CHECKS ==="
log_msg "Checking Jetson connectivity..."
if ! jetson_exec "echo OK" > /dev/null 2>&1; then
    log_msg "ERROR: Cannot reach Jetson at $JETSON_IP"
    exit 1
fi
log_msg "✓ Jetson accessible"

log_msg "Checking if stockbot container is running..."
if ! jetson_exec "docker ps | grep -q stockbot"; then
    log_msg "WARNING: stockbot container not running (may be restarting)"
else
    log_msg "✓ stockbot container is running"
fi

# Step 2: Sync code
log_msg ""
log_msg "=== STEP 2: SYNCING CODE ==="
log_msg "Syncing src/ to Jetson..."
cd "$LOCAL_STOCKBOT_DIR" || exit 1

# Use rsync with --exclude .env to avoid overwriting production config
rsync -az --exclude='.env' --exclude='.git' --exclude='__pycache__' \
    --exclude='*.pyc' --exclude='.venv' --exclude='database/' \
    src/ "$JETSON_USER@$JETSON_IP:$STOCKBOT_REMOTE_DIR/src/" 2>&1 | tee -a "$DEPLOYMENT_LOG"

log_msg "✓ Code synced"

# Step 3: Verify fix was applied
log_msg ""
log_msg "=== STEP 3: VERIFY FIX APPLIED ==="
log_msg "Checking if timeout wrapper removed..."

# Look for the line WITHOUT asyncio.wait_for
TIMEOUT_CHECK=$(jetson_exec "grep -A 1 'await self.stream._run_forever()' $STOCKBOT_REMOTE_DIR/src/data/realtime_stream.py | head -1")

if echo "$TIMEOUT_CHECK" | grep -q "asyncio.wait_for"; then
    log_msg "ERROR: asyncio.wait_for still present in code!"
    log_msg "  Found: $TIMEOUT_CHECK"
    exit 1
fi

log_msg "✓ Timeout wrapper removed"
log_msg "  Found: $TIMEOUT_CHECK"

# Step 4: Restart container
log_msg ""
log_msg "=== STEP 4: RESTARTING CONTAINER ==="
log_msg "Stopping container..."
jetson_exec "docker stop stockbot" 2>&1 | tee -a "$DEPLOYMENT_LOG" || true
sleep 2

log_msg "Starting container..."
jetson_exec "docker start stockbot" 2>&1 | tee -a "$DEPLOYMENT_LOG"

# Step 5: Verify health
log_msg ""
log_msg "=== STEP 5: HEALTH VERIFICATION ==="
log_msg "Waiting 10 seconds for container to stabilize..."
sleep 10

log_msg "Checking Docker logs (last 20 lines)..."
LOGS=$(jetson_exec "docker logs stockbot --tail=20 2>&1")
echo "$LOGS" | tee -a "$DEPLOYMENT_LOG"

if echo "$LOGS" | grep -q "error\|ERROR\|failed\|FAILED"; then
    log_msg "WARNING: Error messages found in logs — see above"
else
    log_msg "✓ No obvious errors in logs"
fi

log_msg "Checking API health endpoint..."
HEALTH=$(jetson_exec "curl -s http://127.0.0.1:8000/api/health 2>&1")
echo "  Response: $HEALTH" | tee -a "$DEPLOYMENT_LOG"

if echo "$HEALTH" | grep -q '"status":"ok"'; then
    log_msg "✓ API health check passed"
else
    log_msg "WARNING: API health check returned unexpected response"
fi

# Step 6: Summary
log_msg ""
log_msg "=========================================="
log_msg "DEPLOYMENT COMPLETE"
log_msg "=========================================="
log_msg "Log saved to: $DEPLOYMENT_LOG"
log_msg ""
log_msg "Next steps:"
log_msg "1. Monitor container logs before market open"
log_msg "2. June 25 13:15 UTC: Begin Phase 0 pre-market gates"
log_msg "3. June 25 13:30 UTC: Market open — verify signals generated"
log_msg ""
log_msg "If stream still times out:"
log_msg "1. Review Docker logs: docker logs stockbot --since 10m"
log_msg "2. Check realtime_stream.py: docker exec stockbot grep -A 5 'def _run_async'"
log_msg "3. Rollback: docker stop stockbot && docker run [with previous image]"

exit 0
