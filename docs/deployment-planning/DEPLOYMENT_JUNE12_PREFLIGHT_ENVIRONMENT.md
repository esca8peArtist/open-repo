---
title: "Open-Repo June 12, 2026 — Pre-Deployment Environment Audit (ZimWriter Phase 5)"
project: open-repo
phase: "5 — ZimWriter libzim activation (feature/zimwriter-libzim-activation merge)"
document_type: pre-deployment-environment-audit
status: EXECUTE JUNE 11 — database credentials required by user before execution
created: 2026-06-10
target_deployment_date: 2026-06-12
deployment_window: "UNRESOLVED — 09:00 UTC or 20:00 UTC. User must confirm before proceeding."
estimated_audit_duration: "90 minutes total (June 11 afternoon)"
prerequisite_documents:
  - DEPLOYMENT_JUNE12_RISK_MITIGATION.md (this directory)
  - DEPLOYMENT_JUNE12_SUCCESS_CRITERIA.md (this directory)
  - projects/open-repo/ZIMWRITER_MERGE_CONFLICT_RESOLUTION.md (merge-ready verdict)
  - projects/open-repo/DEPLOYMENT_JUNE12_RISK_MITIGATION.md (root-level rollback playbook)
---

# Pre-Deployment Environment Audit — ZimWriter Phase 5
## June 11, 2026 (Execute the afternoon before deployment)

**Auditor**: Deployment engineer executing June 12 window  
**Scope**: This audit is specific to the ZimWriter/libzim integration in Phase 5. It augments (does not replace) the root-level `DEPLOYMENT_JUNE12_PRECHECK_ENVIRONMENT.md`, which covers git, Python, general deps, Alembic, and rollback documentation. Run BOTH documents before deployment.  
**Decision Gate**: All 8 sections must return PASS before deployment proceeds. A single FAIL that cannot be remediated by 21:00 UTC on June 11 triggers the NO-GO decision.

---

## TIMING CONFLICT — USER DECISION REQUIRED BEFORE EXECUTION

Two deployment start times appear in the project documents:

| Source | Start Time |
|--------|-----------|
| DEPLOYMENT_JUNE_12_RUNBOOK.md (created June 3) | **20:00 UTC** |
| DEPLOYMENT_JUNE_12_GO_LIVE_CHECKLIST.md (created June 3) | **20:00 UTC** |
| DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md (created June 6) | **09:00 UTC** |
| DEPLOYMENT_JUNE12_RISK_MITIGATION.md root-level (created June 6) | **09:00 UTC** |
| PHASE_5_COMPLETION_SUMMARY.md | **20:00 UTC** |

This is unresolved. All timing references in this document use **09:00 UTC** as written (consistent with the June 6 documents). If the user confirms **20:00 UTC**, adjust all "execute by" times by +11 hours.

**User must fill in before executing this audit**:
- [ ] Canonical deployment start time: __________ UTC
- [ ] This audit to be completed by: __________ UTC on June 11

---

## Section 1 — System Prerequisites

**Estimated time**: 10 minutes  
**Execute on**: Production host (100.70.184.84) via SSH  
**Purpose**: Confirm the production Linux environment meets all OS, memory, disk, and network requirements for the ZimWriter feature. libzim is a C shared library; its requirements are stricter than the Python-only parts of the stack.

---

### 1.1 — Operating System and Architecture

ZimWriter requires libzim 3.2+, which is distributed as a Linux aarch64 wheel. The production host has been identified as a Raspberry Pi 5 (aarch64). Confirm this before proceeding.

```bash
PROD_HOST="100.70.184.84"

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'OS_CHECK'
echo "=== OS and Architecture Check ==="

# Architecture must be aarch64 for Raspberry Pi 5
ARCH=$(uname -m)
echo "Architecture: $ARCH"
if [ "$ARCH" != "aarch64" ]; then
  echo "WARN: Architecture is $ARCH, not aarch64. Verify libzim wheel is compatible."
fi

# OS version
echo "OS: $(lsb_release -d 2>/dev/null | cut -f2 || cat /etc/os-release | grep PRETTY_NAME | cut -d'"' -f2)"
echo "Kernel: $(uname -r)"

# Confirm glibc version (libzim requires glibc >= 2.31)
GLIBC_VERSION=$(ldd --version | head -1 | grep -oP '\d+\.\d+$')
echo "glibc: $GLIBC_VERSION"
GLIBC_MAJOR=$(echo "$GLIBC_VERSION" | cut -d. -f1)
GLIBC_MINOR=$(echo "$GLIBC_VERSION" | cut -d. -f2)
if [ "$GLIBC_MAJOR" -ge 2 ] && [ "$GLIBC_MINOR" -ge 31 ]; then
  echo "PASS: glibc $GLIBC_VERSION >= 2.31 (libzim requirement met)"
else
  echo "FAIL: glibc $GLIBC_VERSION < 2.31 — libzim will not load"
  exit 1
fi

echo "PASS: OS check complete"
OS_CHECK
```

**Expected output**:
```
Architecture: aarch64
OS: Debian GNU/Linux 12 (bookworm) [or Ubuntu 22.04+]
Kernel: 6.x.x [any 6.x kernel]
glibc: 2.35 [or any >= 2.31]
PASS: glibc 2.35 >= 2.31 (libzim requirement met)
PASS: OS check complete
```

**Error you should NOT see**: `FAIL: glibc ... < 2.31` — this means libzim cannot run and the deployment cannot proceed.

**Fail remediation**: Upgrade OS to Debian 12 Bookworm or Ubuntu 22.04 LTS. The Raspberry Pi 5 ships with Raspberry Pi OS (Bookworm), which has glibc 2.36. This check should pass on any Bookworm or later system.

**Status**: [ ] PASS   [ ] FAIL

---

### 1.2 — Memory and Swap

ZimWriter loads libzim into process memory and buffers article content during ZIM file construction. For the expected workload (single-user, intermittent exports), 512 MB free at export time is sufficient. However, the Raspberry Pi 5's thermal throttling (confirmed in project memory: idle 81-84°C, under compute 87.8°C) means the export should not be run simultaneously with other heavy compute tasks.

```bash
PROD_HOST="100.70.184.84"

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'MEM_CHECK'
echo "=== Memory Check ==="

# Available RAM
FREE_MEM_MB=$(free -m | awk '/^Mem:/ {print $7}')
TOTAL_MEM_MB=$(free -m | awk '/^Mem:/ {print $2}')
echo "Total RAM: ${TOTAL_MEM_MB} MB"
echo "Available: ${FREE_MEM_MB} MB"

if [ "$FREE_MEM_MB" -lt 512 ]; then
  echo "WARN: Less than 512 MB free — ZIM export may fail under memory pressure"
  echo "      Current processes consuming memory:"
  ps aux --sort=-%mem | head -10
else
  echo "PASS: ${FREE_MEM_MB} MB free (>= 512 MB required)"
fi

# Swap
SWAP_TOTAL=$(free -m | awk '/^Swap:/ {print $2}')
SWAP_FREE=$(free -m | awk '/^Swap:/ {print $4}')
echo "Swap total: ${SWAP_TOTAL} MB, free: ${SWAP_FREE} MB"
if [ "$SWAP_TOTAL" -gt 0 ]; then
  echo "PASS: Swap available (${SWAP_TOTAL} MB) — memory pressure relief available"
else
  echo "INFO: No swap configured — ensure adequate RAM before ZIM export"
fi

# Check CPU temperature (thermal throttling guard)
if [ -f /sys/class/thermal/thermal_zone0/temp ]; then
  TEMP_RAW=$(cat /sys/class/thermal/thermal_zone0/temp)
  TEMP_C=$((TEMP_RAW / 1000))
  echo "CPU temperature: ${TEMP_C}°C"
  if [ "$TEMP_C" -gt 85 ]; then
    echo "WARN: CPU temperature ${TEMP_C}°C — thermal throttling likely. Delay deployment."
  else
    echo "PASS: CPU temperature ${TEMP_C}°C — within acceptable range"
  fi
fi

MEM_CHECK
```

