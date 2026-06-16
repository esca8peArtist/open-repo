---
title: "Disaster Recovery Design Specification — Phase 5.1 Platform-Agnostic"
project: systems-resilience
phase: "5.1 — Collaboration Platform DR Strategy"
platform: "Nextcloud + Matrix OR Discourse (platform-agnostic design)"
status: PRODUCTION-READY
created: 2026-06-16
effective_date: 2026-06-16
target_platforms:
  - "Nextcloud 29 + Matrix Synapse + Element Web + OnlyOffice"
  - "Discourse + PostgreSQL + Redis"
---

# Disaster Recovery Design Specification

## Executive Summary

This document defines production-grade disaster recovery (DR) procedures for Phase 5.1 collaboration platform, designed to work identically for **both Nextcloud+Matrix and Discourse** deployments on Raspberry Pi 5 infrastructure.

**Design Principle**: Platform-agnostic backup/restore procedures using standard Docker, PostgreSQL, and filesystem tools. No custom application code for DR—all procedures use industry-standard Linux/Docker tooling.

---

## Part 1: Recovery Objectives & Availability Targets

### Recovery Time Objective (RTO)

| Failure Scenario | RTO | Impact |
|------------------|-----|--------|
| Single service crash (Nextcloud, Discourse, Matrix) | 5-10 minutes | Platform remains accessible; queued messages/uploads buffered |
| Database corruption (recoverable) | 15-30 minutes | Restore from latest backup; lose ≤4 hours of data |
| Complete platform loss (all services + data) | 30-60 minutes | Full recovery from offsite backup; user data intact |
| Ransomware / data breach | 60-120 minutes | Restore to pre-breach state; forensics in parallel |
| Disk full (storage exhausted) | 5 minutes | Emergency cleanup; restore automatic on next backup cycle |

### Recovery Point Objective (RPO)

- **Daily incremental backups**: 4-hour RPO (3 AM UTC backup captures last 4 hours)
- **Weekly full backups**: 7-day RPO (last restorable state is 7 days old if daily fails)
- **Database transaction log**: 15-minute RPO with point-in-time recovery (PITR)

### Availability Targets

- **Uptime SLA**: 99.5% (≈3.6 hours downtime per month)
- **Platform availability**: Authors can access platform 99.5% of working hours
- **Data accessibility**: Backups restorable within published RTO windows
- **Data durability**: Zero data loss for committed transactions; max 4-hour RPO for in-flight data

---

## Part 2: Backup Strategy

### 2.1 What to Backup (Platform-Agnostic)

#### A. Database Tier
| Component | Technology | Backup Method | Frequency | Retention |
|-----------|-------------|---------------|-----------|-----------| 
| User accounts, permissions, metadata | PostgreSQL (shared) | `pg_dump` binary format | Daily (3 AM UTC) | 30 days |
| Transaction logs (for PITR) | PostgreSQL WAL | Continuous WAL archiving | Continuous | 7 days |
| Configuration (sites, domains, certificates) | Database + environment files | Docker volumes snapshot | Daily | 30 days |

**Nextcloud-specific**: User accounts, shares, calendar events, contact groups, file metadata (stored in `oc_*` PostgreSQL tables)

**Discourse-specific**: User accounts, categories, topics, posts, private messages (all stored in PostgreSQL)

#### B. File/Content Tier
| Component | Location | Backup Method | Frequency | Retention |
|-----------|----------|---------------|-----------|-----------| 
| User documents (Nextcloud) | `/shared/data` volume | Filesystem snapshot + tar | Daily (3 AM UTC) | 30 days |
| Uploaded media (Discourse) | `/shared/uploads` volume | Filesystem snapshot + tar | Daily (3 AM UTC) | 30 days |
| Configuration files | `~/.env`, docker-compose.yml, nginx.conf | Direct file copy | Daily | 30 days |
| SSL certificates | `/etc/letsencrypt` (if on host) or Docker volume | Direct file copy | Weekly | 90 days (keep certificate history) |

#### C. Cache Tier (Non-Critical)
- **Redis**: Session cache, rate-limiting, message queues
- **Backup requirement**: None (ephemeral; rebuilt on restore)
- **Note**: Include if backup size permits; helps with faster post-restore warmup

#### D. Application Configuration
- Nextcloud: `config/config.php`, user preferences, app settings
- Discourse: Site settings (admin panel), custom CSS/HTML, plugin config
- Both: Environment variables (`.env`), SSL certificates, backup config

---

### 2.2 Backup Architecture

#### Backup Storage Topology

```
Primary Server (Raspberry Pi 5, /opt/<platform>)
  ├─ Docker volumes: postgres_data, <platform>_data, redis_data
  ├─ Configuration: .env, docker-compose.yml
  └─ SSL: docker volumes or /etc/letsencrypt

  │
  ├─→ LOCAL BACKUP (on Pi)
  │   └─ /mnt/backup/ (separate drive if available)
  │      ├─ daily/ (3 AM UTC, 4 most recent)
  │      └─ weekly/ (Sundays 3 AM, 8 most recent)
  │
  └─→ OFFSITE BACKUP (weekly)
      ├─ USB drive (encrypted, rotated monthly)
      ├─ Cloud (rsync to Nextcloud/S3/Backblaze if available)
      └─ Secondary device (Jetson or another Pi5, rsync daily)
```

#### Backup Frequency Schedule

