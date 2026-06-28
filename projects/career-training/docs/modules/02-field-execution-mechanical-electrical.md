---
title: Field Execution of Mechanical and Electrical Work on Industrial Construction
type: reference
audience: general-contractor
discipline: [mechanical, electrical, instrumentation, controls]
codes: [ASME B31.1, ASME B31.3, NFPA 70 (NEC), NFPA 70E, AWS D1.1, API 686]
created: 2026-05-12
tags: [career-training, industrial-construction, piping, electrical, commissioning]
---

# Field Execution of Mechanical and Electrical Work on Industrial Construction

A working reference for self-performing crews and the general contractor overseeing them. The reader is assumed to be trades-fluent (former electrician, pipefitter, or millwright) stepping into a GC role where they must direct subcontractors, sign off on installations, hold their own with owner engineers, and answer to third-party inspectors. This document is denser than a homeowner's how-to and lighter than a code book — it is the field knowledge that lives between the spec and the wrench.

> **Document scope note:** This is a US-code-anchored reference. The dominant codes are ASME B31.1 (power), ASME B31.3 (process), the National Electrical Code (NFPA 70), and NFPA 70E. Owner specifications almost always tighten these — read the spec before the code.

---

## 1. Mechanical Systems on Industrial Projects

### 1.1 Process Piping vs. Utility Piping vs. Plumbing

These three categories look similar from the outside (a pipe is a pipe), but they live under different codes, different inspectors, and different consequences for failure.

| Category | Governing Code | Typical Service | Inspector | Failure Consequence |
|---|---|---|---|---|
| Process piping | ASME B31.3 | Hydrocarbons, acids, steam (process side), solvents | Owner engineer + AIA/AI (Authorized Inspector) | Release, fire, fatalities |
| Power/utility piping | ASME B31.1 | High-pressure steam, boiler feed, condensate, plant air mains, hot water | Jurisdictional boiler inspector | Steam release, boiler trip |
| Plumbing | IPC / UPC (jurisdictional) | Potable water, sanitary drains, vents, gas to fixtures | City plumbing inspector | Cross-connection, sanitary |

**Code execution differences that matter on site:**

- **B31.3 (Process)** allows random radiography (typically 5% of welds per "lot") as the default for Normal Fluid Service, and tightens to higher percentages for Category M (lethal) or severe cyclic service. It permits slightly higher allowable stresses than B31.1, which produces thinner walls for the same pressure. Tolerances on spool fabrication are tight: ±1.6 mm pipe-to-fitting for ≤24" NPS.
- **B31.1 (Power)** generally requires 100% volumetric examination (RT or UT) on high-pressure, high-temperature steam lines, longer post-weld heat treatment hold times for chrome-moly, and stricter PQR/WPS traceability.
- **Plumbing** is governed by the IPC or UPC depending on the jurisdiction, inspected by the city, and uses fundamentally different materials (PEX, copper, no-hub cast iron, ABS/PVC DWV) and joining methods (solvent weld, soldered, press-fit, no-hub clamps).

A practical site-rule: **if it has a P&ID line number, it is process; if it serves a fixture, it is plumbing; if it is between a boiler and a turbine, it is B31.1.** Inspectors do not share jurisdiction — keep their packages separated.

### 1.2 Pipe Specifications: Materials, Schedules, Fittings, Flanges

Every line has a **piping spec** (a.k.a. "line class" or "PMS"). The spec dictates material, schedule, fitting type, flange rating, gasket, bolt grade, branch reinforcement method, and NDE level. A pipefitter who reads the spec correctly cannot pick the wrong elbow.

**Material families on industrial sites:**

- **Carbon steel (CS):** A106 Gr B (seamless) for high-temp/high-pressure; A53 Gr B (ERW) for utility air, water, low-temp. The default for hydrocarbons, steam, plant air, and most process lines.
- **Low-temp carbon steel (LTCS):** A333 Gr 6 for service below −20 °F (cryogenic, LPG, refrigerated propane). Identical look to A106 but impact-tested.
- **Stainless steel:** 304/304L (general corrosion), 316/316L (chloride resistance), duplex/super-duplex (sour service, seawater). The "L" grades have lower carbon to prevent sensitization in the HAZ during welding.
- **Chrome-moly alloys:** P11 (1¼ Cr − ½ Mo), P22 (2¼ Cr − 1 Mo), P91 (9 Cr − 1 Mo − V) for high-temp steam. Require pre-heat, interpass control, and PWHT.
- **HDPE (high-density polyethylene):** Outfalls, brine, slurry, fire water (where allowed), buried utility. Joined by butt-fusion or electrofusion — both require qualified operators with calibrated machines.
- **PVC / CPVC:** Drains, low-pressure chemical, vent lines. Solvent-welded. Not for compressed gas — period.
- **Fiberglass (FRP/GRP):** Caustic, brine, demin water. Joined by bell-and-spigot adhesive or butt-and-strap layup.

**Schedule (wall thickness):** Sch 40, Sch 80, Sch 160, XS, XXS. For stainless, the equivalents are 10S, 40S, 80S. Schedule increases with pressure. Above 10" NPS, schedule numbers become non-standard — read the actual wall in mm or inches.

**Fittings:** Buttweld (BW) for ≥2", socket-weld (SW) or threaded (THD) for ≤1½", flanged at equipment and at maintenance break points. Standards: ASME B16.9 (BW), B16.11 (SW/THD forged), B16.5 (flanges ≤24"), B16.47 (flanges >24"). Branch connections are made with weldolets/sockolets/threadolets or with full reinforcing pads per the spec's branch table.

**Flanges:** Rated by pressure class — 150, 300, 600, 900, 1500, 2500. The class is **not** psi; a Class 300 flange in CS at 100 °F is good for ~740 psig but de-rates with temperature. Face types: raised face (RF) is the default, ring-type joint (RTJ) for high-pressure/high-temp, flat face (FF) when bolted to a cast-iron body. Gaskets: spiral-wound with inner/outer ring (most common), Kammprofile (high-temp, recoverable), soft-cut (utility), RTJ (oval or octagonal soft iron/SS).

