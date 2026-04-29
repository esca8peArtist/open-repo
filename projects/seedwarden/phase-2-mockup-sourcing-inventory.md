---
title: "Seedwarden Phase 2 — Mockup Sourcing Inventory"
prepared: 2026-04-29
status: production-ready
scope: 21 Phase 2 products — iStock and Unsplash search strings, file format requirements, naming convention, timeline
cross-references:
  - phase-2-mockup-production-plan.md (method assignments per product)
  - phase-2-photography-strategy.md (aesthetic and licensing guidance)
  - WORKLOG.md (download log — required after each acquisition)
---

# Phase 2 Mockup Sourcing Inventory

**Purpose**: Per-product search string reference for stock image acquisition. Every product that uses a stock or Wikimedia source has its primary and fallback search strings listed here, along with the expected image count, format requirements, and the naming convention that connects sourced images to the rest of the pipeline.

Use this document when sitting down for a stock sourcing session. Work down the tier list in order. Cross off each item as the image is downloaded and logged in WORKLOG.md.

---

## File Format Requirements (all sourced images)

**Download format**: Original or largest available JPEG. Do not download compressed preview or watermarked versions.

**Minimum resolution**: 3000px on the shortest side. Anything smaller cannot be cropped and composited into a 2400×2400px output without visible quality loss.

**Color mode**: RGB (not CMYK). Verify in image properties before downloading from iStock — iStock sometimes serves editorial images in CMYK.

**Preferred aspect ratio**: Horizontal (landscape) or square. Vertical originals work but reduce cropping flexibility during compositing. Note preferred ratio in the search string column below — filter by it when the platform allows.

**File size**: iStock delivers full-resolution downloads as JPEG or TIFF. Prefer JPEG. For Wikimedia Commons, use the "Download" link and select the original resolution, not a web-optimized version.

**Staging directory**: All sourced images (pre-compositing) go to `projects/seedwarden/assets/stock-raw/` with the filename `[product-slug]-source-[n].jpg` where n is the image number if multiple were downloaded for the same product. Do not rename the file to the final output name until compositing is complete and QA is passed.

---

## Naming Convention for Batch Processing

All final output files follow the naming convention defined in `phase-2-mockup-production-plan.md`. Repeated here for quick reference during batch sessions:

| Output type | Pattern | Example |
|-------------|---------|---------|
| Etsy slot 4 (lifestyle/flat-lay) | `[slug]-slot4.jpg` | `seed-saving-field-manual-slot4.jpg` |
| Etsy slot 5 (in-use/contextual) | `[slug]-slot5.jpg` | `seed-saving-field-manual-slot5.jpg` |
| Pinterest pin | `[slug]-pin.jpg` | `seed-saving-field-manual-pin.jpg` |
| Instagram/TikTok crop | `[slug]-social.jpg` | `seed-saving-field-manual-social.jpg` |
| Raw stock source (staging) | `[slug]-source-[n].jpg` | `seed-saving-field-manual-source-1.jpg` |

Final output directory: `projects/seedwarden/marketing/lifestyle-photos/etsy-ready/`

**Slugs for all 21 products** are listed in the slug reference table in `phase-2-mockup-production-plan.md`. Do not invent new slugs — use the exact strings in that table so filenames stay consistent with existing mockup slot 1–3 files.

---

## Sourcing Timeline

| Phase | Days | Work | Products covered |
|-------|------|------|-----------------|
| Stock sourcing sprint 1 | Days 1–3 | Cluster D: 4 products, iStock primary | Survival Garden, Hunting Manual, Livestock Manual, Meat/Fish Preservation |
| Stock sourcing sprint 2 | Day 8 | Cluster E: 1 product, Wikimedia primary | Native Plants Regional Guide |
| Physical shoot — Cluster C | Day 5 (Week 1) + Day 1 (Week 2) | No sourcing; shoot from props | Harvest Preservation, Fermented Harvest, Hot Sauce |
| Physical shoot — Cluster A | Day 2 (Week 2) | No sourcing; shoot from props | Seed Saving, Heirloom Guide, Anti-Catalog, Companion Planting, Zone Calendar, Food Sovereignty, Apt Seed Starting, Urban Planner, Free 5 Easiest |
| Physical shoot — Cluster B | Day 3 (Week 2) | No sourcing; shoot from props | Container Growing, Apartment Growing Guide, Apartment Plant Catalog, Seed Swap Kit |
| Compositing | Days 1–2 (Week 3) | Assemble all stock composites | All stock-sourced products |
| QA + export | Days 3–4 (Week 3) | Final checks and export | All 21 products |

