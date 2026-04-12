---
title: "Open-Repo: Architecture Notes — Initial Design Thinking"
date: 2026-04-13
status: initial-draft
tags: [open-knowledge, architecture, federated, distributed]
---

# Open-Repo: Architecture Notes

## Core Thesis

The project should not try to be a better Wikipedia or a bigger Internet Archive. Both exist and both do their jobs reasonably well. The project's value is in three things none of the incumbents do:

1. **The practical knowledge layer**: structured, machine-readable how-to content (build, grow, repair, make, cook) linked across formats — text, 3D model, schematic, bill of materials, video
2. **The index/bridge layer**: a federated graph that ties together Wikipedia, Wikidata, OSM, Gutenberg, Printables, GitHub, Instructables, and everything else via stable URIs and semantic links
3. **The human exchange layer**: connecting knowledge to the people who hold it and the communities that need it — local skills, services, and mutual aid

---

## Architecture Decision: Federated, Not Centralised

### Why not centralised?

The centralised model is the failure mode we have already observed:
- Internet Archive: single organisation, single set of servers, subject to legal attack, funding crises, and state censorship. The 2024 hack and subsequent legal defeats are not anomalies; they are the predictable outcome of centralisation
- Thingiverse: corporate ownership drift; Instructables: Autodesk acquisition; decay or restriction follows
- Anna's Archive: cannot be officially cited or linked to; legally precarious; survives only because it is technically distributed

A single organisation owning "all of humanity's knowledge" recreates the exact control problem the project is meant to solve.

### Why not pure peer-to-peer?

Pure IPFS / BitTorrent has the opposite problem: content disappears when nobody is pinning it. The 2025 ACM WWW paper documents that IPFS in practice is already highly centralised — most traffic routes through a handful of gateways. Without economic incentives for persistence, content that isn't popular vanishes.

### The right model: federated instances + IPFS content addressing

Inspired by:
- **ActivityPub / Fediverse**: independently hosted instances that speak a common protocol. Mastodon (~9,000 servers), PeerTube, Pixelfed all demonstrate that this model can achieve global scale without a central controller
- **IPFS for content**: store blobs (files, images, models, PDFs) on IPFS with pinning redundancy; use content hashes as stable identifiers that work across hosts
- **Wikidata's data model**: stable QIDs, structured triples, SPARQL queryable — but extended to non-encyclopedic content

**Recommended architecture:**

```
[Content Nodes]           [Index Layer]           [Client Apps]
Instance A ──────────────► Federated Graph ◄────── Web app
Instance B ──────────────► (ActivityPub + ◄────── Kiwix export
Instance C ──────────────►  OpenAPI)       ◄────── Mobile app
...                                         ◄────── AI/LLM access
         ▼
[IPFS / Filecoin]
(content-addressed blob storage)
```

Each instance hosts a domain of content (e.g., one community runs the agricultural knowledge node; another runs the electronics schematics node). The federated graph indexes all of them with a shared metadata standard. Content blobs are stored on IPFS with pinning by multiple nodes for redundancy.

---

## Content Taxonomy

The taxonomy must be flat enough to be learnable but structured enough to enable cross-domain discovery. Proposed top-level domains:

### Tier 1: Knowledge Domains

| Domain | Description | Links to Existing Sources |
|---|---|---|
| **encyclopedic** | Facts, concepts, entities | Wikipedia, Wikidata |
| **scientific** | Research, papers, data | Semantic Scholar, arXiv, PubMed |
| **textual** | Books, documents, primary sources | Gutenberg, Wikisource, Open Library |
| **educational** | Courses, exercises, curricula | Khan Academy, LibreTexts, OpenStax |
| **procedural** | How-to: build, repair, grow, cook, make | **Primary gap to fill** |
| **geospatial** | Maps, places, local information | OpenStreetMap |
| **physical** | 3D models, schematics, BOM, plans | Printables, GitHub, GrabCAD, WikiHouse |
| **exchange** | Services, skills, time banking | hOurworld, Shareish |
| **cultural** | Traditional knowledge, oral history, arts | **Critical gap** |
| **biological** | Species, ecosystems, agriculture | iNaturalist, GBIF |

