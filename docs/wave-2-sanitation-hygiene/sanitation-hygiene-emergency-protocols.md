---
title: "Sanitation and Hygiene: Emergency and Low-Resource Protocols"
domain: sanitation-hygiene
phase: "5.2 Wave 2"
wave: 2
domain_number: 3
status: production-ready
confidence: 87%
word_count: ~9600
license: CC-BY-4.0
last_updated: 2026-07-05
author: "Open-Repo Project"
sanitation_subtypes:
  - pit_latrine
  - composting_toilet
  - handwashing
  - solid_waste
  - emergency_hygiene
cross_links:
  - WAVE_0_DOMAIN_1_WATER_ASSESSMENT_AND_TESTING.md
  - WAVE_0_DOMAIN_2_RAINWATER_HARVESTING_AND_STORAGE.md
  - WAVE_0_DOMAIN_4_WASTEWATER_AND_GREYWATER_SYSTEMS.md
  - WAVE_1_COMPOSTING_AND_SOIL_AMENDMENT.md
  - WAVE_2_DOMAIN_2_SMALL_SCALE_LIVESTOCK.md
sources:
  - "UNHCR WASH Manual 8th Edition (March 2026): https://www.unhcr.org/sites/default/files/2026-03/unhcr-wash-manual-8th-edition-march-2026.pdf"
  - "Sphere Handbook WASH Standards: https://handbook.spherestandards.org"
  - "CAWST WASH Resources: https://washresources.cawst.org"
  - "Humanitarian Sanitation Hub: https://sanihub.info"
  - "MSF Medical Guidelines ORS: https://medicalguidelines.msf.org"
  - "WHO Communicable Diseases After Natural Disasters: https://cdn.who.int/media/docs/default-source/documents/emergencies/communicable-diseases-following-natural-disasters.pdf"
  - "Humanure Handbook: https://humanurehandbook.com"
  - "Global Handwashing Partnership: https://globalhandwashing.org"
  - "UNICEF Sudan Emergency WASH Guidelines: https://www.unicef.org/sudan/media/1031/file/Emergency-Technical-Guidelines-2017.pdf"
  - "PMC Tippy-Tap Systematic Review: https://pmc.ncbi.nlm.nih.gov/articles/PMC7316639/"
  - "PMC Post-Disaster Communicable Disease Review: https://pmc.ncbi.nlm.nih.gov/articles/PMC3263111/"
  - "PMC Ash Handwashing Review: https://pmc.ncbi.nlm.nih.gov/articles/PMC7192094/"
---

<!-- License: Creative Commons Attribution 4.0 International (CC BY 4.0) -->
<!-- You are free to share and adapt this material for any purpose, provided appropriate credit is given. -->
<!-- Attribution: Open-Repo Project, 2026. https://github.com/open-repo -->

# Sanitation and Hygiene: Emergency and Low-Resource Protocols

## Introduction

Sanitation is the mechanism by which human waste is separated from human contact. When that mechanism fails — in floods, earthquakes, displacement crises, infrastructure collapse, or simply in rural settings that never had sewage infrastructure — the consequences arrive faster than most practitioners expect. Within 48 hours of a large displacement event without adequate sanitation, open defecation begins contaminating water sources. Within two weeks, diarrheal disease rates in an unserved camp frequently exceed 10 cases per 10,000 people per day — the WHO emergency threshold that triggers a formal outbreak response.

This domain is the second half of the WASH (Water, Sanitation, and Hygiene) framework that began in Wave 0 of this library. Wave 0 covered water sourcing, testing, treatment, and basic greywater management. This domain covers what happens to human waste, how hygiene is maintained when water is scarce, how disease transmission is interrupted, and how the most vulnerable people in a displacement setting — pregnant women, infants, the elderly, and people with disabilities — are specifically protected.

The content is organized for practitioners: WASH coordinators, community health workers, NGO field staff, emergency responders, and community members preparing for or responding to disruption. It is not a guide for licensed engineers designing permanent municipal infrastructure. It covers the gap between nothing and a functional sanitation system — the gap that determines whether a community stays healthy through a crisis.

**Reader assumptions.** No engineering background is required. You should be able to read a measuring tape, mix cement, dig a pit, and give clear instructions to a small work group. Detailed technical specifications (pit dimensions, concrete mix ratios, vent pipe diameters) are provided because imprecision in these numbers causes latrine collapse, groundwater contamination, and disease. These are not suggestions; they are field-validated minimums from UNHCR, WHO, Sphere Standards, CAWST, and MSF field experience across hundreds of emergency settings.

**A note on units.** Volumes are given in liters, distances in meters, temperatures in Celsius. Field conversions: 1 liter = approximately 1 quart; 1 meter = approximately 3.3 feet; 55°C ≈ 130°F.

---

## Section 1: Emergency Water Sanitation Assessment

*Note: This section bridges directly to Wave 0 Domain 1 (Water Assessment and Testing). If water testing protocols are needed, cross-reference that document. This section covers the rapid triage decisions specific to sanitation-linked water contamination.*

### 1.1 The Fecal-Oral Cycle: What You Are Interrupting

The diseases that kill people after sanitation failure are transmitted by a single mechanism: fecal matter from an infected person reaching the mouth of another person. The routes are:

- Contaminated drinking water (most significant in mass displacement)
- Contaminated food handled by unwashed hands
- Contaminated surfaces — especially shared items like food utensils, water containers, and door handles
- Direct person-to-person contact in crowded, low-hygiene settings

Understanding this cycle is operationally important because every sanitation intervention is designed to cut one or more of these routes. A pit latrine cuts the water contamination route. Handwashing facilities cut the hand-to-mouth route. Food hygiene cuts the food route. A comprehensive WASH program cuts all three simultaneously, which is why partial interventions consistently underperform relative to integrated ones.

**Confidence: 92% — well-established epidemiological consensus across WHO, CDC, and MSF field reporting.**

### 1.2 Rapid Water Quality Triage

Before sanitation infrastructure is established, the first 24–48 hours require rapid assessment of whether water sources have been contaminated by human waste. This is particularly urgent after floods, which physically mix surface water with latrine contents, and after earthquakes, which crack sanitation infrastructure and allow infiltration to groundwater.

**Field assessment checklist (no laboratory equipment required):**

1. **Source identification** — Map all water sources in use. For each source, note: type (well, surface, piped, collected rain), recent history (flooding, infrastructure damage, proximity to defecation areas).

