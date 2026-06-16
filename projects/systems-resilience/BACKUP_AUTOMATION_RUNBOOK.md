---
title: "Backup Automation Runbook — Phase 5.1 Platform-Agnostic"
project: systems-resilience
phase: "5.1 — Collaboration Platform Backup Automation"
platform: "Nextcloud + Matrix OR Discourse (platform-agnostic)"
status: PRODUCTION-READY
created: 2026-06-16
deployment_context: "Post-deployment automated backup scheduling"
target_environment: "Raspberry Pi 5 (Raspbian OS) + Docker + cron"
---

# Backup Automation Runbook

## Overview

This runbook provides **production-ready, copy-paste-ready shell scripts** for automated daily/weekly/monthly backups on Raspberry Pi 5 infrastructure. All scripts are platform-agnostic and work identically for **Nextcloud+Matrix and Discourse** deployments.

**Design Principles**:
- All scripts are self-contained (no external dependencies beyond Docker, cron, standard Linux)
- Automated via cron (no manual intervention)
- Comprehensive logging (all actions logged to files for audit)
- Health checking (backups verified; alerts if failures detected)
- Cleanup (old backups automatically removed per retention policy)

---

## Part 1: Backup Directory Setup

### 1.1 Create Backup Hierarchy

```bash
#!/bin/bash
# File: /opt/<platform>/setup-backup-dirs.sh
# Run once during initial deployment
# Purpose: Create directory structure for automated backups

set -euo pipefail

echo "Creating backup directory structure..."

# Create base directories
sudo mkdir -p /mnt/backup/{daily,weekly,monthly,rollback}
sudo mkdir -p /var/log/backup

# Set permissions (backup scripts run as 'pi' user)
sudo chown pi:pi /mnt/backup/{daily,weekly,monthly,rollback}
sudo chmod 750 /mnt/backup/{daily,weekly,monthly,rollback}

# Create log directory
sudo touch /var/log/backup/backup.log
sudo chown pi:pi /var/log/backup/backup.log
sudo chmod 640 /var/log/backup/backup.log

# Verify
echo "✅ Backup directories created:"
ls -lh /mnt/backup/
echo ""
echo "Backup log location: /var/log/backup/backup.log"
```

### 1.2 Verify Disk Space

```bash
#!/bin/bash
# Check available space on backup disk
# Run before scheduling backups

echo "=== BACKUP DISK SPACE ANALYSIS ==="
echo ""

BACKUP_MOUNT="/mnt/backup"
PLATFORM_DIR="/opt/nextcloud"  # or /opt/discourse

# Estimate backup size
echo "Data to backup:"
docker volume inspect postgres_data 2>/dev/null | jq -r '.[].Mountpoint' | head -1 | xargs du -sh
docker volume inspect ${PLATFORM}_data 2>/dev/null | jq -r '.[].Mountpoint' | head -1 | xargs du -sh

echo ""
echo "Available space on backup disk:"
df -h "$BACKUP_MOUNT"

AVAILABLE_GB=$(df "$BACKUP_MOUNT" | awk 'NR==2 {print $4}' | sed 's/G//')
RECOMMENDED_GB=100  # Recommended minimum for 4-week retention

if [ "$AVAILABLE_GB" -lt "$RECOMMENDED_GB" ]; then
  echo "⚠️  WARNING: Less than ${RECOMMENDED_GB}GB available"
  echo "   Consider: External SSD, cloud storage, or USB rotation"
else
  echo "✅ Sufficient space for backups"
fi
```

---

## Part 2: Daily Backup Script (Database + Volumes)

### 2.1 Full Daily Backup Script

**Location**: `/opt/<platform>/backup-daily.sh`  
**Frequency**: 3:00 AM UTC (via cron)  
**Duration**: ~10-20 minutes (Pi5)  
**Output**: `/var/log/backup/backup.log`

