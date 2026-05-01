---
title: "Phase 2 Orchestrator Tasks — Non-User-Action Items"
prepared: 2026-05-01
status: active — tasks available for parallel execution
references:
  - TRACK_B_PRODUCTION_PIPELINE.md
  - CANVA_ZONE_CARD_BATCH_WORKFLOW.md
  - CANVA_ZONE_CARD_DESIGN_GUIDE.md
  - PHASE_2_EMAIL_STRATEGY.md
  - MAY_CONTENT_EXECUTION_PLAN.md
  - TRACK_B_READINESS_CHECKLIST.md
  - phase-2-production-checklist.json
---

# Phase 2 Orchestrator Tasks — Non-User-Action Items

**Purpose**: This document identifies every Phase 2 task the orchestrator can execute in
parallel with the user's May 1-11 physical actions (social account creation, filming, props
sourcing, and photo shoot). Nothing in this document requires the user to have completed any
preceding step — each task is either independently executable today or depends only on other
orchestrator tasks.

**Scope boundary**: This document does not cover user-action tasks (filming, physical sourcing,
the May 10-11 shoot, social account creation, Canva Brand Kit setup). Those are in
`TRACK_B_PRODUCTION_PIPELINE.md` Section 3.

---

## Critical Path Context

The May 30 launch depends on this sequence:

```
[User: May 1-9 props + accounts + filming]
         |
[User: May 10-11 photo shoot]
         |
[May 12-14: Image culling + editing]  <-- orchestrator can pre-stage all tooling
         |
[May 15-17: Cluster D/E compositing + zone cards 9 and 10]  <-- orchestrator can execute
         |
[May 17-22: Kit email automation build]  <-- orchestrator can execute
         |
[May 22-30: Scheduling + launch coordination]
```

The orchestrator can work on two independent tracks simultaneously:

**Track 1 (image pipeline)**: Prepare compositing workflow for Cluster D/E before the shoot
completes. Set up the output directory structure and naming spec so files drop straight into
the right places when editing begins May 12.

**Track 2 (email and zone cards)**: Zone card content is fully written and ready to paste into
Canva. Email copy is production-ready. Neither depends on photos or social accounts.

---

## Section 1: Tasks Available for Immediate Execution (May 1-9)

These tasks have no pending dependencies. They can be executed in any order, in parallel.

---

### Task 1.1 — Verify Image Output Directory Structure

**What**: Confirm the `marketing/lifestyle-photos/etsy-ready/` and
`marketing/lifestyle-photos/pins/` directories exist and are empty (ready to receive exports).
If subdirectories are needed for cluster organization, create them.

**Why now**: If the directories or naming structure are wrong when image editing begins May 12,
the editor wastes time reorganizing. Confirming them now costs nothing.

**Output**: Verified directory tree at:
```
marketing/lifestyle-photos/
  etsy-ready/       (receives 30 final 2400x2400 JPEG files)
  pins/             (receives 60 social variant crops — 1:1, 4:5, 16:9)
```

**Naming convention to confirm**:
- Etsy-ready: `[product-slug]-slot4.jpg` and `[product-slug]-slot5.jpg`
- Instagram crop: `[product-slug]-ig.jpg`
- Pinterest crop: `[product-slug]-pin.jpg`

**Status at session start**: Both directories exist and are empty. No action needed unless
cluster-level subdirectories are preferred for the editing workflow. Recommendation: keep
flat (no subdirectories) — all 30 files land in `etsy-ready/` and the naming convention
makes cluster membership self-evident from the slug.

**Conclusion**: Directory structure is confirmed ready. No file system changes needed.

---

### Task 1.2 — Verify Cluster D/E Stock File Completeness

**What**: Confirm all 10 staged Cluster D and E stock image files are present and correctly
named in `assets/stock-raw/`.

**Status at session start**: Verified present.

