---
title: "Phase 5 Candidate 1 (ZimWriter/libzim) — Pre-Decision Implementation Verification"
project: open-repo
phase: 5
candidate: 1
document_type: feasibility-verification
status: complete
date: 2026-05-22
session: research-agent
supersedes: "PHASE_5_CANDIDATE_1_IMPLEMENTATION_VERIFICATION_v3.md"
confidence: high
target_decision: "2026-05-23 to 2026-05-24"
effort_estimate: "8-11 hours implementation"
---

# Phase 5 Candidate 1: Implementation Verification Report

**Prepared**: 2026-05-22 (research agent, live system audit)
**Decision target**: May 23-24 (user approval of Phase 5 direction)
**Purpose**: Fresh audit of Candidate 1 (ZimWriter/libzim activation) feasibility ahead of user decision. Prior v3 report (Session 1444, May 21) covered most ground; this report extends with live re-verification of the current codebase state, complete stub sample validation with a new seed, and an updated implementation checklist.

---

## Most Important Finding First

Candidate 1 is feasible and the majority of the hard work is already done. libzim 3.10.0 is installed, importable, and confirmed working on the Pi 5 aarch64 hardware. The 88-test suite passes cleanly. The corpus (32 articles) is clean. **Three concrete blockers remain before a ZIM file can actually be written**: (1) `libzim` is absent from `pyproject.toml`, (2) the `_stub_write_placeholder()` call in `create_zim()` must be replaced with the real Creator pattern, and (3) the `config_indexing()` call must be moved to before the Creator context manager entry. None of these are difficult — the code for all three is written and ready to paste in. Total implementation time for the core activation (Changes 1-4): 2-4 hours.

A fourth confirmed blocker exists for full production readiness: `zimcheck` binary is not installed. This gates the validation loop but does not block proving ZIM output correctness via magic bytes verification.

---

## Section 1: libzim Python Binding Audit

### 1.1 Installed Versions — Live Verification (2026-05-22)

| Component | Version | Verification method |
|-----------|---------|-------------------|
| libzim Python package | **3.10.0** | `importlib.metadata.version('libzim')` |
| libzim C++ bundled library | **9.7.0** | `from libzim.version import get_libzim_version; get_libzim_version()` |
| Python runtime | 3.11.2 (CPython) | `python --version` |
| Platform | aarch64 (Raspberry Pi 5) | `uname -m` |
| Wheel platform tag | `manylinux_2_27_aarch64.manylinux_2_28_aarch64` | dist-info WHEEL file |

All four writer classes confirmed importable without error:

```
from libzim.writer import Creator, Item, StringProvider, Hint  # OK
libzim C++ core: 9.7.0  # via get_libzim_version()
```

The `libzim` package does **not** expose `libzim.__version__` — this raises `AttributeError`. Use `importlib.metadata.version('libzim')` instead. The roadmap's example command (`python -c "import libzim; print(libzim.__version__)"`) will fail; this is a documentation error, not a blocker.

### 1.2 Xapian — System Package vs. Bundled

`import xapian` raises `ModuleNotFoundError` — the system Xapian Python binding is not installed, and `pkg-config --modversion xapian-core` returns nothing. **This is correct and expected.** libzim bundles its own Xapian C++ library inside the wheel. The Xapian full-text search index is created internally by the libzim C++ layer when `creator.config_indexing(True, 'eng')` is called before the context manager entry. No system Xapian package is required. The `python-xapian` binding is irrelevant to ZimWriter.

### 1.3 Version Compatibility with March 2026 Releases

The roadmap pins `libzim>=3.2,<4.0`. libzim 3.10.0 (current, installed) was released approximately April-May 2026. The pyproject.toml on local master does **not yet declare libzim as a dependency** — verified live: the `[project.dependencies]` list in `backend/pyproject.toml` contains no libzim entry. libzim 3.10.0 is only in the venv because it was manually installed in a prior session.

On `open-repo/main` (remote), the prior Session 1500 audit confirmed the pin is `libzim>=3.2,<4.0`. The recommended pin for any new declaration is `libzim>=3.10.0,<4.0` to match the tested version.

