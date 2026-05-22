---
title: "Phase 5 Candidate 1 — Step-by-Step Implementation Checklist"
project: open-repo
phase: 5
candidate: 1
document_type: execution-checklist
status: ready-to-execute
date: 2026-05-22
session: 1507
branch: feature/zimwriter-libzim-activation
total_time: "5.5–6 hours (all 5 code changes already done; this is cleanup + tests + PR)"
---

# Phase 5 Candidate 1: Step-by-Step Implementation Checklist

**Audience**: The person executing Phase 5 merge and activation.
**Purpose**: Mechanical execution guide. All 5 code changes are already implemented. This checklist covers the remaining cleanup, missing tests, and verification steps to reach a merge-ready PR.
**Total time**: 5.5–6 hours
**Branch**: `feature/zimwriter-libzim-activation`
**Key constraint**: Do not merge to `main` until Phase 4 PR #1 has landed.

---

## Pre-Flight Check (5 minutes)

| # | Check | Command | Expected Result | Blocker? |
|---|-------|---------|----------------|---------|
| P1 | Confirm on feature branch | `git branch --show-current` | `feature/zimwriter-libzim-activation` | Yes |
| P2 | libzim installed | `uv run python3 -c "from libzim.writer import Creator, Item, StringProvider, Hint; print('OK')"` | `OK` | Yes |
| P3 | Baseline test run | `uv run pytest tests/integration/test_export_pipeline.py -q` | `87 passed, 1 failed` | No — 1 known failing test |
| P4 | Disk space | `df -h /tmp` | At least 500 MB free | Yes (ZIM files up to ~500 MB) |
| P5 | Migration chain | `alembic history` | Shows 001, 002, 003 | No — but note if 003 missing |

---

## Phase A: Fix Two Known Issues (45 minutes)

### Step A1: Install zimcheck binary
**Duration**: 5 minutes
**Blocker for**: All zimcheck validation steps (A3, E2, E3)
**Risk if skipped**: Exports appear validated but zimcheck is not actually run

```bash
sudo apt install zim-tools
```

Verify:
```bash
zimcheck --version
```
Expected: version line containing `3.1.3` or similar.

If apt fails (e.g., older sources list): Download from https://download.openzim.org/release/zim-tools/ and install manually.

---

### Step A2: Remove duplicate _FALLBACK_ILLUSTRATION_PNG definition
**Duration**: 15 minutes
**File**: `projects/open-repo/backend/app/services/export/zim_writer.py`
**Issue**: The constant is defined twice — approximately lines 66-70 (first definition, a 1x1 PNG) and lines 72-75 (second definition, the correct 48x48 PNG). The second overwrites the first. Remove the first.

Find and remove the block that looks like:
```python
_FALLBACK_ILLUSTRATION_PNG = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x000\x00\x00\x000"
    b"\x08\x06\x00\x00\x00W\x02\xf9\x87\x00\x00\x00\x0bIDATx\x9cc"
    b"\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82"
)
```

Keep only the second definition (the longer bytes starting with `b'\x89PNG\r\n...'` ending in `...IEND\xaeB\x60\x82'`).

Verify:
```bash
uv run pytest tests/integration/test_export_pipeline.py::TestLibZIMIntegration::test_fallback_png_is_valid_48x48 -v
```
Expected: `PASSED` — confirms 48x48 dimensions.

```bash
uv run python3 -c "
import struct
from app.services.export.zim_writer import _FALLBACK_ILLUSTRATION_PNG
offset = 8
ihdr_offset = offset + 8
w = struct.unpack('>I', _FALLBACK_ILLUSTRATION_PNG[ihdr_offset:ihdr_offset+4])[0]
h = struct.unpack('>I', _FALLBACK_ILLUSTRATION_PNG[ihdr_offset+4:ihdr_offset+8])[0]
print(f'PNG dimensions: {w}x{h}')
assert w == 48 and h == 48
print('OK')
"
```
Expected: `PNG dimensions: 48x48` and `OK`.

---

### Step A3: Fix the one failing test
**Duration**: 30 minutes
**File**: `projects/open-repo/backend/tests/integration/test_export_pipeline.py`
**Test**: `TestLibZIMIntegration::test_config_indexing_call_in_metadata_apply` (line 1497)

**Root cause**: The test calls `writer._apply_metadata_to_creator(mock_creator)` and asserts `config_indexing` was called on the mock. But `config_indexing()` is called in `create_zim()`, not in `_apply_metadata_to_creator()`. The implementation is correct; the test expectation is wrong.