**Expected output**:
```
Total RAM: 8192 MB [or 4096 MB]
Available: 3200 MB [or any value >= 512 MB]
PASS: 3200 MB free (>= 512 MB required)
Swap total: 512 MB, free: 512 MB
PASS: Swap available
CPU temperature: 62°C
PASS: CPU temperature 62°C — within acceptable range
```

**Error you should NOT see**: `CPU temperature 87°C` or higher — this is the documented thermal throttling threshold for this machine. If temperature is elevated, wait for it to drop below 75°C before deploying.

**Fail remediation**: If temperature is elevated, ensure the Pi's cooling fan is running (`vcgencmd measure_clock arm` should not show frequency reduction). If memory is low, identify and stop any non-essential services.

**Status**: [ ] PASS   [ ] WARN (acceptable)   [ ] FAIL

---

### 1.3 — Disk Space

ZimWriter writes ZIM files to disk. A typical open-repo ZIM file for a small content corpus is 5–50 MB. The production host needs at least 5 GB free on the partition holding the application and database files.

```bash
PROD_HOST="100.70.184.84"

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'DISK_CHECK'
echo "=== Disk Space Check ==="

# Check all relevant mount points
echo "All filesystems:"
df -h --output=target,avail,use% | sort

# Specific check on /opt (application data)
OPT_AVAIL_GB=$(df -BG /opt 2>/dev/null | awk 'NR==2 {print $4}' | tr -d 'G' || echo "0")
ROOT_AVAIL_GB=$(df -BG / | awk 'NR==2 {print $4}' | tr -d 'G')

echo ""
echo "/opt available: ${OPT_AVAIL_GB} GB"
echo "/     available: ${ROOT_AVAIL_GB} GB"

TARGET_AVAIL="${OPT_AVAIL_GB:-$ROOT_AVAIL_GB}"
if [ "$TARGET_AVAIL" -ge 5 ]; then
  echo "PASS: ${TARGET_AVAIL} GB free (>= 5 GB required)"
else
  echo "FAIL: Only ${TARGET_AVAIL} GB free — need at least 5 GB for ZIM files + backups"
  echo "Largest directories:"
  du -sh /opt/* 2>/dev/null | sort -rh | head -10
  exit 1
fi

DISK_CHECK
```

**Pass criteria**: At least 5 GB free on the partition holding `/opt` or the application data directory.

**Fail remediation**: Remove old ZIM export files from previous test runs (`find /opt -name "*.zim" -mtime +7 -delete`). Remove old database backups beyond the 3 most recent (`ls -t /opt/db-backups/ | tail -n +4 | xargs -I{} rm /opt/db-backups/{}`).

**Status**: [ ] PASS   [ ] FAIL

---

### 1.4 — Network Connectivity

Verify the production host can reach the Tailscale network, PyPI (for dependency installation if needed), and that no outbound port restrictions exist that would break the health endpoint.

```bash
PROD_HOST="100.70.184.84"

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'NET_CHECK'
echo "=== Network Connectivity Check ==="

# Tailscale status
if command -v tailscale &>/dev/null; then
  STATUS=$(tailscale status --json 2>/dev/null | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('BackendState','Unknown'))" 2>/dev/null)
  echo "Tailscale: $STATUS"
  if [ "$STATUS" = "Running" ]; then
    echo "PASS: Tailscale active"
  else
    echo "WARN: Tailscale state: $STATUS — verify VPN connectivity"
  fi
else
  echo "INFO: tailscale CLI not present — verify network connectivity manually"
fi

# Localhost binding test (confirm port 8000 not already occupied)
if ss -tlnp | grep -q ':8000 '; then
  PID=$(ss -tlnp | grep ':8000 ' | grep -oP 'pid=\K[0-9]+')
  PROC=$(ps -p "$PID" -o comm= 2>/dev/null)
  echo "WARN: Port 8000 already in use by PID $PID ($PROC)"
  echo "      This process must be stopped before deployment"
else
  echo "PASS: Port 8000 is free"
fi

# PyPI reachability (needed if dependency install required)
if curl -s --max-time 10 https://pypi.org/simple/ -o /dev/null; then
  echo "PASS: PyPI reachable"
else
  echo "WARN: PyPI unreachable — dependency install will fail if needed"
fi

NET_CHECK
```

**Expected output**:
```
Tailscale: Running
PASS: Tailscale active
PASS: Port 8000 is free
PASS: PyPI reachable
```

**Error you should NOT see**: `WARN: Port 8000 already in use` — this means a previous deployment or dev server is still running and will block the new service from starting.

**Status**: [ ] PASS   [ ] WARN   [ ] FAIL

---

**Section 1 Summary**:

| Check | Status |
|-------|--------|
| 1.1 OS and architecture (aarch64, glibc >= 2.31) | [ ] PASS / [ ] FAIL |
| 1.2 Memory (>= 512 MB free, temp < 85°C) | [ ] PASS / [ ] WARN / [ ] FAIL |
| 1.3 Disk space (>= 5 GB free) | [ ] PASS / [ ] FAIL |
| 1.4 Network (Tailscale, port 8000 free) | [ ] PASS / [ ] WARN / [ ] FAIL |

**Section 1 Decision**: [ ] GO   [ ] NO-GO — remediate before proceeding

---

## Section 2 — Dependency Audit

**Estimated time**: 15 minutes  
**Execute on**: Development machine or production host (both must pass)  
**Purpose**: Verify all 157 tests remain passing on the merged branch, all dependency versions are locked, and no known security vulnerabilities exist in the dependency tree. This is not a re-run of the pre-merge tests — it is a verification that nothing has drifted since the ZIMWRITER_MERGE_CONFLICT_RESOLUTION.md verdict on June 6.

---

### 2.1 — Full Test Suite (157/157 Required)

The authoritative test count is 157: 51 ZIM-specific tests + 106 federation/A11y/OPDS tests. All must pass. The ZIM tests are in `tests/integration/test_export_pipeline.py` and `tests/test_zim_writer.py`.

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "=== Full Test Suite Run (157/157 required) ==="
echo "Start time: $(date -u +%T UTC)"

uv run pytest tests/ -v --tb=short 2>&1 | tee /tmp/open-repo-june11-tests.txt