2. **30-meter exclusion check** — No water source should be within 30 meters of a latrine, pit, or defecation area. If the distance is less than 30 meters, treat that source as contaminated until laboratory testing confirms otherwise. In sandy or gravel soils, increase this to 50 meters (faster infiltration rates).

3. **Groundwater depth check** — The bottom of any pit latrine must sit at least 1.5 meters above the seasonal high groundwater table. If you cannot confirm this, default to treating local well water as potentially contaminated.

4. **Organoleptic signs** — Color, odor, and turbidity are not reliable indicators of contamination with fecal pathogens (Vibrio cholerae is odorless in water), but visible contamination (brown color, sewage smell) is a definitive disqualification for use without treatment. Do not let "clear water" create false confidence.

5. **Upstream/downstream mapping** — Identify the direction of flow for any surface water. Latrine sites must be located downstream and downslope from all water collection points.

**Minimum safe water quantities per person per day (Sphere Standards):**

| Phase | Minimum | Target |
|---|---|---|
| Acute emergency (first 48–72 hours) | 3 liters (survival) | 7.5 liters |
| Ongoing emergency | 7.5 liters | 15 liters |
| Stable displacement setting | 15 liters | 20 liters |

Note: These quantities include drinking, cooking, and basic hygiene. Laundry, bathing, and livestock are not included in these minimums. Handwashing alone at the tippy-tap scale uses only 50 ml per wash — a critical fact for water rationing decisions.

### 1.3 Prioritizing Treatment When Supply Is Constrained

When water must be rationed, allocation priority is:

1. Drinking water for infants, young children, pregnant and lactating women, and patients with diarrhea or fever — these groups are highest risk for fatal dehydration.
2. Food preparation water — all water used to cook must meet drinking water standards.
3. Handwashing water — even grey/recycled water (from dish washing or light laundry) is acceptable for handwashing if soap is available, because the soap does the pathogen removal work, not the water purity.
4. General hygiene and laundry — lowest priority when supply is constrained.

For water treatment methods in resource-limited settings, refer to Wave 0 Domain 3 (Chemical Disinfection, Boiling, and Filtration).

*Sources: Sphere Standards WASH chapter; WHO Technical Notes on Water, Sanitation and Hygiene in Emergencies (who.int); UNHCR WASH Manual 8th Edition, March 2026.*

---

## Section 2: Waste Management and Latrine Systems

### 2.1 The Latrine Decision Tree

Before building any latrine, three site assessment questions determine which system is appropriate:

**Question 1: What is the groundwater depth?**
- More than 3 meters below surface: standard pit latrine is viable
- 1.5–3 meters: lined pit with impermeable base required (or composting toilet)
- Less than 1.5 meters: pit latrines are contraindicated; use composting toilet, container-based toilet, or above-ground sealed vault

**Question 2: What is the soil type?**
- Loamy or sandy: standard unlined pit bottom is fine (percolation is needed)
- Rocky or highly compacted: pit excavation may be impossible; earthbag or prefab alternatives
- High clay content: low percolation means pits fill faster; size up by 30%

**Question 3: How long is the expected use period?**
- Under 2 weeks: trench latrine or cat-hole field latrine (see Section 5.1)
- 2 weeks to 6 months: single pit latrine
- Over 6 months or permanent: ventilated improved pit (VIP) latrine or composting toilet

### 2.2 Single Pit Latrine

The single pit latrine is the fastest deployable permanent sanitation solution when soil conditions permit. It requires no electricity, no chemicals, and minimal specialized materials.

**Siting requirements:**
- Minimum 30 meters from any water source (well, spring, surface water collection point)
- Minimum 6 meters from any dwelling
- At least 15 meters from a cooking area or food storage
- Downslope and downwind from the dwelling and water source
- The pit bottom must be at least 1.5 meters above the seasonal high groundwater table

**Pit sizing calculation:**

The standard accumulation rate is 40–60 liters per person per year using wet cleansing (water). Using dry cleansing materials (leaves, paper), the rate rises to 90 liters per person per year. Use the higher figure when material type is uncertain.

Formula for minimum pit volume in liters:
```
Pit Volume = (Users × 90 L/year × Design Life in years) × 1.3 safety factor
```

Example: A household of 6 people, 5-year design life:
6 × 90 × 5 × 1.3 = 3,510 liters minimum

Practical pit dimensions yielding approximately 3,500 liters: 2.5 meters deep × 1.3 meters diameter (approximately 1 meter × 1 meter square cross-section is acceptable if round excavation is impractical).

**Standard minimum dimensions (Sphere / UNHCR):**
- Minimum depth: 3 meters
- Minimum diameter: 1 meter
- Minimum volume: 1,000 liters

One pit 3 meters deep and 1 meter in diameter, serving 50 users with dry cleansing materials, fills in approximately 6 months. For family-scale use (6 people), the same pit provides approximately 4–5 years of service.

**Pit lining:**
- The upper 1 meter of the pit wall (from slab level down) must be lined to prevent collapse and to stop rodents from burrowing in.
- The bottom of the pit remains unlined to allow urine and liquid to infiltrate the soil.
- Lining materials: mortared brick (most durable), concrete rings, rot-resistant timber, bamboo, or stabilized earth (in low-rainfall areas).
- Lining must extend at least 40 cm above slab level.

**Slab construction (on-site concrete):**

Materials for a 1.1 meter × 1.1 meter slab:
- Portland cement: 5 kg
- Coarse sand: 10 kg
- Fine gravel or crushed stone: 15 kg
- Water: approximately 3 liters (mix should hold shape when squeezed, not slump)
- Reinforcing: two 6mm steel rods crossing at center, or chicken wire laid flat

Procedure:
1. Build a mold from timber boards or earthen banks, slightly larger than the pit opening.
2. Mix cement, sand, and gravel dry first, then add water gradually until the mix is stiff but workable.
3. Pour a 2 cm base layer into the mold.
4. Lay reinforcement across center, then pour remaining 6–8 cm of mix over reinforcement. Total slab thickness: 8–10 cm.
5. Place the foot rests and keyhole-shaped drop hole form before the mix sets (drop hole: 25 cm × 35 cm or circular 30 cm diameter).
6. Cover with wet cloth or plastic for 7 days of curing. Do not load the slab until 28 days have elapsed.

The slab must sit at least 10 cm above ground level to prevent rainwater runoff from entering the pit.

**Superstructure:**
Build for privacy and safety. Minimum requirements: full-height walls on three sides (roof optional), a lockable or self-latching door, and ventilation at the top of the back wall. Materials: any locally available option — timber, bamboo, woven grass, metal sheeting, earthen block. Place the superstructure door on the shaded side (away from prevailing wind) for fly and odor management.

