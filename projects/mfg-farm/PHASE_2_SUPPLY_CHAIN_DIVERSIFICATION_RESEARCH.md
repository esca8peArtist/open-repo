---
title: Phase 2 Supply Chain Diversification Research — Item 25
project: mfg-farm (ModRun / Etsy Print Farm)
created: 2026-06-23
session: 4100
status: production-ready
confidence: 88%
scope: >
  Five vendor categories researched: PLA+ filament (extends prior work), resin suppliers,
  carbon fiber and advanced materials (new), shipping/packaging materials (extended), and
  payment processors (new). All data verified against public sources June 2026.
  Complements existing PHASE_2_TRACK_1_SUPPLY_CHAIN_DIVERSIFICATION.md with deeper
  coverage of previously thin categories.
related:
  - PHASE_2_TRACK_1_SUPPLY_CHAIN_DIVERSIFICATION.md
  - supply-chain-diversification-strategy.md
  - PHASE_2_SUPPLIER_PRESTAGING_STRATEGY.md
  - post-test-print-doc-5-supplier-contact-matrix.md
---

# Phase 2 Supply Chain Diversification Research

**Lead finding**: The five-category supply chain is largely de-risked for filament (dual-source architecture built in prior sessions). The three remaining gaps — carbon fiber / advanced materials, packaging cost optimization at low volumes, and payment processor lock-in awareness — are addressed here. On payment processing: Etsy Payments is mandatory and non-substitutable; Stripe and PayPal comparisons are relevant only for non-Etsy channels (Shopify, direct website). On carbon fiber: the material commands a 3–4× cost premium over standard PLA ($48–55/kg vs. $12–15/kg) and requires a hardened nozzle, making it a Phase 3+ specialty tier SKU rather than a Phase 2 production material. On packaging: at the 10–100 unit order volumes relevant to Phase 1/early Phase 2, plain poly mailers (from Shop4Mailers or ULINE) remain the clear cost winner at $0.05–0.17/unit; custom branded boxes are viable at 250+ units for ~$1.00–3.33/unit.

---

## Category 1: PLA+ Filament Suppliers

> **Status**: Covered in depth in PHASE_2_TRACK_1_SUPPLY_CHAIN_DIVERSIFICATION.md and PHASE_2_SUPPLIER_PRESTAGING_STRATEGY.md. This section summarizes and extends with geographic diversity and tariff-immunity ranking.

### Vendor Matrix

| Vendor | $/kg (10kg tier) | $/kg (50kg tier) | MOQ | Lead Time | Quality / Certs | Geography | Risk Score (1–10 low=good) | Tariff Immunity |
|---|---|---|---|---|---|---|---|---|
| **eSUN** | $12–13 | ~$10 (direct) | 1kg (Amazon) | 1–5 days | ±0.03mm; AMS 9/10; vacuum sealed varies | China (US stock via Amazon) | 3 | None — Chinese origin |
| **Anycubic** | $10.49 | $10.49 (50kg pallet) | None | 3–7 days | ±0.04mm; AMS 7/10 (winding reports) | China (direct ship) | 4 | None — Chinese origin |
| **Polymaker** | $14.99 | $14.99 (~5–10% vol. disc.) | $1,000 order | 3–5 days | ±0.02mm; AMS certified; vacuum/foil | **US warehouse (Houston, TX)** | 2 | **Full — US-warehoused** |
| **SUNLU** | $10.26–12 | No listed tier | 6kg | 3–7 days | AMS 6.5/10; mix-match colors | China | 5 | None |
| **Overture (PLA)** | $12–14 | Up to 35% via wholesale | None (Amazon) | 2–5 days | AMS 8/10; ±0.02mm | China / US Amazon stock | 3 | Partial (US Amazon stock) |
| **Push Plastic** | ~$22–25 | Contact for bulk | 1 spool | 3–5 days | US-made (NatureWorks PLA); ±0.05mm | **USA (Springdale AR)** | 2 | **Full — domestically made** |
| **MatterHackers Build PLA** | $19–23 | Business acct. discount | 1 spool | 2–4 days | NatureWorks 4043D; ±0.03mm | **US domestic** | 2 | **Full — domestic** |
| **Polar Filament** | ~$18.99 | 3+ spools free shipping | 1 spool | 3–5 days | NatureWorks PLA; confirm AMS test | **USA (Michigan)** | 2 | **Full — domestic** |

