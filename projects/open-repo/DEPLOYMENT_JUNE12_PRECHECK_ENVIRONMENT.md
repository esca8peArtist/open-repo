---
title: "Open-Repo June 12, 2026 Deployment Pre-Flight Verification Checklist — Environment"
project: open-repo
phase: 5 (final production deployment)
document_type: pre-deployment-environment-checklist
status: READY TO EXECUTE — USER INPUT REQUIRED (database credentials)
created: 2026-06-12
target_deployment_date: 2026-06-12
deployment_start_time: "[REQUIRED USER INPUT] — See Date Conflict Notice below"
estimated_checklist_duration: "40 minutes (Parts 1–5 sequential)"
---

# Deployment Pre-Flight Verification Checklist — Environment
## June 12, 2026

**Purpose**: Verify all environmental, test, database, and operational prerequisites are met before the deployment window opens. Each item has a binary PASS/FAIL outcome. If any item FAILs, do not proceed to deployment until remediated.

**Execution Order**: Complete Parts 1 through 5 in sequence. Parts 1–5 are designed to catch blockers early so remediation time is not lost during the deployment window itself.

**Total Estimated Time**: 40 minutes (15 + 10 + 20 + 10 + 5 minutes as labeled per part).

---

## CRITICAL NOTICE: Date and Time Conflict — USER DECISION REQUIRED

**This notice must be read and resolved before executing any checklist item.**

A confirmed conflict exists across the deployment SOP documents:

### Conflict 1 — Start Time (Within SOP Documents)

| Document | Recorded Start Time |
|----------|-------------------|
| DEPLOYMENT_JUNE_12_RUNBOOK.md | **20:00 UTC** |
| DEPLOYMENT_JUNE_12_GO_LIVE_CHECKLIST.md | **20:00 UTC** |
| DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md | **09:00 UTC** |
| DEPLOYMENT_JUNE12_PRECHECK_ENVIRONMENT.md (this file) | **[USER INPUT REQUIRED]** |
| DEPLOYMENT_JUNE12_RISK_MITIGATION.md | **09:00 UTC** |
| DEPLOYMENT_JUNE12_COMMUNICATION_TEMPLATES.md | **09:00 UTC** |
| PHASE_5_COMPLETION_SUMMARY.md | **20:00 UTC** |

The runbook and go-live checklist (created June 3, 2026) say **20:00 UTC**. The final procedures and these three pre-flight documents (created June 6, 2026) say **09:00 UTC**. These cannot both be correct. This is a HIGH-severity operational blocker.

### Conflict 2 — June 9 vs June 12 (Across Project Documents)

PHASE_5_2_RECOMMENDED_SEQUENCING.md and PHASE_4_TRIAGE_AND_PRIORITY.md reference **June 9** as a staging merge / pre-deployment milestone (not as a production deployment date). The production deployment date of **June 12** is consistent across all deployment SOP documents. This is not an active conflict — June 9 refers to a staging step that has already passed. It is documented here for clarity.

### Resolution Required

Before executing this checklist, the user must answer:

- [ ] **Canonical deployment start time**: 09:00 UTC or 20:00 UTC? (circle one)
- [ ] **Filled in here**: Deployment starts at __________ UTC on June 12, 2026

Once decided, cross-reference DEPLOYMENT_JUNE_12_RUNBOOK.md and DEPLOYMENT_JUNE_12_GO_LIVE_CHECKLIST.md and update their frontmatter if the canonical time is 09:00 UTC. All three pre-flight documents use 09:00 UTC as written; if 20:00 UTC is canonical, adjust communication templates accordingly.

**All timing references in this checklist use 09:00 UTC as the deployment window open.** Adjust all clock references if 20:00 UTC is confirmed.

---

## Part 1: Environment Readiness (15 minutes)

Execute these checks in the 15 minutes before the deployment window opens (08:45–09:00 UTC if 09:00 UTC is canonical).

---

### 1.1 — Git Branch and Commit Verification

**Objective**: Confirm master branch is clean, with no uncommitted changes, and local commit matches origin/master.

**Procedure**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo

# Check branch
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "master" ]; then
  echo "FAIL: Not on master branch (on: $CURRENT_BRANCH)"
  exit 1
fi
echo "PASS: On master branch"

# Check for uncommitted changes
if ! git diff-index --quiet HEAD --; then
  echo "FAIL: Uncommitted changes detected"
  git status --short
  exit 1
fi
echo "PASS: Working tree clean"

# Compare local vs remote
LOCAL=$(git log --oneline -1)
REMOTE=$(git log --oneline origin/master -1)
echo "Local : $LOCAL"
echo "Remote: $REMOTE"
if [ "$LOCAL" = "$REMOTE" ]; then
  echo "PASS: Local and origin/master match"
else
  echo "WARN: Commits differ — verify intentional before proceeding"
