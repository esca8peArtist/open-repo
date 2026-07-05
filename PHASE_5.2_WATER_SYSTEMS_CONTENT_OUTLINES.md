---
title: "Phase 5.2 Water Systems Content Outlines"
project: open-repo
phase: "5.2 Wave 0"
document_type: content-structure
status: production-ready
date: 2026-07-04
word_count: ~4200
confidence: 91%
---

# Phase 5.2 Water Systems Content Outlines

**Purpose**: 10–15 section outline for each of the four Water Systems domains, with 1–2 sentence descriptions per section. These outlines define the complete chapter structure that contributors will follow and maintainers will use for content curation.

---

## Domain 1: Water Assessment & Testing

### Section 1: Why Water Testing Matters—Problem Statement & Context
Introduction explaining why knowing water quality is critical in resource-constrained contexts. Covers disease transmission vectors (bacteria, parasites, viruses), chemical contamination risks, and the cost/time tradeoff of testing methods. Establishes value prop: rapid field assessment prevents illness and guides treatment decisions without lab access.

### Section 2: Understanding Water Hazards—Biological, Chemical & Physical
Explains three contamination categories: pathogens (bacteria, viruses, protozoa, helminths), chemicals (residual chlorine, pesticides, heavy metals, industrial pollutants), and physical parameters (turbidity, color, odor, temperature). Describes which organisms cause which illnesses, when chemical contamination is likely (industrial vs. rural contexts), and what each physical parameter suggests about water safety.

### Section 3: Visual Assessment—What You Can See, Smell & Taste (Safely)
Practical field observation procedures: checking color (clear vs. brown/yellow/red—what each suggests), turbidity (using white paper behind clear container, Secchi disk method), odor (safe sniffing technique, interpreting smells), and basic taste (safe sampling for salt content only, not safety assessment). Explains what observations suggest and what they don't tell you about pathogens.

### Section 4: Rapid Test Kits—Selection, Use & Interpretation
Overview of commercially available field test kits for bacteria (coliform presence, E. coli), parasites (turbidity proxies), chemical parameters (pH, hardness, chlorine residual, nitrates). For each test type: brand examples (Aquachek, 3M Clean-Trace, etc.), cost, required equipment, time to result, accuracy limitations, and how to interpret results. Explains false negatives (test says safe but contamination present) and false positives (test says unsafe but water is actually clean).

### Section 5: DIY Testing Methods—Low-Cost Procedures Without Commercial Kits
Procedures requiring only local materials: boiling & observation test for coliform presence (time-based culture observation), clarity testing with Secchi disk (homemade using rope and white plate), pH testing using natural indicators (red cabbage juice, beet juice), salinity testing by taste and specific gravity (using salt water reference). Establishes confidence limits ("this tells you if water is obviously contaminated, not whether it's truly safe").

### Section 6: Testing for Specific Contamination—Decision Trees by Water Source
Context-specific testing protocols: well water (test for coliform, nitrates, hardness), surface water (test for turbidity, coliform, parasites), rainwater (test for contamination from roof/gutters, not natural contamination), treated municipal water in crisis (test for residual chlorine, coliform failure). For each source type: most likely contaminants, most cost-effective test sequence, what results mean for treatment decisions.

### Section 7: Interpreting Results—Safe, Uncertain & Unsafe Classifications
Framework for converting test results to treatment decisions: what result means "safe to drink as-is," what means "needs treatment," what means "unsuitable (requires source finding or professional help)." Includes WHO drinking water quality thresholds and field-pragmatic decision rules (e.g., "if coliform present, treat by boiling or chemical; if turbidity >5 NTU, filtration first then boiling").

### Section 8: Documentation & Data Sharing—Recording Test Results
Procedure for documenting test results (what to record: date, time, source, test method, result, tester name, conditions). Explains how to structure data for Kiwix integration and external sharing (CSV format, JSON-LD metadata). Covers when and how to report results to health authorities or water system operators.

