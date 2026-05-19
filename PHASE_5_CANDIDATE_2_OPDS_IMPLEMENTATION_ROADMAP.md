---
title: "Phase 5 Candidate 2 — OPDS Feed Generator: Detailed Implementation Roadmap"
project: open-repo
phase: 5
candidate: 2
status: ready-for-implementation-after-candidate-1
date: 2026-05-19
effort_estimate: "8-11 hours"
pr_dependency: "Candidate 1 (ZimWriter) merged and producing valid ZIM exports"
---

# Phase 5 Candidate 2: OPDS Feed Generator
## Detailed Implementation Roadmap

**Status**: Conditional — development can begin in parallel with Candidate 1, but must not merge before Candidate 1 produces valid ZIM exports  
**Effort**: 8-11 hours  
**Dependency**: `OPDSEntry.from_zim_export()` requires real `ZimExport` ORM rows (only exist after Candidate 1 produces valid ZIM output)  
**Unblocks**: Kiwix in-app catalog discovery, library/institutional distribution partnerships

---

## Architecture: OPDS 1.2 Catalog Structure

```
              KIWIX APP / OPDS CLIENT
              (Android F-Droid, Desktop, kiwix-serve)
                          │
                          │  GET /opds/v2/root.xml
                          ▼
              ┌──────────────────────────────────┐
              │  OPDS Root Navigation Catalog    │
              │  /opds/v2/root.xml               │
              │                                  │
              │  <feed kind=navigation>          │
              │    <link rel=search .../>        │
              │    <entry>                       │
              │      <link rel=subsection        │
              │            href=.../entries/>    │
              │    </entry>                      │
              │  </feed>                         │
              └─────────────┬────────────────────┘
                            │  GET /opds/v2/entries
                            ▼
              ┌──────────────────────────────────┐
              │  OPDS Acquisition Feed           │
              │  /opds/v2/entries                │
              │                                  │
              │  <feed kind=acquisition>         │
              │    <totalResults>N</totalResults>│
              │    <entry> per ZIM export:       │
              │      <id>urn:uuid:...</id>       │
              │      <title>Full Library</title> │
              │      <dc:language>eng</dc:lang.> │
              │      <dc:issued>2026-05</dc:iss> │
              │      <link rel=acquisition       │
              │            type=application/x-   │
              │            zim href=CDN_URL      │
              │            length=BYTES/>        │
              │      <link rel=related           │
              │            href=CDN_URL.sha256/> │
              │      <!-- version history -->    │
              │    </entry>                      │
              │  </feed>                         │
              └─────────────┬────────────────────┘
                            │  one-click install
                            ▼
              ┌──────────────────────────────────┐
              │  Cloudflare R2 CDN               │
              │  open-repo_en_nopic_2026-05.zim  │
              │  open-repo_en_nopic_2026-05      │
              │    .zim.sha256                   │
              └──────────────────────────────────┘
```

### Feed Generation Flow (post-integration)

```
                    zim_exports TABLE
                    (populated by ZimWriter, Candidate 1)
                          │
                          │  SELECT WHERE is_current=True
                          ▼
                    ┌──────────────────────────────┐
                    │  ExportJob trigger            │
                    │  (after each successful       │
                    │  ZimWriter.create_zim() call) │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │  OPDSEntry.from_zim_export()  │
                    │  (new factory method)         │
                    │                               │
                    │  Maps ZimExport ORM row →     │
                    │  OPDSEntry dataclass          │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │  OPDSGenerator with feedgen   │
                    │  (replaces xml.etree)         │
                    │                               │
                    │  fg = FeedGenerator()         │
                    │  fg.id(...), fg.title(...)    │
                    │  fg.link(rel="self", ...)     │
                    │  for entry: fg.add_entry()    │
                    │  return fg.atom_str()         │
                    └──────────────┬───────────────┘
                                   │
                                   ├─── /opds/v2/root.xml (navigation)
                                   ├─── /opds/v2/entries (acquisition)
                                   ├─── /opds/v2/entry/{uuid} (single)
                                   └─── /opds/v2/searchdescription.xml
```