**Total stock sourcing sessions**: 2 dedicated sessions (Sprint 1 and Sprint 2). Everything else is physical photography — no online search required.

**iStock credit allocation**: Budget a maximum of 5 credits across the entire Phase 2 sourcing sprint. Cluster D gets first claim (up to 4 credits); Cluster E uses Wikimedia at no cost. Do not purchase iStock credits beyond 5 — if a Cluster D product cannot be sourced at iStock within budget, use Pexels (free) or the AI composite fallback described in `phase-2-mockup-production-plan.md`.

---

## Tier 1 Products — Stock Sourcing (Cluster D)

### 1. Survival Garden Regional Plans — slug: `survival-garden-regional-plans`

**Method**: Stock composite (iStock or Pexels)
**Images needed**: 2 (one for slot 4, one for slot 5)
**Expected count from search** (how many results the search typically returns): 200–400 on iStock, 80–150 on Pexels

**Slot 4 — primary lifestyle/flat-lay**:
- iStock search string: `raised bed garden rows planning overhead` — filter: horizontal or square, lifestyle/real people, not illustration
- iStock fallback 1: `homestead garden planning table outdoor`
- iStock fallback 2: `vegetable garden layout aerial view`
- Pexels fallback: `raised bed vegetable garden` (search), filter for horizontal
- What to select for: scene that reads as planning (maps, notes, or layout visible in the scene) rather than just a garden photo. The guide will be composited in as though spread on the surface.
- Reject if: commercial farm scale, artificial-looking staging, chrome or modern patio furniture, or any scene that reads as aspirational real estate rather than a working homestead.

**Slot 5 — in-use/contextual**:
- iStock search string: `hands garden planning outdoor table`
- iStock fallback: `garden layout planning notes person`
- Pexels fallback: `person planning garden outdoor`
- What to select for: hands interacting with a surface (table, ground cloth, bale of hay) where the guide can be composited to appear as though open in the scene.

**iStock credits**: 1 (slot 4 only — if Pexels yields an acceptable slot 5, save the credit)
**WORKLOG entry required**: Yes — after each download

---

### 2. Hunting, Fishing and Trapping Manual — slug: `hunting-fishing-trapping-manual`

**Method**: Stock composite (iStock priority — Pexels is thin for this niche)
**Images needed**: 2
**Expected count from search**: 150–300 on iStock (hunting and fishing content is available but not abundant); Pexels has minimal usable hunting lifestyle content

**Slot 4 — primary lifestyle/flat-lay**:
- iStock search string: `fly fishing stream rustic lifestyle` — filter: horizontal, no commercial fishing
- iStock fallback 1: `outdoor field guide jacket pocket lifestyle`
- iStock fallback 2: `trapper cabin rustic morning` (for trapping product alignment)
- What to select for: outdoor setting that reads as self-sufficient, not sport or trophy. Stream, field edge, woodland, or a simple outdoor table. Guide will be composited as open on a flat surface or visible in a pack/pocket.
- Reject if: mounted trophies, competition sport contexts, commercial fishing gear, or anything that reads as big-game trophy hunting rather than subsistence and field skills.

**Slot 5 — in-use/contextual**:
- iStock search string: `hands open field guide outdoor nature`
- iStock fallback: `fishing guide hands water reading`
- What to select for: a hand or hands interacting with pages in an outdoor context. The guide must appear to be actively consulted, not posed.

**iStock credits**: 2 (this product gets priority credit allocation per `phase-2-mockup-production-plan.md`)
**WORKLOG entry required**: Yes

---

### 3. Small-Scale Livestock Field Manual — slug: `small-scale-livestock-field-manual`

**Method**: Stock composite (iStock or Pexels — Pexels has decent backyard chicken coverage; check free sources first)
**Images needed**: 2
**Expected count from search**: Pexels backyard chicken: 100–200 usable results; iStock: 300+ but variable quality at small-farm scale

**Slot 4 — primary lifestyle/flat-lay**:
- Pexels search string (check first): `backyard chickens small farm`
- Pexels fallback: `homestead chickens morning`
- iStock search string (if Pexels is insufficient): `backyard chickens homestead lifestyle`
- iStock fallback: `small farm morning routine goats ducks`
- What to select for: domestic scale (backyard, not commercial). Imperfect coops, functional fencing, actual morning chore context. One or two animals is better than a flock suggesting commercial scale.
- Reject if: commercial poultry operation scale, aspirational "farmhouse" staging with styled props, or any image that reads as a stock photo rather than a real small farm.

