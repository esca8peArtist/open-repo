---
title: "Filtration & Biosand Systems: Slow Sand, Ceramic, and Gravity Filters"
domain: "water-systems"
domain_number: 3
article: "3.3"
section: "filtration-biosand-systems"
content_type: "procedure"
difficulty: "intermediate"
estimated_read_time: "18 minutes"
author: "Open-Repo Project"
last_updated: "2026-07-05"
project: open-repo
phase: "5.2 Wave 0"
status: production-ready
confidence: 88%
license: "CC-BY-4.0"
sources_verified: true
cross_references:
  - "WAVE_0_DOMAIN_3_BOILING_AND_HEAT_TREATMENT.md"
  - "WAVE_0_DOMAIN_3_CHEMICAL_DISINFECTION.md"
  - "projects/systems-resilience/individual/01-water.md"
---

# Filtration & Biosand Systems: Slow Sand, Ceramic, and Gravity Filters

## Overview & Value

Filtration removes particles, reduces turbidity, and — in biological filtration systems — removes or kills pathogens through physical removal and biological action. Unlike boiling or chemical treatment, filtration can treat large volumes of water continuously with minimal fuel or chemical inputs. A well-maintained biosand or slow sand filter can serve a household for years.

Filtration is most important as a pre-treatment stage before disinfection, but biological filters (slow sand, biosand) can also function as primary treatment for biological contamination, achieving pathogen reductions comparable to chlorination when properly maintained.

**Who should read this**: Households or communities planning medium-to-long-term water treatment systems where chemical or fuel costs are a constraint; anyone building off-grid infrastructure; anyone seeking to understand what commercial gravity filters (Berkey, Sawyer, LifeStraw) actually do and what their limits are; anyone considering a biosand filter for a low-resource or humanitarian setting.

**What you'll learn**: How slow sand and biosand filtration works biologically, how to construct a simple biosand filter, what the evidence actually shows about long-term performance (including failure modes), how gravity ceramic filters work, and how to integrate filtration into a complete treatment chain.

**Key decision points**:
- Are you filtering for turbidity reduction only, or do you need biological pathogen removal? (See Section 1)
- Is this a short-term emergency setup or a permanent installation? (Determines which filter type is appropriate)
- What is your flow rate requirement? (See Section 2 decision table)

---

## Section 1: Filtration Types and What Each Removes

Not all filters are the same. The critical distinction is between filters that physically remove particles (including pathogens) and filters that reduce turbidity but do not remove pathogens.

### 1.1 Filter Type Comparison

| Filter Type | Primary Removal | Pathogen Removal? | Flow Rate | Lifespan |
|-------------|----------------|-------------------|-----------|---------|
| Cloth / fabric | Large particles (>100 microns) | No | High | Single use or limited |
| Sand filter (non-biological) | Particles >50 microns, turbidity reduction | No | Moderate | Years if maintained |
| Slow sand / biosand filter | Particles + biological removal via schmutzdecke layer | Yes — E. coli 80–97% | Low (0.1–0.3 L/min) | Years to decades if maintained |
| Ceramic gravity filter | Particles down to 0.3–0.5 microns | Yes — bacteria and protozoa; not viruses | Very low (1–5 L/hr) | 1–2 years per element |
| Commercial microfilter (Sawyer, LifeStraw) | 0.1 micron absolute | Yes — bacteria, protozoa; not viruses | Moderate | 100,000 gallons (Sawyer) |
| Activated carbon | Organic compounds, taste/odor | Partial (some pathogens adsorb) | High | Months |
| Reverse osmosis membrane | Particles, ions, organics, some viruses | Yes — broad spectrum | Very low | Years |

**Critical understanding**: Standard mechanical filters (sand, cloth, ceramic) do not reliably remove viruses. Viruses are 0.02–0.3 microns — smaller than most filter pores. In most US contexts (except crowded urban flooding or water that may carry sewage contamination), viruses are less of a concern than bacteria and protozoa. In international settings or in extreme flood events, combine filtration with chlorination or UV treatment to address viruses. [Sources: 1, 4]

### 1.2 When Filtration Alone Is Sufficient vs. When It Must Be Combined with Disinfection

**Filtration alone may be sufficient when**:
- Source is groundwater with known low biological contamination (tested well in a non-flooded area)
- Purpose is turbidity reduction for a water source that is otherwise safe
- Using a filter with verified virus removal capability (some RO and UF membranes)
- The risk assessment indicates bacterial/protozoan contamination only, with no fecal contamination from human sources (which would introduce viral pathogens)