**Confidence: 88% — specifications drawn from Sphere Handbook, UNHCR emergency standards, and UNICEF Ghana Technical Guidelines. Pit sizing accumulation rates are field-measured values, not theoretical.**

### 2.3 Ventilated Improved Pit (VIP) Latrine

The VIP latrine solves the two main complaints about pit latrines: odor and flies. Both problems are solved by the same mechanism — a properly installed vent pipe. This makes the VIP latrine strongly preferred over a basic pit latrine for any installation expected to serve more than a week.

**How the fly trap mechanism works:**

Flies enter the pit through the drop hole (drawn by waste odor). The interior of the superstructure is kept dark — critical — by keeping the drop hole covered with a lid and using a dark interior. Flies, following light to escape, fly upward into the vent pipe where a fly screen traps them. They die there. Simultaneously, air flows across the latrine opening, down into the pit, and up through the vent pipe, carrying odors out. Result: an essentially odor-free, fly-minimizing latrine.

**Vent pipe specifications:**
- Minimum internal diameter: 11 cm (smaller pipes clog with dust and restrict airflow)
- Height: extends at minimum 30 cm above the highest point of the superstructure roof (taller is better in low-wind areas)
- Material: PVC pipe, metal pipe, masonry chimney, or hollowed bamboo (bamboo effective for 3–5 years before replacement)
- Color: paint black on the exterior to absorb solar heat; heat difference between cool pit and warm pipe creates additional updraft in low-wind conditions
- Fly screen: fixed to the top of the pipe opening; mesh size 1.2–1.5 mm (large enough to avoid dust clogging, small enough to trap flies)

**Verification test:** Hold a smoking stick or smoldering cloth at the drop hole of the latrine. Smoke should be visibly drawn downward into the pit. If smoke drifts up toward the user, airflow is reversed and the vent pipe is obstructed or too short.

**Orientation:** Position the vent pipe on the sunny side of the superstructure to maximize solar heating of the pipe. The superstructure opening (door/entrance) faces away from the prevailing wind so that wind accelerates airflow across the drop hole.

**Site requirements:** VIP latrines need modest wind exposure. Do not build in completely sheltered depressions or against wind-blocking walls.

**Maintenance:**
- Clean fly screen monthly (or when noticeably clogged with debris)
- Replace fly screen when any hole larger than 2 mm develops
- Keep interior dark at all times (the darkness is structural to the fly trap; painting interior walls black is not required but improves function)
- Monitor fill level quarterly; begin planning pit decommissioning at 75% full

*Sources: Humanitarian Sanitation Hub VIP Latrine specification (sanihub.info); CAWST VIP Latrine Fact Sheet; IRCWASH VIP Latrine Builders Guide.*

### 2.4 Composting Toilets

Composting toilets convert human waste into pathogen-safe compost through the same biological processes documented in Wave 1's hot composting section. The key difference from a pit latrine: waste is not buried or infiltrated into the soil — it is composted in an above-ground or raised chamber.

**When composting toilets are appropriate:**
- High groundwater tables that prohibit pit latrines
- Rocky soils that prohibit pit excavation
- Settings where agricultural use of finished compost is desired
- Cold climates where thermophilic composting is still achievable with proper insulation

**When they are not appropriate:**
- Acute emergency phase (require weeks to set up correctly and months to produce safe compost)
- Settings without access to cover material (carbon) on an ongoing basis
- Communities where acceptance of humanure as agricultural input is low (requires discussion and consent)

**Pathogen safety: the thermophilic requirement**

This is the most important technical point in composting toilet operation. A composting pile that never reaches thermophilic temperatures is not safe for agricultural use — it is decomposed waste, not sanitized compost. The minimum validated parameters are:

- 55°C maintained for at least 14 consecutive days, OR
- 60°C maintained for at least 7 consecutive days

These temperatures kill Ascaris eggs (among the most heat-resistant human pathogens in fecal matter), Salmonella, E. coli O157:H7, Vibrio cholerae, and Hepatitis A virus. If thermophilic temperatures are not achieved, an additional 12-month aging period at ambient temperature is required before agricultural use.

A hand-inserted compost thermometer is the only reliable way to verify temperature. Field judgment ("the pile feels warm") is not sufficient.

**Two-chamber (alternating) design:**

The two-chamber design is the most practical household-scale composting toilet for continuous-use settings. One chamber receives fresh inputs for approximately 9 months; it then rests and composts for an additional 9 months while the second chamber receives fresh inputs. Total cycle: 18 months from fresh waste to safe compost for a family of four.

Chamber dimensions for a family of four (Humanure Handbook guidelines):
- Each chamber: approximately 1 cubic meter (1m × 1m × 1m) minimum
- Chambers may be constructed of concrete block, brick, or treated timber
- The bottom must be permeable (earth, gravel, or drainage holes) to allow liquid drainage into the soil
- Chambers must be covered and protected from rain (rain dilutes compost and inhibits thermophilic heating)

**Cover material (carbon source):**
Every deposit of waste must be immediately covered with a generous layer of high-carbon material. The smell test is reliable: if there is any odor after covering, add more cover material. Options by availability:

| Material | Notes |
|---|---|
| Dry straw or hay | Excellent; abundant in agricultural settings |
| Dry leaves | Good; collect in autumn, store dry |
| Wood shavings or sawdust | Excellent; small particle size decomposes faster |
| Dry grass clippings | Acceptable if fully dry (green clippings are high nitrogen) |
| Rice hulls | Acceptable; very slow to decompose |
| Shredded cardboard | Acceptable; avoid glossy or colored printing |

Do not use soil as cover material — it creates anaerobic pockets and suppresses thermophilic activity.

**Urine diversion:**
Urine diversion (separate collection of urine before it enters the compost chamber) significantly improves composting performance by reducing moisture content. Diverted urine, diluted 1:8 with water, is an effective liquid fertilizer safe for application to non-food-contact crop surfaces (soil, not leaves). Urine diversion is optional for basic household systems but should be considered for higher-volume community systems.

**Agricultural use of finished compost:**
Compost that has verifiably reached thermophilic temperatures (documented with a thermometer) for the required periods, and has subsequently completed a 9-month rest period, is safe for agricultural use on any crop. Compost that has not met the temperature standard should be restricted to non-edible crops or used only on the base of trees, never on vegetable beds.

*Sources: Humanure Handbook 4th Edition (humanurehandbook.com); PMC Thermophilic Composting of Human Feces study (PMC8895236); Wave 1 Composting Domain cross-reference.*

