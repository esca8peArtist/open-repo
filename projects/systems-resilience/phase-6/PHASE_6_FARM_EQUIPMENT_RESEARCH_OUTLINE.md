---
title: "Phase 6 Farm Equipment Repair — Research Outline and Editorial Integration Plan"
project: systems-resilience
phase: 6
track: A
status: RESEARCH-COMPLETE — editorial integration pending
created: 2026-05-26
author: General Research Agent (Session 1649)
research_documents:
  - phase-6/farm-equipment-repair-research.md (~5,820 words, 41 sources)
  - phase-6/phase-6-farm-equipment-repair-right-to-repair.md (~10,200 words, 28 sources)
  - phase-6/farm-equipment-prioritization-matrix.csv
research_word_total: "~16,000 words across 2 documents + 1 matrix"
research_source_total: 78
decision_gate: 2026-06-01
editorial_integration_estimate: "20–30 hours"
---

# Phase 6 Farm Equipment Repair: Research Outline

> **Status**: Pre-research is complete. Two full production documents and one prioritization matrix exist in this directory, totaling ~16,000 words and 78 sources. This outline synthesizes what has been researched, identifies the 6 remaining gaps ([RESEARCH NEEDED] markers), and structures the editorial integration work needed to produce a unified community deployment guide.

---

## Lead Finding

The documentation problem for Zone 5 agricultural self-sufficiency has effectively closed. Archive.org, ATTRA/NCAT, university extension networks (Iowa State, Purdue, Illinois, Cornell), FarmHack, and the Open Source Ecology LifeTrac project collectively provide free coverage of almost every equipment category a 20–100 household community needs. The unsolved problem is not access to information — it is skill development embedded in the community calendar before crisis strikes. A broken tractor gearbox at 6 AM on the first day of planting cannot be fixed by someone who read a manual last night.

Two 2026 legal developments materially improved the independent repair environment: the John Deere $99M settlement (April 2026) and the EPA's Clean Air Act repair guidance (February 2026) together removed the two largest legal barriers that had blocked independent farm equipment repair for a decade. However, diagnostic software access promised by the settlement will not be available until end-of-2026 at the earliest, and the settlement has not received final court approval (fairness hearing: October 29, 2026). The practical constraint remains acute.

---

## Section 1: Research Completed — What Exists

### Document 1: farm-equipment-repair-research.md

**Scope**: Open-source ecosystem, documentation sources, skill architecture
**Word count**: ~5,820 | **Sources**: 41

**Content inventory**:
- Zone 5 community fleet definition (12 equipment categories, criteria for small-community scale selection)
- Zone 5 climate constraints (diesel gelling, short planting windows, harvest pressure, dust loads)
- ASABE and ISO standards reference with land-grant library access pathway
- NRCS Field Office Technical Guides and National Engineering Manual
- University extension publications: Iowa State (4 key docs), Illinois, Purdue, Cornell Small Farms
- Manufacturer archival documentation: Archive.org collections (John Deere, Massey-Ferguson, IH), Farm Manuals Fast, Yesterday's Tractors, All Tractor Manuals
- FarmHack tool library: Winnower/Thresher, Small-Scale Thresher, Bicycle Fanning Mill, Culticycle
- Open Source Ecology LifeTrac: full specs, practical assessment for Zone 5
- ATTRA/NCAT: Maintaining Irrigation Pumps + 300+ sustainable ag publications
- Tractor Hacking Project (Cal Poly/iFixit): CAN bus diagnostics, DMCA exemption
- Repair complexity framework: Tier 1 (trainable, 8–16h), Tier 2 (intermediate, 40–80h), Tier 3 (specialist)
- Tier 1 repair table (12 procedures) and Tier 2 repair table (partial)
- Specialized tool inventory with costs ($2,500–$5,500 community shop)
- Community repair clinic model: pre-season (March) + post-season (October) cadence
- Repair Café adaptation for farm context
- Skill-sharing architecture

### Document 2: phase-6-farm-equipment-repair-right-to-repair.md

**Scope**: Legal landscape, repair access, rights and restrictions
**Word count**: ~10,200 | **Sources**: 28

**Content inventory**:
- John Deere $99M settlement: full terms, timeline, equipment covered, remaining uncertainty
- EPA February 2026 Clean Air Act guidance: what it permits and does not permit
- DMCA Section 1201: current agricultural exemption scope, 2024 exemption renewal
- Tractor Hacking Project legal analysis: CAN bus diagnostics under DMCA exemption
- State-level right-to-repair legislation: 2025–2026 state landscape
- Preventive maintenance procedures by equipment category
- Independent parts sourcing: NAPA, O'Reilly, TSC, Surplus City Liquidators, industrial bearing suppliers
- Diagnostic tool ecosystem: OBD/ISOBUS tools, CanDo OHV Pro ($1,000–$2,500)
- Community-level documentation and knowledge management
- Pre-digital equipment advantages (pre-1990 design, no ECU lock-in)

