---
title: "Phase 5.2 Priority Matrix — Impact × Effort Scoring and June 2026 Roadmap"
project: open-repo
phase: "5.2 planning"
status: "pre-merge planning (June 1+ implementation target)"
created: 2026-05-21
author: General Research Agent
depends_on: "PHASE_5.2_FEATURE_CANDIDATES.md, PHASE_5.2_CAPABILITY_AUDIT.md"
---

# Phase 5.2 Priority Matrix

**Purpose**: Assign quantitative scores to all ten Phase 5.2 candidates and produce the recommended June 2026 implementation sequence. This document is the decision-ready output; the detailed rationale for each score is in PHASE_5.2_FEATURE_CANDIDATES.md and PHASE_5.2_CAPABILITY_AUDIT.md.

**Scoring methodology**:
- **Impact** (1–10): Breadth of benefit across active projects + life-safety criticality. 10 = directly saves lives in multiple failure scenarios; 1 = marginal quality improvement.
- **Effort** (1–10): Implementation complexity. 10 = most effort (highest person-hours, new dependencies, design decisions). Low effort = high score advantage in the matrix.
- **Alignment** (1–10): Fit with open-repo mission ("documentation archives for topics critical to human survival and flourishing") and the user's four active related projects (systems-resilience, seedwarden, off-grid-living, cybersecurity-hardening).
- **Composite score**: (Impact × 0.4) + ((10 − Effort) × 0.35) + (Alignment × 0.25). Weights reflect: impact matters most, effort matters nearly as much (lower effort = higher score), alignment is the tiebreaker.

---

## Scoring Table

| # | Candidate | Impact (1–10) | Effort (1–10) | Alignment (1–10) | Composite | Quadrant |
|---|---|---|---|---|---|---|
| 2 | Medical Reference | 9 | 4 | 10 | 9×0.4 + 6×0.35 + 10×0.25 = **3.60+2.10+2.50 = 8.20** | High-Impact / Low-Effort |
| 1 | Botanical Knowledge | 8 | 4 | 9 | 8×0.4 + 6×0.35 + 9×0.25 = **3.20+2.10+2.25 = 7.55** | High-Impact / Low-Effort |
| 9 | Seed Preservation | 8 | 4 | 10 | 8×0.4 + 6×0.35 + 10×0.25 = **3.20+2.10+2.50 = 7.80** | High-Impact / Low-Effort |
| 5 | Food Preservation | 8 | 3 | 8 | 8×0.4 + 7×0.35 + 8×0.25 = **3.20+2.45+2.00 = 7.65** | High-Impact / Low-Effort |
| 3 | Water Systems | 8 | 3 | 9 | 8×0.4 + 7×0.35 + 9×0.25 = **3.20+2.45+2.25 = 7.90** | High-Impact / Low-Effort |
| 6 | Communications | 7 | 3 | 7 | 7×0.4 + 7×0.35 + 7×0.25 = **2.80+2.45+1.75 = 7.00** | High-Impact / Low-Effort |
| 7 | Sanitation | 7 | 2 | 7 | 7×0.4 + 8×0.35 + 7×0.25 = **2.80+2.80+1.75 = 7.35** | High-Impact / Low-Effort |
| 10 | Community Governance | 6 | 3 | 9 | 6×0.4 + 7×0.35 + 9×0.25 = **2.40+2.45+2.25 = 7.10** | Medium-Impact / Low-Effort |
| 4 | Energy Systems | 7 | 7 | 8 | 7×0.4 + 3×0.35 + 8×0.25 = **2.80+1.05+2.00 = 5.85** | High-Impact / High-Effort |
| 8 | Security Protocols | 5 | 2 | 6 | 5×0.4 + 8×0.35 + 6×0.25 = **2.00+2.80+1.50 = 6.30** | Medium-Impact / Low-Effort |

---

## Ranked Priority Order

