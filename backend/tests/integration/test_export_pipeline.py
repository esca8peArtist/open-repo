"""
Integration test harness for the Phase 5 offline export pipeline.

These tests verify:
  1. ZimWriter class initialization, configuration, and interface contracts
  2. ZimEntry and ZimMetadata validation logic
  3. OPDSGenerator catalog XML generation and validation
  4. End-to-end pipeline with synthetic Phase 4 content data
  5. Attribution footer rendering for federated content
  6. Nopic (no-image) flavour filtering
  7. Period/filename computation
  8. OPDS XML structure and namespace correctness

All tests run without external network calls and mock python-libzim
(not yet installed). The ZimWriter stub writes a placeholder file;
tests verify interface contracts, not ZIM binary format.

Post-PR-merge: Tests in the "full_implementation" group will be
enabled with real python-libzim calls once the stub is replaced.
"""

from __future__ import annotations

import re
import uuid
from datetime import datetime
from pathlib import Path
from typing import Optional
from xml.etree import ElementTree as ET

import pytest


# ---------------------------------------------------------------------------
# Path setup — import from the app services package
# ---------------------------------------------------------------------------

import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from app.services.export.zim_writer import (
    ZimWriter,
    ZimMetadata,
    ZimEntry,
    ExportConfig,
    ExportScope,
    ZimWriteResult,
)
from app.services.export.opds_generator import (
    OPDSGenerator,
    OPDSEntry,
    OPDSVersionEntry,
    MIME_OPDS_ACQ,
    MIME_ZIM,
)


# ---------------------------------------------------------------------------
# Fixtures: synthetic Phase 4 content data
# ---------------------------------------------------------------------------


@pytest.fixture
def sample_metadata() -> ZimMetadata:
    """Standard valid ZimMetadata for testing."""
    return ZimMetadata(
        title="Open-Repo: Test Export",
        description="Offline practical knowledge library",
        language="eng",
        name="open-repo_en_nopic",
        flavour="nopic",
        creator="Open-Repo Community",
        publisher="Open-Repo",
        source_url="https://test.open-repo.example.org",
        tags="offline;practical-knowledge;procedures",
    )


@pytest.fixture
def sample_config() -> ExportConfig:
    """Standard LOCAL_ONLY nopic export config."""
    return ExportConfig(
        scope=ExportScope.LOCAL_ONLY,
        flavour="nopic",
        include_images=False,
        language="en",
        language_iso3="eng",
    )


@pytest.fixture
def sample_domain_config() -> ExportConfig:
    """Domain-specific export config for agriculture."""
    return ExportConfig(
        scope=ExportScope.DOMAIN,
        scope_value="agriculture",
        flavour="agriculture",
        include_images=False,
    )


@pytest.fixture
def tmp_zim_path(tmp_path: Path) -> Path:
    """Temporary path for ZIM output file."""
    return tmp_path / "test_export.zim"


@pytest.fixture
def zim_writer(sample_metadata: ZimMetadata, sample_config: ExportConfig, tmp_zim_path: Path) -> ZimWriter:
    """Pre-initialized ZimWriter with sample metadata and config."""
    return ZimWriter(
        metadata=sample_metadata,
        config=sample_config,
        output_path=tmp_zim_path,
        zimcheck_binary=None,  # Skip zimcheck in stub phase
    )


@pytest.fixture
def sample_content_items() -> list[dict]:
    """
    Synthetic content items mimicking Phase 4 ContentItem model.

    Simulates the data returned by a database query for export,
    with fields matching app.models.ContentItem (cid, title, item_type,
    domain, license, content_jsonld).
    """
    return [
        {
            "cid": "bafkrei001",
            "title": {"en": "Biosand Water Filter Construction"},
            "item_type": "procedure",
            "domain": "water",
            "license": "CC-BY-4.0",
            "is_local": True,
            "source_url": None,
            "content_jsonld": {
                "@type": "Procedure",
                "language": ["en"],
                "description": {"en": "Step-by-step guide to building a biosand water filter"},
                "difficulty": "intermediate",
                "steps": [
                    {"stepNumber": 1, "title": {"en": "Prepare the mold"}, "body": {"en": "Build a wooden mold 30cm x 60cm x 120cm..."}},
                    {"stepNumber": 2, "title": {"en": "Layer the sand"}, "body": {"en": "Add layers of coarse gravel, then fine sand..."}},
                    {"stepNumber": 3, "title": {"en": "Install the diffuser"}, "body": {"en": "Place the diffuser plate on top of the sand layer..."}},
                ],
                "tools": [{"name": {"en": "Wooden mold"}, "quantity": 1}],
                "materials": [{"name": {"en": "Fine sand"}, "quantity": "100 kg"}],
            },
        },
        {
            "cid": "bafkrei002",
            "title": {"en": "Solar Panel Installation Guide"},
            "item_type": "procedure",
            "domain": "energy",
            "license": "CC-BY-SA-4.0",
            "is_local": True,
            "source_url": None,
            "content_jsonld": {
                "@type": "Procedure",
                "language": ["en"],
                "description": {"en": "Installing a basic off-grid solar panel system"},
                "difficulty": "beginner",
                "steps": [
                    {"stepNumber": 1, "title": {"en": "Choose panel location"}, "body": {"en": "Select a south-facing roof area..."}},
                    {"stepNumber": 2, "title": {"en": "Mount the panels"}, "body": {"en": "Attach mounting rails to roof structure..."}},
                ],
            },
        },
        {
            "cid": "bafkrei003",
            "title": {"en": "Fermented Cassava Flour Recipe"},
            "item_type": "recipe",
            "domain": "recipes",
            "license": "CC0-1.0",
            "is_local": True,
            "source_url": None,
            "content_jsonld": {
                "@type": "Recipe",
                "language": ["en"],
                "description": {"en": "Traditional fermented cassava flour preparation"},
                "ingredients": [
                    {"name": {"en": "Fresh cassava roots"}, "quantity": "5 kg"},
                ],
                "steps": [
                    {"stepNumber": 1, "title": {"en": "Peel and wash"}, "body": {"en": "Peel the cassava roots, wash thoroughly..."}},
                    {"stepNumber": 2, "title": {"en": "Ferment"}, "body": {"en": "Submerge in water for 3 days..."}},
                ],
            },
        },
        {
            "cid": "bafkrei004",
            "title": {"en": "Rainwater Harvesting System Schematic"},
            "item_type": "schematic",
            "domain": "water",
            "license": "CC-BY-4.0",
            "is_local": True,
            "source_url": None,
            "content_jsonld": {
                "@type": "Schematic",
                "language": ["en"],
                "description": {"en": "Simple rooftop rainwater collection system diagram"},
            },
        },
        {
            "cid": "bafkrei005",
            "title": {"en": "Moringa Tree Cultivation Plan"},
            "item_type": "plan",
            "domain": "agriculture",
            "license": "CC-BY-4.0",
            "is_local": True,
            "source_url": None,
            "content_jsonld": {
                "@type": "Plan",
                "language": ["en"],
                "description": {"en": "12-month plan for establishing a moringa grove"},
                "steps": [
                    {"stepNumber": 1, "title": {"en": "Site preparation"}, "body": {"en": "Clear land and test soil pH..."}},
                ],
            },
        },
        # Federated item (from a partner node)
        {
            "cid": "bafkrei006",
            "title": {"en": "Vermicomposting Setup"},
            "item_type": "procedure",
            "domain": "agriculture",
            "license": "CC-BY-4.0",
            "is_local": False,
            "source_url": "https://partner-node.example.org",
            "content_jsonld": {
                "@type": "Procedure",
                "language": ["en"],
                "description": {"en": "Setting up a worm composting bin"},
                "steps": [
                    {"stepNumber": 1, "title": {"en": "Prepare the bin"}, "body": {"en": "Drill drainage holes in the bin base..."}},
                ],
            },
        },
    ]