| Product | Slot 4 file | Slot 5 file | Location |
|---------|------------|------------|---------|
| survival-garden-regional-plans | `survival-garden-regional-plans-slot4.jpg` | `survival-garden-regional-plans-slot5.jpg` | `assets/stock-raw/survival-garden-regional-plans/` |
| hunting-fishing-trapping-field-manual | `hunting-fishing-trapping-field-manual-slot4.jpg` | `hunting-fishing-trapping-field-manual-slot5.jpg` | `assets/stock-raw/hunting-fishing-trapping-field-manual/` |
| small-scale-livestock-field-manual | `small-scale-livestock-field-manual-slot4.jpg` | `small-scale-livestock-field-manual-slot5.jpg` | `assets/stock-raw/small-scale-livestock-field-manual/` |
| meat-fish-preservation-field-manual | `meat-fish-preservation-field-manual-slot4.jpg` | `meat-fish-preservation-field-manual-slot5.jpg` | `assets/stock-raw/meat-fish-preservation-field-manual/` |
| native-plants-regional-guide | `native-plants-regional-guide-slot4.jpg` | `native-plants-regional-guide-slot5.jpg` | `assets/stock-raw/native-plants-regional-guide/` |

All 10 files confirmed present. Candidate alternates are also staged for 4 of the 5 products.

**Attribution note for native-plants-regional-guide-slot4.jpg**: When uploading this image
to the Native Plants listing on Etsy, add the following line to the listing description footer:
"Background photo (listing image 4): Joe Mabel, CC BY-SA 3.0, via Wikimedia Commons."
This is an Etsy upload-time action, not an orchestrator action, but it must be logged here
so it is not missed.

---

### Task 1.3 — Produce 21-Product Compositing Instruction Sheet

**What**: Create a per-product instruction table that the user (or orchestrator) can follow
during the May 15 Canva compositing session for Cluster D/E. Each row specifies: which stock
image to use, which product PDF overlay to apply, what export settings to use, and where to
save the output.

**Why now**: The compositing session (May 15) is one day after the photo shoot ends. If the
instruction sheet is not ready, the session stalls on lookups. Having it ready in advance
means the compositing session is pure execution — open Canva, follow the table, export.

**Source documents**: `TRACK_B_PRODUCTION_PIPELINE.md` Section 2 (cluster assignments),
`phase-2-production-checklist.json` W4-05 (compositing technique), `CANVA_EXECUTION_PLAYBOOK.md`.

**Output target**: The instruction table lives in `TRACK_B_PRODUCTION_PIPELINE.md` Section 4
as the upload priority table. This task confirms those instructions are complete and adds
per-product notes for the compositing step if not already present.

**Action**: Review Section 2 and Section 4 of `TRACK_B_PRODUCTION_PIPELINE.md` at compositing
time and confirm stock file → Canva composite → export path for each of the 5 Cluster D/E
products. Log each completed composite filename in `WORKLOG.md` using the existing image
sourcing table format.

---

### Task 1.4 — Audit Tags for Phase 2 Backlog Products 10-19

**What**: For the 15 backlog products not covered in `UPLOAD_SEQUENCE.md`'s corrected tag
section, verify every tag in `etsy-store-copy.md` is 20 characters or fewer. Produce a
corrections table if violations are found.

**Why now**: Products 10-19 upload in Week 2 (May 2026 or later, depending on Phase 1 launch
date). Having the tags verified before Week 2 means no upload is delayed by a compliance check.

**Products to audit**:
- 12-Month Urban Growing Planner
- Container Growing Blueprint Pack
- Heirloom Variety Selection Guide
- Fermented & Preserved Harvest Handbook
- Apartment Growing Complete Guide
- Grow Your Own Hot Sauce
- Harvest Preservation Field Manual
- Small-Scale Livestock Field Manual
- Meat/Fish Preservation Field Manual
- Hunting, Fishing & Trapping Field Manual

**Method**: Open `etsy-store-copy.md`, find each product's tags block, count characters for
every tag. Flag violations (tag length > 20 chars), propose replacement, and add to
`UPLOAD_SEQUENCE.md` in the Tag Corrections section.

**Priority**: Medium. Phase 1 must launch first. Do this task while Phase 1 is being uploaded
(Days 1-3) or immediately after Phase 1 goes live.

---

## Section 2: Tasks Available After Photo Shoot Completes (May 12+)

These tasks are sequenced after the May 10-11 photo shoot and can begin immediately on May 12.

---

### Task 2.1 — Image Culling Guidance (May 12)

