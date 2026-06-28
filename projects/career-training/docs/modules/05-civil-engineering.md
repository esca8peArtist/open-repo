---
title: "Civil Engineering for the General Contractor"
module: 05
discipline: ["civil", "sitework", "earthwork", "drainage", "foundations"]
audience: "General contractor — construction-experienced, not a licensed engineer"
status: "reference"
tags: [career-training, civil-engineering, sitework, drainage, earthwork, foundations, utilities]
created: 2026-05-12
---

# Civil Engineering for the General Contractor

A working reference for residential and light-commercial GCs who need to read civil drawings fluently, coordinate intelligently with civil engineers, manage earthwork and underground subs without getting taken, and recognize site problems before they become claims. This is not a textbook — it is the field knowledge you need so the civil engineer cannot snow you, the dirt sub cannot pad quantities on you, and the building inspector does not red-tag your pad.

> **Bottom line first**: Civil mistakes are the most expensive mistakes on a job. A footing error wastes a footing. A grading error wastes a building. The GC who understands soils reports, drainage logic, and compaction testing **before** breaking ground saves more money than any other single skill on the project. The engineer owns the design and the stamp; the GC owns means, methods, conformance to plan, and field verification. Know the line, hold the line.

---

## Part 1 — Site Analysis and Survey

### 1.1 The Survey Plat and Legal Description

Before you set a stake, you need to know what land you are building on. Three documents define this:

| Document | What it tells you | Who produces it |
|---|---|---|
| **ALTA/NSPS Land Title Survey** | Boundary, easements, encroachments, improvements, title exceptions plotted. Required by most lenders. | Licensed Professional Land Surveyor (PLS) |
| **Boundary Survey** | Just the property lines and corners. Cheaper. Not adequate for development. | PLS |
| **Topographic Survey** | Elevations, contours, existing improvements, trees, utilities. Often combined with boundary. | PLS |

A **legal description** is the words that define the parcel. Two common forms:

- **Metes and bounds**: directional and distance calls from a Point of Beginning (POB). Reads like *"Thence N 32°15'42" E, 147.83 feet to an iron pin..."* Common in original 13 states, Texas, and irregular parcels everywhere. The bearings are azimuths from true or grid north — confirm which.
- **Lot and block** (subdivision): *"Lot 14, Block 3, Sunset Hills Subdivision, as recorded in Plat Book 22, Page 47, of the official records of [County], [State]."* Common in platted subdivisions. Simpler but you must pull the recorded plat for actual dimensions.
- **Public Land Survey System (PLSS)**: section/township/range, used in most western states. *"The NE 1/4 of the SW 1/4 of Section 12, Township 3 North, Range 5 West..."* A full section is 1 mile square = 640 acres. A quarter-quarter is 40 acres.

**GC red flags on legal descriptions**:
- Bearings that do not close (the boundary does not return to the POB) — survey error or undisclosed gap.
- "More or less" acreage that differs significantly from the recorded plat.
- "Subject to easements of record" with no schedule of those easements attached. **Always demand a title commitment with Schedule B-II exceptions** before bidding.

### 1.2 Easements, Rights-of-Way, and Setbacks

| Term | Meaning | GC implication |
|---|---|---|
| **Easement** | Right granted to a non-owner to use part of the property for a specific purpose. Runs with the land. | You cannot build a permanent structure in most easements. Driveways and pavement are usually OK in utility easements; foundations almost never. |
| **Right-of-Way (ROW)** | Public corridor, usually for a road or major utility. The municipality owns the rights, not the abutting owner. | Anything you do in the ROW (curb cuts, sidewalk, tap-ins) requires an **encroachment permit** or **ROW permit**. |
| **Utility easement** | Typically 5–15 ft along the rear and side lot lines for power, gas, telecom, water, sewer. | Read the recorded plat; the easement may be exclusive (one utility) or blanket (any utility). |
| **Drainage easement** | Strip designated to carry stormwater. Often along swales or rear of lots. | Do not regrade or fence across these. You will be liable for upstream flooding. |
| **Conservation easement** | Permanent restriction to protect wetlands, trees, habitat. | Construction limit. Survey-stake it before any earthwork. |
| **Access easement** | Driveway across one parcel to reach another (landlocked or shared drive). | Confirm maintenance responsibility in the recorded document. |
| **Sight-distance easement** | Triangle at corners for traffic visibility. | No structures or vegetation over ~30 in. |
| **Setback** | Zoning-mandated buffer from the property line. Front, side, rear, and often a separate accessory-structure setback. | Set by **zoning**, not the deed. Check both the easement *and* the setback; the more restrictive controls. |

**Practical rule**: Stake every easement and every setback before the foundation layout. The cost of a re-stake is $400; the cost of a building 18 in. into an easement is litigation or a tear-out.

### 1.3 Topographic Surveys and Contours

A topo shows existing ground surface as a set of **contour lines** — lines of equal elevation.

- **Contour interval (CI)**: vertical distance between adjacent lines. Typical: 1 ft for residential sites, 2 ft for larger commercial, 5 ft for rural/master plans. Verify CI in the legend before reading anything.
- **Index contours**: every 5th contour, drawn heavier with elevation labeled.
- **Reading slope from contours**:
  - Contours close together = steep
  - Contours far apart = flat
  - Contours forming a V pointing **uphill** = drainage swale or stream (water flows down the V)
  - Contours forming a V pointing **downhill** = ridge
  - Concentric closed contours = hilltop (or depression if hachured / labeled "D")
- **Slope calculation**: rise over run. If two contours 2 ft apart vertically are 20 ft apart horizontally, slope = 2/20 = 10% (or 1:10).

### 1.4 Benchmarks and Vertical Datums

| Datum | Year | Where used | Notes |
|---|---|---|---|
| **NGVD29** | National Geodetic Vertical Datum of 1929 | Older drawings, some still-current FEMA maps | Tied to mean sea level at 26 tide gauges. Increasingly obsolete. |
| **NAVD88** | North American Vertical Datum of 1988 | Modern standard for CONUS | More accurate, tied to a single benchmark in Canada. |
| **Assumed datum** | Site-local | Small residential jobs | An arbitrary 100.00 ft set at a defined point (e.g., top of a manhole rim). Fine for small jobs, **disaster** if you tie a second survey to it without knowing. |
| **NAVD88 → NGVD29 conversion** | varies by location | When old and new plans coexist | Conversion is typically **NGVD29 − offset = NAVD88**; offset varies from about −0.5 to −1.5 ft in CONUS. **Never assume — use NOAA's VERTCON tool**. |

**Critical**: When a flood elevation is called out, **confirm the datum**. A BFE of 12.5 ft NGVD29 is not the same as 12.5 ft NAVD88. In some Gulf Coast counties the difference is more than a foot — enough to put your finished floor below the BFE and void the flood insurance.

**Benchmarks on plans** are shown as a triangle or X with elevation. There should be at least two on any site so you can check one against the other. The surveyor should leave **temporary benchmarks (TBMs)** — usually a chiseled X or set spike — so the GC can re-verify elevations without re-hiring the surveyor.

### 1.5 Geotechnical Reports

The geotech (soils) report is the most important document the GC reads after the structural drawings. The structural engineer designs to the **allowable bearing capacity** and **soil parameters** the geotech provides. If the GC fails to deliver the soil condition the report assumed, the structure fails or the geotech writes a costly remedial letter.

**Standard contents of a geotech report**:

1. Project description and locations of borings
2. Site geology and regional context
3. Boring logs (one per boring)
4. Laboratory test results
5. Subsurface profile (cross-section showing soil layers)
6. Recommendations: foundation type, allowable bearing pressure, lateral earth pressures, slab subgrade prep, pavement section, seismic site class, groundwater, drainage
7. Construction observation and testing requirements

**Reading boring logs — what to look for**:

| Element | What it tells you | GC concern |
|---|---|---|
| **Depth** | How deep the boring went. Typical: 15–25 ft for residential, 50–100 ft for commercial, deeper for piles or high loads. | Did they bore deep enough to capture all soils your foundation might influence? Rule of thumb: 2× foundation width below bearing. |
| **Soil description (USCS)** | Unified Soil Classification System — letter pairs like SP, SC, CL, CH, ML, MH, GW, GP. Top letter is dominant grain size, second is gradation/plasticity. See §1.6. | Tells you what the dirt actually is. |
| **SPT N-value** | Blows of a 140-lb hammer falling 30 in. to drive a 2-in. sampler 12 in. (after seating 6 in.). Higher = denser/stiffer. | Direct correlation to bearing capacity and compactability. See table below. |
| **Moisture content (w%)** | Mass of water as % of dry soil mass. | High moisture in clay = soft, low bearing, hard to compact. |
| **Groundwater elevation** | Often labeled "GWT" or "WL" with a date and an "after drilling" or "stabilized" note. | Drives dewatering plan, basement waterproofing, slab-on-grade vapor strategy. |
| **Refusal** | Boring stopped because it could not penetrate further. | Rock or hard till. May trigger blasting, ripping, or pile redesign. |
| **Sample type** | SS = split spoon, ST = Shelby tube (undisturbed for clay), RC = rock core. | Tells you what tests can be run. |

**SPT N-value interpretation (rule-of-thumb correlations — not for design)**:

| N (blows/ft) | Granular (sand/gravel) | Cohesive (clay) — approx. unconfined compressive strength |
|---|---|---|
| 0–4 | Very loose | Very soft (<500 psf) |
| 4–10 | Loose | Soft (500–1,000 psf) |
| 10–30 | Medium dense | Medium stiff (1,000–2,000 psf) |
| 30–50 | Dense | Stiff to very stiff (2,000–4,000 psf) |
| 50+ | Very dense | Hard (>4,000 psf) |

**Bearing capacity**: The report will give an **allowable** bearing pressure (already includes a factor of safety, typically 3.0). Residential spread footings on competent soil are commonly designed for 1,500–2,500 psf. If the report says 2,000 psf and your foundation plan was drawn assuming 3,000 psf, you have a problem before you mobilize.

**Expansion index (EI) / Plasticity Index (PI)** — the two most important numbers for clay sites:

| Test | What it measures | Trigger value |
|---|---|---|
| **EI (ASTM D4829)** | How much a remolded clay swells when wetted | EI < 20 = non-expansive; 21–50 = low; 51–90 = medium; 91–130 = high; >130 = very high |
| **PI (Atterberg limits, ASTM D4318)** | Plasticity range between liquid and plastic limits | PI < 15 = low plasticity; 15–25 = medium; >25 = high. PI > 15 generally requires expansive-soil precautions |

**If EI > 50 or PI > 15**: expect engineered slab (post-tension or stiffened mat), moisture conditioning of subgrade, perimeter moisture barriers, restrictions on planting near foundation. Do not let architecture put irrigated plants 18 in. from a slab edge on a high-PI site.

**Liquefaction potential**: in seismic regions on saturated loose sand. The geotech runs a Seed-Idriss or similar analysis. If the report identifies liquefaction-susceptible layers, the foundation will require **deep foundations, ground improvement (stone columns, compaction grouting), or structural mat**. This is not a GC choice; it is a designed condition.

