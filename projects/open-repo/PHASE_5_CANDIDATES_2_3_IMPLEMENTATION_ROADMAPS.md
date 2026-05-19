---
title: "Phase 5 Candidates 2 & 3 — Combined Implementation Roadmaps"
project: open-repo
phase: 5
candidates: [2, 3]
status: ready-for-user-approval
date: 2026-05-19
decision_window: "May 25-26"
execution_start: "June 1+ (post-approval)"
---

# Phase 5 Candidates 2 & 3: Combined Implementation Roadmaps

**Purpose**: Pre-staged, production-ready implementation roadmaps for Candidates 2 and 3 to enable rapid execution immediately following user approval (May 25-26 decision window).

**Candidate 1 (ZimWriter)**: Already detailed in `PHASE_5_CANDIDATE_1_ZIMWRITER_IMPLEMENTATION_ROADMAP.md`. This document picks up where Candidate 1 ends.

**Decision scope**: User approves which candidates to implement. Candidate 1 is the prerequisite for both; neither Candidate 2 nor 3 requires the other.

---

## Summary Table

| Candidate | Title | Effort | Dependency | Merge sequence |
|-----------|-------|--------|-----------|----------------|
| **1** | ZimWriter libzim integration | 8-11 hrs | None (structural prerequisite) | First |
| **2** | OPDS feedgen catalog | 8-11 hrs | Candidate 1 must produce valid ZIM output | Second |
| **3** | README accuracy pass + contributor quickstart | 2-3 hrs | None (fully independent) | Any order |

**Combined execution budget (Candidates 2 + 3)**: 10-14 hours over June 1-12 window.

---

## Part 1: Candidate 2 — OPDS Feedgen Catalog Migration

### 1.1 What This Delivers

OPDS (Open Publication Distribution System) 1.2 is the in-app catalog standard that Kiwix readers use to discover downloadable archives. Without a valid OPDS catalog, users must know the direct CDN URL to download ZIM files. With OPDS, Kiwix Android (F-Droid), Kiwix Desktop, and kiwix-serve can display the open-repo archive library in their built-in browser, enabling one-click install.

**Four endpoints delivered**:
- `GET /opds/v2/root.xml` — Navigation catalog (links to sub-feeds)
- `GET /opds/v2/entries` — Acquisition feed (one entry per ZIM export with download links)
- `GET /opds/v2/entry/{uuid}` — Single entry view with version history
- `GET /opds/v2/searchdescription.xml` — OpenSearch description for in-app search

**User-facing outcome**: A user types the OPDS URL into Kiwix Android, sees "Open-Repo Full Library (English, 22 MB)" with an Install button, taps it, and the ZIM downloads automatically.

### 1.2 Architecture: Data Flow Post-Integration

```
                zim_exports TABLE
                (populated by ZimWriter, Candidate 1)
                SELECT WHERE is_current=True AND cdn_url IS NOT NULL
                          │
                          ▼
                ┌──────────────────────────────┐
                │  OPDSCatalogService           │
                │  .regenerate()                │
                │                               │
                │  Called after each successful │
                │  ZimWriter.create_zim() run   │
                └──────────────┬───────────────┘
                               │
                               ▼
                ┌──────────────────────────────┐
                │  OPDSEntry.from_zim_export()  │
                │  (new factory classmethod)    │
                │                               │
                │  Maps ZimExport ORM row to    │
                │  OPDSEntry dataclass          │
                │  - Validates cdn_url present  │
                │  - Validates sha256 present   │
                └──────────────┬───────────────┘
                               │
                               ▼
                ┌──────────────────────────────┐
                │  OPDSGenerator               │
                │  (rewritten with feedgen)    │
                │                               │
                │  fg = FeedGenerator()         │
                │  fg.id(...), fg.title(...)    │
                │  for entry: fg.add_entry()    │
                │  _add_dc_elements_to_feed()   │
                │  return fg.atom_str()         │
                └──────────────┬───────────────┘
                               │
                ┌──────────────┼──────────────┐
                ▼              ▼              ▼
         /opds/v2/      /opds/v2/    /opds/v2/
         root.xml        entries    entry/{uuid}
                               │
                               ▼
                ┌──────────────────────────────┐
                │  Kiwix Android / Desktop /   │
                │  kiwix-serve                 │
                │  One-click ZIM download      │
                └──────────────────────────────┘
```

### 1.3 Exact Code Entry Points and Files to Modify

**Effort breakdown by file**:

| File | Change type | Estimated time |
|------|------------|---------------|
| `pyproject.toml` | Add feedgen dependency (1 line) | 5 min |
| `app/services/export/opds_generator.py` | Add feedgen import guard, implement `from_zim_export()`, rewrite generate methods, add DC post-processor | 4-5 hrs |
| `app/routers/opds.py` | New file: 4 FastAPI endpoints | 1-1.5 hrs |
| `app/main.py` | Register OPDS router (1 line) | 5 min |
| `tests/unit/test_opds_generator.py` | Add 4 new tests to existing 19 (23 total) | 1-1.5 hrs |
| `tests/integration/test_opds_kiwix.py` | New file: kiwix-serve integration test | 1 hr |

**Total file changes**: 4 modified, 2 new.

#### File 1: `pyproject.toml` — add one dependency

```toml
# ADD under [project.dependencies]:
"feedgen>=0.9,<2.0",
```

Pin to `<2.0` to prevent automatic upgrades to potentially incompatible future versions. The version ceiling is deliberate: feedgen has an inactive release cadence and a future major bump could introduce breaking changes. The `<2.0` pin is safe for the foreseeable lifecycle of this project.

#### File 2: `app/services/export/opds_generator.py` — four changes

**Change 2a: Add feedgen import guard** (after existing imports, after line 41)

```python
try:
    from feedgen.feed import FeedGenerator
    from feedgen.entry import FeedEntry
    _FEEDGEN_AVAILABLE = True
except ImportError:
    _FEEDGEN_AVAILABLE = False
    FeedGenerator = None  # type: ignore[assignment,misc]
    FeedEntry = None      # type: ignore[assignment,misc]
```

This guard allows the module to load in test environments where feedgen is not installed. The fallback is the existing `xml.etree` path. Remove the guard once feedgen is confirmed stable in CI.

**Change 2b: Implement `OPDSEntry.from_zim_export()` classmethod** (add to `OPDSEntry` class, after the existing `from_dict()` classmethod, around line 174)

This is the critical bridge between Candidate 1 (ZimWriter) and Candidate 2 (OPDS). Every OPDS acquisition entry originates here.

