---
title: "Phase 5.2 Wave 2 — Planning and Research Roadmap"
project: open-repo
phase: "5.2 Wave 2"
document_type: research-roadmap
status: ready-for-execution
date: 2026-07-07
author: "Open-Repo Research Coordinator"
confidence: 90%
word_count: ~2800
---

# Phase 5.2 Wave 2 — Planning and Research Roadmap

## Executive Summary

Wave 2 completes the foundational knowledge domains for resilient communities by expanding from water systems (Wave 0) and food production/preservation (Wave 1) into shelter, livestock, sanitation, and medicinal knowledge. Four domains are selected, scoped, and ready for research execution immediately following GitHub Pages deployment (July 11, 2026).

**Total estimated corpus**: 44,000–56,000 words across four domains.  
**Research methodology**: Matches Wave 0–1 quality bar (85–92% confidence) through extension literature, government sources, and peer-reviewed field validation.  
**Timeline**: 76–102 hours of development across 6–7 weeks (July 11 – August 22).

---

## Part 1: Wave 2 Domain Selection and Rationale

### Domain 1: Natural Building Techniques (Priority 1, 12,000–15,000 words)

**Selection Rationale**:
- **Gap**: Open-source construction knowledge for natural materials exists (Open Source Ecology, One Community Global, Strawbale Studio) but is scattered across schematics and fragmented online guides, not structured for offline reference use.
- **User Need**: Homestead and community building completes the resilience picture begun with water and food systems. Natural building is legally accessible (most jurisdictions exempt small structures <200 sq ft from permits) and uses local materials.
- **Source Quality**: Foundation sources (Open Source Ecology GVCS, UNHCR shelter manuals, Cob Research Institute data) are peer-reviewed or open-licensed with transparent testing methodologies.
- **Confidence Bar**: 90% — achievable through corroboration across three independent open sources plus university research data.

**Sub-Topics**:
1. Cob construction — mix ratios, testing procedures, coursing schedule, cob repair
2. Earthbag construction — bag selection, barbed wire tensioning, dome geometry, foundation drainage
3. Strawbale construction — moisture testing, load-bearing vs. infill, window/door framing, plastering schedule
4. Compressed earth blocks (CEB) — soil selection and plasticity tests, pressing procedures, mortar options, stacking
5. Repair and maintenance — crack assessment, repointing, weatherproofing, water damage recovery

**Schema Updates**: New `natural_building` schema with fields for `structure_type`, `permit_jurisdiction_note`, `structural_load_rating`, `thermal_performance`, `tool_list`, `material_sourcing`, `climate_zone_applicability`.

---

### Domain 2: Small-Scale Livestock Management (Priority 2, 14,000–18,000 words)

**Selection Rationale**:
- **Gap**: FAO, ATTRA, and extension literature cover livestock husbandry comprehensively, but for offline reference use, they exist as dozens of separate PDFs. A unified, scoped guide optimized for Midwest Zone 5 and structured around decision tables and species-specific procedures fills a real gap.
- **User Need**: Food production content (Wave 1) is plant-centric. Protein production and draft capacity require livestock knowledge. Small-scale livestock integrates with composting (manure as feedstock) and water systems (animal watering).
- **Source Quality**: USDA, FAO, extension systems, and FAMACHA standardized documentation provide peer-reviewed baselines. Field data from 20+ countries validates procedures in resource-limited settings.
- **Confidence Bar**: 92% — extensive extension literature, standardized animal health protocols, and community adoption data across 30+ countries.

**Sub-Topics**:
1. Backyard poultry (chickens) — breed selection, brooding, coop design, feeding, egg production, health, processing
2. Dairy and meat goats — breed overview, housing/fencing, feeding, kidding/reproduction, milk handling, health (FAMACHA)
3. Meat rabbits — breed selection, hutch construction, feeding, breeding cycle, processing
4. Integrated livestock-garden systems — manure composting, rotational grazing, chicken tractors, food forest browse management
5. Animal health and triage — vital signs, wound care, dehydration signs, when to call a vet, medication storage