**Things to flag in a geotech report and bring to the engineer of record**:

- Groundwater within 5 ft of finish floor in a slab-on-grade design
- Recommendations for over-excavation that the structural plans do not show
- Expansive soil recommendations not reflected in slab details
- Pavement section recommendations that differ from civil drawings
- A note that says "additional borings recommended" — almost always ignored, almost always a future change order
- Recommendation for a Geotechnical Engineer of Record to provide construction observation. **This is not optional.** Insist the owner contract it; without it the report's recommendations may be void.

### 1.6 Unified Soil Classification System (USCS) — Quick Reference

| Symbol | Name | Behavior |
|---|---|---|
| **GW** | Well-graded gravel | Excellent, free-draining, no frost heave |
| **GP** | Poorly graded gravel | Good, free-draining |
| **GM/GC** | Silty/clayey gravel | Fair, drainage drops with fines |
| **SW** | Well-graded sand | Excellent fill material |
| **SP** | Poorly graded sand | Good but compacts narrowly — moisture sensitive |
| **SM** | Silty sand | Common fill, moisture sensitive |
| **SC** | Clayey sand | OK fill if PI controlled |
| **ML** | Low-plasticity silt | Frost-susceptible, soft when wet |
| **MH** | High-plasticity silt | Volume change risk |
| **CL** | Low-plasticity clay (lean clay) | Compactable, moderate swell |
| **CH** | High-plasticity clay (fat clay) | **High swell/shrink, the troublemaker** |
| **OL/OH** | Organic silt/clay | Unsuitable for structural fill |
| **Pt** | Peat | Unsuitable, must remove |

### 1.7 Environmental Constraints

**FEMA Flood Zones (FIRM — Flood Insurance Rate Map)**:

| Zone | Meaning | Construction implications |
|---|---|---|
| **X (unshaded)** | Minimal flood hazard | No flood-specific restrictions |
| **X (shaded)** | 0.2% annual chance (500-year) | Lender may require flood insurance; some jurisdictions add freeboard |
| **A, AE, AH, AO** | 1% annual chance (100-year) — SFHA | Lowest floor at or above BFE; many jurisdictions require freeboard of 1–3 ft. AE has a published BFE; A does not (developer must establish). |
| **AO** | Sheet flow flood, 1–3 ft depth | Finished floor 1 ft above highest adjacent grade plus the AO depth |
| **V, VE** | Coastal, with wave action | Open foundations (piles or piers) required; breakaway walls below BFE; substantial engineering. |
| **Floodway** | Channel + adjacent land that must be reserved | **No fill, no structures, no rise.** Effectively undevelopable. |

- **BFE (Base Flood Elevation)**: elevation of the 1% annual chance flood at that point.
- **DFE (Design Flood Elevation)**: BFE + local freeboard. Build to DFE, not BFE.
- **Elevation Certificate** (FEMA Form 086-0-33): required pre- and post-construction in SFHAs. Surveyor produces it.
- **LOMA / LOMR**: Letter of Map Amendment / Revision — used to remove a structure or property from the SFHA after grading or survey shows it is above BFE. Plan 4–6 months minimum.

**Wetlands**:
- Federally regulated under Clean Water Act §404 (USACE jurisdiction).
- Identified by hydrology, hydric soils, and hydrophytic vegetation — a **wetland delineation** is required by a qualified scientist if there is any chance.
- **Section 404 permit** required for any fill in jurisdictional waters. Nationwide Permits (NWP) cover small impacts; individual permits for larger.
- Many states have their own wetland regulations stricter than federal (NJ, MA, FL, CA).

**Grading ordinances**: Most municipalities have a grading permit threshold (e.g., 50 CY moved, or any cut/fill over 4 ft, or any disturbance over 1 acre). Triggers a **grading plan** review, an erosion control plan, and inspections. Some jurisdictions also require:
- Slope limits (e.g., max 2:1 unless engineered)
- Distance setbacks from top/toe of slope to structures
- Tree protection (often anything > 6 in. DBH)
- Hillside ordinance (California): geotechnical and slope-stability reports, terracing rules

---

## Part 2 — Earthwork and Grading

### 2.1 Cut/Fill Calculations and Mass Haul

**Cut**: material excavated below existing grade.
**Fill**: material placed above existing grade.
**Balanced site**: cut quantity equals fill quantity (in compacted volume).

Three measurement states — **know which one the spec calls for**:

| State | Symbol | Description |
|---|---|---|
| **Bank** | BCY (Bank Cubic Yards) | Volume in place, before excavation |
| **Loose** | LCY | Volume in truck, after excavation, before compaction |
| **Compacted** | CCY | Volume in place, after compaction |

**Soils change volume**:

| Soil type | Swell (bank→loose) | Shrinkage (bank→compacted) |
|---|---|---|
| Sand, gravel (GW, SW) | 10–15% | 0 to −5% |
| Silty/clayey sand (SM, SC) | 15–25% | 5–10% |
| Lean clay (CL) | 25–35% | 10–20% |
| Fat clay (CH) | 30–40% | 15–25% |
| Topsoil/loam | 25% | 15–25% |
| Rock (blasted) | 40–80% | −20 to −30% (cannot be re-densified to original) |

**Example**: Plans show 1,000 BCY of cut to be used as fill, but the spec calls for 95% compaction. If the soil shrinks 15%, you need 1,000 BCY × (1 / 0.85) = 1,176 BCY-equivalent of compacted fill. You are 176 BCY short and must import.

**Mass haul diagram**: cumulative net volume along the alignment. Used on linear projects (roads, sewers) to plan where to take cut and where to place fill, minimizing haul distance. For most residential sites it is overkill, but on a 20-lot subdivision it pays for itself.

**GC math check on every site**: 
1. Total cut (BCY) − total fill (BCY) = net before adjustment
2. Apply shrinkage to fill: fill (CCY) × (1 / (1 − shrinkage)) = fill (BCY-equivalent)
3. Net BCY = cut − adjusted fill. Positive = export. Negative = import.
4. Convert export/import to LCY for trucking: LCY = BCY × (1 + swell)
5. Trucks: standard 10 CY dump = ~10 LCY. Belly dump = 20–28 LCY.

### 2.2 Compaction Specifications

**Relative compaction** is measured as a percent of a laboratory maximum dry density.

| Test | Energy | Use |
|---|---|---|
| **Standard Proctor (ASTM D698)** | 12,400 ft-lb/ft³ | Older spec, light loads, residential pads sometimes |
| **Modified Proctor (ASTM D1557)** | 56,250 ft-lb/ft³ | Modern standard for structural fill, pavements, foundations |

**Typical relative compaction requirements (Modified Proctor)**:

| Application | RC required |
|---|---|
| Structural fill below footings | 95% min |
| Building pad subgrade | 90–95% |
| Pavement subgrade | 95% |
| Pavement aggregate base | 95–100% |
| Utility trench backfill (under pavement) | 95% |
| Utility trench backfill (landscape) | 85–90% |
| Top 12 in. of landscape fill | 85% (to allow plant growth) |

**Optimum moisture content (OMC)**: each Proctor curve has a peak — the moisture % that yields maximum density. Fill placed too dry will not compact; too wet will pump and not compact. Spec usually requires moisture within **±2% of OMC**. The dirt sub must water or dry the fill to land in this window — and the GC must let him.

**Field density testing**:

| Method | Speed | Accuracy | Notes |
|---|---|---|---|
| **Nuclear density gauge (ASTM D6938)** | 2–5 min/test | Good | The standard. Requires licensed operator, source security, daily/standard calibration. |
| **Sand cone (ASTM D1556)** | 30–45 min/test | Best (when done right) | The referee test when nuclear is disputed. Slow, destructive. |
| **Drive cylinder (ASTM D2937)** | 15 min/test | Fair | Cohesive soils only. |
| **DCP (Dynamic Cone Penetrometer)** | Fast | Indicator only | Not a primary acceptance test. Useful for QC screening. |

**Testing frequency** — typical commercial spec:
- 1 test per 2,500 ft² of fill area per 12-in. lift, OR
- 1 test per 100 LF of trench per lift, with min 3 tests per day
- 1 test per 500 ft² of footing subgrade
- Failed test = retest after rework, no payment for the failed lift until passing

**Reflexive GC checks**:
- Are tests being taken in your presence or are you trusting the report? Ask for the daily test log.
- Is the testing lab independent or hired by the earthwork sub? Insist on an owner-paid independent geotechnical inspector.
- Are tests in the middle of fills or on the edges? Edges fail more; testers know this and may avoid them.
- Lift thickness exceeding 8 in. compacted (12 in. loose) is almost always non-compliant. Watch the lifts.

### 2.3 Subgrade Preparation and Over-Excavation

**Standard subgrade prep under a building pad**:
1. Strip topsoil, organic, debris — typically 4–12 in. Stockpile separately, do not mix with structural fill.
2. **Proof-roll** the exposed subgrade with a loaded dump truck or rubber-tired roller. Watch for pumping (the surface deflects under load). Pumping areas = unsuitable.
3. **Scarify** the top 8–12 in., moisture-condition, and **recompact** to spec.
4. Place engineered fill in lifts to design subgrade elevation.
5. Final proof-roll before slab/foundation.

**Over-excavation** is used to remove unsuitable soil and replace with structural fill. Triggered by:
- Soft/wet zones identified in proof-roll
- Expansive clay where the design assumed non-expansive
- Buried debris, organics, old foundations, fill of unknown origin

Typical over-ex for expansive soils: 24–36 in. below footings and 12–24 in. below slab, extending 5 ft beyond footing perimeter. The geotech specifies.

**Unsuitable material claim** — the most common changed-condition dispute. The earthwork sub claims to find peat/debris/saturated clay that was not disclosed; the GC owes the cost of removal and import. Defenses:
- Was it disclosed in the geotech report? If yes, the sub took the risk.
- Did the sub investigate before bidding? Most contracts contain a "duty to inspect" clause.
- Document the condition: photos, surveyor cross-section, truck counts, weigh tickets. **Never approve a unit-price change order for unsuitable material without independent quantity verification.**

### 2.4 Grading Plan Interpretation

A grading plan is a topographic plan showing both existing (dashed, lighter, often labeled "EG" or "EX") and proposed (solid, heavier, often labeled "FG" or "PR") contours.

**Key callouts**:

| Symbol/notation | Meaning |
|---|---|
| **FFE / FF** | Finish Floor Elevation |
| **FG / FGE** | Finish Grade Elevation |
| **EG / EX** | Existing Grade |
| **TC / GS** | Top of Curb / Gutter (Spot) |
| **FL / FLOW** | Flow line (lowest point in gutter or swale) |
| **TW / BW** | Top of Wall / Bottom of Wall (retaining) |
| **HP / LP** | High Point / Low Point |
| **PAD** | Pad elevation (top of compacted pad, typically 4–6 in. below FFE for slab thickness + base) |
| **2.0%** | Slope (percent grade); without arrow assume downhill the way the number is written |
| **2:1** | Slope ratio (run:rise); 2:1 = 50% = 26.6° |
| **TYP** | Typical |

