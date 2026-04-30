---
title: "Zone Quick-Start Card — Production Timeline"
date: 2026-04-30
status: production-ready
context: Phase 2, Track B — Zone card build plan
references: ZONE_QUICKSTART_CARD_SPEC.md, email-growth-playbook.md, email-list-building-playbook.md
---

# Zone Quick-Start Card — Production Timeline
## Week-by-Week Implementation Plan for 8-Zone PDF Build

**Purpose**: This document is the implementation schedule for building the 8 Zone Quick-Start Card PDFs in Canva. ZONE_QUICKSTART_CARD_SPEC.md is the content brief — it specifies every word, color, font, and layout element. This document tells you when to do what, in what order, and how long each step takes. When you complete week-by-week work as scheduled, the full 8-card set is ready for email delivery integration by the end of Week 4.

**Assumptions**:
- Canva Pro is available (required for Brand Kit and custom fonts). If not, Canva free tier works for layout and color; fonts must be substituted with free Canva equivalents.
- The user has approximately 2–3 hours per week available for Canva work.
- Email delivery is through Kit (ConvertKit) free tier.
- No designer is hired — this is a self-build using the spec and template approach documented here.

---

## Pre-Canva Content Verification Checklist

Complete this checklist before opening Canva for the first time. The Canva build is faster and produces fewer errors when all content decisions are locked before the design session begins. This checklist covers the content layer; the Canva layer (colors, fonts, icons) is covered in Week 0.

### Zone Content Readiness

Confirm the following source data is available and finalized for all 8 zones before Week 1. All data lives in ZONE_QUICKSTART_CARD_SPEC.md Part 5. This checklist is a verification step, not a research step — if any item is missing, resolve it in the spec first.

| Item | Source | Confirmed? |
|---|---|---|
| Last frost date range for each zone (3–10) | ZONE_QUICKSTART_CARD_SPEC.md Part 5 | [ ] |
| First frost date range for each zone | ZONE_QUICKSTART_CARD_SPEC.md Part 5 | [ ] |
| Growing season length (days) for each zone | ZONE_QUICKSTART_CARD_SPEC.md Part 5 | [ ] |
| 2–3 example cities per zone | ZONE_QUICKSTART_CARD_SPEC.md Part 5 | [ ] |
| "This Month" tasks (3 per zone, current month) | ZONE_QUICKSTART_CARD_SPEC.md Part 5 | [ ] |
| Quick-Start Crops (3 per zone, with one-line notes) | ZONE_QUICKSTART_CARD_SPEC.md Part 5 | [ ] |
| Storage and Preservation tips (2–3 per zone) | ZONE_QUICKSTART_CARD_SPEC.md Part 5 | [ ] |
| Heirloom Variety Spotlight (3 varieties per zone, one-line each) | ZONE_QUICKSTART_CARD_SPEC.md Part 5 | [ ] |
| Zone band colors confirmed against color table | ZONE_CARD_PRODUCTION_TIMELINE.md Week 0 | [ ] |

**This Month task currency**: The "This Month" block is the only time-sensitive element in the card. For a May 2026 launch, the tasks should reflect May planting priorities, not April. If the spec currently has April tasks, update them before building the cards — it is faster to update 8 spec entries than to re-export 8 PDFs after the fact.

### Footer Copy Lock

The card footer contains two links that must be finalized before export. Do not build cards with placeholder text that gets forgotten. Lock these now:

| Footer Element | Status | Confirmed Value |
|---|---|---|
| Etsy store URL for Zone Calendar product | [ ] Live / [ ] Placeholder | ___________________________ |
| Lead magnet landing page URL (seedwarden.com/zone or Kit URL) | [ ] Live / [ ] Placeholder | ___________________________ |

If either URL is not live at build time, use clearly marked placeholder text (e.g., `[ETSY-LINK-INSERT]`) in the card and do a find-and-replace update before final export. Do not leave placeholder text without a visual marker — it is the single most common cause of launching cards with broken links.

### Design System Decisions

Confirm these three decisions before starting the Canva build. Each is a choice that affects every card and cannot be changed without rebuilding:

**Decision 1: Portrait vs. landscape orientation**

The spec recommends portrait (8.5x11 vertical). If the landing page or email template has an image that requires landscape, resolve this now. **Default: portrait.**

**Decision 2: One PDF per zone vs. interactive multi-zone document**

The spec recommends individual zone PDFs (one per zone, 8 total). If Kit's delivery mechanism requires a different format, resolve this before building. **Default: 8 individual zone PDFs.**

**Decision 3: "This Month" update cadence**

Decide now whether the "This Month" block will be updated monthly or quarterly. Monthly updates keep the card seasonally useful but require a recurring 20-minute maintenance task. Quarterly updates require less maintenance but mean the card is 1–3 months out of date for some subscribers. **Default: monthly update, first business day of each month.**

---

## Week 0 — Pre-Work: Canva Brand Kit Setup (30-Minute User Action)

This is the only task in the timeline that requires direct user action before any card can be built. Every card, every template, and every future Seedwarden Canva design depends on getting this right once. It takes 30 minutes.

### Brand Kit Setup Checklist

Complete these steps in order inside Canva (Account > Brand Hub > Brand Kit).

**Step 1: Create the Brand Kit (5 minutes)**
- Log into Canva Pro
- Click the grid/waffle icon (top left) to open the home menu
- Click "Brand Hub" in the left sidebar
- Click "Create a Brand Kit"
- Name it: `Seedwarden`

**Step 2: Upload the Logo (5 minutes)**
- In the Brand Kit, find the "Logos" section
- Upload the primary Seedwarden logo (from `/projects/seedwarden/logos/`)
- Upload a white-background version if available, and a transparent-background PNG version
- Canva will use these in brand templates; having both variants prevents background conflicts

**Step 3: Add Colors (5 minutes)**
Add these six hex values exactly as listed. The names matter for team clarity.

| Name | Hex | Use |
|---|---|---|
| Forest Green — Primary | #2D5016 | Headers, borders, zone band (Zones 5–6) |
| Warm Cream — Background | #F5EDD6 | Page background on all 8 cards |
| Burnt Sienna — Accent | #A0522D | Icons, CTA buttons, zone number, zone band (Zones 9–10) |
| Dark Charcoal — Body | #2C2C2C | All body text |
| Parchment — Spotlight Band | #EDE0C4 | Variety spotlight section background |
| Warm Grey — Footer | #7A7060 | Footer text only |

Additionally, add these four zone-band colors:

| Name | Hex | Use |
|---|---|---|
| Zone Band Cool — Zones 3–4 | #3D6B8A | Horizontal rule in Zone 3 and 4 cards |
| Zone Band Temperate — Zones 5–6 | #2D5016 | Horizontal rule in Zone 5 and 6 cards |
| Zone Band Warm — Zones 7–8 | #C9943A | Horizontal rule in Zone 7 and 8 cards |
| Zone Band Hot — Zones 9–10 | #A0522D | Horizontal rule in Zone 9 and 10 cards |

Total: 10 colors in the Brand Kit. Do not add any other colors — extra colors lead to drift from the approved palette.

**Step 4: Set Fonts (5 minutes)**
Canva's free font library includes both required fonts.
- Primary: Playfair Display (find via Canva font search)
- Secondary: Montserrat (find via Canva font search)
- Add both to the Brand Kit under "Fonts"
- Designate Playfair Display as the "Heading" font, Montserrat as the "Body" font

**Step 5: Upload Icons (10 minutes)**
The card uses five line-style icons (see ZONE_QUICKSTART_CARD_SPEC.md Part 4). These can be sourced from Canva's built-in element library using the search terms listed in the spec. The faster path for brand consistency:
- Search "botanical calendar outline" in Canva Elements
- Select a line-style (not filled) icon that reads clearly at 24px
- Right-click the icon on a blank canvas, select "Add to Brand Kit" or drag to the icons section
- Repeat for: thermometer minimal outline, seed envelope outline, mason jar outline, seedling sprout outline
- All icons must be in one consistent visual family (same stroke weight, same line style)