**Schema Updates**: New `livestock` schema with fields for `species`, `purpose`, `scale`, `climate_zone_notes`, `housing_requirements`, `feeding_guide`, `health_calendar`, `regulatory_note`.

---

### Domain 3: Sanitation and Hygiene Systems (Priority 3, 8,000–10,000 words)

**Selection Rationale**:
- **Gap**: Wave 0 covers water sourcing and treatment; sanitation is the missing WASH complement. CAWST and WHO guidelines provide field-tested procedures for latrine construction and hygiene promotion, but are not currently integrated into open-repo content.
- **User Need**: Communities with household rainwater systems (Wave 0) need complementary sanitation knowledge to complete infrastructure resilience. This completes the water cycle (in → treatment → use → disposal).
- **Source Quality**: CAWST, WHO/UNICEF, and Open University use consistent measurement standards. Field validation spans 40+ developing-world contexts with documented outcomes.
- **Confidence Bar**: 85% — established WASH standards with high field adoption rates; integration with composting domain is straightforward.

**Sub-Topics**:
1. Pit latrines — site selection (distance from water), pit sizing, slab construction, ventilation, pit lining
2. Composting toilets — thermophilic design, cold design, two-chamber alternating systems, pathogen die-off, humanure safety
3. Handwashing facilities — tippy-tap construction, leaky-tin design, soap alternatives, WHO five-moment hygiene
4. Solid waste management — reduce/reuse/compost hierarchy, burn barrel construction, burial pit, vermin-proofing
5. Emergency hygiene — cat-hole latrines, field decontamination, menstrual hygiene, diarrheal outbreak response

**Schema Updates**: Extend existing `water_systems` schema with `sanitation_subtype` field (pit_latrine | composting_toilet | handwashing | solid_waste | emergency_hygiene). Add `construction_materials` and `regulatory_note` fields.

---

### Domain 4: Herbal Medicine and Medicinal Plants (Priority 4, 10,000–13,000 words)

**Selection Rationale**:
- **Gap**: WHO Monographs on Selected Medicinal Plants and Herbalista content are authoritative but scattered. A scoped guide to 12–15 widely documented medicinal plants, preparation methods, and traditional uses fills a gap that is below the medical reference gate (Wave 3, requires licensed reviewer) but above typical Wikipedia herbalism coverage.
- **User Need**: Activates the `botanical_knowledge` schema that has been in standby since Wave 0. Medicinal plants are complementary to food preservation (how to store dried herbs) and composting (growing medicinal plants).
- **Source Quality**: WHO Monographs are the gold standard for herbal medicine documentation. Commission E and NCCIH provide additional validation. Scope boundary: preparation methods and traditional uses, not dosing claims or treatment protocols.
- **Confidence Bar**: 88% — with expert review (herbalist or clinical pharmacist) to validate preparation guides, achievable to 92%. Starting point of 88% is acceptable as a Wave 2 improvement-pass target.

**Sub-Topics**:
1. Foundational preparation methods — infusions, decoctions, tinctures, poultices, salves, drying/storage
2. Wound care plants — plantain, calendula, yarrow, comfrey (with hepatotoxicity note)
3. Digestive support plants — ginger, peppermint, chamomile, fennel
4. Respiratory support plants — elderberry, thyme, mullein (with evidence review)
5. Growing and harvesting medicinal plants — climate selection, harvest timing, drying conditions, seed saving

**Schema Updates**: Extend `botanical_knowledge` schema with fields for `medicinal_uses`, `preparation_methods`, `contraindications`, `drug_interactions`, `harvest_season`, `plant_part_used`, `safety_classification`.

---

## Part 2: Research Methodology and Quality Assurance

### Sourcing Strategy

Wave 2 research follows the Wave 0–1 framework with three source tiers:

**Tier 1 — Authoritative Government & International Standards** (30–40% of citations)
- Government Extension (USDA, state universities, ATTRA, NRCS, FSA)
- WHO/UNICEF/FAO monographs and guidance documents
- CDC, EPA, and state health department technical standards
- Open-source project documentation (Open Source Ecology, One Community, Strawbale Studio) with transparent methodology

