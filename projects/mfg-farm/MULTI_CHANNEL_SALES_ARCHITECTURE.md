---
title: "Multi-Channel Sales Architecture — ModRun Manufacturing Farm"
created: 2026-05-21
status: production-ready
scope: "Platform comparison, fee analysis, feature parity matrix, and channel activation roadmap for Etsy → Amazon FBA → Shopify D2C expansion"
confidence: high
related: amazon-fba-analysis.md, ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md, ETSY_SEO_STRATEGY_Q2_Q3_2026.md, AMAZON_FBA_READINESS_CHECKLIST.md, SHOPIFY_PRINTFUL_INTEGRATION_GUIDE.md, UNIFIED_INVENTORY_MODEL.md
---

# Multi-Channel Sales Architecture — ModRun

**Lead finding:** Etsy is the correct and only launch channel for ModRun through the first 90 days. Amazon FBA becomes worth activating at 50+ units/month with $400+ capital available. Shopify D2C is a Phase 3 investment — it generates higher per-unit margin and owns customer data, but the customer acquisition cost burden ($55–$75 blended D2C CAC) makes it uneconomic before Etsy has built a brand foundation and review base. The sequencing is not a preference — it is a capital efficiency calculation. Running all three simultaneously at launch guarantees under-execution in all three rather than excellence in one.

---

## Part 1: Platform Overview

### 1.1 Channel Landscape

ModRun's product set (cable clips, headphone hooks, magnetic bin labels) fits across four channel archetypes:

| Channel | Buyer Intent | Audience | ModRun Fit |
|---|---|---|---|
| Etsy | Discovery/gift/made-to-order | Handmade/original design shoppers, gift buyers, home office optimizers | Excellent — original-design 3D print is core Etsy product |
| Amazon Handmade FBA | Purchase/Prime delivery | Prime members with high purchase intent, convenience-first buyers | Good — captures buyers who won't find Etsy, additive volume |
| Shopify D2C | Direct/brand-loyal | Returning customers, referral-driven, email list | Good at scale — requires existing brand awareness to convert |
| eBay | Liquidation/price-sensitive | Deal hunters, comparison shoppers | Poor — race-to-bottom pricing destroys margin on precision products |

eBay is excluded from the active roadmap. The platform's buyer expectations around price and condition are incompatible with ModRun's positioning.

### 1.2 Platform Architecture Summary

Each channel has a different operating model that determines when it makes sense to activate:

**Etsy (Active — Phase 1)**
- Made-to-order model; no forward inventory required
- Audience already buys original-design 3D-printed products
- Total fees: ~11–13% of sale price (rising to ~20–23% if/when Offsite Ads mandatory at $10K+/year)
- Zero fixed monthly cost at base level
- Launch capital requirement: ~$40
- Time to first revenue: 5–8 days after launch

**Amazon Handmade FBA (Planned — Phase 2)**
- Requires forward inventory shipped to Amazon warehouses
- Prime badge is the conversion driver; FBM without Prime is not viable
- Total fees: ~27–35% of sale price all-in (referral 15% + FBA fulfillment $3.22–$3.83 + monthly plan amortized)
- Fixed cost: $39.99/month Professional plan (waived from Month 2 onward for approved Handmade sellers)
- Launch capital requirement: $412–$462 (50-unit first batch + ad spend + logistics)
- Time to first revenue: 16–30 days after inventory receives

**Shopify D2C (Planned — Phase 3)**
- Owned storefront; no marketplace fee on the transaction, only payment processing
- Total fees: ~5–7% of sale price (Shopify Basic $39/month amortized + 2.9% + $0.30 Shopify Payments)
- Customer acquisition cost is the critical variable: $55–$75 blended D2C CAC for home goods category (2026 benchmark)
- Viable when email list and repeat customer base exist to lower the paid acquisition burden
- Launch capital requirement: ~$100 (Shopify subscription + domain + basic apps) + ongoing CAC budget

---

## Part 2: Fee Structure Comparison

### 2.1 Platform Fee Matrix (Starter Bundle, $28.99 sale price)

| Fee Component | Etsy | Amazon FBA | Amazon FBM | Shopify D2C |
|---|---|---|---|---|
| Marketplace referral / transaction | 6.5% ($1.88) | 15% ($4.35) | 15% ($4.35) | 0% |
| Payment processing | 3% + $0.25 ($1.12) | Included in referral | Included in referral | 2.9% + $0.30 ($1.14) |
| Listing fee | $0.20 (per unit sold) | $0 | $0 | $0 |
| FBA fulfillment (5 oz) | — | $3.41 (incl. April 2026 surcharge) | — | — |
| Monthly plan amortized @ 50 units | $0 | $0.80 | $0.80 | $0.78 |
| Inbound placement (FBA) | — | $0.25 | — | — |
| Offsite Ads (if > $10K/year) | $0–$3.48 | — | — | — |
| **Total platform fees** | **$3.20 (11.0%)** | **$8.81 (30.4%)** | **$6.14 (21.2%)** | **$1.92 (6.6%)** |
| **Net per unit ($28.99 price, no COGS)** | **$25.79** | **$20.18** | **$22.85** | **$27.07** |

