# Open-Repo Schema Documentation

**Version**: 0.4.0  
**Status**: Production-ready (Phase 5 complete)  
**Last Updated**: 2026-06-28

---

## Overview

Open-Repo is a distributed, decentralized knowledge network for sharing practical information: procedures, recipes, schematics, plans, and services. All content is stored as JSON-LD objects with content identifiers (CIDs) computed via SHA256 hashing of the normalized JSON-LD form.

This document defines:
1. **Database Schema** — SQLAlchemy ORM models for persistence
2. **API Schema** — Request/response Pydantic models
3. **Content Types** — Five content categories with field specifications
4. **Federation Schema** — ActivityPub models for P2P synchronization
5. **Offline Export Schema** — ZIM model for offline access

---

## Database Schema

### Content Storage

#### **ContentItem** Table
Stores the canonical JSON-LD content object for each item in the network.

| Column | Type | Nullable | Index | Notes |
|--------|------|----------|-------|-------|
| `cid` | String(255) | No | Yes | **Primary Key**. Content Identifier computed as SHA256 hash of normalized JSON-LD. Example: `sha256-abc123...` |
| `title` | String(500) | No | Yes | Human-readable title (multilingual via JSON-LD `title` field) |
| `item_type` | String(50) | No | Yes | Type enumeration: `procedure`, `recipe`, `schematic`, `plan`, `service-listing` |
| `domain` | String(50) | No | Yes | Domain classification (e.g., `procedural`, `food`, `medical`, `energy`) |
| `license` | String(50) | No | No | License identifier (e.g., `CC-BY-4.0`, `OGC-ODbL`) |
| `content_jsonld` | JSON | No | No | Full JSON-LD object; stores all type-specific fields |
| `source_url` | String(500) | Yes | No | Attribution: URL of original source for federated content |
| `source_title` | String(255) | Yes | No | Attribution: Title of source for federated content |
| `created_at` | DateTime | No | Yes | Timestamp when item first entered this node |
| `updated_at` | DateTime | No | No | Last modification timestamp (updates via federation or local edits) |

**Sample Row**:
```json
{
  "cid": "sha256-a7c9f...",
  "title": "Water Purification by Boiling",
  "item_type": "procedure",
  "domain": "water",
  "license": "CC-BY-4.0",
  "content_jsonld": {
    "@context": "https://schema.org",
    "@type": "Procedure",
    "title": { "en": "Water Purification by Boiling", "es": "Purificación de agua..." },
    "description": {...},
    "steps": [...],
    "tools": [...],
    ...
  },
  "created_at": "2026-06-15T10:30:00",
  "updated_at": "2026-06-28T14:45:00"
}
```

---

### User Feedback & Endorsements

#### **Endorsement** Table
Tracks user feedback (upvotes, downvotes, flags) on content items.

| Column | Type | Nullable | Index | Notes |
|--------|------|----------|-------|-------|
| `id` | Integer | No | Yes | **Primary Key**. Auto-incremented |
| `item_cid` | String(255) | No | Yes | **Foreign Key** → `content_items.cid` |
| `user_id` | String(255) | No | Yes | User identifier (DIDs in production; simple strings in MVP) |
| `endorsement_type` | Enum | No | Yes | `upvote`, `downvote`, or `flag` |
| `created_at` | DateTime | No | Yes | Endorsement timestamp |

**Constraints**: 
- Unique index on `(item_cid, user_id, endorsement_type)` prevents duplicate endorsements
- Cascading delete if content item is removed

---

### Contributions & Review Workflow

#### **Contribution** Table
Tracks user submissions (new items or edits to existing items) through the review lifecycle.

