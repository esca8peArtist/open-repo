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

### 1.5 Acupuncturists and Midwives — Distinct Sub-Channel Protocols

**Acupuncturists**: Licensed acupuncturists (LAc credential) are a distinct sub-segment within the practitioner direct channel. They are not herbalists in the Western clinical tradition, but Traditional Chinese Medicine (TCM) training includes herbs extensively — Astragalus (*Huang Qi*), Schisandra (*Wu Wei Zi*), and Valerian are routinely part of the TCM materia medica. Seedwarden's Phase 3 guides that explicitly cover TCM use patterns alongside Western evidence tiers are directly relevant to this audience.

- **Directory**: American Society of Acupuncturists (asacu.org) member directory; National Certification Commission for Acupuncture and Oriental Medicine (nccaom.org) practitioner finder
- **Licensing compliance**: LAc practitioners in the US operate under state licensing (not federal). All 50 states have some form of acupuncture licensure. Selling educational guides to LAcs does not require any practitioner licensing validation on Seedwarden's part — the guides are educational products, not regulated clinical tools.
- **Outreach framing**: Lead with the TCM name + Western name pairing in the guide (e.g., "Astragalus membranaceus (*Huang Qi*)") as a signal of TCM integration. This framing distinguishes Seedwarden from Western-only herbal guides that are of limited value to TCM practitioners.
- **10-pack relevance**: LAc practitioners with an herbal supplement retail component in their practice (common in integrative TCM offices) are good 10-pack targets — they distribute guides to clients alongside supplement recommendations.
- **Addressable pool**: ~38,000 licensed acupuncturists in the US (NCCAOM data). Even at 0.1% penetration, this represents 38 practitioner relationships. Target the subset with documented herbal practice integration — estimated 8,000–12,000 practitioners.

**Midwives**: Certified Nurse-Midwives (CNMs) and Certified Midwives (CMs) are a high-value practitioner sub-channel for the Women's Health bundle specifically. Herbal support during pregnancy, postpartum recovery, and reproductive health is a documented area of clinical midwifery practice, and midwives are frequently the primary point of contact for herbal guidance with pregnant and postpartum clients.

- **Directory**: American College of Nurse-Midwives (midwife.org) member directory; MANA (Midwives Alliance of North America) directory for direct-entry midwives
- **Licensing compliance**: CNMs are APRNs regulated under state nursing boards. CMs are credentialed by the American Midwifery Certification Board. Selling educational guides to CNMs/CMs involves no additional licensing or B2B compliance requirement on Seedwarden's part.
- **Critical content note**: The Women's Health bundle must include explicit contra-indications for pregnancy and breastfeeding on every herb entry. CNMs and CMs will not recommend a guide to clients if it does not distinguish between herbs safe in pregnancy vs. contraindicated. This is already required by the evidence tier content standards in PHASE_3_BUNDLE_CONTENT_OUTLINE_DETAILED.md — verify it is implemented before outreach to this channel.
- **10-pack relevance**: Midwifery practices with a regular client panel (birth center or large home birth practice) are the highest-LTV version of this channel. A busy CNM seeing 20–30 births per year plus prenatal/postpartum visits has continuous need for reliable herbal education materials to distribute to clients.
- **Addressable pool**: ~13,000 CNMs and ~200 CMs in the US (ACNM data). The subset with documented herbal practice integration is estimated at 2,000–4,000. Target primarily independent midwifery practices and birth centers rather than hospital-employed CNMs (hospital employed CNMs face institutional guidelines that may restrict distributing non-formulary materials).
- **Outreach framing**: Lead with safety (contraindications and evidence-based caution language) before clinical application. Midwives evaluate resources for safety first — the evidence tier system and explicit contra-indication coverage is the primary selling point.

### 1.6 Timeline

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

## Part 6: Tier 1 Partner List — June 15 Outreach Targets

These are the 10 highest-leverage practitioner and institutional targets for June 15 affiliate and wholesale outreach. Each is named, with the specific outreach angle that distinguishes a Seedwarden contact from a generic pitch. All contacts have been drawn from HERBALIST_PRACTITIONER_ECOSYSTEM.md, PHASE_3_HERBALIST_NETWORK_PRESTAGING.md, and the PRACTITIONER_FIRST_CONTACT_SEQUENCE.md pre-staged list.

