# Seedwarden Mockup Strategy & Implementation
## Status: COMPLETE — 21/21 Products Ready for Launch

**Last Updated:** April 26, 2026  
**Completion Status:** ✅ All 21 products have tablet mockup images generated and ready for Etsy listings

---

## Executive Summary

All 21 Seedwarden products have professional mockup images ready for launch. Tablet mockup images (2400×2400px PNG) show each product's PDF on a realistic iPad-style device, providing the #1 conversion factor for digital products on Etsy. No additional mockup generation needed.

**What's Complete:**
- 21 tablet mockup images (one per product) — ready for Etsy primary image slot
- High resolution (2400×2400px) — meets Etsy's zoom-functionality requirement (2000px+ shortest side)
- Consistent brand design — matching seedwarden color palette and layout
- Professional quality — suitable for primary (cover) image on all listings

**What's Ready to Deploy:**
- All mockup images in `/projects/seedwarden/mockups/` directory
- Script for regenerating mockups if PDFs change: `scripts/generate_mockups.py`
- No additional tools or dependencies required

---

## Current Mockup Architecture

### Image Specifications

| Specification | Value |
|---|---|
| Format | PNG (RGB, 8-bit color) |
| Resolution | 2400×2400 pixels |
| Size per image | 350–400 KB (highly optimized) |
| Device type | iPad/Tablet in portrait orientation |
| Content shown | Top 55% of PDF first page (rich header + title area) |
| Aspect ratio | 1:1 square (optimal for Etsy grid thumbnails) |
| Color management | Consistent brand green (#143b28) + device bezel |

### Visual Design

Each mockup shows:
1. **Tablet device frame** — realistic aluminum bezel with rounded corners, camera dot, home button
2. **Screen content** — PDF cover page (top 55% of page, where visual branding is strongest)
3. **Background** — subtle sage gradient (light warm white to deeper sage)
4. **Drop shadow** — soft shadow behind tablet for depth perception
5. **Highlights** — thin edge highlight on top-left for dimension

The design is programmatically generated — no external design tools or licensed assets needed.

---

## Product Coverage

All 21 products have mockups:

| Product | Mockup | Status |
|---|---|---|
| Food Sovereignty Starter Guide | ✅ | Ready |
| Seed Saving Field Manual | ✅ | Ready |
| Apartment Seed Starting Kit | ✅ | Ready |
| 12-Month Urban Growing Planner | ✅ | Ready |
| Container Growing Blueprint Pack | ✅ | Ready |
| Seed Swap Hosting Kit | ✅ | Ready |
| Heirloom Variety Selection Guide | ✅ | Ready |
| Fermented & Preserved Harvest Handbook | ✅ | Ready |
| Grow Your Own Hot Sauce | ✅ | Ready |
| Anti-Catalog: 30 Heirlooms | ✅ | Ready |
| Small-Scale Livestock Field Manual | ✅ | Ready |
| Meat/Fish Preservation Field Manual | ✅ | Ready |
| Harvest Preservation Field Manual | ✅ | Ready |
| Native Plants Regional Guide | ✅ | Ready |
| Apartment Plant Catalog | ✅ | Ready |
| Survival Garden Regional Plans | ✅ | Ready |
| Hunting, Fishing & Trapping Manual | ✅ | Ready |
| Apartment Growing Complete Guide | ✅ | Ready |
| Companion Planting Chart | ✅ | Ready |
| Zone-by-Zone Seed Starting Calendar | ✅ | Ready |
| Free: 5 Easiest Vegetables | ✅ | Ready |

---

## Etsy Best Practices — Implemented

### Image Quality & Technical Compliance

✅ **High resolution** — All mockups are 2400×2400px, exceeding Etsy's minimum of 2000px on shortest side. This enables Etsy's zoom viewer, allowing customers to see product details.

✅ **Square format** — 1:1 aspect ratio performs best in Etsy's grid display and minimizes cropping on mobile devices.

✅ **Optimized file size** — 350–400 KB per image balances quality and load speed.

### Mockup Best Practices

✅ **Device mockup** — Tablet format is the most effective for digital products. It immediately communicates "digital download" without requiring customers to interpret an abstract cover.

✅ **Realistic context** — The aluminum device bezel, shadow, and background create a professional, trustworthy appearance. Research shows realistic mockups increase conversion rates significantly compared to plain screenshots.

✅ **Focused content** — Mockup captures top 55% of PDF (header + title), where the most visually interesting content lives, avoiding blank space that would reduce visual appeal.

✅ **Brand consistency** — All mockups use the same design system, ensuring the Seedwarden store maintains visual cohesion across all 21 products.

---

## Etsy Listing Image Strategy

### Primary Image (Slot 1)
Use the tablet mockup. This should be the first image customers see in search results and on the listing page.

**Why:** 
- Tablet mockups convert better than plain screenshots (research from MyDesigns, 2026)
- Immediately communicates "digital product"
- Shows scale and context
- High resolution enables zoom inspection

### Additional Images (Slots 2–10)
Etsy allows up to 10 images per listing. For maximum conversion potential, consider adding:

**Recommended additional images:**
1. **Cover mockup** (current primary image — tablet mockup)
2. **Page interior mockup** — Show a sample interior page on the same tablet frame (demonstrates content depth)
3. **Flat lay mockup** — Printed pages spread on a wooden desk/outdoor setting (appeals to customers who print products)
4. **Device mockup variation** — Same PDF on a phone or laptop to show compatibility
5. **Lifestyle shot** — PDF being used in actual context (e.g., planner on desk while gardening, guide in hand in field)
6. **Text close-up** — Detail shot highlighting writing quality and depth
7. **Comparison/scale shot** — Page next to a hand or coffee cup to show size
8. **Color/design detail** — Highlight the branded cover design elements
9. **Features list** — Graphic listing what's included
10. **Customer testimonial/benefit** — Visual showing the value proposition

**Current Status:** Only slot 1 (primary mockup) is complete. Slots 2–10 would require:
- Additional mockup angles (phone, laptop, printed pages)
- Lifestyle photography
- Graphic design for benefits/features

### Recommended Sequencing for Launch

For Phase 1 launch (6 products):
1. Use tablet mockups as primary images (slots 1) for all 6 products
2. Add basic interior page mockups for slots 2 (will increase if time allows)
3. Monitor conversion rates for first 2 weeks
4. Add additional mockup angles (phone, printed pages) in Phase 2 based on performance

---

## Regeneration Workflow

If product PDFs are updated, mockups can be regenerated instantly using the existing script.

### Regenerate All Mockups

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/seedwarden
uv run python scripts/generate_mockups.py
```

**What this does:**
- Scans `/scripts/output/` for all .pdf files
- Renders the first page of each PDF
- Crops to the top 55% (title area)
- Composites onto a tablet device frame
- Saves high-res PNG to `/mockups/` directory
- Overwrites existing mockups without prompting

**Duration:** ~30 seconds for all 21 products
**Dependencies:** pypdfium2, Pillow (already in project)

### Regenerate Single Mockup

To regenerate just one product's mockup after editing its PDF:

```bash
uv run python scripts/generate_mockups.py
```

(The script processes all PDFs in the output directory. To regenerate just one, manually delete the old mockup and re-run the script, or modify the script to accept a product argument.)

### After PDF Regeneration

If you edit product markdown files and regenerate PDFs:
1. Run `generate_pdfs.py` to create updated PDFs
2. Run `generate_mockups.py` to create updated mockups
3. Commit both changes together: `git add scripts/output/ mockups/`

---

## Technical Implementation Details

### Script: `scripts/generate_mockups.py`

**Purpose:** Automate tablet mockup generation from PDF first pages

**Key Features:**
- **Programmatic design** — Entire tablet frame drawn with Pillow (PIL), no external assets or licensed images
- **Responsive rendering** — Handles PDFs of any size, crops to optimal content area
- **High-quality output** — Renders at 2× resolution then downscales for antialiasing
- **Batch processing** — Processes all 21 products in one command
- **Error handling** — Reports failures clearly without stopping the batch

**Input:** `/scripts/output/*.pdf` (all product PDFs)

**Output:** `/mockups/*-mockup.png` (tablet mockups, one per product)

**Colors used:**
- Brand green: #143b28 (RGB: 20, 59, 40) — matches logo
- Bezel aluminum: Light → Mid → Dark gradient
- Background: Sage gradient (warm white to deeper sage)
- Shadow: Soft drop shadow for depth

**Canvas dimensions:**
- 2400×2400 px total
- Tablet area: 1200×1580 px
- Bezel width: 60px (sides), 90px (top/bottom)
- Screen area: 1080×1400 px

### Dependencies

```python
pypdfium2     # PDF rendering
Pillow (PIL)  # Image compositing and drawing
```

Both are already in the project dependencies. No additional installation required.

---

## Future Enhancement Opportunities

### Short-term (Phase 2 — Week 3–4)

1. **Phone mockup variations** — Create alternative mockups showing the same PDF on iPhone/mobile screen
   - Helps customers see the product works on their phones
   - Quick to generate with modified script (swap device frame)
   - Estimated effort: 2–3 hours to create phone frame, 30 minutes to generate all variants

2. **Printed page mockups** — Show pages on a flat surface (desk, outdoor table, with coffee cup)
   - Targets customers who print digital products
   - Requires lifestyle photography or stock image integration
   - Estimated effort: 4–6 hours to design and test

3. **Interior page mockup** — Show an example page from inside the PDF instead of just the cover
   - Demonstrates content depth and quality
   - More realistic for a "sample" image
   - Can use same tablet frame, different PDF page
   - Estimated effort: 1–2 hours to modify script

### Medium-term (Phase 3 — Month 2)

4. **Lifestyle photography** — Real-world usage shots
   - Person reading on tablet in garden
   - Printed pages on a gardening workspace
   - Product being used in actual context
   - Requires shooting/photography or purchasing stock images
   - Estimated effort: 4–8 hours (includes props/setup)

5. **Comparison mockups** — Side-by-side of bundled products
   - Shows value in bundles
   - Visual emphasis for cross-selling
   - Estimated effort: 2–3 hours design + generation

6. **Features graphic** — Callout highlighting what's inside
   - Text overlay on mockup listing key features
   - Data-driven (shows why customers should buy)
   - Estimated effort: 2–4 hours design work

### Long-term Optimization

7. **A/B test variations** — Generate multiple thumbnail crops and test which performs best
   - Etsy's Experiments feature allows testing different primary images
   - Could test wide variety of angles and crops cheaply
   - Estimated effort: 3–5 hours testing across products

---

## Mockup Quality Assessment

### Current Strengths

- **Professional appearance** — Tablet device looks realistic and high-quality
- **Consistent branding** — All mockups use the same design language
- **High resolution** — Meets technical Etsy requirements
- **Fast generation** — Reproducible in seconds if PDFs change
- **No licensing concerns** — Programmatically generated, no copyrighted assets

### Limitations & Tradeoffs

- **Single angle** — Only tablet device, only front-facing view
- **No context** — Doesn't show the product "in use" or in a lifestyle setting
- **No people** — Impersonal compared to a human hand holding the device
- **Static background** — Neutral sage gradient works but is quite minimal
- **Cover-only view** — Only shows first page, not interior content

**Assessment:** Current mockups are solid and launch-ready. Adding 2–3 additional angles (phone, printed pages, lifestyle) in Phase 2 would boost conversion rates further, but is not required for launch.

---

## Etsy Launch Checklist — Mockups Section

- [x] **Primary mockup images created** (tablet mockups, all 21 products)
- [x] **Resolution meets Etsy requirements** (2400×2400px ≥ 2000px minimum)
- [x] **File format correct** (PNG, RGB, 8-bit)
- [x] **File sizes optimized** (350–400 KB per image)
- [x] **Mockup script documented** (can regenerate if PDFs change)
- [ ] *Optional:* Additional angles (phone, printed pages) — Phase 2
- [ ] *Optional:* Lifestyle photography — Phase 3
- [ ] *Optional:* Interior page mockups — Phase 2

**For immediate launch:** Tablet mockups only (all items above with [x] marked complete)

---

## File Organization

```
projects/seedwarden/
├── mockups/                           # Tablet mockups (ready for Etsy)
│   ├── 12-month-urban-growing-planner-mockup.png
│   ├── anti-catalog-30-heirlooms-mockup.png
│   ├── apartment-growing-complete-guide-mockup.png
│   ├── apartment-plant-catalog-mockup.png
│   ├── apartment-seed-starting-kit-mockup.png
│   ├── companion-planting-chart-mockup.png
│   ├── container-growing-blueprint-pack-mockup.png
│   ├── fermented-preserved-harvest-handbook-mockup.png
│   ├── food-sovereignty-starter-guide-mockup.png
│   ├── free-5-easiest-vegetables-mockup.png
│   ├── grow-your-own-hot-sauce-mockup.png
│   ├── harvest-preservation-field-manual-mockup.png
│   ├── heirloom-variety-selection-guide-mockup.png
│   ├── hunting-fishing-trapping-field-manual-mockup.png
│   ├── meat-fish-preservation-field-manual-mockup.png
│   ├── native-plants-regional-guide-mockup.png
│   ├── seed-saving-field-manual-mockup.png
│   ├── seed-swap-hosting-kit-mockup.png
│   ├── small-scale-livestock-field-manual-mockup.png
│   ├── survival-garden-regional-plans-mockup.png
│   └── zone-seed-starting-calendar-mockup.png
│
├── scripts/
│   ├── generate_mockups.py            # Tablet mockup generation (documented above)
│   ├── generate_pdfs.py               # PDF generation
│   └── output/                        # Source PDFs (input for generate_mockups.py)
│
├── products/                          # Source markdown files
├── MOCKUP_STRATEGY.md                 # This file
└── WORKLOG.md

```

---

## Deployment Instructions

### For Etsy Listing Upload

1. **Navigate to mockups directory:**
   ```bash
   cd /home/awank/dev/SuperClaude_Framework/projects/seedwarden/mockups/
   ```

2. **Select appropriate mockup for each product:**
   Use the filename to match product name, e.g.:
   - `food-sovereignty-starter-guide-mockup.png` → Food Sovereignty Starter Guide listing

3. **Upload as primary image:**
   On Etsy listing creation → "Photos" section → Upload first image → This tablet mockup

4. **Repeat for all 21 products** in Phase 1 and beyond

### For Quality Check Before Upload

1. **Verify all mockups exist:**
   ```bash
   ls mockups/*-mockup.png | wc -l  # Should output 21
   ```

2. **Spot-check a few images:**
   ```bash
   file mockups/*.png | grep -c "2400 x 2400"  # Should output 21
   ```

3. **Sample visual inspection:**
   Open 3–5 random mockups in an image viewer to verify:
   - Device frame is visible and clear
   - PDF content is readable
   - Pricing/title is visible
   - No artifacts or rendering errors

---

## Support & Troubleshooting

### Issue: Mockup looks blurry or low quality

**Solution:** This is likely a display issue, not a file issue. The original files are 2400×2400px. Check:
- Are you viewing at 100% zoom in your image viewer?
- Is the file really 2400×2400? Run: `identify mockups/[filename].png`

### Issue: Need to regenerate mockups after updating PDFs

**Solution:**
1. Update product markdown files
2. Run `uv run python scripts/generate_pdfs.py` to generate updated PDFs
3. Run `uv run python scripts/generate_mockups.py` to generate updated mockups
4. Commit both: `git add scripts/output/ mockups/`

### Issue: One PDF didn't generate a mockup

**Solution:** The script skips PDFs with rendering errors. Check:
1. Does the PDF file exist in `/scripts/output/`?
2. Is the PDF corrupted? Try opening it in a PDF reader
3. Check the error message from the script output
4. If needed, regenerate just that PDF: `uv run python scripts/generate_pdfs.py [product-name]`

### Issue: Device frame looks slightly different than expected

**Solution:** The frame is designed in Python/Pillow. Minor variations in gradient or shadow rendering are normal due to anti-aliasing. If the frame looks significantly wrong:
1. Check the colors in `generate_mockups.py` (constants at top of file)
2. Verify Pillow is up-to-date: `uv pip install --upgrade Pillow`
3. Regenerate: `uv run python scripts/generate_mockups.py`

---

## Maintenance & Updates

### When to Regenerate Mockups

- **PDF content changes** — Always regenerate (cover design, title, pricing, etc.)
- **Brand color updates** — Edit `generate_mockups.py` constants and regenerate
- **Device frame design changes** — Modify the frame code and regenerate
- **New product added** — Add markdown to `/products/`, generate PDF, generate mockup

### When NOT to Regenerate

- Changing Etsy listing copy (doesn't affect PDF/mockup)
- Changing product tags or metadata (no effect on mockup)
- Editing interior page content that doesn't appear on cover (optional to regenerate)

### Schedule

- **Before each launch phase** — Regenerate all mockups to ensure PDFs are latest
- **After any product update** — Regenerate affected product's mockup
- **Monthly review** — Check for any design tweaks or brand alignment issues

---

## References & Sources

### Etsy Best Practices Consulted

- [Etsy Digital Products Guide — SEO, Mockups, Printables](https://www.etsy.com/listing/4452814618/etsy-digital-products-guide-beginner-seo)
- [Designing High-Converting Digital Product Mockups — MyDesigns](https://mydesigns.io/blog/designing-high-converting-digital-product-mockups/)
- [How to Sell PDFs on Etsy: Digital Downloads Guide 2026 — Insight Agent](https://www.insightagent.app/guides/how-to-sell-pdfs-on-etsy)
- [How to Make Mockups for Etsy Digital Downloads in Canva — Firther Design Co.](https://www.firtherdesignco.com/blog/how-to-make-mockups-for-etsy-digital-downloads-in-canva)
- [How to Use Laptop Mockups to Sell Digital Products — Bashny](https://bashny.net/en/how-to-use-laptop-mockups-to-sell-digital-products-on-etsy-and-gumroad)
- [Etsy Product Photography Guide 2026 — ListyBox](https://listybox.com/blog/etsy-product-photography-guide-2026)
- [Digital Products to Sell on Etsy: 30 Profitable Ideas 2026 — MyDesigns](https://mydesigns.io/blog/digital-products-to-sell-on-etsy/)

### Key Findings

1. **Resolution matters** — Mockups must be ≥2000px on shortest side to enable Etsy's zoom viewer
2. **Device mockups convert better** — Realistic tablet/phone frames outperform plain screenshots
3. **Multiple angles help** — Using all 10 image slots with varied angles increases conversion by 20–40%
4. **Square format works best** — 1:1 aspect ratio performs better in Etsy's grid display
5. **Lifestyle shots drive connection** — Images showing the product "in use" trigger emotional engagement
6. **Mockup variations worth testing** — A/B testing different primary images can reveal which angle/crop performs best

---

## Summary

**Status:** ✅ All 21 products are ready for Etsy launch with professional tablet mockup images.

**Next Steps:**
1. Use the existing mockups for Phase 1 launch (6 products, Week 1–2)
2. Monitor conversion metrics on Etsy
3. In Phase 2 (Week 3–4), consider adding phone mockup variations and printed page mockups
4. If conversion rates plateau, invest in lifestyle photography and interior page mockups

**No blocker:** The lack of additional mockup angles is NOT a blocker for launch. The tablet mockups alone are professional, high-quality, and sufficient for market testing.
