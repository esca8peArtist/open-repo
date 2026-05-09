---
title: "Phase 2 Launch Validation Report — Pre-Flight Asset & System Audit"
date: 2026-05-09
scope: Full end-to-end validation across 5 areas prior to May 30, 2026 launch
launch_date: 2026-05-30
days_until_launch: 21
assessor: Seedwarden Agent (file-system audit; no live platform access)
status: CONDITIONAL GO — 2 critical blockers, 3 high items, multiple medium items
---

# Phase 2 Launch Validation Report

**Prepared**: May 9, 2026
**Launch target**: May 30, 2026 (21 days)
**Scope**: Asset inventory audit + system readiness validation across 5 domains
**Method**: File-system inspection of `/projects/seedwarden/` and all planning documents. No live platform access (Etsy, Kit, Canva, social accounts, Buffer). Platform-side status is inferred from the most recent status documents on file, which reflect last-updated dates of May 5–9, 2026.

---

## Executive Summary

**Overall launch assessment: CONDITIONAL GO**

The Seedwarden Phase 2 launch is achievable on May 30, 2026 but requires immediate resolution of two critical blockers and three high-priority items within the next 7–10 days. Failure to resolve the critical blockers shifts the full launch to June 6, 2026 (the documented contingency date).

**What is ready**:
- Wild-edibles habitat photo set: 18/18 files present and correctly named
- Strategy, copy, and planning infrastructure: complete across all domains
- Social content calendar: 90-post schedule written and structured
- Email sequence copy: 5-email welcome sequence written and staged
- Etsy listing copy, pricing, and SEO tags: documented for all Phase 2 products
- Contingency playbooks, analytics dashboards, and go/no-go frameworks: production-ready

**What is not ready (as of last recorded status)**:
- Kit account, landing page, and automation: not created (confirmed NOT STARTED as of May 5, 2026)
- Canva Brand Kit and zone cards: not built (confirmed NOT STARTED as of May 5, 2026)
- Social media accounts (Instagram, TikTok, Pinterest): not created
- Lifestyle photography (Etsy slots 4–5): 0/42 images in etsy-ready directory
- Endangered-species photos: 0 files in assets/endangered-species-photos/
- Multiple wild-edibles photos: below 1200x800 minimum resolution threshold

**Severity summary**:
- Critical (launch blockers): 2
- High (must fix before May 28): 3
- Medium (acceptable with contingency): 4
- Low (post-launch fix): 3

---

## Validation Area 1: Photo Assets

### Wild-Edibles Habitat Photos (18 species)

**Finding**: All 18 required habit photo files are present in `assets/wild-edibles/`. File count: 18/18. File naming convention: correct (`[species-slug]-habit.jpg`).

**Resolution/dimension audit** (via file command on all 18 files):

| Species file | Dimensions | Min 1200x800? | Status |
|---|---|---|---|
| allium-tricoccum-habit.jpg | 1296x864 | YES | PASS |
| amaranthus-retroflexus-habit.jpg | 640x480 | NO — 640px wide | FAIL |
| arctium-lappa-habit.jpg | 2288x1712 | YES | PASS |
| asclepias-syriaca-habit.jpg | 1200x1800 | YES | PASS |
| chenopodium-album-habit.jpg | 1110x1671 | NO — 1110px wide | FAIL |
| cichorium-intybus-habit.jpg | 500x437 | NO — both dims low | FAIL |
| daucus-carota-habit.jpg | 500x333 | NO — both dims low | FAIL |
| epilobium-angustifolium-habit.jpg | 375x500 | NO — both dims low | FAIL |
| fallopia-japonica-habit.jpg | 1200x828 | YES | PASS |
| fragaria-virginiana-habit.jpg | 375x500 | NO — both dims low | FAIL |
| helianthus-tuberosus-habit.jpg | 375x500 | NO — both dims low | FAIL |
| nasturtium-officinale-habit.jpg | 375x500 | NO — both dims low | FAIL |
| oxalis-stricta-habit.jpg | 834x672 | NO — 834px wide | FAIL |
| portulaca-oleracea-habit.jpg | 500x281 | NO — both dims low | FAIL |
| stellaria-media-habit.jpg | 1600x1200 | YES | PASS |
| taraxacum-officinale-habit.jpg | 1765x1413 | YES | PASS |
| typha-latifolia-habit.jpg | 500x375 | NO — both dims low | FAIL |
| urtica-dioica-habit.jpg | 609x640 | NO — 609px wide | FAIL |

