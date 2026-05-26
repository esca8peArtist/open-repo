---
title: "Water Systems & Purification"
series: "Systems Resilience — Phase 5 Wave 3"
zone: "Zone 5 (Midwest US)"
climate: "30–38 in annual precipitation, -20°C winters, seasonal freeze-thaw"
scale: "Individual → Household → Community (2,000–5,000 gal/day)"
last_updated: 2026-05-26
status: production-ready
word_count: ~6700
---

# Water Systems & Purification

## Overview

Water is the single most urgent dependency in any infrastructure disruption scenario. An adult in Zone 5 requires approximately 1 gallon per day as a bare survival minimum (0.5 gal for drinking, 0.5 gal for minimal cooking and sanitation), with comfortable household function requiring 3–5 gallons per person per day [1]. At 4 people per household, that is 16–20 gallons per day to maintain basic hygiene and food preparation. At the community scale of 20–50 households, a functioning water system must deliver 1,000–5,000 gallons per day continuously.

Municipal water in the Zone 5 Midwest depends on electrical pumps, chlorination equipment, and distribution pressure maintained by overhead storage tanks or elevated pumps. A sustained power outage of more than 48–72 hours typically results in loss of municipal water pressure; contamination risk increases as distribution pressure drops. In a prolonged infrastructure failure scenario — the core planning scenario for this knowledge base — municipal water may be unavailable for weeks to months.

Zone 5 presents specific challenges that are not generic:
- **Winter:** Surface water and shallow groundwater freeze. Any above-ground storage system freezes unless insulated or heated. Snowmelt is a large seasonal water input but introduces contamination risk.
- **Spring:** Snowmelt and heavy precipitation generate turbid, sediment-laden surface water. Agricultural runoff in the Midwest (nitrates, pesticides, pathogens from livestock operations) peaks in March–May.
- **Summer:** Algae blooms in standing water and surface sources. Evaporation from open storage.
- **Growing season:** Water demand for irrigation competes with drinking and sanitation needs.

**Critical quantities:**
- Minimum per person per day (survival): 1 gallon [1]
- Comfortable per person per day: 3–5 gallons [2]
- Household (4 people) daily need: 16–20 gallons comfortable
- Community (50 people) daily need: 150–250 gallons minimum, 500–1,000 gallons comfortable
- 30-day household storage (1 gal/person/day, 4 people): 120 gallons minimum
- Zone 5 annual precipitation: 30–38 inches (Illinois 36 in, Indiana 42 in, Ohio 38 in, Minnesota 27 in, Wisconsin 32 in) [3]
- Roof collection potential: 1,200 sq ft roof at 36 in rainfall = ~22,000 gal/year [4]

This document covers water collection, purification, storage, backup sources, failure mode recovery, and scaling pathways. All methods are designed to function without grid electricity or professional infrastructure.

---

## Section 1: Individual Scale — Collection and Basic Purification

### 1.1 Rainwater Collection Systems

Rainwater collection is legal in all Zone 5 Midwest states, with varying regulatory frameworks:
- **Illinois:** Legal; non-potable use standard; systems over 5,000 gal capacity require permitting [5]
- **Indiana:** Legal; non-potable systems covered under 2020 Indiana Residential Code Chapter 29 [5]
- **Ohio:** Legal; potable use allowed under Ohio Rev. Code §3701.344 for private systems serving fewer than 25 people [5]
- **Minnesota:** Legal; encouraged; rooftop collection only (not surface runoff); no permit needed for outdoor non-potable use [5]
- **Wisconsin:** Legal; no statewide restrictions; local ordinances may apply [5]

**First-flush diverter (essential for any collection system):** The first 1–2 gallons of rain from a roof flush accumulated bird droppings, dust, debris, and microbial contamination into a separate chamber, bypassing the cistern. Without a first-flush diverter, collected water will be significantly more contaminated. Commercial units cost $15–$40; DIY versions use a capped 4-inch PVC standpipe of calculated volume (1 gallon per 100 sq ft of roof area) connected to a tee fitting before the cistern inlet [6].

**Collection infrastructure — individual scale (rain barrel, 50–100 gallons):**
1. Position barrel below downspout; install overflow pipe at 85% capacity.
2. Screen inlet with 1/8-inch or finer mesh to exclude insects (mosquitoes breed in standing water in as little as 7 days).
3. Add first-flush diverter.
4. Cover completely — light excludes algae growth; sealed cover excludes insects.
5. Opaque barrels prevent algae; dark colors also reduce UV degradation.
6. This water is suitable for garden irrigation. For drinking/cooking, full purification is required.

**Collection infrastructure — household scale (250–1,500 gallons):**

A 1,000-gallon polyethylene cistern (IBC tote or dedicated poly tank, $150–$400) installed below a 1,500 sq ft roof in Illinois (36 in annual rainfall) can collect approximately 33,000 gallons annually — far more than household drinking water needs, but substantially reduced by collection efficiency losses (20–30% from evaporation, first-flush bypass, and dry periods) [4]. Practical yield: 20,000–25,000 gallons per year from a well-designed system.