**Step 6: Save and verify (5 minutes)**
- Create a new Canva design (US Letter, portrait)
- Open the Brand Kit panel (left sidebar > Brand)
- Confirm all 10 colors, 2 fonts, 5 icons, and the logo appear without error
- Delete this test design — it was just a verification step

Brand Kit setup is now complete. Every subsequent design step uses these assets.

---

## Week 1 — Master Template Build (Zones 5 and 6 First)

Build the master template using Zone 5 content. Zone 5 is the first build because it is the most common zone in Seedwarden's core market (Central Corridor, Southern New England, Mid-Elevation West) and represents the median growing season — all timing guidance is easiest to calibrate starting here.

### Session 1A: Layout Structure (90 minutes)

**Create the base design:**
- New Canva design: US Letter (8.5 x 11 inches), portrait orientation
- Resolution: 300 DPI (set at creation, not after — Canva sets this at new design time)
- Background color: Warm Cream #F5EDD6

**Build the header block (20 minutes):**
- Top section, full width: Seedwarden wordmark (Playfair Display, 16pt, small caps, Forest Green) on the left
- Right side of header: "Zone Quick-Start Card" label (Montserrat Light, 12pt, Warm Grey)
- Below the header text: full-width horizontal rule, 12px height, Zone Band Temperate #2D5016 (this is the zone color band that changes per zone)
- Zone number: Playfair Display Bold, 72pt, Burnt Sienna #A0522D, positioned prominent in the header area
- Zone name / region: Playfair Display Italic, 18pt, Forest Green, below the zone number

**Build the three-column body (40 minutes):**
- Column widths: 35% / 35% / 30% (left to right)
- Column 1 header: "Frost Dates and Season" — Montserrat All Caps, 11pt, tracked +50, Forest Green, with calendar icon above
- Column 2 header: "Quick-Start Crops" — same styling, with seed envelope icon
- Column 3 header: "Storage and Preservation" — same styling, with mason jar icon
- Body text blocks: Montserrat Light 10pt, Dark Charcoal #2C2C2C, line height 1.4
- No borders between columns — use whitespace (16px minimum between column text edges)

**Build the Variety Spotlight section (20 minutes):**
- Full-width band below the three columns
- Background: Parchment #EDE0C4
- Header: "Heirloom Variety Spotlight" — Montserrat All Caps, 11pt, tracked +50, Forest Green, with seedling icon
- Three rows of variety content — Montserrat Light 10pt for variety names (italic for species names), Dark Charcoal

**Build the footer (10 minutes):**
- Single line, Montserrat Light 8pt, Warm Grey #7A7060
- Left: "Get the full Zone [X] Calendar — [Etsy link placeholder]"
- Right: "Free guide: seedwarden.com/zone"
- These are placeholder links for now — update with live URLs before publishing

### Session 1B: Zone 5 Content Population (60 minutes)

With the layout structure built, populate Zone 5 content from ZONE_QUICKSTART_CARD_SPEC.md Part 5.

**Populate Zone 5:**
- Zone number: 5
- Region line: "Central Corridor, Southern New England, Mid-Elevation West"
- Zone band color: Temperate #2D5016 (already the default — no change needed)
- Last frost: April 15 – May 10
- First frost: October 1 – October 20
- Growing season: 150–180 days
- Example cities: Denver CO, Des Moines IA, Boston MA suburbs
- This Month tasks (April 2026): three tasks from spec
- Quick-Start Crops: Dragon Tongue bean, Mortgage Lifter tomato, Lemon cucumber
- Storage tips: two-window preservation seasons; tomato sauce as anchor; hot sauce fermentation
- Variety spotlight: Mortgage Lifter, Dragon Tongue, Chioggia beet

**Review and visual check (15 minutes):**
- Print to PDF (Canva export: Download > PDF Print)
- Open the PDF and view at 100% zoom
- Check: zone number is the largest element, column headers are clearly legible, body text at 10pt is readable without zooming, footer is present
- Note any layout adjustments needed before duplicating to other zones

**Save the Zone 5 file as the master template:**
- In Canva, right-click the design > "Use as template" or simply keep this file as the base
- Name it: `Seedwarden Zone [5] Quick-Start Card — MASTER`

