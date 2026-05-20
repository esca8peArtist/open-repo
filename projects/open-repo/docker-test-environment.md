---
title: "Phase 5 Candidate 1 — Docker Test Environment Configuration"
project: open-repo
phase: 5
candidate: 1
status: ready-to-use
date: 2026-05-20
---

# Docker Test Environment for Phase 5 Candidate 1

**Purpose**: Isolated test environment for libzim integration verification  
**Duration**: 15-20 minutes to set up  
**Platform**: Docker (Linux containers, works on any host OS)

---

## Quick Start (5 minutes)

### Option A: Test on Current System (Recommended)

```bash
# No Docker needed — run tests directly
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# Install dependencies
pip install -e ".[dev]"

# Run all tests
python3 -m pytest tests/integration/test_export_pipeline.py -v

# Verify 88 tests pass
```

This is the fastest path. The environment already has libzim 3.9.0 installed.

---

## Option B: Isolated Docker Container

### Build Test Image

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo

cat > Dockerfile.test << 'EOF'
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    zim-tools \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy backend code
COPY backend /app

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel && \
    pip install -e ".[dev]"

# Run tests by default
ENTRYPOINT ["python3", "-m", "pytest", "tests/integration/test_export_pipeline.py", "-v"]
EOF

# Build
docker build -t open-repo-phase5-test:latest -f Dockerfile.test .
```

### Run Tests in Container

```bash
# Run all 88 tests
docker run --rm open-repo-phase5-test:latest

# Run specific test
docker run --rm open-repo-phase5-test:latest \
  python3 -m pytest tests/integration/test_export_pipeline.py::TestZimWriter -v

# Interactive shell
docker run --rm -it open-repo-phase5-test:latest /bin/bash
```

### Test Output Example

```
tests/integration/test_export_pipeline.py::TestZimEntry::test_valid_zimentry_initializes PASSED
tests/integration/test_export_pipeline.py::TestZimEntry::test_zimentry_rejects_absolute_path PASSED
...
tests/integration/test_export_pipeline.py::TestOPDSGenerator::test_entries_sorted_alphabetically PASSED
tests/integration/test_export_pipeline.py::TestLibZIMIntegration::test_fallback_png_is_valid_48x48 PASSED
tests/integration/test_export_pipeline.py::TestLibZIMIntegration::test_zim_magic_bytes_present PASSED
============================== 88 passed in 0.15s ==============================
```

---

## Manual Test: Create Real ZIM File

### Test 1: Minimal 5-Article Export

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

python3 << 'EOF'
import tempfile
from pathlib import Path
from app.services.export.zim_writer import (
    ZimWriter, ZimMetadata, ExportConfig, ExportScope
)

print("=== Test 1: Minimal 5-Article ZIM ===")

with tempfile.TemporaryDirectory() as tmpdir:
    output_path = Path(tmpdir) / "test_minimal.zim"
    
    metadata = ZimMetadata(
        title="Test Minimal",
        description="5-article test",
        language="eng",
        name="test-minimal_en_nopic",
        flavour="nopic",
        creator="Test",
        publisher="Test",
        source_url="http://test"
    )
    
    config = ExportConfig(
        scope=ExportScope.LOCAL_ONLY,
        flavour="nopic"
    )
    
    writer = ZimWriter(metadata=metadata, config=config, output_path=output_path)
    
    # Add 5 articles
    for i in range(5):
        writer.add_article(
            path=f"test/article-{i}",
            title=f"Article {i}",
            content=f"<h1>Article {i}</h1><p>Content {i}</p>",
        )
    
    result = writer.create_zim()
    
    # Verify
    assert output_path.exists()
    file_size = output_path.stat().st_size
    magic = output_path.read_bytes()[:4]
    
    print(f"✓ Test passed")
    print(f"  File: {output_path.name}")
    print(f"  Size: {file_size} bytes")
    print(f"  Magic: {magic!r}")
    print(f"  Articles: {result.article_count}")
    print(f"  SHA-256: {result.sha256[:16]}...")
EOF
```

