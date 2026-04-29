---
title: ModRun Material Sourcing and Supplier Economics
date: 2026-04-29
status: active
tags: [3d-printing, mfg-farm, supply-chain, filament, petg, pla, cogs, modrun]
confidence: high
related: phase-2-supplier-research.md, multi-printer-architecture.md, pricing-strategy.md
---

# ModRun Material Sourcing and Supplier Economics

**Lead finding:** PLA+ is the correct production material for ModRun cable clips at launch and through at least 500 units/month. PETG is the right upgrade trigger at the Standard-tier premium SKU when customer willingness-to-pay for "premium material" is confirmed (expected Month 3–4). Material cost currently represents 13–18% of total COGS on a $12 unit, which means supplier optimization is the highest-leverage cost variable available — more impactful than electricity savings or depreciation reduction at this scale.

**Note on scope:** `phase-2-supplier-research.md` already provides comprehensive supplier profiles for eSUN, Anycubic, Polymaker, Overture, and SUNLU. This document does not repeat those profiles. It provides: (1) material selection analysis with property requirements, (2) a cost sensitivity matrix showing margin impact by material, (3) a worked COGS model at multiple volume tiers, (4) a bulk purchasing decision tree, and (5) a supplier evaluation framework for future supplier additions.

---

## 1. Material Selection: What the ModRun Use Case Actually Requires

### 1.1 Performance Requirements for Cable Clips

Cable management clips sit in a demanding but not extreme mechanical environment. The relevant stress profile:

- **Snap-fit installation stress**: The clip flexes 3–8mm during installation, then returns to shape. This is a one-time flexure event (installation), not cyclic fatigue. The material needs sufficient elongation-at-break to survive this without cracking.
- **Sustained tension on cables**: Once installed, the clip holds cables in mild compression. This is a low-load, continuous-duty condition (months to years).
- **Temperature exposure**: Desktop electronics in normal operation generate localized heat of 40–65°C at contact points. Server room or enthusiast-class hardware (GPUs under load, power bricks) can push cable-adjacent temperatures to 60–75°C.
- **UV and chemical exposure**: Indoor use only for most cable management. No UV resistance required for the core SKU. Chemical exposure is minimal (incidental contact with cleaning products only).

### 1.2 Material Comparison by Requirement

| Property | PLA Standard | PLA+ | PETG | ABS | Relevance to ModRun |
|---|---|---|---|---|---|
| Heat deflection temp | 50–55°C | 55–60°C | 70–75°C | 88–98°C | Critical — see 1.3 |
| Elongation at break | 3–6% | 5–8% | 50–200% | 2–5% | Important for snap-fit installation |
| Tensile strength | 50–65 MPa | 55–70 MPa | 48–53 MPa | 40–50 MPa | Moderate importance |
| Impact resistance | Low | Medium | High | Medium | Useful for durability claims |
| Print success rate | ~92–95% | ~92–95% | ~77–91% | ~75–85% | Directly affects COGS |
| Retail price (bulk) | $11–14/kg | $11–14/kg | $14–18/kg | $12–15/kg | See Section 2 |
| Post-processing ease | Excellent | Excellent | Good | Fair (fumes) | Shop environment factor |
| AMS compatibility | Excellent | Excellent | Good (brand-dependent) | Adequate | Relevant for Bambu P1S |

*Sources: Xometry PETG vs PLA comparison; 3DFilamentPrice PETG vs PLA analysis; Ultimaker material comparison; SigmaFilament guide 2026.*

### 1.3 The Heat Deflection Decision

PLA's glass transition temperature (50–55°C for standard, up to 60°C for PLA+) is the sharpest risk factor in the material selection. PLA begins to soften at temperatures well within range of:

- A PC tower chassis under full GPU load: 55–70°C at cable contact points
- A power brick sitting against a clip: 60–75°C surface temperature
- A car dashboard or window-mount application: 70–85°C

