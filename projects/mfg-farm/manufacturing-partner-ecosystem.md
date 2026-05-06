---
title: Manufacturing Partner Ecosystem — Contract, Fulfillment, QA, and Packaging Partners
project: mfg-farm
created: 2026-05-06
status: production-ready
session: Item-52
confidence: high — based on current vendor pricing (May 2026), published SLAs, and direct cost benchmarks
related: supplier-ecosystem-planning.md, 3pl-readiness-analysis.md, scaling-cost-levers.md, ITEM18_ADJACENT_MANUFACTURING_ECONOMICS.md
---

# Manufacturing Partner Ecosystem

**Lead finding:** For ModRun cable management at current and near-term scale, the partner ecosystem divides into two fundamentally different use cases. Partners that make sense now (Pirate Ship for shipping, poly mailer vendors for packaging) and partners that only become relevant at a specific volume trigger or manufacturing event (contract manufacturers for overflow, Simpl/Fulfillrite 3PLs for fulfillment outsourcing above 250 orders/month, QA inspection services for high-value new product launches). No print-on-demand partner can replicate the $0.08–$0.13/unit COGS that in-house FDM provides for ModRun's current product — outsourced FDM costs $3–15/unit for the same small parts. The correct mental model is not "find a partner to replace in-house production" but rather "maintain in-house FDM as core, identify partners for specific overflow, surge, and specialty needs."

---

## Section 1: Contract Manufacturers — FDM, SLA, and Resin

### 1.1 The Economics of Contract FDM at ModRun's Scale

The hard number to internalize first: outsourced FDM for a small plastic part comparable to a ModRun clip (roughly 16mm × 10mm × 22mm, ~5–10g) runs $3–15/unit at domestic contract manufacturers in 2026. In-house printing at 12-up plate batching costs $0.08–0.13/unit. The gap is 20–100x.

This is not a criticism of contract manufacturing — it reflects the genuine cost structure of a service bureau operating industrial equipment with overhead, labor, and margin. The implication for ModRun is that contract FDM is never appropriate as a primary production channel. It is appropriate for: (1) overflow surge production when in-house capacity is genuinely maxed out and order delays would damage Etsy standing, (2) new product prototyping for sizes or materials that ModRun's current printer cannot handle, and (3) production continuity when in-house equipment is down for repair.

**Volume at which contract FDM becomes a meaningful cost burden:** Even at the $3/unit floor, 500 units/month sourced externally costs $1,500/month in manufacturing alone versus approximately $65/month in-house (500 units × $0.13). The $1,435/month gap equals 15 Bambu P1S printers paid off annually. Contract FDM is a bridge, not a channel.

### 1.2 Domestic Contract FDM Partners

**Protolabs (protolabs.com)**
- Technology: FDM, SLA, SLS, MJF, Polyjet — broadest capability range of any domestic platform
- Minimum order: No official minimum, but pricing per part starts around $95 and the platform is designed for engineering prototypes, not consumer product production runs
- Turnaround: 1 business day for simple FDM parts, 3–5 days standard
- Quality: ISO 9001 certified. Dimensional tolerances: ±0.005 inch (±0.127mm) for FDM, better for SLA. First-article inspection included at no extra charge
- DFM feedback: Automated instant DFM analysis on upload — a genuine value-add for new products
- Cost range: $95–500+ per part for small FDM. High minimum per-part cost makes Protolabs economically unsuitable for ModRun's commodity clips, but appropriate for one-off prototypes of rail designs, custom mounting hardware, or new product validation
- **Use case for ModRun:** New product prototype validation. Budget $150–300 per part for a first-article test when evaluating a new product that would take 3–5 design iterations before production lock
- SLA (service level agreement): 24-hour turnaround on standard FDM, 2-hour quoting
- Certifications: ISO 9001, ITAR registered