```python
@classmethod
def from_zim_export(cls, export: "ZimExport") -> "OPDSEntry":
    """
    Construct an OPDSEntry from a ZimExport ORM row (zim_exports table).

    This is the primary construction path for auto-generated OPDS entries.
    Called by OPDSCatalogService after each successful ZimWriter.create_zim() run.

    Args:
        export: ZimExport SQLAlchemy model instance. Must have status='available'
                and a non-None cdn_url before calling this method.

    Returns:
        OPDSEntry ready to be added to OPDSGenerator.

    Raises:
        ValueError: If export.cdn_url is None (CDN upload must complete first).
        ValueError: If export.sha256 is None (ZIM must be validated first).
    """
    if not export.cdn_url:
        raise ValueError(
            f"ZimExport {export.id} (name={export.name}) has no cdn_url. "
            f"CDN upload must complete before adding to OPDS catalog."
        )
    if not export.sha256:
        raise ValueError(
            f"ZimExport {export.id} has no sha256 checksum. "
            f"ZIM must be validated before adding to catalog."
        )
    return cls(
        uuid=export.zim_uuid,
        title=export.title,
        name=export.name,
        flavour=export.flavour,
        language=export.language,
        period=export.period,
        description=export.description,
        download_url=export.cdn_url,
        file_size_bytes=export.file_size_bytes,
        sha256_checksum=export.sha256,
        article_count=export.article_count,
        generated_at=export.completed_at or export.created_at,
        is_reference=export.is_reference,
        version_history=[],  # populated by OPDSCatalogService separately
    )
```

**Change 2c: Rewrite generate methods with feedgen** (replace existing stub generate methods)

```python
def generate_root_catalog(self) -> bytes:
    """Generate the OPDS root navigation catalog."""
    if _FEEDGEN_AVAILABLE:
        return self._generate_root_catalog_feedgen()
    return self._generate_root_catalog_etree()  # existing fallback

def _generate_root_catalog_feedgen(self) -> bytes:
    entries_url = self.catalog_url.replace("root.xml", "entries")
    search_url = self.catalog_url.replace("root.xml", "searchdescription.xml")

    fg = FeedGenerator()
    fg.id(f"urn:uuid:{self.node_uuid}")
    fg.title(f"{self.node_name} Offline Library Catalog")
    fg.author({"name": self.node_name, "uri": self.node_url})
    fg.updated(self._generated_at)
    fg.link(href=self.catalog_url, rel="self", type=MIME_OPDS_NAV)
    fg.link(href=self.catalog_url, rel="start", type=MIME_OPDS_NAV)
    fg.link(href=search_url, rel="search", type=MIME_OPENSEARCH)

    fe = fg.add_entry()
    fe.id(f"urn:uuid:{self.node_uuid}:all")
    fe.title("All Offline Exports")
    fe.updated(self._generated_at)
    fe.summary(f"{len(self._entries)} offline ZIM file(s) available for download")
    fe.link(href=entries_url, rel="subsection", type=MIME_OPDS_ACQ)

    return fg.atom_str(pretty=True)

def generate_acquisition_feed(self) -> bytes:
    """Generate the OPDS acquisition feed."""
    if _FEEDGEN_AVAILABLE:
        raw = self._generate_acquisition_feed_feedgen()
        return self._add_dc_elements_to_feed(raw, list(self._entries.values()))
    return self._generate_acquisition_feed_etree()  # existing fallback

def _generate_acquisition_feed_feedgen(self) -> bytes:
    entries_url = self.catalog_url.replace("root.xml", "entries")

    fg = FeedGenerator()
    fg.id(f"urn:uuid:{self.node_uuid}:entries")
    fg.title(f"{self.node_name} — All Offline Exports")
    fg.author({"name": self.node_name, "uri": self.node_url})
    fg.updated(self._generated_at)
    fg.link(href=entries_url, rel="self", type=MIME_OPDS_ACQ)
    fg.link(href=self.catalog_url, rel="start", type=MIME_OPDS_NAV)

    for entry in self.get_entries_sorted():
        self._add_feedgen_entry(fg, entry)

    return fg.atom_str(pretty=True)

def _add_feedgen_entry(
    self, fg: "FeedGenerator", entry: "OPDSEntry"
) -> None:
    fe = fg.add_entry()
    fe.id(entry.entry_id)
    fe.title(entry.title)
    fe.updated(entry.generated_at)
    fe.summary(entry.description)
    fe.link(
        href=entry.download_url,
        rel="http://opds-spec.org/acquisition",
        type=MIME_ZIM,
        title=entry.filename,
    )
    fe.link(
        href=entry.download_url + ".sha256",
        rel="related",
        type="text/plain",
        title=f"SHA-256 checksum for {entry.filename}",
    )
    if entry.illustration_url:
        fe.link(
            href=entry.illustration_url,
            rel="http://opds-spec.org/image",
            type="image/png",
        )
    for prev in sorted(
        entry.version_history, key=lambda v: v.period, reverse=True
    )[:self.max_version_history]:
        fe.link(
            href=prev.download_url,
            rel="related",
            type=MIME_ZIM,
            title=f"Previous version: {prev.period}",
        )
```

**Change 2d: Add Dublin Core post-processor** (new private method in `OPDSGenerator`)

feedgen generates valid Atom RFC 4287 but does not have native OPDS or Dublin Core extensions. The `dc:language` and `dc:issued` elements (OPDS 1.2 "SHOULD") must be added via a post-processing step using `lxml`:

```python
def _add_dc_elements_to_feed(
    self, xml_bytes: bytes, entries: list["OPDSEntry"]
) -> bytes:
    """
    Post-process feedgen Atom output to add Dublin Core namespace elements.

    feedgen generates valid Atom but lacks dc:language, dc:issued, and
    opensearch:totalResults. This method parses the output and appends them.

    Kiwix does not require these elements to discover or download archives,
    so their absence is not a blocking failure. The try/except ensures a
    degraded-mode fallback (without DC elements) if lxml is unavailable.
    """
    try:
        from lxml import etree
    except ImportError:
        logger.warning(
            "lxml not available; dc:language and dc:issued will be absent from "
            "OPDS feed. Install lxml for full OPDS 1.2 compliance."
        )
        return xml_bytes

    ATOM_NS = "http://www.w3.org/2005/Atom"
    DC_NS = "http://purl.org/dc/terms/"
    OPENSEARCH_NS = "http://a9.com/-/spec/opensearch/1.1/"

    root = etree.fromstring(xml_bytes)

    # Add opensearch:totalResults to feed root
    total_elem = etree.SubElement(root, f"{{{OPENSEARCH_NS}}}totalResults")
    total_elem.text = str(len(entries))

    # Add dc:language and dc:issued to each entry
    entry_map = {e.entry_id: e for e in entries}
    for entry_elem in root.findall(f"{{{ATOM_NS}}}entry"):
        id_elem = entry_elem.find(f"{{{ATOM_NS}}}id")
        if id_elem is None:
            continue
        opds_entry = entry_map.get(id_elem.text)
        if opds_entry is None:
            continue
        lang_elem = etree.SubElement(entry_elem, f"{{{DC_NS}}}language")
        lang_elem.text = opds_entry.language
        issued_elem = etree.SubElement(entry_elem, f"{{{DC_NS}}}issued")
        issued_elem.text = opds_entry.period

    return etree.tostring(
        root, xml_declaration=True, encoding="utf-8", pretty_print=True
    )
```

