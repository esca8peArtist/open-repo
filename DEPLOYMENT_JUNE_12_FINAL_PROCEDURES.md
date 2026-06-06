---
title: "Open-Repo June 12, 2026 Final Deployment Procedures (Enhanced)"
project: open-repo
phase: 5 (final production deployment)
document_type: deployment-procedures
status: READY TO EXECUTE
created: 2026-06-06
target_deployment_date: 2026-06-12 (09:00 UTC)
deployment_window: "09:00–11:00 UTC (120 minutes)"
rollback_path: "revert commit, redeploy previous master"
rollback_time: "10 minutes"
---

# Enhanced June 12 Deployment Final Procedures

**Deployment Date**: June 12, 2026  
**Deployment Start Time**: 09:00 UTC (morning UTC, adjust for your timezone)  
**Estimated Total Duration**: 45 minutes (10 min pre-flight + 25 min deployment + 10 min health checks)  
**Deployment Target**: Production environment (Raspberry Pi 5, 100.70.184.84)  
**Deployer**: Must have SSH access to production host and git push access to upstream

---

## SECTION 1: Deployment Schedule & Timeline

### June 12, 2026 Timeline

| Time (UTC) | Activity | Duration | Owner |
|-----------|----------|----------|-------|
| 08:45 | Pre-deployment notifications sent | 5 min | Deployer |
| 09:00 | **DEPLOYMENT WINDOW OPENS** | — | — |
| 09:00–09:10 | Environment variable validation & pre-flight checks | 10 min | Deployer |
| 09:10–09:35 | Deployment execution (steps 1–7) | 25 min | Deployer |
| 09:35–09:45 | Post-deployment health verification | 10 min | Deployer |
| 09:45 | **DEPLOYMENT WINDOW CLOSES** | — | — |
| 09:45–10:45 | **ACTIVE MONITORING** (60 minutes) | 60 min | Ops team |
| 10:45 onwards | **PASSIVE MONITORING** (24 hours) | 24 hours | Ops team |

**Timeline Notes**:
- If any step takes longer than allocated, add 5 min buffer before next step
- If deployment is not complete by 10:00 UTC, ABORT and rollback (fail-safe)
- Active monitoring starts immediately after deployment window closes
- See POST_DEPLOYMENT_MONITORING_PLAN.md for monitoring details

### Deployment Window Maintenance Notice

**Notify users/stakeholders**: 2 hours before deployment (07:00 UTC)

---

## SECTION 2: Environment Variables Pre-Flight Validation

This section validates all required environment variables are set correctly BEFORE deployment begins. Completion time: ~5 minutes.

**Objective**: Ensure application will not crash due to missing or misconfigured environment variables.

### Step 1: List Required Environment Variables

The application requires these environment variables. Create a reference file:

```bash
cat > /tmp/required-env-vars.txt << 'EOF'
# Open-Repo Required Environment Variables (Phase 5)
# Format: VARIABLE_NAME=expected_type_or_example

DATABASE_URL=string (postgres:// or sqlite:/// URL)
SECRET_KEY=string (random 32+ char string, do NOT log)
OPDS_CATALOG_NAME=string (name of OPDS catalog, e.g., "Open Repository")
LOG_LEVEL=string (DEBUG|INFO|WARNING|ERROR|CRITICAL)
FASTAPI_ENV=string (development|production|testing)
UVICORN_HOST=string (127.0.0.1 or production IP)
UVICORN_PORT=int (8000)
ZIM_EXPORT_PATH=string (optional, path to ZIM export directory)
EOF
cat /tmp/required-env-vars.txt
```

**Expected Output**:
```
# Open-Repo Required Environment Variables (Phase 5)
# Format: VARIABLE_NAME=expected_type_or_example
...
```

### Step 2: Verify Variables on Deployment Machine (Local)

Before SSH into production, verify your deployment environment is correct:

```bash
#!/bin/bash
echo "=== Verifying Environment Variables on Deployment Machine ==="

required_vars=(
  "DATABASE_URL"
  "SECRET_KEY"
  "OPDS_CATALOG_NAME"
  "LOG_LEVEL"
)

echo ""
echo "Checking required environment variables..."
all_set=true

for var in "${required_vars[@]}"; do
  value="${!var}"
  if [ -z "$value" ]; then
    echo "❌ MISSING: $var"
    all_set=false
  else
    # Don't print SECRET_KEY value for security
    if [[ "$var" == "SECRET_KEY" ]]; then
      echo "✅ SET: $var (***REDACTED***)"
    else
      echo "✅ SET: $var=$value"
    fi
  fi
done

echo ""
if [ "$all_set" = true ]; then
  echo "✅ All required environment variables are set"
  exit 0
else
  echo "❌ DEPLOYMENT BLOCKED: Missing required environment variables"
  exit 1
fi
```