**What**: During culling (selecting 30 of 80-100 RAW captures), apply these criteria to keep
orchestrator involvement consistent with the brief in `TRACK_B_READINESS_CHECKLIST.md`:

Selection criteria:
1. One sharp-focus frame per product-and-slot combination (reject motion blur, back focus)
2. For slot 4 (context shot): natural light visible, no harsh shadows crossing the product
3. For slot 5 (detail shot): printed page or key prop clearly readable at thumbnail scale
4. No frame where the product mock-up text is obscured or at an angle exceeding 15 degrees

After culling: confirm 30 selects are present (2 per product for 15 physical-shoot products,
accounting for Clusters A, B, C covering 16 products total — see cluster table below).

Physical shoot cluster breakdown (from `TRACK_B_PRODUCTION_PIPELINE.md`):
- Cluster A: 9 products (seed/garden) — 18 images expected
- Cluster B: 4 products (urban/container) — 8 images expected
- Cluster C: 3 products (food preservation) — 6 images expected
- Total: 16 products, 32 images from the physical shoot

Wait for user confirmation that 30+ selects exist before beginning batch editing.

---

### Task 2.2 — Image Editing Execution (May 13-14)

**What**: Apply the batch editing spec from `TRACK_B_READINESS_CHECKLIST.md` Section 1F.
Export 30 final JPEGs to `marketing/lifestyle-photos/etsy-ready/`.

**Editing consistency checklist** (from Section 1F):
- [ ] White balance: match across all images in the same cluster (all Cluster A window-light
  images should have the same color temperature)
- [ ] Exposure: no clipping in highlights on the printed product pages or white backgrounds
- [ ] Crop: 2400x2400 px square (1:1) — anchor the product in the lower-center third
- [ ] Sharpening: output sharpening for screen (not print) — apply at export
- [ ] File format: JPEG, quality 85-90 (stays under 400 KB per file while retaining detail)

**Output naming**: `[product-slug]-slot4.jpg` and `[product-slug]-slot5.jpg`

**Output path**: `marketing/lifestyle-photos/etsy-ready/`

**Log in WORKLOG.md**: Each exported file with its source cluster and edit date.

---

### Task 2.3 — Cluster D/E Canva Compositing (May 15)

**What**: For the 5 Cluster D/E products, apply the Canva compositing technique from
`phase-2-production-checklist.json` W4-05. These products use staged stock images from
`assets/stock-raw/` — no physical shoot needed.

**Products and source files**:

| Product | Slot 4 source | Slot 5 source | Output files |
|---------|--------------|--------------|-------------|
| survival-garden-regional-plans | `assets/stock-raw/survival-garden-regional-plans/survival-garden-regional-plans-slot4.jpg` | `…slot5.jpg` | `marketing/lifestyle-photos/etsy-ready/survival-garden-regional-plans-slot4.jpg` and `…slot5.jpg` |
| hunting-fishing-trapping-field-manual | `assets/stock-raw/hunting-fishing-trapping-field-manual/hunting-fishing-trapping-field-manual-slot4.jpg` | `…slot5.jpg` | `marketing/lifestyle-photos/etsy-ready/hunting-fishing-trapping-field-manual-slot4.jpg` and `…slot5.jpg` |
| small-scale-livestock-field-manual | `assets/stock-raw/small-scale-livestock-field-manual/small-scale-livestock-field-manual-slot4.jpg` | `…slot5.jpg` | `marketing/lifestyle-photos/etsy-ready/small-scale-livestock-field-manual-slot4.jpg` and `…slot5.jpg` |
| meat-fish-preservation-field-manual | `assets/stock-raw/meat-fish-preservation-field-manual/meat-fish-preservation-field-manual-slot4.jpg` | `…slot5.jpg` | `marketing/lifestyle-photos/etsy-ready/meat-fish-preservation-field-manual-slot4.jpg` and `…slot5.jpg` |
| native-plants-regional-guide | `assets/stock-raw/native-plants-regional-guide/native-plants-regional-guide-slot4.jpg` | `…slot5.jpg` | `marketing/lifestyle-photos/etsy-ready/native-plants-regional-guide-slot4.jpg` and `…slot5.jpg` |

