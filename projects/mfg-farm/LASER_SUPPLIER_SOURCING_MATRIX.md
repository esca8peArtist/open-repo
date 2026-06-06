---
title: Laser Supplier Sourcing Matrix — Equipment Vendors, Material Suppliers, Cost Breakdown
project: mfg-farm
created: 2026-06-06
status: research-complete
session: laser-engraving-market-research
depends_on: LASER_ENGRAVING_MARKET_ANALYSIS.md
confidence: high — vendor pricing sourced from official sites, Amazon listings, and market research (June 2026); material unit costs are ranges based on wholesale volume; verify current pricing before purchasing
---

# Laser Supplier Sourcing Matrix

**Lead finding**: Equipment purchasing risk is low — all five vendors listed have U.S. warehouse fulfillment and established return/warranty policies. Material sourcing is the more important lever for margin: the difference between buying laser blanks from a specialty wholesale supplier (MakerFlo, Master Maker Crafts) versus retail channels (Amazon) is 30–50% per unit, which directly determines whether Tier 1 and Tier 2 products meet the 4×–6× markup target. Establish wholesale accounts with at least two material suppliers before first order.

---

## Part 1: Equipment Suppliers

### 1.1 xTool (Makeblock Co.)

**Products**: S1 20W/40W, P2S CO2, D1 Pro, M1, F1 fiber
**Relevant model**: S1 40W (primary recommendation)

| Attribute | Detail |
|---|---|
| U.S. presence | Yes — warehouse fulfillment; support team in U.S. time zones |
| Purchase channels | xTool.com (direct), Amazon, Swing Design, Dynamism |
| S1 40W price range | $1,549–$2,099 (sales events reach $1,359) |
| Delivery | 3–7 business days from U.S. warehouse |
| Warranty | 1-year machine, 6 months laser module |
| Support quality | Strong — active xTool community, official YouTube tutorials, LightBurn integration, responsive email support |
| Return policy | 30 days from xTool direct; Amazon return policy applies for Amazon orders |
| Replacement parts | Laser modules sold separately ($499–799 for 40W module) — modular design extends machine life |
| Software | xTool Creative Space (free, macOS/Windows), LightBurn compatible (industry standard) |

**Recommended purchase path**: Buy directly from xTool.com or Amazon. Watch for sales (Black Friday, Chinese New Year, xTool Anniversary) — 15–25% discounts are common. The Basic Bundle (machine + honeycomb + air assist) is sufficient for launch; rotary can be added later if tumbler engraving becomes a SKU.

**Notes**: xTool is a subsidiary of Makeblock, a well-funded Chinese edtech/hardware company. Not a fly-by-night operation. Parts availability and software updates have been consistent since S1 launch (2023).

---

### 1.2 OMTech Laser

**Products**: Full range from entry-level 40W diode to industrial 150W CO2; also fiber laser and DTF printers
**Relevant model**: Maker MF1624-60 (60W CO2, 16"×24") as the garage/production alternative

| Attribute | Detail |
|---|---|
| U.S. presence | Yes — warehouses in New Jersey and Georgia; demo room available |
| Purchase channels | omtech.com (direct), Amazon |
| MF1624-60 price range | $899–$1,499 (varies with bundle — water chiller, LightBurn license) |
| Delivery | 3–7 business days standard; freight shipping for larger models |
| Warranty | 2 years on machine (best warranty in this comparison) |
| Support quality | Virtual installation sessions, live chat, phone, email. Community forum active. |
| Return policy | 30-day returns; contact customer service for RMA |
| Software | RDWorks (bundled, free), LightBurn compatible ($60 license) |

**Notes**: OMTech sells directly via omtech.com with the same Amazon pricing but often better bundle deals (water chiller + LightBurn included). The 2-year warranty on entry-level machines is a material differentiator — most competitors offer 1 year.

**Budget path**: The MF1624-60 at ~$1,099 with a $150 inline fan/exhaust duct setup and $60 LightBurn license totals approximately $1,310 — less than the xTool S1 Basic Bundle, with a larger work area and stronger cutting power. The tradeoff is open-frame design requiring external ventilation.

---

### 1.3 Glowforge

**Products**: Pro HD, Pro (rebuilt), Plus (rebuilt)
**Relevant model**: Pro HD (listed only for completeness — not recommended at this stage)

