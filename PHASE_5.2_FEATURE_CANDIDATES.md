---
title: "Phase 5.2 Feature Candidates — Top 10 Evaluation"
project: open-repo
phase: "5.2 planning"
status: "pre-merge planning (June 1+ implementation target)"
created: 2026-05-21
author: General Research Agent
depends_on: "Phase 5.1 MVP merge (feature/zimwriter-libzim-activation)"
---

# Phase 5.2 Feature Candidates

**Context**: Phase 5.1 MVP (ZimWriter libzim integration) is in CONDITIONAL APPROVE state — zero merge blockers, four post-merge action items. This document assumes Phase 5.1 merges in late May 2026 and that Phase 5.2 implementation begins June 1. Phase 5.2 expands coverage to new "subset-of-humanity" domains not yet in open-repo's ZIM pipeline.

**What Phase 5.1 established (constraints that carry forward)**:
- ZIM export pipeline via `libzim>=3.10.0` with Xapian full-text search
- Content model: HTML articles rendered from structured JSON-LD content items via Jinja2
- Domain taxonomy: `agriculture`, `water`, `food`, `electronics`, `building`, `energy`
- Offline constraint: all ZIM content must be self-contained (no external CSS/JS/image URLs)
- Platform: Raspberry Pi 5 (aarch64, Python 3.11.2, 4–8 GB RAM, thermal ceiling ~87°C)
- Distribution: Cloudflare R2 CDN, OPDS catalog, Kiwix readers (Android/Desktop/kiwix-serve)

---

## The Coverage Gap

The Phase 5.1 domain taxonomy covers high-level categories but omits significant life-critical knowledge domains that the user's active projects explicitly address. Cross-referencing the open-repo domains against the systems-resilience PLAN.md and off-grid-living master outline reveals these gaps:

| systems-resilience / off-grid-living domain | open-repo ZIM coverage | Gap severity |
|---|---|---|
| Biological preservation (seeds, genetics) | Absent | High — seedwarden project has no ZIM representation |
| Offline medical reference (drug interactions, dosing) | Absent | High — off-grid-living 08-medical-health.md has no downstream archive |
| Water systems (well drilling, testing, filtration) | Partial (general "water" domain) | Medium — lacks structured procedural depth |
| Energy systems (solar/wind sizing, battery management) | Partial (general "energy" domain) | Medium — pvlib-class calculations not yet archived |
| Food preservation (canning, fermentation, root cellaring) | Partial (general "food" domain) | Medium — process safety data absent |
| Communications in austere conditions | Absent | High — off-grid-living 11-communications.md has no ZIM |
| Waste and sanitation | Absent | Medium — off-grid-living 09-waste-sanitation.md |
| Security and defense protocols | Absent | Medium — off-grid-living 12-security-defense.md |
| Botanical identification (wild edibles, medicinals) | Absent | High — seedwarden medicinal herbs work unarchived |
| Community governance and conflict resolution | Absent | Low-medium — systems-resilience phase-5 wave-2 docs |

---

## Candidate 1: Botanical Knowledge Archiver

**Feature name**: `BotanicalArchiver` — structured ZIM module for plant identification, medicinal herb profiles, seed saving, and wild edibles

**Description**: Ingests structured plant data from multiple sources (OpenFarm archive, USDA PLANTS database, seedwarden project documents) and renders it as ZIM articles with species cards: common name, Latin binomial, growing zone, edibility/toxicity classification, harvest calendar, seed saving instructions, medicinal properties with evidence level, and lookalike hazard warnings. Each article links to related species.

**Coverage gap**: Botanical knowledge spans three critical domains: food security (wild foraging supplements caloric supply during infrastructure failure), medicine (herbalism is the accessible alternative when pharmaceuticals are unavailable), and ecological restoration (native plant propagation for long-term land recovery). None of these are in the current ZIM taxonomy.