| Column | Type | Nullable | Index | Notes |
|--------|------|----------|-------|-------|
| `id` | BigInteger | No | Yes | **Primary Key**. Auto-incremented |
| `contribution_type` | Enum | No | Yes | `new_item` (create) or `edit_item` (modify) |
| `status` | Enum | No | Yes | State machine: `pending` → `revision_requested` / `approved` / `rejected` |
| `contributor_id` | String(255) | No | Yes | Author ID |
| `created_at` | DateTime | No | Yes | Submission timestamp |
| `updated_at` | DateTime | No | Yes | Last status change timestamp |
| `target_item_cid` | String(255) | Yes | Yes | For edit contributions: CID of item being edited; NULL for new items |
| `proposed_cid` | String(255) | Yes | Yes | For new contributions: CID of proposed content |
| `item_data` | JSON | No | No | Full proposed JSON-LD object |
| `edit_diff` | JSON | Yes | No | For edits: structured diff (`{field: old_value, new_value}`) |
| `reviewer_notes` | Text | Yes | No | Reviewer comments |
| `rejection_reason` | Text | Yes | No | Reason if rejected |
| `required_revisions` | JSON | Yes | No | Array of `{field: string, suggestion: string}` for revision-requested status |

**State Machine**:
```
pending
  ├→ revision_requested (reviewer requests changes)
  │   └→ pending (contributor resubmits)
  ├→ approved (reviewer approves)
  └→ rejected (reviewer rejects)
```

**Relationships**:
- `reviewer_queue_items` (one-to-many) — Round-robin reviewer assignments
- `feedback_items` (one-to-many) — Audit trail of reviewer feedback

---

#### **ReviewerQueueItem** Table
Tracks round-robin reviewer assignments for the contribution review process.

| Column | Type | Nullable | Index | Notes |
|--------|------|----------|-------|-------|
| `id` | BigInteger | No | Yes | **Primary Key** |
| `contribution_id` | BigInteger | No | Yes | **Foreign Key** → `contributions.id` |
| `reviewer_id` | String(255) | No | Yes | Assigned reviewer's ID |
| `assigned_at` | DateTime | No | Yes | Assignment timestamp |
| `decided_at` | DateTime | Yes | No | Time when reviewer made decision (NULL until decided) |
| `decision` | String(50) | Yes | No | `approve`, `reject`, or `revision_requested` |
| `reviewer_notes` | Text | Yes | No | Reviewer's comments on the contribution |

---

#### **ContributionFeedback** Table
Audit trail of specific reviewer feedback messages during the review process.

| Column | Type | Nullable | Index | Notes |
|--------|------|----------|-------|-------|
| `id` | BigInteger | No | Yes | **Primary Key** |
| `contribution_id` | BigInteger | No | Yes | **Foreign Key** → `contributions.id` |
| `feedback_type` | Enum | No | Yes | `text_only`, `minor_correction`, `missing_field` |
| `severity` | Enum | No | Yes | `low`, `medium`, `high` |
| `message` | Text | No | No | Feedback content |
| `resolved` | Integer | No | No | 0 = unresolved, 1 = resolved |
| `resolved_at` | DateTime | Yes | No | When feedback was resolved |
| `created_at` | DateTime | No | Yes | When feedback was posted |

---

### Federation (ActivityPub)

#### **FederationPartner** Table
Tracks peer nodes in the federated network and their public keys for signature verification.

| Column | Type | Nullable | Index | Notes |
|--------|------|----------|-------|-------|
| `id` | BigInteger | No | Yes | **Primary Key** |
| `name` | String(255) | No | Yes | Partner node name (unique) |
| `base_url` | String(512) | No | Yes | Partner's base URL; used to fetch `.well-known/webfinger` |
| `public_key_pem` | Text | No | No | PEM-encoded RSA public key for HTTP signature verification |
| `key_id` | String(512) | No | Yes | Key identifier URI (unique) |
| `trust_state` | Enum | No | Yes | `pending`, `trusted`, `untrusted`, `revoked` |
| `created_at` | DateTime | No | Yes | When partner was first discovered |
| `updated_at` | DateTime | No | No | Last metadata update |
| `public_key_expires_at` | DateTime | Yes | No | Key expiration time (for key rotation) |
| `last_key_refresh_at` | DateTime | Yes | No | When key was last refreshed from partner |
| `last_activity_at` | DateTime | Yes | Yes | Last time we received activity from this partner |