### Top Recommendations

1. **Primary**: eSUN 10kg Amazon bundles — speed, reliability, cost. Reorder at 2-week inventory level.
2. **Volume/cost leader**: Anycubic 50kg pallet ($10.49/kg) after AMS validation test. Saves ~$0.34/kg vs. eSUN bundles.
3. **Tariff hedge / quality tier**: Polymaker wholesale (Houston, TX) activated at 50+ kg/month. Full tariff immunity.

### Price Sensitivity (3-clip bundle @ $28.99 retail, 75g/bundle)

| Scenario | $/kg | Material cost | COGS | GM% | vs. baseline |
|---|---|---|---|---|---|
| Retail eSUN | $15.00 | $1.13 | $8.87 | 69.4% | baseline |
| eSUN 10kg bundle | $12.50 | $0.94 | $8.68 | 70.0% | +0.6 pts |
| Anycubic 50kg pallet | $10.49 | $0.79 | $8.53 | 70.6% | +1.2 pts |
| eSUN direct wholesale | $10.00 | $0.75 | $8.49 | 70.7% | +1.3 pts |
| Polymaker wholesale | $14.99 | $1.12 | $8.86 | 69.4% | -0.0 pts (quality offset) |

Note: Margin impact of supplier choice is secondary to bundle AOV strategy. Shipping ($5–5.50) dominates COGS at single-clip orders.

### Category Risk Assessment

- **Concentration risk**: Medium-high. Both primaries (eSUN, Anycubic) are Chinese-origin. Tariff escalation of 15%+ adds $0.15–0.23/unit.
- **Mitigation**: Maintain Polymaker wholesale relationship as tariff backstop; stock 4-week buffer in all production colors.
- **Geopolitical risk**: Active in 2026 (US-China trade tensions). Push Plastic and Polar Filament are domestic activations at +$10–12/kg premium — justified only above 20%+ tariff increase.

---

## Category 2: Resin Suppliers (Anycubic i3 MegaS Compatible)

> **Note**: The Anycubic i3 MegaS is an FDM (filament) printer, not a resin (MSLA/SLA) machine. This section covers resin suppliers for potential future resin printer (e.g., Anycubic Photon series) expansion. Resin printing is a Phase 4+ consideration per PHASE_2_TRACK_1_SUPPLY_CHAIN_DIVERSIFICATION.md. Data here focuses on the most cost-effective resin suppliers if a resin printer is added to the farm.

### Vendor Matrix

| Vendor | Resin Type | $/L (single) | $/L (bulk 10L+) | MOQ | Lead Time | Key Notes | Risk Score |
|---|---|---|---|---|---|---|---|
| **Elegoo** | Standard, ABS-Like V2, Plant-Based | ~$20–25/L | ~$18–22/L (10kg) | 1 kg | 3–7 days (US warehouse) | Best commodity access; 10kg grey ABS-Like ~$199–$320; wide compatibility | 3 |
| **Anycubic** | Standard V2, Colored UV, ABS-Like | ~$13–22/L | ~$13–18/L (multi-pack) | 1 kg | 3–10 days | Best price for bulk multi-pack bundles; Photon ecosystem native | 3 |
| **Siraya Tech** | ABS-Like Fast, Blu Tough (impact), Sculpt (high-temp), Clear | ~$48–58/L | ~$55–72/L (5kg bulk) | 1 kg retail; 5 kg bulk | 5–14 days (US + intl) | Best specialty tier: Blu Tough 5kg ~$360 ($72/L); impact-resistant, high-heat; open platform | 2 |
| **Formlabs** | Engineering resins (Tough 2000, Flexible 80A, Draft) | $150–300/L | Quote required | 1 L | 2–5 days | Premium engineering properties; requires Form 4 printer ($3,499+); not compatible with open-platform printers | 4 |

