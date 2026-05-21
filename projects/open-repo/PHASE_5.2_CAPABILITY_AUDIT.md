---
title: "Phase 5.2 Capability Audit — Library and Tool Assessment per Candidate"
project: open-repo
phase: "5.2 planning"
status: "pre-merge planning (June 1+ implementation target)"
created: 2026-05-21
author: General Research Agent
depends_on: "PHASE_5.2_FEATURE_CANDIDATES.md"
---

# Phase 5.2 Capability Audit

**Purpose**: For each of the ten Phase 5.2 feature candidates, assess the Python library landscape, data source availability, offline capabilities, ZIM format compatibility (as understood from Phase 5.1), implementation risk, and person-hour estimates. This document is the technical due-diligence layer supporting the priority matrix.

**Phase 5.1 constraints that govern all assessments**:
1. ZIM articles are static HTML only — no JavaScript, no live API calls at read time
2. All CSS must be inline in `<style>` tags; no external stylesheets
3. Images must be base64-embedded or omitted in the nopic ZIM variant
4. Content must render correctly in Kiwix Android (WebView) and kiwix-serve (local HTTP)
5. Full-text search is Xapian-based, embedded in the ZIM — article titles and body text are indexed
6. Platform is Raspberry Pi 5 aarch64 — all Python wheels must have aarch64 manylinux builds

---

## Candidate 1: Botanical Knowledge Archiver

### Python Libraries

| Library | Version | Purpose | aarch64 wheel | Maintenance | License |
|---|---|---|---|---|---|
| `biopython` | 1.87 (March 2026) | Sequence file parsing (FASTA/GenBank) for genetic archival | Yes — manylinux2014_aarch64 | Active (monthly releases) | Biopython License (BSD-like) |
| `openfoodfacts` | 3.x | Nutritional supplementation data | Yes — pure Python | Active | MIT |

**Assessment**: BioPython is the only non-trivial dependency and it is **optional** — the core botanical module (species cards, growing guides, seed saving) works entirely from Markdown/CSV sources without it. BioPython is warranted only if genetic sequence archival (FASTA files from GRIN or NCBI) is in scope for Phase 5.2; this can be deferred to Phase 5.3. The `openfoodfacts` library is optional supplementary data; not on the critical path.

**Key finding**: USDA PLANTS Database provides complete species metadata in CSV format (public domain, ~44,000 species). OpenFarm was shut down in April 2025 but its GitHub repository and data (CC BY 4.0) remain available for download and local deployment. Both sources are offline-capable without any live API calls.

### Data Sources

| Source | Format | Offline capable | License | Size |
|---|---|---|---|---|
| USDA PLANTS Database | CSV download | Yes — full dump available | Public domain | ~15 MB CSV |
| OpenFarm GitHub archive | Ruby/PostgreSQL dump | Yes — self-host or parse CSV export | CC BY 4.0 | ~50 MB data |
| seedwarden project Markdown | .md files (internal) | Yes — local filesystem | Internal project | ~100–200 KB |
| GRIN (USDA Germplasm Resources) | CSV download | Yes | Public domain | ~200 MB full |

**Offline capability**: Full. No live API calls required. USDA and GRIN data can be downloaded once and bundled into the import pipeline.

### ZIM Format Compatibility

- Species cards render cleanly as structured HTML articles
- Botanical illustrations: if sourced from Wikimedia Commons (CC licensed), can be base64-embedded in the "all" ZIM variant; omitted in nopic
- Cross-linking between species articles (lookalikes, companion plants): standard `<a href="/items/{slug}">` links — supported natively in ZIM
- Taxon hierarchy (Family > Genus > Species): renders as breadcrumb HTML or as category index articles — both compatible

**Risk**: None for ZIM compatibility. Botanical content is text-and-table-heavy, well-suited to ZIM's static HTML model.

### Implementation Risk: LOW

**Rationale**: Source data is well-structured (USDA CSV, internal Markdown). ZIM rendering is straightforward. No computation at read time. BioPython is optional.

### Estimated Person-Hours: 12–16 hours

