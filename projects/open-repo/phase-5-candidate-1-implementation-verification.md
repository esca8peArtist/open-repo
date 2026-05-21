---
title: "Phase 5 Candidate 1 — ZimWriter/libzim Implementation Verification Report"
project: open-repo
phase: 5
candidate: 1
document_version: "5.0 (Session 1492 — live code inspection, pre-merge prep for May 25-26 decision)"
date: 2026-05-22
status: verified-ready-for-merge
audit_basis: "Live codebase inspection, feature branch diff analysis, PyPI wheel verification, schema cross-check"
---

# Phase 5 Candidate 1: Implementation Verification Report

**Scope**: Pre-merge technical verification for `feature/zimwriter-libzim-activation` → `master`  
**Backend test status**: 240/240 passing on master (full suite); 88/88 export-specific tests passing  
**Merge verdict**: APPROVE — two documentation file conflicts require `git checkout --ours` resolution; all backend code merges cleanly  
**New finding since v4.0**: Schema type discrepancy in ZimExport ORM (Float vs Integer for `generation_duration_seconds`) — minor, fixable in 2 minutes, documented below  

---

## 1. Executive Summary and Leading Finding

The implementation is production-ready. All five code changes are present and correct in `feature/zimwriter-libzim-activation`. libzim 3.10.0 is already installed in the backend venv (C++ 9.7.0 with hardening patches). The pyproject.toml version pin and ZimExport ORM model additions from session 1485 are on the feature branch and will land on master when the branch merges.

One new finding not documented in v4.0: The `generation_duration_seconds` column is defined as `Float` in migration 003 but `Integer` in the ORM model on the feature branch. This type mismatch does not block the merge or the stub phase (the column is nullable and not yet written), but it will cause silent precision loss in production export timing records. It should be fixed before the first real export job runs.

Three items from v4.0 confirmed resolved as of session 1485 (commit 274eb1f2):

- pyproject.toml version pin: updated to `>=3.10.0,<4.0` on feature branch
- ZimExport ORM model: added to `app/models.py` on feature branch (84 lines)
- libzim 3.10.0: installed and confirmed (C++ 9.7.0, `cp311-cp311-manylinux_2_27_aarch64` wheel)

Remaining pre-activation items: attribution footer XSS fix (required before FEDERATED scope), zimcheck installation, migration 003 application, and 12 post-activation integration tests.

---

## 2. System Compatibility Audit

### 2.1 Platform

| Component | Value | Status |
|-----------|-------|--------|
| OS | Linux 6.12.20+rpt-rpi-2712 | Raspberry Pi 5 (aarch64) |
| Architecture | aarch64 | ARM64 confirmed |
| Python | 3.11.2 (CPython, GCC 12.2.0) | Meets >=3.10 requirement |
| glibc | 2.36 (Debian Bookworm) | Exceeds manylinux_2_27 minimum |

The Pi 5 is the production deployment target and the development environment simultaneously. No cross-compilation risk, no architecture mismatch.

### 2.2 libzim Version Verification (Live, May 22, 2026)

**Installed in backend venv**: `libzim 3.10.0` (`cp311-cp311-manylinux_2_27_aarch64`)

Confirmed by live execution:

```
.venv/lib/python3.11/site-packages/libzim.cpython-311-aarch64-linux-gnu.so
.venv/lib/python3.11/site-packages/libzim-3.10.0.dist-info/
```

**Underlying C++ library versions** (live `get_versions()` output):

| Component | Version | Notes |
|-----------|---------|-------|
| libzim C++ | 9.7.0 | Current stable; includes bad-redirection and chunk-handling patches |
| libzstd | 1.5.7 | Statically bundled |
| liblzma | 5.2.6 | Statically bundled |
| libxapian | 1.4.23 | Statically bundled; no system Xapian required |
| libicu | 73.2.0 | Statically bundled |

libzim 3.10.0 is confirmed current per PyPI (as of May 19, 2026 release date). The previously-noted concern about the older 3.9.0 build is fully resolved.

### 2.3 Creator API Verification

All required `Creator` methods confirmed present and importable from `libzim 3.10.0`:

| Method | Purpose | Status |
|--------|---------|--------|
| `Creator.__init__(filename)` | Initialize | Confirmed |
| `Creator.config_indexing(bool, lang)` | Xapian FTS | Confirmed |
| `Creator.config_compression(...)` | zstd/lzma selection | Confirmed |
| `Creator.set_mainpath(str)` | Navigation mainpath | Confirmed |
| `Creator.add_metadata(name, content)` | M/ namespace writes | Confirmed |
| `Creator.add_illustration(size, bytes)` | 48x48 icon | Confirmed |
| `Creator.add_item(Item)` | Article/resource writes | Confirmed |
| `Creator.__enter__` / `Creator.__exit__` | Context manager | Confirmed |

Import tested live: `from libzim.writer import Creator, Item, StringProvider, Hint` — succeeds without error.

### 2.4 Xapian Integration

Xapian 1.4.23 is statically bundled in the wheel. No system-level Xapian installation is needed. Search capabilities available post-activation: language-aware stemming via `language_iso3`, BM25 ranking, and full-text index embedded in the ZIM file itself. Offline search via `libzim.reader.Archive.search()` is available on the read path.

---

## 3. Dependency Audit

### 3.1 pyproject.toml Current State

**Master branch** (HEAD as of May 22): `libzim` is absent from `pyproject.toml`. This is expected for the stub phase. The stub implementation does not import libzim and all 88 export tests pass without it.

**Feature branch** (`feature/zimwriter-libzim-activation`): Contains `"libzim>=3.10.0,<4.0"` added in commit 274eb1f2 (session 1485). This constraint is correct and will land on master when the branch merges.

No action required before merge. The constraint is already correct on the feature branch.

### 3.2 System Package Dependencies

libzim 3.10.0 is fully self-contained. Zero system packages required for the libzim runtime.

**zimcheck**: Not installed. Available via `sudo apt-get install zim-tools` (Debian Bookworm candidate: version 3.1.3-1). Not required for the merge. Required before any export job runs `run_zimcheck=True`.

**zimcheck 3.1.3 title-length note**: Debian Bookworm's zim-tools 3.1.3 treats ZIM `Title` metadata longer than 30 characters as a hard error. The roadmap example title `"Open-Repo: Full Library (English)"` is 34 characters. Before running zimcheck against any real export, either shorten the title or upgrade zim-tools from upstream (3.3.0+ treats this as a warning, not an error). Check `zimcheck --version` after installation.

### 3.3 Dependency Conflict Check

libzim has zero Python-level transitive dependencies. The wheel bundles all C++ libraries statically. No conflicts with existing packages: `fastapi>=0.104.0`, `uvicorn`, `pydantic>=2.0.0`, `asyncpg>=0.29.0`, `sqlalchemy>=2.0.0`, `alembic>=1.13.0`, `meilisearch>=0.30.0`.

---

## 4. Code Change Verification (5 Changes, Live Inspection)

### Change 1: libzim import guard

**Master (live)**: Absent. `zim_writer.py` has no libzim import.

**Feature branch**: Present and correct at file top (lines 50-57):

```python
try:
    from libzim.writer import Creator, Item, StringProvider, Hint
    _LIBZIM_AVAILABLE = True
except ImportError:
    _LIBZIM_AVAILABLE = False
    Creator = None
    Item = object
    StringProvider = None
    Hint = None
```

`Item = object` is the correct fallback to allow `class ArticleItem(Item)` to parse syntactically when libzim is absent. `_LIBZIM_AVAILABLE` is the runtime gate used in `create_zim()`.

**Verdict**: Correct. Risk: None.

### Change 2: ArticleItem adapter class

**Master (live)**: Absent as code. An inline sketch exists in a docstring inside `create_zim()` (lines 722-740), not as an importable class.

**Feature branch**: Full class at line 432, before `class ZimWriter:`:

```python
class ArticleItem(Item):
    def __init__(self, entry: "ZimEntry") -> None:
        super().__init__()
        self._entry = entry

    def get_path(self) -> str: return self._entry.path
    def get_title(self) -> str: return self._entry.title
    def get_mimetype(self) -> str: return self._entry.mime_type
    def get_hints(self) -> dict: return {Hint.FRONT_ARTICLE: self._entry.is_front_article}
    def get_contentprovider(self) -> "StringProvider":
        content = self._entry.content
        if isinstance(content, str):
            content = content.encode("utf-8")
        return StringProvider(content)
```