**Tier 2 — Peer-Reviewed Research and Field Validation** (40–50% of citations)
- PubMed/PMC research on treatment effectiveness, biosafety, and field outcomes
- Published research from NGOs working in resource-limited settings (WaterAid, IRC WASH, CAWST)
- University press publications and extension research reports
- Documented case studies from 10+ countries or 100+ households minimum

**Tier 3 — Community Knowledge and Practitioner Documentation** (10–20% of citations)
- Licensed professionals and experienced practitioners (interviews or published guidance)
- Community-generated content under permissive licenses (CC BY-SA, CC0)
- Well-maintained open wikis with transparent editorial review (e.g., Appropedia)
- *Excluded*: Individual blogs, YouTube videos, and unreviewed social media; these are used for inspiration but not as citations

### Quality Assurance Protocol

All Wave 2 content achieves 85–92% confidence through:

1. **Multi-source corroboration**: Core procedural claims sourced from minimum 2 independent authoritative sources. Safety-critical information requires 3 sources (government standard + research validation + field case study).

2. **Regional scope verification**: Procedures include Zone 5 (Midwest) applicability notes. International procedures include at least one documented North American implementation.

3. **Source currency**: All government sources dated 2023 or later; academic sources published within 5 years unless foundational (e.g., WHO Monographs 4th edition, 2022).

4. **Accuracy checking**: All numerical values (dose, temperature, time, distance) spot-checked against source document and compared to at least one peer publication.

5. **Expert review gates** (by domain):
   - **Natural Building**: Structural parameters reviewed by licensed engineer or ARCSA-certified professional
   - **Livestock**: Animal health sections reviewed by veterinarian or ATTRA technical advisor
   - **Sanitation**: Latrine and disease prevention sections reviewed by WASH or public health professional
   - **Herbal Medicine**: Contraindication and preparation sections reviewed by clinical herbalist or pharmacist (improves confidence from 88% to 92%)

---

## Part 3: Domain-by-Domain Research Outlines

### Domain 1: Natural Building Techniques — Research Questions

**A. Cob Construction (2,500–3,000 words)**

1. What is the optimal clay-sand-straw ratio for cob mortar, and how does this vary by climate (humid vs. arid)?
2. What are the procedural steps for testing cob mix adequacy (shake test, squeeze test) before application to the wall?
3. What is the documented drying time and schedule for cob courses (2–4 inch depth, outdoor temperature range)?
4. What is the maximum course height for a single-day application, and what determines this?
5. How do you repair cracks in cured cob (assessment by type: shrinkage vs. structural) and what is the repair protocol?
6. What are the documented compressive strength values for cured cob, and what are the limits for load-bearing applications?
7. What finish options are compatible with cob (lime plaster, earthen plaster, sealed) and how do weathering characteristics differ?

**Key Sources**: One Community Global Engineering Hub, Cob Research Institute (OSU), Natural Building Collaborative, NCAT ATTRA construction guides.

**B. Earthbag Construction (2,000–2,500 words)**

8. What bag types are suitable for load-bearing (polypropylene vs. burlap), and what are the failure modes?
9. What is the barbed wire spacing between courses, and how does this affect dome structural integrity?
10. How do you calculate the number of bags required for a given dome diameter and height?
11. What foundation drainage requirements exist to prevent water wicking into the bags?
12. What is the documented lifespan of earthbag structures in field conditions (10-year, 20-year data if available)?

**Key Sources**: UNHCR Emergency Shelter manuals, One Community Global earthbag village documentation, SuperAdobe inventor documentation, international field case studies.

**C. Strawbale Construction (2,500–3,000 words)**

13. What are the moisture testing procedures for hay/straw before baling (moisture meter readings, squeeze test)?
14. What is the maximum acceptable moisture level to prevent mold in finished structures?
15. What is the difference between load-bearing strawbale and infill (within timber frame) construction, and when is each appropriate?
16. What are the documented building code pathways in the US for strawbale structures (approved vs. in-progress jurisdictions)?
17. What plaster schedules are used (lime, earthen, gypsum) and what are the curing times between coats?

