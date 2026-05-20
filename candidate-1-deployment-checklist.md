---
title: "Phase 5 Candidate 1: Deployment Execution Checklist"
project: open-repo
phase: 5
candidate: 1
status: ready-for-execution
date: 2026-05-20
total_effort_hours: 3.0
---

# Phase 5 Candidate 1: Deployment Execution Checklist

**Purpose**: Step-by-step execution checklist with per-item time estimates and immediate next actions. This checklist guides the deployment process from merge decision through production verification.

**Use this document**: Once user approves merge (target: May 26, 2026). Execute sequentially starting May 28–29.

**Total effort**: 2.75–3.0 hours (including 30-minute buffer for unexpected issues)

---

## PHASE 0: Pre-Merge Setup (0.5 hours)

**Timeline**: May 28–29, 2026 (can execute 1–2 days before merge)

### [ ] 0.1 Verify Feature Branch Commit Hash

**Time**: 5 minutes  
**Blocker**: No

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo
git log feature/zimwriter-libzim-activation -3 --oneline
```

**Expected output**:
```
ec0ff7be feat(open-repo): Phase 5 Candidate 1 libzim integration — ZimWriter production-ready
[... previous commits ...]
```

**Verification**: Confirm `ec0ff7be` is the latest commit on the feature branch.

---

### [ ] 0.2 Confirm System Meets Prerequisites

**Time**: 5 minutes  
**Blocker**: Yes — if any fail, stop and troubleshoot

```bash
# Check Python version
python3 --version
# Expected: Python 3.11.2 or compatible 3.11.x

# Check pip/uv available
uv --version
# Expected: uv version 0.x.x (any recent version)

# Check git available
git --version
# Expected: git version 2.x.x
```

**Verification**: All commands succeed without errors.

---

### [ ] 0.3 Create Test Environment Directory

**Time**: 5 minutes  
**Blocker**: No

```bash
# Create temporary directory for test artifacts
mkdir -p /tmp/candidate-1-deploy
cd /tmp/candidate-1-deploy

# Create subdirectories for test outputs
mkdir -p test-zims logs

echo "Test directory ready: /tmp/candidate-1-deploy"
```

**Verification**: Directory exists and is writable.

---

### [ ] 0.4 Install libzim Python Wheel (15 minutes)

**Time**: 15 minutes  
**Blocker**: Yes — required for deployment

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# Install libzim >= 3.2, < 4.0
uv pip install "libzim>=3.2,<4.0"

# Verify installation
python -c "from libzim.writer import Creator, Item, StringProvider, Hint; print('✓ libzim imports OK')"
```

**Expected output**:
```
✓ libzim imports OK
```

**Troubleshooting**:
- If wheel not found: Fall back to source build (adds 15 min; acceptable)
- If import fails: Check `uv pip list | grep libzim` — should show `libzim 3.10.0`
- If permission denied: Check venv is active (`which python` should show `.venv/bin/python`)

---

### [ ] 0.5 Optional: Install zim-tools Binary (5 minutes)

**Time**: 5 minutes  
**Blocker**: No — optional but recommended

```bash
# Install zim-tools for zimcheck validation
sudo apt-get update && sudo apt-get install -y zim-tools

# Verify installation
zimcheck --version
# Expected: Something like "1.6.0"
```

**Troubleshooting**:
- If `apt-get` fails: `zimcheck` is optional; tests will skip zimcheck validation
- If no sudo access: Deploy without zimcheck validation (acceptable for MVP)

---

## PHASE 1: Manual Pre-Deployment Testing (1.5 hours)

**Timeline**: May 28–29, 2026 (critical path — complete before merge)

### [ ] 1.1 Run ZIM Test Suite (30 minutes)

**Time**: 30 minutes  
**Blocker**: Yes — all 84 tests must pass

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# Run ZIM-specific tests
uv run pytest tests/integration/test_export_pipeline.py -v --tb=short 2>&1 | tee /tmp/candidate-1-deploy/logs/test-zim.log

