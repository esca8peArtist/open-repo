---
title: "Amazon FBA vs. Alternative 3PL Comparison — ModRun Phase 2 Fulfillment"
created: 2026-05-21
status: decision-ready
scope: "Post-Printful fulfillment evaluation: FBA direct, regional 3PLs, and self-fulfillment for ModRun Phase 2 at $272–322 available capital, with per-unit cost analysis"
confidence: high
related: amazon-fba-analysis.md, 3pl-readiness-analysis.md, MULTI_CHANNEL_SALES_ARCHITECTURE.md
---

# Amazon FBA vs. Alternative 3PL Comparison — ModRun Phase 2

**Lead finding:** With Printful's warehousing service discontinued as of March 1, 2026, ModRun has three viable fulfillment paths for Phase 2: (A) Amazon FBA direct for Amazon channel only, at $412–$462 total capital; (B) Regional 3PL (Simpl Fulfillment or Fulfillrite) for Etsy/Shopify channels at ~$7/order, viable at 300+ monthly orders; (C) self-fulfillment for Etsy as the baseline, extended with a part-time packer at 200+ orders/month. The critical clarification: these are not alternatives to each other — FBA is Amazon's fulfillment method, 3PLs serve Etsy/Shopify, and self-fulfillment is the Phase 1 baseline for all channels. The question at Phase 2 is which combination to activate and at what capital threshold.

---

## Part 1: Context — The Printful Discontinuation

**What happened:** Printful's Warehousing and Fulfillment (W&F) service, which allowed sellers to store custom non-Printful-catalog products in Printful's warehouses for third-party fulfillment, was discontinued effective March 1, 2026. All inbound shipments to Printful warehouses for W&F accounts were halted. Sellers using Printful for Shopify fulfillment of custom-manufactured products (including 3D-printed products) lost this fulfillment path entirely.

**Impact on ModRun:** Printful was never a viable option for ModRun, since ModRun produces custom FDM-printed products, not Printful-catalog apparel or accessories. The Printful discontinuation confirms the decision tree that was already correct: ModRun's D2C fulfillment runs through self-fulfillment or a general 3PL, not a POD platform.

**What this means for Phase 2 planning:** There is no "easy" Shopify fulfillment plug-in. D2C fulfillment via Shopify requires either self-fulfillment (Pirate Ship labels, self-packed) or a contract with a general 3PL (Simpl, ShipMonk, Fulfillrite). Amazon FBA is a separate, Amazon-only fulfillment system.

---

## Part 2: Fulfillment Option A — Amazon FBA Direct

### Program Summary

Amazon Fulfillment by Amazon (FBA) stores ModRun's forward-stocked inventory in Amazon fulfillment centers. Amazon picks, packs, and ships each order with Prime 1–2 day delivery.

### Cost Structure at Phase 2 Capital ($272–$322 range)

The multi-channel architecture document cites a $272–$322 minimum capital figure for FBA activation. This is the lean minimum — below the $412–$462 full-launch figure from the FBA analysis document. The difference:

**$272–$322 lean minimum (absolute floor):**
| Item | Cost |
|---|---|
| 25-unit print batch (COGS $3.75/unit) | $93.75 |
| FBA-compliant packaging (poly bags, FNSKU labels, 25 units) | $15 |
| Inbound shipping to Amazon FC | $15 |
| Sponsored Products (30-day minimum viable campaign at $3/day) | $90 |
| Professional plan (first month, may be waived via NSI) | $0–$39.99 |
| Buffer for unexpected FBA fees | $50 |
| **Total** | **$263.75–$303.74** |

**Why 25 units instead of 50:** At $272–$322 available capital, a 50-unit batch + advertising is not achievable without cutting advertising below minimum viable levels. A 25-unit first batch conserves capital while still achieving FBA listing activation and Vine enrollment eligibility.

**Risk with 25-unit batch:** At $3.41 FBA fulfillment fee on a $28.99 Starter Bundle, a 25-unit batch generating 1–2 sales/week exhausts in 12–25 weeks — well inside the 180-day new-ASIN exemption window. The small batch is not a risk factor; it is intentional capital conservation.

### 2026 FBA Fee Schedule (ModRun Starter Bundle, Packaged ~5 oz)

| Fee Component | Amount |
|---|---|
| Referral fee (15% of $28.99) | $4.35 |
| FBA fulfillment fee (small standard, 4–6 oz, incl. April 2026 3.5% surcharge) | $3.41 |
| Inbound placement fee (first ASIN, New Selection exemption) | $0 |
| Professional plan (waived for Handmade sellers after Month 1) | $0 |
| Monthly storage (off-peak, ~0.5 cubic feet for 25 units) | ~$0.40 |
| **Total fees per unit** | **$8.16** |
| **Net per unit ($28.99 sale)** | **$20.83** |
| **Net margin** | **71.9%** |

