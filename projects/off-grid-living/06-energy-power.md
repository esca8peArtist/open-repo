---
title: "Energy & Power — Off-Grid Reference"
domain: 6
project: off-grid-living
status: complete
created: 2026-04-13
cross-refs: [01-site-selection, 03-water, 07-heating-cooling, 11-communications, 15-disaster-scenarios]
---

# Domain 6: Energy & Power

> Power is the force multiplier for every other system. Water pumps, refrigeration,
> communications, tools, medical equipment — all depend on it. Design your energy
> system for the worst realistic week, not the average sunny day. Build in redundancy
> before you build in comfort.

---

## Quick-Reference Decision Framework

Before reading further, locate yourself in one of these starting positions:

| Site condition | Primary system | Backup | First action |
|---|---|---|---|
| Good solar resource (>4 peak sun hours), no stream | Solar PV + LiFePO4 | Propane generator | Section 1 load calc, then Section 2 sizing |
| Year-round stream with 30+ ft head | Micro-hydro primary, solar secondary | Generator | Section 6 hydro assessment first |
| High wind site (>10 mph average) with cloudy winters | Solar + wind hybrid | Generator | Section 7 wind assessment, then Section 8 integration |
| All of the above uncertain | Solar PV + LiFePO4 — it works everywhere | Generator | Section 1 load calc |
| Nuclear/disaster scenario focus | Manual fallbacks + hardened spares | Everything above | Section 11 EMP/emergency |

Work through Section 1 (load calculation) before making any purchasing decisions. Undersizing and oversizing are both expensive mistakes; the math is straightforward.

---

## 1. Energy Needs Assessment

The most common off-grid mistake is guessing at load and then being surprised by either empty batteries or a massively over-built system. Do the math first.

### 1.1 Load Calculation Methodology

The basic approach: list every electrical load, its wattage, and its average daily run hours. Sum the daily watt-hours. That is your daily energy demand. Everything else — panel count, battery bank, inverter size — flows from this number.

**Step 1: List loads with wattage and daily hours**

| Appliance | Typical watts | Notes |
|---|---|---|
| LED bulb (per fixture) | 8–15 W | Replace all incandescents immediately |
| LED shop light (4-ft) | 40–50 W | |
| Chest freezer (efficient, 5 cu ft) | 30–60 W avg | Cycles; use average over 24 hrs |
| Chest freezer (older, 15 cu ft) | 80–150 W avg | Replace with efficient unit |
| Propane fridge (electric ignition) | 3–10 W | Mostly for controls/ignition |
| 12V DC refrigerator (Dometic, Vitrifrigo) | 25–40 W avg | Best choice for off-grid |
| Laptop computer | 45–90 W | |
| Desktop computer | 100–300 W | |
| Phone charging | 5–20 W | |
| Tablet | 10–20 W | |
| Internet router / modem | 5–20 W | Run 24/7; constant load |
| Starlink dish (flat, 2nd gen) | 50–75 W avg | Peaks to 100 W; use avg |
| Ham radio (receive) | 5–20 W | |
| Ham radio (transmit, 100W) | 200–300 W | Short duty cycle |
| Small water pump (12V, 1/3 HP) | 300–400 W | Run time varies greatly |
| Well pump (1/2 HP submersible, 240V) | 750–1,000 W | Runtime: 1–2 hrs/day typical |
| Washing machine (front-load efficient) | 300–500 W | |
| Spin dryer (non-heat) | 300–400 W | Replace clothes dryer |
| Electric clothes dryer (avoid) | 4,000–6,000 W | Do not use off-grid |
| Electric stove (avoid) | 1,200–3,000 W/burner | Use propane instead |
| Electric water heater (avoid) | 4,000–5,500 W | Use solar thermal or propane |
| Mini-split AC (1 ton, 12,000 BTU) | 800–1,200 W avg | Seasonal; see Section 7 heating doc |
| Power tool: circular saw | 1,200–1,800 W | Short bursts |
| Power tool: drill | 300–600 W | Short bursts |
| Power tool: angle grinder | 700–1,400 W | Short bursts |
| Bench grinder | 250–400 W | Short bursts |
| Welder (small MIG) | 3,000–7,500 W | Short bursts; generator preferred |
| Medical CPAP | 30–60 W | If applicable; run nightly |
| Medical nebulizer | 150–250 W | If applicable; short runtime |
| Pulse oximeter, BP cuff, small devices | 5–20 W | |

**Step 2: Calculate daily watt-hours (Wh/day)**

```
Daily Wh = Watts × Hours per day
```

Example household (2 adults, 2 children — moderate comfort, no propane appliances):

| Load | Watts | Hours/day | Wh/day |
|---|---|---|---|
| LED lighting (8 fixtures avg on) | 80 | 4 | 320 |
| 12V DC refrigerator | 35 avg | 24 | 840 |
| Chest freezer (efficient) | 45 avg | 24 | 1,080 |
| Laptops (2) | 120 | 6 | 720 |
| Phone/tablet charging | 40 | 3 | 120 |
| Internet router + Starlink | 90 | 24 | 2,160 |
| Water pump (1/2 HP, 240V) | 850 | 1.5 | 1,275 |
| Washing machine | 400 | 1 | 400 |
| Misc small loads | 100 | 4 | 400 |
| **Total** | | | **7,315 Wh/day** |

Round to **7.5 kWh/day** — a realistic moderate-comfort household without electric cooking, heating, or clothes drying.

**Step 3: Seasonal adjustment**

Summer and winter consumption differ. Summer: AC loads may add 3–8 kWh/day in hot climates. Winter: longer lighting hours add 0.5–1 kWh/day; heating fans or circulators may add 1–2 kWh/day; but solar production also drops (fewer peak sun hours, lower sun angle). Design for the worst combination: your highest-demand season coinciding with your lowest-production season.

In most of the US, the critical design period is **December–January**: shortest days, lowest sun angle, highest lighting load, and often heating loads added.

### 1.2 Household Size Benchmarks

Use these as sanity checks after doing your own load calc:

| Household profile | Daily kWh demand | Notes |
|---|---|---|
| 1 person, minimal (lighting + laptop + fridge) | 1.5–3.0 kWh | No AC, no large appliances |
| 2-person cabin, basic comforts | 3.0–5.0 kWh | Fridge, freezer, lights, comms |
| Family of 4, moderate (propane cooking/heat) | 5.0–9.0 kWh | This document's worked example |
| Family of 4, full electric (no propane) | 15–30 kWh | Requires very large system |
| Working homestead (shop tools, pumping) | 8–15 kWh | Includes periodic heavy loads |

**Key design decision**: Electric cooking and water heating are the largest discretionary loads. Eliminating them by using propane reduces system size — and cost — by 30–60%. This is almost always the right call for off-grid builds.

### 1.3 Load Reduction First

Before sizing any power system, cut loads. In order of impact:

1. Switch to propane cooking, water heating, and space heating (see Domain 7)
2. Replace any incandescent or CFL lighting with LEDs
3. Replace a full-size refrigerator with a 12V DC chest-style unit (SunDanzer, Vitrifrigo, Isotherm)
4. Eliminate electric clothes dryer — use spin dryer + line dry
5. Replace electric well pump with a solar-direct pump (Grundfos SQFlex, Lorentz) or pressure-tank-and-fill system
6. Use DC-native devices where possible — every DC-to-AC-to-DC conversion loses 5–15%

---

## 2. Solar Photovoltaic Systems

### 2.1 Panel Types

**Monocrystalline silicon (mono-Si)**
The standard choice for off-grid in 2025. Efficiency 20–23% for mainstream panels, up to 24–25% for premium (SunPower, REC Alpha). Higher efficiency means more watts per square foot — important when roof or ground space is limited. Temperature coefficient typically -0.35 to -0.45%/°C — performance degrades in heat but less than poly. Best for most applications.