# Count passing tests
uv run pytest tests/integration/test_export_pipeline.py --tb=no -q | tail -1
```

**Expected output**:
```
============================== 84 passed in 0.14s ===============================
```

**Verification checklist**:
- [ ] Line shows `84 passed`
- [ ] No failures (`FAILED` should not appear)
- [ ] Execution time <1 second (real libzim integration should be fast)

**Troubleshooting**:
- If tests fail: Check libzim import — run `python -c "from libzim.writer import Creator"`
- If memory errors: Check available RAM — `free -h`
- If timeout: Run single test in isolation — `uv run pytest tests/integration/test_export_pipeline.py::test_valid_metadata_initializes -v`

**Decision point**: If any test fails, **STOP deployment. Do NOT proceed to merge.** Escalate to development team.

---

### [ ] 1.2 Single-Article Export Test (10 minutes)

**Time**: 10 minutes  
**Blocker**: Yes — verifies real libzim execution

Create file `/tmp/candidate-1-deploy/test_single_article.py`:

```python
"""Test single-article ZIM export with real libzim."""
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 
                "dev/SuperClaude_Framework/projects/open-repo/backend"))

from app.services.export.zim_writer import (
    ZimWriter, ZimMetadata, ExportConfig, ZimEntry, ExportScope
)

print("Creating metadata...")
metadata = ZimMetadata(
    title="Single Article Test",
    description="MVP single-article test",
    language="eng",
    creator="Test User",
    publisher="Test",
    source_url="https://test.example.org",
    date="2026-05-20",
    name="test_single_eng_nopic",
    flavour="nopic",
)

print("Creating config...")
config = ExportConfig(
    scope=ExportScope.LOCAL_ONLY,
    flavour="nopic",
    language="en",
    language_iso3="eng",
)

output_path = Path("/tmp/candidate-1-deploy/test-zims/test_single.zim")
print(f"Output path: {output_path}")

print("Initializing ZimWriter...")
writer = ZimWriter(
    metadata=metadata,
    config=config,
    output_path=output_path,
    zimcheck_binary=None,  # Skip zimcheck for now
)

print("Adding article...")
writer.add_article(
    path="index",
    content="<h1>Welcome</h1><p>This is a test article for MVP validation.</p>",
    article_type="procedure",
    language="en",
)

print("Creating ZIM file...")
result = writer.create_zim(run_zimcheck=False)

print(f"✓ ZIM created successfully")
print(f"  Path: {result.output_path}")
print(f"  Size: {result.file_size_bytes} bytes")
print(f"  Articles: {result.article_count}")
print(f"  SHA-256: {result.sha256[:16]}...")
print(f"  Name: {result.name}")
print(f"  Flavour: {result.flavour}")
```

Run:
```bash
cd /tmp/candidate-1-deploy
python test_single_article.py 2>&1 | tee logs/test-single-article.log
```

**Expected output**:
```
Creating metadata...
Creating config...
Output path: /tmp/candidate-1-deploy/test-zims/test_single.zim
Initializing ZimWriter...
Adding article...
Creating ZIM file...
✓ ZIM created successfully
  Path: /tmp/candidate-1-deploy/test-zims/test_single.zim
  Size: 12345 bytes
  Articles: 1
  SHA-256: a1b2c3d4e5f6g7h8...
  Name: test_single_eng_nopic
  Flavour: nopic