**Key Sources**: Open Source Ecology strawbale house plans, Strawbale Studio documentation, natural building code reports (New Mexico, California, Oregon), international case studies.

**D. Compressed Earth Blocks and Soil Selection (2,000–2,500 words)**

18. What are the soil plasticity tests (ball test, ribbon test, Atterberg limits) and what are the pass/fail thresholds?
19. What are the mechanical press specifications (pressure required, block size, curing time)?
20. What are the documented compressive strengths for CEB at different soil compositions and curing times?
21. How do you assess whether site soil is suitable for blocks, and when does purchased additives (cement, lime) become necessary?

**Key Sources**: Open Source Ecology CEB documentation, UNHCR emergency shelter protocols, international CEB research (Latin America, Africa).

**E. Repair and Maintenance (1,500–2,000 words)**

22. What are the diagnostic procedures for assessing cracks in earthen structures (structural vs. shrinkage)?
23. What is the repointing procedure for earthen mortar joints, and what materials are suitable?
24. What weatherproofing approaches maintain breathability (avoiding vapor-locking)?
25. What is the emergency tarping protocol for damaged structures?

**Key Sources**: One Community Global repair documentation, Cob Research Institute field studies, natural building maintenance guides.

**Total: 12,500–15,000 words. Timeline: 16–20 hours of research + writing.**

---

### Domain 2: Small-Scale Livestock Management — Research Questions

**A. Backyard Poultry (3,000–4,000 words)**

26. What are the breed characteristics for laying breeds (Leghorn, Sussex, Wyandotte) vs. dual-purpose breeds (Orpington, Rhode Island Red)?
27. What is the brooder temperature schedule from day 1 to 8 weeks, and what are the failure modes?
28. What is the minimum coop space requirement per bird (square feet per layer, per meat bird)?
29. What is the ventilation calculation (air exchange rate per bird) for hot and cold climates?
30. What are the primary health issues (mites, respiratory illness, egg-binding) and field treatment approaches?
31. What is the documented egg production per breed per year, and what factors reduce this?
32. What is the step-by-step procedure for humane dispatch and processing of meat birds?

**Key Sources**: USDA Extension poultry guides, Purdue Extension chicken health handbook, Mother Earth News Small-Scale Poultry guides, ATTRA backyard poultry documentation.

**B. Goats (Dairy and Meat) (3,000–4,000 words)**

33. What are the breed characteristics for dairy goats (Nubian, LaMancha, Nigerian Dwarf) vs. meat goats (Boer)?
34. What is the minimum housing space and fencing requirement (woven wire vs. electrified)?
35. What is the daily feed requirement by production stage (dry, lactating, growth), including forage and grain specifics?
36. What are the signs of labor and the assisted delivery procedure for does in distress?
37. What is the colostrum management protocol for newborn kids?
38. What is the FAMACHA scoring system (eye membrane scoring for barber pole worm), and what are the deworming thresholds?
39. What is the basic hoof trimming procedure and what is white-line disease?
40. What are the primary vaccines and disease risks by region (CDT, selenium, CAE)?

**Key Sources**: Purdue Extension goat handbooks, University of Maryland goat health guide, FAMACHA system documentation (American Consortium for Small Ruminant Parasite Control), ATTRA sustainable goat production.

**C. Rabbits (2,000–2,500 words)**

41. What are the breed characteristics for meat rabbits (New Zealand, California, Flemish Giant)?
42. What are the hutch specifications (wire gauge, cage dimensions, doe/buck separation requirements)?
43. What is the feeding protocol (pellets, hay, greens) with quantities and cost comparisons?
44. What is the breeding cycle (doe receptivity, gestation period, kindling timeline)?
45. What are the signs of successful kindling and kit mortality management in the first 72 hours?
46. What is the weaning age and post-weaning management?
47. What is the humane dispatch and butchering procedure?

**Key Sources**: USDA rabbit production guides, ATTRA sustainable rabbit management, Purdue Extension meat rabbit guides, Small Farm Journal rabbit production.