**Polycrystalline silicon (poly-Si)**
Older technology, now largely superseded by monocrystalline at similar price points. Efficiency 15–17%. Slightly worse temperature performance. Harder to find as of 2025 — manufacturers have largely shifted to mono. Avoid unless clearing old stock at significant discount.

**Thin-film (CdTe, CIGS, amorphous silicon)**
- CdTe (First Solar): Efficiency 18–20%, excellent low-light and high-temperature performance, lower temperature coefficient (-0.32%/°C). Primarily commercial scale.
- CIGS (flexible): Efficiency 12–16% for flexible panels, useful for curved surfaces or lightweight applications. Higher cost per watt. Not ideal as primary off-grid source.
- Amorphous silicon: Low efficiency (6–8%), performs better in diffuse/cloudy light than crystalline but requires 2–3x more area for same output. Rarely the right choice.

**Bifacial panels**
Both sides generate power; the rear collects reflected albedo light. Yield gains of 5–30% depending on ground reflectivity (snow is 80%, grass is 20%). Premium ~10% over monofacial. Best on ground mounts over light-colored gravel or snow-likely terrain.

**For most off-grid builds**: 400–500W monocrystalline panels from Tier 1 manufacturers (Longi, Canadian Solar, Jinko, Q CELLS, REC, Silfab) at $0.25–$0.45/W (wholesale) or $0.40–$0.80/W (retail/DIY) are the correct choice as of 2025.

### 2.2 Sizing Calculations

**Peak sun hours (PSH)** is not "hours of daylight" — it is the equivalent number of hours at 1,000 W/m² (full sun). A day with 8 hours of moderate sun might deliver only 5 PSH.

**PSH by US region (annual average, south-facing fixed mount):**

| Region | Annual avg PSH | Winter worst-month PSH |
|---|---|---|
| Southwest desert (AZ, NM, S. CA) | 5.5–7.0 | 4.5–5.5 |
| Southeast (GA, FL, AL, MS) | 4.5–5.5 | 3.5–4.5 |
| Texas / Oklahoma | 5.0–6.0 | 4.0–5.0 |
| Midwest (IA, IL, MO, KS) | 4.0–5.0 | 2.5–3.5 |
| Pacific Northwest (WA, OR west of Cascades) | 3.5–4.5 | 1.5–2.5 |
| Appalachia / Southeast mountains | 4.0–4.8 | 2.5–3.5 |
| Rocky Mountain states | 5.0–6.5 | 3.5–4.5 |
| Northern plains (ND, SD, MN) | 4.5–5.5 | 2.5–3.0 |

Use NREL's PVWatts calculator (pvwatts.nrel.gov) for precise site-specific data — enter your coordinates, tilt angle, and azimuth.

**Basic panel array sizing formula:**

```
Array kW = (Daily kWh demand) / (PSH × derating factor)
```

**Derating factor** accounts for real-world losses: temperature, wiring resistance, soiling, inverter/controller inefficiency, module mismatch. Use **0.75** as a conservative default (represents ~25% combined losses). Use 0.80 for a well-designed system in a clean environment.

**Worked example** (7.5 kWh/day demand, Midwest in December, PSH = 3.0):

```
Array kW = 7.5 / (3.0 × 0.75) = 7.5 / 2.25 = 3.33 kW
```

Round up to **3.5–4.0 kW** of panels to provide margin.

**Battery charging ratio**: Add 20–25% to the above to also cover battery charging losses (typically 90–95% for LiFePO4, 80–85% for lead-acid).

**Panel tilt angle for fixed mount:**

- Optimal annual average tilt = your latitude (e.g., 35° for Nashville, TN)
- For winter optimization (if you have wind/snow concerns): tilt = latitude + 15°
- For summer optimization: tilt = latitude − 15°
- Rule of thumb for off-grid where winter is the critical period: use latitude + 10° to 15°

A south-facing roof in most US locations within 15° of true south loses less than 5% of annual yield from suboptimal azimuth.

**Tilt and snow shedding**: In snow country, steeper tilt (50–60°) sheds snow better. Panels buried under snow produce zero watts. Design mounts at 45°+ if winter snow is regular.

### 2.3 Array Configurations

Panels can be wired in **series** (voltages add), **parallel** (currents add), or **series-parallel** combinations.

**Series strings**: Required to reach the input voltage of your charge controller or string inverter. If your MPPT controller needs 100–150V input and each panel is 40V Voc, wire 3 in series = 120V string.

**Parallel strings**: Multiple series strings connected in parallel multiply the current. A 4-string array of 3S panels = 3 panels × 40V = 120V, 4 strings × panel Isc = total array current.

**Practical guidelines**:
- Match panels within strings: same model, same orientation, same age. Mismatch degrades the whole string to the weakest panel.
- Keep string lengths equal in parallel configurations.
- Array voltage for 48V battery system: MPPT controllers typically accept 100–150V input. Three 400W panels at ~40V Voc in series = 120V — ideal.
- For 24V system: two panels in series (80V) into 24V MPPT works; keep array below controller max input voltage.

**Combiners and disconnects**:
- Series fuses or circuit breakers in each parallel string at the combiner box (NEC 690.9).
- Combiner box (Midnite Solar, Midnight Classic, Schneider) collects strings and provides per-string overcurrent protection.
- Array DC disconnect required by NEC 690.13 — must be accessible, lockable, rated for DC voltage and current.

**Wiring**: Use listed PV wire (USE-2/PV wire rated 600V or 1,000V) for runs between panels. Keep positive and negative conductors bundled to minimize electromagnetic interference. Size wire for less than 3% voltage drop for array runs; use 2% for longer runs (see Section 9 wiring tables).

### 2.4 MPPT vs. PWM Charge Controllers

**PWM (Pulse Width Modulation)**
The older, simpler technology. The controller connects the array directly to the battery via a switch that opens and closes rapidly. Array voltage is pulled down to near battery voltage — so a 40V panel charging a 12V battery wastes roughly 70% of the panel's voltage potential. Efficiency 70–75% for mismatched panel/battery voltages. Only makes sense if:
- Battery voltage matches panel Vmp closely (e.g., 12V nominal panel into 12V battery)
- Very small systems under 200W where cost matters more than efficiency
- Panels are otherwise free/salvaged

**MPPT (Maximum Power Point Tracking)**
The controller continuously sweeps the I-V curve of the array and operates at the true maximum power point, then converts that power to the battery's voltage at high efficiency. Real-world efficiency 93–97%. Required for any serious system. Allows higher-voltage arrays with lower-voltage batteries — enabling longer, thinner wire runs from the array.

**MPPT sizing**:

```
Controller amps = (Array watts × 1.25) / Battery bank voltage
```

The 1.25 factor (NEC 690.8 safety margin) also accounts for cold-temperature Voc boost and ensures the controller is not thermally stressed.

Example: 3,600W array, 48V battery bank:
```
Controller amps = (3,600 × 1.25) / 48 = 93.75A → use 100A MPPT controller
```

**Name-brand MPPT controllers worth buying (2025)**:
- Victron SmartSolar MPPT — excellent monitoring via Bluetooth/VRM, widely supported, 75V to 250V models from 15A to 250A
- Midnite Classic — robust, US-made, good for larger arrays
- Schneider Electric MPPT 60/80 — integrated with Schneider XW+ systems
- Renogy Rover / Wanderer — budget option for smaller systems; adequate but limited monitoring
- Epever Tracer — popular budget MPPT; use for non-critical or backup systems

**Avoid**: Generic "MPPT" controllers from unknown Chinese brands at implausibly low prices. Many are actually PWM controllers with misleading labeling. Buy from distributors with return policies and test with a clamp meter on day one.

---

## 3. Battery Storage

### 3.1 Chemistry Comparison

