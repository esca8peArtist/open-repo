---
title: "Phase 3 Revenue and Pricing Strategy — Medicinal Herbs Bundles"
date: 2026-05-20
status: production-ready
phase: Phase 3 pre-sprint preparation
purpose: >
  Per-bundle P&L analysis, discount and discount-tier strategy, competitive pricing
  context from Etsy medicinal herbs category, steady-state revenue projections,
  and 3-bundle vs. 5-bundle scenario modeling. Decision-ready for May 30 scope review.
cross-references:
  - medicinal-herbs-candidate-list.md (production cost estimates by species)
  - phase-3-medicinal-herbs-content-outline.md (bundle word targets and species)
  - PHASE_3_PRODUCTION_TIMELINE.md (sprint hours, COGS build-up)
  - competitor-landscape.md (Etsy market structure data)
  - financial-sustainability-model.md (digital product revenue baseline)
tags: [seedwarden, phase-3, revenue, pricing, P&L, competitive-pricing, scenarios]
word_count: 1,800+
---

# Phase 3 Revenue and Pricing Strategy — Medicinal Herbs Bundles

**Prepared**: May 20, 2026
**Pricing decision gate**: May 30, 2026
**Revenue baseline from prior analysis**: Digital products alone project $6,000–$11,000 gross Year 2 (from `financial-sustainability-model.md`)

---

## Part 1: Per-Bundle P&L Analysis

### Cost of Goods — Digital Product COGS Model

Digital products have near-zero unit COGS after the initial production investment. The COGS for Seedwarden's medicinal herb bundles is structured differently from physical products: it is a one-time production cost amortized over expected lifetime sales, plus ongoing Etsy platform fees per transaction.

**Production cost by bundle** (based on sprint hours from `PHASE_3_PRODUCTION_TIMELINE.md`):

| Bundle | Sprint Hours | Imputed Labor @ $25/hr | Design Hours | Design Cost @ $25/hr | Photo Sourcing | Total Production COGS |
|---|---|---|---|---|---|---|
| Women's Health (5 species) | 14–16 hrs | $350–400 | 2.0 hrs | $50 | $40 (Mountain Rose + props share) | $440–490 |
| Respiratory (4 species) | 12–14 hrs | $300–350 | 2.0 hrs | $50 | $30 | $380–430 |
| Immunity (4 species + CITES) | 14–16 hrs | $350–400 | 2.0 hrs | $50 | $35 | $435–485 |
| Sleep (4 species) | 12–14 hrs | $300–350 | 2.0 hrs | $50 | $30 | $380–430 |
| Digestive (4 species) | 12–14 hrs | $300–350 | 2.0 hrs | $50 | $30 | $380–430 |
| **Total — 5 bundles** | **64–74 hrs** | **$1,600–1,850** | **10 hrs** | **$250** | **$165** | **$2,015–2,265** |

Notes on imputed labor rate:
- $25/hour is the standard Seedwarden imputed rate for creative and research work. This is not an out-of-pocket cash cost; it is the opportunity cost floor for estimating break-even.
- Photography props (~$160 total) allocated across the five bundles proportionally. Stock images (Wikimedia CC, iNaturalist) are zero direct cost.
- Supplier costs (Mountain Rose Herbs $80–120, plant specimens $250–386) are split between photography purposes and guide development. The photography allocation above ($165 total) represents only the guide-development share.

### Etsy Platform Fee Structure (Per Transaction)

| Fee Type | Rate | On a $22 Sale | On a $20 Sale |
|---|---|---|---|
| Listing fee (per-listing) | $0.20 per listing (one-time per 4 months) | — | — |
| Transaction fee | 6.5% of sale price | $1.43 | $1.30 |
| Payment processing (Etsy Payments) | 3% + $0.25 | $0.91 | $0.85 |
| Offsite Ads fee (if applicable) | 15% of sale price (only on Offsite Ad sales) | $3.30 | $3.00 |
| **Total per sale (no Offsite Ad)** | | **$2.34** | **$2.15** |
| **Total per sale (with Offsite Ad)** | | **$5.64** | **$5.15** |
| **Net to seller (no Offsite Ad)** | | **$19.66** | **$17.85** |
| **Net to seller (Offsite Ad)** | | **$16.36** | **$14.85** |