#### File 3: `app/routers/opds.py` — new file (4 endpoints)

Create this file at `app/routers/opds.py`. The module does not currently exist; it is a new file.

```python
"""
OPDS 1.2 catalog endpoints for Kiwix in-app archive discovery.

Endpoints:
    GET /opds/v2/root.xml         — Navigation catalog
    GET /opds/v2/entries          — Acquisition feed (all current exports)
    GET /opds/v2/entry/{uuid}     — Single export entry with version history
    GET /opds/v2/searchdescription.xml — OpenSearch description

All endpoints return Atom XML with Content-Type: application/atom+xml.
"""

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.services.export.opds_generator import OPDSGenerator, OPDSEntry
from app.models import ZimExport, ZimExportStatus  # from Candidate 1

router = APIRouter(prefix="/opds/v2", tags=["opds"])

CONTENT_TYPE_ATOM = "application/atom+xml; charset=utf-8"
CONTENT_TYPE_OPENSEARCH = "application/opensearchdescription+xml; charset=utf-8"


def _make_generator(db_url: str, base_url: str) -> OPDSGenerator:
    """Construct an OPDSGenerator with node configuration from environment."""
    import os
    return OPDSGenerator(
        node_uuid=os.environ.get("NODE_UUID", "550e8400-e29b-41d4-a716-446655440000"),
        node_name=os.environ.get("NODE_NAME", "Open-Repo Node"),
        node_url=os.environ.get("NODE_URL", base_url),
        catalog_url=f"{base_url}/opds/v2/root.xml",
    )


async def _load_current_exports(db: AsyncSession) -> list[ZimExport]:
    """Query zim_exports for current available exports."""
    from sqlalchemy import select
    result = await db.execute(
        select(ZimExport).where(
            ZimExport.is_current.is_(True),
            ZimExport.status == ZimExportStatus.AVAILABLE,
            ZimExport.cdn_url.isnot(None),
        )
    )
    return list(result.scalars().all())


@router.get("/root.xml", response_class=Response)
async def opds_root_catalog(
    request,
    db: AsyncSession = Depends(get_db),
) -> Response:
    """OPDS navigation catalog root."""
    base_url = str(request.base_url).rstrip("/")
    exports = await _load_current_exports(db)
    generator = _make_generator(str(request.base_url), base_url)
    for export in exports:
        generator.add_entry(OPDSEntry.from_zim_export(export))
    return Response(
        content=generator.generate_root_catalog(),
        media_type=CONTENT_TYPE_ATOM,
        headers={"Cache-Control": "public, max-age=3600"},
    )


@router.get("/entries", response_class=Response)
async def opds_acquisition_feed(
    db: AsyncSession = Depends(get_db),
    request=None,
) -> Response:
    """OPDS acquisition feed: all current ZIM exports."""
    base_url = str(request.base_url).rstrip("/")
    exports = await _load_current_exports(db)
    generator = _make_generator(str(request.base_url), base_url)
    for export in exports:
        generator.add_entry(OPDSEntry.from_zim_export(export))
    return Response(
        content=generator.generate_acquisition_feed(),
        media_type=CONTENT_TYPE_ATOM,
        headers={"Cache-Control": "public, max-age=3600"},
    )


@router.get("/entry/{zim_uuid}", response_class=Response)
async def opds_single_entry(
    zim_uuid: str,
    db: AsyncSession = Depends(get_db),
    request=None,
) -> Response:
    """Single ZIM export entry with version history."""
    from sqlalchemy import select
    result = await db.execute(
        select(ZimExport).where(ZimExport.zim_uuid == zim_uuid)
    )
    export = result.scalar_one_or_none()
    if export is None:
        raise HTTPException(status_code=404, detail=f"Export {zim_uuid} not found")

    base_url = str(request.base_url).rstrip("/")
    generator = _make_generator(str(request.base_url), base_url)
    generator.add_entry(OPDSEntry.from_zim_export(export))
    return Response(
        content=generator.generate_acquisition_feed(),
        media_type=CONTENT_TYPE_ATOM,
    )


@router.get("/searchdescription.xml", response_class=Response)
async def opds_search_description(request=None) -> Response:
    """OpenSearch description for Kiwix in-app search integration."""
    base_url = str(request.base_url).rstrip("/")
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
  <ShortName>Open-Repo Library</ShortName>
  <Description>Search Open-Repo offline archives</Description>
  <Url type="application/atom+xml;profile=opds-catalog;kind=acquisition"
       template="{base_url}/opds/v2/entries?q={{searchTerms}}"/>
</OpenSearchDescription>""".encode("utf-8")
    return Response(content=xml, media_type=CONTENT_TYPE_OPENSEARCH)
```

#### File 4: `app/main.py` — register OPDS router (1 line addition)

Locate the section where other routers are registered (around line 40-60 in `main.py`) and add:

```python
from app.routers.opds import router as opds_router
app.include_router(opds_router)
```

This line follows the same pattern as other router registrations in the file. No other changes to `main.py` are needed.

### 1.4 Metadata Mapping: ZimExport ORM to OPDS Feed Fields

| `zim_exports` column | OPDS element | Required by spec | Kiwix behavior if absent |
|---------------------|-------------|-----------------|--------------------------|
| `zim_uuid` | `<id>urn:uuid:{uuid}</id>` | MUST | Feed entry rejected |
| `title` | `<title>{title}</title>` | MUST | Feed entry rejected |
| `completed_at` | `<updated>{datetime}Z</updated>` | MUST | Feed entry rejected |
| `cdn_url` | `<link rel="http://opds-spec.org/acquisition" href=.../>` | MUST for ACQ feed | Entry not downloadable |
| `description` | `<summary>{desc}</summary>` | SHOULD | Blank catalog entry description |
| `language` | `<dc:language>eng</dc:language>` | SHOULD | Silently ignored |
| `period` | `<dc:issued>2026-05</dc:issued>` | SHOULD | Silently ignored |
| `file_size_bytes` | `<link ... length="{bytes}"/>` | SHOULD | File size not shown in Kiwix UI |
| `sha256` | `<link rel="related" href="{url}.sha256"/>` | No (project standard) | No checksum sidecar link |
| `is_reference` | `<category term="archive" .../>` | No | No "Archive" badge in Kiwix |

### 1.5 Test Matrix

**8 required test scenarios** (4 new tests added to the existing 19 in `test_opds_generator.py`):

