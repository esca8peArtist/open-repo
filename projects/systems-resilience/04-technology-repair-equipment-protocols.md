---
title: "Technology Repair and Maintenance — Equipment Protocols"
phase: 4a
status: complete
word_count: ~8900
audience: "Project lead (Anya) — community scale, 50–150 people, Midwest Zone 5"
created: 2026-05-17
cross_references:
  - individual/04-energy.md
  - individual/01-water.md
  - household/04-energy-coordination.md
  - household/02-water-coordination.md
  - community/02-infrastructure-interdependency.md
  - 04-technology-repair-community-infrastructure.md
---

# Technology Repair and Maintenance — Equipment Protocols

> **Region**: Midwest US (Zone 5) | **Scale**: 50–150 people
> **Phase**: 4a — Specific maintenance procedures for critical community equipment
> **Cross-references**: [04-technology-repair-community-infrastructure.md](04-technology-repair-community-infrastructure.md) · [individual/04-energy.md](individual/04-energy.md) · [individual/01-water.md](individual/01-water.md) · [community/02-infrastructure-interdependency.md](community/02-infrastructure-interdependency.md)

---

## How to Use This Document

This document provides specific, actionable maintenance procedures for each major equipment category. It is intended to be used by the 2–3 people per category who have been trained as described in [04-technology-repair-community-infrastructure.md](04-technology-repair-community-infrastructure.md). The procedures are organized by equipment type, not by timeline, so you can navigate directly to the system you are working on.

For each equipment category: read the annual schedule first, then read the detailed procedures for the work you are about to do. Cross-reference the equipment's own service manual (printed copy should be in the community shop reference library) for model-specific torque specifications, part numbers, and wiring diagrams.

**Zone 5 Midwest calendar anchor points** referenced throughout this document:
- **October inspection**: pre-winter; address freeze protection, winterize outdoor equipment
- **April inspection**: post-winter; recommission systems, address any winter damage
- **July/August pre-harvest**: full inspection of harvest-critical equipment before peak load season

---

## Section 1: Solar Power System Maintenance

Solar power systems are among the most maintenance-sparse pieces of equipment in a community's inventory — but when maintenance is neglected, the consequences are expensive and slow to manifest. A battery bank destroyed by overcharging or sulfation costs $500–$3,000+ to replace. A dirty panel array silently loses 25–50% of its output. The goal of this section is to prevent expensive failures through cheap routine care.

See [individual/04-energy.md](individual/04-energy.md) for system sizing, load management, and the Zone 5 solar reality (2.5–6.5 peak sun hours per day by season).

### Annual Maintenance Schedule

| Task | Frequency | Season | Time required |
|---|---|---|---|
| Panel cleaning | Every 3–6 months | After harvest (Oct) and before summer (Apr) | 30 min per 4 panels |
| Visual panel inspection | Monthly | Ongoing | 10 min |
| Battery specific gravity (flooded LA) | Quarterly | Jan, Apr, Jul, Oct | 20 min per battery bank |
| Battery equalization (flooded LA only) | Annually | Spring (April) | 2–4 hours |
| Battery water top-off (flooded LA) | Monthly in summer, every 6 weeks in winter | Ongoing | 10 min |
| Battery terminal cleaning and tightening | Annually | October | 30 min |
| Charge controller inspection | Semi-annually | April and October | 30 min |
| Inverter inspection | Annually | October | 45 min |
| Wiring inspection (connections, corrosion) | Annually | October | 60 min |
| System output test (record and compare) | Quarterly | Jan, Apr, Jul, Oct | 30 min |

### Panel Cleaning Procedure

Dust accumulation reduces solar output by 15–25% under normal conditions; in higher-dust environments (near gravel roads, harvested fields), reduction can reach 40–50% [1]. For a Zone 5 Midwest installation, the highest dust periods are July–October (field operations, dry summers). Clean panels at minimum in October (post-harvest) and April (pre-summer).

**Procedure:**
1. Work on cloudy days or early morning (panels are cool; thermal shock from cold water on hot glass can stress cell adhesive)
2. Use a soft brush or soft sponge — never abrasive pads or metal tools
3. Plain water is sufficient; if panels are heavily soiled, mild dish soap solution is acceptable; avoid harsh chemicals (strip anti-reflective coating)
4. Rinse from top to bottom; don't push water under panel frames (pooling water causes corrosion)
5. Inspect while cleaning: look for cracked glass, delamination (bubbles between layers), discoloration (brownish patches indicate hot spots from cell damage), damaged frames, loose mounting hardware
6. For roof-mounted panels: use a soft brush with extension pole from the ground if possible; if you must go on the roof, wear a harness and have a second person present
7. Ground-mounted panels: clean from the ground easily; check mounting posts for rust and anchor integrity annually

**What to look for during inspection:**
- Cracked glass: a crack allows moisture ingress and eventual cell failure; a cracked panel should be isolated (disconnected) and replaced when possible, but can continue generating at reduced output short-term
- Hot spots: dark brownish spots visible in direct sun indicate cell damage, often from partial shading or physical damage; a panel with multiple hot spots will drag down an entire string
- Delamination: bubbling or yellowing of the encapsulant layer reduces output and eventually causes failure; a fully delaminated panel must be replaced
- Loose MC4 connectors: check that all cable connections are fully seated; a partially connected MC4 connector will arc and fail

### Battery Maintenance — Flooded Lead-Acid

Flooded lead-acid (FLA) batteries are the most common battery type for off-grid systems where cost is the primary constraint and maintenance capability exists. They are also the most demanding of the three battery types (FLA, AGM, lithium). Treat them correctly and they last 3–5 years; neglect them and they die in 18 months.

**Monthly: Water top-off**
1. Check water level monthly (more often in summer when electrolyte evaporates faster)
2. Wear eye protection and gloves — battery acid causes chemical burns
3. Cells should be filled to just below the bottom of the fill tube (visible when you remove the cap); never above
4. Use only distilled water; tap water contains minerals that contaminate electrolyte and accelerate plate sulfation
5. Do not top off before charging — water level rises as the battery charges; fill after a full charge to avoid overflow

**Quarterly: Specific gravity testing**
Specific gravity measures how fully charged a flooded battery cell is by measuring the density of the electrolyte [2].

Equipment needed: battery hydrometer (must be in community tool library)

| Specific gravity reading | State of charge |
|---|---|
| 1.265–1.280 | Fully charged |
| 1.210–1.240 | 75% charged |
| 1.155–1.190 | 50% charged |
| 1.100–1.130 | 25% charged |
| Below 1.100 | Discharged (risk of sulfation damage) |

