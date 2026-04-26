#!/usr/bin/env bash
# flush_queues.sh — Gracefully drain AgentCore task queues before Redis shutdown
# Containerized AI Agents — v1.0
#
# Waits for all task queue Lists to drain naturally (workers consuming items),
# then force-deletes remaining items after a configurable timeout.
# Intended for use as the ExecStop handler in agentcore.service.
#
# Usage:
#   ExecStop=/opt/redis/flush_queues.sh
#   ExecStop=/opt/redis/flush_queues.sh --timeout 60   # custom timeout
#
# Environment variables (can be overridden):
#   REDIS_HOST        Redis host (default: localhost)
#   REDIS_PORT        Redis port (default: 6379)
#   REDIS_PASSWORD    Redis auth password (default: empty)
#   DRAIN_TIMEOUT     Seconds to wait for queues to drain naturally (default: 30)
#
# Exit codes:
#   0  — All queues drained cleanly within timeout.
#   2  — Timeout reached; queues force-cleared. Items were in flight.

set -euo pipefail

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
REDIS_HOST="${REDIS_HOST:-localhost}"
REDIS_PORT="${REDIS_PORT:-6379}"
REDIS_PASSWORD="${REDIS_PASSWORD:-}"
DRAIN_TIMEOUT="${DRAIN_TIMEOUT:-30}"

QUEUES=(
    "agentcore:queue:high"
    "agentcore:queue:normal"
    "agentcore:queue:low"
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
log() {
    echo "[flush_queues] $(date -u '+%Y-%m-%dT%H:%M:%SZ') $*" >&2
}

redis_cmd() {
    if [[ -n "$REDIS_PASSWORD" ]]; then
        redis-cli --no-auth-warning \
            -h "$REDIS_HOST" -p "$REDIS_PORT" \
            -a "$REDIS_PASSWORD" \
            "$@"
    else
        redis-cli -h "$REDIS_HOST" -p "$REDIS_PORT" "$@"
    fi
}

get_queue_length() {
    local queue="$1"
    redis_cmd llen "$queue" 2>/dev/null || echo "0"
}

total_queue_depth() {
    local total=0
    for queue in "${QUEUES[@]}"; do
        depth=$(get_queue_length "$queue")
        total=$(( total + depth ))
    done
    echo "$total"
}

print_queue_depths() {
    for queue in "${QUEUES[@]}"; do
        depth=$(get_queue_length "$queue")
        log "  ${queue}: ${depth} items"
    done
}

force_clear_queues() {
    log "Force-clearing remaining queue items..."
    for queue in "${QUEUES[@]}"; do
        depth=$(get_queue_length "$queue")
        if [[ "$depth" -gt 0 ]]; then
            redis_cmd del "$queue" > /dev/null
            log "  Deleted ${queue} (${depth} items discarded)"
        fi
    done
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
log "Starting queue drain — timeout: ${DRAIN_TIMEOUT}s"
log "Queues monitored:"
print_queue_depths

INITIAL_DEPTH=$(total_queue_depth)
if [[ "$INITIAL_DEPTH" -eq 0 ]]; then
    log "All queues already empty. Nothing to drain."
    exit 0
fi

log "Total items in queue: ${INITIAL_DEPTH}. Waiting for workers to drain..."

ELAPSED=0
POLL_INTERVAL=2

while [[ "$ELAPSED" -lt "$DRAIN_TIMEOUT" ]]; do
    sleep "$POLL_INTERVAL"
    ELAPSED=$(( ELAPSED + POLL_INTERVAL ))

    DEPTH=$(total_queue_depth)
    log "  t+${ELAPSED}s — total queue depth: ${DEPTH}"

    if [[ "$DEPTH" -eq 0 ]]; then
        log "All queues drained cleanly after ${ELAPSED}s."
        exit 0
    fi
done

# ---------------------------------------------------------------------------
# Timeout reached — force clear
# ---------------------------------------------------------------------------
log "WARN: Drain timeout (${DRAIN_TIMEOUT}s) reached. Remaining items:"
print_queue_depths
force_clear_queues
log "Queues force-cleared. Redis is safe to stop."
exit 2