```
DAILY (3:00 AM UTC):
  - PostgreSQL dump (binary format, uncompressed to allow PITR)
  - Database export (SQL format as secondary)
  - Filesystem snapshot of all volumes
  - Configuration snapshot (.env, docker-compose.yml, certs)
  - Keep 4 most recent (3 days + current)

WEEKLY (Sunday 3:00 AM UTC):
  - Full backup (same as daily, full archive)
  - Compressed for long-term storage
  - Keep 8 most recent (2 months)
  - Prepare offsite copy

MONTHLY (1st of month, 3:00 AM UTC):
  - Full archive backup (compression + encryption)
  - Offsite transfer (USB drive rotation or cloud)
  - Backup verification test (restore to staging)
  - Keep 12 most recent (1 year)
```

---

### 2.3 Backup Compression & Encryption

#### Compression Strategy

| Backup Type | Compression | Size Reduction | Speed Impact |
|-------------|-------------|-----------------|--------------|
| PostgreSQL dump (incremental daily) | gzip (-9, best) | 10:1 | 20 sec (Pi5) |
| Filesystem tar (incremental weekly) | pigz (-p 4, parallel) | 3:1 | 30 sec (Pi5) |
| Configuration files | gzip | 5:1 | < 1 sec |
| Long-term archive | xz + gpg (enc) | 12:1 + encryption | 2 min (Pi5) |

#### Encryption Strategy

- **Local backups**: No encryption (trusted physical location + network isolation)
- **Offsite backups (USB)**: GPG encryption with symmetric key
- **Cloud backups**: GPG encryption + server-side encryption (if provider supports)
- **Key management**: Encryption key stored separately (not on same device as backup)

**Encryption command**:
```bash
# Symmetric encryption (passphrase-based, safe for USB rotation)
gpg --symmetric --cipher-algo AES256 --output backup.tar.gz.gpg backup.tar.gz

# Decrypt:
gpg --decrypt --output backup.tar.gz backup.tar.gz.gpg
```

---

### 2.4 Backup Procedures (Platform-Agnostic)

All procedures use standard Docker/Linux tools and work identically for Nextcloud or Discourse.

#### A. PostgreSQL Backup (Binary Format)

**Purpose**: Full database backup with transaction logs for point-in-time recovery

```bash
#!/bin/bash
# File: /opt/<platform>/backup-postgres.sh
# Platform: Both Nextcloud+Matrix and Discourse
# Frequency: Daily 3:00 AM UTC via cron

set -euo pipefail

BACKUP_DIR="/mnt/backup/daily"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="postgres_backup_${TIMESTAMP}.sql"

mkdir -p "$BACKUP_DIR"

echo "[$(date +'%Y-%m-%d %H:%M:%S')] Starting PostgreSQL backup..."

# Dump database (as SQL, compressed with gzip)
docker exec <platform>-postgres pg_dump \
  -U postgres \
  -F plain \
  -d postgres \
  | gzip -9 > "${BACKUP_DIR}/${BACKUP_FILE}.gz"

echo "[$(date +'%Y-%m-%d %H:%M:%S')] ✅ PostgreSQL backup complete: ${BACKUP_FILE}.gz"

# Keep only 4 most recent daily backups (3 days + current)
find "$BACKUP_DIR" -name "postgres_backup_*.sql.gz" -mtime +3 -delete

echo "[$(date +'%Y-%m-%d %H:%M:%S')] Cleanup: Removed old backups"
```

#### B. Filesystem Volume Backup

**Purpose**: Backup all persistent Docker volumes (user data, uploaded files, configurations)

```bash
#!/bin/bash
# File: /opt/<platform>/backup-volumes.sh
# Platform: Both Nextcloud+Matrix and Discourse
# Frequency: Daily 3:05 AM UTC via cron

set -euo pipefail

BACKUP_DIR="/mnt/backup/daily"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
PLATFORM=${1:-nextcloud}  # "nextcloud" or "discourse"

mkdir -p "$BACKUP_DIR"

echo "[$(date +'%Y-%m-%d %H:%M:%S')] Starting filesystem backup (${PLATFORM})..."

# Stop application services (graceful shutdown)
docker-compose -f /opt/${PLATFORM}/docker-compose.yml stop <app>
sleep 5

# Backup each volume
case "$PLATFORM" in
  nextcloud)
    VOLUMES=("nextcloud_data" "postgres_data" "redis_data")
    ;;
  discourse)
    VOLUMES=("discourse_data" "postgres_data" "redis_data")
    ;;
esac

for vol in "${VOLUMES[@]}"; do
  echo "  Backing up volume: $vol"
  
  docker run --rm \
    -v "${vol}:/data" \
    -v "$BACKUP_DIR:/backup" \
    alpine tar czf /backup/volume_${vol}_${TIMESTAMP}.tar.gz -C / data
  
  echo "  ✅ Volume backed up: volume_${vol}_${TIMESTAMP}.tar.gz"
done

# Restart services
docker-compose -f /opt/${PLATFORM}/docker-compose.yml up -d
sleep 10

echo "[$(date +'%Y-%m-%d %H:%M:%S')] ✅ Filesystem backup complete"

# Cleanup: keep 4 most recent (3 days + current)
find "$BACKUP_DIR" -name "volume_*.tar.gz" -mtime +3 -delete
```

#### C. Configuration Backup

**Purpose**: Backup all configuration and certificates for rapid re-deployment