Temperature correction: at below 70°F (21°C), add 0.004 to the reading for every 10°F below 70°F. At above 70°F, subtract 0.004 per 10°F.

**Interpreting readings:**
- All cells within 0.030 specific gravity of each other: healthy battery
- One cell more than 0.050 lower than the others: that cell is failing; the battery will need replacement within 1–2 cycles
- All cells low and won't come up with charging: battery is sulfated; equalization may help (see below)

**Annual: Equalization**
Equalization is a controlled overcharge that mixes the stratified electrolyte and breaks down sulfate crystals on the battery plates. Do this once per year, in spring (April), after the battery has been at a full charge.

Warning: Never equalize AGM or gel batteries. The high voltage will ruin them. Equalization is for flooded lead-acid only [3].

1. Verify the battery is at or near full charge before starting
2. Set the charge controller to equalization mode (consult your controller's manual — this is model-specific)
3. Target voltage: 15.0–15.5V for a 12V bank; equalization typically runs for 1–3 hours
4. Monitor: the battery will gas (hydrogen venting); this is normal. Ensure ventilation in the battery enclosure. Do not allow sparks or open flame near venting batteries.
5. Check specific gravity during equalization; stop when all cells read within 0.010 of each other or after 3 hours, whichever comes first
6. After equalization, allow the charge controller to return to float charge

**Battery replacement intervals:**
- Flooded lead-acid, well maintained: 3–5 years
- Flooded lead-acid, poorly maintained (deep discharges, no equalization, improper watering): 18–24 months
- AGM: 4–7 years (no maintenance required beyond keeping connections clean and monitoring voltage)
- Lithium (LiFePO4): 10–15 years at 80% capacity; no routine maintenance but requires a battery management system (BMS)

**Signs a battery bank needs replacement:**
- Capacity has dropped to less than 70% of original (you get much less runtime per charge cycle)
- Individual cells reading dramatically different specific gravity despite equalization
- Physical damage: cracked case, corrosion on terminals that returns immediately after cleaning, bulging sides
- Consistent sulfation that does not respond to equalization

### Charge Controller Diagnostics and Failure Modes

The charge controller is the brain of the solar system — it regulates current from panels into batteries and protects against overcharge. Most modern controllers display error codes or indicator light patterns when a fault occurs.

**Common fault codes and field responses (MPPT controllers):**

Most manufacturers use similar code structures [4][5]:

| Fault type | Display | Likely cause | Field response |
|---|---|---|---|
| Over-temperature | High temp symbol or E01 | Controller in enclosed/unventilated space | Move to ventilated location; clean heat sink fins |
| Battery over-voltage | OVP or E02 | Battery bank voltage exceeds controller limit | Check battery connections; verify bank voltage matches controller setting |
| PV over-voltage | PV OVP or E04 | Panel array voltage exceeds controller input limit | Too many panels in series; reconfigure to parallel; check for shading reversal |
| Battery under-voltage | UVP | Severely depleted battery | Charge from alternate source; check for load fault |
| Short circuit | E03 | Wiring fault or failed component | Inspect all connections; check for corroded or damaged wire |
| Communication error | Comm Err | Controller cannot read BMS or display unit | Check data cable connections; restart controller |

**Field inspection procedure (semi-annual, April and October):**
1. Inspect the charge controller's heat sink — clean dust and debris with compressed air or soft brush; dust insulates and causes overheating
2. Check all terminal connections: pull gently on each wire; any movement means the terminal is loose; re-torque to manufacturer spec
3. Inspect wiring insulation for rodent damage (a significant risk in rural Midwest — mice nest in electrical enclosures)
4. Check the display or indicator LEDs: all should be within normal operating parameters during a sunny period
5. Record the bulk, absorption, and float voltage readings in the logbook — compare to previous readings; drift outside of 0.2V indicates calibration drift or battery condition change
6. Clean the exterior; inspect the enclosure for moisture ingress

**Failure mode analysis:**
The most common charge controller failures in order of frequency:
1. Overtemperature shutdown (poor ventilation) — resolve by improving ventilation
2. Rodent-chewed wiring — resolve by physical exclusion and inspection
3. Lightning damage — partially preventable with surge arrestors at the PV input; if the controller dies after a storm, the surge arrestor likely sacrificed itself (check it first)
4. Capacitor failure after 5–10 years — symptoms: erratic charging voltage, controller resets unexpectedly; board-level repair requires a trained electronics technician; replacement is often more practical

### Inverter Inspection

Inverters convert DC battery power to AC current for appliances. They are generally more reliable than charge controllers over short timeframes but have specific failure modes over the 5–10 year horizon.

**Annual inspection (October):**
1. Power off the inverter (DC input breaker off, then AC output off)
2. Inspect the heat sink fins — clean dust buildup with compressed air
3. Inspect cooling fan: spin the fan blade manually; it should turn freely. A fan that doesn't spin freely will cause thermal shutdown under load.
4. Check all DC input terminals and AC output connections for tightness and corrosion
5. Inspect the DC input wiring for wear, rodent damage, or heat marks (heat marks indicate a loose connection that has been arcing)
6. Power the inverter back on and check display for fault codes; run a load test (connect a known load and measure output with a multimeter)

**Common inverter faults:**
- Low battery voltage: inverter shuts off below a set threshold (typically 10.5–11V for a 12V system); check battery state
- Overload: too many loads simultaneously; shed loads, reset inverter
- Over-temperature: improve ventilation; check cooling fan
- Ground fault: check AC wiring for neutral-ground short
- Failed transfer relay (for inverter-chargers): symptoms include no battery charging from AC input; relay replacement requires technician

---

## Section 2: Well Pump and Water System Maintenance

Water system failure is the most immediately life-threatening equipment failure in a community. A community of 50–150 people needs a minimum of 100–300 gallons per day just for drinking and cooking; with sanitation and basic agriculture, that rises to 500–1,500 gallons per day. See [individual/01-water.md](individual/01-water.md) and [household/02-water-coordination.md](household/02-water-coordination.md) for system sizing and storage protocols.

### Annual Maintenance Schedule

| Task | Frequency | Season | Time required |
|---|---|---|---|
| Hand pump inspection | Annually | April | 1 hour |
| Hand pump leathercup check | Annually; replace at 3–5 years or when pumping effort increases | April | 2 hours to replace |
| Pressure tank air charge check | Annually | April | 30 min |
| Pressure tank knock test (bladder check) | Semi-annually | April, October | 10 min |
| Submersible pump performance check (flow rate) | Annually | July | 30 min |
| Water storage tank inspection | Annually | October | 1 hour |
| Well cap and casing inspection | Annually | April | 30 min |
| Pressure switch contacts inspection | Annually | April | 20 min |
| Winterization of above-ground components | Annually | October | 1–2 hours |

### Hand Pump Maintenance (Simple Pump and Pitcher Pump types)

Hand pumps are the critical backup when the electric submersible fails. For Phase 1–3 communities, a hand pump (Simple Pump, Bison Pump, or similar) installed alongside the submersible pump is the water security baseline. Maintenance is minimal but must be done.

**Annual inspection (April):**
1. Pump 20 strokes; note pumping effort (baseline this in the first year — effort increases as leathercup wears)
2. Check for water leakage at the pump cylinder (the barrel below the handle pivot point); leakage here indicates leathercup wear
3. Inspect the pump rod for straightness (bent rods cause eccentric wear on the cylinder); a visible bend requires rod replacement
4. Inspect the pump handle pivot bolt and linkage for wear; replace any hardware showing significant wear
5. Clean the pump exterior; inspect the pump head for cracks in cast iron or plastic components
6. Check the drop pipe connections (where visible above the wellcasing) for corrosion

**Leathercup replacement:**
The leathercup is the rubber or leather piston seal inside the pump cylinder that creates suction. It is the primary wear component on a hand pump [6].

- Replacement interval: 1–5 years depending on use. A pump used multiple times per day will need annual replacement; occasional-use pumps may last 3–5 years. Increased pumping effort or reduced flow is the primary indicator.
- Parts to have stocked: 6 leathercup seals per pump (3–5 year supply), O-rings for cylinder, valve washers
- Replacement procedure:
  1. Remove the pump handle and pump head from the well casing per the pump manufacturer's instructions
  2. Pull up the drop pipe and rod assembly (this is a 2-person task; use the community's come-along or hand-over-hand if the well is under 25 ft)
  3. Remove the cylinder from the bottom of the rod assembly
  4. Soak replacement leathercup(s) in water for 2 hours before installation — dry leather cracks under the stress of initial use
  5. Install new leathercup per manufacturer diagram; reassemble cylinder
  6. Re-lower the assembly; reinstall pump head and handle
  7. Prime and pump — note that new leathers may take 10–20 strokes to develop full suction
  8. Log the replacement date and parts used in the shop logbook

### Pressure Tank Maintenance and Bladder Diagnosis

The pressure tank is a steel vessel that holds water under air pressure, delivering it to the distribution system when the pump is off. It extends pump life by reducing short-cycling.

**How to check air pressure (with system off):**
1. Shut off power to the pump
2. Open a faucet or drain valve to relieve all pressure from the system
3. Use a standard tire pressure gauge on the Schrader valve at the top of the tank
4. Correct pre-charge pressure: 2 PSI below the pump cut-in pressure. For a 30/50 switch, that means 28 PSI. For a 40/60 switch, that means 38 PSI. [7]
5. If pressure is low, add air with a bicycle pump or compressor; if zero, the bladder has likely failed
6. If water comes out of the Schrader valve when you press the pin, the bladder has ruptured (water is in the air space)

**Bladder failure diagnosis — the knock test:**
1. Shut off power to the pump; do not drain the system
2. Knock firmly on the pressure tank, 4" from the top and again 4" from the bottom
3. Healthy tank: top sounds hollow (air), bottom sounds dull (water)
4. Waterlogged tank (bladder failed): both top and bottom sound the same — heavy and dull [7][8]

**Signs of pressure tank problems:**
- Rapid pump cycling: pump turns on and off every few seconds when a faucet is open — indicates waterlogged tank (no air cushion to maintain pressure)
- Pump runs constantly: could be pressure switch failure, a leak in the distribution system, or a failed check valve
- Fluctuating water pressure at fixtures: less dramatic than rapid cycling but indicates reduced air charge
- Rust in water: internal tank corrosion; replace the tank

**Bladder replacement:**
Some pressure tanks have replaceable bladders; others must be replaced as a complete unit. Check the tank model before purchasing replacement parts. Replacement is a straightforward plumbing task requiring: pipe wrench, Teflon tape, new tank (or bladder kit), and 2 hours. The most difficult part is draining the system completely before disconnecting the old tank.

### Electric Submersible Pump Failure Signs and Diagnosis

A submersible pump failure is a major event — pulling the pump requires equipment (cable puller or improvised block-and-tackle) and is a significant labor investment. The goal of this section is to diagnose the problem before pulling the pump, and to recognize the signs early enough to prepare.

**Signs of submersible pump problems (in order of urgency):**

| Sign | Likely problem | Response |
|---|---|---|
| No water at all | Complete pump failure, blown fuse, or no power | Check power first (breaker, fuses, pressure switch); if power is good, pump has failed |
| Breaker trips immediately | Motor winding short (pump seized) | Replace pump |
| Constant low pressure (not fluctuating) | Impeller wear or partial clog | Pull and inspect |
| Air spurting from faucets | Check valve failure allowing air into line | Check valve replacement (above ground if possible; may require pump pull) |
| Sand or grit in water | Sand infiltration from damaged well screen or pump drawing from bottom of well | Pull pump; inspect screen; raise pump setting |
| Pump cycles but pressure won't reach cut-off | Worn impellers, hole in drop pipe, or pressure switch stuck | Check pressure switch contacts; if ok, pull pump |
| Sudden loss of flow with good motor function | Clogged intake screen | Pull and clean |

**Before pulling the pump (field diagnostics):**
1. Verify power: check that the breaker hasn't tripped, voltage at the pump control box is correct (230V for most submersibles), and the pressure switch contacts are not corroded
2. Check the pressure switch: remove the cover (power off first), inspect the contacts for pitting or corrosion. Clean with fine sandpaper if mildly corroded.
3. Check the capacitor (in the control box): submersible pumps use a start capacitor; a failed capacitor prevents the motor from starting. Symptoms: breaker trips immediately or pump hums but doesn't run. Testing requires a multimeter with capacitance mode.
4. If all above checks out and the pump still doesn't work, it's time to pull the pump

**Pulling the pump — community task:**
This is not a solo task. You need at minimum 2–3 people.
1. Power off the pump at the breaker panel; lock out / tag out
2. Gather equipment: cable puller (or block-and-tackle), rope or safety cable, clean bucket, work gloves
3. Remove the well cap; the pump cable, drop pipe, and safety cable run down the casing
4. Attach a pulling strap to the drop pipe just below the well cap
5. Pull hand-over-hand or use the come-along; lower each section of pipe to the ground as you work up
6. Inspect the pump at ground level: check for sand/sediment in the intake, damage to the impeller (visible at the bottom of the pump), corrosion on the motor body
7. A clogged intake can be cleaned in the field with water; impeller damage and motor failure require replacement

### Water Storage Tank Inspection

**Annual inspection (October, before winter):**
1. Visually inspect the exterior for cracks, bulging, or UV degradation (visible as chalky surface on polyethylene tanks)
2. For tanks with inlet screens: remove and clean screens; replace any screens showing holes or significant corrosion
3. Inspect the outlet valve and any associated fittings for leaks and corrosion
4. Check liner integrity if using a tank with an inner bladder or liner
5. Inspect the overflow pipe to ensure it drains away from the tank foundation and building
6. For winterization: either drain and blow out the tank if it's in an unheated location, or ensure the tank building has adequate insulation to keep water above freezing (32°F / 0°C)

**Sediment management:**
Tanks accumulate sediment over time. Drain and flush tanks annually; a garden hose connected to the drain valve and directed to a safe disposal area makes this practical.

---

## Section 3: Generator Maintenance

Generators are the most maintenance-intensive piece of equipment in a community's inventory. A generator that hasn't been run in 6 months with old fuel in the carburetor will not start when you need it. The maintenance schedule below is designed to prevent the two most common failures: oil degradation and carburetor gum.

### Annual Maintenance Schedule

| Task | Frequency | Notes |
|---|---|---|
| Oil change | Every 100 hours of use; every 50 hours under heavy load; annually even if not used | Use the oil weight specified on the generator (typically SAE 10W-30) |
| First oil change (new generator) | After first 20–25 hours of use | Break-in oil contains metal particles |
| Air filter inspection | Every 50 hours or monthly | Clean or replace if dirty; a clogged filter causes rich running and accelerated wear |
| Spark plug inspection | Annually or every 100 hours | Gap should match spec (typically 0.028–0.035") |
| Spark plug replacement | Every 2 years or 200 hours | Cheap insurance; carry 2 spare plugs per generator |
| Fuel system inspection | Before each use after any storage period | Look for gum/varnish in fuel valve and carburetor |
| Carburetor cleaning | If generator won't start after storage, or runs rough | See procedure below |
| Load test | Monthly (run at 50–75% rated load for 30 minutes) | Prevents wet stacking (carbon buildup from light loading) |
| Battery (electric start) | Monthly voltage check | Keep above 12.4V; charge with trickle charger if stored |
| Voltage output check | Annually | Measure with multimeter at the outlet: 115–125V AC at no load |

### Oil Change Procedure

1. Run the generator for 5 minutes to warm the oil (warm oil drains faster and more completely)
2. Shut down; engage the fuel valve to off position
3. Locate the drain plug (usually underneath the engine; may require tilting the generator to one side)
4. Place a drain pan; remove the drain plug and allow oil to drain completely (3–5 minutes)
5. Remove the oil fill cap/dipstick
6. Replace the drain plug and torque finger-tight plus 1/4 turn (do not overtighten — the drain plug is in aluminum and strips easily)
7. Add fresh oil through the fill opening; use the grade specified on the generator (SAE 10W-30 for most portable generators; some specify 5W-30 for cold-weather operation)
8. Check the oil level with the dipstick; do not overfill (overfilling causes oil to blow out past seals and into the air filter)
9. Dispose of old oil appropriately: used motor oil is a significant soil contaminant; store in a sealed container for later disposal

**Oil quantity (typical portable generators):**
- 1,000–3,500W: 0.6–0.9 qt
- 3,500–7,500W: 0.9–1.5 qt
- 7,500–12,000W: 1.5–2.0 qt

### Carburetor Cleaning — The Critical Maintenance Task

The carburetor is the most common failure point in stored generators. Gasoline — especially ethanol blends (E10 or E15) — begins to degrade within 30 days of storage. Ethanol absorbs water from the air, and when fuel sits, lighter volatile fractions evaporate, leaving a varnish that coats and clogs carburetor passages [9][10].

**Prevention (far easier than cleaning):**
- Run the generator monthly, even for 30 minutes under load
- After each use, if the generator will be stored more than 30 days: run the engine with the fuel valve closed until it stops — this uses the fuel remaining in the carburetor, preventing varnish formation
- Alternatively, add a fuel stabilizer (STA-BIL Storage) to the tank: 1 oz per 2.5 gallons of fuel; run for 5 minutes to distribute through the system; treated gasoline remains usable for up to 24 months [11]
- Use ethanol-free premium fuel for long-term storage generators when available — it degrades far more slowly

**Sea Foam carburetor treatment (for a gummed carburetor that still runs):**
1. Add Sea Foam Motor Treatment to a low fuel tank at a high concentration: 1 part Sea Foam to 3–4 parts gasoline
2. Start the engine and allow it to idle for 8–10 minutes to circulate the Sea Foam through the carburetor
3. Shut the engine off and allow it to soak for several hours (overnight is best)
4. Restart and run at moderate load; the dissolved varnish will burn off (expect white smoke for a few minutes)
5. Drain the remaining Sea Foam mixture and refill with fresh fuel

**Full carburetor removal and cleaning (for a generator that won't start due to gum):**
This is a 1–2 hour task requiring: screwdrivers, a carb cleaner spray can, a small brush, a flat clean workspace, and the service manual with carburetor diagram.

1. Power off and allow the engine to cool; disconnect spark plug wire
2. Turn fuel valve to off; disconnect fuel line from carburetor (have a rag ready for fuel drips)
3. Remove the air filter housing (2–4 bolts or clips)
4. Remove the carburetor (2 bolts or a single clamp; disconnect throttle linkage and choke linkage — photograph or sketch their positions before removal)
5. Disassemble: float bowl (one bolt underneath), float (pin slides out), needle, main jet
6. Spray all passages with carburetor cleaner; compressed air through each jet and passage is best; compressed air is second best; blowing through with your mouth is a last resort
7. The main jet has a small hole in the center — this must be open; run a single bristle from a wire brush through it
8. Reassemble; reinstall on engine; reconnect linkages and fuel line
9. Open fuel valve; attempt to start

### Startup Procedures

**Cold weather startup (below 20°F / -7°C):**
1. Keep the generator in a heated space (pump house, garage) when temperatures drop below 0°F — oil thickens and battery cold-cranking amps drop significantly
2. Use the correct oil weight: if you normally run 10W-30, switch to 5W-30 for winter operation
3. Choke fully closed for cold start; as engine warms (30–60 seconds), gradually open choke to half; fully open when engine is running smoothly
4. Allow the engine to warm at low load for 2–3 minutes before applying full load
5. Do not run a generator in an enclosed space — carbon monoxide is lethal within minutes in an enclosed area

**Load management:**
- Never exceed 80% of rated wattage for sustained loads
- Never start a motor load (refrigerator, pump, saw) without first calculating its startup wattage (typically 2–3× running wattage)
- If the generator surges or sputters under load, reduce load and investigate cause before continuing

### Fuel Storage and Rotation

**Gasoline:**
- Untreated gasoline: 3–6 months usable; ethanol blends degrade faster
- Treated with STA-BIL Storage: up to 24 months [11]
- Storage containers: red plastic jerricans or metal safety cans; do not store in galvanized metal (galvanizing reacts with ethanol blends)
- Storage conditions: cool, dark, and ventilated location; away from any ignition sources; not in the same structure as living quarters
- Rotation schedule: label containers with date filled; use oldest first; add new fuel as you draw down; do not let stored fuel sit beyond the stabilizer's rated period

**Diesel:**
- Untreated diesel: 6–12 months; begins to grow microbial contamination (dark slime) after 12 months
- Treated with STA-BIL Diesel: up to 12 months beyond normal storage [11]
- Diesel is generally more stable than gasoline but more vulnerable to microbial growth; use a biocide additive (sold with diesel stabilizers) if storing for extended periods
- Signs of bad diesel: dark color, sediment at bottom of container, waxy clouding at cold temperatures (normal in winter, but if it doesn't clear when warmed, the fuel has gelled)

---

## Section 4: Small Engine Maintenance

### Chainsaw Maintenance

The chainsaw is the primary firewood-cutting tool for a Midwest community dependent on wood heat. A dull or poorly maintained chainsaw is also one of the most dangerous pieces of equipment a community handles — dull chains require more force and are more likely to kick back.

**Annual maintenance schedule:**

| Task | Frequency | Notes |
|---|---|---|
| Chain sharpening | Every 2–3 hours of use, or when cutting effort increases | See sharpening procedure below |
| Chain tension adjustment | Before each use | Correct tension: chain lifts 1/8" from bar groove; snaps back |
| Bar oil reservoir | Every tankful of fuel | Bar oil is separate from 2-stroke mix; don't run without it |
| Air filter cleaning | Every 5–10 hours of use | Tap out; wash in warm water if paper element; replace if torn |
| Fuel filter | Annually | Inside the fuel tank; replace the small cylindrical filter on the fuel pickup line |
| Spark plug | Annually | Check gap; replace if corroded or carbon-fouled |
| Bar inspection | Every 10 hours or monthly in heavy use | Check for rail wear, groove wear, sprocket nose |
| Chain replacement | When chain is shorter than the replacement guide marks, or when sharpening doesn't restore cutting performance | Do not run a stretched chain |
| Starter cord | As needed | Replace before it breaks all the way through |

**Chain sharpening procedure:**
The round file diameter for sharpening must match the chain's pitch [12]:

| Chain pitch | Round file diameter |
|---|---|
| 1/4" | 4.0 mm (5/32") |
| .325" | 4.8 mm (3/16") |
| 3/8" (standard) | 5.5 mm (7/32") |
| 3/8" low-profile (Picco) | 4.0 mm (5/32") |
| 0.404" | 5.5 mm (7/32") or 6.4 mm (1/4") |

The chain pitch is usually stamped on the drive links or listed in the owner's manual. When in doubt, measure 3 rivets center-to-center and divide by 2.

**Sharpening steps:**
1. Secure the bar in the bench vise (or use a bar mount)
2. Identify the shortest cutter tooth — all cutters must be filed to this length for even cutting
3. Place the round file in the tooth's curved face at the correct angle: most chains require 25–35° horizontal and 10° down-tilt (consult the file guide or chain manufacturer's spec)
4. File with smooth forward strokes (2–4 strokes per tooth for regular sharpening); rotate the file every 10–15 teeth to use fresh abrasive
5. Alternate teeth: chains have left-cutting and right-cutting teeth alternating; file all of one orientation, then rotate the bar 180° and file the other
6. After filing cutters, check depth gauges (the raker in front of each cutter): if depth gauges are higher than the cutter by more than 0.025" (use a depth gauge tool or flat file guide), file them down. Low depth gauges cause aggressive cutting; high depth gauges cause poor cutting performance.
7. Re-tension the chain; oil the bar groove; test by cutting a small log

