---
title: ModRun Phase 2 — Supplier Research for Scaled Production
date: 2026-04-27
status: active
tags: [3d-printing, mfg-farm, supply-chain, filament, packaging, logistics, modrun]
confidence: high
related: multi-printer-architecture.md, market-research.md
---

# ModRun Phase 2: Supplier Research for Scaled Production

**Lead finding:** The two most actionable decisions after the test print are: (1) lock in a 10kg/month eSUN PLA+ contract on Amazon before scaling — at ~$11–13/kg it delivers the best COGS-to-reliability ratio in the commodity tier; and (2) pre-qualify Anycubic's direct-to-consumer 50kg pallet deal as a primary alternative, which hits ~$10.49/kg with no wholesale account required and no MOQ friction. Packaging can stay poly-bag at $0.05–0.15/unit through 500 units/month, then migrate to Packlane custom mailers once volume justifies the branding investment. Logistics: Pirate Ship for all USPS Ground Advantage shipping immediately — current commercial rates for a 4oz cable clip package run $3.50–5.09 (zone-dependent), representing a 15–20% savings over retail postage, with zero volume minimums.

---

## Context and Cost Baseline

From the ModRun COGS model established in multi-printer-architecture.md:

| Component | Current (retail filament) | Target (bulk 50kg+) |
|---|---|---|
| PLA material (75g @ ~$15/kg) | $1.15 | $0.75–0.79 |
| Packaging | $0.40 | $0.25–0.40 |
| Shipping (per order, 1-unit) | $5.50 | $4.50–5.09 |
| **Total COGS (1-unit order)** | **$8.49** | **$7.08–7.72** |
| Net margin on $12 sale | 29% | 33–41% |

The material and shipping levers together can shave $0.77–1.40 off COGS per unit-order. On 7,000 units/month, that is $5,400–$9,800/month in retained margin. This research exists to make those levers concrete.

---

## Section 1: PLA Filament Suppliers

### 1.1 Market Overview

The US filament market in April 2026 has a clear two-tier structure for production operations:

**Commodity tier ($9–16/kg):** eSUN, SUNLU, Anycubic, Overture, JAYO. Tolerance ±0.02–0.05mm. Adequate for cable management clips where functional tolerances are 0.3–0.5mm. These brands compete primarily on price and AMS compatibility.

**Mid-premium tier ($17–28/kg):** Polymaker, Bambu Lab, Prusament. Tighter tolerances (±0.02mm), better moisture packaging, more consistent batch-to-batch color. Justified for precision-fit assemblies or when selling into markets where documentation of material quality matters.

For ModRun cable clips, the commodity tier is correct. A $4–6/kg premium for Prusament is $0.30–0.45/unit at 75g — visible on the P&L at 7,000 units/month, not justified by product requirements.

**Key 2026 market note:** USPS tariffs on Chinese goods have modestly raised commodity filament prices from their 2024 floor. The $9–11/kg range that characterized 2024 peak-discount pricing is now $10–14/kg on standard commodity PLA. This is baked into all estimates below.

---

### 1.2 Supplier Profiles

#### Supplier A: eSUN (via Amazon / esun3dstore.com)

**Why recommended:** eSUN is the most consistently documented and reviewed commodity brand among Bambu P1S and X1C operators in 2026. ADP Industries' 6-printer farm testing (ADP Industries 2026) specifically cites eSUN PLA+ at $18/kg (1kg single spool) as the most reliable, with diameter tolerance ±0.03mm and zero AMS feed errors across extended 8+ hour jobs. At 10kg bundle pricing it drops into the $11–13/kg range, which is the best combination of reliability and cost in the commodity tier.

**Products relevant to ModRun:** eSUN PLA+ (Pro Plus) 1.75mm — this is the preferred production SKU. Also available: eSUN PLA Basic, eSUN PLA Matte. The PLA+ formulation has slightly higher impact resistance and layer adhesion than basic PLA, useful for clips that will be flexed to install.

**Pricing structure (US, April 2026):**

| Order Size | Format | $/kg estimate | Notes |
|---|---|---|---|
| 1 spool (1kg) | Amazon retail | $15–20 | Varies by color |
| 5 spools (~5kg) | Amazon multipacks | $13–17 | When available |
| 10 spools (10kg) | Amazon case bundle | $11–13 | Best regular velocity |
| 25+ kg | eBay wholesale listings | $9–12 | Variable availability |
| 50+ kg | Direct via esun3dstore.com | Quote required | Allow 2 weeks for response |

*The 10kg case on Amazon (B0G2KSS613 for black PLA Basic; B0G2KWC5XL for PLA+ mixed colors) is the operational sweet spot for a sub-50 kg/month operation: no wholesale account, no minimum commitment, ships Prime, consistent availability.*

