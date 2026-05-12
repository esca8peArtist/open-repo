---
title: "Residential Solar PV and Battery Storage for the General Contractor"
module: 27
discipline: ["solar", "battery-storage", "electrical", "NEM", "Title24"]
audience: "Residential GC coordinating or managing solar and battery installations in California"
status: "reference"
tags: [career-training, solar, battery-storage, NEM3, Title24, California, Enphase, Tesla-Powerwall, NEC690, electrical]
created: 2026-05-12
---

# Residential Solar PV and Battery Storage for the General Contractor

> Solar PV is **mandatory** on every new single-family home and most low-rise multifamily projects in California. As a GC, you do not need to be a solar designer, but you do need to (a) rough-in correctly so the C-10/C-46 sub does not tear out your work, (b) coordinate the roofer, framer, electrician, and solar installer on a shared layout, (c) advise the homeowner accurately on cost, payback, and battery decisions under NEM 3.0, and (d) close out the utility interconnection without delaying CofO.

---

## 1. California Solar Mandates and Incentives

### 1.1 Title 24 — The Solar Mandate

California is the only state that **mandates** rooftop solar on new homes. The mandate sits inside **Title 24, Part 6 (Building Energy Efficiency Standards)**, administered by the California Energy Commission (CEC). It is enforced at the local building department through plan-check and the CF1R/CF2R/CF3R documents prepared by your Title 24 energy consultant.

| Code Cycle | Effective | What It Did |
|---|---|---|
| **2019 Title 24** | Jan 1, 2020 | First-in-nation solar PV mandate for new single-family homes and low-rise multifamily (≤3 stories). Sized by climate zone × conditioned floor area. |
| **2022 Title 24** | Jan 1, 2023 | Extended PV + battery storage requirements to **high-rise multifamily** and most **nonresidential** new construction. Added prescriptive **battery option** for low-rise residential (25% PV reduction if a JA12-compliant battery ≥7.5 kWh is installed). |
| **2025 Title 24** | Jan 1, 2026 | Tightens electrification and grid-harmonization provisions; PV/battery framework largely retained. Verify current edition in your jurisdiction at permit submittal. |

**Single-family and ADU (2022 code)**:
- Solar PV required on every new dwelling unit.
- PV sizing formula (prescriptive): **kWPV = (CFA × A) / 1000 + (NDwell × B)**, where CFA = conditioned floor area, NDwell = number of dwelling units, and A/B coefficients vary by climate zone (Table 150.1-C). Typical output: **2.5–4.5 kW** for a single-family home.
- Battery optional. If a JA12-listed battery ≥7.5 kWh is installed, PV may be reduced 25%.

**Low-rise multifamily (≤3 stories)**:
- Solar PV required. Same formula approach by climate zone.
- Battery storage option triggers 25% PV reduction.
- High-rise multifamily (4+ stories): both PV **and** battery are prescriptively required.

**Exceptions to the PV mandate** (Section 150.1(c)14):
1. **Insufficient solar access** — roof has <80 contiguous sf of effective solar zone after deducting shading from adjacent objects, vents, and equipment.
2. **Steep north-facing roof** — when the only available roof area faces north of east-west azimuth at steep pitch.
3. **Roof area too small** — effective solar zone is less than required by formula due to roof geometry, dormers, or required setbacks.
4. **All-electric or near-zero compliance path** — performance method may show equivalence without PV in limited cases.
5. **Solar-ready stub-out** — when an exception applies, the building must still be **solar-ready** (conduit, panel space, structural).

### 1.2 NEM 3.0 — The Net Billing Tariff (NBT)

The CPUC's December 2022 decision replaced NEM 2.0 with the **Net Billing Tariff** (commonly "NEM 3.0"), effective **April 15, 2023** for new interconnection applications submitted to PG&E, SCE, and SDG&E. Existing NEM 2.0 customers are grandfathered for 20 years from their PTO date.

| | NEM 2.0 (pre-Apr 2023) | NEM 3.0 / NBT (Apr 2023–) |
|---|---|---|
| **Export credit** | Full retail rate, ~$0.30–0.40/kWh | Avoided Cost Calculator (ACC); ~$0.04–0.08/kWh midday, higher at peak |
| **Credit value** | Symmetrical (kWh in = kWh out) | Asymmetrical $-based; export is small, import is full retail |
| **Annual true-up** | Yes | Yes; bill credits can roll month-to-month then settle |
| **Avg. midday export rate** | ~$0.32/kWh | **~$0.05/kWh** (PG&E summer 2025 ACC) |
| **Peak export rate** | ~$0.40/kWh | **~$2.00–3.00/kWh** during summer 4–9 pm peak events |
| **Lock-in period** | 20 yrs from PTO | **9 yrs** of ACC schedule locked at vintage year of PTO |
| **Economic logic** | Export = save → big systems | Self-consume → battery-driven sizing |

**What this means for the GC**:
- Solar-only payback under NEM 3.0 has stretched from ~6 years (NEM 2.0) to **9–12+ years**.
- Solar + battery payback under NEM 3.0 is **6–9 years** because the battery shifts midday production to evening peak hours when the home would otherwise pay $0.40–0.55/kWh retail rates.
- The economic message to clients: **"Battery makes the system pay back; solar alone no longer does as fast."**
- Vintage year matters. A 2026 PTO locks in the 2025 ACC schedule for 9 years. Pushing PTO past Dec 31 of a given year may matter if the next year's ACC schedule is lower.

### 1.3 Federal Investment Tax Credit (ITC)

Authorized under the **Inflation Reduction Act of 2022, IRC §25D** (residential) and **§48** (commercial/third-party-owned).

| Year | Residential ITC (§25D) |
|---|---|
| 2022–2032 | **30%** |
| 2033 | 26% |
| 2034 | 22% |
| 2035+ | 0% (unless extended) |

**What qualifies**:
- Solar panels, inverters, racking, wiring, labor, permitting, sales tax.
- **Battery storage** (≥3 kWh) qualifies as a standalone credit since 2023 — it no longer must be solar-charged.
- Roof structural reinforcement directly required for solar mounting may qualify; **general re-roof does not**.
- Reasonable installation costs.

**How it works**: Nonrefundable credit against the homeowner's federal income tax liability for the tax year the system was placed in service (PTO date is the conservative anchor). Unused credit carries forward.

**Documentation the GC should help collect**: itemized contractor invoice, manufacturer specs, PTO letter from utility, photos of completed installation. The homeowner's CPA files Form 5695.

**Note on third-party ownership**: If the system is leased or under a PPA, the third party claims the §48 ITC, not the homeowner.

### 1.4 SGIP — Self-Generation Incentive Program

CPUC-administered rebate for battery storage. **As of late 2025, the General Market, Equity, and Equity Resiliency budgets all closed Dec 31, 2025.** The only currently active pathway is the **Residential Solar and Storage Equity (RSSE) program** funded under AB 209, which is **waitlist-only** for households under 80% AMI.