**Filtration must be combined with disinfection when**:
- Source is surface water (stream, pond, lake) — viral contamination is possible
- Any flooding has occurred — sewage contamination introduces viruses
- Source water has confirmed or suspected fecal contamination from human sources
- You cannot confirm filter performance (new filter that has not developed biological layer, damaged filter elements)

**The safest universal approach**: Filter first, then disinfect (boil or chlorinate). Filtration reduces turbidity, which improves disinfection effectiveness. Disinfection addresses pathogens that pass through filter pores. The two stages complement each other and together provide a robust treatment chain.

---

## Section 2: Slow Sand and Biosand Filters — How They Work

### 2.1 The Biological Mechanism: Schmutzdecke

The most important concept in biological sand filtration is the **schmutzdecke** (German: "dirt blanket") — a thin biological layer that forms on the top 1–2 inches of sand in a slow sand filter. This layer consists of:
- Algae
- Bacteria that consume pathogens
- Protozoa that graze on bacteria
- Diatoms and fungi
- Organic material from filtered water

The schmutzdecke forms naturally when water with organic material and pathogens is passed slowly through fine sand. It is the biologically active layer that provides pathogen removal; the sand below provides mechanical filtration and supports the biological community. This is why slow sand filters must be operated within their design flow rate — too much flow disrupts the layer.

The schmutzdecke takes **2–4 weeks to develop fully** in a new filter. During this startup period, biological filtration effectiveness is limited; the filter should not be relied upon as the sole treatment during startup. Use boiling or chemical treatment alongside new filter output until the startup period is complete. [Source: 4]

### 2.2 Biosand Filter Specifications

A biosand filter is a compact, household-scale version of the slow sand filter. The standard design, developed by Manz (1993) and refined through international field deployment, consists of:

**Physical dimensions**:
- Container: 90 cm tall × 30 cm × 30 cm (concrete) or equivalent cylindrical (PVC pipe, 55-gallon drum), approximately 75–100 liters total volume
- Diffuser plate (top): distributes incoming water evenly without disrupting sand surface
- Fine sand layer: 50 cm deep (minimum) — this is the primary treatment zone
- Coarse sand layer: 5 cm deep — transition layer
- Gravel layer: 5 cm deep — drainage and support
- Drainage pipe: extends up through gravel and coarse sand to establish a standing water layer above fine sand

**The standing water layer**: This is a key design feature specific to biosand filters. The drainage pipe outlet height is set so that 5–7 cm of water remains standing above the sand at all times. This keeps the sand and schmutzdecke permanently wet, maintaining the biological community even between uses. This is the primary difference from a simple intermittent sand filter, which dries between uses and loses its biological community.

**Flow rate**: Design flow rate is 0.1–0.3 liters per minute. Do not pour water in faster than this; faster flow reduces contact time and disturbs the schmutzdecke. For a household of 4 people needing 20 liters per day, the filter needs to run approximately 1–2 hours per day to supply drinking and cooking water only. [Sources: 1, 4, 9]

---

## Section 3: Biosand Filter Performance — The Complete Evidence Picture

This section presents the honest evidence, including both best-case data and long-term field performance. The purpose is to help communities make informed decisions.

### 3.1 Best-Case Performance Data

The strongest controlled trials of biosand filters show impressive results:

**Ghana randomized controlled trial** (PMC3524599, n = households):
- 97% E. coli reduction
- 67% turbidity reduction
- 60% reduction in diarrheal disease incidence in treated households
- This represents well-designed, properly monitored biosand filters in their first years of operation. [Source: 5]

**Somalia field study** (Research Square rs-7668141, 2024 — most recent field data):
- 95.66% bacterial reduction
- 85% turbidity reduction
- Results from field deployment in Borama region, 2024. [Source: 6]

### 3.2 Field-Realistic Performance

Field conditions differ from controlled trials. The Nicaragua field study (n = 199 households) found:
- Median bacterial removal efficiency: 80%
- Reduced to detectable reduction in 74% of households
- Reduced to <10 CFU/100 mL in only 17% of households

This means that in typical field use, biosand filters reduce E. coli contamination significantly, but most households still had detectable bacterial levels in filtered water — not zero. [Source: 7]

### 3.3 Long-Term Performance — The Critical Caution