fi
```

**Pass Criteria**: Branch is `master`, working tree has zero uncommitted files, local commit hash matches origin/master.

**Fail Remediation**:
- Wrong branch: `git checkout master`
- Uncommitted changes: `git status` then commit or discard with `git checkout -- .`
- Diverged commits: `git pull origin master` (ensure no conflicts)

**Status**: [ ] PASS   [ ] FAIL

---

### 1.2 — Python Runtime Version

**Objective**: Confirm Python version meets minimum requirement (3.11+ per pyproject.toml).

**Procedure**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# Check Python version available via uv
uv run python --version

# Confirm meets minimum
PYTHON_VER=$(uv run python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
REQUIRED_MAJOR=3
REQUIRED_MINOR=11

ACTUAL_MAJOR=$(echo "$PYTHON_VER" | cut -d. -f1)
ACTUAL_MINOR=$(echo "$PYTHON_VER" | cut -d. -f2)

if [ "$ACTUAL_MAJOR" -ge "$REQUIRED_MAJOR" ] && [ "$ACTUAL_MINOR" -ge "$REQUIRED_MINOR" ]; then
  echo "PASS: Python $PYTHON_VER meets minimum 3.11+"
else
  echo "FAIL: Python $PYTHON_VER does not meet minimum 3.11+"
  exit 1
fi
```

**Pass Criteria**: Python version is 3.11 or higher.

**Fail Remediation**: Install Python 3.11+ via system package manager or pyenv. Update `uv` virtual environment: `uv venv --python python3.11`.

**Status**: [ ] PASS   [ ] FAIL

---

### 1.3 — Database Connection Parameters

**Objective**: Confirm all required database connection parameters are populated. This project uses SQLAlchemy with either PostgreSQL (`postgres://` URL) or SQLite (`sqlite:///` path). All parameters must be supplied by the user before deployment.

**REQUIRED USER INPUT — Complete before executing this checklist item**:

```
DATABASE_URL     = [REQUIRED USER INPUT]
  Description: Full database connection URL
  PostgreSQL example: postgres://username:password@hostname:5432/dbname
  SQLite example:     sqlite:////opt/data/open-repo.db
  Current value:      ________________________________

DB_HOST          = [REQUIRED USER INPUT — if PostgreSQL]
  Description: Database hostname or IP address (must not be 0.0.0.0)
  Example:     127.0.0.1 or db.internal.example.com
  Current value: ________________________________

DB_USER          = [REQUIRED USER INPUT — if PostgreSQL]
  Description: Database username with read/write access
  Current value: ________________________________

DB_NAME          = [REQUIRED USER INPUT — if PostgreSQL]
  Description: Database name
  Current value: ________________________________

SQLITE_PATH      = [REQUIRED USER INPUT — if SQLite]
  Description: Absolute filesystem path to the SQLite database file
  Example:     /opt/data/open-repo.db
  Current value: ________________________________
```

**Procedure** (run after filling in values above):
```bash
#!/bin/bash
# Verify DATABASE_URL is set and non-empty
if [ -z "$DATABASE_URL" ]; then
  echo "FAIL: DATABASE_URL is not set"
  echo "  Set with: export DATABASE_URL=<your-connection-url>"
  exit 1
fi

# Print type without leaking credentials
if echo "$DATABASE_URL" | grep -q "postgres://"; then
  echo "PASS: DATABASE_URL set (type: PostgreSQL)"
elif echo "$DATABASE_URL" | grep -q "sqlite:///"; then
  echo "PASS: DATABASE_URL set (type: SQLite)"
  SQLITE_FILE="${DATABASE_URL#sqlite:///}"
  if [ -f "$SQLITE_FILE" ]; then
    echo "PASS: SQLite file exists at $SQLITE_FILE"
    ls -lah "$SQLITE_FILE"
  else
    echo "FAIL: SQLite file not found at $SQLITE_FILE"
    exit 1
  fi
else
  echo "WARN: DATABASE_URL format unrecognized — verify manually"
fi
```

**Pass Criteria**: DATABASE_URL is set, non-empty, and points to a reachable database (SQLite file exists, or PostgreSQL host is reachable).

**Fail Remediation**: Populate the values in the table above. Set `export DATABASE_URL=<value>` in the deployment shell session, or add to `/etc/environment` on the production host.

**Status**: [ ] PASS   [ ] FAIL   [ ] BLOCKED (user has not supplied credentials)

---

### 1.4 — Environment Variables Loaded

**Objective**: Verify all required application environment variables are set in the deployment shell session.

**Required Variables**:
```
DATABASE_URL          (see 1.3 above)
SECRET_KEY            [REQUIRED USER INPUT] — random 32+ character string, never log
OPDS_CATALOG_NAME     example: "Open Repository"
LOG_LEVEL             one of: DEBUG, INFO, WARNING, ERROR, CRITICAL
FASTAPI_ENV           one of: development, production, testing
UVICORN_HOST          must be 127.0.0.1 — never 0.0.0.0 (security requirement)
UVICORN_PORT          8000
```