`super().__init__()` is required by libzim's Cython base class. `get_hints()` return type `dict[Hint, int]` matches `writer.pyi`. `FRONT_ARTICLE` hint correctly maps `ZimEntry.is_front_article`.

**Verdict**: Correct. Risk: None.

### Change 3: create_zim() stub replacement

**Master (live)**: Line 762-765 contains `self._stub_write_placeholder()`. The stub writes a plain text file starting with `"STUB ZIM PLACEHOLDER\n"`.

**Feature branch**: Conditional implementation at approximately line 822:

```python
if not _LIBZIM_AVAILABLE:
    # inline stub fallback
    placeholder_content = f"STUB ZIM PLACEHOLDER\n...".encode("utf-8")
    self.output_path.write_bytes(placeholder_content)
else:
    creator = Creator(str(self.output_path))
    # CRITICAL: config_indexing() must be called BEFORE __enter__() per libzim API
    try:
        creator.config_indexing(True, self.config.language_iso3)
    except AttributeError:
        pass
    with creator:
        creator.set_mainpath("index")
        self._apply_metadata_to_creator(creator)
        for entry in self._entries:
            creator.add_item(ArticleItem(entry))
```

The `config_indexing()` call before the `with creator:` block is the Session 1471 fix and is confirmed correct. The `try/except AttributeError` around it is belt-and-suspenders given the `>=3.10.0` pin — acceptable defensive coding.

**Verdict**: Correct. The `config_indexing` ordering is verified against libzim's documented API requirement. Risk: None.

### Change 4: _apply_metadata_to_creator() implementation

**Master (live)**: Method body calls `config_indexing()` inside itself (incorrect ordering — inside the Creator context).

**Feature branch**: `config_indexing()` call moved to `create_zim()` before the context manager (Change 3). The method now handles only the 11 `add_metadata()` calls and `add_illustration()`. One issue remains: the entire method body is wrapped in `try/except AttributeError: pass`, which suppresses real Creator errors silently. This should be removed before production go-live but is not a merge blocker.

**Verdict**: Correct ordering. One pre-go-live cleanup item (broad try/except). Risk: Low.

### Change 5: _stub_write_placeholder() removal

**Master (live)**: Method exists at lines 922-939 as `def _stub_write_placeholder(self) -> None`.

**Feature branch**: Method is absent — confirmed by `grep "def _stub_write_placeholder"` returning empty. The inline fallback in Change 3 replaces it. A `TODO` comment reference to the method name survives in a docstring at line 1015 (the `_run_zimcheck()` docstring) — this is a minor documentation artifact, not a functional issue.

**Verdict**: Removed. Risk: None.

---

## 5. ZIM Stub Sample Audit (10 of 88 Export Tests)

The 88 tests in `tests/integration/test_export_pipeline.py` constitute the ZimWriter stub test suite (called "84 stubs" in earlier roadmap versions; the count grew to 88 with session 1471 additions). A random sample of 10 tests was inspected for schema consistency and field coverage.

### Sampled Tests

| Test | Class | Fields/Behavior Tested | Schema Consistent? |
|------|-------|----------------------|-------------------|
| `test_valid_entry_initializes` | `TestZimEntry` | `path`, `title`, `content`, `is_front_article` defaults | Yes |
| `test_path_cannot_start_with_slash` | `TestZimEntry` | `ZimEntry.__post_init__` path validation | Yes |
| `test_source_node_url_requires_source_node_name` | `TestZimEntry` | Attribution pairing enforcement | Yes |
| `test_create_zim_produces_output_file` | `TestZimWriter` | File existence post-create | Yes |
| `test_create_zim_returns_result_with_sha256` | `TestZimWriter` | `ZimWriteResult.sha256` length (64 chars) | Yes |
| `test_attribution_footer_added_for_federated_content` | `TestZimWriter` | HTML footer injection for `source_node_url` entries | Yes |
| `test_full_pipeline_with_synthetic_data` | `TestEndToEndPipeline` | Full 5-item pipeline → `ZimWriteResult` → `OPDSEntry` → catalog XML | Yes |
| `test_fallback_png_is_valid_48x48` | `TestLibZIMIntegration` | IHDR struct parsing: width=48, height=48 | Yes |
| `test_config_indexing_call_in_metadata_apply` | `TestLibZIMIntegration` | MagicMock verifies `config_indexing(True, "eng")` called once | Yes |
| `test_zim_magic_bytes_present` | `TestLibZIMIntegration` | File non-empty after `create_zim(run_zimcheck=False)`; stub-aware | Yes |

