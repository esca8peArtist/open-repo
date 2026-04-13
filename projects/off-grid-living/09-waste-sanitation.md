---
title: "Domain 9: Waste & Sanitation"
project: off-grid-living
status: complete
created: 2026-04-13
cross-refs: [03-water, 04-food-production, 08-medical-health, 01-site-selection, 15-disaster-scenarios]
---

# Domain 9: Waste & Sanitation

> Waste management is the infrastructure that makes everything else possible. Every disease outbreak
> in human history traces, at some level, to failed sanitation. Clean water systems, productive
> gardens, healthy animals — all are compromised by poor waste handling. This chapter covers human
> waste, greywater, and solid waste with the same engineering rigor applied to the rest of the
> homestead. There is no low-stakes shortcut here. The epidemiology is unambiguous: fecal-oral
> transmission kills, and it kills in ways that are slow, painful, and entirely preventable.
>
> **Hierarchy**: Prevent contamination → Reuse nutrients → Treat what cannot be reused → Dispose
> of what cannot be treated. Follow this order. It is not philosophical — it is the correct
> engineering sequence for both cost and outcome.

---

## Quick-Reference: System Selection

Before reading further, place yourself in one of these scenarios:

| Situation | Primary system | First action |
|---|---|---|
| Permanent homestead, lenient county, 2+ acres | Composting toilet + greywater to landscape | Read 9.2.1 (composting toilets), then 9.3 |
| Permanent homestead, permit required | Septic + greywater diversion | Read 9.2.4 (septic), talk to county first |
| Remote site, no permits obtainable | Outhouse or humanure system | Read 9.2.2 and 9.2.3 |
| Temporary camp, short-term (< 1 year) | Humanure bucket system | Read 9.2.3 |
| Budget under $1,000 | DIY two-chamber or outhouse | Read 9.2.1 DIY section or 9.2.2 |
| Nuclear/CBRN scenario | Deep burial + sealed containment | Read 9.8 |

Septic is not always the "safe" default — it is the most expensive and least nutrient-cycling option. Understand what your county actually requires before assuming you need it.

---

## 9.1 Why This Matters: Pathogens and Public Health

### 9.1.1 The Fecal-Oral Route

The mechanism by which human waste causes disease is well-established: pathogens shed in feces contaminate water, soil, or food surfaces, then enter a new host via ingestion. The route is: feces → environment (water, soil, hands, food) → mouth → infection. Every waste management intervention targets one link in that chain.

**Key pathogens in untreated human waste:**

| Pathogen | Type | Disease | Infective dose | Survival in soil/water |
|---|---|---|---|---|
| *Escherichia coli* O157:H7 | Bacterium | Hemorrhagic colitis, HUS | 10–100 organisms | Days to weeks in soil |
| *Salmonella* spp. | Bacterium | Gastroenteritis, typhoid | 10,000–1,000,000 | Weeks in wet soil |
| *Campylobacter jejuni* | Bacterium | Gastroenteritis | 500–800 organisms | Days in water |
| *Giardia lamblia* | Protozoan | Giardiasis (chronic diarrhea) | 1–10 cysts | Months in cold water |
| *Cryptosporidium parvum* | Protozoan | Cryptosporidiosis | 1–10 oocysts | Months; chlorine resistant |
| *Ascaris lumbricoides* | Helminth (roundworm) | Ascariasis (intestinal) | 1 embryonated egg | Years in soil |
| *Hepatitis A virus* | Virus | Hepatitis A | Low | Weeks to months |
| *Norovirus* | Virus | Severe vomiting, diarrhea | 10–100 particles | Weeks on surfaces |

The practical implication: human waste is a pathogen reservoir even from apparently healthy individuals. Asymptomatic carriers of *Giardia* and *Cryptosporidium* are common. Treat all waste as infectious.

### 9.1.2 Temperature Kill Data

Heat is the most reliable pathogen kill method. The evidence base from WHO Guidelines for the Safe Use of Wastewater, Excreta and Greywater (WHO, 2006) and subsequent studies:

- **55°C for 3 days**: Kills most enteric bacteria and viruses including *E. coli*, *Salmonella*, *Campylobacter*, hepatitis A
- **55°C for 7 days**: Additional safety margin; standard for hot composting protocols
- **60°C for 1 hour**: Kills *Ascaris* eggs (the most heat-resistant common pathogen)
- **70°C**: Instantaneous kill of most pathogens including *Ascaris*
- **Mesophilic composting (20–40°C)**: Does not reliably kill pathogens — requires extended time (1+ year) or final pasteurization step

The implication: DIY and commercial composting toilets operating at mesophilic temperatures must complete a curing phase before the compost is safe for use on food crops. Hot composting (thermophilic) shortens this to weeks.

### 9.1.3 The Highest-ROI Intervention

Handwashing with soap after toilet use and before food preparation reduces diarrheal disease incidence by 40–47% (Cochrane Review, Freeman et al., 2014). This exceeds the benefit of most individual water treatment technologies. You need soap, water, and consistent behavior. Build handwashing infrastructure into every toilet facility as a physical requirement, not an afterthought.

**Soap vs. plain water**: Soap is significantly more effective than water alone. The mechanism is surfactant action physically removing and suspending pathogens. Ash or sand can substitute for commercial soap in extremis — both have abrasive and some surfactant properties — but commercial soap is cheap enough that substitutes are unnecessary in non-emergency conditions.

---

## 9.2 Human Waste Systems

### 9.2.1 Composting Toilets

#### How Composting Works

Composting toilets decompose human waste through microbial action, producing a humus-like material that can be used as a soil amendment. Two temperature regimes are relevant:

**Mesophilic composting (20–40°C)**: Most commercial self-contained units operate in this range. Decomposition is slow (6–18 months to produce safe finished compost) and requires careful management of moisture, C:N ratio, and aeration. Pathogens may persist unless the finished product is hot-composted or left to cure for 1–2 years.

**Thermophilic composting (40–70°C)**: Required for faster pathogen kill. Achieved in large-volume systems (separate-chamber or two-chamber designs) where microbial activity generates self-sustaining heat. Requires pile volume of at least 1 cubic yard and proper C:N ratio (25–30:1). Self-contained commercial units rarely achieve sustained thermophilic temperatures.

#### Carbon:Nitrogen Ratio Management

Human feces has a C:N ratio of approximately 8:1 — too nitrogen-rich for efficient composting and responsible for the odor problems in poorly managed systems. Urine is even more nitrogen-dense (C:N < 1:1 when urine and feces are combined). Bulking material is not optional.

**Bulking material C:N ratios:**

| Material | C:N ratio | Notes |
|---|---|---|
| Sawdust (dry) | 400–500:1 | Excellent; available at sawmills for free or very cheap |
| Wood chips (fresh) | 100–150:1 | Good; slightly wet — allow to dry first |
| Straw | 60–80:1 | Common, effective, cheap |
| Dry leaves | 40–80:1 | Seasonal availability; good autumn collection |
| Peat moss | 58:1 | Effective but expensive; also acidic, which inhibits decomposition |
| Coco coir | 80:1 | Common in commercial units; consistent quality |
| Pine shavings | 150–200:1 | Excellent; available as animal bedding |

**Target ratio in the unit**: Add enough carbon material per deposit to bring the effective C:N to 25–30:1. For a typical deposit:
- Urine-diverting system: approximately 1 cup of sawdust per bowel movement
- Non-diverting system: 2–3 cups of sawdust per bowel movement (urine greatly increases nitrogen load)

#### Commercial Models: Honest Assessment

**Nature's Head (Separating)**
- Price: $960–$1,100 (direct), slightly higher through retailers
- Type: Urine-diverting; separates liquid from solids at the toilet seat
- Capacity: Designed for 1–2 full-time users or up to 4 on reduced-use schedule
- Compost chamber volume: ~6 gallons for solids
- Mechanism: Hand-crank mixing handle; coco coir as medium
- Emptying frequency: Every 4–8 weeks for 1 person continuous use; more like 3–4 weeks for 2 people
- Urine: Diverted to separate 2-gallon bottle; dilute 1:8–1:20 with water for direct landscape application (excellent nitrogen fertilizer) or pour on compost pile
- Power: 12V fan (included), ~1–2 watts continuous; ventilation hose to exterior required (1.5-inch hose, 4–8 feet max)
- Pros: Most popular off-grid unit; well-documented; compact for boats, tiny homes, RVs
- Cons: Small capacity means frequent emptying; mixing mechanism can break; not suitable for larger households without multiple units; solids do not reach thermophilic temperatures
- **Failure mode**: If urine diversion gasket fails or is improperly seated, urine mixes with solids — the resulting mix is anaerobic, wet, and extremely odorous. Check gasket condition monthly.