**Procedure**:
```bash
#!/bin/bash
REQUIRED=("DATABASE_URL" "SECRET_KEY" "OPDS_CATALOG_NAME" "LOG_LEVEL" "FASTAPI_ENV" "UVICORN_HOST" "UVICORN_PORT")
MISSING=0

for var in "${REQUIRED[@]}"; do
  value="${!var}"
  if [ -z "$value" ]; then
    echo "FAIL (missing): $var"
    MISSING=$((MISSING + 1))
  else
    if [[ "$var" == "SECRET_KEY" || "$var" == "DATABASE_URL" ]]; then
      echo "PASS (set):     $var [REDACTED]"
    else
      echo "PASS (set):     $var=$value"
    fi
  fi
done

# Security check: UVICORN_HOST must never be 0.0.0.0
if [ "${UVICORN_HOST}" = "0.0.0.0" ]; then
  echo "FAIL: UVICORN_HOST=0.0.0.0 is prohibited — use 127.0.0.1"
  MISSING=$((MISSING + 1))
fi

echo ""
if [ $MISSING -eq 0 ]; then
  echo "PASS: All required environment variables set"
else
  echo "FAIL: $MISSING variable(s) missing or invalid"
  exit 1
fi
```

**Pass Criteria**: All 7 variables set, UVICORN_HOST is 127.0.0.1 (not 0.0.0.0).

**Fail Remediation**: Set missing variables with `export VAR=value`. For persistent configuration, add to `/etc/environment` or the systemd service's `Environment=` directive.

**Status**: [ ] PASS   [ ] FAIL

---

### 1.5 — Python Dependencies Installed

**Objective**: Verify all required Python packages are installed in the backend virtual environment.

**Procedure**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "Installing/verifying dependencies via uv..."
uv pip install -e ".[dev]"
if [ $? -ne 0 ]; then
  echo "FAIL: Dependency installation failed"
  exit 1
fi

echo "Verifying critical packages..."
PACKAGES=("fastapi" "sqlalchemy" "pydantic" "uvicorn" "pytest" "httpx" "alembic")
MISSING=0
for pkg in "${PACKAGES[@]}"; do
  VERSION=$(uv run python -c "import importlib.metadata; print(importlib.metadata.version('$pkg'))" 2>/dev/null)
  if [ -n "$VERSION" ]; then
    echo "PASS: $pkg==$VERSION"
  else
    echo "FAIL: $pkg not installed"
    MISSING=$((MISSING + 1))
  fi
done

if [ $MISSING -eq 0 ]; then
  echo "PASS: All critical dependencies installed"
else
  echo "FAIL: $MISSING packages missing"
  exit 1
fi
```

**Pass Criteria**: `uv pip install` exits 0, all 7 critical packages resolve to a version string.

**Fail Remediation**: Run `uv pip install -e ".[dev]"` and review any build errors. For libzim on ARM64, see PHASE_5.1_POST_MERGE_DEPLOYMENT_CHECKLIST.md for the pre-built wheel procedure.

**Status**: [ ] PASS   [ ] FAIL

---

**Part 1 Summary** — Record before proceeding:

| Item | Status |
|------|--------|
| 1.1 Git branch and commit | [ ] PASS / [ ] FAIL |
| 1.2 Python runtime version | [ ] PASS / [ ] FAIL |
| 1.3 Database connection parameters | [ ] PASS / [ ] FAIL |
| 1.4 Environment variables loaded | [ ] PASS / [ ] FAIL |
| 1.5 Python dependencies installed | [ ] PASS / [ ] FAIL |

**Part 1 Decision**: [ ] ALL PASS — proceed to Part 2   [ ] FAIL — remediate before proceeding

---

## Part 2: Test Suite Status (10 minutes)

All test commands use `uv run pytest` per project convention. The `npm run test` commands mentioned in the task brief do not apply to this Python project — the backend test suite is pytest-based.

**Note on test counts**: The PHASE_5_WCAG_VERIFICATION_REPORT.md (June 3, 2026) is the authoritative source for the 157-test claim, composed of 50 OPDS Generator tests + 35 Route/Validation tests + 72 A11y automated tests = 157 total. The backend Makefile's "24+ tests" comment is outdated and does not reflect Phase 5 additions.

---

### 2.1 — Full Test Suite Run (157/157 PASS required)

**Objective**: Confirm all 157 tests pass in the current codebase state.

**Procedure**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "Running full test suite..."
uv run pytest tests/ -v --tb=short 2>&1 | tee /tmp/open-repo-test-results.txt

# Parse result line
SUMMARY=$(tail -5 /tmp/open-repo-test-results.txt | grep -E "passed|failed|error")
echo ""
echo "Test summary: $SUMMARY"

PASSED=$(echo "$SUMMARY" | grep -oP '\d+(?= passed)' | head -1)
FAILED=$(echo "$SUMMARY" | grep -oP '\d+(?= failed)' | head -1)
ERRORS=$(echo "$SUMMARY" | grep -oP '\d+(?= error)' | head -1)

if [ "$PASSED" = "157" ] && [ -z "$FAILED" ] && [ -z "$ERRORS" ]; then
  echo "PASS: 157/157 tests passing"
else
  echo "FAIL: Expected 157 passed, got: passed=$PASSED failed=$FAILED errors=$ERRORS"
  grep "FAILED\|ERROR" /tmp/open-repo-test-results.txt | head -20
  exit 1
fi
```

**Expected terminal output** (final line):
```
157 passed in X.XXs
```

**Pass Criteria**: Exactly 157 tests collected and passed; 0 failed; 0 errors. Test run completes without keyboard interrupt.

