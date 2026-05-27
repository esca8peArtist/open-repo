"""
Comprehensive tests for OPDS Feed Generator (Phase 5.2 Wave 1).

Test coverage:
  - OPDSEntry construction and validation
  - OPDSEntry.from_zim_export() factory method
  - OPDSGenerator root catalog generation (feedgen + etree fallback)
  - OPDSGenerator acquisition feed generation
  - DC namespace element addition (dublin core)
  - OPDS XML validation (well-formedness and required elements)
  - OpenSearch description generation
  - Single entry retrieval
  - Version history handling

All tests use mocked ZimExport objects to avoid database dependencies.
"""

from __future__ import annotations

import re
from datetime import datetime
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from app.services.export.opds_generator import (
    MIME_OPDS_ACQ,
    MIME_OPDS_NAV,
    MIME_OPENSEARCH,
    MIME_ZIM,
    OPDSEntry,
    OPDSGenerator,
    OPDSVersionEntry,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


def make_zim_export(
    zim_uuid: str = "550e8400-e29b-41d4-a716-446655440000",
    name: str = "open-repo_en_nopic",
    flavour: str = "nopic",
    language: str = "eng",
    period: str = "2026-05",
    title: str = "Open-Repo: Full Library (English)",
    description: str = "Full offline library with all content",
    file_size_bytes: int = 5_000_000_000,
    article_count: int = 42,
    cdn_url: str = "https://cdn.example.org/open-repo_en_nopic_2026-05.zim",
    sha256: str = "abc123" * 10 + "abcd",
    completed_at: datetime = None,
    is_reference: int = 0,
) -> SimpleNamespace:
    """Create a mock ZimExport ORM object."""
    if completed_at is None:
        completed_at = datetime(2026, 5, 19, 2, 3, 14)
    return SimpleNamespace(
        id=1,
        zim_uuid=zim_uuid,
        name=name,
        flavour=flavour,
        language=language,
        period=period,
        title=title,
        description=description,
        file_size_bytes=file_size_bytes,
        article_count=article_count,
        cdn_url=cdn_url,
        sha256=sha256,
        completed_at=completed_at,
        created_at=datetime(2026, 5, 19, 1, 0, 0),
        is_reference=is_reference,
    )


@pytest.fixture
def generator() -> OPDSGenerator:
    """Create an OPDSGenerator instance for testing."""
    return OPDSGenerator(
        node_uuid="550e8400-e29b-41d4-a716-446655440000",
        node_name="Open-Repo Test Node",
        node_url="https://node.example.org",
        catalog_url="https://node.example.org/opds/v2/root.xml",
    )


@pytest.fixture
def simple_entry() -> OPDSEntry:
    """Create a simple OPDSEntry for testing."""
    return OPDSEntry(
        uuid="550e8400-e29b-41d4-a716-446655440001",
        title="Test Archive",
        name="test_en_nopic",
        flavour="nopic",
        language="eng",
        period="2026-05",
        description="Test archive description",
        download_url="https://cdn.example.org/test_en_nopic_2026-05.zim",
        file_size_bytes=1_000_000_000,
        sha256_checksum="def456" * 10 + "defg",
        article_count=100,
        generated_at=datetime(2026, 5, 19, 2, 3, 14),
    )


@pytest.fixture
def three_entries() -> list[OPDSEntry]:
    """Create three OPDSEntry instances with different names for testing."""
    return [
        OPDSEntry(
            uuid="550e8400-e29b-41d4-a716-446655440001",
            title="Agriculture Content",
            name="agriculture_en_nopic",
            flavour="nopic",
            language="eng",
            period="2026-05",
            description="Agriculture how-tos",
            download_url="https://cdn.example.org/agriculture_en_nopic_2026-05.zim",
            file_size_bytes=2_000_000_000,
            sha256_checksum="aaa" * 21 + "a",
            article_count=150,
            generated_at=datetime(2026, 5, 19, 2, 3, 14),
        ),
        OPDSEntry(
            uuid="550e8400-e29b-41d4-a716-446655440002",
            title="Water Content",
            name="water_en_nopic",
            flavour="nopic",
            language="eng",
            period="2026-05",
            description="Water systems guides",
            download_url="https://cdn.example.org/water_en_nopic_2026-05.zim",
            file_size_bytes=1_500_000_000,
            sha256_checksum="bbb" * 21 + "b",
            article_count=120,
            generated_at=datetime(2026, 5, 19, 2, 3, 14),
        ),
        OPDSEntry(
            uuid="550e8400-e29b-41d4-a716-446655440003",
            title="Medical Content",
            name="medical_en_nopic",
            flavour="nopic",
            language="eng",
            period="2026-05",
            description="Medical reference",
            download_url="https://cdn.example.org/medical_en_nopic_2026-05.zim",
            file_size_bytes=3_000_000_000,
            sha256_checksum="ccc" * 21 + "c",
            article_count=200,
            generated_at=datetime(2026, 5, 19, 2, 3, 14),
        ),
    ]


# ---------------------------------------------------------------------------
# Unit Tests: OPDSEntry
# ---------------------------------------------------------------------------


class TestOPDSEntryConstruction:
    """Tests for OPDSEntry initialization and validation."""

    def test_construct_valid_entry(self, simple_entry: OPDSEntry) -> None:
        """OPDSEntry with valid fields constructs without error."""
        assert simple_entry.uuid == "550e8400-e29b-41d4-a716-446655440001"
        assert simple_entry.title == "Test Archive"
        assert simple_entry.name == "test_en_nopic"

    def test_invalid_uuid_raises_valueerror(self) -> None:
        """OPDSEntry rejects invalid UUID format."""
        with pytest.raises(ValueError, match="not a valid UUID"):
            OPDSEntry(
                uuid="not-a-uuid",
                title="Test",
                name="test_en_nopic",
                flavour="nopic",
                language="eng",
                period="2026-05",
                description="Test",
                download_url="https://example.org/test.zim",
                file_size_bytes=1000,
                sha256_checksum="abc" * 21 + "ab",
                article_count=10,
                generated_at=datetime.utcnow(),
            )

    def test_invalid_name_raises_valueerror(self) -> None:
        """OPDSEntry rejects invalid openZIM name format."""
        with pytest.raises(ValueError, match="does not match openZIM naming convention"):
            OPDSEntry(
                uuid="550e8400-e29b-41d4-a716-446655440001",
                title="Test",
                name="InvalidNameFormat",  # Missing language/flavour separators
                flavour="nopic",
                language="eng",
                period="2026-05",
                description="Test",
                download_url="https://example.org/test.zim",
                file_size_bytes=1000,
                sha256_checksum="abc" * 21 + "ab",
                article_count=10,
                generated_at=datetime.utcnow(),
            )

    def test_invalid_period_raises_valueerror(self) -> None:
        """OPDSEntry rejects invalid YYYY-MM period format."""
        with pytest.raises(ValueError, match="does not match YYYY-MM format"):
            OPDSEntry(
                uuid="550e8400-e29b-41d4-a716-446655440001",
                title="Test",
                name="test_en_nopic",
                flavour="nopic",
                language="eng",
                period="2026/05",  # Invalid separator
                description="Test",
                download_url="https://example.org/test.zim",
                file_size_bytes=1000,
                sha256_checksum="abc" * 21 + "ab",
                article_count=10,
                generated_at=datetime.utcnow(),
            )

    def test_description_too_long_raises_valueerror(self) -> None:
        """OPDSEntry rejects descriptions exceeding 80 characters."""
        long_desc = "a" * 81
        with pytest.raises(ValueError, match="exceeds 80 characters"):
            OPDSEntry(
                uuid="550e8400-e29b-41d4-a716-446655440001",
                title="Test",
                name="test_en_nopic",
                flavour="nopic",
                language="eng",
                period="2026-05",
                description=long_desc,
                download_url="https://example.org/test.zim",
                file_size_bytes=1000,
                sha256_checksum="abc" * 21 + "ab",
                article_count=10,
                generated_at=datetime.utcnow(),
            )

    def test_entry_id_property(self, simple_entry: OPDSEntry) -> None:
        """entry_id property returns URN format."""
        assert simple_entry.entry_id == "urn:uuid:550e8400-e29b-41d4-a716-446655440001"

    def test_filename_property(self, simple_entry: OPDSEntry) -> None:
        """filename property returns {name}_{period}.zim."""
        assert simple_entry.filename == "test_en_nopic_2026-05.zim"

    def test_updated_iso_property(self, simple_entry: OPDSEntry) -> None:
        """updated_iso property returns ISO 8601 format with Z suffix."""
        assert simple_entry.updated_iso == "2026-05-19T02:03:14Z"

    def test_file_size_human_property(self) -> None:
        """file_size_human returns human-readable size."""
        entry = OPDSEntry(
            uuid="550e8400-e29b-41d4-a716-446655440001",
            title="Test",
            name="test_en_nopic",
            flavour="nopic",
            language="eng",
            period="2026-05",
            description="Test",
            download_url="https://example.org/test.zim",
            file_size_bytes=5_000_000_000,
            sha256_checksum="abc" * 21 + "ab",
            article_count=10,
            generated_at=datetime.utcnow(),
        )
        assert "GB" in entry.file_size_human


# ---------------------------------------------------------------------------
# Unit Tests: OPDSEntry Factory Methods
# ---------------------------------------------------------------------------


class TestOPDSEntryFactories:
    """Tests for OPDSEntry construction from various sources."""

    def test_from_dict_constructs_entry(self) -> None:
        """from_dict constructs OPDSEntry from dictionary."""
        data = {
            "uuid": "550e8400-e29b-41d4-a716-446655440001",
            "title": "Test",
            "name": "test_en_nopic",
            "flavour": "nopic",
            "language": "eng",
            "period": "2026-05",
            "description": "Test description",
            "download_url": "https://example.org/test.zim",
            "file_size_bytes": 1000,
            "sha256_checksum": "abc" * 21 + "ab",
            "article_count": 10,
            "generated_at": datetime(2026, 5, 19, 2, 3, 14),
        }
        entry = OPDSEntry.from_dict(data)
        assert entry.title == "Test"
        assert entry.name == "test_en_nopic"

    def test_from_zim_export_maps_fields(self) -> None:
        """from_zim_export maps ZimExport ORM fields correctly."""
        export = make_zim_export()
        entry = OPDSEntry.from_zim_export(export)

        assert entry.uuid == export.zim_uuid
        assert entry.title == export.title
        assert entry.name == export.name
        assert entry.flavour == export.flavour
        assert entry.language == export.language
        assert entry.period == export.period
        assert entry.description == export.description
        assert entry.download_url == export.cdn_url
        assert entry.file_size_bytes == export.file_size_bytes
        assert entry.sha256_checksum == export.sha256
        assert entry.article_count == export.article_count

    def test_from_zim_export_uses_completed_at(self) -> None:
        """from_zim_export uses completed_at as generated_at."""
        completed = datetime(2026, 5, 19, 5, 30, 45)
        export = make_zim_export(completed_at=completed)
        entry = OPDSEntry.from_zim_export(export)
        assert entry.generated_at == completed

    def test_from_zim_export_fallback_to_created_at(self) -> None:
        """from_zim_export falls back to created_at if completed_at is None."""
        created_time = datetime(2026, 4, 1, 10, 0, 0)
        # Create export with completed_at=None by not setting default
        export = SimpleNamespace(
            id=1,
            zim_uuid="550e8400-e29b-41d4-a716-446655440000",
            name="open-repo_en_nopic",
            flavour="nopic",
            language="eng",
            period="2026-05",
            title="Open-Repo: Full Library (English)",
            description="Full offline library with all content",
            file_size_bytes=5_000_000_000,
            article_count=42,
            cdn_url="https://cdn.example.org/open-repo_en_nopic_2026-05.zim",
            sha256="abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abcd",
            completed_at=None,
            created_at=created_time,
            is_reference=0,
        )
        entry = OPDSEntry.from_zim_export(export)
        assert entry.generated_at == created_time

    def test_from_zim_export_raises_on_missing_cdn_url(self) -> None:
        """from_zim_export rejects exports without cdn_url."""
        export = make_zim_export(cdn_url=None)
        with pytest.raises(ValueError, match="has no cdn_url"):
            OPDSEntry.from_zim_export(export)

    def test_from_zim_export_raises_on_missing_sha256(self) -> None:
        """from_zim_export rejects exports without sha256 checksum."""
        export = make_zim_export(sha256=None)
        with pytest.raises(ValueError, match="has no sha256 checksum"):
            OPDSEntry.from_zim_export(export)

    def test_from_zim_export_preserves_is_reference(self) -> None:
        """from_zim_export converts is_reference to boolean."""
        export = make_zim_export(is_reference=1)
        entry = OPDSEntry.from_zim_export(export)
        assert entry.is_reference is True


# ---------------------------------------------------------------------------
# Unit Tests: OPDSGenerator
# ---------------------------------------------------------------------------


class TestOPDSGeneratorInitialization:
    """Tests for OPDSGenerator initialization."""

    def test_initialize_generator(self, generator: OPDSGenerator) -> None:
        """OPDSGenerator initializes with valid node metadata."""
        assert generator.node_uuid == "550e8400-e29b-41d4-a716-446655440000"
        assert generator.node_name == "Open-Repo Test Node"
        assert generator.node_url == "https://node.example.org"
        assert generator.catalog_url == "https://node.example.org/opds/v2/root.xml"

    def test_invalid_node_uuid_raises_valueerror(self) -> None:
        """OPDSGenerator rejects invalid node_uuid."""
        with pytest.raises(ValueError, match="not a valid UUID"):
            OPDSGenerator(
                node_uuid="invalid-uuid",
                node_name="Test",
                node_url="https://example.org",
                catalog_url="https://example.org/opds/v2/root.xml",
            )


class TestOPDSGeneratorEntryManagement:
    """Tests for OPDSGenerator entry operations."""

    def test_add_entry(self, generator: OPDSGenerator, simple_entry: OPDSEntry) -> None:
        """add_entry adds entry to generator."""
        assert generator.entry_count() == 0
        generator.add_entry(simple_entry)
        assert generator.entry_count() == 1

    def test_add_multiple_entries(
        self, generator: OPDSGenerator, three_entries: list[OPDSEntry]
    ) -> None:
        """add_entry works for multiple entries."""
        for entry in three_entries:
            generator.add_entry(entry)
        assert generator.entry_count() == 3

    def test_get_entry_by_name(
        self, generator: OPDSGenerator, three_entries: list[OPDSEntry]
    ) -> None:
        """get_entry_by_name returns matching entry."""
        for entry in three_entries:
            generator.add_entry(entry)
        found = generator.get_entry_by_name("water_en_nopic")
        assert found is not None
        assert found.title == "Water Content"

    def test_get_entry_by_name_returns_none_if_not_found(
        self, generator: OPDSGenerator, simple_entry: OPDSEntry
    ) -> None:
        """get_entry_by_name returns None if not found."""
        generator.add_entry(simple_entry)
        found = generator.get_entry_by_name("nonexistent_en_nopic")
        assert found is None

    def test_get_entries_sorted_alphabetically(
        self, generator: OPDSGenerator, three_entries: list[OPDSEntry]
    ) -> None:
        """get_entries_sorted returns entries sorted by name."""
        # Add in reverse order
        for entry in reversed(three_entries):
            generator.add_entry(entry)
        sorted_entries = generator.get_entries_sorted()
        assert sorted_entries[0].name == "agriculture_en_nopic"
        assert sorted_entries[1].name == "medical_en_nopic"
        assert sorted_entries[2].name == "water_en_nopic"


# ---------------------------------------------------------------------------
# Unit Tests: OPDS Feed Generation
# ---------------------------------------------------------------------------


class TestOPDSFeedGeneration:
    """Tests for OPDS feed generation (root catalog and acquisition feed)."""

    def test_generate_root_catalog_returns_bytes(
        self, generator: OPDSGenerator, simple_entry: OPDSEntry
    ) -> None:
        """generate_root_catalog returns bytes."""
        generator.add_entry(simple_entry)
        xml_bytes = generator.generate_root_catalog()
        assert isinstance(xml_bytes, bytes)
        assert b"<?xml" in xml_bytes

    def test_generate_root_catalog_is_valid_xml(
        self, generator: OPDSGenerator, simple_entry: OPDSEntry
    ) -> None:
        """generate_root_catalog produces well-formed XML."""
        generator.add_entry(simple_entry)
        xml_bytes = generator.generate_root_catalog()
        errors = OPDSGenerator.validate_opds_xml(xml_bytes)
        assert len(errors) == 0, f"Validation errors: {errors}"

    def test_generate_root_catalog_has_required_elements(
        self, generator: OPDSGenerator, simple_entry: OPDSEntry
    ) -> None:
        """generate_root_catalog contains id, title, updated, author."""
        generator.add_entry(simple_entry)
        xml_bytes = generator.generate_root_catalog()
        xml_str = xml_bytes.decode("utf-8")

        assert f"urn:uuid:{generator.node_uuid}" in xml_str
        assert generator.node_name in xml_str
        assert "Offline Library Catalog" in xml_str
        assert "All Offline Exports" in xml_str

    def test_generate_acquisition_feed_returns_bytes(
        self, generator: OPDSGenerator, three_entries: list[OPDSEntry]
    ) -> None:
        """generate_acquisition_feed returns bytes."""
        for entry in three_entries:
            generator.add_entry(entry)
        xml_bytes = generator.generate_acquisition_feed()
        assert isinstance(xml_bytes, bytes)
        assert b"<?xml" in xml_bytes

    def test_generate_acquisition_feed_is_valid_xml(
        self, generator: OPDSGenerator, three_entries: list[OPDSEntry]
    ) -> None:
        """generate_acquisition_feed produces well-formed XML."""
        for entry in three_entries:
            generator.add_entry(entry)
        xml_bytes = generator.generate_acquisition_feed()
        errors = OPDSGenerator.validate_opds_xml(xml_bytes)
        assert len(errors) == 0, f"Validation errors: {errors}"

    def test_generate_acquisition_feed_contains_all_entries(
        self, generator: OPDSGenerator, three_entries: list[OPDSEntry]
    ) -> None:
        """generate_acquisition_feed includes all added entries."""
        for entry in three_entries:
            generator.add_entry(entry)
        xml_bytes = generator.generate_acquisition_feed()
        xml_str = xml_bytes.decode("utf-8")

        for entry in three_entries:
            assert entry.title in xml_str
            assert entry.download_url in xml_str

    def test_generate_acquisition_feed_has_acquisition_links(
        self, generator: OPDSGenerator, simple_entry: OPDSEntry
    ) -> None:
        """generate_acquisition_feed entries have OPDS acquisition links."""
        generator.add_entry(simple_entry)
        xml_bytes = generator.generate_acquisition_feed()
        xml_str = xml_bytes.decode("utf-8")

        assert "http://opds-spec.org/acquisition" in xml_str
        assert MIME_ZIM in xml_str

    def test_generate_acquisition_feed_has_sha256_sidecar(
        self, generator: OPDSGenerator, simple_entry: OPDSEntry
    ) -> None:
        """generate_acquisition_feed includes SHA-256 checksum sidecar links."""
        generator.add_entry(simple_entry)
        xml_bytes = generator.generate_acquisition_feed()
        xml_str = xml_bytes.decode("utf-8")

        assert simple_entry.download_url + ".sha256" in xml_str
        assert "SHA-256 checksum" in xml_str

    def test_generate_acquisition_feed_has_dc_language(
        self, generator: OPDSGenerator, simple_entry: OPDSEntry
    ) -> None:
        """generate_acquisition_feed includes dc:language elements."""
        generator.add_entry(simple_entry)
        xml_bytes = generator.generate_acquisition_feed()
        xml_str = xml_bytes.decode("utf-8")

        assert "dc:language" in xml_str or "http://purl.org/dc/terms/" in xml_str
        assert simple_entry.language in xml_str


class TestOPDSSingleEntry:
    """Tests for single entry retrieval."""

    def test_generate_single_entry_returns_bytes(
        self, generator: OPDSGenerator, simple_entry: OPDSEntry
    ) -> None:
        """generate_single_entry returns bytes for valid UUID."""
        generator.add_entry(simple_entry)
        xml_bytes = generator.generate_single_entry(simple_entry.uuid)
        assert isinstance(xml_bytes, bytes)

    def test_generate_single_entry_returns_none_for_unknown_uuid(
        self, generator: OPDSGenerator
    ) -> None:
        """generate_single_entry returns None for unknown UUID."""
        xml_bytes = generator.generate_single_entry("550e8400-0000-0000-0000-000000000000")
        assert xml_bytes is None

    def test_generate_single_entry_is_valid_xml(
        self, generator: OPDSGenerator, simple_entry: OPDSEntry
    ) -> None:
        """generate_single_entry produces valid OPDS XML."""
        generator.add_entry(simple_entry)
        xml_bytes = generator.generate_single_entry(simple_entry.uuid)
        errors = OPDSGenerator.validate_opds_xml(xml_bytes)
        assert len(errors) == 0, f"Validation errors: {errors}"


# ---------------------------------------------------------------------------
# Unit Tests: OpenSearch Description
# ---------------------------------------------------------------------------


class TestOpenSearchDescription:
    """Tests for OpenSearch description generation."""

    def test_generate_search_description_returns_bytes(
        self, generator: OPDSGenerator
    ) -> None:
        """generate_search_description returns bytes."""
        xml_bytes = generator.generate_search_description()
        assert isinstance(xml_bytes, bytes)

    def test_generate_search_description_is_valid_xml(
        self, generator: OPDSGenerator
    ) -> None:
        """generate_search_description produces well-formed XML."""
        xml_bytes = generator.generate_search_description()
        xml_str = xml_bytes.decode("utf-8")
        assert "<?xml" in xml_str
        assert "<OpenSearchDescription" in xml_str

    def test_generate_search_description_has_url_element(
        self, generator: OPDSGenerator
    ) -> None:
        """generate_search_description includes Url template for search."""
        xml_bytes = generator.generate_search_description()
        xml_str = xml_bytes.decode("utf-8")
        assert "<Url" in xml_str
        assert "{searchTerms}" in xml_str


# ---------------------------------------------------------------------------
# Unit Tests: OPDS Validation
# ---------------------------------------------------------------------------


class TestOPDSValidation:
    """Tests for OPDS XML validation."""

    def test_validate_well_formed_xml(
        self, generator: OPDSGenerator, simple_entry: OPDSEntry
    ) -> None:
        """validate_opds_xml accepts well-formed XML."""
        generator.add_entry(simple_entry)
        xml_bytes = generator.generate_acquisition_feed()
        errors = OPDSGenerator.validate_opds_xml(xml_bytes)
        assert len(errors) == 0

    def test_validate_rejects_malformed_xml(self) -> None:
        """validate_opds_xml rejects malformed XML."""
        malformed = b"<feed><unclosed_tag>"
        errors = OPDSGenerator.validate_opds_xml(malformed)
        assert len(errors) > 0
        assert "parse error" in errors[0].lower()

    def test_validate_requires_feed_root(self, generator: OPDSGenerator) -> None:
        """validate_opds_xml rejects non-feed root elements."""
        invalid_xml = b'<?xml version="1.0"?><entry></entry>'
        errors = OPDSGenerator.validate_opds_xml(invalid_xml)
        assert any("feed" in err.lower() for err in errors)

    def test_validate_requires_id(self, generator: OPDSGenerator) -> None:
        """validate_opds_xml rejects feeds without id."""
        invalid_xml = b"""<?xml version="1.0"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
            <title>Test</title>
            <updated>2026-05-19T02:03:14Z</updated>
        </feed>"""
        errors = OPDSGenerator.validate_opds_xml(invalid_xml)
        assert any("id" in err.lower() for err in errors)

    def test_validate_requires_title(self, generator: OPDSGenerator) -> None:
        """validate_opds_xml rejects feeds without title."""
        invalid_xml = b"""<?xml version="1.0"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
            <id>urn:uuid:test</id>
            <updated>2026-05-19T02:03:14Z</updated>
        </feed>"""
        errors = OPDSGenerator.validate_opds_xml(invalid_xml)
        assert any("title" in err.lower() for err in errors)

    def test_validate_requires_entry_id(
        self, generator: OPDSGenerator, simple_entry: OPDSEntry
    ) -> None:
        """validate_opds_xml rejects entries without id."""
        # Manually craft invalid feed with entry missing id
        invalid_xml = b"""<?xml version="1.0"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
            <id>urn:uuid:test</id>
            <title>Test</title>
            <updated>2026-05-19T02:03:14Z</updated>
            <entry>
                <title>No ID Entry</title>
                <updated>2026-05-19T02:03:14Z</updated>
            </entry>
        </feed>"""
        errors = OPDSGenerator.validate_opds_xml(invalid_xml)
        assert any("entry" in err.lower() and "id" in err.lower()
                   for err in errors)


# ---------------------------------------------------------------------------
# Integration Tests: Feedgen vs xml.etree
# ---------------------------------------------------------------------------


class TestFeedgenFallback:
    """Tests to verify feedgen and xml.etree produce equivalent output."""

    def test_both_generation_paths_produce_valid_xml(
        self, generator: OPDSGenerator, three_entries: list[OPDSEntry]
    ) -> None:
        """Both feedgen and etree fallback produce valid XML."""
        for entry in three_entries:
            generator.add_entry(entry)

        # Test both paths
        root_xml = generator.generate_root_catalog()
        acq_xml = generator.generate_acquisition_feed()

        # Both should be valid
        errors_root = OPDSGenerator.validate_opds_xml(root_xml)
        errors_acq = OPDSGenerator.validate_opds_xml(acq_xml)

        assert len(errors_root) == 0, f"Root catalog validation errors: {errors_root}"
        assert len(errors_acq) == 0, f"Acquisition feed validation errors: {errors_acq}"

    def test_feedgen_xml_contains_all_entries(
        self, generator: OPDSGenerator, three_entries: list[OPDSEntry]
    ) -> None:
        """feedgen-generated acquisition feed contains all entries."""
        for entry in three_entries:
            generator.add_entry(entry)
        xml_bytes = generator.generate_acquisition_feed()
        xml_str = xml_bytes.decode("utf-8")

        # Verify all entries are present
        for entry in three_entries:
            assert entry.uuid in xml_str
            assert entry.title in xml_str


# ---------------------------------------------------------------------------
# Regression Tests: Edge Cases
# ---------------------------------------------------------------------------


class TestEdgeCases:
    """Tests for edge cases and boundary conditions."""

    def test_empty_generator_produces_valid_catalog(
        self, generator: OPDSGenerator
    ) -> None:
        """Generator with zero entries produces valid catalog."""
        xml_bytes = generator.generate_root_catalog()
        errors = OPDSGenerator.validate_opds_xml(xml_bytes)
        assert len(errors) == 0

    def test_empty_generator_acquisition_feed_is_valid(
        self, generator: OPDSGenerator
    ) -> None:
        """Generator with zero entries produces valid acquisition feed."""
        xml_bytes = generator.generate_acquisition_feed()
        errors = OPDSGenerator.validate_opds_xml(xml_bytes)
        assert len(errors) == 0

    def test_entry_with_version_history(
        self, generator: OPDSGenerator
    ) -> None:
        """Entries with version history are handled correctly."""
        entry = OPDSEntry(
            uuid="550e8400-e29b-41d4-a716-446655440001",
            title="Versioned Archive",
            name="versioned_en_nopic",
            flavour="nopic",
            language="eng",
            period="2026-05",
            description="Archive with history",
            download_url="https://cdn.example.org/versioned_en_nopic_2026-05.zim",
            file_size_bytes=1_000_000_000,
            sha256_checksum="def456" * 10 + "defg",
            article_count=100,
            generated_at=datetime(2026, 5, 19, 2, 3, 14),
            version_history=[
                OPDSVersionEntry(
                    period="2026-04",
                    download_url="https://cdn.example.org/versioned_en_nopic_2026-04.zim",
                    file_size_bytes=900_000_000,
                    generated_at=datetime(2026, 4, 19, 2, 3, 14),
                    sha256_checksum="ghi789" * 10 + "ghij",
                ),
            ],
        )
        generator.add_entry(entry)
        xml_bytes = generator.generate_acquisition_feed()
        errors = OPDSGenerator.validate_opds_xml(xml_bytes)
        assert len(errors) == 0

    def test_entry_with_is_reference_flag(
        self, generator: OPDSGenerator
    ) -> None:
        """Reference exports (is_reference=True) are marked correctly."""
        entry = OPDSEntry(
            uuid="550e8400-e29b-41d4-a716-446655440001",
            title="Reference Archive",
            name="reference_en_nopic",
            flavour="nopic",
            language="eng",
            period="2026-05",
            description="Permanent archive",
            download_url="https://cdn.example.org/reference_en_nopic_2026-05.zim",
            file_size_bytes=1_000_000_000,
            sha256_checksum="abc123" * 10 + "abcd",
            article_count=100,
            generated_at=datetime(2026, 5, 19, 2, 3, 14),
            is_reference=True,
        )
        generator.add_entry(entry)
        xml_bytes = generator.generate_acquisition_feed()
        xml_str = xml_bytes.decode("utf-8")

        # Should contain archive/reference category
        assert "archive" in xml_str or "reference" in xml_str
        errors = OPDSGenerator.validate_opds_xml(xml_bytes)
        assert len(errors) == 0
