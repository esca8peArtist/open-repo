# Energy — Individual Scale
> **Region**: Midwest US (Zone 5) | **Tracks**: Rural + Suburban
> **Scale**: One adult or 1–2 person household, starting from zero external power
> **Cross-references**: [individual/03-shelter.md](03-shelter.md) · [individual/01-water.md](01-water.md) · [individual/02-food.md](02-food.md) · [off-grid-living/07-heating-cooling.md](../../off-grid-living/07-heating-cooling.md)

---

## Quick Reference Card

**Zone 5 Midwest solar reality** (Chicago/Indianapolis/Des Moines baseline):

| Season | Peak sun hours/day | 100W panel output/day | Notes |
|---|---|---|---|
| Winter (Dec–Jan) | 2.5–3.5 h | 250–350 Wh | Short days, low sun angle, cloud cover. Plan for worst case. |
| Shoulder (Mar–Apr, Oct–Nov) | 3.5–5.0 h | 350–500 Wh | Variable; spring often cloudier than fall |
| Summer (Jun–Aug) | 5.5–6.5 h | 550–650 Wh | Maximum generation window; charge ahead |

**Immediate fallback — no power available right now:**
1. LED lantern (AA batteries): 40–100 hours per battery set
2. Propane camp lantern (Aladdin-style): 8–15 hours per 1-lb cylinder
3. Hand-crank flashlight or USB charger: no consumables, indefinite
4. 12V car battery + 12V LED strips: days of light from a vehicle battery

**Critical principle**: address heating and cooking through non-electric means first (propane, wood). Electrical systems are then sized for remaining loads — lighting, water pumping, and electronics — where they are irreplaceable. Attempting to heat a Zone 5 home electrically from batteries is cost-prohibitive at any residential scale.

---

## Day 1–3: Immediate Survival

### Energy Prioritization Without Power

In a sudden grid-down scenario, the single most important energy decision is **load shedding** — cutting all non-critical consumption before building any generation capacity.

**Critical loads (address immediately):**
- Lighting: 5–10 watts of LED per occupied space is sufficient
- Phone/radio charging: 10–20 watts, intermittent
- Medical equipment: CPAP, insulin refrigeration, powered wheelchair — assess your specific needs now, not during an emergency
- Water pumping: if you have a well, assess whether you have a hand pump alternative

**Deferrable loads (suspend immediately):**
- Refrigerator: in Midwest winter, move perishables to garage (32–40°F ambient) or a buried root cellar
- Electric heating: switch to propane or wood immediately — do not attempt to maintain electric heat without grid power
- Power tools, entertainment, hot water heaters

**Assessment matrix for any energy emergency:**

| Load | Why critical | Zero-power alternative |
|---|---|---|
| Lighting | Safety, work, morale | Lanterns, candles (fire risk), LED + batteries |
| Heat | Survival in Zone 5 winter | Propane heater, wood stove, layering |
| Cooking | Nutrition | Propane stove, camp stove, wood fire |
| Water pumping | Survival | Hand pump, gravity tank, bucket from source |
| Phone/communication | Situational awareness | Car charger (engine-off safe for ~5 min), hand crank |
| Refrigeration | Food preservation | Ambient cold, root cellar, smoking/curing |
| Medical equipment | Life-critical | Prioritize battery backup; plan before emergency |

### Battery-Free or Minimum-Battery Lighting

Before investing in any solar system, establish a no-power lighting baseline:

**Option A — AA/D battery lanterns**: Black Diamond Moji Lantern (200 lumens, 70 hours per 3 AAA), GoalZero Lighthouse Micro Charge (150 lumens). Store 24–48 AA batteries per person rotated annually ($8–12 worth of Energizer at Walmart). This provides 3–5 nights of full lighting with zero infrastructure.

**Option B — Propane lantern**: Coleman dual-mantle propane lantern (1,000–1,500 BTU, 700 lumens equivalent). One 1-lb cylinder gives 5–8 hours at medium setting. 12-lb cylinder supply covers 60–100 hours. Propane stores indefinitely. Cost: $30–60 heater, $1–2 per 1-lb cylinder. Note: produces CO — ventilate or use outdoors.

**Option C — 12V vehicle-to-lighting**: A single automotive battery (60–100 Ah) at 12V connected to a 10W LED strip provides 60–120 hours of good lighting before the battery reaches 50% discharge. Do not run vehicle to charge; instead, let car idle occasionally or drive — a 5-minute idle adds roughly 10–15 Ah at the alternator.

---

## Week 1–4: Stabilization — Small Solar Systems

### Understanding Solar Generation in Zone 5

The Midwest receives adequate solar radiation for off-grid use, but requires more oversizing than the Southwest due to two factors:

1. **Cloud cover**: the Great Lakes region and upper Midwest averages 50–60% cloud cover on an annual basis [1]. This compares unfavorably to the Southwest (30–40%) but is workable with proper system sizing.

2. **Seasonal swing**: Zone 5 at latitude ~41°N has a 14-hour swing in day length annually. Sunrise at 7:30 am and sunset at 4:30 pm in December (9 hours total, 2.5–3 peak sun hours) compared to 5:15 am and 8:30 pm in June (15+ hours total, 6+ peak sun hours). This 2-to-1 ratio in generation capacity is the central planning challenge. Size your system for winter, then harvest surplus in summer.

**Monthly generation estimate per 100W panel, Zone 5 (Chicago lat/long, 30° fixed tilt, south-facing)** [2]:

| Month | Peak Sun Hours | Generation per 100W panel | Generation per 400W array |
|---|---|---|---|
| January | 2.8 | 224 Wh/day | 896 Wh/day |
| February | 3.5 | 280 Wh/day | 1,120 Wh/day |
| March | 4.3 | 344 Wh/day | 1,376 Wh/day |
| April | 4.9 | 392 Wh/day | 1,568 Wh/day |
| May | 5.4 | 432 Wh/day | 1,728 Wh/day |
| June | 5.8 | 464 Wh/day | 1,856 Wh/day |
| July | 5.9 | 472 Wh/day | 1,888 Wh/day |
| August | 5.6 | 448 Wh/day | 1,792 Wh/day |
| September | 5.0 | 400 Wh/day | 1,600 Wh/day |
| October | 4.0 | 320 Wh/day | 1,280 Wh/day |
| November | 3.0 | 240 Wh/day | 960 Wh/day |
| December | 2.6 | 208 Wh/day | 832 Wh/day |

*Apply ~0.80 derating factor for real-world losses (wiring, dust, temperature, panel degradation). December actual: ~166 Wh/100W, ~665 Wh/400W array.*

### Starter System: 100W Solar + Battery + LED ($250–500)

The entry-level resilience system. Powers lighting and device charging only; no appliances.

**Components:**

```
[100W monocrystalline panel]
        |
        v
[MPPT charge controller, 10–20A]
        |
        v
[12V LiFePO4 battery, 100Ah = 1.2 kWh usable]
        |
        +---> [12V LED strips or fixtures, 10–20W]
        +---> [12V phone/USB charger]
        +---> [12V car-style outlets]
```

**What this powers (December baseline, ~166 Wh/day generation):**
- 3× 5W LED strips × 6 hours: 90 Wh
- Phone charging × 2: 20 Wh
- Small 12V radio: 10 Wh
- Total: 120 Wh — within winter generation with margin for cloudy days

**Battery sizing note**: 100Ah LiFePO4 at 12V = 1,200 Wh total. At 80% DoD (safe limit) = 960 Wh usable. At 120 Wh/day consumption: 8 days of autonomy without any solar. In practice, even overcast winter days produce 30–50 Wh, extending autonomy further.

**Cost breakdown:**

| Component | Example | Cost |
|---|---|---|
| 100W monocrystalline panel | Renogy RNG-100D or equivalent | $80–110 |
| MPPT charge controller, 20A | Renogy Rover 20A | $45–65 |
| 100Ah LiFePO4 battery | Battle Born, Ampere Time | $180–280 |
| 12V wiring, connectors, fuse | — | $25–40 |
| Mounting hardware | Ground stake or roof mount | $20–60 |
| **Total** | | **$350–555** |

### LiFePO4 vs. Lead-Acid Battery: Zone 5 Decision

**Cold weather is the decisive factor for Zone 5.**

LiFePO4 batteries must not be charged below 0°C (32°F) without active battery management protection. Charging below freezing causes lithium plating — metallic lithium deposits on the anode — which is irreversible and can trigger internal short circuits [3]. Most quality LiFePO4 batteries include a Battery Management System (BMS) that disconnects charging below 0°C. However, discharge can continue safely down to -20°C.

