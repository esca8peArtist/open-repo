---
title: "Phase 5.2 Medical / Water / Seed — Implementation Roadmap"
project: open-repo
phase: "5.2"
document_type: implementation-roadmap
status: pre-implementation (pending Phase 5.1 production stability)
created: 2026-05-27
target_start: "June 1, 2026"
target_completion: "July 5, 2026"
candidates:
  - "Medical Reference (Score 8.20, Candidate 2)"
  - "Water Systems (Score 7.90, Candidate 3)"
  - "Seed Preservation (Score 7.80, Candidate 9)"
priority_source: "PHASE_5.2_PRIORITY_MATRIX.md"
---

# Phase 5.2 Implementation Roadmap: Medical, Water, Seed

**Purpose**: Timeline-format implementation plan for the three highest-priority Phase 5.2 candidates (Medical Reference, Water Systems, Seed Preservation). Covers data sourcing, content structure, ZIM integration, resource estimates, and specific June 1–15 tasks for each.

**Prerequisites**:
- Phase 5.1 production-stable (48-hour zero-error monitoring window complete, per deployment checklist).
- Post-merge action items resolved: XSS fix applied, `ZimExport` ORM class created, `libzim>=3.10.0` in `pyproject.toml`.
- Feature branch workflow: each module gets its own branch (`feature/phase-5.2-medical`, `feature/phase-5.2-water`, `feature/phase-5.2-seed`).

**What Phase 5.1 established (constraints carried forward)**:
- ZIM export via `libzim>=3.10.0` with Xapian full-text search.
- Content model: HTML articles rendered from structured JSON-LD content items via Jinja2 templates.
- Offline constraint: all ZIM content must be self-contained — no external CSS/JS/image URLs, no `http://` in `src` or `href` attributes.
- Platform: Raspberry Pi 5, aarch64, Python 3.11.2, 4–8 GB RAM, thermal ceiling 92°C.
- Existing domain taxonomy: `agriculture`, `water`, `food`, `electronics`, `building`, `energy`.
- The `ZimWriter` class interface: `add_article(path, content, article_type, ...)` → `create_zim()` → `ZimWriteResult`.

---

## Priority 1: Medical Reference Module

**Composite score**: 8.20 (highest among all Phase 5.2 candidates).
**Rationale**: Highest life-safety value. Source content exists in `off-grid-living/08-medical-health.md` (~1,500+ lines). No new Python library dependencies. Serves ~2 billion people without reliable healthcare access.

### Data Sourcing

All sources are open-access or public domain. No scraping needed — all are downloadable structured data.

| Source | URL | Format | License | What to extract |
|---|---|---|---|---|
| WHO Essential Medicines List | https://www.who.int/groups/expert-committee-on-selection-and-use-of-essential-medicines/essential-medicines-lists | PDF (also structured CSV via WHO API) | CC BY-NC-SA 3.0 IGO | Drug name, indication class, dosage forms, standard treatment notes |
| off-grid-living 08-medical-health.md | Internal — `projects/off-grid-living/08-medical-health.md` | Markdown | Internal | Condition sections, drug monographs, dosing tables, evacuation criteria |
| Wilderness Medical Society guidelines | https://wms.org/magazine/1288/wms-practice-guidelines | Open access PDFs | As cited per publication | Field treatment protocols, austere environment decision trees |
| ICRC First Aid guidelines | https://www.icrc.org/en/first-aid-guidelines | PDF | ICRC open access | First aid procedure steps, triage criteria |
| RxNorm drug database | https://www.nlm.nih.gov/research/umls/rxnorm/index.html | CSV/JSON (NLM API) | Public domain (US government) | Drug name normalization, interaction data, generic/brand cross-reference |
| National Library of Medicine MedlinePlus | https://medlineplus.gov/ | Structured HTML, XML feeds | Public domain | Patient-readable condition summaries (supplement, not primary source) |

**Download sequence (June 1–2)**:
1. Download WHO Essential Medicines List PDF and extract CSV. The WHO has structured versions available via their API (`https://list.essentialmedicines.org/`).
2. Copy `off-grid-living/08-medical-health.md` to the importer's source directory.
3. Download ICRC First Aid PDF and extract procedure sections.
4. Pull RxNorm download file from NLM (free registration, no OAuth required): `https://www.nlm.nih.gov/research/umls/licensedcontent/rxnormfiles.html`.