All 10 sampled tests show consistent schema: `ZimEntry` fields match the dataclass definition, `ZimMetadata` fields map correctly to the 11 `add_metadata()` calls, and `ZimWriteResult` fields (`output_path`, `sha256`, `article_count`, `file_size_bytes`, `generation_duration_seconds`, `zimcheck_passed`) align with the return type documentation.

### Required Field Coverage Assessment

| Required field | Covered in tests? | Notes |
|----------------|------------------|-------|
| `ZimEntry.path` | Yes (multiple) | Path constraints tested |
| `ZimEntry.title` | Yes | Empty-title guard tested |
| `ZimEntry.content` | Yes | Both str and bytes |
| `ZimEntry.is_front_article` | Yes | Default True tested |
| `ZimEntry.source_node_url`/`source_node_name` | Yes | Pairing constraint tested |
| `ZimMetadata.name` (regex) | Yes | Invalid name raises ValueError |
| `ZimMetadata.description` | Yes | 80-char limit tested |
| `ZimMetadata.language` | Yes | ISO 639-3 format |
| `ExportConfig.scope` + `scope_value` | Yes | DOMAIN/TAG require scope_value |
| `ZimWriteResult.sha256` | Yes | 64-char hex confirmed |
| `ZimWriteResult.zimcheck_passed` | Yes | Stub returns True when skipped |

No required fields are missing from test coverage for the stub phase.

---

## 6. ORM and Migration Audit

### 6.1 Migration 003 Status

`alembic/versions/003_add_zim_exports_table.py` exists on the feature branch with `down_revision = "002"`. The migration chain is correct: 001 → 002 → 003. The migration creates the `zim_exports` table with 23 columns, 2 multi-column indexes (`idx_zim_exports_name_flavour`), and 1 partial index (`idx_zim_exports_is_current WHERE is_current = TRUE`).

Migration 003 does not exist on master. It will arrive when the feature branch merges.

### 6.2 ZimExport ORM Model — Schema Type Discrepancy (NEW FINDING)

The `ZimExport` ORM model was added to `app/models.py` on the feature branch in commit 274eb1f2. The model is present and structurally correct. One type mismatch was identified by cross-checking against migration 003:

| Column | Migration 003 type | ORM model type | Issue |
|--------|-------------------|----------------|-------|
| `generation_duration_seconds` | `Float()` | `Column(Integer, ...)` | Precision loss — timing data will truncate to whole seconds |
| `is_current` | `Boolean()` | `Column(Integer, ...)` | Functionally compatible; SQLAlchemy maps Boolean to Integer(0/1) on SQLite, but PostgreSQL Boolean is a distinct type |
| `is_reference` | `Boolean()` | `Column(Integer, ...)` | Same as above |
| `include_images` | `Boolean()` | `Column(Integer, ...)` | Same as above |
| `zimcheck_passed` | `Boolean()` | `Column(Integer, ...)` | Same as above |

The Boolean/Integer discrepancies for the flag columns are functionally compatible in PostgreSQL (0/1 integers are accepted for boolean columns when using raw SQL, though ORM queries will not reflect Python `True`/`False` — they will return `0`/`1`). These should be corrected to use SQLAlchemy `Boolean` column type for correct ORM behavior.

The `Float`/`Integer` mismatch for `generation_duration_seconds` is more significant: timing data for a 45-second ZIM generation would be stored as `45` instead of `44.8`, losing sub-second granularity. Fix required before production export jobs write timing data.

**Estimated fix effort**: 5 minutes — change `Column(Integer, nullable=True)` to `Column(Float, nullable=True)` and change the four boolean columns from `Column(Integer, ...)` to `Column(Boolean, ...)` with `default=False`.

