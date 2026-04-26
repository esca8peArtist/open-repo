#!/usr/bin/env bash
# healthcheck.sh — Docker health check for the Redis service
# Containerized AI Agents — v1.0
#
# Issues a PING command via redis-cli and checks for a PONG response.
# The REDIS_PASSWORD env var is injected by Docker from the compose environment.
#
# Exit codes (Docker convention):
#   0  — healthy: Redis responded with PONG
#   1  — unhealthy: no PONG (Redis down, password wrong, or connection refused)
#
# Usage (in docker-compose.yml):
#   healthcheck:
#     test: ["CMD", "/opt/redis/healthcheck.sh"]
#     interval: 10s
#     timeout: 5s
#     retries: 5
#     start_period: 10s

REDIS_HOST="${REDIS_HOST:-localhost}"
REDIS_PORT="${REDIS_PORT:-6379}"
REDIS_PASSWORD="${REDIS_PASSWORD:-}"

if [[ -n "$REDIS_PASSWORD" ]]; then
    RESPONSE=$(redis-cli \
        --no-auth-warning \
        -h "$REDIS_HOST" \
        -p "$REDIS_PORT" \
        -a "$REDIS_PASSWORD" \
        ping 2>&1)
else
    RESPONSE=$(redis-cli \
        -h "$REDIS_HOST" \
        -p "$REDIS_PORT" \
        ping 2>&1)
fi

if [[ "$RESPONSE" == "PONG" ]]; then
    echo "HEALTHY: Redis responded PONG at ${REDIS_HOST}:${REDIS_PORT}"
    exit 0
else
    echo "UNHEALTHY: Redis returned '${RESPONSE}' (expected PONG) at ${REDIS_HOST}:${REDIS_PORT}"
    exit 1
fi