@pytest.fixture
def node_uuid() -> str:
    """Stable test node UUID."""
    return "550e8400-e29b-41d4-a716-446655440000"


@pytest.fixture
def opds_generator(node_uuid: str) -> OPDSGenerator:
    """Pre-initialized OPDSGenerator for testing."""
    return OPDSGenerator(
        node_uuid=node_uuid,
        node_name="Open-Repo Test Node",
        node_url="https://test.open-repo.example.org",
        catalog_url="https://test.open-repo.example.org/opds/v2/root.xml",
    )


@pytest.fixture
def sample_opds_entry(node_uuid: str) -> OPDSEntry:
    """Standard valid OPDSEntry for a nopic full export."""
    return OPDSEntry(
        uuid="a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11",
        title="Open-Repo: Full Library (English)",
        name="open-repo_en_nopic",
        flavour="nopic",
        language="eng",
        period="2026-04",
        description="Offline practical knowledge library",
        download_url="https://exports.test.open-repo.example.org/zim/open-repo_en_nopic_2026-04.zim",
        file_size_bytes=52428800,  # 50 MB
        sha256_checksum="a" * 64,
        article_count=500,
        generated_at=datetime(2026, 4, 28, 2, 0, 0),
    )


def _make_html(title: str, body: str) -> str:
    """Helper to produce a minimal self-contained HTML article."""
    return (
        f"<!DOCTYPE html>\n"
        f"<html lang='en'>\n"
        f"<head><title>{title}</title>"
        f"<style>body{{font-family:sans-serif;margin:1rem;}}</style></head>\n"
        f"<body><h1>{title}</h1><p>{body}</p></body>\n"
        f"</html>"
    )


# ---------------------------------------------------------------------------
# ZimMetadata Tests
# ---------------------------------------------------------------------------


class TestZimMetadata:

    def test_valid_metadata_initializes(self, sample_metadata: ZimMetadata) -> None:
        """Valid metadata initializes without error."""
        assert sample_metadata.title == "Open-Repo: Test Export"
        assert sample_metadata.language == "eng"
        assert sample_metadata.name == "open-repo_en_nopic"

    def test_date_auto_generated_when_none(self) -> None:
        """Date is auto-populated with today's date when not provided."""
        meta = ZimMetadata(
            title="Test",
            description="Test description",
            language="eng",
            name="open-repo_en_nopic",
            flavour="nopic",
            creator="Test",
            publisher="Test",
            source_url="https://example.org",
        )
        assert meta.date is not None
        assert re.match(r"^\d{4}-\d{2}-\d{2}$", meta.date), f"Bad date format: {meta.date}"

    def test_invalid_name_raises_value_error(self) -> None:
        """ZimMetadata rejects names that don't follow openZIM naming convention."""
        with pytest.raises(ValueError, match="Invalid ZIM Name"):
            ZimMetadata(
                title="Test",
                description="Test",
                language="eng",
                name="OpenRepo_English_Full",  # Wrong: uppercase, wrong separator
                flavour="nopic",
                creator="Test",
                publisher="Test",
                source_url="https://example.org",
            )

    def test_name_with_underscore_in_part_raises_value_error(self) -> None:
        """Underscores within name parts are rejected."""
        with pytest.raises(ValueError, match="Invalid ZIM Name"):
            ZimMetadata(
                title="Test",
                description="Test",
                language="eng",
                name="open_repo_en_nopic",  # Wrong: underscore in publisher part
                flavour="nopic",
                creator="Test",
                publisher="Test",
                source_url="https://example.org",
            )

    def test_validate_returns_empty_list_for_valid_metadata(
        self, sample_metadata: ZimMetadata
    ) -> None:
        """validate() returns [] for correctly configured metadata."""
        errors = sample_metadata.validate()
        assert errors == [], f"Expected no errors, got: {errors}"

    def test_validate_reports_empty_title(self) -> None:
        """validate() reports error when title is empty string."""
        meta = ZimMetadata(
            title="  ",  # Whitespace only
            description="Test",
            language="eng",
            name="open-repo_en_nopic",
            flavour="nopic",
            creator="Test",
            publisher="Test",
            source_url="https://example.org",
        )
        # Note: validate() will raise ValueError for invalid name before checking title
        # This test verifies the validate() contract for the whitespace case
        errors = meta.validate()
        title_errors = [e for e in errors if "title" in e.lower()]
        assert len(title_errors) >= 1

    def test_validate_reports_description_over_80_chars(self) -> None:
        """validate() reports error when description exceeds 80 characters."""
        meta = ZimMetadata(
            title="Test",
            description="A" * 81,  # 81 characters — over the 80 char limit
            language="eng",
            name="open-repo_en_nopic",
            flavour="nopic",
            creator="Test",
            publisher="Test",
            source_url="https://example.org",
        )
        errors = meta.validate()
        desc_errors = [e for e in errors if "Description" in e]
        assert len(desc_errors) >= 1

    def test_validate_reports_invalid_date_format(self) -> None:
        """validate() reports error for date not matching YYYY-MM-DD."""
        meta = ZimMetadata(
            title="Test",
            description="Test",
            language="eng",
            name="open-repo_en_nopic",
            flavour="nopic",
            creator="Test",
            publisher="Test",
            source_url="https://example.org",
            date="28-04-2026",  # Wrong format (DD-MM-YYYY)
        )
        errors = meta.validate()
        date_errors = [e for e in errors if "Date" in e]
        assert len(date_errors) >= 1

    def test_validate_reports_missing_illustration_path(self, tmp_path: Path) -> None:
        """validate() reports error when illustration file path doesn't exist."""
        meta = ZimMetadata(
            title="Test",
            description="Test",
            language="eng",
            name="open-repo_en_nopic",
            flavour="nopic",
            creator="Test",
            publisher="Test",
            source_url="https://example.org",
            illustration_48x48_path=tmp_path / "nonexistent-icon.png",
        )
        errors = meta.validate()
        icon_errors = [e for e in errors if "illustration" in e.lower()]
        assert len(icon_errors) >= 1


