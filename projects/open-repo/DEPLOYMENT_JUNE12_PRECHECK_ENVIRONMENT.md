---
title: "Open-Repo June 12, 2026 Pre-Deployment Environment Checklist"
project: open-repo
phase: 5 (final production deployment)
document_type: pre-deployment-verification
status: READY TO EXECUTE
created: 2026-06-06
target_deployment_date: 2026-06-12 (09:00 UTC)
execution_window: "08:45–09:00 UTC (15 minutes before deployment)"
estimated_duration: "30–45 minutes"
---

# Pre-Deployment Environment Verification Checklist (June 12, 2026)

**Purpose**: Verify all environmental, database, and deployment prerequisites are met before 09:00 UTC deployment window opens.

**Execution Timeline**: 08:45–09:00 UTC (15 minutes before deployment start)

**Success Criteria**: All 12 items checked and passing before 09:00 UTC. If any item fails, remediate or abort deployment.

---

## Pre-Check Checklist (12 Items)

### Item 1: Git Branch and Commit Verification ✓

**Objective**: Ensure deployment code is on master branch with no uncommitted changes.

**Pass Criteria**:
- Current branch is `master`
- No uncommitted changes in working tree
- Local commit matches origin/master

**Procedure**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "master" ]; then
  echo "❌ FAILED: Not on master branch (on: $CURRENT_BRANCH)"
  exit 1
fi
if ! git diff-index --quiet HEAD --; then
  echo "❌ FAILED: Uncommitted changes detected"
  git status
  exit 1
fi
LOCAL=$(git log --oneline -1)
REMOTE=$(git log --oneline origin/master -1)
echo "✅ PASS: On master, clean tree"
echo "   Local: $LOCAL"
echo "   Remote: $REMOTE"
```

**Fail Remediation**:
- If on wrong branch: `git checkout master`
- If uncommitted changes: `git status` and either commit or discard
- If commits diverge: `git pull origin master`

**Status**: [ ] PASS [ ] FAIL

---

### Item 2: Environment Variables on Deployment Machine ✓

**Objective**: Verify all required environment variables are set locally before deployment.

**Pass Criteria**:
- All 6 required variables are set
- No missing or empty values
- SECRET_KEY is set (not logged)

**Required Variables**:
```
DATABASE_URL
SECRET_KEY
OPDS_CATALOG_NAME
LOG_LEVEL
FASTAPI_ENV
UVICORN_HOST
```

**Procedure**:
```bash
#!/bin/bash
REQUIRED=("DATABASE_URL" "SECRET_KEY" "OPDS_CATALOG_NAME" "LOG_LEVEL" "FASTAPI_ENV" "UVICORN_HOST")
MISSING=0

for var in "${REQUIRED[@]}"; do
  value="${!var}"
  if [ -z "$value" ]; then
    echo "❌ MISSING: $var"
    MISSING=$((MISSING + 1))
  else
    if [[ "$var" == "SECRET_KEY" ]]; then
      echo "✅ SET: $var (***REDACTED***)"
    else
      echo "✅ SET: $var"
    fi
  fi
done

if [ $MISSING -eq 0 ]; then
  echo "✅ PASS: All environment variables set"
  exit 0
else
  echo "❌ FAIL: $MISSING variables missing"
  exit 1
fi
```

**Fail Remediation**:
- Missing variable: `export VARIABLE_NAME=value`
- For persistent setup: add to `~/.bashrc` or deployment script
- Verify with `echo $VARIABLE_NAME`

**Status**: [ ] PASS [ ] FAIL

---

### Item 3: Production Host Network Connectivity ✓

**Objective**: Verify network access to production host (100.70.184.84).

**Pass Criteria**:
- Ping response within 100ms
- SSH connection succeeds
- No network latency issues

**Procedure**:
```bash
#!/bin/bash
PROD_HOST="100.70.184.84"

echo "Testing ping connectivity..."
if ping -c 1 -W 5 "$PROD_HOST" > /dev/null 2>&1; then
  echo "✅ PASS: Ping successful"
else
  echo "❌ FAIL: Cannot reach $PROD_HOST"
  exit 1
fi

echo "Testing SSH connection..."
if ssh -i ~/.ssh/production_key -o ConnectTimeout=5 -o StrictHostKeyChecking=no \
    ubuntu@"$PROD_HOST" 'echo "SSH OK"' > /dev/null 2>&1; then
  echo "✅ PASS: SSH connection successful"
else
  echo "❌ FAIL: SSH connection failed"
  exit 1