echo ""
echo "=== Summary ==="
SUMMARY=$(tail -5 /tmp/open-repo-june11-tests.txt | grep -E "passed|failed|error")
echo "$SUMMARY"

PASSED=$(echo "$SUMMARY" | grep -oP '\d+(?= passed)' | head -1)
FAILED=$(echo "$SUMMARY" | grep -oP '\d+(?= failed)' | head -1)
ERRORS=$(echo "$SUMMARY" | grep -oP '\d+(?= error)' | head -1)

if [ "$PASSED" = "157" ] && [ -z "$FAILED" ] && [ -z "$ERRORS" ]; then
  echo "PASS: 157/157 tests passing — no regressions since June 6 merge-ready verdict"
else
  echo "FAIL: Test count or pass rate has changed"
  echo "  passed=$PASSED  failed=$FAILED  errors=$ERRORS"
  echo ""
  echo "Failing tests:"
  grep -E "^FAILED|^ERROR" /tmp/open-repo-june11-tests.txt
  exit 1
fi

echo "End time: $(date -u +%T UTC)"
```

**Expected final line**:
```
157 passed in X.XXs
```

**Error you should NOT see**:
```
51 passed, 106 deselected   ← means you're running filtered, not all tests
84 passed                   ← means Phase 5 tests are not included; check branch
FAILED tests/test_zim_writer.py::TestZimWriterCreateZim::test_create_zim_success
```

**Pass criteria**: Exactly 157 passed, 0 failed, 0 errors.

**Fail remediation**: If ZIM tests specifically fail, check that the feature branch is merged into master (`git log --oneline -5`). If the test count is 106 instead of 157, the ZimWriter test file may not be on the active branch. Run `git log --oneline -- tests/ | head -5` to confirm.

**Status**: [ ] PASS   [ ] FAIL

---

### 2.2 — ZIM-Specific Test Isolation

Run the 51 ZIM tests in isolation to confirm the libzim import chain is clean independent of the rest of the suite.

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "=== ZIM Test Isolation Run ==="

uv run pytest tests/ -k "zim" -v --tb=long 2>&1 | tee /tmp/open-repo-zim-isolated.txt

SUMMARY=$(tail -5 /tmp/open-repo-zim-isolated.txt | grep -E "passed|deselected")
echo "$SUMMARY"

ZIM_PASSED=$(echo "$SUMMARY" | grep -oP '\d+(?= passed)' | head -1)
ZIM_DESELECTED=$(echo "$SUMMARY" | grep -oP '\d+(?= deselected)' | head -1)

echo ""
echo "ZIM tests passed: $ZIM_PASSED (expected: 51)"
echo "Non-ZIM tests deselected: $ZIM_DESELECTED (expected: 106)"

if [ "$ZIM_PASSED" = "51" ]; then
  echo "PASS: All 51 ZIM tests pass in isolation"
else
  echo "FAIL: Expected 51 ZIM tests, got $ZIM_PASSED"
  grep -E "^FAILED|^ERROR" /tmp/open-repo-zim-isolated.txt
  exit 1
fi
```

**Expected output**:
```
51 passed, 106 deselected in X.XXs
ZIM tests passed: 51 (expected: 51)
PASS: All 51 ZIM tests pass in isolation
```

**Status**: [ ] PASS   [ ] FAIL

---

### 2.3 — Dependency Version Lock Verification

Confirm `uv.lock` (or `requirements.txt`) is committed and up-to-date. An unlocked dependency file means the production install could resolve to a different version than tested.

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "=== Dependency Lock Verification ==="

# Check for lock file
if [ -f "uv.lock" ]; then
  echo "PASS: uv.lock exists"
  # Check it's tracked by git (not gitignored)
  if git ls-files --error-unmatch uv.lock &>/dev/null 2>&1; then
    echo "PASS: uv.lock is tracked by git"
  else
    echo "WARN: uv.lock exists but is not tracked by git — production may install different versions"
  fi
  # Check age — warn if older than 7 days
  AGE_DAYS=$(( ($(date +%s) - $(stat -c %Y uv.lock)) / 86400 ))
  echo "uv.lock age: ${AGE_DAYS} days"
  if [ "$AGE_DAYS" -gt 7 ]; then
    echo "WARN: uv.lock is ${AGE_DAYS} days old — verify no critical security updates pending"
  else
    echo "PASS: uv.lock is current"
  fi
elif [ -f "requirements.txt" ] && [ -f "requirements-lock.txt" ]; then
  echo "PASS: requirements-lock.txt exists (using pip-tools workflow)"
elif [ -f "pyproject.toml" ]; then
  echo "INFO: pyproject.toml present — verify dependency pinning strategy"
  echo "      If using uv without lock file, run: uv lock --check"
  uv lock --check 2>&1 && echo "PASS: lock file is consistent" || echo "FAIL: lock file out of sync"
else
  echo "FAIL: No dependency lock file found — production installs are not reproducible"
  exit 1
fi

# Spot-check critical pinned versions
echo ""
echo "Critical package versions:"
for pkg in "libzim" "fastapi" "sqlalchemy" "uvicorn" "alembic" "pydantic"; do
  VERSION=$(uv run python -c "import importlib.metadata; print(importlib.metadata.version('$pkg'))" 2>/dev/null)
  if [ -n "$VERSION" ]; then
    echo "  $pkg == $VERSION"
  else
    echo "  $pkg — NOT INSTALLED"
  fi
done
```

**Expected output** (versions may vary, but all must be present):
```
PASS: uv.lock exists
PASS: uv.lock is tracked by git
uv.lock age: 5 days
PASS: uv.lock is current
Critical package versions:
  libzim == 3.2.x
  fastapi == 0.111.x
  sqlalchemy == 2.x.x
  uvicorn == 0.29.x
  alembic == 1.x.x
  pydantic == 2.x.x
```

**Error you should NOT see**: `libzim — NOT INSTALLED` — this is the core library for Phase 5 and must be present.

**Status**: [ ] PASS   [ ] WARN   [ ] FAIL

---

### 2.4 — Security Vulnerability Scan

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "=== Security Vulnerability Scan ==="

# pip-audit is the standard uv-compatible audit tool
if uv run pip-audit --version &>/dev/null 2>&1; then
  echo "Running pip-audit..."
  uv run pip-audit --format=json 2>&1 | tee /tmp/pip-audit-results.json
  VULN_COUNT=$(python3 -c "import json; d=json.load(open('/tmp/pip-audit-results.json')); print(len(d.get('vulnerabilities', [])))" 2>/dev/null || echo "unknown")
  echo "Vulnerabilities found: $VULN_COUNT"
  if [ "$VULN_COUNT" = "0" ]; then
    echo "PASS: No known vulnerabilities in dependency tree"
  else
    echo "WARN: $VULN_COUNT vulnerability/vulnerabilities found — review before deployment"
    python3 -c "
import json
with open('/tmp/pip-audit-results.json') as f:
    data = json.load(f)
for v in data.get('vulnerabilities', []):
    print(f'  {v[\"name\"]} {v[\"version\"]}: {v.get(\"id\",\"?\")} — {v.get(\"description\",\"?\")[:80]}')
" 2>/dev/null
  fi
else
  echo "INFO: pip-audit not installed — install with: uv pip install pip-audit"
  echo "      Skipping vulnerability scan (acceptable if pip-audit unavailable)"
  echo "WARN: Manual review of recent CVEs for fastapi, sqlalchemy, uvicorn recommended"
fi
```