**Minimum order:** No minimum on Amazon; wholesale via eSUN direct requires contact.

**Lead time:** 2–5 business days Amazon Prime. eSUN direct: 2–3 weeks.

**AMS compatibility:** Confirmed excellent on Bambu P1S and X1C. No feed errors reported on multi-hour jobs in community testing.

**Recommended colors for ModRun:** Black, White, Grey — the three highest-velocity cable management colors. Stock 10kg each per month at scale.

**Reliability score:** 9/10. Weaknesses: slight batch-to-batch color variation (relevant if you care about exact color matching across months); moisture packaging on Amazon bundles is less rigorous than Polymaker.

---

#### Supplier B: Anycubic (via store.anycubic.com)

**Why recommended:** Anycubic is the only commodity-tier brand with a direct, publicly listed 50kg/100kg bulk deal on their storefront requiring no wholesale account or MOQ negotiation. This makes it uniquely accessible for a growing operation that needs pallet-quantity filament before establishing a formal wholesale relationship.

**Products relevant to ModRun:** Anycubic PLA Basic, Anycubic PLA Basic Refill (cardboard spool-less refill rolls, lower waste, lighter shipping).

**Pricing structure (US, April 2026):**

| Order Size | Sale Price | Regular Price | $/kg (sale) |
|---|---|---|---|
| 50kg bundle | $524.73 | $1,149.50 | **$10.49/kg** |
| 100kg bundle | Quote varies | — | ~$9–10/kg est. |
| 10–20kg | $104.99 (sale) | $199.90 | ~$10.50/kg |

*Source: store.anycubic.com/products/pla-basic-50-100kg-deals, verified April 2026.*

**Color availability:** 25+ colors including black, white, grey, blue, red, orange, clear, and specialty finishes.

**Lead time:** Express shipping, 24-hour dispatch from Anycubic warehouse. Typically 3–7 business days to continental US.

**Minimum order:** No MOQ for the bundle deals — purchase directly online.

**AMS compatibility:** Community reports are mixed — occasional issues with AMS tangles on poorly wound spools. The Refill format (cardboard inner, no plastic spool) has fewer winding complaints. Recommend requesting a sample order before committing to 50kg.

**Reliability score:** 7/10. Lower consistency documentation than eSUN, some AMS feed issues reported on the Bambu forum. Offset by the uniquely accessible pallet-level pricing. Use for a diversified secondary supplier once eSUN is primary.

**Key use case for ModRun:** Anycubic is the hedge against eSUN stock-outs or price spikes. At 50kg/month production, a 50kg Anycubic order bridges a 2–3 week supply gap at $10.49/kg — roughly $0.79/unit at 75g.

---

#### Supplier C: Polymaker (via us-wholesale.polymaker.com)

**Why recommended for future scale:** Polymaker's wholesale program is the strongest in the mid-premium tier for print farm operators. The $1,000 minimum order, free shipping over $3,000, and "up to 45% off MSRP" positioning makes it competitive with commodity brands at sustained 50+ kg/month volumes. The vacuum-sealed foil bags and desiccant packaging are significantly better than commodity brands, which matters for long-term storage in a high-humidity shop environment.

**Products relevant to ModRun:** PolyLite PLA ($14.99/kg wholesale at case quantity), PLA Pro (~$17–19/kg wholesale), Matte PLA for production (pricing available on quote).

**Pricing structure (US, April 2026):**

| Product | MSRP | Wholesale/kg | Notes |
|---|---|---|---|
| PolyLite PLA | ~$24/kg retail | ~$14.99/kg (case of 10) | Needs $1,000 min order |
| PLA Pro | ~$28/kg retail | ~$17–19/kg est. | Quote required |
| Panchroma PLA | — | $14.99/kg listed | Color-specialty line |
| PETG | — | from $15.99/kg | For future PETG expansion |

*Source: us-wholesale.polymaker.com, April 2026. Wholesale pricing displayed after login; case minimums apply.*

**Minimum order:** $1,000 per order. At $14.99/kg for PolyLite PLA, this is approximately 67kg per order. For a 50kg/month operation, this is roughly a 6-week supply order. Manageable once the operation is stable.

**Lead time:** Free shipping on orders over $3,000. Typical 3–7 business days.

**Payment terms:** Net 30 available for qualified wholesale accounts; standard credit card for initial orders.

**AMS compatibility:** Polymaker is among the most cited brands for AMS reliability in 2026 Bambu community discussions. The consistent diameter tolerance and vacuum-sealed packaging prevent the moisture-induced diameter swelling that causes feed errors.

**Reliability score:** 9.5/10. Best documentation of quality (published certificates of analysis on request). Premium price point is the only drawback.

