---
title: "Advanced Water Systems: Hydrology, Treatment, Wastewater Integration, and Resilience"
domain: "water-systems"
domain_number: 5
article: "5.0"
wave: 3
section: "water-systems-advanced"
content_type: "procedure"
difficulty: "advanced"
estimated_read_time: "90 minutes"
author: "Open-Repo Project"
last_updated: "2026-07-06"
version: "1.0"
license: "CC-BY-4.0"
climate_zone: "multi-climate"
scale: "rural-landholder, homesteader, small-community"
tags: ["hydrology", "water-budget", "reverse-osmosis", "UV-disinfection", "ion-exchange", "constructed-wetlands", "greywater-cascading", "living-machine", "water-rights", "PFAS", "drought-resilience", "micro-hydro", "aquaponics", "water-testing", "freeze-protection"]
description: "Advanced water systems guide for self-sufficient practitioners. Covers hydrology and water budgeting, multi-stage treatment including RO and UV, greywater cascading, constructed wetlands, living machines, storage optimization, field testing protocols, seasonal adaptation, system integration, maintenance, and regulatory compliance. Sourced from USGS, EPA, WHO, NSF, peer-reviewed hydrology journals, and extension guides."
confidence: "88% — hydrology calculations from USGS Technical Methods; treatment efficacy from EPA Technology Guidance and NSF/ANSI standards; water rights data from National Agricultural Law Center and state water boards; wastewater design criteria from EPA subsurface flow wetland guidance; PFAS MCLs from EPA April 2024 final rule. Lower confidence on site-specific well yield (hyperlocal aquifer variables), living machine performance at very small scale (<5 PE), and state-level regulatory changes after July 2026."
prerequisites:
  - "WAVE_0_DOMAIN_1_WATER_ASSESSMENT_AND_TESTING.md"
  - "WAVE_0_DOMAIN_2_RAINWATER_HARVESTING_AND_STORAGE.md"
  - "WAVE_0_DOMAIN_4_WASTEWATER_AND_GREYWATER_SYSTEMS.md"
cross_references:
  - "wave-3-energy-systems/energy-systems-complete-guide.md"
  - "wave-3-fermentation-preservation/"
  - "projects/systems-resilience/individual/01-water.md"
sources_count: 52
---

# Advanced Water Systems: Hydrology, Treatment, Wastewater Integration, and Resilience

## Overview and Purpose

This guide assumes you have completed the Wave 0 water systems foundation — you understand source typing, basic filtration, chemical disinfection, and rainwater storage fundamentals. The goal here is depth: moving from understanding what your water system does to understanding why it behaves the way it does, and how to design, integrate, and maintain systems at the level a self-sufficient property demands.

**What this guide covers:**

1. Hydrology and water budgeting — source yield, aquifer assessment, demand modeling
2. Advanced treatment systems — multi-stage design, UV/solar disinfection, ion exchange, reverse osmosis
3. Wastewater integration — greywater cascading, constructed wetlands, living machines
4. Storage optimization — thermal mass, sediment management, long-term preservation
5. Water testing and monitoring — field protocols, laboratory referral thresholds, emerging contaminants
6. Seasonal and climate adaptation — freeze protection, drought contingency, flood management
7. System integration — water's relationship with food production, energy systems, and waste cycling
8. Maintenance and troubleshooting — common failures, scale management, repair procedures
9. Regulatory compliance — water rights doctrine, permit requirements, discharge standards
10. Source trade-offs — rainwater vs. groundwater vs. surface water by site type

**Who should read this:** Homesteaders and rural landholders who have operational water systems and need to deepen their understanding; anyone designing a new system from scratch where reliability over years — not months — is the standard; small-community water managers building multi-source resilience.

**License:** CC-BY-4.0. Share and adapt with attribution to the Open-Repo Project.

---

## Section 1: Hydrology and Water Budgeting

Understanding your water budget — the accounting of every input and output of water across your property — is the foundation for every design decision that follows. A system sized without a water budget is a guess. A system sized with one is an engineering decision.

### 1.1 The Water Budget Equation

The basic catchment water balance is:

```
P = ET + R + ΔS

Where:
  P   = Precipitation (input)
  ET  = Evapotranspiration (primary loss)
  R   = Runoff (surface departure)
  ΔS  = Change in storage (groundwater recharge or depletion)
```

For practical site use, you are solving for available water — what remains after ET and runoff losses. USGS groundwater programs use the Soil-Water Balance (SWB) model to calculate this spatially, but you can estimate it manually using regional data. [1]

**Worked example — 10-acre rural property, mid-Atlantic:**

| Component | Value | Source |
|-----------|-------|--------|
| Annual precipitation | 42 inches | NOAA Climate Normals [2] |
| Estimated ET (temperate deciduous landscape) | 26 inches | USGS SWB regional averages [1] |
| Surface runoff | 8 inches | NRCS curve number estimate |
| Estimated groundwater recharge | ~8 inches | By subtraction |
| Total rechargeable water (10 acres) | ~217,800 gallons/year | 8 in × 43,560 sq ft/acre × 10 × 0.0231 gal/in·sqft |

This 217,800 gallons/year is a theoretical maximum. Practical well yield is constrained by aquifer hydraulic conductivity and your pump capacity.

### 1.2 Surface Water Source Assessment

**Stream flow measurement** is the starting point for any surface diversion design. The bucket-and-stopwatch method works for small streams: place a container of known volume (5-gallon bucket) at the discharge point of a narrowed channel and time how long it takes to fill.

```
Flow rate (gpm) = Volume (gallons) ÷ Fill time (seconds) × 60
```

For example: a 5-gallon bucket fills in 8 seconds → 5 ÷ 8 × 60 = **37.5 gpm**

At minimum flow (late summer drought): repeat this measurement across multiple seasons. USGS StreamStats provides regional low-flow statistics for most US watersheds — use the 7Q10 value (7-day minimum flow with 10-year return period) as your design flow for a year-round diversion. [3]

**Seasonal variability index**: Calculate the ratio of peak monthly flow to minimum monthly flow. A ratio above 10:1 indicates high variability; you need substantial storage to bridge low-flow periods. Glacially-fed or spring-fed streams typically show ratios of 3:1 to 5:1 — far more reliable for continuous diversion.

### 1.3 Groundwater Source Assessment

**Spring typing and reliability:** Not all springs are equal. Contact springs — formed where an impervious layer intercepts a perched water table — maintain relatively consistent year-round flow because they draw from a confined aquifer section. Depression springs, which surface where the water table intersects topography, fluctuate with the water table and may fail in drought years. [4]

To assess a spring:
1. Measure flow monthly for at least one full year before committing it as a primary source.
2. After rainfall events, observe whether turbidity spikes — this indicates surface water connection and means you must treat for pathogens regardless of apparent clarity. [4]
3. A spring that runs clear within 48 hours of heavy rain has good aquifer protection; one that stays turbid for a week or more has a direct surface-water pathway.

**Well yield and aquifer testing:** A proper well yield test pumps the well at a controlled rate for 4–8 hours while monitoring drawdown. USGS methods distinguish between:

- **Specific yield** (unconfined aquifer): water drained by gravity when head declines
- **Storativity** (confined aquifer): water released from elastic storage under head decline [5]

For practical purposes, a 4-hour pump test that stabilizes drawdown at less than 50% of the water column indicates sustainable yield at that pumping rate. If drawdown continues accelerating, you are mining the aquifer — not using sustainable yield.

**Rule of thumb for residential wells:** A well yielding 1–2 gpm (1,440–2,880 gallons/day) is typically adequate for a household of 4 with water-efficient fixtures and a separate irrigation source. A 0.5 gpm well can serve a household with cistern storage and careful demand management.

### 1.4 Demand Modeling

Accurate demand modeling prevents both undersizing (system failure during peak demand) and oversizing (wasted capital).

**Household demand by category:**

| Use Category | Efficient (gal/person/day) | Standard (gal/person/day) | Notes |
|-------------|--------------------------|--------------------------|-------|
| Drinking and cooking | 1–2 | 2–3 | Fixed; cannot compress |
| Toilet flushing | 4–8 | 15–20 | Composting toilet: <1 |
| Shower/bathing | 8–15 | 20–30 | Low-flow showerhead critical |
| Laundry | 3–6 | 8–12 | HE washer vs. top-loader |
| Kitchen/dishes | 3–5 | 5–8 | |
| **Household total** | **~20–36** | **50–73** | EPA benchmark: 80–100 [6] |

**Agricultural demand** (irrigation) typically dominates a rural property's total budget. The Penman-Monteith equation is the international standard for calculating reference evapotranspiration (ET₀) from which crop water requirements are derived. A simplified field estimate: [7]

```
Crop water requirement (in/week) = ET₀ × Kc

Where:
  ET₀ = Reference evapotranspiration (NOAA data; ~1.5–2.5 in/week in summer for temperate US)
  Kc  = Crop coefficient (0.4–0.9 depending on crop and growth stage)
```

