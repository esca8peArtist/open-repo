---
title: "Phase 5.2 Wave 0 Water Systems — Preliminary Findings"
project: open-repo
phase: "5.2 Wave 0"
document_type: preliminary-research-synthesis
status: active
created: 2026-07-05
confidence: 85%
word_count: ~3,100
sources_consulted: 25
cross_references:
  - PHASE_5_2_WAVE_0_WATER_SYSTEMS_RESEARCH_OUTLINE.md
  - PHASE_5.2_WATER_CONTENT_SOURCING_CHECKLIST.md
  - PHASE_5.2_WATER_SYSTEMS_CONTENT_OUTLINES.md
  - projects/off-grid-living/03-water.md
  - projects/systems-resilience/individual/01-water.md
---

# Phase 5.2 Wave 0 Water Systems — Preliminary Findings

**Purpose**: Initial synthesis addressing the top research questions for Water Systems Wave 0 content. This document is a working draft of the key facts, procedures, and evidence that will feed directly into publication-ready section text. It is not formatted as a final guide — it is organized by finding type to serve the writer, not the end reader.

**Leading finding**: The technical water treatment methods that are most effective at community scale (boiling, SODIS, biosand filtration) are thoroughly documented by WHO and CDC, and the data is internally consistent across sources. The main gap is not procedural — it is the recontamination problem. Field evidence consistently shows that correctly treated water frequently fails at the storage and handling stage, not the treatment stage. Any publication-ready guide that does not foreground safe storage and recontamination prevention alongside treatment procedures will be incomplete in the way that actually kills people.

---

## Finding 1: Emergency Water Access — What Works, What Fails, and the Real Priority Order

### 1.1 The Standard Quantities

The authoritative baseline figures for emergency water planning are consistent across FEMA, CDC, and WHO:

- **FEMA/Ready.gov baseline**: 1 gallon (3.8 liters) per person per day for survival. This covers approximately 2 quarts for drinking and 2 quarts for food preparation and hygiene. It excludes bathing, laundry, and toilet flushing. [Source: FEMA Food and Water in an Emergency; Ready.gov/water]
- **Realistic livable baseline**: 2 gallons per person per day — the figure most preparedness practitioners use for 2-week self-sufficiency planning. Children, nursing mothers, and individuals in hot climates or with fever require more. [Source: Ready.gov/water; Safecastle preparedness guidance]
- **FEMA preparation target**: At least 2 weeks (14 days) of self-sufficiency. This is updated from the earlier 72-hour recommendation, based on evidence from major disasters showing 72 hours is frequently insufficient for community-level supply restoration. [Source: Ready.gov/water]
- **WHO minimum for sustainable household water use**: 15–20 liters (4–5.3 gallons) per person per day, covering drinking, cooking, and basic sanitation. This is the international development standard, not the emergency standard. [Source: WHO Guidelines for Drinking-Water Quality, 4th ed., 2022]

**Implication for content**: The emergency section (Domain 1, Domain 3) should lead with the 1-gallon/day survival figure and clarify immediately that this is inadequate for sustained health. The 2-gallon/day figure is the 2-week planning number. The WHO 15–20 liter figure frames the longer-term infrastructure goal.

### 1.2 Sources Available Before Any Preparation

Before external water is required, a household already has significant water stores:

| Source | Approximate Volume | Treatment Required |
|--------|-------------------|--------------------|
| Water heater tank | 30–80 gallons | None if tank is clean and undisturbed |
| Toilet tank (not bowl) | 1–3 gallons each | None |
| Ice in freezer | Variable | Melt; no treatment |
| Canned goods liquid | Variable | None |
| Water pipes (drained from lowest faucet after shutoff) | 5–15 gallons | None |
| Bathtub (filled immediately on warning) | 50–100 gallons | None (if filled before supply disruption) |
| WaterBOB bathtub bladder ($30, pre-purchased) | 100 gallons | None if sealed |