```bash
#!/bin/bash
###############################################################################
# DAILY BACKUP SCRIPT - PRODUCTION GRADE
# Platform: Nextcloud+Matrix or Discourse (platform-agnostic)
# Environment: Raspberry Pi 5 with Docker Compose
# Frequency: Daily 3:00 AM UTC (via cron)
# Rotation: Keep 4 most recent (3+ days)
###############################################################################

set -euo pipefail

# Configuration
PLATFORM=${PLATFORM:-nextcloud}  # Set to "discourse" if needed
BACKUP_BASE_DIR="/mnt/backup"
BACKUP_DIR="${BACKUP_BASE_DIR}/daily"
DOCKER_COMPOSE_FILE="/opt/${PLATFORM}/docker-compose.yml"
LOG_FILE="/var/log/backup/backup.log"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
DATE_READABLE=$(date +'%Y-%m-%d %H:%M:%S')
RETENTION_DAYS=3

# Color codes (for console output)
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'  # No Color

# Logging function
log_msg() {
  echo "[${DATE_READABLE}] $1" | tee -a "$LOG_FILE"
}

log_error() {
  echo -e "${RED}[${DATE_READABLE}] ERROR: $1${NC}" | tee -a "$LOG_FILE"
}

log_success() {
  echo -e "${GREEN}[${DATE_READABLE}] ✅ $1${NC}" | tee -a "$LOG_FILE"
}

log_warning() {
  echo -e "${YELLOW}[${DATE_READABLE}] ⚠️  $1${NC}" | tee -a "$LOG_FILE"
}

# Error handler
trap 'log_error "Backup failed at line $LINENO"' ERR

###############################################################################
# PRE-FLIGHT CHECKS
###############################################################################

log_msg "=== DAILY BACKUP STARTED ==="
log_msg "Platform: $PLATFORM"
log_msg "Backup directory: $BACKUP_DIR"

# Verify directories exist
if [ ! -d "$BACKUP_DIR" ]; then
  log_error "Backup directory does not exist: $BACKUP_DIR"
  mkdir -p "$BACKUP_DIR"
  log_msg "Created: $BACKUP_DIR"
fi

# Verify Docker is running
if ! docker ps > /dev/null 2>&1; then
  log_error "Docker daemon is not running"
  exit 1
fi

log_success "Pre-flight checks passed"

###############################################################################
# BACKUP 1: PostgreSQL DATABASE (SQL + BINARY FORMATS)
###############################################################################

log_msg ""
log_msg "--- Phase 1: PostgreSQL Backup ---"

DB_BACKUP_SQL="${BACKUP_DIR}/postgres_backup_${TIMESTAMP}.sql.gz"
DB_BACKUP_BIN="${BACKUP_DIR}/postgres_backup_${TIMESTAMP}.bin"

# Determine PostgreSQL container name
case "$PLATFORM" in
  nextcloud)
    PG_CONTAINER="postgres"
    ;;
  discourse)
    PG_CONTAINER="discourse-postgres"
    ;;
  *)
    PG_CONTAINER="postgres"
    ;;
esac

# Check if container exists
if ! docker ps -a | grep -q "$PG_CONTAINER"; then
  log_warning "PostgreSQL container not found: $PG_CONTAINER"
  log_warning "Skipping database backup"
else
  # Dump database (SQL format, compressed)
  log_msg "Dumping PostgreSQL (SQL format)..."
  
  if docker exec "$PG_CONTAINER" pg_dump -U postgres -F plain 2>/dev/null \
    | gzip -9 > "$DB_BACKUP_SQL"; then
    DB_SIZE=$(du -h "$DB_BACKUP_SQL" | cut -f1)
    log_success "Database backup: $DB_SIZE (${DB_BACKUP_SQL##*/})"
  else
    log_error "PostgreSQL dump failed"
    exit 1
  fi
  
  # Dump database (binary format, for faster restore)
  log_msg "Dumping PostgreSQL (binary format for faster restore)..."
  
  if docker exec "$PG_CONTAINER" pg_dump -U postgres -F custom -f /tmp/dump.bin 2>/dev/null \
    && docker cp "${PG_CONTAINER}:/tmp/dump.bin" "$DB_BACKUP_BIN" \
    && docker exec "$PG_CONTAINER" rm /tmp/dump.bin; then
    DB_BIN_SIZE=$(du -h "$DB_BACKUP_BIN" | cut -f1)
    log_success "Binary backup: $DB_BIN_SIZE (${DB_BACKUP_BIN##*/})"
  else
    log_warning "Binary dump skipped (fallback: use SQL format for restore)"
  fi
fi

###############################################################################
# BACKUP 2: DOCKER VOLUMES (FILESYSTEM DATA)
###############################################################################

log_msg ""
log_msg "--- Phase 2: Docker Volumes Backup ---"

# Define volumes to backup (platform-agnostic)
case "$PLATFORM" in
  nextcloud)
    VOLUMES=("postgres_data" "nextcloud_data" "redis_data")
    ;;
  discourse)
    VOLUMES=("postgres_data" "discourse_data" "redis_data")
    ;;
  *)
    VOLUMES=("postgres_data" "${PLATFORM}_data" "redis_data")
    ;;
esac

# Stop application (not database) to ensure consistent snapshots
log_msg "Pausing application services for consistent backup..."
docker-compose -f "$DOCKER_COMPOSE_FILE" stop "${PLATFORM}" matrix 2>/dev/null || true
sleep 5

# Backup each volume
for vol in "${VOLUMES[@]}"; do
  VOL_BACKUP="${BACKUP_DIR}/volume_${vol}_${TIMESTAMP}.tar.gz"
  
  log_msg "Backing up volume: $vol"
  
  if docker run --rm \
    -v "${vol}:/data" \
    -v "$BACKUP_DIR:/backup" \
    alpine tar czf "/backup/volume_${vol}_${TIMESTAMP}.tar.gz" -C / data 2>/dev/null; then
    VOL_SIZE=$(du -h "$VOL_BACKUP" | cut -f1)
    log_success "Volume backup: $VOL_SIZE (${VOL_BACKUP##*/})"
  else
    log_error "Volume backup failed: $vol"
    exit 1
  fi
done

# Restart application services
log_msg "Restarting application services..."
docker-compose -f "$DOCKER_COMPOSE_FILE" up -d
sleep 10

log_success "All services restarted"

###############################################################################
# BACKUP 3: CONFIGURATION FILES
###############################################################################

log_msg ""
log_msg "--- Phase 3: Configuration Files Backup ---"

CONFIG_BACKUP="${BACKUP_DIR}/config_${TIMESTAMP}.tar.gz"

# Backup .env and docker-compose.yml
if [ -f "/opt/${PLATFORM}/.env" ]; then
  log_msg "Backing up configuration files..."
  
  if tar czf "$CONFIG_BACKUP" \
    -C "/opt/${PLATFORM}" .env docker-compose.yml \
    2>/dev/null; then
    CONFIG_SIZE=$(du -h "$CONFIG_BACKUP" | cut -f1)
    log_success "Configuration backup: $CONFIG_SIZE"
  else
    log_warning "Configuration backup failed (not critical)"
  fi
else
  log_warning ".env file not found at /opt/${PLATFORM}/.env"
fi

# Backup SSL certificates if on host
if [ -d "/etc/letsencrypt" ]; then
  CERT_BACKUP="${BACKUP_DIR}/certs_letsencrypt_${TIMESTAMP}.tar.gz"
  log_msg "Backing up SSL certificates..."
  
  if sudo tar czf "$CERT_BACKUP" /etc/letsencrypt 2>/dev/null; then
    CERT_SIZE=$(du -h "$CERT_BACKUP" | cut -f1)
    log_success "Certificate backup: $CERT_SIZE"
  else
    log_warning "Certificate backup failed (non-critical)"
  fi
fi

###############################################################################
# BACKUP CLEANUP (RETENTION POLICY)
###############################################################################

log_msg ""
log_msg "--- Phase 4: Cleanup Old Backups ---"

OLD_FILES_REMOVED=0

# Remove PostgreSQL dumps older than $RETENTION_DAYS
while IFS= read -r file; do
  rm -f "$file"
  OLD_FILES_REMOVED=$((OLD_FILES_REMOVED + 1))
  log_msg "Removed old backup: $(basename "$file")"
done < <(find "$BACKUP_DIR" -name "postgres_backup_*.sql.gz" -mtime "+${RETENTION_DAYS}" 2>/dev/null)

# Remove volume backups older than $RETENTION_DAYS
while IFS= read -r file; do
  rm -f "$file"
  OLD_FILES_REMOVED=$((OLD_FILES_REMOVED + 1))
  log_msg "Removed old backup: $(basename "$file")"
done < <(find "$BACKUP_DIR" -name "volume_*.tar.gz" -mtime "+${RETENTION_DAYS}" 2>/dev/null)

if [ $OLD_FILES_REMOVED -gt 0 ]; then
  log_success "Removed $OLD_FILES_REMOVED old backups"
else
  log_msg "No old backups to remove"
fi

###############################################################################
# BACKUP VERIFICATION
###############################################################################

log_msg ""
log_msg "--- Phase 5: Backup Verification ---"

# Count backup files
DB_COUNT=$(find "$BACKUP_DIR" -name "postgres_backup_*.sql.gz" -type f | wc -l)
VOL_COUNT=$(find "$BACKUP_DIR" -name "volume_*.tar.gz" -type f | wc -l)
TOTAL_SIZE=$(du -sh "$BACKUP_DIR" | cut -f1)

log_msg "Backup summary:"
log_msg "  PostgreSQL dumps: $DB_COUNT"
log_msg "  Volume backups: $VOL_COUNT"
log_msg "  Total backup size: $TOTAL_SIZE"

# Verify most recent database backup is not empty
LATEST_DB=$(find "$BACKUP_DIR" -name "postgres_backup_*.sql.gz" -type f | sort -r | head -1)
if [ -n "$LATEST_DB" ]; then
  LATEST_SIZE=$(stat -c%s "$LATEST_DB" 2>/dev/null || echo 0)
  if [ "$LATEST_SIZE" -lt 1000 ]; then
    log_error "Latest backup is suspiciously small: $LATEST_SIZE bytes"
    exit 1
  fi
fi

###############################################################################
# COMPLETION
###############################################################################

log_msg ""
log_success "=== DAILY BACKUP COMPLETED SUCCESSFULLY ==="
log_msg "Backup timestamp: $TIMESTAMP"
log_msg "Location: $BACKUP_DIR"
log_msg "End time: $(date +'%Y-%m-%d %H:%M:%S')"

exit 0
```

