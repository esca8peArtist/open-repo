# Seedwarden Product Audit — April 11, 2026

> Comprehensive assessment of all products for launch readiness.
> Prioritized by: content completeness, listing readiness, risk level, market potential.

---

## Summary

| # | Product | Lines | PDF | Etsy Copy | Action Plan | Price | Launch Tier |
|---|---------|-------|-----|-----------|-------------|-------|-------------|
| 1 | Food Sovereignty Starter Guide | 475 | Yes | Yes | — | $8 | Tier 1 |
| 2 | Seed Saving Field Manual | 853 | Yes | Yes | — | $14 | Tier 1 |
| 3 | Apartment Seed Starting Kit | 350 | Yes | Yes | — | $9 | Tier 1 |
| 4 | 12-Month Urban Growing Planner | 745 | Yes | Yes | — | $7 | Tier 1 |
| 5 | Container Growing Blueprint Pack | 576 | Yes | Yes | — | $12 | Tier 1 |
| 6 | Seed Swap Hosting Kit | 428 | Yes | Yes | — | $10 | Tier 1 |
| 7 | Heirloom Variety Selection Guide | 627 | Yes | Yes | — | $11 | Tier 1 |
| 8 | Fermented & Preserved Harvest Handbook | 522 | Yes | Yes | — | $13 | Tier 1 |
| 9 | Grow Your Own Hot Sauce | 491 | Yes | Yes | — | $15 | Tier 1 |
| 10 | Anti-Catalog: 30 Heirlooms | 607 | Yes | Yes | — | $10 | Tier 1 |
| 11 | Small-Scale Livestock Field Manual | 531 | Yes | Yes* | — | $18 | Tier 1 |
| 12 | Meat/Fish Preservation Field Manual | 947 | Yes | Yes* | — | $18 | Tier 1 |
| 13 | Harvest Preservation Field Manual | 901 | Yes | Yes* | — | $16 | Tier 1 |
| 14 | Native Plants Regional Guide | 7717 | Yes (57MB) | Yes* | Yes | $18 | Tier 2 |
| 15 | Apartment Plant Catalog | 1171 | Yes | Yes* | Yes | $14 | Tier 2 |
| 16 | Survival Garden Regional Plans | 1363+ | Yes | Yes (updated) | Yes | $22 | Tier 1 |
| 17 | Hunting, Fishing & Trapping Manual | 747 | Yes | Yes* | — | $20 | Tier 1 |
| 18 | Apartment Growing Complete Guide | 3110 | Yes (146pp) | Yes | **No** | $13 | Tier 2 |
| 19 | Companion Planting Chart | 382 | Yes (21pp) | Yes | — | $5 | Tier 1 |
| 20 | Zone-by-Zone Seed Starting Calendar | 1635 | Yes (82pp) | **No** | — | $7–$18 | Tier 1 |

\* Listing copy written this session (April 11, 2026)

---

## Launch Tiers

### Tier 1 — Ready to List (14 products)

Products with complete content, generated PDF, and Etsy listing copy. These can be listed on Etsy after completing the shared pre-launch checklist below.

**Products 1-13 + 17**: All have substantive content, branded PDFs, and full Etsy listing copy with titles, descriptions, and tags.

**Pre-launch checklist (applies to ALL Tier 1 products):**
- [ ] **PDF mockup images** — Every listing needs 2-3 mockup images showing the PDF on a tablet/phone/table. Use Canva or a free mockup generator. This is the #1 conversion factor for digital products on Etsy.
- [x] **Legal disclaimer page** — All 21 product files verified to have disclaimers (Session 87). Native Plants, Hunting/Trapping, Livestock, both Preservation manuals, Hot Sauce: all have appropriate risk-specific language. Gardening-only products: standard educational disclaimers.
- [x] **Internal cross-links** — All 21 products verified to have cross-links to related products (Session 87). Format varies ("More From Seedwarden" section, inline product mentions, closing recommendations) but all include 2–3 related products with prices.
- [ ] **Voice consistency pass** — Read each product aloud to flag academic, hedging, or filler language. Brand voice is direct, practical, honest.
- [ ] **Regenerate all PDFs** — After any content edits, run `generate_pdfs.py` to update all PDFs.

### Tier 2 — Needs Specific Work (3 products)

**14. Native Plants Regional Guide** ($18)
- **Status**: Content is the strongest in the catalog (7717 lines, 80+ plants, 9 regions). But:
- [ ] Photo sourcing pass — has `[PHOTO: description]` placeholders throughout. At minimum, source 1 image per plant with dangerous lookalike. Use CC0/CC-BY images from iNaturalist, USDA PLANTS Database.
- [ ] Legal disclaimer — foraging guide liability is higher than gardening guides. Add prominent disclaimer.
- [ ] Move "Six Questions Before You Eat" safety rules earlier (currently in appendix — should be page 2-3).
- [ ] PDF is 57MB — may need image optimization or splitting for Etsy download limits.
- **Recommendation**: Can list now with a note that photos are pending. The content is strong enough to sell on text alone. But photos will meaningfully increase conversion.

