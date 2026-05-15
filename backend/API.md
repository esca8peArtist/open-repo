# Open-Repo Backend API Documentation

**Version**: 0.4.0  
**Base URL**: `http://localhost:8000` (development)  
**Status**: Phase 4 (CRUD + Search + Endorsements + Federation + Export Framework)

---

## Overview

The Open-Repo Backend is a full-stack FastAPI + PostgreSQL application that implements complete CRUD, search, endorsement, and federation endpoints for managing OpenRepoItem content in JSON-LD format and distributing content via Kiwix offline archives.

**Phase 4 includes**:
- ✅ CRUD operations with JSON-LD validation
- ✅ Full-text search (Meilisearch)
- ✅ Endorsement system (voting, flagging)
- ✅ Federation service layer (partner registration, HTTP signature verification)
- ✅ Export framework (ZimWriter stubs + OPDS catalog stubs)
- ✅ Admin dashboard (partner management, conflict logs)

**Out of scope for Phase 4**:
- libzim integration (Phase 5 - stubs in place)
- feedgen migration for OPDS (Phase 5 - raw XML used for now)
- DID-based authentication (Phase 6)

---

## Endpoints

### Health & Status

#### `GET /health`

Health check endpoint. Returns API and database status.

**Response** (200 OK):
```json
{
  "status": "healthy",
  "version": "0.1.0",
  "database": "healthy"
}
```

**Status values**:
- `healthy`: API and database operational
- `degraded`: API running, database unreachable

---

#### `GET /`

Root endpoint returning API metadata.

**Response** (200 OK):
```json
{
  "name": "Open-Repo API",
  "version": "0.1.0",
  "docs": "/docs",
  "health": "/health"
}
```

---

### Content Items

#### `POST /api/items`

Create a new content item. The item is stored with its full JSON-LD representation and assigned a IPFS-compatible CID (SHA256-based hash).

**Request Body**:
```json
{
  "title": {
    "en": "Growing Potatoes: Earthing Up for Maximum Yield",
    "es": "Cultivo de patatas: Aporcado para máximo rendimiento"
  },
  "type": "procedure",
  "domain": "procedural",
  "license": "CC-BY-4.0",
  "language": ["en", "es"],
  "description": {
    "en": "How to grow potatoes with proper hilling technique"
  },
  "tags": ["agriculture", "potato", "organic"],
  "difficulty": "beginner",
  "outcome": {
    "en": "High-yield potato harvest"
  },
  "steps": [
    {
      "stepNumber": 1,
      "title": {"en": "Prepare seed potatoes"},
      "body": {"en": "Set seed potatoes in a cool, light location to sprout"}
    }
  ],
  "attribution": {
    "source": "https://openfarm.cc",
    "sourceTitle": "OpenFarm — Free and Open Database"
  }
}
```

**Required Fields**:
- `title` (object): Multilingual title. Must have at least one language key.
- `type` (string): Content type. One of: `procedure`, `recipe`, `schematic`, `plan`, `service-listing`
- `domain` (string): Content domain (e.g., `procedural`, `structural`, `service`)
- `license` (string): License identifier (e.g., `CC-BY-4.0`, `CC0-1.0`, `CC-BY-SA-4.0`)

**Optional Fields**:
- `description` (object): Multilingual description
- `language` (array): Language codes (ISO 639-1). Default: `["en"]`
- `tags` (array): Searchable tags. Default: `[]`
- `attribution` (object): Source metadata with `source` and `sourceTitle`
- `wikidataLinks` (array): Wikidata QIDs

**Type-Specific Fields** (procedure):
- `difficulty` (string): One of `beginner`, `intermediate`, `advanced`
- `outcome` (object): Expected result
- `timeRequired` (object): ISO 8601 durations (e.g., `{"execution": "PT6H"}`)
- `tools` (array): Required tools/materials
- `materials` (array): Material requirements
- `steps` (array): Ordered steps with verification points
- `safetyNotes` (array): Safety warnings
- `performanceData` (object): Measured performance metrics
- `costEstimate` (object): Budget estimate

**Type-Specific Fields** (recipe):
- `category` (string): One of `food`, `beverage`, `medicine`, etc.
- `subcategory` (string): More specific category (e.g., `grain-preservation`)
- `yield` (object): Output quantity and unit
- `ingredients` (array): Ingredient list
- `equipment` (array): Required equipment
- `storageInstructions` (object): How to store the product
- `foodSafety` (object): Safety warnings for consumption