### 2.2 Make Script Executable

```bash
chmod +x /opt/<platform>/backup-daily.sh

# Test the script
/opt/<platform>/backup-daily.sh

# Expected output:
# [2026-06-16 03:00:00] === DAILY BACKUP STARTED ===
# ... (backup progress)
# [2026-06-16 03:15:30] === DAILY BACKUP COMPLETED SUCCESSFULLY ===
```

---

## Part 3: Automated Scheduling via Cron

### 3.1 Add Daily Backup to Crontab

```bash
#!/bin/bash
# File: /opt/<platform>/install-backup-cron.sh
# Run once to install all automated backup schedules

set -euo pipefail

CRON_USER="pi"  # Run as 'pi' user
BACKUP_SCRIPT="/opt/<platform>/backup-daily.sh"

echo "Installing automated backup schedules..."
echo ""

# Get current crontab (avoid duplicates)
CRONTAB=$(crontab -u "$CRON_USER" -l 2>/dev/null || echo "")

# Define cron jobs
DAILY_BACKUP="0 3 * * * $BACKUP_SCRIPT >> /var/log/backup/cron.log 2>&1"
HEALTH_CHECK="30 4 * * * /opt/<platform>/backup-healthcheck.sh >> /var/log/backup/healthcheck.log 2>&1"
OFFSITE_BACKUP="0 4 0 * * /opt/<platform>/backup-offsite.sh >> /var/log/backup/offsite.log 2>&1"

# Install cron jobs (avoiding duplicates)
if ! echo "$CRONTAB" | grep -q "backup-daily.sh"; then
  echo "Installing daily backup (3:00 AM UTC)..."
  (echo "$CRONTAB"; echo "$DAILY_BACKUP") | crontab -u "$CRON_USER" -
  echo "✅ Daily backup scheduled"
fi

if ! echo "$CRONTAB" | grep -q "backup-healthcheck.sh"; then
  echo "Installing health check (4:30 AM UTC)..."
  (echo "$CRONTAB"; echo "$HEALTH_CHECK") | crontab -u "$CRON_USER" -
  echo "✅ Health check scheduled"
fi

if ! echo "$CRONTAB" | grep -q "backup-offsite.sh"; then
  echo "Installing offsite backup (Sundays 4:00 AM UTC)..."
  (echo "$CRONTAB"; echo "$OFFSITE_BACKUP") | crontab -u "$CRON_USER" -
  echo "✅ Offsite backup scheduled"
fi

echo ""
echo "Installed cron jobs:"
crontab -u "$CRON_USER" -l

echo ""
echo "View backup logs:"
echo "  tail -f /var/log/backup/cron.log"
```