---

## Exact Code Entry Points and Files to Modify

### File 1: `pyproject.toml`
**Change**: Add one line under `[project.dependencies]`

```toml
# ADD under [project.dependencies]:
"feedgen>=0.9",
```

**Dependency health note**: feedgen (lkiesow/python-feedgen) has approximately 35,000 weekly downloads as of 2026 but shows an inactive release cadence. The fallback is always available: if feedgen causes issues, revert to the existing `xml.etree` implementation which is already proven to work. The feedgen rewrite is a code quality improvement, not a correctness fix — both approaches produce valid Atom XML.

**Alternative**: If feedgen proves unstable, use `lxml.etree` instead (which supports namespace-aware XML generation more robustly than `xml.etree`). The architecture is identical; only the XML building library changes.

---

### File 2: `app/services/export/opds_generator.py` — Four Changes

#### Change 1: Add feedgen import (with fallback guard)

**Location**: After existing imports (after line 41 `from xml.etree import ElementTree as ET`)

```python
# feedgen for cleaner Atom/OPDS generation
# Fallback to xml.etree if feedgen is not installed
try:
    from feedgen.feed import FeedGenerator
    from feedgen.entry import FeedEntry
    _FEEDGEN_AVAILABLE = True
except ImportError:
    _FEEDGEN_AVAILABLE = False
    FeedGenerator = None  # type: ignore[assignment,misc]
    FeedEntry = None      # type: ignore[assignment,misc]
```

#### Change 2: Implement `OPDSEntry.from_zim_export()` classmethod

**Location**: Add to `OPDSEntry` class, after the existing `from_dict()` classmethod (line ~174)

This is the critical method that connects Candidate 1 to Candidate 2:

```python
    @classmethod
    def from_zim_export(cls, export: "ZimExport") -> "OPDSEntry":
        """
        Construct an OPDSEntry from a ZimExport ORM row.

        This is the primary construction path for auto-generated OPDS entries.
        Called by OPDSCatalogService after each successful ZimWriter.create_zim() run.

        Args:
            export: ZimExport SQLAlchemy model instance (from zim_exports table).
                    Must have status='available' and a non-None cdn_url.

        Returns:
            OPDSEntry ready to be added to OPDSGenerator.

        Raises:
            ValueError: If export.cdn_url is None (upload must complete before
                        adding to catalog).
            ValueError: If export.zim_uuid is not a valid UUID format.
        """
        if not export.cdn_url:
            raise ValueError(
                f"ZimExport {export.id} (name={export.name}) has no cdn_url. "
                f"Upload to CDN must complete before adding to OPDS catalog."
            )
        if not export.sha256:
            raise ValueError(
                f"ZimExport {export.id} has no sha256 checksum. "
                f"ZIM must be validated before adding to catalog."
            )

        # Build version history from sibling exports (same name+flavour, not current)
        # The caller is responsible for pre-loading version history if needed.
        # Default: empty version history (populated by OPDSCatalogService).
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
            version_history=[],  # populated by OPDSCatalogService
        )
```

#### Change 3: Rewrite `generate_root_catalog()` and `generate_acquisition_feed()` using feedgen

**Location**: Replace the two generate methods in `OPDSGenerator`

The current implementations use `xml.etree` internally (via `_build_root_catalog_element()` and `_build_acquisition_feed_element()`). Replace with feedgen-based equivalents:

```python
    def generate_root_catalog(self) -> bytes:
        """
        Generate the OPDS root navigation catalog using feedgen.
        Falls back to xml.etree if feedgen is not installed.
        """
        if _FEEDGEN_AVAILABLE:
            return self._generate_root_catalog_feedgen()
        return self._generate_root_catalog_etree()  # existing fallback

    def _generate_root_catalog_feedgen(self) -> bytes:
        """feedgen-based root catalog generation."""
        entries_url = self.catalog_url.replace("root.xml", "entries")
        search_url = self.catalog_url.replace("root.xml", "searchdescription.xml")

        fg = FeedGenerator()
        fg.id(f"urn:uuid:{self.node_uuid}")
        fg.title(f"{self.node_name} Offline Library Catalog")
        fg.author({"name": self.node_name, "uri": self.node_url})
        fg.updated(self._generated_at)

        # OPDS profile link relations — must set raw XML for OPDS-specific types
        fg.link(href=self.catalog_url, rel="self",
                type=MIME_OPDS_NAV)
        fg.link(href=self.catalog_url, rel="start",
                type=MIME_OPDS_NAV)
        fg.link(href=search_url, rel="search",
                type=MIME_OPENSEARCH)

        # Navigation entry: subsection link to acquisition feed
        fe = fg.add_entry()
        fe.id(f"urn:uuid:{self.node_uuid}:all")
        fe.title("All Offline Exports")
        fe.updated(self._generated_at)
        fe.summary(f"{len(self._entries)} offline ZIM file(s) available for download")
        fe.link(href=entries_url, rel="subsection", type=MIME_OPDS_ACQ)

        return fg.atom_str(pretty=True)

    def generate_acquisition_feed(self) -> bytes:
        """
        Generate the OPDS acquisition feed using feedgen.
        Falls back to xml.etree if feedgen is not installed.
        """
        if _FEEDGEN_AVAILABLE:
            return self._generate_acquisition_feed_feedgen()
        return self._generate_acquisition_feed_etree()  # existing fallback

    def _generate_acquisition_feed_feedgen(self) -> bytes:
        """feedgen-based acquisition feed generation."""
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

    def _add_feedgen_entry(self, fg: "FeedGenerator", entry: "OPDSEntry") -> None:
        """Add an OPDSEntry to a feedgen FeedGenerator as a FeedEntry."""
        fe = fg.add_entry()
        fe.id(entry.entry_id)
        fe.title(entry.title)
        fe.updated(entry.generated_at)
        fe.summary(entry.description)

        # Dublin Core namespace elements — must be added as raw XML extensions
        # feedgen's extension mechanism handles this via nsmap registration
        # Pattern: fe.dc.dc_language(entry.language) if DC extension is loaded,
        # OR use a custom XML extension to append raw elements.
        # Practical approach: append DC elements via feedgen's load_extension or
        # directly extend the atom XML post-generation.
        # See "feedgen OPDS Namespace Handling" note below.

        # Acquisition link (primary download)
        fe.link(
            href=entry.download_url,
            rel="http://opds-spec.org/acquisition",
            type=MIME_ZIM,
            title=entry.filename,
        )
        # length attribute is not a standard feedgen link field — set via extra_attrs
        # This requires feedgen>=0.9 which supports extra link attributes.

        # SHA-256 sidecar
        fe.link(
            href=entry.download_url + ".sha256",
            rel="related",
            type="text/plain",
            title=f"SHA-256 checksum for {entry.filename}",
        )

        # Illustration
        if entry.illustration_url:
            fe.link(href=entry.illustration_url,
                    rel="http://opds-spec.org/image",
                    type="image/png")

        # Version history
        for prev in sorted(entry.version_history,
                           key=lambda v: v.period, reverse=True)[:self.max_version_history]:
            fe.link(
                href=prev.download_url,
                rel="related",
                type=MIME_ZIM,
                title=f"Previous version: {prev.period}",
            )
```

#### Change 4: Add missing OPDS 1.2 elements and DC namespace

**The OPDS namespace challenge with feedgen**: feedgen natively supports Atom RFC 4287 but does not have built-in OPDS or Dublin Core extensions. OPDS-specific link relations (`rel="http://opds-spec.org/acquisition"`) and Dublin Core elements (`dc:language`, `dc:issued`) must be added via feedgen's extension API or via post-processing of the generated XML.

