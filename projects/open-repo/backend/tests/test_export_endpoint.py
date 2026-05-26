"""
Tests for POST /api/v1/export and GET /api/v1/export/{export_id}.

Covers:
  - Endpoint accepts valid ZIM export requests and returns 202 with in_progress
  - Validation rejects unsupported formats (non-zim)
  - Validation rejects invalid scope values
  - Validation rejects domain scope without scope_value
  - Validation rejects invalid flavour values
  - 404 returned when no content items match
  - Status poll endpoint returns 404 for unknown export_id
  - Status poll returns in_progress, success, and error states
  - _render_item_html produces valid HTML for a ContentItem-like object
  - _iso2_to_iso3 converts known and unknown language codes
"""

from __future__ import annotations

import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

# ---------------------------------------------------------------------------
# Path setup — mirror conftest.py approach
# ---------------------------------------------------------------------------

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.api.v1.export import (
    ExportRequest,
    ExportResponse,
    _export_jobs,
    _export_jobs_lock,
    _get_job,
    _iso2_to_iso3,
    _render_item_html,
    _set_job,
    router,
)


# ---------------------------------------------------------------------------
# Helper: clear job registry between tests
# ---------------------------------------------------------------------------


@pytest.fixture(autouse=True)
def clear_job_registry():
    """Wipe the in-memory job registry before each test."""
    with _export_jobs_lock:
        _export_jobs.clear()
    yield
    with _export_jobs_lock:
        _export_jobs.clear()


# ---------------------------------------------------------------------------
# Helper: minimal ContentItem-like object
# ---------------------------------------------------------------------------


def _make_item(**kwargs) -> SimpleNamespace:
    defaults = {
        "cid": "sha256-abc123",
        "title": "Biosand Filter Construction",
        "item_type": "procedure",
        "domain": "water",
        "license": "CC-BY-4.0",
        "content_jsonld": {
            "description": {"en": "Step-by-step biosand filter guide"},
            "steps": [
                {
                    "stepNumber": 1,
                    "title": {"en": "Prepare mold"},
                    "body": {"en": "Build a wooden mold"},
                }
            ],
        },
    }
    defaults.update(kwargs)
    return SimpleNamespace(**defaults)


# ---------------------------------------------------------------------------
# Unit tests: helper functions
# ---------------------------------------------------------------------------


class TestRenderItemHtml:

    def test_renders_basic_item(self) -> None:
        """_render_item_html produces a string containing the item title."""
        item = _make_item()
        html = _render_item_html(item)
        assert "Biosand Filter Construction" in html
        assert "<!DOCTYPE html>" in html

    def test_renders_description(self) -> None:
        """_render_item_html includes the English description."""
        item = _make_item()
        html = _render_item_html(item)
        assert "biosand filter guide" in html

    def test_renders_steps(self) -> None:
        """_render_item_html includes step content in an <ol>."""
        item = _make_item()
        html = _render_item_html(item)
        assert "<ol>" in html
        assert "Prepare mold" in html

    def test_handles_no_description(self) -> None:
        """_render_item_html does not crash when description is missing."""
        item = _make_item(content_jsonld={})
        html = _render_item_html(item)
        assert "<!DOCTYPE html>" in html

    def test_handles_string_description(self) -> None:
        """_render_item_html handles string description (non-dict)."""
        item = _make_item(content_jsonld={"description": "Plain text description"})
        html = _render_item_html(item)
        assert "Plain text description" in html

    def test_handles_none_content_jsonld(self) -> None:
        """_render_item_html does not crash when content_jsonld is None."""
        item = _make_item(content_jsonld=None)
        html = _render_item_html(item)
        assert "<!DOCTYPE html>" in html

    def test_output_is_string(self) -> None:
        """_render_item_html always returns a str."""
        item = _make_item()
        html = _render_item_html(item)
        assert isinstance(html, str)