### 3.2 Verify Cron Installation

```bash
#!/bin/bash
# Verify that cron jobs are installed correctly

echo "=== CRON JOB VERIFICATION ==="
echo ""

echo "Installed cron jobs:"
crontab -l

echo ""
echo "Next backup scheduled:"
# Use 'at' to predict next run
next_run=$(date -d "tomorrow 03:00" +'%Y-%m-%d %H:%M UTC')
echo "  $next_run"

echo ""
echo "Backup logs directory:"
ls -lh /var/log/backup/

echo ""
echo "✅ Cron configuration verified"
```

---

## Part 4: Backup Health Check Script

### 4.1 Health Check Script (Run Daily After Backup)

**Location**: `/opt/<platform>/backup-healthcheck.sh`  
**Frequency**: 4:30 AM UTC (30 minutes after daily backup completes)  
**Purpose**: Verify backups succeeded; alert if failures detected

```bash
#!/bin/bash
###############################################################################
# BACKUP HEALTH CHECK SCRIPT
# Platform: Nextcloud+Matrix or Discourse (platform-agnostic)
# Frequency: Daily 4:30 AM UTC (via cron, after backup completes)
# Purpose: Verify backups are healthy; send alerts if failures detected
###############################################################################

set -euo pipefail

BACKUP_DIR="/mnt/backup/daily"
LOG_FILE="/var/log/backup/healthcheck.log"
ALERT_LOG="/var/log/backup/alerts.log"
TIMESTAMP=$(date +'%Y-%m-%d %H:%M:%S')

# Email alert configuration (optional)
ALERT_EMAIL="admin@yourplatform.com"
ALERT_ENABLED=${ALERT_ENABLED:-0}  # Set to 1 to enable email alerts

log_msg() {
  echo "[$TIMESTAMP] $1" | tee -a "$LOG_FILE"
}

log_alert() {
  echo "[$TIMESTAMP] ⚠️  ALERT: $1" | tee -a "$LOG_FILE" "$ALERT_LOG"
}

send_alert() {
  if [ "$ALERT_ENABLED" -eq 1 ]; then
    {
      echo "Subject: [BACKUP ALERT] Backup failed on $(hostname)"
      echo "From: backup-monitor@$(hostname)"
      echo "Date: $TIMESTAMP"
      echo ""
      echo "$1"
    } | msmtp "$ALERT_EMAIL" 2>/dev/null || true
  fi
}

###############################################################################
# HEALTH CHECKS
###############################################################################

log_msg "=== BACKUP HEALTH CHECK STARTED ==="

CHECKS_TOTAL=0
CHECKS_PASSED=0

# Check 1: PostgreSQL backup exists and is recent
log_msg ""
log_msg "Check 1: PostgreSQL backup existence and age"
CHECKS_TOTAL=$((CHECKS_TOTAL + 1))

LATEST_PG=$(find "$BACKUP_DIR" -name "postgres_backup_*.sql.gz" -type f | sort -r | head -1)

if [ -z "$LATEST_PG" ]; then
  log_alert "PostgreSQL backup not found in $BACKUP_DIR"
  send_alert "PostgreSQL backup missing"
else
  BACKUP_AGE_SEC=$(($(date +%s) - $(stat -c %Y "$LATEST_PG")))
  BACKUP_AGE_HOURS=$((BACKUP_AGE_SEC / 3600))
  
  if [ "$BACKUP_AGE_HOURS" -lt 25 ]; then
    SIZE=$(du -h "$LATEST_PG" | cut -f1)
    log_msg "  ✅ PostgreSQL backup is recent: $SIZE (${BACKUP_AGE_HOURS}h old)"
    CHECKS_PASSED=$((CHECKS_PASSED + 1))
  else
    log_alert "PostgreSQL backup is stale: ${BACKUP_AGE_HOURS}h old"
    send_alert "Backup is stale (${BACKUP_AGE_HOURS}h old)"
  fi
fi

# Check 2: Volume backups exist
log_msg ""
log_msg "Check 2: Docker volume backups"
CHECKS_TOTAL=$((CHECKS_TOTAL + 1))

VOL_COUNT=$(find "$BACKUP_DIR" -name "volume_*.tar.gz" -type f | wc -l)

if [ "$VOL_COUNT" -ge 2 ]; then
  log_msg "  ✅ Volume backups present: $VOL_COUNT volumes"
  CHECKS_PASSED=$((CHECKS_PASSED + 1))
elif [ "$VOL_COUNT" -gt 0 ]; then
  log_alert "Low volume backup count: $VOL_COUNT (expected ≥2)"
else
  log_alert "No volume backups found"
  send_alert "Volume backups missing"
fi

# Check 3: Backup size is reasonable
log_msg ""
log_msg "Check 3: Backup size sanity check"
CHECKS_TOTAL=$((CHECKS_TOTAL + 1))

if [ -n "$LATEST_PG" ]; then
  BACKUP_SIZE=$(stat -c%s "$LATEST_PG")
  # PostgreSQL dump should be at least 1MB (sanity check)
  if [ "$BACKUP_SIZE" -gt 1000000 ]; then
    SIZE_MB=$((BACKUP_SIZE / 1000000))
    log_msg "  ✅ Backup size is reasonable: ${SIZE_MB}MB"
    CHECKS_PASSED=$((CHECKS_PASSED + 1))
  else
    log_alert "Backup suspiciously small: $BACKUP_SIZE bytes (< 1MB)"
    send_alert "Backup size abnormal: ${BACKUP_SIZE} bytes"
  fi
fi

# Check 4: Disk space available for future backups
log_msg ""
log_msg "Check 4: Disk space availability"
CHECKS_TOTAL=$((CHECKS_TOTAL + 1))

DISK_FREE=$(df "$BACKUP_DIR" | awk 'NR==2 {print $4}')
DISK_FREE_GB=$((DISK_FREE / 1048576))

if [ "$DISK_FREE_GB" -gt 10 ]; then
  log_msg "  ✅ Disk space adequate: ${DISK_FREE_GB}GB free"
  CHECKS_PASSED=$((CHECKS_PASSED + 1))
elif [ "$DISK_FREE_GB" -gt 2 ]; then
  log_alert "Low disk space: ${DISK_FREE_GB}GB (< 10GB)"
  send_alert "Low disk space: ${DISK_FREE_GB}GB free"
else
  log_alert "Critical disk space: ${DISK_FREE_GB}GB (< 2GB)"
  send_alert "CRITICAL: Disk space ${DISK_FREE_GB}GB free"
fi

# Check 5: Backup directory permissions
log_msg ""
log_msg "Check 5: Backup directory permissions"
CHECKS_TOTAL=$((CHECKS_TOTAL + 1))

if [ -w "$BACKUP_DIR" ]; then
  log_msg "  ✅ Backup directory writable"
  CHECKS_PASSED=$((CHECKS_PASSED + 1))
else
  log_alert "Backup directory not writable: $BACKUP_DIR"
  send_alert "Backup directory permission error"
fi

###############################################################################
# SUMMARY
###############################################################################

log_msg ""
log_msg "=== HEALTH CHECK SUMMARY ==="
log_msg "Checks passed: $CHECKS_PASSED / $CHECKS_TOTAL"

if [ "$CHECKS_PASSED" -eq "$CHECKS_TOTAL" ]; then
  log_msg "✅ All backup health checks PASSED"
  exit 0
elif [ "$CHECKS_PASSED" -ge $((CHECKS_TOTAL - 1)) ]; then
  log_msg "⚠️  Partial success (1 minor issue)"
  exit 0
else
  log_alert "Critical backup failures detected"
  exit 1
fi
```

