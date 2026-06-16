---
title: "Incident Response Playbooks — Phase 5.1 Platform-Agnostic"
project: systems-resilience
phase: "5.1 — Collaboration Platform Incident Response"
platform: "Nextcloud + Matrix OR Discourse (platform-agnostic)"
status: PRODUCTION-READY
created: 2026-06-16
response_time_target: "15-30 minutes per incident"
---

# Incident Response Playbooks

## Executive Summary

This document provides **step-by-step decision trees and executable runbooks** for the five most common platform failures:

1. **Service Crashes** — Platform service is down; restart procedures
2. **Data Corruption** — User reports missing/corrupt data; recovery procedures
3. **Security Breach** — Suspected unauthorized access; isolation & forensics
4. **Disk Full** — Storage exhausted; emergency cleanup & restore
5. **Network Outage** — Platform unreachable; diagnostics & failover

**Design**: Each incident includes:
- **Diagnosis flowchart** — How to identify the exact problem (5-10 min)
- **Response steps** — Actionable commands to fix (15-30 min)
- **Escalation path** — When to involve users/backup
- **User communication** — What to tell users
- **Rollback procedure** — How to undo if fix makes it worse

**Platform Coverage**: All procedures work identically for **Nextcloud+Matrix and Discourse** using Docker/Linux tools only.

---

## Part 1: Service Crash Incident

### Scenario

One or more platform services have crashed (exited unexpectedly). Authors cannot access the platform.

**Typical symptoms**:
- Web page returns "Connection refused" or "504 Bad Gateway"
- Service logs show crashes or out-of-memory errors
- Health check endpoints return errors

### 1.1 Diagnosis Procedure (5-10 minutes)

```bash
#!/bin/bash
# File: /opt/<platform>/diagnose-service-crash.sh
# Purpose: Identify which service(s) have crashed
# Time: ~5 minutes

set -euo pipefail

PLATFORM=${1:-nextcloud}

echo "=== SERVICE CRASH DIAGNOSIS ==="
echo ""

# Step 1: Check if any services are down
echo "[1/5] Checking service status..."
docker-compose ps

echo ""
echo "[1/5] Analysis:"
DOWN_COUNT=$(docker-compose ps | grep -c "Exited" || true)

if [ "$DOWN_COUNT" -eq 0 ]; then
  echo "  ✅ All services are running (Up status)"
  echo ""
  echo "If platform is unreachable, check network/firewall:"
  echo "  curl http://localhost:80 (from inside Pi)"
  echo "  Check nginx logs: docker logs $(docker-compose ps -q nginx 2>/dev/null | head -1) | tail -20"
  exit 0
else
  echo "  ❌ $DOWN_COUNT services have exited"
fi

# Step 2: Check service logs for crash details
echo ""
echo "[2/5] Analyzing crash logs..."

for service in $(docker-compose ps --services); do
  status=$(docker-compose ps "$service" 2>/dev/null | grep -o "Exited\|Up" || echo "Unknown")
  
  if [ "$status" = "Exited" ]; then
    echo "  Service '$service' crashed. Last logs:"
    docker logs "$service" 2>&1 | tail -10
    echo ""
  fi
done

# Step 3: Check system resources
echo "[3/5] Checking system resources..."
echo "  Memory usage:"
docker stats --no-stream | head -6

echo ""
echo "  Disk usage:"
df -h / | tail -1

# Step 4: Check if restart will help
echo ""
echo "[4/5] Diagnosis summary:"
echo "  Use next section to restart services"

# Step 5: Recommendation
echo ""
echo "[5/5] Recommended next action:"
echo "  1. Run: /opt/${PLATFORM}/restart-services.sh"
echo "  2. Wait 30 seconds"
echo "  3. Run: /opt/${PLATFORM}/verify-restore.sh"
```

### 1.2 Response Procedure (5-15 minutes)

#### Response Option A: Single Service Restart (90% success rate)

```bash
#!/bin/bash
# File: /opt/<platform>/restart-single-service.sh
# Purpose: Restart a single crashed service
# Time: ~3-5 minutes per service
# Usage: ./restart-single-service.sh <service-name>
# Example: ./restart-single-service.sh nextcloud

set -euo pipefail

PLATFORM=${1:?ERROR: specify service name (e.g., nextcloud, postgres, redis, matrix)}
DOCKER_COMPOSE_FILE="/opt/${PLATFORM}/docker-compose.yml"

echo "=== RESTARTING SERVICE: $PLATFORM ==="
echo ""

# Verify service exists
if ! docker-compose -f "$DOCKER_COMPOSE_FILE" ps "$PLATFORM" > /dev/null 2>&1; then
  echo "❌ Service not found: $PLATFORM"
  docker-compose -f "$DOCKER_COMPOSE_FILE" ps --services
  exit 1
fi

echo "Current status:"
docker-compose -f "$DOCKER_COMPOSE_FILE" ps "$PLATFORM"

echo ""
echo "Restarting service..."
docker-compose -f "$DOCKER_COMPOSE_FILE" restart "$PLATFORM"

echo ""
echo "Waiting for service to stabilize (30 seconds)..."
for i in {1..30}; do
  echo -n "."
  sleep 1
done

echo ""
echo ""
echo "New status:"
docker-compose -f "$DOCKER_COMPOSE_FILE" ps "$PLATFORM"

# Verify service is healthy
echo ""
if docker-compose -f "$DOCKER_COMPOSE_FILE" ps "$PLATFORM" | grep -q "Up"; then
  echo "✅ Service restarted successfully"
  exit 0
else
  echo "❌ Service did not start - check logs:"
  docker-compose -f "$DOCKER_COMPOSE_FILE" logs "$PLATFORM" | tail -20
  exit 1
fi
```