**Fix**: Replace the test with one that verifies the Xapian index is actually present in a real generated ZIM:

```python
def test_config_indexing_enables_fulltext_search(self) -> None:
    """config_indexing(True, lang) is called in create_zim() — verify via archive.has_fulltext_index."""
    import tempfile
    import libzim
    from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig

    metadata = ZimMetadata(
        title="FTS Test",
        description="Full-text search test",
        language="eng",
        name="test_en_nopic",
        flavour="nopic",
        creator="Test",
        publisher="Test",
        source_url="https://test.example.org",
    )
    config = ExportConfig(scope=ExportScope.LOCAL_ONLY, language_iso3="eng")

    with tempfile.TemporaryDirectory() as tmpdir:
        writer = ZimWriter(
            metadata=metadata,
            config=config,
            output_path=Path(tmpdir) / "fts_test.zim",
            zimcheck_binary=None,
        )
        writer.add_article(
            path="index",
            content="<html><body><h1>Index</h1><p>Practical knowledge.</p></body></html>",
            article_type="index",
        )
        writer.add_article(
            path="water/biosand-filter",
            content="<html><body><h1>Biosand Filter</h1><p>Removes pathogens.</p></body></html>",
            article_type="procedure",
        )
        result = writer.create_zim(run_zimcheck=False)
        archive = libzim.Archive(str(result.output_path))
        assert archive.has_fulltext_index, "Xapian FTS index must be present in ZIM"
```

Verify:
```bash
uv run pytest tests/integration/test_export_pipeline.py -q
```
Expected: `88 passed` (zero failures).

**If libzim not available during test**: Mark the new test with `@pytest.mark.integration` and add a skip guard:
```python
pytest.importorskip("libzim", reason="libzim required for FTS test")
```

---

## Phase B: Run zimcheck on a Real ZIM (30 minutes)

**Blockers**: A1 (zimcheck installed), A2 (PNG fixed), A3 (tests all pass)

### Step B1: Generate and validate a 10-article ZIM

```bash
cd projects/open-repo/backend
uv run python3 -c "
import tempfile
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope

meta = ZimMetadata(
    title='Open-Repo Verification',
    description='Phase 5 validation export',
    language='eng',
    name='open-repo_en_nopic',
    flavour='nopic',
    creator='Open-Repo Community',
    publisher='Open-Repo',
    source_url='https://example.org',
)
config = ExportConfig(scope=ExportScope.LOCAL_ONLY)
writer = ZimWriter(metadata=meta, config=config,
    output_path=Path('/tmp/phase5-verify.zim'), zimcheck_binary='zimcheck')
writer.add_article(path='index',
    content='<html><head><title>Open-Repo</title></head><body><h1>Open-Repo</h1><p>Offline knowledge.</p></body></html>',
    article_type='index')
for i in range(9):
    writer.add_article(
        path=f'agriculture/guide-{i:03d}',
        content=f'<html><head><title>Guide {i}</title></head><body><h1>Guide {i}</h1><p>Practical guide {i}. Water, soil, crops.</p></body></html>',
        article_type='procedure')
result = writer.create_zim(run_zimcheck=True)
print('zimcheck_passed:', result.zimcheck_passed)
print('file_size_bytes:', result.file_size_bytes)
print('sha256 prefix:', result.sha256[:16])
print('duration:', round(result.generation_duration_seconds, 3), 's')
"
```

Expected output:
```
zimcheck_passed: True
file_size_bytes: [> 50000]
sha256 prefix: [16 hex chars]
duration: [< 2.0] s
```

**If zimcheck fails**: Run `zimcheck --verbose /tmp/phase5-verify.zim` for specific error messages. Common causes and fixes:

| zimcheck error | Cause | Fix |
|---------------|-------|-----|
| `Illustration must be 48x48` | Wrong PNG size | Verify Step A2 removed the 1x1 version |
| `Description too long` | description field > 80 chars | Shorten description in `ZimMetadata` |
| `Name is not valid` | Name contains uppercase/spaces | Must match pattern `{publisher}_{lang}_{flavour}` |
| `No front articles` | No article with `is_front_article=True` | Ensure at least one article with `article_type="index"` |

---

## Phase C: Write Missing Integration Tests (1 hour)

**Blockers**: B1 complete (ZIM generation working, zimcheck passing)

These 3 test files do not yet exist. They correspond to the 12 test scenarios in the roadmap's test matrix.

### Step C1: Create tests/unit/test_zim_writer_libzim.py
**Duration**: 30 minutes
**Tests to implement** (8 tests covering the libzim integration layer):