**Slot 5 — in-use/contextual**:
- Pexels search string: `homesteader reading outdoors farm`
- iStock fallback: `homesteader reading guide barn`
- What to select for: person near animal housing or in a working outdoor context, with a surface or hands that allow guide compositing.

**iStock credits**: 1 (only if Pexels cannot supply a sufficient slot 4 image)
**WORKLOG entry required**: Yes

---

### 4. Meat and Fish Preservation Field Manual — slug: `meat-fish-preservation-field-manual`

**Method**: Stock composite (Pexels first, iStock fallback)
**Images needed**: 2
**Expected count from search**: Pexels home preservation: 80–160 results; iStock artisan charcuterie: 200–400

**Slot 4 — primary lifestyle/flat-lay**:
- Pexels search string (check first): `home meat preservation artisan`
- Pexels fallback 1: `artisan charcuterie wooden board`
- Pexels fallback 2: `smoked meat hanging rack`
- iStock search string (fallback): `artisan charcuterie rustic lifestyle`
- iStock fallback: `home smokehouse exterior traditional`
- What to select for: rustic and functional — salt-cured meat, a smoking rack, a cutting board with preserved product. The guide is composited as open next to the preservation setup. Color temperature should read warm and earthy, not food-magazine clinical.
- Reject if: commercial food production scale, overly styled food photography, clinical white backgrounds.

**Slot 5 — in-use/contextual**:
- Pexels search string: `hands slicing cured meat wooden board`
- Pexels fallback: `food preservation process kitchen hands`
- iStock fallback: `artisan meat curing hands`
- What to select for: hands engaged in a preservation task on a wooden or stone surface where guide pages can be composited nearby.

**iStock credits**: 1 (fallback only — Pexels likely sufficient)
**WORKLOG entry required**: Yes

---

## Tier 2 Products — Physical Photography (Clusters A, B, C)

These products require no stock image sourcing. All assets come from physical photography sessions. The table below is a reference for what props and setups to prepare before each session — not a sourcing list.

### Cluster C Physical Session (Tier 1: Product 5; Tier 2: Products 6–7)

| Product | Slug | Key Props Needed | Shoot Session |
|---------|------|-----------------|---------------|
| Harvest Preservation Field Manual | `harvest-preservation-field-manual` | 3–4 mason jars (used look, real contents), canning funnel or jar lifter, wooden surface | Cluster C, Day 5 Week 1 |
| Fermented and Preserved Harvest Handbook | `fermented-preserved-harvest-handbook` | Add fermentation crock weights, one jar actively bubbling or showing ferment visible | Cluster C, Day 1 Week 2 |
| Grow Your Own Hot Sauce | `grow-your-own-hot-sauce` | Dried chilis, fresh peppers, cutting board, mortar and pestle or empty glass bottle | Cluster C, Day 1 Week 2 |

**No sourcing actions needed.** Shoot from props. Sourcing step is prop acquisition: purchase dried chilis and fresh peppers, and verify mason jar supply, before the Cluster C session.

---

### Cluster A Physical Session (Products 8–17)

| Product | Slug | Key Prop Variation |
|---------|------|--------------------|
| Seed Saving Field Manual | `seed-saving-field-manual` | Seed envelopes fanned, one open with seeds spilling, wooden surface |
| Heirloom Variety Selection Guide | `heirloom-variety-selection-guide` | Multiple seed packets suggesting comparison; handwritten variety list |
| Anti-Catalog: 30 Heirlooms | `anti-catalog-30-heirlooms` | Multiple seed packets variety spread overhead |
| Companion Planting Chart | `companion-planting-chart` | Two small pots with different plant species together |
| Zone-by-Zone Seed Starting Calendar | `zone-by-zone-seed-starting-calendar` | Seed starting tray, printed calendar page |
| Food Sovereignty Starter Guide | `food-sovereignty-starter-guide` | Seed envelopes with hand-written labels |
| Apartment Seed Starting Kit | `apartment-seed-starting-kit` | Small cell trays with starter mix and seeds |
| 12-Month Urban Growing Planner | `12-month-urban-growing-planner` | Printed planner page, small pot, pencil |
| Free 5 Easiest Vegetables Guide | `free-5-easiest-vegetables-guide` | 3 seed packets, guide page — minimal arrangement |

**No sourcing actions needed.** Cluster A session is one continuous setup (wooden surface, natural light) with prop swaps between products. Estimated total shoot time: 4 hours including setup.

---

### Cluster B Physical Session (Products 18–21)

