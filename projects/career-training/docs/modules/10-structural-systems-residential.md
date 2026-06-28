---
title: "Structural Systems for the Residential General Contractor"
module: 10
discipline: ["structural", "framing", "concrete", "foundations", "seismic"]
audience: "Residential GC — construction-experienced, not a structural engineer"
status: "reference"
tags: [career-training, structural, framing, concrete, foundations, seismic, wood-framing, steel]
created: 2026-05-12
---

# Structural Systems for the Residential General Contractor

> **How to use this document**: This is a field reference, not a textbook. It's organized so you can find the answer to "what does this mean / what do I do" fast. The goal is to make you the smartest non-engineer in the trailer — able to read drawings, manage subs, catch errors before they're poured or covered, and know when to call the engineer instead of guessing.

---

## 1. Structural Engineering Basics for GCs

### 1.1 The Mental Model: Everything is a Load Path

Every pound of weight in a building — drywall, snow, a piano, a person — has to get to the ground. The structure is a **continuous load path** of members sized to carry that weight, plus a margin of safety. If any link is broken, undersized, or missing a connector, the whole path fails. Your job is to make sure the path the engineer drew is the path that actually gets built.

Two categories of forces:

| Force type | Direction | Source | Resisted by |
|---|---|---|---|
| **Gravity** | Vertical (down) | Self-weight, occupants, furniture, snow | Beams, joists, posts, bearing walls, footings |
| **Lateral** | Horizontal | Wind, seismic, earth pressure | Shear walls, diaphragms, hold-downs, moment frames |

### 1.2 Loads — Where They Come From

**Dead load (DL)** — permanent weight of the structure itself. Lumber, drywall, roofing, mechanical equipment. Engineer calculates from the assembly: a typical wood-framed floor is ~10–15 psf dead, a tile roof is ~15–20 psf, an asphalt-shingle roof is ~7–10 psf. Doesn't change once built.

**Live load (LL)** — variable load from occupants, furniture, movable equipment. Code-prescribed minimums:

| Use | Live load (psf) |
|---|---|
| Residential floor (sleeping) | 30 |
| Residential floor (living) | 40 |
| Stairs | 40 |
| Decks (residential) | 40 (some jurisdictions 60) |
| Garage (passenger vehicle) | 50 |
| Roof live load (low slope, no snow) | 20 |
| Attic with limited storage | 20 |
| Attic without storage | 10 |

**Snow load** — geographic, from ground snow map (ASCE 7). Ranges from 0 psf (Florida) to 100+ psf (mountain Sierra, Rockies). Reduces with roof slope (snow slides off). Drifting at parapets, dormers, and lower roofs against walls can be 2–3x the flat-roof value — this is a common engineering oversight on additions.

**Wind load** — depends on basic wind speed (V, from ASCE 7 map, typically 95–130 mph for residential), exposure category (B, C, D — sheltered to coastal), and building height. Wind creates both **uplift** on roofs (suction) and **lateral** pressure on walls. Critical at hip/eave/ridge connections — this is why you see hurricane ties (H1, H2.5) on every rafter.

**Seismic load** — proportional to building weight and site seismicity (Ss, S1 from USGS). Heavy buildings shake harder. Two big design parameters: **SDS** (short-period acceleration) and **SDC** (Seismic Design Category, A–F). California is mostly SDC D, parts SDC E. See Section 6.

**Special loads** — concentrated point loads (post landing on a beam), unbalanced snow, ponding, hydrostatic pressure on basement walls, vehicle impact. These are case-by-case engineered.

### 1.3 Load Path — A Worked Example

Trace a snowflake from the roof to the dirt:

```
Snow (40 psf) lands on roofing
    ↓
Roof sheathing (½" plywood, spans rafter-to-rafter)
    ↓
Rafter / truss top chord (2x10 @ 24" o.c., spans 12')
    ↓
Ridge beam or bearing wall (collects rafter reactions)
    ↓
Top plate of bearing wall (double 2x6)
    ↓
Studs (2x6 @ 16" o.c., transfer axial load)
    ↓
Bottom plate / sill plate
    ↓
Rim joist / blocking at floor
    ↓
Floor joist below or directly to foundation
    ↓
Concrete stem wall or foundation wall
    ↓
Footing (spreads load over soil)
    ↓
Soil bearing (1500–3000 psf typical residential)
```

**Every transition is a critical detail**. The post-to-beam connection, the beam-to-post-cap, the post base anchored to concrete — these are where engineers spend most of their time, and where framers most often screw up. A 6x6 post carrying 12,000 lb is useless if it sits on a piece of OSB. There must be **direct bearing** all the way down.

### 1.4 Lateral Force Resisting System (LFRS)

Gravity is forgiving. Lateral forces are not — a building can stand up to gravity for decades and collapse in 30 seconds in an earthquake or hurricane. The LFRS has three parts working together:

1. **Diaphragm** — roof and floor sheathing act as horizontal beams, collecting wind/seismic from one side of the building and delivering it to shear walls. Diaphragms must be **continuous** (blocked at panel edges for high loads).
2. **Shear walls** — vertical walls sheathed with structural panels (typically ⅜"–⅝" OSB or plywood), nailed at a prescribed schedule, with **hold-downs** at the ends to prevent overturning.
3. **Collectors and chord elements** — top plates, drag struts, rim joists that tie the diaphragm into the shear walls.

Three failure modes engineers worry about:
- **Sliding** — building slides off its foundation. Prevented by anchor bolts and mudsill plate.
- **Overturning** — shear wall tips over. Prevented by hold-downs (HDU, HTT, PHD) at each end.
- **Racking** — wall parallelogram-shapes. Prevented by sheathing with adequate nailing.

### 1.5 Safety Factors — Why Things Look "Overbuilt"

A beam designed to carry 2,000 lb is sized to actually hold ~4,000–6,000 lb before failure. This isn't waste — it accounts for:

- Variability in lumber grading (one 2x10 isn't another)
- Long-term creep and load duration
- Unforeseen loads (a contractor stacking drywall on a floor)
- Workmanship variability (nails missed, miscounted)
- Material degradation over 50+ years

The Load and Resistance Factor Design (**LRFD**) method bakes safety factors into both sides — load factors (1.2 DL + 1.6 LL is typical for gravity) and resistance reduction (phi factors, e.g., 0.9 for flexure). The Allowable Stress Design (**ASD**) method instead reduces allowable stress to ~60% of failure. Both arrive at similar member sizes.

**Practical implication**: Don't second-guess the engineer. A 4x12 header where you've seen "always" a 4x10 isn't padding — there's usually a reason (longer span, point load above, larger window opening). Ask before you substitute.

### 1.6 Reading a Structural Note Without an Engineering Degree

A typical note: `4x12 DF #1 HDR W/ (2) JACK & (1) KING EA END, A35 EA TRUSS`

Decoded:
- **4x12** — nominal dimensions (actual 3½" × 11¼")
- **DF #1** — Douglas Fir, Grade No. 1
- **HDR** — Header
- **(2) JACK** — Two jack studs (trimmers) supporting the header at each end
- **(1) KING** — One king stud (full-height) at each end
- **A35** — Simpson A35 angle clip
- **EA TRUSS** — at each truss bearing on the header

Another: `(3) 1¾" × 11⅞" LVL @ MFR'S 2.0E, FLITCH W/ ½" Ø BOLTS @ 16" O.C. STAGGERED`

Decoded:
- Three 1¾" × 11⅞" LVL plies
- 2.0E (modulus of elasticity, common LVL grade — 2.0 million psi)
- "FLITCH" — built up as a multi-ply beam
- ½" diameter through-bolts spaced 16" on center, staggered top/bottom

Memorize the abbreviations table in Section 7.4.

### 1.7 When to Call the Engineer

| Field condition | Action |
|---|---|
| Beam doesn't fit where shown (HVAC, plumbing conflict) | **Call.** Beam relocation changes load path. |
| Need to drill a hole in an LVL or I-joist | **Check manufacturer chart first**, then call if outside allowed zones. |
| Found rot or termite damage in existing structure during remodel | **Call.** May require sistering, replacement, or shoring. |
| Soil at footing excavation looks soft / different than expected | **Call AND notify soils engineer.** Do not pour. |
| Cracked concrete after stripping forms | **Call** if structural (through-cracks, horizontal cracks in walls). Shrinkage cracks <1/16" usually OK. |
| Sub wants to substitute lumber species or hardware | **Call.** Even apparent equivalents (PHD vs. HTT) resist different loads. |
| Adding a beam pocket, notching a joist beyond code, modifying a truss | **Call. Always.** Trusses especially — never field-modify a truss without truss manufacturer + EOR approval. |
| Window or door opening grew during framing | **Call** if the header now spans more than originally engineered. |
| Hold-down nut won't engage threads | **Call.** Indicates anchor was set short or out of plumb. |
| Sheathing nail schedule on plans is different from what framer is installing | **Stop work, call.** This is one of the most common (and dangerous) field shortcuts. |

**Default rule**: Any deviation from the structural drawings requires written approval from the Engineer of Record (EOR). Verbal in the field doesn't count. Email or RFI response.

---

## 2. Foundations

### 2.1 Soil Bearing — The Foundation Under the Foundation

Soil bearing capacity is the load (psf) the soil can support without excessive settlement. From IRC Table R401.4.1 (presumptive, with no soils report):

| Soil class | Presumptive bearing (psf) |
|---|---|
| Crystalline bedrock | 12,000 |
| Sedimentary rock | 4,000 |
| Sandy gravel / gravel (GW, GP) | 3,000 |
| Sand, silty sand (SW, SP, SM, SC, GM, GC) | 2,000 |
| Clay, sandy clay, silty clay (CL, ML, MH, CH) | 1,500 |

If a geotechnical report exists, **use those values** — they override the presumptive table and may be higher (allowing smaller footings) or lower (requiring deeper foundations, piers, or soil improvement).

**Field red flags requiring geotech callout**:
- Soil that crumbles, has voids, or shows organic material (roots, peat)
- Wet or saturated subgrade
- Fill that you didn't place and document
- Bedrock or boulders that prevent full footing depth
- Slope conditions (hillside, near retaining walls)

### 2.2 Spread Footings

Concrete pads under columns or isolated point loads. Sizing principle: **Area = Load ÷ Soil bearing**.

A 24-kip column on 2000 psf soil needs 24,000 ÷ 2,000 = 12 sf, so a 3'-6" square pad. Typical residential pads:

| Pad size | Typical load |
|---|---|
| 24" × 24" × 12" | Up to ~8 kip |
| 30" × 30" × 12" | Up to ~12 kip |
| 36" × 36" × 12" | Up to ~18 kip |
| 48" × 48" × 12" | Up to ~32 kip |

**Reinforcing** — typically #4 or #5 bars each way at 8"–12" o.c., 3" cover from earth. Bottom mat only for shallow loads; top and bottom mat for heavily loaded or eccentric pads. Frost depth governs minimum depth (24"–48" in cold climates, 12"–18" in California where frost isn't a concern but uplift, expansive soil, and seismic still drive embedment).

### 2.3 Continuous Footings

Run under perimeter and bearing walls. Typical dimensions:

| Footing | Width | Depth | Reinforcing |
|---|---|---|---|
| 1-story wood frame | 12" | 12" | (2) #4 continuous |
| 2-story wood frame | 15" | 12" | (2)–(3) #4 continuous |
| 3-story / heavy load | 18"–24" | 12"–18" | (3)–(4) #4 or #5 continuous |
| Interior bearing | 12"–15" | 12" | (2) #4 continuous |

**Stem wall** sits on the footing. Typical residential stem walls are 8" thick concrete or 8" CMU (grouted), with vertical rebar (#4 @ 24"–48" o.c.) hooked into the footing and horizontal rebar (#4 top and bottom). Anchor bolts (½" or ⅝" × 10" or 12" long, 5"–7" embedment) embed in the top of the stem at 4'–6' o.c. or as specified.

**Thickened slab edge (monolithic pour)** — used for slab-on-grade homes (common in Texas, Florida, parts of California). Slab and footing pour together; the perimeter is a thickened beam, typically 12" × 24" deep, with (2) #4 top and (2) #4 bottom continuous.

### 2.4 Slab-on-Grade

Build-up from bottom:
1. **Compacted subgrade** — 95% relative compaction, tested
2. **Base course** — 4" of ¾" crushed rock (Class II base in California)
3. **Vapor barrier** — 10–15 mil polyethylene (Stego Wrap is the de facto standard for high-performance), seams taped, penetrations sealed
4. **Optional**: 2" rigid foam (XPS) under-slab insulation for conditioned slabs
5. **Reinforcement** — 6×6 W2.9×W2.9 WWM (welded wire mesh) OR #3/#4 rebar @ 18"–24" each way on chairs (3"–4" above bottom of slab)
6. **Concrete** — typically 3000–4000 psi, 4" thick (5" for garages, more for floors with heavy loads)

**WWM vs. rebar debate**: WWM is cheaper and faster but routinely ends up on the dirt because it gets walked on during the pour ("flat WWM is no WWM"). Rebar on chairs stays in position. For any slab you care about, spec rebar.

**Joints**:
- **Control joints** — saw-cut within 6–18 hours of pour, ¼ slab thickness deep, spacing ≤ 2.5× slab thickness in feet (e.g., 4" slab → 10' max).
- **Construction joints** — where a pour ends and another begins. Use keyway or dowels.
- **Isolation joints** — where slab meets walls, columns, footings. ½" expansion material.

**Curing** — concrete gains 70% of its 28-day strength in 7 days *if kept moist*. Wet-cure (burlap, plastic, soaker hoses) or curing compound. Curing matters more in hot/dry/windy conditions — without curing, the surface evaporates faster than hydration, leading to crazing, dusting, and reduced surface strength.

### 2.5 Post-Tension (PT) Slabs

PT slabs use high-strength steel tendons (7-wire strands, ½" diameter, 270 ksi) sheathed in plastic, placed in the slab, and **stressed (tensioned) after the concrete cures** to 33,000 lb each. The compression preloads the slab, allowing larger spans, thinner sections, and better crack control. Common on expansive soil (Texas, Southern California) and large-footprint residential.

**Sequence**:
1. Tendons placed in profile (typically draped, low in middle, high at edges) on chairs
2. Tendon ends stick through the perimeter form
3. Slab is poured around tendons
4. Concrete cures to ~3000 psi (usually 3–7 days, verified by cylinder break)
5. Stressing crew jacks each tendon to specified elongation, marks, and cuts the tail
6. End pockets grouted

**GC critical responsibilities**:
- **Do NOT cut, drill, or core a PT slab without locating tendons**. A severed tendon whips and can kill someone, plus it destroys the structural integrity. Use GPR (ground-penetrating radar) scanning. Most PT slab projects require a PT scan before any post-installation penetration.
- Document tendon layout (as-built drawings from the PT supplier) and keep on file forever.
- Saw-cut control joints are typically **not** done on PT slabs (the post-tensioning provides crack control). If specified, they're shallow.
- Plumbing penetrations and embeds must be coordinated **before** the pour. Once stressed, you can't easily add anything.
- Watch the stressing log — the engineer wants a stressing report showing required elongation per tendon. Out-of-tolerance tendons (too short or too long elongation) require investigation.

### 2.6 Raised Foundation / Crawlspace

Used where slab is impractical (sloping site, flood zones, traditional regional style). Components:

| Component | Description |
|---|---|
| **Stem wall** | 8" CMU or concrete, on continuous footing |
| **Mudsill (sill plate)** | Pressure-treated (PT) 2x6 bolted to stem with anchor bolts, sill seal/gasket below |
| **Anchor bolts** | ½"–⅝" diameter, 7"+ embedment, 6' o.c. max (4' o.c. in high seismic), within 12" of plate ends and corners |
| **Floor joists** | Solid sawn 2x8/2x10/2x12 or I-joists, spanning between stem walls and interior girder |
| **Girder** | (3) 2x10/2x12 built-up beam, glulam, or LVL on posts, mid-span support for joists |
| **Posts** | 4x4 or 6x6, on concrete piers (12" min above grade if untreated, on PT post bases) |
| **Crawlspace vents** | Required for vented crawl: 1 sf vent per 150 sf floor area, or 1:1500 with vapor barrier. Conditioned (unvented) crawlspaces are increasingly preferred per energy codes |
| **Vapor barrier** | 6 mil minimum poly on ground, lapped 12" at seams |

**Common issues**: Untreated wood within 8" of grade is a building code violation (decay risk). Anchor bolts missing or too far from corners. PT mudsill in direct contact with concrete without sill seal — code-allowed but the gasket is cheap insurance against capillary moisture.

### 2.7 Basement Foundations

Full-height basement walls (typically 8'–10' tall) carry both gravity (load above) and **lateral earth pressure** (active soil pressure pushing in). The lateral component dominates — an 8' basement wall sees ~30–60 psf at the bottom from soil + surcharge.

**Wall thickness and reinforcing** (typical, but always per engineer):

| Wall height | Wall thickness | Vertical rebar | Horizontal rebar |
|---|---|---|---|
| 7' or less | 8" | #4 @ 24" | #4 @ 24" |
| 8' | 8"–10" | #4 @ 16"–24" | #4 @ 18" |
| 9'–10' | 10"–12" | #5 @ 12"–16" | #4 @ 16"–18" |

Vertical rebar hooks into the footing and extends to (or near) the top of the wall, lapped per ACI splice tables.

**Critical detail**: The wall must be **braced** at the top before backfill. The floor diaphragm braces the top of the wall — backfilling before the first floor is framed can blow the wall in. Temporarily brace with kickers from inside or wait for framing.

**Waterproofing vs. dampproofing**:
- **Dampproofing** (sprayed asphalt emulsion) — minimum code, resists capillary moisture, NOT water pressure
- **Waterproofing** (sheet membranes like Bituthene, fluid-applied like Tremco TUFF-N-DRI, or composite systems) — required where water table can rise to footing or where habitable space is below grade. Always use for finished basements.

**Drainage**:
- Footing drain — perforated 4" pipe in gravel, wrapped in filter fabric, sloped to daylight or sump
- Dimple board / drainage plane on outside of wall — directs water down to footing drain instead of against the wall
- Backfill with free-draining material (gravel) at least 2' wide against wall before native soil

### 2.8 Drilled Piers / Caissons

Used when surface soils are inadequate (loose fill, expansive clay, organic) or on hillsides where shear loads + uplift must transfer deep. Common on California hillside homes.

**Process**:
1. Drilling rig augers a hole, typically 12"–36" diameter, to specified depth (15'–50'+)
2. Soils engineer inspects bottom — confirms bearing stratum reached
3. **Bell** (optional) — bottom is reamed out wider to spread load (only in cohesive soil)
4. Reinforcing cage lowered in (longitudinal #6–#8 bars, ties or spiral)
5. Concrete placed via tremie pipe (placing freely creates segregation)
6. Pier reinforcing extends up into grade beam or pile cap

**Bearing verification** — geotech sign-off at every pier bottom is non-negotiable. If you see different soil than expected, stop and call. Drilled piers are the most expensive thing to redo.

**Grade beams** tie pier tops together — concrete beams, typically 12"×24" or larger, reinforced top and bottom. They span between piers, carrying the building above.

### 2.9 Hold-Downs and Anchor Bolts — The Most Frequently Botched Detail

Hold-downs resist **uplift** at the ends of shear walls. When a shear wall sees lateral force, it tries to rotate — one end goes down, the other end pulls up. The hold-down anchors that tension end into the foundation. **Lose the hold-down, lose the shear wall.**

Common Simpson hold-down types in residential:

| Product | How it attaches | Typical capacity (lb) | When used |
|---|---|---|---|
| **SSTB / SB anchor bolt** | Cast-in-place anchor bolt with bend | 2,000–7,000 | Most common cast-in anchor for HDU hold-downs |
| **PAB anchor bolt** | Cast-in pre-anchored bolt | 7,000–14,000 | Higher capacity |
| **HDU (2, 4, 5, 8, 11, 14)** | Bolts to post, threads onto SSTB | 3,000–14,500 | Most common modern hold-down |
| **HTT (HTT4, HTT5)** | Strap-style, bolts/nails to post | 3,000–4,500 | Common for lighter shear walls, retrofit |
| **PHD (PHD2, PHD5, PHD6)** | Bolted hold-down | 3,000–5,400 | Older but still used; bolts through stud pack |
| **Strong-Rod (ATS)** | Threaded rod through multi-story walls | Up to 20,000+ | Tall walls, stacked shear walls in multi-story |

**Installation tolerances and inspection points**:
- Anchor bolt placement — the SSTB must be within ±¼" of the centerline shown on plans (HDU shoe is rigid). Sloppy form work = hold-down doesn't engage = inspection fail.
- Anchor bolt embedment — must be the full depth shown (e.g., SSTB16 = 16" embedment). Pulling up an anchor that's "too long" before pour is a major mistake.
- Anchor bolt projection — must extend high enough above concrete to engage hold-down + nut. Cutting an anchor "to make it fit" the post is a fail.
- Post material — the HDU bolts to a 4x or larger post. Not to a single 2x. Plans will specify (e.g., "(3) 2x6 stud pack").
- Nut tightness — snug-tight, not impact-gunned to oblivion. Some engineers specify torque values.
- After framing, before insulation: visually verify hold-down is in place, plumb, full bolt engagement, and nailed/bolted to post per Simpson installation requirements (the small print in the catalog matters).

**Anchor bolts (general, for mudsill)**:
- ½" or ⅝" diameter, 7" min embedment (10" in some jurisdictions)
- Spaced 6' o.c. max (4' o.c. in some high-seismic conditions)
- Within 12" of plate ends and at all corners
- Plate washers required (3" × 3" × ¼" minimum in SDC D, E, F per code)
- ⅛" gap to nut max — over-drilled holes are a fail

---

## 3. Wood Framing

### 3.1 Lumber Species, Grades, and Grade Stamps

**Species** dictates strength, stiffness, and availability. The big three in residential:

| Species (combo) | Region of use | Strength | Notes |
|---|---|---|---|
| **Douglas Fir-Larch (DF-L)** | West Coast, widely used nationally | Highest of common species | Standard in California. Strong, holds nails well. |
| **Hem-Fir (HF)** | West Coast and intermountain | ~85% of DF-L | Often substituted for DF when DF is short. Allowed only if engineer accepts. |
| **Spruce-Pine-Fir (SPF)** | Northern US, Canada | Moderate | Common in Midwest, Northeast. Lighter than DF. |
| **Southern Yellow Pine (SYP)** | Southeast | High | Dense, heavy, holds fasteners well. Common for PT lumber. |

**Grades** (from highest to lowest for visually-graded lumber):
- **Select Structural (SS)** — premium, highest values
- **No. 1** — high quality, used for headers, beams
- **No. 2** — most common framing grade (studs, joists, rafters)
- **No. 3 / Stud / Utility / Construction / Standard** — lower grades, NOT for engineered framing without specific allowance

**MSR (Machine Stress-Rated) lumber** — graded by machine that flexes each board and measures E (stiffness). Marked with E value (e.g., 1650f-1.5E means 1650 psi bending stress, 1.5×10⁶ psi modulus). Used where you need consistent properties.

**Grade stamp** — every piece of structural lumber bears a stamp showing mill, grade, species, and moisture content (S-GRN = green, surfaced; S-DRY = ≤19% MC; KD = kiln-dried, typically ≤15%). **If you can't find a grade stamp, the lumber isn't graded and can't be used structurally.**

**Substitution rule**: Engineer specifies DF #2, the framer can use DF #1 or Select Structural (better is OK). Can NOT use HF #2 without engineer approval (different species).

### 3.2 Floor Systems

**Solid sawn joists** — traditional 2x8, 2x10, 2x12. Cheapest, but limited span and prone to shrinkage/twist as they dry. Max span depends on species, grade, spacing, and load:

| Joist | DF #2 @ 16" o.c., 40 psf LL | Notes |
|---|---|---|
| 2x8 | ~12'–13' | Light floors |
| 2x10 | ~15'–16' | Most common residential |
| 2x12 | ~18'–19' | Long spans, heavy loads |

**I-joists** (TJI, BCI, LPI brands) — manufactured wood I-beam with OSB web, LVL flanges. Long spans (up to 30'+), lightweight, dimensionally stable. Strict rules:
- **Holes**: round holes only in web, only in approved zones (see manufacturer chart). Generally larger holes allowed in mid-span (low shear), no holes near supports.
- **Flange notching**: NEVER. Notching or cutting the flange destroys the joist.
- **Squash blocks** required under bearing walls above (the web alone can't carry the point load).
- **Web stiffeners** required at concentrated loads and some hanger conditions.
- **Hangers**: I-joist-specific hangers (IUS, ITT, MIU). Standard solid-sawn hangers don't work.
- **Storage**: stand on edge, not flat (a 30' I-joist stored flat will permanently bow).

**LVL joists** — used where you need long span or high load. More expensive per foot but stable.

**Open-web floor trusses** — pre-fabricated, allow ductwork to pass through web openings. Engineered per project; long spans common. Same rule as roof trusses: never field-modify.

**Joist hangers** — Simpson LUS (light/medium), HUS (heavy), specifically marked for "joist" or "rafter" use:
- LUS28 — 2x8 single-ply
- LUS210 — 2x10 single-ply
- HUS28/210/212 — heavy duty
- LVL hangers — wider face, sized for the LVL thickness (e.g., HU3.56/11 for a 3½" × 11¼" LVL)

**Critical**: Hangers require **all** holes filled with the correct fastener (Simpson SD or SDS structural screws, OR 10d/16d nails per the catalog). Joist hangers are rated based on full nailing. Half-nailed = half-strength = inspection fail.

**Blocking and bridging**:
- **Solid blocking** at joist ends (over bearing) and at mid-span of long joists. Required by code for joists ≥ 2x10 spanning ≥ 8'.
- **Cross-bridging** (1x4 or metal cross-braces) — older method, less common now.
- Blocking also serves the **diaphragm function** at edges of the floor — required to transfer shear from sheathing to wall plates below.

**Subfloor**:
- **Plywood** — typically ¾" T&G (tongue-and-groove) for 16"–19.2" o.c. joist spacing, or 1⅛" for 24" o.c. APA-rated Sturdi-Floor 24 OC or 32 OC.
- **OSB** — equivalent strength, less expensive, slightly worse moisture performance. Modern OSB (e.g., AdvanTech) is engineered to outperform plywood for floor applications.
- **Glue-nailed** — construction adhesive (PL Premium or equiv.) between joist and sheathing, plus ring-shank or screw nails at 6" edges / 12" field. Eliminates squeaks, adds composite stiffness. Required for most modern floor designs.

### 3.3 Wall Framing

**Bearing wall** = supports gravity load from above (roof or floor). **Non-bearing** = doesn't.

| Element | Bearing wall typical | Non-bearing typical |
|---|---|---|
| Stud size | 2x6 or 2x4 | 2x4 |
| Spacing | 16" o.c. (24" o.c. allowed for some configs) | 16" or 24" o.c. |
| Top plate | Double 2x6 / 2x4 | Single OK in some cases |
| Header | Sized per opening | None (or single 2x for trim) |
| Bottom plate | Single 2x6 / 2x4, anchored | Single, attached to floor |

**2x6 advanced framing** (24" o.c., single top plate aligned with truss/joist above, insulated headers) is energy-code-driven and structurally adequate when done right. But: requires precise layout and is unforgiving to mistakes.

**Headers** size table for openings (DF #2, single floor + roof above, snow 25 psf, simple wood-frame house, NO point loads — always verify with plans):

| Opening | Header (typical) |
|---|---|
| ≤ 3'-0" | (2) 2x6 |
| 3'-0" to 5'-0" | (2) 2x8 |
| 5'-0" to 7'-0" | (2) 2x10 |
| 7'-0" to 9'-0" | (2) 2x12 or (3) 1¾" × 9¼" LVL |
| 9'-0" to 12'-0" | (3) 1¾" × 11⅞" LVL or (3) 2x12 |
| 12'-0"+ | LVL, glulam, or steel — engineered |

**Built-up headers** (e.g., (2) 2x12) need ½" plywood between for 2x4 walls, or no spacer for 2x6 walls (header is 2-ply 3" wide). Some engineers spec a sandwich of ½" plywood between plies for shear continuity.

**Jack (trimmer) and king studs**:
- Jack stud — full-height to bottom of header, carries header reaction down
- King stud — full-height to top plate, alongside the jack stud, ties the header to the plates
- (1) jack each end for openings ≤ 4', (2) jacks for larger openings (verify with plans)
- (1) king each side typical, (2) for very wide / heavy openings

**Top plates** — almost always **double** (two layers of 2x lumber). Functions: lap continuity at corners and tees, distribute concentrated loads from above to multiple studs below, serve as a chord member for the diaphragm. Lap splices must be at least 24" offset between plies, with 8 16d nails or per schedule.

**Cripples** — short studs between header and top plate (above) or between sill and bottom plate (below window). Typically same spacing as wall studs (16" o.c.).

### 3.4 Roof Framing

**Stick-frame** (cut roof) — rafters cut on site, ridge board, ceiling joists tie rafter feet to prevent ridge thrust. Used for: custom geometry, additions matching existing, dormers and architectural complexity that pre-fab trusses can't handle.

Key elements:
- **Ridge board** (non-structural) vs. **Ridge beam** (structural, used in vaulted ceilings where there's no ceiling joist to tie rafters). Ridge beam needs proper bearing at each end.
- **Collar ties** — high in the rafter, prevent ridge separation, NOT a substitute for ceiling joists in resisting thrust.
- **Rafter ties / ceiling joists** — at the rafter feet, prevent the walls from being pushed outward by rafter thrust. If absent, the engineer must design for a structural ridge.
- **Birdsmouth cut** — notch at rafter where it bears on top plate. Per code: notch must not exceed ¼ depth of rafter; the bearing surface must be at least 1½" (full bearing on plate).

**Trusses** — engineered components delivered to site. Types:

| Type | Profile | Use |
|---|---|---|
| **Fink (W-truss)** | Triangular, common gable | Most common residential |
| **Howe** | Vertical webs | Heavy loads |
| **Scissor** | Bottom chord rises to mid-height | Vaulted ceiling inside |
| **Attic truss** | Open space in middle | Walkable storage / bonus room |
| **Hip truss / step-down** | Step-down profile for hip end | Hip roof |
| **Gable end truss** | Vertical web, flat at end | End walls |

**Reading truss engineering** — each truss has a calc sheet showing loads, span, deflection, web/chord forces, and bearing reactions. The reaction value (e.g., 1,800 lb at each bearing) is what you need to verify the wall below can support.

**Truss spacing** — typically 24" o.c. for residential; 16" possible for heavy loads. Bracing requirements per BCSI (Building Component Safety Information) — temporary and permanent bracing critical to prevent collapse during install. Top chord laterals (2x4 nailed to top of every truss in the field) and bottom chord laterals are mandatory.

**Truss handling rules**:
- Lift with spreader bar, not single point (banana-loading damages the truss)
- Don't store flat — store on edge or stacked vertically with supports
- Don't field-modify (NO drilling, cutting, notching). If you need to, get the truss manufacturer's repair detail.
- Verify all hangers and connectors per truss-to-truss connection plan (girder trusses, valley sets, hip jacks)

### 3.5 Shear Walls

A shear wall is a wall sheathed with structural panels (OSB or plywood) nailed at a prescribed schedule to resist lateral force. Capacity depends on:
- Sheathing thickness
- Nail size and spacing (edge vs. field)
- Whether panels are blocked (every edge nailed)
- Hold-downs at ends
- Anchor bolts at base

**Common shear wall types** (from SDPWS — Special Design Provisions for Wind and Seismic):

| Sheathing | Edge nail spacing | Field | Allowable shear (plf, seismic) |
|---|---|---|---|
| ⅜" OSB/plywood, 8d common | 6" o.c. | 12" | ~260 |
| ⅜" OSB/plywood, 8d common | 4" o.c. | 12" | ~380 |
| ⅜" OSB/plywood, 8d common | 3" o.c. | 12" | ~490 |
| ⅜" OSB/plywood, 8d common | 2" o.c. | 12" | ~640 |
| ½" or ⅝" — higher values | | | up to ~870 |

(Plf = pounds per linear foot of shear wall.)

**Critical install details**:
- Edge nails must be ⅜" minimum from panel edge — closer than that and the panel splits
- Use 8d **common** nails (0.131" shank) or 8d box (0.113") — they're NOT the same; common is required for full shear capacity
- Pneumatic gun nails — verify shank diameter matches required. Many gun nails are smaller (clipped-head 8d at 0.113") and give 60–70% of common-nail capacity
- **NO overdriven nails** — nail head flush, not driven below the surface (countersunk nails reduce shear strength dramatically and are a common fail)
- All panel edges (top, bottom, side) must land on framing or blocking
- 3-stud post (or column) at all shear wall ends (for hold-down attachment)
- Continuous load path from sheathing → hold-down → anchor bolt → foundation

**Continuous tie / ATS rod systems** — for tall walls (multi-story), Simpson Strong-Rod (ATS) or similar systems run a threaded rod from foundation through each story to the top, with take-up devices to compensate for wood shrinkage. Required where individual hold-downs at each level aren't adequate.

### 3.6 Diaphragms

The floor and roof sheathing act as a **horizontal shear element** that transmits lateral force to the shear walls. Sheathing thickness and nailing schedule are engineered just like shear walls.

| Diaphragm | Blocked / unblocked | Nail spacing edge / field | Capacity (plf) |
|---|---|---|---|
| ½" CDX plywood roof | Unblocked, 8d @ 6"/12" | ~240 plf |
| ½" CDX plywood roof | Blocked, 8d @ 6"/6"/12" | ~360 plf |
| ¾" T&G plywood floor | Blocked, 10d @ 6"/12" | ~640 plf |

**Blocked** = solid blocking at every panel edge so every edge has a nailing surface. **Unblocked** = only the framing-supported edges are nailed. Blocked diaphragms are 2–3× stronger but cost more in labor.

**Edge nailing at diaphragm boundary** — where roof or floor meets the shear wall, the perimeter nailing is the **chord/collector**. Often called out separately on plans as "boundary nailing" with tighter spacing (e.g., 4" o.c.).

### 3.7 Engineered Lumber

| Product | What it is | Common uses | Strengths | Watch-outs |
|---|---|---|---|---|
| **LVL** (Laminated Veneer Lumber) | Cross-laminated wood veneers (parallel grain), glued | Headers, beams, joists, rim board | High strength, dimensionally stable | Holes only per manufacturer chart. Strict bearing requirements. Multi-ply LVLs need specified bolt/screw pattern to act as a unit |
| **PSL** (Parallel Strand Lumber) — Parallam | Long wood strands, parallel, resin-bonded | Beams, columns, exposed structural | Very high strength, large sizes available, attractive (can be left exposed) | Expensive. Heavy. PT versions for exterior. |
| **LSL** (Laminated Strand Lumber) — TimberStrand | Short strands, parallel, resin-bonded | Rim joist, studs (tall walls), headers (lighter loads), garage door headers | Stable, lower cost than LVL/PSL | Lower strength than LVL — don't substitute |
| **GLB / Glulam** (Glued Laminated Beam) | Stacked dimensional lumber, glued | Beams (especially long-span), arches, exposed structural | Long lengths (40'+), curved possible, attractive | Camber matters — install crown up. Wet conditions cause delamination if not PT |
| **CLT** (Cross-Laminated Timber) | Mass timber panels, alternating grain | Mass timber buildings, slabs, walls | Big spans, prefab | Rare in single-family residential, more common in multi-family/commercial |

**LVL multi-ply assemblies** — when plans show (3) 1¾" × 11⅞" LVL, all three plies must act together. This requires fasteners through all plies per the engineer's spec (typically (2) rows of 16d nails @ 12" o.c. for 2-ply, OR ½" bolts staggered for 3+ ply). Side-loaded LVLs (load from one side only, like a hanger on the face) need closer fasteners or through-bolts.

**Bearing length** — engineered lumber is sensitive to bearing length. A long-span LVL might need a 3½" or 5½" bearing surface (verify on plan). Insufficient bearing causes crushing failure perpendicular to grain.

**Connector selection for engineered lumber** — use the manufacturer-specific hanger (Simpson HU/HUS sized for the LVL face, or LVL-specific HHUS series for top-flange / face-mount). Standard 2x10 hanger doesn't fit a 1¾" LVL face properly.

### 3.8 Simpson Strong-Tie Hardware

The Simpson catalog is the bible of wood-frame hardware. The most-used residential connectors:

**Joist hangers**:
- **LUS** — Light double-shear, single-ply joists (LUS26, LUS28, LUS210)
- **HUS** — Heavy duty, often used for engineered lumber and high loads
- **HU** — Single-shear face-mount hanger
- **MIU / IUS** — I-joist hangers (sized to fit I-joist depth)
- **HHUS** — Heavy duty for LVL/glulam beams

**Straps / ties**:
- **CS / LSTA / MSTA** — flat straps, used to tie members together across a joint (rafter-to-stud, beam-to-post, splice continuity)
- **CMST** / **MSTC** — heavy strap, used for continuous-tension applications
- **H1 / H2.5 / H10** — Hurricane / rafter ties, connect rafter to top plate, resist uplift
- **LTP4** — Lateral tie plate, plate-to-plate or plate-to-rim continuity

**Post bases**:
- **ABA** — adjustable post base, raises post off concrete (post bottom min 1" above concrete required by code)
- **ABU** — adjustable, heavier
- **PBS** — non-adjustable post base, faster but less forgiving on bolt placement
- **BC** — column cap (post-to-beam, top of post)
- **CCQ** — heavy column cap for engineered beams

**Hold-downs** — covered in 2.9.

**Field installation rules (universal)**:
- Use the specified fastener (Simpson SD screws, SDS screws, or specific nail size). **N10** = 10d common nail. **N10x1½** = 10d × 1½" (used in joist hangers where a full-length 10d would split a 2x). **N16** = 16d common.
- Fill **all** fastener holes. Hangers list two ratings — full nailing and reduced; default is always full.
- Don't bend or modify the connector. If you have to twist it to fit, you're using the wrong one.
- Bolts in hold-downs and post-base anchors must engage threads fully — at least 1 thread past the nut.

---

## 4. Concrete and Masonry

### 4.1 Concrete Mix Design

Concrete is specified by **compressive strength at 28 days (f'c)** in psi:

| Mix (psi) | Typical residential use |
|---|---|
| 2,500 | Mud slabs, blinding, very light duty (rarely spec'd anymore — IRC minimum is higher) |
| 3,000 | Footings, slab-on-grade interior, non-exposed (most common base mix in mild climates) |
| 3,500 | Stem walls, slab on grade in exposed conditions |
| 4,000 | Garage slabs, exterior flatwork (driveways, patios), post-tension slabs, freeze-thaw climates |
| 4,500–5,000 | Structural columns, heavy-load slabs, custom architectural |

**Water-Cement (W/C) ratio** — lower W/C = stronger and more durable concrete. Typical residential:
- 0.50 for general work
- 0.45 for exposure to freezing/thawing or de-icing salts
- 0.40 for severe exposure

The ready-mix plant designs the mix. Field-adding water at the truck **raises W/C and weakens the concrete**. Allow 1–2 gallons per yard for slump correction if needed, but require a slump test after any water addition. Excessive site water-addition is one of the most common causes of substandard concrete.

**Admixtures**:
- **Air-entrainment** — 5–7% air for freeze-thaw protection (exterior slabs in freezing climates). NOT for interior trowel-finished slabs (air weakens the surface for finishing).
- **Accelerators** (calcium chloride, non-chloride) — speed up set in cold weather. NOT in prestressed/PT concrete (corrosion).
- **Retarders** — slow set in hot weather, long hauls, complex pours
- **Plasticizers / superplasticizers** — increase workability without adding water. Common in high-strength mixes.
- **Fibers** (polypropylene, steel) — secondary reinforcement for slabs, replace WWM in some cases. Synthetic fibers help with plastic shrinkage cracking; steel fibers can replace structural rebar in some industrial floors (rare residentially).

**Aggregate size** — typically ¾" coarse aggregate for slabs and footings, ⅜" for walls with congested rebar or pumped applications. Larger aggregate is cheaper and stronger but harder to place.

**Slump** — measure of consistency, in inches:
- Footings: 4"–6"
- Slabs: 4"–5"
- Walls: 4"–6"
- Pumped concrete: 5"–7"
- High-slump (super-flowable, with superplasticizer): 7"–9"

### 4.2 Rebar

**Grade designations**:
- **Grade 40** (yield 40,000 psi) — older / lighter use, becoming uncommon
- **Grade 60** (yield 60,000 psi) — current residential standard
- **Grade 75 / 80** — heavy construction, not typical residential

**Bar size** = number ÷ 8 in diameter:
- #3 = ⅜" diameter
- #4 = ½"
- #5 = ⅝"
- #6 = ¾"
- #7 = ⅞"
- #8 = 1"

**Lap splices** — Grade 60 deformed bar in 3,000 psi concrete, "Class B" tension splice (most common): ~50× bar diameter. For #4 bar, lap is 25". For #5 bar, lap is ~32". Always verify with the engineer's lap schedule — splices in critical zones (column ties, near supports) may have specific length and location requirements.

**Cover** (concrete to outermost rebar):

| Condition | Cover |
|---|---|
| Concrete cast against earth (no formwork) | 3" |
| Concrete formed, exposed to earth or weather | 1½" (#5 or smaller); 2" (#6 and larger) |
| Slab top (above grade), interior, not exposed | ¾" |
| Beam / column stirrups | 1½" |

Cover is what stops corrosion. Insufficient cover = rust = concrete spalling years later. Use **chairs and dobies** (not blocks of wood) to hold rebar up off the form bottom.

**Hooks and bends** — 90° hook (length = 12db, where db = bar diameter), 180° hook (4db + bar diameter), 135° seismic hook (used for ties). Don't bend rebar that has already been bent (work-hardens, can crack). Don't heat rebar to bend it.

### 4.3 Forming Systems

**Wood forms** — plywood or OSB sheathing on dimensional lumber framing. Cheap, flexible, made on site. Standard for footings, stem walls, custom shapes.
- Form ties at 24"–32" o.c.
- Walers and strongbacks to keep walls plumb under pressure
- **Release agent** (form oil) on plywood to allow stripping
- Check plumb and brace before pour — concrete pressure can blow out a wall

**Metal forms** (Symons, EFCO, etc.) — modular aluminum or steel panels. Faster on repetitive work (housing tracts), better surface finish, expensive for one-offs.

**ICF (Insulated Concrete Forms)** — EPS foam blocks (Nudura, Fox Blocks, BuildBlock) snap together, get filled with concrete and rebar, stay in place as permanent insulation. Used for basements, full ICF homes, energy-efficient builds.

When ICF makes sense:
- Basements / below-grade walls — strong, insulated, waterproof-able
- High-performance / energy-focused builds
- Storm/hurricane-prone areas
- Acoustic isolation (separation walls in multifamily)

Watch-outs:
- Pour rate matters — too fast and forms blow out. Typically 4' lifts max, slower in tall walls.
- Bracing — extensive bracing required for plumb and straight; not optional
- Penetrations — must be planned and built in before the pour. After pour, cutting through 8" of concrete + 5" of foam is miserable.
- Electrical / plumbing — usually run in chases cut into the foam, but coordination with subs in advance is mandatory.

### 4.4 Pour Sequence and Cold Joints

Typical residential foundation sequence:
1. **Footings** — pour, let set (overnight minimum)
2. **Stem walls** — form on top of footings, set anchor bolts and hold-down anchors, pour
3. **Backfill** (if appropriate, after stem walls cure and waterproofing applied)
4. **Slab on grade** — base course, vapor barrier, mesh/rebar, pour, finish

**Continuous pour** — best for structural integrity. Plan truck deliveries to keep the pour moving — gaps of more than 30–45 minutes start to create cold joints. For long pours, schedule double trucks (one finishing while next arrives).

**Cold joints**:
- **Planned** — at construction joints with keyway or dowels and roughened surface. Acceptable when designed.
- **Unplanned** — pour stopped without preparation (truck didn't arrive, pump broke, weather). Acceptable only if joint can be cleaned, roughened, and tied with dowels before resuming. Otherwise, the wall must be removed and re-poured.

### 4.5 Curing

Concrete reaches design strength by hydration — a chemical reaction between cement and water that takes weeks. If the surface dries before hydration completes, you get:
- **Plastic shrinkage cracks** — fine cracks within hours, from rapid surface evaporation
- **Drying shrinkage cracks** — over days/weeks
- **Crazing** — fine surface cracks (mostly cosmetic)
- **Dusting** — soft, powdery surface
- **Reduced strength** — particularly at the surface, where wear happens

**Curing methods** (use at least one, especially in hot/dry/windy conditions):
- **Wet cure** — soaker hoses, sprinklers, wet burlap, or plastic sheeting with water under. 7 days minimum.
- **Curing compound** — sprayed-on membrane that traps moisture. Apply as soon as bleed water disappears. Some compounds interfere with floor finishes — confirm compatibility.
- **Wet burlap / curing blankets** — labor-intensive but effective. Common on quality flatwork.

**Hot weather precautions** — concrete temperature > 90°F at placement is high-risk. Pour in early morning, ice the mix water, shade the pour, fog-spray to prevent surface drying, use a retarder. Below 40°F: cold-weather precautions — heat mix, blankets, temporary enclosures, accelerator (if not PT).

### 4.6 Concrete Testing

**Slump test** (ASTM C143) — cone filled with fresh concrete in 3 layers, rodded 25 times each, cone lifted, measure slump. Done at the chute before pour. Outside spec slump = reject or adjust at plant (NOT at site beyond the allowed water addition).

**Air content** (ASTM C231 pressure method or C173 volumetric) — required for air-entrained concrete. 5–7% target.

**Cylinder breaks** — 4"×8" or 6"×12" cylinders cast at the pour, cured in lab, broken at 7 and 28 days.
- Set: typically 4 cylinders per 100 yd³ or per pour day, whichever more frequent
- 7-day break is an early indicator — typically 70% of 28-day strength
- 28-day is the design strength check
- If 28-day fails: ACI 318 specifies retest with core samples; persistent failure may require demolition of the affected pour

**What PSI to spec**: Default to local convention plus 500 psi for safety. A 3,000-psi residential mix is typical. Spec 4,000 for garages and exposed exterior, 5,000+ only when engineer requires. Higher strength = more cement = more cost AND more shrinkage cracking (cement, not aggregate, shrinks).

### 4.7 CMU — Concrete Masonry Units

Concrete blocks. Standard sizes (nominal): 4", 6", 8", 12" thick. Actual = nominal minus ⅜" (for 8" mortar joint).

**Types**:
- **Hollow** — most common, can be reinforced with rebar and grouted
- **Solid** — used where no grout is needed, e.g., bond beam course
- **Bond beam blocks** — U-shape, used for horizontal bond beams (continuous reinforced course at top of wall, at floor lines, above openings)

**Grouting** — pour concrete (grout, typically 2,000 psi, high-slump, pea-gravel mix) into cells with vertical rebar. Two methods:
- **High-lift** — grout the whole wall after laying up (requires cleanouts at bottom of wall to flush out mortar droppings)
- **Low-lift** — grout in 4'–5' lifts as the wall is laid

**Reinforcing**:
- Vertical bars (#4 or #5) at 16"–48" o.c. depending on engineering
- Horizontal joint reinforcement (ladder or truss wire, e.g., Dur-O-Wall) every other course
- Bond beam (with continuous horizontal rebar) at top of wall, at intermediate heights, and above openings

**Lintels** — beams over openings in CMU walls. Options: precast concrete lintel, steel angle (L-shape), bond-beam block with rebar, or CMU lintel block with rebar. Lintel bears on jamb minimum 8" each side.

### 4.8 Retaining Walls

**Cantilever concrete retaining walls** — reinforced concrete wall and footing form an L (or inverted T). The footing must be wide enough that soil weight on the heel stabilizes the wall against overturning.

Typical residential retaining wall design checks:
1. **Overturning** — moment from soil pressure must be < resisting moment (×1.5 safety factor)
2. **Sliding** — soil friction on footing base must exceed sliding force (×1.5 SF)
3. **Bearing** — soil pressure at toe must be < allowable bearing
4. **Internal stress** — stem and footing reinforcing must handle bending

**CMU retaining walls** — similar concept but masonry stem. Vertical rebar in cells, grouted full height. Bond beams horizontally. Often less expensive than concrete for small walls.

**Drainage** — *the* failure mode for retaining walls is water pressure (hydrostatic) building up behind. Required:
- Weep holes (3"–4" pipe through wall at 6'–10' o.c., or full drain pipe at base behind the wall)
- Filter fabric (geotextile) wrapped around drain rock
- 12"–24" of free-draining backfill (crushed rock or gravel) against back of wall
- Daylight or sump connection — water must have somewhere to go

**Waterproofing** — back of wall coated with bituminous or sheet membrane if any wet face is unacceptable.

**Heights and design responsibility**:
- ≤ 3'–4' (varies by jurisdiction) — typically no permit, prescriptive design OK
- 4'–6' — permit required, may use prescriptive tables (NCMA TEK manuals)
- > 6' or supporting surcharge — engineered design required
- Any wall supporting a structure or driveway = engineered regardless of height

---

## 5. Steel

### 5.1 Structural Steel Shapes

| Shape | Description | Residential use |
|---|---|---|
| **W-shape** (W12×26 = "12-inch deep, 26 lb/ft") | Wide-flange I-beam | Long-span beams (garage openings, great rooms, ridge beams), moment frames |
| **HSS** (Hollow Structural Section, e.g., HSS6×6×¼) | Square or rectangular tube | Columns, exposed structural posts, sometimes beams |
| **C-channel** (e.g., C8×11.5) | C-shape | Stair stringers, light beams |
| **Angle (L-shape)** (e.g., L4×4×⅜) | L-shape | Lintels in masonry, brick shelf supports, connectors |
| **Plate** (e.g., PL ½"×8"×0'-10") | Flat | Bearing plates, gussets, moment connection plates |
| **Pipe column** (e.g., 4" XS pipe) | Round pipe | Basement columns, lally columns |

**Designations**: A36 = older mild steel (36 ksi yield). A992 (Grade 50) = current standard for W-shapes (50 ksi yield). HSS = A500 or A1085. Designating "A36" on a W-shape on new drawings is technically wrong — call the engineer.

### 5.2 Steel Connections

**Bolted connections**:
- **A325 / A490** high-strength bolts — most common for structural steel
- **Snug-tight** vs. **pretensioned** vs. **slip-critical** — pretensioned/slip-critical requires turn-of-nut or DTI (direct tension indicator) washers
- Bolt holes: standard = bolt diameter + 1/16"; short slot, long slot, oversized for alignment tolerance
- Inspection: count bolts, verify size and grade marking on head (3 radial lines = A325)

**Welded connections** — fillet welds, groove welds (penetration welds). Residential typically fillet only.
- Welder qualification — for structural welds in many jurisdictions, AWS-certified welder required and welds inspected (visual, sometimes UT)
- Field welds vs. shop welds — shop welds are generally higher quality (controlled conditions). Specify shop welds where possible.
- **Don't weld galvanized steel** without proper ventilation — galvanized fumes (zinc oxide) cause "metal fume fever"

**Moment vs. shear connections**:
- **Shear connection** — transfers only vertical load (beam-to-column simple connection, typical residential). Allows the beam to rotate at the support, like a hinge.
- **Moment connection** — transfers vertical load AND moment (rigid). Used in moment frames where lateral resistance comes from the frame itself, not shear walls. More complex — full-penetration welds or heavy bolted flange plates.

### 5.3 Post-Installed Anchors

For attaching steel posts, ledgers, or hold-downs to existing concrete (renovations, additions, retrofits).

**Mechanical anchors**:
- **Wedge anchors** (Hilti Kwik Bolt, Simpson Wedge-All) — expansion at end of bolt as nut tightens
- **Sleeve anchors** — friction along full embedment
- **Drop-in anchors** — internal expander, allows shorter embedment
- **Screw anchors** (Titen HD) — self-tapping into concrete, no expansion, can be removed

**Adhesive (epoxy) anchors**:
- **Hilti HIT-RE 500 V3, HIT-HY 200**, Simpson SET-XP — two-part epoxy injected into clean hole, threaded rod or rebar inserted
- **Higher capacity** than most mechanical anchors, work in cracked concrete (where rated)
- **Sensitive to hole cleanliness** — manufacturers require specific brushing and air-blowing procedures
- **Cure time** — varies with temperature, several hours to overnight before loading

**Pullout vs. shear**:
- **Pullout (tension)** — pulling the anchor straight out
- **Shear** — load perpendicular to anchor (e.g., a steel plate trying to slide)
- Anchor capacity tables list each separately, plus combined loading
- Hold-down anchors are tension-loaded; ledger bolts can be both

**Embedment depth** — critical. The deeper the embedment, the higher the capacity. Manufacturer spec is minimum; don't go shorter. Common mistake: drilling too shallow because of rebar interference, then using a shorter bolt — capacity drops to nothing.

**Critical install rules**:
- Use the correct drill bit diameter — listed in product literature. Too large = no grip; too small = bolt won't seat.
- Clean the hole. Adhesive anchors especially — failure to brush and blow out dust is the #1 cause of pullout. Manufacturer-specified brush and 4-cycle blow-brush-blow-brush procedure.
- Concrete strength matters — capacities are listed for specific f'c (e.g., 2,500 psi). Low-strength or cracked concrete reduces capacity.
- Edge distance and spacing — anchors near edges or close together have reduced capacity. Manufacturers publish minimum edge distance and spacing tables.
- Special inspection — adhesive anchors in seismic zones typically require special inspection (continuous or periodic) per IBC Chapter 17.

### 5.4 Light Gauge Steel Framing (Cold-Formed Steel — CFS)

Cold-formed C-shapes and tracks made from 18–14 gauge galvanized steel.

**Where used in residential**:
- Basement walls (non-bearing partitions, doesn't rot in damp basements)
- Mid-rise wood-frame buildings (wood at lower levels switched to CFS for upper levels in some Type V over Type I)
- Interior non-bearing walls in commercial/mixed-use
- Soffit framing, ceiling framing, drop ceilings
- Sometimes load-bearing walls in modular or panelized construction

**Stud designations**: 600S162-43 means:
- 600 = 6" (6.00") depth
- S = stud (T = track)
- 162 = 1.625" flange width
- 43 = 43-mil thickness (~18 gauge)

**Gauges**:
- 25 ga (18 mil) — non-structural, partition only
- 20 ga (33 mil) — light load
- 18 ga (43 mil) — structural, common bearing wall
- 16 ga (54 mil) — heavier
- 14 ga (68 mil) — heavy bearing

**Track** — U-shape that the stud sits in, top and bottom

**Fasteners** — self-drilling screws (Tek screws), pan-head or wafer-head for stud-to-track and sheathing-to-stud. Don't use drywall screws structurally — they snap.

### 5.5 Lally Columns and Point Loads

A **lally column** is a steel pipe (typically 3½" or 4" diameter, schedule 40) filled with concrete (originally — modern lally is often just steel pipe). Used in basements to support floor girders and remove mid-span sag.

**Components**:
- Steel pipe column
- **Top plate** (cap) — welded steel plate, ~⅜" × 6"× 6", with edges turned up or with anti-rotation tab
- **Bottom plate** (base) — welded steel plate, sized for bearing on concrete footing
- **Concrete footing or pad** — sized for the load and soil bearing

**Adjustable steel columns** (with screw jack at top) — useful for new construction with leveling needed, but **not permitted as permanent structural columns in most codes** without specific listing. They can creep, rust, and lose adjustment. Inspectors will fail an adjustable column installed as a permanent structural support unless it's a listed product (e.g., Akron Adjusta-Post) for that use.

**Point loads** — when a beam lands on a column, that point load must be carried straight down through a continuous load path:
1. Column → bearing plate → footing
2. Footing must be sized for the point load + soil bearing
3. If column lands on a slab, the slab must be thickened beneath OR an isolated footing poured

**Typical residential point load issue**: New beam added in a remodel needs to land on a post that lands on... a slab. Without a footing beneath, the slab cracks and the column sinks. Always extend the load to engineered footing.

---

## 6. Seismic Design — California Specific

### 6.1 Seismic Design Categories (SDC)

SDC is determined by:
1. **Site spectral accelerations Ss (short period) and S1 (1-second)** from USGS Seismic Design Maps (search address at hazards.atcouncil.org or USGS site)
2. **Site class** (A–F) — soil classification from a soils report or default
3. **Risk Category** (I–IV) — most residential is II
4. The resulting SDS and SD1 fall into SDC A (lowest seismic risk) through F (highest)

| SDC | Risk level | Region examples |
|---|---|---|
| **A** | Negligible | Florida, parts of Texas |
| **B** | Low | Midwest (most), Southeast (most) |
| **C** | Moderate | Some West Coast valleys, parts of Tennessee, New Madrid edges |
| **D** | High | Most of California, Pacific Northwest, parts of Salt Lake City |
| **E, F** | Very high | Near major faults (parts of Bay Area, LA basin), high-risk-category buildings |

**Most California residential = SDC D.** Some hillside sites near major faults are SDC E.

### 6.2 Prescriptive vs. Engineered Path

The **California Residential Code (CRC, based on IRC)** allows two paths:

1. **Prescriptive (conventional construction)** — follow CRC Sections R602.10 (wall bracing), R301 (loads), etc. No engineering needed if all the prescriptive limits are met.
2. **Engineered** — structural engineer designs the LFRS per ASCE 7 / SDPWS

**Prescriptive limits** (R301.2.2.1 and similar) — prescriptive path NOT allowed if:
- Building height > 2 stories (or 3 in some cases)
- Irregularities: cantilevered walls, large openings, stories shifted in plan, mass irregularities
- Cripple walls > 4'
- Hillside conditions
- SDC E (parts of California near faults)
- Site Class E or F (poor soil)

In practice in California, **most custom residential is engineered**, not prescriptive. Tract builders use prescriptive on simple plans.

### 6.3 Braced Wall Panels (Prescriptive)

When using the prescriptive path, lateral resistance is provided by **braced wall panels (BWPs)** spaced at intervals along each braced wall line. Methods listed in IRC R602.10.4:

| Method | Description |
|---|---|
| **LIB** | Let-in 1x4 bracing (rare now) |
| **DWB** | Diagonal wood boards (almost obsolete) |
| **WSP** | Wood structural panel sheathing (plywood/OSB) — **most common** |
| **SFB** | Structural fiberboard |
| **PCP** | Portland cement plaster (stucco over wood frame) |
| **GB** | Gypsum board |
| **PBS** | Particleboard sheathing |
| **PFH** | Portal frame with hold-downs (used at garage openings) |
| **PFG** | Portal frame at garage |
| **CS-WSP, CS-G, etc.** | Continuous sheathing methods |

**Spacing and length** per code table by SDC, story, and wall length:
- In SDC D, BWPs typically need to be at intervals of ≤ 25' along each braced wall line
- Min panel length depends on stud height (e.g., 48" for an 8' wall)

### 6.4 Soft-Story Buildings and Retrofit

**Soft-story** building — first story is significantly weaker/more flexible than upper stories. Classic example: tuck-under-parking apartment with the front of the ground floor mostly open garage doors. Failed catastrophically in the 1989 Loma Prieta and 1994 Northridge earthquakes.

**California retrofit ordinances**:
- **SB 1818 / SB 99 (statewide framework)** — enabling legislation
- **City ordinances** drive actual enforcement:
  - **Los Angeles (LADBS)** — Ordinance 183893 (2015): mandatory retrofit of pre-1978 wood-frame soft-story buildings with ≥ 2 stories above a soft, weak, or open-front (SWOF) story
  - **San Francisco** — mandatory soft-story retrofit ordinance, by tier
  - **Berkeley, Oakland, West Hollywood, Santa Monica, Pasadena, Beverly Hills** — similar programs
- Typical retrofit: install steel moment frames at garage openings, plywood shear panels and hold-downs on existing first-floor walls, foundation strengthening

### 6.5 Cripple Walls

A **cripple wall** is a short stud wall between the foundation and the first floor (raised foundation homes). In old California houses, these are often unbraced or sheathed only with brittle finishes — they fail in earthquakes, dropping the house off its foundation.

**Cripple wall retrofit (CRC Appendix AA, Plan Set A / ICC-style)**:
- Install ½" structural plywood sheathed on inside face of cripple wall, blocked
- 8d common nails at 4" o.c. edges, 12" o.c. field (or denser per engineer)
- Foundation bolts added by epoxy (titen HD or Hilti HIT-RE) if missing
- Plate washers added at all anchor bolts
- Cripple walls > 4' require engineered design (prescriptive path ends)

### 6.6 Anchor Bolt Standards at Mudsill

For prescriptive construction in SDC D (typical California):

| Spec | Requirement |
|---|---|
| Diameter | ⅝" minimum (½" only for very light loads) |
| Embedment | 7" minimum |
| Spacing | 6' o.c. max in SDC A–C; **4'-6' o.c. max in SDC D, E, F** (verify per engineer or per code table) |
| End distance | 7 bolt diameters or 7" from cut end of sill plate, max 12" from ends |
| Plate washer | 3" × 3" × 0.229" (¼" nominal) required in SDC D, E, F |
| Hole oversizing | Standard ⅛" oversize; do NOT enlarge to "make it fit" |

**Plate washers** are not optional in California SDC D. They prevent the sill plate from splitting upward through the nut during seismic uplift. An inspector will fail mudsill without them.

### 6.7 Site-Specific Seismic Analysis

Required when:
- Site Class F soils (very soft, organic, sensitive clay, liquefiable, peat) — requires site-specific ground motion analysis per ASCE 7
- Near-fault site (within ~9 mi of major fault) for some building types — near-fault directivity adjustments
- Performance-based design (PBD) — for unique, tall, or special-use buildings
- Hillside / landslide-prone sites — slope stability analysis

The geotechnical engineer provides ground motion parameters; the structural engineer designs to them. This bumps the engineer cost up — budget for it on hillside or fill sites.

---

## 7. Reading Structural Drawings

### 7.1 Sheet Organization

A typical residential structural set:

| Sheet | Contents |
|---|---|
| **S0.1 — General Notes** | Code basis, design loads, material specs (concrete, rebar, lumber, hardware), special inspection list, abbreviations, symbols. **Read this first, every time.** |
| **S1.0 — Foundation Plan** | Plan view of all footings, pads, piers, anchor bolts, hold-down anchors. Elevations / step downs. Slab edge and thickenings. |
| **S2.0 — First Floor Framing Plan** | Joist layout, beams, headers, posts, bearing points, shear walls. |
| **S2.1 — Second Floor Framing Plan** | Same for second floor. |
| **S3.0 — Roof Framing Plan** | Rafter or truss layout, ridge, valley, hip framing, blocking, ties. |
| **S4.0 — Schedules** | Beam schedule, header schedule, post schedule, hold-down schedule, footing schedule. |
| **S5.0+ — Details** | Connection details, foundation sections, framing sections, shear wall details, hold-down installation. |

### 7.2 Foundation Plan — What to Look For

- **Grid lines** — A, B, C... and 1, 2, 3... reference points for locating everything
- **Footing callouts** — F1, F2, F3 (referenced to footing schedule)
- **Stem wall heights and step-downs** — site grade changes
- **Anchor bolt callouts** — typically by note or symbol (often "A.B." with size and spacing)
- **Hold-down anchor locations** — circled, with type callout (HDU5-SDS2.5, SSTB20, etc.)
- **Rebar callouts** — sometimes on plan, more often in section details
- **Underground utility coordination** — sleeve locations, plumbing penetrations

**Before pouring**, walk the foundation with the plan in hand and verify:
- Every footing dimension matches plan
- Every anchor bolt is set per plan (count them, measure spacing)
- Every hold-down anchor is in the right location (most critical)
- All rebar is per schedule (cover, lap, hooks at corners)
- Sleeves and penetrations are in (plumbing, electrical conduit, radon)

### 7.3 Framing Plan — What to Look For

- **Joist direction arrows** — which way the joists run, with size and spacing (e.g., "2x10 DF #2 @ 16" o.c.")
- **Beams** — drawn as heavier lines, called out (e.g., "B1: (3) 1¾"x11⅞" LVL")
- **Headers** — at every opening (door, window) below
- **Posts** — at beam ends and bearing points, called out (e.g., "P1: (3) 2x6")
- **Bearing walls** — typically hatched or shaded differently than non-bearing
- **Shear walls** — heavy lines or distinct hatch, with type/tag (e.g., "SW-1" → see shear wall schedule for nailing)
- **Hold-down locations** — typically at each end of every shear wall

### 7.4 Structural Abbreviations

| Abbreviation | Meaning |
|---|---|
| BM | Beam |
| BLDG | Building |
| BLK / BLKG | Block / blocking |
| BRG | Bearing |
| BTM | Bottom |
| CJ | Control joint, or ceiling joist (context) |
| CL or ¢ | Centerline |
| CLR | Clear |
| CONT | Continuous |
| COL | Column |
| CONC | Concrete |
| DBL | Double |
| DF | Douglas Fir |
| DIA or ø | Diameter |
| EA | Each |
| EQ | Equal |
| EW | Each way (for rebar in slabs) |
| EOR | Engineer of Record |
| FDN | Foundation |
| FT | Footing |
| FTG | Footing |
| GLB or GLU | Glulam |
| HDR | Header |
| HD | Hold-down |
| HSS | Hollow Structural Section |
| LVL | Laminated Veneer Lumber |
| MAX | Maximum |
| MIN | Minimum |
| O.C. | On center |
| OPNG | Opening |
| PT | Pressure-treated (or post-tensioned, by context) |
| PSL | Parallel Strand Lumber |
| SIM | Similar |
| SHW or SW | Shear wall |
| STD | Standard |
| STIFF | Stiffener |
| STL | Steel |
| TBJ or TJI | I-joist (TrusJoist trademark, often used genericly) |
| T&G | Tongue & groove |
| TYP | Typical |
| U.N.O. | Unless noted otherwise |
| VIF | Verify in field |
| WSP | Wood structural panel |
| W/ | With |

### 7.5 Typical Details and the "Override" Hierarchy

Structural drawings rely on **typical details** ("TYP") to avoid drawing every condition. The general principle:

1. **Specific callout in plan / section** overrides
2. **Schedule** (beam schedule, hold-down schedule)
3. **Typical detail** referenced
4. **General notes** (default for anything not otherwise specified)

When in doubt, escalate to the engineer. Do not assume the typical detail applies if there's any specific note nearby — read both, ask if conflicting.

### 7.6 Coordination Between Structural and Architectural

The eternal conflict: structural calls for a post that the architect's plan doesn't show, OR the architect's elevation requires a window where the structural has a shear wall.

**Resolution priorities**:
1. **Life safety / structural integrity** wins — you can't move a load path because it's inconvenient
2. **Architectural intent** is preserved when possible — the engineer designs around the architecture
3. **Dimension control** — when dimensions conflict, the architectural plan typically controls plan dimensions; the structural plan controls structural sizes and connections; the MEP plans control utility routing. RFI for any conflict.

**Common conflicts and how they get resolved**:
- Beam depth conflicts with ceiling height → engineer changes to a shallower section (e.g., steel W-beam instead of glulam) at higher cost
- Post lands in middle of a room → engineer relocates with header pickup or column wraps to disguise
- Shear wall conflicts with window → engineer relocates shear wall OR uses a portal frame (PFH) to allow the opening
- HVAC duct conflicts with joist → joist re-engineered with allowable hole, or duct rerouted

**Your role as GC** — flag conflicts during pre-construction coordination meetings, NOT in the field when concrete is being poured. Most coordination issues are foreseeable if architectural + structural + MEP are reviewed side-by-side.

---

## 8. Common Framing Mistakes and Quality Control

### 8.1 Top 10 Framing Inspection Failures

Based on what inspectors most commonly cite:

1. **Missing hardware** — joist hangers absent, hurricane ties skipped at every other rafter, post bases not anchored. Walk-through after framing rough and before insulation.
2. **Wrong / undersized nailing** — clipped-head gun nails (0.113") used where 8d common (0.131") specified. Edge nails > ⅜" from edge. Overdriven nails. Inadequate nails per hanger (half-nailed hangers).
3. **Undersized headers** — opening grew during framing, header didn't grow with it. Or, framer used "2x10 because we have it" instead of the LVL specified.
4. **Shear wall sheathing missing blocking** — panel edges meeting in the field of the wall without solid blocking behind. Inspector won't see the framing once sheathing is up — verify before sheathing closes it in.
5. **Hold-downs not properly installed** — wrong type substituted, anchor bolt missed (no anchor below hold-down), anchor too short, hold-down nuts not snug-tight, hold-down not on a 3-stud minimum post pack.
6. **Anchor bolts missing plate washers** (SDC D requires) — easy fix during framing, expensive after sheetrock.
7. **Notching / drilling beyond code** — joist or stud notched > 1/6 of depth, holes > ⅓ of depth, holes too close to edges. I-joists drilled outside allowed zones.
8. **Sheathing nails missed framing** — "shiners" (nails that missed the framing member and only penetrate sheathing). Inspector will sight along the sheathing edge looking for these.
9. **Roof venting / fire-blocking missing** — at top of stud bays in 2-story walls, behind soffit returns, at chimney chases. Often forgotten.
10. **Stairs out of code** — riser height inconsistent (>⅜" variation), tread depth too small, headroom too low at landings, guards/handrails missing or wrong height.

### 8.2 Pre-Framing Inspection Checklist (GC walks before inspector arrives)

**Foundation interface**:
- [ ] Mudsill is PT (pressure-treated), correct size (2x6 typical), properly capped at corners
- [ ] Anchor bolts at correct spacing, with washers and snug-tight nuts, plate washers per SDC
- [ ] Hold-down anchors visible, in correct positions, threads engaged with hold-down nut
- [ ] No bowed / cupped mudsill — flat to concrete with sill seal

**Wall framing**:
- [ ] Stud spacing correct (16" / 24" o.c. per plan)
- [ ] Top plates doubled, laps offset and nailed per schedule
- [ ] Headers per schedule, with correct jacks and kings
- [ ] Posts continuous to bearing below (no posts landing on subfloor only)
- [ ] Hold-down posts are correct stud pack size (e.g., (3) 2x6 stud pack at HDU8)

**Floor / ceiling framing**:
- [ ] Joist hangers installed with all holes filled, correct nails
- [ ] Solid blocking at joist ends and at mid-span for required spans
- [ ] Squash blocks under bearing walls above (I-joists)
- [ ] Subfloor glue-nailed per spec, no overdriven nails

**Shear walls**:
- [ ] Sheathing per schedule (thickness, type)
- [ ] Nail spacing per schedule, measured at random panels
- [ ] All panel edges supported (blocking present where required)
- [ ] No overdriven nails (sample 10 random nails)
- [ ] Hold-downs at every shear wall end, correct type and anchored
- [ ] 3" × 3" plate washers at sill anchor bolts (SDC D/E/F)

**Roof framing**:
- [ ] Hurricane ties / rafter ties at every rafter or truss
- [ ] Truss bracing per BCSI (top chord laterals, bottom chord laterals, X-bracing)
- [ ] No field-modified trusses (no cuts, drills, or notches)
- [ ] Sheathing per schedule, nail spacing per schedule, no overdriven nails
- [ ] Ridge ventilation / soffit ventilation per architectural plans

**Miscellaneous**:
- [ ] Fire blocking at all required locations (top/bottom of stud cavities, soffits, chases)
- [ ] Draft stops in floor cavities > 1000 sf
- [ ] Stair geometry: riser ≤ 7¾", tread ≥ 10", riser variation ≤ ⅜" max, headroom ≥ 6'-8"
- [ ] Notch and bore limits respected, no rogue plumbing notches

### 8.3 Moisture in Framing

**Acceptable moisture content (MC)**:
- Framing lumber: ≤ 19% (S-DRY grade stamp)
- Engineered lumber (LVL, I-joist): ≤ 16% per manufacturer
- Before drywall closes the wall: ≤ 19% (some specs require ≤ 15%)
- Hardwood flooring substrate: ≤ 12% for joists, ≤ 8% for hardwood

**Use a pin-type or pinless moisture meter** (Wagner, Delmhorst) and spot-check during construction. Critical points:
- After rough framing, before sheathing
- After a rain delay
- Before insulation closes the wall
- Before drywall

**Consequences of framing wet**:
- **Shrinkage** — lumber shrinks ~⅛"/foot in width as it dries from 30% MC to 8%. A wet 2x12 joist loses ~⅛"–¼" of depth and floor sags. Drywall cracks at corners. Doors stick. Floors squeak.
- **Mold** — wet wood > 70°F for > 48 hours grows mold in the wall cavity. Hidden, hard to find later, eventually a callback.
- **Hardware corrosion** — galvanized hardware can corrode in wet wood (zinc + acidic wet lumber = white powder, reduced strength). Stainless or extra-thick galvanized (G185) for PT lumber.
- **Fastener withdrawal** — nails in wet lumber lose holding power as the wood shrinks around them. Loose nails = loose connections = squeaks and creaks.

**Mitigation**:
- Tarp lumber on-site (off the ground, on dunnage)
- Don't close walls until dry — even if schedule pressure exists
- Use kiln-dried lumber where possible; engineered lumber is dimensionally stable but expensive
- Run dehumidifiers / heat after a wet delay if needed before continuing

### 8.4 Managing Field Changes — "We Can't Make It Work"

The sub comes to you: "There's a duct in the way of that beam. We can't put it there."

**Bad GC response**: "Just move it 6 inches."
**Worse GC response**: "OK, do whatever you need to do."
**Good GC response**:
1. **Stop the work** at that location
2. **Document** with photo and measurement
3. **Issue RFI** to architect and structural engineer with the conflict described, plus 1–2 proposed solutions
4. **Wait** for written response (don't proceed verbally — emails/RFIs are the record if there's a callback or failure)
5. **Update as-builts** with the approved change

**When you can solve in field without RFI**:
- Trivial deviations (joist moved 1"-2" to clear a vent stack, where the engineer's intent is preserved)
- Items explicitly delegated ("contractor to coordinate joist layout to avoid plumbing")
- Standard typical conditions where the typical detail clearly applies

**When you absolutely escalate**:
- Anything that changes a load path
- Anything that resizes or relocates a beam, column, or shear wall
- Anything affecting a hold-down or anchor bolt location
- Any modification to a truss or engineered member
- Anything that the inspector might catch and you can't justify with a written engineer response

**The RFI / change record is your liability shield.** If a beam is undersized and fails 5 years later, the engineer of record's stamp + written approval of the field condition is what keeps you out of the lawsuit. Verbal "yeah, that's fine" from the engineer at the job site is worthless without a follow-up email or RFI response.

---

## Appendix A: Quick Reference Tables

### A.1 Nail Designations

| Nail callout | Common dia. | Length | Common use |
|---|---|---|---|
| 6d common | 0.113" | 2" | Light framing, lath |
| 8d common | 0.131" | 2½" | Sheathing (most common), framing |
| 8d box | 0.113" | 2½" | Sheathing (lower capacity than 8d common) |
| 10d common | 0.148" | 3" | Joist hangers, heavy sheathing |
| 10d × 1½" | 0.148" | 1½" | Joist hangers (short to avoid splitting 2x face) |
| 16d common | 0.162" | 3½" | Framing nailer, plate-to-plate, stud-to-plate |
| 16d sinker | 0.148" | 3¼" | Gun nail equivalent (slightly less capacity than 16d common) |
| 20d common | 0.192" | 4" | Heavy framing |

**Pneumatic gun nails** — verify shank diameter. Many "16d" gun nails are 0.131"–0.148" (sinkers) and have less capacity than 16d common. Engineers and inspectors increasingly call out specific diameters: "16d (0.162") common nails" leaves no ambiguity.

### A.2 Span Tables — Cheat Sheet (DF #2 framing, residential, simple span)

**Floor joists, 40 psf LL + 10 psf DL, L/360 deflection:**

| Joist | 12" o.c. | 16" o.c. | 19.2" o.c. | 24" o.c. |
|---|---|---|---|---|
| 2x8 | 14'-2" | 12'-10" | 12'-1" | 11'-3" |
| 2x10 | 17'-9" | 16'-1" | 15'-2" | 14'-1" |
| 2x12 | 21'-7" | 19'-7" | 18'-5" | 17'-2" |

**Ceiling joists, 20 psf LL + 10 psf DL, no future room:**

| Joist | 12" o.c. | 16" o.c. | 24" o.c. |
|---|---|---|---|
| 2x6 | 13'-9" | 12'-6" | 11'-0" |
| 2x8 | 18'-1" | 16'-5" | 14'-4" |

(These are approximate — always defer to AWC Span Tables or engineer.)

### A.3 Hold-Down Quick Reference

| Hold-down | Tension capacity (lb, allowable) | Typical anchor | Post requirement |
|---|---|---|---|
| HTT4 | 3,165 | SSTB16 or ⅝" AB | 4x or (2) 2x6 |
| HTT5 | 4,605 | SSTB16 or ⅝" AB | 4x or (3) 2x4 |
| HDU2 | 3,075 | SSTB16 / SB ⅝×8 | 4x4 |
| HDU4 | 4,565 | SSTB20 / SB ⅝×24 | 4x4 |
| HDU5 | 5,645 | SSTB20 / SB ⅝×24 | (3) 2x4 or 4x4 |
| HDU8 | 7,870 | SSTB24 / SB ⅞×24 | (3) 2x6 or 4x6 |
| HDU11 | 9,335 | SB1×24 | (3) 2x6 or 4x6 |
| HDU14 | 14,445 | SB1×30 | (4) 2x6 or 6x6 |
| PHD2 | 3,285 | (2) ⅝" through-bolts | (2) 2x4 |
| PHD5 | 5,360 | (2) ⅝" through-bolts | (3) 2x4 |

Always verify against the current Simpson Strong-Tie catalog — capacities and details are updated regularly.

### A.4 Concrete Mix Quick Reference

| Application | f'c (psi) | Slump | Aggregate | Air entrainment |
|---|---|---|---|---|
| Mud slab / blinding | 2,000 | 5"–7" | ¾" or pea | No |
| Continuous footings | 2,500–3,000 | 4"–6" | ¾" | No (unless freezing) |
| Stem walls | 3,000 | 4"–5" | ¾" | No (unless freezing) |
| Interior slab on grade | 3,000–3,500 | 4"–5" | ¾" | No (interior) |
| Garage slab | 4,000 | 4"–5" | ¾" | Yes in freezing climates |
| Exterior flatwork | 4,000–4,500 | 4"–5" | ¾" | Yes (5–7%) in freezing |
| Post-tension slab | 3,500–4,500 | 5"–6" | ¾" or ⅜" | No (PT incompatibility) |
| Driveway / sidewalk | 3,500–4,000 | 4"–5" | ¾" | Yes in freezing |
| Structural columns | 4,000–5,000 | 4"–6" | ¾" or ⅜" | No (interior) |

---

## Appendix B: When You're Stuck — Resources

- **AWC Wood Frame Construction Manual (WFCM)** — prescriptive wood frame design
- **APA — The Engineered Wood Association** (apawood.org) — span tables, panel info
- **Simpson Strong-Tie catalog** (strongtie.com) — connectors, hold-downs, anchors
- **SDPWS (AWC Special Design Provisions for Wind and Seismic)** — shear wall and diaphragm engineering
- **ACI 318** — concrete code
- **California Residential Code (CRC), California Building Code (CBC)** — the governing documents
- **IRC / IBC** — base model codes
- **ASCE 7** — Minimum Design Loads (wind, snow, seismic)
- **USGS Seismic Design Maps** (hazards.atcouncil.org / earthquake.usgs.gov) — site-specific seismic parameters
- **TPI 1 (Truss Plate Institute)** — truss engineering and bracing
- **BCSI** (Building Component Safety Information) — truss handling and installation
- **Local jurisdiction amendments** — many cities and counties modify code, especially in California (LADBS, SFDBI, etc.)

---

*Document version: 1.0 — 2026-05-12*
*Maintain alongside project-specific structural drawings and engineer correspondence.*
