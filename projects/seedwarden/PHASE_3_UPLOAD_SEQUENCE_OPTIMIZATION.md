---
title: "Phase 3 Upload Sequence Optimization"
date: 2026-05-31
status: production-ready — staged for June 1 review
scope: Etsy upload sequencing, SKU model, photo naming, tag strategy, pricing matrix, shop description, cross-selling
cross-references:
  - PHASE_3_ETSY_LISTING_CHECKLIST.md (companion file — per-bundle one-page checklist)
  - PHASE_3_RAPID_DECISION_TREE.md (scenario determines which bundles are uploaded)
  - phase-3-medicinal-herbs-etsy-listings.md (listing copy — titles, descriptions, tags)
  - PHASE_3_UPLOAD_SEQUENCE_OPTIMIZATION.md is pre-staged; activate per scenario on June 21
word_count: ~1,100
---

# Phase 3 Upload Sequence Optimization

**Prepared**: May 31, 2026  
**Purpose**: Minimize Etsy upload friction, coordinate stock availability signals, and sequence bundle launches for cash-flow smoothing and cross-sell amplification.

---

## 1. Upload Sequencing Strategy

Stagger bundle uploads across a 7-week window for three reasons: (a) each new listing generates a "new listing" Etsy search boost that drives organic traffic, (b) sequential uploads allow cash-flow observation between bundles before committing photographer/design time for later bundles, and (c) staggered launches enable cross-sell links between bundles (the Women's Health listing can link to Respiratory once it exists).

### Standard Upload Sequence (applies to Scenarios B and C; Scenario A is single-upload)

| Week | Bundle | Upload target | Rationale |
|---|---|---|---|
| Week 1 | Women's Health | July 19–26 | Highest-demand bundle; anchors herbalist cohort; cross-sells from Phase 2 forager buyers |
| Week 3 | Respiratory | August 2–9 | Second-highest demand; Elderberry search volume peaks fall; allows Women's Health sales data before committing full design time |
| Week 5 | Sleep & Nervines | August 16–23 | Third bundle; Lavender cross-sell bridge from Women's Health; activate Kit email sequence for cross-bundle |
| Week 7 | Immunity | August 30–Sept 5 | Final bundle; Goldenseal conservation framing differentiates; Full Library Bundle listing activated alongside |

**Scenario A**: Single upload on Week 1 target date only. No sequencing required.
**Scenario B**: Weeks 1 and 3 only.
**Scenario C**: Full 7-week sequence.

---

## 2. Variant SKU Model

Each bundle has three SKU variants in Etsy. Create these as separate listings, not as Etsy variants within a single listing (Etsy digital download variant behavior is unreliable for multi-file orders).

| SKU type | Listing title suffix | Price | Notes |
|---|---|---|---|
| Single bundle | (none — base listing) | $12.99–$14.99 | Main listing; drives most organic traffic |
| Practitioner 10-Pack | "— Practitioner 10-Pack License" | $34.99–$39.99 | Separate listing; cross-referenced in base listing description |
| Full Library Bundle | "— Complete 4-Bundle Medicinal Herb Library" | $39.99–$44.99 | Single listing; activate after all 4 bundles live; links to all 4 individual listings |

**SKU naming convention** (for internal tracking and PHOTO_ATTRIBUTION_LOG.md):

`SW-P3-[BUNDLE-SLUG]-[VARIANT]`

Examples:
- `SW-P3-WH-SINGLE` — Women's Health, single bundle
- `SW-P3-WH-10PACK` — Women's Health, practitioner 10-pack
- `SW-P3-RESP-SINGLE` — Respiratory, single bundle
- `SW-P3-LIBRARY` — Full Library Bundle (all 4)

---

## 3. Photo Asset Naming Convention and Directory Structure

All Phase 3 Etsy listing photos stored at:
`projects/seedwarden/assets/phase-3-listing-photos/`

Directory structure:
```
assets/phase-3-listing-photos/
├── womens-health/
│   ├── womens-health-flatlay-01.jpg      (Etsy slot 1 — main image)
│   ├── womens-health-lifestyle-01.jpg    (Etsy slot 2)
│   ├── womens-health-species-01.jpg      (Etsy slot 3 — species collage or detail)
│   ├── womens-health-interior-01.jpg     (Etsy slot 4 — inside spread mockup)
│   └── womens-health-lifestyle-02.jpg    (Etsy slot 5)
├── respiratory/
│   └── [same 5-image structure]
├── sleep-nervines/
│   └── [same 5-image structure]
├── immunity/
│   └── [same 5-image structure]
└── library-bundle/
    └── library-bundle-flatlay-01.jpg     (collage of all 4 covers)
```

Create this directory before the June 21 production start. All photos delivered by the photographer or sourced from Wikimedia go into these folders before Etsy upload.

---

## 4. Tag Strategy Per Bundle

Phase 3 tags must differentiate from Phase 1 (native plants regional guide) and Phase 2 (wild foraging guides) to avoid cannibalization while capturing herbalist-specific search intent.

**Phase 1 tag fingerprint** (avoid duplicating): `native plants`, `wildflower guide`, `plant identification`, `regional plants`, `zone guide`

**Phase 2 tag fingerprint** (avoid duplicating): `foraging guide`, `wild edibles`, `mushroom foraging`, `plant foraging`, `edible plants`

**Phase 3 tag themes** (use these; do not reuse Phase 1/2 tags in Phase 3 listings):

| Bundle | Primary tags (high-volume) | Secondary tags (specific intent) |
|---|---|---|
| Women's Health | `women's herbal guide`, `herbal remedy PDF`, `medicinal herb guide`, `black cohosh guide`, `lavender cultivation` | `hormonal balance herbs`, `women's wellness digital`, `herb identification PDF`, `practitioner herb guide`, `herbalist reference` |
| Respiratory | `elderberry growing guide`, `herbal cold remedy`, `respiratory herbs`, `echinacea guide`, `herb cultivation PDF` | `immune support herbs`, `elderberry syrup guide`, `herbal medicine PDF`, `botanical herb guide`, `medicinal plants guide` |
| Sleep & Nervines | `sleep herb guide`, `nervine herbs`, `valerian guide`, `passionflower growing`, `herbal sleep remedy` | `herbal anxiety relief`, `calming herbs guide`, `lemon balm growing`, `nervine plants`, `herbal wellness PDF` |
| Immunity | `goldenseal guide`, `immunity herb guide`, `adaptogen plants`, `herbal immune support`, `ashwagandha growing` | `goldenseal cultivation`, `medicinal herb reference`, `forest farm herbs`, `at-risk plants guide`, `herbal apothecary` |

**Tag overlap policy**: Two or three generic tags (`medicinal herb guide`, `herbal remedy PDF`, `herb cultivation PDF`) can appear across multiple bundles — this is acceptable because the listings are distinct. Avoid using the same 5+ tags across all listings.

---

## 5. Pricing Test Matrix

Target price range: $12.99–$16.99 for single bundles. Psychological price points for digital downloads at this content depth:

| Price point | Buyer perception | Conversion effect | When to use |
|---|---|---|---|
| $12.99 | Accessible, impulse-buy threshold | Highest conversion, lowest AOV | First bundle launch; new shop phase; if Phase 2 conversion < 2.5% |
| $14.99 | Value-positioned; still under $15 threshold | Mid conversion; good AOV | Standard price after first 20 sales; most bundles |
| $16.99 | Premium signal; above $15 threshold | Lower impulse conversion; higher perceived quality | After reviews accumulate (10+ positive reviews); Full Quad bundle scenario |

**A/B test recommendation**: Launch Women's Health at $12.99. If 10+ sales and 4+ positive reviews arrive within 14 days, increase to $14.99. Monitor conversion rate change over 7 days. If conversion holds within 20% of the $12.99 rate, keep $14.99. This is the only price test needed for launch.

**10-Pack pricing**: $34.99 is the standard. At 2.3× the single-bundle price, it represents a clear value proposition for practitioners (10 clients vs. 1 at $12.99 each would be $129.90 vs. $34.99). Do not discount the 10-pack — its price point is already positioned as a discount.

**Full Library Bundle**: $39.99 (4 bundles at $14.99 each would be $59.96; the bundle at $39.99 is a 33% discount). Activate this listing only after all four bundles are live.

---

## 6. Etsy Shop Description Updates

The current shop description (from Phase 1/2) positions Seedwarden as a native plants and foraging resource. Phase 3 requires an additive update, not a replacement — the existing buyer base should not be confused or devalued.

**Additive paragraph to append to current shop description**:

```
Now expanding into Medicinal Herb Guides — a new series covering cultivation, identification,
active constituents, and safe use for home herbalists, small-scale growers, and practitioner
reference. The same field-tested, research-backed format as our native plants guides, now
applied to the medicinal garden. Practitioner 10-Pack Licenses available for clinical herbalists
and wellness educators.
```

**Do not change**: shop name, banner image, or the native plants section of the description. Phase 3 is additive positioning.

---

## 7. Cross-Selling Strategy

**Phase 2 buyers → Phase 3**: The highest-probability cross-sell is the Phase 2 forager/wild edibles buyer to the Women's Health and Respiratory bundles. Dandelion and Elderberry appear in both Phase 2 foraging content and Phase 3 medicinal content — the content bridge is direct.

**Activation**: Tag all Phase 2 buyers in Kit with `phase2-buyer`. Send a targeted email 7 days after Phase 3 Women's Health launches: "You bought our foraging guide — here's how several of those same plants are used medicinally." Subject line: "The plants you already know, in a new light."

**Cross-bundle cross-sell (within Phase 3)**: Each bundle listing description should contain one sentence referencing the complementary bundle. Example in Women's Health listing: "Lavender also appears in our Sleep & Nervines bundle — see cross-bundle practitioner discount in the Seedwarden shop." Add this sentence only after the second bundle is live.

**Full Library Bundle activation**: The Full Library Bundle listing is the primary cross-sell target for buyers who have purchased one or two individual bundles. Etsy does not have an automated cross-sell feature, but Kit can trigger a "complete your library" email 14 days after a single-bundle purchase. Build this automation in Kit during the Week 1 launch window.

---

*The companion file `PHASE_3_ETSY_LISTING_CHECKLIST.md` contains a one-page per-bundle checklist with SKU, tags, title, description, and photos checklist for each of the four Phase 3 bundles.*