**Flooded Lead-Acid (FLA)**
The original off-grid battery. Still viable but requires maintenance.
- Requires watering every 1–3 months (check electrolyte level, top with distilled water)
- Vents hydrogen gas during charging — must be in ventilated enclosure; explosion risk if venting is inadequate
- Usable depth of discharge (DoD): 50% to preserve cycle life; going to 80% regularly halves cycle life
- Cycle life at 50% DoD: 500–1,500 cycles depending on temperature and maintenance
- Self-discharge: 1–3%/month at room temperature
- Temperature sensitivity: freezes at partial charge (electrolyte diluted); must remain above 0°F when charged; performance drops significantly below 32°F
- Cost: $100–$200/kWh for L-16 or golf cart batteries (cheapest storage $/kWh)
- Good brands: Trojan, Crown, US Battery, Rolls/Surrette

**AGM Lead-Acid (Absorbed Glass Mat)**
Sealed, maintenance-free, no watering. VRLA (valve-regulated) design handles hydrogen internally.
- No liquid to spill; can be mounted on side
- Slightly better cycle life than FLA if not over-discharged: 400–700 cycles at 50% DoD
- More expensive than FLA: $200–$350/kWh
- Same freeze susceptibility as FLA at low state of charge
- Good for remote or infrequently visited systems where maintenance is impossible
- Brands: Lifeline (best, aerospace-grade), DEKA, Odyssey, Trojan AGM

**LiFePO4 (Lithium Iron Phosphate)**
The correct choice for most new off-grid systems in 2025.
- Usable DoD: 80–100% (can be fully cycled without damage)
- Cycle life: 2,000–6,000+ cycles at 80% DoD depending on brand and BMS quality
- At 0.5C charge/discharge rates, premium cells (CATL, EVE, CALB) commonly exceed 4,000 cycles
- No maintenance
- No watering, no ventilation requirement for hydrogen (though thermal runaway is possible from shorting)
- Flat discharge curve: ~51.2V for a 48V nominal pack across most of the discharge range; delivers nearly rated capacity vs. lead-acid which sags under load
- Temperature: charge cutoff below 32°F (0°C) — BMS must enforce this; charging at subfreezing temperatures permanently damages cells. Discharge works down to -4°F (-20°C) with reduced capacity.
- Self-discharge: <3%/month
- Weight: 40–60% lighter than equivalent lead-acid
- Cost battery-only: $200–$400/kWh wholesale (direct China import); $350–$600/kWh retail packaged (Epoch, Chins, Ampere Time, SOK); $600–$900/kWh premium rack units (Victron, Pylontech, SimpliPhi)
- 10-year lifecycle cost is typically lower than lead-acid even at higher upfront price, once cycle life is factored in

**NMC/NCA (Lithium Nickel Manganese Cobalt / Nickel Cobalt Aluminum)**
- Higher energy density than LiFePO4 (150–250 Wh/kg vs. 90–160 Wh/kg for LFP)
- Less thermally stable — higher risk of thermal runaway; more cautious fire consideration
- Common in EV packs (Tesla, most EVs), power tools, laptops
- Less suitable than LFP for stationary off-grid storage due to safety and longevity trade-offs
- Not recommended for DIY off-grid builds

**Summary table**:

| Chemistry | $/kWh (2025) | DoD | Cycles (typical) | Maintenance | Freeze risk |
|---|---|---|---|---|---|
| Flooded LA | $100–200 | 50% | 500–1,500 | High | Yes, if discharged |
| AGM | $200–350 | 50% | 400–700 | None | Yes, if discharged |
| LiFePO4 | $200–600 | 80–100% | 2,000–6,000 | None | Charge cutoff <0°C |
| NMC | $250–500 | 80% | 1,000–2,000 | None | Charge cutoff <0°C |

### 3.2 Bank Sizing

**Days of autonomy**: How many days can the battery bank power your loads with zero solar input? Two to three days is standard for most locations. Five days is appropriate for extended cloudy periods (Pacific NW winter, hurricane belt).

**Bank sizing formula (LiFePO4, 80% DoD):**

```
Usable kWh needed = Daily kWh × Days of autonomy
Bank kWh = Usable kWh / 0.80  (DoD factor)
```

Example: 7.5 kWh/day × 3 days / 0.80 = **28.1 kWh bank**

For lead-acid at 50% DoD: 7.5 × 3 / 0.50 = 45 kWh of rated capacity needed for same autonomy — 60% more battery mass and volume for equivalent storage.

**Amp-hour sizing** (for 48V nominal system):

```
Ah = kWh × 1,000 / Nominal voltage
```

28.1 kWh at 48V nominal = 28,100 / 48 = **585 Ah** at 48V

Round up to 600 Ah — e.g., two 300 Ah 48V rack batteries in parallel, or a 24S LiFePO4 custom bank at 600 Ah.

### 3.3 BMS Requirements

Every lithium battery bank must have a BMS (Battery Management System). Functions:
- Cell voltage balancing (top balancing or bottom balancing depending on design)
- Overvoltage protection: disconnect charge if any cell exceeds 3.65V (LFP)
- Undervoltage protection: disconnect load if any cell drops below 2.5V (LFP)
- Overcurrent protection: disconnect on excessive discharge current
- Short circuit protection
- Over/undertemperature protection: block charging below 0°C, block operation above 55°C
- State of charge estimation

**Critical**: Never connect a lithium bank without a BMS. Never bypass the BMS except for momentary diagnostic testing.

For DIY builds using raw prismatic cells (EVE, CATL, CALB), the BMS is purchased separately:
- Daly BMS: budget option, widely used; functional but limited communication
- Overkill Solar BMS: popular in DIY community, Bluetooth monitoring
- JK BMS (Jikong): active balancing, good communication, reliable; recommended for 100–400 Ah builds
- Batrium, Orion BMS: professional-grade, used in larger custom builds
- REC BMS: CAN bus integration with Victron ecosystem

**Pre-built LiFePO4 packs** (2025 recommended options):
- Epoch Batteries 200Ah 48V: strong reputation, 10-year warranty, ~$2,400
- SOK Battery 200Ah 48V: good value, $1,500–1,800
- Ampere Time / LiTime 200Ah 48V: budget-tier but functional, ~$1,200
- Pylontech US5000 (4.8 kWh rack): excellent CAN bus integration with Victron/SMA, ~$1,500 per unit
- Victron Lithium Smart 200Ah 25.6V: premium, seamless Victron integration, ~$1,800

### 3.4 Series and Parallel Wiring

**Parallel**: Connect multiple identical batteries positive-to-positive, negative-to-negative. Voltage stays the same; capacity (Ah) adds. All batteries must be identical (same model, same age ideally). Use equal-length cables from each battery to the bus bar to ensure equal current sharing.

**Series**: Connect positive of one to negative of next. Voltages add; capacity (Ah) stays the same. Used to reach system voltage (e.g., four 12V batteries in series = 48V bank).

**Best practice for large banks**: Use a bus bar system rather than daisy-chaining terminals. Fuse each parallel string (class T fuse or MRBF terminal fuse) at the battery terminal before combining at the bus bar.

**Temperature matching**: In cold climates, insulate the battery bank enclosure but do not heat it actively unless temperatures routinely drop below -4°F (-20°C). The goal is keeping batteries in the 50–80°F range for optimal performance.

### 3.5 Safety

- LiFePO4 thermal runaway is possible but rare; the main causes are: external short circuit, physical puncture of cells, charging with failed BMS above max voltage, charging while frozen.
- Install a smoke detector and CO detector in any battery/generator room.
- Keep a Class C or ABC dry chemical fire extinguisher within reach. Note: water makes lithium battery fires worse. A lithium-specific extinguisher (F-500, AVD) is preferred for pack fires.
- No smoking, open flames, or sparks in the battery room.
- Fuse all conductors leaving the battery bank before the first connection point. The short-circuit current of a large battery bank can exceed 5,000A for milliseconds — unfused conductors will vaporize and start fires.

---

## 4. Inverters

### 4.1 Pure Sine vs. Modified Sine Wave

