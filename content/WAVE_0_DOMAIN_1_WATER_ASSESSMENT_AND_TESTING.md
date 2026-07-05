---
title: "Water Assessment & Testing: How to Know if Water Is Safe"
domain: "water-systems"
domain_number: 1
article: "1.0"
section: "water-assessment-and-testing"
content_type: "procedure"
difficulty: "beginner"
estimated_read_time: "35 minutes"
author: "Open-Repo Project"
last_updated: "2026-07-05"
project: open-repo
phase: "5.2 Wave 0"
status: active
confidence: 87%
estimated_word_count: 7400
license: "CC-BY-4.0"
sources_verified: true
cross_references:
  - "WAVE_0_DOMAIN_3_BOILING_AND_HEAT_TREATMENT.md"
  - "WAVE_0_DOMAIN_3_CHEMICAL_DISINFECTION.md"
  - "WAVE_0_DOMAIN_3_FILTRATION_AND_BIOSAND.md"
  - "projects/systems-resilience/individual/01-water.md"
  - "projects/off-grid-living/03-water.md"
---

# Water Assessment & Testing: How to Know if Water Is Safe

## Overview & Value

Before treating water, you need to know what you are treating. Using the wrong method wastes time and resources and—more importantly—may give you false confidence in water that is still dangerous.

This guide walks through every level of water assessment: what your eyes, nose, and basic observation can tell you; what commercial test kits reveal and where they fall short; how to collect a sample correctly; how to read results; and when field assessment alone is enough versus when you need a certified laboratory.

**Who should read this**: Anyone using a private well, collecting surface or rainwater, managing water after a flood or emergency, or setting up a household monitoring plan. No prior water testing knowledge is required.

**What you'll learn**: The complete assessment sequence from visual observation through commercial test kits to lab referral; which contaminants field tests detect reliably and which they miss; how to avoid the most common testing errors; and how to convert results into treatment decisions.

**Key decision points**:
- Can I see, smell, or taste a problem? (Section 2 — visual assessment)
- Which test kit is right for my source type? (Section 3 — commercial test kits)
- My source is in an agricultural area — what do I need to test for? (Section 4 — chemical contaminants)
- How do I collect a sample without ruining the result? (Section 5 — field procedures)
- My test came back positive — what does that mean? (Section 6 — interpreting results)
- How often should I test, and when should I call a lab? (Section 7 — decision framework and frequency)

---

## Section 1: Why Water Testing Matters — The Problem Statement

### 1.1 What Visually Safe Water Can Hide

Water that looks clear, smells neutral, and tastes fine can still make you seriously ill. The most dangerous waterborne pathogens — including *E. coli* O157:H7, *Cryptosporidium*, hepatitis A virus, and Giardia — are invisible to the naked eye and have no reliable taste or odor.

The opposite is also true: water that looks brown, smells like rotten eggs, or has a metallic taste may be unpleasant but not acutely dangerous. Iron, manganese, and hydrogen sulfide commonly cause bad taste and odor at levels that are nuisance problems rather than health emergencies.

This means that:

1. **Visual clarity does not confirm safety.** A positive visual assessment tells you what to rule out, not that water is safe.
2. **Visual problems do not automatically confirm danger.** Many aesthetic issues are treatable without emergency action.
3. **Testing is the only way to know.** Each assessment level — visual, field kit, laboratory — gives you different information about different threat types.

### 1.2 The Three Contamination Categories

Every water source can contain three types of contamination. Understanding which type you are testing for is essential to choosing the right test.

| Category | What It Includes | What Tests Detect It | What Treatment Addresses It |
|----------|-----------------|---------------------|---------------------------|
| **Biological** | Bacteria (*E. coli*, coliforms, Salmonella), viruses (norovirus, hepatitis A), protozoa (Giardia, Cryptosporidium), worms/helminths | Coliform/E. coli test kits; turbidity (proxy only) | Boiling, chemical disinfection (chlorine/iodine), UV treatment, filtration to <0.1 micron |
| **Chemical** | Nitrates, pesticides (atrazine, glyphosate), heavy metals (arsenic, lead), PFAS, petroleum compounds | Nitrate test strips; multi-parameter kits; lab testing for most chemicals | Activated carbon (limited), reverse osmosis, distillation; boiling and standard filtration do NOT remove chemicals |
| **Physical** | Turbidity (suspended particles), color, sediment, temperature | Visual assessment; turbidity tubes; test strips for pH and hardness | Settling, filtration, pH adjustment |

**The critical point for field users**: Boiling kills biological threats but does nothing for chemical contamination. If you suspect agricultural or industrial chemical contamination, no field treatment method makes that water safe — you need lab testing and an alternative source.

---

## Section 2: Visual Assessment — What You Can Learn Without Any Equipment

Visual assessment is your first filter. It takes no equipment, no cost, and no time beyond the observation itself. Done systematically, it tells you which tests to run first and whether a source is immediately unusable.

### 2.1 Turbidity — Cloudiness Assessment

Turbidity is the measure of how much suspended material is in the water. High turbidity signals particles that may harbor pathogens, and it directly interferes with disinfection effectiveness.

**The white paper method** (field substitute for a turbidity meter):

1. Fill a clear glass or plastic container to about 15 cm (6 inches) depth.
2. Hold a sheet of white paper with black text printed on it behind the container.
3. Look through the water from the front and try to read the text.
4. Interpret results:

| What You See | Estimated Turbidity | Implication |
|-------------|--------------------|------------------------------------|
| Text is clearly readable | <4 NTU | Chlorination may proceed at standard dose (if biological only) |
| Text is blurry but present | 4–20 NTU | Pre-filter before chemical treatment; double chlorine dose |
| Text is not visible | >20 NTU | Filter or settle before any treatment; chlorination alone will fail |
| Water is opaque or visibly colored | >100 NTU | Heavy treatment required; this water should not be used for drinking until extensively treated and tested |

**Important note on the threshold**: The WHO recommends turbidity below 1 NTU before disinfection for municipal systems. For field conditions, the practical limit for chlorination to be effective is 5 NTU. Above 5 NTU, particles physically shield pathogens from contact with chlorine, and disinfection cannot be confirmed without post-treatment testing. [Sources: 1, 2]

**Why turbidity matters for Cryptosporidium specifically**: *Cryptosporidium* oocysts (resistant cysts) attach to suspended particles. Even at turbidities that chlorination would otherwise handle, *Cryptosporidium* in turbid water may not be killed. This protozoan requires filtration (not just chlorination) for reliable removal.

### 2.2 Color Assessment

Color tells you about the mineral and organic content of water, not directly about pathogens. Use this table to interpret what you see:

| Water Color | Likely Cause | Health Relevance | Immediate Action |
|-------------|-------------|-----------------|-----------------|
| Clear | Normal; no unusual suspended material | No indication from color alone | Proceed to other assessment |
| Light yellow / pale straw | Tannins from organic matter; peat soils | Not a direct health threat but may indicate high organic load | Test for total organic carbon if available; use carbon filtration |
| Brown or rust | Iron or manganese oxidation; disturbed sediment; surface infiltration | High iron/manganese: taste/nuisance; but brown after flooding indicates surface contamination — test for coliform | Test coliform urgently if recent flooding or runoff is possible source |
| Red/dark orange | Very high iron (>0.3 mg/L); sometimes iron bacteria | Nuisance but not acutely dangerous; iron bacteria can degrade water quality over time | Test for iron; consider iron removal treatment |
| Black or dark gray | Manganese; hydrogen sulfide; coal or industrial runoff | May indicate industrial contamination or high manganese (neurological risk at high levels) | Lab testing required before use |
| Green | Algae bloom; algal toxins possible | Algal toxins (cyanotoxins) can cause liver damage; boiling does NOT remove algal toxins — it can concentrate them | Do not use for drinking; find alternative source; lab testing required |
| Milky white | Dissolved air (harmless); very fine suspended mineral particles | Air in water is harmless and clears in minutes; persistent white/gray suggests particles | Let sit 5 minutes and observe whether it clears |

**The most important color rule**: Brown water immediately following flooding of a well or surface source must be treated as biologically contaminated until tested. Flooding introduces surface pathogens into groundwater systems. [Source: 3]

### 2.3 Odor Assessment — Safe Sniffing Protocol

You should never smell water directly from an open container by putting your nose over it. Instead:

1. Fill a clean glass about halfway.
2. Cover the glass with your palm for 30 seconds.
3. Remove your hand and wave it gently over the glass to direct air toward your nose.
4. Inhale gently. Do not inhale deeply from the glass itself.

**Interpret what you smell**:

| Odor | Likely Cause | What It Means | Action |
|------|-------------|--------------|--------|
| None | Normal | No odor clue; proceed to other tests | Test as normal |
| Chlorine (pool-like) | Residual disinfectant from treatment | Expected if source is treated municipal water; not a health concern at low levels | If strong in private well: investigate recent shock chlorination |
| Rotten eggs (sulfur/hydrogen sulfide) | Naturally occurring hydrogen sulfide; iron bacteria in well; anaerobic bacterial activity | Not acutely dangerous at low levels but indicates bacteria may be present; unpleasant | Test coliform; aeration or carbon filtration addresses odor |
| Musty/earthy | Iron bacteria; algae; organic decomposition | Suggests biological activity; may mean bacterial or algal contamination | Test coliform; also visually inspect storage tanks or well casing |
| Chemical/petroleum/solvent | Industrial or agricultural chemical contamination; fuel spill near well | Potential serious contamination — do not use; this type does NOT respond to boiling or standard filtration | Do not treat in field; seek lab testing; find alternative source |
| Sewage/fecal | Septic system infiltration; surface fecal contamination | High risk of pathogen contamination; treat as biologically unsafe until tested | Treat as unsafe; test immediately; shock chlorinate well if confirmed pathogen source |

**Critical safety rule**: A chemical or petroleum smell is a reason to stop using the source entirely until lab testing confirms what the contaminant is. No household treatment method reliably removes petroleum hydrocarbons or industrial solvents. [Source: 4]

### 2.4 What Visual Assessment Cannot Tell You

Visual assessment cannot detect:
- Nitrates (colorless, odorless, tasteless at dangerous levels)
- Most pesticides and herbicides
- Heavy metals including lead and arsenic
- PFAS ("forever chemicals")
- Most viruses and bacteria at typical infectious doses
- *Cryptosporidium* and *Giardia* oocysts/cysts

**Key message**: A visually clean, odorless, clear water sample may still be unsafe. Visual assessment filters out obvious problems — it does not confirm safety.

---

## Section 3: Commercial Test Kits — Selection, Use, and What They Actually Tell You

### 3.1 Categories of Available Test Kits

Commercial test kits fall into three categories by what they test:

1. **Coliform/E. coli presence/absence tests** — detect fecal indicator bacteria
2. **Chemical parameter strips** — test pH, nitrate, hardness, chlorine residual, iron, and other dissolved parameters
3. **Multi-parameter kits** — combine multiple tests in one package

For household water safety in an emergency, **coliform/E. coli testing is the highest priority** because biological contamination is the most common cause of acute illness from untreated water. Chemical testing is important for long-term safety, particularly for agricultural area wells, but most chemical contamination does not cause immediate illness.

### 3.2 Coliform and E. Coli Test Kits — Brands, Specs, and Accuracy

**What these tests detect**: Total coliform bacteria are a broad group of bacteria, some from fecal sources and some from soil. *E. coli* is the specific bacterium that indicates fecal contamination. A positive E. coli test is more serious than a positive total coliform result.

| Brand / Product | Test Type | Time to Result | Approximate Cost | What It Tests | Key Limitations |
|----------------|-----------|----------------|-----------------|---------------|-----------------|
| **IDEXX Colilert** | Enzyme-based presence/absence or quantitative | 18–24 hours | $8–15/test | Total coliform + E. coli simultaneously | Incubation at 35°C required; not fully DIY without incubator; lab-standard accuracy |
| **Colisure (IDEXX)** | Enzyme-based presence/absence | 24 hours | $5–12/test | Total coliform + E. coli | Same incubation requirement; widely used in field settings with portable incubators |
| **3M Petrifilm Aqua Coliform Count Plates** | Culture-based enumeration | 24 hours | $4–8/plate | Total coliform count | Validated for bottled water; designed for laboratory use; AOAC Performance Tested Method |
| **WaterSafe Bacteria Test** | H2S medium (presence/absence, indirect) | 48 hours | $10–20/kit | H2S-producing bacteria as coliform proxy | Does not directly test E. coli; false negatives possible for non-H2S coliforms |
| **ITS Total Bacteria/Coliform Test** | Growth medium | 48 hours | $12–25/kit | Coliform + general bacteria | No incubator required (room temperature); less sensitive than enzyme-based methods |
| **Simple Well Water Test Kit (multiple brands)** | Multi-parameter strip + bacteria vial | 48 hours | $15–30/kit | Coliform + pH + nitrate + hardness + chlorine | Low sensitivity for bacteria; strips not validated against EPA methods; primarily screening use |

**Understanding false positives and false negatives**:

- **False positive** (test says contaminated when water is actually clean): Can be caused by contaminating the sample vessel, using tap water to rinse collection containers, or testing water with high non-coliform bacterial counts that can cross-react with some culture media.
- **False negative** (test says clean when water is actually contaminated): The most dangerous error. Causes include: insufficient contact time with medium, too short an incubation period, testing water with residual chlorine that kills bacteria before the test runs, or dilute contamination below the test's detection limit.