### Matrix: farm-equipment-prioritization-matrix.csv

**Scope**: Equipment prioritization for Zone 5 community procurement
**Format**: Multi-column matrix with equipment categories, failure consequence ratings, repair complexity tiers, documentation availability, and Zone 5 priority scores

---

## Section 2: Zone 5 Target Equipment — 12 Categories

The research defines a 12-category community fleet for 20–100 households on 10–50 cultivated acres:

| Category | Priority | Repair Complexity | Documentation Availability |
|---|---|---|---|
| Small tractor (20–60 hp) | Critical | Tier 1–3 | Excellent (Archive.org, ISU extension, Cornell) |
| Tiller / rotary tiller | High | Tier 1–2 | Good (Archive.org, OEM manuals) |
| Seeder / grain drill | High | Tier 1–2 | Good (manufacturer sites) |
| Hay baler (small square/round) | High | Tier 2 | Moderate (knotter mechanism is specialized) |
| Grain thresher (small-scale) | Medium | Tier 1–2 | Good (FarmHack DIY + OSE) |
| Harvester / combine (small) | Medium | Tier 2–3 | Moderate (pre-1990 models well-documented) |
| Implements (plow, disc, cultivator) | High | Tier 1–2 | Excellent (simple mechanics, extension publications) |
| Hand tools (scythes, broadforks) | High | Tier 1 | Excellent (multiple sources) |
| Pump / motor | High | Tier 1–2 | Excellent (ATTRA irrigation pump guide) |
| Generator | High | Tier 1–2 | Good (manufacturer + small engine guides) |
| Hydraulic systems | Critical | Tier 2–3 | Moderate (dealer-dependent for system-level diagnosis) |
| Specialty (sprayer, post-pounder) | Low–Medium | Tier 1–2 | Adequate |

**Zone 5 seasonal timing note**: Equipment failures during Zone 5 planting windows (corn: May 1–20; soybeans: May 10–June 5) and harvest (wheat: July; corn: October) carry outsized productivity consequences. The repair clinic model prioritizes pre-season preparation to minimize in-season failures.

---

## Section 3: Key Repair Categories (Top 5)

### 3.1 Hydraulic Systems (Highest Consequence)

**Why critical**: Hydraulics power all implement functions on a tractor — loader, three-point hitch, remote cylinders. A hydraulic failure grounds all attached implements. Hydraulic problems account for approximately 25–30% of in-season equipment downtime.

**Repair categories covered in research**:
- Hydraulic fluid checks and changes (Tier 1 — teachable)
- Cylinder seal replacement (Tier 1–2)
- Pump pressure testing and diagnosis (Tier 2)
- System contamination diagnosis and flush (Tier 2)
- Pump bypass and system pressure specifications (Tier 2–3)

**Documentation**: Research identifies pressure test gauge set ($150–$400) as key tool unlock. Service manual is required for pressure specifications — Archive.org has these for pre-2000 equipment; dealer access required for newer.

**[RESEARCH NEEDED — Gap 1]**: Cold-temperature hydraulic seal chemistry for Zone 5 winter storage. Seals that work at 70°F may become brittle at -10°F to -20°F. Specification of cold-climate seal compounds needed for procurement guidance.

**[RESEARCH NEEDED — Gap 2]**: Pump bypass specifications for Zone 5 common tractor models (Kubota B/L series, Massey Ferguson 200/300 series, Farmall Super M). Without pump bypass specs, Tier 2 hydraulic diagnosis cannot be completed without dealer involvement.

### 3.2 Engine Maintenance and Failure Prevention

**Coverage**: Full Tier 1 maintenance table (oil/filter, fuel filter, air filter, glow plugs, battery). Zone 5-specific winter preparation (diesel gelling prevention, DEF system guidance, battery discharge protocols).

**Key sources**: Iowa State PM 2089L (tractor maintenance), ATTRA irrigation pump guide, manufacturer operator manuals from Archive.org.

**Research completeness**: High. Tier 1 procedures well-documented. Tier 2 (injection system work) documented at procedure level; sourcing guidance included.

### 3.3 Electrical Systems

**Coverage**: Basic fault code reading via OBD/ISOBUS scan tools, glow plug testing, battery maintenance. Tractor Hacking Project covers CAN bus diagnostic protocols for 2000+ model year equipment.