- `test_zim_writer_creates_real_zim_file`: Assert `open(path, 'rb').read(4) == b'\x5a\x49\x4d\x04'`
- `test_zim_metadata_all_mandatory_fields`: Use `libzim.Archive.get_metadata()` for all 7 text fields
- `test_xapian_index_populated`: Assert `archive.has_fulltext_index == True`; search returns >=1 result
- `test_article_count_matches_input`: Assert `archive.entry_count == N` for N articles added
- `test_html_no_external_dependencies`: BeautifulSoup parse — no `http://` in `src` or `href` attributes
- `test_period_collision_handling`: `ZimWriter.compute_period(["2026-05"], now=datetime(2026, 5, 22))` returns `"2026-05a"`
- `test_zimwriter_not_reusable_after_finalize`: Second `create_zim()` call raises `RuntimeError`
- `test_nopic_variant_excludes_images`: No entries with `mime_type.startswith("image/")` when `include_images=False`

All tests must use `tmp_path` pytest fixture for output isolation. No shared state between tests.

### Step C2: Create tests/integration/test_zimcheck_validation.py
**Duration**: 15 minutes
**Tests to implement** (2 tests):

- `test_zimcheck_passes_on_valid_export`: Generate 10-article ZIM with `zimcheck_binary='zimcheck'`; assert `result.zimcheck_passed == True`
- `test_zimcheck_fails_on_corrupted_archive`: Generate ZIM, corrupt bytes after write, assert file renamed to `.zim.invalid` and `result.zimcheck_passed == False`

Both tests must be decorated `@pytest.mark.integration` and skip if zimcheck is not in PATH:
```python
pytestmark = pytest.mark.integration
zimcheck_available = pytest.mark.skipif(
    not shutil.which("zimcheck"), reason="zimcheck not installed"
)
```

### Step C3: Create tests/integration/test_zim_readback.py
**Duration**: 15 minutes
**Tests to implement** (2 tests):

- `test_offline_read_article_by_path`: Write article at known path; verify `archive.get_entry_by_path(path).get_item().content` returns correct bytes
- `test_unicode_content_survives_roundtrip`: Write article with French (`Déjà vu`), Arabic (`كل شيء`), Japanese (`日本語`); read back; assert all three are in returned content string

Both tests require `libzim` — skip gracefully if not installed:
```python
libzim = pytest.importorskip("libzim", reason="libzim required")
```

### Step C4: Run complete test suite
```bash
uv run pytest tests/ -q
```
Expected: All tests pass (88 existing + 12 new = ~100 tests total).

---

## Phase D: Cleanup (30 minutes)

**Blockers**: C4 complete (all tests passing including new ones)

### Step D1: Delete _stub_write_placeholder() method
**Duration**: 15 minutes
**File**: `projects/open-repo/backend/app/services/export/zim_writer.py`

Locate and delete the entire `_stub_write_placeholder()` method (approximately lines 914-931). It looks like:
```python
    def _stub_write_placeholder(self) -> None:
        """Write a minimal stub file..."""
        placeholder_content = (
            f"STUB ZIM PLACEHOLDER\n"
            ...
        ).encode("utf-8")
        self.output_path.write_bytes(placeholder_content)
```

Also remove the fallback branch in `create_zim()` that calls it:
```python
        if not _LIBZIM_AVAILABLE:
            # Fallback stub...
            self._stub_write_placeholder()
        else:
```
becomes:
```python
        # (no fallback branch)
```

Keep the `try/except ImportError` import guard at the top — remove it only in a follow-up commit after CI confirms libzim is always installed.

Verify:
```bash
uv run pytest tests/ -q
```
Expected: Same test count, all passing.

### Step D2: Verify migration 003
**Duration**: 15 minutes

```bash
cd projects/open-repo/backend
alembic history
```
Expected: Shows `001 -> 002 -> 003` chain.

