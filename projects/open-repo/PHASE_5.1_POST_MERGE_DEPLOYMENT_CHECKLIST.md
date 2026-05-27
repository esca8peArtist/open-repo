---
title: "Phase 5.1 Post-Merge Deployment Checklist"
project: open-repo
phase: 5.1
document_type: deployment-checklist
status: ready-to-execute
created: 2026-05-27
depends_on: "feature/zimwriter-libzim-activation merge approval"
target_merge_window: "May 26–29, 2026"
target_production: "May 30–31, 2026"
---

# Phase 5.1 Post-Merge Deployment Checklist

**Purpose**: Runnable checklist for the full deployment sequence after the `feature/zimwriter-libzim-activation` branch is merged. Execute phases in order. Do not skip ahead.

**Current status**: Feature branch has 51/51 ZIM tests passing, 240 passed / 19 skipped / 35 warnings total. Merge verdict: CONDITIONAL APPROVE (0 merge blockers, 3 post-merge action items). See `phase-5-1-pre-merge-audit-findings.md` for audit details.

**Estimated total time**: 12–18 hours across 4 phases over 5–6 days.

**Deployment target**: Raspberry Pi 5 (raspby1, 100.70.184.84), aarch64, Python 3.11.2, 4–8 GB RAM.

---

## Phase 1: Pre-Merge Verification (May 26–27)

**Objective**: Confirm feature branch is in merge-ready state before user approves PR.
**Duration**: 45–90 minutes.
**Who runs this**: Agent or developer verifying branch state.

### 1.1 Pull Feature Branch and Inspect

- [ ] **Pull the feature branch locally**:
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo
  git fetch open-repo
  git checkout feature/zimwriter-libzim-activation
  git log --oneline master..HEAD
  ```
  **Expected**: 6 commits ahead of master (conventional commit format: `feat()`, `fix()`, `docs()`, `audit()` prefixes).

- [ ] **Confirm branch is up-to-date with master** (no trailing divergence):
  ```bash
  git log --oneline feature/zimwriter-libzim-activation..master
  ```
  **Expected**: Empty output (no master commits missing from branch). If not empty, rebase is required before merge.

- [ ] **Check for merge conflict markers**:
  ```bash
  grep -rn "<<<<<<\|=======\|>>>>>>>" \
    /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend/app/services/export/zim_writer.py \
    /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend/tests/
  ```
  **Expected**: Zero matches. If any found, resolve before proceeding.

### 1.2 Run Full Test Suite on Feature Branch

- [ ] **Run the complete test suite**:
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  uv run pytest tests/ -q --tb=short 2>&1 | tail -30
  ```
  **Expected test count**: 240 passed, 19 skipped, 35 warnings. Zero failures.

- [ ] **Run the ZIM export integration tests specifically** (the 51 new tests):
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  uv run pytest tests/ -k "zim" -v --tb=short 2>&1 | tail -60
  ```
  **Expected**: 51 passed. Zero failures. This is the gate metric — if any of the 51 ZIM tests fail, do not merge until root cause is identified and fixed.

- [ ] **Confirm ZIM magic bytes test passes** (the test that proves real libzim is running, not stub):
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  uv run pytest tests/ -k "magic" -v
  ```
  **Expected**: Test `test_zim_writer_creates_real_zim_file` passes. If no test by that name exists, verify `test_zim_magic_bytes` or equivalent. The test must assert `output.read(4) == b'\x5a\x49\x4d\x04'` — this proves the Creator context manager path is active.

