---
title: "Phase 2 Track 2 — Supply Chain & Logistics Research"
project: mfg-farm (ModRun)
created: 2026-06-28
status: production-ready
confidence: 90%
scope: >
  3PL provider comparison, fulfillment center costs, carrier economics for small packages,
  inventory management platforms, and packaging optimization. Builds on AMAZON_FBA_ALTERNATIVE_3PL_COMPARISON.md
  and PHASE_2_SUPPLY_CHAIN_DIVERSIFICATION_RESEARCH.md; does not repeat covered material.
related:
  - AMAZON_FBA_ALTERNATIVE_3PL_COMPARISON.md
  - PHASE_2_SUPPLY_CHAIN_DIVERSIFICATION_RESEARCH.md
  - supplier-economics.md
---

# Phase 2 Track 2 — Supply Chain & Logistics Research

**Lead finding**: At Phase 2 volumes (50–300 orders/month), self-fulfillment via Pirate Ship remains the economically correct choice. The 3PL break-even is 300–400 orders/month, which corresponds roughly to $8,000–10,000/month revenue on the current SKU set. Flexport's January 2026 minimum fee jump to $5,000/month eliminates it entirely for ModRun. ShipBob and Red Stag are both viable at scale but have MOQ hurdles that disqualify them until Phase 3. The fulfillment tool stack that matters now is: (1) Pirate Ship for labels, (2) Craftybase for COGS/inventory tracking, and (3) Trunk for cross-channel inventory sync once Amazon FBA is live.

---

## Part 1: 3PL Provider Comparison — Updated 2026

### Provider Matrix

| Provider | Monthly Minimum | Per-Order Cost | Etsy Integration | Amazon Integration | Best For | ModRun Verdict |
|---|---|---|---|---|---|---|
| **ShipBob** | ~$250 (Growth plan) | $2.50–4.00 pick + carrier | Yes | Yes (FBA prep available) | Small-medium products, fast-moving SKUs | Viable at 300+ orders/month; minimum is low but per-order + storage adds up quickly on slow-moving items |
| **Red Stag** | Custom quote (~$500 implied) | Higher pick/pack than ShipBob; custom rate | Yes | Yes | Heavy/fragile items needing accuracy guarantee | Not suited for lightweight cable clips — accuracy premium is wasted on sub-$25 items |
| **Flexport** | **$5,000/month (effective Jan 2026)** | Included in minimum | Yes (via Shopify) | Yes | Enterprise-scale sellers only | **Disqualified for ModRun at any Phase 2 volume** |
| **Shopify Fulfillment Network (SFN)** | $0 minimum; requires Shopify account | Custom quote | No (Shopify only) | No | Shopify D2C sellers; requires Phase 3 Shopify activation | Only relevant in Phase 3; no Etsy channel integration |
| **Fulfillrite (Baltimore)** | ~$399/month (~140 orders) | $3–5 pick + carrier | Confirmed | Yes | SMB sellers in Mid-Atlantic; geographic speed advantage | Best regional option for ModRun; activate at 150+ Etsy orders/month |
| **Simpl Fulfillment** | $750/month (~100 orders at $7/order all-in) | ~$7 all-in | Yes (80+ channels) | Yes | Multi-channel sellers wanting one 3PL | Higher minimum than Fulfillrite; break-even requires 300+ orders |
| **ShipMonk** | ~$250 | $2.50 first item + $0.50 each additional | Yes | Yes | Lower-barrier 3PL with broad integration | Documented difficult account exit; billing continues post-termination; use cautiously |

### Critical 2026 Update: Flexport's $5,000/month Minimum

Flexport raised its monthly minimum fulfillment spend from $500 (July–December 2025) to $5,000 effective January 2026. This means sellers shipping fewer than ~400 orders/month will pay the deficit. For ModRun Phase 2 (50–150 orders/month), Flexport would cost $5,000/month minimum against approximately $350–1,000 in actual fulfillment activity — making it 5–14x more expensive than self-fulfillment. Flexport is not a viable option until monthly revenue exceeds $30,000+.

### 3PL Break-Even Analysis

| Monthly Orders | Self-Fulfill Total (incl. labor) | ShipBob Estimated | Simpl Estimated | Delta (best 3PL vs. self-fulfill) |
|---|---|---|---|---|
| 50 | $580 | $875+ | $1,100 | 3PL 51–90% more expensive |
| 100 | $1,155 | $1,500 | $1,475 | 3PL 28–52% more expensive |
| 200 | $2,130 | $2,800 | $2,260 | 3PL 6–32% more expensive |
| 300 | $3,100 | $3,200 | $3,160 | Near parity |
| 400 | $4,830 | $4,445 | $4,445 | 3PL $385–385 cheaper |