**Alignment with related projects**:
- **seedwarden**: Direct — medicinal-herbs-candidate-list.md, native-plants-regional-guide (listed in systems-resilience source integration), endangered-species-candidate-list.md all need offline archival
- **systems-resilience**: midwest/foraging-species.md explicitly called out as dependent on seedwarden pull
- **off-grid-living**: skills chapter (16) lists herbal medicine as a Tier 4 skill

**Estimated scope**:
- New module: `app/services/importers/botanical_importer.py` (~300–400 lines)
- New content schema: `botanical_item` type with species-specific fields (~100 lines)
- ZIM article template: `templates/botanical_article.html` (~80 lines)
- Tests: ~30 new unit tests
- Total: ~500–600 lines of new code

**Dependencies**:
- `biopython>=1.87` — for parsing FASTA/GenBank sequence files if genetic data is included; optional
- OpenFarm GitHub archive (CC BY 4.0, code/data available since April 2025 shutdown)
- USDA PLANTS Database downloadable CSV (public domain, ~44,000 species)
- seedwarden project Markdown files (internal, already written)

**Complexity**: Low-medium. Data parsing and template work; no new backend infrastructure required.

---

## Candidate 2: Offline Medical Reference Module

**Feature name**: `MedicalReferenceArchiver` — drug dosing, procedure guides, and first-aid protocols rendered as offline-safe ZIM articles

**Description**: Curates and structures the content from off-grid-living's 08-medical-health.md plus authoritative open-access references (WHO Essential Medicines List, ICRC First Aid guides, Wilderness Medical Society protocols) into discrete ZIM articles: one per condition, one per procedure, one per drug class. Each article includes: indication, contraindications, adult dosing, pediatric dosing (weight-based), supply quantities for 1-year household stock, and when to evacuate.

**Coverage gap**: The single highest-value domain in austere-environment survival knowledge. The off-grid-living project has ~1,500+ lines of medical content that has no offline ZIM representation. Users without internet who need this content most — disaster zones, remote homesteads, low-bandwidth regions — cannot access it.

**Alignment with related projects**:
- **systems-resilience**: individual/05-healthcare.md depends on off-grid-living 08-medical-health.md as source
- **off-grid-living**: 08-medical-health.md is the primary source document
- **open-repo mission**: "documentation archives for topics critical to human survival" — medicine is unambiguous

**Estimated scope**:
- New content type: `medical_article` with structured fields (indication, dosing, contraindications, evacuation criteria)
- Importer: `app/services/importers/medical_importer.py` (~250 lines)
- Template: `templates/medical_article.html` (~100 lines, careful layout for quick-reference card format)
- Disclaimer system: legal/liability boilerplate must be consistent and prominent (~30 lines)
- Tests: ~25 new unit tests
- Total: ~450 lines of new code

**Dependencies**:
- No new Python library dependencies; content is Markdown-sourced from project files
- WHO Essential Medicines List (public domain PDF/CSV — freely downloadable)
- Wilderness Medical Society guidelines (open access publications)
- RxNorm drug database (NLM, free to download for offline use)

**Complexity**: Low-medium. High sensitivity: requires rigorous disclaimer/liability framework in article template. Medical accuracy review is mandatory before publication.

---

## Candidate 3: Water Systems Knowledge Module

**Feature name**: `WaterSystemsArchiver` — well drilling, filtration, water testing, and household sizing procedures

**Description**: Extends the existing "water" domain with structured procedural content: hand pump construction schematics (Simple Pump, PVC pitcher pump), well drilling methods (jetting, cable tool, hand auger), water quality testing protocols (coliform, turbidity, nitrates), filtration system selection guides (ceramic, gravity, UV, chlorination), and per-household sizing calculations (gallons/day by activity).

**Coverage gap**: The systems-resilience PLAN.md lists "Hand pump construction schematics" and "Well drilling — hand methods" as explicit research gaps requiring new content. The current open-repo "water" domain exists at taxonomy level only; no structured procedural content has been imported.

