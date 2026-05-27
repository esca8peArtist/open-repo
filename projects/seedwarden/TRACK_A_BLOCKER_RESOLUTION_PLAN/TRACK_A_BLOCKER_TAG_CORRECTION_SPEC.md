---
title: "Track A Blocker 1 — Tag Correction Specification"
created: 2026-05-27
status: production-ready — user action required
effort: 15 minutes
references:
  - TRACK_A_BLOCKER_RESOLUTION.md (original correction table, Sessions 700s)
  - TRACK_A_RESOLUTION_PROTOCOL.md (execution context, May 15)
  - ETSY_PHASE_1_UPLOAD_CHECKLIST.md (upload readiness)
---

# Track A Blocker 1: Tag Correction Specification

**Blocker type**: User action — manual edits in Etsy listing draft interface  
**Effort**: 15 minutes total (three listings, copy-paste corrections)  
**External wait**: None — corrections take effect immediately on save  
**Rollback**: Trivially reversible — any tag can be re-entered at any time  
**Status as of May 27**: Unresolved — all three corrections still pending

---

## 1. Why This Is Blocking

Etsy enforces a hard limit of 20 characters per tag. Tags submitted above this limit are silently truncated — Etsy does not warn you, the listing appears to accept them, but the truncated keyword is what actually indexes in search. The practical effect is that the listing ranks for a shorter, often unrelated keyword fragment rather than the intended phrase. This wasted keyword authority cannot be recovered by editing after launch without resetting the listing's search ranking clock.

Three listings in Phase 1 (Track A) have tags that either violate the 20-character limit or are borderline and historically inconsistently accepted by Etsy's system. Uploading these listings in their current state would permanently compromise their Day 1 search ranking potential.

No other listings among the 21 Phase 1 products require tag corrections. The three below are the complete set.

---

## 2. Etsy Tag Format Specification (2026)

These rules are confirmed current as of May 2026:

| Rule | Specification |
|------|---------------|
| Maximum tags per listing | 13 |
| Maximum characters per tag | 20 (including spaces) |
| Allowed characters | Letters, numbers, spaces, hyphens (-), apostrophes (') |
| Not allowed | Special characters, symbols, commas, leading hyphens or apostrophes |
| Case sensitivity | None — title case has no SEO effect |
| Duplicates across listings | Permitted and often appropriate for related products |
| Tags vs. title | Tags and title are both indexed; overlap is acceptable |
| API access for bulk edits | Not available to third-party tools — corrections must be applied in the Etsy UI |

**Character counting note**: Spaces count toward the 20-character limit. "companion planting" = 18 characters (c-o-m-p-a-n-i-o-n = 9, space = 1, p-l-a-n-t-i-n-g = 8). Count manually or use any text character counter before saving if uncertain.

---

## 3. Affected Guides — Correction Table

| Listing Name | File Reference | Correction Type | Time |
|---|---|---|---|
| Companion Planting Chart | Phase 1 listing draft | Full tag set replacement (13 tags) | 5 min |
| Survival Garden Regional Plans | Phase 1 listing draft | Single tag swap | 2 min |
| Zone-by-Zone Seed Starting Calendar | Phase 1 listing draft | Single tag swap | 2 min |

---

## 4. Correction 1: Companion Planting Chart

**Issue**: The existing tag set for this listing has tags that are outdated, contain character-count violations, or do not match current Etsy keyword search volume patterns. The full set needs to be replaced.

**Current tags**: Existing set in Etsy draft (do not use — replace entirely)

**Target tags — copy this set exactly (13 tags, all within 20 characters):**

```
companion planting
garden planning
vegetable garden
organic gardening
plant combinations
pest control
garden chart
raised bed garden
square foot garden
permaculture
homestead garden
garden printable
digital download
```

**Character verification** (all within 20-character limit):

| Tag | Character Count | Status |
|-----|----------------|--------|
| companion planting | 18 | OK |
| garden planning | 15 | OK |
| vegetable garden | 16 | OK |
| organic gardening | 17 | OK |
| plant combinations | 18 | OK |
| pest control | 12 | OK |
| garden chart | 12 | OK |
| raised bed garden | 17 | OK |
| square foot garden | 18 | OK |
| permaculture | 12 | OK |
| homestead garden | 16 | OK |
| garden printable | 16 | OK |
| digital download | 16 | OK |

**How to apply:**

1. Log into Etsy at etsy.com
2. Click your profile icon (top right) > "Sell on Etsy" > "Shop Manager"
3. Click "Listings" in the left sidebar
4. Find "Companion Planting Chart" (status: Draft)
5. Click the listing title or the pencil/edit icon
6. Scroll to the "Tags" field
7. Select all existing tags and delete them (click the X next to each tag, or clear the field)
8. Type or paste each tag from the list above, pressing Enter after each one
9. Confirm 13 tags are present in the field
10. Click "Save and continue" or "Publish" (keep as Draft — do not publish yet)

---

## 5. Correction 2: Survival Garden Regional Plans

**Issue**: The tag `self sufficient garden` contains 21 characters (s-e-l-f = 4, space = 1, s-u-f-f-i-c-i-e-n-t = 10, space = 1, g-a-r-d-e-n = 6 = 22 characters — actually 22, above the 20-character limit). Etsy will truncate this silently to a shorter fragment.

**Specific change:**

| Action | Tag |
|--------|-----|
| Remove | `self sufficient garden` |
| Add | `self-sufficient` |

**All other tags for this listing remain unchanged.**

**Character verification:**

| Tag | Character Count | Status |
|-----|----------------|--------|
| self sufficient garden | 22 | REMOVE — over limit |
| self-sufficient | 15 | OK — use this instead |

**How to apply:**

1. In Etsy Shop Manager > Listings, find "Survival Garden Regional Plans" (Draft)
2. Click to edit the listing
3. Scroll to the "Tags" field
4. Locate the tag `self sufficient garden` — click the X to remove it
5. In the tag input field, type `self-sufficient` and press Enter
6. Confirm the tag now reads `self-sufficient` (not the old version)
7. Confirm all other tags are still present and unchanged
8. Click "Save and continue" (keep as Draft)

---

## 6. Correction 3: Zone-by-Zone Seed Starting Calendar

**Issue**: The tag `veggie planting guide` is exactly 20 characters (v-e-g-g-i-e = 6, space = 1, p-l-a-n-t-i-n-g = 8, space = 1, g-u-i-d-e = 5 = 21 characters — actually 21, over the limit). Additionally, keyword research shows `veggie plant guide` (18 characters) has stronger search volume on Etsy's platform for this product category.

**Specific change:**

| Action | Tag |
|--------|-----|
| Remove | `veggie planting guide` |
| Add | `veggie plant guide` |

**All other tags for this listing remain unchanged.**

**Character verification:**

| Tag | Character Count | Status |
|-----|----------------|--------|
| veggie planting guide | 21 | REMOVE — over limit |
| veggie plant guide | 18 | OK — use this instead |

**How to apply:**

1. In Etsy Shop Manager > Listings, find "Zone-by-Zone Seed Starting Calendar" (Draft)
2. Click to edit the listing
3. Scroll to the "Tags" field
4. Locate the tag `veggie planting guide` — click the X to remove it
5. In the tag input field, type `veggie plant guide` and press Enter
6. Confirm the tag now reads `veggie plant guide`
7. Confirm all other tags are still present and unchanged
8. Click "Save and continue" (keep as Draft)

---

## 7. How to Apply Tag Corrections — Method Options

**Method A: Direct Etsy UI (required — only method available)**

Etsy does not expose a public API endpoint for bulk tag modification by third-party scripts. The listing data exists in Etsy's internal systems; the tag field in the Etsy listing editor is the only interface for making these changes. All three corrections must be done manually in the Etsy web interface.

There are no local project files to edit as a pre-upload step — the tags in `TRACK_A_BLOCKER_RESOLUTION.md` and this document are the source-of-truth specification, but they must be transcribed into Etsy's listing editor directly.

**Method B: Batch upload via CSV (not recommended for corrections only)**

Etsy supports bulk listing upload via CSV for new listings, but editing existing Draft listings via CSV requires downloading the existing listing data, modifying the CSV, and re-uploading — a process that is more complex than three manual edits and risks overwriting other listing fields. Use Method A.

---

## 8. Success Criteria

After completing all three corrections, verify the following before considering this blocker resolved:

- [ ] **Companion Planting Chart**: Exactly 13 tags present in the Etsy tag field. No tag exceeds 20 characters. Spot-check: "companion planting" (18), "square foot garden" (18), "digital download" (16) — all visible.
- [ ] **Survival Garden Regional Plans**: `self-sufficient` present in tag list. `self sufficient garden` absent. All other tags for this listing are unchanged.
- [ ] **Zone-by-Zone Seed Starting Calendar**: `veggie plant guide` present in tag list. `veggie planting guide` absent. All other tags for this listing are unchanged.
- [ ] **No other listings were modified** — only three listings touched during this session.
- [ ] **Log in WORKLOG.md**: "Track A Blocker 1 — tag corrections applied [date]"

**Verification method in Etsy UI**: After saving each listing, click back into the listing editor and visually confirm the tags field shows the expected set. There is no bulk tag report in Etsy — visual confirmation listing by listing is the only verification method.

---

## 9. Effort Estimate

| Step | Time |
|------|------|
| Log into Etsy Shop Manager and navigate to Listings | 2 min |
| Companion Planting Chart: delete old tags, enter 13 new ones | 5 min |
| Survival Garden Regional Plans: single tag swap | 2 min |
| Zone-by-Zone Seed Starting Calendar: single tag swap | 2 min |
| Visual verification of all three listings | 3 min |
| Log completion in WORKLOG.md | 1 min |
| **Total** | **15 min** |

No document preparation is needed — the exact tag text is in this file, ready to copy.

---

## 10. Rollback Plan

Etsy tag changes are immediately reversible. If a tag is applied incorrectly:

1. Navigate to the affected listing draft in Etsy Shop Manager > Listings
2. Click to edit the listing
3. In the Tags field, click the X next to the incorrect tag to remove it
4. Type the correct tag and press Enter
5. Save

There is no confirmation step, no cooldown, and no SEO penalty for correcting tags on a Draft listing (the listing is not yet live, so no ranking history exists to disrupt). Even on a live listing, tag corrections take effect within the next Etsy indexing cycle (typically 24–72 hours) with no permanent penalty.

**Worst-case rollback scenario**: If all tags on a listing were accidentally deleted, re-enter the correct tag set from this document. The listing draft will not be published until you explicitly click "Publish" — so there is no risk of a tag-less listing going live during the correction session.

---

## 11. Scope Confirmation — What Is NOT Affected

These 18 listings do not require any tag changes and are upload-ready as-is:

Food Sovereignty Starter Guide, Seed Saving Field Manual, Anti-Catalog (30 Heirlooms), Seed Swap Hosting Kit, Apartment Plant Catalog, Heirloom Seed Bank Builder, Wild Edibles Quick Reference, Native Plants Regional Guide, Forager's Seasonal Harvest Calendar, Plant ID Photo Guide, Hunting/Fishing/Trapping Field Manual, Meat and Fish Preservation Field Manual, Water Sourcing and Purification Guide, Off-Grid Cooking Field Manual, Herbal First Aid Field Guide, Home Apothecary Starter Kit, Medicinal Herb Grow Guide, Zone Quick-Start Card Set.

Do not modify the tags on any of these listings during the tag correction session.

---

*Sources consulted: Etsy Help Center tag documentation; ListingForge 2026 Etsy tag character limit guide (listing-forge.com/blog/etsy-character-limits); Listybox 2026 Etsy tags optimization guide (listybox.com/blog/etsy-tags-optimization-guide); TRACK_A_BLOCKER_RESOLUTION.md and TRACK_A_RESOLUTION_PROTOCOL.md (Sessions 700s–1344, May 2026).*