Lead-acid batteries (AGM, flooded) can be charged at temperatures below freezing at reduced rates, but lose 30–40% capacity at 0°C and up to 60% at -20°C [4]. They also require venting (off-gas hydrogen during charging), have 200–500 cycle life versus 2,000–4,000 for LiFePO4, and weigh 3–4× more for the same capacity.

**For Zone 5 off-grid use, LiFePO4 is the clear choice** if the battery bank is housed in a conditioned space (above 32°F when charging). If the battery must be in an unheated space (barn, uninsulated garage), either:
- Use AGM lead-acid and accept the capacity penalty
- Use heated LiFePO4 with self-heating capability (Battle Born, CANBAT, others — add $50–100/battery premium)
- Insulate the battery box and use waste heat from the inverter to maintain temperature above 32°F

**LiFePO4 vs. Lead-Acid comparison:**

| Metric | LiFePO4 | AGM Lead-Acid |
|---|---|---|
| Cycle life (to 80% capacity) | 2,000–4,000 | 300–500 |
| Usable DoD | 80–100% | 50% |
| Weight per kWh | ~14 kg/kWh | ~60 kg/kWh |
| Cold weather charge limit | 0°C (BMS cutoff) | -20°C at 0.1C |
| Cold weather capacity at -10°C | ~70–80% | ~50–60% |
| Cost per usable kWh | $450–600 | $200–300 |
| 10-year total cost | Lower (fewer replacements) | Higher |
| Thermal runaway risk | Very low | Low |

### System Voltage: 12V, 24V, or 48V?

System voltage selection determines the entire system's wiring and component choices. The rule of thumb [5]:

- **12V**: under 500 Wh/day consumption. Simple wiring, cheap components, direct compatibility with automotive accessories.
- **24V**: 500–2,000 Wh/day. Better for longer wire runs; components slightly more expensive but more efficient.
- **48V**: over 2,000 Wh/day (moderate household loads). Required for most residential inverter systems (Victron, Schneider, SMA). Higher voltage = lower current = smaller wires = less heat loss.

A 1–2 person minimal household typically falls in the 300–800 Wh/day range, making 12V or 24V appropriate for lighting-and-charging systems and 48V necessary if adding refrigeration or well pump support.

### Hand-Crank Generators as Backup

Hand-crank generators produce electricity mechanically, requiring no fuel or sunlight. They are a useful backup for emergency phone charging and radio use, but are not practical for sustained household loads.

**Realistic output**: a human can sustain roughly 75–100W of mechanical output for short periods [6]. Generator efficiency converts this to 50–70W of electrical output. Generating 100 Wh (to charge a phone 6–8 times) requires 1.5–2 hours of continuous cranking.

**Practical options:**
- K-TOR Power Box 50W hand crank generator: $150. Produces 120VAC or 12VDC. Suitable for phone charging and small electronics.
- Eton FRX5-BT hand crank radio/lantern/charger: $60. Low-output but includes NOAA weather radio — high value as an emergency communication device.
- For mechanical work (pumps, grinders): treadle or bicycle pedal generators. A bicycle generator can sustain 80–150W output. Plans and kits available from Pedal Power Projects and similar sources.

---

## Month 1–6: Building Systems

### Sizing a Household Energy Budget

Before specifying any generation system, catalog your actual loads. This "demand-first" approach consistently produces better outcomes than guessing at system size.

**Typical 1–2 person household loads in Zone 5:**

| Load | Watts | Hours/day (winter) | Hours/day (summer) | Wh/day winter | Wh/day summer |
|---|---|---|---|---|---|
| LED lighting (4 zones) | 5W each | 8 | 4 | 160 | 80 |
| Phone charging × 2 | 10W each | 2 | 2 | 40 | 40 |
| NOAA weather radio | 3W | 6 | 6 | 18 | 18 |
| Laptop/tablet | 30–60W | 2 | 2 | 80 | 80 |
| Chest freezer (efficient) | 30W avg | 24 | 24 | 720 | 720 |
| Well pump (1/2 HP, 375W) | 375W | 0.5 | 0.5 | 188 | 188 |
| CPAP (medical, if needed) | 30–50W | 8 | 8 | 320 | 320 |
| Small power tools (occasional) | 300–800W | 0.5 | 1 | 300 | 600 |

**Key insight**: refrigeration/freezer is the largest consistent load for most households (720 Wh/day = ~22 kWh/month). Replacing it with a propane refrigerator or propane/electric hybrid refrigerator eliminates the single largest battery drain.

**Practical load categories:**

- **Minimal survival system** (no refrigeration, no well pump, no power tools): ~300–500 Wh/day in winter
- **Basic comfort** (refrigeration + pump + basics): ~1,200–1,500 Wh/day year-round
- **Moderate household** (above + power tools, occasional AC): ~3,000–5,000 Wh/day summer

### Designing a 1–3 kWh/day System (Basic Comfort)

**System architecture:**

```
[4× 100W panels in series-parallel = 400W array, 24V nominal]
                    |
              [MPPT controller, 40A, 24V]
                    |
        [4× 100Ah LiFePO4 at 24V = ~9.6 kWh bank]
                    |
         [Pure sine wave inverter, 1,000–2,000W, 24V]
                    |
        [AC distribution panel, 4–6 circuits]
              /          \
    [120VAC outlets]   [12V/USB direct]
```

**Target loads**: lighting (200 Wh), refrigeration (720 Wh), phone/laptop (140 Wh), pump (188 Wh/day). Total: ~1,250 Wh/day.

**Winter generation check**: 400W array × 2.6 peak sun hours × 0.80 derate = 832 Wh/day actual December. This falls short of the 1,250 Wh/day load — a 418 Wh/day shortfall in worst-case months. Solutions:

1. Tilt panels steeper in winter (from 30° to 50–60°) to capture lower sun angle: adds 15–25% winter output [7]
2. Reduce refrigeration load: use outdoor ambient cold for food storage in winter (below 40°F in Midwest from November–March), removing 720 Wh/day from the load
3. Add a 6th panel (100W) to array
4. Accept battery discharge over multi-day cloudy periods; rely on 3–5 day autonomy buffer

**Battery bank autonomy**: 9.6 kWh × 80% usable = 7.68 kWh. At 1,250 Wh/day draw: 6.1 days autonomy without solar. Chicago averages 4.2 consecutive overcast days in winter [1]; this bank provides adequate buffer.

### Battery Management Systems (BMS) and Monitoring

Every lithium battery bank requires a BMS. For DIY banks built from cells, an external BMS is mandatory. For commercial LiFePO4 batteries (Battle Born, Ampere Time, EG4, etc.), the BMS is integrated.

**BMS functions** [8]:
- Overcharge protection: disconnects when cell voltage exceeds 3.65V
- Over-discharge protection: disconnects when cell voltage falls below 2.5V
- Over-temperature: disconnects charging above 45°C and below 0°C
- Cell balancing: equalizes charge across cells to prevent divergence
- Short circuit protection: overcurrent disconnect in milliseconds

**Monitoring hardware**: For systems above 1 kWh, install a battery monitor (Victron BMV-712, $120–160) that displays state of charge, daily consumed energy, and remaining time-to-empty. This prevents the most common off-grid failure: running batteries flat without realizing it.

**Balancing requirement**: LiFePO4 cells in series must be balanced. A 24V bank (8 cells in series) that develops 0.1V imbalance will have one cell chronically over- or under-charged, shortening that cell's life to 500–800 cycles. Use a BMS with active or passive balancing. For large DIY banks, a top-balancing procedure before initial use (charging all cells to 3.65V individually before series connection) establishes a strong starting baseline [9].

### Inverters: Sizing and Selection

Inverters convert DC battery power to 120VAC for standard AC loads.

**Pure sine wave vs. modified sine wave** [10]:
- Pure sine wave produces a smooth sinusoidal AC output nearly identical to grid power. Required for: CPAP machines, variable-speed motors (well pumps), medical equipment, modern laptops, LED dimmers.
- Modified sine wave produces a stepped approximation. Works for: incandescent lights, simple resistive loads (toasters, heat elements), older power tools. Damages or shortens life of: variable-speed motors, audio equipment, transformers, most electronics.

**Recommendation**: always use pure sine wave. The cost premium ($50–150) is irrelevant at the system scale where the inverter matters.

**Sizing inverters:**