**Alignment with related projects**:
- **systems-resilience**: individual/01-water.md is Priority 1 execution item; sources/schematics.md needs pump/well content
- **off-grid-living**: 03-water.md is the source for the cross-reference; needs ZIM representation
- **open-repo**: "water" domain already in taxonomy — this fills it with real content

**Estimated scope**:
- Content: importer for Markdown-sourced procedural content (~200 lines)
- Sizing calculator: `WaterSizingCalculator` static utility (~150 lines, generates sizing HTML table in article)
- Template: extends base article template with calculation output tables
- Tests: ~20 new unit tests
- Total: ~400 lines of new code

**Dependencies**:
- No new Python library dependencies
- WHO Water Quality Guidelines (public domain)
- CDC water treatment guidance (public domain)
- USDA rural water/well guides (public domain)

**Complexity**: Low. Content-heavy, code-light. Main challenge is schematic representation — ZIM is HTML-only, so schematics must be SVG-embedded or ASCII art.

---

## Candidate 4: Energy Systems Sizing Module

**Feature name**: `EnergySystemsArchiver` — solar/wind/hydro sizing calculators, battery storage guides, and load estimation tools

**Description**: Wraps `pvlib-python` calculations into offline-accessible articles: solar array sizing by location (using embedded irradiance lookup tables for US climate zones rather than live API calls), battery bank sizing (lead-acid vs. lithium chemistry comparison, depth-of-discharge calculations), load estimation worksheets, and generator fuel consumption tables. Each article is static HTML with embedded calculation results pre-computed for common household configurations.

**Coverage gap**: The off-grid-living 06-energy-power.md chapter is complete at ~1,500+ lines but has no offline ZIM representation. Pre-computed sizing tables for US climate zones (Zone 3 through Zone 7) would serve as offline decision support for rural homesteaders planning solar/battery systems without internet access.

**Alignment with related projects**:
- **systems-resilience**: individual/04-energy.md ("solo power needs; suburban grid-tied backup") is listed as Priority 7
- **off-grid-living**: 06-energy-power.md is the primary source; needs archival
- **open-repo**: "energy" domain in taxonomy — currently empty

**Estimated scope**:
- `EnergyCalculator` class: pre-computes sizing tables using pvlib at build time, embeds results in HTML (~300 lines)
- Importer/template: ~150 lines
- Pre-computation script: runs during ZIM build, not at runtime (~100 lines)
- Tests: ~20 unit tests (test pre-computed values match pvlib output)
- Total: ~550 lines of new code

**Dependencies**:
- `pvlib>=0.11.0` — solar modeling (PyPI, actively maintained, Python 3.11 compatible)
- `numpy>=1.24` — already likely in environment
- US climate zone irradiance dataset: NREL's National Solar Radiation Database (downloadable CSV, public domain)

**Complexity**: Medium. pvlib is a real dependency with significant scope; the pre-computation approach limits runtime complexity. Requires careful design to keep ZIM articles static while still being useful for varied configurations.

---

## Candidate 5: Food Preservation Safety Module

**Feature name**: `FoodPreservationArchiver` — canning safety tables, fermentation protocols, drying/dehydrating guides, root cellaring specifications

**Description**: Structures food preservation safety data into ZIM articles: USDA-tested canning processing times by food type and jar size, fermentation starter ratios and temperature ranges, dehydrator temperature/time tables, root cellar construction specifications (temperature/humidity requirements by crop), and pressure canning altitude adjustments. Critically includes botulism risk identification and failure mode recognition.

**Coverage gap**: Food preservation safety is time-sensitive and error-prone. Without accurate processing times, home canning causes botulism. The off-grid-living 05-food-preservation.md exists but has no offline ZIM archival. The USDA Complete Guide to Home Canning is public domain and authoritative.

**Alignment with related projects**:
- **systems-resilience**: individual/02-food.md includes root cellar and fermentation content
- **off-grid-living**: 05-food-preservation.md is the source document
- **seedwarden**: harvest-preservation-field-manual.md is already written and needs archival

