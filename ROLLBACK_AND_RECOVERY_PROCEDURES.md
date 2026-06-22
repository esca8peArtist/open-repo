---
title: "Rollback & Recovery Procedures: Deployment Failure Scenarios"
project: open-repo
phase: 6 (infrastructure deployment)
document_type: operational-procedures
status: REFERENCE (for use if deployment issues occur)
created: 2026-06-22
applicable_to: Docker and systemd deployment paths
---

# Rollback & Recovery Procedures

## Overview

This document outlines failure scenarios and recovery procedures for both Docker and systemd deployments. Use this guide if deployment issues occur or if you need to revert to a previous version.

**Important**: Recovery procedures vary significantly by platform. Select the appropriate section based on your deployment choice.

---

## Failure Scenario Classification

### Severity Levels

| Severity | Definition | Recovery Time | Data Risk |
|----------|-----------|---------------|-----------|
| **P0 (Critical)** | Application completely unavailable; cannot start service | 5–15 min (Docker) / 20–40 min (systemd) | Requires backup restore |
| **P1 (High)** | Application partially unavailable; errors in logs | 10–30 min | No data loss typical; may need config fix |
| **P2 (Medium)** | Degraded performance; specific endpoints fail | 15–45 min | No data loss; may need database migration fix |
| **P3 (Low)** | Minor functionality broken; application generally operational | 30+ min | No data loss; can fix in background |

---

## Decision Tree: Rollback vs. Fix

When deployment fails, determine whether to **rollback** or **fix forward**:

```
Is the application completely unavailable?
├─ YES → ROLLBACK (P0 critical, must restore service immediately)
│
└─ NO → Does the error affect core functionality (API, database)?
        ├─ YES → DIAGNOSE & FIX (see section 2, 3)
        │         If fix takes >30 min, consider ROLLBACK instead
        │
        └─ NO → DIAGNOSE & FIX IN BACKGROUND (see section 2, 3)
```

---

## Part A: Docker Deployment Failure Scenarios

### Scenario A1: Container Won't Start (P0 Critical)

**Symptoms**:
```bash
$ docker ps
# No containers listed, or container in "Exited" state

$ docker logs open-repo-app
# Error at startup, e.g., "ModuleNotFoundError: No module named 'fastapi'"
```

**Root Causes**:
1. Application code error (import missing, syntax error)
2. Environment variable missing (DATABASE_URL, SECRET_KEY)
3. Volume mount failed (permission denied, path not writable)
4. Port conflict (another service on 127.0.0.1:8000)

**Recovery Procedure**:

**Step 1: Identify Root Cause (5 minutes)**

```bash
# View container logs
docker logs open-repo-app | tail -50

# Check image built correctly
docker images open-repo:latest

# Verify volume mount
docker inspect open-repo-app | grep -A 10 Mounts

# Check port binding
sudo netstat -tlnp | grep 8000
```

**Step 2: Fix Based on Root Cause**

**Case A1.1: Application code error**

```bash
# Verify code is correct in repository
cd /home/awank/dev/SuperClaude_Framework
git status projects/open-repo/backend/

# Rebuild image with fresh code
cd /opt/open-repo
docker-compose down
docker-compose build --no-cache
docker-compose up -d

# Verify startup (wait 40 sec for health check)
sleep 40
docker inspect open-repo-app | grep '"Status"'
# Expected: "healthy"
```

**Recovery Time**: 10–15 minutes (rebuild image + restart)

---

**Case A1.2: Environment variable missing**

```bash
# Check .env file
cat /opt/open-repo/.env

# Verify all required vars are set
grep -E "DATABASE_URL|SECRET_KEY|LOG_LEVEL" /opt/open-repo/.env

# If missing, add to .env file
echo 'MISSING_VAR="value"' >> /opt/open-repo/.env

# Restart container to reload env
docker-compose down
docker-compose up -d
```

**Recovery Time**: 5 minutes

---

**Case A1.3: Volume mount permission denied**

