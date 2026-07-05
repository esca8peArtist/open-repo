---
title: "Open-Repo Wave 2 Content Strategy"
project: open-repo
phase: "5.2 Wave 2"
document_type: strategy
status: ready-for-execution
date: 2026-07-05
author: "Open-Repo Research Agent"
confidence: 88%
word_count: ~2800
---

# Open-Repo Wave 2 Content Strategy

**Purpose**: Domain selection, scope, and execution plan for Wave 2 content development. Intended for rapid execution post-July-11 GitHub Pages deployment gate.

**Context**: Wave 0+1 complete as of July 5, 2026. Six domains covered: medical reference (schema + sourcing framework), water systems (assessment/testing, rainwater harvesting, boiling/heat treatment, chemical disinfection, filtration/biosand, wastewater/greywater), seed preservation (community-building stage), food preservation (water bath canning, pressure canning, lacto-fermentation, dehydration), botanical knowledge (schema ready, content deferred), and composting/soil amendment (hot composting, cold composting, vermicomposting, soil application). Estimated corpus: 59,078 words across ~8 production documents.

**What Wave 2 is not**: Wave 2 does not write more water or food preservation content beyond the deferred Wave 1 items. Wave 2 is a horizontal expansion to new knowledge domains. Deferred Wave 1 items (bokashi fermentation, root cellaring, smoking/curing, pressure canning for meat) are picked up in Wave 2 Domain 1 as an extension, not as a separate domain.

**Confidence level**: 88%. Domain gap analysis draws on open-source content landscape research, Wave 0+1 domain selection frameworks, and deferred candidate inventories. Content volume estimates are informed estimates based on comparable extension-literature corpora, not empirical measurement.

---

## Executive Summary — Four Wave 2 Domains

| Domain | Priority | Estimated Words | Schema Status | Safety Gate |
|---|---|---|---|---|
| Natural Building Techniques | 1 | 12,000–15,000 | New schema needed | None (permit-scope-bounded) |
| Small-Scale Livestock Management | 2 | 14,000–18,000 | New schema needed | None (no licensed-professional requirement) |
| Sanitation and Hygiene Systems | 3 | 8,000–10,000 | Extends water_systems schema | None (extends existing scope) |
| Herbal Medicine and Medicinal Plants | 4 | 10,000–13,000 | Extends botanical_knowledge schema | Expert review recommended for preparation guides |

**Total Wave 2 estimated corpus**: 44,000–56,000 words across four domains.

**What is deliberately excluded from Wave 2**:
- Medical reference (requires reviewer recruitment gate not yet closed; planned for Wave 3 post-reviewer onboarding)
- Foraging/wild edibles identification (lookalike toxicity risk; requires identified domain expert; previously deferred from Wave 1 for this reason)
- Energy systems (off-grid solar, wind) — high complexity, jurisdiction-dependent electrical codes, best served by dedicated Phase 6 partnership with Open Source Ecology GVCS documentation

---

## Domain 1: Natural Building Techniques

### Philosophy

This domain fills a gap that is directly adjacent to the composting and seed preservation content already live: if someone is building a homestead or community resilience infrastructure, they need to build or repair structures. Natural building (cob, earthbag, strawbale, timber frame basics) is among the most openly documented construction knowledge sets in the world. Open Source Ecology, One Community Global, and Strawbale Studio have released schematics and plans under open licenses. The key scoping constraint from Wave 1 applies here: content covers structures that do not require local building permits in most US rural and international jurisdictions (under 200 sq ft, non-habitable, accessory structures), plus general principles that apply regardless of jurisdiction.

### Sub-topics

1. **Cob construction** — wall building, mix ratios (clay-sand-straw), testing (shake test, squeeze test), coursing and drying rates, cob repair. Source: One Community Global Engineering Hub (open-licensed), Cob Research Institute publications.

