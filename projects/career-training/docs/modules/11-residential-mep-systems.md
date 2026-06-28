---
title: "Residential MEP Systems for the General Contractor"
module: 11
discipline: ["plumbing", "electrical", "mechanical", "HVAC", "MEP"]
audience: "Residential GC — construction-experienced, managing MEP trades for the first time"
status: "reference"
tags: [career-training, MEP, plumbing, electrical, HVAC, mechanical, California, residential]
created: 2026-05-12
---

# Residential MEP Systems for the General Contractor

> **How to use this document**: MEP is where projects bleed money, fail inspections, and produce callbacks for years. A licensed plumber, electrician, or HVAC contractor knows their own trade — but nobody but you is responsible for the *interfaces* between them, the *sequence*, and whether the system the engineer drew is the system that actually got built. This document gives you the working knowledge to scope subcontracts correctly, read a rough-in, recognize bad work before it gets covered, and pass inspection the first time. You will not become a licensed trade. You will become the smartest non-trade person in the trailer.

---

## How MEP Differs From Carpentry: A Mental Model

Framing is forgiving. You can sister a joist, add a strap, shim a wall. MEP is not forgiving in the same way. Once a drain is poured into a slab, once Romex is buried in a wall, once a refrigerant line is brazed and pressurized — fixing it costs 10× what doing it right cost.

Three rules govern everything in this document:

1. **MEP is sequential and irreversible.** Drains go in first because they need slope and can't go around obstacles. Water and gas come next (smaller, more flexible). Electrical follows (most flexible). HVAC ducts are big and dumb — they take what space is left, so they must be coordinated *first* on paper even though they install later.
2. **MEP is about flow rates, not parts.** Plumbing moves water and waste at flow rates; electrical moves current at amperages; HVAC moves air and refrigerant at CFM and tonnage. Every code rule, every pipe size, every wire gauge is ultimately about whether the system can carry its required flow under worst-case demand.
3. **MEP inspections catch what you cannot see later.** Rough inspections exist because the inspector cannot verify a buried pipe or a wire in a wall after drywall. Once you cover an inspection failure, you own it forever. **Never cover a rough that has not been signed.**

### MEP Sequencing Master Sequence

| Phase | Plumbing | Electrical | HVAC |
|---|---|---|---|
| **Underground** | DWV in slab, water service stub | Conduit under slab for service, EV, future loads | Refrigerant line chase, condensate drain stub |
| **Top-out / Rough** | DWV through wall and roof, water supply, gas | Panel set, all wire pulled, boxes set, low-voltage | Equipment set, ducts, refrigerant lines, vent flues |
| **Inspection** | DWV pressure/water test, water 100 PSI, gas 10 PSI | Rough wire inspection (visible) | Duct leakage, combustion air, condensate |
| **Insulation / Drywall** | (covered) | (covered) | (ducts covered) |
| **Trim** | Fixtures, faucets, water heater set, gas connections | Devices, fixtures, panel labels, smoke/CO | Registers, grilles, thermostat, commissioning |
| **Final** | Fixture test, hot water delivery time, leak check | All circuits energized, AFCI/GFCI test | Refrigerant charge verification, HERS, startup |

---

# PART I: PLUMBING

---

## 1. Drain, Waste & Vent (DWV)

DWV moves wastewater out of the building by gravity (drains) and equalizes pressure so traps don't siphon dry (vents). It is the single most error-prone system in a remodel because every fixture has to connect to a stack, every stack needs a vent, and slopes have to work in real space without hitting joists, beams, or other trades.

### 1.1 DWV Pipe Materials

| Material | Where used | Joining | Noise | CA / CPC notes |
|---|---|---|---|---|
| **ABS (black plastic)** | Most common in CA residential; above and below ground; vents | Solvent cement (one-step, black) | Loud — water hammer and gurgle audible through pipe | CPC allows; many CA jurisdictions default ABS. Schedule 40 standard. |
| **PVC (white plastic)** | Allowed for DWV; common in commercial; some CA jurisdictions prefer | Primer (purple) + solvent cement (clear/blue) | Slightly quieter than ABS, still loud | CPC allows. **Never mix ABS and PVC** without a transition coupling (mechanical, not solvent). |
| **Cast iron (no-hub)** | Premium residential; vertical stacks in multi-story; wherever noise matters (bedroom stack, theater wall) | No-hub clamps (Husky-style stainless bands) or hub-and-spigot with neoprene gaskets | Very quiet — best material for above-ceiling drains over occupied space | CPC allows; required by some HOAs and luxury specs. Heavy — needs proper support every 5 ft horizontal. |
| **Galvanized steel** | Legacy only; **never specify for new** | Threaded | n/a | Corrodes from inside; if you find it in a remodel, expect to replace. |
| **Copper DWV** | Rare, vintage | Solder | Quiet | Cost-prohibitive today; mention only because you'll see it in old houses. |

**Practical scoping rules:**
- For a typical CA tract-style residential, ABS Sch 40 is standard and what every plumber will bid by default. Specify in the contract: "Schedule 40 ABS for DWV above and below grade, cast iron no-hub for any DWV run above a finished ceiling in a sleeping area."
- Cast iron costs roughly 3–4× ABS in labor and material. Use it strategically — bedroom-over-living-room stack, theater wall, primary bath above kitchen. The owner will hear ABS forever and blame you.
- If you specify cast iron, also specify **no-hub** (banded couplings), not hub-and-spigot. Faster install, no oakum-and-lead nonsense, easier repairs.

### 1.2 Pipe Sizing (Drainage)

DWV sizing is governed by **Drainage Fixture Units (DFUs)** — each fixture is assigned a number representing its load, and pipe sizes are capped at a maximum DFU per pipe diameter and slope.

#### Trap and minimum drain sizes by fixture (CPC Table 7-3, abridged)

