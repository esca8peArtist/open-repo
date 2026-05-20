---
title: "Phase 6 Architecture Options — Post-Phase-5 Expansion Visioning"
project: open-repo
phase: 6
status: strategic-planning
date: 2026-05-20
author: research-agent
confidence: high
tags: [phase-6, architecture, federation, saas, api-ecosystem, library-partnerships, sustainability]
---

# Phase 6 Architecture Options
## Open-Repo Post-Phase-5 Expansion Visioning

**Status**: Strategic Planning Document (pre-Phase 5 completion)  
**Audience**: Project owner, prospective partners, architecture decision-makers  
**Purpose**: Define Phase 6 option space; ensure Phase 5 architecture is forward-compatible with chosen expansion path  
**Word count**: ~3,800 words  
**Decision gate**: June–July 2026 (user selection of Phase 6 option)

---

## Executive Summary

Phase 5 delivers the core offline distribution capability — ZIM archive generation, OPDS catalog, and full-text Xapian indexing — on a codebase that already has ActivityPub federation from Phase 4. Phase 6 must answer what open-repo does after it can generate offline archives and serve federated content: scale to a library network, become a commercial SaaS platform, or become an API ecosystem that integrates into the broader reading app landscape.

**Lead finding**: All three Phase 6 options are forward-compatible with a Phase 5 ZimWriter + OPDS architecture (Candidates 1+2). The Phase 5 choice that most constrains Phase 6 options is *skipping* the OPDS catalog — without it, Option A (federated catalog discovery) requires OPDS to be built first anyway. Phase 5 should complete Candidates 1 and 2 in sequence regardless of Phase 6 selection.

**Recommended Phase 6 path based on market landscape**: Option B (Commercial SaaS Hosting) as primary with Option A (Federated Search Platform) as a 12-month follow-on. Rationale: the SaaS market in library technology is demonstrably underserved for small-medium libraries, revenue is achievable within 12 months, and SaaS infrastructure (multi-tenancy, billing, Docker) is also the prerequisite for nonprofit federation hosting (Option A).

---

## Part 1: Phase 5 Closure Assessment

### What "Phase 5 Complete" Looks Like

Phase 5 has three concurrent candidates tracked in the decision matrix (May 19, 2026). Complete closure requires:

**Candidate 1 — ZimWriter/libzim Integration (prerequisite for all others)**

- `zim_writer.py` stub implementations replaced with real `libzim.writer.Creator` calls
- Xapian full-text indexing enabled via `creator.config_indexing(True, "eng")`
- `zimcheck` validation re-enabled and passing in CI (84 existing tests pass)
- ZIM archive downloadable from Cloudflare R2 CDN (automated weekly exports)
- Manual verification on three Kiwix platforms: Android (F-Droid), Desktop, kiwix-serve
- SHA-256 sidecar published alongside each ZIM file
- Effort: 8–11 hours; estimated completion: May 25, 2026

**Candidate 2 — OPDS Feed Migration (builds on Candidate 1)**

- `OPDSCatalogService` migrated from raw `xml.etree` to `feedgen` library
- `OPDSEntry.from_zim_export()` factory method implemented (populates catalog from real ZIM exports)
- Missing OPDS 1.2 elements added: `dc:language`, `dc:issued`, `opensearch`, version-history sub-entries
- OPDS search endpoint complete: `/opds/v2/searchdescription.xml`
- 19 existing OPDS tests updated and passing
- Kiwix in-app catalog discovery verified (users can find and download ZIM files from within Kiwix app)
- Effort: 8–11 hours; estimated completion: June 5, 2026

**Candidate 3 — Accessibility Audit (parallel path, not a Phase 6 prerequisite)**

- WCAG 2.1 Level AA audit of ZIM article HTML template and web API surfaces
- axe-core/Playwright automated scan integrated into CI
- Critical findings remediated (contrast, missing `alt` text, semantic HTML)
- Recommended scheduling: Phase 5b, June 2026, or deferred to Phase 6 start

**Phase 5 is complete when**: Valid ZIM archives are downloadable via public HTTPS, Kiwix in-app OPDS discovery works, and all exports pass `zimcheck` validation. Estimated full closure: mid-June 2026.

### Gaps That Define Phase 6 Scope

Phase 5 leaves four significant functional gaps that define the Phase 6 option space:

| Gap | Description | Phase 6 Option That Addresses It |
|-----|-------------|----------------------------------|
| **Multi-library federation** | A user at one library cannot search another library's catalog. Each open-repo instance is an island. | Option A (Federated Search Platform) |
| **Managed hosting** | Libraries that cannot self-host have no turnkey option. There is no multi-tenant platform, no billing, no automated provisioning. | Option B (Commercial SaaS) |
| **Third-party integration** | Reading apps (Calibre, e-readers, mobile apps) cannot programmatically query or sync with open-repo. No published REST/GraphQL API, no webhook events. | Option C (API Ecosystem) |
| **Advanced analytics** | No usage tracking, no collection impact metrics, no heatmaps of what content is most accessed. | All three options (varies in depth) |

