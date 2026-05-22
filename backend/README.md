# Open-Repo Backend

**Status**: Phase 5.1 Complete - ZimWriter libzim integration for offline export (ZIM/Kiwix)

**Version**: 0.5.0

A full-stack FastAPI backend for the Open-Repo federated knowledge network. Phase 5.1 delivers production-ready offline export via ZIM archives (readable by Kiwix on any device), building on Phase 4's federation infrastructure. Content items from any federated node can be exported to a single searchable offline file for use in disconnected environments.

## What's Implemented

### Endpoints (30+ routes)

**Phase 1 - CRUD**:
- `POST /api/items` - Create a new content item (procedure, recipe, schematic, plan, or service-listing)
- `GET /api/items/{cid}` - Retrieve a single item by Content Identifier
- `GET /api/items` - List items with pagination and filters (type, domain, tags)

**Phase 2 - Search + Endorsements**:
- `GET /api/items/search` - Full-text search with Meilisearch
- `POST /api/items/{cid}/endorse` - Submit endorsement (upvote/downvote/flag)
- `GET /api/items/{cid}/endorsements` - Get endorsement statistics
- `GET /api/items/{cid}/endorsements/my-endorsement` - Get user's endorsement
- `DELETE /api/items/{cid}/endorsements/my-endorsement` - Delete user's endorsement
- `GET /admin/items/{cid}/endorsements` - Admin audit log

**Phase 4 - Federation + Export**:
- `POST /api/federation/partners` - Register federated partner node
- `GET /api/federation/partners` - List registered partners
- `GET /api/federation/partners/{partner_id}` - Get partner details
- `POST /api/federation/inbox` - Receive federated activities (HTTP signature verified)
- `GET /api/federation/.well-known/webfinger` - Node discovery endpoint
- `POST /api/export/zim` - Generate ZIM archive for offline distribution
- `GET /api/export/opds` - Generate OPDS 1.2 catalog for Kiwix client
- `GET /admin/federation` - Federation status dashboard
- `GET /admin/conflicts` - View concurrent-edit conflict log

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
- **194 passing tests** (4 skipped, 0 failures) covering:
  - Required field validation (title, type, domain, license)
  - Type validation (procedure, recipe, schematic, plan, service-listing)
  - Multilingual content support
  - Procedure-specific fields (steps, materials, tools, difficulty, etc.)
  - Recipe-specific fields (ingredients, yield, storage, category)
  - CID computation and format (deterministic SHA256)
  - Response model structure and serialization
  - Pagination and filtering
  - Health check endpoint
  - Search response schemas and filtering
  - Endorsement type validation and schemas
  - Endorsement statistics aggregation
  - Endorsement service CRUD operations
  - Search service initialization and singleton pattern

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
uv run uvicorn app.main:create_app --reload --host 127.0.0.1 --port 8000

# Server will be available at http://127.0.0.1:8000
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
│   ├── __init__.py                    # Package metadata
│   ├── main.py                        # FastAPI app factory
│   ├── database.py                    # AsyncPG connection and session management
│   ├── models.py                      # SQLAlchemy ORM models
│   ├── schemas.py                     # Pydantic validation models
│   ├── http_signatures.py             # RFC 9421 signature verification & signing
│   ├── routes.py                      # API endpoints (CRUD)
│   ├── api/
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── items.py               # Item CRUD routes
│   │       ├── search.py              # Search routes
│   │       ├── endorsements.py        # Endorsement routes
│   │       └── federation.py          # Partner registration, federation routes
│   └── services/
│       ├── __init__.py
│       ├── search_service.py          # Meilisearch integration
│       ├── endorsement_service.py     # Endorsement logic
│       ├── federation_service.py      # Federation coordination
│       ├── http_signatures.py         # Signature verification service
│       └── export/
│           ├── zim_writer.py          # ZIM archive writer (libzim integration)
│           ├── opds_generator.py      # OPDS catalog generator
│           └── config.py              # Export configuration
├── scripts/
│   └── load_seed_data.py              # OpenFarm data loader
├── tests/
│   ├── conftest.py                    # Pytest fixtures
│   ├── unit/
│   │   └── test_*.py                  # Unit tests for services
│   ├── integration/
│   │   └── test_*.py                  # Integration tests
│   └── admin/
│       └── test_*.py                  # Admin route tests
├── pyproject.toml                     # Project metadata and dependencies
├── API.md                             # Full API documentation (Wave 4 updated)
└── README.md                          # This file
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

## What's Complete

### Phase 5.1 — Offline Export (ZIM/Kiwix)

The export pipeline is production-ready:

- **ZimWriter** (`app/services/export/zim_writer.py`): Generates valid `.zim` archives using python-libzim. Supports Xapian full-text indexing, federated attribution footers with sanitised HTML, and graceful fallback when libzim is unavailable. Produces archives compatible with Kiwix on Android, iOS, desktop, and kiwix-serve.
- **OPDS 1.2 catalog** (`app/services/export/opds_generator.py`): Raw XML generation of a complete OPDS feed listing all published ZIM archives. Kiwix clients discover archives via this feed.
- **zim_exports table** (migration 003): Tracks every ZIM export lifecycle (GENERATING → COMPLETE → SUPERSEDED). `ZimExport` ORM model in `app/models.py`.
- **84 integration tests** in `tests/integration/test_export_pipeline.py` covering ZimWriter, OPDS, and the full export pipeline.

### Phase 5.2 — Domain Content Modules (June–July 2026)

Five domain-specific importer modules are in design. Each generates ZIM articles from structured source data:
- Medical Reference (WHO Essential Medicines, ICRC First Aid)
- Water Systems (WHO Drinking Water Guidelines, CDC disinfection)
- Seed Preservation (GRIN accession data)
- Food Safety (USDA Complete Guide to Home Canning)
- Botanical Knowledge (USDA PLANTS database)

See `PHASE_5.2_IMPLEMENTATION_ROADMAP.md` for the full schedule.

### Installing libzim

The export pipeline requires libzim 3.10.0+:

```bash
uv pip install "libzim>=3.10.0,<4.0"
# Optional: install zimcheck for post-export validation
sudo apt-get install zim-tools
```

The libzim pre-built wheel covers Python 3.10–3.14 on aarch64 (Raspberry Pi 5), x86_64, and macOS. No compiler or system C++ libraries required.

## Next Phases

**Phase 5.2** (Domain Content Coverage, June–July 2026):
- Medical Reference, Water Systems, Seed Preservation, Food Safety, Botanical Knowledge importers
- ~110 new unit + integration tests
- Full multi-domain ZIM build and OPDS catalog update

**Phase 5.3** (Federation, post-July 2026):
- Peer-to-peer ZIM library sharing via signed manifests + multi-channel transfer
- mDNS local library discovery
- IPFS CID-addressed ZIM distribution

**Phase 6+** (Advanced Federation & Scale):
- ActivityPub outbox implementation (content propagation)
- DID-based identity and decentralized identity verification
- Cross-node conflict resolution improvements

## Important Notes

- **Authentication**: Not implemented. All endpoints are public. DID-based auth planned for Phase 6.
- **Database**: Uses async SQLAlchemy with asyncpg driver for PostgreSQL.
- **JSON-LD**: Full JSON-LD objects are generated and stored with every item for federation compatibility.
- **CID Format**: SHA256-based (`sha256-{hex}`). IPFS-compatible for future blob storage.
- **Export scope**: The export pipeline can produce LOCAL_ONLY, DOMAIN-scoped, or FULL library ZIM files depending on the ExportConfig.

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