The 7-year Rwanda field study (IWA Publishing, 2023) is the most important long-term data available on biosand filter performance:

- 92.9% of filters were still in use at 7 years
- Only 64.3% were functioning well at 7 years
- **50% of effluent samples were positive for fecal coliforms at 7 years**

This finding — that half of biosand filter effluent samples showed fecal contamination after 7 years — represents the core challenge of biological sand filtration at community scale: filters that worked in year 1 may not be protecting users in year 7. The cause is maintenance failures: the schmutzdecke becomes over-thick, the sand becomes clogged, or the standing water layer is disrupted. [Source: 8]

**What this means for implementation decisions**:

| Scenario | Recommended Approach |
|---------|---------------------|
| New filter, properly maintained, years 1–3 | Biosand filter as primary treatment for bacteria/protozoa; combine with chlorination for viruses |
| Filter more than 3 years old, maintenance history uncertain | Always follow with boiling or chemical treatment; do not rely on filter alone |
| Community-scale deployment without dedicated maintenance oversight | Pair with chlorination as standard practice regardless of filter age |
| Individual/household filter with known maintenance | Single filter acceptable for bacteria/protozoa; boiling for any virus concern |

### 3.4 What Biosand Filters Remove and What They Do Not

| Pathogen/Contaminant | Biosand Filter Effectiveness |
|----------------------|------------------------------|
| E. coli and coliform bacteria | 80–97% under good conditions; 50% or less without maintenance |
| Giardia lamblia cysts | High removal due to size (10–20 microns) — physical straining |
| Cryptosporidium oocysts | High removal due to size (5–10 microns) — physical straining |
| Viruses | Poor — viruses (0.02–0.3 microns) are too small for sand filtration |
| Turbidity / sediment | 50–85% reduction |
| Nitrates | None |
| PFAS | None |
| Heavy metals | Partial (some adsorption of certain metals by biological layer) |
| Organic compounds | Partial (biological degradation of some organics) |

---

## Section 4: DIY Biosand Filter Construction

This section provides a construction procedure for a functional household biosand filter using materials available in most US contexts. This design follows the established WHO/Manz standard but adapted for materials available at a hardware store.

### 4.1 Materials List

**Container**: One food-grade 5-gallon plastic bucket with lid (top bucket — filter) + one food-grade 5-gallon bucket without lid or with spigot (bottom bucket — collection). Alternatively, a 55-gallon drum or large food-grade plastic container can be used for larger volume.

**For a 5-gallon bucket biosand filter**:

| Item | Specification | Source | Quantity |
|------|--------------|--------|---------|
| Food-grade 5-gallon buckets | HDPE #2 plastic (marked on bottom) | Hardware store, restaurant supply | 2 |
| Fine sand | Unwashed river sand or "play sand" — grain size 0.15–0.35 mm; avoid beach sand | Hardware store (pool filter sand works well) | 15–20 lbs |
| Coarse sand | Grain size 0.5–2 mm | Hardware store | 5 lbs |
| Gravel | Washed pea gravel, 3–6 mm | Hardware store | 5 lbs |
| PVC pipe | 1/2-inch diameter | Hardware store | 12 inches |
| PVC pipe cap | 1/2-inch | Hardware store | 1 |
| Drill + bits | 1/2-inch bit for PVC pipe hole, small bit for multiple drainage holes | — | — |
| Diffuser plate | Small plastic plate or lid cut to fit inside bucket, with 1/4-inch holes drilled throughout | — | 1 |

**Estimated cost**: $40–80 depending on locally available sand and container costs.

### 4.2 Construction Procedure

**Step 1: Prepare the drainage PVC pipe**

1. Cut a 10-inch length of 1/2-inch PVC pipe.
2. Drill 6–8 small holes (1/8-inch) in the bottom 3 inches of the pipe — these are the drainage holes that allow water through while keeping sand out.
3. Cap the bottom with a 1/2-inch PVC cap.

**Step 2: Prepare the filter bucket**

1. Drill a 1/2-inch hole in the center of the bottom of the upper bucket.
2. Insert the PVC pipe through the hole so the capped (holed) end is inside the bucket at the bottom. The pipe should extend 5–7 cm above the bottom of the bucket. This creates the standing water layer — water drains through the holes into the pipe and out the bottom, but the pipe height keeps 5–7 cm of water standing above the sand at all times.
3. Seal around the pipe with food-safe sealant (aquarium silicone sealant works well) to prevent leaks around the pipe hole.