**Calculation formula:**
Roof area (sq ft) × Annual rainfall (in) × 0.623 × Collection efficiency (0.75–0.80) = Annual gallons collected [4]

Example: 1,500 sq ft × 36 in × 0.623 × 0.78 = 26,100 gallons/year

**Zone 5 winter management of cisterns:**
Any cistern that holds water through a Zone 5 winter must be either below ground (below the frost line of 42–60 inches depending on location [7]), insulated, or drained. Options:
- **Below-ground poly or concrete cistern:** Most reliable. Install at minimum 48 inches below grade in Illinois/Indiana/Ohio; 54–60 inches in Minnesota/Wisconsin [7]. Inlet and outlet pipes must also be below frost line or insulated.
- **Insulated above-ground tank:** Wrap with minimum R-20 closed-cell foam insulation panels; bury tank base in earth berm; add tank heater if electricity is available. Without heating, above-ground tanks will freeze solid in Zone 5 winters.
- **Seasonal drainage:** Drain above-ground tanks before first hard freeze (typically October 15–November 1 in Zone 5). Refill in spring from snowmelt or early rains.

### 1.2 Purification Methods Requiring No Electricity

**Method 1 — Boiling (most reliable, no equipment):**
Boiling is 100% effective against bacteria, viruses, and protozoa. Bring water to a rolling boil (any visible bubbling) and maintain for 1 minute at elevations below 6,500 ft (all Zone 5 sites qualify) [1]. At high turbidity, filter first (see below), then boil. Boiling does not remove chemical contaminants, heavy metals, or dissolved salts.

Fuel cost: approximately 0.5 kWh per gallon of water boiled (on electric stove), or equivalent in wood, propane, or natural gas. A household using boiling as primary purification needs to plan significant fuel storage. A rocket stove or wood gasifier reduces fuel consumption by 60–80% vs. open fire [8].

**Method 2 — Chlorine bleach (convenient, chemical):**
Unscented regular liquid bleach with sodium hypochlorite as the only active ingredient (5.25–8.25% concentration) is effective against bacteria and most viruses but not Cryptosporidium. EPA-specified dosage [9]:

| Water condition | 6% bleach | 8.25% bleach |
|----------------|-----------|-------------|
| Clear water | 8 drops/gallon | 6 drops/gallon |
| Cloudy/cold water | 16 drops/gallon | 12 drops/gallon |

After adding bleach: stir, let stand 30 minutes. Water should have slight chlorine smell; if not, repeat dose and wait another 15 minutes. If still no chlorine smell, discard and find alternate source.

Important: Bleach degrades over time. Bleach stored at room temperature loses approximately 50% of potency within 6 months [9]. Date bleach bottles when purchased; replace every 6 months for emergency use. Calcium hypochlorite pool shock (granular, 68–78% available chlorine, $15–$25 for 1 lb) is more shelf-stable (3–5 years) and can treat far larger volumes: 1 heaping teaspoon (~¼ oz) in 2 gallons water creates a stock solution; add 1 part stock solution to 100 parts water to treat (roughly equivalent to bleach treatment) [9].

**Method 3 — Solar disinfection (SODIS):**
Clear PET plastic bottles (1–2 liter) filled with water and placed in direct sunlight for 6 hours (full sun) to 2 days (cloudy) achieve >99.9% kill of bacteria and >99% kill of viruses via UV-A radiation and heat synergy [10]. WHO recommends SODIS as a proven household water treatment method [10].

Limitations for Zone 5:
- Effective only in turbidity below 30 NTU (water must appear relatively clear). Pre-filter highly turbid water.
- Zone 5 November–March: insufficient solar intensity and duration for reliable SODIS; daylight hours and cloud cover severely limit effectiveness.
- Summer Zone 5: effective June–August; adequate September–October on clear days.
- No effect on chemical contamination.

Materials: Clear PET bottles (not polycarbonate, which blocks UV). Black mat or roof surface as solar collector increases effectiveness.

**Method 4 — Gravity filtration (multi-stage):**

A DIY gravity filter using stacked 5-gallon food-grade buckets can remove sediment and many biological contaminants:

*Construction specifications (two-bucket system):*
- Upper bucket (dirty water input): drill two 7/16-inch holes in bottom; install two ceramic or carbon block candle filters (rated 0.5 micron minimum) through holes with food-grade rubber gaskets and wing nuts [11].
- Lower bucket (clean water output): drill 1/2-inch hole in side at 1.5 inches from bottom; install spigot.
- Stack upper bucket on lower; water flows by gravity through filters at 0.3–0.5 liter/minute per filter element.
- Cost: $20–$40 for buckets and spigot; $25–$60 per ceramic filter element with 2,000–6,000 gallon rated life [11].