The June 15 date is required because Tier A partners who confirm before launch can (a) share launch-week promotional posts on June 22, (b) receive pre-configured Etsy coupon codes before launch, and (c) be featured in the launch-week email broadcast as "trusted practitioner partners" — a credibility multiplier with a high ROI for the affiliate program's perceived legitimacy.

---

### Tier 1A — Clinical Educators and Authors (Highest Amplification Value)

**1. Tieraona Low Dog, MD, ABOIM, RH (AHG)**
- Organization: Medicine Lodge Academy; UC Irvine Integrative Medicine Fellowship
- Contact: drlowdog.com [web form]
- Outreach angle: Seedwarden's Women's Health bundle evidence tier system (Traditional, Ethnobotanical, Clinical, Research) is structurally aligned with Dr. Low Dog's evidence-based integrative approach to botanical safety and efficacy. Lead with the evidence tier framework and the clinical accuracy differentiation from competing guides. Specific hook: the guide's herb-drug interaction section mirrors the clinical safety framing in her textbook Complementary and Integrative Approaches to Women's Health.
- Ask: 10-pack co-distribution ($125) for use with Fellowship students + affiliate link for her clinic and newsletter audience. Optional: quote or endorsement for the Etsy listing description.
- Lead time: 3–4 weeks from first contact to confirmation — send by June 15 for a July 1 activation window.
- Risk: High-value contacts have gatekeepers. If no response to the initial web form contact within 7 days, follow up via her AHG Registered Herbalist listing contact path.

**2. David Winston, RH (AHG)**
- Organization: David Winston's Center for Herbal Studies (NJ)
- Contact: davidwinston.org or herbalstudies.net [contact forms]
- Outreach angle: David Winston is one of the most-cited clinical herbalists in North America on respiratory and adaptogen applications. Lead with the Respiratory Support bundle and the traditional use evidence tier for Elecampane and Marshmallow Root — herbs he has written about extensively. Specific hook: the guide's integration of both Western and Traditional Chinese Medicine use patterns (Schisandra, Astragalus) matches his clinical teaching framework.
- Ask: Tier A affiliate (20% commission) for Center for Herbal Studies students and newsletter subscribers. Practitioner 10-pack for use in clinical training programs.
- Lead time: 2–3 weeks — high response probability given AHG overlap.

**3. Christopher Hobbs, PhD (UMass Medicinal Plant Program)**
- Organization: University of Massachusetts Amherst, Medicinal Plant Program
- Contact: christopherhobbs.com [web form]; UMass MPP: umass.edu/mpp
- Outreach angle: Dr. Hobbs is the author of Adaptogens and multiple clinical guides on immune herbs. Lead with the Immunity bundle (Elderberry, Echinacea, Astragalus) and specifically the forest-farming and sustainability sourcing framing for Goldenseal and American Ginseng — research territory that overlaps with UMass MPP's cultivation and ethnobotany work.
- Ask: Affiliate link for his website/newsletter audience. Optional: course adoption inquiry for UMass MPP students (academic 10-pack licensing conversation).
- Lead time: 3–4 weeks.

---

### Tier 1B — School Program Directors (Institutional Bulk Licensing)

**4. Jenn Dazey, ND, RH (AHG) — Bastyr University**
- Organization: Bastyr University, Botanical Medicine/Herbal Sciences Department (Kenmore, WA)
- Contact: bastyr.edu/about/faculty [web form]
- Outreach angle: Bastyr offers the only nationally accredited BS in Herbal Sciences in the United States. Department chairs make adoption decisions for supplemental course materials. Lead with the clinical accuracy of the evidence tier system and the specific alignment with Bastyr's materia medica curriculum. Specific hook: the herb-drug interaction coverage and contraindications section in each bundle match the clinical safety standard Bastyr requires for course materials.
- Ask: Academic bulk licensing — 50-pack or 100-pack for course supplemental materials. Frame as course adoption of a practitioner reference guide, not a retail sale. Net to Seedwarden at academic pricing (40% discount from 10-pack rate): approximately $750 per 100-student cohort.
- Lead time: 4–6 weeks (department chair decisions require a proposal, not just an email).