**Resolution pass/fail**: 6 pass (1200x800+), 12 fail. The 12 failing files are all present and renderable JPEG files but do not meet the 1200x800 minimum suitable for Canva guide production.

**Severity**: HIGH — 12 of 18 wild-edibles photos are below minimum resolution for guide and Etsy use. These files were downloaded from Wikimedia Commons and represent the images available under CC licensing, but smaller-format versions were used. For Canva layout at print quality these need replacement with higher-resolution sources where available.

**Licensing documentation**: WORKLOG.md contains no download entries for wild-edibles photos (the worklog records sessions from May 9 only, not prior download sessions). The files were added to the repository on April 14 (stellaria, taraxacum) and April 28 (remaining 16). CC license documentation for these 18 files is absent from WORKLOG.md. The files are named correctly and attributed via the ENDANGERED_SPECIES_PHOTO_PIPELINE.md protocol, but the actual WORKLOG entries confirming source URL and license per file are missing.

**Severity**: MEDIUM — licenses need retroactive documentation before commercial use in guides and Etsy listings.

### Endangered-Species Candidate Photos

**Finding**: `assets/endangered-species-photos/` directory exists but contains 0 files. The ENDANGERED_SPECIES_PHOTO_PIPELINE.md (prepared May 6) documents a complete sourcing plan for American Ginseng, Goldenseal, Black Cohosh, and Ramps (Wave 1), with iNaturalist CC-BY search URLs and institutional outreach templates. As of May 6, the iNaturalist sourcing sprint and all institutional outreach were listed as "Not started."

**Current status**: 0 photos sourced. Phase 2 endangered species series (Wave 1) targets a September 2026 launch. This does not block the May 30 launch — endangered-species guides are not in the Phase 2 May launch scope. However, the June 15 first checkpoint for Phase 2 performance evaluation requires confident production of endangered species content to begin by June/July if the September timeline is to hold.

**Severity**: MEDIUM (does not block May 30 launch; blocks September 2026 Wave 1 launch if not started by June).

### Format and Corruption Check

All 18 wild-edibles photos were confirmed valid JPEG files (JFIF standard, readable by the `file` command). No corrupted files detected. All are baseline or progressive JPEG format. No encoding errors.

**Severity**: LOW — no action required for file integrity.

---

## Validation Area 2: Guide Template Validation (Canva)

**Finding**: Canva Brand Kit and all zone card templates are confirmed NOT STARTED as of May 5, 2026 (CANVA_SETUP_STATUS.md) and NOT STARTED as of April 29, 2026 (TRACK_B_LAUNCH_STATUS.md). No evidence of completion in any subsequent document.

**What was planned**:
- Canva Brand Kit: 6 hex colors, 3 fonts (Playfair Display, Lato/Source Sans 3, Cormorant Garamond), logo upload — estimated 30 minutes
- Zone 5 master card: 150–180 minutes (the gating deliverable for all other 7 cards)
- Zones 6, 3, 4, 7, 8, 9, 10: 35–45 minutes each (clone from Zone 5)
- Total Canva build: 7.5–9 hours

**What was needed by what date**: Brand Kit by May 8; Zone 5 master by May 9; all 8 zone cards by May 17 (per may-30-launch-readiness-audit.md critical path).

**Current position (May 9)**: If the Brand Kit has not been started, the Zone 5 master card is already 1 day behind the critical path. Zone card completion by May 17 is still achievable but requires an immediate start and roughly 3–4 hours per day across May 10–17 while also executing the photo shoot.

**Zone card PDF directory**: `assets/zone-cards/` exists but contains 0 PDF files. No zone card has been exported.

