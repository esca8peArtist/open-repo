---
title: "Household Water Coordination — 3-Household Scale"
scale: household
region: "Midwest US (Zone 5)"
tracks: "Rural + Suburban"
word_count: ~7400
citation_count: 29
created: 2026-05-17
cross_references:
  - individual/01-water.md
  - household/01-household-coordination-overview.md
  - midwest/calendar.md
  - individual/04-energy.md
  - individual/02-food.md
---

# Household Water Coordination — 3-Household Scale
> **Region**: Midwest US (Zone 5) | **Tracks**: Rural + Suburban
> **Scale**: 3 households, 10–14 people, shared or adjacent parcels
> **Cross-references**: [individual/01-water.md](../individual/01-water.md) · [01-household-coordination-overview.md](01-household-coordination-overview.md) · [midwest/calendar.md](../midwest/calendar.md) · [individual/04-energy.md](../individual/04-energy.md)

---

## The Most Important Finding

The critical insight from 3-household water coordination is not that more storage is better — it is that distributed sources with a managed shared reserve outperform any single large system. Three households, each with an independent primary source (well, roof cistern, or spring), sharing a common overflow tank and governed by a written drought protocol, can sustain water supply through a 90-day drought with no one household in crisis. The same cluster relying on a single shared well fails the first day that well's pump breaks. Design for distributed redundancy first; optimize for cost and labor second.

This document covers coordination design exclusively. It assumes each household in the cluster has already built or is building the individual-scale capabilities described in `individual/01-water.md` — those cover emergency treatment, individual storage, hand pumps, and individual well management. This document picks up where that one ends: at the boundary between one household's system and the next.

---

## Quick Reference Card
*(Print and share with all cluster households)*

**Reference scenario**: 3 households (A, B, C), 12 people, adjacent rural parcels totaling 5 acres, Zone 5 Midwest, well depths 120–180 ft, average annual rainfall 35–40 inches.

### Three-Well Distributed Architecture — Failure Tolerance

| Failure Condition | Households Affected | Response Time | Recovery |
|---|---|---|---|
| One well pump fails | 1 of 3 (33%) | < 2 hours (gravity from shared tank) | 1–7 days (pump repair/replace) |
| Two well pumps fail simultaneously | 2 of 3 (66%) | < 4 hours (shared tank + working well) | 1–14 days |
| All three wells fail | 3 of 3 | 24–48 hours (shared tank storage) | Cistern bridges gap; emergency source activated |
| Primary cistern fails | All (storage loss only) | Immediate (switch to wells) | Days (repair/replace cistern) |
| Shared distribution line breaks | All (distribution only) | Hours (bypass to buckets) | 1–3 days (pipe repair) |

**Key principle**: No single failure should leave any household without water for more than 6 hours. This requires the shared tank to always contain at minimum 72 hours of full-cluster consumption (approximately 400–500 gallons for a 12-person cluster at 3 gallons/person/day).

### Cluster Water Budget — 3 Households, 12 People

| Category | Per Person/Day | 12-Person Cluster/Day | Notes |
|---|---|---|---|
| Drinking + cooking | 1–1.5 gal | 12–18 gal | Non-negotiable minimum |
| Hygiene (sponge bath standard) | 0.5–1 gal | 6–12 gal | Grid-absent standard |
| Sanitation (toilet/outhouse) | 0–1.5 gal | 0–18 gal | Zero if composting toilets in use |
| Garden irrigation (shared) | Varies | 50–200 gal | Drip irrigation; seasonal; see Section 5 |
| Livestock (if present) | — | 5–50 gal | Chickens: 0.5 gal/10 birds; dairy cow: 35 gal |
| **Survival minimum** | **2 gal** | **24 gal/day** | Drinking + cooking + basic hygiene only |
| **Comfortable baseline** | **5 gal** | **60 gal/day** | Full hygiene, light sanitation, no irrigation |
| **Full operations** | **10+ gal** | **120+ gal/day** | Irrigation, livestock, preservation work |

---

## Section 1: Cistern Capacity Planning — 3-Household Scale

### Design Principle: Catch, Store, Bridge

The fundamental logic of shared water infrastructure is three-layer: (1) each household catches from its own roof and manages its own primary source, (2) excess flows into a shared central cistern, and (3) that cistern bridges supply gaps across any single household's production failure. This is different from all households drawing from one shared source — distributed catch with shared reserve is far more resilient.

### Calculating Combined Catchment

At 3-household scale, combined roof area typically runs 3,000–6,000 sq ft. Using the Midwest catchment formula from Texas A&M AgriLife Extension [1]:

```
Gallons = Roof_sq_ft × Rainfall_inches × 0.623 × 0.85 (efficiency factor)
```

**Combined catchment table for the reference scenario** (three 1,500 sq ft effective roof surfaces = 4,500 sq ft combined):

| Month | Central IL avg rainfall | Gallons harvestable (4,500 sq ft) | 12-person demand (60 gal/day) | Net surplus/(deficit) |
|---|---|---|---|---|
| January | 1.5" | 3,578 | 1,860 | +1,718 |
| February | 1.5" | 3,578 | 1,680 | +1,898 |
| March | 2.3" | 5,487 | 1,860 | +3,627 |
| April | 3.2" | 7,634 | 1,800 | +5,834 |
| May | 3.9" | 9,304 | 1,860 | +7,444 |
| June | 3.9" | 9,304 | 1,800 | +7,504 |
| July | 3.7" | 8,828 | 1,860 | +6,968 |
| August | 3.4" | 8,113 | 1,860 | +6,253 |
| September | 2.8" | 6,683 | 1,800 | +4,883 |
| October | 2.9" | 6,921 | 1,860 | +5,061 |
| November | 2.4" | 5,726 | 1,800 | +3,926 |
| December | 1.8" | 4,294 | 1,860 | +2,434 |
| **Annual** | **33.3"** | **79,448** | **21,900** | **+57,548** |

