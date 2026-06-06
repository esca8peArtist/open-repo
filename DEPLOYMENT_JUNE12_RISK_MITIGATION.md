---
title: "Open-Repo June 12, 2026 Risk Mitigation & Rollback Procedures"
project: open-repo
phase: 5 (final production deployment)
document_type: risk-and-contingency
status: READY TO EXECUTE
created: 2026-06-06
target_deployment_date: 2026-06-12 (09:00 UTC)
deployment_window: "09:00–11:00 UTC"
rollback_time_estimate: "5–10 minutes"
---

# Risk Mitigation & Rollback Procedures (June 12, 2026)

**Purpose**: Identify critical failure modes, establish rapid detection/recovery procedures, and document rollback strategy for any deployment contingency.

**Scope**: Database, code, tests, A11y, and infrastructure failures during June 12 deployment window (09:00–11:00 UTC).

---

## Section 1: Critical Failure Modes (5 Identified)

### Failure Mode 1: Database Migration Failure

**Description**: Alembic migration fails or corrupts schema during Step 6.

**Probability**: Low (3%) — No schema changes for Phase 5 A11y  
**Severity**: Critical — Application cannot start without correct schema  
**User Impact**: High — Service down, data potentially inaccessible

---

#### Detection Method

```bash
# During Step 6 execution:
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'DETECT'
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# Check migration status
alembic current &> /tmp/alembic-current.log
if [ $? -ne 0 ]; then
  echo "❌ CRITICAL: Migration check failed"
  cat /tmp/alembic-current.log
  exit 1
fi

# Verify schema matches expected state
python -c "
from sqlalchemy import inspect
from app.database import engine
inspector = inspect(engine)
tables = inspector.get_table_names()
if 'zim_exports' not in tables:
  print('❌ CRITICAL: Required table missing')
  exit(1)
" 2>&1 | tee /tmp/schema-check.log

if [ $? -ne 0 ]; then
  echo "❌ CRITICAL: Schema validation failed"
  cat /tmp/schema-check.log
  exit 1
fi

echo "✅ Migration successful"
DETECT
```

#### Impact Assessment

- **Data Loss Risk**: High if migration partially applied (half-way state)
- **Service Availability**: 100% down until rollback or fix
- **User-Facing**: Yes — OPDS endpoints return 500 errors
- **Recovery Time**: 5–10 minutes for rollback

#### Recovery Procedure

**Step 1: Stop Application**
```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'STOP'
sudo systemctl stop open-repo
echo "Service stopped at $(date -u +%T UTC)"
STOP
```

**Step 2: Restore Database Backup**
```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'RESTORE_DB'
BACKUP_FILE=$(ls -t /opt/db-backups/*.{db,sql.gz} 2>/dev/null | head -1)
echo "Restoring from: $BACKUP_FILE"

if [[ "$BACKUP_FILE" == *.sql.gz ]]; then
  # PostgreSQL restore
  gunzip -c "$BACKUP_FILE" | psql [connection-string]
elif [[ "$BACKUP_FILE" == *.db ]]; then
  # SQLite restore
  cp "$BACKUP_FILE" /path/to/database.db
  chmod 644 /path/to/database.db
fi

echo "Database restored"
RESTORE_DB
```

**Step 3: Rollback Code to Previous Version**
```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'ROLLBACK_CODE'
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo

# Get previous commit (rollback)
CURRENT=$(git log --oneline -1)
echo "Current: $CURRENT"

# Reset to previous stable version
git reset --hard HEAD~1
NEW_CURRENT=$(git log --oneline -1)
echo "Rolled back to: $NEW_CURRENT"
ROLLBACK_CODE
```

**Step 4: Start Application**
```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'START'
sudo systemctl start open-repo
sleep 5
if sudo systemctl is-active --quiet open-repo; then
  echo "✅ Service restarted successfully"
else
  echo "❌ Service failed to start, check logs"
  sudo journalctl -u open-repo -n 20
fi
START
```

#### Escalation

- **Immediate** (0–2 min): Log error, stop application
- **Short-term** (2–5 min): Initiate rollback procedure
- **Medium-term** (5–10 min): Verify rollback success, notify stakeholders
- **Long-term** (30+ min): Post-mortem: why did migrations run when not needed?