**Decision gate**: Activate Fulfillrite (Baltimore) when Etsy + Amazon combined orders consistently exceed 150/month and daily packing time exceeds 45 minutes. Do not activate sooner.

---

## Part 2: Carrier Comparison for Small Packages ($5–25 items)

### 2026 Rate Environment

USPS Ground Advantage implemented a +7.8% average rate increase heading into 2026, the steepest in the carrier comparison group. Despite this, USPS remains the dominant choice for packages under 1 pound going to residential addresses.

### Carrier Decision Matrix (per shipment, blended zones, ~4 oz package)

| Carrier | Service | Approx. Rate (4 oz, Zone 4) | Residential Surcharge | Delivery Time | Best Use |
|---|---|---|---|---|---|
| **USPS Ground Advantage** | Standard | $4.50–6.70 (Zone 1–8) | **None** | 2–5 business days | Default carrier for all ModRun Etsy/Shopify orders |
| USPS Priority Mail | Expedited | $7.90–10.00 | None | 1–3 business days | For "rush" option or Prime-competing speed tier |
| UPS Ground | Standard | $9.00–14.00 after surcharges | **$6.45–6.95** | 1–5 business days | Not competitive at sub-1-lb weights; rounds up to 1 lb billing |
| FedEx Ground | Standard | $9.00–14.00 after surcharges | **$6.45–6.95** | 1–5 business days | Not competitive at sub-1-lb weights; same rounding problem as UPS |

**Key insight**: USPS Ground Advantage does not charge a residential surcharge — this is decisive for D2C ecommerce. UPS and FedEx both round up to 1 lb for billing and add a $6.45–6.95 residential surcharge, making them $4–10 more expensive per shipment than USPS for cable clips delivered to home addresses. USPS is the correct carrier for Phase 2 at all volumes.

### Shipping Platform: Pirate Ship vs. Alternatives

| Platform | API? | Carriers | Cost | Best For |
|---|---|---|---|---|
| **Pirate Ship** | No | USPS + UPS | Free | Phase 1–2 self-fulfillment; no integration needed for manual order volume |
| **Shippo** | Yes (SDKs in major languages) | 40+ carriers | $0.05/label (PAYG) or $19/month | Phase 2+ when Shopify + Etsy + Amazon orders need a unified shipping dashboard; API enables batch label generation |
| **EasyPost** | Yes | 100+ carriers | $0.08/label (3,000 free/month) | Phase 3+ custom enterprise integrations; more developer-facing than Shippo |

**Recommendation for Phase 2**: Upgrade from Pirate Ship to Shippo when Amazon FBA self-fulfilled orders (Walmart, Faire) require multi-carrier rate shopping, or when the Shopify store launches in Phase 3. Pirate Ship is adequate until 100+ daily shipments require batch API automation.

---

## Part 3: Inventory Management Platforms

### Platform Comparison Matrix

| Platform | Monthly Cost | Etsy Integration | Amazon Integration | COGS Tracking | MOQ/Maker-Focused | Best For |
|---|---|---|---|---|---|---|
| **Craftybase** | $20/month (Pro, up to 25 orders/channel) → $49/month (Studio) → $349/month (Growth) | Native import | Yes | Automatic (weighted average, GAAP-compliant) | Yes — built for handmade/maker businesses | **Recommended for Phase 1–2**; tracks filament as raw material, cable clips as finished goods |
| **Trunk** | Custom pricing | Yes | Yes | No (inventory sync only) | No | Cross-channel inventory sync when Amazon FBA + Etsy risk stock-outs from same inventory pool |
| **Sellbrite** | Custom | Yes | Yes | No | No | Multi-channel listing management at scale |
| **Zoho Inventory** | $29–349/month | Yes | Yes | Yes | Moderate | Phase 3+ when Shopify + Amazon + Etsy + Faire require unified PO/inventory management |
| **Cin7** | $349+/month | Yes | Yes | Yes | No | Not viable at Phase 2 cost; enterprise-oriented |

### Phase-Appropriate Recommendation

**Phase 1–2 (current):** Craftybase Pro ($20/month, 25 orders/channel/day) or Studio ($49/month for more). Tracks filament inventory as raw material, finished cable clips as manufactured goods, calculates COGS per batch, and imports Etsy orders automatically. When Amazon FBA activates, add Trunk ($15–40/month estimated) for real-time stock sync between Etsy + Amazon to prevent overselling.

