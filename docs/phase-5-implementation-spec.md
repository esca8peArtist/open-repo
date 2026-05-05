---
title: "Phase 5: Kiwix/ZIM Export — Implementation Specification"
project: open-repo
phase: 5
status: ready-to-implement
date: 2026-05-04
author: engineering
tags: [kiwix, zim, export, implementation-spec, api, database, testing]
---

# Phase 5: Kiwix/ZIM Export — Implementation Specification

This document is the engineering implementation spec for Phase 5 offline export. It is written to be
actionable immediately once PR #1 (Phase 4 federation) merges to main. The architecture document
(`phase-5-kiwix-architecture.md`) and the stub code already committed to the codebase
(`backend/app/services/export/`) are the foundation; this spec fills in every contract gap needed
to move from stubs to production code.

**Prerequisites**: PR #1 merged. `libzim`, `feedgen`, and `boto3` added to `pyproject.toml`.

---

## 1. ExportService Interface Design

### Role in the Service Layer

The existing service layer (`backend/app/services/`) holds one class per concern:
`EndorsementService`, `ContributionService`, `SearchService`, and so on. `ExportService` follows
the same pattern: one class, one file at `backend/app/services/export_service.py`, injected into
route handlers via FastAPI's `Depends()`.

`ExportService` sits between the HTTP layer and `ZimWriter`. It owns:

- Database queries to build the article list for a given `ExportConfig`
- HTML rendering of `ContentItem` records into self-contained strings
- Lifecycle management of `ExportJob` database rows
- Dispatch of background tasks
- Post-export upload to object storage

### Class Signature

```python
class ExportService:
    def __init__(self, db: AsyncSession) -> None: ...

    async def create_export_job(
        self,
        config: ExportConfig,
        requested_by: Optional[str] = None,
    ) -> ExportJob:
        """
        Persist a new ExportJob row with status=pending and return it.
        The caller is responsible for scheduling the background task.
        Does not start the export; that is done by run_export_job().
        """

    async def run_export_job(self, job_id: int) -> ExportJob:
        """
        Execute a full export for the given job_id.

        Flow:
          1. Load ExportJob from DB; raise if not found or not pending.
          2. Set status=running, started_at=now.
          3. Query ContentItem rows per job.config scope (see _query_articles).
          4. Render each ContentItem to HTML via _render_article().
          5. Feed rendered HTML into ZimWriter.add_article().
          6. Call ZimWriter.create_zim() to write the ZIM file.
          7. Upload ZIM to object storage via _upload_to_storage().
          8. Update ExportJob with status=completed, file_path, article_count,
             file_size_bytes, sha256_checksum, completed_at.
          9. Regenerate OPDS catalog via OPDSGenerator and persist to DB.
         10. Return the updated ExportJob.

        On any exception: set status=failed, error_message, completed_at; re-raise.
        """

    async def get_job(self, job_id: int) -> Optional[ExportJob]:
        """Return ExportJob by id, or None."""

    async def list_jobs(
        self,
        status: Optional[str] = None,
        limit: int = 20,
        offset: int = 0,
    ) -> tuple[list[ExportJob], int]:
        """Return (jobs, total_count) with optional status filter."""

    async def list_completed_exports(self) -> list[ExportJob]:
        """Return all completed jobs ordered by completed_at desc."""

    async def get_download_url(self, job_id: int) -> str:
        """
        Return a pre-signed or direct download URL for the ZIM file.
        If using Cloudflare R2, return a 24-hour pre-signed URL.
        If using local storage, return the /exports/{id}/download path.
        Raises HTTPException 404 if job not found or not completed.
        """

    async def _query_articles(
        self, config: ExportConfig
    ) -> list[ContentItem]:
        """
        Query ContentItem rows from the database per config scope.

        Scope logic:
          LOCAL_ONLY: WHERE source_url IS NULL (items authored locally).
          FEDERATED:  All rows (local + received via ActivityPub).
          DOMAIN:     WHERE domain = config.scope_value.
          TAG:        WHERE content_jsonld->'tags' @> '["<scope_value>"]'
                      (PostgreSQL JSONB containment operator).

        Content freeze: when config.export_started_at is set,
        adds WHERE updated_at <= config.export_started_at to exclude
        items modified after the job was enqueued.
        """

    def _render_article(
        self,
        item: ContentItem,
        language: str = "en",
    ) -> str:
        """
        Render a ContentItem as a self-contained HTML string.

        Requirements:
          - No external HTTP dependencies. All CSS inlined or in <style> tags.
          - No <script> tags (ZIM files should not execute arbitrary JS).
          - Multilingual fields (title, description) resolved to `language`
            with English fallback.
          - For procedure/recipe items: render steps as an ordered list.
          - Include license badge in footer.
          - Include <title> tag matching the item's resolved title string
            (ZimWriter._extract_title_from_html() relies on this).

        Returns a complete HTML document string, not a fragment.
        """
```