Notes:
- Shopify net assumes Shopify Payments (waives additional 2.0% third-party fee); if using PayPal instead, add 2.0% to the Shopify column.
- Shopify D2C net does not account for customer acquisition cost — the fee structure is cheap but acquiring the customer is expensive until a brand and email list exist.
- Amazon FBM is included for comparison only; it is not recommended as a long-term strategy (see `amazon-fba-analysis.md` Part 4 for conversion rate analysis).

### 2.2 Fee Differential at Scale — Per-100-Unit Analysis

| Channel | Platform Fees (100 units) | Net Revenue (100 units @ $28.99) | Margin Before COGS |
|---|---|---|---|
| Etsy (50 units/month velocity) | $320 | $2,579 | 88.9% |
| Amazon FBA (50 units/month velocity) | $881 | $2,018 | 69.6% |
| Shopify D2C (no CAC) | $192 | $2,707 | 93.4% |
| Shopify D2C (with $60 blended CAC per new customer) | $192 + $6,000 CAC | Negative at 100 units | Not viable without repeat buyers |

The Shopify channel looks cheapest on paper but the cost shifts from platform fees to customer acquisition. At 100 units/month with all new customers and $60 CAC, the channel generates a net loss. The math only works when CAC drops due to repeat purchases, email-driven sales, and organic search — all of which take 6–12 months to develop.

### 2.3 The Etsy Offsite Ads Inflection Point

At $10,000/year in Etsy revenue (approximately $833/month), Etsy's Offsite Ads become mandatory at 12% for attributable orders. This changes the effective fee structure:

- On a $28.99 sale with Offsite Ads attribution: $28.99 × 12% = $3.48 additional fee
- Total Etsy fee on an Offsite Ads order: $3.20 base + $3.48 = $6.68 (23.0%)
- At this level, Amazon FBA's 30.4% fee differential vs. Etsy narrows to ~7 percentage points
- This is the structural trigger point for Amazon FBA acceleration: once Etsy crosses $10K/year, the FBA margin penalty becomes less severe relative to Etsy's true effective fee rate

**Decision rule**: If monthly Etsy revenue exceeds $833/month consistently, expedite the FBA Phase 2 activation regardless of unit count. The fee gap has narrowed enough to justify the investment.

---

## Part 3: Fulfillment Method Comparison

### 3.1 Fulfillment Method by Channel

| Channel | Fulfillment Method | Who Picks/Packs | Who Ships | Prime/Fast Badge |
|---|---|---|---|---|
| Etsy Phase 1 | Self-fulfilled (made-to-order) | ModRun | USPS via Pirate Ship | Star Seller (3–5 day) |
| Amazon FBA | Amazon-fulfilled (forward stock) | Amazon warehouse | Amazon carrier | Prime (1–2 day) |
| Amazon FBM (not recommended) | Self-fulfilled | ModRun | USPS/FedEx | None |
| Shopify D2C Phase 3 | Self-fulfilled or 3PL | ModRun or ShipMonk | Carrier via Shippo/Pirate Ship | None (3–7 day) |

**Printful warehouse fulfillment is not available for ModRun products.** Printful's Warehousing & Fulfillment service for custom/own-inventory products was discontinued as of March 1, 2026 (all inbound shipments halted). Printful is a POD platform for Printful-catalog items (apparel, accessories); it does not and cannot fulfill custom 3D-printed products. The Shopify D2C fulfillment method for ModRun is self-fulfillment or 3PL, not Printful.

### 3.2 Customer Delivery Speed by Channel

| Channel | Expected Delivery Time | Customer Baseline Expectation | Risk of Review Damage |
|---|---|---|---|
| Etsy (Star Seller) | 3–7 business days | 5–7 days is normal; 3–4 days exceeds expectations | Low if within stated window |
| Amazon FBA (Prime) | 1–2 business days | Prime members expect 1–2 days | High if non-Prime; account penalty if OTDR < 97% |
| Shopify D2C | 3–7 business days | No baseline expectation — set in store policy | Low if communicated clearly |

### 3.3 International Shipping Channel Analysis