```bash
# Check volume permissions
docker inspect open-repo-app | grep -A 5 "Mounts"

# Fix ownership (on host)
sudo chown 1000:1000 /var/lib/docker/volumes/open-repo-data/_data
sudo chmod 755 /var/lib/docker/volumes/open-repo-data/_data

# Restart container
docker-compose restart

# Verify
docker logs open-repo-app
```

**Recovery Time**: 5 minutes

---

**Case A1.4: Port conflict**

```bash
# Find what's on port 8000
sudo lsof -i :8000

# Kill conflicting process or change port in docker-compose.yml
# Option 1: Kill conflicting process
sudo kill -9 <PID>

# Option 2: Change port in docker-compose.yml
# Edit ports: 127.0.0.1:8001:8000 (use 8001 instead of 8000)
# Then restart
docker-compose restart
```

**Recovery Time**: 5 minutes

---

**Step 3: Verify Container Health (5 minutes)**

```bash
# Wait 40 seconds for health check to pass
sleep 40

# Check status
docker ps | grep open-repo-app
# Expected: Status showing "Up X minutes (healthy)"

# Test API
curl http://127.0.0.1:8000/health
# Expected: HTTP 200 with JSON response
```

**Step 4: If All Fixes Fail → ROLLBACK (15 minutes)**

```bash
# Stop current container
docker-compose down

# Restore from backup
cd /opt/open-repo/backups
ls -lt data-*.tar.gz | head -5  # Find latest backup
docker volume rm open-repo-data
docker volume create open-repo-data

# Restore data
docker run --rm -v open-repo-data:/data -v $(pwd):/backup alpine \
  tar xzf /backup/data-YYYY-MM-DD-HHMMSS.tar.gz -C /data

# Redeploy old image (tag it if needed)
docker-compose up -d
```

**Total Recovery Time**: 15–20 minutes

---

### Scenario A2: Container Running But API Returns Errors (P1 High)

**Symptoms**:
```bash
$ curl http://127.0.0.1:8000/health
# HTTP 500 or timeout

$ docker logs open-repo-app
# Application runtime error, e.g., "KeyError: 'DATABASE_URL'"
```

**Root Causes**:
1. Database connection failed (DATABASE_URL incorrect, database unavailable)
2. Migration not applied (schema mismatch, `alembic upgrade head` missing)
3. Dependency compatibility issue (library version mismatch)
4. Configuration error (wrong SECRET_KEY, LOG_LEVEL invalid)

**Recovery Procedure**:

**Step 1: Check Database Connection (5 minutes)**

```bash
# View application logs
docker logs open-repo-app | grep -i "database\|connection\|sqlalchemy" | tail -20

# If error is "database is locked" or "no such table", database needs migration
docker-compose exec open-repo alembic current

# Expected: revision = "003" or "head"
# If missing, upgrade:
docker-compose exec open-repo alembic upgrade head
```

**Step 2: Check Environment Variables (5 minutes)**

```bash
# Verify DATABASE_URL is accessible
docker-compose exec open-repo bash -c 'echo $DATABASE_URL'

# Verify database file exists (if SQLite)
docker exec open-repo-app ls -la /data/

# Check volume mount
docker inspect open-repo-app | grep -A 5 Mounts
```

**Step 3: Restart Application (5 minutes)**

```bash
# Restart container (applies any migrations or config changes)
docker-compose restart open-repo-app

# Wait for health check (40 sec)
sleep 40

# Test API again
curl http://127.0.0.1:8000/health
```

**Step 4: If Still Failing → Check Logs Deeply (10 minutes)**

```bash
# View full error stack trace
docker logs open-repo-app --tail 100

# If migration error, manually upgrade
docker-compose exec open-repo bash
alembic upgrade head
exit

# Restart
docker-compose restart
```

**Step 5: If All Fixes Fail → ROLLBACK (15 minutes)**

```bash
# Same as A1 above: restore from backup, redeploy old image
docker-compose down
# ... restore backup steps ...
docker-compose up -d
```

