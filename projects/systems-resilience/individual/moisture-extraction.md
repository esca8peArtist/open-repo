# Moisture Extraction — Individual Scale
> **Region**: Midwest US (Zone 5) | **Tracks**: Rural + Suburban
> **Scale**: One or two adults, household supplemental water source
> **Cross-references**: [individual/01-water.md](01-water.md) · [midwest/moisture-extraction-farm-tools.md](../midwest/moisture-extraction-farm-tools.md) · [midwest/calendar.md](../midwest/calendar.md)

---

## Quick Reference Card

**Moisture extraction — Zone 5 Midwest viability at a glance:**

| Method | Type | Daily Yield | Power | Zone 5 Feasibility | Cost |
|---|---|---|---|---|---|
| Compressor dehumidifier + filter | Active, electric | 5–15 liters | 300–700 W | Excellent (June–Aug) | $200–400 |
| Desiccant dehumidifier + filter | Active, electric | 3–8 liters | 400–1,000 W | Good (spring/fall/winter) | $250–450 |
| Thermoelectric (Peltier) DIY | Active, low-power | 0.2–1 liter | 70–100 W | Marginal — supplement only | $80–145 |
| Passive desiccant solar panel | Passive, zero power | 0.1–0.5 liter/panel | None | Very low; emergency backup | $45–100 |
| Stone air well (gravity condenser) | Passive, zero power | 0.05–2 liters | None | Low; long-term infrastructure | $50–200 materials |
| Commercial AWG unit | Active, electric | 25–50 liters | 1,000–2,000 W | Good with solar/generator | $1,800–3,000 |

**Primary principle:** Atmospheric moisture extraction is a supplemental water source in Zone 5 — not a primary one. Midwest summer humidity (65–80% RH, June–August) creates the best conditions; winter is poor (20–40% RH). Pair with rainwater collection and well water as your first two sources.

---

## Section 1: How Atmospheric Moisture Extraction Works

### Core Physics

All moisture extraction methods exploit one of two principles:

1. **Condensation (cooling-based):** Cool a surface below the dew point temperature and water vapor condenses out of the air — the same physics that makes a cold glass sweat on a humid day. Compressor dehumidifiers, thermoelectric Peltier units, and commercial AWG machines all use this principle.

2. **Desiccant adsorption:** A material (silica gel, zeolite, lithium chloride) captures water molecules from air through chemical attraction, then releases them when heated. Desiccant dehumidifiers and passive solar panels use this principle.

**Zone 5 dew point context:** At 75°F and 70% relative humidity (typical Zone 5 July morning), the dew point is approximately 63°F. Any surface cooled to 63°F or below will condense water from the air. The midwest's high summer humidity makes this practical; its cold, dry winters make it largely impractical from November through March.

### Zone 5 Seasonal Feasibility

| Season | Avg RH | Dew Point Range | Extraction Viability |
|---|---|---|---|
| June–August | 65–80% | 60–70°F | Excellent — peak production |
| April–May, September–October | 50–65% | 45–60°F | Good — 50% of summer yield |
| November–March | 20–40% | 10–30°F | Poor — not a practical source |