Offsite Ads apply only when Etsy places a listing on Google Shopping or partner sites and a buyer purchases within 30 days. Shops with over $10,000 in revenue must participate; shops below that threshold can opt out. Seedwarden should remain opted out of Offsite Ads until revenue exceeds $8,000 (at which point the forced enrollment applies) — the 15% fee significantly compresses margins at early sales volumes.

### Per-Bundle Break-Even Analysis

Break-even is calculated at net revenue after Etsy transaction and payment processing fees (Offsite Ads excluded).

| Bundle | Price | Net/Sale (no OA) | Production COGS | Break-Even Units | Units at $300 Gross | Units at $600 Gross |
|---|---|---|---|---|---|---|
| Women's Health | $22 | $19.66 | $465 mid | 24 units | 40 units | 55 units |
| Respiratory | $20 | $17.85 | $405 mid | 23 units | 39 units | 57 units |
| Immunity | $22 | $19.66 | $460 mid | 23 units | 40 units | 55 units |
| Sleep | $20 | $17.85 | $405 mid | 23 units | 39 units | 57 units |
| Digestive | $20 | $17.85 | $405 mid | 23 units | 39 units | 57 units |

**Key finding**: All five bundles break even at 23–24 sales. At the Phase 2 forager cohort attach rate of 15% on a 500-buyer email list, 75 purchases from the existing list alone clears break-even on any single bundle. The launch-day cross-sell email (Day 14 Kit sequence) targeting the forager cohort is the break-even mechanism — it does not require organic Etsy discovery to clear break-even.

### Practitioner 10-Pack P&L

The practitioner 10-pack is the highest-margin SKU in Phase 3. The PDF is the same file as the consumer bundle; the license grants distribution rights to up to 10 clients. The additional value is the license, not additional content production.

| Bundle | 10-Pack Price | Net/Sale | Production COGS (same file) | Break-Even Units | 10-Pack Gross at 1 Sale/Month |
|---|---|---|---|---|---|
| Women's Health | $125 | ~$109 (6.5% + processing) | $0 additional | 5 units total | $109/mo |
| Respiratory | $120 | ~$105 | $0 additional | 4 units total | $105/mo |
| Immunity | $130 | ~$114 | $0 additional | 5 units total | $114/mo |
| Sleep | $120 | ~$105 | $0 additional | 4 units total | $105/mo |
| Digestive | $120 | ~$105 | $0 additional | 4 units total | $105/mo |

**Practitioner tier strategy**: One practitioner 10-pack sale per bundle per month generates approximately $538/month gross across all five bundles. This is almost entirely additive to consumer sales revenue. The practitioner tier does not require Etsy organic discovery — it is driven by the herbalist network email outreach documented in `PHASE_3_HERBALIST_NETWORK_PRESTAGING.md`.

---

## Part 2: Discount Strategy

### Launch Discount Policy

**Recommended**: No launch discount in Weeks 1–2. Reason: Etsy's 72-hour algorithmic discovery window favors full-price sales. A launch discount signals to the Etsy algorithm that the full price is inflated, which suppresses organic ranking. Price the bundles at their permanent price on launch day.

**Alternative (if Week 1 review velocity is below target)**: Activate a 15% Etsy coupon code distributed only to the Kit email list in the Day 7 email sequence. This creates scarcity (limited offer) while protecting the organic listing price. The coupon code is never displayed publicly on the Etsy listing.

**Sale pricing (ongoing)**: Etsy's sale feature (temporary price reduction on the listing itself) is appropriate for two occasions: Black Friday/Cyber Monday (20–25% reduction, Nov 25–Dec 2) and a Summer Wellness Sale (10–15% reduction, July 4–7 window). Two sales per year, not continuous discounting.