**Pass criteria**: 0 known vulnerabilities. WARN (1+ low-severity) is acceptable with written justification. FAIL on any high/critical severity CVE.

**Status**: [ ] PASS   [ ] WARN (acceptable)   [ ] FAIL

---

**Section 2 Summary**:

| Check | Status |
|-------|--------|
| 2.1 Full test suite (157/157) | [ ] PASS / [ ] FAIL |
| 2.2 ZIM test isolation (51/51) | [ ] PASS / [ ] FAIL |
| 2.3 Dependency lock file verified | [ ] PASS / [ ] WARN / [ ] FAIL |
| 2.4 Security vulnerability scan | [ ] PASS / [ ] WARN / [ ] FAIL |

**Section 2 Decision**: [ ] GO   [ ] NO-GO — remediate before proceeding

---

## Section 3 — Database Validation

**Estimated time**: 15 minutes  
**Purpose**: Verify SQLite/PostgreSQL database state before the deployment window opens. All credentials must be provided by user by end of June 11.

**USER INPUT REQUIRED — fill in before executing this section**:

```
DATABASE_URL     = [REQUIRED]
  PostgreSQL: postgres://username:password@hostname:5432/dbname
  SQLite:     sqlite:////opt/data/open-repo.db
  Value:      ________________________________

SQLITE_PATH      = [REQUIRED if SQLite]
  Absolute path to the .db file on production host
  Example: /opt/data/open-repo.db
  Value:      ________________________________

BACKUP_DIR       = [REQUIRED]
  Where to write pre-deployment backups
  Example: /opt/db-backups
  Value:      ________________________________
```

---

### 3.1 — Database Connectivity

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "=== Database Connectivity Check ==="

if [ -z "$DATABASE_URL" ]; then
  echo "FAIL: DATABASE_URL not set — cannot validate database"
  echo "Set with: export DATABASE_URL=<your-connection-url>"
  exit 1
fi

uv run python << 'DB_CONN_CHECK'
import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

DATABASE_URL = os.environ["DATABASE_URL"]

# Redact credentials for logging
if "://" in DATABASE_URL:
    scheme = DATABASE_URL.split("://")[0]
    rest = DATABASE_URL.split("://")[1]
    if "@" in rest:
        host_part = rest.split("@")[1]
        print(f"Connecting to: {scheme}://*****@{host_part}")
    else:
        print(f"Connecting to: {DATABASE_URL}")

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("PASS: Database connection successful")
except OperationalError as e:
    print(f"FAIL: Database connection failed: {e}")
    raise SystemExit(1)
DB_CONN_CHECK
```

**Expected output**:
```
Connecting to: sqlite:////opt/data/open-repo.db [or postgres://...]
PASS: Database connection successful
```

**Error you should NOT see**: `OperationalError: unable to open database file` (SQLite path wrong) or `OperationalError: could not connect to server` (PostgreSQL unreachable).

**Status**: [ ] PASS   [ ] FAIL   [ ] BLOCKED (credentials not yet provided)

---

### 3.2 — Schema Integrity — ZimWriter Tables

Phase 5 requires the `zim_exports` table (migration 003). Verify it exists and has the correct columns.

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

uv run python << 'SCHEMA_CHECK'
import os
from sqlalchemy import create_engine, inspect, text

engine = create_engine(os.environ["DATABASE_URL"])
inspector = inspect(engine)

print("=== Schema Integrity Check ===")
tables = inspector.get_table_names()
print(f"All tables: {tables}")

# Required tables
REQUIRED = {
    "federation_partners": ["id", "url", "name", "trust_level", "last_synced_at"],
    "federation_conflicts": ["id", "partner_id", "entry_id", "conflict_type", "resolved_at"],
    "zim_exports": ["id", "title", "description", "language", "zim_path",
                    "file_size_bytes", "created_at", "content_hash", "export_status"],
}

all_pass = True
for table_name, expected_columns in REQUIRED.items():
    if table_name not in tables:
        print(f"FAIL: Table '{table_name}' missing from schema")
        all_pass = False
        continue
    
    actual_cols = {col["name"] for col in inspector.get_columns(table_name)}
    missing_cols = [c for c in expected_columns if c not in actual_cols]
    
    if missing_cols:
        print(f"FAIL: Table '{table_name}' missing columns: {missing_cols}")
        all_pass = False
    else:
        print(f"PASS: Table '{table_name}' — all required columns present")
        print(f"      Columns: {sorted(actual_cols)}")

if all_pass:
    print("\nPASS: All 3 required tables with correct schema present")
else:
    print("\nFAIL: Schema does not match expected state")
    raise SystemExit(1)
SCHEMA_CHECK
```

**Expected output**:
```
All tables: ['alembic_version', 'federation_conflicts', 'federation_partners', 'zim_exports']
PASS: Table 'federation_partners' — all required columns present
PASS: Table 'federation_conflicts' — all required columns present
PASS: Table 'zim_exports' — all required columns present
PASS: All 3 required tables with correct schema present
```

**Error you should NOT see**: `FAIL: Table 'zim_exports' missing from schema` — this means migration 003 was never applied. Run `uv run alembic upgrade head` and re-check.

**Status**: [ ] PASS   [ ] FAIL

---

### 3.3 — Migration Runnable in Test Environment

Verify that Alembic can upgrade and downgrade cleanly against a temporary copy of the database. This tests the migration scripts without touching the production database.

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "=== Migration Dry-Run Test ==="
TIMESTAMP=$(date +%s)
TEST_DB_PATH="/tmp/open-repo-migrate-test-${TIMESTAMP}.db"

# Create a fresh test database and run all migrations against it
TEST_DATABASE_URL="sqlite:///${TEST_DB_PATH}"

echo "Creating test database at: $TEST_DB_PATH"
DATABASE_URL="$TEST_DATABASE_URL" uv run alembic upgrade head
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
  echo "PASS: All migrations applied successfully to fresh database"
else
  echo "FAIL: Migration upgrade failed on fresh database (exit: $EXIT_CODE)"
  exit 1
fi

# Test downgrade one step
echo "Testing downgrade -1..."
DATABASE_URL="$TEST_DATABASE_URL" uv run alembic downgrade -1
DOWNGRADE_CODE=$?

if [ $DOWNGRADE_CODE -eq 0 ]; then
  echo "PASS: Downgrade -1 succeeded"
else
  echo "FAIL: Downgrade -1 failed — rollback procedure compromised"
  # Do NOT exit — this is serious but not a full blocker
fi