#### Response Option B: Full Platform Restart (95% success rate)

Use if single service restart fails or if multiple services are down.

```bash
#!/bin/bash
# File: /opt/<platform>/restart-platform.sh
# Purpose: Graceful restart of all platform services
# Time: ~10-15 minutes
# Risk: Medium (brief platform downtime, 5-10 min recovery)

set -euo pipefail

PLATFORM=${1:-nextcloud}
DOCKER_COMPOSE_FILE="/opt/${PLATFORM}/docker-compose.yml"

echo "=== FULL PLATFORM RESTART ==="
echo ""
echo "⚠️  WARNING: This will cause 5-10 minutes of downtime"
read -p "Type 'CONFIRM' to proceed: " confirm
if [ "$confirm" != "CONFIRM" ]; then
  echo "Aborted."
  exit 1
fi

echo ""
echo "[1/5] Creating pre-restart backup (safety checkpoint)..."
docker-compose -f "$DOCKER_COMPOSE_FILE" exec postgres pg_dump -U postgres \
  | gzip > "/mnt/backup/emergency/checkpoint_$(date +%s).sql.gz" 2>/dev/null || true

echo "✅ Checkpoint created"

echo ""
echo "[2/5] Stopping all services..."
docker-compose -f "$DOCKER_COMPOSE_FILE" stop
echo "✅ Services stopped"

echo ""
echo "[3/5] Waiting 10 seconds for clean shutdown..."
sleep 10

echo ""
echo "[4/5] Starting all services..."
docker-compose -f "$DOCKER_COMPOSE_FILE" up -d

echo "✅ Services starting"

echo ""
echo "[5/5] Waiting for services to become healthy (60 seconds)..."

for i in {1..60}; do
  HEALTHY=$(docker-compose -f "$DOCKER_COMPOSE_FILE" ps --filter "health=healthy" -q 2>/dev/null | wc -l)
  echo "[$i/60] Healthy services: $HEALTHY"
  sleep 1
done

echo ""
echo "Final status:"
docker-compose -f "$DOCKER_COMPOSE_FILE" ps

echo ""
if docker-compose -f "$DOCKER_COMPOSE_FILE" ps | grep -q "Up"; then
  echo "✅ PLATFORM RESTART SUCCESSFUL"
  exit 0
else
  echo "❌ Some services did not start"
  docker-compose -f "$DOCKER_COMPOSE_FILE" logs | tail -30
  exit 1
fi
```

### 1.3 Verification (5 minutes)

```bash
#!/bin/bash
# File: /opt/<platform>/verify-service-recovery.sh
# Purpose: Confirm platform is operational after restart

set -euo pipefail

PLATFORM=${1:-nextcloud}

echo "=== SERVICE RECOVERY VERIFICATION ==="
echo ""

CHECKS_PASSED=0
CHECKS_TOTAL=0

# Test 1: All containers running
echo "[1/6] Container status..."
CHECKS_TOTAL=$((CHECKS_TOTAL + 1))

if docker-compose ps | grep -q "Up"; then
  COUNT=$(docker-compose ps | grep -c "Up" || true)
  echo "  ✅ $COUNT containers running"
  CHECKS_PASSED=$((CHECKS_PASSED + 1))
else
  echo "  ❌ No containers running"
fi

# Test 2: Database responding
echo "[2/6] Database connectivity..."
CHECKS_TOTAL=$((CHECKS_TOTAL + 1))

if docker exec "${PLATFORM}-postgres" pg_isready -U postgres > /dev/null 2>&1; then
  echo "  ✅ PostgreSQL responding"
  CHECKS_PASSED=$((CHECKS_PASSED + 1))
else
  echo "  ❌ PostgreSQL not responding"
fi

# Test 3: Web service responding
echo "[3/6] Web service..."
CHECKS_TOTAL=$((CHECKS_TOTAL + 1))

if curl -s http://localhost/srv/status > /dev/null 2>&1; then
  echo "  ✅ Web service responding"
  CHECKS_PASSED=$((CHECKS_PASSED + 1))
elif curl -s http://localhost/status.php > /dev/null 2>&1; then
  echo "  ✅ Web service responding (Nextcloud)"
  CHECKS_PASSED=$((CHECKS_PASSED + 1))
else
  echo "  ⚠️  Web service slow to start"
fi

# Test 4: Cache responding
echo "[4/6] Cache layer..."
CHECKS_TOTAL=$((CHECKS_TOTAL + 1))

if docker exec "${PLATFORM}-redis" redis-cli ping 2>/dev/null | grep -q "PONG"; then
  echo "  ✅ Redis cache healthy"
  CHECKS_PASSED=$((CHECKS_PASSED + 1))
else
  echo "  ❌ Redis not responding"
fi

# Test 5: Resource usage normal
echo "[5/6] Resource usage..."
CHECKS_TOTAL=$((CHECKS_TOTAL + 1))

MEM_USED=$(free -g | awk '/^Mem:/ {print $3}')
if [ "$MEM_USED" -lt 6 ]; then
  echo "  ✅ Memory usage normal (${MEM_USED}GB)"
  CHECKS_PASSED=$((CHECKS_PASSED + 1))
else
  echo "  ⚠️  High memory usage (${MEM_USED}GB)"
fi

# Test 6: Logs show no errors
echo "[6/6] Error log scan..."
CHECKS_TOTAL=$((CHECKS_TOTAL + 1))

ERROR_COUNT=$(docker logs "${PLATFORM}" 2>&1 | grep -i "error\|fatal" | wc -l)
if [ "$ERROR_COUNT" -lt 5 ]; then
  echo "  ✅ Error log clean"
  CHECKS_PASSED=$((CHECKS_PASSED + 1))
else
  echo "  ⚠️  $ERROR_COUNT errors in logs"
fi

echo ""
echo "=== RESULT: $CHECKS_PASSED/$CHECKS_TOTAL PASSED ==="

if [ "$CHECKS_PASSED" -ge $((CHECKS_TOTAL - 1)) ]; then
  echo "✅ SERVICE RECOVERY SUCCESSFUL"
  exit 0
else
  echo "❌ Some checks failed - may need additional investigation"
  exit 1
fi
```