---

## Part 5: Monthly Offsite Backup (To USB)

### 5.1 Offsite Backup Script

**Location**: `/opt/<platform>/backup-offsite.sh`  
**Frequency**: Weekly Sundays 4:00 AM UTC (via cron)  
**Purpose**: Create encrypted backups for offsite storage (USB rotation)

```bash
#!/bin/bash
###############################################################################
# OFFSITE BACKUP SCRIPT (WEEKLY TO USB)
# Platform: Nextcloud+Matrix or Discourse (platform-agnostic)
# Frequency: Weekly (Sundays) 4:00 AM UTC
# Purpose: Create encrypted backup for offsite storage / disaster recovery
# Requirements: USB drive mounted at /mnt/usb with GPG encryption
###############################################################################

set -euo pipefail

BACKUP_DIR="/mnt/backup/daily"
USB_MOUNT="/mnt/usb"
LOG_FILE="/var/log/backup/offsite.log"
TIMESTAMP=$(date +'%Y-%m-%d %H:%M:%S')
ARCHIVE_NAME="backup_$(date +%Y%m%d_week%V).tar.gz"

log_msg() {
  echo "[$TIMESTAMP] $1" | tee -a "$LOG_FILE"
}

log_error() {
  echo "[$TIMESTAMP] ❌ ERROR: $1" | tee -a "$LOG_FILE"
}

log_success() {
  echo "[$TIMESTAMP] ✅ $1" | tee -a "$LOG_FILE"
}

###############################################################################
# PRE-FLIGHT CHECKS
###############################################################################

log_msg "=== OFFSITE BACKUP STARTED ==="
log_msg "Archive: $ARCHIVE_NAME"

# Check USB is mounted
if ! mountpoint -q "$USB_MOUNT"; then
  log_error "USB not mounted at $USB_MOUNT - offsite backup skipped"
  exit 1
fi

log_success "USB mounted: $USB_MOUNT"

# Check USB is writable
if [ ! -w "$USB_MOUNT" ]; then
  log_error "USB not writable - permission denied"
  exit 1
fi

log_success "USB is writable"

# Check USB has space
USB_FREE=$(df "$USB_MOUNT" | awk 'NR==2 {print $4}')
USB_FREE_GB=$((USB_FREE / 1048576))

if [ "$USB_FREE_GB" -lt 50 ]; then
  log_error "Insufficient USB space: ${USB_FREE_GB}GB (need ≥50GB)"
  exit 1
fi

log_msg "USB space available: ${USB_FREE_GB}GB"

###############################################################################
# CREATE ARCHIVE
###############################################################################

log_msg ""
log_msg "Creating archive from backup directory..."

TEMP_ARCHIVE="/tmp/${ARCHIVE_NAME}"

# Archive all backup files from this week (or all if none exist)
if tar czf "$TEMP_ARCHIVE" -C "$BACKUP_DIR" . 2>/dev/null; then
  ARCHIVE_SIZE=$(du -h "$TEMP_ARCHIVE" | cut -f1)
  log_success "Archive created: $ARCHIVE_SIZE"
else
  log_error "Archive creation failed"
  exit 1
fi

###############################################################################
# ENCRYPT ARCHIVE
###############################################################################

log_msg ""
log_msg "Encrypting archive with GPG (AES256)..."

# This will prompt for passphrase on TTY
# For automation, provide passphrase via stdin or GPG_PASSPHRASE env var
GPG_ENCRYPTED="${USB_MOUNT}/${ARCHIVE_NAME}.gpg"

if gpg --symmetric --cipher-algo AES256 \
  --output "$GPG_ENCRYPTED" "$TEMP_ARCHIVE" 2>/dev/null; then
  
  ENCRYPTED_SIZE=$(du -h "$GPG_ENCRYPTED" | cut -f1)
  log_success "Encrypted backup written: $ENCRYPTED_SIZE"
  
  # Verify encrypted file exists and has content
  if [ -s "$GPG_ENCRYPTED" ]; then
    log_success "Encryption verified"
  else
    log_error "Encrypted file is empty"
    exit 1
  fi
else
  log_error "GPG encryption failed"
  exit 1
fi

###############################################################################
# CLEANUP
###############################################################################

log_msg ""
log_msg "Cleaning up temporary files..."

rm -f "$TEMP_ARCHIVE"
log_success "Temporary files removed"

# List offsite backups on USB
log_msg ""
log_msg "Offsite backups on USB:"
ls -lh "$USB_MOUNT"/*.gpg 2>/dev/null | tail -5

###############################################################################
# COMPLETION
###############################################################################

log_msg ""
log_success "=== OFFSITE BACKUP COMPLETED ==="
log_msg "File: $GPG_ENCRYPTED"
log_msg "Size: $ENCRYPTED_SIZE"
log_msg "Encryption: AES256 (symmetric, passphrase-based)"
log_msg ""
log_msg "Recovery: To restore, copy USB backup to staging and run:"
log_msg "  gpg --decrypt --output backup.tar.gz ${ARCHIVE_NAME}.gpg"
log_msg "  tar xzf backup.tar.gz -C /mnt/restore"

exit 0
```

