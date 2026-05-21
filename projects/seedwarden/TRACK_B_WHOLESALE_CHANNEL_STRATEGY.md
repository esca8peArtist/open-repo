---
title: "Track B Wholesale Channel Strategy — Post-June-22 Activation"
date: 2026-05-21
version: 1.0
status: decision-ready
phase: Post-June-22 activation planning
purpose: >
  Wholesale and B2B channel strategy for Track B Medicinal Herbs bundles covering
  practitioner direct (B2B2C), complementary medicine clinics, natural retailers,
  and online marketplaces. Margin models, minimum orders, infrastructure, and
  Tier 1/2/3 decision matrix. Independent of Track A and May 30 scope decisions.
cross-references:
  - HERBALIST_NETWORK_ECOSYSTEM_MAPPING.md (practitioner network baseline)
  - PRACTITIONER_FIRST_CONTACT_SEQUENCE.md (outreach templates)
  - AFFILIATE_PARTNERSHIP_FRAMEWORK.md (commission structure)
  - PHASE_3_REVENUE_AND_PRICING_STRATEGY.md (pricing baseline and Etsy fees)
  - B2B_DISTRIBUTION_STRATEGY.md (Phase 2 B2B foundations)
  - TRACK_B_GEOGRAPHIC_EXPANSION_ANALYSIS.md (geographic channel context)
tags: [seedwarden, track-b, wholesale, B2B, channels, practitioners, clinics, retailers, amazon]
---

# Track B Wholesale Channel Strategy
## Practitioner Direct · Clinics · Natural Retailers · Online Marketplaces

**Prepared**: May 21, 2026
**Channel activation window**: June 22, 2026 (Tier A practitioners) through December 2026 (Phase 2 online platforms)
**Independence note**: All channel activations are independent of Track A blockers. Practitioner Tier A launches June 22 concurrent with public listing. Complementary clinic and online marketplace channels do not require Track A resolution.

---

## Lead Finding

The highest-margin wholesale channel in the first six months is practitioner direct — specifically the 150–300 US herbalist network targeted in PRACTITIONER_FIRST_CONTACT_SEQUENCE.md and HERBALIST_NETWORK_ECOSYSTEM_MAPPING.md. The practitioner 10-pack ($120–$130 per bundle, up to 5 bundles = $499 library price) generates $105–$114 net per sale against zero additional production cost. A single practitioner 10-pack sale per week generates $5,460–$5,928 gross annually — equivalent to 263–301 consumer bundle sales.

Complementary medicine clinics (acupuncture, naturopathy, functional medicine offices) are the Phase 1 physical-presence channel — viable for printed or packaged digital delivery but require consignment logistics that add operational overhead. Activate July 1–15 with geographic clustering to keep fulfillment cost low.

Natural foods retailers (Whole Foods, UNFI/KeHE distributor pathway, independent co-ops) are Phase 2 targets requiring UPC barcoding and distributor relationships. The MOQ reality for distributors (500+ units, net-30/60 payment) makes this channel appropriate only after June 22 launch validates sustained demand. Activate no earlier than September 2026.

Online marketplace expansion (Amazon KDP, iHerb, Vitacost) is Phase 2 for Amazon KDP and Phase 3 for specialty supplement retailers. Amazon KDP provides 35–70% royalty on digital products — the margin is competitive with Etsy but requires separate content formatting and listing work.

---

## Part 1: Practitioner Direct (B2B2C)

### 1.1 Channel Overview

**Target**: 150–300 credentialed and emerging clinical herbalists, naturopathic doctors, and clinical herbalism educators extracted from HERBALIST_NETWORK_ECOSYSTEM_MAPPING.md and the broader AHG/AANP/UpS directories.

