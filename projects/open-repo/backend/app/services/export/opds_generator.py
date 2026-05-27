"""
OPDSGenerator: OPDS 1.2 catalog generation for open-repo ZIM export discovery.

Generates an Atom-based OPDS catalog that allows Kiwix apps and other OPDS clients
to discover and download open-repo ZIM exports. The catalog is regenerated after
each successful export job and committed to the database for serving via the FastAPI
OPDS endpoint at /opds/v2/root.xml.

OPDS Catalog Spec: https://wiki.kiwix.org/wiki/OPDS
Atom RFC 4287: https://tools.ietf.org/html/rfc4287

Design references:
  - phase-5-offline-export-architecture.md section 4 (OPDS Catalog Integration)
  - phase-5-kiwix-integration-guide.md section 7 (OPDS strategy)

Dependencies:
  - feedgen>=0.9 (PyPI: feedgen) — Atom feed generation

Usage pattern (post-implementation):
    generator = OPDSGenerator(
        node_uuid="550e8400-e29b-41d4-a716-446655440000",
        node_name="Open-Repo Node",
        node_url="https://node.example.org",
        catalog_url="https://node.example.org/opds/v2/root.xml",
    )
    for export_row in db.query(ZimExport).filter_by(is_current=True):
        entry = OPDSEntry.from_zim_export(export_row)
        generator.add_entry(entry)
    xml_bytes = generator.generate_root_catalog()
    xml_bytes = generator.generate_acquisition_feed()
"""

from __future__ import annotations

import logging
import re
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import TYPE_CHECKING, Optional
from xml.etree import ElementTree as ET

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

if TYPE_CHECKING:
    from feedgen.feed import FeedGenerator as FeedGeneratorType

logger = logging.getLogger(__name__)

# OPDS namespaces used in catalog XML
OPDS_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "opds": "http://opds-spec.org/2010/catalog",
    "dc": "http://purl.org/dc/terms/",
    "opensearch": "http://a9.com/-/spec/opensearch/1.1/",
}

# MIME types used in OPDS links
MIME_OPDS_NAV = "application/atom+xml;profile=opds-catalog;kind=navigation"
MIME_OPDS_ACQ = "application/atom+xml;profile=opds-catalog;kind=acquisition"
MIME_ZIM = "application/x-zim"
MIME_OPENSEARCH = "application/opensearchdescription+xml"


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------


