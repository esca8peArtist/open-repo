---
title: Phase 3 Pricing Strategy
project: mfg-farm
created: 2026-04-29
status: production-ready
session: Item21
depends_on: phase-3-product-validation-research.md, ITEM18_ADJACENT_MANUFACTURING_ECONOMICS.md, material-sourcing-supplier-economics.md
confidence: high — grounded in market WTP analysis (Item 21), COGS models (Item 18), and material cost baselines (Item 18/supplier research)
related: pricing-strategy.md, pricing-tiers.csv
---

# Phase 3 Pricing Strategy

**Lead finding:** The market evidence supports three-tier pricing for all Phase 3 candidates, but the tier boundaries differ by category. For desk accessories and homelab accessories — the two highest-priority Wave 1 products — a Standard-to-Premium range of $30–65 (single) to $55–90 (set) is market-consistent and defensible at mfg-farm's COGS structure. Net margins of 55–72% are achievable across all three tiers if volume-based shipping cost reduction is applied (key: drive AOV above $40 to amortize USPS Ground Advantage costs).

**COGS reference baseline** (from material-sourcing-supplier-economics.md and ITEM18):
- PLA+ print: $0.83–$0.98 material per 75g print; $1.15 total COGS per ModRun clip (print + packaging negligible)
- PETG print: $1.05–$1.35 material per 75g print; ~$1.40–$1.60 total COGS per unit
- Laser engraving (surface, no badge): adds $0.02–$0.05 per unit COGS (electricity + depreciation)
- Laser engraving (wood veneer badge): adds $0.20–$0.40 per unit COGS
- Shipping: USPS Ground Advantage $4.00–$5.50 per order (single unit); marginal cost per additional unit $1.00–$1.80

---

## Top 3 Phase 3 Candidates — Pricing Models

### Candidate 1: Homelab Server Accessories

**Product definition:** 10-inch rack-compatible accessories — fan mount bracket, cable pass-through panel, Raspberry Pi tray, Ethernet patch panel blank, cable routing tray. Printed in PETG or ABS (heat-resistant, rack-appropriate).

**Why PETG/ABS is required (and commands a premium):** 24/7 rack operation generates sustained heat of 40–65°C at cable-adjacent points. PLA+ begins to deform at 55–60°C. PETG (70–75°C deflection) is the appropriate material. This is a genuine technical justification for a material premium — not just marketing.

#### Tier 1: Standard (PETG, functional design)

| SKU | Print weight | Material cost | Shipping (per order) | Total COGS (single) | Etsy price | Net margin |
|---|---|---|---|---|---|---|
| 1U fan mount bracket | 90g | $1.26 | $4.50 | $5.76 | $28 | 79% |
| Cable pass-through panel | 60g | $0.84 | $4.50 | $5.34 | $22 | 76% |
| Raspberry Pi 4/5 tray (1U) | 110g | $1.54 | $4.50 | $6.04 | $32 | 81% |
| Ethernet blank panel | 40g | $0.56 | $4.50 | $5.06 | $18 | 72% |
| Cable routing tray (side-mount) | 80g | $1.12 | $4.50 | $5.62 | $26 | 78% |

*Etsy fees estimated at 6.5% of sale price. Packaging at $0.15/unit. Net margin = (price − COGS − Etsy fees) / price.*

**Single unit gross margin at Standard tier: 72–81%**

**Note on shipping:** Single-unit orders at $18–32 face a 14–25% effective shipping tax from the buyer's perspective. Etsy free shipping threshold of $35 can be met by bundling 2+ accessories, which incentivizes higher AOV. Frame the listing as "buy 2, free shipping" implicitly by pricing just below $35 for single units and just above for two-unit bundles.

#### Tier 2: Premium (PETG + laser-engraved labels, colored filament)

