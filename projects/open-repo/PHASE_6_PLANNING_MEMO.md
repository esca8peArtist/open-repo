---
title: "Phase 6 Planning Memo — Managed Hosting + Federated Network"
project: open-repo
phase: 6
document_type: planning-memo
status: decision-ready
created: 2026-06-03
author: research-agent
confidence: high
tags: [phase-6, saas, federation, opds, multi-tenancy, kiwix, sustainability]
decision_deadline: "2026-06-30"
---

# Phase 6 Planning Memo
## Open-Repo: From Single Instance to Distributed Platform

**Status**: Decision-Ready  
**Audience**: Project owner  
**Decision needed by**: June 30, 2026  
**Estimated effort**: 80–120 hours (MVP); 200–280 hours (full Phase 6A + 6B)  
**Recommended start**: July 1, 2026 (immediately after June 12 deployment verification)

---

## The Phase 5 Exit State

Phase 5 delivered four capabilities that together define what open-repo is now and, by extension, what Phase 6 must build on top of:

1. **Offline-first distribution** — valid ZIM archives generated weekly, hosted on Cloudflare R2, discoverable via Kiwix in-app OPDS catalog
2. **Federation-ready architecture** — ActivityPub inbox/outbox from Phase 4, HTTP Signature signing, WebFinger identity, content-addressed CIDs
3. **WCAG 2.1 AA compliance** — zero P0 violations, one outstanding P1 (color contrast in third-party ReDoc component), deployment cleared for June 12
4. **Moderated contribution pipeline** — community submissions, editorial approval, auditable history from Phase 3

The platform is now architecturally sound, accessibility-compliant, and capable of offline distribution. It is not yet monetizable, not multi-tenant, and not discoverable beyond its immediate operator's network. Phase 6 changes all three.

---

## What Phases 1–5 Did Not Solve

Four functional gaps define the Phase 6 option space (documented in the pre-Phase-5 architecture analysis):

| Gap | Business consequence |
|-----|---------------------|
| Each open-repo instance is an island — users at one library cannot search another's catalog | Limits network-effect value; every new deployment starts from zero |
| No managed hosting option | Organizations without IT staff cannot adopt the platform; addressable market is capped at technical operators |
| No third-party integrations (OAuth API, webhooks) | Reading apps, e-readers, and catalog aggregators cannot consume open-repo content programmatically |
| No usage analytics | Operators cannot demonstrate collection impact; grant applications lack evidence |

These gaps are compounding: without managed hosting, the user base grows slowly; without a user base, the federated network has no nodes to connect; without a federated network, the value proposition is weaker than Internet Archive for every potential partner.

---

## The Recommendation: Option B First, Then Option A

Two design documents produced during Phase 5 — `ITEM15_PHASE6_FEDERATION_ROADMAP.md` and `PHASE_6_ARCHITECTURE_OPTIONS.md` — analyzed three Phase 6 paths (Federated Search Platform, Commercial SaaS Hosting, API Ecosystem) against effort, revenue timeline, and mission alignment. The finding is consistent: **build the SaaS hosting layer before the federated network**, because the SaaS infrastructure (multi-tenancy, billing, automated provisioning, analytics) is a strict prerequisite for hosting federation nodes affordably.

Building the federation first means building multi-tenancy twice. Building SaaS first creates the revenue stream that funds federation development.

Phase 6 should therefore proceed in two sub-phases:

**Phase 6A (July–October 2026): Managed SaaS Hosting MVP**  
**Phase 6B (October 2026–March 2027): Federated Network + Partner Onboarding**

The API ecosystem (Option C) is not a separate phase — it emerges naturally from the SaaS platform's admin API and requires no additional architectural investment beyond rate limiting and OAuth.

---

## Phase 6A: Managed SaaS Hosting MVP

### Scope

