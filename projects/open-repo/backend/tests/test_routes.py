"""Tests for API routes - validation and endpoint structure."""

import pytest
from httpx import AsyncClient
from pydantic import ValidationError


@pytest.mark.asyncio
async def test_health_check(client: AsyncClient):
    """Test health check endpoint exists."""
    response = await client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "version" in data


@pytest.mark.asyncio
async def test_root_endpoint(client: AsyncClient):
    """Test root endpoint."""
    response = await client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Open-Repo API"


def test_validation_required_title():
    """Test that title is required."""
    from app.schemas import ContentItemCreateRequest

    with pytest.raises(ValidationError):
        ContentItemCreateRequest(
            type="procedure",
            domain="procedural",
            license="CC-BY-4.0",
        )


def test_validation_required_type():
    """Test that type is required."""
    from app.schemas import ContentItemCreateRequest

    with pytest.raises(ValidationError):
        ContentItemCreateRequest(
            title={"en": "Test"},
            domain="procedural",
            license="CC-BY-4.0",
        )


def test_validation_required_domain():
    """Test that domain is required."""
    from app.schemas import ContentItemCreateRequest

    with pytest.raises(ValidationError):
        ContentItemCreateRequest(
            title={"en": "Test"},
            type="procedure",
            license="CC-BY-4.0",
        )


def test_validation_required_license():
    """Test that license is required."""
    from app.schemas import ContentItemCreateRequest

    with pytest.raises(ValidationError):
        ContentItemCreateRequest(
            title={"en": "Test"},
            type="procedure",
            domain="procedural",
        )


def test_validation_invalid_type():
    """Test that invalid types are rejected."""
    from app.schemas import ContentItemCreateRequest

    with pytest.raises(ValidationError):
        ContentItemCreateRequest(
            title={"en": "Test"},
            type="invalid_type",
            domain="procedural",
            license="CC-BY-4.0",
        )


def test_validation_valid_types(sample_procedure, sample_recipe):
    """Test that all valid types are accepted."""
    from app.schemas import ContentItemCreateRequest

    valid_types = ["procedure", "recipe", "schematic", "plan", "service-listing"]

    for valid_type in valid_types:
        item = sample_procedure.copy()
        item["type"] = valid_type
        # Should not raise
        ContentItemCreateRequest(**item)


def test_validation_multilingual_title():
    """Test multilingual title support."""
    from app.schemas import ContentItemCreateRequest

    item = {
        "title": {
            "en": "English title",
            "es": "Título en español",
            "sw": "Kichwa cha kiswahili",
        },
        "type": "procedure",
        "domain": "procedural",
        "license": "CC-BY-4.0",
        "language": ["en", "es", "sw"],
    }

    request = ContentItemCreateRequest(**item)
    assert request.title["en"] == "English title"
    assert request.title["es"] == "Título en español"
    assert request.title["sw"] == "Kichwa cha kiswahili"


def test_validation_language_codes():
    """Test language codes are accepted."""
    from app.schemas import ContentItemCreateRequest

    item = {
        "title": {"en": "Test"},
        "type": "procedure",
        "domain": "procedural",
        "license": "CC-BY-4.0",
        "language": ["en", "es", "sw", "am", "fr"],
    }

    request = ContentItemCreateRequest(**item)
    assert request.language == ["en", "es", "sw", "am", "fr"]


def test_validation_tags_array():
    """Test tags array support."""
    from app.schemas import ContentItemCreateRequest

    item = {
        "title": {"en": "Test"},
        "type": "procedure",
        "domain": "procedural",
        "license": "CC-BY-4.0",
        "tags": ["water", "filtration", "sanitation", "DIY"],
    }

    request = ContentItemCreateRequest(**item)
    assert len(request.tags) == 4


def test_validation_procedure_specific_fields(sample_procedure):
    """Test procedure-specific fields."""
    from app.schemas import ContentItemCreateRequest

    request = ContentItemCreateRequest(**sample_procedure)
    assert request.outcome is not None
    assert request.difficulty == "beginner"
    assert request.timeRequired is not None


def test_validation_recipe_specific_fields(sample_recipe):
    """Test recipe-specific fields."""
    from app.schemas import ContentItemCreateRequest

    request = ContentItemCreateRequest(**sample_recipe)
    assert request.category == "food"
    assert request.subcategory == "grain-preservation"


def test_validation_attribution():
    """Test attribution structure."""
    from app.schemas import ContentItemCreateRequest

    item = {
        "title": {"en": "Test"},
        "type": "procedure",
        "domain": "procedural",
        "license": "CC-BY-4.0",
        "attribution": {
            "source": "https://example.org",
            "sourceTitle": "Example Source",
            "author": "John Doe",
        },
    }

    request = ContentItemCreateRequest(**item)
    assert request.attribution.source == "https://example.org"
    assert request.attribution.sourceTitle == "Example Source"