**Guide template assessment for screen sizes and brand consistency**: Cannot directly validate in Canva (agent has no browser/Canva access). However, full specifications exist in CANVA_ZONE_CARD_DESIGN_GUIDE.md and CANVA_SETUP_STATUS.md including: exact hex codes, font pairing, layout zones, column guides at documented pixel positions, and footer placeholder protocol. Design specifications are production-ready; execution has not started.

**Pinterest pin templates**: 5 templates specified in `pin-template-specs.md`, none built. Social calendar image references (cluster-a-slot4.jpg, cluster-b-slot4.jpg, cluster-c-slot4.jpg, cluster-a-bts.jpg, quote-card.jpg, cluster-d-composite.jpg) all resolve to files that do not exist in `marketing/lifestyle-photos/etsy-ready/`.

**Canva pricing tier**: Free tier confirmed sufficient for all Phase 2 zone card work. Pro not required.

**Severity**: CRITICAL — Canva Brand Kit and zone cards are on the critical path. Zone cards gate Kit Email 1 (email automation cannot be tested without them). Without zone cards, the Kit email funnel cannot go live, which means the May 30 launch cannot include email list building.

---

## Validation Area 3: Email Automation (Kit)

**Finding**: Kit account is confirmed NOT STARTED as of May 5, 2026 (KIT_SETUP_NOTES.md, CANVA_SETUP_STATUS.md). All setup steps (account creation, tags, landing page, email sequence, automation wiring, end-to-end test) are listed as NOT STARTED.

**What exists and is ready**:
- Full 5-email welcome sequence copy: in `marketing/email-and-launch-plan.md`
- Day-by-day email timing and A/B subject lines: in `phase-2-email-automation-sequence.md`
- Complete tag architecture (15 tags — 8 zone + 7 interest cohort): documented in KIT_SETUP_NOTES.md
- Zone routing automation logic: documented (Option A — 8 Email 1 variants per zone)
- Landing page specifications: complete (headline, form fields, CTA text, trust text, background color)
- UTM schema for GA4 attribution: documented and ready to apply
- End-to-end test protocol: documented with specific failure diagnosis paths
- Compliance: unsubscribe language specified, privacy policy link expected in footer (not confirmed as drafted)
- CAN-SPAM: Kit platform-level compliance assumed (Kit handles footer requirements for commercial senders)

**What is blocked**:
- Kit account creation (user action, 10 minutes)
- Landing page build and publish (30–45 minutes)
- Email sequence build in Kit UI (60–90 minutes per pass)
- Zone card PDF uploads to Google Drive (prerequisite: zone cards must exist)
- End-to-end test (prerequisite: landing page live + zone cards deliverable)
- Launch broadcast scheduling (prerequisite: automation must be live and tested)

**Critical dependency chain**: Canva zone cards → Google Drive upload → Kit Email 1 variants → automation wiring → end-to-end test → landing page goes live → bio links go active → email list building begins. Every link in this chain is currently at zero.

**Email compliance**: Kit free tier confirmed adequate (up to 10,000 subscribers, unlimited sends, 1 landing page). SPF/DKIM DNS configuration documented in `docs/phase-2-setup-guides/phase-2-kit-landing-page-setup-guide.md`. However, these records have not been submitted — they cannot be submitted until the Kit account exists. DNS propagation takes up to 48 hours, creating a time buffer requirement: Kit account must exist by May 20 at the latest to guarantee SPF/DKIM are active before May 30.

**Severity**: CRITICAL — Kit account creation is the single highest-priority user action. It gates email list building, zone card delivery, launch broadcast, and the entire email revenue channel.

---

## Validation Area 4: Etsy Integration

**Finding**: Phase 2 Etsy product listings are documented in planning files but their live status cannot be confirmed (agent has no Etsy account access). Phase 1 status from last available document (ETSY_PHASE_1_UPLOAD_CHECKLIST.md, April 26, 2026) confirmed 6 lead products ready for upload with one critical issue: `native-plants-regional-guide.pdf` exceeds Etsy's 5MB limit at 56.96MB.