**5. Notre Dame of Maryland University — MS Clinical Herbal Medicine Program**
- Organization: Notre Dame of Maryland University, Clinical Herbal Medicine MS
- Contact: ndm.edu/academics/integrative-health/herbal-medicine [contact form]
- Outreach angle: This is the only MS-level Clinical Herbal Medicine program at a nationally accredited university. Program directors for a clinical graduate program are receptive to practitioner-caliber field guides that supplement evidence-based coursework. Lead with clinical contraindication coverage and the Research-tier evidence category (which identifies herbs with Phase 1/2 trial data, appropriate for a clinical graduate audience).
- Ask: Same academic bulk licensing ask as Bastyr. Offer a free review copy to the program director before any licensing conversation.
- Lead time: 4–6 weeks.

**6. Northeast School of Botanical Medicine (7Song / Jonathan Treasure)**
- Organization: NESBM, Ithaca, NY
- Contact: 7song.com/contact/
- Outreach angle: NESBM has trained hundreds of community herbalists since 1992. 7Song's naturalist background and emphasis on species identification accuracy makes the field guide format directly relevant to his curriculum. Lead with the full-plant habit photo sourcing protocol (CC-licensed Wikimedia images with ID-specific image sequences) as a signal of the visual and botanical accuracy standard. Specific hook: the guide's wild edibles / first-aid application sections complement NESBM's community herbalism focus.
- Ask: Tier A affiliate (20% commission) for NESBM students and alumni network. NESBM's alumni community is active on social media and well-networked in the northeastern US herbalist community.
- Lead time: 2 weeks — 7Song is known for direct communication.

---

### Tier 1C — Association and Network Amplifiers (Broadcast Reach)

**7. American Herbalists Guild — Education Committee**
- Organization: AHG (americanherbalistsguild.com)
- Contact: AHG office contact form; target the Education or Communications committee lead
- Outreach angle: The AHG newsletter and annual symposium are the highest-reach broadcast channels in the US clinical herbalism community. A Seedwarden feature or advertising placement in the AHG newsletter reaches the entire active AHG membership (4,000–6,000 practitioners). Lead with the evidence tier system and the clinical accuracy differentiation. Frame the relationship as educational publisher partnership, not vendor promotion.
- Ask: Paid editorial feature or "sponsor spotlight" in the AHG newsletter (typically $200–$500/issue) plus a practitioner discount code (15% off for AHG members). This is a paid channel, not a free affiliate placement — budget accordingly.
- Lead time: 3–4 weeks (newsletter placement requires advance booking).

**8. United Plant Savers (UpS)**
- Organization: unitedplantsavers.org
- Contact: UpS member contact form
- Outreach angle: UpS is the primary conservation advocacy organization for North American medicinal plants, with particular focus on CITES-adjacent and at-risk species (Black Cohosh, Goldenseal, American Ginseng, Ramps). Seedwarden's sourcing philosophy — sustainable cultivation, forest farming, no wild harvest of at-risk species — directly aligns with UpS's organizational mission. Lead with the conservation framing in the Phase 3 sourcing guide and the explicit "at-risk species sourcing" coverage in the Immunity bundle.
- Ask: Affiliate partnership for UpS member newsletter and website listings page. UpS maintains a resources/directory page for educational products. A listing there is high-credibility, low-cost reach to the conservation-focused herbalism audience that is particularly receptive to the Seedwarden value proposition.
- Lead time: 3–4 weeks.

**9. Herbal Academy (theherbalacademy.com)**
- Organization: Herbal Academy (online herbalism education platform, Burlington, VT-based)
- Contact: theherbalacademy.com/contact
- Outreach angle: The Herbal Academy has the largest online herbalism student community in the US — tens of thousands of enrolled and alumni students across introductory through advanced clinical programs. Their affiliate program is open to herbalism product and education partners. Lead with the Intermediate and Advanced curriculum alignment (herb-drug interactions, clinical evidence tiers) to signal that Seedwarden's guides are appropriate for the advanced student and practicing clinician audience, not just beginners.
- Ask: Herbal Academy affiliate partnership. Their affiliate program (affiliate.theherbalacademy.com) has an established application process. Apply directly and reference the AHG and UpS partnerships as credibility context.
- Lead time: 2–3 weeks (affiliate application review).