| # | Test ID | Category | Priority | What it verifies |
|---|---------|----------|----------|-----------------|
| 1 | `test_opds_root_catalog_valid_atom` | Unit | P0 | Root catalog is well-formed Atom XML; `validate_opds_xml()` returns empty list |
| 2 | `test_opds_acquisition_feed_has_required_elements` | Unit | P0 | Each entry has `<id>`, `<title>`, `<updated>`, and `<link rel="http://opds-spec.org/acquisition">` |
| 3 | `test_opds_acquisition_link_type_is_zim` | Unit | P0 | Acquisition link MIME type is `application/x-zim` |
| 4 | `test_opds_from_zim_export_factory` | Unit | P0 | Factory maps all fields correctly from mocked ZimExport ORM row |
| 5 | `test_opds_from_zim_export_raises_on_missing_cdn_url` | Unit | P1 | `from_zim_export()` raises `ValueError` for ZimExport with `cdn_url=None` |
| 6 | `test_opds_dc_language_element_present` | Unit | P1 | Feed XML contains `<dc:language>eng</dc:language>` in entry |
| 7 | `test_opds_feed_parseable_by_kiwix_catalog_parser` | Integration | P0 | kiwix-serve accepts the OPDS URL and lists the archive |
| 8 | `test_opds_search_description_valid` | Unit | P1 | `generate_search_description()` is well-formed XML with `<Url>` element |

**Test execution commands**:

```bash
# All OPDS unit tests:
uv run pytest tests/unit/test_opds_generator.py -v

# Integration test (requires Docker with kiwix-serve):
docker run -d -p 8080:80 kiwix/kiwix-serve
uv run pytest tests/integration/test_opds_kiwix.py -v -m integration

# Full OPDS suite:
uv run pytest tests/ -k "opds" -v
```

### 1.6 Integration Sequence with Candidate 1

**The merge dependency is hard**: Candidate 2 cannot merge before Candidate 1 because `OPDSEntry.from_zim_export()` requires `ZimExport` ORM rows, which are created by Candidate 1's Alembic migration.

**Practical development sequence** (allows maximum parallelism):

```
Step 0: Verify Candidate 1 merged and zim_exports table has real rows
  SELECT * FROM zim_exports WHERE status='available' LIMIT 1;
  -- Must return at least one row with cdn_url populated

Step 1: Create feature branch
  git checkout -b feature/opds-feedgen-migration

Step 2: Add feedgen dependency
  pyproject.toml: add "feedgen>=0.9,<2.0"
  uv pip install feedgen
  python -c "from feedgen.feed import FeedGenerator; print('OK')"

Step 3: Add feedgen import guard to opds_generator.py
  Place after existing imports; verify _FEEDGEN_AVAILABLE flag works

Step 4: Implement OPDSEntry.from_zim_export()
  Write factory method (Change 2b above)
  Write test_opds_from_zim_export_factory using mocked ZimExport
  Run test: uv run pytest tests/unit/test_opds_generator.py::test_opds_from_zim_export_factory

Step 5: Run existing 19 OPDS tests
  uv run pytest tests/unit/test_opds_generator.py -v
  All 19 should pass — from_zim_export is new code, not a replacement

Step 6: Write feedgen generate methods
  Implement _generate_root_catalog_feedgen()
  Implement _generate_acquisition_feed_feedgen()
  Implement _add_dc_elements_to_feed()
  Update generate_root_catalog() and generate_acquisition_feed() to use feedgen path

Step 7: Run all 23 OPDS tests
  uv run pytest tests/unit/test_opds_generator.py -v
  Fix any test failures from feedgen namespace handling differences
  (Likely: exact XML string comparisons need to become structure checks)

Step 8: Create app/routers/opds.py
  Implement all 4 endpoints (File 3 above)
  Register in app/main.py (1 line)

Step 9: Manual kiwix-serve verification
  Start FastAPI backend
  Point kiwix-serve at /opds/v2/root.xml
  Confirm Kiwix lists the archive with an Install button

Step 10: Integration test
  Write tests/integration/test_opds_kiwix.py
  Requires Docker: docker run -d -p 8080:80 kiwix/kiwix-serve

Step 11: Rebase on main (pull Candidate 1 merge)
  git fetch origin main
  git rebase origin/main
  Run full test suite: uv run pytest tests/ -v

Step 12: PR creation
  Title: "feat(phase-5): OPDS feedgen catalog with ZimExport factory"
  Must not merge until Candidate 1 has produced at least one real ZIM export
  Target branch: main
```

### 1.7 Risk Assessment

**Risk 1: feedgen cannot set OPDS acquisition link relation URI**
- Probability: Medium (feedgen's `add_link()` accepts string `rel` values but behavior with full URIs is untested against Kiwix's parser)
- Impact: High (Kiwix shows no Install button)
- Detection: `test_opds_acquisition_link_type_is_zim` fails, or Kiwix shows "Browse" not "Install"
- Mitigation: Test `fe.link(href=..., rel="http://opds-spec.org/acquisition", type="application/x-zim")` as the first change in Step 6. If feedgen escapes the URI, use the existing `xml.etree` fallback for this specific link only.

**Risk 2: Kiwix silently rejects malformed namespace declarations**
- Probability: Medium (OPDS namespace handling is a known silent-failure source)
- Impact: High (Kiwix library shows nothing, no error message)
- Detection: Manual test — point Kiwix Android at the OPDS URL; library stays empty
- Mitigation: Compare generated XML against the known-good example in `PHASE_5_ARCHITECTURE.md` Appendix C. Run `xmllint --noout` on the feed before testing in Kiwix.

**Risk 3: feedgen inactive maintenance causes import failure**
- Probability: Low (35K weekly downloads; current version stable)
- Impact: Low (xml.etree fallback activates automatically via `_FEEDGEN_AVAILABLE` flag)
- Detection: `uv pip install feedgen` fails or `from feedgen.feed import FeedGenerator` raises ImportError
- Mitigation: The import guard handles this at runtime. The xml.etree fallback is always available and produces valid Atom XML.

**Risk 4: `from_zim_export()` factory maps incorrect field**
- Probability: Low (field mapping is straightforward 1-to-1)
- Impact: High (wrong download URLs or file sizes mislead users)
- Detection: `test_opds_from_zim_export_factory` must verify every field individually
- Mitigation: The factory test must not just verify "construction succeeds" — it must assert each field value matches the mocked export row's corresponding column.

### 1.8 Deployment Gate: OPDS-Specific Pre-Deployment Verification

These items are in addition to the shared pre-deployment items in Section 3 (Deployment Gates).

```
[ ] Candidate 1 (ZimWriter) gate fully complete — all items checked
[ ] zim_exports has at least one row with status='available' and cdn_url populated
[ ] OPDSEntry.from_zim_export() tested with real ZimExport DB row (not mock)
[ ] uv run pytest tests/unit/test_opds_generator.py -v — all 23 tests pass
[ ] GET /opds/v2/root.xml returns 200 with Content-Type: application/atom+xml
[ ] GET /opds/v2/entries returns acquisition feed with at least one <entry>
[ ] OPDSGenerator.validate_opds_xml(feed_bytes) returns empty list
[ ] xmllint --noout on feed XML passes (no namespace errors)
[ ] Kiwix Android (F-Droid): Add library URL -> shows open-repo archives -> Install button visible
[ ] Kiwix Desktop: Add library URL -> shows archive list
[ ] GET /opds/v2/searchdescription.xml returns well-formed XML
[ ] OPDS catalog auto-regenerates after new ZimWriter export completes
[ ] Version history: second export for same flavour appears in version_history
[ ] DC elements in feed: <dc:language> and <dc:issued> present in each entry
[ ] Cache-Control headers present: max-age=3600 on /opds/v2/entries
```