**Estimated scope**:
- Importer: ~200 lines
- Safety data parser: USDA canning tables as structured JSON embedded in articles (~150 lines)
- Template: must render lookup tables clearly for quick reference in austere conditions (~80 lines)
- Tests: ~15 unit tests (validate processing time table completeness and accuracy)
- Total: ~450 lines of new code

**Dependencies**:
- No new Python library dependencies
- USDA Complete Guide to Home Canning (public domain, structured data available as JSON)
- National Center for Home Food Preservation datasets (public domain)
- Open Food Facts Python SDK (`openfoodfacts>=3.0`) for nutritional supplementation data — optional

**Complexity**: Low. Data-entry-heavy. Main challenge is ensuring safety data accuracy (processing times must not be interpolated or modified from USDA source).

---

## Candidate 6: Communications in Austere Conditions Module

**Feature name**: `AustereCommunicationsArchiver` — ham radio licensing reference, mesh networking setup guides, GMRS/MURS protocols, Meshtastic configuration

**Description**: Structures the off-grid-living 11-communications.md content into discrete ZIM articles: radio frequency allocation tables (FRS/GMRS/MURS/ham), ham radio license quick-reference (Technician class question pool excerpts), Meshtastic device configuration guides, AREDN mesh networking setup, Winlink digital email procedures, EMP hardening specifications (Faraday cage construction), and a decision matrix for selecting comms technology by scenario.

**Coverage gap**: The communications domain has zero ZIM representation despite off-grid-living's 1,650-line chapter covering the full stack. This is a life-safety domain during infrastructure failure: knowing whether to evacuate, knowing the status of family members in another location, and coordinating community response all depend on working communications systems.

**Alignment with related projects**:
- **systems-resilience**: cross-references 11-communications.md; no existing systems-resilience communications document yet
- **off-grid-living**: 11-communications.md is primary source
- **cybersecurity-hardening**: EMP/Faraday hardening overlaps with the broader infrastructure hardening work

**Estimated scope**:
- Importer: ~200 lines
- Frequency tables: embedded as static HTML tables (no computation needed) (~100 lines)
- Meshtastic config articles: structured from meshtastic.org documentation (CC licensed)
- Template: quick-reference card format for field use (~80 lines)
- Tests: ~15 unit tests
- Total: ~400 lines of new code

**Dependencies**:
- `meshtastic` Python SDK (`meshtastic>=2.3`) — for generating device config examples programmatically; optional, can be static content instead
- FCC frequency allocation tables (public domain)
- ARRL Technician license pool (public domain, question pool released every 4 years)

**Complexity**: Low. Content-heavy, code-light. Meshtastic Python SDK optional — static content works without it.

---

## Candidate 7: Sanitation and Waste Management Module

**Feature name**: `SanitationArchiver` — composting toilet design, greywater systems, humanure composting, biogas digester specifications

**Description**: Structures off-grid-living's 09-waste-sanitation.md into ZIM articles covering: composting toilet design (continuous vs. batch composters, carbon:nitrogen ratios, temperature management), greywater system design (garden irrigation, subsurface drip vs. mulch basins), humanure composting protocols (CDC/WHO pathogen kill temperatures and times), and small-scale biogas digester construction for methane production from organic waste.

**Coverage gap**: Sanitation failure in a grid-down scenario kills faster than almost any other infrastructure failure (cholera, typhoid, dysentery are historically the leading causes of death in disaster zones). The off-grid-living chapter exists but has no ZIM representation.

**Alignment with related projects**:
- **systems-resilience**: community-scale sanitation is implicit in community/01-water.md and community/05-healthcare.md
- **off-grid-living**: 09-waste-sanitation.md is primary source

**Estimated scope**:
- Importer: ~150 lines
- Calculation utilities: nitrogen loading calculations, tank sizing (~100 lines)
- Template: ~60 lines
- Tests: ~12 unit tests
- Total: ~320 lines of new code