**The IDEXX Colilert advantage over culture media**: Traditional culture media allows non-target bacteria to grow and mimic coliform appearance (causing false positives). Enzyme-based methods like Colilert target the specific enzyme (β-galactosidase for total coliform, β-glucuronidase for E. coli) and have three times lower false-positive rates than membrane filtration methods. [Source: 5]

**Residual chlorine interference**: If your water has been recently chlorinated (including shock chlorination of a well), wait at least 5–7 days before bacterial testing, or add sodium thiosulfate to the sample bottle to neutralize residual chlorine. Residual chlorine will kill bacteria in your sample bottle and produce a false negative. Most lab-provided sample bottles already contain sodium thiosulfate — this is one reason lab-provided containers are preferred over generic bottles.

### 3.3 Chemical Parameter Test Strips

These are simpler, faster, and more affordable than bacterial tests, but they test for different threats:

| Parameter | What It Indicates | EPA MCL | Test Strip Cost | Accuracy in Field |
|-----------|------------------|---------|----------------|------------------|
| **Nitrate (NO3)** | Agricultural fertilizer runoff; septic leakage; infant risk | 10 mg/L as N | $0.50–2/strip | Moderate; strips read ±2–5 mg/L; adequate for screening but lab recommended for infants |
| **pH** | Corrosivity; disinfection efficiency; taste | Secondary standard 6.5–8.5 | $0.10–0.50/strip | Good for range estimation; not precise to 0.1 units |
| **Free chlorine residual** | Confirms chlorination treatment was effective | Target 0.2–0.5 mg/L | $0.25–1/strip | Reliable at concentrations above 0.1 mg/L |
| **Total hardness** | Dissolved calcium/magnesium; scale, taste | Secondary standard; no health MCL | $0.25–1/strip | Good; reliable estimation |
| **Iron** | Dissolved iron; taste and staining | Secondary standard 0.3 mg/L | $0.50–2/strip | Adequate for above/below threshold determination |
| **Manganese** | Dissolved manganese; neurological risk at >0.3 mg/L | Secondary 0.05 mg/L (advisory) | $1–3/strip | Less reliable; lab confirmation recommended if above threshold |

**Practical note on multi-parameter strips**: Products that test 7–10 parameters on a single strip (common pool test strips adapted for drinking water) are useful for quick screening but are not validated against EPA drinking water methods. Use them to identify which specific parameters need closer attention, then follow up with individual validated tests or lab analysis for any parameters showing elevated values.

### 3.4 The Turbidity Tube — Low-Cost Measurement Without Equipment

A turbidity tube (also called a T-tube) allows you to estimate NTU without a meter. It is the recommended field tool for communities with limited resources. [Source: 6]

**How to build a turbidity tube from local materials**:

1. Obtain a clear plastic tube or pipe at least 60 cm (24 inches) long and 4–5 cm (1.5–2 inches) in diameter.
2. Seal one end with a clear plug or transparent tape.
3. On the sealed bottom end, affix a small black-and-white checkerboard pattern (8mm squares). Print or draw this on waterproof paper or tape.
4. Mark the tube at 10 cm, 20 cm, 30 cm, 40 cm, and 60 cm from the bottom.
5. To test: Stand the tube upright, sealed end down. Slowly pour your water sample into the tube. Stop when the checkerboard pattern just disappears from view. Record the water depth.

**Interpreting turbidity tube readings**:

| Water Depth When Pattern Disappears | Approximate NTU | Treatment Implication |
|------------------------------------|----------------|----------------------|
| >60 cm (full tube; pattern still visible) | <10 NTU | Suitable for chlorination at standard dose |
| 40–60 cm | 10–20 NTU | Pre-filter recommended; double chlorine dose if filtering is not possible |
| 20–40 cm | 20–50 NTU | Filter or settle before any disinfection |
| <20 cm | >50 NTU | Extensive pre-treatment required before any disinfection; water is not suitable for direct treatment |

---

## Section 4: Chemical Contaminants — When Field Testing Is Not Enough

### 4.1 Agricultural Contaminants That Survive Boiling and Filtration

This section addresses a critical gap in most emergency water guides: **boiling and standard filtration do not remove agricultural chemicals**. Users in farming regions with contaminated wells cannot make their water safe with heat or basic filters.

**Nitrates**:
- Source: Synthetic nitrogen fertilizers, manure from livestock operations, septic systems.
- Behavior: Highly water-soluble; readily leaches into groundwater, particularly in sandy soils or karst geology.
- Health risk: Nitrates above 10 mg/L cause methemoglobinemia (blue-baby syndrome) in infants under 6 months. Adults are generally not at risk from typical nitrate levels, but elevated levels in pregnant women are a concern.
- Does boiling help?: No. Boiling concentrates nitrates in water as water evaporates. **Never boil high-nitrate water for infant formula.**
- Does filtration help?: Standard filters (sand, cloth, carbon) do not remove nitrates. Reverse osmosis or distillation is required.
- Field detection: Nitrate test strips are adequate for screening; confirm with lab if strips show >5 mg/L and infants or pregnant women are drinking the water. [Sources: 7, 8]

**Atrazine**:
- Source: Widely used corn and sorghum herbicide; second most common pesticide found in US groundwater.
- Behavior: Moderately persistent in soil; moves into groundwater via sandy or permeable soils; most commonly found in shallow wells near agricultural fields.
- Health risk: Endocrine disruptor; possible carcinogen; EPA MCL 3 µg/L (3 ppb).
- Does boiling help?: No. Atrazine does not volatilize at boiling temperature.
- Does filtration help?: Granular activated carbon (GAC) partially reduces atrazine but effectiveness varies by contact time and filter age.
- Field detection: No reliable field kit. Lab testing required.
- When to suspect: Well within 1 mile of corn/sorghum fields; sandy or permeable soils between field and well. [Source: 9]

**Glyphosate**:
- Source: Most widely used herbicide globally (Roundup and generics). Found in agricultural runoff.
- Behavior: Binds to soil particles but can reach groundwater in sandy soils or after heavy rain; highly water-soluble.
- Health risk: Classified as probable human carcinogen by IARC; EPA MCL is 700 µg/L (700 ppb), which is very high — most actual contamination levels are far below this.
- Does boiling help?: No.
- Does filtration help?: GAC filtration provides partial removal. No field kit reliably detects glyphosate at low concentrations.
- Field detection: No reliable field kit. Lab testing required if suspected. [Source: 10]

**PFAS ("Forever Chemicals")**:
- Source: Industrial manufacturing, firefighting foam (AFFF), non-stick cookware production, many consumer products.
- Behavior: Extremely persistent; do not break down in environment; accumulate in groundwater near industrial sites, military bases, and airports.
- Health risk: PFOA and PFOS EPA MCL set at 4 parts per trillion (0.000004 mg/L) — among the strictest drinking water standards ever set.
- Does boiling help?: No. Boiling concentrates PFAS.
- Does filtration help?: Standard carbon filters do not reliably remove PFAS. Reverse osmosis or granular activated carbon specifically designed for PFAS is needed.
- Field detection: No field kit available. Lab testing required.
- When to suspect: Near military bases (former fire training areas), airports, industrial sites using fluorinated products, or areas with known PFAS plumes documented by state EPA. [Source: 11]