**Fictiv (fictiv.com)**
- Technology: FDM, SLA, SLS, MJF, CNC — curated network model (vetted suppliers, Fictiv manages QC)
- Turnaround: 3 days typical for small parts; 1-day expedited available
- Quality: Inbound inspection on all parts, dimensional verification on critical features, 100% visual inspection
- Pricing: More competitive than Protolabs for production quantities; quote-based; small FDM parts typically $15–40/unit at 10–50 unit quantities
- DFM support: Engineering team reviews files before quoting — useful for catching orientation and tolerance issues
- **Use case for ModRun:** Medium-volume (50–200 unit) overflow runs where lead time is 3–5 days acceptable. Fictiv's inbound QC offloads inspection labor at the cost of higher per-unit price
- Network: ~1,000 vetted manufacturing partners across US, Mexico, and Asia

**Xometry (xometry.com)**
- Technology: Broadest platform — 5,000+ global manufacturing partners; 20+ processes including FDM, SLA, SLS, injection molding, CNC
- Pricing: AI-driven instant quoting; FDM small parts start around $3–8/unit at US partners, lower at Asian partners; US-only sourcing adds 40–70% cost premium vs. offshore
- Turnaround: 3–10 business days typical; expedited available
- Quality: Variable — depends on which network partner fulfills the order. Xometry reviews shop certifications but does not inspect individual shipments by default. First-article inspection is an add-on
- **Use case for ModRun:** Price-sensitive overflow where delivery in 5–10 days is acceptable and QC responsibility stays with ModRun. Xometry is the lowest-cost domestic option for functional (non-precision) FDM parts at 100–500 unit quantities
- Risk: Post-processing fee disclosure issues noted in some comparisons — quote clearly states add-on charges
- Etsy seller relevance: Xometry's speed and pricing make it viable for a second-printer failure scenario (printer down for 1–2 weeks) to maintain Etsy order fulfillment

**JLC3DP (jlc3dp.com)**
- Technology: FDM, SLA, SLS, MJF, resin — offshore (Shenzhen) with international shipping
- Pricing: Starting from $0.30/part for FDM; small cable clip equivalent: $1–3/unit at 50+ unit quantities depending on material
- Turnaround: 4–7 days production + 5–14 days international shipping; 24-hour production available with premium
- Quality: IATF 16949 certification (automotive supply chain standard — indicates systematic quality management). Dimensional accuracy ±0.2–0.3mm for FDM
- **Use case for ModRun:** Price-sensitive bulk prototyping or new product line testing where 2–3 week total lead time is acceptable. At $1–3/unit, JLC3DP is the most economical contract option for functional small parts, but overseas shipping eliminates its utility for emergency surge production
- Risk: Chinese supply chain exposure — tariff changes (current USPS tariff environment as of May 2026) may affect pricing and lead times. Never use as sole backup for time-sensitive production continuity

### 1.3 SLA and Resin Contract Manufacturing

SLA produces dramatically better surface finish and dimensional accuracy than FDM but costs 3–5x more per unit. For ModRun cable clips (under-desk, function-critical but not appearance-critical), SLA is cost-unjustified. SLA becomes relevant for ModRun only if:

1. A new product line requires transparency, jewelry-grade finish, or sub-0.1mm feature tolerance
2. A resin product prototype needs external validation before investing in in-house MSLA equipment
3. A customer-facing product justifies $15–35/unit contract SLA pricing for premium market positioning

**Protolabs SLA:** $95–200/part for small parts at standard lead time. Materials include Somos Watershed (water-clear), Accura Xtreme (ABS-like), Accura 25 (flexible)
**Xometry SLA:** $15–45/part at US shops; DLP resin options available for smaller feature sizes
**Formlabs Factory (formlabs.com/factory):** Formlabs offers a manufacturing-as-a-service channel using their Form 3L and Fuse 1+ platforms; pricing quote-based; strength is biocompatible and dental-grade resins, not relevant for cable management