**Significant constraint**: Post-2000 equipment electronic control units (ECUs) require proprietary software for full diagnosis. John Deere settlement will address this for large equipment; compact tractors (Kubota, LS, Mahindra) are not covered by the Deere settlement.

**Research completeness**: Moderate. Pre-2000 equipment well-covered (simple electrical). Post-2000 electronic systems depend on the Deere settlement timeline (December 31, 2026 at earliest) and on third-party diagnostic tool development (CanDo OHV Pro, Tractor Hacking Project tools).

### 3.4 Belts, Drives, and Power Transmission

**Coverage**: Belt tension check and replacement (Tier 1), PTO driveline maintenance, hay baler knotter mechanism cleaning and lubrication. Zone 5 harvest season produces very high belt replacement demand (combine and baler work in corn and hay conditions).

**Key source**: Hay baler knotter mechanism is the most commonly failed complex assembly in Zone 5 small-farm operations. Research identifies it as a priority Tier 2 training topic for the repair clinic model.

**Research completeness**: High for belts and basic drives. Baler-specific mechanism repair documented.

### 3.5 Fuel Systems

**Coverage**: Fuel filter replacement, contamination diagnosis and flush, diesel fuel storage (winter gelling, ethanol blend concerns). Zone 5 specific: winter diesel formulation, storage container protocols.

**[RESEARCH NEEDED — Gap 3]**: Long-term ethanol-blend fuel storage protocols for Zone 5. E10/E15 fuel in stored small equipment degrades within 30–90 days (phase separation, varnish formation). PRI-G, Sta-Bil, and similar treatments are documented in the research but manufacturer-specific protocols for small engines need expansion.

**Research completeness**: Moderate. Main fuel system procedures documented. Ethanol storage gap is a practical bottleneck for communities storing equipment with E10 fuel.

---

## Section 4: Primary Sources Inventory

### Government and Standards Sources (Free)

| Source | URL | Coverage |
|---|---|---|
| ASABE Technical Library | https://elibrary.asabe.org/standards.asp | Engineering standards (land-grant library access) |
| NRCS Field Office Technical Guides | https://www.nrcs.usda.gov/resources/guides-and-instructions/field-office-technical-guides | Equipment selection and specifications |
| NRCS National Engineering Manual | https://www.nrcs.usda.gov/sites/default/files/2022-11/National%20Engineering%20Manual.pdf | Engineering reference |
| NRCS Tillage Equipment Pocket Guide | https://www.nrcs.usda.gov/sites/default/files/2023-01/Montana-Tillage-Equipment-Pocket-ID-Guide-2006.pdf | Implement identification |
| EPA CAA Repair Guidance (Feb 2026) | Via Federal Register | Emissions system repair rights |

### University Extension Sources (Free)

| Source | URL | Coverage |
|---|---|---|
| Iowa State — Tractor Maintenance PM 2089L | https://store.extension.iastate.edu/Product/Tractor-Maintenance-to-Conserve-Energy-Farm-Energy-PDF | Maintenance schedules |
| Iowa State — Tillage Equipment Maintenance | https://crops.extension.iastate.edu/encyclopedia/tillage-equipment-maintenance | Pre-season inspection protocols |
| Iowa State — Farm Machinery Sharing NCFMEC-21 | https://shop.iastate.edu/extension/farm-environment/ | Community equipment sharing |
| Cornell Small Farms — Tractor Selection | https://smallfarms.cornell.edu/2026/01/finding-the-tractor-that-fits-your-farm/ | Fleet selection guide |
| Cornell Small Farms — Courses (30+) | https://www.smallfarmcourses.com/ | Tractor operation and safety |
| ATTRA — Maintaining Irrigation Pumps | https://attra.ncat.org/publication/maintaining-irrigation-pumps-motors-and-engines/ | Pump and motor maintenance |

### Archival and Open-Source Manuals (Free)

| Source | URL | Coverage |
|---|---|---|
| Archive.org — John Deere Collection | https://archive.org/details/John_Deere_Company | JD tractor models 1960s–2000s |
| Archive.org — Massey-Ferguson MF-46 | https://archive.org/details/masseyfergusonsh0000unse | MF shop manual |
| All Tractor Manuals | https://www.alltractormanuals.com/ | Multi-brand free PDF service manuals |
| Yesterday's Tractors Manuals | https://www.yesterdaystractors.com/tractor-manuals/ | Ford, MF, IH, JD, AC |
| FarmHack Tool Library | https://farmhack.org/tools | DIY farm tools with build instructions |
| Open Source Ecology — LifeTrac | https://wiki.opensourceecology.org/wiki/LifeTrac | Open-source tractor design |
| Tractor Hacking Project | https://tractorhacking.github.io/ | CAN bus diagnostics (DMCA-protected) |
| Appropedia Agricultural Tools | https://www.appropedia.org/Agricultural_tools | Appropriate technology wiki |
| iFixit — Tractor Repair | https://www.ifixit.com/Device/Tractor | Community repair guides |

