"""
Tests for ExportService — Phase 5 Step 1.

Tests cover:
  1. HTML rendering: all content types (procedure, recipe, schematic, plan, generic)
  2. HTML rendering: multilingual field fallback
  3. HTML rendering: XSS escaping of user-supplied fields
  4. HTML rendering: attribution footer for federated content
  5. HTML rendering: index page generation
  6. generate_zim_metadata(): name convention, title truncation, language display
  7. validate_zim_output(): all check conditions
  8. export_to_zim(): full pipeline with stub DB (index-only ZIM)
  9. export_to_zim(): pipeline integration — ZimWriter receives correct calls
  10. _pick_language() and _escape() utility functions
  11. _license_url() for known and unknown identifiers

All tests run without a real database connection: ExportService is instantiated
with db_session=None (stub mode). The ZimWriter stub (no python-libzim) is used
throughout, meaning no real ZIM binary is produced. Tests verify pipeline logic,
not ZIM binary format.
"""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path
from typing import Optional
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from app.services.export.export_service import (
    ExportService,
    _escape,
    _license_url,
    _pick_language,
)
from app.services.export.zim_writer import (
    ExportConfig,
    ExportScope,
    ZimMetadata,
    ZimWriteResult,
    ZimWriter,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def service() -> ExportService:
    """ExportService in stub mode (no database session)."""
    return ExportService(db_session=None)


@pytest.fixture
def procedure_item() -> dict:
    """Synthetic Procedure content item."""
    return {
        "cid": "bafkrei001",
        "title": {"en": "Biosand Water Filter Construction"},
        "item_type": "procedure",
        "domain": "water",
        "license": "CC-BY-4.0",
        "is_local": True,
        "source_url": None,
        "source_title": None,
        "created_at": datetime(2026, 1, 15),
        "updated_at": datetime(2026, 1, 15),
        "content_jsonld": {
            "@type": "Procedure",
            "language": ["en"],
            "description": {"en": "Step-by-step biosand water filter construction."},
            "difficulty": "intermediate",
            "tools": [
                {"name": {"en": "Wooden mold"}, "quantity": 1},
                {"name": {"en": "Level"}, "quantity": 1},
            ],
            "materials": [
                {"name": {"en": "Fine sand"}, "quantity": "100 kg"},
                {"name": {"en": "Coarse gravel"}, "quantity": "20 kg"},
            ],
            "steps": [
                {
                    "stepNumber": 1,
                    "title": {"en": "Prepare the mold"},
                    "body": {"en": "Build a wooden mold 30 cm x 60 cm x 120 cm."},
                },
                {
                    "stepNumber": 2,
                    "title": {"en": "Layer the sand"},
                    "body": {"en": "Add coarse gravel first, then fine sand."},
                },
            ],
        },
    }


@pytest.fixture
def recipe_item() -> dict:
    """Synthetic Recipe content item."""
    return {
        "cid": "bafkrei003",
        "title": {"en": "Fermented Cassava Flour"},
        "item_type": "recipe",
        "domain": "recipes",
        "license": "CC0-1.0",
        "is_local": True,
        "source_url": None,
        "source_title": None,
        "created_at": datetime(2026, 2, 10),
        "updated_at": datetime(2026, 2, 10),
        "content_jsonld": {
            "@type": "Recipe",
            "description": {"en": "Traditional fermented cassava flour."},
            "ingredients": [
                {"name": {"en": "Fresh cassava roots"}, "quantity": "5 kg"},
                {"name": {"en": "Water"}, "quantity": "10 L"},
            ],
            "steps": [
                {"stepNumber": 1, "title": {"en": "Peel and wash"}, "body": {"en": "Peel roots, wash well."}},
                {"stepNumber": 2, "title": {"en": "Ferment"}, "body": {"en": "Submerge in water 3 days."}},
            ],
        },
    }


@pytest.fixture
def schematic_item() -> dict:
    """Synthetic Schematic content item."""
    return {
        "cid": "bafkrei004",
        "title": {"en": "Rainwater Harvesting Schematic"},
        "item_type": "schematic",
        "domain": "water",
        "license": "CC-BY-4.0",
        "is_local": True,
        "source_url": None,
        "source_title": None,
        "created_at": datetime(2026, 3, 5),
        "updated_at": datetime(2026, 3, 5),
        "content_jsonld": {
            "@type": "Schematic",
            "description": {"en": "Rooftop rainwater collection system."},
        },
    }


@pytest.fixture
def plan_item() -> dict:
    """Synthetic Plan content item."""
    return {
        "cid": "bafkrei005",
        "title": {"en": "Moringa Grove 12-Month Plan"},
        "item_type": "plan",
        "domain": "agriculture",
        "license": "CC-BY-4.0",
        "is_local": True,
        "source_url": None,
        "source_title": None,
        "created_at": datetime(2026, 3, 20),
        "updated_at": datetime(2026, 3, 20),
        "content_jsonld": {
            "@type": "Plan",
            "description": {"en": "Twelve-month plan for establishing a moringa grove."},
            "steps": [
                {"stepNumber": 1, "title": {"en": "Site preparation"}, "body": {"en": "Clear land and test soil pH."}},
                {"stepNumber": 2, "title": {"en": "Seed sourcing"}, "body": {"en": "Source moringa seeds locally."}},
            ],
        },
    }


@pytest.fixture
def federated_item() -> dict:
    """Synthetic federated content item (from a partner node)."""
    return {
        "cid": "bafkrei006",
        "title": {"en": "Vermicomposting Setup"},
        "item_type": "procedure",
        "domain": "agriculture",
        "license": "CC-BY-4.0",
        "is_local": False,
        "source_url": "https://partner-node.example.org",
        "source_title": "Partner Node Alpha",
        "created_at": datetime(2026, 4, 1),
        "updated_at": datetime(2026, 4, 1),
        "content_jsonld": {
            "@type": "Procedure",
            "description": {"en": "Setting up a worm composting bin."},
            "steps": [
                {"stepNumber": 1, "title": {"en": "Prepare the bin"}, "body": {"en": "Drill drainage holes."}},
            ],
        },
    }


@pytest.fixture
def sample_metadata() -> ZimMetadata:
    """Standard valid ZimMetadata for pipeline tests."""
    return ZimMetadata(
        title="Open-Repo: Test Export",
        description="Offline practical knowledge library",
        language="eng",
        name="open-repo_en_nopic",
        flavour="nopic",
        creator="Open-Repo Community",
        publisher="Open-Repo",
        source_url="https://test.open-repo.example.org",
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


# ---------------------------------------------------------------------------
# 1. HTML rendering — Procedure
# ---------------------------------------------------------------------------


class TestRenderProcedure:

    def test_procedure_produces_html5_document(
        self, service: ExportService, procedure_item: dict
    ) -> None:
        """Rendered HTML starts with DOCTYPE and has <html> element."""
        html = service.render_article_html(procedure_item)
        assert html.startswith("<!DOCTYPE html>")
        assert "<html" in html
        assert "</html>" in html

    def test_procedure_title_in_head_and_h1(
        self, service: ExportService, procedure_item: dict
    ) -> None:
        """Title appears in both <title> tag and <h1> heading."""
        html = service.render_article_html(procedure_item)
        assert "<title>Biosand Water Filter Construction</title>" in html
        assert "<h1>Biosand Water Filter Construction</h1>" in html

    def test_procedure_has_inline_css(
        self, service: ExportService, procedure_item: dict
    ) -> None:
        """Rendered HTML has a <style> block (inline CSS for self-containment)."""
        html = service.render_article_html(procedure_item)
        assert "<style>" in html
        assert "body {" in html or "body{" in html

    def test_procedure_has_no_external_css_links(
        self, service: ExportService, procedure_item: dict
    ) -> None:
        """No <link rel='stylesheet'> pointing to external URLs."""
        html = service.render_article_html(procedure_item)
        # No external http stylesheet links
        assert not re.search(r'<link[^>]+rel=["\']stylesheet["\'][^>]+href=["\']http', html)

    def test_procedure_renders_tools_table(
        self, service: ExportService, procedure_item: dict
    ) -> None:
        """Tools appear in an HTML table."""
        html = service.render_article_html(procedure_item)
        assert "Wooden mold" in html
        assert "Level" in html
        assert "<table" in html.lower()

    def test_procedure_renders_materials_table(
        self, service: ExportService, procedure_item: dict
    ) -> None:
        """Materials appear in an HTML table."""
        html = service.render_article_html(procedure_item)
        assert "Fine sand" in html
        assert "100 kg" in html

    def test_procedure_renders_numbered_steps(
        self, service: ExportService, procedure_item: dict
    ) -> None:
        """Steps appear as an ordered list."""
        html = service.render_article_html(procedure_item)
        assert "Prepare the mold" in html
        assert "Layer the sand" in html
        assert "<ol" in html

    def test_procedure_includes_difficulty(
        self, service: ExportService, procedure_item: dict
    ) -> None:
        """Difficulty level appears in rendered HTML."""
        html = service.render_article_html(procedure_item)
        assert "intermediate" in html

    def test_procedure_includes_license_with_link(
        self, service: ExportService, procedure_item: dict
    ) -> None:
        """Known license identifiers are rendered with a hyperlink."""
        html = service.render_article_html(procedure_item)
        assert "CC-BY-4.0" in html
        assert "creativecommons.org" in html

    def test_procedure_has_article_footer(
        self, service: ExportService, procedure_item: dict
    ) -> None:
        """Footer with Open-Repo attribution is present."""
        html = service.render_article_html(procedure_item)
        assert "Open-Repo Offline Library" in html

    def test_procedure_no_attribution_footer_for_local_item(
        self, service: ExportService, procedure_item: dict
    ) -> None:
        """Local items must NOT have a federated attribution block."""
        html = service.render_article_html(procedure_item)
        assert "Federated content" not in html
        assert "Originally published on" not in html


# ---------------------------------------------------------------------------
# 2. HTML rendering — Recipe
# ---------------------------------------------------------------------------


class TestRenderRecipe:

    def test_recipe_renders_ingredients_table(
        self, service: ExportService, recipe_item: dict
    ) -> None:
        """Ingredients appear in an HTML table with quantity and name columns."""
        html = service.render_article_html(recipe_item)
        assert "Ingredients" in html
        assert "Fresh cassava roots" in html
        assert "5 kg" in html
        assert "<table" in html.lower()

    def test_recipe_renders_method_steps(
        self, service: ExportService, recipe_item: dict
    ) -> None:
        """Recipe steps are labelled 'Method' and rendered as ordered list."""
        html = service.render_article_html(recipe_item)
        assert "Method" in html
        assert "Peel and wash" in html
        assert "Ferment" in html

    def test_recipe_step_bodies_present(
        self, service: ExportService, recipe_item: dict
    ) -> None:
        """Step body text is included in recipe HTML."""
        html = service.render_article_html(recipe_item)
        assert "Submerge in water 3 days" in html

    def test_recipe_cc0_license(
        self, service: ExportService, recipe_item: dict
    ) -> None:
        """CC0 license is rendered with creativecommons.org link."""
        html = service.render_article_html(recipe_item)
        assert "CC0-1.0" in html
        assert "creativecommons.org" in html


# ---------------------------------------------------------------------------
# 3. HTML rendering — Schematic
# ---------------------------------------------------------------------------


class TestRenderSchematic:

    def test_schematic_includes_diagram_note(
        self, service: ExportService, schematic_item: dict
    ) -> None:
        """Schematic entries include a note about the diagram file."""
        html = service.render_article_html(schematic_item)
        assert "schematic diagram" in html

    def test_schematic_title_rendered(
        self, service: ExportService, schematic_item: dict
    ) -> None:
        """Schematic title appears correctly in HTML."""
        html = service.render_article_html(schematic_item)
        assert "Rainwater Harvesting Schematic" in html


# ---------------------------------------------------------------------------
# 4. HTML rendering — Plan
# ---------------------------------------------------------------------------


class TestRenderPlan:

    def test_plan_renders_milestones(
        self, service: ExportService, plan_item: dict
    ) -> None:
        """Plan steps are labelled 'Milestones' in the HTML."""
        html = service.render_article_html(plan_item)
        assert "Milestones" in html

    def test_plan_steps_rendered(
        self, service: ExportService, plan_item: dict
    ) -> None:
        """Plan step titles appear in HTML."""
        html = service.render_article_html(plan_item)
        assert "Site preparation" in html
        assert "Seed sourcing" in html

    def test_plan_step_bodies_present(
        self, service: ExportService, plan_item: dict
    ) -> None:
        """Plan step body text is included."""
        html = service.render_article_html(plan_item)
        assert "Clear land and test soil pH" in html


# ---------------------------------------------------------------------------
# 5. HTML rendering — Federated attribution
# ---------------------------------------------------------------------------


class TestRenderFederatedAttribution:

    def test_federated_item_has_attribution_block(
        self, service: ExportService, federated_item: dict
    ) -> None:
        """Federated content renders with an attribution block."""
        html = service.render_article_html(federated_item)
        assert "Federated content" in html
        assert "partner-node.example.org" in html

    def test_federated_item_attribution_includes_source_title(
        self, service: ExportService, federated_item: dict
    ) -> None:
        """Attribution block shows the source node's display name."""
        html = service.render_article_html(federated_item)
        assert "Partner Node Alpha" in html

    def test_federated_attribution_href_matches_source_url(
        self, service: ExportService, federated_item: dict
    ) -> None:
        """Attribution link href matches source_url."""
        html = service.render_article_html(federated_item)
        assert 'href="https://partner-node.example.org"' in html


# ---------------------------------------------------------------------------
# 6. HTML rendering — Multilingual fallback
# ---------------------------------------------------------------------------


class TestMultilingualFallback:

    def test_picks_requested_language(self, service: ExportService) -> None:
        """render_article_html selects the requested language from a multilingual dict."""
        item = {
            "cid": "bafkrei-ml-001",
            "title": {"en": "English Title", "fr": "Titre Français"},
            "item_type": "procedure",
            "domain": "water",
            "license": "CC-BY-4.0",
            "is_local": True,
            "source_url": None,
            "source_title": None,
            "created_at": datetime(2026, 1, 1),
            "updated_at": datetime(2026, 1, 1),
            "content_jsonld": {
                "description": {"en": "English desc", "fr": "Description française"},
                "steps": [],
            },
        }
        html_en = service.render_article_html(item, language="en")
        html_fr = service.render_article_html(item, language="fr")

        assert "English Title" in html_en
        assert "Titre Français" not in html_en

        assert "Titre Français" in html_fr
        assert "English Title" not in html_fr

    def test_falls_back_to_available_language(self, service: ExportService) -> None:
        """When requested language is absent, falls back to first available."""
        item = {
            "cid": "bafkrei-ml-002",
            "title": {"sw": "Jua Kali"},  # only Swahili available
            "item_type": "procedure",
            "domain": "water",
            "license": "CC-BY-4.0",
            "is_local": True,
            "source_url": None,
            "source_title": None,
            "created_at": datetime(2026, 1, 1),
            "updated_at": datetime(2026, 1, 1),
            "content_jsonld": {"steps": []},
        }
        html = service.render_article_html(item, language="en")
        assert "Jua Kali" in html


# ---------------------------------------------------------------------------
# 7. HTML rendering — XSS escaping
# ---------------------------------------------------------------------------


class TestXSSEscaping:

    def test_title_xss_escaped(self, service: ExportService) -> None:
        """Malicious title content is HTML-escaped and not rendered as tags."""
        item = {
            "cid": "bafkrei-xss-001",
            "title": {"en": "<script>alert('xss')</script>"},
            "item_type": "procedure",
            "domain": "test",
            "license": "CC0-1.0",
            "is_local": True,
            "source_url": None,
            "source_title": None,
            "created_at": datetime(2026, 1, 1),
            "updated_at": datetime(2026, 1, 1),
            "content_jsonld": {"steps": []},
        }
        html = service.render_article_html(item)
        assert "<script>" not in html
        assert "&lt;script&gt;" in html

    def test_domain_xss_escaped(self, service: ExportService) -> None:
        """Domain field is HTML-escaped."""
        item = {
            "cid": "bafkrei-xss-002",
            "title": {"en": "Safe Title"},
            "item_type": "procedure",
            "domain": '<img src=x onerror="alert(1)">',
            "license": "CC0-1.0",
            "is_local": True,
            "source_url": None,
            "source_title": None,
            "created_at": datetime(2026, 1, 1),
            "updated_at": datetime(2026, 1, 1),
            "content_jsonld": {"steps": []},
        }
        html = service.render_article_html(item)
        assert '<img src=x onerror="alert(1)">' not in html
        assert "&lt;img" in html

    def test_step_body_xss_escaped(self, service: ExportService) -> None:
        """Step body text is HTML-escaped."""
        item = {
            "cid": "bafkrei-xss-003",
            "title": {"en": "Title"},
            "item_type": "procedure",
            "domain": "test",
            "license": "CC0-1.0",
            "is_local": True,
            "source_url": None,
            "source_title": None,
            "created_at": datetime(2026, 1, 1),
            "updated_at": datetime(2026, 1, 1),
            "content_jsonld": {
                "steps": [
                    {"stepNumber": 1, "title": {"en": "Step"}, "body": {"en": "<b>bold</b> text"}}
                ]
            },
        }
        html = service.render_article_html(item)
        assert "<b>bold</b>" not in html
        assert "&lt;b&gt;" in html

    def test_source_url_escaped_in_attribution(self, service: ExportService) -> None:
        """Malicious source_url is HTML-escaped in the attribution link."""
        item = {
            "cid": "bafkrei-xss-004",
            "title": {"en": "Title"},
            "item_type": "procedure",
            "domain": "test",
            "license": "CC0-1.0",
            "is_local": False,
            "source_url": 'https://safe.example.org" onmouseover="alert(1)',
            "source_title": None,
            "created_at": datetime(2026, 1, 1),
            "updated_at": datetime(2026, 1, 1),
            "content_jsonld": {"steps": []},
        }
        html = service.render_article_html(item)
        assert 'onmouseover="alert(1)' not in html


# ---------------------------------------------------------------------------
# 8. Index page rendering
# ---------------------------------------------------------------------------


class TestRenderIndexPage:

    def test_index_page_is_valid_html(self, service: ExportService) -> None:
        """render_index_html produces a valid HTML5 document."""
        html = service.render_index_html()
        assert html.startswith("<!DOCTYPE html>")
        assert "<html" in html
        assert "</html>" in html

    def test_index_page_contains_node_name(self, service: ExportService) -> None:
        """Node name appears in the index page title."""
        html = service.render_index_html(node_name="My Test Node")
        assert "My Test Node" in html

    def test_index_page_with_domains(self, service: ExportService) -> None:
        """Index page renders domain cards when items_by_domain is provided."""
        items_by_domain = {
            "water": [{"cid": "a"}, {"cid": "b"}],
            "agriculture": [{"cid": "c"}],
        }
        html = service.render_index_html(items_by_domain=items_by_domain)
        assert "Water" in html  # domain.title()
        assert "Agriculture" in html
        assert "2 articles" in html
        assert "1 article" in html  # singular

    def test_index_page_no_domains(self, service: ExportService) -> None:
        """Index page without domain data shows generic welcome message."""
        html = service.render_index_html(items_by_domain=None)
        assert "offline copy" in html.lower() or "knowledge library" in html.lower()

    def test_index_page_kiwix_link_present(self, service: ExportService) -> None:
        """Index footer links to kiwix.org."""
        html = service.render_index_html()
        assert "kiwix.org" in html

    def test_index_page_has_inline_css(self, service: ExportService) -> None:
        """Index page is self-contained with inline CSS."""
        html = service.render_index_html()
        assert "<style>" in html


# ---------------------------------------------------------------------------
# 9. generate_zim_metadata()
# ---------------------------------------------------------------------------


class TestGenerateZimMetadata:

    def test_generates_valid_metadata(self) -> None:
        """generate_zim_metadata() produces a ZimMetadata with no validation errors."""
        metadata = ExportService.generate_zim_metadata(
            node_url="https://node.example.org",
            flavour="nopic",
            language_iso3="eng",
            node_name="Open-Repo",
        )
        errors = metadata.validate()
        assert errors == [], f"Unexpected validation errors: {errors}"

    def test_name_follows_openzim_convention(self) -> None:
        """Generated name matches {publisher}_{lang}_{flavour} pattern."""
        metadata = ExportService.generate_zim_metadata(
            node_url="https://node.example.org",
            flavour="nopic",
            language_iso3="eng",
            node_name="Open-Repo",
        )
        assert metadata.name == "open-repo_en_nopic"

    def test_name_slugifies_node_name_spaces(self) -> None:
        """Spaces in node_name are converted to hyphens in the slug."""
        metadata = ExportService.generate_zim_metadata(
            node_url="https://node.example.org",
            flavour="agriculture",
            language_iso3="spa",
            node_name="My Knowledge Node",
        )
        assert metadata.name == "my-knowledge-node_sp_agriculture"

    def test_title_contains_language_display(self) -> None:
        """Generated title references the language (English or truncated prefix of it)."""
        metadata = ExportService.generate_zim_metadata(
            node_url="https://node.example.org",
            flavour="nopic",
            language_iso3="eng",
            node_name="Open-Repo",
        )
        # The title may be truncated to 30 chars; it will contain at least the
        # opening parenthesis and the first few characters of "English".
        assert "(En" in metadata.title or "English" in metadata.title

    def test_title_under_30_chars_when_truncated(self) -> None:
        """Very long node names result in a title truncated to <=30 chars."""
        metadata = ExportService.generate_zim_metadata(
            node_url="https://node.example.org",
            flavour="nopic",
            language_iso3="eng",
            node_name="A Very Long Node Name That Exceeds Everything",
        )
        # May be truncated with ellipsis
        assert len(metadata.title) <= 30

    def test_description_under_80_chars(self) -> None:
        """Generated description is <=80 characters."""
        metadata = ExportService.generate_zim_metadata(
            node_url="https://node.example.org",
            flavour="nopic",
            language_iso3="eng",
            node_name="Open-Repo",
        )
        assert len(metadata.description) <= 80

    def test_scope_label_appears_in_title(self) -> None:
        """Custom scope_label appears in the generated title."""
        metadata = ExportService.generate_zim_metadata(
            node_url="https://node.example.org",
            flavour="agriculture",
            language_iso3="eng",
            node_name="Open-Repo",
            scope_label="Agriculture",
        )
        assert "Agriculture" in metadata.title

    def test_source_url_defaults_to_node_url(self) -> None:
        """source_url defaults to node_url when not explicitly set."""
        metadata = ExportService.generate_zim_metadata(
            node_url="https://node.example.org",
            flavour="nopic",
            language_iso3="eng",
        )
        assert metadata.source_url == "https://node.example.org"

    def test_custom_source_url_overrides_node_url(self) -> None:
        """Explicit source_url overrides node_url."""
        metadata = ExportService.generate_zim_metadata(
            node_url="https://internal.example.org",
            source_url="https://public.example.org",
            flavour="nopic",
            language_iso3="eng",
        )
        assert metadata.source_url == "https://public.example.org"

    def test_custom_tags_preserved(self) -> None:
        """Custom tags are stored in metadata.tags."""
        custom_tags = "offline;water;filtration"
        metadata = ExportService.generate_zim_metadata(
            node_url="https://node.example.org",
            flavour="water",
            language_iso3="eng",
            tags=custom_tags,
        )
        assert metadata.tags == custom_tags


# ---------------------------------------------------------------------------
# 10. validate_zim_output()
# ---------------------------------------------------------------------------


class TestValidateZimOutput:

    def _make_result(
        self,
        tmp_path: Path,
        *,
        sha256: str = "a" * 64,
        article_count: int = 5,
        file_size_bytes: int = 1024,
        generation_duration_seconds: float = 1.0,
        zimcheck_passed: bool = True,
        create_file: bool = True,
    ) -> ZimWriteResult:
        """Helper to create a ZimWriteResult for testing."""
        path = tmp_path / "test.zim"
        if create_file:
            path.write_bytes(b"STUB ZIM")
        return ZimWriteResult(
            output_path=path,
            sha256=sha256,
            article_count=article_count,
            resource_count=0,
            file_size_bytes=file_size_bytes,
            generation_duration_seconds=generation_duration_seconds,
            zimcheck_passed=zimcheck_passed,
            name="open-repo_en_nopic",
            flavour="nopic",
        )

    def test_valid_result_has_no_errors(self, tmp_path: Path) -> None:
        """validate_zim_output() returns empty list for a valid result."""
        result = self._make_result(tmp_path)
        errors = ExportService.validate_zim_output(result)
        assert errors == [], f"Expected no errors: {errors}"

    def test_invalid_sha256_reported(self, tmp_path: Path) -> None:
        """validate_zim_output() reports error for invalid SHA-256."""
        result = self._make_result(tmp_path, sha256="not-a-sha256")
        errors = ExportService.validate_zim_output(result)
        sha_errors = [e for e in errors if "SHA-256" in e or "checksum" in e.lower()]
        assert len(sha_errors) >= 1

    def test_zero_articles_reported(self, tmp_path: Path) -> None:
        """validate_zim_output() reports error for zero article count."""
        result = self._make_result(tmp_path, article_count=0)
        errors = ExportService.validate_zim_output(result)
        count_errors = [e for e in errors if "article" in e.lower()]
        assert len(count_errors) >= 1

    def test_zero_file_size_reported(self, tmp_path: Path) -> None:
        """validate_zim_output() reports error for zero file size."""
        result = self._make_result(tmp_path, file_size_bytes=0)
        errors = ExportService.validate_zim_output(result)
        size_errors = [e for e in errors if "size" in e.lower() or "bytes" in e.lower()]
        assert len(size_errors) >= 1

    def test_negative_duration_reported(self, tmp_path: Path) -> None:
        """validate_zim_output() reports error for negative duration."""
        result = self._make_result(tmp_path, generation_duration_seconds=-1.0)
        errors = ExportService.validate_zim_output(result)
        dur_errors = [e for e in errors if "duration" in e.lower() or "timing" in e.lower()]
        assert len(dur_errors) >= 1

    def test_missing_output_file_reported(self, tmp_path: Path) -> None:
        """validate_zim_output() reports error when output_path does not exist."""
        result = self._make_result(tmp_path, create_file=False)
        errors = ExportService.validate_zim_output(result)
        file_errors = [e for e in errors if "does not exist" in e or "output" in e.lower()]
        assert len(file_errors) >= 1

    def test_zimcheck_failure_reported(self, tmp_path: Path) -> None:
        """validate_zim_output() reports error when zimcheck_passed is False."""
        result = self._make_result(tmp_path, zimcheck_passed=False)
        errors = ExportService.validate_zim_output(result)
        zc_errors = [e for e in errors if "zimcheck" in e.lower()]
        assert len(zc_errors) >= 1

    def test_multiple_errors_accumulated(self, tmp_path: Path) -> None:
        """validate_zim_output() accumulates multiple errors."""
        result = self._make_result(
            tmp_path,
            sha256="bad",
            article_count=0,
            file_size_bytes=0,
            zimcheck_passed=False,
            create_file=False,
        )
        errors = ExportService.validate_zim_output(result)
        assert len(errors) >= 4  # sha256 + article + size + file + zimcheck


# ---------------------------------------------------------------------------
# 11. export_to_zim() — stub DB pipeline
# ---------------------------------------------------------------------------


class TestExportToZim:

    @pytest.mark.asyncio
    async def test_export_produces_output_file(
        self,
        service: ExportService,
        sample_metadata: ZimMetadata,
        sample_config: ExportConfig,
        tmp_path: Path,
    ) -> None:
        """export_to_zim() creates a ZIM file at the output path."""
        output_path = tmp_path / "test_export.zim"
        result = await service.export_to_zim(
            metadata=sample_metadata,
            config=sample_config,
            output_path=output_path,
            zimcheck_binary=None,
            run_zimcheck=False,
        )
        assert result.output_path.exists()

    @pytest.mark.asyncio
    async def test_export_returns_valid_result(
        self,
        service: ExportService,
        sample_metadata: ZimMetadata,
        sample_config: ExportConfig,
        tmp_path: Path,
    ) -> None:
        """export_to_zim() returns a ZimWriteResult with sha256 and article count."""
        result = await service.export_to_zim(
            metadata=sample_metadata,
            config=sample_config,
            output_path=tmp_path / "test.zim",
            zimcheck_binary=None,
            run_zimcheck=False,
        )
        assert result.sha256 is not None
        assert len(result.sha256) == 64
        assert re.match(r"^[0-9a-f]{64}$", result.sha256)

    @pytest.mark.asyncio
    async def test_export_stub_mode_has_index_article(
        self,
        service: ExportService,
        sample_metadata: ZimMetadata,
        sample_config: ExportConfig,
        tmp_path: Path,
    ) -> None:
        """In stub mode (no DB), export produces at least the index article."""
        result = await service.export_to_zim(
            metadata=sample_metadata,
            config=sample_config,
            output_path=tmp_path / "test.zim",
            zimcheck_binary=None,
            run_zimcheck=False,
        )
        # Stub mode: only index article (no DB content)
        assert result.article_count >= 1

    @pytest.mark.asyncio
    async def test_export_result_metadata_matches(
        self,
        service: ExportService,
        sample_metadata: ZimMetadata,
        sample_config: ExportConfig,
        tmp_path: Path,
    ) -> None:
        """Result name and flavour match the provided metadata."""
        result = await service.export_to_zim(
            metadata=sample_metadata,
            config=sample_config,
            output_path=tmp_path / "test.zim",
            zimcheck_binary=None,
            run_zimcheck=False,
        )
        assert result.name == sample_metadata.name
        assert result.flavour == sample_metadata.flavour

    @pytest.mark.asyncio
    async def test_export_validate_passes_for_stub_output(
        self,
        service: ExportService,
        sample_metadata: ZimMetadata,
        sample_config: ExportConfig,
        tmp_path: Path,
    ) -> None:
        """validate_zim_output() passes for the stub ZIM output."""
        result = await service.export_to_zim(
            metadata=sample_metadata,
            config=sample_config,
            output_path=tmp_path / "test.zim",
            zimcheck_binary=None,
            run_zimcheck=False,
        )
        errors = ExportService.validate_zim_output(result)
        # The only expected "error" is zimcheck_passed=True (we skipped it),
        # which is fine — validate_zim_output treats skipped zimcheck as passed.
        assert errors == [], f"Unexpected validation errors: {errors}"

    @pytest.mark.asyncio
    async def test_export_css_resource_included(
        self,
        service: ExportService,
        sample_metadata: ZimMetadata,
        sample_config: ExportConfig,
        tmp_path: Path,
    ) -> None:
        """export_to_zim() adds the shared CSS resource to the ZimWriter."""
        result = await service.export_to_zim(
            metadata=sample_metadata,
            config=sample_config,
            output_path=tmp_path / "test.zim",
            zimcheck_binary=None,
            run_zimcheck=False,
        )
        # CSS is a non-front resource; resource_count should be >= 1
        assert result.resource_count >= 1

    @pytest.mark.asyncio
    async def test_export_invalid_metadata_raises(
        self,
        service: ExportService,
        sample_config: ExportConfig,
        tmp_path: Path,
    ) -> None:
        """export_to_zim() raises ValueError for invalid ZimMetadata."""
        bad_metadata = ZimMetadata(
            title="Test",
            description="A" * 81,  # Exceeds 80-char limit
            language="eng",
            name="open-repo_en_nopic",
            flavour="nopic",
            creator="Test",
            publisher="Test",
            source_url="https://example.org",
        )
        with pytest.raises(ValueError, match="validation failed"):
            await service.export_to_zim(
                metadata=bad_metadata,
                config=sample_config,
                output_path=tmp_path / "bad.zim",
                zimcheck_binary=None,
                run_zimcheck=False,
            )

    @pytest.mark.asyncio
    async def test_export_nonexistent_directory_raises(
        self,
        service: ExportService,
        sample_metadata: ZimMetadata,
        sample_config: ExportConfig,
    ) -> None:
        """export_to_zim() raises FileNotFoundError for nonexistent output directory."""
        with pytest.raises(FileNotFoundError):
            await service.export_to_zim(
                metadata=sample_metadata,
                config=sample_config,
                output_path=Path("/nonexistent/directory/test.zim"),
                zimcheck_binary=None,
                run_zimcheck=False,
            )


# ---------------------------------------------------------------------------
# 12. export_to_zim() — with synthetic content (mock DB)
# ---------------------------------------------------------------------------


class TestExportToZimWithContent:
    """
    Tests that inject synthetic content items via a mock async generator,
    simulating the full pipeline including DB-originated content.
    """

    @pytest.mark.asyncio
    async def test_content_items_reach_zim_writer(
        self,
        sample_metadata: ZimMetadata,
        sample_config: ExportConfig,
        tmp_path: Path,
        procedure_item: dict,
        recipe_item: dict,
    ) -> None:
        """Content items injected via mock are reflected in article_count."""
        service = ExportService(db_session=object())  # non-None DB

        # Patch query_content_items to yield synthetic items
        async def _fake_query(config):
            for item in [procedure_item, recipe_item]:
                yield item

        service.query_content_items = _fake_query  # type: ignore[assignment]

        result = await service.export_to_zim(
            metadata=sample_metadata,
            config=sample_config,
            output_path=tmp_path / "with_content.zim",
            zimcheck_binary=None,
            run_zimcheck=False,
        )
        # 2 content items + 1 index page
        assert result.article_count == 3

    @pytest.mark.asyncio
    async def test_federated_item_attribution_rendered(
        self,
        sample_metadata: ZimMetadata,
        sample_config: ExportConfig,
        tmp_path: Path,
        federated_item: dict,
    ) -> None:
        """Federated items pass source_node_url/name through to ZimWriter."""
        service = ExportService(db_session=object())

        writer_calls: list[dict] = []
        original_add_article = ZimWriter.add_article

        def capturing_add_article(self_writer, **kwargs):
            writer_calls.append(kwargs)
            return original_add_article(self_writer, **kwargs)

        async def _fake_query(config):
            yield federated_item

        service.query_content_items = _fake_query  # type: ignore[assignment]

        with patch.object(ZimWriter, "add_article", capturing_add_article):
            await service.export_to_zim(
                metadata=sample_metadata,
                config=sample_config,
                output_path=tmp_path / "federated.zim",
                zimcheck_binary=None,
                run_zimcheck=False,
            )

        # Check that one of the captured calls has source_node_url set
        federated_calls = [c for c in writer_calls if c.get("source_node_url")]
        assert len(federated_calls) >= 1
        assert federated_calls[0]["source_node_url"] == "https://partner-node.example.org"

    @pytest.mark.asyncio
    async def test_domain_grouping_in_index_page(
        self,
        sample_metadata: ZimMetadata,
        sample_config: ExportConfig,
        tmp_path: Path,
        procedure_item: dict,
        recipe_item: dict,
    ) -> None:
        """Index page reflects domain grouping from content items."""
        service = ExportService(db_session=object())

        async def _fake_query(config):
            yield procedure_item  # domain: "water"
            yield recipe_item    # domain: "recipes"

        service.query_content_items = _fake_query  # type: ignore[assignment]

        # Capture what gets passed to add_article for path "index"
        index_html_captured: list[str] = []
        original = ZimWriter.add_article

        def capturing(self_writer, path, content, **kwargs):
            if path == "index":
                index_html_captured.append(content)
            return original(self_writer, path=path, content=content, **kwargs)

        with patch.object(ZimWriter, "add_article", capturing):
            await service.export_to_zim(
                metadata=sample_metadata,
                config=sample_config,
                output_path=tmp_path / "index_test.zim",
                zimcheck_binary=None,
                run_zimcheck=False,
            )

        assert len(index_html_captured) == 1
        index_html = index_html_captured[0]
        assert "Water" in index_html or "water" in index_html
        assert "Recipes" in index_html or "recipes" in index_html


# ---------------------------------------------------------------------------
# 13. Utility functions
# ---------------------------------------------------------------------------


class TestPickLanguage:

    def test_returns_exact_match(self) -> None:
        assert _pick_language({"en": "Hello", "fr": "Bonjour"}, "fr") == "Bonjour"

    def test_short_code_fallback(self) -> None:
        """'en-US' falls back to 'en' if present."""
        assert _pick_language({"en": "Hello"}, "en-US") == "Hello"

    def test_any_value_fallback(self) -> None:
        """Returns first available value when requested language absent."""
        result = _pick_language({"sw": "Habari"}, "en")
        assert result == "Habari"

    def test_returns_none_for_empty_dict(self) -> None:
        assert _pick_language({}, "en") is None

    def test_non_dict_returns_str(self) -> None:
        """Non-dict input is coerced to string."""
        assert _pick_language("plain string", "en") == "plain string"  # type: ignore[arg-type]

    def test_none_input_returns_none(self) -> None:
        assert _pick_language(None, "en") is None  # type: ignore[arg-type]


class TestEscapeFunction:

    def test_escapes_ampersand(self) -> None:
        assert _escape("A & B") == "A &amp; B"

    def test_escapes_less_than(self) -> None:
        assert _escape("<script>") == "&lt;script&gt;"

    def test_escapes_greater_than(self) -> None:
        assert _escape("1 > 0") == "1 &gt; 0"

    def test_escapes_double_quote(self) -> None:
        assert _escape('He said "hello"') == "He said &quot;hello&quot;"

    def test_escapes_single_quote(self) -> None:
        assert _escape("It's fine") == "It&#x27;s fine"

    def test_safe_string_unchanged(self) -> None:
        safe = "Hello, World! This is open-repo 2026."
        assert _escape(safe) == safe

    def test_non_string_coerced(self) -> None:
        """Non-string inputs are coerced to string before escaping."""
        assert _escape(42) == "42"  # type: ignore[arg-type]

    def test_empty_string(self) -> None:
        assert _escape("") == ""


class TestLicenseUrl:

    def test_cc_by_4(self) -> None:
        url = _license_url("CC-BY-4.0")
        assert url is not None
        assert "creativecommons.org" in url
        assert "by/4.0" in url

    def test_cc_by_sa_4(self) -> None:
        url = _license_url("CC-BY-SA-4.0")
        assert url is not None
        assert "by-sa" in url

    def test_cc0(self) -> None:
        url = _license_url("CC0-1.0")
        assert url is not None
        assert "publicdomain" in url

    def test_mit(self) -> None:
        url = _license_url("MIT")
        assert url is not None
        assert "opensource.org" in url

    def test_apache(self) -> None:
        url = _license_url("Apache-2.0")
        assert url is not None
        assert "apache.org" in url

    def test_unknown_returns_none(self) -> None:
        assert _license_url("UNKNOWN-LICENSE") is None

    def test_empty_returns_none(self) -> None:
        assert _license_url("") is None
