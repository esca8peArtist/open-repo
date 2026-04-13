---
title: "Open-Repo: MVP Protocol Design"
date: 2026-04-13
status: draft
tags: [open-knowledge, protocol, schema, mvp, federated]
---

# Open-Repo: MVP Protocol Design

> This document defines the minimum viable protocol for the open-repo network:
> content type schemas, federation mechanics, bootstrapping plan, and the
> first-node build scope. The goal is a deployable MVP — not a complete system,
> but a working instance with real content that demonstrates the core value proposition.

---

## What MVP Must Prove

The MVP proves one thing: **a structured practical knowledge graph is useful enough
that people contribute to it and link to it.** Not federation at scale, not governance,
not the full content taxonomy. One thing. The minimum footprint to prove that is:

1. A working federated node hosting `procedure` and `recipe` content types
2. 50–200 seed items in one domain (agricultural / food production)
3. A usable read API that any developer or AI can query
4. Anonymous contribution with simple review flow
5. Kiwix/offline export working

Everything else is subsequent.

---

## Section 1: Content Type Schemas

The content types are defined as JSON-LD schemas. JSON-LD was chosen because:
- It is W3C standard; human-readable; machine-parseable
- It maps naturally to Wikidata's data model via QIDs
- It extends schema.org's existing `HowTo`, `Recipe`, and `CreativeWork` types
  rather than inventing from scratch
- It is compatible with ActivityPub's `object` type system

All schemas below extend a **base content type** (`OpenRepoItem`) then add
type-specific fields.

