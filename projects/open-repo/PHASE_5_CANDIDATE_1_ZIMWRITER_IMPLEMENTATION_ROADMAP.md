---
title: "Phase 5 Candidate 1 — ZimWriter libzim Integration: Detailed Implementation Roadmap"
project: open-repo
phase: 5
candidate: 1
status: ready-for-implementation
date: 2026-05-19
effort_estimate: "8-11 hours"
pr_dependency: "Phase 4 PR #1 merged (255 tests passing)"
---

# Phase 5 Candidate 1: ZimWriter libzim Integration
## Detailed Implementation Roadmap

**Status**: Ready for implementation — scaffold 100% complete, stubs awaiting replacement  
**Effort**: 8-11 hours  
**Blocking**: Nothing. Can start on a feature branch immediately.  
**Unblocks**: OPDS feed (Candidate 2), CDN upload, scheduled exports, IPFS integration

---

## Architecture: How ZimWriter Will Work After Integration

```
                    PHASE 4 DATABASE
                    ┌──────────────────────────────┐
                    │  content_items                │
                    │  WHERE is_local=True          │
                    │  AND status IN (published,    │
                    │    featured)                  │
                    │  ORDER BY domain, created_at  │
                    └──────────────┬───────────────┘
                                   │  batches of 200
                                   ▼
                    ┌──────────────────────────────┐
                    │  ExportJob (FastAPI           │
                    │  BackgroundTask / APScheduler)│
                    │  app/api/v1/export.py         │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │  ZimWriter.__init__()         │
                    │  app/services/export/         │
                    │  zim_writer.py                │
                    │                               │
                    │  - Validates ZimMetadata      │
                    │  - Opens libzim.Creator ctx   │
                    │  - Configures Xapian index    │
                    │  - Sets mainpath = "index"    │
                    └──────────────┬───────────────┘
                                   │  add_article() per item
                                   ▼
                    ┌──────────────────────────────┐
                    │  HTML Rendering               │
                    │  (inline Jinja2 templates     │
                    │  in zim_writer.py)            │
                    │                               │
                    │  - Self-contained CSS         │
                    │  - No external deps           │
                    │  - Static content only        │
                    │  - Attribution footer for     │
                    │    federated items            │
                    └──────────────┬───────────────┘
                                   │  ZimEntry objects
                                   ▼
                    ┌──────────────────────────────┐
                    │  libzim.writer.Creator        │
                    │  (real, not stub)             │
                    │                               │
                    │  creator.add_item(            │
                    │    ArticleItem(entry))        │
                    │                               │
                    │  context exit → ZIM written   │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │  zimcheck subprocess          │
                    │  validation                   │
                    │  [FAIL → .zim.invalid]        │
                    │  [PASS → continue]            │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │  SHA-256 checksum             │
                    │  .sha256 sidecar file         │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │  ZimWriteResult               │
                    │  → zim_exports DB table       │
                    │  → CDN upload (R2)            │
                    │  → OPDS catalog update        │
                    └──────────────────────────────┘
```

**Offline archive variants produced:**

| Variant | Query filter | Expected size | Schedule |
|---------|-------------|---------------|----------|
| Full nopic | is_local=True, all domains | 15-80 MB compressed | Weekly Sunday 02:00 UTC |
| Domain (agriculture) | is_local=True, domain='agriculture' | 3-10 MB | Weekly if >10 items |
| Domain (recipes) | is_local=True, domain='recipes' | 3-10 MB | Weekly if >10 items |
| Full with images | is_local=True, include_images=True | 60-400 MB | Monthly |
| Reference snapshot | Frozen at request time | Variable | Manual trigger |

---

## Exact Code Entry Points and Files to Modify

### File 1: `pyproject.toml`
**Change**: Add one line under `[project.dependencies]`

```toml
# ADD under [project.dependencies]:
"libzim>=3.2,<4.0",
```

**Note**: The PyPI package name is `libzim`, not `python-libzim`. The import is `from libzim.writer import Creator, Item, StringProvider, Hint`. Pre-built wheels are available for Linux x86_64, ARM64 (Raspberry Pi 5 supported), macOS, and Windows. No compiler required for standard deployments.

---

### File 2: `app/services/export/zim_writer.py` — Five Changes