2. **Earthbag construction** — bag selection and filling, barbed wire tensioning between courses, foundation drainage, dome and vault geometry. Source: UNHCR earthbag shelter manuals (open access), One Community Global earthbag village plans.

3. **Strawbale construction** — bale selection and moisture testing, load-bearing vs. infill configurations, pinning, plastering (lime and earthen), window and door framing. Source: Open Source Ecology strawbale house plans (open-licensed), Strawbale Studio documentation.

4. **Compressed earth block (CEB)** — soil selection (plasticity tests), block pressing procedures (manual and motorized), curing and stacking, mortar options. Source: Open Source Ecology CEB press documentation (open-licensed GVCS), UNHCR emergency shelter protocols.

5. **Repair and maintenance** — crack assessment and triage for earthen structures, repointing, weatherproofing, emergency tarping, water damage remediation.

### Estimated Scope

12,000–15,000 words. Each sub-topic covers: materials selection with sourcing guidance, step-by-step construction procedure, structural performance parameters (load ratings, R-values where applicable), tool list, troubleshooting table, and cross-links to relevant water and composting content (earthen structures integrate with water harvesting systems).

### Primary Open Sources

- [Open Source Ecology GVCS Documentation](https://opensourceecology.dozuki.com/c/Global_Village_Construction_Set) — open-licensed, CEB press + strawbale house plans
- [One Community Global Engineering Hub](https://onecommunityglobal.org/cob-village-engineering/) — county-approved cob plans, open-share license
- UNHCR Emergency Shelter publications — earthbag shelter protocols, publicly available
- Natural Building Blog (naturalbuildingblog.com) — aggregates CC-licensed practitioner knowledge
- Cob Research Institute at Oregon State University — peer-reviewed testing data on cob structural performance

### Example Content Pieces

1. "Cob wall construction: mix ratios, slump tests, and coursing schedule for a 12-inch earthen wall"
2. "Earthbag dome geometry: calculating bag count and course height for a 14-foot diameter dome"
3. "Strawbale moisture testing: four field tests and pass/fail thresholds before plastering"
4. "Compressed earth block soil selection: the ribbon test, ball test, and plasticity index requirement"
5. "Cob crack assessment: distinguishing structural from shrinkage cracks and repair protocols for each"
6. "Window and door bucks in strawbale construction: framing, attachment, and plaster transition"
7. "Lime plaster over earthen wall: scratch coat, brown coat, and finish coat schedule"

### Interdependencies with Wave 0+1

- Water domain: earthen structures integrate with cisterns and rainwater capture systems covered in Wave 0 Domain 2 (rainwater harvesting and storage). Cross-links between cistern sizing and earthbag foundation waterproofing.
- Composting domain: building with local materials requires on-site soil assessment; composting content introduces soil biology that informs clay content evaluation for cob mixes.
- Seed preservation: seed storage in earthen structures requires humidity management; this domain covers wall breathability relevant to storage conditions.

### Schema Update Required

New `natural_building` schema extending the existing `procedure` type. Fields: `structure_type` (cob | earthbag | strawbale | ceb | hybrid), `permit_jurisdiction_note` (boolean flag indicating permit research required), `structural_load_rating` (optional), `thermal_performance` (R-value or qualitative), `tool_list`, `material_sourcing` (local vs. purchased), `climate_zone_applicability`.

---

## Domain 2: Small-Scale Livestock Management

### Philosophy

Livestock are the animal-agriculture complement to the plant-based food production coverage already in open-repo. Wave 0+1 covers seeds, composting, and food preservation — all plant-centric. A self-sufficient household or small community also needs protein and draft animal capacity, which requires livestock knowledge. The Wave 1 selection document explicitly deferred this domain with the note "Content depth requires species-specific sections (chickens, goats, rabbits). Adequate for Wave 2." The FAO's "Small Animals for Small Farms" and extension literature from UMD, Purdue, and ATTRA (National Sustainable Agriculture Information Service) provide the open-source foundation.

### Sub-topics

1. **Backyard poultry (chickens)** — breed selection for climate and purpose (laying vs. dual-purpose), brooding (chick setup, temperature schedule), coop design (space requirements, ventilation, predator protection), feeding (commercial feed vs. forage supplementation), egg production management, common health issues (mites, respiratory illness, egg-binding), slaughter and processing basics.

2. **Dairy and meat goats** — breed overview (Nubian, LaMancha, Nigerian Dwarf, Boer), housing and fencing (minimum standards, electrified vs. woven wire), feeding (hay, browse, mineral supplementation), kidding (signs of labor, assisted delivery basics, colostrum management), milk handling (pasteurization options, storage), health basics (FAMACHA scoring for barber pole worm, hoof trimming, common vaccines).

3. **Meat rabbits** — breed overview (New Zealand, California, Rex), hutch construction (wire gauge, cage size, doe/buck separation), feeding (pellets + hay + greens), breeding cycle (kindling signs, nest box prep, weaning), processing (humane dispatch, skinning, butchering for fryers).

4. **Integrated livestock-garden systems** — manure management and composting (extension of Wave 1 composting domain), rotational grazing as ground preparation, chicken tractors for pest management, goat browse management in food forests.

5. **Basic animal health and triage** — vital signs by species, wound cleaning and bandaging in the field, signs of dehydration, when to call a veterinarian (indicators that exceed field-care scope), medication storage and basic drug guide (dewormers, vitamins, electrolytes — sourced from FAMACHA and extension veterinary guidance, not original medical advice).

### Estimated Scope

14,000–18,000 words. Each species section follows a consistent template: setup and equipment, feeding guide (with tables), reproductive cycle summary, health maintenance calendar, common problems + triage table, slaughter/processing basics (where applicable). The integrated systems section is 2,000–3,000 words connecting livestock output to composting and garden systems.

### Primary Open Sources

- [FAO "Small Animals for Small Farms"](https://www.fao.org/4/i2469e/i2469e00.pdf) — publicly available, FAO open license
- ATTRA (National Sustainable Agriculture Information Service) — practical guides on pasture poultry, goat health, rabbit production; government-funded, freely available
- [USDA Guide for Organic Livestock Producers](https://www.ams.usda.gov/sites/default/files/media/GuideForOrganicLivestockProducers.pdf) — USDA public domain
- University of Maryland Extension Beginning Farmer Livestock Manual — extension literature, freely available
- FAO Farmer Field Schools for Small-Scale Livestock Producers — open-access, field-tested curriculum
- FAMACHA system documentation (Barber pole worm management in small ruminants) — publicly available from American Consortium for Small Ruminant Parasite Control

### Example Content Pieces

1. "Backyard chicken brooder setup: temperature schedule days 1–56 and common failure modes"
2. "Chicken coop ventilation: calculating square footage of ventilation per bird for hot and cold climates"
3. "Goat FAMACHA scoring: the 5-point eye-membrane scale and deworming thresholds"
4. "Rabbit kindling: nest box preparation, monitoring the doe, and managing kit mortality in the first 72 hours"
5. "Integrated chicken tractor: pasture rotation schedule and ground preparation yield for vegetable beds"
6. "Goat hoof trimming: tools, angle targets, and white line disease identification"
7. "Small ruminant vital signs: normal ranges for temperature, pulse, respiration by species and age"
8. "Manure management: comparing nitrogen content and composting requirements for chicken, goat, and rabbit manure"

### Interdependencies with Wave 0+1

- Composting (Wave 1): Livestock manure is high-nitrogen (green) compost feedstock. Direct cross-link from composting C:N ratio tables to per-species manure nitrogen content. Livestock section references composting procedures for manure management.
- Food preservation (Wave 1): Meat processing from rabbits and chickens connects to the food safety principles in the pressure canning section. Rendered lard storage references food preservation principles.
- Water systems (Wave 0): Animal waterers and livestock water quality; cross-reference to water testing procedures for animal health contexts.
- Seed preservation: Chicken tractors in seed production plots require sequencing with seed saving — animals must be excluded from seed plants during pollination windows.

### Schema Update Required

New `livestock` schema. Fields: `species` (chicken | goat | rabbit | duck | bee | other), `purpose` (dairy | meat | eggs | dual-purpose | draft), `scale` (backyard | small-farm | homestead), `climate_zone_notes`, `housing_requirements` (minimum sq ft per animal), `feeding_guide` (structured object with feeds, quantities, schedule), `health_calendar` (array of seasonal tasks), `regulatory_note` (flag for slaughter/processing legal requirements by jurisdiction).

---

## Domain 3: Sanitation and Hygiene Systems

### Philosophy

The water systems content in Wave 0 covers water sourcing, testing, treatment, and greywater management. Sanitation is the complement: what happens to human waste and solid waste in the absence of municipal infrastructure. This is not a distinct new domain — it directly extends the water systems schema and is positioned as the missing half of the WASH (Water, Sanitation, Hygiene) framework that Wave 0 began. The CAWST (Centre for Affordable Water and Sanitation Technology) and WHO have extensive open-licensed practical guides on latrine construction and hygiene promotion.

### Sub-topics

1. **Pit latrines** — site selection (distance from water sources, groundwater depth), pit sizing (volume calculation for household size and emptying frequency), slab construction (ferro-cement vs. concrete), superstructure basics, ventilation pipes for odor and fly management, pit lining options.

2. **Composting toilets** — thermophilic vs. cold composting toilet designs, carbon cover material, two-chamber alternating systems, pathogen die-off requirements (time + temperature), humanure safety and agricultural use.

3. **Handwashing facilities** — tippy-tap construction (sub-1-hour build, no tools required), leaky-tin and bottle trap designs, soap alternatives (ash, plant-based), WHO five-moment hand hygiene protocol adapted for field context.

4. **Solid waste and refuse management** — reduce/reuse/compost priority hierarchy, burn barrel construction and safe operation, burial pit (medical waste vs. general), vermin-proofing food waste storage (connection to composting domain).

5. **Hygiene in field emergencies** — body waste management for groups in transit or temporary camps (cat-hole latrines, field decontamination), menstrual hygiene management in resource-limited settings, disease prevention during diarrheal outbreaks (oral rehydration salts formula, safe water sourcing for sick individuals).

### Estimated Scope

8,000–10,000 words. This is the lightest of the four Wave 2 domains — not because the topic is unimportant but because the technical procedures are fewer and less variable than natural building or livestock. The content is high-density and practical, with construction diagrams described in text (waiting for image/schematic upload capability).

### Primary Open Sources

- CAWST (cawst.org) — WASH in humanitarian settings, latrine construction modules, freely available
- [WaterAid Technical Guide for Handwashing Facilities](https://washmatters.wateraid.org/sites/g/files/jkxoof256/files/2024-10/Technical-guide-handwashing-facilities-public-places-2024.pdf) — publicly available
- WHO/UNICEF WASH guidelines — public access
- Open University OpenLearn module on latrine construction (open.edu/openlearncreate) — Creative Commons licensed
- The Humanure Handbook by Joseph Jenkins — 4th edition available free from the author at humanurehandbook.com (author's explicit permission for non-commercial distribution)
- UNHCR Emergency Shelter and WASH technical guidelines — open access

### Example Content Pieces

1. "Pit latrine siting: minimum distances from wells, rivers, property boundaries"
2. "Ferro-cement latrine slab: materials list, mixing ratios, reinforcement layout, and curing schedule"
3. "Ventilated improved pit (VIP) latrine: fly trap mechanism, screen selection, and maintenance"
4. "Tippy-tap construction: step-by-step for a 5-liter nail-activated handwashing station"
5. "Two-chamber composting toilet: alternating chamber schedule, cover material guide, and compost safety assessment"
6. "Oral rehydration salts: WHO formula (1 liter water + 6 level teaspoons sugar + 0.5 teaspoon salt) and administration protocol"
7. "Cat-hole latrine protocol: depth, distance from camp, soil replacement, and group sanitation for travel"

### Interdependencies with Wave 0+1

- Water systems (Wave 0): Directly extends the greywater and wastewater domain (Wave 0 Domain 4). Sanitation siting criteria reference groundwater protection from water assessment content (Domain 1). Handwashing connects to water treatment for handwashing water quality.
- Medical reference (future Wave 3): Oral rehydration salts and diarrheal disease management in Section 5 of this domain creates a natural cross-link to the future medical domain.
- Composting (Wave 1): Composting toilet and humanure content directly extends the composting procedures already documented. Identical biology; different feedstock. References to thermophilic requirements in the hot composting section apply.

### Schema Update Required

No new schema required. Content fits within the existing `water_systems` schema with an added `sanitation_subtype` field (pit_latrine | composting_toilet | handwashing | solid_waste | emergency_hygiene). Consider adding a `construction_materials` structured field and `regulatory_note` for jurisdictions where composting toilets require permits.

---

## Domain 4: Herbal Medicine and Medicinal Plants

### Philosophy

This domain sits at the intersection of the botanical knowledge schema (already built) and the medical domain (deferred pending reviewer recruitment). Herbal medicine occupies a distinct tier: it does not require licensed physician sign-off for the core content (preparation methods, traditional uses, safety contraindications from WHO monographs) but does require more care than composting or food preservation. The scope boundary is: preparation guides for widely documented medicinal plants sourced from WHO Monographs on Selected Medicinal Plants and Herbalista's CC BY-SA 4.0 content. Dosing and treatment claims are not made — the guide presents traditional use and preparation methods with sourcing, explicitly stating that this is not medical advice and that symptoms requiring diagnosis should be evaluated by a licensed provider.

This domain directly activates the botanical_knowledge schema that has been in standby since Wave 0.

### Sub-topics

1. **Foundational preparation methods** — infusions and teas (cold vs. hot infusion, steep time, water temperature by plant part), decoctions (root and bark extraction, simmering times), tinctures (menstruum selection, folk method ratios, straining, storage), poultices and compresses, salves and infused oils (double boiler and cold-infusion methods), drying and storage of plant material.

2. **Wound care and skin plants** — plantain (Plantago major/lanceolata), calendula, yarrow, comfrey (for bruises and closed wounds only — hepatotoxicity note for internal use). Each plant: identification notes (morphological, not full field-guide), preparation methods, documented actions, contraindications from WHO or Commission E monographs.

3. **Digestive support plants** — ginger (nausea, digestive motility), peppermint (IBS, nausea), chamomile (spasm, anxiety-adjacent effects), fennel (gas, bloating). Documentation structure same as wound care section.

4. **Respiratory support plants** — elderberry (antiviral evidence review: moderate quality RCT evidence for duration reduction), thyme (expectorant, antispasmodic), mullein (demulcent for dry cough). Same documentation structure.

5. **Growing and harvesting medicinal plants** — which of the above grow in temperate climates from seed, harvest timing by plant part (leaf vs. flower vs. root), drying conditions and storage requirements, seed saving for perennial medicinals. Cross-links to seed preservation domain.

### Estimated Scope

10,000–13,000 words. Section 1 (preparation methods) is the largest at ~3,000 words because it is referenced by all subsequent sections. Each plant entry in Sections 2–4 runs 400–600 words covering identification, preparation, documented actions, dosage range from literature, contraindications, and drug interactions (where documented). Approximately 12–15 plant profiles across the three topic sections.

### Primary Open Sources

- [WHO Monographs on Selected Medicinal Plants](https://www.who.int/publications/i/item/9789241545228) — 4 volumes, publicly available, authoritative
- Herbalista (herbalista.org) — CC BY-SA 4.0 license, community health herbalism focus
- NCCIH (National Center for Complementary and Integrative Health) "Herbs at a Glance" — US government, public domain
- Commission E Monographs (German regulatory authority) — widely cited in secondary literature; primary texts in German with English translations available through American Botanical Council
- University of Maryland Medical Center herbal medicine reference — historical web archive available
- Bastyr University herbal monograph database — academic institution, educational use

### Expert Review Status

This domain is below the medical reviewer gate required for medical reference content, but a review by someone with herbal medicine training (clinical herbalist, naturopathic physician, or pharmacist with botanical medicine background) would increase confidence from 80% to 92%+ on preparation guides and contraindication sections. This should be treated as a Wave 2 improvement pass target (initial content at 80% confidence, reviewer-validated content at 92%+), not a hard gate that blocks publication.

### Example Content Pieces

1. "Cold infusion vs. hot infusion: which plant constituents survive which temperatures, and why"
2. "Folk method tincture: menstruum ratios, maceration time, and straining protocol for 10 common medicinals"
3. "Plantain poultice: identification (ribbed parallel veins, seed head), preparation for insect stings and minor wounds"
4. "Yarrow first aid: styptic application for minor bleeding, wound wash preparation, contraindications (pregnancy)"
5. "Elderberry syrup: berry selection, preparation (must cook to deactivate sambunigrin), sweetener ratios, storage"
6. "Ginger for nausea: fresh vs. dried preparations, dosage range from clinical literature, contraindications for anticoagulant medications"
7. "Medicinal herb drying: temperature limits, humidity targets, and storage containers for 5 common species"

### Interdependencies with Wave 0+1

- Botanical knowledge (schema): Directly activates the botanical_knowledge schema that has been waiting since Wave 0. The plant profiles in this domain are the first production content for that schema.
- Seed preservation: Growing medicinal plants from seed; seed saving for perennial herbals. Cross-link to seed drying and storage from seed preservation content.
- Medical reference (future Wave 3): Drug interaction notes and contraindications in this domain create natural handoff points to the more comprehensive medical reference domain planned for Wave 3.
- Composting: Growing conditions and soil amendment for medicinal herb gardens reference the compost application section from Wave 1.

### Schema Update Required

Extends the `botanical_knowledge` schema with new fields: `medicinal_uses` (array of documented uses with source citations), `preparation_methods` (array of method objects), `contraindications` (array with severity level), `drug_interactions` (array), `harvest_season`, `plant_part_used`, `safety_classification` (GRAS | WHO-approved | traditional-use-only | safety-uncertain). Safety classification is required for every medicinal plant entry.

---

## Execution Timeline

**Pre-condition**: GitHub Pages deployment live by July 11, 2026 (user gate).

### Phase 1: Schema Development (July 11–18, 1 week)

Two new schemas must be written and published to `docs/schemas/` before content development begins:

- `natural_building.schema.json` — based on field specifications above
- `livestock.schema.json` — based on field specifications above
- `water_systems.schema.json` update — add `sanitation_subtype` field (non-breaking addition)
- `botanical_knowledge.schema.json` update — add medicinal fields listed above

Estimated time: 6–10 hours of schema authoring + validation.

### Phase 2: Domain 3 Content (July 18–25, 1 week)

Sanitation and hygiene is the fastest domain (8,000–10,000 words, no new schema, directly extends existing water systems framework). Publish first as it completes Wave 0's WASH coverage and cross-links to existing water content immediately.

Research → Draft → Review → Publish cycle: 10–14 hours of writing time, 1–2 hours of source verification per section.

### Phase 3: Domains 1, 2, and 4 Content (July 25 – August 22, 4 weeks)

All three remaining domains can be researched and drafted in parallel if multiple sessions are available. Sequential single-session approach:

- Week 1 (July 25 – August 1): Natural building research and draft (12,000–15,000 words)
- Week 2 (August 1–8): Small-scale livestock research and draft (14,000–18,000 words)
- Week 3 (August 8–15): Herbal medicine research and draft (10,000–13,000 words)
- Week 4 (August 15–22): Review pass, cross-linking, schema validation, publication

### Total Execution Time

- Schema work: 8–12 hours
- Sanitation/hygiene writing: 12–16 hours
- Natural building writing: 16–20 hours
- Livestock writing: 18–24 hours
- Herbal medicine writing: 14–18 hours
- Review, cross-linking, publication: 8–12 hours

**Total estimated hours**: 76–102 hours of content development across 6–7 weeks.

If sessions are constrained to 2–3 hours each, this translates to approximately 30–45 sessions. If sessions average 3 hours each with focused research-first protocols, the timeline compresses to 6 weeks (July 11 – August 22).

### Parallel Acceleration Option

Domains 1, 2, and 4 have no content dependencies on each other. They can be assigned to parallel research agents without state conflict. The only sequencing constraint is: schemas must be complete before any schema-dependent content is published. Domain 3 (sanitation) can begin immediately after schema update because it uses an existing schema field addition only.

---

## Distribution Integration

### How Wave 2 Integrates with GitHub Pages

Wave 2 content follows the same folder structure established in Wave 1:

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
└── wave-2-herbal-medicine/
    ├── index.md
    └── herbal-medicine-complete-guide.md
```

New schemas are published to `docs/schemas/` alongside the five existing schemas.

### ZIM File Update

After Wave 2 content is live, a new ZIM file is generated covering all Wave 0+1+2 content (~100,000+ words at completion). This ZIM file is submitted to the OPDS catalog and announced on the Kiwix third-party library submission thread.

### Cross-Linking Priority

The highest-value cross-links to establish at Wave 2 publication:

1. Natural building → Water harvesting (cistern-to-earthen-wall integration)
2. Livestock → Composting (manure as feedstock, C:N ratios)
3. Sanitation → Water systems (greywater domain, handwashing water quality)
4. Herbal medicine → Botanical knowledge schema (plant profile pages)
5. Herbal medicine → Seed preservation (growing medicinal herbs from seed)

---

## Sources

- [Open Source Ecology GVCS Documentation](https://opensourceecology.dozuki.com/c/Global_Village_Construction_Set)
- [One Community Global Cob Village Engineering Hub](https://onecommunityglobal.org/cob-village-engineering/)
- [FAO Small Animals for Small Farms (PDF)](https://www.fao.org/4/i2469e/i2469e00.pdf)
- [USDA Guide for Organic Livestock Producers (PDF)](https://www.ams.usda.gov/sites/default/files/media/GuideForOrganicLivestockProducers.pdf)
- [WaterAid Technical Guide for Handwashing Facilities (PDF)](https://washmatters.wateraid.org/sites/g/files/jkxoof256/files/2024-10/Technical-guide-handwashing-facilities-public-places-2024.pdf)
- [CAWST WASH Resources](https://washresources.cawst.org/en/topics/a2d19a80/sanitation)
- [WHO Monographs on Selected Medicinal Plants](https://www.who.int/publications/i/item/9789241545228)
- [Herbalista Open Source Herbalism Resources](https://herbalista.org/resources-detail-page/) — CC BY-SA 4.0
- [MSF Medical Guidelines](https://medicalguidelines.msf.org/en/home-page) — field reference standard
- [Open Source Ecology Strawbale House Plans](https://www.opensourceecology.org/open-source-manual-ceb-press-and-open-source-prefab-strawbale-house/)
- [Free Open Source Strawbale House Design — Natural Building Blog](https://naturalbuildingblog.com/free-open-source-strawbale-house-design/)
- [FAO Farmer Field Schools for Small-Scale Livestock Producers](https://resources.peopleinneed.net/documents/357-fao-2018-farmer-field-schools-for-small-scale-livestock-producers.pdf)

---

*Prepared 2026-07-05. Ready for execution post-July-11 GitHub Pages deployment gate. Confidence: 88%.*