**Compatibility verdict**: Full compatibility confirmed. No source-build fallback needed. No system Xapian needed. The wheel installs cleanly on the Pi 5 aarch64.

### 1.4 Critical API Ordering Bug: config_indexing Must Precede the Context Manager

**This is the single most operationally critical finding across all prior audits, and it remains unresolved in local master.**

In libzim 3.9.0+ (confirmed via live test in Session 1444), calling `creator.config_indexing()` **inside** a `with creator:` block raises `RuntimeError: Creator started`. The docstring embedded in `create_zim()` at lines 735-741 shows the wrong pattern — `config_indexing` is shown inside the `with creator:` block.

The correct pattern, verified working against libzim 3.9.0 on this hardware:

```python
creator = Creator(str(self.output_path))
creator.config_indexing(True, self.config.language_iso3)  # BEFORE __enter__
creator.set_mainpath("index")                             # BEFORE __enter__
with creator:
    self._apply_metadata_to_creator(creator)
    for entry in self._entries:
        creator.add_item(ArticleItem(entry))
# Creator.__exit__ triggers ZIM file write
```

Additionally, `_apply_metadata_to_creator()` at lines 873-904 currently calls `creator.config_indexing()` at line 886, **inside** its method body (which is called inside the `with creator:` block). This will raise `RuntimeError: Creator started`. The `except AttributeError: pass` guard at line 903 does **not** catch `RuntimeError`, so the exception propagates and causes `create_zim()` to fail entirely.

**Fix required**: Remove the `config_indexing()` call from `_apply_metadata_to_creator()`. Remove the `except AttributeError: pass` guard entirely. Move both pre-configuration calls to before the `with creator:` entry in `create_zim()`.

---

## Section 2: ZIM Stub Validation — Random Sample of 10

### 2.1 Corpus Overview

The content corpus is `data/openfarm_procedures.jsonl` — 32 records, sourced from the OpenFarm import pipeline (Phase 3). There is no separate "stub" file; these 32 records are the MVP ZIM export input.

### 2.2 Schema Validation — 10-Record Sample (Seed 99, fresh for this audit)

| Result | CID (last 16 chars) | Title | Steps |
|--------|---------------------|-------|-------|
| PASS | d347176ec853176f | Growing Beets: Root and Leaf | 3 |
| PASS | c38b605321f98c8c | Growing Kale Through the Seasons | 3 |
| PASS | cd2f5f44e4545ce3 | Growing Cucumbers: Heat, Water, and Consisten... | 4 |
| PASS | db83a835fac85838 | Growing Bush Beans: The Beginner's Protein Ga... | 3 |
| PASS | 1c2d4a20cb5a5045 | Growing Cherry Tomatoes from Seed to Harvest | 5 |
| PASS | f50620562af1006c | Growing Basil: From Seed to Kitchen | 3 |
| PASS | bc4aef9e81a22869 | Establishing Rosemary as a Long-Lived Garden... | 3 |
| PASS | 954a487d947eaa23 | Growing Carrots: Soil Preparation and Thinning | 4 |
| PASS | 399240c7e127640f | Lettuce: Succession Planting for Year-Round S... | 3 |
| PASS | 383cba9fab1a9455 | Growing Onions from Sets | 3 |

**10/10 PASS** across all required fields.

### 2.3 Full Corpus Schema — All 32 Records

Validated programmatically. Results:

| Field | Present in 32/32 | Notes |
|-------|-----------------|-------|
| `@context` | Yes | Three-element ActivityStreams/Schema.org/OpenRepo array |
| `@type` | Yes | Always `"procedure"` |
| `cid` | Yes | `sha256-` prefix + 64 hex chars (URL-safe, no encoding needed) |
| `title.en` | Yes | Multilingual dict with `"en"` key present |
| `domain` | Yes | Always `"procedural"` |
| `license` | Yes | Always `"CC0-1.0"` |
| `language` | Yes | Array `["en"]` |
| `steps` | Yes | All non-empty |
| `steps[].body.en` | Yes | All steps have English body text |
| `outcome` | Yes | Present in all 32 |
| `difficulty` | Yes | `"beginner"` or `"intermediate"` only |