**Response** (201 Created):
```json
{
  "cid": "sha256-4a35babef40b26cf425e6f535754556822cfcef58ddb7db812a7ff0c60c5ebc3",
  "title": {
    "en": "Growing Potatoes: Earthing Up for Maximum Yield",
    "es": "Cultivo de patatas: Aporcado para máximo rendimiento"
  },
  "item_type": "procedure",
  "domain": "procedural",
  "license": "CC-BY-4.0",
  "language": ["en", "es"],
  "tags": ["agriculture", "potato", "organic"],
  "created_at": "2026-04-26T03:45:23.123456",
  "updated_at": "2026-04-26T03:45:23.123456",
  "content_jsonld": {
    "@context": [
      "https://www.w3.org/ns/activitystreams",
      "https://schema.org/",
      "https://openrepo.net/ns/v1"
    ],
    "@type": "procedure",
    "id": "https://node.openrepo.example.org/items/sha256-4a35...",
    "cid": "sha256-4a35babef40b26cf425e6f535754556822cfcef58ddb7db812a7ff0c60c5ebc3",
    "title": {...},
    "version": "1"
  }
}
```

**Error Responses**:
- **409 Conflict**: Item with this CID already exists
- **422 Unprocessable Entity**: Validation error (invalid type, missing required fields, etc.)

---

#### `GET /api/items/{cid}`

Retrieve a single item by its Content Identifier (CID).

**Parameters**:
- `cid` (string, path): The SHA256-based CID of the item

**Response** (200 OK):
```json
{
  "cid": "sha256-4a35...",
  "title": {...},
  "item_type": "procedure",
  "domain": "procedural",
  "license": "CC-BY-4.0",
  "language": ["en"],
  "created_at": "2026-04-26T03:45:23.123456",
  "updated_at": "2026-04-26T03:45:23.123456",
  "content_jsonld": {...}
}
```

**Error Responses**:
- **404 Not Found**: Item with this CID does not exist

---

#### `GET /api/items`

List content items with pagination and optional filters.

**Query Parameters**:
- `limit` (integer, default: 10, min: 1, max: 100): Number of items per page
- `offset` (integer, default: 0, min: 0): Pagination offset
- `item_type` (string, optional): Filter by type (`procedure`, `recipe`, `schematic`, `plan`, `service-listing`)
- `domain` (string, optional): Filter by domain (`procedural`, `structural`, etc.)
- `tags` (string, optional): Filter by comma-separated tags (matches any tag)

**Response** (200 OK):
```json
{
  "items": [
    {
      "cid": "sha256-...",
      "title": {"en": "Growing Potatoes"},
      "item_type": "procedure",
      "domain": "procedural",
      "license": "CC-BY-4.0",
      "language": ["en"],
      "tags": ["agriculture", "potato"],
      "created_at": "2026-04-26T03:45:23.123456",
      "updated_at": "2026-04-26T03:45:23.123456",
      "content_jsonld": {...}
    }
  ],
  "total": 32,
  "limit": 10,
  "offset": 0,
  "has_more": true
}
```

**Example Queries**:
```
GET /api/items?limit=20&offset=0                    # First 20 items
GET /api/items?item_type=procedure&limit=50         # All procedures
GET /api/items?domain=procedural&tags=water         # Procedures tagged 'water'
GET /api/items?item_type=recipe&limit=100           # All recipes
```

---

## Data Model

### ContentItem (Database)

| Field | Type | Indexed | Description |
|-------|------|---------|-------------|
| `cid` | VARCHAR(255) | ✓ PRIMARY | Content Identifier (SHA256 hash) |
| `title` | VARCHAR(500) | ✓ | English title for display/search |
| `item_type` | VARCHAR(50) | ✓ | Type: procedure, recipe, schematic, plan, service-listing |
| `domain` | VARCHAR(50) | ✓ | Domain/category |
| `license` | VARCHAR(50) | | License identifier |
| `content_jsonld` | JSON | | Full JSON-LD object (all schema fields) |
| `created_at` | DateTime | ✓ | Creation timestamp |
| `updated_at` | DateTime | | Last update timestamp |
| `source_url` | VARCHAR(500) | | Original source URL |
| `source_title` | VARCHAR(255) | | Original source title |

### JSON-LD Structure