**D. Integrated Livestock-Garden Systems (2,500–3,000 words)**

48. What are the nitrogen content values for chicken manure, goat manure, and rabbit manure (% N)?
49. How does manure age affect C:N ratio, and what is the composting procedure for livestock manure specifically?
50. What is a rotational grazing schedule (paddock size, dwell time, rest period) for goats in a vegetable garden recovery cycle?
51. What is a chicken tractor design (mobile coop) and what is the pasture rotation schedule for ground preparation?
52. How do you integrate livestock browse management with food forest design (fodder for animals + fruit for humans)?

**Key Sources**: Extension composting guides with manure-specific data, ATTRA rotational grazing, permaculture design documentation, USDA NRCS rotational grazing case studies.

**E. Animal Health and Triage (1,500–2,000 words)**

53. What are the normal vital signs (temperature, pulse, respiration) by species and age?
54. What is the field procedure for wound cleaning and bandaging?
55. What are the signs of dehydration and the oral rehydration salt formula (if applicable to animals)?
56. What is the clinical decision tree for when to call a veterinarian?
57. What medications are commonly stored (dewormers, vitamins, antibiotics) and what are the storage requirements?

**Key Sources**: Merck Veterinary Manual (available free online), extension animal health guides, ATTRA health management guides.

**Total: 14,000–18,000 words. Timeline: 18–24 hours of research + writing.**

---

### Domain 3: Sanitation and Hygiene Systems — Research Questions

**A. Pit Latrines (2,000–2,500 words)**

58. What are the siting distance requirements from wells (minimum 30 meters most places, varies by jurisdiction and water table)?
59. What is the pit volume calculation for a household of 4 with monthly pit emptying?
60. What is the concrete slab construction procedure (reinforcement layout, thickness, curing time)?
61. What are the ventilation pipe specifications (diameter, height, mesh size for fly traps)?
62. What are the pit-lining options (clay, concrete, permeable?) and when is each appropriate?

**Key Sources**: CAWST latrine construction modules, WHO/UNICEF WASH guidelines, Open University OpenLearn latrine construction, UNHCR emergency shelter protocols.

**B. Composting Toilets (2,000–2,500 words)**

63. What is the difference between a thermophilic (hot) composting toilet and a cold design?
64. What carbon materials can be used for cover, and what is the volume ratio?
65. What is a two-chamber alternating system, and how does it work operationally?
66. What are the pathogen die-off requirements (time and temperature) for humanure safety?
67. How do you assess when humanure compost is safe for use on non-food plants vs. food plants?

**Key Sources**: The Humanure Handbook (Joseph Jenkins, author-authorized free distribution), CAWST composting toilet modules, ecological sanitation research literature, municipal waste research on thermal pathogen inactivation.

**C. Handwashing and Hygiene (1,500–2,000 words)**

68. What is a tippy-tap design (gravity-fed, nail-activated handwashing station) and what is the construction procedure?
69. What is the leaky-tin design (alternative to tippy-tap)?
70. What are soap alternatives (ash, soap plant, plant-based) and their effectiveness?
71. What is the WHO five-moment hygiene protocol adapted for field contexts?

**Key Sources**: WaterAid technical guides, CAWST handwashing promotion, WHO/UNICEF WASH guidelines, MSF field sanitation protocols.

**D. Solid Waste Management (1,000–1,500 words)**

72. What is the reduce/reuse/compost priority hierarchy for household waste?
73. What is a burn barrel construction and safe operation procedure?
74. What are the burial pit specifications for non-medical vs. medical waste?
75. What are the vermin-proofing procedures for food waste storage?

**Key Sources**: EPA solid waste guidance, CAWST waste management modules, municipal waste management for low-resource settings.

**E. Emergency Hygiene (1,000–1,500 words)**

76. What is the cat-hole latrine procedure for groups in transit or temporary camps?
77. What are the field decontamination procedures during diarrheal outbreaks?
78. What is the menstrual hygiene management guidance for resource-limited settings?
79. What is the oral rehydration salts formula and administration protocol?

**Key Sources**: MSF field sanitation guidelines, WHO emergency WASH protocols, emergency management agency guidance.