### 1.1 Base Schema: OpenRepoItem

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://schema.org/",
    "https://openrepo.net/ns/v1"
  ],
  "@type": "OpenRepoItem",
  "id": "https://node.example.org/items/abc123",
  "cid": "bafybeigdyrzt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi",
  "title": {
    "en": "How to build a biosand water filter",
    "es": "Cómo construir un filtro de agua de bioarena",
    "sw": "Jinsi ya kujenga chujio cha maji cha biosand"
  },
  "description": {
    "en": "A slow-sand biofilm filter for household drinking water..."
  },
  "domain": "procedural",
  "type": "procedure",
  "license": "CC-BY-4.0",
  "language": ["en", "es", "sw"],
  "created": "2026-04-13T00:00:00Z",
  "updated": "2026-04-13T00:00:00Z",
  "attribution": {
    "author": "did:web:contributor.example.org",
    "source": "https://original-source.org/biosand-filter",
    "sourceTitle": "CAWST Biosand Filter Manual"
  },
  "tags": ["water", "filtration", "sanitation", "DIY", "low-tech"],
  "wikidataLinks": ["Q3284", "Q948"],
  "endorsements": [],
  "relatedItems": [],
  "mediaItems": [],
  "node": "https://node.example.org",
  "version": "1"
}
```

**Field notes**:
- `cid`: IPFS Content Identifier for the canonical blob. If the content is text,
  the CID is the hash of the JSON body. If it includes attachments (images, files),
  each attachment has its own CID.
- `wikidataLinks`: Array of Wikidata QIDs that this item relates to. Enables semantic
  linking without duplicating encyclopedic content.
- `endorsements`: Array of endorsement objects (see Section 2: Endorsements).
- `node`: The originating federated node. When the item is federated, this field
  is preserved — the origin is always visible.

---

### 1.2 Schema: `procedure`

A `procedure` is a structured how-to: steps that, if followed in order with the
listed materials, produce a defined outcome. Maps to schema.org `HowTo`.

```json
{
  "@type": "procedure",
  "outcome": {
    "en": "A functioning biosand filter producing <1 NTU turbidity output water"
  },
  "difficulty": "beginner",
  "timeRequired": {
    "preparation": "PT2H",
    "execution": "PT6H",
    "curing": "P30D"
  },
  "tools": [
    {
      "name": {"en": "Concrete mold (30 cm × 30 cm × 90 cm)"},
      "required": true,
      "substitute": {"en": "55-gallon steel drum cut to size"},
      "cid": null
    },
    {
      "name": {"en": "Sand (0.1–0.3 mm diameter, washed)"},
      "required": true,
      "quantity": "80 kg",
      "substitute": null,
      "cid": null
    }
  ],
  "materials": [
    {
      "name": {"en": "Portland cement Type 1"},
      "quantity": "40 kg",
      "unit": "kg",
      "required": true,
      "cost": {"USD": 12, "year": 2025}
    },
    {
      "name": {"en": "Gravel (3–6 mm)"},
      "quantity": "20 kg",
      "unit": "kg",
      "required": true
    }
  ],
  "steps": [
    {
      "stepNumber": 1,
      "title": {"en": "Prepare the concrete shell"},
      "body": {
        "en": "Mix cement and aggregate at 1:3 ratio by volume. Fill mold to 5 cm wall thickness. Allow to cure 7 days minimum before filling with sand layers."
      },
      "media": [],
      "warningNote": {
        "en": "Do not fill with sand until concrete has cured fully — premature loading causes cracking."
      },
      "verificationStep": {
        "en": "Tap the walls with a metal rod — a ringing sound indicates adequate cure; a dull thud indicates still-green concrete."
      }
    },
    {
      "stepNumber": 2,
      "title": {"en": "Layer the sand media"},
      "body": {
        "en": "Add layers in order from bottom to top: 5 cm gravel drainage layer, 5 cm transition sand (0.3–0.6 mm), 50 cm fine sand (0.1–0.3 mm) biological layer, 5 cm standing water layer above sand surface. The standing water feeds the biolayer (schmutzdecke)."
      },
      "media": [],
      "warningNote": null,
      "verificationStep": {
        "en": "Measure sand depth with a ruler. Fine sand layer must be 40–55 cm for adequate pathogen removal."
      }
    }
  ],
  "safetyNotes": [
    {"en": "Wear dust mask when working with dry cement — silica dust causes silicosis with chronic exposure."}
  ],
  "performanceData": {
    "pathogenReduction": "99.98% E. coli (WHO field data, 2020)",
    "turbidityReduction": "< 1 NTU output when input < 50 NTU",
    "flowRate": "0.1–0.6 L/min (design target 0.3 L/min)",
    "lifespan": "30+ years with maintenance",
    "maintenanceInterval": "When flow rate drops below 0.1 L/min"
  },
  "costEstimate": {
    "materials": {"USD": 25, "year": 2025, "region": "Sub-Saharan Africa"},
    "labor": {"hours": 6, "skilled": false}
  },
  "relatedSchematics": [],
  "relatedProcedures": [],
  "adaptations": [
    {
      "context": {"en": "High-turbidity source water (> 50 NTU)"},
      "modification": {"en": "Add a pre-sedimentation tank or coagulation step before the biosand filter. Without this, the biolayer clogs within weeks."}
    }
  ]
}
```

**Design decisions**:
- `steps[].verificationStep`: Each step has an optional verification test. This
  transforms a procedure into a checkable protocol rather than a set of instructions
  that may or may not have been followed correctly.
- `performanceData`: Structured performance data rather than prose claims. Enables
  comparison queries: "find all water treatment procedures that achieve > 99% E. coli
  reduction and cost less than $30."
- `adaptations`: Regional and contextual modifications documented in the schema, not
  in footnotes. This is the field that allows a single procedure to serve multiple
  contexts (high turbidity / low turbidity; different material availability).
- Time uses ISO 8601 duration format (`PT2H` = 2 hours, `P30D` = 30 days).

---

### 1.3 Schema: `recipe`

A `recipe` is a specific sub-type of `procedure` for preparing food, beverages,
medicines, or other consumables with ingredients, yields, and nutritional context.
Maps to schema.org `Recipe`.

```json
{
  "@type": "recipe",
  "category": "food",
  "subcategory": "grain-preservation",
  "yield": {
    "quantity": "4",
    "unit": "kg",
    "description": {"en": "4 kg dried grain (wheat, rye, or spelt)"}
  },
  "servings": null,
  "ingredients": [
    {
      "name": {"en": "Wheat grain"},
      "quantity": "5 kg",
      "notes": {"en": "Freshly harvested, < 14% moisture for best preservation"},
      "substitute": {"en": "Rye or spelt; adjust drying time by +15% for spelt"},
      "preparation": {"en": "Winnow to remove chaff before drying"}
    }
  ],
  "nutritionPerServing": null,
  "steps": [],
  "difficulty": "beginner",
  "timeRequired": {
    "active": "PT1H",
    "passive": "P3D"
  },
  "equipment": [
    {"name": {"en": "Solar dehydrator or grain dryer"}, "required": true},
    {"name": {"en": "Moisture meter"}, "required": false, "notes": {"en": "Strongly recommended; visual inspection is unreliable"}}
  ],
  "storageInstructions": {
    "en": "Store in airtight containers (glass jars, sealed drums, mylar bags with oxygen absorbers) in cool, dark, dry location. Properly dried grain stored this way lasts 10–25 years.",
    "temperatureRange": {"min_C": 0, "max_C": 21},
    "shelfLife": {"value": 25, "unit": "years", "condition": "optimal storage"}
  },
  "foodSafety": {
    "en": "Mold is the primary risk. If grain shows any discoloration, musty smell, or > 14% moisture, do not store — use immediately or discard affected portions."
  },
  "costEstimate": null,
  "scalingNotes": {
    "en": "Scales linearly to any quantity. Commercial grain drying uses the same principles at industrial scale with forced-air dryers."
  }
}
```

**Key differences from `procedure`**:
- `ingredients` vs `materials`: ingredients have nutritional/edible context; materials do not
- `storageInstructions` as a first-class field with structured shelf-life data
- `yield` in consumption units (kg of finished product, servings)
- `nutritionPerServing`: null in this example but available for recipes where nutrition data exists

---

### 1.4 Schema: `schematic`

A `schematic` is a technical drawing, circuit diagram, building plan, or mechanical
specification. May exist as a media file (PNG/PDF) with structured metadata, or as
a native CAD format (STL, DXF, STEP, KiCad).

```json
{
  "@type": "schematic",
  "schematicType": "electrical-circuit",
  "format": ["KiCad", "PDF"],
  "blobs": [
    {
      "format": "KiCad",
      "cid": "bafybeig...",
      "filename": "solar-charge-controller.kicad_sch",
      "url": "https://ipfs.io/ipfs/bafybeig..."
    },
    {
      "format": "PDF",
      "cid": "bafybeid...",
      "filename": "solar-charge-controller-rev1.pdf",
      "url": "https://ipfs.io/ipfs/bafybeid..."
    }
  ],
  "version": "Rev 1.2",
  "standards": ["IEC 60617"],
  "specification": {
    "voltage": {"input": "12-48V DC", "output": "12-24V DC"},
    "current": {"max_A": 40},
    "efficiency": ">= 94%",
    "protection": ["overvoltage", "overcurrent", "reverse-polarity", "short-circuit"]
  },
  "billOfMaterials": [
    {
      "component": "MOSFET IRF540N",
      "quantity": 2,
      "footprint": "TO-220",
      "partNumber": "IRF540NPBF",
      "substitutes": ["IRF3205", "IRLB8721"],
      "cost": {"USD": 1.20, "year": 2025}
    },
    {
      "component": "Microcontroller ATmega328P",
      "quantity": 1,
      "footprint": "DIP-28",
      "cost": {"USD": 2.50, "year": 2025}
    }
  ],
  "manufacturingNotes": {
    "en": "Through-hole design for hand assembly without SMD equipment. PCB can be ordered from JLCPCB or fabricated with toner transfer method."
  },
  "safetyRating": {
    "endorsed": false,
    "endorsements": [],
    "disclaimer": {"en": "This schematic has not been independently verified by a licensed electrical engineer. Use at your own risk. Verify all safety-critical connections before energizing."}
  },
  "relatedProcedures": [],
  "usedInProjects": []
}
```

**Key design decisions**:
- `blobs`: Each format is a separate IPFS-addressed file. The KiCad file is the
  authoritative source; PDF is a rendered export. Both are preserved.
- `billOfMaterials`: Structured component list with substitutes and current pricing.
  This is what elevates a schematic from "a drawing" to "a buildable thing."
- `safetyRating`: Safety-critical schematics require explicit endorsement metadata.
  An un-endorsed schematic is still visible and useful — the risk level is surfaced,
  not the content hidden.
- `specification`: Structured technical parameters that can be queried. "Find all
  solar charge controllers rated for >= 20A at 24V" is a useful query; it requires
  structured data, not a paragraph.

---

### 1.5 Schema: `plan`

A `plan` is a spatial or architectural document: building plans, site layouts,
garden designs, infrastructure plans.

```json
{
  "@type": "plan",
  "planType": "building",
  "subtype": "root-cellar",
  "scale": "1:20",
  "unit": "metric",
  "dimensions": {
    "length_m": 4.0,
    "width_m": 3.0,
    "height_m": 2.2,
    "depth_below_grade_m": 1.8
  },
  "blobs": [
    {
      "format": "DXF",
      "cid": "bafybeig...",
      "filename": "root-cellar-plan.dxf"
    },
    {
      "format": "PDF",
      "cid": "bafybeid...",
      "filename": "root-cellar-plan-with-notes.pdf"
    }
  ],
  "buildingCode": {
    "jurisdiction": "general",
    "notes": {"en": "Verify local setback requirements and excavation permits. Most jurisdictions exempt underground outbuildings < 200 sq ft from permit requirements, but this varies significantly."}
  },
  "materials": [
    {"name": "Concrete block (8x8x16)", "quantity": 240, "unit": "blocks"},
    {"name": "Portland cement Type 1", "quantity": "20 bags (94 lb each)"},
    {"name": "Gravel backfill", "quantity": "4 cubic yards"}
  ],
  "estimatedCost": {"USD": 2500, "year": 2025, "laborIncluded": false},
  "skillLevel": "intermediate",
  "relatedProcedures": [],
  "adaptations": [
    {
      "context": {"en": "High water table (< 6 ft to water table)"},
      "modification": {"en": "Use poured concrete with waterproofing membrane rather than block. Add French drain around exterior perimeter. This adds ~$800–$1,200 to materials."}
    }
  ]
}
```

---

### 1.6 Schema: `service-listing`

A human exchange listing — a person, cooperative, or organisation offering a skill,
service, or resource within a community.

```json
{
  "@type": "service-listing",
  "offerType": "skill",
  "category": "agriculture",
  "title": {"en": "Grain threshing — hand and mechanical — available seasonal"},
  "description": {"en": "Available for contract threshing of small grains (wheat, oats, spelt) using a 1940s John Deere thresher restored to operation. Serve within 50km of Ithaca NY. Rate negotiable; prefer time-bank or skill exchange."},
  "provider": {
    "did": "did:web:provider.example.org",
    "displayName": "Hawthorne Farm",
    "verificationLevel": "self-attested"
  },
  "location": {
    "type": "Point",
    "coordinates": [-76.5, 42.4],
    "radiusKm": 50,
    "description": {"en": "Tompkins County, NY"}
  },
  "availability": {
    "seasonal": true,
    "months": [7, 8, 9],
    "notes": {"en": "Available August–September; contact in June to schedule"}
  },
  "exchangeTypes": ["time-bank", "skill-exchange", "cash", "barter"],
  "contact": {
    "method": "instance-message",
    "handle": "@hawthornefarmlisting@node.example.org"
  },
  "endorsed": false,
  "expires": "2027-04-13T00:00:00Z"
}
```

---

## Section 2: Endorsement Schema

Endorsements are metadata objects that are attached to any `OpenRepoItem`.
They are surfaced as trust signals, not as gates on visibility.

```json
{
  "endorsement": {
    "id": "https://node.example.org/endorsements/e123",
    "endorser": {
      "did": "did:web:engineer.example.org",
      "displayName": "Jane Smith, P.E.",
      "credential": {
        "type": "LicensedEngineer",
        "jurisdiction": "New York",
        "verificationUrl": "https://opweb.dos.ny.gov/..."
      }
    },
    "itemId": "https://node.example.org/items/abc123",
    "endorsementType": "technical-verification",
    "statement": {"en": "I have reviewed this schematic and verified the component values, protection logic, and safety-critical connections. The design is sound for its stated application."},
    "timestamp": "2026-04-13T10:00:00Z",
    "signature": "base64-encoded-DID-signature"
  }
}
```

**Endorsement types**:
- `technical-verification`: A qualified expert has verified the content is technically correct
- `field-tested`: A contributor attests they have personally completed this procedure and confirms the steps work
- `translated-verified`: The translation in a given language has been verified by a fluent speaker
- `community-validated`: The content has been reviewed and confirmed by the instance's community review process

---

## Section 3: Federation Protocol

### 3.1 Core Protocol: ActivityPub + Extensions

The federation layer uses ActivityPub as the base protocol. Content items are
ActivityPub `Object` types; nodes are ActivityPub `Actor` types. The
standard ActivityPub inbox/outbox mechanics handle content propagation.

**Extensions required** (ActivityPub does not natively handle):
1. **Structured content queries**: ActivityPub is event-stream oriented; we need
   pull-based structured queries. Add a `GET /api/v1/items` OpenAPI endpoint
   alongside the ActivityPub inbox/outbox.
2. **Content addressing**: Each published item includes its IPFS CID in the object.
   When an item is received via federation, the receiving node verifies the CID
   matches the content before accepting.
3. **Endorsement propagation**: Endorsements are ActivityPub `Announce` activities
   with a structured payload. Any node can receive and display endorsements from
   any other node.

### 3.2 Federation Flow

```
Node A publishes a new procedure:
1. Item created, CID computed, item stored locally
2. ActivityPub Create activity broadcast to follower nodes (Node B, C, D...)
3. Node B receives Create activity, verifies CID, stores item locally
4. Node B indexes item in its local search index
5. Node B's search results now include Node A's item