**Critical note from internal source (systems-resilience/individual/01-water.md)**: The action to take on any warning of supply disruption is to fill every available container immediately — bathtubs, pots, buckets, trash cans lined with clean trash bags. This is more valuable than any other emergency preparation action because it costs nothing and buys 24–72 hours of supply independence.

### 1.3 The Priority Stack for Emergency Water Access

Based on sources across CDC, FEMA, internal documents, and WHO, the correct prioritization is:

1. **Inventory on-hand water** (toilet tanks, water heater, ice, pipes) — zero cost, zero lead time
2. **Treated stored water from pre-positioned containers** — requires advance preparation
3. **Rainwater collection from available catchment** — available in 1–7 days depending on rain; treat before drinking
4. **Known clean groundwater sources** (neighbor with tested well, community spring) — if accessible and verified
5. **Surface water (stream, pond, lake)** — requires full treatment chain; available immediately but treatment takes time

The practical error in most emergency guides is treating all five of these as equal-effort options. Category 1 is free and requires zero setup. Categories 4 and 5 require correct treatment, which is where life-safety risk concentrates.

---

## Finding 2: Water Testing and Treatment Viability — The Evidence Base

### 2.1 Boiling: What the Evidence Actually Says

Boiling is the most universally endorsed treatment method across WHO, CDC, and field studies. The key findings:

**Effectiveness**: Boiling at a rolling boil for 1 minute at sea level kills all known waterborne pathogens: bacteria, viruses, and protozoa including Cryptosporidium and Giardia — the two protozoan cysts that chemical disinfection alone cannot reliably kill. [Source: WHO GDWQ 4th ed., Chapter 9; CDC Water Treatment Guidance]

**Altitude adjustment**: At altitudes above 6,500 feet (2,000 m), boiling point drops enough that 1-minute boil is insufficient. CDC recommends 3 minutes above 6,500 feet. This is a hard rule that must appear in any boiling procedure. [Source: CDC Water Treatment Guidance, elevation note; off-grid-living/03-water.md]

**What boiling does NOT do**: Boiling does not remove chemical contaminants — pesticides, nitrates, heavy metals, PFAS compounds, or petroleum products. In agricultural regions, a water source with high nitrate contamination (above 10 mg/L MCL) is not made safe by boiling; nitrate concentration actually increases slightly as water volume reduces. [Source: EPA NPDWR; internal systems-resilience/individual/01-water.md, Midwest agricultural warning]

**The recontamination problem**: A 2010 study of rural Guatemala boiling practices found that while boiling reduced thermotolerant coliforms by 86.2%, only 71.2% of stored boiled water samples met WHO zero-TTC standards — because water was recontaminated after boiling through unhygienic handling, non-clean storage containers, or contaminated ladles. [Source: PMC/pmc.ncbi.nlm.nih.gov/articles/PMC2829912/] This finding is critical: treatment effectiveness in the lab and treatment effectiveness in actual household use are different numbers, and the gap is almost entirely in post-treatment handling.

**Content implication**: Every boiling procedure section must include post-treatment handling as part of the procedure, not as a separate optional section. Clean storage container, clean hands, covered storage, no-dip dispensing. This is as important as the boiling time itself.

### 2.2 Chemical Disinfection: Chlorination Specifics

Chlorination is the second-line treatment method, suitable when fuel for boiling is unavailable. The key facts for content writing:

**Standard dose for clear water** (turbidity <1 NTU): 8 drops of regular unscented 6% sodium hypochlorite bleach per gallon of water (approximately 0.75 mL per gallon). Contact time: 30 minutes before drinking. [Source: CDC Water Treatment Guidance; WHO GDWQ 4th ed.]

**Dose for cloudy water** (turbidity 1–10 NTU): Double the dose (16 drops per gallon). Contact time: 60 minutes. [Source: CDC Water Treatment Guidance]

**Dose for turbidity >10 NTU**: Chlorination alone is insufficient. Pre-filtration (cloth, sand) is required to reduce turbidity before chlorination can be effective. This is the most common field error — chlorinating visibly cloudy water and assuming it is safe. [Source: WHO GDWQ 4th ed., Chapter 9; off-grid-living/03-water.md]