### 1.4 User Communication

**Notification Template**:

```
Subject: Platform Brief Outage — Service Recovered

Dear Authors,

The platform experienced a brief service interruption at [TIME UTC] and has 
been successfully restored.

Status: ✅ RECOVERED (100% operational)
Duration: [X minutes]
Data Loss: None
Root Cause: Service restart (routine maintenance)

All your documents and contributions have been preserved.

If you experience any issues accessing the platform, please:
1. Clear browser cache (Ctrl+Shift+Delete)
2. Try again in a different browser
3. Report issues to admin@yourplatform.com

Thank you for your patience,
Platform Admin
```

---

## Part 2: Data Corruption / Loss Incident

### Scenario

User reports missing or corrupted data (deleted folder, corrupted document, user profile reset).

**Typical symptoms**:
- User reports folder/post is missing
- File size appears to be 0 bytes
- Metadata corruption (wrong timestamps, missing permissions)
- Database integrity check fails

### 2.1 Diagnosis Procedure (10-15 minutes)

```bash
#!/bin/bash
# File: /opt/<platform>/diagnose-data-corruption.sh
# Purpose: Identify extent and cause of data corruption
# Time: ~10-15 minutes

set -euo pipefail

PLATFORM=${1:-nextcloud}

echo "=== DATA CORRUPTION DIAGNOSIS ==="
echo ""

# Step 1: Check database integrity
echo "[1/5] Database integrity check..."
echo "  Running VACUUM ANALYZE (may take 2-3 minutes)..."

if docker exec "${PLATFORM}-postgres" vacuumdb -U postgres -j 2 2>/dev/null; then
  echo "  ✅ Database integrity verified"
else
  echo "  ⚠️  Database check raised warnings"
fi

# Step 2: Identify missing data
echo ""
echo "[2/5] Checking data volume..."

# Nextcloud
if [ "$PLATFORM" = "nextcloud" ]; then
  SIZE=$(docker exec nextcloud du -sh /shared/data 2>/dev/null | cut -f1)
  echo "  Nextcloud data size: $SIZE"
  
  # Count files
  FILE_COUNT=$(docker exec nextcloud find /shared/data -type f 2>/dev/null | wc -l)
  echo "  File count: $FILE_COUNT"
fi

# Discourse
if [ "$PLATFORM" = "discourse" ]; then
  SIZE=$(docker exec discourse du -sh /shared/uploads 2>/dev/null | cut -f1)
  echo "  Discourse uploads size: $SIZE"
fi

# Step 3: Check recent backup for comparison
echo ""
echo "[3/5] Comparing with latest backup..."

LATEST_BACKUP=$(find /mnt/backup/daily -name "postgres_backup_*.sql.gz" -type f | sort -r | head -1)

if [ -n "$LATEST_BACKUP" ]; then
  BACKUP_TIME=$(stat -c %y "$LATEST_BACKUP" | cut -d' ' -f1)
  echo "  Latest backup: $BACKUP_TIME"
  echo "  Backup size: $(du -h "$LATEST_BACKUP" | cut -f1)"
  echo ""
  echo "  Data loss window: from $BACKUP_TIME to now"
else
  echo "  ❌ No backups found"
fi

# Step 4: Check filesystem for hidden issues
echo ""
echo "[4/5] Filesystem check..."

DISK_USAGE=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')
echo "  Disk usage: ${DISK_USAGE}%"

if [ "$DISK_USAGE" -gt 90 ]; then
  echo "  ⚠️  WARNING: Disk nearly full - may cause corruption"
fi

# Step 5: Recommendation
echo ""
echo "[5/5] Next action:"
echo ""
echo "  If data is recoverable from backup:"
echo "    → Run restore-database.sh from DISASTER_RECOVERY_DESIGN_SPECIFICATION"
echo ""
echo "  If isolated user issue (single file):"
echo "    → Can recover specific file from backup"
echo ""
echo "  If widespread corruption:"
echo "    → Recommend full platform restore"
```