**10. Shannon Elizabeth Bell, PhD — Virginia Tech Forest Botanicals Research**
- Organization: Virginia Tech, Dept. of Sociology
- Contact: sbell33@vt.edu
- Outreach angle: Dr. Bell's 2024–2025 research on increasing forest farming in Appalachia — directly focused on at-risk species commercialization through sustainable cultivation rather than wild harvest — is the strongest academic alignment with Seedwarden's sourcing philosophy. A co-promotion or educational partnership with her research group provides academic credibility that no competitor in the Etsy herbal guide category can replicate. Lead with the goldenseal forest farming photo plan and the conservation sourcing framing.
- Ask: Research partnership inquiry — specifically, permission to cite her Virginia Tech research findings in the Immunity bundle guide text (attribution + potential interview for the "expert note" feature box). This is a research relationship ask, not an affiliate pitch. If she engages, a practitioner resource referral via her professional network is a secondary ask.
- Lead time: 1–2 weeks (academic email response is typically faster than web form contacts).

---

### Partner Outreach Summary Table

| # | Partner | Type | Ask | Target Response Date | Risk |
|---|---|---|---|---|---|
| 1 | Tieraona Low Dog, MD, RH | Author/educator | 10-pack + affiliate | July 1 | High-value, slower response |
| 2 | David Winston, RH | Author/educator | Tier A affiliate | June 29 | High probability response |
| 3 | Christopher Hobbs, PhD | Academic/author | Affiliate + academic inquiry | July 1 | Medium response |
| 4 | Jenn Dazey, ND — Bastyr | Academic director | Bulk academic licensing | July 15 | Proposal required |
| 5 | Notre Dame of MD — MS program | Academic director | Bulk academic licensing | July 15 | Proposal required |
| 6 | 7Song / NESBM | School director | Tier A affiliate | June 27 | High probability response |
| 7 | AHG Education Committee | Association | Paid newsletter feature | June 27 | Budget required ($200–500) |
| 8 | United Plant Savers | Conservation org | Directory listing + newsletter | July 1 | High alignment, low friction |
| 9 | Herbal Academy | Online platform | Affiliate application | June 25 | Formal application process |
| 10 | Shannon Bell, PhD — VT | Academic researcher | Research citation permission | June 22 | Low friction, high credibility |

---

## Part 7: Channel Risk Assessment (May 30–July 2026)

### Risk 1: Practitioner Affiliate Non-Response Rate

**Risk**: The Tier A outreach to 25 contacts by June 15 may yield only 5–10 confirmations, not 20–25. Industry standard affiliate activation rates for cold outreach in niche B2B channels are 15–30% without an existing relationship.

**Impact**: If only 8 Tier A affiliates confirm by June 22, the launch-week affiliate amplification (social shares, newsletter mentions) is significantly reduced, and the June 22 sales velocity benchmark from PHASE_3_REVENUE_AND_PRICING_STRATEGY.md may not be reached in Week 1.

**Mitigation**: Front-load outreach to the 10 Tier 1 contacts above by June 8 (7 days before the June 15 outreach window). Higher-quality first-wave contacts convert better than a large cold list. Track response rates in the master affiliate CRM and escalate to secondary contacts (AHG chapter leaders, Herbal Academy affiliate dashboard) if primary contacts are unresponsive by June 15.

**Threshold**: If fewer than 5 Tier A affiliates confirm by June 19, activate a "soft launch" version of the affiliate announcement that highlights the guide quality rather than partner endorsements. A strong review from even 2–3 credentialed practitioners is sufficient social proof for launch.

---

### Risk 2: Clinic Consignment Throughput Below Breakeven

**Risk**: The complementary clinic channel (Part 2) requires a minimum of 5 sales per clinic per 90 days to generate commission revenue that justifies the tracking and management overhead. Busy urban integrative practices can achieve this; smaller acupuncture practices may not.