**Zero data quality issues across all 32 records.**

### 2.4 Content Metrics and ZIM Size Estimate

| Metric | Value |
|--------|-------|
| Total records | 32 |
| Step counts | min 3, max 5, avg 3.4 |
| Avg words per article | ~193 |
| Estimated HTML per article | 1-3 KB |
| Estimated total HTML (uncompressed) | ~100-200 KB |
| Estimated ZIM file size (Zstandard compressed) | 500 KB - 2 MB |

At 32 articles the corpus is well within all memory and I/O constraints on the Pi 5. The memory concern (ZimWriter buffers all entries) is only relevant past ~5,000 articles.

### 2.5 One Cosmetic Note (Non-Blocking)

`steps[].body.en` fields contain embedded environment metadata in parenthetical blocks (e.g., "Sun requirement: Full Sun. Minimum growing temperature: 7C."). These render readably as plain text in HTML. Structured rendering is a Phase 5.2 styling task.

---

## Section 3: Prerequisite Audit

### 3.1 Python Dependencies — Gap Analysis

Current `backend/pyproject.toml` `[project.dependencies]` (verified live 2026-05-22):

```
fastapi>=0.104.0, uvicorn[standard]>=0.24.0, pydantic>=2.0.0,
pydantic[email]>=2.0.0, asyncpg>=0.29.0, sqlalchemy>=2.0.0,
alembic>=1.13.0, python-multipart>=0.0.6, meilisearch>=0.30.0
```

**Missing**: `libzim` is not declared. A fresh `uv pip install -e .` on any other system will not install it.

Recommended declaration: `"libzim>=3.10.0,<4.0"` (pinned to tested version).

`jinja2` is referenced in older Phase 5 docs but is not imported in `zim_writer.py` — the HTML renderer uses inline f-strings. jinja2 is not a Phase 5.1 requirement.

### 3.2 System Packages — Gap Analysis

| Package | Status | Required for |
|---------|--------|-------------|
| `zim-tools` (provides `zimcheck`) | NOT installed | ZIM post-write validation |
| `libzim-dev` | Not needed | libzim ships pre-built wheel |
| Any Xapian system package | Not needed | bundled in libzim wheel |

**zimcheck availability**: `apt-cache policy zim-tools` confirms version 3.1.3-1 available in Debian Bookworm repos. Installation: `sudo apt install zim-tools`.

**Impact of missing zimcheck**: `create_zim(run_zimcheck=True)` silently skips validation and hardcodes `zimcheck_passed=True` in the result when `self.zimcheck_binary` is falsy. This is deceptive behavior. Fix: return `None` (unknown) rather than `True` when zimcheck is skipped. Alternatively, install zimcheck before activation.

### 3.3 Configuration Requirements

No new environment variables are needed for Phase 5.1 MVP. `ZimWriter` takes `output_path` as a constructor argument. Export output directory configuration via env var is a Phase 5.2 concern.

The `_FALLBACK_ILLUSTRATION_PNG` bytes at line 55 of `zim_writer.py` were live-tested with `add_illustration(48, ...)` and accepted by libzim in Session 1444. Do not replace these bytes with the bytes shown in the roadmap document — the roadmap bytes were not tested on this system.

### 3.4 Database Prerequisites

The `zim_exports` table does not exist. Migration 003 has not been created. The `ZimExport` SQLAlchemy model is absent from `app/models.py` (verified: file ends at `NodePublicKey` class, 400 lines). Migration 003 is required for production export record write-back but is not required for Phase 5.1 smoke testing.

Missing from roadmap's dependency list: migration 003 and the `ZimExport` ORM model are not listed as prerequisites in the roadmap's "What's NOT modified" section, but they are required for full production use.

---

## Section 4: Implementation Checklist — 5 Code Changes

### Summary of Changes