Save as `/tmp/verify-env-local.sh` and run:
```bash
bash /tmp/verify-env-local.sh
```

**Expected Output**:
```
=== Verifying Environment Variables on Deployment Machine ===

Checking required environment variables...
✅ SET: DATABASE_URL=postgres://...
✅ SET: SECRET_KEY=(***REDACTED***)
✅ SET: OPDS_CATALOG_NAME=Open Repository
✅ SET: LOG_LEVEL=INFO

✅ All required environment variables are set
```

**If any variable is missing**:
1. Set it in your shell: `export VARIABLE_NAME=value`
2. Or set it in `~/.bashrc` for permanent configuration
3. Re-run verification script
4. **DO NOT PROCEED** with deployment until all variables are set

### Step 3: Verify Variables on Production Host

Once confirmed locally, verify they're also set on production:

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'VERIFY_PROD'
echo "=== Production Environment Variable Verification ==="
echo ""
echo "Checking /etc/environment for Open-Repo variables..."

# Check system-wide environment
grep -E "DATABASE_URL|OPDS_CATALOG_NAME|LOG_LEVEL" /etc/environment || echo "  (none in /etc/environment)"

echo ""
echo "Checking systemd service configuration..."
sudo systemctl cat open-repo | grep -E "Environment=" || echo "  (no Environment directives in systemd)"

echo ""
echo "Checking .bashrc or virtualenv activation..."
if [ -f ~/.bashrc ]; then
  grep -E "DATABASE_URL|OPDS_CATALOG_NAME|LOG_LEVEL" ~/.bashrc || echo "  (none in ~/.bashrc)"
fi

echo ""
echo "Note: Variables may also be set inside Python application"
echo "or passed at runtime. This check only verifies system-wide settings."
VERIFY_PROD
```

**Expected Output**:
```
=== Production Environment Variable Verification ===

Checking /etc/environment for Open-Repo variables...
DATABASE_URL=postgres://...
OPDS_CATALOG_NAME=Open Repository
LOG_LEVEL=INFO

Checking systemd service configuration...
Environment="DATABASE_URL=postgres://..."

Checking .bashrc or virtualenv activation...
  (none in ~/.bashrc)

Note: Variables may also be set inside Python application
or passed at runtime. This check only verifies system-wide settings.
```

**If variables are not found on production**:
1. This may be OK if variables are hardcoded in the application
2. Or if they're set in a `.env` file that gets loaded at startup
3. Check the application startup logs to verify variables are actually being used
4. If variables are truly missing and needed, set them before starting the service:
   ```bash
   ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
   # Add to /etc/environment or systemd service file
   # Then reload systemd: sudo systemctl daemon-reload
   EOF
   ```

---

## SECTION 3: Database Migration Verification

This section verifies the database is in the correct state before deployment. Completion time: ~3 minutes.

**Objective**: Ensure database schema matches the code being deployed (no pending migrations, no conflicts).

### Step 1: Check Current Migration Status (Local)

```bash
#!/bin/bash
echo "=== Database Migration Status Check ==="
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# If using Alembic for migrations:
echo ""
echo "Checking Alembic migration status..."

if command -v alembic &> /dev/null; then
  echo "Current revision:"
  alembic current
  
  echo ""
  echo "Latest (head) revision:"
  alembic heads
  
  echo ""
  echo "Pending migrations (if any):"
  alembic history | head -5
else
  echo "Alembic not found. If using SQLAlchemy ORM directly, run ORM migrations manually."
fi

# If using direct ORM (no Alembic):
# python -c "from app.models import Base; Base.metadata.create_all(bind=engine)"
# (adjust import path for your setup)
```

**Expected Output** (if using Alembic):
```
=== Database Migration Status Check ===

Checking Alembic migration status...
Current revision:
abc123def456 (head)

Latest (head) revision:
abc123def456 (Phase 5 A11y deployment) -> None