For under-desk cable management in a climate-controlled home office — the primary ModRun customer segment — typical cable temperatures are 35–50°C. PLA+ survives comfortably in this environment.

**The risk case that justifies a PETG SKU**: Any buyer installing ModRun clips near active electronics (server rack, gaming rig with aggressive GPU, enclosed PC cabinet) is in the 60–75°C zone where PLA+ begins to deform. PETG's 70–75°C deflection point provides the margin of safety. This is why the Standard-tier "PETG Premium" positioning in the pricing strategy is materially justified, not just a marketing claim.

**Practical decision rule for production:**
- Default production material: PLA+ (eSUN PLA+ or equivalent)
- Premium SKU trigger: PETG for any clip or rail sold into the Standard or Premium tier with explicit "heat-resistant" or "server room" positioning
- Do not use standard PLA for any production unit (the $0–2/kg cost difference vs. PLA+ is not worth the deformation risk at client-reported 60°C scenarios)

### 1.4 Why ABS and Resin Are Not the Answer

**ABS** has better heat resistance (88–98°C deflection) but lower elongation at break than PETG (2–5% vs. 50–200%), meaning clip snap-fits are more likely to crack on installation. ABS also requires an enclosure for reliable printing (warping from ambient temperature fluctuation) and releases styrene vapor — a shop safety and home operation concern. ABS's advantages in temperature resistance over PETG are not needed for this use case. Exclude from production consideration.

**Resin (MSLA/SLA)**: Produces higher-detail prints but is brittle (near-zero elongation at break). A cable clip in standard UV resin will fracture at the snap-fit point on first installation. Flexible resins exist but are expensive ($60–120/L) and not suitable for batch farm production economics. Exclude from production consideration.

---

## 2. Cost Sensitivity Matrix

### 2.1 Material Cost Per Unit at Different Volumes

Assuming a 75g print per standard ModRun clip (per COGS baseline in `phase-2-supplier-research.md`):

| Material | Bulk Price/kg | Cost/75g unit | vs. PLA+ Baseline | Delta at 500 units/mo | Delta at 7,000 units/mo |
|---|---|---|---|---|---|
| PLA Standard (commodity) | $10–12/kg | $0.75–$0.90 | −$0.15 to −$0.10 | −$75 to −$50/mo | −$1,050 to −$700/mo |
| **PLA+ (recommended)** | **$11–13/kg** | **$0.83–$0.98** | **baseline** | **—** | **—** |
| PETG (commodity) | $14–18/kg | $1.05–$1.35 | +$0.22 to +$0.37 | +$110 to +$185/mo | +$1,540 to +$2,590/mo |
| PETG (mid-premium, Overture) | $16–20/kg | $1.20–$1.50 | +$0.37 to +$0.52 | +$185 to +$260/mo | +$2,590 to +$3,640/mo |
| ABS (commodity) | $12–15/kg | $0.90–$1.13 | +$0.07 to +$0.15 | +$35 to +$75/mo | +$490 to +$1,050/mo |

**Reading this table**: Switching from PLA+ to commodity-tier PETG costs approximately $0.22–$0.37 more per unit in raw material. On the current pricing model, a PETG clip must command at least $0.25–$0.50 more in retail price to remain margin-neutral — achievable by positioning it as the "PETG Premium" SKU at $2–4 above the PLA+ equivalent. At 7,000 units/month, the cost gap is $1,540–$2,590/month; price-justified only if the premium SKU clears that in added revenue (which it does at volume if PETG units sell for $2+ more than PLA+ equivalents).

### 2.2 Material Cost as Percentage of COGS

Full COGS breakdown for one 75g PLA+ clip at production scale (from `multi-printer-architecture.md` baseline, extended):