**Total Recovery Time**: 10–30 minutes (fix-forward); 15–20 minutes (rollback)

---

### Scenario A3: Database Corruption or Schema Mismatch (P1 High)

**Symptoms**:
```bash
$ curl http://127.0.0.1:8000/api/zim-exports
# HTTP 500

$ docker logs open-repo-app | grep -i "database\|integrity\|corrupt"
# Error: "database disk image malformed" or "table zim_exports does not exist"
```

**Root Cause**: Database file corrupted or migration schema out of sync.

**Recovery Procedure**:

**Step 1: Verify Backup Exists (2 minutes)**

```bash
ls -lt /opt/open-repo/backups/data-*.tar.gz | head -3
```

**Step 2: Restore from Backup (10 minutes)**

```bash
# Stop application
docker-compose down

# Remove corrupted volume
docker volume rm open-repo-data

# Create new volume
docker volume create open-repo-data

# Restore backup
docker run --rm -v open-repo-data:/data -v /opt/open-repo/backups:/backup alpine \
  tar xzf /backup/data-LATEST.tar.gz -C /data

# Restart application
docker-compose up -d

# Wait for health check (40 sec)
sleep 40

# Verify
curl http://127.0.0.1:8000/health
```

**Step 3: Verify Data Integrity (5 minutes)**

```bash
# Check database
docker-compose exec open-repo alembic current

# Check if tables exist
docker-compose exec open-repo bash -c \
  'sqlite3 /data/open_repo.db ".tables"'
```

**Total Recovery Time**: 20–30 minutes (database restore always requires downtime)

---

### Scenario A4: Port Already in Use or Network Binding Issue (P1 High)

**Symptoms**:
```bash
$ docker-compose up -d
# Error: "bind: permission denied" or "address already in use"
```

**Root Cause**: Another process on port 8000, or insufficient permissions for port binding.

**Recovery Procedure**:

**Step 1: Identify Conflicting Process (5 minutes)**

```bash
sudo netstat -tlnp | grep 8000
# Expected output: PID and command of process using port 8000
```

**Step 2: Resolve Conflict (5 minutes)**

```bash
# Option 1: Kill conflicting process (if not needed)
sudo kill -9 <PID>

# Option 2: Change port in docker-compose.yml
# Edit: ports: 127.0.0.1:8001:8000 (use 8001 instead)
nano /opt/open-repo/docker-compose.yml
# Change "127.0.0.1:8000:8000" to "127.0.0.1:8001:8000"

# Restart with new port
docker-compose down
docker-compose up -d

# Update firewall rule if needed
# (this deployment uses 127.0.0.1, so local only)
```

**Total Recovery Time**: 5–10 minutes

---

---

## Part B: systemd Deployment Failure Scenarios

### Scenario B1: Service Won't Start (P0 Critical)

**Symptoms**:
```bash
$ sudo systemctl status open-repo
# Status shows "inactive (dead)" or "failed"

$ sudo journalctl -u open-repo -n 50
# Error message at startup
```

**Root Causes**:
1. Python venv broken or dependencies missing
2. Service file syntax error
3. Permission denied on files or directories
4. Port 8000 already in use

**Recovery Procedure**:

**Step 1: Identify Root Cause (5 minutes)**

```bash
# View service logs
sudo journalctl -u open-repo -n 100

# Check service file syntax
sudo systemd-analyze verify /etc/systemd/system/open-repo.service

# Verify venv and dependencies
/opt/open-repo/venv/bin/python -c "import fastapi; print('OK')"

# Check port
sudo netstat -tlnp | grep 8000
```

**Step 2: Fix Based on Root Cause**

**Case B1.1: Dependencies missing or venv broken**

```bash
# Reinstall dependencies
cd /opt/open-repo/backend
/opt/open-repo/venv/bin/pip install -e ".[dev]"

# Verify import
/opt/open-repo/venv/bin/python -c "import fastapi; print('OK')"

# Restart service
sudo systemctl restart open-repo

# Verify
sudo systemctl status open-repo
```