### Tier 2: Content Types (cross-domain)

Each piece of content has a `type` independent of its `domain`:

- `article` — text document
- `procedure` — step-by-step instructions (machine-readable)
- `model-3d` — STL/OBJ/STEP file
- `schematic` — circuit diagram, mechanical drawing
- `plan` — building/construction plan
- `recipe` — procedure with ingredients/quantities/scaling
- `dataset` — structured data
- `media` — image, audio, video
- `service-listing` — a person or group offering a skill or service

### Content Linking

A `procedure` for building a solar water heater would have typed links to:
- `model-3d` — STL for the collector frame
- `schematic` — pipe layout drawing
- `article` — Wikipedia article on solar thermal principles (Wikidata QID)
- `recipe` — the fill-fluid mixture instructions
- `dataset` — performance data for different climates
- `service-listing` — local builders who have built this design

This cross-linking is what none of the existing platforms do and what makes the whole worth more than the sum of parts.

---

## Identity and Contribution Model

### The contribution model that works at scale

From studying what actually scales:
- **Wikipedia**: works because the barrier to contribute is low (edit a text field) and the feedback loop is fast
- **OpenStreetMap**: works because contribution is grounded in ground truth — you are adding what you can personally verify is there
- **Open Food Facts**: works because contribution is a single atomic action (scan product, confirm data) with immediate value to the contributor
- **GitHub**: works because the contribution unit (the pull request) is self-contained and reviewable

The failure mode is: requiring registration before contributing anything, requiring expertise before contributing, and requiring a full submission before any feedback.

**Proposed model:**

1. **Anonymous micro-contributions**: fix a typo, confirm a step is correct, tag a photo — no account required, stored as signed edits with IP/timestamp
2. **Identified contributions**: create an account to author new content, comment, propose structured edits. Account is a DID (Decentralized Identifier) — not tied to any single instance
3. **Expert endorsement**: domain-verified contributors (e.g., a licensed electrician) can endorse procedural content; endorsements are metadata, not gatekeeping
4. **Institutional mirroring**: organisations (libraries, universities, NGOs) can mirror an instance and contribute their collections under the federation protocol

### Identity: Decentralized Identifiers (DID)

Use W3C DIDs rather than instance-local accounts. A contributor's identity is portable across instances — if the node they registered on goes down, their contributions remain attributed to them. This solves the single-instance dependency problem that plagues Mastodon accounts.

---

## Discovery Layer

### The hard problem

Search and discovery is harder to federate than content storage. Existing approaches:

- **Wikidata SPARQL**: powerful but requires query expertise; single endpoint bottleneck
- **ActivityPub**: designed for social feeds, not structured knowledge queries
- **Elasticsearch / Solr**: centralised; fast; the incumbent model
- **Semantic search / vectors**: promising; Wikidata added vector embeddings in October 2025

**Recommended approach: layered search**

1. **Full-text search**: each instance runs its own Meilisearch/Typesense node; federated via a lightweight aggregation protocol (similar to how SearXNG aggregates search results)
2. **Graph queries**: a subset of Wikidata-compatible SPARQL over the federated graph for structured queries
3. **Semantic/vector search**: content embeddings generated at ingest; stored alongside IPFS CID; queryable for "similar to" discovery
4. **Offline index**: periodic export of the full index as a compressed file suitable for Kiwix or offline deployment

### Taxonomy-aware routing

Queries are routed to the relevant domain nodes first. A query for "how to build a rainwater harvesting system" routes primarily to `procedural` + `physical` nodes, with supplementary results from `encyclopedic` and `scientific`. This keeps response times reasonable without requiring a global index of everything.

---

## Governance Model

### The fundamental problem

Every sufficiently large open platform faces the same crisis: who decides what stays, what goes, and what the rules are? Wikipedia's answer (centralised bureaucracy + policy) works at Wikipedia's scale but excludes huge populations. Mastodon's answer (instance-level autonomy + defederation) works for social content but produces fragmentation.

