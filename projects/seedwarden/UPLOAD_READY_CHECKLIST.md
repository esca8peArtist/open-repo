# Seedwarden — Upload Ready Checklist
**Validation date**: 2026-04-26
**Session**: 439 (Phase 1 upload GO)
**Status**: READY WITH CORRECTIONS — 3 manual actions + 3 tag corrections required before uploading

---

## Summary

All 6 Phase 1 products are validated and production-ready. Three tag compliance issues were
found during validation (details below) that must be corrected before listing creation.
Everything else — PDFs, mockups, titles, descriptions — passes all checks.

---

## Section 1: Phase 1 PDF Files

All 6 lead product PDFs are present, readable, within Etsy's 5 MB file limit, and within the
size range documented in UPLOAD_SEQUENCE.md.

| # | Product | PDF File | Size | Etsy Limit |
|---|---------|----------|------|------------|
| 1 | Companion Planting Chart | `companion-planting-chart.pdf` | 682.0 KB | PASS |
| 2 | Food Sovereignty Starter Guide | `food-sovereignty-starter-guide.pdf` | 710.3 KB | PASS |
| 3 | Anti-Catalog: 30 Heirlooms | `anti-catalog-30-heirlooms.pdf` | 686.8 KB | PASS |
| 4 | Seed Saving Field Manual | `seed-saving-field-manual.pdf` | 724.9 KB | PASS |
| 5 | Apartment Plant Catalog | `apartment-plant-catalog.pdf` | 748.2 KB | PASS |
| 6 | Survival Garden Regional Plans | `survival-garden-regional-plans.pdf` | 753.8 KB | PASS |

Note: `survival-garden-regional-plans.pdf` is 753.8 KB, fractionally above the 753 KB upper
bound cited in UPLOAD_SEQUENCE.md. This is a documentation rounding issue only — the file is
well within Etsy's 5 MB hard limit.

**BLOCKED (do not upload)**: `native-plants-regional-guide.pdf` — 56.96 MB, exceeds Etsy's
5 MB hard limit. Must be rebuilt before it can be listed.

All Phase 1 PDFs are located at:
`projects/seedwarden/scripts/output/`

---

## Section 2: Mockup Images

### Dimensions

All 21 mockups confirmed 2400x2400 px PNG. Zero failures.

| Mockup | Dimensions | Result |
|--------|-----------|--------|
| 12-month-urban-growing-planner-mockup.png | 2400x2400 | PASS |
| anti-catalog-30-heirlooms-mockup.png | 2400x2400 | PASS |
| apartment-growing-complete-guide-mockup.png | 2400x2400 | PASS |
| apartment-plant-catalog-mockup.png | 2400x2400 | PASS |
| apartment-seed-starting-kit-mockup.png | 2400x2400 | PASS |
| companion-planting-chart-mockup.png | 2400x2400 | PASS |
| container-growing-blueprint-pack-mockup.png | 2400x2400 | PASS |
| fermented-preserved-harvest-handbook-mockup.png | 2400x2400 | PASS |
| food-sovereignty-starter-guide-mockup.png | 2400x2400 | PASS |
| free-5-easiest-vegetables-mockup.png | 2400x2400 | PASS |
| grow-your-own-hot-sauce-mockup.png | 2400x2400 | PASS |
| harvest-preservation-field-manual-mockup.png | 2400x2400 | PASS |
| heirloom-variety-selection-guide-mockup.png | 2400x2400 | PASS |
| hunting-fishing-trapping-field-manual-mockup.png | 2400x2400 | PASS |
| meat-fish-preservation-field-manual-mockup.png | 2400x2400 | PASS |
| native-plants-regional-guide-mockup.png | 2400x2400 | PASS |
| seed-saving-field-manual-mockup.png | 2400x2400 | PASS |
| seed-swap-hosting-kit-mockup.png | 2400x2400 | PASS |
| small-scale-livestock-field-manual-mockup.png | 2400x2400 | PASS |
| survival-garden-regional-plans-mockup.png | 2400x2400 | PASS |
| zone-seed-starting-calendar-mockup.png | 2400x2400 | PASS |

### File Sizes (all 21, target: 300–400 KB)

All 21 mockups fall within the 300–400 KB target range. No outliers.