| Channel | International Capability | Complexity | Recommended for ModRun Phase |
|---|---|---|---|
| Etsy | Seller-enabled per listing; USPS First Class International via Pirate Ship | Low (opt-in, quote-based) | Enable in Phase 2 for top 5 countries (CA, UK, AU, DE, FR) |
| Amazon FBA (US) | FBA Export: Amazon ships internationally from US FC for eligible products | Low (Amazon handles customs) | Enable in Phase 2 alongside FBA launch |
| Amazon FBA (UK/EU) | Requires separate UK or EU FBA accounts with VAT registration | High (VAT registration, separate inventory) | Phase 4+ only; not before 200+ units/month |
| Shopify D2C | Easyship or Shippo integration for 200+ carrier rate comparison; customs docs required | Medium | Phase 3 — add at Shopify launch |

**FBA Export program note**: Amazon's FBA Export program allows US-based FBA inventory to ship internationally without the seller managing customs directly. For eligible products (cable clips qualify — no restricted materials), Amazon handles the export documentation and international carrier coordination. The fee structure is slightly higher than US-only FBA but removes the compliance burden for Phase 2 international orders.

---

## Part 4: Feature Parity Matrix

What capabilities does ModRun need, and which channels provide them natively?

| Capability | Etsy | Amazon FBA | Shopify D2C |
|---|---|---|---|
| Organic discovery (new buyer acquisition) | High (SEO-driven) | Medium (requires 20+ reviews first) | Low (requires paid/SEO investment) |
| Review/social proof system | Strong (native, visible) | Strong (native, critical for algorithm) | Absent (third-party tools needed) |
| Made-to-order compatibility | Native | No (requires forward stock) | Native |
| Inventory management tools | Native (per-listing quantity) | Native (FBA inventory dashboard) | Via app (QuickSync, LitCommerce) |
| Customer email capture | Not permitted | Not permitted | Full control |
| Discount/coupon tools | Native | Via Seller Central | Full control |
| Bundle pricing | Native (variant listings) | Via parent/child ASINs | Full control |
| Analytics dashboard | Basic (Etsy Stats) | Detailed (Business Reports + Brand Analytics) | Detailed (Shopify Analytics) |
| Advertising platform | Etsy Ads (CPC) | Sponsored Products (CPC) | External (Meta, Google) |
| Returns management | Seller-managed | Amazon-managed (FBA) | Seller-managed |
| International shipping | Manual per listing | FBA Export (semi-automated) | Via Easyship/Shippo apps |
| Custom branding/packaging | Full control | Limited (FBA packaging rules) | Full control |
| Subscription/LTV features | No | Subscribe & Save | Full control (Recharge app) |

**Key implication**: Shopify's structural advantage is customer data ownership and LTV features. Neither Etsy nor Amazon permits sellers to directly market to their customer base outside the platform. Shopify D2C is the only channel where ModRun builds a proprietary customer asset — but that asset only matters when volume is sufficient to justify the CAC investment to acquire customers in the first place.

---

## Part 5: Platform Risk Assessment

### 5.1 Single-Channel Risk

100% revenue on Etsy creates existential platform concentration risk. Etsy demonstrated in June 2025 that it can implement sweeping policy changes (ban on unlicensed STL resells) affecting entire categories with limited seller notice. While original-design sellers like ModRun benefited from that change, the platform relationship is asymmetric — Etsy can and does reprice fees, change algorithm weighting, and alter category rules unilaterally.

**Risk mitigation sequence**:
1. Months 1–3: Accept Etsy concentration risk (no practical alternative at sub-$400 capital)
2. Months 3–6: Add Amazon FBA (diversifies to 2 channels; if Etsy suspends or changes fees, Amazon covers ~30–40% of volume)
3. Months 7–12: Add Shopify D2C (builds owned channel; 3-channel diversification means no single platform controls more than 50% of revenue)

### 5.2 Platform Stability Ratings (2026)

| Platform | Policy Stability | Fee Stability | Account Suspension Risk | Overall Risk |
|---|---|---|---|---|
| Etsy | Medium (2 major policy changes in 18 months) | Medium (fees frozen since 2022 but Offsite Ads expansion) | Low (shop suspensions rare vs. Amazon) | Medium |
| Amazon | Low (annual fee increases; 3.5% April 2026 surcharge) | Low (documented fee creep since 2022) | High (account-level suspensions; inventory trapped) | High |
| Shopify | High (platform fees unchanged 2024–2026) | High (payment processing rates stable) | Very Low (self-owned store) | Low |

Shopify is the only channel with no platform-level suspension risk — it is ModRun's store on Shopify's infrastructure, and Shopify does not suspend stores for sales velocity or competitive reasons. The risk is operational (downtime, payment processor issues) not existential.

---

## Part 6: Channel Activation Roadmap

### Phase 1: Etsy Only (Month 0–3, starting May 30, 2026)