**Source validation rule**: Never modify WHO or USDA dosing data. Transcription errors in medical dosing are dangerous. If the source document says 500 mg, the ZIM article must say 500 mg — no rounding, no interpolation. Add a `source_citation` field to every medical article pointing to the exact source document and page number.

### Content Structure

Each medical article is one of three types:

**Type 1: Condition article** (one per medical condition)
```
Fields:
- condition_name (string): "Dehydration — Moderate"
- synonyms (list): ["Fluid deficit", "Volume depletion"]
- indication_summary (string, ≤200 chars): Brief description for Xapian search
- signs_and_symptoms (list): Bullet list, 3–8 items
- treatment_steps (ordered list): Step-by-step, numbered
- medications (list of drug references): Links to drug monograph articles
- evacuation_criteria (string): When to transport for definitive care
- evidence_level (enum): WHO_LISTED | FIELD_PROTOCOL | EMPIRICAL
- source_citation (string): "off-grid-living 08-medical-health.md §3.2"
```

**Type 2: Drug monograph article** (one per drug class or specific drug)
```
Fields:
- drug_name (string): "Amoxicillin"
- drug_class (string): "Antibiotic — Penicillin"
- indications (list): Conditions this drug treats (links to condition articles)
- adult_dose (string): "500 mg PO TID x 7 days"
- pediatric_dose (string): "40 mg/kg/day divided TID" (weight-based)
- contraindications (list): Absolute and relative
- supply_quantity_1yr (string): "42 capsules (500 mg) for one adult"
- storage_requirements (string): "Room temperature, dry"
- who_essential_medicines (bool): True if on WHO EML
- source_citation (string): "WHO EML 2025, Section 6.1"
```

**Type 3: Procedure article** (one per clinical procedure)
```
Fields:
- procedure_name (string): "Wound Irrigation"
- indication (string): When to perform this procedure
- supplies_needed (list): Equipment checklist
- steps (ordered list): Numbered steps
- failure_signs (list): When the procedure is failing
- source_citation (string): "ICRC First Aid Guidelines 2024"
```

The existing `content_items` schema uses a `content_jsonld` JSON-LD blob. The three medical article types map to three new `item_type` values: `medical_condition`, `drug_monograph`, `medical_procedure`. These extend the existing type enum without requiring a migration change.

### ZIM Integration

The ZIM integration uses the existing `ZimWriter.add_article()` interface. No API changes are needed. The `MedicalReferenceArchiver` module is a standalone importer that produces articles and feeds them to `ZimWriter`.

**Compatibility check**: The existing ZIM integration uses `article_type='procedure'` as the Jinja2 template selector. The new `medical_condition` and `drug_monograph` types will require two new Jinja2 templates:
- `templates/medical_condition.html` — quick-reference card layout (condition on top, treatment steps, medications, evacuation criteria).
- `templates/drug_monograph.html` — dosing reference layout (drug name header, adult/pediatric doses in a clear table, contraindications in red-bordered box, supply quantity).

Both templates must be self-contained (no external CSS). Use inline `<style>` blocks with system fonts only.

**Offline constraint verification**: The existing test `test_html_no_external_dependencies` in `tests/unit/test_zim_writer_libzim.py` scans all articles for `http://` in `src`/`href` attributes. Medical articles must pass this test. Source citations are plain text, not hyperlinks.

**ZIM article path naming convention**:
```
medicine/condition/{slug}        # e.g., medicine/condition/dehydration-moderate
medicine/drug/{slug}             # e.g., medicine/drug/amoxicillin
medicine/procedure/{slug}        # e.g., medicine/procedure/wound-irrigation
medicine/index                   # Table of contents article
```

### Resource Estimate

| Task | Hours | Description |
|---|---|---|
| Data download and audit | 2 | WHO EML CSV, off-grid-living extraction, ICRC PDF, RxNorm |
| Content schema design | 1.5 | Finalize 3 article type field definitions |
| `MedicalReferenceArchiver` module | 5 | `app/services/importers/medical_importer.py`, ~250 lines |
| Jinja2 templates | 2 | `medical_condition.html`, `drug_monograph.html`, `medical_procedure.html` |
| Disclaimer system | 1 | Legal/liability boilerplate in base template (required before publication) |
| Unit tests | 4 | ~25 tests: field validation, dosing format, XSS prevention in medical content |
| ZIM integration test | 2 | Generate medical ZIM, verify with zimcheck, open in Kiwix |
| Medical accuracy review | 4 | Manual review of all dosing values against source documents |
| **Total** | **21.5** | |