Pending migrations (if any):
None (up to date)
```

**Success Criteria**:
- Current revision matches head revision
- No pending migrations
- No "ERROR" or "FAILED" messages

**If there are pending migrations**:
1. DO NOT PROCEED with deployment
2. Apply migrations locally first: `alembic upgrade head`
3. Test application locally to verify schema changes work
4. Only then proceed with deployment

### Step 2: Verify Database Accessibility from Production (if database is remote)

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'DB_CHECK'
echo "=== Production Database Connectivity Check ==="

# Adjust these for your database type and location
DB_HOST="[database-host]"  # e.g., "db.internal.company.com" or "127.0.0.1"
DB_PORT="5432"              # e.g., 5432 for PostgreSQL, 3306 for MySQL
DB_USER="[database-user]"
DB_NAME="[database-name]"

echo "Testing connectivity to: $DB_HOST:$DB_PORT"

# Test with nc (netcat) — safe, no credentials needed
if nc -zv -w 5 "$DB_HOST" "$DB_PORT" &>/dev/null; then
  echo "✅ Database host is reachable on port $DB_PORT"
else
  echo "❌ FAILED: Cannot reach database on $DB_HOST:$DB_PORT"
  echo "   Check network connectivity and database service status"
  exit 1
fi

# Test with psql (if PostgreSQL) or mysql (if MySQL)
# Example for PostgreSQL:
# PGPASSWORD="$DB_PASSWORD" psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -c "SELECT 1;"

echo ""
echo "If using local SQLite, database file check:"
if [ -f "/path/to/database.db" ]; then
  echo "✅ SQLite database file exists"
  ls -lah /path/to/database.db
else
  echo "⚠️  SQLite database file not found (may be created on first run)"
fi
DB_CHECK
```

**Expected Output**:
```
=== Production Database Connectivity Check ===

Testing connectivity to: db.internal.company.com:5432
✅ Database host is reachable on port 5432

If using local SQLite, database file check:
✅ SQLite database file exists
-rw-r--r-- 1 ubuntu ubuntu 4.5M Jun 12 08:00 /path/to/database.db
```

**If database is not reachable**:
1. Check network connectivity from production host: `ping [db-host]`
2. Verify database service is running on the remote host
3. Check firewall rules allow traffic on database port
4. If cannot be resolved, DO NOT PROCEED with deployment

### Step 3: Pre-Deployment Database Backup (Safety)

Create a backup of the database before deployment (can be used for emergency rollback):

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'DB_BACKUP'
echo "=== Creating Pre-Deployment Database Backup ==="

BACKUP_DIR="/opt/db-backups"
mkdir -p "$BACKUP_DIR"

# For PostgreSQL:
if command -v pg_dump &> /dev/null; then
  BACKUP_FILE="$BACKUP_DIR/open-repo-$(date +%Y%m%d-%H%M%S).sql.gz"
  pg_dump [database-connection-string] | gzip > "$BACKUP_FILE"
  echo "✅ PostgreSQL backup created: $BACKUP_FILE"
  ls -lah "$BACKUP_FILE"
fi

# For SQLite:
if [ -f "/path/to/database.db" ]; then
  BACKUP_FILE="$BACKUP_DIR/open-repo-$(date +%Y%m%d-%H%M%S).db.bak"
  cp /path/to/database.db "$BACKUP_FILE"
  echo "✅ SQLite backup created: $BACKUP_FILE"
  ls -lah "$BACKUP_FILE"
fi
DB_BACKUP
```

**Expected Output**:
```
=== Creating Pre-Deployment Database Backup ===

✅ SQLite backup created: /opt/db-backups/open-repo-20260612-085930.db.bak
-rw-r--r-- 1 ubuntu ubuntu 4.5M Jun 12 08:59 /opt/db-backups/open-repo-20260612-085930.db.bak
```

---

## SECTION 4: Deployment Execution (Detailed Steps)

Follow these steps in order. Do **not** skip or reorder steps.

### Pre-Execution: Final Sanity Checks (3 minutes)

```bash
#!/bin/bash
echo "=== Final Pre-Deployment Sanity Checks ==="

# 1. Confirm on correct branch
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "master" ]; then
  echo "❌ ERROR: Not on master branch (currently on: $CURRENT_BRANCH)"
  exit 1
fi
echo "✅ On master branch"

# 2. Confirm no uncommitted changes
if ! git diff-index --quiet HEAD --; then
  echo "❌ ERROR: Uncommitted changes in working tree"
  git status
  exit 1
fi
echo "✅ No uncommitted changes"

# 3. Confirm network access to production
ping -c 1 -W 5 100.70.184.84 > /dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "❌ ERROR: Cannot reach production host 100.70.184.84"
  exit 1
fi
echo "✅ Can reach production host"

# 4. Confirm SSH access
ssh -i ~/.ssh/production_key -o StrictHostKeyChecking=no ubuntu@100.70.184.84 \
  'echo "SSH connection verified"' > /dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "❌ ERROR: Cannot SSH to production host"
  exit 1
fi
echo "✅ SSH access confirmed"