**Phase 3+ (Shopify live, 300+ orders/month):** Evaluate Zoho Inventory or Cin7 for PO management, supplier reordering, and multi-channel fulfillment routing. At that point, Craftybase's maker-focused model may limit scalability.

---

## Part 4: Packaging Optimization

### Current Baseline (Phase 1)

Plain poly mailers (9×12") from Shop4Mailers or ULINE at $0.05–0.17/unit. Review card $0.03/unit. Desiccant $0.02/unit. Total packaging cost: $0.10–0.22/unit. This is optimal for Phase 1–2.

### Phase-by-Phase Packaging Strategy

| Phase | Volume | Packaging Type | Cost/Unit | Branding | Notes |
|---|---|---|---|---|---|
| Phase 1–2 | 50–300 orders/month | Plain poly mailer | $0.05–0.17 | None | Lowest cost; meets Etsy shipping requirements |
| Phase 2+ | 300–500 orders/month | Custom printed poly mailer | $0.25–0.50 | Logo + URL | MOQ typically 500 units; viable at this volume; $0.15–0.33 premium over plain |
| Phase 3 | 500+ orders/month | Custom branded kraft mailer or small box for bundles | $0.80–2.00 | Full brand treatment | For bundles ($40+ orders) or wholesale shipments; plain mailer stays for single-unit orders |

### Brand Investment Threshold

Custom poly mailers become cost-effective at 500 orders/month, where the per-unit cost premium of $0.15–0.33 is offset by repeat purchase rate improvements (typically 20–40% lift on repeat purchases is cited by packaging suppliers, though this is a supplier claim — treat as aspirational). At Phase 2 volumes, the cash is better deployed in ad spend than packaging branding.

### DIM Weight and Carrier Compatibility

Cable clips in poly mailers ship at actual weight (under 1 lb). USPS Ground Advantage prices by actual weight for sub-1-lb packages, eliminating DIM weight entirely. This is the optimal configuration — do not use boxes for single-unit cable clip orders, as a box adds 2–4 oz to actual weight and dramatically worsens DIM weight economics with UPS/FedEx.

---

## Sources

- [ShipBob vs Red Stag 2026 — Fit Small Business](https://fitsmallbusiness.com/shipbob-vs-redstag/)
- [Best Fulfillment Companies for Small Ecommerce 2026 — OCNJ Daily](https://ocnjdaily.com/news/2026/apr/27/best-fulfillment-companies-for-small-ecommerce-businesses-in-2026/)
- [Flexport $5,000 Monthly Minimum — Cahoot.ai](https://www.cahoot.ai/flexport-5000-minimum-fee-analysis/)
- [Flexport Raises Monthly Minimum — Supply Chain Dive](https://www.supplychaindive.com/news/flexport-fulfillment-minimum-fee-2026-increase/757128/)
- [USPS vs UPS vs FedEx 2026 — Gobolt](https://www.gobolt.com/blog/usps-vs-ups-vs-fedex-comparison/)
- [2026 UPS & FedEx Rate Hikes — Zenventory](https://www.zenventory.com/blog/blog/ups-fedex-shipping-rate-hikes-strategies)
- [Pirate Ship vs EasyPost 2026 — SelectHub](https://www.selecthub.com/shipping-software/pirate-ship-vs-easypost/)
- [Shippo vs Pirate Ship vs ShipStation 2026 — Shippo](https://goshippo.com/blog/shippo-vs-pirate-ship-vs-shipstation-how-the-top-shipping-platforms-compare)
- [Craftybase Pricing 2026](https://craftybase.com/pricing)
- [Top Etsy Inventory Management Software 2026 — LitCommerce](https://litcommerce.com/blog/etsy-inventory-management/)
- [Trunk Inventory Sync — Etsy/Amazon](https://www.trunkinventory.com/sync-amazon-etsy-inventory)
- [eCommerce Packaging Guide 2026 — Atomix Logistics](https://www.atomixlogistics.com/blog/guide-ecommerce-packaging)
- [Custom Poly Mailers vs Boxes — aplasticbag.com](https://blog.aplasticbag.com/custom-poly-mailers-vs-shipping-boxes-which-saves-more-money/)

*Research completed June 28, 2026. Builds on AMAZON_FBA_ALTERNATIVE_3PL_COMPARISON.md (May 2026) — does not repeat 3PL cost-per-unit tables already computed there.*