**Common bleach concentrations require dose adjustment**:
- 6% sodium hypochlorite (standard unscented bleach): 8 drops/gallon clear water
- 8.25% sodium hypochlorite (concentrated bleach, increasingly common in US): 6 drops/gallon
- Calcium hypochlorite (pool shock, 68–78%): 1/8 teaspoon per 5 gallons (much smaller quantity due to high concentration)
[Source: CDC Water Treatment Guidance; off-grid-living/03-water.md]

**What chlorination does NOT kill**: Cryptosporidium parvum oocysts are resistant to standard chlorine concentrations at typical contact times. Water suspected of Cryptosporidium contamination (after flooding, surface water in areas with cattle) requires boiling or UV treatment, not chlorination alone. [Source: WHO GDWQ 4th ed.; CDC Water Treatment Guidance]

**Contact time and temperature**: Colder water (<15°C) requires longer contact time. At 15–20°C, 30-minute contact time is standard. Below 10°C, extend contact time to 60 minutes. This is documented in WHO guidelines and is frequently omitted from simplified emergency guides. [Source: WHO GDWQ 4th ed., treatment methods chapter]

**Content implication**: The chlorination procedure must include a dose adjustment table (covering both bleach concentrations and turbidity levels) and must explicitly note the Cryptosporidium limitation and temperature adjustment. These omissions in simplified guides create false safety.

### 2.3 SODIS (Solar Disinfection): When It Works and When It Fails

SODIS is the primary low-fuel treatment option in high-UV environments. The evidence base is extensive:

**Core procedure**: Fill clear PET plastic bottles (1.5–2 liter) with water. Shake to aerate. Place on corrugated metal roof or reflective surface in direct sunlight. Exposure time: 6 hours on sunny or partly cloudy days (>50% of day with sun). 48 hours minimum on fully overcast days. [Source: SODIS Reference Center, Eawag; WHO GDWQ 4th ed., Chapter 9]

**Turbidity threshold**: 30 NTU is the maximum turbidity for SODIS to be effective. Above 30 NTU, UV penetration is insufficient to inactivate pathogens throughout the bottle volume. This threshold is the most critical operational parameter. [Source: SODIS Eawag; Frontiers in Water, 2025; PubMed 19570059]

**Effectiveness data from field studies**:
- At low turbidity (16 NTU): 99.7% pathogen removal [Source: Frontiers in Water 2025]
- E. coli: consistent inactivation at standard exposure times in clear water [Source: SODIS Eawag field validation data]
- Cryptosporidium parvum: SODIS achieves inactivation in clear water at standard UV dose but requires longer exposure or pre-filtration in turbid water [Source: PubMed 19570059, field study with Cryptosporidium in PET bottles under full sunlight]
- Field studies in Ethiopia (Tigray region) confirmed: daily UV dose accumulated in high-altitude Africa is sufficient to achieve bacterial contamination removal at standard SODIS exposure times [Source: PMC9640691]

**Critical limitations**:
- Requires clear plastic PET bottles — glass blocks UV; colored plastic blocks UV. Only clear PET works. Bottles must be in good condition; scratches reduce UV penetration.
- Not effective for chemical contamination.
- Reduced effectiveness in consistently overcast climates (Pacific Northwest, northern Europe, similar low-UV zones).
- Requires pre-filtration if turbidity exceeds 30 NTU.

**Content implication**: SODIS is a genuine option for tropical, semi-arid, and high-UV temperate contexts. It is less reliable for Zone 5 Midwest cloudy winters but effective in summer months. The guide should include a seasonal/climate applicability note and a turbidity pre-check procedure.

### 2.4 Biosand Filtration: The Honest Evidence

Biosand filters are the most frequently recommended low-cost community-scale treatment device. The evidence is more nuanced than most guides acknowledge:

**Best-case performance** (well-designed, properly maintained):
- 97% E. coli reduction (Ghana RCT) [Source: PMC3524599]
- 87.9–98.5% bacterial reduction in field conditions (Somalia case study) [Source: Research Square rs-7668141]
- 60% reduction in diarrheal disease incidence in household RCT [Source: PMC3524599]
- 85% turbidity reduction [Source: Research Square rs-7668141]

**Long-term performance** (7-year field data from Rwanda):
- 92.9% of filters still in use at 7 years
- Only 64.3% functioning well at 7 years
- 50% of effluent samples positive for fecal coliforms at 7 years
[Source: IWA Publishing, seven-year biosand filter performance study, doi: 10.2166/washdev.2023.119]

**What this means for communities**: Biosand filters work well when properly maintained. They degrade significantly without maintenance. The 7-year Rwanda data showing 50% fecal coliform detection in effluent represents the most important caution for any community implementing biosand at scale — the filter that worked in year 1 may not be protecting users in year 7 without visible signs of failure.

**Field-realistic performance** (Nicaragua, 199 households):
- Median bacterial removal efficiency: 80%
- Reduced CFUs in 74% of households
- Reduced to <10 CFU/100mL in only 17% of households
[Source: PubMed 20795755]

**Content implication**: Biosand filters should be presented with honest performance ranges — best-case (~97%), field-realistic (~80%), and long-term without maintenance (~50% fecal detection). This framing allows communities to make informed decisions about whether to rely on biosand as primary treatment or as pre-treatment before boiling or chlorination.

---

## Finding 3: Storage Feasibility and Cost Models

### 3.1 Rainwater Harvesting Feasibility by Context

The core yield calculation is simple and consistent across all sources:

**US/Imperial formula**: Annual yield (gallons) = Annual rainfall (inches) × Catchment area (sq ft) × 0.623

The 0.623 factor accounts for evaporation losses, gutter spillage, and first-flush diversion. [Source: Texas A&M AgriLife Extension; NRCS Rainwater Harvesting Technical Note]

**Key feasibility thresholds based on internal source analysis and the sample section worked example**:

| Annual Rainfall | Catchment Size | Annual Yield | Household Drinking Use (4 people) | Viable? |
|----------------|----------------|-------------|----------------------------------|---------|
| 40 inches | 1,200 sq ft | ~29,900 gal | ~2,920 gal | Yes — surplus; can support garden |
| 30 inches | 1,500 sq ft | ~28,000 gal | ~2,920 gal | Yes — surplus; can support garden + toilet |
| 20 inches | 1,500 sq ft | ~18,700 gal | ~2,920 gal | Yes for drinking; limited for garden |
| 15 inches | 1,000 sq ft | ~9,345 gal | ~2,920 gal | Marginal; supplement only in dry months |
| 12 inches | 500 sq ft | ~3,738 gal | ~2,920 gal | Insufficient for drinking + any other use |

**Critical climate nuance from NCA5 (Zone 5 Midwest)**: Annual rainfall averages are deceptive. Zone 5 receives approximately 35–40% of annual precipitation as winter snow. Summer months — July and August — deliver only 5–7 inches combined, which is far below peak demand for garden irrigation and livestock. Tank sizing must bridge this summer deficit, not match the annual average. [Source: NCA5 Chapter 24; systems-resilience/PHASE_5_WATER_SYSTEMS_RESEARCH_OUTLINE.md]

### 3.2 Tank Types and Costs

Cost data from internal sources (off-grid-living/03-water.md) and the sample section, verified against current market data:

| Tank Type | Volume | Cost Range | Lifespan | Installation Complexity |
|-----------|--------|-----------|----------|------------------------|
| Plastic (polyethylene) above-ground | 500–10,000 gal | $0.50–1.00/gal | 15–30 years | Low (level ground, no excavation) |
| Metal (galvanized) above-ground | 500–5,000 gal | $0.75–1.50/gal | 20–40 years | Low-moderate |
| Concrete above-ground | 1,000–10,000+ gal | $0.30–0.75/gal | 40–50+ years | Moderate (requires foundation) |
| Underground plastic cistern | 500–5,000 gal | $1.50–3.00/gal all-in | 30–50 years | High (requires excavation) |
| IBC tote (used, food-grade) | 275–330 gal | $50–100 each | 3–5 years | Very low |
| 55-gallon food-grade drum | 55 gal | $20–30 each | 10–15 years | Very low |