echo ""
echo "All pre-execution checks passed. Deployment may proceed."
```

**Run this before proceeding**:
```bash
bash /tmp/final-sanity-checks.sh
```

### Deployment Step 1: Pull Latest Code on Production (1 minute)

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'STEP1'
echo "=== STEP 1: Pull Latest Code ==="

cd /home/awank/dev/SuperClaude_Framework/projects/open-repo
echo "Current directory: $(pwd)"

# Fetch latest from origin
echo "Fetching latest code from origin/master..."
git fetch origin master

# Show what will be deployed
echo ""
echo "Latest commit:"
git log --oneline origin/master | head -1

# Verify commit matches local
LOCAL_COMMIT=$(git log --oneline -1)
REMOTE_COMMIT=$(git log --oneline origin/master | head -1)

if [ "$LOCAL_COMMIT" = "$REMOTE_COMMIT" ]; then
  echo "✅ Local and remote commits match"
else
  echo "⚠️  Commits differ (local: $LOCAL_COMMIT, remote: $REMOTE_COMMIT)"
  echo "   This is OK if changes were just pushed"
fi
STEP1
```

**Expected Output**:
```
=== STEP 1: Pull Latest Code ===

Current directory: /home/awank/dev/SuperClaude_Framework/projects/open-repo
Fetching latest code from origin/master...

Latest commit:
abc123d feat(open-repo): Phase 5 A11y verification deployment

✅ Local and remote commits match
```

**If error**: Check git connectivity and branch status. If "fatal: unable to access", check GitHub SSH/HTTPS credentials.

---

### Deployment Step 2: Stop Running Application (2 minutes)

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'STEP2'
echo "=== STEP 2: Stop Running Application ==="

echo "Stopping service: open-repo"
sudo systemctl stop open-repo

# Wait for graceful shutdown
echo "Waiting for graceful shutdown (3 seconds)..."
sleep 3

# Verify stopped
echo ""
echo "Verifying process is stopped..."
if ps aux | grep -E "uvicorn.*open" | grep -v grep > /dev/null; then
  echo "⚠️  Process still running. Attempting graceful termination..."
  pkill -f "uvicorn.*open"
  sleep 2
  if ps aux | grep -E "uvicorn.*open" | grep -v grep > /dev/null; then
    echo "❌ Process still running. Using hard kill..."
    sudo pkill -9 -f "uvicorn.*open"
  fi
fi

# Final verification
if ! ps aux | grep -E "uvicorn.*open" | grep -v grep > /dev/null; then
  echo "✅ Application stopped successfully"
else
  echo "❌ FAILED: Application still running. Manual intervention required."
  exit 1
fi

# Show service status
echo ""
echo "Service status:"
sudo systemctl status open-repo || echo "(Service is stopped)"
STEP2
```

**Expected Output**:
```
=== STEP 2: Stop Running Application ===

Stopping service: open-repo
Waiting for graceful shutdown (3 seconds)...

Verifying process is stopped...
✅ Application stopped successfully

Service status:
● open-repo.service - Open-Repo OPDS Server
     Loaded: loaded (/etc/systemd/system/open-repo.service; enabled; vendor preset: enabled)
     Active: inactive (dead) since Thu 2026-06-12 09:04:23 UTC; 2s ago
```

**If error**: Application may be hung. Run `sudo systemctl kill -9 open-repo` to force kill.

---

### Deployment Step 3: Backup Current Deployment (1 minute)

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'STEP3'
echo "=== STEP 3: Backup Current Deployment ==="

cd /home/awank/dev/SuperClaude_Framework/projects/open-repo

BACKUP_DIR="/opt/backups/open-repo-$(date +%Y%m%d-%H%M%S)"
mkdir -p /opt/backups

echo "Creating backup directory: $BACKUP_DIR"
cp -r . "$BACKUP_DIR"

if [ -d "$BACKUP_DIR" ]; then
  echo "✅ Backup created successfully"
  echo "Location: $BACKUP_DIR"
  du -sh "$BACKUP_DIR"
else
  echo "❌ FAILED: Backup directory not created"
  exit 1
fi

# Show recent backups
echo ""
echo "Recent backups:"
ls -lt /opt/backups | head -5
STEP3
```

**Expected Output**:
```
=== STEP 3: Backup Current Deployment ===

Creating backup directory: /opt/backups/open-repo-20260612-090420
✅ Backup created successfully
Location: /opt/backups/open-repo-20260612-090420
245M	/opt/backups/open-repo-20260612-090420

Recent backups:
total 490M
drwxr-xr-x ubuntu ubuntu 4.0K Jun 12 09:04 open-repo-20260612-090420
drwxr-xr-x ubuntu ubuntu 4.0K Jun 11 14:23 open-repo-20260611-142301
```

**If backup fails**: Check disk space with `df -h /`. If <10GB free, this may fail.

---

### Deployment Step 4: Deploy New Code (2 minutes)

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'STEP4'
echo "=== STEP 4: Deploy New Code ==="

cd /home/awank/dev/SuperClaude_Framework/projects/open-repo

echo "Checking current git status..."
git status

echo ""
echo "Resetting to origin/master..."
git fetch origin master
git reset --hard origin/master