**Modified sine wave (MSW)**: Cheaper ($100–$400 for 1,000–2,000W). Produces a stepped approximation of a sine wave. Acceptable for resistive loads (incandescent lights, simple heating elements, basic tools). **Not acceptable** for:
- Motors (runs hot, reduces motor life, may not start)
- Variable-speed drives (VFD)
- Some battery chargers
- Audio equipment (audible hum)
- Medical equipment (CPAP, infusion pumps — check manufacturer spec)
- Any device with active power factor correction

**Pure sine wave (PSW)**: Required for all modern electronics, motor loads, and medical equipment. Produces a clean 60 Hz sine wave indistinguishable from grid power. Cost $200–$1,500 for 1,000–4,000W. Buy pure sine for any off-grid system that powers a modern home. Modified sine is only acceptable for a dedicated tool shed or simple emergency lighting.

### 4.2 Inverter-Charger Combos

A combined inverter-charger (often called an "inverter/charger" or "multiplus") adds a battery charger function — when grid or generator power is present, the unit charges the battery bank and can pass power through to loads simultaneously. This is the correct architecture for off-grid homesteads.

**Leading inverter-charger brands (2025)**:
- **Victron MultiPlus-II**: Industry standard for off-grid. Models from 800W to 10,000W. Integrates with Victron's GX control system, Cerbo GX, VRM cloud monitoring. Parallel operation for 3-phase or higher power. 48V models preferred. 5,000VA model ~$1,200.
- **Victron Quattro**: Like MultiPlus but with two AC inputs (grid + generator with automatic switching). Higher price but eliminates need for a separate transfer switch.
- **Schneider Electric XW+**: Robust, US-assembled, popular in professional installations. 6,000W and 8,000W models. ~$2,500–$3,500.
- **Magnum Energy MSH**: Reliable US product, older but proven design.
- **Growatt SPF**: Budget option for smaller systems; adequate monitoring, less refined than Victron.
- **EG4 6000XP / 18kPV**: US-distributed, competitive price, good community support; popular for larger DIY off-grid builds.

**Do not buy**: Generic brand inverter-chargers from Amazon without established community support and firmware update history.

### 4.3 Sizing for Surge Loads

Motors require 3–7× their running wattage to start (inrush/surge current). Size your inverter for the highest concurrent surge load, not just the running load.

Example: Running loads = 2,500W. Well pump (1 HP, 750W running) surges to ~3,500W on start. Total surge requirement = 2,500 + 3,500 = 6,000W. Use a 6,000W or larger inverter.

**Inverter sizing rule of thumb**: Select a continuous watt rating 1.25–1.5× your expected maximum running load. For surge tolerance, the inverter's surge rating (usually 2× continuous for 5–30 seconds) must exceed your worst-case motor start.

Running two large motors simultaneously (well pump + washing machine motor) creates the worst-case surge scenario. Stagger start times in practice.

### 4.4 Transfer Switching

When a generator or grid tie is present, transfer switching disconnects one source before connecting another. Never parallel a generator and inverter output without proper automatic transfer equipment.

**Options**:
- Built-in transfer relay in inverter-charger (Victron MultiPlus has this) — seamless, sub-20ms transfer
- Manual transfer switch (inexpensive, requires manual action — acceptable for planned generator use)
- Automatic transfer switch (ATS): senses loss of primary source, switches to backup within 1–10 seconds. Required if generator is auto-start. Cost: $200–$600 for residential ATS.

---

## 5. Backup Generation

### 5.1 Generator Types

**Gasoline generators**: Inexpensive ($400–$2,000 for 3,000–8,000W), widely available fuel, but gasoline shelf life is 6–12 months without stabilizer (24 months with Sta-Bil). Carburetors gum up from ethanol in modern gasoline — drain fuel before storage, or run on ethanol-free gas (available at marinas, airports). Good brands: Honda EU7000is, Yamaha EF6300iSDE, Generac GP8000E.

**Propane generators**: Propane stores indefinitely, burns clean, no carburetor fouling. Fuel cost slightly higher than gasoline but offset by elimination of stabilizer issues and longer storage. Same engine choices as gasoline (many can be dual-fuel). Champion 7500W dual-fuel is a popular off-grid choice ($800–$1,000).

**Diesel generators**: Best fuel efficiency, longest service life (20,000+ hours for industrial engines vs. 1,500–3,000 for gasoline), diesel stores 18–24 months without treatment (PrimaLube or PRI-D extends this). More expensive upfront ($2,000–$8,000+). Preferred for high-usage scenarios (daily generator use). Brands: Kubota, Yanmar, Cummins Onan.

**Inverter generators** (Honda EU, Yamaha EF series): Electronically controlled throttle adjusts engine speed to match load. Much quieter than conventional generators (50–60 dB vs. 70–80 dB). Cleaner power output. Better fuel efficiency at partial load. Premium price ($800–$3,000 for 2,000–6,300W). Ideal for off-grid where generator runs alongside solar/battery rather than as primary source.

**Natural gas**: Requires pipeline supply — not practical for most off-grid sites. Skip.

### 5.2 Auto-Start and Remote Monitoring

An auto-start generator circuit senses battery state of charge (or voltage) and starts the generator automatically when batteries fall below a threshold (typically 20–30% SoC). When batteries are full (or a time limit is reached), the generator shuts off.

Victron Cerbo GX can trigger auto-start via a relay output. Victron's VRM portal allows remote monitoring and manual start/stop from anywhere with internet.

For dedicated auto-start: Champion and Generac make generators with built-in auto-start modules. Pair with a battery bank monitor (Victron BMV-712 or similar) and a relay interface.

### 5.3 Fuel Storage and Shelf Life

| Fuel | Shelf life untreated | With stabilizer | Notes |
|---|---|---|---|
| Gasoline | 3–6 months | 12–24 months (Sta-Bil, PRI-G) | Ethanol-free lasts longer; avoids carb issues |
| Diesel | 12–18 months | 24–36 months (PRI-D, Diesel Kleen) | Biocide needed if storing >6 months |
| Propane | Indefinite | N/A | No degradation; ideal long-term fuel |
| Kerosene | 24 months | 5+ years with stabilizer | Burns clean; limited generator use |

**Fuel rotation strategy**: FIFO (first in, first out) for gasoline and diesel. Label every container with fill date. Minimum 30-day supply on hand at all times; 90-day supply preferred.

**Storage safety**:
- Gasoline in UL-listed metal safety cans (Eagle, Justrite) — not plastic jugs
- Propane in properly rated cylinders stored upright outdoors, away from ignition sources
- Diesel in metal drums with pump, or in approved poly containers — less fire risk than gasoline
- Store fuel away from the house (30+ feet), never in an attached garage

---

## 6. Micro-Hydro Power

### 6.1 Why Micro-Hydro Excels

A properly sized micro-hydro system produces power 24 hours a day, 365 days a year — not just when the sun shines. A 1 kW micro-hydro system delivers 24 kWh/day. A 1 kW solar array in a good location delivers 4–6 kWh/day. For a site with a qualifying stream, hydro is the first choice.

**The key variables are head and flow:**

```
Power (watts) = Head (feet) × Flow (GPM) × 0.085 × efficiency
```

Or in metric:
```
Power (watts) = Head (meters) × Flow (liters/second) × 9.81 × efficiency
```

Efficiency for a well-designed Pelton or Turgo turbine: 65–85%. Use 0.70 as a conservative working estimate.

**Worked examples:**

| Head (ft) | Flow (GPM) | Estimated power |
|---|---|---|
| 20 ft | 200 GPM | 20 × 200 × 0.085 × 0.70 = 239 W |
| 50 ft | 100 GPM | 50 × 100 × 0.085 × 0.70 = 298 W |
| 100 ft | 50 GPM | 100 × 50 × 0.085 × 0.70 = 298 W |
| 200 ft | 30 GPM | 200 × 30 × 0.085 × 0.70 = 357 W |
| 100 ft | 200 GPM | 100 × 200 × 0.085 × 0.70 = 1,190 W |
| 300 ft | 50 GPM | 300 × 50 × 0.085 × 0.70 = 893 W |