### Inputs and Outputs Summary

| Input | Type | Notes |
|---|---|---|
| `config` | `ExportConfig` | Scope, language, flavour, max_items |
| `ContentItem` rows | SQLAlchemy model | Queried from `content_items` table |
| Rendered HTML | `str` | Produced by `_render_article()` |
| `ZimWriteResult` | Dataclass | Returned by `ZimWriter.create_zim()` |

| Output | Type | Notes |
|---|---|---|
| ZIM file | File on disk / R2 | Path stored in `ExportJob.file_path` |
| `ExportJob` | ORM row | Status, SHA-256, size, article count |
| OPDS catalog XML | `bytes` | Regenerated after each completed job |

---

## 2. ZimWriter Wrapper

### Current State

`ZimWriter` is already implemented as a full stub in
`backend/app/services/export/zim_writer.py`. The class structure, docstrings, data models
(`ZimMetadata`, `ZimEntry`, `ExportConfig`, `ExportScope`, `ZimWriteResult`), validation logic,
attribution footer, filename generation, and SHA-256 computation are production-ready. The only
missing piece is the `create_zim()` body, which currently calls `_stub_write_placeholder()` instead
of the python-libzim `Creator` API.

### Completing `create_zim()`

Replace `_stub_write_placeholder()` with the following pattern (fully documented in the
`create_zim()` docstring as a TODO):

```python
from libzim.writer import Creator, Item, StringProvider, Hint

class _ArticleItem(Item):
    def __init__(self, entry: ZimEntry) -> None:
        super().__init__()
        self._entry = entry

    def get_path(self) -> str:
        return self._entry.path

    def get_title(self) -> str:
        return self._entry.title

    def get_mimetype(self) -> str:
        return self._entry.mime_type

    def get_hints(self) -> dict:
        return {Hint.FRONT_ARTICLE: self._entry.is_front_article}

    def get_contentprovider(self):
        content = self._entry.content
        if isinstance(content, str):
            content = content.encode("utf-8")
        return StringProvider(content)

with Creator(str(self.output_path)) as creator:
    creator.config_indexing(True, self.config.language_iso3)
    creator.set_mainpath("index")
    self._apply_metadata_to_creator(creator)
    for entry in self._entries:
        creator.add_item(_ArticleItem(entry))
# Creator.__exit__ triggers the ZIM write
```

Remove `_stub_write_placeholder()` entirely once this is in place.

### Article Batching Strategy

For Phase 5 MVP, the current buffering approach (accumulate all `ZimEntry` objects, then open
`Creator`) is acceptable. The full dataset at current scale is a few hundred to a few thousand items;
at 20 KB average rendered HTML per article, 10,000 articles is ~200 MB of in-memory strings — within
the bounds of a modest production server.

If article count grows beyond 50,000, switch to streaming mode: open the `Creator` context before
the article loop, call `creator.add_item()` directly from `add_article()`, and close the context in
`create_zim()`. The `ZimWriter` docstring already describes this restructuring. This is the same
approach used by `gutenberg2zim` after its v3.0 refactor. No interface change is needed; it is an
internal implementation swap.

Do not implement streaming mode for Phase 5 MVP. Add a `# TODO(phase-5.1)` comment and a test
that documents the memory ceiling (`assert writer.article_count < 50_000`).

### Progress Callback Design

`ZimWriter.create_zim()` should accept an optional `progress_callback` parameter:

```python
def create_zim(
    self,
    compression: str = "default",
    run_zimcheck: bool = True,
    progress_callback: Optional[Callable[[int, int], None]] = None,
) -> ZimWriteResult:
    """
    progress_callback(articles_written: int, total_articles: int) -> None

    Called after every 100 articles are added to the Creator.
    Used by ExportService to update ExportJob.progress_pct in the database
    so that the /exports/{id}/status endpoint can report live progress.
    """
```