| Task | Hours |
|---|---|
| USDA CSV parser and species card model | 3–4 |
| OpenFarm data importer | 2–3 |
| seedwarden Markdown importer | 2 |
| ZIM article template (botanical) | 2 |
| Unit tests (30 cases) | 2–3 |
| Documentation | 1 |
| **Total** | **12–16** |

---

## Candidate 2: Offline Medical Reference Module

### Python Libraries

No new Python library dependencies required. The medical content pipeline is purely Markdown-to-HTML. RxNorm drug data (NLM) is available as SQL dump for local ingestion — no `requests` or live API calls needed.

| Library | Purpose | Required | Note |
|---|---|---|---|
| None beyond existing stack | — | — | Markdown parsing via standard library or existing project tooling |

**Assessment**: This is the cleanest candidate from a dependency perspective. The implementation complexity is almost entirely in content structuring and the disclaimer/liability framework — not in library integration.

### Data Sources

| Source | Format | Offline capable | License | Key content |
|---|---|---|---|---|
| off-grid-living/08-medical-health.md | Markdown | Yes | Internal project | ~1,500 lines primary source |
| WHO Model Formulary | PDF/HTML | Yes — downloadable | CC BY-NC-SA | Drug dosing, essential medicines |
| ICRC First Aid Guidelines | PDF | Yes — downloadable | Free for humanitarian use | Trauma/field medicine |
| Wilderness Medical Society protocols | PDF (open access papers) | Yes — downloadable | CC BY | Altitude, environmental, backcountry |
| RxNorm drug database | SQL dump (~3 GB) | Yes — local PostgreSQL | Public domain (NLM) | Drug names, interactions, NDC codes |
| CDC Emergency Preparedness guides | HTML/PDF | Yes | Public domain | Household planning, pandemic |

**Offline capability**: Full. All sources are downloadable for local use. RxNorm is large (3 GB SQL dump) but the relevant subset (essential medicines, ~2,000 drugs) is extractable as a ~10 MB CSV.

### ZIM Format Compatibility

- Drug monograph articles: structured HTML with a consistent template (name, class, indication, dosing table, contraindications, warnings) — ideal ZIM article format
- Quick-reference card format (printable single-page equivalent): CSS-based print media queries are ignored by Kiwix WebView, but a "compact view" CSS class can achieve the same effect in-app
- Drug interaction tables: static HTML lookup tables — fully compatible; no dynamic lookup possible offline, so interaction data must be pre-rendered per drug pair
- Evacuation criteria: formatted as visual alert boxes with high-contrast border CSS — fully compatible

**Key constraint**: Drug interaction lookup is inherently a cross-reference problem (O(n²) pairs). For a 200-drug formulary, pre-rendering all pairs is ~40,000 entries. Practical approach: include a "known interactions" section per drug article listing only clinically significant interactions (the WHO formulary already structures this), rather than a full cross-reference matrix.

**Risk**: Liability/disclaimer framework is the primary non-technical challenge. Every article must carry a prominent notice that this information is for prepared individuals in austere conditions, not a replacement for professional medical care. This is a content policy decision, not a code challenge.

### Implementation Risk: LOW-MEDIUM

**Rationale**: Low technical risk (no new dependencies, straightforward content pipeline). Medium policy risk: medical accuracy review is mandatory before any publication. The user's off-grid-living 08-medical-health.md already reflects this philosophy ("not a replacement for training, but a knowledge foundation") — this framing must be preserved and amplified in the ZIM articles.

### Estimated Person-Hours: 10–14 hours

| Task | Hours |
|---|---|
| Medical content type schema and importer | 3–4 |
| Disclaimer/liability template system | 2 |
| ZIM article template (medical) | 2 |
| RxNorm essential medicines subset extraction | 1–2 |
| Unit tests (25 cases) | 2 |
| Documentation | 1 |
| **Total** | **10–14** |

---

## Candidate 3: Water Systems Knowledge Module

### Python Libraries

No new dependencies required. Sizing calculations are arithmetic (gallons/day × household members), implementable without scientific libraries.

| Library | Purpose | Required | Note |
|---|---|---|---|
| None required | — | — | All sizing tables are pre-computed static HTML |

### Data Sources

