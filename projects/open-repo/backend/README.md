# Open-Repo MVP Backend

**Status**: Phase 1 Complete - FastAPI + PostgreSQL CRUD scaffolding

**Version**: 0.1.0

A minimal FastAPI backend for the Open-Repo federated knowledge network. Phase 1 implements CRUD endpoints for content items with JSON-LD validation against the schema defined in `../mvp-protocol-design.md`.

## What's Implemented

### Endpoints (3 core routes)
- `POST /api/items` - Create a new content item (procedure, recipe, schematic, plan, or service-listing)
- `GET /api/items/{cid}` - Retrieve a single item by Content Identifier
- `GET /api/items` - List items with pagination and filters (type, domain, tags)

### Schema & Validation
- Pydantic models for JSON-LD validation against OpenRepoItem schema
- Support for 5 content types: procedure, recipe, schematic, plan, service-listing
- Multilingual support (en, es, sw, etc.)
- CID (Content Identifier) computation using SHA256 hashing
- Full JSON-LD object generation and storage

### Database
- SQLAlchemy async models for PostgreSQL
- Single table: `content_items` with CID as primary key
- Indexed fields: cid, title, item_type, domain, created_at
- JSON column for full JSON-LD content

### Tests
- **24 passing tests** covering:
  - Required field validation
  - Type validation (procedure, recipe, etc.)
  - Multilingual content
  - Procedure-specific fields (steps, materials, tools, etc.)
  - Recipe-specific fields (ingredients, yield, storage)
  - CID computation and format
  - Response model structure
  - Pagination model
  - Health check endpoint

## Quick Start

### Setup

```bash
# Navigate to backend directory
cd projects/open-repo/backend

# Install dependencies (FastAPI, SQLAlchemy, Pydantic, pytest, etc.)
uv pip install -e ".[dev]"

# Or manually:
uv pip install fastapi uvicorn pydantic sqlalchemy asyncpg pytest pytest-asyncio httpx
```

### Database Setup

```bash
# Create PostgreSQL database
createdb open_repo

# Or with Docker:
docker run -d \
  --name open_repo_db \
  -e POSTGRES_DB=open_repo \
  -e POSTGRES_PASSWORD=postgres \
  -p 5432:5432 \
  postgres:16

# Set environment variable
export DATABASE_URL="postgresql+asyncpg://postgres:postgres@localhost:5432/open_repo"
```

### Run Development Server

```bash
# Start the server with auto-reload
uv run uvicorn app.main:create_app --reload --host 0.0.0.0 --port 8000

# Server will be available at http://localhost:8000
# Interactive API docs at http://localhost:8000/docs
# ReDoc at http://localhost:8000/redoc
```

### Run Tests

```bash
# Run all tests
uv run pytest tests/ -v

# Run specific test file
uv run pytest tests/test_routes.py -v

# Run with coverage
uv run pytest tests/ --cov=app --cov-report=html
```

### Load Seed Data

```bash
# Load 32 OpenFarm growing guides into the database
uv run python scripts/load_seed_data.py

# This loads from ../data/openfarm_procedures.jsonl
# Items: 32 crops (potatoes, garlic, lettuce, strawberries, carrots, etc.)
```

## API Usage

### Create an Item

```bash
curl -X POST http://localhost:8000/api/items \
  -H "Content-Type: application/json" \
  -d '{
    "title": {"en": "Growing Potatoes"},
    "type": "procedure",
    "domain": "procedural",
    "license": "CC-BY-4.0",
    "language": ["en"],
    "difficulty": "beginner",
    "outcome": {"en": "Healthy potato harvest"},
    "steps": [
      {
        "stepNumber": 1,
        "title": {"en": "Prepare seed"},
        "body": {"en": "Set seed potatoes to sprout..."}
      }
    ],
    "tags": ["agriculture", "potato"],
    "attribution": {
      "source": "https://openfarm.cc",
      "sourceTitle": "OpenFarm"
    }
  }'
```

**Response** (201 Created):
```json
{
  "cid": "sha256-4a35babef40b26cf425e6f535754556822cfcef58ddb7db812a7ff0c60c5ebc3",
  "title": {"en": "Growing Potatoes"},
  "item_type": "procedure",
  "domain": "procedural",
  "license": "CC-BY-4.0",
  "language": ["en"],
  "tags": ["agriculture", "potato"],
  "created_at": "2026-04-26T03:45:23.123456",
  "updated_at": "2026-04-26T03:45:23.123456",
  "content_jsonld": {
    "@context": [...],
    "@type": "procedure",
    "cid": "sha256-4a35...",
    ...
  }
}
```

### Get an Item

```bash
curl http://localhost:8000/api/items/sha256-4a35babef40b26cf425e6f535754556822cfcef58ddb7db812a7ff0c60c5ebc3
```

### List Items