| COGS Component | Low Est. | Mid Est. | High Est. | % of COGS (mid) |
|---|---|---|---|---|
| Material (filament at $12/kg, 75g) | $0.83 | $0.90 | $1.10 | **18.2%** |
| Electricity ($0.025/hr × 45 min) | $0.02 | $0.02 | $0.03 | 0.4% |
| Printer depreciation ($0.14/hr × 45 min) | $0.09 | $0.11 | $0.14 | 2.2% |
| Print failure waste (10% buffer) | $0.09 | $0.10 | $0.12 | 2.0% |
| Packaging (poly mailer, 1 unit) | $0.06 | $0.08 | $0.15 | 1.6% |
| Shipping (USPS Ground Advantage) | $3.50 | $4.50 | $5.50 | **91.1%** |
| **Total COGS (shipped single unit)** | **$4.59** | **$5.71** | **$7.04** | **100%** |

**Critical insight**: Shipping dwarfs material cost in single-unit order economics. Material is only 18% of COGS; shipping is 79% at mid-estimate. The actionable implication: margin optimization at early scale should focus on (a) increasing average order value (AOV) to amortize shipping across multiple units, and (b) Pirate Ship commercial rate discipline — not filament cost reduction. On a 3-unit order where shipping is $5.00 total instead of $3 × $4.50 = $13.50, the math flips dramatically.

**Per-unit COGS on a 3-clip bundle order at $28.99:**

| Component | 3-Unit Bundle | Per-Unit Equiv. |
|---|---|---|
| Material (3 × 75g @ $0.90) | $2.70 | $0.90 |
| Electricity + depreciation | $0.39 | $0.13 |
| Failure waste | $0.27 | $0.09 |
| Packaging (one poly mailer) | $0.08 | $0.03 |
| Shipping (single Ground Advantage) | $5.00 | $1.67 |
| **Total COGS** | **$8.44** | **$2.81** |
| Retail price | $28.99 | — |
| Net after Etsy 6.5% fees | $26.10 | — |
| **Gross margin** | **$17.66** | **60.9%** |

Bundling alone moves margin from ~54% (single unit) to ~61% (3-unit bundle) with no change in material cost or supplier. This reinforces why the bundle strategy in `pricing-strategy.md` is the highest-leverage margin improvement available.

### 2.3 Margin Impact of Bulk Material Purchasing

| Monthly Volume | Material at Retail ($18/kg) | Material at Bulk 10kg ($12/kg) | Material at Bulk 50kg ($10.49/kg) | Monthly Savings vs. Retail |
|---|---|---|---|---|
| 100 units (7.5 kg) | $135 | $90 | $78.68 | $45 to $56 |
| 500 units (37.5 kg) | $675 | $450 | $393 | $225 to $282 |
| 1,000 units (75 kg) | $1,350 | $900 | $787 | $450 to $563 |
| 3,000 units (225 kg) | $4,050 | $2,700 | $2,360 | $1,350 to $1,690 |
| 7,000 units (525 kg) | $9,450 | $6,300 | $5,507 | $3,150 to $3,943 |

**Takeaway**: At 100 units/month, the absolute dollar difference between retail and bulk purchasing is only $45–$56/month. The operational overhead of managing a bulk order relationship (lead time, storage, quality inspection) likely costs more than $45/month in operator time. Bulk purchasing becomes worth the management overhead around 500 units/month (~$225–$282/month saved), and becomes clearly material at 1,000+ units/month.

---

## 3. Bulk Purchasing Decision Tree

Use this to determine the right procurement strategy at each production phase.

### Trigger: Current Monthly Filament Consumption

**Under 10 kg/month (under ~130 units at 75g/unit):**
- Buy retail on Amazon. eSUN PLA+ single spools ($15–20/kg) or 10kg bundles ($11–13/kg) via Prime.
- No MOQ pressure, no storage overhead, no capital lock-in.
- Priority: Prove the product sells before optimizing cost.
- Action: Open a Pirate Ship account and buy 2–3 spools in your primary color.