### 4.2 Minimum Testing Frequency for Wells in Agricultural Areas

For a private well used as a primary household water source, the CDC recommends annual testing at minimum. However, for wells in agricultural contexts, this baseline should be increased:

| Context | Recommended Minimum Testing Frequency | Priority Parameters |
|---------|--------------------------------------|-------------------|
| Any private well (baseline) | Annually | Total coliform, E. coli, nitrate, pH, total dissolved solids |
| Shallow well (<100 feet) in agricultural area | Every 6 months | Above + nitrate, pesticide screen |
| Well near livestock operations (within 0.5 mile) | Every 6 months (dry season and after spring thaw) | Above + nitrate, coliform (seasonal surface contamination) |
| Well with history of coliform positive results | Every 3 months for 1 year after last positive, then resume annual | Total coliform, E. coli |
| Well that has flooded | Immediately after water recedes + repeat 2 weeks later | Total coliform, E. coli, nitrate |
| Household with infant or immunocompromised member | Every 6 months | Total coliform, E. coli, nitrate |
| Recent well repair or pump replacement | Within 2 weeks of work | Total coliform, E. coli |

**Events that trigger immediate testing (at any time)**:
- Noticeable change in water color, odor, or taste
- Known flooding of the well casing or surrounding area
- Spill or visible contamination event near the well
- Illness in multiple household members with no other identified cause [Source: 12]

### 4.3 Site Indicators of Chemical Contamination Risk

Before testing, observe the area around your water source. These site features increase the probability that lab testing (not just field testing) is warranted:

**Biological and physical site indicators**:

1. **Concentrated animal feeding operations (CAFOs) within 1 mile**: High nitrate and coliform risk; manure storage and land application can reach shallow groundwater.
2. **Agricultural fields within 0.5 mile with visible spray equipment**: Pesticide risk in sandy-soil areas.
3. **Industrial facilities or former industrial sites within 1 mile**: Heavy metals, solvents, PFAS risk.
4. **Military bases or airports within 2 miles**: High PFAS risk from historical AFFF use.
5. **Older homes (pre-1986) with lead pipes or solder**: Lead leaching risk — not related to source water but to distribution pipes; test for lead separately.
6. **Septic tanks within 100 feet of well**: Nitrate and coliform risk.
7. **Fuel storage (above or underground tanks) within 500 feet**: Petroleum hydrocarbon risk.
8. **Geological indicators**: Karst (limestone) terrain, very sandy soils, or visible sinkholes near a well significantly increase infiltration risk.

**Vegetation indicators** (use as supporting evidence only, not as standalone indicators):

- Unusual die-off in aquatic plants in a stream used as a water source may suggest chemical runoff or dissolved oxygen depletion.
- Bright green algal mats on surface water indicate high nutrient loading (phosphorus, nitrogen) consistent with agricultural runoff; this water requires lab testing before use.
- No living organisms in a pond or stream (fish kills, no invertebrates) is a sign of serious chemical contamination.

---

## Section 5: Field Testing Procedures — Collecting Samples That Give Accurate Results

Sample collection errors cause more inaccurate test results than laboratory equipment failures. A clean laboratory cannot fix a contaminated sample. This section covers exactly how to collect a valid water sample.

### 5.1 What You Need Before You Start

**For bacterial (coliform/E. coli) testing**:
- A sterile, pre-labeled sample bottle — ideally one provided by your lab, which will contain sodium thiosulfate to neutralize residual chlorine. If using your own container, use a clean glass bottle that has been heat-sterilized (oven at 175°C/350°F for 1 hour, cooled before use).
- Clean, dry gloves — latex, nitrile, or plastic food service gloves.
- Permanent marker for labeling.
- Insulated cooler with ice (for transport; bacterial samples must be kept at ≤10°C and analyzed within 6 hours for most bacterial parameters).

**For chemical testing (nitrate, metals)**:
- For nitrate strips: clean plastic container; the bottle the strips come in.
- For lab chemical testing: a clean plastic (HDPE) or glass bottle of at least 500 mL, rinsed with distilled water or deionized water only — not tap water. Never rinse with the sample water.

**For multi-parameter strip testing**:
- The test strip container.
- A clean, dry glass or plastic cup (not washed with dish soap immediately before use — soap residues cause false high pH readings and can interfere with other parameters).

### 5.2 Collecting a Sample from a Faucet or Well Tap

This is the most common collection method for household well users.

**Step-by-step procedure**:

1. **Select the right faucet**: Use the cold water tap that most directly represents your well water — typically an outdoor faucet or laundry room faucet not connected to a water softener, filter, or treatment system. If you want to test treated water, use a kitchen tap after the treatment point.

2. **Remove aerator and screen**: Unscrew the aerator (the small screen attachment at the tip of the faucet). Aerators harbor bacteria that are not representative of your well water and will skew coliform results upward. This is the most commonly overlooked step and a major source of false positives for household coliform tests.

3. **Disinfect the faucet opening**: Wipe the faucet opening with a clean cloth or paper towel soaked in household bleach (unscented). Wait 30 seconds. Do not rinse off the bleach.

4. **Flush the line**: Open the tap fully and let water run for 3–5 minutes (or until water temperature stabilizes and any initial discoloration clears). This removes water sitting in the pipes, which is not representative of your groundwater.

5. **Open the sample bottle**: Open immediately before collecting. Do not touch the inside of the bottle, the inside of the cap, or set the cap down — this is the single most common source of sample contamination.

6. **Reduce the flow and fill the bottle**: Reduce the tap to a moderate flow. Hold the open bottle under the faucet and fill, leaving about 1 inch of air space at the top if using a liquid medium (not needed for strip tests). For bacterial testing, fill to the indicator line on the lab bottle.

7. **Cap immediately**: Cap the bottle without touching the interior.

8. **Label**: Write on the bottle: date, time, sample location (e.g., "kitchen cold tap after aerator removal"), and whether the water has been treated (e.g., "no treatment" or "shock chlorinated 7 days ago").

9. **Keep cold**: Place in an insulated cooler with ice. Bacterial samples must reach the laboratory or be analyzed within 6 hours of collection. If using a room-temperature commercial bacteria test kit (such as an H2S vial), follow the product's storage instructions.

### 5.3 Collecting a Surface Water Sample (Stream, Pond, River)

Surface water requires a different approach because you want to represent the bulk water quality, not just the surface (which may have floating material) or the bottom (sediment).

