---
title: Amazon FBA vs. Etsy Fulfillment Strategy Analysis — ModRun Cable Management
date: 2026-04-28
status: active
tags: [mfg-farm, amazon, etsy, fulfillment, strategy, modrun]
related: pricing-strategy.md, fulfillment-workflow.md, market-research.md
---

# Amazon FBA vs. Etsy Fulfillment Strategy Analysis

**Recommendation upfront:** Launch on Etsy first. Add Amazon (Handmade + FBA for forward stock) only after reaching 20+ units/month and achieving a 4.8+ review baseline. The capital requirements, inventory risk, and metric complexity of FBA are disproportionate to where ModRun will be at launch. Etsy is the right first channel for a capital-constrained original-design maker — the maker audience is already there, fees are structurally lower at low volume, and the feedback loop is faster. Amazon becomes the right second channel once demand is validated and the review base is strong enough to compete algorithmically.

---

## Part 1: Amazon FBA Program Overview

### What FBA Is

Fulfillment by Amazon (FBA) means you ship your inventory to Amazon's fulfillment centers in advance. Amazon stores it, then picks, packs, and ships individual orders to customers on your behalf. Your products become Prime-eligible, which is the single biggest advantage — Prime buyers heavily filter for Prime shipping, and conversion rates for non-Prime listings are substantially lower in most categories.

FBA is available on the standard Amazon marketplace. There is also Amazon Handmade, a separate storefront within Amazon specifically for artisan-made products. Handmade items can use either FBA (print forward stock in batches, ship to warehouse) or FBM (Fulfillment by Merchant — you ship each order yourself). For 3D-printed products, FBA requires printing batches in advance; FBM allows made-to-order fulfillment.

### Cost Structure (2026 Rates)

**Selling plan:**
- Individual plan: $0 monthly fee + $0.99/item sold
- Professional plan: $39.99/month, no per-item fee
- Break-even: 40 units/month — below that, Individual is cheaper

**Referral fees (category-specific, charged on total sale price):**
- Office Products: 15% (cable management, desk organizers fall here)
- Home & Kitchen: 15%
- Minimum per item: $0.30
- Referral fees are unchanged from 2025 and frozen through 2026

**FBA fulfillment fees (2026 rates for small standard-size items, effective January 15, 2026):**
ModRun clips and rails are small standard-size (under 15x12x0.75 inches, under 16 oz). Based on weight:
- 2 oz or less: $3.11/unit
- 2–4 oz: $3.20/unit
- 4–6 oz: $3.29/unit
- 6–8 oz: $3.38/unit
- 8–10 oz: $3.48/unit
- 10–12 oz: $3.58/unit
- 12–16 oz: $3.65–$3.70/unit

3D-printed PLA/PETG clips are lightweight — a typical cable clip set of 3–5 pieces is likely 2–4 oz total. A full starter bundle (rail + clips + hardware) packaged for FBA shipment is likely 4–8 oz. Expect $3.11–$3.38 as the realistic FBA fulfillment fee per unit.

**Monthly storage fees:**
- January–September (off-peak): $0.78/cubic foot/month
- October–December (peak season): $2.40/cubic foot/month

Small 3D-printed items are extremely low-volume. A set of 50 cable clips could occupy less than 0.5 cubic feet. At $0.78/ft³, monthly storage cost for 50 units of ModRun is roughly $0.39 — negligible at low volume.

**Aged inventory surcharge (formerly LTSF — this is where risk accumulates):**
- Days 181–270: $0.50/ft³/month (in addition to regular storage)
- Days 271–365: $1.50–$5.45/ft³/month (escalates sharply)
- Days 365+: $6.90/ft³/month

This is the stranded inventory trap. If a batch of 50 units sits unsold for 6+ months, the storage penalty compounds until Amazon begins forcing liquidation.