**Compositing technique**: Open source image in Canva → place product PDF cover as an overlay
element → position and scale to sit naturally in scene → export as JPEG 2400x2400px.

**Test first**: Run the compositing technique on `survival-garden-regional-plans` slot 4 only.
Confirm the result looks convincing before running all 10 files. If the composite looks flat
or unconvincing, fall back to the flat 2D label overlay technique (see risk register in
`TRACK_B_PRODUCTION_PIPELINE.md`).

**Log in WORKLOG.md**: Each completed composite with source filenames, technique used, and
export date.

---

## Section 3: Zone Card Build Tasks (May 5-17)

Zone card content is 100% written. These tasks require only Canva access and
`CANVA_ZONE_CARD_BATCH_WORKFLOW.md` open alongside Canva. No user inputs are needed.

---

### Task 3.1 — Zone 5 Master Template Build (May 5-7, 150-180 min)

**Source**: `CANVA_ZONE_CARD_DESIGN_GUIDE.md` Parts 2-4 (step-by-step build guide)
**Content**: `CANVA_ZONE_CARD_BATCH_WORKFLOW.md` Zone 5 content table
**Zone band hex**: `#2D5016` (Temperate)
**Output**: Zone 5 master template saved in Canva as "Zone 5 Master — DO NOT EDIT"
**Export**: `assets/zone-cards/zone-5-quick-start-card.pdf`

This is the only build that takes 150-180 minutes — all subsequent cards are clone-and-swap
at 30-45 minutes each. This is the highest-value single Canva session in Track B.

---

### Task 3.2 — Zone 6 Card Build (May 5-7, 30 min)

**Source**: Clone Zone 5 master; update zone band color (same hex `#2D5016`); swap content
from `CANVA_ZONE_CARD_BATCH_WORKFLOW.md` Zone 6 table.
**Export**: `assets/zone-cards/zone-6-quick-start-card.pdf`

---

### Task 3.3 — Zone 3 Card Build (May 7-9, 45 min)

**Zone band hex**: `#3D6B8A` (Cool)
**Source**: Clone Zone 5 master; change band hex; swap Zone 3 content.
**Export**: `assets/zone-cards/zone-3-quick-start-card.pdf`

---

### Task 3.4 — Zone 4 Card Build (May 7-9, 45 min)

**Zone band hex**: `#3D6B8A` (Cool)
**Source**: Clone Zone 3 (already has correct band color); swap Zone 4 content.
**Export**: `assets/zone-cards/zone-4-quick-start-card.pdf`

---

### Task 3.5 — Zone 7 Card Build (May 11-12, 45 min)

**Zone band hex**: `#C9943A` (Warm)
**Source**: Clone Zone 5 master; change band hex; swap Zone 7 content.
**Export**: `assets/zone-cards/zone-7-quick-start-card.pdf`

Build on May 11 afternoon (same day as Cluster C shoot). The shoot ends by noon; the Canva
session runs in the afternoon.

---

### Task 3.6 — Zone 8 Card Build (May 11-12, 45 min)

**Zone band hex**: `#C9943A` (Warm)
**Source**: Clone Zone 7; swap Zone 8 content.
**Export**: `assets/zone-cards/zone-8-quick-start-card.pdf`

---

### Task 3.7 — Zone 9 Card Build (May 15-17, 45 min)

**Zone band hex**: `#A0522D` (Hot)
**Source**: Clone Zone 5 master; change band hex; swap Zone 9 content.
**Export**: `assets/zone-cards/zone-9-quick-start-card.pdf`

---

### Task 3.8 — Zone 10 Card Build (May 15-17, 45 min)

**Zone band hex**: `#A0522D` (Hot)
**Source**: Clone Zone 9; swap Zone 10 content.
**Export**: `assets/zone-cards/zone-10-quick-start-card.pdf`

---

### Task 3.9 — Full 8-Card Review (May 16-17, 30 min)

After all 8 cards are exported:

- [ ] Open each PDF and verify zone band color matches the correct color group
- [ ] Confirm zone number is correct on each card (Zone 3 = Zone 3, not Zone 5 misprint)
- [ ] Confirm "This Month" content block shows May 2026 content, not placeholder text
- [ ] Check footer URLs: `[ETSY-ZONE-CALENDAR-LINK]` — leave as-is if Etsy listing is not
  yet live; replace with actual URL when available