- [ ] **Run linting**:
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  uv run ruff check app/services/export/ --select=E,F,W
  ```
  **Expected**: 0 errors. If errors present, fix before merge.

### 1.3 Verify libzim Wheel Availability on Deployment Target

The deployment target is a Raspberry Pi 5 (aarch64). The `libzim>=3.10.0,<4.0` wheel must be available for `cp311-manylinux_2_27_aarch64` before the merge is approved. This was verified May 21 as part of the pre-merge audit, but confirm before executing the deployment.

- [ ] **Check ARM64 wheel availability** (run from Pi 5 or confirm via PyPI index):
  ```bash
  # If running from the Pi:
  pip index versions libzim | grep -i "3.10"
  ```
  **Expected**: libzim 3.10.0 or later listed. If wheel not found, the deployment will require a source build (C++ toolchain, ~30 minutes). See rollback trigger R4 in Phase 4.

- [ ] **Verify zimcheck binary is available** on deployment target:
  ```bash
  which zimcheck && zimcheck --version
  ```
  **Expected**: `/usr/bin/zimcheck` and version line (3.1.3 or similar). If not found: `sudo apt-get install zim-tools`.

### 1.4 Pre-Merge Verification Complete

- [ ] All 240 tests pass (including 51 ZIM tests).
- [ ] Zero merge conflict markers.
- [ ] Branch is up-to-date with master.
- [ ] ARM64 libzim wheel confirmed available.
- [ ] Linting passes.

**Gate decision**: If all items above are checked, signal the user that the branch is ready for merge. Do not merge yourself — write PR description in CHECKIN.md and wait for user approval.

---

## Phase 2: Post-Merge Validation (May 28–29, Immediately After Merge)

**Objective**: Verify merge stability, database migrations, and that the codebase is still healthy immediately after the user merges the PR.
**Duration**: 2–4 hours.
**Trigger**: Run as soon as the user confirms the PR is merged.

### 2.1 Pull Merged Master and Confirm State

- [ ] **Switch to master and pull**:
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo
  git checkout master
  git pull open-repo master
  git log --oneline | head -5
  ```
  **Expected**: Merge commit at top, followed by feature branch commits. Confirm `feature/zimwriter-libzim-activation` commits are now visible in master history.

- [ ] **Delete the feature branch** (cleanup):
  ```bash
  git branch -d feature/zimwriter-libzim-activation
  git push open-repo --delete feature/zimwriter-libzim-activation
  ```

### 2.2 Run Alembic Migration on Post-Merge Database

This is the first critical gate. Migration 003 (`add_zim_exports_table`) must apply cleanly. The migration creates a 26-column `zim_exports` table.

- [ ] **Run migration from clean state**:
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  rm -f sqlite.db  # Remove any existing dev database
  uv run alembic upgrade head
  ```
  **Expected**: Migration runs without errors. All 3 migrations (001, 002, 003) apply in sequence.

- [ ] **Verify `zim_exports` table was created correctly**:
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  sqlite3 sqlite.db ".schema zim_exports"
  ```
  **Expected**: Schema output with `id`, `zim_uuid`, `name`, `flavour`, `language`, `period`, `article_count`, `file_size_bytes`, `sha256`, `title`, `description`, `cdn_url`, `local_path`, `status`, `is_current`, `is_reference`, `export_scope`, `scope_value`, `include_images`, `zimcheck_passed`, `zimcheck_output`, `generation_duration_seconds`, `started_at`, `completed_at`, `superseded_at`, `deleted_at`, `created_at`, `updated_at` columns. All 26 columns must be present.

- [ ] **Verify migration version**:
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  uv run alembic current
  ```
  **Expected**: `003 (head)` — indicates all migrations applied.

- [ ] **Verify foreign key constraints are valid**:
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  sqlite3 sqlite.db "PRAGMA foreign_key_check;"
  ```
  **Expected**: Empty output (no constraint violations).

- [ ] **Verify existing tables are unaffected**:
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  sqlite3 sqlite.db ".tables"
  ```
  **Expected**: `content_items`, `endorsements`, `contributions`, other Phase 1–4 tables, AND `zim_exports`. Migration must not have dropped or modified any earlier tables.

**Rollback trigger**: If migration fails with any error — `alembic.exc.CommandError`, SQL syntax error, or any exception — STOP. Do not attempt to proceed to Phase 3. See rollback triggers section.

### 2.3 Run Post-Merge Test Suite

- [ ] **Run full test suite on master**:
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  uv run pytest tests/ -q --tb=short 2>&1 | tail -30
  ```
  **Expected**: 240 passed, 19 skipped, 35 warnings. Zero failures. This must match the pre-merge count exactly. Any regression (fewer passing tests or new failures) is a blocker.

- [ ] **Run ZIM integration tests specifically**:
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  uv run pytest tests/ -k "zim" -v --tb=short
  ```
  **Expected**: 51 passed. Zero failures.

- [ ] **Check that all Phase 1–4 tests still pass** (no regressions):
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  uv run pytest tests/ -k "not zim" -q --tb=short 2>&1 | tail -20
  ```
  **Expected**: All prior tests pass. If any previously passing test now fails, treat as a merge-induced regression and investigate before proceeding.