**Critical DIY note on IBC totes**: IBC totes are suitable for short-term or backup storage, but their 3–5 year lifespan makes them a provisional solution. They are excellent for household rainwater testing before committing to a permanent tank. IBC totes must be food-grade (white/translucent plastic, not chemical-storage units). [Source: water-systems-domain-sample-section.md; off-grid-living/03-water.md]

### 3.3 Legal Landscape for Rainwater Harvesting

**Key finding**: As of 2026, rainwater harvesting is legal in all 50 US states. However, 19 states maintain restrictions on volume, use type, or permitting requirements. The trend is toward increased permissibility — states that restricted collection (notably Colorado) have relaxed rules.

**Most restrictive states**:
- **Colorado**: Limited to 110 gallons per day from roof; may not collect from ground; potable use restrictions
- **Utah**: Registration required for systems above a certain size threshold; use restrictions in some watersheds
- **Nevada**: Permits required for systems above a volume threshold; prior appropriation water rights doctrine applies

**Most permissive states (good case studies for content)**:
- **Texas**: Fully legal; no permit required for household systems; encouraged for stormwater management; financial incentives in some counties
- **Arizona**: No restrictions on residential collection; widely practiced
- **Florida**: Encouraged for stormwater reduction; no permit required

**Implication for content**: The Domain 2 legal section should open with the headline that collection is legal everywhere, then explain the variation, and provide specific guidance for the three most common restriction types: volume limits, potable-use restrictions, and registration/permit requirements. [Source: NCSL Map Monday; World Water Reserve state-by-state guide 2026; water-systems-domain-sample-section.md state table]

---

## Finding 4: Technical Requirements vs. Community Capacity

### 4.1 What Works at Household Scale Without Expert Help

These procedures are within the realistic capability of a motivated adult with no prior water systems experience, based on the evidence and the existing sample section content:

| Procedure | Skill Required | Typical Time | Minimum Cost |
|-----------|---------------|-------------|-------------|
| Emergency household inventory (water heater, toilet tanks) | None | 30 minutes | $0 |
| Boiling water treatment | Basic (stove/fire, timer) | 1 hour setup; ongoing | $0 (fuel only) |
| Chlorine disinfection with bleach | Basic (measuring, mixing) | 45 minutes | <$5 |
| Simple cloth prefiltration | None | 15 minutes | $0 |
| Rainwater collection from downspout to barrel | Basic carpentry | 4–8 hours | $50–200 |
| IBC tote setup for rainwater storage | Basic (hose fittings) | 2–4 hours | $100–200 |
| SODIS in PET bottles | None | 15 minutes setup; 6 hours sun | $0 |
| Simple sand filter from 5-gallon bucket | None | 1–2 hours | $15–30 |
| Field water testing with commercial kit | Basic (follow instructions) | 30–60 minutes per test | $15–50 per kit |

### 4.2 What Requires Professional Help or Significant Skill

These procedures are beyond realistic DIY scope and require either professional installation or significant prior experience:

- Well drilling and casing (any depth greater than 25–30 feet) — requires licensed well driller
- Pressure system installation for household plumbing integration
- Septic system design and installation — requires licensed septic designer and installer
- Large cistern construction (concrete, underground) — requires excavation and structural knowledge
- Greywater permit compliance in restricted jurisdictions — requires consultation with local authority

**Content implication**: Each domain section should explicitly flag the DIY/professional boundary. The purpose is not to discourage readers but to prevent harm from misapplied DIY procedures. A failed septic installation creates contamination risk for neighbors. A failed large cistern can create structural failure risk. The sections covering these procedures should lead with the boundary and then provide enough information for readers to evaluate their options and have productive conversations with contractors. [Source: PHASE_5.2_WATER_SYSTEMS_CONTENT_OUTLINES.md, implementation notes]