| System Level | Recommended Inverter | Peak Load Coverage | Example Models |
|---|---|---|---|
| Minimal (lighting/charging) | 400–600W pure sine | LED lights, phone/laptop, small radio | Victron Phoenix 12/500, Renogy 500W |
| Basic household | 1,000–2,000W | Above + well pump (but not simultaneously with other loads) | Renogy 2000W, Victron Multiplus 24/1200 |
| Full household | 3,000–5,000W | All loads simultaneously; well pump + refrigerator + tools | Victron Multiplus-II 48/3000, Schneider XW+ |

**Heat management**: inverters generate heat proportional to inefficiency. A 2,000W inverter at 92% efficiency rejects 160W of heat. In a sealed insulated space, this can cause overheating. Mount in a ventilated location, never enclosed in a sealed box.

**Standby loss**: inverters draw 10–30W continuously even at zero load. A 20W standby draw costs 480 Wh/day — 40% of a minimal system's entire winter generation budget. Use a switched outlet or smart relay to cut the inverter when not needed.

### MPPT vs. PWM Charge Controllers

**PWM (Pulse Width Modulation)**: simpler, cheaper ($20–60), less efficient. Works by directly connecting the panel to the battery and pulse-switching; panel voltage must match battery voltage. Only appropriate for 12V systems with 12V nominal panels. Wastes 20–30% of potential generation.

**MPPT (Maximum Power Point Tracking)**: extracts maximum power from the panel by continuously adjusting the operating point. Converts higher panel voltage down to battery voltage with 93–97% efficiency. Particularly valuable in cold weather and partial shading where panel voltage peaks [11]. Cost: $50–200. Required for any 24V or 48V system.

**Rule**: use MPPT always for systems over 100W or any 24V/48V system.

---

## Month 3–12: Intermediate Systems

### Wind Energy in Zone 5

The Midwest has substantial wind resources — Iowa, Illinois, and Indiana have some of the highest wind capacity factors in the continental US [12]. However, small residential wind is a different calculation than utility-scale wind.

**Zone 5 wind resource for small turbines:**
- Ground-level wind (10m height) in flat Midwest averages 5–7 m/s in open areas, 3–5 m/s in suburban/wooded areas [13]
- Hilltops and ridge lines: 7–10 m/s
- Minimum economical wind speed for small turbines: 5 m/s annual average
- Wind power scales as the cube of wind speed: doubling wind speed = 8× the power

**Small wind turbine options:**

| Turbine | Type | Rated Power | Rated Wind Speed | Estimated Annual Output (5 m/s avg) | Cost |
|---|---|---|---|---|---|
| Bergey Excel 1 | HAWT | 1 kW | 11 m/s | 800–1,200 kWh/year | $5,000–8,000 + tower |
| Primus Wind Power AIR 40 | HAWT | 160W | 12.5 m/s | 150–250 kWh/year | $700–900 |
| Tesup Atlas 1kW VAWT | VAWT | 1 kW | — | 600–900 kWh/year | $2,500–4,000 |
| DIY savonius/VAWT | VAWT | 200–500W | — | 100–400 kWh/year | $200–800 materials |

**HAWT vs. VAWT for Zone 5:**
- Horizontal-axis turbines (HAWT, propeller type) are more efficient (Cp up to 0.45) and better suited to consistent wind directions.
- Vertical-axis turbines (VAWT, Savonius/Darrieus types) accept wind from any direction, perform better in turbulent urban/suburban airflows, but typically have lower efficiency (Cp 0.15–0.30) and require more maintenance.

**Honest assessment for Zone 5 residences:**
Small wind is most cost-effective on rural properties with open exposure and confirmed wind resources. In suburban environments with trees, buildings, and turbulent low-level airflow, small wind rarely achieves payback under 15 years [14]. For most Zone 5 households, additional solar panels deliver better value than small wind turbines.

If you have a hilltop rural property with clear exposure: commission a wind resource assessment (affordable anemometer loggers run $200–500; log for 6–12 months before purchasing turbines). The DOE WINDExchange site provides free county-level wind resource maps as a preliminary screening tool [13].

### Micro-Hydro: The Best Off-Grid Source (If Available)

Micro-hydro is the highest-value small-scale generation technology when site conditions permit: it produces power 24 hours/day regardless of weather, requires minimal land, and produces consistent output that dramatically simplifies battery sizing.

**Requirements:**
- A flowing water source (year-round stream, spring)
- A measurable head (vertical elevation drop from intake to turbine): minimum 2m (6 ft) useful; 5–30m (15–100 ft) optimal
- Adequate flow: minimum 1–2 gallons per minute (GPM) at low head; 0.1–0.5 GPM at high head

**Power output formula:**
```
Power (W) = Head (m) × Flow (L/s) × 9.81 × Turbine efficiency (0.65–0.85)
```

Example: 10m head, 0.5 L/s (8 GPM) flow, 75% efficiency: 10 × 0.5 × 9.81 × 0.75 = **36.8W continuous** = 883 Wh/day — equivalent to a 400W solar array in winter Midwest.

**Turbine types:**
- **Pelton wheel**: high head (10m+), low flow. Most common for rural streams. Jet of water strikes cup-shaped buckets on a wheel. Described in detail in Thake's *Micro-hydro Pelton Turbine Manual* [15]. DIY construction possible with basic metalworking skills.
- **Turgo turbine**: medium head (2–20m), higher flow. Jet strikes blades at an angle. Slightly less efficient than Pelton but handles higher flow rates.
- **Propeller turbine**: very low head (1–5m), very high flow. Runs partially submerged. Appropriate for run-of-river applications.

**Commercial options:**
- PowerSpout LH (low head), EL (extra-low head), PLT (Pelton): $700–2,500 depending on head/flow combination [16]
- Harris Hydroelectric: custom turbines $1,500–5,000 + engineering [17]

**Midwest seasonal availability:**
- Spring (March–May): highest flow from snowmelt and rain — best production period
- Summer (June–August): variable; many Midwest streams drop 40–70% in August drought [18]
- Fall (September–October): recovering flow post-summer
- Winter (November–February): ice can block intakes; screen protection and slight submersion of intake pipe mitigates ice bridging