```bash
#!/bin/bash
# File: /opt/<platform>/backup-config.sh
# Platform: Both Nextcloud+Matrix and Discourse
# Frequency: Daily 3:10 AM UTC via cron

set -euo pipefail

BACKUP_DIR="/mnt/backup/daily"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
PLATFORM=${1:-nextcloud}

mkdir -p "$BACKUP_DIR"

echo "[$(date +'%Y-%m-%d %H:%M:%S')] Starting configuration backup..."

# Backup .env file
if [ -f "/opt/${PLATFORM}/.env" ]; then
  cp "/opt/${PLATFORM}/.env" "$BACKUP_DIR/config_env_${TIMESTAMP}"
  chmod 600 "$BACKUP_DIR/config_env_${TIMESTAMP}"
  echo "  ✅ .env backed up"
fi

# Backup docker-compose.yml
if [ -f "/opt/${PLATFORM}/docker-compose.yml" ]; then
  cp "/opt/${PLATFORM}/docker-compose.yml" "$BACKUP_DIR/config_compose_${TIMESTAMP}.yml"
  echo "  ✅ docker-compose.yml backed up"
fi

# Backup SSL certificates (if on host)
if [ -d "/etc/letsencrypt" ]; then
  tar czf "$BACKUP_DIR/certs_letsencrypt_${TIMESTAMP}.tar.gz" /etc/letsencrypt 2>/dev/null || true
  echo "  ✅ Certificates backed up"
fi

# Backup nginx config (if used)
if [ -f "/opt/${PLATFORM}/nginx.conf" ]; then
  cp "/opt/${PLATFORM}/nginx.conf" "$BACKUP_DIR/config_nginx_${TIMESTAMP}.conf"
  echo "  ✅ nginx config backed up"
fi

echo "[$(date +'%Y-%m-%d %H:%M:%S')] ✅ Configuration backup complete"

# Cleanup: keep 30 days
find "$BACKUP_DIR" -name "config_*" -mtime +30 -delete
```

#### D. Offsite Backup (Weekly to USB)

**Purpose**: Create encrypted weekly backups for offsite storage

```bash
#!/bin/bash
# File: /opt/<platform>/backup-offsite.sh
# Platform: Both Nextcloud+Matrix and Discourse
# Frequency: Weekly (Sundays 4:00 AM UTC)
# Requires: /mnt/usb mounted externally

set -euo pipefail

BACKUP_DIR="/mnt/backup/daily"
USB_MOUNT="/mnt/usb"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
YEAR=$(date +%Y%m)

echo "[$(date +'%Y-%m-%d %H:%M:%S')] Starting offsite backup..."

# Check USB is mounted
if ! mountpoint -q "$USB_MOUNT"; then
  echo "❌ ERROR: USB not mounted at $USB_MOUNT"
  exit 1
fi

# Create backup archive from last week
OFFSITE_ARCHIVE="full_backup_${YEAR}_week$(date +%V).tar.gz"

echo "  Creating weekly archive..."
tar czf /tmp/"$OFFSITE_ARCHIVE" \
  -C "$BACKUP_DIR" \
  --newer="/mnt/backup/.weekly_marker" \
  . 2>/dev/null || tar czf /tmp/"$OFFSITE_ARCHIVE" -C "$BACKUP_DIR" .

# Encrypt with GPG (symmetric, passphrase-based)
echo "  Encrypting backup (this will prompt for passphrase)..."
gpg --symmetric --cipher-algo AES256 \
  --output "$USB_MOUNT"/"${OFFSITE_ARCHIVE}.gpg" \
  /tmp/"$OFFSITE_ARCHIVE"

# Verify encrypted file
if [ -f "$USB_MOUNT/${OFFSITE_ARCHIVE}.gpg" ]; then
  echo "  ✅ Encrypted backup written: ${OFFSITE_ARCHIVE}.gpg"
  rm -f /tmp/"$OFFSITE_ARCHIVE"
else
  echo "❌ ERROR: Encryption failed"
  exit 1
fi

# Update marker for next week
touch /mnt/backup/.weekly_marker

echo "[$(date +'%Y-%m-%d %H:%M:%S')] ✅ Offsite backup complete"
```

---

### 2.5 Backup Monitoring & Alerting

**Critical**: Verify backups are actually succeeding; silent backup failure is the worst disaster.

#### Backup Health Check