### 2.4 Test ZIM Export on Post-Merge Master

This verifies the real libzim Creator path is active on the merged master (not stub).

- [ ] **Install libzim on the development machine**:
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  uv pip install "libzim>=3.10.0,<4.0"
  ```

- [ ] **Run the ZIM magic-bytes smoke test**:
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  uv run python3 -c "
  import tempfile
  from pathlib import Path
  from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig

  tmp = tempfile.mkdtemp()
  meta = ZimMetadata(
      title='Post-Merge Smoke Test',
      description='Verify ZIM creator path is active',
      language='eng',
      name='open-repo_en_nopic',
      flavour='nopic',
      creator='Open-Repo Community',
      publisher='Open-Repo',
      source_url='https://example.org'
  )
  config = ExportConfig()
  writer = ZimWriter(metadata=meta, config=config, output_path=Path(tmp) / 'smoke_test.zim', zimcheck_binary=None)
  writer.add_article(path='index', content='<html><body><h1>Smoke Test</h1></body></html>', article_type='procedure')
  result = writer.create_zim(run_zimcheck=False)

  with open(result.output_path, 'rb') as f:
      magic = f.read(4)
  assert magic == b'\x5a\x49\x4d\x04', f'Expected ZIM magic bytes, got: {magic.hex()}'
  print('Post-merge ZIM smoke test PASSED. Real ZIM file created:', result.output_path)
  print('File size:', result.file_size_bytes, 'bytes')
  "
  ```
  **Expected**: `Post-merge ZIM smoke test PASSED.`

  **If magic bytes are wrong** (`5a 49 4d 04` not found): The stub path is still running. This means `_LIBZIM_AVAILABLE` is `False` — libzim import failed silently. Run `uv run python3 -c "import libzim; print(libzim.__version__)"` to diagnose. If libzim is not installed, run the install step above.

### 2.5 Record Post-Merge Baseline

After all post-merge tests pass, record the baseline state in a short note:

- [ ] **Document test count**: Total passed = _____, ZIM tests = 51, skipped = 19.
- [ ] **Document migration state**: `alembic current` shows _____.
- [ ] **Document ZIM file size** from smoke test: _____ bytes.
- [ ] **Confirm date/time of merge**: _____ UTC.

### 2.6 Resolve Three Post-Merge Action Items (parallel tracks)

These 3 items were identified in the Session 1447 pre-merge audit. They are not blockers for merge but must be resolved before Phase 5.1 goes live in production. Begin them immediately after post-merge validation passes. All three can be worked in parallel.

**Action Item 1 — XSS fix** (1 hour): Apply `html.escape()` to `source_node_url` and `source_node_name` in the attribution footer in `zim_writer.py`. Add URL scheme validation (reject `javascript:` and `data:`). Add unit test for XSS prevention. See `PHASE_5_1_POST_MERGE_ACTIVATION_CHECKLIST.md` Section 1 for exact code.

**Action Item 2 — ZimExport ORM model** (1.5 hours): Add the `ZimExport` SQLAlchemy class and `ZimExportStatus` enum to `app/models.py`, mapping all 26 migration columns. Add unit tests for `is_active()` and `is_ready()` helper methods. See `PHASE_5_1_POST_MERGE_ACTIVATION_CHECKLIST.md` Section 2 for the full class definition.

**Action Item 3 — pyproject.toml dependency** (30 minutes): Add `libzim>=3.10.0,<4.0` to `[project.dependencies]` in `backend/pyproject.toml`. Verify `uv pip install -e ".[dev]"` resolves cleanly. Confirm `from libzim.writer import Creator` imports without error.

- [ ] Action Item 1 (XSS fix) complete and tested.
- [ ] Action Item 2 (ZimExport ORM) complete and tested.
- [ ] Action Item 3 (pyproject.toml dependency) complete and verified.

---

## Phase 3: Staging Deployment (May 29–30)

**Objective**: Deploy merged master to the staging environment (Pi 5 dev environment), run smoke tests, and monitor for 2 hours with no errors before declaring staging stable.
**Duration**: 3–5 hours active work + 2 hours passive monitoring.
**Prerequisite**: All Phase 2 items complete, including the 3 post-merge action items.

