---
title: "Zone Cards Verification Report — Track B Pre-Launch Checklist"
date: 2026-05-26
status: complete
format: checklist
---

# Zone Cards Verification Report
## Track B Launch Readiness — May 26, 2026

**Scope**: All 8 Zone Quick-Start Card PDFs in `projects/seedwarden/assets/zone-cards/`
**Launch target**: May 30, 2026
**Verification method**: File manifest check, content spot-check (Zones 3, 6, 9), cross-card consistency audit

---

## File Manifest

| Filename | Size | Status |
|----------|------|--------|
| seedwarden-zone-3-quickstart-card.pdf | 648 KB | Present |
| seedwarden-zone-4-quickstart-card.pdf | 649 KB | Present |
| seedwarden-zone-5-quickstart-card.pdf | 648 KB | Present |
| seedwarden-zone-6-quickstart-card.pdf | 648 KB | Present |
| seedwarden-zone-7-quickstart-card.pdf | 649 KB | Present |
| seedwarden-zone-8-quickstart-card.pdf | 648 KB | Present |
| seedwarden-zone-9-quickstart-card.pdf | 648 KB | Present |
| seedwarden-zone-10-quickstart-card.pdf | 648 KB | Present |

**Count**: 8/8 present. All files within the 1.5 MB per-file specification.

---

## Output Quality Checklist

### Branding and Formatting

- [x] Seedwarden logo and wordmark present in header on all 8 cards
- [x] Zone color band applied correctly: Zones 3–4 cool slate blue, Zones 5–6 forest green, Zones 7–8 warm amber, Zones 9–10 terracotta — verified against ZONE_QUICKSTART_CARD_SPEC.md Part 4
- [x] Zone number rendered as the largest typographic element on each card (36pt, terracotta accent)
- [x] Three-column layout (Frost Dates / Quick-Start Crops / Storage and Preservation) renders cleanly on all verified cards
- [x] Heirloom Variety Spotlight section present at bottom of each card, separated by full-width background band
- [x] Footer present on all 8 cards with zone-calendar and free-guides links
- [x] Font rendering consistent (Playfair Display zone name and number, Montserrat body text)
- [x] Background color: warm cream (#F5EDD6) — correct

### Content Completeness

- [x] Frost dates (last frost, first frost, season length) present and accurate on all verified cards
- [x] "This Month" task block present with 3 zone-specific tasks (calibrated to May 2026)
- [x] Quick-Start Crops section: 3 crops per card with variety type (H = heirloom, OP = open-pollinated) and days-to-maturity noted
- [x] Storage and Preservation Tips: 3 tips per card, matched to each zone's harvest window
- [x] Heirloom Variety Spotlight: 3 varieties per card with provenance notes and growing information
- [x] Region line correct for each zone (e.g., Zone 3: Northern Plains, Mountain Interior, Upper Great Lakes)

### Zone-Specific Content Accuracy (Spot-Check: Zones 3, 6, 9)

**Zone 3**: Last frost May 15–June 1, first frost September 5–20, season 95–125 days — correct. Stupice tomato (52–65 days), Provider bush bean (55 days) match spec. Short-season framing is consistent throughout.

**Zone 6**: Last frost April 5–April 25, first frost October 10–November 1, season 170–200 days — correct. Cherokee Purple tomato (72–80 days), Rattlesnake pole bean (65–70 days) — correct. Two-season preservation note is accurate.

**Zone 9**: Last frost February 10–March 5, first frost November 20–December 15, season 260–300 days — correct. Heat-set tomato varieties (Heat Wave II / Solar Fire) and cowpea selection appropriate for Gulf Coast / SoCal Inland climate. Two spring and fall processing windows noted accurately.

### Known Issues

| Issue | Cards Affected | Severity | Blocks Launch |
|-------|---------------|----------|---------------|
| Text-wrap artifact: "ferment hot sauce" wraps mid-phrase | Zone 6 | Cosmetic | No |
| Text-wrap artifact: "ripen" clips near column edge | Zone 9 | Cosmetic | No |
| Footer placeholder URLs (seedwarden.co/zone, seedwarden.co/zone-calendar) | All 8 | Pre-launch action item | No — update before May 30 |

**Note on footer URLs**: Placeholder domains are intentional per the generator spec. Update the `footer` section in `projects/seedwarden/scripts/generate_zone_cards.py` with live URLs and re-run before publishing. Sharing links for Google Drive uploads do not change after re-export.

---

## Cross-Card Consistency Summary

Ten elements verified as consistent across all 8 cards:

1. Brand logo placement (top-left header)
2. Seedwarden wordmark
3. "Zone Quick-Start Card" label in header
4. Section headers (Frost Dates, Quick-Start Crops, Storage and Preservation, Heirloom Variety Spotlight)
5. Zone band color (correct pair-assignment by temperature range)
6. Zone number size and accent color
7. Footer format and link structure
8. File size range (648–649 KB — no outliers, all well within 1.5 MB spec)
9. Single-page US Letter landscape layout
10. Variety type labels (H / OP) present on all spotlighted varieties

---

## Verification Sign-Off

**All 8 Zone Cards cleared for Track B May 30 launch.**

- Blocking defects: 0
- Non-blocking cosmetic issues: 2 (minor text-wrap in Zones 6 and 9)
- Pre-launch action required: Update footer URLs in the generator and re-export, or accept placeholder URLs for initial Gist distribution
- No re-verification required after URL update unless content changes are made

*Verified: May 26, 2026. Source spec: ZONE_QUICKSTART_CARD_SPEC.md.*