**Sun-Mar Excel NE (Non-Electric)**
- Price: $1,400–$1,700
- Type: Non-separating; handles both urine and feces in one drum
- Capacity: Rated for 3–4 people seasonal or 1–2 full-time
- Mechanism: Bio-drum (rotating drum) for active composting; finishing drawer below
- Power: None required (NE model); electric model has heating element for colder climates
- Pros: Larger capacity than Nature's Head; drum rotation improves aeration and C:N mixing; finishing tray allows curing stage before removal
- Cons: Bulky (39" H × 21" W × 34" D); harder to install in small spaces; if overloaded or underfed carbon, develops liquid accumulation in bottom ("tea") requiring drainage; higher price
- **Failure mode**: Overloading produces liquid accumulation. Sun-Mar sells a mulch mix specifically for their units. Using sawdust works equally well at 1/10th the cost.

**Separett Villa 9215 AC/DC**
- Price: $1,300–$1,500
- Type: Urine-diverting; one of the most used European designs, increasingly available in US
- Capacity: Up to 5 people
- Mechanism: Rotating container; fan-only model (no heat); urine diverted to separate tank or directly to drain/landscape
- Power: 12V DC or 120V AC for fan; approximately 2–4 watts
- Pros: Very clean design; the rotating container means the user never manually empties loose compost — the entire container (with a biodegradable liner bag) is removed and replaced; good for families
- Cons: Biodegradable bags are an ongoing cost ($30–50/year); needs a bin or outdoor composting area for the removed containers to complete curing; pricey relative to Nature's Head
- **Failure mode**: Fan blockage causes odor. Clean fan and screen annually. The biodegradable bags occasionally fail — maintain a stock.

**BioLet 55 NE**
- Price: $1,200–$1,500
- Type: Non-separating
- Capacity: Rated for 2–3 people full-time
- Mechanism: Electrically-driven rake (electric model) or manual rake; evaporator tray
- Pros: Compact; installs in existing bathroom footprint
- Cons: Electric model requires power; rake mechanism is a known failure point; non-diverting design means more careful moisture management
- **Best for**: Situations transitioning from flush toilet where footprint cannot change

#### DIY Two-Chamber Composting System

The most practical DIY composting toilet for a permanent homestead. Operates on the humanure principle (see 9.2.3) but in a dedicated structure with two chambers that alternate use. Considerably cheaper than commercial units and scales to larger households.

**Design:**

Two adjacent chambers, each approximately:
- 3 feet wide × 3 feet deep × 4 feet tall (internal dimensions) = 36 cubic feet per chamber
- Adequate for 2–4 people for 12–18 months of filling before switching chambers

**Materials per chamber:**
- (12) 8-inch concrete blocks (CMU) or equivalent, for walls if not using wood
- 3/4-inch exterior plywood for top and seat platform
- 2×6 framing for superstructure
- Hardware cloth (1/4-inch) for bottom (prevents rodents, allows drainage)
- Vent pipe: 4-inch PVC, black-painted, 3+ feet above roofline for passive draft
- Toilet seat mounted over access hole in plywood
- Hinged access door at rear or side for compost removal

**Operation:**
1. Add 4–6 inches of straw, wood chips, or leaves to floor before first use
2. After each use, cover with a generous handful of sawdust or wood chips (2 cups minimum)
3. When chamber is full (typically 12–18 months), close it and switch to Chamber 2
4. Chamber 1 cures for 12+ months with cover crop planted on top (squash works well and shades the pile)
5. After curing, finished compost tests should show no detectable *E. coli* or *Salmonella* before applying to food crops (soil testing labs can run this, ~$25–40 per sample)
6. Finished compost safe for non-edible plants and tree basins immediately after curing; use on food crops only after confirming pathogen kill

**Total DIY cost:** $200–$500 depending on materials sourced and superstructure design. A pallet-wood enclosure with a corrugated metal roof is effective and costs under $200 in materials.

#### Vermicomposting Toilet Variant

A small number of designs incorporate red wiggler worms (*Eisenia fetida*) directly into the composting chamber. Worms dramatically accelerate decomposition and can handle a higher nitrogen load than microbe-only systems. The practical challenge: worms require consistent moisture (40–60% moisture content), temperatures above 40°F, and are stressed by fresh urine (pH and ammonia). Best implemented in two-stage systems where fresh waste is pre-composted before entering the worm bin, or in urine-diverting designs where the solids chamber can be managed for worm habitat. Not recommended for beginners — straight aerobic composting is more forgiving.

#### Legal Status by State

Composting toilet legality is patchwork. "Legal" often means "permitted with conditions" — typically that you also have a permitted greywater system or septic system for liquid waste, and sometimes that you maintain a backup flush toilet. Verify with your county health department before installation.

| State | Composting toilet status | Notes |
|---|---|---|
| California | Permitted; NSF/ANSI 41 certification required | Must also have permitted greywater system |
| Oregon | Permitted with approval | DEQ review; compost end use regulated |
| Washington | Permitted; case-by-case county approval | Some counties require backup system |
| Arizona | Generally permissive | Greywater separately regulated; CT often approved |
| Texas | Permitted in most rural counties | Urban areas more restrictive; septic may be required |
| Montana | Generally permissive in rural areas | Individual county variation |
| Colorado | Permitted; requires county health approval | NSF 41 required in many counties |
| Vermont | Permitted with DEQ oversight | Strong history of alternative systems approval |
| New York | Restrictive in most areas | NSF 41 required; backup system typically required |
| Florida | Restrictive; septic often required | High water table makes alternatives complex |
| Georgia | Generally restrictive | County variance possible in rural areas |
| Tennessee | Permitted in rural counties | County health department approval |
| New Mexico | Generally permissive | Good support for alternative systems |
| Idaho | Generally permissive in rural areas | County by county |
| Maine | Permitted under plumbing code | Strong alternative system history |

**NSF/ANSI 41 certification**: The standard commercial composting toilet products are tested against this standard. It covers pathogen reduction, vector control, and structural requirements. Nature's Head and Separett both carry this certification. DIY systems do not, which can complicate permitting — frame DIY installations as "alternative systems" under your county's hardship or variance procedures.

#### Troubleshooting Composting Toilets

| Problem | Cause | Solution |
|---|---|---|
| Strong ammonia odor | Too much nitrogen (urine), insufficient carbon | Add more sawdust; in non-diverting units, increase carbon ratio significantly |
| Wet, soupy consistency | Too much liquid, insufficient carbon, or overloading | Add dry bulking material; check urine diverter function; reduce use rate |
| Fruit flies or other insects | Moisture and odor attracting insects; poor seal | Add 1/4 inch of sawdust after every use as covering layer; check gaskets and lid seal |
| No decomposition visible | Too dry or too cold | Add small amount of water if below 40% moisture; move unit to warmer location or add heat pad |
| Vent pipe odor inside | Back-draft; vent too short or insufficient draft | Extend vent pipe above roofline by 12+ inches; paint black for solar draft; add inline fan if passive draft inadequate |
| Compost hardening into dry mass | Too dry; too much carbon | Add water carefully; reduce sawdust |

---

### 9.2.2 Outhouse / Pit Latrine

The outhouse is the oldest engineered sanitation solution and, done correctly, is effective and extremely low-cost. Its advantage over composting toilets: no maintenance beyond site selection and occasional abandonment. Its disadvantage: permanent installation in one location, setback requirements, and eventual abandonment of filled pits.

#### Site Selection

Site selection is not optional — it determines whether groundwater and surface water are protected.

**Mandatory setbacks (minimums; verify local codes):**
- 100 feet from any well, spring, or drinking water source
- 100 feet from streams, ponds, lakes, or intermittent drainage courses
- 10 feet from property lines
- 15 feet from the dwelling (odor management while maintaining practical access)
- Not in a 100-year flood plain
- Not in soil with a seasonal high water table within 4 feet of the bottom of the pit

**Soil suitability:** The pit relies on soil absorption and filtration of leachate. Ideal soil is sandy loam or loam — enough particle size to allow drainage but enough clay to provide filtration. Very sandy soils drain too fast for adequate pathogen removal before reaching groundwater. Clay soils may not drain at all — liquid accumulates and odor becomes a major problem. A simple percolation test (dig a 12-inch hole, fill with water, measure how long until empty) helps assess drainage; 30–60 minutes per inch of drainage is adequate.

**Seasonal high water table**: Probe the soil in late winter or early spring (highest water table period). Use a 1.5-inch diameter soil probe to 6 feet depth. If you encounter saturated soil within 4 feet of the surface, a conventional pit latrine is not appropriate — use composting toilet or septic instead.

#### Pit Sizing

For a 4-person household with year-round use:

**Volume calculation:**
- Average accumulation rate: 0.03–0.06 cubic feet per person per day (including anal cleansing materials)
- 4 people × 0.04 cu ft/day × 365 days/year = 58.4 cu ft/year
- Adequate pit volume for 2–3 years: 120–175 cu ft
- Example pit dimensions: 4 feet wide × 4 feet long × 8 feet deep = 128 cu ft (achievable with a tractor-mounted post-hole auger)
- More typical hand-dug: 3 feet wide × 4 feet long × 5 feet deep = 60 cu ft (1–1.5 years for 4 people)

For longer service life, dig two pits and alternate, same as the two-chamber composting system. This also allows the full pit to decompose and potentially be emptied and used as soil amendment.

#### Lining vs. Unlined

**Unlined pit:**
- Pros: Maximum drainage; pathogens filtered by soil passage; standard in most of the world
- Cons: Pit walls may collapse; minimal protection in sandy or loose soils; not appropriate near water table

**Lined pit (perforated or porous lining):**
- Materials: Concrete rings (precast), block construction with open joints, or perforated PVC culvert
- Pros: Prevents wall collapse; allows drainage while maintaining structural integrity; extends pit life
- Cons: More construction effort; concrete adds cost
- Appropriate when: Soil is sandy and prone to collapse; depth exceeds 6 feet; high use rate

**Sealed liner (full concrete):**
- Not appropriate for an outhouse — eliminates drainage and creates a septic tank in the wrong location
- Only use sealed construction if connecting to a proper drain field

#### VIP Design (Ventilated Improved Pit)

The Ventilated Improved Pit design addresses the two primary complaints about outhouses: odor and flies.

**Mechanism:**
1. A 4-inch or 6-inch vent pipe extends from the pit interior to 18+ inches above the superstructure roof
2. The pipe is painted black (or is black ABS plastic) to absorb solar heat, creating an upward draft
3. The toilet seat is kept covered with a close-fitting lid when not in use
4. The interior of the superstructure is kept dark

**Why it works**: Warm air in the black vent pipe rises, drawing air from the pit interior upward and out. Odors exit via the vent rather than the seat hole. Flies attracted by odor exit the pit through the vent pipe and, encountering the light at the top (dark interior conditions essential), are trapped and die. The result is a near-odor-free interior and dramatically reduced fly population.

**Materials for VIP modification:**
- 4-inch black ABS pipe: $0.80–1.20/foot
- 10 feet typically sufficient: $8–12
- Flyscreen cap for pipe top (galvanized hardware cloth): $5–10
- Total additional cost over standard outhouse: $15–25

#### Superstructure: DIY Cost Breakdown

A functional, weathertight outhouse superstructure:

| Component | Quantity | Unit cost | Total |
|---|---|---|---|
| 2×4 framing lumber (pressure-treated sill plate) | 20 LF | $0.90/LF | $18 |
| 2×4 framing lumber (wall framing) | 80 LF | $0.65/LF | $52 |
| T1-11 siding (2 sheets, 4×8) | 2 | $38 | $76 |
| Roofing (corrugated metal, 4×8 panel) | 2 | $28 | $56 |
| Roofing screws and ridge cap | 1 lot | $15 | $15 |
| 2×6 seat platform (exterior plywood) | 1 sheet | $42 | $42 |
| Toilet seat | 1 | $18 | $18 |
| Door hardware (hinges, latch) | 1 lot | $15 | $15 |
| Vent pipe and screen | 10 LF | $1.10/LF | $16 |
| Nails, screws, misc | 1 lot | $20 | $20 |
| **Total** | | | **$328** |

Labor: 1–2 people, 1 full day. No special skills beyond basic carpentry.

#### When and How to Abandon a Full Pit

When a pit is within 18 inches of the surface (measure by probing with a stick), it is time to abandon.

**Abandonment procedure:**
1. Fill with alternating layers of wood ash and soil, tamping each layer
2. Cap with 6–8 inches of clean soil mounded above grade to account for settling
3. Mark the location — it will settle over time and you need to know where not to excavate
4. Plant a deep-rooted perennial (comfrey, shrub, fruit tree) over the site — the nutrient reservoir is substantial

**Compost viability**: After 2+ years of aerobic decomposition, the contents of a well-managed pit can be used as soil amendment for non-edible plants. Do not apply to vegetable crops without pathogen testing.

---

### 9.2.3 Humanure System (Haverstock Method)

Developed and documented by Joseph Jenkins in *The Humanure Handbook* (3rd ed., 2005), the humanure system is arguably the safest closed-loop human waste management approach when properly executed, because it routes waste through a thermophilic hot compost pile that reliably kills pathogens.

#### The Bucket System

**Equipment:**
- 5-gallon plastic bucket with tight-fitting lid (one per toilet, plus spares)
- Toilet seat designed for 5-gallon bucket (available for $10–20, or improvise from standard seat)
- Large dedicated compost pile, separate from kitchen/garden compost, 3–6 feet from ground access

**Per-use protocol:**
1. Use the toilet normally
2. Cover deposit immediately with 1–2 cups of bulking material (sawdust, straw, peat — anything carbon-rich)
3. Replace lid tightly
4. When bucket is full (every 2–5 days for one person, every 1–2 days for a family), carry to compost pile and deposit in a designated area of the pile
5. Cover deposit with a generous layer of straw, wood chips, or hay (6+ inches)
6. Keep the compost pile covered with straw at all times

**Handwashing station adjacent to bucket toilet**: Mandatory. Bucket, water, and soap minimum. No exceptions.

#### The Thermophilic Pile

The critical component. The hot compost pile must reach and sustain 55°C (131°F) for at least 3 consecutive days — measured with a compost thermometer (a long-probe thermometer inserted to the center of the pile).

**Pile requirements for reaching thermophilic temperatures:**
- Minimum volume: 1 cubic yard (3' × 3' × 3')
- C:N ratio: 25–30:1 (achieved by heavy straw covering of each deposit)
- Moisture: 40–60% (squeeze test — soil should hold form when squeezed but not drip)
- Oxygen: Pile must be turned periodically or have adequate loose structure for airflow

**Annual cycle:**
- Year 1: Actively add to pile. Monitor temperature with compost thermometer.
- Year 2: Pile 1 is curing. Begin Pile 2 for active deposits.
- Year 3: Test Pile 1 for pathogens. If clear (no detectable *E. coli* or *Salmonella* by lab test), apply as soil amendment to any part of the garden including food crops.

**Pathogen testing**: Soil testing labs routinely test for *E. coli* and *Salmonella*. Cost: $25–50. Worth doing at least once per pile to build confidence in your system and verify adequate pathogen kill. UMass Extension, Texas A&M AgriLife, and most state land-grant university extensions offer this service by mail.

**Evidence base**: Jenkins cites multiple studies, and this is supported by the WHO guidelines: hot composting at 55°C for 3 days, combined with a 12-month curing period, produces compost meeting WHO category A safety standards (safe for unrestricted agricultural use).

**What this system is not**: It is not a quick solution. It requires a separate compost area, consistent discipline in covering deposits, two-pile alternation, and temperature monitoring. The cost is near zero. The discipline requirement is high. It works only if you follow the protocol.

---

### 9.2.4 Septic Systems

#### How They Work

A conventional septic system has two components:

**Septic tank (600–1,500 gallons for a 3–4 bedroom house):**
- Receives all waste from the house (black and grey water)
- Solids settle to the bottom (sludge); grease and lighter material float (scum layer)
- Clarified liquid (effluent) in the middle exits to the drain field
- Anaerobic bacteria partially decompose solids in the tank
- Tank requires pumping every 3–5 years to remove accumulated sludge; failure to pump causes solids to exit to drain field, clogging it

**Drain field (leach field):**
- Network of perforated 4-inch PVC pipes in trenches of gravel
- Typical trench depth: 24–36 inches; trench width: 24 inches; gravel depth: 12 inches
- Effluent percolates through gravel and into soil, where final filtration and pathogen removal occurs
- Sizing is based on soil perc rate and daily flow

#### Percolation Test

Before a septic system can be permitted, the soil must pass a percolation test (perc test) — typically conducted by a licensed engineer or health department inspector.

**Test method:**
1. Dig test holes 12 inches in diameter to proposed trench depth
2. Presoak holes for 24 hours (ensures soil is at field capacity)
3. Add 6 inches of water; measure time for water to drop 1 inch
4. Repeat 3 times; use average

**Perc rates and drain field sizing:**

| Perc rate (min/inch) | Soil type | Drain field size (4 BR house, ~400 gpd) |
|---|---|---|
| 1–3 | Very sandy | 450–600 sq ft trench area |
| 3–10 | Sandy loam | 600–900 sq ft |
| 10–30 | Loam | 900–1,500 sq ft |
| 30–60 | Clay loam | 1,500–2,500 sq ft |
| >60 | Marginal | May require alternative system |
| >120 | Clay | Conventional septic not feasible |

#### System Sizing

**Tank sizing** (from EPA Onsite Wastewater Treatment Systems Manual):
- 1–2 bedrooms: 750-gallon minimum
- 3 bedrooms: 1,000-gallon minimum
- 4 bedrooms: 1,200-gallon minimum
- Each additional bedroom: add 250 gallons

**Drain field sizing**: Contact local health department — sizing formulas vary by state. The perc test result drives the calculation.

**Daily flow estimate**: 75 gallons/person/day for design purposes. A 4-person household = 300 gpd design flow.

#### Installation Costs

| Item | Cost range | Notes |
|---|---|---|
| Perc test and site evaluation | $200–$800 | Varies by state, required before permit |
| Permit fees | $300–$1,500 | County dependent |
| Septic tank (1,000 gal concrete) | $400–$800 | Material only; concrete or fiberglass |
| Tank installation (excavation, backfill) | $600–$1,500 | |
| Drain field excavation and pipe | $2,000–$8,000 | Highly dependent on soil and field size |
| Distribution box | $50–$200 | Splits flow evenly to drain field lines |
| Total conventional system | **$5,000–$15,000** | Higher in difficult soils or remote access |
| Mound system (poor perc soils) | $8,000–$20,000+ | Engineered fill mound above grade |
| Aerobic treatment unit (ATU) | $8,000–$18,000 | Active aeration; produces cleaner effluent |

#### Maintenance

**Pump every 3–5 years**: The most important maintenance task. Cost: $200–$500. Skip this and you pay $3,000–8,000 to repair or replace a clogged drain field.

**Signs of drain field failure:**
- Lush green grass over drain field in dry weather (hydraulic overload)
- Soggy ground or standing water over drain field
- Sewage odors in yard
- Slow drains throughout the house
- Sewage backup into lowest drains

**What not to put in a septic system:**
- Cooking grease: coats pipes and kills bacterial population
- Non-biodegradable wipes (even "flushable" wipes): clogs distribution box
- Antibacterial soaps in large quantities: kills the beneficial bacterial population
- Prescription pharmaceuticals: pass through to drain field; environmental concern
- Paint, solvents, harsh chemicals: kill bacterial population and may contaminate groundwater

**Greywater diversion to reduce load**: Diverting laundry and shower greywater to a landscape system (see 9.3) reduces the hydraulic load on a septic system by 40–60%. This can extend drain field life significantly and is worth doing even with a functioning septic system.

#### Alternative Septic Systems

**Mound system**: For soils with high water table or poor perc rates. Engineered fill mound elevates the drain field above restrictive soil layer. Costs 50–100% more than conventional. Requires pump for pressurized distribution.

**Aerobic Treatment Unit (ATU)**: Active aeration in the tank stage produces effluent with BOD/TSS levels dramatically lower than conventional. Required in some environmentally sensitive areas. Ongoing maintenance contract typically required by regulation ($100–$200/year). Brands: Norweco, Jet Inc., Consolidated Treatment Systems.

**Drip irrigation system**: Pressurized delivery of treated effluent to shallow soil injection points. Expensive but flexible — can distribute over large area in smaller quantities. Common in Texas and other states with shallow restrictive layers.

#### Emergency Scenarios

If the septic system backs up and you cannot get a pump truck for days:

1. Immediately minimize water use (no laundry, no dishwasher, minimal showers)
2. Set up a temporary bucket-and-sawdust system for toilet use
3. Any liquid waste going to the septic will continue to load the system; greywater to a landscape area instead
4. If the tank is pumped but drain field is the problem, a tank backup is likely within 24–48 hours of normal use resuming — arrange pumping and field evaluation before resuming normal use

---

### 9.2.5 Emergency and Field Scenarios

For temporary camps, disaster scenarios, or situations where permanent infrastructure is not yet established:

**Cat hole** (individual, short-term): Dig 6–8 inches deep in organic topsoil, at least 200 feet from water. Cover completely. Effective for individual camping but not for household use — concentration of cat holes in a small area quickly exceeds soil capacity.

**Temporary bucket system**: 5-gallon bucket, heavy plastic bag liner, sawdust. Fill, tie off bag, double-bag, and store in a closed container until proper disposal is available. This is the baseline for hurricane sheltering-in-place and immediate post-disaster situations.

**Portable commode over a bucket**: For mobility-limited individuals or indoor situations.

---

## 9.3 Greywater Systems

### 9.3.1 Greywater vs. Blackwater

**Legal and practical distinction:**
- **Blackwater**: Toilet waste (urine + feces). Contains the full pathogen load described in 9.1. Requires septic, composting toilet, or outhouse in all jurisdictions.
- **Greywater**: Water from sinks, showers, bathtubs, and laundry. Does not contain fecal matter under normal use. Significantly lower pathogen load. The legal treatment varies dramatically by state.

**Health context**: Greywater is not sterile. It contains bacteria from skin, mouths, and food preparation. It contains organic matter that supports pathogen growth if allowed to pool. The key difference from blackwater is the absence of enteric pathogens from feces — though cross-contamination is possible (washing diapers, rinsing cutting boards after raw meat, etc.). The practical guideline: treat greywater as potentially contaminated and manage accordingly — never allow surface pooling, never allow contact with edible plant parts, and never allow it to reach a drinking water source.

**Volume estimates** for a 4-person household:
- Shower/bath: 8–25 gallons per shower; 35–50 gallons per bath
- Kitchen sink: 3–7 gallons per meal cleanup
- Bathroom sink: 1–3 gallons per use
- Laundry: 15–30 gallons per load (front-loading washer on low setting)
- **Total greywater production**: 50–120 gallons per household per day

### 9.3.2 Laundry-to-Landscape (L2L)

The most commonly permitted and simplest greywater system. Laundry water is piped directly to mulched tree or shrub basins.

**Why laundry specifically**: Washing machine discharge is accessible from a single exit point (the drain hose), is produced in large batches convenient for landscape irrigation, and is typically the highest-volume single greywater source.

**Basic L2L design:**

1. Remove or bypass the standpipe connection; run the washing machine drain hose to a 3-way ball valve
2. One valve position sends to the sewer/septic as normal; other position sends to landscape
3. From the ball valve, run 1.5-inch or 2-inch Schedule 40 PVC to the yard
4. At each landscape outlet, create a mulch basin: excavate a shallow depression 18–24 inches diameter, fill with 4–6 inches of coarse wood chip mulch
5. Outlet pipe terminates within the mulch basin, below mulch surface
6. Space outlets at least 6 feet apart; minimum 2 feet from structures; minimum 100 feet from wells

**Sizing**: One washer load (15–25 gallons) per basin per week is generally adequate. A household producing 4–5 loads per week can supply 4–5 tree or shrub basins.

**What cannot go to L2L:**
- Wash water from diapers or heavily soiled infant items (fecal contamination risk)
- Water used to wash raw meat or poultry (Salmonella risk)
- Loads with bleach, strong disinfectants, or industrial cleaners (toxic to soil biology)
- Water from heavily sick household members

### 9.3.3 Branched Drain Gravity System

A more comprehensive system that handles shower, sink, and laundry from multiple sources. Gravity-fed to multiple landscape outlets.

**Core design rules** (from Art Ludwig's *Create an Oasis with Greywater*, 6th ed., the definitive technical reference):

1. **2% minimum slope**: Every pipe run must slope at 2% (1/4 inch per foot) from source to outlet. No exceptions — greywater with food particles and soap will clog any flat or backfilled pipe.
2. **No valves except at the source**: Valves downstream create partial blockages that fill with solids. The system branches via Y-fittings only.
3. **Surge tank before distribution** (optional but recommended for showers/sinks): A 5–10 gallon surge tank with a float valve allows the system to distribute a sudden surge (shower drain) gradually to multiple outlets rather than overwhelming one basin.
4. **Branched outlets**: Use 2-inch-diameter Y-fittings to split flow progressively — 1 source → 2 outlets → 4 outlets, etc.

**Pipe sizing:**
- Main drain from house: 2-inch Schedule 40 PVC
- Branch lines: 1.5-inch ABS or PVC acceptable
- Final distribution in mulch basin: 1-inch perforated pipe or open end in mulch

**Surge tank design:**
- A 5-gallon food-grade plastic bucket serves as a surge tank
- Inlet at top; outlet near bottom with 1-inch standpipe inside to allow sediment to settle
- Inspect and clean every 6 months; accumulated hair and grease must be removed
- Total cost for surge tank: $5–15

**Typical installed branched drain cost (DIY):** $200–$600 in materials. Labor: 1–2 people, 1–2 days.

### 9.3.4 Constructed Wetland / Reed Bed

The highest-treatment greywater system achievable without powered components. Constructed wetlands use plant roots and soil microbiota to remove BOD (biological oxygen demand), suspended solids, and pathogens from greywater.

**Two types:**

**Horizontal subsurface flow (HSSF) wetland** (most common for greywater):
- Greywater flows horizontally through gravel bed; plants root through the gravel
- Water remains below the gravel surface (no surface ponding)
- Aerobic and anaerobic zones coexist
- Better odor control than surface flow; lower mosquito risk

**Vertical flow constructed wetland (VFCW)**:
- Water is intermittently dosed onto the surface; flows downward through sand/gravel media
- Fully aerobic treatment; better nitrification
- Requires dosing mechanism (gravity from a surge tank or timed pump)
- Better performance for high-BOD inputs

**Sizing for a 4-person household producing 80 gallons/day of greywater:**
- HSSF wetland: 50–80 square feet of bed area
- Bed depth: 24–30 inches of 3/4-inch washed gravel
- Inlet and outlet pipes: 4-inch perforated PVC along width of bed
- Overflow connection to drain field or polishing area

**Construction:**
1. Excavate to 30 inches depth; slope bed 1% from inlet to outlet end
2. Line with 40-mil EPDM pond liner (available from pond supply companies, $0.50–0.80/sq ft)
3. Fill with 4 inches of coarse sand as bottom layer, then 20+ inches of 3/4-inch gravel
4. Install 4-inch perforated PVC inlet pipe at one end (elevated 6 inches from bottom); outlet at opposite end 6 inches from bottom
5. Plant with wetland species spaced 12–18 inches apart
6. Mulch surface with 2 inches of wood chips to prevent surface evaporation and odor

**Plant species** (choose for your climate):
- *Phragmites australis* (common reed): Most widely used; extremely effective but invasive in some regions — check your state's invasive species list before planting
- *Scirpus* spp. (bulrushes): Excellent; non-invasive; good for most North American climates
- *Typha* spp. (cattails): Very effective; aggressive spreader — confine with root barrier
- *Iris pseudacorus* (yellow flag iris): Effective; ornamental; non-invasive in most areas
- *Juncus effusus* (soft rush): Moderate performance; good for systems with variable flow

**Expected performance**: BOD removal 70–90%; suspended solids 75–90%; fecal coliform 1–2 log reduction (90–99%). This produces effluent suitable for landscape irrigation of non-edible plants. Not potable.

**Constructed wetland total DIY cost (4-person system, 60 sq ft):**
- EPDM liner (80 sq ft with margins): $50–65
- 3/4-inch gravel (3 cubic yards): $90–150
- Inlet/outlet PVC pipe and fittings: $40–80
- Plants (12–20): $30–80
- Coarse sand (0.5 cubic yard): $20–40
- Excavation (manual 2-person, 1–2 days): $0 DIY
- **Total materials: $230–$415**

### 9.3.5 Soap Selection for Greywater Systems

This is not a minor detail. The wrong soap chemistry will damage the soil structure in mulch basins and kill beneficial microbial populations.

**Avoid:**
- **Sodium-based soaps**: Sodium (Na) is a dispersing agent for clay soils — literally the same chemistry used to break down soil structure. High-sodium greywater applied repeatedly to clay soils creates a sodium-dispersed, impermeable layer. This is permanent damage. Check ingredient lists for sodium lauryl sulfate (SLS), sodium laureth sulfate (SLES), sodium hydroxide as primary ingredient.
- **Boron/borax-based products**: Toxic to plants at the concentrations that accumulate in soil with repeated greywater application
- **Bleach or chlorine-containing products**: Kills soil microbiology and is particularly harmful to constructed wetland plant roots
- **Phosphate-containing detergents**: Algae-blooming risk in any water receiving the discharge

**Prefer:**
- **Potassium-based soaps**: Potassium (K) is a beneficial plant nutrient and does not disperse clay. Most "natural" and "plant-based" liquid soaps use potassium hydroxide as the saponifier.
- **Oasis Biocompatible Laundry Liquid**: The most frequently recommended by greywater engineers (Art Ludwig and others); designed specifically for greywater reuse; $20–25/gallon, concentrated
- **Ecos (Earth Friendly Products)**: Widely available; phosphate-free, plant-based; functional for greywater
- **Dr. Bronner's Pure Castile Soap**: Potassium-based; suitable; biodegrades rapidly; no problematic additives
- **Seventh Generation Free & Clear (laundry)**: Phosphate-free; no optical brighteners; acceptable for greywater

Test soils annually with a simple EC (electrical conductivity) meter ($15–30) to detect sodium accumulation over time.

### 9.3.6 Greywater Legal Status by State

| State | System type | Legal status | Notes |
|---|---|---|---|
| California | L2L | Fully permitted; no permit for simple L2L | Title 22 and local plumbing code; best regulations in country |
| California | Branched drain / constructed wetland | Permitted with permit | Tier 1 systems permit-free; larger systems need permit |
| Arizona | All greywater systems | Generally permissive; permit-free under 400 gpd | Detailed regulations in ARS §49-371; clear guidance available |
| New Mexico | Most greywater systems | Permitted; progressive regulations | NMAC 20.7.3 governs; permit required |
| Oregon | L2L and branched drain | Permitted; permit required | DEQ administers; some counties more strict |
| Washington | L2L | Permitted with permit in most counties | County variance available |
| Texas | Limited; some municipalities permitting | No statewide framework | Patchwork; Austin and some cities have local ordinances |
| Florida | Restrictive | Generally requires full septic connection | High water table and karst geology drive restrictions |
| Montana | Permissive in rural areas | No specific greywater regulations; common-sense application | Best to notify county health |
| Colorado | Moderate | Indoor reuse (toilet flushing) easier than outdoor | HB 10-1105 allows some systems |
| Nevada | Moderate | Permit required; reasonable process | |
| Idaho | Rural areas generally permissive | County dependent | |
| Vermont | Moderate | Permit required under plumbing code | |
| North Carolina | Restrictive | Pilot program only; limited availability | |
| Georgia | Restrictive | Septic required for most applications | |

**The trend**: Western states (CA, AZ, NM, OR) have the most developed greywater regulatory frameworks. This reflects water scarcity driving policy: greywater reuse reduces potable water demand. Eastern states with abundant rainfall have less regulatory development and often default to prohibiting systems not explicitly permitted. Always check with the state plumbing board and county health department before installation.

### 9.3.7 Common Greywater Failures

| Failure | Cause | Prevention |
|---|---|---|
| Clogged pipes | Insufficient slope; hair and grease accumulation | Maintain 2% minimum slope; install lint trap/hair filter on shower drain |
| Odor | Greywater held standing; anaerobic decomposition | Design for rapid drainage to mulch basin; no ponding |
| Plant damage | High-sodium soap; boron accumulation | Switch to greywater-compatible soap immediately |
| Soil waterlogging | Outlet too concentrated; mulch basin too small | Distribute to more outlets; enlarge mulch basin |
| Fly and mosquito breeding | Surface pooling | Extend mulch depth; ensure full subsurface distribution |
| Permit non-compliance | System installed without permit | Check with county before install; after-the-fact permits possible in many jurisdictions |

---

## 9.4 Solid Waste Management

### 9.4.1 Reduction Hierarchy

In order of priority: refuse → reduce → reuse → recycle → recover → landfill

**Refuse**: The most powerful and least-implemented strategy. Declining to purchase materials in non-recyclable packaging, refusing single-use items, buying in bulk reduces the problem before it arrives. A homestead producing its own food largely eliminates food packaging waste — the largest component of household solid waste by volume.

**Reduce**: Right-sizing purchases. Buying exactly what you need, not a safety-buffer excess that often becomes waste.

**Reuse**: Glass canning jars, cotton bags, repair before replacement. The infrastructure investment in a small sewing kit, a basic tool set, and the skills to use them is the highest-ROI waste reduction strategy.

**Recycle**: Metal and glass are the primary recyclables with value at a rural homestead. Paper and cardboard are better composted or used as weed barriers. Plastic is difficult — rural areas rarely have plastic recycling pickup; baling and hauling to a recycling center on monthly town trips is the realistic approach.

**Recovery**: Biochar production, rendering fat from food waste, feeding vegetable scraps to chickens — extracting value from materials before disposal.

**Landfill**: What remains after the above is genuinely waste. Minimize this category by working down the hierarchy.

### 9.4.2 On-Site Composting

See also Domain 4 (Food Production) for integration with garden fertility systems.

**Two-bin hot compost system:**
- Bin 1 (active): Receive kitchen scraps, garden waste, coffee grounds, eggshells, and paper/cardboard (torn small)
- Bin 2 (curing): Finished material from Bin 1 cures for 4–8 weeks before use
- Each bin: 3×3×3 feet minimum for thermophilic temperatures; wire mesh or pallet construction
- Turn Bin 1 weekly to maintain aerobic conditions and distribute heat
- Target internal temperature: 55–65°C (130–150°F)

**Feed the compost (yes):** Vegetable scraps, fruit peelings, coffee grounds, tea bags, eggshells, grass clippings, leaves, shredded paper, cardboard, wood ash (small amounts), manure from herbivores

**Do not compost:** Meat, fish, dairy (rodent attractant and odor problems in open bins), cooked food with fats, pet feces (pathogens), diseased plant material

**Vermicomposting** (see 9.4.5) handles kitchen scraps more efficiently than hot compost for small households.

### 9.4.3 Burn Barrel and Open Burning

Burning is a practical reality at many rural homesteads for paper, cardboard, and clean wood waste. It is not appropriate for plastics, painted wood, treated lumber, or electronics.

**Legal status**: Highly variable.
- Many rural counties permit outdoor burning with no permit for agricultural waste and clean wood
- Air quality regulations (state and EPA) often exempt agricultural burning and small-scale burning from permitting
- Many states prohibit burning on high-wind or high-fire-risk days (check local burn bans)
- Burning municipal solid waste (household garbage) is regulated or prohibited in most states
- **Always check local ordinances and active burn bans before burning**

**What to burn:**
- Dry, untreated wood scraps and lumber offcuts
- Paper and cardboard (without glossy coatings when possible)
- Dry brush and garden trimmings
- Agricultural waste (straw, cornstalks, dry crop residue)

**What not to burn — ever:**
- Plastics: produces dioxins, furans, hydrogen chloride, benzene
- Treated/painted lumber: contains arsenic (CCA), chromium, lead, or VOCs
- Rubber (tires, hoses): benzene, polycyclic aromatic hydrocarbons, hydrogen sulfide
- Electronics: lead, mercury, cadmium — bio-accumulate and are highly toxic
- Styrofoam: styrene (carcinogen)
- Glossy/colored paper: heavy metal-based inks

**Optimal burn conditions:**
- Dry, calm days (wind < 10 mph; burning in wind spreads embers and reduces combustion efficiency)
- Afternoon when humidity is lowest
- Never burn when soil is dry and there is fire spread risk
- Attend the burn; have a water source nearby
- Allow ash to cool completely (24 hours) before handling or disposing

**Burn barrel vs. open pit:**
- Burn barrel (55-gallon steel drum with holes drilled): better combustion efficiency, more contained, easier to manage; draft holes at bottom improve combustion temperature
- Open pit: simpler but allows ash and embers to scatter; appropriate on large properties with clear zones

### 9.4.4 Biochar Production

Biochar is the product of pyrolysis — combustion of organic matter in low-oxygen conditions. At temperatures between 300°C and 700°C without full combustion oxygen, organic material is converted to a highly porous carbon structure rather than CO2. Applied to soil, biochar:
- Provides habitat for soil microbial populations (the pore structure dramatically increases surface area)
- Improves water retention in sandy soils
- Improves drainage in clay soils (counterintuitive but documented)
- Sequesters carbon for centuries to millennia
- Is pH-neutral to slightly alkaline — useful for acidic soils
- Does not provide nutrients itself but acts as a nutrient sponge when charged (see below)

**Retort design** (simple, scalable):

The simplest retort is a cone pit:
1. Dig a cone-shaped pit approximately 2 feet deep and 2–3 feet diameter at the top
2. Light a small fire in the bottom of the cone
3. As the fire establishes, add wood in layers, covering the fire partially before it burns to ash
4. When the layer below glows without flame (charcoal), add the next layer
5. Continue adding material until the pit is nearly full
6. Quench immediately with water to halt combustion before ash stage
7. Dry the biochar and screen to remove incompletely carbonized material

**Kiln retort** (higher volume):
- A 55-gallon drum with a smaller (30-gallon or similar) inner vessel
- Inner vessel holds the feedstock; outer vessel provides the combustion air and radiant heat
- Top-lit updraft (TLUD) design: light fuel on top; fire burns downward through column of material
- Pyrolysis gases exit the top and can be burned as fuel (wood gas)
- More consistent product and larger batches than cone pit

**Temperature targets:**
- 300–400°C: Low-temperature biochar; higher volatile content; improves moisture retention
- 500–700°C: High-temperature biochar; more porous; better for microbial habitat; standard agricultural target
- >700°C: Ash conversion begins; avoid

**Charging biochar before soil application:**
Raw biochar straight from the kiln is essentially inert. It must be "charged" — loaded with nutrients and microbial inoculant — before application, or it will initially draw nutrients from the soil.

**Charging methods:**
1. Mix 1 part biochar with 2 parts mature compost; allow to sit for 2–4 weeks
2. Soak biochar in diluted urine (1:5 ratio with water) for 2–3 days before incorporating into compost
3. Mix into an active hot compost pile during turning

**Application rates:**
- Standard: 0.5–2 kg per square meter (1–4 lbs per 10 sq ft) incorporated into top 6–8 inches
- Do not exceed 5% of soil volume; excessive biochar can impair drainage

### 9.4.5 Vermicomposting

Red wigglers (*Eisenia fetida*) are not the same as garden earthworms (*Lumbricus terrestris*). They are surface dwellers adapted to processing decomposing organic matter — exactly what a kitchen compost bin produces. They can process kitchen scraps 2–4 times faster than hot compost in a warm climate.

**Bin sizing:**
- Rule of thumb: 1 square foot of bin surface per pound of kitchen waste per week
- A 4-person household producing 3–5 lbs of kitchen scraps per week needs 3–5 square feet of surface area
- Standard starter bin: 2 feet × 2 feet × 1 foot deep (4 sq ft) — handles 3–4 lbs/week

**Starter bin construction:**
- Plastic storage tote (12–18 gallon) or wooden box; drill 1/4-inch holes in bottom (drainage) and lid (ventilation)
- Bedding: shredded cardboard and newspaper (60% moisture — wrung out but not dripping), coconut coir, or aged leaf litter
- Introduce worms at 1 lb per square foot of surface (approximately 1,000 worms/lb)
- Cover worms with a layer of moist cardboard to reduce light exposure

**Feeding:**
- Feed in small batches buried in bedding; do not leave exposed
- Optimal: vegetable scraps, fruit peels, coffee grounds, tea bags, crushed eggshells, small amounts of bread/grain
- Avoid: citrus in large quantities (acidic), onion and garlic (strong oils), dairy, meat, oily foods, salty foods
- One rule: if you wouldn't leave it on a kitchen counter for 3 days, bury it deeper in the bin

**Harvest** (every 3–4 months):
- Push finished vermicompost to one side; add fresh bedding and food to other side
- Worms migrate to fresh food over 1–2 weeks
- Harvest finished side; screen through 1/4-inch hardware cloth to remove remaining worms

**Worm sourcing**: 1-lb starter cultures available for $30–45 from Uncle Jim's Worm Farm, Nature's Good Guys, or local beekeeping and garden supply stores.

### 9.4.6 Hazardous Materials

Some waste streams require special handling regardless of off-grid status. Federal and state laws govern disposal.

**Batteries (lead-acid):**
- Automotive batteries, deep-cycle batteries from solar systems
- All retailers selling lead-acid batteries are required by law to accept old batteries for recycling
- Do not bury, burn, or dump — lead and sulfuric acid contaminate groundwater
- Sealed or AGM batteries: same requirements

**Lithium batteries (LiFePO4, lithium-ion):**
- No federal take-back requirement, but most battery retailers and Call2Recycle locations accept them
- Fire risk if punctured or improperly stored — do not throw in burn barrel
- Earth911.com locator for recycling locations by zip code

**Motor oil and automotive fluids:**
- All auto parts stores (AutoZone, O'Reilly, NAPA) accept used motor oil for free
- Never dump on ground: petroleum contamination, EPA violation
- Coolant and antifreeze: sweet taste attracts animals; toxic; same take-back at auto parts stores

**Paint:**
- Latex paint: can be dried out and landfilled (leave lid off until completely solid)
- Oil-based paint: hazardous waste; county hazardous waste collection events (typically 1–4 times/year)
- PaintCare.org drop-off program active in most states

**Propane tanks:**
- 1 lb (camping cylinders): accept at many hardware stores for recycling
- 20 lb and larger: take to propane dealer for exchange or proper disposal

**Pesticides and herbicides:**
- County hazardous waste collection events; never pour down drain or on ground

**Electronics:**
- E-Stewards certified recyclers: strict chain-of-custody for proper material recovery
- Best Buy and Staples accept most consumer electronics
- Do not burn; do not bury

**Practical approach for remote rural homesteaders**: Accumulate hazardous materials in a dedicated, labeled, leak-proof storage cabinet. Make a quarterly town run specifically to drop off at appropriate collection points. Earth911.com and Call2Recycle.org provide drop-off locators.

---

## 9.5 Pathogen Risk and Health — Epidemiological Summary

### 9.5.1 Transmission Model

The F-diagram (originally from WHO/UNICEF) maps the transmission routes:

**Primary routes:**
- **Fluids** (water): Contaminated water source — the highest volume transmission route
- **Fields** (soil): Contact with contaminated soil, then hand-to-mouth
- **Fingers** (hands): Direct fecal-oral via unwashed hands
- **Flies**: Mechanical transmission by insects from waste to food
- **Food**: Contaminated produce or food prepared with contaminated water or hands

**Barrier interventions by route:**
- Water source protection and treatment → breaks the Fluids route
- Proper waste containment (composting toilet, outhouse, septic) → breaks Fields and Fly routes
- Handwashing → breaks Fingers and Food routes
- Food hygiene → breaks Food route

### 9.5.2 WHO Safe Use Standards

WHO Category A (compost/biosolids safe for unrestricted agricultural use):
- < 1 helminth egg per gram dry weight
- < 1,000 fecal coliforms per gram dry weight
- Requires sustained thermophilic composting (55°C × 3 days) or extended mesophilic composting (1+ year with monitoring)

WHO Category B (safe for restricted agricultural use — non-edible crops, food crops not in direct contact):
- < 10 helminth eggs per gram
- Higher fecal coliform counts acceptable
- Standard cured composting toilet output after 12 months

**Practical guidance**: Test finished compost before use on food crops. The $25–40 cost of a pathogen screen from a university extension lab is negligible compared to the risk of gastroenteritis outbreak from improperly composted material.

---

## 9.6 Legal and Permit Landscape

### 9.6.1 Federal Baseline vs. State Primacy

The EPA's National Pollutant Discharge Elimination System (NPDES) governs discharge of pollutants to surface waters. Septic systems and on-site waste treatment are regulated under state primacy — each state administers its own program within federal minimum requirements.

The EPA's "Guidelines for Water Reuse" (2012, updated guidance ongoing) provides federal recommendations, but these are non-binding. States can be more or less permissive.

**Key federal thresholds affecting off-grid systems:**
- Any system discharging to a surface water (stream, pond) requires an NPDES permit — this is rarely appropriate for on-site systems and generally precludes direct discharge of untreated greywater to waterways
- Underground injection of treated wastewater is governed by the Underground Injection Control (UIC) program — septic drain fields fall under a Class V injection well classification that is typically permitted by operation (no specific permit required for residential septic)

### 9.6.2 States by Off-Grid Sanitation Friendliness

**Most permissive:**
- **Arizona**: Clear greywater regulations; composting toilets allowed; off-grid widely supported
- **California**: Complex regulations but well-defined; composting toilets and greywater both have clear permitting pathways; tiered system allows simple systems permit-free
- **New Mexico**: Generally permissive; clear alternative system support
- **Montana**: Rural areas largely unregulated; county health departments typically practical
- **Idaho**: Rural areas permissive; county dependent

**Moderate:**
- **Oregon**: Regulated but reasonable; DEQ administers; alternative systems permittable
- **Washington**: County dependent; rural counties generally more accommodating
- **Colorado**: Has specific alternative system provisions; permit required but achievable
- **Vermont**: Good alternative system history; regulated but permittable
- **Texas**: Rural counties often permissive; no statewide greywater framework but local adoption growing

**More restrictive:**
- **Florida**: High water table, karst aquifer, and dense population drive strict septic requirements; greywater reuse difficult
- **New York**: Strong regulation; alternative systems require extensive variance process
- **New Jersey**: Dense population and environmental sensitivity drive strict regulation
- **Georgia, Carolinas**: Generally restrictive; septic typically required; greywater prohibited in most counties

### 9.6.3 What "Composting Toilet Legal" Actually Means

This is one of the most misunderstood areas in off-grid planning. "Legal" almost never means "install it and you are done." In most jurisdictions:

1. The composting toilet may require NSF/ANSI 41 certification (commercial units typically have this; DIY units do not)
2. A permitted system for liquid waste is typically also required — either a septic/drain field for greywater, or a permitted greywater system
3. Some codes still require a backup flush toilet to be plumbed, even if the composting toilet is the primary
4. The composting toilet may be considered an "alternative system" requiring an engineer's stamp or county health department approval letter

**The bottom line**: In many jurisdictions, a composting toilet permits you to size your septic system smaller (because you have reduced the liquid waste load by 40–60%) but does not eliminate the need for a permitted liquid waste system. Verify this before buying equipment.

### 9.6.4 Working With County Health Departments

County health departments administer sanitation permits in most of the US. They are not universally adversarial — many rural health inspectors have practical experience and are willing to work with alternative systems when approached properly.

**Approach protocol:**
1. Before buying anything, call the county health department and ask: "I'm planning an off-grid homestead. What are the requirements for on-site sewage, composting toilets, and greywater systems?"
2. Get names. Follow up in writing. Paper trail matters.
3. Bring documentation: manufacturer spec sheets for proposed composting toilet (with NSF 41 certification), site plan showing setbacks, proposed greywater system design
4. Frame the conversation around safety and compliance, not ideology

**Variance and hardship permits:**
Most codes include variance or hardship provisions for situations where strict compliance is technically infeasible or economically prohibitive. These require a formal application, often an engineer's letter, and sometimes a public hearing. For remote rural parcels where septic installation would cost $15,000–$25,000 due to access constraints, a variance for an alternative system is often achievable.

---

## 9.7 System Selection Decision Matrix

| Household size | Land area | Budget | County permitting | Water table | Recommended primary system | Secondary/backup |
|---|---|---|---|---|---|---|
| 1–2 people | Any | < $1,000 | Non-required or rural | Any | DIY two-chamber or humanure | Bucket system |
| 1–2 people | Any | $1,000–2,500 | Any | Any | Nature's Head + L2L greywater | — |
| 2–4 people | 2+ acres | < $1,500 | Rural, flexible | > 4 ft | Outhouse + humanure | Bucket system |
| 2–4 people | 2+ acres | $1,500–5,000 | Moderate | > 4 ft | DIY two-chamber composting + branched drain greywater | — |
| 2–4 people | Any | $5,000–20,000 | Strict permit required | Any | Septic + greywater diversion | Composting toilet planning |
| 4–8 people | 5+ acres | $2,000–5,000 | Rural, flexible | > 4 ft | DIY two-chamber (two units or large) + constructed wetland | — |
| 4–8 people | Any | $10,000+ | Strict permit required | Any | Full septic with ATU + constructed wetland for greywater | — |
| Temporary camp | Any | < $500 | Not applicable | Any | Humanure bucket + cat holes | — |
| Any | 1+ acres | Any | Any | < 2 ft | Composting toilet or septic (mound) + no in-ground greywater | — |

---

## 9.8 CBRN and Nuclear Scenarios

### 9.8.1 Radiation-Contaminated Waste

In a fallout scenario, human waste, vomit, and clothing become radiation-contaminated materials requiring careful handling. The primary risk is internal contamination from ingesting or inhaling radioactive particles, not gamma irradiation from waste itself (at realistic fallout levels).

**Protocol for contaminated waste in fallout scenario:**
1. **Solid waste (fecal)**: Deposit in sealed plastic bags within a covered bucket. Double-bag. Store at distance from living quarters, outdoors in a sealed metal container if possible. Do not apply to garden — Cs-137 and Sr-90 in compost applied to soil will enter the food chain.
2. **Vomit from radiation sickness**: Same containment protocol; radiation sickness vomit is contaminated, not contagious
3. **Contaminated clothing and bedding**: Seal in plastic bags; store separate from living quarters; long-term plan is burial or professional hazmat disposal after the acute phase
4. **Handwashing**: Especially critical after handling any contaminated material; use clean pre-stored water

**Contaminated water and waste disposal:**
- Do not use a greywater-to-landscape system after a fallout event — you would be concentrating radioactive particles in the topsoil of your growing area
- Direct all wastewater to septic or an impermeable containment vessel until radiation levels are assessed with a Geiger counter (see Domain 8 for Geiger counter specs)
- After 2 weeks, gamma radiation from short-lived isotopes (I-131, half-life 8 days) has dropped significantly. Long-lived isotopes (Cs-137, 30-year half-life; Sr-90, 28-year half-life) remain a concern for soil management

**Burial vs. containment:**
- For acute scenario (first 2–4 weeks): sealed containment is preferable — you can test later
- Deep burial (6+ feet) in a non-agricultural area is an acceptable long-term approach for moderate contamination levels after the acute phase
- Do not burn contaminated materials — this aerosolizes radioactive particles

### 9.8.2 Chemical Contamination

If water or food supply contamination from a chemical release (industrial accident, chemical weapon, agricultural chemical spill) is suspected:

- All waste from exposed individuals should be treated as potentially contaminated
- Activated charcoal in sufficient quantity can bind many chemical contaminants in the gut (see Domain 8)
- Wastewater from decontamination showers contains concentrated chemical contaminants — do not route to garden or water source; impermeable containment until verified safe
- Contact Poison Control (800-222-1222) or CHEMTREC (800-424-9300) for specific chemical guidance if you have communications capability

### 9.8.3 Biological Emergency Waste Handling

In a severe infectious disease scenario where household members have confirmed or suspected high-consequence infectious disease (e.g., cholera, Ebola-class hemorrhagic fever):

- Feces and vomit from infected individuals must be treated as highly infectious
- Lime (calcium oxide or calcium hydroxide) directly applied to fecal material before disposal reduces viable pathogens significantly; 1 cup of hydrated lime per gallon of waste, allow 30 minutes contact time
- Separate waste stream from healthy household members' waste
- All PPE (gloves, masks, gowns) used in patient care should be bagged and double-bagged before disposal; bury or burn after clinical phase
- Handwashing after any exposure is non-negotiable; 20-second scrub with soap, clean water

---

## 9.9 Cost and Equipment Table

| Item | Price range | Source | Notes |
|---|---|---|---|
| Nature's Head composting toilet | $960–$1,100 | Nature's Head direct, Amazon | NSF 41 certified; most popular off-grid unit |
| Separett Villa 9215 composting toilet | $1,300–$1,500 | Separett direct, Lehman's | Urine-diverting; biodegradable liners ongoing cost |
| Sun-Mar Excel NE composting toilet | $1,400–$1,700 | Sun-Mar direct, retailers | Non-separating; larger household capacity |
| BioLet 55 NE composting toilet | $1,200–$1,500 | BioLet retailers | Non-separating; compact footprint |
| DIY two-chamber composting system | $200–$500 | Hardware store / salvage | Concrete block + plywood + pallet wood |
| Coco coir bale (10 lb) | $15–25 | Amazon, garden stores | 1–2 bale/year for composting toilet |
| Compost thermometer (long probe) | $15–30 | Amazon, garden stores | 20-inch probe minimum; essential for humanure |
| 5-gallon bucket with lid (per unit) | $8–12 | Home Depot, Lowes | Buy 3–4; rotate when one is full |
| Bucket toilet seat | $10–20 | Amazon, Lehman's | Snap-on; fits standard 5-gallon bucket |
| Outhouse construction (complete DIY) | $300–$500 | Local hardware store | Framing, siding, roofing, seat, vent pipe |
| Pit excavation (tractor hire) | $200–$600 | Local equipment rental | 8-foot depth; 4×4-foot pit; 1–2 hours work |
| VIP vent pipe kit (4-inch black ABS) | $15–25 | Hardware store | 10 feet + screen cap |
| Septic tank (1,000 gal concrete) | $400–$800 | Concrete products supplier | Installed price additional |
| Septic system full installation | $5,000–$15,000 | Licensed contractor | Perc test, permit, tank, drain field |
| Mound septic system | $8,000–$20,000 | Licensed contractor | Poor perc soils |
| Aerobic treatment unit (ATU) | $8,000–$18,000 | Licensed contractor | Norweco, Jet, Consolidated |
| L2L greywater system (complete DIY) | $50–$150 | Hardware store | Ball valve, PVC pipe, mulch |
| Branched drain greywater system (DIY) | $200–$600 | Hardware store | PVC pipe, Y-fittings, surge tank |
| EPDM pond liner (20 mil, per sq ft) | $0.50–0.80 | Pond supply / Amazon | For constructed wetland bed |
| Constructed wetland (60 sq ft, DIY) | $230–$415 | Hardware/landscape supply | Liner, gravel, pipe, plants |
| 3/4-inch washed gravel (per cu yd) | $30–50 | Landscape supply | Wetland media |
| Oasis greywater laundry liquid (gal) | $20–25 | Amazon, Lehman's | Concentrated; greywater-safe |
| EC meter (soil testing) | $15–30 | Amazon | Detect sodium accumulation |
| Worm bin starter kit (worms + bin) | $60–100 | Uncle Jim's Worm Farm, local | 1 lb worms + basic setup |
| Red wiggler worms (1 lb) | $30–45 | Uncle Jim's, Nature's Good Guys | Eisenia fetida; not earthworms |
| 55-gallon steel drum (burn barrel) | $20–60 | Craigslist, industrial surplus | Drill 1-inch holes at base ring |
| Hydrated lime (50 lb bag) | $12–20 | Hardware store, farm supply | Pathogen reduction; also useful for liming soil |
| Geiger counter (RADEX RD1503+) | $60–80 | Amazon | CBRN waste assessment |
| Pathogen test (E. coli + Salmonella) | $25–50 | UMass Extension, state labs | Verify compost safety before food crop use |

---

## 9.10 Skill and Labor Requirements

### 9.10.1 What You Need to Know

**Tier 1 — Essential for anyone installing an alternative waste system:**
- Basic plumbing: cutting and gluing PVC/ABS pipe, compression fittings, angle measurement for slope
- Site assessment: reading a soil probe, percolation test procedure, water table estimation
- Composting fundamentals: C:N ratio concept, moisture assessment, temperature monitoring
- Regulatory awareness: knowing which county agency to call, what questions to ask

**Tier 2 — Required for more complex systems:**
- Greywater system design: slope calculation, distribution layout, surge tank design
- Constructed wetland design: bed sizing, liner installation, plant establishment
- Septic system basics: enough to communicate with a licensed installer and understand what you are buying, and to perform ongoing maintenance correctly

**Tier 3 — Advanced / situational:**
- Biochar production: kiln design and operation, pyrolysis temperature management
- CBRN waste handling protocols
- Pathogen testing interpretation

### 9.10.2 DIY vs. Professional

| Task | DIY feasibility | Notes |
|---|---|---|
| Composting toilet installation | High | Follow manufacturer instructions; requires only basic tools and vent pipe penetration |
| Outhouse construction | High | Standard carpentry; no specialized skills |
| Humanure bucket system | Trivially high | No construction required; discipline is the skill |
| L2L greywater system | High | Washing machine drain reroute; basic plumbing |
| Branched drain greywater | High | PVC plumbing; accessible to anyone comfortable with basic pipework |
| Constructed wetland | Moderate-High | Physical labor (excavation); liner installation requires care but no special skills |
| Septic system installation | Low (permitted work requires licensed contractor in most states) | Design and permitting requires engineer; installation requires equipment |
| Perc test administration | Moderate | Homeowner can dig test holes; formal interpretation may require inspector |
| Biochar kiln construction | High | Cone pit is trivially simple; drum retort requires basic metalwork |
| Hazardous waste disposal | Not DIY | Drop off at designated facilities — do not attempt on-site treatment |

### 9.10.3 Skill Acquisition Path

**For a household planning to install a composting toilet + greywater system:**

1. Read Art Ludwig's *Create an Oasis with Greywater* (6th ed., $20 print / free PDF portions online) — the definitive greywater reference
2. Read Jenkins' *The Humanure Handbook* (3rd ed., free PDF at humanurehandbook.com) — essential for humanure and composting fundamentals
3. Spend 2–3 hours with a basic plumbing guide (YouTube: "How to cut and glue PVC pipe") — covers the physical skills for greywater installation
4. Contact your county health department with specific questions about local code — 30 minutes of prep saves months of uncertainty
5. Install in stages: L2L first (lowest cost, easiest, high confidence), then evaluate whether more complex systems are needed

**For a household planning septic or complex alternative systems:**

1. Hire a licensed sanitation engineer for site evaluation and perc test. Cost: $300–$800. Money well spent.
2. Understand the permit process before committing to a system design — code requirements may constrain your design significantly
3. Get 3 contractor bids; understand what each includes; do not assume the cheapest bid includes all required components

**Time to operational competence:**
- Composting toilet operation: 2 hours reading + 1 installation day → operational
- L2L greywater: 4 hours research + 1 day DIY install → operational
- Branched drain greywater: 1–2 days design + 1–2 days installation
- Constructed wetland: 2–3 days design + 3–5 days construction
- Hot compost / humanure: Ongoing; reaches proficiency after 1–2 full cycles (18–24 months)
- Septic system: Professional installation; homeowner role is maintenance and monitoring

---

## Summary: Priority Sequence

For a homestead at ground zero, prioritize in this order:

1. **Establish a functional human waste system before permanent occupancy.** Bucket system if nothing else is in place. No exceptions. The disease vector risk of no sanitation is acute and fast-moving.
2. **Handwashing infrastructure adjacent to every toilet.** Soap and water. Build this at the same time as the toilet.
3. **Composting toilet or outhouse as the first permanent installation.** Commercial composting toilet ($960–$1,100) or DIY outhouse ($300–$500) are both achievable in the first weeks of site development.
4. **Greywater system second.** L2L from laundry is the entry point — $50–150 in materials, 4 hours of work, and it removes 40+ gallons per day from the waste stream.
5. **Contact county health before building permanent infrastructure.** Expensive mistakes happen when the septic system required by code conflicts with what you installed first. One phone call, early.
6. **Test finished compost before applying to food crops.** $25–40 for a pathogen test is not optional — it is the verification step that makes the system safe.
7. **Build the solid waste reduction systems.** Compost bins, vermicompost, burn barrel, hazardous storage cabinet. These can be phased in after the primary waste systems are established.

> **Central principle**: Every dollar and every hour invested in proper sanitation infrastructure returns in avoided medical costs and avoided contamination of the water and food systems everything else depends on. The homesteader who cuts corners on sanitation is not saving money — they are accumulating a debt payable in illness. Build it right.

---

*Key references: WHO Guidelines for the Safe Use of Wastewater, Excreta and Greywater, Vol. 2 (2006); Jenkins, J. — The Humanure Handbook, 3rd ed. (2005); Ludwig, A. — Create an Oasis with Greywater, 6th ed. (2015); EPA On-Site Wastewater Treatment Systems Manual (2002); NSF/ANSI 41 Standard for Non-Liquid Saturated Treatment Systems; Freeman et al. — Cochrane Review: Handwashing to prevent diarrhea (2014); EPA Guidelines for Water Reuse (2012).*