### Top Recommendations

- **If activating commodity resin (Phase 4)**: Elegoo ABS-Like (sub-$25/L) as primary; Anycubic as secondary.
- **If activating specialty resin (Phase 4+ premium line)**: Siraya Tech Blu Tough (impact-resistant, $72/L) for functional parts requiring better mechanical properties than standard resin.
- **Do not activate**: Until FDM monthly revenue exceeds $10K consistently. Resin requires additional hardware ($300–600 MSLA printer), ventilation, PPE, and waste handling infrastructure.

### Safety / Handling Requirements (for planning)

- All UV resins require nitrile gloves, UV-protective eyewear, ventilation, and UV-safe disposal
- Resin waste (IPA wash, failed prints) is hazardous — cannot go in household trash; requires local chemical disposal
- Storage: dark location, 10–30°C, shelf life 12 months sealed / 3 months open
- Fire risk: UV resins are not flammable under standard conditions; IPA wash solvent is flammable — store separately

### Category Risk Assessment

- **Risk**: Low (Phase 4+ trigger means no near-term exposure)
- **Mitigation**: No action needed until $10K/month FDM revenue confirmed

---

## Category 3: Carbon Fiber and Advanced Materials

> **New category — not previously documented in mfg-farm research.**

### Context and Rationale

Carbon fiber reinforced PLA (PLA-CF) and glass fiber reinforced PLA (PLA-GF) offer significantly higher stiffness and surface hardness than standard PLA. For ModRun cable clips, the use case is: premium "Pro" variant for industrial or high-load-bearing installations, or as a visual differentiator. The material commands a 3–4× price premium and requires hardened steel nozzles (0.4mm or 0.6mm hardened) to prevent accelerated nozzle wear.

**Critical hardware note**: Carbon fiber and glass fiber filaments are highly abrasive. Standard brass nozzles (as shipped on Bambu P1S) wear out in 10–50 hours on CF/GF materials vs. 600–800 hours on standard PLA. Hardened steel nozzles are required for any CF/GF production run. Bambu Lab sells P1S-compatible hardened steel 0.4mm nozzles (~$5–7 each). Budget for 2–3× nozzle replacement rate vs. standard PLA.

### Vendor Matrix — Carbon Fiber PLA (PLA-CF)

| Vendor | Product | $/kg (1 spool) | $/kg (bulk) | MOQ bulk | Lead Time | AMS Compat. | Key Notes | Risk Score |
|---|---|---|---|---|---|---|---|---|
| **eSUN ePLA-CF** | Carbon fiber PLA, matte texture | ~$32–38/kg (1kg) | ~$28–35/kg (10kg est.) | 10kg (direct) | 3–7 days | 6/10 (CF is harder on AMS) | Established eSUN quality; German-imported CF fibers; flexural modulus 3,552 MPa; widely available on Amazon | 3 |
| **Hatchbox PLA-CF** | Carbon fiber PLA, standard | $48/kg (1kg) | No public bulk tier | 1 spool | 1–2 days (Amazon Prime) | 6/10 | Fast availability; premium pricing; ±0.05mm tolerance | 3 |
| **Atomic Filament CF Extreme** | Carbon fiber PLA, high-fill | $49.99/kg (1kg) | 3.5kg spool available | 1 spool | Contact for bulk | 5/10 | US-based (CA); highest CF content; sales@atomicfilament.com; 818-583-0004 | 2 |
| **Overture Matte CF Black** | Carbon fiber matte PLA | ~$25–30/kg est. | Bulk offer (stacked bundles) | 1 spool | 2–5 days | 7/10 | More economical CF option; confirm AMS suitability before production | 3 |
| **SigmaFilament (CF-PLA)** | Carbon fiber PLA wholesale | Contact for quote | 30–50% off at 100+ spools | 100 spools | 5–35 days (FOB/DDP) | Unknown | China-based wholesale; requires AMS validation; sales@sigmafilament.com | 5 |
| **Polymaker Fiberon PA12-CF10** | Carbon fiber nylon (PA12) | ~$87/kg (0.5kg spool) | Wholesale inquiry req. | Contact | 3–5 days | 5/10 | Not PLA — Nylon 12 base; significantly higher strength and heat resistance; overkill for cable clips but relevant for industrial SKU | 2 |