**Step 3: Layer the media**

Layer in this order (bottom to top):

1. **Gravel** (2 inches / 5 cm): Pour washed gravel around the base of the PVC pipe. This supports the sand layers and provides drainage.
2. **Coarse sand** (2 inches / 5 cm): Pour on top of gravel. This is the transition layer.
3. **Fine sand** (8–10 inches / 20–25 cm minimum; more is better up to 18 inches / 45 cm): Pour slowly on top of coarse sand. Tamp gently to remove air pockets. This is the primary treatment zone where the schmutzdecke will develop.
4. **Leave 3–4 inches of space at the top** for the diffuser plate and incoming water.

**Step 4: Create the diffuser plate**

The diffuser plate prevents incoming water from disturbing the sand surface when poured in.

1. Cut a plastic plate or lid to fit inside the bucket diameter, with 1–2 inches clearance on all sides.
2. Drill 12–15 holes (1/4-inch) distributed evenly across the plate.
3. Place over the top of the sand on short spacers (3 plastic bottle caps or similar) so water can flow out from under the plate across the sand surface without point impact.

**Step 5: Set up the collection bucket**

Place the collection bucket directly below the filter bucket. The PVC pipe extends out the bottom of the filter bucket and should drain directly into the collection bucket. If using a 5-gallon bucket setup, one bucket sits on a shelf or elevated surface above the second.

**Step 6: Connect and test for leaks**

Fill the filter bucket with clean water and observe:
- Water should drain slowly through the sand, down the PVC pipe, and into the collection bucket below.
- The standing water level above the sand should stabilize at approximately 5–7 cm (the height of the PVC pipe above the sand surface).
- No water should bypass through leaks around the PVC pipe.

### 4.3 Startup Period and Initial Conditioning

A new biosand filter requires 2–4 weeks of operation before the schmutzdecke layer develops to full effectiveness. During this period:

1. **Week 1–2**: Run the filter daily with your source water. Do NOT drink the output yet, or treat with boiling or chemicals as backup. The filter is mechanically removing sediment but biological removal is not yet reliable.

2. **Week 2–4**: Biological layer is developing. Filter output should be visibly clearer. You may begin to see a slight greenish-grey layer on the sand surface — this is the schmutzdecke forming.

3. **Week 4+**: Full biological removal capability. If you have a water test kit, test for E. coli at this point. A well-developed filter should show significant reduction.

**The schmutzdecke during startup is fragile**: Avoid draining the filter completely during startup. The standing water layer must be maintained to keep the biological community alive. If you cannot use the filter for more than 2–3 days, cover it to reduce evaporation but do not drain it.

### 4.4 Maintenance Schedule

| Frequency | Task |
|-----------|------|
| Daily | Pour 15–20 liters through the filter as needed; do not exceed flow rate |
| Weekly | Check that standing water layer is maintained (5–7 cm above sand) |
| Monthly | Remove diffuser plate and inspect sand surface; if heavily clogged with black or brown material, gentle scraping of the top 1 cm of sand is needed ("wet harrowing") — see Step below |
| Every 6–12 months (when flow rate drops significantly) | Wet harrowing procedure — see below |
| Annually | Inspect PVC pipe for clogging; rinse gravel layer |

**Wet harrowing procedure** (when clogging reduces flow rate):

1. Before harrowing, collect and save the standing water above the sand in a clean container.
2. Using a clean spoon or spatula, gently stir and scrape the top 1–2 cm of the sand surface while the sand is still wet — do not allow it to dry.
3. Remove the disturbed top layer (it will be dark with biological material).
4. Pour back the saved standing water to maintain the wet environment.
5. Resume use immediately — do not let the sand dry.

**Why harrowing works**: It removes the clogged overburden while preserving the deeper schmutzdecke. The biological community regenerates in the disturbed top layer within 1–2 weeks. [Source: 4]

---

## Section 5: Commercial Gravity Filters — What They Are and Their Limits

### 5.1 Ceramic Gravity Filters (Berkey, Doulton, British Berkefeld)

**How they work**: Ceramic filter elements contain millions of tiny pores (0.3–0.9 microns). Water is poured into the upper chamber and gravity-fed through the ceramic element into the lower chamber. Pathogens larger than the pore size are physically removed. Some ceramic elements also contain colloidal silver, which provides additional antibacterial action.