**Note on accuracy review**: The 4-hour medical accuracy review is not optional. Every dosing value in a drug monograph must be cross-checked against the exact source document before the ZIM is published. This review is done by the author, not automated. The accuracy review gates the ZIM publication step.

### Timeline: June 1–15

```
June 1 (Mon):  Branch: git checkout -b feature/phase-5.2-medical
               Data download: WHO EML CSV, off-grid-living copy, ICRC PDF
               Content schema: Finalize 3 article type field definitions
               
June 2 (Tue):  Implement MedicalReferenceArchiver importer (~250 lines)
               Parse off-grid-living 08-medical-health.md sections
               
June 3 (Wed):  Implement Jinja2 templates for 3 article types
               Implement disclaimer system (liability boilerplate)
               
June 4 (Thu):  Write unit tests (25 tests)
               Run: uv run pytest tests/ -k "medical" -v
               Expected: all pass
               
June 5 (Fri):  Outline complete milestone: Medical module generates correct
               article JSON for at least 20 conditions and 30 drug monographs.
               Gate: this milestone gates Water module start (see parallel analysis)
               
June 6–7:      ZIM integration test: generate medical.zim with zimcheck
               Verify in Kiwix Android: articles render, search finds "amoxicillin"
               
June 8–11:     Medical accuracy review: cross-check all dosing values
               Fix any transcription errors found in review
               
June 12 (Fri): Medical first draft complete milestone.
               Gate: this milestone gates ZIM integration validation for Water/Seed
               Push feature branch: git push open-repo feature/phase-5.2-medical
               
June 13–14:    Final test run (full suite), fix any failures
               Write CHECKIN.md entry for user review of medical PR
               
June 15 (Mon): Medical module ready for PR merge review.
```

### Success Metrics for Medical Module

- [ ] `MedicalReferenceArchiver` produces at least 60 articles: ≥20 conditions, ≥30 drug monographs, ≥10 procedures.
- [ ] All articles pass `test_html_no_external_dependencies` (no external URLs in HTML content).
- [ ] `zimcheck` passes on the generated `open-repo_en_medicine_YYYY-MM.zim` file.
- [ ] ZIM file is readable in Kiwix: articles display, search returns results for at least 5 drug names.
- [ ] Medical accuracy review complete: all dosing values verified against source citations.
- [ ] All 25 unit tests pass in under 1 second (stub mode; integration tests with real libzim run separately).
- [ ] Disclaimer boilerplate present and visible on all condition and drug monograph articles.

---

## Priority 2: Water Systems Module

**Composite score**: 7.90.
**Rationale**: Priority 1 in systems-resilience execution queue. The existing "water" domain in the taxonomy has no structured procedural content — this fills it. Source documents exist (off-grid-living 03-water.md, systems-resilience individual/01-water.md). No new Python dependencies.

### Data Sourcing

| Source | URL | Format | License | What to extract |
|---|---|---|---|---|
| WHO Water Quality Guidelines | https://www.who.int/publications/i/item/9789241549950 | PDF (also as structured HTML) | CC BY-NC-SA 3.0 IGO | Quality parameters, treatment effectiveness, turbidity thresholds |
| CDC Water Treatment Guidance | https://www.cdc.gov/healthywater/drinking/index.html | HTML (structured pages) | Public domain | Treatment methods, chlorination rates, boiling times by elevation |
| USDA Rural Water/Well Guides | https://www.rd.usda.gov/sites/default/files/... (search "rural water well") | PDF | Public domain | Well drilling methods, pump selection, yield calculations |
| off-grid-living 03-water.md | Internal — `projects/off-grid-living/03-water.md` | Markdown | Internal | Household sizing, filtration selection, storage calculations |
| systems-resilience individual/01-water.md | Internal — `projects/systems-resilience/individual/01-water.md` | Markdown | Internal | Priority procedures, schematic references, community scale guidance |
| Simple Pump documentation | https://www.simplepump.com/resources/technical | HTML/PDF | Proprietary, reference only | Hand pump construction reference (cite, do not reproduce verbatim) |

**Important note on schematics**: The systems-resilience PLAN.md lists "hand pump construction schematics" and "well drilling — hand methods" as research gaps. ZIM is HTML-only. Schematics must be represented as SVG (embedded inline in HTML) or ASCII art. Budget 2–3 hours for schematic conversion for the most critical diagrams (hand pump cross-section, pitcher pump assembly).

### Content Structure

The water module extends the existing "water" domain with two new `item_type` values:

**Type 1: Water procedure article** (`water_procedure`)
```
Fields:
- procedure_name (string): "Household Chlorination — Shallow Well"
- water_source_type (enum): WELL | SURFACE | RAINWATER | PIPED
- household_size (enum): INDIVIDUAL | FAMILY_4 | COMMUNITY_25 | COMMUNITY_100
- treatment_steps (ordered list): Numbered steps with exact quantities
- chemical_quantities (dict): {"sodium_hypochlorite_pct": 5, "dose_ml_per_100L": 4}
- contact_time_minutes (int): Minimum contact time before use
- quality_test_result (string): "Residual chlorine 0.2–0.5 mg/L"
- source_citation (string): "CDC 2022, Table 1"
```

**Type 2: Sizing guide article** (`sizing_guide`)
```
Fields:
- sizing_scenario (string): "4-person household, all uses, no sanitation"
- daily_requirement_liters (int): 80
- calculation_breakdown (dict): {"drinking": 8, "cooking": 6, "hygiene": 40, "sanitation": 26}
- storage_recommendation_liters (int): 240  # 3-day reserve
- pump_yield_required_lpm (float): 0.5
- notes (string): "Adjust for livestock if applicable"
```

**Type 3: System selection guide** (`system_selection`)
```
Fields:
- scenario (string): "Off-grid, 20-person homestead, drought region"
- recommended_system (string): "Drilled well + submersible pump + 1000L cistern"
- alternatives (list): Ranked by cost and reliability
- decision_criteria (list): Trade-offs for each option
- installation_complexity (enum): INDIVIDUAL | SKILLED_LABOR | PROFESSIONAL
```

**`WaterSizingCalculator` utility** (~150 lines): A static utility class that generates sizing HTML tables at build time. Takes household size and activity profile as inputs; outputs a formatted `<table>` element embedded in the sizing guide article. This runs during ZIM build, not at request time.

### Resource Estimate

| Task | Hours | Description |
|---|---|---|
| Data download and review | 2 | WHO guidelines, CDC guidance, off-grid-living/systems-resilience extraction |
| SVG schematic conversion | 3 | Hand pump cross-section, pitcher pump, well casing diagram (3 schematics) |
| Content schema design | 1 | Finalize 3 article type field definitions |
| `WaterSystemsArchiver` module | 4 | `app/services/importers/water_importer.py`, ~200 lines |
| `WaterSizingCalculator` | 3 | Static sizing table generator, ~150 lines |
| Jinja2 templates | 2 | `water_procedure.html`, `sizing_guide.html`, `system_selection.html` |
| Unit tests | 3 | ~20 tests: sizing calculations, procedure step validation, schematic rendering |
| ZIM integration test | 2 | Generate water.zim, verify with zimcheck |
| **Total** | **20** | |

### Timeline: June 10–30

```
June 10 (Wed): Branch: git checkout -b feature/phase-5.2-water
               Data download: WHO, CDC, USDA, off-grid-living extraction
               Begin SVG schematic conversion (hand pump cross-section)
               
June 11 (Thu): Complete 3 SVG schematics
               WaterSizingCalculator design: input/output specification
               
June 12 (Fri): Implement WaterSizingCalculator (~150 lines)
               Unit tests for sizing calculations (8 tests)
               
June 13–14:    Implement WaterSystemsArchiver importer (~200 lines)
               Parse off-grid-living 03-water.md and systems-resilience 01-water.md
               
June 15 (Mon): Implement Jinja2 templates (3 templates)
               
June 16–17:    Write remaining unit tests (~12 tests)
               Run: uv run pytest tests/ -k "water" -v — all pass
               
June 18–20:    ZIM integration test: generate water.zim with zimcheck
               Verify in Kiwix: schematics render, sizing tables display correctly
               
June 21–28:    Content review: verify WHO and CDC data values transcribed correctly
               Fix any errors found in review
               
June 28 (Sun): Push feature branch: git push open-repo feature/phase-5.2-water
               Write CHECKIN.md entry for user review
               
June 30 (Tue): Water module ready for PR merge review.
```

### Success Metrics for Water Module

- [ ] `WaterSystemsArchiver` produces at least 40 articles: ≥15 procedures, ≥10 sizing guides, ≥5 system selection guides, ≥10 general water knowledge articles.
- [ ] At least 3 SVG schematics embedded correctly in articles (hand pump, pitcher pump, well casing).
- [ ] `WaterSizingCalculator` produces correct sizing for all 4 household sizes (individual, family-4, community-25, community-100).
- [ ] `zimcheck` passes on `open-repo_en_water_YYYY-MM.zim`.
- [ ] All WHO and CDC chemical quantity values verified against source citations.
- [ ] 20 unit tests pass.