Minimum practical system: 20 ft head with 30+ GPM sustained year-round, or 50 ft head with 15+ GPM. Below these thresholds, the civil works (intake, penstock, powerhouse) cost more than the value delivered.

### 6.2 Site Assessment

**Measuring head**: Use a contractor's level and tape measure (string method), a hand level with measuring rod, or a GPS altimeter. For a rough field estimate, walk the stream from proposed intake to proposed powerhouse, counting steps on slope. Measure precisely before ordering equipment.

**Measuring flow**: Build a temporary weir across the stream using a board pressed into a shallow notch. The flow through a rectangular notch:

```
Flow (GPM) ≈ 3.33 × L × H^1.5 × 449
```

Where L = notch width in feet, H = water depth over notch in feet. For a quick approximation: time how long a known volume bucket fills at the stream's natural pour-off point.

**Critical**: Measure flow in late summer (low water) and early spring (high water). Design to the minimum sustainable flow. A 100 GPM stream in April that drops to 8 GPM in August cannot support a system requiring 15 GPM minimum.

**Water rights**: In prior appropriation states (most of the West), you must hold a water right to divert water from a stream — even on your own property. Review your state's water rights database. In eastern riparian states, your rights are more flexible but still require you not to impair downstream users. Contact your state water authority before installing any intake.

### 6.3 Turbine Types

**Pelton wheel**: Used for high head (50+ feet), low-to-moderate flow. One or more water jets impinge on cup-shaped buckets on the wheel periphery. High efficiency (75–90%), robust, simple to maintain. Excellent for mountain/foothill sites. Brands: Energy Systems & Design (SD), Canyon Hydro, Teco (China).

**Turgo turbine**: Similar to Pelton but jet enters one side of the wheel and exits the other. Better for moderate head (30–100 ft) and higher flow rates than Pelton. Slightly higher flow capacity for same wheel diameter.

**Crossflow (Banki-Michell)**: Works over a wide range of head (6–200 ft) and flow conditions. Lower efficiency (~65–75%) than impulse types but handles wide variation in flow well. Often locally fabricated.

**Propeller/Kaplan**: For very low head (<20 ft) with high flow. Common in run-of-river applications. More complex mechanically. Not typical for small homestead scale.

For most homestead micro-hydro sites in the US (50–300 ft head, 10–100 GPM): **Pelton wheel** from Energy Systems & Design or equivalent is the standard recommendation.

### 6.4 Penstock Design

The penstock is the pipe that carries water under pressure from the intake to the turbine. It is often the most expensive component of a micro-hydro installation.

**Material**: HDPE pipe (high-density polyethylene) is the standard — flexible, corrosion-resistant, available in sizes from 2-inch to 12-inch, pressure-rated for 100–160 PSI. SDR 11 (pressure class) or SDR 17 depending on static head.

**Maximum static pressure**: Static head in PSI = Head in feet / 2.31. A 250-ft head = 108 PSI static. Use pipe rated for at least 1.5× the static pressure.

**Sizing for velocity**: Keep water velocity in the penstock below 5 ft/sec to minimize friction losses and water hammer. Use the Hazen-Williams formula or a pipe friction calculator.

```
Pipe diameter guideline: Q(GPM) / (velocity 3-5 ft/sec) → area in sq inches → diameter
```

A 50 GPM flow at 4 ft/sec requires approximately a 2-inch diameter pipe. A 200 GPM flow requires approximately a 4-inch pipe.

**Friction losses**: Long penstock runs lose pressure to friction. Calculate with Darcy-Weisbach or Hazen-Williams (free online calculators). A 500-foot run of 3-inch pipe at 50 GPM loses approximately 15% of head to friction — factor this into power calculations.

### 6.5 System Components

1. **Intake screen**: Stainless mesh (1/16-inch) on a submerged intake box. Exclude debris, fish, and invertebrates that would damage the turbine nozzle.
2. **Settling tank / forebay**: Small settling basin at the top of the penstock removes suspended sediment before it enters the pipe. Clean monthly during high turbidity periods.
3. **Penstock**: Discussed above.
4. **Turbine and generator**: Pelton/Turgo driving a permanent magnet alternator (PMA) for battery charging, or an induction generator for direct AC output.
5. **Electronic load controller (ELC)** or **ballast load**: Micro-hydro turbines run best at constant load. An ELC diverts excess power to a ballast (resistive heating element — space heater, water heater) when batteries are full, maintaining constant turbine speed and stable frequency. Essential for grid-tied operation; important for battery systems too.
6. **Turbine controller**: Regulates charging voltage; many modern micro-hydro units (Harris, Energy Systems & Design) include this.

---

## 7. Wind Power

### 7.1 Site Assessment

Wind resource is the most variable and hardest to predict without measurements. The US average wind speed at 80-meter hub height is 6.5–8.5 m/s across the Great Plains, 4.5–6 m/s in the Southeast, and 3.5–5 m/s in most forested/mountainous areas. **But small turbines sit at 30–50 meters, not 80, and terrain effects dominate at these heights.**

The key rules:
- Wind power scales as the cube of wind speed: doubling wind speed = 8× more power. A site with 8 m/s average is enormously more productive than one with 6 m/s.
- Turbulence destroys both energy production and turbine longevity. Trees, buildings, and terrain within 500 feet upwind cause turbulence. The tower must extend at least 30 feet above any obstacle within 500 feet.
- In most forested or hilly terrain east of the Mississippi, small wind is marginal or uneconomic. Solar will outperform it.
- In the open Great Plains, northern Rocky Mountain passes, coastal hilltops, and ridge lines: wind can be excellent.

**Data sources**:
- NREL Wind Prospector: maps.nrel.gov/wind-prospector — free, enter coordinates
- AWS Truepower WindNavigator
- Measure Your Wind: install a calibrated anemometer at tower height for 6–12 months before buying a turbine. $200–$500 for a monitoring kit. This is the only reliable method.

### 7.2 Small Turbine Options

| Turbine | Rated power | Rated wind speed | Rotor diameter | Notes |
|---|---|---|---|---|
| Bergey Excel 10 | 10 kW | 11 m/s (25 mph) | 7.0 m | Premium, US-made, 5-year warranty, proven 30-year track record |
| Primus Wind Power Air 30 | 400 W | 12.5 m/s | 1.17 m | Small, for boats/cabins, not for primary power |
| Primus Air Silent X | 400 W | 11 m/s | 1.15 m | Ultra-quiet, residential use |
| Xzeres 442SR | 10 kW | 11 m/s | 7.2 m | Good reliability record |
| Endurance E-3120 | 50 kW | 11 m/s | 21.0 m | Community-scale, not homestead |
| Chinese small turbines (2-5 kW) | 2–5 kW nominal | Various | 3–5 m | Rated power is often optimistic; verify with annual kWh data from independent installations |

**Rated power caveat**: Turbine rated power is at a specific wind speed (typically 11–13 m/s = 25–30 mph). Average wind on most sites is well below this. Annual energy production (AEP in kWh/year) at your actual average wind speed is the only meaningful metric. Ask vendors for AEP at 5 m/s, 6 m/s, and 7 m/s — these are the realistic conditions on most non-wind-specialist sites.

### 7.3 Towers

**Free-standing lattice towers**: Most economical for 30–80 ft heights. Require concrete foundation. Can be climbed for maintenance. Brands: Rohn (industry standard), US Tower.

**Tilt-up (guyed) towers**: Hinged at the base, raised and lowered with a gin pole and winch. No climbing required for maintenance — tilt down, service, raise again. More practical for owner-maintained systems. Require anchor points for 4–6 guy wires. Brands: Rohn 25G with tilt-up kit, Wincharger tilt-up.