echo ""
echo "Current deployed commit:"
git log --oneline -1

echo ""
echo "✅ Code deployed"
STEP4
```

**Expected Output**:
```
=== STEP 4: Deploy New Code ===

Checking current git status...
On branch master
nothing to commit, working tree clean

Resetting to origin/master...
HEAD is now at abc123d feat(open-repo): Phase 5 A11y verification deployment

Current deployed commit:
abc123d feat(open-repo): Phase 5 A11y verification deployment

✅ Code deployed
```

**If error**: Git may fail if network is down or repository is locked. See troubleshooting section.

---

### Deployment Step 5: Install Python Dependencies (2 minutes)

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'STEP5'
echo "=== STEP 5: Install Python Dependencies ==="

cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# Verify venv exists
if [ ! -d "/opt/venv/open-repo" ]; then
  echo "Creating new virtual environment..."
  python3 -m venv /opt/venv/open-repo
fi

# Activate venv
source /opt/venv/open-repo/bin/activate

echo "Python: $(python --version)"
echo "Pip: $(pip --version)"

echo ""
echo "Upgrading pip, setuptools, wheel..."
pip install --upgrade pip setuptools wheel

echo ""
echo "Installing requirements..."
pip install -r requirements.txt

echo ""
echo "Verifying critical dependencies..."
pip list | grep -E "fastapi|sqlalchemy|pydantic|uvicorn"

if [ $? -eq 0 ]; then
  echo "✅ Dependencies installed successfully"
else
  echo "❌ WARNING: Could not verify all dependencies"
  exit 1
fi
STEP5
```

**Expected Output**:
```
=== STEP 5: Install Python Dependencies ===

Creating new virtual environment...
Python: Python 3.9.2
Pip: pip 21.0.1

Upgrading pip, setuptools, wheel...
Successfully installed pip-25.1.2 setuptools-68.0.0 wheel-0.41.2

Installing requirements...
Successfully installed fastapi==0.95.0 sqlalchemy==2.0.0 ...

Verifying critical dependencies...
fastapi                 0.95.0
sqlalchemy              2.0.0
pydantic                2.0.0
uvicorn                 0.21.0

✅ Dependencies installed successfully
```

**If pip fails** (especially on ARM64):
- libzim compilation may fail. See PHASE_5.1_POST_MERGE_DEPLOYMENT_CHECKLIST.md for ARM64 workarounds
- Continue deployment; libzim may not be strictly required for June 12 deployment

---

### Deployment Step 6: Database Migrations (1 minute)

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'STEP6'
echo "=== STEP 6: Database Migrations ==="

cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
source /opt/venv/open-repo/bin/activate

echo "Checking for pending migrations..."

# If using Alembic:
if [ -d "alembic" ]; then
  echo "Using Alembic for migrations..."
  
  echo "Current revision:"
  alembic current
  
  echo ""
  echo "Applying any pending migrations..."
  alembic upgrade head
  
  if [ $? -eq 0 ]; then
    echo "✅ Migrations applied (or no migrations needed)"
  else
    echo "❌ FAILED: Migration failed"
    exit 1
  fi
else
  echo "⚠️  Alembic not found. Assuming no migrations needed (A11y changes are CSS/JS only)."
  echo "✅ No migrations required for Phase 5 A11y deployment"
fi
STEP6
```

**Expected Output**:
```
=== STEP 6: Database Migrations ===

Checking for pending migrations...
Using Alembic for migrations...
Current revision:
abc123def456 (head)

Applying any pending migrations...
INFO [alembic.runtime.migration] Context impl PostgresqlImpl with target metadata...
INFO [alembic.runtime.migration] Will assume transactional DDL.
✅ Migrations applied (or no migrations needed)
```

**If migrations fail**:
- Do NOT proceed
- Investigate error: `alembic history | grep -A5 "ERROR"`
- Rollback migration: `alembic downgrade -1` (if safe)
- Or execute rollback procedure if database is corrupted

---

### Deployment Step 7: Start Application (2 minutes)

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'STEP7'
echo "=== STEP 7: Start Application ==="

echo "Starting service: open-repo"
sudo systemctl start open-repo

echo "Waiting for application startup (5 seconds)..."
sleep 5

echo ""
echo "Checking service status..."
if sudo systemctl is-active --quiet open-repo; then
  echo "✅ Service is active"
  sudo systemctl status open-repo | head -5
else
  echo "❌ FAILED: Service failed to start"
  echo ""
  echo "Recent service logs:"
  sudo journalctl -u open-repo -n 30
  exit 1
fi

echo ""
echo "Checking if uvicorn process is running..."
if ps aux | grep -E "uvicorn" | grep -v grep > /dev/null; then
  echo "✅ Uvicorn process running"
  ps aux | grep "uvicorn" | grep -v grep | head -1
else
  echo "❌ FAILED: Uvicorn process not found"
  exit 1
fi

echo ""
echo "✅ Application started successfully"
STEP7
```