**Expected Output**:
```
=== Test 1: Minimal 5-Article ZIM ===
✓ Test passed
  File: test_minimal.zim
  Size: 3456 bytes
  Magic: b'\x5aIM\x04'
  Articles: 5
  SHA-256: a1b2c3d4e5f6...
```

---

### Test 2: Large 50-Article Export with Xapian Search

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

python3 << 'EOF'
import tempfile
from pathlib import Path
from app.services.export.zim_writer import (
    ZimWriter, ZimMetadata, ExportConfig, ExportScope
)
from libzim.reader import Archive

print("=== Test 2: Large 50-Article Export with Search ===")

with tempfile.TemporaryDirectory() as tmpdir:
    output_path = Path(tmpdir) / "test_large.zim"
    
    metadata = ZimMetadata(
        title="Test Large Export",
        description="50-article agriculture domain",
        language="eng",
        name="test-large_en_agri",
        flavour="agriculture",
        creator="Test",
        publisher="Test",
        source_url="http://test"
    )
    
    config = ExportConfig(
        scope=ExportScope.DOMAIN,
        scope_value="agriculture",
        flavour="agriculture"
    )
    
    writer = ZimWriter(metadata=metadata, config=config, output_path=output_path)
    
    # Add 50 articles with agriculture keywords
    for i in range(50):
        title = f"Agriculture Article {i}"
        content = f"""
        <h1>{title}</h1>
        <p>This article discusses biosand filters, water purification, and sustainable farming.</p>
        <p>Keywords: agriculture, water, farming, biosand, purification, sustainability</p>
        """
        writer.add_article(
            path=f"agriculture/article-{i:03d}",
            title=title,
            content=content,
        )
    
    result = writer.create_zim()
    
    # Verify file
    print(f"✓ ZIM created: {output_path.name}")
    print(f"  Size: {result.file_size_bytes} bytes")
    print(f"  Articles: {result.article_count}")
    
    # Test search via libzim reader
    print(f"\nTesting offline search...")
    try:
        archive = Archive(str(output_path))
        
        # Search for agriculture keyword
        search_results = archive.search("biosand")
        result_count = len(list(search_results))
        
        if result_count > 0:
            print(f"✓ Search works! Found {result_count} results for 'biosand'")
        else:
            print(f"⚠️  Search returned 0 results for 'biosand'")
        
        # Verify metadata
        title = archive.get_metadata("Title")
        print(f"✓ Metadata readable: Title = '{title}'")
        
    except Exception as e:
        print(f"✗ Search test failed: {e}")

EOF
```

**Expected Output**:
```
=== Test 2: Large 50-Article Export with Search ===
✓ ZIM created: test_large.zim
  Size: 45678 bytes
  Articles: 50

Testing offline search...
✓ Search works! Found 50 results for 'biosand'
✓ Metadata readable: Title = 'Test Large Export'
```

---

## Test Data Preparation

### Synthetic Database for Testing

The existing test suite already includes synthetic Phase 4 content data. To create custom test data:

```python
# Example: Create domain-specific test articles

test_articles = [
    {
        "path": "agriculture/biosand-filter",
        "title": "Building a Biosand Filter",
        "content": """
        <h1>Biosand Water Filter Construction</h1>
        <p>A biosand filter is a simple, effective water purification system...</p>
        <ul>
            <li>Sand: 20cm</li>
            <li>Gravel: 5cm</li>
            <li>Charcoal: 3cm</li>
        </ul>
        """,
        "domain": "agriculture",
        "cid": "biosand-filter"
    },
    {
        "path": "agriculture/drip-irrigation",
        "title": "Drip Irrigation Systems",
        "content": "<h1>Drip Irrigation</h1><p>Efficient water delivery to crops...</p>",
        "domain": "agriculture",
        "cid": "drip-irrigation"
    }
]

# Feed to ZimWriter
for article in test_articles:
    writer.add_article(
        path=article["path"],
        title=article["title"],
        content=article["content"]
    )