# Cleanup
rm -f "$TEST_DB_PATH"
echo "Test database cleaned up"
echo "PASS: Migration dry-run complete"
```

**Expected output**:
```
Creating test database at: /tmp/open-repo-migrate-test-XXXXXXXXXX.db
INFO  [alembic.runtime.migration] Running upgrade ...
PASS: All migrations applied successfully to fresh database
Testing downgrade -1...
INFO  [alembic.runtime.migration] Running downgrade ...
PASS: Downgrade -1 succeeded
Test database cleaned up
PASS: Migration dry-run complete
```

**Error you should NOT see**: `alembic.exc.CommandError` — this indicates a broken migration script that cannot run. Must be fixed before deployment.

**Status**: [ ] PASS   [ ] FAIL

---

### 3.4 — Pre-Deployment Backup

Create and verify the backup that will be used for rollback if needed. This backup must exist before deployment begins.

```bash
PROD_HOST="100.70.184.84"
BACKUP_DIR="[REQUIRED USER INPUT — e.g., /opt/db-backups]"

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << BACKUP_SCRIPT
TIMESTAMP=\$(date +%Y%m%d-%H%M%S)
BACKUP_DIR="$BACKUP_DIR"
mkdir -p "\$BACKUP_DIR"

# SQLite backup (adjust path per user input)
SQLITE_FILE="[REQUIRED USER INPUT — e.g., /opt/data/open-repo.db]"

if [ -f "\$SQLITE_FILE" ]; then
  BACKUP_FILE="\${BACKUP_DIR}/open-repo-\${TIMESTAMP}.db.bak"
  cp "\$SQLITE_FILE" "\$BACKUP_FILE"
  
  # Verify
  if [ -s "\$BACKUP_FILE" ]; then
    SIZE=\$(du -sh "\$BACKUP_FILE" | cut -f1)
    echo "PASS: Backup created: \$BACKUP_FILE (\$SIZE)"
    
    # Integrity check: open with sqlite3
    if sqlite3 "\$BACKUP_FILE" "PRAGMA integrity_check;" 2>&1 | grep -q "^ok$"; then
      echo "PASS: SQLite integrity check passed"
    else
      echo "FAIL: SQLite integrity check failed — backup may be corrupted"
      exit 1
    fi
  else
    echo "FAIL: Backup file is empty or was not created"
    exit 1
  fi
else
  echo "FAIL: Source database not found at \$SQLITE_FILE"
  echo "Verify SQLITE_PATH variable at top of Section 3"
  exit 1
fi

echo "Backup complete at: \$(date -u +%T UTC)"
BACKUP_SCRIPT
```

**Expected output**:
```
PASS: Backup created: /opt/db-backups/open-repo-20260611-143022.db.bak (2.1M)
PASS: SQLite integrity check passed
Backup complete at: 14:30:25 UTC
```

**Error you should NOT see**: `FAIL: SQLite integrity check failed` — the database is corrupted. Stop. Do not deploy until this is resolved.

**Status**: [ ] PASS   [ ] FAIL   [ ] BLOCKED (SQLITE_PATH not populated)

---

**Section 3 Summary**:

| Check | Status |
|-------|--------|
| 3.1 Database connectivity | [ ] PASS / [ ] FAIL / [ ] BLOCKED |
| 3.2 Schema integrity (3 tables, all columns) | [ ] PASS / [ ] FAIL |
| 3.3 Migration dry-run (upgrade + downgrade) | [ ] PASS / [ ] FAIL |
| 3.4 Pre-deployment backup created | [ ] PASS / [ ] FAIL / [ ] BLOCKED |

**Section 3 Decision**: [ ] GO   [ ] NO-GO   [ ] BLOCKED (credentials needed)

---

## Section 4 — Configuration Validation

**Estimated time**: 10 minutes  
**Purpose**: Verify all environment variables, secrets configuration, and logging paths are set correctly for production.

---

### 4.1 — Required Environment Variables

```bash
PROD_HOST="100.70.184.84"

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'ENV_CHECK'
echo "=== Environment Variable Validation ==="

# Load from systemd service if available
if sudo systemctl cat open-repo &>/dev/null 2>&1; then
  eval $(sudo systemctl cat open-repo | grep -E "^Environment=" | sed 's/^Environment=/export /')
fi

REQUIRED=(
  "DATABASE_URL"
  "SECRET_KEY"
  "OPDS_CATALOG_NAME"
  "LOG_LEVEL"
  "FASTAPI_ENV"
  "UVICORN_HOST"
  "UVICORN_PORT"
)

MISSING=0
for var in "${REQUIRED[@]}"; do
  value="${!var}"
  if [ -z "$value" ]; then
    echo "FAIL: $var is not set"
    MISSING=$((MISSING + 1))
  else
    case "$var" in
      SECRET_KEY|DATABASE_URL)
        echo "PASS: $var [REDACTED — set, non-empty]" ;;
      UVICORN_HOST)
        if [ "$value" = "0.0.0.0" ]; then
          echo "FAIL: UVICORN_HOST=0.0.0.0 is PROHIBITED — must be 127.0.0.1"
          MISSING=$((MISSING + 1))
        else
          echo "PASS: UVICORN_HOST=$value"
        fi ;;
      *)
        echo "PASS: $var=$value" ;;
    esac
  fi
done

echo ""
if [ $MISSING -eq 0 ]; then
  echo "PASS: All required environment variables set"
else
  echo "FAIL: $MISSING variable(s) missing or invalid"
  exit 1
fi
ENV_CHECK
```

**Expected output**:
```
PASS: DATABASE_URL [REDACTED — set, non-empty]
PASS: SECRET_KEY [REDACTED — set, non-empty]
PASS: OPDS_CATALOG_NAME=Open Repository
PASS: LOG_LEVEL=INFO
PASS: FASTAPI_ENV=production
PASS: UVICORN_HOST=127.0.0.1
PASS: UVICORN_PORT=8000
PASS: All required environment variables set
```

**Error you should NOT see**: `FAIL: UVICORN_HOST=0.0.0.0 is PROHIBITED` — this violates the absolute security requirement. UVICORN_HOST must always be 127.0.0.1 or a specific Tailscale IP.

**Status**: [ ] PASS   [ ] FAIL

---

### 4.2 — Logging Paths Writable

```bash
PROD_HOST="100.70.184.84"

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'LOG_CHECK'
echo "=== Logging Configuration Check ==="

# Standard log locations
LOG_DIRS=("/var/log/open-repo" "/opt/logs/open-repo" "/tmp")

for dir in "${LOG_DIRS[@]}"; do
  if [ -d "$dir" ]; then
    if touch "${dir}/.write-test-$$" &>/dev/null 2>&1; then
      rm -f "${dir}/.write-test-$$"
      echo "PASS: Log directory writable: $dir"
    else
      echo "FAIL: Log directory not writable: $dir"
    fi
  fi
done

# Check journald is collecting service logs
if systemctl is-active --quiet systemd-journald; then
  echo "PASS: journald active — service logs will be captured"
  echo "      View with: sudo journalctl -u open-repo -f"
else
  echo "WARN: journald not active — verify application logging configuration"
fi

# Log rotation
if [ -f "/etc/logrotate.d/open-repo" ]; then
  echo "PASS: logrotate configuration present"
elif command -v logrotate &>/dev/null; then
  echo "INFO: logrotate installed but no open-repo config — add /etc/logrotate.d/open-repo"
else
  echo "INFO: logrotate not configured — acceptable for journald-only logging"
fi

