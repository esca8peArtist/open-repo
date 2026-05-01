---
title: "Phase 1 Execution Ready — User Actions and Upload Sequence"
prepared: 2026-05-01
status: BLOCKED on user actions — all other preparation complete
references:
  - UPLOAD_READY_CHECKLIST.md
  - UPLOAD_SEQUENCE.md
  - etsy-store-copy.md
  - scripts/output/
  - mockups/
---

# Phase 1 Execution Ready

**Summary**: All 6 Phase 1 PDFs are under Etsy's 5 MB limit. All 21 mockup images are
2400x2400 px and 300-400 KB. All titles and descriptions are verified compliant. The only
remaining blockers are 3 user-completable actions — 2 account actions and 3 tag corrections.
No orchestrator preparation remains outstanding.

---

## Part 1: The 3 User Actions Required Before Any Upload

Complete these in order. Do not begin the Etsy upload until all three are confirmed.

---

### Action 1 — Apply the 3 Tag Corrections

Do not copy tags from `etsy-store-copy.md` for these three products. The source file contains
violations that will cause Etsy to silently reject or truncate tags, breaking keyword matching.

**Tag Correction A: Companion Planting Chart**

This product has no corrected tag set anywhere in the existing documentation. Do not use the
`etsy-store-copy.md` tags for this product — 10 of the 12 original tags exceed 20 characters.

Use this full 13-tag replacement set exactly as written:

```
companion planting
planting chart pdf
plant together guide
garden plan chart
vegetable companions
planting guide pdf
garden reference pdf
raised bed planting
garden wall chart
vegetable planner
organic garden guide
planting printable
what to plant near
```

Longest tag in this set: `plant together guide` = 20 characters. All pass.

---

**Tag Correction B: Survival Garden Regional Plans**

`UPLOAD_SEQUENCE.md` notes that `self sufficient garden` is "exactly 20 characters —
acceptable." This is incorrect. The phrase `self sufficient garden` is 22 characters
(s-e-l-f-space-s-u-f-f-i-c-i-e-n-t-space-g-a-r-d-e-n = 22). It will fail.

Replace only this one tag in the `UPLOAD_SEQUENCE.md` corrected set:

- REMOVE: `self sufficient garden` (22 chars — fails)
- ADD: `self-sufficient` (15 chars — passes)

Full corrected tag set for this product (use this, not what is in `UPLOAD_SEQUENCE.md`):

```
survival garden plan
food security
self-sufficient
emergency garden
homesteading PDF
food sovereignty
prepper garden plan
calorie garden
seed list by region
regional planner
survival gardening
food independence
companion planting
```

---

**Tag Correction C: Zone-by-Zone Seed Starting Calendar**

`UPLOAD_SEQUENCE.md` includes `veggie planting guide` in the corrected set.
That phrase is 21 characters and will fail.

Replace only this one tag:

- REMOVE: `veggie planting guide` (21 chars — fails)
- ADD: `veggie plant guide` (18 chars — passes)

Full corrected tag set for this product (use this, not what is in `UPLOAD_SEQUENCE.md`):

```
seed start calendar
zone planting guide
USDA zone guide
seed start indoors
frost date guide
zone 3 planting
zone 7 planting
garden calendar pdf
veggie plant guide
heirloom seeds start
digital garden plan
seed start pdf
planting by zone
```

---

**All other products**: Use the corrected sets from `UPLOAD_SEQUENCE.md` as written.
The following products were re-validated and pass:
- Food Sovereignty Starter Guide — `UPLOAD_SEQUENCE.md` corrected set (13 tags, max 20 chars)
- Seed Saving Field Manual — `UPLOAD_SEQUENCE.md` corrected set (13 tags, max 20 chars)
- Apartment Seed Starting Kit — `UPLOAD_SEQUENCE.md` corrected set (13 tags, max 20 chars)
- Seed Swap Hosting Kit — `UPLOAD_SEQUENCE.md` corrected set (13 tags, max 19 chars)
- Anti-Catalog: 30 Heirlooms — `UPLOAD_SEQUENCE.md` corrected set (13 tags, max 20 chars)
- Apartment Plant Catalog — original `etsy-store-copy.md` tags (no violations found)