| Change | File | What | Duration |
|--------|------|------|----------|
| 1 | pyproject.toml | Add libzim dependency | 5 min |
| 2 | zim_writer.py | Add libzim import guard | 5 min |
| 3 | zim_writer.py | Add ArticleItem class | 15 min |
| 4 | zim_writer.py | Replace stub + fix _apply_metadata_to_creator | 1.5-2.5 hours |
| 5 | zim_writer.py | Delete stub method | 20 min |
| + | models.py | Add ZimExport ORM model | 30 min |
| + | alembic/ | Create migration 003 | 20 min |

### Change 1: Add libzim to pyproject.toml (5 minutes)

Add to `[project.dependencies]`:
```toml
"libzim>=3.10.0,<4.0",
```
Verify: `uv pip install -e . && importlib.metadata.version('libzim')` returns `'3.10.0'`.

### Change 2: Add libzim import guard (5 minutes)

After line 50 (`from typing import Optional`) in `zim_writer.py`:
```python
try:
    from libzim.writer import Creator, Item, StringProvider, Hint
    _LIBZIM_AVAILABLE = True
except ImportError:
    _LIBZIM_AVAILABLE = False
    Creator = None  # type: ignore[assignment,misc]
    Item = object   # type: ignore[assignment,misc]
    StringProvider = None  # type: ignore[assignment,misc]
    Hint = None  # type: ignore[assignment,misc]
```
Verify: `python -c "from app.services.export.zim_writer import ZimWriter"` succeeds.

### Change 3: Add ArticleItem class (15 minutes)

Insert between `ZimEntry` class (ends ~line 405) and `ZimWriter` class (starts line 412):
```python
class ArticleItem(Item):
    """Adapter from ZimEntry to libzim's Item interface."""

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
Verify: Run 88-test suite — expect 88 passed (ArticleItem not yet called; tests use stub path).

### Change 4: Replace stub and fix _apply_metadata_to_creator (1.5-2.5 hours)

**This is the critical change. Follow the exact ordering below.**

**4a. Replace stub call in `create_zim()` (lines 762-765)**

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
            self._stub_write_placeholder()
        else:
            creator = Creator(str(self.output_path))
            creator.config_indexing(True, self.config.language_iso3)
            creator.set_mainpath("index")
            with creator:
                self._apply_metadata_to_creator(creator)
                for entry in self._entries:
                    creator.add_item(ArticleItem(entry))
            # Creator.__exit__ triggers ZIM file finalization and write
```

**Critical**: `config_indexing` and `set_mainpath` must be called on the `creator` object BEFORE the `with creator:` entry. Calling either inside the `with` block raises `RuntimeError: Creator started`.

**4b. Fix `_apply_metadata_to_creator()` (lines 873-904)**

Replace the entire method body with:
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
        illustration_bytes = self._get_illustration_bytes()
        creator.add_illustration(48, illustration_bytes)
```

Key changes from current code:
- Removed `creator.config_indexing()` (moved to before `with creator:` in Change 4a)
- Removed `try: ... except AttributeError: pass` (was silently masking errors)
- Illustration call is now unconditional (since `_get_illustration_bytes()` always returns bytes)

**4c. Smoke test with real Creator**

```python
import tempfile, pathlib
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope

with tempfile.TemporaryDirectory() as tmpdir:
    metadata = ZimMetadata(
        title="Smoke Test",
        description="Phase 5.1 smoke test",
        language="eng",
        name="open-repo_en_test",
        flavour="nopic",
        creator="Open-Repo",
        publisher="Open-Repo",
        source_url="http://localhost",
    )
    config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour="nopic")
    output = pathlib.Path(tmpdir) / "test.zim"
    writer = ZimWriter(metadata=metadata, config=config, output_path=output)
    writer.add_article(path="index", content="<html><body><h1>Test</h1></body></html>",
                       article_type="article", language="en")
    result = writer.create_zim(run_zimcheck=False)
    
    with open(output, 'rb') as f:
        magic = f.read(4)
    assert magic == b'\x5a\x49\x4d\x04', f"Expected ZIM magic, got {magic.hex()}"
    print(f"ZIM file: {result.file_size_bytes} bytes, SHA-256: {result.sha256[:12]}...")
    print("SMOKE TEST PASSED")