All five changes are in the same file. The class hierarchy, data models, and method signatures do not change — only the stub internals are replaced.

#### Change 1: Add import at top of file (after existing imports)

**Location**: After line 48 (`from typing import Optional`)

```python
# ADD these imports (only active after libzim is installed):
try:
    from libzim.writer import Creator, Item, StringProvider, Hint
    _LIBZIM_AVAILABLE = True
except ImportError:
    _LIBZIM_AVAILABLE = False
    Creator = None  # type: ignore[assignment,misc]
```

This import guard allows the module to load in test environments without libzim installed, falling back to the stub behavior. Remove the guard after the integration is verified in CI.

#### Change 2: Add `ArticleItem` inner class (new class, not replacing anything)

**Location**: Add after the `ZimEntry` dataclass (before the `ZimWriter` class, around line 408)

```python
class ArticleItem(Item):
    """
    Adapter from ZimEntry to libzim's Item interface.

    libzim.writer.Creator.add_item() requires an Item subclass.
    This class bridges ZimEntry (our data model) to libzim's API.

    Thread safety: Each ArticleItem instance is consumed once by add_item()
    and not retained. Thread-safe as long as the owning ZimWriter is
    called from a single thread (which is enforced by ZimWriter's docs).
    """

    def __init__(self, entry: "ZimEntry") -> None:
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

    def get_contentprovider(self) -> "StringProvider":
        content = self._entry.content
        if isinstance(content, str):
            content = content.encode("utf-8")
        return StringProvider(content)
```

#### Change 3: Replace `create_zim()` stub call

**Location**: `ZimWriter.create_zim()` method, around line 762

Replace:
```python
        # TODO(post-PR-merge): Replace this stub with actual python-libzim Creator calls
        # See the docstring above for the correct implementation pattern.
        # For now, write a placeholder file to allow test harness to run.
        self._stub_write_placeholder()
```

With:
```python
        if not _LIBZIM_AVAILABLE:
            # Fallback stub for environments without libzim installed (dev/CI without wheel)
            self._stub_write_placeholder()
        else:
            with Creator(str(self.output_path)) as creator:
                creator.config_indexing(True, self.config.language_iso3)
                creator.set_mainpath("index")
                self._apply_metadata_to_creator(creator)
                for entry in self._entries:
                    creator.add_item(ArticleItem(entry))
            # Creator.__exit__ triggers ZIM file finalization and write
```

#### Change 4: Implement `_apply_metadata_to_creator()`

**Location**: `ZimWriter._apply_metadata_to_creator()`, around line 870

Replace the entire method body (currently just `pass`) with:

```python
    def _apply_metadata_to_creator(self, creator: "Creator") -> None:
        """Apply all ZimMetadata fields to the open libzim Creator instance."""
        creator.add_metadata("Title", self.metadata.title)
        creator.add_metadata("Description", self.metadata.description)
        creator.add_metadata("Language", self.metadata.language)
        creator.add_metadata("Creator", self.metadata.creator)
        creator.add_metadata("Publisher", self.metadata.publisher)
        creator.add_metadata("Date", self.metadata.date)
        creator.add_metadata("Name", self.metadata.name)
        creator.add_metadata("Flavour", self.metadata.flavour)
        creator.add_metadata("Tags", self.metadata.tags)
        creator.add_metadata("Source", self.metadata.source_url)
        creator.add_metadata("Scraper", self.metadata.scraper)
        if self.metadata.long_description:
            creator.add_metadata("LongDescription", self.metadata.long_description)
        # Add illustration — required for zimcheck to pass
        illustration_bytes = self._get_illustration_bytes()
        if illustration_bytes:
            creator.add_illustration(48, illustration_bytes)
        else:
            # Fallback: 1x1 transparent PNG (passes zimcheck with a warning, not a failure)
            creator.add_illustration(48, _FALLBACK_ILLUSTRATION_PNG)
```

Add at module level (before the `ZimWriter` class):

```python
# Minimal 1x1 transparent PNG — used as fallback illustration when no icon is provided.
# This is a well-formed PNG that passes zimcheck with a warning rather than a failure.
# Replace with a real 48x48 branded icon before publishing.
_FALLBACK_ILLUSTRATION_PNG = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x000\x00\x00\x000"
    b"\x08\x06\x00\x00\x00W\x02\xf9\x87\x00\x00\x00\x0bIDATx\x9cc"
    b"\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82"
)
```