**Trust State Machine**:
```
pending
  ├→ trusted (after key verification)
  ├→ untrusted (failed signature verification)
  └→ revoked (administrator revokes trust)
```

---

#### **Activity** Table
Stores ActivityPub activities for federation (Create, Update, Delete, Announce, etc.).

| Column | Type | Nullable | Index | Notes |
|--------|------|----------|-------|-------|
| `id` | BigInteger | No | Yes | **Primary Key** |
| `activity_type` | Enum | No | Yes | `Create`, `Update`, `Delete`, `Announce`, `Undo`, `Follow`, `Accept` |
| `activity_id` | String(512) | No | Yes | Unique activity URI (unique) |
| `actor_url` | String(512) | No | Yes | Full actor URL (person or organization who performed the action) |
| `object_id` | String(512) | Yes | Yes | Object URI or inline object CID |
| `object_data` | JSON | Yes | No | Full object for Create/Update (nested JSON-LD) |
| `activity_data` | JSON | No | No | Complete ActivityPub activity as JSON-LD |
| `local` | Integer | No | No | 1 = generated locally, 0 = received from remote |
| `partner_id` | BigInteger | Yes | Yes | **Foreign Key** → `federation_partners.id` (only set for received activities) |
| `signature_header` | String(1024) | Yes | No | Raw HTTP Signature header (for audit) |
| `signature_verified` | Integer | No | No | 1 = verified, 0 = unverified/failed |
| `created_at` | DateTime | No | Yes | When activity was created locally or received |
| `published` | DateTime | No | No | Activity publication timestamp |

**Sample Activity**:
```json
{
  "activity_type": "Create",
  "activity_id": "https://node-a.example.com/activities/uuid-1234",
  "actor_url": "https://node-a.example.com/users/alice",
  "object_id": "sha256-a7c9f...",
  "activity_data": {
    "@context": "https://www.w3.org/ns/activitystreams",
    "type": "Create",
    "id": "https://node-a.example.com/activities/uuid-1234",
    "actor": "https://node-a.example.com/users/alice",
    "object": { "@type": "Procedure", "title": "...", ... }
  },
  "local": 0,
  "partner_id": 1,
  "signature_verified": 1
}
```

---

#### **FederationConflict** Table
Records signature/key/trust verification failures for admin monitoring.

| Column | Type | Nullable | Index | Notes |
|--------|------|----------|-------|-------|
| `id` | BigInteger | No | Yes | **Primary Key** |
| `partner_id` | BigInteger | No | Yes | **Foreign Key** → `federation_partners.id` |
| `activity_id` | BigInteger | Yes | Yes | **Foreign Key** → `activities.id` (NULL for key-level conflicts) |
| `conflict_type` | Enum | No | Yes | `signature_mismatch`, `key_expired`, `key_revoked`, `trust_failure` |
| `status` | Enum | No | Yes | `active`, `resolved` |
| `error_message` | Text | Yes | No | Error details from verification failure |
| `resolution_action` | Enum | Yes | No | `auto_downgrade`, `manual_review`, `ignore` |
| `resolved_by` | String(255) | Yes | No | Admin user ID or system ID |
| `resolution_notes` | Text | Yes | No | Resolution explanation |
| `detected_at` | DateTime | No | Yes | When conflict was detected |
| `resolved_at` | DateTime | Yes | Yes | When conflict was resolved (NULL if active) |

---

#### **NodePublicKey** Table
Cache of public keys from other nodes (for optimization and fallback).