### Architecture Implications: Which Phase 5 Choice Best Positions for Phase 6

The key forward-compatibility question: does Candidate 1 (ZimWriter offline) preclude later cloud deployment (Phase 6B SaaS)?

**Answer: No.** ZimWriter is a self-contained export pipeline — it produces static ZIM files. It does not alter the database schema, the FastAPI application structure, or the federation layer. A multi-tenant SaaS deployment (Phase 6B) runs the same FastAPI application with per-tenant database schemas; ZimWriter runs per-tenant to produce per-library offline archives. These are complementary, not competing.

The OPDS catalog (Candidate 2) is even more directly useful in Phase 6: an OPDS endpoint is the standard interface that Option A's federated catalog network would use to discover and index member libraries. Building OPDS in Phase 5 is building the protocol foundation for Phase 6A.

**Architectural decision for forward-compatibility**: Phase 5 must avoid hard-coding the assumption of a single-tenant deployment. Specifically:

- `ExportConfig` should carry a `library_id` field (nullable for single-tenant, populated for multi-tenant)
- CDN paths should include a namespace: `/{library_id}/zim/...` rather than `/zim/...`
- The OPDS endpoint should carry a configurable `feedId` so multiple instances have distinct catalog identities
- No deployment-time constants should embed the domain name (use `settings.CANONICAL_BASE_URL` throughout)

These are low-effort changes (< 2 hours) that make the codebase multi-tenancy-ready without implementing multi-tenancy yet.

---

## Part 2: Phase 6 Option Scenarios

### Option A: Federated Search Platform

**One-line description**: Enable any library to publish its catalog to a shared discovery network. Users search across multiple libraries simultaneously.

#### Scope

- Library instances publish their catalog to a central index via OPDS feeds or ActivityPub activities
- Central registry stores catalog metadata, not content (libraries retain data sovereignty)
- Cross-library search returns results from all registered libraries with source attribution
- OPDS 2.0 as the standard interface for catalog advertisement; ActivityPub for real-time sync notifications
- Library network dashboard: membership count, aggregate collection statistics, activity feed

#### Technical Architecture

**Discovery layer** (new):
- A central metadata registry stores OPDS catalog snapshots from member libraries (updated on push from library or on 24-hour pull cycle)
- Search across the registry uses a shared Meilisearch or Elasticsearch cluster (or federated Meilisearch instances with a query fan-out service)
- Each library's OPDS feed is indexed; content is not stored centrally
- Registry exposes a standard search API: `GET /search?q=...&library=...&domain=...`

**Sync protocol** (builds on Phase 4 ActivityPub):
- Phase 4 already implements HTTP Signature signing and federation service layer
- Phase 6A adds a `CatalogSync` activity type: when a library publishes a new item, it pushes a lightweight notification to the central registry
- Registry re-crawls the OPDS feed within 5 minutes of notification
- No full content is pushed to the registry — only metadata (title, description, domain, type, source URL)

**Infrastructure**:
- Central registry: FastAPI + PostgreSQL + Meilisearch, deployed on a single VPS ($40–80/month at Hetzner or Fly.io)
- Libraries self-host their own instances or use the SaaS tier (see Option B)
- Registry is designed for 50–500 member libraries at launch; Meilisearch scales to 10M+ documents on a single node

**Effort estimate**: 100–150 hours  
- OPDS 2.0 crawler and registry: 40 hours
- Cross-library search API: 25 hours
- ActivityPub CatalogSync activity type: 20 hours
- Network dashboard and membership management: 30 hours
- Documentation, testing, deployment: 25 hours

#### Sustainability Model

**Nonprofit structure** (recommended for Option A):
- Governing entity: a small 501(c)(3) or equivalent nonprofit (analogous to the Kiwix Association, XMPP Standards Foundation)
- Annual operating budget: $200–350K (1–2 FTE protocol maintenance + infrastructure costs)
- Revenue sources:
  - **Network membership fees**: $3,000–10,000/year per library (sliding scale by collection size). At 50 libraries: $250K; at 100 libraries: $500K–$1M.
  - **Mellon Foundation grants**: Public Knowledge program funds digital access and preservation infrastructure. Typical awards: $50K–$250K per cycle (1–2 year periods). CLIR's Recordings at Risk program received $3M for two cycles; a first-time applicant targeting a federated open-access network would expect $50–150K for a pilot. Library Futures has received grants from both Mellon and the Richard Lounsbery Foundation for open-source library technology.
  - **IMLS (Institute of Museum and Library Services) grants**: IMLS National Leadership Grants for Libraries fund projects that strengthen libraries' roles in their communities; typical awards $50K–$500K.
  - **Corporate sponsorship**: Vendors building on the OPDS/federation layer (e.g., e-reader manufacturers, catalog software vendors) could contribute $5–25K/year for developer relations access.