| Source | Format | Offline capable | License | Key content |
|---|---|---|---|---|
| off-grid-living/03-water.md | Markdown | Yes | Internal | Primary source |
| systems-resilience/individual/01-water.md | Markdown | Yes | Internal | Already authored |
| WHO Drinking Water Quality Guidelines | PDF | Yes | CC BY-NC-SA | Testing standards, contamination thresholds |
| CDC WASH guidelines | HTML/PDF | Yes | Public domain | Emergency water treatment |
| USDA Natural Resources Conservation Service well/irrigation guides | PDF | Yes | Public domain | Hydrology, well yield testing |

**Offline capability**: Full.

### ZIM Format Compatibility

Schematics (pump diagrams, well cross-sections) present the main compatibility challenge. ZIM supports SVG as embedded content within HTML articles. Hand pump diagrams exist as public-domain SVG from Practica Foundation and WHO. These can be embedded directly. ASCII art is the fallback for nopic variant.

**Risk**: SVG schematic quality depends on available public-domain source files. If high-quality SVGs are not available, ASCII art representations reduce usability significantly.

### Implementation Risk: LOW

### Estimated Person-Hours: 8–12 hours

| Task | Hours |
|---|---|
| Content importer (Markdown sources) | 2 |
| WaterSizingCalculator (pre-computed tables) | 2–3 |
| SVG schematic sourcing and embedding | 2–3 |
| ZIM article template | 1 |
| Unit tests (20 cases) | 1–2 |
| **Total** | **8–12** |

---

## Candidate 4: Energy Systems Sizing Module

### Python Libraries

| Library | Version | Purpose | aarch64 wheel | Maintenance | License |
|---|---|---|---|---|---|
| `pvlib` | 0.11.x | Solar irradiance modeling, PV system simulation | Yes — pure Python + scipy | Active (quarterly releases, Sandia/NREL backed) | BSD 3-Clause |
| `numpy` | 1.24+ | Array operations for pvlib | Yes — pre-built manylinux | Active | BSD 3-Clause |
| `pandas` | 2.x | Time-series data handling for irradiance | Yes — manylinux aarch64 | Active | BSD 3-Clause |

**Assessment**: pvlib is a production-grade library with US government (Sandia National Laboratories) backing. It has aarch64 wheels. However, it introduces `numpy` and `pandas` as runtime dependencies, which adds ~200 MB to the build environment. These are not new to the platform conceptually, but should be verified as not already present in the open-repo backend environment.

**Critical design decision**: pvlib must be used at **build time only**, pre-computing sizing tables for embedded US climate zones (Zone 3–7). The ZIM articles must be static HTML — pvlib cannot run inside Kiwix. The build process generates lookup tables (e.g., "4 kW array in Zone 5, south-facing, 30° tilt: estimated 5,200 kWh/year") that are embedded as HTML tables in the articles.

### Data Sources

| Source | Format | Offline capable | License | Key content |
|---|---|---|---|---|
| NREL National Solar Radiation Database (NSRDB) | CSV/HDF5 download | Yes — download subset | Public domain | Irradiance by US location |
| NREL System Advisor Model typical-year data | CSV | Yes | Public domain | 60+ US climate locations |
| off-grid-living/06-energy-power.md | Markdown | Yes | Internal | Primary source content |

**Offline capability**: Full after one-time data download at build time. pvlib's `get_clearsky()` and location-based models work without internet access once data files are local.

### ZIM Format Compatibility

Pre-computed HTML tables are fully compatible. Interactive calculators (e.g., sliders for array size) are impossible in ZIM (no JavaScript). The design must present pre-computed tables for common configurations — this is adequate for planning purposes.

### Implementation Risk: MEDIUM

**Rationale**: pvlib is a real dependency with significant API surface. The pre-computation architecture is the right design but requires careful implementation to avoid building brittle lookup table generation code. pandas/numpy dependency adds build complexity. Recommend implementing this last in Phase 5.2.

### Estimated Person-Hours: 16–22 hours

| Task | Hours |
|---|---|
| pvlib environment setup and dependency verification | 2–3 |
| EnergyCalculator pre-computation script | 5–7 |
| NSRDB data download and preprocessing | 2–3 |
| ZIM article template with embedded tables | 2 |
| Unit tests (validate pre-computed vs. pvlib live) | 3 |
| Documentation | 1–2 |
| **Total** | **16–22** |