---

## Part 2: Candidate 3 — README Accuracy Pass and New-Contributor Quickstart

### 2.1 What This Delivers

The backend `README.md` was last meaningfully updated at Phase 2 completion. The current README misrepresents the project state in ways that directly harm first impressions for contributors, institutional evaluators, and security reviewers:

- Reports "Phase 2 Complete" when the actual state is Phase 4 Complete
- Shows 35 passing tests when the actual count is 255
- Omits `app/api/v1/`, `app/services/`, `app/http_signatures.py`, and the entire export layer from the project structure diagram
- Describes Phase 3 (contributions) as the "Next Phases" goal
- Has a development server command binding to `0.0.0.0` — a direct violation of the project security rule requiring `127.0.0.1`
- `API.md` is stamped "MVP Phase 1" and documents none of the federation or export endpoints

**Candidate 3 is fully independent of Candidates 1 and 2.** It can be developed on a separate branch, merged to main at any time, and requires zero risk to the running application. It is purely documentation.

**User-facing outcome**: A developer who discovers the open-repo GitHub repository sees accurate documentation, a correct setup guide, a working dev server command that does not violate security rules, and a federation/export endpoint reference.

### 2.2 Exact Changes Required: `README.md`

**Current state vs. required state (file-by-file analysis)**:

#### Change 3a: Status line and version

Current (line 3):
```markdown
**Status**: Phase 2 Complete - FastAPI + PostgreSQL + ...
```

Required:
```markdown
**Status**: Phase 4 Complete — Federation Stack Live | Phase 5 In Development (Offline Export / Kiwix)

**Version**: 0.4.0  
**Tests**: 255 passing, 0 failures (federation, endorsements, contributions, CRUD)
```

#### Change 3b: "What's Implemented" — endpoint list

The current endpoint list covers Phase 1 and Phase 2 only. The Phase 3 contribution workflow, Phase 4 federation partner API, and admin routes are missing. Required additions:

```markdown
**Phase 3 - Contributions**:
- `POST /api/contributions` — Submit a proposed content change
- `GET /api/contributions` — List contributions with status filter
- `GET /api/contributions/{contribution_id}` — Single contribution detail
- `POST /api/review/{contribution_id}/approve` — Approve a contribution
- `POST /api/review/{contribution_id}/reject` — Reject with reason

**Phase 4 - Federation**:
- `POST /api/federation/partners` — Register a federated node
- `GET /api/federation/partners` — List registered partners
- `POST /api/inbox` — ActivityPub inbox (receives Announce activities from peers)
- `POST /api/outbox` — ActivityPub outbox (sends activities to peers)
- `GET /admin/federation/partners` — Admin: view all partner registrations
- `GET /admin/federation/conflicts` — Admin: view conflict log
```

#### Change 3c: Project structure diagram

Current diagram omits most of the actual codebase. Required replacement:

```markdown
## Project Structure

```
backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── admin/              # Admin dashboard routes
│   ├── services/
│   │   ├── export/
│   │   │   ├── zim_writer.py       # ZIM archive generation (Phase 5)
│   │   │   └── opds_generator.py   # OPDS catalog (Phase 5)
│   │   ├── contribution_service.py
│   │   ├── endorsement_service.py
│   │   ├── endorsement_propagation_service.py
│   │   ├── federation_conflict_service.py
│   │   └── search_service.py
│   ├── database.py
│   ├── http_signatures.py          # RFC 9421 HTTP signature verification
│   ├── main.py
│   ├── models.py                   # SQLAlchemy ORM models
│   ├── routes.py                   # Main API routes
│   └── schemas.py                  # Pydantic schemas
├── alembic/                        # Database migrations
├── tests/
│   ├── integration/                # Integration tests (export pipeline)
│   ├── conftest.py
│   ├── test_activitypub.py
│   ├── test_contributions.py
│   ├── test_federation_partner.py
│   ├── test_phase_3_endpoints.py
│   ├── test_routes.py
│   ├── test_wave3_endorsement_propagation.py
│   └── test_wave4_phase4_conflict_logging.py
├── API.md                          # Endpoint documentation
├── pyproject.toml
└── README.md
```
```

#### Change 3d: Development server command — CRITICAL SECURITY FIX

Current (line 93):
```bash
uvicorn app.main:create_app --reload --host 0.0.0.0 --port 8000
```

This binds the development server to all network interfaces. This is a live security rule violation (`0.0.0.0` is prohibited on all projects per CLAUDE.md). Required replacement:

```bash
# Start the server (binds to localhost only)
uv run uvicorn app.main:create_app --reload --host 127.0.0.1 --port 8000
```

This is the only security-critical change in Candidate 3. It must be included regardless of whether any other documentation change is made.

#### Change 3e: Test suite section

Current test count (line 40) is wrong. Required update:

```markdown
### Tests

**255 passing tests** covering:
- Required field validation, type validation (CRUD)
- Multilingual content support
- CID computation and format verification
- Endorsement type validation, statistics, service CRUD
- Search response schemas and filtering
- ActivityPub inbox/outbox message handling
- Federation partner registration and HTTP signature verification
- Conflict detection and logging (Wave 4)
- Contribution submission, review workflow, status tracking
- Export pipeline integration (ZimWriter and OPDS stubs, Phase 5 preparation)
```

#### Change 3f: "Next Phases" section

Current text describes Phase 3 as next. Required replacement:

```markdown
## Next Phases

### Phase 5 — Offline Export (In Development)
- ZIM archive generation via python-libzim (Kiwix-compatible offline archives)
- OPDS 1.2 catalog for in-app discovery (Kiwix Android, Desktop, kiwix-serve)
- Cloudflare R2 CDN distribution (zero-egress-cost hosting)
- Weekly automated exports via APScheduler
- SHA-256 sidecar files for download integrity verification

### Phase 6 — Distribution Expansion
- IPFS/CAR file generation for censorship-resistant distribution
- BitTorrent seeding for community distribution
- Multi-language ZIM exports
- Incremental/differential export optimization
- Distributed sync (peer-to-peer node synchronization, Wave 5.2)
```

#### Change 3g: Add contributor quickstart section (new section)

The README currently has no path for contributors to make their first contribution. Required addition:

```markdown
## Contributing: First-Time Setup

### Prerequisites
- Python 3.11+
- PostgreSQL 16
- uv (Python package manager): `pip install uv`

### Setup Steps

```bash
# Clone and navigate to backend
git clone https://github.com/esca8peArtist/open-repo.git
cd open-repo/projects/open-repo/backend

# Install development dependencies
uv pip install -e ".[dev]"

# Copy environment template
cp .env.example .env
# Edit .env: set DATABASE_URL to your local PostgreSQL

# Apply database migrations
alembic upgrade head

# Run tests to verify your setup
uv run pytest tests/ -v
# Expected: 255 tests pass, 0 fail