---

## Finding 5: Regulatory Landscape and Compliance Decision Tree

### 5.1 Regulatory Framework by Domain

Water systems touch four distinct regulatory bodies, and the interaction between them is the most common source of compliance confusion:

| Domain | Regulatory Body | Type of Regulation | Permit Required? |
|--------|----------------|-------------------|-----------------|
| Water treatment (household) | None at household scale in most US jurisdictions | Safety standards apply (EPA MCLs) but not to private wells | No (private well) |
| Rainwater harvesting | State water rights board; local zoning | Volume limits; use restrictions; system registration | Varies by state (see above) |
| Greywater reuse | State plumbing code; county health department | System design standards; setback requirements; use restrictions | Often yes in restricted states |
| Septic / blackwater | County health department; state environmental agency | System design approval; setback requirements; professional installation | Always required |

**EPA MCLs apply to public water systems** (serving 25 or more people 60 or more days per year), not to private household wells. A private well owner is not legally required to test or treat their well water, though it is strongly advisable. This is a common point of confusion in emergency preparedness content.

### 5.2 Urban vs. Rural vs. Mixed Implementation Decision Tree

The correct approach to water systems differs substantially by context. This decision tree maps to the four domains:

**Urban, on municipal water supply**:
- Primary risk: Short-term supply disruption (storm, pipe failure, contamination event)
- Best response: Pre-positioned stored water (14-day supply); emergency treatment capability
- Domains of primary relevance: Domain 1 (testing after contamination event); Domain 3 (short-term treatment)
- Domain 2 relevance: Supplemental (toilet flushing, garden); may require permits for collection

**Suburban, on municipal water supply with yard/roof catchment**:
- Primary risk: Extended supply disruption; summer water restrictions
- Best response: Rainwater collection for non-potable use; stored water for potable emergency
- Domains of primary relevance: Domain 2 (rainwater collection); Domain 3 (treatment for potable use if needed); Domain 4 (greywater to reduce potable demand)
- Key regulatory point: Verify state and county rules before installation

**Rural, on private well**:
- Primary risk: Well pump failure (power outage, pump breakdown); drought-driven water table decline; agricultural contamination
- Best response: Hand pump backup for power outages; rainwater catchment for drought; regular testing for contamination
- Domains of primary relevance: Domain 1 (water testing — critical for private well users); Domain 2 (rainwater backup); Domain 3 (treatment if well tests positive or suspected)
- Key regulatory point: Private well users have no mandatory testing requirement — but the absence of regulation does not mean the absence of risk. Agricultural runoff (nitrates, atrazine) and septic contamination are the most common private well failure modes in US rural areas.

**Off-grid, no existing water supply**:
- Primary situation: Starting from scratch; rainwater and/or groundwater are primary sources
- Best response: Site-specific assessment of groundwater depth and quality; rainwater catchment sized for primary use; full treatment chain for all water
- Domains of primary relevance: All four domains; off-grid-living/03-water.md is the primary reference for this context
- Key regulatory point: Off-grid systems that serve a single household fall outside most regulatory requirements, but building permit requirements may apply to cisterns, especially in urban-adjacent counties

---

## Section 6: Integration Points with Other Domains

### 6.1 Food Security Domain

Water quality for food production does not require potable treatment. Irrigation water can be untreated surface water unless there is specific pathogen risk (flooding, upstream sewage). Water used for washing produce that will be eaten raw should be potable quality. Water for cooking should be potable. [Source: WHO GDWQ 4th ed.; CDC food safety guidance]

**Integration note**: Rainwater collection systems sized for garden irrigation should be presented as a different scale of system from potable-use systems. A 500-gallon tank for garden irrigation is designed for a different demand profile than a 500-gallon tank for household potable backup.

### 6.2 Healthcare Domain