1. **Wear gloves** throughout the collection procedure.
2. **Wade into the water** if possible, or extend the collection bottle from shore, to avoid sampling disturbed sediment from the bank or bottom.
3. **Position the bottle**: Hold it about 30 cm (1 foot) below the water surface.
4. **Fill by scooping upstream**: With the bottle opening facing upstream (water flows into it), let it fill. This avoids collecting water that has passed over your hands or disturbed sediment in your immediate vicinity.
5. **Cap immediately** after removing from the water.
6. **Do not pour from one container into another**: Bacteria transfer easily.
7. **Label** with date, time, specific location (GPS coordinates if available, or clear description: "main stream channel, 50 meters downstream from bridge, center of flow").

### 5.4 Collecting a Rainwater or Cistern Sample

1. **Wait at least 5 minutes into a rain event** before collecting a sample, or open the first-flush diverter if your system has one. First-flush water contains roof contamination.
2. **Sample from the storage tank or cistern outlet**, not from the collection gutters.
3. **If sampling from inside a tank**: Use a clean bucket on a rope, pre-rinsed with distilled water. Lower to mid-depth; do not scrape the bottom.
4. Follow the same labeling and cold-storage procedure as other samples.

### 5.5 Common Field Testing Errors and How to Avoid Them

| Error | Why It Happens | How to Avoid It | Which Test It Affects |
|-------|---------------|----------------|----------------------|
| Not removing aerator | Aerators harbor biofilm with non-well bacteria | Always remove aerator before bacterial sampling | Coliform (causes false positives) |
| Touching inside of sample bottle | Transfers skin bacteria | Gloves; do not touch interior surfaces | Coliform (false positives) |
| Failing to flush the line | Water sitting in pipes has more bacteria than well water | Run tap 3–5 min before collecting | Coliform (both directions) |
| Residual chlorine in sample | Recent shock chlorination kills bacteria in test medium | Wait 5–7 days post-chlorination; use sodium thiosulfate | Coliform (false negatives) |
| Using expired test medium | Culture media degrades; enzyme activity declines | Check expiration dates; test within date range | All bacterial tests |
| Misreading color chart | Poor lighting; wet color block reference | Use the color chart in the same lighting as reading; compare to printed chart, not memory | Strip tests, color-comparison kits |
| Exceeding sample hold time | Bacteria multiply or die in transit, changing counts | Keep cold; reach lab within 6 hours for bacteria; 24 hours for nitrate | All parameters |
| Testing after heavy rain | Runoff temporarily introduces surface contamination | If well floods or surface runoff reaches casing, this is a real event — not a sampling error; repeat test after conditions normalize | Coliform |
| Using soapy containers | Surfactants kill bacteria and alter pH | Rinse containers with distilled water only; use clean containers not freshly washed with dish soap | Coliform, pH |

---

## Section 6: Interpreting Results — What Your Test Is Actually Telling You

### 6.1 E. Coli and Coliform Results

**Worked Example 1 — Positive E. coli result**:

You test your private well after heavy spring rains. The coliform/E. coli test returns positive for both total coliform and E. coli.

Step 1: Interpret the result correctly.

- E. coli in drinking water = zero tolerance under EPA drinking water standards. This is an extreme health hazard.
- E. coli indicates fecal contamination — human or animal feces has entered the water pathway.
- The presence of E. coli does NOT prove which other specific pathogens are present. However, it confirms that a contamination pathway exists between fecal material and your water. Viruses (norovirus, hepatitis A), other bacteria (Salmonella, Campylobacter), and protozoa (Giardia, Cryptosporidium) may also be present. You cannot test for them all — the positive E. coli is sufficient reason to treat the source as biologically unsafe for drinking until the source of contamination is identified and eliminated, and the water retests negative.

Step 2: Take immediate action.

1. Stop using the water for drinking, cooking, baby formula, ice-making, and tooth-brushing. Use bottled water or boiled water from a confirmed alternative source.
2. Shock chlorinate the well (see procedure in the well maintenance section of Domain 3).
3. Wait 5–7 days after chlorination, then flush until the chlorine smell is gone.
4. Retest for coliform and E. coli.
5. If the retest is negative, resume use but monitor again in 2 weeks to confirm.
6. If the retest is positive, the contamination source has not been eliminated. At this point, seek professional help — the problem may be a cracked casing, a compromised septic system, or surface infiltration that requires structural repair.

Step 3: Consider the cause.

Common causes of post-rain E. coli in a well:
- Shallow casing (well casing not extending above ground surface)
- Cracked or uncapped well casing
- Surface water running toward wellhead (poor grading)
- Nearby septic system within 100 feet

**Result decision tree for coliform/E. coli**:

```
Total Coliform: ABSENT
  → E. coli will also be absent
  → No fecal contamination detected
  → Water passes this test; proceed to chemical assessment if applicable
  → Retest: annually (or per your monitoring schedule)

Total Coliform: PRESENT, E. coli: ABSENT
  → Coliform detected but no definitive fecal indicator
  → Water is a potential health hazard; contamination pathway exists
  → Possible causes: soil bacteria, non-fecal organic material, aerator contamination
  → Action: Resample (remove aerator, flush thoroughly, use lab bottle)
  → If second test also positive: shock chlorinate; investigate casing and wellhead
  → Retest after 48 hours of chlorination and 5-day flush

Total Coliform: PRESENT, E. coli: PRESENT
  → Confirmed fecal contamination
  → Extreme health hazard — do not drink
  → Stop use; shock chlorinate; retest; investigate source
  → Retest in 7–14 days post-treatment
```

### 6.2 Nitrate Results

**EPA MCL for nitrate**: 10 mg/L as nitrogen (often written as "10 ppm NO3-N"). Some test strips measure as nitrate (NO3) rather than nitrate-nitrogen (NO3-N) — these show different numbers for the same water. Check your test strip labeling.

**Converting between units**:
- Nitrate (NO3) divided by 4.4 = Nitrate-Nitrogen (NO3-N)
- Example: 44 mg/L NO3 = 10 mg/L NO3-N (this is the EPA MCL)

**Risk by result level**:

| Nitrate-Nitrogen (mg/L) | Risk Level | Action |
|------------------------|-----------|--------|
| <5 mg/L | Low | No action needed; retest annually |
| 5–9 mg/L | Moderate | Safe for adults; caution for infants and pregnant women; monitor every 6 months |
| 10–20 mg/L | Exceeds MCL | Do not use for infant formula or as primary drinking water for infants; adults can tolerate but should seek alternative; do not boil (concentrates nitrate) |
| >20 mg/L | High | Do not use for drinking by anyone; find alternative source; lab testing to confirm level |

**Worked Example 2 — Nitrate result near threshold**:

You are in a rural agricultural county. Your well test strip shows approximately 8–9 mg/L nitrate-nitrogen. Your household includes a 3-month-old infant.

