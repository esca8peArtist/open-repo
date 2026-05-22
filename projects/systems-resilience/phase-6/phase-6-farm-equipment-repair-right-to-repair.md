---
title: "Farm Equipment Repair & Right-to-Repair"
phase: 6
status: production
word_count: ~10200
audience: "Systems-resilience project — individual through community scale, Midwest Zone 5"
created: 2026-05-22
cross_references:
  - individual/06-agriculture.md
  - 04-technology-repair-equipment-protocols.md
  - 04-technology-repair-community-infrastructure.md
  - midwest/moisture-extraction-farm-tools.md
sources_count: 28
---

# Farm Equipment Repair & Right-to-Repair

> **Region**: Midwest US (Zone 5) | **Scale**: Individual → community
> **Phase**: 6 — Exploration Queue Item 28
> **Cross-references**: [individual/06-agriculture.md](../individual/06-agriculture.md) · [04-technology-repair-equipment-protocols.md](../04-technology-repair-equipment-protocols.md) · [04-technology-repair-community-infrastructure.md](../04-technology-repair-community-infrastructure.md) · [midwest/moisture-extraction-farm-tools.md](../midwest/moisture-extraction-farm-tools.md)

---

## The Most Important Finding

The legal and regulatory landscape for farm equipment repair shifted materially in 2026. Two developments happened within months of each other: John Deere agreed in April 2026 to a $99 million class-action settlement requiring the company to provide farmers and independent repair providers (IRPs) genuine access to diagnostic tools and software for ten years, and the EPA issued guidance in February 2026 explicitly affirming that the Clean Air Act permits temporary override of emissions control systems — including Diesel Exhaust Fluid (DEF) inducement systems — when the purpose is repair. Taken together, these two actions removed two of the largest legal and practical barriers that have blocked independent farm equipment repair for a decade.

What has not changed: the DMCA Section 1201 problem remains live, the John Deere settlement has not yet received final court approval as of May 2026, and the actual diagnostic software access promised by the settlement is not scheduled to become available until end-of-2026. This is an improving landscape, not a solved one. For a household or community planning around system failure, the practical constraint is still acute: a broken tractor during planting or harvest season represents a catastrophic productivity loss that the legal landscape does not yet reliably prevent.

The operational response to this gap is the main focus of this document: preventive maintenance procedures that reduce failure probability, diagnostic approaches that reduce dependence on proprietary software, parts sourcing strategies that reduce dependence on dealers, and the current legal status of repair approaches including software circumvention.

---

## Part 1: The Legal Landscape — What Changed in 2026

### The John Deere $99 Million Settlement (April 2026)

In April 2026, John Deere reached a class-action antitrust settlement in the Northern District of Illinois, agreeing to pay $99 million to farmers who paid dealer-exclusive repair costs between January 10, 2018 and the settlement date. The settlement received preliminary court approval in May 2026. A fairness hearing is scheduled for October 29, 2026 — final approval is not yet granted.

**What the settlement requires Deere to provide:**

- Digital tools enabling farmers and IRPs to diagnose and repair large agricultural equipment without requiring authorized dealer involvement
- Access to the same repair tools available through Deere's Dealer Technical Assistance Center (DTAC)
- Ability to perform reprogramming and diagnostic functions in offline mode through John Deere Operations Center PRO Service
- These obligations extend for a ten-year period from settlement finalization

**Timeline:** Deere committed that customer access to offline diagnostic and reprogramming functions would be available by December 31, 2026.

**Equipment covered:** Large agricultural equipment — tractors, combines, and sugarcane harvesters. Smaller equipment (compact tractors, consumer lawn equipment) is not specified in the settlement.

**Remaining uncertainty:** The settlement specifies that tools will be provided "on fair and reasonable terms" but does not cap pricing. Deere can set its own price for software access. The settlement does not address Deere's ongoing separate FTC lawsuit, which challenges the structural repair restrictions beyond just class member compensation.