At minimum, wound irrigation water should be treated to at least chemical disinfection quality (chlorinated) — potable quality is preferred but not always available. Medical procedures requiring sterile water (wound care, medical equipment rinsing) need boiled water with clean covered storage, not just filtered water. [Source: WHO GDWQ 4th ed.; CDC WASH guidance]

**PFAS note for healthcare connection**: EPA's 2024 PFAS MCL regulation (PFOA/PFOS at 4.0 parts per trillion) established for the first time that PFAS contamination of public water supplies is a regulated violation. Private wells in areas with known PFAS contamination (near airports, military bases, industrial facilities) cannot be made safe by boiling or standard filtration — only reverse osmosis or granular activated carbon designed for PFAS removal is effective. This creates a healthcare crossover: communities near these PFAS sources need professional lab testing, not field treatment. [Source: EPA PFAS NPDWR, 2024]

### 6.3 Energy Domain

Water pumping is the primary water-energy intersection:
- A submersible electric well pump requires continuous power. In a grid outage, it fails completely.
- A solar-powered pump can maintain well access during grid outages if properly sized.
- A hand pump (e.g., Simple Pump or Baker pump) maintains well access indefinitely with no power.
- A gravity-fed system from an elevated rainwater tank requires no pumping energy at all.

**Integration note**: The energy domain should reference these water pumping configurations. The water domain should specify which configurations require power, which are power-independent, and what the transition procedure is from electric to manual when power is unavailable.

---

## Evidence Gaps and Confidence Notes

### Gaps Requiring Additional Research

**Commercial test kit accuracy data** (Research questions 2, 13): The performance specifications for commonly available commercial field test kits (Aquachek, 3M Clean-Trace, H2O test strips) are documented in manufacturer specifications but are not consistently validated in peer-reviewed field studies. Confidence in the "field-realistic" accuracy of these kits is moderate. Additional research needed: search PubMed for "field water testing kit accuracy" or "coliform test kit validation" before writing Domain 1 Section 4.

**Activated charcoal DIY production** (Research question 42): The procedures for making and activating charcoal from local materials are well-documented in historical literature and permaculture resources but are not extensively validated in peer-reviewed sources for pathogen or organic contaminant removal at household scale. Confidence in this section is low without additional source validation. Recommended approach: include the procedure with a clear caveat about limited evidence compared to commercial activated carbon.

**Greywater legal status completeness** (Research question 46): The NCSL map and World Water Reserve guide provide good coverage of state-level rainwater harvesting rules but are less comprehensive on greywater-specific regulations. The 10 most populous states need individually verified greywater legal status before Domain 4 content is written.

**Constructed wetland plant species by US region** (Research question 52): The general design specifications for constructed wetlands are documented in EPA guidance, but regional plant species lists (which native species perform best as wetland treatment plants in Zone 3 vs. Zone 8) require additional research through Missouri Botanical Garden or similar botanical sources.

### Confidence Assessment by Domain

| Domain | Confidence | Primary Uncertainty |
|--------|-----------|-------------------|
| 1: Water Assessment & Testing | 82% | Commercial kit accuracy; DIY pH test precision; field contamination detection limits |
| 2: Rainwater Harvesting & Storage | 88% | State-by-state legal detail completeness; tropical climate sizing specifics |
| 3: Water Treatment & Purification | 90% | Strong evidence base; main uncertainty is SODIS performance in specific US climate zones |
| 4: Wastewater & Greywater Systems | 75% | Regulatory complexity; greywater state-by-state detail incomplete; professional knowledge verification needed |
| Overall | 85% | Consistent with Wave 0 preliminary phase; confidence builds through full research execution |

---

## Numbered Sources (Selected for This Document)

