---
title: "Phase 5.2 Implementation Roadmap — Post-Merge Execution Plan"
project: open-repo
phase: "5.2 implementation planning"
status: "pre-activation (awaiting Phase 5.1 merge, expected May 25-26)"
created: 2026-05-21
author: General Research Agent
depends_on: "PHASE_5.2_PRIORITY_MATRIX.md, PHASE_5.2_CAPABILITY_AUDIT.md, PHASE_5.2_FEATURE_CANDIDATES.md"
activation_gate: "Phase 5.1 merge confirmed + four post-merge action items resolved"
---

# Phase 5.2 Implementation Roadmap

## Executive Summary

Phase 5.2 expands the open-repo ZIM pipeline from infrastructure (Phase 5.1) to content coverage across five new domains: medicine, water systems, seed preservation, food preservation, and botanical knowledge. All five are archival projects — the hard intellectual work (source documents, data validation, medical review) already exists in the user's active projects. Phase 5.2 is primarily a structuring and pipeline exercise.

**Target window**: June 1 – July 4, 2026 (34 days)
**Total estimated effort**: 55–75 person-hours across five modules
**Critical path**: Medical content sourcing review (must begin before June 1 to avoid blocking Wave 1)
**One-developer feasibility**: Yes — parallel modules within each wave are independent; a single developer can alternate between them in the same day

---

## Phase 5.1 Activation Prerequisites

Before any Phase 5.2 code is written, the four post-merge action items from the Phase 5.1 audit must be resolved. These are tracked in `phase-5-1-pre-merge-audit-findings.md`.

| Action | Blocker for |
|---|---|
| `html.escape()` on `source_node_url` / `source_node_name` in attribution footer | Federated content export (Phase 5.2 module cross-references) |
| `ZimExport` SQLAlchemy ORM class added to `app/models.py` | All Phase 5.2 modules (they register exports via the same ORM) |
| `libzim>=3.10.0,<4.0` in `pyproject.toml` and installed | End-to-end ZIM generation test for all new modules |
| README updated for Phase 5 | Documentation accuracy for new domains |

Phase 5.2 feature branches **can** be created before Actions 1–4 are resolved, and stub-mode unit tests will pass without libzim. However, the ZIM integration tests (generating a real `.zim` file and validating with `zimcheck`) require Action 3. Plan to resolve all four action items in the first three days of June before Wave 1 implementation begins.

---

## Wave Structure Overview

| Wave | Dates | Modules | Est. Hours | Gate |
|---|---|---|---|---|
| Wave 0 (pre-work) | May 22 – May 31 | Medical sourcing outreach, schema design, branch setup | 6–10 | Phase 5.1 merge confirmed |
| Wave 1 | June 1 – June 10 | Medical Reference + Water Systems | 18–26 | Wave 0 complete; Action 2 (ORM) resolved |
| Wave 2 | June 11 – June 20 | Seed Preservation + Food Preservation | 20–28 | Wave 1 modules pass zimcheck |
| Wave 3 | June 21 – July 4 | Botanical Knowledge (+ buffer) | 12–16 | Wave 2 modules pass zimcheck |
| Integration | July 1 – July 4 | Full ZIM build, OPDS catalog update, CDN push | 3–5 | All modules pass individual zimcheck |

**Total**: 59–85 person-hours. With 2–3 focused hours per working day, this is a 30–35 day window. June 1 start and July 4 delivery is achievable with no slack removed.

---

## Wave 0: Pre-Implementation (May 22 – May 31)

Wave 0 runs before the Phase 5.1 merge is confirmed. It does not write production code. Its purpose is to eliminate the two longest lead-time items so they do not block Wave 1.

### 0.1 Medical Content Review Initiation (CRITICAL PATH)

The medical module is the highest-priority candidate and has the longest non-technical lead time: a medical accuracy review is mandatory before any `MedicalReferenceArchiver` content is published in a ZIM. This review cannot happen the same week the code is written.

**Actions required in Wave 0**:
- Identify a medical reviewer (wilderness medicine physician, pharmacist, or trained EMT with field medicine background) who can verify that drug dosing tables and procedure protocols from `off-grid-living/08-medical-health.md` are accurate and appropriately caveated for austere environments.
- Share the draft content outline (article categories: drug monographs, procedure guides, first aid protocols, evacuation criteria) with the reviewer so they understand the scope.
- Establish a review turnaround timeline: aim for the reviewer to provide feedback by June 20, so Wave 1 Medical articles can be revised before the Wave 3 integration build.