**Inbound placement fee (new in 2025, restructured 2026):**
- For small standard items: approximately $0.21–$0.30/unit for minimal split (single fulfillment center)
- Can be eliminated by splitting shipment to 4+ recommended centers (operationally complex for first-time sellers)
- First-time sellers get inbound fee waived on first 100 units per ASIN under the New Selection Program

**April 17, 2026 fuel surcharge:**
Amazon added a ~3.5% surcharge to all FBA fulfillment fees effective April 17, 2026. This adds approximately $0.11–$0.12/unit on top of the base fulfillment fee for small standard items.

**Total FBA cost stack example (Starter Bundle, $28.99 sale price, 5 oz packaged weight):**
| Fee | Amount |
|---|---|
| Professional plan (amortized at 50 units/mo) | $0.80 |
| Referral fee (15%) | $4.35 |
| FBA fulfillment fee (5 oz) | $3.29 |
| Fuel surcharge (~3.5%) | $0.12 |
| Inbound placement fee | $0.25 |
| Monthly storage (50 units, ~0.02 ft³/unit) | $0.02 |
| **Total Amazon fees** | **$8.83** |
| COGS (Starter Bundle, ~200 units/mo volume) | $3.10 |
| Packaging | $0.35 |
| **Net revenue** | **$16.71** |
| **Net margin** | **57.6%** |

This compares to the existing Etsy pricing model showing ~72% margin on the Starter Bundle. Amazon captures 14–15 percentage points of margin through the combination of higher referral fees and fulfillment charges.

### Seller Reputation and the A9 Algorithm

Amazon's ranking system (A9, now with an AI layer called COSMO) is primarily conversion-rate-driven — Amazon shows listings that sell. For a new seller with zero reviews, the algorithm offers no favor. Getting visible requires either paid advertising (Sponsored Products) or Amazon Vine (early review program, free for new sellers for the first 30 days under New Seller Incentives).

**Critical performance metrics Amazon enforces:**
- Order Defect Rate (ODR): Must be below 1%. Combines negative feedback, A-to-Z claims, and chargebacks. Exceed 1% and you lose Buy Box eligibility for up to 60 days.
- Late Shipment Rate (LSR): Must be below 4%. For FBA this is Amazon's problem, not yours — but FBM sellers face this directly.
- Valid Tracking Rate (VTR): Above 95% required. Expanded in 2025 to cover all carriers.
- On-Time Delivery Rate (OTDR): Above 97% required. As of February 2026, Amazon deactivates individual listings (not whole accounts) that drag down OTDR.

For FBA sellers, Amazon handles LSR, VTR, and OTDR — those metrics are their responsibility once inventory is in the warehouse. The seller's reputation risk concentrates in ODR (product quality, listing accuracy, customer disputes) and overall review score.

**New Seller Incentives (available within 90 days of account opening):**
- $50 in coupon credits
- Free Vine enrollment (important for getting initial reviews)
- FBA storage credits
- $200 in Amazon Advertising credit

### Fulfillment Timeline

FBA order-to-delivery: 1–2 days for Prime members. This is the FBA crown jewel. Etsy's average is 3–7 days for standard shipping.

Time to get inventory into FBA: Creating a shipment plan takes 1–2 hours. Receiving and processing time at Amazon's fulfillment centers is typically 2–5 business days after arrival. You need to ship your inventory to Amazon first, which adds 2–5 transit days depending on your location relative to the assigned center. Total time from "I want to list this" to "it's live and Prime-eligible" is approximately 1–2 weeks.

---

## Part 2: Etsy-Only Approach

### Strengths

**Maker audience alignment.** Etsy's user base expects and pays premium for handmade, original-design products. This is exactly what ModRun is. Buyers searching "cable organizer" or "desk management" on Etsy are explicitly seeking something they cannot find at Target — a thoughtfully designed, artisan-made product. The audience is pre-qualified.

**Original design advantage post-June 2025.** Etsy's policy change banning licensed STL files culled a significant portion of the 3D-print category. Original-design sellers now face a smaller competitive field, and Etsy's algorithm rewards listings that survived the purge with better organic placement.