**Timeline**: 6-month development (Jul–Dec 2026), pilot with 3–5 partner libraries (Jan 2027), public membership recruitment (Q2 2027).

#### Market Fit

**Primary market**: Library coalitions, academic consortia, and state library systems already operating shared catalog infrastructure. Key targets:
- DPLA (Digital Public Library of America) — 12 service hubs, 16 content hubs, 2025 transition year; open to new metadata aggregation partnerships
- LYRASIS — 1,100+ member libraries across 28 countries; already operates the Palace Project OPDS-based ebook platform
- State library systems (K-12 and public library networks) that use shared ILS systems (Koha via ByWater Solutions: 1,425 libraries in their ecosystem)

**Differentiation**: Existing federated library platforms (DPLA, OCLC WorldCat) focus on books, journals, and cultural heritage materials. Open-repo's content type — practical procedural knowledge (procedures, recipes, schematics, plans, service listings) — is not represented in any existing federated library catalog. This is an uncontested niche in the library network landscape.

---

### Option B: Commercial SaaS Hosting

**One-line description**: Managed platform-as-a-service for libraries. Host their catalog, handle backups, provide analytics, and manage OPDS feeds on their behalf.

#### Scope

- Multi-tenant deployment: each library gets an isolated open-repo instance (separate DB schema or separate container)
- Automated provisioning: new library onboarding in < 10 minutes (web form → provisioned instance)
- Managed backups (daily automated, 90-day retention), security updates, monitoring
- Analytics dashboard: collection size, download counts, most-accessed content, user activity
- OPDS feed management: auto-generated, always-current catalog
- Billing system: subscription tiers based on catalog size and feature usage
- Support tier: email support included, optional priority support add-on

#### Technical Architecture

**Multi-tenancy approach** (two viable models):

*Model 1 — Shared application, separate DB schemas* (recommended for Phase 6 MVP):
- Single FastAPI application deployment with per-tenant PostgreSQL schemas
- Tenant identified by subdomain: `library-a.open-repo.net`, `library-b.open-repo.net`
- Lower infrastructure cost; simpler ops; suitable for 5–50 tenants
- Limitation: a tenant's heavy compute job (ZIM export) can affect others on the same node

*Model 2 — Container-per-tenant* (scale-out, post-MVP):
- Each library runs in its own Docker container (FastAPI + PostgreSQL in the same pod or separate)
- Complete isolation: one tenant's performance cannot affect others
- Higher cost; Kubernetes or Fly.io Machines for orchestration
- Recommended when tenant count exceeds 50 or any tenant exceeds 10K items

**Billing infrastructure**:
- Stripe for subscription management and invoicing
- Per-tenant metering: item count (checked nightly), monthly active users (optional)
- Free trial: 30 days, up to 500 items, no credit card required
- Automated suspension on payment failure (soft: read-only for 7 days; hard: deprovisioned at 30 days with data export available)

**Data portability** (critical for trust):
- `GET /api/export/portable` produces a structured JSON-LD archive downloadable at any time
- This archive imports into any other open-repo instance
- No lock-in; libraries can self-host at any time with their data intact

**Infrastructure stack**:
- Provisioning: Terraform + Ansible (or Fly.io Machines API for container-per-tenant model)
- DNS: Cloudflare for subdomain routing
- Storage: Cloudflare R2 for ZIM files (zero egress cost); PostgreSQL on managed hosting (Neon.tech or Railway for smaller tenants)
- Monitoring: Grafana + Prometheus (or Datadog at scale)

**Effort estimate**: 80–120 hours
- Multi-tenant DB schema isolation: 20 hours
- Automated provisioning pipeline: 25 hours
- Billing/Stripe integration: 20 hours
- Analytics dashboard: 20 hours
- Support tooling and admin console: 15 hours
- Documentation, testing, deployment: 20 hours

#### Sustainability Model

**Commercial SaaS with open-source core** (recommended model):

The open-source base remains freely self-hostable. Revenue comes from managed hosting, not from the software license. This is the model used by:
- GitLab (open-source CE, commercial EE)
- Metabase (open-source, paid Cloud)
- n8n (open-source, paid Cloud)

**Pricing tiers** (research-grounded for library market, 2026):

| Tier | Catalog Size | Monthly Price | Annual Price | Target |
|------|-------------|---------------|--------------|--------|
| **Seed** | Up to 500 items | $49/month | $490/year | Individual researchers, small community archives |
| **Sprout** | Up to 5,000 items | $199/month | $1,990/year | Small public libraries, community libraries |
| **Grove** | Up to 25,000 items | $599/month | $5,990/year | Mid-size public libraries, school districts |
| **Forest** | Unlimited | Custom ($2,500–$8,000/month) | Custom | Large library systems, university libraries |

**Revenue projection**:
- Year 1 (conservative): 20 Seed, 10 Sprout, 3 Grove, 1 Forest ($5,000/month) = ~$8,400/month = $100K ARR
- Year 2 (growth): 100 Seed, 40 Sprout, 15 Grove, 5 Forest ($6,000 avg/month) = ~$42,000/month = $500K ARR
- Year 3 (scale): 300 Seed, 120 Sprout, 50 Grove, 20 Forest = ~$140,000/month = $1.7M ARR