```

**Verification checklist**:
- [ ] File created at `/tmp/candidate-1-deploy/test-zims/test_single.zim`
- [ ] File size > 1000 bytes (not a stub; real ZIM)
- [ ] Articles count = 1
- [ ] SHA-256 present and 64 characters long
- [ ] Metadata name and flavour match

---

### [ ] 1.3 Multi-Article Export Test (10 minutes)

**Time**: 10 minutes  
**Blocker**: No — supplementary verification

Create file `/tmp/candidate-1-deploy/test_multi_article.py`:

```python
"""Test multi-article ZIM export with real libzim."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / 
                "dev/SuperClaude_Framework/projects/open-repo/backend"))

from app.services.export.zim_writer import (
    ZimWriter, ZimMetadata, ExportConfig, ExportScope
)

print("Creating metadata...")
metadata = ZimMetadata(
    title="Multi-Article Test Archive",
    description="Multi-article MVP export test",
    language="eng",
    creator="Test User",
    publisher="Test",
    source_url="https://test.example.org",
    date="2026-05-20",
    name="test_multi_eng_nopic",
    flavour="nopic",
)

print("Creating config...")
config = ExportConfig(
    scope=ExportScope.LOCAL_ONLY,
    flavour="nopic",
    language="en",
    language_iso3="eng",
)

output_path = Path("/tmp/candidate-1-deploy/test-zims/test_multi.zim")

print("Initializing ZimWriter...")
writer = ZimWriter(
    metadata=metadata,
    config=config,
    output_path=output_path,
    zimcheck_binary=None,
)

print("Adding 10 test articles...")
for i in range(10):
    path = f"article_{i}" if i > 0 else "index"
    title = f"Article {i}" if i > 0 else "Index"
    content = f"<h1>{title}</h1><p>Test content for article {i}.</p>"
    
    writer.add_article(
        path=path,
        content=content,
        article_type="procedure",
        language="en",
    )

print("Creating ZIM file...")
result = writer.create_zim(run_zimcheck=False)

print(f"✓ Multi-article ZIM created")
print(f"  Path: {result.output_path}")
print(f"  Size: {result.file_size_bytes} bytes")
print(f"  Articles: {result.article_count}")
print(f"  Resources: {result.resource_count}")
print(f"  SHA-256: {result.sha256[:16]}...")
```

Run:
```bash
cd /tmp/candidate-1-deploy
python test_multi_article.py 2>&1 | tee logs/test-multi-article.log
```

**Expected output**:
```
✓ Multi-article ZIM created
  Path: /tmp/candidate-1-deploy/test-zims/test_multi.zim
  Size: 45678 bytes
  Articles: 10
  Resources: 0
  SHA-256: b2c3d4e5f6g7h8i9...
```

**Verification**: Articles count = 10, file size reasonable (>5000 bytes).

---

### [ ] 1.4 Optional: zimcheck Validation (5 minutes)

**Time**: 5 minutes  
**Blocker**: No — optional if zim-tools installed

```bash
# Run zimcheck on test files (if available)
if command -v zimcheck &> /dev/null; then
    echo "Running zimcheck on test ZIM files..."
    zimcheck /tmp/candidate-1-deploy/test-zims/test_single.zim
    zimcheck /tmp/candidate-1-deploy/test-zims/test_multi.zim
    echo "✓ zimcheck validation complete"
else
    echo "zim-tools not installed; skipping zimcheck (optional)"
fi
```

**Expected output** (if zimcheck available):
```
Checking /tmp/candidate-1-deploy/test-zims/test_single.zim
  Errors: 0
  Warnings: 0 (or minor illustration size warnings; acceptable)
Summary: 100% OK

Checking /tmp/candidate-1-deploy/test-zims/test_multi.zim
  Errors: 0
Summary: 100% OK
```

---

### [ ] 1.5 Verify No Federation Regression (15 minutes)

**Time**: 15 minutes  
**Blocker**: Yes — must ensure Phase 4 unaffected

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# Run all tests (full suite)
uv run pytest tests/ -v --tb=short 2>&1 | tee /tmp/candidate-1-deploy/logs/full-test-suite.log

# Count results
echo "Test summary:"
uv run pytest tests/ --tb=no -q 2>&1 | tail -3
```

**Expected output**:
```
============================== X passed in Y.XXs ===============================
```

**Verification checklist**:
- [ ] No failures reported
- [ ] All tests pass (including federation tests)
- [ ] Execution time reasonable (<5 min for full suite)

---

## PHASE 2: Merge & Integration (0.25 hours)

**Timeline**: May 30, 2026 (production merge day)

### [ ] 2.1 Verify Current Branch is master

**Time**: 2 minutes  
**Blocker**: Yes

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo

git branch
# Expected: * master (current branch marked with *)

git log -1 --oneline
# Expected: Latest commit on master (before merge)
```

**Verification**: Confirm `master` branch is checked out.

---

### [ ] 2.2 Check for Uncommitted Changes

**Time**: 2 minutes  
**Blocker**: Yes — working directory must be clean

```bash
git status
# Expected: "On branch master" and "nothing to commit, working tree clean"
```

**If changes present**: Stash or commit them before merge.

---

### [ ] 2.3 Dry-run Merge (No Commit)

**Time**: 5 minutes  
**Blocker**: Yes

```bash
git merge --no-commit --no-ff feature/zimwriter-libzim-activation

# Review changes
git diff --cached --stat

# Abort (do NOT commit yet)
git merge --abort
```

**Expected output**:
```
Merge made by the 'ort' strategy.
 projects/open-repo/backend/app/services/export/zim_writer.py | 143 ++++
 projects/open-repo/backend/alembic/versions/003_add_zim_exports_table.py | 57 ++
 projects/open-repo/backend/pyproject.toml | 1 +
 3 files changed, 201 insertions(+), 42 deletions(-)
```

**Verification checklist**:
- [ ] 3 files modified (zim_writer.py, migration, pyproject.toml)
- [ ] No unexpected files changed
- [ ] No conflicts reported (Merge made by 'ort' strategy)

**Troubleshooting**:
- If conflicts occur: Note the conflicting files and resolve:
  - `zim_writer.py`: Ensure libzim imports guarded with `try/except`
  - `pyproject.toml`: Ensure `libzim>=3.2,<4.0` dependency is present
  - `migration`: Check Alembic version number is unique (003 is correct)

---

### [ ] 2.4 Execute Real Merge (No Abort)

**Time**: 5 minutes  
**Blocker**: No (point of no return)

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo

# Perform the actual merge
git merge --no-ff feature/zimwriter-libzim-activation -m "feat(open-repo): ZimWriter libzim activation — Phase 5.1 MVP (offline export)"

# Verify merge succeeded
git log -3 --oneline
# Expected: Latest commit is the merge commit from feature branch
```

**Expected output**:
```
Merge made by the 'ort' strategy.
 3 files changed, 201 insertions(+)
 create mode 100644 projects/open-repo/backend/alembic/versions/003_add_zim_exports_table.py
```

**Verification checklist**:
- [ ] Merge completed without errors
- [ ] 3 files modified as expected
- [ ] New migration created

---

### [ ] 2.5 Verify Merge in Log

**Time**: 3 minutes  
**Blocker**: No

```bash
# View the merged commit
git show --stat

# Verify code is present
git log --oneline -5

# Check branch has merged
git branch -v
# Expected: master points to merge commit
```

**Verification**: Latest commit on master is the merge commit; feature branch changes are present.

---

## PHASE 3: Post-Merge Testing (1.5 hours)

**Timeline**: May 30, 2026 (immediately after merge)

### [ ] 3.1 Run Full Test Suite (45 minutes)

**Time**: 45 minutes  
**Blocker**: Yes — all tests must pass

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# Run full test suite with detailed output
uv run pytest tests/ -v --tb=short 2>&1 | tee /tmp/candidate-1-deploy/logs/post-merge-tests.log

# Summary
echo "Test summary:"
uv run pytest tests/ --tb=no -q 2>&1 | tail -3
```

**Expected output**:
```
============================== X passed in Y.XXs ===============================
```

**Verification checklist**:
- [ ] All tests pass (including 84 ZIM tests)
- [ ] No failures or errors
- [ ] Federation tests pass (Phase 4 unaffected)

**Troubleshooting**:
- If test fails: Check error message in log file
- If libzim import error: Verify `uv pip list | grep libzim`
- If migration error: Check Alembic ran correctly — `alembic current`

---

### [ ] 3.2 Manual 8-Step Validation (45 minutes)

**Time**: 45 minutes  
**Blocker**: No — supplementary verification

Execute the following in sequence:

#### Step A: Single-Article Export (5 min)
```bash
cd /tmp/candidate-1-deploy
python test_single_article.py
# Expected: ✓ ZIM created successfully
```

#### Step B: Multi-Article Export (10 min)
```bash
cd /tmp/candidate-1-deploy
python test_multi_article.py
# Expected: ✓ Multi-article ZIM created
```

#### Step C: zimcheck Validation (5 min, if available)
```bash
if command -v zimcheck &> /dev/null; then
    zimcheck /tmp/candidate-1-deploy/test-zims/test_single.zim
    zimcheck /tmp/candidate-1-deploy/test-zims/test_multi.zim
fi
# Expected: No errors, summary 100% OK
```

#### Step D: Memory Check (5 min)
```bash
# Monitor memory during multi-article export
free -h
df -h
# Expected: >1GB free RAM, >5GB free disk
```

#### Step E: Temp File Cleanup (5 min)
```bash
# Verify no stranded temp files
find /tmp -name "*zim*.tmp" 2>/dev/null | wc -l
# Expected: 0

# Verify test ZIMs exist
ls -lh /tmp/candidate-1-deploy/test-zims/
# Expected: test_single.zim, test_multi.zim present
```

#### Step F: Log Review (10 min)
```bash
# Check for errors in logs
grep -i "error\|warning\|exception" /tmp/candidate-1-deploy/logs/*.log | head -20
# Expected: No critical errors; warnings acceptable

# Check test execution details
tail -20 /tmp/candidate-1-deploy/logs/post-merge-tests.log
# Expected: "X passed" summary
```

---

### [ ] 3.3 Check Disk Space & Cleanup (15 minutes)

**Time**: 15 minutes  
**Blocker**: No

```bash
# Check available disk space
df -h /home /tmp
# Expected: >5GB free on each partition

# List test artifacts
du -sh /tmp/candidate-1-deploy/*
# Expected: Total <100MB (small test exports)

# Archive logs for later review (optional)
tar -czf /tmp/candidate-1-deploy/logs.tar.gz /tmp/candidate-1-deploy/logs/
```

---

## PHASE 4: Production Deployment (0.5 hours)

**Timeline**: May 30, 2026 (after post-merge testing)

### [ ] 4.1 Update Database (Run Alembic Migration)

**Time**: 5 minutes  
**Blocker**: Yes

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# Check current migration version
alembic current
# Expected: Shows current version (before 003)

# Run pending migrations
alembic upgrade head
# Expected: "Running upgrade ... -> 003..."

# Verify new version
alembic current
# Expected: Shows version 003 as current
```

**Expected output**:
```
Running upgrade 002 -> 003 ... done
```

**Verification checklist**:
- [ ] Alembic upgrade succeeds
- [ ] Version updated to 003
- [ ] No SQL errors

**Troubleshooting**:
- If migration fails: Check database connectivity — `psql -U user -d dbname -c "SELECT 1"`
- If table already exists: Migration is idempotent; safe to re-run

---

### [ ] 4.2 Restart API Server (5 minutes)

**Time**: 5 minutes  
**Blocker**: No (optional if running in container)

```bash
# If running in Docker:
# docker restart open-repo

# If running systemd service:
# systemctl restart open-repo-api

# If running directly:
# Kill existing process
pkill -f "uvicorn.*open.*repo" || echo "No process found"

# Restart (in new terminal or via supervisor)
# cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
# uvicorn app.main:app --host 127.0.0.1 --port 8000
```

**Verification**: Server restarts without errors.

---

### [ ] 4.3 Smoke Test (10 minutes)

**Time**: 10 minutes  
**Blocker**: No (supplementary)

```bash
# Health check
curl -s http://localhost:8000/health || echo "Server not responding"

# Test imports (if API not running)
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
python -c "from app.services.export.zim_writer import ZimWriter; print('✓ ZimWriter importable')"

# Check migration applied
python -c "from sqlalchemy import inspect, create_engine; engine = create_engine('sqlite:///test.db'); print(inspect(engine).get_table_names())" || echo "SQLite test skipped"
```

**Expected output**:
```
✓ ZimWriter importable
```

---

### [ ] 4.4 Check Server Logs (10 minutes)

**Time**: 10 minutes  
**Blocker**: No

```bash
# View recent logs
docker logs open-repo 2>&1 | grep -i "zim\|error" | tail -20
# OR
tail -50 /var/log/open-repo/app.log | grep -i "zim\|error"
# OR
journalctl -u open-repo-api -n 50 | grep -i "zim\|error"

# Expected: No critical errors; normal startup messages
```

**Verification**: No error messages related to libzim or ZIM exports.

---

### [ ] 4.5 Verify Database Changes (5 minutes)

**Time**: 5 minutes  
**Blocker**: No (verification only)

```bash
# Check that zim_exports table exists (if using database)
# psql -U dbuser -d dbname -c "SELECT * FROM zim_exports LIMIT 1;" || echo "Table empty (expected)"

# Or with SQLite:
# sqlite3 app.db ".tables" | grep zim
```

**Expected**: Table exists (may be empty after initial deploy).

---

## PHASE 5: Post-Deployment Verification (0.25 hours)

**Timeline**: May 30–31, 2026 (final validation)

### [ ] 5.1 Run Test Suite One More Time (10 minutes)

**Time**: 10 minutes  
**Blocker**: No (final sanity check)

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

uv run pytest tests/ -q --tb=short 2>&1 | tail -10
```

**Expected**: All tests still pass.

---

### [ ] 5.2 Document Deployment (10 minutes)

**Time**: 10 minutes  
**Blocker**: No

Create a deployment record file:

```bash
cat > /tmp/candidate-1-deploy/DEPLOYMENT_RECORD.md << 'EOF'
# Phase 5 Candidate 1: Deployment Record

**Date**: 2026-05-30  
**Deployed by**: [User name]  
**Branch**: master (merged from feature/zimwriter-libzim-activation)  
**Commit**: [hash of merge commit]

## Checklist Summary

- [x] Phase 0: Pre-merge setup (0.5 hours)
- [x] Phase 1: Manual testing (1.5 hours)
- [x] Phase 2: Merge (0.25 hours)
- [x] Phase 3: Post-merge testing (1.5 hours)
- [x] Phase 4: Deployment (0.5 hours)
- [x] Phase 5: Verification (0.25 hours)

## Test Results

- ZIM tests: 84/84 passing
- Full suite: X/X passing
- Federation tests: All passing (no regression)

## Known Issues

None identified during deployment.

## Next Steps

1. Begin Phase 5.2 planning (Xapian FTS integration)
2. Add HTTP API endpoint for exports
3. Monitor production for any issues

## Monitoring

- [ ] Check logs daily for first week
- [ ] Monitor export duration (target: <10s for single article)
- [ ] Track ZIM file sizes (typical MVP: <200MB)

EOF

cat /tmp/candidate-1-deploy/DEPLOYMENT_RECORD.md
```

---

### [ ] 5.3 Cleanup Test Artifacts (5 minutes)

**Time**: 5 minutes  
**Blocker**: No

```bash
# Remove test ZIM files (optional; can keep for reference)
# rm -f /tmp/candidate-1-deploy/test-zims/*.zim

# Remove test scripts
# rm -f /tmp/candidate-1-deploy/*.py

# Archive logs for later review
# tar -czf /tmp/candidate-1-deploy/deployment-logs.tar.gz /tmp/candidate-1-deploy/logs/

# Keep deployment record
echo "Deployment record kept at: /tmp/candidate-1-deploy/DEPLOYMENT_RECORD.md"
```

---

## PHASE 6: Post-Deployment Monitoring (Ongoing)

**Timeline**: May 31+ (monitor for 1 week post-deploy)

### Daily Checks (First Week)

```bash
# Daily: Check for errors in ZIM export logs
grep -i "error\|exception" /var/log/open-repo/app.log | grep -i "zim"

# Daily: Verify server is responding
curl -s http://localhost:8000/health

# Daily: Check disk space
df -h | grep -E "^/dev"

# Weekly: Run full test suite
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
uv run pytest tests/ -q
```

### Monitoring Metrics

Track these during first week:

- Export job count (expected: 0 for MVP; increases with user adoption)
- Export duration (target: <10s for single article, <60s for 100 articles)
- ZIM file sizes (typical: 5MB–200MB depending on scope)
- Error rate (target: 0% for MVP; document any failures)

### Escalation

If issues arise:

1. Check logs: `grep -i "error\|libzim" /var/log/open-repo/app.log`
2. Verify libzim installed: `python -c "from libzim.writer import Creator; print('OK')"`
3. Re-run tests: `uv run pytest tests/integration/test_export_pipeline.py -v`
4. If unresolved: Escalate to development team with error log excerpt

---

## Summary & Sign-Off

### Pre-Deployment Checklist (Phase 0–1)

| Step | Time | Status |
|------|------|--------|
| 0.1 Verify feature branch | 5 min | [ ] |
| 0.2 Confirm prerequisites | 5 min | [ ] |
| 0.3 Create test directory | 5 min | [ ] |
| 0.4 Install libzim wheel | 15 min | [ ] |
| 0.5 Install zim-tools (optional) | 5 min | [ ] |
| 1.1 Run ZIM tests (84 pass) | 30 min | [ ] |
| 1.2 Single-article export | 10 min | [ ] |
| 1.3 Multi-article export | 10 min | [ ] |
| 1.4 zimcheck (optional) | 5 min | [ ] |
| 1.5 No federation regression | 15 min | [ ] |

**Phase 0–1 Total**: 2 hours

### Merge & Deployment Checklist (Phase 2–5)

| Step | Time | Status |
|------|------|--------|
| 2.1 Verify master branch | 2 min | [ ] |
| 2.2 Check working directory clean | 2 min | [ ] |
| 2.3 Dry-run merge | 5 min | [ ] |
| 2.4 Execute real merge | 5 min | [ ] |
| 2.5 Verify merge in log | 3 min | [ ] |
| 3.1 Full test suite | 45 min | [ ] |
| 3.2 Manual 8-step validation | 45 min | [ ] |
| 3.3 Disk space check | 15 min | [ ] |
| 4.1 Run Alembic migration | 5 min | [ ] |
| 4.2 Restart API server | 5 min | [ ] |
| 4.3 Smoke test | 10 min | [ ] |
| 4.4 Check logs | 10 min | [ ] |
| 4.5 Verify database changes | 5 min | [ ] |
| 5.1 Final test run | 10 min | [ ] |
| 5.2 Document deployment | 10 min | [ ] |
| 5.3 Cleanup (optional) | 5 min | [ ] |

**Phase 2–5 Total**: 1 hour 15 minutes

### **Total Estimated Time: 3.25 hours** (with 15-minute buffer)

---

## Quick Reference Commands

**Emergency rollback** (if critical issue):

```bash
# Revert merge
git revert -m 1 HEAD

# Or reset to before merge
git reset --hard HEAD~1

# Remove libzim if needed
uv pip uninstall -y libzim
```

**Health check**:

```bash
# Verify libzim
python -c "from libzim.writer import Creator; print('✓ libzim OK')"

# Run tests
uv run pytest tests/integration/test_export_pipeline.py -q

# Check logs
docker logs open-repo | grep -i error | tail -10
```

**Get deployment status**:

```bash
# Check what's on master
git log -3 --oneline

# Verify merge commit present
git log --oneline | grep -i "libzim\|zimwriter"

# Check test results
uv run pytest tests/ --tb=no -q
```

---

## Sign-Off

**Pre-deployment completed**: [ ] Date: ______  
**Merge executed**: [ ] Date: ______  
**Post-deployment verification passed**: [ ] Date: ______  
**Production monitoring initiated**: [ ] Date: ______  

**Deployed by**: ______________________  
**Reviewed by**: ______________________ (optional)  

---

**Document prepared**: May 20, 2026  
**Status**: Ready for execution  
**Recommended execution date**: May 28–30, 2026  
**Total effort**: 3–3.25 hours