Multi-tenant deployment of open-repo with automated provisioning, subscription billing, usage analytics, and OPDS feed management. A library or community archive signs up on a web form, pays by credit card, and has a running open-repo instance within ten minutes.

The technical model is shared application / separate PostgreSQL schemas for the MVP (appropriate for 5–50 tenants), with a migration path to container-per-tenant when any tenant exceeds 10,000 items or when total tenant count crosses 50.

### Deliverables

| Deliverable | Effort estimate |
|-------------|----------------|
| Multi-tenant DB schema isolation (per-tenant `library_id`, namespaced CDN paths, configurable OPDS `feedId`) | 20 hours |
| Automated provisioning pipeline (web form → running instance in <10 minutes) | 25 hours |
| Stripe billing integration (subscription tiers: Seed/Sprout/Grove/Forest) | 20 hours |
| Analytics dashboard (collection size, download counts, most-accessed content) | 20 hours |
| Admin console and support tooling | 15 hours |
| Data portability: `GET /api/export/portable` for any tenant at any time | 5 hours |
| Documentation and deployment | 15 hours |

**Total Phase 6A: 120 hours**

### Pricing Tiers

| Tier | Catalog Size | Monthly Price | Annual Price | Target |
|------|-------------|---------------|--------------|--------|
| Seed | Up to 500 items | $49/month | $490/year | Individual researchers, small archives |
| Sprout | Up to 5,000 items | $199/month | $1,990/year | Small public libraries |
| Grove | Up to 25,000 items | $599/month | $5,990/year | Mid-size libraries, school districts |
| Forest | Unlimited | Custom | Custom | Large systems, universities |

### Revenue Projection

- Year 1 (conservative, 20 Seed + 10 Sprout + 3 Grove + 1 Forest at $5K): ~$8,400/month = **$100K ARR**
- Year 2 (growth, 100 Seed + 40 Sprout + 15 Grove + 5 Forest): ~$42,000/month = **$500K ARR**

The Year 1 target is achievable with five to eight paying customers in the library and community archive space, which is reachable through direct outreach to the Koha/ByWater Solutions ecosystem (1,425 libraries) and LYRASIS members.

### Success Criteria

- [ ] Three to five partner libraries onboarded to private beta by September 1, 2026
- [ ] Automated provisioning: new tenant live in under ten minutes, zero manual steps
- [ ] Data portability: any tenant can export their full dataset at any time
- [ ] Billing: Stripe integration live; at least one paying customer before public launch
- [ ] Phase 5 OPDS feed works per-tenant (each library has its own discoverable catalog)
- [ ] Public launch by November 1, 2026

### Dependencies

- Phase 5 deployment verified (June 12 target) — this is the upstream you build on
- The two low-effort forward-compatibility changes called out in the architecture analysis must be confirmed in the Phase 5 codebase before Phase 6A begins: `library_id` in `ExportConfig`, `feedId` in OPDS config, namespaced CDN paths, no hard-coded domain constants (estimated 2–4 hours, not included in Phase 6A estimate above)
- Stripe account and domain for SaaS subdomain routing (Cloudflare DNS)

---

## Phase 6B: Federated Network + Partner Onboarding

### Scope

Enable any open-repo instance — whether self-hosted or SaaS-provisioned — to join a shared discovery network. Users at one library can search across all federated libraries simultaneously. Catalog metadata propagates via OPDS 2.0 and ActivityPub `CatalogSync` activities; content stays on the originating node.

This is not the full multi-organization federation described in `ITEM15_PHASE6_FEDERATION_ROADMAP.md` (that is a 12–18 month effort including DID:WEB identity, compliance tiering, and governance formalization). Phase 6B delivers the minimum federation that creates visible value: cross-library search discovery.

### Deliverables