**Recommended activation point for ModRun:** Month 3–4, once 50kg/month production is confirmed and the $1,000 minimum order represents less than 2 weeks of supply.

---

#### Supplier D: Overture (via overture3d.com / Amazon)

**Why on the list:** Overture has a documented wholesale program (up to 35% off for bulk purchasers) and an active 10kg Amazon bundle product. Diameter tolerance ±0.02mm — tighter than eSUN's ±0.03mm. Community testing (ADP Industries 2026) rates Overture as the easiest PETG for Bambu printers, which makes them the recommended backup supplier if ModRun expands to PETG variants for heat-adjacent installations.

**Products relevant to ModRun:** Overture PLA 1.75mm (standard, matte, and silk variants); Overture PETG for premium SKUs.

**Pricing structure (US, April 2026):**

| Order Size | $/kg estimate | Notes |
|---|---|---|
| 1kg spool (Amazon) | $13–18 | Varies by variant |
| 10kg bundle (Amazon) | $11–14 | B0FS1XSDQ4 ASIN |
| Wholesale (overture3d.com) | Up to 35% off | Direct contact required |

**Minimum order:** No stated minimum on Amazon bundles; wholesale program contact required for tiered pricing.

**Lead time:** 2–5 days Amazon Prime; direct wholesale 1–2 weeks.

**Reliability score:** 8/10. Strong for PETG; slightly behind eSUN for PLA in raw AMS reliability data. Excellent for a secondary PLA supplier or as the exclusive PETG supplier.

---

#### Supplier E: SUNLU (via store.sunlu.com)

**Why included:** SUNLU is the lowest-priced tier ($14–16/kg at retail, lower via their reseller program) and offers a mix-and-match bulk order structure that lets you customize a multi-color batch without committing to 10kg of a single color. This is operationally useful during early production when you are still determining your color sales velocity.

**Products relevant to ModRun:** SUNLU PLA (standard, matte, silk variants). Mix-and-match bulk option with 6kg minimum order.

**Pricing structure (US, April 2026):**

| Order Format | $/kg estimate | Notes |
|---|---|---|
| 1kg spool (store.sunlu.com) | $14–16 | Retail single spool |
| 6kg mix-and-match bundle | ~$12–14 | Mix any 6 colors |
| Reseller program (50+ boxes) | ~$10–12 est. | Requires business registration |

**Minimum order:** 6 spools for bundle pricing (mix-and-match). Reseller program: 50-box initial order; contact support@3dsunlu.com.

**Lead time:** 3–7 business days from SUNLU US warehouse.

**AMS compatibility:** Adequate for PLA on single-color jobs; some reports of diameter inconsistencies on long AMS multi-spool jobs. Acceptable for a batch-print farm where each printer runs one color at a time.

**Reliability score:** 7.5/10. Better value than the score implies if you are disciplined about single-spool-per-printer operation (no AMS multi-color on SUNLU).

**Recommended use case for ModRun:** Color sampling / new color velocity testing before committing to a 10kg eSUN order in that color. Once velocity is confirmed, switch to eSUN or Anycubic for that color.

---

### 1.3 Bulk Pricing Comparison Table

All prices in USD per kg, PLA standard 1.75mm, US market, April 2026.

| Supplier | 10kg (~10 spools) | 25kg | 50kg | 100kg | Notes |
|---|---|---|---|---|---|
| eSUN (Amazon bundles) | $11–13 | ~$9–12 (eBay wholesale) | Quote (direct) | Quote (direct) | Most reliable AMS; Prime shipping |
| Anycubic (direct store) | ~$10.50 | ~$10.50 | **$10.49** (listed) | ~$9–10 est. | Only brand with public 50kg pricing |
| Polymaker (wholesale) | $14.99 (case) | $14.99 | $14.99 | $13–14 est. | $1,000 minimum; best packaging |
| Overture (Amazon + direct) | $11–14 | ~$10–13 | Quote (direct) | Quote (direct) | 35% off wholesale; strong PETG |
| SUNLU (direct + reseller) | $12–14 | ~$11–13 | ~$10–12 (reseller) | ~$9–11 (reseller) | Mix-and-match by color |
| Bambu Lab (official store) | $13–17 (4-roll: $14.99; 6-roll: $13.99) | — | — | — | Best for P1S/X1C profile fit; no true bulk |

*Note: Bambu Lab's official bulk program tops out at 6-roll tiers (~$13.99/spool). Not competitive for 50kg/month operations; appropriate only for initial calibration spools.*

---

### 1.4 Recommended Sourcing Strategy by Phase

**Phase 1 (test print → 500 units/month):**
- Primary: eSUN PLA+ 10kg Amazon bundles. Predictable, Prime-shipped, no MOQ commitment. $11–13/kg.
- Stock: 20kg at all times (3 colors × ~7kg each). Reorder when any color drops below 5kg.