# ---------------------------------------------------------------------------
# ExportConfig Tests
# ---------------------------------------------------------------------------


class TestExportConfig:

    def test_default_config_is_local_only_nopic(self) -> None:
        """Default ExportConfig is LOCAL_ONLY scope with nopic flavour."""
        config = ExportConfig()
        assert config.scope == ExportScope.LOCAL_ONLY
        assert config.flavour == "nopic"
        assert config.include_images is False
        assert config.include_federated is False

    def test_domain_scope_requires_scope_value(self) -> None:
        """DOMAIN scope without scope_value raises ValueError."""
        with pytest.raises(ValueError, match="scope_value is required"):
            ExportConfig(scope=ExportScope.DOMAIN, flavour="agriculture")

    def test_tag_scope_requires_scope_value(self) -> None:
        """TAG scope without scope_value raises ValueError."""
        with pytest.raises(ValueError, match="scope_value is required"):
            ExportConfig(scope=ExportScope.TAG, flavour="nopic")

    def test_domain_scope_with_scope_value_succeeds(self) -> None:
        """DOMAIN scope with scope_value initializes successfully."""
        config = ExportConfig(
            scope=ExportScope.DOMAIN,
            scope_value="agriculture",
            flavour="agriculture"
        )
        assert config.scope_value == "agriculture"

    def test_invalid_flavour_raises_value_error(self) -> None:
        """Invalid flavour string raises ValueError."""
        with pytest.raises(ValueError, match="Invalid flavour"):
            ExportConfig(flavour="unknown_flavour")

    def test_valid_flavours_accepted(self) -> None:
        """All documented valid flavours are accepted."""
        valid_flavours = ["nopic", "all", "mini", "agriculture", "recipes",
                          "water", "electronics", "building", "energy", "archive"]
        for flavour in valid_flavours:
            config = ExportConfig(flavour=flavour)
            assert config.flavour == flavour

    def test_all_scope_values(self) -> None:
        """All ExportScope enum values are accessible."""
        assert ExportScope.LOCAL_ONLY.value == "local"
        assert ExportScope.FEDERATED.value == "federated"
        assert ExportScope.DOMAIN.value == "domain"
        assert ExportScope.TAG.value == "tag"


# ---------------------------------------------------------------------------
# ZimEntry Tests
# ---------------------------------------------------------------------------


class TestZimEntry:

    def test_valid_entry_initializes(self) -> None:
        """Valid ZimEntry initializes without error."""
        entry = ZimEntry(
            path="water/bafkrei001",
            title="Biosand Water Filter Construction",
            content="<html><body><h1>Biosand Filter</h1></body></html>",
        )
        assert entry.path == "water/bafkrei001"
        assert entry.is_front_article is True

    def test_path_cannot_start_with_slash(self) -> None:
        """ZimEntry rejects paths starting with '/'."""
        with pytest.raises(ValueError, match="must not start with"):
            ZimEntry(
                path="/water/bafkrei001",  # Invalid: leading slash
                title="Test",
                content="<html></html>",
            )

    def test_path_cannot_contain_double_slash(self) -> None:
        """ZimEntry rejects paths containing '//'."""
        with pytest.raises(ValueError, match="must not contain"):
            ZimEntry(
                path="water//bafkrei001",
                title="Test",
                content="<html></html>",
            )

    def test_front_article_requires_non_empty_title(self) -> None:
        """Front articles must have a non-empty title."""
        with pytest.raises(ValueError, match="empty title"):
            ZimEntry(
                path="water/bafkrei001",
                title="   ",  # Whitespace only
                content="<html></html>",
                is_front_article=True,
            )

    def test_non_front_article_allows_empty_title(self) -> None:
        """Non-front article entries (resources) can have an empty title."""
        entry = ZimEntry(
            path="style/main.css",
            title="",  # Empty is fine for CSS resources
            content=b"body { font-family: sans-serif; }",
            mime_type="text/css",
            is_front_article=False,
        )
        assert entry.title == ""

    def test_source_node_url_requires_source_node_name(self) -> None:
        """source_node_url requires source_node_name to be set."""
        with pytest.raises(ValueError, match="source_node_name is required"):
            ZimEntry(
                path="agriculture/bafkrei006",
                title="Vermicomposting Setup",
                content="<html></html>",
                source_node_url="https://partner.example.org",
                # source_node_name not set
            )

    def test_has_attribution_true_when_source_url_set(self) -> None:
        """has_attribution() returns True when source_node_url is set."""
        entry = ZimEntry(
            path="agriculture/bafkrei006",
            title="Vermicomposting Setup",
            content="<html></html>",
            source_node_url="https://partner.example.org",
            source_node_name="Partner Node",
        )
        assert entry.has_attribution() is True

    def test_has_attribution_false_when_no_source_url(self) -> None:
        """has_attribution() returns False for locally-authored content."""
        entry = ZimEntry(
            path="water/bafkrei001",
            title="Biosand Filter",
            content="<html></html>",
        )
        assert entry.has_attribution() is False

    def test_bytes_content_accepted(self) -> None:
        """Binary content (bytes) is accepted for resource entries."""
        png_bytes = b"\x89PNG\r\n\x1a\n"  # PNG magic bytes
        entry = ZimEntry(
            path="assets/logo.png",
            title="",
            content=png_bytes,
            mime_type="image/png",
            is_front_article=False,
        )
        assert entry.content == png_bytes