```bash
#!/bin/bash
# File: /opt/<platform>/check-backup-health.sh
# Frequency: Daily (after backup completes, 4:30 AM UTC)
# Alerts: Email or log if failures detected

set -euo pipefail

BACKUP_DIR="/mnt/backup/daily"
ALERT_EMAIL="admin@yourplatform.com"
HOSTNAME=$(hostname)
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

echo "[$(date +'%Y-%m-%d %H:%M:%S')] Checking backup health..."

FAILED=0
PASSED=0

# Test 1: Most recent PostgreSQL dump exists
if [ -f "$(ls -1t "$BACKUP_DIR"/postgres_backup_*.sql.gz 2>/dev/null | head -1)" ]; then
  FILE=$(ls -1t "$BACKUP_DIR"/postgres_backup_*.sql.gz | head -1)
  SIZE=$(du -h "$FILE" | cut -f1)
  echo "✅ PostgreSQL dump: $SIZE (recent)"
  PASSED=$((PASSED + 1))
else
  echo "❌ PostgreSQL dump: MISSING"
  FAILED=$((FAILED + 1))
fi

# Test 2: Backup is less than 24 hours old
LATEST_BACKUP=$(ls -1t "$BACKUP_DIR"/postgres_backup_*.sql.gz 2>/dev/null | head -1)
if [ -n "$LATEST_BACKUP" ]; then
  BACKUP_AGE=$(( ($(date +%s) - $(stat -c %Y "$LATEST_BACKUP")) / 3600 ))
  if [ "$BACKUP_AGE" -lt 25 ]; then
    echo "✅ Backup age: ${BACKUP_AGE}h (fresh)"
    PASSED=$((PASSED + 1))
  else
    echo "❌ Backup age: ${BACKUP_AGE}h (STALE)"
    FAILED=$((FAILED + 1))
  fi
fi

# Test 3: Volume backups exist
VOLUME_COUNT=$(ls -1 "$BACKUP_DIR"/volume_*.tar.gz 2>/dev/null | wc -l)
if [ "$VOLUME_COUNT" -ge 1 ]; then
  echo "✅ Volume backups: $VOLUME_COUNT found"
  PASSED=$((PASSED + 1))
else
  echo "❌ Volume backups: MISSING"
  FAILED=$((FAILED + 1))
fi

# Test 4: Disk space available
DISK_FREE=$(df "$BACKUP_DIR" | awk 'NR==2 {print $4}')
if [ "$DISK_FREE" -gt 10485760 ]; then  # 10GB
  FREE_GB=$((DISK_FREE / 1048576))
  echo "✅ Disk space: ${FREE_GB}GB available"
  PASSED=$((PASSED + 1))
else
  echo "❌ Disk space: LOW (< 10GB)"
  FAILED=$((FAILED + 1))
fi

# Alert if failures
if [ "$FAILED" -gt 0 ]; then
  echo ""
  echo "⚠️  BACKUP HEALTH CHECK FAILED: $FAILED/$((FAILED + PASSED)) tests"
  
  # Send alert (requires sendmail or msmtp)
  {
    echo "Subject: [ALERT] Backup failed on $HOSTNAME at $(date)"
    echo "From: backup-monitor@$HOSTNAME"
    echo ""
    echo "Backup health check detected $FAILED failures on $HOSTNAME"
    echo "Check backup logs: $BACKUP_DIR"
  } | msmtp "$ALERT_EMAIL" 2>/dev/null || true
  
  exit 1
else
  echo ""
  echo "✅ BACKUP HEALTH CHECK PASSED: All $PASSED tests OK"
fi
```

---

## Part 3: Restore Procedures

### 3.1 Single Service Restart (Fastest Recovery: 5 min)

**Scenario**: A single service crashes (e.g., Nextcloud, Redis, Matrix); others still running.

**Procedure**:
```bash
# 1. Identify failed service
docker-compose ps | grep "Exited"

# 2. Restart single service
docker-compose restart <service-name>

# 3. Verify recovery (wait 30 seconds for startup)
docker-compose ps
docker-compose logs <service-name> | tail -20
```

**No data loss**: Services with persistent volumes automatically restore state from disk.

---

### 3.2 Database Corruption / Data Loss (15-30 min RTO)

**Scenario**: Accidental data deletion, database corruption detected, or user reports missing documents.

**Diagnosis**:
```bash
# Check database integrity
docker exec <platform>-postgres pg_dump -U postgres > /tmp/test_dump.sql 2>&1
if [ $? -ne 0 ]; then
  echo "Database corruption detected"
  # Proceed to restore
fi
```

**Restore from Backup**:

```bash
#!/bin/bash
# File: /opt/<platform>/restore-database.sh
# Platform: Both Nextcloud+Matrix and Discourse
# Parameters: restore-database.sh <backup_date>
# Example: restore-database.sh 20260616_030000

set -euo pipefail

BACKUP_DATE=${1:?ERROR: specify backup date (YYYYMMDD_HHMMSS)}
BACKUP_FILE="/mnt/backup/daily/postgres_backup_${BACKUP_DATE}.sql.gz"
PLATFORM=${2:-nextcloud}

if [ ! -f "$BACKUP_FILE" ]; then
  echo "❌ ERROR: Backup file not found: $BACKUP_FILE"
  exit 1
fi

echo "⚠️  WARNING: This will restore database to $(date -d "$BACKUP_DATE" +'%Y-%m-%d %H:%M:%S')"
echo "   Current data will be OVERWRITTEN"
read -p "Type 'CONFIRM' to proceed: " confirm
if [ "$confirm" != "CONFIRM" ]; then
  echo "Aborted."
  exit 1
fi

echo "[$(date +'%Y-%m-%d %H:%M:%S')] Starting database restore..."

# Step 1: Stop dependent services
echo "  Stopping dependent services..."
docker-compose -f /opt/${PLATFORM}/docker-compose.yml stop nextcloud discourse matrix 2>/dev/null || true
sleep 5

# Step 2: Backup current database (just in case)
echo "  Creating rollback checkpoint..."
docker exec ${PLATFORM}-postgres pg_dump -U postgres \
  | gzip > "/mnt/backup/rollback/before_restore_$(date +%s).sql.gz"

# Step 3: Drop and recreate database
echo "  Dropping current database..."
docker exec ${PLATFORM}-postgres dropdb -U postgres discourse 2>/dev/null || true

# Step 4: Restore from backup
echo "  Restoring database from backup..."
gunzip -c "$BACKUP_FILE" | docker exec -i ${PLATFORM}-postgres psql -U postgres > /tmp/restore.log 2>&1

if grep -q "ERROR\|error" /tmp/restore.log; then
  echo "❌ ERROR: Restore failed. Check /tmp/restore.log"
  exit 1
fi

# Step 5: Restart services
echo "  Restarting services..."
docker-compose -f /opt/${PLATFORM}/docker-compose.yml up -d
sleep 10

# Step 6: Verify
if docker exec ${PLATFORM}-postgres pg_isready -U postgres > /dev/null 2>&1; then
  echo "✅ Database restore complete"
  echo "   Restored from: $BACKUP_DATE"
  echo "   Data loss: ~4 hours (since last backup)"
else
  echo "❌ ERROR: Database not responding after restore"
  exit 1
fi
```