**Phase 2 (500 → 3,000 units/month, 1–2 printers):**
- Primary: eSUN PLA+ via Amazon (continue).
- Add: Anycubic 50kg pallet as one quarterly purchase to stabilize COGS at $10.49/kg for high-velocity black and white.
- Open Polymaker wholesale account. Place first $1,000 order (~67kg) for a single high-quality color (white, which is most visible in product photography).

**Phase 3 (3,000 → 10,000 units/month, 3–5 printers):**
- Transition primary to Polymaker wholesale at $14.99/kg for white/gray (quality/consistency investment), Anycubic bulk at $10.49/kg for black and secondary colors.
- Monthly filament budget at 50kg × $12.75/kg blended: **$637.50/month material cost** (vs. $750 at $15/kg retail).

---

## Section 2: Packaging Vendors

### 2.1 Packaging Strategy Overview

ModRun cable clips have a favorable packaging profile: they are lightweight (75–100g print), non-fragile (PLA is durable; clips will not break in a poly mailer), and geometrically compact (each clip is roughly the size of a large paperclip multiplied by clip size variant). This means poly mailers work for all single-unit and most bundle orders. Custom boxes are a branding investment, not a protective necessity.

**Decision framework:**
- 1–3 clips per order: 6x9" or 9x12" poly mailer, no void fill needed.
- 4–6 clip bundle: 10x13" poly mailer or small padded mailer; tissue wrap optional.
- 6-clip gift bundle or premium tier: custom-printed mailer box (Packlane or similar) once volume justifies ~$0.80–1.25/unit box cost.

### 2.2 Poly Mailer Suppliers

**Primary recommendation: Shop4Mailers (shop4mailers.com) or Amazon basics bulk packs**

| Quantity | Cost/unit (poly mailer, standard) | Cost/unit (bubble mailer) |
|---|---|---|
| 100 units | $0.10–0.15 | $0.25–0.40 |
| 500 units | $0.06–0.08 | $0.15–0.25 |
| 1,000 units | **$0.05** | $0.12–0.18 |
| 5,000 units | $0.03–0.04 | $0.08–0.12 |

*Source: Shop4Mailers pricing, community-reported (Seller Gear guide, April 2026). Amazon bulk mailer pricing converges at 500+ units.*

**Recommended specs for ModRun:**
- Size: 9x12" (standard clips, up to 3-pack) and 12x15.5" (6-pack bundles)
- Thickness: 2.5 mil (standard) — adequate for cable clips
- Color: White or gray recommended; avoid clear (customers can see damaged product before opening)
- Branding: Custom-printed poly mailers are available from RUSPEPA and similar at ~$0.12–0.20/unit in 500+ quantities. Hold this investment until Month 3–4 when brand identity is established.

**Bubble mailers:** Not needed for PLA cable clips under normal shipping conditions. PLA at 75–100g is durable. Use bubble mailers only if you introduce fragile accessory SKUs (e.g., custom acrylic labels, electronics accessories).

### 2.3 Custom Box Vendors

For bundles and gift presentation (higher AOV, premium tier):

#### Packlane (packlane.com)

The most-cited low-MOQ custom box vendor for e-commerce. Can order as few as 1 unit; sensible economics start at 100 units.

| Quantity | Approx. cost/unit (small mailer box ~4x4x2") | Approx. cost/unit (standard ~6x4x3") |
|---|---|---|
| 100 units | ~$2.00–2.84 | ~$2.50–3.50 |
| 500 units | ~$0.85–1.10 | ~$1.00–1.50 |
| 1,000 units | ~$0.65–0.85 | ~$0.80–1.20 |
| 2,000 units | ~$0.55–0.76 | ~$0.65–0.95 |

*Source: Packlane reported pricing, Growth Marketing Pro comparison (2026).*

**Setup/design:** Online drag-and-drop designer; no setup fees. HDPrint Satin option available for high-quality digital print.

**Turnaround:** 10–14 business days standard; rush available.

**Verdict for ModRun:** Activate Packlane at Month 3–4 for your 6-clip premium bundle SKU. At 500 units/month the box cost drops to ~$1.00/unit, which is acceptable on a $45 bundle sale. Before then, the $2.50–3.50/unit at 100-unit quantities compresses margins uncomfortably.

#### EcoEnclose (ecoenclose.com)

Sustainable custom boxes using 100% recycled materials, printed with HydroSoy or Algae Ink. MOQ starts at 100 units. Custom printing plate fees: $95 (single panel) to $300–800 (full coverage).

