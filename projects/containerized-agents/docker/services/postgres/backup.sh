#!/usr/bin/env bash
# backup.sh — PostgreSQL backup for Containerized AI Agents
# Containerized AI Agents — v1.0
#
# Creates a compressed pg_dump snapshot and retains the last 7 backups.
# Can be run manually or scheduled via cron / Docker's restart policy.
#
# Usage:
#   ./backup.sh
#   ./backup.sh --backup-dir /custom/path --keep 14
#
# Cron example (daily at 02:00):
#   0 2 * * * /opt/postgres/backup.sh >> /var/log/postgres-backup.log 2>&1
#
# Environment variables (override defaults):
#   POSTGRES_HOST     — default: localhost
#   POSTGRES_PORT     — default: 5432
#   POSTGRES_DB       — default: agents
#   POSTGRES_USER     — default: agents
#   PGPASSWORD        — set to avoid password prompt (or use .pgpass)
#   BACKUP_DIR        — default: /backups/postgres
#   BACKUP_KEEP       — default: 7  (number of backups to retain)

set -euo pipefail

# ---------------------------------------------------------------------------
# Defaults (override via environment or --flags)
# ---------------------------------------------------------------------------
POSTGRES_HOST="${POSTGRES_HOST:-localhost}"
POSTGRES_PORT="${POSTGRES_PORT:-5432}"
POSTGRES_DB="${POSTGRES_DB:-agents}"
POSTGRES_USER="${POSTGRES_USER:-agents}"
BACKUP_DIR="${BACKUP_DIR:-/backups/postgres}"
BACKUP_KEEP="${BACKUP_KEEP:-7}"

# ---------------------------------------------------------------------------
# Colour helpers
# ---------------------------------------------------------------------------
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
BLUE='\033[0;34m'; RESET='\033[0m'

info()    { echo -e "${BLUE}[INFO]${RESET}  $(date '+%Y-%m-%d %H:%M:%S') $*"; }
success() { echo -e "${GREEN}[OK]${RESET}    $(date '+%Y-%m-%d %H:%M:%S') $*"; }
warn()    { echo -e "${YELLOW}[WARN]${RESET}  $(date '+%Y-%m-%d %H:%M:%S') $*"; }
error()   { echo -e "${RED}[ERROR]${RESET} $(date '+%Y-%m-%d %H:%M:%S') $*" >&2; }

# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------
while [[ $# -gt 0 ]]; do
  case "$1" in
    --backup-dir) BACKUP_DIR="$2"; shift 2 ;;
    --keep)       BACKUP_KEEP="$2"; shift 2 ;;
    --db)         POSTGRES_DB="$2"; shift 2 ;;
    --host)       POSTGRES_HOST="$2"; shift 2 ;;
    --port)       POSTGRES_PORT="$2"; shift 2 ;;
    --user)       POSTGRES_USER="$2"; shift 2 ;;
    -h|--help)
      echo "Usage: $(basename "$0") [--backup-dir DIR] [--keep N] [--db DB] [--host H] [--port P] [--user U]"
      exit 0 ;;
    *) error "Unknown argument: $1"; exit 1 ;;
  esac
done

# ---------------------------------------------------------------------------
# Dependency check
# ---------------------------------------------------------------------------
if ! command -v pg_dump &>/dev/null; then
  error "'pg_dump' not found in PATH. Install postgresql-client."
  exit 1
fi

if ! command -v gzip &>/dev/null; then
  error "'gzip' not found in PATH."
  exit 1
fi

# ---------------------------------------------------------------------------
# Prepare backup directory
# ---------------------------------------------------------------------------
mkdir -p "$BACKUP_DIR"

# ---------------------------------------------------------------------------
# Generate filename
# ---------------------------------------------------------------------------
TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
BACKUP_FILE="${BACKUP_DIR}/${POSTGRES_DB}_${TIMESTAMP}.sql.gz"

info "Starting backup"
info "  Database : ${POSTGRES_DB} @ ${POSTGRES_HOST}:${POSTGRES_PORT}"
info "  Output   : ${BACKUP_FILE}"
info "  Retention: last ${BACKUP_KEEP} backups"

# ---------------------------------------------------------------------------
# Run pg_dump and compress
# ---------------------------------------------------------------------------
pg_dump \
  --host="$POSTGRES_HOST" \
  --port="$POSTGRES_PORT" \
  --username="$POSTGRES_USER" \
  --no-password \
  --format=plain \
  --encoding=UTF8 \
  --no-owner \
  --no-acl \
  "$POSTGRES_DB" \
  | gzip --best > "$BACKUP_FILE"

if [[ ! -s "$BACKUP_FILE" ]]; then
  error "Backup file is empty or was not created: ${BACKUP_FILE}"
  rm -f "$BACKUP_FILE"
  exit 1
fi

BACKUP_SIZE=$(du -sh "$BACKUP_FILE" | cut -f1)
success "Backup complete: ${BACKUP_FILE} (${BACKUP_SIZE})"

# ---------------------------------------------------------------------------
# Pruning — keep the last N backups
# ---------------------------------------------------------------------------
info "Pruning old backups (keeping last ${BACKUP_KEEP})..."

# List all backups for this database, sorted oldest first
mapfile -t OLD_BACKUPS < <(
  ls -1t "${BACKUP_DIR}/${POSTGRES_DB}_"*.sql.gz 2>/dev/null | tail -n +"$((BACKUP_KEEP + 1))"
)

if [[ ${#OLD_BACKUPS[@]} -eq 0 ]]; then
  info "No old backups to prune"
else
  for old in "${OLD_BACKUPS[@]}"; do
    rm -f "$old"
    warn "Removed old backup: $(basename "$old")"
  done
  success "Pruned ${#OLD_BACKUPS[@]} old backup(s)"
fi

# ---------------------------------------------------------------------------
# Final listing
# ---------------------------------------------------------------------------
info "Current backups in ${BACKUP_DIR}:"
ls -lh "${BACKUP_DIR}/${POSTGRES_DB}_"*.sql.gz 2>/dev/null | awk '{print "  " $5 "  " $9}' || true

success "Backup job finished successfully"
exit 0