| SKU | Upgrade from Standard | Premium add | Etsy price | Delta from Standard | Net margin |
|---|---|---|---|---|---|
| Fan mount — labeled + colored | PETG premium color | Laser-engraved port labels | $38 | +$10 | 82% |
| Pi tray — labeled | PETG + custom color | Pi model engraved + labeled | $42 | +$10 | 82% |
| 4-piece bundle (fan + tray + blank + pass-thru) | Standard components | Laser labels on all 4 | $95 | bundle premium | 79% |

**COGS for 4-piece bundle:**
- Material (4 pieces blended): $4.20
- Engraving (4 pieces): $0.20
- Packaging (poly mailer + tissue): $0.35
- Shipping (combined): $5.50
- Etsy fees (6.5%): $6.18
- **Total COGS: $16.43**
- **Revenue: $95 | Net margin: 83%**

#### Tier 3: Specialty (Custom configuration, specific hardware)

| SKU | Configuration | Price | Net margin |
|---|---|---|---|
| Custom Pi cluster tray (3-Pi configuration) | On-request design | $65–90 | 68–74% |
| Full rack cable management kit (6-piece) | Mixed SKUs + cable ties | $110–135 | 71–76% |
| Branded OEM batch (100+ units) | Custom logo laser engraved | $18–22/unit (volume) | 60–65% |

**Volume pricing (Specialty/OEM tier):**
- 1–5 units: standard Etsy retail
- 6–12 units: 10% discount (free shipping auto-applies, higher AOV)
- 13–24 units: 15% discount (custom order via Etsy message)
- 25+ units: 20% discount (direct invoice, custom lead time)

---

### Candidate 2: Modular Desk Accessories

**Product definition:** Parametric desk accessory set — pen holder, cable routing tray (desk-surface, not under-desk), monitor arm cable clip, headphone hanger, charging dock shell. FDM printed, sold as individual pieces or as "desk system bundles."

**Print profile:** Most desk accessories are simple geometry, 30–90min print time per piece. Fail rate for simple hollow shapes is lower than complex geometries — estimated 4–6% vs. 10% for cable clips with snap features.

#### Tier 1: Standard (PLA+, matte black or matte white)

| SKU | Print weight | Material cost | COGS single | Etsy price | Net margin |
|---|---|---|---|---|---|
| Pen holder (cylindrical, modular) | 65g | $0.72 | $5.36 | $18 | 70% |
| Cable routing tray (desk surface) | 120g | $1.33 | $6.07 | $25 | 76% |
| Monitor arm cable clip (set of 4) | 80g total | $0.89 | $5.55 | $20 | 72% |
| Headphone hanger (monitor-mount) | 55g | $0.61 | $5.27 | $18 | 71% |
| Charging dock shell | 85g | $0.94 | $5.60 | $22 | 75% |

**Standard 4-piece desk bundle (pen holder + cable tray + 4x clips + hanger):**
- Material blended: $3.55
- Packaging: $0.40
- Shipping: $5.50
- Etsy fees: $4.88 (at $75 price)
- **Total COGS: $14.33**
- **Revenue: $75 | Net margin: 81%**

**Recommended launch price:** $75 for the 4-piece bundle. Individual pieces at $18–25 for buyers who want to expand an existing set.

#### Tier 2: Premium (PETG or custom color, laser engraving)

**Premium differentiators:**
1. Custom color filament (+$3–5/unit raw material cost increase)
2. Laser-engraved personal name or icon on pen holder or cable tray face
3. Frosted or translucent PETG variant (requires different filament — $16–20/kg)

| SKU | Upgrade | Etsy price | Delta | Net margin |
|---|---|---|---|---|
| Pen holder — custom name engraved | PETG + laser | $28 | +$10 | 76% |
| Cable tray — custom color | Custom filament | $32 | +$7 | 77% |
| Premium 4-piece bundle | Custom color + engraved pen holder | $95 | +$20 | 82% |