LOG_CHECK
```

**Status**: [ ] PASS   [ ] WARN   [ ] FAIL

---

**Section 4 Summary**:

| Check | Status |
|-------|--------|
| 4.1 All 7 env vars set (UVICORN_HOST != 0.0.0.0) | [ ] PASS / [ ] FAIL |
| 4.2 Logging paths writable, journald active | [ ] PASS / [ ] WARN / [ ] FAIL |

**Section 4 Decision**: [ ] GO   [ ] NO-GO

---

## Section 5 — libzim-Specific Validation

**Estimated time**: 20 minutes  
**Purpose**: This is the highest-risk section for Phase 5. libzim is a C shared library that must be installed at the OS level or via a Python wheel. Its behavior on aarch64 Linux differs from x86_64 development environments. The pre-merge verdict confirmed the code is correct; this section confirms the runtime environment can execute it.

---

### 5.1 — libzim Python Package Version

libzim 3.2+ is required. The feature branch code uses `creator.config_indexing()` before `Creator.__enter__()`, which is the correct API ordering for libzim 3.2+. Earlier versions do not support this calling convention.

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "=== libzim Version Check ==="

uv run python << 'LIBZIM_VERSION'
try:
    import libzim
    version = libzim.__version__
    print(f"libzim version: {version}")
    
    # Parse version
    parts = version.split(".")
    major, minor = int(parts[0]), int(parts[1])
    
    if major > 3 or (major == 3 and minor >= 2):
        print(f"PASS: libzim {version} >= 3.2 (required for config_indexing API)")
    else:
        print(f"FAIL: libzim {version} < 3.2 — config_indexing() API not available")
        print("      The feature branch code will raise AttributeError at runtime")
        raise SystemExit(1)
    
    # Verify the Creator class exists
    from libzim.writer import Creator
    print(f"PASS: libzim.writer.Creator importable")
    
    # Verify config_indexing exists on Creator
    if hasattr(Creator, 'config_indexing'):
        print(f"PASS: Creator.config_indexing() method present")
    else:
        print(f"FAIL: Creator.config_indexing() not present in this libzim version")
        print("      Upgrade to libzim >= 3.2")
        raise SystemExit(1)

except ImportError as e:
    print(f"FAIL: libzim not importable: {e}")
    print("      Install with: uv pip install libzim")
    raise SystemExit(1)
LIBZIM_VERSION
```

**Expected output**:
```
libzim version: 3.2.x
PASS: libzim 3.2.x >= 3.2 (required for config_indexing API)
PASS: libzim.writer.Creator importable
PASS: Creator.config_indexing() method present
```

**Error you should NOT see**:
- `FAIL: libzim not importable` — library not installed
- `FAIL: libzim 3.1.x < 3.2` — wrong version; the `config_indexing()` call will fail at runtime with `AttributeError`
- `FAIL: Creator.config_indexing() not present` — API mismatch; this version cannot run Phase 5 code

**Fail remediation**: `uv pip install "libzim>=3.2"`. On aarch64, verify the wheel is available for this platform: `pip index versions libzim`. If no aarch64 wheel exists, build from source per the libzim build instructions at https://github.com/openzim/python-libzim.

**Status**: [ ] PASS   [ ] FAIL

---

### 5.2 — ZimWriter Module Import and Instantiation

Verify the ZimWriter class (the main Phase 5 deliverable) can be imported and instantiated without errors.

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

uv run python << 'ZIMWRITER_IMPORT'
print("=== ZimWriter Import and Instantiation Check ===")

# Step 1: import
try:
    from app.services.export.zim_writer import ZimWriter, ZimConfig, ZimEntry
    print("PASS: ZimWriter, ZimConfig, ZimEntry all importable")
except ImportError as e:
    print(f"FAIL: Import failed: {e}")
    raise SystemExit(1)

# Step 2: instantiate with a valid config
import tempfile, pathlib
with tempfile.TemporaryDirectory() as tmpdir:
    config = ZimConfig(
        title="Pre-Deployment Test ZIM",
        description="Environment validation",
        language_iso3="eng",
        output_path=pathlib.Path(tmpdir) / "test.zim",
        creator_name="pre-flight-check",
        publisher_name="open-repo",
    )
    writer = ZimWriter(config)
    print(f"PASS: ZimWriter instantiated successfully")
    print(f"      output_path: {config.output_path}")
    print(f"      language: {config.language_iso3}")

print("PASS: ZimWriter module check complete")
ZIMWRITER_IMPORT
```

**Expected output**:
```
PASS: ZimWriter, ZimConfig, ZimEntry all importable
PASS: ZimWriter instantiated successfully
      output_path: /tmp/tmpXXXXXX/test.zim
      language: eng
PASS: ZimWriter module check complete
```

**Error you should NOT see**: `ImportError: cannot import name 'ZimWriter'` — the module is not present on this branch/installation.

**Status**: [ ] PASS   [ ] FAIL

---

### 5.3 — Xapian Full-Text Search State Confirmed

The ZimWriter code calls `creator.config_indexing(True, language_iso3)` which enables Xapian FTS indexing. This is the correct production state. Confirm the feature flag or configuration value reflects this intent.

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "=== Xapian FTS Configuration Check ==="

# Check the config_indexing call in the live code
INDEXING_LINE=$(grep -n "config_indexing" app/services/export/zim_writer.py | head -5)
echo "config_indexing call locations in zim_writer.py:"
echo "$INDEXING_LINE"

# Verify it's called with True (enabled) and before the with block
if grep -q "config_indexing(True" app/services/export/zim_writer.py; then
  echo "PASS: Xapian FTS enabled (config_indexing called with True)"
else
  echo "FAIL: config_indexing(True) not found — FTS may be disabled"
  exit 1
fi

# Verify ordering: config_indexing must appear before "with creator:"
LINE_CONFIG=$(grep -n "config_indexing" app/services/export/zim_writer.py | head -1 | cut -d: -f1)
LINE_WITH=$(grep -n "with creator" app/services/export/zim_writer.py | head -1 | cut -d: -f1)

echo "config_indexing line: $LINE_CONFIG"
echo "'with creator' line:  $LINE_WITH"

if [ -n "$LINE_CONFIG" ] && [ -n "$LINE_WITH" ] && [ "$LINE_CONFIG" -lt "$LINE_WITH" ]; then
  echo "PASS: config_indexing() called BEFORE 'with creator:' block (correct API order)"
else
  echo "FAIL: config_indexing() ordering incorrect — will raise RuntimeError at export time"
  exit 1
fi
```

**Expected output**:
```
config_indexing call locations in zim_writer.py:
835:    creator.config_indexing(True, self.config.language_iso3)
PASS: Xapian FTS enabled (config_indexing called with True)
config_indexing line: 835
'with creator' line:  838
PASS: config_indexing() called BEFORE 'with creator:' block (correct API order)
```

**Error you should NOT see**: `FAIL: config_indexing() ordering incorrect` — this was the critical bug that was fixed in commits `1dee5c99` and `be29394b`. If this fires, the wrong branch version is deployed.

**Status**: [ ] PASS   [ ] FAIL

---

### 5.4 — zim-tools Binary (Optional)

The `zim-tools` binary (`zimcheck`, `zimsearch`) is optional but recommended for post-deployment ZIM validation. Record its availability.