Commercial equivalent: Black Berkey elements (stainless steel housing, $250–$400 retail, rated 6,000 gallons per filter pair) achieve equivalent performance. The DIY version uses the same ceramic or carbon block elements in a lower-cost housing.

Ceramic candle filters rated at 0.5 microns or finer remove Giardia and Cryptosporidium protozoa, bacteria, and turbidity. They do not remove viruses (100 nanometers, smaller than 500 nanometer rating). For surface water in agricultural Midwest where viral contamination is a real risk, combine filtration with chemical disinfection or boiling.

*Five-stage filtration sequence for high-turbidity Zone 5 surface water:*
1. Pre-settle: let turbid water stand 30–60 minutes; decant top 2/3.
2. Coarse filter: pour through clean cloth or coffee filter (removes large particles).
3. Fine filter: gravity ceramic filter (removes bacteria, protozoa, turbidity).
4. Disinfect: bleach dose or boil (kills viruses, any organisms passing filter).
5. Store: in sanitized covered container.

### 1.3 Biosand Filter Construction

The biosand filter (BSF) is a concrete or plastic container filled with layers of sand and gravel, matured over 2–3 weeks to develop a biological layer (schmutzdecke) of beneficial microorganisms on the top 1–2 cm of sand. This biological layer, combined with mechanical filtration, achieves 90–99% bacteria removal and 70–99% virus removal after full maturation [12].

**CAWST Version 10 concrete BSF specifications:**
- Container: concrete, 0.9 m (35 in) tall, 0.3 m (12 in) square footprint (~1 cubic ft)
- Layer sequence (bottom to top): gravel (1–4 mm, 5 cm depth), fine gravel (1–2 mm, 5 cm), fine sand (0.15–0.35 mm, 55 cm), standing water layer (5 cm above sand)
- Diffuser plate: installed above sand surface to prevent disruption during water pouring
- Outlet pipe: adjusts standing water depth to 5 cm
- Output: up to 36 liters/hour (0.4 L/min maximum recommended) [12]
- Maturation time: 2–3 weeks of daily operation with source water before biological layer fully develops
- Cost: $15–$30 in materials; requires concrete work

**Zone 5 BSF consideration:** The biological layer dies if the filter freezes or is unused for more than 2–3 weeks. Zone 5 winter use requires either indoor installation (garage, basement) with unfrozen water supply, or seasonal restart in spring (requires 2–3 week re-maturation). Plan for this gap in winter water supply from BSF.

---

## Section 2: Household Scale — Storage, Wells, and Year-Round Systems

### 2.1 Water Storage Systems

Effective household water security requires stored reserves against both short supply disruptions and purification/collection infrastructure failures.

**Storage targets:**
- Emergency minimum (72 hours): 3 gallons × 4 people = 12 gallons in food-grade containers
- 2-week buffer (FEMA recommended): 112 gallons for 4 people at 1 gal/person/day [1]
- 30-day resilience buffer: 240 gallons minimum (4 people, 2 gal/person/day)
- 90-day supply: 720 gallons at 2 gal/person/day

**Container options:**

| Container type | Volume | Cost | Shelf life of stored water | Notes |
|---------------|--------|------|--------------------------|-------|
| Commercial 1-gal jugs | 1 gal | $1–$2 | 1 year (manufacturer seal) | Convenient; rotation-dependent |
| WaterBob bathtub bladder | 100 gal | $25–$35 | 16 weeks | Emergency fill from tap |
| 55-gal food-grade barrel | 55 gal | $40–$80 | 6–12 months with chlorination | Bung-sealed, opaque |
| 275/330-gal IBC tote | 275–330 gal | $100–$200 used | 6–12 months with treatment | Below-ground or insulated for Zone 5 |
| Concrete cistern | 1,000–10,000 gal | $500–$5,000 | Long-term | Requires regular inspection and treatment |

**Water treatment for long-term storage:** For water stored more than 6 months, treat with sodium hypochlorite at 1/4 teaspoon per 5 gallons every 6 months. Store in opaque containers to prevent algae growth. Test before drinking after extended storage [13].

**Zone 5 freeze protection for storage:**
Above-ground tanks and barrels will freeze solid by January in Zone 5 unless protected. Methods [7]:
- **Burial:** Most reliable. Install below frost line (48–60 in depending on latitude). Inlet/outlet pipes must also be insulated or buried below frost line.
- **Insulation + partial burial:** Earth-berm tank on north-facing slope, R-20 minimum insulation on exposed surfaces, buried 2–3 feet in ground.
- **Indoor installation:** Basement, insulated outbuilding. Space requirement for 300+ gallon tank is significant.
- **Tank heater:** Electric tank heaters (pond heaters or stock tank heaters, $20–$60) maintain above-freeze temperatures at low power draw (~150 watts). Requires power — not infrastructure-independent.
- **Thermal mass:** Very large volumes freeze more slowly. A 1,000-gallon tank will resist freezing longer than a 55-gallon barrel; still inadequate for -20°C Zone 5 nights without insulation.