**Listing copy and SEO**: Phase 2 product descriptions, titles, pricing, and tag sets are documented in:
- `products/` directory guides (21 product files confirmed present)
- `etsy-store-copy.md` (store bio and policy copy)
- `etsy-seo-market-research.md` (keyword research)
- `may-2026-competitor-pricing-update.md` (seasonal keyword table)
- `endangered-species-market-analysis.md` (Phase 2 endangered species SEO context)

All listing copy is written and tagged to Etsy's 13-tag maximum. Titles are in natural language format per the May 2026 Etsy title algorithm documented in `phase-2-pre-launch-checklist.md`.

**Product photography (Etsy slots 4–5)**:
- `marketing/lifestyle-photos/etsy-ready/` directory: 0 files
- `marketing/lifestyle-photos/pins/` directory: 0 files
- `assets/stock-raw/` directory: stock images staged for Clusters D and E (native plants, hunting, meat/fish, livestock, survival garden) — 5 products × 2 slots = 10 images staged but not composited
- Clusters A, B, C (12 products): require physical photo shoot (planned May 10–11)
- Status: 0/42 Etsy lifestyle images in the etsy-ready directory

**Brand consistency**: Phase 2 product photography strategy is documented in `LIFESTYLE_PHOTOGRAPHY_STRATEGY.md`. Brand colors and typography for photo overlays are specified in `CANVA_EXECUTION_PLAYBOOK.md`. The consistency framework exists but no Phase 2 photos have been produced yet, so consistency cannot be verified.

**Shop policies**: `etsy-store-copy.md` includes shipping, returns, refunds, and digital download policies. These are documented but cannot be confirmed as live in the Etsy shop (agent has no platform access).

**Native plants PDF**: The 56.96MB native-plants-regional-guide.pdf exceeds Etsy's 5MB limit. This was flagged as a critical issue in April. No resolution document exists. Options A (exclude from Phase 1/2) and B (recompress) were identified but neither shows evidence of execution.

**SEEDWARDEN15 coupon**: Planned discount code for Kit Email 5. Documented in the pre-launch checklist as requiring creation in Etsy Shop Manager before May 22. Cannot confirm whether created (platform access required).

**Severity**: HIGH — 0/42 lifestyle photos in the etsy-ready directory. Physical photo shoot (May 10–11) is on the critical path. Additionally, the native-plants PDF oversize issue requires explicit resolution before any launch scope that includes that listing.

---

## Validation Area 5: Social Media Assets and Scheduling

**Finding**: Social media accounts (Instagram, TikTok, Pinterest) are confirmed NOT STARTED as of April 29 (TRACK_B_LAUNCH_STATUS.md). Last recorded status: accounts not created.

**What is ready**:
- 60-day content calendar: 90 posts across Instagram, TikTok, Pinterest (June 1–30) in `docs/phase-2-operations/phase-2-social-posting-scheduler.csv`
- Caption copy, hashtag packs (10–15 per post), platform-specific posting times: fully specified
- Content type distribution: Educational (40%), Product Pin (22%), CTA (15%), Social Proof (12%), BTS (10%), Launch (1%)
- Video scripts for Instagram Reels and TikTok: documented in `marketing/video-scripts/`
- Hashtag strategy: 10 evergreen + rotating seasonal, platform-specific, within 10–15 per post
- Pinterest pin templates: specifications complete in `pin-template-specs.md` (5 templates)

**What is not ready**:
- Social accounts: not created (zero posting history, which the pre-launch checklist identifies as increasing launch-day algorithm suppression risk)
- Image files referenced in the social calendar: all resolve to `marketing/lifestyle-photos/etsy-ready/` which is empty
- Pinterest pin image files: `assets/zone-cards/zone-5-preview.png` (referenced in 8 pins) does not exist
- Scheduling tool (Buffer/Later): account not set up, posts not loaded
- Pre-launch content (Day 1 Reel, Day 3 Carousel, first 6 Pinterest pins): not produced