**Bolting:** ASTM A193 Gr B7 stud / A194 Gr 2H nut is the workhorse. B7M / 2HM for sour service (NACE MR0175). B8/B8M for stainless service. Always torque to a pattern with a calibrated wrench; on critical joints (≥Class 600, hot service, hazardous fluid), use **hydraulic tensioning** and document the values.

### 1.3 Piping Fabrication: Spools, Shop vs. Field, Fit-up, Welding

A **spool** is a pre-assembled section of piping — typically straight pipe with elbows, tees, flanges, and short branches — fabricated to fit on a truck (often ≤40 ft, ≤8 ft wide) and lifted into the rack as a unit. Spool drawings are produced from the 3D model (or hand-isos for small jobs) and carry: line number, spool number, BOM, weld map, NDE map, and a fabrication tolerance block.

**Shop vs. field fabrication trade-offs:**

| Factor | Shop | Field |
|---|---|---|
| Welder productivity | High (positioner, downhill, automated GTAW) | Low (overhead, weather, scaffold) |
| Quality | Tightly controlled, easy NDE | Variable; harder NDE access |
| Schedule risk | Long lead | Responsive to changes |
| Field fit | Requires "field weld" gaps and adjustment spools | Naturally accommodating |
| Cost | Lower $/diameter-inch (DI) | Higher $/DI |

A common rule: maximize shop fabrication; leave **field-weld (FW) joints** at strategic locations — typically one or two per spool — and **leave one spool per loop with a 4–6" stub long** for cut-to-fit adjustment per B31.3 fabrication practice.

**Fit-up:** Before tacking, verify alignment, gap (typically 3/32"−1/8" for open-root GTAW; tighter for SMAW with backing), internal misalignment ("hi-lo," limited to 1.6 mm per B31.3), and squareness. Spider clamps, chain clamps, and external line-up clamps are the tools. Bevel angle is set per the WPS (commonly 30° single-V or compound).

**Welding processes used in the field:**

- **SMAW (stick, Process 111):** The universal field process for CS. E6010 root, E7018 fill/cap on most CS pipe. Tolerant of wind and contamination. Slower deposition.
- **GTAW (TIG, Process 141):** Root pass on stainless, alloy, and high-purity. Required for sanitary and stainless process. Argon shielding; needs wind screens outdoors.
- **FCAW (flux-cored, Process 136):** High-deposition fill/cap on heavy-wall CS structural and piping. Self-shielded (FCAW-S) or gas-shielded (FCAW-G). Common on storage tank shells.
- **GMAW (MIG):** Less common on code pipe but used on tank shells, structural, and shop fab.
- **Combo welds:** GTAW root + SMAW fill/cap on stainless and alloy is the industrial standard.

Every weld must be made to a **qualified Welding Procedure Specification (WPS)**, backed by a **Procedure Qualification Record (PQR)**, by a welder qualified under ASME Section IX with a current continuity log. The welder's stamp goes on every joint or on the weld map.

### 1.4 Weld Inspection: VT, PT, MT, UT, RT