---

### Failure Mode 2: Test Regression (Tests Failing at Deployment)

**Description**: One or more of 157 tests fail during pre-deployment test run or post-deployment verification.

**Probability**: Very Low (1%) — Tests passed in pre-check  
**Severity**: High — Indicates code issue; deployment may be unstable  
**User Impact**: Potentially High — Unknown code quality

---

#### Detection Method

```bash
# Run test suite before deployment (pre-check)
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
python -m pytest tests/ -v --tb=line 2>&1 | tee /tmp/tests-predeployment.txt

# Check results
PASSED=$(grep -oP '\d+(?= passed)' /tmp/tests-predeployment.txt | head -1)
FAILED=$(grep -oP '\d+(?= failed)' /tmp/tests-predeployment.txt | head -1)

if [ "$PASSED" != "157" ] || [ ! -z "$FAILED" ]; then
  echo "❌ TEST FAILURE: $FAILED tests failing"
  grep "FAILED::" /tmp/tests-predeployment.txt
  exit 1
fi
```

#### Impact Assessment

- **Data Loss Risk**: None directly; tests are read-only
- **Service Availability**: Unknown — failed tests indicate code issue
- **User-Facing**: Potentially — unknown feature stability
- **Recovery Time**: 5–10 minutes for rollback

#### Recovery Procedure

**Step 1: Identify Failed Tests**
```bash
# Extract list of failing tests
grep "FAILED::" /tmp/tests-predeployment.txt > /tmp/failed-tests.log
echo "Failed tests:"
cat /tmp/failed-tests.log
```

**Step 2: Assess Severity**
- Is it an A11y test? → Can potentially defer
- Is it a core functionality test? → Must fix before deployment
- Is it integration test? → May indicate environmental issue

**Step 3: Decision Tree**
```
If test is A11y regression:
  → Can defer to Phase 5.2 if not critical
  → Update DEPLOYMENT_NOTES.md with known issue
  
If test is core functionality:
  → DO NOT DEPLOY
  → Rollback code and fix in next release
  
If test is environment/infrastructure:
  → May be CI/CD environment issue (not prod)
  → Can proceed with caution, add monitoring
```

**Step 4: If Decision is ROLLBACK**
```bash
# Revert to previous commit
git reset --hard origin/master~1
git push -f origin master  # Force-push previous version
# Then run rollback procedure from Failure Mode 1
```

#### Escalation

- **Immediate** (0–1 min): Flag failed test, stop deployment
- **Short-term** (1–5 min): Triage: critical vs. deferrable
- **Medium-term** (5–10 min): Decision: fix or rollback
- **Long-term** (10+ min): Implement decision, notify stakeholders

---

### Failure Mode 3: Deployment Latency / Timeout (Steps Take Too Long)

**Description**: One or more deployment steps exceed time allocation, pushing deployment beyond 10:00 UTC hard deadline.

**Probability**: Low (5%) — Estimated 45 minutes, 75-minute window available  
**Severity**: Medium — Extends maintenance window but doesn't necessarily fail  
**User Impact**: Medium — Service unavailable for longer than communicated

---

#### Detection Method

```bash
# Monitor elapsed time during deployment
DEPLOYMENT_START=$(date +%s)
TIMEOUT_LIMIT=$((120 * 60))  # 120 minutes (10:00 UTC hard stop)

# Check time after each step
check_time() {
  CURRENT_TIME=$(date +%s)
  ELAPSED=$(($CURRENT_TIME - $DEPLOYMENT_START))
  REMAINING=$(($TIMEOUT_LIMIT - $ELAPSED))
  
  if [ $REMAINING -lt 600 ]; then  # 10 minutes left
    echo "⚠️  WARNING: Only ${REMAINING}s remaining before hard deadline"
    return 1
  fi
  return 0
}

# Call after each step
# If time runs out: immediately abort and rollback
```

#### Impact Assessment

- **Data Loss Risk**: None
- **Service Availability**: Down for extended period
- **User-Facing**: Yes — users see "service unavailable" longer
- **Recovery Time**: 5–10 minutes for rollback

#### Recovery Procedure

**Step 1: Monitor Time Throughout Deployment**
- Set phone alarm for 09:50 UTC (10 minutes before hard stop)
- Log time after each major step
- If approaching 10:00 UTC: ABORT immediately