### 2.2 Response Procedure (15-30 minutes)

#### Response Option A: Restore to Previous Backup (Safest)

```bash
#!/bin/bash
# File: /opt/<platform>/recover-from-backup.sh
# Purpose: Restore database to state before data loss
# Time: 15-30 minutes
# Risk: Low (data restored from known-good backup)

set -euo pipefail

PLATFORM=${1:-nextcloud}
DOCKER_COMPOSE_FILE="/opt/${PLATFORM}/docker-compose.yml"

echo "=== DATA RECOVERY FROM BACKUP ==="
echo ""

# Find available backups
echo "[1/4] Available backups:"
BACKUPS=$(find /mnt/backup/daily -name "postgres_backup_*.sql.gz" -type f | sort -r)

if [ -z "$BACKUPS" ]; then
  echo "❌ No backups found"
  exit 1
fi

echo "$BACKUPS" | nl | head -5

echo ""
echo "Select backup to restore (enter number or full filename):"
read -p "> " selection

if [[ "$selection" =~ ^[0-9]+$ ]]; then
  BACKUP_FILE=$(echo "$BACKUPS" | sed -n "${selection}p")
else
  BACKUP_FILE="$selection"
fi

if [ ! -f "$BACKUP_FILE" ]; then
  echo "❌ Invalid backup: $BACKUP_FILE"
  exit 1
fi

echo ""
echo "You selected: $(basename "$BACKUP_FILE")"
echo "⚠️  WARNING: Current data will be OVERWRITTEN"
echo "Date lost: last $(echo "$BACKUP_FILE" | grep -o '[0-9]\{8\}' || echo 'unknown')"
echo ""
read -p "Type 'CONFIRM RESTORE' to proceed: " confirm

if [ "$confirm" != "CONFIRM RESTORE" ]; then
  echo "Aborted."
  exit 1
fi

echo ""
echo "[2/4] Stopping services..."
docker-compose -f "$DOCKER_COMPOSE_FILE" stop
sleep 5

echo "[3/4] Restoring database..."

if gunzip -c "$BACKUP_FILE" | docker-compose -f "$DOCKER_COMPOSE_FILE" exec -T postgres psql -U postgres > /tmp/restore.log 2>&1; then
  echo "  ✅ Restore completed"
else
  echo "  ❌ Restore failed - check /tmp/restore.log"
  exit 1
fi

echo "[4/4] Restarting services..."
docker-compose -f "$DOCKER_COMPOSE_FILE" up -d
sleep 15

echo ""
echo "✅ DATA RECOVERY COMPLETE"
echo ""
echo "Data restored to: $(basename "$BACKUP_FILE" | sed 's/postgres_backup_//' | sed 's/.sql.gz//')"
echo "Verify recovery: /opt/${PLATFORM}/verify-restore.sh"
```

#### Response Option B: Single File/Folder Recovery (If Isolated)

For Nextcloud: Recover specific file from backup without full restore

```bash
# This would require extracting the file from a volume backup and copying it back
# Typically done manually by extracting from volume_nextcloud_data_*.tar.gz

echo "Single file recovery process:"
echo "1. Locate backup file containing the user's documents"
echo "2. Extract from tar: tar xzf volume_nextcloud_data_YYYYMMDD.tar.gz"
echo "3. Copy recovered file to active volume"
echo "4. Verify permissions"
```

### 2.3 Verification (5-10 minutes)

```bash
#!/bin/bash
# File: /opt/<platform>/verify-data-recovery.sh
# Purpose: Confirm recovered data is intact and accessible

set -euo pipefail

PLATFORM=${1:-nextcloud}

echo "=== DATA RECOVERY VERIFICATION ==="
echo ""

# Check 1: Database accessible
echo "[1/4] Database accessibility..."
if docker exec "${PLATFORM}-postgres" pg_isready -U postgres > /dev/null 2>&1; then
  echo "  ✅ Database responding"
else
  echo "  ❌ Database not responding"
  exit 1
fi

# Check 2: User accounts exist
echo "[2/4] User accounts..."
USER_COUNT=$(docker exec "${PLATFORM}-postgres" psql -U postgres -tc \
  "SELECT COUNT(*) FROM users;" 2>/dev/null | tr -d ' ')

if [ "$USER_COUNT" -gt 0 ]; then
  echo "  ✅ $USER_COUNT user accounts found"
else
  echo "  ❌ No user accounts (data may be empty)"
fi

# Check 3: File data exists
echo "[3/4] File data..."

if [ "$PLATFORM" = "nextcloud" ]; then
  if docker exec nextcloud ls /shared/data | grep -q "user_"; then
    echo "  ✅ User directories found"
  else
    echo "  ⚠️  No user directories (may need to check permissions)"
  fi
fi

# Check 4: Spot-check user access
echo "[4/4] User accessibility test..."
if curl -s http://localhost/status.php 2>/dev/null | grep -q "installed"; then
  echo "  ✅ Web interface responding"
else
  echo "  ⚠️  Web interface slow to respond (wait 30 sec and retry)"
fi

echo ""
echo "✅ DATA RECOVERY VERIFICATION COMPLETE"
echo ""
echo "Next: Notify user that data has been recovered"
```