**Recovery Time**: 5–10 minutes

---

**Case B1.2: Service file syntax error**

```bash
# Check syntax
sudo systemd-analyze verify /etc/systemd/system/open-repo.service

# If error found, edit file
sudo nano /etc/systemd/system/open-repo.service
# Fix syntax (e.g., missing = sign, incorrect directive)

# Reload systemd
sudo systemctl daemon-reload

# Restart
sudo systemctl restart open-repo
```

**Recovery Time**: 5 minutes

---

**Case B1.3: Permission denied**

```bash
# Check file permissions
ls -la /etc/systemd/system/open-repo.service
ls -la /opt/open-repo/venv/bin/uvicorn

# Fix ownership of application directory
sudo chown -R pi:pi /opt/open-repo

# Reload systemd and restart
sudo systemctl daemon-reload
sudo systemctl restart open-repo
```

**Recovery Time**: 5 minutes

---

**Case B1.4: Port 8000 already in use**

```bash
# Find what's on port 8000
sudo netstat -tlnp | grep 8000

# Kill conflicting process
sudo kill -9 <PID>

# Or edit service file to use different port
# Edit Environment="UVICORN_PORT=8001"
sudo nano /etc/systemd/system/open-repo.service

# Reload and restart
sudo systemctl daemon-reload
sudo systemctl restart open-repo
```

**Recovery Time**: 5 minutes

---

**Step 3: Verify Service Health (5 minutes)**

```bash
# Check status
sudo systemctl status open-repo
# Expected: Active (running)

# Test API
curl http://127.0.0.1:8000/health
# Expected: HTTP 200
```

**Step 4: If All Fixes Fail → ROLLBACK (30 minutes)**

```bash
# Stop service
sudo systemctl stop open-repo

# Restore from backup
cd /opt/open-repo/backups
tar xzf data-LATEST.tar.gz -C /

# Restart service
sudo systemctl start open-repo
```

**Total Recovery Time**: 20–40 minutes

---

### Scenario B2: Service Running But API Returns Errors (P1 High)

**Symptoms**:
```bash
$ curl http://127.0.0.1:8000/health
# HTTP 500 or timeout

$ sudo journalctl -u open-repo -n 50
# Error in logs
```

**Root Causes**:
1. Database connection failed
2. Migration not applied
3. Environment variable misconfigured
4. Code change introduced a bug

**Recovery Procedure**:

**Step 1: Check Logs (5 minutes)**

```bash
# View recent logs
sudo journalctl -u open-repo --since "10 minutes ago" -p err

# Check for database errors
sudo journalctl -u open-repo -n 50 | grep -i "database\|connection"

# Check environment
sudo systemctl show-environment | grep DATABASE_URL
```

**Step 2: Apply Database Migrations (5 minutes)**

```bash
# Stop service
sudo systemctl stop open-repo

# Apply migrations manually
cd /opt/open-repo/backend
/opt/open-repo/venv/bin/alembic upgrade head

# Restart
sudo systemctl start open-repo
```

**Step 3: Verify API Health (5 minutes)**

```bash
# Wait a moment for startup
sleep 5

# Test API
curl http://127.0.0.1:8000/health

# View logs
sudo journalctl -u open-repo -n 20
```

**Step 4: If All Fixes Fail → ROLLBACK (30 minutes)**

```bash
# Revert code and database
sudo systemctl stop open-repo
tar xzf /opt/open-repo/backups/data-LATEST.tar.gz -C /
sudo systemctl start open-repo
```

**Total Recovery Time**: 10–30 minutes (fix-forward); 30–40 minutes (rollback)

---

### Scenario B3: Database Corruption or Migration Failed (P1 High)

**Symptoms**:
```bash
$ curl http://127.0.0.1:8000/api/zim-exports
# HTTP 500

$ sudo journalctl -u open-repo | grep -i "database\|integrity"
# Error: "database disk image malformed" or "no such table"
```