| Deliverable | Effort estimate |
|-------------|----------------|
| OPDS 2.0 crawler and central metadata registry (FastAPI + PostgreSQL + Meilisearch on a single VPS) | 40 hours |
| Cross-library search API (`GET /search?q=...&library=...`) | 25 hours |
| ActivityPub `CatalogSync` activity type (lightweight push notification to registry when items are created/updated) | 20 hours |
| Network dashboard (membership count, aggregate statistics, activity feed) | 20 hours |
| Data boundary: residency tagging on objects, inbound residency filter per node | 15 hours |
| Graduated migration tooling (shadow mode → read-only federation → full) | 10 hours |
| Documentation, testing, deployment | 30 hours |

**Total Phase 6B: 160 hours**

### Success Criteria

- [ ] Three to five pilot libraries federated and returning cross-library search results
- [ ] Activity propagation latency p95 under 120 seconds (target for 6B; tighten in 6C)
- [ ] Each federated node has a declared residency policy (prerequisite for EU participation)
- [ ] Kiwix catalog listing submitted (requires a validated ZIM feed from Phase 5 — submit by October 1, 2026)
- [ ] Pilot operational by January 2027

### Strategic Partnerships to Activate in Phase 6B

**Kiwix Association** — highest-leverage, lowest friction. Appearing in `get.kiwix.org` is achievable immediately post-Phase-5 (Phase 5 ZIM export is the only technical prerequisite). This exposes open-repo to Kiwix's 10M+ user base at zero cost. File the catalog listing application by October 1, 2026.

**LYRASIS / Palace Project** — the Palace Project is OPDS-native and has 100+ library members. Open-repo's Phase 5 OPDS feed is technically compatible today. A formal content partnership (open-repo appears in Palace's discovery layer) is achievable with a single OPDS integration point.

**Mellon Foundation LOI** — the Public Knowledge program funds "networks to increase knowledge sharing," which precisely describes Phase 6B. Submit a letter of inquiry by November 15, 2026 targeting a $100–200K pilot grant for the federated network's first 18 months. Grant funding fills the revenue gap during the 12–24 months before membership fees reach sustainability.

---

## Phase 6 is Expansion, Not Stabilization

The framing question in the task brief is worth answering directly: is Phase 6 about expansion, stabilization, performance/reliability, or distribution?

Phase 5's A11y work was stabilization. The platform is now stable and compliant. The P1 violation (ReDoc color contrast) is in a third-party component with limited remediation surface — it does not block deployment and should be tracked but not prioritized over Phase 6 work.

Phase 6 is unambiguously **expansion with a commercial sustainability purpose**. The platform has the right technical foundation. What it lacks is the operational layer (multi-tenancy, billing, provisioning) that lets it reach the libraries and archives that would most benefit from it, and the federation layer that makes the network worth joining.

The sequencing — SaaS before federation — is also a distribution strategy. Every library onboarded to SaaS is a node ready to participate in the federated network when Phase 6B launches. The SaaS beta is the federation network's pilot cohort.

---

## Timeline

| Period | Milestone |
|--------|-----------|
| June 12, 2026 | Phase 5 deployment verified; Phase 6 prerequisites confirmed |
| June 30, 2026 | User decision on Phase 6 option (this memo is the decision document) |
| July 1 – August 31, 2026 | Phase 6A: Multi-tenancy foundation + billing infrastructure |
| September 1, 2026 | Private beta: 3–5 partner libraries onboarded |
| October 1, 2026 | Kiwix catalog listing submitted |
| October 15, 2026 | Phase 6A feature-complete |
| November 1, 2026 | Phase 6A public launch (self-service signup, billing live) |
| November 15, 2026 | Mellon Foundation LOI submitted |
| December 1, 2026 | Phase 6B: CatalogSync ActivityPub activity type + pilot federation with 2 self-hosted partners |
| January 2027 | Phase 6B: Central registry public; DPLA and LYRASIS outreach with OPDS integration demo |
| March 2027 | Phase 6A ARR checkpoint ($100K target); Phase 6B network membership checkpoint (10+ libraries) |

---

## Risks and Mitigations