---

## Candidate 5: Food Preservation Safety Module

### Python Libraries

No new dependencies required. USDA canning data is available as structured JSON (extractable from the USDA Complete Guide to Home Canning PDF).

| Library | Purpose | Required | Note |
|---|---|---|---|
| `openfoodfacts` | Nutritional data supplementation | Optional | Pure Python, no binary deps |

### Data Sources

| Source | Format | Offline capable | License | Key content |
|---|---|---|---|---|
| USDA Complete Guide to Home Canning | PDF (public domain) | Yes — parse to JSON | Public domain | Authoritative processing times |
| National Center for Home Food Preservation | HTML (downloadable) | Yes | Public domain | Fermentation, dehydration tables |
| seedwarden/harvest-preservation-field-manual.md | Markdown | Yes | Internal | Regional/seasonal preservation |
| off-grid-living/05-food-preservation.md | Markdown | Yes | Internal | Primary source |

**Offline capability**: Full. All USDA data is public domain and downloadable as PDFs that can be parsed to structured JSON during the build pipeline.

**Safety note**: Processing time tables must be verified against the current USDA edition (2015 edition is latest as of 2026) and must NOT be modified or interpolated. Altitude adjustments must be included as a separate lookup table.

### ZIM Format Compatibility

Processing time lookup tables are the core content type — static HTML tables render perfectly in Kiwix. Fermentation recipe articles follow the same pattern as existing food-type articles. Botulism risk identification boxes use the same high-contrast CSS alert pattern as medical evacuation criteria.

### Implementation Risk: LOW

Safety-critical data accuracy is the key concern, not technical complexity.

### Estimated Person-Hours: 8–12 hours

| Task | Hours |
|---|---|
| USDA canning data parser (PDF-to-JSON extraction, one-time) | 3–4 |
| Content importer (Markdown sources) | 2 |
| ZIM article template with lookup tables | 2 |
| Unit tests (15 cases, verify table completeness) | 1–2 |
| **Total** | **8–12** |

---

## Candidate 6: Communications in Austere Conditions Module

### Python Libraries

| Library | Purpose | Required | Note |
|---|---|---|---|
| `meshtastic` | Generate Meshtastic device config examples | Optional | Pure Python, generates config JSON |

**Assessment**: The `meshtastic` Python SDK is optional. Its value is generating structured device configuration examples programmatically (so they stay current with firmware changes). However, static documentation of Meshtastic configuration is equally valid for a ZIM archive — the configuration syntax changes infrequently enough that static articles are maintainable.

### Data Sources

| Source | Format | Offline capable | License | Key content |
|---|---|---|---|---|
| off-grid-living/11-communications.md | Markdown | Yes | Internal | 1,650-line primary source |
| FCC frequency allocation tables | PDF | Yes | Public domain | Band plan, power limits |
| ARRL Technician license question pool | PDF | Yes | Public domain (released 4-year cycle) | License exam prep content |
| Meshtastic documentation | HTML (GitHub) | Yes — mirrored | Apache 2.0 | Device setup guides |
| AREDN mesh networking docs | HTML | Yes — downloadable | GPL | Community mesh setup |

**Offline capability**: Full. FCC data and ARRL question pool are public domain downloadables.

### ZIM Format Compatibility

Frequency allocation tables as HTML — ideal. Quick-reference decision matrix (already present in off-grid-living source as Markdown table) — renders directly. Meshtastic device setup is step-by-step HTML — straightforward.

### Implementation Risk: LOW

### Estimated Person-Hours: 8–10 hours

| Task | Hours |
|---|---|
| Content importer | 2 |
| Frequency table structuring | 2 |
| Meshtastic/AREDN config articles | 2 |
| ZIM article template | 1 |
| Unit tests (15 cases) | 1–2 |
| **Total** | **8–10** |

---

## Candidate 7: Sanitation and Waste Management Module

### Python Libraries

No new dependencies required.

### Data Sources

