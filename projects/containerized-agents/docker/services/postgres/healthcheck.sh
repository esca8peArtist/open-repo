#!/usr/bin/env bash
# healthcheck.sh — Docker health check for the PostgreSQL service
# Containerized AI Agents — v1.0
#
# Exit codes (Docker convention):
#   0  — healthy: PostgreSQL is accepting connections
#   1  — unhealthy: PostgreSQL is not reachable
#
# Usage (in docker-compose.yml):
#   healthcheck:
#     test: ["CMD", "/opt/postgres/healthcheck.sh"]
#     interval: 10s
#     timeout: 5s
#     retries: 5
#     start_period: 30s

POSTGRES_HOST="${POSTGRES_HOST:-localhost}"
POSTGRES_PORT="${POSTGRES_PORT:-5432}"
POSTGRES_USER="${POSTGRES_USER:-agents}"
POSTGRES_DB="${POSTGRES_DB:-agents}"

# pg_isready returns:
#   0 — server is accepting connections
#   1 — server is rejecting connections
#   2 — no response (server is not running / unreachable)
pg_isready \
  --host="$POSTGRES_HOST" \
  --port="$POSTGRES_PORT" \
  --username="$POSTGRES_USER" \
  --dbname="$POSTGRES_DB" \
  --quiet

STATUS=$?

if [[ $STATUS -eq 0 ]]; then
  echo "HEALTHY: PostgreSQL is accepting connections at ${POSTGRES_HOST}:${POSTGRES_PORT}"
  exit 0
else
  echo "UNHEALTHY: PostgreSQL is not ready (pg_isready exit code: ${STATUS})"
  exit 1
fi