**Lower effective fees at low volume.** Total Etsy fees on a $28.99 sale: 6.5% transaction ($1.88) + 3% + $0.25 payment processing ($1.12) + $0.20 listing = $3.20, or 11.0%. Amazon's equivalent on FBA runs 26–35% of sale price total. The fee delta is real and significant at low volume.

**Made-to-order production fit.** Etsy supports made-to-order fulfillment natively. ModRun at launch will print to order — no forward inventory investment. This is the only viable model before demand is validated.

**Customer data and direct relationship.** Etsy provides buyer email addresses (message thread) and allows follow-up communication within their messaging system. Building a repeat customer relationship is possible. Amazon explicitly prohibits seller-to-buyer communication outside the platform.

**Feedback loop speed.** First sales generate reviews, reviews surface patterns in product quality and packaging, and you can iterate quickly. With Etsy's 4-month listing window, you can test variants, update photos, and revise listing copy without platform penalty.

### Weaknesses

**Traffic ceiling.** Etsy search volume is substantial but finite, and dominated by SEO dynamics. Without strong review history and sales velocity, new listings start buried. Paid Etsy ads are available but can erode margins. Growing beyond 50–100 units/month on Etsy typically requires building a shop with strong review history, which takes 6–12 months.

**Offsite Ads mandatory at scale.** Once annual Etsy revenue exceeds $10,000, Offsite Ads become mandatory at 12% of the sale price for orders driven by Etsy's external advertising. This is not a choice — it is automatically applied and recalculated monthly. On a $28.99 sale, this is $3.48 additional fee, pushing total Etsy fees to 23–24%.

**No fulfillment infrastructure.** At higher volumes, self-fulfillment becomes the operational bottleneck. Etsy doesn't offer a fulfillment service. At 100+ units/month, packing and shipping dominates time. Third-party 3PL fulfillment is an option but adds per-unit cost.

**Platform dependency risk.** Etsy's policies have shifted twice in 18 months. The June 2025 policy change hurt thousands of sellers. Any seller building exclusively on Etsy is subject to future policy changes, fee increases, and algorithmic shifts they cannot control.

### Etsy Fee Summary (2026)

| Fee | Rate | Notes |
|---|---|---|
| Listing fee | $0.20/listing | Charged every 4 months, and on each sale renewal |
| Transaction fee | 6.5% of total (including shipping) | Applied to entire buyer payment |
| Payment processing | 3% + $0.25 | US sellers via Etsy Payments |
| Offsite Ads | 12–15% (if triggered) | Mandatory above $10K/year; optional below |
| Shop setup | $15 one-time | New shop opening fee |

---

## Part 3: Cost Comparison Matrix

**Assumptions:**
- Representative product: ModRun Starter Bundle at $28.99 sale price
- COGS: $3.10 (at 200+ units/month volume); $3.75 (at 50 units/month); $4.20 (at <50 units/month)
- Packaging: $0.35/unit (Etsy), $0.40/unit (FBA-packaged)
- Shipping (Etsy): $4.50 average USPS First Class (included in sale or charged to buyer; assume buyer pays shipping separately for margin clarity)
- Etsy Offsite Ads: not triggered until $10K/year threshold

### 10 Units/Month Scenario

| Cost Element | Etsy Only | Amazon FBA | Amazon Handmade FBM |
|---|---|---|---|
| Sale price | $28.99 | $28.99 | $28.99 |
| Platform fees | $2.13 (7.3%) | $8.83 (30.4%) | $4.35 referral only (15%) |
| COGS | $4.20 | $4.20 | $4.20 |
| Packaging | $0.35 | $0.40 | $0.35 |
| Professional plan (amortized) | — | $4.00 ($39.99/10) | — ($0.99 x10 = $9.90 individual) |
| Shipping (seller-paid) | $4.50 | included in FBA | $4.50 |
| **Net per unit** | **$17.81** | **$11.56** | **$14.95** |
| **Net margin** | **61.4%** | **39.9%** | **51.6%** |