**Recommended approach — post-processing with `lxml`**:

```python
    def _add_dc_elements_to_feed(self, xml_bytes: bytes,
                                  entries: list[OPDSEntry]) -> bytes:
        """
        Post-process feedgen output to add Dublin Core and OPDS namespace elements.

        feedgen generates valid Atom but lacks native OPDS/DC extension support.
        This method parses the Atom output and adds dc:language, dc:issued, and
        opensearch:totalResults elements per entry.

        Called by generate_acquisition_feed() after feedgen generates the base XML.
        """
        try:
            from lxml import etree
        except ImportError:
            # lxml not available — return xml_bytes unchanged (DC elements omitted)
            # This is acceptable for basic OPDS compatibility; Kiwix does not
            # require dc:language to discover and download ZIM files.
            return xml_bytes

        ATOM_NS = "http://www.w3.org/2005/Atom"
        DC_NS = "http://purl.org/dc/terms/"
        OPENSEARCH_NS = "http://a9.com/-/spec/opensearch/1.1/"

        root = etree.fromstring(xml_bytes)
        nsmap = root.nsmap
        nsmap["dc"] = DC_NS
        nsmap["opensearch"] = OPENSEARCH_NS

        # Add opensearch:totalResults to feed
        total_elem = etree.SubElement(root,
                                       f"{{{OPENSEARCH_NS}}}totalResults")
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

        return etree.tostring(root, xml_declaration=True,
                              encoding="utf-8", pretty_print=True)
```

**Alternative — xml.etree fallback remains the safety net**: The existing `_build_root_catalog_element()` and `_build_acquisition_feed_element()` methods remain in place as `_generate_root_catalog_etree()` and `_generate_acquisition_feed_etree()`. If the feedgen path has issues, disable `_FEEDGEN_AVAILABLE` to fall back immediately.

---

## Metadata Mapping: ZimExport ORM → OPDS Feed Fields

| `zim_exports` column | OPDS element | Required | Notes |
|---------------------|-------------|----------|-------|
| `zim_uuid` | `<id>urn:uuid:{uuid}</id>` | Yes | Stable across versions |
| `title` | `<title>{title}</title>` | Yes | Max 30 chars recommended |
| `description` | `<summary>{desc}</summary>` | Yes | Max 80 chars |
| `language` | `<dc:language>{lang}</dc:language>` | OPDS 1.2 recommended | ISO 639-3 |
| `period` | `<dc:issued>{period}</dc:issued>` | OPDS 1.2 recommended | YYYY-MM format |
| `cdn_url` | `<link rel="http://opds-spec.org/acquisition" href=.../>` | Yes | Must be publicly reachable |
| `file_size_bytes` | `<link ... length="{bytes}"/>` | OPDS recommended | In bytes (not human-readable) |
| `sha256` | `<link rel="related" href="{cdn_url}.sha256"/>` | No (open-repo standard) | Points to sidecar file |
| `article_count` | `<dc:extent>{count} articles</dc:extent>` | No | Informational |
| `completed_at` | `<updated>{datetime}</updated>` | Yes | ISO 8601 with Z suffix |
| `is_reference` | `<category term="archive" .../>` | No | Reference exports only |
| `flavour` | Not a direct element | N/A | Used for entry title construction |

### OPDS 1.2 Required vs Optional Field Compliance Matrix

| Element | Spec requirement | Implementation | Kiwix behavior if missing |
|---------|-----------------|----------------|--------------------------|
| `atom:id` | MUST | Always present (from `zim_uuid`) | Feed rejected |
| `atom:title` | MUST | Always present | Feed rejected |
| `atom:updated` | MUST | Always present | Feed rejected |
| Acquisition link | MUST (for ACQ feed) | Always present | Entry not downloadable |
| `atom:author` | SHOULD | Present at feed level | Silently ignored |
| `dc:language` | SHOULD | Present after DC post-processing | Silently ignored |
| `dc:issued` | SHOULD | Present after DC post-processing | Silently ignored |
| `opensearch:totalResults` | SHOULD | Present at feed level | Pagination may not work |
| Illustration link | SHOULD | Present when `illustration_url` set | Blank thumbnail in Kiwix |