| SGIP Track (historical / current) | Incentive | Status (May 2026) |
|---|---|---|
| General Market | ~$0.15/Wh | Closed |
| Equity | ~$0.85/Wh | Closed |
| Equity Resiliency (battery only) | **$1.10/Wh** | Closed; reopening uncertain |
| RSSE (AB 209, income-qualified) | $1,100/kWh storage + $3,100/kW solar | **Waitlist-only** |

For a typical 13.5 kWh Powerwall, the historical Equity Resiliency incentive was ~$15,000 — substantial. For market-rate clients in 2026, **do not promise SGIP funding** in your scope or proforma. Track [PG&E SGIP page](https://www.pge.com/en/save-energy-and-money/rebates-and-incentives/self-generation-incentive-program.html) and [CPUC SGIP](https://www.cpuc.ca.gov/industries-and-topics/electrical-energy/demand-side-management/self-generation-incentive-program/participating-in-self-generation-incentive-program-sgip) for reopen announcements.

### 1.5 Property Tax Exclusion

California Revenue & Taxation Code §73 excludes the value of an **active solar energy system** from property tax reassessment. Originally sunset 2024, extended by **SB 1340 (2022) through Jan 1, 2027**, with further extension expected. This applies to:
- The PV system itself.
- Storage installed at the same time as the PV.
- New construction: the value of the included PV is excluded from initial assessment.

Watch the sunset date if your project carries past 2026 close-out — current law as of May 2026 has the exclusion active through Dec 31, 2026 with legislative extension pending.

### 1.6 Other Incentives Worth Knowing

| Program | What It Is | Relevance |
|---|---|---|
| **DAC-SASH** | No-cost solar for low-income single-family homeowners in disadvantaged communities. | Administered by GRID Alternatives. Sub-eligible only. |
| **TECH Clean California** | Heat pump rebates that pair well with solar+battery proposals. | Bundle into all-electric remodel scope. |
| **LADWP Solar Rooftops** | Municipal utility incentives outside CPUC jurisdiction. | LADWP is **not** on NEM 3.0; still operates a successor program. Different rules entirely. |
| **SMUD, SDG&E, others** | Local POU rules vary. | Confirm utility before sizing. |

---

## 2. System Components — What the GC Needs to Know

### 2.1 Solar Panels (Modules)

Effectively 100% of new residential California installations use **monocrystalline silicon** modules. Polycrystalline is obsolete; thin-film (CdTe, CIGS) is utility-scale only.

| Tier | Brands (May 2026) | Power | Efficiency | Temp Coeff (Pmax) | Warranty |
|---|---|---|---|---|---|
| **Premium** | Maxeon (formerly SunPower), REC Alpha Pure-R, Panasonic EverVolt, Silfab Elite | 425–460 W | 21–23% | -0.27 to -0.29 %/°C | 25/40 yr |
| **Mainstream** | Q CELLS Q.PEAK DUO, Canadian Solar HiKu, Jinko Tiger Neo, Longi Hi-MO, Trina Vertex S+ | 400–445 W | 19.5–21% | -0.30 to -0.34 %/°C | 25 yr power |
| **Value** | Various Tier-2 | 380–420 W | 18–20% | -0.34 to -0.38 %/°C | 25 yr (verify mfr solvency) |

**What matters in California**:
- **Power class**: 400–460 W is the current standard. A 7 kW system = 16–18 panels at 430 W. Higher wattage means fewer panels = fewer roof penetrations = faster install.
- **Temperature coefficient**: Inland Empire/Central Valley summer roof temps hit 70–75°C. A panel rated -0.34%/°C loses ~17% of its rating from 25°C to 75°C. Premium panels at -0.27%/°C are noticeably better in hot zones.
- **Form factor**: Most current panels are ~67 × 45 inches × ~1.4 inches thick. Confirm with mfr before designing fascia/parapet conditions.
- **Aesthetics**: All-black (black frame + black backsheet) is the default for residential. Silver frame is for utility/commercial.

**SunPower bankruptcy note (relevant to old quotes)**: SunPower Corp filed Chapter 11 in August 2024. The Maxeon panel brand continues independently and is sold through new channel partners. The "SunPower" name is now mostly a service legacy; honor warranty service via Maxeon or Complete Solaria where applicable.

### 2.2 Inverters

The inverter converts panel DC to grid-frequency AC and is the single largest reliability variable in the system.

| Architecture | Example | How It Works | Pros | Cons |
|---|---|---|---|---|
| **Microinverter** | Enphase IQ8M/IQ8H/IQ8P, IQ8X | One per panel; AC trunk cable on roof | Per-panel MPPT, per-panel monitoring, no single point of failure, rapid shutdown built-in, no DC on roof, easy expansion | Higher per-watt cost; more components to fail (mitigated by 25-yr warranty) |
| **String inverter** | Fronius Primo, SMA Sunny Boy, GoodWe | One central inverter; DC strings from roof | Lowest cost, fewer parts | Shading on one panel reduces whole string; central failure = total outage; needs separate rapid shutdown device (e.g., Tigo) |
| **DC optimizer + string inverter** | SolarEdge HD-Wave + P-series optimizers | Per-panel optimizer; central inverter | Per-panel MPPT, central inverter is replaceable cheaply | Two failure modes; SolarEdge financial distress noted 2024–2025; verify warranty support |
| **Hybrid inverter** | Tesla Powerwall 3 (integrated PV inverter), Enphase IQ8 + IQ Battery, Franklin aPower | Solar inverter + battery inverter in one cabinet | DC-coupled efficiency, simpler install, single warranty | Locks you into one ecosystem |

**Dominant California residential choice (May 2026)**: Enphase IQ8 microinverters paired with Enphase IQ Battery 5P, **or** Tesla Powerwall 3 (which includes its own PV string inverter on the AC side and can drive panels via integrated MPPTs).

**Rapid shutdown compliance (NEC 690.12)**: All California rooftop systems must comply. Enphase microinverters are inherently compliant (no DC voltage on roof when AC is off). SolarEdge optimizers comply via the SafeDC feature. String inverters without optimizers require an added rapid shutdown initiator/transmitter.

### 2.3 Battery Storage

| Battery | Usable kWh | Continuous Power | Surge | Chemistry | Coupling | Notes |
|---|---|---|---|---|---|---|
| **Tesla Powerwall 3** | 13.5 | 11.5 kW (split-phase 240V) | 30 kW PV+battery startup | LFP | DC-coupled PV (up to 20 kW DC) + AC | Up to 4 units in parallel; integrated PV inverter (6 strings, 2 MPPTs); built-in Backup Gateway optional |
| **Tesla Powerwall 2** | 13.5 | 5 kW continuous, 7 kW peak | 7 kW | NMC | AC-coupled | Being phased out; refurb only as of 2026 |
| **Enphase IQ Battery 5P** | 5.0 | 3.84 kW per unit | 7.68 kW peak (10 sec) | LFP | AC-coupled | Modular: stack 1–4 (up to 20 kWh) per system; pairs natively with IQ8 microinverters via IQ System Controller 3 |
| **Enphase IQ Battery 10C** | 10.08 | 7.68 kW | 10.5 kW | LFP | AC-coupled | Newer SKU; combines two 5C modules |
| **Franklin WH aPower 2** | 15.0 | 10 kW | 22 kW | LFP | AC-coupled | UL 9540 listed; competitive $/kWh; works with most PV inverters |
| **FranklinWH aGate** | — | — | — | — | Controller | Required system controller for aPower |
| **LG Chem RESU Prime** | 9.6/16 | 5/7 kW | — | NMC | DC or AC | Declining presence post-recall history |
| **Generac PWRcell** | 9/12/15/18 | Up to 11 kW | — | NMC | DC | Pairs with Generac PV-Link optimizers |

**Chemistry — LFP vs NMC**:

| | LFP (LiFePO4) | NMC (NiMnCoO) |
|---|---|---|
| Cycle life | 6,000+ cycles to 80% | 3,000–4,000 cycles |
| Thermal runaway risk | Low (very stable) | Moderate |
| Energy density | Lower (bigger box) | Higher |
| Cost ($/kWh) | Now comparable | Now comparable |
| Resi market share 2026 | ~85% | ~15% (declining) |

LFP has effectively won the residential market on safety, cycle life, and recent cost parity. Spec LFP unless there is a specific reason not to.

**AC-coupled vs DC-coupled**:
- **AC-coupled**: battery has its own inverter; can be added to any existing PV system after the fact. Slightly less efficient (DC→AC→DC→AC = ~90% round-trip).
- **DC-coupled**: battery shares an inverter with the PV array; must be designed together. Better round-trip efficiency (~94%). Better for new construction where the system is designed as one.

**For new construction**: DC-coupled (Powerwall 3 or Generac PWRcell) is slightly more efficient and slightly cheaper. AC-coupled (Enphase, Franklin) is more flexible and easier to expand later. Both are legitimate choices.

### 2.4 Racking and Mounting

| System | Use | Notes |
|---|---|---|
| **IronRidge XR Rail (XR10, XR100, XR1000)** | Composite shingle, tile, metal | Most popular in CA; QBlock or FlashFoot2 flashings |
| **Unirac SolarMount / SunFrame** | Composite, tile | Strong dealer network |
| **SnapNrack TopSpeed, Series 100** | Composite, tile | Roof Mount NXT for fast install |
| **Quick Mount PV (now part of Esdec)** | Flashings (works with any rail) | Industry-standard flashing |
| **Ballasted (S-5!, PanelClaw)** | Flat or low-slope membrane roofs | No penetrations; requires structural review of dead load |
| **Ground mount (IronRidge GMS, Unirac GFT)** | When roof is unsuitable | Better orientation but trenching, conduit run, possibly setback issues |
| **Solar canopy / patio cover** | Detached structure | Often a separate building permit; structural design required |
| **Tile hooks / S-tile flashings** | Concrete or clay tile roofs | Tile replacement and proper hook flashing is the #1 leak risk |

**Roof attachment fundamentals**:
- L-foot or standoff lag bolted into **rafter** (never just sheathing). Pull-out values per IBC 2304 and mfr spec.
- Flashing must integrate with roofing per the roof manufacturer's warranty. Tile roofs require either a tile replacement flashing (e.g., Quick Mount Tile Replacement) or a tile hook with proper underlayment work.
- Composition shingle: lag bolt sealed with butyl, then flashing slipped under upper course shingles.

### 2.5 Monitoring

All current systems include built-in monitoring via the inverter or battery manufacturer's app:
- **Enphase Enlighten** (microinverters + IQ Battery) — per-panel data, lifetime warranty cloud.
- **Tesla App** — Powerwall + Solar (if Tesla inverter) — slick UI but limited per-panel.
- **SolarEdge mySolarEdge** — per-panel via optimizers.
- **Franklin WH App** — system level.

Customer expects this on day one. Confirm Wi-Fi reach to inverter/gateway location during rough-in (or run Cat6 to it).

---

## 3. NEC 690 — Electrical Code for Solar

California adopts the NEC via the **2022 California Electrical Code (Title 24, Part 3)**, currently the 2023 NEC base. The 2026 cycle adopts NEC 2026 — verify with your AHJ at permit submittal.

### 3.1 Governing Articles

| NEC Article | Scope |
|---|---|
| **690** | Solar Photovoltaic Systems |
| **691** | Large-scale PV (>5 MW; not residential) |
| **705** | Interconnected Electric Power Production Sources (where PV ties into the grid) |
| **706** | Energy Storage Systems (batteries) |
| **710** | Stand-alone systems (off-grid) |
| **712** | DC microgrids |

### 3.2 System Limits

| Parameter | Residential Limit |
|---|---|
| AC inverter output | Typically ≤30 kW (above triggers more stringent interconnection review) |
| DC input voltage (string) | ≤600 V for most residential inverters; up to 1000 V for some |
| Maximum array voltage | NEC 690.7 — open-circuit voltage corrected to lowest expected ambient temperature |
| Number of strings per inverter | Inverter-specific; see datasheet |

### 3.3 Rapid Shutdown — NEC 690.12

Within **30 seconds** of initiating shutdown, conductors **inside the array boundary** (within 1 ft of the array) must drop to **≤30 V**, and conductors **outside the boundary** (running down the wall to the inverter) must drop to **≤30 V** as well.

**Initiation**: a shutdown switch at a readily accessible location — typically next to the AC disconnect or service panel. Marked "Rapid Shutdown Switch for Solar PV System" with a NEC-mandated red/yellow placard.

**Why it matters**: firefighter safety. Pre-rapid-shutdown systems had ~600 V DC live on the roof even with AC off. Now a firefighter cutting through a roof faces ≤30 V.

**Compliance methods**:
- Microinverters (Enphase) — inherently compliant.
- Optimizers with SafeDC (SolarEdge, Tigo) — compliant.
- String inverter alone — NOT compliant; needs added module-level disconnect.

### 3.4 Grounding and Bonding (NEC 250 + 690 V)

- **Equipment grounding** — all metal frames, racking, inverter chassis, junction boxes bonded to a single equipment grounding conductor (EGC) returning to the main service bonding bus.
- **Array frame grounding** — most rails use UL 2703-listed integrated grounding via WEEBs (Washer, Electrical Equipment Bonding) so the EGC bonds the rail and modules continuously.
- **PV system grounding** — modern inverters are transformerless; the array is **ungrounded DC** (functionally grounded through GFDI inside inverter). Do NOT install a separate DC grounding electrode unless the inverter spec requires it.
- **Battery grounding** — NEC 706 + mfr instructions; LFP systems require equipment grounding only.

### 3.5 Disconnects

| Disconnect | Required | Location |
|---|---|---|
| **AC disconnect (PV)** | Yes (NEC 690.13 + utility) | Within sight of inverter and within 10 ft of utility service meter; lockable in OFF position; visible blade or labeled |
| **DC disconnect** | Yes (NEC 690.15) | Within sight of inverter; usually integrated in inverter cabinet |
| **Battery disconnect** | Yes (NEC 706.7) | Within sight of battery; usually integrated |
| **Rapid shutdown initiator** | Yes (NEC 690.12) | Readily accessible; often co-located with AC disconnect |
| **Utility service disconnect** | Yes (CA law since 2020) | Outside the home for fire department access — usually 200A main breaker in exterior service section |

### 3.6 Production Meter

For NEM, the utility requires either:
- A **dedicated production meter** adjacent to the main service meter (older utility standard), or
- A **single bidirectional meter** that reads inflow and outflow (current PG&E and SCE standard).

If the inverter has built-in revenue-grade metering (Enphase Envoy, Tesla Gateway), some utilities accept that and skip the separate meter. Confirm with utility before rough-in.

### 3.7 Battery Electrical (NEC 706)

- **Working clearances** — NEC 110.26: 36" front clearance, 30" wide, 6'-6" headroom in front of battery.
- **Egress** — battery cannot block an emergency egress path.
- **Location restrictions** — not inside a dwelling unit habitable space unless UL 9540A tested for that location. Garages, exterior walls, and utility rooms are standard. Bedroom and closet installations are restricted.
- **CRC R327 / CFC** — California Fire Code rules: max 20 kWh per battery system in residential garages without additional separation; >20 kWh requires 1-hr rated separation or alternate compliance per UL 9540A test data. Spec sheets from mfr include AHJ-acceptance language.
- **Smoke / heat detection** — required in battery room per CFC.
- **Ventilation** — LFP batteries are sealed and do not require room ventilation. NMC may require ventilation per mfr.
- **Temperature** — typical operating range 32°F to 110°F; garage walls in inland zones can hit 120°F+ in summer. Consider insulating or shading the battery wall.

### 3.8 Labeling

Required at multiple points (NEC 690.13, 690.54, 690.56, 705.10, etc.):
- **Service panel placard**: "Photovoltaic System Connected" + system specs (Vmax, Isc, AC output).
- **Bidirectional meter**: "Photovoltaic Power Source" placard.
- **AC disconnect**: "PV System AC Disconnect" + rated current and voltage.
- **DC conduit and junction boxes**: "Warning: Photovoltaic Power Source" — every 10 ft and at every change of direction.
- **Rapid shutdown placard**: red/yellow per NEC 690.56(C) at service entrance.
- **Battery placard**: chemistry, kWh, voltage, "Energy Storage System" warning.

All labels must be **engraved or UV-stable laminated**, not handwritten or paper labels.

---

## 4. GC's Rough-In Scope for New Construction

### 4.1 What the GC Actually Does

You are not the solar installer. The solar installer is licensed under **CSLB C-46 (Solar Contractor)** or **C-10 (Electrical Contractor)**. Your responsibility is to **prepare the building** so the installer can complete the work efficiently and so the system passes inspection and PTO.

**Your rough-in scope typically includes**:
1. Structural framing capable of carrying the panel array.
2. Conduit runs (often pulled by your electrical sub).
3. Panel sizing and breaker space.
4. Roof penetration blocking.
5. Battery wall space + clearances.
6. Wi-Fi/Ethernet to inverter location.
7. Sub coordination — solar designer's plan ↔ framer ↔ roofer ↔ electrician.

### 4.2 Solar-Ready (When PV Is NOT Installed at Construction)

Required by **CRC R331** and **Title 24 §110.10** when an exception to the PV mandate applies. The "solar-ready" stub-out cost is typically $400–800 if planned, $3,000+ if retrofitted later.

| Component | Spec |
|---|---|
| **Conduit from main panel to attic/roof** | Min **1" EMT or PVC** (some jurisdictions require 1¼"); dedicated; labeled "Solar PV System — Future Use" at both ends |
| **Solar zone on roof** | Minimum **250 sf** (single-family) of unshaded south, east, or west-facing roof |
| **Structural** | Roof framing designed for 5 psf additional dead load |
| **Main panel** | Reserved breaker space OR a sub-panel ready for backfeed |
| **Documentation** | Permanent placard in electrical room/garage describing solar-ready provisions and intended array location |

