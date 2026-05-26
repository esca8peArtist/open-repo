---
title: "Phase 6 Wave 1 Research Outline — Farm Equipment & Communication Infrastructure"
project: systems-resilience
phase: 6
wave: 1
status: FOUNDATION-COMPLETE — ready for June 1 decision
version: 2
purpose: "Structural outline + bibliography for Phase 6 Track A (Farm Equipment Repair) and Track B (Meshtastic Mesh Networking). Foundation work for June 1 user decision on Phase 5 Wave 2 sequencing."
created: 2026-05-26
word_count: ~4200
decision_window: 2026-06-01
activation_target: 2026-06-01 to 2026-06-15
cross_references:
  - phase-6/farm-equipment-repair-research.md
  - phase-6/phase-6-farm-equipment-repair-right-to-repair.md
  - phase-6/meshtastic-community-networking-research.md
  - phase-6/phase-6-meshtastic-lora-mesh-networking.md
  - phase-6/farm-equipment-prioritization-matrix.csv
  - PHASE_6_COMMUNICATION_INFRASTRUCTURE_SCOPING.md
  - PHASE_5_WAVE_2_PHASE_6_EXECUTION_SEQUENCING.md
---

# Phase 6 Wave 1 Research Outline
## Track A: Farm Equipment Repair Guide + Track B: Meshtastic Mesh Networking

> **Lead finding across both tracks**: The documentation problem for Zone 5 agricultural self-sufficiency is already solved — Archive.org, ATTRA/NCAT, university extension systems, and FarmHack collectively provide free coverage of almost every equipment category a 20–100 household community needs. The unsolved problem is pre-crisis skill development embedded in the community calendar. For mesh networking, Meshtastic's June 2025 cryptographic vulnerabilities (CVE-2025-52464, CVSSv4 9.5) were patched in v2.6.11 and are no longer a blocker for deployment, but every community starting in 2026 must run firmware v2.6.11 or later and regenerate all PKI keys. Both tracks are execution-ready for a June 1 launch decision.

---

## Status Summary

| Item | Status |
|---|---|
| Track A pre-research (farm equipment) | COMPLETE — 3 documents, 44,000+ words, 78 sources |
| Track B pre-research (Meshtastic) | COMPLETE — 2 documents, 15,600+ words, 71 sources |
| Right-to-repair legal landscape (Track A) | COMPLETE — April 2026 Deere $99M settlement + EPA Feb 2026 guidance |
| Zone 5 hardware selection (Track B) | COMPLETE — 5 hardware platforms compared |
| June 1 decision package | READY |
| Phase 6 activation sequence | Documented in PHASE_5_WAVE_2_PHASE_6_EXECUTION_SEQUENCING.md |

---

## Track A: Farm Equipment Repair Guide

### Introduction: Why Agricultural Self-Sufficiency Requires Repair Skills

The single most important finding in the pre-research: the documentation gap has closed. The skill gap has not.

Farm equipment repair costs rose 41% between 2020 and 2023. The April 2026 John Deere $99 million class-action settlement and the EPA's February 2026 guidance affirming farmers' right to repair emissions systems together removed two of the largest legal barriers to independent repair — but the diagnostic software Deere promised to provide will not be available until December 31, 2026 at the earliest, and the settlement has not yet received final court approval (fairness hearing: October 29, 2026).

The operational implication: a community depending on farm equipment for food production cannot wait for the legal and regulatory landscape to finish evolving. Equipment fails during planting (Zone 5 corn planting window: May 1–20) and harvest (wheat: July; corn: October). Downtime during those windows has outsized productivity consequences. Communities must build repair capability now, before crisis, with the resources already available — which are extensive.

**Why supply chain fragility makes this urgent:**
- Dealer service backlogs: 4–8 weeks during peak season is documented; independent repair shops have partially filled the gap but carry their own capacity constraints
- Parts lead times for specialty hydraulic components, injectors, and electronic components have extended since 2020 supply chain disruptions
- Replacement equipment costs have risen 40–60% since 2019 for new equipment; used equipment markets tightened through 2024
- A community with repair skill turns a $3,000 dealer repair (or a 6-week wait) into a $400 parts cost and two days of community labor

**Scope justification for Zone 5:**
A 20–100 household community in Zone 5 (northern Illinois, Iowa, southern Wisconsin, Indiana, Ohio) operating 10–50 cultivated acres requires a shared fleet of 5–12 equipment categories. This outline covers the repair knowledge architecture for three of the highest-consequence categories: hand tools (fail silently and accumulate into productivity loss), small equipment (tillers, chainsaws, pressure washers — high repair frequency, moderate parts cost), and hydraulic systems (tractor-critical; failure grounds the entire implement-dependent work program).

---

### Section 1: Hand Tools

**Scope and importance for Zone 5**: Hand tools are the gap-fillers in any mechanized system — they handle the work that tillers and tractors cannot reach, and they are the fallback when mechanized equipment is down. A community with sharp, functional hand tools loses less productivity to equipment downtime. The total cost to restore a degraded hand tool inventory is typically $20–$80 per tool in parts; the skill barrier is low.

**1.1 Wood-Working Tools** (chisels, planes, saws, mallets)
- Common failures: dull edges (chisels, planes), cracked handles (all), set drift in hand saws, loose mallet heads
- Diagnostic: visual edge inspection, handle flex test, saw set test against straight edge
- Repair: bench stone sharpening protocol (Norton combination India stone, then strop), handle replacement (ash or hickory stock, $8–$20, hardware store), saw set with a saw set tool, mallet head soaking to re-tighten
- Parts sourcing: Ace Hardware, Lee Valley, Woodcraft; handle blanks at any lumber yard
- Cost-benefit: A $6 handle blank and 30 minutes restores a $40–$80 tool; replacement threshold only at structural cracks through the socket or ferrule

**1.2 Soil-Working Tools** (broadfork, wheel hoe, hoe, rake)
- Common failures: bent broadfork tines, wheel hoe blade dulling and rust, broken hoe handles, loose rake tines
- Diagnostic: tine straightness check (lay broadfork flat, sight down tines), blade sharpness scratch test on thumbnail, handle integrity flex test
- Repair: bent tines — clamp, heat with propane torch, pound back to alignment; wheel hoe blade — mill bastard file, 10–15 degree bevel, followed by rust removal with wire wheel and WD-40 protective coat; rake tine replacement (riveted: drill out rivet, replace with equivalent, peen new rivet)
- Parts sourcing: Valley Oak Tool Company (broadfork parts), Johnny's Selected Seeds, Hoss Tools; generic handles at any farm supply