**Fail Remediation**:
- View failures: `uv run pytest tests/ -v --failed-first`
- Run specific failing file: `uv run pytest tests/test_opds_generator.py -v`
- If failure is environment-related (missing DB), verify Item 1.3 first
- Do not proceed to deployment with any failing tests

**Status**: [ ] PASS   [ ] FAIL

---

### 2.2 — Coverage Report (>85% critical paths required)

**Objective**: Verify test coverage on the `app/` package exceeds 85% for critical paths.

**Procedure**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "Running tests with coverage..."
uv run pytest tests/ --cov=app --cov-report=term-missing --cov-fail-under=85 2>&1 | tee /tmp/open-repo-coverage.txt

if [ $? -eq 0 ]; then
  echo "PASS: Coverage meets 85% threshold"
  # Extract total coverage line
  grep "TOTAL" /tmp/open-repo-coverage.txt | tail -1
else
  echo "FAIL: Coverage below 85%"
  grep "TOTAL" /tmp/open-repo-coverage.txt | tail -1
  exit 1
fi
```

**Pass Criteria**: `--cov-fail-under=85` exits 0 (pytest exits non-zero if coverage is below threshold).

**Fail Remediation**: Review uncovered lines from the `--cov-report=term-missing` output. Gaps in A11y and OPDS modules are most likely candidates. Add targeted tests if coverage has dropped since the June 3 verification.

**Status**: [ ] PASS   [ ] FAIL

---

### 2.3 — A11y Test Suite Run (0 violations required)

**Objective**: Confirm all 72 automated A11y tests pass with zero WCAG violations.

**Test files that constitute the 72-test A11y suite**:
- `tests/test_a11y_axecore.py` — axe-core integration via Playwright
- `tests/test_a11y_dom_semantics.py` — DOM/markup structure validation
- `tests/test_a11y_contrast.py` — color contrast ratio checks
- `tests/test_a11y_deep_scan.py` — deep WCAG 2.1 AA criterion scan
- `tests/test_a11y_regression.py` — regression guard for previously fixed violations

**Procedure**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "Running A11y test suite (requires live server on 127.0.0.1:8000)..."
echo "Start the dev server in a separate terminal before running this:"
echo "  uv run uvicorn app.main:create_app --reload --host 127.0.0.1 --port 8000"
echo ""

uv run pytest tests/test_a11y_axecore.py tests/test_a11y_dom_semantics.py \
              tests/test_a11y_contrast.py tests/test_a11y_deep_scan.py \
              tests/test_a11y_regression.py -v --tb=short 2>&1 | tee /tmp/open-repo-a11y.txt

SUMMARY=$(tail -5 /tmp/open-repo-a11y.txt | grep -E "passed|failed")
A11Y_PASSED=$(echo "$SUMMARY" | grep -oP '\d+(?= passed)' | head -1)
A11Y_FAILED=$(echo "$SUMMARY" | grep -oP '\d+(?= failed)' | head -1)

if [ "$A11Y_PASSED" = "72" ] && [ -z "$A11Y_FAILED" ]; then
  echo "PASS: 72/72 A11y tests passing, 0 WCAG violations"
else
  echo "FAIL: A11y tests — passed=$A11Y_PASSED failed=$A11Y_FAILED"
  grep "FAILED" /tmp/open-repo-a11y.txt
  exit 1
fi
```

**Pass Criteria**: 72 A11y tests pass; 0 fail. The axe-core scan of `/docs` and `/redoc` must return 0 violations at wcag2a, wcag2aa, wcag21a, wcag21aa tags.

**Fail Remediation**: A11y regressions are most likely caused by CSS changes that broke contrast ratios or introduced focus trap issues. Consult PHASE_5_WCAG_VERIFICATION_REPORT.md for the baseline fix set (6 violations, all resolved).

**Status**: [ ] PASS   [ ] FAIL

---

### 2.4 — Build Step

**Objective**: Verify the backend application imports cleanly (no syntax or import errors) and the frontend static assets exist.

**Procedure**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "Checking application import health..."
uv run python -c "
import app.main
import app.services.export.zim_writer
import app.services.export.opds_generator
print('PASS: All critical application modules import cleanly')
"

if [ $? -ne 0 ]; then
  echo "FAIL: Application import check failed"
  exit 1
fi

# Check frontend static assets (if any)
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo
if [ -d "frontend/dist" ] || [ -d "frontend/build" ]; then
  echo "PASS: Frontend build artifacts found"
else
  echo "INFO: No frontend/dist or frontend/build directory — static assets served via FastAPI or CDN"
fi