**Decision rule:** Do not use external SLA for ModRun clips. Use external SLA exclusively for (1) prototype validation of a new product requiring fine surface finish before investing in in-house resin capability, budget $100–300 per validation run, and (2) specialty product line testing (transparent organizers, display pieces) where appearance justifies cost.

---

## Section 2: Print-on-Demand Fulfillment Networks

### 2.1 Why Standard POD Platforms Cannot Serve ModRun

Printful, Printify, Gooten, and similar POD networks produce their own catalog products (apparel, mugs, canvas prints, phone cases). They cannot accept externally manufactured FDM parts as inbound inventory and ship them on demand. The term "print-on-demand" in this context means the platform prints items itself — it is not a general fulfillment model for custom-manufactured goods.

Printful announced a merger with Printify in 2025, combining Printful's in-house production expertise with Printify's network of 80+ print providers. The combined entity covers 900+ product types, none of which are FDM-printed cable management parts.

**There is no mainstream POD network that fulfills FDM 3D printed consumer goods as of May 2026.** The closest analogues are:

### 2.2 3D-Print-Specific On-Demand Platforms

**Shapeways (shapeways.com)**
- Model: Upload STL → Shapeways manufactures → ships to customer or to seller's customer (white-label option)
- Technologies: MJF (Nylon PA12), SLS, FDM, full-color sandstone, precious metals
- Pricing: Volume-based; for a small functional plastic part at FDM, expect $8–20/unit. MJF PA12 (their strongest plastic option) runs $15–40/unit for small parts
- Turnaround: 5–12 business days production + shipping
- Quality: Recent expansions added FDM capability. MJF parts have excellent surface finish and strength. FDM parts through Shapeways have less consistent quality documentation than their powder-bed options
- **Use case for ModRun:** Not appropriate for commodity cable clips (margin destruction: $8–20/unit COGS vs. $0.13 in-house). Appropriate for specialty ModRun products where surface finish matters and volume is low — custom engraved desktop accessories, personalized sets, gift-market items where $30–50 price points justify outsourced manufacturing. Also useful for market testing new designs before investing in in-house production capability

**Craftcloud (craftcloud3d.com)**
- Model: Aggregator / comparison engine — uploads file, gets quotes from multiple service bureaus, selects and orders
- No proprietary production; uses a network of 100+ manufacturing partners globally
- No service fee or order minimums — key differentiator
- Pricing: Competitive; typically the lowest-price quote for a given STL comes through Craftcloud's aggregation because it includes offshore partners
- Turnaround: Varies by selected partner (24 hours to 2 weeks)
- Quality: No standardized QC — quality depends entirely on selected partner. Good for iterative design prototyping where consistency across orders is not critical
- **Use case for ModRun:** Design iteration and new product prototyping. When testing a new STL variant, Craftcloud's aggregation finds the cheapest option for a one-off test print. Do not use for production runs requiring consistent quality

**Treatstock (treatstock.com)**
- Model: Marketplace connecting buyers to local 3D printing service providers; includes both professional service bureaus and hobbyist operators
- Known issue: Algorithm modification of thin-wall features (reported 0.12mm thickening in some tests) — problematic for snap-fit parts where ModRun's 1.4mm snap arm tolerance is critical
- Pricing: Lower than Craftcloud in some cases, but quality variance is higher
- **Use case for ModRun:** Avoid for production or prototyping of snap-fit parts. The automated file repair behavior is a direct risk to ModRun's click-fit tolerance. Useful only for non-critical decorative or marketing sample prints

### 2.3 General 3PL Networks (Not POD)

For fulfillment of FDM-manufactured goods (not printing), the relevant partners are:

**Simpl Fulfillment**
- All-inclusive flat rate approximately $7/order (pick, pack, standard packaging, postage)
- No setup fees, no receiving fees for standard inbound
- Monthly minimum: $750 (~100 orders)
- Etsy integration: confirmed among 80+ channel integrations
- **Break-even for ModRun:** Only makes financial sense above 250–300 orders/month where the DIY labor cost exceeds $7/order equivalent. Below that, in-house fulfillment is cheaper