| Attribute | Detail |
|---|---|
| U.S. presence | Yes — designed, manufactured, and serviced in U.S. (Seattle) |
| Purchase channels | glowforge.com, shop.glowforge.com |
| Pro HD price | $6,995 |
| Delivery | 1–2 weeks |
| Warranty | 1-year standard |
| Support quality | U.S.-based; strong community; but cloud dependency is a business risk |
| Return policy | 30-day return policy |
| Software | Web-based only — no LightBurn, no offline operation |

**Notes**: Do not purchase unless clear acrylic panel cutting is a core SKU and the cloud-only software model is acceptable. The $7,000 price point requires $1,000/month in gross profit contribution to pay back in 24 months — achievable but requires committed product focus.

---

### 1.4 Thunder Laser USA

**Products**: Nova 24, Nova Plus 35, Nova 63, and smaller Bolt series
**Relevant model**: Nova Plus 35 (noted as Phase 3 target)

| Attribute | Detail |
|---|---|
| U.S. presence | Yes — Thunder Laser USA (California) handles U.S. sales and service |
| Purchase channels | thunderlaserusa.com, thunderlaser.com |
| Nova Plus 35 price | $10,350 |
| Delivery | Freight, 2–4 weeks; demo available at showroom |
| Warranty | 2 years machine, 1 year laser tube |
| Support quality | Rated highly — 100% customer recommendation rate. U.S. presence enables faster service. |
| Return policy | 30-day return; freight return logistics apply |
| Software | LightBurn + RDWorks compatible |

**Notes**: Thunder Laser is the correct machine for a Phase 3 production upgrade. The 900×500mm bed handles 2–3 cutting boards simultaneously per run. Acquisition makes sense at 400+ units/month production volume with a clear ROI model.

---

### 1.5 Ortur

**Products**: Laser Master 3, LM3 LE, LU series modules
**Relevant model**: Laser Master 3 (10W or 20W, for validation/entry only)

| Attribute | Detail |
|---|---|
| U.S. presence | Ships from U.S. Amazon FBA warehouse |
| Purchase channels | Amazon primarily; ortur.net direct |
| LM3 20W price | $499–$599 |
| Delivery | Amazon Prime, 2–3 days |
| Warranty | 1-year |
| Support quality | Active community; Ortur has official support channels; spare parts available |
| Return policy | Amazon standard 30-day return |
| Software | LightBurn + LaserGRBL compatible |

---

### 1.6 Equipment Supplier Comparative Recommendation

| Scenario | Recommended Vendor | Rationale |
|---|---|---|
| Phase 1, indoor workspace | xTool S1 40W via Amazon/xTool.com | Enclosed, safe, easy setup, best community |
| Phase 1, garage/outdoor workspace | OMTech MF1624-60 via omtech.com | Better $/watt, larger work area, 2-year warranty |
| Validation only | Ortur LM3 20W via Amazon | Minimal capital risk before proving demand |
| Phase 3 production scale | Thunder Laser Nova Plus 35 | Best production throughput, proven quality |
| Only if clear acrylic is core SKU | Glowforge Pro HD via glowforge.com | Only machine with clear acrylic + ease of use |

---

## Part 2: Material Suppliers — Laser Engraving Blanks and Consumables

### 2.1 MakerFlo

**Website**: makerflo.com
**Type**: Wholesale blanks specialist — tumblers, cutting boards, drinkware, wood products
**Positioning**: Built explicitly for professional laser engravers and sublimation sellers; bulk pricing tiers

| Product Category | Unit Type | Est. Price Range (Retail/Single) | Bulk Discount |
|---|---|---|---|
| 20oz stainless tumbler blanks | Per unit | $4–7 | 10% @ 25+; 20% by case |
| Bamboo cutting boards (14"×10") | Per unit | $6–9 | 15–20% at case quantities |
| Walnut cutting boards | Per unit | $9–15 | 15–20% at case quantities |
| Rubberwood cutting boards | Per unit | $5–8 | 15–20% at case quantities |
| Wine decanters (clear glass, laser-safe) | Per unit | $8–14 | By case |
| Coaster blanks (bamboo, 4-pack set) | Per set | $3–5 | By case |

**Strengths**: Blanks are engineered and pre-tested for laser compatibility; gift-ready boxes included with all products; 2-business-day processing; mix-and-match bulk pricing.