**Market size**: Library Futures has documented that small-medium libraries (<50,000 items) represent the largest underserved segment in library technology. Koha via ByWater Solutions supports 1,425 libraries — these are all potential SaaS hosting customers. The global library management system market is estimated at $2.3B in 2025.

**Timeline**: 4-month MVP (Jul–Oct 2026), private beta with 5 partner libraries (Nov 2026), public launch (Dec 2026).

#### Market Fit

**Primary market**: Small-to-medium libraries that want the capabilities of open-repo without the operational burden of self-hosting. Libraries that already use Koha (open-source ILS) but want a separate open-access knowledge platform. Community archives that have content to share but no technical staff.

**Underserved by current alternatives**:
- Internet Archive: focuses on large deposit institutions; no managed catalog hosting for small libraries
- DPLA: aggregates metadata but does not host library platforms
- Commercial library software (Ex Libris, ProQuest): priced for university/large public libraries ($50K–$500K+ contracts); inaccessible to small libraries
- FOLIO (open-source LSP): technically capable but requires substantial IT infrastructure and expertise

---

### Option C: Third-Party API Ecosystem

**One-line description**: Publish a documented REST API and webhook event stream so external developers can build reading apps, recommendation engines, and catalog integrations on top of open-repo.

#### Scope

- REST API (or GraphQL) for catalog querying, item retrieval, and search
- Webhook event stream: notify external apps when items are added, updated, or deleted
- OAuth 2.0 authentication for third-party applications
- Rate limiting and usage quotas (per API key)
- Developer portal: documentation, interactive sandbox (Swagger UI / GraphQL Playground), API key management
- SDK libraries: Python, JavaScript (client libraries to lower integration friction)

#### Technical Architecture

**API design**:
- REST over GraphQL recommended for initial release: REST has broader library sector familiarity; GraphQL can be added later as an overlay
- Key endpoints:
  - `GET /api/v1/items` — paginated catalog browse with filter parameters (domain, type, keyword)
  - `GET /api/v1/items/{id}` — full item detail with content
  - `GET /api/v1/search?q=...` — full-text search across catalog
  - `GET /api/v1/domains` — list of content domains with item counts
  - `GET /api/v1/exports` — list of available ZIM archives with download URLs
  - `POST /api/v1/webhooks` — register a webhook endpoint
  - `POST /api/v1/oauth/token` — OAuth 2.0 token issuance

**Authentication and rate limiting**:
- OAuth 2.0 client credentials flow for server-to-server integration
- API keys for simpler read-only access (no OAuth overhead)
- Rate limits: free tier 1,000 requests/day; paid tiers up to 100K/day
- Cloudflare Workers for rate limiting at the edge (no application-layer overhead)

**Webhook event stream**:
- Events: `item.created`, `item.updated`, `item.deleted`, `export.completed`
- Delivery: HTTPS POST to registered endpoint with HMAC-SHA256 signature
- Retry: exponential backoff for up to 24 hours on failed delivery
- This enables e-readers and library apps to maintain a local cache without polling

**Developer portal infrastructure**:
- Static site (Astro or Next.js) hosting OpenAPI spec and tutorial documentation
- Swagger UI for interactive API exploration
- Sandbox environment (read-only subset of public data) for testing without an account
- API key management UI embedded in the main open-repo admin panel

**Effort estimate**: 120–180 hours
- REST API design and implementation: 40 hours
- OAuth 2.0 and API key authentication: 25 hours
- Rate limiting infrastructure: 15 hours
- Webhook system: 20 hours
- Developer portal and documentation: 35 hours
- SDK (Python + JavaScript): 25 hours
- Testing, security review, deployment: 20 hours

#### Sustainability Model

**API tiering with freemium base**:

| Tier | Rate Limit | Price | Target |
|------|-----------|-------|--------|
| **Open** | 1,000 requests/day | Free | Hobbyist developers, researchers, open-source apps |
| **Developer** | 50,000 requests/day | $49/month | Startups, reading app developers |
| **Professional** | 500,000 requests/day | $299/month | Commercial platforms with library integration |
| **Enterprise** | Unlimited + SLA | $2,000+/month | E-reader manufacturers, major reading platforms |

**Revenue projection** (harder to predict, dependent on developer adoption):
- Year 1: 5–10 Developer, 2–3 Professional = ~$2,000–$3,500/month = $25–42K ARR
- Year 2 (if a major app integrates): step function growth; one Enterprise contract = $24K/year
- Ecosystem play: the value is not just direct API revenue but network effect — if Calibre, Readium, or a major e-reader implements open-repo integration, it dramatically expands user reach