For 5,000 sq ft of mid-season vegetable garden with Kc = 0.8 and ET₀ = 2 in/week:
- Weekly irrigation need: 2 × 0.8 = 1.6 inches
- Volume: 1.6 in × (5,000 / 144) sq yd × 0.62 gal/in·sqft ≈ **500 gallons/week**

**Total property water budget summary worksheet:**

| Category | Daily Demand (gal) | Annual (gal) |
|----------|-------------------|-------------|
| Household (4 persons, efficient) | 120 | 43,800 |
| Livestock (2 beef cattle + 10 poultry) | 25 | 9,125 |
| Garden irrigation (5,000 sq ft, May–Sept) | 70 seasonal average | 12,600 |
| System losses (evaporation, leaks) | 5% of above | ~3,280 |
| **Total** | **~220** | **~68,800** |

Annual demand of 68,800 gallons against recharge of 217,800 gallons gives a theoretical surplus of 149,000 gallons — but this surplus is only accessible if storage capacity and distribution infrastructure can bridge seasonal demand-supply gaps.

---

## Section 2: Advanced Treatment Systems

Wave 0 covered boiling, chemical disinfection, and basic sand/biosand filtration. This section covers the systems that address what those methods cannot: dissolved chemical contaminants, scale-forming minerals, and high-volume treatment without consumable chemicals.

### 2.1 Understanding the Treatment Train Concept

No single treatment technology reliably addresses all contaminant categories. Professional water treatment is always a sequence — a **treatment train** — where each stage addresses specific threats and conditions the water for the next stage.

```
Raw Source Water
      │
      ▼
[Stage 1: Pre-filtration / Sediment]  ← Removes particles >5–50 microns
      │                                  Protects downstream equipment
      ▼
[Stage 2: Coarse filtration / Media]  ← Removes particles >1–5 microns
      │                                  Removes iron, manganese (with aeration)
      ▼
[Stage 3: Chemical treatment]         ← Carbon block: chlorine, VOCs, taste/odor
      │                                  Ion exchange: hardness, nitrates
      │                                  Acid/base: pH adjustment
      ▼
[Stage 4: Membrane / RO]              ← Removes dissolved solids, heavy metals,
      │                                  PFAS, nitrates, arsenic
      ▼
[Stage 5: Post-disinfection]          ← UV: kills any bacteria post-membrane
      │                                  Final polishing
      ▼
Treated Water to Use
```

The key principle: **never skip pre-treatment.** A reverse osmosis membrane exposed to sediment will fail within weeks instead of lasting years. An UV lamp treating turbid water loses disinfection effectiveness exponentially. Each stage protects the next.

### 2.2 Multi-Stage Sediment and Carbon Filtration

**Sediment pre-filter sizing:** Match to your source quality.
- Clear source water (well): 20–50 micron polypropylene cartridge, replaced every 3–6 months
- Moderately turbid source: 50 micron pre-filter → 20 micron → 5 micron sequence
- High-turbidity surface water: Media filter (sand/anthracite/gravel, 60-gallon backwash tank minimum) before cartridge filters

**Activated carbon:** Two forms with different applications:

| Type | Pore Size | Best For | Limitations |
|------|-----------|----------|------------|
| Granular Activated Carbon (GAC) | Large pores, high surface area | Chlorine, VOCs, taste/odor, some PFAS (long-chain) | Channels can form; bacteria can colonize |
| Carbon Block | Dense, fine pores | Chlorine, VOCs, cysts, some heavy metals, better PFAS contact time | Higher pressure drop; requires periodic replacement |

GAC achieves over 95% removal of long-chain PFAS (PFOS, PFOA) with an empty bed contact time (EBCT) of 10–20 minutes. Short-chain PFAS require longer contact or alternative treatment. [8] Replace GAC media before breakthrough — typically when influent PFAS or VOC concentrations start appearing in the effluent. Annual media testing is advisable for PFAS-contaminated areas.

**Microfiltration and ultrafiltration membranes:**

| Technology | Pore Size | Removes | Does Not Remove |
|-----------|-----------|---------|----------------|
| Microfiltration (MF) | 0.1–10 microns | Sediment, bacteria, some protozoa | Viruses, dissolved chemicals |
| Ultrafiltration (UF) | 0.01–0.1 microns | Bacteria, viruses, Giardia, Cryptosporidium | Dissolved minerals, metals |
| Nanofiltration (NF) | 0.001–0.01 microns | Most dissolved solids except monovalent ions | Sodium, chloride |
| Reverse Osmosis (RO) | <0.001 microns | Dissolved solids, most ions, PFAS | Nothing at >90% rejection |

UF systems require no electricity (gravity-fed designs exist) and provide reliable pathogen removal for biological-only contamination. They are the preferred low-energy option where chemical contamination is not a concern. [9]

### 2.3 UV Disinfection — Principles and Practical Application

Ultraviolet disinfection at 254 nm (UV-C) inactivates pathogens by inducing direct damage to nucleic acids and generating reactive oxygen species that damage DNA, proteins, and lipids. Pathogens cannot replicate after proper UV exposure. [10]

**Dose requirements for target pathogens (mJ/cm²):**

| Pathogen | 4-log inactivation dose |
|----------|------------------------|
| E. coli | 6–7 mJ/cm² |
| Giardia cysts | 5–10 mJ/cm² |
| Cryptosporidium oocysts | 3–10 mJ/cm² |
| Adenovirus (most resistant) | 30–150 mJ/cm² |

NSF 55 Class A certification requires ≥40 mJ/cm² at end-of-lamp-life with 5 NTU influent turbidity — this covers all common pathogens. Class B (16 mJ/cm²) covers bacteria only.

**Critical limitations:**
1. **Turbidity destroys UV effectiveness.** Water entering a UV system must be ≤1 NTU for Class A performance. At 5 NTU, dose delivery drops by 30–50%. Pre-filter to <1 NTU before UV.
2. **UV provides no residual.** Unlike chlorine, UV does not protect water after treatment. Ensure treated water has no contamination pathway.
3. **Lamp aging.** UV lamp output degrades over time, typically to 70% of initial output after 9,000–12,000 hours (about 1 year of continuous operation). Replace annually regardless of apparent function.
4. **UV does not remove any chemical contamination.** It addresses biological threats only.

**Solar disinfection (SODIS):** WHO recommends SODIS as an emergency backup when electricity is unavailable. Clear PET bottles filled with water turbid to <30 NTU placed in direct sunlight for 6+ hours (or 2 consecutive days under cloudy conditions) achieve 4-log bacteria reduction. Virus inactivation requires 6 hours at ≥150 W/m² solar irradiance. Cryptosporidium requires 8–12 hours with polypropylene containers. [11] SODIS is a last-resort method only — it is not reliable enough for daily primary treatment.

### 2.4 Ion Exchange Systems

Ion exchange replaces undesirable dissolved ions with less harmful ones using charged resin beads. The most common application is water softening, but the technology also addresses nitrates, arsenic, and PFAS.

**Water softening (hardness removal):**

Hard water contains calcium (Ca²⁺) and magnesium (Mg²⁺) that cause scale formation, reduce soap effectiveness, and damage appliances and distribution hardware. Water with hardness above 120 mg/L as CaCO₃ (7 gpg) benefits from softening for household use; water above 180 mg/L (10.5 gpg) causes aggressive scaling in pipes and water heaters within 2–3 years. [12]

A cation exchange softener passes water through sulfonated polystyrene resin beads charged with sodium ions (Na⁺). Calcium and magnesium displace the sodium and adhere to the resin; sodium is released into the water. When the resin is exhausted, backwashing with concentrated brine (NaCl solution) regenerates it by reversing the exchange.

**Sizing formula:**

```
Daily regeneration need (grains) = Hardness (gpg) × Daily flow (gallons)

Regeneration frequency = Resin capacity (grains) ÷ Daily need

Example:
  Hardness: 20 gpg
  Flow: 300 gpd (household of 4)
  Daily load: 20 × 300 = 6,000 grains/day
  32,000-grain resin tank → regenerates every ~5 days
```

**Considerations:** Softened water contains elevated sodium — roughly 8 mg of sodium per grain of hardness removed per liter. People on sodium-restricted diets should use potassium chloride regenerant instead, or install a separate bypass line for drinking water. [12] Softened water should not be used directly for irrigation; sodium accumulation in soil harms soil structure over time.

**Nitrate removal via anion exchange:** Anion exchange resins in chloride form can reduce nitrates from high-nitrate well water (common in agricultural areas). Specialty resins with nitrate selectivity over sulfate are required — standard water softeners do NOT remove nitrates. Target MCL: 10 mg/L as NO₃-N (EPA). [13] Regeneration produces a nitrate-concentrated brine requiring careful disposal — do not discharge to areas with shallow water tables.

**PFAS removal:** Single-use anion exchange resins (IX) are EPA-designated Best Available Technology for PFAS. They achieve >99% removal for long-chain PFAS and significantly better short-chain PFAS removal than activated carbon. Spent resin requires disposal as hazardous waste in some jurisdictions. [8]

### 2.5 Reverse Osmosis for Residential and Emergency Use