| Column | Type | Nullable | Index | Notes |
|--------|------|----------|-------|-------|
| `id` | BigInteger | No | Yes | **Primary Key** |
| `key_id` | String(512) | No | Yes | Unique key URI (unique) |
| `public_key_pem` | Text | No | No | PEM-encoded public key |
| `node_url` | String(512) | No | Yes | Source node URL |
| `created_at` | DateTime | No | Yes | When key was cached |
| `updated_at` | DateTime | No | No | Last refresh timestamp |

---

### Offline Export (Phase 5 - ZIM)

#### **ZimExport** Table
Tracks offline content exports in ZIM format (Kiwix-compatible). Each export is a snapshot of content at a specific time.

| Column | Type | Nullable | Index | Notes |
|--------|------|----------|-------|-------|
| `id` | BigInteger | No | Yes | **Primary Key** |
| `zim_uuid` | String(36) | No | Yes | Unique export identifier (UUID v4) (unique) |
| `name` | String(255) | No | Yes | Export name (e.g., `openrepo`) |
| `flavour` | String(50) | No | Yes | Flavor: `nopic` (no images), `all` (with images) |
| `language` | String(10) | No | No | Primary language code (e.g., `en`, `es`, `multi`) |
| `period` | String(10) | No | Yes | Period string (e.g., `2026-06a` for June 2026) |
| `article_count` | Integer | No | No | Number of articles in the ZIM file |
| `file_size_bytes` | BigInteger | No | No | Size of generated ZIM file in bytes |
| `sha256` | String(64) | No | No | SHA256 hash of ZIM file for integrity verification |
| `title` | String(255) | No | No | Display title for the ZIM file |
| `description` | String(80) | No | No | Short description (max 80 chars per ZIM spec) |
| `cdn_url` | String(512) | Yes | No | CDN/public URL for the ZIM file (if hosted) |
| `local_path` | String(512) | Yes | No | Local filesystem path where ZIM file is stored |
| `status` | String(20) | No | Yes | `generating`, `complete`, `superseded`, `deleted` |
| `is_current` | Integer | No | Yes | 1 = current production export, 0 = archived/superseded |
| `is_reference` | Integer | No | No | 1 = reference/baseline export for comparison |
| `export_scope` | String(20) | No | No | `all` (full corpus), `domain` (single domain), `tag` (by tag) |
| `scope_value` | String(100) | Yes | No | Domain name or tag value (if scoped export) |
| `include_images` | Integer | No | No | 1 = images included in ZIM, 0 = text-only |
| `zimcheck_passed` | Integer | Yes | No | 1 = zimcheck validation passed, 0 = failed, NULL = not run |
| `zimcheck_output` | Text | Yes | No | Output from zimcheck command (for debugging) |
| `generation_duration_seconds` | Integer | Yes | No | How long the ZIM generation took |
| `started_at` | DateTime | No | No | When export process started |
| `completed_at` | DateTime | Yes | No | When export process completed (NULL if still generating) |
| `superseded_at` | DateTime | Yes | No | When this export was replaced by a newer version |
| `deleted_at` | DateTime | Yes | No | When this export was deleted (soft delete) |
| `created_at` | DateTime | No | Yes | Record creation timestamp |
| `updated_at` | DateTime | No | No | Last metadata update |

**Sample Row**:
```json
{
  "zim_uuid": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "name": "openrepo",
  "flavour": "nopic",
  "language": "en",
  "period": "2026-06a",
  "article_count": 2847,
  "file_size_bytes": 524288000,
  "sha256": "abc123def456...",
  "title": "Open-Repo June 2026",
  "description": "Decentralized knowledge network snapshot",
  "status": "complete",
  "is_current": 1,
  "zimcheck_passed": 1
}
```

---

## API Schema (Request/Response Models)

### Content Creation & Retrieval

#### **POST /api/items** — Create Content Item