| Method | Detects | When required (typical) |
|---|---|---|
| **VT** (Visual) | Surface defects, profile, undercut | 100% of all welds, every code |
| **PT** (Liquid Penetrant) | Surface-breaking cracks on non-magnetic materials (stainless, alloys, aluminum) | Stainless root passes, weld repairs |
| **MT** (Magnetic Particle) | Surface and near-surface defects on ferromagnetic materials | CS root passes, fillet welds on alloy, casting repairs |
| **UT** (Ultrasonic) | Volumetric subsurface defects; PAUT/TOFD increasingly accepted in lieu of RT | Heavy wall (>1"), structural T/K/Y joints, weld repairs |
| **RT** (Radiography) | Volumetric defects; the historical gold standard | 5% random under B31.3 Normal Service; 100% on Category M, severe cyclic, B31.1 high-energy |

**B31.3 acceptance criteria** live in Table 341.3.2. For Normal Fluid Service, no cracks, no lack of fusion, limited porosity (single pore ≤¼T or 3 mm, whichever is less), limited slag, defined undercut limits, and minimum/maximum reinforcement. Reject a weld and you cut it out, re-weld, re-NDE. Cut-out, rework, and re-NDE is **the** schedule killer on process projects — every 1% increase in reject rate cascades into rerun radiography, rerun PWHT, and rerun hydro.

**The NDE map** is the GC's friend. It tells every welder which joints will be radiographed and lets you concentrate your best hands there.

### 1.5 Pressure Testing: Hydrostatic vs. Pneumatic

**Hydrostatic test** is the default per B31.3 §345.4. Test pressure = **1.5 × design pressure × (stress ratio Sₜ/S)** corrected for temperature. Hold time ≥10 minutes after gauge stabilization, then walk every joint at design pressure. Water is the test medium because it is nearly incompressible — a failure releases stored elastic energy in tens of milliseconds, not catastrophically.

**Pneumatic test** (B31.3 §345.5) is permitted only when (a) hydrotest would damage linings/refractory, (b) traces of water cannot be tolerated, or (c) drying is impractical. Pressure ramp is staged: 25 psig → half test pressure with 10-min hold and bubble-test → full test pressure. The owner usually requires a **stored-energy evaluation** and an exclusion zone calculated from TNT-equivalent. Pneumatic is dangerous; many owners prohibit it above 15 psig without a written deviation.

**Test packages** are the GC's documentation deliverable. Each package contains:

- Marked-up P&ID and isometrics with test boundary highlighted
- Blind list (every spade location, with tags)
- Valve isolation list and "leave-open / leave-closed" instructions
- Calibration certificates for the pressure gauge (within 6 months, two gauges minimum, one digital one analog) and any relief valve
- WPS/PQR/welder qualifications for every weld in the package
- NDE reports
- PWHT charts (if applicable)
- Test pressure calculation sheet, engineer-approved
- Witness signature sheet (contractor QC, owner, AI if applicable)

A clean test package handed to the AI on day-of saves rerun tests. A messy one costs days.

### 1.6 Equipment Installation: Pumps, Compressors, Heat Exchangers, Vessels, Tanks

**Foundation acceptance** comes first. Verify anchor bolt pattern, projection, sleeve location, and concrete strength (typically ≥3,000 psi or per spec, often ≥4,000 psi for rotating equipment). Foundation top is rough — never set equipment directly on it. Chip to clean, sound concrete and ensure ¾"–1½" grout space.

**Soleplate / baseplate setting:** Set on jack-screws or shim packs. Level to ±0.002 in/ft (0.17 mm/m) — tighter for high-speed turbomachinery (per API 686). Pre-grout the baseplate before final coupling alignment if the spec permits; otherwise rough-align, grout, then fine-align cold.

**Grouting:** Non-shrink cementitious grout for general service; epoxy grout (high-strength, chemical-resistant, vibration-dampening) for rotating equipment, compressors, and any service with thermal cycling or chemical exposure. Pour from one side only to avoid air entrapment; vent the far side; head box on the high side to develop hydrostatic head. Cure ≥7 days before final alignment on epoxy, ≥3 days on cementitious.

**Coupling alignment** for direct-coupled pumps and motors:
- Soft-foot check first (≤0.002 in deflection at each foot when bolts loosened one at a time)
- Initial rim-and-face dial indicators or laser tool (Pruftechnik, Ludeca, SKF)
- Targets: angular ≤0.0005 in/in, parallel offset ≤0.002 in cold (with thermal growth offsets per OEM)
- **Hot alignment check** after first run-in and thermal stabilization — most refineries require this and a signed alignment report

**Heat exchangers** (shell and tube): set on saddle supports; one saddle fixed, the other on a slide plate (graphite or PTFE) to accommodate thermal growth. Channel-end orientation matters — confirm nozzle orientation before lifting.

**Vessels and columns:** Set plumb to ≤1:1000 (vertical columns). Levelness of the top platform matters for tray installation later. Internal tray installation, demister pads, and packing are usually a separate scope but the GC owns access (manway scaffolding) and cleanliness (white-glove).

**Tanks** (API 650): erected ring-by-ring or jacked from the top. Roundness, plumbness, and weld peaking are checked per API 650 §7. Floor welds get vacuum-box testing; shell welds get RT/UT per the spec.

### 1.7 Mechanical HVAC: Industrial Ventilation, Exhaust, Dust Collection, Cooling Towers

Industrial HVAC is not commercial HVAC. The drivers are **process heat rejection, contaminant control, and personnel protection**, not occupant comfort.

- **General ventilation:** Sized by air changes per hour (ACH) — 6 ACH typical for warehouse, 20+ ACH for battery rooms, 12 ACH minimum for indoor process areas with hydrocarbon potential.
- **Local exhaust ventilation (LEV):** Capture velocities per ACGIH Industrial Ventilation Manual. Welding booths 100 fpm at the source, grinding ≥200 fpm.
- **Dust collection:** Cyclone + baghouse for combustible dust (NFPA 652/654/664/61) with explosion venting, isolation valves, and rotary airlocks. The dust hazard analysis (DHA) drives the design — read it before installing.
- **Cooling towers:** Mechanical-draft (induced or forced). Field assembly is a major lift (FRP or concrete basin, structural framing, fill packs, drift eliminators, fan stack). Pay attention to plumb on the fan stack and torque on fan blades; an out-of-balance fan will destroy a gearbox in months.
- **Exhaust stacks:** Air permit dictates discharge height, velocity, and monitoring (CEMS — continuous emissions monitoring). Coordinate stack platform access for source-testing crews.

### 1.8 Insulation

Three reasons to insulate: **energy conservation, process control (heat retention or cold preservation), personnel protection (PP — surfaces above 140 °F).**

- **Hot service:** Mineral wool (≤1200 °F), calcium silicate (≤1700 °F), perlite (cryogenic and hot), ceramic fiber (≥1800 °F). Aluminum jacket outdoors; stainless jacket on saltwater coast.
- **Cold service:** Cellular glass (Foamglas), polyurethane foam, elastomeric (Armaflex). Vapor barrier is critical — moisture ingress destroys cold insulation in months.
- **Personnel protection cages** are an option in lieu of full insulation around man-access zones, but most owners prefer full insulation for energy reasons.

Insulation goes **after** hydrotest and **after** final paint. CUI (corrosion under insulation) is the dominant maintenance issue in refineries — keep insulation off until paint is fully cured, and verify jacket sealing at every termination.

### 1.9 Valves: Types and Applications

| Type | Action | Use |
|---|---|---|
| Gate | On/off, full bore | Block valves on liquid lines, low pressure drop |
| Globe | Throttling | Manual flow control, bypass lines |
| Ball | On/off, quarter-turn | Block valves, instrument air, utilities |
| Butterfly | On/off or throttling | Large diameters, water, low-pressure air |
| Check | Backflow prevention | Pump discharge, compressor discharge — swing, lift, dual-plate (wafer), tilting disc |
| Plug | On/off, quarter-turn | Sludge, slurry, sour service |
| Diaphragm | On/off, throttling | Sanitary, corrosive, slurry |
| Control valve | Modulating | Flow/pressure/temperature control under DCS command; globe or rotary body, pneumatic actuator |
| PSV/PRV | Pressure relief | Code-stamped, set per relief calc, sealed |

**Field execution notes:** Install gate valves with stems vertical or 45° off vertical (never stem-down). Check valves must have the arrow oriented with flow — sounds obvious, gets installed backwards on every project. Control valves go in **after** the line is flushed; protect them during construction with spool pieces or strainers in the line. PSVs must be set, tested, and tagged by a certified valve shop — do not crack the seal in the field.

### 1.10 P&ID Interpretation for Construction Crews

The P&ID (per ISA S5.1) is the contract document. Crews who learn to read it work faster and make fewer mistakes than crews who only follow isos.

**What a P&ID tells you:**
- Line number (typ: "6"-PG-150-CS-1A" = 6" pipe, process gas, Class 150, carbon steel, line 1A)
- Equipment tags and elevations
- Instrument bubbles (FT, PT, TT, LT for transmitters; FIC, PIC, TIC, LIC for controllers)
- Control loop function (modulating, on/off, ESD)
- Insulation (H = hot, C = cold, PP = personnel protection)
- Heat-tracing requirements (electric, steam)
- Set points, alarms, trip points (on the bubble or on a separate spec sheet)

**Isos and GADs build from the P&ID.** The iso shows three-dimensional routing for fabrication. The GAD (General Arrangement Drawing) shows where it sits on the pipe rack. If a line on the iso conflicts with a P&ID line class, **the P&ID wins** — it is the source of truth for service, line class, and instrumentation.

---

## 2. Electrical Systems on Industrial Projects

### 2.1 Power Distribution

Industrial power comes in at **medium voltage** (4.16 kV, 13.8 kV, 34.5 kV, 69 kV) from the utility, steps down through transformers, and distributes at **low voltage** (480Y/277 V is the workhorse; 600 V in Canada; 208Y/120 V for receptacles and lighting).

**Typical hierarchy:**

```
Utility feed → Main MV switchgear → Power transformer (e.g., 13.8 kV / 480 V) →
LV switchgear → MCC(s) → motor branch circuits + feeder breakers → panelboards → receptacles/lighting
```

- **MV switchgear:** Metal-clad, draw-out breakers (vacuum or SF₆), arc-resistant construction increasingly standard. Installed in dedicated electrical rooms, kept positive-pressure-ventilated, with redundant cooling.
- **Power transformers:** Oil-filled (outdoor, with secondary containment per NEC 450 / SPCC) or dry-type cast-resin (indoor, no oil). Bushings, lightning arresters, sudden-pressure relay, Buchholz relay, and tap changer all live in the GC's commissioning checklist.
- **LV switchgear:** Air circuit breakers, fixed or draw-out. Bussed at 65 kAIC or 100 kAIC; coordinate with the arc-flash study.
- **MCCs:** Drawer-type "buckets" — each bucket houses a starter (FVNR, RVSS, VFD), an overload, and control. NEMA Type 1, 3R (outdoor), or 12 (dust-tight). Sized by horizontal bus ampacity (600 A, 800 A, 1200 A, 1600 A, 2000 A typical) and vertical bus.
- **Bus duct (busway):** Used for short, high-current feeders between transformer and switchgear, or between switchgear and large MCCs. Plug-in busway is used overhead in large plants for tap-off to loads. Installation requires careful joint torquing (per manufacturer) and megger testing of each section.
- **Panelboards:** Branch distribution to lighting, receptacles, instrument power. 42-circuit max under NEC unless a "lighting and appliance panelboard" exception applies; modern NEC has relaxed this.

### 2.2 Conduit Systems

Industrial wiring methods are selected by **area classification, environmental exposure, and mechanical protection** — not by cost alone.

| Conduit | Use |
|---|---|
| **RMC** (Rigid Metallic, threaded steel) | Hazardous areas, refineries, chemical plants, anywhere mechanical damage is likely. Threaded joints with explosion-proof fittings (Crouse-Hinds, Appleton). |
| **IMC** (Intermediate Metallic) | Lighter than RMC, same threading, allowed in most of the same locations. Cost compromise. |
| **EMT** (Electrical Metallic Tubing) | Indoor general-use, non-hazardous, non-corrosive. Compression or set-screw fittings (set-screw not allowed in wet locations under most specs). |
| **PVC** (Schedule 40 / 80) | Underground duct banks, corrosive environments, wet locations. Sch 80 above grade (impact rating); Sch 40 in concrete encasement. |
| **PVC-coated RMC** ("Plasti-Bond," "Ocal," "Rob-Roy") | Highly corrosive areas — pulp mills, chlorine plants, fertilizer. RMC core for mechanical protection + PVC jacket for corrosion. |
| **Flexible (LFNC, LFMC)** | Final connection to motors and vibrating equipment — limited length per NEC 350/356, usually ≤6 ft. |
| **Cable tray** | The dominant industrial method — see §2.3. |

**Field rules:** Conduit ≥3/4" minimum in most industrial specs (1/2" not allowed). Bends limited to 360° between pulls (NEC 344.26 / 358.26). Support spacing per NEC 344.30. Expansion fittings in long straight runs (rule of thumb: 1 fitting per 100 ft, or per the spec). For hazardous areas, seal fittings (EYS, EYD) within 18" of every enclosure entering/leaving the classified area per NEC 501.15.