**Hashtag count validation**: Spot-checked 10 posts in the CSV. All contain 6–8 hashtags in the CSV hashtag field. The strategy document specifies 10–15 hashtags per post as best practice. The CSV hashtag packs are shorter than the strategy target — this is a medium-priority item (more hashtags increase discovery but shorter sets are acceptable).

**Link validation**: All Etsy listing destination links in the CSV are written as product names (e.g., "Harvest Preservation Handbook Etsy listing") rather than actual URLs. UTM-parameterized URLs have not been inserted. This means the social calendar is written but not production-ready for copy-paste into Buffer without a URL insertion pass.

**Visual consistency**: Cannot validate (no photos or account assets exist to compare). The brand guide (colors, fonts, layout principles) is fully documented. Consistency will be achievable once Canva Brand Kit is set up and applied to pin templates.

**Severity**: HIGH — accounts not created (social account creation was on zero-slack schedule as of May 7). Without accounts, no pre-launch content can post, and the algorithm-warming period before launch day has already been compressed or lost.

---

## Severity-Classified Findings

### Critical (Launch Blockers)

**CRITICAL-1: Kit account, landing page, and automation not created**
- Impact: No email list building. No zone card delivery. No launch broadcast. Email revenue channel offline at launch.
- Fix: User creates Kit account (10 min) + builds landing page (30–45 min). Email sequence build requires Kit account + zone card PDFs.
- Owner: User (platform access required)
- Timeline: Kit account must exist by May 10; landing page by May 12; full automation by May 22; end-to-end test by May 22.
- Contingency: If Kit not live by May 25, launch proceeds as social+Etsy-only; email comes online in first week of June (documented in june-6-contingency-path.md).

**CRITICAL-2: Canva Brand Kit and zone cards not built**
- Impact: Blocks Kit Email 1 variants (no zone card PDFs to link). Blocks all Pinterest pin production. Blocks Etsy listing image compositing for Cluster D+E. Blocks social content image library.
- Fix: User sets up Canva Brand Kit (30 min) then builds Zone 5 master card (150–180 min); clone remaining 7 zones (3.5–4 hours additional).
- Owner: User (Canva access required)
- Timeline: Zone 5 master by May 11; all 8 cards by May 17; PDF export to Google Drive by May 17.
- Contingency: If zone cards slip to May 20, Kit automation setup compresses to 2 days before the end-to-end test target (still feasible; tight).

### High (Fix Before May 28)

**HIGH-1: Social media accounts not created**
- Impact: Zero posting history before launch day; algorithm suppression risk on May 30 posts. No live bio link to Kit landing page. No social proof or warm audience at launch.
- Fix: User creates Instagram Business (20 min), TikTok Business (15 min), Pinterest Business (15 min); adds Kit landing page URL to all bios.
- Owner: User
- Timeline: Accounts should have been created May 7. Every additional day further compresses pre-launch posting history. Create by May 10 at the absolute latest to have 20 days of posting history.

**HIGH-2: Etsy lifestyle photos (slots 4–5) — 0/42 produced**
- Impact: All Phase 2 Etsy listings launch with only 3 images (mockup slots 1–3). Listings are less competitive and conversion rates will be lower. The 12 Cluster A/B/C products require physical photography.
- Fix: Execute planned May 10–11 photo shoot (8.5 hours across 2 days); cull and edit May 12–14; export and upload to Etsy by May 22.
- Owner: User (physical photography)
- Timeline: May 10–11 shoot date is already set. If shoot slips to May 17–18, launch proceeds with partial images; June 3–6 for all slots to be complete.
- Contingency: Stock compositing for Cluster D+E (5 products) can proceed independently — stock images are staged in assets/stock-raw/.