**Duplicate and build Zone 6 (30 minutes):**
- Duplicate the Zone 5 master
- Name the duplicate: `Seedwarden Zone [6] Quick-Start Card`
- Change: zone number (5 → 6), region line, frost dates, example cities, This Month tasks, crops, storage tips, variety spotlight — all from Part 5 of the spec
- Zone band color: same #2D5016 (Zones 5–6 share the Temperate color)
- Export Zone 6 PDF for review

**Week 1 output**: Zone 5 master template complete, Zone 6 card complete. Two PDFs ready for preview review.

---

## Week 2 — Cool Zone Cards (Zones 3 and 4) + Warm Zone Cards (Zones 7 and 8)

With the master template in hand, each subsequent zone card takes 30–45 minutes to produce. Four zones can be completed in two 90-minute sessions.

### Session 2A: Zone 3 and Zone 4 (90 minutes)

**Zone 3 build (45 minutes):**
- Duplicate the Zone 5 master
- Update: zone number to 3, region line to "Northern Plains, Mountain Interior, Upper Great Lakes"
- Update zone band color: change from #2D5016 to Cool Slate Blue #3D6B8A (Zones 3–4 use the cool color)
- Update frost dates, example cities, This Month tasks, Quick-Start crops, storage tips, variety spotlight — all from spec
- Export PDF: `zone-3-quick-start-card.pdf`