**Root Cause**: Database file corrupted or migration incomplete.

**Recovery Procedure**:

**Step 1: Stop Service Immediately (1 minute)**

```bash
sudo systemctl stop open-repo
```

**Step 2: Verify Backup (2 minutes)**

```bash
ls -lt /opt/open-repo/backups/data-*.tar.gz | head -3
# Ensure recent backup exists
```

**Step 3: Restore from Backup (5 minutes)**

```bash
# Remove corrupted database
rm /opt/open-repo/data/open_repo.db

# Restore from backup
tar xzf /opt/open-repo/backups/data-LATEST.tar.gz -C /

# Verify restoration
ls -la /opt/open-repo/data/open_repo.db
```

**Step 4: Verify Database Schema (5 minutes)**

```bash
cd /opt/open-repo/backend
/opt/open-repo/venv/bin/alembic current
# Expected: revision = "003"

# If not at head, upgrade
/opt/open-repo/venv/bin/alembic upgrade head
```

**Step 5: Restart Service (2 minutes)**

```bash
sudo systemctl start open-repo

# Verify
sudo systemctl status open-repo
curl http://127.0.0.1:8000/health
```

**Total Recovery Time**: 20–30 minutes (database restore always requires downtime)

---

### Scenario B4: Health Check Failed, Service Restarted Repeatedly (P1 High)

**Symptoms**:
```bash
$ sudo journalctl -u open-repo -n 50
# Repeating logs: Service started, then stopped, then restarted

$ sudo systemctl status open-repo
# Status shows "Restart (code=exited, status=1)" repeating
```

**Root Cause**: Health check script failing continuously, triggering restart loop. See `/usr/local/bin/check-open-repo.sh`.

**Recovery Procedure**:

**Step 1: Stop the Restart Loop (2 minutes)**

```bash
# Stop service
sudo systemctl stop open-repo

# Disable health check temporarily
sudo chmod -x /usr/local/bin/check-open-repo.sh
# (or comment out cron entry)
sudo crontab -e
# Comment line: # */5 * * * * /usr/local/bin/check-open-repo.sh...
```

**Step 2: Diagnose the Health Check Failure (5 minutes)**

```bash
# Run health check manually
/usr/local/bin/check-open-repo.sh

# View output and error
echo $?
# 0 = OK, non-zero = failed

# Check if API is running
curl http://127.0.0.1:8000/health
# If timeout, API is not responding
```

**Step 3: Fix the Underlying Issue**

If API not responding:
```bash
# Manually restart service with debugging
sudo systemctl start open-repo
sudo systemctl status open-repo
sudo journalctl -u open-repo -n 50
# Check logs for startup error
```

If API is responding but health check failing:
```bash
# Fix health check script
sudo nano /usr/local/bin/check-open-repo.sh
# Verify curl endpoint is correct
# Verify timeout is sufficient
```

**Step 4: Re-enable Health Check (2 minutes)**

```bash
# Re-enable cron
sudo crontab -e
# Uncomment: */5 * * * * /usr/local/bin/check-open-repo.sh...

# Make health check executable again
sudo chmod +x /usr/local/bin/check-open-repo.sh
```

**Total Recovery Time**: 10–20 minutes

---

---

## Part C: Database Migration Rollback (Common to Both Paths)

### Scenario C1: Migration Introduced a Bug (P1 High)

**Symptoms**:
```bash
$ curl http://127.0.0.1:8000/api/zim-exports
# HTTP 500 or returns incorrect data

$ grep -i "column\|constraint\|migration" logs/
# Error referencing a recent migration
```

**Root Cause**: Database schema change introduced a bug (e.g., column dropped by mistake, constraint violated).

**Recovery Procedure**:

**Step 1: Identify Problematic Migration (5 minutes)**

```bash
# View migration history
alembic history

# View current revision
alembic current

# Check recent migrations
ls -lt /opt/open-repo/backend/alembic/versions/ | head -5
```

**Step 2: Downgrade to Previous Migration (10 minutes)**