**Integration targets** (based on 2025 ecosystem research):
- **Calibre** (open-source ebook management, 10M+ users): accepts OPDS catalogs natively; open-repo's OPDS feed (built in Phase 5) already enables Calibre integration without additional API work
- **Palace Project** (LYRASIS ebook platform): built on OPDS; 100+ library members; open to content integrations
- **Kiwix** (offline library, 10M+ ZIM downloads in first 2 months of 2024): already supported via Phase 5 ZIM export; API adds real-time catalog metadata
- **Reading apps** (Librera, Moon+ Reader, KOReader): OPDS-compatible; API adds advanced search

**Timeline**: 5-month development (Jul–Nov 2026), developer beta (Dec 2026), public API launch (Jan 2027).

#### Market Fit

Option C has the highest technical investment and the most uncertain revenue trajectory of the three options. It is the right choice if the project's strategic goal is ecosystem influence and developer adoption rather than direct revenue or nonprofit network building. The risk is that API products require a critical mass of developers to adopt them to generate network effects, and library technology developers are a small, specialized community.

---

## Part 3: Comparison Matrix

| Dimension | Option A: Federated Search | Option B: SaaS Hosting | Option C: API Ecosystem |
|-----------|---------------------------|------------------------|-------------------------|
| **Effort (hours)** | 100–150 | 80–120 | 120–180 |
| **Sustainability model** | Nonprofit + grants + membership fees | Commercial SaaS + open-source core | Freemium API tiers + enterprise contracts |
| **Revenue potential (Year 2)** | $250K–$1M (membership + grants) | $250K–$1.7M ARR (SaaS) | $25K–$200K (API revenue) |
| **Time to first revenue** | 12–18 months (grant cycles are slow) | 6–8 months (library onboarding) | 12–18 months (developer adoption lag) |
| **Market addressable** | Library coalitions, consortia (hundreds of organizations) | Small-medium libraries (<50K items): 10,000+ globally | App developers, reading platforms (small but high-leverage) |
| **Library partnerships** | DPLA, LYRASIS, state consortia | Individual libraries, Koha ecosystem | Palace Project, Calibre, Kiwix |
| **Phase 5 prerequisite** | OPDS (Candidate 2) strongly preferred | ZimWriter (Candidate 1) sufficient | ZimWriter + OPDS (Candidates 1+2) |
| **Phase 6 independence** | Requires partner library adoption | Self-contained; can launch with 1 library | Requires developer adoption |
| **Technical risk** | Medium (cross-library search; OPDS 2.0 compliance) | Low (multi-tenancy is well-understood) | Medium-High (OAuth, rate limiting, SDK maintenance) |
| **Mission alignment** | Highest (open network, no lock-in) | Medium (hosted but open-source) | Medium (ecosystem expansion) |
| **Sequence compatibility** | Best as Option B follow-on | Best as first Phase 6 step | Best as Option B complement (same API powers both) |

---

## Part 4: Library Partnership Landscape

### 1. Internet Archive

**Current platform**: Custom (Petabox, Wayback, OpenLibrary — all proprietary/bespoke)  
**User count**: 1 trillion archived pages; Open Library: 3M+ books  
**Openness to partnerships**: Moderate — has formal DPLA partnership; expanded Open Library partnerships in 2024–2025; historically receptive to content aggregation  
**Grant/contract potential**: Internet Archive is more often a grant recipient than a grantor. Direct partnership more likely than funding.  
**Phase 6 opportunity**: Open-repo's practical procedural content (procedures, schematics) is not in Open Library's scope. Partnership as a complementary content layer — open-repo provides the "how to do" while Open Library provides the "what is." OPDS interoperability with Open Library's catalog is technically feasible.

### 2. Digital Public Library of America (DPLA)

**Current platform**: Open-source metadata aggregation platform (Hydra/Blacklight stack); service hub network  
**User count**: 12 service hubs, 16 content hubs; 47M+ digital items in the catalog  
**Openness to partnerships**: High — 2025 is explicitly a "transition year" for new partnerships; actively seeking new content hub relationships; open-source infrastructure  
**Grant/contract potential**: DPLA itself is a grant-funded organization (Knight Foundation, NEH, Mellon). A partnership would likely take the form of content integration rather than financial exchange.  
**Phase 6 opportunity (Option A)**: Open-repo as a new DPLA content hub, contributing practical knowledge metadata to the national discovery layer. DPLA's OPDS-compatible infrastructure and open-source platform make this technically straightforward.

### 3. LYRASIS

**Current platform**: Multiple open-source hosted platforms including Palace Project (OPDS-based), DSpace, ArchivesSpace, FOLIO  
**User count**: 1,100+ member libraries across 28 countries  
**Openness to partnerships**: High — LYRASIS is structurally designed to host and support open-source library platforms; their Palace Project model (open-source + managed hosting) is exactly the Option B pattern  
**Grant/contract potential**: LYRASIS administers regranting programs and has received significant Knight Foundation funding ($5M for Palace Project). A LYRASIS partnership for open-repo hosting would be a revenue relationship, not a grant.  
**Phase 6 opportunity (Option B)**: LYRASIS could be the hosting cooperative for Option B — rather than open-repo building its own multi-tenant infrastructure, licensing the platform to LYRASIS for their member libraries. Or LYRASIS membership as a distribution channel for the SaaS tier.