Note: the **3" conduit** spec mentioned by some installers refers to large multifamily or oversized provisions; the code minimum for single-family is 1". Verify with AHJ.

### 4.3 When PV IS Installed at Construction (the Mandate Default)

#### Main service panel sizing

| Home Load Profile | Recommended Panel |
|---|---|
| Standard 2,000 sf, gas appliances, no EV | 200 A |
| All-electric (heat pump HVAC + HPWH + induction) | 200 A with EV-ready provision |
| All-electric + Level 2 EV (40 A) | 200 A with smart panel (SPAN, Lumin) **or** 225/400 A |
| All-electric + EV + battery + pool + AC | **400 A** service or smart-panel load-shedding |

**Calculate per NEC 220 Part III** (Standard Calc) or **Part IV** (Optional Method) with the energy consultant or electrician. NEC 705.12 governs the **120% rule** for backfed solar breakers — the inverter breaker amperage plus the main breaker cannot exceed 120% of the busbar rating. Example: 200A busbar, 200A main = 40A backfeed allowed (200 × 1.2 - 200 = 40 A). A 7.6 kW inverter at 240 V = 31.7 A, OK.

**Workarounds when 120% rule is exceeded**:
1. Upsize main panel (200A → 225A busbar).
2. Move main breaker to derated position ("line side tap" via meter-main with separate solar disconnect, or use a "supply-side tap" per NEC 705.11).
3. Use a **smart panel** (SPAN, Lumin, Leviton) that allows dynamic load management.