- [ ] Confirm all 8 PDFs are present in `assets/zone-cards/`

Expected files after review:
```
assets/zone-cards/zone-3-quick-start-card.pdf
assets/zone-cards/zone-4-quick-start-card.pdf
assets/zone-cards/zone-5-quick-start-card.pdf
assets/zone-cards/zone-6-quick-start-card.pdf
assets/zone-cards/zone-7-quick-start-card.pdf
assets/zone-cards/zone-8-quick-start-card.pdf
assets/zone-cards/zone-9-quick-start-card.pdf
assets/zone-cards/zone-10-quick-start-card.pdf
```

---

## Section 4: Email Automation Build Tasks (May 17-22)

These tasks require a Kit (kit.co) account to exist. That is a user-action gate (30 min,
no approvals). All email copy is production-ready and waiting.

---

### Task 4.1 — Kit Platform Setup Verification

**What**: Confirm the Kit free account is created and the following are set up:
- Zone Card sign-up landing page is live with a URL
- Subscriber zone preference field (dropdown: Zones 3-10) is added to the sign-up form
- Kit file library can receive 8 PDF uploads (verify free tier storage limit)

**Dependencies**: User must create the Kit account first. After that, this is an
orchestrator-executable configuration check.

**Reference**: `PHASE_2_EMAIL_STRATEGY.md` Part 2 (platform setup sequence) and
`marketing/email-automation-blueprint.md` (full technical setup).

---

### Task 4.2 — Zone Card Upload to Kit File Library

**What**: Upload all 8 zone card PDFs to Kit's file library. Each PDF gets a unique
download URL that the automation will send to subscribers based on their zone selection.

**File sources**: `assets/zone-cards/zone-[3-10]-quick-start-card.pdf` (all 8 files)

**Dependency**: Task 3.9 (all 8 cards reviewed and confirmed) must be complete first.

**Log**: Record each Kit download URL in WORKLOG.md alongside the PDF filename.
Format:
```
zone-3-quick-start-card.pdf | Kit URL: [URL] | uploaded 2026-05-[date]
```

---

### Task 4.3 — Email Automation Build in Kit

**What**: Build the 3-email welcome sequence in Kit using the production-ready copy from
`MAY_CONTENT_EXECUTION_PLAN.md` Section "Email Sequences."

Build order:
1. Email 1 — Zone Card delivery (8 zone-specific variants; triggered at sign-up)
   - One variant per zone; each sends the matching zone card download URL from Task 4.2
   - Kit routing: `IF subscriber.zone == 3 THEN send zone-3-link` (and so on for each zone)
2. Email 2 — Seed saving educational content (Day 5, single version for all subscribers)
3. Email 3 — Companion planting guide (Day 12, single version for all subscribers)

**Copy source**: `MAY_CONTENT_EXECUTION_PLAN.md` — Email Sequences section.
Subject lines, full body copy, and Kit setup notes are all present.

**Reference**: `PHASE_2_EMAIL_STRATEGY.md` Part 2 steps 3-6 for the platform setup sequence.

---

### Task 4.4 — End-to-End Email Test (May 17-22)

**What**: Send a test sign-up through the Kit form to verify the full automation works.

Test sequence:
1. Sign up with a test email address, selecting Zone 5
2. Confirm Email 1 arrives with the Zone 5 card download URL
3. Confirm the download URL returns `zone-5-quick-start-card.pdf`
4. Note that Email 2 and 3 will not arrive for 5 and 12 days respectively — manually trigger
   them in Kit's test mode instead of waiting

Second test:
1. Repeat with Zone 7 (largest subscriber population in Zone 7 belt per risk register)
2. Confirm Email 1 sends the Zone 7 card, not the Zone 5 card

**Pass criteria**: Both zone-specific deliveries work correctly. Log result in WORKLOG.md.

---

## Section 5: Pre-Launch Social Content Preparation (May 22-30)

These tasks run in parallel with the user's Week 4 social posting activity.

---

### Task 5.1 — Lifestyle Image Selection for Launch Week