The callback fires inside the entry loop:

```python
for i, entry in enumerate(self._entries):
    creator.add_item(_ArticleItem(entry))
    if progress_callback and entry.is_front_article and (i + 1) % 100 == 0:
        progress_callback(self._article_count, total_front_articles)
```

`ExportService.run_export_job()` passes a closure that writes `progress_pct` to the `ExportJob`
row. The status endpoint reads this field and returns it in the response.

---

## 3. Export Catalog API Endpoints

All endpoints are mounted under the `/api/v1/` prefix, consistent with the existing route
structure. Add them to a new router file at `backend/app/api/v1/exports.py` and register it in
`backend/app/routes.py`.

### `GET /api/v1/exports`

List all completed export jobs available for download.

**Query parameters**: none required. Optional: `flavour`, `language` for filtering.

**Response** (`200 OK`):

```json
{
  "exports": [
    {
      "id": 3,
      "status": "completed",
      "flavour": "nopic",
      "language": "eng",
      "article_count": 847,
      "file_size_bytes": 41943040,
      "file_size_human": "40.0 MB",
      "sha256_checksum": "a3f2...",
      "zim_name": "open-repo_en_nopic_2026-04.zim",
      "started_at": "2026-04-28T02:00:00Z",
      "completed_at": "2026-04-28T02:04:33Z",
      "download_url": "https://exports.example.org/zim/open-repo_en_nopic_2026-04.zim"
    }
  ],
  "total": 1
}
```

**Implementation note**: `download_url` is generated by `ExportService.get_download_url()`. For R2,
this is a pre-signed URL generated at request time and valid for 24 hours. For local storage, it is
the `/api/v1/exports/{id}/download` path.

### `POST /api/v1/exports`

Trigger a new export job asynchronously.

**Request body**:

```json
{
  "scope": "local",
  "scope_value": null,
  "flavour": "nopic",
  "language": "en",
  "include_federated": false
}
```

All fields are optional; defaults match `ExportConfig` defaults. Validate using a Pydantic schema
`ExportCreateRequest` that mirrors `ExportConfig` fields.

**Rate limiting**: reject the request with `429 Too Many Requests` if a job with `status=running`
already exists for the same `flavour+language` combination. This prevents accidental concurrent
exports of the same ZIM variant.

**Response** (`202 Accepted`):

```json
{
  "id": 4,
  "status": "pending",
  "flavour": "nopic",
  "language": "eng",
  "created_at": "2026-05-04T10:00:00Z",
  "status_url": "/api/v1/exports/4/status"
}
```

**Background task dispatch**: use `fastapi.BackgroundTasks` for the MVP. If Celery is added (Phase
5.1), replace with `celery.send_task()`. The background task calls
`await export_service.run_export_job(job_id)`.

### `GET /api/v1/exports/{id}/status`

Poll the status of a specific export job.

**Path parameter**: `id` (integer).

**Response** (`200 OK`):

```json
{
  "id": 4,
  "status": "running",
  "progress_pct": 42,
  "article_count": null,
  "file_size_bytes": null,
  "sha256_checksum": null,
  "error_message": null,
  "started_at": "2026-05-04T10:00:05Z",
  "completed_at": null
}
```

`status` is one of: `pending`, `running`, `completed`, `failed`.

`progress_pct` is `null` when status is `pending`, an integer 0–100 when `running` or `completed`,
and `null` when `failed`.

**Response** (`404 Not Found`) if job id does not exist.

### `GET /api/v1/exports/{id}/download`

Stream the ZIM file to the client.

**Path parameter**: `id` (integer). Job must be in `completed` status.

**Response headers**:

```
Content-Type: application/x-zim
Content-Disposition: attachment; filename="open-repo_en_nopic_2026-04.zim"
Content-Length: <file_size_bytes>
ETag: "<sha256_checksum>"
Accept-Ranges: bytes
```

**Range request support**: implement using `starlette.responses.FileResponse` with
`headers={"Accept-Ranges": "bytes"}`. For R2-hosted files, redirect to the pre-signed URL instead
of proxying (saves bandwidth; the ZIM file may be several gigabytes).

**Response** (`404 Not Found`) if job id does not exist or status is not `completed`.

**Response** (`409 Conflict`) if status is `running` or `pending`.