**HIGH-3: 12 of 18 wild-edibles photos below 1200x800 resolution**
- Impact: Insufficient resolution for Canva guide layout at print quality. Etsy listing use would produce blurry or pixelated results on zoom.
- Fix: Source higher-resolution versions from Wikimedia Commons for the 12 affected species. The WORKLOG.md Wikimedia search URLs and species identification work is already done; higher-resolution file versions are typically available on Wikimedia.
- Owner: Agent can execute (Wikimedia download task)
- Timeline: Before Canva guide layout begins. Canva layout for wild-edibles guides is not yet in the critical path for May 30 launch (wild-edibles guides are Phase 1 products); however, resolution must be resolved before any guide PDF production.
- Specific species needing replacement: amaranthus-retroflexus (640x480), chenopodium-album (1110x1671 — width is borderline), cichorium-intybus (500x437), daucus-carota (500x333), epilobium-angustifolium (375x500), fragaria-virginiana (375x500), helianthus-tuberosus (375x500), nasturtium-officinale (375x500), oxalis-stricta (834x672), portulaca-oleracea (500x281), typha-latifolia (500x375), urtica-dioica (609x640).

### Medium (Acceptable With Contingency Plan)

**MEDIUM-1: Wild-edibles CC licensing not documented in WORKLOG.md**
- Impact: 18 photos in production use without per-file license documentation. If any file is incorrectly licensed, it creates commercial use liability.
- Fix: Add retroactive WORKLOG.md entries for all 18 files with source URL, license, and attribution line. WORKLOG.md template exists.
- Owner: Agent can execute (research + document)
- Timeline: Before any guide PDF exports or Etsy listing use.

**MEDIUM-2: Endangered-species photo sourcing not started**
- Impact: Does not affect May 30 launch. Affects September 2026 Wave 1 guide launch. All 4 species (Ginseng, Goldenseal, Black Cohosh, Ramps) have 0 photos sourced. Institutional outreach emails (MBG, NCBG) not sent.
- Fix: Execute iNaturalist CC-BY sourcing sprint and send institutional outreach emails per ENDANGERED_SPECIES_PHOTO_PIPELINE.md. Sprint is self-serve and can be done in a focused session.
- Owner: Agent can execute iNaturalist sprint; user must send institutional emails from wanka95@gmail.com.
- Timeline: Start sourcing sprint week of May 12; send outreach emails by May 15 (allows 2–4 weeks for institutional response before June guide production begins).

**MEDIUM-3: native-plants-regional-guide.pdf oversize issue unresolved**
- Impact: PDF at 56.96MB cannot be uploaded to Etsy (5MB limit). This listing cannot go live until resolved.
- Fix: Re-export PDF with compressed images (target <1MB). ETSY_PHASE_1_UPLOAD_CHECKLIST.md identified this in April; no resolution documented.
- Owner: Agent (can attempt PDF recompression via scripts if source is accessible; otherwise user action with PDF optimizer).
- Timeline: Must be resolved before any Etsy upload session that includes native plants.

**MEDIUM-4: Social calendar image files do not exist**
- Impact: The 90-post social calendar references image files that are all in `marketing/lifestyle-photos/etsy-ready/` (empty directory). Buffer/Later upload cannot proceed until images exist. Posts referencing zone-5-preview.png and BTS/testimonial composites also reference non-existent files.
- Fix: Image files are produced as part of the photo shoot and Canva compositing workflow (HIGH-2 and CRITICAL-2). This medium finding resolves automatically when those are complete.
- Owner: Resolved by HIGH-2 and CRITICAL-2 completion.
- Timeline: By May 22 (lifestyle images); zone-5-preview.png by May 17 (zone card export).

### Low (Post-Launch Fix)

**LOW-1: Social calendar hashtag packs shorter than strategy target**
- Impact: 6–8 hashtags per post in the CSV vs. 10–15 recommended in the strategy. Minor reduction in discovery reach.
- Fix: Expand hashtag packs to 10–15 when loading posts into Buffer.
- Owner: User (during Buffer load session, May 25–29).
- Timeline: Pre-launch or within first week of posting.

**LOW-2: Social calendar Etsy links are names, not URLs**
- Impact: Posts cannot be copy-pasted into Buffer without a URL insertion pass. Low risk — this is a pre-scheduling data entry task.
- Fix: Before loading into Buffer, replace all Etsy product name references with actual UTM-parameterized Etsy listing URLs. UTM schema is documented in `phase-2-email-automation-sequence.md`.
- Owner: User (during Buffer load session).
- Timeline: May 25–29 (Buffer loading session).