**Note**: Replace `_FALLBACK_ILLUSTRATION_PNG` with a real 48x48 open-repo branded PNG before going live. The fallback passes zimcheck with a warning on illustration dimensions but does not cause export failure.

#### Change 5: Re-enable zimcheck in `create_zim()`

The existing `_run_zimcheck()` method is already correct. The only change needed is removing the `TODO` comment and ensuring `run_zimcheck=True` (which is the default). No code changes needed in this method.

However, in `create_zim()`, the conditional `if run_zimcheck and self.zimcheck_binary:` on line ~774 already handles this correctly. Verify that the default call path `writer.create_zim()` uses `run_zimcheck=True`.

---

### File 3: `app/services/export/zim_writer.py` — Remove dead code after verification

After all tests pass, remove `_stub_write_placeholder()` entirely (lines 914-931). It should not exist in the final implementation. Delete it as a separate commit after integration tests confirm correctness.

---

### Files NOT Modified
- `app/services/export/opds_generator.py` — untouched by Candidate 1
- `app/models.py` — no schema changes needed for Candidate 1
- `app/api/v1/` — the export API endpoint (once created) calls ZimWriter; no ZimWriter changes needed
- `tests/` — all 84 export tests already cover the public interface; stub swaps out transparently

---

## Database Schema: ZimExport Table

A new table is needed to record completed exports. This schema is referenced by the OPDS generator (Candidate 2) and any future CDN management logic.

**Migration file**: `alembic/versions/2026_05_XXXX_add_zim_exports_table.py`

```sql
CREATE TABLE zim_exports (
    id              BIGSERIAL PRIMARY KEY,

    -- ZIM identity (stable across versions of the same flavour)
    zim_uuid        VARCHAR(36) NOT NULL UNIQUE,
    name            VARCHAR(255) NOT NULL,      -- e.g., "open-repo_en_nopic"
    flavour         VARCHAR(50) NOT NULL,       -- e.g., "nopic", "agriculture"
    language        VARCHAR(10) NOT NULL,       -- ISO 639-3 e.g., "eng"
    period          VARCHAR(10) NOT NULL,       -- e.g., "2026-05"

    -- Content metadata
    article_count   INTEGER NOT NULL,
    file_size_bytes BIGINT NOT NULL,
    sha256          VARCHAR(64) NOT NULL,
    title           VARCHAR(255) NOT NULL,
    description     VARCHAR(80) NOT NULL,

    -- Storage
    cdn_url         VARCHAR(512),               -- R2 or GitHub Releases URL
    local_path      VARCHAR(512),               -- Temp local path (cleared after upload)

    -- State machine
    status          VARCHAR(20) NOT NULL DEFAULT 'generating',
    -- Valid statuses: generating, validating, uploading, available, superseded, deleted, error

    is_current      BOOLEAN NOT NULL DEFAULT FALSE,
    is_reference    BOOLEAN NOT NULL DEFAULT FALSE,

    -- Export job tracking
    export_scope    VARCHAR(20) NOT NULL,       -- ExportScope enum value
    scope_value     VARCHAR(100),               -- Domain name for DOMAIN scope
    include_images  BOOLEAN NOT NULL DEFAULT FALSE,

    -- Validation results
    zimcheck_passed BOOLEAN,
    zimcheck_output TEXT,
    generation_duration_seconds FLOAT,

    -- Timestamps
    started_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    completed_at    TIMESTAMPTZ,
    superseded_at   TIMESTAMPTZ,
    deleted_at      TIMESTAMPTZ,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Indexes for common query patterns
CREATE INDEX idx_zim_exports_name_flavour ON zim_exports (name, flavour);
CREATE INDEX idx_zim_exports_is_current ON zim_exports (is_current) WHERE is_current = TRUE;
CREATE INDEX idx_zim_exports_status ON zim_exports (status);
CREATE INDEX idx_zim_exports_period ON zim_exports (period);
```

**SQLAlchemy model** (`app/models.py` addition):