**Fulfillrite**
- Regional provider (East Coast, near Baltimore) — proximity advantage for ModRun's Maryland location
- Monthly minimum approximately $399 (~140 orders)
- Etsy integration confirmed; high satisfaction ratings from small Etsy sellers
- Per-order pricing requires direct quote
- **Break-even for ModRun:** Approximately Month 5–6 at current scaling trajectory

**ShipMonk**
- Per-order: $2.50 first item + $0.50/additional item pick fee + shipping
- Monthly minimum: ~$250 (derived from order volume minimums)
- Inbound receiving: $0.20–$0.50/unit — adds pre-packaging labor requirement back to ModRun
- **Break-even for ModRun:** Approximately Month 6–8; inbound pre-packaging requirement makes this the most labor-intensive 3PL option to onboard

For all 3PL options, the inbound requirement is the key constraint: all mainstream 3PLs require pre-packaged, individually labeled, barcode-scannable units. ModRun must pre-package every unit at production time rather than at order time when using a 3PL. This adds 60–90 seconds/unit of upstream labor but eliminates pack-and-ship time at fulfillment.

---

## Section 3: Quality Assurance Partners

### 3.1 In-House QA as Primary Model (Appropriate to Launch and Wave 2)

For FDM consumer products, meaningful QA is a visual and functional inspection protocol that any operator can perform. The investment required is in protocol design, not in outsourced inspection services. Formal third-party QA inspection is only economically justified when:

1. A buyer (wholesale, retail channel, corporate customer) requires certified inspection documentation
2. Product liability risk is elevated (structural load-bearing parts, products sold into regulated markets)
3. Production scale makes systematic sampling more efficient than 100% inspection

For ModRun cable clips at 20–500 units/month, none of these conditions apply. In-house QA is correct.

**Recommended in-house QA protocol for ModRun clips:**

| Check | Method | Pass/Fail Criteria | Time |
|---|---|---|---|
| Visual inspection | Direct examination | No stringing, no layer delamination, no warping >0.5mm | 5 sec/unit |
| Dimensional check (snap arm) | Caliper measurement, 1-in-10 sampling | Snap arm thickness 1.3–1.5mm (±0.1mm tolerance on 1.4mm nominal) | 15 sec/sample |
| Functional fit test | Install on cable/rail | Audible click engagement, clean release with 1–2 lb pull | 10 sec/unit |
| Surface finish | Touch check | No sharp protrusions, no support remnants, no edge burrs | 3 sec/unit |

Total inspection time: approximately 33 seconds/unit for 100% inspection, 15 seconds/unit with 10% dimensional sampling. At 12 units/plate, a plate inspection takes 4–7 minutes total.

### 3.2 Formal QA Partners (Wave 2+ or Wholesale Entry)

When ModRun enters wholesale channels, corporate clients, or Amazon FBA with significant inventory commits, third-party inspection becomes relevant.

**Protolabs Quality Services:** First-article inspection and dimensional reports included with standard orders; can serve as documented QC validation for a new product launch without separate inspection cost. Not applicable for ongoing production run QA.

**Bureau Veritas / Intertek / SGS (global inspection firms):** These are standard consumer product inspection firms used by brands sourcing from contract manufacturers. Typical inspection cost: $200–400/inspection day for a batch inspection at a manufacturing facility. Relevant for ModRun if production ever moves to a contract manufacturer in a facility the operator cannot personally inspect. Not relevant at current in-house scale.

**Local manufacturing inspection contractors:** Available through manufacturing associations and quality networks at $45–75/hour for on-site inspection. For a specific product launch requiring dimensional validation and sampling plan documentation, a 2-hour local inspection engagement ($90–150) provides an audit trail without formal agency fees.