- This level is below the EPA MCL of 10 mg/L.
- However, the strip's accuracy is ±2–5 mg/L, meaning the actual level could be 6–14 mg/L.
- Given the uncertainty and the presence of an infant, you should:
  1. Immediately switch to bottled water for infant formula.
  2. Submit a sample to a certified lab for a precise nitrate measurement.
  3. If the lab confirms >10 mg/L, use bottled water for the infant until a reverse osmosis system is installed or an alternative source is confirmed.
  4. Never boil water to reduce nitrate — boiling increases the concentration as water volume decreases.

### 6.3 Turbidity Results

| Turbidity (NTU) | Implication | Treatment Decision |
|----------------|-------------|-------------------|
| <1 NTU | Excellent clarity; disinfection can proceed normally | Chlorinate at standard dose; proceed |
| 1–5 NTU | Acceptable; chlorination may proceed | Standard chlorine dose; 30-min contact time |
| 5–10 NTU | Elevated; chlorination reliability reduced | Pre-filter with cloth or sand; double chlorine dose; extend contact time to 60 min |
| 10–50 NTU | High turbidity | Filter and settle first (1–2 hours minimum); then disinfect; consider boiling instead |
| >50 NTU | Very high turbidity | Extensive pre-treatment required; do not attempt chlorination without filtration; boiling is preferred if fuel available |

**See Domain 3 (Water Treatment & Purification)** for the complete pre-treatment and multi-stage treatment sequence.

---

## Section 7: Decision Framework — Field Testing vs. Laboratory Testing

### 7.1 When Field Testing Is Sufficient

Field testing is sufficient for an initial assessment when:

1. **The concern is biological contamination only** (no agricultural or industrial chemical inputs near the source)
2. **You are screening for action vs. non-action** (treating vs. not treating), not for regulatory compliance
3. **You are monitoring a previously tested and known-safe source** for recurrence of previously identified contamination
4. **You need a result within hours**, not days

**Field testing is definitive for**:
- Confirming that treated water has adequate chlorine residual (test strip)
- Determining whether turbidity requires pre-filtration before disinfection
- Screening pH for corrosivity and disinfection efficiency
- Hardness screening for scale formation planning

**Field testing is a screening tool (not definitive) for**:
- Coliform/E. coli — positive results should be confirmed by lab
- Nitrate — near-threshold results should be confirmed by lab
- Iron and manganese — above secondary standards should be confirmed

### 7.2 When You Must Use a Certified Laboratory

You should stop field testing and seek a certified laboratory when:

1. **Any field test shows a result near or above a health-based threshold** — lab confirmation before taking major action (especially before deciding an alternative source is permanent)
2. **Your source is in an agricultural area** and has not been comprehensively tested for chemical contaminants in the past 3 years
3. **You are near an industrial site, military base, or airport** and have not tested for PFAS
4. **Your home was built before 1986** and you have not tested for lead (this is a plumbing issue, not a source water issue, but requires lab testing)
5. **You have a recurring coliform positive that returns after shock chlorination** — this indicates a structural problem requiring investigation
6. **Field test results conflict with each other** or with your visual/odor assessment
7. **You are establishing a new water source** for the first time
8. **A household member is immunocompromised, pregnant, or an infant** — stricter standards apply and field screening is insufficient

### 7.3 How to Find a Certified Laboratory Without Internet Access

In order of reliability:

1. **Call your county health department** — every US county has a health department that can provide a list of certified labs or offer free/subsidized well water testing. Look up the number in a phone book under "[County Name] Health Department" or call your local government main line and ask to be transferred.

2. **Call your state drinking water program** — every US state has a state drinking water program with contacts who can direct you to certified labs. Search your state name + "drinking water program" in a phone book or call state government information.

3. **Call your Cooperative Extension office** — the USDA Cooperative Extension system has offices in every US county. They routinely help rural residents with water testing and can provide contacts and sometimes subsidized testing kits.

4. **Call a local water or irrigation supply store** — these businesses often know local water testing labs and can direct you without internet access.

**What to tell the lab**:
- Your water source type (private well, cistern, surface water)
- Whether there has been a recent flooding event or known contamination event
- Whether the water has been shock chlorinated recently (affects bacterial test timing)
- The specific concern (bacteria, nitrate, pesticides, or comprehensive panel)
- Ask specifically for a "state-certified" analysis and confirm they follow EPA-approved methods

**Cost context**: A basic bacteria + nitrate panel typically costs $30–80. A comprehensive well water panel (bacteria, nitrate, pH, hardness, iron, metals, VOCs) typically runs $150–300. Some states offer free or discounted testing through health departments or extension programs — ask about this when you call.

### 7.4 Documentation — Recording Test Results for Household Monitoring

Every test result should be documented. This record enables you to detect trends (gradual deterioration over years), provides evidence if you later need to work with health authorities, and is required if you ever sell property with a well.

**Minimum documentation format** (can be handwritten):

```
Date: 
Time of collection: 
Source (describe specifically): 
Water source type: [well / surface / rainwater / cistern / other]
Recent events that may affect quality (flooding, drought, nearby construction, etc.):
Tests performed:
  - Test name/kit: _________ Result: _________ Units: _________
  - Test name/kit: _________ Result: _________ Units: _________
Visual observations (color, odor, turbidity estimate):
Person who collected sample:
Person who performed test:
Actions taken based on result:
Next scheduled test:
```

**If sharing with a community water monitoring network**, collect this data in a format compatible with what your local health authority uses. CSV format (comma-separated values) is the most widely accepted for sharing across systems. Include latitude/longitude if you have GPS access.

---

## Section 8: Case Study — Post-Flood Assessment Protocol

**Scenario**: A well owner in a river-bottom agricultural area receives 4 inches of rain over 36 hours. The well casing is above the flood line, but surface water approached within 10 feet of the wellhead. Some surface water may have infiltrated via cracks in the well cap.

**Step-by-step assessment sequence**:

**Day 0 (during or immediately after flooding)**:
1. Do not use the well water for drinking. Switch to bottled water immediately.
2. Visually inspect the wellhead: Check for obvious damage (cap knocked off, debris in casing, brown or silty water when pump runs).
3. Note the flood extent and how close surface water came to the wellhead.

**Day 1 (flood water receded)**:
1. Run the well pump for 15 minutes to flush any water that entered during the event.
2. Observe the water: color, odor, obvious turbidity.
3. **Do not test yet** — bacterial counts will be high immediately post-flood regardless and the results will not help you plan your response. The action regardless of result is shock chlorination.
4. Perform shock chlorination (see Domain 3 for the full procedure).

**Days 1–7 (post-shock-chlorination)**:
1. Do not use the well for drinking.
2. After 24 hours of chlorination, flush the well until the chlorine odor is no longer detectable from the tap.
3. Continue using bottled water.

