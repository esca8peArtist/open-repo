#!/usr/bin/env sh
# =============================================================================
# docker/services/chromadb/healthcheck.sh — ChromaDB health check
#
# Called by Docker's HEALTHCHECK instruction.
# Performs a GET to /api/v1/heartbeat and verifies the response contains
# the expected "nanosecond heartbeat" field.
#
# Exit codes:
#   0 — healthy (heartbeat response received and valid)
#   1 — unhealthy (connection failed or unexpected response)
# =============================================================================

set -e

CHROMA_HOST="${CHROMA_HOST:-localhost}"
CHROMA_PORT="${CHROMA_PORT:-8000}"
HEARTBEAT_URL="http://${CHROMA_HOST}:${CHROMA_PORT}/api/v1/heartbeat"

# Perform the request; capture response body and HTTP status code.
# Uses curl with a short timeout to avoid hanging the healthcheck.
response=$(curl \
    --silent \
    --max-time 5 \
    --write-out "\n%{http_code}" \
    "${HEARTBEAT_URL}" 2>/dev/null) || {
    echo "healthcheck: curl failed — ChromaDB unreachable at ${HEARTBEAT_URL}"
    exit 1
}

# Split response body and HTTP status code (last line after \n separator).
http_body=$(echo "${response}" | head -n -1)
http_code=$(echo "${response}" | tail -n 1)

# Verify HTTP 200.
if [ "${http_code}" != "200" ]; then
    echo "healthcheck: unexpected HTTP ${http_code} from ${HEARTBEAT_URL}"
    exit 1
fi

# Verify the response body contains the expected heartbeat field.
# ChromaDB returns: {"nanosecond heartbeat": <unix_ns>}
if echo "${http_body}" | grep -q '"nanosecond heartbeat"'; then
    echo "healthcheck: ChromaDB is healthy (${HEARTBEAT_URL})"
    exit 0
else
    echo "healthcheck: unexpected response body — missing 'nanosecond heartbeat' field"
    echo "  Response: ${http_body}"
    exit 1
fi