**Step 2: If Timeout Occurs (>10:00 UTC)**
```bash
# Do NOT continue to next step
# Immediately abort and rollback

echo "⚠️  HARD TIMEOUT REACHED: Aborting deployment"
# Execute rollback procedure from Failure Mode 1
```

**Step 3: Post-Timeout Analysis**
```
Which step took too long?
- Git fetch? → Network issue, consider caching
- Pip install? → Dependency resolution slow, consider pre-staging
- Tests? → Already pre-checked, shouldn't happen
- Migrations? → Database issue, needs investigation

Take action:
- Extend timeout window (push deployment start 30 min earlier)
- Pre-stage slow operations (pip wheel, git clone)
- Identify and fix bottleneck
```

#### Escalation

- **Immediate** (9:50 UTC): First warning (10 min remaining)
- **Hard Stop** (10:00 UTC): Abort, initiate rollback
- **Medium-term** (10–15 min): Verify rollback complete
- **Long-term** (30+ min): Root cause analysis, optimize next deployment

---

### Failure Mode 4: Application Startup Failure

**Description**: Application service (uvicorn) fails to start or crashes immediately after starting.

**Probability**: Low (5%) — Dependencies verified, code tested  
**Severity**: Critical — Service completely non-functional  
**User Impact**: High — OPDS endpoints return 500, all features down

---

#### Detection Method

```bash
# During Step 7 (Start Application)
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'DETECT_START'
echo "Starting service..."
sudo systemctl start open-repo

# Wait for startup sequence
sleep 5

# Check if service is actually running
if ! sudo systemctl is-active --quiet open-repo; then
  echo "❌ CRITICAL: Service failed to start"
  
  # Get error logs
  sudo journalctl -u open-repo -n 50 | tee /tmp/startup-error.log
  exit 1
fi

# Check if uvicorn process is running
if ! ps aux | grep -E "uvicorn" | grep -v grep > /dev/null; then
  echo "❌ CRITICAL: Uvicorn process not found (crashed immediately)"
  sudo journalctl -u open-repo -n 50
  exit 1
fi

# Test health endpoint
HEALTH=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8000/health)
if [ "$HEALTH" != "200" ]; then
  echo "❌ CRITICAL: Health endpoint returned $HEALTH (expected 200)"
  exit 1
fi

echo "✅ Service started successfully"
DETECT_START
```

#### Common Startup Errors

```
Error: "ImportError: No module named 'app'"
→ Cause: Python path incorrect or virtual environment not activated
→ Fix: Verify systemd service file activates venv correctly

Error: "sqlalchemy.exc.OperationalError: cannot open shared object"
→ Cause: Missing system library (libpq for PostgreSQL)
→ Fix: Install: sudo apt install libpq-dev

Error: "Connection refused to database"
→ Cause: Database not running or network unreachable
→ Fix: Check database service status, network routing

Error: "Address already in use (port 8000)"
→ Cause: Another process listening on port 8000
→ Fix: Kill previous process or find what's blocking
```

#### Impact Assessment

- **Data Loss Risk**: None
- **Service Availability**: 100% down
- **User-Facing**: Yes — all endpoints fail
- **Recovery Time**: 5–10 minutes for rollback

#### Recovery Procedure

**Step 1: Get Detailed Error Logs**
```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'LOGS'
echo "=== Recent Service Logs (100 lines) ==="
sudo journalctl -u open-repo -n 100 --no-pager

echo ""
echo "=== System Logs (in case of system-level issue) ==="
sudo dmesg | tail -20
LOGS
```

**Step 2: Attempt Quick Fix** (only if obvious issue)
```bash
# Example: Port already in use
lsof -i :8000
# If another process: sudo kill -9 [PID]
# Then try: sudo systemctl start open-repo

# Example: Missing dependency
pip install [missing-package]
# Then: sudo systemctl restart open-repo
```

**Step 3: If Not Fixable in <5 Minutes → Rollback**
```bash
# Don't waste time troubleshooting during deployment window
# Execute rollback procedure from Failure Mode 1
```

#### Escalation