**Model structure**:
- Tier A (launch partners, June 22): 25 contacts from PRACTITIONER_FIRST_CONTACT_SEQUENCE.md. Offer: 20% affiliate commission via Etsy coupon code + optional co-branded content.
- Tier B (network expansion, July 15–August 15): 125–275 additional practitioners from AHG directory, AANP state chapters, Herbal Academy alumni network. Offer: 15% affiliate commission (standard practitioner tier per AFFILIATE_PARTNERSHIP_FRAMEWORK.md).
- Practitioner 10-pack: Direct outreach offer for clinical practitioners who want to distribute to clients. License grants distribution rights for up to 10 clients per bundle. Not an affiliate commission structure — this is a direct sale.

### 1.2 Margin Model

**Consumer bundle direct sale**:
| Item | Amount |
|---|---|
| Retail price | $22.00 |
| Etsy transaction fee (6.5%) | -$1.43 |
| Etsy payment processing (3% + $0.25) | -$0.91 |
| Net to Seedwarden | **$19.66** |

**Affiliate sale (20% commission, Tier A)**:
| Item | Amount |
|---|---|
| Retail price | $22.00 |
| Etsy fees (same as direct) | -$2.34 |
| Affiliate commission (20% of $22) | -$4.40 |
| Net to Seedwarden | **$15.26** |