**Risk 1: Library sales cycles are slow (6–12 months)**  
The library sector evaluates software through committees. The first paying customer may take three to four months from initial contact. Mitigation: begin outreach immediately, targeting small community archives and individual researchers (Seed tier) who can buy with less process overhead. Do not wait for library procurement to validate the pricing model.

**Risk 2: Phase 5 codebase is not multi-tenancy-ready**  
The architecture analysis flagged four specific single-tenant assumptions in the Phase 5 codebase (hard-coded domain constants, unnested CDN paths, single `ExportConfig`, single OPDS feedId). If these were not addressed in Phase 5, they must be the first Phase 6A task. Effort is 2–4 hours. Verify before estimating Phase 6A scope.

**Risk 3: EU data residency creates federation friction**  
If an EU library wants to federate with a US-hosted node, GDPR transfer rules require either an adequacy decision or SCCs. The residency tagging system in Phase 6B (data boundary deliverable) addresses the protocol layer. An EU-facing Terms of Service and Data Processing Agreement template should be drafted before the first EU-resident SaaS customer is onboarded. This is a legal work item, not a development item.

**Risk 4: Kiwix catalog listing is not guaranteed**  
Kiwix has content standards. Open-repo ZIM files must pass zimcheck validation and meet Kiwix's metadata requirements. Phase 5's ZIM export pipeline is built to those requirements, but the listing application will need a maintained ZIM feed URL and a description of the content scope. The application should be prepared in August 2026 and filed October 1.

**Risk 5: Phase 6B federation undercut by single-tenant competitors**  
A single-tenant managed hosting offering (Phase 6A) is immediately replicable by any VPS host. The federation layer (Phase 6B) is the strategic moat — a federated network with 30+ nodes is much harder to replicate than a Docker container. The sequencing is correct, but the roadmap to Phase 6B should not slip more than two quarters.

---

## What This Memo Does Not Decide

The full governance formalization, DID:WEB researcher identity portability, Shamir key escrow, and economic sustainability mechanisms for the coordination layer (all documented in `ITEM15_PHASE6_FEDERATION_ROADMAP.md`) are Phase 6C work — appropriate when the network has 10+ active nodes and the governance overhead is warranted. Imposing governance process on a pre-critical-mass network creates process debt without benefit.

The API ecosystem (Option C from `PHASE_6_ARCHITECTURE_OPTIONS.md`) requires no separate decision. The REST API that powers the SaaS admin dashboard is the public API. Rate limiting and OAuth 2.0 are the only additions needed to productize it, and those are low-complexity additions to Phase 6A.

---

## Decision Required

By June 30, 2026, one decision:

**Proceed with Phase 6A (SaaS Hosting MVP) as primary Phase 6 path, with Phase 6B (Federated Network) as the 12-month follow-on.**

If the user instead wants to prioritize Phase 6B (federation) before Phase 6A (SaaS), that is the higher-mission, lower-revenue path. Both paths are documented. The recommendation in this memo and in both predecessor documents is Phase 6A first. Override that recommendation only if revenue is explicitly deprioritized in favor of nonprofit network-building from the outset, in which case a Mellon/IMLS grant application should be filed before development begins.

---

## Supporting Documents

- `/projects/open-repo/PHASE_6_ARCHITECTURE_OPTIONS.md` — Full option analysis (SaaS vs. federation vs. API ecosystem), revenue projections, library partnership landscape, 12-month roadmap
- `/projects/open-repo/ITEM15_PHASE6_FEDERATION_ROADMAP.md` — Detailed federation architecture: peer mesh topology, compliance tiering, economic model, governance evolution, risk register
- `/projects/open-repo/PHASE_5_ARCHITECTURE.md` — Phase 5 technical foundation this builds on
- `/projects/open-repo/a11y-audit-results/JUNE1_FINDINGS_REPORT.md` — Current WCAG compliance state (2 minor violations in third-party components; zero blockers)