---

## Pagination and Filtering for Large Catalogs

The current implementation loads all current exports into memory and serializes them in one pass. This is acceptable for the Phase 5 launch (expected: 5-20 ZIM variants). For larger catalogs (50+ variants), add OpenSearch-based pagination.

### Pagination Implementation (Phase 5.1, deferred)

When entry count grows past 20, add `start` and `count` query parameters:

```
GET /opds/v2/entries?start=0&count=10
GET /opds/v2/entries?start=10&count=10
```

In the feed, add `<opensearch:startIndex>`, `<opensearch:itemsPerPage>`, and `<link rel="next" .../>` / `<link rel="previous" .../>` navigation links.

For Phase 5 launch, pagination is not needed. The OpenSearch `totalResults` element is sufficient.

### Filtering (Domain Sub-Feeds)

Add domain-specific sub-feeds at `/opds/v2/entries/domain/{domain}`:

```
GET /opds/v2/entries/domain/agriculture
→ Returns only agriculture domain ZIM exports
```

This enables Kiwix users to browse by domain without seeing all variants. Implemented by adding a `domain` filter parameter to `OPDSGenerator.generate_acquisition_feed()`.

---

## Test Matrix

### 8 Test Scenarios

**Category: Feed Validity (unit)**

| # | Test ID | What it tests | Input | Expected result | Priority |
|---|---------|--------------|-------|----------------|----------|
| 1 | `test_opds_root_catalog_valid_atom` | Root catalog is well-formed Atom XML | OPDSGenerator with 3 entries | `OPDSGenerator.validate_opds_xml()` returns empty error list; root element is `<feed>` | P0 |
| 2 | `test_opds_acquisition_feed_has_required_elements` | Each entry has id, title, updated, and at least one acquisition link | 2 OPDSEntries | All `<entry>` elements have `<id>`, `<title>`, `<updated>`, and `<link rel="http://opds-spec.org/acquisition">` | P0 |
| 3 | `test_opds_acquisition_link_type_is_zim` | Acquisition link MIME type is `application/x-zim` | 1 OPDSEntry | `<link type="application/x-zim">` present in first entry | P0 |

**Category: Metadata Accuracy (unit)**

| # | Test ID | What it tests | Input | Expected result | Priority |
|---|---------|--------------|-------|----------------|----------|
| 4 | `test_opds_from_zim_export_factory` | `from_zim_export()` maps all fields correctly | Mocked ZimExport ORM row | `OPDSEntry.uuid == export.zim_uuid`, `download_url == export.cdn_url`, `file_size_bytes == export.file_size_bytes`, `sha256_checksum == export.sha256` | P0 |
| 5 | `test_opds_from_zim_export_raises_on_missing_cdn_url` | Factory rejects incomplete export | ZimExport with `cdn_url=None` | Raises `ValueError: ZimExport ... has no cdn_url` | P1 |
| 6 | `test_opds_dc_language_element_present` | DC namespace language element is in each entry | OPDSEntry with `language="eng"` | Feed XML contains `<dc:language>eng</dc:language>` in entry | P1 |

**Category: Client Compatibility (integration)**

| # | Test ID | What it tests | Input | Expected result | Priority |
|---|---------|--------------|-------|----------------|----------|
| 7 | `test_opds_feed_parseable_by_kiwix_catalog_parser` | Feed is accepted by Kiwix's built-in OPDS parser | Root catalog XML | `GET /opds/v2/root.xml` from a running kiwix-serve configured with this catalog returns 200 and lists the expected archives | P0 |
| 8 | `test_opds_search_description_valid` | OpenSearch description is well-formed XML | OPDSGenerator instance | `generate_search_description()` output parses as XML; contains `<Url type="...acquisition">` element | P1 |