**Practitioner 10-pack (Women's Health, $125)**:
| Item | Amount |
|---|---|
| 10-pack price | $125.00 |
| Etsy transaction fee (6.5%) | -$8.13 |
| Etsy payment processing (3% + $0.25) | -$4.00 |
| Net to Seedwarden | **$112.87** |

**Affiliate 10-pack (20% commission on $125)**:
| Item | Amount |
|---|---|
| 10-pack price | $125.00 |
| Etsy fees | -$12.13 |
| Affiliate commission (20%) | -$25.00 |
| Net to Seedwarden | **$87.87** |

**Margin assessment**: Even at 20% affiliate commission, the practitioner 10-pack generates $87.87 net — 5.8x the net revenue of a single consumer bundle direct sale. The priority is to maximize 10-pack sales through affiliate outreach, not to protect the higher-margin direct sale by limiting affiliate commissions.

### 1.3 Infrastructure Requirements

**Phase 1 (Etsy-based, June 22–August 31)**:
- Etsy coupon code system: Each affiliate gets a unique 15% discount coupon code. Seedwarden tracks coupon redemptions via Etsy's native coupon report. Zero setup cost.
- Practitioner 10-pack: Separate Etsy listing with a license addendum in the PDF ("This purchase grants rights to distribute to up to 10 clients under your practice name"). No DRM enforcement at this stage.
- Monthly payout: Manual PayPal transfer based on coupon redemption report. Tracked in a Google Sheet (template from AFFILIATE_PARTNERSHIP_FRAMEWORK.md).

**Phase 2 (Payhip Pro migration, Q4 2026)**:
- Migrate from Etsy coupon code tracking to Payhip Pro ($99/month, 0% transaction fee, built-in affiliate dashboard).
- Payhip enables automated affiliate commission tracking, direct affiliate dashboard for partners, and unlimited download links per sale.
- Justification threshold: Activate Payhip Pro when monthly affiliate commissions exceed $500 (25+ affiliate sales/month) — at that point the $99/month overhead is offset by fee savings.

**Wholesale login portal (not recommended for Phase 1)**:
- Shopify's "Wholesale Channel" app ($14–$29/month depending on plan) enables a separate password-protected wholesale storefront with tiered pricing.
- Activation threshold: Implement only when Tier B practitioners (July–August) consistently generate >20 wholesale inquiries/month. Before that threshold, email-based invoicing via PayPal is lower friction.

### 1.4 Risk: Channel Conflict and Cannibalization

**Risk**: Practitioners who receive 10-packs ($125) distribute guides to clients who would have purchased consumer bundles ($22) individually. Each 10-pack "replaces" up to 10 consumer sales — but only if those clients would have purchased independently, which requires them to discover the Etsy listing organically.

**Calibration**: At early-stage volume (June–August), organic Etsy discovery is low. The 10-pack cannibalization risk is theoretical. The actual dynamic is: practitioners introduce their clients to guides they would not have found independently, generating sales from a population that would not have been reached through Etsy organic search.

**Mitigation**: Do not publicize the 10-pack price in consumer-facing marketing. The 10-pack listing exists on Etsy but is not featured in the primary social media content calendar. It appears in the practitioner-specific email sequence only.

### 1.5 Timeline

| Date | Action |
|---|---|
| June 15 | Affiliate program live, coupon codes distributed to Tier A (25 contacts) |
| June 22 | Public launch, Tier A affiliates receive promotional assets for launch-week sharing |
| July 1 | First monthly affiliate payout (June 22–30 redemptions) |
| July 15 | Tier B recruitment begins (AHG directory + AANP state chapters) |
| August 15 | Tier B recruitment closes. Evaluate Payhip Pro threshold. |
| September 1 | Canada practitioner outreach begins (OHA + CAND directories) if US launch metrics met |

---

## Part 2: Complementary Medicine Retailers (Clinics)

### 2.1 Channel Overview

**Target**: 50–100 integrative and complementary medicine clinics — acupuncture practices, naturopathic offices, functional medicine clinics, and Ayurvedic wellness centers. Geographic clustering priority: Pacific Northwest (Seattle, Portland), California (Bay Area, LA), New York metro, Chicago, Austin.

**Product format note**: Track B products are digital PDFs. Physical clinic placement requires either (a) a printed physical version or (b) a digital access code card that clinics display and distribute to clients. Both options require additional production decisions:
- Printed guide: POD (print-on-demand) via a service such as Printify or Lulu — 50–75 pages, saddle-stitch or perfect-bound, estimated COGS $3.50–$5.00/copy at 50+ units
- Access code card: A branded postcard with a QR code linking to a PDF download. COGS $0.25–$0.50/card printed at Moo.com or Vistaprint

**Phase 1 recommendation**: Access code cards, not printed guides. Cards are lower cost, eliminate the inventory risk that comes with printed consignment, and preserve digital margin. A clinic displaying a card rack earns the same commission model regardless of physical vs. digital delivery.

### 2.2 Margin Models

**Consignment model (clinic takes revenue share)**:
| Item | Amount |
|---|---|
| Consumer bundle retail price | $22.00 |
| Clinic's share (50% consignment) | -$11.00 |
| Etsy/payment processing fees (on direct PayPal payment from clinic) | -$0.65 (PayPal 2.9% + $0.30) |
| Seedwarden net per consignment sale | **$10.35** |

**Wholesale model (clinic buys upfront)**:
| Item | Amount |
|---|---|
| Wholesale price to clinic (35% discount from $22 retail) | $14.30 |
| PayPal transfer fee (2.9% + $0.30) | -$0.71 |
| Seedwarden net per wholesale unit | **$13.59** |

**Margin comparison**: Wholesale ($13.59) nets more than consignment ($10.35) per unit — but requires the clinic to pay upfront, which creates friction. For Phase 1, consignment is lower-barrier to clinic adoption. Wholesale is appropriate for Phase 2 clinics with demonstrated throughput.

**Minimum order**:
- Consignment: 20 access code cards minimum. Cards cost Seedwarden $5–$10 per batch of 20 (Moo.com pricing). Commission paid monthly on scan-and-purchase completions.
- Wholesale: 10 digital access codes minimum (delivered as a PDF with 10 unique QR codes, each linked to a single-use download). Zero print cost. $143 minimum order value.

### 2.3 Infrastructure Requirements

**Consignment tracking**: A Google Sheets consignment tracker (clinic name, date placed, cards distributed, monthly redemptions, commission owed). Manually updated monthly per clinic. Scales to 30–40 clinics before a dedicated tool (Craftybase or similar) becomes necessary.

**QR code generation**: Each clinic receives a unique QR code linking to a coupon-discounted landing page on Etsy or Payhip. Unique QR codes allow per-clinic redemption tracking. QR code generation: free via QR Tiger or QRCode Monkey.

**Return/restock cycle**: 60-day consignment cycle. Clinics report redemptions monthly. Non-redeemed access codes expire after 6 months (Seedwarden retains revenue). No physical inventory return logistics for digital access code model.

**Clinic outreach targeting**:
- Pacific Northwest cluster (Seattle, Portland): 15–20 clinics. Research via Psychology Today therapist directory (naturopath filter), Zocdoc (integrative medicine), and local Yelp searches for "acupuncture" + "herbalist."
- Bay Area/LA cluster: 20–30 clinics. High density of functional medicine and integrative wellness practices.
- New York metro: 10–15 clinics.
- Austin, Chicago: 5–8 clinics each.

### 2.4 Risk: Slow-Moving Inventory and Low Throughput

**Risk**: Clinics with low patient traffic generate few QR code redemptions, resulting in monthly commissions of $10–$30 — insufficient to justify the outreach and tracking overhead.

**Mitigation**: Require a 90-day performance review. Clinics that generate fewer than 5 sales in 90 days receive a restock decision (no new access codes) and transition to a passive affiliate relationship (coupon code only, no active placement tracking).

**Realistic throughput estimate**: A busy integrative medicine practice seeing 30–50 patients/week might place 2–5 guide bundles per month. A quiet acupuncture practice seeing 10–15 clients/week might place 0–1/month. Target the former, not the latter, in Phase 1 geographic clustering.

### 2.5 Timeline

| Date | Action |
|---|---|
| July 1 | Identify Pacific Northwest clinic cluster (15–20 targets via directory research) |
| July 8–15 | Send clinic outreach emails (template: consignment offer + access code card sample) |
| July 22 | First clinic placements activated (target: 5–10 clinics) |
| August 1 | First 30-day consignment review |
| August 15 | Expand to Bay Area/LA cluster based on PNW results |
| September 1 | 90-day performance review: retain high-throughput clinics, sunset low-throughput |

---

## Part 3: Natural Foods and Supplement Retailers

### 3.1 Channel Overview

**Target**: Two distinct sub-channels with radically different requirements:
- **Sub-channel A**: Independent natural foods co-ops and independent natural stores (25–50 stores, lower MOQ, direct relationship possible)
- **Sub-channel B**: National distributor pathway (UNFI, KeHE, direct Whole Foods vendor)

**Critical note on product format**: Natural food retailers stock physical products with UPCs, case packs, and shelf-ready packaging. Track B digital PDF guides are not directly shelf-stocked. Entry into this channel requires either (a) a printed physical edition of the guides or (b) a printed booklet + digital download card hybrid product. Both require new product development decisions that are appropriately Phase 2 or Phase 3 scope.

### 3.2 Sub-Channel A: Independent Co-ops and Natural Stores

**Target stores**: Natural Grocers (245 stores, Rocky Mountain/Pacific NW focus), independent co-ops with educational section (Wedge Co-op Minneapolis, Willy Street Madison, Honest Weight Albany), local natural health shops.

**Model**: Direct wholesale relationship, no distributor. Seedwarden sells printed guide booklets to co-ops at wholesale (35% discount from retail). Co-op marks up and retails on the educational/wellness shelf.

**Margin model (printed physical guide)**:

| Item | Amount |
|---|---|
| Retail price (physical printed guide) | $24.99 |
| Co-op wholesale discount (35%) | -$8.75 |
| Co-op pays Seedwarden | $16.24 |
| Printed guide COGS (POD, 50-page saddle stitch) | -$4.50 |
| Shipping (case of 20 to co-op, ~$12 flat via USPS) | -$0.60 |
| PayPal/payment processing | -$0.77 |
| Seedwarden net per unit | **$10.37** |

**Minimum order**: 20 printed copies (one case). Minimum order value: $324.80 at wholesale.

**Infrastructure requirements**:
- UPC barcoding: Required for any product stocked at retail. A US UPC (GS1 registered barcode) costs $30 (single barcode) via GS1 US. Estimated 4 hours to generate and integrate into print files.
- Case pack standardization: 20 units/case, shrink-wrap or corrugated box, weight and dimension data for shipping calculation.
- POD production: Lulu.com, Printify, or IngramSpark. Turnaround: 5–7 business days. Unit cost $4–5.50 at 20+ quantity.
- Invoicing: QuickBooks Self-Employed or Wave Accounting for net-30 payment terms.

**Realistic volume and revenue**:
- 25 co-ops × 20 units/order × $10.37 net = $5,185 gross per order cycle
- If co-ops reorder quarterly: ~$20,740 annualized gross (Year 1 partial year)
- This is a meaningful revenue addition — but requires physical product development, UPC acquisition, and POD supplier setup. Total setup time: 20–30 hours.

### 3.3 Sub-Channel B: National Distributor Pathway (UNFI/KeHE)

**UNFI and KeHE market position**: UNFI is the exclusive primary distributor for Whole Foods Market through 2032. KeHE serves Sprouts, regional chains, and independent naturals. Both require:
- Minimum annual volume commitments in the range of $50,000–$100,000+ for new vendors
- Net-30/net-60 payment terms (Seedwarden carries inventory cost for 30–60 days before receiving payment)
- Slotting fees or marketing development funds (MDFs) for shelf placement
- Case pack standardization, EDI (electronic data interchange) capability, and UPC/GS1 compliance

**Assessment**: The UNFI/KeHE pathway is not viable for a digital guide product in 2026. It requires:
1. A physical product with consistent print quality and case pack standardization
2. Volume commitments that require 500–1,000 unit initial inventory commitment
3. Net-30/60 cash flow impact that is inappropriate for a bootstrap operation
4. A distributor broker relationship (independent food broker who carries Seedwarden to distributors) — this broker earns 5–10% of wholesale revenue

**Phase 3 recommendation (2027)**: If printed physical guides are introduced as a product line and the co-op direct channel validates demand, evaluate UNFI/KeHE onboarding in 2027 with a dedicated broker and $5,000–$10,000 slotting/marketing budget.

### 3.4 Margin Model Comparison

| Channel | Seedwarden Net per Unit | Minimum Order | Setup Complexity |
|---|---|---|---|
| Direct consumer (Etsy) | $19.66 | 1 unit | Low |
| Affiliate sale | $15.26 | 1 unit | Low |
| Co-op wholesale (direct) | $10.37 | 20 units printed | Medium |
| UNFI/KeHE distributor | ~$8.00–$10.00 | 500+ units | High |
| Clinic consignment | $10.35 | 20 access codes | Medium |
| Practitioner 10-pack | $112.87 | 1 unit | Low |

The margin hierarchy is clear: practitioner 10-pack > direct consumer > affiliate sale > clinic consignment > co-op wholesale > distributor. Channel selection should prioritize the high-margin practitioner direct channel in Phase 1, with clinic and co-op channels as Phase 2 volume diversification.

### 3.5 Timeline

| Date | Action |
|---|---|
| September 2026 | Physical guide POD evaluation (Lulu/IngramSpark spec and cost comparison) |
| September 2026 | UPC acquisition (GS1 US, $30 per barcode) for 5 bundle titles |
| October 2026 | Approach 5 pilot co-ops (Pacific NW focus) with physical guide samples |
| November 2026 | First co-op orders (target: $3,000–$5,000 gross, 10–15 co-ops) |
| January 2027 | Evaluate UNFI/KeHE pathway based on Q4 co-op sales data |

---

## Part 4: Online Marketplaces

### 4.1 Amazon KDP

**Applicability**: Amazon Kindle Direct Publishing (KDP) supports digital product distribution for self-published books, guides, and educational PDFs in ebook format (.epub or .mobi) and print-on-demand books. Seedwarden's medicinal herbs guides are a strong fit for KDP ebook format.

**Fee structure**:
- 70% royalty option (requires $2.99–$9.99 USD pricing, enrollment in KDP Select — 90-day exclusivity on Kindle format)
- 35% royalty option (no pricing restriction, no exclusivity requirement, available in all markets including international)

**Pricing and net revenue**:
| Pricing option | List price | Royalty rate | Delivery fee | Net to Seedwarden |
|---|---|---|---|---|
| 70% royalty ($9.99 price) | $9.99 | 70% | -$0.15/MB (approx -$0.30) | ~$6.69 |
| 35% royalty ($22 price) | $22.00 | 35% | $0 | $7.70 |
| 35% royalty ($9.99 price) | $9.99 | 35% | $0 | $3.50 |

**Recommendation**: The 35% royalty at $22 price point ($7.70 net) is comparable to the 70% royalty at $9.99 ($6.69 net) and does not require KDP Select exclusivity. Maintain Etsy as the primary sales channel; add Amazon KDP as a secondary discovery channel with the same $22 price point and 35% royalty.

**KDP Select exclusivity conflict**: Enrolling in KDP Select (for 70% royalty) prohibits selling the ebook version through any other platform during the 90-day enrollment window. This conflicts with Etsy PDF sales. **Do not enroll in KDP Select.** Use 35% royalty with no exclusivity.

**Amazon international reach**: KDP automatically distributes to Amazon.ca, Amazon.co.uk, Amazon.de, Amazon.fr, Amazon.it — providing international market access with zero additional setup. This supports the geographic expansion strategy in TRACK_B_GEOGRAPHIC_EXPANSION_ANALYSIS.md at zero additional compliance cost.

**Setup requirements**: KDP account registration (free), epub formatting of each PDF guide (Calibre software, free; 2–4 hours per title), cover image at 1600×2560px minimum. Total setup: 15–25 hours for 5 bundle titles.

**Timeline**: Phase 2 activation, August 2026. Launch after June 22 US Etsy launch validates content quality through reviews.

### 4.2 iHerb and Vitacost

**Platform overview**:
- iHerb: Specialty health and wellness marketplace, primarily physical supplement products. No native digital product support for PDFs or ebooks. **Not applicable for digital guide products.**
- Vitacost (owned by Kroger): Similar physical supplement focus. **Not applicable for digital guide products.**

**Conclusion**: iHerb and Vitacost are physical supplement retail channels. They do not support digital PDF or ebook listings. Relevant only if Seedwarden introduces a physical supplement or printed book product line. Defer to Phase 3 if a physical product is developed.

### 4.3 Specialty Herbalism Marketplaces (Starwest Botanicals, Mountain Rose Herbs Partner Programs)

**Mountain Rose Herbs affiliate program**: Mountain Rose Herbs runs a creator/educator affiliate program. Seedwarden's guides can be listed as recommended resources in an MRH partner newsletter or blog feature. This is an inbound traffic source, not a marketplace listing — MRH does not host or sell Seedwarden products.

**Thrive Market**: A membership-based natural foods marketplace. Thrive Market carries digital wellness products under their "Education and Books" category, but vendor onboarding requires a Thrive Market vendor application (invite-only for new brands). **Phase 2 target if Thrive Market opens a guide/education vendor program.**

**Substack and Gumroad**: Seedwarden's guides could be listed on Gumroad (10% transaction fee, no monthly fee) as a backup distribution channel if Etsy's account verification issues (Track A) become extended. Gumroad's natural health and herbalism category has an active buyer community.

**Platform margin comparison**:
| Platform | Take Rate | Net per $22 Sale | Notes |
|---|---|---|---|
| Etsy | ~10.7% + $0.25 | $19.66 | Primary channel |
| Gumroad | 10% | $19.80 | Lower fees, smaller audience |
| Amazon KDP (35%) | 65% | $14.30 at $22 | Discovery upside, smaller net |
| Payhip | 5% (free plan) / 0% ($99/mo) | $20.90 / $21.36 | Phase 2 direct store migration |

### 4.4 Timeline

| Date | Platform | Action |
|---|---|---|
| August 1 | Amazon KDP | Upload 3 bundles (Women's Health, Respiratory, Sleep) to KDP in epub format |
| August 15 | Amazon KDP | Confirm US, Canada, UK listings live |
| September 1 | Gumroad | Create backup storefront as Track A contingency if Etsy verification extends |
| October 1 | Amazon KDP | Upload remaining 2 bundles (Immunity, Digestive) if June 22 reviews validate quality |
| Q4 2026 | Payhip Pro | Evaluate migration from Etsy coupon codes if affiliate volume exceeds $500/month |

---

## Part 5: Decision Matrix

### 5.1 Channel Scoring by Dimension

| Channel | Revenue Potential | Margin Impact | Operational Complexity | Time to Revenue | Risk Profile | Score |
|---|---|---|---|---|---|---|
| Practitioner Direct (B2B2C) | High (5-figure annual) | Excellent ($112/10-pack) | Low | Immediate (June 22) | Low | **9/10** |
| Amazon KDP | Medium (US+intl coverage) | Good ($7.70 net at $22) | Medium (epub setup) | 6–8 weeks | Low | **7/10** |
| Complementary Clinics | Medium-Low (50 clinics) | Good ($10.35/consign) | Medium (tracking) | 4–6 weeks | Medium | **6/10** |
| Independent Co-ops | Medium (25 stores) | Moderate ($10.37 net) | High (physical product) | 10–14 weeks | Medium | **5/10** |
| Gumroad/Payhip | Low-Medium (discovery) | Excellent (0–5% fee) | Low | 1–2 weeks | Low | **6/10** |
| UNFI/KeHE Distributor | Very High (ceiling) | Moderate ($8–10 net) | Very High | 6–12 months | High | **3/10** |
| iHerb/Vitacost | N/A (physical products only) | N/A | N/A | N/A | N/A | **1/10** |

### 5.2 Tier Ranking

**Tier 1 — Activate Phase 1 (June 22 – August 31, 2026)**:
- Practitioner Direct (Tier A June 22, Tier B July 15)
- Complementary Clinics (Pacific NW cluster, July 1)

**Tier 2 — Activate Phase 2 (September – November 2026)**:
- Amazon KDP (August 1 setup, September live)
- Independent Natural Co-ops (October pilot, 5 stores)
- Gumroad backup storefront (September if needed)
- Payhip Pro migration (Q4 if affiliate volume threshold met)

**Tier 3 — Evaluate Phase 3 (2027)**:
- UNFI/KeHE distributor pathway (only with printed physical product)
- Thrive Market vendor program (if opened to educational publishers)
- iHerb/Vitacost (only with physical supplement product line)

### 5.3 Annual Revenue Projection (Year 1, June 22–June 21, 2027)

| Channel | Conservative | Base Case |
|---|---|---|
| Practitioner Direct (US affiliates) | $8,000 | $18,000 |
| Practitioner 10-pack (US direct) | $5,400 | $12,000 |
| Clinic consignment (50 clinics) | $3,000 | $7,500 |
| Amazon KDP (US + international) | $2,000 | $5,000 |
| Co-op direct (25 stores) | $2,500 | $6,000 |
| Direct Etsy (consumer, non-affiliate) | $6,000 | $14,000 |
| **Year 1 Total** | **$26,900** | **$62,500** |

**Note**: Conservative scenario reflects June 22 launch with 3-bundle Option C (PHASE_3_OPTION_ANALYSIS.md); base case reflects Option A or B with all 5 bundles by August 3 and active practitioner + clinic outreach through August.

---

*Cross-references: HERBALIST_NETWORK_ECOSYSTEM_MAPPING.md, PRACTITIONER_FIRST_CONTACT_SEQUENCE.md, AFFILIATE_PARTNERSHIP_FRAMEWORK.md, PHASE_3_REVENUE_AND_PRICING_STRATEGY.md, TRACK_B_GEOGRAPHIC_EXPANSION_ANALYSIS.md, TRACK_B_GO_LIVE_SEQUENCING.md*