**2-stroke fuel mix:**
Most modern chainsaws run on a 50:1 ratio (gasoline to 2-stroke oil): 50 parts gasoline, 1 part 2-stroke oil [12]. Some older saws or air-cooled engines specify 40:1. Check the saw's manual.

Premix in a dedicated container:
- For 1 gallon of fuel: 2.6 oz of 2-stroke oil (50:1) or 3.2 oz (40:1)
- Use fresh fuel (under 30 days old, or stabilized); ethanol-blend degradation in a 2-stroke system is more damaging than in 4-stroke because there is no oil reservoir to compensate

### Small Tractor and ATV Maintenance

For a Midwest community of 50–150 people, a small utility tractor (20–50 HP) or ATV with a utility bed is the primary field transportation and light farm implement platform.

**Annual schedule:**

| Task | Frequency | Notes |
|---|---|---|
| Oil and filter change | Every 100 hours | Use the oil weight in the operator's manual; do not guess |
| Air filter | Every 100 hours or annually | Replace paper filter; clean pre-cleaner foam in warm soapy water |
| Hydraulic fluid check | Monthly | Maintain at the full mark on the dipstick; use only the specified fluid (HY-TRAN or equivalent) |
| Hydraulic filter | Every 300 hours or annually | Replace; also drain and replace hydraulic fluid at 500-hour intervals |
| Belt inspection | Annually (pre-season, April) | Check all drive belts for cracking, glazing, fraying; replace before they break |
| Tire pressure and seating | Monthly | Under-inflated tires increase rolling resistance and cause uneven wear; over-inflated tires on soft soil cause compaction |
| PTO shaft and driveline | Semi-annually | Grease all fittings; inspect for missing shields (a rotating PTO shaft without a shield is a severe injury hazard) |
| Battery | Monthly | Check terminals; keep clean; check voltage (12.4–12.8V at rest) |
| Coolant (liquid-cooled engines) | Annually | Check level; replace every 2 years or per manufacturer spec |
| Grease all zerks | Every 50 hours | All grease nipples (zerks) on pivot points, drag links, and axles |