**Request Body**:
```json
{
  "title": {
    "en": "Water Purification by Boiling",
    "es": "Purificación de agua por ebullición"
  },
  "type": "procedure",
  "domain": "water",
  "license": "CC-BY-4.0",
  "description": {
    "en": "How to purify water through boiling for safe drinking",
    "es": "Cómo purificar agua..."
  },
  "language": ["en", "es"],
  "tags": ["water", "safety", "no-equipment", "emergency"],
  "difficulty": "easy",
  "timeRequired": {
    "en": "15-30 minutes",
    "es": "15-30 minutos"
  },
  "tools": [
    {
      "en": "Pot or kettle",
      "es": "Olla o tetera",
      "quantity": "1"
    }
  ],
  "materials": [
    {
      "en": "Water (from any source)",
      "es": "Agua (de cualquier fuente)",
      "quantity": "1-2 liters"
    }
  ],
  "steps": [
    {
      "stepNumber": 1,
      "title": { "en": "Fill pot with water" },
      "body": { "en": "Fill your pot or kettle with water..." }
    },
    {
      "stepNumber": 2,
      "title": { "en": "Boil the water" },
      "body": { "en": "Bring to a rolling boil..." }
    }
  ],
  "safetyNotes": [
    {
      "en": "Water must reach 100°C (212°F) for at least 1 minute"
    }
  ],
  "outcome": {
    "en": "Water safe for drinking"
  }
}
```

**Response** (HTTP 201):
```json
{
  "cid": "sha256-a7c9f8e...",
  "title": {
    "en": "Water Purification by Boiling",
    "es": "Purificación de agua por ebullición"
  },
  "item_type": "procedure",
  "domain": "water",
  "license": "CC-BY-4.0",
  "description": { "en": "...", "es": "..." },
  "language": ["en", "es"],
  "tags": ["water", "safety", "no-equipment", "emergency"],
  "created_at": "2026-06-28T14:30:00Z",
  "updated_at": "2026-06-28T14:30:00Z",
  "content_jsonld": {
    "@context": "https://schema.org",
    "@type": "Procedure",
    "identifier": { "@type": "PropertyValue", "propertyID": "CID", "value": "sha256-..." },
    "title": { ... },
    "steps": [ ... ],
    ...
  }
}
```

---

#### **GET /api/items/{cid}** — Retrieve Single Item

**Response** (HTTP 200):
```json
{
  "cid": "sha256-a7c9f8e...",
  "title": { "en": "...", "es": "..." },
  "item_type": "procedure",
  "domain": "water",
  "license": "CC-BY-4.0",
  "created_at": "2026-06-28T14:30:00Z",
  "updated_at": "2026-06-28T14:30:00Z",
  "content_jsonld": { ... }
}
```

---

#### **GET /api/items** — List Items (Paginated)

**Query Parameters**:
- `limit` (int, default 50, max 200) — Items per page
- `offset` (int, default 0) — Number of items to skip
- `type` (string, optional) — Filter by item type
- `domain` (string, optional) — Filter by domain
- `tag` (string, optional) — Filter by tag

**Response** (HTTP 200):
```json
{
  "items": [
    {
      "cid": "sha256-abc...",
      "title": { "en": "Water Purification by Boiling" },
      "item_type": "procedure",
      "domain": "water",
      "license": "CC-BY-4.0",
      "created_at": "2026-06-28T14:30:00Z",
      "updated_at": "2026-06-28T14:30:00Z",
      "content_jsonld": { ... }
    }
  ],
  "total": 2847,
  "limit": 50,
  "offset": 0,
  "has_more": true
}
```

---

### Search

#### **GET /api/items/search** — Full-Text Search

**Query Parameters**:
- `q` (string, required) — Search query
- `limit` (int, default 20, max 100)
- `offset` (int, default 0)

**Response** (HTTP 200):
```json
{
  "query": "water boiling",
  "hits": [
    {
      "cid": "sha256-a7c9f8e...",
      "title": "Water Purification by Boiling",
      "description": "How to purify water through boiling...",
      "tags": ["water", "safety", "emergency"],
      "domain": "water",
      "item_type": "procedure",
      "author": "Alice (node-a.example.com)",
      "created_at": "2026-06-28T14:30:00Z"
    }
  ],
  "limit": 20,
  "offset": 0,
  "estimated_total_hits": 47,
  "processing_time_ms": 15
}
```