### Test File Location

```
tests/
├── unit/
│   └── test_opds_generator.py   # Tests 1-6 (19 existing tests + 4 new = 23 total)
└── integration/
    └── test_opds_kiwix.py       # Test 7 (requires kiwix-serve Docker container)
```

The 19 existing OPDS tests already exercise the public interface. After the feedgen rewrite, most will pass without modification. The main adjustment will be in tests that do exact XML string comparisons — these should be updated to parse and check structure rather than compare raw XML strings, since feedgen may reorder attributes or whitespace.

### Running the Test Matrix

```bash
# All OPDS unit tests:
uv run pytest tests/unit/test_opds_generator.py -v

# Integration test (requires Docker):
docker run -d -p 8080:80 kiwix/kiwix-serve --library /path/to/library.xml
uv run pytest tests/integration/test_opds_kiwix.py -v

# Full export suite including OPDS:
uv run pytest tests/ -k "opds" -v
```

---

## Integration Sequence with Phase 4 Federation

### Step-by-Step Sequence (starts after Candidate 1 merge)

```
Step 0: Verify Candidate 1 has merged and zim_exports table has real rows
  Check: SELECT * FROM zim_exports WHERE status='available' LIMIT 1;
  Must return at least one row with cdn_url populated.

Step 1: Create feature branch
  git checkout -b feature/opds-feedgen-migration

Step 2: Add dependency
  Edit pyproject.toml — add "feedgen>=0.9" to [project.dependencies]
  uv pip install feedgen
  Verify import: python -c "from feedgen.feed import FeedGenerator; print('OK')"

Step 3: Add import guard to opds_generator.py
  Add feedgen import with _FEEDGEN_AVAILABLE fallback flag

Step 4: Implement OPDSEntry.from_zim_export()
  Add factory classmethod to OPDSEntry
  Write test: test_opds_from_zim_export_factory

Step 5: Run existing 19 OPDS tests
  uv run pytest tests/unit/test_opds_generator.py -v
  All 19 should pass (from_zim_export is new; existing tests use from_dict)

Step 6: Write feedgen-based generate methods
  Implement _generate_root_catalog_feedgen()
  Implement _generate_acquisition_feed_feedgen()
  Implement _add_dc_elements_to_feed() (lxml post-processing)

Step 7: Run all 23 OPDS tests
  uv run pytest tests/unit/test_opds_generator.py -v
  Fix any test failures from feedgen namespace differences

Step 8: Validate feed against Kiwix catalog parser
  Start kiwix-serve with test ZIM
  Point it to /opds/v2/root.xml from the FastAPI app
  Confirm Kiwix shows the archive in its library browser

Step 9: Verify OPDS search integration
  GET /opds/v2/searchdescription.xml
  Verify it's valid XML with Url template element

Step 10: Add FastAPI OPDS endpoint (if not already present)
  app/api/v1/opds.py with:
    GET /opds/v2/root.xml
    GET /opds/v2/entries
    GET /opds/v2/entry/{uuid}
    GET /opds/v2/searchdescription.xml
  All endpoints call OPDSGenerator and return bytes with Content-Type application/atom+xml

Step 11: Wire catalog regeneration to export job
  After ZimWriter.create_zim() succeeds and CDN upload completes,
  trigger OPDSCatalogService.regenerate() which rebuilds the catalog
  from all current zim_exports rows

Step 12: Update version history in catalog
  OPDSCatalogService.regenerate() also fetches previous-version rows
  (same name+flavour, status='superseded', within retention window)
  and populates OPDSEntry.version_history for each current export

Step 13: PR creation
  Title: "feat(phase-5): migrate OPDS generator to feedgen, add from_zim_export factory"
  Must not merge until Candidate 1 has produced valid ZIM exports and the
  zim_exports table has at least one real row with cdn_url populated
```

