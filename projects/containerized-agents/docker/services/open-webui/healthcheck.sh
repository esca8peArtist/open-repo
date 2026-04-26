#!/usr/bin/env bash
# healthcheck.sh — Docker health check for the Open WebUI service
# Containerized AI Agents — v1.0
#
# Open WebUI exposes a /health endpoint that returns HTTP 200 when the
# application is running and the database connection is established.
#
# Exit codes (Docker convention):
#   0  — healthy: Open WebUI returned HTTP 200
#   1  — unhealthy: non-200 response or connection refused
#
# Usage (in docker-compose.yml):
#   healthcheck:
#     test: ["CMD", "/opt/open-webui/healthcheck.sh"]
#     interval: 30s
#     timeout: 10s
#     retries: 5
#     start_period: 30s

WEBUI_HOST="${WEBUI_HOST:-localhost}"
WEBUI_PORT="${WEBUI_PORT:-3000}"
HEALTH_URL="http://${WEBUI_HOST}:${WEBUI_PORT}/health"

HTTP_STATUS=$(curl --silent --output /dev/null --write-out "%{http_code}" \
    --max-time 8 \
    --connect-timeout 3 \
    "$HEALTH_URL")

if [[ "$HTTP_STATUS" -eq 200 ]]; then
    echo "HEALTHY: Open WebUI responded HTTP 200 at ${HEALTH_URL}"
    exit 0
else
    echo "UNHEALTHY: Open WebUI returned HTTP ${HTTP_STATUS} (expected 200) at ${HEALTH_URL}"
    exit 1
fi