1. CDC. "How to Create an Emergency Water Supply." https://www.cdc.gov/water-emergency/about/how-to-create-and-store-an-emergency-water-supply.html
2. Ready.gov / FEMA. "Water." https://www.ready.gov/water
3. FEMA. "Food and Water in an Emergency." https://www.fema.gov/pdf/library/f&web.pdf
4. WHO. "Guidelines for Drinking-Water Quality, 4th Edition." Geneva, 2022. https://www.who.int/publications/i/item/9789240045064 (NCBI Bookshelf: https://www.ncbi.nlm.nih.gov/books/NBK579461/)
5. WHO. "Treatment Methods and Performance." GDWQ 4th ed. Chapter, NCBI Bookshelf. https://www.ncbi.nlm.nih.gov/books/NBK579455/
6. CDC. "Water Treatment." https://www.cdc.gov/healthywater/drinking/index.html
7. EPA. "National Primary Drinking Water Regulations." https://www.epa.gov/ground-water-and-drinking-water/national-primary-drinking-water-regulations
8. EPA. "PFAS National Primary Drinking Water Regulation." Federal Register, April 26, 2024. https://www.epa.gov/sdwa/proposed-pfoa-and-pfos-compliance-extension-rule
9. SODIS Reference Center, Eawag. "SODIS Method: Application." https://www.sodis.ch/methode/anwendung/index_EN
10. Ubomba-Jaswa E., et al. "Efficacy of Solar Water Disinfection (SODIS) in Turbid Waters." PubMed 19570059. https://pubmed.ncbi.nlm.nih.gov/19570059/
11. Frontiers in Water. "Potential of Solar Water Disinfection (SODIS) for Pathogen Control During Water Scarcity Crisis." 2025. https://www.frontiersin.org/journals/water/articles/10.3389/frwa.2025.1679793/full
12. IWA Publishing. "Effectiveness of Solar Disinfection for Household Water Treatment." https://iwaponline.com/washdev/article/11/3/374/80556/
13. PMC. "SODIS in Large-Volume Containers, Tigray Ethiopia." https://pmc.ncbi.nlm.nih.gov/articles/PMC9640691/
14. IWA Publishing. "Seven-Year Performance of Biosand Filters in Rural Rwanda." https://iwaponline.com/washdev/article/13/5/333/94658/
15. PMC. "Evaluation of the Impact of the Plastic BioSand Filter, Rural Tamale, Ghana." https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3524599/
16. Research Square. "Efficacy and Sustainable Adoption of BioSand Filters, Borama Somalia." https://www.researchsquare.com/article/rs-7668141/v1
17. RRH Rural and Remote Health. "BioSand Filters in the Artibonite Valley of Haiti." https://www.rrh.org.au/journal/article/570/
18. PubMed. "Assessment of Biosand Filter Performance in Nicaragua." https://pubmed.ncbi.nlm.nih.gov/20795755/
19. PMC. "Microbiological Effectiveness of Disinfecting Water by Boiling in Rural Guatemala." https://pmc.ncbi.nlm.nih.gov/articles/PMC2829912/
20. PMC. "Effect of Household Water Treatment with Chlorine, Dire Dawa Ethiopia." https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7278122/
21. NCSL. "Is Catching Rainwater Legal in Your State?" https://www.ncsl.org/resources/map-monday-is-catching-rainwater-legal-in-your-state
22. World Water Reserve. "Rainwater Collection Laws by State (2026)." https://worldwaterreserve.com/is-it-illegal-to-collect-rainwater/
23. Texas A&M AgriLife Extension. "Rainwater Harvesting for Texas." https://aggie-horticulture.tamu.edu/
24. NCA5. "Fifth National Climate Assessment, Chapter 24: Midwest." https://nca2023.globalchange.gov/
25. EESI. "Amidst Climate Impacts, Rural Water Systems Rely on Federal Programs." https://www.eesi.org/articles/view/amidst-climate-impacts-rural-water-systems-need-federal-programs
26. GAO. "Water Infrastructure Resilience: Agencies Could Better Assess Efforts." GAO-25-107013, 2025. https://www.gao.gov/products/gao-25-107013

---

*Prepared 2026-07-05. Preliminary phase; confidence 85%. Full research execution (9.5–10 hours per research outline timeline) will close the documented evidence gaps and bring Domain 3 and Domain 2 to publication readiness first, followed by Domains 1 and 4.*