This is not a code task. It is a content quality and liability task. If medical review is not initiated in Wave 0, it becomes a blocker for the final June ZIM release.

### 0.2 Content Type Schema Draft

Before Wave 1 code begins, draft the data schemas for all five new content types. This is the technical design work that prevents rework in Wave 1–3.

**Deliverables from Wave 0**:
- `medical_article` schema: fields for indication, symptom list, dosing (adult/pediatric/weight-based), contraindications, drug interactions (clinically significant only), supply quantity for 1-year stock, evacuation criteria, disclaimer text (non-negotiable field, cannot be null)
- `water_procedure` schema: procedure name, equipment list, steps (ordered list), sizing inputs/outputs, safety thresholds (e.g., acceptable turbidity NTU range), source citation
- `seed_species` schema: common name, Latin binomial, family, GRIN accession number, storage temperature/humidity, expected viability years, germination rate, USDA hardiness zones, seed saving difficulty
- `food_safety_table` schema: food type, jar size, pressure/water bath method, processing time in minutes, altitude adjustment table, botulism risk level, source (must be USDA or equivalent, cannot be blank)
- `botanical_species` schema: extends `seed_species` with edibility classification, toxicity notes, evidence level for medicinal claims (A = clinical trial, B = traditional use, C = anecdotal), lookalike hazard warnings

**Estimated time**: 4–6 hours total (schema definition, not implementation)

### 0.3 Feature Branch Creation

Create the feature branch immediately after Phase 5.1 merge is confirmed:

```
git checkout main
git pull origin main
git checkout -b feature/phase-5.2-wave-1
```

Subsequent waves get their own branches:
- `feature/phase-5.2-wave-2`
- `feature/phase-5.2-wave-3`

Each wave branch is created from `main` after the previous wave merges. This keeps the branches small and reviewable.

---

## Wave 1: Medical Reference + Water Systems (June 1 – June 10)

Wave 1 targets the two highest-priority candidates (scores 8.20 and 7.90). Both have no new Python dependencies, complete internal source documents, and directly address life-critical knowledge gaps.

### Development Phases

**Phase 1a: Stub Architecture (June 1–2)**

Create the module skeletons with full type signatures, docstrings, and `raise NotImplementedError` bodies. This gives the test suite something to run against before any logic is implemented.

Files to create:
- `app/services/importers/medical_importer.py` — `MedicalReferenceArchiver` class
- `app/services/importers/water_importer.py` — `WaterSystemsArchiver` class
- `app/templates/medical_article.html` — ZIM article template
- `app/templates/water_procedure.html` — ZIM article template
- `tests/test_medical_importer.py` — 25 test stubs (see test specification below)
- `tests/test_water_importer.py` — 20 test stubs

All 45 test stubs should exist and fail (not error) before Phase 1b begins. This confirms the test infrastructure works and catches import errors early.

**Phase 1b: Data Sourcing (June 2–4)**

Download and verify all external source files:

Medical sources:
- WHO Model Formulary PDF: `wget https://apps.who.int/iris/bitstream/handle/10665/44053/9789241547659_eng.pdf`
- WHO Essential Medicines List 23rd edition (2023): available as CSV supplement
- ICRC First Aid Guidelines: downloadable PDF at icrc.org
- RxNorm essential medicines subset: NLM provides an API-free SQL dump; extract ~2,000 essential drugs to CSV using the provided RxNorm scripts

Water sources:
- WHO Drinking Water Quality Guidelines 4th edition PDF (2022): downloadable from who.int
- CDC Emergency Water Disinfection guidance: downloadable from cdc.gov
- USDA NRCS well yield and construction guides: available at nrcs.usda.gov

All downloaded files go in `data/sources/` and are listed in `.gitignore` (they are large; only the parsed output goes in git). Add a `scripts/download_sources.sh` script so any developer can reproduce the download.

**Phase 1c: ZIM Integration and Template Implementation (June 4–8)**

Implement both importer classes against the schemas designed in Wave 0. Each importer:
1. Reads structured source data (Markdown + JSON extracted from PDFs)
2. Validates required fields (no null disclaimer on medical articles, no missing citations on safety tables)
3. Renders to HTML via the Jinja2 template
4. Returns a list of `ContentItem`-equivalent objects that the existing ZIM pipeline can process