**Staging environment**: The Raspberry Pi 5 (raspby1, 100.70.184.84) running in dev mode. The production deployment target is the Jetson (xxsb-01, 100.120.18.84), which remains untouched until Phase 4.

### 3.1 Sync Code to Staging

- [ ] **Push merged master to open-repo remote**:
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo
  git push open-repo master
  ```

- [ ] **Rsync backend code to Pi 5** (do not use scp):
  ```bash
  rsync -av --exclude='__pycache__' --exclude='*.pyc' --exclude='.git' \
    /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend/ \
    awank@100.70.184.84:/opt/open-repo/backend/
  ```
  **Expected**: File transfer completes without errors. No `rsync error` messages.

- [ ] **Install libzim on Pi 5** (if not already installed):
  ```bash
  ssh awank@100.70.184.84 "cd /opt/open-repo/backend && uv pip install 'libzim>=3.10.0,<4.0'"
  ```
  **Expected**: Install completes in under 2 minutes (ARM64 wheel download). If it exceeds 5 minutes, a source build has started — see rollback trigger R4.

- [ ] **Install zimcheck on Pi 5** (if not already installed):
  ```bash
  ssh awank@100.70.184.84 "sudo apt-get install zim-tools && zimcheck --version"
  ```

- [ ] **Run migrations on staging database**:
  ```bash
  ssh awank@100.70.184.84 "cd /opt/open-repo/backend && uv run alembic upgrade head"
  ```
  **Expected**: Migration 003 applies cleanly. `alembic current` shows `003 (head)`.

### 3.2 Smoke Tests on Staging

- [ ] **Run full test suite on Pi 5**:
  ```bash
  ssh awank@100.70.184.84 "cd /opt/open-repo/backend && uv run pytest tests/ -q --tb=short 2>&1 | tail -30"
  ```
  **Expected**: 240 passed, 19 skipped. Zero failures.

- [ ] **Endpoint availability check** (health endpoint):
  ```bash
  # Start the server on Pi 5 (bind to 127.0.0.1 only — never 0.0.0.0):
  ssh awank@100.70.184.84 "cd /opt/open-repo/backend && \
    uv run uvicorn app.main:app --host 127.0.0.1 --port 8080 --reload &"
  sleep 5

  # Check health endpoint:
  ssh awank@100.70.184.84 "curl -s http://127.0.0.1:8080/health"
  ```
  **Expected**: `{"status": "ok"}` or equivalent health response. If 404 or connection refused, check server logs.

- [ ] **Export endpoint smoke test** (if `/api/v1/export` endpoint exists):
  ```bash
  ssh awank@100.70.184.84 "curl -s -X POST http://127.0.0.1:8080/api/v1/export \
    -H 'Content-Type: application/json' \
    -d '{\"domain\": \"agriculture\", \"flavour\": \"nopic\", \"max_items\": 10}' \
    --max-time 30"
  ```
  **Expected**: Response within 30 seconds with export job ID or ZIM file details. Acceptable responses: 200 OK with job metadata, or 202 Accepted with task ID. Not acceptable: 500 Internal Server Error or timeout.

  **Latency gate**: Export endpoint must respond in under 5 seconds for the initial response (job acceptance), even if the ZIM generation itself takes longer. If initial response takes >5 seconds, investigate FastAPI startup or database query time.

- [ ] **ZIM export function smoke test** (direct Python invocation on Pi 5):
  ```bash
  ssh awank@100.70.184.84 "cd /opt/open-repo/backend && uv run python3 -c \"
  import tempfile
  from pathlib import Path
  from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig

  tmp = tempfile.mkdtemp()
  meta = ZimMetadata(
      title='Staging Smoke Test',
      description='Staging environment validation',
      language='eng',
      name='open-repo_en_nopic',
      flavour='nopic',
      creator='Test',
      publisher='Test',
      source_url='https://example.org'
  )
  writer = ZimWriter(metadata=meta, config=ExportConfig(), output_path=Path(tmp) / 'staging.zim')
  for i in range(20):
      writer.add_article(path=f'item/{i:03d}', content=f'<html><body><h1>Item {i}</h1></body></html>', article_type='procedure')
  writer.add_article(path='index', content='<html><body><h1>Home</h1></body></html>', article_type='procedure')
  result = writer.create_zim()
  print('Staging ZIM OK. Articles:', result.article_count, '| Size:', result.file_size_bytes, 'bytes | zimcheck:', result.zimcheck_passed)
  \""
  ```
  **Expected**: `Staging ZIM OK. Articles: 21 | Size: [>1024] bytes | zimcheck: True`

  **ZIM size gate**: File size must be greater than 1024 bytes. A file smaller than this indicates the stub path ran instead of the Creator path.

### 3.3 Monitor Staging for 2 Hours

- [ ] **Start log monitoring**:
  ```bash
  ssh awank@100.70.184.84 "cd /opt/open-repo/backend && \
    uv run uvicorn app.main:app --host 127.0.0.1 --port 8080 2>&1 | tee /tmp/staging_app.log &"
  ```

- [ ] **Set monitoring start time**: _____ UTC

- [ ] **After 1 hour — check error count in logs**:
  ```bash
  ssh awank@100.70.184.84 "grep -c 'ERROR\|CRITICAL\|Traceback' /tmp/staging_app.log || echo '0 errors'"
  ```
  **Expected**: 0 errors. If any `ERROR` lines appear, inspect immediately.

- [ ] **After 2 hours — final error check**:
  ```bash
  ssh awank@100.70.184.84 "grep -c 'ERROR\|CRITICAL\|Traceback' /tmp/staging_app.log || echo '0 errors'"
  ```
  **Expected**: 0 errors in the full 2-hour window.

- [ ] **Check memory usage** (no memory leak):
  ```bash
  ssh awank@100.70.184.84 "ps aux | grep uvicorn | grep -v grep | awk '{print \"RSS:\", \$6/1024, \"MB\"}'"
  ```
  **Expected**: RSS under 500 MB after 2 hours. If RSS is growing continuously, investigate potential memory leak in the export buffer.

- [ ] **Check thermal state** (Pi 5 thermal ceiling):
  ```bash
  ssh awank@100.70.184.84 "cat /sys/class/thermal/thermal_zone0/temp | awk '{print \$1/1000 \"°C\"}'"
  ```
  **Expected**: Below 87°C at idle. Pi 5 thermal ceiling during compute is 92°C before throttle engages.

### 3.4 Staging Staging Gate Decision

All of the following must be true to proceed to Phase 4 (production):

- [ ] 240 tests pass on Pi 5 staging environment.
- [ ] Health endpoint responds with 200 OK.
- [ ] Export endpoint latency under 5 seconds for initial response.
- [ ] ZIM smoke test produces file >1024 bytes with `zimcheck: True`.
- [ ] 0 errors in 2-hour staging monitoring window.
- [ ] Memory RSS stable (not growing) after 2 hours.
- [ ] CPU temperature below 87°C at idle.

**If any item is not met**: Fix the issue, re-run smoke tests, restart the 2-hour monitoring window. Do not proceed to production until all staging gate criteria pass.

---

## Phase 4: Production Monitoring (May 30–31+)

**Objective**: Deploy to production (if applicable), monitor health check and export endpoint, and maintain clear rollback triggers.
**Duration**: 2–4 hours active work + 48 hours passive monitoring.
**Prerequisite**: Phase 3 staging gate passes completely.

**Note on production target**: The open-repo project's primary deployment is the Pi 5 itself running in local-server mode. If a separate production instance exists (e.g., Docker container on Jetson or external server), follow the same sequence as Phase 3 but against the production environment. If Pi 5 IS the production instance, then staging and production deployment are the same machine, and Phase 4 is the monitoring period following Phase 3 deployment.

### 4.1 Production Deployment

- [ ] **If production is a separate environment from staging**, repeat Phase 3 steps 3.1 and 3.2 against the production target.

- [ ] **If Pi 5 is the production environment** (most likely), promote the staging deployment:
  ```bash
  # Confirm current deployed version
  ssh awank@100.70.184.84 "cd /opt/open-repo/backend && git log --oneline | head -3"
  ```
  **Expected**: Shows merged master commit at top.

- [ ] **Restart application with production settings**:
  ```bash
  ssh awank@100.70.184.84 "pkill -f uvicorn; sleep 2; \
    cd /opt/open-repo/backend && \
    uv run uvicorn app.main:app --host 127.0.0.1 --port 8080 \
    --workers 1 --log-level info 2>&1 >> /opt/open-repo/logs/app.log &"
  ```
  Note: `--host 127.0.0.1` is mandatory. Never `0.0.0.0`. One worker is appropriate for Pi 5 to avoid memory pressure.

- [ ] **Verify production startup**:
  ```bash
  sleep 5
  ssh awank@100.70.184.84 "curl -s http://127.0.0.1:8080/health"
  ```
  **Expected**: Health check responds with 200 OK.

### 4.2 Production Health Monitoring

- [ ] **Set monitoring start time**: _____ UTC

- [ ] **Hour 1 check** — verify health and no errors:
  ```bash
  ssh awank@100.70.184.84 "curl -s http://127.0.0.1:8080/health && \
    grep -c 'ERROR\|CRITICAL' /opt/open-repo/logs/app.log || echo '0 errors'"
  ```
  **Expected**: Health 200 OK, 0 errors.

- [ ] **Hour 4 check** — verify stability and thermal:
  ```bash
  ssh awank@100.70.184.84 "curl -s http://127.0.0.1:8080/health && \
    cat /sys/class/thermal/thermal_zone0/temp | awk '{print \$1/1000 \"°C\"}'"
  ```
  **Expected**: Health OK, temperature below 85°C.

- [ ] **Hour 24 check** — full health and memory review:
  ```bash
  ssh awank@100.70.184.84 "curl -s http://127.0.0.1:8080/health && \
    ps aux | grep uvicorn | grep -v grep | awk '{print \"RSS:\", \$6/1024, \"MB\"}' && \
    grep -c 'ERROR\|CRITICAL' /opt/open-repo/logs/app.log || echo '0'"
  ```
  **Expected**: Health OK, RSS stable (under 500 MB), 0 errors.

- [ ] **Hour 48 check** — final review before declaring production stable:
  ```bash
  ssh awank@100.70.184.84 "curl -s http://127.0.0.1:8080/health && \
    grep -c 'ERROR\|CRITICAL' /opt/open-repo/logs/app.log || echo '0'"
  ```
  **Expected**: Health OK, 0 errors over full 48-hour window.

### 4.3 Alert Thresholds and Rollback Triggers

The following conditions trigger immediate investigation. Each is listed with the specific rollback decision.

**R1 — Database migration fails**
- Symptom: `alembic upgrade head` exits non-zero; `zim_exports` table not created or columns missing.
- Action: STOP. Do not proceed to Phase 3 or 4. Run `uv run alembic downgrade 002` to revert to pre-Phase-5.1 schema. Investigate migration 003 syntax and retry.
- Rollback: Immediate, to pre-merge master. Timeline: 30–60 minutes.

**R2 — ZIM export produces wrong magic bytes**
- Symptom: Smoke test reads `f.read(4)` and does not get `5a 49 4d 04`; output file is zero-byte or contains HTML/plaintext stub content.
- Action: Investigate `_LIBZIM_AVAILABLE` flag. Run `uv run python3 -c "import libzim; print(libzim.__version__)"`. If libzim is not installed, install and retest. If libzim is installed but Creator path is not running, check for uncaught import exception in `zim_writer.py`.
- Rollback: Conditional. If libzim install fixes it, no rollback needed. If code issue, rollback feature branch merge and investigate.

**R3 — ZIM export missing pages (fewer articles than inserted)**
- Symptom: `result.article_count` does not match the number of `add_article()` calls made. Off by more than ±2%.
- Action: Investigate libzim Creator session handling. Check whether `add_item()` raised a silent exception. Run with `--verbose` logging. Check for path collision (duplicate paths overwriting each other).
- Rollback: Do not roll back deployment. Isolate to a single bug. Fix the path collision or Creator exception handling, re-test, and deploy the fix.

**R4 — libzim installation requires source build on ARM64**
- Symptom: `pip install libzim` download takes longer than 5 minutes; compiler output visible; `gcc` or `cmake` invoked.
- Action: Check PyPI for ARM64 wheel. If wheel is not present for libzim 3.10.0, try `libzim>=3.9.0,<4.0` (earlier release with confirmed ARM64 wheel). If neither version has a wheel, provide a Docker image with pre-built libzim.
- Rollback: Delay Phase 3 staging until libzim wheel issue is resolved. The stub path in `_LIBZIM_AVAILABLE` means the application still functions — no emergency rollback needed.

**R5 — Health check fails after production deployment**
- Symptom: `curl http://127.0.0.1:8080/health` returns non-200, or times out after 10 seconds.
- Action: Check uvicorn process is running (`ps aux | grep uvicorn`). Check for import errors in startup logs. Check if port 8080 is in use by another process (`ss -tlnp | grep 8080`).
- Rollback: If health check fails within first 30 minutes: rollback to pre-merge master immediately. If health check was passing and then failed: investigate cause before rolling back (could be an unrelated infrastructure issue).