- **Immediate** (0–2 min): Capture logs, assess issue
- **Short-term** (2–5 min): Attempt quick fix if obvious
- **Medium-term** (5–10 min): If unfixable, initiate rollback
- **Long-term** (30+ min): Root cause analysis, update deployment checklist

---

### Failure Mode 5: Post-Deployment Verification Fails

**Description**: Health check, OPDS endpoint, or A11y regression tests fail after deployment completes.

**Probability**: Medium (10%) — Indicates code issue that passed pre-check  
**Severity**: High — Code appears to work but specific failure detected  
**User Impact**: High — Users hit bug or broken endpoint

---

#### Detection Method

```bash
# During Section 5 (Post-Deployment Verification)

echo "=== Health Check ==="
HEALTH=$(curl -s -o /dev/null -w "%{http_code}" http://100.70.184.84:8000/health)
if [ "$HEALTH" != "200" ]; then
  echo "❌ FAIL: Health endpoint returned $HEALTH"
  exit 1
fi

echo "=== OPDS Endpoints ==="
OPDS=$(curl -s -o /dev/null -w "%{http_code}" \
  -H "Accept: application/atom+xml" \
  http://100.70.184.84:8000/api/v2/opds/root.xml)
if [ "$OPDS" != "200" ]; then
  echo "❌ FAIL: OPDS root returned $OPDS"
  exit 1
fi

echo "=== A11y Regression Tests (if quick run configured) ==="
pytest tests/test_a11y_axecore.py -q --tb=line
if [ $? -ne 0 ]; then
  echo "❌ FAIL: A11y regression detected"
  exit 1
fi

echo "✅ All post-deployment verifications passed"
```

#### Common Post-Deployment Failures

```
Health endpoint 500:
→ Likely: Database connection error, missing env var, import error
→ Fix: Check logs, verify database running, check env vars

OPDS endpoint 500:
→ Likely: Database query error, missing ZIM export data
→ Fix: Check if zim_exports table has data

A11y regression:
→ Likely: CSS not deployed, JavaScript not minified
→ Fix: Verify frontend assets in deployment, check browser cache
```

#### Impact Assessment

- **Data Loss Risk**: None (but may expose existing data issue)
- **Service Availability**: Partial — some endpoints work, some don't
- **User-Facing**: Yes — users hit specific broken feature
- **Recovery Time**: 5–10 minutes for rollback

#### Recovery Procedure

**Step 1: Identify Which Endpoint Failed**
- If health: Database or core app issue
- If OPDS: Specific endpoint issue, may be fixable
- If A11y: Frontend asset issue

**Step 2: Assess Fix Feasibility** (for <5 min fix)
```
Can I fix in 2 minutes?
- Rebuild frontend assets? (if just CSS)
- Restart database? (if connection timeout)
- Set missing env var? (and restart app)

If YES: Attempt fix
If NO: Rollback immediately
```

**Step 3: If Fix Fails → Rollback**
```bash
# Execute rollback procedure from Failure Mode 1
```

#### Escalation

- **Immediate** (0–1 min): Identify exact failure
- **Short-term** (1–5 min): Attempt quick fix if feasible
- **Medium-term** (5–10 min): If unfixable, initiate rollback
- **Long-term** (30+ min): Debug in staging, redeploy after fix

---

## Section 2: Complete Rollback Playbook

**Objective**: If ANY critical failure occurs, execute this procedure to restore previous version with minimal data loss.

**Rollback Trigger**: Deploy-mode decision tree = ROLLBACK (any failure mode above)

**Rollback Duration**: 5–10 minutes total

---

### Rollback Step 1: Stop Current Deployment

```bash
#!/bin/bash
PROD_HOST="100.70.184.84"

echo "=== ROLLBACK INITIATED ==="
echo "Timestamp: $(date -u +%T UTC)"
echo ""
echo "Step 1: Stop current deployment..."

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'STOP'
echo "Stopping open-repo service..."
sudo systemctl stop open-repo

# Verify stopped
sleep 2
if ps aux | grep -E "uvicorn.*open" | grep -v grep > /dev/null; then
  echo "⚠️  Process still running, force killing..."
  sudo pkill -9 -f "uvicorn.*open"
fi

# Wait for port to be released
sleep 2

echo "✅ Service stopped"
STOP

echo "✅ Rollback Step 1 complete"
```