class TestIso2ToIso3:

    def test_english(self) -> None:
        assert _iso2_to_iso3("en") == "eng"

    def test_spanish(self) -> None:
        assert _iso2_to_iso3("es") == "spa"

    def test_arabic(self) -> None:
        assert _iso2_to_iso3("ar") == "ara"

    def test_unknown_code_produces_three_chars(self) -> None:
        """Unknown codes produce a 3-char string."""
        result = _iso2_to_iso3("xx")
        assert len(result) == 3

    def test_case_insensitive(self) -> None:
        assert _iso2_to_iso3("EN") == "eng"


# ---------------------------------------------------------------------------
# Unit tests: job registry helpers
# ---------------------------------------------------------------------------


class TestJobRegistry:

    def test_get_job_returns_none_for_missing_id(self) -> None:
        result = _get_job("nonexistent-id")
        assert result is None

    def test_set_and_get_job(self) -> None:
        _set_job("test-id", {"status": "in_progress"})
        job = _get_job("test-id")
        assert job is not None
        assert job["status"] == "in_progress"

    def test_set_job_overwrites_previous_state(self) -> None:
        _set_job("test-id", {"status": "in_progress"})
        _set_job("test-id", {"status": "success", "download_url": "file:///tmp/out.zim"})
        job = _get_job("test-id")
        assert job["status"] == "success"
        assert "download_url" in job


# ---------------------------------------------------------------------------
# Unit tests: ExportRequest schema validation
# ---------------------------------------------------------------------------


class TestExportRequestSchema:

    def test_default_values(self) -> None:
        req = ExportRequest()
        assert req.format == "zim"
        assert req.scope == "local"
        assert req.flavour == "nopic"
        assert req.language == "en"
        assert req.content_ids is None

    def test_accepts_valid_request(self) -> None:
        req = ExportRequest(
            format="zim",
            content_ids=["sha256-abc", "sha256-def"],
            scope="local",
            flavour="nopic",
            language="en",
        )
        assert req.content_ids == ["sha256-abc", "sha256-def"]

    def test_domain_scope_with_scope_value(self) -> None:
        req = ExportRequest(scope="domain", scope_value="agriculture")
        assert req.scope_value == "agriculture"


# ---------------------------------------------------------------------------
# Integration tests: HTTP endpoint via ASGI transport
# ---------------------------------------------------------------------------


@pytest.fixture
async def export_client():
    """Test client for the export router only, with mocked database."""
    import httpx
    from fastapi import FastAPI
    from app import database

    app = FastAPI()
    app.include_router(router)

    async def mock_get_db():
        session = AsyncMock()
        yield session

    app.dependency_overrides[database.get_db] = mock_get_db

    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        yield client

    app.dependency_overrides.clear()