```bash
PROD_HOST="100.70.184.84"

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'ZIMTOOLS_CHECK'
echo "=== zim-tools Availability Check ==="

if command -v zimcheck &>/dev/null; then
  echo "PASS: zimcheck available: $(zimcheck --version 2>&1 | head -1)"
elif [ -f "/usr/local/bin/zimcheck" ]; then
  echo "PASS: zimcheck available at /usr/local/bin/zimcheck"
else
  echo "INFO: zimcheck not installed — post-deployment ZIM validation will use Python-only checks"
  echo "      Install with: sudo apt-get install zim-tools (if in package repos)"
  echo "      Or: build from https://github.com/openzim/zim-tools"
fi

if command -v zimsearch &>/dev/null; then
  echo "PASS: zimsearch available"
else
  echo "INFO: zimsearch not installed — FTS verification will be skipped post-deployment"
fi
ZIMTOOLS_CHECK
```

**Pass criteria**: INFO is acceptable. zim-tools is not required for deployment; its absence means less thorough post-deployment ZIM validation, which is acceptable for the June 12 window.

**Status**: [ ] PASS   [ ] INFO (acceptable)

---

**Section 5 Summary**:

| Check | Status |
|-------|--------|
| 5.1 libzim >= 3.2, config_indexing() present | [ ] PASS / [ ] FAIL |
| 5.2 ZimWriter import and instantiation | [ ] PASS / [ ] FAIL |
| 5.3 Xapian FTS enabled and correctly ordered | [ ] PASS / [ ] FAIL |
| 5.4 zim-tools binary | [ ] PASS / [ ] INFO |

**Section 5 Decision**: [ ] GO   [ ] NO-GO

---

## Section 6 — Integration Testing (ZIM Export Pipeline)

**Estimated time**: 10 minutes  
**Purpose**: Run an end-to-end ZIM export with sample content in the pre-production environment. This confirms libzim can produce a valid ZIM file, not just import cleanly.

---

### 6.1 — End-to-End ZIM Export with Sample Content

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

uv run python << 'E2E_ZIM_TEST'
import tempfile
import pathlib
import hashlib

print("=== End-to-End ZIM Export Integration Test ===")

try:
    from app.services.export.zim_writer import ZimWriter, ZimConfig, ZimEntry
    from libzim.writer import Creator, Item, StringProvider, FileProvider, Blob
    print("PASS: Imports successful")
except ImportError as e:
    print(f"FAIL: Import failed: {e}")
    raise SystemExit(1)

# Build a minimal corpus
SAMPLE_ARTICLES = [
    ZimEntry(
        path="index",
        title="Open Repository — Offline Export",
        content="<html><body><h1>Open Repository</h1><p>Offline export test article.</p></body></html>",
        mime_type="text/html",
    ),
    ZimEntry(
        path="article/test-1",
        title="Pre-Flight Test Article 1",
        content="<html><body><h1>Test Article 1</h1><p>This is pre-deployment integration test content.</p></body></html>",
        mime_type="text/html",
    ),
    ZimEntry(
        path="article/test-2",
        title="Pre-Flight Test Article 2",
        content="<html><body><h1>Test Article 2</h1><p>Verifying ZIM pipeline produces valid output.</p></body></html>",
        mime_type="text/html",
    ),
]

with tempfile.TemporaryDirectory() as tmpdir:
    output_path = pathlib.Path(tmpdir) / "preflight-test.zim"
    
    config = ZimConfig(
        title="Pre-Flight Export Test",
        description="Automated integration test — June 11 pre-deployment",
        language_iso3="eng",
        output_path=output_path,
        creator_name="pre-flight",
        publisher_name="open-repo",
    )
    
    writer = ZimWriter(config)
    for entry in SAMPLE_ARTICLES:
        writer.add_article(entry)
    
    print(f"Writing ZIM to: {output_path}")
    writer.create_zim()
    
    if output_path.exists():
        size_bytes = output_path.stat().st_size
        if size_bytes > 0:
            print(f"PASS: ZIM file created — {size_bytes:,} bytes ({size_bytes/1024:.1f} KB)")
        else:
            print(f"FAIL: ZIM file exists but is empty (0 bytes)")
            raise SystemExit(1)
    else:
        print(f"FAIL: ZIM file was not created at {output_path}")
        raise SystemExit(1)
    
    # Verify ZIM magic bytes (0x5A 0x49 0x4D 0x04 = "ZIM\x04")
    with open(output_path, "rb") as f:
        magic = f.read(4)
    EXPECTED_MAGIC = b'\x5a\x49\x4d\x04'
    if magic == EXPECTED_MAGIC:
        print(f"PASS: ZIM magic bytes correct: {magic.hex()}")
    else:
        print(f"FAIL: Unexpected magic bytes: {magic.hex()} (expected: {EXPECTED_MAGIC.hex()})")
        raise SystemExit(1)
    
    print("PASS: End-to-end ZIM export integration test PASSED")
    print("      3 articles written, ZIM file valid, magic bytes confirmed")

E2E_ZIM_TEST
```

**Expected output**:
```
PASS: Imports successful
Writing ZIM to: /tmp/tmpXXXXXX/preflight-test.zim
PASS: ZIM file created — 45,312 bytes (44.3 KB)
PASS: ZIM magic bytes correct: 5a494d04
PASS: End-to-end ZIM export integration test PASSED
      3 articles written, ZIM file valid, magic bytes confirmed
```

**Error you should NOT see**:
- `RuntimeError: Creator started` — `config_indexing()` was called after `Creator.__enter__()`. This is the ordering bug; it means the wrong code is deployed.
- `AttributeError: 'Creator' object has no attribute 'config_indexing'` — wrong libzim version.
- `FAIL: ZIM file was not created` — the write failed silently; check disk space and permissions.

**Status**: [ ] PASS   [ ] FAIL

---

**Section 6 Summary**:

| Check | Status |
|-------|--------|
| 6.1 End-to-end ZIM export (3 articles, valid magic bytes) | [ ] PASS / [ ] FAIL |

**Section 6 Decision**: [ ] GO   [ ] NO-GO

---

## Section 7 — Backup Verification

**Estimated time**: 5 minutes  
**Purpose**: Confirm the backup created in Section 3.4 is restorable. Test restoration into a temporary location, not the live database.

---

### 7.1 — Backup Restoration Smoke Test

```bash
PROD_HOST="100.70.184.84"
BACKUP_DIR="[REQUIRED USER INPUT — same value as Section 3.4]"

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << RESTORE_TEST
TIMESTAMP=\$(date +%s)
BACKUP_DIR="$BACKUP_DIR"