**15. Apartment Plant Catalog** ($14)
- **Status**: Most complete product per the action plan assessment. But:
- [ ] Verify pet toxicity table against ASPCA database — this table will be relied on by buyers with pets. Errors carry real liability.
- [x] Add seasonal growing calendar (one page, edible plants × season × light category). *(Done: Session 23, April 11 — 19 edible plants with start/harvest timing, light needs, and quarterly summary)*
- **Recommendation**: Could list immediately after toxicity verification. Lowest risk product in the catalog.

**16. Survival Garden Regional Plans** ($22 bundle / $5.99 per region)
- **Status**: Now 7 regions (1363 lines), listing copy updated, cross-links added. Remaining:
- [x] Add 2-3 more regions (PNW, Mid-Atlantic). *(Done: expanded from 5 to 7 regions — PNW and Mid-Atlantic added, +414 lines)*
- [x] Caloric output tables only exist for Houston; add for all regions. *(Done: Session 23, April 11 — tables added for NW Arkansas, SE Wisconsin, Central Wisconsin, Central Michigan)*
- [ ] Decide single product vs. per-region pricing. Recommendation: 8 listings (7 individual at $5.99 + 1 bundle at $22) for maximum SEO surface.
- [ ] System 2 schematics are prose-only; should match System 1 ASCII grids.
- [ ] Needs PDF regeneration after region expansion.
- **Recommendation**: Promoted to Tier 1. List the 7-region bundle now. Add individual region listings in a follow-up pass.

### Tier 3 — Needs Decision (0 products)

*(Previously: Apartment Growing Complete Guide. Decision made April 13, 2026 — listing as standalone product at $13. Upgraded to Tier 2 pending PDF generation.)*

**18. Apartment Growing Complete Guide** (3110 lines, no PDF, listing copy written April 13, 2026)
- Listed as a standalone product at $13 — distinct from Apartment Plant Catalog (decorative/edible plant profiles) and Apartment Seed Starting Kit (seed starting focus). This guide is organized by growing environment and covers the full range: indoor no-light, outdoor balcony, jar growing, and grow-light growing.
- Etsy copy written and added to etsy-store-copy.md (April 13, 2026).
- Remaining blockers:
  - [ ] PDF generation
  - [ ] PDF mockup images

### New Product — Added April 12

**19. Companion Planting Chart** ($5)
- **Status**: Content complete (382 lines, 40 plants). Listing copy written. Cross-links added (referencing actual products). Legal disclaimer included.
- [ ] Needs PDF generation.
- [ ] Needs mockup images.
- **Recommendation**: Tier 1. Low price, high search volume keyword ("companion planting chart"), excellent lead-in product. Should be in Phase 1 launch alongside the other low-price products.

---

## Product Line Analysis

### Strengths
- **Breadth**: 18 products covering gardening, foraging, food preservation, livestock, hunting/fishing, and community organizing (seed swaps). This is a genuinely comprehensive food sovereignty catalog.
- **Content quality**: Writing is consistently strong — direct, practical, safety-conscious. The brand voice is well-established across all products.
- **Price ladder**: $7 (planner) to $20 (hunting manual). Good range for impulse buys through considered purchases.
- **Cross-sell potential**: Products naturally cluster into bundles:
  - Apartment Grower: Seed Starting Kit + Plant Catalog + Container Blueprints + Urban Planner ($42 → bundle at $32)
  - Food Sovereignty: Starter Guide + Seed Saving Manual + Anti-Catalog + Seed Swap Kit ($42 → bundle at $30)
  - Regional Self-Sufficiency: Survival Garden Plans + Native Plants Guide ($36 → bundle at $28)
  - Preservation: Harvest Preservation + Meat/Fish Preservation + Fermented Harvest ($52 → bundle at $38)
  - Homesteader's Complete: Livestock Manual + Hunting/Fishing Manual + Both Preservation Manuals ($72 → bundle at $50)

### Gaps
- **No free lead magnet** — The Apartment Seed Starting Kit ($9) or a single-page "5 Easiest Vegetables to Start With" could serve as a free download to build the email list. High-value strategy for driving first sales.
- **No customer reviews** — New store, no social proof. Plan for getting first 10-20 reviews: consider offering 1-2 products at heavy discount or free to friends/family/community members in exchange for honest reviews.
- **No bundle listings** — The cross-sell clusters above should be actual Etsy listings, not just "mentioned in the description." Each bundle is a separate listing with its own SEO potential.
- **Photos in Native Plants guide** — The highest-value product in the catalog is also the one most dependent on visual content.