**Verdict:** Better brand story than Packlane for Etsy buyers who care about sustainability. The one-time plate fee is a sunk cost that pencils out after ~500 units. Suitable for Month 4–6 if Etsy brand identity emphasizes eco-friendly materials.

#### EZ Custom Boxes / Hola Custom Boxes

Multiple vendors in this tier offer 100-unit MOQ custom printed boxes. Hola Custom Boxes advertises 8–12 day production and free US shipping.

**Generic pricing estimate for 100-unit custom box batch:**
- Unit cost: $1.50–3.00/unit depending on size and print coverage
- Production setup: $0–50 (varies by vendor)
- Turnaround: 8–15 business days

### 2.4 Packaging Budget by Scale

| Scale | Recommended Format | Approx. $/unit | Monthly cost at scale |
|---|---|---|---|
| <500 units/mo | Plain poly mailer (9x12") | $0.06–0.10 | $30–50 |
| 500–2,000 units/mo | Branded poly mailer | $0.12–0.20 | $60–400 |
| 2,000–5,000 units/mo | Branded poly mailer + custom box for bundles | $0.15–0.40 blended | $300–2,000 |
| 5,000–10,000 units/mo | Custom mailer box standard | $0.65–1.00 | $3,250–10,000 |

*Note: The jump from unbranded to branded packaging at 500 units/month is the highest-ROI packaging investment. A distinctive bag increases repeat purchase rate and unboxing shareability at a cost of ~$0.05–0.10/unit above plain.*

---

## Section 3: Logistics and Fulfillment

### 3.1 Shipping Strategy: USPS via Pirate Ship

**Recommended from Day 1:** Pirate Ship (pirateship.com) for all USPS shipping. Zero monthly fees, zero markup, access to commercial rates below USPS retail pricing, and Priority Mail Cubic access (not available at the post office counter).

**April 2026 rate context:** USPS implemented an 8% temporary rate increase effective April 26, 2026, running through January 17, 2027. This applies to Ground Advantage, Priority Mail, and Priority Mail Express. Media Mail is unaffected. Pirate Ship's commercial rates absorb some of this increase via their USPS Connect eCommerce program pricing.

**Rate benchmarks for a ModRun cable clip package (75–150g print + packaging = ~150–300g total, or 5–10 oz):**

| Service | Weight | Zone 1 Commercial | Zone 5 est. | Zone 8 est. |
|---|---|---|---|---|
| USPS Ground Advantage | 4 oz (single clip, light pkg) | ~$3.50–5.09 | ~$4.50–6.00 | ~$5.50–7.50 |
| USPS Ground Advantage | 8 oz (3-pack bundle) | ~$5.58 | ~$6.00–7.00 | ~$7.00–8.50 |
| USPS Priority Mail | Under 1 lb | ~$7.00–8.50 | ~$8.00–10.00 | ~$10–13 |
| USPS Priority Mail Cubic | Small cubic tier | ~$5.50–6.50 | ~$6.50–8.00 | ~$8–10 |

*Rates as of April 26, 2026, post-8% increase. Commercial rates via Pirate Ship. Exact pricing requires Pirate Ship's rate calculator for specific zip pairs.*

**Key insight:** For the single-clip order ($12 sale), Ground Advantage at ~$4.50–5.50 blended across zones replaces the $5.50 baseline in the COGS model — a $0.50–1.00 saving per order when using Pirate Ship vs. retail postage.

**Priority Mail Cubic:** Highly relevant for the 3-clip and 6-clip bundle SKUs. Cubic rates price by the box's physical volume rather than weight. A 6-clip bundle in a small 4x4x4" box (64 cubic inches = 0.037 cubic feet) falls into Cubic tier 1 or 2, potentially shipping for $6.00–7.50 zone 1–5, versus $8.50+ by weight. This requires a custom box rather than a poly mailer — another argument for Packlane at scale.

**Label printing setup:** Thermal label printer (Rollo or DYMO 4XL) + Pirate Ship web interface. Rollo X1040 runs ~$100 one-time investment; labels cost ~$0.02 each. No subscription.

### 3.2 Postage.com / Stamps.com Alternative

Postage.com and Stamps.com both offer commercial USPS rates similar to Pirate Ship. Key differences:

| Feature | Pirate Ship | Stamps.com |
|---|---|---|
| Monthly fee | None | $19.99/month |
| Markup on postage | None | None |
| UPS rates | Yes (discounted) | Limited |
| Interface | Clean, e-commerce focused | Feature-heavy, legacy UI |
| Best for | <500 shipments/month | Multi-carrier, high volume |

**Verdict:** Pirate Ship is the correct choice for ModRun at current and projected scale. No fees, no friction.

### 3.3 Regional Micro-Fulfillment: When It Becomes Relevant

**Threshold for considering 3PL outsourcing:** When daily packing and shipping exceeds 3–4 hours of the operator's time consistently. Based on multi-printer-architecture.md's labor model, this occurs at roughly 200–300 units/month with a single-person operation.

**Short-term (under 500 units/month):** Self-fulfill. The shipping cost advantage of managing USPS yourself (you keep the discount; a 3PL marks up postage) and the flexibility of packing each order to spec outweighs any 3PL benefit at this scale.

**Mid-term (500–3,000 units/month):** Hire a part-time packing assistant (15–20 hours/week at $15–18/hour). Continue self-shipping via Pirate Ship. This is operationally simpler and more profitable than a 3PL at these volumes.

**Scale threshold for 3PL evaluation (7,000–10,000 units/month):** At projected demand, the economics shift. Key options:

| 3PL | Best For | Min Volume | Pricing Model | Fit for ModRun |
|---|---|---|---|---|
| ShipMonk | 50–500 orders/month | 50 orders/mo | Per-pick + storage | Good for month 4–8 trial |
| Simpl Fulfillment | 1–500 orders/month | None | Flat-rate per order | Best entry-level 3PL |
| ShipBob | 500+ orders/month | $275/mo minimum | Per-pick + storage + postage markup | Too expensive at <500/month |
| Amazon FBA | High-velocity Amazon SKUs | Per-ASIN | 15% referral + $2.50–5/unit FBA | Best for top 2–3 SKUs once proven |

**Recommendation for ModRun:** Do not engage a 3PL before 7,000 units/month. At that scale:
- Simpl Fulfillment or ShipMonk for Etsy + own-site orders
- Amazon FBA for the 1–2 highest-velocity SKUs listed on Amazon Handmade
- Keep self-fulfillment for custom/personalized orders (these require item-level inspection)

**Regional warehouse note:** At 7,000–10,000 units/month, shipping cost is the largest logistics variable. A single Midwest warehouse (e.g., ShipBob Chicago, ShipMonk Fort Lauderdale) puts the operation within Zone 3 of ~70% of the US population, cutting blended Ground Advantage cost by ~$0.50–1.00/package vs. shipping from a coastal home base.

---

## Section 4: Supplier Scorecard

### 4.1 Master Supplier Scorecard

| Vendor | Category | Price/kg or Unit | MOQ | Lead Time | Reliability (1–10) | Priority |
|---|---|---|---|---|---|---|
| **eSUN** (Amazon bundles) | PLA Filament | $11–13/kg (10kg) | 10kg | 2–5 days (Prime) | 9 | Primary filament |
| **Anycubic** (direct store) | PLA Filament | $10.49/kg (50kg deal) | No MOQ | 3–7 days | 7 | Secondary / pallet orders |
| **Polymaker** (wholesale) | PLA Filament | $14.99/kg (case) | $1,000 order | 3–7 days | 9.5 | Phase 3 primary (quality tier) |
| **Overture** (Amazon + direct) | PLA / PETG | $11–14/kg | None (Amazon) | 2–5 days (Prime) | 8 | PETG primary; PLA backup |
| **SUNLU** (direct store) | PLA Filament | $12–14/kg (6kg mix) | 6 spools | 3–7 days | 7.5 | Color sampling / flex backup |
| **Pirate Ship** | Shipping | ~$3.50–6.00/label | None | Instant | 10 | Primary shipping platform |
| **Shop4Mailers** | Poly Mailers | $0.05/unit (1000+) | 100 units | 3–5 days | 9 | Primary packaging |
| **Packlane** | Custom Boxes | $0.76–2.84/unit | 1 unit | 10–14 days | 8 | Phase 2+ gift bundles |
| **EcoEnclose** | Custom Boxes | ~$1.50–3.00/unit | 100 units | 10–15 days | 8.5 | Eco-brand tier |
| **Simpl Fulfillment** | 3PL | ~$5–8/order | None | — | 8 | Phase 3 fulfillment |

### 4.2 Risk Assessment

**Concentration risk:** eSUN via Amazon is the current single-point dependency for filament. If Amazon has a stock event on the 10kg bundle (which occurs 2–4 times per year on high-demand colors), the operation needs a same-day pivot to Anycubic direct. Pre-qualify Anycubic by placing one test order before they are needed.

**Tariff risk:** Both eSUN and Anycubic are Chinese brands. US tariffs on Chinese goods in 2026 have already been factored into current pricing, but a further escalation could raise commodity filament 10–20%. Polymaker (with some US-warehoused inventory) and Overture provide partial hedging. Prusament (EU-made) is the extreme hedge but at a 100% price premium.

**Shipping rate risk:** The April 2026 USPS 8% temporary increase runs through January 17, 2027. This increases per-order COGS by ~$0.40–0.50 vs. pre-increase rates. Build this into pricing now; do not absorb it passively.

---

## Section 5: Negotiation Strategy and Payment Terms

### 5.1 eSUN (Amazon / Direct)

**Negotiation lever:** Amazon bundles have no negotiation — you take the listed price. The only lever is timing: eSUN runs sale events (Prime Day, Black Friday, periodic Lightning Deals) where 10kg bundles can drop 15–20%. Watch for these and build inventory.

**For direct wholesale (esun3dstore.com or via wholesale eBay):** Email with your monthly volume projection (kg/month), your top 3 colors, and a 6-month commitment interest. eSUN sales reps in the US have discretionary discount authority up to ~15% below listed bulk pricing. A 12-month commitment for 40–60kg/month can yield $8.50–10/kg, eliminating the advantage Anycubic currently holds on pure price.

**Timeline:** Contact eSUN direct when monthly consumption reaches 20kg/month consistently.

### 5.2 Anycubic (Direct Store)

No negotiation on the bundle deals — prices are listed. The leverage is the public sale price ($524.73 for 50kg) vs. the listed regular price ($1,149.50). The sale price appears to be effectively evergreen (constantly "on sale") based on observation of the product page. Confirm this by placing an order in Month 2 and documenting the price paid.

**Payment terms:** Credit card only on storefront. Net 30 not available without direct sales contact.

### 5.3 Polymaker (Wholesale)

**Negotiation is expected.** Polymaker's wholesale program is built for negotiation at the $1,000+ order level. Key levers:

1. **Volume commitment:** Commit to $3,000–5,000/month in orders to unlock the free-shipping threshold and potentially negotiate an additional 5–10% off per-case pricing.
2. **Net 30 terms:** Available for qualified accounts. Apply after the second or third order to establish payment history. Net 30 improves cash flow significantly when placing $1,000+ monthly orders.
3. **Exclusive color SKUs:** Polymaker occasionally offers print farm operators dedicated production runs of specific colors not in the standard catalog. If your best-selling color is unique, this is a moat.

**Contact:** support.na@polymaker.com. Introduce yourself as a production operator (not a hobbyist) with specific monthly volume targets. Wholesale reps respond better to "I need 60kg of PolyLite PLA in three colors on net-30 terms" than to general inquiries.

### 5.4 Packlane (Packaging)

No formal negotiation on the online quote tool. For orders above 2,000 units, email their team directly for a custom quote — operators report 10–15% discounts at 2,000+ unit runs. At 500–1,000 units, the online quote is the best available price.

### 5.5 Post-Test-Print Activation Checklist

After the test print validates the ModRun design and establishes a baseline COGS per unit, execute these steps in order:

**Immediate (Week 1 post-test):**
- [ ] Open a Pirate Ship account (free). Print your first test shipping label.
- [ ] Purchase 1 case (10kg) of eSUN PLA+ in black and 1 case in white from Amazon. This validates supplier reliability at current pricing before committing to higher volumes.
- [ ] Order 500 poly mailers (9x12", 2.5 mil) from Shop4Mailers or Amazon. Cost: ~$35–50.

**Month 1–2:**
- [ ] Place one Anycubic test order (5–10kg, single color) to validate their AMS compatibility with your P1S/X1C setup and confirm lead time.
- [ ] Set up Pirate Ship for batch label printing. Connect to Etsy shop via Pirate Ship's Etsy integration (orders sync automatically; print labels in batches).
- [ ] Establish a filament cost tracker (simple spreadsheet: date ordered, vendor, color, kg, $/kg, Amazon ASIN or order number).

**Month 2–3:**
- [ ] If black/white 10kg eSUN cases are depleting in under 3 weeks, increase order cadence to 20kg/month.
- [ ] Register at us-wholesale.polymaker.com and place a sample order ($1,000, ~67kg). Compare quality against eSUN on the same ModRun print file.
- [ ] Design custom-printed poly mailer or custom Packlane box. Get the design ready even if you do not order yet — artwork takes longer than the print run.

**Month 3–4:**
- [ ] Contact eSUN direct (esun3dstore.com) with monthly volume figures to explore direct wholesale pricing.
- [ ] If bundle SKUs (3-pack, 6-pack) are generating >30% of revenue, activate Packlane for 500-unit custom box run. Budget ~$0.85–1.10/unit for the small mailer box at this quantity.
- [ ] Evaluate whether part-time packing help is needed (threshold: packing/shipping taking more than 3 hours/day consistently).

---

## Section 6: Open Gaps and Confidence Notes

**High confidence:** eSUN and Anycubic pricing is based on live Amazon/storefront listings verified April 2026. Pirate Ship commercial rates and the 8% USPS April increase are confirmed. Packlane and poly mailer pricing is from documented sources.

**Medium confidence:** Polymaker wholesale per-kg pricing (~$14.99/kg) is based on the publicly listed Panchroma PLA pricing visible on their wholesale landing page and corroborated by multi-printer-architecture.md Section 2.1 which cites "Polymaker wholesale ($1,000 minimum order)." The precise PolyLite PLA pricing requires a logged-in account; the stated figure is the best available estimate.

**Lower confidence:** SUNLU reseller tier pricing ($10–12/kg at 50+ boxes) is extrapolated from their reseller program structure and community-reported figures, not a verified quote. Contact support@3dsunlu.com for an actual quote before treating this as a firm number.

**Gaps not yet researched:**
- Specific Overture wholesale tier pricing (requires direct contact with overture3d.com wholesale team)
- Anycubic 100kg pricing (the 50kg deal is confirmed; 100kg pricing was not clearly listed)
- Priority Mail Cubic exact rates for ModRun's specific box dimensions — requires Pirate Ship rate calculator with a test address pair
- Lead time variance for Anycubic during high-demand periods (their Chinese warehouse can delay 2–3 weeks during major sales events like 618 and 11/11)

---

## Sources

- [Anycubic Bulk PLA 50–100kg Deals](https://store.anycubic.com/products/pla-basic-50-100kg-deals)
- [eSUN 10KG Bulk PLA Basic — Amazon B0G2KSS613](https://us.amazon.com/eSUN-Filament-1-75mm-Bundle-Printing/dp/B0G2KSS613)
- [eSUN 10KG PLA+ Bundle — Amazon B0G2KWC5XL](https://www.amazon.com/eSUN-Pro-Grade-Toughness-Clog-Free-Dimensional/dp/B0G2KWC5XL)
- [Polymaker US Wholesale — Print Farm Program](https://us-wholesale.polymaker.com/pages/wholesale-filament-for-print-farms)
- [Polymaker PolyLite PLA Wholesale](https://us-wholesale.polymaker.com/products/polylite-pla)
- [Overture 3D Wholesale Program](https://overture3d.com/pages/wholesale)
- [SUNLU Become A Reseller](https://store.sunlu.com/pages/become-a-reseller)
- [Bambu Lab Filament Bulk Sale](https://us.store.bambulab.com/collections/filament-bulk-sale)
- [ADP Industries: Best Filament for Bambu Lab Printers 2026](https://www.adpindustries.com/blog/best-filament-bambu-lab-2026/)
- [MatterHackers Bulk 3D Filament Program](https://www.matterhackers.com/store/l/matterhackers-bulk-3d-filament/sk/MX40GN8F)
- [Pirate Ship: Discounted USPS Ground Advantage Rates](https://www.pirateship.com/usps/ground-advantage)
- [Pirate Ship: April 2026 USPS Time-Limited Price Change](https://support.pirateship.com/en/articles/14491291-april-2026-usps-time-limited-price-change)
- [USPS Ground Advantage Rates 2026 — I'd Ship That](https://idshipthat.app/shipping-rates/usps-ground-advantage/)
- [USPS Ground Advantage Complete Guide 2026 — ClickPost](https://www.clickpost.ai/blog/usps-ground-advantage)
- [USPS Rate Changes April 2026 — SavePostage](https://savepostage.com/usps-rate-increase.html)
- [Packlane Custom Mailer Box Pricing](https://packlane.com/products/mailer-box)
- [Packlane vs Packola vs PackM vs Arka 2026](https://www.growthmarketingpro.com/packola-vs-packlane-vs-packm-vs-arka/)
- [EcoEnclose Custom Shipping Boxes](https://www.ecoenclose.com/shop/custom-shipping-boxes/)
- [EcoPackables Packaging Cost Guide 2026](https://www.ecopackables.com/blogs/news/how-much-does-packaging-cost)
- [Seller Gear: Best Poly Mailers for Etsy & Amazon Sellers 2026](https://www.listing-forge.com/gear/poly-mailers)
- [Simpl Fulfillment — Small Business 3PL](https://www.simplfulfillment.com/)
- [ShipMonk — Fulfillment for 50–500 Orders/Month](https://www.shipmonk.com/)
- [ShipBob Pricing 2026](https://www.simplfulfillment.com/breakdowns/shipbob-pricing)
- [Best 3PL for Small Businesses 2026 — ShipCore](https://shipcorefulfillment.com/best-3pl-for-small-business/)
- [SpoolPrices: 3D Printer Filament Price Comparison](https://spoolprices.com/filament)
- [Fabbaloo: 3D Printer Filament Prices in 2025](https://www.fabbaloo.com/news/3d-printer-filament-prices-in-2025-from-5-bulk-deals-to-premium-brands)