**Site assessment before purchase**: measure flow (bucket-and-timer method) and head (surveyor's rod or GPS elevation) at your lowest expected flow (late August). Design to that minimum; summer surplus powers charging.

### Propane as the Essential Complementary System

Propane is not a backup to solar — it is a co-equal energy vector that makes a solar-battery system economically viable in Zone 5. The hybrid propane + solar approach consistently outperforms all-electric off-grid at equivalent cost.

**Why propane is irreplaceable in Zone 5:**
- Heating demand peaks in winter precisely when solar generation is at its minimum. Attempting to cover heating with batteries would require a battery bank 10–20× larger than one sized for lighting and appliances alone.
- Propane stores indefinitely without degradation (unlike gasoline: 6–12 months; diesel: 12–24 months treated).
- Propane appliances (stoves, heaters, refrigerators, water heaters) are simpler and more reliable than electric equivalents at off-grid power levels.

**Propane applications:**
- **Cooking**: standard propane range/oven. 1 lb of propane ≈ 22,000 BTU. A family cooking 3 meals/day uses 1–2 lbs/day = 365–730 lbs/year ≈ 1.5–3 standard propane exchanges or 85–175 gallons in bulk.
- **Space heating**: Mr. Heater Big Buddy (18,000 BTU/hr) on 20-lb tank: 50–120 hours. Whole-house propane furnace or boiler: most efficient, safest, most comfortable option.
- **Water heating**: tankless propane (e.g., Eccotemp L5 or Rinnai): 80,000–180,000 BTU/hr, heats water on demand without electricity.
- **Refrigeration**: propane refrigerators (Consul, Unique) run entirely off propane flame, drawing zero electricity. A full-size unit uses 1–1.5 lbs/day (0.5–0.75 gallons). This eliminates the single largest electrical load.
- **Lighting**: Aladdin-style kerosene/propane mantle lanterns (7,000–10,000 BTU, 60–70 watt equivalent): excellent emergency and supplemental lighting.

**Propane storage options and regulations:**

| Tank Size | Gallons | Setback from buildings | Typical use |
|---|---|---|---|
| 20-lb cylinder (standard BBQ) | 4.7 gallons | None required | Portable, emergency |
| 100-lb cylinder | 24 gallons | 3 ft from openings | Small appliances, seasonal heating |
| 120 gallon above-ground | 120 gallons | 10 ft from building | Small home, primary cooking + hot water |
| 500 gallon above-ground | 500 gallons | 10 ft from building, 10 ft from property line | Full home heating + all appliances |
| 1,000 gallon above-ground | 1,000 gallons | 25 ft from building | Whole-farm or large home |

Setback requirements per NFPA 58 (2017 edition) [19]. Tanks between 125 and 500 gallons require 10 ft separation from buildings and buildable property lines. Local AHJ (Authority Having Jurisdiction) may have stricter requirements; verify before installation.

**Propane economics (2025 Midwest pricing, approximate):**
- Bulk residential delivery: $2.00–3.50/gallon depending on region and winter demand
- Cylinder exchange (20 lb): $4–5/gallon equivalent — expensive for large volumes
- 500-gallon tank filled at $2.50/gallon = $1,250 total; 1 year of heating for a well-insulated 1,200 sq ft home
- Compare to all-electric off-grid heating: same home would need ~30 kWh/day in January; at $0.50/kWh battery amortized cost = $15/day = $4,500 for January alone

**Redundancy principle**: with propane + solar-battery, failure of either system does not cause total loss. Solar fails (equipment fault, extended overcast): propane handles heating, cooking, and lighting. Propane delivery fails (shortage, supply disruption): solar handles lighting and small loads; wood stove handles heating. This two-vector approach is the practical foundation of energy resilience.

---

## Year 1+: Long-Term and Complex Systems

### Larger Battery Banks: 5–15 kWh

For a household targeting full comfort (refrigeration, well pump, lighting, occasional power tools), a 5–15 kWh LiFePO4 bank is the target.

**Bank sizing formula:**
```
Battery bank (kWh) = Daily consumption (kWh) × Days of autonomy ÷ Usable DoD (0.80)
```

Example: 2 kWh/day load, 5 days autonomy, 80% DoD: 2 × 5 ÷ 0.80 = **12.5 kWh bank**

At $450–600/kWh: $5,625–7,500 for the battery bank alone.

**Physical requirements for a 15 kWh, 48V LiFePO4 bank:**
- 16 cells × 3.2V × 300Ah = 15.36 kWh nominal (DIY prismatic cells approach)
- Dimensions: roughly 24"×18"×24" for a rack-mounted bank
- Weight: ~200 kg (440 lbs) — floor loading consideration; a standard wood-frame floor (40 psf capacity) can handle this if distributed over 6+ sq ft with plywood spreading
- Temperature: maintain above 32°F for charging; a heated utility closet or basement is ideal

**Commercial integrated systems (2025)**:
- EG4 48V 100Ah wall-mount: $1,100–1,400/unit (4.8 kWh usable); three units = $3,300–4,200 for 12 kWh [5]
- Victron 25.6V 200Ah Smart: $1,800/unit
- Tesla Powerwall 3: 13.5 kWh, $11,000–13,000 installed (includes integrated inverter)

### Grid-Tie Solar with Battery Backup

If grid power is available and the goal is resilience rather than full independence, a grid-tied system with battery backup is the most economical path.

**System architecture:**
- 5–10 kW solar array (20–40× 300W panels): covers annual household electrical consumption with surplus
- Hybrid inverter (Victron Multiplus-II, SolarEdge StorEdge, Enphase IQ): operates both grid-connected and island mode
- Battery bank (5–15 kWh): provides backup during outages; charges from solar or grid during off-peak
- Grid interconnection: required per IEEE 1547-2018 [20]; state-level implementation varies

**Grid interconnection requirements in Zone 5 Midwest states:**
All five major Zone 5 Midwest states (Illinois, Indiana, Iowa, Ohio, Wisconsin) have adopted IEEE 1547-2018 in whole or part. The standard requires:
- Anti-islanding protection (inverter shuts down when grid fails, to protect line workers)
- Voltage and frequency ride-through capability
- Power quality compliance (THD < 5%, DC injection < 0.5% rated output)
- Utility interconnection agreement and inspection (typically $100–500 application fee + utility inspection)

**Midwest-specific snow management for rooftop solar [21]:**
- Zone 5 ground snow load: 25–40 psf in most areas; roof design load typically 20–35 psf
- Solar panels must have structural loading equal to or exceeding the roof design snow load
- Panel angle: at 30° tilt, wet snow adheres; at 40°+ tilt, snow sheds after one sunny day [21]
- Winter optimization: adjust fixed-tilt ground mounts to 50–55° for December–February; this improves winter output by 15–25% compared to summer-optimized 30° tilt [7]
- Snow on panels is NOT a system emergency — most snow melts or slides within 1–3 sunny days. Do not climb on icy roof panels; use a roof rake from the ground if needed.

**Cost (2025):**
- 10 kW installed (panels + racking + inverter + permits): $25,000–35,000 before incentives
- Federal ITC (Investment Tax Credit): 30% through 2032
- Net after ITC: $17,500–24,500
- With 15 kWh battery backup: add $8,000–12,000
- Payback period Zone 5 Midwest: 8–12 years at current utility rates

### Off-Grid Complete System: Solar + Battery + Generator Backup

For properties without grid access or choosing full independence:

**System design:**

```
[3–5 kW solar array, ground mount, adjustable tilt]
                    |
           [MPPT charge controller, 60–100A, 48V]
                    |
         [15 kWh LiFePO4 bank, 48V, heated enclosure]
                    |
         [5,000W pure sine wave inverter/charger]
                  / | \
      [AC panel] [DC loads] [Generator input]
                    |
        [5–8 kW diesel or propane generator]
          [fuel: 50–100 gal diesel storage]
```

**Generator sizing rule**: the generator must be able to charge the battery bank at a reasonable rate while simultaneously supplying household loads. A 48V, 15 kWh bank drawn to 30% SOC (emergency) needs to recharge 10.5 kWh. At 3,000W charging (practical maximum for a Victron 3kVA inverter/charger): 3.5 hours of generator run time. A 5 kW generator handles this while running lights and refrigerator simultaneously.

**Diesel fuel storage:**
- 5-gallon containers: $30–50 each. Suitable for short-term, but unstable beyond 6–12 months without stabilizer.
- Treated diesel (Pri-D or equivalent fuel stabilizer): extends storage to 24–36 months.
- 50-gallon above-ground tank: optimal for homestead use; rotate fuel annually.
- OSHA limits residential above-ground flammable liquid storage: 25 gallons without special provisions; 60 gallons in approved safety containers [22]. Consult local AHJ for buried tank regulations.

**Generator maintenance schedule:**
- Monthly: run under load for 30 minutes (prevents varnish in carburetor, exercises starter)
- Every 50 hours: oil change (SAE 30 or 10W-30 per manufacturer)
- Annual: air filter, spark plug (gasoline), fuel filter inspection
- Every 2 years: coolant change (diesel liquid-cooled); carburetor cleaning (gasoline)

### Biogas from Manure (Rural, Livestock Required)

If the property has livestock, a biogas digester can produce methane for cooking gas from manure that would otherwise go to waste.

**Production yields:**
- Dairy cattle: approximately 3.85 cubic feet of methane per pound of volatile solids [23]
- One dairy cow produces ~140 lbs/day manure; at 8% volatile solids: 11.2 lbs VS/day × 3.85 = 43 cu ft CH₄/day
- Biogas composition: ~60% methane, 40% CO₂; energy content ~600 BTU/cubic foot [23]
- 43 cu ft CH₄/day × 600 BTU = 25,800 BTU/day — adequate for cooking and some space heating

**Temperature dependence:**
Methane-producing bacteria (methanogens) operate best at 35°C (95°F) and are severely inhibited below 15°C [24]. In Zone 5, outdoor digesters cease production November–March without heating. Options:
- Insulate the digester tank; use solar thermal or waste heat to maintain 30–35°C
- Build digester inside a greenhouse or heated outbuilding
- Accept seasonal production (spring–fall) and supplement with propane in winter

**DIY digester design:**
- Batch digester (simplest): sealed 200–500 gallon tank; load manure + water (8–10% total solids); maintain temperature; gas collected from top. Cycle time: 30–60 days at 35°C.
- Continuous-flow digester: daily input of fresh manure; gas collected continuously. More complex plumbing but steady output.
- Resources: Penn State Extension biogas guides [23]; Mother Earth News DIY digester plans [25]; University of Missouri Extension G1881 [26]

**Safety requirements:**
- Methane is flammable from 5–15% concentration in air; lighter than air, so it rises and dissipates outdoors
- Always install pressure relief valve on digester tank (set at 0.5–1 PSI)
- Never enter a confined digester space — CO₂ accumulates at bottom; oxygen-deficient atmospheres are lethal
- CO and CO₂ detectors required near any biogas combustion appliance

### Vehicle-to-Home (V2H) as Battery Backup

Bidirectional-capable electric vehicles can serve as mobile battery banks, powering household loads during grid outages.

**Available V2H systems (2025):**
- **Ford F-150 Lightning + Ford Intelligent Backup Power**: 98 kWh usable pack; 9.6 kW export rate (80A, 240V); powers average home 3–10 days. Requires Ford 80A home charger with automatic transfer switch ($5,000–7,500 installed) [27]. The largest and most capable residential V2H system currently available.
- **Hyundai Ioniq 9 / Kia EV9**: V2H capable with compatible EVSE; 110 kWh pack; 3.6–11 kW bidirectional output. Systems being deployed 2025 [28].
- **Nissan Leaf (2024+)**: V2X capable in principle; no residential-scale CHAdeMO V2H inverter commercially available in the US as of 2025 [29].

**Honest limitations for off-grid use:**
- V2H systems require a connection to the utility grid for some system functions; true off-grid (islanding without any grid connection) is not supported by most current implementations
- EV range is consumed while powering the home; the vehicle becomes temporarily non-mobile
- Cold weather reduces EV battery capacity (Zone 5 winter: expect 20–30% capacity reduction)
- V2H is best positioned as a grid-outage backup for grid-connected homes, not as a standalone off-grid power source

---

## Heating Integration: The Dominant Energy Problem

Heating is the single largest energy demand in Zone 5 Midwest. Chicago accumulates 6,493 heating degree days annually [30]; Milwaukee reaches 7,635. Getting heating right before sizing electrical systems is the correct order of operations.

### Passive Solar (Free Energy, Requires Design)

Passive solar reduces heating demand by 20–40% in well-designed homes without any mechanical system [31]. The principles:

- **South-facing glazing**: 7–12% of floor area in south-facing glass (at 41°N latitude). Too much glass without thermal mass creates overheating in shoulder seasons.
- **Thermal mass**: materials that absorb heat during the day and release it at night. Concrete, brick, tile, or water-filled containers placed in direct winter sun. Rule of thumb: 3–4 sq ft of 4" concrete slab per 1 sq ft of south glass [31].
- **Proper overhangs**: at 41°N, summer sun is 64° above horizon at noon; winter sun is 18°. An overhang of projection = 0.32 × window height blocks summer sun while admitting winter sun (from shelter.md cross-reference).
- **Superinsulation**: Zone 5 targets — attic R-49 to R-60, walls R-21 minimum, slab/foundation R-10 perimeter. Every R-value point added directly reduces heating demand proportionally.

### Wood Stove (Primary Backup Heat)

A wood stove with EPA Phase 2 certification (or the current "Step 2" standard effective May 2020) is the single most resilient heating system for Zone 5 because it operates with zero electrical input and uses locally-sourced, storable fuel.

**Current EPA standards:** EPA certified wood stoves must emit no more than 2.0 g/hr particulate matter (Step 2, post-2020) [32]. Efficiency: most EPA-certified stoves test at 70–83% efficiency [33].

**Heat output and firewood requirements:**

| Home size | Stove output needed | Firewood/year (Zone 5) |
|---|---|---|
| 800 sq ft, well insulated | 20,000–30,000 BTU/hr | 1.5–2 cords |
| 1,200 sq ft, average insulation | 30,000–45,000 BTU/hr | 2–3 cords |
| 1,800 sq ft, average insulation | 45,000–60,000 BTU/hr | 3–4 cords |

**Species BTU content (per cord)** [34]:
- Hickory: 28 million BTU — highest density in Midwest; burns hot and long
- White/Red Oak: 24–26 million BTU — excellent; widely available
- Ash: 23 million BTU — burns even when slightly green; splits easily
- Hard maple: 22 million BTU
- Black locust: 27 million BTU — underutilized; invasive in parts of Midwest, free for harvest
- Cottonwood/poplar: 14–16 million BTU — low value; poor choice for sole heat source

**Splitting and seasoning**: freshly cut hardwood runs 40–50% moisture content. Burning wet wood produces creosote (chimney fire risk) and dramatically reduces heat output. Target 20% moisture or below (measure with $15 wood moisture meter). Time to dry: 6 months for split wood in dry, breezy outdoor stack; 12–18 months for unprocessed rounds.

**Chimney and maintenance**: annual chimney inspection and cleaning required. Creosote buildup >1/8" is a fire risk. A certified chimney sweep runs $150–250/year — worthwhile.

### Rocket Mass Heater (High Efficiency, Code Challenges)

Rocket mass heaters (RMH) achieve combustion temperatures of 1,100–1,200°C in the insulated burn tunnel, achieving stated efficiencies of 80–92% compared to 70–83% for conventional wood stoves [35]. The thermal mass (cob bench, masonry bench) stores heat and releases it over 12–24 hours, creating radiant comfort from smaller amounts of fuel.

**Practical notes:**
- A well-built RMH can heat the same Zone 5 home with 50–90% less wood than a conventional stove [35]
- Building codes: RMHs lack standardized testing and ICC/UL listing; most local building departments cannot permit them under standard categories. Rural areas without code enforcement are the practical setting [35]
- Insurance: many homeowners insurance policies exclude DIY site-built masonry heaters; consult your insurer before building
- Resources: Ianto Evans and Leslie Jackson, *Rocket Mass Heaters* (Cob Cottage Co., 2014); Paul Wheaton's "better wood heat" resources [36]

### Air-Source Heat Pump (High Efficiency, High Power Requirement)

Modern cold-climate heat pumps achieve COP (coefficient of performance) of 2–3 at 30°F and maintain COP greater than 1.75 at 5°F [37]. Below -10°C (14°F), performance degrades but does not cease entirely; DOE research has achieved COP > 1.0 down to -35°F [38].

**Zone 5 practical reality:**
- A cold-climate ASHP is 2–3× more efficient than electric resistance heating at Zone 5 temperatures
- A 12,000 BTU/hr (1-ton) heat pump draws ~1,200W at 30°F (COP = 2.8) — approximately 29 kWh/day for continuous heating of an 800 sq ft space
- This is 3–5× the daily output of a realistic off-grid solar array
- **Heat pumps are not viable as primary heat for off-grid solar systems** at typical residential battery capacities. They become viable only when paired with a large grid-tied system or when grid power is available.
- For grid-tied resilience (grid outage backup): a 5 kW ASHP + 15 kWh battery can heat a well-insulated home for 6–8 hours per battery charge cycle — useful for short outages, not extended ones.

**Ground-source heat pump (GSHP/geothermal):**
- More efficient than ASHP (COP 3–5 year-round due to stable 50–55°F ground temperature)
- Requires excavation or well drilling for ground loops: $8,000–20,000 for loop field alone
- Total installed cost: $18,000–40,000 [39]
- 30% federal tax credit through 2032
- After ITC: $12,600–28,000 — best suited for new construction where loop field is included in initial excavation

---

## Seasonal Planning and Energy Budgets

### Seasonal Energy Profiles

**Summer (June–August) — High generation, low heat demand:**
- Solar generation: 5.5–6.5 peak sun hours/day
- Priority: maximize battery charging; top off any lead-acid banks; do power-intensive work
- High-power tasks to complete in summer: well drilling, wood cutting (chainsaw), post-hole digging, wood processing (splitter), pressure washing
- Storage building: fill propane tanks before fall price increases (propane is typically $0.30–0.50/gallon cheaper in summer vs. winter peak)
- Thermal buffer: use summer surplus to heat a large water storage tank (if radiant heat system present)

**Shoulder seasons (April–May, September–October) — Variable:**
- March–April: often the cloudiest months in the Midwest — solar output can be 15–25% below the monthly average due to storm fronts [1]
- September–October: best shoulder months; clear skies, moderate temperatures
- Priority: split and stack firewood (split in spring, stack for fall drying); pre-charge batteries before winter; inspect and service all systems

**Winter (November–March) — Low generation, high heat demand:**
- Solar generation: 2.5–3.5 peak sun hours/day
- System design must be validated against December–January minimums
- Reduce non-critical loads: suspend power tool use, reduce lighting hours with solar-optimized schedule (bright hours = work hours)
- Heating priority: wood stove and propane carry the load; electrical heating is prohibitively expensive at battery capacity
- Panel management: tilt to 50–55° for winter; check for snow accumulation after storms

**Monthly energy budget table (400W solar array, 5 kWh battery, Zone 5):**

| Month | Solar generation/day | Load (moderate, 1.5 kWh/day) | Net | Notes |
|---|---|---|---|---|
| December | 0.67 kWh | 1.5 kWh | -0.83 kWh | Battery draining; generator or propane supplements |
| January | 0.72 kWh | 1.5 kWh | -0.78 kWh | Worst month |
| February | 0.90 kWh | 1.4 kWh | -0.50 kWh | Slightly better |
| March | 1.10 kWh | 1.2 kWh | -0.10 kWh | Near-balance |
| April | 1.25 kWh | 1.0 kWh | +0.25 kWh | Charging begins |
| May–August | 1.4–1.5 kWh | 0.9–1.0 kWh | +0.4–0.6 kWh | Surplus; high generation |
| September | 1.28 kWh | 1.0 kWh | +0.28 kWh | Good |
| October | 1.02 kWh | 1.1 kWh | -0.08 kWh | Near-balance |
| November | 0.77 kWh | 1.3 kWh | -0.53 kWh | Battery draining begins |

*Generation values use December 2.6 PSH, etc. from Table 1 × 400W × 0.80 derate. Winter load elevated for longer lighting hours.*

**Implication**: a 400W array + 5 kWh battery runs a deficit from November through March. A generator or propane generator supplement is necessary for those 5 months unless array is oversized. Adding a 6th panel (100W, $80–100) reduces but does not eliminate the winter deficit.

---

## Monitoring and Maintenance

### Battery Monitoring

**State of charge (SOC) by voltage (LiFePO4, 12V system)** [8]:

| SOC | Resting Voltage (12V) | Action |
|---|---|---|
| 100% | 13.4V | Fully charged |
| 80% | 13.1V | Normal operating range |
| 50% | 13.0V | Watch consumption rate |
| 20% | 12.8V | Reduce loads; recharge soon |
| 10% | 12.5V | Critical — BMS may disconnect |
| 0% | 12.0V | BMS cutoff; do not discharge further |

*Note: LiFePO4 has a very flat discharge curve; voltage is a poor SOC indicator until the final 10–20%. Use a Coulomb-counting battery monitor (Victron BMV, Renogy RVR) for accurate SOC.*

**Monitoring checklist (monthly):**
- [ ] Check all cell voltages if DIY bank (should be within 0.05V at full charge)
- [ ] Inspect terminals for corrosion (copper sulfate, white powder): clean with baking soda + water, dry thoroughly
- [ ] Log cycle count (from BMS display)
- [ ] Test charge controller output voltage (should match battery absorption voltage, typically 14.4–14.6V for 12V LiFePO4)
- [ ] Verify inverter standby draw with clamp meter

### Solar Panel Maintenance

- **Cleaning**: dust and pollen reduce output 5–15%; rinse with water and soft brush. Zone 5: cottonwood season (May–June) leaves significant fuzz on panels; clean after.
- **Snow**: allow natural clearing unless panels are at low tilt (< 20°). Telescoping roof rake from ground (keep metal parts away from panels). Never use rock salt — damages encapsulant.
- **Annual output check**: record kWh production from charge controller logs each month. If year-over-year production drops >10–15%, investigate (shading from new tree growth, soiling, delamination, cracked cells).
- **Panel snow load**: rated at 40 psf for most commercial panels; Zone 5 roof design snow load 20–35 psf. Structural panels are not the limiting factor; roof structure under the mount is [21].

### Generator Servicing

- Run at least 30 minutes under 50–75% load monthly (prevents stale fuel in carburetor)
- Oil change: every 50 hours or annually, whichever comes first
- Fuel: rotate stored diesel every 12–18 months (add Pri-D stabilizer for longer storage); drain gasoline generators completely if storing over 30 days

### Kill-a-Watt Load Assessment

Before building any solar system, audit actual loads with a Kill-a-Watt P4400 ($20–30 at hardware stores). Plug every appliance in individually, run for 24 hours, and record actual energy consumption. Real-world results often differ significantly from nameplate ratings:

- "300W" laptop charger: actual draw 45–80W
- "Energy Star" refrigerator: actual consumption varies 0.3–2.0 kWh/day depending on age, seal condition, and ambient temperature
- Well pump: nameplate 1,000W; actual starting surge 2,500–3,000W (inverter must handle this peak)

Clamp meters ($30–100, e.g., Klein CL120) measure current on 240V loads (well pump motor, electric water heater, HVAC) without interrupting service.

---

## Cost and Configuration Examples

### Configuration 1: Minimal Survival ($350–555)

**Goal**: lighting and phone charging, 2–3 cloudy days autonomy. No refrigeration, no well pump support.

| Component | Cost |
|---|---|
| 100W monocrystalline panel | $85–110 |
| 20A MPPT charge controller | $45–65 |
| 100Ah 12V LiFePO4 battery | $180–280 |
| Wiring, fuse, connectors | $25–40 |
| Ground mount or roof mount | $20–60 |
| **Total** | **$355–555** |

Powers: 4× 5W LED fixtures (8h/night), 2 phone charges, NOAA radio. Heating/cooking: propane entirely.

---

### Configuration 2: Basic Comfort ($2,800–4,500)

**Goal**: lighting, refrigeration alternative (propane fridge), well pump (limited), device charging. 5-day autonomy.

| Component | Cost |
|---|---|
| 4× 100W panels + ground mount | $400–600 |
| 40A MPPT charge controller (24V) | $120–180 |
| 4× 100Ah LiFePO4 at 24V (9.6 kWh bank) | $1,200–1,800 |
| 1,500W pure sine wave inverter/charger (24V) | $300–500 |
| Wiring, breakers, fusing | $150–250 |
| Battery monitor | $120–160 |
| Propane refrigerator (Unique or Consul) | $1,200–2,000 |
| **Total** | **$3,490–5,490** |

Powers: full lighting, refrigeration (propane), well pump (30 min/day), device charging, laptop. No AC, no electric heat.

---

### Configuration 3: High Resilience ($14,000–22,000)

**Goal**: full household operation (minus AC in summer), grid-independent. Includes backup generator.

| Component | Cost |
|---|---|
| 3 kW solar array (10× 300W), adjustable ground mount | $2,500–4,000 |
| 80A MPPT charge controller (48V) | $400–600 |
| 15 kWh LiFePO4 bank (48V, commercial integrated) | $6,000–9,000 |
| 5 kW pure sine wave inverter/charger (48V, Victron or equiv.) | $1,500–2,500 |
| Transfer switch, AC distribution panel | $400–700 |
| 6 kW diesel generator (Kubota, Kohler, Generac) | $3,000–5,000 |
| Wiring, conduit, install materials | $800–1,500 |
| Battery monitoring, communications | $200–400 |
| **Total** | **$14,800–23,700** |

Powers: full household lighting, refrigeration/freezer (standard electric), well pump (daily), laptop/entertainment, power tools (1–2 at a time). Heating: wood stove primary, propane backup. No whole-house electric heat.

---

## Midwest-Specific Considerations

### Ice, Snow, and Panel Management

Zone 5 averages 25–50 inches of annual snowfall (Chicago: 37 in.; Des Moines: 32 in.; Milwaukee: 49 in.) [40]. Snow on panels is a nuisance, not a system crisis:

- Panels at 40°+ tilt typically self-clear within 1–2 sunny days
- Panels at 20–30° (most roof-mount systems) may hold snow for 3–7 days
- Priority: ensure mount structure and roof penetrations are waterproofed; ice dams at penetrations cause leaks
- **Do not use metal tools on panels**: Tempered glass cracks easily from thermal shock or impact. Use a soft roof rake or allow natural clearing.

### Humidity and Corrosion

Zone 5 Midwest relative humidity averages 60–80% year-round [1]. All battery enclosures should be sealed against moisture ingress:

- LiFePO4 cells: rated for operation to 95% RH, but BMS electronics and terminals corrode in humid environments over time
- Sealed NEMA 3R or 4 enclosures for outdoor battery installations
- Apply dielectric grease to all DC terminals annually
- Fused connections: use ring terminal crimps with heat shrink — wire nuts corrode and arc in DC circuits

### Spring Tornado and Derecho Wind Loading

April–June tornado and derecho season brings 60–80 mph sustained winds and gusts to 100+ mph. Ground-mount solar arrays in these conditions are projectiles if improperly anchored.

**Structural requirements:**
- Ground mounts: concrete pier footings, minimum 36" deep (below frost line), 12" diameter; anchor bolts through base plate
- Array wind load: 20–40 psf lateral for typical Midwest exposure per ASCE 7 [41]
- Manufacturer wind ratings: most commercial panel mounts are rated to 90–100 mph; verify for your specific product
- In tornado watch/warning: if array is portable or lightweight, move panels to sheltered location. Fixed ground mounts should be designed for 90+ mph without modification.

### Day-Length Seasonal Swing

Zone 5 at 41°N latitude experiences 8 hours 44 minutes of daylight on December 21 and 15 hours 13 minutes on June 21 — a 6.5-hour swing [42]. This is larger than most non-polar climate zones and is the primary driver for oversizing winter storage or accepting generator supplementation in winter.

**Practical implication**: align work schedules to available light in winter. Avoid starting high-power tasks (well pump, power tools) before 9 am or after 3 pm in December — solar generation is minimal at low sun angles, and battery-only operation at those times accelerates winter deficit.

---

## Wiring Safety and Code Compliance

### DC Wiring — The Most Common Failure Mode

Most off-grid system fires start with undersized DC wiring, loose connections, or absent fusing. DC arcs do not self-extinguish the way AC arcs do (no zero-crossing), and can sustain combustion indefinitely.

**Wire sizing (12V DC, single run):**

| Load | Maximum current | Minimum wire gauge | Max run (3% voltage drop) |
|---|---|---|---|
| 5W LED strip | 0.5A | 18 AWG | 40 ft |
| 20W LED array | 1.7A | 16 AWG | 30 ft |
| 100W device | 8.5A | 12 AWG | 25 ft |
| 400W load | 33A | 8 AWG | 15 ft |
| 1,000W load | 83A | 4 AWG | 8 ft |

**Fusing rule**: every positive wire must be fused as close to the battery as possible — within 18 inches. Use properly rated DC fuses (MIDI, ANL, or inline blade fuses for smaller runs). AC fuses and circuit breakers are not rated for DC breaking capacity.

**Grounding**: in a 12V DC system, negative grounding (chassis/earth ground) prevents common-mode failures and is required by NEC Article 690 for solar installations [43].

### NEC Article 690 (Solar Photovoltaic Systems)

All solar installations in the US are subject to NEC 690, adopted in most jurisdictions as part of the local building code. Key requirements:

- Rapid shutdown requirement (NEC 690.12): residential rooftop systems must have a rapid shutdown mechanism to de-energize conductors on the roof in case of emergency
- Ground fault protection required
- All wiring in conduit or rated for outdoor/UV exposure (USE-2 or PV wire)
- Permit and inspection required for most grid-tied and larger off-grid installations

**Rural properties without code enforcement**: even without permit requirement, following NEC 690 wiring standards prevents fires and equipment failures.

---

## Equipment and Materials List

### Tier 1 — Immediate Lighting Resilience (Under $100)

- [ ] 4× AA battery-powered LED lanterns: $15–25 each ($60–100 total)
- [ ] 48× AA Energizer batteries (4-year supply): $25–40
- [ ] Hand-crank NOAA weather radio with USB output (Eton FRX5): $50–70
- [ ] 12V car adapter + USB hubs for vehicle phone charging: $15–25
- [ ] Headlamps × 2 (Black Diamond Spot 400): $35–40 each

### Tier 2 — Small Solar System ($400–700)

- [ ] 100W monocrystalline solar panel: $85–110
- [ ] 20A MPPT charge controller: $45–65
- [ ] 100Ah LiFePO4 12V battery: $180–280
- [ ] 10 ft 10 AWG battery cable with ring terminals: $20–30
- [ ] 40A MIDI fuse + holder: $15–20
- [ ] 4-outlet 12V DC power strip: $20–30

### Tier 3 — Propane Integration ($200–500 startup)

- [ ] Mr. Heater Big Buddy (18,000 BTU, indoor-safe): $100–130
- [ ] 20 lb propane cylinder: $30–50
- [ ] Propane cylinder adapter hose to standard appliance (12 ft): $25–35
- [ ] CO + CO₂ detector: $30–50
- [ ] Propane camp stove (Camp Chef 2-burner): $70–100

### Tier 4 — Basic Comfort System ($3,000–5,500)

- [ ] 4× 100W panels: $340–440
- [ ] Ground mount racking: $150–250
- [ ] 40A MPPT charge controller, 24V: $120–180
- [ ] 4× 100Ah LiFePO4, 24V configuration: $1,200–1,800
- [ ] 1,500W pure sine inverter/charger: $300–500
- [ ] Battery monitor (Victron BMV-712): $120–160
- [ ] Kill-a-Watt P4400 meter: $25–35
- [ ] Clamp meter (Klein CL120): $35–60

---

## Step-by-Step Procedures

### Procedure 1: Emergency Power Triage (30 minutes)

When power fails unexpectedly:

1. **Assess duration**: call utility company outage line; check outage map. Under 8 hours vs. 8–72 hours vs. extended changes all decisions.
2. **Cut non-critical loads**: unplug everything not needed. One LED lantern per occupied room, one phone charger. Everything else off.
3. **Assess heating**: if winter, how long until interior temperature drops to 50°F? (See shelter.md calculation.) Activate propane heater or wood stove immediately if outage is likely > 4 hours in cold weather.
4. **Assess food**: if outage > 4 hours, refrigerator food is at risk past 4 hours (FDA guideline) [44]. In winter, move to cold garage or cooler with ice; chest freezer stays frozen 48–72 hours if sealed.
5. **Activate backup power**: if generator available, connect per manual transfer switch protocol. If solar battery system available, verify SOC and connect critical loads.
6. **Communicate**: let one out-of-household contact know your status.

### Procedure 2: Commissioning a New 12V Solar System (4–6 hours)

1. **Pre-wire battery connections**: connect all battery cables and fuse holders BEFORE connecting panel or charge controller. Verify polarity at every connection.
2. **Mount charge controller**: indoors or in weatherproof enclosure; near battery bank.
3. **Connect battery to charge controller**: follow manufacturer polarity markings (usually +/- terminals clearly labeled). Charge controller should power on.
4. **Configure charge controller**: set battery type (LiFePO4), voltage (12V), and absorption/float voltages. LiFePO4 correct values: absorption 14.4–14.6V, float 13.6V, low disconnect 11.0–11.5V [8].
5. **Mount panels**: assemble racking, position panel for unshaded southern exposure, secure per mount instructions.
6. **Connect panels to charge controller**: per polarity; controller should show charge current within minutes if sunlight is available.
7. **Verify system**: measure battery voltage with multimeter (should be rising if sunny). Check charge controller display for PV watts.
8. **Connect loads**: add LED fixtures, USB chargers, inverter through fused connections.

### Procedure 3: Winter Battery Care Protocol (Monthly, November–March)

1. Verify battery enclosure temperature is above 32°F before attempting to charge. If below: do not connect charging source until temperature is confirmed above 32°F.
2. Check cell voltages (if accessible): all cells in a balanced bank should be within 0.05V of each other.
3. Inspect all terminals: wipe clean any white or blue corrosion with dry rag; apply dielectric grease.
4. Log current SOC and compare to previous month: downward trend indicates load exceeds generation or cells degrading.
5. If battery is consistently discharging deeper than 50% SOC: reduce loads, run generator supplement, or add panels.

---

## Primary Sources and References

### Solar Resource Data
| # | Resource | URL | Notes |
|---|---|---|---|
| [1] | Solcast — Bright US Midwest 2024 analysis | https://solcast.com/blog/bright-us-midwest-contrasts-with-cloudy-coasts-in-2024 | Cloud cover, irradiance; 2024 Midwest anomaly data |
| [2] | NREL PVWatts Calculator | https://pvwatts.nrel.gov/ | Monthly generation estimates; use Chicago (ORD) station for Zone 5 baseline |
| [7] | Expert CE — Designing for Wind & Snow Loads on Solar | https://expertce.com/learn-articles/designing-solar-wind-snow-loads/ | Tilt optimization for winter; snow load compliance |
| [40] | National Weather Service — Snowfall Climatology | https://www.weather.gov/lot/Chicago_Snowfall_Climatology | Chicago annual snowfall; zone 5 snow reference |
| [42] | NOAA Solar Calculator | https://gml.noaa.gov/grad/solcalc/ | Day length by latitude and date |

### Battery Technology
| # | Resource | URL | Notes |
|---|---|---|---|
| [3] | RELiON — LiFePO4 Cold Temperature Performance | https://www.relionbattery.com/knowledge/how-do-lifepo4-batteries-perform-in-cold-temperatures | Lithium plating mechanism; temperature limits |
| [4] | Battle Born Batteries — Heated Lithium Cold Weather | https://battlebornbatteries.com/heated-lithium-batteries-providing-warmth-power-cold-weather/ | Cold-weather solutions; heated battery options |
| [5] | Motoma — Solar Battery Cost Guide 2025 | https://motoma.com/industry/solar-battery-cost-in-2025---how-much-does-a-home-system-cost.html | 2025 pricing; LiFePO4 vs alternatives |
| [8] | Bioenno Power — Optimize LiFePO4 in Freezing Temperatures | https://www.bioennopower.com/blogs/news/optimize-your-lifepo4-battery-in-freezing-temperatures | BMS function; voltage tables; balancing |
| [9] | Anern Store — Sizing LiFePO4 for Islanded Homes | https://www.anernstore.com/blogs/off-grid-solar-solutions/sizing-lifepo4-islanded-vs-grid | Bank sizing methodology; top-balancing |
| [11] | Renogy — MPPT vs PWM Buyers Guide | https://www.renogy.com/blogs/buyers-guide/lithium-batteries-in-cold-weather | Charge controller selection; cold weather MPPT advantage |

### Inverters and Power Electronics
| # | Resource | URL | Notes |
|---|---|---|---|
| [10] | Eaton — Pure sine wave vs modified sine wave | https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/pure-sine-wave-vs--modified-sine-wave-explained.html | Device compatibility; efficiency comparison |
| [6] | K-TOR — Power Box Generator specifications | https://www.k-tor.com/power-box.html | Hand-crank output specs; 50W rating |

### Heating Systems
| # | Resource | URL | Notes |
|---|---|---|---|
| [30] | NOAA Climate Data Online — Chicago Heating Degree Days | https://www.ncei.noaa.gov/cdo-web/ | Annual HDD; climate zones |
| [31] | NREL — Passive Solar Strategies for Midwest | https://docs.nrel.gov/docs/legosti/old/17254.pdf | South glass ratios; thermal mass; overhang calculations |
| [32] | US EPA — Choosing the Right Wood-Burning Stove | https://www.epa.gov/burnwise/choosing-right-wood-burning-stove | Step 2 certification; current emissions standard |
| [33] | NESCAUM — Assessment of EPA Residential Wood Heater Program | https://www.nescaum.org/documents/nescaum-review-of-epa-rwh-nsps-certification-program-rev-3-30-21.pdf | Efficiency ranges; testing methodology critique |
| [34] | Missouri Extension — Wood Fuel Heating | https://extension.missouri.edu/media/wysiwyg/Extensiondata/Pub/pdf/agguides/forestry/g05450.pdf | Species BTU content; seasoning requirements |
| [35] | Ecohome — Rocket Mass Stoves vs Wood Stoves | https://www.ecohome.net/en/guides/4156/rocket-stoves-the-high-efficiency-diy-alternative-to-masonry-heaters/ | Efficiency claims; code compliance discussion |
| [36] | Paul Wheaton — Efficient Clean Wood Heat | https://paulwheaton.com/efficient-wood-heat/ | RMH community reference; practical construction |
| [37] | NEEP — Cold Climate ASHP Specification v4.0 | https://neep.org/sites/default/files/media-files/cold_climate_air_source_heat_pump_specification_-_version_4.0_final.pdf | COP at 5°F; rated performance standards |
| [38] | DOE — Detailed Air-Source HP Evaluation for Very Cold Climates | https://www.energy.gov/sites/default/files/2024-11/bto-peer-2024_32264-detailed-air-source-hp-evaluation-for-very-cold-climates-munk.pdf | COP > 1.0 at -35°F; 2024 research |
| [39] | EnergySage — Geothermal Heat Pump Cost 2025 | https://www.energysage.com/heat-pumps/costs-benefits-geothermal-heat-pumps/ | GSHP installed cost ranges; payback |

### Wind and Hydro
| # | Resource | URL | Notes |
|---|---|---|---|
| [12] | DOE NREL — Distributed Wind ATB 2024 | https://atb.nrel.gov/electricity/2024/distributed_wind | Small wind capacity factors; cost trends |
| [13] | DOE WINDExchange — Maps and Data | https://www.energy.gov/windexchange/maps | County-level wind resource maps; free screening tool |
| [14] | NREL — Wind Energy Resource Atlas | https://www.nrc.gov/docs/ML0609/ML060940383.pdf | Historical wind resource; Midwest ratings |
| [15] | Thake, J. — Micro-hydro Pelton Turbine Manual | https://www.amazon.com/Micro-Hydro-Pelton-Turbine-Manual-Installation/dp/1853394602 | DIY Pelton design; 100W–100kW range |
| [16] | PowerSpout — Home Scale Micro Hydro | https://www.powerspout.com/ | Commercial turbine specs; head/flow selection |
| [17] | Harris Microhydro | https://www.harrismicrohydro.com/ | Custom turbine systems; US-based |
| [18] | DOE — Microhydropower Systems | https://www.energy.gov/energysaver/microhydropower-systems | General micro-hydro primer; resource assessment |

### Propane and Fuel Storage
| # | Resource | URL | Notes |
|---|---|---|---|
| [19] | NFPA 58 — Placing LP Gas Containers Fact Sheet | https://www.nfpa.org/downloadable-resources/fact-sheets/placing-lp-gas-containers-fact-sheet | Setback requirements by tank size; NFPA 58 (2017) |
| [22] | OSHA 1910.106 — Flammable Liquid Storage | https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.106 | Residential storage limits; container requirements |

### Biogas
| # | Resource | URL | Notes |
|---|---|---|---|
| [23] | Penn State Extension — Biogas from Manure | https://extension.psu.edu/biogas-from-manure | Methane yield; volatile solids; system design |
| [24] | Frontiers in Energy Research — Anaerobic Digestion Temperature Effects | https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2021.740314/full | Temperature dependence of methanogen activity; 2021 peer-reviewed |
| [25] | Mother Earth News — DIY Biogas Generator | https://www.motherearthnews.com/sustainable-living/renewable-energy/biogas-generator-zm0z14aszrob/ | DIY design plans; construction overview |
| [26] | University of Missouri Extension G1881 — Generating Methane from Manure | https://extension.missouri.edu/publications/g1881 | Manure yields; digester types |

### Vehicle-to-Home
| # | Resource | URL | Notes |
|---|---|---|---|
| [27] | Green Car Reports — F-150 Lightning V2H | https://www.greencarreports.com/news/1141671_how-the-ford-f-150-lightning-could-help-lower-electric-bills | F-150 Lightning system specs; 131 kWh capacity |
| [28] | Recharged — EVs with V2H Charging 2026 | https://recharged.com/articles/evs-with-vehicle-to-home-charging | Ioniq 9, EV9 V2H deployment status |
| [29] | EOS Energy — Nissan Leaf V2H US Availability | https://www.eos-e.com/blog/nissan-leaf-v2h | Leaf V2H limitations; US market status |

### Grid Interconnection and Codes
| # | Resource | URL | Notes |
|---|---|---|---|
| [20] | NREL — IEEE 1547-2018 Standard Guidance | https://www2.nrel.gov/grid/ieee-standard-1547/ | Interconnection requirements; state adoption tracker |
| [21] | Silfab Solar — PV and Extreme Weather | https://silfabsolar.com/solar-pv-and-extreme-weather/ | Panel snow load ratings; wind load; 40 psf reference |
| [41] | Solar Permit Solutions — Wind and Snow Load Analysis | https://www.solarpermitsolutions.com/blog/solar-wind-load-snow-load-analysis | ASCE 7 solar array loading; wind exposure categories |
| [43] | NEC Article 690 — Solar Photovoltaic Systems | https://www.nfpa.org/codes-and-standards/nfpa-70-standard-development/70 | Wiring, grounding, rapid shutdown requirements |

### Food and Medical Crosslinks
| # | Resource | URL | Notes |
|---|---|---|---|
| [44] | FDA — Safe Food Storage During Power Outage | https://www.fda.gov/food/buy-store-serve-safe-food/food-safety-power-outage | 4-hour refrigerator safety window; food disposal guidance |

---

## Cross-References

- **Heating fuel (firewood)**: See `individual/03-shelter.md` — wood stove sizing, chimney installation, firewood math
- **Water pumping**: See `individual/01-water.md` — hand pump options, cistern gravity systems, well pump power requirements
- **Food preservation**: See `individual/02-food.md` — root cellar as zero-power refrigeration; propane refrigerator integration with food systems
- **Heating and cooling systems (full depth)**: See `off-grid-living/07-heating-cooling.md`
- **Community-scale energy**: See `community/04-energy.md` (planned) — microgrid coordination, shared generation, neighborhood-level resilience
- **Agriculture power (irrigation, equipment)**: See `individual/06-agriculture.md`