### Vendor Matrix — Glass Fiber Reinforced (PLA-GF / Nylon-GF)

| Vendor | Product | $/kg (1 spool) | Key Properties | AMS Compat. | Notes |
|---|---|---|---|---|---|
| **eSUN ePLA-GF** | 16% glass fiber PLA | ~$25–35/kg (est.) | +40% stiffness vs. PLA; better dimensional stability | 6/10 | US Amazon availability; confirm current pricing; esun3d.com/epla-gf-product/ |
| **3DXTech FibreX ABS+GF** | 30% glass fiber ABS | $55/kg (1kg) | Industrial-grade; not PLA-compatible profiles | 3/10 | Best for high-temp applications; not drop-in for standard PLA clip profiles |
| **3DXTech FIBREX Nylon PA6+GF30** | 30% glass fiber nylon | $56–138/kg | Highest stiffness/strength; requires enclosed printer | 3/10 | Engineering-grade; significant profile change from PLA; nozzle temp 260–280°C |

### Top Recommendations

1. **If launching CF variant (Phase 3+ only)**: eSUN ePLA-CF as primary (established supplier, AMS experience, Amazon availability). Validate first with 1kg test spool before any production commitment.
2. **US-domestic option**: Atomic Filament (Chatsworth, CA) — highest CF content, established US brand, direct sales channel.
3. **Glass fiber**: eSUN ePLA-GF as the most accessible GF option; 3DXTech for industrial-grade engineering specs only if customer spec requires it.

### Performance vs. Cost Tradeoff

| Material | $/kg | Flexural Modulus (MPa) | Hardness | Nozzle life (hrs) | Best Use Case |
|---|---|---|---|---|---|
| Standard PLA+ | $10–15 | ~2,200 | Good | 600–800 (brass) | All current production |
| PLA-CF | $30–50 | 3,500–4,500 | Excellent | 10–50 (brass); 200–400 (hardened) | Premium industrial clip SKU |
| PLA-GF | $25–35 | 3,000–4,000 | Very good | 20–80 (brass); 150–300 (hardened) | Mid-tier strength upgrade |
| Nylon-CF (PA12-CF) | $80–100 | 5,000–7,000 | Superior | 50–150 (hardened) | High-load industrial / machine-guard clips |

### Category Risk Assessment

- **Risk**: Low near-term (no Phase 2 activation planned)
- **Material availability**: All CF filament is readily available; no stockout risk for test orders
- **Cost risk**: CF materials are 3–4× more expensive; margin on CF SKU must be modeled separately before activation
- **Hardware risk**: Nozzle wear is the primary operational risk; budget 3× nozzle replacement rate vs. standard PLA

---

## Category 4: Shipping Materials and Packaging

> **Extends prior work in PRE_PRODUCTION_SUPPLY_CHAIN_RISK_MITIGATION.md. New focus: cost-per-unit at 10–100 unit order sizes, custom printing economics, void fill comparison, and insert card pricing.**

### 4a. Poly Mailers (Primary Shipping Material)