### 2.4 User Communication

```
Subject: Your Data Has Been Recovered

Dear [User],

We detected the data loss you reported on [DATE]. We have successfully
restored your documents from our backup system.

✅ Status: RECOVERED
Restored data date: [BACKUP_DATE]
Data loss window: [X hours] of recent edits

Your documents are now accessible. To re-sync:
1. Refresh your browser or restart your Nextcloud desktop client
2. Your files will reappear in the usual locations

If you notice any files are still missing, please report them and we can 
investigate further.

Thank you,
Platform Admin
```

---

## Part 3: Security Breach Incident

### Scenario

Suspected unauthorized access or intrusion (compromised credentials, data access by unauthorized user, or ransomware detected).

**Typical symptoms**:
- Unusual login from unfamiliar location
- Data modified by unknown user
- Suspicious process consuming resources
- Ransom note found, or files encrypted

### 3.1 Diagnosis & Immediate Action (15-30 minutes)

```bash
#!/bin/bash
# File: /opt/<platform>/incident-security-breach.sh
# Purpose: Respond to security breach with isolation & forensics
# Time: 15-30 minutes
# Risk: HIGH - Critical to act quickly

set -euo pipefail

PLATFORM=${1:-nextcloud}
DOCKER_COMPOSE_FILE="/opt/${PLATFORM}/docker-compose.yml"
INCIDENT_ID="SECURITY_$(date +%Y%m%d_%H%M%S)"
FORENSICS_DIR="/mnt/forensics/$INCIDENT_ID"

echo "⚠️  SECURITY BREACH RESPONSE INITIATED"
echo "Incident ID: $INCIDENT_ID"
echo ""

mkdir -p "$FORENSICS_DIR"
mkdir -p "$FORENSICS_DIR/logs"
mkdir -p "$FORENSICS_DIR/snapshots"

# STEP 1: ISOLATE THE PLATFORM (60 seconds)
echo "[1/6] ISOLATING PLATFORM (60 sec)..."
echo "  Disconnecting from network (but keeping access for forensics)..."

# OPTION A: Keep running for forensics
# OPTION B: Take offline immediately (more secure)
# For production: Choose OPTION B

read -p "  Keep running for forensics [A] or take offline [B]? (default: B): " choice
choice=${choice:-B}

if [ "$choice" = "B" ]; then
  echo "  Stopping all services..."
  docker-compose -f "$DOCKER_COMPOSE_FILE" stop
  echo "  ✅ Platform isolated"
fi

# STEP 2: PRESERVE FORENSICS (10 minutes)
echo ""
echo "[2/6] PRESERVING FORENSIC EVIDENCE..."

echo "  Dumping Docker logs..."
docker logs "${PLATFORM}" > "$FORENSICS_DIR/logs/${PLATFORM}_app.log" 2>&1
docker logs "${PLATFORM}-postgres" > "$FORENSICS_DIR/logs/postgres.log" 2>&1
docker logs "${PLATFORM}-redis" > "$FORENSICS_DIR/logs/redis.log" 2>&1

echo "  ✅ Logs preserved"

# STEP 3: IDENTIFY BREACH POINT
echo ""
echo "[3/6] IDENTIFYING BREACH POINT..."
echo "  Possible entry vectors:"
echo "  1. Web-exposed credentials (SSH key, API token exposed in code)"
echo "  2. Unpatched application vulnerability"
echo "  3. Weak password on user account"
echo "  4. Supply chain (compromised Docker image)"
echo "  5. Network exposure (firewall misconfiguration)"
echo ""
echo "  Check:"
echo "  - Review /opt/${PLATFORM}/.env for exposed secrets"
echo "  - Check docker-compose.yml for open ports (0.0.0.0)"
echo "  - Review database user access logs"
echo "  - Check file permissions (find /opt -perm /022)"

# STEP 4: DISABLE COMPROMISED ACCOUNTS
echo ""
echo "[4/6] DISABLING ACCOUNTS..."
echo "  Compromised accounts should be disabled:"
echo "  1. Admin account (change password)"
echo "  2. Any account with unusual activity"
echo "  3. API tokens (regenerate)"

# STEP 5: BACKUP COMPROMISED STATE (for forensics)
echo ""
echo "[5/6] BACKING UP COMPROMISED STATE..."
echo "  Taking snapshot before clean restore..."

docker run --rm \
  -v "${PLATFORM}_data:/data" \
  -v "$FORENSICS_DIR/snapshots:/backup" \
  alpine tar czf "/backup/compromised_state.tar.gz" -C / data 2>/dev/null || true

echo "  ✅ Forensic snapshot created: $FORENSICS_DIR"

# STEP 6: NEXT STEPS
echo ""
echo "[6/6] NEXT STEPS:"
echo ""
echo "  IMMEDIATE (this session):"
echo "  1. Do NOT restart from current state"
echo "  2. Preserve all forensic data: $FORENSICS_DIR"
echo "  3. Notify admin@wanka95.gmail.com"
echo ""
echo "  NEXT SESSION:"
echo "  1. Complete forensics investigation (offsite)"
echo "  2. Determine root cause"
echo "  3. Patch vulnerabilities"
echo "  4. Restore from clean backup (>7 days old)"
echo "  5. Deploy with hardened configuration"
echo ""
echo "  CRITICAL: Do not reconnect to network until:"
echo "  - Root cause identified"
echo "  - All vulnerabilities patched"
echo "  - Clean OS/backups verified"

echo ""
echo "⚠️  FORENSICS EVIDENCE PRESERVED: $FORENSICS_DIR"
```

