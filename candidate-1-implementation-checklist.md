---
title: "Phase 5 Candidate 1 — ZimWriter/libzim: Executable Implementation Checklist"
project: open-repo
phase: 5
candidate: 1
document_type: execution-checklist
status: ready-to-execute
date: 2026-05-20
session: 1429
path: feature/zimwriter-libzim-activation -> master
total_estimate: "2-3 hours (merge path, not from-scratch)"
supersedes: PHASE_5_CANDIDATE_1_IMPLEMENTATION_CHECKLIST.md
---

# Phase 5 Candidate 1: Executable Implementation Checklist

**State of play**: Implementation is complete on `feature/zimwriter-libzim-activation` (commit ec0ff7be). Two defects must be fixed before merging. This checklist covers the merge path only — the 8-11 hour from-scratch implementation is done.

**Working directory for all commands**: `/home/awank/dev/SuperClaude_Framework/projects/open-repo/backend`

**Total estimated time**: 2-3 hours

---

## Pre-Flight Gate (10 minutes)

Complete all items before touching any code. If any item fails, stop and diagnose before proceeding.

| # | Check | Command | Pass condition |
|---|---|---|---|
| PF1 | Python version | `python3 --version` | `Python 3.11.x` |
| PF2 | Architecture | `uname -m` | `aarch64` |
| PF3 | On master, clean | `git status` | `nothing to commit` |
| PF4 | Feature branch exists | `git branch -a \| grep zimwriter-libzim-activation` | Branch listed |
| PF5 | Baseline 84 tests pass on master | `python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=no` | `84 passed` (stub mode, no libzim) |
| PF6 | Disk space | `df -h /tmp` | At least 2 GB free |

If PF5 shows something other than `84 passed`, the master branch has a pre-existing regression. Do not proceed until that is diagnosed — it is not caused by this feature.

---

## Phase 1: Environment Setup (est. 45 min)

### Step 1.1 — Create working branch from feature branch

**Duration**: 2 minutes

```bash
git checkout feature/zimwriter-libzim-activation
git checkout -b fix/phase5-zimwriter-premerge-defects
```

This creates a clean branch on top of the feature work where defect fixes will be committed before PR creation.

**Verify**:
```bash
git log --oneline -3
```
Expected: top commit is from the feature branch history (feat(open-repo): Phase 5 Candidate 1 libzim integration or similar).

---

### Step 1.2 — Install libzim Python wheel

**Duration**: 3 minutes

```bash
uv pip install "libzim>=3.2,<4.0"
```

**Verify**:
```bash
uv run python3 -c "from libzim.writer import Creator, Item, StringProvider, Hint; import libzim; print('libzim version:', libzim.__version__)"
```
Expected: `libzim version: 3.10.0` (or similar 3.x version).

If the install fails with "no matching distribution found":
- Confirm architecture: `uname -m` should be `aarch64`
- Try: `uv pip install libzim --verbose` to see the detailed resolution log
- Fallback: `pip install libzim` to rule out uv resolver issues

---

### Step 1.3 — Install zimcheck binary

**Duration**: 5 minutes

```bash
sudo apt-get install -y zim-tools
```

**Verify**:
```bash
zimcheck --version
```
Expected: A version line from zim-tools (3.x or later).

If `sudo` is not available, use the integration test skip approach and defer zimcheck validation to a docker environment.

---

### Step 1.4 — Confirm 88 tests pass on feature branch

**Duration**: 30 seconds