### Bundle Discount (Multi-Bundle Purchase)

**Mechanism**: A Kit email sequence offer to buyers who purchase any single bundle. Day 30 email: "You have the Women's Health guide. Complete your apothecary library — bundle all five guides for $85 (saving $19 vs. buying individually)."

| Configuration | Individual Price | Bundle Price | Discount |
|---|---|---|---|
| All 5 bundles (consumer) | $104 combined | $85 | 18% / ~$19 |
| All 5 bundles (practitioner 10-pack) | $615 combined | $499 | 19% / ~$116 |

The 5-bundle email offer is positioned as a "Complete Library" not a discount — the framing is "build the full apothecary reference shelf" not "price reduction."

### Practitioner Tier Pricing Strategy

**Anchoring**: The practitioner 10-pack listing appears on the same Etsy shop page as the consumer bundle. A practitioner who views the consumer bundle at $22 immediately sees the 10-pack at $125 — the 10-pack framing makes the consumer price feel like the entry point, not the primary product.

**Institutional pricing (Phase 3b — not June launch)**: A 50-pack institutional license ($350–400 per bundle) is reserved for community health programs, school nursing curricula, and Herbal Academy course supplementation. This tier is not launched June–August; it is a Phase 3b scope item if practitioner sales show demand signals after October 2026.

---

## Part 3: Competitive Pricing Context

### Etsy Medicinal Herbs Digital Guide Market — Observed Price Bands

Based on aggregated search index data and the analysis in `competitor-landscape.md` (April 30, 2026):

**Price Band 1: $3–10 (single herb charts and reference printables)**
- Products: Medicinal herb reference charts, single-herb information cards, herb ID posters
- Format: 1–3 page PDF, typically not a guide
- Volume: Highest sales counts in the niche, lowest average order value
- Review counts: High (200–1,000+ for established sellers)
- Buyer type: Casual/decorative buyer, not practitioner
- Seedwarden positioning: Not competing here directly. The Wild Edibles Quick Reference ($10) occupies the top of this band.

**Price Band 2: $10–20 (short herbal guides, 20–80 pages)**
- Products: Beginner herbalism ebooks, single-theme guides, seasonal foraging guides
- Format: 20–80 page PDF, often PLR-based content
- Volume: Moderate sales counts (50–500 reviews for established sellers)
- Review counts: 50–400 for sellers with 1–3 years of operation
- Buyer type: Home herbalist, wellness curious
- Seedwarden adjacent: The Wild Edibles Quick Reference ($10) competes in the low end; Phase 3 bundles are priced above this band.

**Price Band 3: $18–30 (substantive single-topic guides, 100–200 pages)**
- Products: Research-based herbal guides, cultivation manuals, practitioner references
- Format: 100–200 page PDF with original content or significant curation
- Volume: Lower sales counts (20–200 reviews) but higher per-unit revenue
- Review counts: Most sellers in this band are under 100 total reviews — the segment is under-reviewed relative to its quality level
- Buyer type: Serious herbalist, clinical practitioner, advanced home grower
- Seedwarden positioning: Phase 3 bundles at $20–22 are in the mid-range of this band.

**Price Band 4: $30–75 (multi-guide bundles, practitioner reference sets)**
- Products: Multi-guide collection bundles, comprehensive practitioner libraries
- Format: 3–6 guides in a single download
- Volume: Low sales counts (under 50 reviews typically)
- Review counts: Thin — the market is under-developed at this price point
- Buyer type: Practitioner, clinical educator, serious collector
- Seedwarden positioning: The 5-bundle library offer ($85) is above this band. The practitioner 10-packs ($120–130) are above it entirely.

### Specific Competitors and Positioning Benchmarks

