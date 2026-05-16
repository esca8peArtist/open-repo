# Moisture Extraction + Farm Tools — Individual Scale
> **Region**: Midwest US (Zone 5) | **Tracks**: Rural + Suburban
> **Scale**: One or two adults, small homestead or garden plot
> **Cross-references**: [individual/01-water.md](../individual/01-water.md) · [individual/02-food.md](../individual/02-food.md) · [midwest/calendar.md](calendar.md)

---

## Quick Reference Card

**Atmospheric moisture extraction — Midwest viability at a glance:**

| Method | Equipment | Water Yield/Day | Power Needed | Zone 5 Feasibility |
|---|---|---|---|---|
| Modified dehumidifier + filter | Dehumidifier, 3-stage filter | 3–10 liters | 300–500 watts | Good (summer: 60–80% RH) |
| Thermoelectric (Peltier) unit | Peltier module, heat sinks, fan | 0.2–1 liter | 70–100 watts | Marginal — supplement only |
| Solar desiccant panel | Silica gel, glass panel | 0.06–0.16 liters | None (solar passive) | Very low yield; backup only |
| Commercial AWG unit | Purpose-built appliance | 10–50 liters | 500–1,500 watts | Good with solar or generator |

**Two-person farm tool summary:**

| Tool | Two-Person Use | Source | Cost |
|---|---|---|---|
| Walk-behind push seeder (single row) | One pushes, one marks rows | EarthWay 1001-B, Hoss Seeder | $120–$200 |
| Water wheel transplanter (tractor-towed) | Operator drives; one feeds transplants | Water Wheel / Mechanical Transplanter Co. | $800–$2,000 |
| Two-row 3-pt hitch planter | Tractor only; two-person benefit in setup | Field Tuff, Knapik | $400–$1,200 |
| Hand-dibble + seed pouch (manual) | One dibbles, one drops seeds | DIY / any supplier | $10–$30 |

---

## Section 1: Atmospheric Moisture Extraction

### How It Works — Core Physics

The atmosphere contains water vapor at all times. At 70°F with 60% relative humidity, there are approximately 12–15 grams of water vapor per cubic meter of air. Zone 5 Midwest summers regularly reach 70–85% relative humidity from June through August — excellent conditions for extraction. Winters are less hospitable (20–40% RH), making this primarily a warm-season supplemental source.

All extraction methods exploit one of two physics principles:

1. **Condensation (cooling-based):** Cool a surface below the dew point and water condenses out of the air, just as a cold glass sweats on a humid day. This is how dehumidifiers and most AWG systems work.
2. **Desiccant adsorption (passive):** A desiccant material (silica gel, calcium chloride, or zeolite) captures water molecules from air by chemical attraction, then releases them when heated — using sunlight or waste heat.

### Zone 5 Feasibility Assessment

**Summer (June–August):** Best conditions. Midwest average July humidity is 65–75% in the morning; dew points of 65–70°F are common in Illinois, Indiana, Iowa, and Wisconsin. A good-quality dehumidifier running 8–10 hours during this period reliably yields 5–10 liters per day. This is meaningful supplemental water.

**Spring and Fall (April–May, September–October):** Moderate conditions. 50–65% humidity; yields drop to 2–5 liters per day from a dehumidifier.

**Winter (November–March):** Poor conditions. Cold, dry air with 20–40% RH yields very little. Atmospheric extraction is not a viable water strategy during Midwest winters. Prioritize well, cistern, and snowmelt for this period.

**Key constraint:** Atmospheric extraction uses electricity. In a grid-down scenario, it requires solar panels or a generator — both are feasible additions but increase cost and complexity. Plan atmospheric extraction as a supplemental source, not a primary one.

### Method 1: Modified Dehumidifier (Best Practical Option)

This is the highest-yield, most practical approach for Midwest homestead use. A standard dehumidifier is a condensation machine — it already does the core extraction step. The modification is adding food-safe filtration so the collected water is drinkable.