**10–25 kg/month (130–330 units):**
- Commit to 10kg Amazon bundle orders. eSUN PLA+ 10kg bundle at $11–13/kg via Prime is the default.
- Maintain 1 case (10kg) of safety stock per primary color (black, white, grey).
- Reorder trigger: When any color drops below 5kg on hand.
- Do not move to direct wholesale yet — the volume doesn't justify the account setup friction.

**25–50 kg/month (330–660 units):**
- Place one Anycubic 50kg test order ($10.49/kg, no MOQ). This validates that supplier and the AMS compatibility on your specific hardware, and gets you familiar with the lead time.
- Continue eSUN 10kg bundles as the primary safety-stock source.
- Begin tracking by color: which colors are consuming the most? This data shapes the Polymaker wholesale color selection in the next phase.
- Storage requirement now matters: 50kg of PLA needs roughly 2–3 cubic feet of dry, climate-controlled storage. Invest in sealed storage bins + silica gel desiccant packs. Total equipment cost: $30–60.

**50–100 kg/month (660–1,320 units):**
- Open Polymaker wholesale account ($1,000 minimum, free shipping over $3,000). Place first order in your 2 highest-velocity colors.
- Use Anycubic 50kg deals for black (cheapest, highest volume) and eSUN bundles for remaining colors.
- Begin tracking cost per successful unit (not just cost per gram). At this volume, failed print waste is measurable in dollars per week.
- Negotiate with eSUN direct (esun3dstore.com) at this consumption level: $8.50–10/kg on a 40–60kg/month commitment is achievable.

**Over 100 kg/month (1,320+ units, 3+ printers):**
- Transition to Polymaker as primary white/grey supplier (quality consistency, vacuum packaging, AMS reliability).
- Anycubic as primary black supplier (lowest $/kg publicly available at pallet scale).
- eSUN as backup for emergency stock-outs (Prime shipping as safety net).
- Explore Push Plastic or IC3D as US-made option if tariff exposure on Chinese goods worsens.
- Negotiate net-30 terms with Polymaker after 2nd or 3rd order. This improves cash flow by $1,000–3,000/month at this volume.

### Storage Requirements by Volume Tier

| Monthly Consumption | Inventory Buffer Target | Storage Volume Needed | Key Storage Requirement |
|---|---|---|---|
| <10 kg/mo | 1–2 weeks (2.5–5 kg) | <0.5 cu ft | Sealed bin + desiccant |
| 10–25 kg/mo | 2 weeks (5–12 kg) | 0.5–1 cu ft | Dry box or sealed totes |
| 25–50 kg/mo | 3 weeks (18–38 kg) | 2–3 cu ft | Climate-controlled storage |
| 50–100 kg/mo | 4 weeks (50–100 kg) | 4–6 cu ft | Dedicated filament wall/rack |
| 100+ kg/mo | 4 weeks (100+ kg) | 8–12+ cu ft | Separate room or storage unit |

**Filament shelf life parameters**: PLA and PLA+ last 1–3 years under proper storage (15–25°C, under 30% RH). PETG lasts 2–4 years under same conditions. Moisture is the primary degradation vector — absorbed moisture causes diameter swelling, bubble artifacts during extrusion, and layer adhesion failures. At 50kg+ inventory levels, invest in a humidity-controlled dry cabinet ($80–200) or vacuum-seal bags + dedicated desiccant maintenance rotation.

---

## 4. Supplier Evaluation Framework

Use this framework when considering any new filament supplier — domestic or international. Score each criterion 1–5. A supplier scoring under 30 total should not be adopted as primary; under 20 should be excluded entirely.

### 4.1 Scoring Criteria