**Expected Output**:
```
=== STEP 7: Start Application ===

Starting service: open-repo
Waiting for application startup (5 seconds)...

Checking service status...
✅ Service is active
● open-repo.service - Open-Repo OPDS Server
     Loaded: loaded (/etc/systemd/system/open-repo.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2026-06-12 09:07:12 UTC; 1s ago

Checking if uvicorn process is running...
✅ Uvicorn process running
ubuntu 12345 0.5 1.2 123456 45678 ? Ssl 09:07 0:00 uvicorn app.main:app --host 127.0.0.1 --port 8000

✅ Application started successfully
```

**If start fails**:
- Check logs: `sudo journalctl -u open-repo -n 50`
- Common issues: Missing dependencies, database connection, port already in use
- See troubleshooting section at end of document

---

## SECTION 5: Post-Deployment Health Verification (10 minutes)

### Verification Step 1: Health Endpoint (1 minute)

```bash
echo "=== POST-DEPLOYMENT: Health Endpoint Check ==="

echo "Testing health endpoint..."
HEALTH_RESPONSE=$(curl -s -w "\n%{http_code}" http://100.70.184.84:8000/health)
HTTP_CODE=$(echo "$HEALTH_RESPONSE" | tail -1)
BODY=$(echo "$HEALTH_RESPONSE" | head -n -1)

echo "HTTP Status: $HTTP_CODE"
echo "Response body:"
echo "$BODY" | jq . || echo "$BODY"

if [ "$HTTP_CODE" = "200" ]; then
  echo "✅ Health endpoint OK"
else
  echo "❌ FAILED: Health endpoint returned $HTTP_CODE"
  exit 1
fi
```

**Expected Output**:
```
=== POST-DEPLOYMENT: Health Endpoint Check ===

Testing health endpoint...
HTTP Status: 200
Response body:
{
  "status": "ok",
  "timestamp": "2026-06-12T09:08:45Z"
}
✅ Health endpoint OK
```

---

### Verification Step 2: Documentation Endpoints (2 minutes)

```bash
echo "=== POST-DEPLOYMENT: Documentation Endpoints Check ==="

# Check Swagger UI
echo "Checking /docs (Swagger UI)..."
DOCS_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://100.70.184.84:8000/docs)
if [ "$DOCS_CODE" = "200" ]; then
  echo "✅ /docs endpoint OK (HTTP 200)"
else
  echo "❌ /docs failed (HTTP $DOCS_CODE)"
fi

# Check ReDoc
echo "Checking /redoc (ReDoc)..."
REDOC_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://100.70.184.84:8000/redoc)
if [ "$REDOC_CODE" = "200" ]; then
  echo "✅ /redoc endpoint OK (HTTP 200)"
else
  echo "❌ /redoc failed (HTTP $REDOC_CODE)"
fi

# Check OpenAPI schema
echo "Checking /openapi.json (OpenAPI schema)..."
OPENAPI_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://100.70.184.84:8000/openapi.json)
if [ "$OPENAPI_CODE" = "200" ]; then
  echo "✅ /openapi.json OK (HTTP 200)"
else
  echo "❌ /openapi.json failed (HTTP $OPENAPI_CODE)"
fi

if [ "$DOCS_CODE" = "200" ] && [ "$REDOC_CODE" = "200" ] && [ "$OPENAPI_CODE" = "200" ]; then
  echo "✅ All documentation endpoints OK"
else
  echo "❌ Some documentation endpoints failed"
fi
```

**Expected Output**:
```
=== POST-DEPLOYMENT: Documentation Endpoints Check ===

Checking /docs (Swagger UI)...
✅ /docs endpoint OK (HTTP 200)
Checking /redoc (ReDoc)...
✅ /redoc endpoint OK (HTTP 200)
Checking /openapi.json (OpenAPI schema)...
✅ /openapi.json OK (HTTP 200)
✅ All documentation endpoints OK
```

---

### Verification Step 3: OPDS Endpoints (3 minutes)