```python
class ZimExportStatus(str, enum.Enum):
    GENERATING = "generating"
    VALIDATING = "validating"
    UPLOADING = "uploading"
    AVAILABLE = "available"
    SUPERSEDED = "superseded"
    DELETED = "deleted"
    ERROR = "error"

class ZimExport(Base):
    __tablename__ = "zim_exports"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    zim_uuid = Column(String(36), unique=True, nullable=False, index=True)
    name = Column(String(255), nullable=False, index=True)
    flavour = Column(String(50), nullable=False, index=True)
    language = Column(String(10), nullable=False)
    period = Column(String(10), nullable=False, index=True)
    article_count = Column(Integer, nullable=False)
    file_size_bytes = Column(BigInteger, nullable=False)
    sha256 = Column(String(64), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String(80), nullable=False)
    cdn_url = Column(String(512), nullable=True)
    local_path = Column(String(512), nullable=True)
    status = Column(Enum(ZimExportStatus), nullable=False,
                    default=ZimExportStatus.GENERATING, index=True)
    is_current = Column(Boolean, nullable=False, default=False, index=True)
    is_reference = Column(Boolean, nullable=False, default=False)
    export_scope = Column(String(20), nullable=False)
    scope_value = Column(String(100), nullable=True)
    include_images = Column(Boolean, nullable=False, default=False)
    zimcheck_passed = Column(Boolean, nullable=True)
    zimcheck_output = Column(Text, nullable=True)
    generation_duration_seconds = Column(Float, nullable=True)
    started_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    superseded_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow,
                        onupdate=datetime.utcnow)
```

---

## Serialization and Sync Protocol

### What Gets Bundled Per Export

Each ZIM archive is a single self-contained binary file containing:

1. **ZIM header** (libzim-managed): compression settings, cluster offsets, index pointers
2. **Articles** (one per `content_items` row): path, HTML content, title
3. **Metadata M/ namespace**: Title, Description, Language, Creator, Publisher, Date, Name, Flavour, Tags, Source, Scraper, LongDescription, Illustration
4. **Xapian full-text index** (auto-generated by libzim): embedded search database covering all article titles and bodies
5. **Shared CSS resource** (added via `add_resource()`): `style/main.css` for consistent article rendering

### Sync and Version Management

**Stable UUID per flavour**: Each name+flavour combination (e.g., `open-repo_en_nopic`) gets a UUID assigned at first export creation. This UUID is stored in `zim_exports.zim_uuid` and reused across all subsequent monthly exports for that flavour. Kiwix uses this UUID to recognize new exports as updates to the same content rather than new catalogs.

**Period collision handling**: `ZimWriter.compute_period()` (already implemented) appends alphabetic suffixes for same-month re-exports: `2026-05`, `2026-05a`, `2026-05b`.

**Retention policy** (applied after each successful export and CDN upload):
- Set `is_current = True` on the new export
- Set `is_current = False` + `status = superseded` on the previous current export for the same name+flavour
- Delete any export older than 60 days that is not `is_reference = True`
- Keep a maximum of 2 non-reference versions in the `available` state at any time

### Offline Integrity Verification

Every export produces a `.sha256` sidecar file at `{cdn_url}.sha256` containing a single line: `{hex_hash}  {filename}` (standard `sha256sum` format). Users can verify with:

```bash
sha256sum -c open-repo_en_nopic_2026-05.zim.sha256
```

`zimcheck` validation runs before the SHA-256 is computed, so the checksum covers a verified-valid ZIM only.

---

## Test Matrix

### 12 Test Scenarios

**Category: Core ZIM Output (unit, no zimcheck subprocess)**

| # | Test ID | What it tests | Input | Expected result | Priority |
|---|---------|--------------|-------|----------------|----------|
| 1 | `test_zim_writer_creates_real_zim_file` | libzim Creator produces a binary ZIM file (not stub placeholder) | 10 articles with valid HTML content | Output file is > 1KB; first bytes match ZIM magic header `\x5a\x49\x4d\x04` | P0 |
| 2 | `test_zim_metadata_all_mandatory_fields` | All 8 mandatory ZIM metadata fields are written | ZimMetadata with full field set | libzim reader can retrieve Title, Description, Language, Creator, Publisher, Date, Name, Illustration via `Archive.get_metadata()` | P0 |
| 3 | `test_xapian_index_populated` | Full-text search index is embedded and returns results | 5 articles on agriculture | `Archive.search("biosand filter")` returns >= 1 result matching a known article | P0 |
| 4 | `test_article_count_matches_database` | All queried content items appear in ZIM | 50 articles from DB | `len(Archive.get_articles())` == 50 (or equivalent iteration count) | P0 |
| 5 | `test_html_no_external_dependencies` | Rendered HTML has no external HTTP refs | Article with image references | BeautifulSoup parse: no `<link href="http">`, no `<img src="http">`, no `<script src="http">` | P0 |