---

### Endorsements

#### **POST /api/items/{cid}/endorse** — Create Endorsement

**Request Body**:
```json
{
  "user_id": "alice@node-a.example.com",
  "endorsement_type": "upvote"
}
```

**Response** (HTTP 201):
```json
{
  "id": 1,
  "item_cid": "sha256-a7c9f8e...",
  "user_id": "alice@node-a.example.com",
  "endorsement_type": "upvote",
  "created_at": "2026-06-28T15:00:00Z"
}
```

---

#### **GET /api/items/{cid}/endorsements** — Get Endorsement Statistics

**Response** (HTTP 200):
```json
{
  "item_cid": "sha256-a7c9f8e...",
  "upvote_count": 42,
  "downvote_count": 3,
  "flag_count": 1,
  "total_endorsements": 46,
  "user_endorsement": null
}
```

---

#### **DELETE /api/items/{cid}/endorsements/my-endorsement** — Remove Endorsement

**Response** (HTTP 204): No content

---

### Health Check

#### **GET /api/health** — System Health

**Response** (HTTP 200):
```json
{
  "status": "healthy",
  "version": "0.4.0",
  "database": "connected"
}
```

---

## Content Type Specifications

### 1. **Procedure**
Step-by-step instructions for accomplishing a task or goal.

**Required Fields**:
- `title` (Dict[str, str]) — Multilingual title
- `outcome` (Dict[str, str]) — What the procedure accomplishes
- `steps` (List[Step]) — Ordered list of steps

**Optional Fields**:
- `difficulty` (str) — `easy`, `medium`, `hard`
- `timeRequired` (Dict[str, str]) — Estimated duration
- `tools` (List[Dict]) — Tools needed
- `materials` (List[Dict]) — Materials needed
- `safetyNotes` (List[Dict[str, str]]) — Safety warnings
- `performanceData` (Dict) — Metrics or performance info
- `costEstimate` (Dict) — Cost breakdown
- `relatedProcedures` (List[str]) — CIDs of related procedures
- `relatedSchematics` (List[str]) — CIDs of related schematics
- `adaptations` (List[Dict]) — Adaptations for different contexts

**Step Format**:
```json
{
  "stepNumber": 1,
  "title": { "en": "Step title", "es": "Título del paso" },
  "body": { "en": "Detailed step description" },
  "media": [],
  "warningNote": { "en": "Optional warning" },
  "verificationStep": { "en": "How to verify this step worked" }
}
```

---

### 2. **Recipe**
Instructions for preparing food or beverages.

**Required Fields**:
- `title` (Dict[str, str])
- `yield_` (Dict) — Output quantity/servings
- `ingredients` (List[Dict]) — List of ingredients with quantities

**Optional Fields**:
- `category` (str) — `breakfast`, `lunch`, `dinner`, `dessert`, `beverage`, `condiment`, etc.
- `subcategory` (str) — More specific category
- `equipment` (List[Dict]) — Required kitchen equipment
- `storageInstructions` (Dict[str, str]) — How to store leftovers
- `foodSafety` (Dict[str, str]) — Food safety notes
- `scalingNotes` (Dict[str, str]) — How to scale recipe up/down

**Ingredient Format**:
```json
{
  "item": { "en": "flour", "es": "harina" },
  "quantity": "2",
  "unit": { "en": "cups", "es": "tazas" },
  "notes": { "en": "all-purpose" }
}
```

---

### 3. **Schematic**
Diagrams, blueprints, or technical drawings for building or constructing something.

**Required Fields**:
- `title` (Dict[str, str])
- `description` (Dict[str, str])