All items are stored with a full JSON-LD representation including:

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://schema.org/",
    "https://openrepo.net/ns/v1"
  ],
  "@type": "procedure",
  "id": "https://node.openrepo.example.org/items/{cid}",
  "cid": "{sha256-hash}",
  "title": {...},
  "domain": "procedural",
  "type": "procedure",
  "license": "CC-BY-4.0",
  "language": [...],
  "created": "2026-04-26T...",
  "updated": "2026-04-26T...",
  "tags": [...],
  "wikidataLinks": [...],
  "endorsements": [],
  "relatedItems": [],
  "mediaItems": [],
  "node": "https://node.openrepo.example.org",
  "version": "1",
  ...type-specific fields...
}
```

---

## Content Types

### Procedure

A step-by-step how-to guide with structured materials, tools, and verification steps.

**Key Fields**:
- `outcome`: Expected result
- `difficulty`: beginner/intermediate/advanced
- `timeRequired`: ISO 8601 durations
- `steps`: Array of step objects with verification points
- `materials`: Bill of materials
- `tools`: Required tools
- `performanceData`: Measured results (e.g., "99.98% E. coli reduction")
- `safetyNotes`: Safety warnings

### Recipe

A specialized procedure for food/beverage/medicine preparation.

**Key Fields**:
- `category`: food/beverage/medicine
- `yield`: Output quantity
- `ingredients`: Ingredient list with quantities
- `storageInstructions`: How to preserve the product
- `foodSafety`: Food-specific safety notes
- `equipment`: Kitchen/preparation equipment

### Schematic

Technical drawings, circuit diagrams, or CAD files.

**Key Fields**:
- `schematicType`: electrical-circuit, mechanical, building, etc.
- `blobs`: Array of file references (KiCad, PDF, DXF, etc.)
- `billOfMaterials`: Component list with substitutes and pricing
- `specification`: Technical parameters (voltage, current, efficiency, etc.)

### Plan

Spatial/architectural documents: building plans, garden layouts, site designs.

**Key Fields**:
- `planType`: building, garden, site, etc.
- `scale`: Drawing scale (e.g., "1:20")
- `dimensions`: Physical dimensions
- `blobs`: CAD file references (DXF, PDF, etc.)
- `buildingCode`: Jurisdiction and compliance notes
- `estimatedCost`: Budget estimate

### Service Listing

A human exchange listing (skill, service, or resource within a community).

**Key Fields**:
- `offerType`: skill, service, tool, resource
- `category`: agriculture, repair, construction, etc.
- `provider`: DID and verification level
- `location`: Point geometry with radius
- `availability`: Seasonal or standing availability
- `exchangeTypes`: time-bank, skill-exchange, cash, barter

---

## Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK - Request succeeded |
| 201 | Created - Item successfully created |
| 400 | Bad Request - Malformed request |
| 404 | Not Found - Item does not exist |
| 409 | Conflict - Item already exists (duplicate CID) |
| 422 | Unprocessable Entity - Validation error |
| 500 | Internal Server Error |

---

## Authentication & Authorization

**Phase 1 MVP**: No authentication required. All endpoints are public read/write.

**Future Phases**:
- DID-based identity (did:web)
- Contribution review workflow
- Endorsement signatures

---

## Pagination

All list endpoints support cursor-free offset-based pagination:

- `limit`: How many items to return (1-100, default 10)
- `offset`: How many items to skip (default 0)
- `has_more`: Boolean indicating if more items exist beyond this page

**Example**:
```
GET /api/items?limit=25&offset=0   # Items 1-25
GET /api/items?limit=25&offset=25  # Items 26-50
GET /api/items?limit=25&offset=50  # Items 51-75
```

---

## Filtering

### By Type
```
GET /api/items?item_type=procedure
GET /api/items?item_type=recipe
GET /api/items?item_type=schematic
```

### By Domain
```
GET /api/items?domain=procedural
GET /api/items?domain=structural
```

### By Tags (any match)
```
GET /api/items?tags=water
GET /api/items?tags=water,filtration,DIY
```

### Combined Filters
```
GET /api/items?item_type=procedure&domain=procedural&tags=water&limit=50
```

---

## Content Identifier (CID) Format

CIDs are SHA256-based hashes of the core content:

```
sha256-{hex_digest}
```

**Example**:
```
sha256-4a35babef40b26cf425e6f535754556822cfcef58ddb7db812a7ff0c60c5ebc3
```

**Computed from**: Title, domain, type, license (stable hash for identical content)

---

## Running the Backend

### Setup

```bash
# Install dependencies
cd projects/open-repo/backend
uv pip install -e ".[dev]"

# Create PostgreSQL database (local or Docker)
# export DATABASE_URL="postgresql+asyncpg://user:pass@localhost:5432/open_repo"

# Initialize schema
uv run python -c "
import asyncio
from app.database import init_db
asyncio.run(init_db())
"
```

### Running the Server

```bash
# Development server with auto-reload
uv run uvicorn app.main:create_app --reload --host 0.0.0.0 --port 8000