### 2.5 Portable and Emergency-Phase Sanitation

During the first 24–72 hours of a displacement event or infrastructure failure, permanent latrine construction is not possible. The following options buy time:

**Bucket toilets with lined containment:** Standard 20-liter buckets with tight-fitting lids, lined with a bag. Contents are sealed and transferred to a containment point for later treatment. Requires daily management — this is the highest-maintenance option. Suitable only when committed management personnel are available.

**Trench latrines (group use, short duration):** A trench 30 cm wide, 20–30 cm deep, and 3.5 meters long serves approximately 100 people for one day. Depth increases by 30 cm with each day of use. Cover contents with a thin layer of excavated soil after each use. Maximum duration: 5–7 days. Siting requirements same as for pit latrines (30 meters from water, downslope).

**Commercial chemical or composting portable toilets:** Where procurement is possible, these are the fastest deployable option. Management is simplified. Primary constraint is supply chain — in a large regional emergency, rental equipment quickly becomes unavailable. Pre-positioned stock or procurement relationships with local suppliers are necessary for rapid deployment.

**Sphere Standards minimum requirement:** No latrine should be used by more than 50 persons during the initial emergency phase (measured per drophole). In the post-emergency stabilization phase, no toilet should serve more than 20 persons. These are starting thresholds — priority is rapid deployment, then iterative improvement to the 20-person standard.

---

## Section 3: Hygiene Protocols in Resource Scarcity

### 3.1 Hand Hygiene: The Highest-Impact Single Intervention

The epidemiological evidence base for handwashing is among the most robust in public health. Handwashing with soap reduces diarrheal disease by up to 48% and acute respiratory infections by up to 27% (Global Handwashing Partnership, meta-analysis of 55+ studies). In emergency settings where diarrhea is responsible for 25–40% of child deaths, handwashing is not a comfort measure — it is a primary clinical intervention.

The critical moments for handwashing (adapted from WHO Five Moments for community emergency context):

1. **Before preparing or eating food** — highest-impact single moment for fecal-oral disease interruption
2. **After defecation** — essential; this is where fecal contamination begins its transmission chain
3. **After handling an ill person** — especially important during diarrheal outbreak
4. **After handling infant or child waste** — child feces are as infectious as adult feces; "it is small so it is safe" is a dangerous misconception
5. **Before breastfeeding** — protects infant from pathogen transfer via skin

**The water efficiency problem:** Conventional handwashing at a tap uses 500–1,000 ml per wash. In a setting where each person's total daily water allocation is 7.5–15 liters, conventional handwashing is impossible to sustain across five critical moments. The solution is not to reduce handwashing — it is to use water-efficient delivery systems.

### 3.2 Tippy-Tap Construction

The tippy-tap is a foot-operated, nail-activated handwashing station that delivers approximately 50 ml of water per wash — a 90–95% reduction from conventional tap use. It was developed for use in East Africa and has been validated in systematic review (PMC7316639) across multiple countries, with adoption rates exceeding 80% in structured rollout programs.

**Materials (no tools required for basic version):**

- One 5-liter plastic jerrycan or bottle with tight-fitting cap
- Two upright poles or sticks, 1.5 meters tall (bamboo, timber, metal rebar)
- One horizontal cross-stick, approximately 80 cm long
- Rope or wire for lashing
- One nail or nail-substitute (small stick, thorn, pin)
- Soap (bar or liquid) suspended nearby on rope or wire
- Optional: small stick or stone as foot pedal for nail activation

**Construction procedure:**

1. Drive two upright poles into the ground approximately 60 cm apart and 60 cm in front of a latrine or cooking area.
2. Lash the horizontal cross-stick to both uprights at approximately chest height (1.2–1.3 m for adults).
3. Punch a small hole (2–3 mm diameter) through the cap of the jerrycan. Replace cap.
4. Insert a nail through the hole in the cap. When the nail is pressed downward (by foot on a foot pedal) it opens the hole; when released, it re-seals.
5. Hang the jerrycan upside down from the horizontal cross-stick using rope. Adjust height so the water stream falls conveniently for handwashing.
6. Suspend soap on a cord attached to the cross-stick, within arm's reach of the water stream.
7. Set up a flat stone or tied foot pedal at ground level connected to the nail by a cord, so a user can tip the water by foot without using the hands being washed.

**Alternate simplified version (nail not required):** Hang the jerrycan upside down with a simple punctured cap hole. The hole diameter (approximately 3 mm) creates a slow drip sufficient for handwashing when the can is tilted slightly by touching it.

**Water refill:** A 5-liter can serves 15–30 handwashing events. In a family of 6 with 5 handwashing moments per person per day, refill is needed roughly once daily — a very low management burden.

**Demonstrated effectiveness:** A systematic review found tippy-tap installation increased handwashing after toilet use from 5.5% to 65%, and soap use rose from 13.5% to 84.5% in school settings. Adoption exceeded 80% in community settings with minimal promotion.

### 3.3 Soap Alternatives When Soap Is Unavailable

Soap works by reducing surface tension, allowing water to lift pathogen-laden oil films off skin. When soap is unavailable:

**Wood ash:** The only validated alternative. Ash creates an alkaline solution (pH approximately 9–11) that disrupts cell membranes of bacteria and may inactivate some viruses. WHO classifies ash as "last resort" when soap is unavailable — it is likely more effective than water-only handwashing but evidence for virus inactivation is limited. Use dry, cooled ash from wood fires only. Procedure: wet hands, rub ash vigorously across all surfaces for 20 seconds, rinse with water.

**Soapy water (diluted soap from any source):** If bar soap is too scarce for individual use, dissolve one bar of soap in 5 liters of water and dispense from the tippy-tap. Diluted soap retains significant antimicrobial function.

**Chlorine solution (0.05% concentration):** Works as a last resort for surface disinfection and can be used for hand disinfection in outbreak response settings. Causes skin dryness with extended use. WHO recommends only as an interim measure. Preparation: 1 ml of 5% household bleach per liter of water.

**Important:** Hand sanitizer (alcohol gel) is effective against most bacterial pathogens and enveloped viruses but does NOT reliably kill norovirus or Cryptosporidium, which are significant diarrheal pathogens in emergency settings. Handwashing with water and soap or ash remains superior for broad-spectrum effectiveness.

*Sources: Global Handwashing Partnership FAQ; PMC ash handwashing review (PMC7192094); WHO Guidelines on Hand Hygiene in Healthcare; MSF field guidance.*

### 3.4 Disease Vectors in Crowded Shelter