**Day 7–10 (after chlorine has fully flushed)**:
1. Collect a water sample using the faucet procedure in Section 5.2.
2. Submit to a certified lab for: total coliform, E. coli, and nitrate.
3. Given the agricultural context, also request: pesticide/herbicide screen (if within 0.5 mile of row crops) and volatile organic compounds (if near any industrial or fuel storage sites).

**Days 10–14 (lab results return)**:
- If coliform/E. coli **absent** and nitrate **<10 mg/L**: Resume use. Schedule a follow-up test in 4 weeks to confirm recovery.
- If coliform/E. coli **present**: Do not resume use. A single positive result after shock chlorination suggests a structural problem (cracked casing, surface infiltration pathway). Contact a licensed well driller to inspect the physical condition of the casing and wellhead.
- If nitrate **>10 mg/L**: The flood may have delivered agricultural nitrogen. Do not resume use for infants or pregnant women. Send a second sample to lab to confirm result (post-flood nitrate can be temporarily elevated and may decrease after several weeks of normal operation).

---

## Section 9: DIY Testing Methods — Low-Cost Alternatives Without Commercial Kits

When commercial kits are unavailable, these improvised methods can detect obvious problems. They are not substitutes for validated tests and cannot confirm safety — they can only detect obvious contamination or rule out gross problems.

### 9.1 Hydrogen Sulfide (H2S) Presence/Absence — Improvised Method

H2S-producing bacteria are common fecal indicator organisms. A basic version of the H2S test can be approximated with local materials, though accuracy is significantly lower than commercial H2S vials.

**Materials**: Lead acetate test paper (if available from a chemistry supply) or improvised paper soaked in diluted lead acetate solution. This approach has limited practical value in a true field emergency — the H2S vial kits are inexpensive enough (~$10–20) that sourcing them is the better choice.

**Practical limitation**: The improvised H2S test detects only H2S-producing bacteria, not all coliforms. Many dangerous coliforms do not produce H2S and will not be detected. **False negatives are common.** This method should be treated as a rough screening tool only, with explicit documentation of its limitations.

### 9.2 pH Testing with Red Cabbage Juice

Red cabbage contains anthocyanin pigments that change color with pH. This method provides a rough indication of acidity/alkalinity but not a precise pH value.

**Procedure**:
1. Boil chopped red cabbage in water for 10 minutes. Strain out the cabbage. The liquid will be purple.
2. Let the liquid cool. It is now your indicator.
3. Add a small amount of your water sample (about 10 mL) to a small glass of the cabbage juice.
4. Observe the color:
   - Red/pink → strongly acidic (<pH 4)
   - Purple → neutral (pH 6–7)
   - Blue/green → alkaline (pH 8–9)
   - Yellow/greenish → strongly alkaline (>pH 10)

**Accuracy limitation**: This method can reliably distinguish strongly acidic from strongly alkaline water but cannot resolve the 6.5–8.5 range that matters for disinfection effectiveness. Color interpretation is subjective and varies with lighting. Do not use this as the basis for specific dosing decisions.

**For pH that matters for treatment decisions** (e.g., confirming water is in the range where chlorination is effective), use a commercial pH test strip. They cost $0.10–0.50 each and provide ±0.5 unit accuracy, which is adequate for treatment decisions. [Source: 13]

### 9.3 Settling Test for Turbidity

If no turbidity tube is available, settle and observe:
1. Fill a clear plastic bottle with your water sample.
2. Let it sit undisturbed on a flat surface for 1 hour.
3. Observe the water column and the bottom of the bottle.

| What You See | Interpretation |
|-------------|---------------|
| Water is still cloudy after 1 hour | Very fine colloidal turbidity; settling alone is insufficient pre-treatment |
| Visible sediment on bottom; water is clearer above | Coarse particle turbidity; settling improved clarity; pour clear upper portion carefully for further treatment |
| Water is clear throughout after 1 hour | Low turbidity from coarse particles; proceed with standard treatment |

---

## Section 10: Testing After Treatment — Confirming Disinfection Was Effective

After treating water, you should verify the treatment worked before consuming it.

**For boiled water**: No test is needed to confirm biological safety if a full rolling boil was maintained (see Domain 3 for time requirements). The test is observational — did the water reach a rolling boil?

**For chlorinated water**:
1. Use a free chlorine test strip after the full contact time (30 min at >15°C; 60 min at <15°C).
2. Target residual: 0.2–0.5 mg/L free chlorine.
3. If residual is 0: Re-treat. The water had too high a chlorine demand. Pre-filter, add another dose, and retest.
4. If residual is >1 mg/L: Water is safe but may taste strongly of chlorine. Allow to sit in an open container for 30–60 minutes to off-gas, or pour between two containers several times to aerate. Retest before drinking.

**For filtered water**:
- You cannot directly test whether filtration was effective in a field setting without specialized equipment.
- Confirm that turbidity decreased visually (turbidity tube before/after).
- For biological safety, combine filtration with a second treatment step (boiling or chlorination). See Domain 3 for multi-stage procedures.

**Chlorine residual without a test strip** — the smell test (limited accuracy):
If you have no test strip, smell the treated water after the contact period. You should be able to detect a faint chlorine smell. This is not a reliable quantitative measure but indicates that some residual chlorine is present. No chlorine smell = no residual = possible underdosing. [Source: 14]

---

## Sources