**Expected Output**:
```
Step 1: Stop current deployment...
Stopping open-repo service...
✅ Service stopped
✅ Rollback Step 1 complete
```

---

### Rollback Step 2: Restore Database

```bash
#!/bin/bash
PROD_HOST="100.70.184.84"

echo ""
echo "Step 2: Restore database from backup..."

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'RESTORE'
BACKUP_DIR="/opt/db-backups"
LATEST_BACKUP=$(ls -t "$BACKUP_DIR"/*.{db,sql.gz} 2>/dev/null | head -1)

if [ -z "$LATEST_BACKUP" ]; then
  echo "❌ ERROR: No database backup found!"
  exit 1
fi

echo "Restoring from: $LATEST_BACKUP"

# Backup current (broken) database first
if [ -f "/path/to/database.db" ]; then
  cp /path/to/database.db "/path/to/database.db.broken-$(date +%s)"
  echo "✅ Broken database backed up"
fi

# Restore from clean backup
if [[ "$LATEST_BACKUP" == *.db ]]; then
  echo "Restoring SQLite database..."
  cp "$LATEST_BACKUP" /path/to/database.db
  chmod 644 /path/to/database.db
  echo "✅ SQLite restored"
elif [[ "$LATEST_BACKUP" == *.sql.gz ]]; then
  echo "Restoring PostgreSQL database..."
  gunzip -c "$LATEST_BACKUP" | psql [connection-string]
  echo "✅ PostgreSQL restored"
fi

echo "✅ Database restore complete"
RESTORE

echo "✅ Rollback Step 2 complete"
```

**Expected Output**:
```
Step 2: Restore database from backup...
Restoring from: /opt/db-backups/open-repo-20260612-085930.db.bak
✅ Broken database backed up
✅ SQLite restored
✅ Database restore complete
✅ Rollback Step 2 complete
```

---

### Rollback Step 3: Revert Code to Previous Version

```bash
#!/bin/bash
PROD_HOST="100.70.184.84"

echo ""
echo "Step 3: Revert code to previous version..."

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'REVERT'
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo

echo "Current commit:"
git log --oneline -1

echo ""
echo "Fetching from origin..."
git fetch origin master

echo ""
echo "Resetting to previous stable version..."
git reset --hard origin/master~1

echo ""
echo "New current commit:"
git log --oneline -1

echo "✅ Code reverted"
REVERT

echo "✅ Rollback Step 3 complete"
```

**Expected Output**:
```
Step 3: Revert code to previous version...
Current commit:
abc123d feat(open-repo): Phase 5 A11y verification (BROKEN)

Fetching from origin...

Resetting to previous stable version...
HEAD is now at xyz789p feat(open-repo): Phase 4 foundation (STABLE)

New current commit:
xyz789p feat(open-repo): Phase 4 foundation (STABLE)

✅ Code reverted
✅ Rollback Step 3 complete
```

---

### Rollback Step 4: Reinstall Dependencies

```bash
#!/bin/bash
PROD_HOST="100.70.184.84"

echo ""
echo "Step 4: Reinstall Python dependencies for reverted version..."

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'DEPS'
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
source /opt/venv/open-repo/bin/activate

echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt --quiet

echo "Verifying critical packages..."
pip show fastapi sqlalchemy uvicorn | grep "^Name:" | cut -d' ' -f2 | tr '\n' ', '
echo ""
echo "✅ Dependencies installed"
DEPS

echo "✅ Rollback Step 4 complete"
```

**Expected Output**:
```
Step 4: Reinstall Python dependencies...
Installing dependencies from requirements.txt...
Verifying critical packages...
fastapi, sqlalchemy, uvicorn,
✅ Dependencies installed
✅ Rollback Step 4 complete
```

---

### Rollback Step 5: Start Application

```bash
#!/bin/bash
PROD_HOST="100.70.184.84"

echo ""
echo "Step 5: Start application..."

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'START'
echo "Starting open-repo service..."
sudo systemctl start open-repo

echo "Waiting for startup (5 seconds)..."
sleep 5

# Verify running
if sudo systemctl is-active --quiet open-repo; then
  echo "✅ Service is active"
else
  echo "❌ ERROR: Service failed to start"
  sudo journalctl -u open-repo -n 30
  exit 1
fi

# Health check
HEALTH=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8000/health)
if [ "$HEALTH" = "200" ]; then
  echo "✅ Health endpoint OK"
else
  echo "❌ Health endpoint failed: $HEALTH"
  exit 1
fi

echo "✅ Application started"
START

echo "✅ Rollback Step 5 complete"
```