| Source | Format | Offline capable | License | Key content |
|---|---|---|---|---|
| off-grid-living/09-waste-sanitation.md | Markdown | Yes | Internal | Primary source |
| WHO Sanitation Safety Planning manual | PDF | Yes | CC BY-NC-SA | Pathogen kill data, system sizing |
| EPA biosolids guidance | HTML/PDF | Yes | Public domain | Land application, composting specs |

**Offline capability**: Full.

### ZIM Format Compatibility

Carbon:nitrogen ratio tables, temperature monitoring requirements, and tank sizing calculations are all static HTML-compatible. Biogas yield calculations (cubic meters per kg dry matter) can be pre-computed as embedded tables.

### Implementation Risk: LOW

### Estimated Person-Hours: 6–8 hours

---

## Candidate 8: Security and Defense Protocols Module

### Python Libraries

No new dependencies required.

### Data Sources

| Source | Format | Offline capable | License | Key content |
|---|---|---|---|---|
| off-grid-living/12-security-defense.md | Markdown | Yes | Internal | 1,252-line primary source |

**Offline capability**: Full — internal source only.

### ZIM Format Compatibility

Threat matrix tables, perimeter design checklists, and quarterly audit checklists are all static HTML-compatible.

### Implementation Risk: LOW (technical), MEDIUM (content policy)

**Content policy note**: Security/defense content requires careful scope boundaries to ensure the archive remains focused on defensive infrastructure hardening rather than tactical offense. The off-grid-living source already maintains this boundary (focuses on site design, livestock protection, access control, OPSEC). The ZIM articles must replicate this boundary explicitly.

### Estimated Person-Hours: 6–8 hours

---

## Candidate 9: Biological Seed Preservation Module

### Python Libraries

| Library | Version | Purpose | aarch64 wheel | Required |
|---|---|---|---|---|
| `biopython` | 1.87 | FASTA/GenBank sequence file parsing | Yes — manylinux2014_aarch64 | Optional (defer to Phase 5.3) |

**Assessment**: BioPython is the right library if genetic sequence archival (documenting the DNA of heritage varieties) is in scope. For Phase 5.2, the core value is in procedural content (viability testing, storage specifications, germination calendars) — all of which work without BioPython. Recommend deferring BioPython integration to Phase 5.3 when the scope for genetic data archival can be defined precisely.

### Data Sources

| Source | Format | Offline capable | License | Key content |
|---|---|---|---|---|
| seedwarden project Markdown files | .md files | Yes | Internal | Primary source — already authored |
| GRIN (USDA Germplasm Resources) | CSV download | Yes | Public domain | 600,000+ accessions, viability data |
| Seed Savers Exchange variety database | HTML (scrape) | Partial — no bulk download | Copyright (informational use) | Heritage variety profiles |
| USDA Seed Storage Guidelines | PDF | Yes | Public domain | Temperature/humidity specs |

**Offline capability**: Full for GRIN and internal sources. Seed Savers Exchange does not provide bulk data download; use GRIN as primary authoritative source for viability data.

### ZIM Format Compatibility

Species cards with viability tables are ideal ZIM article format. Germination calendar (visual planting timeline by species) can be rendered as an HTML grid table — Kiwix renders these correctly. Cross-links between related species articles are native ZIM links.

### Implementation Risk: LOW-MEDIUM

BioPython being optional reduces risk. GRIN data parsing is the main engineering task — the CSV format is well-documented.

### Estimated Person-Hours: 12–16 hours

| Task | Hours |
|---|---|
| GRIN CSV parser and species model | 3–4 |
| seedwarden Markdown importer | 2 |
| Viability calculator (pre-computed tables) | 2 |
| ZIM article template (seed/species card) | 2 |
| Unit tests (20 cases) | 2 |
| Documentation | 1 |
| **Total** | **12–16** |

---

## Candidate 10: Community Governance and Conflict Resolution Module

### Python Libraries

No new dependencies required. Decision tree rendering can be accomplished with existing Python standard library (HTML generation from YAML-format decision trees).

### Data Sources