Reverse osmosis (RO) forces water at pressure through a semi-permeable membrane with pore sizes of <0.001 microns, rejecting dissolved solids, heavy metals, PFAS, arsenic, nitrates, and most other ionic contaminants at 90–99% rejection rates.

**What RO addresses that other methods do not:**
- Arsenic (MCL: 10 ppb) — especially in geological hotspots (New England, Southwest US, Midwest)
- Lead (<0.015 mg/L action level) — especially post-treatment when source water is fine but distribution infrastructure is not
- PFAS (MCL: 4 ppt PFOA/PFOS as of April 2024) [14]
- Nitrates (10 mg/L MCL) from agricultural contamination
- Total dissolved solids (TDS) in brackish groundwater

**Water efficiency — the critical limitation:** A standard POU RO system produces approximately 1 gallon of treated water for every 3–5 gallons sent to drain as concentrate (reject water). High-efficiency systems achieve 1:1 to 1:2 ratios. For off-grid systems with limited water supply, this reject ratio must be factored into the water budget. [15]

**RO system sizing:**

```
Required RO capacity (gpd) = Daily drinking/cooking demand × (Reject ratio + 1)

Example:
  Household drinking/cooking: 5 gallons/day
  Reject ratio: 4:1
  Required RO system throughput: 5 × 5 = 25 gpd
  Select a 25–50 gpd rated system with storage tank
```

**Pre-treatment requirements:** Without pre-treatment, RO membranes fail rapidly.
- SDI (Silt Density Index) must be <3 for RO
- Feed water pH should be 4–11 (adjust if outside range)
- Chlorine must be removed before RO (use carbon pre-filter) — chlorine destroys polyamide thin-film composite membranes
- Feed water hardness >200 mg/L requires anti-scalant dosing or softening before RO

**Mineral replacement:** RO removes beneficial minerals including calcium and magnesium. For long-term use, re-mineralize treated water with a calcite post-filter (raises pH and hardness) or ensure dietary mineral intake from food sources. [15]

**NSF/ANSI 58** certification is required by model plumbing codes for residential POU RO systems. Verify any purchased system carries this certification before deployment. [15]

---

## Section 3: Wastewater Integration — Cascading and Living Systems

The best-designed water system treats every outflow as a potential input. This section covers advanced wastewater integration: moving beyond the septic/greywater binary into cascading systems where water does useful work at each stage of its quality decline.

### 3.1 Greywater Cascading Principles

**The cascading concept:** Instead of sending all greywater to a single treatment system, route it through a sequence of uses that match water quality to task requirements:

```
Source Water (potable)
      │
      ▼
[Drinking, cooking, bathing]
      │
      ▼
Greywater (post-use, high BOD from soap/organics)
      │
      ▼
[Toilet flushing]  ← requires minimal treatment
      │
      ▼
[Laundry rinse]    ← reduces clean water demand if separate plumbing
      │
      ▼
[Sub-surface irrigation]  ← primary use for most greywater
      │
      ▼
[Constructed wetland / treatment] ← advanced polishing before discharge
```

A combined trickling filter and constructed wetland system has achieved TOC, TN, and TP removals from greywater of 83.5%, 85.5%, and 92.1% respectively, with a cascading multi-stage approach. [16]

**Designing a cascade:** The key principle is that water quality declines at each use and treatment restores it before the next use or final discharge. Match the quality standard to the actual need — toilet flushing does not require drinking water quality; subsurface irrigation does not require toilet-flushing quality.

**Volume accounting:** For a household of four using efficient fixtures:
- Greywater generated: ~140–200 gallons/day
- Toilet flushing demand: ~32–64 gallons/day (8 flushes × 4 people × 1.6 gpf)
- Net greywater available after toilet flushing: ~100–140 gallons/day for irrigation

If routing greywater to toilet flushing, install a gray-water holding tank (50–100 gallon capacity) with a float valve that switches to fresh supply when the gray tank is empty.

### 3.2 Constructed Wetlands for On-Site Treatment

Constructed wetlands are engineered systems that use wetland plants, soils, and microbial communities to treat wastewater through physical, chemical, and biological processes. They are proven, low-energy, low-maintenance treatment options for greywater, septic effluent, and stormwater. [17]

**Two primary types:**

| Type | Flow Pattern | BOD Removal | Pathogen Removal | Area Required | Odor Risk |
|------|-------------|-------------|-----------------|--------------|-----------|
| **Free Water Surface (FWS)** | Water flows above gravel/substrate | 85–95% | Moderate | 5–10 m²/PE | Moderate (open water) |
| **Subsurface Flow (SSF)** | Water flows through gravel/soil media | 80–95% | High (media filtration) | 3–8 m²/PE | Low (no surface water) |

SSF systems are preferred for residential applications due to lower odor and vector risk. Horizontal SSF designs are simpler; vertical SSF designs provide better nitrification for nitrogen removal. [17]

**EPA design criteria for SSF constructed wetlands:** [17]
- BOD₅ loading: ≤6 g/m²/day for secondary effluent target (30 mg/L)
- TSS loading: ≤20 g/m²/day
- Typical hydraulic retention time: 5–7 days
- Gravel media: washed ½" river gravel, hydraulic conductivity 300–3,000 m/day
- Water depth: 0.3–0.6 m

**Sizing a residential SSF wetland:**

```
For a household of 4, targeting secondary treatment of septic effluent:

Design flow = 4 persons × 75 gpd = 300 gpd = 1,135 L/day
Required area = Design flow ÷ BOD loading rate

Influent BOD (septic effluent) ≈ 150 mg/L
Target effluent BOD ≈ 20 mg/L
BOD to remove: 130 mg/L × 1,135 L/day = 147,550 mg/day = 148 g/day

Area = 148 g/day ÷ 6 g/m²/day = ~25 m² (270 sq ft)
```

A 270 sq ft SSF wetland is a practical, residential-scale installation — approximately 12 ft × 22 ft. Use a liner (HDPE or EPDM), set gravel bed with inlet distribution pipe at one end and outlet collection pipe at the other, plant with *Phragmites australis* (common reed), *Typha* spp. (cattail), or *Scirpus* (bulrush) at 4–6 plants/m².

**Nitrogen and phosphorus removal:** Nitrogen removal requires anaerobic denitrification after aerobic nitrification — achievable in a two-stage SSF system or by recirculation. Phosphorus removal via constructed wetlands is limited (10–30%) unless iron- or aluminum-rich media is used as an adsorptive substrate. For high-nutrient applications, supplement with a phosphorus-adsorbing media layer (blast furnace slag, steel slag) or follow with a sand-filtration polishing step. [18]

**Plants for constructed wetlands — regional selection guide:**

| Plant Species | Climate Range | Nitrogen Uptake | Notes |
|--------------|---------------|----------------|-------|
| *Phragmites australis* | USDA zones 4–9 | High | Aggressive spreader; contain edges |
| *Typha latifolia* (cattail) | Zones 3–10 | Moderate | Excellent for cold climates |
| *Scirpus acutus* (bulrush) | Zones 4–10 | High | Good cold tolerance |
| *Iris pseudacorus* | Zones 5–9 | Moderate | Less aggressive; attractive |
| *Cyperus papyrus* | Zones 9–11 | High | Tropical; greenhouse use in cold climates |

### 3.3 Living Machines

The Living Machine, pioneered by ecological designer Dr. John Todd beginning in the 1970s, is an intensified version of wetland ecology for contained spaces. [19] It simulates a wetland ecosystem using sequentially arranged ecological cells filled with diverse plant communities, bacteria, fungi, algae, and small aquatic animals. The result is wastewater treatment within a building footprint, with treated water suitable for toilet flushing or sub-surface irrigation.

**How it works — the cell sequence:**

```
[Anaerobic reactor] → [Aerated cells with algae + microorganisms]
     → [Wetland plant cells] → [Clarifier] → [Treated water reuse]
```

Each cell provides different treatment conditions: the anaerobic reactor breaks down BOD and TSS; aerated cells promote nitrification; wetland plant cells enable nutrient uptake and final polishing; the clarifier removes residual suspended solids.

**Performance:** Operating installations achieve secondary (30/30 BOD/TSS) to tertiary (10/10) treatment standards without chemical inputs. Worrell Water Technologies systems are operating in over two dozen locations worldwide. [19]

**Footprint:** A Living Machine serving 50 PE (person equivalents) typically requires 1,000–2,000 sq ft of indoor growing space — feasible for institutional or community-scale applications. Below 10 PE, simpler constructed wetland designs typically deliver equivalent results at lower cost.

**Suitability:** Living machines are best suited to:
- Institutional buildings (schools, offices, retreat centers) needing on-site water recycling
- Communities in cold climates where outdoor constructed wetlands are seasonally impaired
- Sites where LEED certification or ecological demonstration is a program goal

---

## Section 4: Water Storage Optimization

Storage is the bridge between variable supply and consistent demand. Getting storage right means more than choosing a tank size — it means managing thermal behavior, sediment dynamics, biological stability, and long-term structural integrity.

### 4.1 Storage Sizing for Resilience

**The 30-60-90 day rule:** A resilience-focused storage target:
- **30 days** — minimum functional buffer against pump or well failure
- **60 days** — appropriate for areas with >45-day dry seasons
- **90 days** — target for full water self-sufficiency in most climates