At 10 units/month, FBA is economically destructive. The professional plan alone costs $4.00/unit. Amazon Handmade FBM is viable but margins still trail Etsy by nearly 10 points.

### 50 Units/Month Scenario

| Cost Element | Etsy Only | Amazon FBA | Hybrid (30 Etsy / 20 FBA) |
|---|---|---|---|
| Sale price | $28.99 | $28.99 | — |
| Platform fees | $2.13 (7.3%) | $8.83 (30.4%) | blended |
| COGS | $3.75 | $3.75 | $3.75 |
| Packaging | $0.35 | $0.40 | blended |
| Professional plan (amortized) | — | $0.80 | $0.80 (shared) |
| Shipping (seller-paid) | $4.50 | included | blended |
| **Net per unit** | **$18.26** | **$15.21** | **$17.08** |
| **Net margin** | **63.0%** | **52.5%** | **58.9%** |
| **Monthly net revenue (channel only)** | **$547.80** | **$304.20** | **$512.40** |

At 50 units/month, FBA starts approaching viability. The hybrid generates nearly the same total revenue as Etsy-only despite a lower per-unit margin — because Amazon volume is additive, not substitutive. However, this requires $150–200 forward inventory investment in FBA stock.

### 100+ Units/Month Scenario

| Cost Element | Etsy Only | Amazon FBA | Hybrid (50/50) |
|---|---|---|---|
| Sale price | $28.99 | $28.99 | — |
| Platform fees | $2.13 | $8.83 | blended |
| COGS | $3.10 (scale benefit) | $3.10 | $3.10 |
| Professional plan (amortized) | — | $0.40 | $0.40 |
| **Net per unit** | **$19.41** | **$16.56** | **$17.99** |
| **Net margin** | **67.0%** | **57.1%** | **62.1%** |
| **Monthly net revenue** | **$1,941** | **$1,656** | **$3,597** (combined) |

At 100 units/month split across both channels, hybrid generates $3,597/month vs. $1,941 Etsy-only — 85% more revenue despite the lower Amazon margin. The volume expansion justifies the margin compression. **This is the target state, not the starting state.**

---

## Part 4: Fulfillment Timelines and Customer Experience

### Etsy (Made-to-Order, Current Model)

| Stage | Time |
|---|---|
| Order placed → Print job queued | 0–12 hours (morning review cycle) |
| Print time (Bambu P1S, small batch) | 3–8 hours |
| QA + packaging | 30–60 minutes |
| Label generated + USPS dropoff | Same day or next morning |
| USPS First Class transit | 2–5 business days |
| **Total order-to-delivery** | **3–7 business days** |

This is acceptable for Etsy buyers. The Etsy expectation is 5–7 days for made-to-order; beating that to 3–4 days is a positive review driver. The 2-business-day processing promise (from fulfillment-workflow.md) is appropriate and achievable.

### Amazon FBA (Forward Stock Model)

| Stage | Time |
|---|---|
| Order placed → warehouse picks item | 2–4 hours (automated) |
| Packaging + handoff to carrier | Same day if ordered by cutoff |
| Prime shipping transit | 1–2 days |
| **Total order-to-delivery** | **1–2 business days** |

The customer experience gap between Etsy made-to-order (3–7 days) and Amazon Prime (1–2 days) is real. For commodity products, this gap is decisive. For ModRun, the question is whether ModRun buyers are primarily conversion-rate driven (Prime urgency) or value-driven (original design, maker story). Given the Etsy audience, they skew toward value-driven. On Amazon, the Prime expectation is table stakes — which is why FBM on Amazon is at a structural disadvantage.

### Amazon Handmade FBM (Made-to-Order on Amazon)

Amazon Handmade allows extended processing times (up to 3 days) but this puts listings at a disadvantage in search against Prime sellers. Customer satisfaction on Amazon is calibrated to faster delivery, so a 5–7 day delivery on Amazon generates worse reviews than the same timeline on Etsy.