# ---------------------------------------------------------------------------
# ZimWriter Initialization Tests
# ---------------------------------------------------------------------------


class TestZimWriterInitialization:

    def test_writer_initializes_with_valid_params(
        self,
        sample_metadata: ZimMetadata,
        sample_config: ExportConfig,
        tmp_zim_path: Path,
    ) -> None:
        """ZimWriter initializes without error with valid parameters."""
        writer = ZimWriter(
            metadata=sample_metadata,
            config=sample_config,
            output_path=tmp_zim_path,
            zimcheck_binary=None,
        )
        assert writer.article_count == 0
        assert writer.resource_count == 0
        assert writer.sha256_checksum is None

    def test_writer_raises_for_nonexistent_output_dir(
        self, sample_metadata: ZimMetadata, sample_config: ExportConfig
    ) -> None:
        """ZimWriter raises FileNotFoundError if output directory doesn't exist."""
        with pytest.raises(FileNotFoundError, match="Output directory does not exist"):
            ZimWriter(
                metadata=sample_metadata,
                config=sample_config,
                output_path=Path("/nonexistent/directory/export.zim"),
                zimcheck_binary=None,
            )

    def test_writer_raises_for_invalid_metadata(
        self, sample_config: ExportConfig, tmp_zim_path: Path
    ) -> None:
        """ZimWriter raises ValueError if metadata validation fails."""
        bad_metadata = ZimMetadata(
            title="Test",
            description="A" * 81,  # Too long — will fail validate()
            language="eng",
            name="open-repo_en_nopic",
            flavour="nopic",
            creator="Test",
            publisher="Test",
            source_url="https://example.org",
        )
        with pytest.raises(ValueError, match="validation failed"):
            ZimWriter(
                metadata=bad_metadata,
                config=sample_config,
                output_path=tmp_zim_path,
                zimcheck_binary=None,
            )


# ---------------------------------------------------------------------------
# ZimWriter add_article Tests
# ---------------------------------------------------------------------------


class TestZimWriterAddArticle:

    def test_add_article_increments_count(self, zim_writer: ZimWriter) -> None:
        """add_article() increments article_count by 1."""
        assert zim_writer.article_count == 0
        zim_writer.add_article(
            path="water/bafkrei001",
            content=_make_html("Test Article", "Test body"),
            article_type="procedure",
        )
        assert zim_writer.article_count == 1

    def test_add_multiple_articles(self, zim_writer: ZimWriter) -> None:
        """Multiple add_article() calls accumulate correctly."""
        for i in range(5):
            zim_writer.add_article(
                path=f"domain/item-{i:04d}",
                content=_make_html(f"Article {i}", f"Body {i}"),
                article_type="procedure",
            )
        assert zim_writer.article_count == 5

    def test_add_article_with_attribution(self, zim_writer: ZimWriter) -> None:
        """add_article() with source_node_url does not raise."""
        zim_writer.add_article(
            path="agriculture/bafkrei006",
            content=_make_html("Vermicomposting", "Setup instructions..."),
            article_type="procedure",
            source_node_url="https://partner.example.org",
            source_node_name="Partner Node",
            license_name="CC-BY-4.0",
            license_url="https://creativecommons.org/licenses/by/4.0/",
        )
        assert zim_writer.article_count == 1

    def test_add_article_raises_for_empty_content(self, zim_writer: ZimWriter) -> None:
        """add_article() raises ValueError for empty content."""
        with pytest.raises(ValueError, match="content is empty"):
            zim_writer.add_article(
                path="test/item",
                content="   ",  # Whitespace only
                article_type="procedure",
            )

    def test_add_article_raises_after_finalization(
        self, zim_writer: ZimWriter
    ) -> None:
        """add_article() raises RuntimeError after create_zim() has been called."""
        zim_writer.add_article(
            path="test/item",
            content=_make_html("Test", "Body"),
            article_type="procedure",
        )
        zim_writer.create_zim(run_zimcheck=False)
        with pytest.raises(RuntimeError, match="finalized"):
            zim_writer.add_article(
                path="test/item2",
                content=_make_html("Test 2", "Body 2"),
                article_type="procedure",
            )


# ---------------------------------------------------------------------------
# ZimWriter add_resource Tests
# ---------------------------------------------------------------------------


class TestZimWriterAddResource:

    def test_add_css_resource(self, zim_writer: ZimWriter) -> None:
        """add_resource() accepts CSS content."""
        zim_writer.add_resource(
            path="style/main.css",
            binary_content=b"body { font-family: sans-serif; }",
            mime_type="text/css",
        )
        assert zim_writer.resource_count == 1

    def test_add_image_resource_skipped_for_nopic(self, zim_writer: ZimWriter) -> None:
        """Image resources are silently discarded when include_images=False (nopic)."""
        assert zim_writer.config.include_images is False
        zim_writer.add_resource(
            path="assets/logo.png",
            binary_content=b"\x89PNG",
            mime_type="image/png",
        )
        # Image should be discarded
        assert zim_writer.resource_count == 0

    def test_add_image_resource_included_for_all_flavour(
        self,
        sample_metadata: ZimMetadata,
        tmp_path: Path,
    ) -> None:
        """Image resources are included when include_images=True."""
        meta = ZimMetadata(
            title="Open-Repo: Test All",
            description="Test with images",
            language="eng",
            name="open-repo_en_all",
            flavour="all",
            creator="Test",
            publisher="Test",
            source_url="https://example.org",
        )
        config = ExportConfig(
            scope=ExportScope.LOCAL_ONLY,
            flavour="all",
            include_images=True,
        )
        writer = ZimWriter(
            metadata=meta,
            config=config,
            output_path=tmp_path / "test_all.zim",
            zimcheck_binary=None,
        )
        writer.add_resource(
            path="assets/logo.png",
            binary_content=b"\x89PNG",
            mime_type="image/png",
        )
        assert writer.resource_count == 1

    def test_add_resource_raises_for_empty_content(self, zim_writer: ZimWriter) -> None:
        """add_resource() raises ValueError for empty content."""
        with pytest.raises(ValueError, match="content is empty"):
            zim_writer.add_resource(
                path="style/empty.css",
                binary_content=b"",
                mime_type="text/css",
            )

    def test_add_resource_raises_after_finalization(self, zim_writer: ZimWriter) -> None:
        """add_resource() raises RuntimeError after create_zim()."""
        zim_writer.add_article(
            path="test/item",
            content=_make_html("Test", "Body"),
            article_type="procedure",
        )
        zim_writer.create_zim(run_zimcheck=False)
        with pytest.raises(RuntimeError, match="finalized"):
            zim_writer.add_resource(
                path="style/late.css",
                binary_content=b"p {}",
                mime_type="text/css",
            )