# Or directly
cd backend
uv run python app/main.py
```

### Loading Seed Data

```bash
cd backend
uv run python scripts/load_seed_data.py
```

This loads the 32 OpenFarm growing guides from `../data/openfarm_procedures.jsonl`.

### Running Tests

```bash
cd backend
uv run pytest tests/ -v                      # All tests
uv run pytest tests/test_routes.py -v        # Route tests only
uv run pytest tests/ -v --cov=app            # With coverage
```

---

## OpenAPI Documentation

When running locally, access interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## Phase 2 Implementation: Search + Endorsements

### Search Endpoint

#### `GET /api/items/search`

Full-text search against content items using Meilisearch.

**Query Parameters**:
- `q` (string, required): Search query string (minimum 1 character)
- `limit` (integer, default: 10, min: 1, max: 100): Number of results to return
- `offset` (integer, default: 0, min: 0): Pagination offset
- `item_type` (string, optional): Filter by type (`procedure`, `recipe`, `schematic`, `plan`, `service-listing`)
- `domain` (string, optional): Filter by domain
- `tags` (string, optional): Filter by comma-separated tags (matches any tag)

**Searchable Fields**: title, description, tags, domain, item_type, author

**Response** (200 OK):
```json
{
  "query": "potato",
  "hits": [
    {
      "cid": "sha256-...",
      "title": "Growing Potatoes",
      "description": "How to grow potatoes...",
      "tags": ["agriculture", "potato"],
      "domain": "procedural",
      "item_type": "procedure",
      "author": "OpenFarm",
      "created_at": "2026-04-26T..."
    }
  ],
  "limit": 10,
  "offset": 0,
  "estimated_total_hits": 32,
  "processing_time_ms": 45
}
```

**Example Queries**:
```
GET /api/items/search?q=water                                    # Basic search
GET /api/items/search?q=filter&item_type=procedure&limit=50      # With filter
GET /api/items/search?q=agriculture&tags=organic,DIY&offset=20   # With tags and pagination
```

---

### Endorsement Endpoints

#### `POST /api/items/{cid}/endorse`

Submit an endorsement for a content item.

**Request Body**:
```json
{
  "user_id": "user@example.com",
  "endorsement_type": "upvote"
}
```

**Endorsement Types**:
- `upvote` - Positive endorsement
- `downvote` - Negative endorsement  
- `flag` - Flag for moderation (inappropriate, spam, etc.)

**Note**: If a user submits multiple endorsements for the same item, the latest one overwrites the previous.

**Response** (201 Created):
```json
{
  "id": 1,
  "item_cid": "sha256-...",
  "user_id": "user@example.com",
  "endorsement_type": "upvote",
  "created_at": "2026-04-26T03:45:23.123456"
}
```

**Error Responses**:
- **404 Not Found**: Item with this CID does not exist
- **422 Unprocessable Entity**: Invalid endorsement_type

---

#### `GET /api/items/{cid}/endorsements`

Get aggregated endorsement statistics for an item.

**Response** (200 OK):
```json
{
  "item_cid": "sha256-...",
  "upvote_count": 15,
  "downvote_count": 2,
  "flag_count": 1,
  "total_count": 18,
  "score": 13
}
```

**Score Calculation**: `upvote_count - downvote_count`

**Error Responses**:
- **404 Not Found**: Item does not exist

---

#### `GET /api/items/{cid}/endorsements/my-endorsement`

Get a specific user's endorsement for an item (if any).

**Query Parameters**:
- `user_id` (string, required): The user identifier

**Response** (200 OK):
```json
{
  "endorsement": {
    "id": 1,
    "item_cid": "sha256-...",
    "user_id": "user@example.com",
    "endorsement_type": "upvote",
    "created_at": "2026-04-26T03:45:23.123456"
  }
}
```

**Response when user has not endorsed** (200 OK):
```json
{
  "endorsement": null
}
```

**Error Responses**:
- **404 Not Found**: Item does not exist

---

#### `DELETE /api/items/{cid}/endorsements/my-endorsement`

Remove a user's endorsement from an item.

**Query Parameters**:
- `user_id` (string, required): The user identifier

**Response** (204 No Content)

**Error Responses**:
- **404 Not Found**: Item does not exist

---

#### `GET /admin/items/{cid}/endorsements`

Get full endorsement audit log for an item (admin endpoint).

Returns all endorsements for the item in reverse chronological order (newest first).

**Response** (200 OK):
```json
[
  {
    "id": 1,
    "item_cid": "sha256-...",
    "user_id": "user@example.com",
    "endorsement_type": "upvote",
    "created_at": "2026-04-26T03:45:23.123456"
  },
  {
    "id": 2,
    "item_cid": "sha256-...",
    "user_id": "admin@example.com",
    "endorsement_type": "flag",
    "created_at": "2026-04-26T03:40:00.000000"
  }
]
```

**Error Responses**:
- **404 Not Found**: Item does not exist

---

## Next Phases

**Phase 3** (Contribution):
- `POST /api/contributions` (anonymous submission)
- Review queue and moderation workflow
- Contribution draft state

**Phase 4+** (Federation):
- ActivityPub inbox/outbox
- `.well-known/webfinger` for node discovery
- Federated content sync across nodes