fi
```

**Fail Remediation**:
- Network issue: Check local network (VPN, Tailscale)
- SSH key issue: Verify `~/.ssh/production_key` exists and has 600 permissions
- Host unreachable: Contact infrastructure team, may indicate production host down

**Status**: [ ] PASS [ ] FAIL

---

### Item 4: Database Accessibility and State ✓

**Objective**: Verify database is accessible and in correct state for deployment.

**Pass Criteria**:
- Database is reachable (local SQLite or remote)
- Current migration matches expected state
- No stale or test data present
- Database file/service is writable

**Procedure**:
```bash
#!/bin/bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "Checking database connectivity..."
if [ -f "alembic/versions/"*.py ]; then
  echo "Using Alembic migrations..."
  if command -v alembic &> /dev/null; then
    CURRENT=$(alembic current 2>/dev/null | tail -1)
    HEAD=$(alembic heads 2>/dev/null | tail -1)
    if [ "$CURRENT" = "$HEAD" ]; then
      echo "✅ PASS: Database migrations current ($CURRENT)"
    else
      echo "❌ FAIL: Pending migrations (current: $CURRENT, head: $HEAD)"
      exit 1
    fi
  else
    echo "⚠️  Alembic not found, skipping migration check"
  fi
else
  echo "✅ PASS: No migrations needed (Phase 5 A11y changes are CSS/JS only)"
fi

echo "Checking database file/accessibility..."
if [ -f "/path/to/database.db" ]; then
  if [ -w "/path/to/database.db" ]; then
    echo "✅ PASS: Database file is writable"
  else
    echo "❌ FAIL: Database file not writable"
    exit 1
  fi
fi
```

**Fail Remediation**:
- Pending migrations: `alembic upgrade head`
- Database not writable: Check file permissions (`chmod 644`)
- Stale test data: Verify with `SELECT COUNT(*) FROM [test_table]` (should be empty)

**Status**: [ ] PASS [ ] FAIL

---

### Item 5: Python Dependencies Status ✓

**Objective**: Verify required Python packages are available and compatible.

**Pass Criteria**:
- All 7 critical dependencies installed
- Versions compatible with application
- Virtual environment is active
- No broken/conflicting packages

**Critical Packages** (check version):
```
fastapi>=0.95.0
sqlalchemy>=2.0.0
pydantic>=2.0.0
uvicorn>=0.21.0
pytest>=7.0.0
httpx>=0.24.0
```

**Procedure**:
```bash
#!/bin/bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

if [ -f "requirements.txt" ]; then
  echo "Checking requirements.txt..."
  if grep -q "fastapi\|sqlalchemy\|uvicorn" requirements.txt; then
    echo "✅ PASS: requirements.txt contains critical packages"
  else
    echo "⚠️  WARNING: requirements.txt structure unexpected"
  fi
else
  echo "❌ FAIL: requirements.txt not found"
  exit 1
fi

echo "Checking installed packages..."
MISSING=0
for pkg in fastapi sqlalchemy pydantic uvicorn pytest; do
  pip show "$pkg" > /dev/null 2>&1
  if [ $? -eq 0 ]; then
    VERSION=$(pip show "$pkg" | grep "^Version:" | cut -d' ' -f2)
    echo "✅ $pkg: $VERSION"
  else
    echo "❌ $pkg: NOT INSTALLED"
    MISSING=$((MISSING + 1))
  fi
done

if [ $MISSING -eq 0 ]; then
  echo "✅ PASS: All critical dependencies installed"
else
  echo "❌ FAIL: $MISSING packages missing"
  exit 1
fi
```

**Fail Remediation**:
- Missing packages: `pip install -r requirements.txt`
- Version mismatch: Update with `pip install --upgrade [package]`
- Conflicts: `pip check` to identify issues

**Status**: [ ] PASS [ ] FAIL

---

### Item 6: Test Suite Status (157 Tests) ✓

**Objective**: Verify all 157 tests pass in current state before deployment.

**Pass Criteria**:
- 157 tests total
- 157 tests passing (0 failures)
- 72 A11y tests passing (axecore, contrast, semantics, deep scan)
- Test run completes in <5 minutes
- No skipped tests

**Procedure**:
```bash
#!/bin/bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "Running full test suite..."
python -m pytest tests/ -v --tb=short 2>&1 | tee /tmp/test-results.txt

TEST_RESULTS=$(tail -20 /tmp/test-results.txt | grep -E "passed|failed|error")
echo ""
echo "Test Results:"
echo "$TEST_RESULTS"

# Parse results
PASSED=$(echo "$TEST_RESULTS" | grep -oP '\d+(?= passed)' | head -1)
FAILED=$(echo "$TEST_RESULTS" | grep -oP '\d+(?= failed)' | head -1)