**Why dehumidifier water is NOT automatically drinkable:** The internal tank and coils of a standard dehumidifier are not designed for food contact. Water can contain dust, mold, volatile organic compounds, and microbial growth from standing in the tank. Filtration is not optional.

**System design:**

```
[Humid room or outdoor air]
        ↓
[Dehumidifier — condenses moisture onto coils]
        ↓
[Collection → Drain hose → Sealed food-grade reservoir]
        ↓
[Stage 1: Sediment pre-filter (5 micron)]
        ↓
[Stage 2: Activated carbon filter (removes VOCs, odors)]
        ↓
[Stage 3: UV-C sterilizer lamp or ceramic filter]
        ↓
[Drinking water container]
```

**Equipment list:**
- Dehumidifier, 20–30 pint (compressor-based; NOT thermoelectric/Peltier): $150–250 (Frigidaire, LG, GE)
- Food-grade 5-gallon bucket or sealed container for reservoir: $5–10
- Drill for drain port modification: already owned
- 3-stage inline filter: $30–60 (sediment + carbon + UV or ceramic); available Amazon, Walmart
- Silicone food-safe drain hose: $10–20
- Total cost: $200–350

**Assembly steps:**
1. Identify the drain port on the rear of the dehumidifier (most units have a continuous-drain port for garden hose use)
2. Connect food-safe silicone tubing from drain port to the reservoir bucket, sealed with a food-safe bulkhead fitting to prevent contamination
3. Connect inline 3-stage filtration between reservoir and a separate drinking container
4. Position the dehumidifier in your most humid space — basement, humid room, or partially sheltered outdoor space during summer
5. Run the unit during warm daytime hours; drain to reservoir continuously
6. Filter water on demand through the 3-stage system before drinking

**Expected yield:**
- 20-pint unit, 70% RH, 75°F: 4–7 liters/day
- 30-pint unit, same conditions: 6–10 liters/day
- Power consumption: 300–500 watts continuous (7–12 kWh/day)
- With a 400-watt solar array and sufficient batteries, this is feasible off-grid during summer

**Important note on dehumidifier placement:** If running indoors, the heat the unit exhausts into the room is significant — it will raise room temperature. In summer this is not ideal unless the space is large and ventilated. Running it in a partially sheltered outdoor position during summer is more efficient.