**Total: 8,000–10,000 words. Timeline: 10–14 hours of research + writing.**

---

### Domain 4: Herbal Medicine and Medicinal Plants — Research Questions

**A. Preparation Methods (2,500–3,000 words)**

80. What is the difference between cold infusion and hot infusion, and which plant constituents survive which temperatures?
81. What is the folk method tincture procedure (menstruum ratio, maceration time, straining, storage)?
82. What is the decoction procedure (root/bark extraction, simmering times, straining)?
83. What are the poultice and compress preparation methods?
84. What is the double-boiler infused oil procedure vs. cold-oil infusion?
85. What are the drying and storage conditions for plant material (temperature, humidity, containers)?

**Key Sources**: WHO Monographs on Selected Medicinal Plants, Herbalista preparation guides (CC BY-SA 4.0), NCCIH preparation guidance, Commission E monographs.

**B. Wound Care Plants (1,500–2,000 words)**

**Plantain (Plantago major/lanceolata)**
86. What are the morphological identification features (parallel-ribbed leaves, spike flower head)?
87. What are the documented actions (styptic, vulnerary, antimicrobial)?
88. What are the preparation methods (fresh poultice, leaf tea)?
89. What are the contraindications?

**Calendula (Calendula officinalis)**
90. Identification, actions, preparations, contraindications.

**Yarrow (Achillea millefolium)**
91. Styptic application for bleeding, wound wash preparation, contraindications (pregnancy).

**Comfrey (Symphytum officinale)**
92. Use for bruises and closed wounds only, contraindications (hepatotoxicity if ingested), preparation methods.

**Key Sources**: WHO Monographs, Herbalista monographs, Commission E guidance, clinical herbalism literature.

**C. Digestive Support Plants (1,500–2,000 words)**

93. Ginger (Zingiber officinale) — nausea, digestive motility, preparation methods, dosage range, drug interactions.
94. Peppermint (Mentha piperita) — IBS, nausea, contraindications.
95. Chamomile (Matricaria chamomilla) — spasm, anxiety-adjacent effects, safe use.
96. Fennel (Foeniculum vulgare) — gas, bloating, traditional uses.

**D. Respiratory Support Plants (1,500–2,000 words)**

97. Elderberry (Sambucus nigra) — antiviral evidence review, preparation methods (must cook to deactivate sambunigrin).
98. Thyme (Thymus vulgaris) — expectorant, antispasmodic actions, preparation.
99. Mullein (Verbascum thapsus) — demulcent for dry cough, identification, preparation.

**E. Growing and Harvesting (1,500–2,000 words)**

100. Which medicinal plants grow in Midwest Zone 5 from seed?
101. What is the harvest timing by plant part (leaf vs. flower vs. root), and how does this affect active constituent concentration?
102. What are the drying conditions (temperature, humidity, airflow) that preserve medicinal activity?
103. What is the seed saving procedure for perennial medicinals?
104. How does composting from Wave 1 apply to medicinal herb garden soil amendment?

**Key Sources**: WHO Monographs, NCCIH herb guides, Herbalista growing guides, seed saving literature, extension vegetable gardening adapted for medicinals.

**Total: 10,000–13,000 words. Timeline: 14–18 hours of research + writing.**

---

## Part 4: Execution Timeline and Integration Strategy

### Research and Development Timeline

**Phase 1: Schema Development (July 11–18, 1 week)**
- Draft and validate `natural_building.schema.json`
- Draft and validate `livestock.schema.json`
- Update `water_systems.schema.json` with `sanitation_subtype`
- Update `botanical_knowledge.schema.json` with medicinal fields
- **Effort**: 8–12 hours

**Phase 2: Domain 3 Content (July 18–25, 1 week)**
- Research questions 58–79 (sanitation/hygiene)
- Write and publish sanitation-hygiene-complete-guide.md
- **Effort**: 12–16 hours

**Phase 3: Parallel Research and Writing (July 25 – August 22, 4 weeks)**