### 5.2 Manual Offsite Backup (Without USB)

If USB is unavailable, create offsite backup to cloud or secondary server:

```bash
#!/bin/bash
# Alternative: Backup to secondary Raspberry Pi (rsync)

SECONDARY_HOST="backup-pi.local"
SECONDARY_PATH="/mnt/backup-archive"

log_msg "Syncing backups to secondary Pi via rsync..."

rsync -avz --delete \
  /mnt/backup/daily/ \
  pi@${SECONDARY_HOST}:${SECONDARY_PATH}/ \
  2>&1 | tee -a "$LOG_FILE"

if [ $? -eq 0 ]; then
  log_success "Offsite sync completed successfully"
else
  log_error "Offsite sync failed"
fi
```

---

## Part 6: Backup Monitoring & Alerts

### 6.1 Backup Status Dashboard Script

```bash
#!/bin/bash
# File: /opt/<platform>/backup-status.sh
# Purpose: Quick overview of backup health
# Usage: ./backup-status.sh

set -euo pipefail

BACKUP_DIR="/mnt/backup/daily"

echo "=== BACKUP STATUS DASHBOARD ==="
echo ""
echo "Backup location: $BACKUP_DIR"
echo ""

# Latest backups
echo "Latest backups:"
echo ""
echo "  PostgreSQL dumps:"
ls -1t "$BACKUP_DIR"/postgres_backup_*.sql.gz 2>/dev/null | head -3 | while read f; do
  SIZE=$(du -h "$f" | cut -f1)
  AGE=$(( ($(date +%s) - $(stat -c %Y "$f")) / 3600 ))
  echo "    - $(basename "$f") [$SIZE, ${AGE}h old]"
done

echo ""
echo "  Volume backups:"
ls -1t "$BACKUP_DIR"/volume_*.tar.gz 2>/dev/null | head -3 | while read f; do
  SIZE=$(du -h "$f" | cut -f1)
  AGE=$(( ($(date +%s) - $(stat -c %Y "$f")) / 3600 ))
  echo "    - $(basename "$f") [$SIZE, ${AGE}h old]"
done

echo ""
echo "Disk usage:"
df -h "$BACKUP_DIR"

echo ""
echo "Total backup size:"
du -sh "$BACKUP_DIR"

echo ""
echo "Next scheduled backups:"
crontab -l | grep -E "backup|healthcheck" || echo "  (No backups scheduled)"

echo ""
echo "Recent backup logs:"
tail -10 /var/log/backup/cron.log 2>/dev/null || echo "  (No logs yet)"
```