#### Conduit routing

| Run | Typical Size |
|---|---|
| Roof to attic/inverter (microinverter AC trunk) | 3/4" EMT (carries 240V AC, 1–2 trunk cables, ~25–40 A) |
| Roof to inverter (string inverter DC) | 3/4" to 1" EMT (DC strings + EGC) |
| Inverter to main panel (AC output) | 3/4" to 1" EMT depending on amperage |
| Battery to inverter / gateway | 1" to 1¼" EMT or LFMC for DC bus and comms |
| Critical-load subpanel feed | 1" minimum |

**Pull strings** in every empty conduit. Sweep elbows, not LBs, on long runs (>20 ft) to keep pull tension low. Limit conduit fill to NEC Chapter 9 Table 1.

#### Roof penetrations

- Final panel layout from solar designer **before** the roofer dries-in.
- Frame **2× blocking** between rafters at every anticipated attachment point (typically every 48" on center along rails) — gives the installer flexibility if the layout shifts.
- Use **engineered flashing** (Quick Mount QB, FlashFoot2, Oatey) for every penetration. **Never** caulk only.
- Single conduit roof penetration (for AC trunk down from microinverter system) — use a **storm collar flashing** (Oatey or DECKMATE).

#### Battery location

| Acceptable | Marginal | Avoid |
|---|---|---|
| Attached garage, interior wall | Detached garage (range to inverter) | Inside conditioned living space (CFC restriction) |
| Exterior wall, north or shaded side, weather-rated enclosure | Crawlspace (humidity, access) | Attic (heat) |
| Utility/mechanical room | Carport (security) | Bedroom or closet |
| Basement (CA homes rare) | | |

Clearances per NEC 110.26 (electrical) **and** mfr install manual (often 6" sides, 12" top, 36" front). Coordinate with HVAC, water heater, electrical panel for the 36" front clearance — this is the most common AHJ red-tag at rough-in inspection.

#### Interconnection point

- Pre-coordinate the **solar backfeed breaker** location with the electrician. NEC 705.12(B)(3)(2): backfeed breaker should be at the **opposite end of the busbar from the main breaker** when possible.
- Reserve **2 adjacent spaces** (240V double-pole) for the solar breaker.
- Reserve additional **2 spaces** for the battery breaker (if AC-coupled).
- Label-as-built when the installer connects.

#### Wi-Fi and gateway

- The inverter/gateway needs Internet for monitoring and (per NEM agreement) revenue-grade reporting.
- Pull **Cat6** to inverter and battery gateway locations. Wi-Fi alone is acceptable but creates support headaches when the homeowner changes routers.

---

## 5. Permitting Solar in California

### 5.1 Who Pulls What

| Permit | Who Pulls | Notes |
|---|---|---|
| Building permit (combined with solar) | Solar contractor (C-46 or C-10) | Most CA jurisdictions issue a single combined solar permit |
| Structural component (roof penetrations) | Same | Some AHJs require a structural calc letter (PE-stamped) for non-prescriptive racking |
| Electrical | Same | Includes battery |
| Battery storage (when separate) | Same | A few AHJs require a separate ESS permit |

For the GC running a new home: **the solar permit is usually pulled by your solar sub** under their license, separate from your master building permit. Coordinate timing so the solar permit is pulled and the rough-in inspection on solar conduit happens before drywall closes the walls.

### 5.2 SolarAPP+ — Instant Online Permitting

NREL-developed automated permit platform. Authorized statewide under **SB 379 (Wiener, 2022)**, which requires non-exempt cities and counties to offer an online instant-permit platform for residential solar.

| Year | CA Jurisdictions Adopted |
|---|---|
| 2022 | ~5 (early pilots) |
| 2024 | ~15 |
| 2026 | **20+** (per CEC dashboard, Jan 2026 data) — includes LA, San Francisco, Oakland, Fresno, Stockton, San Jose, and others |

**How it works**:
1. Solar contractor enters system specs into SolarAPP+ web tool.
2. Algorithm checks against NEC, CRC, CFC, Title 24 rules.
3. Compliant systems receive **instant permit** (PDF) — usually within minutes; some AHJs cap at 1 business day.
4. Inspection still required after install.

**What disqualifies a project from SolarAPP+** (forces conventional plan-check):
- Non-prescriptive racking (engineered structural required).
- System >38.4 kW DC (most residential is fine).
- Ground mount (some AHJs).
- Battery >40 kWh.
- Complex interconnection (line-side tap, supply-side, sub-feed).
- Historic district or design review overlay.

Track adoption at the [CEC Residential Solar Permit Status Dashboard](https://www.energy.ca.gov/programs-and-topics/programs/residential-solar-permit-reporting-program-sb-379/residential-solar).

### 5.3 Inspections

| Inspection | Triggers | What's Checked |
|---|---|---|
| **Rough-in (conduit)** | Before drywall closes wall | Conduit sizing, supports, EGC, labels |
| **Roof / structural** | After racking installed, before panels | Flashing, lag location into rafter, rail anchorage, dead load math |
| **Electrical final** | After panel install and inverter wired | Conductor sizing, OCPD, labels, rapid shutdown function test, AC disconnect, grounding |
| **Battery** | After battery wired, often combined with electrical final | NEC 706 clearances, 110.26, ventilation, smoke/heat detector, fire separation |
| **Building final** | All of the above signed off | AHJ stamps system "Final" — required for utility PTO |

### 5.4 Utility Interconnection

Separate process from building permit. Steps:

1. **Pre-construction** (during design): Solar designer submits Interconnection Application via PG&E/SCE/SDG&E online portal. PG&E uses the "Your Projects" portal. Application includes single-line diagram, equipment list, site plan.
2. **AHJ Final Inspection**: building dept signs off; solar contractor uploads signed-off card to utility portal.
3. **Net Energy Metering Agreement / NBT Agreement**: customer signs electronically; sets vintage year for ACC rate.
4. **PTO (Permission to Operate)**: utility issues PTO email/letter. **Until PTO, the system must remain OFF** (penalty if energized). PTO turnaround: PG&E 2–6 weeks (was 8–12 in 2023); SCE 1–4 weeks; SDG&E 2–4 weeks; LADWP 4–8 weeks (longer).
5. **Meter upgrade** (if needed): utility swaps in bidirectional smart meter — often does this in parallel.

**GC's role**: monitor PTO milestone for CofO compliance. Many CA jurisdictions require **interconnection approval (or at least signed-off final)** prior to issuing Certificate of Occupancy on a new home.

### 5.5 Title 24 Documentation Chain (CF1R / CF2R / CF3R)

| Doc | Who Signs | When |
|---|---|---|
| **CF1R-PRF-01-E** | Energy consultant | Submitted at plan check; defines design |
| **CF2R-PV-01-E** | Solar installer | Submitted after install; documents what was built |
| **CF3R-PV-01-E** | HERS rater (if required) | Submitted after HERS verification of any solar-related compliance measures |

Solar PV itself is typically **prescriptively self-certifying** (no HERS test of production), but if the system is sized via performance method or includes battery for the 25% PV reduction, the documents must close out.

---

## 6. System Sizing — What the GC Should Know

### 6.1 Basic Sizing Math

**Annual kWh consumption ÷ Annual production per kW = system size in kW**

| Region | kWh/kW/year (Annual Specific Yield) |
|---|---|
| **San Diego, OC** (Climate Zones 6–7) | 1,700–1,900 |
| **Inland Empire, Sacramento, Central Valley** (CZ 9, 10, 12, 13) | **1,900–2,100** |
| **Coastal LA / Long Beach** (CZ 8) | 1,600–1,800 |
| **San Francisco Bay Area** (CZ 3) | 1,400–1,650 |
| **North Coast (Eureka, Mendocino)** (CZ 1) | 1,200–1,400 |
| **High Desert (Palmdale, Victorville)** (CZ 14) | 2,000–2,200 |

**Worked example**: Sacramento home, 12,000 kWh/yr usage.
- 12,000 ÷ 2,000 = **6.0 kW DC** system.
- At 430 W per panel = **14 panels**.
- At ~$3.25/W installed = **~$19,500** pre-incentives; **~$13,650** after 30% ITC.

### 6.2 Title 24 Prescriptive Sizing

The 2022 Title 24 formula (Section 150.1(c)14):

**kWPV = (CFA × A) / 1000 + (NDwell × B)**

Where:
- CFA = conditioned floor area (sf)
- NDwell = number of dwelling units (1 for SFR)
- A, B = climate-zone-specific coefficients (Table 150.1-C)

**Typical results**:

| Climate Zone | Example City | A (Wdc/sf) | B (kW/dwelling) | 2,500 sf home PV size |
|---|---|---|---|---|
| 3 | San Francisco | 0.504 | 0.871 | **~2.13 kW** |
| 9 | Burbank | 0.625 | 0.846 | **~2.41 kW** |
| 12 | Sacramento | 0.617 | 0.871 | **~2.41 kW** |
| 13 | Fresno | 0.620 | 0.842 | **~2.39 kW** |
| 14 | Palmdale | 0.717 | 0.846 | **~2.64 kW** |

**These are minimums.** Most homeowners want larger systems to offset full electric load, especially with NEM 3.0 + battery economics. The mandate floor is rarely the practical install size — typical SFR installs are 5–10 kW.

**With battery (JA12-compliant ≥7.5 kWh)**: multiply PV size by 0.75 (25% reduction). A 2.41 kW prescriptive becomes 1.81 kW PV + 7.5 kWh battery.

### 6.3 Battery Sizing

Decision framework:

| Client Goal | Battery Configuration |
|---|---|
| Title 24 compliance minimum + 25% PV reduction | 1× 7.5 kWh JA12 battery (one IQ Battery 10C or smaller Powerwall slice) |
| TOU arbitrage only (no backup) | 1× 10–13.5 kWh battery |
| Backup for **critical loads** (fridge, lights, internet, one HVAC mini-split) for 12–24 hr outage | 1× 13.5 kWh Powerwall 3, or 2× IQ Battery 5P |
| **Whole-home backup** including AC and EV charging | 2–3× 13.5 kWh Powerwalls, or 3–4× IQ Batteries |
| Off-grid capable (rare in CA) | 4× 13.5 kWh + generator backup |

**Sizing for backup** — figure out the critical load list with the homeowner, sum the power draw and run-time:
- Refrigerator: ~1.5 kWh/day
- Lighting (LED, partial): ~1.5 kWh/day
- Internet/networking: ~0.5 kWh/day
- Window AC or one mini-split: ~5–10 kWh/day
- EV charging (Level 2 at 32 A): 7.7 kW — generally NOT recommended for backup

A typical critical-load backup is 8–15 kWh/day for ~24-hour ride-through.

### 6.4 Shading Analysis

The single most impactful design constraint. Solar designers use **Solmetric SunEye**, **Aurora Solar's 3D modeling**, or drone LIDAR to map shading hour-by-hour throughout the year.

| Orientation | Annual Production vs. South-Optimal |
|---|---|
| South, 20° pitch, no shade | 100% (baseline) |
| Southwest or Southeast | 95–98% |
| East or West | 80–88% |
| Flat (0°) | 88–92% |
| North | 60–70% (rarely worth installing) |
| South with 30% shade at midday | 60–75% |

**As a GC**: tree removal or trimming is often needed for the array to pencil. Address this with the homeowner **before** sub-bids. A protected oak tree on the south side can kill the project economics.

---

## 7. Coordination for New Construction

### 7.1 Roofing Coordination

The single biggest source of warranty disputes between subs.

| Issue | Best Practice |
|---|---|
| Who installs the flashing? | **Solar installer** installs racking flashings (they own the array warranty). Roofer dries-in the field. Specify in subcontract scope. |
| What about the conduit penetration? | **Roofer** installs the conduit jack/storm collar (it's a roofing component); electrician runs conduit through. |
| Warranty interaction | Tile/composition mfr warranty often voided if untrained installer penetrates. Use a **mfr-certified solar installer** for tile roofs (CertainTeed, Owens Corning, GAF Solar all certify). |
| Tile roofs | Replace tiles at every attachment with a tile-replacement flashing (Quick Mount Tile, IronRidge Tile Hook with proper underlayment). Avoid tile hooks without underlayment work. |
| Membrane (TPO, PVC) | Hot-air-weld an attachment plate. Specialty contractor (the roofer, usually). |
| Standing-seam metal | S-5! clamps — no penetration. |
| Coordination sequence | **(1) Frame** with solar blocking → **(2) Dry-in** by roofer → **(3) Final roof finish** with array layout marked → **(4) Solar installer** installs flashings + racking → **(5) Solar installer** installs panels and wiring → **(6) Roofer punches** any remaining detail work |

### 7.2 Framing Coordination

- Rafter spacing: most CA tract framing is 24" o.c. Custom homes may be 16" o.c. **Get the solar designer's panel layout before framing.**
- Add **2× blocking** between rafters at planned attachment rows (every 48" o.c. vertically). Costs nothing at framing; expensive to retrofit.
- **Truss roof**: blocking must not interfere with truss web members; coordinate with truss engineer if non-prescriptive racking is needed.
- **Snow load**: rare in CA but matters in Tahoe, Mammoth — adds panel + snow dead load to the roof design.

### 7.3 Electrical Coordination

| Phase | Action |
|---|---|
| Plan check | Solar single-line on permit set; electrical engineer reviews backfeed and 120% rule |
| Rough wiring | Electrician runs conduit per solar designer's plan; pulls **only the conductors they own**; leaves the DC and microinverter trunk for the solar installer |
| Service panel | Electrician installs panel with **reserved breaker spaces** at the opposite end of busbar from the main |
| Battery wall | Electrician sets junction box + 50 A or 60 A breaker per battery mfr |
| Bonding | Single grounding electrode system, bonded to the main panel; PV equipment EGC lands on the panel ground bus |

### 7.4 Utility Coordination

- **Service meter**: PG&E/SCE often does a meter swap to a smart bidirectional meter at PTO. The GC's electrician must leave the meter socket and service section to utility spec — verify meter pan dimensions and labeling before installing.
- **Notice of Completion (NOC)**: solar installer files this with the utility once final inspection passes. The GC may file the master NOC for the whole project separately.
- **Streetlight/transformer review**: large systems (>10 kW) may trigger transformer load review. Rare for SFR but possible in older neighborhoods.

### 7.5 HERS Verification

Solar PV by itself is **not a HERS-tested measure**. HERS raters do not test production. However:
- **Battery storage** used to reduce required PV size (25% reduction) requires CF2R documentation; some AHJs interpret this as requiring HERS verification of the install.
- **Quality Insulation Installation (QII)** and **HERS heat-pump verification** can interact with the energy budget when solar is sized via performance method.
- Coordinate with your Title 24 consultant to confirm CF3R requirements early.

---

## 8. Economics for Client Conversations

### 8.1 Typical California Installed Costs (May 2026)

| System Size | Solar Only | Solar + 1 Battery | Solar + 2 Batteries |
|---|---|---|---|
| 5 kW PV | $14,000–17,000 | $26,000–32,000 | $38,000–45,000 |
| 7 kW PV | $19,000–23,000 | $31,000–37,000 | $43,000–50,000 |
| 10 kW PV | $26,000–32,000 | $38,000–45,000 | $50,000–58,000 |
| 13 kW PV | $33,000–40,000 | $45,000–53,000 | $57,000–66,000 |

Approx **$3.00–3.50/W** for solar-only, **$1,000–1,200/kWh** added for battery (installed) including SGIP-free pricing.

**After 30% federal ITC** (homeowner take-home cost on cash purchase):

| System Size | Solar Only Net | Solar + 1 Battery Net |
|---|---|---|
| 5 kW | $9,800–11,900 | $18,200–22,400 |
| 7 kW | $13,300–16,100 | $21,700–25,900 |
| 10 kW | $18,200–22,400 | $26,600–31,500 |
| 13 kW | $23,100–28,000 | $31,500–37,100 |

### 8.2 Payback Periods Under NEM 3.0

| Configuration | Typical Payback (post-ITC) | Notes |
|---|---|---|
| Solar only, no battery, NEM 3.0 | **9–13 years** | Self-consumption only; export credit weak |
| Solar + 1 battery, NEM 3.0 | **6–9 years** | Battery shifts midday to peak; arbitrage value is the killer feature |
| Solar + 2 batteries, NEM 3.0 | **7–10 years** | Diminishing returns past first battery for arbitrage; second battery is for backup |
| Solar only, NEM 2.0 (grandfathered) | 5–7 years (legacy) | Not available for new systems |

**Why batteries pay back faster under NEM 3.0**:

| Energy Flow | Rate Value |
|---|---|
| Solar produced at noon, exported to grid | ~$0.05/kWh credit |
| Solar produced at noon, stored to battery, discharged at 6 PM | Avoids ~$0.45–0.55/kWh import (PG&E E-TOU-C peak) |
| Differential value of battery vs. export | **~$0.40–0.50/kWh per stored kWh** |
| Daily battery cycle benefit | ~10 kWh × $0.45 = **$4.50/day** = ~$1,650/yr |

A $12,000 battery generating $1,650/yr in TOU arbitrage value pays back in ~7.3 years on its own, before ITC.

### 8.3 Financing Options

| Option | How It Works | GC Implications |
|---|---|---|
| **Cash** | Homeowner pays up front | GC bills solar in construction draw; homeowner claims 30% ITC; cleanest for new construction |
| **Construction loan rolled into mortgage** | Solar cost included in construction loan; refinanced into permanent mortgage | Most common for new homes; monthly mortgage increase ~$50–80 for typical PV; client claims ITC at year-end |
| **Solar loan** (separate) | 7–25 year solar-specific loan (Mosaic, Sungage, GoodLeap, Service Finance) | Often used in resale market; less common in new construction; client claims ITC |
| **Solar lease** | Third party owns system; client pays monthly fee | Third party claims §48 ITC; client gets fixed monthly bill; no upside; **avoid for new construction** — complicates future home sale |
| **PPA (Power Purchase Agreement)** | Third party owns; client pays per kWh produced | Same caveats as lease; legacy California product, less common since NEM 3.0 |

**For new construction**: cash or construction-loan-financed is overwhelmingly the right answer. Leases and PPAs encumber title and complicate resale.

### 8.4 New Construction Cost Loading

Critical point for client conversation:

| Path | Monthly Cost Impact (typical 7 kW + Powerwall on $800K home, 30-yr mortgage) |
|---|---|
| Add $25,000 net solar+battery to mortgage | +$140/month mortgage payment (at 6.5%) |
| Eliminate utility bill (typical $250/month before solar) | -$200/month utility |
| **Net monthly cash flow** | **+$60/month** (cash positive day one) |

This is the single most powerful framing for new construction solar. The home is **cash-flow-positive from move-in**, even before counting the 30% ITC refund the homeowner gets at tax time.

### 8.5 Common Client Questions and Answers

**Q: "Should I install solar or solar + battery?"**
A: Under NEM 3.0, battery turns marginal economics into strong economics. If the budget exists, install a battery. If not, the system can be added later (AC-coupled) — but plan conduit and wall space now.

**Q: "What if I install it later instead of now?"**
A: On new construction, you lose: (1) construction-loan financing (have to use a solar loan instead), (2) the value of having the GC coordinate roof/framing/electrical at no upcharge, (3) any current Title 24 compliance shortcut, (4) easier roof access. Adding solar later usually costs 15–25% more all-in.

**Q: "How long do panels last?"**
A: 25-year power warranty is standard (panels still produce ~85% of nameplate at year 25). Real-world degradation is ~0.4–0.5% per year. Inverters: 12–25 years (microinverters 25, string inverters 12 with extended warranty available). Batteries: 10-year warranty, typical real-world life 12–15 years to 70% capacity.

**Q: "What about hail / wildfire / earthquake?"**
A: Most homeowner policies cover roof solar as part of the dwelling. Standalone solar insurance is available (Solar Insure). Discuss with insurance broker. Wildfire risk districts may require Class A roof assembly under the panels — verify with AHJ.

**Q: "What if I sell the home?"**
A: Owned solar adds value (~$15,000 to $30,000 per Lawrence Berkeley Lab studies). Leased solar can complicate sale (buyer must assume lease or seller buys out). Strongly recommend owned, not leased, for resale value.

---

## 9. Quick-Reference Checklists

### 9.1 Schematic Design Phase

- [ ] Climate zone identified, Title 24 PV size calculated.
- [ ] Roof plan reviewed for solar zone availability; shading flagged.
- [ ] Battery decision made (yes/no, capacity, location).
- [ ] Main panel size confirmed via NEC 220 load calc.
- [ ] All-electric vs. mixed-fuel decision (impacts panel size).
- [ ] Solar contractor selected (C-46 or C-10 + solar specialty).

### 9.2 Permit Set

- [ ] Title 24 CF1R complete with PV (and battery if applicable).
- [ ] Solar single-line diagram and site plan in permit set.
- [ ] Structural calcs for racking (if non-prescriptive).
- [ ] Battery cut sheets and CFC compliance letter.
- [ ] Combined building + electrical permit submitted (or SolarAPP+ if available in AHJ).
- [ ] Utility interconnection application submitted.

### 9.3 Rough-In

- [ ] Roof blocking installed per solar layout.
- [ ] Conduit from roof to inverter/main panel + Cat6 pull string.
- [ ] Conduit from inverter to battery location.
- [ ] Main panel set with reserved breaker spaces at opposite end of busbar from main breaker.
- [ ] Battery wall clearances confirmed (36" front per NEC 110.26).
- [ ] Smoke/heat detector at battery location wired.
- [ ] AC disconnect location coordinated.
- [ ] Rough-in inspection signed off **before drywall**.

### 9.4 Trim / Solar Install

- [ ] Roofer dry-in complete with array footprint marked.
- [ ] Solar installer installs flashings + racking + panels.
- [ ] Inverter and battery wired and labeled.
- [ ] Rapid shutdown function tested.
- [ ] All NEC 690.56 labels installed.
- [ ] System remains de-energized pending PTO.

### 9.5 Final

- [ ] Building final inspection passed.
- [ ] Electrical final passed.
- [ ] Battery / ESS final passed.
- [ ] Title 24 CF2R signed by installer.
- [ ] Utility interconnection PTO received.
- [ ] System energized; monitoring active.
- [ ] Homeowner walkthrough: app setup, breaker labeling, shutdown procedure, warranty docs.
- [ ] CofO issued (where utility PTO required for CofO).

---

## 10. Failure Modes — What Goes Wrong

| Failure | Cause | Prevention |
|---|---|---|
| **Conduit re-pulled after drywall** | Solar designer's layout changed after rough-in | Lock layout before framing; overprovision conduit (1" instead of 3/4") |
| **120% rule violated at panel** | Panel sized without solar in mind | Include solar in NEC 220 load calc from day one |
| **Battery clearances fail inspection** | Homeowner stored items in front of battery; or water heater/HVAC installed in clearance zone | Mark 36" clear zone on slab/floor; communicate with HVAC and plumbing subs |
| **Roof leak at attachment** | Improper flashing; lag bolt missed rafter | Use trained installer + flashing inspection prior to panel install |
| **PTO delayed past CofO** | Interconnection app submitted late; utility backlog | Submit interconnection app at rough-in stage; don't wait for completion |
| **Customer surprised by NEM 3.0 export rates** | Sold under NEM 2.0 assumptions | Use current ACC rates and battery economics in proposal; document expectations |
| **Title 24 compliance fails CF2R** | Wrong panel count, wrong inverter, undersized battery | CF1R and CF2R must match; verify installer files CF2R immediately post-install |
| **SunPower-installed system orphaned** | Customer bought pre-2024 SunPower lease/loan | Refer to current Maxeon / Complete Solaria warranty service; document chain of custody |
| **Battery too hot in garage** | Inland zone, uninsulated west-facing wall | Locate on north or shaded wall; insulate; add ventilation if NMC |

---

## 11. Codes, Standards, and References Cheat Sheet

| Code / Standard | Topic |
|---|---|
| **NEC 690** | Solar PV systems |
| **NEC 705** | Interconnection |
| **NEC 706** | Energy storage |
| **NEC 110.26** | Working clearances |
| **NEC 250** | Grounding and bonding |
| **NEC 220** | Branch circuit and feeder load calculations |
| **Title 24, Part 6** | California Energy Code (PV mandate, sizing) |
| **Title 24, Part 3** | California Electrical Code |
| **Title 24, Part 9** | California Fire Code (battery clearances, separation) |
| **CRC R327 / R331** | Battery / solar-ready prescriptive |
| **UL 1741 SA / SB** | Inverter grid support / smart inverter functions |
| **UL 9540 / 9540A** | ESS safety / fire propagation testing |
| **UL 1703 / 61730** | PV module safety |
| **UL 2703** | PV racking and grounding |
| **IEEE 1547-2018** | Distributed energy resource interconnection |
| **NREL JA12 / California JA12** | Battery storage compliance for Title 24 25% PV reduction |
| **CPUC D.22-12-056** | NEM 3.0 / NBT decision |
| **CEC Joint Appendix JA11** | Energy management control device specifications |

---

## 12. Bottom Line for the GC

1. **Treat solar as a standard new-home system**, like HVAC or plumbing. Get the layout locked at schematic design.
2. **Pull conduit at rough-in even if the array isn't certain.** Walls are cheaper than retrofit.
3. **NEM 3.0 changed the math.** Sell the battery, not just the panels. Use TOU arbitrage as the headline economic argument.
4. **Coordinate four subs**: framer (blocking), roofer (dry-in and flashings interface), electrician (panel + conduit), solar installer (final). Pre-construction meeting prevents 80% of disputes.
5. **Watch PTO** as a CofO dependency. Submit the interconnection application at rough-in, not at final.
6. **Don't promise SGIP** in market-rate proposals (May 2026 funding closed). Federal 30% ITC and Title 24 compliance are the reliable economic levers.
7. **Sell the cash-flow story** on new construction: mortgage adder < utility savings = positive cash flow on day one.

---

## Sources

- [CPUC: Net Energy Metering and Net Billing](https://www.cpuc.ca.gov/industries-and-topics/electrical-energy/demand-side-management/customer-generation/net-energy-metering-and-net-billing)
- [PG&E Solar Billing Plan (NEM 3.0)](https://www.pge.com/en/clean-energy/solar/getting-started-with-solar/solar-billing-plan.html)
- [Aurora Solar — Explaining California's Net Billing Tariff (NEM 3.0)](https://aurorasolar.com/blog/explaining-and-modeling-californias-net-billing-tariff-nem-3-0/)
- [CEC: 2022 Low-Rise Multifamily Solar PV](https://www.energy.ca.gov/programs-and-topics/programs/building-energy-efficiency-standards/energy-code-support-center/2022-2)
- [CEC: Solar PV, Solar Ready, BESS & BESS-Ready](https://www.energy.ca.gov/programs-and-topics/programs/building-energy-efficiency-standards/energy-code-support-center/solar)
- [CEC: California Automated Permit Processing Program (CalAPP)](https://www.energy.ca.gov/programs-and-topics/programs/california-automated-permit-processing-program-calapp)
- [CEC: Residential Solar Permit Reporting Dashboard (SB 379)](https://www.energy.ca.gov/programs-and-topics/programs/residential-solar-permit-reporting-program-sb-379/residential-solar)
- [CPUC: Self-Generation Incentive Program (SGIP)](https://www.cpuc.ca.gov/industries-and-topics/electrical-energy/demand-side-management/self-generation-incentive-program/participating-in-self-generation-incentive-program-sgip)
- [PG&E: Self-Generation Incentive Program](https://www.pge.com/en/save-energy-and-money/rebates-and-incentives/self-generation-incentive-program.html)
- [Tesla Support: Net Billing Tariff](https://www.tesla.com/support/energy/solar-panels/learn/net-billing)
- [EnergySage: NEM 3.0 in California](https://www.energysage.com/blog/net-metering-3-0/)
- [FranklinWH: California Net Billing Tariff Knowledge Center](https://www.franklinwh.com/knowledge-center/california-net-billing-tariff-nbt)
- [DOE: Streamlining Solar Permitting with SolarAPP+](https://www.energy.ca.gov/programs-and-topics/programs/residential-solar-permit-reporting-program-sb-379/residential-solar)
- [CEC Energy Code Ace: §140.10 Prescriptive Requirements for PV and Battery Storage](https://energycodeace.com/site/custom/public/reference-ace-2022/Documents/section14010prescriptiverequirementsforphotovoltaicandbatterysto.htm)
- IRS Form 5695 instructions (Residential Energy Credits, IRC §25D)
- NEC 2023 (NFPA 70) — Articles 690, 705, 706
- 2022 California Building Standards Code (Title 24, Parts 3, 6, 9)