**Tower height**: Minimum 30 feet above any obstacle within 500 feet (the "10/500 rule"). Taller is almost always better — every 10 feet of additional height increases energy production by 5–15% on a typical site.

### 7.4 Seasonal and Solar Complementarity

In many US locations, wind is inversely correlated with solar. The Pacific Northwest has strong fall/winter winds when solar is weakest. The Great Plains have spring wind surges. The Southeast has summer doldrums in both sun and wind.

Before adding wind to a solar system, get monthly average wind speed data for your site (from nearby weather stations at minimum; ideally from your own anemometer). Plot wind power against solar power by month. If the two curves are complementary (wind high when solar low), the combination reduces battery bank size required. If they track together (both low in winter), wind adds less value.

---

## 8. System Integration

### 8.1 Architecture Options

**DC-coupled (most common for off-grid)**:
All generation sources (solar, wind, hydro) feed into the DC battery bus via charge controllers. The inverter draws from the battery bus to produce AC. Generator charges batteries through the inverter-charger.

Advantages: Simple, robust, efficient for small-to-medium systems; single battery bank; works with all source types.

Disadvantage: All solar power passes through the charge controller and battery, even if going immediately to loads (adds ~5% loss).

**AC-coupled (for larger systems or grid-tie hybrid)**:
A grid-tie inverter (string inverter) converts solar/wind to AC and feeds it to the AC bus directly. A separate battery inverter manages the battery bank. AC coupling allows higher solar input voltage and simpler expansion.

Used in SMA Sunny Island + SMA Sunny Boy combinations; Victron MultiPlus + Fronius Primo; OutBack FX + Grid-tied inverter.

**Hybrid inverters (all-in-one)**:
Single unit handles solar MPPT input, battery management, AC output, and grid/generator connection. Simplest installation. Examples: Sol-Ark 12K/15K (popular, US-assembled), EG4 18kPV, Growatt SPH, Deye, Sungold.

For new builds under 15 kW AC output: **hybrid inverter** architecture is the simplest and increasingly the most cost-effective path. Sol-Ark 12K at ~$2,200 includes 2× MPPT inputs (each to 6,000W), 12,000W continuous output, and battery charger.

### 8.2 Generator Integration

When a generator runs in an off-grid system:
1. Generator connects to the AC input of the inverter-charger (or hybrid inverter)
2. Inverter-charger passes power through to loads AND charges batteries simultaneously
3. When batteries reach set charge level or time limit expires, inverter auto-disconnects from generator (auto-start systems can shut down generator automatically)

**Generator sizing for charging**: The inverter-charger's maximum AC input (charge amps × battery voltage) determines how fast the generator can charge batteries. A 5,000W charger at 48V = 104A charge current. Your generator should be rated at least 20% above the charger draw + any pass-through loads.

Rule: Generator kW ≥ (Inverter charger watts / 0.85) + maximum simultaneous load watts.

### 8.3 Monitoring Systems

Do not operate a serious off-grid system without monitoring. You need to know state of charge, power flow, and any fault conditions.

**Victron Energy / VRM ecosystem**: The industry standard for off-grid monitoring. Cerbo GX or Color Control GX hub connects to all Victron devices via VE.Can or VE.Direct and provides:
- Real-time system overview (battery SoC, solar watts, load watts, generator status)
- Historical data logging
- Remote access via VRM portal (app or browser) from anywhere
- Firmware updates OTA
- Configurable alerts (low SoC, high temperature, etc.)

Cerbo GX: ~$180. GX Touch 70 display: ~$150. VRM cloud logging is free.

**SMA Sunny Island + Sunny Portal**: Alternative for AC-coupled systems; robust but less flexible than Victron.

**EG4 / Sol-Ark apps**: Cloud monitoring included with hybrid inverters; improving but not yet as mature as Victron VRM.

**Standalone battery monitors** (if you lack a full monitoring system):
- Victron BMV-712: $90; Bluetooth, 500A shunt, accurate SoC calculation; essential
- Victron SmartShunt: $80; same capability, no display (uses Bluetooth app)
- Renogy 500A Battery Monitor: $50; adequate for basic monitoring

---

## 9. Wiring and Safety

### 9.1 Wire Sizing

Wire must be sized for both **ampacity** (thermal limit) and **voltage drop** (performance limit). In off-grid DC systems, voltage drop is often the binding constraint because wire runs can be long and DC current is high.

**3% voltage drop limit**: For most DC power runs, keep voltage drop below 3%. For critical battery interconnects and main DC bus runs, use 1–2% maximum.

**Voltage drop formula:**

```
Wire gauge needed (approximate):
VD = (2 × L × I × Resistance per foot) / Voltage
```