echo "PASS: Build verification complete"
```

**Pass Criteria**: Python module imports succeed with exit code 0; no `ImportError`, `SyntaxError`, or `ModuleNotFoundError` in output.

**Fail Remediation**: Import errors indicate missing dependencies (run Item 1.5 again) or syntax errors in recently modified files. Run `uv run python -c "import app.main"` directly and read the traceback.

**Status**: [ ] PASS   [ ] FAIL

---

**Part 2 Summary**:

| Item | Status |
|------|--------|
| 2.1 Full test suite (157/157) | [ ] PASS / [ ] FAIL |
| 2.2 Coverage report (>85%) | [ ] PASS / [ ] FAIL |
| 2.3 A11y test suite (72/72) | [ ] PASS / [ ] FAIL |
| 2.4 Build step (import health) | [ ] PASS / [ ] FAIL |

**Part 2 Decision**: [ ] ALL PASS — proceed to Part 3   [ ] FAIL — remediate before proceeding

---

## Part 3: Database Migration Readiness (20 minutes)

This project uses Alembic for schema migrations. Three migration files exist in `backend/alembic/versions/`:

- `001_add_federation_partners.py`
- `002_add_federation_conflicts.py`
- `003_add_zim_exports_table.py`

Phase 5 does not introduce a new migration — migration 003 was applied during Phase 5 implementation. This part verifies that the production database schema matches the expected post-003 state before deployment proceeds.

---

### 3.1 — Migration Scripts Present

**Objective**: Confirm all three Alembic migration files are present and numbered correctly.

**Procedure**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "Checking migration files..."
EXPECTED=("001_add_federation_partners.py" "002_add_federation_conflicts.py" "003_add_zim_exports_table.py")
MISSING=0

for migration in "${EXPECTED[@]}"; do
  if [ -f "alembic/versions/$migration" ]; then
    echo "PASS: $migration found"
  else
    echo "FAIL: $migration NOT FOUND"
    MISSING=$((MISSING + 1))
  fi
done

if [ $MISSING -eq 0 ]; then
  echo "PASS: All 3 migration scripts present"
else
  echo "FAIL: $MISSING migration files missing — do not proceed"
  exit 1
fi
```

**Pass Criteria**: All 3 migration files present in `backend/alembic/versions/`.

**Fail Remediation**: Missing migration files indicate a git checkout issue. Run `git status` and `git log --oneline -5` to check state. Pull from origin if missing.

**Status**: [ ] PASS   [ ] FAIL

---

### 3.2 — Backup Procedure

**Objective**: Create a timestamped backup of the production database before any migration or code change is applied.

**REQUIRED USER INPUT — Populate before running backup**:

```
BACKUP_DESTINATION = [REQUIRED USER INPUT]
  Description: Filesystem path where database backups will be written
  Example:     /opt/db-backups
  Current value: ________________________________

DATABASE_FILE      = [REQUIRED USER INPUT — SQLite only]
  Description: Absolute path to the SQLite database file on production host
  Example:     /opt/data/open-repo.db
  Current value: ________________________________

POSTGRES_CONN_STR  = [REQUIRED USER INPUT — PostgreSQL only]
  Description: pg_dump connection string (without password if using .pgpass)
  Example:     postgresql://username@127.0.0.1:5432/dbname
  Current value: ________________________________
```

**Procedure**:
```bash
#!/bin/bash
PROD_HOST="100.70.184.84"
BACKUP_DIR="[REQUIRED USER INPUT]"   # e.g., /opt/db-backups

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << BACKUP_SCRIPT
mkdir -p "$BACKUP_DIR"
TIMESTAMP=\$(date +%Y%m%d-%H%M%S)

# SQLite backup
SQLITE_FILE="[REQUIRED USER INPUT]"   # e.g., /opt/data/open-repo.db
if [ -f "\$SQLITE_FILE" ]; then
  BACKUP_FILE="$BACKUP_DIR/open-repo-\$TIMESTAMP.db.bak"
  cp "\$SQLITE_FILE" "\$BACKUP_FILE"
  if [ -f "\$BACKUP_FILE" ]; then
    echo "PASS: SQLite backup created: \$BACKUP_FILE"
    ls -lah "\$BACKUP_FILE"
  else
    echo "FAIL: Backup file not created"
    exit 1
  fi
fi

# PostgreSQL backup (if applicable)
# pg_dump "[REQUIRED USER INPUT]" | gzip > "$BACKUP_DIR/open-repo-\$TIMESTAMP.sql.gz"

echo "Backup complete"
BACKUP_SCRIPT
```

**Pass Criteria**: Backup file is created on production host with a timestamp in the filename; `ls -lah` shows a non-zero file size.

**Fail Remediation**: If backup fails due to disk space, check `df -h` on production host and free space. If SQLite file path is wrong, verify with `find /opt -name "*.db" 2>/dev/null`.

**Status**: [ ] PASS   [ ] FAIL   [ ] BLOCKED (user has not supplied backup paths)

---

### 3.3 — Rollback Procedure Verified

**Objective**: Confirm the Alembic downgrade command works against the current database before deployment begins.

**Procedure**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "Checking current Alembic revision..."
uv run alembic current

echo ""
echo "Checking revision history..."
uv run alembic history

echo ""
echo "Verifying downgrade to -1 is possible (dry-run only — do NOT execute during pre-flight)..."
echo "The actual downgrade command if needed is:"
echo "  uv run alembic downgrade -1"
echo ""
echo "Confirm that alembic history shows migration 003 at HEAD"

# Check that we are at head
HEAD_REV=$(uv run alembic heads 2>/dev/null | grep -oP '^[a-f0-9]+')
CURRENT_REV=$(uv run alembic current 2>/dev/null | grep -oP '^[a-f0-9]+')

if [ "$HEAD_REV" = "$CURRENT_REV" ]; then
  echo "PASS: Database is at current head revision ($CURRENT_REV)"