| Criterion | Weight | Score (1–5) | Notes |
|---|---|---|---|
| Price competitiveness at your current volume tier | 5x | — | Compare $/kg at your actual order size, not best-case |
| AMS/multi-material compatibility (Bambu P1S specific) | 5x | — | Community testing reports on Bambu forum, ADP Industries testing |
| Diameter tolerance consistency (target: ±0.02–0.03mm) | 4x | — | Published spec + community reports; request CoA |
| Lead time reliability (stated vs. actual) | 4x | — | Place a test order before relying on this supplier |
| Moisture packaging quality | 3x | — | Vacuum-sealed foil with desiccant = 5; plastic bag only = 1–2 |
| Minimum order flexibility | 3x | — | No MOQ or Amazon available = 5; $1,000 minimum = 3; $5,000+ = 1 |
| Color availability (black, white, grey priority) | 2x | — | Core 3 colors always in stock? |
| Payment terms | 2x | — | Net-30 available = 5; credit card only = 3 |
| Tariff/supply chain risk | 2x | — | US-made = 5; EU-made = 4; Chinese-made = 2 (current tariff environment) |
| Customer service responsiveness | 1x | — | Test with an email inquiry before committing |

**Maximum score: 155 points (5 × each weighted criterion)**

### 4.2 Current Supplier Scores (Estimated)

| Supplier | Price | AMS Compat. | Diameter | Lead Time | Packaging | MOQ Flex | Color | Payment | Tariff | Service | **Total** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| eSUN (Amazon) | 4×5=20 | 5×5=25 | 4×4=16 | 5×4=20 | 2×3=6 | 5×3=15 | 5×2=10 | 3×2=6 | 2×2=4 | 4×1=4 | **126** |
| Anycubic (direct) | 5×5=25 | 3×5=15 | 3×4=12 | 4×4=16 | 1×3=3 | 5×3=15 | 5×2=10 | 3×2=6 | 2×2=4 | 3×1=3 | **109** |
| Polymaker (wholesale) | 3×5=15 | 5×5=25 | 5×4=20 | 4×4=16 | 5×3=15 | 2×3=6 | 4×2=8 | 4×2=8 | 2×2=4 | 5×1=5 | **122** |
| Overture (Amazon) | 4×5=20 | 4×5=20 | 5×4=20 | 5×4=20 | 3×3=9 | 5×3=15 | 4×2=8 | 3×2=6 | 2×2=4 | 4×1=4 | **126** |
| Push Plastic (US-made) | 2×5=10 | 3×5=15 | 4×4=16 | 3×4=12 | 4×3=12 | 3×3=9 | 3×2=6 | 3×2=6 | 5×2=10 | 4×1=4 | **100** |

**Interpretation**: eSUN and Overture are tied at 126/155. Both are valid primary suppliers. Polymaker is close behind at 122/155 and becomes the quality-tier primary once volume justifies their MOQ. Anycubic at 109/155 is correctly positioned as a secondary/pallet-level hedge. Push Plastic at 100/155 is a viable domestic hedge against tariff escalation — not competitive on price today, but gap narrows if Chinese filament tariffs increase another 15–20%.

### 4.3 When to Add a New Supplier

Add a new supplier to the evaluation matrix when any of the following trigger conditions occur:

1. **Primary supplier stock-out lasting over 72 hours** on your highest-velocity color (signals the need for pre-qualified alternative)
2. **Tariff increase on Chinese goods of 10%+ in a single action** — reassess domestic suppliers (Push Plastic, IC3D, 3D-Fuel) and recalculate break-even against domestic premium
3. **Monthly filament spend exceeds $500** — at this level, a dedicated wholesale account negotiation is worth 4–8 hours of time investment
4. **New material introduction (PETG tier, flexible TPU)** — existing PLA suppliers may not have competitive PETG; evaluate Overture specifically for PETG (strongest community reliability data per `phase-2-supplier-research.md`)
5. **Quality-related failure rate exceeds 12%** on a single supplier's material — document batch numbers, photograph defects, contact supplier for replacement or credit, and simultaneously pre-qualify alternative

---

## 5. Sustainability Options and Price Premium Analysis

### 5.1 Bio-Based and Recycled Options