### 2.2 Private Wells — The Most Reliable Zone 5 Source

A properly constructed private well drawing from a confined aquifer is the most reliable infrastructure-independent water source in Zone 5. Drilled wells can access water at depths of 50–400+ feet; water in confined aquifers is naturally pressurized, physically isolated from surface contamination, and temperature-stable year-round [14].

**Well components relevant to off-grid operation:**
- **Hand pump:** A cylinder-type or pitcher pump installed as a backup to the electric pump allows manual water extraction during power outages. Bison, Simple Pump, and Flojak are commonly cited brands ($300–$900) that can be installed alongside electric submersible pumps in wells down to 300 feet [15].
- **Well depth in Zone 5 Midwest:** Domestic wells typically 50–200 feet in Indiana, Illinois, Ohio; 100–400+ feet in areas with deep bedrock aquifers in Minnesota and Wisconsin [14]. Local well records are available through USGS and state geological surveys.
- **Flow rate:** Most Zone 5 residential wells yield 2–15 gallons per minute (gpm), adequate for household use without power [14].

**Annual water quality testing for private wells:**

USGS recommends annual testing for: total coliform bacteria, nitrates, pH, and total dissolved solids as baseline [14]. Additional testing for contaminants of local concern: arsenic (elevated in parts of Midwest), pesticides/herbicides (agricultural areas), manganese, and iron.

Testing sources: Many counties offer free or reduced-cost testing; state-certified private labs charge $15–$100 per parameter panel. EPA website provides state-certified lab locator [14].

**Nitrate contamination (high risk in Zone 5 agricultural areas):**
- MCL (Maximum Contaminant Level): 10 mg/L as nitrogen [14]
- Elevated nitrate (>10 mg/L) is common in shallow wells in corn/soybean zones due to fertilizer leaching
- Risk: blue baby syndrome in infants; do not give water with nitrate >10 mg/L to infants under 6 months
- Treatment: reverse osmosis, distillation, or ion exchange — all require some infrastructure. A failed well for nitrates may require seeking an alternative source.
- Shock chlorination does not remove nitrates [16]

### 2.3 Surface Water — Collection and High-Level Purification

Zone 5 Midwest surface water sources (rivers, streams, ponds, lakes) require the most intensive purification of any water source. Agricultural runoff introduces nitrates, phosphates, herbicides, and fecal coliform from livestock operations; urban runoff adds petroleum products and heavy metals; natural sources include algae, turbidity, and protozoa.

**Do not drink unpurified surface water in Zone 5 agricultural areas.** Even clear-appearing surface water in Midwest watersheds may contain 10,000–100,000 CFU/100mL coliform bacteria and nitrate levels exceeding MCLs during spring runoff periods [17].

**Surface water purification sequence (Zone 5):**
1. **Collection:** Gather from flowing water (streams) rather than stagnant water (ponds, ditches) when possible. Flowing water has lower bacterial and algae concentrations.
2. **Pre-settling (30–60 min):** Remove heavy sediment.
3. **Pre-filtration:** Coffee filter, clean cloth, or packed gravel/sand pre-filter to reduce turbidity below 30 NTU.
4. **Ceramic/biosand filtration:** Removes bacteria, protozoa, most turbidity.
5. **Chemical disinfection:** Bleach (double dose if any remaining turbidity) or calcium hypochlorite stock solution.
6. **Boiling (optional, maximally safe):** If viral contamination suspected or water from heavily agricultural area.

This sequence does not fully address dissolved chemical contamination (nitrates, pesticides, heavy metals). In prolonged infrastructure failure, chemical testing capability may not be available; the practical approach is to avoid surface water from known agricultural runoff zones and prefer rainwater or groundwater sources.

**Algae bloom identification and response:**
Blue-green algae (cyanobacteria) blooms occur in Zone 5 ponds and lakes during warm summer months. Visual indicators: blue-green or gray-green surface scum, paint-like texture, musty or fishy odor. Cyanobacteria produce toxins (microcystins) not removed by boiling or standard filtration [18]. **Do not use water from visibly blooming bodies.** Activated carbon filtration (GAC filter, $30–$80) can adsorb some microcystins but is not fully reliable; the safest response is avoidance.

---

## Section 3: Community Scale — Systems Design and Governance

### 3.1 Scaling from Household to Community

A 50-person community requires 250 gallons per day at 5 gallons/person minimum, or 500+ gallons for reasonable comfort and sanitation. This scale is beyond what hand-pump wells or individual cisterns can reliably supply; it requires designed water system infrastructure.

**Option A — Distributed household systems with shared purification:**
Each household maintains its own collection and storage; a community purification station (gravity filter bank, chemical treatment, UV system if power available) processes bulk surface or rain water for communal access. Low capital cost; relies on individual household compliance with storage standards.