```bash
echo "=== POST-DEPLOYMENT: OPDS Endpoints Check ==="

# Check OPDS root catalog
echo "Checking /api/v2/opds/root.xml..."
ROOT_CODE=$(curl -s -o /dev/null -w "%{http_code}" \
  -H "Accept: application/atom+xml" \
  http://100.70.184.84:8000/api/v2/opds/root.xml)

if [ "$ROOT_CODE" = "200" ]; then
  echo "✅ OPDS root catalog OK (HTTP 200)"
  # Show first few lines
  curl -s -H "Accept: application/atom+xml" \
    http://100.70.184.84:8000/api/v2/opds/root.xml | head -3
else
  echo "❌ OPDS root catalog failed (HTTP $ROOT_CODE)"
fi

# Check OPDS entries feed
echo ""
echo "Checking /api/v2/opds/entries..."
ENTRIES_CODE=$(curl -s -o /dev/null -w "%{http_code}" \
  -H "Accept: application/atom+xml" \
  http://100.70.184.84:8000/api/v2/opds/entries)

if [ "$ENTRIES_CODE" = "200" ]; then
  echo "✅ OPDS entries feed OK (HTTP 200)"
  # Show first few lines
  curl -s -H "Accept: application/atom+xml" \
    http://100.70.184.84:8000/api/v2/opds/entries | head -3
else
  echo "❌ OPDS entries feed failed (HTTP $ENTRIES_CODE)"
fi

if [ "$ROOT_CODE" = "200" ] && [ "$ENTRIES_CODE" = "200" ]; then
  echo "✅ All OPDS endpoints OK"
else
  echo "❌ Some OPDS endpoints failed"
fi
```

**Expected Output**:
```
=== POST-DEPLOYMENT: OPDS Endpoints Check ===

Checking /api/v2/opds/root.xml...
✅ OPDS root catalog OK (HTTP 200)
<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>Open Repository</title>

Checking /api/v2/opds/entries...
✅ OPDS entries feed OK (HTTP 200)
<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>All Available Books</title>

✅ All OPDS endpoints OK
```

---

### Verification Step 4: Application Logs Check (2 minutes)

```bash
echo "=== POST-DEPLOYMENT: Application Logs Review ==="

ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'LOGS_CHECK'
echo "Recent application logs (last 50 lines):"
sudo journalctl -u open-repo -n 50

echo ""
echo "Checking for CRITICAL or ERROR level messages:"
ERRORS=$(sudo journalctl -u open-repo --since "5 minutes ago" | \
  grep -E "CRITICAL|ERROR" | wc -l)

if [ "$ERRORS" -eq 0 ]; then
  echo "✅ No critical errors in recent logs"
else
  echo "⚠️  Found $ERRORS error messages in recent logs. Review above."
  sudo journalctl -u open-repo --since "5 minutes ago" | grep -E "CRITICAL|ERROR"
fi
LOGS_CHECK
```

**Expected Output**:
```
=== POST-DEPLOYMENT: Application Logs Review ===

Recent application logs (last 50 lines):
Jun 12 09:07:12 raspby1 systemd[1]: Started Open-Repo OPDS Server.
Jun 12 09:07:13 raspby1 open-repo[12345]: INFO:     Uvicorn server running on http://127.0.0.1:8000
Jun 12 09:07:13 raspby1 open-repo[12345]: INFO:     Application startup complete
Jun 12 09:07:15 raspby1 open-repo[12345]: INFO:     GET /health - 200
...

Checking for CRITICAL or ERROR level messages:
✅ No critical errors in recent logs
```

---

## SECTION 6: Deployment Completion & Sign-Off

### Deployment Completion Checklist

If all verification steps passed, mark deployment as complete:

- [ ] Pre-flight environment variables verified
- [ ] Database migrations checked and applied (or not needed)
- [ ] Code deployed and current commit verified
- [ ] Dependencies installed without errors
- [ ] Application started and process verified
- [ ] Health endpoint responding with 200
- [ ] /docs and /redoc endpoints responding
- [ ] OPDS endpoints responding with valid XML
- [ ] Application logs show no critical errors
- [ ] No resource exhaustion detected (CPU/memory/disk)

**If all checked**: Proceed to **ACTIVE MONITORING** phase (see POST_DEPLOYMENT_MONITORING_PLAN.md)

**If any item failed**: Go to troubleshooting section, then decide: fix or rollback

---

## SECTION 7: Stakeholder Communication Templates

Use these templates to notify stakeholders at key points.

### Template 1: Pre-Deployment Notification (2 hours before)

**To**: #deployments Slack channel (or distribution list)  
**Send At**: 07:00 UTC (2 hours before 09:00 UTC deployment start)

```
🚀 DEPLOYMENT ALERT: Open-Repo Phase 5 Production Deployment

Deployment will start at 09:00 UTC on June 12, 2026.

Expected impact:
• Maintenance window: 09:00–11:00 UTC (2 hours maximum)
• Service may be unavailable during deployment (estimated 25–45 minutes)
• OPDS endpoints, Swagger UI, and ReDoc will be inaccessible during deployment
• Data is safe; no data loss expected

Timeline:
• 09:00 UTC: Deployment starts
• 09:45 UTC: Expected service restoration
• 10:00–11:00 UTC: Active monitoring (may have higher latency)

Action required:
• Do not deploy code or infrastructure during this window
• Do not restart services during this window

Questions? Reach out to [deployer name/team]

Thank you for your patience.
```