```
Storage volume (gallons) = Daily demand (gpd) × Storage days

Example: 220 gpd household × 90 days = 19,800 gallons
```

This is typically achieved with multiple tanks rather than one large vessel: 2–4 poly tanks of 1,500–5,000 gallons each, connected in series for sequential fill and parallel for simultaneous draw.

**Dead storage fraction:** Tanks never fully empty in practice — sediment accumulates at the bottom, and suction pipes should be positioned 4–6 inches off the tank floor to avoid drawing sediment. Plan for 10–15% dead storage (unusable volume) in your sizing calculation.

### 4.2 Underground Storage and Thermal Mass

Underground cisterns (buried concrete, fiberglass, or HDPE) offer significant advantages over above-ground storage:

1. **Freeze protection:** Below the frost line (typically 4–6 feet in northern US), water remains above freezing year-round without any active heating. [20]
2. **Thermal stability:** Soil acts as a large thermal mass, maintaining water temperature at 50–60°F year-round in temperate climates. This reduces biological growth rates compared to warm above-ground tanks.
3. **Evaporation elimination:** Sealed underground cisterns lose negligible water to evaporation, critical in arid climates where open surface storage can lose 5–7 feet of depth annually.
4. **Pressure head:** A buried cistern with a riser pipe can provide low-pressure gravity feed to a distribution system, reducing pump energy requirements.

Historical underground cisterns in arid Iran maintained stored water at 12–13°C through summers reaching 42°C ambient, with an average energy storage time constant of approximately 8 months. [21] This thermal inertia is a genuine operational advantage.

**Underground cistern construction standards:**
- Concrete cisterns: minimum 4-inch walls with #4 rebar on 12" centers; waterproofed with two coats crystalline waterproof coating on interior
- Fiberglass: pre-manufactured underground tanks rated for burial depth; verify manufacturer's burial depth ratings — overloading causes wall collapse
- HDPE poly: not suitable for burial unless specifically rated; above-grade use only
- Any potable storage vessel must meet NSF 61 for material safety [22]

### 4.3 Sediment Management

Sediment accumulates in all storage vessels. Fine silts and clays from surface water, pipe corrosion products, and calcium carbonate precipitation settle to create a biofilm-friendly sludge layer that harbors pathogens and degrades water quality.

**Prevention strategies:**
- First-flush diverter (rainwater systems): diverts the first 1–2 gallons per 100 sq ft of catchment area, which carries 80–90% of accumulated surface contaminants [22]
- Inlet configuration: introduce water at the top of the tank via a downturned elbow to prevent disturbance of settled sediment
- Outlet/suction pipe: position 4–6 inches above tank floor; use foot valve with screen to prevent backflow and sediment draw
- Pre-filtration: 100-micron inlet screen minimum for all surface water sources

**Removal schedule:**
- Inspect annually: shine a flashlight through an inspection port; visible settled layer >½" indicates cleaning is overdue
- Clean every 2–3 years for well-protected rainwater systems
- Clean annually for surface water systems with high sediment load
- Deep clean: drain tank, remove sediment with scooping tool and wet/dry vac, scrub interior walls with 1:10 bleach solution, rinse thoroughly, refill

**Disinfection after cleaning:** After any tank cleaning, chlorinate to 50 ppm using unscented household bleach (8.25%):

```
Chlorine dose (oz of bleach) = Tank volume (gallons) ÷ 100 × 0.6

Example: 2,500-gallon tank × 0.006 = 15 oz bleach
Allow 24-hour contact time, then flush before returning to service
```

### 4.4 Long-Term Water Preservation

Water stored for emergency use (72-hour to 6-month reserves) degrades over time through:
- Chlorine loss (tap water loses residual chlorine within 1–2 weeks)
- Bacterial regrowth (any viable cell can multiply in a nutrient-rich storage environment)
- Plastic leaching (compounds from container walls migrate into water over months)

**Commercial storage (55-gallon food-grade barrels, NSF 61 rated):**
- Add sodium hypochlorite to 1–4 mg/L residual if source water is chlorinated
- Store in a cool, dark location (temperature variation accelerates chemical processes)
- Rotate every 6 months — empty, clean, refill
- Use a food-grade bung with a closed vent; never store in containers that held chemicals

**Extended storage (>6 months):** Add 8 drops of unscented bleach per gallon (achieving ~5–10 ppm chlorine) and seal tightly. This maintains disinfection for 1–2 years if stored <70°F. Test with pool test strips before use; re-dose if residual drops below 0.5 ppm. [22]

---

## Section 5: Water Testing and Monitoring

Advanced water management requires a systematic testing protocol, not one-off testing. Your water quality changes seasonally, responds to land-use changes, and may shift gradually over years in ways that require trend analysis to detect.

### 5.1 Field Testing Capabilities and Limits

Field tests provide rapid results but have fundamental limitations in sensitivity, specificity, and detection range. Understanding these limits prevents false confidence.

**Field-testable parameters:**

| Parameter | Field Method | Detection Range | Limitation |
|-----------|-------------|----------------|-----------|
| pH | Test strips or digital meter | 4–10 | Strips: ±0.5 accuracy only |
| Total Dissolved Solids (TDS) | Conductivity meter | 0–2,000 ppm | Does not identify which solids |
| Free chlorine | DPD colorimetric test | 0–5 mg/L | Interferes with some organics |
| Nitrates | Colorimetric test strips | 0–50 mg/L | ±20% accuracy; cannot distinguish NO₃-N from NO₂-N |
| Turbidity | Turbidity tube (Secchi-type) | >5 NTU | Low precision below 5 NTU |
| Coliform bacteria | Presence/absence test (24–48 hr incubation) | Qualitative | Cannot distinguish E. coli from other coliforms; false negatives possible at low concentrations |
| Hardness | Titration kit | 0–500 mg/L as CaCO₃ | Good accuracy; ±10 mg/L |
| Iron | Colorimetric strip | 0–3 mg/L | Cannot distinguish ferrous from ferric iron |

**Parameters that require laboratory analysis:** Arsenic (<10 ppb MCL requires detection below field-test capability), lead (EPA action level 15 ppb is below reliable field detection), PFAS (4 ppt MCL requires high-sensitivity analytical chemistry), pesticides/herbicides, radionuclides (radon, radium), volatile organic compounds.

### 5.2 Laboratory Testing Protocol

**Annual baseline testing** (private wells and non-municipal sources): [23]
- Total coliform and E. coli (EPA Colilert or equivalent method)
- Nitrates/nitrites as nitrogen (colorimetric)
- Total dissolved solids
- pH and hardness

**Every 3–5 years (or after land-use changes nearby):**
- Heavy metals panel: arsenic, lead, manganese, iron, barium, chromium
- Fluoride
- Radionuclides (if in geological risk area — New England granite, Rocky Mountain region)

**Triggered testing (perform after any of these events):**
- Nearby agricultural chemical application (test pesticides, herbicides, nitrates)
- Flooding that submerges well head (test coliform, E. coli, turbidity)
- Change in taste, color, or odor (full panel)
- New industrial development within 2 miles (PFAS, VOCs, metals)
- Infant in household (test lead and nitrates — infants are especially vulnerable)

**PFAS testing:** The 2024 EPA MCLs at 4 ppt PFOA/PFOS require Method 533 or 537.1 analysis — available from EPA-certified labs only. [14] Recommended if: property is within 1 mile of a PFAS source (military bases, industrial sites, airports using AFFF foam, certain manufacturers).

### 5.3 Interpreting Results and Treatment Decisions

**Decision framework:**

```
Test result received
      │
      ├─ Is any MCL exceeded? → YES: Stop use for affected purpose immediately
      │                               Identify treatment technology (Sections 2.2–2.5)
      │                               Retest after treatment installation
      │
      ├─ Is any result near (>50% of) MCL? → YES: Retest quarterly
      │                                            Investigate source
      │                                            Begin treatment planning
      │
      └─ All results below MCL: → Continue annual monitoring
                                    Note any upward trends
```

**The trend warning:** A single result below the MCL is not fully reassuring if the trend is rising. A nitrate result at 7 mg/L (MCL: 10 mg/L) that was 4 mg/L two years ago warrants investigation and more frequent monitoring — not a clean bill of health.

**When to use an NSF-certified laboratory:** Always for regulatory compliance, legal property transactions, and when results will inform treatment system design. NSF-certified labs participate in proficiency testing programs; uncertified labs have no quality assurance verification.

---

## Section 6: Seasonal and Climate Adaptation

A water system sized for average conditions will fail during extremes — the events that most demand reliable supply. Design for your 20th percentile year (dry year drought), your coldest recorded temperature, and your maximum observed flood event.

### 6.1 Freeze Protection

Water freezes at 32°F (0°C) and expands 9% in volume. This expansion will rupture any closed container — pipes, tanks, pump housings, filter housings, or distribution lines — if not protected.