```bash
# All items, default pagination (limit=10, offset=0)
curl http://localhost:8000/api/items

# With custom pagination
curl "http://localhost:8000/api/items?limit=50&offset=0"

# Filter by type
curl "http://localhost:8000/api/items?item_type=procedure"

# Filter by tags
curl "http://localhost:8000/api/items?tags=water,filtration"

# Combined filters
curl "http://localhost:8000/api/items?item_type=procedure&domain=procedural&limit=20"
```

## Project Structure

```
backend/
├── app/
│   ├── __init__.py           # Package metadata
│   ├── main.py               # FastAPI app factory
│   ├── database.py           # AsyncPG connection and session management
│   ├── models.py             # SQLAlchemy ORM models
│   ├── schemas.py            # Pydantic validation models
│   └── routes.py             # API endpoints (POST/GET /api/items)
├── scripts/
│   └── load_seed_data.py     # OpenFarm data loader
├── tests/
│   ├── conftest.py           # Pytest fixtures (sample data, client)
│   └── test_routes.py        # 24 validation and routing tests
├── pyproject.toml            # Project metadata and dependencies
├── API.md                    # Full API documentation
└── README.md                 # This file
```

## Content Types

### Procedure
Structured how-to guides with steps, materials, tools, and verification points.

**Example fields**: `outcome`, `difficulty`, `timeRequired`, `steps`, `materials`, `tools`, `safetyNotes`, `performanceData`

### Recipe
Food/beverage/medicine preparation with ingredients and storage.

**Example fields**: `category`, `ingredients`, `yield`, `storageInstructions`, `foodSafety`

### Schematic
Technical drawings or CAD files (circuit diagrams, mechanical designs, etc.).

**Example fields**: `schematicType`, `blobs`, `billOfMaterials`, `specification`

### Plan
Spatial/architectural documents (building plans, garden layouts, site designs).

**Example fields**: `planType`, `scale`, `dimensions`, `blobs`, `estimatedCost`

### Service Listing
Human exchange listings (skills, services, resources within a community).

**Example fields**: `offerType`, `category`, `provider`, `location`, `availability`

## Database Schema

```sql
CREATE TABLE content_items (
    cid VARCHAR(255) PRIMARY KEY,
    title VARCHAR(500) NOT NULL,
    item_type VARCHAR(50) NOT NULL,
    domain VARCHAR(50) NOT NULL,
    license VARCHAR(50) NOT NULL,
    content_jsonld JSON NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    source_url VARCHAR(500),
    source_title VARCHAR(255)
);

CREATE INDEX idx_item_type ON content_items(item_type);
CREATE INDEX idx_domain ON content_items(domain);
CREATE INDEX idx_created_at ON content_items(created_at);
```

## Environment Variables

```bash
# PostgreSQL connection
export DATABASE_URL="postgresql+asyncpg://user:password@localhost:5432/open_repo"

# Debug SQL queries
export SQL_ECHO="true"
```

## Testing

The test suite covers:
- ✅ Required field validation (title, type, domain, license)
- ✅ Type validation (only 5 allowed types)
- ✅ Multilingual support (en, es, sw, etc.)
- ✅ Procedure-specific fields
- ✅ Recipe-specific fields
- ✅ Attribution and licensing
- ✅ Cost estimates and performance data
- ✅ CID computation (deterministic, correct format)
- ✅ Response model structure
- ✅ Pagination model

Run all tests:
```bash
uv run pytest tests/ -v
```

## Next Phases

**Phase 2** (Search + Endorsements):
- Meilisearch integration for full-text search
- Endorsement object support and propagation
- `GET /api/items/{cid}/endorsements` endpoint

**Phase 3** (Contributions):
- Anonymous contribution submissions
- Review workflow and moderation queue
- Draft state for unpublished items

**Phase 4+** (Federation):
- ActivityPub inbox/outbox implementation
- Node discovery via `.well-known/webfinger`
- Content propagation and sync across federated nodes

## Important Notes

- **Phase 1 scope**: CRUD only. No search, endorsements, or federation yet.
- **Authentication**: Not implemented. All endpoints are public. Will add DID-based auth in future phases.
- **Database**: Uses async SQLAlchemy with asyncpg driver for PostgreSQL.
- **JSON-LD**: Full JSON-LD objects are generated and stored with every item for federation compatibility.
- **CID Format**: SHA256-based (`sha256-{hex}`). IPFS-compatible for future blob storage.

## Development Guide

### Adding a New Endpoint

1. Add validation schema to `app/schemas.py`
2. Implement route handler in `app/routes.py`
3. Add tests in `tests/test_routes.py`
4. Update `API.md` documentation

### Running Code Quality Checks

```bash
# Lint with ruff
uv run ruff check app/

# Format code
uv run ruff format app/
```

## License

This backend implementation is part of the Open-Repo project. See `../../LICENSE` for details.

## References

- **Protocol Design**: `../mvp-protocol-design.md` (711 lines, complete JSON-LD schemas)
- **Seed Data**: `../data/openfarm_procedures.jsonl` (32 crops, 100% schema-compliant)
- **Architecture**: Open-Repo federated knowledge network (Phase 1-5 roadmap)