### Where Candidate 2 Connects to Phase 4

| Phase 4 artifact | How OPDS uses it |
|-----------------|-----------------|
| `FederationPartner` model | Node name/URL written to `<author>` in the catalog feed (identifies which node published these exports) |
| `content_items` table | Not directly used by OPDS; only used by ZimWriter. OPDS reads from `zim_exports`. |
| ActivityPub endpoints | Not used by OPDS in Phase 5. Future Wave 5.2 may use federation to distribute OPDS catalogs across nodes. |

---

## Risk Assessment

### Risk 1: feedgen OPDS acquisition link relations are non-standard
**Probability**: High — feedgen is an Atom/RSS library, not an OPDS library  
**Impact**: Medium — acquisition links may not be recognized by Kiwix's catalog parser  
**Technical detail**: OPDS acquisition links use `rel="http://opds-spec.org/acquisition"`, which is a full URI as the link relation. feedgen's `add_link()` accepts `rel` as a string, so this should work. The risk is in testing: feedgen may escape or truncate the URI.  
**Detection**: `test_opds_acquisition_link_type_is_zim` test fails, or Kiwix does not show an "Install" button for the archive  
**Mitigation**:
- Test `fe.link(href=..., rel="http://opds-spec.org/acquisition", type="application/x-zim")` before committing the full rewrite
- If feedgen cannot handle the full URI relation, use `xml.etree` for only the acquisition link while using feedgen for the feed structure
- The existing `xml.etree` fallback is always available

### Risk 2: Kiwix catalog parser silently rejects malformed OPDS
**Probability**: Medium — OPDS namespace handling is known to have silent failure modes  
**Impact**: High — users see nothing in Kiwix's library browser without any error message  
**Detection**: Manual test — point Kiwix Android (F-Droid) at the OPDS URL; library browser stays empty  
**Mitigation**:
- Compare generated XML byte-for-byte against the known-good OPDS example in `PHASE_5_ARCHITECTURE.md` Appendix C
- Test with `kiwix-serve`'s built-in OPDS parser before testing on mobile (kiwix-serve gives more debug output)
- Run `xmllint --noout` on the generated feed to catch namespace declaration issues
- Check that the `xmlns` and `xmlns:opds` namespace declarations are on the root `<feed>` element (not on individual child elements)

### Risk 3: feedgen inactive maintenance causes version incompatibility
**Probability**: Low-to-medium (no new PyPI release in 12+ months as of 2026)  
**Impact**: Low — current feedgen version works; the risk is future breakage  
**Detection**: `uv pip install feedgen` installs a version that breaks on newer Python  
**Mitigation**:
- Pin feedgen version: `feedgen>=0.9,<2.0` to prevent automatic upgrades to potentially incompatible future versions
- The xml.etree fallback requires no external dependencies and will always work
- If feedgen is abandoned, fork or replace with `lxml.etree` (functionally identical for this use case)

### Risk 4: `dc:language` and `dc:issued` namespace declaration conflicts
**Probability**: Medium — XML namespace handling in Python varies by library  
**Impact**: Low — Kiwix does not require DC elements; they improve catalog display but are not mandatory  
**Detection**: Feed XML has malformed or duplicate namespace declarations  
**Mitigation**:
- Use the `_add_dc_elements_to_feed()` post-processing approach which adds DC elements as a final step with correct namespace declarations
- Validate the final XML with `validate_opds_xml()` (already implemented in the class)
- If lxml is not available for post-processing, skip DC elements (they are OPDS 1.2 "SHOULD", not "MUST")