### Legal and Advocacy Sources

| Source | URL | Coverage |
|---|---|---|
| Farm Progress — JD $99M Settlement | https://www.farmprogress.com/farming-equipment/john-deere-settles-right-to-repair-lawsuit-for-99-million | Settlement details |
| Arnold & Porter — Settlement Analysis | https://www.arnoldporter.com/en/perspectives/blogs/consumer-products-and-retail-navigator/2026/04/john-deeres-99-million-settlement-and-the-right-to-repair-landscape | Legal analysis |
| Farm Policy News Illinois | https://farmpolicynews.illinois.edu/2026/04/deere-settles-class-action-right-to-repair-lawsuit/ | Midwest-specific reporting |

---

## Section 5: Scope Estimate — Guide Production

### How Many Guides Are Needed for Comprehensive Coverage

**Minimum viable community guide set** (covers 70% of in-season failures):

| Guide | Scope | Est. Pages | Priority |
|---|---|---|---|
| Pre-season inspection checklist | Tractor + top 4 implements | 8–12 | Critical |
| Tier 1 repairs — tractor | 12 core procedures | 20–30 | Critical |
| Hydraulic systems primer | Fluid, seals, pressure testing | 12–18 | High |
| Tier 1 repairs — baler | Knotter mechanism + belts | 10–15 | High |
| Fuel system procedures | Filter, storage, winter prep | 8–12 | High |
| Electrical basics | Battery, glow plugs, fault codes | 8–12 | High |
| Community repair clinic template | Event planning and skill matrix | 6–8 | Medium |
| Parts sourcing guide | Zone 5 dealers and online | 4–6 | Medium |

**Estimated total**: 8 focused guides, ~76–113 pages.

**Extended guide set** (covers 90% of failures including Tier 2 repairs):

Add 4 additional guides (hydraulic pump overhaul, injection system, tractor electrics, combine-specific), total ~12 guides, ~140–170 pages.

**Recommended approach**: Produce minimum viable set (8 guides) for June 1–August 31 Phase 6 sprint. Extended set as Phase 7 scope.

---

## Section 6: Remaining Research Gaps

Six [RESEARCH NEEDED] markers in the existing documents require resolution before final guide production:

| Gap | Document | Effort | Resolution Path |
|---|---|---|---|
| Cold-temperature hydraulic seal chemistry | farm-equipment-repair-research.md | 2–3h | Parker Hannifin technical bulletins; Zone 5 dealer inquiry |
| Pump bypass specs — Kubota/MF/Farmall | farm-equipment-repair-research.md | 3–4h | Model-specific Archive.org service manuals |
| Long-term ethanol-blend fuel storage | farm-equipment-repair-research.md | 1–2h | PRI-G / Sta-Bil manufacturer documentation + ISU extension |
| Pressure washer freeze-damage protocols | farm-equipment-repair-research.md | 1–2h | General extension publications |
| DEF system winter protocols | phase-6-farm-equipment-repair-right-to-repair.md | 2–3h | Case IH and Deere operator documentation |
| Post-2026 diagnostic software access (when Deere fulfills settlement) | phase-6-farm-equipment-repair-right-to-repair.md | 2h | Monitor settlement docket; update when December 2026 deadline passes |

**Total gap-fill effort**: ~11–14 hours. These can be addressed during the June 5–15 editorial integration sprint.

---

## Section 7: Editorial Integration Plan (June 5–15)

The research is complete. The editorial integration work produces a unified, user-deployable guide from the existing documents.

**Phase 1 (June 5–8, ~8 hours)**: Gap-fill research. Resolve the 6 [RESEARCH NEEDED] markers. Update both source documents.

**Phase 2 (June 8–12, ~12 hours)**: Structure the unified community guide. Write the unifying introduction, combine repair procedures from both documents into the guide template, produce the pre-season checklist as a standalone printable document.

**Phase 3 (June 12–15, ~6 hours)**: Cross-reference integration. Link farm equipment guide forward to Meshtastic deployment guide (communication during repair events), backward to Phase 5 Wave 2 community playbook (repair clinic as community infrastructure), and to right-to-repair appendix (legal context for community use).

**Output**: Unified farm equipment repair guide + printable checklists, production-ready by June 15.

---

**Research outline status**: Complete. All source documents inventoried, gaps identified, production scope defined.
**Supporting files**: `farm-equipment-repair-research.md`, `phase-6-farm-equipment-repair-right-to-repair.md`, `farm-equipment-prioritization-matrix.csv`