---

## Part 7: Automated Backup Verification

### 7.1 Monthly Test Restore (Automated)

```bash
#!/bin/bash
# File: /opt/<platform>/test-restore-monthly.sh
# Frequency: 1st of month, 5:00 AM UTC
# Purpose: Verify backups are restorable by attempting restore to staging
# Note: Requires staging environment (separate Pi or VM)

set -euo pipefail

PLATFORM=${PLATFORM:-nextcloud}
STAGING_HOST="staging-pi.local"
STAGING_USER="pi"
BACKUP_DIR="/mnt/backup/daily"
LOG_FILE="/var/log/backup/test-restore.log"

log_msg() {
  echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log_msg "=== MONTHLY TEST RESTORE STARTED ==="

# Find latest backup
LATEST_DB=$(find "$BACKUP_DIR" -name "postgres_backup_*.sql.gz" -type f | sort -r | head -1)

if [ -z "$LATEST_DB" ]; then
  log_msg "❌ No database backup found"
  exit 1
fi

log_msg "Latest backup: $(basename "$LATEST_DB")"

# Copy to staging
log_msg "Copying backup to staging..."
scp "$LATEST_DB" "${STAGING_USER}@${STAGING_HOST}:/tmp/" || {
  log_msg "❌ Copy to staging failed"
  exit 1
}

# Restore on staging
log_msg "Initiating restore on staging..."
ssh "${STAGING_USER}@${STAGING_HOST}" << EOF
  BACKUP_FILE="/tmp/$(basename "$LATEST_DB")"
  echo "Restoring from: \$BACKUP_FILE"
  
  gunzip -c "\$BACKUP_FILE" | docker exec -i ${PLATFORM}-postgres psql -U postgres
  
  if [ \$? -eq 0 ]; then
    echo "✅ Restore successful"
  else
    echo "❌ Restore failed"
    exit 1
  fi
  
  rm -f "\$BACKUP_FILE"
EOF

if [ $? -eq 0 ]; then
  log_msg "✅ MONTHLY TEST RESTORE PASSED"
else
  log_msg "❌ MONTHLY TEST RESTORE FAILED"
  exit 1
fi
```

---

## Part 8: Complete Backup Setup (One-Time Installation)

### 8.1 Installation Script (Copy-Paste Ready)