**Conclusion on timelines:** Etsy made-to-order is the right operational model at launch. Amazon FBA (forward stock) is the right model if and when Amazon is added as a second channel. Amazon Handmade FBM is a compromise that captures neither Etsy's audience alignment nor Amazon's fulfillment advantage.

---

## Part 5: Seller Reputation Mechanics

### Etsy Star Rating System

Etsy uses a 5-star review system visible on every listing. Reviews are left voluntarily by buyers after order completion; Etsy prompts buyers to review at 7 and 14 days post-delivery.

**Star Seller badge** (evaluated monthly on rolling 3-month window):
- Average review rating: 4.8 or higher
- Message response rate: 95%+ within 24 hours
- On-time shipping with tracking: 95%+ of orders

Star Seller status contributes positively to your Customer and Market Experience Score, which feeds directly into Etsy's search ranking algorithm. The effect is most visible in competitive categories where many listings compete for the same keywords.

**Practical implication:** The first 20–30 reviews are the most important and hardest to get. Early buyers are core to building the rating base. Listing strategy, packaging insert cards asking for reviews, and fast friendly responses to any issues all contribute. A single 1-star review with no others is catastrophic; a 1-star review among 50 five-star reviews is manageable.

Products with 5+ reviews are 270% more likely to sell than unreviewed products (Capital One Shopping research). Reaching the 5-review threshold is the first critical milestone.

**Etsy algorithm search ranking factors:**
- Keyword relevance (listing title, tags, description)
- Conversion rate (clicks → purchases)
- Customer and Market Experience Score (reviews, messages, shipping)
- Recency (new listings get a temporary boost)
- Shop quality history (no policy violations, no cases)

Review-building strategy is covered in the launch checklist; the key point here is that Etsy's reputation system rewards early investment in customer experience (fast shipping, quality packaging, proactive communication) in ways that directly improve organic search visibility.

### Amazon Seller Metrics and A9 Algorithm

Amazon's performance metric thresholds are significantly stricter and carry harsher penalties than Etsy's:

| Metric | Amazon Threshold | Penalty for Failure |
|---|---|---|
| Order Defect Rate (ODR) | < 1% | Loss of Buy Box eligibility up to 60 days |
| Late Shipment Rate (LSR) | < 4% | Account action |
| Valid Tracking Rate (VTR) | > 95% | Suspension risk |
| On-Time Delivery Rate (OTDR) | > 97% | Listing-level deactivation (since Feb 2026) |

For FBA sellers, Amazon handles LSR/VTR/OTDR, removing those as active risks. The seller's remaining risk is ODR — negative reviews, A-to-Z claims, chargebacks. A single bad batch of prints, or a product that doesn't match the listing description, can push ODR toward the 1% threshold fast at low volume (10 defective orders out of 1,000 = 1%; but 1 defective order out of 50 = 2%).

**A9 ranking for new sellers:** A new Amazon listing with zero reviews is invisible without advertising. Amazon's algorithm prioritizes conversion rate and sales velocity. Without an initial review base, a new listing will not convert, which means it won't rank, which means it won't get reviews — a classic cold-start problem. Breaking the loop requires:
1. Amazon Vine (free for new sellers via New Seller Incentives, first 30 days)
2. Sponsored Products advertising (pay-per-click, cost varies but can be $0.50–2.00/click in home office categories)
3. Price-based conversion (lower launch price to drive initial velocity)

The minimum viable Amazon review base before organic visibility becomes real is approximately 20–30 reviews with a 4.3+ average. Getting there without advertising investment is a 3–6 month timeline in most categories.

---

## Part 6: Capital Requirements and Cash Flow

### Etsy-Only Launch (Phase 1)

**Minimum capital required:**
- Etsy shop setup: $15
- Initial listings (10 SKUs x $0.20): $2.00
- Photography setup: already invested (from launch-checklist.md)
- Packaging supplies (50 units buffer): ~$20
- **Total: ~$40**

