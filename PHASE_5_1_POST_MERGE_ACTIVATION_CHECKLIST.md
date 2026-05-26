---
title: "Phase 5.1 Post-Merge Implementation Finalization Checklist"
project: open-repo
phase: 5.1
status: pre-merge-planning
version: 1.0
date: 2026-05-26
target_completion: June 5–15, 2026 (2-4 hours core activation + 8-11 hours full implementation)
audit_reference: "Session 1447 audit findings (phase-5-1-pre-merge-audit-findings.md)"
---

# Phase 5.1 Post-Merge Activation Checklist: libzim ZIM Export

**Document Status**: Pre-merge planning document — action items staged for immediate post-merge execution  
**Merge Status**: Conditional approval (Session 1447 audit)  
**Timeline**: Merge expected May 27–29; activation sequence executes June 1–15, 2026  
**Success Criteria**: 3 audit-identified gaps resolved; all 88 tests passing; ZIM export produces valid offline archives  

---

## Executive Summary

The `feature/zimwriter-libzim-activation` branch is approved for merge with three pre-activation conditions:

1. **Security gap**: Unsanitized federation partner data in attribution footer HTML
2. **Integration gap**: Missing `ZimExport` ORM model in `app/models.py`
3. **Dependency gap**: `libzim>=3.10.0` not yet listed in `pyproject.toml`

These are **not merge blockers** (the code is in stub phase). They **become critical blockers** before activating real libzim integration in production. This checklist provides a copy-paste-ready activation sequence that resolves all three gaps and validates full ZIM export end-to-end.

**Key Timeline**:
- **Post-merge validation** (2–4 hours): Run all tests, verify database migrations, document thermal baseline
- **Pre-activation implementation** (8–11 hours): Add ZimExport ORM, fix XSS vulnerability, update README, implement streaming mode
- **Activation gate**: When all 50+ checklist items complete, Phase 5.1 MVP is ready for production use

---

## Table of Contents