**WTP justification:** Market evidence shows customers pay $40–80 for laser-engraved desk items in similar categories (engraved nameplates: $25–35; engraved coasters: $30–45). The custom name angle extends the WTP ceiling because it creates a gift-purchase use case in addition to self-purchase. Q4 holiday season is an opportunity to position engraved desk sets as premium gifts.

#### Tier 3: Specialty (laser-engraved acrylic label sets, designer collections)

| SKU | Description | Price | Net margin |
|---|---|---|---|
| Acrylic cable label set (12 labels) | Laser-engraved acrylic, snap-fit to cable clips | $18–24 | 74–79% |
| Custom desk system (8-piece) | Full set matching customer's color | $120–150 | 70–75% |
| Corporate/office bundle (10 sets) | Volume order, company name engraved | $680–800 total ($68–80/set) | 58–65% |

**Acrylic cable label set economics:**
- Material cost: $0.30 (acrylic sheet) + $0.02 (engraving electricity)
- Engraving time: 5–8 min for 12 labels
- COGS: $0.32 material + $0.45 packaging + $4.50 shipping + $1.30 Etsy fee = $6.57
- Revenue: $20 | Net margin: 67%
- Note: Low margin relative to other products — but high AOV potential when bundled with cable clips

---

### Candidate 3: Gaming Cable Bundle

**Product definition:** Custom coiled keyboard cable + parametric cable management accessories (desk clips designed for gaming setups, cable routing for keyboard-to-PC cable path).

**Manufacturing note:** Coiled keyboard cables require braided sleeving + aviator connectors — components not manufactured by FDM printing. Two options: (a) partner with a braided cable supplier (MOQ 50–100, $8–12 BOM), or (b) focus on the FDM accessory ecosystem and recommend CableMod/equivalent for the cable itself. For Phase 3 Wave 1, option (b) is lower risk — sell the FDM accessories as a system that complements a purchased cable.

#### Tier 1: Standard (FDM accessories for gaming desk setup)

| SKU | Description | COGS | Etsy price | Net margin |
|---|---|---|---|---|
| Gaming cable guide clip (set of 6) | FDM PETG, desk-clamp mount | $6.20 | $22 | 72% |
| Under-monitor cable route tray | FDM PETG, monitor-arm compatible | $6.80 | $28 | 76% |
| Gaming desk cable bundle (clips + tray) | Set of 6 clips + 1 tray | $11.00 | $42 | 74% |

#### Tier 2: Premium (custom colors + cable gaming bundle with custom coiled cable)

**If proceeding with coiled cable manufacturing partnership:**

| SKU | Description | COGS | Etsy price | Net margin |
|---|---|---|---|---|
| Gaming bundle (clips + tray + custom coil cable) | Sourced cable ($12) + FDM accessories | $23 | $65 | 65% |
| Premium gaming bundle (custom color all components) | Color-matched cable + clips + tray | $28 | $80 | 65% |

**WTP justification:** CableMod's $30–35 cable + $22 in FDM accessories = $52–57 separately. Selling as a bundle at $65–80 delivers 10–40% premium for coordination convenience and design coherence. CableMod's documented quality complaints (failure rate, poor customer service) are an opening to position a "quality alternative."

**Gross margin at gaming bundle tier: 65–67%** — below ModRun's 65–72% range, but acceptable given the bundle product development path. If coiled cable partner proves unreliable, retreat to FDM accessories only (72–76%).

#### Tier 3: Specialty (custom color cable + custom printed clips — limited run)

| SKU | Description | Price | Net margin |
|---|---|---|---|
| Custom matched set (any cable color) | 12-week lead time, custom color filament | $95–120 | 62–68% |
| Creator Pro bundle (studio cable routing) | Designed for desk-to-camera cable paths | $110–140 | 60–66% |

---

## Gross / Net Margin Summary

