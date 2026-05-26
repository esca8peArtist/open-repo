# Zone Quick-Start Cards — Production Notes
## Status: All 8 PDFs Complete (May 26, 2026)

---

## Deliverable Status

All 8 Zone Quick-Start Card PDFs are production-ready in this directory:

| File | Zone | Size |
|------|------|------|
| `seedwarden-zone-3-quickstart-card.pdf` | Zone 3 — Northern Plains, Mountain Interior, Upper Great Lakes | 633 KB |
| `seedwarden-zone-4-quickstart-card.pdf` | Zone 4 — Upper Midwest, Northern New England, Mountain Valleys | 633 KB |
| `seedwarden-zone-5-quickstart-card.pdf` | Zone 5 — Central Corridor, Southern New England, Mid-Elevation West | 633 KB |
| `seedwarden-zone-6-quickstart-card.pdf` | Zone 6 — Mid-Atlantic, Ohio Valley, Central Transition Zone | 632 KB |
| `seedwarden-zone-7-quickstart-card.pdf` | Zone 7 — Piedmont South, Oklahoma, North Texas, Maritime Northwest | 633 KB |
| `seedwarden-zone-8-quickstart-card.pdf` | Zone 8 — Deep South, Coastal Pacific Northwest, Central Texas | 632 KB |
| `seedwarden-zone-9-quickstart-card.pdf` | Zone 9 — Gulf Coast, Southern Texas, Central Florida, SoCal Inland | 633 KB |
| `seedwarden-zone-10-quickstart-card.pdf` | Zone 10 — South Florida, Coastal Southern California, Hawaii | 632 KB |

All files: valid PDF, under 1.5MB spec limit, US Letter landscape (11x8.5 in), Seedwarden brand palette.

---

## How These Were Built

Cards were generated using a Python script (`scripts/generate_zone_cards.py`) with fpdf2, using
the existing Montserrat font family already in the project. Content is drawn directly from
ZONE_QUICKSTART_CARD_SPEC.md Part 5 — every zone has its correct frost dates, region name,
This Month tasks (calibrated for May 2026), Quick-Start Crops, Storage tips, and Variety Spotlight.

**To regenerate or edit**: Open `scripts/generate_zone_cards.py`, update the `ZONES` dict for
the zone(s) you need to change, then run:

```
cd projects/seedwarden/scripts
uv run python3 generate_zone_cards.py
```

New PDFs overwrite the old ones in `assets/zone-cards/`.

---

## Canva Brand Kit — Palette Reference

If you build Canva versions of these cards (for editable team templates), use this exact palette.
The Canva Brand Kit setup procedure is in ZONE_CARD_PRODUCTION_TIMELINE.md Week 0.

**Status as of May 26**: Canva Brand Kit palette extension was not confirmed approved before
this build session. The PDFs were generated without Canva to meet the May 30 deadline.
Canva templates can be added post-launch as a supplement — they are not required for email delivery.

### Color Palette (10 colors to add to Canva Brand Kit)

| Name | Hex | Use |
|------|-----|-----|
| Forest Green — Primary | #2D5016 | Headers, borders, zone band (Zones 5-6) |
| Warm Cream — Background | #F5EDD6 | Page background, all 8 cards |
| Burnt Sienna — Accent | #A0522D | Zone number, icons, CTA, zone band (Zones 9-10) |
| Dark Charcoal — Body | #2C2C2C | All body text |
| Parchment — Spotlight Band | #EDE0C4 | Variety spotlight section background |
| Warm Grey — Footer | #7A7060 | Footer text only |
| Zone Band Cool — Zones 3-4 | #3D6B8A | Header band for Zone 3 and 4 cards |
| Zone Band Temperate — Zones 5-6 | #2D5016 | Header band for Zone 5 and 6 cards |
| Zone Band Warm — Zones 7-8 | #C9943A | Header band for Zone 7 and 8 cards |
| Zone Band Hot — Zones 9-10 | #A0522D | Header band for Zone 9 and 10 cards |

### Fonts

| Role | Font | Size | Style |
|------|------|------|-------|
| Wordmark "SEEDWARDEN" | Montserrat Bold | 9pt | All caps |
| Zone number | Montserrat Bold | 36pt | Bold |
| Zone name/region | Montserrat Regular | 7.5pt | Regular |
| Column headers | Montserrat Bold | 8pt | All caps |
| Body text | Montserrat Regular | 7.5pt | Regular |
| Footer | Montserrat Regular | 6.5pt | Regular |

Note: Playfair Display (the spec's preferred heading font) can be substituted in Canva
versions if desired. The Python generator uses Montserrat Bold throughout because Playfair
Display was not available offline. The visual result is equivalent at these sizes.

---

## May 30 Launch Checklist — Outstanding Steps

The PDFs are ready. The remaining steps to complete the email delivery system:

- [ ] Update footer placeholder URLs: edit `ZONES` dict in `generate_zone_cards.py`, replace
      `seedwarden.co/zone-calendar` with live Etsy listing URL and `seedwarden.co/zone` with live
      Kit landing page URL, then re-run the generator.
- [ ] Upload 8 PDFs to Kit: Content > Files. Copy the 8 download URLs to a notes file.
- [ ] Create zone-selection sign-up form in Kit with "Growing Zone" dropdown (Zones 3-10).
- [ ] Build 8 welcome email automations triggered by form + zone tag, each with the correct PDF link.
- [ ] Set up Kit landing page at seedwarden.com/zone (or Kit-generated URL for launch).
- [ ] Test: submit form for Zone 5 and Zone 3, confirm correct PDFs arrive by email.
- [ ] Add landing page URL to Etsy bio and PDF end-pages.

**Time estimate for these steps**: 2-3 hours (Kit setup is the main time cost).

---

## Monthly Refresh Protocol

The "This Month" block in Column 1 is time-sensitive. It is currently set to May 2026.
Update it at the start of each month:

1. Open `scripts/generate_zone_cards.py`
2. In the `ZONES` dict, find the `"this_month"` key for each zone
3. Update all 8 zones' task lists to reflect the new month's planting priorities
   (source: `products/zone-seed-starting-calendar.md`)
4. Update the "THIS MONTH — [MONTH] 2026" label in the `build_card` method (line referencing "MAY 2026")
5. Run `uv run python3 generate_zone_cards.py`
6. Re-upload all 8 PDFs to Kit (existing Google Drive sharing links update automatically)

This takes 20-30 minutes once per month.