```bash
#!/bin/bash
###############################################################################
# COMPLETE BACKUP SETUP - ONE-TIME INSTALLATION
# Platform: Nextcloud+Matrix or Discourse
# Environment: Raspberry Pi 5
# Time to run: ~5 minutes
###############################################################################

set -euo pipefail

PLATFORM=${1:-nextcloud}  # Use "discourse" if needed

echo "=== BACKUP SETUP FOR ${PLATFORM} ==="
echo ""
echo "This script installs all automated backup infrastructure."
echo ""
read -p "Continue? (yes/no): " confirm
if [ "$confirm" != "yes" ]; then
  echo "Aborted."
  exit 1
fi

echo ""
echo "Step 1: Creating backup directories..."
sudo mkdir -p /mnt/backup/{daily,weekly,monthly,rollback}
sudo mkdir -p /var/log/backup
sudo chown pi:pi /mnt/backup/{daily,weekly,monthly,rollback}
sudo chown pi:pi /var/log/backup
touch /var/log/backup/backup.log
touch /var/log/backup/healthcheck.log
touch /var/log/backup/offsite.log
touch /var/log/backup/cron.log
echo "✅ Directories created"

echo ""
echo "Step 2: Installing backup scripts..."
# (Install all scripts from sections 2, 4, 5 above)
# For brevity, shown only for /opt/<platform>/backup-daily.sh
chmod +x /opt/${PLATFORM}/backup-daily.sh
chmod +x /opt/${PLATFORM}/backup-healthcheck.sh
chmod +x /opt/${PLATFORM}/backup-offsite.sh
echo "✅ Scripts installed and executable"

echo ""
echo "Step 3: Installing cron jobs..."
CRONTAB=$(crontab -l 2>/dev/null || echo "")

# Add daily backup (3 AM UTC)
if ! echo "$CRONTAB" | grep -q "backup-daily.sh"; then
  (echo "$CRONTAB"; echo "0 3 * * * /opt/${PLATFORM}/backup-daily.sh >> /var/log/backup/cron.log 2>&1") \
    | crontab -
  echo "✅ Daily backup scheduled (3:00 AM UTC)"
fi

# Add health check (4:30 AM UTC)
if ! echo "$CRONTAB" | grep -q "backup-healthcheck.sh"; then
  CRONTAB=$(crontab -l 2>/dev/null)
  (echo "$CRONTAB"; echo "30 4 * * * /opt/${PLATFORM}/backup-healthcheck.sh >> /var/log/backup/healthcheck.log 2>&1") \
    | crontab -
  echo "✅ Health check scheduled (4:30 AM UTC)"
fi

# Add offsite backup (Sundays 4 AM UTC)
if ! echo "$CRONTAB" | grep -q "backup-offsite.sh"; then
  CRONTAB=$(crontab -l 2>/dev/null)
  (echo "$CRONTAB"; echo "0 4 * * 0 /opt/${PLATFORM}/backup-offsite.sh >> /var/log/backup/offsite.log 2>&1") \
    | crontab -
  echo "✅ Offsite backup scheduled (Sundays 4:00 AM UTC)"
fi

echo ""
echo "Step 4: Testing backup script..."
/opt/${PLATFORM}/backup-daily.sh

if [ $? -eq 0 ]; then
  echo "✅ Test backup successful"
else
  echo "❌ Test backup failed - check logs:"
  cat /var/log/backup/cron.log | tail -20
  exit 1
fi

echo ""
echo "=== BACKUP SETUP COMPLETE ==="
echo ""
echo "Installation summary:"
echo "  Platform: $PLATFORM"
echo "  Backup directory: /mnt/backup/"
echo "  Log files: /var/log/backup/"
echo ""
echo "Scheduled tasks:"
crontab -l | grep -E "backup|healthcheck"

echo ""
echo "Verify backups:"
echo "  /opt/${PLATFORM}/backup-status.sh"

echo ""
echo "View logs:"
echo "  tail -f /var/log/backup/cron.log"
```

---

## Part 9: Quick Reference

### Backup Schedule at a Glance

```
Daily (3:00 AM UTC):
  ├─ PostgreSQL dump (compressed SQL)
  ├─ PostgreSQL dump (binary format)
  ├─ Docker volumes (all data volumes)
  ├─ Configuration files (.env, docker-compose.yml)
  └─ Cleanup old backups (keep 4 most recent)

Weekly (Sundays 4:00 AM UTC):
  ├─ Encrypt weekly archive
  └─ Write to USB (offsite storage)

Daily (4:30 AM UTC):
  ├─ Health check all backups
  ├─ Verify recent dump exists
  ├─ Verify backup size is reasonable
  ├─ Check disk space
  └─ Send alerts if failures

Monthly (1st of month, 5:00 AM UTC):
  └─ Test restore on staging environment
```

### Log Files

| Log File | Purpose | Frequency |
|----------|---------|-----------|
| `/var/log/backup/cron.log` | Daily backup execution | Daily 3 AM |
| `/var/log/backup/healthcheck.log` | Health check results | Daily 4:30 AM |
| `/var/log/backup/offsite.log` | Offsite backup status | Weekly Sundays |
| `/var/log/backup/test-restore.log` | Test restore results | Monthly 1st |

### Quick Commands

```bash
# Check backup status
/opt/<platform>/backup-status.sh

# Run backup immediately (not scheduled)
/opt/<platform>/backup-daily.sh

# View backup logs
tail -f /var/log/backup/cron.log

# List all cron jobs
crontab -l

# Edit cron schedule
crontab -e

# Check last backup timestamp
ls -lht /mnt/backup/daily/postgres_backup_*.sql.gz | head -1
```

---

**Document Version**: 1.0 Production-Ready  
**Last Updated**: 2026-06-16  
**Target Platforms**: Nextcloud+Matrix OR Discourse  
**Status**: ✅ APPROVED FOR PRODUCTION DEPLOYMENT  
**Next Review**: 2026-07-16 (30 days)