Source: [NOAA Climate Data for the Midwest](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/regional) · [Atmospheric Water Generator overview — Wikipedia](https://en.wikipedia.org/wiki/Atmospheric_water_generator)

---

## Section 2: Commercial Approaches

### Approach 1: Compressor Dehumidifier (Best All-Around Value)

**How it works:** A refrigeration compressor pumps refrigerant through coils, creating a cold surface. A fan draws humid room air across the cold coils, condensing water that drips into a collection reservoir. This is the most efficient condensation method for warm, humid conditions.

**Zone 5 performance:** Compressor dehumidifiers operate most effectively above 60°F (15°C). They are ideal for Zone 5 summer use and marginally functional down to about 41°F (5°C), below which efficiency drops sharply. For summer supplemental water production, this is the best choice.

**Why the collected water is not automatically drinkable:** Standard dehumidifiers are designed for moisture removal, not food-safe water production. The internal coils, tank, and hose materials may leach volatile organic compounds (VOCs) and harbor biofilm. Filtration before drinking is non-negotiable.

**Modified drinkable water system:**

```
[Humid room or outdoor air (summer)]
        ↓
[Compressor dehumidifier — continuous drain mode]
        ↓
[Silicone food-safe drain hose → sealed food-grade reservoir]
        ↓
[Stage 1: 5-micron sediment pre-filter]
        ↓
[Stage 2: Activated carbon block filter (removes VOCs, odors)]
        ↓
[Stage 3: UV-C sterilizer lamp (kills biological threats)]
        ↓
[Drinking water container — sealed, food-grade]
```

**Equipment and cost:**

| Item | Cost | Notes |
|---|---|---|
| Compressor dehumidifier, 30–50 pint | $150–250 | Frigidaire FFAD3033W1, LG PuriCare — both well-reviewed |
| Food-grade 5-gallon reservoir bucket | $5–10 | HDPE #2 |
| Silicone food-safe drain hose, 6 ft | $10–20 | Do not use standard garden hose (not food-safe) |
| 3-stage inline filter housing + cartridges | $30–60 | Sediment + carbon + UV-C or ceramic |
| UV-C sterilizer (if not included in filter set) | $20–40 | 12V models available for solar integration |
| **Total** | **$215–380** | |

**Assembly steps:**
1. Locate the continuous drain port on the rear of the dehumidifier (standard on most units — designed for garden hose attachment)
2. Attach silicone food-safe tubing from drain port; run to sealed reservoir bucket at a lower elevation than the drain port (gravity fed)
3. Add a bulkhead fitting with food-safe gasket where hose enters bucket lid to prevent outside contamination
4. Connect the 3-stage filtration inline between reservoir and a separate drinking container
5. Run the dehumidifier in your most humid indoor space (basement preferred in summer) or a partially sheltered outdoor position

**Expected output:**
- 30-pint unit, 70% RH, 75°F ambient: 6–9 liters/day
- 50-pint unit, same conditions: 10–15 liters/day
- Power consumption: 300–500 watts (7–12 kWh/day)
- Off-grid feasibility: 400+ watt solar array with battery bank can run a 30-pint unit during summer daylight hours

**Zone 5 optimal timing:** Run during peak summer humidity (early morning hours, 5–10 AM, often have highest RH). Running 6–8 hours during this window yields meaningful supplemental water without excessive electricity consumption.

Source: [Compressor vs. Desiccant vs. Thermoelectric Dehumidifiers — Vankool](https://vankool.com/dehumidifier-compressor-vs-desiccant-vs-thermoelectric/) · [How Much Water Can an AWG Make? — Quality Water Treatment](https://qualitywatertreatment.com/blogs/news/how-much-water-can-an-atmospheric-water-generator-make)

---

### Approach 2: Desiccant Dehumidifier (Cold-Season and Year-Round Option)

**How it works:** Air is pulled across a rotating desiccant wheel (typically silica gel or zeolite embedded in a fiberglass matrix). The desiccant absorbs moisture; the wheel rotates through a heated zone where the moisture is driven off as vapor; the vapor is condensed on a cold surface and collected. Unlike compressor units, there is no refrigeration coil.

**Zone 5 advantage:** Desiccant dehumidifiers maintain effectiveness below 5°C (41°F), making them the only practical electric moisture extraction option during Zone 5 spring (March–April) and fall (October–November) when temperatures drop below the compressor's effective range. They are also excellent for unheated garages, outbuildings, and winter basements.

**Disadvantage:** Higher electricity consumption than comparable compressor units — desiccant machines use a heating element to regenerate the desiccant wheel (400–1,000 W vs. 300–500 W for compressor units of similar extraction capacity). Less energy efficient per liter extracted in warm conditions, but the only functional option in cool conditions.

**When to choose desiccant over compressor:**
- Space temperature is regularly below 60°F (15°C): basements, garages, spring/fall use
- You need year-round moisture extraction capability
- You have generator or wood gasifier power that can easily supply 600+ watts

**Commercial options for Zone 5:**

| Unit | Capacity | Power Draw | Cost | Notes |
|---|---|---|---|---|
| Meaco DD8L Zambeze | 8 liters/day | 650 W | $200–280 | Quiet; compact; good for living spaces |
| Ebac BD150 | 14 liters/day | 1,000 W | $300–450 | Industrial-grade; unheated garages/outbuildings |
| Pro Breeze PB-D005 | 500 mL/day | 22.5 W | $35–55 | Mini desiccant for small spaces; not a primary source |

**Filtration requirement:** Same as compressor units — add 3-stage filtration (sediment + carbon + UV-C) before drinking. The desiccant wheel is food-safe, but collection tank and hose require the same treatment as compressor systems.

Source: [Desiccant vs. Compressor Dehumidifiers — EcoAir](https://ecoair.org/pages/desiccant-vs-compressor-dehumidifiers) · [Dehumidifier Desiccant vs. Compressor Guide — HumidityFixers](https://humidityfixers.com/dehumidifiers/dehumidifier-desiccant-vs-compressor/)

---

### Approach 3: Thermoelectric Peltier Dehumidifier (Low-Power Supplement)

**How it works:** The Peltier (thermoelectric) effect passes DC current through a semiconductor junction, creating a cold side and a hot side. Humid air contacts the cold side; water condenses and drips into a collection tray. No compressor, no refrigerant, no moving parts beyond a fan.

**Honest expectation:** Thermoelectric units produce a fraction of the output of compressor models — typically 300–700 mL per day in a single small room at 60–70% RH. This is not enough for primary water supply, but it is a practical low-power supplement and a repairable, DIY-buildable technology (see Section 3).

**Zone 5 application:** Most useful as a continuous-run low-power unit during summer for small spaces (bedroom, pantry) where a larger compressor unit is impractical. Also useful as a 12V solar-powered supplemental unit.

**Commercial mini-desiccant/thermoelectric options:**

| Unit | Capacity | Power | Cost | Notes |
|---|---|---|---|---|
| Eva-Dry Wireless Mini | 100–200 mL/day | 7.5 W (renewable cycle) | $20–30 | Renewable silica desiccant; recharged by plugging in; no continuous power needed |
| SEAVON Electric Dehumidifier | 300–500 mL/day | 22.5 W | $30–45 | Thermoelectric; silent; small rooms |
| Vetsun 1200ML | 500–800 mL/day | 45 W | $40–60 | Slightly higher output; still supplemental |

Source: [Compressor vs. Desiccant vs. Thermoelectric Comparison — Vankool](https://vankool.com/dehumidifier-compressor-vs-desiccant-vs-thermoelectric/) · [Atmospheric Water Generators: A Smart Solution — Quality Water Treatment](https://qualitywatertreatment.com/blogs/water-company/atmospheric-water-generators-for-water-security)

---

### Approach 4: Commercial Atmospheric Water Generator (High-Yield, High-Cost)

For homesteads with a generator or substantial solar array (3+ kW), commercial AWG units designed specifically for potable water production combine condensation, UV sterilization, and multi-stage filtration in a single appliance.

**Key distinction from dehumidifiers:** Commercial AWG units are purpose-built for drinking water. The internal components are food-safe, and the filtration system is integrated. No modification is required.

**Zone 5 performance:** Commercial AWGs achieve best output above 65°F with >60% RH. Zone 5 summer conditions are excellent. They are impractical in winter.

**Commercial options:**

| Unit | Yield/Day | Power | Cost | Notes |
|---|---|---|---|---|
| EcoloBlue 30/30E | ~30 liters (8 gal) | ~1,400 W | $1,800–2,500 | 12-stage filtration built-in; hot and cold dispensing; most popular residential model |
| Watergen GENNY | 25–30 liters | ~1,400 W | $2,200–3,000 | Israeli military-origin technology; 93% energy efficiency vs. other AWG; designed for off-grid |
| Aquair 100 | 10–15 liters | None (wind-powered) | $1,200–1,800 | Wind-driven condenser; no solar or grid power; unusual but viable for windy Midwest plains |

**Cost per gallon:** EcoloBlue states approximately 6 cents per gallon from grid power, rising to ~25–40 cents per gallon from solar power (factoring amortized panel cost).

**Reality check:** At $2,000+ plus power infrastructure, commercial AWG is a significant investment. For Zone 5, a compressor dehumidifier with filtration achieves similar summer output at 10–15% of the cost. Commercial AWG is appropriate when you want an integrated, all-in-one potable water system and have the power infrastructure to support it.

Source: [EcoloBlue AWG Product Line](https://www.ecoloblue.com/49-atmospheric-water-generator) · [Watergen GENNY](https://watergen.com/) · [AWG for Water Security — World Economic Forum](https://www.weforum.org/stories/2024/02/atmospheric-water-generators/)

---

## Section 3: DIY Moisture Extraction Methods

### DIY Method 1: Modified Dehumidifier Build (Highest Practical Yield)

The most practical DIY approach is modifying an inexpensive compressor dehumidifier with food-safe components and proper filtration. This is not building from scratch — it is repurposing existing proven technology with purpose-specific components.

**Full parts list:**

| Item | Approx. Cost | Source |
|---|---|---|
| Used or refurbished 30-pint compressor dehumidifier | $50–150 | Facebook Marketplace, thrift stores, Craigslist |
| Food-grade silicone tubing (1/2" ID, 6 ft) | $10–15 | Amazon, hardware store |
| Food-grade HDPE bucket (5 gallon) with lid | $5–8 | Home Depot, Walmart |
| HDPE bulkhead fitting (1/2") for bucket lid | $3–6 | Amazon |
| 3-stage inline filter housing (standard 10" housings × 3) | $30–50 | Amazon |
| 5-micron polypropylene sediment cartridge | $5–8 | Amazon |
| Activated carbon block cartridge (0.5 micron) | $8–15 | Amazon |
| UV-C sterilizer lamp (12V, 6W) | $15–30 | Amazon |
| 12V power supply for UV lamp | $10–15 | Amazon |
| Food-grade HDPE final storage container (5-gallon with spigot) | $10–15 | Home Depot |
| **Total** | **$146–312** | |

**Assembly procedure (2–3 hours):**

1. **Test the dehumidifier:** Run unit 30 minutes to confirm it extracts water normally. Inspect internal collection tank for visible mold or debris — clean with 1:10 bleach:water solution and rinse thoroughly.

2. **Locate or drill continuous drain port:** Most units have a 3/4" threaded drain port on the rear, covered by a rubber plug. If not present, drill a 3/4" hole at the lowest point of the collection reservoir. Thread in a 3/4" barb fitting.

3. **Connect drain hose:** Push food-grade silicone tubing over the barb fitting. Run the hose to the collection bucket at a lower elevation than the drain port — this is gravity-fed, no pump required. The bucket must be at least 6–12 inches below the drain port for reliable flow.

4. **Seal the bucket:** Drill a hole in the bucket lid to accept the bulkhead fitting. Push hose through bulkhead; seal with food-grade gasket. Bucket should be enclosed to prevent outside contamination of collected water.

5. **Wire filtration in series:** Connect the 5-micron sediment filter, then the activated carbon block filter, then the UV-C sterilizer between the collection bucket and the final drinking water container. Each filter housing connects with standard 1/4" push-fit tubing.

6. **Mount UV lamp:** The UV-C lamp needs a brief dwell time in the water stream. Place it in a section of clear HDPE or quartz tube so water flows past the lamp. Most 12V UV sterilizers include a housing.

7. **Label and date:** Mark the collection bucket "AWG — filter before drinking" and mark the final container "Filtered AWG — safe to drink."

**Flow diagram:**

```
Dehumidifier drain port
        |
        | silicone food-safe hose (gravity)
        ↓
Sealed HDPE reservoir bucket
        |
        | push-fit 1/4" tubing
        ↓
5-micron sediment filter
        |
        ↓
Activated carbon block filter
        |
        ↓
UV-C sterilizer chamber
        |
        ↓
Drinking water container (HDPE, food-grade, with spigot)
```

**Cleaning schedule:** Empty and clean reservoir bucket weekly with dilute food-safe sanitizer (Star San or equivalent). Replace sediment filter every 3–6 months. Replace carbon block filter every 6–12 months. UV-C lamp: check output annually (lamps degrade; a UV-sensing card indicates when output is insufficient).

Source: [DIY Atmospheric Water Generator — Instructables](https://www.instructables.com/DIY-Atmospheric-Water-Generator/) · [DIY AWG Guide — Energy of Supply](https://energyofsupply.com/how-to-make-an-atmospheric-water-generator/) · [How to Build an AWG for Home Use — Life Off-Grid](https://www.lifeoffgrid.org/atmospheric-water-generator/)

---

### DIY Method 2: Thermoelectric Peltier Unit (12V Solar-Compatible Build)

A DIY Peltier unit built from off-the-shelf components produces 200–500 mL per day under good summer conditions. Its primary advantage is compatibility with 12V solar power — it can run directly off a solar panel and battery bank without an inverter.

**Materials list:**

| Item | Cost | Notes |
|---|---|---|
| TEC1-12706 Peltier module (12V, 60W) | $8–15 | Amazon; standard module used in DIY AWG builds |
| Aluminum heat sink with fins, large (hot side) | $12–20 | 40mm × 40mm fins minimum; larger is better |
| Aluminum heat sink with fins, small (cold side) | $8–15 | Smaller, positioned to drip into collection tray |
| 12V brushless fan (80mm) | $8–15 | For hot side heat dissipation |
| Thermal grease (Noctua NT-H1 or similar) | $5–8 | Critical — prevents dry contact failure |
| M4 steel bolts (4) + nuts + washers | $3–5 | Clamping sandwich; stainless preferred |
| Stainless steel drip tray (food-grade) | $8–15 | Position under cold side; angle toward drain |
| Food-grade silicone tubing (drain from tray) | $5–8 | |
| Activated carbon inline filter | $8–15 | Minimum filtration before drinking |
| 12V power supply (10A+) or solar panel + battery | $30–80 | Solar panel: 20W panel sufficient for Peltier + fan |
| Second 80mm fan (optional, for cold side airflow) | $8–12 | Pulls humid air across cold face; increases yield by 30–50% |
| **Total** | **$103–208** | |

**Build procedure:**

1. Apply a thin, even layer of thermal grease (size of a grain of rice) to both faces of the Peltier module. Spread with a straight edge.

2. Sandwich the Peltier between the two heat sinks: large (hot side) on one face, small (cold side) on the other. Use the M4 bolts to clamp the sandwich — finger tight plus 1/4 turn. Do not overtighten: Peltier modules are brittle ceramic and crack under excess pressure.

3. Mount the 80mm fan to the large (hot side) heat sink using the fan's mounting holes, so the fan blows air across the fins and away from the Peltier. This is critical: the hot side must dissipate heat efficiently, or the Peltier cannot maintain a cold differential.

4. Position the small (cold side) heat sink horizontally above the stainless drip tray, tilted slightly (5°) so condensate runs toward one edge and drips into the tray.

5. If using the optional second fan: mount it to draw ambient humid air across the cold face, perpendicular to the heat sink fins. This dramatically increases the rate of condensation by continuously refreshing the air at the cold surface.

6. Drain the drip tray through food-grade silicone tubing into an activated carbon filter and then into a covered collection container.

7. Wire Peltier module and fans to 12V power source. The TEC1-12706 draws approximately 5–6 amps at 12V = 60–72 watts. A 20W solar panel produces sufficient current during peak hours.

**Schematic (ASCII):**

```
              → AIR FLOW →
[Fan] → [HOT SIDE HEAT SINK (large)]
                   |
            [PELTIER MODULE] ← 12V DC power
                   |
         [COLD SIDE HEAT SINK (small)]
                   |      ↑ humid air (second fan, optional)
         (condensate drips down)
                   ↓
         [Stainless drip tray (tilted)]
                   |
         [Silicone drain tube]
                   |
         [Activated carbon filter]
                   |
         [Drinking water container]
```

**Expected yield:** At 70% RH and 75°F ambient: 300–500 mL/day with single cold-side fan; 400–700 mL/day with dual fans. This is enough for emergency drinking water but not a household supply.

**Operational notes:**
- Clean the cold-side heat sink weekly — it accumulates dust and biofilm rapidly in warm, humid conditions
- In >65% RH, condensation begins within 2–3 minutes of power-on
- The unit produces best output during the early morning high-humidity hours in Zone 5

Source: [How to Make an Atmospheric Water Generator: 3 Methods — ScienceInsights](https://scienceinsights.org/how-to-make-an-atmospheric-water-generator-3-methods/) · [DIY Atmospheric Drinking Water Generator — Instructables](https://www.instructables.com/DIY-Atmospheric-Water-Generator/) · [Atmospheric Water Generator — Wikipedia](https://en.wikipedia.org/wiki/Atmospheric_water_generator)

---

## Section 4: Manual and Passive Methods (No Electricity Required)

These methods produce significantly less water than active electric systems, but they require no power and no purchased components beyond materials. They function as emergency backup sources and long-term passive infrastructure. Their primary value in a Zone 5 resilience context is zero operating cost and continued function during extended grid-down periods.

### Manual Method 1: Passive Solar Desiccant Panel

**Principle:** Silica gel desiccant absorbs moisture from night air passively over 8–12 hours, becoming saturated. Enclosed in a solar-heated glass chamber during the day, the moisture is driven off as vapor, rises, condenses on cooler glass, and runs to a collection gutter.

**Materials:**

| Item | Cost | Notes |
|---|---|---|
| Silica gel beads, blue indicator type (1 kg) | $15–25 | Amazon; reusable indefinitely; turns pink when saturated |
| Dark anodized aluminum baking pan (13"×9"×2") | $8–15 | Dark surface maximizes solar absorption |
| Clear tempered glass or polycarbonate sheet (14"×10"×1/4") | $15–35 | Cut to size; lightly frosted sides improve condensate runoff |
| Aluminum angle stock (collection gutter, 12") | $5–8 | Attached at lower edge of glass to catch drips |
| Food-grade silicone tubing (drain) | $5–8 | |
| Weather stripping foam (seal between pan and glass) | $3–5 | Creates closed solar still chamber |
| **Total per panel** | **$51–96** | |

**Construction:**

1. Fill the aluminum pan 1–2 inches deep with silica gel beads, spread evenly.

2. Attach aluminum angle gutter to the lower (tilted) edge of the glass sheet using waterproof silicone sealant.

3. Cut weather stripping to form a gasket around the perimeter of the pan; the glass sheet should rest on this gasket and create a sealed enclosure when closed.

4. Attach food-grade silicone tubing to the gutter drain hole; route to a covered collection container.

5. Mark the assembly with an arrow indicating which end goes down (lower edge with gutter).

**Two-phase operation:**

**Night phase (adsorption, 8–12 hours):** Open the glass panel; expose the silica gel tray to ambient night air. Silica gel absorbs moisture passively as it cools. Blue beads turn progressively pink as they saturate. In Zone 5 summer conditions (70%+ RH at night), the gel reaches saturation in 6–10 hours.

**Day phase (desorption, 4–8 hours):** Close the glass panel over the saturated silica gel tray. Angle 30–45° toward south. Sunlight heats the sealed chamber (often reaching 140–160°F inside on clear summer days), driving moisture off the gel as vapor. Vapor condenses on the cooler glass surfaces; droplets run to the gutter and drain to the collection container.

**Yield:** 100–160 mL per panel per 24-hour cycle in Zone 5 summer (7–9 peak sun hours, 70% RH). Six panels produce 600–960 mL/day — just under 1 liter. This is emergency water, not household supply.

**Schematic (cross-section view):**

```
                  SUNLIGHT ↓ ↓ ↓
  ┌─────────────────────────────────┐
  │      Clear glass/polycarbonate   │
  │                                  │
  │    ← Vapor condenses here ←      │
  │              ↓↓                  │
  │ ┌──────────────────────────────┐ │
  │ │   Silica gel beads (dark pan)│ │← HEAT from solar gain
  │ └──────────────────────────────┘ │
  │              ↓↓ condensate       │
  │           [GUTTER]               │
  └─────────────────────────────────┘
                  ↓
         [Silicone drain tube]
                  ↓
         [Collection container]

TILT: 30–45° facing south
```

**Regenerating silica gel:** Blue indicator gel turns pink when saturated. Dry out in a 250°F oven for 1–2 hours, or in a solar oven/glass-enclosed box. Reuse indefinitely — silica gel does not degrade with repeated cycling.

Source: [Window-sized device taps the air for safe drinking water — MIT News, June 2025](https://news.mit.edu/2025/window-sized-device-taps-air-safe-drinking-water-0611) · [Condensate and Dew Harvesting — Rainwater Harvesting for Drylands and Beyond (Brad Lancaster)](https://www.harvestingrainwater.com/water-harvesting/harvests-of-different-waters/condensate-harvesting/)

---

### Manual Method 2: Stone Air Well (Passive Gravity Condenser)

**Principle:** Dense stones absorb daytime heat and radiate it through the evening, but if the stone mass is cool enough relative to the dew point, condensation forms on the stone surfaces. Water runs down by gravity to a collection basin below. This is an ancient technology: Friedrich Zibold documented large stone condensers near Feodosia, Crimea, in 1900, theorizing they were ancient water supply structures.

**Zone 5 practical reality:** Stone air wells work best in arid regions with large day-night temperature swings. Zone 5's summer nights remain relatively warm and humid, which limits the temperature differential. A well-built stone air well in Zone 5 will produce meaningful condensation on clear, calm nights when humidity is high — but production is highly variable and typically lower than in arid climates. This is a long-term infrastructure investment, not an immediate supply solution.

**Materials:**

| Item | Quantity | Cost | Notes |
|---|---|---|---|
| Dense basalt or granite stones (3"–8" diameter) | 300–500 lbs | $0–80 | Quarry free if sourcing from land; do NOT use limestone, shale, or porous rock |
| Food-grade pond liner or concrete basin (3 ft diameter) | 1 | $20–60 | Collection basin under the stone pile |
| Central perforated PVC pipe (4" diameter, 3 ft long) | 1 | $8–15 | Air chimney through center of pile |
| Clean gravel (1/2" to 1" diameter, for basin drainage) | 50 lbs | $5–15 | Lines bottom of collection basin before pond liner |
| PVC drain pipe (1", 12 ft) | 1 | $8–15 | Drains collected water from basin to storage container |
| **Total materials** | | **$41–185** | Labor intensive; materials inexpensive |

**Build procedure:**

1. **Site selection:** Choose an open, slightly elevated location with maximum sky exposure (radiative cooling requires open sky). Prevailing breeze improves air circulation through the stone pile. Western afternoon shade from a tree or building is beneficial — extends the cooling period before night.

2. **Dig collection basin:** Excavate a pit 3 ft in diameter and 18" deep. Line with 4" of clean gravel. Install food-grade pond liner or pour a shallow concrete basin. Slope the basin floor 2° toward a central drain point. Install the 1" drain pipe through the basin wall at the lowest point.

3. **Install central air chimney:** Set a 3-ft section of 4" perforated PVC pipe vertically in the center of the basin. This creates an air chimney through the stone pile, allowing warm air to rise and draw fresh humid air through the rock gaps from below.

4. **Stack stones:** Begin stacking around the central pipe. Use the largest, densest stones at the base and mid-height. The key to effective condensation is **large gaps between stones** for air circulation — stones touching too closely create insulation, not condensation surface. Stack 3–5 feet total height for meaningful surface area.

5. **Do not use:** Limestone (dissolves and adds minerals to water), shale (too porous), pumice or vesicular rock (internal air pockets act as insulation). Basalt, granite, quartzite, and dense sandstone work well.

6. **Drain connection:** Run 1" PVC drain from the basin to a covered, food-grade collection container at a lower elevation (gravity-fed).

**Schematic (cross-section, not to scale):**

```
     STONE PILE (3–5 ft tall, loosely stacked)
   ╔══════════════════════════════╗
   ║ ▓▓  ▓▓   ▓▓  ▓▓   ▓▓  ▓▓  ║  ← Large stones, large gaps
   ║  ▓▓  ║  ▓▓   ▓▓  ║▓▓      ║
   ║ ▓▓   ║  ▓▓  ▓▓   ║ ▓▓ ▓▓  ║  ← Air chimney (perforated PVC)
   ║  ▓▓  ║  ▓▓  ▓▓   ║ ▓▓     ║
   ╟───────╨──────────╨─────────╢
   ║         COLLECTION BASIN    ║  ← Pond liner / concrete
   ║  (gravel base, 3 ft wide)   ║
   ╚══════════════════|══════════╝
                      |
             1" drain pipe (gravity)
                      |
             Covered collection container
```

**Expected yield:** 50–500 mL per day in Zone 5 summer (highly variable based on night temperature, humidity, and stone mass quality). The ancient Zibold structures reportedly yielded far more, but those were enormous (10+ meter diameter) stone structures. A garden-scale 4-ft pile produces modest but real water. Scale up by adding more pile width and stone mass.

**Maintenance:** No mechanical maintenance. Annual inspection: check that drain pipe remains clear of debris; inspect pond liner for damage; remove any moss or organic growth from stone surfaces (reduces condensation surface).

Source: [Air Well (Condenser) — Wikipedia](https://en.wikipedia.org/wiki/Air_well_(condenser)) · [Passive Dew Harvesting For Gardens — EcoSnippets](https://www.ecosnippets.com/permaculture/passive-dew-harvesting-for-gardens/) · [How to Pull Water Out of Air Using Only Gravity — Anthropocene Magazine, 2024](https://www.anthropocenemagazine.org/2024/10/pullithe-air-contains-6x-more-water-than-all-the-worlds-rivers-heres-how-to-harvest-it/)

---

### Manual Method 3: Mesh Dew Collector (Radiation Fog Net)

**Principle:** Fog nets and dew collectors use a surface with high surface area to intercept water droplets from fog or high-humidity air, allowing them to coalesce and drain by gravity. Most effective in areas with regular radiation fog (common in Midwest river valleys on clear, calm summer mornings).

**Materials:**

| Item | Cost | Notes |
|---|---|---|
| Polypropylene shade cloth (30–50% density) or polyester mesh (1mm grid) | $15–30 | 4 ft × 6 ft panel minimum |
| PVC pipe frame (1" diameter, 4-piece) | $15–25 | Mount mesh taut and vertical |
| Collection trough (aluminum gutter section, 4 ft) | $8–15 | Mounted at bottom of mesh |
| Food-grade drain hose | $5–8 | From trough to container |
| **Total** | **$43–78** | |

**Setup:**
1. Build a simple rectangular PVC frame (4 ft wide × 6 ft tall is a common size)
2. Stretch mesh taut across the frame (loose mesh loses water; taut mesh coalesces it)
3. Angle the frame slightly (5–10°) so water runs down to the lower edge
4. Mount aluminum gutter at the lower edge to collect dripping water
5. Orient perpendicular to prevailing morning wind

**Yield:** Highly dependent on local fog conditions. In river valley fog: 0.5–3 liters per foggy morning per 24 sq ft of mesh. On non-foggy nights: essentially zero in Zone 5 (unlike coastal fog regions). This is an opportunistic supplement, not a reliable source.

**Zone 5 context:** Midwest river valleys (Illinois River, Mississippi River corridor, Kankakee River area, Wisconsin river valleys) experience radiation fog on clear autumn mornings regularly. A fog net positioned in these areas can collect meaningful water opportunistically. For gardens and seedlings, the collected water is excellent — not requiring the same level of filtration as drinking water.

Source: [Atmospheric Water Harvesting — ACS Materials Letters](https://pubs.acs.org/doi/10.1021/acsmaterialslett.0c00130) · [Condensate and Dew Harvesting — Brad Lancaster / HarvestingRainwater.com](https://www.harvestingrainwater.com/water-harvesting/harvests-of-different-waters/condensate-harvesting/)

---

## Section 5: Water Safety for All AWG Methods

Regardless of extraction method, treat all collected moisture before drinking:

**Minimum treatment requirements:**

1. **Sediment pre-filter (5 micron):** Removes particulates and large biological matter from the water stream. Replace every 3–6 months or when flow rate drops significantly.

2. **Activated carbon block filter (0.5 micron):** Removes volatile organic compounds (VOCs), chlorine byproducts, taste and odor compounds, and reduces microbial load. This is the most important treatment step for AWG water, which can concentrate VOCs from paint, cleaning products, and pesticides in the surrounding air. Replace every 6–12 months.

3. **UV-C sterilization or boiling:** Kills bacteria, viruses, and protozoa that survive filtration. UV-C at adequate intensity (40 mJ/cm² or higher) is the most practical inline option. Boiling (1 minute rolling boil) is a no-cost alternative if filtering batch quantities.

**Do not use AWG water for drinking if:**
- The unit has been running near any chemical storage (paint, solvents, pesticides, cleaning products, fuel) — VOCs concentrate into condensate
- Equipment has not been cleaned in >2 weeks (biofilm and mold risk)
- Water has a chemical smell or unusual appearance after filtration

**Collection and storage:**
- Store in sealed, food-grade containers (HDPE #2 or glass)
- Label with collection date; rotate within 72 hours or re-treat
- Keep collection containers in dark locations to prevent UV degradation and algae growth

---

## Section 6: Maintenance and Materials Schedule

### Annual Maintenance Calendar

| Month | Task | Time Required |
|---|---|---|
| May | Activate AWG system for summer; run test cycle; check all hose connections | 30 min |
| May | Replace activated carbon filter cartridge (annual) | 15 min |
| June–August | Weekly reservoir cleaning; weekly cold-side heat sink cleaning on Peltier units | 15 min/week |
| June–August | Regenerate silica gel panels if using passive desiccant method | 2 hrs |
| August | Test UV-C lamp output with UV indicator card | 10 min |
| September | Replace sediment filter before end-of-season shutdown | 15 min |
| October | Shut down outdoor AWG components; drain all hoses; store in frost-free location | 30 min |
| October | Regenerate silica gel; store dry in sealed container until spring | 1 hr |

### Replacement Parts and Shelf Life

| Component | Replace When | Shelf Life if Unused | Cost |
|---|---|---|---|
| 5-micron sediment filter cartridge | Every 6 months or when flow drops | 3–5 years sealed | $5–8 |
| Activated carbon block filter | Every 12 months | 3–5 years sealed | $8–15 |
| UV-C lamp | Every 2 years (output degrades before it fails visibly) | 5 years | $15–30 |
| Silicone drain tubing | Every 3–5 years or when cracked | Indefinite if stored cool/dark | $10–20 |
| Silica gel | Never — regenerate indefinitely | Indefinite | — |
| TEC1-12706 Peltier module | When efficiency drops (test with thermometer) | 10+ years if properly assembled | $8–15 |

---

## Equipment Recommendations by Homestead Size

| Setup | Primary Method | Secondary Method | Annual Water Yield (Summer) | Cost |
|---|---|---|---|---|
| Suburban apartment | Mini desiccant (Eva-Dry) | None practical | 30–75 liters | $25–40 |
| Suburban home with basement | 30-pint compressor + filter | Passive desiccant panel | 600–1,200 liters | $200–350 |
| Rural homestead, no tractor | 50-pint compressor + filter | Stone air well | 1,000–2,500 liters | $300–500 |
| Rural homestead with solar array | Commercial AWG (EcoloBlue) | Compressor dehumidifier | 5,000–9,000 liters | $2,000–2,800 |

**Contextual note:** Even at maximum summer output (15 liters/day from a 50-pint compressor unit), AWG production covers roughly 5–7 days of one person's full water needs per week in summer. AWG is a meaningful supplement to stored water, rainwater collection, and well water — it rarely replaces them.

---

## Primary Sources

### Atmospheric Water Extraction — Physics and Technology
- [Atmospheric Water Generator — Wikipedia](https://en.wikipedia.org/wiki/Atmospheric_water_generator) — Overview of all AWG technologies and methods
- [How Much Water Can an AWG Make? — Quality Water Treatment](https://qualitywatertreatment.com/blogs/news/how-much-water-can-an-atmospheric-water-generator-make) — Yield calculations under different humidity conditions
- [Atmospheric Water Generators: A Smart Solution — Quality Water Treatment](https://qualitywatertreatment.com/blogs/water-company/atmospheric-water-generators-for-water-security) — Commercial and DIY AWG guide
- [AWG for Water Security — World Economic Forum](https://www.weforum.org/stories/2024/02/atmospheric-water-generators/) — Market overview and efficiency comparisons
- [Atmospheric Water Generation Research — US EPA](https://19january2021snapshot.epa.gov/water-research/atmospheric-water-generation-research_.html) — EPA research overview
- [Solar-Powered Atmospheric Water Generator — IJIRSET (2018)](https://www.ijirset.com/upload/2018/january/6_IJIRSET_Paper_Solar%20Powered%20%20Atmospheric%20Water%20Generator%20-%20FINAL.pdf)

### Dehumidifier Types and Comparison
- [Compressor vs. Desiccant vs. Thermoelectric — Vankool Guide](https://vankool.com/dehumidifier-compressor-vs-desiccant-vs-thermoelectric/) — Comprehensive type comparison
- [Desiccant vs. Compressor Dehumidifiers — EcoAir](https://ecoair.org/pages/desiccant-vs-compressor-dehumidifiers) — Performance at low temperatures
- [Dehumidifier Desiccant vs. Compressor — HumidityFixers](https://humidityfixers.com/dehumidifiers/dehumidifier-desiccant-vs-compressor/) — Cost and effectiveness comparison
- [Compressor v. Desiccant — Honeywell Air Comfort](https://honeywellaircomfort.com/blogs/news/compressor-v-desiccant-dehumidifiers-which-kind-is-right-for-me) — Best-use-case guide

### DIY Build Instructions
- [DIY Atmospheric Drinking Water Generator (with Pictures) — Instructables](https://www.instructables.com/DIY-Atmospheric-Water-Generator/) — Step-by-step with photographs
- [How to Make an Atmospheric Water Generator: 3 Methods — ScienceInsights](https://scienceinsights.org/how-to-make-an-atmospheric-water-generator-3-methods/) — Peltier, dehumidifier, and desiccant methods
- [How to Build an AWG for Home Use — Life Off-Grid](https://www.lifeoffgrid.org/atmospheric-water-generator/) — Practical homestead-scale build
- [DIY AWG Guide — Energy of Supply](https://energyofsupply.com/how-to-make-an-atmospheric-water-generator/) — Component sourcing and assembly
- [How to Build a Homemade AWG — Practical Survivalist](https://practicalsurvivalist.com/diy-video-how-to-build-a-homemade-atmospheric-water-generator-produces-extracts-distilled-water-from-the-air/)

### Passive and Manual Methods
- [Passive Dew Harvesting For Gardens — EcoSnippets](https://www.ecosnippets.com/permaculture/passive-dew-harvesting-for-gardens/) — Stone air well design and dew harvesting methods
- [Air Well (Condenser) — Wikipedia](https://en.wikipedia.org/wiki/Air_well_(condenser)) — Historical context, Zibold's research, design types
- [How to Pull Water Out of Air Using Only Gravity — Anthropocene Magazine, 2024](https://www.anthropocenemagazine.org/2024/10/pullithe-air-contains-6x-more-water-than-all-the-worlds-rivers-heres-how-to-harvest-it/) — Radiative cooling and passive condensation research
- [Condensate and Dew Harvesting — Rainwater Harvesting for Drylands and Beyond (Brad Lancaster)](https://www.harvestingrainwater.com/water-harvesting/harvests-of-different-waters/condensate-harvesting/) — Comprehensive passive collection guide
- [Window-Sized Device Taps Air for Safe Drinking Water — MIT News, June 2025](https://news.mit.edu/2025/window-sized-device-taps-air-safe-drinking-water-0611) — Latest passive AWG research
- [Atmospheric Water Harvesting: A Review — ACS Materials Letters](https://pubs.acs.org/doi/10.1021/acsmaterialslett.0c00130) — Academic review of harvesting materials and designs
- [Harvesting Drinking Water from Humid Air Around the Clock — ScienceDaily (2021)](https://www.sciencedaily.com/releases/2021/06/210623141652.htm) — Hydrogel passive AWG research

### Commercial AWG Products
- [EcoloBlue AWG Product Line](https://www.ecoloblue.com/49-atmospheric-water-generator) — Residential and commercial units
- [EcoloBlue 30E Specifications](https://www.ecoloblue.com/atmospheric-water-generator/228-148-ecoloblue-30e) — 12-stage filtration; 30 liters/day
- [Watergen GENNY](https://watergen.com/) — High-efficiency military-origin AWG

---

## Cross-References

- **Primary water systems**: See `individual/01-water.md` — AWG output integrates with the rainwater + well system; use during summer dry spells to reduce draw on stored reserves
- **Farm tools and atmospheric extraction (existing reference)**: See `midwest/moisture-extraction-farm-tools.md` — covers AWG basics and farm planting tools in combined format
- **Annual timing**: See `midwest/calendar.md` — AWG startup/shutdown months, filter replacement schedule
- **Food security**: See `individual/02-food.md` — AWG water for seedling irrigation during dry spells
- **Energy systems** (when created): AWG power requirements and solar sizing