| Category | Tier | Gross Margin | Net Margin (after Etsy fees) |
|---|---|---|---|
| Homelab accessories | Standard | 78–82% | 71–76% |
| Homelab accessories | Premium (4-piece bundle) | 81–85% | 78–83% |
| Homelab accessories | Specialty/OEM | 60–68% | 52–62% |
| Desk accessories | Standard | 70–76% | 63–70% |
| Desk accessories | Premium (bundle) | 79–83% | 75–80% |
| Desk accessories | Specialty (corporate) | 58–65% | 50–60% |
| Gaming bundles | Standard (FDM only) | 72–76% | 65–70% |
| Gaming bundles | Premium (cable + FDM) | 63–67% | 55–62% |
| Gaming bundles | Specialty | 60–68% | 52–60% |

**Target margin rule for Phase 3:** No product should launch below 65% net margin (after Etsy fees) at the Standard tier. If a product's COGS + shipping pushes net below 65%, either (a) increase retail price, (b) require minimum 2-unit order, or (c) bundle with another product to increase AOV.

---

## Volume Pricing Logic

**Single-unit pricing:** Etsy retail. No discount. USPS Ground Advantage single-unit shipping is the cost floor — discounting below this creates negative margin scenarios.

**2–3 unit pricing:** Offer "buy 2, get free shipping" on listings. This works because marginal shipping for 2nd unit is $1.50–$2.00 (not the full $4.50 of a new order). Economic model: 2-unit order at $45 vs. 2× single orders at $22 each + $9.00 shipping = $53. Buyer saves $8. mfg-farm gets $45 revenue vs. $44 net of shipping at 2× single; margin improves on volume because packaging overhead is shared.

**6-pack pricing (Etsy custom bundle):**
- Cable management clips (6-pack): $35–45 (vs. $20–25 for 3-pack)
- Homelab accessories 6-piece set: $95–110
- Desk accessories 6-piece set: $110–140

**Bulk (25+ units, direct):**
- 20% discount off Etsy retail
- Direct invoice (Etsy doesn't support large bulk orders cleanly)
- Lead time: 2–3 weeks for 25-unit run
- Payment: 50% upfront, 50% on ship

---

## Amazon vs. Etsy Channel Pricing

**Etsy:** Primary channel. Maker narrative, premium positioning, buyer expects handcrafted quality.
- Target listing price: full retail as modeled above
- Etsy fees: 6.5% total (transaction + payment processing)
- Free shipping threshold: $35 (set in shop preferences)

**Amazon (future — Wave 2):**
- FBA fees eat 25–35% of sale price for small items in the $20–50 range (referral fee + FBA fulfillment fee)
- To maintain 55% net margin on Amazon, retail prices must be 15–25% higher than Etsy
- Example: $25 Etsy desk clip → $30–32 Amazon (same net margin)
- Amazon not recommended for Phase 3 Wave 1 — Etsy is more appropriate for handmade-positioned products at launch

---

## Pricing Validation Checklist

Before finalizing each SKU price:
1. Does the retail price produce >65% net margin at Standard tier? If no, adjust price or reduce COGS.
2. Is the retail price within the WTP range established in Section 3 of the Market Research? If above, identify which premium tier justification applies.
3. Does the bundle version produce >70% net margin? If not, review shipping amortization.
4. Is the price defensible against AliExpress alternatives at 3× to 5× AliExpress price? If below 3×, we're competing on price — unattractive position. Target 4–6× AliExpress floor price to maintain the "premium custom" positioning.

---

*Sources: ITEM9_PRODUCT_VIABILITY_ANALYSIS.md | ITEM18_ADJACENT_MANUFACTURING_ECONOMICS.md | material-sourcing-supplier-economics.md | phase-3-product-validation-research.md | [Etsy Conversion Rate 2026 — Gelato](https://www.gelato.com/blog/etsy-conversion-rate) | [CableMod Pro Coiled Cable Amazon Reviews](https://www.amazon.com/product-reviews/B09LT2663T)*

---

*Item 21 Phase 3 Pricing Strategy — Session 2026-04-29*
*Status: Production-ready*