| Rank | Candidate | Composite Score | Implementation window |
|---|---|---|---|
| 1 | Medical Reference | 8.20 | June 1–7 |
| 2 | Water Systems | 7.90 | June 1–7 (parallel with Medical) |
| 3 | Seed Preservation | 7.80 | June 8–14 |
| 4 | Food Preservation | 7.65 | June 8–14 (parallel with Seed) |
| 5 | Botanical Knowledge | 7.55 | June 15–21 |
| 6 | Sanitation | 7.35 | June 15–21 (parallel with Botanical) |
| 7 | Community Governance | 7.10 | June 22–28 |
| 8 | Communications | 7.00 | June 22–28 (parallel with Governance) |
| 9 | Security Protocols | 6.30 | June stretch / Phase 5.3 |
| 10 | Energy Systems | 5.85 | Phase 5.3 (pvlib dependency warrants dedicated sprint) |

---

## Impact × Effort Quadrant Analysis

### Quadrant 1: High-Impact / Low-Effort (DO FIRST)

These candidates deliver the most life-safety value per hour of implementation work. All source data is available internally or as public-domain downloads. No new Python runtime dependencies required.

**Candidates in this quadrant**: Medical Reference (#2), Water Systems (#3), Food Preservation (#5), Botanical Knowledge (#1), Seed Preservation (#9), Sanitation (#7), Communications (#6)

This is an unusually favorable distribution — seven of ten candidates land here. The reason: the user's active projects have already produced high-quality primary source documents (off-grid-living, systems-resilience, seedwarden). Phase 5.2 is primarily an archival and structuring exercise, not a research exercise. The hard intellectual work is already done.

### Quadrant 2: High-Impact / High-Effort (SCHEDULE CAREFULLY)

**Energy Systems** is the single candidate in this quadrant. Its impact score is high (offline solar sizing is genuinely valuable), but the pvlib dependency, NSRDB data download, and pre-computation architecture introduce meaningful complexity that could consume disproportionate time relative to other candidates. Recommend scheduling this as a standalone Phase 5.3 sprint with a dedicated implementation plan.

### Quadrant 3: Medium-Impact / Low-Effort (FILL-IN CANDIDATES)

**Community Governance** and **Security Protocols** land here. Both are valuable but neither rises to life-critical urgency in the way that medical, water, and food preservation do. Community Governance is the better candidate for June (score 7.10) because it directly archives Phase 5 Wave 2 content from systems-resilience that has already been written. Security Protocols (6.30) is the lowest-priority June candidate — its content policy sensitivity warrants a careful review before publishing in the ZIM format.

### Quadrant 4: Low-Impact / High-Effort

No candidates land in this quadrant. All Phase 5.2 candidates are justifiable.

---

## Recommended Phase 5.2 Priority Order (Top 5 for June 1–30)

### Priority 1: Medical Reference + Water Systems (June 1–10, parallel)

**Why first**: These two candidates address the Rule of 3 survival priorities directly — water kills in 3 days, medical emergencies without care kill within hours. Both have:
- Complete primary source documents already written (off-grid-living 03-water.md, 08-medical-health.md)
- Zero new Python dependencies
- The highest composite scores (8.20 and 7.90 respectively)
- Direct archival need: systems-resilience individual/01-water.md is listed as Priority 1 execution item

**June 1–7 deliverables**:
- `MedicalReferenceArchiver` module: 10–14 person-hours
- `WaterSystemsArchiver` module: 8–12 person-hours
- Both produce new ZIM content type schemas, article templates, and 25–30 unit tests each
- ZIM exports: new `medical` and `water` domain ZIM files pass zimcheck and open in Kiwix

### Priority 2: Seed Preservation + Food Preservation (June 8–17, parallel)

**Why second**: These two candidates serve the seedwarden project directly and address the next survival tier (food production and preservation). Seed Preservation archives irreplaceable heritage variety knowledge. Food Preservation prevents botulism — the key safety-critical data archival task.

**June 8–17 deliverables**:
- `SeedPreservationArchiver` module: 12–16 person-hours
- `FoodPreservationArchiver` module: 8–12 person-hours
- USDA canning time tables embedded in ZIM as authoritative, unmodified lookup tables
- GRIN viability data for 500+ commonly saved species
- 30–40 new unit tests

### Priority 3: Botanical Knowledge (June 18–24)

**Why third**: The botanical module spans the most related projects (seedwarden, systems-resilience midwest/foraging-species.md, off-grid-living skills chapter) and serves both food security and medicine domains. It is slightly more complex than the Wave 1–2 candidates due to USDA PLANTS CSV parsing, but remains low-risk.

**June 18–24 deliverables**:
- `BotanicalArchiver` module: 12–16 person-hours
- 1,000+ species cards (USDA PLANTS subset: food-producing and medicinal plants for US zones 3–8)
- Cross-links between botanical and medical articles (medicinal plants reference their off-grid-living drug monograph equivalents)

---

## Expected Outcomes: June 2026 Phase 5.2

### New Feature Modules (code)

| Module | New content types | New ZIM domains | Lines of new code |
|---|---|---|---|
| `MedicalReferenceArchiver` | `medical_article`, `drug_monograph` | `medicine` | ~450 |
| `WaterSystemsArchiver` | `water_procedure`, `sizing_guide` | `water` (deepened) | ~400 |
| `SeedPreservationArchiver` | `seed_species`, `viability_table` | `seeds` | ~480 |
| `FoodPreservationArchiver` | `preservation_recipe`, `safety_table` | `food` (deepened) | ~450 |
| `BotanicalArchiver` | `botanical_species`, `plant_card` | `botany` | ~560 |
| **Phase 5.2 total** | **10 new content types** | **5 new/deepened domains** | **~2,340 lines** |

### Updated Documentation

- `docs/PHASE_5_USER_GUIDE.md`: extended with new domain descriptions and download links for domain-specific ZIM files
- `docs/CONTENT_DOMAINS.md`: new document listing all 10+ content domains with ZIM download sizes
- Module-level docstrings for all five new importer modules

### Test Coverage

Estimated new tests per module: 20–30 each → **100–150 new unit tests** added to the existing 88-test Phase 5.1 suite

Target: maintain existing standard of 0 failures, all tests passing in < 1 second (stub mode) for the import pipeline unit tests; integration tests with real libzim run in CI only.

### ZIM Archive Size Estimates (post-Phase 5.2, nopic variant)

| ZIM file | Estimated articles | Estimated size (nopic) |
|---|---|---|
| `open-repo_en_medicine_YYYY-MM.zim` | 200–500 | 2–8 MB |
| `open-repo_en_water_YYYY-MM.zim` | 50–150 | 1–3 MB |
| `open-repo_en_seeds_YYYY-MM.zim` | 500–1,500 | 3–10 MB |
| `open-repo_en_food_YYYY-MM.zim` | 200–600 | 2–8 MB |
| `open-repo_en_botany_YYYY-MM.zim` | 1,000–3,000 | 5–15 MB |
| `open-repo_en_nopic_YYYY-MM.zim` (full) | 2,000–6,000 | 15–50 MB |

All estimates are within the Phase 5 architecture targets (full < 500 MB, domain < 50 MB, nopic variant < 80 MB).

---

## Phase 5.3 Candidates (July 2026+)

The following candidates are deferred from Phase 5.2 for specific reasons. They are not abandoned; they are staged for the next sprint.

**Energy Systems (Candidate 4)**: Deferred because pvlib + NSRDB dependency chain warrants a dedicated sprint. Should be Phase 5.3 Wave 1 — implement after Phase 5.2 stabilizes, with a standalone test environment for the pvlib pre-computation pipeline.

**Communications (Candidate 6)**: Composite score is 7.00 — just below the June 30 cutoff. The off-grid-living 11-communications.md source is complete. Recommend adding to Phase 5.3 Wave 1 alongside Energy Systems.

**Sanitation (Candidate 7)**: Composite 7.35 but deprioritized due to lower perceived user engagement despite high public health value. Recommend Phase 5.3 Wave 2.

**Community Governance (Candidate 10)**: Composite 7.10. Systems-resilience Phase 5 Wave 2 documentation is recently written and may still be in flux. Recommend Phase 5.3 Wave 2 after the systems-resilience content stabilizes.

**Security Protocols (Candidate 8)**: Composite 6.30. Requires a content policy review before ZIM publication. Phase 5.3 Wave 3 with explicit scope boundary definition.

---

## Pre-Merge Activation Checklist (Phase 5.1 → Phase 5.2 handoff)

Before starting Phase 5.2 implementation, confirm the Phase 5.1 post-merge action items are resolved. These were identified in the pre-merge audit (phase-5-1-pre-merge-audit-findings.md):

- [ ] **Action 1**: `html.escape()` applied to `source_node_url`/`source_node_name` in attribution footer — required before federated content export activation
- [ ] **Action 2**: `ZimExport` SQLAlchemy ORM class added to `app/models.py` — required before export pipeline wires to database
- [ ] **Action 3**: `libzim>=3.10.0,<4.0` added to `pyproject.toml` and installed — required before real ZIM creation replaces stub
- [ ] **Action 4**: README updated for Phase 5 — documentation accuracy

Phase 5.2 feature modules can be developed on separate feature branches immediately (they do not depend on the stub-to-real ZIM transition), but the full end-to-end ZIM generation test (new articles appearing in a real ZIM file readable in Kiwix) requires Action 3 to be complete.

---

## Decision Gate: What to Approve Now

**Immediate approval needed** (before June 1):

**Approve the Phase 5.2 roadmap**: Three waves, five modules, June 1–30 implementation window, targeting ~80 person-hours of work.

If the roadmap is approved, the first implementation task is:

1. Create branch: `git checkout -b feature/phase-5.2-wave-1`
2. Implement `MedicalReferenceArchiver` and `WaterSystemsArchiver` in parallel (independent modules, same feature branch or two sub-branches)
3. Define the `medical_article` and `water_procedure` content type schemas in `app/models.py` alongside the `ZimExport` ORM class (Action 2 from Phase 5.1)
4. Write ZIM article templates for both new content types
5. Import source content from off-grid-living Markdown files
6. Run 88 existing export pipeline tests + new module tests: verify all pass
7. Generate test ZIM with sample medical and water articles; validate with zimcheck; open in Kiwix Android

**Approval format**:
- "Approved: Phase 5.2 Wave 1 (Medical + Water). Start June 1."
- "Approved: Phase 5.2 full roadmap (all 5 modules). Execute June 1–30."
- "Approved: Adjust priority — start with Seed Preservation instead of Medical."

---

## Sources

- Phase 5.1 pre-merge audit — `/projects/open-repo/phase-5-1-pre-merge-audit-findings.md`
- Phase 5.2 Feature Candidates — `/projects/open-repo/PHASE_5.2_FEATURE_CANDIDATES.md`
- Phase 5.2 Capability Audit — `/projects/open-repo/PHASE_5.2_CAPABILITY_AUDIT.md`
- systems-resilience PLAN.md execution priority table
- off-grid-living master-outline.md domain completion status
- [pvlib-python — Sandia National Laboratories](https://pvlib-python.readthedocs.io/)
- [BioPython 1.87 — biopython.org](https://biopython.org/)
- [openZIM libzim — GitHub](https://github.com/openzim)
- [Meshtastic — meshtastic.org](https://meshtastic.org/)
- [WHO Essential Medicines List](https://www.who.int/groups/expert-committee-on-selection-and-use-of-essential-medicines/essential-medicines-lists)
- [USDA PLANTS Database](https://plants.usda.gov/)
- [OpenFarm archive — GitHub](https://github.com/openfarmcc/OpenFarm)
- [EFF LoRa regulatory update 2025](https://www.eff.org/deeplinks/2025/07/radio-hobbyists-rejoice-good-news-lora-mesh)