**Herbal Home Apothecary Ebook** (Etsy listing 1886431111):
- Content: 100+ medicinal herbs, 250+ remedies, 200+ pages
- Price: $21.65 (observed March 2026; appears to have sale/regular pricing fluctuation)
- Bundle type: Comprehensive reference, not themed bundles
- Differentiation from Seedwarden: Breadth-oriented (many herbs, general) vs. Seedwarden's depth-oriented (fewer herbs, cultivation + conservation + clinical detail). This is the most direct consumer-tier competitor at similar price point.

**Herbalism Ebook: Seasonal Foraging and Plant Recipes** (Etsy listing 1840459616):
- Content: 12 monthly herb profiles, botanical information, seasonal harvesting
- Price: Not confirmed; estimated $12–18 based on category comparable
- Bundle type: Seasonal/calendar format — different from Seedwarden's themed bundles
- Differentiation from Seedwarden: Seasonal framing vs. Seedwarden's health-condition framing. Both are cultivation-adjacent, but the seasonal format does not group herbs by therapeutic theme, which is what the practitioner buyer specifically values.

**Materia Medica journal / herb profile journal formats**:
- Multiple sellers; price range $7–18 per journal/template
- Content: Herb study journal templates rather than pre-filled guides
- Star Seller status for top performers
- Differentiation: These are workbooks for the student; Seedwarden's guides are the reference the student fills in the workbook from. Different buyer function.

**Herbal Actions Quick Reference Guide** (Etsy listing 1661249982):
- 43 reviews, 5.0 star average — a strong quality signal for a niche product
- Content: 50 herbal actions with definitions and herb examples — education-focused
- Price: Estimated $8–14 based on format and category
- Differentiation: Pharmacology reference format; Seedwarden's guides are cultivation and traditional use format. Different content philosophy.

### Price Positioning Decision