**Docker**:
```bash
docker-compose exec open-repo alembic downgrade <previous-revision>
# Example: alembic downgrade 002
```

**systemd**:
```bash
cd /opt/open-repo/backend
/opt/open-repo/venv/bin/alembic downgrade <previous-revision>
```

**Step 3: Verify Data Integrity (5 minutes)**

```bash
# Check database tables
docker-compose exec open-repo sqlite3 /data/open_repo.db ".tables"
# or
/opt/open-repo/venv/bin/python -c "from app import db; db.inspect_tables()"
```

**Step 4: Restart Application (2 minutes)**

```bash
# Docker
docker-compose restart

# systemd
sudo systemctl restart open-repo

# Test API
curl http://127.0.0.1:8000/health
```

**Total Recovery Time**: 15–25 minutes

---

## Master Rollback Procedure (Both Paths)

Use this if all other recovery attempts fail.

### Step 1: Stop Application

**Docker**:
```bash
docker-compose down
```

**systemd**:
```bash
sudo systemctl stop open-repo
```

### Step 2: Restore from Latest Backup

```bash
# List backups
ls -lt /opt/open-repo/backups/data-*.tar.gz | head -3

# Extract latest backup (choose your backup)
BACKUP=$(ls -1t /opt/open-repo/backups/data-*.tar.gz | head -1)
tar xzf $BACKUP -C /

# Verify restoration
ls -la /opt/open-repo/data/open_repo.db
```

### Step 3: Restart Application

**Docker**:
```bash
docker-compose up -d
sleep 40  # Wait for health check
curl http://127.0.0.1:8000/health
```

**systemd**:
```bash
sudo systemctl start open-repo
sleep 5
curl http://127.0.0.1:8000/health
```

### Step 4: Verify Data

```bash
# Docker
docker logs open-repo-app | tail -20

# systemd
sudo journalctl -u open-repo -n 20
```

---

## Recovery Time Estimates by Scenario

| Scenario | Fix-Forward Time | Rollback Time | Recommended |
|----------|-----------------|---------------|-------------|
| **A1 / B1**: Container/Service won't start | 10–15 min | 15–20 min | Fix-forward (faster) |
| **A2 / B2**: API returns errors | 10–30 min | 15–20 min | Fix-forward if <30 min, else rollback |
| **A3 / B3**: Database corruption | N/A | 20–30 min | Rollback (database must be restored) |
| **A4 / B4**: Network/health issues | 5–10 min | 15–20 min | Fix-forward (faster) |
| **C1**: Migration bug | 10–20 min | 15–25 min | Fix-forward or downgrade migration |

---

## Communication During Downtime

If deployment fails and requires rollback/recovery:

1. **Notify stakeholders** (email, Slack):
   - Deployment encountered an issue at [TIME]
   - Recovery in progress (ETA: [TIME])
   - Will update every 15 minutes

2. **After recovery**:
   - Service restored at [TIME]
   - RCA to follow (within 24 hours)

---

## Prevention Best Practices

To avoid failure scenarios in future deployments:

1. **Pre-deployment validation**:
   - Run full test suite before deployment (197+ tests passing)
   - Validate all environment variables are set
   - Test database migrations on staging first

2. **Incremental rollout**:
   - Deploy to a staging/test environment first (if available)
   - Run smoke tests post-deployment
   - Monitor logs for first 24 hours actively

3. **Backup discipline**:
   - Automated daily backups in place
   - Test restore procedure quarterly
   - Keep at least 7 days of backups

4. **Health check monitoring**:
   - Automated health checks every 5 minutes (systemd) or 30 sec (Docker)
   - Alerting on failures
   - Log all health check results

---

## Document Metadata

- **Version**: 1.0 (production-ready)
- **Last Updated**: 2026-06-22
- **Status**: REFERENCE (use if deployment issues occur)
- **Applicable To**: Docker and systemd deployment paths
- **Authored By**: Claude Haiku 4.5 (Session 3904)