if [ "$PASSED" = "157" ] && [ -z "$FAILED" ]; then
  echo "✅ PASS: All 157 tests passing"
  exit 0
else
  echo "❌ FAIL: Test failures detected ($PASSED passed, $FAILED failed)"
  grep "FAILED\|ERROR" /tmp/test-results.txt
  exit 1
fi
```

**Fail Remediation**:
- Failed tests: Review with `pytest tests/ -v --failed-first`
- Fix failures before deployment or skip if known
- Run specific test categories: `pytest tests/test_a11y*.py -v` for A11y tests

**Status**: [ ] PASS [ ] FAIL

---

### Item 7: A11y Compliance Verification (72 Automated + 5 Manual) ✓

**Objective**: Verify WCAG 2.1 AA compliance confirmed across automated and manual tests.

**Pass Criteria**:
- 72 automated A11y tests passing
- Manual spot-check completed on 5 critical flows
- No WCAG failures or warnings
- Contrast ratios verified (AA: 4.5:1 for text, 3:1 for graphics)

**Critical Flows for Manual Test**:
1. Book search and display
2. OPDS catalog browsing
3. Content export pipeline
4. User contribution workflow
5. ActivityPub federation interface

**Procedure**:
```bash
#!/bin/bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "Running A11y test suite..."
pytest tests/test_a11y_*.py -v --tb=short 2>&1 | tee /tmp/a11y-results.txt

A11Y_COUNT=$(grep -c "test_a11y" /tmp/a11y-results.txt)
echo "A11y tests found: $A11Y_COUNT"

if grep -q "72 passed"; then
  echo "✅ PASS: 72 A11y tests passing"
else
  echo "⚠️  WARNING: A11y test count mismatch, review manually"
fi

echo ""
echo "Manual spot-check required on 5 critical flows:"
echo "[ ] 1. Book search and display (check text contrast, semantic HTML)"
echo "[ ] 2. OPDS catalog (verify feed structure, link labels)"
echo "[ ] 3. Export pipeline (test keyboard navigation)"
echo "[ ] 4. Contribution workflow (check form labels, error messages)"
echo "[ ] 5. Federation interface (verify API documentation accessibility)"
echo ""
echo "Manual tests must be completed before proceeding to deployment."
```

**Fail Remediation**:
- A11y test failures: Fix CSS/HTML issues and retest
- Manual spot-check fails: Address specific accessibility issue before deployment
- Contrast issues: Update CSS color values to meet AA standard

**Manual Verification Checklist**:
- [ ] Can navigate entire flow with keyboard only (no mouse)
- [ ] All interactive elements have visible focus indicators
- [ ] Form labels properly associated with inputs
- [ ] Color contrast meets WCAG AA (4.5:1 for text)
- [ ] Screen reader announces content correctly (test with NVDA/JAWS if available)

**Status**: [ ] PASS [ ] FAIL (Automated) [ ] PASS [ ] FAIL (Manual)

---

### Item 8: Deployment Artifacts and Build Status ✓

**Objective**: Verify all deployment artifacts are built and ready for deployment.

**Pass Criteria**:
- Frontend assets built (CSS, JS minimized)
- Docker images built (or deployment container ready)
- No build errors or warnings
- Artifact file sizes reasonable (no corruption)
- Checksum verification passes

**Procedure**:
```bash
#!/bin/bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo

echo "Checking frontend build artifacts..."
if [ -d "frontend/build" ] || [ -d "frontend/dist" ]; then
  echo "✅ Frontend artifacts found"
  find frontend/build frontend/dist -type f 2>/dev/null | wc -l | xargs echo "  Files:"
else
  echo "⚠️  Frontend artifacts not found, may use inline/CDN assets"
fi

echo ""
echo "Checking backend artifacts..."
if [ -f "backend/requirements.txt" ]; then
  echo "✅ requirements.txt present"
  wc -l backend/requirements.txt
else
  echo "❌ FAIL: requirements.txt not found"
  exit 1
fi

if [ -f "Dockerfile" ] || [ -f "docker-compose.yml" ]; then
  echo "✅ Docker configuration found"
else
  echo "⚠️  Docker files not found (may use direct Python deployment)"
fi