**Women's Health at $22 and Immunity at $22**: The premium two-bundle price is justified by:
1. Conservation content (Black Cohosh, Goldenseal) — legally precise, research-grounded, no PLR equivalent
2. Species count (5 species for Women's Health vs. 4 for others)
3. CITES sidebar (Immunity) — no competitor has this content

**Respiratory, Sleep, Digestive at $20**: The standard tier price is at the upper-mid range of Price Band 3. This is the correct positioning — not premium enough to create friction for the home herbalist buyer, substantive enough to signal quality against the $12–15 PLR guides that dominate Price Band 2.

**Do not underprice to drive volume in Weeks 1–2**: The Etsy algorithm rewards consistent full-price sales. Undercutting at launch to get reviews faster trains the algorithm to associate the listing with a lower price. Hold $20–22.

---

## Part 4: Steady-State Revenue Projections

### Model Assumptions

- Monthly views per listing after 90-day establishment: 200–400 views (conservative for a new listing in a niche market)
- Conversion rate: 1.5–2.5% (Etsy category average for digital products is 6–7%, but medicinal herb guides are a considered purchase with lower impulse conversion; 2% is the realistic target by Month 3)
- Average sale price: $21 blended (mix of $20 and $22 bundles; practitioner sales are counted separately)
- Practitioner 10-pack sales: 0.5 units/bundle/month conservative, 2 units/bundle/month optimistic

### Consumer Revenue Model (5 Bundles)

| Scenario | Monthly Views/Listing | Conversion | Monthly Sales/Bundle | Revenue/Bundle/Month | Total 5 Bundles/Month |
|---|---|---|---|---|---|
| Conservative (Month 3) | 200 | 1.5% | 3 units | $63 | $315/month |
| Base (Month 6) | 300 | 2.0% | 6 units | $126 | $630/month |
| Optimistic (Month 12) | 400 | 2.5% | 10 units | $210 | $1,050/month |

Note: Month 1–2 projections are lower due to minimal review count. The 72-hour algorithmic window after each upload provides a burst of visibility; sustained views require accumulated reviews (target: 5+ reviews per listing by Month 2).

### Practitioner Revenue Model (5 Bundles, Added on Top)

| Scenario | Sales/Bundle/Month | Revenue/Bundle/Month | Total 5 Bundles/Month |
|---|---|---|---|
| Conservative | 0.5 | ~$53 | $265/month |
| Base | 1.0 | ~$107 | $535/month |
| Optimistic | 2.0 | ~$214 | $1,070/month |

### Combined Steady-State Revenue (Year 1, 12 Months Post-Launch)

| Scenario | Consumer | Practitioner | Total Monthly | Annual |
|---|---|---|---|---|
| Conservative | $315 | $265 | $580/month | $6,960 |
| Base | $630 | $535 | $1,165/month | $13,980 |
| Optimistic | $1,050 | $1,070 | $2,120/month | $25,440 |

This range ($6,960–25,440 annual) is additive to Phase 1 and Phase 2 revenue. The base case of $13,980/year from Phase 3 medicinal bundles alone is the target.

### Forager Cohort Cross-Sell Revenue (Incremental to Above)

The Wild Edibles Quick Reference buyer list (existing cohort) is the highest-value cross-sell channel. At Phase 2's 15% cross-sell attach rate applied to the Digestive bundle (Dandelion cross-sell hook):

- If email list has 500 forager cohort buyers at Digestive bundle launch (August 3): 75 sales × $20 = $1,500 in Week 1–2 from cross-sell alone
- This single cross-sell event likely exceeds the entire first month of organic Etsy discovery for the Digestive bundle

---

## Part 5: Scenario Modeling — 3-Bundle vs. 5-Bundle Revenue Impact

### Option C (3-Bundle Sprint) vs. Option A (5-Bundle Sprint)

| Metric | Option A (5 Bundles) | Option C (3 Bundles) | Revenue Gap |
|---|---|---|---|
| Bundles live by July 13 | 3 (WH, Resp, Sleep) | 3 (identical) | $0 — Week 1–3 identical |
| Bundles live by August 3 | 5 (all) | 3 still | 2 bundles delayed |
| Monthly revenue base by August | $1,165 (base) | $699 (3 bundles at base) | -$466/month |
| Break-even for delayed bundles (Immunity, Digestive) | Already cleared by launch | Delayed ~14–17 days | ~$100 at break-even delay |
| 12-month cumulative gap | $13,980 | ~$8,388 (3-bundle estimate) | ~$5,592 |

**Interpretation for May 30 scope decision**:
- The first three upload dates (June 29, July 6–7, July 13) are identical under Option A and Option C.
- The revenue impact of choosing Option C is approximately $5,600 over 12 months — roughly the equivalent of 280 sales of the Digestive bundle at $20.
- Option C is not a revenue disaster; it is a conservative insurance policy. The 12-month gap is recoverable if the three-bundle sprint succeeds and the writer has capacity for Immunity and Digestive in August–September.
- Option A is the right choice if daily writing availability is 4+ hours/day during the sprint. Option C is the right choice if availability is uncertain.

### Revenue Trigger Points

| Trigger | Revenue Milestone | Action |
|---|---|---|
| First Women's Health sale (Week 1) | Revenue has started — momentum signal | Continue daily word count targets |
| First practitioner 10-pack sale (any bundle) | Practitioner channel validated — do not discount | Begin herbalist network outreach for second practitioner sale |
| 5 reviews per bundle | Etsy algorithm priority increases — visibility expands | No action needed; this is a passive milestone |
| Week 6 forager cross-sell email | Digestive bundle cross-sell trigger | Confirm Kit sequence is set up and live |
| Month 3 cumulative sales >$1,000 | Phase 3 revenue layer contributing meaningfully to sustainability model | Record in WORKLOG.md; include in Phase 4 financial planning |

---

*Prepared: May 20, 2026. Etsy fee structure current as of 2025-2026. Revenue projections are estimates based on category benchmarks and Phase 2 conversion data. Verify practitioner tier pricing ($120–130) against competitor practitioner products before final price confirmation on May 30.*