**LOW-3: Buffer/Later account not set up; connections not authorized**
- Impact: Scheduled posting cannot be loaded until connected. OAuth tokens require re-authorization every 30 days — plan to re-authorize the week before launch.
- Fix: Set up Buffer or Later, connect all three platforms. Load 60-day calendar.
- Owner: User.
- Timeline: May 25. Per the pre-launch checklist, Buffer connections should be re-authorized within 7 days of launch (so no later than May 23).

---

## Remediation Timeline (May 10–29)

| Date | Action | Owner | Resolves |
|------|--------|-------|----------|
| May 10 | Create Instagram, TikTok, Pinterest Business accounts; add placeholder bios | User | HIGH-1 |
| May 10 | Create Kit account at kit.co | User | CRITICAL-1 |
| May 10–11 | Execute photo shoot (Clusters A, B, C) | User | HIGH-2 (partial) |
| May 10 | Set up Canva Brand Kit (30 min) | User | CRITICAL-2 (unblocks) |
| May 11 | Begin Zone 5 master card in Canva | User | CRITICAL-2 |
| May 12–16 | Edit and export lifestyle photos; build remaining zone cards | User | HIGH-2, CRITICAL-2 |
| May 12 | Begin iNaturalist endangered-species photo sprint | Agent | MEDIUM-2 |
| May 13 | Add retroactive WORKLOG entries for 18 wild-edibles photos | Agent | MEDIUM-1 |
| May 13 | Source higher-res versions of 12 undersized wild-edibles photos | Agent | HIGH-3 |
| May 15 | Send institutional outreach emails (MBG, NCBG) | User | MEDIUM-2 |
| May 17 | Export all 8 zone card PDFs; upload to Google Drive | User | CRITICAL-2 |
| May 17–21 | Build Kit landing page, 15 tags, Email 1–5, automation wiring | User | CRITICAL-1 |
| May 22 | Kit end-to-end test (Zone 5 and Zone 7) | User | CRITICAL-1 |
| May 22 | Upload lifestyle images to Etsy slots 4–5 | User | HIGH-2 |
| May 22 | Composite Cluster D+E stock images in Canva; upload to Etsy | User | HIGH-2 |
| May 25 | Set up Buffer/Later; begin loading 60-day calendar | User | LOW-3 |
| May 25–29 | Insert Etsy UTM URLs into social calendar; expand hashtag packs | User | LOW-1, LOW-2 |
| May 28 | Final system checks: Google Drive links, Kit automation, Etsy coupon, Buffer OAuth | User | All |
| May 29 | Pre-launch go/no-go (Etsy / Kit / Social / Canva-Files) per pre-launch checklist | User | Final gate |

---

## Risk Mitigation: Contingency Path

If critical blockers are not resolved by May 22, the June 6, 2026 contingency path is activated. This is a documented and fully planned option:

**May 30 soft launch (if photo shoot slips or Kit is not fully tested)**:
- Kit automation may be live but not fully tested — proceed with live but monitor closely
- Etsy listings active with slots 1–3 (mockup images only); slots 4–5 upload June 1–6
- Social accounts live and posting; lifestyle image content follows as produced

**June 6 full launch**:
- All 42 lifestyle images in Etsy slots 4–5
- Kit automation end-to-end tested and confirmed
- Buffer loaded with full 60-day calendar
- Zone card PDFs confirmed downloadable

**Reference**: `june-6-contingency-path.md` and `phase-2-contingency-playbook.md` document this path in full. The June 6 contingency does not reduce total Phase 2 revenue potential — it shifts the launch window by 7 days.

---

*Prepared: 2026-05-09. Scope: file-system audit of /projects/seedwarden/. No live platform access. Platform status inferred from most recent status documents on file. All time estimates from reference planning documents. File resolution measurements from `file` command output.*