**R6 — Staging logs show errors during 2-hour monitoring**
- Symptom: `grep -c 'ERROR\|CRITICAL' /tmp/staging_app.log` returns >0.
- Action: Inspect the specific error lines. If error is in ZIM export path: isolate and fix before proceeding to production. If error is in unrelated Phase 1–4 code: assess severity. Critical errors block production deployment. Non-critical warnings do not block.
- Rollback: Fix and re-run 2-hour staging window. Production deployment is blocked until 2-hour staging window completes with 0 errors.

**R7 — Thermal throttling during export**
- Symptom: CPU temperature exceeds 92°C during a ZIM export run; export duration is 2–3x slower than baseline.
- Action: This is not a code bug — it is a hardware constraint. Mitigation: (1) Schedule exports at 02:00 UTC (off-peak), (2) Reduce `max_items` to 500 per export job, (3) Install active cooling (5V fan, ~$5).
- Rollback: Not applicable. No code rollback. Document mitigation and schedule exports off-peak.

### 4.4 Production Stability Declaration

Phase 5.1 is declared production-stable when ALL of the following are true:

- [ ] Health check has returned 200 OK continuously for 48 hours.
- [ ] Zero ERROR or CRITICAL log entries in 48-hour window.
- [ ] Export endpoint has successfully generated at least one ZIM file with `zimcheck: True`.
- [ ] Memory RSS is stable (not growing trend over 48 hours).
- [ ] CPU temperature has not exceeded 92°C (no throttle events).
- [ ] All 3 post-merge action items (XSS fix, ORM model, pyproject.toml) are complete and tested.