| Vendor | Size | $/unit @ 100 | $/unit @ 500 | $/unit @ 1,000 | MOQ | Lead Time | Notes |
|---|---|---|---|---|---|---|---|
| **Shop4Mailers** | 9×12" 2.5mil | ~$0.07 | ~$0.06 | ~$0.05–0.06 | 100 | 3–5 days | Volume leader; standard 2.5mil poly; shop4mailers.com |
| **ULINE S-3352** | 6×9" tear-proof | $0.17 | $0.14 | $0.13 | 100 (1 case) | 1–3 days | More durable, professional; 14 US distribution centers; uline.com |
| **Amazon bulk (Ruspepa etc.)** | 6×9" or 9×12" | $0.07–0.10 | $0.05–0.08 | N/A | 100 | 1–2 days Prime | Zero lead-time risk; quality varies by brand; useful for emergency fill |
| **Interplas** | 6×9" to 10×13" | ~$0.08 | $0.07 | $0.05–0.06 | 1,000 | 3–5 days | Activate at 150+ orders/week; interplas.com |

**Recommendation**: Amazon bulk for Phase 1 (simplicity, Prime speed). ULINE for Phase 2 (unit economics improve at 5-case quantities). Shop4Mailers for Phase 3 volume (sub-$0.06/unit at scale).

### 4b. Mailer Boxes (Custom and Plain)

| Vendor | Type | $/unit @ 25 | $/unit @ 100 | $/unit @ 500 | MOQ | Lead Time | Notes |
|---|---|---|---|---|---|---|---|
| **MrBoxOnline** | Plain kraft mailer | ~$0.85 | ~$0.63 | ~$0.45 | 25 | 3–5 days | Best cost for plain bulk boxes; mrboxonline.com |
| **Amazon (RetailSource)** | Plain kraft | $0.40–0.80 | $0.40–0.70 | N/A | 25 | 1–2 days Prime | Emergency fill; quality acceptable |
| **ULINE corrugated mailers** | Self-sealing corrugated | $0.75–0.85 | $0.65–0.75 | N/A | 25 | 1–3 days | Professional grade; same-day ship from 14 centers |
| **Packlane** | Custom printed mailer | ~$4.50+ | ~$2.50–3.00 | $1.00–1.50 | 1 | 10–14 days | MOQ 1 unit (use for prototypes); $3.33/unit at 250 qty confirmed; packlane.com |
| **EcoEnclose** | Custom recycled | ~$2.00–3.00 | $1.50–2.50 | $1.00–1.50 | 100 | 10–15 days | 100% recycled + soy ink; $95–800 one-time plate fee; ecoenclose.com |
| **noissue** | Custom eco mailer/box | ~$3.00–5.00 | $2.00–3.00 | $1.00–2.00 | 25 | 10–14 days | Compostable options; sustainability branding; noissue.co |

**Recommendation by phase**:
- Phase 1 (1–50 orders/week): MrBoxOnline plain kraft for rail orders; Amazon Prime as backup
- Phase 2 (50–200 orders/week): Custom boxes at Packlane (250+ unit run at ~$1.00–3.33/unit) for bundles; plain for singles
- Phase 3 (200+ orders/week): EcoEnclose for sustainability narrative alignment with Etsy buyers

### 4c. Void Fill

| Material | $/shipment (est.) | Cost per cu ft | Eco rating | Notes |
|---|---|---|---|---|
| **Crinkle paper / kraft tissue** | $0.03–0.08 | $0.20–0.40/lb | Good | Best for cable clip boxes; low weight, easy sourcing; Amazon or ULINE |
| **Air pillows (pre-inflated)** | $0.05–0.15 | $0.05–0.10/cu ft | Moderate | Best cost per cu ft; higher upfront machine cost ($200–400); suited for Phase 3+ volume |
| **Recycled packing peanuts** | $0.08–0.15 | $0.15–0.25/cu ft | Poor (EPS) | Cheapest per-unit but customer perception negative; biodegradable PEA starch peanuts available at ~2× cost |
| **Honeycomb paper** | $0.10–0.20 | $0.50–0.80/lb | Excellent | Premium eco option; differentiates unboxing; available from ULINE, EcoEnclose, noissue |
| **Bubble wrap (perforated)** | $0.05–0.12 | $0.30–0.50/roll | Poor | Works for fragile inserts; plastic waste; avoid for eco-brand alignment |