### Section 9: Quality Assurance & Avoiding Testing Errors
Common mistakes in field testing (contaminating the sample, using expired reagents, misreading color charts, testing in wrong order). Procedures for validating test kit accuracy (positive/negative controls, shelf-life tracking) and for repeat-testing if results seem wrong. Includes troubleshooting: "Test says unsafe but water looks clear—what now?"

### Section 10: Testing Frequency & Monitoring Plans
Guidance on testing frequency for different water sources and uses: emergency (daily until source is safe), household well (quarterly routine, monthly if children/elderly), surface water systems (weekly or after heavy rain), treated public water (respond to alerts). Procedure for setting up a simple monitoring log and recognizing when contamination risk has changed (seasonal patterns, upstream events).

### Section 11: Advanced Testing—Microbiology Without a Lab
Introduction to flow cytometry concepts, heterotrophic plate counts (simplified), and turbidity as a proxy for particulate contamination. Explains when these more complex assessments are worth the cost and how to request them from regional labs. Not a DIY procedure section, but resource-connection section.

### Section 12: Case Study: Testing Protocol for Emergency Water Supply
Worked example: after flooding, water from three sources (well, cistern, stream). Step-by-step testing sequence, interpretation of results, treatment decisions, documentation, and communication to community. Shows how assessment informs treatment choices.

### Section 13: Equipment Checklist & Supply Sources
Complete checklist of testing equipment (minimum: visual assessment kit; basic: commercial tests; comprehensive: multiple test types). For each item: purpose, cost, local sourcing options (where kits are available without internet ordering), shelf life, training required. Includes DIY material alternatives.

### Section 14: Resources for Further Learning
Curated list of authoritative sources: WHO drinking water quality standards, CDC water testing guidance, academic papers on field testing accuracy, links to kit vendors, and contact info for regional water authorities. Includes offline resource pointers (iNaturalist for biomonitoring, citizen science networks).

### Section 15: Next Steps—From Testing to Treatment Decisions
Bridge section linking assessment to treatment domain: "Your test shows E. coli—now what? See Domain 3 (Water Treatment & Purification)." Establishes pathway from assessment to action.

---

## Domain 2: Rainwater Harvesting & Storage

### Section 1: Is Rainwater Harvesting Right for Your Site?—Decision Framework
Worksheet-style section helping readers evaluate feasibility: climate (annual rainfall, rainfall patterns), site (catchment area available, roof type, soil type), water needs (household consumption, garden irrigation, livestock), and local regulations. Includes maps/data for US regions and international contexts. Explains when rainwater harvesting is viable (wet climates, large catchment, low demand), marginal (seasonal rainfall, moderate demand), or impractical (dry climates, large demand relative to catchment).

### Section 2: Understanding Your Water Balance—Rainfall, Demand & Tank Sizing
Explains the core calculation: rainfall × catchment area = annual water volume available. Contrasts with household/irrigation demand to determine tank size. Covers rainfall variability (dry months, wet months) and surplus/deficit analysis. Includes simplified worksheets for calculating tank volume without advanced modeling, plus pointers to free online calculators (IRRI, Rainwater Harvesting Supplies calculators).

### Section 3: Catchment Selection—Roofs, Ground, and Material Considerations
Evaluation of different collection surfaces: pitched metal roofs (best), asphalt shingle roofs (acceptable, some debris), clay tile (debris, potential contamination), ground catchment (high debris, poor water quality). For each type: first-flush volume needed (how much water to discard before storage), treatment requirements, maintenance load. Includes materials comparison (metal vs. plastic gutters, downspout types) with cost/longevity tradeoffs.

### Section 4: Rainwater Storage Design—Tank Types, Materials & Sizing
Overview of storage options: above-ground tanks (plastic, metal, concrete; cost, durability, space), underground cisterns (buried plastic/concrete; cost, digging required), and combined systems. For each type: volume range (100–10,000+ gallons), cost estimates, installation difficulty, longevity, maintenance access, and freeze/heat considerations by climate. Includes DIY concrete tank and IBC tote conversion procedures.