| Material | Supplier | Price Premium vs. Standard PLA | Customer Claim | Confidence |
|---|---|---|---|---|
| rPLA (recycled PLA) | 3D-Fuel (US-made) | +$3–5/kg (~20–35%) | "Made from recycled material" | High — 3D-Fuel publishes recycled content certificates |
| Bio-PETG | Fillamentum (EU) | +$8–15/kg (~40–75%) | "Plant-based PETG" | High |
| Eco-PLA (compostable) | Colorfabb, eSUN Eco | +$4–8/kg (~25–50%) | "Compostable" (industrial composting only) | Medium — home composting is unlikely; verify claim scope |
| Standard PLA (inherently bio-based) | eSUN, Anycubic, Polymaker | baseline | "Plant-based plastic, not petroleum" | High — this is already true of all PLA |

**Important clarification**: Standard PLA is already bio-based (derived from corn starch or sugarcane) and is not petroleum-derived like ABS or PETG. This is a factual marketing claim available at no cost premium when using any standard PLA supplier. The claim "plant-based material, not petroleum plastic" is legitimately applicable to the base product.

**When to pay the sustainability premium**: EcoEnclose packaging (noted in `phase-2-supplier-research.md`) is the higher-ROI sustainability investment over eco-filament, because packaging is visible to the customer whereas the filament is not. Spend the eco-premium on packaging first, filament second.

---

## 6. Scaling Material Consumption Curves

### 6.1 Printer Fleet vs. Monthly Filament Consumption

From `multi-printer-architecture.md`: A Bambu P1S running 16 hours/day at 45 minutes/clip produces approximately 21 clips/day, 640 clips/month. At 75g/clip:

| Printer Count | Monthly Units (16hr/day) | Monthly Filament (75g/unit) | At $12/kg Material Cost |
|---|---|---|---|
| 1 printer | ~600–640 units | ~45–48 kg | ~$540–$576 |
| 2 printers | ~1,200–1,280 units | ~90–96 kg | ~$1,080–$1,152 |
| 3 printers | ~1,800–1,920 units | ~135–144 kg | ~$1,620–$1,728 |
| 5 printers | ~3,000–3,200 units | ~225–240 kg | ~$2,700–$2,880 |

**Supplier transition triggers by printer count:**
- 1 printer: eSUN 10kg Amazon bundles, Prime-shipped, no wholesale
- 2 printers: Add Anycubic 50kg deal for primary black; eSUN remains for white/grey
- 3 printers: Open Polymaker wholesale; negotiate eSUN direct pricing; monthly spend justifies account management
- 5 printers: Blended supplier strategy mandatory; $2,700–$2,880/month material budget makes $/kg optimization worth dedicated time

### 6.2 When Supplier Change or Negotiation Makes Sense

The decision to actively negotiate (rather than buy at listed rates) is a function of time investment vs. savings:

Assume: Supplier negotiation/account setup = 4–8 hours of operator time. Value of operator time = $50/hour (opportunity cost).
Cost of negotiation: $200–$400 in time.
Required monthly savings to break even in 6 months: ~$33–$67/month.

At $12/kg blended, a 10% price improvement saves $1.20/kg. To save $67/month, you need to be purchasing 56 kg/month (~$670 in filament). This corresponds to roughly 750 units/month, achievable around Month 4–6 of production at a single printer running near-full utilization.

**Negotiation activation threshold: 750+ units/month or $600+/month in filament spend.**

---

## 7. Confidence Notes and Gaps

**High confidence** (live data, April 2026):
- eSUN 10kg bundle pricing ($11–13/kg, Amazon Prime)
- Anycubic 50kg deal pricing ($524.73 / 50kg = $10.49/kg, verified on store)
- PETG vs PLA heat deflection temperature thresholds (material science, well-established)
- Print success rate differential: PLA ~92–95%, PETG ~77–91% (from 3DFilamentPrice production testing)
- USPS 8% temporary rate increase effective April 26, 2026 through January 17, 2027