**Best for**: Cutting boards, tumblers, drinkware — the Tier 1 and Tier 2 high-volume products.

**Wholesale access**: Apply at makerflo.com/pages/wholesale. No minimum stated for first order; case discounts kick in automatically at order thresholds.

---

### 2.2 Master Maker Crafts (mastermakercrafts.com)

**Type**: U.S.-based wholesale craft supplier — wood, metal, acrylic blanks for custom gifts
**Target customer**: Etsy sellers, laser engravers, sublimation businesses

| Product Category | Est. Unit Price | Notes |
|---|---|---|
| Wood keychains and small shapes | $0.50–1.50 | High-margin gift accessories |
| Wood sign blanks (6"–12") | $2–5 | Rounds, rectangles, states |
| Leatherette sheets (laser-safe) | $1.50–3.50/sheet | Patches, keychains, coasters |
| Bamboo products | $1–4 | Cutting boards, coasters, spoons |
| Acrylic blanks (colored, pre-cut) | $0.80–2.50 | Keychains, ornaments, signs |

**Strengths**: Wide variety for small accessory products; good for Tier 3 high-margin niches (keychains, small signs, ornaments).

**Best for**: High-margin accessory SKUs with fast engraving time (pet tags, keychains, ornaments, small signs).

---

### 2.3 JPPlus (Johnson Plastics Plus)

**Website**: jpplus.com
**Type**: Professional engraving material distributor — 50+ years in industry; serves sign shops and award shops
**Target customer**: Professional engravers, sign makers, award shops, promotional products businesses

| Product Category | Est. Unit Price | Notes |
|---|---|---|
| Rowmark acrylic laser sheets | $8–25/sheet (12"×24") | 50+ color/finish combos; UV-resistant options |
| Coated metal blanks | $2–8 per piece | Aluminum, brass for CO2 engraving |
| Wood plywood sheets (laser-grade) | $5–15/sheet | Baltic birch, maple; guaranteed consistent quality |
| Engraving blanks (awards, tags) | $0.50–8.00 | Desk nameplates, ID tags, awards |
| Sample kits | $15–40 | Material sample packs for testing |

**Strengths**: Professional-grade materials with guaranteed consistency for production engraving. Rowmark acrylic is industry-standard for sign and award shops — produces clean, consistent results. Material sample kits allow material testing before buying production quantities.

**Best for**: Acrylic desk signs, awards, coated metal products. Essential if acrylic desk products become a core SKU.

**Minimum orders**: Typically no minimums on standard items; quantity pricing available.

---

### 2.4 Crafted Supplies (craftedsupplies.com)

**Type**: Small-batch laser engraving blanks; leatherette specialist
**Target customer**: Etsy sellers, small laser engraving businesses

| Product Category | Est. Unit Price | Notes |
|---|---|---|
| Leatherette patches and sheets | $1.50–3.00 | Patches, keychains, coasters — laser-safe |
| Wood keychains and bottle openers | $0.80–2.00 | Popular Tier 2 gift products |
| Wood cutting boards | $5–12 | Various sizes |

**Strengths**: Specializes in leatherette/PU leather products that are underrepresented on other suppliers. Good for differentiated product lines.

**Best for**: Leather-adjacent products where real leather cost is prohibitive ($5–15/piece) but the leatherette aesthetic achieves 80% of the look at 20% of the cost.

---

### 2.5 Amazon Bulk (Supplemental / Emergency)

**Use case**: Spot purchasing when wholesale suppliers are out of stock; initial testing before opening wholesale accounts.

| Product Category | Est. Price | vs. Wholesale |
|---|---|---|
| 20oz tumbler blanks (12-pack) | $48–72/pack ($4–6/unit) | ~0–20% premium to wholesale |
| Wood cutting board blanks | $8–15/unit | 20–40% premium to wholesale |
| Laser material sample kits | $15–40 | Useful for initial material testing |

**Notes**: Amazon pricing varies widely. For first 10–20 test units, Amazon convenience is acceptable. Beyond that, establish MakerFlo or Master Maker Crafts wholesale accounts to capture the 20–30% price difference.

---

## Part 3: Per-Unit Material Cost Breakdown by Product Tier

### Assumptions
- All prices reflect wholesale/bulk purchasing (not Amazon retail)
- Labor cost basis: $15/hour operator time
- Machine depreciation: $0.10–0.25/unit (based on xTool S1 at $1,899 amortized over 18 months, 500 units/month)
- Electricity: ~$0.02–0.05/hour at current residential rates
- Packaging: $0.40–1.00 per shipment