**What ceramic gravity filters remove**:
- Bacteria: 99.99% (log 4 removal or better) — verified by NSF/ANSI testing
- Protozoa (Giardia, Cryptosporidium): >99.9%
- Turbidity and sediment: Significant reduction
- Some organic compounds: Varies by element; models with activated carbon post-filter improve this

**What ceramic gravity filters do NOT reliably remove**:
- Viruses — most ceramic elements have pores too large to exclude viruses consistently
- Dissolved chemicals (nitrates, PFAS, heavy metals) — unless an activated carbon stage is included
- Fluoride — unless a specific fluoride-removal element is included

**Flow rate**: Very slow — typically 1–5 liters per hour depending on element condition, head pressure, and turbidity of source water. A 3-gallon Berkey-style filter typically produces 3–6 gallons per day at gravity flow rates. This is adequate for drinking and cooking for a household but not for full household water needs.

**Maintenance**: Ceramic elements clog over time with sediment. They can be cleaned by gently scrubbing the outer surface with a soft brush under running water — this removes the clogged surface layer and restores flow. Elements eventually lose their ability to be scrubbed clean (after 5–10 cleanings in many models) and must be replaced.

**Cost**: Commercial units (Big Berkey, Doulton) run $200–500. Filter elements are $30–100 each and need replacement every 3,000–6,000 gallons depending on source water quality. Replacement elements from reputable manufacturers are the same price as in original units.

**DIY version (2-bucket ceramic filter)**:
- Two stacked food-grade 5-gallon buckets
- One or two ceramic filter elements with threaded base ($30–60 each)
- Drill 5/8-inch hole in bottom of upper bucket; thread filter element through; tighten to seal
- Spigot hole in lower bucket: drill 7/8-inch hole, install plastic spigot ($5)
- Stack with upper bucket above lower; pour source water into upper
- Total DIY cost: ~$75–150; same performance as commercial units [Source: 10]

### 5.2 Portable Microfilters (Sawyer Squeeze, LifeStraw)

**How they work**: Hollow fiber membrane with 0.1-micron absolute filtration. Water is squeezed or sucked through the membrane; anything larger than 0.1 micron — including bacteria and protozoa — is physically excluded. The membrane cannot be clogged permanently; it is backwashed with clean water to restore flow.

**What they remove**:
- Bacteria: 99.99999% (log 7 removal) — verified laboratory performance
- Protozoa (Giardia, Cryptosporidium): 99.9999% (log 6 removal)

**What they do NOT remove**: Viruses, chemicals (nitrates, PFAS, heavy metals), dissolved contaminants.

**Capacity**: The Sawyer Squeeze filter is rated for 100,000 gallons before replacement is needed. At 2 gallons per day for a person, this is 137 years of personal use — the filter is effectively permanent if properly maintained (backwashed when flow slows).

**Limitations for long-term household use**: Sawyer and LifeStraw filters are designed for individual or small-group use with relatively clear source water. They work poorly with very high turbidity (>30 NTU) — pre-filter through cloth first. They require user effort (squeezing or creating suction), making them less practical for treating large volumes.

**Best use cases**: Camping, backpacking, emergency kit inclusion, individual-scale backup treatment. Less appropriate as a household's primary water system for treating 10–20 gallons per day. [Sources: 1, 4]

### 5.3 Activated Carbon Filters

**How they work**: Activated carbon is a highly porous form of carbon (charcoal that has been chemically or thermally activated to create millions of internal pores). Water passes through the carbon; organic compounds adsorb (stick) to the carbon surface.

**What activated carbon removes**:
- Chlorine and chloramines (taste/odor improvement)
- Many organic chemicals (some pesticides, VOCs, some pharmaceuticals)
- Some heavy metals (lead, mercury — partial)
- Improves taste and odor significantly

**What it does NOT remove**: Bacteria, viruses, protozoa, nitrates, dissolved salts, fluoride, PFAS (unless specifically rated for PFAS).

**Use case in a treatment chain**: Activated carbon is a post-treatment polishing stage, not a primary treatment for biological or chemical contamination. In a multi-stage treatment chain:
- Stage 1: Biosand or ceramic filter (remove sediment, bacteria, protozoa)
- Stage 2: Boiling or chlorination (kill viruses; add residual chlorine for storage)
- Stage 3: Activated carbon (remove chlorine taste; remove any organic compounds)

This sequence produces water that is safe from biological contamination, virus-free, and has improved taste — close to bottled water quality from most source waters (excepting chemical contamination).