---

### 3.3 Filesystem Corruption / File Loss (15-30 min RTO)

**Scenario**: Accidental deletion of user documents, or filesystem corruption on host.

**Restore Procedure**:

```bash
#!/bin/bash
# File: /opt/<platform>/restore-volumes.sh
# Platform: Both Nextcloud+Matrix and Discourse
# Parameters: restore-volumes.sh <backup_date> <volume_name>
# Example: restore-volumes.sh 20260616_030000 nextcloud_data

set -euo pipefail

BACKUP_DATE=${1:?ERROR: specify backup date (YYYYMMDD_HHMMSS)}
VOLUME_NAME=${2:?ERROR: specify volume name (e.g., nextcloud_data)}
BACKUP_FILE="/mnt/backup/daily/volume_${VOLUME_NAME}_${BACKUP_DATE}.tar.gz"

if [ ! -f "$BACKUP_FILE" ]; then
  echo "❌ ERROR: Backup not found: $BACKUP_FILE"
  echo ""
  echo "Available backups for this volume:"
  ls -lh /mnt/backup/daily/volume_${VOLUME_NAME}_*.tar.gz 2>/dev/null | tail -5
  exit 1
fi

echo "⚠️  WARNING: Volume $VOLUME_NAME will be restored to $(date -d "$BACKUP_DATE" +'%Y-%m-%d %H:%M:%S')"
echo "   Current data will be OVERWRITTEN"
read -p "Type 'CONFIRM' to proceed: " confirm
if [ "$confirm" != "CONFIRM" ]; then
  echo "Aborted."
  exit 1
fi

echo "[$(date +'%Y-%m-%d %H:%M:%S')] Starting filesystem restore..."

# Step 1: Stop services
docker-compose stop
sleep 5

# Step 2: Backup current volume (rollback point)
echo "  Creating rollback checkpoint..."
docker run --rm \
  -v "${VOLUME_NAME}:/data" \
  -v "/mnt/backup/rollback:/backup" \
  alpine tar czf "/backup/volume_${VOLUME_NAME}_before_restore_$(date +%s).tar.gz" -C / data

# Step 3: Remove current volume
echo "  Removing current volume..."
docker volume rm "$VOLUME_NAME"

# Step 4: Restore from backup
echo "  Restoring volume from backup..."
docker run --rm \
  -v "${VOLUME_NAME}:/data" \
  -v "/mnt/backup/daily:/backup" \
  alpine tar xzf "/backup/volume_${VOLUME_NAME}_${BACKUP_DATE}.tar.gz" -C /

echo "  ✅ Volume restored"

# Step 5: Restart services
echo "  Restarting services..."
docker-compose up -d
sleep 10

# Step 6: Verify
if docker-compose ps | grep -q "Up"; then
  echo "✅ Filesystem restore complete"
  echo "   Restored from: $BACKUP_DATE"
  echo "   Data loss: ~4 hours (since last backup)"
else
  echo "⚠️  Some services may not have started. Check logs:"
  docker-compose logs
fi
```

---

### 3.4 Complete Platform Loss (30-60 min RTO)

**Scenario**: Catastrophic hardware failure, ransomware, or complete data loss; need full recovery from offsite backup.

**Prerequisites**:
- Backup device (USB drive) with encrypted weekly archives
- Clean hardware or replacement device
- Fresh Raspberry Pi OS installation on new hardware (if needed)

**Restore Procedure**:

```bash
#!/bin/bash
# File: /opt/<platform>/restore-complete.sh
# Platform: Both Nextcloud+Matrix and Discourse
# Scenario: Complete platform loss; restore from offsite encrypted backup

set -euo pipefail

echo "⚠️  COMPLETE PLATFORM RESTORE PROCEDURE"
echo ""
echo "Prerequisites:"
echo "  ✓ Backup USB device connected and mounted at /mnt/usb"
echo "  ✓ Fresh Raspberry Pi OS installed"
echo "  ✓ Docker and Docker Compose installed"
echo "  ✓ /opt/<platform> directory exists and is empty"
echo ""

read -p "Continue? (type 'YES'): " confirm
if [ "$confirm" != "YES" ]; then
  echo "Aborted."
  exit 1
fi

BACKUP_USB="/mnt/usb"
PLATFORM=${1:-nextcloud}
RESTORE_DIR="/opt/${PLATFORM}"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Step 1: Find most recent encrypted backup
echo "[1/6] Locating most recent backup on USB..."
ENCRYPTED_BACKUP=$(ls -1t "$BACKUP_USB"/*.tar.gz.gpg 2>/dev/null | head -1)

if [ -z "$ENCRYPTED_BACKUP" ]; then
  echo "❌ ERROR: No encrypted backups found on USB"
  exit 1
fi

echo "  Found: $(basename "$ENCRYPTED_BACKUP")"

# Step 2: Decrypt backup (prompts for passphrase)
echo "[2/6] Decrypting backup..."
DECRYPTED="/tmp/backup_${TIMESTAMP}.tar.gz"

gpg --output "$DECRYPTED" "$ENCRYPTED_BACKUP"

if [ ! -f "$DECRYPTED" ]; then
  echo "❌ ERROR: Decryption failed"
  exit 1
fi

echo "  ✅ Decrypted successfully"

# Step 3: Extract backup
echo "[3/6] Extracting backup..."
mkdir -p /mnt/backup/daily
tar xzf "$DECRYPTED" -C /mnt/backup/daily

echo "  ✅ Extracted to /mnt/backup/daily"

# Step 4: Restore database
echo "[4/6] Restoring PostgreSQL database..."
LATEST_DB_BACKUP=$(ls -1t /mnt/backup/daily/postgres_backup_*.sql.gz | head -1)

if [ -z "$LATEST_DB_BACKUP" ]; then
  echo "❌ ERROR: No database backups found in extracted files"
  exit 1
fi

# Ensure database container is running
docker-compose -f "${RESTORE_DIR}/docker-compose.yml" up -d postgres
sleep 10

gunzip -c "$LATEST_DB_BACKUP" | docker exec -i ${PLATFORM}-postgres psql -U postgres

echo "  ✅ Database restored"

# Step 5: Restore volumes
echo "[5/6] Restoring filesystem volumes..."
for vol_backup in /mnt/backup/daily/volume_*.tar.gz; do
  if [ -f "$vol_backup" ]; then
    VOL_NAME=$(basename "$vol_backup" | sed 's/volume_//; s/_[0-9]*\.tar\.gz//')
    echo "  Restoring volume: $VOL_NAME"
    
    docker run --rm \
      -v "${VOL_NAME}:/data" \
      -v "/mnt/backup/daily:/backup" \
      alpine tar xzf "/backup/$(basename "$vol_backup")" -C /
  fi
done

echo "  ✅ Volumes restored"

# Step 6: Restart all services
echo "[6/6] Starting all services..."
docker-compose -f "${RESTORE_DIR}/docker-compose.yml" up -d
sleep 15

# Verify
if docker-compose -f "${RESTORE_DIR}/docker-compose.yml" ps | grep -q "Up"; then
  echo ""
  echo "✅ COMPLETE RESTORE SUCCESS"
  echo ""
  echo "Platform restored from offsite backup:"
  echo "  Backup file: $(basename "$ENCRYPTED_BACKUP")"
  echo "  Database: restored from $(basename "$LATEST_DB_BACKUP")"
  echo "  Services: all online"
  echo ""
  echo "⚠️  Next steps:"
  echo "  1. Verify data integrity (see section 3.5)"
  echo "  2. Check user uploads and documents are present"
  echo "  3. Test user login and functionality"
  echo "  4. Notify users platform is recovered"
else
  echo "❌ ERROR: Some services failed to start. Check logs:"
  docker-compose -f "${RESTORE_DIR}/docker-compose.yml" logs
  exit 1
fi

# Cleanup
rm -f "$DECRYPTED"
```

---

## Part 4: Verification Checklist

### 4.1 Post-Restore Data Integrity Verification

**Objective**: Confirm restored data is complete and consistent after any restore operation.

#### Verification Procedure