For a knowledge commons, the stakes are higher: bad information kills people (medical misinformation), discriminatory curation excludes communities, and corporate capture can happen gradually.

### Recommended governance structure: layered autonomy with cross-instance consensus

Inspired by Bluesky's "stackable moderation" model (open-sourced as Ozone in 2024):

**Layer 1 — Instance autonomy**: Each federated instance sets its own rules for content in its domain. An agricultural knowledge node run by a farming cooperative has different standards than a medical knowledge node run by a public health organisation. No central authority overrides instance-level decisions.

**Layer 2 — Cross-instance shared labels**: Instances can subscribe to shared label services (e.g., "this content contains dangerous medical advice" or "this schematic has been verified by a licensed engineer"). Labels are metadata; they inform but do not enforce. Users choose which label services to trust.

**Layer 3 — Protocol-level invariants**: A small number of rules that are enforced at the protocol level across all instances: no CSAM, no content that doxes individuals, content must have a declared license. These are minimal and hard to dispute.

**Layer 4 — Federation network governance**: The group of federated instance operators elects a technical steering committee that governs only the protocol and metadata standards, not content. Any instance can propose protocol changes; adoption is voluntary; incompatible forks are acceptable (the network fragments rather than being controlled).

### Content moderation in practice

The academic literature (Policy Review 2025, Carnegie Endowment 2025) shows decentralised moderation works for social content but struggles with:
- Coordinated inauthentic behaviour at scale
- Automated spam and manipulation
- Smaller instances lacking tooling for automated detection

Mitigations:
- Open-source the moderation tooling (Bluesky's Ozone model)
- Trust scores based on contribution history and endorsements
- Cross-instance blocklists for known bad actors (federated, opt-in)
- Rate limiting on anonymous contributions

---

## Technical Stack Recommendations

These are directional, not final decisions. The point is to avoid lock-in.

| Layer | Technology | Rationale |
|---|---|---|
| Protocol | ActivityPub + extensions | W3C standard; proven at scale; existing tooling |
| Storage (blobs) | IPFS + Filecoin pinning | Content addressing; censorship resistance |
| Storage (structured data) | PostgreSQL + RDF triples | Wikidata-compatible data model |
| Search | Meilisearch (per instance) + aggregator | Open source; fast; federable |
| Identity | W3C DID (did:web or did:plc) | Portable; decentralised; no vendor lock-in |
| API | OpenAPI 3.x + SPARQL endpoint | Machine-readable; LLM/AI compatible |
| Export | ZIM format (Kiwix-compatible) | Offline distribution to low-bandwidth contexts |
| Frontend | Progressive Web App | Works offline; installable; cross-platform |

### What to build first vs. what to federate

**Do not build from scratch:**
- Encyclopedic content (link Wikidata)
- Scientific papers (link Semantic Scholar / arXiv)
- Maps (link / embed OpenStreetMap)
- Public domain texts (link Gutenberg / Wikisource)
- 3D model files (federate with Printables / MyMiniFactory via API)

**Build the missing layer:**
- The schema and protocol for `procedure`, `recipe`, `schematic`, `plan`, `service-listing` content types
- The cross-domain linking graph
- The federated search aggregation layer
- The contribution UX for non-technical users
- The offline/Kiwix export pipeline

---

## Hard Problems and Open Questions

### 1. Bootstrap problem

A federated network with no content is useless. Seeding requires either:
a) Importing existing open-licensed content (Open Food Facts recipes, WikiHouse plans, Instructables with CC licenses, CERN Open Hardware Repository)
b) Focusing on a single high-value niche first (e.g., agricultural techniques for the Global South) and building out from there
c) Partnering with an existing community that has the content

**Recommendation:** Start with a single domain (agricultural / food production seems highest impact globally), get the protocol right there, then expand.

### 2. Sustainability without corporate control

Options:
- Grants (Wikimedia Foundation model) — sustainable until they aren't
- Donations (Internet Archive model) — fragile; see 2024
- Protocol fees (Filecoin model) — creates a market but introduces financialisation
- Instance operator network (Mastodon model) — community-sustained but requires critical mass

