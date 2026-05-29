---
title: "Phase 5.2 Water Purification Standards — Content Sourcing & Platform Validation Checklist"
project: open-repo
phase: "5.2"
module: "Water Systems (Priority 2)"
composite_score: 7.90
implementation_start: "June 10, 2026"
status: "pre-implementation validation — complete before June 10"
created: 2026-05-27
depends_on: "PHASE_5.2_MEDICAL_WATER_SEED_ROADMAP.md"
---

# Phase 5.2 Water Purification Standards — Content Sourcing & Platform Validation Checklist

**Purpose**: June 10 morning startup guide for the Water Systems module. This checklist enables a developer to arrive on June 10 and immediately begin implementation without any additional sourcing research.

**Gate**: Medical module first-draft milestone (June 12) is the soft gate for Water ZIM integration work; however, Water sourcing and schema work can and should begin in parallel on June 10.

---

## Tier Classification

**Tier 1 — Required**: Core treatment method documentation covering the 6-8 technology categories. All public domain or open-access.
**Tier 2 — Recommended**: Regional variation and specialized technique sources. Higher extraction effort.
**Tier 3 — Nice-to-have**: Proprietary product documentation and ISO standards (commercial licensing required).

---

## Tier 1: Required Sources

### T1-A: WHO Guidelines for Drinking-Water Quality, 4th Edition (2022 addenda)