Sources: [John Deere settles right-to-repair lawsuit for $99 million — Farm Progress](https://www.farmprogress.com/farming-equipment/john-deere-settles-right-to-repair-lawsuit-for-99-million) · [John Deere's $99 Million Settlement — Arnold & Porter](https://www.arnoldporter.com/en/perspectives/blogs/consumer-products-and-retail-navigator/2026/04/john-deeres-99-million-settlement-and-the-right-to-repair-landscape) · [Federal Court Preliminary Approval — American Ag Network](https://www.americanagnetwork.com/2026/05/20/federal-court-gives-preliminary-approval-to-99-million-john-deere-right-to-repair-settlement/) · [Deere Right-to-Repair Settlement Gets Preliminary Approval — Farm Policy News Illinois](https://farmpolicynews.illinois.edu/2026/04/deere-settles-class-action-right-to-repair-lawsuit/)

### EPA February 2026 Guidance — Clean Air Act and Repair

On February 3, 2026, the EPA issued guidance clarifying that the Clean Air Act (CAA) supports farmers' right to repair their own equipment and does not restrict it. The specific context: equipment manufacturers had used CAA anti-tampering provisions as justification for locking farmers out of emissions control system repair, requiring dealer-only access to DEF (Diesel Exhaust Fluid) and SCR (Selective Catalytic Reduction) system diagnostics.

**What the guidance permits:**
- Temporary overrides of emissions control systems when done "for the purpose of repair" to restore proper functionality
- Repair of DEF, SCR, and inducement system components without requiring an authorized dealer
- Independent repair providers performing emissions-related diagnostics and repairs

**What it does not permit:**
- Permanent deletion or defeat of emissions systems
- Tune-based disabling of emissions controls for performance purposes
- Any modification that results in operation outside emissions compliance after repair is complete

The EPA separately issued guidance in March 2026 removing the requirement for DEF sensors specifically — addressing a narrow but operationally significant maintenance cost for farmers with Tier 4 Final diesel equipment.

**Legal status:** This is regulatory guidance, not statutory change. A future administration could revise or withdraw it. The Clean Air Act itself has not changed. For practical purposes: repair that restores proper function is permissible; permanent defeat is still federally prohibited.

Sources: [EPA Advances Farmers' Right to Repair — US EPA](https://www.epa.gov/newsreleases/epa-advances-farmers-right-repair-their-own-equipment-saving-repair-costs-and) · [EPA Affirms Farmers' Right to Repair Equipment — Farm Policy News](https://farmpolicynews.illinois.edu/2026/02/epa-affirms-farmers-right-to-repair-equipment/) · [EPA Guidance Allows Farmers to Repair Equipment Emissions — DTN/Progressive Farmer](https://www.dtnpf.com/agriculture/web/ag/equipment/article/2026/02/02/trump-epa-declares-farmers-can) · [EPA Eases DEF Sensor Rules — DTN](https://www.dtnpf.com/agriculture/web/ag/equipment/article/2026/03/30/epa-eases-def-sensor-rules-keeps-def)

### State Right-to-Repair Laws — Status as of May 2026

State right-to-repair legislation has moved faster than federal action, but coverage of agricultural equipment varies significantly.

| State | Law | Covers Farm Equipment? | Effective Date |
|---|---|---|---|
| Colorado | Consumer Right to Repair Digital Electronic Equipment Act | Yes — only US state with explicit farm equipment coverage | January 1, 2026 |
| Minnesota | Digital Fair Repair Act | No — agricultural and off-road equipment explicitly excluded | July 1, 2024 |
| Washington | Right to Repair | Consumer electronics only; farm equipment excluded | May 2025 |
| Texas | Right to repair | Phones, laptops, tablets; medical and farm equipment excluded | September 2025 |

Right-to-repair legislation has been introduced in all 50 US states. Fewer than 10 have enacted anything. Colorado stands alone in including agricultural equipment. Illinois — the state containing John Deere's headquarters and most relevant to Midwest farmers — has not enacted agricultural right-to-repair legislation as of this writing.

**Practical implication for Midwest Zone 5:** The federal legal landscape (EPA guidance + Deere settlement) is your primary legal cover for independent repair. State-level coverage is not reliable unless you are in Colorado.

Sources: [The State of Right to Repair — PIRG](https://pirg.org/edfund/resources/the-state-of-right-to-repair/) · [Right to Repair Laws Have Been Introduced in All 50 States — iFixit](https://www.ifixit.com/News/108371/right-to-repair-laws-have-now-been-introduced-in-all-50-us-states) · [Right to Repair Farm Equipment — ThomasNet](https://www.thomasnet.com/insights/right-to-repair-farm-equipment/) · [Colorado HB24-1121](http://leg.colorado.gov/bills/hb24-1121)

### DMCA Section 1201 — The Remaining Software Problem

The most significant remaining legal barrier is the Digital Millennium Copyright Act Section 1201, which prohibits circumvention of software access controls on any digital system — including agricultural equipment ECUs. Criminal penalties for Section 1201 violations are up to five years in federal prison and $500,000 in fines.

**The narrow agricultural exemption:** The Copyright Office has granted and repeatedly renewed a Section 1201 exemption specifically allowing tractor owners to diagnose, maintain, and repair their own vehicles. This exemption covers:
- Accessing ECU data for diagnosis and repair
- Modifying software only to the extent necessary for repair
- Work performed by the owner or a person working on the owner's behalf

**What the exemption does not cover:**
- Bypassing emissions controls for performance tuning (not repair)
- Enabling a tractor to operate outside of its certified emissions compliance
- Third-party jailbreaking tools distributed commercially
- Any modification that permanently defeats security or licensing controls

**Farm Freedom to Repair Act:** Pending federal legislation would permanently codify this exemption rather than requiring renewal every three years. As of May 2026, it has not passed.

**Practical bottom line:** A farmer accessing their own tractor's ECU to diagnose and repair a fault code operates within a valid DMCA Section 1201 exemption. A farmer permanently removing emissions controls or unlocking a software-restricted feature for non-repair purposes does not. The line is repair-intent vs. defeat-intent. Use care about third-party "jailbreak" tools sold online — their legal status is less clear and the consequences of a bad outcome are severe.

Sources: [John Deere Really Doesn't Want You to Own That Tractor — EFF](https://www.eff.org/deeplinks/2016/12/john-deere-really-doesnt-want-you-own-tractor) · [How Copyright Enabled John Deere to Restrict Farmers' Right to Repair — Captured Economy](https://capturedeconomy.com/how-copyright-enabled-john-deere-to-restrict-farmers-right-to-repair/) · [Deere Promised Farmers the Right to Repair — iFixit](https://www.ifixit.com/News/70877/deere-promised-farmers-the-right-to-repair-can-we-trust-them)

---

## Part 2: CAN Bus and OBD Diagnostics for Farm Equipment

### How Modern Tractors Communicate

Modern farm tractors — any equipment manufactured roughly post-2000, and increasingly relevant for 2010+ equipment — use a Controller Area Network (CAN bus) for internal communications between electronic control units (ECUs). Every major subsystem — engine, transmission, hydraulics, implement management, emissions controls — has its own ECU that broadcasts status data and receives commands over the CAN bus.

Unlike automotive OBD-II (which uses a standardized 16-pin port and standardized protocols), agricultural equipment uses ISO 11783 (ISOBUS) as the primary communication standard. ISOBUS is CAN-based but uses a different connector (a proprietary 9-pin diagnostic port on John Deere equipment; similar variations exist for AGCO and CNH equipment) and different protocol structure than automotive OBD-II.

**Key distinction:** You cannot plug a standard OBD-II scanner from an auto parts store into most tractors and get useful data. You need agricultural-specific diagnostic adapters and software.

### Independent Diagnostic Tools — What Actually Works

The diagnostic tool landscape for independent repair has improved significantly since 2020. The following tools provide real alternatives to proprietary dealer software:

**CanDo OHV Pro (Off-Highway Vehicle)**
- Purpose: Full-featured scan tool for agricultural, construction, and other off-highway equipment
- Coverage: John Deere, AGCO, CNH (Case/New Holland), and other brands
- Capability: Read/clear fault codes, live data streaming, bi-directional controls, limited calibrations
- Price range: $1,000–$2,500 for hardware + software bundle
- Key limitation: Calibrations and parameter changes that require manufacturer authentication tokens are still blocked without dealer-level access

Source: [CanDo OHV Pro — Diesel Laptops](https://www.diesellaptops.com/products/cando-ohv-pro-off-highway-vehicle-scan-tool) · [Dealer-Level Farm Diagnostic Bundle — Diesel Laptops](https://www.diesellaptops.com/products/dealer-level-farm-and-construction-diagnostic-kit-for-john-deere)

**Jaltest AGV (Agricultural Vehicles)**
- Purpose: Dealer-level diagnostics for agricultural machinery
- Coverage: All major brands — comprehensive multi-make capability
- Capability: Full system access including bi-directional controls, calibrations, ECU configuration for many functions
- Price range: $2,000–$4,000 initial investment; annual subscription fee for updates
- Key advantage: Closest to dealer capability currently available to independent shops

Source: [Jaltest AGV — Abilene Machine](https://www.abilenemachine.com/diagnostics-kit-agricultural-amx36285) · [Jaltest Diagnostics](https://www.jaltest.com/en/diagnostics/jaltest-agv-agricultural-vehicles/)

**Baltic Diagnostics Agricultural Tools**
- Purpose: Brand-specific and all-makes options for tractor diagnostics
- Coverage: Varies by tool; some brand-specific tools provide deeper access for specific manufacturers
- Price range: $500–$2,000
- Key advantage: Lower cost entry for single-brand shops

Source: [Baltic Diagnostics Agricultural Tools](https://www.balticdiag.com/agricultural-machinery-diagnostic-tools/)

**Eco Tractor Tune (Brand-Specific Tools)**
- Provides a comprehensive guide to best diagnostic tools by tractor brand
- Notable for identifying which tools provide the deepest access for specific manufacturers

Source: [Best Diagnostic Tools by Tractor Brand — Eco Tractor Tune](https://ecotractortune.com/the-best-diagnostic-tools-for-each-tractor-brand-a-complete-guide-for-2025/)

### What Diagnostic Tools Can and Cannot Do (Independent Repair Providers)

**Can do today (without dealer tools):**
- Read all stored fault codes across all ECUs
- Clear fault codes after repair
- View real-time sensor data (temperatures, pressures, voltages, RPM)
- Test actuators (fuel injectors, solenoids, EGR valves) in many cases
- Perform calibrations not requiring manufacturer authentication (zero-point calibrations, sensor resets)
- Identify failed components through live data comparison against spec

**Cannot do today without dealer tool access:**
- Reprogram ECUs (replace firmware)
- Unlock software-locked features
- Perform JDLink connectivity resets (John Deere)
- Calibrations requiring manufacturer-issued authorization tokens
- Serial number or equipment configuration changes

**Will be possible by end-2026 (per Deere settlement):**
- Offline reprogramming and calibration through Operations Center PRO Service
- Access to DTAC-level remote diagnostic tools
- Diagnostic and repair without requiring authorized dealer involvement

The gap between "what independent tools can do" and "what dealer tools can do" narrows in the next 12 months if the settlement proceeds as structured. Monitor settlement implementation for actual tool availability.

### Tractor Hacking — Open-Source Diagnostic Projects

The open-source community has developed free diagnostic alternatives, most prominently:

**Tractor Hacking Project** (tractorhacking.github.io)
- Open-source project providing documentation on CAN bus interface for common tractor brands
- Focuses on reading and interpreting CAN bus traffic without proprietary software
- Requires technical comfort with CAN bus tools (e.g., SocketCAN on Linux)
- Legal status: falls within the DMCA Section 1201 agricultural equipment exemption when used for diagnosis and repair on your own equipment

This approach is appropriate for technically capable users who want to understand their equipment without paying for proprietary diagnostic software. It is not a plug-and-play solution.

Source: [Tractor Hacking — GitHub Pages](https://tractorhacking.github.io/usage/)

---

## Part 3: Failure Mode Reference — What Breaks and Why

Understanding the failure modes most likely to ground equipment during planting or harvest allows you to prioritize preventive maintenance and pre-position spare parts. The following covers the failure modes with the highest productivity impact for Zone 5 small and mid-scale farms.

### Diesel Engine Failure Modes

**Most common failures in order of frequency:**

1. **Fuel system contamination** — Diesel fuel degrades over winter storage (Zone 5 winters require winter-blend diesel or treated fuel from October). Microbial contamination (diesel bug) is common in equipment that sits with partially filled tanks. Symptoms: rough running, hard starting, black smoke, power loss. Preventive: treat stored fuel with biocide stabilizer; drain carbs and fuel bowls before storage; change primary and secondary fuel filters at start of season.

2. **Air filter plugging** — Especially acute during harvest (corn dust, chaff). A plugged air filter causes power loss, black smoke, and if severe, can cause engine damage. Check air filter restriction indicator daily during harvest. Keep two spare air filter elements per tractor.

3. **Cooling system failure** — Thermostat failure, coolant pump failure, plugged radiator. Zone 5 summer heat + field dust + long operating hours create stress. Check coolant level, belt condition, and radiator fins weekly during heavy use. Flush and replace coolant every two years regardless of appearance.

4. **Injection pump and injector wear** — These are high-pressure precision components that fail over time, especially with contaminated fuel. Symptoms: misfiring at high load, hard starting, white or blue smoke. Diagnosis requires a pressure tester or injector flow bench. Replacement is expensive ($300–$1,500 per injector; injection pump $1,500–$5,000+).

5. **Glow plug failure** — Affects cold starting for pre-combustion chamber diesels. Zone 5 winters below 0°F make this a real operational issue. Test all glow plugs at the October inspection. Keep spare glow plugs for each engine in your inventory.

Sources: [Common Tractor Issues and Repair Solutions — Crown Power & Equipment](https://crown-power.com/dealer/common-tractor-issues-and-repair-solutions-every-farmer-needs/) · [Tractor Diesel Engine Problems Solved — Bell Performance](https://www.bellperformance.com/bell-performs-blog/tractor-diesel-engine-problems-solved)

### Hydraulic System Failure Modes

Hydraulic failure is the most common reason a tractor becomes operationally useless — implements won't lift, 3-point hitch is inoperable, power steering fails.

**Most common failures in order of impact:**

1. **Low or contaminated hydraulic fluid** — The single most preventable failure. Low fluid levels cause pump cavitation and accelerate wear on all downstream components. Contaminated fluid (water intrusion, metal particles) causes rapid pump, valve, and cylinder failure. Check and record fluid level monthly. Change fluid and filter every 500 hours or annually, whichever comes first. Drain from the lowest point; use particle counting to assess contamination if fluid looks unusual.

2. **Hydraulic pump failure** — Gear pumps (most common on older equipment) wear gradually; piston pumps (modern, high-pressure systems) fail more abruptly. Symptoms: slow lift speed, low operating pressure, whining under load. Diagnosis: measure system pressure at the remote outlet with a test gauge ($50 gauge; spec in service manual). A worn pump will produce low pressure under load.

3. **Control valve wear or sticking** — Spool valves stick from contamination or from corrosion during winter storage. Symptoms: implement drift (slow lowering under load), jerky response, implement moving without input. Partial repair: flush with clean fluid; if sticking persists, valve replacement is required.

4. **Hose and fitting failures** — High-pressure hydraulic hoses fail at fittings from vibration fatigue. Inspect all hoses at seasonal inspection. Replace hoses with any cracking, chafing, or bulging — do not run to failure on high-pressure lines. Keep a hydraulic hose repair kit (fittings and hose sections) in the shop for field emergency repair.

5. **Cylinder seal failure** — O-ring and lip seal degradation causes slow cylinder drift and external leakage. Repair is straightforward if you have seals: disassemble cylinder, replace seals, reassemble. Seal kits are available for virtually all cylinders from aftermarket suppliers ($15–$80 per cylinder depending on size). This is a high-value DIY repair that dealers charge $300–$800 labor for.

Sources: [Hydraulic System Failures in Tractors — Fleet Works](https://www.fleetworksinc.com/articles/hydraulic-system-failures-in-tractors-diagnosis-and-repair-tips) · [Tractor Hydraulics Troubleshooting — Tonys Tractors](https://tonystractors.com/tractor-hydraulics-troubleshooting-your-ultimate-guide.htm) · [Troubleshooting Tractor Hydraulics — Team Tractor & Equipment](https://www.teamtractor.com/blog/troubleshooting-tractor-hydraulics--74797)

### DEF/SCR System Failure Modes (Tier 4 Final Equipment, 2011+)

Diesel Exhaust Fluid systems are the single most disruptive failure mode on modern equipment because DEF inducement — the system that derate or shuts down the engine when DEF quality or levels are inadequate — can halt field operations completely regardless of whether the underlying engine is functional.

**DEF inducement escalation (typical sequence):**
1. DEF level below 10%: warning lamp
2. DEF level below 5%: engine derate to 50% power
3. DEF quality fault sustained: engine derate or shutdown depending on manufacturer

**Common DEF system faults:**

- **DEF sensor contamination or failure** — NOx sensors and DEF quality sensors are reliability problems across all brands. With the EPA's March 2026 guidance removing the requirement for DEF sensor monitoring in certain contexts, farms may now legally operate equipment with a failed DEF sensor without the sensor forcing shutdown — check the specific guidance for your equipment type.

- **DEF pump failure** — Frozen DEF (DEF freezes at approximately 12°F / -11°C) can damage the pump if the heating circuit fails. Zone 5 winters make freeze protection critical. Ensure the DEF system heating circuit is functional before freezing temperatures arrive.

- **DEF crystallization** — Spilled DEF or slow leaks crystallize and block fittings, sensors, and lines. Flushing with warm water dissolves crystite. Address leaks immediately.

- **SCR catalyst degradation** — Long-term performance issue in high-hours equipment. Requires exhaust gas analysis to confirm, and catalyst replacement is expensive ($2,000–$8,000).

**Field workaround (legal — EPA guidance):** Per the February 2026 EPA guidance, temporary override of the inducement system for the purpose of completing a repair (then returning to full compliance) is permissible. This means: if a DEF sensor fails during harvest, a qualified independent repair person can access the inducement system to allow operation while the sensor is sourced and replaced, without violating the Clean Air Act — provided the system is returned to proper function.

**Permanent deletion remains illegal federally.** State enforcement varies, but federal exposure under the Clean Air Act is real. The EPA explicitly confirmed that permanent defeat of DEF/SCR systems is not authorized by their guidance.

Sources: [What does the new DEF guidance mean for farmers? — Farm Progress](https://www.farmprogress.com/farming-equipment/what-does-the-new-def-guidance-mean-for-farmers-) · [EPA Eases DEF Sensor Rules — DTN](https://www.dtnpf.com/agriculture/web/ag/equipment/article/2026/03/30/epa-eases-def-sensor-rules-keeps-def)

### Transmission and Drivetrain Failures

**Wet-clutch transmission (most common on utility tractors under 100 hp):**
- Clutch slip: caused by worn clutch pack or improper fluid (wet clutches require specific UTTO — Universal Tractor Transmission Oil; automotive ATF destroys them)
- Shift difficulty: worn synchros or improper adjustment
- Fluid contamination: most common cause of accelerated drivetrain wear

**Power Shift / CVT (common on 100+ hp modern equipment):**
- Solenoid failures in electrohydraulic control valves: fault codes, erratic shifting; often diagnosable and replaceable by independent shops
- Software calibration required after solenoid replacement in many cases — this is a current limitation for independent repair that the Deere settlement aims to address
- Full transmission failure: rare if fluid maintenance is performed; catastrophic repair cost ($15,000–$50,000) when it occurs

**PTO system:**
- Independent PTO clutch wear: symptoms are slipping under load, slow engagement, or failure to engage; seal and clutch pack replacement is DIY-accessible
- PTO shaft damage from overloads: always use appropriately-rated driveline shafts with overrunning clutches for driven implements

---

## Part 4: Preventive Maintenance — Zone 5 Seasonal Schedule

Cross-reference [04-technology-repair-equipment-protocols.md](../04-technology-repair-equipment-protocols.md) for the general equipment maintenance framework. The following is farm-specific.

### Pre-Season Inspection (March–April)

| System | Task | Time Required | Parts to Pre-Position |
|---|---|---|---|
| Engine | Oil and filter change, check coolant condition | 45 min | Oil, filter, coolant |
| Fuel | Drain any standing fuel from winter; replace primary and secondary filters; check for microbial contamination | 30 min | Primary and secondary fuel filters, biocide treatment |
| Hydraulics | Check fluid level and condition; change if discolored or last changed >12 months | 30 min | Hydraulic filter, UTTO fluid |
| Air | Inspect air filter element; replace if used heavily last season | 15 min | Air filter element |
| Electrical | Check battery voltage (12.6V+ fully charged); clean terminals; check all lights and instruments | 20 min | Battery terminals, dielectric grease |
| Glow plugs | Test each glow plug with circuit tester; replace any that fail | 20 min | Replacement glow plugs |
| DEF system | Check DEF level; inspect pump and heater circuit; check for crystallization at fittings | 20 min | DEF fluid |
| Tires | Check inflation and tread condition; note any cracking on sidewalls | 15 min | n/a |
| Grease points | Grease all fittings; note any stiff or unresponsive points (possible fitting failure) | 30 min | Grease gun, grease cartridges |

### In-Season Checks (May–October)

**Daily during heavy use (planting, cultivation, harvest):**
- Engine oil level
- Coolant level
- Air filter restriction indicator
- Hydraulic fluid level (weekly if no leaks observed)
- DEF level (Tier 4 Final equipment)
- Walk-around inspection for fluid leaks, unusual wear

**Weekly during heavy use:**
- Hydraulic fluid level and condition
- Belt tension and condition
- Grease all PTO and implement attachment points
- Check tire inflation

**After every 50–100 hours of heavy use:**
- Engine oil and filter change (consult service manual for correct interval for your engine)
- Hydraulic filter check (bypass indicator)

### Pre-Winter Storage (October–November)

| Task | Why | Procedure |
|---|---|---|
| Drain fuel from carbureted equipment | Stale fuel causes varnish deposits | Run engine until fuel starvation; add stabilizer to tank |
| Treat diesel fuel in tanks | Prevent microbial growth and gelling | Add winter-grade treatment; use winter-blend diesel |
| Change engine oil | Combustion acids in used oil accelerate corrosion | Change oil and filter before storage |
| Protect exposed metal | Prevent corrosion on 3-point hitch, cylinder rods | Apply light oil or grease to exposed metal surfaces |
| DEF system freeze protection | DEF freezes at 12°F | Confirm heating element function; park in heated space when temperatures approach 0°F |
| Disconnect battery or use tender | Prevent discharge over winter | Trickle charger on battery; or remove and store in warm location |
| Inflate tires to storage pressure | Prevent flat-spotting | Raise to max sidewall pressure if equipment will sit for months |

---

## Part 5: Parts Sourcing — Independent Supply Chain

The most operationally significant aspect of right-to-repair at the community scale is not legal access to software — it is physical access to parts without dependence on a single dealer with a months-long backorder queue during peak season. Parts sourcing strategy should be built before crisis.

### Major Independent Parts Suppliers

**Shoup Manufacturing (shoupparts.com)**
- Scope: Planter, combine, tillage, and other field equipment parts for John Deere, Case-IH, AGCO, and others
- Key strength: Specialty wear parts (planter discs, row cleaners, closing wheels) at 30–60% below OEM
- Best use: High-turnover wear parts that you know you'll use; worth stocking ahead of season

**All States Ag Parts (tractorpartsasap.com)**
- Scope: Used, remanufactured, and new aftermarket parts; tractors, combines, skid steers
- Key strength: Used and reman parts for older equipment where new parts are expensive or discontinued
- Best use: Major components (engines, transmissions, pumps) where OEM price is prohibitive

**Sparex (us.sparex.com)**
- Scope: Broad range of tractor parts — engine, transmission, hydraulics, electrical, bodywork
- Key strength: UK-based origin means good coverage for European brands (Massey Ferguson, Fendt, Landini) uncommon in US dealer networks
- Best use: Mixed-brand fleets; good catalog for older Massey Ferguson and older Case equipment

**Worthington Ag Parts (worthingtonagparts.com)**
- Scope: Non-OEM aftermarket and used parts
- Key strength: Competitive pricing; good for older equipment
- Best use: Budget repair of older iron where cosmetics are irrelevant

**Abilene Machine (abilenemachine.com)**
- Scope: Aftermarket agricultural parts; also carries diagnostic equipment
- Key strength: Broad catalog; good for less common older brands
- Best use: Parts for 1970s–1990s vintage equipment that OEM networks have deprecated

**A&I Products** (available through multiple distributors)
- Scope: OEM-quality aftermarket replacement parts for agricultural, turf, and industrial equipment
- Key strength: Manufacturer-grade quality without OEM markup; used by independent dealers
- Best use: Drivetrain and wear parts where quality matters

Sources: [Shoup](https://www.shoupparts.com/) · [All States Ag Parts](https://www.tractorpartsasap.com/) · [Sparex](https://us.sparex.com/) · [Worthington Ag Parts](https://www.worthingtonagparts.com/) · [Abilene Machine](https://www.abilenemachine.com/)

### Community-Scale Parts Strategy

For a community of 20–100 households with shared agricultural equipment, a coordinated parts inventory dramatically reduces risk compared to each household trying to source parts during a crisis:

**Tier 1 — Consumables (always in stock):**
- Engine oil, 5W-30 and 15W-40 in appropriate quantities (5+ gallons per tractor per season)
- Engine oil filters (2+ per tractor model in use)
- Fuel filters — primary and secondary (2+ sets per engine)
- Air filter elements (2+ per tractor in use)
- Hydraulic filters (1–2 per tractor)
- Grease cartridges (5+ for community shop)
- DEF fluid (5+ gallons per Tier 4 tractor)
- Glow plugs (full set per engine type)
- V-belts in the most common sizes for your equipment (2 of each)

**Tier 2 — Failure-probability parts (keep 1 set on hand):**
- Thermostat for each engine model in use
- Water pump impeller or full pump for each engine
- Hydraulic pump seal kit for each pump type
- Hydraulic cylinder seal kits for each cylinder in use
- Injector sealing washers (copper washers under injectors — cheap and frequently needed)
- Solenoid valves for hydraulic control (if known failure mode on your equipment)

**Tier 3 — Major components (negotiate lead time, don't stock):**
- Hydraulic pump (price and source, do not stock unless cash permits)
- Fuel injection pump (same)
- Alternator and starter (rebuild vs. new — often faster to rebuild locally)

**Cost guidance:** Tier 1 community inventory for 3–4 tractors costs approximately $500–$1,500 in consumable stock. Tier 2 runs $800–$2,500 depending on equipment complexity. Budget this as insurance, not inventory — use it, rotate it, don't let it sit for 5 years.

### Cost Comparison: Dealer vs. Independent vs. DIY

| Repair | Dealer Cost | Independent Shop | DIY with Right Parts |
|---|---|---|---|
| Engine oil and filter change | $80–$150 labor | $50–$80 | $30–$60 in parts |
| Hydraulic filter and fluid change | $120–$200 | $80–$120 | $40–$80 in parts |
| Hydraulic cylinder re-seal | $300–$800 | $150–$350 | $15–$80 in seals |
| Glow plug replacement (all 4) | $200–$400 | $100–$200 | $30–$80 in plugs |
| Fuel filter replacement | $80–$150 | $50–$80 | $15–$40 in parts |
| DEF sensor replacement | $400–$800 | $200–$400 | $100–$250 in parts |
| Fault code read and clear | $150–$300 service call | $80–$150 | $0 if you own a tool |
| Hydraulic pump rebuild | $2,000–$5,000 | $800–$1,800 | $200–$600 in parts (skill-intensive) |

The pattern is consistent: labor at authorized dealers runs 2–4× independent shop rates, which run 3–5× DIY parts cost. The constraint on DIY is skill and diagnostic capability, not parts availability for most common repairs. The Deere settlement's diagnostic tool access provision, when implemented, directly addresses the diagnostic capability gap.

---

## Part 6: OBD/CAN Security — Cross-Reference to Cybersecurity

This section cross-references the cybersecurity-hardening domain (see parallel security documentation in this project).

Modern farm equipment with CAN bus connectivity and JDLink / AFS Connect (John Deere / CNH) telematics presents genuine cybersecurity attack surfaces. Relevant threat vectors:

**Telematics platform compromise:** Deere's Operations Center and CNH's AFS Connect store machine data (location, operating hours, fuel consumption, fault history) in cloud infrastructure. Compromise of these platforms could expose farm operational data, machine location, or potentially allow remote commands to equipment if the telematics gateway has write access. In a societal disruption scenario, these platforms may be unavailable or unreliable.

**CAN bus injection attacks:** Physical access to a machine's diagnostic port (or a compromised telematics connection) allows injection of CAN bus messages that can command actuators or falsify sensor data. This is primarily relevant in organized adversarial contexts — not a common threat for most farm operations. However, in a post-disruption scenario with higher-stakes resource competition, machine theft or sabotage via CAN bus is a non-trivial risk.

**Practical countermeasures:**
- Disable remote telematics access if not actively monitored (reduces cloud attack surface)
- Secure physical access to diagnostic port (cab lockout when not in use)
- Do not connect proprietary diagnostic tools to untrusted computers
- For community-shared equipment: establish a documented key/access control procedure

The primary security value of right-to-repair here is actually defensive: if you understand your own machine's communication architecture, you can identify anomalous behavior (unexpected fault codes, unusual telematics events) that might indicate tampering. This knowledge was previously monopolized by dealers.

---

## Part 7: Practical Implementation Path for Zone 5

### Year One (2026)

1. **Audit your equipment.** Inventory every piece of farm equipment, its model year, whether it has Tier 4 Final emissions controls (2011+ for >25 hp equipment), and its known maintenance history. Identify gaps.

2. **Establish a parts inventory.** Using the Tier 1 list above, build a 12-month consumable inventory for each tractor or major piece of equipment in your operation. Store in a cool, dry location. Label clearly with equipment model and part number.

3. **Invest in basic diagnostic capability.** At minimum, a quality code reader for your specific equipment (John Deere: EDL-compatible adapter; multi-brand: CanDo or Jaltest). The ability to read fault codes yourself eliminates the $150–$300 dealer "diagnostic fee" for every fault code event.

4. **Print service manuals.** For every piece of equipment you own, obtain and print the operator manual and service manual. John Deere's TechCD / Service Advisor may become accessible via the settlement by end-2026, but print what you can now from official and archive sources. Manuals go into the community shop reference library (see [04-technology-repair-equipment-protocols.md](../04-technology-repair-equipment-protocols.md)).

5. **Establish an independent repair relationship.** Find an independent repair shop familiar with your equipment brands before you need them urgently. Establish a relationship, know their capabilities, and understand their parts sourcing approach.

6. **Train.** Agricultural extension programs (Iowa State, University of Illinois, Purdue) continue to offer tractor maintenance workshops. Attend at least one hands-on event before crisis. The skills gap — not the parts gap or the legal gap — is the primary limit on DIY repair capability.

### Monitor (2026 Q4)

Watch for two things:
- John Deere's Operations Center PRO Service offline diagnostic capability (promised by December 31, 2026 per settlement)
- Final court approval of the $99M settlement at the October 29, 2026 fairness hearing

If the settlement is approved and tools become available, revise the diagnostic tool investment accordingly — dealer-tier access at lower cost changes the calculus for some repairs.

---

## Sources

1. [John Deere and Right to Repair over the years — PIRG](https://pirg.org/resources/john-deere-and-right-to-repair-over-the-years/)
2. [John Deere Paying Nearly $100 Million In Right-to-Repair Settlement — The Truth About Cars](https://www.thetruthaboutcars.com/cars/news-blog/john-deere-paying-nearly-100-million-in-right-to-repair-settlement-45134824)
3. [Deere Settles Class Action Right-to-Repair Lawsuit — Farm Policy News Illinois](https://farmpolicynews.illinois.edu/2026/04/deere-settles-class-action-right-to-repair-lawsuit/)
4. [Right-to-Repair Momentum Continues with John Deere Settlement — Reinhart Law](https://www.reinhartlaw.com/news-insights/right-to-repair-momentum-continues-with-john-deere-settlement)
5. [John Deere's $99 Million Settlement and the Accelerating State Right-to-Repair Landscape — Arnold & Porter](https://www.arnoldporter.com/en/perspectives/blogs/consumer-products-and-retail-navigator/2026/04/john-deeres-99-million-settlement-and-the-right-to-repair-landscape)
6. [John Deere settles right-to-repair lawsuit for $99 million — Farm Progress](https://www.farmprogress.com/farming-equipment/john-deere-settles-right-to-repair-lawsuit-for-99-million)
7. [Right-to-repair advocates score a small win at John Deere's expense — Investigate Midwest](https://investigatemidwest.org/2025/07/08/right-to-repair-advocates-score-a-small-win-at-john-deeres-expense/)
8. [Federal Court Gives Preliminary Approval to $99 Million John Deere Settlement — American Ag Network](https://www.americanagnetwork.com/2026/05/20/federal-court-gives-preliminary-approval-to-99-million-john-deere-right-to-repair-settlement/)
9. [John Deere's $99 Million Right-to-Repair Settlement Gets Preliminary Court Approval — DTN](https://www.dtnpf.com/agriculture/web/ag/equipment/article/2026/05/18/john-deeres-99-million-right-repair)
10. [EPA Advances Farmers' Right to Repair Their Own Equipment — US EPA](https://www.epa.gov/newsreleases/epa-advances-farmers-right-repair-their-own-equipment-saving-repair-costs-and)
11. [EPA Sets Record Straight — Americans Have the Right to Repair Their Farm Equipment — US EPA](https://www.epa.gov/newsreleases/icymi-epa-sets-record-straight-americans-have-right-repair-their-farm-or-other-nonroad)
12. [EPA Affirms Farmers' Right to Repair Equipment — Farm Policy News](https://farmpolicynews.illinois.edu/2026/02/epa-affirms-farmers-right-to-repair-equipment/)
13. [EPA Guidance Allows Farmers to Repair Equipment Emissions — DTN](https://www.dtnpf.com/agriculture/web/ag/equipment/article/2026/02/02/trump-epa-declares-farmers-can)
14. [EPA Eases DEF Sensor Rules — DTN](https://www.dtnpf.com/agriculture/web/ag/equipment/article/2026/03/30/epa-eases-def-sensor-rules-keeps-def)
15. [EPA's New Guidance Removes Requirement for DEF Sensors — US EPA](https://www.epa.gov/newsreleases/icymi-epas-new-guidance-removes-requirement-diesel-exhaust-fluid-def-sensors-saves)
16. [The State of Right to Repair — PIRG](https://pirg.org/edfund/resources/the-state-of-right-to-repair/)
17. [Right to Repair Laws Have Now Been Introduced in All 50 US States — iFixit](https://www.ifixit.com/News/108371/right-to-repair-laws-have-now-been-introduced-in-all-50-us-states)
18. [John Deere Really Doesn't Want You to Own That Tractor — EFF](https://www.eff.org/deeplinks/2016/12/john-deere-really-doesnt-want-you-own-tractor)
19. [How Copyright Enabled John Deere to Restrict Farmers' Right to Repair — Captured Economy](https://capturedeconomy.com/how-copyright-enabled-john-deere-to-restrict-farmers-right-to-repair/)
20. [Deere Promised Farmers the Right to Repair. Can We Trust Them? — iFixit](https://www.ifixit.com/News/70877/deere-promised-farmers-the-right-to-repair-can-we-trust-them)
21. [Tractor Hacking — GitHub Pages](https://tractorhacking.github.io/usage/)
22. [CanDo OHV Pro — Diesel Laptops](https://www.diesellaptops.com/products/cando-ohv-pro-off-highway-vehicle-scan-tool)
23. [Jaltest AGV — Abilene Machine](https://www.abilenemachine.com/diagnostics-kit-agricultural-amx36285)
24. [Best Diagnostic Tools for Each Tractor Brand — Eco Tractor Tune](https://ecotractortune.com/the-best-diagnostic-tools-for-each-tractor-brand-a-complete-guide-for-2025/)
25. [Hydraulic System Failures in Tractors — Fleet Works](https://www.fleetworksinc.com/articles/hydraulic-system-failures-in-tractors-diagnosis-and-repair-tips)
26. [Tractor Hydraulics Troubleshooting — Tonys Tractors](https://tonystractors.com/tractor-hydraulics-troubleshooting-your-ultimate-guide.htm)
27. [Shoup Manufacturing](https://www.shoupparts.com/)
28. [All States Ag Parts](https://www.tractorpartsasap.com/)
29. [Ongoing Coverage: Right-to-Repair Impact on Dealers, Deere, OEMs — Farm Equipment](https://www.farm-equipment.com/articles/20002-ongoing-coverage-right-to-repair-impact-on-dealers-deere-other-oems)
30. [John Deere ECU Repair — OBDII Shop Blog](https://blog.obdii.shop/john-deere-ecu-repair/)

---

*Confidence level: High on legal status (primary sources from EPA and court records); Medium on specific settlement implementation details (not yet finalized); High on failure modes and parts sourcing (well-documented across multiple independent technical sources). Monitor John Deere's Operations Center PRO Service announcement for settlement implementation updates after October 2026 fairness hearing.*