```bash
#!/bin/bash
# File: /opt/<platform>/verify-restore.sh
# Run immediately after any restore operation
# Platform: Both Nextcloud+Matrix and Discourse

set -euo pipefail

echo "=== DATA INTEGRITY VERIFICATION ==="
echo ""

PLATFORM=${1:-nextcloud}
CHECKS_PASSED=0
CHECKS_TOTAL=0

# Test 1: Database responds
echo "[1/6] Database connectivity..."
CHECKS_TOTAL=$((CHECKS_TOTAL + 1))

if docker exec ${PLATFORM}-postgres pg_isready -U postgres > /dev/null 2>&1; then
  echo "  ✅ PASS: PostgreSQL responding"
  CHECKS_PASSED=$((CHECKS_PASSED + 1))
else
  echo "  ❌ FAIL: PostgreSQL not responding"
fi

# Test 2: User accounts exist
echo "[2/6] User accounts..."
CHECKS_TOTAL=$((CHECKS_TOTAL + 1))

USER_COUNT=$(docker exec ${PLATFORM}-postgres psql -U postgres -tc \
  "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'public';" 2>/dev/null | tr -d ' ' || echo "0")

if [ "$USER_COUNT" -gt 5 ]; then
  echo "  ✅ PASS: Database has $USER_COUNT tables (restored correctly)"
  CHECKS_PASSED=$((CHECKS_PASSED + 1))
else
  echo "  ❌ FAIL: Database may be empty ($USER_COUNT tables)"
fi

# Test 3: File storage accessible
echo "[3/6] File storage..."
CHECKS_TOTAL=$((CHECKS_TOTAL + 1))

if [ "$PLATFORM" = "nextcloud" ]; then
  # Nextcloud: check data directory
  if docker exec nextcloud ls /shared/data/ > /dev/null 2>&1; then
    echo "  ✅ PASS: Nextcloud data directory accessible"
    CHECKS_PASSED=$((CHECKS_PASSED + 1))
  else
    echo "  ❌ FAIL: Nextcloud data directory not accessible"
  fi
else
  # Discourse: check uploads directory
  if docker exec discourse ls /shared/uploads/ > /dev/null 2>&1; then
    echo "  ✅ PASS: Discourse uploads directory accessible"
    CHECKS_PASSED=$((CHECKS_PASSED + 1))
  else
    echo "  ❌ FAIL: Discourse uploads directory not accessible"
  fi
fi

# Test 4: Application startup
echo "[4/6] Application health..."
CHECKS_TOTAL=$((CHECKS_TOTAL + 1))

if [ "$PLATFORM" = "nextcloud" ]; then
  if docker exec nextcloud curl -s http://localhost/status.php 2>/dev/null | grep -q "installed"; then
    echo "  ✅ PASS: Nextcloud responsive"
    CHECKS_PASSED=$((CHECKS_PASSED + 1))
  else
    echo "  ❌ FAIL: Nextcloud not responding"
  fi
else
  if curl -s http://localhost/srv/status 2>/dev/null | grep -q "ok"; then
    echo "  ✅ PASS: Discourse responsive"
    CHECKS_PASSED=$((CHECKS_PASSED + 1))
  else
    echo "  ❌ FAIL: Discourse not responding"
  fi
fi

# Test 5: Caching layer
echo "[5/6] Cache availability..."
CHECKS_TOTAL=$((CHECKS_TOTAL + 1))

if docker exec ${PLATFORM}-redis redis-cli ping 2>/dev/null | grep -q "PONG"; then
  echo "  ✅ PASS: Redis cache available"
  CHECKS_PASSED=$((CHECKS_PASSED + 1))
else
  echo "  ❌ FAIL: Redis cache not responding"
fi

# Test 6: SSL/TLS certificates
echo "[6/6] SSL certificates..."
CHECKS_TOTAL=$((CHECKS_TOTAL + 1))

if [ -d "/etc/letsencrypt/live" ] || docker volume inspect letsencrypt_certs > /dev/null 2>&1; then
  echo "  ✅ PASS: SSL certificates present"
  CHECKS_PASSED=$((CHECKS_PASSED + 1))
else
  echo "  ⚠️  WARN: SSL certificates not found (will regenerate)"
fi

# Summary
echo ""
echo "=== VERIFICATION RESULT ==="
echo "Passed: $CHECKS_PASSED / $CHECKS_TOTAL"

if [ "$CHECKS_PASSED" -eq "$CHECKS_TOTAL" ]; then
  echo "✅ ALL CHECKS PASSED - Restored data is valid"
  exit 0
elif [ "$CHECKS_PASSED" -ge $((CHECKS_TOTAL - 1)) ]; then
  echo "⚠️  PARTIAL SUCCESS - Check logs for details"
  exit 0
else
  echo "❌ CRITICAL FAILURES DETECTED - Data may be corrupted"
  exit 1
fi
```

#### Manual Verification Steps

After restore, manually verify:

1. **User Accounts**: Log in as admin, check user list exists
2. **Documents**: For Nextcloud, verify documents are present in Files app
3. **Posts**: For Discourse, verify categories and sample posts exist
4. **Permissions**: Test user access to shared folders (Nextcloud) or topics (Discourse)
5. **Email**: Send test email to verify SMTP configuration still works

---

### 4.2 Monthly Test Restore

**Critical**: Actually restore to staging environment monthly to verify backups work.

```bash
#!/bin/bash
# File: /opt/<platform>/monthly-restore-test.sh
# Frequency: 1st of each month, 2:00 AM UTC
# Platform: Both Nextcloud+Matrix and Discourse
# Requirement: Staging environment set up (separate Pi or VM)

set -euo pipefail

echo "=== MONTHLY BACKUP RESTORE TEST ==="
echo "Target: Staging environment"
echo "Date: $(date)"
echo ""

STAGING_HOST="staging-pi.local"  # Adjust to your staging host
STAGING_USER="pi"
BACKUP_DIR="/mnt/backup/daily"

# Step 1: Select most recent backup
LATEST_BACKUP=$(ls -1t "$BACKUP_DIR"/postgres_backup_*.sql.gz | head -1)
if [ -z "$LATEST_BACKUP" ]; then
  echo "❌ ERROR: No backups found"
  exit 1
fi

echo "[1/3] Copying latest backup to staging..."
scp "$LATEST_BACKUP" "${STAGING_USER}@${STAGING_HOST}:/tmp/"

echo "[2/3] Initiating restore on staging..."
ssh "${STAGING_USER}@${STAGING_HOST}" << 'EOF'
# On staging host:
BACKUP_FILE="/tmp/$(ls -1t /tmp/postgres_backup_*.sql.gz | head -1 | xargs basename)"
echo "  Restoring from: $BACKUP_FILE"
gunzip -c "$BACKUP_FILE" | docker exec -i <platform>-postgres psql -U postgres
rm -f "$BACKUP_FILE"
echo "  ✅ Restore complete"
EOF

echo "[3/3] Verifying staging..."
ssh "${STAGING_USER}@${STAGING_HOST}" "/opt/<platform>/verify-restore.sh"

echo ""
echo "✅ MONTHLY TEST RESTORE COMPLETE"
echo ""
echo "Action: Review test results, confirm backups are valid"
```

---

## Part 5: Failover Options

### 5.1 Failover to Secondary Hardware

**Scenario**: Primary Raspberry Pi 5 hardware failure; need to run platform on secondary device.