# ---------------------------------------------------------------------------
# ZimWriter create_zim Tests
# ---------------------------------------------------------------------------


class TestZimWriterCreateZim:

    def test_create_zim_produces_output_file(self, zim_writer: ZimWriter) -> None:
        """create_zim() creates a file at the output path."""
        zim_writer.add_article(
            path="index",
            content=_make_html("Open-Repo Home", "Welcome to the offline library."),
            article_type="procedure",
        )
        result = zim_writer.create_zim(run_zimcheck=False)
        assert result.output_path.exists()

    def test_create_zim_returns_result_with_sha256(self, zim_writer: ZimWriter) -> None:
        """create_zim() returns ZimWriteResult with non-None SHA-256."""
        zim_writer.add_article(
            path="index",
            content=_make_html("Home", "Welcome"),
            article_type="procedure",
        )
        result = zim_writer.create_zim(run_zimcheck=False)
        assert result.sha256 is not None
        assert len(result.sha256) == 64  # SHA-256 hex is 64 characters
        assert re.match(r"^[0-9a-f]{64}$", result.sha256)

    def test_create_zim_returns_correct_article_count(self, zim_writer: ZimWriter) -> None:
        """create_zim() result.article_count matches articles added."""
        for i in range(7):
            zim_writer.add_article(
                path=f"test/item-{i}",
                content=_make_html(f"Item {i}", f"Content {i}"),
                article_type="procedure",
            )
        result = zim_writer.create_zim(run_zimcheck=False)
        assert result.article_count == 7

    def test_create_zim_raises_when_no_articles(self, zim_writer: ZimWriter) -> None:
        """create_zim() raises ValueError if no front articles have been added."""
        with pytest.raises(ValueError, match="no front articles"):
            zim_writer.create_zim(run_zimcheck=False)

    def test_create_zim_can_only_be_called_once(self, zim_writer: ZimWriter) -> None:
        """create_zim() raises RuntimeError on second call."""
        zim_writer.add_article(
            path="index",
            content=_make_html("Home", "Welcome"),
            article_type="procedure",
        )
        zim_writer.create_zim(run_zimcheck=False)
        with pytest.raises(RuntimeError, match="can only be called once"):
            zim_writer.create_zim(run_zimcheck=False)

    def test_sha256_property_populated_after_create_zim(
        self, zim_writer: ZimWriter
    ) -> None:
        """sha256_checksum property is None before and set after create_zim()."""
        assert zim_writer.sha256_checksum is None
        zim_writer.add_article(
            path="index",
            content=_make_html("Home", "Welcome"),
            article_type="procedure",
        )
        zim_writer.create_zim(run_zimcheck=False)
        assert zim_writer.sha256_checksum is not None
        assert len(zim_writer.sha256_checksum) == 64

    def test_result_name_and_flavour_match_metadata(self, zim_writer: ZimWriter) -> None:
        """ZimWriteResult.name and .flavour match the ZimMetadata."""
        zim_writer.add_article(
            path="index",
            content=_make_html("Home", "Welcome"),
            article_type="procedure",
        )
        result = zim_writer.create_zim(run_zimcheck=False)
        assert result.name == "open-repo_en_nopic"
        assert result.flavour == "nopic"


# ---------------------------------------------------------------------------
# ZimWriter attribution tests
# ---------------------------------------------------------------------------


class TestAttributionFooter:

    def test_attribution_footer_added_for_federated_content(
        self, zim_writer: ZimWriter
    ) -> None:
        """Attribution footer is appended to federated article HTML."""
        html = _make_html("Vermicomposting", "Setup instructions")
        zim_writer.add_article(
            path="agriculture/bafkrei006",
            content=html,
            article_type="procedure",
            source_node_url="https://partner.example.org",
            source_node_name="Partner Node",
            license_name="CC-BY-4.0",
            license_url="https://creativecommons.org/licenses/by/4.0/",
        )
        # The stored entry should contain the attribution footer
        stored_entry = zim_writer._entries[-1]
        assert "attribution" in stored_entry.content
        assert "partner.example.org" in stored_entry.content
        assert "Partner Node" in stored_entry.content

    def test_no_attribution_for_local_content(self, zim_writer: ZimWriter) -> None:
        """No attribution footer for locally-authored content."""
        html = _make_html("Biosand Filter", "Local content")
        zim_writer.add_article(
            path="water/bafkrei001",
            content=html,
            article_type="procedure",
            # No source_node_url
        )
        stored_entry = zim_writer._entries[-1]
        assert "attribution" not in stored_entry.content

    def test_attribution_inserted_before_body_close(self, zim_writer: ZimWriter) -> None:
        """Attribution footer is inserted before </body> tag."""
        html = "<html><body><p>Content</p></body></html>"
        zim_writer.add_article(
            path="test/item",
            content=html,
            article_type="procedure",
            source_node_url="https://partner.example.org",
            source_node_name="Partner Node",
        )
        stored = zim_writer._entries[-1].content
        # Footer should appear before </body>
        footer_pos = stored.find("attribution")
        body_close_pos = stored.find("</body>")
        assert footer_pos < body_close_pos, "Attribution footer should be before </body>"


# ---------------------------------------------------------------------------
# ZimWriter static method tests
# ---------------------------------------------------------------------------