**Category: ZimCheck Validation (integration, requires zimcheck binary)**

| # | Test ID | What it tests | Input | Expected result | Priority |
|---|---------|--------------|-------|----------------|----------|
| 6 | `test_zimcheck_passes_on_valid_export` | zimcheck subprocess validates the output | 10-article nopic ZIM | `zimcheck output.zim` returns exit code 0; no error lines in stdout | P0 |
| 7 | `test_zimcheck_fails_on_corrupted_archive` | ZimWriter handles zimcheck failure gracefully | Force-corrupt ZIM bytes after write | `create_zim()` renames file to `.zim.invalid`; `ZimWriteResult.zimcheck_passed == False`; no exception raised | P1 |

**Category: Offline Read Scenarios (integration, uses libzim reader)**

| # | Test ID | What it tests | Input | Expected result | Priority |
|---|---------|--------------|-------|----------------|----------|
| 8 | `test_offline_read_article_by_path` | Written articles are retrievable by path | Export with `path="agriculture/biosand-filter"` | `Archive.get_entry_by_path("agriculture/biosand-filter").get_item().content.tobytes()` returns the HTML bytes | P0 |
| 9 | `test_unicode_content_survives_roundtrip` | Non-ASCII characters survive write-read cycle | Article with Spanish accents, Arabic script | Read-back content matches original UTF-8 encoding exactly; no replacement characters | P1 |
| 10 | `test_nopic_variant_excludes_images` | nopic export has no binary image resources | 3 articles with inline image data, `include_images=False` | ZIM archive contains no entries with `mime_type.startswith("image/")` | P1 |

**Category: Sync and Recovery (unit)**

| # | Test ID | What it tests | Input | Expected result | Priority |
|---|---------|--------------|-------|----------------|----------|
| 11 | `test_period_collision_handling` | Duplicate period gets alphabetic suffix | `existing_periods=["2026-05"]`, `now=datetime(2026, 5, 19)` | `ZimWriter.compute_period(...)` returns `"2026-05a"` | P1 |
| 12 | `test_zimwriter_not_reusable_after_finalize` | Second `create_zim()` call raises RuntimeError | Call `create_zim()` twice on same instance | `RuntimeError: ZimWriter.create_zim() can only be called once` | P2 |

### Test File Locations

```
tests/
├── unit/
│   ├── test_zim_writer.py          # Tests 1-5, 7, 10-12 (no subprocess, no libzim reader)
│   └── test_zim_metadata.py        # Metadata validation tests (already exists, passes with stubs)
└── integration/
    ├── test_zimcheck_validation.py  # Tests 6-7 (requires zimcheck binary in PATH)
    └── test_zim_readback.py         # Tests 8-9 (requires libzim.reader.Archive)
```

### Running the Test Matrix

```bash
# All 84 existing + 12 new export tests:
uv run pytest tests/unit/test_zim_writer.py tests/unit/test_zim_metadata.py -v

# With zimcheck integration (requires apt install zim-tools or brew install zim-tools):
uv run pytest tests/integration/test_zimcheck_validation.py -v -m integration

# Full export suite:
uv run pytest tests/ -k "zim" -v
```

---

## Integration Sequence with Phase 4 Federation

Phase 4 delivered the federation infrastructure. ZimWriter connects to it at exactly one point: the content query.

### Step-by-Step Integration Sequence