### 2.3 Wire and Cable, Cable Tray

Industrial wiring is rarely pulled in conduit end-to-end — it travels in **cable tray** above the pipe rack and drops to equipment in short conduit "stubs."

**Conductor sizing:** NEC Table 310.16 (in conduit / cable) and 310.17 (free air) give ampacities. Industrial circuits start at 90 °C insulation (THHN/THWN-2, XHHW-2) and derate per ambient and conduit fill. Voltage drop is sized separately — keep total drop ≤3% feeders, ≤5% combined feeder + branch (NEC 210.19 Informational Note).

**Cable construction:**
- **THHN/THWN-2:** Building wire, dry/wet, 90 °C. Default for branch circuits in conduit.
- **XHPE (XLPE):** Cross-linked polyethylene insulation; common in cable tray cables.
- **TC-ER (tray cable, exposed run rated):** Multi-conductor cable approved for direct cable tray use without a jacketed inner conduit. Default for motor feeders and control circuits in industrial.
- **MC cable:** Metal-clad armored cable. Acceptable in some industrial specs; uncommon in heavy process.
- **MV cable** (5 kV, 15 kV, 35 kV): Triplexed or single-conductor with EPR or XLPE insulation, copper tape shield, PVC or CPE jacket. Cable terminations are made with cold-shrink or heat-shrink kits — every termination is **a separate qualified procedure with a certified installer**.

**Cable tray** (NEC Article 392):
- Ladder, ventilated trough, and solid bottom. Ladder is dominant in industrial.
- Minimum single-conductor size in tray: **1/0 AWG.** Smaller conductors go in multi-conductor cable.
- Single conductors 1/0–4/0 in uncovered tray: ampacity = 65% of Table 310.17; 600 kcmil+ = 75%.
- Conductors in random fill: derate per 392.80(A).
- Support spacing per manufacturer NEMA rating (NEMA VE-1); typically 12 ft for aluminum ladder tray.
- Bonding: every joint, with bonding jumpers; tray itself can serve as EGC if rated and marked.