| Mockup | Size | In Range |
|--------|------|----------|
| container-growing-blueprint-pack-mockup.png | 341.9 KB | PASS |
| grow-your-own-hot-sauce-mockup.png | 344.3 KB | PASS |
| companion-planting-chart-mockup.png | 345.7 KB | PASS |
| 12-month-urban-growing-planner-mockup.png | 346.0 KB | PASS |
| apartment-seed-starting-kit-mockup.png | 346.5 KB | PASS |
| seed-swap-hosting-kit-mockup.png | 346.7 KB | PASS |
| harvest-preservation-field-manual-mockup.png | 349.0 KB | PASS |
| seed-saving-field-manual-mockup.png | 349.5 KB | PASS |
| small-scale-livestock-field-manual-mockup.png | 351.2 KB | PASS |
| survival-garden-regional-plans-mockup.png | 352.7 KB | PASS |
| apartment-plant-catalog-mockup.png | 352.8 KB | PASS |
| food-sovereignty-starter-guide-mockup.png | 352.8 KB | PASS |
| heirloom-variety-selection-guide-mockup.png | 352.8 KB | PASS |
| native-plants-regional-guide-mockup.png | 354.8 KB | PASS |
| fermented-preserved-harvest-handbook-mockup.png | 364.2 KB | PASS |
| hunting-fishing-trapping-field-manual-mockup.png | 365.3 KB | PASS |
| anti-catalog-30-heirlooms-mockup.png | 373.7 KB | PASS |
| apartment-growing-complete-guide-mockup.png | 370.3 KB | PASS |
| meat-fish-preservation-field-manual-mockup.png | 388.9 KB | PASS |
| zone-seed-starting-calendar-mockup.png | 388.0 KB | PASS |
| free-5-easiest-vegetables-mockup.png | 360.5 KB | PASS |

### Visual Inspection (3 mockups)

Three mockups were visually inspected for AI artifacts, layout clarity, and thumbnail legibility:

**companion-planting-chart-mockup.png** — Clean tablet mockup, dark green product cover visible,
price badge ($5) present, Seedwarden tagline in footer. Product title visible in thumbnail.
No AI artifacts detected. PASS.

**zone-seed-starting-calendar-mockup.png** — Clean tablet mockup, product title readable, price
badge ($18) present. Minor note: the mockup displays "$18 (Complete Bundle)" — the Phase 1 listing
price for this product is $8 (individual). Verify the correct price is shown in this mockup before
uploading, or confirm this mockup is designated for a bundle listing, not the individual calendar.
FLAG for user review.

**survival-garden-regional-plans-mockup.png** — Clean tablet mockup, product title and subtitle
visible, price badge ($18) correct for this listing. No AI artifacts. PASS.

---

## Section 3: Title and Description Compliance (Spot-Check)

Three Phase 1 products spot-checked: Companion Planting Chart, Survival Garden Regional Plans,
and Zone-by-Zone Seed Starting Calendar (substituted for Pest Management Guide, which is not
a Phase 1 product).

### Titles

| Product | Title | Length | Symbols | Result |
|---------|-------|--------|---------|--------|
| Companion Planting Chart | "Companion Planting Chart PDF \| 40 Vegetables Herbs Flowers \| What to Plant Together Garden Reference Printable Wall Chart" | 121 chars | None | PASS |
| Zone Seed Starting Calendar | "Seed Starting Calendar by Zone \| USDA Zones 3-10 Planting Schedule \| Digital PDF Gardening Guide" | 96 chars | None | PASS |
| Survival Garden Regional Plans | "Survival Garden Plan 7 US Regions \| Calorie Focused Food Garden Layout \| Printable PDF" | 86 chars | None | PASS |

All three titles are under the 140-character Etsy limit, contain no forbidden symbols, and
front-load the primary keyword in the first 3–5 words.

### Descriptions (First 160 Characters)

**Companion Planting Chart**: Opens with "Stop Googling 'can I plant tomatoes next to peppers'
every spring." — conversational hook with the primary use case embedded. Keyword-dense without
being stuffed. No excessive caps. No banned phrases. PASS.