**Impact**: If 80% of clinic partners generate fewer than 3 redemptions in the first 90 days, the clinic channel operational cost (monthly commission tracking, QR code regeneration, outreach follow-up) exceeds the revenue it generates.

**Mitigation**: Apply a strict clinic selection filter in July 1 outreach. Target only practices with at least one of: (a) 5+ Google Maps reviews mentioning herbal medicine, (b) an educational resources page on their website, (c) a naturopathic doctor on staff. Practices with these signals are 3–5x more likely to actively place guides with clients than a general acupuncture office.

**Threshold**: Sunset any clinic generating fewer than 2 redemptions in the first 60 days. Transition to passive affiliate relationship (coupon code only, no consignment tracking).

---

### Risk 3: Amazon KDP Content Formatting Errors

**Risk**: Epub conversion of Seedwarden's PDF guides (designed for 8.5x11 visual layout with custom tables, image-text interleaving, and multi-column evidence tier sections) may produce malformed ebook output that renders incorrectly on Kindle devices. A poorly formatted ebook will generate 1-star reviews that damage the brand.

**Impact**: Amazon reviews are permanent and cannot be removed. A batch of negative reviews on the Kindle version would be visible to US buyers as well as international buyers (Amazon shows global review aggregate for the same title across storefronts).

**Mitigation**: Run a full epub validation on the first converted guide (Women's Health) using Amazon's Kindle Previewer (free tool) before uploading to KDP. Validate rendering on at least three device emulations (Kindle Paperwhite, Kindle Fire, iOS Kindle app). If tables and images do not render correctly, convert to a reflowable text format first or publish as a PDF-only file (KDP supports PDF upload for non-Kindle ebook formats). Allow 3–4 weeks for formatting and validation before the August 1 KDP launch target.

---

### Risk 4: Wholesale Pricing Disclosure Triggering Consumer Price Sensitivity

**Risk**: If practitioner 10-pack pricing ($125 for 10 licenses = $12.50/guide) becomes visible to retail consumers via social media or Etsy listing cross-discovery, consumers paying $22/guide may perceive their pricing as unfair, creating friction or negative reviews.

**Impact**: Consumer trust erosion, potential review retaliation, pricing pressure on the $22 consumer bundle.

**Mitigation**: Keep the practitioner 10-pack listing on Etsy but do not include it in any consumer-facing social content. Ensure the 10-pack listing title specifies "Practitioner Bulk License — For Clinical Use" so it does not appear in consumer search results (Etsy search ranking for bulk licensing terms is distinct from consumer purchase terms). This is already noted in Part 1.4 of this document.

---

### Risk 5: Physical Product Development Delay Blocking Co-op Channel

**Risk**: The independent co-op channel (Part 3) requires a printed physical product, UPC barcoding, and POD supplier setup. If these decisions are deferred past September 2026 due to competing priorities, the October 2026 co-op pilot launch will slip to Q1 2027, reducing the channel's Year 1 revenue contribution below the conservative estimate in Section 5.3.

**Impact**: Conservative Year 1 projection loses $2,500 from the co-op direct line, reducing total conservative to $24,400.

**Mitigation**: The September 2026 physical guide decision gate (POD evaluation, UPC acquisition) does not require user action before June 22. It is a standalone decision event. Flag in the MAY_30_FINAL_LAUNCH_CHECKLIST.md as a September 1 milestone review rather than a June launch dependency.

---

*Cross-references: HERBALIST_NETWORK_ECOSYSTEM_MAPPING.md, PRACTITIONER_FIRST_CONTACT_SEQUENCE.md, AFFILIATE_PARTNERSHIP_FRAMEWORK.md, PHASE_3_REVENUE_AND_PRICING_STRATEGY.md, TRACK_B_GEOGRAPHIC_EXPANSION_ANALYSIS.md, TRACK_B_GO_LIVE_SEQUENCING.md, HERBALIST_PRACTITIONER_ECOSYSTEM.md, PHASE_3_HERBALIST_NETWORK_PRESTAGING.md*