**Field execution:** Tray runs are surveyed and hung first, then cables pulled in **layers** (power on top, control middle, instrument bottom — or instrument on its own tray entirely). Pulling tension is calculated for long runs; lubrication and pulling-eye are required for heavy MV pulls. Every pull gets a **megger test** before and after.

### 2.4 Grounding and Bonding

Grounding (NEC Article 250) does two distinct things: **provides a path for fault current back to the source** (so the breaker trips) and **bonds metal parts to limit voltage to ground** (so people don't get shocked).

**Grounding electrode system** at an industrial facility typically includes:
- Building steel (bonded at the column base)
- Concrete-encased electrode ("Ufer ground" — 20 ft of #4 rebar or #4 bare copper in the foundation footing)
- Ground ring (#2/0 or larger bare copper, ≥30" deep, around the building)
- Ground rods (8 ft × 5/8" copper-clad, ≥6 ft apart) — at substation corners, lightning protection downconductors, fuel tanks
- All bonded together at the **main grounding electrode**; resistance to earth typically ≤5 Ω (per spec; NEC §250.53 allows 25 Ω from a single rod but most industrial specs are tighter)

**Equipment grounding conductor (EGC):** Sized per NEC Table 250.122 based on the upstream OCPD. In tray systems, often a separate dedicated green conductor in addition to the tray ground.

**Lightning protection** (NFPA 780): Air terminals, downconductors, ground ring, surge protection at the service. Required by spec for tank farms, control rooms, and any structure with electronic systems.

**Static grounding** for tank loading, drum filling, and IBC dispensing: dedicated bonding clamps to verified ground point. Critical in flammable service — the GC owns verification that bonding points exist and are tested.

### 2.5 Hazardous Locations (NEC Article 500 / 505)

Industrial facilities almost always have **classified areas** — places where flammable gas/vapor, combustible dust, or fibers might be present.

**Class / Division (legacy US system, NEC 500–504):**

| Class | Material | Division 1 | Division 2 |
|---|---|---|---|
| I | Flammable gases/vapors | Present during normal operation | Present only abnormally |
| II | Combustible dusts | Suspended in normal operation | Only during accident/upset |
| III | Easily ignitable fibers/flyings | (Division split deprecated in newer code) | |

**Groups** refine the material: A (acetylene), B (hydrogen), C (ethylene), D (propane/most hydrocarbons) for Class I; E (metal dust), F (carbon dust), G (grain/flour) for Class II.

**Zone system (NEC 505, IEC-aligned):** Zone 0 (continuous), Zone 1 (likely under normal), Zone 2 (abnormal only). Increasingly the global standard; Owner-specified per project.

**Equipment protection methods:** Explosion-proof (XP, contains internal ignition), intrinsically safe (IS, limits energy below ignition threshold), purged/pressurized (Type X, Y, Z per NFPA 496), increased safety (Ex e), encapsulation (Ex m). Each method has its own installation rules — **seals, conduit type, drains, and gland selection** all change by method.

**Field execution rules:**
- Seal-offs at every classified-area boundary per NEC 501.15
- Drain seals at low points where condensation collects
- No flexible conduit in Class I Div 1 except as specifically allowed (sealed flex with rated fitting)
- Cover plates must be code-listed; ordinary cover plates are not allowed
- Every fixture, J-box, motor, and disconnect must be **rated for the area's Class/Div/Group** — and verified with the nameplate before installation. Inspectors photograph nameplates.
- Documentation: an **area classification drawing** is part of the design package; reference it constantly.

### 2.6 Motors, VFDs, Soft Starters

**Motor connections:** Three-phase induction motors are wired Wye or Delta per the nameplate. Lead numbering follows NEMA MG-1: 6-lead (single-voltage Y or Δ), 9-lead (dual-voltage Y/Δ), 12-lead (dual-voltage Y/Δ with both reduced-voltage start options).

**VFD (Variable Frequency Drive):**
- Rectifier + DC bus + IGBT inverter → variable V/Hz output
- **VFD cable** (XLPE, symmetrical grounding conductors, foil + copper-braid shield) is required to limit common-mode currents and bearing currents. Standard THHN is **not** acceptable.
- Cable length limits to motor (per drive vendor; typically ≤300 ft without dV/dt filter, longer with output reactor or sine filter)
- Bearing protection: shaft grounding ring or insulated NDE bearing for motors ≥100 HP on VFDs
- Cable shield bonded at **both ends** (360° gland)

**Soft starters (RVSS):** SCR-based reduced-voltage starter. Cheaper than VFD when speed control is not needed (large pumps, fans starting). Bypass contactor closes after ramp.

**Motor commissioning:** Megger to ground (>100 MΩ on a clean new motor; ≥1 MΩ/kV + 1 minimum), winding resistance balance (<5% phase-to-phase), rotation verification (bumped uncoupled, then verified coupled), thermal protection wired and tested.

### 2.7 Instrument and Control Wiring

Instrument signals are **low-energy, low-voltage** and live in a different cable world from power.

**4–20 mA loop:** The industrial workhorse. Two-wire transmitter (powered by the loop), single-pair twisted-shielded cable (typ. 18 AWG), shield grounded at the **control room end only** (one-point ground prevents shield current loops). The DCS provides 24 VDC; the transmitter regulates current to indicate process value (4 mA = 0%, 20 mA = 100%).

**Thermocouple wiring:** Use **extension wire of the same alloy as the thermocouple** (Type K, J, T, E, etc.). Copper wire introduces a cold-junction error. Polarity matters (red is negative in US thermocouple color codes — opposite of power wiring). Shielded twisted pair.

**RTD wiring:** Three-wire RTD is the industrial default (compensates for lead resistance). Four-wire for high-accuracy. Copper instrumentation cable, shielded.

**Cable tray segregation:** Most owner specs require separate cable trays (or dividers) for:
- 480 V power and above
- 120 V control
- 24 VDC instrument
- Intrinsically safe (IS) — light blue jacket, **physically separated** from non-IS

**Junction boxes and marshalling:** Field instruments terminate at local JBs (often FRP or stainless, NEMA 4X). Multi-pair "home-run" cables go from JBs to the marshalling cabinet in the control room. Marshalling terminates at the DCS I/O.

**Loop check:** Pre-commissioning, every loop is **simulated end-to-end** — inject a known value at the field transmitter, verify on the DCS screen, exercise the control output to the valve, verify positioner feedback. Documented on a loop sheet, signed by I&E QC and the commissioning engineer.

### 2.8 Lighting

Industrial lighting design (IES RP-7) is driven by foot-candle targets at the work plane (typically 20 fc walkways, 30–50 fc operating, 100 fc precision tasks), and by fixture rating to the area class.

- **General area:** Industrial LED high-bays, vapor-tight LEDs.
- **Hazardous areas:** Listed Class I Div 1 or Div 2 LED fixtures with rated globes; no fluorescent in Div 1.
- **Emergency / egress** (NFPA 101, NEC 700): 90-min battery backup or generator-fed; minimum 1 fc along path of egress; activated within 10 seconds of normal loss.
- **Obstruction lighting** for tall stacks/towers per FAA AC 70/7460.

### 2.9 Arc Flash Studies and NFPA 70E

Every industrial facility must have a **current arc flash study** per NFPA 70E. The study calculates **incident energy** (cal/cm²) at each work location and the **arc flash boundary** (distance at which IE = 1.2 cal/cm²).

**Two NFPA 70E methods:**
1. **Incident Energy Analysis** (130.5(G)) — IEEE 1584 calc or equivalent software. Produces a label with calculated cal/cm², working distance, AFB, and required PPE arc rating.
2. **PPE Category Table** (130.7(C)(15)) — task-based lookup, limited to listed equipment parameters (e.g., ≤25 kA, ≤2 cycles clearing).

**PPE categories:**

| Category | Min arc rating | Typical use |
|---|---|---|
| 1 | 4 cal/cm² | Lower-energy panels |
| 2 | 8 cal/cm² | Most MCC buckets, 480 V panels |
| 3 | 25 cal/cm² | Large switchgear, MCCs at the line side |
| 4 | 40 cal/cm² | Service entrance, MV gear |
| ">40" (no category) | Engineer-specified | High IE — typically requires de-energization |

**Field execution:**
- Every panel gets a **label**: nominal voltage, AFB, incident energy at working distance, required PPE level, shock approach boundaries.
- Energized work requires an **energized electrical work permit** (EEWP) — owner signs.
- "De-energized" requires **LOTO** with verification at the point of work using a tested meter.
- The GC owns: ensuring labels are installed before energization, ensuring electricians on site have appropriate arc-rated clothing on, and pushing back when the owner asks for "just a quick check" on live gear.

### 2.10 Grounding Electrode Systems for Industrial Facilities

Beyond §2.4 essentials, industrial facilities typically engineer the grounding system to limit **step and touch potentials** at substations (per IEEE 80) and **soil resistivity** to a target. Design inputs: Wenner four-pin soil-resistivity test, available fault current, clearing time. Design output: grid layout (ground ring with crossing conductors at 10–20 ft spacing), rod count, and resistance target.

Field execution checks:
- Cadweld (exothermic) connections at every below-grade splice; mechanical only above grade
- Fall-of-potential test (3-pin) after installation to verify ≤ design resistance
- Photographic record of every below-grade connection before backfill — this is the GC's only proof the work was done

---

## 3. Installation Sequences and Field Coordination

### 3.1 Typical Industrial Construction Sequence

```
Site prep & geotech
  ↓
Civil / structural foundations (footings, piers, equipment foundations, slabs)
  ↓
Underground (storm, sanitary, process underground, fire water, electrical duct banks) — DO THIS BEFORE SLAB
  ↓
Structural steel erection (racks, mezzanines, equipment supports)
  ↓
Major equipment set (cranes drop tanks, columns, compressors — schedule-critical)
  ↓
Mechanical piping (spool delivery, fit-up, weld-out, NDE)
  ↓
Electrical (cable tray, conduit, gear installation, wire pulling)
  ↓
Instrumentation (transmitters, JBs, control wiring, loop checks)
  ↓
Insulation, paint, fireproofing
  ↓
Pressure testing, flushing, cleaning
  ↓
Commissioning (energize, run-in, performance test)
  ↓
Turnover (mechanical completion, then operational acceptance)
```

**Critical path principle:** Equipment with long lead times (transformers, compressors, custom vessels) is set as soon as the foundation cures. The pipe rack is built around the equipment. **The GC's master schedule must protect the equipment-set milestones above all else** — every other discipline can absorb slip; a missed compressor lift cascades for months.

### 3.2 Underground Coordination

Underground is where projects bleed money. Three to five trades compete for the same trench depth, and rework after the slab pour is brutal.

**Sequence within underground:**
1. Storm and sanitary (deepest, gravity-flow, set the elevations everything else works around)
2. Fire water (large diameter, high pressure, often ductile iron)
3. Process underground (chemical sewer, oily water)
4. Electrical duct banks (PVC-encased-in-concrete, 24–36" cover minimum, "red dye" concrete for ID)
5. Communications / fiber

**Duct bank specifics:**
- Schedule 40 PVC ducts (or fiberglass for high-temp) on spacers every 5–8 ft
- Concrete encasement minimum 3" all sides, often dyed red
- Pull strings in every conduit
- Megger and "mandrel" (proof of bore) test before backfill
- As-built **before** the slab pours over it — once it's under concrete, it's a future hot job

**Trench safety:** OSHA 1926 Subpart P. Anything over 4 ft deep needs protective system (sloping, shoring, shielding). The GC owns this.

### 3.3 Mechanical-Electrical Interface

The interface that costs the most rework is **the motor terminal box**. The mechanical crew sets and aligns the pump/motor; the electrical crew pulls cable and lands leads. Coordination issues:

- **Lead length:** Electrical needs ~18" of slack in the motor JB. Mechanical sometimes installs the JB rotated wrong or removes it for clearance.
- **Conduit hub orientation:** Confirm before cable pull — wrong orientation = hard 90° in a tiny space.
- **Grounding:** Motor frame ground lug bonded to EGC. Verify after termination.
- **Heater connection:** Space heaters in large motors are wired separately (often 120 V); easy to miss.
- **RTD/thermistor connections:** Bearing and winding temperature sensors land in a separate JB; usually 6–12 conductors.
- **Rotation check:** After termination, bumped uncoupled. If rotation is wrong, swap any two phases at the **starter** (not at the motor) so subsequent motor swaps don't need re-rotation.

**MCC wiring to field devices:**
- Power feeder from MCC bucket to motor (in tray, then conduit stub)
- Control wiring from bucket to local Start/Stop station and back (usually 14 AWG, often in TC-ER or in conduit)
- Status wiring back from local devices (run feedback, ammeter, emergency stop)
- Increasingly, all of the above is collapsed into a **fieldbus** (Profibus, EtherNet/IP, DeviceNet) — the bucket has an intelligent overload (Allen-Bradley E300, Siemens Sirius) and one fieldbus cable carries everything.

### 3.4 Instrument Installation

Instruments are the last things installed, the first things damaged, and the highest-precision items on the site.

**Sequence:**
1. Install root valves and process taps during piping (transmitter not yet mounted)
2. Install stanchions, brackets, and JBs after piping is hydrotested
3. Install transmitters and field elements **after** flushing/blowing is complete
4. Install impulse tubing (typically 1/2" 316 SS with compression fittings) — slope correctly (1:10 toward transmitter for liquid, 1:10 away from transmitter for gas/steam)
5. Connect signal cable from JB to transmitter
6. Loop check (see §2.7)

**Common field instruments:**
- **Pressure (PT/PIT):** Diaphragm seal or direct-mount; impulse tubing with manifold (3-valve or 5-valve)
- **Differential pressure (DPT):** Used for flow (orifice plates, venturis), level (DP across a tank), and filter ΔP. 5-valve manifold standard.
- **Temperature (TT):** Thermowell installed during piping (it's a process penetration); RTD or TC inserted at instrumentation phase.
- **Level (LT):** Guided-wave radar (modern default), DP-cell, displacer (legacy), ultrasonic.
- **Flow (FT):** Coriolis (high-accuracy, expensive), magnetic (conductive liquids), vortex, orifice + DP.
- **Analyzers:** pH, conductivity, gas chromatograph, oxygen — typically in shelter buildings with sample conditioning systems. Their own discipline.

### 3.5 Working with Owner's Engineers and Third-Party Inspectors

The GC is the choke point between subcontractors and owner/AI scrutiny. Mishandling these relationships is more expensive than mishandling the work.

**Owner's engineers (typically resident on a major project):**
- Process engineer — owns the P&ID; deviations need a process MoC
- Mechanical engineer — owns piping, equipment, vessels; signs spec deviations
- Electrical engineer — owns SLDs, coordination, area classification
- I&C engineer — owns loop sheets, DCS configuration, alarm rationalization
- Civil/structural engineer — owns foundations, structural deviations
- Project engineer / construction manager — the daily interface

**Third-party inspectors:**
- **Authorized Inspector (AI)** for code piping/vessels — signs U-1 forms, witnesses hydros
- **NDE Level III** — reviews NDE procedures, signs off on radiograph interpretation
- **Coatings inspector** (NACE Level 2/3) — witnesses surface prep and DFT
- **Geotech inspector** — witnesses soil compaction, concrete pours, rebar inspection
- **Welding inspector (CWI per AWS QC1)** — witnesses fit-ups, monitors WPS compliance

**GC operating principles:**
- **Give inspectors advance notice** of hold points (usually 24–48 hr). Failure to notify = work redone.
- **Maintain a hold-point register** — every test, every weld inspection, every coating DFT. Cross-reference to the test pack.
- **Photographs of everything before it gets covered** — concrete-encased rebar, before-backfill underground, behind-wall conduit, foundation anchor bolts.
- **A daily turnover log** that captures: punch items raised, RFIs in flight, MoC items pending, NCRs (non-conformance reports) open. This is what gets reviewed at the weekly progress meeting and what protects the GC during change-order disputes.
- **Speak the inspector's language.** An AI cares about the U-1 and the welder log. A NACE inspector cares about the WFT/DFT and the holiday test. Bringing them the right document the first time builds trust that pays back later when a marginal call goes your way.

---

## Quick-Reference Checklists

### Mechanical Pre-Energization
- [ ] All welds VT'd, NDE complete per ITP, repairs cleared
- [ ] PWHT records (if applicable) attached to test pack
- [ ] Hydro/pneumatic test signed by AI and owner
- [ ] Flushing complete; strainers cleaned; temporary spools removed
- [ ] Control valves re-installed; PSVs installed with seals intact
- [ ] Insulation and personnel protection in place
- [ ] As-built P&IDs marked up

### Electrical Pre-Energization
- [ ] Megger test results filed (all feeders, all motors)
- [ ] Hi-pot test on MV cable (per IEEE 400)
- [ ] Phase rotation verified at gear and at each motor (uncoupled bump)
- [ ] Grounding system tested (fall-of-potential)
- [ ] Arc flash labels installed at every applicable enclosure
- [ ] Protective relay settings loaded and tested
- [ ] LOTO procedures in place; energization permit signed
- [ ] All hazardous-area equipment nameplates verified against area classification drawing

### Instrumentation Pre-Commissioning
- [ ] Loop sheets signed for every loop
- [ ] Transmitters calibrated (cert on file)
- [ ] Impulse tubing leak-tested
- [ ] Control valves stroked; feedback verified
- [ ] DCS graphics validated against P&ID
- [ ] Alarm and trip points loaded and tested

---

## Sources

**Mechanical / Piping**

- ASME B31.3 (Process Piping) vs. B31.1 (Power Piping) overview — [EPCLand](https://epcland.com/asme-b31-1-vs-b31-3-comparison/) and [Alek VS](https://www.alekvs.com/asme-b31-3-vs-asme-b31-1-whats-the-difference/)
- Pipe fabrication tolerances under ASME B31.3 — [Piping World](https://www.piping-world.com/pipe-fabrication-tolerances)
- ASME B31.3 weld acceptance criteria (Table 341.3.2) — [NDT.net B31.3 PDF](https://www.ndt.net/forum/files/rt-asmeb31.3-withoutsecure.pdf) and [Welding & NDT](https://www.weldingandndt.com/acceptance-criteria-for-weld-defects/)
- Random radiography under B31.3 — [The Fabricator](https://www.thefabricator.com/thewelder/article/testingmeasuring/random-radiography)
- ASME B31.3 leak testing — [Piping World leak testing guide](https://www.piping-world.com/asme-b31-3-leak-testing-requirements-overview), [EPCLand hydrotest](https://epcland.com/piping-hydrostatic-test-procedure-asme-b31-3/), and [Petersen Products](https://www.petersenproducts.com/articles/asme-hydrostatic-test-requirements.html)
- Industrial pump installation, alignment and grouting — [Chemitek](https://www.chemitek.co.in/blogs/industrial-pump-installation-guide), [Michael Smith Engineers](https://www.michael-smith-engineers.co.uk/resources/useful-info/pump-alignment), and [Ludeca laser alignment](https://ludeca.com/categories/shaft-alignment/)
- Soleplate vs. baseplate grouting — [Epoxy Resin Factory](https://epoxyresinfactory.com/blog/grouting-soleplate-baseplate-turbo-machinery)
- P&ID symbols and interpretation — [Lucidchart P&ID guide](https://www.lucidchart.com/pages/tutorial/p-and-id), [Vista Projects symbol library](https://www.vistaprojects.com/common-pid-symbols/), and [Wikipedia P&ID](https://en.wikipedia.org/wiki/Piping_and_instrumentation_diagram)
- P&ID vs. isometric drawings — [Elegrow](https://elegrow.com/the-major-differences-between-pid-piping-and-instrumentation-diagram-and-isometric-drawings/)

**Electrical**

- NEC Article 500 hazardous locations — [IAEI Magazine](https://iaeimagazine.org/2014/novemberdecember-2014/hazardous-classified-locations-nec-articles-500-through-517/), [EC&M](https://www.ecmweb.com/national-electrical-code/article/20897567/hazardous-locations-and-the-nec), [Delta Wye Electric](https://deltawye.com/nec-requirements-for-hazardous-locations/), and [Wikipedia Electrical equipment in hazardous areas](https://en.wikipedia.org/wiki/Electrical_equipment_in_hazardous_areas)
- Class I Div 2 and NEC 500 — [JCE Group](https://jcegroup.com/understanding-class-i-division-2-hazardous-locations-and-nec-500-compliance/)
- Motor control centers — [JDI Industrial](https://jdiindustrial.com/motor-control-center-installations-what-they-are-how-jdi-installs/), [Eaton MCC design guide](https://www.eaton.com/content/dam/eaton/products/design-guides---consultant-audience/eaton-low-voltage-mcc-design-guide-dg043001en.pdf), and [Wikipedia MCC](https://en.wikipedia.org/wiki/Motor_control_center)
- NFPA 70E arc flash methods and PPE categories — [NFPA blog](https://www.nfpa.org/news-blogs-and-articles/blogs/2022/01/14/a-better-understanding-of-nfpa-70e-correctly-using-the-incident-energy-analysis-and-arc-flash-ppe), [Tyndale USA PPE Category Method](https://tyndaleusa.com/nfpa-70e/130-5-arc-flash-ppe-table-method/), [OSHA 4472](https://www.osha.gov/sites/default/files/publications/OSHA4472.pdf), and the [Arc Flash 101 lookup table](https://arcflash101.webflow.io/lookup-tables/table-130-7-c-15-a-ppe-categories-for-ac-systems)
- NEC 392 cable tray ampacity and sizing — [Nassau National Cable Article 392 primer](https://nassaunationalcable.com/blogs/blog/explaining-nec-article-392-on-cable-trays), [ExpertCE 392.80 calc](https://expertce.com/learn-articles/cable-tray-conductor-ampacity-calculation-nec-392-80/), and [ECMag tray ampacity](https://www.ecmweb.com/magazine/articles/article-detail/ampacity-calculations-cable-tray-installations-can-be-tricky-part-2)
- Underground duct banks — [Baker Construction](https://bakerconstruction.com/industrial-services/underground-utilities-and-duct-banks/), [Champion Fiberglass](https://championfiberglass.com/what-to-consider-for-underground-duct-bank-runs/), [Utility Pipe Supply](https://utilitypipesupply.com/blogs/news/what-is-a-duct-bank), and the [Northwestern duct bank spec](https://www.northwestern.edu/facilities/docs/construction/design_guidelines/26_electrical/NU_26%200543%20-%20UNDERGROUND%20DUCTS%20AND%20RACEWAYS%20FOR%20ELECTRICAL%20SYSTEMS.pdf)

**Instrumentation**

- Thermocouple / RTD to 4–20 mA practice — [PR Electronics knowledge library](https://www.prelectronics.com/support/pr-knowledge-library/tips-and-tricks/advantages-of-converting-rtd-and-thermocouple-signals-to-4-20-ma-current/), [Datexel signal splitters](https://www.datexel.com/choosing-between-4-20mA-rtd-thermocouple-signal-splitters.html), and [Anixter Wire Wisdom](https://www.anixter.com/en_us/resources/literature/wire-wisdom/thermocouple-and-rtd-wire.html)
- 3-wire RTD wiring and shielding — [Industrial Monitor Direct](https://industrialmonitordirect.com/blogs/knowledgebase/3-wire-rtd-wiring-shielded-cable-requirements-and-installation)

**General**

- LANL ASME B31.3 Process Piping Guide (engineering standards) — [LANL EngStandards PDF](https://engstandards.lanl.gov/esm/pressure_safety/Section%20REF-3-R0.pdf)
- EIGA pressure-testing guideline for field-installed piping — [EIGA Doc 254](https://www.eiga.eu/uploads/documents/DOC254.pdf)

---

> **Confidence note:** Code numbers and procedural specifics (B31.3 tolerance values, NEC ampacity factors, NFPA 70E PPE category thresholds) reflect current editions as of writing. Always verify against the edition adopted in the project's contract specification — owners frequently cite a specific year (e.g., "B31.3-2020"), and acceptance criteria do shift between editions. The execution sequences and field-coordination guidance are industry-consensus practice and do not vary by code edition.
