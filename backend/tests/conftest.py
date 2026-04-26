"""Pytest configuration and fixtures."""

import os
import pytest
import httpx
from httpx import AsyncClient
from unittest.mock import AsyncMock, MagicMock, patch


@pytest.fixture
async def client():
    """Create test client with mocked database and search service."""
    from app.main import create_app
    from app import database
    from app.services.search_service import reset_search_service

    # Reset search service
    reset_search_service()

    # Mock the get_db dependency
    async def mock_get_db():
        session = AsyncMock()
        yield session

    app = create_app()
    app.dependency_overrides[database.get_db] = mock_get_db

    async with AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        yield ac

    app.dependency_overrides.clear()
    reset_search_service()


@pytest.fixture
def sample_procedure():
    """Sample procedure for testing."""
    return {
        "title": {"en": "How to build a biosand filter"},
        "type": "procedure",
        "domain": "procedural",
        "license": "CC-BY-4.0",
        "description": {"en": "A slow-sand biofilm filter for drinking water"},
        "language": ["en"],
        "difficulty": "beginner",
        "outcome": {"en": "A functioning water filter"},
        "timeRequired": {"execution": "PT6H"},
        "steps": [
            {
                "stepNumber": 1,
                "title": {"en": "Prepare the concrete shell"},
                "body": {"en": "Mix cement and aggregate at 1:3 ratio"},
            }
        ],
        "tags": ["water", "filtration", "DIY"],
        "attribution": {
            "source": "https://example.org/filter",
            "sourceTitle": "Filter Manual",
        },
    }


@pytest.fixture
def sample_recipe():
    """Sample recipe for testing."""
    return {
        "title": {"en": "Grain preservation guide"},
        "type": "recipe",
        "domain": "procedural",
        "license": "CC0-1.0",
        "description": {"en": "How to preserve grain for long-term storage"},
        "language": ["en"],
        "category": "food",
        "subcategory": "grain-preservation",
        "yield": {"quantity": "4", "unit": "kg"},
        "difficulty": "beginner",
        "ingredients": [
            {"name": {"en": "Wheat grain"}, "quantity": "5 kg"}
        ],
        "steps": [
            {
                "stepNumber": 1,
                "title": {"en": "Dry the grain"},
                "body": {"en": "Sun dry for several days"},
            }
        ],
        "tags": ["preservation", "storage"],
    }