Crowded shelters create specific sanitation transmission risks beyond the fecal-oral route:

**Respiratory droplet transmission:** Measles, influenza, and meningococcal disease spread rapidly in crowded indoor settings. Sanitation's role here is indirect but important: malnourished children weakened by diarrheal disease are more susceptible to respiratory infection. Reducing diarrhea incidence reduces overall disease burden.

**Contact transmission surfaces:** Shared water containers are among the highest-risk surfaces for fecal-oral transmission. Assign individual cups for drinking. Shared cooking pots must be washed with soap between uses. The latrine door handle, water container spigot, and food preparation surfaces should be disinfected daily with diluted chlorine (0.1%) during outbreak conditions.

**Vector-borne transmission:** Standing water from poor drainage breeds Aedes and Anopheles mosquitoes within 7–10 days. Drainage around latrines and cooking areas is a sanitation responsibility, not only a comfort issue. Drain or cover all standing water within 50 meters of sleeping areas. During the acute emergency phase, chemical vector control (indoor residual spraying) must be coordinated with the health cluster; this is beyond field-improvised scope.

**Scabies and skin infections:** Crowding, water scarcity, and lack of bathing create conditions for scabies transmission. Scabies is not directly fecal-oral but creates breaks in skin that permit secondary bacterial infection. In scabies-endemic regions, priority for bathing water should be given to infants and young children whose skin barrier is most vulnerable.

---

## Section 4: Disease Prevention and Rapid Response

### 4.1 The Priority Diseases

The leading sanitation-linked illness categories in post-disaster and displacement settings, ranked by kill potential in under-resourced environments:

**Cholera (Vibrio cholerae):** Waterborne transmission. Onset 6 hours–5 days after exposure. Profuse rice-water diarrhea, rapid dehydration, and death within hours without oral rehydration. Case fatality rate in untreated severe cases: 25–50%. With prompt ORS: below 1%. Geographic distribution: endemic in parts of sub-Saharan Africa, South Asia, and parts of the Americas; capable of outbreak anywhere sanitation collapses. Key prevention: safe water, latrine use, and handwashing.

**Typhoid fever (Salmonella Typhi):** Fecal-oral, water, and food transmission. Onset 6–30 days. Sustained high fever, abdominal pain, rose spots. Case fatality rate without treatment: 10–30%. Key prevention: water treatment and food safety; vaccination is available (oral Ty21a or injectable Vi polysaccharide) and should be considered for outbreak settings.

**Hepatitis A and E:** Fecal-oral transmission. Hepatitis A is self-limiting in most adults but causes significant morbidity; Hepatitis E has a case fatality rate of 15–25% in pregnant women — a critical consideration for antenatal population management. Key prevention: water treatment, hand hygiene, and Hepatitis A vaccination where available.

**Shigellosis (dysentery):** Directly fecal-oral, person-to-person. Very low infectious dose (10–100 organisms sufficient for infection). Bloody diarrhea, fever, tenesmus. High risk in settings with shared water containers and poor handwashing. Key prevention: handwashing and proper latrine use.

**Cryptosporidiosis and Giardiasis:** Protozoan, waterborne and direct contact. Not killed by standard chlorination doses — requires filtration (biosand or ceramic filter, from Wave 0 Domain 5) or boiling. Cause prolonged diarrhea especially in children and immunocompromised individuals. Key prevention: water filtration.

**Confidence: 90% — established WHO/CDC epidemiological consensus; disease-specific case fatality rates are ranges from literature, not precise point estimates.**

### 4.2 Oral Rehydration: The Core Field Treatment

Oral rehydration therapy (ORT) using oral rehydration salts (ORS) is the single most impactful field-deployable medical intervention for diarrheal disease. It has reduced global cholera mortality from 25–50% to below 1% where properly applied. It requires no IV access, no electricity, and no specialized training.

**WHO ORS standard formula (packaged sachet):** One sachet in 1 liter of clean water. Prepared solution is viable for 24 hours; discard after that.

**Home preparation formula (when sachets unavailable):**
```
1 liter of clean (boiled or treated) water
6 level teaspoons (30 ml) of table sugar
0.5 level teaspoon (2.5 ml) of table salt
```
Mix until dissolved. This approximates the glucose-sodium electrolyte balance needed for intestinal absorption. The ratio must be correct — too much salt causes hypernatremia, which is dangerous. Always use level (not heaped) measures.

**Dosing protocol (adapted from MSF Medical Guidelines):**

*Prevention dose (mild diarrhea, no dehydration signs):*
- Under 2 years: 50–100 ml after each loose stool
- 2–10 years: 100–200 ml after each loose stool
- Over 10 years/adults: 200–400 ml after each loose stool

*Treatment dose (moderate dehydration — increased thirst, dry mouth, decreased urine output):*
Give 75 ml/kg body weight over 4 hours. For a 70 kg adult: approximately 5.25 liters over 4 hours. This is aggressive but necessary.

*Severe dehydration (sunken eyes, no tears, very dry mouth, skin pinch test does not return within 2 seconds, lethargy):*
Severe dehydration requires IV rehydration if available. If IV is not available, give ORS by nasogastric tube (NGT) at 20 ml/kg/hour under supervision, or by mouth in small sips if patient is conscious. Severe dehydration in infants and toddlers is a medical emergency requiring evacuation if any evacuation option exists.

**If vomiting occurs:** Stop ORS for 10 minutes. Then resume at a very slow rate (small sips, teaspoon at a time). Most patients who vomit ORS can tolerate it if given slowly enough.

**Breastfeeding:** Continue breastfeeding throughout illness. Breast milk provides hydration and immune support. Do not substitute ORS for breastfeeding in infants under 6 months.

**ReSoMal (Rehydration Solution for Malnourished children):** Standard ORS is contraindicated in severely malnourished children (MUAC below 115 mm or visible severe wasting) except in cholera. Use ReSoMal at 5 ml/kg/hour for the first 2 hours if available.

### 4.3 Field Prevention Checklist

For rapid assessment of a shelter or displacement site, this checklist identifies the highest-priority interventions:

**Water safety:**
- [ ] All drinking water treated (boiled, chemically disinfected, or filtered) — do not assume safety based on appearance
- [ ] Water storage containers have tight-fitting lids and are not shared for drinking without dedicated utensils
- [ ] Water collection point is at least 30 meters from any latrine

**Sanitation:**
- [ ] Functioning latrine with at least 1 drophole per 50 people (immediate phase) or 1 per 20 people (stabilization)
- [ ] No open defecation within 30 meters of dwellings, water sources, or food preparation areas
- [ ] Latrine area has hand hygiene facility within arm's reach (tippy-tap or equivalent)