**Decision rule for QA partners:** Spend zero on external QA inspection through Wave 1 and early Wave 2. Budget $150–300 for a first-article dimensional inspection report when entering wholesale or Amazon FBA for the first time — one inspection event, not ongoing. Evaluate formal QC contracts only when monthly volume exceeds 2,000 units and a buyer requires third-party certification.

---

## Section 4: Packaging Partners

### 4.1 Pirate Ship (pirateship.com) — Shipping Software and Rate Access

Pirate Ship is the correct shipping platform from day one. Zero subscription fees, access to USPS Commercial Pricing (not available at retail) including Priority Mail Cubic, and direct Etsy integration that auto-imports orders.

**Current rate benchmarks (May 2026):**
- USPS Ground Advantage, 1–4 oz, Zone 1–3: $3.50–$4.20
- USPS Ground Advantage, 1–4 oz, Zone 4–6: $4.20–$5.09
- USPS Ground Advantage, 1–4 oz, Zone 7–8: $5.09–$6.15
- Priority Mail Cubic (small items <0.5 cubic feet): $8.50–$12.00 for 1–5 lb; use only for orders where speed justifies cost
- UPS discounted rates via Pirate Ship: typically 10–20% above USPS Ground for small packages under 1 lb; use for heavy multi-unit orders above 1 lb where UPS becomes competitive

Pirate Ship advertises up to 89% off USPS retail rates. The real practical savings for a typical ModRun shipment (4 oz, average zone) is approximately 15–25% versus retail counter rates, equivalent to $0.70–$1.10/order saved.

**Etsy integration specifics:** Orders automatically import into Pirate Ship's dashboard. Batch label printing for a day's orders takes approximately 5–10 minutes. Labels print directly to any thermal printer (Rollo, DYMO 4XL) — thermal label printers are the correct equipment, not inkjet labels on standard paper.

### 4.2 Poly Mailer Vendors (Primary Packaging, Launch Through Wave 2)

Poly mailers are the correct primary packaging for ModRun clips through at least 500 units/month. Lightweight (adds minimal shipping weight), tamper-evident, water-resistant, and far cheaper than boxes for small parts.

**Recommended vendors:**

**ULINE (uline.com)**
- Best-in-class for plain/unbranded poly mailers in bulk quantities
- 6"×9" poly mailer (appropriate for 1–5 clip orders): approximately $0.05–$0.08/unit at case quantities (200–500 count)
- No minimums; ships from regional distribution centers (fast delivery, often next-day for mid-Atlantic businesses)
- **Use for:** All standard plain mailers from launch through 200 orders/month

**noissue (noissue.co)**
- Custom-printed mailers with biodegradable/compostable options
- Minimum order: 500 units for custom printing; approximately $0.35–$0.55/unit at 500 count
- Lead time: 2–3 weeks for custom printing production
- FSC-certified materials; marketing-appropriate for Etsy's environmentally conscious buyer segment
- **Use for:** Brand differentiation at 300–500 orders/month, when customer unboxing experience becomes a conversion and review driver. Not justified before 300 orders/month

**Packlane (packlane.com)**
- Custom-printed mailer boxes (not poly mailers) for premium packaging at low minimums
- No minimum order (even 1 unit available); pricing drops sharply at 50+, 100+, 250+ quantities
- Custom 6"×4"×2" mailer box: approximately $3.00–$5.00 at 25 units, dropping to $1.50–$2.50 at 100 units
- **Use for:** Gift market product variants, retail channel packaging, or multi-unit bundle presentation at Wave 2+. Not appropriate for standard Etsy fulfillment at <200 orders/month due to cost and volume

**Custom Box Makers / Novatech Packaging / 7packaging.com:**
- Higher-volume custom mailer box vendors with lower per-unit cost at scale
- Minimum order: 500–1,000 units typical; pricing $0.80–$1.50/unit at 1,000 count for simple custom print
- **Use for:** Wave 3 packaging when monthly volume makes 1,000-unit packaging runs viable

### 4.3 Insert and Accessory Packaging

For any ModRun product requiring a printed insert (installation guide, brand card, care instructions), two options:

**Moo.com / VistaPrint:** Business card-sized inserts at $35–65/250 count (~$0.14–$0.26/unit). Minimum order 50 units. Appropriate from launch for any order requiring an installation guide insert.

**Canva + local print (FedEx Office, Staples):** Design a two-sided installation/brand card in Canva, print locally at $0.15–$0.25/page. Good for low-volume launch testing before committing to minimum order quantities with a print vendor.

**Recommendation for launch:** Start with ULINE plain poly mailers + Moo.com installation insert card if needed. Add custom branding packaging when reaching 300+ orders/month and a custom packaging run (500 units minimum) becomes financially sensible.

---

## Section 5: Cost Analysis and Service-Level Comparison

### 5.1 Partner Cost Comparison Matrix

| Partner Type | Partner | Per-Unit Cost | Minimum | Turnaround | Best Use Case |
|---|---|---|---|---|---|
| Contract FDM (domestic) | Protolabs | $95–200/part | $95 | 1–3 days | New product prototype validation |
| Contract FDM (domestic) | Fictiv | $15–40/unit | ~$50 | 3 days | Overflow surge (50–200 units) |
| Contract FDM (domestic) | Xometry | $3–15/unit | None | 5–10 days | Emergency overflow, price-sensitive |
| Contract FDM (offshore) | JLC3DP | $1–3/unit | None | 9–21 days | Bulk prototype testing, non-urgent |
| POD/Specialty 3D | Shapeways | $8–20/unit (FDM), $15–40 (MJF) | None | 5–12 days | Premium product variants, gift market |
| POD/Specialty 3D | Craftcloud | Variable (lowest bid) | None | Varies | Design iteration, one-off prototypes |
| 3PL Fulfillment | Simpl | ~$7/order all-in | $750/month | Same-day pick | Wave 2 fulfillment outsourcing |
| 3PL Fulfillment | Fulfillrite | Quote required | $399/month | Same-day pick | Regional alternative; Etsy-native |
| 3PL Fulfillment | ShipMonk | $2.50 + $0.50/item + ship | $250/month | Same-day pick | High-integration option; pre-pack required |
| Shipping platform | Pirate Ship | $0 platform fee; USPS/UPS rates | None | Real-time label | Day-1 and permanent |
| Packaging (plain) | ULINE | $0.05–$0.08/mailer | Case qty | 1–3 days | Launch through Wave 2 |
| Packaging (custom) | noissue | $0.35–$0.55/mailer | 500 units | 2–3 weeks | Wave 2+ brand differentiation |
| Packaging (boxes) | Packlane | $1.50–$5.00/box | 1 unit | 1–2 weeks | Gift market, retail channel |
| QA (in-house) | Internal protocol | $0 material cost | — | Inline | All volumes below 2,000 units/month |
| QA (external) | Bureau Veritas/SGS | $200–400/inspection day | 1 day | 3–5 days | Wholesale/FBA channel entry |

### 5.2 Volume-Based Partner Selection Rules

**Phase 1 (0–$10K/month revenue, ~50–150 orders/month):**
- Shipping: Pirate Ship immediately
- Packaging: ULINE plain poly mailers
- Manufacturing: 100% in-house (Bambu P1S)
- QA: In-house visual + functional protocol
- Contract MFG partners: Protolabs for one-off prototype only
- 3PL: None — DIY fulfillment

**Phase 2 / Wave 2 ($10K–$50K/month, ~150–500 orders/month):**
- Shipping: Pirate Ship (unchanged)
- Packaging: ULINE plain + noissue custom at 300 order/month trigger
- Manufacturing: In-house primary; Xometry or Fictiv for overflow when printers are maxed for >2 consecutive weeks
- QA: In-house + one SGS inspection event at Amazon FBA entry (~$300 budget)
- 3PL: Simpl or Fulfillrite at 250–300 orders/month trigger