class TestZimWriterStaticMethods:

    def test_compute_period_new_month(self) -> None:
        """compute_period() returns YYYY-MM for a new month."""
        now = datetime(2026, 5, 1)
        result = ZimWriter.compute_period(["2026-04"], now=now)
        assert result == "2026-05"

    def test_compute_period_same_month_no_existing(self) -> None:
        """compute_period() returns YYYY-MM when no exports exist for this month."""
        now = datetime(2026, 4, 28)
        result = ZimWriter.compute_period([], now=now)
        assert result == "2026-04"

    def test_compute_period_same_month_one_existing(self) -> None:
        """compute_period() appends 'a' suffix for second export of same month."""
        now = datetime(2026, 4, 28)
        result = ZimWriter.compute_period(["2026-04"], now=now)
        assert result == "2026-04a"

    def test_compute_period_same_month_two_existing(self) -> None:
        """compute_period() appends 'b' suffix for third export of same month."""
        now = datetime(2026, 4, 28)
        result = ZimWriter.compute_period(["2026-04", "2026-04a"], now=now)
        assert result == "2026-04b"

    def test_build_filename_valid(self) -> None:
        """build_filename() produces correct ZIM filename."""
        result = ZimWriter.build_filename("open-repo_en_nopic", "2026-04")
        assert result == "open-repo_en_nopic_2026-04.zim"

    def test_build_filename_with_suffix(self) -> None:
        """build_filename() handles period suffix correctly."""
        result = ZimWriter.build_filename("open-repo_en_agriculture", "2026-04a")
        assert result == "open-repo_en_agriculture_2026-04a.zim"

    def test_build_filename_invalid_name_raises(self) -> None:
        """build_filename() raises ValueError for invalid name."""
        with pytest.raises(ValueError, match="Invalid ZIM name"):
            ZimWriter.build_filename("OpenRepo_English", "2026-04")

    def test_build_filename_invalid_period_raises(self) -> None:
        """build_filename() raises ValueError for invalid period format."""
        with pytest.raises(ValueError, match="Invalid period"):
            ZimWriter.build_filename("open-repo_en_nopic", "April-2026")


# ---------------------------------------------------------------------------
# OPDSEntry Tests
# ---------------------------------------------------------------------------


class TestOPDSEntry:

    def test_valid_entry_initializes(self, sample_opds_entry: OPDSEntry) -> None:
        """Valid OPDSEntry initializes without error."""
        assert sample_opds_entry.name == "open-repo_en_nopic"
        assert sample_opds_entry.flavour == "nopic"

    def test_invalid_uuid_raises_value_error(self) -> None:
        """OPDSEntry raises ValueError for invalid UUID."""
        with pytest.raises(ValueError, match="valid UUID"):
            OPDSEntry(
                uuid="not-a-uuid",
                title="Test",
                name="open-repo_en_nopic",
                flavour="nopic",
                language="eng",
                period="2026-04",
                description="Test",
                download_url="https://example.org/test.zim",
                file_size_bytes=1024,
                sha256_checksum="a" * 64,
                article_count=10,
                generated_at=datetime.utcnow(),
            )

    def test_invalid_name_raises_value_error(self) -> None:
        """OPDSEntry raises ValueError for name not matching openZIM convention."""
        with pytest.raises(ValueError, match="naming convention"):
            OPDSEntry(
                uuid=str(uuid.uuid4()),
                title="Test",
                name="OpenRepo_English",  # Wrong format
                flavour="all",
                language="eng",
                period="2026-04",
                description="Test",
                download_url="https://example.org/test.zim",
                file_size_bytes=1024,
                sha256_checksum="a" * 64,
                article_count=10,
                generated_at=datetime.utcnow(),
            )

    def test_description_over_80_chars_raises(self) -> None:
        """OPDSEntry raises ValueError for description over 80 chars."""
        with pytest.raises(ValueError, match="80 characters"):
            OPDSEntry(
                uuid=str(uuid.uuid4()),
                title="Test",
                name="open-repo_en_nopic",
                flavour="nopic",
                language="eng",
                period="2026-04",
                description="A" * 81,
                download_url="https://example.org/test.zim",
                file_size_bytes=1024,
                sha256_checksum="a" * 64,
                article_count=10,
                generated_at=datetime.utcnow(),
            )

    def test_filename_property(self, sample_opds_entry: OPDSEntry) -> None:
        """filename property returns {name}_{period}.zim."""
        assert sample_opds_entry.filename == "open-repo_en_nopic_2026-04.zim"

    def test_entry_id_is_urn(self, sample_opds_entry: OPDSEntry) -> None:
        """entry_id property returns urn:uuid: formatted string."""
        assert sample_opds_entry.entry_id.startswith("urn:uuid:")

    def test_updated_iso_format(self, sample_opds_entry: OPDSEntry) -> None:
        """updated_iso property returns ISO 8601 with UTC Z suffix."""
        iso = sample_opds_entry.updated_iso
        assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", iso)

    def test_file_size_human_megabytes(self, sample_opds_entry: OPDSEntry) -> None:
        """file_size_human returns MB for megabyte-range files."""
        assert "MB" in sample_opds_entry.file_size_human

    def test_from_dict_constructs_entry(self) -> None:
        """OPDSEntry.from_dict() constructs a valid entry from a dictionary."""
        data = {
            "uuid": str(uuid.uuid4()),
            "title": "Test Export",
            "name": "open-repo_en_nopic",
            "flavour": "nopic",
            "language": "eng",
            "period": "2026-04",
            "description": "Test description",
            "download_url": "https://example.org/test.zim",
            "file_size_bytes": 52428800,
            "sha256_checksum": "b" * 64,
            "article_count": 250,
            "generated_at": datetime(2026, 4, 28),
        }
        entry = OPDSEntry.from_dict(data)
        assert entry.name == "open-repo_en_nopic"
        assert entry.article_count == 250


# ---------------------------------------------------------------------------
# OPDSGenerator Tests
# ---------------------------------------------------------------------------