```
Step 1: Create feature branch
  git checkout -b feature/zimwriter-libzim-integration

Step 2: Add dependency
  Edit pyproject.toml — add "libzim>=3.2,<4.0" to [project.dependencies]
  uv pip install libzim  (verify wheel installs, no compile step)

Step 3: Add ArticleItem class
  Edit app/services/export/zim_writer.py
  Add import guard for libzim at top
  Add ArticleItem class before ZimWriter class

Step 4: Replace stub in create_zim()
  Edit ZimWriter.create_zim() — replace _stub_write_placeholder() with
  the Creator context manager block

Step 5: Implement _apply_metadata_to_creator()
  Replace the pass-only method body with all creator.add_metadata() calls
  Add _FALLBACK_ILLUSTRATION_PNG constant at module level

Step 6: Run existing 84 tests
  uv run pytest tests/ -k "export" -v
  All should pass — stub swaps out without changing public interface

Step 7: Run new integration tests
  Install zimcheck: apt-get install zim-tools (or brew install zim-tools)
  uv run pytest tests/integration/test_zimcheck_validation.py -v
  All should pass with exit code 0

Step 8: Manual end-to-end test (required before PR)
  Generate a small export (10-50 articles) from real DB
  Download Kiwix Android (F-Droid)
  Transfer ZIM to phone, open in Kiwix
  Verify: articles display, search returns results, offline read works

Step 9: Delete stub method
  Remove _stub_write_placeholder() from zim_writer.py
  Re-run all tests to confirm nothing breaks

Step 10: Create export API endpoint (if not already present)
  Create app/api/v1/export.py with POST /api/exports and GET /api/exports/{job_id}
  Wire to ZimWriter via ExportJob BackgroundTask

Step 11: Add ZimExport Alembic migration
  alembic revision --autogenerate -m "add_zim_exports_table"
  Review generated migration; apply: alembic upgrade head

Step 12: Update README and CONTRIBUTING
  Reflect Phase 5 status, test count, next steps

Step 13: PR creation
  Title: "feat(phase-5): activate libzim integration in ZimWriter"
  Must not merge to main until Phase 4 PR #1 has landed
```

### Phase 4 Code Consumed by ZimWriter

| Phase 4 artifact | How ZimWriter uses it |
|-----------------|----------------------|
| `content_items` table | Queried for items where `is_local=True` (or `domain=X` for domain exports) |
| `FederationPartner` model | Source node name/URL written to ZIM attribution footers for federated items |
| HTTP signature key infrastructure | Not directly used by ZimWriter; used by the federation sync layer (Wave 5.2) |

---

## Risk Assessment

### Risk 1: libzim wheel not available for CI or Raspberry Pi ARM64
**Probability**: Low-to-medium  
**Impact**: High — blocks CI and deployment  
**Detection**: `uv pip install libzim` fails with "no matching distribution"  
**Mitigation**:
- libzim 3.7.0 ships pre-built wheels for `manylinux2014_aarch64` (covers Raspberry Pi 5 running 64-bit OS)
- If wheel is missing: use `pip install libzim --no-binary :all:` to build from source (adds 5-10 minutes to CI)
- Worst case: `--no-build-isolation` flag with `apt-get install libzim-dev` in CI before the wheel build
- Always test wheel installation as the first CI step, before any test runs

### Risk 2: zimcheck fails on valid-seeming ZIM
**Probability**: Low-to-medium  
**Impact**: High — exports fail validation  
**Detection**: `zimcheck output.zim` returns non-zero exit code  
**Common causes**:
- Title > 30 characters (zimcheck warning, not failure in newer versions, but older zimcheck treats it as failure)
- Description > 80 characters (hard failure)
- Missing or wrong-size Illustration (hard failure in strict mode)
- Non-ASCII characters in Name metadata field (must be lowercase alphanumeric + hyphens + underscores)
- Empty article title on any front article (Xapian indexing requires non-empty title)
**Mitigation**:
- Run `zimcheck --verbose` to get specific error messages
- Compare against a known-good ZIM (Wikipedia English download) using `zimcheck` flags
- `ZimMetadata.validate()` already checks description length and name format before ZIM creation begins
- The `_FALLBACK_ILLUSTRATION_PNG` covers the missing-illustration case

### Risk 3: Xapian indexing produces corrupt or oversized index
**Probability**: Low  
**Impact**: Medium — ZIM opens but search is broken  
**Detection**: `zimcheck` fails with Xapian-related error, or `Archive.search()` returns empty results for known keywords  
**Mitigation**:
- Disable indexing as a diagnostic step: `creator.config_indexing(False, "eng")` — produces valid ZIM without search
- Ensure all articles have non-empty titles before passing to `ArticleItem.get_title()`
- `ZimEntry.__post_init__()` already raises `ValueError` for empty front-article titles