```bash
python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=short
```
Expected: `88 passed` (the feature branch has 4 additional tests compared to master's 84). If the count is 84, that is also acceptable — the important thing is no failures.

If tests fail here, diagnose the specific failure before proceeding. Do not proceed with defect fixes if the test baseline is already broken.

---

### Step 1.5 — Perform ZIM magic header smoke test

**Duration**: 2 minutes

This confirms libzim is actually producing binary ZIM files, not the stub placeholder.

```bash
uv run python3 -c "
import tempfile
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig

tmp = tempfile.mkdtemp()
meta = ZimMetadata(
    title='Smoke Test',
    description='Pre-merge smoke test export',
    language='eng',
    name='open-repo_en_nopic',
    flavour='nopic',
    creator='Test',
    publisher='Test',
    source_url='https://example.org'
)
config = ExportConfig()
writer = ZimWriter(metadata=meta, config=config,
                   output_path=Path(tmp) / 'smoke.zim', zimcheck_binary=None)
writer.add_article(path='index',
                   content='<html><body><h1>Home</h1></body></html>',
                   article_type='procedure')
result = writer.create_zim(run_zimcheck=False)
magic = open(result.output_path, 'rb').read(4)
print('Magic bytes:', magic.hex())
assert magic == b'\\x5a\\x49\\x4d\\x04', f'Expected ZIM magic, got: {magic.hex()}'
print('ZIM magic OK — libzim is producing real ZIM files')
"
```
Expected: `ZIM magic OK — libzim is producing real ZIM files`

If magic bytes are wrong or file is text (stub mode), `_LIBZIM_AVAILABLE` is False despite the install. Check: `uv run python3 -c "from libzim.writer import Creator; print('OK')"`. If that fails, the wheel is not installed in the correct venv.

---

## Phase 2: Defect Fixes (est. 30 min)

### Step 2.1 — Fix Defect 1: Remove duplicate `_FALLBACK_ILLUSTRATION_PNG` constant

**Duration**: 5 minutes
**File**: `app/services/export/zim_writer.py`
**Lines to remove**: approximately 62-71 (the first of the two `_FALLBACK_ILLUSTRATION_PNG` definitions)

The file contains two module-level assignments to `_FALLBACK_ILLUSTRATION_PNG`. The first one (a multi-line bytes literal) is dead code — Python uses the second (single-line bytes literal on approximately line 75) at runtime. Remove the first definition entirely including its comment block.

Find and remove this block (it appears before `logger = logging.getLogger(__name__)`):
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

Keep the second definition (the one-liner on approximately line 75 starting with `# Fallback 48x48 transparent PNG illustration...`).

**Verify**:
```bash
grep -c "_FALLBACK_ILLUSTRATION_PNG" app/services/export/zim_writer.py
```
Expected: 3 occurrences (one definition + two references in method body). Was 4 before this fix (two definitions + two references).

Re-run tests:
```bash
python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=short
```
Expected: same pass count as Step 1.4.

---

### Step 2.2 — Fix Defect 2: Remove silent `except AttributeError: pass` from `_apply_metadata_to_creator()`

**Duration**: 10 minutes
**File**: `app/services/export/zim_writer.py`
**Method**: `_apply_metadata_to_creator()`

The method currently wraps all Creator calls in a bare try/except. Locate the method body (approximately line 948-985) and remove the try/except wrapper, leaving only the method calls directly in the method body.

Current form (to replace) — find this pattern:
```python
        try:
            creator.config_indexing(True, self.config.language_iso3)
            creator.add_metadata("Title", self.metadata.title)
            ...
            creator.add_illustration(48, _FALLBACK_ILLUSTRATION_PNG)
        except AttributeError:
            pass
```

Replace with the same calls but without the try/except wrapper:
```python
        creator.config_indexing(True, self.config.language_iso3)
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
        if illustration_bytes:
            creator.add_illustration(48, illustration_bytes)
        else:
            creator.add_illustration(48, _FALLBACK_ILLUSTRATION_PNG)
```

**Verify**:
```bash
grep "except AttributeError" app/services/export/zim_writer.py
```
Expected: no output (the except clause has been removed).

Re-run the ZIM magic smoke test from Step 1.5 to confirm ZIM creation still works.

Re-run tests:
```bash
python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=short
```
Expected: same pass count.

---

### Step 2.3 — Commit defect fixes

**Duration**: 5 minutes

```bash
git add app/services/export/zim_writer.py
git commit -m "fix(phase-5): remove duplicate PNG constant and silent AttributeError catch in ZimWriter"
```

---

## Phase 3: Integration and Testing (est. 1.5 hrs)

### Step 3.1 — Run full export test suite

**Duration**: 1 minute

```bash
python3 -m pytest tests/ -k "zim or export" -v --tb=short 2>&1 | tail -30
```
Expected: All tests pass. Zero `FAILED` or `ERROR` lines.

---

### Step 3.2 — Metadata readback verification

**Duration**: 5 minutes

Verify that metadata written by `_apply_metadata_to_creator()` is readable back via the libzim reader:

```bash
uv run python3 -c "
import tempfile
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig
from libzim.reader import Archive

tmp = tempfile.mkdtemp()
meta = ZimMetadata(
    title='Metadata Readback Test',
    description='Verifying metadata fields round-trip',
    language='eng',
    name='open-repo_en_nopic',
    flavour='nopic',
    creator='Open-Repo Community',
    publisher='Open-Repo',
    source_url='https://example.org'
)
config = ExportConfig()
writer = ZimWriter(metadata=meta, config=config,
                   output_path=Path(tmp) / 'meta_test.zim', zimcheck_binary=None)
writer.add_article(path='index',
                   content='<html><head><title>Home</title></head><body><h1>Open-Repo</h1></body></html>',
                   article_type='procedure')
result = writer.create_zim(run_zimcheck=False)

archive = Archive(str(result.output_path))
fields = {
    'Title': 'Metadata Readback Test',
    'Language': 'eng',
    'Creator': 'Open-Repo Community',
    'Name': 'open-repo_en_nopic',
}
all_ok = True
for key, expected in fields.items():
    actual = archive.get_metadata(key).decode('utf-8')
    status = 'OK' if actual == expected else f'MISMATCH: got {actual!r}'
    print(f'{key}: {status}')
    if actual != expected:
        all_ok = False
print('Metadata readback:', 'PASS' if all_ok else 'FAIL')
"
```
Expected: All four fields show `OK` and final line is `Metadata readback: PASS`.

This is the critical test for Defect 2 — if the `except AttributeError: pass` was silently swallowing failures before, this test would have shown metadata missing. After the fix, it must pass.

---

### Step 3.3 — zimcheck validation run

**Duration**: 5 minutes

Requires zimcheck binary installed in Step 1.3.

```bash
uv run python3 -c "
import tempfile
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig

tmp = tempfile.mkdtemp()
meta = ZimMetadata(
    title='Open-Repo Test Library',
    description='Offline knowledge for zimcheck test',
    language='eng',
    name='open-repo_en_nopic',
    flavour='nopic',
    creator='Open-Repo Community',
    publisher='Open-Repo',
    source_url='https://example.org'
)
config = ExportConfig()
writer = ZimWriter(metadata=meta, config=config,
                   output_path=Path(tmp) / 'zimcheck_test.zim',
                   zimcheck_binary='zimcheck')
for i in range(10):
    writer.add_article(
        path=f'article/{i:03d}',
        content=f'<html><head><title>Article {i}</title></head><body><h1>Article {i}</h1><p>Content.</p></body></html>',
        article_type='procedure'
    )
writer.add_article(
    path='index',
    content='<html><head><title>Open-Repo</title></head><body><h1>Open-Repo Offline Library</h1></body></html>',
    article_type='procedure'
)
result = writer.create_zim(run_zimcheck=True)
print('zimcheck passed:', result.zimcheck_passed)
print('File size:', result.file_size_bytes, 'bytes')
print('Articles:', result.article_count)
"
```
Expected:
```
zimcheck passed: True
File size: [> 5000]
Articles: 11
```

If `zimcheck passed: False`, run `zimcheck --verbose /path/to/zimcheck_test.zim` for specific error messages. Common causes and fixes:

| Error message | Cause | Fix |
|---|---|---|
| `Missing mandatory metadata: Title` | Defect 2 not fixed | Re-apply Step 2.2 |
| `Illustration size should be 48x48` | Wrong PNG dimensions | Verify line-75 PNG is 48x48 |
| `Description too long` | Description >80 chars | Trim test description |
| `Name is invalid` | Uppercase or spaces in name | Use all-lowercase `{pub}_{lang}_{flavour}` pattern |
| `No article found` | No front articles added | Ensure article_type produces is_front_article=True |

---

### Step 3.4 — Full test suite run

**Duration**: 2 minutes

```bash
python3 -m pytest tests/ -v --tb=short 2>&1 | tail -40
```
Expected: All tests pass. Zero failures. Zero errors.

---

### Step 3.5 — Unicode round-trip verification

**Duration**: 5 minutes

```bash
uv run python3 -c "
import tempfile
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig
from libzim.reader import Archive

tmp = tempfile.mkdtemp()
meta = ZimMetadata(
    title='Unicode Test',
    description='Non-ASCII content round-trip test',
    language='fra',
    name='open-repo_fr_nopic',
    flavour='nopic',
    creator='Test',
    publisher='Test',
    source_url='https://example.org'
)
config = ExportConfig()
writer = ZimWriter(metadata=meta, config=config,
                   output_path=Path(tmp) / 'unicode_test.zim', zimcheck_binary=None)
content = '<html><head><title>Test Unicode</title></head><body><h1>Espanol: nono</h1><p>Arabic: content</p></body></html>'
writer.add_article(path='index', content=content, article_type='procedure')
result = writer.create_zim(run_zimcheck=False)
archive = Archive(str(result.output_path))
entry = archive.get_entry_by_path('index')
read_back = bytes(entry.get_item().content).decode('utf-8')
assert 'Test Unicode' in read_back
assert chr(0xFFFD) not in read_back, 'Replacement character found — encoding corrupted'
print('Unicode round-trip: PASS')
"
```
Expected: `Unicode round-trip: PASS`

---

## Phase 4: Deployment Prep (est. 1 hr)

### Step 4.1 — Performance baseline

**Duration**: 10 minutes

Measure ZIM generation time for a representative article count:

```bash
uv run python3 -c "
import tempfile, time
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig

tmp = tempfile.mkdtemp()
meta = ZimMetadata(
    title='Performance Baseline',
    description='50-article baseline measurement',
    language='eng',
    name='open-repo_en_nopic',
    flavour='nopic',
    creator='Baseline',
    publisher='Baseline',
    source_url='https://example.org'
)
config = ExportConfig()
writer = ZimWriter(metadata=meta, config=config,
                   output_path=Path(tmp) / 'baseline.zim', zimcheck_binary=None)
writer.add_article(path='index',
                   content='<html><body><h1>Index</h1></body></html>',
                   article_type='procedure')
for i in range(49):
    writer.add_article(
        path=f'item/{i:04d}',
        content='<html><head><title>Item ' + str(i) + '</title></head><body><h1>Item ' + str(i) + '</h1><p>Content paragraph. Content paragraph. Content paragraph.</p></body></html>',
        article_type='procedure'
    )
start = time.time()
result = writer.create_zim(run_zimcheck=False)
elapsed = time.time() - start
print(f'50 articles: {elapsed:.2f}s, {result.file_size_bytes / 1024:.1f} KB')
print(f'Rate: {50/elapsed:.0f} articles/second')
"
```

Expected range: 0.5-5 seconds for 50 articles on RPi 5 (thermal throttling can extend this at high CPU temperature). Record the actual result as the baseline. The roadmap monitoring alert threshold is >300 seconds for a full nopic export — this baseline confirms whether the hardware is in range.

---

### Step 4.2 — Alembic migration dry run

**Duration**: 10 minutes

Verify the migration chain before applying to any real database:

```bash
alembic history
```
Expected: Shows migrations 001, 002, 003 in sequence.

```bash
alembic show 003
```
Expected: Shows `003_add_zim_exports_table` migration details with `down_revision = 002`.

To apply (only if a database is running and accessible):
```bash
alembic upgrade head
alembic current
```
Expected: `003 (head)`

Verify rollback works:
```bash
alembic downgrade 002
alembic current  # should show 002
alembic upgrade head  # return to head
```

---

### Step 4.3 — Production environment parity check

**Duration**: 5 minutes

Before deploying to production, confirm all items are checked:

- [ ] Production server has `zim-tools` installed (`zimcheck --version` works in prod)
- [ ] Production server has at least 1 GB free disk in the ZIM output directory
- [ ] `alembic upgrade head` has been run on the production database
- [ ] Production Python venv includes `libzim>=3.2,<4.0` (verify after merge + deploy)
- [ ] Production architecture is aarch64 (same as dev — wheel compatibility confirmed)
- [ ] No 0.0.0.0 bindings introduced by this change (ZimWriter is a service library, not a server — confirmed)

---

### Step 4.4 — Rollback procedure

If a post-deployment issue requires reverting:

**Code rollback**: Revert the merge commit: `git revert {merge_commit_sha}` on master. The stub paths in `create_zim()` will re-activate — ZIM exports will produce placeholder text files rather than binary ZIMs. This is a safe state (no corrupt files, just inactive feature).

**Database rollback**: `alembic downgrade 002` drops the `zim_exports` table. Safe as long as no application code is actively writing to `zim_exports`.

**Wheel rollback**: Removing libzim (`uv pip uninstall libzim`) automatically falls back to stub mode via the import guard. No code change required.

---

### Step 4.5 — Monitoring setup verification

Confirm these metrics can be observed after first production export:

| Metric | Observation point | Alert threshold |
|---|---|---|
| Export duration | `zim_exports.generation_duration_seconds` | >300s for nopic |
| zimcheck pass rate | `zim_exports.zimcheck_passed` | Any False on automated export |
| File size | `zim_exports.file_size_bytes` | <1 KB (stub) or >500 MB (nopic) |
| Stuck export | `zim_exports WHERE status='generating'` age | >90 minutes |
| CDN upload | Application logs for boto3 exceptions | Any failure |

---

### Step 4.6 — Create PR

**Duration**: 5 minutes

```bash
git push -u origin fix/phase5-zimwriter-premerge-defects
```

PR title: `fix(phase-5): pre-merge defect cleanup for ZimWriter libzim integration`

PR body must include:
- Reference to base branch `feature/zimwriter-libzim-activation`
- Description of the two defects fixed (duplicate PNG constant, silent except)
- Test count: 88+ passing with real libzim integration
- Gate note: **Do not merge until Phase 4 PR #1 has landed on master**

---

## Phase 5: Blockers and Contingencies

### Blocker: libzim wheel not available for aarch64

**Symptom**: `uv pip install libzim` fails with "No matching distribution found"

**Contingency A** (preferred): Build from source.
```bash
sudo apt-get install -y libzim-dev zlib1g-dev libicu-dev
pip install libzim --no-binary :all:
```
Adds 5-10 minutes.

**Contingency B**: Use confirmed aarch64 version: `pip install "libzim==3.7.0"`

**Contingency C** (temporary): Proceed with stub mode. The import guard means `_LIBZIM_AVAILABLE = False` and exports produce placeholder files. Feature is architecturally complete; offline exports can be activated later when the wheel is available.

---

### Blocker: zimcheck reports failures after defect fixes

**Symptom**: `zimcheck passed: False` in Step 3.3

**Diagnosis steps**:
1. Run `zimcheck --verbose /path/to/file.zim`
2. Read the specific error message

**Fixes by error**:

| Error | Cause | Fix |
|---|---|---|
| `Missing mandatory metadata: Title` | Defect 2 not fully fixed | Re-verify `except AttributeError` was removed |
| `Illustration size should be 48x48` | First PNG definition (1x1) is still active | Re-verify Defect 1 fix removed the first definition |
| `Description too long` | Test description >80 chars | Count characters in test description string |
| `Name is invalid` | Name has uppercase or spaces | Ensure name matches `[a-z0-9_]+_[a-z]{2,3}_[a-z0-9_]+` |
| `No front article` | No article with is_front_article=True | Use `article_type='procedure'` which defaults to is_front_article=True |

---

### Blocker: Tests fail after Defect 2 fix (bare except removal)

**Symptom**: Tests pass before Step 2.2 but fail after

**Diagnosis**: A test is passing a mock Creator object that raises `AttributeError` when real methods are called. The bare `except` was masking this. The fix correctly exposes it.

**Resolution**: Update the failing test to either:
- Pass a real Creator object inside a real `with Creator(...) as creator:` context, OR
- Mock all necessary Creator methods explicitly (`mock.add_metadata`, `mock.add_illustration`, `mock.config_indexing`)

This is the correct fix — the test was depending on silent failure behavior that should not exist.

---

### Blocker: Alembic migration fails

**Symptom**: `alembic upgrade head` fails with IntegrityError or OperationalError

**Diagnosis**:
- Check `alembic current` — if already at 003, the migration was already applied
- If `down_revision` mismatch: ensure `002_add_federation_conflicts.py` exists in `alembic/versions/`

**Contingency**: Apply the SQL from the `upgrade()` function manually, then stamp: `alembic stamp 003`

---

## Completion Definition

Phase 5 Candidate 1 is ready for merge when ALL of the following are true:

- [ ] `python3 -m pytest tests/ -q --tb=short` reports all tests passing (zero failures)
- [ ] ZIM magic header smoke test passes (`5a494d04` confirmed)
- [ ] Metadata readback verification passes (Title, Language, Creator, Name all readable via Archive)
- [ ] zimcheck reports `True` on an 11-article test ZIM
- [ ] Unicode content round-trip test passes
- [ ] No duplicate `_FALLBACK_ILLUSTRATION_PNG` definitions remain (grep count = 3)
- [ ] No `except AttributeError: pass` in `_apply_metadata_to_creator()` (grep returns nothing)
- [ ] `alembic history` shows migrations 001, 002, 003 in sequence
- [ ] PR created with reference to Phase 4 PR #1 as merge gate
- [ ] Phase 4 PR #1 is merged to master before this PR merges

---

## Quick Reference: All Commands

```bash
# 1. Setup branch
git checkout feature/zimwriter-libzim-activation
git checkout -b fix/phase5-zimwriter-premerge-defects

# 2. Environment
uv pip install "libzim>=3.2,<4.0"
sudo apt-get install -y zim-tools

# 3. Verify libzim
uv run python3 -c "import libzim; print(libzim.__version__)"

# 4. Baseline tests
python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=short

# 5. Check for defects (before fixing)
grep -n "_FALLBACK_ILLUSTRATION_PNG" app/services/export/zim_writer.py  # should show 4 before fix, 3 after
grep -n "except AttributeError" app/services/export/zim_writer.py        # should show 1 before fix, 0 after

# 6. After fixing defects
python3 -m pytest tests/ -q --tb=short

# 7. Alembic check
alembic history
alembic upgrade head

# 8. PR
git push -u origin fix/phase5-zimwriter-premerge-defects
```