---

## Section 6: Building a Complete Household Filtration System

For a household seeking to treat 10–20 gallons per day from surface water or a turbid groundwater source, a staged system outperforms any single filter:

### 6.1 Minimum-Cost Staged System (~$100–200 total)

**Stage 1: Settling tank** — 5-gallon bucket, 1–2 hours settling time for turbid water. Cost: $5.

**Stage 2: DIY biosand filter** — as described in Section 4. Cost: $40–80. Removes bacteria, protozoa, sediment.

**Stage 3: Boiling or chlorination** — fuel/stove cost or bleach cost. Addresses viruses and provides residual disinfectant.

**Throughput**: Biosand filter at 0.2 L/min for 2 hours = approximately 24 liters (6.3 gallons) per day. Sufficient for drinking and cooking for a household of 4 at 1.5 gallons/person/day.

### 6.2 Moderate-Cost System ($200–400) with Ceramic Polish Stage

**Stage 1**: Cloth pre-filter (free — clean t-shirt cloth over bucket mouth)

**Stage 2**: Biosand filter (as above, ~$80)

**Stage 3**: DIY 2-bucket ceramic filter ($80–150) — removes any bacteria/protozoa that passed the biosand filter; adds a second physical barrier

**Stage 4**: Chlorination (bleach or pool shock — $5–20/year)

**Throughput**: Limited by ceramic filter (1–5 L/hour gravity flow). For 20 liters per day, the ceramic filter needs to run 4–20 hours. May need two parallel ceramic filter units for larger households.

### 6.3 Flow Rate Planning Table

| Household Size | Daily Drinking + Cooking Need | Filter Setup Required |
|---------------|------------------------------|----------------------|
| 1 person | 2–3 liters | Single ceramic filter unit (any gravity filter) |
| 2–3 people | 4–8 liters | Single ceramic filter or small biosand filter |
| 4–5 people | 8–15 liters | Biosand filter (2 hrs/day) + ceramic polish stage |
| 6–8 people | 15–25 liters | Two biosand filters or one large-volume biosand filter |
| 10+ people (small community) | 30–50+ liters | Community-scale slow sand filter (see WHO guidance) |

---

## Section 7: SODIS as a Non-Filtration Treatment Option for Clear Water

Solar disinfection (SODIS) is included here because it fits in the treatment chain when water is already low-turbidity — either naturally clear or filtered to below 30 NTU.

**SODIS procedure**:

1. Assess turbidity: Hold a newspaper behind a filled 1.5-liter clear PET bottle. If you can read the headline through the bottle, turbidity is below approximately 30 NTU and SODIS is viable.

2. Fill clear PET plastic bottles (1–2 liter size). Shake for 20 seconds to aerate — aeration slightly improves SODIS effectiveness.

3. Place bottles on a corrugated metal or aluminum surface (reflective surface increases UV exposure by 25–30%), or lay flat on any surface in direct sunlight.

4. **Exposure time**:

| Sky Conditions | Required Exposure Time |
|---------------|----------------------|
| Sunny (>50% sun visible over the period) | 6 hours |
| Cloudy but UV reaches ground (white cloud cover) | 6 hours (some sources: up to 8 hours) |
| Completely overcast (heavy cloud, no UV) | 2 consecutive days minimum |

5. After treatment, consume directly from bottle. Do not pour into another container (introduces contamination risk).

**What SODIS removes**: Bacteria (including E. coli), viruses (UV-sensitive viruses), and protozoa (with sufficient UV dose). Cryptosporidium removal is less reliable than from boiling.

**What SODIS does NOT do**: Chemical removal. No effect on nitrates, PFAS, heavy metals, or agricultural chemicals.

**Bottle requirements**: Clear PET plastic only. PET is labeled with the recycling number "1" on the bottle bottom. Glass blocks UV. Colored, scratched, or clouded PET reduces UV transmission. Use bottles in good condition without significant scratching.

**Climate suitability for SODIS in the US**:

| Region | Season | SODIS Viability |
|--------|--------|-----------------|
| Southwest (Arizona, New Mexico, Nevada) | Year-round | Excellent — high UV index, low cloud cover |
| Southeast (Florida, Texas Gulf) | March–November | Good |
| Midwest (Zone 5) | May–September | Acceptable; overcast days require 2-day exposure |
| Pacific Northwest | May–August only | Limited — high cloud cover reduces effectiveness |
| Mountain West (Colorado, Utah) | May–October | Good at altitude (higher UV at elevation) |