The medical template must include the disclaimer block as a styled `<aside>` element with high-contrast border, not as small-font body text. This is a content policy requirement, not a style preference.

**Phase 1d: ZIM Validation (June 8–10)**

- Run `uv run pytest tests/test_medical_importer.py tests/test_water_importer.py` — all 45 tests must pass
- Run the existing 88-test Phase 5.1 suite — zero regressions
- Generate a test ZIM with 10–20 sample medical articles and 10 water procedure articles
- Run `zimcheck` against the output file; zero errors permitted
- Open the ZIM in Kiwix Android (or kiwix-serve locally); verify article rendering, search, and cross-links

Wave 1 is complete when: all tests pass, zimcheck reports 0 errors, and a human has confirmed the ZIM renders correctly in Kiwix.

### Resource Allocation

| Task | Hours |
|---|---|
| Medical importer + tests | 10–14 |
| Water importer + tests | 8–12 |
| Shared: schema implementation in `app/models.py` | 2 |
| Shared: ZIM validation and Kiwix spot-check | 2 |
| **Wave 1 total** | **22–30 hours** |

---

## Wave 2: Seed Preservation + Food Preservation (June 11 – June 20)

Wave 2 targets scores 7.80 and 7.65. Both modules use exclusively public-domain data (GRIN, USDA canning guides) and internal seedwarden/off-grid-living source documents. No safety-sensitive external reviewer is required, but the food preservation module has a strict data accuracy requirement: USDA canning processing times must be reproduced verbatim, not derived or interpolated.

### Development Phases

**Phase 2a: Stub Architecture (June 11–12)**

Files to create:
- `app/services/importers/seed_importer.py` — `SeedPreservationArchiver` class
- `app/services/importers/food_importer.py` — `FoodPreservationArchiver` class
- `app/templates/seed_species.html`
- `app/templates/food_safety.html`
- `tests/test_seed_importer.py` — 20 test stubs
- `tests/test_food_importer.py` — 15 test stubs

**Phase 2b: Data Sourcing (June 11–13, parallel with 2a)**

GRIN data:
- GRIN provides bulk CSV downloads of accession data at grin.gov. The relevant subset for Phase 5.2 is "domesticated species with viability data" — approximately 8,000 accessions from 600,000+ total.
- Download once, add to `.gitignore`, parse to `seed_species` records in the importer.

USDA canning data:
- The USDA Complete Guide to Home Canning (2015 edition, public domain) is the sole authoritative source for processing times.
- A structured JSON representation of the processing time tables exists in the `data/` directory from prior research. If it does not, extract from PDF using `pdfplumber` (existing dependency or one-time script).
- Safety requirement: every `food_safety_table` record must carry a `usda_edition` field confirming the source edition. The 2015 edition is the current version as of 2026.

**Phase 2c: Implementation and Testing (June 13–18)**

Viability calculator implementation (`SeedPreservationArchiver`):
- Pre-computes expected seed viability years by species from GRIN data and storage conditions
- Outputs a static HTML table per species — not a live calculator
- Test: for a known species (Zea mays / corn), verify expected viability at 40°F/40% RH matches GRIN reference value within ±10%

Food safety validation (`FoodPreservationArchiver`):
- Every processing time table row must have a corresponding unit test asserting the value matches the source PDF
- This is not a performance test — it is a data integrity test. These tables prevent botulism; they must be correct.
- 15 tests minimum: cover all major food categories (tomatoes, low-acid vegetables, fruits, meats, pickles)

**Phase 2d: ZIM Validation (June 18–20)**

Same validation sequence as Wave 1: tests pass, zimcheck 0 errors, Kiwix spot-check. Additionally:
- Verify that cross-links from seed species articles to food preservation articles work (e.g., "Zea mays" species card links to "Corn — Pressure Canning Safety" article)
- Verify altitude adjustment table renders correctly on a small screen (Kiwix Android)

### Resource Allocation

| Task | Hours |
|---|---|
| Seed importer + tests | 12–16 |
| Food importer + tests | 8–12 |
| Wave 2 ZIM validation | 2 |
| **Wave 2 total** | **22–30 hours** |

---

## Wave 3: Botanical Knowledge (June 21 – July 4)