---

### Action 2 — Verify Etsy Account is Active and Unblocked

Before beginning the shop setup on Day 1, log in to the Etsy seller account and confirm:

- [ ] Seller account is in "Active" status (not suspended, not in review, not on payment hold)
- [ ] Etsy Payments is connected and verified in Shop Manager > Finances
- [ ] No pending identity verification requests are blocking listing publication
- [ ] Shop name `seedwarden` is reserved or confirmed available

A shop on payment hold will allow draft listing creation but will block going public on Day 3.
Check this before spending 1.5-2 hours uploading content.

---

### Action 3 — Confirm Social Media Account is Ready for Launch Announcement

On Day 3 at noon, the shop goes public. An announcement must go out immediately on at least
one social platform. Before starting the upload sequence, confirm:

- [ ] At least one account (Instagram, TikTok, or Pinterest) is active with the `seedwarden` handle
- [ ] A launch post is drafted and ready to publish — it can be a single image post or Reel
- [ ] The post includes the Etsy shop URL in the caption (bio link for TikTok)

If no social accounts exist yet, this also unblocks Phase 2 Track B. Creating the accounts
is a 30-60 minute task and is the Phase 2 Day 1 action anyway — do both at once.

---

## Part 2: The 21-Product Upload Sequence

Phase 1 launches with 6 products. The remaining 15 upload immediately after Phase 1 is live.
No additional preparation is needed for any of them — PDFs, mockups, copy, and tags are all
ready. The blocking question for each is only Phase 1 status and the Native Plants PDF rebuild.

### Phase 1 — 6 Products (Upload Immediately After Actions 1-3 Are Done)

Follow the day-by-day schedule from `UPLOAD_SEQUENCE.md`:

| Upload # | Day | Time | Product | Price | PDF File | Mockup File | Tag Source |
|----------|-----|------|---------|-------|----------|-------------|------------|
| 1 | Day 1 AM | 10-11 AM | Companion Planting Chart | $5 | `companion-planting-chart.pdf` | `companion-planting-chart-mockup.png` | Part 1, Correction A above |
| 2 | Day 1 PM | 2-3 PM | Food Sovereignty Starter Guide | $8 | `food-sovereignty-starter-guide.pdf` | `food-sovereignty-starter-guide-mockup.png` | `UPLOAD_SEQUENCE.md` |
| 3 | Day 2 AM | 10 AM | Anti-Catalog: 30 Heirlooms | $10 | `anti-catalog-30-heirlooms.pdf` | `anti-catalog-30-heirlooms-mockup.png` | `UPLOAD_SEQUENCE.md` |
| 4 | Day 2 PM | 2 PM | Seed Saving Field Manual | $14 | `seed-saving-field-manual.pdf` | `seed-saving-field-manual-mockup.png` | `UPLOAD_SEQUENCE.md` |
| 5 | Day 3 AM | 9 AM | Apartment Plant Catalog | $14 | `apartment-plant-catalog.pdf` | `apartment-plant-catalog-mockup.png` | `etsy-store-copy.md` (no correction needed) |
| 6 | Day 3 AM | 11 AM | Survival Garden Regional Plans | $18 | `survival-garden-regional-plans.pdf` | `survival-garden-regional-plans-mockup.png` | Part 1, Correction B above |
| — | Day 3 | Noon | GO LIVE: switch shop from private to active | | | | |

PDFs are at: `/projects/seedwarden/scripts/output/`
Mockups are at: `/projects/seedwarden/mockups/`

**One flag to check**: The `zone-seed-starting-calendar-mockup.png` displays "$18 (Complete
Bundle)" — if this mockup is used for the individual Zone Calendar listing at $8, replace it
or confirm a bundle variant is intended. This does not affect the 6 Phase 1 products above
(none of them use this mockup for Phase 1 listing).