**Zone-by-Zone Seed Starting Calendar**: Opens with a pain-point quote ("Plant after danger of
frost" is the most useless advice in gardening). Primary keyword "seed starting" does not appear
in the first 160 characters — it appears in the title and later in the description. Etsy weighs
the title heavily for search matching, so this is acceptable. No banned phrases, no caps abuse.
PASS with note: consider adding "seed starting calendar" earlier in the body if search rank
is underperforming after launch.

**Survival Garden Regional Plans**: Opens with a direct product summary ("Seven regions, two
growing systems each, full seed lists..."). Dense with relevant keywords. No banned phrases.
No excessive caps. PASS.

All three descriptions are well within the 20,000 character Etsy limit.

---

## Section 4: Tag Compliance

Etsy's hard limit is 20 characters per tag. Tags over 20 characters are silently truncated or
rejected, breaking keyword matching.

### Previously Corrected Tags (from UPLOAD_SEQUENCE.md)

7 products had corrections documented in UPLOAD_SEQUENCE.md. All corrected tag sets were
re-validated character by character.

| Product | Tags | Max Length | Result |
|---------|------|-----------|--------|
| Food Sovereignty Starter Guide | 13 | 20 chars | PASS |
| Seed Saving Field Manual | 13 | 20 chars | PASS |
| Apartment Seed Starting Kit | 13 | 20 chars | PASS |
| Seed Swap Hosting Kit | 13 | 19 chars | PASS |
| Anti-Catalog: 30 Heirlooms | 13 | 20 chars | PASS |
| Apartment Plant Catalog | 13 | 19 chars | PASS |

### REMAINING VIOLATIONS — Correct Before Uploading

Three tag issues were found that are NOT fixed in the current UPLOAD_SEQUENCE.md. These must
be corrected before entering tags in Etsy.

---

**Issue 1: Survival Garden Regional Plans**

UPLOAD_SEQUENCE.md notes that `self sufficient garden` is "exactly 20 characters — acceptable."
This is incorrect. `self sufficient garden` is 22 characters and will be rejected.

Replace this one tag:
- OLD (22 chars, FAILS): `self sufficient garden`
- NEW (15 chars, PASSES): `self-sufficient`

Full corrected tag set for this product (apply instead of what is in UPLOAD_SEQUENCE.md):
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

**Issue 2: Zone-by-Zone Seed Starting Calendar**

`veggie planting guide` in the UPLOAD_SEQUENCE.md corrected set is 21 characters.

Replace this one tag:
- OLD (21 chars, FAILS): `veggie planting guide`
- NEW (18 chars, PASSES): `veggie plant guide`

Full corrected tag set for this product (apply instead of what is in UPLOAD_SEQUENCE.md):
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

**Issue 3: Companion Planting Chart — No Corrections Exist in UPLOAD_SEQUENCE.md**

The Companion Planting Chart is the #1 upload product. Its original tags in `etsy-store-copy.md`
have 10 of 12 tags over 20 characters, and only 12 tags are listed (Etsy allows 13). No
corrected set was ever written into UPLOAD_SEQUENCE.md.

Do not copy tags from `etsy-store-copy.md` for this product. Use this replacement set:

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

All 13 tags are 20 characters or under (max: 20, "plant together guide" and "vegetable
companions" and "garden reference pdf" and "organic garden guide"). This set preserves the
core SEO terms: companion planting, planting chart, vegetable garden, raised bed, organic
garden, printable reference.

---

### Full Tag Compliance Summary

| Product | Corrected Set Source | Status |
|---------|---------------------|--------|
| Companion Planting Chart | Section 4 above (this file) | READY |
| Food Sovereignty Starter Guide | UPLOAD_SEQUENCE.md | READY |
| Anti-Catalog: 30 Heirlooms | UPLOAD_SEQUENCE.md | READY |
| Seed Saving Field Manual | UPLOAD_SEQUENCE.md | READY |
| Apartment Plant Catalog | etsy-store-copy.md (original OK) | READY |
| Survival Garden Regional Plans | Section 4 above (corrected) | READY |

---

## Section 5: Day-by-Day Upload Schedule

From UPLOAD_SEQUENCE.md. Reproduced here for convenience.

**Day 1 — Monday, April 28**
- Morning: Complete one-time shop setup (icon, banner, announcement, about, policies)
- 10–11 AM: Upload listing #1 — Companion Planting Chart ($5)
- 2–3 PM: Upload listing #2 — Food Sovereignty Starter Guide ($8)
- Shop stays private/draft until Day 3

**Day 2 — Tuesday, April 29**
- 10 AM: Upload listing #3 — Anti-Catalog: 30 Heirlooms ($10)
- 2 PM: Upload listing #4 — Seed Saving Field Manual ($14)
- Verify first two listings display correctly on mobile and desktop

**Day 3 — Wednesday, April 30**
- 9 AM: Upload listing #5 — Apartment Plant Catalog ($14)
- 11 AM: Upload listing #6 — Survival Garden Regional Plans ($18)
- Noon: Switch shop from private to Active
- Immediately: Announce on email list and social media

**Estimated time per product**: 15–20 minutes (copy-paste workflow using pre-written copy)
**Total upload time**: 6 products x 15–20 min = 1.5–2 hours across 3 days
**Per-day commitment**: 30–40 minutes

---

## Section 6: Post-Upload Monitoring Checklist

### Day 3 — Within 1 Hour of Going Public

- [ ] View each listing on a mobile device — verify image loads and title is readable in thumbnail
- [ ] View each listing in a logged-out browser — verify Add to Cart button appears
- [ ] Test purchase one low-priced listing (Companion Planting Chart at $5 is ideal)
- [ ] Confirm download link works after purchase and delivers the correct PDF
- [ ] Share shop link to all social media bios immediately

### 24–48 Hours Post-Launch

- [ ] Check Shop Manager Stats: which listings have views? Any favorites?
- [ ] Verify all 6 listings are indexed (search for each product title in Etsy search)
- [ ] Confirm "Instant download" delivery is shown on every listing
- [ ] Respond to any buyer messages within 24 hours

### Week 1

- [ ] Track views per listing daily for 7 days
- [ ] Note which listing gets first sale — prioritize similar products for Phase 2
- [ ] If a listing has 50+ views but no sales: review mockup quality, price vs. competition,
  and description opening line
- [ ] If a listing has under 5 views in 48 hours: re-verify tags for 20-char compliance and
  confirm title front-loads primary keyword
- [ ] Begin Phase 2 planning when first sale is confirmed

---

## Section 7: 3 Required Manual Actions Before Uploading

These cannot be completed by this agent. The user must confirm or complete each one.

**Action 1 — Apply the corrected tag sets**

Do not use raw tags from `etsy-store-copy.md`. Three products need corrections that are not
fully captured in `UPLOAD_SEQUENCE.md`:
- Companion Planting Chart: use the full 13-tag set from Section 4 of this file
- Survival Garden Regional Plans: replace `self sufficient garden` with `self-sufficient`
- Zone-by-Zone Seed Starting Calendar: replace `veggie planting guide` with `veggie plant guide`
All other products: use the corrected sets from UPLOAD_SEQUENCE.md as written.

**Action 2 — Verify Etsy account is active**

Confirm that the Etsy seller account is active, that Etsy Payments is connected, and that the
account is not in any hold or suspended state before beginning the shop setup on Day 1.
A seller account in review or hold will prevent listing publication even if all content is ready.

**Action 3 — Confirm social media accounts are ready for launch announcement**

On Day 3, noon, the shop goes public and an announcement should go out immediately. Confirm
in advance that at least one social media account (Instagram, TikTok, or Pinterest) is active
and that the launch post is drafted and ready to publish on the day.

---

## Section 8: Phase 2 Enhancements

The following enhancements are optional and should be prioritized based on Phase 1 conversion
data. Do not spend time on these until at least 7 days of live listing data is available.

**Phone mockups**
Add portrait-orientation phone mockups (1080x1920 or equivalent) as image slots 2–3 in each
listing. Phone mockups capture buyers browsing on mobile, who represent the majority of Etsy
traffic. Prioritize the listings with highest view-to-sale ratio first.

**Lifestyle photography**
Flat-lay or "in use" photos showing the printed guide alongside seeds, garden tools, or produce.
Lifestyle images increase perceived value and conversion rate. Test on the first product that
reaches 100 views without a sale before rolling out broadly.

**Printed page mockups**
Show an interior page of the PDF alongside the cover mockup. This is especially useful for
chart-style products (Companion Planting Chart, Seed Starting Calendar) where buyers want to
see the content format before purchasing. A printed-page mockup in image slot 2 can reduce
buyer hesitation for higher-priced listings.

Rollout order recommendation (based on expected conversion data):
1. Companion Planting Chart — high volume, low price, test mockup formats here first
2. Seed Saving Field Manual — highest technical depth, interior page mockup adds credibility
3. Survival Garden Regional Plans — highest price point, lifestyle shot justifies $18 price

---

## Validation Sign-Off

| Check | Result |
|-------|--------|
| 6 Phase 1 PDFs present and under 5 MB | PASS |
| All 21 mockups 2400x2400 px | PASS |
| All 21 mockups 300–400 KB | PASS |
| 3 mockups visually inspected, no AI artifacts | PASS (1 flag on zone calendar price badge) |
| Titles: 3 spot-checked, all <=140 chars, no forbidden symbols | PASS |
| Descriptions: 3 spot-checked, first 160 chars keyword-rich, no banned phrases | PASS |
| UPLOAD_SEQUENCE.md corrected tags re-validated | 6 of 7 corrected products pass |
| Remaining tag violations documented with fixes | 3 issues documented in Section 4 |
| Upload schedule documented | PASS |
| Post-upload monitoring checklist present | PASS |
| 3 manual user actions documented | PASS |

**Overall status**: READY TO UPLOAD after applying the 3 tag corrections in Section 4 and
completing the 3 manual actions in Section 7.