def test_validation_cost_estimate():
    """Test cost estimate structure."""
    from app.schemas import ContentItemCreateRequest

    item = {
        "title": {"en": "Test"},
        "type": "procedure",
        "domain": "procedural",
        "license": "CC-BY-4.0",
        "costEstimate": {
            "materials": {"USD": 25, "year": 2025},
            "labor": {"hours": 6, "skilled": False},
        },
    }

    request = ContentItemCreateRequest(**item)
    assert request.costEstimate is not None


def test_validation_wikidata_links():
    """Test wikidata links array."""
    from app.schemas import ContentItemCreateRequest

    item = {
        "title": {"en": "Test"},
        "type": "procedure",
        "domain": "procedural",
        "license": "CC-BY-4.0",
        "wikidataLinks": ["Q3284", "Q948", "Q12345"],
    }

    request = ContentItemCreateRequest(**item)
    assert len(request.wikidataLinks) == 3


def test_validation_time_required_iso8601():
    """Test ISO 8601 duration format for timeRequired."""
    from app.schemas import ContentItemCreateRequest

    item = {
        "title": {"en": "Test"},
        "type": "procedure",
        "domain": "procedural",
        "license": "CC-BY-4.0",
        "timeRequired": {
            "preparation": "PT2H",
            "execution": "PT6H",
            "curing": "P30D",
        },
    }

    request = ContentItemCreateRequest(**item)
    assert request.timeRequired is not None


def test_validation_steps_structure(sample_procedure):
    """Test procedure steps structure."""
    from app.schemas import ContentItemCreateRequest

    request = ContentItemCreateRequest(**sample_procedure)
    assert len(request.steps) > 0
    assert request.steps[0].stepNumber == 1
    assert "en" in request.steps[0].title


def test_validation_materials_array():
    """Test materials array."""
    from app.schemas import ContentItemCreateRequest

    item = {
        "title": {"en": "Test"},
        "type": "procedure",
        "domain": "procedural",
        "license": "CC-BY-4.0",
        "materials": [
            {"name": "Portland cement", "quantity": "40 kg"},
            {"name": "Sand", "quantity": "20 kg"},
        ],
    }

    request = ContentItemCreateRequest(**item)
    assert len(request.materials) == 2


def test_validation_ingredients_array():
    """Test ingredients array for recipes."""
    from app.schemas import ContentItemCreateRequest

    item = {
        "title": {"en": "Test Recipe"},
        "type": "recipe",
        "domain": "procedural",
        "license": "CC0-1.0",
        "ingredients": [
            {"name": {"en": "Wheat"}, "quantity": "5 kg"},
            {"name": {"en": "Salt"}, "quantity": "1 tsp"},
        ],
    }

    request = ContentItemCreateRequest(**item)
    assert len(request.ingredients) == 2


def test_cid_computation_is_consistent():
    """Test that CID computation is deterministic."""
    from app.routes import compute_cid

    content1 = {"title": {"en": "Test"}, "domain": "procedural", "type": "procedure"}
    content2 = {"title": {"en": "Test"}, "domain": "procedural", "type": "procedure"}

    cid1 = compute_cid(content1)
    cid2 = compute_cid(content2)

    assert cid1 == cid2


def test_cid_computation_format():
    """Test that CID has correct format."""
    from app.routes import compute_cid

    content = {"title": {"en": "Test"}, "domain": "procedural", "type": "procedure"}
    cid = compute_cid(content)

    assert cid.startswith("sha256-")
    assert len(cid) == 71  # "sha256-" (7 chars) + 64 hex chars


def test_response_model_structure():
    """Test ContentItemResponse model structure."""
    from app.schemas import ContentItemResponse
    from datetime import datetime

    response_data = {
        "cid": "sha256-abc123",
        "title": {"en": "Test"},
        "item_type": "procedure",
        "domain": "procedural",
        "license": "CC-BY-4.0",
        "language": ["en"],
        "tags": ["test"],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
        "content_jsonld": {"@type": "procedure", "title": {"en": "Test"}},
    }

    response = ContentItemResponse(**response_data)
    assert response.cid == "sha256-abc123"
    assert response.item_type == "procedure"


def test_list_response_model():
    """Test ContentItemsListResponse model."""
    from app.schemas import ContentItemsListResponse, ContentItemResponse
    from datetime import datetime

    items_data = [
        {
            "cid": "sha256-abc123",
            "title": {"en": "Test"},
            "item_type": "procedure",
            "domain": "procedural",
            "license": "CC-BY-4.0",
            "language": ["en"],
            "tags": ["test"],
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "content_jsonld": {"@type": "procedure"},
        }
    ]

    response = ContentItemsListResponse(
        items=[ContentItemResponse(**item) for item in items_data],
        total=1,
        limit=10,
        offset=0,
        has_more=False,
    )

    assert response.total == 1
    assert len(response.items) == 1