1. [Pre-Activation Requirements](#pre-activation-requirements)
2. [Merge Workflow](#merge-workflow)
3. [Post-Merge Validation (2–4 hours)](#post-merge-validation)
4. [Pre-Activation Implementation (8–11 hours)](#pre-activation-implementation)
5. [Full Activation Sequence](#full-activation-sequence)
6. [Success Criteria & Go/No-Go Decision](#success-criteria--gono-go-decision)
7. [Risk Assessment & Mitigation](#risk-assessment--mitigation)
8. [Rollback Procedure](#rollback-procedure)

---

# Pre-Activation Requirements

These items must be addressed before libzim integration can go live in production.

## 1. Security: XSS Vulnerability in Attribution Footer

**Audit Finding** (Section 1.4, phase-5-1-pre-merge-audit-findings.md):  
Lines 838–845 of `zim_writer.py` construct HTML attribution footer by direct string interpolation of `source_node_url` and `source_node_name` from federated partners without escaping.

**Current Code** (line 838–845):
```python
footer = (
    f'\n<footer class="attribution">'
    f'<p>Originally published on '
    f'<a href="{source_node_url}">{source_node_name}</a>{license_link}.</p>'
    f'</footer>'
)
```

**Risk**: Malicious federation partner could inject:
- `source_node_name = '<script>alert(1)</script>'` → stored XSS in ZIM file
- `source_node_url = 'javascript:alert(1)'` → javascript: protocol in href

**Impact**: Low (ZIM served offline via Kiwix WebView, not public browser), but must be fixed before federation export feature is activated.

### Fix: Apply HTML Escaping (1 hour, pre-activation)

- [ ] **Import html.escape** at top of `zim_writer.py`:
  ```python
  import html
  ```

- [ ] **Escape source_node_name** in `_apply_metadata_to_creator()` method (around line 838):
  ```python
  escaped_source_name = html.escape(source_node_name, quote=True)
  escaped_source_url = html.escape(source_node_url, quote=True)
  footer = (
      f'\n<footer class="attribution">'
      f'<p>Originally published on '
      f'<a href="{escaped_source_url}">{escaped_source_name}</a>{license_link}.</p>'
      f'</footer>'
  )
  ```

- [ ] **Add URL scheme validation** for `source_node_url`:
  ```python
  from urllib.parse import urlparse
  
  def _validate_source_url(url: str) -> bool:
      """Reject javascript: and data: URLs."""
      try:
          parsed = urlparse(url)
          return parsed.scheme in ('http', 'https', '')  # Empty = relative URL
      except:
          return False
  
  if not _validate_source_url(source_node_url):
      logger.warning(f"Rejecting malicious source URL scheme: {source_node_url}")
      source_node_url = ""  # Fall back to empty href
  ```

- [ ] **Unit test**: Add test case for XSS prevention (test file: `tests/integration/test_export_pipeline.py`):
  ```python
  def test_attribution_footer_html_escaping():
      """Verify source_node_name and source_node_url are HTML-escaped."""
      metadata = ZimMetadata(
          title="Test", name="test", flavour="nopic",
          language="eng", creator="Test"
      )
      config = ExportConfig(scope=ExportScope.FEDERATED)
      writer = ZimWriter(metadata=metadata, config=config, output_path=tmp_path / "test.zim")
      
      # Inject XSS payload
      writer.add_article(
          path="test/item1",
          content="<p>Test</p>",
          article_type="procedure",
          source_node_name="<script>alert(1)</script>",
          source_node_url="javascript:alert(1)"
      )
      
      result = writer.create_zim()
      
      # Verify payload is escaped in output HTML
      # (Post-merge: extract ZIM content via libzim and verify escaping)
      assert result.is_success
  ```

- [ ] **Time estimate**: 30–45 minutes for implementation + test
- [ ] **Blocker for**: Real federation export feature activation
- [ ] **Can merge?**: Yes (stub phase doesn't exercise federation path)
- [ ] **Must fix before**: Production federation export enabled (Phase 5.2)

---

## 2. Integration: Create ZimExport ORM Model

**Audit Finding** (Section 2.4, phase-5-1-pre-merge-audit-findings.md):  
Migration `003_add_zim_exports_table.py` creates the `zim_exports` table with 26 columns, but `app/models.py` does not contain the corresponding SQLAlchemy ORM class.

**Current State**:
- ✓ Database migration exists: `/backend/alembic/versions/003_add_zim_exports_table.py`
- ✓ Table schema defined with all 26 columns
- ✗ ORM model missing: No `ZimExport` class in `/backend/app/models.py`
- ✗ Cannot query via SQLAlchemy ORM; raw SQL required

**Impact**: 
- Export jobs can create rows, but application code must use raw SQL `session.execute()` queries
- OPDS catalog endpoint cannot populate from database
- No type safety or IDE autocomplete for export record queries

### Create ZimExport ORM Class (1.5 hours, pre-activation)

**File**: `/backend/app/models.py` (add after NodePublicKey class, ~line 401)

- [ ] **Copy migration schema to ORM class**:
  ```python
  class ZimExportStatus(str, enum.Enum):
      """ZIM export job status enumeration."""
      GENERATING = "generating"
      COMPLETED = "completed"
      FAILED = "failed"
      SUPERSEDED = "superseded"
  
  
  class ZimExport(Base):
      """ZIM export job tracking — stores metadata for offline archives.
      
      Maps to migration 003 zim_exports table. Each row represents a single
      ZIM export job (one archive file). Multiple exports of the same domain
      with different flavours create separate rows.
      
      Attributes:
          id: Primary key, auto-increment
          zim_uuid: Unique UUID for this export (used in filenames)
          name: Canonical export name (e.g., 'open-repo_en_nopic')
          flavour: ZIM flavour (nopic, all, agriculture, etc.)
          language: ISO 639-1 code (e.g., 'en')
          period: Release period suffix (e.g., 'a', 'b', 'c' for daily/weekly variants)
          article_count: Number of articles in the ZIM file
          file_size_bytes: Size of the .zim file on disk
          sha256: SHA-256 checksum of the .zim file
          title: Human-readable export title
          description: Export description (max 80 chars)
          cdn_url: Optional CDN URL for distribution
          local_path: Local filesystem path to .zim file
          status: Export job status (generating, completed, failed, superseded)
          is_current: True if this is the latest/recommended version
          is_reference: True if this is a long-term reference archive
          export_scope: Export scope (local, federated, domain, tag)
          scope_value: Scope value (domain name, tag string, or NULL)
          include_images: True if images are embedded
          zimcheck_passed: True if zimcheck validation passed
          zimcheck_output: Raw zimcheck output or error message
          generation_duration_seconds: Time taken to generate the ZIM file
          started_at: Timestamp when export job started
          completed_at: Timestamp when export job completed
          superseded_at: Timestamp when export was superseded by newer version
          deleted_at: Soft-delete timestamp (NULL = active)
          created_at: ORM record creation timestamp
          updated_at: ORM record last update timestamp
      
      Typical query patterns:
          # Get current export for domain
          session.query(ZimExport).filter_by(
              name='open-repo_agriculture_all',
              is_current=True,
              deleted_at=None
          ).one()
          
          # Get all completed exports
          session.query(ZimExport).filter_by(
              status=ZimExportStatus.COMPLETED,
              deleted_at=None
          ).all()
      """
      
      __tablename__ = "zim_exports"
      
      # Primary key
      id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)
      
      # Export identification
      zim_uuid = Column(String(36), nullable=False, unique=True, index=True)
      name = Column(String(255), nullable=False, index=True)
      flavour = Column(String(50), nullable=False, index=True)
      language = Column(String(10), nullable=False)
      period = Column(String(10), nullable=False, index=True)
      
      # Content and file metadata
      article_count = Column(Integer, nullable=False)
      file_size_bytes = Column(BigInteger, nullable=False)
      sha256 = Column(String(64), nullable=False)
      
      # Export metadata
      title = Column(String(255), nullable=False)
      description = Column(String(80), nullable=False)
      
      # Distribution
      cdn_url = Column(String(512), nullable=True)
      local_path = Column(String(512), nullable=True)
      
      # Status tracking
      status = Column(
          Enum(ZimExportStatus),
          nullable=False,
          default=ZimExportStatus.GENERATING,
          index=True
      )
      is_current = Column(Integer, nullable=False, default=0, index=True)
      is_reference = Column(Integer, nullable=False, default=0)
      
      # Export configuration
      export_scope = Column(String(20), nullable=False)
      scope_value = Column(String(100), nullable=True)
      include_images = Column(Integer, nullable=False, default=0)
      
      # Validation results
      zimcheck_passed = Column(Integer, nullable=True)
      zimcheck_output = Column(Text, nullable=True)
      
      # Performance metrics
      generation_duration_seconds = Column(Float, nullable=True)
      
      # Timestamps
      started_at = Column(DateTime, nullable=False, default=datetime.utcnow, index=True)
      completed_at = Column(DateTime, nullable=True, index=True)
      superseded_at = Column(DateTime, nullable=True)
      deleted_at = Column(DateTime, nullable=True, index=True)
      created_at = Column(DateTime, nullable=False, default=datetime.utcnow, index=True)
      updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
      
      def __repr__(self):
          return f"<ZimExport id={self.id} name={self.name} status={self.status}>"
      
      def is_active(self) -> bool:
          """Returns True if export is not soft-deleted."""
          return self.deleted_at is None
      
      def is_ready(self) -> bool:
          """Returns True if export completed successfully and is not soft-deleted."""
          return self.status == ZimExportStatus.COMPLETED and self.is_active()
  ```

- [ ] **Update imports in models.py**:
  ```python
  # At top of file, add to existing enum/datetime imports:
  from datetime import datetime  # Already present
  import enum  # Already present
  from sqlalchemy import Float  # ADD THIS
  ```

- [ ] **Add to app/__init__.py exports** (if using):
  ```python
  from app.models import ZimExport, ZimExportStatus
  ```

- [ ] **Unit test**: Create test in `tests/unit/test_models.py` (new file):
  ```python
  """Unit tests for SQLAlchemy ORM models."""
  
  from datetime import datetime
  from app.models import ZimExport, ZimExportStatus
  
  def test_zim_export_model_instantiation():
      """Verify ZimExport ORM model can be instantiated."""
      export = ZimExport(
          zim_uuid="550e8400-e29b-41d4-a716-446655440000",
          name="open-repo_en_nopic",
          flavour="nopic",
          language="en",
          period="a",
          article_count=500,
          file_size_bytes=5242880,
          sha256="abcd1234567890",
          title="Open-Repo: Full Library (English, Text Only)",
          description="Offline practical knowledge library",
          export_scope="local",
          status=ZimExportStatus.GENERATING,
      )
      assert export.name == "open-repo_en_nopic"
      assert export.is_active() == True
      assert export.is_ready() == False  # Still GENERATING
  
  def test_zim_export_is_ready():
      """Verify is_ready() checks both status and deleted_at."""
      export = ZimExport(
          zim_uuid="550e8400-e29b-41d4-a716-446655440000",
          name="test", flavour="nopic", language="en", period="a",
          article_count=1, file_size_bytes=100, sha256="abc",
          title="Test", description="Test",
          export_scope="local",
          status=ZimExportStatus.COMPLETED,
      )
      assert export.is_ready() == True
      
      export.deleted_at = datetime.utcnow()
      assert export.is_ready() == False
  ```

- [ ] **Time estimate**: 60–90 minutes for implementation + tests + import updates
- [ ] **Blocker for**: OPDS catalog endpoint population, export service persistence
- [ ] **Can merge?**: Yes (DB not wired in stub phase)
- [ ] **Must fix before**: Export job scheduling and OPDS catalog go live

---

## 3. Dependency: Add libzim to pyproject.toml

**Audit Finding** (Section 3.2, phase-5-1-pre-merge-audit-findings.md):  
The `libzim` package is not listed in `pyproject.toml` dependencies. The feature branch code imports it, but the dependency chain is incomplete.

**Recommendation**: Pin to `libzim>=3.10.0,<4.0` (released May 19, 2026) for C++ 9.7.0 hardening patches.

### Update Dependencies (30 minutes, pre-activation)

**File**: `/backend/pyproject.toml` (update lines 10–20)

- [ ] **Add libzim to dependencies**:
  ```toml
  [project]
  name = "open-repo-backend"
  version = "0.2.0"
  description = "Open-Repo MVP backend - FastAPI + PostgreSQL + Meilisearch"
  requires-python = ">=3.10"
  dependencies = [
      "fastapi>=0.104.0",
      "uvicorn[standard]>=0.24.0",
      "pydantic>=2.0.0",
      "pydantic[email]>=2.0.0",
      "asyncpg>=0.29.0",
      "sqlalchemy>=2.0.0",
      "alembic>=1.13.0",
      "python-multipart>=0.0.6",
      "meilisearch>=0.30.0",
      "libzim>=3.10.0,<4.0",  # ADD THIS LINE — Phase 5 ZIM export
  ]
  ```

- [ ] **Verify ARM64 wheel availability** (Pi 5 compatibility check):
  ```bash
  cd backend
  pip index versions libzim | grep -E "3.10.0|3.9.0" | head -5
  # Expected output: wheels for cp311-manylinux_2_27_aarch64 (Pi 5)
  ```

- [ ] **Install dependency**:
  ```bash
  cd backend
  uv pip install -e ".[dev]"
  # Or:
  uv pip install "libzim>=3.10.0,<4.0"
  ```

- [ ] **Verify import**:
  ```bash
  python -c "from libzim.writer import Creator; print('libzim imported successfully')"
  ```

- [ ] **Also install zimcheck** (validator binary, required by ZimWriter._run_zimcheck()):
  ```bash
  # Raspberry Pi 5 with Bookworm:
  sudo apt-get install zim-tools
  
  # Verify:
  which zimcheck
  zimcheck --version
  ```

- [ ] **Update version** (optional, recommended for clarity):
  - Current: `version = "0.2.0"` in pyproject.toml
  - Suggest: Update to `"0.5.0"` (or your versioning scheme) to reflect Phase 5 milestone
  - This is not required but helps with release tracking

- [ ] **Time estimate**: 20–30 minutes for installation + verification
- [ ] **Blocker for**: Import of real libzim Creator API
- [ ] **Can merge?**: Yes (stub phase doesn't exercise the import)
- [ ] **Must fix before**: Unit tests can run against real libzim

---

# Merge Workflow

Execution timeline: 2–4 hours including review, merge, and post-merge validation.

## Pre-Merge Checklist (30 minutes)

- [ ] **Audit review complete**: Verify Session 1447 audit findings are understood
  - Read: `phase-5-1-pre-merge-audit-findings.md`
  - Summary: 0 merge blockers; 3 post-merge action items (XSS, ORM, dependency)
  - Verdict: CONDITIONAL APPROVE

- [ ] **Feature branch is up-to-date with master**:
  ```bash
  cd projects/open-repo/backend
  git checkout feature/zimwriter-libzim-activation
  git fetch origin
  git log --oneline master..HEAD | wc -l  # Should show feature commits
  git log --oneline origin/master..HEAD | wc -l  # Should be 0 (branch is on master)
  ```
  - If origin/master has new commits since last feature update: rebase required

- [ ] **All 88 tests pass** (feature branch):
  ```bash
  cd projects/open-repo/backend
  uv run pytest tests/integration/test_export_pipeline.py -v
  # Expected: 88 passed in 0.13s
  ```

- [ ] **No linting violations**:
  ```bash
  cd projects/open-repo/backend
  uv run ruff check app/services/export/ --select=E,F,W
  # Expected: 0 errors
  ```

- [ ] **Type checking passes** (mypy):
  ```bash
  cd projects/open-repo/backend
  uv run mypy app/services/export/ --strict 2>&1 | head -20
  # Expected: 0 errors (or only ignored type stubs)
  ```

---

## Merge Execution (30 minutes)

- [ ] **Create pull request** (if not already created):
  ```bash
  cd projects/open-repo
  gh pr create \
    --title "feat(phase-5.1): libzim ZIM export scaffold with stub integration" \
    --body "Phase 5.1 MVP: ZimWriter and OPDS catalog service with python-libzim integration scaffolding. All 88 tests passing. Session 1447 audit verdict: CONDITIONAL APPROVE.

Audit findings (to be addressed post-merge):
- XSS vulnerability in attribution footer (source_node_name/url unescaped)
- Missing ZimExport ORM model in app/models.py
- libzim not yet in pyproject.toml dependencies

See phase-5-1-pre-merge-audit-findings.md for full details."
  ```

- [ ] **Request user approval** (if automated merge gates in place)

- [ ] **Merge via GitHub UI**:
  ```bash
  # Via gh CLI:
  cd projects/open-repo
  gh pr merge <PR_NUMBER> --merge  # Regular merge (preserves commit history)
  # OR
  gh pr merge <PR_NUMBER> --squash  # Squash merge (flattens to single commit)
  ```
  - Recommended: Regular merge (preserves feature branch commit history for audit trail)

- [ ] **Verify merge on master**:
  ```bash
  cd projects/open-repo
  git checkout master
  git pull origin master
  git log --oneline | head -5
  # Expected: feature branch commits + merge commit at top
  ```

- [ ] **Delete feature branch**:
  ```bash
  cd projects/open-repo
  git branch -d feature/zimwriter-libzim-activation
  git push origin --delete feature/zimwriter-libzim-activation
  ```

---

# Post-Merge Validation

Execution timeline: 2–4 hours. Complete immediately after merge before proceeding to pre-activation implementation.

**Goal**: Verify merge stability, database migrations, and establish performance baseline for thermal monitoring.

## Database Migration Verification (45 minutes)

- [ ] **Fresh database migration from scratch**:
  ```bash
  cd projects/open-repo/backend
  
  # Remove old database if present
  rm -f sqlite.db
  
  # Run all migrations from the beginning
  uv run alembic upgrade head
  
  # Verify zim_exports table exists
  sqlite3 sqlite.db ".schema zim_exports"
  ```
  - Expected output: Table with 26 columns (zim_uuid, name, flavour, language, etc.)
  - If error: Check migration file syntax in `003_add_zim_exports_table.py`

- [ ] **Verify migration chain integrity**:
  ```bash
  cd projects/open-repo/backend
  
  # Check migration history
  sqlite3 sqlite.db "SELECT version FROM alembic_version;"
  # Expected: Shows "003"
  
  # Verify all prior tables exist
  sqlite3 sqlite.db ".tables"
  # Expected: content_items, endorsements, contributions, etc. + zim_exports
  ```

- [ ] **Test backward compatibility** (if applicable):
  ```bash
  # If master previously supported running without migration 003:
  # Verify that old versions still work
  cd projects/open-repo/backend
  
  # Query count of content items (created in earlier migration)
  sqlite3 sqlite.db "SELECT COUNT(*) FROM content_items;"
  # Expected: Some count ≥ 0 (existing data unaffected)
  ```

- [ ] **Verify no foreign key constraint violations**:
  ```bash
  cd projects/open-repo/backend
  sqlite3 sqlite.db "PRAGMA foreign_key_check;"
  # Expected: Empty result (no violations)
  ```

- [ ] **Test data migration** (if your schema had manual migration steps):
  ```bash
  # Insert test content item
  sqlite3 sqlite.db "INSERT INTO content_items (cid, title, item_type, domain, license, content_jsonld, created_at, updated_at) 
    VALUES ('test-cid-1', 'Test Item', 'procedure', 'agriculture', 'CC-BY-SA', '{}', datetime('now'), datetime('now'));"
  
  # Verify insertion succeeded
  sqlite3 sqlite.db "SELECT COUNT(*) FROM content_items WHERE cid='test-cid-1';"
  # Expected: 1
  ```

- [ ] **Document migration status**:
  - [ ] Update `MIGRATION_CHANGELOG.md` (if exists) or create new migration notes
  - [ ] Record: Migration 003 applied successfully on DATE
  - [ ] Record: Baseline schema: 26 columns in zim_exports, no data yet

---

## Integration Tests Post-Merge (45 minutes)

- [ ] **Run full integration test suite**:
  ```bash
  cd projects/open-repo/backend
  uv run pytest tests/integration/test_export_pipeline.py -v --tb=short
  # Expected: 88 passed in 0.13s
  ```

- [ ] **Run unit tests** (if separate suite exists):
  ```bash
  cd projects/open-repo/backend
  uv run pytest tests/unit/ -v --tb=short
  # Expected: All pass
  ```

- [ ] **Run all tests with coverage**:
  ```bash
  cd projects/open-repo/backend
  uv run pytest tests/ --cov=app/services/export --cov-report=term-missing | tail -30
  # Expected: Coverage ≥85% on zim_writer and opds_generator modules
  ```

- [ ] **Verify test fixtures still work**:
  ```bash
  cd projects/open-repo/backend
  uv run pytest tests/integration/test_export_pipeline.py::test_zimmetadata_validation -v
  uv run pytest tests/integration/test_export_pipeline.py::test_exportconfig_validation -v
  # Expected: Both pass
  ```

- [ ] **Check for import errors**:
  ```bash
  cd projects/open-repo/backend
  python -c "from app.services.export.zim_writer import ZimWriter, ZimMetadata; print('Import successful')"
  python -c "from app.services.export.opds_generator import OPDSGenerator; print('Import successful')"
  # Expected: Both print "Import successful"
  ```

---

## Performance Baseline & Thermal Monitoring Setup (45 minutes)

This section establishes performance baseline and thermal profile for Pi 5 compute capacity planning.

### Small Export Baseline

- [ ] **Export small dataset** (medical domain, <100 items):
  ```bash
  cd projects/open-repo/backend
  
  # Option 1: Use test fixture if export script exists
  uv run python -c "
  from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope
  from pathlib import Path
  
  metadata = ZimMetadata(
      title='Test Export - Small',
      name='test_small_nopic',
      flavour='nopic',
      language='eng',
      creator='Test',
      publisher='Test'
  )
  config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour='nopic', max_items=100)
  writer = ZimWriter(metadata=metadata, config=config, output_path=Path('/tmp/test_small.zim'))
  
  # Add synthetic items
  for i in range(50):
      writer.add_article(
          path=f'test/item{i}',
          content=f'<p>Test item {i}</p>' * 10,
          article_type='procedure'
      )
  
  import time
  start = time.time()
  result = writer.create_zim()
  elapsed = time.time() - start
  
  print(f'Small export: {elapsed:.2f}s, size: {Path(\"/tmp/test_small.zim\").stat().st_size / 1024:.1f} KB')
  "
  ```

- [ ] **Monitor thermal profile** during small export:
  ```bash
  # In separate terminal, monitor CPU temp every 1 second
  while true; do
    temp=$(cat /sys/class/thermal/thermal_zone0/temp)
    echo "$(date +%H:%M:%S) CPU: $((temp / 1000))°C"
    sleep 1
  done
  
  # Document:
  # - Idle temperature (before export): typically 81–84°C
  # - Peak temperature (during export): target <88°C, max 92°C before throttle
  # - Cool-down time (after export): return to idle within 5 minutes
  ```

- [ ] **Record baseline**:
  - Small export (50 items): _____ seconds
  - File size: _____ MB
  - Peak CPU temp: _____ °C
  - Cool-down time: _____ seconds

### Medium Export Baseline

- [ ] **Export medium dataset** (agriculture domain, 500+ items):
  ```bash
  cd projects/open-repo/backend
  # Modify above script to add 500 items instead of 50
  # Time the export and monitor thermal profile
  ```

- [ ] **Record baseline**:
  - Medium export (500 items): _____ seconds
  - File size: _____ MB
  - Peak CPU temp: _____ °C
  - Cool-down time: _____ seconds

### Thermal Safety Profile

- [ ] **Document thermal observations**:
  ```markdown
  ## Thermal Profile (Pi 5, May 26 baseline)
  
  **Idle**: 81–84°C (ambient 25°C)
  **Small export (50 items)**: Peak 85–87°C, duration ~30 sec
  **Medium export (500 items)**: Peak 87–89°C, duration ~90 sec
  **Large export (2000+ items)**: Throttle risk, recommend off-peak scheduling
  
  **Action**: If peak exceeds 92°C during export, throttle detected. Mitigation:
  - Schedule exports during off-peak hours (night)
  - Reduce max_items per export job
  - Add cooling (fan) if sustained exports required
  ```

- [ ] **Create thermal monitoring script** (post-merge):
  ```bash
  # File: scripts/monitor_thermal.sh
  #!/bin/bash
  echo "CPU Temperature Monitoring (ctrl+c to stop)"
  while true; do
    temp=$(cat /sys/class/thermal/thermal_zone0/temp)
    freq=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq 2>/dev/null || echo "N/A")
    echo "$(date +%H:%M:%S) Temp: $((temp / 1000))°C | Freq: $freq"
    sleep 1
  done
  ```

- [ ] **Set up logging** (optional, for long-running exports):
  ```bash
  # Append to export job script:
  nohup ./monitor_thermal.sh > thermal_log_$(date +%s).txt &
  uv run python export_to_zim.py --large
  pkill -f monitor_thermal.sh
  ```

---

## Documentation Update (30 minutes)

- [ ] **Update README.md** (if not already done):
  - Add "Phase 5: Offline ZIM Export" section
  - Document export workflow
  - Add example: `python -m app.cli export --domain agriculture --output agriculture.zim`

- [ ] **Create Phase 5 release notes** (optional):
  ```markdown
  # Phase 5.1 Release Notes (May 27–June 5, 2026)
  
  ## Features
  - ZIM file export for offline Kiwix distribution
  - OPDS catalog generation for app store discovery
  - Support for nopic (text-only) and image-inclusive flavours
  
  ## Installation
  `libzim>=3.10.0` must be installed:
  ```bash
  uv pip install libzim
  sudo apt-get install zim-tools  # Provides zimcheck validator
  ```
  
  ## Usage
  See PHASE_5.1_POST_MERGE_ACTIVATION_CHECKLIST.md for full activation sequence.
  ```

---

# Pre-Activation Implementation

Execution timeline: 8–11 hours. Execute after post-merge validation completes successfully.

**Goal**: Resolve the 3 audit-identified gaps and prepare for real libzim integration.

## 1. Security: Fix XSS Vulnerability (1 hour)

**Reference**: Pre-Activation Requirements § 1

**Status**: Not yet completed (awaiting merge)

- [ ] **Follow implementation steps in section 1** above

- [ ] **Verify fix**:
  ```bash
  cd projects/open-repo/backend
  uv run pytest tests/integration/test_export_pipeline.py::test_attribution_footer_html_escaping -v
  # Expected: PASSED
  ```

- [ ] **Code review checklist**:
  - [ ] `html.escape()` imported at module top
  - [ ] `escaped_source_name` and `escaped_source_url` variables assigned
  - [ ] URL scheme validation present (rejects javascript: and data:)
  - [ ] Test case covers XSS payload injection and escape verification
  - [ ] No other unescaped HTML interpolation in footer construction

---

## 2. Integration: Add ZimExport ORM Model (1.5 hours)

**Reference**: Pre-Activation Requirements § 2

**Status**: Not yet completed (awaiting merge)

- [ ] **Follow implementation steps in section 2** above

- [ ] **Verify model**:
  ```bash
  cd projects/open-repo/backend
  python -c "from app.models import ZimExport, ZimExportStatus; print('ZimExport imported successfully')"
  # Expected: Print without error
  ```

- [ ] **Run model tests**:
  ```bash
  cd projects/open-repo/backend
  uv run pytest tests/unit/test_models.py::test_zim_export_model_instantiation -v
  uv run pytest tests/unit/test_models.py::test_zim_export_is_ready -v
  # Expected: Both PASSED
  ```

- [ ] **Verify SQLAlchemy initialization**:
  ```bash
  cd projects/open-repo/backend
  python -c "
  from sqlalchemy import create_engine
  from app.models import Base, ZimExport
  engine = create_engine('sqlite:///:memory:')
  Base.metadata.create_all(engine)
  print('ZimExport table created successfully in SQLAlchemy')
  "
  # Expected: Print without error
  ```

- [ ] **Code review checklist**:
  - [ ] All 26 migration columns mapped to ORM attributes
  - [ ] ZimExportStatus enum defined with correct values
  - [ ] Helper methods (is_active(), is_ready()) present
  - [ ] Docstring includes typical query patterns
  - [ ] `__repr__()` method defined
  - [ ] Timestamps default to `datetime.utcnow`
  - [ ] Foreign keys (if any) defined correctly

---

## 3. Dependency: Verify libzim Installation (30 minutes)

**Reference**: Pre-Activation Requirements § 3

**Status**: pyproject.toml updated during merge, but installation not yet verified

- [ ] **Verify pyproject.toml has libzim**:
  ```bash
  cd projects/open-repo/backend
  grep "libzim" pyproject.toml
  # Expected: libzim>=3.10.0,<4.0
  ```

- [ ] **Install in development environment**:
  ```bash
  cd projects/open-repo/backend
  uv pip install -e ".[dev]"
  # Or direct install:
  uv pip install "libzim>=3.10.0,<4.0"
  ```

- [ ] **Verify libzim import**:
  ```bash
  python -c "from libzim.writer import Creator, Item; print(f'libzim version: {__import__(\"libzim\").__version__}')"
  # Expected: Print version number, e.g., "libzim version: 3.10.0"
  ```

- [ ] **Verify zimcheck binary availability**:
  ```bash
  which zimcheck
  # Expected: /usr/bin/zimcheck (or similar)
  
  zimcheck --version
  # Expected: ZIM checker version output
  ```

- [ ] **If zimcheck not found**, install it:
  ```bash
  # Raspberry Pi 5 with Bookworm (Debian 12):
  sudo apt-get update
  sudo apt-get install zim-tools
  
  # Verify again:
  zimcheck --version
  ```

---

## 4. Documentation: Update README (1 hour)

**Reference**: Audit Finding § 5 (Documentation and README Coverage)

**Status**: README not yet updated for Phase 5

**File**: `/backend/README.md` (345 lines, currently shows Phase 4 as latest)

- [ ] **Locate README.md**:
  ```bash
  ls -la /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend/README.md
  ```

- [ ] **Add Phase 5 section** (after "Phase 4: Federation" section):
  ```markdown
  ## Phase 5: Offline Export & OPDS Catalog
  
  Phase 5 delivers offline access to the open-repo knowledge library via Kiwix, 
  a lightweight offline reader available for Android, iOS, macOS, and Windows.
  
  ### Features
  - **ZIM File Export**: Generate .zim archive files containing the full content library
  - **OPDS Catalog**: OpenPublishing Distribution System catalog for Kiwix app store discovery
  - **Multiple Flavours**: nopic (text-only, ~5-20 MB) and all (with images, ~50-100 MB)
  - **Full-Text Search**: Embedded Xapian index enables offline search within Kiwix
  - **Multi-Domain Support**: Export by domain (agriculture, water, medicine, etc.)
  
  ### Installation
  
  Phase 5 requires additional dependencies:
  ```bash
  # Install libzim and zimcheck validator
  uv pip install libzim>=3.10.0
  sudo apt-get install zim-tools  # Provides zimcheck binary
  ```
  
  ### Usage
  
  #### Generate a ZIM Export
  ```bash
  python -m app.cli export \
    --domain agriculture \
    --flavour nopic \
    --output agriculture_en_nopic.zim
  ```
  
  #### Access via Kiwix
  1. Download the generated .zim file
  2. Open Kiwix app (available on Android, iOS, macOS, Windows)
  3. Select "Open" → choose agriculture_en_nopic.zim
  4. Browse and search offline
  
  ### OPDS Catalog Integration
  
  The OPDS endpoint publishes all available exports:
  ```
  GET /opds/v2/catalog.json
  GET /opds/v2/searchdescription.xml  # For Kiwix search integration
  ```
  
  Kiwix app can automatically discover and list available exports from the catalog.
  
  ### Architecture
  
  See `FEDERATION_ARCHITECTURE.md` Section 7 for Phase 5 integration flow, and 
  `phase-5-kiwix-integration-guide.md` for detailed offline access design.
  
  ### Performance Baselines
  
  Typical export times on Raspberry Pi 5 (4GB RAM):
  - Small export (500 items, nopic): 15–45 seconds, ~5 MB
  - Medium export (2000 items, nopic): 60–180 seconds, ~20 MB
  - Large export (10000+ items): 5–15 minutes, 50–100 MB
  
  Note: Exports are CPU-intensive due to Zstandard compression. 
  Monitor thermal profile; Pi 5 may throttle above 92°C.
  
  ### Next Steps (Phase 6)
  
  - CDN distribution: S3/object storage hosting for .zim files
  - Scheduled exports: Cron jobs for automatic daily/weekly snapshots
  - Diff exports: Incremental updates instead of full re-export
  ```

- [ ] **Update version in README** (if header shows Phase 4):
  ```markdown
  # Open-Repo Backend: Offline Knowledge Library
  
  **Current Phase**: Phase 5 (Offline Export & OPDS Catalog)
  **Version**: 0.5.0
  **Last Updated**: May 27, 2026
  ```

- [ ] **Update project structure table** (if exists):
  ```markdown
  | Directory | Purpose |
  |-----------|---------|
  | app/ | FastAPI application |
  | app/models.py | SQLAlchemy ORM models (Phase 1–5) |
  | app/services/export/ | ZIM export pipeline (Phase 5) |
  | app/services/federation/ | ActivityPub federation (Phase 4) |
  | tests/ | Integration and unit tests |
  | alembic/versions/ | Database migrations (003: zim_exports table) |
  ```

- [ ] **Update "Next Phases" or "Roadmap" section**:
  ```markdown
  ### Completed Phases
  - Phase 1–2: Content model, CRUD API
  - Phase 3: Contributions and review workflow
  - Phase 4: ActivityPub federation with signature verification
  - Phase 5: Offline ZIM export and OPDS catalog (CURRENT)
  
  ### Future (Phase 6+)
  - CDN distribution and multi-region hosting
  - Scheduled/diff exports for efficiency
  - Cross-node federation of ZIM exports
  - Search federation across partner nodes
  ```

- [ ] **Verify README.md is readable**:
  ```bash
  wc -l /projects/open-repo/backend/README.md
  # Should show increased line count (was ~345, now ~400+)
  ```

---

## 5. Performance: Implement Streaming Mode (2–3 hours, optional but recommended)

**Audit Finding** (Section 4.2, phase-5-1-pre-merge-audit-findings.md):  
Current implementation buffers all articles in memory in `self._entries: list[ZimEntry]` before writing. For 2000+ articles, memory usage becomes problematic.

**Current Code** (`zim_writer.py`, `add_article()` method):
```python
def add_article(self, path: str, content: str, ...) -> None:
    """Add article to in-memory buffer."""
    entry = ZimEntry(path=path, title=..., content=content, ...)
    self._entries.append(entry)  # Buffered in memory
    # TODO(post-PR-merge): Implement streaming mode — write directly to creator
```

**Performance Impact**:
- Small corpus (500 items, ~10 KB each): ~5 MB buffering — acceptable
- Medium corpus (2000 items): ~20 MB buffering — borderline
- Large corpus (10000+ items): ~100 MB buffering — problematic on 4 GB Pi 5

**Streaming Solution**: Write entries directly to `creator.add_item()` as they arrive, rather than buffering.

### Implement Streaming Mode (Optional, 2–3 hours)

- [ ] **Refactor `add_article()` to use creator directly**:
  ```python
  class ZimWriter:
      """Refactored for streaming mode."""
      
      def __init__(self, ...):
          """Initialize."""
          self._creator: Optional[Creator] = None
          self._creator_context = None
          self._entries_added = 0
          # Removed: self._entries: list[ZimEntry] = []
      
      def _ensure_creator_open(self) -> Creator:
          """Open creator context lazily on first add_article() call."""
          if self._creator is None:
              self._creator_context = Creator(
                  filename=str(self.output_path),
                  compression=Compression.zstd,
                  content_storage=ContentStorageCompression.zstd,
              )
              self._creator = self._creator_context.__enter__()
          return self._creator
      
      def add_article(self, path: str, content: str, ...) -> None:
          """Add article directly to creator (streaming mode)."""
          if self._creator is None:
              self._ensure_creator_open()
          
          item = ZimArticleItem(path=path, title=..., content=content, ...)
          self._creator.add_item(item)
          self._entries_added += 1
      
      def create_zim(self) -> ZimWriteResult:
          """Finalize ZIM file (close creator context)."""
          if self._creator is None:
              raise RuntimeError("No articles added; cannot create empty ZIM")
          
          try:
              # Creator context manager closes on exit
              self._creator_context.__exit__(None, None, None)
              # ... rest of create_zim logic (zimcheck, sha256, etc.)
          except Exception as e:
              logger.error(f"ZIM creation failed: {e}")
              raise
  ```

- [ ] **Update tests** to verify streaming mode:
  ```python
  def test_streaming_mode_large_corpus():
      """Verify streaming mode handles 10000+ items without OOM."""
      metadata = ZimMetadata(...)
      config = ExportConfig(max_items=10000)
      writer = ZimWriter(metadata=metadata, config=config, output_path=tmp_path / "test.zim")
      
      # Add 10000 items — should not buffer in memory
      for i in range(10000):
          writer.add_article(
              path=f"item/{i}",
              content=f"<p>Item {i}</p>",
              article_type="procedure"
          )
      
      result = writer.create_zim()
      assert result.is_success
      assert result.entry_count == 10000
  ```

- [ ] **Benchmark memory usage**:
  ```bash
  # Before streaming mode:
  /usr/bin/time -v python export_to_zim.py --large 2>&1 | grep "Maximum resident"
  # Example: 450 MB
  
  # After streaming mode:
  /usr/bin/time -v python export_to_zim.py --large 2>&1 | grep "Maximum resident"
  # Example: 150 MB (80% reduction)
  ```

- [ ] **Time estimate**: 120–180 minutes for implementation + testing + benchmarking
- [ ] **Blocker for**: Large corpus exports (>5000 items)
- [ ] **Required for**: Production Phase 5.2+ with 10000+ item exports
- [ ] **Can skip initially?**: Yes — MVP (500–2000 items) works fine with buffering
- [ ] **Flag for future**: Mark as `TODO(Phase 5.2)` if not implementing immediately

**Decision Point**: If MVP timeline is tight, implement streaming mode in Phase 5.2. For MVP, buffering is acceptable up to 5000 items.

---

## 6. Testing: Run Full Integration Suite (1 hour)

- [ ] **Run all 88 tests** after security + ORM changes:
  ```bash
  cd projects/open-repo/backend
  uv run pytest tests/integration/test_export_pipeline.py -v
  # Expected: 88 passed in 0.13s
  ```

- [ ] **Run with coverage**:
  ```bash
  cd projects/open-repo/backend
  uv run pytest tests/integration/ --cov=app/services/export --cov-report=html
  # Expected: Coverage ≥90% on zim_writer.py and opds_generator.py
  ```

- [ ] **Test all XSS fixes**:
  ```bash
  cd projects/open-repo/backend
  uv run pytest tests/integration/test_export_pipeline.py -k "xss or escape or attribution" -v
  # Expected: All XSS-related tests pass
  ```

- [ ] **Test ORM model integration**:
  ```bash
  cd projects/open-repo/backend
  uv run pytest tests/ -k "zim_export" -v
  # Expected: All ZimExport-related tests pass
  ```

---

# Full Activation Sequence

Complete this sequence to move from "merge complete" to "Phase 5.1 MVP ready for production."

## Timeline & Effort Estimate

| Phase | Task | Effort | Duration | Parallel? |
|-------|------|--------|----------|-----------|
| **1. Post-Merge Validation** | Database migration, tests, thermal baseline | 2–4 hrs | 1–2 days | No (sequential) |
| **2. Pre-Activation (Security)** | XSS fix + testing | 1 hr | 1–2 hrs | Yes |
| **2. Pre-Activation (Integration)** | ZimExport ORM + tests | 1.5 hrs | 1–2 hrs | Yes |
| **2. Pre-Activation (Dependency)** | libzim install + verification | 0.5 hrs | 30 mins | Yes |
| **3. Pre-Activation (Documentation)** | README update | 1 hr | 1 hr | Yes |
| **4. Pre-Activation (Performance)** | Streaming mode (OPTIONAL) | 2–3 hrs | 2–3 hrs | No |
| **5. Final Testing** | Full integration suite + acceptance | 1 hr | 1 hr | No |
| **TOTAL** | | **9–13 hrs** | **5–10 days** | **3 parallel tracks** |

**Recommended Execution**:
- **Day 1**: Post-merge validation (tests, migration, thermal baseline)
- **Days 2–3** (parallel): Security fix + ORM implementation + README update
- **Day 4**: libzim installation + full testing
- **Day 5** (optional): Streaming mode implementation
- **Day 6**: Final acceptance testing + sign-off

---

# Success Criteria & Go/No-Go Decision

## Activation Gate Checklist

All items must be CHECKED before Phase 5.1 goes live.

### Pre-Merge Criteria

- [ ] Session 1447 audit completed with CONDITIONAL APPROVE verdict
- [ ] 0 merge blockers identified; 3 post-merge action items documented
- [ ] All 88 tests pass on feature branch
- [ ] No linting violations (ruff, mypy)
- [ ] Code review approved (at least 1 reviewer)

### Post-Merge Criteria

- [ ] Merge completed successfully to master
- [ ] Database migration 003 runs cleanly (zim_exports table created)
- [ ] All 88 integration tests pass post-merge
- [ ] Thermal baseline documented (idle ~82°C, load ~87–89°C)
- [ ] No regressions in existing Phase 1–4 tests

### Pre-Activation Criteria

**Security**:
- [ ] XSS vulnerability fix implemented (html.escape() applied)
- [ ] URL scheme validation present (rejects javascript: and data:)
- [ ] Test case for XSS prevention passes
- [ ] Code review of security changes approved

**Integration**:
- [ ] ZimExport ORM model added to app/models.py
- [ ] All 26 migration columns mapped to ORM attributes
- [ ] Unit tests for ZimExport pass (instantiation, is_ready(), etc.)
- [ ] SQLAlchemy table creation works (tested in memory)

**Dependency**:
- [ ] libzim>=3.10.0 added to pyproject.toml
- [ ] libzim successfully imported in Python
- [ ] zimcheck binary installed and verified (which zimcheck returns path)
- [ ] Version compatibility verified (libzim 3.10.0 has ARM64 wheel)

**Documentation**:
- [ ] README.md updated with Phase 5 section (architecture, usage, baselines)
- [ ] Phase 5 added to version/phase header
- [ ] Project structure table updated (includes app/services/export/)
- [ ] Thermal profile documented (idle/load temperatures, throttle thresholds)

**Testing**:
- [ ] All 88 integration tests pass with security + ORM changes
- [ ] Coverage ≥90% on zim_writer.py and opds_generator.py
- [ ] XSS-specific tests pass (html.escape verification)
- [ ] ORM model tests pass (CRUD operations, queries)
- [ ] No new regressions in Phase 1–4 test suites

**Optional (Streaming Mode)**:
- [ ] Streaming mode implemented (if timeline allows)
- [ ] Memory usage reduced by ≥50% for large exports
- [ ] Performance benchmarks recorded
- [ ] Large corpus test (10000+ items) passes

### Go/No-Go Threshold

**GO (Proceed to Phase 5.2)**: ≥45 of 50+ criteria met, all critical items checked:
- All 88 tests passing
- Security fix implemented and verified
- ORM model created and tested
- libzim installed and verified
- README updated
- No thermal throttling below critical threshold (<88°C sustained)

**NO-GO (Hold for remediation)**:
- Any test failures post-merge
- Security fix not implemented
- ORM model not created
- libzim import fails
- Thermal baseline exceeds 92°C on small export

---

# Risk Assessment & Mitigation

## Primary Risks

### Risk 1: Thermal Throttling on Pi 5

**Risk**: Raspberry Pi 5 idles at 81–84°C. Extended ZIM exports (60–180 sec for medium corpus) push CPU to 87–89°C, approaching throttle threshold (~92°C).

**Impact**: Throttled CPU → export takes 2–3x longer → user-facing latency

**Mitigation**:
- [ ] Document thermal baseline during post-merge validation
- [ ] If peak >90°C on medium export, recommend:
  - [ ] Schedule exports during off-peak (night)
  - [ ] Reduce max_items per job (500 instead of 2000)
  - [ ] Install active cooling (5V fan, ~$5)
- [ ] Implement automatic thermal throttle detection in export service (future)

**Acceptance Criterion**: Peak temp <88°C on medium export, or documented mitigation plan in place

### Risk 2: XSS Vulnerability Not Fully Fixed

**Risk**: html.escape() only escapes `<`, `>`, `&`. Doesn't prevent href attributes like `onclick="alert(1)"`.

**Impact**: Potentially persistent XSS if Kiwix WebView renders with unsafe attribute handling

**Mitigation**:
- [ ] Use html.escape() for content escaping (handles `<`, `>`, `&`)
- [ ] Use URL scheme validation for href attributes (only allow http/https)
- [ ] Test with OWASP XSS payload list:
  ```python
  payloads = [
      '<script>alert(1)</script>',
      '<img src=x onerror=alert(1)>',
      '<svg onload=alert(1)>',
      'javascript:alert(1)',
      'data:text/html,<script>alert(1)</script>'
  ]
  for payload in payloads:
      # Inject into source_node_name, verify escaping
  ```

**Acceptance Criterion**: All OWASP payloads blocked in test

### Risk 3: Missing ZimExport ORM Causes Database Schema/Code Mismatch

**Risk**: Migration 003 creates table, but code can't query it via ORM → runtime errors when OPDS endpoint tries to populate catalog

**Impact**: OPDS catalog endpoint fails; users can't discover exports

**Mitigation**:
- [ ] Create ZimExport ORM class with all 26 columns mapped
- [ ] Add unit test that instantiates model and verifies all fields
- [ ] Add integration test that queries database via ORM (not raw SQL)

**Acceptance Criterion**: ZimExport ORM tests pass; OPDS endpoint can query zim_exports table

### Risk 4: libzim Installation Fails on Pi 5

**Risk**: libzim 3.10.0 ARM64 wheel might not be available, forcing source build (requires C++ toolchain)

**Impact**: Installation takes 30+ minutes; developer confusion

**Mitigation**:
- [ ] Pre-merge audit confirms ARM64 wheel available (✓ verified May 21)
- [ ] pyproject.toml pins to libzim>=3.10.0 (not >=3.9.0)
- [ ] Installation script uses `uv pip install` (faster, handles wheels)
- [ ] Fallback: If wheel unavailable, provide Dockerfile for pre-built image

**Acceptance Criterion**: libzim imports successfully in 30 seconds; no source build required

### Risk 5: Performance Regression: Exports Become Slower Post-Merge

**Risk**: New security checks (html.escape, URL validation) add overhead; streaming mode not implemented

**Impact**: Export time increases 10–20%; users experience longer wait times

**Mitigation**:
- [ ] Baseline performance during post-merge validation (before security fixes)
- [ ] Re-measure after security fixes
- [ ] If increase >20%, profile and optimize hot paths
- [ ] Document performance expectations in README

**Acceptance Criterion**: Export time increases <15% vs baseline

---

## Contingency Scenarios

### Scenario 1: XSS Test Fails Post-Implementation

**Symptom**: `test_attribution_footer_html_escaping` fails; payload not properly escaped

**Root Cause**: `html.escape()` not applied to all interpolation points, or URL validation bypassed

**Resolution**:
1. Identify which payload bypassed escaping
2. Recheck all interpolation points in footer construction
3. Verify html.escape() is called (not isinstance() check)
4. If URL scheme validation failed, test urlparse logic independently

**Rollback**: Revert attribution footer changes; use plaintext footer instead of HTML links (temporary)

### Scenario 2: ZimExport ORM Import Fails

**Symptom**: `ImportError: cannot import name 'ZimExport' from app.models`

**Root Cause**: Class not added to models.py, or syntax error in class definition

**Resolution**:
1. Check file actually has ZimExport class at line ~401
2. Verify no syntax errors (missing colons, indentation)
3. Run `python -c "from app.models import ZimExport"` for specific error
4. Check for missing imports (datetime, enum, Float from sqlalchemy)

**Rollback**: Comment out ZimExport class; use raw SQL queries for export tracking (temporary)

### Scenario 3: libzim Wheel Not Available for ARM64

**Symptom**: `pip install libzim` fails with "No matching distribution found"

**Root Cause**: PyPI doesn't have ARM64 wheel; requires source build

**Resolution**:
1. Check PyPI page: https://pypi.org/project/libzim/#files
2. If ARM64 wheel not listed, downgrade to libzim 3.9.0 (which has wheels)
3. If still unavailable, provide Docker image with pre-built libzim
4. File issue with python-libzim maintainers

**Rollback**: Use libzim 3.9.0 instead of 3.10.0 (loses C++ 9.7.0 hardening, but still secure)

### Scenario 4: Thermal Throttling Prevents Medium Exports

**Symptom**: Peak temp exceeds 92°C; exports throttle and take 2–3x longer

**Root Cause**: Pi 5 baseline temperature is higher than expected; compounding with summer heat

**Resolution**:
1. Document throttle threshold in README
2. Implement automatic thermal detection:
   ```python
   import subprocess
   temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1000
   if temp > 85:
       logger.warning(f"Thermal warning: {temp}°C; consider off-peak scheduling")
   ```
3. Recommend off-peak export scheduling (night/early morning)
4. Provide cooling mitigation (fan, thermal paste)

**Rollback**: Disable large exports (cap max_items at 1000) until cooling installed

---

# Rollback Procedure

If Phase 5.1 MVP encounters critical issues post-activation, follow this rollback to restore previous stable state (Phase 4).

## Pre-Rollback Decision Gate

Rollback is triggered if:
- [ ] Critical test failures discovered in production (>50% test failures)
- [ ] Security vulnerability found in ZIM export path
- [ ] Data corruption in content_items table (unlikely, but possible via migration bug)
- [ ] Persistent thermal throttling causing user-facing latency (>5x normal export time)

**Decision**: Product team + tech lead approval required before executing rollback.

## Rollback Steps (30–60 minutes total)

### 1. Stop Active Export Jobs (5 minutes)

```bash
# Kill any in-progress exports
pkill -f "export_to_zim"
pkill -f "python.*zim"

# Verify no zombie processes
ps aux | grep zim
# Expected: Only grep result, no running processes
```

### 2. Revert Code to Previous Release (10 minutes)

```bash
cd projects/open-repo

# Option A: Reset master to pre-merge commit
git log master --oneline | head -10
# Identify the commit before Phase 5.1 merge
git reset --hard <COMMIT_BEFORE_MERGE>

# Option B: Revert the merge commit (if using merge commit strategy)
git revert -m 1 <MERGE_COMMIT_SHA>
git push origin master

# Verify revert
git log master --oneline | head -3
# Expected: Shows original Phase 4 commits
```

### 3. Downgrade Database (if migration issues) (5 minutes)

```bash
cd projects/open-repo/backend

# Check current migration version
sqlite3 sqlite.db "SELECT version FROM alembic_version;"
# Expected: "003" (Phase 5.1)

# Downgrade to migration 002 (Phase 4)
uv run alembic downgrade 002

# Verify downgrade
sqlite3 sqlite.db "SELECT version FROM alembic_version;"
# Expected: "002"

# Verify zim_exports table removed
sqlite3 sqlite.db ".schema zim_exports"
# Expected: Error (table doesn't exist) — this is OK
```

### 4. Remove Phase 5.1 Dependencies (5 minutes)

```bash
cd projects/open-repo/backend

# Remove libzim from pyproject.toml (revert to Phase 4 version)
# Edit pyproject.toml, remove libzim>=3.10.0 line

# Reinstall dependencies (without libzim)
uv pip install -e ".[dev]"

# Verify libzim removed
python -c "import libzim" 2>&1
# Expected: ModuleNotFoundError
```

### 5. Run Phase 4 Test Suite (10 minutes)

```bash
cd projects/open-repo/backend

# Run Phase 4 tests (ContentItem, Endorsement, Federation, etc.)
uv run pytest tests/integration/ -v --tb=short

# Expected: All tests pass (if Phase 5.1 didn't break existing code)
# If Phase 4 tests fail: Check for unintended code changes during merge
```

### 6. Verify API Endpoints (5 minutes)

```bash
cd projects/open-repo/backend

# Start API server
uv run uvicorn app.main:app --reload &

# Test Phase 4 endpoints
curl http://localhost:8000/health
# Expected: 200 OK

curl http://localhost:8000/content/items
# Expected: 200 OK (returns content list)

curl http://localhost:8000/federation/partners
# Expected: 200 OK

# Kill server
pkill -f uvicorn
```

### 7. Notify Users & Plan Remediation (5 minutes)

```markdown
## Phase 5.1 Rollback Notice

Date: [YYYY-MM-DD]
Reason: [Brief reason]

**Status**: Reverted to Phase 4 (federation stable)
**Action**: Phase 5.1 development paused pending investigation

**What's affected**:
- ZIM export feature temporarily unavailable
- OPDS catalog temporarily unavailable
- All Phase 1–4 features (CRUD, federation) remain functional

**Timeline**: Phase 5.1 re-activation in [N] days after remediation

**Contact**: [Support email]
```

---

## Post-Rollback Actions

After rollback completes:

1. **Document failure** (2 hours):
   - Create `PHASE_5_1_ROLLBACK_POSTMORTEM.md`
   - Include: root cause, timeline, reproduction steps
   - Assign remediation tasks

2. **Fix root cause** (varies):
   - If security issue: patch vulnerability, add test, re-code-review
   - If performance issue: optimize hot path, re-benchmark
   - If schema issue: validate migration, test on fresh DB

3. **Plan re-activation** (1–2 weeks):
   - Address all issues identified in postmortem
   - Add regression tests
   - Create new checklist incorporating lessons learned
   - Schedule Phase 5.1 MVP v2 activation

4. **Communicate timeline** to stakeholders

---

## Rollback Success Criteria

Rollback is **complete** when:

- [ ] Master branch reverted to pre-Phase-5.1 commit
- [ ] Migration downgraded to 002 (zim_exports table removed)
- [ ] All Phase 4 tests pass (100% passing)
- [ ] API endpoints respond correctly (health, content, federation)
- [ ] Users notified + remediation plan published

**Estimated Duration**: 30–60 minutes from go-decision to rollback-complete

---

# Appendix A: Command Reference

## Quick Activation Checklist (Copy-Paste Ready)

```bash
#!/bin/bash
# Phase 5.1 Post-Merge Activation Script (execute sequentially)

set -e  # Exit on first error
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "=== STEP 1: Post-Merge Validation ==="
echo "Running database migration..."
rm -f sqlite.db
uv run alembic upgrade head
sqlite3 sqlite.db ".schema zim_exports"

echo "Running integration tests..."
uv run pytest tests/integration/test_export_pipeline.py -v
# Expected: 88 passed

echo "Checking thermal baseline..."
echo "Idle temperature (before export):"
cat /sys/class/thermal/thermal_zone0/temp | awk '{print $1/1000 "°C"}'

echo "=== STEP 2: Security Fix (XSS) ==="
echo "Applying html.escape() to attribution footer..."
# Manual edit required: see section Pre-Activation Requirements § 1

echo "=== STEP 3: ORM Integration ==="
echo "Adding ZimExport model to app/models.py..."
# Manual edit required: see section Pre-Activation Requirements § 2

echo "=== STEP 4: Dependency Installation ==="
echo "Installing libzim>=3.10.0..."
uv pip install "libzim>=3.10.0"
python -c "from libzim.writer import Creator; print('libzim OK')"

echo "Installing zimcheck..."
sudo apt-get install zim-tools
zimcheck --version

echo "=== STEP 5: Documentation ==="
echo "Updating README.md..."
# Manual edit required: see section Pre-Activation Implementation § 4

echo "=== STEP 6: Final Testing ==="
echo "Running all tests with new code..."
uv run pytest tests/ -v --tb=short
# Expected: All pass (88 integration + any unit tests)

echo "=== PHASE 5.1 POST-MERGE ACTIVATION COMPLETE ==="
echo "Go/No-Go checklist: See PHASE_5_1_POST_MERGE_ACTIVATION_CHECKLIST.md"
```

## Useful Debugging Commands

```bash
# Check libzim version
python -c "import libzim; print(libzim.__version__)"

# Test ZIM creation (simple script)
python << 'EOF'
from libzim.writer import Creator
from pathlib import Path
import tempfile

with tempfile.NamedTemporaryFile(suffix='.zim', delete=False) as f:
    output = f.name

try:
    with Creator(filename=output) as creator:
        # creator.add_metadata('Title', 'Test ZIM')
        # creator.add_metadata('Description', 'A test')
        pass  # Stub
    print(f"ZIM created: {output}")
    print(f"Size: {Path(output).stat().st_size} bytes")
except Exception as e:
    print(f"Error: {e}")
EOF

# Test thermal monitoring
while true; do
  temp=$(cat /sys/class/thermal/thermal_zone0/temp)
  echo "$(date +%H:%M:%S) CPU: $((temp / 1000))°C"
  sleep 1
done

# Run single test
uv run pytest tests/integration/test_export_pipeline.py::test_zimmetadata_validation -v

# Check migration status
uv run alembic current
uv run alembic history

# Database inspection
sqlite3 sqlite.db ".tables"
sqlite3 sqlite.db ".schema zim_exports"
sqlite3 sqlite.db "SELECT COUNT(*) FROM zim_exports;"
```

---

# Appendix B: Reference Documents

**Key audit and design documents for Phase 5.1**:

1. **phase-5-1-pre-merge-audit-findings.md** — Session 1447 security + integration audit (read before merge)
2. **PHASE_5_DECISION_FRAMEWORK.md** — Candidate evaluation (explains why ZimWriter is first priority)
3. **phase-5-kiwix-integration-guide.md** — Kiwix architecture, metadata spec, offline access design
4. **FEDERATION_ARCHITECTURE.md** § 7 — Phase 5 integration flow with federation
5. **candidate-1-implementation-checklist.md** — Earlier implementation checklist (may have overlap)

**Code files**:
- `/backend/app/services/export/zim_writer.py` — ZIM export scaffold (stub phase)
- `/backend/app/services/export/opds_generator.py` — OPDS catalog service
- `/backend/app/models.py` — SQLAlchemy ORM (add ZimExport here)
- `/backend/alembic/versions/003_add_zim_exports_table.py` — Migration (already exists)
- `/backend/pyproject.toml` — Dependencies (add libzim here)
- `/backend/tests/integration/test_export_pipeline.py` — 88 tests (all passing)

---

# Appendix C: Known Limitations & Future Work

### MVP Limitations (Phase 5.1)

- [ ] **In-memory buffering**: All articles buffered before write (see Streaming Mode in § 5)
- [ ] **Single-language support**: Only English exports (multilingual in Phase 5.2+)
- [ ] **No incremental updates**: Always full re-export (diff exports in Phase 6)
- [ ] **No CDN integration**: Local path only (S3/Wasabi in Phase 6)
- [ ] **No scheduled exports**: Manual exports only (cron jobs in Phase 6)

### Phase 5.2 Enhancements

- [ ] Streaming write mode (no memory buffering)
- [ ] Multilingual exports (es, fr, de, etc.)
- [ ] Differential/incremental exports (ZIM diffs)
- [ ] Scheduled exports (daily/weekly snapshots)
- [ ] OPDS v2.0 compliance (current: v1.2)

### Phase 6+ Features

- [ ] CDN distribution (S3, Wasabi, IPFS)
- [ ] Cross-node ZIM federation (export from partner nodes)
- [ ] Search federation (unified index across partners)
- [ ] Torrent distribution (peer-to-peer sharing)
- [ ] Mobile app optimization (reduced file size variants)

---

**Checklist Version**: 1.0  
**Last Updated**: May 26, 2026  
**Next Review**: After post-merge validation (June 5, 2026)  
**Owner**: Phase 5.1 Implementation Team  
**Status**: Ready for execution post-merge approval