**Security**: do not expose the internal `file_path` column in any response. The download endpoint
resolves the path server-side from the job id.

---

## 4. Database Schema Additions

### ExportJob Table

Add the following migration as `backend/alembic/versions/003_add_export_jobs.py`:

```python
def upgrade():
    op.create_table(
        "export_jobs",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("status", sa.Enum(
            "pending", "running", "completed", "failed",
            name="exportjobstatus"
        ), nullable=False, index=True, server_default="pending"),
        sa.Column("scope", sa.String(20), nullable=False, server_default="local"),
        sa.Column("scope_value", sa.String(100), nullable=True),
        sa.Column("flavour", sa.String(50), nullable=False, server_default="nopic"),
        sa.Column("language", sa.String(10), nullable=False, server_default="eng"),
        sa.Column("include_federated", sa.Boolean, nullable=False, server_default="false"),
        sa.Column("requested_by", sa.String(255), nullable=True),
        sa.Column("progress_pct", sa.Integer, nullable=True),
        sa.Column("article_count", sa.Integer, nullable=True),
        sa.Column("file_size_bytes", sa.BigInteger, nullable=True),
        sa.Column("file_path", sa.String(1024), nullable=True),
        sa.Column("sha256_checksum", sa.String(64), nullable=True),
        sa.Column("zim_name", sa.String(255), nullable=True),
        sa.Column("error_message", sa.Text, nullable=True),
        sa.Column("started_at", sa.DateTime, nullable=True, index=True),
        sa.Column("completed_at", sa.DateTime, nullable=True, index=True),
        sa.Column("created_at", sa.DateTime, nullable=False,
                  server_default=sa.func.now(), index=True),
    )

def downgrade():
    op.drop_table("export_jobs")
    op.execute("DROP TYPE IF EXISTS exportjobstatus")
```

### ORM Model

Add `ExportJob` to `backend/app/models.py` alongside the existing federation models:

```python
class ExportJobStatus(str, enum.Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

class ExportJob(Base):
    __tablename__ = "export_jobs"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    status = Column(Enum(ExportJobStatus), nullable=False,
                    default=ExportJobStatus.PENDING, index=True)
    scope = Column(String(20), nullable=False, default="local")
    scope_value = Column(String(100), nullable=True)
    flavour = Column(String(50), nullable=False, default="nopic")
    language = Column(String(10), nullable=False, default="eng")
    include_federated = Column(Boolean, nullable=False, default=False)
    requested_by = Column(String(255), nullable=True)
    progress_pct = Column(Integer, nullable=True)
    article_count = Column(Integer, nullable=True)
    file_size_bytes = Column(BigInteger, nullable=True)
    file_path = Column(String(1024), nullable=True)
    sha256_checksum = Column(String(64), nullable=True)
    zim_name = Column(String(255), nullable=True)
    error_message = Column(Text, nullable=True)
    started_at = Column(DateTime, nullable=True, index=True)
    completed_at = Column(DateTime, nullable=True, index=True)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow, index=True)
```

### Migration Strategy

Follow the additive-only rule already established by migrations `001` and `002`:

- `003_add_export_jobs.py` adds the new table. No existing tables are altered.
- The `ExportJobStatus` enum is created as a PostgreSQL `TYPE` in `upgrade()` and dropped in
  `downgrade()`. This is consistent with how `ConflictType`, `TrustStatus`, and other enums are
  handled in the existing migrations.
- If the migration needs to be rolled back before Phase 5 is complete, `downgrade()` drops only the
  new table and its associated enum type. No data loss to existing tables.
- No column renames, no `ALTER COLUMN` statements, no changes to `content_items`, `endorsements`,
  `contributions`, `federation_partners`, `activities`, or any existing table.

---

## 5. Test Strategy

### Unit Tests: ZimWriter

**File**: `backend/tests/test_zim_writer.py` (add alongside existing test files in
`backend/tests/`).

The integration test file at `backend/tests/integration/test_export_pipeline.py` already covers
the stub phase thoroughly. Once `create_zim()` is completed with real python-libzim calls, add the
following unit tests that validate ZIM binary correctness by reading the output back:

```python
# Post-stub: read output with libzim.reader.Archive
from libzim.reader import Archive

def test_zim_readable_after_creation(zim_writer, tmp_zim_path):
    """The created ZIM file is openable by libzim.reader.Archive."""
    zim_writer.add_article(path="index", content=make_html("Home", "Welcome"),
                           article_type="procedure")
    result = zim_writer.create_zim(run_zimcheck=False)
    archive = Archive(str(result.output_path))
    assert archive.article_count >= 1

def test_zim_main_entry_accessible(zim_writer, tmp_zim_path):
    """The main path ('index') is accessible via archive.main_entry."""
    zim_writer.add_article(path="index", content=make_html("Home", "Welcome"),
                           article_type="procedure")
    result = zim_writer.create_zim(run_zimcheck=False)
    archive = Archive(str(result.output_path))
    main = archive.main_entry
    assert main.path == "index"

def test_zim_full_text_search_index_present(zim_writer, tmp_zim_path):
    """Full-text search index is present (config_indexing was called)."""
    zim_writer.add_article(path="water/bafkrei001",
                           content=make_html("Biosand Filter", "Sand filtration"),
                           article_type="procedure")
    result = zim_writer.create_zim(run_zimcheck=False)
    archive = Archive(str(result.output_path))
    assert archive.has_fulltext_index
```

**Mocking libzim for pure unit tests**: when testing batching logic and callback firing without
writing a real ZIM, patch `libzim.writer.Creator` with `unittest.mock.patch`. The existing stub
tests in `test_export_pipeline.py` already demonstrate this pattern (by way of
`zimcheck_binary=None`).

**Batching tests to write now** (can run without libzim):

```python
def test_progress_callback_fires_every_100_articles(zim_writer):
    """progress_callback is called after every 100 articles."""
    calls = []
    callback = lambda written, total: calls.append((written, total))
    for i in range(250):
        zim_writer.add_article(path=f"test/{i}", content=make_html(f"Item {i}", ""),
                               article_type="procedure")
    # With real Creator, would call create_zim(progress_callback=callback)
    # For now: test that callback signature is accepted
    result = zim_writer.create_zim(run_zimcheck=False,
                                   progress_callback=callback)
    assert result.article_count == 250
```

### Integration Test: 5-Article Round-Trip

**File**: `backend/tests/integration/test_export_pipeline.py` (already exists; extend with a
`@pytest.mark.integration` class).

The goal is: create 5 test articles in a real (test) database, run `ExportService.run_export_job()`,
read the output ZIM with `libzim.reader.Archive`, and verify correctness.

```python
@pytest.mark.integration
class TestExportRoundTrip:

    async def test_five_articles_to_zim_and_back(
        self, db_session, tmp_path, five_content_items
    ):
        """
        Create 5 ContentItem rows -> ExportService -> ZimWriter -> read ZIM back.

        Verifies:
          - article_count in ZIM matches DB query result
          - Each article path is accessible via archive.get_entry_by_path()
          - Full-text search index is present
          - ExportJob row is updated with completed status and correct metadata
        """
        config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour="nopic")
        service = ExportService(db=db_session)
        job = await service.create_export_job(config=config)

        # Override output path to tmp_path for test isolation
        await service.run_export_job(job.id, output_dir=tmp_path)

        # Reload from DB
        updated_job = await service.get_job(job.id)
        assert updated_job.status == ExportJobStatus.COMPLETED
        assert updated_job.article_count == 5 + 1  # 5 items + index page
        assert updated_job.sha256_checksum is not None
        assert updated_job.file_size_bytes > 0

        # Read ZIM back
        archive = Archive(str(updated_job.file_path))
        assert archive.article_count >= 5
        assert archive.has_fulltext_index
```

### Test Fixtures Needed

| Fixture | File | Description |
|---|---|---|
| `five_content_items` | `tests/conftest.py` | 5 `ContentItem` rows inserted into test DB |
| `db_session` | `tests/conftest.py` | Async test DB session (already exists in `conftest.py`) |
| `tmp_zim_path` | `tests/integration/test_export_pipeline.py` | Already exists |
| `sample_metadata` | `tests/integration/test_export_pipeline.py` | Already exists |
| `sample_config` | `tests/integration/test_export_pipeline.py` | Already exists |
| `zim_writer` | `tests/integration/test_export_pipeline.py` | Already exists |

The `five_content_items` fixture does not yet exist. It should insert 5 `ContentItem` rows with
distinct `cid`, `item_type`, and `domain` values, and yield them (using `pytest.fixture` with
`yield` for teardown). Use the same synthetic data as `sample_content_items` in the existing
pipeline tests.