**Field evidence from high-altitude Africa** (Ethiopia, Rwanda, Kenya): SODIS achieves full bacterial inactivation at standard 6-hour exposure times even in partially cloudy conditions, due to high UV index at elevation. PMC article PMC9640691 confirmed SODIS effectiveness in Tigray, Ethiopia. These conditions are comparable to US mountain regions at similar elevation. [Source: 12]

**2025 review** (Frontiers in Water, 2025): SODIS achieved 99.7% pathogen removal at turbidity of 16 NTU in recent multi-country field study. The review confirmed SODIS as a reliable household treatment for clear-to-moderate turbidity water in high-UV environments. [Source: 11]

---

## Section 8: Worked Examples

### Worked Example 1: Biosand Filter for a Rural Off-Grid Household

**Situation**: 4-person household, off-grid. Water source is a shallow pond (spring-fed, but with waterfowl — higher biological contamination likely). No electricity. Chemical supplies available but costly. Building a permanent water treatment setup.

**Goal**: Treat 20 liters per day of pond water for drinking and cooking.

**System design**:

Stage 1: Settling bucket — 5-gallon bucket, fill from pond and let sit 2 hours each morning. Ladle from top 4 gallons (leaving sediment at bottom).

Stage 2: Biosand filter — constructed as per Section 4. Run settled water through biosand filter during the morning; collect filtered water in lower bucket. Run time: 2 hours at 0.2 L/min = 24 liters. More than adequate.

Stage 3: Chemical treatment for viruses — add 8 drops of 6% bleach per gallon to the filtered output (waterfowl contamination makes viral risk non-trivial). Contact time: 30 minutes.

Stage 4: Store in covered food-grade containers. Consume within 24 hours.

**Startup note**: During the first 4 weeks of filter operation, boil instead of chlorinating — establishes a higher-confidence treatment baseline while the schmutzdecke develops.

**Annual maintenance plan**: Wet harrowing every 3–6 months when flow rate drops. Inspect sand surface monthly. Replace top 2 cm of sand annually after year 3.

### Worked Example 2: Gravity Filter for Emergency Apartment Use

**Situation**: Urban apartment, no yard. Municipal water under a 2-week boil-water advisory following pipe damage. Family of 3. Has a Berkey-style filter unit with 2 ceramic elements. Source: tap water (still running, possibly contaminated with pipe bacteria).

**Assessment**: Tap water from pipe damage: bacterial risk (E. coli, legionella possible), turbidity may be elevated (pipe sediment). Chemical contamination is not likely from pipe damage. Viral risk is low in a municipal pipe damage scenario (not a sewage contamination event).

**Treatment**:

1. Run tap water into upper Berkey chamber.
2. Gravity-filter through ceramic elements into lower chamber.
3. Ceramic removes bacteria and sediment. For this scenario (bacterial risk, no viral concern), ceramic filtration alone may be adequate.
4. For additional security, after filtering, add 2 drops of 6% bleach per liter for viral coverage. Contact time: 30 minutes.

**Flow rate planning**: Two Berkey elements at standard gravity flow rate = approximately 4 liters/hour. For 20 liters per day (3 people at ~6 liters/day including cooking and hygiene water), filter runs approximately 5 hours per day. Practical — run filter continuously through the day, filling from tap as needed.

**Note**: Do not clean Berkey ceramic elements with tap water during this advisory — if tap water is contaminated, cleaning with it would recontaminate the filter element. If elements need cleaning, use previously filtered and chlorinated water.

### Worked Example 3: SODIS for an Emergency Camp Setting

**Situation**: 8 people in a temporary camp after a disaster. Source water is a running stream (low turbidity, clear — moderate biological contamination likely). No stove fuel. Sun is available. Have 12 clear 1.5-liter PET bottles.

**Water needs**: 8 people × 2 liters/day = 16 liters/day minimum.

**SODIS capacity with 12 bottles at 1.5 liters each**: 18 liters per 6-hour treatment cycle. One cycle per day produces 18 liters — exactly adequate for minimum needs.

**Procedure**:

Morning: Fill all 12 bottles with stream water. Shake each to aerate. Place on metal roof or reflective tarp in direct sunlight at 9 AM.

3 PM (6 hours later): Confirm sunny conditions maintained. Collect bottles. These are ready to drink.