**Zone 5 harvest season note:**
August–October represents 200–300% of normal tractor intensity for harvest operations. Pre-harvest inspection in late July should include: full oil and filter change, hydraulic fluid top-off, all belts, and a complete grease of all zerks. Do not defer this inspection — a tractor failure during harvest cannot wait 2 weeks for a part.

### Hand Tool Maintenance

Hand tools are often the most neglected category — until they fail. An axe with a loose head that flies off is a serious injury risk. A dull hoe requires 3× the labor. Basic hand tool maintenance extends tool life from decades to generations.

**Axe and splitting maul:**
- Edge sharpening: file with a single-cut bastard file in a concave-to-convex motion following the original edge bevel; finish with a whetstone (80 then 120 grit)
- Handle tightening: if the head is loose, soak the head and handle in water for 24 hours — the wood swells and tightens in the eye. This is a temporary fix; a properly fitted wooden wedge (or a steel expansion wedge driven with a hammer) provides a durable solution [13].
- Handle replacement: when a handle is cracked or broken, do not burn out the old handle (heat can draw the temper from the steel head, permanently softening the cutting edge). Instead: drill or chisel out the old handle from the eye; fit a replacement ash or hickory handle from a hardware or farm supply store; drive a steel expansion wedge into the handle end after fitting. A good replacement handle costs $10–15.
- Storage: oil the head lightly before winter storage to prevent rust; hang the axe (or hang in a rack) to keep the edge off the ground