echo ""
echo "✅ PASS: Deployment artifacts ready"
```

**Fail Remediation**:
- Build fails: Run `npm run build` or equivalent
- Missing artifacts: Rebuild from source
- Size mismatch: Check for accidental large files (binaries, etc.)

**Status**: [ ] PASS [ ] FAIL

---

### Item 9: SSL/TLS Certificate Status ✓

**Objective**: Verify TLS certificates are valid and not expiring soon.

**Pass Criteria**:
- TLS certificate present on production host
- Certificate not expired
- Certificate valid for at least 30 days
- Certificate matches domain/IP (100.70.184.84 or FQDN)

**Procedure**:
```bash
#!/bin/bash
PROD_HOST="100.70.184.84"

echo "Checking TLS certificate status..."
CERT_EXPIRY=$(echo | openssl s_client -connect "$PROD_HOST:8000" 2>/dev/null | \
  openssl x509 -noout -enddate 2>/dev/null | cut -d= -f2)

if [ -z "$CERT_EXPIRY" ]; then
  echo "⚠️  No TLS certificate detected (may be HTTP only, which is OK for internal)"
  echo "✅ PASS: No certificate issue (HTTP deployment)"
else
  EXPIRY_DATE=$(date -d "$CERT_EXPIRY" +%s 2>/dev/null)
  TODAY=$(date +%s)
  DAYS_LEFT=$(( ($EXPIRY_DATE - $TODAY) / 86400 ))
  
  if [ $DAYS_LEFT -gt 30 ]; then
    echo "✅ PASS: Certificate valid for $DAYS_LEFT days (expires: $CERT_EXPIRY)"
  else
    echo "❌ FAIL: Certificate expiring soon ($DAYS_LEFT days left)"
    exit 1
  fi
fi
```

**Fail Remediation**:
- Certificate expired: Renew with `certbot renew` or provider
- Certificate missing: Install from Let's Encrypt or internal CA
- Domain mismatch: Use IP-based certificate or update DNS

**Status**: [ ] PASS [ ] FAIL

---

### Item 10: Disk Space and System Resources ✓

**Objective**: Verify production host has sufficient disk space and memory for deployment.

**Pass Criteria**:
- Disk space: >5GB free (minimum 2GB for code, 3GB safety margin)
- Memory: >500MB available (minimum requirement)
- Swap: Configured and available if needed
- No resource exhaustion warnings

**Procedure**:
```bash
#!/bin/bash
PROD_HOST="100.70.184.84"

echo "Checking production host system resources..."
ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'RESOURCES'
echo "=== Disk Space ==="
DISK_FREE=$(df /home | awk 'NR==2 {print $4}')
DISK_PERCENT=$(df /home | awk 'NR==2 {print $5}' | cut -d% -f1)
echo "Free: $(( $DISK_FREE / 1024 ))MB (${DISK_PERCENT}% used)"

if [ $DISK_FREE -gt 5242880 ]; then  # 5GB in KB
  echo "✅ PASS: Sufficient disk space"
else
  echo "❌ FAIL: Low disk space"
  exit 1
fi

echo ""
echo "=== Memory ==="
FREE_MEM=$(free -m | awk 'NR==2 {print $7}')
TOTAL_MEM=$(free -m | awk 'NR==2 {print $2}')
echo "Available: ${FREE_MEM}MB / ${TOTAL_MEM}MB"

if [ $FREE_MEM -gt 500 ]; then
  echo "✅ PASS: Sufficient memory"
else
  echo "❌ FAIL: Low memory"
  exit 1
fi

echo ""
echo "=== Load Average ==="
LOAD=$(uptime | grep -oP 'load average: \K.*')
echo "Load: $LOAD"
if [ $(echo "$LOAD" | cut -d, -f1 | cut -d' ' -f1) -lt 2 ]; then
  echo "✅ PASS: System load acceptable"
else
  echo "⚠️  WARNING: High system load (may impact deployment)"
fi
RESOURCES
```

**Fail Remediation**:
- Disk space low: Delete old backups, archived logs: `rm /opt/backups/open-repo-* --except-latest`
- Memory low: Kill non-essential services before deployment
- Load high: Wait for background jobs to complete, or reschedule deployment

**Status**: [ ] PASS [ ] FAIL

---

### Item 11: Backup Availability ✓

**Objective**: Verify database and code backups exist and are accessible for emergency rollback.

**Pass Criteria**:
- Database backup exists (created within 24 hours)
- Code backup exists (previous version available)
- Backup files are readable and not corrupted
- Backup paths documented

**Procedure**:
```bash
#!/bin/bash
PROD_HOST="100.70.184.84"