**Key takeaway**: Annual collection is over 3.6x annual demand — but the table assumes all collection goes to use. In practice, the system must be sized to buffer the seasonal imbalance (dry summer + drought risk) and carry from winter through to spring refill.

### Sizing the Shared Cistern

The shared cistern is the buffer between individual household production and full-cluster consumption. For a 3-household reference cluster:

**Minimum shared cistern = 90-day worst-case bridge × full-cluster daily demand**

A Midwest Zone 5 cluster should plan for a drought scenario modeled on the region's 50-year recurrence drought: approximately 45–60 consecutive days without meaningful rain in the July–September window, when ground water is typically lowest [USGS Upper Midwest Water Science Center, 2]. Adding a 25% safety factor as recommended by Penn State Extension [3]:

```
Shared cistern minimum = (60 days × 60 gal/day × 1.25) + individual household reserves
                       = 4,500 gallons (shared cistern) + ~500 gal per household (individual)
                       ≈ 6,000 gallons combined (shared + individual)
```

**Practical implementation options**:

| Configuration | Capacity | Cost estimate | Notes |
|---|---|---|---|
| Single 5,000-gal polyethylene tank | 5,000 gal | $1,800–2,500 | Easiest installation; single point of failure |
| Two 2,500-gal poly tanks (parallel-connected) | 5,000 gal | $2,200–3,200 | Allows isolation if one leaks; recommended |
| Poured concrete in-ground cistern (8×8×12 ft) | ~5,700 gal | $2,000–4,000 materials | Permanent; frost-proof; best Zone 5 option |
| Three 1,500-gal IBC totes (parallel-connected) | 4,500 gal | $800–1,500 used | Fastest, cheapest; not frost-proof above ground |

**Zone 5 frost note**: Any above-ground cistern must be drained or insulated for November–March. An in-ground concrete cistern buried below the 42–48 inch frost line [4] stays above freezing without insulation and allows year-round access. This is the recommended configuration for the Midwest reference scenario.

### Multi-Unit Collection Optimization

When three households feed a shared cistern, the collection plumbing must address:

**First-flush management**: Each roof contributes a first-flush contaminant load from bird droppings, dust, and organic debris. Each household's collection system should have its own first-flush diverter (sized to ~1 gallon per 100 sq ft of roof) before any flow enters the shared cistern. Do not rely on a single shared first-flush at the cistern inlet — the contaminant loads from three rooftops simultaneously overwhelm any single diverter during heavy rain events.

**Inter-tank connection method**: For a three-household shared cistern with individual household reserves, the parallel connection method (bottom-to-bottom pipe) is strongly preferred over series connection. In parallel configuration, all tanks fill and drain simultaneously; a leak in one household's storage tank does not drain the entire cluster's reserve. Texas A&M AgriLife Extension and National Poly Industries both recommend parallel connection with isolation valves at each tank outlet [1, 5]. Minimum pipe diameter: 2-inch PVC for gravity-balanced connections; 3-inch for overflow lines.

**Overflow management**: The shared cistern overflow must be routed to a defined destination — never to an uncontrolled discharge. Options: a swale leading to a garden bed, a French drain leading away from foundations, or a secondary storage tank. The overflow pipe should match the inlet pipe diameter and should include a mesh screen at the terminus to prevent insect intrusion.

**Example 3-household collection schematic**:
```
Household A roof (1,500 sq ft)       Household B roof       Household C roof
     ↓ first-flush diverter                ↓                      ↓
   HH-A individual tank (500 gal)    HH-B individual tank   HH-C individual tank
     ↓ overflow                          ↓ overflow              ↓ overflow
     ├──────────────────────────────────┼───────────────────────┤
                                        ↓
                         Shared cistern (5,000 gal, in-ground)
                                        ↓ overflow
                              Swale → orchard/garden
```

---

## Section 2: Greywater Systems — 3-Household Coordination

### What Greywater Coordination Adds at This Scale

At individual scale, greywater is a minor offset — reducing consumption by 20–30% through landscape reuse. At 3-household scale, coordinated greywater systems eliminate the largest single waste stream (shower and laundry water) from the load on the cistern, freeing stored capacity for critical uses during dry periods. A well-designed cluster greywater system can offset 40–60% of summer irrigation demand from the main water supply.

Greywater is water from showers, bathroom sinks, and laundry machines. It does not include toilet waste (blackwater), kitchen sink waste (too high in food particles and grease), or dishwasher discharge. Greywater must never be stored — it must be dispersed to the landscape within 24 hours or pathogens multiply to dangerous levels. [SF Public Utilities Commission Graywater Design Manual, 6]

### System Tiers for 3-Household Clusters

**Tier 1 — Laundry-to-Landscape (L2L), per household**

The simplest and most cost-effective greywater intervention. Each household diverts its laundry machine drain directly to a mulch basin or series of mulch basins on the landscape. Total cost: $100–250/household in materials. No permits required in most Midwest states for single-family residence laundry diversion under 250 gpd.

Design requirements from California experience (most directly applicable):
- Minimum 2" mulch depth over any irrigation point
- No sprinkler or surface ponding of greywater
- No irrigation of root crops that contact soil
- 100 ft setback from any creek or wetland [6]
- Must include a 3-way valve to divert back to sewer during winter/wet season

**Tier 2 — Branched-drain shower greywater, per household**