**Objective**: Validate product-market fit, build review base, accumulate capital.

**KPIs to track**:
- Units/month: Target 20–50
- Review count: Target 15+ at 4.8+ average
- Accumulated capital from profits: Target $400+
- Etsy conversion rate: Target 2%+

**Phase 1 exits**: At any two of the following: 20+ monthly units (sustained 2 months), 15+ reviews at 4.8+, $400+ available capital.

### Phase 2: Add Amazon FBA (Month 3–6, conditional)

**Trigger conditions** (all three required):
- 20+ monthly Etsy units for two consecutive months
- 15+ Etsy reviews at 4.8+ average
- $400+ in discretionary capital (beyond operating reserves)

**Activation sequence** (see `AMAZON_FBA_READINESS_CHECKLIST.md` for step-by-step):
1. Open Amazon Professional Seller account
2. Apply for Amazon Handmade category approval
3. Apply for Brand Registry (enables Vine enrollment)
4. Enroll Starter Bundle and Pro Expansion Pack ASINs (exclude Economy tier)
5. Print 50-unit initial batch; apply FBA-compliant packaging
6. Ship inbound to Amazon FC
7. Enroll in Vine ($200 New Seller Incentives credit)
8. Launch Sponsored Products at $3/day targeting "cable management," "desk cable organizer"
9. Set 60-day checkpoint: if FBA conversion rate > 3% and 20+ reviews at 4.2+, expand batch size to 75–100 units

**Expected Phase 2 outcome**: Combined Etsy + Amazon revenue of $1,600–$2,200/month at 50–70 combined units/month.

### Phase 3: Add Shopify D2C (Month 7–12)

**Trigger conditions** (all three required):
- 50+ monthly units across channels (Etsy + Amazon combined)
- Etsy review base of 50+ reviews (brand credibility established)
- Accumulated email list of 100+ past customers (from package inserts + QR codes)

**Activation sequence** (see `SHOPIFY_PRINTFUL_INTEGRATION_GUIDE.md` for step-by-step):
1. Create Shopify Basic store ($39/month); activate Shopify Payments
2. Install QuickSync or LitCommerce to sync Etsy inventory → Shopify product catalog
3. Set up Pirate Ship or Shippo integration for shipping label generation
4. Build email capture mechanism (post-purchase pop-up, package insert QR code)
5. Launch email marketing via Klaviyo free tier (500 contacts free)
6. Drive initial Shopify traffic via:
   - QR code on Etsy package inserts: "10% off your next order at modrun.com"
   - Amazon package inserts (within Amazon TOS): "Register your product at modrun.com"
   - Organic social (Instagram, Pinterest) featuring workspace photos
7. Do NOT launch paid Meta/Google ads until Shopify has 30+ days of organic conversion data

**Expected Phase 3 outcome**: Shopify adds 15–25 units/month initially, rising to 30–50 units/month by Month 12 as email list grows to 500+ contacts.

### Phase 4 and Beyond: International Expansion + Shopify Scale

**Month 12+**: Evaluate Amazon UK/EU FBA only after US Amazon generates 75+ units/month consistently. EU VAT registration and Pan-European FBA adds compliance complexity worth ~$500–$800/year in accounting costs — not justified below 75 units/month EU-destined.

---

## Sources

- [Shopify Pricing 2026 — Taxomate](https://taxomate.com/blog/shopify-fees)
- [Shopify Fees 2026 — Qualimero](https://qualimero.com/en/blog/shopify-fees)
- [D2C Customer Acquisition Cost Benchmarks 2026 — Tenten.co](https://tenten.co/shopify/d2c-cac-benchmarks-2026/)
- [45 Ecommerce CAC Statistics 2026 — Ringly.io](https://www.ringly.io/blog/ecommerce-customer-acquisition-cost-statistics-2026)
- [Shopify CAC Benchmarks 2026 — EasyAppsEcom](https://easyappsecom.com/guides/shopify-customer-acquisition-cost-benchmarks)
- [Printful Warehousing & Fulfillment Discontinuation — Printful Help Center](https://help.printful.com/hc/en-us/articles/21048694941340-What-should-I-know-about-the-Dallas-warehousing-service-closure)
- [Printful Shopify Integration — Printful](https://www.printful.com/integrations/shopify)
- [Amazon FBA International Cross-Border 2026 — SAL Accounting](https://salaccounting.ca/blog/international-selling-amazon-fba/)
- [Amazon vs Etsy 2026 — Willow Commerce](https://willowcommerce.ai/amazon-vs-etsy/)
- Internal: `amazon-fba-analysis.md`, `ETSY_SEO_STRATEGY_Q2_Q3_2026.md`, `fulfillment-workflow.md`