**Hygiene:**
- [ ] Soap or ash available at each handwashing point
- [ ] Hands washed at every critical moment (5 moments above), especially before food and after defecation
- [ ] Food preparation surfaces cleaned with soap between uses
- [ ] All food covered to prevent fly contact

**Surveillance:**
- [ ] Daily count of diarrhea cases (3+ loose stools in 24 hours) among any age group
- [ ] WHO outbreak threshold: 1 case per 10,000 people per day triggers investigation; 2 cases per 10,000 triggers formal response
- [ ] Alert pathway identified: who to notify if case counts rise

**First supply priority (if resupply possible):**
ORS sachets, water purification tablets, soap bars, plastic sheeting for latrine privacy, and basic hygiene kits (toothbrush, comb, soap, menstrual supplies) — in that order of priority for disease prevention per dollar.

*Sources: WHO Communicable Diseases Following Natural Disasters guidelines; MSF Medical Guidelines ORS protocol; Sphere Handbook WASH chapter; PMC post-disaster communicable disease review (PMC3263111).*

### 4.4 Environmental Decontamination After Outbreak

When a confirmed diarrheal outbreak (cholera, Shigella, or similar) has occurred in a shelter:

**Fecal spill response:** Any fecal contamination on surfaces must be cleaned immediately using a two-step process: (1) remove visible material with disposable rag, incinerate or bury; (2) apply 0.5% chlorine solution to the contaminated surface, leave 30 minutes, wipe. The person doing this must wear gloves or use doubled plastic bags over their hands.

**Latrine disinfection:** Sprinkle dry lime (calcium hydroxide) or 2% chlorine solution into latrine pits containing confirmed cholera patient waste. This is the MSF standard for CTC (Cholera Treatment Center) operations: 2% chlorine solution added to each bucket of cholera patient feces or vomit.

**Chlorine solution preparation for decontamination:**
- 0.5% (surface disinfection): 100 ml of 5% household bleach per 900 ml water
- 2% (latrine disinfection): 400 ml of 5% household bleach per 600 ml water
- Note: chlorine degrades rapidly in sunlight; prepare fresh solutions daily and store in covered containers

---

## Section 5: Vulnerable Populations

### 5.1 Field Latrine Systems for Groups in Transit

Groups traveling or relocating who have not yet established fixed infrastructure require field sanitation protocols. These are the lightest-weight deployable systems, not suitable for use beyond 7–10 days.

**Cat-hole latrine (individual, under 5 people, 1–2 nights):**
- Dig 15–20 cm deep, approximately 15 cm in diameter
- Position at least 60 meters from the campsite, water source, and cooking area
- After use, cover with the full depth of excavated soil; lightly tamp
- One cat hole per person per day maximum

**Group trench latrine (6+ people, up to 7 days):**
- Trench dimensions: 30 cm wide, 25–30 cm deep per day of use, 3.5 meters long per 100 people per day
- Minimum distances: 30 meters from any water source, 15 meters from the camp perimeter, downslope and downwind from sleeping and cooking areas
- Cover each use with a thin layer (2–3 cm) of excavated soil
- Assign a latrine attendant whose daily task includes adding cover soil, maintaining basic privacy, and monitoring fill level
- When trench is within 10 cm of full, close it by filling completely with excavated soil, marking the location, and opening a new trench at least 5 meters away

**Privacy:** A privacy screen (tarp, cloth, vegetated windbreak) must be provided. Lack of privacy is the primary reason latrines go unused in displacement settings, particularly by women and girls. This is not a comfort consideration — it is a use-compliance factor with direct disease outcomes.

### 5.2 Menstrual Hygiene Management in Displacement

Menstrual hygiene management (MHM) in humanitarian settings is consistently under-resourced relative to its public health impact. Women and girls who cannot manage menstruation safely and privately often avoid latrine areas entirely during their period, increasing open defecation and creating safety risks. This section covers the minimum requirements for MHM in any displacement setting.

**Infrastructure requirements:**
- Latrines used by women must have: (1) internal locks or secure latching; (2) sufficient interior lighting or accessibility without artificial light; (3) a bucket with a lid or covered waste bin inside the stall for disposal of used materials; (4) water available within the latrine stall or immediately outside, not across an open space
- Washing water does not need to be treated to drinking quality for this purpose, but must not be visibly contaminated
- A clothesline or drying rack within a private area (screened from public view) is required for drying reusable materials

**Menstrual materials:**
Priority supply list from UNHCR guidance:
1. Underpants/underwear (most frequently cited unmet need)
2. Soap (for washing both hands and reusable pads)
3. Small bucket with lid (for soaking and washing)
4. Reusable cloth pads or commercial pads — both are appropriate; cloth requires washing and drying infrastructure; commercial pads require disposal infrastructure
5. Washbasin or small container for private washing

**Disposal of used materials:**
Disposal is a sanitation problem, not only a hygiene problem. Improper disposal (throwing into pit latrines, open burning) creates vector attraction and latrine clogging. Proper disposal:
- Reusable pads: rinse, soak 30 minutes in diluted chlorine (0.1%) or soapy water, wash with soap, dry in sun (UV exposure provides additional disinfection)
- Disposable pads: wrap tightly in paper, place in covered waste bin; incinerate in dedicated medical waste burn (not in open cooking fire) or in a deep burial pit at least 50 cm depth

**Girls and adolescents:** Girls aged 10–19 who have not received MHM education are at highest risk of distress and non-use of facilities. A minimum of one private MHM explanation session per week, delivered by a female community health worker, is the Sphere-recommended minimum. The emphasis should be on what is available and how to use it, not on what is unavailable.

*Sources: UNHCR WASH Manual 8th Edition (March 2026); IRC Menstrual Hygiene Management in Emergencies Toolkit; PMC Menstrual Hygiene Management in Africa scoping review (PMC11948744); PMC MHM Cox's Bazar study (PMC7912835).*

### 5.3 Pediatric Hygiene

Children under five have three specific vulnerabilities in sanitation emergencies:

**1. Fecal-oral exposure from child defecation management.** In open-defecation or transitional settings, infant and toddler feces are frequently not managed as carefully as adult waste. Child feces are as pathogenic as adult feces; in some stages of infection, more concentrated. Standard practice: all child feces disposed of in the latrine, not buried, left on ground, or thrown into drains.