**Option B — Gravity-fed spring or well system (most infrastructure-independent):**
If an elevated spring or artesian well exists within or uphill from the community, a gravity-fed distribution system can deliver continuous water without pumps or electricity [19].

*Gravity-fed spring box system components:*
1. **Spring box (catchment structure):** Concrete box built around spring emergence point, 4 ft x 4 ft x 4 ft minimum. Interior screened to exclude insects and animals. Outlet pipe installed 5–10 cm below overflow level. Cleanout drain at bottom. Tight-fitting lid. Backfilled with gravel for drainage [20].
2. **Supply pipe:** Schedule 40 PVC, minimum 1-inch diameter for household-scale, 2-inch for community scale. Buried 48 inches (below frost line) or insulated above grade. Gravity requires at minimum 5 feet of elevation drop per 1,000 feet of horizontal pipe distance for adequate pressure [19].
3. **Storage tank:** 1,000–5,000 gallon concrete or poly cistern at system midpoint or endpoint, providing buffer for peak demand periods.
4. **Distribution pipes:** Buried PVC to tap points or household connections.
5. **Chlorination (optional):** Drip chlorinator at spring box outlet; 0.2–0.5 mg/L residual chlorine is adequate [20].

Capacity: A spring yielding 2 gpm = 2,880 gallons/day — sufficient for 50+ people at 5 gal/person/day [19].

**Option C — Centralized well with community hand-pump distribution:**
A single deep drilled well with a community-maintained hand pump (Bison or Simple Pump, rated for high-volume daily use) serves as the community water supply point. Households carry water in containers (5-gallon jugs, food-safe barrels) from this central point.

*Practical capacity:* A hand pump on a 5-gpm well can deliver 300 gallons/hour with continuous hand-pumping operation. At 4 hours per day of active pumping = 1,200 gallons/day — adequate for 50+ people at survival level but requires organized labor scheduling.

**Cost modeling — community water options:**

| System | Capital cost (50-person community) | Ongoing cost/year | Electricity dependency |
|--------|-----------------------------------|-------------------|----------------------|
| Distributed rainwater (50 households × 500 gal cistern) | $5,000–$10,000 | $200–$400 (lids, bleach) | None |
| Spring box + gravity distribution | $3,000–$8,000 | $100–$200 | None |
| Centralized well + hand pump | $8,000–$20,000 (well drilling + pump) | $200–$500 | None |
| Electric pump well (with generator backup) | $5,000–$15,000 + $3,000–$6,000 generator | $1,000–$2,500 (fuel) | Generator |

Well drilling in Zone 5 Midwest ranges from $15–$50/linear foot depending on bedrock geology; a 150-foot well costs $2,250–$7,500 for drilling alone [14].

### 3.2 Community Water Governance

Water governance prevents contamination and access conflicts — the two most common failure modes in shared water systems. Key governance decisions:

**Who manages the system?** Designate 1–2 system operators responsible for daily checks, testing, maintenance, and treatment. Rotate responsibility with documented training handoff.

**Access rules:** Community spring box or well is a common-pool resource. Rules against contamination (no washing, defecating, or dumping within 100 feet of intake) must be explicit and enforced socially.

**Water testing schedule:** Test monthly during summer (higher contamination risk) and seasonally in winter. Test immediately after any flooding event, equipment failure, or suspected contamination. Keep written log of all test results.

**System maintenance fund:** Even infrastructure-independent systems require occasional maintenance (cracked pipes, clogged filters, sediment clearing). Budget $200–$500 annually for a community-scale gravity system; more for pumped systems.

### 3.3 Failure Mode Recovery

**Failure Mode 1 — Bacterial contamination of well (positive coliform test):**
1. Immediately stop using well for drinking/cooking.
2. Identify likely contamination pathway: flooding of wellhead, cracked casing, contaminated grout seal, shallow well in area with high animal density.
3. Perform shock chlorination: pour calculated volume of bleach (varies by well depth and casing diameter) into well; run water until chlorine smell appears at all taps; let sit 12–24 hours; flush until chlorine smell dissipates; retest 1–2 weeks later [16].
4. If E. coli specific: shock chlorination plus structural inspection. E. coli indicates fecal contamination pathway; fix pathway, not just contamination.
5. If contamination recurs: likely structural issue requiring well rehabilitation or new construction.

Shock chlorination quantities (approximate):
- 6-inch casing, 100 ft deep: ~2 quarts of 5.25% bleach [16]
- 6-inch casing, 200 ft deep: ~1 gallon of 5.25% bleach [16]

**Failure Mode 2 — Cistern algae contamination:**
Green, slippery, or floating algae growth indicates light exposure or organic contamination.
1. Drain and clean cistern completely.
2. Scrub interior with diluted bleach (1:10 bleach:water). Rinse 3–4 times with clean water.
3. Identify and fix light infiltration (add opaque lid or cover if above-ground).
4. Add first-flush diverter if not present (bird droppings are primary nutrient source for algae).
5. Treat stored water with 0.5 ppm chlorine maintenance dose.