### Section 5: First-Flush Diverter Design & Construction
Procedure for building or selecting first-flush diverters (device that discards first rainfall, which contains roof debris and contamination). Explains sizing: typical rule is 10 gallons per 1,000 sq ft of catchment. Includes designs for gravity-fed systems (simple float-ball design) and manual flush-valve systems. Explains what "first-flush" achieves (turbidity reduction, heavy contamination removal) and limitations (doesn't remove all pathogens).

### Section 6: Filtration Strategies—Sediment, Mesh & Multi-Stage Systems
Design options for filtering collected water before tank storage: mesh screen (100–200 micron, removes coarse debris), sand filter (improves clarity, removes some particles), settling tank (allows sediment to drop before transfer to main tank). Explains when each is needed: minimal filtration for non-potable (landscape, livestock) vs. more thorough for potable water. Includes DIY sand filter construction procedure.

### Section 7: Water Quality Maintenance—Algae, Bacteria & Long-Term Storage
Procedures for keeping stored rainwater safe: covering tanks to exclude light (prevents algae growth), maintaining water level (minimizes air space), periodic cleaning (emptying tanks annually to remove sediment), and monitoring for odor/taste changes. Covers when chlorination is needed (for potable use) vs. when settling and filtration suffice (non-potable). Includes troubleshooting: green water (algae), brown water (sediment/tannins), rotten smell (anaerobic bacteria).

### Section 8: Potable vs. Non-Potable Use—Safety & Treatment Pathways
Clear framework: rainwater for landscape/toilet flushing/car washing requires minimal treatment (filtration only); rainwater for drinking requires either boiling, chemical treatment, or professional testing. Explains limitations of rainwater quality (atmospheric dust, roof debris, bird feces) and why supplementary testing is important. Links to Domain 1 (Water Assessment) and Domain 3 (Water Treatment).

### Section 9: Sizing Examples Worked Through—Climate & Demand Scenarios
Three detailed worked examples: (1) temperate climate, 2,000 sq ft roof, household + garden (annual demand ~15,000 gal; tank sizing calculation), (2) semi-arid climate, 1,500 sq ft roof, household only (demand ~5,000 gal; seasonal storage tradeoff), (3) tropical climate, 1,000 sq ft roof + ground catchment, large garden (demand ~25,000 gal; multi-season design). Each example includes local rainfall data, surplus/deficit graph, and tank recommendation.

### Section 10: Legal & Regulatory Context—US States & International
State-by-state summary of rainwater harvesting legality/restrictions in US (note: increasingly legal; some states restrict potable use without treatment). Explains permit requirements and exemptions by state. Includes international context (Australia, Kenya, Brazil examples). Explains what to check with local building/zoning dept before installation. Links to state extension office resources.

### Section 11: System Installation—Gutters, Downspouts, Routing & Overflow
Step-by-step procedure for installing a basic rainwater system: gutter sizing (½" for small buildings, ¾"+ for larger), downspout routing, overflow design (how excess water leaves the system during heavy rain), and tank placement relative to distribution points. Includes safety considerations (tank overflow into neighbors' property, tank stability/anchoring) and freeze-protection (draining downspouts in winter climates).

### Section 12: Distribution & Irrigation Use—Pumping Options & Water Delivery
Methods for getting water from tank to point of use: gravity feed (simple, requires elevated tank), manual (bucket/pump), and motorized (submersible pump, pressure tank). Explains pump sizing (gallons per minute needed, head pressure required), power requirements (hand, solar, electric), and cost. Includes procedure for setting up simple drip irrigation from stored rainwater.

### Section 13: Maintenance Schedules & Troubleshooting
Annual/seasonal maintenance calendar: pre-season checks (gutters clear, tank accessible), in-season monitoring (sediment buildup, algae growth), and post-season shutdown (draining gutters in freeze zones, tank winterization). Common problems and fixes: gutter leaks (replacement section, sealing), tank cracks (epoxy repair, patching), algae bloom (cover improvement, algaecide use), mosquito breeding (tight lid, screen any openings).

### Section 14: Cost Analysis & ROI—System Economics Over Time
Tables comparing upfront costs (tank, gutters, filters, installation) vs. water cost savings (depends on local water rates, tank size, usage). Includes 10-year and 20-year payback analysis. Explains soft benefits (water independence, resilience, stormwater reduction) that don't show in pure ROI but matter in water-scarce or unstable-grid contexts.

### Section 15: Advanced Topics & Resources
Pointers to more sophisticated approaches: stormwater harvesting at scale (municipal/commercial), greywater system integration (Domain 4), monitoring systems (flow meters, tank level sensors), and modeling tools (IRRI's DSSAT for climate impact on rainfall patterns). Links to permaculture design resources and academic papers on rainwater systems in various climates.

---

## Domain 3: Water Treatment & Purification

### Section 1: Understanding Contamination & Treatment Goals—When Treatment Is Needed
Explains three contamination categories (biological, chemical, physical) and which treatments address each. Establishes the decision framework: Is water certainly unsafe (needs treatment before drinking) or just uncertain (testing can clarify)? Covers when treatment is insufficient (permanently unsafe sources, requires finding alternative water). Links to Domain 1 (Water Assessment) for testing procedures.

### Section 2: Boiling—Time, Temperature & Altitude Adjustments
Procedure for safe drinking water via boiling: time required at sea level (1 minute rolling boil) and adjusted times by altitude (3 minutes at 6,500 ft; 5 minutes at 10,000 ft). Explains what boiling kills (pathogens: bacteria, viruses, parasites) and doesn't kill (chemical pollutants, heavy metals, salts). Includes fuel efficiency tips (insulated pot, covering water, Group boiling). Cost analysis (estimated fuel cost per gallon in different regions).

### Section 3: Chemical Disinfection—Chlorine & Iodine Dosing by Water Quality
Procedure for chlorine disinfection: calculating dose based on water volume and desired final residual (0.5–1 ppm free chlorine). Includes dose tables for different chlorine sources (household bleach 5% available chlorine, calcium hypochlorite, chlorine tablets). Covers contact time (at least 30 minutes before drinking) and color-matching test strips to verify treatment. Explains when chlorine is ineffective (high turbidity, some protozoa) and requires pre-filtration or alternative methods.

### Section 4: Iodine & Potassium Permanganate Alternatives
Procedures for iodine tablets/liquid (dosing, waiting time before drinking, taste concerns) and potassium permanganate (iron/manganese removal, oxidation). Covers advantages (portable, lightweight) and limitations (taste/odor, cost, health concerns with long-term use of iodine). Explains when each is best suited (emergency travel vs. long-term treatment). Includes contraindications (pregnancy, thyroid issues) for iodine.

### Section 5: Settling & Sedimentation—Pre-Treatment for Turbid Water
Procedure for simple sedimentation: pouring water into clean container, waiting 1–2 hours for particles to settle, carefully pouring clear water into clean container (leaving sediment behind). Explains effectiveness (removes coarse particles, some bacteria-laden sediment) and limitations (very slow, doesn't remove viruses, requires large volume tanks). Useful as pre-treatment before boiling or chemical disinfection.

### Section 6: Cloth Filtration—Folding & Using Simple Filters
Procedure for filtering water through clean cloth (double-folded cotton material, clean cloth napkin, or purpose-made cloth filters). Explains effectiveness (removes coarse particles, some bacteria; reduces turbidity). Includes repeated-filtering technique (pushing water through multiple times) to improve clarity. Covers cloth maintenance (washing, drying, storage). Low-cost, no-equipment option for reducing contamination visibly.

### Section 7: Sand Filtration—DIY Slow Sand & Biosand Filter Construction
Detailed procedure for building a simple sand filter: 5-gallon bucket or 55-gallon drum, 1–2 feet of fine sand, gravel layer (prevents sand loss), collection container below. Includes packed sand filter (water poured in, filtered through sand layer, collected below) and upflow filter designs. Explains filtration rate (slow sand: 1–3 gallons/hour; faster designs: 5–10 gal/hr), effectiveness (turbidity reduction, some pathogen removal, improves water clarity). Covers sand selection, pre-filtering water before sand, and regeneration (stirring top layer, backflushing).

### Section 8: Ceramic & Membrane Filtration—Commercial Filters & Maintenance
Overview of commercial ceramic filters (Doulton, OriginClear, similar brands), membrane filters (ultrafiltration, nanofiltration), and performance claims. For each: cost, replacement cartridge frequency and cost, effectiveness (what pathogens/chemicals removed), maintenance requirements. Explains difference between filters (remove particles down to micron/submicron size) and RO (true removal of dissolved solids and salts). Covers when filters are worth the cost investment vs. boiling/chemical.

### Section 9: Multi-Stage Treatment—Combining Methods for Comprehensive Safety
Procedure for combining multiple methods (settling → filtration → boiling, or filtration → chlorination) to address different contamination types. Explains when each stage is needed: pre-treatment (settling/filtration) removes particles and visible contamination, disinfection (boiling/chlorine) addresses pathogens. Includes decision flowchart: "Water has [description]—use [method sequence]." Covers order-of-operations (e.g., filter before chlorinating to avoid consuming excess chlorine on particles).

### Section 10: Addressing Specific Contaminants—Chemical & Heavy Metal Concerns
Clear explanation of contaminant types beyond pathogens: pesticides, petroleum, heavy metals (lead, arsenic, mercury), and what treatment works for each. Honest assessment: boiling and simple filtration don't remove chemicals. Covers activated charcoal filter effectiveness (limited; works for some organics, not metals). Directs readers to professional testing for suspected chemical contamination. Includes natural/alternative materials (coconut shell charcoal, locally activated charcoal) with caveats about effectiveness.

### Section 11: Testing Water After Treatment—Confirming Safety
Links to Domain 1 procedures for testing treated water: checking for residual chlorine (test strip), clarity assessment, odor/taste evaluation, and when to do post-treatment testing (after first use of a system, monthly if routine treatment, after source changes). Includes troubleshooting: "Treated water smells bad—what now?" (reboil, change carbon filter, investigate source).

### Section 12: Storage of Treated Water—Maintaining Potability After Treatment
Procedure for storing treated drinking water safely: clean, covered containers (prevents recontamination from air/dust), cool location (reduces chlorine loss, bacterial growth), and reasonable timeframe (boiled water in sealed container: 2–4 days; chlorinated water: 1 week; best practice: use within 24 hours). Includes labeling (date treated, source, method used) and rotation (oldest first).

### Section 13: Case Studies—Common Water Contamination Scenarios
Worked examples: (1) after flooding, surface water with high turbidity and suspected bacterial contamination—treatment sequence, testing, and confirmation. (2) Private well with brown/iron-stained water—treatment approach and when professional help is needed. (3) Disaster response with unknown water quality—rapid assessment, treatment on-site, and distribution to community.

### Section 14: Treatment in Austere Contexts—Improvisation & Limitations
Practical guidance for situations where commercial supplies are unavailable: boiling with scarce fuel (most reliable), chemical disinfection alternatives (bleach from other sources, iodine substitutes), and cloth/sand filtering with local materials. Honest assessment: some scenarios offer no reliable treatment with available resources. When that's the case: finding alternative water sources (rainwater, springs known to be safe, etc.).

### Section 15: Resources & References
Links to WHO, CDC, EPA drinking water quality standards, academic papers on field water treatment, treatment product recommendations (brands, where to source), and contact info for water system support orgs (environmental health depts, humanitarian orgs). Includes offline pointers and permission to print relevant CDC documents.

---

## Domain 4: Wastewater & Greywater Systems

### Section 1: Understanding Wastewater Streams—Classification by Source & Safety
Explains water categories: potable (drinking/cooking water), greywater (sink, shower, laundry—minimally contaminated), blackwater (toilet—highly contaminated with fecal pathogens), and yellow water (urine). For each: contaminant profile, basic treatment needed, safe reuse applications, and health risks. Establishes decision framework: what water can be safely reused with minimal treatment, what needs professional treatment, what must be disposed of.

### Section 2: Greywater Reuse—Safety, Legal Limits & Regulations
Explains what greywater reuse means: redirecting sink/shower water to landscape irrigation. Covers safety considerations: soap residues, food particles, potential pathogens, and pH changes. Includes regulatory framework: most US states prohibit potable reuse of greywater without treatment, allow non-potable uses (landscape, toilet flushing) under specific conditions. Procedure: check local code before any system, get permits where required, understand liability. Links to state extension office summaries of greywater legality.

### Section 3: Simple Greywater Systems—Gravity-Fed Landscape Irrigation
Procedure for minimal-treatment greywater: capturing sink/shower water in tank, simple settling/screening to remove food/hair particles, and gravity-fed drip irrigation to landscape. Includes system components (diverter valve, tank, filter, distribution lines), sizing (for household greywater volume ~30–50 gal/day), and siting (tank elevated relative to garden for gravity feed). Cost estimates and typical lifespan.

### Section 4: Greywater Filtration & Treatment—Settling, Sand & Biological Options
Methods for improving greywater quality before reuse: settling (remove solids), sand/gravel filtration (improve clarity, remove suspended particles), and biological treatment (constructed wetlands, simpler systems like gravel-planted-with-vegetation). Explains effectiveness (treatment reduces but doesn't eliminate pathogens—greywater remains non-potable even after treatment) and maintenance needs. Includes DIY constructed wetland design (small wetland cells planted with reeds/iris, water flows through substrate, emerges cleaner).

### Section 5: Septic System Basics—Maintenance & Care
Overview of septic systems (tank + drainfield) as the most common on-site wastewater treatment in rural areas. Covers how a septic system works (solids settle in tank, bacteria break down waste, effluent flows to drainfield, soil absorbs and filters), maintenance (pumping tank every 3–5 years, not flushing non-degradable items), and common problems (tank failure, drainfield saturation, surface discharge). Procedure for septic system inspections and pump-out scheduling.

### Section 6: Septic Troubleshooting—Failure Signs & Remediation
Symptoms of septic failure: slow drains, backup into house, wet patches over drainfield, persistent odors. For each symptom: likely causes and remediation steps. Covers when professional help is needed (tank structural failure, drainfield redesign) vs. when owner can fix (pumping tank, reducing water use, improving drain maintenance). Includes cost estimates for repair vs. replacement.

### Section 7: Septic-Safe Practices—What Not To Flush
Explains products that damage septic systems: paper towels, cat litter, feminine hygiene products, medications (harm bacteria), grease (clogs pipes/tank), and toxic chemicals (antibiotic cleaners). For each: why it's problematic and safe alternatives. Procedure: maintaining a septic-friendly household (minimize flushing, choose septic-safe products, monitor drains). Includes cost-effective septic maintenance (bacteria additives—effectiveness debated; focusing on behavior is better).

### Section 8: Blackwater Treatment—Composting Toilets & Alternative Systems
Overview of blackwater treatment options beyond septic: composting toilets (human waste to compost, minimal liquid output, no septic needed), waterless systems (chemical or compost-based), and advanced treatment (media filters, lagoons). For each: capital cost, maintenance requirements, suitability for different contexts. Explains when each is preferred: waterless/compost in water-scarce areas, composting for off-grid, septic for conventional.

### Section 9: Composting Toilet Installation & Maintenance
Detailed procedure for selecting and installing a composting toilet: site choices (inside with external vent, outside as separate structure), power requirements (ventilation fan for aerobic vs. passive systems), and maintenance (adding carbon material, monitoring liquid output, harvesting finished compost). Includes DIY designs (building simple composting structure around toilet seat) and commercial models (Nature's Head, Sun-Mar). Explains learning curve and maintenance labor required.

### Section 10: Greywater + Septic Integration—System Design Considerations
When systems are combined (greywater irrigation + septic for blackwater): design considerations for keeping them separate (greywater doesn't go through septic—reduces septic load) and when to integrate (small properties where separate drainfield isn't feasible). Procedure for greywater diversion system that lets greywater bypass septic tank. Includes code considerations (most jurisdictions require blackwater to go through septic, but allow greywater diversion).

### Section 11: Constructed Wetlands—Design & Operation
Procedure for designing a constructed wetland for greywater treatment: site with good drainage, sizing (surface area relative to flow rate), substrate (gravel, sand, soil), and vegetation (reeds, cattails, willows). Explains how wetland works (water filters through substrate, plants uptake nutrients, soil bacteria process pollutants). Includes maintenance (harvesting plants periodically, monitoring water level, troubleshooting standing water/odors). Applicable at household or small community scale.

### Section 12: System Sizing Examples—Household & Small Community
Worked examples: (1) household of 4, greywater only (50 gal/day), designing simple gravity system for 0.5 acre garden. (2) Small community (20 households), blackwater through septic, greywater to constructed wetland, tank sizing and drainage design. Each includes calculation worksheets, cost estimates, and maintenance labor.

### Section 13: Code Compliance & Permitting—What Local Authorities Require
Procedure for getting wastewater system approval: what permits are needed (septic/drainfield design approval, greywater system permits—varies by state), site assessment requirements (soil testing, percolation test), and system design review. Includes regional variations (coastal areas often stricter; rural areas may be more flexible). Forms and contact info for county health dept/extension office. Emphasizes that unpermitted systems create liability and resale problems.

### Section 14: Household Water Audit—Reducing Greywater Volume
Simple procedure for measuring household water use (showers, laundry, sinks) and identifying high-volume opportunities for reduction: low-flow fixtures, shorter showers, load-appropriate laundry machine. Includes calculations: smaller greywater volume = smaller treatment system = lower cost. Links to cost/benefit analysis of conservation vs. system expansion.

### Section 15: Resources & Advanced Topics
Links to EPA onsite wastewater treatment guides, state extension office bulletins on septic/greywater, DIY constructed wetland designs, and contacts for water system designers and inspectors. Pointers to commercial treatment systems (Advanced Enviro-Septic, FAST chambers) for those choosing commercial over DIY. Includes references to household water reuse literature and permaculture-integrated wastewater design resources.

---

## Implementation Notes

### Section Depth
Each section is written as a complete, standalone chapter (typically 800–1,500 words when fully written). Sections assume readers may not read sequentially (offline access, search-based discovery); each includes sufficient context to be self-explanatory.

### Cross-Domain Links
Sections include "See Domain X, Section Y" links to related procedures in other water domains (e.g., Domain 3, Section 1 links to Domain 1 for testing procedures; Domain 2 links to Domain 3 for treating collected rainwater).

### Visual & Practical Focus
Outlines are written with visual learners in mind: each section emphasizes numbered steps, decision trees, photographs/diagrams, and tables over abstract explanation. Full content will include placeholder notes for diagrams, photos, and worksheets.

### Contributor Assignment Strategy
These outlines are designed for different contributor types: Sections 1–2 of each domain (conceptual overview) can be authored by the maintainer using authoritative sources. Sections 3+ (procedures, case studies) are ideal for practitioner contributors with field experience. Wave 0 contributors will be invited to submit content for specific outlined sections.

---

*Prepared 2026-07-04. Ready to guide content development and external contributor submissions.*