**Below-grade protection:** Bury all water-carrying infrastructure below the frost depth for your region. USDA frost depth maps show:
- Deep South: 0–6 inches
- Mid-Atlantic, Pacific Northwest: 12–24 inches
- Upper Midwest, New England: 48–72 inches
- Northern Minnesota, Alaska: 72–120+ inches

All distribution lines should be buried at least 12 inches deeper than the regional frost line. [24] Freeze failures most commonly occur at inadequately buried fittings, where lines emerge from the ground, and at poorly insulated above-grade installations.

**Above-grade tanks:** Wrap with closed-cell foam insulation (R-10 minimum for zone 5+ climates). Dark-colored tanks absorb solar heat gain — HDPE black tanks perform significantly better than white ones in marginal freeze conditions. For sustained temperatures below -10°F, active protection is required:
- Thermostatically controlled heat tape on pipes (thermostat set at 38°F, not continuous — this wastes significant energy)
- Small submersible aquarium heater (50W) in a 500-gallon tank can prevent freezing to -20°F ambient if tank is insulated [24]
- Stock tank heaters (150–500W de-icers) for livestock water tanks

**Pump and filter housing protection:**
- Well pump houses: install thermostatically controlled heat cable on drop pipe and a 40–60W incandescent bulb (not LED — must generate heat) inside the well house
- Filter housings: drain and remove cartridges from any housing that cannot be protected to above 35°F
- Pressure tanks: locate inside heated space; if outside, insulated enclosure with heat tape

**Winterizing seasonal systems:** For systems not in year-round use, follow this sequence:
1. Shut off supply
2. Open all lowest-point drain valves and faucets
3. Use compressed air (30–50 psi) to blow out all lines from highest to lowest point
4. Remove and store all cartridge filters
5. Add non-toxic RV antifreeze (propylene glycol) to pump bodies, filter housings, and trap sections
6. Drain hot water heater if temperature will drop below 35°F

### 6.2 Drought Contingency Planning

Drought planning operates on three levels: conservation, supplementation, and emergency rationing.

**Level 1 — Conservation (reduce demand 20–30%):**
- Identify and repair all leaks (a dripping faucet wastes 3 gallons/day; a running toilet, 200 gallons/day)
- Shift outdoor irrigation to deficit irrigation: water to 70% of full ET requirement; most established plants tolerate this without yield loss
- Grey-to-garden routing: any treated greywater not yet in service goes to irrigation before drawing from primary storage
- Mulch all irrigated areas with 4-inch organic mulch layer: reduces evaporation by 50–70%

**Level 2 — Supplementation (alternative sources):**
- Pre-identified backup sources: neighbor's well (reciprocal agreement before drought onset), community water source, municipal fill station for cisterns
- Water delivery: determine haul cost and tank access points in advance; 1,000 gallons delivered typically costs $100–$200 in rural US
- Graywater maximization: connect any previously bypassed gray sources to irrigation
- Pool/pond emergency reserve: surface water with no treatment history should be treated as contaminated; filter and disinfect before any potable use

**Level 3 — Emergency rationing:**

WHO minimum survival quantity: 15 liters (4 gallons) per person per day for drinking, cooking, and basic hygiene. [7] At this level, all non-essential uses (irrigation, livestock not critical to food security, all cleaning beyond minimal hygiene) are suspended.

**Level 3 water budget (4 persons, 3-week emergency):**
- Drinking and cooking: 2 gal/person/day × 4 × 21 = 168 gallons
- Basic hygiene: 1 gal/person/day × 4 × 21 = 84 gallons
- **Total: 252 gallons** — approximately 6 standard 55-gallon barrels

Maintaining this pre-positioned emergency reserve, refreshed semi-annually, is the most important drought resilience investment a household can make.

### 6.3 Flood Management and Water Quality After Flooding

Flooding is a dual threat: it can both inundate infrastructure (damaging pumps, contaminating cisterns) and deliver sudden high-volume surface water that could supplement supply if managed safely.

**Protecting wells and cisterns from flood contamination:**
- Well head should be at least 1 foot above the 100-year flood plain elevation
- If flooding submerges a well head, assume contamination: test for coliform, E. coli, turbidity, and nitrates before any use
- Shock-chlorinate the well after flooding: add sufficient bleach to achieve 50–100 ppm chlorine in the well water column, let stand 12 hours, pump out until chlorine odor is gone, test before returning to service [22]

**Stormwater diversion and retention for supply:**
- Swales on contour: level earthwork channels that intercept and redirect surface flow into storage basins or infiltration areas. A swale with 3:1 side slopes and 1-foot depth captures roughly 50 gallons per linear foot of swale volume. [25]
- Diversion berms: compacted earth ridges positioned to redirect flood flow away from structures; typically designed to handle a 25-year storm event
- Retention basins: sized to capture the volume of the design storm event minus what infiltrates during the event; a 1,000 sq ft basin 4 feet deep holds approximately 3,000 gallons net

**Flood water as supply source:** Surface water after flood events carries extremely high turbidity, pathogen loads, and potentially chemical contamination from agricultural runoff, sewage, and petroleum. Do not use flood water for any potable purpose without complete treatment through sediment filtration, activated carbon, UV disinfection, and water quality testing.

---

## Section 7: System Integration

Water operates in ecological and functional relationships with every other resilience system on a property. Treating it as isolated infrastructure misses substantial optimization opportunities.

### 7.1 Water and Food Production

**Direct irrigation integration:**
- Zone irrigation by water quality: cleanest water to root vegetables and salad greens; treated greywater to fruit trees, established perennials, and non-edible ornamentals; drip irrigation for all food crops (eliminates foliar contact with water carrying biological risk)
- Mulched swales below food crops: capture irrigation runoff as infiltration; reduce total irrigation demand 30–50% by maintaining soil moisture

**Aquaponics as closed water loops:** Recirculating aquaponics systems use fish waste as plant nutrients and plants as biological filters — fish water is used for plant growth; plants return filtered water to the fish. Water use is reduced to approximately 2% of the requirement for equivalent soil-grown vegetables. [26] Recirculating systems return 95–99% of water to the system, with losses only from evapotranspiration through plant leaves and water incorporated into harvested crops.

A small aquaponics system (200 gallon fish tank + 100 sq ft media bed) requires makeup water of approximately 2–3 gallons/day to replace evapotranspiration losses. This makes aquaponics one of the most water-efficient food production methods available.

**Irrigation scheduling for water budget adherence:**
- Install tensiometers or simple capacitance soil moisture sensors to trigger irrigation only when soil moisture falls below field capacity threshold
- Soil at field capacity holds 1–2 inches of available water per foot of depth; irrigate before plant stress at 50–70% depletion
- Drip irrigation at 90% efficiency vs. overhead sprinklers at 70% efficiency: for the same crop, drip reduces water use by approximately 20%

### 7.2 Water and Energy Systems

**Gravity-fed distribution:** Elevating storage tanks eliminates pump energy for distribution. A tank positioned 2.31 feet above the point of use produces 1 psi of pressure. For typical household distribution (20–40 psi minimum needed), the tank needs to be 46–92 feet above the lowest fixture. [27]

On hilly properties, gravity feed from a hillside spring or elevated tank to a lower homesite is one of the most energy-efficient water distribution solutions available. Gravity systems have zero operating energy cost and fail only from pipe blockage, not power outages.

**Micro-hydro energy generation:** If your site has flowing water with measurable head (vertical drop), micro-hydro generation is often more reliable and cost-effective than solar for off-grid power. The power output formula:

```
Power (watts) = Net Head (ft) × Flow (gpm) × 0.18 × Turbine efficiency (0.40–0.70)

Example: 40 ft head × 30 gpm × 0.18 × 0.55 = 119 watts continuous

Over 24 hours: 119W × 24h = 2.86 kWh/day
Annual generation: 2.86 × 365 = 1,044 kWh/year
```

Key thresholds: 10 ft head and 10 gpm flow is the practical minimum for useful power generation. Above 20 ft head and 20 gpm, micro-hydro typically outperforms a similarly-sized solar array in terms of levelized energy cost, particularly in cloudy or forested environments. [27]

**Water in energy storage:** Large volumes of water have significant thermal mass — 1 gallon of water stores approximately 8.3 BTU per degree Fahrenheit. A 5,000-gallon storage tank can act as a thermal battery, absorbing heat from solar thermal collectors and releasing it slowly for space heating or domestic hot water. This is a mature technology; solar thermal systems with storage tank integration have been in use since the 1970s.

**Pump energy optimization:** Well pump energy is often the largest electrical load in an off-grid water system. Strategies to reduce it:
- Match pump flow rate to system demand — oversized pumps that short-cycle consume more energy than correctly sized pumps running at full load
- Pressure tanks sized at 10× the pump flow rate in gallons minimize short-cycling: a 10 gpm pump should have a 100-gallon pressure tank
- Solar-direct pumping (pump runs only when sun shines, into storage) eliminates battery energy losses for pump operation

### 7.3 Water and Waste Management

**Composting toilet effluent:** Composting toilets eliminate the blackwater stream — the high-pathogen component that requires the most intensive treatment — from the waste management equation. A well-managed composting toilet serving a household of 4 produces approximately 50–80 lbs of finished compost annually, usable on non-edible plantings, orchards, or perennial beds after meeting the full composting standard (12+ months at adequate temperature). This eliminates 40–60 gallons/day of blackwater generation.