**Expected Output**:
```
Step 5: Start application...
Starting open-repo service...
Waiting for startup (5 seconds)...
✅ Service is active
✅ Health endpoint OK
✅ Application started
✅ Rollback Step 5 complete
```

---

### Rollback Step 6: Verify Rollback Success

```bash
#!/bin/bash
PROD_HOST="100.70.184.84"

echo ""
echo "Step 6: Verify rollback success..."

# Test all critical endpoints
echo "Testing endpoints..."

echo "1. Health endpoint:"
HEALTH=$(curl -s -o /dev/null -w "%{http_code}" http://$PROD_HOST:8000/health)
if [ "$HEALTH" = "200" ]; then
  echo "   ✅ Health: 200"
else
  echo "   ❌ Health: $HEALTH"
fi

echo "2. OPDS root:"
OPDS=$(curl -s -o /dev/null -w "%{http_code}" \
  -H "Accept: application/atom+xml" \
  http://$PROD_HOST:8000/api/v2/opds/root.xml)
if [ "$OPDS" = "200" ]; then
  echo "   ✅ OPDS: 200"
else
  echo "   ❌ OPDS: $OPDS"
fi

echo "3. Swagger UI:"
DOCS=$(curl -s -o /dev/null -w "%{http_code}" http://$PROD_HOST:8000/docs)
if [ "$DOCS" = "200" ]; then
  echo "   ✅ Swagger: 200"
else
  echo "   ❌ Swagger: $DOCS"
fi

echo ""
echo "✅ Rollback verification complete"
echo ""
echo "=== ROLLBACK COMPLETE ==="
echo "Timestamp: $(date -u +%T UTC)"
```

**Expected Output**:
```
Step 6: Verify rollback success...
Testing endpoints...
1. Health endpoint:
   ✅ Health: 200
2. OPDS root:
   ✅ OPDS: 200
3. Swagger UI:
   ✅ Swagger: 200

✅ Rollback verification complete

=== ROLLBACK COMPLETE ===
Timestamp: 09:12 UTC
```

---

## Section 3: Pre-Deployment Backup Strategy

**Objective**: Ensure all critical data is safely backed up before deployment window opens.

### Database Backup

**When**: Must complete by 08:45 UTC (15 minutes before deployment)

**Procedure**:
```bash
#!/bin/bash
PROD_HOST="100.70.184.84"

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'BACKUP_DB'
BACKUP_DIR="/opt/db-backups"
mkdir -p "$BACKUP_DIR"

BACKUP_FILE="$BACKUP_DIR/open-repo-$(date +%Y%m%d-%H%M%S).db.bak"

echo "Creating database backup: $BACKUP_FILE"

if [ -f "/path/to/database.db" ]; then
  cp /path/to/database.db "$BACKUP_FILE"
  chmod 644 "$BACKUP_FILE"
  ls -lah "$BACKUP_FILE"
  echo "✅ Backup complete"
fi
BACKUP_DB
```

**Retention**: Keep last 3 backups (auto-cleanup old ones)

```bash
# Cleanup script
ls -t /opt/db-backups/*.db 2>/dev/null | tail -n +4 | xargs rm -f
```

### Code Backup

**When**: Created automatically during Step 3 of deployment

**Location**: `/opt/backups/open-repo-[timestamp]/`

**Verification**:
```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'VERIFY'
if [ -d "/opt/backups/open-repo-"* ]; then
  echo "✅ Code backups exist:"
  ls -lt /opt/backups | head -5
else
  echo "⚠️  No code backups found"
fi
VERIFY
```

### Backup Retention Policy

- **Database backups**: Keep last 7 days (daily)
- **Code backups**: Keep last 10 deployments
- **Cleanup frequency**: Daily at 00:00 UTC

---

## Section 4: Communication Triggers & Escalation

### Communication Trigger: When to Notify Stakeholders