---

## Priority 3: Seed Preservation Module

**Composite score**: 7.80.
**Rationale**: Direct archival of seedwarden project content. Knowledge is irreversible to lose — if heritage variety seed saving knowledge is unavailable offline, it cannot be recreated. Source documents already written by the seedwarden project.

### Data Sourcing

| Source | URL / Path | Format | License | What to extract |
|---|---|---|---|---|
| seedwarden project docs | Internal — `projects/seedwarden/` | Markdown | Internal | Seed saving procedures, viability data, variety identification |
| GRIN (USDA Germplasm Resources Information Network) | https://www.grin.usda.gov/gringlobal/dataExport.aspx | CSV/XML download | Public domain | Species viability data: temp, humidity, expected years for 500+ species |
| USDA PLANTS Database | https://plants.usda.gov/downloads | CSV | Public domain | Species taxonomy, growing zones (US zones 3–8), growth habit |
| off-grid-living 04-food-production.md | Internal | Markdown | Internal | Seed saving chapter, storage recommendations |
| systems-resilience midwest/calendar.md | Internal | Markdown | Internal | Zone-specific planting calendar cross-references |
| Open Pollinated seed catalogs | Fedco Seeds (https://www.fedcoseeds.com/), Baker Creek (https://www.rareseeds.com/) — reference only | HTML | Proprietary, reference only | Variety name validation (do not reproduce catalog text) |

**Note on BioPython**: The `biopython>=1.87` dependency is optional. The core seed preservation module works without it. BioPython would be needed only if genetic sequence data (FASTA/GenBank files from GRIN) is included in Phase 5.2. Recommendation: defer genetic sequence archival to Phase 5.3. Keep Phase 5.2 seed module free of BioPython dependency to maintain the zero-new-dependencies record established by Candidates 2 and 3.

### Content Structure

The seed module introduces the "seeds" ZIM domain. Three new `item_type` values:

**Type 1: Seed species card** (`seed_species`)
```
Fields:
- common_name (string): "Cherokee Purple Tomato"
- latin_binomial (string): "Solanum lycopersicum var. 'Cherokee Purple'"
- usda_symbol (string): "SOLY" (from USDA PLANTS database)
- variety_type (enum): OPEN_POLLINATED | HEIRLOOM | HYBRID | LANDRACE
- growing_zones_us (list): [5, 6, 7, 8]
- days_to_maturity (int): 80
- seed_saving_type (enum): SELF_POLLINATING | CROSS_POLLINATING | WIND_POLLINATED
- isolation_distance_ft (int): 25 (for cross-pollinating varieties)
- seed_extraction_method (string): "Fermentation method; ferment pulp 2–3 days"
- viability_years (int): 4  (from GRIN data)
- storage_temp_f_max (int): 50
- storage_humidity_pct_max (int): 50
- germination_rate_pct_min (int): 70  (minimum viable for planting)
- source_citation (string): "GRIN Viability Data, seedwarden seed-saving-field-manual.md §4.1"
```

**Type 2: Viability testing article** (`viability_test`)
```
Fields:
- test_name (string): "Water Float Test"
- time_required_minutes (int): 5
- supplies_needed (list): ["Glass of water", "Seeds to test"]
- steps (ordered list): Numbered procedure
- interpretation (dict): {"floaters": "low viability — may still germinate", "sinkers": "high viability"}
- limitations (string): "Less reliable for very fresh seeds"
- source_citation (string): "seedwarden seed-saving-field-manual.md §2.3"
```

**Type 3: Regional growing calendar** (`planting_calendar`)
```
Fields:
- region (string): "USDA Zone 5 — Central Midwest"
- frost_dates (dict): {"last_spring_frost": "May 10", "first_fall_frost": "Oct 5"}
- species_list (list): Each entry: {species, start_indoors_weeks, transplant_date, direct_sow_date}
- notes (string): Zone-specific notes
- source_citation (string): "systems-resilience midwest/calendar.md"
```

**`SeedViabilityCalculator` utility** (~100 lines): Takes species GRIN data and current year; generates a viability projection table showing expected germination rate decline over storage years. Embedded in species card articles as a static HTML table.

### Resource Estimate

| Task | Hours | Description |
|---|---|---|
| Data download and review | 2 | GRIN CSV, USDA PLANTS CSV, seedwarden extraction |
| Content schema design | 1 | Finalize 3 article type field definitions |
| `SeedPreservationArchiver` module | 4 | `app/services/importers/seed_importer.py`, ~200 lines |
| `SeedViabilityCalculator` | 2 | Viability projection table generator, ~100 lines |
| GRIN data parser | 3 | Parse GRIN CSV and extract viability data for 500+ species |
| Jinja2 templates | 2 | `seed_species.html`, `viability_test.html`, `planting_calendar.html` |
| Unit tests | 3 | ~20 tests: viability calculations, species card validation, calendar rendering |
| ZIM integration test | 2 | Generate seeds.zim, verify with zimcheck |
| Content review | 2 | Verify GRIN viability data correctly transcribed |
| **Total** | **21** | |

### Timeline: June 15 – July 5

```
June 15 (Mon): Branch: git checkout -b feature/phase-5.2-seed
               Data download: GRIN CSV, USDA PLANTS CSV download (large files — start early)
               Begin seedwarden content extraction
               
June 16–17:    Implement GRIN data parser (~150 lines)
               Extract viability data for 500+ species, validate against known values
               
June 18 (Thu): Implement SeedViabilityCalculator (~100 lines)
               Unit tests for viability calculations (8 tests)
               
June 19–20:    Implement SeedPreservationArchiver importer (~200 lines)
               Parse seedwarden seed-saving-field-manual.md
               Parse off-grid-living 04-food-production.md seed saving chapter
               
June 21 (Sun): Content schema finalization: review species card fields
               
June 22–24:    Implement Jinja2 templates (3 templates)
               Write remaining unit tests (~12 tests)
               Run: uv run pytest tests/ -k "seed" -v — all pass
               
June 25–28:    ZIM integration test: generate seeds.zim with zimcheck
               Verify in Kiwix: species cards display correctly
               Content review: spot-check 20 species viability values against GRIN
               
June 29 (Mon): Fix any errors found in content review
               
June 30 (Tue): Push feature branch: git push open-repo feature/phase-5.2-seed
               Write CHECKIN.md entry for user review
               
July 1–3:      Final test run, fix any failures
               
July 5 (Sun):  Seed module ready for PR merge review.
```

### Success Metrics for Seed Module

- [ ] `SeedPreservationArchiver` produces species cards for at least 200 species (subset of GRIN database covering food-producing and medicinal species for US zones 3–8).
- [ ] `SeedViabilityCalculator` produces correct viability projections for all 200 species (validated against at least 10 known GRIN reference values).
- [ ] Regional growing calendars for at least 5 USDA hardiness zones (zones 3–8 is the target).
- [ ] `zimcheck` passes on `open-repo_en_seeds_YYYY-MM.zim`.
- [ ] ZIM readable in Kiwix: species cards display, search finds "Cherokee Purple".
- [ ] 20 unit tests pass.
- [ ] Viability data spot-check: 20 randomly selected species verified against GRIN source.

---

## Parallel vs. Sequential Analysis

### The Core Question

Can Medical, Water, and Seed all start June 1? The priority matrix scoring (8.20, 7.90, 7.80) implies parallel execution. The question is whether the constraints justify it.

### Constraints That Apply to All Three Modules

**Single author constraint**: All three modules require the same author. Parallelizing three implementation tracks means context-switching between three content domains simultaneously. Medical dosing, water chemistry quantities, and seed viability data each require careful attention. Errors in any are dangerous. Context-switching between them in the same day is a quality risk.

**ZIM integration testing constraint**: Each module generates a ZIM file that must be validated with zimcheck and manually verified in Kiwix. This testing cannot be parallelized — it requires the author's attention to verify that articles render correctly and search works. Three simultaneous ZIM validation cycles would require three separate test ZIM files open at the same time, which is feasible technically but cognitively demanding.

**Content sourcing workflow constraint**: Medical requires downloading WHO/ICRC PDFs and extracting structured data. Water requires downloading WHO/CDC guidance and converting schematics to SVG. Seed requires downloading GRIN CSV and USDA PLANTS CSV (large files). Starting all three downloads simultaneously on June 1 is fine — they are independent. But processing each source into structured article data requires sequential focus.

**Medical accuracy review constraint**: The medical accuracy review (4 hours) is a hard sequential constraint. It cannot be parallelized with anything — it requires focused review of every dosing value. This review gates the Medical module's publication. The review cannot begin until the Medical first draft is complete (target: June 12).

### Option A: Full Parallel (All Three Start June 1)

All three branches created June 1. Work proceeds simultaneously.

**Benefits**:
- Earliest possible completion for all three (Water could complete by ~June 20, Seed by ~June 28, assuming Medical complete June 15).
- Maximizes use of time if the author is disciplined about context-switching.

**Risks**:
- Content quality risk: Medical dosing errors caused by rushing to also work on Water chemistry or Seed viability data. These are different cognitive domains — simultaneous work increases the probability of transcription errors.
- ZIM validation risk: Three ZIM files in parallel validation requires careful tracking of which article appeared in which ZIM file.
- Medical accuracy review would still block the Medical ZIM publication until June 12–13, regardless of how early the Water and Seed modules started.

**Honest assessment of full parallel**: The content quality risk in Medical is not acceptable. Medical dosing errors are not just bugs — they are safety hazards. The medical accuracy review is a gate that already serializes Medical publication relative to any other work. The practical benefit of starting Water and Seed on June 1 instead of June 10/15 is 2–5 days of schedule compression for the overall June roadmap. That 2–5 day gain does not justify the quality risk from simultaneous context-switching across three life-safety content domains.

### Option B: Sequential with Staggered Start Dates (Recommended)

**Medical**: June 1–15 (gates Water start on June 10)
**Water**: June 10–30 (starts when Medical outline is complete June 5)
**Seed**: June 15 – July 5 (starts when Medical first draft is complete June 12)

The stagger dates are not arbitrary. They are derived from the Medical module's internal milestones:
- June 5: Medical outline complete (generates correct article JSON for 20+ conditions and 30+ drug monographs). This milestone confirms the article schema is stable enough that Water can use it as a reference — Water's `water_procedure` and `sizing_guide` schemas follow the same structural pattern.
- June 12: Medical first draft complete. By this date, the Jinja2 template pattern is established, the ZIM integration test harness is proven, and the unit test patterns are defined. Water and Seed can reuse all of this.

**Benefits of staggered starts**:
- Medical receives focused author attention June 1–12 with no distraction.
- Water starts with the benefit of seeing Medical's completed module as a reference implementation — importer structure, template patterns, and unit test patterns are all already established.
- Seed starts with the benefit of both Medical and Water as reference implementations.
- Each module's ZIM integration test runs sequentially, reducing cognitive load.

**Costs of staggered starts**:
- Water completes June 30 instead of ~June 20 (10-day delay).
- Seed completes July 5 instead of ~June 28 (7-day delay).
- Total June 1–30 deliverable count: 1 module ready for PR (Medical), 1 in review (Water), 1 in development (Seed). Vs. full parallel: potentially 3 in review by June 30.

### Risk Profile Comparison

| Risk | Full Parallel | Staggered |
|---|---|---|
| Medical dosing transcription error | Higher (context-switching) | Lower (focused attention) |
| Water chemistry value error | Moderate | Lower (Medical template as reference) |
| Seed viability data error | Moderate | Lower (Medical+Water as reference) |
| ZIM validation confusion (wrong file) | Higher (3 files simultaneously) | Lower (sequential validation) |
| Overall quality risk | HIGH for Medical | LOW for all three |
| Schedule compression (days gained) | 7–10 days faster | 0 (baseline) |
| June 30 deliverable count | 3 in review (if clean) | 1 ready + 1 in review + 1 in dev |

### Recommendation: Staggered Sequential

Start Medical June 1. Start Water June 10 (after Medical outline complete). Start Seed June 15 (after Medical first draft complete). This is the safer approach for public-facing, safety-critical content.

If the user explicitly accepts the quality risk and wants to compress the schedule, Water can start June 1 alongside Medical with the following constraint: Water implementation work happens only after Medical daily tasks are complete. No day should involve simultaneous Medical content editing and Water content editing.

---

## Success Metrics and Rollback Triggers

### Phase 5.2 Pre-Start Gate (Before Any Phase 5.2 Branch Is Created)

These must be true before June 1 work begins:

- [ ] Phase 5.1 48-hour production monitoring window complete with zero errors.
- [ ] Post-merge action items complete: XSS fix, ZimExport ORM, pyproject.toml dependency.
- [ ] `uv run pytest tests/ -q` on master shows 240 passed, 0 failures.
- [ ] `alembic current` shows `003 (head)` on production database.
- [ ] libzim confirmed installed on deployment target Pi 5.

### Shared Metrics for All Three Modules

**Database migration success metrics**:
- Migration applies without error (`alembic upgrade head` exits 0).
- All new content types appear in the `content_items` schema as valid `item_type` enum values.
- No existing Phase 1–4 data is modified or deleted.
- Zero foreign key constraint violations (`PRAGMA foreign_key_check` returns empty).

**ZIM export success metrics**:
- Generated ZIM file size > 50 MB indicates valid content (nopic variant with 200+ articles). Files below 1 MB indicate stub path or empty export.
- `zimcheck` exits 0 (no warnings about metadata, illustration, or content).
- ZIM file is readable by Kiwix (articles open, content displays, full-text search returns results).
- ZIM exports all expected articles: `result.article_count` matches the number of `add_article()` calls.

**Test coverage metrics**:
- Each module: minimum 20 unit tests, all passing.
- Full test suite after each module: prior 240 tests still pass (no regressions).
- Integration test with real libzim produces valid ZIM (zimcheck passes, article count correct).

**Rollback triggers for Phase 5.2 modules**:

- **Dosing/quantity value discrepancy**: If content review finds a medical dosing value, water chemical quantity, or seed viability value that differs from the source document by more than rounding — stop publication, fix the error, re-run content review for all articles in the same category. Do not publish the ZIM until the full category passes review.

- **ZIM article count mismatch**: If `result.article_count` is less than 90% of the number of `add_article()` calls — investigate Creator session handling before publishing. A 10% or greater drop in article count indicates a systematic bug in the importer.

- **zimcheck failure**: If zimcheck exits non-zero — diagnose immediately. Common causes: illustration dimensions wrong (must be 48x48 PNG), description field exceeds 80 characters, name field contains uppercase or spaces. Fix the specific violation and regenerate. Do not publish a ZIM that fails zimcheck.

- **Module test regression**: If adding a new Phase 5.2 module causes any of the original 240 Phase 5.1 tests to fail — revert the new module changes and investigate before merging. The Phase 5.1 test suite is the stability contract.

### Module-Specific Gates

**Medical outline complete by June 5** — gates Water module start:
- Medical importer produces valid article JSON for at least 20 conditions and 30 drug monographs.
- Article field validation passes for all 3 article types.
- No template errors in Jinja2 rendering.

**Medical first draft complete by June 12** — gates ZIM integration validation for Water and Seed:
- All Medical unit tests pass (25 tests).
- Medical ZIM generates with zimcheck passing.
- Medical accuracy review scheduled (may not be complete by June 12, but must be scheduled).

**ZIM integration validated before publication** — applies to all three modules:
- No module's ZIM is published to the OPDS catalog or CDN until zimcheck passes AND the content accuracy review is complete.
- "Content accuracy review" means: every numerical value (dose, quantity, storage temperature, viability years) has been cross-checked against its source citation by the author.

---

## Appendix: Phase 5.2 Architecture Notes

**Module file locations** (following the Phase 5.1 importer pattern):
- `app/services/importers/medical_importer.py`
- `app/services/importers/water_importer.py`
- `app/services/importers/seed_importer.py`
- `app/templates/medical_condition.html`
- `app/templates/medical_drug_monograph.html`
- `app/templates/medical_procedure.html`
- `app/templates/water_procedure.html`
- `app/templates/sizing_guide.html`
- `app/templates/seed_species.html`

**New ZIM files produced by Phase 5.2**:
- `open-repo_en_medicine_YYYY-MM.zim` (estimated 2–8 MB, 200–500 articles)
- `open-repo_en_water_YYYY-MM.zim` (estimated 1–3 MB, 50–150 articles)
- `open-repo_en_seeds_YYYY-MM.zim` (estimated 3–10 MB, 500–1,500 articles)

**No new Python runtime dependencies for Phase 5.2 (Candidates 2, 3, 9)**:
- BioPython is optional and deferred to Phase 5.3.
- pvlib is deferred to Phase 5.3 (Energy Systems, Candidate 4).
- No new dependencies means Phase 5.2 modules install cleanly on any environment where Phase 5.1 works.

**Content disclaimer requirement (Medical only)**:
All medical condition and drug monograph articles must include a visible disclaimer. Suggested text:
> "This information is for reference in austere environments where professional medical care is unavailable. It does not replace professional medical advice. Seek qualified medical care whenever possible."

The disclaimer must be rendered prominently in the article template — not in a collapsed section, not in a footnote. Place it at the top of every medical article, before treatment content.