Once all items are checked, Phase 5.1 is stable and Phase 5.2 implementation can begin.

---

## Rollback Procedure (If Critical Issue Found Post-Merge)

Execute this procedure only if a critical issue is found that cannot be patched quickly (within 2 hours).

**Step 1 — Stop active jobs** (2 minutes):
```bash
ssh awank@100.70.184.84 "pkill -f uvicorn; pkill -f 'python.*zim'"
```

**Step 2 — Identify the pre-merge master commit**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo
git log --oneline | head -10
# Find the commit just before the Phase 5.1 merge commit
```

**Step 3 — Revert the merge commit** (preserves history):
```bash
git revert -m 1 <MERGE_COMMIT_SHA>
git push open-repo master
```

**Step 4 — Downgrade staging database** (if migration caused issues):
```bash
ssh awank@100.70.184.84 "cd /opt/open-repo/backend && uv run alembic downgrade 002"
```

**Step 5 — Redeploy pre-rollback code**:
```bash
rsync -av /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend/ \
  awank@100.70.184.84:/opt/open-repo/backend/
ssh awank@100.70.184.84 "cd /opt/open-repo/backend && \
  uv run uvicorn app.main:app --host 127.0.0.1 --port 8080 &"
```

**Step 6 — Verify Phase 4 is stable**:
```bash
ssh awank@100.70.184.84 "curl -s http://127.0.0.1:8080/health"
```

**Estimated rollback duration**: 30–60 minutes.

---

## Deployment Summary

| Phase | Target dates | Duration | Gate metric |
|---|---|---|---|
| Phase 1: Pre-merge verification | May 26–27 | 45–90 min | 51/51 ZIM tests pass; ARM64 wheel confirmed |
| Phase 2: Post-merge validation | May 28–29 | 2–4 hours | Migration 003 clean; 240/240 tests pass; ZIM magic bytes correct |
| Phase 3: Staging deployment | May 29–30 | 3–5 hours + 2hr monitoring | 0 staging errors; export latency <5s; zimcheck passes |
| Phase 4: Production monitoring | May 30–31+ | 2–4 hours + 48hr monitoring | 48-hour zero-error window; health check continuous |

**Gate rule**: Each phase must fully pass before starting the next. No partial passes.