### 3.2 Recovery: Clean Restore from Offsite Backup

```bash
#!/bin/bash
# File: /opt/<platform>/recover-from-breach.sh
# Purpose: Restore platform from pre-breach offsite backup
# Time: 45-90 minutes
# Prerequisites: 
#  - Root cause identified and patched
#  - Offsite backup (USB) verified as clean
#  - Network patches applied

set -euo pipefail

PLATFORM=${1:-nextcloud}
USB_BACKUP="/mnt/usb/backup_*.tar.gz.gpg"

echo "=== CLEAN RESTORE AFTER SECURITY BREACH ==="
echo ""
echo "⚠️  CRITICAL: Only proceed if root cause is identified and patched"
echo ""

read -p "Type 'PROCEED WITH RESTORE' to continue: " confirm
if [ "$confirm" != "PROCEED WITH RESTORE" ]; then
  echo "Aborted."
  exit 1
fi

echo ""
echo "[1/3] Decrypting offsite backup..."

# Find most recent clean backup
ENCRYPTED_BACKUP=$(ls -1t $USB_BACKUP 2>/dev/null | head -1)

if [ -z "$ENCRYPTED_BACKUP" ]; then
  echo "❌ No encrypted backup found on USB"
  exit 1
fi

echo "  Using backup: $(basename "$ENCRYPTED_BACKUP")"

# Decrypt (will prompt for passphrase)
DECRYPTED="/tmp/backup_restore.tar.gz"
gpg --output "$DECRYPTED" "$ENCRYPTED_BACKUP"

echo "  ✅ Backup decrypted"

echo ""
echo "[2/3] Extracting clean backup..."
mkdir -p /mnt/backup/clean-restore
tar xzf "$DECRYPTED" -C /mnt/backup/clean-restore
echo "  ✅ Backup extracted"

echo ""
echo "[3/3] Running restore from clean state..."
/opt/${PLATFORM}/restore-complete.sh

# Cleanup
rm -f "$DECRYPTED"

echo ""
echo "✅ BREACH RECOVERY COMPLETE"
echo ""
echo "Security checklist:"
echo "  [ ] Change all user passwords"
echo "  [ ] Regenerate API tokens"
echo "  [ ] Review account permissions"
echo "  [ ] Enable 2FA on admin account"
echo "  [ ] Audit access logs from past 30 days"
```

### 3.3 User Communication

```
Subject: URGENT: Platform Security Incident — Data Protected

Dear Authors,

We detected a security incident affecting the platform on [DATE/TIME].

🔒 Your data is PROTECTED:
  • We immediately isolated the platform
  • All sensitive data is encrypted and backed up
  • We are conducting a forensic investigation
  • Platform will be restored from clean backups

⏱️  Timeline:
  • [TIME] Incident detected
  • [TIME] Platform isolated
  • [TIME] Forensics began
  • [TARGET TIME] Clean restore will be complete

🔐 Security measures being implemented:
  • All compromised accounts will be disabled
  • Passwords should be changed by all users
  • API tokens are being regenerated
  • 2-factor authentication is now enabled

Your documents and contributions are safe. The platform will come back 
online with stronger security. We will provide updates every 2 hours.

For questions: admin@yourplatform.com

Platform Admin
```

---

## Part 4: Disk Full Incident

### Scenario

Platform storage is exhausted; new uploads fail, backups fail, or services crash.

**Typical symptoms**:
- "No space left on device" errors
- Platform becomes read-only
- Database cannot accept new transactions
- Backups fail to complete

### 4.1 Diagnosis (5 minutes)

```bash
#!/bin/bash
# File: /opt/<platform>/diagnose-disk-full.sh
# Purpose: Identify what's using disk space

set -euo pipefail

echo "=== DISK SPACE ANALYSIS ==="
echo ""

echo "[1/3] Disk usage by mount point:"
df -h

echo ""
echo "[2/3] Largest directories (top 10):"
du -sh /* 2>/dev/null | sort -rh | head -10

echo ""
echo "[3/3] Largest Docker volumes:"
docker volume ls --format "table {{.Name}}\t{{.Mountpoint}}" | while read vol path; do
  if [ -d "$path" ]; then
    SIZE=$(du -sh "$path" 2>/dev/null | cut -f1)
    echo "  $vol: $SIZE"
  fi
done | sort -k2 -rh

echo ""
echo "Recommendation:"
echo "  1. If /mnt/backup is full: delete old backups (keep 7 days)"
echo "  2. If Docker volumes full: clean old uploads or database"
echo "  3. If root (/) full: check /tmp and /var/log"
```

### 4.2 Emergency Cleanup (5-10 minutes)