**Zone 4 build (45 minutes):**
- Duplicate Zone 3 (already has the #3D6B8A zone band set)
- Update all content to Zone 4 values from spec
- Zone band color: same #3D6B8A (no change needed — Zone 4 is also Cool)
- Export PDF: `zone-4-quick-start-card.pdf`

### Session 2B: Zone 7 and Zone 8 (90 minutes)

**Zone 7 build (45 minutes):**
- Duplicate the Zone 5 master
- Update: zone number to 7, region line to "Upper South, Pacific Northwest Interior, Transition Zone"
- Update zone band color to Warm Amber #C9943A
- Update all content from spec
- Add subzone note in frost dates block: "Zone 7a last frost April 5–15; Zone 7b last frost March 20–April 5. Check planthardiness.ars.usda.gov for your exact location."
- Export PDF: `zone-7-quick-start-card.pdf`

**Zone 8 build (45 minutes):**
- Duplicate Zone 7 (already has the #C9943A zone band)
- Update all content to Zone 8 values
- Zone band color: same #C9943A (no change needed)
- Export PDF: `zone-8-quick-start-card.pdf`

**Week 2 output**: Zones 3, 4, 7, 8 complete. Six of eight cards finished. Two remain (Zones 9 and 10).

---

## Week 3 — Hot Zone Cards (Zones 9 and 10) + Full Set Review

### Session 3A: Zone 9 and Zone 10 (90 minutes)

**Zone 9 build (45 minutes):**
- Duplicate Zone 5 master
- Update: zone number to 9, region line to "Lower South, Desert Southwest, Central Coast California"
- Update zone band color to Terracotta #A0522D
- Update all content from spec (the Zone 9 content has the most distinct growing pattern — two growing seasons, summer dormancy notes — verify against spec carefully)
- Export PDF: `zone-9-quick-start-card.pdf`

**Zone 10 build (45 minutes):**
- Duplicate Zone 9 (already has the #A0522D zone band)
- Update all content to Zone 10 values
- Zone band color: same #A0522D (no change needed)
- Export PDF: `zone-10-quick-start-card.pdf`

### Session 3B: Full Set Review and Print Test (60 minutes)

This is the quality check before email integration. Do not skip this step — errors found here are easier to fix than errors discovered after email delivery is live.

**Review checklist for all 8 PDFs:**

For each card, open the PDF and confirm:

| Check | Pass Criteria |
|---|---|
| Zone number is the dominant element | Zone number visible from 2 feet away when printed |
| Zone band color is correct | Matches the spec color table (cool/temperate/warm/hot) |
| Frost dates are accurate | Match the ZONE_QUICKSTART_CARD_SPEC.md Part 5 tables exactly |
| This Month tasks are present | Three tasks visible in Column 1 |
| Quick-Start Crops are present | Three crops with one-line notes in Column 2 |
| Storage tips are present | Two to three tips in Column 3 |
| Variety spotlight: three varieties | All three have one-line descriptions |
| Footer links are placeholder | Do NOT have live URLs yet — confirms these are not accidentally published before Etsy/landing page is live |
| File size under 1.5 MB | Canva PDF Print exports typically come in at 800 KB–1.2 MB for single-page designs |
| Font rendering correct | No font substitution errors (Playfair Display and Montserrat should render correctly in Canva export) |

**Print test (optional but recommended):**
Print Zone 5 and Zone 3 cards at home at actual 8.5 x 11 size. Check:
- Zone number legible
- Body text at 10pt readable without reading glasses
- Colors accurate on standard home printer paper (they will be slightly duller than screen — this is expected)
- No text clipping at the page edges (if text is too close to margins, add 0.25-inch margins)

**Week 3 output**: All 8 PDFs complete and reviewed. Full card set ready for delivery integration.

---

## Week 4 — Email Delivery Integration and Landing Page Setup

### Session 4A: Kit (ConvertKit) Delivery Setup (60 minutes)

The Kit free tier supports conditional content delivery using tags — this is the mechanism for delivering zone-specific cards without a paid automation plan.

**Step 1: Upload all 8 PDFs to Kit (15 minutes)**
- In Kit: Content > Files
- Upload each PDF: `zone-3-quick-start-card.pdf` through `zone-10-quick-start-card.pdf`
- After upload, Kit generates a unique download URL for each file
- Copy all 8 URLs into a local notes file — you will use them in the email templates

**Step 2: Create zone-selection sign-up form (20 minutes)**
- In Kit: Forms > New Form
- Form type: inline or landing page (whichever matches the delivery mechanism)
- Add a custom field: "Growing Zone" — dropdown with values: 3, 4, 5, 6, 7, 8, 9, 10
- The subscriber selects their zone at sign-up; Kit stores this as a tag or custom field value
- This is the data that drives conditional delivery — without this field, you cannot send zone-specific cards

**Step 3: Create 8 welcome email sequences (25 minutes)**
One email per zone, each containing the matching download link. These are simple one-email automations triggered by form submission + zone tag.

**Email template (fill in [X] for each zone):**

Subject line: "Your Zone [X] Quick-Start Card is ready"

Body:
```
Hi [First Name],

Your Zone [X] Quick-Start Card is attached — one page with everything 
you need to get started this season.

[Download Your Zone [X] Card]

Inside the card:
- Your exact frost date range
- The three crops to plant this month in Zone [X]
- Storage tips matched to your harvest window
- Three heirloom variety picks for your zone

If you want the full month-by-month planting schedule for Zone [X], 
the Zone-by-Zone Seed Starting Calendar covers every week of the 
growing season for your zone: [Etsy link]

Happy growing,
Seedwarden
```

Create eight versions of this email — one per zone — each with the correct download link. In Kit, set each email to trigger when a subscriber submits the sign-up form AND their zone field = [X].

### Session 4B: Landing Page Setup (45 minutes)

**Option A: Kit landing page (fastest, free)**
- In Kit: Landing Pages > New Landing Page
- Use a minimal layout template
- Headline: "Get Your Free Zone Quick-Start Card"
- Subheadline: "One page. Your zone. What to plant right now."
- Form: embed the zone-selection form built in Step 2
- Below the form, three lines: "Enter your growing zone, get your personalized card instantly. No spam. Unsubscribe any time."
- No images required for launch — the copy carries the landing page at Phase 2 scale

**Option B: Carrd.co single-page site ($19/year)**
- Slightly more design control than Kit landing pages
- Worth the cost if the landing page will also serve as a marketing touchpoint for Pinterest pins
- Embeds the Kit form directly via HTML snippet

**Landing page URL**: Map the page to `seedwarden.com/zone` (or whatever the Seedwarden domain resolves to). If no custom domain is set up yet, use the Kit-generated URL for initial launch and update when the domain is configured.

**Publish and test (15 minutes):**
- Submit a test form entry for Zone 5
- Confirm the welcome email arrives with the correct Zone 5 PDF download link
- Download the PDF from the link — confirm it opens correctly
- Check the "from" email address in the welcome email — should be a Seedwarden-branded sender, not a Kit default address
- If using a custom domain email (hello@seedwarden.com), verify it is authenticated in Kit settings before sending

**Week 4 output**: All 8 cards in Kit file library, zone-selection form live, 8 welcome email sequences active, landing page published, test submission successful.

---

## Launch Readiness Checklist

Before promoting the Zone Quick-Start Card via any channel, confirm all items below.

### Content Checks

- [ ] All 8 zone PDFs exported and stored in `/projects/seedwarden/assets/zone-cards/`
- [ ] All 8 zone PDFs uploaded to Kit and download URLs logged
- [ ] Frost dates in each card verified against USDA zone data (planthardiness.ars.usda.gov)
- [ ] "This Month" tasks are current for the actual current month (update each month — this is the only recurring maintenance task)
- [ ] No placeholder text remaining (no "[LINK]" or "[ZONE NAME]" unfilled)
- [ ] Etsy product links in footer are live and pointing to actual listings

### Technical Checks

- [ ] Zone-selection sign-up form is live and accepting submissions
- [ ] All 8 welcome email automations are active in Kit
- [ ] Test submission completed for at least Zone 5 and Zone 3 (temperate + cool)
- [ ] Download links in emails open correct PDFs
- [ ] Landing page URL resolves correctly (no 404)
- [ ] Landing page mobile display checked (open on phone and confirm form is functional)
- [ ] Kit sender email is authenticated (SPF/DKIM) — prevents welcome emails going to spam

### Integration Checks

- [ ] Landing page URL is added to the Seedwarden Etsy shop announcement or bio
- [ ] PDF end-pages for the top 5 Etsy products include the landing page URL as a CTA
- [ ] Pinterest and/or Instagram bio updated with landing page link
- [ ] WORKLOG.md entry written logging: all 8 card file paths, Kit URL, landing page URL, launch date

---

## Monthly Maintenance: Updating "This Month" Tasks

The Zone Quick-Start Card has one time-sensitive element: the "This Month" task block in Column 1. This block names April-specific tasks for April 2026. When May arrives, this block should be updated to May tasks for all 8 zones.

**Monthly update workflow (20 minutes, done once per month):**

1. Open the Canva master template for each zone
2. Update the "This Month" header to the current month name
3. Replace the three task bullets with the appropriate tasks from the Zone-by-Zone Seed Starting Calendar product (already authored and ready — this is your own product)
4. Export new PDF
5. In Kit: upload the new PDF, replace the old download URL in the welcome email automation
6. Log the update in WORKLOG.md

This monthly update is what differentiates the Zone Quick-Start Card from a static lead magnet. Subscribers who download in April get an April card. Subscribers who download in June get a June card. The seasonal freshness is the mechanism that keeps the card genuinely useful rather than archival.

**Monthly update should occur:** First business day of each month. Set a recurring calendar reminder.

---

## Timeline Summary

| Week | Sessions | Work | Output |
|---|---|---|---|
| Week 0 | 1 session × 30 min | Canva Brand Kit setup | Brand Kit live; 10 colors, 2 fonts, 5 icons, logo |
| Week 1 | 2 sessions × 90 min + 60 min | Master template + Zones 5 and 6 | Master template; Zones 5, 6 PDFs |
| Week 2 | 2 sessions × 90 min | Zones 3, 4, 7, 8 | Four zone PDFs |
| Week 3 | 1 session × 90 min + 60 min | Zones 9, 10 + full review | All 8 PDFs complete and verified |
| Week 4 | 2 sessions × 45–60 min | Kit delivery + landing page | Live lead magnet funnel |
| **Total** | | **~10 hours across 4 weeks** | **Full lead magnet system live** |

This is 4 weeks of light part-time work (2.5 hours per week average). If the user can dedicate a full Saturday to Week 1 and Week 2 together (4 hours), the full card set can be ready for email delivery in two weeks instead of four.