**Medium confidence** (corroborated but not directly quoted):
- Polymaker wholesale PolyLite PLA pricing (~$14.99/kg) — public landing page listing, logged-in account required for full catalog
- Material cost as ~18% of single-unit COGS — derived from the documented COGS model in `multi-printer-architecture.md`; correct under stated assumptions
- PETG real cost per successful print ~$0.58 vs. PLA ~$0.42 (from 3DFilamentPrice methodology; sample size not disclosed)

**Gaps requiring direct verification:**
- Push Plastic US-domestic pricing at 25kg+ volumes (website lists 10kg subscriptions but bulk quote requires direct contact)
- IC3D bulk PETG pricing (listed on website but requires quote for print farm quantities)
- Overture direct wholesale tier pricing (requires contact with overture3d.com wholesale team)
- PETG AMS compatibility testing on ModRun's specific print profile — the Overture PETG community positive reports are for Bambu printers generally; need one test spool on the actual ModRun clip file to confirm

---

## Sources

- [Xometry: PETG vs. PLA Strength and Printing Comparison](https://www.xometry.com/resources/3d-printing/petg-vs-pla-3d-printing/)
- [Ultimaker: PETG vs PLA vs ABS Strength Comparison](https://ultimaker.com/learn/petg-vs-pla-vs-abs-3d-printing-strength-comparison/)
- [3DFilamentPrice: PETG vs PLA — Ultimate 2026 Cost and Performance Comparison](https://www.3dfilamentprice.com/blog/pla-vs-petg)
- [SigmaFilament: Professional's Guide to PETG Filament 2026](https://sigmafilament.com/petg-filament-professional-guide/)
- [SigmaFilament: 3D Print Cost Estimator Guide 2026](https://sigmafilament.com/3d-print-cost-estimator-guide/)
- [3DPUT: Best PETG 3D Printing Settings Guide 2026](https://3dput.com/petg-3d-printing-settings-guide-temperature-speed-cooling-2026/)
- [SpoolPrices: Filament Price Comparison 2026](https://spoolprices.com/filament)
- [LayerMath: Filament Cost Per Gram 2026](https://layermath.com/blog/filament-cost-per-gram)
- [eufymake: 3D Printing Costs 2026](https://www.eufymake.com/blogs/buying-guides/how-much-do-3d-prints-cost)
- [Prusa Blog: How to Calculate 3D Printing Costs](https://blog.prusa3d.com/how-to-calculate-printing-costs_38650/)
- [3D Solved: Is PLA heat resistant? ABS, ASA, PETG comparison](https://3dsolved.com/is-pla-heat-resistant-abs-asa-petg-and-more/)
- [Siraya Tech: How Long Does Filament Last — Shelf Life Guide](https://siraya.tech/blogs/news/how-long-does-filament-last)
- [Ultimaker: 3D Printer Filament Storage Tips](https://ultimaker.com/learn/3d-printer-filament-storage-essential-tips-and-ideas/)
- [3DPrinterly: Filament Storage and Humidity Guide](https://3dprinterly.com/easy-guide-to-3d-printer-filament-storage-humidity-pla-abs-more/)
- [3D-Fuel: Wholesale 3D Printer Filament (US-Made)](https://www.3dfuel.com/pages/wholesale-3d-printer-filament)
- [Push Plastic: US-Made Filament and 10kg Subscriptions](https://www.pushplastic.com/)
- [IC3D: Bulk 3D Printing Filament](https://www.ic3dprinters.com/bulk-3d-printing-filament/)
- [Overture: PLA vs PETG Comparison Guide](https://overture3d.com/blogs/overture-blogs/pla-vs-petg-comparison)
- [Polymaker US Wholesale](https://us-wholesale.polymaker.com/)
- [Anycubic 50–100kg Bulk PLA Deals](https://store.anycubic.com/products/pla-basic-50-100kg-deals)