**What**: From the 30 final lifestyle images in `marketing/lifestyle-photos/etsy-ready/`,
select the top 10 for launch-week social use.

Selection criteria:
- Visual diversity (no two adjacent posts with the same background or color tone)
- At least one image per content category: seeds/garden, food preservation, urban/container
- Best-performing thumbnail legibility (the product title or printed page must be readable
  at 200x200 px — test by zooming out in preview)

Output: A numbered list of 10 selected filenames, in recommended posting order, written to
WORKLOG.md.

---

### Task 5.2 — Pinterest Batch Production (May 25-29)

**What**: Using the 10 lifestyle images selected in Task 5.1, produce 15+ Pinterest pins
for Tier 1-2 products.

**Template specs**: `pin-template-specs.md` (5 templates, full specs)
**Implementation guide**: `CANVA_EXECUTION_PLAYBOOK.md` (Canva step-by-step)
**Hashtag stacks and captions**: `MAY_CONTENT_EXECUTION_PLAN.md` and
`phase-2-social-content-calendar-60day.md`

Output: 15+ Pinterest pin images at 1000x1500 px, saved to `marketing/lifestyle-photos/pins/`
with naming convention `[product-slug]-pin-[variant-number].jpg`.

---

### Task 5.3 — Launch Week Social Post Scheduling

**What**: Prepare the launch-week social post schedule for Buffer/Later (or native schedulers).

Schedule:
- May 30, 10:00 AM: Phase 2 launch announcement (Instagram Reel + TikTok — same video)
- May 30, 2:00 PM: Pinterest pin batch goes live (schedule 5 pins for this day)
- May 31: Instagram Carousel — "21 products now live" product overview
- June 1-2: Stories cadence from `MAY_CONTENT_EXECUTION_PLAN.md` Week 5

**Copy source**: `phase-2-social-content-calendar-60day.md` Days 29-33.

---

## Section 6: Task Summary by Date

| Date | Tasks | Depends On |
|------|-------|------------|
| May 1-4 | 1.1 directory verify, 1.2 stock file confirm, 1.4 tag audit for products 10-19 | Nothing |
| May 5-7 | 3.1 Zone 5 master build, 3.2 Zone 6 build | Canva Brand Kit (user, Day 1) |
| May 7-9 | 3.3 Zone 3 build, 3.4 Zone 4 build | Zone 5 master |
| May 11-12 | 3.5 Zone 7 build, 3.6 Zone 8 build | Photo shoot complete (user, May 11) |
| May 12 | 2.1 Image culling guidance | Photo shoot complete (user) |
| May 13-14 | 2.2 Image editing + export | May 12 culling |
| May 15 | 2.3 Cluster D/E compositing | Canva Brand Kit (user); stock files confirmed |
| May 15-17 | 3.7 Zone 9, 3.8 Zone 10, 3.9 full 8-card review | All zones 3-8 complete |
| May 17-22 | 4.1-4.4 Kit platform + email automation | Kit account (user); zone cards complete |
| May 22-30 | 5.1-5.3 social content prep + Pinterest batch | Lifestyle images complete |

---

## Section 7: User-Action Gates Summary

These are the only items the orchestrator cannot do. Listed for completeness.

| Gate | User Time Required | Unblocks |
|------|--------------------|---------|
| Social accounts (Instagram, TikTok, Pinterest) with handle `seedwarden` | 30-60 min | All social scheduling, Day 1 Reel, bio links |
| Canva Brand Kit setup (6 hex colors, 3 fonts, logo) | 30 min | Zone card builds (Tasks 3.1-3.8), pin production |
| Kit (kit.co) account creation | 30 min | Email automation (Tasks 4.1-4.4) |
| May 1: Start germination tray | 5 min | Sprout props for May 10 shoot |
| May 2-3: Film Day 1 Reel | 60-90 min | Week 1 social reach |
| May 5-9: Props sourcing run | Half-day | May 10 shoot |
| May 8: Submit pages to print shop | 15 min | Printed-page props at May 10 shoot |
| May 10-11: Photo shoot | 2 days | All Cluster A/B/C lifestyle images |

---

**Prepared**: 2026-05-01
**Status**: Tasks 1.1, 1.2, and 1.4 are available immediately. All others are sequenced
per the date table above.