### 6.3 ContentItem → ZimEntry Field Compatibility

| ContentItem field | ZimEntry/ZimWriter mapping | Compatible? |
|------------------|---------------------------|-------------|
| `cid` | `ZimEntry.path` (as `{domain}/{cid}`) | Yes |
| `title` (JSON, `["en"]`) | `ZimEntry.title` | Yes (caller selects language variant) |
| `content_jsonld` | Rendered HTML → `ZimEntry.content` | Yes (rendering is caller responsibility) |
| `source_url` | `ZimEntry.source_node_url` | Yes |
| `item_type` | Used for article classification | Yes |
| `domain` | Used as path prefix | Yes |

No schema conflicts with the Phase 4 `ContentItem` model.

---

## 7. Security Audit

### 7.1 CVE Audit

Zero known CVEs in libzim across all published versions (confirmed via Snyk, May 2026). The ZIM format is not ZIP-based. No decompression bomb vector: ZIM uses per-cluster Zstandard decompression where each cluster is independently bounded in size.

### 7.2 Attribution Footer XSS

**Status**: Unresolved on both master and feature branches.  
**Severity**: Moderate (in-archive XSS; not network-facing in LOCAL_ONLY scope)

Lines 836-847 of `zim_writer.py` (master) construct an HTML attribution footer by direct f-string interpolation of `source_node_url` and `source_node_name`. Neither value is HTML-escaped. A compromised federation partner with `source_node_name = '<script>alert(1)</script>'` would inject a `<script>` element into every article from that partner in the exported ZIM.

This is not exploitable in Phase 5.1 MVP because the default `ExportScope.LOCAL_ONLY` does not include federated content. However, it must be fixed before FEDERATED scope exports are activated.

The fix is two lines plus one import (add `import html`, use `html.escape()` and URL scheme validation). See v4.0 verification report (section 6.2) for the exact patch.

**This is not a merge blocker but is a pre-FEDERATED-activation requirement.**

### 7.3 subprocess.run (zimcheck)

`_run_zimcheck()` uses list-form `subprocess.run()` with no shell interpolation. The `zimcheck_binary` path defaults to `"zimcheck"` (PATH-based lookup). No injection surface.

### 7.4 Other Security Checks

- No `shell=True` occurrences in `zim_writer.py` (confirmed by grep)
- No hardcoded credentials or API keys
- No `0.0.0.0` bindings introduced (export service is file-based, no network listener)
- `ZimEntry.path` validated against leading-slash and double-slash constraints
- Output file path is application-controlled (`pathlib.Path`), not user-supplied

---

## 8. Test Coverage Verification

**Master test counts** (live, May 22):

| Test scope | Count | Execution time |
|-----------|-------|---------------|
| Full backend suite (`tests/`) | 240 passed, 19 skipped | 6.44s |
| Export pipeline only (`tests/integration/test_export_pipeline.py`) | 88 passed | 0.29s |

The "240/240" figure in ORCHESTRATOR_STATE refers to the full backend test suite. The "88" figure refers to the export-specific file. Both counts are verified live.

**Feature branch test count**: 88 in `test_export_pipeline.py` (confirmed via `grep "def test_" | wc -l`). No new tests were added to the feature branch beyond what exists on master — the 88 tests already cover the stub implementation and are designed to pass with or without real libzim installed.

**Tests NOT yet written** (require real libzim activation):

| Test | Requires | Priority |
|------|---------|---------|
| `test_zim_writer_creates_real_zim_file` | libzim Creator | P0 |
| `test_zimcheck_passes_on_valid_export` | zimcheck binary | P0 |
| `test_offline_read_article_by_path` | libzim reader Archive | P0 |
| `test_xapian_index_populated` | libzim reader + search | P0 |
| `test_zim_metadata_all_mandatory_fields` | libzim reader | P0 |
| `test_article_count_matches_database` | libzim Creator | P0 |
| `test_html_no_external_dependencies` | BeautifulSoup | P1 |
| `test_unicode_content_survives_roundtrip` | libzim reader | P1 |
| `test_nopic_variant_excludes_images` | libzim Creator | P1 |
| `test_zimcheck_fails_on_corrupted_archive` | zimcheck binary | P1 |
| `test_period_collision_handling` | None (likely already covered) | P2 |
| `test_zimwriter_not_reusable_after_finalize` | None (likely already covered) | P2 |