**Optional Fields**:
- `scale` (str) — Drawing scale (e.g., `1:10`)
- `materials` (List[Dict]) — Material specifications
- `dimensions` (Dict) — Key measurements
- `drawings` (List[Dict]) — Embedded or referenced drawings
- `cuttingLists` (List[Dict]) — Material cutting specifications

---

### 4. **Plan**
Long-term strategic or operational plans for communities, projects, or systems.

**Required Fields**:
- `title` (Dict[str, str])
- `description` (Dict[str, str])

**Optional Fields**:
- `timeline` (Dict) — Project timeline/milestones
- `resources` (List[Dict]) — Resource requirements
- `phases` (List[Dict]) — Project phases
- `risks` (List[Dict]) — Risk assessment
- `contingencies` (List[Dict]) — Contingency plans

---

### 5. **Service-Listing**
Descriptions of services available (repair, teaching, consulting, distribution, etc.).

**Required Fields**:
- `title` (Dict[str, str])
- `description` (Dict[str, str])
- `service_type` (str) — Type of service

**Optional Fields**:
- `availability` (Dict[str, str]) — When service is available
- `servicingArea` (str) — Geographic service area
- `pricing` (Dict) — Pricing model
- `contactInfo` (Dict) — Contact details

---

## Validation Rules

### Content Item Validation

| Rule | Applies To | Constraint |
|------|-----------|-----------|
| Required fields | All types | `title`, `domain`, `license`, `type` must be present |
| Type enumeration | All types | Must be one of: `procedure`, `recipe`, `schematic`, `plan`, `service-listing` |
| CID computation | All types | Deterministic SHA256 of normalized JSON-LD; used as primary key |
| License format | All types | Must be valid SPDX identifier (e.g., `CC-BY-4.0`, `OGC-ODbL`) |
| Multilingual support | All types | `title` and `description` are Dict[str, str] with ISO 639-1 language codes |
| Steps for procedures | Procedure | Required; each step must have `stepNumber` (sequential), `title`, `body` |
| Ingredients for recipes | Recipe | Required; each ingredient must have `item`, `quantity`, `unit` |
| Federated attribution | All types | If `source_url` is set, `source_title` must also be provided |

---

## Federation & ActivityPub

### Activity Publication

When a local user creates or updates content, the system generates an ActivityPub `Create` or `Update` activity:

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Create",
  "id": "https://this-node.example.com/activities/uuid-1234",
  "actor": "https://this-node.example.com/users/alice",
  "object": {
    "@context": "https://schema.org",
    "@type": "Procedure",
    "identifier": { "propertyID": "CID", "value": "sha256-..." },
    "title": "...",
    "steps": [ ... ],
    ...
  },
  "published": "2026-06-28T14:30:00Z"
}
```

This activity is:
1. Signed with HTTP Signature (RSA-SHA256)
2. Sent to subscribed federation partners
3. Stored locally with `local=1`
4. Stored on receiving partners with `local=0` + their partner ID

### Signature Verification

All received activities from federation partners are verified using:
1. **Key Lookup**: Fetch partner's public key via `.well-known/webfinger` if not cached
2. **Signature Header Parsing**: Extract `keyId`, `signature`, `algorithm`
3. **Signature Verification**: Verify HTTP Signature using partner's public key
4. **Trust State Check**: Only accept activities from partners with `trust_state='trusted'`

Failed verifications are logged to `federation_conflicts` table for admin review.

---

## Offline Export (ZIM) Architecture

### Export Scope

Exports can be generated with different scopes:

| Scope | Description | Example Use |
|-------|-------------|-------------|
| `all` | Full corpus (all content items) | Complete backup snapshot |
| `domain` | Single domain (e.g., `water`, `food`, `medical`) | Specialized offline guide |
| `tag` | Items tagged with a specific tag | By-topic extract |

### Flavours

- **`nopic`** — Text-only ZIM file (no images, smaller, faster to generate)
- **`all`** — Complete ZIM with images (larger, comprehensive)

### ZIM File Structure

```
openrepo_2026-06a.zim
├── A/index.html (main entry point)
├── A/water-purification-boiling.html
├── A/wheat-flour-milling.html
├── ...
├── -/favicon.ico
├── -/style.css
├── -/script.js
└── zimcheck.txt (validation report)
```

### Naming Convention

```
{name}_{period}.{flavour}.zim
Example: openrepo_2026-06a.nopic.zim
```

Where:
- `name` = lowercase project name (e.g., `openrepo`)
- `period` = YYYY-MMX (month) or YYYY-Qn (quarter) — e.g., `2026-06a`, `2026-Q2`
- `flavour` = `nopic` or `all`

---

## Indexes & Query Performance

### Recommended Query Patterns

**Get all items by domain**:
```sql
SELECT * FROM content_items WHERE domain = 'water' ORDER BY created_at DESC;
```

**Get endorsement aggregates**:
```sql
SELECT 
  item_cid,
  COUNT(CASE WHEN endorsement_type='upvote' THEN 1 END) as upvotes,
  COUNT(CASE WHEN endorsement_type='downvote' THEN 1 END) as downvotes,
  COUNT(CASE WHEN endorsement_type='flag' THEN 1 END) as flags