**Failure Mode 3 — Sediment/turbidity surge (spring snowmelt, post-storm):**
Turbid water that passes filtration can carry pathogen load above normal levels. In Zone 5, March–May is highest risk.
1. Increase pre-settling time to 4–8 hours before filtration.
2. Replace or backwash ceramic filter elements if flow rate has dropped.
3. Double chemical disinfection dose.
4. Boil all water intended for drinking until turbidity drops below visible levels (typically 3–7 days after peak runoff).

**Failure Mode 4 — Biosand filter biological layer disruption (from freezing or extended non-use):**
1. Do not use filter output for drinking immediately after restart.
2. Run non-chlorinated source water through filter daily for 2–3 weeks before trusting biological layer.
3. During re-maturation period, supplement with boiling or chemical treatment.

---

## Section 4: Implementation Roadmap

### Phase 1 — Bootstrap (First 30 Days)

**Goal:** Establish 30-day water independence for one household.

1. **Immediate storage:** Fill 2–3 clean 55-gallon food-grade barrels from municipal tap before disruption, treating with 1/4 tsp bleach per 5 gallons. This provides 110–165 gallons — 27–41 days at 1 gal/person/day for a family of 4.
2. **Collect and test:** If rainwater system not yet installed, identify collection points (downspouts, clean roof surfaces). Obtain basic water test strips ($10–$25) for bacteria, nitrate, and pH.
3. **Purification capability:** Stock: 1 gallon unscented bleach (rotate every 6 months), 1 lb calcium hypochlorite pool shock (3–5 year shelf life), plus a means of boiling (propane camp stove with 2–3 lbs propane, or rocket stove materials).
4. **DIY gravity filter:** Build two-bucket ceramic filter system ($50–$80) as backup to chemical treatment.

### Phase 2 — Stabilize (Months 1–6)

**Goal:** Year-round collection + purification + freeze-protected storage.

1. **Rainwater system:** Install 250–500 gallon below-ground or properly insulated cistern. Add first-flush diverter. This system provides primary collection March–November in Zone 5.
2. **Biosand filter (spring–fall):** Construct and mature a concrete BSF for intermediate purification of collected rainwater; use indoors to prevent freeze damage.
3. **Well assessment:** If property has an existing well, have it tested for bacteria, nitrates, and local contaminants. Assess whether a hand pump can be installed alongside existing electric pump.
4. **Winter planning:** Transition to stored reserves and treated cistern water November–March; plan for snowmelt collection in late February/March as supplemental source.

### Phase 3 — Scale (Months 6–24)

**Goal:** Community water infrastructure serving 20–50 households.

1. **Community water audit:** Map all existing water sources (wells, springs, surface water, existing cisterns) within 1-mile radius of community center. Identify 1–2 high-quality sources for shared system.
2. **Spring box or community well:** If spring is available and elevation permits, design and construct gravity-fed distribution. If no spring, evaluate community drilled well with hand pump installation.
3. **Water governance document:** Establish written rules for access, testing schedule, contamination response, and maintenance responsibilities before first community use.
4. **Cross-domain dependencies:** Water systems integrate directly with Food Preservation (water for canning, sanitation), Community Health (waterborne illness prevention, triage), and Infrastructure Maintenance (pipe repair, pump maintenance). These domains must coordinate on resource allocation.

---

## References

### EPA and Federal Water Guidance
[1] FEMA / Ready.gov. (2024). *Water*. https://www.ready.gov/water

[2] WHO. *Technical Notes on Drinking-Water, Sanitation and Hygiene in Emergencies — How Much Water is Needed?* https://cdn.who.int/media/docs/default-source/wash-documents/who-tn-09-how-much-water-is-needed.pdf

[3] NOAA National Centers for Environmental Information. (2024). Referenced in: https://www.drought.gov/drought-status-updates/drought-status-update-midwest-2026-03-26

[4] WaterCache. (2024). *Rainwater Harvesting Calculator, Formulas, and Equations*. https://www.watercache.com/resources/rainwater-collection-calculator

[5] World Water Reserve / NTO Tank. (2026). *Rainwater Harvesting Laws by State*. https://worldwaterreserve.com/is-it-illegal-to-collect-rainwater/; https://www.ntotank.com/blog/rainwater-harvesting-laws-regulations-and-rights-by-us-state

[6] WaterCache. (2024). *Rainwater Harvesting 101 — How-To Collect Rainwater Guide*. https://www.watercache.com/education/rainwater-harvesting-101

[7] Enduraplas. (2024). *How to Prevent Your Water Tank From Freezing In Winter*. https://blog.enduraplas.com/water-storage-rain-harvesting/how-to-prevent-your-water-tank-from-freezing-in-winter; Tank Depot: https://www.tank-depot.com/blog/how-to-prevent-a-water-tank-from-freezing-in-winter