**Cash flow pattern:** Etsy holds payment for 3 days after a transaction is marked shipped before releasing to your Etsy Payments account. For a new shop, Etsy may hold funds for up to 5 days additionally as part of their new seller reserve. First revenue available approximately 5–8 days after first sale. This is fast enough to be nearly self-funding from first order onward.

**Operational investment:** The Bambu P1S is the capital constraint, and it is already in hand. Ongoing costs are filament (~$0.05–0.10/unit material cost at retail PLA/PETG prices), packaging, and shipping labels. Working capital needed to sustain operations at 10 units/month is essentially zero beyond the initial $40.

### Amazon FBA Launch (Phase 2 Addition)

**Minimum capital required to add FBA:**
- Amazon Professional account: $39.99/month (mandatory for FBA viability above 40 units/month)
- Initial inventory batch for FBA (50 units at $3.10 COGS + $0.40 packaging): $175
- Inbound shipping to Amazon's fulfillment center (50 units, small box, ~$15–25): $20
- FBA-compliant packaging upgrade (poly bags, labels, barcode stickers): ~$30
- Sponsored Products launch budget (recommended): $50–100
- **Total Phase 2 capital requirement: $300–400**

**Cash flow pattern:** Amazon pays every 14 days via disbursement, 2 business days to bank. Payment cycle is significantly slower than Etsy. More importantly, you are floating inventory costs before any sales occur. At $175 inventory investment + $70 operational setup, you are ~$245 in before the first FBA order ships.

**Stranded inventory risk:** If the FBA batch of 50 units does not sell within 6 months, aged inventory surcharges begin at $0.50/ft³/month at day 181. For 50 small cable management units (estimated ~1 cubic foot total), this is an additional $0.50/month on top of regular storage — not catastrophic, but rising steeply after 270 days. The real risk is capital tied up in inventory that isn't moving while aged fees compound.

**Cash flow comparison:**

| Scenario | Etsy Only | FBA Added |
|---|---|---|
| Upfront capital | $40 | $340–440 |
| First revenue | 5–8 days after launch | 14–21 days after launch |
| Payment cycle | 3–8 days post-shipment | 14-day disbursement cycle |
| Inventory float | None (made-to-order) | $175–300 always at risk |
| Fixed monthly cost | $0 | $39.99 (Professional plan) |

---

## Part 7: Risk Assessment

### Etsy-Only Risks

**Platform concentration risk (HIGH):** A single Etsy policy change, algorithm shift, or account suspension can eliminate 100% of revenue overnight. Etsy has demonstrated willingness to make sweeping policy changes (June 2025) with limited seller notice. This is the primary long-term risk of Etsy-only.

**Traffic ceiling (MEDIUM):** Etsy search traffic for functional desk accessories is real but finite. Organic growth slows after the first 6–12 months without active SEO effort and listing portfolio expansion. Reaching $5,000+/month on a single product line requires either broader product range or paid traffic.

**Offsite Ads margin compression (LOW initially, MEDIUM at scale):** Once the $10,000/year threshold is crossed, Offsite Ads at 12% become mandatory. This compresses margins by approximately 10 percentage points on affected orders and cannot be opted out of.

**Policy evolution (MEDIUM):** Etsy has tightened manufacturing disclosure requirements (June 2025) and may further restrict 3D-printed products, require manufacturing audits, or impose additional disclosure fees. Original-design sellers are better protected than resellers, but risk is non-zero.

### Amazon FBA Risks

**Cold-start visibility problem (HIGH):** A new Amazon listing with no reviews has no organic visibility. Without advertising investment or the Vine program, early sales velocity will be near zero. Every day the listing sits with no sales deepens the algorithm penalty.

**Stranded inventory (HIGH for new sellers):** If the initial FBA batch doesn't sell, you face two bad options: pay aged inventory surcharges (escalating past 180 days) or create a removal order and pay $0.97–$1.90/unit removal fee (typical for small standard items). At 50 units, a failed batch costs $50–95 in removal fees on top of the original $175 inventory investment.