# Start development server (localhost only)
uv run uvicorn app.main:create_app --reload --host 127.0.0.1 --port 8000
# API docs available at http://localhost:8000/docs
```

### Development Conventions

- **Branch naming**: `feature/description`, `fix/issue-number`, `docs/topic`
- **Commit format**: Conventional commits (`feat:`, `fix:`, `docs:`, `test:`, `chore:`)
- **Test coverage**: New features must include tests; run `uv run pytest tests/ --cov=app` to check
- **Linting**: `uv run ruff check app/` must pass before committing
- **Formatting**: `uv run ruff format app/` before commits
- **Never bind to `0.0.0.0`**: All services must bind to `127.0.0.1` or a specific interface

### Running Specific Test Groups

```bash
# Federation tests only
uv run pytest tests/test_federation_partner.py tests/test_activitypub.py -v

# Export pipeline integration tests
uv run pytest tests/integration/ -v -m integration

# Contribution workflow tests
uv run pytest tests/test_contributions.py tests/test_phase_3_endpoints.py -v

# With coverage report
uv run pytest tests/ --cov=app --cov-report=html
```
```

### 2.3 Exact Changes Required: `API.md`

`API.md` is stamped "MVP Phase 1" and documents only CRUD endpoints. Required changes:

#### Change 3h: Update version and status header

Current:
```markdown
**Version**: 0.1.0 (MVP Phase 1)
```

Required:
```markdown
**Version**: 0.4.0 (Phase 4 Complete — Federation + Contributions + Endorsements)
```

#### Change 3i: Add Phase 3 and Phase 4 endpoint sections

After the existing CRUD and endorsement sections, add:

```markdown
### Contributions (Phase 3)

#### `POST /api/contributions`

Submit a proposed change to an existing content item.

**Request body**:
```json
{
  "item_cid": "sha256-abc123",
  "proposed_changes": { ... },
  "contributor_id": "did:key:z6Mk..."
}
```

**Response**: `201 Created` with `contribution_id`.

---

#### `POST /api/review/{contribution_id}/approve`

Approve a contribution and apply changes to the content item.

**Response**: `200 OK` with updated item.

---

### Federation (Phase 4)

#### `POST /api/federation/partners`

Register a new federated node. Requires HTTP signature verification.

**Request body**:
```json
{
  "node_url": "https://partner.example.org",
  "node_name": "Partner Node A",
  "public_key_pem": "-----BEGIN PUBLIC KEY-----..."
}
```

**Response**: `201 Created` with partner registration record.

---

#### `POST /api/inbox`

ActivityPub inbox. Receives signed `Announce` activities from federated partners.
All inbound requests must carry a valid HTTP signature (RFC 9421).

**Content-Type**: `application/activity+json`

---

#### Admin Endpoints

All admin endpoints require admin authentication.

`GET /admin/federation/partners` — List all registered partners and their sync status  
`GET /admin/federation/conflicts` — List detected sync conflicts requiring resolution  
`POST /admin/federation/conflicts/{id}/resolve` — Mark a conflict as resolved
```

### 2.4 File-Level Change Summary

| File | Change | Risk | Effort |
|------|--------|------|--------|
| `backend/README.md` | Status line, test count, project structure, dev server host, test description, Next Phases, contributor quickstart | Zero (documentation only) | 1-1.5 hrs |
| `backend/API.md` | Version header, Phase 3 contribution endpoints, Phase 4 federation endpoints | Zero (documentation only) | 1 hr |

**Total files changed**: 2. **New files created**: 0. **Code changes**: 0.

### 2.5 Security Impact of the 0.0.0.0 Fix

The development server command in the README currently reads:

```
uvicorn app.main:create_app --reload --host 0.0.0.0 --port 8000
```

A developer following this quickstart would bind the FastAPI server to all network interfaces on their machine, exposing the development server (with no authentication and no rate limiting) to any device on their local network. This is a violation of the project security rule and a concrete risk for developers who run the server in shared network environments (offices, coffee shops, university networks).

The fix is one word: replace `0.0.0.0` with `127.0.0.1`. This single character-level change is the highest-priority item in Candidate 3 and should be made even if no other documentation change is made.

### 2.6 Test Coverage Requirements

Candidate 3 is a documentation-only change. No new tests are required. The 255 existing tests continue to pass without modification.

**Verification after merge**:
```bash
# Confirm test count matches what README claims
uv run pytest tests/ -v --tb=no -q | tail -3
# Expected output: 255 passed
```

### 2.7 Integration Sequence for Candidate 3

Because Candidate 3 has zero dependencies, it can be executed in any order relative to Candidates 1 and 2.

**Recommended execution**: Merge Candidate 3 first (before Candidate 1), since it fixes a live security issue (`0.0.0.0`) and requires no review of code logic. This is the lowest-friction item in Phase 5.

```
Step 1: Create feature branch
  git checkout -b docs/readme-phase4-accuracy

Step 2: Apply all README changes
  Edit backend/README.md (Changes 3a through 3g above)
  Critical: Change host 0.0.0.0 → 127.0.0.1 (Change 3d)

Step 3: Apply API.md changes
  Edit backend/API.md (Changes 3h and 3i above)

Step 4: Verify test count matches documentation
  uv run pytest tests/ -q
  Count: must be 255 passed

Step 5: Verify project structure in README matches actual filesystem
  ls -R backend/app/ (compare to new diagram in Change 3c)

Step 6: Verify dev server command
  Test: uv run uvicorn app.main:create_app --reload --host 127.0.0.1 --port 8000
  Should start without error and bind to localhost only

Step 7: PR creation
  Title: "docs(phase-4): update README accuracy, fix 0.0.0.0 security issue, add contributor quickstart"
  Can merge to main at any time — no dependency on Candidates 1 or 2
  Fast review expected: pure documentation, zero code changes
```

### 2.8 Risk Assessment

**Risk 1: README accuracy drifts again after merge**
- Probability: Medium (test counts and endpoint lists change with each phase)
- Impact: Low (cosmetic; does not affect functionality)
- Mitigation: Add a note in CONTRIBUTING.md that README test counts must be updated when tests are added. No automated enforcement is necessary at this scale.

**Risk 2: Project structure diagram goes stale**
- Probability: Low (structure is stable for Phase 5 execution period)
- Impact: Low (outdated diagram is less harmful than outdated security guidance)
- Mitigation: Document that the structure diagram should be updated when new modules are added in Phase 5.

**Risk 3: Contributor quickstart setup steps are inaccurate**
- Probability: Low (setup steps reflect the actual `pyproject.toml` and migration structure)
- Impact: Medium (new contributors cannot set up the project)
- Mitigation: Manually test the quickstart steps before submitting the PR. This takes approximately 20 minutes on a clean environment.

---

## Part 3: Integration Sequence — How Candidates 1, 2, and 3 Stack

### 3.1 Dependency Graph