| Source | Format | Offline capable | License | Key content |
|---|---|---|---|---|
| systems-resilience phase-5 wave-2 docs | Markdown | Yes | Internal | Community implementation playbooks |
| off-grid-living/13-community-organization.md | Markdown | Yes | Internal | 1,700-line primary source |
| systems-resilience/phase-5-wave-2-conflict-resolution-framework.md | Markdown | Yes | Internal | Conflict resolution ladder |
| systems-resilience/phase-5-wave-2-psychological-support-guide.md | Markdown | Yes | Internal | Mental health protocols |

**Offline capability**: Full — all internal sources.

### ZIM Format Compatibility

Governance model comparison tables, skill inventory templates, and decision trees are all well-suited to static HTML. Decision trees rendered as nested HTML lists or CSS-styled flowcharts — both render in Kiwix without JavaScript.

### Implementation Risk: LOW

### Estimated Person-Hours: 8–10 hours

---

## Consolidated Risk and Effort Summary

| Candidate | Risk Level | Person-Hours | New Dependencies | Data Readiness |
|---|---|---|---|---|
| 1 — Botanical Knowledge | Low | 12–16 | biopython (optional) | High — USDA CSV + internal docs |
| 2 — Medical Reference | Low-Medium | 10–14 | None | High — internal docs + WHO PDFs |
| 3 — Water Systems | Low | 8–12 | None | High — internal docs + public domain |
| 4 — Energy Systems | Medium | 16–22 | pvlib, numpy, pandas | Medium — NSRDB download required |
| 5 — Food Preservation | Low | 8–12 | None | High — USDA PDF + internal docs |
| 6 — Communications | Low | 8–10 | meshtastic (optional) | High — internal + FCC public domain |
| 7 — Sanitation | Low | 6–8 | None | High — internal + WHO PDFs |
| 8 — Security Protocols | Low (tech) / Medium (policy) | 6–8 | None | High — internal docs |
| 9 — Seed Preservation | Low-Medium | 12–16 | biopython (optional) | High — GRIN + internal docs |
| 10 — Community Governance | Low | 8–10 | None | High — internal docs |

**Total estimated Phase 5.2 effort** (top 6 candidates, Wave 1–2): **58–84 person-hours**

**Recommended June 2026 scope (top 5 candidates)**: 48–72 person-hours — achievable within a 30-day implementation window at ~2–3 hours/day.

---

## ZIM Format Compatibility Summary

All ten candidates produce content that is compatible with the Phase 5.1 ZIM pipeline. Key observations:

1. **Static HTML is sufficient** for all candidate content types. No JavaScript is needed for any of the survival knowledge domains.
2. **Lookup tables** (drug dosing, canning times, solar sizing, seed viability) are the dominant content structure — these render well in both Kiwix Android WebView and kiwix-serve.
3. **SVG schematics** (water pumps, shelter construction) require public-domain SVG sourcing. This is the only format risk across all candidates.
4. **Cross-linking** between articles (species lookalikes, drug interactions, companion plants) uses standard ZIM internal links — fully supported.
5. **Safety-critical data** (medical dosing, canning times) must never be dynamically generated or interpolated — static tables from authoritative sources only.

---

## Sources

- [BioPython 1.87 release notes — biopython.org](https://biopython.org/)
- [pvlib-python documentation — pvlib-python.readthedocs.io](https://pvlib-python.readthedocs.io/)
- [Meshtastic Python SDK — meshtastic.org](https://meshtastic.org/)
- [OpenFarm shutdown and archive — GitHub openfarmcc](https://github.com/openfarmcc/OpenFarm)
- [Open Food Facts Python SDK — PyPI](https://pypi.org/project/openfoodfacts/)
- [RxNorm (NLM drug database) — NLM](https://www.nlm.nih.gov/research/umls/rxnorm/)
- [NREL pvlib iotools paper — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0038092X23007260)
- [WHO Model Formulary — WHO](https://www.who.int/publications/i/item/9789241547659)
- [USDA PLANTS Database](https://plants.usda.gov/)
- [GRIN Germplasm Resources — USDA](https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/nutrient-data-laboratory/)
- [ZIM format multi-domain support — openZIM GitHub](https://github.com/openzim)
- [libzim Python bindings — PyPI](https://pypi.org/project/libzim/)