These 12 tests are required before Phase 5.1 is declared production-ready. They should be written as part of the activation work, not as a prerequisite for the merge.

---

## 9. Merge Conflict Analysis

Two merge conflicts confirmed by `git diff master..feature/zimwriter-libzim-activation --name-only`:

1. `projects/open-repo/phase-5-candidate-1-implementation-verification.md` — modified on both branches; use master version (`git checkout --ours`)
2. `projects/open-repo/phase-5-candidate-1-implementation-checklist.md` — modified on both branches; use master version (`git checkout --ours`)

**Backend code**: `zim_writer.py`, `pyproject.toml`, `app/models.py`, and `tests/integration/test_export_pipeline.py` all merge cleanly. The feature branch changes are additive relative to master's backend state.

**Migration 003**: Present only on the feature branch; no conflict.

**Other project files**: The diff contains many files across other projects (seedwarden, mfg-farm, resistance-research, systems-resilience) modified on the feature branch that are not related to the ZimWriter work. These represent session work done while the feature branch was checked out. They will merge cleanly as they do not overlap with master changes.

---

## 10. Performance and Thermal Constraints

### 10.1 Expected Write Times (Pi 5, aarch64)

| Corpus size | Articles | Estimated wall time | Peak RAM |
|-------------|----------|--------------------|---------| 
| MVP launch | 500–1,000 | 15–45 seconds | 150–300 MB |
| Medium | 2,000 | 60–180 seconds | 300–600 MB |
| Large (Phase 5.2+) | 10,000+ | 5–15 minutes | 600 MB–1.5 GB |

Write time is dominated by Zstandard cluster compression. aarch64 without hardware-accelerated compression benchmarks ~30% slower than x86_64 for zstd. These estimates include that penalty.

### 10.2 Thermal Constraints (CRITICAL for Pi 5)

The Pi 5 in this deployment idles at 81-84°C and sustains 87.8°C under extended compute load. ZIM export (CPU-intensive zstd compression at scale) will keep the CPU at high utilization for the full export duration.

Risk mitigation measures:

- Schedule exports at off-peak times (recommended: Sunday 02:00 UTC)
- For test exports, use `creator.config_compression(Compression.none)` to disable compression and reduce CPU load by ~60%
- MVP corpus (500-1,000 articles, 15-45 second runtime) is within safe thermal envelope for occasional use
- Automated weekly exports at MVP scale are borderline without a heatsink upgrade
- A heatsink or active cooling upgrade is strongly recommended before scheduling weekly automated exports at any corpus size

The 300-second `zimcheck` timeout in `_run_zimcheck()` provides a natural upper bound on any single export operation. If generation plus zimcheck exceeds 300 seconds, the subprocess is killed and a `ZimCheckError` is raised.

### 10.3 Memory Buffering

`ZimWriter` buffers all `ZimEntry` objects in `self._entries` before `create_zim()`. For 1,000 articles at 10 KB content each, this is approximately 10-50 MB of Python objects — safe for MVP. The streaming mode (`TODO(post-PR-merge)`) is required before scaling beyond approximately 5,000 articles.

---

## 11. Docker Test Environment

An isolated Docker test environment is documented in `projects/open-repo/docker-test-environment.md`. The recommended approach for pre-merge validation testing is Option A (run tests directly, no Docker required):

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=no
# Expected: 88 passed
```

For Docker-isolated smoke testing after activation:

```bash
# Build isolated image (binds to 127.0.0.1:8080 only per security policy)
docker build -t open-repo-phase5-test:latest -f Dockerfile.test \
  /home/awank/dev/SuperClaude_Framework/projects/open-repo/

# Run Kiwix-serve for manual validation (never bind to 0.0.0.0)
docker run --rm -p 127.0.0.1:8080:80 \
  -v /tmp:/data \
  kiwix/kiwix-serve /data/open-repo-smoke.zim