**Biogas capture from concentrated waste:** If managing manure (livestock) or concentrated organic waste, anaerobic digestion produces biogas (methane) as a byproduct. The water separated from digested slurry (digestate liquid) is a nutrient-rich, relatively pathogen-reduced fertilizer appropriate for subsurface injection into field crops.

**Vermicomposting and kitchen greywater:** Kitchen sink water rich in food particles can be pre-filtered through a vermicomposting (worm bin) pre-treatment filter before the greywater cascade. Worms consume organic solids, dramatically reducing BOD in the water before it enters the constructed wetland or drip system.

---

## Section 8: Maintenance and Troubleshooting

A water system that isn't maintained is a ticking clock toward failure, often at the worst possible moment. Preventive maintenance schedules, based on manufacturer specifications and performance data, are more reliable than reactive troubleshooting.

### 8.1 Scheduled Maintenance Calendar

**Monthly:**
- Check pressure tank for correct pre-charge pressure (2 psi below pump cut-in pressure, measured with pump off and tank depressurized)
- Inspect first-flush diverter: verify float is seated and diverter is reset after recent rain
- Check filter pressure differential: if pre/post filter pressure drop exceeds 15 psi, replace cartridge
- Test free chlorine residual in storage (should be 0.2–0.5 mg/L for maintained storage)

**Quarterly:**
- Run bypass on UV system and inspect lamp for mineral deposits; clean quartz sleeve with citric acid solution if coated
- Check pump runtime logs or cycle counter: increasing cycles per hour indicates pressure tank problems or demand leak
- Inspect all distribution line visible sections for seepage, rodent damage, freeze damage
- Test water quality basics: pH, TDS, chlorine residual, turbidity

**Annually:**
- Replace UV lamp regardless of apparent function (lamp output degrades; budget replacement into annual operating cost)
- Replace RO membrane pre-filters (sediment and carbon cartridges)
- Test RO system rejection rate: measure TDS pre- and post-membrane; rejection should be >90%; membrane replacement indicated if below 80%
- Pull and inspect any submersible pump installed >5 years ago: check motor amp draw against nameplate rating; rising amp draw indicates impeller wear
- Full water quality laboratory test

**Every 3–5 years:**
- Drain and clean all storage tanks
- Inspect and replace any rubber components (diaphragm in pressure switch, bladder in pressure tank, gaskets throughout)
- Comprehensive well inspection: video inspection if >10 years old, check well casing integrity, measure static water level

### 8.2 Diagnosing Common System Failures

**No water at fixtures:**

```
Check breaker/power to pump → Check pressure switch contacts (test: jump across contacts)
  → Check pump amp draw at disconnect → Compare to nameplate amps
    → High amps: pump blocked or failed → Low amps: motor failed or pump not primed
```

**Low pressure:**

- Waterlogged pressure tank: tap test — hollow sound should occupy top third; if solid throughout, bladder has failed. Check air valve: water coming out (not air) confirms bladder failure. Replace tank.
- Partially plugged sediment filter: measure pressure pre/post filter; >15 psi drop indicates clogged cartridge
- Pump partial failure: pump running but delivering less flow — impeller wear, especially in submersible pumps >8 years old

**Pressure cycling rapidly (short cycling):**

Short cycling — pump switching on and off every few seconds — is almost exclusively caused by a waterlogged pressure tank. A bad capacitor accounts for approximately 90% of outright pump motor failures. [28] Replace the pressure tank; if cycling continues, test the capacitor (discharge it safely first).

**Yellow/brown water:**

- Rust or iron: sediment pre-filter + oxidation/aeration + catalytic carbon or iron removal media
- Manganese: above pH 8 in an aerating filter OR potassium permanganate regenerating media; manganese MCL: 0.05 mg/L (secondary, aesthetic)
- Tannins (surface water): activated carbon + coagulation/flocculation; water turns brown-orange and leaves stains

**Sulfur odor (rotten egg smell):**

Hydrogen sulfide (H₂S) in water, produced by sulfur-reducing bacteria in the aquifer or water heater. Not necessarily a health risk at low concentrations but highly objectionable. Treatment: aeration (shock-chlorinate water heater to eliminate bacteria colonization of heater); or chlorination followed by activated carbon to remove chlorine and residual H₂S.

### 8.3 Scale Management

Calcium carbonate scale (limescale) forms when hard water is heated or when CO₂ is degassed. Scale acting as thermal insulation forces systems to consume up to 25% more energy to heat water through the limescale layer. [29] Scale also reduces pipe diameter — a 1-inch pipe scaled to ½-inch effective bore flows at 25% of its original capacity (Hazen-Williams relationship: flow varies as diameter^2.63).

**Scale prevention:**
- Ion exchange softening: removes calcium and magnesium before heating; most effective prevention
- Phosphate dosing: food-grade polyphosphate sequesters calcium ions, preventing crystallization; used in municipal systems and residential inline feeders
- Template-assisted crystallization (TAC): forces aragonite rather than calcite crystal formation — aragonite does not adhere to surfaces; no salt required, no discharge concern [29]
- Magnetic water conditioners: some evidence of effectiveness for scale form modification; results are inconsistent and not reliably reproducible across studies

**Chemical descaling (existing scale):**
- Citric acid (10% solution): safe, effective for light to moderate carbonate scale; circulate for 30–60 minutes, rinse thoroughly; food-safe
- Vinegar (5% acetic acid): works for accessible fixtures, shower heads, aerators; soak 30–120 minutes
- Hydrochloric acid (10% dilution): rapid and effective; requires full PPE (gloves, goggles, ventilation); not suitable for aluminum or galvanized components; follow with thorough water flush before returning to service

---

## Section 9: Regulatory Compliance by Region

Water law is a major operational constraint for any water system beyond the most minimal household use. Getting the regulatory picture wrong can result in fines, forced removal, or loss of water rights that took decades to establish.

### 9.1 Surface Water Rights — Prior Appropriation vs. Riparian Doctrine

The United States operates under two fundamentally different surface water legal systems, determined largely by climate history. [30]

**Eastern US — Riparian Doctrine:**
Riparian rights tie water use rights to ownership of land adjacent to a watercourse. If your land borders a stream, you have the right to make "reasonable use" of that stream — but you cannot divert and store large quantities, and you cannot use the water in ways that significantly harm downstream users.

States: Alabama, Arkansas, Connecticut, Delaware, Florida, Georgia, Illinois, Indiana, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, New Hampshire, New Jersey, New York, North Carolina, Ohio, Pennsylvania, Rhode Island, South Carolina, Tennessee, Vermont, Virginia, West Virginia, Wisconsin

**Western US — Prior Appropriation ("First in time, first in right"):**
Prior appropriation grants water rights based on beneficial use priority date, regardless of land ownership. The first person to divert water for beneficial use has senior rights that cannot be curtailed even by landowners with adjacent land. [30]

States using prior appropriation only: Arizona, Colorado, Idaho, Montana, Nevada, New Mexico, Utah, Wyoming

States with dual systems: California, Kansas, Nebraska, North Dakota, Oklahoma, Oregon, South Dakota, Texas, Washington

**Prior appropriation requirements:** To establish a water right in a prior appropriation state typically requires:
1. File a permit application with the state water board before beginning diversion
2. Demonstrate a beneficial use (domestic, agricultural, municipal, industrial)
3. Construct the diversion and begin use by the priority date
4. Report annual use to the state

Failure to use the full appropriated amount consistently can result in loss of the right under "use it or lose it" provisions.

### 9.2 Groundwater Rights

Groundwater rights vary independently of surface water rights — a parcel can have strong surface water rights and severely restricted groundwater rights, or vice versa. Five principal doctrines govern groundwater:

| Doctrine | Right Basis | Common in | Key Implication |
|---------|------------|-----------|-----------------|
| Absolute Dominion (English Rule) | Landowner owns all water beneath their land | Some eastern states | Can pump without regard to neighbor impacts |
| Reasonable Use | Can pump if used on overlying land, no export | Texas (surface) | Common in humid states |
| Correlative Rights | Proportional sharing in shortage | California | Adjudicated basins |
| Prior Appropriation | First in time, first in right | Most western states | Permit required before drilling |
| Restatement (Modern) | Unreasonable interference with another's right | Growing adoption | Negligence-based liability |

**Critical practical point:** Even in "absolute dominion" states, pumping that causes a neighbor's well to go dry will increasingly result in civil liability as aquifer depletion becomes more common. Pumping test your well and understand the aquifer conditions before installing high-capacity pumps. [31]

### 9.3 Rainwater Harvesting Regulations

Most US states permit residential rainwater harvesting without restriction. As of 2026, the regulatory landscape by region:

| Region | General Status | Notable Restrictions |
|--------|---------------|---------------------|
| Pacific Northwest (WA, OR) | Permitted; Oregon requires permit for large systems | WA allows up to 10,000 gal/year uncollected |
| Southwest (AZ, NV, NM) | Actively encouraged; some rebates | AZ: unlimited; NV: 100 gal max without permit |
| Mountain (CO, UT, ID) | Colorado legalized in 2016 (max 110 gal/property) | Utah allows potable use with certification |
| Midwest/South | Generally unrestricted | State-specific agricultural use restrictions |
| Texas | Actively promoted; tax exemptions available | No permit required for residential |
| Southeast | Generally unrestricted | Florida offers incentives |

**Colorado's unique situation:** Colorado, as a prior appropriation state, historically prohibited rainwater collection because every rain drop was claimed by downstream appropriators. The 2016 legislation created a narrow residential exemption: two rain barrels, maximum 110 gallons combined, for outdoor use only. This illustrates the tension between water law and modern sustainable practice that exists throughout the arid West. [30]

### 9.4 Wastewater Discharge Standards

**Septic and subsurface treatment:** Construction of any septic system, constructed wetland, or subsurface disposal field requires a permit from the county health department or state environmental agency in all US jurisdictions. Minimum setbacks are typically:
- 50 feet from any well
- 100 feet from any surface water
- 25 feet from property lines
- Per perc test results for soil infiltration rates

**Greywater reuse:** A growing number of states now have specific greywater codes, typically based on the International Plumbing Code (IPC) Appendix C framework:
- Direct permit-exempt reuse: California, Arizona, Texas, New Mexico, Montana (specific conditions apply)
- Permit required: most other states; contact state environmental or plumbing office
- Prohibited or no code: a shrinking list; check current state law before installation

**Surface discharge:** Any surface discharge of treated wastewater (to a stream or water of the state) requires an NPDES (National Pollutant Discharge Elimination System) permit under the Clean Water Act. [32] This applies regardless of treatment quality. Residential systems discharging to the surface are rarely practical — use subsurface disposal instead.