### Risk 5: `OPDSEntry.from_zim_export()` field mapping error
**Probability**: Low (the field mapping is straightforward 1-to-1)  
**Impact**: High — wrong download URLs or file sizes in the catalog mislead users  
**Detection**: `test_opds_from_zim_export_factory` test catches wrong field mappings  
**Mitigation**:
- The factory test must be P0 and must verify every field individually, not just "construction succeeds"
- Add a validation step in `OPDSCatalogService.regenerate()` that calls `OPDSGenerator.validate_opds_xml()` on the generated output before writing to the endpoint response

### Risk 6: Version history incorrectly populated or missing
**Probability**: Low  
**Impact**: Low — users can still download the current version; history is a nice-to-have  
**Detection**: Kiwix shows only one version instead of previous versions  
**Mitigation**:
- Add a dedicated query in `OPDSCatalogService.regenerate()` that fetches `status='superseded'` rows ordered by period descending, limited to `max_version_history`
- Integration test: create two exports with the same name+flavour, run regenerate(), verify version history has 1 entry

---

## Deployment Gates and Go-Live Checklist

See `PHASE_5_IMPLEMENTATION_DECISION_TREE.md` for the shared go-live checklist.

### OPDS-Specific Pre-Deployment Verification

```
[ ] Candidate 1 (ZimWriter) is merged and producing real ZIM exports
[ ] zim_exports table has at least one row with status='available' and cdn_url populated
[ ] uv run pytest tests/unit/test_opds_generator.py -v — all 23 tests pass
[ ] GET /opds/v2/root.xml returns 200 with Content-Type: application/atom+xml
[ ] GET /opds/v2/entries returns acquisition feed with at least one entry
[ ] Feed XML is valid: OPDSGenerator.validate_opds_xml() returns empty list
[ ] Kiwix Android (F-Droid): OPDS URL shows open-repo library with "Install" button
[ ] Kiwix Desktop: OPDS URL shows same library
[ ] kiwix-serve: catalog endpoint returns correct archive list
[ ] Search description XML is valid: GET /opds/v2/searchdescription.xml is well-formed
[ ] Version history: second export for same flavour appears in version_history of first
[ ] Catalog regenerates automatically after new ZIM export completes
```

---

## Post-Launch Monitoring

### Metrics to Watch

| Metric | Tool | Alert threshold |
|--------|------|----------------|
| OPDS endpoint availability | Uptime monitor on `/opds/v2/root.xml` | Alert if response > 500ms or non-200 |
| Catalog entry count | `OPDSGenerator.entry_count()` in health endpoint | Alert if 0 (catalog regeneration may have failed) |
| Feed parse errors | `validate_opds_xml()` result logged after each regeneration | Alert on any non-empty error list |
| Kiwix catalog discovery rate | Kiwix Library download events from R2 logs | Monitor weekly trend; significant drop may indicate feed breakage |
| OPDS endpoint cache hit rate | Cloudflare cache analytics | Feed should be cached; direct origin hits indicate missing cache headers |

### Health Check Integration

Extend the existing `GET /api/exports/health` endpoint with OPDS status:

```json
{
  "last_successful_export": "2026-05-19T02:03:14Z",
  "opds": {
    "catalog_url": "https://node.example.org/opds/v2/root.xml",
    "entry_count": 6,
    "last_regenerated": "2026-05-19T02:04:22Z",
    "validation_errors": []
  }
}
```

---

## Sources

- [OPDS 1.2 Specification](https://specs.opds.io/opds-1.2.html)
- [OPDS 1.0 Specification (base)](https://specs.opds.io/opds-1.0.html)
- [feedgen PyPI](https://pypi.org/project/feedgen/)
- [feedgen GitHub](https://github.com/lkiesow/python-feedgen)
- [feedgen Documentation](https://feedgen.kiesow.be/)
- [Kiwix OPDS documentation](https://wiki.kiwix.org/wiki/OPDS)
- [Atom Syndication Format RFC 4287](https://tools.ietf.org/html/rfc4287)
- [OpenSearch 1.1 Specification](http://a9.com/-/spec/opensearch/1.1/)
- [Dublin Core Terms namespace](http://purl.org/dc/terms/)