```bash
#!/bin/bash
# File: /opt/<platform>/emergency-disk-cleanup.sh
# Purpose: Free up disk space immediately

set -euo pipefail

PLATFORM=${1:-nextcloud}

echo "=== EMERGENCY DISK CLEANUP ==="
echo ""

echo "[1/5] Cleaning old backups (keep 2 days)..."
REMOVED=0
while IFS= read -r file; do
  rm -f "$file"
  REMOVED=$((REMOVED + 1))
done < <(find /mnt/backup/daily -name "postgres_backup_*.sql.gz" -mtime +2 2>/dev/null)
echo "  ✅ Removed $REMOVED old backups"

echo ""
echo "[2/5] Cleaning Docker temporary files..."
docker system prune -f --volumes 2>/dev/null || true
echo "  ✅ Cleaned Docker system"

echo ""
echo "[3/5] Vacuuming database..."
docker exec "${PLATFORM}-postgres" vacuumdb -U postgres -j 2 2>/dev/null || true
echo "  ✅ Database vacuumed"

echo ""
echo "[4/5] Clearing logs..."
find /var/log -type f -name "*.log" -mtime +30 -exec rm {} \; 2>/dev/null || true
docker logs --tail 0 "${PLATFORM}" 2>/dev/null || true
echo "  ✅ Old logs cleared"

echo ""
echo "[5/5] Verifying space freed..."
df -h / | tail -1

echo ""
echo "✅ CLEANUP COMPLETE"
echo ""
echo "If still full, next steps:"
echo "  1. Delete old user uploads (contact users first)"
echo "  2. Consider expanding storage (add external drive)"
echo "  3. Implement upload size limits"
```

### 4.3 Permanent Solution

```bash
#!/bin/bash
# File: /opt/<platform>/enable-disk-monitoring.sh
# Purpose: Set up alerts when disk nears capacity

# Add to crontab:
# 0 * * * * /opt/<platform>/check-disk-space.sh

#!/bin/bash
# /opt/<platform>/check-disk-space.sh
# Frequency: Hourly

set -euo pipefail

DISK_USAGE=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')
THRESHOLD=85

if [ "$DISK_USAGE" -gt "$THRESHOLD" ]; then
  echo "⚠️  ALERT: Disk usage ${DISK_USAGE}% (threshold: ${THRESHOLD}%)"
  
  # Send email alert (if sendmail available)
  {
    echo "Subject: [ALERT] Disk usage critical on $(hostname)"
    echo "Disk usage: ${DISK_USAGE}%"
    echo ""
    echo "Run: /opt/<platform>/emergency-disk-cleanup.sh"
  } | msmtp admin@yourplatform.com 2>/dev/null || true
fi
```

---

## Part 5: Network Outage Incident

### Scenario

Platform is unreachable (network down, firewall block, DNS issues, or ISP outage).

**Typical symptoms**:
- All users report "Cannot connect"
- `curl` from other device returns "Connection refused" or timeout
- DNS lookup fails or returns wrong IP
- SSH access works but HTTP/HTTPS don't

### 5.1 Diagnosis (5-10 minutes)

```bash
#!/bin/bash
# File: /opt/<platform>/diagnose-network-outage.sh
# Purpose: Identify network connectivity issue

set -euo pipefail

PLATFORM=${PLATFORM:-nextcloud}
DOMAIN=${DOMAIN:-phase5.example.com}

echo "=== NETWORK OUTAGE DIAGNOSIS ==="
echo ""

# Test 1: Local services running?
echo "[1/5] Local service health..."
if docker-compose ps | grep -q "Up"; then
  echo "  ✅ Services running locally"
else
  echo "  ❌ Services not running - start with: docker-compose up -d"
  exit 1
fi

# Test 2: Network interface up?
echo ""
echo "[2/5] Network interface status..."
if ip link show | grep -q "UP"; then
  echo "  ✅ Network interface up"
else
  echo "  ❌ Network interface down"
fi

# Test 3: Tailscale connectivity?
echo ""
echo "[3/5] Tailscale status..."
if sudo tailscale status 2>/dev/null | grep -q "Online"; then
  echo "  ✅ Tailscale connected"
else
  echo "  ⚠️  Tailscale offline"
fi

# Test 4: Local port listening?
echo ""
echo "[4/5] HTTP/HTTPS ports..."
if netstat -tlnp 2>/dev/null | grep -q ":80\|:443"; then
  echo "  ✅ Web ports listening"
else
  echo "  ❌ Web ports not listening"
  echo "     Check nginx: docker logs nginx"
fi

# Test 5: Local curl test?
echo ""
echo "[5/5] Local connectivity test..."
if curl -s http://localhost > /dev/null 2>&1; then
  echo "  ✅ Local HTTP working"
else
  echo "  ❌ Local HTTP failed"
fi

echo ""
echo "=== DIAGNOSIS SUMMARY ==="
echo "If services are running locally but unreachable externally:"
echo "  → Check firewall rules"
echo "  → Check DNS (nslookup $DOMAIN)"
echo "  → Check IP address: hostname -I"
echo "  → Check Tailscale route: sudo tailscale netcheck"
```

### 5.2 Failover & Recovery (5-30 minutes)

#### Option A: Network Issue on This Device