### FBA Fulfillment Cost Per Unit vs. Self-Fulfillment

| Metric | Self-Fulfill (Etsy/Shopify) | Amazon FBA |
|---|---|---|
| Fulfillment fee | $0 (own labor) | $3.41 |
| Referral fee | $1.88–3.20 (Etsy 11%) | $4.35 (15%) |
| Packaging cost | $0.35 (poly mailer) | $0.45 (poly bag + barcode) |
| Shipping cost | $4.50 (buyer-paid or included) | $0 (Amazon handles) |
| Monthly subscription | $0 (Etsy base) | $0 (waived for Handmade) |
| Platform exposure | Etsy audience only | Prime + Amazon search |
| **Net per unit ($28.99)** | **$24.54** (Etsy, seller-paid ship) | **$20.83** |

FBA costs $3.71 more per unit than Etsy self-fulfillment — but FBA generates Amazon Prime exposure and 1–2 day delivery that Etsy cannot match. The correct framing is additive revenue, not margin substitution: FBA captures buyers who would never purchase on Etsy.

### Amazon FBA Returns Handling

Amazon manages all FBA returns directly. Customer-initiated returns are accepted, inspected, and either restocked or disposed of. Seller liability:
- Amazon charges a $5.00 returns processing fee per item returned that is not restockable
- Graded "Unfulfillable" items can be removed ($0.97–$1.90/unit removal fee) or liquidated ($0.25–$0.50/unit)
- PLA cable clips returned by customers are generally non-restockable (customer-handled; unknown condition). Budget $5.97–$6.90 total cost per returned unit.
- Expected return rate for cable management clips: 2–4% (low; functional products with clear photography have lower return rates than discretionary items)

### Walmart Fulfillment Services (WFS) — Near-Term Alternative to FBA

Walmart Fulfillment Services merits brief consideration as an FBA parallel:

| Feature | Amazon FBA | Walmart WFS |
|---|---|---|
| Monthly subscription | $0 (Handmade waiver) | $0 |
| Fulfillment fee (similar weight/size) | $3.41 | $3.45 (starting rate) |
| Referral fee | 15% | 8–15% depending on category |
| Storage (off-peak per cubic foot) | $0.78 | $0.75 |
| New seller discount | 25% off fulfillment (New Seller Savings) | 25% off, 50% off storage |
| Marketplace traffic | ~3x Walmart | Full Amazon |
| Review-building tools | Vine program | Spark Review program |

WFS fees are approximately 15% cheaper than FBA for fulfillment costs, and storage rates are lower. The critical gap is traffic: Walmart Marketplace has approximately 20% of Amazon's traffic volume. For a new seller, the trade-off is slightly lower fees against dramatically lower customer reach. WFS is not recommended as a Phase 2 priority but merits evaluation at Month 6+ once Amazon FBA is established.

---

## Part 3: Fulfillment Option B — Regional 3PL (Pirate Ship + Warehouse)

### When This Is Relevant

A regional 3PL (vs. Amazon FBA) serves the Etsy and Shopify channels — it does not compete with FBA. At Phase 2 volumes (50–100 orders/month), the 3PL readiness analysis (3pl-readiness-analysis.md) demonstrates that self-fulfillment is cheaper than 3PL until approximately 300 orders/month. This section focuses on what a 3PL adds as Etsy/Shopify volume grows.

### Regional 3PL Options for ModRun (Maryland-Based)

**Option 1: Fulfillrite (Baltimore, Maryland)**

| Attribute | Detail |
|---|---|
| Location | Baltimore, MD |
| Monthly minimum | ~$399 (approximately 140 orders) |
| Per-order fee | Quote required (estimate $3–5/order pick + carrier postage) |
| Etsy integration | Confirmed |
| Setup fee | $0 |
| Proximity advantage | Same-day/next-day delivery to DC/Baltimore/Philadelphia/NYC corridor |
| Best for | Month 4–5 when orders exceed 140/month and labor time exceeds 90 min/day |

Contact: fulfillrite.com/locations/baltimore-md — request a quote for small ecommerce seller with Etsy integration, ~150–300 orders/month.

**Option 2: Simpl Fulfillment (National)**