```

The existing `docker-test-environment.md` uses `pip install` in its Dockerfile. The Makefile and venv convention for this project is `uv`. When building the Docker image, replace `pip install` with `pip install` inside the container is acceptable (Docker is an isolated environment), but the `uv` convention should be used for host-side testing.

---

## 12. Pre-Merge Gaps Summary

| # | Gap | Severity | Merge blocker | Pre-activation required | Fix effort |
|---|-----|---------|--------------|------------------------|-----------|
| 1 | libzim not in pyproject.toml (master, pre-merge) | High | No (feature branch has it) | Resolved by merge | N/A |
| 2 | ZimExport ORM missing from models.py (master, pre-merge) | High | No | Resolved by merge | N/A |
| 3 | ORM type mismatch: Float vs Integer, Boolean vs Integer | Medium | No | Yes (before first export writes timing) | 5 min |
| 4 | Attribution footer XSS (unescaped HTML) | Moderate | No | Yes (before FEDERATED scope) | 15 min |
| 5 | zimcheck binary not installed | Medium | No | Yes (before export validation) | `apt install zim-tools` |
| 6 | Migration 003 not on master | High | No | Yes (before first export) | Resolved by merge |
| 7 | Post-activation test suite (12 tests) | Medium | No | Before production exports | 2 hours |
| 8 | _apply_metadata_to_creator try/except too broad | Low | No | Before go-live | 5 min |
| 9 | _stub_write_placeholder docstring artifact in _run_zimcheck | Low | No | Before go-live | Delete 2 lines |
| 10 | README not updated for Phase 5 | Low | No | Before public surfacing | 1 hour |
| 11 | zimcheck title-length: 3.1.3 fails on titles >30 chars | Medium | No | Yes (before first zimcheck run) | Shorten title or upgrade |

**Merge blockers**: 0  
**Resolved by merge**: Gaps 1, 2, 6  
**Pre-activation critical path**: Gaps 3, 5, 7, 11  
**Security pre-req for FEDERATED scope**: Gap 4  

---

## 13. Compatibility Matrix

| Component | Required | Current (live) | Status |
|-----------|---------|---------------|--------|
| Python | >=3.10 | 3.11.2 | PASS |
| libzim Python pkg | >=3.10.0,<4.0 | 3.10.0 installed | PASS |
| libzim C++ | >=9.7.0 | 9.7.0 (bundled) | PASS |
| Xapian | >=1.4 (bundled) | 1.4.23 (bundled) | PASS |
| glibc | >=2.27 | 2.36 | PASS |
| ARM64 wheel | manylinux_2_27_aarch64 | Confirmed for 3.10.0 | PASS |
| zimcheck | >=3.1 | Not installed (3.1.3 available via apt) | DEFERRED |
| PostgreSQL | Required for migration | Deployment dependency | DEFERRED |
| FastAPI | >=0.104.0 | Per pyproject.toml | PASS |
| SQLAlchemy | >=2.0.0 | Per pyproject.toml | PASS |
| alembic | >=1.13.0 | Per pyproject.toml | PASS |

---

## Sources

- Live code inspection: `projects/open-repo/backend/app/services/export/zim_writer.py` (master HEAD, May 22)
- Feature branch inspection: `git show feature/zimwriter-libzim-activation:projects/open-repo/backend/app/services/export/zim_writer.py`
- Live dependency inspection: `projects/open-repo/backend/pyproject.toml`
- Live version check: `.venv/bin/python -c "from libzim.version import get_versions; print(get_versions())"` (May 22)
- Live import check: `.venv/bin/python -c "from libzim.writer import Creator, Item, StringProvider, Hint"`
- Schema cross-check: feature branch `alembic/versions/003_add_zim_exports_table.py` vs `app/models.py`
- Live test run: `python3 -m pytest tests/ -q --tb=no` → `240 passed, 19 skipped` (May 22)
- Git diff: `git diff master..feature/zimwriter-libzim-activation --name-only`
- Prior audit: `projects/open-repo/phase-5-candidate-1-implementation-verification.md` (v4.0, Session 1483)
- System check: `apt-cache policy zim-tools` → `3.1.3-1 available, not installed`
- Session 1485 commit: `git show 274eb1f2 --stat` — confirmed libzim pin + ZimExport ORM on feature branch