### Risk 4: HTML rendering produces external dependencies
**Probability**: Low (templates are already written to be self-contained)  
**Impact**: High — zimcheck rejects ZIM  
**Detection**: `test_html_no_external_dependencies` test fails; zimcheck reports external link error  
**Mitigation**:
- Add BeautifulSoup scan in CI as a pre-write check (scan rendered HTML for `http` in `src`/`href` attributes)
- The Jinja2 templates already embed CSS; the risk is in content HTML from the database that may contain absolute URLs in user-submitted content

### Risk 5: Memory exhaustion for large exports
**Probability**: Low (Phase 5 launch with <1000 items)  
**Impact**: Medium — export job OOM-killed  
**Detection**: Export job dies without completing; no ZimWriteResult returned  
**Mitigation**:
- Current implementation buffers all entries before calling `creator.add_item()`. At <1000 items, typical HTML is ~5-50KB each = 5-50MB in memory, well within normal limits.
- The `TODO(post-PR-merge)` in `add_article()` notes a streaming mode for future optimization. Activate if the item count grows past ~5,000.

### Risk 6: Concurrent export jobs conflict
**Probability**: Medium (if APScheduler overlaps with manual trigger)  
**Impact**: Medium — duplicate or partial ZIM file  
**Mitigation**:
- Add a lock mechanism in the ExportJob: check `zim_exports` for any row with `status='generating'` for the same name+flavour before starting a new job
- APScheduler's `misfire_grace_time` prevents overlapping scheduled runs

---

## Deployment Gates and Go-Live Checklist

See `PHASE_5_IMPLEMENTATION_DECISION_TREE.md` for the shared go-live checklist.

### ZimWriter-Specific Pre-Deployment Verification

```
[ ] uv run pytest tests/ -k "export" -v — all 84 + new tests pass
[ ] zimcheck passes on a 50-article test export
[ ] ZIM opens in Kiwix Android (F-Droid) — articles display
[ ] ZIM opens in Kiwix Desktop — full-text search returns results for at least 3 keywords
[ ] ZIM opens in kiwix-serve (docker run kiwix/kiwix-serve) — accessible via localhost:8080
[ ] SHA-256 checksum verified: sha256sum -c *.sha256 passes
[ ] zim_exports Alembic migration applied cleanly (alembic upgrade head)
[ ] Export job API endpoint returns 200 and a valid job_id
[ ] CDN upload test: boto3 put_object to R2 bucket succeeds
[ ] Retention policy test: running two exports marks first as superseded
```

---

## Post-Launch Monitoring

### Metrics to Watch

| Metric | Tool | Alert threshold |
|--------|------|----------------|
| Export job completion rate | APScheduler + DB status | Alert if `status='generating'` row >90 minutes old |
| zimcheck pass rate | `zim_exports.zimcheck_passed` | Alert if `FALSE` on any automated export |
| Export generation time | `zim_exports.generation_duration_seconds` | Alert if >300 seconds (5 minutes) for nopic |
| ZIM file size | `zim_exports.file_size_bytes` | Alert if nopic >500 MB or <1 MB (indicates empty export) |
| CDN upload errors | boto3 exception logs | Alert on any upload failure (falls back to local path) |
| Xapian search quality | Manual monthly check | Verify top 10 search terms return relevant results |

### Health Check Endpoint

Add `GET /api/exports/health` returning:
```json
{
  "last_successful_export": "2026-05-19T02:03:14Z",
  "current_exports": [
    {"name": "open-repo_en_nopic", "period": "2026-05", "status": "available",
     "article_count": 487, "file_size_bytes": 23456789}
  ],
  "zimcheck_pass_rate_7d": 1.0
}
```

---

## Sources

- [python-libzim ReadTheDocs](https://python-libzim.readthedocs.io/en/latest/)
- [python-libzim GitHub](https://github.com/openzim/python-libzim)
- [python-libzim PyPI](https://pypi.org/project/libzim/)
- [openZIM ZIM format specification](https://wiki.openzim.org/wiki/ZIM_file_format)
- [openZIM Metadata specification](https://wiki.openzim.org/wiki/Metadata)
- [zimcheck tool](https://github.com/openzim/zim-tools)
- [Kiwix OPDS documentation](https://wiki.kiwix.org/wiki/OPDS)