Shower drain connected to a branched 1½" ABS or PVC pipe network that distributes greywater through gravity to 3–6 mulch basins under fruit trees or shrubs. Requires 2% minimum slope from shower to each basin. Cost: $200–400/household. Works well in Zone 5 from May through October; must divert to sewer November–April when ground is frozen.

Biological treatment in mulch basins: The mulch basin functions as a passive constructed wetland. Woodchips provide high surface area for aerobic bacteria; earthworms and soil organisms degrade BOD by 84–92% and reduce pathogens to safe levels before greywater reaches the root zone. [7] Banana trees, willows, and cattails (Typha spp.) are particularly effective in greywater mulch basins and can be clustered to form a "banana circle" structure used in permaculture design.

**Tier 3 — Shared constructed wetland (cluster-scale)**

If the three households share physical space (adjacent gardens, shared orchard), a single cluster-scale subsurface-flow constructed wetland can treat combined household greywater — approximately 150–300 gallons/day for a 12-person cluster. This is a more complex installation requiring a settling tank, gravel bed, wetland plants (Juncus, Typha, Scirpus), and a distribution manifold. This meets NSF/ANSI 350 performance standards when properly designed and maintained [8], treating to BOD < 10 mg/L and meeting EPA water reuse standards. Build cost: $1,500–3,500 shared across households.

Constructed wetland sizing rule of thumb for greywater: 5–10 sq ft of wetland surface per 10 gallons treated per day. [9] For 200 gal/day: 100–200 sq ft of wetland surface.

### Emergency Flush Protocol

During a water shortage, greywater systems must shift function. The cluster greywater protocol:

1. **Normal operations**: All shower/laundry greywater routes to landscape basins; zero to sewer
2. **Water restriction Level 1** (shared cistern below 50% capacity): Laundry-only greywater to landscape; showers routed to sewer to conserve soap contamination in dwindling water
3. **Water restriction Level 2** (shared cistern below 25%): All greywater to sewer; all water use restricted to survival minimum (2 gal/person/day); irrigation suspended
4. **Emergency only** (cistern below 72-hour reserve): Greywater system shut down entirely; conserve all infrastructure for drinking and cooking

A clearly labeled 3-way diverter valve at each household's greywater junction makes this a 10-second operation at each house. Label the valve positions with laminated cards: "Normal / Restriction / Emergency."

---

## Section 3: Storage Redundancy Architecture

### The Four-Layer Model

A resilient 3-household water storage system has four distinct layers, each serving a different function:

**Layer 1 — Individual household reserves** (72-hour minimum per household)
Each household maintains sealed, treated water sufficient for 72 hours of survival minimum (2 gal/person × 72 hours × household occupants). These reserves are physically in the household, not shared infrastructure. In a full-cluster emergency, these reserves ensure no individual household faces immediate crisis while the shared system is restored. Target: 60–90 gallons per household for an average household of 4. Source: 7-gallon Aquatainers, 55-gallon drums, or WaterBOB.

**Layer 2 — Individual primary source** (ongoing production)
Each household's well, spring, or roof cistern provides ongoing daily production. The goal is that no two households share the same primary source — a failure in one does not reduce the others. In the reference scenario, Household A has a 150 ft drilled well, Household B has a 180 ft drilled well, and Household C has a 120 ft well + 2,000-gallon individual roof cistern.

**Layer 3 — Shared central cistern** (90-day bridge)
The 5,000-gallon shared cistern described in Section 1. Filled passively by overflow from each household's collection system. Managed by a designated water steward (see Section 4 governance). Maintained at a minimum of 25% capacity (1,250 gallons) at all times.

**Layer 4 — Emergency backup sources**
A documented list of secondary sources accessible to the cluster within 2 hours:
- Nearest hand-pumpable shallow well (specify: whose property, what depth, what yield)
- Nearest surface water (creek, pond) with treatment protocol (see individual/01-water.md)
- Municipal fill station if within 30-minute drive (identify two; hours and cost)
- Neighbor with different water infrastructure outside the cluster

### Shallow Well as Backup Source

A hand-dug or driven-point shallow well (20–30 ft depth) to a seasonal perched aquifer serves well as a summer backup if the primary deep wells fail simultaneously. The shallow well is not used routinely — which keeps it as a true emergency reserve and reduces the risk of contamination from overuse. Keep a hand pump permanently installed. The Well Owner's Guide (WellOwner.org, EPA-funded) [10] provides inspection and maintenance schedules applicable to shallow backup wells.

**Midwest shallow well caution**: Shallow aquifers (< 50 ft) in the Zone 5 agricultural Midwest carry elevated nitrate risk during spring thaw (April–May) when surface runoff charges the shallow groundwater directly. A 2021 study in the PMC found nitrate detection probabilities significantly higher in shallow wells in Wisconsin's fractured dolomite aquifer during spring recharge periods [11]. Do not use a shallow backup well for drinking water without nitrate testing during March–May. Use it for irrigation and sanitation during those months; use deep well or stored reserve for drinking.

### Spring Box Protection

If any parcel in the cluster has a natural spring, this is the most valuable individual water asset the cluster has — springs require no energy to produce and are typically connected to a deeper, more stable aquifer than shallow wells. Protect it:

- **Spring box construction**: Concrete box over the spring emergence point; 6" overflow pipe set 2" below the top of the spring box to prevent artesian overpressure from blowing out seals; screened vent to prevent insects; access hatch with lock
- **Spring capture line**: 1¼" or 2" polyethylene pipe gravity-fed from spring box to storage tank; minimum 2% grade; bury below frost line (42–48" in Zone 5)
- **Protection perimeter**: No septic or animal pasture within 100 ft of spring emergence; no surface water allowed to flow into spring box (divert with grade)
- **Winter management**: Spring boxes do not freeze if flow is constant; if flow drops in winter, insulate the box with 6–8" of straw bales covered with a tarp; never let standing water develop inside the box

---

## Section 4: Testing, Quality Assurance, and Documentation

### Why Testing Is a Shared Governance Function

Individual households test their own wells once a year and typically don't discuss the results. At cluster scale, one household's compromised well can indicate a cluster-wide contamination risk — especially when the shared cistern mixes water from multiple sources. Coordinated testing, shared documentation, and a clear protocol for contamination findings make the cluster genuinely safer than isolated individual testing.

### What to Test, When, and How

**Minimum annual test panel** (each household's primary source, every April):

| Parameter | Why April | Method | Threshold | Cost |
|---|---|---|---|---|
| Total coliform + E. coli | Spring thaw = peak surface water intrusion risk [11, 12] | Lab mail-in (most accurate) or DIY presence/absence kit | Zero E. coli; < 1 cfu/100mL coliform | $25–40 lab; $10–15 DIY |
| Nitrates | Spring runoff charges shallow aquifers; corn belt background load | Lab mail-in preferred | < 10 mg/L (EPA MCL) | $20–30 |
| pH | Affects plumbing corrosion; taste | pH strips or digital meter | 6.5–8.5 | $5–10 |
| Turbidity (visual or measured) | Cloudy water indicates sediment intrusion; signals filter need | Comparison to clear water standard; commercial NTU tube or transparency tube | < 1 NTU (drinking); < 5 NTU (max) [13] | $0 visual; $30–80 instrument |

**Additional tests for the shared cistern** (every 6 months — October and April):

| Parameter | Notes |
|---|---|
| Coliform + E. coli | Shared cistern can accumulate contamination from multiple inputs |
| Sediment inspection | Open access hatch; check for biofilm, algae, sediment accumulation |
| Cover/seal inspection | Mosquito screen intact; vents screened; hatch sealed against insects |
| Chlorine residual | If cistern was recently treated; use pool test strips |

**DIY kit accuracy context**: DIY coliform kits provide a presence/absence result at a sensitivity of ~1 colony per mL. They are adequate for routine monitoring and can detect gross contamination. However, per Clean Water Store and Tap Score analysis, DIY kits cannot quantify the level of contamination and cannot identify specific strains [14, 15]. Lab confirmation is required for any positive result, and the cluster protocol should specify: any positive DIY result triggers a lab confirmation test before that household's water is used or mixed into shared storage.

### Turbidity Assessment — Practical Methods

Turbidity above 1 NTU in drinking water warrants filtration before consumption; above 5 NTU requires investigation of the source [13]. Two methods accessible to rural clusters:

**Visual method (zero cost)**: Fill a clear glass; hold it against a white background in bright light. Drinking-quality water is visibly clear. Slight cloudiness suggests 5–10 NTU. Noticeably cloudy water (you cannot see through 1 inch of depth) is above 10 NTU and should not be consumed without filtration and disinfection.

**Transparency tube ($10–20 DIY)**: A 45 cm clear tube with a Secchi disk pattern at the bottom. Fill from the top; read the water level at which the disk pattern becomes invisible. Compare to NTU conversion chart. Water Rangers (a Canadian citizen-science organization) publishes the conversion guide free online [16].

### Seasonal Contamination Patterns — Zone 5 Midwest

The cluster's testing schedule should be calibrated to known regional contamination risk windows:

**Spring thaw (March–May)**: Highest risk. Snowmelt + spring rain saturates the soil profile and carries surface contaminants (animal waste, nitrate from ag fields, road salt, septic overflow) into the shallow aquifer within days. A ScienceDirect study on groundwater-surface water exchange in freeze-thaw watersheds confirmed that nitrate concentrations spike with spring groundwater recharge [12]. Test wells in April before drawing down the cistern for summer irrigation.

**Tornado/severe storm season (May–July)**: Floodwaters carry sewage, agricultural chemicals, and debris. Any well or cistern exposed to surface flooding during a tornado or major storm must be tested before use; in the interim, use only sealed pre-storm reserves or treat with 50 ppm chlorine shock (1/3 cup 8.25% bleach per 100 gallons) and allow 24 hours contact time before use.

**Late summer drought (August–September)**: Well yields can drop; Midwest aquifer depths can fall 5–15 ft during extended droughts. Lower water tables concentrate existing contamination (nitrates, minerals) in a smaller water volume. If pH or hardness changes suddenly, test for nitrates.

**Fall recharge (October–November)**: Second recharge event; lower contamination risk than spring (crop applications mostly complete) but sediment can be high after harvest-season soil disturbance.

### Documentation for Shared Decision-Making

Each cluster should maintain a shared water log — a simple 3-ring binder or shared document accessible to all households. Minimum contents:

1. **Water test results**: Date, source (which well or cistern), parameters tested, results, lab name and reference number. Keep minimum 5 years of records.
2. **Maintenance log**: Dates of filter cleaning, cistern inspection, pump maintenance, pipe repair. Who did the work, what was found, what was replaced.
3. **Consumption tracking**: Weekly shared cistern level readings (a simple stick gauge or float indicator); marked against rainfall and usage events. Establishes the data needed to invoke drought protocols early.
4. **Incident log**: Any contamination event, pump failure, treatment action, or quality concern, with response taken.
5. **Emergency contacts**: Well driller (with after-hours number), pump supplier, county health department (for lab referrals), nearest municipal water fill station address and hours.

---

## Section 5: Governance — Shared Responsibility and Drought Protocols

### The Water Steward Role

A 3-household cluster should designate one person — rotating annually or until the individual wants to step down — as the cluster's water steward. This role is not about exclusive control; it is about continuity of institutional knowledge. The water steward:

- Schedules and organizes all cluster-wide testing (but any household member can conduct the test)
- Maintains the shared water log
- Calls the cluster's quarterly water check meeting (15–20 minutes; can be combined with other coordination)
- Reads the shared cistern level weekly and records it
- Activates the drought protocol when the shared cistern drops below 50%

The Water Systems Council's Shared Well Agreement template [17] and the USDA Rural Development model agreement [18] both provide foundational language for codifying the water steward role in a written agreement.

### Maintenance Responsibility Assignment

| Infrastructure | Responsible Party | Frequency | Notes |
|---|---|---|---|
| Individual household well | That household | Annual pump inspection; as-needed repair | Each household bears own well costs |
| Individual first-flush diverters | That household | Clean after every major rain (> 1 inch); inspect monthly | Neglect = contaminated cistern |
| Individual household storage | That household | Inspect for leaks, clean annually | |
| Shared cistern | Rotating quarterly (all 3 households take a turn) | Inspect cover and screen monthly; clean interior annually | |
| Shared distribution lines | All households together | Visual inspection after freeze-thaw; test flow seasonally | Repair costs split equally |
| Greywater mulch basins | Each household manages own | Replenish mulch annually; add woodchips after each frost season | |
| Shared constructed wetland (if present) | Designated to one household; others rotate backup | Monthly plant health check; semi-annual gravel flush | |

**Inspection schedule quick reference**:

| Month | Task |
|---|---|
| March | Inspect all pipes for frost heave damage; prepare cistern for spring refill season |
| April | Test all primary sources (coliform + nitrates); inspect cistern interior; log results |
| May | Begin greywater landscape diversion (end of freeze season); check first-flush diverters |
| June | Cistern level check; confirm overflow route is clear of plant growth |
| August | Cistern level check; check drought protocol trigger levels |
| October | Test shared cistern; winterize greywater systems (divert back to sewer); inspect spring box insulation |
| November | Drain above-ground distribution lines before first hard freeze; check buried line depths |
| December | Review annual water log; update emergency contacts; plan next year's maintenance budget |

### Drought Protocol — Whose Tank Gets Priority

The most contentious scenario in cluster water governance is a prolonged drought when the shared cistern is declining and every household needs more water than the system is producing. Without a pre-written protocol, this becomes a conflict about fairness under pressure. With one, it is a mechanical decision.

**The cluster's drought protocol has four stages, triggered by shared cistern level readings**:

**Stage 0 — Normal operations** (cistern > 50% full, roughly > 2,500 gallons)
All households draw freely from their own wells. Shared cistern fills passively from overflow. Greywater goes to landscape. Irrigation running on household schedule.

**Stage 1 — Conservation watch** (cistern 25–50%, roughly 1,250–2,500 gallons)
Water steward convenes a brief meeting within 24 hours. Households voluntarily reduce irrigation by 50%. Greywater systems confirmed operational (every gallon reused is a gallon saved from cistern). No new shared cistern drawdowns for non-essential uses (vehicle washing, equipment rinse).

**Stage 2 — Mandatory conservation** (cistern 10–25%, roughly 500–1,250 gallons)
Irrigation suspended for all households. Greywater goes only to highest-priority trees/perennials. Shared cistern reserved for human consumption and cooking only. Each household draws from its own well first; any household whose well fails draws from shared cistern with a daily allocation (suggestion: 15 gallons/person/day from shared cistern = 180 gallons/day for a 12-person cluster).

**Stage 3 — Emergency** (cistern < 10%, roughly < 500 gallons)
All irrigation suspended. Livestock water reduced to survival minimum. All greywater to sewer. Shared cistern allocated as emergency drinking reserve only. Cluster activates Layer 4 backup sources (emergency shallow well, municipal haul). If multi-week drought continues, the cluster begins water haul from municipal station. Cost shared equally by all households.

**Why this protocol works**: It is written before any crisis, agreed to by all households, and based on an objective measurable threshold (cistern gauge reading). No household can claim unfair treatment because the protocol treats all households symmetrically. The critical authority question — "whose tank gets priority" — is answered in Stage 3: the shared cistern belongs to no single household and is reserved for basic human consumption, distributed equally per person regardless of which household's well is working.

### Conflict Resolution

Even with written protocols, conflicts over water use arise. The cluster water governance agreement should specify a three-step process:

1. **Direct conversation**: The water steward convenes a conversation between affected parties within 24 hours of a dispute. Most conflicts at Stage 0–1 are resolved here — they are usually about perception and communication, not actual water scarcity.
2. **Cluster meeting with recorded decision**: All households meet; issue is described; each household states their need; a solution is proposed. The water log records the decision.
3. **Deferred to Stage 3 emergency protocol**: If no resolution is reached, Stage 3 allocation rules take precedence. This is the default and eliminates the need for consensus under stress.

---

## Section 6: Integration with Energy, Food, and Individual Scale

### Integration with Energy (individual/04-energy.md)

Pumping is the largest energy load in any water system. For a 3-household cluster, coordinating pump schedules and power sources prevents energy-water conflicts:

**Solar-direct pumping**: A submersible pump wired to a dedicated solar array (300–400W typical for a 200 ft well) draws only during sunlight. Size the solar array to pump the day's water need in 5–6 peak sun hours. AltE Store's pump sizing method [19] gives the formula: `Panel watts = (Daily demand in gallons ÷ Peak sun hours ÷ GPM) × Pump wattage ÷ 0.85`. For 120 gallons/day from a 200 ft well at 2 GPM with a 500W pump: approximately 400W of panel.

**Pump scheduling coordination**: If Households A and B share a distribution line from the shared cistern, both should not run their booster pumps simultaneously — simultaneous draws cause pressure drops and can starve one line. Designate morning (6–10 AM) and evening (4–8 PM) fill windows per household and stagger by 30-minute offsets.

**Generator backup**: The cluster generator (see household/01-coordination-overview.md) must be rated to start the largest well pump in the cluster. Well pumps have a high startup surge current (2–3× running current). A 240V submersible at 1 HP requires ~2,000W running; startup surge can hit 5,000W. Ensure the shared generator is rated at minimum 5,500W before assuming it can cover pump backup. [20]

**Gravity distribution eliminates pump dependency**: Where terrain allows, a shared cistern placed 25+ ft above the household distribution points provides 10+ PSI of pressure without any pump. Twenty-five feet of head × 0.433 PSI/ft = 10.8 PSI — below municipal standard (40–80 PSI) but adequate for gravity-fed drip irrigation, livestock waterers, and sink faucets. [21] Investing in terrain-appropriate cistern siting during design eliminates the energy-water dependency entirely for most uses.

### Integration with Food (individual/02-food.md)

Irrigation scheduling is a coordination point that directly affects cistern drawdown rates. Three households with independent gardens irrigating simultaneously during July drought conditions can draw 300–500 gallons/day — the single fastest way to empty a shared cistern.

**Shared irrigation schedule principles**:
- One household irrigates per day in rotation during Stage 1 and Stage 2 drought protocols (a household that irrigated yesterday waits while the next household irrigates today)
- Drip irrigation required for all cluster garden beds during any active drought protocol; overhead sprinklers suspended
- Mulching (3–4 inch depth of straw or wood chips) is a cluster-level requirement for any bed using shared water, as mulch reduces irrigation demand by 30–50%
- Rainwater catchment from greenhouse roofs (if present) is priority-diverted to garden storage before entering the shared cistern — it is warm, low-nitrate, and ideal for direct irrigation

**Food preservation water**: August–October canning and fermentation season significantly increases household water demand. Alert the water steward before any major food preservation push (> 50 gallons anticipated). This allows the steward to confirm cistern level and adjust Stage protocols if needed.

### Integration with Individual Scale (individual/01-water.md)

This document assumes each cluster household has:
- A minimum 72-hour individual emergency reserve (sealed, treated water)
- A hand pump on their primary well if it is electrically pumped
- An individual first-flush diverter and basic rain collection system
- The ability to treat uncertain water using the three-step method (filter → disinfect → store)

These are prerequisites, not nice-to-haves. A cluster member without individual-scale water capability is a liability during Layer 4 emergency activation — they will draw on cluster reserves immediately rather than bridging with their own supplies.

The single most important individual-scale dependency for cluster function is the hand pump. If every household has a hand pump on their well, the cluster can never be entirely without water production even during a complete power failure. Without hand pumps, all three households may be dependent on the shared cistern simultaneously during any grid-down scenario — a dangerous concentration of dependency.

---

## Section 7: Implementation — 3-Household Build Timeline

### Phase 1 (Month 1–3): Documentation and Agreement

Before building anything, the cluster should:

1. Draft and sign a shared water agreement based on the Water Systems Council template [17], covering: cistern ownership, maintenance responsibilities, drought protocol triggers, testing schedule and cost sharing, dispute resolution process
2. Produce a shared water log (binder or digital document with offline backup)
3. Conduct a simultaneous baseline water test on all three primary sources (same week, same lab). Compare results. If any source tests positive for coliform or exceeds 10 mg/L nitrate, begin remediation on that source before contributing its water to any shared infrastructure
4. Map all water infrastructure on a single diagram: wells, existing storage, spring locations, garden areas, potential cistern sites

**Cost**: Essentially zero (testing: $75–100 total across three households; agreement: free template)

### Phase 2 (Month 3–6): Individual Household Hardening

Each household, independently, brings its own infrastructure to cluster-ready status:
- Install hand pump if not already present (see individual/01-water.md for pump selection by well depth)
- Install first-flush diverter on all downspouts that will feed the shared cistern
- Install individual household reserve storage (minimum 72 hours at 2 gal/person/day)
- Install 3-way greywater diverter valve at laundry machine (Tier 1 greywater)

**Cost per household**: $400–2,000 depending on existing infrastructure. Hand pump is typically the largest single cost ($800–2,000 installed).

### Phase 3 (Month 6–12): Shared Infrastructure Build

With individual households hardened, build the shared layer:

**Shared cistern installation** (best done April–May or September when ground is workable [midwest/calendar.md]):
- Site selection: Choose the highest point accessible to all three households that is gravity-downhill to garden/distribution areas. Minimum 50 ft from any septic system; 100 ft from any chemical storage
- In-ground concrete option (recommended): Hire a concrete contractor for the excavation and form work, or rent a backhoe and build from 8" CMU blocks on poured footing with poured concrete cap. Total materials ~$1,500–2,500; contractor labor $1,000–2,000 additional
- Connect overflow lines from each household's individual storage to the cistern inlet; parallel-connect any secondary tanks with 2" PVC at the bottom with isolation valves

**Distribution line** (if cluster chooses shared distribution):
- Bury 1¼" or 2" polyethylene water service line below frost line (42–48" minimum in Zone 5) between shared cistern and household tap points
- Install a gate valve and backflow preventer at each household connection
- Run line to garden distribution points with hose bib outlets

**Cost for Phase 3 (3 households sharing)**: $2,500–6,000 depending on cistern type, distance of distribution line, and whether contractor labor is hired. Split three ways: $833–2,000 per household — significantly less than each household building an equivalent individual backup cistern (~$1,000–2,500 each).

### Phase 4 (Year 2+): Greywater and Advanced Integration

After the shared cistern is proven functional through one full seasonal cycle:
- Add Tier 2 shower greywater systems per household ($200–400 each)
- If cluster has shared garden space, evaluate the shared constructed wetland ($1,500–3,500 shared)
- Add solar-direct pump on any well that currently relies on grid power for backup pumping
- Expand shared cistern or add a secondary tank if actual consumption data (from the water log) shows the 5,000-gallon capacity is regularly drawn below 50% during summer

---

## Section 8: International Precedent — What Other Contexts Teach

### Germany — Neighborhood-Scale Rainwater Infrastructure

Germany has over 1.8 million households and businesses using rainwater collection systems, installing at least 60,000 new rainwater tanks annually. The country leads Europe in rainwater harvesting both by practice and policy. [22] The Berlin Berliner Strasse 88 settlement, a late-1980s social housing development in Zehlendorf, demonstrates the cluster model at neighborhood scale: rooftop rainwater is collected into a shared underground cistern, filtered, and pumped to communal green areas, with overflow routed to a public garden. [22] The critical design lesson from German practice is the emphasis on underground cistern placement — the German standard for frost-proof siting (60–80 cm depth minimum) aligns with the Zone 5 requirement (42–48 inch frost line) and demonstrates that this design works in cold-climate contexts at scale.

### Kenya — Smallholder Multi-Plot Rainwater Systems

Kenya's National Water Harvesting and Storage Strategy (2020–2025) [23] emerged from a recognition that smallholder farmers operating at 1–5 acre scale face water insecurity that individual household systems cannot resolve alone. Research on smallholder rainwater harvesting optimization by IWA Publishing [24] found that combining catchment from multiple structures and coordinating storage among 3–5 neighboring plots substantially improved water security metrics compared to single-household systems — the same finding that motivates the 3-household architecture described in this document. Kenyan implementers at Kijabe and similar sites found that the most durable systems (10+ year operation) had three characteristics: community ownership of the shared cistern through a formal written agreement, designated maintenance responsibility (rotating), and a defined system for cost recovery. All three map directly to the governance provisions in Section 5.

### Philippines — Community-Based Water Association Model

The Philippine classification of rural water supply identifies Level I systems (single household source, serving 15–25 households within 250 meters) as the most common small-cluster configuration. [25] Management is assigned to a Barangay Waterworks and Sanitation Association (BWSA) — a community organization elected by users. The BWSA collects water fees, manages maintenance, and appropriates reserve funds. The key transferable lesson for the Midwest reference scenario: even at 3-household scale, a named organizational structure with explicit financial authority (even if it is just a shared maintenance fund held by the water steward) is more durable than informal arrangements. Clusters that establish a simple joint maintenance fund (e.g., $20/household/month) before they have any shared infrastructure have money available to repair it quickly when something breaks, rather than needing to negotiate cost-sharing at the worst possible moment.

### India — Traditional Collective Water Structures

India's traditional water management systems — the Johad of Rajasthan (earthen check dams), the Ahar and Pyne system of Bihar (irrigation ponds linked by earthen channels), and the Zabo of Nagaland (multi-use terrace catchment) [26] — all predate modern engineering but encode the same principle: distributed collection feeding a shared reserve, managed collectively with defined individual rights. The Zabo system is particularly instructive for Zone 5 clusters: it integrates roof catchment, terraced field catchment, and forest area catchment into a single shared cistern, with separate allocations for drinking, livestock, and irrigation — a multi-source, multi-use architecture that parallels the four-layer model described in Section 3.

---

## Primary Sources

| # | Resource | URL | Notes |
|---|---|---|---|
| 1 | Texas A&M AgriLife Extension — Rainwater Harvesting Hub | https://rainwaterharvesting.tamu.edu/connecting-multiple-tanks/ | Best free engineering resource; multi-tank connection methods |
| 2 | USGS Upper Midwest Water Science Center | https://www.usgs.gov/centers/upper-midwest-water-science-center | Groundwater levels, seasonal aquifer patterns, drought tracking |
| 3 | Penn State Extension — Rainwater Cisterns | https://extension.psu.edu/rainwater-cisterns-design-construction-and-treatment | Cistern sizing; recommends 25% safety factor over drought capacity |
| 4 | Heat-Line Freeze Protection — Frost Line Burial Depths | https://heatline.com/how-deep-to-bury-water-pipes-to-prevent-freezing/ | Zone 5 Midwest: 42–48 inch burial minimum for pipes |
| 5 | National Poly Industries — Linking Multiple Water Tanks | https://nationalpolyindustries.com.au/wp-content/uploads/2018/03/how-to-link-multiple-water-tanks-to-increase-rainwater-harvesting-capacity.pdf | Parallel vs. series tank connection; isolation valve requirement |
| 6 | SF Public Utilities Commission — Graywater Design Manual | https://www.sfpuc.gov/sites/default/files/documents/Graywater_Design_Manual.pdf | Laundry-to-landscape and branched drain design requirements |
| 7 | Done Off Grid — Wetland Greywater Biofilters | https://doneoffgrid.com/wetland-greywater-biofilters/ | BOD removal 84–92%; pathogen reduction; mulch basin performance |
| 8 | NSF/ANSI 350 Standard — Water Reuse Treatment Systems | https://www.nsf.org/knowledge-library/nsf-ansi-standard-350-certification-water-reuse-treatment-systems | Certification standard for onsite residential greywater treatment |
| 9 | Appropedia — Subsurface Flow Constructed Wetland for Greywater | https://www.appropedia.org/Subsurface_flow_constructed_wetland_for_greywater | Sizing rules; plant species; gravel media specifications |
| 10 | WellOwner.org — 2021 Well Owner's Guide (EPA-funded) | https://wellowner.org/wp-content/uploads/2021/04/2021-WellOwners-Guide.pdf | Annual inspection checklist; shallow well maintenance |
| 11 | PMC — Sources and Risk Factors for Nitrate/Microbial Contamination, Fractured Dolomite Aquifer, NE Wisconsin | https://pmc.ncbi.nlm.nih.gov/articles/PMC8221036/ | 32–50% of shallow wells exceed coliform/nitrate detection thresholds in fractured geology |
| 12 | ScienceDirect — Groundwater-Surface Water Exchange and Nitrate in Freeze-Thaw Watersheds | https://www.sciencedirect.com/science/article/abs/pii/S0022169425001416 | Nitrate spikes correlate with spring recharge; seasonal well risk confirmed |
| 13 | EPA Drinking Water Standards — Turbidity | https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water | < 1 NTU drinking standard; < 5 NTU maximum; treatment required above threshold |
| 14 | Clean Water Store — DIY Coliform Test Kit Analysis | https://www.cleanwaterstore.com/blog/diy-well-water-test-kits-for-coliform-bacteria/ | DIY kits: presence/absence only; lab confirmation required for any positive result |
| 15 | Tap Score — Coliform and E. coli Water Test | https://mytapscore.com/products/coliform-bacteria-water-test | Mail-in lab standard; quantitative results; recommended for shared-system baseline testing |
| 16 | Water Rangers — Turbidity NTU Testing | https://waterrangers.com/testkits/tests/turbidity-ntu/ | Transparency tube method; NTU conversion guide; free resource |
| 17 | Water Systems Council — Shared Well Agreement Template | https://www.watersystemscouncil.org/download/wellcare_information_sheets/other_information_sheets/Shared_Well_Agreement.pdf | HUD/USDA-based template; adapt with attorney; covers maintenance, cost allocation, dispute process |
| 18 | USDA Rural Development — Shared Water Resources | https://www.rd.usda.gov/programs-services/water-environmental-programs | Rural water technical assistance; community water planning resources |
| 19 | AltE Store — Solar Water Pumping System Sizing | https://www.altestore.com/blogs/articles/solar-water-pumping-part-2-how-to-size-a-system | Pump sizing formula; daily demand, peak sun hours, GPM calculation |
| 20 | Off Grid Collective — Off-Grid Water Pumping Design | https://offgridcollective.co/us/guides/water-systems/off-grid-water-pumping/ | Submersible pump startup surge; generator sizing for well pump backup |
| 21 | RPS Solar Pumps — Solar Transfer Pump from Cistern or Shallow Well | https://www.rpssolarpumps.com/solar-pump-diagrams/solar-transfer-pump-from-spring-box-pond-cistern-or-shallow-well/ | Gravity distribution pressure calculation; 25 ft head = 10.8 PSI |
| 22 | Rain Harvesting — Why Germany Leads in Rainwater Harvesting | https://rainharvesting.com.au/us/blog/germany-rainwater-harvesting-leader-policies-incentives/ | 1.8 million systems; 60,000 tanks/year; Berliner Strasse 88 neighborhood example |
| 23 | Kenya National Water Harvesting and Storage Strategy 2020–2025 | https://faolex.fao.org/docs/pdf/ken214247.pdf | National smallholder water security policy; community ownership model |
| 24 | IWA Publishing — Optimization of Rainwater Harvesting System Design for Smallholder Irrigation Farmers in Kenya | https://iwaponline.com/aqua/article/70/4/483/81472/Optimization-of-rainwater-harvesting-system-design | Multi-plot shared systems outperform single-household; durability factors |
| 25 | Philippine Rural Water Supply Design Manual (World Bank/PPIAF) | https://www.ppiaf.org/documents/1338 | Level I–III classification; BWSA community management model |
| 26 | ClearIAS — Rainwater Harvesting Traditional Systems India | https://www.clearias.com/rainwater-harvesting/ | Johad, Ahar, Zabo systems; multi-source shared cistern principles |
| 27 | Minnesota Stormwater Manual — Rainwater Harvest Design Criteria | https://stormwater.pca.state.mn.us/index.php/Design_criteria_for_stormwater_and_rainwater_harvest_and_use/reuse | Zone 5 northern Midwest design criteria; shared cistern performance standards |
| 28 | Greywater Action — Woodchip Biofilter for Greywater | https://greywateraction.org/woodchip-biofilter-for-kitchen-sink-wetlands/ | DIY mulch basin construction; woodchip depth; maintenance |
| 29 | Coerco — Two Ways to Link Multiple Water Tanks | https://www.coerco.com.au/technical-information/two-ways-to-link-multiple-water-tanks-to-maximise-rainwater-harvesting-potential | Parallel vs. series multi-tank connection; detailed pipe sizing guidance |

---

## Cross-References

- **Individual water systems**: [individual/01-water.md](../individual/01-water.md) — individual emergency stores, hand pump selection, well drilling, individual rainwater collection, treatment protocols
- **Energy**: [individual/04-energy.md](../individual/04-energy.md) — solar pump sizing, generator backup, battery storage for pump loads
- **Food coordination**: [individual/02-food.md](../individual/02-food.md) — irrigation scheduling, food preservation water demand
- **Seasonal calendar**: [midwest/calendar.md](../midwest/calendar.md) — monthly task integration, spring thaw timing, freeze dates for pipe management
- **Cluster governance overview**: [household/01-household-coordination-overview.md](01-household-coordination-overview.md) — MOU templates, domain-specialist authority model, cluster failure scenarios
- **Community scale**: `community/01-water.md` (forthcoming) — scaling beyond 5 households to shared well infrastructure with formal utility management