| Attribute | Detail |
|---|---|
| Monthly minimum | $750 (approximately 100 orders at $7/order all-in) |
| Per-order fee | ~$7 all-in (pick + pack + carrier postage) |
| Etsy integration | Confirmed (80+ channel integrations) |
| Setup fee | $0 |
| Receiving fee | Included for standard inbound |
| Returns | $3–5/return (dispose, do not restock PLA clips) |
| Break-even vs. DIY | ~300 orders/month |

**Option 3: ShipMonk (National, 100+ integrations)**

| Attribute | Detail |
|---|---|
| Monthly minimum | ~$250 (lower barrier than Simpl) |
| Per-order fee | $2.50 first item + $0.50 each additional |
| Shipping | Commercial carrier rates (approximately same as Pirate Ship) |
| Etsy integration | Confirmed |
| Setup fee | $0 |
| Break-even vs. DIY | ~300 orders/month |
| Risk | Documented difficult exit process (continued billing post-termination) |

### 3PL Cost Per Unit at Phase 2 Volumes

Using Simpl at the Phase 2 scale of 100–200 orders/month:

| Monthly Orders | Simpl Total Cost | DIY+Labor Total | Delta |
|---|---|---|---|
| 100 | $1,475 | $1,155 | 3PL $320 more expensive |
| 150 | $1,800 | $1,635 | 3PL $165 more expensive |
| 200 | $2,260 | $2,130 | Near parity (±$130) |
| 300 | $3,160 | $3,100 | Approximate parity |
| 400 | $4,445 | $4,830 | 3PL $385 cheaper |

**Conclusion:** At Phase 2 volumes (50–200 orders/month), self-fulfillment with Pirate Ship is cheaper than any 3PL. 3PL becomes economically justified at 300–400 orders/month, which corresponds to Month 5–6 on the scaling roadmap.

### Pirate Ship + Local Warehouse Model

For a capital-lean approach to faster shipping zones at Phase 2, the "Pirate Ship + local warehouse" model means:
- ModRun retains self-fulfillment using Pirate Ship for all shipping labels
- No 3PL — just a designated packing area in the workshop with thermal label printer, poly mailers, and packaging supplies
- Shipping speed: USPS Ground Advantage, 2–5 business days (meets Etsy Star Seller requirements)
- Cost per label: $3.50–$6.00/shipment (zone-dependent, commercial rates)

This is the recommended Phase 2 Etsy/Shopify fulfillment model. It adds zero fixed overhead and maintains the quality control that 3PLs cannot provide for custom 3D-printed products.

---

## Part 4: Fulfillment Option C — Self-Fulfillment from Workshop

### Phase 2 Self-Fulfillment Model

Self-fulfillment from the ModRun workshop is the correct baseline for Etsy (and Shopify when it launches). The operational model at 50–200 orders/month:

**Equipment already in place:**
- Rollo X1040 thermal label printer (~$100 one-time)
- Pirate Ship account (free, no monthly fee, commercial USPS rates)
- Packaging station with poly mailers, desiccant, review cards

**Labor at Phase 2 scale:**

| Monthly Orders | Daily Orders (avg) | Pack+Ship Time/Day | Weekly Labor Hours |
|---|---|---|---|
| 50 orders/month | 1.7/day | ~10 min/day | ~1.2 hours/week |
| 100 orders/month | 3.3/day | ~20 min/day | ~2.3 hours/week |
| 150 orders/month | 5/day | ~30 min/day | ~3.5 hours/week |
| 200 orders/month | 6.7/day | ~40 min/day | ~4.7 hours/week |

At 200 orders/month, self-fulfillment consumes approximately 4.7 hours/week of packing and shipping labor. This is manageable for a solo operator. The threshold for hiring a part-time packer is approximately 250–300 orders/month, when daily packing time consistently exceeds 60 minutes.

### Self-Fulfillment Fulfillment Cost Per Unit