```

Expected: ZIM magic bytes `5a494d04`, file size ~50-80 KB for a single article.

**4d. Run 88-test suite**
```
uv run pytest tests/integration/test_export_pipeline.py -q
```
Expected: 88 passed. The MagicMock-based `TestLibZIMIntegration` tests exercise method signatures and will pass.

### Change 5: Delete stub method (20 minutes, post-verification)

Only after Change 4's smoke test passes:
1. Delete lines 922-939 (`_stub_write_placeholder()` method)
2. Update Change 4a: replace `if not _LIBZIM_AVAILABLE: self._stub_write_placeholder()` with `raise RuntimeError("libzim is not installed.")`
3. Run 88-test suite — confirm no test asserts on stub file content
4. Expected: 88 passed

### Hour-by-Hour Timeline

| Hour | Work |
|------|------|
| 0:00-0:10 | Create feature branch: `git checkout -b feature/zimwriter-libzim-activation` |
| 0:10-0:15 | Change 1: Add libzim to pyproject.toml; verify install |
| 0:15-0:25 | Change 2: Add import guard; verify module import |
| 0:25-0:45 | Change 3: Add ArticleItem; run 88-test suite |
| 0:45-2:00 | Change 4a+4b: Replace stub + fix _apply_metadata_to_creator |
| 2:00-3:00 | Change 4c: Smoke test; debug if needed |
| 3:00-3:15 | Change 4d: Run 88-test suite; verify no regressions |
| 3:15-4:30 | Add ZimExport model to app/models.py |
| 4:30-5:00 | Create Alembic migration 003; review SQL |
| 5:00-5:30 | Change 5: Delete stub; rerun tests |
| 5:30-6:00 | Manual end-to-end test (32-article export from real corpus) |
| 6:00-7:00 | Install zimcheck; run integration tests |
| 7:00-8:00 | Write new test cases (P0 tests from 12-test matrix) |
| 8:00-9:00 | README update, cleanup, PR prep |
| 9:00-11:00 | Buffer: debugging, PR review |

---

## Section 5: Test Environment Setup

### 5.1 Current Baseline (Verified 2026-05-22)

```
uv run pytest tests/integration/test_export_pipeline.py -q
# Result: 88 passed in 0.12s
```

All 88 tests run against the stub path and pass cleanly.

### 5.2 Test Isolation Strategy

No Docker container is needed for the core ZimWriter tests. The real Creator writes to `tmp_path` (pytest fixture). Each test produces independent `.zim` files with no shared state.

For zimcheck integration tests only, the binary must be installed:
```bash
sudo apt install zim-tools   # version 3.1.3-1 from Debian Bookworm
which zimcheck               # /usr/bin/zimcheck
```

If sudo is unavailable, zimcheck tests can run in Docker:
```yaml
services:
  zimwriter-test:
    image: python:3.11-slim-bookworm
    volumes:
      - ./backend:/app
    command: >
      bash -c "apt-get update && apt-get install -y zim-tools &&
               pip install -e /app &&
               pytest /app/tests/integration/test_zimcheck_validation.py -v"