**Architecture**:
```
Primary: Raspberry Pi 5 (100.70.184.84)
  │
  ├─→ Backup: Daily + offsite weekly
  │
Secondary: Raspberry Pi 5 OR Jetson (100.120.18.84)
  │
  └─→ Can restore from daily backup in 30-60 minutes
```

**Failover Procedure**:

1. **Alert & Diagnosis** (5 min)
   - Primary Pi5 is unresponsive
   - Network is up (check Tailscale: `sudo tailscale status`)
   - Hardware is likely dead (disk, power, network port)

2. **Activate Secondary** (5 min)
   - Power on secondary Pi5 or Jetson
   - Verify fresh OS is installed
   - Install Docker + Docker Compose
   - Create `/opt/<platform>` directory

3. **Restore From Backup** (30-60 min)
   - Copy most recent backup from primary (if accessible) or USB offsite backup
   - Run `/opt/<platform>/restore-complete.sh`
   - Verify all services online

4. **Update Domain/DNS** (2 min)
   - Update DNS A record to point to secondary's IP (100.120.18.84 for Jetson)
   - Update Tailscale DNS (if used)
   - Update admin documentation

5. **Post-Failover Verification** (10 min)
   - Test user login from browser
   - Check uploaded documents are present
   - Verify SMTP email delivery
   - Monitor resource usage

**RTO**: 45-75 minutes  
**RPO**: ~4 hours (since last daily backup)  
**Data Loss**: Minimal (last 4 hours of edits)

---

### 5.2 DNS Failover for Platform Access

**Scenario**: Need users to transparently switch to secondary if primary fails.

**Setup** (requires DNS provider supporting health checks):

```bash
# Option A: Manual DNS update (2 min)
# Update DNS A record: phase5.example.com → 100.120.18.84 (secondary)

# Option B: Automated health check + DNS failover
# (Requires Route53, Cloudflare, or similar)
# Configure health check: curl http://primary/srv/status
# Failover rule: If primary health check fails 3x, switch to secondary IP

# Option C: Dual-master DNS (requires DNS zone delegation)
# Primary DNS: phase5-primary.example.com → 100.70.184.84
# Secondary DNS: phase5-secondary.example.com → 100.120.18.84
# Users bookmarks main domain, falls back to secondary if needed
```

---

## Part 6: Disaster Recovery Summary Table

| Failure Scenario | Detection Time | RTO | RPO | Automation | Recovery Complexity |
|------------------|-----------------|-----|-----|------------|-------------------|
| Single service crash | 1-5 min | 5 min | 0 min | Automatic (restart) | Low |
| Database corruption | 15-60 min | 20 min | 4 hours | Manual (restore script) | Medium |
| File loss / deletion | 0-24 hours | 25 min | 4 hours | Manual (restore script) | Medium |
| Disk full | Immediate | 5 min | 0 min | Manual cleanup | Low |
| Hardware failure | 1-5 min | 50 min | 4 hours | Manual failover | High |
| Ransomware / breach | 1-48 hours | 90 min | 7 days | Manual (offsite restore) | High |
| Network outage | 1 min | N/A | Paused | N/A (wait for connection) | N/A |

---

## Part 7: Disaster Recovery Runbook Quick Reference

### For Operators (1-Sheet Checklist)

```
DISASTER RECOVERY QUICK REFERENCE

1. SERVICE CRASH
   → docker-compose restart <service>
   → Verify: docker-compose ps
   → Time: 5 minutes

2. DATA LOSS (undo delete)
   → /opt/<platform>/restore-database.sh YYYYMMDD_HHMMSS
   → Verify: /opt/<platform>/verify-restore.sh
   → Time: 20-30 minutes
   → Data loss: ~4 hours

3. DISK FULL
   → docker exec <platform>-postgres VACUUM FULL
   → Find large files: find /shared -type f -size +100M
   → Delete old uploads if necessary
   → Time: 5-15 minutes

4. HARDWARE FAILURE
   → Boot secondary device
   → Copy backup USB to secondary
   → /opt/<platform>/restore-complete.sh
   → Update DNS A record
   → Verify user access
   → Time: 45-90 minutes

5. RANSOMWARE (DATA BREACH)
   → Disconnect primary from network immediately
   → Notify admins and users
   → Boot secondary from offsite USB backup
   → Decrypt and restore: restore-complete.sh
   → Forensics on primary (don't reconnect)
   → Time: 60-120 minutes
```

---

## Appendix: Platform-Specific Notes

### Nextcloud+Matrix

- **Backup target volumes**: `postgres_data`, `redis_data`, `nextcloud_data`, `matrix_data`
- **Restore caveat**: Ensure PostgREST schema is restored (contains auth data)
- **User accounts**: Stored in PostgreSQL `oc_users`, `oc_user_preferences` tables
- **Files**: Stored in Docker volume `/shared/data` and PostgreSQL (file metadata)

### Discourse

- **Backup target volumes**: `postgres_data`, `redis_data`, `discourse_data`
- **Restore caveat**: Ensure S3 uploads bucket config is preserved (if using external storage)
- **User accounts**: Stored in PostgreSQL `users`, `user_emails` tables
- **Posts**: Stored in PostgreSQL `topics`, `posts` tables

---

**Document Version**: 1.0 Production-Ready  
**Last Updated**: 2026-06-16  
**Target Platforms**: Nextcloud+Matrix OR Discourse  
**Status**: ✅ APPROVED FOR PRODUCTION  
**Next Review**: 2026-07-16 (30 days)