**2. Higher susceptibility to dehydration.** A 10 kg child loses a proportionally much larger fraction of body weight per episode of diarrhea than an adult. Dehydration signs appear faster and progress faster. Caregivers must be specifically trained to recognize early dehydration in children:
- Decreased urine (no wet diaper in 8+ hours)
- No tears when crying
- Dry mouth and lips
- Sunken fontanelle (in infants under 18 months)
- Lethargy, decreased responsiveness

Any of these signs requires aggressive ORS administration and escalation if available.

**3. Latrine accessibility.** Standard drop-hole dimensions (25–30 cm) are dangerous for toddlers who may fall in. Options: provide a child potty (small container) that is emptied into the latrine by an adult; use a reduced-size drop hole (15 cm diameter) for child-specific latrine stalls; or fit the standard hole with a restraint rail children can hold while squatting. Do not allow young children to use latrines unsupervised.

**Nutrition-sanitation linkage:** Diarrheal disease and malnutrition create a self-reinforcing cycle. A malnourished child is more susceptible to diarrheal disease; diarrheal disease worsens malnutrition through nutrient malabsorption. In settings where both are present, sanitation interventions and nutrition support must be coordinated.

### 5.4 Elderly and Mobility-Limited Populations

Elderly adults and people with physical disabilities face specific access barriers that standard emergency sanitation does not address by default:

**Physical access barriers:**
- Standard pit latrines require squatting — functionally impossible for many elderly adults and people with lower-extremity disabilities
- Trench latrines require crossing open ground, often at night, without lighting — high fall risk
- Distance from sleeping area to latrine: Sphere recommends no more than 50 meters, but for mobility-limited users, 30 meters is a more practical maximum
- Latrine entrance should be at least 90 cm wide to accommodate crutches or walking aids

**Adaptations:**
- Retrofitting a pit latrine for seated use: construct a wooden seat frame across the top of the slab with the opening positioned for seated use. Seat height of 40–45 cm from floor is standard for adult comfort. Armrests on both sides reduce fall risk significantly.
- Night access: a covered collection vessel (bucket with lid) in the sleeping area, emptied into the latrine in the morning, eliminates the need for nighttime navigation across open ground. This is the most practical solution for mobility-limited individuals who cannot safely travel 50 meters in the dark.
- Handrail: a single upright pole or rail within arm's reach of the latrine entrance reduces fall risk during approach and entry.

**Cognitive impairment:** Elderly individuals with dementia may require accompanied latrine use and may not self-initiate. Assign a specific caregiver responsibility for accompanying and monitoring.

**Dignity:** Maintain privacy for assisted latrine use. A second person present during assisted use should be the same gender as the user where possible. This is not optional in any properly managed displacement setting.

---

## Section 6: Organizational Readiness and WASH Coordination

### 6.1 WASH Cluster Coordination

In any large-scale emergency, WASH services are coordinated through a cluster or sector mechanism under the Inter-Agency Standing Committee (IASC) framework. The WASH Cluster is typically led by UNICEF with IFRC and NGO partners. For field practitioners, the operational implications are:

**Registration:** Any NGO providing WASH services in a formal emergency response should register with the WASH Cluster. Registration provides access to: shared situation reporting, standardized assessment forms, coordinated geographic coverage (avoiding duplication and gaps), procurement pooling, and technical standards.

**The 3Ws:** WASH Clusters use "Who does What, Where" (3W) matrices to map coverage. Field teams must report their 3W data regularly. This is administrative but directly affects resource allocation.

**Technical standards in cluster responses:** Sphere Standards are the baseline technical reference. UNHCR standards apply specifically in refugee settings. IASC guidelines govern inter-agency coordination protocols. Field teams should carry Sphere Handbook (print or offline) as a reference standard.

**Avoiding standards drift:** In acute emergency conditions, there is persistent pressure to accept below-standard sanitation ("something is better than nothing"). This is partly true but requires active management. Below-standard latrines (fewer than 1 per 50 people, no privacy, no handwashing) achieve much lower usage rates than standards-compliant facilities and may produce little measurable disease benefit. Advocate for standards-compliant facilities as rapidly as possible.

### 6.2 Supplies Procurement

**Minimum pre-positioned supplies for 100-person, 30-day sanitation capacity:**

| Item | Quantity | Notes |
|---|---|---|
| Portland cement (50 kg bags) | 10 bags | For 2 latrine slabs |
| Rebar (6mm, 6m lengths) | 12 lengths | Slab reinforcement |
| PVC pipe (110mm diameter, 3m length) | 4 lengths | Vent pipes for 4 VIP latrines |
| Fly screen (1.2mm mesh, 1m width) | 2 meters | Vent pipe covers |
| 20L plastic buckets with lids | 10 | Emergency toilets, water management |
| Bar soap (200g bars) | 50 bars | 30 days for 100 people, 1 bar per 2 people |
| Chlorine bleach (5% household) | 10 liters | Disinfection |
| ORS sachets (1L preparation) | 200 sachets | Treatment reserve |
| Reusable cloth pads or disposable pads | 120 units | MHM for estimated 30 women of menstruating age |
| Plastic sheeting (4m × 6m) | 4 pieces | Emergency latrine privacy screens |
| Tippy-tap construction materials (rope, nails, jerry cans) | Per design | Source locally when possible |

**Procurement lead times in emergency contexts:** Cement and steel are often available locally. ORS sachets require health cluster coordination. Pre-positioned supply caches (3-month reserve) are strongly preferred over just-in-time procurement for any organization operating in high-risk areas.

### 6.3 Rapid Adaptation Playbooks

**Scenario A: Urban building collapse, 200 people, no water, no latrines**

Priority sequence:
1. Hours 0–6: Identify open defecation zone and establish minimum 30-meter exclusion from any water source. Mark the zone. Assign an attendant.
2. Hours 6–24: Excavate trench latrine (minimum 4 trenches for 200 people at Sphere ratio). Begin water procurement — identify nearest safe water source or supplier.
3. Hours 24–72: Establish tippy-taps at latrine access points. Begin ORS distribution if any diarrheal cases present.
4. Days 3–7: Begin pit latrine construction to replace temporary trenches. Register with WASH cluster if formal response activated.
5. Days 7–14: Upgrade to VIP design. Establish MHM distribution. Conduct surveillance for diarrheal disease.

**Scenario B: Rural community, seasonal flooding, contaminated wells, no displacement**