| Fixture | Trap size | Drain DFU | Min branch drain |
|---|---|---|---|
| Lavatory (bathroom sink) | 1¼" (1½" preferred) | 1 | 1¼"/1½" |
| Kitchen sink (single or double) | 1½" | 2 | 1½" |
| Kitchen sink with disposal/dishwasher | 1½" | 2–3 | 2" recommended |
| Shower | 2" | 2 | 2" |
| Tub | 1½" | 2 | 1½" |
| Toilet (water closet) | Integral (3") | 3–4 | 3" |
| Laundry standpipe (washer) | 2" | 2 | 2" |
| Floor drain | 2" | 2 | 2" |
| Bidet | 1¼" | 1 | 1¼" |
| Bar sink | 1½" | 1 | 1½" |

**Critical rules:**
- A 2" drain cannot serve a toilet. **Toilets need a 3" minimum drain** (4" preferred for multiple WCs on one branch).
- A horizontal branch carrying a WC must be 3" minimum for its entire length until it joins a larger main.
- You can never reduce pipe size in the direction of flow.

#### Horizontal branch drain slope

| Pipe size | Minimum slope | Note |
|---|---|---|
| 2½" and smaller | ¼" per foot (2%) | Standard residential — memorize this |
| 3" to 6" | ⅛" per foot (1%) acceptable, ¼" preferred | For long horizontal mains |
| 8" and larger | 1/16" per foot acceptable | Commercial scale |

**Slope is non-negotiable.** Too flat → solids drop out, clog. Too steep (greater than 1" per foot or roughly 45°) → liquid runs ahead of solids, leaves them behind, clog. The "Goldilocks zone" of ¼" per foot is what every residential plumber should hit.

**How to verify on site:** A 4-foot level reading a full bubble of slope on a 4-ft run = 1" drop = ¼" per foot. Walk every drain run with a 4-ft level before drywall. This is a 30-minute task on a full house and catches roughly 90% of DWV failures before inspection.

#### Stack sizing (vertical drains)

| Stack DFU load | Min stack size |
|---|---|
| Up to 2 DFU | 1½" |
| Up to 6 DFU | 2" |
| Up to 20 DFU | 2½" |
| Up to 30 DFU (one WC OK) | 3" |
| Up to 240 DFU (multiple WCs) | 4" |

A typical 3-bath house with kitchen, laundry, and 3 WCs runs about 35–45 DFU total — a 3" main stack is standard, 4" for redundancy on larger homes.

### 1.3 Venting

Every trap must be vented or it siphons dry → sewer gas in the house. Venting is the most-failed item on DWV rough inspections, almost always because of vent slope (wet horizontal vents) or trap-to-vent distance.

#### Vent types

| Vent type | What it is | Where used |
|---|---|---|
| **Individual vent** | Dedicated vent from each trap up to the vent stack | Best practice; required by some inspectors for kitchens |
| **Common vent** | One vent serves two fixtures back-to-back (e.g., double-sink, two lavs on opposite walls) | Very common in residential |
| **Wet vent** | A drain that also serves as a vent for an upstream fixture (limited size and DFU) | Common in residential when planned carefully |
| **Circuit / loop vent** | Vents several fixtures off a horizontal branch | Rare in single-family |
| **Air Admittance Valve (AAV)** | One-way mechanical valve that opens under negative pressure to admit air | **Restricted in California — see below** |

#### Trap-to-vent distance (CPC Table 10-1, the "critical distance")

| Trap arm size | Max trap-to-vent horizontal distance |
|---|---|
| 1¼" | 2'-6" (30") |
| 1½" | 3'-6" (42") |
| 2" | 5'-0" (60") |
| 3" | 6'-0" (72") |
| 4" | 10'-0" (120") |

**This is the most-violated DWV rule in residential.** A homeowner-installed bath vanity 8 feet from the wall vent on a 1½" trap arm is a code violation, and the inspector will catch it.

The trap arm must also not drop more than one full pipe diameter between trap weir and vent connection (otherwise the trap is "double-trapped" by its own slope).

#### Air Admittance Valves (AAVs) in California

CPC §905.0 allows AAVs but **most California AHJs heavily restrict them**:
- Many CA jurisdictions disallow AAVs entirely in new construction.
- Where allowed, they are typically permitted only for island sinks (where running a true vent is impossible) and only with AHJ pre-approval.
- AAVs cannot serve as the sole vent for an entire building — a true atmospheric vent through the roof is required somewhere.
- AAVs must be accessible — never seal one behind drywall.
- They have a lifespan (15–20 years) and fail silently.

**Practical rule:** Design for atmospheric venting through the roof. Use AAVs only for island sinks and only after confirming with the inspector. Never let your plumber substitute AAVs for studor-vented kitchens without a written variance.

### 1.4 Cleanouts (CPC §707)

A cleanout is an accessible plug in a drain line that a snake or jetter can be inserted into. Inspectors check these obsessively because they're free to miss during framing and impossible to add later.

**Required cleanout locations:**
- At the **upstream end** of every horizontal drain line
- At every **change in direction greater than 45°** (some AHJs require at every 45° fitting; check local)
- Every **100 feet** of horizontal run for 4" and smaller; every 200 ft for larger
- **Two-way cleanout** within 2 ft of where the building sewer exits the building (CA standard practice)
- At the **base of every stack**
- Upstream of fixtures where a snake can't otherwise reach (e.g., concealed fixtures)

**Access requirements:**
- Cleanout plug must have clearance equal to the pipe diameter — **18" clearance for a 4" cleanout, 12" for a 3"**, measured to the plug face.
- Cleanouts in floors must be accessible — no tile over cleanout caps unless flush-mounted access plates are used.
- Concealed cleanouts (in walls) require an access panel. Note these on plans and confirm trim sequence — they are often missed at finish.

**Field check before drywall:** Walk every drain main. Is there a cleanout at every direction change? Is the upstream cleanout accessible (not buried by a return air chase, not behind framing)? Are wall cleanouts called out for access panels?

### 1.5 DWV Pressure / Water Test

Two options for testing — **water test** is most common, **air test** in cold weather or when water access is limited.

#### Water test (CPC §712.2)

1. Cap all DWV openings except the highest (roof penetration).
2. Fill the system with water from a hose at the highest point.
3. Water must stand for **15 minutes minimum** with no drop in level (some AHJs want longer).
4. Test pressure on the lowest fitting is the static head from the highest fixture — typically 10–20 ft of water (4–9 PSI), depending on house height.

#### Air test

1. Cap all DWV openings.
2. Pressurize to **5 PSI** with a hand pump and gauge.
3. Hold for **15 minutes** with no measurable drop.

**What the test finds:** Leaks at solvent-welded joints (skipped primer, cold glue, cracked fitting), cracked fittings from rough handling, missing caps, unsealed cleanouts.

**What it does not find:** Slope problems, vent problems, missing cleanouts, undersized pipe — those are visual inspections.

**GC role:** Schedule the test for daylight when you can see drips. Have the plumber on site (you can't fix it). Have a bucket and rag — small leaks are tightened up in real time and re-tested.

### 1.6 Common Rough Plumbing Mistakes (the things that fail inspection)

| Mistake | What it looks like | How to catch |
|---|---|---|
| **Insufficient slope** | Drain run looks "level" by eye | Walk every run with a 4-ft level; ¼" per foot |
| **Reverse slope** | Drain slopes the wrong way | Same — bubble on the wrong side |
| **Missing vent** | Trap with no vertical takeoff above the weir | Trace every trap to a vent; every trap MUST have one |
| **Wet vent overload** | Wet vent serves too many DFUs | Sum DFUs; wet vent typically limited to 4 DFU |
| **Trap-to-vent too far** | Vanity 8 ft from wall, vent on the wall | Measure trap arm; compare to Table 10-1 |
| **Cleanout missed** | No CO at end of run or at direction change | Walk plans; flag every horizontal main |
| **Concealed cleanout, no access** | CO behind drywall | Identify and order access panels |
| **Pipe support missing** | Long horizontal ABS without straps | Strap every 4 ft horizontal, every 10 ft vertical |
| **Damaged fitting** | Crack, burn mark, melted plastic from over-cementing | Walk system before test |
| **Drain runs through a beam/joist** without proper notch/hole | Structurally illegal | Coordinate with framer; engineer review |

---

## 2. Water Supply (Potable)

Water supply is the high-pressure side of plumbing — every joint will leak under 80 PSI if it's wrong, and unlike a DWV leak (which is contained to the drain when something is flushed), a supply leak runs continuously. Leak-detected supply lines in a wall destroy a house in 8 hours.

### 2.1 Water Supply Pipe Materials

| Material | Description | Pros | Cons | Joining |
|---|---|---|---|---|
| **Type L copper** | Hard copper, medium wall thickness | Long-proven; rigid; high-temp tolerant; recyclable | Most expensive labor; pinhole leaks possible in aggressive water; requires skilled solderers | Solder (lead-free) or press fittings (ProPress) |
| **Type M copper** | Thinner wall copper | Cheaper than L | **Not allowed underground in many CA jurisdictions**; more susceptible to pinholes | Solder or press |
| **PEX-A (e.g., Uponor)** | Cross-linked polyethylene, manufactured by Engel method | Most flexible; freeze-resistant (can expand 8% before bursting); fewest fittings; fastest install | Most expensive PEX; expansion-fitting tool required ($400+); UV-degrades — cover quickly | Cold expansion (Uponor ProPEX) |
| **PEX-B (e.g., Viega, Apollo)** | Cross-linked polyethylene, silane method | Cheap; widely available; uses crimp fittings | Slightly less flexible; more restrictive fittings reduce flow | Crimp rings (copper or stainless) or stainless clamps |
| **PEX-C** | Cross-linked by irradiation | Cheapest; rarely specified now | Stiffer, less freeze-tolerant | Crimp or clamp |
| **CPVC** | Chlorinated PVC | Cheap; OK for hot water; lighter than copper | Brittle when cold or aged; solvent-glue dependency; uncommon in CA | Primer + solvent cement |
| **Galvanized steel** | Legacy | n/a | Corrodes from inside; **replace on any remodel where exposed** | Threaded |

**California acceptance:** All five (Type L copper, PEX-A, PEX-B, PEX-C, CPVC) are CPC-approved. PEX-A is the dominant new-construction standard for cost and flexibility reasons.

**Practical scoping rules:**
- **Default residential spec**: PEX-A with home-run manifold for distribution; copper for water heater connections (high temp, codes require metallic at WH within 18" in some AHJs).
- **Slab penetrations**: PEX-A in sleeve (no fittings in slab). Never put a fitting in a slab — a leak there is a slab-jacker.
- **Hot water lines**: PEX-A or copper. CPVC OK but uncommon.
- **Exterior hose bibbs**: Copper sweat or PEX with a copper stub at the bibb. Frost-free bibbs in cold climates.
- **Recirculation lines**: PEX-A or copper (continuous duty).

#### Manifold vs. trunk-and-branch

| System | How it works | Pros | Cons |
|---|---|---|---|
| **Trunk-and-branch** | Main line tees off to each fixture; tees daisy-chain | Less pipe total; simpler | More fittings; pressure drop affects last fixture; one line shut-off affects many fixtures |
| **Home-run (manifold)** | Each fixture gets its own dedicated line back to a central manifold | Independent shut-offs per fixture; balanced pressure; faster hot water arrival; uses smaller pipe | More total feet of pipe; manifold takes wall space |

Modern PEX residential is almost always manifold. Specify manifold location early (utility room, hallway closet, garage) — it needs ~24"×30" of wall space.

### 2.2 Pressure and Pressure Regulation

**Typical municipal water service pressure: 50–80 PSI.** Some California neighborhoods are higher (foothills, pressure zones above the reservoir).

**Code rule (CPC §608.2):** If static pressure exceeds **80 PSI**, a Pressure Reducing Valve (PRV) is required.

#### PRV (Pressure Reducing Valve)

- Installed at the main water entry to the house, downstream of the main shut-off.
- Set to **60–65 PSI** typical (some plumbers set 55 PSI for older fixture comfort).
- Has a gauge port — install a gauge or test with one at rough.
- Creates a "closed system" — see expansion tank below.

#### Expansion tank (CPC §608.3)

When you install a PRV, the water heater can no longer push expanded hot water back into the city main (the PRV is a one-way valve). The expanded water has nowhere to go — pressure builds in the system, T&P valve weeps, fixtures bleed.

**Solution: thermal expansion tank** at the water heater cold inlet. Captures the expansion volume in a rubber bladder.

- Required by code whenever a PRV, check valve, or backflow preventer is installed (which is virtually every new CA house).
- Size: 2-gallon tank for most residential WHs (40–80 gal); larger for tankless or commercial.
- Pre-charge: match incoming cold water pressure (typically 50 psi).
- Mount: supported independently — never let the tank hang from copper alone (15+ lbs filled).

### 2.3 Pipe Sizing (Water Supply)

Water supply sizing is driven by **fixture units (FU)** and **velocity limits**.

**Velocity limit: 8 fps maximum** (CPC §610.12). Higher velocity causes:
- Pipe erosion (especially copper) — pinhole leaks years later.
- Water hammer.
- Noise.

Some CA AHJs recommend **5 fps for hot water** lines (copper erosion is accelerated by heat).

#### Simplified residential sizing (Type L copper or PEX-A)

| Pipe size | Max flow @ 8 fps | Typical use |
|---|---|---|
| ½" | ~7 GPM | Last 5 ft to a fixture (lav, shower, toilet) |
| ¾" | ~14 GPM | Branch lines, hose bibbs, water heater inlet |
| 1" | ~25 GPM | Service line, manifold inlet, irrigation |
| 1¼" | ~37 GPM | Large homes, multi-zone |
| 1½" | ~55 GPM | Large estates, multifamily |

**Typical residential service**: 1" copper or PEX-A from meter to house, ¾" branches, ½" drops. Larger homes (3+ baths, multiple WHs) often need 1¼" service.

**Demand-based sizing:** Look at simultaneous demand — what's the worst case? Two showers running while the dishwasher fills and the toilet refills. A 1" service handles roughly 25 GPM; the worst case for a typical 3-bath house is 12–18 GPM. So 1" is comfortable. If you've got 4+ baths or pressurized irrigation, run 1¼".

### 2.4 Hot Water — Recirculation and Insulation

#### Title 24 / CalGreen requirements (2022 cycle, in effect)

**Hot water pipe insulation** (Title 24 §150.0(j)):
- All hot water piping ¾" and larger requires **R-3 minimum insulation** (typically ½" closed-cell foam — Armaflex or similar).
- All hot water piping serving a kitchen requires insulation regardless of size.
- All hot water piping under a slab requires insulation regardless of size.
- First 5 ft of cold water piping from the WH requires insulation (heat migration).
- Pipe in unconditioned space (attic, exterior wall) requires insulation per Title 24 Table 120.3-A.

**Hot water demand recirculation** (Title 24 §150.0(n)):
- Required when the distance from WH to farthest fixture exceeds certain thresholds, or when the building exceeds certain plumbing layouts.
- Three compliant strategies:
  1. **Demand recirculation** — button-activated pump that runs only when needed (lowest energy).
  2. **Compact hot water distribution** — short pipe runs, manifold, ≤24 oz of water in any branch.
  3. **Continuous recirculation with high-efficiency controls** (timer + temp modulation).

**Practical rule:** Specify a **manifold + compact distribution** or a **demand-activated recirculation pump** (e.g., Taco D'MAND, Grundfos Comfort System). Continuous recirculation pumps with no controls fail Title 24 and waste energy.

### 2.5 Water Heater Types and Rough-In

| Type | How it works | Pros | Cons | Rough-in needs |
|---|---|---|---|---|
| **Tank, atmospheric vent (natural draft)** | Gas burner, hot exhaust rises through B-vent | Cheap; simple; most common in older homes | Backdrafting risk; lower efficiency (EF ~0.60); being phased out for code | B-vent chase to roof, combustion air, gas, cold inlet, hot outlet, T&P drain |
| **Tank, power vent** | Fan blows combustion exhaust horizontally | Vents through wall, no chase | Needs 120V circuit at WH; louder | PVC vent to exterior wall, 120V outlet, gas, water, drain |
| **Tank, direct vent / sealed combustion** | Draws combustion air from outside, exhausts outside, sealed combustion chamber | Safest; no indoor air for combustion; OK in tight homes | More expensive; specific vent layout | Concentric vent or two-pipe vent through wall, gas, water, drain |
| **Tankless gas (non-condensing)** | Burner fires on demand, heats water through HX | Endless hot water; smaller footprint | Higher install cost; needs larger gas line (¾"); won't work in low-flow situations; vent material limited | ¾" gas (often a dedicated run from meter), 120V circuit, Category III stainless vent or sealed concentric, water, drain |
| **Tankless gas (condensing)** | Same plus secondary HX recovers vapor | Higher efficiency (95%+); PVC vent allowed | Highest install cost; condensate drain required | ¾" gas, 120V, PVC vent, condensate drain, water |
| **Heat pump water heater (HPWH)** | Pulls heat from air, dumps cold air, heats tank | Highest efficiency (UEF 3.0+); no gas; eligible for incentives | Needs ~700+ cubic ft of conditioned/garage space; cooler air output (50°F cooler); louder; recovery is slow | 240V/30A circuit, condensate drain, 700+ cu ft of space, no closet install unless louvered |
| **Electric resistance tank** | Heating elements in tank | Cheap; no gas | Highest operating cost; slow recovery; not Title 24 compliant for new construction in most cases | 240V/30A circuit, water, drain |

#### Seismic strapping (CPC §507.2, CRC R313)

**California requirement: every water heater must be strapped at two locations** — upper third and lower third of the tank.

- Strap must be a metal strap or plumber's tape designed for the purpose (24-ga galvanized minimum, 1¼" wide).
- Anchored to wall studs with lag bolts (not drywall anchors).
- Strap must wrap around the tank and bolt to both sides.
- Tankless WHs require seismic anchoring per manufacturer instructions and CRC.

**Failure to strap is the #1 cause of post-earthquake fires** (WH falls, gas line breaks, ignition source nearby).

#### Other water heater rough-in details

- **T&P (temperature and pressure relief) discharge**: Pipe from T&P valve must run downward to within 6" of floor (or to exterior, or to indirect waste), full-size pipe (¾"), no traps, no threaded end.
- **Drain pan**: Required when WH is in attic or on a finished floor where leakage would cause damage (CPC §507.5). Pan drains to indirect waste or exterior.
- **Combustion air**: For gas WHs in a closet, two openings (high and low) sized per CPC Chapter 5, or sealed combustion (direct vent) WH.
- **Earthquake shut-off**: Some CA jurisdictions require automatic gas shutoff valve at WH (in addition to seismic shutoff at meter); check local AHJ.
- **18-inch rule** (legacy): Burners on gas WHs in garages must be 18" above floor (for fuel vapors). FVIR (Flammable Vapor Ignition Resistant) WHs may eliminate this requirement — confirm with AHJ.

### 2.6 Water Supply Pressure Test (CPC §609.4)

**Test pressure: 100 PSI static, held for 15 minutes minimum**, with no measurable drop on a 100 PSI gauge.

**Setup:**
1. All fixture stubs capped (use compression caps, threaded caps, or pressure test caps).
2. WH and any fixtures isolated (the test stresses pipe, not equipment).
3. Air bled from system (water-only test) OR pressurized with air (air test allowed by some AHJs but most CA inspectors prefer water).
4. Hand pump or test pump pressurizes to 100 PSI.
5. Note gauge, wait 15 minutes, re-check.

**What the test finds:** Loose crimps, missed solder joints, hairline cracks in fittings, manufacturer defects.

**What it does not find:** Velocity issues, sizing problems, hot/cold reversed, missed shutoffs.

### 2.7 Shut-offs

| Location | Required by code | Practical recommendation |
|---|---|---|
| **Main shut-off at meter** | Yes (utility-side) | Confirm location with utility; tag |
| **Main shut-off at building entry** | Yes (CPC §606.3) | Inside garage or in mechanical room, accessible, full-port ball valve |
| **Water heater (cold inlet)** | Yes | Ball valve, full port, accessible |
| **Each fixture** | Yes — every fixture must have a stop (CPC §606.5) | ¼-turn ball stops, not multi-turn (ball stops never freeze in place) |
| **Hose bibbs** | Yes — interior shut-off plus bibb | Ball valve inside; frost-free bibb where freezing possible |
| **Manifold (if used)** | Each line has a ball valve at the manifold | Specify ¼-turn |

**Field rule:** No fixture gets installed without a working shut-off underneath it. The plumber will tell you "the main valve is the shut-off" — that's not what the code says. Every fixture.

---

## 3. Gas

Natural gas piping is governed by CPC Chapter 12 and adopted NFPA 54 (National Fuel Gas Code). It is unforgiving — a 1/16" leak can fill a house overnight and explode. There is no "minor" gas mistake.

### 3.1 Gas Pipe Materials

| Material | Where used | Pros | Cons | Joining |
|---|---|---|---|---|
| **Black iron (Schedule 40 steel)** | Standard for fixed gas runs; exposed and concealed | Cheapest material; long-proven; mechanically rugged | Heavy; labor-intensive; threaded joints can leak; requires pipe dope rated for gas (yellow Teflon or Megaloc) | NPT threaded (with gas-rated dope or Teflon) |
| **CSST (corrugated stainless steel tubing)** | Concealed runs through framing; flex; appliance feeds (long runs) | Fast install; bends around obstacles; fewer fittings | More expensive material; requires special fittings; **bonding required**; some brands not arc-resistant | Manufacturer-specific compression fittings (HOM-Flex, OmegaFlex TracPipe, Gastite) |
| **Galvanized steel** | Allowed but uncommon | Same as black iron | Zinc flakes can clog gas valves | Threaded |
| **Copper (Type L)** | Allowed for natural gas (with sulfur-resistant coating) in some jurisdictions; widely used for **propane (LP)** | Flexible; clean install | Reacts with sulfur in some gas distribution (causes sulfide flaking); check AHJ | Solder (silver) or flare |
| **Flexible appliance connectors** | Final 6 ft connection from gas valve to appliance (range, dryer, WH) — **not for concealed runs** | Allows appliance to slide for service | Limited to 3 ft (range/dryer) or 6 ft (others) typical, depending on AHJ; **never extend with multiple connectors** | Flare fittings, factory ends |

**Practical scoping rule:** Black iron for fixed runs above ground, CSST for concealed runs through framing where flexibility helps (especially for kitchen island ranges). Each appliance gets a flex connector — but only the final connector, never an extension.

### 3.2 Gas Pipe Sizing (BTU Load Method)

Gas pipe is sized by **total connected load (BTU/hr)** and **developed pipe length** (longest run from meter to farthest appliance).

#### Common appliance loads (typical)

| Appliance | BTU/hr |
|---|---|
| Gas range/cooktop | 65,000 |
| Gas oven (built-in) | 25,000 |
| Gas range with oven | 90,000 |
| Tankless gas WH (whole house) | 199,000 |
| Tank gas WH (50 gal) | 40,000 |
| Forced-air furnace (mid-size home) | 80,000 |
| Gas dryer | 22,000 |
| Gas fireplace (decorative) | 35,000 |
| BBQ stub-out | 60,000 |
| Pool heater | 250,000–400,000 |

#### Pipe sizing approach

Use the **NFPA 54 longest-length method**:
1. Sum total BTU load of all appliances.
2. Measure longest pipe run (meter to most distant appliance).
3. Use NFPA 54 tables to size each pipe segment (must carry the cumulative BTU of all appliances downstream).

#### Simplified table — Schedule 40 black iron, natural gas (0.5 psi inlet, 0.5" w.c. drop) — common residential

| Pipe size | Length 10 ft | 30 ft | 60 ft | 100 ft | 150 ft |
|---|---|---|---|---|---|
| ½" | 172 cfh / 172,000 BTU | 99 / 99k | 71 / 71k | 55 / 55k | 44 / 44k |
| ¾" | 360 / 360k | 207 / 207k | 148 / 148k | 114 / 114k | 91 / 91k |
| 1" | 678 / 678k | 391 / 391k | 279 / 279k | 215 / 215k | 173 / 173k |
| 1¼" | 1390 / 1.39M | 801 / 801k | 572 / 572k | 441 / 441k | 354 / 354k |

(cfh = cubic feet per hour; natural gas ≈ 1,000 BTU/cf)

**Practical example:** Tankless WH (199k) at 60 ft from meter. From the table, ¾" carries 148k at 60 ft — **not enough**. Need 1" to that WH (279k at 60 ft).

**This is why most tankless installs in retrofit fail — the existing ¾" line was sized for a 40k-BTU tank WH, and the new tankless needs 199k. The plumber must either pull a new ¾" or 1" line or upsize the existing run.**

CSST sizing is different — manufacturers publish their own tables (the corrugations increase friction, so CSST is sized somewhat smaller for the same flow than the equivalent black iron). Use the manufacturer's chart.

### 3.3 Seismic Gas Shut-Off (California)

California Senate Bill 1212 and related local ordinances require **automatic seismic gas shut-off valves** in many jurisdictions and circumstances:
- **Required statewide** for any property where alterations exceed a value threshold (varies by jurisdiction; commonly $10,000+).
- **Required at sale** in some jurisdictions (Los Angeles, others — confirm local).
- **Always required** in new construction in many California cities (LA, SF, etc.).

**Location:** Downstream of the gas meter, before the first branch. Two types:
1. **Excess-flow valves** — trip when flow exceeds a threshold (e.g., line break).
2. **Motion-sensitive valves** — trip on seismic shaking (most common). Manual reset required after triggering.

**Approved brands:** Koso (KAGE), Pacific Seismic Products (PSP), Little Firefighter. Look for the CSA listing and CA-state approval.

**GC role:** Verify in plans, confirm with local AHJ before ordering, install by licensed plumber (some jurisdictions require gas utility involvement).

### 3.4 Gas Pressure Test (CPC §1213.2 / NFPA 54 §8.1)

**Test pressure: 10 PSI minimum, held for 15 minutes** with no drop on a 0–30 PSI gauge (some AHJs want longer — confirm).

**Setup:**
1. All appliances disconnected (valves at end of each line capped).
2. Test gauge installed on test tee (at meter location, or at a tee installed for the test).
3. Pressurize with air (compressor or hand pump).
4. Soap-test every joint with a leak-detection fluid (the test gauge shows total leak rate; soap finds the location).

**What it finds:** Pipe joint leaks, cracked fittings, missing caps, defective valves.

**Field practice:** Pressure-test ALL gas before walls close. Re-test after appliance connection at trim with a manometer (manifold pressure check at each appliance).

### 3.5 Appliance-Specific Gas Rough-In

| Appliance | Gas connection point | Special clearances | Vent / flue |
|---|---|---|---|
| **Range / cooktop** | Stub through floor or wall behind range, ½" or ¾" valve | 30" min above for combustibles; per range manual | Range hood (above) |
| **Wall oven** | Behind unit, ½" valve | Per manufacturer | Vent through wall or up |
| **Gas dryer** | Behind dryer, ½" valve | Min clearances per manual | 4" rigid duct to exterior |
| **Tank water heater** | At valve before WH, ¾" or larger | 6" sides; 18" front; raised burner unless FVIR | B-vent or power vent or sealed |
| **Tankless WH** | At valve, ¾" min usually | Per manufacturer; many side-vented | Category III stainless or sealed concentric |
| **Furnace (FAU)** | At valve before furnace, ½" or ¾" | 6" sides, 18" front, 24" service clearance | B-vent or sealed |
| **Gas fireplace (DV)** | Stub at fireplace, ½" valve | Per listing | Direct vent through wall or roof |
| **BBQ stub-out** | At BBQ location, ½" valve | Outdoors only | n/a (open combustion) |
| **Pool heater** | At pad, ¾" or 1" | Per manual; outdoor placement | Through-roof if indoor (rare) |

### 3.6 CSST Bonding (NEC 250.104(B) and CA amendments)

**The defect:** CSST has thin walls. A nearby lightning strike or fault current can arc through the tubing wall — gas inside, ignition source outside = explosion. Several house explosions and a class-action settlement led to bonding requirements.

**Requirement:** CSST gas piping systems must be bonded to the building's grounding electrode system with a **6 AWG copper conductor minimum** (NEC 250.104(B)).

**Bonding point:** A bonding clamp at the gas meter or just downstream, before the first CSST fitting. The bonding conductor runs to the building grounding electrode (ground rod, Ufer, or main service grounding electrode).

**Arc-resistant CSST (newer products like Gastite FlashShield, OmegaFlex Counterstrike)** have a conductive outer jacket. Some interpretations relax bonding requirements for these — but California AHJs almost universally still require bonding regardless of CSST product. Specify bonding always.

**GC role:** Confirm with plumber and electrician that bonding is installed and inspected — it's often missed because it sits at the interface between two trades.

---

## 4. Fixtures and Trim-Out

Trim is where the project becomes visible. Every wrong rough-in dimension you discover at trim costs you a fixture re-order, drywall patch, and possibly tile re-work. Get this right at rough.

### 4.1 Standard Rough-In Dimensions

| Fixture | Drain | Water supply | Other |
|---|---|---|---|
| **Toilet (standard)** | 12" from finished wall to drain center (some 10", 14") — verify model | Cold supply on left, 7" AFF, 6" left of drain center | Finished floor height critical |
| **Lavatory (vanity)** | 18" AFF for drain center | 21" AFF for supplies (hot left, cold right), 8" apart | Mirror and faucet center |
| **Pedestal lav** | Per fixture spec — usually 22–24" AFF for drain | Per fixture | No vanity to hide stub-outs — get this exactly right |
| **Wall-hung lav (ADA)** | 17–18" AFF for drain | Per fixture | 27" knee clearance, 34" rim max |
| **Tub (drop-in)** | At tub overflow per spec | Per spec, typically 8" AFF for diverter | Drain location varies by tub model |
| **Tub (alcove)** | 14" from finished wall to tub drain center | 12" from finished wall for shower diverter, 28" AFF; tub spout 4" above tub rim | Verify with manufacturer |
| **Shower (standard pan)** | 60"×32" min interior dim (CPC §408.6); drain centered | Diverter 48" AFF; shower head 80" AFF; spray bar height per design | 1500 sq in floor area minimum (CPC) |
| **Shower (barrier-free / ADA)** | 60"×60" or 36"×36" with bench | Grab bars 33–36" AFF; controls 38–48" AFF | 36" min curb-less entry |
| **Kitchen sink** | 18" AFF, centered under sink | 22" AFF, 8" apart | DW stub for tailpiece dishwasher line |
| **Dishwasher** | Air gap or high loop required | ½" hot supply, 120V circuit | Drain via air gap (CPC) or high loop (some AHJs) |
| **Washing machine** | Standpipe 18–30" AFF, P-trap 6–18" AFF | Hot + cold 42–48" AFF | Box recessed into wall (Oatey or equiv.) |
| **Hose bibb** | n/a | ¾" copper, 16" AFF exterior | Vacuum breaker required (CPC §603.5.7) |

### 4.2 CalGreen Mandatory Water Efficiency (CALGreen §4.303)

These are **mandatory** in all new residential construction in California — not optional, not stretch code.

| Fixture | Maximum flow / volume |
|---|---|
| **Showerheads** | 1.8 GPM @ 80 PSI |
| **Lavatory faucets (residential)** | 1.2 GPM @ 60 PSI |
| **Lavatory faucets (public/common areas)** | 0.5 GPM @ 60 PSI |
| **Kitchen faucets** | 1.8 GPM @ 60 PSI (may temp-burst to 2.2 GPM) |
| **Toilets (water closets)** | 1.28 GPF (HET — high-efficiency toilet) |
| **Urinals** | 0.125 GPF (HEU) or 0.5 GPF (max) |

**WaterSense label**: The simplest way to comply is to specify WaterSense-labeled fixtures. The label means EPA tested and certified.

**Verification:** The inspector will check at final — fixture flow rate is stamped on the aerator or showerhead. Have the documentation handy.

**Pitfall:** A homeowner who insists on a "rainfall" showerhead bought online from a non-US-compliant vendor will fail your inspection. Lock fixture selections to WaterSense-compliant items in your selection sheets.

### 4.3 Anti-Scald (Thermostatic / Pressure-Balance) Requirements

**CPC §408.3 / CPC §409.4**: All shower and tub-shower valves must be **pressure-balance, thermostatic, or combination** type, set to deliver water at **120°F maximum** at the outlet.

**Two types:**
- **Pressure-balance valve**: Senses pressure on hot and cold sides; if one drops (toilet flush, dishwasher fill), the valve closes the other side proportionally. Maintains temp. Cheaper.
- **Thermostatic mixing valve (TMV)**: Senses actual outlet temperature; modulates hot/cold to maintain setpoint. More accurate; required for some applications.

**At the fixture:** Every shower valve sold in the US for residential use is one or the other — you can't avoid it. The risk is improper adjustment (factory setting often higher than 120°F).

**At the water heater (alternative or supplemental):** Many jurisdictions and CalGreen recommend (or require for HPWH installations) a **thermostatic mixing valve at the water heater** to allow the tank to operate at 140°F (for Legionella control and effective capacity) while delivering 120°F to fixtures.

**GC verification:** At trim, set each shower valve's "high-limit stop" so the maximum delivered temperature is 120°F. This is a 30-second adjustment per valve — instruct your plumber to do it on every fixture and check before final.

### 4.4 Trim Sequence

| Order | Task |
|---|---|
| 1 | Drywall, tape, texture complete |
| 2 | Tile, stone, finish flooring complete |
| 3 | Cabinets installed |
| 4 | Plumbing trim — fixtures, faucets, toilets, water heater set if not already, shower trim |
| 5 | Electrical trim — devices, fixtures, fan covers |
| 6 | Appliance install |
| 7 | Punch list |
| 8 | Final inspection |

**Critical interfaces:**
- **Toilet flange height**: Must be at finished floor level (or ¼" above). If set at slab and tile is ½" thick + thinset = ¾" off — toilet rocks, wax seal fails. Either build up the flange (Oatey extender kit) or specify a thicker wax ring + flange spacer.
- **Tile-to-shower-valve plate**: Valve plate must be flush with finished tile (within ¼"). If the valve box was set too deep, the trim plate gaps; too shallow, the plate sits proud of the tile. Coordinate at rough.
- **Tub drain assembly**: The trip-lever/lift-and-turn assembly is installed before the tub. Once tub is set, the drain shoe is locked in. Verify tub model and order trim before tub goes in.

---

# PART II: ELECTRICAL

---

## 5. Service and Panel

The electrical service is the connection between the utility's wires and your building's wiring. It determines how much power the house can ever have without a service upgrade. Sizing it correctly today, especially for EV and solar, is critical — a 100A service that "works fine" today will block a heat pump conversion or EV install in 2030.

### 5.1 Service Entrance Components

**Overhead (aerial drop):**
- Utility wires from pole to house attach at a **service mast** (galvanized pipe, often 2" or 2½") secured to the roof or wall.
- Wires terminate at a **weatherhead** (curved fitting at top of mast that allows wires to drip outside before entering conduit).
- Service entrance conductors (SEC) run down inside the mast/conduit to the meter base.
- From meter base, conductors run to main service panel (often through wall directly behind meter).

**Underground (lateral):**
- Utility conduit comes up from the ground at the meter (typically PVC Schedule 80 or 40).
- Service conductors are pulled by the utility (in some areas) or by the electrician (in others — coordinate).
- Meter, then to panel.

#### Service entrance sizing

| Service size | SEC copper | SEC aluminum | Conduit (PVC Sch 40, copper) | Use |
|---|---|---|---|---|
| 100A | #4 THWN | #2 THWN | 1¼" | Small old homes; not allowed for new in most CA — minimum 200A |
| 125A | #2 | #1/0 | 1½" | Small accessory units, ADUs |
| 200A | #2/0 | #4/0 | 2" | Standard new construction in CA |
| 320/400A | 400 MCM | (paralleled or larger) | 3" or 3.5" | Large homes (5000+ sf, multiple HVAC, EV + solar + pool) |

**California standard for new construction: 200A minimum.** Many AHJs now require 200A even for ADU conversions. For homes over 4,000 sf or with multiple heat pumps + EV + solar, plan 320A or 400A.

### 5.2 Panel Sizing

| Panel | When appropriate |
|---|---|
| **100A** | Pre-1970s house; minor remodel; NOT for new construction (insufficient for EV, heat pump conversion) |
| **125–150A** | ADU, very small home, with no plans for EV |
| **200A** | New construction standard; supports EV (50A), heat pump (40A), induction range (50A), and normal load |
| **320A (400A class)** | Large home; multiple HVAC zones; EV(s) + solar + pool + spa; future-proofing |
| **400A (true)** | Estate-scale; rare in residential |

**EV upgrade reality check (2026):** A 200A panel typically has 50–80A of "free" capacity after normal residential loads. A Level 2 EV charger is 32–50A continuous. Adding two EVs to a 200A panel without load management requires careful load calc — most need an EV load manager (Span panel, ChargePoint Home Flex with load sharing) or service upgrade.

### 5.3 NEC 220 Residential Load Calculation (Standard Method, Simplified)

**Two methods**: Standard (NEC 220 Part III) and Optional (NEC 220 Part IV). Optional is easier for residential and is the default. Both give a number — **calculated demand load in amps** — which must be less than the service amp rating.

#### Standard method, NEC 220 Part III (abridged)

1. **General lighting load**: 3 VA × square footage of the dwelling.
2. **Small appliance branch circuits**: 1,500 VA per circuit, minimum 2 circuits (kitchen).
3. **Laundry circuit**: 1,500 VA.
4. **Apply demand factor** to the sum (first 3,000 VA at 100%, next 117,000 VA at 35%, remainder at 25%).
5. **Add fixed appliances** at nameplate: water heater, dishwasher, disposal, microwave, range, dryer, HVAC. Apply demand factors per Section 220.53.
6. **Add largest of: A/C OR heat** (you don't use both simultaneously).
7. Convert to amps: VA ÷ 240V = amps.

#### Optional method, NEC 220 Part IV — much easier

1. Sum **all loads** at nameplate (general lighting at 3 VA × sf, small appliance circuits, fixed appliances, range, dryer, water heater, HVAC, EVSE, etc.).
2. First 10 kVA at 100%, remainder at 40%.
3. Add 100% of largest A/C or heating load.
4. Convert to amps.

**Why the GC needs to verify this was done:** Electricians sometimes "eyeball" panel size based on similar projects. With EV chargers, induction ranges, heat pump water heaters, heat pumps, and pool/spa loads, modern California homes are pushing 200A. Get the written load calc in the permit package and confirm it.

### 5.4 Main Breaker vs. Main Lug; Subpanel Rules; 6-Disconnect Rule

#### Main breaker panel (MBP) vs. main lug panel (MLP)

| Type | Has main breaker? | Use |
|---|---|---|
| **Main breaker panel** | Yes — single breaker disconnects all branch breakers | Service entrance panel (must have a main breaker or qualify under 6-disconnect rule) |
| **Main lug panel** | No — lugs only; fed from upstream disconnect | Subpanels fed from a separately enclosed main disconnect |

#### Subpanel rules (NEC 408 and 250.32)

When a subpanel is fed from the main panel via a feeder, four-wire feed is required:
- **Hot 1, Hot 2** (240V)
- **Neutral** — insulated, NOT bonded at subpanel
- **Ground (equipment grounding conductor)** — bonded to subpanel enclosure

**The most common subpanel mistake**: bonding neutral to ground at the subpanel. Neutrals and grounds are bonded **only at the service entrance**. At a subpanel, the neutral bus must be **isolated from the enclosure** (remove the bonding screw or strap).

#### 6-disconnect rule (NEC 230.71)

Up to 2022 NEC: Service can have up to 6 disconnects without a single main breaker (e.g., 6 main breakers in a row).

**2020 NEC and later (and now CA): Each service must have a single main disconnect.** No more "six disconnect" panels in new construction. There must be one breaker (or pull) that kills everything in the building.

This affects how you specify panels — for new construction, always specify a panel with a single main breaker, sized appropriately.

### 5.5 Grounding and Bonding (NEC 250)

The most-misunderstood part of residential electrical. **Grounding** = connecting the system to earth. **Bonding** = connecting metallic parts together so they're at the same potential.

#### Grounding electrode system (GES)

Every service requires at least **two grounding electrodes** in California (typically):
1. **Concrete-encased electrode (Ufer)** — 20 ft of bare #4 copper or larger in the concrete footing, exposed at one end for connection. Required for new construction.
2. **Ground rods (two)** — 8-ft copper-clad rods driven full depth, spaced 6+ ft apart, connected with bare #6 copper.
3. **Metal water pipe** (if more than 10 ft underground metal) — bonded with #4 or larger.
4. **Building steel** — if structural steel is electrically continuous.

The Ufer alone is often sufficient (resistance to ground is much lower than rods). But two electrodes are typically required.

#### Grounding electrode conductor (GEC)

The conductor from the service neutral/ground bus to the grounding electrode(s).
- To ground rod: **#6 copper minimum** (sized down because rods aren't a great electrode).
- To Ufer: **#4 copper** typically.
- To water pipe: **#4 copper** typically.

#### Equipment grounding conductor (EGC)

The green wire (or bare wire) in every branch circuit. Connects all metal enclosures, boxes, conduit, and the third prong of receptacles back to the panel.
- Sized per NEC 250.122 by the circuit's overcurrent device.
- 15A circuit → #14 EGC; 20A → #12; 30A → #10; 50A → #10; etc.

#### Bonding

- **Main bonding jumper**: At the service equipment, neutral bus is bonded to the enclosure (and ground bus). This is the only place neutral and ground are connected.
- **Equipotential bonding**: Metal water pipe, gas pipe (CSST especially), structural steel, swimming pool equipment, separately derived systems (transformers, generators). Each has its own NEC section.

### 5.6 2022 NEC / 2022 CEC Residential Highlights

California adopts the NEC as the California Electrical Code (CEC) with state amendments. Current code: 2022 CEC (effective 2023). Notable changes from the 2017/2019 cycle:

| Requirement | What changed |
|---|---|
| **AFCI expansion** | All 15A and 20A 120V circuits in dwelling units now require AFCI (except specific exclusions — bathrooms, garages, outdoor) |
| **GFCI expansion** | Now required for all 125V single-phase 15A/20A receptacles in laundry areas, kitchen (all within 6 ft of sink), dishwasher (dedicated GFCI breaker or receptacle), basements (all 125V), garages (all), outdoor, bathrooms, crawl spaces, etc. |
| **Whole-house surge protective device (SPD)** | Required at service equipment for all dwelling units (NEC 230.67). Type 1 or Type 2 SPD on the service panel. |
| **Tamper-resistant receptacles** | All 15A and 20A 125V receptacles in dwelling units (with limited exceptions — appliance receptacles, garage attic, etc.) |
| **EV charging readiness** | 1+ EV-ready space in new garages (California amendment) |
| **Emergency disconnect** | Single outdoor emergency disconnect required for one- and two-family dwellings (NEC 230.85) |

**Outdoor emergency disconnect (230.85)**: A new 2020 NEC requirement, in effect in CA now. A disconnect on the exterior of the dwelling (so firefighters can de-energize the building from outside). Can be the meter-main combo, or a separate disconnect adjacent to the meter. Has changed how service equipment is specified — meter-main combos with main breaker and built-in disconnect are now standard.

---

## 6. Rough-In Wiring

Rough wiring is everything between the panel and the boxes — wire, staples, holes through framing, low-voltage cabling. Once drywall covers it, fixing anything requires opening the wall. This is where the GC has the most influence on quality and the most opportunity to prevent problems.

### 6.1 Wire Types and Ratings

| Wire type | Description | Where allowed | Notes |
|---|---|---|---|
| **NM-B (Romex)** | Non-metallic sheathed cable; black outer jacket; THHN conductors inside | **Allowed in residential** (dwelling units, accessory buildings); in walls, attics, crawl spaces | Most common residential wiring; rated 60°C ampacity for sizing |
| **UF-B (underground feeder)** | NM with sunlight/moisture-resistant jacket | Direct burial; wet locations; underground | Used for buried circuits to detached structures, post lights |
| **THHN/THWN-2** | Single conductor, plastic jacket | **In conduit** only (EMT, PVC, etc.) | Required where exposed to physical damage, in commercial, in service entrance |
| **MC (metal-clad cable)** | Aluminum or steel armor; insulated conductors inside | Allowed in residential; common in some markets (Northeast) | Less common in CA residential; required in some commercial |
| **AC (BX)** | Armor-clad with bonding strip | Allowed; common in older installations | Legacy; rarely specified new |
| **SE / SER / SEU (service entrance)** | Service entrance cable | Service entrance, subfeeders | Sometimes used for subpanel feeds in lieu of conduit |

**When conduit is required in residential (CA):**
- Service entrance conductors (exterior).
- Underground feeders (unless UF cable, direct buried).
- Garage walls in some jurisdictions (impact protection up to a certain height).
- Exposed wiring in attics or crawl spaces where subject to damage (within 6 ft of attic hatch).
- Risers from underground to a service panel.
- Wherever NM-B is exposed to physical damage.

**Wire color conventions (residential):**
- Black, red — hot (ungrounded)
- White — neutral (grounded)
- Green, bare — ground (equipment grounding)
- Blue, yellow — used for travelers in 3-way switches, or in 240V systems

### 6.2 Box Fill Calculations (NEC 314.16)

Every junction box must be sized to hold the conductors, devices, and clamps inside it without overcrowding. This is a top-five rough-inspection failure.

#### Box fill volume allowances

| Conductor size | Volume per conductor |
|---|---|
| #14 | 2.00 in³ |
| #12 | 2.25 in³ |
| #10 | 2.50 in³ |
| #8 | 3.00 in³ |
| #6 | 5.00 in³ |

#### Counting conductors

| Item | Counts as |
|---|---|
| Each insulated conductor entering and leaving the box | 1 conductor |
| All grounding conductors (regardless of how many) | 1 conductor |
| All internal cable clamps (collectively) | 1 conductor |
| Each yoke / strap (device — receptacle, switch) | 2 conductors (or 4 if equipped with a "double yoke" item like a paddle fan switch with multiple gangs) |
| Each support fitting (fixture stud, hickey) | 1 conductor each |

#### Example

A single-gang box with one 14-2 NM coming in, one 14-2 going out, one duplex receptacle, internal clamps:
- Conductors: 14-2 in = 2; 14-2 out = 2 → 4 #14 conductors = 4 × 2.00 = 8.00 in³
- Grounds: 1 #14 = 2.00 in³
- Clamps: 1 #14 = 2.00 in³
- Device: 2 × #14 = 4.00 in³
- **Total: 16.00 in³**

A standard plastic single-gang "new work" box is 18 in³ — OK with 2.0 in³ margin. A metal 4"×4" with mud ring is 21+ in³.

**Practical rule:** For a switch box with a 3-way switch and one cable in + one out, you're full at 18 in³. For 3+ cables, specify deep boxes (4 in deep, 24+ in³).

### 6.3 Circuit Layout — Dedicated and General Circuits

#### Dedicated circuits required by code (NEC 210)

| Load | Circuit size | Notes |
|---|---|---|
| **Refrigerator** | 15A or 20A | Often run on a small-appliance branch circuit (allowed), but dedicated is best practice |
| **Dishwasher** | 15A (most) or 20A | GFCI required (CEC 210.8); dedicated |
| **Disposal** | 15A or 20A | Dedicated; switched at sink |
| **Microwave (built-in)** | 20A | Dedicated; AFCI if in kitchen branch |
| **Range/cooktop (electric)** | 40A or 50A 240V | Dedicated; #8 or #6 wire |
| **Wall oven (electric)** | 30A or 40A 240V | Dedicated |
| **Dryer (electric)** | 30A 240V | Dedicated; 4-wire (hot/hot/neutral/ground) |
| **Laundry (washer + outlets)** | 20A | NEC 210.11(C)(2) — dedicated 20A branch for laundry receptacles |
| **Bathroom receptacles** | 20A | NEC 210.11(C)(3) — separate 20A circuit for bath receptacles (can serve multiple baths) |
| **Small appliance branch circuits (kitchen, pantry, dining)** | 20A × 2 minimum | NEC 210.11(C)(1) — 2+ circuits for countertop receptacles |
| **HVAC** | Sized per equipment nameplate (typically 240V, 15A–60A) | Dedicated per unit |
| **Furnace (FAU) blower** | 15A or 20A 120V | Dedicated if separate from compressor |
| **Garage** | 20A | At least one 20A circuit for garage receptacles (CEC 210.11) |
| **EV charger** | 40A or 50A 240V | Dedicated; see Section 7 |

#### General lighting and receptacle circuits

- NEC 210.11: General lighting load = 3 VA × dwelling area; sized at 15A or 20A circuits.
- Practical: **About 1 circuit per 600 sf of dwelling** is typical for general lighting/receptacles (some electricians go denser).
- Most rooms: lighting and receptacles can share circuits (except bath, kitchen, laundry, garage, basement, outdoor which have specific rules).

**A typical 2,400 sf, 3-bed, 2-bath home has roughly:**
- 20+ branch circuits (12–14 for general lighting/receptacles)
- 6+ dedicated circuits (DW, disposal, microwave, range, dryer, HVAC, laundry, bath)
- 2 small-appliance branch circuits
- 1+ EV-ready circuit
- 1 outdoor circuit, 1 garage circuit
- Total 32–40 spaces in panel, 200A panel typical

### 6.4 Stapling and Support

Per NEC 334.30 (NM-B specifically):

| Location | Support spacing |
|---|---|
| Within 12" of every box / fitting | Mandatory staple within 12" |
| Along framing | Every 4½ ft (54") max |
| Through holes in framing members | Bored hole acts as support; staples not required at every member |
| Vertical runs in stud bays | Every 4½ ft |
| Drop ceilings (not allowed for NM concealed unsupported above grid) | Must be supported by an independent means |

**Staple type:** Insulated staples (with plastic saddle) protect the cable jacket from being cut. Use 1" staples for one or two NM cables; "stack-it" plastic staples for parallel runs.

**Common defect at inspection**: Cables left dangling between studs without staples, "double-stack" runs without parallel staples, staples driven through the cable jacket (especially with metal staples).

### 6.5 Penetration Fire-Blocking

NEC 300.21 and CRC R302 (fire-resistance-rated assemblies) require sealing penetrations through:
- Fire-rated walls and floors (1-hour, 2-hour assemblies — typically garage-to-house, multifamily party walls, attached ADU walls).
- Top plates and bottom plates of bearing walls (CRC R302.11 — draftstopping).
- Penetrations through floor assemblies between stories.

**Methods:**
- **Intumescent firestop caulk** (3M Fire Barrier, STI SpecSeal) — expands when heated to seal the gap.
- **Firestop putty** — moldable; for irregular penetrations.
- **Firestop pillows** — for large openings or future-access penetrations.
- **Metallic raceway sleeves** — for runs through fire-rated floors.

**Critical interfaces:** Where ANY penetration (wire, pipe, duct) goes through a fire-rated wall (especially the garage common wall), the penetration must be sealed per UL listing of the firestop product. The garage-to-house wall is the #1 missed item in residential — Romex through the wall not sealed is a fail.

**GC field check before drywall:** Walk every fire-rated wall (typically marked on plans), confirm every penetration is sealed with intumescent or rated putty. Take photos.

### 6.6 AFCI Requirements (CEC 210.12)

**Arc-Fault Circuit Interrupters** detect the signature of an arcing fault (loose connection, damaged wire) and trip before fire ignition. Required in many residential locations.

#### AFCI-protected locations (CEC 210.12, 2022 cycle)

| Location | AFCI required |
|---|---|
| Kitchens | Yes (15A and 20A 120V outlets) |
| Family rooms, living rooms, dens, libraries | Yes |
| Dining rooms | Yes |
| Bedrooms (all) | Yes |
| Closets | Yes |
| Hallways | Yes |
| Laundry areas | Yes |
| Sunrooms, rec rooms | Yes |
| Garages | Yes (2020 NEC change; verify in CEC) |

**Exceptions:** Bathrooms (GFCI only), outdoor receptacles (GFCI only), some specific appliance receptacles.

**Implementation:** AFCI breaker (in panel) is most common. AFCI receptacle (first outlet on circuit) is an alternative in some cases — but the wiring method must comply with NEC 210.12(B) special wiring requirements.

#### Dual-function AFCI/GFCI

For circuits requiring both AFCI and GFCI (e.g., kitchen branch circuits — required to be both), use a **dual-function AFCI/GFCI breaker** (Square D, Eaton, Siemens, Leviton all make these). Slightly more expensive (~$50 vs. $40 single) but eliminates the need for both a breaker and a GFCI receptacle on the same circuit.

### 6.7 GFCI Requirements (CEC 210.8)

**Ground-Fault Circuit Interrupters** detect imbalance between hot and neutral (current going to ground via a person, water, or fault) and trip in milliseconds. Required everywhere water + people might intersect.

#### GFCI-required locations (CEC 210.8, 2022 cycle)

| Location | All receptacles or specific? |
|---|---|
| Bathrooms | All 125V 15/20A receptacles |
| Kitchens | All receptacles within 6 ft of sink edge; also dishwasher; also pinch points like countertop receptacles |
| Garages | All 125V 15/20A receptacles |
| Outdoor receptacles | All |
| Crawl spaces (at or below grade) | All |
| Unfinished basements | All |
| Boathouses, boat hoists | All |
| Pool, spa, hot tub equipment | All; specific requirements per NEC 680 |
| Laundry areas | All |
| Indoor damp/wet locations | All |
| Within 6 ft of sink (bathroom, laundry, wet bar) | All |
| Within 6 ft of bathtub or shower stall | All |

**Implementation:** Either a GFCI receptacle (at the first outlet on the circuit, with downstream "load" terminals feeding additional receptacles) or a GFCI breaker.

**Common mistake:** Wiring downstream of a GFCI receptacle without using the load terminals — downstream outlets aren't protected. The inspector tests every receptacle for GFCI trip.

### 6.8 Low-Voltage Rough

Structured wiring for data, coax, audio/video. Even in a wireless-everything world, you regret skipping structured wiring later.

**Structured wiring panel:**
- 30"×16"×4" deep recessed cabinet typical (Leviton, Legrand, On-Q).
- Location: central, accessible (not behind a TV), with 120V outlet inside or nearby, ventilation.
- Hosts: Cat 6 patch panel, coax splitter, ONT (fiber optic terminal), Wi-Fi router, network switch.

**Cat 6 / Cat 6a runs:**
- Home-run from each data outlet back to the panel — never daisy-chain or splice.
- Each data outlet typically gets 1 or 2 drops.
- Useful locations: every TV (wired Ethernet beats Wi-Fi for streaming), each office, each bedroom, each Wi-Fi access point location (ceiling-mounted APs need PoE), security system head-end, doorbell.
- Cat 6a (10G capable) is the future-proof choice; Cat 6 is acceptable.

**Coax (RG-6 quad shield):**
- Home-run from each TV/cable jack back to panel.
- Less critical than 10 years ago (streaming has replaced cable for most), but still useful for satellite, OTA antenna distribution.

**Speaker wire and HDMI:**
- Pull 16/4 or 14/4 stranded speaker wire to in-ceiling/in-wall speaker locations.
- HDMI in-wall: use CL2- or CL3-rated cables; pull a string for future re-pulls.

**Separation from line voltage (CEC 800.133):**
- Low-voltage cables must be separated from 120/240V cables by at least 2 inches when run parallel (or in different stud bays).
- Where they cross, they may cross perpendicularly (90°) at the crossing point.
- **Never share a stud bay running parallel with NM-B.** Induction noise on data lines causes intermittent network drops that are impossible to diagnose later.

**Field rule:** Low-voltage trade typically runs after framing, before insulation, in parallel with electrical rough. Insist on a written low-voltage scope and walk-through with the LV trade before drywall — pulling cable through finished walls is 5–10× the cost of pulling at rough.

---

## 7. Specialty Circuits

The four specialty circuits that increasingly define modern residential: EV, solar, backup power, and pool/spa. Each has unique code, scope, and coordination requirements.

### 7.1 EV Charging (California Mandate)

California Title 24 (effective 2020 cycle, current 2022) requires every new single-family home to be **EV-ready**:

| Term | Definition | What it requires |
|---|---|---|
| **EV-capable** | Conduit only, no wiring | 1" conduit from panel to garage, blank cover at panel and garage; reservation of one panel space and dedicated circuit allowance in load calc |
| **EV-ready** | Conduit + wiring + outlet | All of the above + circuit wired + NEMA 14-50 receptacle (50A 240V) or hardwired EVSE box installed |
| **EVSE-installed** | Charger physically installed | EV-ready + actual EVSE unit (Tesla Wall Connector, ChargePoint, JuiceBox, etc.) |

**California 2022 mandate (Title 24 §150.0(o) + CalGreen):**
- **One** EV-ready space required in every new single-family home garage.
- ADUs: at least EV-capable.

Many cities (Berkeley, Oakland, others) require EV-ready (not just capable) and sometimes multiple spaces.

**Practical rough-in:**
1. 50A double-pole breaker space reserved.
2. **#6 NM-B** (or #6 THHN in conduit) from panel to garage termination point.
3. Conduit (¾" or 1") if running through wall cavities; not strictly required if NM-B.
4. NEMA 14-50 outlet (50A 240V — flush mount, 48" AFF typical) OR hardwired junction box for EVSE.
5. If using a smart EVSE with load management (Span panel, ChargePoint w/ load share), specify accordingly.
6. GFCI protection: NEC 625.54 requires GFCI for receptacle-connected EVSEs. (Hardwired EVSE typically has integrated GFCI.) This is a recent code addition; verify with electrician.

### 7.2 Solar PV — What the GC Needs to Know

You won't be installing the solar (separate contractor, often with own permit). But you must rough in for it and coordinate the interface.

#### Components

| Component | What it is |
|---|---|
| **Modules (panels)** | The PV cells on the roof |
| **Inverter(s)** | DC-to-AC conversion. Two flavors: **string inverter** (one large unit, panels wired in series) and **microinverters / DC optimizers** (one per panel) |
| **DC disconnect** | Required at the inverter or array; trips DC supply |
| **AC disconnect** | Required between inverter and main panel; gives utility a single point to de-energize |
| **Production meter** | Measures total energy production (sometimes required by utility) |
| **Net meter** | Bi-directional utility meter that records imported and exported energy |
| **Rapid shutdown** | NEC 690.12 — required for rooftop PV; de-energizes panels to safe voltage in 30 seconds |
| **Battery (optional)** | LiFePO4 or other storage; sized in kWh; with its own inverter |

#### Interconnection types

| Method | Description | NEC reference |
|---|---|---|
| **Supply-side (line-side) tap** | PV connects between meter and main breaker; bypasses the main panel | NEC 705.11 |
| **Load-side (back-feed) breaker** | PV connects via a dedicated breaker in the main panel; subject to the **120% rule** | NEC 705.12 |
| **120% rule** | Sum of main breaker + back-fed PV breaker ≤ 120% of panel bus rating. Example: 200A panel + 200A main + 40A PV breaker = 240A ≤ 240A (120%) — OK | NEC 705.12(B)(3)(2) |

#### What the GC roughs in (current or future)

- **Conduit** from PV inverter location to main panel — typically ¾" or 1" EMT or PVC.
- **Conduit** from roof attic to inverter (for DC wiring from array) — typically 1" or larger.
- **Mounting block** or solar-ready zone marked on the roof per Title 24 §110.10.
- **Panel space** reserved (a backfed breaker space on the opposite end from the main).
- **Outdoor disconnect** location near the meter — coordinated with the utility.

**California Title 24 solar mandate:**
All new low-rise residential (3 stories or fewer) requires solar PV — Title 24 §150.1(c)14. Size: varies, typically 2–4 kW for a typical home. ADUs are typically exempt depending on size.

### 7.3 Emergency / Backup Power

Three approaches, very different in scope and cost.

#### A. Generator with manual transfer switch

- Standalone generator (portable or fixed) feeding a **manual transfer switch** (MTS).
- Cheapest; OK for occasional power outages.
- MTS is wired into the home's panel, typically powering a subset of "essential" circuits.
- Interlock kit alternative: A mechanical interlock on the main panel preventing the main breaker and a back-feed breaker from being on simultaneously. Cheaper than MTS but limited to small loads. Code-acceptable in most CA jurisdictions if listed for the panel.

#### B. Whole-home standby generator with automatic transfer switch (ATS)

- Permanently installed generator (Generac, Kohler, Briggs — typically 14–26 kW for residential).
- LP or natural gas fueled (NG preferred — no fuel tank).
- ATS senses utility loss, starts generator, transfers load automatically.
- Whole-home or essential-loads sub-panel options.
- Rough-in: concrete pad (3'×5'), gas line to genset, 200A or 100A ATS adjacent to main panel, exhaust away from windows/doors (CRC §M1804).
- Cost installed: $10K–$25K depending on size.

#### C. Battery backup (with or without solar)

- Lithium battery storage (Tesla Powerwall, Enphase IQ Battery, Generac PWRcell, FranklinWH).
- Integrated with main panel via a **whole-home backup gateway** or **partial-backup subpanel**.
- Can be combined with solar for self-consumption + backup.
- Rough-in: location (garage wall, outdoor enclosure), conduit to main panel, communication wire (CAT5/Cat6 to internet for monitoring), local disconnect.
- Cost: $10K–$30K per battery installed.

**California reality:** With PSPS (Public Safety Power Shutoff) events common in fire-prone zones and time-of-use rates, battery storage is becoming standard in new construction in CA — especially Tier 2/3 fire zones.

### 7.4 Pool and Spa (NEC 680)

NEC Article 680 is its own world. The #1 cause of pool-related electrocutions historically has been improper bonding. Get this right or someone dies — and you go to jail.

#### Key concepts

| Requirement | What it means |
|---|---|
| **Equipotential bonding grid** | All metallic parts within 5 ft of the inside pool wall (rebar, ladders, handrails, light niches, pumps, motors, even the deck rebar) must be bonded together with #8 solid copper to a common bonding lug. This eliminates voltage differences. |
| **GFCI on pool circuits** | All 120V receptacles within 20 ft of pool, all underwater lights (low-voltage), all pump motors (NEC 680.21) |
| **Receptacle placement** | No receptacle within 6 ft of pool edge; 6–20 ft must be GFCI |
| **Listed equipment** | Pool pump motors, lights, etc. must be listed for pool/spa use |
| **Bonded conductive deck** | Concrete deck within 3 ft of pool must be bonded (rebar grid + bonding wire) |
| **Equipment clearance** | Heater clearances per manufacturer; service clearance for pumps |

**The equipotential bonding grid is the #1 missed item.** During pool excavation/rebar, the bonding grid must be installed before concrete pour, with a bonding lug brought out for connection to pool equipment. If skipped, the only fix is to demo and replumb. Verify with the pool sub and the electrician at rebar stage.

**Spa/hot tub:**
- Self-contained spa: 240V/50A dedicated, GFCI breaker, within 5 ft of disconnect, equipotential bonding similar to pool.
- Built-in spa: treated as a small pool — full NEC 680.

---

## 8. Devices, Fixtures, and Trim-Out

### 8.1 Device Heights (Standard and ADA)

| Device | Standard residential height (to center of box) | ADA / accessible |
|---|---|---|
| **Receptacles (general)** | 12–18" AFF (16" is common) | 15" AFF minimum, 48" AFF max |
| **Receptacles (kitchen counter)** | 4" above counter (44" AFF typical with 36" counter) | Per design; reachable |
| **Receptacles (laundry, garage)** | 42–48" AFF (wash receptacle = 42") | n/a |
| **Receptacles (outdoor)** | 12–18" AFF, weather-resistant box | n/a |
| **Switches** | 48" AFF to center | 48" AFF max (top of switch) |
| **Thermostat** | 60" AFF | 48" AFF max |
| **Smoke / CO detectors** | Ceiling, or wall ≥4" from ceiling and within 12" of ceiling | n/a |
| **Light fixture (vanity)** | Per design; typical 78–80" AFF for sconces | n/a |
| **Doorbell button** | 44–48" AFF | 48" AFF max |
| **Cable / data outlets** | Match receptacle height; or per design | n/a |
| **Floor outlets** | Floor level; recessed in floor box | n/a |

**Consistency rule:** Within one project, pick a standard height for receptacles and switches and don't let trades deviate without permission. Variation between rooms looks sloppy and is the #1 walkthrough complaint.

### 8.2 Smoke Detectors (CRC R314)

**Required locations:**
- Inside **each sleeping room**.
- Outside each sleeping area (in the hallway/space serving the bedrooms).
- On **every story** of the dwelling, including basements.
- Within 36" of the door of a sleeping room.

**Power and interconnection (CRC R314.4):**
- **120V hardwired with battery backup** required in new construction.
- All smoke alarms must be **interconnected** so that activation of one sounds all.
- In existing buildings undergoing alteration, wireless interconnection may be allowed (depending on AHJ).

**Type (CA-specific):**
- **Photoelectric** preferred for smoldering fires; required for placement within 20 ft of a kitchen or bathroom (to reduce nuisance trips from cooking/steam).
- **Ionization** detects flaming fires faster (but more nuisance-prone).
- **Dual-sensor** (photoelectric + ionization) is best in most locations.

**Combination smoke/CO** (e.g., First Alert SC9120B, Kidde) is acceptable and reduces device count.

### 8.3 CO Detectors (CA H&S Code 17926 + CRC R315)

Required in dwellings with:
- Any fuel-burning appliance (furnace, water heater, fireplace, stove).
- An attached garage.

**Locations:**
- Within **3 feet** of each **sleeping area** entrance (hallway outside bedrooms).
- On **every story** of the dwelling, including basements.
- Within 10 ft of each sleeping room door per some local AHJs.

**Type:** Battery-operated OK in existing; **hardwired with battery backup** required in new construction. Often combined with smoke detector.

### 8.4 Tamper-Resistant Receptacles (CEC 406.12)

**Required for all 15A and 20A 125V receptacles in dwelling units** — bedrooms, living areas, bathrooms (interior of), kitchens, hallways, basements, garages, etc.

**Exceptions:**
- Receptacles more than 5½ ft above the floor.
- Receptacles dedicated to specific appliances (refrigerator, range, dishwasher) and inaccessible.
- Receptacles in attic, crawl space (not commonly used).

**Identification:** TR receptacles have "TR" embossed on the face. They have spring-loaded shutters that block insertion of foreign objects unless both contacts are pushed simultaneously.

**Cost:** ~$1 more than standard. Specify TR for all dwelling receptacles in spec — no exceptions during install.

### 8.5 Panel Schedule and Labeling

CEC 408.4 and 110.22 require:
- **Each circuit breaker labeled** with circuit identification (location and function).
- **Panel schedule on the door** (printed legibly, durable — no Sharpie that fades).
- **Service equipment** identified as such ("Service Disconnect" on outdoor disconnect).
- **All disconnect switches** clearly marked.

**As-built accuracy:**
- The panel schedule must reflect what was actually installed, not what was planned. Trades often guess during install and never update.
- Best practice: **field-trace every circuit** at end of project with a circuit tracer (Greenlee, Klein) — one person at the panel turning off breakers, one at receptacles testing. Label the panel based on actual results.
- Hand the homeowner a typed panel schedule (in a sleeve on the panel door) plus a copy in the closeout binder.

**Final inspection:** Inspector checks panel for labeling, AFCI/GFCI function (test buttons), proper torque on breakers (some AHJs require torque records).

---

# PART III: MECHANICAL / HVAC

---

## 9. Load Calculations

HVAC sizing is the most-faked and most-consequential part of mechanical scope. An oversized system short-cycles, fails to dehumidify, wears out faster, and costs more. An undersized system can't meet load on design days. The "rule of thumb" of 1 ton per 500 sf is wrong half the time.

### 9.1 Manual J (Residential Load Calculation)

ACCA Manual J is the residential industry standard. **Most California AHJs require a Manual J on file for new construction and major HVAC replacements.**

#### Inputs

| Input | What it is | Sensitivity |
|---|---|---|
| **Conditioned floor area** | Square footage of conditioned space | Moderate |
| **Climate zone** | California has 16 climate zones (Title 24); each has a design day for heating and cooling | High |
| **Insulation values (R-value)** | Walls, ceiling, floor, slab edge | High |
| **Window area, orientation, SHGC, U-value** | South/west glass drives summer load; north/east drives winter | Very high |
| **Infiltration rate (ACH50)** | Air leakage measured by blower door; modern tight homes are 2–3 ACH50, leaky homes 10+ | High |
| **Internal gains** | Occupants, lights, appliances | Moderate |
| **Duct location** | Conditioned space (no penalty) vs. attic (huge penalty in CA, 20–30% extra load) | High |
| **Latent load** (humidity) | Less critical in dry CA than humid climates | Low in CA inland, moderate on coast |

#### Output

A heating load and a cooling load, each in **BTU/hr** at the design day temperature.

**Equipment sizing:**
- Cooling: equipment selected at **100–115%** of cooling load.
- Heating: equipment selected at **100–125%** of heating load (heat pumps may be sized to balance point and supplemented with strip heat or gas backup).
- **Never** select equipment based on "1 ton per X sf" — this is a 30-year-old rule of thumb from when homes were leaky, single-pane, and oversized to compensate.

**Why GCs care:** The HVAC sub may run a calculation, or may guess. The GC must verify a Manual J was performed (it's in the permit set in most CA jurisdictions) and that the proposed equipment matches. **Oversizing by 50% is common, harms comfort, and wastes the owner's money.**

#### Real-world sizing example

A 2,400 sf well-insulated new CA home in climate zone 12 (Sacramento valley):
- Manual J cooling load: ~24,000 BTU/hr = 2.0 tons
- Manual J heating load (heat pump): ~22,000 BTU/hr
- Old rule of thumb: 2,400 sf / 500 = 4.8 tons → 50 SEER2 unit
- Correct sizing: 2 tons, or 2.5 tons max
- **A 4-ton unit on a 2-ton load short-cycles every 5 minutes, never dehumidifies, dies in 8 years.**

### 9.2 Manual D (Duct Design)

Manual D sizes the ductwork based on:
- **Total airflow** required (CFM = BTU/hr ÷ ΔT — typically 400 CFM per ton cooling).
- **Static pressure budget** — the blower fan can produce a certain pressure (typically 0.5" w.c. at high speed); the duct system must operate within that.
- **Velocity** — supply trunks 700–900 fpm, branches 500–700 fpm, return 400–600 fpm.

**Why GCs care:** Mis-sized ducts cause:
- Noisy supply (too small, too fast)
- Poor distribution (some rooms hot, some cold)
- Restrictive returns (over-pressurized supply, blower strain)
- Failing HERS duct leakage test

Common mistakes that the GC should catch:
- 6" supply duct to a master bedroom that needs 130 CFM (needs 7" or 8").
- Single 14" return for a 3-ton system (needs 16" or two 14").
- Kinked flex duct counted at full length (kinks reduce flow by 50%+).

### 9.3 Manual S (Equipment Selection)

Manual S matches actual equipment to the load.
- Picks a specific AC/HP/furnace model.
- Verifies that the equipment **at the design conditions** delivers ≥100% but ≤115% of cooling load and ≥100% (HP: 100–125%) of heating load.
- Uses manufacturer **expanded performance data** at design temperatures (not nameplate rating, which is at AHRI 95°F / 47°F).

**Why GCs care:** The HVAC sub picks equipment from a catalog. The catalog rating is at standardized AHRI conditions. At actual local design conditions (e.g., 105°F summer in inland CA), the unit may deliver 85% of its rated capacity. Manual S accounts for this.

### 9.4 California Title 24 HVAC Efficiency Requirements

Title 24 mandates minimum efficiency for HVAC equipment. Numbers update each cycle.

| Equipment | Minimum (2022 cycle, simplified) | Notes |
|---|---|---|
| **Split AC** | **SEER2 ≥ 13.4** (most CA climate zones); some zones SEER2 ≥ 14.3 | SEER2 is the new (2023+) test standard; previously SEER |
| **Split heat pump** | **SEER2 ≥ 14.3, HSPF2 ≥ 7.5** (varies by zone) | New federal minimums effective 2023 |
| **Gas furnace** | **AFUE ≥ 81%** (federal min, was 80%); some specs higher | Condensing furnace needed for >90% AFUE |
| **Heat pump WH** | UEF ≥ 2.0+ (Title 24 supports HPWH) | Tank capacity considerations |
| **Mini-split** | **SEER2 ≥ 14.3 cooling, HSPF2 ≥ 8.5 heating** typical | Higher SEER2 ratings common (18, 22, 30+) |

**Title 24 prescriptive vs. performance:** Most projects use the **performance compliance method** with software (EnergyPro, CBECC-Res). The HVAC selection is one input — the energy model balances HVAC, envelope, windows, water heating, lighting. Discuss with your Title 24 consultant before locking in equipment.

---

## 10. Forced Air Systems

The dominant residential HVAC type in CA: a central system with refrigerant-cooled air, distributed through ductwork, with heating from a gas furnace, heat pump, or backup electric strip.

### 10.1 Equipment Types

| System | Description | Pros | Cons | CA fit |
|---|---|---|---|---|
| **Gas furnace + split AC** | Outdoor condenser + indoor coil over furnace; gas heat, electric cool | Cheapest install; familiar | Gas dependency; lower heating efficiency; Title 24 increasingly restrictive | Common but declining |
| **Heat pump (air-to-air, split)** | Outdoor unit + indoor air handler; refrigerant reverses to heat or cool | All-electric; high efficiency; eligible for incentives; works well in CA | Higher install cost; may need auxiliary heat in coldest CA zones | **Standard for new CA construction** |
| **Dual fuel (HP + gas)** | Heat pump for primary; gas furnace as backup when temps below ~30°F | Best efficiency + reliability in cold zones | Most complex; two systems | Mountain zones only |
| **Packaged unit (rooftop or side-yard)** | All components in one cabinet outdoors; ducts run inside | Saves indoor space | Less efficient (longer duct runs through unconditioned air) | Common in flat-roof homes, ADUs |
| **Geothermal (ground-source HP)** | Heat pump using ground loop instead of outdoor air | Highest efficiency | Highest install cost; not common in CA residential | Rare |

### 10.2 Refrigerant Line Sets

The copper tubing connecting outdoor unit to indoor coil. Two lines:
- **Liquid line** (smaller, ¼"–⅜"): high-pressure liquid refrigerant from condenser to evaporator.
- **Suction line** (larger, ½"–¾", insulated): low-pressure vapor returning from evaporator to compressor.

#### Sizing and routing

| Issue | Why it matters |
|---|---|
| **Line set length** | Manufacturers specify max length (typically 50 ft standard, up to 150 ft with additional refrigerant charge). Beyond max = won't work or void warranty. |
| **Vertical lift** | Compressor must lift oil up suction line; max lift typically 25–40 ft. Beyond = oil traps required. |
| **Insulation** | Suction line MUST be insulated (¾" closed-cell, Armaflex) over its entire length. Bare suction line drips condensation, kills efficiency, can ice up. |
| **Routing** | Avoid sharp bends (no <6" radius), kinks, traps; secure every 4–5 ft; protect from UV (outdoor portions); seal penetrations |

**Common defects:**
- Insulation damaged at penetrations through walls (UV-degraded, rodent-chewed).
- Sharp bend at outdoor unit causes turbulence, noise.
- Long horizontal run with sagging — creates oil trap, reduces efficiency.

**GC field check:** Walk the lineset from outdoor unit to air handler. Insulation continuous? Penetrations sealed (and weatherproofed at exterior)? Lineset secured? Outdoor portion in UV-protective sleeve or wrap?

### 10.3 Duct Systems

#### Materials

| Type | Description | CA acceptance | Pros | Cons |
|---|---|---|---|---|
| **Galvanized sheet metal** | Rigid trunks and branches | Yes | Most durable; smoothest interior (lowest resistance); long life | Most expensive labor; takes more space |
| **Flexible duct (flex)** | Polyester or polyethylene inner core, insulation, vapor barrier outer jacket | Yes (with limits) | Cheap; easy to route around obstacles; insulated by default | Higher airflow resistance; easily kinked / damaged; must be tensioned fully; lifespan 15–20 yrs |
| **Duct board (fiberglass)** | Rigid foil-faced fiberglass board fabricated into rectangular ducts | Yes (with limits) | Built-in insulation; quiet | Erodes over time; fibers can release into airstream; less common now |
| **PVC / spiral metal** | High-velocity (Unico, SpacePak) | Yes for small-diameter | Tiny ducts fit in walls | Loud unless designed properly; specialty |

**Typical CA residential mix:** Sheet metal trunks (main supply and return), flex duct branches to registers. Pure flex systems exist but tend to fail HERS leakage tests because of joint quality.

#### Flex duct installation rules

| Rule | Why |
|---|---|
| **Fully extended** | Compressed flex (5 ft of flex stuffed into a 3 ft space) has 2–3× the rated airflow resistance |
| **No kinks** | A kink reduces flow by 50–80% — the room downstream is starved |
| **Bend radius ≥ 1× duct diameter** | Sharp bends cause turbulence and noise |
| **Supported every 4 ft** | Sagging flex creates traps that collect dust and dampen airflow |
| **Sealed at all connections** | Mastic + screws + UL 181 tape (NOT cloth duct tape); inner core sealed first, then insulation/jacket |
| **No splices in flex** | If you need more length, use a metal sleeve coupling (not a flex-to-flex tape splice) |

**GC field check:** Walk every flex run. Fully extended? Tensioned (not loose)? Supported? Connections taped/mastic'd and clamped?

### 10.4 Duct Leakage and Title 24 HERS Testing

California Title 24 requires a **duct leakage test by a certified HERS rater** for new HVAC systems and most replacements.

**Targets:**
- **New construction ducts**: ≤ 5% of system airflow as **total leakage** (or sometimes 6% per Title 24 alternatives).
- **Alteration / retrofit** (existing ducts modified): ≤ 10% or 15% depending on scope.
- "Leakage to outside" (CFM25 out of the conditioned envelope) is the stricter measure used in some cycles.

**What the test is:** Duct blaster (calibrated fan) connected to the air handler with all registers and returns sealed. Pressurize ducts to 25 Pa. Measured airflow at 25 Pa = leakage rate.

**Failure consequences:** Re-seal, re-test ($$$); or relocate ducts to conditioned space; or apply for an alternative compliance path. None are cheap.

#### How the GC prevents test failures

1. **Specify sheet metal trunks** instead of all-flex.
2. **Mastic all joints** (gray paste sealant). NEVER use cloth duct tape — fails within months.
3. **Seal duct boots to drywall/ceiling** before drywall. The boot-to-drywall gap is the #1 leak point. Use foil tape or duct-boot sealant.
4. **Mastic the air handler / plenum connections** — every screw, every seam, every flange.
5. **Take the HERS rater on a pre-test walk-through** before drywall. Identify potential leaks. Fix.
6. **Test before drywall closes anything you can't access.** If you fail the test after drywall, you're tearing out drywall.

**Key insight:** Duct sealing is a 1-hour-of-labor-per-system fix at rough. After drywall, it's an 8-hour-per-system fix. Pay your HVAC sub for the extra labor at rough. Get a HERS pre-test if budget allows.

### 10.5 Filter Location and Access

| Filter type | Location | MERV rating | Service interval |
|---|---|---|---|
| **Return air grille filter** | At the return grille (wall or ceiling) | MERV 5–11 typically (slim disposable) | 1–3 months |
| **Air handler filter** | At the air handler return inlet | MERV 8–13 (deeper media) | 3–6 months |
| **Media cabinet filter** | Dedicated cabinet on return trunk; 4–5" deep media | MERV 11–16 | 6–12 months |
| **Electronic / electrostatic air cleaner** | In return; powered | Equivalent MERV 13–16 | Wash quarterly |

**MERV vs. system compatibility:**
- Higher MERV = more resistance to airflow.
- A high-MERV filter (MERV 13+) on a system designed for MERV 8 will choke airflow, reduce capacity, possibly damage the blower.
- Always confirm MERV rating with the air handler's max static pressure spec.

**Filter access:**
- **Filter must be accessible** for the homeowner — not in a crawl space, not behind a furniture-blocked grille.
- If the filter is at the air handler (which is in a closet/attic), the door must open fully.
- A media cabinet (4" or 5" deep) requires removing the door and pulling the filter out — ensure 18" of clearance in front.

### 10.6 Combustion Air

For any **gas appliance in an enclosed space**, code requires sufficient combustion air to support flame and exhaust.

#### Confined vs. unconfined space (CMC §701)

- **Unconfined space**: Room volume ≥ 50 cubic feet per 1,000 BTU/hr of total appliance input. Most basements, large mechanical rooms.
- **Confined space**: Less than that. Most furnace closets, water heater closets. Requires dedicated combustion air openings.

#### Combustion air openings (CMC §701.4)

If confined, two openings required (one high, one low):
- **From outdoors (preferred)**: Each opening sized at **1 sq inch per 4,000 BTU/hr total appliance input** (with one screen and one louver). Two openings, separate ducts.
- **From within the building**: Each opening sized at **1 sq inch per 1,000 BTU/hr** (must communicate with another unconfined space).

**Direct vent appliances eliminate the need:** A sealed-combustion furnace or WH (concentric vent or two-pipe vent) draws combustion air from outside through its own pipe. No room combustion air openings required.

**Practical rule:** Specify **direct vent / sealed combustion** for all gas appliances in closets. It eliminates the combustion air detail, prevents backdraft, allows tighter closet construction.

#### California low-NOx requirements

California air districts (SCAQMD, BAAQMD) require **low-NOx** gas burners on residential equipment:
- Water heaters: ≤ 10 ng/J NOx (Rule 1146.2 SCAQMD; Reg 9-6 BAAQMD).
- Furnaces: ≤ 14 ng/J NOx.

All equipment sold in CA already meets these — but if you order a non-CA model online (e.g., from a Texas distributor), it may not comply. Verify product is "California compliant" or "low-NOx" before ordering.

### 10.7 Condensate Drainage

Air conditioning evaporator coils produce condensate (water from the air's humidity). It must drain.

#### Drain layout (CMC §310)

- **Primary drain**: ¾" PVC from coil drain pan to an approved location (sanitary drain via air gap, tailpiece of nearby fixture, condensate pump discharge, exterior drainage).
- **Secondary drain (overflow)**: Either a separate drain line to a location that will be noticed (e.g., over a window — water dripping signals problem) OR a **wet switch / float switch** that kills the AC when primary clogs.
- **Safety pan** (auxiliary drain pan): Required under air handler in attic over conditioned space (CMC §310.1). Pan drains to approved location.

**Slope and trap:**
- Primary drain must slope ⅛" per foot minimum.
- A **trap** is required at the air handler (CMC §310.4) to prevent air from being pulled through the drain (creates a "burble" and stops drainage). Trap depth depends on the blower's static pressure.

**Common defects (and AC failures):**
- No trap — drain doesn't flow, pan fills, ceiling drips.
- Trap that dries out — air pulls through, drain doesn't flow.
- Primary drain runs uphill (no slope or reverse slope).
- Secondary drain capped or never installed.

### 10.8 Forced Air Common Issues — GC Checklist

| Issue | How to spot | When to address |
|---|---|---|
| Oversized system | Manual J shows 24k BTU, equipment is 36k | At permit / equipment order |
| Undersized returns | One small return for whole house | At rough; before drywall |
| Wrong refrigerant line size | Lineset doesn't match installation manual | At rough; verify with mfr spec |
| Lineset insulation gaps | Bare copper visible at penetrations | At rough |
| Compressed flex duct | "Coiled-up" flex | At rough |
| Unsealed duct joints | Visible gaps; no mastic | At rough; before HERS |
| Missing condensate trap | No trap at air handler | At rough |
| No secondary drain or float switch | Attic AHU with no overflow protection | At rough |
| Filter not accessible | Filter slot blocked, no door clearance | At trim |
| Combustion air openings missing | Sealed closet, gas WH inside | At rough |
| Wrong thermostat for system | Single-stage stat on 2-stage equipment | At trim |

---

## 11. Ductless / Mini-Split Systems

Ductless mini-splits have become dominant for additions, ADUs, garage conversions, and zoned retrofits in California. They are also frequently misinstalled.

### 11.1 How They Work

- **Outdoor unit (condenser/heat pump)** with inverter-driven compressor (variable speed, not on/off).
- **Indoor unit(s) (head)** — wall-mounted, ceiling-cassette, ducted-concealed.
- **Refrigerant lines** connect outdoor to indoor (no ductwork for wall/cassette types).
- **Inverter compressor** modulates capacity continuously — runs at low speed most of the time, ramps up only for peak load.

**Why they win:**
- No duct losses (ducts in attic lose 20–30% in CA).
- Zone-by-zone control.
- Heat pump efficiency for both heating and cooling.
- Very high SEER2/HSPF2 (often 22+ SEER2).

### 11.2 Single-Zone vs. Multi-Zone

| Type | Description | Pros | Cons |
|---|---|---|---|
| **Single-zone** | One outdoor : one indoor | Highest efficiency; simplest; modulates best | Multiple outdoor units for multi-zone homes (clutter) |
| **Multi-zone (2:1, 3:1, 4:1, 5:1)** | One outdoor : multiple indoor heads | Fewer outdoor units; lower visual impact | Less efficient at part load (one head running but unit still cycles); refrigerant charge complexity; if outdoor unit fails, all zones down |

**Line set limits (typical Mitsubishi, Daikin, Fujitsu):**
- Max length per circuit: 50 ft (single-zone) to 100 ft (multi-zone with larger units).
- Max vertical separation: 30–50 ft.
- Pre-charged for some specific length (e.g., 25 ft); additional charge required beyond.

**Refrigerant charge:**
- Pre-charged outdoor unit has enough for 25–50 ft of lineset, depending on model.
- Beyond that, additional R-410A (or R-32 on newer units) must be added by weight.
- The HVAC tech must follow the manufacturer's charge chart — over- or under-charge by 10% causes 20–30% capacity loss.

### 11.3 Rough-In Requirements

| Item | Requirement |
|---|---|
| **Outdoor unit pad** | Concrete pad, vibration isolation, 12" from wall, 24" service clearance, snow/leaf clearance |
| **Wall penetration for lineset** | Typically a **2.5" hole** through wall framing; sleeved (PVC or rubber grommet); sloped slightly outward for water drainage |
| **Lineset cover** | Outdoor exposed lineset must be in a UV-protective cover (Slimduct or similar) — code requires protection from physical damage |
| **Condensate drain** | Gravity drain from indoor head to exterior (slope), OR condensate pump (with float switch) to discharge |
| **Electrical** | **Dedicated circuit per outdoor unit** (typically 240V, 15–30A depending on size); communication wire from outdoor to indoor (4-conductor, 14 AWG typical); disconnect at outdoor unit (NEC 440.14) |
| **Indoor head mounting** | Mount on stud or proper anchor; level; clearance for filter removal (typically 6" above head) |
| **Service access** | Filter accessible from front of head; lineset and condensate accessible at penetration |

**Condensate routing:** The indoor head has a small drain pan with a flexible tube exiting at the back. Route to exterior or to a condensate pump. **The condensate line is the #1 callback** — improperly sloped, kinked, or terminating where it stains the wall.

### 11.4 HERS Verification for Mini-Splits

Title 24 requires HERS verification of:
- **Refrigerant charge** (correct weight per manufacturer spec).
- **Airflow / superheat / subcooling** in some cases.
- **Installation verification** (proper sizing, correct equipment per Title 24 modeling).

Some specific Title 24 measures for mini-splits:
- **HERS-verified refrigerant charge**: certified rater confirms charge.
- **HERS-verified indoor airflow** (less common for mini-splits than ducted systems).
- **HVAC Compliance Form CF2R/CF3R** signed by installer and rater.

**GC scope:** Confirm HERS rater is engaged. Mini-split-only projects sometimes skip HERS — confirm with Title 24 consultant.

---

## 12. Ventilation

Modern airtight California homes need mechanical ventilation. The default residential standard is **ASHRAE 62.2**, adopted by Title 24.

### 12.1 ASHRAE 62.2 Whole-Building Ventilation

#### Required ventilation rate

ASHRAE 62.2-2016 (the version referenced in Title 24-2022):
- **Total ventilation rate (cfm)** = 0.03 × floor area (sf) + 7.5 × (Nbr + 1)
- Where Nbr = number of bedrooms.

**Example:** 2,000 sf, 3 bedrooms
- Rate = 0.03 × 2000 + 7.5 × 4 = 60 + 30 = **90 cfm continuous**.

This is the **mechanical ventilation** required, in addition to envelope infiltration.

#### Mechanical ventilation strategies

| Strategy | Description | Pros | Cons |
|---|---|---|---|
| **Exhaust-only** | Bath fan(s) run continuously at low CFM; outside air enters through envelope leaks and trickle vents | Cheapest; simple | Less control over inlet air; depressurization risk with combustion appliances |
| **Supply-only** | Fresh-air fan brings outside air in (often into return plenum of HVAC system); air exhausts through envelope leaks | Pressurizes house (prevents radon, soil gas entry); good outside air control | Energy penalty (no recovery) |
| **Balanced — without recovery** | Separate supply and exhaust fans; equal CFM | Best air control | Energy penalty |
| **Balanced — HRV (Heat Recovery Ventilator)** | Balanced + air-to-air heat exchanger recovers heat from exhaust | High efficiency; comfortable | Higher install cost; dedicated ducting |
| **Balanced — ERV (Energy Recovery Ventilator)** | HRV + moisture transfer | Best for humid OR dry climates (moves humidity in direction needed) | Highest install cost |

**California reality:**
- In mild climates (coastal), exhaust-only or supply-only is common.
- In hotter inland or colder mountain zones, HRV/ERV pays back.
- Many CA Title 24 compliance paths require balanced ventilation with recovery in tighter homes.

### 12.2 Bathroom Exhaust Fans

#### CFM sizing

| Application | Required CFM |
|---|---|
| Bath ≤ 100 sf | 50 cfm minimum (intermittent) or 20 cfm (continuous) |
| Bath > 100 sf | 1 cfm per sf intermittent, or 5–8 cfm/sf at peak |
| Whole-bath spa / steam | Per manufacturer; often 150+ cfm |

#### Duct sizing and termination

| Fan CFM | Duct size | Max equivalent length (typical) |
|---|---|---|
| ≤ 50 cfm | 4" rigid duct | 50 ft equivalent |
| 50–100 cfm | 4" or 6" | 75 ft equivalent |
| > 100 cfm | 6" | 100+ ft equivalent |

**Equivalent length:** Each fitting adds equivalent feet (a 90° elbow = ~10 ft; a 45° = ~5 ft; a roof cap = ~30 ft). A 4" duct with two 90° elbows and a roof cap has 50 ft of equivalent fittings before any actual duct length — exceeding the 50 ft limit easily.

**Termination (CRC R303.5.1, CMC §504):**
- Bath fan must terminate **to the exterior** — through a roof cap (sloped roof) or wall cap.
- **Never** terminate into an attic. (This is one of the most violated rules — and an attic full of moisture from a misvented bath fan is a roof rot disaster.)
- Roof cap or wall cap must have an integral backdraft damper.
- Cap must be at least 3 ft from any operable opening (window, soffit vent).

**Common defects:**
- Flex duct from fan to attic, terminated nowhere (or in a soffit, dumping back into attic).
- Crushed or kinked flex duct.
- Fan undersized for run length — air rate at the grille is half the rated cfm.

### 12.3 Kitchen Range Hoods

#### CFM sizing

| Cooktop | Required CFM |
|---|---|
| Standard 30" gas range | 100–300 cfm |
| Commercial-style range (e.g., Wolf, Viking) | 600–1,200 cfm |
| Induction or electric (no combustion) | 100–250 cfm sufficient |

#### Makeup air (CMC §504.3 and CRC §M1503)

**When kitchen exhaust exceeds 400 cfm, makeup air is required.** Why? At 400+ cfm, the hood pulls more air than the envelope can leak in, depressurizing the house — which can backdraft combustion appliances (water heater, furnace), reverse-flow flues, suck radon out of the slab, and disable the hood itself.

**Compliant makeup air:**
- Powered makeup air damper that opens when hood is on, providing fresh air make-up.
- Sized to roughly match hood CFM at full speed.
- Connected to outdoors (tempered if cold climate).
- Interlocked with hood (open when hood on, closed when off).

**Practical implication:** A homeowner who specs a 1,200 cfm commercial hood is committing to a $2,000–$4,000 makeup air install. Catch this at design.

#### Recirculating vs. vented

- **Vented (ducted to outside)**: Standard in CA new construction. Wall cap or roof cap.
- **Recirculating (charcoal filter, no duct)**: Allowed but does not count toward ASHRAE 62.2 ventilation. Common in island ranges where ducting is hard. Captures grease but does nothing for moisture or CO₂.

### 12.4 Dryer Duct (CMC §504.4)

| Spec | Requirement |
|---|---|
| **Duct material** | **Rigid metal (galvanized) or smooth-wall aluminum**. Foil-flex allowed only for the final connection (≤ 6 ft). **No plastic flex** (fire hazard). |
| **Duct diameter** | **4" minimum** |
| **Max length** | **25 ft equivalent length** for typical residential. Each 90° elbow = 5 ft equivalent; each 45° = 2.5 ft. (Newer dryers may allow 35 ft — check manual.) |
| **Termination** | To exterior; backdraft damper; **no screen** (lint clogs; some inspectors require louver-only) |
| **Cleanout** | If duct exceeds equivalent length or has multiple turns, a cleanout access may be required |
| **Booster fan** | If duct exceeds 25 ft, may need a booster fan (Tjernlund, Fantech) |

**Common defects:**
- Foil-flex full run (illegal — fire hazard).
- Crushed duct behind dryer (lint trap).
- Duct length excessive (washer-dryer in a closet remote from exterior wall).
- Screen on termination (lint clogs immediately).

### 12.5 Attic Ventilation (CRC R806)

Naturally ventilated attics require **net free vent area (NFVA)** to prevent moisture buildup and overheating.

| Ratio | When |
|---|---|
| **1:150 of attic floor area** | Default ratio |
| **1:300** | Allowed when 50–60% of vent area is high (ridge/gable) and 40–50% low (soffit), AND a vapor retarder is installed in the ceiling |

**Example:** 2,000 sf attic, 1:300 ratio → 6.67 sf NFVA = 960 sq in total = 480 sq in low + 480 sq in high.

**Vent types and NFVA (typical):**
- **Continuous soffit vent**: ~9 sq in/ft (perforated metal); ~5 sq in/ft (wood vented blocking).
- **Ridge vent**: 12–18 sq in/lf depending on product.
- **Gable vents**: per product (rectangular louvers ~50% gross is NFVA).
- **Roof vents** (box vents, "turtle vents"): ~50 sq in each.

**Balance:** Intake (soffit) area should equal or exceed exhaust (ridge/gable) area. Otherwise, exhaust pulls air from the conditioned space (through ceiling penetrations) — energy penalty.

**Unvented (cathedralized) attic:** Allowed under CRC R806.5 if spray foam under roof deck + air barrier at roof + meets specific moisture control criteria. Common in California for spray-foamed roofs holding HVAC equipment.

---

## 13. Coordination and Commissioning

This is where the GC earns the fee. The trades each do their own thing. The interfaces between them — and the system as a whole — are your responsibility.

### 13.1 MEP Coordination Sequence

#### Order of operations (rough)

| Step | Trade | What happens | GC role |
|---|---|---|---|
| 1 | Plumbing — underground | DWV in slab/crawl; water service stub; gas stub | Verify slope, depth, locations against plan; photograph before pour |
| 2 | Plumbing — top out | DWV through wall and roof; water supply manifold; gas | Walk every drain run for slope; trace every trap to vent; check cleanouts |
| 3 | Electrical — service and rough | Panel set; conduit underground; rough wire pulled to all boxes | Verify panel size, load calc; verify dedicated circuits; check box fill on big boxes |
| 4 | HVAC — equipment set and rough | Air handlers, condensers, ductwork, refrigerant lines, flues | Verify equipment matches load calc; walk ducts; check lineset insulation |
| 5 | Low-voltage rough | Data, coax, audio, alarm | Coordinate with electrician; verify separation from power |
| 6 | **All trades present for inspections** | Plumbing pressure test, electrical rough inspection, mechanical rough inspection | Schedule and attend |
| 7 | Insulation | Wall and ceiling insulation | After rough inspections sign-off |
| 8 | Drywall | Cover all rough | After insulation inspection |
| 9 | Tile / finish / cabinets | (Finish trades) | (Sequence per finish trade) |
| 10 | Plumbing trim, Electrical trim, HVAC trim | Fixtures, devices, registers | Coordinate sequence |
| 11 | HERS testing | Duct leakage, blower door, refrigerant charge, etc. | Schedule HERS rater |
| 12 | Final inspection | All trades + HERS report | Walk through with inspector |

#### Common scheduling errors

| Error | Consequence |
|---|---|
| Drywall before all rough inspections signed off | Inspector requires you to open drywall to verify; $1K+ rework |
| Insulation before plumbing pressure test | Test fails, insulation gets wet, has to be replaced |
| HVAC ducts run before plumbing | Plumber breaks ducts to fit drains, doesn't fix them |
| Drywall before HVAC duct boots sealed | HERS test fails; reopen drywall |
| Cabinets installed before bathroom rough verified | Wrong sink rough-in; cabinet doesn't fit |

### 13.2 Clearances

#### NEC 110.26 — Electrical panel working space

The most violated electrical code in remodels.

| Direction | Clearance required |
|---|---|
| **In front of panel** | 36" minimum, full panel height + 6" above | floor to ceiling |
| **Width** | 30" wide OR panel width, whichever is greater | |
| **Headroom** | 6'-6" minimum (panel cannot be in a low-ceiling closet) | |
| **Access** | Door must open 90° minimum | |

**You cannot store anything in front of a panel.** No water heater, no shelving, no built-in storage. Owner will want to "just put the broom closet in front of it" — say no.

#### Gas appliance clearances (CMC, manufacturer)

| Appliance | Sides | Front (service) | Top | Notes |
|---|---|---|---|---|
| **Forced air furnace (FAU)** | 1–6" sides per listing | **18" front minimum** (for serviceability); 24" preferred | Per listing; combustible | Filter access from front |
| **Tank water heater** | 0–2" sides per listing | 24" front | Combustion air above | Many listed for "zero clearance" sides |
| **Tankless water heater (sealed combustion)** | 0–6" per listing | 24" front | Per listing | Outside install often |
| **Gas fireplace (DV)** | Per listing | Per listing | Per listing | Always check the manual |

### 13.3 HVAC Startup and Commissioning

When equipment is set, ducted, charged, and energized for the first time, a proper startup is critical.

#### Startup checklist (verify HVAC sub performs)

| Check | What it confirms |
|---|---|
| **Voltage at unit** | Within 10% of nameplate (208/240V residential) |
| **Refrigerant charge** | Subcooling (for TXV) or superheat (for fixed orifice) within manufacturer range |
| **Indoor airflow** | Measured CFM matches design (within 10%); too low = strain on coil; too high = poor dehumidification |
| **External static pressure** | Within blower's design range (usually < 0.8" w.c. total) |
| **Temperature split (cooling)** | 15–20°F ΔT across coil (indoor air entering vs. leaving) |
| **Thermostat operation** | Cooling commands cooling; heating commands heating; fan modes work |
| **Condensate drain** | Test by pouring water in pan; verify discharge; verify float switch trips |
| **Filter installed** | Correct MERV; correctly oriented (arrow toward air handler) |
| **Outdoor unit level** | Within manufacturer spec; pad level |
| **All access panels closed** | All screws in; no rattles |

**Documentation:** Get a startup report from the HVAC sub — refrigerant pressures, temperatures, airflow. File in closeout. This is your defense if the system fails in year 1.

### 13.4 Title 24 HERS Inspections

HERS = Home Energy Rating System. A certified HERS rater (third party) performs testing required by Title 24.

#### Common HERS measures (residential)

| Test | What is measured | Pass criteria |
|---|---|---|
| **Duct leakage** | Total or to-outside leakage at 25 Pa | ≤ 5% (new) or 10–15% (alteration) of system airflow |
| **Refrigerant charge** | Subcooling/superheat | Within mfr range |
| **HVAC airflow** | Indoor airflow at supply registers | ≥ design CFM per ton |
| **Fan watt draw** | Watts/CFM for air handler | ≤ 0.58 W/cfm (varies) |
| **Blower door / envelope leakage** | Whole-house air leakage at 50 Pa | ≤ target ACH50 per Title 24 modeling |
| **Quality insulation install (QII)** | Visual + IR inspection of insulation | No voids, no compression, complete coverage |
| **Whole-building ventilation** | ASHRAE 62.2 compliance | Measured cfm at controls/grille |

#### What the GC can do to pass

| Action | Test it helps |
|---|---|
| **Mastic all duct joints** before drywall | Duct leakage |
| **Seal duct boots to drywall** with foil tape or mastic | Duct leakage |
| **Seal all plenum-to-air-handler connections** | Duct leakage |
| **Seal all top plates, electrical box penetrations** | Envelope leakage / blower door |
| **Properly install insulation** — no gaps, no compression, no voids around wires/pipes/boxes | QII / envelope |
| **Confirm HVAC tech verified charge** | Refrigerant charge |
| **Confirm correct filter installed** | HVAC airflow |
| **Schedule HERS rater early** — pre-inspection walk-through before drywall | All tests |

**Critical insight: A failed HERS test costs $1K–$10K to fix** (open drywall, reseal, retest, re-permit). A 30-minute walkthrough with the HERS rater before drywall costs $200. Always do the pre-test.

---

## Field Reference: MEP Quick Checklists

### Pre-Drywall MEP Sign-Off (GC walks the entire house)

#### Plumbing

- [ ] Every horizontal drain slopes ¼"/ft, verified with 4-ft level
- [ ] Every trap traced to a vent
- [ ] Every trap arm within Table 10-1 distance
- [ ] Cleanouts at upstream end of every horizontal main, every direction change, base of every stack
- [ ] Cleanouts in walls have access panels ordered
- [ ] DWV pressure test passed, sign-off in hand
- [ ] All supply lines have shut-off stubs at every fixture
- [ ] Water heater seismic-strapped (top third + bottom third); T&P discharge piped properly
- [ ] Water pressure test passed, sign-off in hand
- [ ] Gas pressure test passed, sign-off in hand
- [ ] CSST bonded to ground (#6 minimum)
- [ ] Manifold installed (if specified) and labeled
- [ ] Expansion tank installed at WH
- [ ] PRV installed at service entry; gauge installed
- [ ] All hot water pipes ¾"+ insulated R-3
- [ ] Recirculation pump installed and demand-control wired (if specified)

#### Electrical

- [ ] Panel size matches load calculation
- [ ] Load calculation in permit set
- [ ] Outdoor emergency disconnect installed (NEC 230.85)
- [ ] Whole-house SPD installed
- [ ] All required dedicated circuits run (range, dryer, DW, disposal, microwave, laundry, bath, garage, HVAC, EV)
- [ ] EV circuit / outlet roughed in
- [ ] All boxes within box fill limits
- [ ] All cables stapled within 12" of boxes, every 4½ ft
- [ ] AFCI required circuits identified
- [ ] GFCI required circuits identified
- [ ] All fire-rated wall penetrations firestopped
- [ ] Garage-to-house wall: every penetration sealed
- [ ] Grounding electrode system installed (Ufer + ground rods)
- [ ] Bonding to gas (CSST) and water complete
- [ ] Low-voltage panel located and ready
- [ ] Cat 6, coax home-runs to each location
- [ ] LV cables separated from power (2" parallel, 90° crossings)
- [ ] All boxes labeled at rough (room name)
- [ ] Rough inspection signed off

#### HVAC

- [ ] Manual J on file
- [ ] Equipment selected matches Manual S
- [ ] All ducts mastic-sealed (every joint, every boot)
- [ ] Duct boots sealed to drywall/ceiling
- [ ] Air handler plenum mastic-sealed
- [ ] Flex ducts fully extended, supported every 4 ft, no kinks
- [ ] Refrigerant lineset insulated full length
- [ ] Lineset penetrations sealed (interior and exterior)
- [ ] Condensate primary drain trapped and sloped
- [ ] Condensate secondary drain or float switch installed
- [ ] Combustion air sized OR direct vent equipment specified
- [ ] Bath fan ducts: 4" rigid, terminate to exterior (not attic)
- [ ] Range hood: ducted to exterior; makeup air if >400 cfm
- [ ] Dryer duct: 4" rigid metal; max 25 ft equivalent
- [ ] Attic ventilation: balanced, 1:300 or 1:150 NFVA
- [ ] Filter location accessible
- [ ] Rough inspection signed off
- [ ] HERS rater scheduled / pre-test walkthrough done

### Trim Sign-Off

#### Plumbing
- [ ] All fixtures installed, anti-scald set to 120°F
- [ ] All shutoffs functional (1/4-turn ball stops)
- [ ] WaterSense documentation in closeout
- [ ] Hot water recirculation tested
- [ ] Hot water delivery time at farthest fixture (target ≤ 30 sec)

#### Electrical
- [ ] All devices installed and torqued
- [ ] AFCI/GFCI tested at every device
- [ ] Panel labeled (typed, in sleeve)
- [ ] Smoke detectors interconnected and tested
- [ ] CO detectors installed at required locations
- [ ] All TR receptacles installed
- [ ] EV outlet labeled and tested
- [ ] Surge protector functional indicator visible

#### HVAC
- [ ] Refrigerant charge verified and HERS-documented
- [ ] Airflow verified at every register (smoke pencil or hood)
- [ ] Thermostat programmed and explained to owner
- [ ] Filter installed (correct MERV)
- [ ] Condensate drain tested
- [ ] HERS report received and submitted
- [ ] CF2R / CF3R signed and submitted

---

## Closing: How a GC Earns the MEP Subcontractor's Respect

You will never know plumbing better than your plumber. You'll never know electrical better than your electrician. You'll never know HVAC better than your mechanical sub. That's not the goal.

The goal is to know enough to:
1. **Catch their mistakes before drywall.** Every trade makes mistakes — they're human. A good plumber and a great GC catch 95% of the plumber's mistakes before they're covered. A bad GC discovers them at year 2 when the trim is leaking.
2. **Coordinate the interfaces they don't own.** The HVAC sub doesn't care if the duct boot conflicts with the framer's joist hanger. The electrician doesn't care if the recessed light location ruined the can spacing. You own the interfaces.
3. **Speak their language enough to call BS.** When the HVAC sub says "the lineset has to run that way," you should know whether that's true. When the plumber says "we don't need a cleanout there," you should know whether that's true. They will respect you for knowing — and try to skip steps when you don't.
4. **Schedule the order of operations** so plumbing doesn't run on top of HVAC, HVAC doesn't punch through electrical, electrical doesn't conflict with low-voltage, and all four make their inspection windows.

Master this document and you will be running MEP, not the other way around.

---

## Sources and Further Reference

- **California Plumbing Code (CPC) 2022** — uniformly adopted statewide; the law for plumbing.
- **California Mechanical Code (CMC) 2022** — uniformly adopted statewide; the law for HVAC.
- **California Electrical Code (CEC) 2022** — based on NEC 2020 with CA amendments; the law for electrical.
- **California Energy Code (Title 24, Part 6) 2022** — energy efficiency requirements.
- **California Green Building Standards Code (CALGreen) 2022** — water efficiency, EV-ready, etc.
- **ACCA Manual J, Manual D, Manual S** — residential HVAC design standards.
- **ASHRAE 62.2-2016** — residential ventilation.
- **NFPA 54 (National Fuel Gas Code)** — adopted into CPC for gas piping.
- **NEC 2020 / NFPA 70** — basis for CEC; the national standard for electrical.

Code adoptions update on a 3-year cycle (next CA code cycle: 2025, effective 2026). Confirm current code with AHJ before each project.