```
              ┌──────────────────────────────┐
              │  Candidate 1: ZimWriter      │
              │  feature/zimwriter-libzim    │
              │  8-11 hours                  │
              │                              │
              │  Deliverable: real .zim      │
              │  files in zim_exports table  │
              └──────────────┬───────────────┘
                             │  merge to main (Candidate 1 gate complete)
                             │
              ┌──────────────┼───────────────┐
              │              │               │
              ▼              ▼               ▼
  ┌───────────────┐  ┌──────────────┐  ┌──────────────────┐
  │ Candidate 2   │  │ Candidate 3  │  │ Future (Phase 6) │
  │ OPDS feedgen  │  │ README pass  │  │ IPFS, BitTorrent │
  │ 8-11 hours    │  │ 2-3 hours    │  │ scheduled cron   │
  │               │  │              │  │                  │
  │ DEPENDS ON    │  │ INDEPENDENT  │  │ DEPENDS ON 1+2   │
  │ Candidate 1   │  │ (can merge   │  │                  │
  │ having valid  │  │  any time)   │  │                  │
  │ ZIM exports   │  │              │  │                  │
  └───────────────┘  └──────────────┘  └──────────────────┘
```

### 3.2 Deployment Order (Recommended)

**Phase 5a (Before Candidate 1, any time)**:

Merge Candidate 3 (README pass). Zero risk, zero dependencies, fixes live security issue. Can be done before any Candidate 1 work begins.

**Phase 5b (After Candidate 1 merges)**:

Merge Candidate 2 (OPDS). Development can run in parallel with Candidate 1 on a separate branch. The merge must wait for Candidate 1 to be stable and producing real ZIM exports.

**What "Candidate 1 stable" means** before Candidate 2 can merge:
- `zim_exports` Alembic migration has run cleanly (`alembic upgrade head`)
- At least one row in `zim_exports` with `status='available'` and `cdn_url` populated
- `OPDSEntry.from_zim_export()` tested against a real (not mocked) ZimExport ORM row

### 3.3 Parallelism: What Can Run Simultaneously

| Work stream | Can start | Can merge |
|-------------|----------|----------|
| Candidate 3 (README) | Immediately, no blocker | Before any other candidate |
| Candidate 1 (ZimWriter) | Immediately, on feature branch | After Phase 4 PR confirmed stable |
| Candidate 2 (OPDS) dev | When Candidate 1 is ~50% done | Only after Candidate 1 merge AND real ZIM exports exist |

**Maximum-parallelism scenario** (for a two-person team or two-branch workflow):

```
Week 1 (June 1-5):
  Branch A: Candidate 3 (docs) — merge on June 1 or 2
  Branch B: Candidate 1 (ZimWriter) — implement and test

Week 2 (June 6-12):
  Branch A: Candidate 2 (OPDS) — development starts June 6
             while Candidate 1 is finalizing tests
  Branch B: Candidate 1 — manual Kiwix test, PR review, merge ~June 7

Week 2 (June 10-12):
  Branch A: Candidate 2 — rebase on Candidate 1 merge
            test with real ZIM exports, PR review, merge ~June 12
```

**Total elapsed time (parallel)**: ~12 days  
**Total elapsed time (sequential)**: ~16 days  
**Effort saved by parallelism**: ~4 days

### 3.4 Phase 6 Readiness: What Each Candidate Enables

| Phase 6 work | Requires Candidate 1 | Requires Candidate 2 | Requires Candidate 3 |
|-------------|---------------------|---------------------|---------------------|
| IPFS/CAR file generation | Yes | No | No |
| BitTorrent seeding | Yes | No | No |
| APScheduler weekly cron | Yes | No | No |
| Library/institutional partnerships | Yes | Yes (OPDS) | No |
| Kiwix Library project indexing | Yes | Yes (OPDS) | No |
| Multi-language ZIM | Yes | No | No |
| Incremental/differential exports | Yes | No | No |
| Contributor onboarding (real contributors) | No | No | Yes (quickstart) |

---

## Part 4: Shared Go-Live Checklist

### 4.1 Pre-Deployment Requirements (All Candidates)

These must be complete before any Candidate 2 or 3 merge:

```
[ ] Phase 4 PR (federation stack, 255 tests) confirmed stable on main
[ ] alembic upgrade head runs cleanly on a fresh database
[ ] Cloudflare R2 bucket configured with public read access
[ ] Environment variables set: R2_ACCOUNT_ID, R2_ACCESS_KEY_ID,
    R2_SECRET_ACCESS_KEY, R2_BUCKET_NAME, NODE_UUID, NODE_URL
[ ] zimcheck installed: apt-get install zim-tools (or brew install zim-tools)
[ ] Kiwix Android (F-Droid) installed on test device
[ ] Kiwix Desktop installed on test machine
[ ] Docker available for kiwix-serve integration test
```

### 4.2 Candidate 1 Go-Live Gate (prerequisite for Candidate 2)

```
[ ] uv run pytest tests/ -k "zim" -v — 84 + 8 new = 92 tests pass
[ ] zimcheck exits 0 on a real 50-article export
[ ] ZIM file first 4 bytes are ZIM magic header (not "STUB")
[ ] Xapian search: known keyword returns >= 1 result
[ ] ZIM opens in Kiwix Android (F-Droid): articles display correctly
[ ] ZIM opens in Kiwix Desktop: full-text search functional
[ ] ZIM opens in kiwix-serve: GET localhost:8080/A/agriculture returns article HTML
[ ] SHA-256 sidecar valid: sha256sum -c *.sha256 passes
[ ] zim_exports DB row with status='available' and cdn_url set
[ ] CDN URL publicly accessible: curl -I https://exports.example.org/zim/...zim -> 200
[ ] Export generation time < 60 seconds for nopic variant
[ ] _stub_write_placeholder() removed from zim_writer.py
```

### 4.3 Candidate 2 Go-Live Gate

```
[ ] Candidate 1 gate complete (all items above)
[ ] OPDSEntry.from_zim_export() tested with real ZimExport DB row
[ ] uv run pytest tests/unit/test_opds_generator.py -v — 23 tests pass
[ ] GET /opds/v2/root.xml -> 200, Content-Type: application/atom+xml
[ ] GET /opds/v2/entries -> 200, >= 1 <entry> with acquisition link present
[ ] OPDSGenerator.validate_opds_xml(feed_bytes) -> empty list
[ ] xmllint --noout <(curl http://localhost:8000/opds/v2/entries) -> 0 exit code
[ ] Kiwix Android: OPDS URL shows archive with Install button, tap installs ZIM
[ ] Kiwix Desktop: OPDS URL shows archive list
[ ] GET /opds/v2/searchdescription.xml -> well-formed XML, <Url> element present
[ ] OPDS catalog regenerates after new ZimWriter export (check last_regenerated_at)
[ ] Version history: 2+ exports for same flavour -> version_history has entries
[ ] DC elements: <dc:language> and <dc:issued> in each acquisition feed entry
```

### 4.4 Candidate 3 Go-Live Gate