Priority sequence:
1. Immediately: Treat all well water (boiling or chlorination per Wave 0 Domain 3). Test pH and turbidity; if wells are visibly turbid, suspend use.
2. Day 1–3: Assess all latrines for flood damage (slab collapse, lateral contamination). Decommission any latrine whose pit has been overtopped by flood water — it is now an open sewage contamination point.
3. Day 3–7: Construct replacement latrines on higher ground, at minimum 30 meters from wells. If community has Wave 0 domain knowledge (rainwater harvesting), activate cistern storage.
4. Ongoing: Establish daily surveillance for diarrheal cases. Distribute ORS if any cases develop.

**Scenario C: 30-person extended family group, off-grid long-term**

This is the composting toilet scenario. The two-chamber composting system (Section 2.4) is the optimal long-term solution if the following are met:
- Cover material (straw, dry leaves, wood shavings) is available in adequate quantity on an ongoing basis
- Community is willing to use finished compost on non-food-contact crops initially, with full approval for food crops after documented thermophilic cycling
- A compost thermometer is available

For a group of 30, build three two-chamber systems to maintain adequate distribution. Alternatively, one large-scale hot-composting system serves 30 people if managed by a dedicated operator.

**VIP upgrade priority:** For any scenario where a pit latrine is planned for use over 3 months, build the VIP from the start. The additional labor is 4–6 person-hours for vent pipe installation and superstructure modification. The reduction in fly-borne disease transmission justifies this investment in any setting.

### 6.4 Water-Sanitation-Hygiene Integration

The three components of WASH are mutually dependent in ways that purely sectoral thinking misses:

- **Sanitation without handwashing:** Latrines interrupt the environmental reservoir of pathogens, but without handwashing, contaminated hands still transmit fecal material to food and mouths. Studies consistently show that sanitation alone produces smaller disease reduction than sanitation combined with hand hygiene promotion.

- **Handwashing without clean water:** The water used for handwashing does not need to meet drinking water standards if soap is available. Grey water (from cooking or light laundry) can be recycled to tippy-taps for handwashing, reducing the demand on clean water supply. Cross-link to Wave 0 Domain 4 (Greywater Management) for detailed greywater treatment before non-contact reuse.

- **Hygiene promotion without behavior change facilitation:** Distributing soap and building latrines without community engagement produces consistently lower utilization rates than identical infrastructure combined with hygiene promotion. This is among the most robust findings in WASH implementation research. Minimum approach: identify respected community members who can serve as hygiene promotion focal points, provide them with basic training (WHO Five Moments, ORS preparation, latrine maintenance), and create a system for them to report emerging problems.

---

## Appendix A: Quick Reference Card

### Critical Numbers

| Parameter | Minimum | Notes |
|---|---|---|
| Water per person per day | 7.5 L (emergency), 15 L (sustained) | Sphere Standards |
| Latrine per persons | 1:50 (acute), 1:20 (sustained) | Sphere WASH |
| Latrine to water source distance | 30 m | Increase to 50 m in sandy soils |
| Latrine to dwelling | 6 m minimum | Privacy and safety |
| Pit depth minimum | 3 m | Collapse and fill risk |
| Pit volume minimum | 1,000 L | Sphere emergency standard |
| Vent pipe minimum diameter | 11 cm | VIP fly mechanism |
| Vent pipe minimum height | 30 cm above roof | Airflow requirement |
| Thermophilic composting safety | 55°C for 14 days OR 60°C for 7 days | Pathogen kill standard |
| Handwashing per tippy-tap wash | 50 ml water | vs. 500 ml conventional |
| ORS home formula (1 liter) | 6 tsp sugar + 0.5 tsp salt | Level measures only |

### Signs of Dehydration

**Mild:** increased thirst, slightly decreased urine output
**Moderate:** dry mouth, sunken eyes, decreased skin elasticity (pinch test: returns in >2 seconds), no tears
**Severe:** lethargy, unresponsive, sunken fontanelle (infants), skin pinch does not return

Moderate: ORS aggressive (75 ml/kg over 4 hours)
Severe: IV preferred; ORS via NGT if IV unavailable; evacuate if any option exists

---

## Appendix B: Sourcing Notes by Sub-Topic

**Section 1 (Water triage and Sphere quantities):** Sphere Standards WASH Chapter (spherestandards.org); WHO Technical Notes on Water, Sanitation and Hygiene in Emergencies; UNHCR Emergency Handbook WASH standards.

**Section 2.2 (Pit latrine construction):** UNICEF Ghana Technical Guidelines for Household Latrine Design and Construction; Emersan Compendium Single Pit Latrine specifications; Sphere minimum standards; UNHCR Emergency Sanitation Standards.

**Section 2.3 (VIP latrine):** Humanitarian Sanitation Hub Single VIP page (sanihub.info); CAWST VIP Latrine Fact Sheet; IRCWASH VIP Latrine Builders Guide (Zimbabwe).

**Section 2.4 (Composting toilets):** Humanure Handbook 4th Edition (humanurehandbook.com — author-released free distribution); PMC study on Thermophilic Composting of Human Feces (PMC8895236); Wave 1 Composting Domain.

**Section 2.5 (Emergency phase):** UNHCR Emergency Sanitation Standards (emergency.unhcr.org); Sphere Standards first-phase latrine ratios.

**Section 3 (Handwashing):** PMC systematic review of tippy-tap effectiveness (PMC7316639); Global Handwashing Partnership (globalhandwashing.org); WHO handwashing guidelines; PMC ash handwashing systematic review (PMC7192094).

**Section 4.1 (Disease prioritization):** WHO Communicable Diseases Following Natural Disasters guidance document; PMC post-disaster communicable disease prevention review (PMC3263111); CDC cholera/typhoid fact sheets.

**Section 4.2 (ORS):** MSF Medical Guidelines (medicalguidelines.msf.org); WHO ORS publications; home formula from CDC cholera treatment guidance.

**Section 5.2 (Menstrual hygiene):** UNHCR WASH Manual 8th Edition (March 2026); IRC MHM in Emergencies Toolkit; PMC MHM scoping review Africa (PMC11948744).

**Section 5.3–5.4 (Pediatric and elderly):** UNICEF/WHO Joint Monitoring Programme child health data; Sphere vulnerable populations chapter; CDC inclusion checklist for disability in WASH.

**Section 6 (WASH coordination):** IASC WASH Cluster guidance; Sphere Standards coordination chapter; UNHCR WASH Manual.

---

*Produced by the Open-Repo Project, 2026. Wave 2 Domain 3. This document is part of a humanitarian knowledge base designed for offline deployment via Kiwix/ZIM format for field use without internet connectivity. Cross-links reference other documents in the same corpus.*

*License: CC BY 4.0 — You may share, adapt, and build upon this material for any purpose with attribution.*