**Shovels, hoes, rakes:**
- Sharpen digging tools annually with a file (shovel blades should maintain a 45° bevel)
- Replace splintered or broken handles using the same wooden wedge method as axes
- Clean soil from metal surfaces after use and dry before storage; a thin coat of oil prevents surface rust

**Saw maintenance (hand saws):**
- Set and sharpen annually for any saw in regular use; this requires a saw set (a tool that bends teeth alternately left and right to maintain the saw kerf) and a triangular file
- A saw that is set properly and sharp requires far less effort and produces much cleaner cuts
- Store hanging or in a blade guard; never stack flat (blade contact with other metal tools dulls the teeth)

---

## Section 5: Electronics and Communication Equipment

### Radio Maintenance (GMRS and Ham)

GMRS (General Mobile Radio Service) and ham radio are the primary community communication systems when cell networks fail. See [community/01-emergency-response-infrastructure.md](community/01-emergency-response-infrastructure.md) for the communication net structure.

**Annual maintenance schedule:**

| Task | Frequency | Notes |
|---|---|---|
| Battery capacity test | Annually | Charge fully; time how long at nominal draw before voltage drops to 80%; compare to previous year |
| Battery replacement | Every 3–5 years for Li-Ion; every 2–3 years for NiMH | Li-Ion loses ~20% capacity/year; replace when capacity drops below 70% |
| Antenna inspection | Semi-annually | Check for physical damage; verify connector is not corroded |
| Audio test | Monthly | Transmit on a test frequency and have another operator confirm audio quality |
| Channel/frequency programming verification | Annually | Verify all programmed channels are still correct per your net frequency list |
| Waterproofing gaskets | When the radio is opened for battery replacement | Inspect O-ring seals; replace if cracked or flattened |