- **URL**: https://www.who.int/publications/i/item/9789240045064
- **License**: CC BY-NC-SA 3.0 IGO — offline redistribution permitted for non-commercial use with attribution
- **Format**: PDF (also available via NCBI Bookshelf at https://www.ncbi.nlm.nih.gov/books/NBK579461/ as structured HTML)
- **What to extract**: Quality parameters (contaminant limits, turbidity thresholds, microbiological criteria), treatment effectiveness by method, guideline values for 100+ contaminants
- **Rate limits**: No API; direct PDF download or NCBI Bookshelf HTML crawl
- **June 10 action**: Download PDF to `data/sources/water/who_drinking_water_guidelines_2022.pdf`. The NCBI Bookshelf HTML version is preferable for structured extraction — mirror the relevant chapters using `requests` and parse with `html.parser`.
- **Priority chapters**: Chapter 7 (Water Treatment), Chapter 9 (Household Water Treatment), Chapter 10 (Rainwater Harvesting). These three chapters contain the treatment protocol content needed for the ZIM.

### T1-B: CDC Safe Water for the World / Household Water Treatment

- **URL**: https://www.cdc.gov/healthywater/drinking/index.html and https://www.cdc.gov/healthywater/global/household-water-treatment/
- **License**: Public domain (US government)
- **Format**: HTML pages
- **What to extract**: Treatment methods with exact quantities — chlorination rates (sodium hypochlorite concentration + dose per volume), boiling time by elevation (critical: boiling point drops ~1°C per 300m altitude; boiling time must increase), solar disinfection (SODIS) procedure, ceramic filtration instructions
- **Rate limits**: No API; HTML download; no throttle concerns
- **June 10 action**: Mirror relevant CDC pages to `data/sources/water/cdc_water/`. Key pages: chlorination, boiling, filtering, solar disinfection, emergency water storage.
- **Elevation note**: CDC documents boiling time at sea level as 1 minute, and recommends 3 minutes above 6,500 feet (2,000m). This altitude-adjusted data must be encoded in the water procedure articles, not averaged out.

### T1-C: EPA Drinking Water Regulations (SDWA Standards)

- **URL**: https://www.epa.gov/ground-water-and-drinking-water/national-primary-drinking-water-regulations
- **License**: Public domain (US government)
- **Format**: HTML tables; also available as downloadable data at https://www.epa.gov/DWdata
- **What to extract**: National Primary Drinking Water Regulations (NPDWR) — maximum contaminant levels (MCLs) for 90+ regulated contaminants; treatment technique requirements; Maximum Contaminant Level Goals (MCLGs)
- **Rate limits**: No API required; static HTML and downloadable CSVs
- **June 10 action**: Download the NPDWR contaminant table as CSV (available via the EPA DWdata site). Save to `data/sources/water/epa_mclg_table.csv`. This data populates the "water quality standards" reference section of the ZIM.
- **Scope note**: EPA SDWA standards are US-specific. Flag them as such in every article. WHO guidelines are the global reference; EPA standards are the US-specific tier.

### T1-D: Internal Source — off-grid-living/03-water.md

- **URL**: `projects/off-grid-living/03-water.md` (internal)
- **License**: Internal; no restrictions
- **Format**: Markdown
- **What to extract**: Household sizing calculations, filtration system selection criteria, storage recommendations, gravity-fed system designs, rainwater catchment sizing
- **June 10 action**: Copy to `data/sources/water/off_grid_water.md`.

### T1-E: Internal Source — systems-resilience/individual/01-water.md

- **URL**: `projects/systems-resilience/individual/01-water.md` (internal)
- **License**: Internal; no restrictions
- **Format**: Markdown
- **What to extract**: Priority procedures, community-scale guidance, hand pump references, well construction schematic references, emergency protocols
- **June 10 action**: Copy to `data/sources/water/systems_resilience_water.md`. Cross-reference with off_grid_water.md to identify content gaps flagged in the systems-resilience PLAN.md.

### T1-F: USDA Rural Development Water/Well Guides

- **URL**: https://www.rd.usda.gov/ — search "rural water well guide" or https://www.nrcs.usda.gov/wps/portal/nrcs/detail/national/water/
- **License**: Public domain (US government)
- **Format**: PDF guides
- **What to extract**: Well drilling methods (hand/cable tool/rotary), pump selection criteria (hand pump vs. submersible by depth), yield estimation, basic well casing requirements
- **June 10 action**: Download relevant USDA RD and NRCS well guides to `data/sources/water/usda_well_guides/`.

### T1-G: SODIS Reference Center (Eawag)

- **URL**: https://www.sodis.ch/methode/anwendung/index_EN (or http://www.sodis.ch/methode/forschung/index_EN)
- **License**: Open access; Eawag (Swiss Federal Institute of Aquatic Science) publishes SODIS documentation for free redistribution
- **Format**: PDF manuals and HTML guidance
- **What to extract**: Solar disinfection procedure (SODIS), bottle selection criteria, exposure time by turbidity and UV index, effectiveness data
- **June 10 action**: Download SODIS manual to `data/sources/water/sodis_manual.pdf`. This is the authoritative source for solar disinfection content.

---

## Tier 2: Recommended Sources

### T2-A: WHO Household Water Treatment and Safe Storage Network

- **URL**: https://www.who.int/teams/environment-climate-change-and-health/water-sanitation-and-health/tools-and-toolkits/household-water-treatment-and-safe-storage
- **License**: CC BY-NC-SA 3.0 IGO
- **Format**: PDF toolkits and guidance documents
- **What to extract**: Field-validated technique guides for low-income settings; ceramic pot filter instructions; chlorine tablet dosing for varying turbidity levels
- **Note**: This source covers techniques appropriate for the open-repo user base better than engineering-focused sources.

### T2-B: UNICEF/WHO Joint Monitoring Programme Water Data

- **URL**: https://washdata.org/ (WASH data portal)
- **License**: Open data with attribution (CC BY)
- **Format**: Downloadable datasets (CSV/Excel)
- **What to extract**: Regional water access data — useful for contextualizing which treatment methods are most relevant by geographic region
- **Note**: Useful for "Regional Variation" section of Water module — quantifies where different treatment needs are concentrated.

### T2-C: University Course Materials — Water Treatment Engineering

- **Primary target**: MIT OpenCourseWare https://ocw.mit.edu (search "water treatment" — courses 1.84J, CEE 44J)
- **License**: CC BY-NC-SA (MIT OCW standard license)
- **Format**: PDFs, lecture notes
- **What to extract**: Treatment process comparisons (advantages/disadvantages tables), chemical dosing calculations, filtration sizing formulas
- **Note**: Academic content is more rigorous than CDC/WHO procedural guides and fills the engineering rationale gap. Useful for the `system_selection` article type.

### T2-D: Regional Variation Sources

**India RO standards**:
- **URL**: https://bis.gov.in/index.php/standards/bis-catalogues/ (Bureau of Indian Standards IS 10500:2012 drinking water standard)
- **License**: BIS standards are available for purchase (~500 INR); summary data is available in academic papers (PubMed/ResearchGate, CC license variants)
- **Action**: Use academic summary sources rather than purchasing BIS directly. Search PubMed for "IS 10500 India drinking water standards review" — multiple open-access review articles exist.

**African boiling best practices**:
- **URL**: WHO/UNICEF WASH documentation covers Sub-Saharan Africa specifically; SODIS documentation covers field use in high-altitude Africa (Ethiopia, Rwanda)
- **Action**: Extract from T1-A (WHO HWTS) and T1-G (SODIS) which both include African field validation data.

**Arctic/subarctic snowmelt**:
- **URL**: CDC ATSDR guides for remote Alaska populations; Canadian Indigenous health documentation
- **Action**: Flag as a content gap if internal sources do not cover this scenario. Snowmelt treatment has distinct considerations (low organics, potential heavy metal contamination from atmospheric deposition). Add a brief "Regional note: Snowmelt" section to the boiling procedure article.

---

## Tier 3: Nice-to-Have (Commercial Licensing or Low ROI)

### T3-A: ISO 3696 (Lab Water) and ISO Water Treatment Standards

- **Status**: BLOCKED — ISO standards are commercially licensed (~CHF 60-120 per standard); redistribution of standard text is prohibited
- **Scope note**: ISO 3696 covers laboratory analytical water — not field drinking water treatment. Low relevance to open-repo use case.
- **Alternative**: EPA MCLGs and WHO Guidelines cover all relevant drinking water quality benchmarks without ISO licensing constraints.

### T3-B: NSF/ANSI Product Certification Data

- **Status**: DEFERRED — NSF certifies commercial products (filters, membranes, treatment chemicals); their standards documents are available but product-specific performance data requires manufacturer submission. Not relevant for the content module which covers techniques, not product endorsements.

### T3-C: Simple Pump / Commercial Hand Pump Documentation

- **Status**: REFERENCE ONLY — proprietary documentation; cite and describe, do not reproduce verbatim
- **Action**: Describe hand pump construction principles from general engineering sources (USDA T1-F) rather than from proprietary product documentation.

---

## Per-Technology Content Roadmap

| Technology | Primary Sources | Source Confidence | Content Type | Regional Applicability |
|---|---|---|---|---|
| Boiling | CDC (T1-B), WHO (T1-A) | HIGH — two authoritative sources with concordant guidance | Procedure article | Global; altitude adjustment required |
| Chlorination | CDC (T1-B), WHO (T1-A), SODIS center | HIGH | Procedure article with chemical quantity table | Global; concentration varies by source turbidity |
| Ceramic/biosand filtration | WHO HWTS (T2-A), SODIS center | HIGH for field use | Procedure article + DIY construction guide | Developing regions; effective for microbiological contamination |
| UV treatment (SODIS / UV lamp) | SODIS center (T1-G), WHO (T1-A) | HIGH for SODIS; MEDIUM for electric UV (power dependency) | Procedure articles (one per UV method) | Tropical/high-UV regions; power-dependent UV deferred |
| Reverse osmosis | Engineering academic (T2-C), EPA (T1-C) | MEDIUM — RO requires power and maintenance; limited off-grid relevance | System selection article (when to use RO vs. alternatives) | Power-available contexts; high-TDS groundwater |
| Well construction | USDA guides (T1-F), internal (T1-E) | MEDIUM — schematic content requires SVG conversion | Procedure article + 3 SVG schematics | Rural/off-grid; requires drilling expertise |
| Rainwater harvesting | off-grid-living (T1-D), WHO (T1-A) | HIGH for sizing; MEDIUM for contamination scenarios | Sizing guide + catchment contamination article | Most applicable where surface/groundwater limited |
| DIY filtration (improvised) | CDC (T1-B), WMS crossover from medical | MEDIUM — techniques are validated but informal | Procedure article with equipment list | Emergency/survival scenarios; primary fallback |

---

## Licensing Landscape Summary

| Source | License | Offline Redistribution | Commercial | Key Restriction |
|---|---|---|---|---|
| WHO Guidelines | CC BY-NC-SA 3.0 IGO | Yes (non-commercial) | No | Attribution required; share-alike |
| CDC materials | Public domain | Yes | Yes | None |
| EPA SDWA/NPDWR data | Public domain | Yes | Yes | US-specific; label as such |
| USDA guides | Public domain | Yes | Yes | None |
| SODIS (Eawag) | Open access | Yes | Educational | Attribution required |
| UNICEF/WHO WASH | CC BY | Yes | Yes | Attribution required |
| MIT OCW | CC BY-NC-SA | Yes (non-commercial) | No | Share-alike |
| ISO standards | Commercial | No | Requires purchase | Do not include |
| NSF/ANSI | Commercial | No | Requires purchase | Do not include |

---

## Water Content Risk Assessment

### Risk Level: MEDIUM

Incorrect water treatment guidance can cause waterborne illness (cholera, typhoid, giardia, cryptosporidium). Risk is moderate rather than high because:
1. Most errors in water treatment (undertreating, wrong contact time) result in illness rather than death, unlike medication dosing errors
2. Multiple cross-checking sources are available (WHO, CDC, EPA all document the same treatment methods)
3. Conservative safety margins can be built into procedures (e.g., recommending 1 minute boiling at sea level even though 30 seconds is sufficient for most pathogens)

**Mitigation**:
- All chemical quantities (chlorine doses, contact times, turbidity limits) cross-checked against at least two authoritative sources before publication
- Procedures include explicit "when to retreat" criteria (re-treat if turbidity remains high after filtration)
- Regional notes included where method effectiveness varies significantly (altitude, temperature, turbidity)
- No improvised treatment method is included without a source that validates its effectiveness for microbiological (not just chemical) contamination

### Attribution Requirements

Water treatment engineering attribution is standard peer-citation. An engineering credential is not required for each article, but each article must cite the governing standard or guideline (WHO, EPA, or peer-reviewed publication). The "source_citation" field is non-nullable.

### Update Cadence

Water treatment standards are among the most stable technical standards. Review cadence:
- WHO Drinking Water Guidelines: Updated approximately every 5-7 years; current 2022 edition is current through ~2027
- EPA SDWA/NPDWR: Updated on an as-needed basis; MCLs rarely change; check the EPA regulations update feed annually
- CDC guidance: Ad hoc; check annually
- SODIS method: Stable since 2002 systematic review; no change expected

**Assessment**: Annual review is sufficient for water treatment content. No monthly update cadence needed.

---

## SVG Schematic Plan (3 Required)

The systems-resilience source documents reference schematics that are not available as open-licensed SVGs. These must be created from scratch before June 15 integration testing:

1. **Hand pump cross-section** — pitcher pump (valves, cylinder, piston rod, handle); reference: USDA well pump guides
2. **Pitcher pump assembly** — exploded view showing valve ball positions; reference: historical public domain pump patent diagrams
3. **Well casing diagram** — shallow dug well with casing, grout seal, pump seat; reference: USDA rural water guide

**SVG creation tools**: Inkscape (open source). Create as inline `<svg>` elements with viewBox set for scalability. Estimated 2-3 hours total for all three schematics. **Start schematics on June 10 in parallel with data download** — this is the critical path item for the Water module.

---

## June 10 Morning Startup Sequence

1. Confirm Medical module branch is active (`feature/phase-5.2-medical`) — Water branch is independent
2. Create branch: `git checkout -b feature/phase-5.2-water`
3. Create directory: `mkdir -p data/sources/water/`
4. Begin parallel downloads: WHO PDF (T1-A), CDC mirror (T1-B), EPA CSV download (T1-C)
5. Copy internal sources: off-grid-living/03-water.md, systems-resilience/individual/01-water.md
6. Download SODIS manual from Eawag (T1-G)
7. Download USDA well guides (T1-F)
8. Start Inkscape SVG work for hand pump cross-section — do not defer this; it is the longest-lead creative task
9. Confirm EPA MCL CSV is downloaded and parseable
10. Begin content schema design for `water_procedure`, `sizing_guide`, `system_selection` article types