| Product | Slug | Key Prop / Setting |
|---------|------|-------------------|
| Container Growing Blueprint Pack | `container-growing-blueprint-pack` | 2–3 containers of different sizes, window light, balcony or window context |
| Apartment Growing Complete Guide | `apartment-growing-complete-guide` | Potted herbs on window sill, grow light optional but authentic if available |
| Apartment Plant Catalog | `apartment-plant-catalog` | Multiple small potted plants, varied species on a shelf or sill |
| Seed Swap Hosting Kit | `seed-swap-hosting-kit` | Seed envelopes being sorted on a table, community table context |

**No sourcing actions needed.** Cluster B session requires urban/small-space setting — a window with a view or visible balcony railing in the background is the key differentiator from Cluster A images.

---

## Tier 2 Product — Wikimedia Sourcing (Cluster E)

### 10. Native Plants Regional Guide — slug: `native-plants-regional-guide`

**Method**: Wikimedia Commons botanical/habitat photos + optional Pexels foraging context image
**Images needed**: 2 (slot 4: habitat overview; slot 5: forager-relationship image)
**License required**: CC BY-SA or CC0 only. Verify before downloading. CC BY-SA requires attribution in the product's photo credits page.
**Expected count from search**: 30–80 usable results per species search; broader habitat category searches return 200+.

**Slot 4 — habitat/overview**:
- Wikimedia search URL pattern: `https://commons.wikimedia.org/wiki/Special:Search?search=[species+name]+habitat`
- Primary search strings:
  - `native wildflower meadow habitat North America`
  - `native prairie plants habitat`
  - `woodland edge native plants`
  - `[specific species name] habitat` — use the most regionally representative species in the guide
- Wikimedia category to browse: `https://commons.wikimedia.org/wiki/Category:Native_plants_of_North_America`
- What to select for: a scene showing a native plant community in its natural ecological context, not a botanical closeup. Companion plants and habitat context should be visible. The guide cover or a native plant ID page will be composited in the foreground.
- Reject if: botanical illustration (correct aesthetic is photographic), horticultural nursery setting, or any image that shows the plant outside its natural habitat.

**Slot 5 — forager/field relationship**:
- Pexels search string: `foraging wild plants hands`
- Pexels fallback: `forager basket wild harvested`
- Wikimedia fallback: `foraging hands field botanical`
- What to select for: a person or hands examining, collecting, or holding a wild plant in a field setting. The relationship between a person and the plant in the field — not a studio botanical photo.

**Attribution handling**: Log the exact Wikimedia file URL, the license type (CC BY-SA version number), and the photographer's name in WORKLOG.md. This information goes into the product's photo credits page in the PDF before Etsy upload.

**iStock credits**: 0 — Wikimedia only for this product.
**WORKLOG entry required**: Yes, including full attribution text.

---

## Summary Counts

| Category | Products | Images to source | Source |
|----------|----------|-----------------|--------|
| Cluster D — stock composite | 4 | 8 (2 per product) | iStock + Pexels |
| Cluster E — Wikimedia | 1 | 2 | Wikimedia + Pexels |
| Cluster C — physical | 3 | 0 (shoot from props) | — |
| Cluster A — physical | 10 | 0 (shoot from props) | — |
| Cluster B — physical | 4 | 0 (shoot from props) | — |
| **Total** | **21** | **10 stock images** | — |

**Total stock images to source**: 10 (8 from iStock/Pexels, 2 from Wikimedia/Pexels)
**Maximum iStock credits**: 5 (ideally 4 or fewer)
**Physical shoot sessions**: 3 (Clusters C, A, B)

---

## First 5 Search Examples (Ready to Execute)

These are the first 5 searches to run when beginning the stock sourcing sprint, in execution order:

1. **Survival Garden slot 4** — iStock: `raised bed garden rows planning overhead` — filter horizontal, lifestyle, not illustration. Target: 1 image showing planning context.

2. **Survival Garden slot 5** — iStock or Pexels: `hands garden planning outdoor table` — Target: 1 image with hands-in-frame in a garden planning context.

3. **Hunting Manual slot 4** — iStock: `fly fishing stream rustic lifestyle` — filter horizontal. Target: 1 image at stream or field edge, rustic and functional.

4. **Hunting Manual slot 5** — iStock: `hands open field guide outdoor nature` — Target: 1 image of hands with pages in an outdoor context.

5. **Livestock Manual slot 4** — Pexels first: `backyard chickens small farm` — filter horizontal. Target: 1 image showing backyard/domestic scale livestock. Use iStock `backyard chickens homestead lifestyle` if Pexels is insufficient.