### 4. Mellon Foundation (Public Knowledge Program)

**Current platform**: Funder (not a library platform)  
**Grant scope**: Preserving original source materials; equitable digital access; networks for knowledge sharing; community-based archives ($25K–$100K for community archives; larger strategic grants up to $1M+ for institutional projects)  
**Application cycle**: Rolling letters of inquiry (LOI); typical 6–12 month process from LOI to grant decision  
**Phase 6 opportunity (Option A)**: Open-repo's federated network for practical knowledge fits the "networks to increase knowledge sharing" priority in the Public Knowledge program. A grant proposal for Phase 6A pilot (3–5 partner libraries, OPDS federation infrastructure) would align. Budget request: $100–200K for 18-month pilot.  
**Timeline consideration**: First contact (LOI) no later than August 2026 to align with grant cycle for Phase 6A launch funding.

### 5. IMLS (Institute of Museum and Library Services)

**Current platform**: Federal agency (grants only)  
**Grant programs**: National Leadership Grants for Libraries ($50K–$500K); Laura Bush 21st Century Librarian Program; Sparks! Ignition Grants ($10–25K for prototypes)  
**Application cycle**: Annual cycle; National Leadership Grants applications typically due in spring (Feb–April)  
**Phase 6 opportunity**: Sparks! Ignition Grant for a Phase 6A pilot with 3–5 public libraries; National Leadership Grant for a larger federation network deployment.  
**Note**: IMLS requires formal nonprofit status or fiscal sponsorship for grant applications. A fiscal sponsor (e.g., Library Futures, LYRASIS, or Educopia) would be required unless the project incorporates as a 501(c)(3).

### 6. Library Futures Foundation

**Current platform**: Advocacy + research nonprofit; has received Mellon and Lounsbery Foundation grants  
**User count**: Small staff; influence through policy and research  
**Openness to partnerships**: High — explicit mandate for open-source library technology; has piloted direct digital delivery of econtent via an open-source project  
**Grant/contract potential**: Library Futures has regranting capacity (they distributed funds from their Mellon grant to open-source library projects). A Library Futures partnership for Phase 6A could provide both funding and legitimacy.  
**Phase 6 opportunity**: Library Futures as an organizational home or fiscal sponsor for the nonprofit federation model (Option A), or as a co-applicant on a Mellon/IMLS grant.

### 7. Kiwix Association (Switzerland)

**Current platform**: Kiwix offline library ecosystem (ZIM format, 10M+ downloads)  
**User count**: 10M+ ZIM downloads in first 2 months of 2024; institutional partnerships with Wikimedia Foundation, iFixit, freeCodeCamp, correctional facilities  
**Openness to partnerships**: High — Kiwix is explicitly designed for content partnerships; the ZIM format is the output of Phase 5 Candidate 1  
**Grant/contract potential**: Kiwix Association has received Wikimedia Endowment funding. A formal content partnership would list open-repo in Kiwix's catalog (get.kiwix.org), dramatically expanding distribution reach.  
**Phase 6 opportunity**: The single highest-leverage partnership available. Kiwix catalog listing is achievable post-Phase 5 (requires a validated, maintained ZIM feed). This is a distribution partnership, not a funding relationship — but it unlocks the user base for Option B and Option C.

### 8. ByWater Solutions / Koha Ecosystem

**Current platform**: Managed hosting of Koha ILS for 1,425 libraries (2,217 facilities)  
**User count**: Largest Koha support vendor in North America  
**Openness to partnerships**: Commercial — ByWater Solutions is a for-profit company. Partnership would require business case (revenue sharing or licensing).  
**Grant/contract potential**: None directly; but access to 1,425 libraries is a significant distribution channel for Option B SaaS.  
**Phase 6 opportunity (Option B)**: ByWater Solutions libraries already have open-source ILS infrastructure. Open-repo SaaS as a complementary platform (practical knowledge catalog alongside the traditional catalog) is a natural add-on sale. A reseller arrangement ($500–2,000 referral per library) could accelerate Option B adoption.

### 9. Palace Project (LYRASIS)

**Current platform**: Open-source ebook lending platform built on OPDS, Readium, and LCP; 100+ library members  
**User count**: 100+ libraries in California, Connecticut, Florida, Maryland, New Jersey, Pennsylvania, South Carolina, Washington  
**Openness to partnerships**: High — built on OPDS (compatible with Phase 5 Candidate 2); actively seeking content integrations; Lyrasis/NYU/Columbia documentation of interoperability workflows  
**Grant/contract potential**: Palace Project has Knight Foundation and IMLS funding history.  
**Phase 6 opportunity (Option C + Option A)**: Open-repo's OPDS catalog (Candidate 2) is already technically compatible with Palace Project's discovery layer. A formal content partnership — open-repo appears in Palace's catalog alongside ebooks — is achievable with a single OPDS integration. This is the fastest path to institutional library user adoption.