1. [WHO Guidelines for Drinking-Water Quality: Acceptability — Taste, Odour and Appearance (NCBI Bookshelf)](https://www.ncbi.nlm.nih.gov/books/NBK579463/) — Turbidity thresholds, color detection limits (15 TCU), odor detection thresholds for specific compounds. WHO GDWQ 4th Edition with 2022 addenda.

2. [Chlorination and Turbidity — Thompson-Nicola Regional District](https://www.tnrd.ca/services/water-sewage/chlorination-and-turbidity/) — Practical explanation of why turbidity above 5 NTU impairs chlorine effectiveness; source of the 5 NTU operational threshold.

3. [Post-Flood Drinking Water Safety for Private Water Systems — Penn State Extension](https://extension.psu.edu/post-flood-drinking-water-safety-for-private-water-systems) — Complete post-flood well assessment and shock chlorination procedure; parameters to test after flooding.

4. [Color Taste Odor and Aesthetic Nuisance Problems in Drinking Water — KnowYourH2O](https://www.knowyourh2o.com/indoor-6/color-taste-odor) — Interpretation of water color and odor by contaminant type; chemical smell as indicator of industrial contamination.

5. [Don't Waste Your Money With Outdated Test Methods — Weber Scientific (Colilert-18)](https://www.weberscientific.com/colilert-18) — Comparison of enzyme-based (Colilert) vs. membrane filtration for coliform false-positive rates; 3x lower false-positive rate for enzyme-based methods.

6. [The Turbidity Tube: Simple and Accurate Measurement of Turbidity in the Field — University of Hawaii, Exploring Our Fluid Earth](https://manoa.hawaii.edu/exploringourfluidearth/sites/default/files/pd-forum-attachments/Turbidity%20Tube.pdf) — Turbidity tube construction and use; correlation with NTU values; recommended for field use in low-resource settings.

7. [Nitrate and Nitrite in Private Drinking Water Wells — UMass Extension](https://www.umass.edu/agriculture-food-environment/cafe/fact-sheets/nitrate-nitrite-in-private-drinking-water-wells) — Sources of nitrate contamination; health effects; boiling as concentrator of nitrate (critical warning for infants).

8. [Nitrate in Drinking Water: Risks, Safe Levels & How to Test — Tap Score](https://mytapscore.com/blogs/tips-for-taps/nitrate-in-drinking-water) — Nitrate interpretation table; EPA MCL 10 mg/L; testing methodology comparison (strips vs. lab).

9. [Atrazine Contaminant of Drinking Water — KnowYourH2O](https://www.knowyourh2o.com/indoor-6/atrazine) — Atrazine behavior in groundwater; risk factors for well contamination; no field kit available.

10. [Glyphosate in Drinking Water: Health Concerns & Removal — WaterVerge](https://www.waterverge.com/contaminants/glyphosate/) — Glyphosate persistence; treatment options; field detection limitations.

11. [EPA Finalizes Drinking Water Standards for Six PFAS — Penn State Extension](https://extension.psu.edu/epa-finalizes-drinking-water-standards-for-six-pfas) — PFOA/PFOS MCL at 4 ppt; PFAS treatment limitations (boiling concentrates PFAS); risk zones.

12. [Guidelines for Testing Well Water — CDC](https://www.cdc.gov/drinking-water/safety/guidelines-for-testing-well-water.html) — Annual testing recommendation; events triggering additional testing; parameters for minimum annual panel; E. coli as extreme health hazard.

13. [How to Test the pH of Water Without a Kit — Biology Insights](https://biologyinsights.com/how-to-test-the-ph-of-water-without-a-kit/) — Red cabbage pH indicator procedure; accuracy limitations; comparison to commercial strips.

14. [Chemical Disinfection: Sodium Hypochlorite, Pool Shock, and Alternatives — Open-Repo Project](./WAVE_0_DOMAIN_3_CHEMICAL_DISINFECTION.md) — Free residual chlorine target (0.2–0.5 mg/L); smell test as residual indicator; contact time requirements.

15. [National Primary Drinking Water Regulations — US EPA](https://www.epa.gov/ground-water-and-drinking-water/national-primary-drinking-water-regulations) — MCLs for total coliform (5% positive threshold), E. coli (zero tolerance), nitrate (10 mg/L as N), turbidity (TT <1 NTU), PFOA/PFOS (4 ppt).

16. [Interpreting Coliform Bacteria Test Results — NRC Labs](https://nrclabs.com/interpreting/) — Health hazard classification by coliform/E. coli result combination; recommended actions; shock chlorination as first response.

17. [Coliform Bacteria as Indicators of Diarrheal Risk — PMC (Systematic Review and Meta-Analysis)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4175079/) — Evidence base for coliform as indicator organism; relationship between E. coli presence and other pathogen risk.

18. [Coliform Bacteria in Drinking Water Supplies — New York State DOH](https://www.health.ny.gov/environmental/water/drinking/coliform_bacteria.htm) — What E. coli presence does and does not prove; contamination pathway concept; potential associated pathogens.

19. [Where Can I Get My Well Water Tested? — USGS](https://www.usgs.gov/faqs/where-can-i-get-my-well-water-tested) — Finding certified labs; county health department as primary referral; cost guidance.

20. [Contact Information for Certification Programs — US EPA](https://www.epa.gov/dwlabcert/contact-information-certification-programs-and-certified-laboratories-drinking-water) — EPA directory of state-certified drinking water laboratory programs.

21. [How to Collect Well Water Sample Without Ruining Results — WellWaterWise](https://wellwaterwise.com/2026/03/30/how-to-collect-a-well-water-sample-without-ruining-your-results/) — Aerator removal; flushing procedure; common collection errors and solutions; hold time requirements.

22. [Groundwater Sample Collection and Analysis Procedures — Minnesota PCA](https://www.pca.state.mn.us/sites/default/files/c-prp4-05.pdf) — Formal sample collection procedures for groundwater; container requirements; preservation; chain of custody.

23. [Secchi Disk Measurements in Turbid Water — ResearchGate](https://www.researchgate.net/publication/340882255_Secchi_Disk_Measurements_in_Turbid_Water) — Correlation between Secchi disk depth and NTU; limitations above 40 NTU; field measurement alternatives.

24. [Effect of Turbidity on Water Disinfection by Chlorination — PubMed](https://pubmed.ncbi.nlm.nih.gov/30777799/) — Composition-dependent turbidity effects; 1 NTU threshold for humic acids; 5 NTU for mineral turbidity.

25. [Avoiding Glyphosate and Atrazine Runoff and Groundwater Contamination — UNL CropWatch](https://cropwatch.unl.edu/avoiding-glyphosate-and-atrazine-runoff-and-groundwater-contamination/) — Agrochemical transport pathways; soil type factors; proximity risk factors for wells.

26. [Using Inundation Extents to Predict Microbial Contamination in Private Wells After Flooding — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10976889/) — Flood depth and well contamination risk; testing sequence post-flood; seasonal coliform patterns.

27. [Coliform Bacteria — Penn State Extension](https://extension.psu.edu/coliform-bacteria) — Total coliform vs. E. coli distinction; shock chlorination procedure overview; follow-up testing timing.

28. [Protect Your Home's Water — EPA Private Wells](https://www.epa.gov/privatewells/protect-your-homes-water) — Well maintenance schedule; annual testing priority parameters; event-triggered testing list.

29. [Secondary Drinking Water Standards — KnowYourH2O](https://www.knowyourh2o.com/indoor-4/secondary-standards) — Iron, manganese, color, taste, odor secondary standards; aesthetic vs. health thresholds; color-to-contaminant interpretation table.

30. [Well Water Testing After Flooding — ETR Labs](https://etrlabs.com/why-you-should-test-your-well-water-after-flooding-or-heavy-rain/) — Post-flood testing sequence; parameters to include; timing of tests relative to shock chlorination.

---

*This document covers Domain 1 (Water Assessment & Testing) of the Water Systems Wave 0 series. Next steps: if your field assessment or test kit shows a problem, proceed to the relevant treatment guide. Domain 3 (Water Treatment & Purification) covers boiling, chemical disinfection, and filtration procedures.*

*See also: WAVE_0_DOMAIN_3_BOILING_AND_HEAT_TREATMENT.md | WAVE_0_DOMAIN_3_CHEMICAL_DISINFECTION.md | WAVE_0_DOMAIN_3_FILTRATION_AND_BIOSAND.md*