The round-trip test requires `libzim` to be installed. Gate it with:

```python
libzim = pytest.importorskip("libzim", reason="libzim not installed")
```

This ensures the test is skipped cleanly in environments where `libzim` is not yet available
(e.g., CI before the dependency is added).

---

## 6. Incremental Export Analysis

### Decision: Full Re-Export on Each Trigger

Phase 5 uses **full re-export** on every trigger. No delta/incremental export is implemented.

### Rationale

**Technical state of incremental ZIM tools**: The `zimdiff`/`zimpatch` tools proposed in 2013
have no evidence of production readiness as of 2025. The Kiwix Android app requires full-file
replacement on update. No major ZIM publisher (Wikipedia, Stack Exchange, Project Gutenberg) has
deployed incremental updates.

**Scale fit**: At open-repo's current scale, a full export of all `content_items` is projected to
complete in under 5 minutes and produce a ZIM file under 500 MB (text-only, nopic flavour). This
is a cost-acceptable operation to run weekly, or on-demand. The design already supports versioned
exports via `ZimWriter.compute_period()` — previous ZIM files remain available for download while
a new one is being generated.

**Alternative for targeted freshness**: If users need fresher snapshots without waiting for a full
re-export, the correct approach is **scoped exports** rather than binary diffs: trigger a
domain-specific export (`ExportConfig(scope=ExportScope.DOMAIN, scope_value="agriculture")`), which
completes faster and produces a smaller file. This is already supported by the `ExportConfig` and
`ExportScope` models and requires no new infrastructure.

**When to revisit**: if article count exceeds 100,000 and full export time exceeds 30 minutes,
revisit with one of: (a) parallel domain exports, (b) tiered export schedule (full weekly, domain
daily), or (c) monitor the openZIM ecosystem for production-ready incremental tooling.

**Summary table**:

| Option | MVP suitability | Complexity | Notes |
|---|---|---|---|
| Full re-export | Yes | Low | Used by Wikipedia, Stack Exchange, Gutenberg |
| Incremental ZIM diff | No | High | No production tool exists |
| Scoped sub-exports | Yes (Phase 5.1) | Medium | Already supported by ExportConfig |
| Segment by date range | Yes (Phase 5.1) | Low | e.g., "articles updated this week" as a ZIM |

---

## Implementation Checklist

Tasks in order of dependency. Items at the same level are parallelizable.

**Level 0 (prerequisites, can start now)**
- [ ] Add `libzim>=3.2,<4.0` to `pyproject.toml`
- [ ] Add `feedgen>=0.9` to `pyproject.toml`
- [ ] Add `boto3>=1.34` (for R2/S3 upload) to `pyproject.toml`
- [ ] Run `uv pip install libzim feedgen boto3`
- [ ] Provision Cloudflare R2 bucket (or local MinIO for development)

**Level 1 (after prerequisites)**
- [ ] Write migration `003_add_export_jobs.py`
- [ ] Add `ExportJob` ORM model to `models.py`
- [ ] Complete `ZimWriter.create_zim()` with real python-libzim Creator calls
- [ ] Remove `_stub_write_placeholder()` from `ZimWriter`
- [ ] Uncomment `_apply_metadata_to_creator()` body

**Level 2 (after Level 1)**
- [ ] Implement `ExportService` at `backend/app/services/export_service.py`
- [ ] Implement `_render_article()` using Jinja2 template
- [ ] Add `progress_callback` parameter to `ZimWriter.create_zim()`

**Level 3 (after Level 2)**
- [ ] Implement export API endpoints (`backend/app/api/v1/exports.py`)
- [ ] Register exports router in `backend/app/routes.py`
- [ ] Add Pydantic schemas for export request/response to `schemas.py`
- [ ] Write unit tests for `ExportService` (mock DB, mock ZimWriter)
- [ ] Write round-trip integration test (real DB, real libzim)

**Level 4 (after Level 3)**
- [ ] OPDS endpoint at `/opds/v2/root.xml` (uses existing `OPDSGenerator`)
- [ ] Scheduled export task (FastAPI startup background task or Celery Beat)
- [ ] User documentation: how to use open-repo offline

**Branch**: `feature/phase-5-export`. Cannot merge to `main` until PR #1 lands.