**Source:** [Atmospheric Water Generators: A Smart Solution for Water Security](https://qualitywatertreatment.com/blogs/water-company/atmospheric-water-generators-for-water-security) · [DIY AWG Guide — Energy of Supply](https://energyofsupply.com/how-to-make-an-atmospheric-water-generator/)

---

### Method 2: Thermoelectric Peltier Unit (DIY Build)

The Peltier module is a solid-state thermoelectric device — run current through it and one face gets hot, the other gets cold. No moving parts beyond a fan. This makes it repairable and buildable from common components.

**Honest expectation:** A single Peltier unit yields 200–500 mL per day in good conditions (65%+ humidity, warm air). This is not enough for a primary water source but is a useful skill to have and a real backup source for drinking water in emergencies.

**Materials list:**
- TEC1-12706 Peltier module (12V, 60W): $8–15 (Amazon)
- Two aluminum heat sinks with fins: $10–20 each
- 12V DC brushless fan (80mm): $8–15
- 12V power supply (6+ amps, or solar panel + battery): $20–40
- Thermal grease: $5
- Stainless steel collection tray or food-safe plastic drip pan: $8–15
- Steel bolts (M3 or M4) for clamping sandwich: $3–5
- Food-grade tubing for drainage: $8–10
- Activated carbon inline filter: $10–20
- Total: $80–145

**Build steps:**
1. Apply a thin, even layer of thermal grease to both faces of the Peltier module
2. Sandwich the Peltier between the two heat sinks with the hot side on one, cold side on the other; clamp with steel bolts — do not overtighten (Peltier modules crack under excess pressure)
3. Mount the fan to the hot-side heat sink so it blows air across the fins and away from the cold face
4. Position the cold-side heat sink horizontally above the collection tray so condensation drips down
5. Connect to 12V power source (or solar panel directly during daylight hours)
6. Water collects on cold face and drips into tray; drain through carbon filter to drinking container

**Schematic (ASCII):**
```
         FAN → [HOT SIDE HEAT SINK]
                        |
                 [PELTIER MODULE]
                        |
               [COLD SIDE HEAT SINK]  ← Water condenses here
                        ↓
              [Collection Tray / Drip Pan]
                        ↓
             [Activated Carbon Filter]
                        ↓
                 [Drinking Container]

Power: 12V DC supply or solar panel → Peltier + Fan
```

**Operational notes:**
- Unit works best when ambient air circulates around the cold face — add a second small fan pointing AT the cold side to pull humid air across it
- In >60% RH conditions at room temperature, condensation begins within minutes of startup
- Clean collection tray weekly with mild soap + rinse; dry completely before restarting to prevent microbial growth in tray

**Source:** [How to Make an Atmospheric Water Generator: 3 Methods — ScienceInsights](https://scienceinsights.org/how-to-make-an-atmospheric-water-generator-3-methods/) · [Wikipedia: Atmospheric Water Generator](https://en.wikipedia.org/wiki/Atmospheric_water_generator)

---

### Method 3: Passive Solar Desiccant Panel (No Electricity Required)

This is the only method that works without power. It produces very little water — 57–161 mL per day per window-sized panel in research conditions — but it works completely passively and is a survival-level skill.

**Materials:**
- Silica gel beads (bulk, blue indicator type): $15–25/kg (Amazon) — reusable indefinitely
- Dark metal tray (aluminum baking pan, angled slightly): $5–15
- Clear glass or polycarbonate panel (window-sized, for solar heating chamber): $20–50
- Collection gutter (aluminum channel at low end of tray): $5–10
- Food-grade container: already owned
- Total: $45–100 per panel

**Two-phase operation:**

**Phase 1 — Night (adsorption):** Expose the desiccant tray to open night air. Silica gel absorbs moisture from the air passively, becoming saturated over 8–12 hours.

**Phase 2 — Day (desorption):** Seal the now-moist silica gel tray inside the clear glass enclosure. Sunlight heats the desiccant; moisture releases as vapor; vapor rises and condenses on the cooler glass panels; condensate runs down to collection gutter.

**Operational detail:**
- For best results, orient the glass enclosure facing south at a 30–45° tilt (matching latitude) to maximize solar gain
- Tilt the collection tray 5–10° so condensate runs toward gutter
- Use a small drip tube (food-grade silicone) to drain from gutter to covered container
- In full Zone 5 summer sun (7–9 peak sun hours), expect one 24-hour cycle to yield 100–160 mL per panel
- Scale: six panels = 600–960 mL/day (just under 1 liter) — marginal but real emergency water

**Regenerating silica gel:** Silica gel turns pink when saturated (with indicator type) and blue when dry. A saturated batch can be dried out in a 250°F oven for 1–2 hours or in a solar oven, then reused indefinitely.

**Sources:** [Window-sized device taps the air for safe drinking water — MIT News, June 2025](https://news.mit.edu/2025/window-sized-device-taps-air-safe-drinking-water-0611) · [ScienceInsights DIY Methods](https://scienceinsights.org/how-to-make-an-atmospheric-water-generator-3-methods/)

---

### Water Safety for All AWG Methods

Regardless of extraction method, treat AWG-collected water before drinking:

1. **Always filter** through at least activated carbon (removes VOCs, taste, and odor)
2. **Add a UV-C stage or boil** — condensation kills biological threats already present in the tank but does not sterilize ongoing exposure to the environment in the collection tray
3. **Clean equipment weekly** — biofilm forms quickly in warm, moist collection systems
4. **Store in sealed, food-grade containers** — do not leave collected water open to air for more than a few hours
5. **Do not consume if unit has been running near chemicals** — paint, cleaning supplies, pesticides — VOCs concentrate into condensate

**Midwest summer integration with water system:** AWG output pairs well with the rainwater collection cistern described in `individual/01-water.md`. During dry summer stretches when rain is absent, a dehumidifier running 8 hours/day can yield 5–10 liters — roughly 3–5 days of drinking water per person, reducing draw on stored reserves.

---

### Commercial AWG Options (If Resources Allow)

For those with a generator or substantial solar array:

| Unit | Yield/Day | Power | Cost | Notes |
|---|---|---|---|---|
| EcoloBlue 28 | 28 liters | ~1,200 watts | $1,800–2,500 | Compressor-based; reliable; built-in UV/RO |
| WaterGen GENNY | 25–30 liters | ~1,400 watts | $2,200–3,000 | Israeli military-origin technology; very efficient |
| Aquair 100 | 10–15 liters (gravity) | None (wind-powered) | $1,200–1,800 | Wind-driven; no solar needed; unusual option |

Source: [World Economic Forum — Atmospheric Water Generators](https://www.weforum.org/stories/2024/02/atmospheric-water-generators/) · [Quality Water Treatment — AWG Guide](https://qualitywatertreatment.com/blogs/water-company/atmospheric-water-generators-for-water-security)

---

## Section 2: Farm Tools for Two-Person Teams

### Philosophy for Small-Scale Homestead Planting

For a 1/4-acre intensive garden (4,800–10,890 sq ft, as described in `individual/02-food.md`), most planting can be done by one person with quality hand tools. Two-person operation shines in specific bottlenecks:

- **Large-area row seeding** (corn, beans, squash — caloric crops over 800+ sq ft)
- **Transplanting** (hundreds of seedlings under time pressure to beat a weather window)
- **Tractor-assisted operations** (one drives, one monitors implement or feeds transplants)

The tools below are organized from most to least infrastructure-intensive.

---

### Tool 1: Tractor-Towed Two-Row Planter (Rural, Tractor-Required)

For homesteads with a compact or subcompact tractor (15–45 HP), a 3-point hitch two-row planter dramatically reduces planting time for caloric crops.

**How it works:** The planter attaches to the tractor's Category 1 three-point hitch. As the tractor moves forward, press-wheels or coulters open furrows, seed plates meter seed at preset spacing, and closing wheels cover the furrow. A two-row planter covers two rows simultaneously with each pass.

**Field Tuff 3-Point 2-Row Corn and Bean Planter:**
- Compatible with tractors 25–45 HP; Category 1 three-point hitch
- Adjustable row width: 14" to 36.6"
- Each hopper holds up to 0.22 bushels (~15 lbs) of seed
- Works for corn, soybeans, and dried beans — all high-caloric crops
- Cost: $400–$600 (Tractor Supply, Rural King)
- Source: [Field Tuff 2 Row Planter — YouTube overview](https://www.youtube.com/watch?v=bx5Em_3DK4s) · [Smallest Two Row Corn Planter for Subcompact Tractor — YouTube](https://www.youtube.com/watch?v=uogwqEuFbo8)

**Two-person value:** Driver operates tractor; second person monitors seed hoppers (which empty at ~1/4 acre per fill at Zone 5 typical row spacing), clears any seed jams, and records pass count and planting pattern. For solo operation the tractor can be left on auto-guidance if available, but that is far above this document's scope.

**Knapik Hydraulic 2-Row Planter (H2L model):**
- Brazilian-made; designed for small-farm market; widely available online
- Hydraulic downforce for consistent depth control
- Works with 15–30 HP compact tractors
- Available through specialty importers: [Knapik H2L on plantknapik.com](https://plantknapik.com/product/knapik-hydraulic-planter-2-rows-2/?lang=en)
- Cost: $700–$1,200 imported

---

### Tool 2: Water Wheel Transplanter (Tractor-Towed, Two-Person Operation)

The water wheel transplanter is the most practical mechanized tool for transplanting vegetable seedlings — tomatoes, peppers, cabbage, broccoli, kale — in the Zone 5 Midwest garden.

**How it works:** A large diameter wheel with molded cups (the "water wheel") rotates as the tractor pulls the implement forward. Each cup holds water that is injected into the soil at the plant spacing interval, opening a hole and wetting it simultaneously. A person riding on the seat behind the wheel drops a transplant into each hole; trailing press wheels firm the soil around roots.

**Two-person operation:** One person drives the tractor at walking speed (0.5–1 mph). One or two operators (one per row) sit on the rear seat(s) and drop transplants from a tray into the water cups as they come around. Experienced transplant operators can place 1,000–2,000 plants per hour per row.

**Equipment options:**
- **Rainflo 1270 Water Wheel Transplanter:** Category I or II 3-point hitch; single row; seats 1 operator; plant spacing 8"–24" adjustable; drench rate adjustable; Cost: $900–$1,400. Available through [Berry Hill Drip](https://www.berryhilldrip.com/product/equipment/planters-and-wheels/1270-water-wheel-transplanter-rainflo/)
- **Mechanical Transplanter Co. 3-Point Hitch Model:** Single or two-row; similar function; [mechanicaltransplanter.com](https://mechanicaltransplanter.com/products/three-point-hitch); Cost: $1,200–$2,000

**Zone 5 timing application:** For Zone 5 Midwest spring transplanting (May window after last frost ~April 15), a two-person team can transplant a 1/4-acre plot of tomatoes, peppers, and brassicas in one afternoon rather than 2–3 days of hand planting.

---

### Tool 3: Walk-Behind Single-Row Push Seeder (No Tractor Required)

The most practical seeding tool for a Zone 5 homestead without a tractor. One person pushes, the seeder plants. A second person can assist by marking row spacing with a rope or row marker ahead of the seeder operator, or by managing the seed supply.

**How it works:** Fill the hopper with seeds; select the appropriate seed plate for the crop; push the seeder forward in a prepared bed. A furrow opener cuts the row; the seed plate meters seeds into the furrow; a closing wheel or chain covers seeds to the set depth. Consistent spacing and depth — far better than hand-planting.

**EarthWay 1001-B Precision Garden Seeder:**
- Weight: ~12 lbs; all steel frame
- 7 interchangeable seed plates cover 38 seed types (corn, beans, peas, beets, carrots, onions, radishes, sunflowers)
- Row marker guides the next row pass for consistent 6"–36" spacing
- Planting depth adjustable via chain position
- Cost: $110–$140 (Amazon, Tractor Supply, Ace Hardware)
- Source: [Amazon EarthWay 10001](https://www.amazon.com/Earthway-1001-B-Precision-Garden-Seeder/dp/B00002N66A)

**Hoss Garden Seeder (higher quality alternative):**
- Weight: 18 lbs; heavier steel construction; more forgiving in tough soil
- Flat round seed plates in three thicknesses (3/32", 3/16", 1/4"); hole patterns create spacing from 1¼" to 19"
- Row marker adjusts from 10"–36" wide; swaps left-right for consecutive passes
- Best for Zone 5 homesteads with clay-heavy or partially worked soil
- Cost: $175–$215 (Hoss Tools direct or Amazon)
- Source: [Hoss Garden Seeder — EasyDigging guide](https://www.easydigging.com/seeders-planters/hoss-garden-seeder.html)

**Two-person workflow with a push seeder:**
1. Person A: marks row spacing using a pre-measured rope or the seeder's built-in row marker. Stakes row endpoints in advance.
2. Person B: operates the seeder, following marked lines.
3. Person A: refills hopper as needed (~1/4–1/2 lb capacity per fill depending on seed size), tracks which rows are planted.
4. Roles can switch every 2–3 rows to reduce operator fatigue.

**Coverage rate:** One pass of EarthWay or Hoss seeder plants one 100-ft row in about 3 minutes. A 4,800 sq ft plot (40 × 120 ft) with 18" row spacing requires ~32 passes = ~1.5–2 hours of seeding for all caloric crops.

---

### Tool 4: Manual Jab Planter (Hand-Held, No Infrastructure)

The simplest of all tools — a hollow tube with a seed magazine and a jaw mechanism. Push the pointed end into the soil, pull the handle, and a seed is deposited at the set depth. No tractor, no assembly, no electricity. 

**How it works:** The user holds the tool upright, positions the tip at the planting point, thrusts downward into the soil (the jaw opens on contact with soil), releases the handle (jaw closes, deposits seed), and moves to the next point. Spacing is measured by the user — a knotted rope guide between two stakes makes this fast.

**Primary use in Zone 5:** Transplanting the Three Sisters mounds (corn, beans, squash — see agriculture section below), planting potatoes, or spot-planting where the push seeder is impractical (slopes, corners, between existing plants).

**Commercial jab planters:**
- [AgriExpo Manual Jab Planter directory](https://www.agriexpo.online/agricultural-manufacturer/manual-jab-planter-6074.html)
- PL1 Jab Planter: works for beans, peas, corn; available through farm supply importers; $25–$60
- DIY version: 1.5" PVC pipe, 18" long, with a spring-loaded gate at the tip (plans widely available on homesteading forums)

**Two-person workflow with jab planter:**
1. Person A: pulls knotted rope guide to mark spacing, calls out "here" at each knot
2. Person B: jabs at each called point, deposits seed
3. Switch roles every 50 plants to reduce lower-back fatigue (jabbing requires bending forward repeatedly)

---

### Tool 5: Hand-Drawn Two-Person Transplant Trailer (DIY)

For homesteads that need to move transplant trays across a large plot (1/4 acre+) without a tractor, a lightweight two-wheeled cart pulled by hand dramatically reduces fatigue.

**Design:** A garden cart with a flat bed sized to hold standard 50-cell or 72-cell seedling trays. Two handles allow two people to share the pulling load across uneven ground. Also functions as a rolling supply cart during harvest.

**DIY build from common materials:**
- Two bicycle wheels (26" or 20"): salvaged or $15–20 each from thrift stores
- Galvanized steel pipe for axle: 1" diameter, 36"–48" long; $15–25
- Plywood flat bed (3/4" exterior grade), 24" × 36": $20–30
- Steel L-brackets for axle mounts: $10–15
- Two wooden handles, 48" long: $10–15 (closet rod)
- Hardware (bolts, nuts): $8–12
- Total materials: $80–125

**Commercial option:** The Gorilla Cart GOR6PS (600 lb capacity; 47"×30" flat bed; pneumatic tires): $130–$160 at Lowe's or Home Depot. Dump-capable. Pulls easily by one adult on flat ground; two adults for slopes.

**Two-person use:** One person at each handle for slopes; one person steering (inside handle) and one side-pushing through row gaps; one person holds while the other transplants from the cart bed.

---

### Zone 5 Planting Tool Recommendations by Homestead Size

| Setup | Primary Tool | Secondary Tool | Estimated Cost |
|---|---|---|---|
| Suburban lot (<3,000 sq ft) | Hoss or EarthWay push seeder | Jab planter | $150–$215 |
| Rural, no tractor (up to 1/4 acre) | Hoss seeder + hand cart | Jab planter | $300–$400 |
| Rural, compact tractor (up to 2 acres) | 2-row 3-pt hitch planter | Water wheel transplanter | $1,400–$2,600 |
| Rural, larger operation (2+ acres) | 2-row planter + water wheel transplanter | Precision seeder | $2,000–$4,000+ |

---

## Sources and References

### Atmospheric Water Extraction
- [Atmospheric Water Generator — Wikipedia](https://en.wikipedia.org/wiki/Atmospheric_water_generator)
- [DIY Atmospheric Drinking Water Generator — Instructables](https://www.instructables.com/DIY-Atmospheric-Water-Generator/)
- [How to Make an Atmospheric Water Generator: 3 Methods — ScienceInsights](https://scienceinsights.org/how-to-make-an-atmospheric-water-generator-3-methods/)
- [How to Build a Homemade AWG — Practical Survivalist](https://practicalsurvivalist.com/diy-video-how-to-build-a-homemade-atmospheric-water-generator-produces-extracts-distilled-water-from-the-air/)
- [How to Make an Atmospheric Water Generator — Energy of Supply](https://energyofsupply.com/how-to-make-an-atmospheric-water-generator/)
- [How to Build an AWG for Home Use — Life Off-Grid](https://www.lifeoffgrid.org/atmospheric-water-generator/)
- [Atmospheric Water Generators: A Smart Solution — Quality Water Treatment](https://qualitywatertreatment.com/blogs/water-company/atmospheric-water-generators-for-water-security)
- [How Much Water Can an AWG Make? — Quality Water Treatment](https://qualitywatertreatment.com/blogs/news/how-much-water-can-an-atmospheric-water-generator-make)
- [Window-sized device taps the air for safe drinking water — MIT News, June 2025](https://news.mit.edu/2025/window-sized-device-taps-air-safe-drinking-water-0611)
- [Atmospheric Water Generation Research — US EPA](https://19january2021snapshot.epa.gov/water-research/atmospheric-water-generation-research_.html)
- [AWG for Water Security — World Economic Forum](https://www.weforum.org/stories/2024/02/atmospheric-water-generators/)
- [Solar Powered Atmospheric Water Generator Overview — IJIRSET (2018)](https://www.ijirset.com/upload/2018/january/6_IJIRSET_Paper_Solar%20Powered%20%20Atmospheric%20Water%20Generator%20-%20FINAL.pdf)

### Farm Planting Tools
- [Field Tuff 2 Row Corn and Bean Planter — YouTube](https://www.youtube.com/watch?v=bx5Em_3DK4s)
- [Smallest Two Row Corn Planter for Subcompact Tractor — YouTube](https://www.youtube.com/watch?v=uogwqEuFbo8)
- [Knapik Hydraulic Planter 2 Rows H2L](https://plantknapik.com/product/knapik-hydraulic-planter-2-rows-2/?lang=en)
- [Rainflo 1270 Water Wheel Transplanter — Berry Hill Drip](https://www.berryhilldrip.com/product/equipment/planters-and-wheels/1270-water-wheel-transplanter-rainflo/)
- [Mechanical Transplanter Company — Three Point Hitch](https://mechanicaltransplanter.com/products/three-point-hitch)
- [EarthWay 1001-B Precision Garden Seeder — Amazon](https://www.amazon.com/Earthway-1001-B-Precision-Garden-Seeder/dp/B00002N66A)
- [Hoss Garden Seeder — EasyDigging Guide](https://www.easydigging.com/seeders-planters/hoss-garden-seeder.html)
- [Manual Jab Planter Directory — AgriExpo](https://www.agriexpo.online/agricultural-manufacturer/manual-jab-planter-6074.html)
- [Walk-Behind Row Crop Planter — AgriExpo Directory](https://www.agriexpo.online/agricultural-manufacturer/walk-behind-manual-seeder-9303.html)
- [Garden Seeder Buying Guide — EasyDigging](https://www.easydigging.com/gardening/articles-g/seeders-planters/buying-guide.html)
- [Farming with Walk-Behind Tractors — Kerr Center (PDF)](https://kerrcenter.com/wp-content/uploads/edd/2018/04/Walk-behind-tractors-2018-web-version.pdf)

---

## Cross-References

- **Water storage and treatment**: See `individual/01-water.md` — AWG output pairs with cistern and rainwater collection; integrated water system diagram
- **Caloric crop planting schedule**: See `individual/02-food.md` — Zone 5 planting calendar for corn, beans, squash; garden layout; seed quantities per tool hopper fill
- **Annual activity calendar**: See `midwest/calendar.md` — planting windows, equipment maintenance schedule by month
- **Regenerative agriculture and planting systems**: See `individual/06-agriculture.md` — Three Sisters mound planting (jab planter application), cover crop seeding (push seeder application)