**Dependencies**:
- No new Python library dependencies
- WHO Sanitation Safety Planning guidelines (public domain)
- EPA biosolids land application guidelines (public domain)

**Complexity**: Low. Primarily a content structuring and templating exercise.

---

## Candidate 8: Security and Defense Protocols Module

**Feature name**: `SecurityProtocolsArchiver` — threat assessment, site hardening, community defense protocols, OPSEC guides

**Description**: Structures the off-grid-living 12-security-defense.md into ZIM articles: threat matrix by region and scenario type, perimeter design specifications (fencing, natural barriers, lighting), lockdown protocols, community sentinel systems, OPSEC for grid-down scenarios, and livestock protection guides. Explicitly excludes tactical doctrine (too specialized) — focuses on practical infrastructure hardening.

**Coverage gap**: Security domain has zero ZIM representation. In grid-down scenarios, property security becomes a critical concern within weeks.

**Alignment with related projects**:
- **systems-resilience**: individual/03-shelter.md references hardening; no dedicated security document
- **off-grid-living**: 12-security-defense.md (~1,252 lines) is primary source
- **cybersecurity-hardening**: digital/physical security crossover (OPSEC, communication security)

**Estimated scope**:
- Importer: ~150 lines
- Template: ~60 lines
- Tests: ~12 unit tests
- Total: ~250 lines of new code

**Dependencies**: None beyond existing stack.

**Complexity**: Low. Content structuring only.

---

## Candidate 9: Biological Seed Preservation Module

**Feature name**: `SeedPreservationArchiver` — genetic archival protocols, seed viability testing, cold/dry storage specifications, heritage variety identification

**Description**: Structures seedwarden project documents into ZIM articles: seed saving field manual procedures, viability testing methods (germination rate calculations, water float test, accelerated aging tests), cold/dry storage specifications by species (temperature, humidity, container type, expected viability years), heritage variety identification (morphological keys), and regional growing calendars.

**Coverage gap**: Biological preservation is the seedwarden project's core purpose, but none of its content has a ZIM representation for offline distribution. Seed saving knowledge is irreplaceable: if heritage varieties are lost, they cannot be recreated.

**Alignment with related projects**:
- **seedwarden**: Direct — seed-saving-field-manual.md, survival-garden-regional-plans.md, small-scale-livestock-field-manual.md are primary sources
- **systems-resilience**: midwest/calendar.md links to seedwarden for zone-specific planting
- **off-grid-living**: 04-food-production.md references seed saving

**Estimated scope**:
- Importer: ~200 lines
- Viability calculator: generates expected lifespan tables per species (~100 lines)
- Template: species card format (~80 lines)
- Tests: ~20 unit tests
- Optional BioPython integration for sequence data: adds ~100 lines if genetic archival is in scope
- Total: ~400–500 lines of new code

**Dependencies**:
- `biopython>=1.87` — optional, for FASTA/GenBank sequence parsing if genetic sequences are to be archived
- GRIN (USDA Germplasm Resources Information Network) public species database
- seedwarden project documents (internal sources, already written)

**Complexity**: Low-medium. BioPython is optional; the core module works without it.

---

## Candidate 10: Community Governance and Conflict Resolution Module

**Feature name**: `CommunityGovernanceArchiver` — governance model templates, mutual aid frameworks, skill inventory systems, emergency decision protocols

**Description**: Structures the systems-resilience phase-5 wave-2 documents (community-implementation-playbook, conflict-resolution-framework, psychological-support-guide) and off-grid-living 13-community-organization.md into ZIM articles: governance model comparison (consensus vs. council vs. sociocracy), mutual aid setup checklists, skill inventory templates, conflict resolution escalation ladders, emergency decision trees by scenario type (CBRN, wildfire, grid-down), and mental health protocols for community crisis.