Label with treatment time if multiple batches will be running (e.g., two batches on a long summer day).

**If overcast**: If day is significantly overcast (heavy clouds most of the day), leave bottles out for a second day before consuming. Treat as untreated until 48-hour exposure is achieved.

**Backup**: If two consecutive overcast days occur, water need exceeds SODIS capacity. Fall back to boiling using any available fuel or fire. Even small amounts of fuel can be used to boil the day's most critical 4–6 liters (drinking water only; use SODIS-treated water for hygiene and cooking where full inactivation is less critical).

---

## Sources

1. CDC. "Water Treatment Methods." Centers for Disease Control and Prevention. https://www.cdc.gov/healthywater/drinking/index.html

2. CDC. "How to Create and Store an Emergency Water Supply." https://www.cdc.gov/water-emergency/about/how-to-create-and-store-an-emergency-water-supply.html

3. EPA. "National Primary Drinking Water Regulations." U.S. Environmental Protection Agency. https://www.epa.gov/ground-water-and-drinking-water/national-primary-drinking-water-regulations

4. WHO. *Guidelines for Drinking-Water Quality: 4th Edition with 1st and 2nd Addenda.* Chapters 7, 9, and 10. World Health Organization, Geneva, 2022. https://www.who.int/publications/i/item/9789240045064 (NCBI Bookshelf: https://www.ncbi.nlm.nih.gov/books/NBK579461/)

5. Stauber CE, et al. "Evaluation of the Impact of the Plastic BioSand Filter on Microbiological Quality of Drinking Water in Rural Tamale, Ghana." *International Journal of Environmental Research and Public Health*, 2012. PMC3524599. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3524599/

6. Khadar MA, et al. "Efficacy and Sustainable Adoption of BioSand Filters for Water Purification in Borama, Somalia." Research Square, 2024. rs-7668141/v1. https://www.researchsquare.com/article/rs-7668141/v1

7. Napotnik JA, et al. "Assessment of Biosand Filter Performance in Households in Three Rural Communities in Nicaragua." *PubMed*, 2020. PMC20795755. https://pubmed.ncbi.nlm.nih.gov/20795755/

8. Abebe LS, et al. "Seven-Year Performance of Biosand Filters in Rural Rwanda." *Journal of Water, Sanitation and Hygiene for Development*, IWA Publishing, 2023. https://iwaponline.com/washdev/article/13/5/333/94658/

9. WHO. "Household Water Treatment and Safe Storage." WASH guidance toolkit. https://www.who.int/teams/environment-climate-change-and-health/water-sanitation-and-health/tools-and-toolkits/household-water-treatment-and-safe-storage

10. Internal Reference. Open-Repo Project. "systems-resilience/individual/01-water.md." DIY Berkey-style gravity filter construction notes.

11. Ubomba-Jaswa E, et al. "Potential of Solar Water Disinfection (SODIS) for Pathogen Control During Water Scarcity Crisis." *Frontiers in Water*, 2025. https://www.frontiersin.org/journals/water/articles/10.3389/frwa.2025.1679793/full

12. Hailu W, et al. "SODIS in Large-Volume Containers in the Tigray Region, Ethiopia." *PMC*, 2022. PMC9640691. https://pmc.ncbi.nlm.nih.gov/articles/PMC9640691/

13. SODIS Reference Center, Eawag. "SODIS Method: Application and Field Validation." Swiss Federal Institute of Aquatic Science and Technology. https://www.sodis.ch/methode/anwendung/index_EN

14. Effectiveness of Solar Disinfection (SODIS) for Household Water Treatment. *IWA Publishing*, 2021. https://iwaponline.com/washdev/article/11/3/374/80556/

---

**Attribution**: This article was produced for the Open-Repo Project, Water Systems Domain 3, Wave 0 content production (July 2026). Biosand filter construction procedure follows the Manz/WHO standard design adapted for US hardware store materials.

**License**: CC-BY-4.0. You are free to adapt, share, and republish with attribution to "Open-Repo Project."

**Safety note**: Biosand filters do not reliably remove viruses. In any situation where human sewage contamination is possible (flooding, surface water near population centers), always follow biosand filtration with boiling or chemical disinfection. Filter performance degrades without maintenance; treat filters older than 3 years as pre-filtration only, not as standalone treatment. The 7-year Rwanda field data (50% fecal coliform detection in effluent) is the most important caution in this article: a filter that worked when installed may not be protecting its users years later without active maintenance.