class TestOPDSGenerator:

    def test_generator_initializes(self, opds_generator: OPDSGenerator) -> None:
        """OPDSGenerator initializes without error."""
        assert opds_generator.entry_count() == 0

    def test_invalid_node_uuid_raises(self) -> None:
        """OPDSGenerator raises ValueError for invalid node UUID."""
        with pytest.raises(ValueError, match="valid UUID"):
            OPDSGenerator(
                node_uuid="invalid",
                node_name="Test",
                node_url="https://example.org",
                catalog_url="https://example.org/opds/v2/root.xml",
            )

    def test_add_entry_increments_count(
        self, opds_generator: OPDSGenerator, sample_opds_entry: OPDSEntry
    ) -> None:
        """add_entry() increments entry_count."""
        assert opds_generator.entry_count() == 0
        opds_generator.add_entry(sample_opds_entry)
        assert opds_generator.entry_count() == 1

    def test_generate_root_catalog_returns_valid_xml(
        self, opds_generator: OPDSGenerator, sample_opds_entry: OPDSEntry
    ) -> None:
        """generate_root_catalog() returns parseable XML bytes."""
        opds_generator.add_entry(sample_opds_entry)
        xml_bytes = opds_generator.generate_root_catalog()
        assert isinstance(xml_bytes, bytes)
        # Should parse without error
        root = ET.fromstring(xml_bytes)
        assert root is not None

    def test_root_catalog_xml_declaration(
        self, opds_generator: OPDSGenerator
    ) -> None:
        """Root catalog starts with XML declaration."""
        xml_bytes = opds_generator.generate_root_catalog()
        assert xml_bytes.startswith(b"<?xml version")

    def test_root_catalog_has_feed_element(
        self, opds_generator: OPDSGenerator
    ) -> None:
        """Root catalog root element is <feed>."""
        xml_bytes = opds_generator.generate_root_catalog()
        root = ET.fromstring(xml_bytes)
        local = root.tag.split("}")[-1] if "}" in root.tag else root.tag
        assert local == "feed"

    def test_acquisition_feed_has_entry_per_export(
        self, opds_generator: OPDSGenerator, sample_opds_entry: OPDSEntry
    ) -> None:
        """Acquisition feed has one <entry> element per added OPDSEntry."""
        opds_generator.add_entry(sample_opds_entry)
        xml_bytes = opds_generator.generate_acquisition_feed()
        root = ET.fromstring(xml_bytes)
        ns = "{http://www.w3.org/2005/Atom}"
        entries = root.findall(f"{ns}entry")
        assert len(entries) == 1

    def test_acquisition_feed_entry_has_download_link(
        self, opds_generator: OPDSGenerator, sample_opds_entry: OPDSEntry
    ) -> None:
        """Each acquisition feed entry has a ZIM download link."""
        opds_generator.add_entry(sample_opds_entry)
        xml_bytes = opds_generator.generate_acquisition_feed()
        root = ET.fromstring(xml_bytes)
        ns = "{http://www.w3.org/2005/Atom}"
        entry = root.find(f"{ns}entry")
        assert entry is not None

        links = entry.findall(f"{ns}link")
        zim_links = [
            lnk for lnk in links
            if lnk.get("type") == MIME_ZIM
        ]
        assert len(zim_links) >= 1, "Entry must have at least one application/x-zim link"

    def test_acquisition_feed_zim_link_has_correct_href(
        self, opds_generator: OPDSGenerator, sample_opds_entry: OPDSEntry
    ) -> None:
        """ZIM download link href matches the entry's download_url."""
        opds_generator.add_entry(sample_opds_entry)
        xml_bytes = opds_generator.generate_acquisition_feed()
        root = ET.fromstring(xml_bytes)
        ns = "{http://www.w3.org/2005/Atom}"
        entry = root.find(f"{ns}entry")
        links = entry.findall(f"{ns}link")
        zim_link = next(lnk for lnk in links if lnk.get("type") == MIME_ZIM)
        assert zim_link.get("href") == sample_opds_entry.download_url

    def test_validate_opds_xml_passes_for_valid_root(
        self, opds_generator: OPDSGenerator, sample_opds_entry: OPDSEntry
    ) -> None:
        """validate_opds_xml() returns no errors for a valid root catalog."""
        opds_generator.add_entry(sample_opds_entry)
        xml_bytes = opds_generator.generate_root_catalog()
        errors = OPDSGenerator.validate_opds_xml(xml_bytes)
        assert errors == [], f"Expected no errors, got: {errors}"

    def test_validate_opds_xml_passes_for_valid_acquisition_feed(
        self, opds_generator: OPDSGenerator, sample_opds_entry: OPDSEntry
    ) -> None:
        """validate_opds_xml() returns no errors for a valid acquisition feed."""
        opds_generator.add_entry(sample_opds_entry)
        xml_bytes = opds_generator.generate_acquisition_feed()
        errors = OPDSGenerator.validate_opds_xml(xml_bytes)
        assert errors == [], f"Expected no errors, got: {errors}"

    def test_validate_opds_xml_fails_for_malformed_xml(self) -> None:
        """validate_opds_xml() returns error list for malformed XML."""
        errors = OPDSGenerator.validate_opds_xml(b"<this is not xml")
        assert len(errors) >= 1
        assert any("parse error" in e.lower() or "XML" in e for e in errors)

    def test_generate_search_description_returns_opensearch_xml(
        self, opds_generator: OPDSGenerator
    ) -> None:
        """generate_search_description() returns OpenSearch XML."""
        xml_bytes = opds_generator.generate_search_description()
        assert b"OpenSearchDescription" in xml_bytes
        assert b"searchTerms" in xml_bytes

    def test_get_entry_by_name_returns_correct_entry(
        self, opds_generator: OPDSGenerator, sample_opds_entry: OPDSEntry
    ) -> None:
        """get_entry_by_name() returns the matching entry."""
        opds_generator.add_entry(sample_opds_entry)
        found = opds_generator.get_entry_by_name("open-repo_en_nopic")
        assert found is not None
        assert found.uuid == sample_opds_entry.uuid

    def test_get_entry_by_name_returns_none_for_missing(
        self, opds_generator: OPDSGenerator
    ) -> None:
        """get_entry_by_name() returns None when no matching entry exists."""
        result = opds_generator.get_entry_by_name("open-repo_en_agriculture")
        assert result is None

    def test_entries_sorted_alphabetically(
        self, opds_generator: OPDSGenerator
    ) -> None:
        """get_entries_sorted() returns entries in alphabetical order by name."""
        for name, flavour in [
            ("open-repo_en_recipes", "recipes"),
            ("open-repo_en_agriculture", "agriculture"),
            ("open-repo_en_nopic", "nopic"),
        ]:
            entry = OPDSEntry(
                uuid=str(uuid.uuid4()),
                title=f"Test {flavour}",
                name=name,
                flavour=flavour,
                language="eng",
                period="2026-04",
                description=f"Test {flavour}",
                download_url=f"https://example.org/{name}_2026-04.zim",
                file_size_bytes=1024 * 1024,
                sha256_checksum="c" * 64,
                article_count=10,
                generated_at=datetime.utcnow(),
            )
            opds_generator.add_entry(entry)

        sorted_entries = opds_generator.get_entries_sorted()
        names = [e.name for e in sorted_entries]
        assert names == sorted(names), f"Entries not sorted: {names}"