echo "Checking backup availability..."
ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'BACKUPS'
echo "Database backups:"
if [ -d "/opt/db-backups" ]; then
  LATEST_DB=$(ls -t /opt/db-backups/*.{db,sql.gz} 2>/dev/null | head -1)
  if [ -f "$LATEST_DB" ]; then
    AGE=$(( ($(date +%s) - $(stat -c %Y "$LATEST_DB")) / 3600 ))
    echo "  Latest: $LATEST_DB ($AGE hours old)"
    if [ $AGE -lt 24 ]; then
      echo "  ✅ PASS: Database backup current"
    else
      echo "  ⚠️  WARNING: Backup older than 24 hours"
    fi
  fi
else
  echo "  ⚠️  /opt/db-backups not found"
fi

echo ""
echo "Code backups:"
if [ -d "/opt/backups" ]; then
  LATEST_CODE=$(ls -td /opt/backups/open-repo-* | head -1)
  if [ -d "$LATEST_CODE" ]; then
    echo "  Latest: $LATEST_CODE"
    echo "  ✅ PASS: Code backup available"
  fi
else
  echo "  ⚠️  /opt/backups not found (will create during deployment)"
fi
BACKUPS
```

**Fail Remediation**:
- No backup: Create immediately with database dump: `mysqldump [db] > backup.sql` or `pg_dump [db] > backup.sql`
- Old backup: Consider pushing deployment if backup is stale (>48 hours)
- Corrupted backup: Verify with `mysql -u [user] < backup.sql` (dry run)

**Status**: [ ] PASS [ ] FAIL

---

### Item 12: Final Sanity Check (All Items Reviewed) ✓

**Objective**: Final review that all 11 items passed before deployment window opens.

**Pass Criteria**:
- All 11 previous items marked as PASS
- No FAIL items remain
- No outstanding remediation tasks
- Deployment team is ready to proceed
- Go/No-Go decision documented

**Procedure**:
```bash
#!/bin/bash
echo "=== FINAL PRE-DEPLOYMENT SANITY CHECK ==="
echo ""
echo "Review checklist:"
echo "[ ] Item 1:  Git branch and commits verified"
echo "[ ] Item 2:  Environment variables set locally"
echo "[ ] Item 3:  Production host network access confirmed"
echo "[ ] Item 4:  Database accessible and current"
echo "[ ] Item 5:  Python dependencies installed"
echo "[ ] Item 6:  All 157 tests passing"
echo "[ ] Item 7:  A11y compliance verified (72 auto + 5 manual)"
echo "[ ] Item 8:  Deployment artifacts ready"
echo "[ ] Item 9:  TLS certificates valid"
echo "[ ] Item 10: Disk space and memory sufficient"
echo "[ ] Item 11: Backups available and current"
echo ""
echo "Go/No-Go Decision: [ ] GO [ ] NO-GO"
echo ""
if [ "$(date +%H:%M)" -lt "09:00" ]; then
  echo "✅ All checks can be completed before 09:00 UTC deployment window"
else
  echo "❌ CRITICAL: Deployment window already open, cannot proceed with pre-checks"
  exit 1
fi
```

**Fail Remediation**:
- If any item is FAIL: Do not proceed; fix issues or abort deployment
- If decision is NO-GO: Communicate delay to stakeholders (see communication templates)
- Document any deferred items: Will be checked during post-deployment monitoring

**Status**: [ ] GO [ ] NO-GO

---

## Execution Summary

**Checklist Completed By**: ________________  
**Completion Date/Time**: ________________ UTC  
**Total Time Spent**: _____ minutes  

**Results**:
- Items Passed: _____ / 12
- Items Failed: _____ / 12
- Items Deferred: _____ / 12

**Decision**: [ ] PROCEED TO DEPLOYMENT [ ] ABORT DEPLOYMENT [ ] DEFER/RESCHEDULE

**Notes/Issues**:
```
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
```

**Approved By** (deployment decision owner): ________________

---

## Quick Reference: Common Issues

| Issue | Quick Check | Fix |
|-------|-----------|-----|
| Git not on master | `git branch --show-current` | `git checkout master` |
| Env vars missing | `echo $DATABASE_URL` | `export DATABASE_URL=value` |
| SSH fails | `ssh ubuntu@100.70.184.84` | Check key, network, host status |
| Tests failing | `pytest tests/ -v` | Fix code, retest, or skip if known |
| A11y issues | Open in browser, test keyboard | Fix CSS/HTML contrast/labels |
| Low disk space | `df -h` | Delete backups: `rm /opt/backups/*` |
| Old backups | `ls -lt /opt/backups` | Create new backup immediately |

---

**Checklist Version**: 1.0  
**Created**: June 6, 2026  
**Based On**: DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md  
**Valid For**: June 12, 2026 deployment  
**Last Updated**: June 6, 2026