[8] EPA. (2024). *Home Drinking Water Filtration Fact Sheet*. https://www.epa.gov/ground-water-and-drinking-water/home-drinking-water-filtration-fact-sheet

[9] EPA. (2024). *Emergency Disinfection of Drinking Water*. https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water

[10] Wikipedia / SODIS. *Solar water disinfection — SODIS*. https://en.wikipedia.org/wiki/Solar_water_disinfection; WHO recommendation via: https://sswm.info/sswm-solutions-bop-markets/affordable-wash-services-and-products/affordable-water-supply/sodis

[11] Dani's Midlife Homestead. (2024). *How to Make a Berkey-Style Water Filter*. https://danismidlife.com/how-to-make-a-berkey-style-water-filter/; Mom With a Prep: https://momwithaprep.com/homemade-berkey/

[12] CAWST. (2009). *Household Water Treatment and Safe Storage Fact Sheet: Biosand Filter*. https://sswm.info/sites/default/files/reference_attachments/CAWST%202009%20Biosand%20Filter%20Fact%20Sheet%20academic_1.pdf; Wikipedia: https://en.wikipedia.org/wiki/Biosand_filter

[13] CDC. (2024). *How to Create an Emergency Water Supply*. https://www.cdc.gov/water-emergency/about/how-to-create-and-store-an-emergency-water-supply.html

[14] USGS. (2024). *Domestic (Private) Supply Wells*. https://www.usgs.gov/mission-areas/water-resources/science/domestic-private-supply-wells; *Contamination in U.S. Private Wells*: https://www.usgs.gov/water-science-school/science/contamination-us-private-wells; *Where to Get Well Water Tested*: https://www.usgs.gov/faqs/where-can-i-get-my-well-water-tested

[15] Referenced in: https://permies.com/t/69613/large-tank-freezing-zone-Wisconsin (Zone 4b/5 hand pump discussion)

[16] Penn State Extension. (2024). *Shock Chlorination of Wells and Springs*. https://extension.psu.edu/shock-chlorination-of-wells-and-springs; University of Nebraska-Lincoln: https://go.unl.edu/shockclorination

[17] EPA. (2024). *National Primary Drinking Water Regulations*. https://www.epa.gov/ground-water-and-drinking-water/national-primary-drinking-water-regulations

[18] CDC / EPA — cyanobacteria toxin information (referenced via general EPA guidance): https://www.epa.gov/ground-water-and-drinking-water/national-primary-drinking-water-regulations

[19] SSWM / Niskanen. (2003). *The Design, Construction, and Maintenance of a Gravity-Fed Water System*. https://sswm.info/sites/default/files/reference_attachments/NISKANEN%202003.%20Design,%20construction%20and%20maintenance%20of%20a%20gravity-fed%20water%20system.pdf

[20] InspectApedia. (2024). *Spring Water Protection: Boxes or Structures for Drinking Water Springs*. https://inspectapedia.com/water/Spring_Box_Construction.php

### Additional Supporting Sources
[21] Safecastle. (2024). *How Many Gallons of Water Per Person Per Day? Emergency Planning Guide*. https://www.safecastle.com/blogs/safecastle-blog/how-many-gallons-of-water-per-person-per-day-emergency-planning-guide

[22] Survival Frog. (2024). *Stocking and Storing Survival Water: How Much Do You Really Need?* https://www.survivalfrog.net/blogs/survival/stocking-and-storing-survival-water-how-much-do-you-really-need

[23] DisasterPrepCalc. (2024). *Water Storage Calculator*. https://disasterprepcalc.com/calculators/water-storage-calculator

[24] NTO Tank. (2024). *Rain Tanks — How Much Rainwater Can I Collect?* https://www.ntotank.com/blog/how-much-rainwater-can-i-collect-with-rainwater-harvesting

[25] Rain Brothers. (2024). *How to Determine Your Rainwater Harvesting Tank Size*. https://www.rainbrothers.com/how-to-size-your-rain-harvesting-system

[26] Oklahoma State University Extension. (2024). *Design of Rainwater Harvesting Systems in Oklahoma*. https://extension.okstate.edu/fact-sheets/design-of-rainwater-harvesting-systems-in-oklahoma.html

[27] Texas Water Newsroom. (2024). *How to Build a High-Volume Residential Rainwater Harvesting System*. https://texaswaternewsroom.org/articles/how_to_build_a_high-volume_residential_rainwater_harvesting_system.html

[28] AquaBarrel. (2024). *What Size Cistern Do I Need?* https://www.aquabarrel.com/what-size-cistern

[29] NTO Tank. (2024). *How to Protect a Rainwater Tank from Freezing*. https://www.ntotank.com/blog/how-to-protect-a-rainwater-tank-from-freezing

[30] GoToTanks. (2024). *How to Keep the Water in a Plastic Storage Tank from Freezing*. https://gototanks.com/plastic-storage-tanks/how-to-keep-the-water-in-a-plastic-storage-tank-from-freezing.html