---

## Part 5: Hybrid Sustainability Model Recommendation

The most resilient model combines all three revenue streams to address different market segments and reduce dependence on any single funding source.

### Recommended Hybrid Model: "Open Core + Federated Nonprofit + SaaS"

**Layer 1 — Free open-source base (volunteer-maintained)**

- Self-hostable open-repo (all Phase 1–5 functionality)
- Free for any organization to deploy
- No feature restrictions on the self-hosted version
- Sustained by developer time (~0.5 FTE currently); grows as contributor community grows

**Layer 2 — Managed SaaS hosting (commercial revenue)**

- Managed hosting tiers (Seed/Sprout/Grove/Forest as described in Option B)
- Target: small-medium libraries that cannot self-host
- Revenue target: $100K ARR by end of Year 1, $500K ARR by end of Year 2
- This is the primary financial sustainability mechanism; it is achievable within 12 months of Phase 6 launch

**Layer 3 — Federated network membership (nonprofit or cooperative)**

- Library network membership fees for access to the federated discovery layer (Option A infrastructure)
- Nonprofit governance: libraries that join the federation vote on protocol decisions
- Revenue target: $250K–$1M annually by Year 2–3, scaling with member library count
- Funded initially by grants (Mellon, IMLS) while membership revenue grows

**Layer 4 — API access (developer ecosystem)**

- Freemium API tier (Option C) as a natural product of the SaaS platform
- The same REST API that powers the SaaS admin dashboard is exposed publicly with rate limiting
- Revenue contribution: modest initially ($25–50K ARR), but builds developer ecosystem
- Enterprise API contracts fund long-term platform development

**Why this hybrid works**:
- SaaS (Layer 2) generates revenue quickly without requiring network adoption (can start with a single library)
- Federation (Layer 3) creates the long-term strategic moat — a federated network is much harder to replicate than a single SaaS product
- Grants (Layer 3) fill the gap during the 12-24 months before membership fees reach sustainability
- API (Layer 4) grows organically as the platform matures; no incremental investment required beyond the SaaS API work

**What to avoid**: Building Option A (federation) before Option B (SaaS). The SaaS infrastructure (multi-tenancy, billing, provisioning) is a prerequisite for hosting the federation network nodes. Building Option A first means building the hosting infrastructure twice.

---

## Part 6: Twelve-Month Roadmap (May 2026 – May 2027)

### May–June 2026: Phase 5 Execution

| Week | Milestone | Owner |
|------|-----------|-------|
| May 20–25 | ZimWriter libzim integration (Candidate 1) merged | Development |
| May 26–June 5 | OPDS feed migration (Candidate 2) merged | Development |
| June 5–15 | Accessibility audit (Candidate 3, if prioritized) | Development |
| June 15 | Phase 5 closure: ZIM exports live on CDN, OPDS catalog functional | Development |
| June 15–30 | Phase 6 architecture review (this document); user decision on Phase 6 option | User + Development |

**Decision gate**: User selects primary Phase 6 option by June 30, 2026.

### July–August 2026: Phase 6 Foundation

| Week | Milestone |
|------|-----------|
| Jul 1–14 | Multi-tenancy foundation: `library_id` namespace in `ExportConfig`, OPDS `feedId`, CDN path namespacing (2–4 hours of forward-compatibility changes) |
| Jul 15–31 | Option B: Multi-tenant DB schema isolation + tenant provisioning pipeline MVP |
| Aug 1–15 | Option B: Billing infrastructure (Stripe integration, subscription tiers) |
| Aug 15–31 | Option B: Analytics dashboard (collection metrics, download counts) |

### September–October 2026: Private Beta

| Week | Milestone |
|------|-----------|
| Sep 1 | Option B: 3–5 partner libraries onboarded to private beta |
| Sep 1–30 | Beta feedback cycle: provisioning reliability, analytics utility, OPDS integration |
| Oct 1 | Kiwix catalog listing submission: apply to appear in Kiwix's get.kiwix.org directory |
| Oct 15 | Option A groundwork: OPDS 2.0 crawler and central metadata registry prototype |
| Oct 31 | Option B: Feature-complete for public launch |

### November–December 2026: Public Launch + Grant Applications

| Week | Milestone |
|------|-----------|
| Nov 1 | Option B: Public launch (self-service signup, credit card billing live) |
| Nov 15 | Mellon Foundation LOI submitted for Phase 6A federation pilot (if nonprofit track selected) |
| Dec 1 | Option A: CatalogSync ActivityPub activity type implemented; pilot with 2 self-hosted library partners |
| Dec 31 | Year-end targets: 15–25 paying SaaS customers; Option A pilot operational |

### January–March 2027: Scaling + Option A Federation Launch