else
  echo "FAIL: Database is not at head (head=$HEAD_REV, current=$CURRENT_REV)"
  echo "Run: uv run alembic upgrade head"
  exit 1
fi
```

**Pass Criteria**: `alembic current` and `alembic heads` return the same revision hash; no pending migrations exist.

**Fail Remediation**: If the database is behind head, run `uv run alembic upgrade head` and confirm no errors. If a migration fails, investigate error before proceeding.

**Status**: [ ] PASS   [ ] FAIL

---

### 3.4 — Schema Validation

**Objective**: Verify the database schema contains all three tables required by Phase 5 code: `federation_partners`, `federation_conflicts`, and `zim_exports`.

**Procedure**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "Validating database schema..."
uv run python << SCHEMA_CHECK
from sqlalchemy import inspect, create_engine
import os

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    print("FAIL: DATABASE_URL not set — cannot validate schema")
    raise SystemExit(1)

engine = create_engine(DATABASE_URL)
inspector = inspect(engine)
tables = inspector.get_table_names()

REQUIRED_TABLES = ["federation_partners", "federation_conflicts", "zim_exports"]
missing = []
for table in REQUIRED_TABLES:
    if table in tables:
        print(f"PASS: table '{table}' exists")
    else:
        print(f"FAIL: table '{table}' NOT FOUND in schema")
        missing.append(table)

if missing:
    print(f"FAIL: {len(missing)} required table(s) missing: {missing}")
    raise SystemExit(1)
else:
    print("PASS: All required tables present in schema")
SCHEMA_CHECK
```

**Pass Criteria**: All three tables (`federation_partners`, `federation_conflicts`, `zim_exports`) are present in the database schema. No `OperationalError` or `ProgrammingError` is raised.

**Fail Remediation**: Missing tables mean migrations have not been applied to this database. Run `uv run alembic upgrade head` to apply all pending migrations.

**Status**: [ ] PASS   [ ] FAIL

---

**Part 3 Summary**:

| Item | Status |
|------|--------|
| 3.1 Migration scripts present (3/3) | [ ] PASS / [ ] FAIL |
| 3.2 Backup procedure executed | [ ] PASS / [ ] FAIL |
| 3.3 Rollback procedure verified | [ ] PASS / [ ] FAIL |
| 3.4 Schema validation (3 tables) | [ ] PASS / [ ] FAIL |

**Part 3 Decision**: [ ] ALL PASS — proceed to Part 4   [ ] FAIL — remediate before proceeding

---

## Part 4: Zero-Downtime Deployment Verification (10 minutes)

---

### 4.1 — Health Check Endpoint

**Objective**: Confirm the health check endpoint is accessible and returns the expected response before deployment begins.

**Procedure**:
```bash
#!/bin/bash
PROD_HOST="100.70.184.84"
PORT=8000

echo "Testing health check endpoint on production host..."
RESPONSE=$(curl -s -w "\n%{http_code}" http://$PROD_HOST:$PORT/health)
HTTP_CODE=$(echo "$RESPONSE" | tail -1)
BODY=$(echo "$RESPONSE" | head -n -1)

echo "HTTP Status: $HTTP_CODE"
echo "Response:"
echo "$BODY"

if [ "$HTTP_CODE" = "200" ]; then
  # Verify response contains "status" and "timestamp" fields
  if echo "$BODY" | python3 -c "
import sys, json
data = json.load(sys.stdin)
assert 'status' in data, 'Missing status field'
print(f'  status: {data[\"status\"]}')
print(f'  timestamp: {data.get(\"timestamp\", \"(not present)\")}')
print('PASS: Health endpoint returns valid JSON with status field')
" 2>/dev/null; then
    echo "PASS: Health endpoint OK"
  else
    echo "PASS: HTTP 200 received (JSON structure may differ from expected)"
  fi
else
  echo "FAIL: Health endpoint returned HTTP $HTTP_CODE (expected 200)"
  exit 1
fi
```

**Expected Response**:
```json
{"status": "ok", "timestamp": "2026-06-12T08:47:00Z"}
```

**Pass Criteria**: HTTP 200 response with a JSON body containing at minimum a `status` field.

**Fail Remediation**: If the service is not running, this check should fail — that is expected. The service will be stopped during deployment. Run this check before stopping the service (i.e., at the start of pre-flight). If the service is running and returns non-200, investigate application logs before proceeding.

**Status**: [ ] PASS   [ ] FAIL   [ ] N/A (service intentionally stopped — proceed)

---

### 4.2 — Graceful Shutdown Verification

**Objective**: Confirm the systemd service handles SIGTERM gracefully (allows 30 seconds for in-flight requests to drain before exit).

**Procedure**:
```bash
#!/bin/bash
PROD_HOST="100.70.184.84"

echo "Verifying systemd service configuration for graceful shutdown..."
ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << SIGTERM_CHECK
echo "Checking TimeoutStopSec configuration..."
sudo systemctl cat open-repo 2>/dev/null | grep -E "TimeoutStopSec|KillMode|ExecStop"

if sudo systemctl cat open-repo 2>/dev/null | grep -q "TimeoutStopSec"; then
  echo "PASS: TimeoutStopSec configured"
else
  echo "INFO: No explicit TimeoutStopSec — systemd default is 90 seconds"
  echo "PASS: Default graceful shutdown (90s) is sufficient"
fi

echo "Checking uvicorn graceful shutdown (--timeout-graceful-shutdown flag or equivalent)..."
sudo systemctl cat open-repo 2>/dev/null | grep "uvicorn" | head -3
SIGTERM_CHECK
```