**Trigger 1: Pre-Deployment Failure** (any item in pre-check fails)

**Action**: Notify immediately, recommend delay

**Message**: "Pre-deployment verification failed on [item]. Recommend delaying deployment 24 hours while issue is investigated."

---

**Trigger 2: Deployment Abort** (any step fails during deployment)

**Action**: Notify within 2 minutes

**Message**: "Deployment failed at Step [X]: [reason]. Rolling back to previous version. Service will be restored within 10 minutes."

---

**Trigger 3: Rollback Initiated** (recovery procedure starts)

**Action**: Notify within 1 minute, escalate to team lead

**Message**: "Deployment rollback initiated (09:12 UTC). Previous version being restored. ETA for service restoration: 09:18 UTC."

---

**Trigger 4: Rollback Successful** (service restored to previous version)

**Action**: Notify within 5 minutes

**Message**: "Service restored to previous stable version (commit: xyz789p). All endpoints healthy. Incident post-mortem scheduled for [date]."

---

**Trigger 5: Extended Outage** (rollback takes >10 minutes)

**Action**: Notify every 5 minutes during outage, escalate to infrastructure team

**Message**: "Extended outage in progress. Rollback taking longer than expected. Infrastructure team investigating. Current ETA: [time]."

---

## Section 5: Success Criteria & Deployment Completion

### Deployment Success Definition

**All of the following must be true**:

- [ ] All 7 deployment steps completed without errors
- [ ] No rollback was necessary
- [ ] Health endpoint returns 200 OK
- [ ] OPDS endpoints return valid XML (200 OK)
- [ ] Swagger UI and ReDoc respond with 200 OK
- [ ] Application logs show no CRITICAL or ERROR messages in past 5 minutes
- [ ] 157 tests confirmed passing (pre-deployment check)
- [ ] A11y compliance verified (72 automated tests + 5 manual spot checks)
- [ ] Database migrations applied successfully (or skipped if not needed)
- [ ] No data loss detected (database records intact)
- [ ] System resources normal (CPU <50%, memory <70%, disk >5GB free)
- [ ] All stakeholders notified of successful deployment

**Decision**: 
- [ ] DEPLOYMENT SUCCESSFUL — Proceed to active monitoring
- [ ] DEPLOYMENT PARTIAL SUCCESS — Known issues documented, proceed with caution
- [ ] DEPLOYMENT FAILED — See post-mortem procedure below

---

### Post-Deployment Monitoring Checklist

After deployment success is confirmed:

- [ ] Start active monitoring for 60 minutes (09:45–10:45 UTC)
- [ ] Check application logs every 10 minutes
- [ ] Sample 3–5 user requests (test OPDS endpoints, API calls)
- [ ] Monitor system resources (CPU, memory, disk)
- [ ] Have rollback procedures ready if issues emerge
- [ ] After 60 minutes, transition to passive monitoring (24 hours)

See **POST_DEPLOYMENT_MONITORING_PLAN.md** for detailed monitoring procedures.

---

### Post-Mortem Procedure (if Rollback Occurred)

**Schedule**: Within 24 hours of failed deployment

**Participants**: Deployer, developer, infrastructure team

**Questions to Answer**:
1. What failed and why?
2. Did detection mechanisms work correctly?
3. How long was outage? How many users affected?
4. What was the rollback duration?
5. What changes are needed to prevent recurrence?

**Output**: Update deployment checklist with new risk items or safeguards

---

## Quick Reference: Rollback Commands

**One-Liner Rollback** (if in emergency):
```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 \
  "sudo systemctl stop open-repo && \
   cp /opt/db-backups/latest.db /path/to/database.db && \
   cd /home/awank/dev/SuperClaude_Framework/projects/open-repo && \
   git reset --hard origin/master~1 && \
   sudo systemctl start open-repo && \
   sleep 5 && \
   curl -s http://localhost:8000/health | grep -q status && echo '✅ Rollback successful' || echo '❌ Verification failed'"
```

---

## Document Information

**Risk Mitigation Version**: 1.0  
**Created**: June 6, 2026  
**Based On**: DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md  
**Covers**: All potential failure modes during June 12, 2026 deployment  
**Review Date**: June 12, 2026 (post-deployment)  
**Next Update**: If new failure modes identified