```

---

## Verification Commands

### 1. Check ZIM File Magic Bytes

```bash
# ZIM files start with \x5a\x49\x4d\x04 (ZIM magic)
xxd -l 16 <zim-file> | head

# Expected:
# 00000000: 5a49 4d04 0000 0000 ...  ZIM\x04...
```

### 2. List Articles in ZIM

```bash
python3 << 'EOF'
from libzim.reader import Archive

archive = Archive("test.zim")
print(f"Article count: {len(list(archive.articles()))}")

for article in archive.articles():
    print(f"  - {article.path}: {article.title}")
EOF
```

### 3. Test Full-Text Search

```bash
python3 << 'EOF'
from libzim.reader import Archive

archive = Archive("test.zim")
results = archive.search("biosand water filter")
for result in results:
    print(f"Match: {result.title} (path: {result.path})")
EOF
```

### 4. Verify Metadata

```bash
python3 << 'EOF'
from libzim.reader import Archive

archive = Archive("test.zim")
metadata_fields = [
    "Title", "Description", "Language", "Creator", 
    "Publisher", "Date", "Name", "Flavour"
]

for field in metadata_fields:
    value = archive.get_metadata(field)
    print(f"{field}: {value}")
EOF
```

### 5. Compute and Verify SHA-256

```bash
# Create .sha256 sidecar file
sha256sum test.zim > test.zim.sha256

# Verify
sha256sum -c test.zim.sha256
# Expected: test.zim: OK
```

---

## CI Integration

### GitHub Actions Workflow (Optional)

If deploying to GitHub, add this to `.github/workflows/test-phase5.yml`:

```yaml
name: Phase 5 Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          cd backend
          pip install -e ".[dev]"
      
      - name: Install zimcheck
        run: sudo apt-get install -y zim-tools
      
      - name: Run tests
        run: |
          cd backend
          python3 -m pytest tests/integration/test_export_pipeline.py -v
      
      - name: Test ZIM generation
        run: |
          cd backend
          python3 << 'EOF'
          import tempfile
          from pathlib import Path
          from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope
          
          with tempfile.TemporaryDirectory() as tmpdir:
              output = Path(tmpdir) / "ci-test.zim"
              metadata = ZimMetadata(
                  title="CI Test", description="Test", language="eng",
                  name="ci-test_en_nopic", flavour="nopic",
                  creator="CI", publisher="CI", source_url="http://ci"
              )
              writer = ZimWriter(metadata, ExportConfig(), output)
              writer.add_article("test", "Test", "<p>Test</p>")
              result = writer.create_zim()
              assert output.exists()
              assert result.article_count == 1
          EOF
```

---

## Troubleshooting

### Problem: "libzim not found"
**Solution**: Ensure venv is activated: `source .venv/bin/activate`

### Problem: "ModuleNotFoundError: app.services..."
**Solution**: Run from backend directory: `cd backend && python3 ...`

### Problem: "zimcheck not found"
**Solution**: Install zim-tools: `apt-get install zim-tools` (optional)

### Problem: Search returns no results
**Solution**: Verify article titles are non-empty; Xapian requires non-empty titles for indexing

### Problem: "Invalid ZIM magic bytes"
**Solution**: Ensure libzim is properly installed; check import in test script

---

## Performance Expectations

| Test | Time | Notes |
|------|------|-------|
| Import libzim | <1s | First import caches module |
| Create 5-article ZIM | 0.5s | Minimal export |
| Create 50-article ZIM | 2-3s | Agriculture domain |
| Search (50 articles) | <1s | Offline Xapian search |
| 88 existing tests | 0.15s | Full test suite |
| 12 new libzim tests | 5-10s | Real ZIM generation + verification |

**Total verification time**: ~15 seconds

---

## Summary

- ✅ Quick option: Run tests directly (88 tests in 0.15s)
- ✅ Isolated option: Use Docker for clean environment
- ✅ Manual tests: Create real ZIMs and verify offline features
- ✅ Verification: 5 commands to check magic bytes, search, metadata
- ✅ CI ready: GitHub Actions workflow template provided

All tools needed are already present. No additional system packages required beyond Docker (if using Option B).