class TestExportEndpointValidation:

    @pytest.mark.asyncio
    async def test_unsupported_format_returns_400(self, export_client) -> None:
        """Non-zim format triggers 400 Bad Request."""
        response = await export_client.post(
            "/api/v1/export",
            json={"format": "pdf"},
        )
        assert response.status_code == 400
        assert "zim" in response.json()["detail"].lower()

    @pytest.mark.asyncio
    async def test_invalid_scope_returns_400(self, export_client) -> None:
        """Unknown scope triggers 400 Bad Request."""
        response = await export_client.post(
            "/api/v1/export",
            json={"format": "zim", "scope": "planetary"},
        )
        assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_domain_scope_without_scope_value_returns_400(self, export_client) -> None:
        """domain scope without scope_value triggers 400."""
        response = await export_client.post(
            "/api/v1/export",
            json={"format": "zim", "scope": "domain"},
        )
        assert response.status_code == 400
        assert "scope_value" in response.json()["detail"].lower()

    @pytest.mark.asyncio
    async def test_invalid_flavour_returns_400(self, export_client) -> None:
        """Unknown flavour triggers 400 (ExportConfig validation)."""
        response = await export_client.post(
            "/api/v1/export",
            json={"format": "zim", "flavour": "invalid_flavour_xyz"},
        )
        assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_no_items_found_returns_404(self, export_client) -> None:
        """404 when DB returns no content items."""
        # DB mock returns empty list
        from app.api.v1 import export as export_module
        from app import database

        app_inner = export_client._transport.app

        async def mock_get_db_empty():
            session = AsyncMock()
            # scalars().all() returns []
            mock_result = MagicMock()
            mock_result.scalars.return_value.all.return_value = []
            session.execute = AsyncMock(return_value=mock_result)
            yield session

        app_inner.dependency_overrides[database.get_db] = mock_get_db_empty

        response = await export_client.post(
            "/api/v1/export",
            json={"format": "zim"},
        )
        assert response.status_code == 404

        # Restore default override
        async def mock_get_db_default():
            session = AsyncMock()
            yield session

        app_inner.dependency_overrides[database.get_db] = mock_get_db_default

    @pytest.mark.asyncio
    async def test_valid_request_with_items_returns_202(self, export_client) -> None:
        """Valid request with mocked items returns 202 with export_id."""
        from app import database
        from unittest.mock import MagicMock, AsyncMock

        app_inner = export_client._transport.app

        fake_item = _make_item()

        async def mock_get_db_with_items():
            session = AsyncMock()
            mock_result = MagicMock()
            mock_result.scalars.return_value.all.return_value = [fake_item]
            session.execute = AsyncMock(return_value=mock_result)
            yield session

        app_inner.dependency_overrides[database.get_db] = mock_get_db_with_items

        response = await export_client.post(
            "/api/v1/export",
            json={"format": "zim", "flavour": "nopic", "scope": "local"},
        )
        assert response.status_code == 202

        body = response.json()
        assert body["status"] == "in_progress"
        assert "export_id" in body
        assert body["export_id"]  # non-empty
        assert body["poll_url"] is not None
        assert "/api/v1/export/" in body["poll_url"]
        assert body.get("error") is None

        # Restore
        async def mock_get_db_default():
            session = AsyncMock()
            yield session

        app_inner.dependency_overrides[database.get_db] = mock_get_db_default


class TestExportStatusEndpoint:

    @pytest.mark.asyncio
    async def test_unknown_export_id_returns_404(self, export_client) -> None:
        """GET /api/v1/export/{unknown_id} returns 404."""
        response = await export_client.get("/api/v1/export/nonexistent-uuid")
        assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_in_progress_job_returns_in_progress(self, export_client) -> None:
        """Polling a running job returns status=in_progress."""
        job_id = "test-in-progress-job"
        _set_job(job_id, {"status": "in_progress"})

        response = await export_client.get(f"/api/v1/export/{job_id}")
        assert response.status_code == 200
        body = response.json()
        assert body["status"] == "in_progress"
        assert body["export_id"] == job_id

    @pytest.mark.asyncio
    async def test_successful_job_returns_download_url(self, export_client) -> None:
        """Completed job returns status=success with download_url and article_count."""
        job_id = "test-success-job"
        _set_job(job_id, {
            "status": "success",
            "download_url": "file:///tmp/open-repo_en_nopic_2026-05.zim",
            "article_count": 42,
            "file_size_bytes": 102400,
        })

        response = await export_client.get(f"/api/v1/export/{job_id}")
        assert response.status_code == 200
        body = response.json()
        assert body["status"] == "success"
        assert body["download_url"] == "file:///tmp/open-repo_en_nopic_2026-05.zim"
        assert body["article_count"] == 42
        assert body["file_size_bytes"] == 102400
        assert body.get("error") is None

    @pytest.mark.asyncio
    async def test_failed_job_returns_error(self, export_client) -> None:
        """Failed job returns status=error with error message."""
        job_id = "test-failed-job"
        _set_job(job_id, {
            "status": "error",
            "error": "Output directory does not exist: /nonexistent",
        })

        response = await export_client.get(f"/api/v1/export/{job_id}")
        assert response.status_code == 200
        body = response.json()
        assert body["status"] == "error"
        assert "nonexistent" in body["error"]
        assert body.get("download_url") is None