**Best bet:** Grants + donations for the protocol layer and seed instances; instance operator network for long-term sustainability. The protocol itself must be free to run; the network effects come from interoperability, not control.

### 3. Quality vs. openness

Open contribution creates noise. Closed curation creates bias. The middle path is endorsement-as-metadata: content is visible without endorsement, but endorsements from trusted sources are surfaced prominently. A rural farmer's technique for dry-season irrigation does not need a PhD's endorsement to be visible — but a PhD's confirmation that it's agronomically sound adds value.

### 4. Language and non-Western knowledge

Wikipedia's English-first bias is well-documented. Traditional and indigenous knowledge is almost entirely absent from digital archives. This project should:
- Build first-class multilingual support into the data model (Wikidata's per-language labels are the right model)
- Actively recruit non-English-speaking instance operators
- Design contribution flows that work with low-bandwidth connections and basic smartphones
- Consider oral knowledge formats: audio recordings with structured metadata are a content type, not a second-class citizen

### 5. The legal minefield

- In-copyright content: do not host; link where legally accessible; advocate for copyright reform
- Traditional knowledge: respect indigenous IP frameworks (Local Contexts / TK Labels); do not harvest without consent
- Building codes and legal standards: vary by jurisdiction; schematic accuracy disclaimers required
- Medical / safety content: require expert endorsement labels; never present as legal/medical advice

---

## Summary: What to Build

The open-repo project should build:

1. **A metadata schema and protocol** for practical knowledge types: `procedure`, `recipe`, `schematic`, `plan`, `service-listing`, with cross-linking to `encyclopedic` and `scientific` content via Wikidata QIDs
2. **A federated node software** (ActivityPub-based) that any community can run to host their domain of knowledge
3. **A contribution UX** optimised for mobile, low-bandwidth, and non-technical contributors — scanning, voice, photo, simple form
4. **A federated search index** that aggregates across instances and integrates external sources (Wikidata, OSM, Semantic Scholar)
5. **An offline export pipeline** producing Kiwix-compatible ZIM files for distribution in low-connectivity contexts
6. **A governance framework** (not software — a document and a community process) for the protocol steering committee

What it should not build: another Wikipedia, another Internet Archive, another GitHub. Those exist. Build the bridge and fill the gaps.

---

## Sources

- [ActivityPub — W3C Standard](https://www.w3.org/TR/activitypub/)
- [Fediverse — Wikipedia](https://en.wikipedia.org/wiki/Fediverse)
- [Bluesky stackable moderation / Ozone](https://bsky.social/about/blog/03-12-2024-stackable-moderation)
- [Decentralised content moderation — Policy Review](https://policyreview.info/glossary/decentralised-content-moderation)
- [Carnegie Endowment: Defederation on decentralized platforms](https://carnegieendowment.org/research/2025/03/fediverse-social-media-internet-defederation?lang=en)
- [Centralization in IPFS — ACM WWW 2025](https://dl.acm.org/doi/10.1145/3696410.3714627)
- [IPFS — Wikipedia](https://en.wikipedia.org/wiki/InterPlanetary_File_System)
- [Wikidata adds AI vectors — Diginomica](https://diginomica.com/wikidata-adds-ai-vectors-graph-and-knowledge-bases-heres-why)
- [Federated knowledge graphs — Wikimedia Meta](https://meta.wikimedia.org/wiki/Federated_knowledge_graphs)
- [WikiHouse](https://www.wikihouse.cc/)
- [Distributed Manufacturing of Open Hardware — NYU Law](https://www.law.nyu.edu/sites/default/files/DistributedManufacturingofOpenHardware.pdf)
- [Open Food Facts](https://github.com/openfoodfacts)
- [Shareish mutual aid — ACM](https://dl.acm.org/doi/10.1145/3593743.3593790)
- [Kiwix](https://kiwix.org/en/)
- [Wikidata Platform — MediaWiki](https://www.mediawiki.org/wiki/Wikidata_Platform)
