#!/usr/bin/env bash
# healthcheck.sh — Docker health check for the Ollama service
# Containerized AI Agents — v1.0
#
# Exit codes (Docker convention):
#   0  — healthy: Ollama is running AND at least one model is available
#   1  — unhealthy: Ollama is not reachable OR no models are loaded
#
# Usage (in docker-compose.yml):
#   healthcheck:
#     test: ["CMD", "/opt/ollama/healthcheck.sh"]
#     interval: 30s
#     timeout: 10s
#     retries: 3
#     start_period: 60s

OLLAMA_HOST="${OLLAMA_HOST:-http://localhost:11434}"
TIMEOUT=8   # curl connect+read timeout in seconds

# ---------------------------------------------------------------------------
# 1. Check that the Ollama API endpoint is reachable
# ---------------------------------------------------------------------------
response=$(curl -sf --max-time "${TIMEOUT}" "${OLLAMA_HOST}/api/tags" 2>/dev/null)
if [[ $? -ne 0 || -z "$response" ]]; then
  echo "UNHEALTHY: Ollama API not reachable at ${OLLAMA_HOST}"
  exit 1
fi

# ---------------------------------------------------------------------------
# 2. Check that at least one model is present / loaded
# ---------------------------------------------------------------------------
# The /api/tags response is JSON: {"models": [ {...}, ... ]}
# We check that the models array is non-empty using basic shell + python/grep.
if command -v python3 &>/dev/null; then
  model_count=$(python3 -c "
import sys, json
try:
    data = json.loads(sys.stdin.read())
    print(len(data.get('models', [])))
except Exception:
    print(0)
" <<< "$response")
else
  # Fallback: count occurrences of '"name"' key inside the models array
  model_count=$(echo "$response" | grep -o '"name"' | wc -l | tr -d ' ')
fi

if [[ -z "$model_count" || "$model_count" -lt 1 ]]; then
  echo "UNHEALTHY: Ollama is running but no models are available"
  exit 1
fi

echo "HEALTHY: Ollama is running with ${model_count} model(s) available"
exit 0