---

### Template 2: Deployment In-Progress Notification

**To**: #deployments Slack channel  
**Send At**: 09:00 UTC (when deployment starts)

```
🔄 DEPLOYMENT IN PROGRESS: Open-Repo Phase 5

Deployment started at 09:00 UTC. Currently executing deployment steps.

Expected completion: 09:45 UTC (45 minutes from now)
Status updates: Will post every 15 minutes

Current step: [Pre-flight checks]

Please avoid any infrastructure changes during this window.
```

---

### Template 3: Deployment Success Notification (Recommend using actual test results)

**To**: #deployments Slack channel  
**Send At**: When all verification steps complete (~09:50 UTC)

```
✅ DEPLOYMENT COMPLETE: Open-Repo Phase 5

Deployment completed successfully at [actual time] UTC.

Verification results:
✅ Health endpoint: 200 OK
✅ Swagger UI (/docs): 200 OK
✅ ReDoc (/redoc): 200 OK
✅ OPDS root endpoint: 200 OK
✅ OPDS entries endpoint: 200 OK
✅ Application logs: No critical errors
✅ System resources: Normal (CPU idle >50%, memory available >2GB)

Deployment details:
• Deployment window: 09:00–10:00 UTC (actual: [actual duration])
• Rolled back: No
• Issues detected: None

Active monitoring: Ongoing until 10:45 UTC (60 minutes from start)
Next steps: Passive monitoring for 24 hours

Thank you for your patience during the maintenance window.
```

---

### Template 4: Rollback Notification (If Needed)

**To**: #deployments Slack channel + team lead  
**Send At**: Immediately when rollback decision made

```
⚠️  ROLLBACK ACTIVATED: Open-Repo Phase 5

Deployment encountered a critical issue and has been rolled back to previous version.

Issue detected: [Brief description]
Time of rollback: [UTC timestamp]
Rollback status: In progress (5–10 minutes expected)

Actions taken:
1. Service stopped
2. Backup restored
3. Previous version starting

Expected service restoration: [time]

Incident report: Will be published within 24 hours

We apologize for the disruption. Engineering team is investigating root cause.
```

---

## SECTION 8: Troubleshooting Common Issues

See **DEPLOYMENT_JUNE_12_RUNBOOK.md** Appendix for detailed troubleshooting. Key issues:

| Issue | Symptom | Quick Fix |
|-------|---------|-----------|
| SSH connection refused | `Connection refused port 22` | Check network routing, verify host is up with ping |
| Git fetch fails | `fatal: unable to access` | Check GitHub credentials, internet connectivity |
| Pip install fails | `ERROR: ... failed building wheel` | For libzim on ARM64, see PHASE_5.1 docs |
| Service won't start | `systemctl start` fails | Check logs: `sudo journalctl -u open-repo -n 50` |
| Health endpoint returns 500 | App crashed | Check database connectivity, review logs |
| OPDS returns 500 | OPDSGenerator error | Check database has ZIM export table, data exists |

---

## SECTION 9: Post-Deployment (After 11:00 UTC)

### Immediate (11:00–12:00 UTC): Active Monitoring
See POST_DEPLOYMENT_MONITORING_PLAN.md Section 1

### 24 Hours Later (June 13, 09:00 UTC): Final Verification
- Verify no errors accumulated during 24-hour passive monitoring period
- Check that error rate is still near 0%
- Review system resource usage trends
- Archive monitoring logs
- Mark deployment as officially complete

---

## Document Sign-Off

**Deployment Executed By**: ________________  
**Execution Date/Time**: ________________ UTC  
**Pre-flight Duration**: _____ minutes  
**Deployment Duration**: _____ minutes  
**Health Check Duration**: _____ minutes  
**Total Duration**: _____ minutes (target: 45 min)  

**Pre-Deployment Status**: 
[ ] All checks passed [ ] Minor issues (documented) [ ] Failed (abort)

**Deployment Status**: 
[ ] SUCCESS [ ] PARTIAL SUCCESS (issues but running) [ ] FAILED (rollback executed)

**Issues Encountered**: 
_________________________________________________________________

**Monitoring Status**: 
[ ] Active monitoring started [ ] Issues during monitoring [ ] Monitoring complete

**Next Steps**: 
_________________________________________________________________

---

**Enhanced Procedures Version**: 1.0  
**Created**: June 6, 2026  
**Based On**: DEPLOYMENT_JUNE_12_RUNBOOK.md (original runbook)  
**Valid For**: June 12, 2026 deployment  
**Last Updated**: June 6, 2026