**Phase 3 / Wave 3 ($50K–$200K/month, 500–2,000+ orders/month):**
- Shipping: Pirate Ship or direct USPS commercial account; evaluate UPS contract at high volume
- Packaging: Custom branded mailers from high-volume vendors (500–1,000 unit runs)
- Manufacturing: Hybrid — in-house fleet for core SKUs, JLC3DP or Xometry for secondary SKUs
- QA: Systematic sampling plan with documented batch acceptance criteria; formal QC at wholesale channel entry
- 3PL: Active 3PL partner (ShipMonk, Simpl, or comparable) as primary fulfillment channel

---

## Section 6: When to Use Each Partner Type

### Decision Tree: Manufacturing Partners

```
Customer order received:
├── In-house capacity available → Print in-house (always preferred)
├── In-house at >90% utilization for >2 weeks AND backlog growing
│   ├── Lead time acceptable (5–10 days) → Xometry (lowest cost at $3–15/unit)
│   ├── Lead time tight (3 days) → Fictiv ($15–40/unit)
│   └── Emergency (<24 hours) → Protolabs ($95+/part, justified for brand protection)
└── New product prototype (no production equivalent)
    ├── Precision required OR surface finish critical → Protolabs or Fictiv SLA
    ├── Cost-sensitive, 2–3 week lead OK → JLC3DP ($1–3/unit)
    └── Aggregator comparison needed → Craftcloud (no service fee)
```

### Decision Tree: 3PL Partners

```
Current fulfillment model assessment:
├── Orders/month < 250 → DIY fulfillment (cheaper than any 3PL minimum)
├── Orders/month 250–400
│   ├── Maryland/mid-Atlantic location → Fulfillrite (proximity advantage)
│   └── National preference → Simpl ($7/order all-in, $750 minimum)
└── Orders/month 400+
    ├── Complex kitting needs → ShipMonk
    ├── High Etsy integration priority → Simpl or Fulfillrite
    └── Enterprise scale (1,000+ orders) → ShipBob or comparable
```

### Decision Tree: Packaging

```
Monthly order volume:
├── < 200 orders → ULINE plain poly mailers ($0.05–0.08/unit)
├── 200–500 orders
│   ├── Brand differentiation goal → noissue custom ($0.35–0.55/unit, 500 minimum)
│   └── Cost optimization only → Continue ULINE
└── 500+ orders OR retail/wholesale channel
    ├── Box presentation required → Packlane or 7packaging ($1–2.50/unit)
    └── Standard mailer at scale → High-volume custom vendor ($0.80–1.50/unit at 1,000 count)
```

---

## Sources

- [Protolabs 3D Printing Quality and Services](https://www.protolabs.com/services/3d-printing/quality/)
- [Fictiv: Sourcing Simplified for Custom Manufacturing](https://www.fictiv.com/)
- [Xometry Custom 3D Printing Services](https://www.xometry.com/capabilities/3d-printing-service/)
- [JLC3DP FDM 3D Printing Service](https://jlc3dp.com/3d-printing/fused-deposition-modeling)
- [Shapeways 3D Printing Services](https://www.shapeways.com/business/3d-printing-services)
- [Craftcloud 3D Printing Services](https://craftcloud3d.com/)
- [Pirate Ship Etsy Integration](https://www.pirateship.com/integrations/etsy)
- [Simpl Fulfillment](https://www.simplfulfilment.com/)
- [ShipMonk D2C 3PL](https://www.shipmonk.com/)
- [Packlane Custom Mailer Boxes](https://packlane.com/products/mailer-box)
- [noissue Custom Packaging](https://www.noissue.co/)
- [MakerStage FDM 3D Printing Cost Guide 2026](https://www.makerstage.com/resources/fdm-3d-printing)
- [Comparing Top On-Demand Manufacturing Platforms 2025](https://www.factorem.co/knowledge-hub/comparing-top-on-demand-manufacturing-platforms-for-cnc-machining-3d-printing-and-sheet-metal-fabrication)