```

### 5.3 New Tests Required (Post-Implementation)

| Test | Priority | Dependency |
|------|----------|-----------|
| `test_zim_writer_creates_real_zim_file` | P0 | libzim only |
| `test_zim_metadata_all_mandatory_fields` | P0 | libzim.reader |
| `test_xapian_index_populated` | P0 | libzim.reader |
| `test_article_count_matches_database` | P0 | libzim only |
| `test_html_no_external_dependencies` | P0 | BeautifulSoup |
| `test_zimcheck_passes_on_valid_export` | P0 | zimcheck binary |
| `test_offline_read_article_by_path` | P0 | libzim.reader |
| `test_unicode_content_survives_roundtrip` | P1 | libzim.reader |
| `test_nopic_variant_excludes_images` | P1 | libzim.reader |
| `test_period_collision_handling` | P1 | None (unit) |
| `test_zimcheck_fails_on_corrupted_archive` | P1 | zimcheck binary |
| `test_zimwriter_not_reusable_after_finalize` | P2 | None (unit) |

`libzim.reader.Archive` is importable with the installed 3.10.0 wheel. BeautifulSoup should be added to `[project.optional-dependencies].dev`.

---

## Section 6: Risk Assessment and Mitigation

### Risk 1: config_indexing ordering causes smoke test failure
**Probability**: HIGH if roadmap's docstring pattern is followed verbatim
**Impact**: High — create_zim() fails immediately
**Detection**: `RuntimeError: Creator started` on first real ZIM attempt
**Mitigation**: Use the corrected pattern (config_indexing before `with creator:`). This deviates from the docstring at line 736. Fix is documented above. 10-minute recovery once identified.
**Status**: DOCUMENTED AND MITIGATED

### Risk 2: zimcheck not installed, silent validation bypass
**Probability**: CERTAIN (not installed, confirmed)
**Impact**: Medium — exports not validated; `zimcheck_passed=True` returned erroneously
**Mitigation**: `sudo apt install zim-tools` (5 min). Or fix: return `zimcheck_passed=None` when skipped.
**Status**: KNOWN GAP, easy to address

### Risk 3: libzim not in pyproject.toml breaks fresh deployments
**Probability**: CERTAIN on any new system
**Impact**: High — ImportError on startup
**Mitigation**: Change 1 must be the first change made. 5 minutes.
**Status**: ADDRESSED IN CHANGE 1

### Risk 4: Silent AttributeError guard in _apply_metadata_to_creator masks failures
**Probability**: CONFIRMED (guard is present in current code)
**Impact**: Medium — metadata errors silently swallowed
**Mitigation**: Remove the `try: ... except AttributeError: pass` guard during Change 4b.
**Status**: ADDRESSED IN CHANGE 4B

### Risk 5: Migration 003 absent — zim_exports table not created
**Probability**: CERTAIN (migration 003 does not exist)
**Impact**: High for production write-back of export records; Low for smoke testing
**Mitigation**: Migration 003 creation is in timeline (hours 3:15-5:00).
**Status**: KNOWN GAP, in scope

### Risk 6: Thermal throttling extends export time
**Probability**: Medium for exports exceeding 30 seconds
**Impact**: Low for 32-article MVP corpus (~3 seconds), Medium for 500+ articles
**Mitigation**: Schedule exports at 02:00-04:00 UTC; verify heatsink seating; avoid concurrent CPU work.
**Status**: LOW RISK for MVP scope

### Risk 7: Export API endpoint absent
**Probability**: CERTAIN (no `app/api/v1/export.py` exists)
**Impact**: Low for Phase 5.1 MVP (ZimWriter invoked directly from Python)
**Mitigation**: Phase 5.2 scope.
**Status**: KNOWN, DEFERRED

### Overall Feasibility Verdict

**Candidate 1 is feasible.** All hard dependencies are resolved. The implementation is ~70% complete (scaffolding done, stubs in place). The remaining work is mechanical code replacement with one critical ordering constraint. An experienced developer following this document can complete Changes 1-4 in 2-4 hours. The full 11-hour estimate includes testing, migration, and PR preparation.

**Confidence**: HIGH (90%) that the smoke test will produce a valid ZIM on first attempt with the corrected pattern. MEDIUM-HIGH (75%) that all 12 new tests pass without additional debugging.

---

## Sources

- Live system inspection: `projects/open-repo/backend/` (2026-05-22, this session)
- Prior audit: `PHASE_5_CANDIDATE_1_IMPLEMENTATION_VERIFICATION_v3.md` (Session 1444, 2026-05-21)
- Prior post-merge audit: `PHASE_5_1_POST_MERGE_VERIFICATION.md` (Session 1500, 2026-05-22)
- Roadmap: `PHASE_5_CANDIDATE_1_ZIMWRITER_IMPLEMENTATION_ROADMAP.md` (2026-05-19)
- [python-libzim PyPI](https://pypi.org/project/libzim/)
- [python-libzim GitHub](https://github.com/openzim/python-libzim)
- [openZIM Metadata spec](https://wiki.openzim.org/wiki/Metadata)