---

### Tier 1 — Basic Products ($15–30 Retail Target)

**Product A: Engraved Keychain (Wood or Acrylic)**

| Cost Element | Unit Cost |
|---|---|
| Blank (wood or acrylic, 2"×2") | $0.60–1.20 |
| Engraving time: 2–4 min @ $15/hr | $0.50–1.00 |
| Machine depreciation | $0.10 |
| Electricity | $0.01 |
| Packaging (small poly bag + card) | $0.20 |
| **Total COGS** | **$1.41–2.51** |
| Retail price | $12–18 |
| **Gross margin** | **86–88%** |

**Product B: Engraved Pet ID Tag (Brass or Stainless)**

| Cost Element | Unit Cost |
|---|---|
| Blank (metal tag, wholesale) | $0.80–1.50 |
| Engraving time: 2–3 min | $0.50–0.75 |
| Machine depreciation | $0.10 |
| Packaging | $0.25 |
| **Total COGS** | **$1.65–2.60** |
| Retail price | $10–18 |
| **Gross margin** | **83–84%** |

**Product C: Engraved Coaster Set (4-pack, Bamboo)**

| Cost Element | Unit Cost |
|---|---|
| 4 bamboo coaster blanks | $2.50–4.00 |
| Engraving time: 10–15 min (batch 4) | $2.50–3.75 |
| Machine depreciation | $0.40 |
| Packaging (kraft box with insert) | $0.60 |
| **Total COGS** | **$6.00–8.75** |
| Retail price | $22–32 |
| **Gross margin** | **68–73%** |

---

### Tier 2 — Premium Products ($30–60 Retail Target)

**Product D: Engraved Cutting Board (14"×10" Bamboo or Walnut)**

| Cost Element | Unit Cost |
|---|---|
| Blank (bamboo wholesale) | $5.50–8.00 |
| Blank (walnut wholesale) | $9.00–13.00 |
| Engraving time: 20–30 min | $5.00–7.50 |
| Machine depreciation | $0.75 |
| Packaging (gift box + kraft wrap) | $0.80 |
| **Total COGS (bamboo)** | **$12.05–17.05** |
| **Total COGS (walnut)** | **$15.55–22.05** |
| Retail price (bamboo) | $35–48 |
| Retail price (walnut) | $45–65 |
| **Gross margin (bamboo)** | **62–66%** |
| **Gross margin (walnut)** | **65–66%** |

**Product E: Engraved Stainless Tumbler (20oz)**

| Cost Element | Unit Cost |
|---|---|
| Blank (wholesale tumbler) | $5.00–7.00 |
| Engraving time: 15–20 min (rotary) | $3.75–5.00 |
| Machine depreciation | $0.50 |
| Rotary depreciation allocation | $0.05 |
| Packaging (gift box) | $0.70 |
| **Total COGS** | **$10.00–13.25** |
| Retail price | $28–45 |
| **Gross margin** | **64–70%** |

---

### Tier 3 — Custom / High-Complexity Products ($60–150 Retail Target)

**Product F: Full Desk Organization Set (Cutting Board + Coasters + Name Plate)**

| Cost Element | Unit Cost |
|---|---|
| Cutting board blank (walnut) | $11.00 |
| 4 coaster blanks (bamboo) | $3.00 |
| Nameplate blank (maple, 5"×2") | $1.50 |
| Engraving time: 60–90 min total | $15.00–22.50 |
| Machine depreciation | $1.50 |
| Premium gift packaging | $3.00 |
| **Total COGS** | **$35.00–42.50** |
| Retail price | $85–130 |
| **Gross margin** | **56–59%** |

**Note**: Tier 3 gross margin appears lower (56–59%) because labor is the dominant cost at high complexity. However, AOV is $100+ which makes these high-revenue-per-order products. Consider whether selling separate items at $35–$45 each with lower labor burden produces better hourly economics than one bundled $100 item.

**Product G: Custom Corporate Gift Set (Branded, 10-unit minimum B2B order)**