**Amazon account suspension risk (MEDIUM):** Amazon's seller accounts can be suspended without warning for a wide range of reasons including ODR threshold breach, policy violations, listing inaccuracy, or counterfeit complaints. Appeals are notoriously slow and outcomes uncertain. Unlike Etsy, where a suspension affects your shop, Amazon suspension affects all your inventory in their warehouses simultaneously.

**Competitive pressure (MEDIUM):** Cable management on Amazon is a crowded category with established Chinese sellers who can undercut on price aggressively. Competing on price is not viable. Competing on design quality and reviews is viable but requires time to establish a review base.

**Fee structure instability (MEDIUM):** Amazon increased FBA fees in 2026, added a fuel surcharge in April 2026, and has increased fees every year since 2022. Fee creep is a structural risk that slowly compresses margins. Each fee increase requires repricing analysis.

**Amazon Handmade eligibility requirements (LOW):** Amazon Handmade requires products to be artisan-made (by the seller or small team, max 100 units/batch). 3D-printed original designs qualify, but you may be subject to audits. Scaling beyond 100 units/batch requires Handmade review. Standard Amazon FBA does not have this restriction if you are not listing under the Handmade storefront.

### Hybrid Strategy Risks

**Operational complexity (MEDIUM):** Managing two channels means two sets of customer service workflows, two fee structures, and two inventory planning systems. This is manageable but is not zero-cost.

**Inventory cannibalization (LOW):** Having forward stock in FBA while running made-to-order on Etsy means your filament and printing time serves two masters. If FBA batch sits unsold, you've locked up working capital that could have been deployed on Etsy orders.

---

## Part 8: Decision Matrix and Recommendation

### Decision Matrix

| Criteria | Etsy Only | FBA Only | Hybrid |
|---|---|---|---|
| Capital requirement at launch | Low ($40) | High ($400+) | Low → Medium ($40 → $400+) |
| Fee burden at low volume (<20/mo) | Low (11%) | Very High (30%+) | Low initially |
| Fee burden at medium volume (50/mo) | Low (11%) | Medium (27%) | Blended (18%) |
| Revenue ceiling | Medium | High | High |
| Audience fit (original design maker) | Excellent | Good | Excellent + Good |
| Customer relationship / data | Good | Poor | Good (Etsy portion) |
| Fulfillment speed | Moderate (3–7 days) | Excellent (1–2 days) | Both |
| Review-building speed | Faster | Slower (cold start) | Faster on Etsy first |
| Platform risk concentration | High | High | Medium (diversified) |
| Operational complexity at launch | Low | High | Low initially |
| Made-to-order compatibility | Excellent | Poor (requires batching) | Mixed |

### Recommendation

**Phase 1 (Launch): Etsy-only, made-to-order.**

The case is clear. At sub-20 units/month, FBA fees would consume 30%+ of revenue on top of COGS and materials, leaving margins half of what Etsy provides. The cold-start problem on Amazon means the first 3–6 months on that platform are expensive in advertising budget without an established review base. The capital constraint makes the $400 FBA setup cost a poor deployment when $40 on Etsy gets you live and selling immediately.

Etsy's audience is explicitly right for ModRun. Buyers searching "3D printed cable organizer" on Etsy are looking for exactly what ModRun is — an original-design, maker-crafted product with premium positioning. The June 2025 policy change has reduced competition in this category. Etsy is the path to first revenue, first reviews, and first product-market fit signal.

**Phase 2 (Month 3–4, conditional): Add Amazon Handmade + FBA with a 50-unit test batch.**

The trigger is 20+ units/month on Etsy with a 4.8+ review average (minimum 15 reviews). At this point: (1) demand is validated, (2) the review base is strong enough to potentially transfer social proof credibility to an Amazon launch, (3) the $400 FBA setup cost is covered by one week of Etsy revenue. Use Amazon Vine for the first 30 reviews via New Seller Incentives. Set Sponsored Products budget at $3–5/day for the first 60 days.