**Recommendation**: Crinkle paper (kraft-colored) for Phase 1–2 cable clip boxes. Low cost, positive unboxing feel, zero customer complaints. Activate honeycomb paper at Phase 3 if premium/eco positioning is confirmed.

### 4d. Tissue Paper

| Vendor | $/sheet @ 25 | $/sheet @ 100 | $/sheet @ 500 | MOQ | Notes |
|---|---|---|---|---|---|
| **Amazon bulk (plain white)** | ~$0.05 | ~$0.03 | ~$0.02 | 100 sheets | Generic; adequate for Phase 1 |
| **noissue custom (compostable)** | N/A | ~$0.35–0.55 | ~$0.25–0.40 | 25–50 sheets | 100% compostable, soy ink; logo printed; low MOQ; noissue.co |
| **EcoEnclose custom** | N/A | N/A | $0.25–0.45/sheet | 500 sheets | Recycled + soy ink; plate fee; ecoenclose.com |

**Recommendation**: Plain white Amazon tissue for Phase 1. noissue custom at 25-sheet MOQ for Phase 2 branded unboxing testing before committing to 500+ sheet EcoEnclose run.

### 4e. Thank You Cards / Insert Cards

| Vendor | $/card @ 100 | $/card @ 250 | $/card @ 500 | MOQ | Lead Time | Notes |
|---|---|---|---|---|---|---|
| **Amazon bulk (pre-printed)** | $0.09–0.15 | N/A | N/A | 50–100 | 1–2 days Prime | Generic "thank you" cards; 2×3.5", 14pt cardstock; no branding |
| **VistaPrint custom** | ~$0.50–0.80 | ~$0.35–0.50 | ~$0.25–0.35 | 25 | 5–10 days | Full custom; online design tool; vistaprint.com |
| **Moo.com (postcards)** | ~$0.70–1.00 | ~$0.50–0.65 | ~$0.35–0.45 | 25 | 5–7 days | Premium stock/finish; brand-quality differentiation; moo.com |
| **Canva + local print** | ~$0.10–0.20 | ~$0.08–0.12 | ~$0.06–0.10 | 1 | 1–3 days (local) | Canva design ($0) + Staples/OfficeMax local print; lowest cost custom option |
| **Packhelp thank-you cards** | ~$0.40–0.60 | ~$0.30–0.45 | ~$0.20–0.35 | 25 | 7–14 days | Eco-options available; packhelp.com |

**Recommendation**: Canva design + Staples local print for Phase 1 (lowest cost, immediate turnaround). VistaPrint for Phase 2 at 250–500 card runs. MOO for premium-tier SKU packaging once revenue justifies.

### Category Risk Assessment (Packaging)

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Amazon poly mailer stockout | Low | Low | ULINE same-day order |
| Custom box lead-time failure | Medium | Medium | 14-day buffer order ahead of expected need; plain boxes as immediate backup |
| Packaging cost inflation | Low | Low | All materials commodity; multiple domestic suppliers; no concentration risk |
| Eco-packaging premium vs. margin | Medium | Low | Phase-gate custom packaging; don't activate until revenue justifies $1.00+/unit premium |

---

## Category 5: Payment Processors

> **New category — critical architecture decision for multi-channel Phase 2 expansion.**

### 5a. Etsy Channel (Mandatory: Etsy Payments)

**Key finding**: Etsy Payments is mandatory for all eligible sellers. Stripe and PayPal cannot be substituted as standalone payment processors on Etsy. Sellers cannot opt out. Etsy integrated Stripe as backend infrastructure in May 2025 for buyer bank payments (Link), but this is invisible to sellers — they receive Etsy Payments terms only.