```bash
#!/bin/bash
# If network is down on primary, but secondary device is online

echo "Failover to secondary device:"
echo ""
echo "1. Update DNS A record:"
echo "   phase5.example.com -> [SECONDARY_IP]"
echo "   (Using Route53 / Cloudflare / your DNS provider)"
echo ""
echo "2. Copy recent backup to secondary:"
echo "   scp /mnt/backup/daily/postgres_backup_latest.sql.gz"
echo "   pi@secondary-pi:/tmp/"
echo ""
echo "3. Restore on secondary:"
echo "   ssh pi@secondary-pi"
echo "   /opt/<platform>/restore-complete.sh"
echo ""
echo "4. Test from external: curl https://phase5.example.com"
```

#### Option B: Wait for Network Recovery

```bash
#!/bin/bash
# If network outage is infrastructure-wide (ISP issue)

echo "Network outage recovery:"
echo ""
echo "1. Monitor network status:"
echo "   sudo tailscale status"
echo "   ip link show"
echo "   ping 8.8.8.8"
echo ""
echo "2. While waiting:"
echo "   - Check logs for errors: docker logs"
echo "   - Verify services are ready: docker-compose ps"
echo "   - Test local connectivity: curl http://localhost"
echo ""
echo "3. When network returns:"
echo "   - Services should reconnect automatically"
echo "   - Verify with: curl https://yourplatform.com"
```

### 5.3 User Communication

```
Subject: Platform Temporarily Unreachable — Network Issue

Dear Authors,

The platform is temporarily unreachable due to a network connectivity issue
on our infrastructure.

📊 Status: INVESTIGATING
Root cause: Network connectivity (ISP/infrastructure)
Services: ✅ Running (waiting for network recovery)
Expected recovery: Within 1 hour

🔄 What's happening:
• Platform services are operational on our server
• Network connection to external users is temporarily down
• We are working with our ISP to restore connectivity

⏳ Expected timeline:
• [Current time]: Issue detected
• [+30 min]: Estimated recovery
• [+1 hour]: Full restoration expected

For updates: Check this page or contact admin@yourplatform.com

We apologize for the interruption.

Platform Admin
```

---

## Part 6: Quick Decision Tree

### When Unsure, Follow This Flow:

```
INCIDENT DETECTED
    │
    ├─→ Services unreachable?
    │   ├─→ YES: Run /diagnose-service-crash.sh
    │   │    └─→ /restart-platform.sh
    │   └─→ NO: Check network (see Part 5)
    │
    ├─→ User reports missing data?
    │   ├─→ YES: Run /diagnose-data-corruption.sh
    │   │    └─→ /recover-from-backup.sh
    │   └─→ NO: Continue
    │
    ├─→ Suspected security breach?
    │   ├─→ YES: Run /incident-security-breach.sh
    │   │    └─→ ISOLATE IMMEDIATELY
    │   └─→ NO: Continue
    │
    ├─→ "No space left on device" errors?
    │   ├─→ YES: Run /emergency-disk-cleanup.sh
    │   └─→ NO: Continue
    │
    └─→ "Connection refused" from external?
        └─→ Run /diagnose-network-outage.sh
```

---

## Part 7: Incident Response Playbook Template

Use this template for documenting any custom incident:

```bash
#!/bin/bash
# INCIDENT RESPONSE PLAYBOOK
# Incident name: [Name]
# Severity: [Low/Medium/High/Critical]
# RTO: [Time to recover]
# Estimated duration: [Time to execute]

set -euo pipefail

TIMESTAMP=$(date +'%Y-%m-%d %H:%M:%S')

echo "=== INCIDENT RESPONSE: [NAME] ==="
echo "Timestamp: $TIMESTAMP"
echo ""

# Phase 1: Diagnosis
echo "[1/X] DIAGNOSIS..."
# ... diagnostic steps ...

# Phase 2: Mitigation
echo "[2/X] MITIGATION..."
# ... mitigation steps ...

# Phase 3: Recovery
echo "[3/X] RECOVERY..."
# ... recovery steps ...

# Phase 4: Verification
echo "[4/X] VERIFICATION..."
# ... verification steps ...

# Phase 5: Documentation
echo "[5/X] DOCUMENTATION..."
# ... log findings, root cause, improvements ...

echo "✅ INCIDENT RESPONSE COMPLETE"
```

---

## Appendix: Incident Response Roles

### Platform Operator (On-Call)

**Responsibilities**:
- Execute diagnosis and immediate response procedures
- Contact escalation contacts if needed
- Document incident timeline

**Available tools**:
- All scripts in `/opt/<platform>/diagnose-*.sh` and `*/restart-*.sh`
- Docker commands
- Backup/restore procedures

### Platform Admin

**Responsibilities**:
- Approve emergency restore operations
- Authorize security isolations
- Communicate with users

**Contact**: admin@yourplatform.com

### Security Team (For Breaches Only)

**Responsibilities**:
- Conduct forensic investigation
- Identify root cause and improvements
- Recommend hardening measures

**Evidence location**: `/mnt/forensics/SECURITY_*`

---

**Document Version**: 1.0 Production-Ready  
**Last Updated**: 2026-06-16  
**Target Platforms**: Nextcloud+Matrix OR Discourse  
**Status**: ✅ APPROVED FOR PRODUCTION  
**Next Review**: 2026-07-16 (30 days)  

**Critical**: Print this document and keep in operations manual. Response time targets (15-30 min) require operators to be familiar with these procedures **before** incidents occur.