**Phase 3 (Month 6+, conditional): Expand Amazon to full product line.**

Trigger: Amazon FBA conversion rate above 5% and repeat Etsy buyer rate above 15%. At this point, the Amazon channel is validated and the multi-channel model is producing compounding revenue. Invest in Amazon SEO, A+ content (enhanced product description), and a small-scale bundle strategy to increase average order value.

**Brand protection note:** Etsy does not provide customer email addresses in bulk, but you do have a messaging relationship with buyers. Amazon actively prohibits seller-buyer communication outside the platform. For long-term brand building — capturing email addresses, building a direct relationship, enabling future Shopify migration — Etsy is structurally superior. Amazon is a revenue channel, not a brand-building platform.

---

## Sources

- [Amazon FBA Fees 2026: Full Breakdown + April 17 Surcharge Update | AMZ Prep](https://amzprep.com/amazon-fba-fees/)
- [Update to U.S. Referral and Fulfillment by Amazon fees for 2026 - Amazon Selling Partners](https://sellingpartners.aboutamazon.com/update-to-u-s-referral-and-fulfillment-by-amazon-fees-for-2026)
- [Amazon 2026 Fees Breakdown: FBA, Referral, Inbound Placement - Brandwoven](https://gobrandwoven.com/resources/articles/amazon-2026-fees-breakdown-fba-referral-inbound-placement/)
- [Amazon Fee Changes 2026: Significant Fee Updates - Seller Snap](https://sellersnap.io/amazon-fee-changes-and-updates/)
- [Etsy Fees & Payments Policy](https://www.etsy.com/legal/fees/)
- [Etsy Fees 2026: Complete Seller Fee Breakdown | Merch Titans](https://merchtitans.com/blog/etsy-fees-guide)
- [Etsy Fees 2026: Every Fee + Profit Calculator | Listybox](https://listybox.com/blog/etsy-fees-explained-profit-margin-calculator)
- [Etsy or Amazon Handmade? We Compared Them for Sellers (2026) - Eufymake](https://www.eufymake.com/blogs/business-ideas/amazon-handmade-vs-etsy)
- [Amazon Handmade vs Etsy 2026: The Ultimate Proven Seller's Guide - Titannetwork](https://titannetwork.com/amazon-handmade-vs-etsy/)
- [Etsy Star Seller 2026: How to Get and Keep the Badge | ListifyAI](https://www.listifyai.net/blog/etsy-star-seller-guide-2026)
- [Amazon Seller Performance Metrics 2026: Thresholds & AHR - Feedvisor](https://feedvisor.com/university/seller-performance-measurements/)
- [Amazon A9 Algorithm 2026: Ranking Factors - EcomRanker](https://ecomranker.com/amazon-a9-algorithm/)
- [Amazon FBA Long-Term Storage Fees 2026: Why Sellers Are Liquidating - Liquidate Products](https://liquidateproducts.com/blog/amazon-fba-liquidation-2026-ltsf-avoid-fees/)
- [Amazon Inbound Placement FBA Fees Explained in 2026 - AMZ Prep](https://amzprep.com/amazon-inbound-placement-fees/)
- [How to Sell 3D-Printed Products on Amazon - AmzChart](https://amzchart.com/blog/sell-3d-prints)
- [NextGenModeling Etsy SEO Success Story - eRank](https://help.erank.com/blog/nextgenmodeling-etsy-seo-success-story/)
- [Etsy Trending 3D Printed Products 2025 - Accio](https://www.accio.com/business/etsy-trending-3d-printed-products-2025)
- [Where to Sell 3D Prints: Etsy vs Shopify vs Facebook (2026) - Cubee3D](https://www.cubee3d.com/post/where-to-sell-3d-printed-products)
- [Selling 3D-Printed Products on Amazon | Fbahelp](https://fba.help/blog/tips/selling-3d-printed-products-on-amazon)