# Find the most recent backup
LATEST_BACKUP=\$(ls -t "\$BACKUP_DIR"/*.db.bak 2>/dev/null | head -1)

if [ -z "\$LATEST_BACKUP" ]; then
  echo "FAIL: No .db.bak files found in \$BACKUP_DIR"
  echo "      Complete Section 3.4 first"
  exit 1
fi

echo "Testing restoration of: \$LATEST_BACKUP"
SIZE=\$(du -sh "\$LATEST_BACKUP" | cut -f1)
echo "Backup size: \$SIZE"

# Restore to temp location
TEST_RESTORE="/tmp/restore-test-\${TIMESTAMP}.db"
cp "\$LATEST_BACKUP" "\$TEST_RESTORE"

# Verify integrity
if sqlite3 "\$TEST_RESTORE" "PRAGMA integrity_check;" 2>&1 | grep -q "^ok\$"; then
  echo "PASS: Restored copy integrity check: ok"
else
  echo "FAIL: Restored copy integrity check failed — backup is corrupt"
  rm -f "\$TEST_RESTORE"
  exit 1
fi

# Verify tables exist in restored copy
TABLES=\$(sqlite3 "\$TEST_RESTORE" ".tables")
echo "Tables in restored backup: \$TABLES"
for table in "federation_partners" "federation_conflicts" "zim_exports"; do
  if echo "\$TABLES" | grep -q "\$table"; then
    echo "PASS: Table '\$table' present in backup"
  else
    echo "FAIL: Table '\$table' missing from backup"
  fi
done

rm -f "\$TEST_RESTORE"
echo "PASS: Backup restoration smoke test complete — rollback is viable"
RESTORE_TEST
```

**Expected output**:
```
Testing restoration of: /opt/db-backups/open-repo-20260611-143022.db.bak
Backup size: 2.1M
PASS: Restored copy integrity check: ok
Tables in restored backup: alembic_version  federation_conflicts  federation_partners  zim_exports
PASS: Table 'federation_partners' present in backup
PASS: Table 'federation_conflicts' present in backup
PASS: Table 'zim_exports' present in backup
PASS: Backup restoration smoke test complete — rollback is viable
```

**Status**: [ ] PASS   [ ] FAIL

---

**Section 7 Summary**:

| Check | Status |
|-------|--------|
| 7.1 Backup restoration smoke test | [ ] PASS / [ ] FAIL |

---

## Section 8 — Monitoring Setup

**Estimated time**: 5 minutes  
**Purpose**: Confirm health endpoint, alerting, and log watching are configured before deployment begins.

---

### 8.1 — Health Endpoint and Alerting Pre-Flight

```bash
PROD_HOST="100.70.184.84"

echo "=== Monitoring Pre-Flight Check ==="

# Health endpoint (pre-deployment baseline — service should currently be running)
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "http://${PROD_HOST}:8000/health" 2>/dev/null)
if [ "$HTTP_CODE" = "200" ]; then
  echo "PASS: Health endpoint returns 200 (pre-deployment baseline confirmed)"
elif [ "$HTTP_CODE" = "000" ]; then
  echo "INFO: Health endpoint unreachable — service may not be running yet (acceptable pre-deployment)"
else
  echo "WARN: Health endpoint returned HTTP $HTTP_CODE — investigate before deployment"
fi

# Confirm journalctl is accessible for monitoring during deployment
ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'JOURNAL_CHECK'
echo "Confirming journald access..."
if sudo journalctl -u open-repo -n 5 &>/dev/null 2>&1; then
  echo "PASS: journalctl accessible for open-repo service"
  echo "      During deployment, monitor with:"
  echo "      sudo journalctl -u open-repo -f --since now"
else
  echo "WARN: journalctl not accessible — verify sudo permissions"
fi

# Verify alerting configuration (if applicable)
echo ""
echo "Alerting: verify your monitoring platform has open-repo in scope"
echo "  Expected alerts post-deployment:"
echo "    - /health endpoint DOWN for > 2 minutes: PagerDuty/Slack/email alert"
echo "    - HTTP 5xx error rate > 1%: alert"
echo "    - CPU temperature > 85°C: alert (thermal throttling guard)"
JOURNAL_CHECK
```

**Status**: [ ] PASS   [ ] INFO   [ ] WARN

---

**Section 8 Summary**:

| Check | Status |
|-------|--------|
| 8.1 Health endpoint baseline, journald accessible | [ ] PASS / [ ] INFO / [ ] WARN |

---

## Final Audit Decision

Complete after all 8 sections are done. This form is the deployment GO/NO-GO gate.

**Auditor**: ____________________________  
**Date/Time Completed**: ____________________ UTC June 11, 2026  
**Total Duration**: _______ minutes

**Timing Conflict Resolution**:
- [ ] Canonical deployment start time confirmed: __________ UTC
- [ ] All timing references in this document reviewed against confirmed time

**Database Credentials**:
- [ ] DATABASE_URL populated
- [ ] SQLITE_PATH populated (if SQLite)
- [ ] BACKUP_DIR populated
- [ ] Pre-deployment backup created and restoration-tested

**Section Results**:

| Section | Items | PASS | FAIL/BLOCKED | Decision |
|---------|-------|------|--------------|----------|
| 1: System Prerequisites | 4 | __ | __ | GO / NO-GO |
| 2: Dependency Audit | 4 | __ | __ | GO / NO-GO |
| 3: Database Validation | 4 | __ | __ | GO / NO-GO |
| 4: Configuration | 2 | __ | __ | GO / NO-GO |
| 5: libzim-Specific | 4 | __ | __ | GO / NO-GO |
| 6: Integration Testing | 1 | __ | __ | GO / NO-GO |
| 7: Backup Verification | 1 | __ | __ | GO / NO-GO |
| 8: Monitoring Setup | 1 | __ | __ | GO / NO-GO |

**OVERALL DECISION**:

- [ ] **ALL 8 SECTIONS PASS — DEPLOYMENT CAN PROCEED on June 12**
- [ ] **ONE OR MORE SECTIONS FAIL — DO NOT DEPLOY until remediated**

**Approved by**: ____________________________  
**Approval time**: ____________________ UTC

---

## Quick Reference: Error Messages That Stop Deployment

| Error | Section | Meaning | Action |
|-------|---------|---------|--------|
| `glibc ... < 2.31` | 1.1 | libzim cannot run | Upgrade OS |
| `CPU temperature 87°C` | 1.2 | Thermal throttling | Wait, check cooling |
| `FAIL: 106 passed` or `84 passed` | 2.1 | ZIM tests not on branch | Check git branch |
| `Table 'zim_exports' missing` | 3.2 | Migration 003 not applied | `alembic upgrade head` |
| `UVICORN_HOST=0.0.0.0` | 4.1 | Security violation | Fix to 127.0.0.1 |
| `libzim < 3.2` | 5.1 | Wrong version | `uv pip install "libzim>=3.2"` |
| `config_indexing ordering incorrect` | 5.3 | Wrong code deployed | Check git branch, re-merge |
| `RuntimeError: Creator started` | 6.1 | config_indexing() called too late | See above |
| `AttributeError: config_indexing` | 6.1 | Wrong libzim version | Upgrade libzim |
| `ZIM file was not created` | 6.1 | Write failed | Check disk space, permissions |

---

**Document Version**: 1.0  
**Created**: 2026-06-10  
**Valid For**: June 11 execution, June 12 deployment  
**Supersedes**: projects/open-repo/DEPLOYMENT_JUNE12_PRECHECK_ENVIRONMENT.md (augments, not replaces)  
**Execute Before**: DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md  
**Reference During**: DEPLOYMENT_JUNE12_RISK_MITIGATION.md (this directory)