```
[ ] README status line reads "Phase 4 Complete"
[ ] README test count reads "255 passing"
[ ] README dev server command uses --host 127.0.0.1 (NOT 0.0.0.0)
[ ] README project structure diagram matches: ls -R backend/app/ output
[ ] README Next Phases section describes Phase 5 (offline export / Kiwix)
[ ] README contributor quickstart: manually tested on clean environment
[ ] API.md version header reads "0.4.0 (Phase 4 Complete)"
[ ] API.md includes federation endpoints (POST /api/federation/partners, POST /api/inbox)
[ ] API.md includes contribution endpoints (POST /api/contributions, review routes)
[ ] uv run pytest tests/ -q confirms 255 passing (matches what README claims)
```

### 4.5 Rollback Procedures

**Candidate 2 rollback**:

The feedgen rewrite is a code quality change with a built-in fallback. Rollback options in order of preference:

1. **Immediate soft rollback**: Set `_FEEDGEN_AVAILABLE = False` at the top of `opds_generator.py`. This switches both generate methods to the xml.etree fallback path without reverting any ORM changes. OPDS endpoints remain up; feed generation uses the proven xml.etree path.

2. **Full git revert**: `git revert <candidate-2-merge-hash>`. This reverts `OPDSEntry.from_zim_export()` as well, so the catalog will not auto-populate from ZimExport rows — but the OPDS endpoints still serve whatever is cached or previously generated.

3. **Schema safety**: Neither rollback removes `zim_exports` rows or changes the database schema. Candidate 1's migration is unaffected by rolling back Candidate 2.

**Candidate 3 rollback**:

Documentation changes. Full git revert restores the old README and API.md. The security fix (`0.0.0.0 -> 127.0.0.1`) is the only change worth retaining if everything else is reverted.

---

## Part 5: Post-Launch Monitoring

### 5.1 Health Check Endpoint (Target State Post-Candidate-2)

After both Candidates 1 and 2 merge, `GET /api/exports/health` should return:

```json
{
  "phase_5_status": {
    "zimwriter": {
      "last_successful_export_at": "2026-06-01T02:03:14Z",
      "current_exports": [
        {
          "name": "open-repo_en_nopic",
          "period": "2026-06",
          "status": "available",
          "article_count": 512,
          "file_size_mb": 24.1,
          "zimcheck_passed": true,
          "cdn_url": "https://exports.example.org/zim/open-repo_en_nopic_2026-06.zim"
        }
      ],
      "failed_exports_7d": 0,
      "avg_generation_seconds_7d": 38.7
    },
    "opds": {
      "catalog_url": "https://node.example.org/opds/v2/root.xml",
      "entry_count": 4,
      "last_regenerated_at": "2026-06-01T02:04:22Z",
      "validation_errors": []
    }
  }
}
```

### 5.2 Alert Conditions

| Condition | Threshold | Response |
|-----------|-----------|----------|
| `zim_exports` row stuck in `status='generating'` | > 90 minutes | Export job may be hung; check APScheduler logs |
| `zim_exports.zimcheck_passed = FALSE` on any automated export | Any failure | Stop CDN upload; investigate zimcheck output |
| `GET /opds/v2/root.xml` returns non-200 | Any failure | OPDS router down; check FastAPI logs |
| CDN URL returns 404 for `status='available'` export | Any | Silent upload failure; re-trigger CDN upload |
| `validate_opds_xml()` returns non-empty list | Any | Feed is malformed; Kiwix may silently reject |
| `generate_acquisition_feed()` response time | > 500ms | Query optimization needed or cache issue |

### 5.3 Weekly Sanity Checks (10 minutes)

1. Download the latest ZIM from the CDN URL; open in Kiwix; search for a known keyword
2. Open Kiwix Android; add OPDS URL; confirm library shows current month's archives with correct file size
3. Check `zim_exports` table: `SELECT * FROM zim_exports WHERE status='generating' AND started_at < NOW() - INTERVAL '90 minutes';` — should return 0 rows
4. Check `zim_exports.zimcheck_passed`: `SELECT * FROM zim_exports WHERE zimcheck_passed = FALSE;` — should return 0 rows for recent exports

---

## Appendix: Effort Estimate Reconciliation

The task brief references "Candidate 2 OPDS feedgen (3-4h)" and "Candidate 3 Zed indexing (2-3h)". The actual effort figures from the detailed technical assessments are:

| Candidate | Task brief estimate | Technical assessment estimate | Discrepancy |
|-----------|--------------------|-----------------------------|-------------|
| Candidate 2 (OPDS) | 3-4 hours | 8-11 hours | Task brief underestimates by ~2x |
| Candidate 3 (README) | 2-3 hours (labeled "Zed indexing") | 2-3 hours | Estimate is accurate; label was wrong |

**On the "Zed indexing" label**: There is no candidate in the open-repo Phase 5 scope involving Zed (the text editor) or a separate indexing optimization. The three Phase 5 candidates are ZimWriter (Candidate 1), OPDS feedgen (Candidate 2), and README accuracy pass (Candidate 3), as documented in `PHASE_5_CANDIDATES.md`. The Candidate 3 scope above reflects the actual project documentation.

**On the OPDS effort discrepancy**: The 3-4h estimate in the task brief appears to assume only the feedgen rewrite without accounting for the OPDS router implementation, new test coverage, and kiwix-serve integration verification. The 8-11h estimate from the technical assessment is the production-accurate figure. Both Candidate 1 and Candidate 2 at 8-11h each fit within a June 1-12 execution window.

---

## Sources

- [OPDS 1.2 Specification](https://specs.opds.io/opds-1.2.html)
- [feedgen PyPI](https://pypi.org/project/feedgen/)
- [feedgen GitHub](https://github.com/lkiesow/python-feedgen)
- [Kiwix OPDS documentation](https://wiki.kiwix.org/wiki/OPDS)
- [Atom Syndication Format RFC 4287](https://tools.ietf.org/html/rfc4287)
- [OpenSearch 1.1 Specification](http://a9.com/-/spec/opensearch/1.1/)
- [Dublin Core Terms namespace](http://purl.org/dc/terms/)
- [openZIM ZIM format specification](https://wiki.openzim.org/wiki/ZIM_file_format)
- [python-libzim PyPI](https://pypi.org/project/libzim/)
- [WCAG 2.1 Level AA (accessibility, referenced for Candidate 3 context)](https://www.w3.org/TR/WCAG21/)
- Internal: `PHASE_5_CANDIDATES.md` — canonical candidate definitions
- Internal: `PHASE_5_CANDIDATE_1_ZIMWRITER_IMPLEMENTATION_ROADMAP.md` — Candidate 1 reference
- Internal: `PHASE_5_CANDIDATE_2_OPDS_IMPLEMENTATION_ROADMAP.md` — Candidate 2 detail (superseded by this document's consolidation)
- Internal: `PHASE_5_IMPLEMENTATION_DECISION_TREE.md` — integration sequencing rationale
- Internal: `PHASE_5_DECISION_FRAMEWORK.md` — candidate ranking and tradeoffs