Or use a wire sizing calculator (available at Victron's website, or Remesys.com/calculators).

**Common DC wire sizing table (12 AWG to 4/0, copper, 48V system)**:

| AWG | Ampacity (60°C insulation) | Approx resistance (Ω/1000 ft) | Max run at 100A, <3% VD (48V) |
|---|---|---|---|
| 12 AWG | 20 A | 1.588 | 9 ft |
| 10 AWG | 30 A | 0.999 | 14 ft |
| 8 AWG | 50 A | 0.628 | 23 ft |
| 6 AWG | 65 A | 0.395 | 36 ft |
| 4 AWG | 85 A | 0.249 | 57 ft |
| 2 AWG | 115 A | 0.156 | 91 ft |
| 1/0 AWG | 150 A | 0.098 | 146 ft |
| 2/0 AWG | 175 A | 0.078 | 184 ft |
| 4/0 AWG | 230 A | 0.049 | 293 ft |

Battery-to-inverter connections are the highest current runs in the system. A 5,000W inverter on a 48V bank draws ~115A at full load and can surge to 300+A. Use 2/0 to 4/0 AWG and keep this run as short as possible (under 6 feet ideally).

### 9.2 Fusing

Every conductor leaving the battery bank must be fused before the first connection, as close to the battery terminal as physically possible.

**Fuse types for DC systems**:
- **Class T fuses** (Ferraz Shawmut, Eaton Bussmann): Fast-blow, rated for DC applications up to 48V+. Available in 100A–600A. The correct choice for battery-to-inverter and battery-to-busbar runs. Expensive ($15–$60 per fuse) but critical for protection.
- **MIDI fuses** (58V DC rated): Mid-size fuses for 30–200A branch circuits; widely used in Victron systems.
- **Automotive blade fuses (ATC/ATO)**: For small DC branch circuits under 30A only.
- **DC breakers**: Can replace fuses for branch circuits where reset without replacement is desired. Must be specifically rated for DC voltage — AC breakers are not interchangeable.

**Never use**: AC-rated circuit breakers in DC applications (they cannot interrupt DC arc), glass tube fuses for anything over 15A, automotive blade fuses above their rated ampacity.

### 9.3 Grounding

**System grounding** (negative grounding) in off-grid DC systems:
- The negative bus of the battery bank is the system common reference
- The negative bus connects to earth ground at one point (the grounding electrode — a ground rod, ground plate, or concrete-encased electrode)
- Ground the system at one point only — multiple ground bonds can create ground loops and corrosion in DC systems

**Equipment grounding** (chassis/safety):
- Metal enclosures of all electrical equipment connect to the equipment grounding conductor (green or bare wire)
- Equipment ground runs back to the main grounding electrode

**PV array grounding**: NEC 690.47 requires the PV array mounting structure to be grounded. This protects against lightning and fault currents. All metal racking is bonded together and tied to the grounding electrode.

**Negative grounding vs. positive grounding**: Virtually all modern off-grid systems use negative-ground (negative battery terminal to earth). Never mix — connecting a negative-ground system to a positive-ground device creates a dead short.

### 9.4 Lightning Protection

Lightning is a primary cause of off-grid system damage. A ground-mounted or rooftop PV array is a significant lightning target.

**Lightning protection measures**:
1. Lightning rod(s) at array perimeter, bonded to ground through 6 AWG copper down conductor to a ground rod
2. Surge protection devices (SPDs) at array combiner box (DC side): Midnite Solar MNSPD, Victron Smart Protector, or dedicated DC SPD rated for your system voltage
3. Surge protection on AC output (common residential SPD, $30–$80)
4. Ground all array racking to a low-impedance earth ground (ground rod every 100 feet of array run, bonded together)
5. Ferrite chokes on data cables entering the monitoring equipment
6. Short wire runs — long wires collect more induced voltage from a nearby strike

Note: Lightning protection reduces risk; it cannot eliminate it. A direct strike to the array will likely damage or destroy equipment regardless. Consider keeping backup charge controllers and critical components in a Faraday-protected enclosure (see Section 11).

### 9.5 Conduit and Enclosures

**Outdoor PV wiring (array to combiner box)**: USE-2 or PV wire in conduit, or listed PV cable with UV-rated jacket, rated for the environment. Liquid-tight conduit fittings at any entry that may contact water.

**Indoor DC wiring (combiner to charge controller, batteries, inverter)**: THHN or THWN in conduit preferred; flexible PV wire acceptable in dry locations. Metallic conduit (EMT or rigid) provides both physical protection and an additional ground path.

**Enclosures**: IP65 or NEMA 4 rated for outdoor combiner boxes. NEMA 1 acceptable for interior dry locations. All unused knockouts sealed.

**Minimum wire fill**: Follow NEC Table 1 for conduit fill — do not exceed 40% fill for three or more conductors.

---

## 10. Cost Tables

### 10.1 Component Costs (2025 retail/DIY pricing)

These are realistic prices as of early 2025 for DIY purchase in the US. Installed prices from a contractor are typically 1.5–2.5× higher.

**Solar panels (retail):**

| Panel type | Size | Cost range | $/W |
|---|---|---|---|
| 400W monocrystalline, Tier 1 | 400 W | $100–$160 | $0.25–$0.40 |
| 500W monocrystalline, Tier 1 | 500 W | $120–$200 | $0.24–$0.40 |
| 400W bifacial, Tier 1 | 400 W | $130–$200 | $0.33–$0.50 |
| Flexible CIGS, 100W | 100 W | $100–$180 | $1.00–$1.80 |

**MPPT charge controllers:**

| Model | Amps | Voltage | Price |
|---|---|---|---|
| Victron SmartSolar 100/30 | 30 A | 100V max | $110 |
| Victron SmartSolar 150/60 | 60 A | 150V max | $280 |
| Victron SmartSolar 150/100 | 100 A | 150V max | $450 |
| Victron SmartSolar 250/100 | 100 A | 250V max | $600 |
| Midnite Solar Classic 150 | 96 A | 150V max | $520 |
| Renogy Rover 40A | 40 A | 100V max | $130 |

**Inverter-chargers:**

| Model | Continuous watts | Battery voltage | Price |
|---|---|---|---|
| Victron MultiPlus-II 24/3000 | 3,000 W | 24V | $800 |
| Victron MultiPlus-II 48/5000 | 5,000 W | 48V | $1,200 |
| Victron MultiPlus-II 48/10000 | 10,000 W | 48V | $2,400 |
| Sol-Ark 12K | 12,000 W | 48V | $2,200 |
| EG4 18kPV | 18,000 W | 48V | $3,000 |
| Schneider XW+ 6848 | 6,800 W | 48V | $2,500 |

**Batteries (LiFePO4, retail):**

| Product | Capacity | Nominal voltage | Usable energy | Price | $/kWh |
|---|---|---|---|---|---|
| Ampere Time 200Ah | 200 Ah | 48V | 9.6 kWh | $1,100–$1,400 | $115–$145 |
| SOK 200Ah | 200 Ah | 48V | 9.6 kWh | $1,500–$1,800 | $155–$188 |
| Epoch 200Ah | 200 Ah | 48V | 9.6 kWh | $2,200–$2,600 | $229–$271 |
| Pylontech US5000 | 4.8 kWh | 48V | 4.32 kWh | $1,400–$1,700 | $325–$395 |
| Victron LiFePO4 200Ah | 200 Ah | 25.6V | 5.12 kWh | $1,700–$2,000 | $332–$391 |

### 10.2 Complete System Cost Estimates (DIY, 2025)

These are material costs only. Add 15–20% for connectors, wire, conduit, fuses, mounting hardware, and small parts.

**1 kW system (tiny cabin, basic needs):**

| Component | Spec | Cost |
|---|---|---|
| Panels | 2× 500W mono = 1,000W | $300–$400 |
| MPPT controller | Victron 100/30 | $110 |
| Inverter-charger | Victron MultiPlus 24/3000 | $800 |
| Battery bank | 2× 100Ah 24V LiFePO4 (5.1 kWh) | $600–$900 |
| Mounting, wiring, fuses, misc | — | $300–$500 |
| **Total DIY materials** | | **$2,110–$2,710** |

Daily capacity: ~5 kWh storage, ~3–4 kWh/day solar input (4 PSH). Suitable for: 2–4 LED circuits, laptop, phone charging, small 12V fridge.

**5 kW system (small homestead, moderate comfort):**

| Component | Spec | Cost |
|---|---|---|
| Panels | 10× 500W mono = 5,000W | $1,500–$2,000 |
| MPPT controller | Victron 150/100 | $450 |
| Inverter-charger | Victron MultiPlus-II 48/5000 | $1,200 |
| Battery bank | 3× 200Ah 48V LiFePO4 (28.8 kWh) | $3,300–$5,400 |
| Cerbo GX monitor | — | $180 |
| Mounting, wiring, combiner, misc | — | $800–$1,200 |
| **Total DIY materials** | | **$7,430–$10,430** |

Daily capacity: ~23 kWh storage, ~15–20 kWh/day solar input (4 PSH). Suitable for: full household lighting, refrigeration, freezer, communications, water pump, washing machine, power tools (periodic).

**10 kW system (established homestead, comfortable):**

| Component | Spec | Cost |
|---|---|---|
| Panels | 20× 500W mono = 10,000W | $3,000–$4,000 |
| MPPT controllers | 2× Victron 250/100 | $1,200 |
| Inverter-charger | Sol-Ark 12K or Victron Quattro 48/10000 | $2,200–$2,800 |
| Battery bank | 6× 200Ah 48V LiFePO4 (57.6 kWh) | $6,600–$10,800 |
| Generator (propane, 7.5 kW) | Champion dual-fuel | $900–$1,200 |
| Cerbo GX + display | — | $330 |
| Racking, wiring, BOS | — | $1,500–$2,500 |
| **Total DIY materials** | | **$15,730–$22,630** |

Daily capacity: ~46 kWh storage, ~30–40 kWh/day solar input. Can support: all household loads, light workshop, electric well pump, seasonal mini-split.

**20 kW system (large homestead / small farm):**

| Component | Spec | Cost |
|---|---|---|
| Panels | 40× 500W mono = 20,000W | $6,000–$8,000 |
| MPPT controllers | 4× Victron 250/100 or 2× Victron 250/200 | $2,400–$3,600 |
| Inverter-chargers | 2× Sol-Ark 12K or EG4 18kPV | $4,400–$6,000 |
| Battery bank | 12× 200Ah 48V LiFePO4 (115 kWh) | $13,200–$21,600 |
| Generator (diesel, 15 kW) | Kubota or Yanmar | $4,000–$8,000 |
| Monitoring + transfer switch | — | $800–$1,200 |
| Racking, wiring, BOS, conduit | — | $3,000–$5,000 |
| **Total DIY materials** | | **$33,800–$53,400** |

Supports: full farm operations, large workshop, EV charging, multiple dwellings.

---

## 11. Emergency and Nuclear Scenarios

### 11.1 What an EMP Actually Threatens

An electromagnetic pulse (EMP) from a nuclear detonation or a coronal mass ejection (CME) can damage electronic equipment through induced voltage spikes on conductive paths. Understanding the threat model helps prioritize protection:

**High risk** (long conductors acting as antennas):
- Grid-tied inverters and charge controllers connected to long wire runs
- Exposed solar arrays with long cable runs to electronics
- Smart meters, grid-connected equipment
- Unshielded electronics near long wire runs

**Moderate risk** (internal circuits, short connections):
- Off-grid inverters and charge controllers
- Battery management systems
- Communications equipment (radios, routers)
- Vehicle electronics

**Lower risk** (passive, no circuitry):
- Solar panels themselves (no active circuitry — the cells are passive semiconductor junctions; large panels are essentially immune to EMP)
- Battery banks (passive electrochemical storage — an EMP will not damage batteries)
- Wiring and physical infrastructure
- Manual/mechanical equipment

The critical insight: **panels and batteries survive an EMP**. The vulnerable components are the electronic controllers — MPPT charge controllers, inverters, BMS units. Protecting these electronics allows the system to be restored.

### 11.2 Faraday Protection for Spares

The practical EMP hardening strategy for a homestead is not to harden the running system (prohibitively expensive and complex) but to protect **spare electronics** in Faraday containers.

**What to protect**:
- 1× complete spare MPPT charge controller
- 1× spare inverter (a smaller modified sine wave unit is acceptable as emergency backup — e.g., 2,000W pure sine for $200)
- Spare BMS unit(s) for battery bank
- Handheld ham radios (Baofeng UV-5R, $25 each — keep 2–3 in Faraday)
- Spare Raspberry Pi or small computer for monitoring
- LED headlamps and flashlights (batteries removed)
- Charge controller and inverter manuals (paper copies too)

**DIY Faraday enclosure**:
1. Metal garbage can with tight-fitting metal lid ($25–$50 at hardware store)
2. Line the inside with cardboard or foam to prevent direct contact between electronics and metal
3. Seal the lid with metallic tape (copper or aluminum foil tape, $10)
4. Ground the can to earth (optional; reduces E3 component risk from geomagnetic storms)

Test your Faraday enclosure: place an FM radio inside with a station playing. If you can still hear the station clearly through the lid, it's not shielded. An effective Faraday cage will silence the radio completely.

**Commercial Faraday options**:
- Mission Darkness Eclipse Faraday bags: tested to MIL-STD-188-125 and IEEE 299-2006; available in sizes from phone to solar panel; $40–$200
- Sol-Ark inverters: marketed as EMP-hardened; Faraday cage design integrated into construction; ~$2,000–$3,000 premium over non-hardened equivalents

### 11.3 Manual and Non-Electronic Backup Systems

If all electronics fail and spares are not available, a homestead needs to maintain minimum function:

**Water**: Hand pump on the well (Bison, Simple Pump) operates with zero electricity. Gravity-fed spring or cistern system. Mechanical ram pump where elevation exists. See Domain 3 for full specification.

**Lighting**: Oil lamps (kerosene or vegetable oil, $15–$40 per lamp), candles, battery-powered LED with hand-crank rechargeable batteries, solar garden lights (extremely simple circuits, EMP-resistant due to low power and very short wire runs).

**Refrigeration without power**: Root cellar at 32–40°F (passive). Zeer pot evaporative cooler (clay pot within clay pot with wet sand — reduces temperature 20–40°F below ambient in dry climates). Spring house (water running over or around storage — traditional 40–50°F passive cooling). Ice house / ice cutting from ponds in winter with insulated sawdust storage.

**Communication**: Battery-powered or hand-crank AM/FM/NOAA weather radio (simple circuitry, usually survives EMP if unplugged). Paper maps and pre-arranged meeting schedules with neighbors. Optical signaling (mirror, colored panels). See Domain 11 for full communications stack.

**Cooking**: Wood stove, rocket stove, propane camp stove. No electronics required.

**Food preservation**: Salt curing, smoking, root cellar, lacto-fermentation — all zero-electricity methods. See Domain 5.

### 11.4 Staged Recovery Plan

Plan for staged power restoration after a grid-down or EMP event:

**Day 1–3 (manual fallback)**:
- Hand pump for water
- Oil lamps for light
- Propane or wood for cooking and heat
- Battery radio for information

**Day 3–7 (partial electronics)**:
- Retrieve spare charge controller and inverter from Faraday enclosure
- Reconnect solar array (panels likely undamaged)
- Connect to battery bank (undamaged)
- Restore basic power: refrigeration, communications charging, LED lighting
- Assess generator status and fuel supply

**Week 2+ (full system assessment)**:
- Test all equipment systematically
- Source replacement components as available (ham radio networks for sourcing information)
- Prioritize: refrigeration, water pump, communications, in that order

### 11.5 Nuclear Fallout and Energy Systems

After a nuclear detonation, the primary concern in the first 2 weeks is radiation shielding (see Domain 15). Energy considerations during shelter period:

- Pre-positioned battery bank in shelter provides power for lighting, communications, medical equipment during the 2-week shelter-in-place
- Minimum recommended: 5–10 kWh of battery capacity in or adjacent to the shelter
- Do not run the generator during active fallout (exhaust requires opening shelter ventilation)
- Solar panels can be used cautiously after day 3–4 when outdoor exposure limits are more manageable; keep wire runs short and sealed through shelter wall penetrations
- The primary energy concern during a shelter period is communications power (radio) and refrigeration for any medications requiring cold storage

**Pre-positioned shelter power kit**:
- 2× 200Ah 12V LiFePO4 batteries (4.8 kWh) in shelter ($600–$900)
- 1× 400W panel near shelter with short wire run through conduit penetration
- 1× 40A MPPT controller (in Faraday bag, retrieve when shelter period ends)
- 12V LED lighting, 12V USB charger, 12V radio
- 1× hand-crank generator (Kaito, Goal Zero Nomad) as final fallback

---

## Sourcing Reference

**Solar panels**: Wholesale Solar (wholesalesolar.com), AM Solar, GoGreenSolar, Renogy (Amazon), local solar distributors — call and ask for contractor pricing even as a DIYer.

**Victron equipment**: Victron dealer network (find via victronenergy.com dealer locator); altE Store; Northern Arizona Wind & Sun (NAWS — excellent technical support); Signaturesolar.com.

**LiFePO4 batteries**: Battlebornbatteries.com (premium, US warranty support); epochbatteries.com; SOK via Amazon; direct from China via Alibaba for large orders (minimum 500 Ah for shipping economy).

**Wire and conduit**: Home Depot/Lowes for small quantities; Wire & Cable (wireandcable.com), Waytek Wire for bulk.

**Micro-hydro**: Energy Systems & Design (microhydropower.net — Canadian, ships to US); Canyon Hydro (canyonhydro.com); Teco-Westinghouse (for larger systems).

**Small wind turbines**: Bergey Windpower (bergey.com — US-made, best support); Primus Wind Power (primuswind.com); compare annual kWh estimates, not rated watts.

**Technical references**:
- Victron Energy installation manuals (free PDF, comprehensive): victronenergy.com/support
- NEC Article 690 (PV systems) and 706 (energy storage): NFPA 70
- NREL PVWatts Calculator: pvwatts.nrel.gov
- Richland Creek Energy (micro-hydro): richlandcreekenergy.com/resources

---

## Cross-Domain Links

- **Domain 3 (Water)**: Solar-powered well pump sizing; pressure tank selection; 12V DC pump compatibility
- **Domain 7 (Heating & Cooling)**: Mini-split sizing and solar compatibility; propane load reduction strategy
- **Domain 11 (Communications)**: Ham radio power requirements; Starlink power budget; 12V DC radio operation
- **Domain 15 (Disaster Scenarios)**: Nuclear shelter power kit; EMP response; fallout period energy management
- **Domain 10 (Tools & Fabrication)**: Generator-powered welding; workshop load calculations