**Battery replacement:**
Handheld GMRS radios typically use a proprietary battery pack (lithium ion). When a battery pack fails, the replacement procedure is:
1. Align the new pack parallel to the radio body; slide upward until it clicks into the battery connector
2. Charge fully before first use (4–6 hours for a depleted pack)
3. Label the pack with the installation date; this is the reference point for the 3–5 year replacement interval

**Manual radio programming (when programming software is unavailable):**
Most GMRS handheld radios allow manual channel programming through the front panel menu. The process varies by model, but the general procedure is:
1. Enter VFO (frequency entry) mode (usually a button labeled VFO, MENU, or similar)
2. Enter the transmit frequency using the keypad
3. Enter any required offset (for repeaters: check the repeater directory for your area)
4. If CTCSS/DCS tone is required (for repeater access), navigate to the tone menu and enter the correct code
5. Save to a channel memory using the MENU or MR (memory recall) button
6. Label the channel in the memory

Print out the programming frequency lists for all community channels and store in the shop reference library. Manual programming from memory is error-prone; printed reference eliminates this problem.

**Antenna inspection:**
- Inspect the antenna for physical damage (kinks, cracks in the rubber boot, bent whip)
- Inspect the connector where the antenna meets the radio body: the connector threads should be clean and the mating surfaces should mate cleanly
- Never use a radio with a damaged or missing antenna — transmitting without an antenna returns the full transmitted power to the radio's final amplifier, damaging it within seconds
- A simple antenna test: transmit and note the SWR (standing wave ratio) with an SWR meter if available; a ratio above 2:1 indicates antenna or connector problems

### Basic Electronics Diagnosis with a Multimeter

A multimeter is the single most important diagnostic tool for electrical and electronic repair. With just a multimeter, a trained person can diagnose the majority of electrical faults in community equipment [14].

**The four measurements you will use most often:**

**1. DC voltage (V DC or ⎓):**
Use to: check battery voltage, verify solar panel output, check that power is reaching a failed device.
- Probe placement: red probe to positive (+), black probe to negative (-) or ground
- Reading: a 12V battery should read 12.0–12.8V at rest (12.0V = discharged; 12.6–12.8V = fully charged)
- A reading significantly below expected indicates a bad connection or depleted source

**2. Continuity (speaker icon or diode symbol):**
Use to: verify a wire is complete (not broken internally), check a switch, test a fuse, trace a circuit.
- Power must be off for continuity testing
- Touch probes to both ends of the wire or component; the multimeter beeps if there is a continuous path
- Application: check a fuse — probes on both ends; beep means fuse is good; no beep means blown fuse
- Check a wire run: probes on both ends; beep means the wire is intact; no beep means the wire is broken somewhere