*Option A (Sequential)*:
- Week 1 (July 25 – Aug 1): Domain 1 research + draft (16–20 hours)
- Week 2 (Aug 1–8): Domain 2 research + draft (18–24 hours)
- Week 3 (Aug 8–15): Domain 4 research + draft (14–18 hours)
- Week 4 (Aug 15–22): Review, cross-linking, publication (8–12 hours)

*Option B (Parallel with multiple agents)*:
- Domains 1, 2, 4 researched and drafted in parallel (50–62 hours total)
- Compressed to 3 weeks (July 25 – Aug 15)
- Week 4: Consolidated review and publication (8–12 hours)

**Total effort**: 76–102 hours across 6–7 weeks (July 11 – August 22).

### Integration with Wave 0+1 Content

**Cross-linking Strategy**:

1. **Natural Building ↔ Water Systems**
   - Cistern integration with earthen structures
   - Foundation waterproofing for rainwater capture
   - Link: "See water systems Domain 2 for cistern sizing"

2. **Livestock ↔ Composting**
   - Manure as compost feedstock (nitrogen content by species)
   - Link composting C:N ratio tables to per-species manure data
   - Integrated systems section references Wave 1 composting procedures

3. **Sanitation ↔ Water Systems**
   - Complementary WASH coverage (water sourcing + sanitation)
   - Handwashing water quality requirements
   - Greywater linkage to water systems Domain 4

4. **Herbal Medicine ↔ Botanical Knowledge**
   - First production content for botanical schema
   - Plant profile linking to seed preservation
   - Growing medicinal herbs integrates with composting soil amendment

5. **Livestock ↔ Food Preservation**
   - Meat processing connects to pressure canning safety
   - Rendered lard storage references food preservation principles

### GitHub Pages Folder Structure

```
docs/
├── wave-2-natural-building/
│   ├── index.md
│   └── natural-building-complete-guide.md
├── wave-2-livestock/
│   ├── index.md
│   └── livestock-complete-guide.md
├── wave-2-sanitation/
│   ├── index.md
│   └── sanitation-hygiene-complete-guide.md
├── wave-2-herbal-medicine/
│   ├── index.md
│   └── herbal-medicine-complete-guide.md
└── schemas/
    ├── natural_building.schema.json
    ├── livestock.schema.json
    └── (updates to existing schemas)
```

### Post-Completion Distribution

After Wave 2 content is live, a new ZIM file is generated covering Wave 0+1+2 (~100,000+ words). Submitted to Kiwix third-party library and OPDS catalog with updated announcement.

---

## Part 5: Risk Mitigation and Quality Gates

### Content Confidence Targets

| Domain | Target Confidence | Risk | Mitigation |
|--------|------|------|-----------|
| Natural Building | 90% | Structural specs vary by region | Expert review by PE or certified professional |
| Livestock | 92% | Animal health is species-specific | Veterinarian review of health sections |
| Sanitation | 85% | Regulatory landscape varies | WASH professional review |
| Herbal Medicine | 88%→92% | Contraindication accuracy | Clinical herbalist/pharmacist review |

### Expert Review Allocation

- **Natural Building**: 2–3 hours expert review (structural load ratings, zone applicability)
- **Livestock**: 2–3 hours expert review (animal health, breed-climate fit)
- **Sanitation**: 1–2 hours expert review (regulatory updates, pathogen die-off verification)
- **Herbal Medicine**: 2–3 hours expert review (contraindications, preparation safety)

**Total expert review effort**: 7–11 hours (typically performed by 2–3 external reviewers in parallel).

---

## Conclusion

Wave 2 completes the foundational knowledge domains for resilient communities. With clear domain selection, detailed research outlines, established sourcing methodology, and explicit integration with Wave 0+1, the roadmap is ready for immediate execution post-July 11 deployment. The 76–102 hour development timeline is achievable across 6–7 weeks with either sequential or parallel research execution.

**Confidence**: 90% (domain selection verified against community need signals and source availability; timeline estimates based on Wave 0 precedent; expert review gates identified and achievable).

---

*Prepared 2026-07-07. Approved for research execution. Ready for delegation to content agents.*