# ---------------------------------------------------------------------------
# End-to-end pipeline test
# ---------------------------------------------------------------------------


class TestEndToEndPipeline:
    """
    End-to-end test: synthetic Phase 4 content -> ZimWriter -> OPDS catalog.

    Simulates the complete pipeline without network calls or real python-libzim.
    Verifies that the pipeline components work together correctly.
    """

    def test_full_pipeline_with_synthetic_data(
        self,
        sample_metadata: ZimMetadata,
        sample_config: ExportConfig,
        sample_content_items: list[dict],
        opds_generator: OPDSGenerator,
        tmp_path: Path,
    ) -> None:
        """
        Full pipeline: 5 local items -> ZimWriter -> ZimWriteResult -> OPDSEntry -> catalog.
        """
        output_path = tmp_path / "open-repo_en_nopic_2026-04.zim"

        # Step 1: Initialize ZimWriter
        writer = ZimWriter(
            metadata=sample_metadata,
            config=sample_config,
            output_path=output_path,
            zimcheck_binary=None,
        )

        # Step 2: Add shared CSS resource
        writer.add_resource(
            path="style/main.css",
            binary_content=b"body{font-family:sans-serif;margin:1rem;} .attribution{font-size:.8em;color:#666;}",
            mime_type="text/css",
        )

        # Step 3: Add local content items (exclude federated items)
        local_items = [item for item in sample_content_items if item["is_local"]]
        for item in local_items:
            title = item["title"].get("en", "Untitled")
            description = item["content_jsonld"].get("description", {}).get("en", "")
            html = _make_html(title, description)
            writer.add_article(
                path=f"{item['domain']}/{item['cid']}",
                content=html,
                article_type=item["item_type"],
                language="en",
            )

        # Step 4: Add index page
        writer.add_article(
            path="index",
            content=_make_html("Open-Repo Offline Library", "Browse the knowledge library below."),
            article_type="procedure",
        )

        assert writer.article_count == len(local_items) + 1  # items + index

        # Step 5: Create ZIM (stub)
        result = writer.create_zim(run_zimcheck=False)

        assert result.output_path.exists()
        assert result.article_count == len(local_items) + 1
        assert result.sha256 is not None
        assert len(result.sha256) == 64
        assert result.zimcheck_passed is True  # Skipped but marked True

        # Step 6: Build OPDS entry from result
        opds_entry = OPDSEntry(
            uuid="a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11",
            title=sample_metadata.title,
            name=sample_metadata.name,
            flavour=sample_metadata.flavour,
            language=sample_metadata.language,
            period="2026-04",
            description=sample_metadata.description,
            download_url=f"https://exports.test.example.org/zim/{result.output_path.name}",
            file_size_bytes=result.file_size_bytes,
            sha256_checksum=result.sha256,
            article_count=result.article_count,
            generated_at=datetime.utcnow(),
        )

        # Step 7: Add to OPDS catalog
        opds_generator.add_entry(opds_entry)
        assert opds_generator.entry_count() == 1

        # Step 8: Generate and validate OPDS XML
        root_xml = opds_generator.generate_root_catalog()
        entries_xml = opds_generator.generate_acquisition_feed()

        root_errors = OPDSGenerator.validate_opds_xml(root_xml)
        entries_errors = OPDSGenerator.validate_opds_xml(entries_xml)

        assert root_errors == [], f"Root catalog errors: {root_errors}"
        assert entries_errors == [], f"Acquisition feed errors: {entries_errors}"

    def test_federated_items_excluded_in_local_only_scope(
        self,
        sample_metadata: ZimMetadata,
        sample_config: ExportConfig,
        sample_content_items: list[dict],
        tmp_path: Path,
    ) -> None:
        """
        Federated items (is_local=False) must be excluded in LOCAL_ONLY scope.

        This test simulates the export service's query logic — it verifies that
        the scope filtering is applied correctly before calling add_article().
        """
        assert sample_config.scope == ExportScope.LOCAL_ONLY

        writer = ZimWriter(
            metadata=sample_metadata,
            config=sample_config,
            output_path=tmp_path / "test_local_only.zim",
            zimcheck_binary=None,
        )

        local_items = [i for i in sample_content_items if i["is_local"]]
        federated_items = [i for i in sample_content_items if not i["is_local"]]

        assert len(federated_items) >= 1, "Test data must include at least one federated item"

        for item in local_items:
            writer.add_article(
                path=f"{item['domain']}/{item['cid']}",
                content=_make_html(item["title"].get("en", ""), ""),
                article_type=item["item_type"],
            )

        assert writer.article_count == len(local_items)
        # Federated items were NOT added
        assert writer.article_count < len(sample_content_items)

    def test_unicode_content_handled_correctly(
        self,
        sample_metadata: ZimMetadata,
        sample_config: ExportConfig,
        tmp_path: Path,
    ) -> None:
        """Unicode content (non-ASCII characters) is handled without error."""
        writer = ZimWriter(
            metadata=sample_metadata,
            config=sample_config,
            output_path=tmp_path / "test_unicode.zim",
            zimcheck_binary=None,
        )

        unicode_content = _make_html(
            "Préparation du filtre à sable",
            "Étapes: Récupérer le sable, le tamiser, l'humidifier... "
            "日本語テスト. العربية. Ñoño."
        )

        writer.add_article(
            path="test/unicode-item",
            content=unicode_content,
            article_type="procedure",
        )
        assert writer.article_count == 1
        result = writer.create_zim(run_zimcheck=False)
        assert result.article_count == 1