| Cost Element | Per Unit (at 10-unit order) |
|---|---|
| Cutting board or tumbler blank | $6.50–9.00 |
| Design setup (one-time, amortized over 10) | $2.00–3.00 |
| Engraving time: 20–25 min | $5.00–6.25 |
| Machine depreciation | $0.50 |
| Packaging (branded box if applicable) | $1.00–2.00 |
| **Total COGS per unit** | **$15.00–20.25** |
| B2B unit price (wholesale to corporate buyer) | $30–50 |
| **Gross margin** | **50–60%** |

**B2B channel note**: Corporate gifting orders at 25–100+ units per order dramatically improve economics at the production level, but initial pricing negotiation often includes discounts. Target 50%+ gross margin on B2B orders; below 45% is not worth the order complexity.

---

## Part 4: Monthly Consumables Cost Estimate

For a single xTool S1 40W running 3–4 hours/day, 20 production days/month:

| Consumable | Est. Monthly Cost | Notes |
|---|---|---|
| Electricity (200W × 4hr × 20 days) | $3.84–$5.76 | At $0.12–$0.18/kWh |
| Air assist filter replacement | $5–10 | Activated carbon filter, monthly if cutting dense wood |
| Lens cleaning supplies | $3–5 | IPA wipes, lens tissue |
| Masking tape / transfer tape | $8–15 | For acrylic and painted surfaces |
| Spare diode modules (annualized / monthly) | $25–40 | 40W module rated ~5,000–8,000 hours; annualized at $480–800/module |
| Spare materials buffer (5% waste/error rate) | 5% of material cost | Varies by product mix |
| **Estimated fixed consumables per month** | **$45–75** | |

**At 200 units/month production**, consumables represent $0.23–$0.38/unit — effectively negligible versus material and labor costs.

**Water chiller note (OMTech CO2 only)**: Add $20–30/month for distilled water replacement and chiller maintenance.

---

## Part 5: Supplier Scorecard Summary

| Supplier | Best For | Min Order | Lead Time | Pricing Tier | Reliability |
|---|---|---|---|---|---|
| MakerFlo | Tumblers, cutting boards, drinkware | No minimum | 2 business days processing | Wholesale (20% bulk discount) | High — built for this market |
| Master Maker Crafts | Small accessories, leatherette, wood shapes | No minimum | Standard shipping | Wholesale | High |
| JPPlus | Acrylic sheets, coated metal, professional-grade | No minimum | Standard shipping | Trade pricing | High — 50+ years in industry |
| Crafted Supplies | Leatherette patches, specialty wood | No minimum | Standard | Retail/small wholesale | Medium |
| Amazon | Emergency / testing | 1 unit | Amazon Prime, 2 days | Retail (20–40% premium) | High for logistics; price is the tradeoff |

---

## Sources

- [MakerFlo Wholesale Blanks](https://makerflo.com/collections/laser-engraving-bulk-blanks)
- [MakerFlo Wholesale Program](https://makerflo.com/pages/wholesale)
- [Master Maker Crafts — Laser Engraving Blanks](https://www.mastermakercrafts.com/collections/laser-engraving-blanks)
- [JPPlus Laser Engraving Materials](https://www.jpplus.com/laser-engraving)
- [JPPlus Engraving Blanks](https://www.jpplus.com/engraving/blanks)
- [Crafted Supplies Laser Blanks](https://www.craftedsupplies.com/)
- [How to Price Laser-Engraved Products: The 4-to-6 Rule — MakerFlo](https://makerflo.com/blogs/craft-library/how-to-price-laser-engraved-products)
- [Laser Engraving Cost Breakdown — Creality Falcon](https://www.crealityfalcon.com/blogs/laser-academy/laser-engraving-cost)
- [How Much to Charge for Laser Engraving — The Maker's Chest](https://themakerschest.com/blogs/laser-engravers/how-much-should-i-charge-for-laser-engraving-services)
- [OMTech 60W CO2 Laser Engraver — Amazon](https://www.amazon.com/OMTech-Engraver-Engraving-Machine-Commercial/dp/B0C6X4VMY6)
- [OMTech Maker MF1624-60 — OMTech Official](https://omtechlaser.com/products/60w-co2-laser-engraver-cutter-usb-6r57-us)
- [Thunder Nova Plus 35 — Thunder Laser USA](https://www.thunderlaserusa.com/nova-35/)
- [xTool S1 — Amazon](https://www.amazon.com/xTool-Engraver-Enclosed-Engraving-Honeycomb/dp/B0CGHXCHDG)