### Market Positioning
The catalog occupies a distinctive niche: **food sovereignty for urban and small-space growers, with an explicitly political consciousness**. This is not generic gardening content — it's positioned around independence, self-sufficiency, and resistance to corporate food systems. This resonates with:
- Urban homesteaders and apartment gardeners
- Preppers and self-sufficiency advocates
- Food sovereignty and food justice communities
- Community gardeners and seed library volunteers
- Hot sauce enthusiasts (niche but passionate)

The political framing is a genuine differentiator on Etsy, where most gardening content is apolitical. It will attract some buyers and repel others — that's correct positioning for a brand, not a weakness.

---

## Recommended Launch Sequence

### Phase 1: First 6 Listings (Week 1-2)
Highest-confidence, lowest-risk products to establish the store:
1. **Companion Planting Chart** ($5) — lowest price point, highest search volume keyword, impulse buy
2. **Apartment Seed Starting Kit** ($9) — low price, clear value, low liability
3. **Food Sovereignty Starter Guide** ($8) — brand flagship, sets the tone
4. **12-Month Urban Growing Planner** ($7) — printable products convert well on Etsy
5. **Grow Your Own Hot Sauce** ($15) — strong hook, passionate niche, shareable
6. **Seed Saving Field Manual** ($14) — core competency product

**Rationale**: These six test the market at different price points ($5-$15), cover the most searchable keywords, and have the lowest risk profile. The companion planting chart at $5 is an ideal entry-point product — low commitment for buyers, high search demand.

### Phase 2: Expand (Week 3-4)
6. **Container Growing Blueprint Pack** ($12)
7. **Heirloom Variety Selection Guide** ($11)
8. **Anti-Catalog: 30 Heirlooms** ($10)
9. **Fermented & Preserved Harvest Handbook** ($13)
10. **Seed Swap Hosting Kit** ($10)

### Phase 3: Premium Products (Week 5-8)
11. **Harvest Preservation Field Manual** ($16)
12. **Small-Scale Livestock Field Manual** ($18)
13. **Meat/Fish Preservation Field Manual** ($18)
14. **Hunting, Fishing & Trapping Manual** ($20)
15. **Apartment Plant Catalog** ($14) — after toxicity verification
16. **Survival Garden Regional Plans** ($18 bundle + individual listings)

### Phase 4: Photo-Dependent
17. **Native Plants Regional Guide** ($18) — after photo sourcing pass

### Phase 5: Bundles
Create 4-5 bundle listings after individual products have some sales data.

---

## Revenue Projections (Conservative)

If all 17 products are listed with an average of 2 sales/month each at average price ~$13.50:
- Monthly: ~$460
- Annual: ~$5,500

At 5 sales/month each (moderate success for niche digital products):
- Monthly: ~$1,150
- Annual: ~$13,800

These numbers assume no bundles, no email marketing, no social media, and no paid promotion. Bundles and marketing would meaningfully increase both volume and average order value.

**Etsy fees**: ~6.5% transaction fee + $0.20 listing fee per 4 months. On a $13.50 sale: ~$1.08 in fees. Net margin on digital products is very high.

---

## Immediate Next Actions

1. **Create PDF mockup images** — This is the single biggest blocker. Without mockups, no listing will convert well. Canva has free mockup templates.
2. ~~**Add legal disclaimers** to all product PDFs, especially the 6 with safety/health content.~~ **DONE** (April 11, Session 20) — Category-specific disclaimers added to all 18 products: foraging (1), food safety (4), hunting (1), livestock (1), general gardening (11).
3. **List the first 5 products** — don't wait for perfection. Get feedback from real buyers.
4. ~~**Create one free lead magnet** — a 1-page "5 Easiest Vegetables to Start in an Apartment" PDF that requires email signup.~~ **DONE** (April 11, Session 20) — Created `free-5-easiest-vegetables.md` (~130 lines, 5 vegetables with variety recs, tips, mistakes to avoid, natural cross-sells).
5. **Regenerate all PDFs** after any content edits.
6. **Decide on apartment-growing-complete-guide.md** — bundle product, standalone, or archive?
7. ~~**Write bundle listing copy**~~ **DONE** (April 11, Session 20) — Created `bundle-listings.md` with 5 bundles: Apartment Grower ($32), Food Sovereignty ($30), Regional Self-Sufficiency ($28), Preservation ($38), Homesteader's Complete ($50).
8. ~~**Add cross-links to all products**~~ **DONE** (April 11, Session 20) — "More from Seedwarden" section added to all 18 products with 2-3 curated recommendations each.