@dataclass
class OPDSEntry:
    """
    Represents a single ZIM export entry in an OPDS catalog.

    Each OPDSEntry maps to one row in the zim_exports database table and
    produces one <entry> element in the OPDS acquisition feed.

    Attributes:
        uuid: Stable UUID for this ZIM flavour (must not change between versions).
            The UUID is stored in zim_exports.zim_uuid and reused across monthly
            export runs for the same name+flavour combination. Kiwix uses this UUID
            to recognize that a new export is an update to the same content.
        title: Human-readable title for the catalog entry (e.g., "Open-Repo: Full
            Library (English)"). Should match the ZIM Title metadata field.
        name: ZIM Name metadata value (e.g., "open-repo_en_nopic"). The stable
            identifier for this flavour across versions.
        flavour: Flavour string (e.g., "nopic", "all", "agriculture").
        language: ISO 639-3 language code (e.g., "eng").
        period: YYYY-MM period string for the current version (e.g., "2026-04").
        description: Short description (max 80 chars). Shown in Kiwix catalog.
        download_url: Direct HTTPS URL to the ZIM file on the CDN.
        file_size_bytes: Size of the ZIM file for display in catalog UI.
        sha256_checksum: SHA-256 checksum for download integrity verification.
        article_count: Number of articles in this ZIM for catalog metadata.
        generated_at: When this export was created (UTC).
        illustration_url: URL of the 48x48 PNG illustration for catalog thumbnail.
            Optional; Kiwix will show a blank thumbnail if not provided.
        is_reference: When True, this is a permanent Reference Export. Displayed
            in the catalog with an "Archive" tag.
        version_history: List of previous OPDSVersionEntry for the version history
            section of the acquisition feed. Ordered newest-first. Max 5 entries.
    """

    uuid: str
    title: str
    name: str
    flavour: str
    language: str
    period: str
    description: str
    download_url: str
    file_size_bytes: int
    sha256_checksum: str
    article_count: int
    generated_at: datetime
    illustration_url: Optional[str] = None
    is_reference: bool = False
    version_history: list["OPDSVersionEntry"] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Validate entry fields."""
        # Validate UUID format
        try:
            uuid.UUID(self.uuid)
        except ValueError as exc:
            raise ValueError(
                f"OPDSEntry uuid '{self.uuid}' is not a valid UUID. "
                f"Generate with: str(uuid.uuid4())"
            ) from exc

        # Validate name format
        if not re.match(r"^[a-z0-9][a-z0-9\-]*_[a-z]{2,3}_[a-z0-9\-]+$", self.name):
            raise ValueError(
                f"OPDSEntry name '{self.name}' does not match openZIM naming convention. "
                f"Expected format: {{publisher}}_{{language}}_{{flavour}}"
            )

        # Validate period format
        if not re.match(r"^\d{4}-\d{2}[a-z]?$", self.period):
            raise ValueError(
                f"OPDSEntry period '{self.period}' does not match YYYY-MM format."
            )

        # Validate description length
        if len(self.description) > 80:
            raise ValueError(
                f"OPDSEntry description exceeds 80 characters ({len(self.description)} chars). "
                f"Kiwix catalog UI will truncate longer descriptions."
            )

    @classmethod
    def from_dict(cls, data: dict) -> "OPDSEntry":
        """
        Construct an OPDSEntry from a dictionary (e.g., a database row as dict).

        Expected keys: uuid, title, name, flavour, language, period, description,
        download_url, file_size_bytes, sha256_checksum, article_count, generated_at.
        Optional: illustration_url, is_reference, version_history.
        """
        return cls(
            uuid=data["uuid"],
            title=data["title"],
            name=data["name"],
            flavour=data["flavour"],
            language=data["language"],
            period=data["period"],
            description=data["description"],
            download_url=data["download_url"],
            file_size_bytes=data["file_size_bytes"],
            sha256_checksum=data["sha256_checksum"],
            article_count=data["article_count"],
            generated_at=data["generated_at"],
            illustration_url=data.get("illustration_url"),
            is_reference=data.get("is_reference", False),
            version_history=data.get("version_history", []),
        )

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

    @property
    def filename(self) -> str:
        """Return the expected ZIM filename: {name}_{period}.zim"""
        return f"{self.name}_{self.period}.zim"

    @property
    def entry_id(self) -> str:
        """URN-format entry ID for Atom <id> element."""
        return f"urn:uuid:{self.uuid}"

    @property
    def updated_iso(self) -> str:
        """generated_at as ISO 8601 string with UTC Z suffix."""
        return self.generated_at.strftime("%Y-%m-%dT%H:%M:%SZ")

    @property
    def file_size_human(self) -> str:
        """Human-readable file size for display (e.g., '42 MB')."""
        if self.file_size_bytes < 1024:
            return f"{self.file_size_bytes} B"
        elif self.file_size_bytes < 1024 * 1024:
            return f"{self.file_size_bytes // 1024} KB"
        elif self.file_size_bytes < 1024 * 1024 * 1024:
            return f"{self.file_size_bytes // (1024 * 1024)} MB"
        else:
            return f"{self.file_size_bytes / (1024 * 1024 * 1024):.1f} GB"


@dataclass
class OPDSVersionEntry:
    """
    A previous version entry in an OPDSEntry's version history.

    Appears in the acquisition feed's version history section, allowing users
    to download older exports during the retention window.

    Attributes:
        period: YYYY-MM period string for this version.
        download_url: Download URL for this specific version.
        file_size_bytes: File size for this version.
        generated_at: When this version was generated.
        sha256_checksum: Checksum for integrity verification.
    """

    period: str
    download_url: str
    file_size_bytes: int
    generated_at: datetime
    sha256_checksum: str


# ---------------------------------------------------------------------------
# Generator
# ---------------------------------------------------------------------------


class OPDSGenerator:
    """
    Generates OPDS 1.2 catalog XML for open-repo ZIM export discovery.

    An OPDSGenerator instance is created per catalog regeneration cycle —
    typically after each successful export job. It accumulates OPDSEntry objects
    and then produces the complete OPDS catalog XML.

    The generator produces two documents:
      1. Root catalog (navigation feed): links to sub-feeds and metadata
      2. Acquisition feed: one <entry> per available ZIM export

    Both documents are valid Atom XML with OPDS profile links, accepted by
    Kiwix readers' OPDS parser.

    Thread safety: NOT thread-safe. Do not share across threads.

    Example (post-implementation):
        generator = OPDSGenerator(
            node_uuid="550e8400-e29b-41d4-a716-446655440000",
            node_name="Open-Repo Node",
            node_url="https://node.example.org",
            catalog_url="https://node.example.org/opds/v2/root.xml",
        )
        for export in db.query(ZimExport).filter_by(is_current=True):
            entry = OPDSEntry.from_dict(export.as_dict())
            generator.add_entry(entry)
        root_xml = generator.generate_root_catalog()
        entries_xml = generator.generate_acquisition_feed()
    """

    def __init__(
        self,
        node_uuid: str,
        node_name: str,
        node_url: str,
        catalog_url: str,
        max_version_history: int = 5,
    ) -> None:
        """
        Initialize OPDSGenerator.

        Args:
            node_uuid: Stable UUID for this open-repo node. Used as the <id>
                of the root catalog feed. Must not change between catalog
                regenerations. Store in node configuration.
            node_name: Human-readable name for this node (e.g., "Open-Repo Node A").
                Shown as the catalog author in Kiwix's library browser.
            node_url: The node's base URL (e.g., "https://node.example.org").
                Used for author URI and external links.
            catalog_url: The full URL of this OPDS catalog root
                (e.g., "https://node.example.org/opds/v2/root.xml").
                Used for the self-referential <link rel="self"> element.
            max_version_history: Maximum number of previous versions to include
                in each entry's version history section. Default 5, matching the
                retention policy.

        Raises:
            ValueError: If node_uuid is not a valid UUID.
        """
        try:
            uuid.UUID(node_uuid)
        except ValueError as exc:
            raise ValueError(
                f"node_uuid '{node_uuid}' is not a valid UUID."
            ) from exc

        self.node_uuid = node_uuid
        self.node_name = node_name
        self.node_url = node_url
        self.catalog_url = catalog_url
        self.max_version_history = max_version_history
        self._entries: list[OPDSEntry] = []
        self._generated_at: datetime = datetime.utcnow()

    def add_entry(self, entry: OPDSEntry) -> None:
        """
        Add a ZIM export entry to the catalog.

        Entries are included in the acquisition feed in the order they are added.
        Callers should add entries sorted by name+flavour for consistent ordering.

        Args:
            entry: OPDSEntry instance (already validated by __post_init__).

        Note:
            This method does not deduplicate entries. If two entries with the
            same UUID are added, both will appear in the feed. The caller is
            responsible for ensuring uniqueness.
        """
        self._entries.append(entry)
        logger.debug("OPDSGenerator: added entry name=%s, period=%s", entry.name, entry.period)

    def generate_root_catalog(self) -> bytes:
        """
        Generate the OPDS root navigation catalog XML.

        The root catalog provides navigation links to:
          - The acquisition feed (list of all ZIM files)
          - OpenSearch description for catalog search

        This is the document served at /opds/v2/root.xml.

        Returns:
            UTF-8 encoded XML bytes, well-formed Atom with OPDS profile.

        Structure produced:
            <feed xmlns="http://www.w3.org/2005/Atom" ...>
              <id>urn:uuid:{node_uuid}</id>
              <title>{node_name} Offline Library Catalog</title>
              <updated>...</updated>
              <author>...</author>
              <link rel="self" type="...navigation" href="{catalog_url}"/>
              <link rel="start" type="...navigation" href="{catalog_url}"/>
              <link rel="search" type="opensearch" href=".../searchdescription.xml"/>
              <entry>
                <title>All Offline Exports</title>
                <link rel="subsection" type="...acquisition" href=".../entries"/>
              </entry>
            </feed>
        """
        if _FEEDGEN_AVAILABLE:
            return self._generate_root_catalog_feedgen()
        return self._generate_root_catalog_etree()

    def generate_acquisition_feed(self) -> bytes:
        """
        Generate the OPDS acquisition feed listing all available ZIM exports.

        The acquisition feed contains one <entry> per ZIM export. Each entry
        includes the download link (with MIME type application/x-zim), file
        metadata, and version history.

        This is the document served at /opds/v2/entries.

        Returns:
            UTF-8 encoded XML bytes.

        Entry structure:
            <entry>
              <id>urn:uuid:{entry.uuid}</id>
              <title>{entry.title}</title>
              <updated>{entry.updated_iso}</updated>
              <dc:language>{entry.language}</dc:language>
              <summary>{entry.description}</summary>
              <link type="image/png" href="{illustration_url}" rel="http://opds-spec.org/image"/>
              <link type="application/x-zim" href="{download_url}"
                    rel="http://opds-spec.org/acquisition"
                    length="{file_size_bytes}"
                    title="{filename}"/>
            </entry>

        Version history is added as additional <link> elements with
        rel="related" and a custom title like "Previous version: 2026-03".
        """
        if _FEEDGEN_AVAILABLE:
            xml_bytes = self._generate_acquisition_feed_feedgen()
            # Post-process to add DC namespace elements if lxml is available
            return self._add_dc_elements_to_feed(xml_bytes, self._entries)
        return self._generate_acquisition_feed_etree()

    def generate_single_entry(self, entry_uuid: str) -> Optional[bytes]:
        """
        Generate the OPDS XML for a single ZIM entry by UUID.

        Used by the /opds/v2/entry/{uuid} endpoint.

        Args:
            entry_uuid: UUID of the entry to retrieve.

        Returns:
            UTF-8 encoded XML bytes for the single entry, or None if not found.
        """
        entry = next((e for e in self._entries if e.uuid == entry_uuid), None)
        if entry is None:
            return None

        feed_elem = self._make_feed_element(
            feed_id=f"urn:uuid:{entry_uuid}",
            title=entry.title,
            feed_type=MIME_OPDS_ACQ,
            self_url=f"{self.catalog_url.replace('root.xml', '')}entry/{entry_uuid}",
        )
        self._add_entry_to_feed(feed_elem, entry)
        xml_str = ET.tostring(feed_elem, encoding="unicode", xml_declaration=False)
        return ('<?xml version="1.0" encoding="UTF-8"?>\n' + xml_str).encode("utf-8")

    def generate_search_description(self) -> bytes:
        """
        Generate OpenSearch description XML for catalog search.

        Used by the /opds/v2/searchdescription.xml endpoint.
        Kiwix uses this to enable search within the catalog.

        Returns:
            UTF-8 encoded OpenSearch description XML.

        TODO(post-PR-merge): Add a proper search endpoint that filters
        the acquisition feed by title/description query parameter.
        """
        entries_url = self.catalog_url.replace("root.xml", "entries")
        xml = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">\n'
            f'  <ShortName>{self.node_name}</ShortName>\n'
            f'  <Description>Search {self.node_name} offline library catalog</Description>\n'
            f'  <Url type="{MIME_OPDS_ACQ}" template="{entries_url}?q={{searchTerms}}"/>\n'
            '</OpenSearchDescription>\n'
        )
        return xml.encode("utf-8")

    def entry_count(self) -> int:
        """Return the number of entries currently in the catalog."""
        return len(self._entries)

    def get_entry_by_name(self, name: str) -> Optional[OPDSEntry]:
        """
        Return the OPDSEntry matching the given ZIM Name value.

        Returns the first match (there should be at most one current entry
        per name in a correctly-maintained catalog).
        """
        return next((e for e in self._entries if e.name == name), None)

    def get_entries_sorted(self) -> list[OPDSEntry]:
        """
        Return entries sorted by name (alphabetically), then by period descending.

        This order matches the expected Kiwix catalog display: alphabetical by
        content name, newest version first within each name.
        """
        # Sort by name ascending, then by period descending
        return sorted(
            self._entries,
            key=lambda e: (e.name, -int(e.period.replace("-", ""))),
        )

    # -------------------------------------------------------------------------
    # feedgen-based generation (primary path)
    # -------------------------------------------------------------------------

    def _generate_root_catalog_feedgen(self) -> bytes:
        """feedgen-based root catalog generation."""
        entries_url = self.catalog_url.replace("root.xml", "entries")
        search_url = self.catalog_url.replace("root.xml", "searchdescription.xml")

        fg = FeedGenerator()
        fg.id(f"urn:uuid:{self.node_uuid}")
        fg.title(f"{self.node_name} Offline Library Catalog")
        fg.author({"name": self.node_name, "uri": self.node_url})
        fg.updated(self._generated_at.isoformat() + "Z")

        # OPDS profile link relations
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
        fe.updated(self._generated_at.isoformat() + "Z")
        fe.summary(f"{len(self._entries)} offline ZIM file(s) available for download")
        fe.link(href=entries_url, rel="subsection", type=MIME_OPDS_ACQ)

        return fg.atom_str(pretty=True)

    def _generate_acquisition_feed_feedgen(self) -> bytes:
        """feedgen-based acquisition feed generation."""
        entries_url = self.catalog_url.replace("root.xml", "entries")

        fg = FeedGenerator()
        fg.id(f"urn:uuid:{self.node_uuid}:entries")
        fg.title(f"{self.node_name} — All Offline Exports")
        fg.author({"name": self.node_name, "uri": self.node_url})
        fg.updated(self._generated_at.isoformat() + "Z")
        fg.link(href=entries_url, rel="self", type=MIME_OPDS_ACQ)
        fg.link(href=self.catalog_url, rel="start", type=MIME_OPDS_NAV)

        for entry in self.get_entries_sorted():
            self._add_feedgen_entry(fg, entry)

        return fg.atom_str(pretty=True)

    def _add_feedgen_entry(self, fg: "FeedGeneratorType", entry: "OPDSEntry") -> None:
        """Add an OPDSEntry to a feedgen FeedGenerator as a FeedEntry."""
        fe = fg.add_entry()
        fe.id(entry.entry_id)
        fe.title(entry.title)
        fe.updated(entry.generated_at.isoformat() + "Z")
        fe.summary(entry.description)

        # Acquisition link (primary download)
        fe.link(
            href=entry.download_url,
            rel="http://opds-spec.org/acquisition",
            type=MIME_ZIM,
            title=entry.filename,
        )

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
            fe.link(href=entry.illustration_url,
                    rel="http://opds-spec.org/image/thumbnail",
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

        # Archive tag for Reference Exports
        if entry.is_reference:
            fe.category(term="archive", label="Permanent Archive",
                       scheme="http://opds-spec.org/system/")

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
            logger.warning(
                "lxml not available; DC namespace elements will be omitted from OPDS feed. "
                "Install lxml for full OPDS 1.2 compliance."
            )
            return xml_bytes

        ATOM_NS = "http://www.w3.org/2005/Atom"
        DC_NS = "http://purl.org/dc/terms/"
        OPENSEARCH_NS = "http://a9.com/-/spec/opensearch/1.1/"

        root = etree.fromstring(xml_bytes)
        nsmap = dict(root.nsmap or {})
        nsmap["dc"] = DC_NS
        nsmap["opensearch"] = OPENSEARCH_NS

        # Add opensearch:totalResults to feed (at the beginning)
        total_elem = etree.Element(f"{{{OPENSEARCH_NS}}}totalResults")
        total_elem.text = str(len(entries))
        # Insert after updated element if it exists, else at the start
        updated_elem = root.find(f"{{{ATOM_NS}}}updated")
        if updated_elem is not None:
            updated_index = list(root).index(updated_elem)
            root.insert(updated_index + 1, total_elem)
        else:
            root.insert(0, total_elem)

        # Add dc:language and dc:issued to each entry
        entry_map = {e.entry_id: e for e in entries}
        for entry_elem in root.findall(f"{{{ATOM_NS}}}entry"):
            id_elem = entry_elem.find(f"{{{ATOM_NS}}}id")
            if id_elem is None:
                continue
            opds_entry = entry_map.get(id_elem.text)
            if opds_entry is None:
                continue

            # Add after summary if present, else at start
            summary_elem = entry_elem.find(f"{{{ATOM_NS}}}summary")
            insert_index = 0
            if summary_elem is not None:
                insert_index = list(entry_elem).index(summary_elem) + 1

            lang_elem = etree.Element(f"{{{DC_NS}}}language")
            lang_elem.text = opds_entry.language
            entry_elem.insert(insert_index, lang_elem)

            issued_elem = etree.Element(f"{{{DC_NS}}}issued")
            issued_elem.text = opds_entry.period
            entry_elem.insert(insert_index + 1, issued_elem)

        return etree.tostring(root, xml_declaration=True,
                              encoding="utf-8", pretty_print=True)

    # -------------------------------------------------------------------------
    # xml.etree-based generation (fallback if feedgen unavailable)
    # -------------------------------------------------------------------------

    def _generate_root_catalog_etree(self) -> bytes:
        """Fallback: xml.etree-based root catalog generation."""
        root = self._build_root_catalog_element()
        xml_str = ET.tostring(root, encoding="unicode", xml_declaration=False)
        xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>\n'
        return (xml_declaration + xml_str).encode("utf-8")

    def _generate_acquisition_feed_etree(self) -> bytes:
        """Fallback: xml.etree-based acquisition feed generation."""
        feed = self._build_acquisition_feed_element()
        xml_str = ET.tostring(feed, encoding="unicode", xml_declaration=False)
        xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>\n'
        return (xml_declaration + xml_str).encode("utf-8")

    # -------------------------------------------------------------------------
    # Internal XML building helpers
    # -------------------------------------------------------------------------

    def _build_root_catalog_element(self) -> ET.Element:
        """Build the root navigation catalog <feed> element."""
        entries_url = self.catalog_url.replace("root.xml", "entries")
        search_url = self.catalog_url.replace("root.xml", "searchdescription.xml")

        feed = self._make_feed_element(
            feed_id=f"urn:uuid:{self.node_uuid}",
            title=f"{self.node_name} Offline Library Catalog",
            feed_type=MIME_OPDS_NAV,
            self_url=self.catalog_url,
        )

        # OpenSearch link
        ET.SubElement(feed, "link", {
            "rel": "search",
            "type": MIME_OPENSEARCH,
            "href": search_url,
        })

        # Navigation entry: All Offline Exports
        entry_elem = ET.SubElement(feed, "entry")
        ET.SubElement(entry_elem, "title").text = "All Offline Exports"
        ET.SubElement(entry_elem, "id").text = f"urn:uuid:{self.node_uuid}:all"
        ET.SubElement(entry_elem, "updated").text = self._generated_at.strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )
        ET.SubElement(entry_elem, "summary").text = (
            f"{len(self._entries)} offline ZIM file(s) available for download"
        )
        ET.SubElement(entry_elem, "link", {
            "rel": "subsection",
            "type": MIME_OPDS_ACQ,
            "href": entries_url,
        })

        return feed

    def _build_acquisition_feed_element(self) -> ET.Element:
        """Build the acquisition feed <feed> element with all entries."""
        entries_url = self.catalog_url.replace("root.xml", "entries")

        feed = self._make_feed_element(
            feed_id=f"urn:uuid:{self.node_uuid}:entries",
            title=f"{self.node_name} — All Offline Exports",
            feed_type=MIME_OPDS_ACQ,
            self_url=entries_url,
        )

        # Add totalResults for OPDS pagination compliance
        total_elem = ET.SubElement(feed, "opensearch:totalResults")
        total_elem.text = str(len(self._entries))
        total_elem.set("xmlns:opensearch", OPDS_NS["opensearch"])

        for entry in self.get_entries_sorted():
            self._add_entry_to_feed(feed, entry)

        return feed

    def _add_entry_to_feed(self, feed: ET.Element, entry: OPDSEntry) -> None:
        """
        Add a single OPDSEntry as an <entry> element to the feed.

        TODO(post-PR-merge): Add dc:language, dc:issued, and opensearch elements.
        These require the DC and OpenSearch XML namespaces to be properly declared
        on the root feed element. The current stub includes them on individual
        elements which is valid but verbose.
        """
        entry_elem = ET.SubElement(feed, "entry")

        ET.SubElement(entry_elem, "id").text = entry.entry_id
        ET.SubElement(entry_elem, "title").text = entry.title
        ET.SubElement(entry_elem, "updated").text = entry.updated_iso
        ET.SubElement(entry_elem, "summary").text = entry.description

        # DC metadata
        lang_elem = ET.SubElement(entry_elem, "dc:language")
        lang_elem.text = entry.language
        lang_elem.set("xmlns:dc", OPDS_NS["dc"])

        # Article count as dc:extent
        extent_elem = ET.SubElement(entry_elem, "dc:extent")
        extent_elem.text = f"{entry.article_count:,} articles"
        extent_elem.set("xmlns:dc", OPDS_NS["dc"])

        # Illustration (thumbnail)
        if entry.illustration_url:
            ET.SubElement(entry_elem, "link", {
                "rel": "http://opds-spec.org/image",
                "type": "image/png",
                "href": entry.illustration_url,
            })
            ET.SubElement(entry_elem, "link", {
                "rel": "http://opds-spec.org/image/thumbnail",
                "type": "image/png",
                "href": entry.illustration_url,
            })

        # Primary acquisition link (current version)
        ET.SubElement(entry_elem, "link", {
            "rel": "http://opds-spec.org/acquisition",
            "type": MIME_ZIM,
            "href": entry.download_url,
            "length": str(entry.file_size_bytes),
            "title": entry.filename,
        })

        # SHA-256 checksum sidecar link
        ET.SubElement(entry_elem, "link", {
            "rel": "related",
            "type": "text/plain",
            "href": entry.download_url + ".sha256",
            "title": f"SHA-256 checksum for {entry.filename}",
        })

        # Version history links (previous versions, newest first)
        history = sorted(
            entry.version_history,
            key=lambda v: v.period,
            reverse=True,
        )[:self.max_version_history]

        for prev in history:
            ET.SubElement(entry_elem, "link", {
                "rel": "related",
                "type": MIME_ZIM,
                "href": prev.download_url,
                "length": str(prev.file_size_bytes),
                "title": f"Previous version: {prev.period} ({_human_size(prev.file_size_bytes)})",
            })

        # Archive tag for Reference Exports
        if entry.is_reference:
            ET.SubElement(entry_elem, "category", {
                "term": "archive",
                "label": "Permanent Archive",
                "scheme": "http://opds-spec.org/system/",
            })

    def _make_feed_element(
        self,
        feed_id: str,
        title: str,
        feed_type: str,
        self_url: str,
    ) -> ET.Element:
        """Create a base <feed> element with id, title, updated, author, and self-link."""
        feed = ET.Element("feed", {
            "xmlns": OPDS_NS["atom"],
            "xmlns:opds": OPDS_NS["opds"],
        })

        ET.SubElement(feed, "id").text = feed_id
        ET.SubElement(feed, "title").text = title
        ET.SubElement(feed, "updated").text = self._generated_at.strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )

        author = ET.SubElement(feed, "author")
        ET.SubElement(author, "name").text = self.node_name
        ET.SubElement(author, "uri").text = self.node_url

        # Self-reference link
        ET.SubElement(feed, "link", {
            "rel": "self",
            "type": feed_type,
            "href": self_url,
        })

        # Start link (root catalog)
        ET.SubElement(feed, "link", {
            "rel": "start",
            "type": MIME_OPDS_NAV,
            "href": self.catalog_url,
        })

        return feed

    @staticmethod
    def validate_opds_xml(xml_bytes: bytes) -> list[str]:
        """
        Validate that OPDS XML is well-formed and contains required elements.

        Returns a list of error strings. Empty list means valid.

        Checks performed:
          1. Well-formed XML (parses without exception)
          2. Root element is <feed>
          3. <id> element is present and non-empty
          4. <title> element is present and non-empty
          5. <updated> element is present and in ISO 8601 format
          6. At least one <link rel="self"> exists
          7. All <entry> elements have <id>, <title>, and at least one <link>

        TODO(post-PR-merge): Validate against the full OPDS 1.2 schema using
        lxml's RelaxNG or Schematron validator for stricter compliance.
        """
        errors = []

        try:
            root = ET.fromstring(xml_bytes)
        except ET.ParseError as exc:
            return [f"XML parse error: {exc}"]

        # Root element check
        local = root.tag.split("}")[-1] if "}" in root.tag else root.tag
        if local != "feed":
            errors.append(f"Root element must be <feed>, got <{local}>")

        # Required elements
        ns = f"{{{OPDS_NS['atom']}}}"
        id_elem = root.find(f"{ns}id")
        if id_elem is None or not id_elem.text:
            errors.append("Missing or empty <id> element in feed")

        title_elem = root.find(f"{ns}title")
        if title_elem is None or not title_elem.text:
            errors.append("Missing or empty <title> element in feed")

        updated_elem = root.find(f"{ns}updated")
        if updated_elem is None or not updated_elem.text:
            errors.append("Missing or empty <updated> element in feed")
        elif not re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", updated_elem.text):
            errors.append(
                f"<updated> element has invalid ISO 8601 format: '{updated_elem.text}'"
            )

        # Self link
        self_links = [
            elem for elem in root.findall(f"{ns}link")
            if elem.get("rel") == "self"
        ]
        if not self_links:
            errors.append("Missing <link rel='self'> in feed")

        # Entry validation
        for i, entry_elem in enumerate(root.findall(f"{ns}entry")):
            entry_id = entry_elem.find(f"{ns}id")
            if entry_id is None or not entry_id.text:
                errors.append(f"Entry #{i+1}: missing or empty <id>")

            entry_title = entry_elem.find(f"{ns}title")
            if entry_title is None or not entry_title.text:
                errors.append(f"Entry #{i+1}: missing or empty <title>")

            entry_links = entry_elem.findall(f"{ns}link")
            if not entry_links:
                errors.append(f"Entry #{i+1}: no <link> elements")

        return errors


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------


def _human_size(size_bytes: int) -> str:
    """Format bytes as human-readable string (e.g., '42 MB')."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes // 1024} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes // (1024 * 1024)} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"