| Processor | Fee Structure | Payout Speed | International | Chargeback Handling |
|---|---|---|---|---|
| **Etsy Payments (mandatory)** | 3% + $0.25 per transaction (payment processing) + 6.5% transaction fee + $0.20 listing fee | Daily / weekly / biweekly / monthly (seller choice) | Automatic currency conversion; no action required | Etsy responds on behalf of seller; seller may bear cost if dispute lost; no flat chargeback fee disclosed |

**Total Etsy fee per sale (example: $28.99 3-clip bundle + $5 shipping):**
- Listing fee: $0.20
- Transaction fee: 6.5% × $33.99 = $2.21
- Payment processing: 3% × $33.99 + $0.25 = $1.27
- **Total Etsy fees: $3.68 on $33.99 gross = 10.8%**

**Payout options**: Etsy deposits to linked bank account on chosen schedule. New shops may have a reserve period (typically 90 days or first 3 months). Established shops receive daily deposits by default.

### 5b. Non-Etsy Channels (Shopify, Direct Website, Amazon)

For Phase 3 multi-channel expansion (Shopify direct, Amazon MCF), payment processor choice matters:

| Processor | Standard Fee (US) | Payout Speed | International | Chargeback Fee | Best For |
|---|---|---|---|---|---|
| **Stripe** | 2.9% + $0.30 | 2 business days (standard); instant (1.5% fee) | 1.5% + currency conversion (1–2%); strongest intl. coverage | $15/dispute (flat) + optional Chargeback Protection (~0.4% of charge value) | Shopify, direct website, API-driven high volume |
| **Square** | 2.9% + $0.30 (online); 2.6% + $0.10 (in-person) | 1–2 business days; same-day (1.5% fee) | Limited intl. support; US-centric | $0 fee but seller bears dispute cost | In-person craft fairs, markets; point of sale |
| **PayPal** | 3.49% + $0.49 (standard online) | Instant to PayPal balance; 1–3 days to bank | 4.5% + fixed fee for cross-border | $20/dispute | Buyer trust signal; already in Etsy ecosystem for buyers; secondary channel only |
| **Etsy Payments (standalone)** | 3% + $0.25 (US) | Scheduled (daily to monthly) | Automatic conversion | Etsy manages | Etsy channel only — not applicable elsewhere |

### 5c. Recommendation by Channel

| Channel | Recommended Processor | Rationale |
|---|---|---|
| **Etsy** | Etsy Payments (no choice) | Mandatory. Fees are competitive with Stripe for small transactions. |
| **Shopify website (Phase 3)** | Stripe | Lower chargeback fee; best API/webhook integration; Shopify Payments is Stripe-powered anyway |
| **Amazon** | Amazon Pay (native) | No choice — Amazon handles payments natively |
| **Craft fairs / in-person** | Square | Best in-person rate (2.6% + $0.10); free card reader |
| **International buyers (direct)** | Stripe | Best intl. card coverage; automatic currency handling |

### 5d. Category Risk Assessment

- **Concentration risk**: High on Etsy (all revenue through one platform = one payment processor)
- **Mitigation**: Phase 2 Shopify direct website diversifies payment processor exposure and captures buyers who prefer not to pay through Etsy
- **Reserve risk**: New Etsy shops face payment reserves for 90+ days. Ensure cash flow projection accounts for 25–50% reserve on first 2 months of revenue.
- **Chargeback risk**: Etsy manages disputes; seller bears cost only if dispute lost. Stripe ($15/chargeback) is lower than PayPal ($20). For low-volume Phase 1, this is negligible (<1% of orders).

---

## Cross-Category Summary: Top Recommendations by Phase