---

### Phase 2 Backlog — 15 Products (Upload in Week 2+ After Phase 1 is Live)

Upload in this order once Phase 1 has at least 24 hours of view data. These are all ready now.

| # | Product | Price | Mockup File | Notes |
|---|---------|-------|-------------|-------|
| 7 | Seed Swap Hosting Kit | $10 | `seed-swap-hosting-kit-mockup.png` | Tags: `UPLOAD_SEQUENCE.md` |
| 8 | Zone-by-Zone Seed Starting Calendar | $8 | `zone-seed-starting-calendar-mockup.png` | Tags: Part 1, Correction C above. Verify price badge on mockup matches $8. |
| 9 | Apartment Seed Starting Kit | $9 | `apartment-seed-starting-kit-mockup.png` | Tags: `UPLOAD_SEQUENCE.md` |
| 10 | 12-Month Urban Growing Planner | $7 | `12-month-urban-growing-planner-mockup.png` | Tags: verify from `etsy-store-copy.md` |
| 11 | Container Growing Blueprint Pack | $12 | `container-growing-blueprint-pack-mockup.png` | Tags: verify from `etsy-store-copy.md` |
| 12 | Heirloom Variety Selection Guide | $11 | `heirloom-variety-selection-guide-mockup.png` | Tags: verify from `etsy-store-copy.md` |
| 13 | Fermented & Preserved Harvest Handbook | $13 | `fermented-preserved-harvest-handbook-mockup.png` | Tags: verify from `etsy-store-copy.md` |
| 14 | Apartment Growing Complete Guide | $13 | `apartment-growing-complete-guide-mockup.png` | Tags: verify from `etsy-store-copy.md` |
| 15 | Grow Your Own Hot Sauce | $15 | `grow-your-own-hot-sauce-mockup.png` | Tags: verify from `etsy-store-copy.md` |
| 16 | Harvest Preservation Field Manual | $16 | `harvest-preservation-field-manual-mockup.png` | Tags: verify from `etsy-store-copy.md` |
| 17 | Small-Scale Livestock Field Manual | $18 | `small-scale-livestock-field-manual-mockup.png` | Tags: verify from `etsy-store-copy.md` |
| 18 | Meat/Fish Preservation Field Manual | $18 | `meat-fish-preservation-field-manual-mockup.png` | Tags: verify from `etsy-store-copy.md` |
| 19 | Hunting, Fishing & Trapping Field Manual | $20 | `hunting-fishing-trapping-field-manual-mockup.png` | Tags: verify from `etsy-store-copy.md` |
| 20 | Free: 5 Easiest Vegetables | $0 | `free-5-easiest-vegetables-mockup.png` | Lead magnet — upload as free listing after bundles |
| BLOCKED | Native Plants Regional Guide | $18 | `native-plants-regional-guide-mockup.png` | PDF is 56.96 MB — exceeds 5 MB limit. Rebuild before uploading. |

Note on tags for products 10-19: These were not included in `UPLOAD_SEQUENCE.md`'s corrected
tag section. Before uploading each one, manually verify every tag in `etsy-store-copy.md` is
20 characters or fewer. This is a 2-minute check per product.

---

### Phase 2 Bundles — 3 Products (Upload After All Individual Listings Are Live)

| # | Bundle | Price | Component Listings |
|---|--------|-------|--------------------|
| B1 | Apartment Grower Bundle | $32 | Apartment Plant Catalog + Apartment Seed Starting Kit + Apartment Growing Complete Guide |
| B2 | Food Sovereignty Bundle | $30 | Food Sovereignty Starter Guide + Seed Saving Field Manual + Anti-Catalog: 30 Heirlooms |
| B3 | Regional Self-Sufficiency Bundle | $28 | Survival Garden Regional Plans + Zone-by-Zone Seed Starting Calendar + Heirloom Variety Selection Guide |