**Standard residential slope minimums** (from IRC and most local ordinances):
- Within first 10 ft of building: **5% (6 in. per 10 ft) away from foundation** — non-paved
- Within first 10 ft of building: **2% away from foundation** — paved
- Swale: **1% min, 2% preferred**, 0.5% absolute minimum in flat terrain (with engineer approval)
- Driveway max: **15% for short distances**, 12% sustained, **10% if you ever expect a fire truck**
- Lawn / general grading: 2% min, 33% (3:1) max for mowable, 50% (2:1) max for unmowed/ungrassed
- ADA accessible route: **5% max running slope, 2% max cross slope** (see Part 6)

**Pad elevation vs. FFE**:
- For a slab-on-grade: PAD = FFE − slab thickness (4 in. typical) − base thickness (4–6 in. typical) = FFE − 8 to 10 in.
- For a stem-wall crawl space: PAD = top of footing
- **Always confirm** the pad/FFE relationship with the structural before setting grade stakes. A miscommunicated 6 in. ruins the threshold, the driveway tie-in, and the door swing.

### 2.5 Erosion and Sediment Control (E&SC)

Federal Clean Water Act regulates construction stormwater discharge. Sites disturbing **1 acre or more** (or part of a larger common plan) need:

- **NPDES Construction General Permit (CGP)** coverage — EPA or delegated state
- **SWPPP** (Stormwater Pollution Prevention Plan) on-site, kept current
- **Notice of Intent (NOI)** filed before disturbance, **Notice of Termination (NOT)** filed at stabilization
- Inspections: typically weekly + within 24 hrs of a 0.25-in. rainfall event
- A trained on-site SWPPP coordinator (some states require certification — e.g., Georgia GSWCC, California QSP)

**Standard BMPs (Best Management Practices)**:

| BMP | Where | Detail to verify |
|---|---|---|
| **Stabilized construction entrance** | All site exits | 50 ft min length, 2–3 in. crushed stone, 6 in. depth, geotextile underneath |
| **Silt fence** | Down-gradient perimeter | Posts max 6 ft o.c. (10 ft if reinforced), fabric trenched in 6 in., wire-backed for slopes >2:1 |
| **Inlet protection** | Every storm drain inlet receiving runoff | Filter sock, block-and-gravel, or fabric basket. Failure mode: clogging and bypass — clean regularly |
| **Straw wattles / fiber rolls** | Across slopes, intervals based on grade | 8–12 in. dia., staked into ground; intervals: 15 ft for >3:1, 25 ft for 4:1, 50 ft for 5:1 |
| **Check dams** | In ditches/swales | Triangular, max 2 ft tall, spaced so toe of upper = top of lower |
| **Sediment basin / trap** | Drainage areas > 5 ac (basin) or < 5 ac (trap) | Sized to retain sediment from 2-yr storm; dewater through skimmer |
| **Dust control** | Active disturbed areas | Water trucks; sometimes polymer or magnesium chloride |
| **Concrete washout** | Designated area | Lined pit or prefab container. Never washout into a drain or onto bare ground. |
| **Temporary seeding / mulch** | Inactive disturbed areas > 14 days | Seed within 14 days of inactivity; mulch at 2 tons/ac straw |

**Penalties for E&SC violations** are real and individually large. EPA fines up to ~$59,000/day (2024 numbers, inflation-adjusted); states often add their own. Worse, an E&SC violation can shut down the entire job pending corrective action.

### 2.6 Retaining Walls

| Type | Range | How it works | When used |
|---|---|---|---|
| **Gravity** | < 4 ft (segmental block, dry-stack stone) | Mass of wall resists overturning | Decorative, low retention, no surcharge |
| **Reinforced concrete cantilever** | 3–20 ft | T- or L-shaped footing uses backfill weight to resist | Most common engineered wall; needs footing depth ~50–65% of wall height |
| **MSE (Mechanically Stabilized Earth)** | 5–40+ ft | Soil mass reinforced with geogrid or steel strips, faced with block or panels | Cost-effective for tall walls if space behind for reinforcement (typically 0.7–1.0× wall height) |
| **Sheet pile / soldier pile** | Any | Steel/timber piles driven into ground | Tight sites, dewatering, temporary excavation support |
| **Soil nail / tieback** | Any | Steel rods drilled into existing soil, faced with shotcrete | Cuts where you cannot reach behind the wall |

**Walls > 4 ft (measured bottom of footing to top of wall) almost universally require engineering and a permit.** Some jurisdictions trigger at 3 ft. Walls with surcharge (e.g., a driveway above the wall, a building near the top) **always** need engineering regardless of height — IRC Section R404.4 and IBC Section 1807.

**Surcharge loading** — extra load on top of the retained soil. Common surcharges:
- Vehicle: 250 psf (passenger), 600 psf (truck)
- Building footing: from structural — site-specific
- Sloped backfill: equivalent fluid pressure increased per the slope angle

**Drainage behind walls — non-negotiable**:
- Free-draining backfill (gravel, GW/GP, < 5% fines) for the first 12 in. behind the wall
- Drain pipe (perforated, 4 in. min) at the heel, daylighted or tied to a drain
- Weep holes every 4–8 ft if no drain pipe (less reliable)
- Geotextile separating native soil from drainage stone
- Surface seal at top of wall (compacted clay cap or paving) to keep runoff out of the wall mass

**The #1 cause of retaining wall failure** is not undersizing — it is **hydrostatic pressure** from inadequate drainage. Water behind a wall designed for drained backfill triples or quadruples the lateral pressure. Build the drainage right or build the wall twice.

---

## Part 3 — Drainage and Stormwater

### 3.1 Hydrology Basics — Rational Method

The **Rational Method** is the workhorse for small drainage areas (< ~200 acres). The civil engineer uses it; you should understand it so you can sanity-check a sized pipe.

$$Q = C \cdot i \cdot A$$

Where:
- **Q** = peak runoff (cubic feet per second, cfs)
- **C** = runoff coefficient (dimensionless, 0–1)
- **i** = rainfall intensity (in/hr) for the design storm and duration equal to time of concentration
- **A** = drainage area (acres)