**3. Resistance (Ω):**
Use to: measure resistance of a component, check for shorts to ground, verify the winding resistance of a motor
- Power must be off; the component must be isolated from the circuit (at least one end disconnected)
- A reading close to 0 Ω where you expect high resistance indicates a short circuit
- A reading of overload (OL or ∞) where you expect a specific value indicates an open circuit (broken wire or failed component)

**4. Capacitance (F or Cap):**
Use to: test electrolytic capacitors (the most common failure in inverters, charge controllers, and motor start circuits)
- Discharge the capacitor first (a moment across a resistor or a brief short with an insulated screwdriver)
- Compare the measured capacitance to the value marked on the capacitor body (usually in microfarads, µF)
- A capacitor reading 20% or more below its rated value is failing; one reading well above its rated value is shorted

**Identifying failed components without measurement (visual inspection):**
Many failed components announce themselves visually before they cause complete failure:
- Blown fuse: the element inside the glass tube is visibly broken or burned
- Burned resistor: brown or black scorching; crumbled body
- Bulging or leaking capacitor: the top of an electrolytic capacitor should be flat; domed or cracked tops indicate failure; brown residue around the base indicates leakage
- Burned PCB traces: black lines where a copper trace used to be
- Corroded connections: greenish oxidation on terminals; white crystalline deposits on battery terminals

### Soldering — Through-Hole Component Replacement

Soldering is the skill that enables board-level repair of failed components (fuses, capacitors, relays) and field fabrication of wire harnesses and antenna connections.

**Equipment required:** Temperature-controlled soldering iron (set to 350°C / 660°F for most electronics work), solder (60/40 tin-lead for older equipment; 63/37 for finer work; lead-free for RoHS-compliant equipment), flux paste or flux pen, desoldering wick or suction pump, safety glasses.

**Basic through-hole component replacement:**
1. Apply flux to the joints you are about to desolder (flux improves heat transfer and wetting)
2. Heat the pad and lead simultaneously with the iron tip; apply desoldering wick to absorb the molten solder
3. When solder is absorbed, the component lead should be free in the hole; repeat for each lead
4. Remove the failed component; note polarity markings for replacements (capacitors and diodes are polarized)
5. Insert the new component; bend leads slightly outward to hold it in place
6. Heat the pad and lead; apply a small amount of fresh solder; the solder should flow around the lead and form a bright, concave cone shape
7. Inspect the joint: a good solder joint is shiny and concave; a cold (failed) joint is dull, grainy, or balled

**Flux cleaning:**
After soldering, clean flux residue with isopropyl alcohol (90% or higher) and a toothbrush. Flux residue is slightly conductive and can cause leakage currents that damage sensitive circuits over time.

**The honest limit of field repair:**
Modern circuit boards contain surface-mount components smaller than 1mm, multi-layer copper traces, and microcontrollers with custom firmware. These cannot be repaired in the field. The practical boundary for community-level electronics repair is:
- Replaceable components: fuses, through-hole capacitors and relays, connectors, switches, wiring harnesses
- Do not attempt: reflowing or replacing surface-mount ICs, anything requiring a schematic for advanced diagnosis, firmware re-flashing without appropriate equipment
- Design principle: when selecting community equipment, prefer designs with modular, replaceable components and documented circuit diagrams (Victron Energy equipment is exemplary in this regard)

---

## Section 6: Zone 5 Midwest Specifics

### Freeze Protection

Zone 5 Midwest temperatures regularly reach -10°F to -20°F (-23°C to -29°C) during January–February. This temperature range freezes water in pipes within minutes to hours depending on exposure. Equipment failure from freezing is entirely preventable with proper preparation.

**Well pump and water system:**
- All above-ground plumbing in unheated or poorly heated spaces must be insulated or heat-taped
- Heat tape (self-regulating electric pipe heating cable): install on water supply lines in unheated crawl spaces, unheated sections of pump houses, and exterior wall pipe runs; wrap the tape in contact with the pipe, then cover with foam pipe insulation
- Self-regulating heat tape adjusts its output based on ambient temperature; it is far safer than constant-wattage tape, which can overheat and cause fires if poorly installed [15]
- Pump house insulation: inspect each October for gaps, missing insulation, broken windows, or poorly sealed penetrations; an insulated pump house with a single 60W bulb can maintain above-freezing temperatures to -20°F ambient if well-sealed
- Winterization of outdoor equipment: any pump, irrigation line, or filter housing that is not heat-protected must be drained before first hard freeze (in Zone 5, the target date is October 15; in northern Zone 5, October 1)

**Generator cold-weather protocol:**
- Oil viscosity: switch to 5W-30 when temperatures consistently drop below 20°F (-7°C)
- Cold start: allow an extra 30–60 seconds of warm-up before applying load; engines run richer on choke and oil doesn't fully circulate until warm
- Storage: store the generator in a space that stays above 20°F (-7°C) if possible; a fully cold generator below 0°F will be very difficult to start and may experience cold-cracking of plastic components
- Extension cord capacity: at low temperatures, copper conductor resistance increases and voltage drop across long runs increases; use heavier gauge cord (10 AWG for runs over 50 ft)

**Battery storage:**
- Lead-acid batteries lose significant cold-cranking capacity at low temperatures: a battery at 0°F has roughly 50% of its capacity compared to 70°F
- Do not charge a frozen battery — this can cause the battery to explode; allow it to warm to above 32°F (0°C) before charging
- Ideally, keep battery banks in an insulated, slightly heated space (above 32°F); even 40°F provides much better performance than 0°F

### Corrosion — Road Salt and Midwest Summers

Zone 5 Midwest communities face a corrosion environment that combines winter road salt (deposited on vehicles and equipment that drive on treated roads, then spread to equipment stored nearby) with warm, humid summers (20–30 inches of rain per year, with dew points regularly exceeding 70°F in July and August).

This combination accelerates metal corrosion significantly compared to either a dry Western climate or a consistently wet Pacific Northwest climate.

**Annual corrosion inspection (October):**
- Inspect all metal-to-metal contacts in electrical systems: battery terminals, inverter bus bars, solar combiner boxes, charge controller terminals — clean with battery terminal cleaner and protect with petroleum jelly or anti-corrosion spray
- Generator: inspect the carburetor, fuel valve, and any aluminum components for white oxidation (electrolytic corrosion from salt); this appears as white powder or pitting on aluminum surfaces
- Hand tools: oil all metal surfaces before winter storage; a light coat of linseed oil or WD-40 on file surfaces and blade edges prevents surface rust
- Chainsaw bar: remove the bar, clean the groove with a flat pick, clean the sprocket nose, and apply bar oil before storage; a gunked bar groove increases chain and motor wear dramatically
- Tractor and ATV: spray exposed undercarriage and all pivot points with chain lube or fluid film after washing in fall; road salt in wheel wells and frame cavities causes accelerated structural corrosion