FROM endorsements
GROUP BY item_cid;
```

**Get pending contributions by reviewer**:
```sql
SELECT c.*, r.reviewer_id
FROM contributions c
LEFT JOIN reviewer_queue_items r ON c.id = r.contribution_id
WHERE c.status = 'pending' AND r.decided_at IS NULL
ORDER BY c.created_at ASC;
```

**Get active federation conflicts**:
```sql
SELECT * FROM federation_conflicts 
WHERE status = 'active' 
ORDER BY detected_at DESC;
```

---

## Error Handling

### Standard HTTP Response Codes

| Code | Scenario | Example |
|------|----------|---------|
| 200 | Success (retrieval) | GET /api/items/{cid} returns item |
| 201 | Success (creation) | POST /api/items creates new item |
| 204 | Success (deletion) | DELETE endorsement succeeds |
| 400 | Validation error | Required field missing |
| 401 | Unauthorized | User authentication required |
| 403 | Forbidden | User lacks permission |
| 404 | Not found | Item CID doesn't exist |
| 409 | Conflict | Duplicate endorsement or contribution |
| 500 | Server error | Database connection failure |
| 503 | Unavailable | Maintenance mode or federation error |

**Error Response Format**:
```json
{
  "detail": "Item with CID 'sha256-xyz' not found",
  "error_code": "ITEM_NOT_FOUND",
  "timestamp": "2026-06-28T14:30:00Z"
}
```

---

## Testing

All schema models are validated by:
1. **51 ZIM export pipeline tests** — Metadata, file generation, zimcheck validation
2. **Federation & endorsement tests** — Type validation, CID computation, pagination
3. **Contribution review tests** — State machine transitions, reviewer queue logic
4. **Search tests** — Meilisearch integration, response schemas

Run tests:
```bash
cd projects/open-repo/backend
uv run pytest tests/ -v
```

---

## Migration History

### Alembic Migrations

All database changes are tracked via Alembic:

```bash
cd projects/open-repo/backend
alembic upgrade head  # Apply all pending migrations
alembic current       # Show current schema version
alembic history       # Show migration history
```

---

## References

- **JSON-LD Specification**: https://www.w3.org/TR/json-ld11/
- **Schema.org Procedure**: https://schema.org/Procedure
- **Schema.org Recipe**: https://schema.org/Recipe
- **ActivityPub Spec**: https://www.w3.org/TR/activitypub/
- **HTTP Signature Draft**: https://tools.ietf.org/html/draft-cavage-http-signatures
- **ZIM Format**: https://openzim.org/
- **SPDX Licenses**: https://spdx.org/licenses/

---

**Last Updated**: 2026-06-28  
**Contact**: Maintained by Open-Repo Contributors  
**License**: CC-BY-4.0
