"""
Tests for OPDS generator (OPDSEntry, OPDSVersionEntry, OPDSGenerator).

These tests verify OPDS 1.2 catalog generation, feedgen integration, and
XML validation for Kiwix compatibility.
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from datetime import datetime
from unittest.mock import Mock

import pytest

from app.services.export.opds_generator import (
    OPDSEntry,
    OPDSVersionEntry,
    OPDSGenerator,
    MIME_OPDS_NAV,
    MIME_OPDS_ACQ,
    MIME_ZIM,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def sample_opds_entry() -> OPDSEntry:
    """Create a sample OPDSEntry for testing."""
    return OPDSEntry(
        uuid="550e8400-e29b-41d4-a716-446655440000",
        title="Open-Repo: Full Library (English)",
        name="open-repo_en_nopic",
        flavour="nopic",
        language="eng",
        period="2026-05",
        description="Full open-repo knowledge base without images",
        download_url="https://cdn.example.org/open-repo_en_nopic_2026-05.zim",
        file_size_bytes=2147483648,  # 2 GB
        sha256_checksum="abc123def456abc123def456abc123def456abc123def456abc123def456abc1",
        article_count=12345,
        generated_at=datetime(2026, 5, 1, 2, 3, 14),
        illustration_url="https://cdn.example.org/open-repo-logo.png",
        is_reference=False,
        version_history=[],
    )


@pytest.fixture
def sample_version_entry() -> OPDSVersionEntry:
    """Create a sample OPDSVersionEntry for testing."""
    return OPDSVersionEntry(
        period="2026-04",
        download_url="https://cdn.example.org/open-repo_en_nopic_2026-04.zim",
        file_size_bytes=2097152000,
        generated_at=datetime(2026, 4, 1, 2, 3, 14),
        sha256_checksum="def456abc123def456abc123def456abc123def456abc123def456abc123def456",
    )


@pytest.fixture
def sample_generator() -> OPDSGenerator:
    """Create a sample OPDSGenerator instance."""
    return OPDSGenerator(
        node_uuid="550e8400-e29b-41d4-a716-446655440000",
        node_name="Open-Repo Node",
        node_url="https://node.example.org",
        catalog_url="https://node.example.org/opds/v2/root.xml",
    )


# ---------------------------------------------------------------------------
# OPDSEntry Tests
# ---------------------------------------------------------------------------


class TestOPDSEntry:
    """Tests for OPDSEntry dataclass."""

    def test_opds_entry_valid_creation(self, sample_opds_entry: OPDSEntry) -> None:
        """Valid OPDSEntry creation with all required fields."""
        assert sample_opds_entry.uuid == "550e8400-e29b-41d4-a716-446655440000"
        assert sample_opds_entry.title == "Open-Repo: Full Library (English)"
        assert sample_opds_entry.language == "eng"

    def test_opds_entry_invalid_uuid(self) -> None:
        """Invalid UUID raises ValueError."""
        with pytest.raises(ValueError, match="is not a valid UUID"):
            OPDSEntry(
                uuid="invalid-uuid",
                title="Test",
                name="test_en_nopic",
                flavour="nopic",
                language="eng",
                period="2026-05",
                description="Test",
                download_url="https://cdn.example.org/test.zim",
                file_size_bytes=1000,
                sha256_checksum="abc123",
                article_count=100,
                generated_at=datetime.now(),
            )

    def test_opds_entry_invalid_name(self, sample_opds_entry: OPDSEntry) -> None:
        """Invalid name format raises ValueError."""
        with pytest.raises(ValueError, match="does not match openZIM naming convention"):
            OPDSEntry(
                uuid=sample_opds_entry.uuid,
                title="Test",
                name="invalid_name",  # Missing language and flavour
                flavour=sample_opds_entry.flavour,
                language=sample_opds_entry.language,
                period=sample_opds_entry.period,
                description="Test",
                download_url=sample_opds_entry.download_url,
                file_size_bytes=sample_opds_entry.file_size_bytes,
                sha256_checksum=sample_opds_entry.sha256_checksum,
                article_count=sample_opds_entry.article_count,
                generated_at=sample_opds_entry.generated_at,
            )

    def test_opds_entry_invalid_period(self, sample_opds_entry: OPDSEntry) -> None:
        """Invalid period format raises ValueError."""
        with pytest.raises(ValueError, match="does not match YYYY-MM format"):
            OPDSEntry(
                uuid=sample_opds_entry.uuid,
                title="Test",
                name=sample_opds_entry.name,
                flavour=sample_opds_entry.flavour,
                language=sample_opds_entry.language,
                period="invalid",  # Invalid format
                description="Test",
                download_url=sample_opds_entry.download_url,
                file_size_bytes=sample_opds_entry.file_size_bytes,
                sha256_checksum=sample_opds_entry.sha256_checksum,
                article_count=sample_opds_entry.article_count,
                generated_at=sample_opds_entry.generated_at,
            )

    def test_opds_entry_description_too_long(self, sample_opds_entry: OPDSEntry) -> None:
        """Description exceeding 80 characters raises ValueError."""
        with pytest.raises(ValueError, match="exceeds 80 characters"):
            OPDSEntry(
                uuid=sample_opds_entry.uuid,
                title="Test",
                name=sample_opds_entry.name,
                flavour=sample_opds_entry.flavour,
                language=sample_opds_entry.language,
                period=sample_opds_entry.period,
                description="x" * 81,  # 81 characters
                download_url=sample_opds_entry.download_url,
                file_size_bytes=sample_opds_entry.file_size_bytes,
                sha256_checksum=sample_opds_entry.sha256_checksum,
                article_count=sample_opds_entry.article_count,
                generated_at=sample_opds_entry.generated_at,
            )

    def test_opds_entry_from_dict(self, sample_opds_entry: OPDSEntry) -> None:
        """Create OPDSEntry from dictionary."""
        data = {
            "uuid": sample_opds_entry.uuid,
            "title": sample_opds_entry.title,
            "name": sample_opds_entry.name,
            "flavour": sample_opds_entry.flavour,
            "language": sample_opds_entry.language,
            "period": sample_opds_entry.period,
            "description": sample_opds_entry.description,
            "download_url": sample_opds_entry.download_url,
            "file_size_bytes": sample_opds_entry.file_size_bytes,
            "sha256_checksum": sample_opds_entry.sha256_checksum,
            "article_count": sample_opds_entry.article_count,
            "generated_at": sample_opds_entry.generated_at,
        }
        entry = OPDSEntry.from_dict(data)
        assert entry.uuid == sample_opds_entry.uuid
        assert entry.title == sample_opds_entry.title

    def test_opds_entry_from_zim_export(self) -> None:
        """Create OPDSEntry from mocked ZimExport ORM row."""
        mock_export = Mock()
        mock_export.id = 1
        mock_export.zim_uuid = "550e8400-e29b-41d4-a716-446655440000"
        mock_export.title = "Test ZIM"
        mock_export.name = "test_en_nopic"
        mock_export.flavour = "nopic"
        mock_export.language = "eng"
        mock_export.period = "2026-05"
        mock_export.description = "A test ZIM"
        mock_export.cdn_url = "https://cdn.example.org/test.zim"
        mock_export.file_size_bytes = 1000000
        mock_export.sha256 = "abc123"
        mock_export.article_count = 100
        mock_export.is_reference = False
        mock_export.completed_at = datetime(2026, 5, 1, 2, 3, 14)
        mock_export.created_at = datetime(2026, 5, 1, 0, 0, 0)

        entry = OPDSEntry.from_zim_export(mock_export)
        assert entry.uuid == "550e8400-e29b-41d4-a716-446655440000"
        assert entry.title == "Test ZIM"
        assert entry.download_url == "https://cdn.example.org/test.zim"
        assert entry.file_size_bytes == 1000000

    def test_opds_entry_from_zim_export_missing_cdn_url(self) -> None:
        """ZimExport without cdn_url raises ValueError."""
        mock_export = Mock()
        mock_export.id = 1
        mock_export.name = "test_en_nopic"
        mock_export.cdn_url = None

        with pytest.raises(ValueError, match="has no cdn_url"):
            OPDSEntry.from_zim_export(mock_export)

    def test_opds_entry_from_zim_export_missing_sha256(self) -> None:
        """ZimExport without sha256 raises ValueError."""
        mock_export = Mock()
        mock_export.id = 1
        mock_export.cdn_url = "https://cdn.example.org/test.zim"
        mock_export.sha256 = None

        with pytest.raises(ValueError, match="has no sha256 checksum"):
            OPDSEntry.from_zim_export(mock_export)

    def test_opds_entry_filename_property(self, sample_opds_entry: OPDSEntry) -> None:
        """Filename property returns correct format."""
        assert sample_opds_entry.filename == "open-repo_en_nopic_2026-05.zim"

    def test_opds_entry_entry_id_property(self, sample_opds_entry: OPDSEntry) -> None:
        """Entry ID property returns URN format."""
        assert sample_opds_entry.entry_id.startswith("urn:uuid:")
        assert sample_opds_entry.entry_id.endswith(sample_opds_entry.uuid)

    def test_opds_entry_updated_iso_property(self, sample_opds_entry: OPDSEntry) -> None:
        """Updated ISO property returns ISO 8601 format with Z suffix."""
        iso = sample_opds_entry.updated_iso
        assert iso.endswith("Z")
        assert "T" in iso
        assert iso == "2026-05-01T02:03:14Z"

    def test_opds_entry_file_size_human_property(self) -> None:
        """File size human property formats bytes correctly."""
        entry = OPDSEntry(
            uuid="550e8400-e29b-41d4-a716-446655440000",
            title="Test",
            name="test_en_nopic",
            flavour="nopic",
            language="eng",
            period="2026-05",
            description="Test",
            download_url="https://cdn.example.org/test.zim",
            file_size_bytes=42 * 1024 * 1024,  # 42 MB
            sha256_checksum="abc123",
            article_count=100,
            generated_at=datetime.now(),
        )
        assert entry.file_size_human == "42 MB"


# ---------------------------------------------------------------------------
# OPDSGenerator Tests
# ---------------------------------------------------------------------------


class TestOPDSGenerator:
    """Tests for OPDSGenerator class."""

    def test_generator_initialization(self, sample_generator: OPDSGenerator) -> None:
        """OPDSGenerator initializes with correct values."""
        assert sample_generator.node_uuid == "550e8400-e29b-41d4-a716-446655440000"
        assert sample_generator.node_name == "Open-Repo Node"
        assert sample_generator.entry_count() == 0

    def test_generator_invalid_node_uuid(self) -> None:
        """Invalid node UUID raises ValueError."""
        with pytest.raises(ValueError, match="is not a valid UUID"):
            OPDSGenerator(
                node_uuid="invalid-uuid",
                node_name="Test",
                node_url="https://example.org",
                catalog_url="https://example.org/opds/v2/root.xml",
            )

    def test_add_entry(self, sample_generator: OPDSGenerator, sample_opds_entry: OPDSEntry) -> None:
        """Adding entries increases entry count."""
        assert sample_generator.entry_count() == 0
        sample_generator.add_entry(sample_opds_entry)
        assert sample_generator.entry_count() == 1

    def test_get_entry_by_name(
        self, sample_generator: OPDSGenerator, sample_opds_entry: OPDSEntry
    ) -> None:
        """Retrieve entry by ZIM name."""
        sample_generator.add_entry(sample_opds_entry)
        entry = sample_generator.get_entry_by_name("open-repo_en_nopic")
        assert entry is not None
        assert entry.uuid == sample_opds_entry.uuid

    def test_get_entry_by_name_not_found(self, sample_generator: OPDSGenerator) -> None:
        """Non-existent name returns None."""
        entry = sample_generator.get_entry_by_name("nonexistent")
        assert entry is None

    def test_get_entries_sorted(self, sample_generator: OPDSGenerator) -> None:
        """Entries are sorted by name, then period descending."""
        entry1 = OPDSEntry(
            uuid="550e8400-e29b-41d4-a716-446655440001",
            title="Test 1",
            name="alpha_en_nopic",
            flavour="nopic",
            language="eng",
            period="2026-05",
            description="Test 1",
            download_url="https://cdn.example.org/test1.zim",
            file_size_bytes=1000,
            sha256_checksum="abc1",
            article_count=100,
            generated_at=datetime(2026, 5, 1),
        )
        entry2 = OPDSEntry(
            uuid="550e8400-e29b-41d4-a716-446655440002",
            title="Test 2",
            name="alpha_en_nopic",
            flavour="nopic",
            language="eng",
            period="2026-04",
            description="Test 2",
            download_url="https://cdn.example.org/test2.zim",
            file_size_bytes=1000,
            sha256_checksum="abc2",
            article_count=100,
            generated_at=datetime(2026, 4, 1),
        )
        sample_generator.add_entry(entry2)
        sample_generator.add_entry(entry1)

        sorted_entries = sample_generator.get_entries_sorted()
        # Both have same name, so should be sorted by period (2026-05 before 2026-04)
        assert sorted_entries[0].period == "2026-05"
        assert sorted_entries[1].period == "2026-04"

    def test_generate_root_catalog_valid_xml(
        self, sample_generator: OPDSGenerator, sample_opds_entry: OPDSEntry
    ) -> None:
        """Root catalog generates valid XML."""
        sample_generator.add_entry(sample_opds_entry)
        xml_bytes = sample_generator.generate_root_catalog()

        # Parse and validate structure
        root = ET.fromstring(xml_bytes)
        assert root.tag.endswith("feed")

        # Check required elements
        ns = "{http://www.w3.org/2005/Atom}"
        id_elem = root.find(f"{ns}id")
        assert id_elem is not None
        assert id_elem.text.startswith("urn:uuid:")

        title_elem = root.find(f"{ns}title")
        assert title_elem is not None
        assert "Offline Library Catalog" in title_elem.text

    def test_generate_acquisition_feed_valid_xml(
        self, sample_generator: OPDSGenerator, sample_opds_entry: OPDSEntry
    ) -> None:
        """Acquisition feed generates valid XML."""
        sample_generator.add_entry(sample_opds_entry)
        xml_bytes = sample_generator.generate_acquisition_feed()

        # Parse and validate structure
        root = ET.fromstring(xml_bytes)
        assert root.tag.endswith("feed")

        # Check required elements
        ns = "{http://www.w3.org/2005/Atom}"
        entries = root.findall(f"{ns}entry")
        assert len(entries) == 1

        entry = entries[0]
        entry_id = entry.find(f"{ns}id")
        assert entry_id is not None

    def test_generate_single_entry(
        self, sample_generator: OPDSGenerator, sample_opds_entry: OPDSEntry
    ) -> None:
        """Single entry endpoint returns correct entry."""
        sample_generator.add_entry(sample_opds_entry)
        xml_bytes = sample_generator.generate_single_entry(sample_opds_entry.uuid)

        assert xml_bytes is not None
        root = ET.fromstring(xml_bytes)
        assert root.tag.endswith("feed")

    def test_generate_single_entry_not_found(self, sample_generator: OPDSGenerator) -> None:
        """Non-existent entry returns None."""
        xml_bytes = sample_generator.generate_single_entry("550e8400-e29b-41d4-a716-446655440000")
        assert xml_bytes is None

    def test_generate_search_description_valid_xml(self, sample_generator: OPDSGenerator) -> None:
        """Search description generates valid OpenSearch XML."""
        xml_bytes = sample_generator.generate_search_description()

        # Parse and validate
        root = ET.fromstring(xml_bytes)
        assert "OpenSearchDescription" in root.tag

    def test_validate_opds_xml_valid(
        self, sample_generator: OPDSGenerator, sample_opds_entry: OPDSEntry
    ) -> None:
        """validate_opds_xml returns empty list for valid feed."""
        sample_generator.add_entry(sample_opds_entry)
        xml_bytes = sample_generator.generate_root_catalog()

        errors = OPDSGenerator.validate_opds_xml(xml_bytes)
        assert errors == []

    def test_validate_opds_xml_malformed(self) -> None:
        """validate_opds_xml detects malformed XML."""
        xml_bytes = b"<invalid>xml"
        errors = OPDSGenerator.validate_opds_xml(xml_bytes)
        assert len(errors) > 0
        assert any("parse error" in e.lower() for e in errors)

    def test_validate_opds_xml_missing_id(self) -> None:
        """validate_opds_xml detects missing id element."""
        xml_bytes = b'<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom"><title>Test</title></feed>'
        errors = OPDSGenerator.validate_opds_xml(xml_bytes)
        assert any("missing or empty <id>" in e.lower() for e in errors)

    def test_opds_entry_with_version_history(
        self, sample_generator: OPDSGenerator, sample_opds_entry: OPDSEntry,
        sample_version_entry: OPDSVersionEntry
    ) -> None:
        """Entry with version history is properly serialized."""
        sample_opds_entry.version_history = [sample_version_entry]
        sample_generator.add_entry(sample_opds_entry)

        xml_bytes = sample_generator.generate_acquisition_feed()
        root = ET.fromstring(xml_bytes)

        # Find the entry and check for related links (version history)
        ns = "{http://www.w3.org/2005/Atom}"
        entries = root.findall(f"{ns}entry")
        assert len(entries) == 1

        entry = entries[0]
        links = entry.findall(f"{ns}link")
        # Should have: acquisition link, sha256 sidecar, and version history link
        assert len(links) >= 2

    def test_opds_entry_with_illustration(
        self, sample_generator: OPDSGenerator, sample_opds_entry: OPDSEntry
    ) -> None:
        """Entry with illustration generates image links."""
        sample_generator.add_entry(sample_opds_entry)

        xml_bytes = sample_generator.generate_acquisition_feed()
        root = ET.fromstring(xml_bytes)

        # Find image links in the entry
        xml_str = ET.tostring(root, encoding="unicode")
        assert "opds-spec.org/image" in xml_str


# ---------------------------------------------------------------------------
# Integration Tests
# ---------------------------------------------------------------------------


class TestOPDSIntegration:
    """Integration tests for OPDS catalog generation."""

    def test_full_catalog_generation(self) -> None:
        """Full workflow: create generator, add entries, generate feeds."""
        generator = OPDSGenerator(
            node_uuid="550e8400-e29b-41d4-a716-446655440000",
            node_name="Test Node",
            node_url="https://test.example.org",
            catalog_url="https://test.example.org/opds/v2/root.xml",
        )

        # Create multiple entries with different names and periods
        for i in range(3):
            entry = OPDSEntry(
                uuid=f"550e8400-e29b-41d4-a716-44665544000{i}",
                title=f"Test Archive {i}",
                name=f"test{i}_en_nopic",
                flavour="nopic",
                language="eng",
                period="2026-05",
                description=f"Test archive {i}",
                download_url=f"https://cdn.example.org/test{i}.zim",
                file_size_bytes=1000000 + i * 100000,
                sha256_checksum=f"abc{i:03d}",
                article_count=100 + i * 10,
                generated_at=datetime(2026, 5, 1),
            )
            generator.add_entry(entry)

        # Generate all feeds
        root_xml = generator.generate_root_catalog()
        acquisition_xml = generator.generate_acquisition_feed()
        search_xml = generator.generate_search_description()

        # Validate all feeds
        root_errors = OPDSGenerator.validate_opds_xml(root_xml)
        acq_errors = OPDSGenerator.validate_opds_xml(acquisition_xml)

        assert root_errors == [], f"Root catalog errors: {root_errors}"
        assert acq_errors == [], f"Acquisition feed errors: {acq_errors}"
        assert len(search_xml) > 0

        # Check acquisition feed has all entries
        root = ET.fromstring(acquisition_xml)
        ns = "{http://www.w3.org/2005/Atom}"
        entries = root.findall(f"{ns}entry")
        assert len(entries) == 3