Sources: [Valley Oak Tool Broadfork and Wheel Hoe Maintenance](https://www.valleyoaktool.com/blogs/news/broadfork-and-wheel-hoe-maintenance) · [UF/IFAS Sharpening Your Tools](https://gardeningsolutions.ifas.ufl.edu/care/tools-and-equipment/sharpening-your-tools/) · [EasyDigging Hoe Sharpening Guide](https://www.easydigging.com/garden-hoes/articles/how-to-sharpen-hoe.html)

**1.3 Pruning Tools** (pruners, loppers, pruning saws)
- Common failures: blade dulling, pivot bolt wear (slop in cut), sap accumulation, broken springs
- Repair: diamond file sharpening on bypass pruner beveled blade (flat side on flat, bevel side at existing angle), Felco pivot bolt replacement (spare bolt + nut, $4), isopropyl or Lestoil cleaning for sap, spring replacement
- Parts sourcing: Felco parts available directly from felco.com, A.M. Leonard; Bahco replacement parts at most hardware suppliers
- [RESEARCH NEEDED]: Long-term durability data comparing carbon steel vs. stainless pruner blades in Zone 5 high-humidity harvest-season conditions

**1.4 Digging Tools** (shovels, spades, post-hole diggers, mattocks)
- Common failures: bent blade (overloaded in rocky soil), cracked or loose handles, dulled digging edge
- Repair: bent blade — straighten in vise or with pipe-over-handle leverage if bend is minor; handle — hickory replacement handles at farm supply; sharpen digging edge with angle grinder or mill file at 45 degrees
- Parts sourcing: True Temper handles at most hardware stores; Seymour at Amazon or direct

**1.5 Fastening Tools** (hammers, wrenches, screwdrivers, ratchets)
- Common failures: loose hammer heads, stripped screwdriver tips, ratchet pawl wear, corrosion on open-end wrenches
- Repair: hammer head — soak handle in water overnight, wood swells; replace handle if cracked (straight grain hickory); screwdriver tips — regrind on bench grinder if tips are large enough; ratchet mechanism — open, clean, regrease with white lithium grease; corrosion — wire wheel + WD-40

**1.6 Measuring Tools** (tape measures, levels, squares, marking gauges)
- Common failures: tape measure spring failure, bubble loss in levels, square drift from impact
- Repair: tape measure — replacement internal spring kits exist for Stanley and Milwaukee (not cost-effective; replace the unit at $8–$15); level — bubbles cannot be refilled without specialized equipment; square recalibration against known flat reference
- Note: Measuring tools are typically replace-rather-than-repair at community scale; maintain one reference quality square and level as calibration standard

**1.7 Cutting Tools** (knives, draw knives, axes, hatchets)
- Common failures: edge rolling (knives), dull axes, cracked or loose handles
- Repair: axes — file or grinder to restore convex primary bevel, strop to finish; draw knife — whetstone at low angle; handles — replace with straight-grain ash, use wedge-and-peen method (traditional) or wood glue + wedge for temporary fix
- Parts sourcing: Council Tool, Gransfors Bruk, and Hults Bruk all sell replacement handles; any hardwood lumber yard for blanks

**1.8 Specialty Tools** (seeders, soil blockers, pot dibbles, paper pot planters)
- Common failures: seeder disc clogging and wear, soil blocker compression surface damage, dibble tip wear
- Repair: seeder — disassemble, clear disc cells with compressed air or small wire, oil moving parts; soil blocker — resurface compression faces with metal epoxy if dented; dibble — sharpen on grinder or replace (most dibbles are $3–$8 to replace)
- [RESEARCH NEEDED]: Parts availability for paper pot transplanter spare parts (Japanese-manufactured; US parts network is thin)

---

### Section 2: Small Equipment

**Scope**: Small equipment (sub-tractor scale) is the bridge between hand tools and full tractor implement work. Tillers and cultivators handle seedbed preparation for intensive beds; chainsaws handle wood and brush management; pressure washers handle equipment cleaning critical to preventing corrosion and blockage. These are typically gasoline or electric powered, mechanically simpler than tractors, and repairable with moderate skill.

**2.1 Tilling Equipment** (walk-behind tillers, rotary tillers)
- Seasonal maintenance: pre-season (April) — oil change, air filter, spark plug, blade inspection; post-season (November) — fuel stabilizer or drain fuel, blade cleaning and rust prevention, tine sharpening
- Common failures: tine wear (normal, replace at 50% width loss), belt wear and breakage (common on rear-tine tillers), transmission oil leak (gear housing seals), carburetor issues after storage
- Repair procedures: tine replacement (unbolt from flanged hub, replace, torque to spec); belt replacement (route per diagram in manual — critical step; wrong routing causes premature wear); carburetor rebuild (float bowl, needle valve, main jet — $15–$25 kit covers 90% of carb failures)
- Parts compatibility matrix: BCS and Grillo tillers have the best parts networks in the US (direct from importers); Honda and Briggs & Stratton engines have universal carburetor kits at any small engine supplier
- Supplier relationships: Northern Tool, DR Equipment, BCS America for brand-specific parts; Hipa Store, Stens, Oregon Parts for generic small engine consumables

Sources: [Family Handyman Small Engine Maintenance](https://www.familyhandyman.com/article/pro-small-engine-maintenance-tips/) · [Homestead Small Engine and Equipment Repair](https://homesteadsmallenginerepair.com/)

**2.2 Spreading Equipment** (broadcast spreaders, drop spreaders, wheelbarrow spreaders)
- Common failures: corroded agitator shaft, worn spreader gate, cracked hopper (UV degradation), impeller failure
- Repair: shaft corrosion — disassemble, wire brush, recoat with zinc cold galvanizing compound; gate — inspect for cracks or warp, replace with manufacturer part or fabricate from sheet aluminum; hopper cracks — epoxy or plastic welding for cosmetic cracks; structural cracks in load-bearing sections are replace conditions

**2.3 Cutting Equipment** (sickle bar mowers, flail mowers, walk-behind mowers)
- Seasonal maintenance: blade sharpening (annually minimum), deck cleaning (after each use in wet conditions to prevent rust accumulation), blade balance check after sharpening
- Common failures: blade impact damage (strikes rocks), blade bolt failure, belt wear, PTO shaft universal joint wear
- Repair: blade sharpening — angle grinder or bench grinder at factory bevel angle (consult manual; typically 25–35 degrees); blade balance — balance gauge or nail through center hole; belt replacement — measure, order by cross-section (A, B, or 5L) and length; PTO U-joint replacement — requires snap ring pliers

**2.4 Pressure Equipment** (pressure washers, pump sprayers)
- Common failures: pump seal failure (most common; manifests as pressure loss), unloader valve wear, nozzle clogging, crankcase oil failure (ignored — catastrophic pump failure)
- Repair: seal replacement — pump seal kits by brand are $20–$40 (General, AR, Cat pumps all have aftermarket kits); unloader valve — replace as a unit if pressure won't hold; nozzle — replace at $5–$8 each (have spares); oil — check every 50 hours
- Parts sourcing: Pressure Washer Products (pwproducts.com), Repair Clinic, Amazon for brand kits
- [RESEARCH NEEDED]: Pump freeze damage prevention protocols for Zone 5 winter storage (below-freezing temperatures destroy pump manifold if water is not fully purged)

**2.5 Chain Equipment** (chainsaws, pole saws)
- Seasonal maintenance: chain sharpening (every 3–5 hours of cutting), bar groove cleaning, sprocket wear check, air filter cleaning (every use in dirty conditions), chain oil and fuel mix check
- Common failures: carburetor failure after storage (ethanol degrades fuel system components), chain stretch, bar groove wear, clutch slippage
- Repair: carburetor rebuild — standard Walbro or Zama carb rebuild kit ($8–$20); chain sharpening — round file at correct diameter for chain pitch (stamped on chain drive links); chain replacement — measure pitch and gauge, replace chain before bar groove is worn to avoid bar replacement; bar groove cleaning — specialized tool or small flat screwdriver; sprocket replacement when teeth are hooked

Sources: [Sears Parts Direct Chainsaw Carburetor Rebuild](https://www.searspartsdirect.com/diy/repair-guide/how-to-rebuild-a-chainsaw-carburetor) · [Briggs & Stratton Carburetor Rebuild FAQ](https://www.briggsandstratton.com/en-gb/support/faqs/carburetor-rebuild) · [Hipa Store Carburetor Cleaning Guide](https://www.hipastore.com/blogs/diy-tips/how-to-clean-and-rebuild-a-carburetor-for-optimal-small-engine-functionality)

**2.6 Fuel System Equipment** (fuel storage tanks, transfer pumps, hand pumps)
- Common failures: gasket degradation (ethanol compatibility), pump diaphragm failure, tank corrosion (steel tanks)
- Repair: gasket replacement (Viton or nitrile for ethanol resistance; standard neoprene degrades rapidly with E10+ fuels); diaphragm pump rebuild (rebuild kits available for all major brands); tank corrosion — treat interior with POR-15 fuel tank sealer for steel; plastic tanks — replace
- [RESEARCH NEEDED]: Long-term storage protocols for ethanol-blend fuels in Zone 5 temperature cycling conditions

---

### Section 3: Hydraulic Systems

**Scope and criticality**: Hydraulic systems are the highest-consequence failure category for tractor-dependent operations. A tractor with a failed hydraulic system cannot lift the 3-point hitch, cannot engage hydraulic PTO functions, and cannot operate any hydraulically driven implement. Hydraulic failure during planting or harvest season is effectively a total work stoppage for everything depending on that tractor.

**3.1 Understanding Hydraulics — The Foundation**
- Hydraulic system architecture on a small tractor: reservoir → pump → pressure relief valve → control valves → cylinders/motors → return filter → reservoir
- Key diagnostic principle: hydraulic problems are almost always one of three things — low fluid, contaminated fluid, or seal failure. External leaks are obvious; internal bypassing (seals worn but no visible leak) is the harder diagnostic
- Zone 5 note: hydraulic fluid viscosity matters in winter operation; thin fluid specification for cold starts prevents cavitation damage
- Tools needed: pressure gauge set (0–3,000 PSI, $150–$400), flow meter (optional, $400+), clean work surface or mat, seal pick set, snap ring pliers
- Primary diagnostic procedure: measure system pressure at a test port against manufacturer specification; if pressure is within spec, problem is downstream (cylinder or control valve); if below spec, problem is upstream (pump, relief valve, or severe internal bypass)

Sources: [Hercules Sealing Products — Hydraulic Seals](https://herculesus.com/) · [Agri Supply — Hydraulic Cylinder Seal Kits](https://www.agrisupply.com/seal-kits/c/2500014/) · [Hydraulic Cylinders Inc — Seal Installation Guide](https://www.hydrauliccylindersinc.com/installation-of-hydraulic-cylinder-seals/)

**3.2 Pressure Systems — Troubleshooting and Adjustment**
- Pressure relief valve: the pressure ceiling for the system; overpressure relief valve failure (stuck closed) causes hose rupture; stuck open causes no-lift condition
- Diagnostic: attach gauge to test port; cycle the hydraulic function; read operating pressure; compare to spec in service manual
- Adjustment: most tractors have an accessible relief valve adjustment screw; turning in (clockwise) increases pressure setpoint; document original position before any adjustment
- Control valve wear: spool valves wear and bypass internally; manifests as slow cylinder operation and fluid heating; test by measuring pressure drop across valve
- [RESEARCH NEEDED]: Hydraulic pump bypass threshold specifications for common Zone 5 small tractor models (John Deere 2000/3000 series, Ford 3000–5000, IH 300–504)

**3.3 Seals and Hoses**
- Seal failure modes: abrasion (dirt ingestion past wiper seals), extrusion (operating above pressure rating), chemical incompatibility (wrong fluid type), thermal degradation (Zone 5 cold start without warm-up)
- Seal material guide: Buna-N (nitrile) — standard petroleum hydraulic fluid, -40°F to 250°F, adequate for Zone 5; Viton (FKM) — biodegradable hydraulic fluid, higher temperature, higher cost ($2–$5× premium)
- Seal replacement procedure (cylinder): release all pressure; remove cylinder from equipment; drain fluid; secure rod in vise; remove gland nut (large spanner wrench or pipe wrench); remove rod from barrel; replace all seals in seal kit (do not replace one seal; kit cost is $20–$50 and replacing all prevents repeat teardown); lubricate seals with clean hydraulic fluid before assembly; reassemble; test at low pressure first, then cycle 10 times to seat seals; test at operating pressure; check for leaks
- Hose repair: hydraulic hoses above 1,500 PSI working pressure are not field-spliced; they are replaced. A hose fabrication shop (Parker Hannifin distributors, Hydraulic Plus) can cut to length and crimp ends in 1–2 hours for $40–$120. Have hose dimensions and thread specifications (SAE or NPT) before the call.
- [RESEARCH NEEDED]: Hydraulic seal material chemistry under Zone 5 cold-temperature cycling — specific elastomer behavior at -10°F to -20°F

Sources: [NOK CN Seals — Guide for Replacing Seals on Hydraulic Cylinders](https://www.nokcn-seals.com/resources/guide-for-replacing-seals-on-hydraulic-cylinders.html) · [AHS Hydraulics — How to Replace Hydraulic Cylinder Seals](https://feeds.ahshydraulics.com/blog/replace-seals-hydraulic-cylinder) · [Blince — Hydraulic Cylinder Repair Handbook](https://www.blince.com/Hydraulic-Cylinder-Repair-Guide-A-Handbook-for-Hydraulic-Cylinder-Seal-Replacement-id48542996.html)

**3.4 Fluid Management**
- Zone 5 fluid selection: most pre-1990 tractors use hydraulic-transmission fluid (sharing a common sump for both functions); correct spec is critical — using a tractor that calls for Hy-Gard with generic AW-46 will cause wet-clutch slippage; always verify from the service manual
- Fluid degradation indicators: milky appearance (water contamination, typically condensation from temperature cycling or a seal failure at the cylinder); dark color and burnt smell (oxidation from overheating); metallic particles in filter (worn pump or cylinder — take oil sample for particle analysis)
- Fluid change schedule: every 500 operating hours or 2 years minimum; Zone 5 winter storage — change before storage, not after; old fluid contains combustion byproducts and acids that concentrate during storage
- [RESEARCH NEEDED]: Cold-start hydraulic flow rate data for Zone 5 January conditions — what warm-up time is needed before full hydraulic load to prevent cavitation in common small tractor pump designs

**3.5 Emergency Field Repairs**
- What can be field-repaired: hose blowout at a fitting (cut hose short of damaged end, re-crimp in shop if fittings are undamaged; or use a hydraulic hose repair kit with reusable fittings for temporary repair); external cylinder leak at wiper seal (temporary packing with Rescue Tape + hydraulic stop-leak can extend function for 4–8 hours; treat as 1-time emergency measure, not ongoing repair)
- What cannot be field-repaired: pump failure (requires shop teardown), control valve bypassing (requires bench work and shimming), internal cylinder damage (requires full teardown)
- Field repair kit for Zone 5 tractor: 1 qt hydraulic fluid, hose repair kit with reusable fittings (1/4" and 3/8" SAE), Rescue Tape (silicone self-fusing), hydraulic stop-leak (last resort), pressure gauge, clean rags and nitrile gloves, flashlight
- Decision framework: if the field repair holds full pressure for one complete operating cycle (lift, extend, hold, lower), it is acceptable for completing the current task. Plan the permanent repair for that evening.

---

### Section 4: Parts Sourcing Strategy

**Supplier relationships — Zone 5 priority stack:**
1. **Shoup Manufacturing** (shoupparts.com) — aftermarket and OEM-equivalent parts for major brands; strong in tillage, planting, and harvesting components; same-day UPS shipping from Kansas
2. **All States Ag Parts** (tractorpartsasap.com) — used, rebuilt, and new parts; strong in tractor mechanical and hydraulic; salvage yard database
3. **Yesterday's Tractors** (yesterdaystractors.com) — community forum for pre-1990 tractor parts sourcing; classifieds with community validation
4. **Hydraulic Plus / Parker Hannifin distributors** — hose fabrication; most Midwest cities have at least one location
5. **Stens / Oregon / Rotary** — OEM-equivalent small engine parts; available through Northern Tool, Stens distributors

**Lead times and strategic stocking:**
- Air, oil, and fuel filters: stock 2 years' worth per tractor (cost: $80–$150/year/tractor; storage: 1 shelf space)
- Hydraulic fluid: stock 2 full changes per tractor (typically 6–8 gallons; about $80–$120 per change)
- Belts: measure and number all belts on each piece of equipment; stock one spare of each critical belt (tiller drive belt, PTO belt, combine reel belt)
- Seal kits: order cylinder seal kits for all cylinders on the primary tractor in advance; seal kits do not degrade in storage

**Supply chain fragility mitigation:**
- Identify two suppliers for every critical consumable before need arises
- Maintain a parts log: part number, supplier, last restock date, current quantity
- Build supplier relationships before crisis; a dealer who knows you does not leave you at the back of the queue during peak service season
- Pre-1995 equipment (pre-Tier 4 diesels) generally has better aftermarket parts availability and simpler diagnostics; this is a deliberate resilience strategy, not nostalgia

---

### Section 5: Cross-Domain Integration

**Seedwarden cultivation tools integration:**
- Seeder calibration: Seedwarden planting guides specify target seeding populations; calibrating a grain drill or precision planter to those targets is a Tier 1 skill (calibration procedure documented in Iowa State extension publication PM-1060)
- Seed-to-harvest equipment chain: tiller → seeder → cultivator → thresher forms the critical path; this outline documents repair for each link; prioritization matrix (companion file) scores by consequence of failure
- Cover crop seeding: NRCS FOTG conservation practices specify seeding rates and equipment requirements for cover crop establishment aligned with Seedwarden soil biology emphasis

**Phase 5 microgrid equipment parallels:**
- Generator repair: Section 2.6 fuel system and Section 2.5 carburetor procedures are directly applicable to generator maintenance; a community with small-engine repair skill maintains both farm equipment and backup generation
- Shared tool investment: the community shop tool set (Section 4 of the pre-research, $2,500–$5,500) services farm equipment, generator maintenance, and general fabrication — single capital investment covering multiple resilience domains
- Power independence crossover: Meshtastic backbone nodes running from the off-grid microgrid (Section 4 of meshtastic-community-networking-research.md) depend on the generator as backup; generator repair skill is part of the communication infrastructure resilience chain

**Off-grid-living equipment overlap:**
- Domain 10 (Tools and Fabrication) establishes that welding capability unlocks Tier 2 farm equipment repairs; the shared community shop with MIG welder serves both domains
- Domain 4 (Food Production) establishes the minimum equipment set for household-scale food self-sufficiency; this outline provides the repair architecture for that equipment set
- Shared documentation archive: farm equipment manuals and off-grid-living documentation share a common storage strategy (USB drive + printed subset); single archival project covers both

---

### Track A Bibliography (44 sources)

**Standards and Regulatory:**
1. [ASABE Technical Library — Standards](https://elibrary.asabe.org/standards.asp)
2. [ISO 11684:2023 — Safety Labels for Agricultural Machinery](https://www.iso.org/standard/74565.html)
3. [NRCS Field Office Technical Guides](https://www.nrcs.usda.gov/resources/guides-and-instructions/field-office-technical-guides)
4. [NRCS National Engineering Manual](https://www.nrcs.usda.gov/sites/default/files/2022-11/National%20Engineering%20Manual.pdf)
5. [Iowa NRCS Engineering Resources](https://www.nrcs.usda.gov/resources/guides-and-instructions/iowa-nrcs-engineering)

**Right-to-Repair Legal Landscape:**
6. [John Deere $99M Settlement — Farm Progress](https://www.farmprogress.com/farming-equipment/john-deere-settles-right-to-repair-lawsuit-for-99-million)
7. [Deere Settlement — Arnold & Porter Analysis](https://www.arnoldporter.com/en/perspectives/blogs/consumer-products-and-retail-navigator/2026/04/john-deeres-99-million-settlement-and-the-right-to-repair-landscape)
8. [Federal Court Preliminary Approval — American Ag Network](https://www.americanagnetwork.com/2026/05/20/federal-court-gives-preliminary-approval-to-99-million-john-deere-right-to-repair-settlement/)
9. [EPA Advances Farmers' Right to Repair — EPA Press Release](https://www.epa.gov/newsreleases/epa-advances-farmers-right-repair-their-own-equipment-saving-repair-costs-and)
10. [EPA Guidance — Farm Policy News](https://farmpolicynews.illinois.edu/2026/02/epa-affirms-farmers-right-to-repair-equipment/)
11. [EPA DEF Sensor Rules — DTN](https://www.dtnpf.com/agriculture/web/ag/equipment/article/2026/03/30/epa-eases-def-sensor-rules-keeps-def)
12. [Tractor Hacking Project](https://tractorhacking.github.io/)

**University Extension:**
13. [Iowa State — Tractor Maintenance PM 2089L](https://store.extension.iastate.edu/Product/Tractor-Maintenance-to-Conserve-Energy-Farm-Energy-PDF)
14. [Iowa State — Tillage Equipment Maintenance](https://crops.extension.iastate.edu/encyclopedia/tillage-equipment-maintenance)
15. [Iowa State — Farm Machinery Replacement Strategies A3-30](https://www.extension.iastate.edu/agdm/crops/pdf/a3-30.pdf)
16. [Iowa State — Farm Machinery Labor Sharing Manual NCFMEC-21](https://shop.iastate.edu/extension/farm-environment/farm-and-business-management/land-and-equipment/ncfmec21.html)
17. [Cornell Small Farms — Tractor Selection 2026](https://smallfarms.cornell.edu/2026/01/finding-the-tractor-that-fits-your-farm/)
18. [Cornell Small Farms — Online Courses](https://www.smallfarmcourses.com/)
19. [Purdue University Extension](https://extension.purdue.edu/)
20. [University of Illinois Extension — Hay and Pasture Ch. 6](http://extension.cropsciences.illinois.edu/handbook/pdfs/chapter06.pdf)

**Manufacturer and Manual Archives:**
21. [Archive.org — John Deere Manual Collection](https://archive.org/details/John_Deere_Company)
22. [Archive.org — Massey-Ferguson MF-46](https://archive.org/details/masseyfergusonsh0000unse)
23. [Archive.org — Farm Equipment and Hand Tools](https://archive.org/details/farm-equipment-and-hand-tools-a-practical-manual)
24. [Farm Manuals Fast](https://farmmanualsfast.com/)
25. [Yesterday's Tractors Manuals](https://www.yesterdaystractors.com/tractor-manuals/)
26. [All Tractor Manuals — Free PDFs](https://www.alltractormanuals.com/)
27. [Hudson Valley Farm Hub — Farm Mechanic Basics](https://hvfarmhub.org/farm-mechanic-basics-program/)
28. [Hudson Valley Farm Hub — Fundamentals of Farm Mechanics](https://hvfarmhub.org/the-fundamentals-of-farm-mechanics-a-training-program/)

**Open-Source Ecosystem:**
29. [FarmHack Tool Library](https://farmhack.org/tools)
30. [FarmHack — Winnower and Thresher](https://farmhack.org/tools/john-howe-winnower-and-thresher)
31. [Open Source Ecology — GVCS](https://www.opensourceecology.org/gvcs/)
32. [LifeTrac Wiki](https://wiki.opensourceecology.org/wiki/LifeTrac)
33. [ATTRA — Irrigation Pumps, Motors, and Engines](https://attra.ncat.org/publication/maintaining-irrigation-pumps-motors-and-engines/)
34. [ATTRA/NCAT Main](https://www.ncat.org/sustainable-agriculture/attra/)
35. [iFixit — Tractor Repair Guides](https://www.ifixit.com/Device/Tractor)
36. [Appropedia — Agricultural Tools](https://www.appropedia.org/Agricultural_tools)
37. [OSU Extension — Small Scale Grain Thresher](https://extension.oregonstate.edu/video/small-scale-grain-thresher)

**Hand Tool and Small Equipment:**
38. [Valley Oak Tool — Broadfork and Wheel Hoe Maintenance](https://www.valleyoaktool.com/blogs/news/broadfork-and-wheel-hoe-maintenance)
39. [UF/IFAS — Sharpening Your Tools](https://gardeningsolutions.ifas.ufl.edu/care/tools-and-equipment/sharpening-your-tools/)
40. [EasyDigging — Hoe Sharpening](https://www.easydigging.com/garden-hoes/articles/how-to-sharpen-hoe.html)
41. [Sears Parts Direct — Chainsaw Carburetor Rebuild](https://www.searspartsdirect.com/diy/repair-guide/how-to-rebuild-a-chainsaw-carburetor)
42. [Family Handyman — Small Engine Maintenance](https://www.familyhandyman.com/article/pro-small-engine-maintenance-tips/)
43. [Hipa Store — Carburetor Cleaning and Rebuild](https://www.hipastore.com/blogs/diy-tips/how-to-clean-and-rebuild-a-carburetor-for-optimal-small-engine-functionality)

**Hydraulic Systems:**
44. [Hercules Sealing Products — Hydraulic Seals](https://herculesus.com/)
45. [Agri Supply — Hydraulic Cylinder Seal Kits](https://www.agrisupply.com/seal-kits/c/2500014/)
46. [Hydraulic Cylinders Inc — Installation Guide](https://www.hydrauliccylindersinc.com/installation-of-hydraulic-cylinder-seals/)
47. [NOK CN Seals — Cylinder Seal Replacement Guide](https://www.nokcn-seals.com/resources/guide-for-replacing-seals-on-hydraulic-cylinders.html)
48. [AHS Hydraulics — Hydraulic Cylinder Seals](https://feeds.ahshydraulics.com/blog/replace-seals-hydraulic-cylinder)

**Parts Sourcing:**
49. [Shoup Manufacturing — Aftermarket Agricultural Parts](https://www.shoupparts.com/)
50. [All States Ag Parts](https://www.tractorpartsasap.com/)
51. [Agproud — Baler Knotter Mechanics](https://www.agproud.com/articles/33893-mechanics-corner-twine-tie-baler-knotters)
52. [Investigate Midwest — Farm Repair Cost Rise 41%](https://investigatemidwest.org/2024/02/07/graphic-cost-to-repair-farm-equipment-rose-50-in-the-last-three-years/)
53. [O*NET — Farm Equipment Mechanics 49-3041.00](https://www.onetonline.org/link/summary/49-3041.00)
54. [Mimeo — Bulk Manual Printing](https://www.mimeo.com/lp/printed-manual/)

---

---

## Track B: Meshtastic Mesh Networking Research Outline

### Introduction: Why Mesh Networking is Critical Infrastructure

The scenario that makes mesh networking a critical infrastructure layer is not a natural disaster — it is any scenario where cellular and internet infrastructure is congested, damaged, or deliberately shut down. Hurricane Helene (September 2024) demonstrated that LoRa mesh networks can carry mutual-aid coordination traffic for days when every other communication system is down. The Am Mellensee, Germany municipal deployment (September 2025) demonstrated the same across nine villages under simultaneous multi-emergency simulation.

The access control implication is equally important: Meshtastic operates on 915 MHz ISM band under FCC Part 15 — no license, no registration, no fee. A community can deploy a functional emergency communication network for $485 (five-household cluster) to $2,520 (25-household community) without asking permission from any authority. This is the critical distinction from licensed amateur radio infrastructure and from commercial carrier-dependent systems.

**Cellular fragility in Zone 5:**
Rural Zone 5 cellular coverage already has gaps. Tower density in northern Illinois, Iowa, and southern Wisconsin is lower than suburban and urban areas; a single tower failure during a severe storm event (the Zone 5 average: 8–12 significant weather events per year) can leave a community area without coverage. Mesh networks provide coverage that degrades gracefully rather than failing completely.

**Internet outage scenarios:**
A community off-grid on microgrids (Phase 5 systems-resilience work) may have power but no internet — ISP infrastructure is fragile and depends on the commercial grid. A Meshtastic mesh operates entirely off-grid; it requires no internet, no cloud, no external servers.

**Government communication shutdown risk:**
At the most extreme end of the scenario range, Meshtastic operates on unlicensed spectrum with end-to-end AES-256 encryption (or AES-128, selectable per channel). A government shutdown of cellular and internet infrastructure does not affect a deployed LoRa mesh running on local hardware. This is not a primary design goal of Meshtastic — it is a consequence of the architecture.

---

### Section 1: Technology Fundamentals

**LoRa physical layer:**
LoRa (Long Range) uses chirp spread-spectrum modulation, developed by Semtech. At 915 MHz with a spreading factor of SF7 (fastest/shortest range): effective data rate ~5.47 kbps, range 2–5 km. At SF12 (slowest/longest range): effective data rate ~0.25 kbps, range 10–15 km in flat terrain.

Zone 5 terrain effect: northern Illinois and Iowa are predominantly flat agricultural terrain — best-case range conditions for LoRa. Southern Wisconsin adds rolling topography; forested valleys cut range by 40–60% compared to open field line-of-sight.

**Firmware: Meshtastic vs. MeshCore:**
Meshtastic (meshtastic.org) uses managed flood routing with hop limits (default 3 hops). Works well to ~100 nodes. MeshCore (2025 emergence) uses hybrid flood/unicast routing with up to 64 hops, designed for regional-scale networks. Both run on the same hardware. They do not interoperate. Zone 5 community recommendation: start with Meshtastic; evaluate MeshCore only if network exceeds 100 nodes or persistent congestion is not resolved by preset tuning.

**Current hardware (May 2026):**
- Heltec LoRa32 V3/V4 ($20–$38): best entry point; ESP32-S3, OLED display, WiFi for MQTT bridging
- LILYGO T-Beam Supreme ($35–$55): best mobile/GPS node; integrated GPS, AXP2101 power management, solar-compatible
- RAK WisBlock Starter Kit ($25–$37): best solar/repeater node; nRF52840 at 3–8 mA receive vs. 30–60 mA for ESP32 equivalents
- Seeed SenseCAP Solar Node P1-Pro ($80–$120): best commercial deployment; IP-rated weatherproof enclosure, integrated solar — used in Am Mellensee nine-village deployment

Sources: [Meshtastic Hardware Complete Guide 2026 — SmartNMagic](https://smartnmagic.com/blogs/solutions/meshtastic-hardware-the-complete-guide) · [Best Meshtastic Devices 2026 — NodakMesh](https://nodakmesh.org/meshtastic/devices) · [Official Meshtastic Devices Docs](https://meshtastic.org/docs/hardware/devices/)

---

### Section 2: Network Topology

**Tier architecture for Zone 5 community deployment:**
- Tier 1 Backbone (3–7 nodes): RAK WisBlock or Heltec V4, solar + LiFePO4, 6 dBi omnidirectional or directional antenna, elevated placement (grain elevator, silo, water tower, church steeple). Role: Router.
- Tier 2 Household nodes (one per household): T-Beam Supreme, battery or AC, carried indoors. Role: Client.
- Tier 3 Mobile nodes: T-Beam Supreme, carried by responders, medical coordinators, patrol. Role: Client Mute in dense networks.

**Coverage estimates, Zone 5 flat terrain:**
3 backbone nodes at 20–30 ft elevation with 6 dBi antennas: 50–150 sq miles. Rule of thumb: one backbone node per 5–8 miles of desired coverage radius. Forested terrain (southern Wisconsin ridge-and-valley): reduce range estimate by 40–60%; add backbone nodes at ridge-top positions.

**Channel preset selection:**
- Default LongFast: correct for networks under 40 active nodes
- MediumSlow: correct for networks 40–150 nodes (Bay Area Mesh switched to MediumSlow at 150 nodes with immediate congestion improvement)
- MediumFast: emerging preference for larger urban deployments; reduces airtime per message

Sources: [Meshtastic Site Planner Documentation](https://meshtastic.org/docs/software/site-planner/) · [Is LongFast Holding Your Mesh Back? — Meshtastic Blog](https://meshtastic.org/blog/why-your-mesh-should-switch-from-longfast/) · [Heartland Emergency Preparedness — Building Community Meshtastic Network](https://heartlandemergencypreparedness.com/2025/08/25/building-a-community-meshtastic-network-step-by-step-guide-for-emergency-preparedness/)

---

### Section 3: Zone 5 Radio Propagation

**Terrain-specific modeling:**
Meshtastic provides a Site Planner tool (meshtastic.org/docs/software/site-planner) for coverage prediction using topographic data. For pre-deployment planning: upload topo data from USGS National Map, place proposed backbone node coordinates, set antenna height and gain, read coverage overlay.

Key Zone 5 terrain variables:
- Corn canopy (June–October): standing corn at 8–10 feet absorbs approximately 6–10 dB at 915 MHz, reducing effective range by 30–50% in corn-covered fields vs. bare ground
- Forest cover: deciduous forest -10 to -20 dB additional path loss vs. open field; conifer forest is worse (-15 to -25 dB)
- Elevation gain: every 10 ft of antenna height gain approximately doubles ground-level coverage area in flat terrain

**Repeater placement strategy:**
Zone 5 priority placement sites (ranked by availability and height gain):
1. Grain elevator (highest structure in most rural communities, 60–120 ft, owner access typically negotiable)
2. Water tower (40–100 ft, municipal permission required, excellent placement)
3. Church steeple (30–60 ft, typical community relationship facilitates access)
4. Barn rooftop (20–40 ft, simplest access for community-owned property)
5. Hilltop installation (terrain-dependent; 20–40 ft of terrain gain at ridge top can exceed 80 ft tower equivalent in flat terrain)

Sources: [Meshtastic Site Planner Introduction — Meshtastic Blog](https://meshtastic.org/blog/meshtastic-site-planner-introduction/) · [USGS National Map](https://apps.nationalmap.gov/viewer/) · [Maximize Meshtastic Range — Mesh Underground](https://meshunderground.com/posts/maximize-meshtastic-range-tips-and-deep-dive/)

---

### Section 4: Regulatory Landscape

**FCC Part 15 unlicensed operation (915 MHz ISM band):**
47 CFR 15.247 governs operation in the 902–928 MHz band. Meshtastic-compatible hardware uses direct-sequence spread spectrum (DSSS) or digital modulation:
- Maximum transmitter output: 1 watt (30 dBm)
- EIRP limit: antennas with gain above 6 dBi require corresponding reduction in transmitter power; high-gain directional antennas (>6 dBi) effectively extend range without increasing legal EIRP
- Power spectral density limit: +8 dBm per 3 kHz
- No license required, no registration required, no fees
- Encryption: permitted (no prohibition on encrypted transmissions in unlicensed Part 15 operation — unlike amateur radio)

**Amateur radio licensing — when it becomes relevant:**
Standard Meshtastic ISM-band operation requires no license. Amateur radio ("Ham mode") becomes relevant only when:
1. A community wants higher transmit power than Part 15 permits (requires license and disabling encryption)
2. A community needs longer-range HF communication (40m or 20m bands, General class license required)
3. A community participates in ARES or RACES emergency communication networks

License classes relevant to community communication:
- **Technician class**: 35-question exam, 26 correct to pass (~75%), $35 FCC fee, $15 exam session fee. Privileges: all VHF/UHF bands above 30 MHz. Limited HF below 30 MHz. Primary benefit for communities: legally operate 2m FM repeaters, GMRS cross-compatibility, APRS on 144.39 MHz.
- **General class**: 35-question exam (must hold Technician first or test same session). Privileges: all amateur bands including HF. Key frequencies: 7.0–7.3 MHz (40m), 14.0–14.35 MHz (20m). Critical for long-range emergency communication.
- **Extra class**: Advanced theory exam; not necessary for community communication purposes

**FCC enforcement risk:**
FCC enforcement against unlicensed Part 15 operators in rural areas is minimal. Enforcement action is overwhelmingly concentrated on:
1. Intentional interference with other licensed services
2. Devices operating significantly outside Part 15 power limits (pirate FM broadcast, etc.)
3. Urban dense environments with frequency congestion

A community operating Meshtastic on 915 MHz within Part 15 limits in a rural Zone 5 context faces negligible enforcement risk. [REGULATORY UPDATE NEEDED: 2026 FCC spectrum policy changes affecting unlicensed bands — FCC spectrum auctions have not touched 902–928 MHz, but monitoring recommended annually]

Sources: [eCFR 47 CFR 15.247](https://www.ecfr.edu/current/title-47/chapter-I/subchapter-A/part-15/subpart-C/subject-group-ECFR2f2e5828339709e/section-15.247) · [FCC Amateur Radio Service](https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service) · [FCC Operator Class Privileges](https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service/operator-class) · [ARRL Getting Your Technician License](http://www.arrl.org/getting-your-technician-license) · [HamStudy — How to Get Licensed](https://hamstudy.org/content/how) · [Meshtastic FAQ — Licensing](https://meshtastic.org/docs/faq/) · [Hoosier Mesh — Amateur Radio and Meshtastic](https://hoosiermesh.org/docs/reference/ham-radio/)

---

### Section 5: Inter-Community Coordination

**Multi-network architecture:**
A regional Zone 5 resilience coalition spanning multiple villages (Scenario C: 200+ people, 3–5 communities) requires a hierarchical network design:
- Local mesh: each community operates its own Meshtastic mesh; channel PSK is community-specific (private)
- Inter-community channel: all participating communities share a common channel with a coalition-level PSK, distributed in person at coalition formation; used only for inter-community coordination
- Regional backbone: for distances exceeding 15–20 km between communities (typical in rural Iowa or Illinois), a high-power repeater at elevation or an amateur radio HF net on 40m (7.2–7.3 MHz, General class) provides the inter-community backbone link

**Firewall protocols:**
- The inter-community channel carries only coordination traffic; local operational traffic stays on local channels
- Coalition PSK is stored only in printed form at designated community coordinators; not on phones
- New community onboarding requires in-person key distribution (physical meeting)

**Coalition governance:**
- Network coordinator role (volunteer): responsible for firmware updates, node health monitoring, quarterly testing protocol, key rotation schedule
- Monthly test: all backbone nodes active, cross-community message delivery confirmed, node count audit
- Quarterly drill: simulated grid-down scenario, all household nodes active, inter-community coordination messaging exercise

[ZONE 5 DEPLOYMENT DATA NEEDED: Real-world inter-village Meshtastic link data for Midwest agricultural terrain at 15–30 km separation distances; NodakMesh (North Dakota) is the closest documented analog but terrain differs]

Sources: [NodakMesh](https://nodakmesh.org/) · [NC Mesh](https://ncmesh.net/) · [Austin Mesh Learn](https://www.austinmesh.org/learn/) · [DEV Community — Infrastructure Meltdown with Meshtastic 2026](https://dev.to/noperai42eng/how-to-survive-an-infrastructure-meltdown-with-meshtastic-and-meshcore-2026-dej)

---

### Section 6: Operational Security

**Cryptographic status as of May 2026:**
- CVE-2025-52464 (CVSSv4 9.5): duplicate X25519 keypair vulnerability — hardware manufacturers created "golden image" clone batches with identical private keys; patched in firmware v2.6.11 (mandatory for all deployments)
- CVE-2025-55293: NodeInfo empty publicKey field attack — allowed downgrade from public-key to shared-key encryption; patched in v2.6.3
- Required action: all nodes must run v2.6.11 or later; all PKI keys must be regenerated after updating (keys generated on older firmware are compromised by definition)
- Channel encryption: AES-256 per-channel PSK, correctly implemented post-v2.6.11; acceptable for community coordination use
- "Harvest now, decrypt later" risk: an adversary recording channel traffic could decrypt it if PSK is obtained later; for higher-sensitivity use (medical, security coordination), rotate PSKs quarterly and store in printed form only

**Key management:**
- Generate unique PSKs for each functional channel (general, medical, security, logistics)
- Print and laminate channel QR codes; store physical copies in multiple locations
- Disable Bluetooth on unattended backbone nodes (reduces attack surface, saves 5–15 mA)
- Position update interval: 10–15 minutes minimum; 30-second intervals expose real-time movement and cause congestion

**MQTT configuration warning:**
Do not connect community emergency net nodes to public MQTT brokers (mqtt.meshtastic.org). This routes all community traffic through a third-party internet server, defeats the zero-infrastructure design, and introduces congestion from unrelated global nodes. Local-only MQTT on a Raspberry Pi for situational awareness dashboards is acceptable.

Sources: [GBHackers — Critical Meshtastic Flaw](https://gbhackers.com/critical-meshtastic-flaw/) · [CVE-2025-55293](https://securityvulnerability.io/vulnerability/CVE-2025-55293) · [Meshtastic Encryption — Official Docs](https://meshtastic.org/docs/overview/encryption/) · [Securing Meshtastic — Hackers Arise](https://hackers-arise.com/off-grid-communications-part-4-securing-your-meshtastic-communications/) · [Meshtastic MQTT Configuration](https://meshtastic.org/docs/configuration/module/mqtt/)

---

### Section 7: Phase 5 Microgrid Integration

**Power integration architecture:**
- Option A (primary): 5V USB from microgrid 12V or 48V bus via buck converter ($3–$8); powers Heltec V3/V4 backbone nodes indefinitely as long as microgrid battery holds charge; negligible load (<150 mA worst case)
- Option B (fallback/remote nodes): dedicated per-node solar + LiFePO4 battery; fully independent of house electrical system; required for nodes at remote elevations (grain elevator, water tower)

**Microgrid status signaling via mesh:**
Use Meshtastic telemetry module for automated status broadcasts:
- Battery voltage and charge percentage from microgrid monitoring system (via simple voltage divider to node ADC pin)
- Solar generation status (binary: charging/not charging)
- Critical alert broadcast: configurable threshold trigger for low battery condition (e.g., <20% state of charge broadcasts alert to all community nodes)
- Medical device power status: for communities with powered medical equipment depending on microgrid continuity

**Emergency coordination integration:**
- Grid-down event detection → automatic alert broadcast to all mesh nodes
- Load-shedding requests: community coordinator broadcasts priority demand reduction request
- Blackout duration estimation: mesh carries generator fuel status, estimated runtime, priority loads

Sources: [Meshtastic Solar Powered — Official Docs](https://meshtastic.org/docs/solar-powered/) · [ADKMesh — Best Meshtastic Solar Node Builds 2026](https://adkmesh.com/best-meshtastic-solar-nodes-builds-2026/) · [Hackaday — Practicality of Solar Powered Meshtastic](https://hackaday.com/2025/09/17/the-practicality-of-solar-powered-meshtastic/)

---

### Section 8: Fallback Radio Protocols

**Three-layer communication architecture for Zone 5 communities:**
- Layer 1 (grid present): GMRS or FRS radios, 462–467 MHz, line-of-sight voice; requires GMRS license ($35, no exam, covers family members) for legal high-power operation
- Layer 2 (grid down, batteries operational): Meshtastic mesh, 915 MHz, text/position, 10–15 km per hop — this outline's primary subject
- Layer 3 (extended emergency, longer range): HF amateur radio, 40m/20m bands, General class license required; range: hundreds to thousands of miles; bandwidth: voice (SSB) or digital modes (WINLINK, JS8Call, Vara FM)

**HF amateur radio for Layer 3:**
- 40m (7.0–7.3 MHz): best for regional communication (100–800 km); day/night active; primary emergency band for Midwest; 7.175–7.300 MHz voice (Upper Sideband convention)
- 20m (14.0–14.35 MHz): best for long-distance (500–5,000+ km); active daytime; 14.225 MHz calling frequency (USB)
- 2m FM (144–148 MHz): local simplex 146.520 MHz national calling frequency; excellent for short-range voice; Technician class sufficient
- ARRL ARES (Amateur Radio Emergency Service): organized volunteer networks in most Zone 5 counties; pre-existing emergency communication infrastructure that a licensed community member can integrate with

**Simplex net protocols for Zone 5 emergencies:**
- Establish community calling frequency on 2m before crisis (typically local ARRL chapter recommendation)
- Check-in protocol: timed net (7:00 AM and 7:00 PM daily), net control rotates, all active stations check in
- Message traffic: formal NTS (National Traffic System) format for inter-region priority messages; informal voice for local coordination
- Integration with Meshtastic: a community with both systems can bridge — amateur radio operator relays Meshtastic text traffic verbally over HF to distant stations that have no mesh connectivity

[TECHNICAL SPEC NEEDED: Specific Zone 5 county ARES repeater listings and simplex frequencies for northern Illinois, Iowa, and southern Wisconsin]

Sources: [ARRL Band Plan](http://www.arrl.org/band-plan) · [ARRL Amateur Radio Emergency Communication](http://www.arrl.org/amateur-radio-emergency-communication) · [FMARC Calling Frequencies](https://fmarc.net/calling-frequencies/) · [FCC Amateur Radio Operator Class](https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service/operator-class)

---

### Track B Bibliography (37 sources)

**Official Meshtastic Documentation:**
1. [Meshtastic Official](https://meshtastic.org/)
2. [Meshtastic Introduction](https://meshtastic.org/docs/introduction/)
3. [Getting Started](https://meshtastic.org/docs/getting-started/)
4. [Hardware Devices](https://meshtastic.org/docs/hardware/devices/)
5. [LoRa Configuration](https://meshtastic.org/docs/configuration/radio/lora/)
6. [Solar Powered](https://meshtastic.org/docs/solar-powered/)
7. [Encryption Documentation](https://meshtastic.org/docs/overview/encryption/)
8. [Known Encryption Limitations](https://meshtastic.org/docs/about/overview/encryption/limitations/)
9. [Site Planner](https://meshtastic.org/docs/software/site-planner/)
10. [FAQ](https://meshtastic.org/docs/faq/)
11. [MQTT Module Configuration](https://meshtastic.org/docs/configuration/module/mqtt/)
12. [Why Meshtastic Uses Managed Flood Routing](https://meshtastic.org/blog/why-meshtastic-uses-managed-flood-routing/)
13. [Is LongFast Holding Your Mesh Back?](https://meshtastic.org/blog/why-your-mesh-should-switch-from-longfast/)
14. [Site Planner Introduction](https://meshtastic.org/blog/meshtastic-site-planner-introduction/)

**Security (CVE):**
15. [GBHackers — Critical Meshtastic Flaw CVE-2025-52464](https://gbhackers.com/critical-meshtastic-flaw/)
16. [SecurityVulnerability.io — CVE-2025-55293](https://securityvulnerability.io/vulnerability/CVE-2025-55293)
17. [Hackers Arise — Securing Your Meshtastic](https://hackers-arise.com/off-grid-communications-part-4-securing-your-meshtastic-communications/)

**Hardware and Solar:**
18. [SmartNMagic — Hardware Guide 2026](https://smartnmagic.com/blogs/solutions/meshtastic-hardware-the-complete-guide)
19. [NodakMesh — Best Devices 2026](https://nodakmesh.org/meshtastic/devices)
20. [Adrelien — Best Devices for Every Use Case](https://adrelien.com/the-best-meshtastic-devices-for-every-use-case-a-comprehensive-guide/)
21. [ADKMesh — Best Solar Node Builds 2026](https://adkmesh.com/best-meshtastic-solar-nodes-builds-2026/)
22. [Hackaday — Practicality of Solar Powered Meshtastic](https://hackaday.com/2025/09/17/the-practicality-of-solar-powered-meshtastic/)
23. [Heltec MeshSolar](https://heltec.org/meshsolar-where-solar-power-meets-meshtastic-freedom/)
24. [Anern — LiFePO4 Winter Performance](https://www.anernstore.com/blogs/off-grid-solar-solutions/lifepo4-deep-winter-loads-myths)

**Community Deployments:**
25. [Heartland Emergency Preparedness — Community Meshtastic Network](https://heartlandemergencypreparedness.com/2025/08/25/building-a-community-meshtastic-network-step-by-step-guide-for-emergency-preparedness/)
26. [Seeed Studio — Am Mellensee Germany Deployment](https://www.seeedstudio.com/blog/2025/10/30/building-resilient-communication-germany-meshtastic-solar-nodes/)
27. [WTXL — Monticello CERT Proposal](https://www.wtxl.com/news/local-news/in-your-neighborhood/monticello/monticello-council-considers-new-emergency-communication-system-proposal/)
28. [Austin Mesh Learn](https://www.austinmesh.org/learn/)
29. [NC Mesh](https://ncmesh.net/)
30. [MeshAVL — Asheville Community](https://meshavl.com/)
31. [NodakMesh](https://nodakmesh.org/)
32. [Puget Mesh](https://pugetmesh.org/)

**MeshCore and Protocol Comparison:**
33. [Broken Signal — MeshCore vs Meshtastic](https://brokensignal.tv/pages/meshcore-vs-meshtastic.html)
34. [Seeed Studio — MeshCore vs Meshtastic March 2026](https://www.seeedstudio.com/blog/2026/03/23/meshcore-vs-meshtastic/)
35. [Austin Mesh — MeshCore vs Meshtastic](https://www.austinmesh.org/learn/meshcore-vs-meshtastic/)

**Academic:**
36. [University of Michigan — LoRa Mesh for Disaster Response](https://deepblue.lib.umich.edu/bitstream/handle/2027.42/176695/LoRa_Thesis.pdf)
37. [IEEE — LoRa Mesh Off-grid Emergency Communications](https://ieeexplore.ieee.org/document/9342944/)
38. [IJARCCE — Solar-Powered LoRa Mesh](https://ijarcce.com/wp-content/uploads/2025/12/IJARCCE.2025.141266-Solar.pdf)

**Regulatory:**
39. [eCFR 47 CFR 15.247](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-15/subpart-C/subject-group-ECFR2f2e5828339709e/section-15.247)
40. [FCC Amateur Radio Service](https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service)
41. [FCC Operator Class](https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service/operator-class)
42. [ARRL Band Plan](http://www.arrl.org/band-plan)
43. [ARRL Emergency Communication](http://www.arrl.org/amateur-radio-emergency-communication)
44. [HamStudy — Getting Licensed](https://hamstudy.org/content/how)
45. [Hoosier Mesh — Amateur Radio and Meshtastic](https://hoosiermesh.org/docs/reference/ham-radio/)

---

## Research Markers Summary

**[RESEARCH NEEDED] items — Track A:**
- Hydraulic seal material chemistry at Zone 5 cold temperatures (-10°F to -20°F): specific elastomer behavior (nitrile vs. Viton) in temperature cycling
- Cold-start hydraulic flow rate data for Zone 5 January conditions: minimum warm-up time before full hydraulic load
- Hydraulic pump bypass threshold specifications for common Zone 5 small tractor models
- Pressure washer pump freeze damage prevention protocols for Zone 5 winter storage
- Paper pot transplanter spare parts US availability (Japanese-manufactured)
- Long-term ethanol-blend fuel storage in Zone 5 temperature cycling conditions

**[TECHNICAL SPEC NEEDED] items — Track B:**
- Zone 5 county ARES repeater listings and simplex frequencies (northern Illinois, Iowa, southern Wisconsin)
- Zone 5-specific LiFePO4 cold-climate Meshtastic deployment field data (NodakMesh is closest analog; actual Zone 5 data needed)

**[ZONE 5 DEPLOYMENT DATA NEEDED] items — Track B:**
- Real-world inter-village Meshtastic link performance at 15–30 km separation in Midwest agricultural terrain (rolling farmland, partial tree cover)
- Corn canopy attenuation measurements at 915 MHz (existing literature is RF propagation models; actual field data is sparse)

**[REGULATORY UPDATE NEEDED] items — Track B:**
- FCC spectrum policy changes affecting unlicensed 902–928 MHz bands — monitor annually; no changes as of May 2026

---

## Phase 6 Activation: June 1 Decision Handoff

**Decision trigger**: User decision on Phase 5 Wave 2 sequencing (June 1, 2026)

**Dependency map for Track B (Meshtastic):**
- If Phase 5 Wave 2 path includes community-scale microgrid implementation: Track B becomes critical immediately; microgrid-mesh integration is the key enabling technology for community coordination
- If Phase 5 Wave 2 defers community-scale to household focus: Track B can deploy in parallel as standalone infrastructure; not dependent on microgrid completion

**Activation sequence (Hybrid Option 3 from PHASE_5_WAVE_2_PHASE_6_EXECUTION_SEQUENCING.md):**
1. June 1–5: Phase 5 Wave 1 publication (production-ready, 14.6K words)
2. June 5–15: Phase 6 framework validation — combine Track A + Track B + microgrid pre-research into `PHASE_6_FRAMEWORK.md` (editorial integration, 2–3 days)
3. June 10–July 10: Phase 5 Wave 2 author writing cycle (35% preliminary drafts ready)
4. July 1–15: Phase 6 document suite finalized

**Zero research blockers**: Both tracks have complete pre-research as of May 26, 2026. The June 1 activation requires only editorial integration of existing pre-research documents — no new research sprints needed before the June 1 decision. New research will be triggered by the [RESEARCH NEEDED] markers during the June 5–15 integration phase.

---

*Confidence assessment: High on documentation sources and hardware specifications (verified through current community deployments and official documentation); High on regulatory status (FCC Part 15 rules confirmed from eCFR, FCC.gov, and ARRL; right-to-repair legal landscape from court filings and EPA press releases); High on Hurricane Helene and Am Mellensee deployments (primary sources from deployers); Medium on Zone 5-specific terrain propagation (extrapolated from flat-terrain LoRa data; Zone 5-specific empirical data is sparse); Medium on cold-climate hydraulic seal behavior (physics-based, confirmed in general hydraulic literature but Zone 5-specific temperature cycling data is a gap). Research markers identify all gaps explicitly.*
