"""
Integration tests for OPDS REST API endpoints.

Tests the FastAPI OPDS endpoints:
  - GET /opds/v2/root.xml
  - GET /opds/v2/entries
  - GET /opds/v2/entry/{uuid}
  - GET /opds/v2/searchdescription.xml
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from datetime import datetime
from unittest.mock import AsyncMock, Mock, patch

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.main import create_app
from app.models import ZimExport


@pytest.fixture
async def async_client() -> AsyncClient:
    """Create an async HTTP client for testing."""
    app = create_app()
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture
def mock_zim_export() -> ZimExport:
    """Create a mock ZimExport ORM object."""
    export = Mock(spec=ZimExport)
    export.id = 1
    export.zim_uuid = "550e8400-e29b-41d4-a716-446655440000"
    export.title = "Open-Repo: Full Library (English)"
    export.name = "open-repo_en_nopic"
    export.flavour = "nopic"
    export.language = "eng"
    export.period = "2026-05"
    export.description = "Full knowledge base without images"
    export.cdn_url = "https://cdn.example.org/open-repo_en_nopic_2026-05.zim"
    export.file_size_bytes = 2147483648
    export.sha256 = "abc123def456abc123def456abc123def456abc123def456abc123def456abc1"
    export.article_count = 12345
    export.completed_at = datetime(2026, 5, 1, 2, 3, 14)
    export.created_at = datetime(2026, 5, 1, 0, 0, 0)
    export.is_current = True
    export.is_reference = False
    return export


# Note: These tests are marked as integration tests because they require
# database mocking or a test database. In a full CI/CD environment, we would
# use a test PostgreSQL database or Docker container for these tests.
# For now, we test the core generator logic in test_opds_generator.py
# and these tests demonstrate the endpoint structure.


@pytest.mark.integration
class TestOPDSEndpoints:
    """Integration tests for OPDS endpoints."""

    @pytest.mark.asyncio
    async def test_root_catalog_endpoint_structure(self) -> None:
        """Test that /opds/v2/root.xml endpoint structure is correct."""
        # Note: This test demonstrates the endpoint exists
        # Full integration testing requires a database or mock
        app = create_app()
        from app.api.v1.opds import router

        assert router is not None
        # Check that routes are defined
        routes = [route.path for route in app.routes]
        assert any("/opds/v2/root.xml" in route for route in routes)
        assert any("/opds/v2/entries" in route for route in routes)

    @pytest.mark.asyncio
    async def test_acquisition_feed_endpoint_structure(self) -> None:
        """Test that /opds/v2/entries endpoint structure is correct."""
        app = create_app()
        routes = [route.path for route in app.routes]
        assert any("/opds/v2/entries" in route for route in routes)

    @pytest.mark.asyncio
    async def test_single_entry_endpoint_structure(self) -> None:
        """Test that /opds/v2/entry/{uuid} endpoint exists."""
        app = create_app()
        routes = [route.path for route in app.routes]
        # The route should be /opds/v2/entry/{entry_uuid}
        assert any("entry_uuid" in route for route in routes)

    @pytest.mark.asyncio
    async def test_search_description_endpoint_structure(self) -> None:
        """Test that /opds/v2/searchdescription.xml endpoint exists."""
        app = create_app()
        routes = [route.path for route in app.routes]
        assert any("searchdescription.xml" in route for route in routes)


# Manual endpoint tests using mock database
@pytest.mark.integration
class TestOPDSEndpointsMocked:
    """OPDS endpoint tests with mocked database."""

    @pytest.mark.asyncio
    async def test_get_opds_generator_function(self, mock_zim_export: ZimExport) -> None:
        """Test the get_opds_generator dependency function."""
        from app.api.v1.opds import get_opds_generator

        # Create a mock database session with proper async behavior
        mock_db = AsyncMock(spec=AsyncSession)

        # Mock the query result
        mock_result = Mock()
        mock_result.scalars.return_value.all.return_value = [mock_zim_export]

        # Make execute return the result directly (not a coroutine)
        async def mock_execute(*args, **kwargs):
            return mock_result

        mock_db.execute = mock_execute

        generator = await get_opds_generator(mock_db)

        # Verify the generator was created with the entry
        assert generator is not None
        assert generator.entry_count() == 1
        assert generator.get_entry_by_name("open-repo_en_nopic") is not None

    @pytest.mark.asyncio
    async def test_root_catalog_response_format(self, mock_zim_export: ZimExport) -> None:
        """Test that root catalog response has correct format."""
        from app.api.v1.opds import get_opds_root_catalog

        # Create a mock database session
        mock_db = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalars.return_value.all.return_value = [mock_zim_export]

        async def mock_execute(*args, **kwargs):
            return mock_result

        mock_db.execute = mock_execute

        # Call the endpoint
        response = await get_opds_root_catalog(mock_db)

        # Response should be a tuple of (bytes, dict)
        assert isinstance(response, tuple)
        assert len(response) == 2

        xml_bytes, headers = response
        assert isinstance(xml_bytes, bytes)
        assert isinstance(headers, dict)
        assert "media_type" in headers
        assert "opds-catalog" in headers["media_type"]

        # Verify XML is valid
        root = ET.fromstring(xml_bytes)
        assert root.tag.endswith("feed")

    @pytest.mark.asyncio
    async def test_acquisition_feed_response_format(self, mock_zim_export: ZimExport) -> None:
        """Test that acquisition feed response has correct format."""
        from app.api.v1.opds import get_opds_acquisition_feed

        # Create a mock database session
        mock_db = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalars.return_value.all.return_value = [mock_zim_export]

        async def mock_execute(*args, **kwargs):
            return mock_result

        mock_db.execute = mock_execute

        # Call the endpoint
        response = await get_opds_acquisition_feed(mock_db)

        # Response should be a tuple of (bytes, dict)
        assert isinstance(response, tuple)
        assert len(response) == 2

        xml_bytes, headers = response
        assert isinstance(xml_bytes, bytes)
        assert "media_type" in headers
        assert "acquisition" in headers["media_type"]

        # Verify XML is valid
        root = ET.fromstring(xml_bytes)
        assert root.tag.endswith("feed")

        # Should contain the entry
        ns = "{http://www.w3.org/2005/Atom}"
        entries = root.findall(f"{ns}entry")
        assert len(entries) >= 1

    @pytest.mark.asyncio
    async def test_single_entry_response_format(self, mock_zim_export: ZimExport) -> None:
        """Test that single entry response has correct format."""
        from app.api.v1.opds import get_opds_single_entry

        # Create a mock database session
        mock_db = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalars.return_value.all.return_value = [mock_zim_export]

        async def mock_execute(*args, **kwargs):
            return mock_result

        mock_db.execute = mock_execute

        # Call the endpoint with the correct UUID
        response = await get_opds_single_entry(mock_zim_export.zim_uuid, mock_db)

        # Response should be a tuple of (bytes, dict)
        assert isinstance(response, tuple)
        assert len(response) == 2

        xml_bytes, headers = response
        assert isinstance(xml_bytes, bytes)

        # Verify XML is valid
        root = ET.fromstring(xml_bytes)
        assert root.tag.endswith("feed")

    @pytest.mark.asyncio
    async def test_single_entry_not_found(self, mock_zim_export: ZimExport) -> None:
        """Test that single entry returns 404 for non-existent UUID."""
        from fastapi import HTTPException

        from app.api.v1.opds import get_opds_single_entry

        # Create a mock database session
        mock_db = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalars.return_value.all.return_value = [mock_zim_export]

        async def mock_execute(*args, **kwargs):
            return mock_result

        mock_db.execute = mock_execute

        # Call with a non-existent UUID
        non_existent_uuid = "00000000-0000-0000-0000-000000000000"

        with pytest.raises(HTTPException) as exc_info:
            await get_opds_single_entry(non_existent_uuid, mock_db)

        assert exc_info.value.status_code == 404

    @pytest.mark.asyncio
    async def test_search_description_response_format(self) -> None:
        """Test that search description response has correct format."""
        from app.api.v1.opds import get_opds_search_description

        # Create a mock database session
        mock_db = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalars.return_value.all.return_value = []

        async def mock_execute(*args, **kwargs):
            return mock_result

        mock_db.execute = mock_execute

        # Call the endpoint
        response = await get_opds_search_description(mock_db)

        # Response should be a tuple of (bytes, dict)
        assert isinstance(response, tuple)
        assert len(response) == 2

        xml_bytes, headers = response
        assert isinstance(xml_bytes, bytes)
        assert "opensearchdescription+xml" in headers["media_type"]

        # Verify XML is valid
        root = ET.fromstring(xml_bytes)
        assert "OpenSearchDescription" in root.tag