**Coverage gap**: Community governance is the multiplier domain — it determines whether all other survival knowledge is actually deployed effectively. Without working governance, a community with food, water, and medical knowledge still fails. Currently absent from ZIM taxonomy.

**Alignment with related projects**:
- **systems-resilience**: Phase 5 Wave 2 community implementation content is directly archivable
- **off-grid-living**: 13-community-organization.md (~1,700 lines) is primary source

**Estimated scope**:
- Importer: ~150 lines
- Decision tree renderer: converts YAML-format decision trees to HTML flowcharts (~100 lines)
- Template: ~70 lines
- Tests: ~12 unit tests
- Total: ~330 lines of new code

**Dependencies**: None beyond existing stack.

**Complexity**: Low. The decision tree renderer is the only non-trivial engineering task.

---

## Priority Ranking

Ranked by composite score of: impact (domain criticality + breadth), effort (implementation hours), and alignment (fit with user's active projects). Full scoring in PHASE_5.2_PRIORITY_MATRIX.md.

| Rank | Candidate | Key rationale |
|---|---|---|
| 1 | Candidate 2 — Medical Reference | Highest life-safety value; source content already exists; no new dependencies |
| 2 | Candidate 1 — Botanical Knowledge | Serves three projects simultaneously (seedwarden, systems-resilience, off-grid-living); lowest-complexity for highest cross-domain value |
| 3 | Candidate 9 — Seed Preservation | Seedwarden direct archival; irreversibility of knowledge loss makes this high priority |
| 4 | Candidate 3 — Water Systems | Priority 1 in systems-resilience execution queue; source content already exists |
| 5 | Candidate 5 — Food Preservation | Safety-critical (botulism prevention); USDA data is structured and public domain |
| 6 | Candidate 6 — Communications | High life-safety value; off-grid-living source document is complete |
| 7 | Candidate 4 — Energy Systems | pvlib dependency adds moderate complexity; real user value for homestead planning |
| 8 | Candidate 7 — Sanitation | High public health value; somewhat lower engagement (less "interesting" content) |
| 9 | Candidate 10 — Community Governance | Lower urgency than survival-critical domains; good June extension candidate |
| 10 | Candidate 8 — Security Protocols | Valuable but sensitive; requires careful scope boundary to avoid misuse |

---

## Implementation Sequence for June 2026

**Wave 1 (June 1–10)**: Candidates 2, 1, 9 — all three use existing internal source documents, require no new Python library dependencies (BioPython optional), and directly archive the user's most active project content (seedwarden + systems-resilience medical/botanical).

**Wave 2 (June 11–20)**: Candidates 3, 5 — water systems and food preservation both draw from public-domain data sources already identified; implementation is content-structuring work.

**Wave 3 (June 21–30)**: Candidates 6, 4 — communications and energy systems. Candidate 4 requires pvlib integration (the only new compute dependency in Phase 5.2); plan this as the last item to avoid blocking earlier waves.

---

## Sources

- [BioPython 1.87 Release — PyPI](https://pypi.org/project/biopython/)
- [pvlib-python documentation](https://pvlib-python.readthedocs.io/)
- [Meshtastic off-grid communications](https://meshtastic.org/)
- [OpenFarm GitHub archive (CC BY 4.0)](https://github.com/openfarmcc/OpenFarm)
- [Open Food Facts Python SDK](https://github.com/openfoodfacts/openfoodfacts-python)
- [USDA PLANTS Database](https://plants.usda.gov/)
- [WHO Essential Medicines List](https://www.who.int/groups/expert-committee-on-selection-and-use-of-essential-medicines/essential-medicines-lists)
- [openZIM GitHub — libzim](https://github.com/openzim)
- [MeshCore lightweight LoRa mesh library](https://hamradio.my/2025/03/introducing-meshcore-a-lightweight-lora-mesh-networking-library/)
- [EFF — LoRa & Mesh regulatory update 2025](https://www.eff.org/deeplinks/2025/07/radio-hobbyists-rejoice-good-news-lora-mesh)