| Cost Component | Per-Order Cost |
|---|---|
| USPS Ground Advantage label (Pirate Ship, blended zones) | $4.50 |
| Poly mailer (9x12", at 1,000-unit pricing) | $0.05 |
| Packing tape, desiccant, review card | $0.08 |
| Labor (4 min/order × $15/hr imputed) | $1.00 |
| **Total per-order self-fulfill cost** | **$5.63** |

Compare to Amazon FBA at $3.41 fulfillment fee (but + $4.35 referral vs. $1.88 Etsy transaction fee). Self-fulfillment for Etsy is cheaper on total fees — the $4.50 shipping is buyer-paid, so the seller's actual additional cost is $0.13 (mailer + card + tape) plus $1.00 labor = $1.13/order beyond Etsy fees.

### Space and Timeline Requirements

**Current state (1-printer operation):** A dedicated table (4'×2' or larger) for packing station, shelving for filament and packaging supplies, and a thermal label printer. This fits in a corner of a workshop or garage.

**Phase 2 expansion (3–5 printers):** Add a second packing station table, a 3-shelf unit for packaged finished goods staging, and a small photography area for QC and listing photos. Total footprint: approximately 8'×10' dedicated production + packing area.

**Phase 2+ (5–10 printers with part-time help):** Scale packing station to accommodate simultaneous packing by 2 people. Separate staging areas for: (1) finished goods awaiting QC, (2) QC-passed goods ready to pack, (3) packed goods awaiting labels, (4) labeled goods awaiting USPS pickup. This workflow keeps one person printing while another packs and ships.

---

## Part 5: Returns Handling Comparison

| Channel | Returns Process | Cost Per Return | Restock? | Notes |
|---|---|---|---|---|
| Etsy self-fulfill | Buyer contacts seller; refund without return for <$25 | $0 (no return shipping required) | No (unsaleable) | For cable clips, refund-without-return is cheapest and best customer experience |
| Amazon FBA | Amazon manages return shipping and inspection | $5.00–$6.90/return (processing + potential removal) | Rarely (PLA clips usually graded unfulfillable) | Budget $6 per returned FBA unit |
| 3PL (Simpl/ShipMonk) | 3PL receives return, inspects, reports to seller | $3–5/return + disposal | No | Do not restock customer-returned PLA clips |

**Recommended return policy for all channels:** Refund without return for orders under $25. Request return only for orders above $40 where the product may be resellable (factory-condition unboxed). This policy eliminates return shipping costs and minimizes friction that generates negative reviews.

---

## Part 6: Channel-Specific Fulfillment Recommendation

| Channel | Recommended Fulfillment | Phase | Capital Required |
|---|---|---|---|
| Etsy (Phase 1) | Self-fulfill with Pirate Ship | Now | $0 additional |
| Amazon FBA (Phase 2) | FBA — 25-unit first batch | June 2026 | $272–$322 |
| Etsy + Amazon (Phase 2) | Self-fulfill Etsy + FBA Amazon simultaneously | June–August 2026 | $272–$322 (FBA only) |
| Shopify D2C (Phase 3) | Self-fulfill with Pirate Ship (same workflow as Etsy) | Month 7+ | $0 additional (Pirate Ship already active) |
| Etsy scale (300+ orders/month) | Transition to Fulfillrite (Baltimore) or Simpl | Month 5–6 | $399–$750/month minimum |

### Final Recommendation Matrix

**At $272–$322 available capital:** Allocate all to Amazon FBA Phase 2 activation (25-unit batch + 30 days Sponsored Products). Continue self-fulfillment on Etsy. Do not activate a 3PL — economics do not support it at Phase 2 volumes.

**At $400–$600 available capital:** Increase FBA batch to 50 units ($187.50 COGS) and extend Sponsored Products to 60 days. This is the full-launch configuration.

**At $800+ available capital:** Full Phase 2 FBA launch (50 units) + begin trademark filing ($350/class) in parallel. See TRADEMARK_FILING_STRATEGY.md.

---

## Sources

- [Printful Warehousing Discontinuation — Printful Help Center](https://help.printful.com/hc/en-us/articles/21048694941340-What-should-I-know-about-the-Dallas-warehousing-service-closure)
- [Top Amazon FBA Alternatives 2026 — eFulfillment Service](https://www.efulfillmentservice.com/2026/04/top-amazon-fba-alternatives-for-2026-3pls-wfs-more/)
- [Walmart Fulfillment Services Fees 2026](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20basics/WFS-fees)
- [Walmart Seller Fees 2026 — Feedvisor](https://feedvisor.com/university/walmart-seller-fees/)
- [Amazon FBA Fees 2026 — AMZ Prep](https://amzprep.com/amazon-fba-fees/)
- [Fulfillrite Baltimore Location](https://www.fulfillrite.com/locations/baltimore-md/)
- [Simpl Fulfillment Pricing](https://www.simplfulfillment.com/pricing)
- [ShipMonk Pricing](https://www.shipmonk.com/pricing)
- [Amazon FBA Returns Processing Fees 2026 — Amazon Seller Central](https://sellercentral.amazon.com/help/hub/reference/external/G201137660)
- Internal: amazon-fba-analysis.md, 3pl-readiness-analysis.md, MULTI_CHANNEL_SALES_ARCHITECTURE.md