```bash
alembic current
```
Expected: Either shows current head or "no migrations applied" (on dev without DB — that's fine).

For a live DB check (if PostgreSQL is running):
```bash
alembic upgrade head
alembic current  # Should show revision 003
```

---

## Phase E: Manual End-to-End Verification (1 hour)

**Blockers**: All Phase A-D complete

### Step E1: Generate real 32-article ZIM from OpenFarm corpus
**Duration**: 20 minutes

```bash
cd projects/open-repo/backend
uv run python3 -c "
import json
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope

# Load OpenFarm corpus
corpus_path = Path('../data/openfarm_procedures.jsonl')
articles = [json.loads(line) for line in corpus_path.read_text().splitlines() if line.strip()]
print(f'Loaded {len(articles)} articles from corpus')

meta = ZimMetadata(
    title='Open-Repo: Practical Knowledge',
    description='Offline practical knowledge library',
    language='eng',
    name='open-repo_en_nopic',
    flavour='nopic',
    creator='Open-Repo Community',
    publisher='Open-Repo',
    source_url='https://example.org',
)
config = ExportConfig(scope=ExportScope.LOCAL_ONLY)
writer = ZimWriter(metadata=meta, config=config,
    output_path=Path('/tmp/open-repo_en_nopic_e2e.zim'), zimcheck_binary='zimcheck')

# Add index page
writer.add_article(path='index',
    content='<html><head><title>Open-Repo Offline Library</title><style>body{font-family:sans-serif;margin:1.5rem;}</style></head><body><h1>Open-Repo</h1><p>Practical knowledge for offline use.</p></body></html>',
    article_type='index')

# Add all corpus articles
for article in articles:
    cid = article['cid']
    title_en = article['title']['en'] if isinstance(article['title'], dict) else article['title']
    domain = article.get('domain', 'general')
    steps_html = ''.join(
        f'<li><strong>Step {i+1}</strong>: {s[\"body\"][\"en\"]}</li>'
        for i, s in enumerate(article.get('steps', []))
        if isinstance(s.get('body'), dict) and 'en' in s['body']
    )
    html = f'<html><head><title>{title_en}</title><style>body{{font-family:sans-serif;margin:1.5rem;}}</style></head><body><h1>{title_en}</h1><ol>{steps_html}</ol></body></html>'
    writer.add_article(path=f'{domain}/{cid}', content=html, article_type='procedure')

result = writer.create_zim(run_zimcheck=True)
print(f'E2E ZIM written: {result.output_path}')
print(f'Articles: {result.article_count}')
print(f'File size: {result.file_size_bytes:,} bytes ({result.file_size_bytes / 1024:.1f} KB)')
print(f'zimcheck passed: {result.zimcheck_passed}')
print(f'SHA-256: {result.sha256}')
print(f'Duration: {result.generation_duration_seconds:.2f}s')

# Verify with SHA-256 sidecar
import hashlib
data = Path(result.output_path).read_bytes()
computed = hashlib.sha256(data).hexdigest()
assert computed == result.sha256, 'SHA-256 mismatch!'
print('SHA-256 checksum verified OK')
"
```

Expected:
```
Loaded 32 articles from corpus
E2E ZIM written: /tmp/open-repo_en_nopic_e2e.zim
Articles: 33
File size: [> 100000] bytes ([> 100] KB)
zimcheck passed: True
SHA-256: [64 hex chars]
Duration: [< 10.0]s
SHA-256 checksum verified OK
```

**If zimcheck fails on real corpus**: Check `zimcheck --verbose /tmp/open-repo_en_nopic_e2e.zim` for errors. Most likely cause is article HTML containing external URLs from OpenFarm content (src/href attributes with http://). Fix by stripping external references in the HTML rendering step before adding articles.

### Step E2: Verify with kiwix-serve (if Docker available)
**Duration**: 20 minutes

```bash
# If Docker is available:
docker run -d --name kiwix-test \
  -v /tmp:/data:ro \
  -p 127.0.0.1:8080:8080 \
  ghcr.io/kiwix/kiwix-tools:latest \
  kiwix-serve --port 8080 /data/open-repo_en_nopic_e2e.zim

curl -s http://127.0.0.1:8080/ | grep -i "open-repo\|kiwix" | head -3
# Should show Kiwix landing page HTML mentioning the ZIM title

docker stop kiwix-test && docker rm kiwix-test
```

Pass criterion: HTTP GET returns HTML containing article content. At least one article title visible in the page source.

### Step E3: Verify SHA-256 sidecar format
**Duration**: 5 minutes

```bash
# Create sidecar file
sha256sum /tmp/open-repo_en_nopic_e2e.zim > /tmp/open-repo_en_nopic_e2e.zim.sha256
# Verify it checks out
sha256sum -c /tmp/open-repo_en_nopic_e2e.zim.sha256
```
Expected: `open-repo_en_nopic_e2e.zim: OK`

### Step E4: Benchmark generation time for thermal monitoring record
**Duration**: 5 minutes

Record the E2E duration from Step E1. Compare against these thresholds:

| Articles | Expected time (Pi 5, warm) | Alert threshold |
|----------|---------------------------|----------------|
| 10 | < 0.5 s | > 2 s |
| 32 (full corpus) | < 3 s | > 10 s |
| 500 (future) | < 60 s | > 120 s |

If the 32-article export exceeds 10 seconds, check CPU temperature (`vcgencmd measure_temp`) and schedule exports for 02:00 UTC when ambient temperature is lowest.

---

## Phase F: PR Preparation (30 minutes)

**Blockers**: All E steps complete

### Step F1: Final full test run

```bash
cd projects/open-repo/backend
uv run pytest tests/ -v 2>&1 | tail -20
```
Expected: All tests pass. Zero failures.

### Step F2: Commit changes

```bash
git add \
  projects/open-repo/backend/app/services/export/zim_writer.py \
  projects/open-repo/backend/tests/integration/test_export_pipeline.py \
  projects/open-repo/backend/tests/unit/test_zim_writer_libzim.py \
  projects/open-repo/backend/tests/integration/test_zimcheck_validation.py \
  projects/open-repo/backend/tests/integration/test_zim_readback.py

git commit -m "fix(phase-5): cleanup before merge — PNG dedup, test fix, new integration tests"
```

### Step F3: Update CHECKIN.md

Add an entry under "Needs Your Input":

```
## Phase 5 Candidate 1 — ZimWriter/libzim — READY FOR MERGE DECISION

Branch: feature/zimwriter-libzim-activation
Status: Implementation complete. Cleanup complete. All tests passing.
Tests: ~100 passing (88 original + 12 new integration tests)
zimcheck: Passing on real ZIM (10-article and 32-article corpus verified)
ZIM opens: Confirmed in kiwix-serve [or: manual verification pending]
Migration: 003_add_zim_exports_table.py ready; applies cleanly

GATE: Must not merge to main before Phase 4 PR #1 has landed.

Decision needed by May 25-26:
[ ] Approve Candidate 1 as Phase 5 direction → merge feature/zimwriter-libzim-activation
[ ] Defer in favor of Candidate 2 (OPDS feed) or Candidate 3
[ ] Merge both (Candidate 1 + 2) simultaneously
```

---

## Completion Definition

Phase 5 Candidate 1 is ready to merge when ALL of the following are checked:

- [ ] `zimcheck --version` exits 0 (zimcheck binary installed)
- [ ] `_FALLBACK_ILLUSTRATION_PNG` defined exactly once (48x48, not 1x1)
- [ ] `uv run pytest tests/ -q` reports 0 failures
- [ ] `zimcheck` passes on a 10-article test ZIM
- [ ] `zimcheck` passes on the 32-article OpenFarm corpus ZIM
- [ ] ZIM opens in kiwix-serve — articles display, search returns results
- [ ] `sha256sum -c {file}.sha256` passes
- [ ] `alembic history` shows 001 → 002 → 003 chain
- [ ] `_stub_write_placeholder()` method deleted from codebase
- [ ] CHECKIN.md updated with merge decision request
- [ ] Phase 4 PR #1 has landed (gate; do not merge before this)

---

## Risk Reference Card

| Symptom | Cause | Fix |
|---------|-------|-----|
| `ModuleNotFoundError: libzim` | Wheel not installed | `uv pip install "libzim>=3.10.0,<4.0"` |
| `zimcheck: command not found` | zim-tools not installed | `sudo apt install zim-tools` |
| `zimcheck FAILED: Illustration` | Fallback PNG wrong dimensions | Confirm Step A2 removed the 1x1 version |
| `zimcheck FAILED: Description too long` | Description > 80 chars | Shorten `ZimMetadata.description` |
| `zimcheck FAILED: Name is not valid` | Name has uppercase or special chars | Pattern must be `{publisher}_{lang}_{flavour}` |
| Magic bytes not `5a494d04` | Stub path still running | Check `_LIBZIM_AVAILABLE` flag; confirm import guard is active |
| `AttributeError: has_full_text_index` | Wrong attribute name | Use `archive.has_fulltext_index` (no underscore between full and text) |
| Export OOM killed | Too many articles buffered | Reduce `max_items` in `ExportConfig` for test; streaming mode is Phase 5.2 |
| Generation > 30s on Pi 5 | Thermal throttling | Check `vcgencmd measure_temp`; schedule at 02:00 UTC |
| `RuntimeError: ZimWriter can only be called once` | `create_zim()` called twice | Use a new `ZimWriter` instance per export |
| Second commit 274eb1f2 adds `libzim>=3.10.0,<4.0` but fails | Pin too tight if wheel unavailable | Loosen to `>=3.2,<4.0` if needed; 3.10.0 is what's installed |