**Summer humidity and electronics:**
- High dew points and warm temperatures create condensation inside electronic enclosures when temperatures drop overnight
- Inspect all electrical enclosures (charge controllers, inverters, radio equipment) for moisture ingress signs: rust on fasteners inside the enclosure, condensation droplets on internal components, corroded terminal strips
- Store silica gel desiccant packets inside sensitive enclosures; replace or regenerate packets annually (bake at 250°F for 2 hours to regenerate)

### Harvest Season Load — August through October

The August–October window represents the highest-intensity equipment use period for a Midwest agricultural community. During this period:

- Tractors may run 10–14 hours per day (vs. 2–3 hours in a normal week)
- Generators run continuously to power sorting, washing, or processing equipment
- Chainsaws may be in use multiple days per week if fall firewood processing coincides with harvest
- Water systems are under peak demand from garden irrigation, livestock watering, and community food processing

This 200–300% intensity load is exactly when equipment failure is most costly — a tractor failure during harvest is measured in days of unharvested food, not just inconvenience.

**Pre-harvest inspection checklist (complete by July 31):**

Tractor:
- [ ] Oil and filter change
- [ ] Hydraulic fluid — check level and color (dark, contaminated fluid indicates water intrusion or overheating)
- [ ] All belts — replace any showing cracks or glazing
- [ ] Grease all zerks
- [ ] Battery voltage and terminal condition
- [ ] Tire pressure — all four tires at correct PSI

Generator:
- [ ] Oil change
- [ ] Air filter — clean or replace
- [ ] Spark plug — inspect and gap; carry spare
- [ ] Carburetor — run Sea Foam treatment if generator has been stored since spring
- [ ] Fuel stabilizer added to fuel tank if it won't be run daily
- [ ] Load test at 75% rated load for 30 minutes

Chainsaw:
- [ ] Chain sharpened
- [ ] Bar oiled; groove cleaned
- [ ] Air filter cleaned
- [ ] Fuel mix prepared fresh

Water system:
- [ ] Pressure tank air charge verified
- [ ] Submersible pump flow rate check (measure gallons per minute; compare to baseline)
- [ ] Storage tank at full level before harvest begins

**During harvest (weekly check):**
- Generator oil level: check weekly when running daily; top off as needed
- Chainsaw chain: sharpen every 2–3 hours of use
- Tractor: check engine oil and hydraulic fluid daily when running extended hours
- Water storage: check tank level daily; ensure inlet and outlet screens are clear

---

## Sources

[1] Solar panel dust accumulation and performance loss data — Enphase solar maintenance guide and Sandbar Solar analysis: https://enphase.com/blog/homeowners/solar-panel-cleaning-and-maintenance-guide

[2] Flooded lead-acid battery specific gravity maintenance and equalization — BSL Power charging guide and Fire Mountain Solar deep-cycle battery reference: https://bslpower.com/lead-acid-battery-charging-guide-flooded-agm-and-gel-batteries-explained

[3] AGM battery equalization warning — Unbound Solar battery comparison guide: https://unboundsolar.com/blog/lead-acid-battery-comparison

[4] MPPT charge controller error codes — Victron Energy MPPT error code reference: https://www.victronenergy.com/live/mppt-error-codes

[5] Solar charge controller troubleshooting — inverter.com field guide: https://www.inverter.com/solar-charge-controller-troubleshooting

[6] Hand pump leathercup replacement intervals — community field reports and Lehman's supply documentation: https://www.lehmans.com/product/replacement-cup-leathers-for-water-pumps/

[7] Pressure tank air charge and bladder diagnosis — Mid-Atlantic Water Services troubleshooting guide and National Water Service diagnosis: https://midatlanticwater.net/blogs/faqs/well-pressure-tank-troubleshooting

[8] Pressure tank knock test and waterlogged tank diagnosis — Engineer Fix and Fresh Water Systems references: https://engineerfix.com/how-to-tell-if-your-well-tank-bladder-is-bad/

[9] Generator carburetor gum from ethanol-blend fuel — FIRMAN Power Equipment maintenance guide: https://firmanpowerequipment.com/blogs/news/general-maintenance

[10] Generator maintenance intervals and oil change schedule — Mi-T-M generator maintenance reference: https://www.mitm.com/blog/generator-maintenance/

[11] STA-BIL fuel stabilizer shelf life and storage duration — Gold Eagle Co. product documentation and Amazon product specifications: https://www.goldeagle.com/product/sta-bil-fuel-stabilizer/

[12] Chainsaw chain sharpening file sizes and 2-stroke fuel mix — Hipa Store chain file guide and VP Racing Fuels chainsaw fuel mix reference: https://www.hipastore.com/blogs/chainsaw/choosing-the-right-round-file-to-sharpen-your-chainsaw-chain

[13] Axe handle replacement procedure — USDA Forest Service publication "Reshaping or Replacing an Ax Handle": https://www.fs.usda.gov/t-d/pubs/pdfpubs/pdf18232812P/Part09_ReplacingHandles.pdf

[14] Multimeter usage guide for electronics diagnosis — iFixit community guide and Fluke continuity testing reference: https://www.ifixit.com/Guide/How+To+Use+A+Multimeter/25632

[15] Freeze protection and heat tape installation — American Red Cross frozen pipe prevention and theplumber.com well freeze protection: https://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-of-emergencies/winter-storm/frozen-pipes.html

[16] Submersible pump failure diagnosis — Rural Water Guide troubleshooting reference and Epp Well Solutions diagnosis guide: https://ruralwaterguide.com/submersible-well-pump-troubleshooting/

[17] Sea Foam carburetor treatment protocol — Sea Foam Works official usage guide: https://seafoamworks.com/small-engine-maintenance/

[18] iFixit Kiwix offline archive — 44,000+ guides, 2.5 GB: https://www.ifixit.com/News/64006/download-every-ifixit-guide-for-free

[19] USDN Tool Lending Libraries initiative — community tool library governance models: https://sustainableconsumption.usdn.org/initiatives-list/tool-lending-libraries

[20] Well pump pressure tank short cycling and diagnosis — National Water Service and Epp Well Solutions references: https://nationalwaterservice.com/is-my-well-pump-or-pressure-tank-bad/