**Where to get current regulatory information:**
- State environmental or water quality agency (primary authority)
- [National Agricultural Law Center water law overview](https://nationalaglawcenter.org/overview/water-law/) [30]
- [California State Water Resources Control Board (model for western prior appropriation)](https://www.waterboards.ca.gov/waterrights/board_info/faqs.html) [31]
- County health department (septic permits, well construction)

---

## Section 10: Rainwater vs. Groundwater vs. Surface Water — Trade-off Analysis

Choosing a primary water source is not a preference decision — it's an engineering decision based on available resources, intended use, site hydrology, treatment capacity, and regulatory context.

### 10.1 Rainwater

**Best for:** Sites with >25 inches annual rainfall, good roof catchment area, and modest demand (household without large irrigation)

**Advantages:**
- No extraction permit required in most states
- Quality starts high (near-distilled, low TDS, low hardness)
- Zero aquifer impact
- Fully under owner control — no shared aquifer, no upstream diversions

**Disadvantages:**
- Highly seasonal — requires substantial storage to bridge dry periods
- Roof and gutter materials matter: metal roofs are best; asphalt roofs contribute volatile compounds; wood roofs are contaminated with preservatives
- Bird and wildlife feces on collection surfaces introduce biological contamination
- Not viable as sole source in <15 inches annual rainfall without impractically large catchment

**Equipment baseline for potable rainwater:**
- Metal roof + gutters + first-flush diverter
- Pre-filter (100-micron inlet screen)
- Storage tank (NSF 61 rated, food-grade)
- Pre-treatment sediment cartridge
- Activated carbon cartridge
- UV disinfection unit (NSF 55 Class A)
- Annual E. coli and turbidity testing

**Typical system cost (1,000-gallon potable storage):** $3,500–$8,000 including tank, treatment train, and plumbing

### 10.2 Groundwater (Wells and Springs)

**Best for:** Properties in areas with reliable aquifers; primary residential water supply for rural properties without municipal service

**Advantages:**
- Year-round supply independent of surface precipitation
- Naturally filtered through soil and rock — lower biological load than surface water
- Consistent quality (changes slowly over years, not weeks)
- No storage required for use (pressure tank handles day-to-day buffering)

**Disadvantages:**
- Well drilling cost: $15–$35/foot typically; $5,000–$30,000+ for a properly constructed well
- Quality reflects aquifer geology — arsenic (New England granite, Rocky Mountain), radium (upper Midwest), iron (Southeast Coastal Plain), hydrogen sulfide (confined aquifers), and nitrates (agricultural areas) are common
- Aquifer depletion is real in overdrafted regions (Central Valley CA, Ogallala in western Kansas/Oklahoma/Texas panhandle, Phoenix basin AZ)
- Dependent on pump and electricity — a power outage without backup means no water

**Site-specific risks requiring investigation before drilling:**
- USGS hydrogeologic atlas for your aquifer type [1]
- Historical data from state well log databases
- Local well driller knowledge of aquifer behavior

### 10.3 Surface Water

**Best for:** Sites adjacent to reliable streams or rivers; supplemental irrigation supply; small-community water systems with treatment capacity

**Advantages:**
- Renewable and replenished seasonally
- No drilling required
- Visible source — problems often detectable without testing
- Can integrate with gravity-fed systems

**Disadvantages:**
- Highest pathogen load of the three source types — E. coli, Giardia, Cryptosporidium, norovirus
- High turbidity during rain events stresses treatment systems
- Most subject to contamination from upstream land use
- Requires most comprehensive treatment train of the three source types
- Most regulatory complexity: riparian or appropriation rights, state permits, instream flow protection

**Minimum treatment train for potable surface water:**
- Sediment settling (24-hour settling tank minimum)
- Multi-stage sediment filtration (50 → 10 → 1 micron)
- Activated carbon (chlorine removal, VOCs)
- Ultrafiltration membrane (virus and bacteria removal)
- UV disinfection (post-membrane)
- Monthly turbidity, coliform, and nitrate testing

**Typical treatment system cost for potable surface water:** $6,000–$18,000 depending on flow rate and source quality

### 10.4 Source Selection Matrix

| Factor | Rainwater | Groundwater | Surface Water |
|--------|-----------|-------------|---------------|
| Initial capital cost | Medium | High | Medium–High |
| Operating cost | Low | Low–Medium | Medium |
| Treatment complexity | Low–Medium | Low–Medium | High |
| Seasonal reliability | Variable | High | Variable |
| Climate vulnerability | Drought: high | Drought: medium | Drought: high |
| Regulatory complexity | Low | Medium | High |
| Water quality consistency | Variable | High | Low |
| Best climate | Humid (>25 in/yr) | Universal | Universal |
| Emergency fallback | Easy (any rain event) | Pump dependent | Gravity dependent |

**Recommended multi-source resilience architecture:**
1. Primary: groundwater well (year-round reliability)
2. Secondary/supplemental: rainwater cistern (bridges power outages, supplements dry-season irrigation)
3. Emergency only: treated surface water (seasonal stream, flood events with full treatment)

A property that can draw from at least two of these three sources, with 30-day storage of each, has dramatically higher water security than any single-source system regardless of how well that single source is sized.

---

## Safety Reference: Critical Water Quality Standards

These EPA Maximum Contaminant Levels (MCLs) govern potable water safety. Any self-produced water used for drinking, cooking, or food preparation should meet these standards. [13][14]

**Primary MCLs (health-based, enforceable):**

| Contaminant | MCL | Health Effect | Primary Source |
|-------------|-----|---------------|----------------|
| E. coli | Zero (any presence) | Gastroenteritis, hemolytic uremic syndrome | Fecal contamination |
| Total coliform | <5% positive samples | Indicator of fecal contamination pathway | Various |
| Nitrate (as NO₃-N) | 10 mg/L | Blue baby syndrome (methemoglobinemia) in infants | Agricultural runoff, septic |
| Arsenic | 0.010 mg/L | Skin damage, circulatory, cancer risk | Geological |
| Lead | 0.015 mg/L (action level) | Neurological damage (especially children) | Pipe corrosion |
| Atrazine | 0.003 mg/L | Reproductive effects | Agricultural herbicide |
| PFOA | 0.000004 mg/L (4 ppt) | Immune, reproductive, cancer (suspected) | Industrial, AFFF foam [14] |
| PFOS | 0.000004 mg/L (4 ppt) | As above | Industrial, AFFF foam [14] |
| Turbidity | <1 NTU (treatment technique) | Indicator of microbial risk | Sediment |
| Radium-226/228 | 5 pCi/L combined | Cancer risk | Geological |

**Secondary MCLs (aesthetic, non-enforceable):**

| Contaminant | SMCL | Effect |
|-------------|------|--------|
| Iron | 0.3 mg/L | Metallic taste, staining |
| Manganese | 0.05 mg/L | Black staining, bitter taste |
| pH | 6.5–8.5 | Corrosion (low pH), scaling (high pH) |
| Hardness | 120–180 mg/L (unofficial guidance) | Scaling, soap interference |
| Sulfate | 250 mg/L | Laxative effect at high levels |
| TDS | 500 mg/L | Mineral taste |

---

## Sources

[1] USGS Groundwater Resources Program — Methods for Estimating Ground-Water Recharge in Humid Regions: https://water.usgs.gov/ogw/gwrp/methods/

[2] NOAA National Centers for Environmental Information — U.S. Climate Normals 2020 (1991–2020): https://www.ncei.noaa.gov/products/land-based-station/us-climate-normals

[3] USGS StreamStats — Streamflow Statistics and Watershed Characteristics: https://streamstats.usgs.gov/ss/

[4] NC State Extension Publications — Protecting Water Supply Springs: https://content.ces.ncsu.edu/protecting-water-supply-springs

[5] USGS Documentation of Spreadsheets for the Analysis of Aquifer-Test and Slug-Test Data (OFR 02-197): https://pubs.usgs.gov/of/2002/ofr02197/documentation.pdf

[6] EPA WaterSense — Indoor Water Use in the United States: https://www.epa.gov/watersense/statistics-and-facts

[7] WHO — Household Water Requirements and Per Capita Standards: https://www.who.int/water_sanitation_health/diseases-risks/diseases/diarrhoea/en/

[8] EPA — Treatment Options for Removing PFAS from Drinking Water (April 2024): https://www.epa.gov/system/files/documents/2024-04/pfas-npdwr_fact-sheet_treatment_4.8.24.pdf

[9] Sepratech Corp — Multi-Media Filtration, Microfiltration, and Ultrafiltration Overview: https://www.sepratechcorp.com/multi-media-filtration-microfiltration-and-ultrafiltration/

[10] Frontiers in Water — Potential of Solar Water Disinfection (SODIS) for Pathogen Control During Water Scarcity Crisis (2025): https://www.frontiersin.org/journals/water/articles/10.3389/frwa.2025.1679793/full

[11] Efficient Solar Disinfection (SODIS) Using Polypropylene-Based Transparent Jerrycans — *Journal of Hazardous Materials* (2023): https://www.sciencedirect.com/science/article/pii/S2213343723005262

[12] University of Nebraska Extension — Drinking Water Treatment: Water Softening (Ion Exchange) (G1491): https://extensionpubs.unl.edu/publication/g1491/2014/html/view

[13] EPA — National Primary Drinking Water Regulations: https://www.epa.gov/ground-water-and-drinking-water/national-primary-drinking-water-regulations

[14] EPA — Final PFAS National Primary Drinking Water Regulation (April 2024): https://www.epa.gov/system/files/documents/2024-04/drinking-water-utilities-and-professionals-technical-overview-of-pfas-npdwr.pdf

[15] EPA WaterSense — Point-of-Use Reverse Osmosis Systems: https://www.epa.gov/watersense/point-use-reverse-osmosis-systems

[16] Greywater Treatment Using Lab-Scale Systems Combining Trickling Filters and Constructed Wetlands — *Resources, Conservation and Recycling Advances* (2024): https://www.sciencedirect.com/science/article/pii/S2589014X24001567

[17] EPA — Subsurface Flow Constructed Wetlands for Wastewater Treatment: https://www.epa.gov/sites/default/files/2015-06/documents/wetlands-subsurface_flow.pdf

[18] ACS ES&T Engineering — Nitrogen and Phosphorus Removal in Free Water Surface Constructed Wetlands (2025): https://pubs.acs.org/doi/10.1021/acsestengg.4c00392

[19] Worrell Water Technologies / Engineering For Change — The Living Machine: https://www.engineeringforchange.org/solutions/product/the-living-machine/

[20] NTO Tank — How to Protect a Rainwater Tank from Freezing: https://www.ntotank.com/blog/how-to-protect-a-rainwater-tank-from-freezing

[21] Long-Term Storage of Chilled Water in Cisterns in Hot, Arid Regions — *Energy and Buildings* (1988): https://www.sciencedirect.com/science/article/abs/pii/0360132388900157

[22] Penn State Extension — Rainwater Cisterns: Design, Construction, and Treatment: https://extension.psu.edu/rainwater-cisterns-design-construction-and-treatment

[23] Testing for Water Quality — UGA Cooperative Extension (C858-2): https://fieldreport.caes.uga.edu/publications/C858-2/testing-for-water-quality/

[24] USDA — Frost Depth Maps and Subsurface Infrastructure Protection: https://www.nrcs.usda.gov/wps/portal/nrcs/detail/national/nedc/?cid=stelprdb1044917

[25] Chelsea Green Publishing — Design Swales for Optimum Water Flow: https://www.chelseagreen.com/2019/design-swales-for-optimum-water-flow/

[26] Frontiers in Sustainable Food Systems — Integrated Nutrient and Feeding Optimization Strategies in Aquaponics (2025): https://www.frontiersin.org/journals/sustainable-food-systems/articles/10.3389/fsufs.2025.1681782/full

[27] US DOE Energy Saver — Planning a Microhydropower System: https://www.energy.gov/energysaver/planning-microhydropower-system

[28] Mid-Atlantic Water — Well Pressure Tank Troubleshooting: Waterlogged, Short Cycling & Low Pressure: https://midatlanticwater.net/blogs/faqs/well-pressure-tank-troubleshooting

[29] MDPI Water — Review of Techniques to Reduce and Prevent Carbonate Scale (2021): https://www.mdpi.com/2073-4441/13/17/2365

[30] National Agricultural Law Center — Water Law Overview: https://nationalaglawcenter.org/overview/water-law/

[31] California State Water Resources Control Board — Water Rights FAQs: https://www.waterboards.ca.gov/waterrights/board_info/faqs.html

[32] EPA — Overview of Drinking Water Treatment Technologies: https://www.epa.gov/sdwa/overview-drinking-water-treatment-technologies

[33] EPA — How EPA Regulates Drinking Water Contaminants (SDWA Framework): https://www.epa.gov/sdwa/how-epa-regulates-drinking-water-contaminants

[34] University of Nebraska Extension — Drinking Water Treatment: Reverse Osmosis: https://extensionpubs.unl.edu/publication/g1490/na/html/view

[35] Virginia Tech Well Water Program — Spring Development and Protection: https://www.wellwater.bse.vt.edu/files/WF4%20spring%20devt%20and%20prot.PDF

[36] USGS Pennsylvania Water Science Center — Groundwater Recharge Methods: https://www.usgs.gov/centers/pennsylvania-water-science-center/science/groundwater-recharge-pennsylvania

[37] EPA — Drought Resilience and Water Conservation: https://www.epa.gov/water-research/drought-resilience-and-water-conservation

[38] USGS — Modeling Surface Water and Groundwater Budgets of the US Using MODFLOW-OWHM: https://www.usgs.gov/publications/modeling-surface-water-and-groundwater-budgets-us-using-modflow-owhm

[39] EPA — Secondary Drinking Water Standards: Guidance for Nuisance Chemicals: https://www.epa.gov/sdwa/secondary-drinking-water-standards-guidance-nuisance-chemicals

[40] EPA — Constructed Wetlands Overview: https://www.epa.gov/wetlands/constructed-wetlands

[41] IWA Publishing — Effectiveness of Solar Disinfection for Household Water Treatment (2021): https://iwaponline.com/washdev/article/11/3/374/80556/

[42] Building America Solution Center (PNNL) — Drinking Water Treatment Systems: https://basc.pnnl.gov/resource-guides/drinking-water-treatment-systems

[43] Oklahoma State University Extension — Whose Water Is It Anyway? Comparing US Water Rights Frameworks: https://extension.okstate.edu/fact-sheets/whose-water-is-it-anyway

[44] Oregon Water Resources Department — Water Rights in Oregon (The Aqua Book): https://www.oregon.gov/owrd/WRDPublications1/aquabook.pdf

[45] Crystal Quest — Membrane Technology in Multistage Filter Systems: https://crystalquest.com/blogs/membrane-filtration/multistage-filter-systems

[46] MDPI Water — Constructed Wetlands for Wastewater Treatment (2010): https://www.mdpi.com/2073-4441/2/3/530

[47] EPA — WaterSense RO Systems Mini-Report (November 2024): https://www.epa.gov/system/files/documents/2024-11/ws-products-ro-systems-mini-report.pdf

[48] EPA — Proposed PFOA and PFOS Compliance Extension Rule: https://www.epa.gov/sdwa/proposed-pfoa-and-pfos-compliance-extension-rule

[49] The Ecologist — The Living Machine: An Ecological Approach to Wastewater: https://theecologist.org/2010/jun/08/living-machine-ecological-approach-poo

[50] Frontiers in Water — SODIS Pathogen Control and Climate Scarcity (2025): https://www.frontiersin.org/journals/water/articles/10.3389/frwa.2025.1679793/full

[51] USGS Water Resources Investigations Report 01-4210 — Aquifer Data Analysis and Synthesis: https://pubs.usgs.gov/wri/wri014210/text/06_data.htm

[52] Agriculture Institute — Underground Cisterns: Reducing Evaporation in Water Storage: https://agriculture.institute/water-harvesting-conservation-utilisation/underground-cisterns-reduce-water-evaporation/

---

*Guide version 1.0 — Open-Repo Project — CC-BY-4.0 — Last updated 2026-07-06*
*Wave 3, Domain 5 — Assumes Wave 0 water systems foundation*
*Confidence: 88% — See YAML frontmatter for confidence notes and known limitations*