[31] Powerblanket. (2024). *Prevent Water Tank Freezing: Effective Solutions for Winter Protection*. https://www.powerblanket.com/blog/how-to-keep-water-tanks-from-freezing/

[32] Polyguard. (2024). *Outdoor Water Tank Insulation Guide*. https://polyguard.com/blog/outdoor-water-tank-insulation

[33] Cunningham Tank and Tower Services. (2024). *Water Tank Freeze Protection*. https://www.cunninghaminc.org/water-tank-freeze-protection-how-to-prevent-freezing-and-damage/

[34] SSWM. (2024). *UV Treatment / Solar Disinfection (SODIS)*. https://www.akvopedia.org/wiki/UV_treatment_/_Solar_disinfection_(SODIS)

[35] ScienceDirect. *UV dosimetry for solar water disinfection (SODIS) carried out in different plastic bottles and bags*. https://www.sciencedirect.com/science/article/abs/pii/S0925400514014014

[36] SSWM. (2024). *SODIS*. https://sswm.info/sswm-solutions-bop-markets/affordable-wash-services-and-products/affordable-water-supply/sodis

[37] ScienceDirect. *A critical overview of household slow sand filters for water treatment*. https://www.sciencedirect.com/science/article/abs/pii/S0043135421010642

[38] World Water Reserve. (2024). *Using the BioSand Water Filter for Off-Grid Living*. https://worldwaterreserve.com/biosand-water-filter/

[39] CAWST / WASH Resources. *Biosand Filter*. https://washresources.cawst.org/en/topics/69af3832/bsf

[40] Engineering for Change. *Berkey Ceramic Filters*. https://www.engineeringforchange.org/solutions/product/berkey-ceramic-filters/

[41] Biology Insights. (2024). *Does Bleach Purify Water? A Step-by-Step Guide*. https://biologyinsights.com/does-bleach-purify-water-a-step-by-step-guide/

[42] Salt & Prepper. (2024). *Bleach to Water Ratios for Emergency Disinfection*. https://www.saltandprepper.com/learn/water/bleach-water-ratios

[43] GridWright. (2024). *Bleach to Water Ratio: The Definitive Purification Chart*. https://gridwright.com/blog/bleach-water-ratio

[44] Alaska DEC. (2024). *Emergency Disinfection of Drinking Water*. https://dec.alaska.gov/eh/dw/resources/emergency-disinfection-drinking-water/

[45] USGS. (2024). *General Facts and Concepts about Ground Water*. https://pubs.usgs.gov/circ/circ1186/html/gen_facts.html

[46] USGS. (2024). *National Ground-Water Monitoring Network*. https://www.usgs.gov/apps/ngwmn/index.jsp

[47] Wisconsin DNR. (2024). *Look Up Groundwater and Well Data*. https://dnr.wisconsin.gov/topic/Groundwater/Data.html

[48] UF of Florida IFAS Extension. (2024). *Private Wells 101: Bacterial Contamination and Shock Chlorination*. https://ask.ifas.ufl.edu/publication/SS700

[49] UGA CAES Field Report. (2024). *Disinfecting Your Well Water: Shock Chlorination*. https://fieldreport.caes.uga.edu/publications/C858-4/disinfecting-your-well-water-shock-chlorination/

[50] Science Insights. (2024). *How to Kill Bacteria in Well Water: Step by Step*. https://scienceinsights.org/how-to-kill-bacteria-in-well-water-step-by-step/

[51] ResearchGate. *Gravity-Fed Water Systems for Developing Communities*. https://www.researchgate.net/publication/281647055_Gravity-Fed_Water_Systems_for_Developing_Communities

[52] ResearchGate. *Analysis of Spring Development and Gravity Flow System to Capture Water for Local Communities*. https://www.researchgate.net/publication/322270463_Analysis_of_Spring_Development_and_Gravity_Flow_System_to_Capture_Water_for_Local_Communities

[53] EPA. (2024). *WaterSense Guide to Selecting Water Treatment Systems*. https://www.epa.gov/system/files/documents/2024-11/ws-products-home-water-treatment-guide_508.pdf

[54] EPA. (2024). *Surface Water Treatment Rules*. https://www.epa.gov/dwreginfo/surface-water-treatment-rules

[55] Homestead Projects. (2024). *Gravity-Fed Water Distribution System*. https://homesteadprojects.org/projects/gravity-fed-water-system/

[56] Salt & Prepper. (2024). *Rainwater Collection Legality by State*. https://www.saltandprepper.com/learn/water/rainwater-legality-by-state

[57] RediscoverRural. (2026). *Rainwater Harvesting Laws by State — What's Legal & How to Start*. https://rediscoverrural.com/rainwater-harvesting-laws-by-state/

[58] Reality Studies. (2026). *Emergency Water Disinfection: Boiling, Bleach & Filters*. https://www.realitystudies.co/p/emergency-water-disinfection-guide-2025