| Phase | Filament | Resin | Carbon Fiber | Packaging | Payment |
|---|---|---|---|---|---|
| **Phase 1 (now)** | eSUN Amazon 10kg; Anycubic backup | None | None | Amazon poly mailers + MrBoxOnline kraft; Amazon thank-you cards | Etsy Payments only |
| **Phase 2 (2-printer, $1.5K+/mo)** | eSUN + Anycubic dual-source; Polymaker white/grey | None | None | ULINE poly mailers; Packlane custom 250-unit run; VistaPrint cards | Etsy Payments + Stripe for Shopify |
| **Phase 3 (3+ printers, $5K+/mo)** | eSUN direct wholesale + Anycubic + Polymaker blended | Elegoo + Anycubic commodity if resin printer added | eSUN ePLA-CF for premium SKU | EcoEnclose custom; noissue tissue; MOO insert cards | Etsy + Stripe + Square (craft fairs) |
| **Phase 4 (farm scale, $10K+/mo)** | Full multi-vendor blended stack; Push Plastic domestic hedge | Siraya Tech for specialty | Atomic Filament CF + 3DXTech GF | Custom unboxing kit standard | All channels active |

---

## Sources

- [eSUN ePLA-CF Product Page](https://www.esun3d.com/epla-cf-product/)
- [eSUN ePLA-GF Product Page](https://www.esun3d.com/epla-gf-product/)
- [Hatchbox Carbon Fiber PLA — $48/kg](https://www.hatchbox3d.com/products/3d-pla-1kg1-75-carbon)
- [Atomic Filament CF Extreme Black PLA — $49.99/kg](https://atomicfilament.com/products/carbon-fiber-extreme-pla-filament)
- [SigmaFilament Wholesale Carbon Fiber](https://sigmafilament.com/wholesale-carbon-fiber-filament/)
- [SigmaFilament Bulk 3D Printer Filament Guide 2026](https://sigmafilament.com/bulk-3d-printer-filament/)
- [3DXTech Glass Fiber Reinforced Filament](https://www.3dxtech.com/collections/glass-fiber)
- [Polymaker Fiberon PA12-CF10 — Wholesale](https://us-wholesale.polymaker.com/products/polymide-pa12-cf)
- [Overture Carbon Fiber Filament](https://overture3d.com/products/overture-carbon-fiber-filament)
- [Elegoo Resin Store](https://us.elegoo.com/collections/resin)
- [Siraya Tech Bulk Resin](https://siraya.tech/collections/sirayatech-buy-in-bulk)
- [Packlane Custom Mailer Boxes](https://packlane.com/products/mailer-box)
- [EcoEnclose Custom Packaging](https://www.ecoenclose.com/eco-friendly-custom-packaging/)
- [noissue Custom Tissue Paper](https://noissue.co/custom-packaging/custom-printed-tissue-paper/)
- [Shop4Mailers Poly Mailers](https://www.shop4mailers.com/)
- [ULINE Poly Mailers S-3352](https://www.uline.com/Product/Detail/S-3352/Poly-Mailers/Tear-Proof-Polyethylene-Mailers-6-x-9)
- [EcoPackables Packaging Cost Guide 2026](https://www.ecopackables.com/blogs/news/how-much-does-packaging-cost)
- [VistaPrint Packaging Insert Cards](https://www.vistaprint.com/marketing-materials/packaging-inserts)
- [Packhelp Thank You Cards](https://packhelp.com/p/thankyou-cards/custom/)
- [Etsy Payment Processing Fees 2026 — ListingForge](https://www.listing-forge.com/blog/etsy-payment-processing-fees)
- [Etsy Fees Complete Breakdown — Craftybase](https://craftybase.com/blog/the-complete-guide-to-etsy-fees)
- [Etsy Payments Policy — Etsy](https://www.etsy.com/legal/etsy-payments/)
- [Stripe vs PayPal vs Square Fee Comparison](https://globalfeecalculator.com/blog/stripe-vs-paypal-vs-square/)
- [Etsy Partners with Stripe — Stripe Blog](https://stripe.com/customers/etsy-spotlight)
- [Etsy Payments Is Mandatory — Synder Guide](https://synder.com/blog/etsy-paypal/)
- [Push Plastic Bulk Pricing](https://www.pushplastic.com/pages/bulk-pricing)
- [Polar Filament (Michigan domestic)](https://polarfilament.com)