Wave 3 targets score 7.55. It is the most complex of the three waves due to the USDA PLANTS CSV parsing (44,000 species, must be filtered to a useful subset of ~1,000–3,000 food-producing and medicinal species), the cross-domain linking requirements (botanical articles must link to medical articles where applicable), and the illustration sourcing question (Wikimedia Commons images vs. nopic variant).

### Development Phases

**Phase 3a: USDA PLANTS Subset Definition (June 21–23)**

The full USDA PLANTS CSV is 44,000 species. The ZIM target is 1,000–3,000 articles covering species with:
- Edibility classification (not blank)
- Native range in US hardiness zones 3–8
- At least one of: food use, medicinal use, or significant toxic/lookalike hazard note

Build a filter script (`scripts/filter_usda_plants.py`) that outputs the filtered subset CSV. Target 1,500–2,500 species. Validate output against a hand-curated list of 20 known food/medicinal plants to confirm the filter is not missing important entries.

**Phase 3b: Illustration Sourcing Decision (June 22–24)**

For each filtered species, determine if a Wikimedia Commons image exists under CC BY or CC BY-SA license. This can be done via the Wikimedia REST API (single batch query). The result is a mapping of species to image URL.

Decision gate: if >60% of filtered species have Commons images, include images in the "all" ZIM variant (base64-embedded) and omit in the nopic variant. If <60%, use nopic for the main release and add images to the "illustrated" variant in a Phase 5.3 pass.

**Phase 3c: Implementation and Testing (June 24 – July 1)**

Files to create:
- `app/services/importers/botanical_importer.py` — `BotanicalArchiver` class
- `app/templates/botanical_species.html`
- `tests/test_botanical_importer.py` — 30 test stubs

Key implementation notes:
- Edibility/toxicity classification is safety-critical: a misclassification (marking a toxic plant as edible) could cause harm. Every species with a toxicity flag must have a source citation in the `botanical_species` schema.
- Medicinal evidence level (A/B/C) must be set conservatively: default to C (anecdotal) unless a specific citation to a peer-reviewed study is present in the source data.
- Cross-links to medical articles: where a medicinal herb appears in `off-grid-living/08-medical-health.md` as a treatment, add a `related_medical_articles` field to the botanical record with the ZIM internal link.

**Phase 3d: Integration Build and Full Validation (July 1–4)**

Generate the complete Phase 5.2 ZIM combining all five Wave 1–3 modules:
- Full library ZIM: all domains (medical, water, seeds, food, botany) in one file
- Domain-specific ZIMs: separate files per domain for targeted download
- Run zimcheck on all six ZIM files
- Update OPDS catalog to include new domain entries
- Push to Cloudflare R2 CDN

### Resource Allocation

| Task | Hours |
|---|---|
| Botanical importer + tests | 12–16 |
| Integration build + OPDS update | 3–5 |
| CDN push and final zimcheck | 1–2 |
| **Wave 3 total** | **16–23 hours** |

---

## CI/CD Integration

### Test Coverage Requirements

Each new module must meet the following test coverage standards before the wave's feature branch is merged:

| Coverage requirement | Standard |
|---|---|
| Unit test count | Minimum 15 per module (medical: 25, botanical: 30) |
| Branch coverage | >85% for importer classes |
| Safety-critical paths | 100% — every path that writes a `food_safety_table` or `drug_monograph` record must have at least one test |
| Regression suite | All 88 Phase 5.1 tests plus new tests must pass before merge |

### CI Pipeline Integration

Add the following jobs to the existing CI configuration (`.github/workflows/` or equivalent):

```yaml
# New job: phase-5.2-module-tests
- name: Run Phase 5.2 module unit tests
  run: uv run pytest tests/test_medical_importer.py tests/test_water_importer.py tests/test_seed_importer.py tests/test_food_importer.py tests/test_botanical_importer.py -v --tb=short

# New job: zim-integration-test (CI only, requires libzim)
- name: ZIM integration test
  run: uv run pytest tests/integration/test_zim_generation.py -v -m "not slow"
  env:
    LIBZIM_AVAILABLE: "true"
```

The ZIM integration test job is marked as requiring `libzim` to be installed. It runs against a small fixture dataset (5 articles per domain) and validates:
1. ZIM file is generated without exceptions
2. `zimcheck` exits with code 0
3. Article count in the ZIM matches the input fixture count

### Deployment Gates

A feature branch is not merged to `main` until all three deployment gates pass:

**Gate 1: Test suite (automated)**
- Zero failing tests in the full suite
- Zero new linting errors (`ruff check app/ tests/`)
- All safety-critical data validation tests pass explicitly (marked with `@pytest.mark.data_integrity`)

**Gate 2: ZIM validation (automated + manual)**
- `zimcheck` reports 0 errors on the generated test ZIM
- A human has opened the ZIM in Kiwix (Android or Desktop) and confirmed:
  - At least 5 articles render without layout breaks
  - Full-text search returns results for a known query
  - Internal cross-links resolve to correct articles

**Gate 3: Medical accuracy (Wave 1 only, manual)**
- The designated medical reviewer has confirmed that drug dosing tables and procedure protocols are accurate and appropriately caveated
- Disclaimer text has been reviewed and approved
- No dosing table has been modified from the WHO/ICRC source values

Wave 1 is the only wave requiring Gate 3. Waves 2 and 3 require Gates 1 and 2 only.

---

## Beta Testing Plan

### Week-of-July 1 Beta

Before Phase 5.2 ZIM files are pushed to the production CDN, distribute to 3–5 beta users:

**User profile**: Existing Kiwix users who have downloaded Phase 5.1 ZIM content, or users from the systems-resilience / off-grid-living community who have expressed interest in offline medical and botanical reference.

**Beta feedback collection**:
- Provide a structured feedback form (Google Form or plain Markdown template in the repository) covering: article rendering quality, search accuracy, content gaps, any factually incorrect information found
- 7-day beta window (July 1–7)
- One dedicated issue tracker label: `phase-5.2-beta-feedback`

**Acceptance criteria for production release**:
- No factual errors reported in medical or food safety content
- No zimcheck failures in any beta tester's environment
- Article rendering confirmed on at least 2 of 3 platforms (Android, Desktop, kiwix-serve)

---

## Timeline Feasibility Assessment

**Can June 1 – July 4 be met by one developer?**

Yes, under the following conditions:
1. Wave 0 pre-work (schema design, medical review outreach, data sourcing) begins May 22 — this week
2. Phase 5.1 post-merge actions are resolved within the first 3 days of June
3. Developer allocates 2.5–3 hours per working day (excludes weekends): 34 days × 2.5 hours = 85 hours available, against 59–85 estimated
4. Medical reviewer is engaged by May 31 and returns feedback by June 20 — this is the only external dependency

The estimate is tight but achievable. The largest single risk is medical review turnaround. If review feedback arrives after June 20, Wave 1 Medical articles ship as "draft — pending medical review" in the beta, and the final accuracy-reviewed version is released in a July patch. This is a defined fallback, not a failure mode.

**Can one developer handle all three waves in parallel?**

Waves 1–3 are sequential by design — each wave's ZIM validation gate confirms output quality before the next wave builds on it. Within each wave, the two modules (e.g., Medical + Water in Wave 1) are independent and can be worked on in the same day by alternating between them. This is the recommended approach: draft Medical importer in the morning, draft Water importer in the afternoon, test both at end of day. The modules share no code; there is no risk of merge conflict between them when developed on the same branch.

---

## Sources

- Phase 5.2 Priority Matrix — `/projects/open-repo/PHASE_5.2_PRIORITY_MATRIX.md`
- Phase 5.2 Feature Candidates — `/projects/open-repo/PHASE_5.2_FEATURE_CANDIDATES.md`
- Phase 5.2 Capability Audit — `/projects/open-repo/PHASE_5.2_CAPABILITY_AUDIT.md`
- Phase 5.1 Pre-Merge Audit — `/projects/open-repo/phase-5-1-pre-merge-audit-findings.md`
- Phase 5 Architecture — `/projects/open-repo/PHASE_5_ARCHITECTURE.md`
- [WHO Essential Medicines List 23rd edition](https://www.who.int/groups/expert-committee-on-selection-and-use-of-essential-medicines/essential-medicines-lists)
- [USDA Complete Guide to Home Canning (2015 edition)](https://nchfp.uga.edu/publications/usda/USDA_complete_guide_home_canning_2015.pdf)
- [GRIN Germplasm Resources Information Network — bulk data](https://www.ars-grin.gov/grin-global/)
- [openZIM zimcheck documentation](https://github.com/openzim/zim-tools)
- [USDA PLANTS Database bulk download](https://plants.usda.gov/home/downloads)