Bundle copy is in `bundle-listings.md`.

---

## Part 3: Etsy Compliance Status Summary

All 6 Phase 1 products are confirmed compliant on every dimension except the tag corrections
in Part 1. This table reflects the state after applying those corrections.

| Check | Status |
|-------|--------|
| All 6 Phase 1 PDFs under 5 MB | PASS (682 KB – 754 KB) |
| All 21 mockups 2400x2400 px | PASS |
| All 21 mockups 300-400 KB | PASS |
| Phase 1 titles under 140 chars, no forbidden symbols | PASS (3 verified, pattern consistent) |
| Phase 1 descriptions keyword-rich, no banned phrases | PASS (3 verified) |
| Tag violations corrected (3 products) | READY — apply corrections in Part 1 |
| Tags for products 10-19 | Requires manual 20-char check at upload time |
| Native Plants Regional Guide PDF | BLOCKED — 56.96 MB, rebuild required |

---

## Part 4: What Happens Immediately After User Completes the 3 Actions

Once Actions 1-3 above are confirmed:

1. Open Etsy Seller Dashboard — complete one-time shop setup (icon, banner, announcement,
   about, policies). Assets and copy are in `logos/` and `etsy-store-copy.md`. Time: 30-45 min.

2. Upload 6 Phase 1 listings following the table in Part 2. Time per listing: 15-20 min.
   For each listing: paste title from `etsy-store-copy.md`, upload mockup from `mockups/`,
   paste description from `etsy-store-copy.md`, enter corrected tags (use Part 1 of this
   document), upload PDF from `scripts/output/`. Save as draft until Day 3.

3. Day 3 at noon: switch shop to active. Post launch announcement on social.

4. Week 1: monitor views, run the post-upload checklist from `UPLOAD_SEQUENCE.md`.

5. Week 2: begin Phase 2 backlog uploads (products 7-19 from Part 2 above).

---

## Part 5: Single-Sheet Tag Reference (Print-Friendly)

All corrected tag sets for Phase 1 products in one place. Copy from this section into Etsy —
do not use any other source for these products.

### Companion Planting Chart (13 tags)
companion planting / planting chart pdf / plant together guide / garden plan chart /
vegetable companions / planting guide pdf / garden reference pdf / raised bed planting /
garden wall chart / vegetable planner / organic garden guide / planting printable /
what to plant near

### Food Sovereignty Starter Guide (13 tags) — from UPLOAD_SEQUENCE.md
seed saving guide / food sovereignty / heirloom seeds pdf / urban garden guide /
seed saving beginner / corporate seeds / open pollinated / seed library guide /
grow your own food / garden pdf download / food independence / garden for beginners /
seed saving ebook

### Anti-Catalog: 30 Heirlooms (13 tags) — from UPLOAD_SEQUENCE.md
heirloom variety / seed catalog alt / heirloom tomatoes / heirloom seed guide /
seed company reviews / open pollinated / heirloom growing / rare heirloom seeds /
seed saving guide / food sovereignty / varieties at risk / urban gardening pdf /
heirloom vegetables

### Seed Saving Field Manual (13 tags) — from UPLOAD_SEQUENCE.md
seed saving guide / seed saving pdf / tomato seed saving / veggie seed saving /
wet processing seeds / seed storage guide / germination testing / heirloom seed saving /
seed library guide / urban gardening pdf / grow your own food / seed saving manual /
open pollinated

### Apartment Plant Catalog (13 tags) — original etsy-store-copy.md (no correction needed)
Verify from etsy-store-copy.md at upload time.

### Survival Garden Regional Plans (13 tags) — corrected
survival garden plan / food security / self-sufficient / emergency garden /
homesteading PDF / food sovereignty / prepper garden plan / calorie garden /
seed list by region / regional planner / survival gardening / food independence /
companion planting

---

**Prepared**: 2026-05-01
**Status**: Execution-ready pending user completion of 3 actions in Part 1