(The units work out because 1 ac-in/hr ≈ 1 cfs; the engineer's shortcut.)

**Typical C values**:

| Surface | C |
|---|---|
| Asphalt / concrete | 0.85–0.95 |
| Roof | 0.90–0.95 |
| Gravel | 0.50–0.70 |
| Lawn, sandy soil, flat | 0.05–0.10 |
| Lawn, sandy soil, steep | 0.15–0.20 |
| Lawn, clay soil, flat | 0.13–0.17 |
| Lawn, clay soil, steep | 0.25–0.35 |
| Woods | 0.05–0.25 |
| Pasture | 0.10–0.30 |

**Composite C** for a mixed site: area-weighted average.

**Rainfall intensity (i)**: looked up from **NOAA Atlas 14 IDF curves** for the site location, design storm return interval (2-, 10-, 25-, 100-year), and duration (= time of concentration).

**Time of concentration (Tc)**: time for runoff to travel from the most hydraulically remote point in the drainage area to the design point. Three flow segments usually summed:
1. **Sheet flow** (first 100 ft max): Manning's-based equation
2. **Shallow concentrated flow**: defined surface paved/unpaved nomographs
3. **Channel flow**: Manning's equation, V = (1.486/n) R^(2/3) S^(1/2)

Typical Tc for residential sites: 5–20 min. **Minimum Tc is usually 5 min** by ordinance; using less artificially inflates i.

**Design storms by use**:

| Conveyance | Design return interval |
|---|---|
| Roof gutters and downspouts | 10-yr, 5-min |
| Yard inlets | 10-yr |
| Storm drain pipes (residential street) | 10-yr to 25-yr |
| Storm drain pipes (commercial) | 25-yr |
| Major culverts (arterial) | 50-yr |
| Detention design | 2-, 10-, 25-, 100-yr (multiple events) |
| Floodplain mapping | 100-yr, sometimes 500-yr for critical facilities |
| Emergency overflow | 100-yr (must safely pass without damage) |

### 3.2 Storm Drain Systems

**Pipe materials**:

| Material | Common diameters | Pros | Cons |
|---|---|---|---|
| **RCP (Reinforced Concrete Pipe)** | 12 in. – 144 in. | Strong, long life (75+ yr), high cover capacity | Heavy, expensive, joints leak more than HDPE |
| **HDPE (corrugated, dual wall)** | 4 in. – 60 in. | Light, flexible, smooth interior (n=0.012), tight joints | Buoyant when empty, cover and burial sensitive |
| **PVC (SDR 35 or solid wall)** | 4 in. – 36 in. | Easy install, smooth | Limited size, UV degrades, deflection in poor backfill |
| **CMP (Corrugated Metal Pipe)** | 12 in. – 144 in. | Cheap, fast install, large sizes | Shorter life (30–50 yr), abrasion and corrosion |
| **Ductile iron** | 4 in. – 64 in. | Pressure-rated, high strength | Expensive, used mainly for water/force main |

**Manning's n values (roughness)** drive capacity calculations:
- Concrete pipe: n = 0.012–0.013
- HDPE smooth wall: n = 0.012
- HDPE corrugated dual wall: n = 0.012 (interior is smooth)
- CMP: n = 0.024 (much rougher — needs larger pipe for same Q)
- PVC: n = 0.010–0.012

**Inlet types**:

| Type | Description | Use |
|---|---|---|
| **Curb inlet** | Opening in curb face | Street drainage |
| **Grate inlet** | Open grate at low point | Parking lots, yards |
| **Combination** | Curb + grate | High-capacity street |
| **Trench drain** | Long linear slot | Driveways, loading docks, sports surfaces |
| **Yard / area drain** | Small grate in turf or hardscape | Local low spots |
| **Catch basin** | Inlet with a sump (sediment trap) below outlet | Where sediment loading expected; cleaned periodically |
| **Drop inlet / junction box** | Below-grade structure to bring lateral into main | Network connections |

**Slope requirements**:
- Minimum: typically **0.5% for 12-in. pipe** dropping to a flatter slope for larger pipes; check that velocity is **at least 2 ft/sec** when flowing full to prevent sediment deposition. **Self-cleaning velocity** is the controlling criterion, not slope alone.
- Maximum: usually no max for pipe, but velocity > 15 ft/sec at outlets requires erosion protection (rip-rap, energy dissipator).

### 3.3 Detention vs. Retention vs. Infiltration

| Type | Function | Outlet | Standing water? |
|---|---|---|---|
| **Detention basin (dry pond)** | Slows release of stormwater to predevelopment peak | Orifice + overflow weir | No (drains 24–72 hrs after storm) |
| **Retention basin (wet pond)** | Holds water permanently, adds quality treatment | Overflow only at design WSEL | Yes, permanent pool |
| **Infiltration basin** | Soaks runoff into ground | None (or emergency overflow) | No |
| **Underground detention** | Same function as detention, underground (CMP, chamber, vault) | Outlet structure | No |

**Design intent**: hold the developed peak flow back so the released rate does not exceed the pre-development rate for the same storm. Typical regulatory rule: **release rate post-development ≤ pre-development for the 2-, 10-, and 100-year storms** (or some subset).

**Maintenance responsibilities** — usually transferred to the HOA, owner, or municipality at project closeout via a recorded **stormwater O&M agreement**. The GC's responsibility is typically:
- Construct to plan
- Establish vegetation/stabilization before turnover
- Perform first-year maintenance (often mowing, sediment cleanout from forebay)
- Deliver as-built drawings and the O&M manual

**LID (Low Impact Development) alternatives**:

| LID feature | Mechanism | Maintenance |
|---|---|---|
| **Bioretention / rain garden** | Engineered soil and plants filter and infiltrate | Mulch, replant, remove sediment yearly |
| **Vegetated swale** | Shallow grassed channel slows and filters | Mow, remove sediment |
| **Permeable pavement** | Water passes through pavement to base storage | **Vacuum sweeping** 2–4×/yr — without it, it clogs |
| **Green roof** | Soil + vegetation absorb and evapotranspire | Irrigation in dry season, weeding, structural inspection |
| **Cisterns / rainwater harvesting** | Capture for reuse | First-flush diverter, mosquito control |

### 3.4 Reading Drainage Plans

Standard symbols and conventions:

| Element | How it appears |
|---|---|
| Storm pipe | Solid line, often with double parallel lines or labeled "SD" |
| Sanitary | Dashed line, labeled "SS" or "S" |
| Water | Dotted/double-dotted, labeled "W" |
| Flow direction | Arrow on the pipe or in gutter |
| Inlet | Square or rectangle with "INLET", "CB", or grate hatching |
| Manhole | Circle, often with "MH" or structure ID |
| Pipe call-out | "24" RCP @ 0.50%, 145 LF" — diameter, material, slope, length |
| Rim elevation | At inlets/manholes; top of structure |
| Invert (IE / FL / INV) | Bottom inside of pipe at structure; usually shown for each pipe entering/leaving |

**Reading an inlet/manhole detail**:
- **Rim**: top of grate or cover. **Should match the surrounding finish elevation** (for grate inlets) or be slightly below (curb inlets, where the throat is below curb).
- **Invert In**: incoming pipe(s); list each separately by direction
- **Invert Out**: outgoing pipe (lower than the incoming)
- **Drop across structure**: typically 0.05–0.10 ft for straight-through, 0.10–0.30 ft for bends or junctions

**Crown vs. invert matching**: when pipe size increases at a junction, match **crowns** (top of pipe), not inverts. This keeps the hydraulic grade line continuous. Inverts will not match — that is intentional.

### 3.5 Utility Conflicts and Coordination

Drainage usually wins vertical conflicts (gravity flow is fixed). Water, gas, and electric have flexibility. Typical priority for vertical resolution:

1. Sanitary sewer (gravity, minimum slope, deepest)
2. Storm drain (gravity, larger but more flexible alignment)
3. Water main (pressure, easier to deflect, but 10-ft horizontal / 18-in. vertical separation from sewer per 10 States Standards)
4. Gas (pressure)
5. Telecom (pressure or shallow)
6. Electric (pressure or shallow)

**The 10-state separation rule** for water and sewer:
- **10 ft horizontal** between water main and any sewer
- **18 in. vertical** with water above sewer at crossings
- If you cannot meet separation, encase one (typically the sewer) in concrete or use ductile iron sewer for the crossing

---

## Part 4 — Utilities and Underground Infrastructure

### 4.1 Water Main

**Materials**:

| Material | Sizes | Pressure rating |
|---|---|---|
| **PVC C900 / C909** | 4 in. – 12 in. (C900); larger in C905 | DR18 = 235 psi; DR14 = 305 psi; DR25 = 165 psi |
| **Ductile Iron (DI)** | 3 in. – 64 in. | Pressure Class 350 standard for water (350 psi) |
| **HDPE** | Any | Various DRs; fused joints; common for trenchless |
| **Copper** | 3/4 in. – 2 in. | Service lines (Type K underground) |

**Connections / fittings**:
- **Mechanical joint (MJ)**: bolted gland with rubber gasket
- **Push-on**: rubber gasket, no bolts
- **Restrained joints**: required at bends, tees, and dead-ends to resist thrust (or use **thrust blocks** of concrete)
- **Thrust block sizing**: civil engineer provides; based on bearing capacity of native soil and the un-restrained force = pressure × cross-sectional area × sin(deflection/2) for bends

**Cover**: typically 36–48 in. for water mains (frost line varies by region — Minnesota requires 7–8 ft; Florida 18 in.).

**Disinfection and pressure testing** (AWWA C600, C651):
- **Pressure test**: 1.5× working pressure or 150 psi minimum, 2 hrs, with leakage allowance per AWWA formula
- **Disinfection**: chlorinate to 25 mg/L, hold 24 hrs, flush, **two consecutive bacteriological samples 24 hrs apart must show no coliform**. Plan 4–7 days minimum from main completion to in-service.

**Fire flow requirements**:
- Residential: typically 1,000–1,500 gpm at 20 psi residual for 2 hrs (IFC Appendix B)
- Commercial/multi-family: 1,500–4,000 gpm depending on building type/size and sprinklers
- Hydrant spacing: 300–500 ft on residential streets, 300 ft on commercial; max 100–250 ft from any point on a building
- Confirm available fire flow with the water utility's flow test **before** committing to building size/type — undersized mains can kill a project

### 4.2 Sanitary Sewer

**Gravity sewer**:

| Pipe size | Minimum slope (typical, 10 States Standards) | Min velocity at design flow |
|---|---|---|
| 4 in. (laterals) | 1.0% (1/8 in. per ft is often used = ~1.04%) | 2 ft/sec |
| 6 in. | 0.60% | 2 ft/sec |
| 8 in. | **0.40%** | 2 ft/sec |
| 10 in. | 0.28% | 2 ft/sec |
| 12 in. | 0.22% | 2 ft/sec |
| 15 in. | 0.15% | 2 ft/sec |

**Minimum slope is the floor**, not the goal. If you can build steeper without dropping into a pumping situation, do — flatter sewer is unforgiving in the field. Field error of ±0.05 ft on a 100-ft run is 0.05% — eats up most of an 8-in. line's safety margin.

**Manholes** are required at:
- All changes in direction, slope, pipe size, or material
- All pipe junctions
- Maximum spacing: 300–400 ft on small lines, 400–500 ft on larger
- Drop manholes when pipe drops > 24 in. through structure

**Cleanouts** on building sewers:
- At the building (within 5 ft)
- At property line
- Every 100 ft on long laterals
- At any 90° bend (or use two 45s with a cleanout between)

**Force mains** (pressure sewer from pump stations):
- Sized for 2 ft/sec min to keep solids in suspension, 8 ft/sec max
- Air release valves at high points
- Cleanouts and pig launchers/receivers for maintenance

**Sewer testing**:
- **Low-pressure air test (ASTM C828, C924)**: pressurize to 4 psig + groundwater head; time pressure drop from 3.5 to 2.5 psig; pass per length-and-diameter table
- **Mandrel deflection test**: pull a go/no-go mandrel through after backfill; max 5% deflection on flexible pipe (PVC SDR 35)
- **Vacuum test on manholes (ASTM C1244)**: 10 in. Hg pulled, time to drop to 9 in. Hg
- **CCTV inspection**: increasingly standard for acceptance — find sags, root intrusion, joint offsets the eye misses

### 4.3 Dry Utilities

| Utility | Cover (typical min) | Material | Easement width (typical) | Notes |
|---|---|---|---|---|
| **Gas (low pressure)** | 24 in. | PE (polyethylene), yellow | 10 ft | Tracer wire required if non-metallic |
| **Gas (medium/high)** | 36 in. | PE or steel | 15–25 ft | Engineering and special permitting |
| **Electric (primary)** | 36 in. (direct bury) or 30 in. (conduit) | Concentric neutral cable or in PVC conduit | 10–15 ft | Red warning tape 12 in. above |
| **Electric (secondary)** | 24 in. | Triplex or in conduit | 5–10 ft | |
| **Telecom (copper/fiber)** | 24 in. | Cable in HDPE conduit | 5 ft | |
| **CATV / fiber** | 18 in. | Cable | Joint trench with telecom common | |

**Joint trench**: dry utilities often share a trench to save excavation cost. Standard order top to bottom: telecom (shallowest), CATV, electric secondary, electric primary, gas (deepest). Minimum 12 in. vertical separation between electric and gas. Each utility's own inspector signs off.

**Crossings with water/sewer**: dry utilities cross wet, never share. Minimum 12 in. vertical separation at crossings.

### 4.4 811 / Call-Before-You-Dig

**Federal law (49 CFR 198) and state laws** require notification of underground utility owners before excavation. **Penalties for hitting a marked or unmarked utility can be six-figure** and the GC carries criminal exposure on gas lines.

**Process**:
1. Call 811 or submit online ticket 2–3 business days before digging (varies by state — Florida 2 days, California 2 days, Texas 2 days; some states 10 business days for design)
2. Each utility owner marks their facilities with color-coded paint/flags within the locate window:
   - **Red** — electric power
   - **Yellow** — gas, oil, steam
   - **Orange** — telecom, alarm
   - **Blue** — potable water
   - **Purple** — reclaimed water, irrigation
   - **Green** — sewer, storm drain
   - **Pink** — temporary survey markings
   - **White** — proposed excavation (GC marks before locator arrives)
3. **Locate is valid for a defined window** (typically 14–28 days). Re-call if you exceed it.
4. **Tolerance zone** (the buffer in which you must hand-dig): typically 18–24 in. each side of the mark
5. **Potholing / soft digging**: hydro-vac or air-vac to physically expose utilities at all crossings before machine digging the trench. **Do this. Every time.** A pothole costs $200; a service interruption claim costs $200,000.

**Unmarked utilities**: not uncommon, especially private services on commercial sites and abandoned lines. If you find one:
- Stop work immediately if it appears live
- Photograph and locate by GPS
- Notify the suspected owner and 811 for re-locate
- Do not assume abandoned utilities are de-energized — verify

### 4.5 Trenching and OSHA Subpart P (29 CFR 1926.650-652)

The standard most violated in residential work, the standard most likely to kill someone, and the standard with no acceptable workaround.

**Trench**: an excavation deeper than it is wide, max 15 ft wide at the bottom.
**Excavation**: any human-made cut or cavity in the ground.

**Soil classification** (for sloping/shoring choice):

| Type | Description | Max allowable slope (H:V) |
|---|---|---|
| **Stable rock** | Solid mineral material in place | 90° (vertical) |
| **Type A** | Cohesive, unconfined comp. strength ≥ 1.5 tsf (clay, silty clay, hardpan) | 0.75:1 (53°) |
| **Type B** | Cohesive 0.5–1.5 tsf, granular cohesionless (silt, sandy loam) | 1:1 (45°) |
| **Type C** | Granular cohesionless (gravel, sand, loamy sand), wet clay, submerged | 1.5:1 (34°) |

**Critical exclusions making any soil Type C**:
- Standing water in or beside the trench
- Previously disturbed (any backfill)
- Surcharge from spoil pile, equipment, or structure
- Layered system with cohesive over granular

**Protective system requirements**:

| Trench depth | Requirement |
|---|---|
| < 5 ft | Protective system not required **unless** competent person identifies a hazard |
| 5–20 ft | Sloping, benching, shoring, or shielding required |
| > 20 ft | Protective system must be **designed by a registered professional engineer** |

**Methods**:
- **Sloping**: cut the sides back per the soil-type table
- **Benching**: stair-step the sides — Type A and B only, not Type C
- **Shoring**: hydraulic, pneumatic, or timber bracing that holds the walls
- **Trench shield (box)**: prefabricated steel/aluminum box that protects workers inside; sides can be vertical because the workers are inside the box, but spoil and surcharge still must be controlled

**Spoil pile**: at least **2 ft from the edge** of the trench. Equipment and material the same.

**Access/egress**: ladder, ramp, or steps within **25 ft of laterally** any worker in a trench 4 ft or deeper.

**Competent person**: per OSHA, a designated individual with the training and authority to identify hazards and stop work. **Required on every excavation, every day, with daily and after-rain inspections logged.** Name them on a sign at the trench, document the inspection.

**Atmospheric hazards** for trenches > 4 ft where oxygen deficiency or hazardous atmospheres may exist (near sewers, landfills, gas mains): test before entry, ventilate as needed.

---

## Part 5 — Foundations from a Civil/Geotechnical Perspective

The structural engineer designs the foundation. The geotech sets the bearing capacity and soil parameters. The GC must understand what drives each foundation type so the soils report makes sense and so the field condition matches the design assumption.

### 5.1 Foundation Type Selection

| Type | Use case | Allowable bearing range | Notes |
|---|---|---|---|
| **Spread footing (isolated)** | Columns on adequate soil | 1,500–6,000+ psf | Most economical |
| **Continuous (strip) footing** | Bearing walls | Same | Standard residential |
| **Combined footing** | Two columns where one footing would encroach | Same | Property line columns |
| **Mat / raft** | Heavy loads on weak soils, or expansive soils | Low (300–1,500 psf) or stiffened on expansive | Distributes load |
| **Post-tensioned slab** | Expansive soils, high PI clay | n/a (slab on grade) | Tendons stressed after curing |
| **Drilled pier (caisson)** | Skin friction + end bearing through bad soil to good | 5,000–30,000+ psf at bell | 18–60+ in. dia., 10–80+ ft deep |
| **Driven pile** | Deep weak soils, high loads, marine | Variable | Steel H, pipe, precast concrete, timber |
| **Helical pier** | Light loads, weak surface soils, remedial | Torque-correlated | Underpinning, decks, light additions |
| **Micropile** | Tight access, low headroom, retrofit | Variable | Drilled, grouted, reinforced |

**Decision drivers** (in order of typical influence):
1. **Allowable bearing capacity** (from geotech)
2. **Loads** (from structural)
3. **Expansive soils** (drives slab type and depth of footing)
4. **Groundwater** (drives waterproofing and dewatering)
5. **Frost depth** (must extend below — varies by region)
6. **Adjacent structures** (settlement influence, underpinning)
7. **Cost and constructability**

**Frost depth (typical)**:

| Region | Frost depth |
|---|---|
| Gulf Coast / Florida | 0–12 in. (often no frost requirement) |
| Mid-Atlantic | 24–36 in. |
| Northeast | 42–48 in. |
| Upper Midwest (MN, ND) | 60–72 in. |
| Mountain West (CO, MT) | 36–60 in. |
| Alaska Interior | 84–120 in., plus permafrost considerations |

Footings must extend **below the local frost depth** to prevent frost heave. IRC Table R301.2(1) and local amendments govern.

### 5.2 Expansive Soils Detailed

Expansive soils shrink when dry and swell when wet. Differential moisture under a slab (wet under landscape, dry under interior) causes differential heave that cracks slabs and walls. Costs the US ~$2.3 billion/year in damage — more than floods, earthquakes, and hurricanes combined.

**Indicators on the boring log**:
- High PI (> 15, very high > 35)
- High EI (> 50)
- Atterberg liquid limit > 50
- USCS classification CH or MH
- High dry density with low moisture content (sometimes a sign of historic shrink)

**Mitigation strategies (geotech specifies)**:

| Strategy | Description |
|---|---|
| **Over-excavation and replacement** | Remove 24–60 in. of expansive soil under and around foundation; replace with select non-expansive fill |
| **Moisture conditioning** | Pre-wet the subgrade to a target moisture (often 3–5% above OMC) and hold; minimizes future swell |
| **Lime treatment** | 4–6% hydrated lime by dry weight blended into top 12 in.; chemically reduces PI |
| **Cement treatment** | Similar to lime, for lower PI clays |
| **Capillary break / moisture barrier** | Aggregate layer + vapor retarder under slab; perimeter membrane to depth of active zone |
| **Post-tensioned slab on grade** | PT tendons in two directions create a stiff slab that bridges localized heave |
| **Drilled piers + structural floor** | Bypass the active zone entirely; suspended slab with void form below |
| **Root barriers and irrigation control** | Prevent vegetation from drying soil under foundation (trees), prevent over-watering near foundation |

**Active zone**: depth to which moisture changes seasonally. Typically 5–15 ft. Foundations and barriers extending below the active zone are unaffected by seasonal heave.

**Common errors on expansive sites**:
- Conventional slab where PT was warranted — predictable cracking in year 1–3
- Inadequate perimeter drainage allowing wet soil under one side
- Landscape watering on one side and not the other — differential heave
- Trees too close to foundation — desiccation cracks, especially after tree removal (causes recovery heave 5+ years later)
- Plumbing leaks under slab — concentrated wetting causes heave; insurance disputes follow

### 5.3 Settlement

**Two types**:

| Type | Time scale | Soil types | Mechanism |
|---|---|---|---|
| **Immediate (elastic)** | Seconds–days | All, dominant in granular | Compression under load, no water expulsion |
| **Consolidation** | Months–years | Clay (especially soft) | Slow expulsion of pore water |
| **Secondary compression** | Years–decades | Organic clay, peat | Creep under sustained load |

**Differential settlement** matters more than total. A building can tolerate 6 in. of uniform settlement if every column drops the same; ½ in. of differential between adjacent columns cracks finishes.

**Typical tolerable differential settlement** for various structures (Skempton & MacDonald, widely cited):

| Structure type | Δ/L (angular distortion) | Δ between adjacent columns (typical) |
|---|---|---|
| Buildings with masonry walls (cracking limit) | 1/500 | < 1/2 in. |
| Steel frame, flexible | 1/300 | < 1 in. |
| Slab on grade, wood frame | 1/250 | Roughly 1 in. over 20 ft span |
| Bridges | 1/250–1/500 | Varies |

The geotech projects total and differential settlement. If projected differential exceeds tolerable, the foundation type or soil treatment must change.

### 5.4 Groundwater and Dewatering

If the water table is at or above the bottom of excavation, you must dewater to work in the dry. Methods:

| Method | Typical use | How it works |
|---|---|---|
| **Sump pumping** | Shallow, low flow (< 50 gpm), short-term | Pump from a sump pit dug at the bottom of excavation |
| **Trenching with sump** | Strip excavations | Perimeter trench drains to a sump |
| **Wellpoints** | 5–18 ft drawdown, moderate flow | Series of small wells (1.5–2 in.) on a header pipe, vacuum |
| **Deep wells** | > 20 ft drawdown, high flow | Individual large-dia. wells with submersible pumps |
| **Sheet piling** | Cut off horizontal flow | Driven steel sheets; combined with internal pumping |
| **Slurry wall / soil mix wall** | Deep, contaminated, or sensitive | Cement-bentonite cutoff wall |
| **Ground freezing** | Tunneling, contaminated | Brine circulation freezes a wall of soil |

**Discharge regulation**: dewatering discharge often requires a **construction dewatering permit** (state NPDES) — water from the trench may contain sediment, oil, or contamination from prior site use. Filter through a dewatering bag or sediment tank before discharge to a storm system or surface water. Some sites prohibit discharge entirely and require off-site disposal.

**Seasonal effects**: water table can vary 5–10 ft seasonally. A geotech boring in dry season at 12 ft may be at 4 ft in wet season. **Always check both seasonal high and seasonal low.**

### 5.5 Seismic Design Considerations

The IBC defines **Seismic Design Categories (SDC) A through F** based on (1) Site Class (soil profile), (2) mapped spectral accelerations (Ss, S1) from USGS, and (3) Risk Category (occupancy importance).

**Site Class** (ASCE 7 Chapter 20):

| Class | Description | Vs (shear wave velocity) or N |
|---|---|---|
| **A** | Hard rock | Vs > 5,000 ft/sec |
| **B** | Rock | 2,500–5,000 ft/sec |
| **C** | Very dense soil / soft rock | 1,200–2,500 ft/sec |
| **D** | Stiff soil | 600–1,200 ft/sec (most sites default here without testing) |
| **E** | Soft clay | < 600 ft/sec or specific PI/moisture/su criteria |
| **F** | Hazardous (liquefiable, sensitive clay, organic) | Site-specific analysis required |

Site Class matters because softer sites **amplify** ground motion — sometimes 2–4×. The same earthquake puts very different forces on a Site Class B building vs. a Site Class D building.

**SDC drives**:
- Lateral force-resisting system options
- Detailing requirements
- Quality assurance and special inspections
- Soil-structure interaction concerns

**SDC A and B**: low seismicity; minimal special detailing
**SDC C**: moderate; some special detailing
**SDC D, E, F**: high; full special seismic detailing, third-party special inspection, peer review on some structures

**Liquefaction** (revisited): saturated loose-medium dense sands lose strength under cyclic loading. Triggers ground deformation, lateral spread, settlement, loss of bearing. Mitigated by:
- Densification (vibro-compaction, dynamic compaction, stone columns)
- Drainage (gravel drains to relieve pore pressure)
- Deep foundations through the liquefiable layer
- Removal and replacement (for shallow layers)

The civil/geotech identifies; the GC does not decide.

---

## Part 6 — Roads and Paving

### 6.1 Pavement Types

| Type | Surface | Base | Use |
|---|---|---|---|
| **Flexible (asphalt)** | Hot-mix asphalt (HMA) | Aggregate base + subbase | Most residential, commercial parking, lower-volume |
| **Rigid (concrete)** | PCC slab | Aggregate or stabilized base | Heavy/industrial loads, intersections, longer life |
| **Composite** | HMA over PCC | Existing rigid base | Reconstruction overlays |
| **Permeable** | Porous asphalt, pervious concrete, pavers | Open-graded stone reservoir | Stormwater LID |

**Asphalt advantages**: lower first cost, faster to construct, easier to repair, quieter, can be opened to traffic in hours.
**Concrete advantages**: longer service life (30–40 yr vs. 15–20 yr), lower long-term maintenance, better in industrial loading and high-temperature climates.

### 6.2 Subgrade Strength — R-value and CBR

The structural capacity of the underlying soil drives pavement section thickness.

| Measure | Used in | Range | Notes |
|---|---|---|---|
| **CBR (California Bearing Ratio, ASTM D1883)** | National, AASHTO design | 1 (soft clay) – 80+ (well-graded gravel) | Most common today |
| **R-value (Hveem stabilometer)** | California Caltrans, some western states | 5 (CH clay) – 80+ | Caltrans-specific |
| **Resilient modulus (Mr)** | AASHTO ME design | psi value, correlates roughly to 1500×CBR | Lab test, modern design |

**Typical CBR by soil**:

| Soil | CBR |
|---|---|
| CH (fat clay) | 2–5 |
| CL (lean clay) | 5–10 |
| ML/MH (silt) | 5–10 |
| SC (clayey sand) | 8–15 |
| SM (silty sand) | 15–30 |
| SP/SW (clean sand) | 20–40 |
| GW (well-graded gravel) | 60–80 |
| Crushed aggregate base | 80–100 |

If your subgrade has a CBR of 3 and the pavement was designed assuming 5, the pavement will fail prematurely (years, not decades). The geotech specifies the design CBR; the GC must deliver it (via subgrade improvement or thicker section).

### 6.3 Typical Sections

**Residential street (low volume, ESALs < 200K)**:
- 2 in. HMA surface (Superpave 12.5 mm or similar)
- 3 in. HMA base or 6 in. aggregate base on stabilized subgrade
- Compacted subgrade at 95% Modified Proctor

**Light commercial parking lot (passenger vehicles)**:
- 2.5–3 in. HMA (in 1 or 2 lifts)
- 6 in. aggregate base (Class 5 or similar, dense-graded)
- 95% Modified Proctor subgrade

**Heavy commercial parking, truck access**:
- 4 in. HMA (1.5 in. surface + 2.5 in. base) **or** 5–6 in. PCC
- 8–12 in. aggregate base
- Stabilized subgrade if CBR < 5

**Truck dock / dumpster pad**:
- 6–8 in. PCC, doweled across joints
- 6 in. aggregate base
- 4,000 psi minimum, often 4,500

### 6.4 Asphalt Mixes

| Mix | Description | Use |
|---|---|---|
| **Dense-graded HMA (Superpave)** | Continuous gradation, low voids | Standard surface and base |
| **Open-graded friction course (OGFC)** | High voids for drainage | Wet-climate surface, reduces hydroplaning |
| **Stone Matrix Asphalt (SMA)** | Gap-graded, polymer-modified, high stone content | Heavy-truck routes, long life |
| **Cold mix** | Emulsified asphalt, no heat | Patch repairs, temporary work |
| **Recycled (RAP / WMA)** | Reclaimed asphalt pavement or warm mix | Cost and sustainability, watch quality |

**Lift thicknesses**:
- Maximum compacted lift: roughly **3× nominal max aggregate size**. A 12.5 mm Superpave mix can be placed up to ~1.5–2 in. compacted; a 19 mm base mix up to ~3 in.
- Minimum lift: roughly 2× nominal max aggregate (any thinner and the mix tears under the screed)
- **Density**: typical spec is **92–96% of theoretical maximum (Gmm)** at acceptance. Insist on cores or nuclear density. A 2% drop in density is roughly a 10% drop in fatigue life.

**Temperature**:
- Place at 280–320°F at the truck, 250°F minimum behind the screed
- Compaction temperature window closes quickly in cold weather — avoid placement below 50°F ambient on thin lifts
- Tack coat (between lifts): 0.05–0.10 gal/yd² emulsion, allowed to break before paving

### 6.5 Concrete Paving

**Mix**: 4,000–4,500 psi at 28 days; air-entrained 5–7% for freeze-thaw climates; w/c ratio ≤ 0.45 for durability.

**Joints**:

| Joint | Spacing | Detail |
|---|---|---|
| **Contraction (sawed)** | 24–36× slab thickness in feet (max ~15 ft on 6-in. slab) | Sawed 1/4 to 1/3 depth within 4–12 hours of finishing |
| **Construction** | Where work stops | Doweled and keyed |
| **Isolation** | Around structures, fixed objects | Full-depth, expansion material |
| **Longitudinal** | Lane lines, 12–15 ft max width | Tie bars across to prevent separation |

**Reinforcement**:
- **Dowels**: smooth bars across **transverse contraction joints**, allow horizontal load transfer, allow opening/closing. Typical: #5–#8, 12–18 in. long, 12 in. o.c., greased one side.
- **Tie bars**: deformed bars across **longitudinal joints**, hold lanes together, prevent opening. Typical: #4–#5, 24–30 in. long, 24–30 in. o.c.
- **Welded wire fabric** or fiber for crack control (in unreinforced JPCP, neither is structural).

**Curing**:
- Wet cure 7 days minimum, OR
- Curing compound applied immediately at 1 gal/150 ft² (white-pigmented in hot weather)
- Failure to cure properly is the #1 cause of premature surface failure (scaling, dusting, crazing)

**Texture / finish**:
- Broom finish standard for sidewalks and most driveways
- Tined finish (raked) for higher friction on roads
- Smooth or rotary float for indoor/decorative
- Skid resistance: BPN > 55 wet (British Pendulum Number) on roadways; coefficient of friction > 0.6 for slip resistance in pedestrian areas

### 6.6 ADA Requirements for Site Work

The Americans with Disabilities Act (ADA) Standards for Accessible Design (2010) and **Public Right-of-Way Accessibility Guidelines (PROWAG)** govern. Key thresholds — **memorize these**:

| Element | Requirement |
|---|---|
| **Accessible route — running slope** | ≤ 5.0% (1:20) without becoming a ramp; > 5% triggers ramp requirements (handrails, landings) |
| **Accessible route — cross slope** | ≤ 2.0% (1:50). **The killer spec.** Most field failures are here. |
| **Ramp — slope** | 1:12 max (8.33%); 1:16–1:20 strongly preferred |
| **Ramp — landings** | 60 in. min length, top and bottom, every 30 ft of run, every change of direction |
| **Ramp — handrails** | Both sides, 34–38 in. above ramp, when rise > 6 in. or run > 72 in. |
| **Curb ramp** | 1:12 max running slope; flared sides 1:10 max if pedestrian path crosses |
| **Detectable warning** | Truncated dome strip 24 in. deep at curb ramps and platform edges; contrast color |
| **Accessible parking — slope** | ≤ 2.0% any direction (including drainage) |
| **Accessible parking — space dimensions** | 96 in. wide × 18 ft long, with 60 in. access aisle (96 in. for van) |
| **Accessible parking — number** | Per ADA Standards 208: 1 of first 25, then sliding scale; minimum 1 of every 6 accessible spaces is van-accessible |
| **Doorway approach — level area** | 60 in. × 60 in. at door, max 2% any direction |

**Field measurement tip**: smart level or digital inclinometer accurate to 0.1%. Survey-grade for acceptance, hand level for QC during construction. Stake elevations to 0.01 ft on accessible routes. **Re-verify after every grading pass** — a curb that was 2.0% becomes 2.3% after the contractor "fixed" the puddle next to it.

### 6.7 Signage, Striping, Traffic Control

Standardized by the **Manual on Uniform Traffic Control Devices (MUTCD)** — federally adopted, state-amended.

**Pavement marking materials**:
- **Latex paint**: cheapest, 6–12 month life. Residential and low-traffic.
- **Thermoplastic**: heated and applied 90–125 mil thick, 3–7 yr life. Standard for commercial.
- **Preformed thermoplastic / tape**: legends, symbols, ADA markings.
- **Epoxy / methacrylate**: long life, high cost, busy commercial.
- **Reflective beads**: dropped on wet paint or thermoplastic for night visibility.

**Common striping specs**:
- Single solid line: 4 in. wide
- Double yellow centerline: two 4 in. lines, 4 in. gap
- Stop bar: 12–24 in. wide
- Crosswalk: 6 in. or 12 in. wide lines, 8–12 ft length
- Accessible space symbol: 36 in. min, white on blue background

**Traffic control during construction (Temporary Traffic Control, TTC)**:
- **MUTCD Part 6** governs
- Need a TCP (Traffic Control Plan) for any work in a ROW
- Flaggers must be **certified** in many states (ATSSA card, state DOT card)
- Signage taper lengths, cone spacing, lighted barricades — all per MUTCD tables
- Night work: type III barricades with steady-burn or flashing lights; reflective vests (ANSI 107 Class 2 day / Class 3 night)

---

## Part 7 — Reading Civil Drawing Sets

### 7.1 Sheet Organization (Typical Order)

| Sheet code | Content |
|---|---|
| **C-0.0 / G-0.0** | Cover sheet — vicinity map, sheet index, code references, contact list |
| **C-1.0** | Existing conditions / demolition plan |
| **C-2.0** | Site / horizontal control plan — building footprint, parking layout, dimensions |
| **C-3.0** | Grading and drainage plan — contours, spot grades, swales |
| **C-4.0** | Utility plan — water, sewer, storm in one or separate sheets (C-4.1, C-4.2, etc.) |
| **C-5.0** | Paving plan — limits, sections, joint layout |
| **C-6.0** | E&SC plan — phase 1 (initial), phase 2 (mass), phase 3 (final) |
| **C-7.0** | Landscape (sometimes L-sheets) |
| **C-8.0+** | Details — typical sections, structures, pavement, retaining walls |
| **C-9.0+** | Profiles — sewer, storm, water (with stations and elevations) |

Larger projects break each discipline into 10+ sheets; small projects may combine grading and utility on one sheet.

**Title block essentials**:
- Project name, address, owner
- Sheet number and total ("C-3.0 of 18")
- Scale (horizontal **and** vertical for profile sheets — often different)
- Date, revisions log
- **PE stamp** (live signature/seal, the licensed engineer of record)
- North arrow

### 7.2 Standard Abbreviations and Symbols

Memorize these — they appear on every civil set:

| Abbr | Meaning | Abbr | Meaning |
|---|---|---|---|
| AC | Asphaltic concrete | LP | Low point |
| BC | Begin curve / Back of curb | LF | Linear feet |
| BFE | Base flood elevation | MH | Manhole |
| BVC | Begin vertical curve | NTS | Not to scale |
| BW | Bottom of wall | OG | Original / existing ground |
| C&G | Curb and gutter | PCC | Portland cement concrete or Point of compound curve |
| CB | Catch basin | PI | Point of intersection (or Plasticity Index, in geotech) |
| CL | Centerline | POB | Point of beginning |
| CY | Cubic yards | PT | Point of tangency |
| DI | Drop inlet / Ductile iron | PVI | Point of vertical intersection |
| EC | End curve | R/W or ROW | Right of way |
| EG | Existing grade | RCP | Reinforced concrete pipe |
| EOP | Edge of pavement | SD | Storm drain |
| EVC | End vertical curve | SS | Sanitary sewer |
| FF / FFE | Finish floor elev. | SF | Square feet / Silt fence |
| FG | Finish grade | STA | Station |
| FH | Fire hydrant | TBM | Temporary benchmark |
| FL | Flow line | TC | Top of curb |
| GB | Grade break | TW | Top of wall |
| GV | Gate valve | TYP | Typical |
| HP | High point | WSEL | Water surface elevation |
| INV / IE | Invert elevation | WV | Water valve |

**Stationing**: linear projects use stations along a centerline. **STA 5+47.32** means 547.32 ft from the project beginning along the centerline. Used for sewer, road, and any linear work.

### 7.3 Construction Limits, ROW, and Easements on Plans

- **Property line**: heavy long-short-short dash, often with bearings and distances
- **ROW line**: similar but typically labeled "R/W"
- **Easement**: lighter dashed line, often hatched on one side, **always labeled** with width and purpose
- **Construction limits / Limits of disturbance (LOD)**: heavy dashed line — **this is where the GC may work; everything outside is owner's, neighbor's, or protected. Stake it.**
- **Tree protection fence / zone**: dashed line with tree symbols inside
- **Wetland buffer / Conservation easement**: heavy dashed, often shaded
- **Silt fence and other E&SC**: shown on the E&SC sheet with their own symbology

### 7.4 GC Responsibility vs. Engineer Review

| Item | GC owns | Engineer owns / approves |
|---|---|---|
| Construction means and methods | Yes | No |
| Conformance to plan (location, elevation, materials) | Yes | Verifies via inspection |
| Field-fit minor changes within tolerance | Yes (small) | No (significant) |
| Substitutions of specified materials | Submit for approval | Approves/rejects |
| Shop drawings for structural items (precast, retaining walls > 4 ft, etc.) | Submit | Reviews and stamps |
| Mix design submittals (concrete, asphalt) | Submit | Reviews |
| Compaction and density results | Generates / reviews | Geotech accepts |
| As-built / record drawings | Produces | Reviews, certifies for closeout |
| Survey layout (corner stakes, offsets) | Hires surveyor | Verifies controlling points |
| Stamped engineering changes in field | Cannot | Issues field directive or RFI response |
| Permit pull (building, grading, ROW, utility) | Typically | Stamps the drawings supporting them |
| Stormwater inspections during construction | Performs and logs | May audit |
| Final certifications (engineer's letter for CO) | Cannot | Issues at closeout |

**Critical line**: if a field condition differs from the plan or the plan does not work, the GC submits an **RFI** (Request for Information). The engineer responds with direction (field directive, plan revision, ASI — Architect's/Engineer's Supplemental Instruction). **The GC never invents a fix that affects design intent.** Photograph everything, document the RFI, wait for the response, then execute.

---

## Part 8 — Managing Civil Subcontractors

### 8.1 Scope Definition and Bid Leveling

The single biggest source of civil cost overruns is sloppy scope. Each civil sub bid must include the same scope or you cannot compare bids. A bid-leveling matrix is the discipline.

**Standard scopes split**:

| Sub | Typical scope |
|---|---|
| **Earthwork / mass grading** | Clearing, stripping topsoil, cut/fill, building pads, rough grading, import/export, dust control, fine grading to subgrade |
| **Underground utilities (wet)** | Storm drain, sanitary sewer, water main, services to building, manholes/structures, testing |
| **Dry utility joint trench** | Trench, sand bedding, conduit/cable installation per utility company specs, backfill, restoration |
| **Paving** | Aggregate base, asphalt or concrete, striping, signage, ADA detection |
| **Concrete flatwork (sitework)** | Curb and gutter, sidewalks, driveway approaches, ADA ramps |
| **Retaining walls** | Material supply and installation; sometimes split between wall sub and earthwork for backfill |
| **Erosion control** | Install, maintain, remove BMPs; SWPPP inspections (sometimes a separate consultant) |
| **Landscape / final grading** | Topsoil placement, hydroseed, plantings |

**Common scope gaps causing change orders**:
- Who pays for over-excavation if subgrade fails proof-roll?
- Who pays for unsuitable material disposal? (Define "unsuitable" — use the geotech's definition)
- Who pays for dewatering? (Almost always earthwork or underground sub; verify before bid)
- Who pays for utility company tap fees, meters, transformers?
- Who pays for testing (compaction, concrete, asphalt)? (Industry standard: owner pays for **acceptance** testing; sub pays for **QC** testing of their own work)
- Who pays for traffic control and ROW permits?
- Who pays for SWPPP inspections, weekly reports, BMP repair after storms?
- Who pays for survey layout? (GC usually owns; sub responsible for fine grading from offsets)
- Who pays for as-built drawings? (Sub provides red-lines; GC's surveyor or engineer prepares final)

**Bid-leveling matrix** — row per scope item, column per bidder, mark Y/N/clarification. Send a clarification RFI back to any bidder with a gap. Award only on apples-to-apples.

### 8.2 Productivity Norms (For Sanity Checks, Not Commitments)

These vary by site, equipment, crew skill, soil, and weather. Use as a reality check on schedules and quotes — too high a number means inflated; too low means a problem in the bid.

**Earthwork**:

| Activity | Production |
|---|---|
| **Cat D6/D8 dozer pushing** (200 ft haul, average soil) | 250–500 BCY/hr |
| **Cat 365 excavator loading trucks** (mass excavation) | 150–300 BCY/hr |
| **CAT 950 wheel loader loading** | 150–250 BCY/hr |
| **Scraper (CAT 627)** (medium haul 1,500 ft, no push assist) | 80–150 BCY/hr per scraper |
| **Truck haul (10 CY dump)** | Cycle-time driven; 8–15 BCY/hr round trip per truck for 5-mile haul |
| **Smooth drum roller compacting** | 1,000–2,000 SY/hr per lift |
| **Mass site grading (typical residential subdivision)** | 2,000–5,000 BCY/day per spread (dozer + scraper + roller + water truck) |

**Pipe installation**:

| Activity | Production |
|---|---|
| **8-in. PVC sanitary, normal depth 8–12 ft, open cut** | 200–400 LF/day per crew of 4–6 |
| **24-in. RCP storm, open cut** | 100–200 LF/day |
| **48-in. RCP storm, open cut** | 40–80 LF/day |
| **8-in. DI water main, normal depth** | 200–400 LF/day |
| **Manhole installation (standard 4 ft dia.)** | 1–3 per day |
| **Service connections (sewer or water)** | 4–8 per day per crew |
| **Boring / directional drilling (4–8 in. casing)** | 100–300 LF/day depending on soil |

**Paving**:

| Activity | Production |
|---|---|
| **Aggregate base placement and compaction** | 1,000–3,000 SY/day per crew |
| **Asphalt paving — surface course, 2 in.** | 1,000–3,000 tons/day for commercial paver |
| **Asphalt paving — small parking lot, 1 paver** | 500–1,000 tons/day |
| **Concrete curb and gutter (slipformed)** | 500–1,500 LF/day |
| **Concrete sidewalk (4 in.)** | 1,000–3,000 SF/day per crew |
| **Striping (paint, single line)** | 5,000–15,000 LF/day |

**Reality check**: if a bidder is 40% above or below these ranges on labor hours or duration, ask why.

### 8.3 Quality Control Checkpoints

| Phase | Hold point — do not proceed past until verified |
|---|---|
| **Pre-construction** | Survey control verified, benchmarks established, locates complete, SWPPP in place |
| **Stripping** | Topsoil depth measured; debris/organics removed |
| **Subgrade preparation** | Proof-roll witnessed; pumping areas addressed; density tests at frequency |
| **Building pad** | Final density tests; pad elevation verified; geotech approval letter |
| **Footing excavations** | Soil verified by geotech; bearing capacity confirmed; bottom hand-cleaned |
| **Underground utilities** | Pre-pour: alignment, slope, joints; mid-backfill: bedding inspected, density tested; final: pressure/leak/vacuum test passed |
| **Backfill of utilities** | Density tested at lifts; no proceeding without passing tests |
| **Aggregate base** | Thickness, gradation (per spec), density, surface tolerance ±1/2 in. |
| **Asphalt** | Mix temperature at truck and behind screed; density cores; thickness cores; smoothness (IRI on roads); surface tolerance |
| **Concrete pavement** | Slump, air, temperature, cylinders; thickness probes; jointing pattern; cure protected |
| **Storm/sanitary final** | CCTV inspection; mandrel deflection; manhole vacuum; as-built |
| **Site final** | All grades verified, ADA slopes verified, striping complete, signage installed, E&SC removed only after final stabilization |

**Testing schedule template** — work with the geotech and structural engineers to set up a project-specific schedule. Issue it before mobilization. Track tests in a log. **Withholding payment on a sub for missing tests is the only language they hear.**

### 8.4 Common Disputes and How to Win Them

**1. Earthwork quantity dispute** (the most common)
- Source: sub claims more cut/fill than the GC paid for, or claims plan quantities were wrong
- **Defense**: pre-construction survey (topo before stripping), interim cross-sections at hold points, post-grading survey. Pay on **measured** quantities, not on visual estimates or truck counts alone.
- Contract clause: define how quantities are measured (BCY in place from cross-sections is the gold standard) and the survey method.

**2. Unsuitable material claim**
- Source: sub encounters material they claim is unsuitable for re-use, demands haul-off and import
- **Defense**: define unsuitable in the contract (per the geotech report's criteria — typically organics > 2%, PI above threshold, debris, etc.). Require sub to notify in writing within 24 hrs of discovery, before disposing. **Photograph everything, weigh tickets, sample for lab test if disputed.**

**3. Changed conditions / Differing Site Conditions**
- Source: subsurface condition differs materially from what the geotech report indicated (e.g., rock encountered where none was reported, water table higher than reported)
- **Defense**: contract should clearly assign the geotech report to the bidders' use; standard AIA A201 §3.7.4 has a Type 1 (differs from contract docs) and Type 2 (differs from norm for area) differing site conditions clause. Notice requirements are short — 14–21 days, sometimes less.
- **Reality**: a real changed condition is a legitimate change order. A "discovered" condition the sub should have anticipated based on the geotech report is not.

**4. Compaction failure on backfill**
- Source: tests fail after sub has backfilled and moved on; sub claims it was the GC's water/utility crew that disturbed it
- **Defense**: test in lifts, not at the end. Require the sub to call for test before each lift covers the previous. If the sub backfilled without inspection, the failed test is their problem — they re-excavate and retest.

**5. Pavement thickness short**
- Source: cores reveal pavement < spec
- **Defense**: thickness probes during placement; cores at acceptance. Specification penalty: typically a pay deduction at small shortages (e.g., 5% deduction per 0.25 in. short) and **removal and replacement above a defined threshold** (e.g., > 0.5 in. short).

**6. Dewatering scope and discharge**
- Source: sub installs minimal dewatering, can't keep up, demands GC pay extra; or discharge violates SWPPP and gets cited
- **Defense**: include a dewatering plan as a submittal requirement before mobilization, with discharge management. Most state SWPPP regs require a dewatering BMP — make this explicit in the scope.

**7. Utility tie-in fees and connection charges**
- Source: city or utility company charges that were not in the bid
- **Defense**: define in scope clearly. Tap fees, meter fees, system development charges are typically **owner's cost**. Connection labor and materials are **sub's cost**. Permit fees: typically owner.

**8. Survey errors and field changes**
- Source: surveyor staked wrong, sub built to stakes, has to redo
- **Defense**: a layout error caught early is cheap; caught late is catastrophic. Verify layout at every major hold point — first footing, first manhole, first pipe segment. Survey QC pass before pouring critical elements.

---

## Part 9 — Working Checklists and Field Quick-Reference

### 9.1 Pre-Bid Site Visit Checklist

- Drive the site perimeter and walk it — every corner, every easement, every existing utility
- Photograph existing conditions, including off-site adjacent and any visible damage
- Note access routes for trucks and equipment — height/weight restrictions, turning radii
- Look for water — springs, wet spots, ponding, vegetation indicators
- Check for buried debris (concrete chunks, asphalt, old foundations, old septics)
- Identify existing utilities visible above ground (pedestals, vaults, hydrants, poles, manholes)
- Note adjacent structures — protection, party walls, settlement concerns
- Check for trees protected by ordinance — measure DBH
- Talk to neighbors when possible — they know about flooding, old structures, prior earthwork
- Locate the closest fire hydrant for fire flow planning
- Check noise/dust restrictions in the area
- Soils visible in any cuts (roadway, ditches) — clay color, gravel content
- Sun and wind exposure — affects concrete cure and dust control
- Cell coverage on site — affects 811 calls, surveys with RTK, daily ops
- Note neighbors' downhill slopes — your stormwater plan affects them

### 9.2 Geotech Report Review Checklist

- [ ] Was the report prepared for THIS project, not a neighbor's? Check the title page and scope.
- [ ] Number and depth of borings — adequate for the building footprint? Spaced reasonably?
- [ ] Date of borings — within the last 12 months? Different season than expected construction?
- [ ] Groundwater observations — both initial and stabilized
- [ ] PI and EI for clay layers
- [ ] Allowable bearing pressure — matches structural assumption?
- [ ] Recommended foundation type — matches design?
- [ ] Subgrade preparation specifics (strip depth, scarify depth, over-ex if any)
- [ ] Compaction specs — standard or modified Proctor, what %
- [ ] Pavement section recommendations — matches civil plans?
- [ ] Seismic site class — matches structural design?
- [ ] Liquefaction analysis if applicable
- [ ] Construction observation recommendation — who is doing it?
- [ ] Caveats and "additional investigations recommended" — addressed?
- [ ] Any specific recommendation for the geotech to review the design? Verify they did.

### 9.3 Pre-Pour / Pre-Backfill Inspections

**Footings**:
- [ ] Excavation matches plan (length, width, depth)
- [ ] Bottom clean — no loose soil, water, mud, debris
- [ ] Bearing strata verified by geotech (sign-off in writing)
- [ ] Reinforcement size, spacing, cover, splices per plan
- [ ] Anchor bolts / dowels / sleeves placed per plan
- [ ] Forms plumb, braced, tight at joints
- [ ] Concrete delivery ticket reviewed — mix, time batched, water added

**Slab on grade**:
- [ ] Subgrade compaction tests passed
- [ ] Base course in place, compacted, to elevation
- [ ] Vapor barrier (10–15 mil) lapped 6 in., taped, sealed at penetrations
- [ ] Reinforcement (rebar/PT/WWF) properly elevated on chairs
- [ ] PT tendons — sleeves at ends, no kinks, dead-end anchors confirmed
- [ ] Sleeves for plumbing, electrical, gas through the slab
- [ ] All embedded items (anchor bolts, hold-downs) properly located

**Backfill of utility**:
- [ ] Pipe pressure / leak / vacuum tested
- [ ] Bedding 4–6 in. of approved material under and 12 in. above pipe
- [ ] No rocks > 1.5 in. against the pipe
- [ ] Lift thickness ≤ 12 in. loose
- [ ] Compaction tests at frequency, passing

### 9.4 ADA Field Verification

After grading, before paving signoff, walk every accessible route with a smart level:

- [ ] All accessible parking spaces: max 2% any direction
- [ ] All accessible access aisles: max 2% any direction
- [ ] Curb ramps: 1:12 max, flares 1:10, detectable warning installed correctly
- [ ] Crosswalks: no high curbs, smooth transitions
- [ ] Accessible route running slope ≤ 5% (or it becomes a ramp)
- [ ] Accessible route cross slope ≤ 2%
- [ ] Doorway landings: 60 in. × 60 in., ≤ 2%
- [ ] Vertical clearance 80 in. min over walking surfaces (signage, branches, awnings)
- [ ] Surface stable, firm, slip resistant — no gravel, no soft surfaces on accessible routes

**Document with photos and a slope diagram**. ADA non-compliance is one of the few issues that can survive certificate of occupancy as an enforcement liability against the owner. Owners come back to GCs for these.

### 9.5 Closeout Documents the Civil Engineer Needs

- [ ] Stamped as-built drawings (often the same engineer who designed redlines them, but the GC delivers field changes)
- [ ] Compaction test reports (full file)
- [ ] Concrete/asphalt mix tickets, cylinders, density cores
- [ ] Pressure test reports for water main
- [ ] Air test, vacuum test, CCTV for sanitary
- [ ] CCTV for storm drain
- [ ] Bacteriological clearance for water
- [ ] SWPPP closeout — final stabilization documentation, Notice of Termination
- [ ] FEMA Elevation Certificate (in flood zones)
- [ ] ADA verification (slope survey)
- [ ] O&M manual for stormwater facilities
- [ ] Survey of as-built monuments, valve locations, manhole rims/inverts
- [ ] Easement and right-of-way recordings if any
- [ ] Maintenance bonds / warranties (1-yr typical, longer in some specs)

The engineer of record usually owes the owner a **letter of substantial conformance** at closeout — they cannot issue it without the GC's documentation. Withholding records delays closeout, retainage release, and final payment. Set up the closeout binder from day one.

---

## Part 10 — Common Civil Mistakes (and the GC's Pre-emptive Counter)

| Mistake | Cost | Counter |
|---|---|---|
| Building 18 in. into a side-yard easement because the surveyor missed a recorded utility easement | Tear out a corner or buy a release; $20K–$200K | Demand a current title commitment; cross-reference Schedule B-II against the survey before layout |
| Setting FFE 6 in. low because the architect's elevation and the civil's elevation were in different datums | Sloping driveway redo, threshold rebuild, sometimes lender flood rejection | Confirm datum on both drawings; if NGVD29 vs. NAVD88, get the offset in writing |
| Pad compaction tested in the easy spots, not on the slope edges | Slab cracks within 1 year; geotech blames the GC | Specify and witness test locations; refuse the testing report if locations are not on a map |
| Wet weather during fill placement; sub pushes wet clay anyway | Pad pumps, fails proof-roll, gets re-done | Suspend filling during/after rain; let the soil dry; do not let schedule pressure override moisture control |
| Underground sewer "passing" pressure test but failing CCTV at acceptance | Bellies and sag = re-excavate sections | Require laser-level checked between manholes during installation, not just at end |
| Storm drain undersized because the engineer used a 5-min Tc when the actual is shorter | Backups during heavy storms, owner sues GC and engineer | Sanity-check the hydrology — Tc of 5 min on a 1-acre flat parking lot is fine; on a steep half-acre lot, may be too long (overestimates pipe capacity)? Actually shorter Tc gives higher intensity i, so longer Tc gives smaller pipe. If the math looks aggressive, ask the engineer to show the work. |
| Hitting a fiber optic cable that was not marked | Repair costs + business interruption claims; can exceed $500K | Always pothole at crossings; if 811 marks seem off, request a re-locate |
| ADA cross slope at 2.5% because the contractor smoothed a puddle | Failed final inspection, occupancy delay | Verify every accessible route with a smart level after every grading pass |
| Trench collapse, fatality | Criminal exposure, OSHA citations, loss of the company | Have a competent person on every trench, every day, with daily inspection logged. **No exceptions for "it's only a short trench."** |
| Expansive clay foundation built per the structural plans but with no perimeter drainage | Heave in 18 months, claims for years | If the soils report calls for perimeter drainage and the plans omit it, file an RFI before mobilization |
| Permeable pavement installed but never specified for vacuum sweeping; clogs in 18 months | Owner blames the GC for "defective work" | Make maintenance requirements explicit in the closeout O&M; document the handover |

---

## Closing Notes — How the GC Stays in Front

1. **Read the geotech before the structural.** Bearing capacity and soil class drive everything else. Half the construction problems trace back to a soils report that nobody on the GC's team actually read.
2. **Stake everything that matters.** Easements, setbacks, construction limits, tree-protection zones, FEMA limits, wetland buffers. The cost of stakes is trivial; the cost of unstaked encroachment is not.
3. **Pre-pour and pre-backfill inspections are uncompromisable.** Once concrete or backfill is in, your ability to verify is gone.
4. **Hold testing schedules religiously.** Compaction, concrete cylinders, asphalt density, pipe pressure. Without tests, you have no record, and without a record you have no defense.
5. **Document conditions before the sub does.** Pre-construction topo, photographs, weather logs, inspection reports. The sub will document their version; the GC must have an equal or better record.
6. **RFIs over field improvisation, always.** If the field condition does not match the plan, stop and write. A 24-hour RFI delay is cheap; a stamped change is a defense; a self-invented fix is a personal liability.
7. **Use the engineer as the engineer.** Their stamp protects them and you — when their advice is in writing. Get it in writing.
8. **Civil is gravity and water.** Both are patient, both are relentless. Build to fight them, document that you did, and most of the things that go wrong on a construction site never start.

---

## Quick-Reference Index

- Frost depth by region: §5.1
- Atterberg limits / PI / EI: §1.5
- USCS soil symbols: §1.6
- FEMA flood zones: §1.7
- Shrinkage/swell factors: §2.1
- Compaction specs by application: §2.2
- E&SC BMPs: §2.5
- Retaining wall types: §2.6
- Rational Method: §3.1
- Storm pipe materials and Manning's n: §3.2
- 10-state water/sewer separation: §3.5
- Water main pressure testing/disinfection: §4.1
- Sanitary sewer min slopes: §4.2
- Trenching soil types and slopes: §4.5
- Foundation types by bearing capacity: §5.1
- Expansive soil mitigations: §5.2
- Tolerable differential settlement: §5.3
- Site Class A–F: §5.5
- CBR by soil: §6.2
- Concrete joint spacing rules: §6.5
- ADA slopes (the 2% cross slope): §6.6
- Productivity norms: §8.2
- Civil sheet codes (C-1.0, C-2.0...): §7.1
- Standard civil abbreviations: §7.2

---

*End of Module 05 — Civil Engineering for the General Contractor*