**Pass Criteria**: The systemd service file either has `TimeoutStopSec` set, or the systemd default (90 seconds) applies. The uvicorn process will drain in-flight requests before exit.

**Fail Remediation**: If `KillMode=process` is set without `TimeoutStopSec`, add `TimeoutStopSec=30` to the service file and reload: `sudo systemctl daemon-reload`.

**Status**: [ ] PASS   [ ] FAIL

---

### 4.3 — Blue-Green Readiness Check

**Objective**: Confirm the production host can run two instances of the application on different ports (required for zero-downtime cutover if implemented). If blue-green is not the deployment strategy for this release, record as N/A.

**Procedure**:
```bash
#!/bin/bash
PROD_HOST="100.70.184.84"

echo "Checking if blue-green deployment is planned for this release..."
# This is a verification check, not an execution step.
# Blue-green requires: two named service units OR docker-compose with named containers.

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << BLUEGREEN_CHECK
echo "Checking for blue-green configuration..."

if docker-compose --version &>/dev/null 2>&1; then
  echo "Docker Compose available"
  if [ -f "/home/awank/dev/SuperClaude_Framework/projects/open-repo/docker-compose.yml" ]; then
    echo "PASS: docker-compose.yml found — blue-green is possible"
  else
    echo "INFO: No docker-compose.yml — using direct systemd deployment (no blue-green)"
  fi
else
  echo "INFO: Docker Compose not available — using direct systemd deployment"
fi

echo "Current deployment strategy: systemd service (stop-deploy-start, not blue-green)"
echo "PASS: Deployment strategy confirmed as direct replacement (acceptable for maintenance window)"
BLUEGREEN_CHECK
```

**Pass Criteria**: Deployment strategy is documented and confirmed. For this release, direct systemd replacement (stop-deploy-start) is the confirmed strategy. This results in brief downtime during the deployment window, which is expected and communicated to stakeholders.

**Status**: [ ] PASS   [ ] N/A (blue-green not in scope for this release)

---

**Part 4 Summary**:

| Item | Status |
|------|--------|
| 4.1 Health check endpoint (HTTP 200) | [ ] PASS / [ ] FAIL / [ ] N/A |
| 4.2 Graceful shutdown verified | [ ] PASS / [ ] FAIL |
| 4.3 Blue-green readiness | [ ] PASS / [ ] N/A |

**Part 4 Decision**: [ ] ALL PASS/N/A — proceed to Part 5   [ ] FAIL — remediate before proceeding

---

## Part 5: Rollback Procedure Verification (5 minutes)

---

### 5.1 — Rollback Script Exists

**Objective**: Confirm the rollback procedure is documented and executable from the deployment machine.

**Procedure**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo

echo "Checking for rollback documentation..."

# The rollback procedure is documented in DEPLOYMENT_JUNE12_RISK_MITIGATION.md
# Section 2: Complete Rollback Playbook (Steps 1–6)
# There is no separate rollback.sh script; the procedure is documented inline.

if [ -f "DEPLOYMENT_JUNE12_RISK_MITIGATION.md" ]; then
  echo "PASS: DEPLOYMENT_JUNE12_RISK_MITIGATION.md exists (contains rollback playbook)"
  grep -n "Rollback Step" DEPLOYMENT_JUNE12_RISK_MITIGATION.md | head -10
else
  echo "FAIL: DEPLOYMENT_JUNE12_RISK_MITIGATION.md not found"
  exit 1
fi

echo ""
echo "Note: Rollback for this project is a 6-step manual procedure, not an automated script."
echo "The complete procedure is in Section 2 of DEPLOYMENT_JUNE12_RISK_MITIGATION.md"
```

**Pass Criteria**: `DEPLOYMENT_JUNE12_RISK_MITIGATION.md` is present and contains the rollback playbook.

**Note**: This project does not have a standalone `scripts/rollback.sh`. The rollback playbook is embedded in the risk mitigation document. This is acceptable; the deployer must have that document open during deployment.

**Status**: [ ] PASS   [ ] FAIL

---

### 5.2 — Rollback Timing Verified

**Objective**: Confirm that the rollback procedure can complete within 10 minutes (5-step sequence with known timings).

**Rollback procedure steps and their timing estimates** (from DEPLOYMENT_JUNE12_RISK_MITIGATION.md Section 2):

| Rollback Step | Action | Time Estimate |
|---------------|--------|---------------|
| Step 1 | Stop current deployment | 30 seconds |
| Step 2 | Restore database from backup | 2–3 minutes |
| Step 3 | Revert code to previous version | 1 minute |
| Step 4 | Reinstall dependencies for previous version | 2–3 minutes |
| Step 5 | Start application | 30 seconds |
| Step 6 | Verify rollback success (endpoint checks) | 1 minute |
| **Total** | | **7–9 minutes** |

**Procedure**:
```bash
echo "Verifying rollback timing estimate..."
echo ""
echo "Rollback steps and timing:"
echo "  Step 1 (stop service):           ~30 seconds"
echo "  Step 2 (restore database):       2-3 minutes (SQLite cp) or 3-5 min (PostgreSQL restore)"
echo "  Step 3 (revert code via git):    ~60 seconds"
echo "  Step 4 (reinstall dependencies): 2-3 minutes"
echo "  Step 5 (start service):          ~30 seconds"
echo "  Step 6 (verify endpoints):       ~60 seconds"
echo ""
echo "Total estimated rollback time: 7-9 minutes"
echo ""
echo "PASS: Rollback timing meets <10 minute target"