Endorsement propagation:
1. Expert on Node C endorses item on Node A
2. Node C sends Announce activity to Node A + broadcasts to its followers
3. Node A attaches endorsement to item
4. Node D (following both A and C) sees item + endorsement
```

### 3.3 Minimal Federation API

Every node must expose:

| Endpoint | Method | Description |
|---|---|---|
| `/.well-known/webfinger` | GET | Node identity / actor discovery |
| `/actor` | GET | ActivityPub Actor object for the node |
| `/inbox` | POST | ActivityPub inbox for receiving activities |
| `/outbox` | GET | ActivityPub outbox (content feed) |
| `/api/v1/items` | GET | Paginated item listing with filters |
| `/api/v1/items/{id}` | GET | Single item retrieval |
| `/api/v1/items/{id}/endorsements` | GET | Endorsements for an item |
| `/api/v1/search` | GET | Full-text search within node |
| `/api/v1/export/zim` | GET | Trigger or download ZIM export |

**Query parameters for `/api/v1/items`**:

```
?type=procedure
?domain=procedural
?tags=water,filtration
?lang=es
?endorsed=true
?endorsementType=technical-verification
?since=2026-01-01T00:00:00Z
?limit=50&offset=0
```

---

## Section 4: Bootstrapping Plan

### Phase 1: Seed Content — Agricultural Domain (Months 1–3)

**Goal**: 100–200 high-quality seed items in the `procedural` domain, focused on
food production and water/sanitation. No new writing required — import and
structure existing open-licensed content.

**Sources to import**:

| Source | License | Content type | Volume |
|---|---|---|---|
| CAWST (Centre for Affordable Water and Sanitation) | CC BY | Water/sanitation procedures | ~30 documents |
| FAO TECA (Technologies for Agriculture) | CC BY-NC | Agricultural procedures | ~200 entries |
| Open Food Facts | ODbL | Recipes (food processing, preservation) | 2.8M (select best 1,000) |
| WikiHouse plans | CC BY-SA 4.0 | Building plans | ~80 designs |
| CERN Open Hardware Repository | CERN-OHL-S | Schematics | ~150 projects |
| Practical Action Technical Briefs | CC BY | Practical how-to procedures | ~120 briefs |
| AT&T (Appropriate Technology Transfer for Rural Areas) | Public domain | Agricultural procedures | ~500 publications |
| OpenFarm | CC0 | Growing guides (vegetables, herbs) | ~1,500 guides |

**Import pipeline**:
1. Fetch source content (respect robots.txt; use official APIs where available)
2. Extract structured data into `OpenRepoItem` JSON schema
3. Generate IPFS CIDs for each item
4. Human review of 10% sample per source for quality/accuracy
5. Load into seed node database
6. Tag with source attribution and import date

**Target**: 150 procedures, 50 recipes, 20 schematics, 10 building plans by end of Phase 1.

### Phase 2: First Public Node (Months 2–4, overlapping Phase 1)

**Goal**: A deployed, publicly accessible node that developers and researchers can interact with.

**Technical requirements**:
- Single VPS (2 vCPU, 4 GB RAM, 40 GB SSD) — cost: ~$20–$40/month
- PostgreSQL for structured data storage
- Meilisearch for full-text search
- IPFS node (Kubo) for blob storage
- ActivityPub implementation: use [Mastodon Go] or [Misskey] fork as base,
  or implement from scratch against the federation spec (more control; more work)
- FastAPI or Rust/Axum for the OpenAPI endpoints
- Simple React/Next.js read-only frontend for browsing

**Minimum viable frontend**:
- Search bar + results list
- Item detail page (title, steps, materials, schematics)
- Language switcher
- "Contribute" link to contribution form (next phase)

**Staffing**: This phase can be built by one developer in ~6–8 weeks. The
schema work in this document is the hard part; the API and database are
conventional.

### Phase 3: Contribution Flow (Months 4–6)

**Goal**: External contributors can submit new items without writing JSON.

**Contribution interface**:
1. **Simple web form**: Title, type (procedure/recipe/schematic), step-by-step editor
   with "add step" button, materials list builder, file upload
2. **Guided import**: Paste a URL from an existing source (Instructables, WikiHow, GitHub)
   and have the system attempt to parse and structure it; human confirms/corrects
3. **Mobile-first form**: Designed for phone submission (the typical contributor in
   a low-bandwidth context)
4. **Anonymous submit**: No account required for initial submission; goes into review queue
5. **Review queue**: Simple admin interface; one-click approve / request-changes / reject

**Review workflow**:
- All submitted items enter a draft state
- At least one registered contributor (with history) must approve before publishing
- Endorsements are added separately from the review workflow

### Phase 4: Federation (Months 6–9)

**Goal**: A second independent node runs and federates with the first.

**Federation bootstrap**:
1. Write the federation client/server code against the ActivityPub + extensions spec
2. Deploy a second test node in a different region
3. Establish federation connection between nodes
4. Verify that items on Node A appear in Node B's search index
5. Verify that endorsements propagate correctly
6. Document the process for a third-party to spin up a new node

**This is the phase that proves the architecture.** Until two independent nodes
are federating real content, the architecture is theoretical.

### Phase 5: Offline Export and Low-Bandwidth Access (Months 6–9)

**Goal**: A ZIM file containing the seed node's content is downloadable and
works in Kiwix on an offline device.

**ZIM generation**:
1. Export all items as static HTML (SSG output of Next.js or Hugo)
2. Include embedded images (IPFS-fetched, bundled)
3. Generate ZIM file using `zimwriterfs` (Kiwix tooling)
4. Host ZIM file on IPFS for distributed download
5. Submit to Kiwix Library catalog

**Target distribution**: The ZIM file should be useful in a school or clinic with
no internet access. A 1,000-item seed collection compresses to ~200–500 MB.

---

## Section 5: MVP Technical Stack (Definitive Choices)

Based on Phase 1–2 scope, these are the definitive MVP stack choices (subject to
revision by whoever actually builds it):

| Layer | Choice | Rationale |
|---|---|---|
| Backend language | Python (FastAPI) | Fastest to prototype; large ecosystem for text processing/NLP for import pipeline; can replace with Rust/Go later |
| Database | PostgreSQL 16 | JSON column support for content items; full-text search via pg_trgm for internal search; proven |
| Search | Meilisearch | Faster to deploy than Elasticsearch; excellent multilingual support; open source; can federate via API |
| IPFS | Kubo (go-ipfs) | Reference implementation; most interoperable; run as local daemon |
| ActivityPub | Custom implementation over FastAPI | Existing Python AP libraries (Little Federation, ActivityPub.py) are immature; simpler to implement the 5 required endpoints directly |
| Frontend | Next.js 15 (App Router) | SSG/SSR hybrid; good for SEO; can export to static HTML for ZIM generation |
| Hosting (seed node) | Hetzner VPS (CX21) | $6/month; EU jurisdiction; GDPR-compliant; adequate for 200 items |
| Content ID | IPFS CIDs (CIDv1, SHA2-256) | Standard; stable; no vendor dependency |
| Identity | DID:WEB | Simplest DID method to implement; no blockchain; maps to domain names |

---

## Section 6: What Success Looks Like at MVP

| Metric | Target |
|---|---|
| Items published | 200+ (Phase 1 seed) |
| Item types | procedure, recipe, schematic, plan, service-listing |
| Languages | Minimum 3 (English, Spanish, one African language — Swahili or Amharic) |
| API uptime | 99%+ (single node; no redundancy yet) |
| Search response time | < 500ms for full-text query |
| ZIM file available | Yes; downloadable from Kiwix Library or IPFS |
| Second federated node | Operational (Phase 4) |
| External contributors | 5+ people who found the project independently and submitted a contribution |
| Developer integrations | At least 1 external app (AI assistant, mobile app, or library system) querying the API |

---

## Open Questions Before Building

These must be answered before writing code:

1. **Who runs the seed node?** A university library, a cooperative, an NGO, or a personal server? This affects trust, sustainability, and jurisdiction.
2. **Which language gets content first?** English-only seed is simpler; multilingual seed is more honest about the mission. Recommendation: English seed, Spanish translation as Phase 1b.
3. **FAO TECA license clarification needed**: CC BY-NC means no commercial use. If the node ever accepts donations or runs ads (unlikely but possible), this creates a license problem. Check with FAO directly before ingesting TECA content.
4. **ActivityPub compatibility with existing Fediverse software**: Do we want items to appear in Mastodon timelines? This requires the items to be `Note` or `Article` types, which may conflict with the richer structured types. Decision: separate the structured data API from the social ActivityPub feed; the social feed is optional.
5. **Contribution spam prevention**: Anonymous contributions with no CAPTCHA will attract spam immediately. Options: proof-of-work (hashcash-style), honeypot fields, moderation queue only (no auto-publish). Recommendation: moderation queue is the safest MVP approach.

---

## Appendix: Content Licensing Policy

All content hosted on open-repo nodes must be under one of:
- Creative Commons (CC0, CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA)
- Open Database License (ODbL) for datasets
- Specific open hardware licenses (CERN-OHL, TAPR OHL)
- Public domain (pre-1928 works, government works in applicable jurisdictions)

Content under "All Rights Reserved" or proprietary licenses is not accepted.
When in doubt about license compatibility, contact the source before importing.

**Traditional knowledge caveat**: Content that documents traditional knowledge
of indigenous communities should carry the Local Contexts TK Label metadata
alongside any CC license. The TK Label system (localcontexts.org) provides
community-specific guidance on appropriate use. This is metadata, not enforcement —
but it is the ethically correct approach.