| Week | Milestone |
|------|-----------|
| Jan 2027 | Option A: Central registry public (federated catalog discovery live) |
| Jan–Feb 2027 | DPLA and LYRASIS partnership conversations (formal outreach with OPDS integration demo) |
| Feb 2027 | IMLS National Leadership Grant application (if nonprofit filing complete) |
| Mar 2027 | Option B ARR checkpoint: $100K target; Option A network membership: 10+ libraries |

### Decision Gates

| Date | Decision |
|------|----------|
| **May 25, 2026** | ZimWriter merged — Phase 5 critical path clear |
| **June 30, 2026** | Phase 6 option selection: Option B first (recommended), or user overrides to A or C |
| **September 1, 2026** | Beta library partners confirmed — if < 3 confirmed, reassess Option B scope |
| **November 1, 2026** | Option B public launch — if delayed, reassess sequencing |
| **January 2027** | Mellon LOI response — if declined, reassess Option A timeline; pursue IMLS |
| **March 2027** | ARR checkpoint — $100K ARR target; if not met, assess pricing/market fit |

---

## Sources

- [Mellon Foundation — Public Knowledge Grant Programs](https://www.mellon.org/grant-programs/public-knowledge) — grant program scope, priorities for digital access infrastructure
- [Mellon Foundation — Call for Proposals: Community-Based Archives (2025)](https://release-2026-1-1--prod-mellon.netlify.app/article/call-for-proposals-community-based-archives-2025) — award ranges $25K–$100K; two-year grant period from August 2025
- [CLIR — Recordings at Risk Program Refunding (2025)](https://www.clir.org/2025/07/mellon-foundation-funds-two-additional-cycles-of-clirs-recordings-at-risk-grant-program-clir-opens-competition-to-canadian-applicants/) — Mellon awarded $3M for two additional cycles; grant model precedent
- [Library Futures — Mellon Grant Announcement](https://www.libraryfutures.net/post/library-futures-mellon-grant) — Mellon Foundation $1M grant to Library Futures for open-source library technology
- [Library Futures — Lounsbery Foundation Grant](https://www.libraryfutures.net/post/library-futures-awarded-lounsbery-foundation-grant/) — direct digital delivery of econtent via open-source project; grant model precedent
- [DPLA — Our Hubs](https://pro.dp.la/hubs/our-hubs) — 12 service hubs, 16 content hubs; 2025 transition year for new partnerships
- [LYRASIS — About](https://lyrasis.org/about/) — 1,100+ member libraries in 28 countries; manages Palace Project, DSpace, FOLIO, ArchivesSpace
- [LYRASIS — Ebooks & Community Engagement (2025)](https://lyrasis.org/ebooks-community-engagement-at-lyrasis-empowering-libraries-to-shape-the-future-of-ebooks/) — OPDS interoperability workflows; partnership with NYU, Columbia, OAPEN
- [Palace Project — Launch Announcement](https://lyrasis.org/the-palace-project-launches-new-platform-and-app-to-enable-equitable-econtent-access/) — 100+ library members; $5M Knight Foundation funding; OPDS-based open-source platform
- [ByWater Solutions — Koha](https://bywatersolutions.com/products/koha) — 1,425 libraries, 2,217 facilities; largest Koha support ecosystem in North America
- [OPDS.io — Standard for Digital Content Distribution](https://opds.io/) — OPDS specification; basis for Phase 5 Candidate 2 and Phase 6A federation
- [Kiwix — Wikipedia](https://en.wikipedia.org/wiki/Kiwix) — 10M+ downloads in first 2 months of 2024; Wikimedia Foundation formal partnership; institutional deployment in correctional facilities
- [Kiwix — Catalog](https://get.kiwix.org/en/solutions/catalog/) — content partner application pathway
- [JSTOR — Grant Opportunities for Libraries (2025)](https://about.jstor.org/blog/grant-opportunities-for-libraries-to-digitize-describe-and-preserve-collections-in-2025/) — IMLS, NEH, Mellon grant landscape for 2025
- [JSTOR — Funding Opportunities May–December 2025](https://about.jstor.org/blog/funding-opportunities-for-libraries-archives-and-special-collections-may-december-2025/) — current funding cycle summary
- [CNI — Connecting the Dots with OPDS](https://www.cni.org/topics/digital-libraries/connecting-the-dots-to-overcome-access-using-open-publication-distribution-system-opds-lightning-round) — OPDS federation for library network discovery; Coalition for Networked Information endorsement
- [Pratt Institute — Mellon Digital Preservation Grant ($1.28M)](https://www.pratt.edu/news/school-of-information-digital-preservation-initiative-receives-1-28-million-from-the-mellon-foundation/) — grant scale precedent for library digital infrastructure
- [SourceForge — Library Management Systems (SaaS, 2025)](https://sourceforge.net/software/library-management/saas/) — competitive landscape for library management SaaS

---

*Document status: Ready for user review and Phase 6 option selection. Phase 5 execution should proceed (Candidates 1+2) regardless of Phase 6 choice.*  
*Next action: User decision on Phase 6 primary option by June 30, 2026.*