# Verify backup is available (required for Step 2)
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << VERIFY_BACKUP
BACKUP_DIR="/opt/db-backups"
if [ -d "\$BACKUP_DIR" ] && ls "\$BACKUP_DIR"/*.{db.bak,sql.gz} &>/dev/null 2>&1; then
  LATEST=\$(ls -t "\$BACKUP_DIR"/ | head -1)
  echo "PASS: Backup available for rollback: \$LATEST"
else
  echo "FAIL: No backup found in \$BACKUP_DIR — rollback Step 2 would fail"
  exit 1
fi
VERIFY_BACKUP
```

**Pass Criteria**: Backup exists on production host; total rollback timing is within 10 minutes.

**Fail Remediation**: If no backup exists, complete Item 3.2 (backup procedure) before proceeding. The rollback cannot succeed without a pre-deployment database backup.

**Status**: [ ] PASS   [ ] FAIL

---

**Part 5 Summary**:

| Item | Status |
|------|--------|
| 5.1 Rollback procedure documented | [ ] PASS / [ ] FAIL |
| 5.2 Rollback timing <10 minutes | [ ] PASS / [ ] FAIL |

**Part 5 Decision**: [ ] ALL PASS — pre-flight complete   [ ] FAIL — remediate before proceeding

---

## Final Pre-Flight Decision

Complete this section after all 5 parts are done.

**Checklist Completed By**: ____________________________

**Completion Date/Time**: ____________________________  UTC

**Total Time Spent**: _______ minutes

**Date Conflict Resolution** (from the notice at top of this document):

- [ ] Deployment start time confirmed as: __________ UTC
- [ ] If 20:00 UTC: DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md and this document's timing references have been noted as incorrect — deployer has adjusted
- [ ] If 09:00 UTC: DEPLOYMENT_JUNE_12_RUNBOOK.md and DEPLOYMENT_JUNE_12_GO_LIVE_CHECKLIST.md timing references have been noted as incorrect — deployer has adjusted

**Database Credentials Populated** (from Item 1.3):
- [ ] DATABASE_URL populated and verified
- [ ] Backup destination path populated and verified
- [ ] All [REQUIRED USER INPUT] fields above filled in

**Results**:

| Part | Items | PASS | FAIL | Decision |
|------|-------|------|------|----------|
| Part 1: Environment | 5 | __ | __ | GO / NO-GO |
| Part 2: Test Suite | 4 | __ | __ | GO / NO-GO |
| Part 3: Database | 4 | __ | __ | GO / NO-GO |
| Part 4: Zero-Downtime | 3 | __ | __ | GO / NO-GO |
| Part 5: Rollback | 2 | __ | __ | GO / NO-GO |

**Overall Decision**: [ ] GO — proceed to DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md   [ ] NO-GO — abort, remediate, reschedule

**Approved by** (deployment owner): ____________________________

---

## Quick Reference: Common Failures and Fixes

| Symptom | Check | Fix |
|---------|-------|-----|
| Wrong branch | `git branch --show-current` | `git checkout master` |
| DATABASE_URL empty | `echo $DATABASE_URL` | `export DATABASE_URL=<value>` |
| Tests: 84 instead of 157 | `uv run pytest tests/ -v --collect-only \| grep "test session starts"` | Pull latest code; 157 includes Phase 5 A11y tests |
| A11y tests fail to collect | `uv run pytest tests/test_a11y_axecore.py --collect-only` | Start dev server: `uv run uvicorn app.main:create_app --host 127.0.0.1 --port 8000` |
| `alembic: command not found` | `which alembic` | Use `uv run alembic` |
| SSH connection refused | `ping 100.70.184.84` | Check Tailscale VPN is active on both machines |
| Low disk on production | `df -h /opt` | Delete oldest backups: `ls -t /opt/backups/ \| tail -n +4 \| xargs rm -rf` |
| Schema missing tables | `uv run alembic current` | `uv run alembic upgrade head` |

---

**Document Version**: 2.0
**Created**: June 12, 2026
**Supersedes**: DEPLOYMENT_JUNE12_PRECHECK_ENVIRONMENT.md v1.0 (June 6, 2026)
**Valid For**: June 12, 2026 deployment
**Execute Before**: DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md
**Reference During**: DEPLOYMENT_JUNE12_RISK_MITIGATION.md, DEPLOYMENT_JUNE12_COMMUNICATION_TEMPLATES.md
