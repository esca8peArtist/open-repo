---
title: "Phase 2 Contingency Playbook"
subtitle: "Scenario-based recovery for photo delay, Kit block, Canva failure, low Phase 1 conversion, and social account issues"
date: 2026-05-06
status: production-ready
covers: top-5-failure-modes
references:
  - june-6-contingency-path.md
  - phase-2-execution-timeline.md
  - TRACK_B_FINAL_EXECUTION_GUIDE.md Section 4
  - phase-2-tool-integration-map.md
---

# Phase 2 Contingency Playbook

**Purpose**: Scenario-specific recovery sequences for the five most likely failure modes. Each scenario has: a trigger condition (how you know it has happened), an immediate response, a recovery sequence, and a revised timeline. None of these scenarios require abandoning Phase 2 — they require routing to a documented alternate path.

**Key principle**: Phase 2 has four parallel workstreams (photography, zone cards, Kit email, social). Three of the four are completely independent of photography. Every contingency described here preserves at least three of the four workstreams on the original schedule.

---

## Scenario 1: Photo Shoot Slips to May 17-18

**What triggers this**: May 10-11 shoot does not happen due to weather, equipment failure, scheduling conflict, illness, or venue unavailability.

**Detection date**: By end of day May 11 (if no shoot happened on May 10-11, this scenario is active).

**Decision deadline**: Make the June 6 call by May 20 — not May 27. Deciding at May 20 gives 17 days to June 6. Deciding at May 27 compresses everything into a 9-day sprint.

---

### Immediate Response (within 24 hours of triggering)

1. Log in WORKLOG.md: "June 6 contingency path activated. Trigger: photo shoot delayed. Date of decision: [date]."
2. Check availability for May 17-18 shoot (same format, same props, same shot list — just one week later).
3. Confirm germination tray status: if the tray was started April 30 or May 1, sprouts will be 17-18 days old by May 17-18, which is still usable (they may be slightly more mature than ideal but they photograph fine).

---

### Recovery Sequence

| Date | Action | Notes |
|---|---|---|
| May 11-16 | Zone card production continues on ORIGINAL SCHEDULE — unaffected by photo delay | All 8 zone cards can be built without photos |
| May 15-16 | Kit account setup, tags, landing page, and Email 1-5 build — ORIGINAL SCHEDULE | Kit setup has zero dependency on photography |
| May 17-18 | Photo shoot: same 2-day structure (Cluster A Saturday, Cluster C Sunday) | Same location, same props, same shot list |
| May 19-20 | Image culling: 80-100 RAW → 30 selects | 2 hours |
| May 21 | Batch editing and export: 30 JPEGs to /etsy-ready/ | 3-4 hours |
| May 22-24 | Canva lifestyle compositing: 21 products × 2 slots = 42 images | 4-5 hours |
| May 23 | Kit end-to-end test and automation go-live (ORIGINAL SCHEDULE — independent of photos) | Kit goes live May 23 regardless |
| May 25-30 | Teaser social track: post zone card previews, behind-the-scenes shoot content, Cluster D+E stock composite images (available without physical shoot) | Maintain social presence May 25-30 even without lifestyle photos |
| May 28-June 4 | Etsy lifestyle image upload (slots 4-5 for all 21 products) | Cluster D+E can upload May 21 as planned; Clusters A, B, C upload May 28-June 4 |
| June 5 | Pre-launch QA: all 21 listings at 5-image status, Kit broadcast rescheduled, social posts rescheduled | Same QA sequence as May 29 but on June 5 |
| June 6 | Full launch: Etsy 10am, email 12pm, social 2pm — identical sequence to May 30 | Same launch day procedure |

### What Does NOT Change (Run on Original Schedule)

These tracks are fully independent of photography. Do not delay them:
- Zone card builds (May 7-21)
- Kit account setup and email sequence build (May 6-16)
- Kit automation wiring and testing (May 16-23)
- Kit automation go-live (May 23)
- Social account creation (May 6)
- Brand Kit setup in Canva (May 6)

### May 30 Soft Launch (Optional, Recommended)

Even on the June 6 path, run a soft launch on May 30 without lifestyle photos:

| Content | Source | What It Communicates |
|---|---|---|
| Zone card preview graphic | Export zone 5 card as PNG in Canva, overlay "Free for growers" badge | "Your free zone guide is ready" |
| Behind-the-scenes shoot reel | Phone footage from the May 17-18 shoot | "Real guide, real grower — here's how it's made" |
| Cluster D+E stock composite images | Already available: survival garden, hunting manual, livestock manual, native plants | 5 products with lifestyle-adjacent appearance |
| Announcement text post | No images needed | "Phase 2 is live June 6 — get your free zone card now at the link in bio" |

The soft launch maintains social momentum, captures email sign-ups via the bio link starting May 25 (when Kit automation is live), and frames June 6 as an anticipated event rather than a delayed one.

### Revenue Impact

Zero. Phase 1 Etsy listings continue generating sales throughout the delay period. The broadcast reaches the same subscriber list on June 6, which by then has accumulated 24-36 additional subscribers from the extra list-building days compared to a May 30 launch.

### Revised Timeline Snapshot

| Launch Track | May 30 Path | June 6 Path | Difference |
|---|---|---|---|
| Zone cards (8 PDFs in Kit) | May 22 | May 22 | No change |
| Kit automation live | May 23 | May 23 | No change |
| Social accounts live | May 6 | May 6 | No change |
| Etsy lifestyle images uploaded | May 15-20 | May 28-June 4 | +8-15 days |
| Email broadcast | May 30 12pm | June 6 12pm | +7 days |
| Social launch posts | May 30 2pm | June 6 2pm | +7 days |

---

## Scenario 2: Kit Account Blocked on Verification

**What triggers this**: Kit account creation is rejected, flagged for review, or the account is suspended after creation due to a new-account policy review.

**Detection**: Kit sends an account restriction notice, or the automation is paused without your action, or the landing page stops accepting subscribers.

**Decision deadline**: If Kit is not operational by May 20, activate the Google Form fallback immediately.

---

### Immediate Response

1. Contact Kit support through kit.co/support. Describe the use case: a new Etsy seller using Kit for a free lead magnet (zone quick-start cards). This is a standard creator/e-commerce use case — restrictions are usually resolved within 24-48 hours.
2. While waiting for Kit support: set up Google Form fallback (15 minutes).
3. Update all social bios to point to the Google Form URL instead of the Kit landing page.

---

### Google Form Fallback Setup (15 minutes)

1. Go to forms.google.com > Create a new form
2. Title: "Get Your Free Zone Quick-Start Card"
3. Add fields:
   - "First name" (Short answer, required)
   - "Email address" (Short answer, required — add email format validation)
   - "Your growing zone" (Multiple choice, required — options: Zone 3, Zone 4, Zone 5, Zone 6, Zone 7, Zone 8, Zone 9, Zone 10)
4. Add a header description: "Know exactly what to plant right now in your zone. Free one-page reference card delivered by email."
5. Click "Send" > copy the shareable link
6. Update all social bios with the Google Form link
7. Set up Google Sheets response destination (Form > Responses tab > Sheets icon) to collect sign-ups

### Manual Delivery Protocol (While Kit is Down)

For each new Google Form submission:
1. Note the subscriber's name, email, and zone
2. Send a Gmail reply from wanka95@gmail.com attaching the corresponding zone card PDF (from assets/zone-cards/)
3. Subject line: "Your Zone [X] Quick-Start Card from Seedwarden"
4. Body: paste Email 1 copy from marketing/email-and-launch-plan.md, substituting the zone number
5. Log the subscriber in a local spreadsheet with: name, email, zone, date subscribed, email 1 sent date

This is manageable at launch list sizes. At 5-15 subscribers per week, manual delivery takes under 30 minutes per week.

### Week 2 Re-Integration Into Kit

When Kit account resolves:
1. Import the manual Google Sheets list into Kit (Kit > Subscribers > Import > upload CSV)
2. For each imported subscriber, apply their zone tag manually (Kit > Subscriber profile > Tags)
3. Determine which welcome sequence email each subscriber should be on based on their subscription date
4. Manually enroll each subscriber at the correct point in the Seedwarden Welcome sequence
5. Remove the Google Form from social bios; replace with the Kit landing page URL

### Impact on Launch

- Email broadcast timing is NOT affected — the broadcast goes to the full confirmed subscriber list on May 30 (or June 6) regardless of whether subscribers were acquired via Kit or via the Google Form fallback
- Zone card delivery continues without interruption
- The only degradation is that behavioral tag click-tracking (Emails 3 and 4) cannot work via Gmail — you lose segmentation data for the subscribers acquired during the Kit outage. When they are re-enrolled in Kit on Week 2, they receive the full sequence going forward.

---

## Scenario 3: Canva Export Failure or Account Access Blocked

**What triggers this**: Canva export produces corrupted PDFs, zone cards fail to download, or Canva account access is blocked (billing issue on a free account is rare but possible if Canva pro trial expired and created a payment block).

**Detection**: PDF exports produce blank files, corrupt files, or Canva shows a download error. Or Canva login shows an account restriction.

---

### Immediate Response

1. Try exporting a test design (a simple 1-page Canva document with just text) to confirm whether the export function itself is broken or only specific zone card files.
2. If export is broken account-wide: clear browser cache and cookies, try again. Try in a different browser (Chrome vs. Firefox vs. Safari). Try in an incognito window.
3. If account access is blocked: go to canva.com/help — free tier accounts are rarely blocked, but if they are, support typically resolves within 24 hours.

---

### Recovery Option A: Static Graphic Fallback (2-3 hours)

If Canva zone card builds are blocked but you have previously created a partially-built card:

1. Take a screenshot of the Canva canvas (full-screen screenshot of the design at high zoom)
2. Crop to the card dimensions (1200×900px) using any photo editor
3. Export as JPEG (not PDF)
4. Upload to Google Drive as an image file (not PDF)
5. In Kit Email 1: update the download button link to the JPEG image URL
6. The subscriber receives a JPEG image instead of a PDF — this is functional (opens in any browser, can be saved and printed) but slightly lower quality than the PDF format

**Zone card count reduction under time pressure**: If compression is needed, launch with 4 zone cards (Zones 5, 6, 7, 8) and send "Your zone's card is coming soon" placeholder Email 1 for Zones 3, 4, 9, 10 with a follow-up email when those cards are ready (Week 2 of June).

---

### Recovery Option B: Figma Alternative (3-4 hours)

If Canva is completely unusable:

1. Go to figma.com > Free account (if not already registered)
2. Import the Brand Kit: add the 10 colors as a color palette in Figma, set font styles for Playfair Display, Lato, and Cormorant Garamond
3. Create a new frame at 1200×900px
4. Rebuild the Zone 5 master card using the same layout specifications in phase-2-canva-workflow.md Part 2
5. Figma export: File > Export > PDF, 72 DPI (sufficient for screen delivery; the zone cards are screen/print documents, not high-production print)
6. Remaining zones: duplicate the Zone 5 frame in Figma, substitute content

**Figma learning curve estimate**: 60-90 minutes for someone new to Figma who is familiar with Canva. The core concepts (frames, text boxes, shapes, layers) are analogous.

---

### Recovery Option C: GIMP (Local, No Internet Required)

If both Canva and Figma are unavailable or internet access is limited:

1. Download GIMP (free, gimp.org) if not installed
2. File > New > 1200×900px, 150 DPI, RGB
3. Use GIMP's text tool to build the zone card text layout
4. Export as PDF: File > Export As > [filename].pdf
5. GIMP PDF export for zone cards: set quality to 90% or maximum

**GIMP note**: GIMP is more technically demanding than Canva or Figma for layout work. Budget an extra 60-90 minutes for the first card if using GIMP. The card will be functional but may not achieve the same visual polish.

---

### Recovery Option D: Text-Only PDF via Google Docs (1 hour)

If all design tools fail:

1. Open Google Docs > new document
2. Set page size: File > Page setup > Custom: 10 inches × 7.5 inches (landscape, approximating the zone card dimensions)
3. Use Docs' built-in formatting: Headers for section titles, tables for crop lists
4. Add Seedwarden branding via the document header (company name, hex color via text color picker)
5. File > Download > PDF Document
6. Upload to Google Drive, share link, load into Kit Email 1

**Visual quality**: Lower than Canva builds, but fully functional. The content (frost dates, crop lists, variety spotlights) is what subscribers signed up for — the visual polish is secondary to content delivery at launch.

---

## Scenario 4: Phase 1 Converts Slower Than Expected

**What triggers this**: After Phase 1 Etsy store has been live for 2+ weeks, data shows fewer than 5 sales and/or listing view-to-click rate is below 0.5%.

**Detection points**: Week 2 checkpoint (May 14), Week 4 checkpoint (May 30).

---

### Diagnosis Before Response

Low Phase 1 performance has two distinct causes with different responses:

**Cause A: Traffic problem (low views)** — Phase 1 listings exist but buyers are not finding them in Etsy search. Indicated by: Etsy shop views < 50/week.

**Cause B: Conversion problem (views but no sales)** — Buyers are visiting listings but not purchasing. Indicated by: Etsy shop views > 100/week but orders < 2.

---

### Response to Cause A: Traffic Problem

Phase 2 is the traffic solution. The zone card email funnel, social presence, and lifestyle photography all drive traffic to listings that already exist. Accelerate Phase 2 launch rather than delaying it.

If Phase 1 has low traffic AND Phase 2 is delayed: prioritize getting Kit automation live and social accounts active above all other Phase 2 tasks. Every day of list-building before the broadcast adds subscribers.

Specific actions:
- Ensure Kit landing page is live and linked from all 3 social bios immediately
- Run a Phase 1 Etsy SEO check: open the 3 highest-traffic listings and verify all 13 tags are filled, title includes the primary keyword in the first 3-5 words, and description opens with a buyer benefit statement (not a product description)

---

### Response to Cause B: Conversion Problem

Compression plan for Phase 2 — maintain May 30 launch but reduce scope:

| Phase 2 Element | Full Plan | Compressed Plan (Low Phase 1 Conversion) |
|---|---|---|
| Zone card count | 8 zones (all zones) | 4 zones (Zones 5, 6, 7, 8 — highest US traffic) |
| Lifestyle photo sessions | 3 clusters, 30 shots | 1 cluster (Cluster A only, 16 shots, 8 best-converting products) |
| Canva compositing | 21 products × 2 = 42 images | 8 products × 2 = 16 images (top 8 by Phase 1 views) |
| Pinterest pins | 15 pins | 6 pins |

**Which 8 products to prioritize for compressed plan**: Use Phase 1 Etsy view data. Take the 8 listings with the highest view counts — those are the products Etsy's algorithm is already surfacing. Upgrade those 8 first.

**Maintain May 30 launch**: Do not delay Phase 2 because Phase 1 is underperforming. The Phase 2 email funnel, lifestyle photography, and social presence are the mechanisms designed to address Phase 1 conversion issues. Delaying Phase 2 leaves the conversion problem unaddressed longer.

---

### If Phase 1 Has Zero Orders After 30+ Days

This is a significant signal that requires immediate investigation. Before Phase 2 launch:

1. Review all 21 listing titles for keyword clarity (does the title describe what the buyer receives in plain language?)
2. Review listing descriptions for the "what problem does this solve" statement in the first paragraph
3. Review price points against comparable Etsy digital goods ($4-8 is typically the low-friction price point for first-time Etsy digital product buyers)
4. Run a competitor check: what are the top-3 similar products showing in Etsy search for "seed saving guide" or "companion planting chart"? Are those listings doing things structurally that yours are not?
5. Consider a temporary price test: set one listing to $2.99 for 2 weeks to see if the conversion rate changes. If yes: pricing is the primary barrier, and the full catalog price should be reviewed before Phase 2 launch.

---

## Scenario 5: Social Account Creation Blocked or Handle Unavailable

**What triggers this**: The @seedwarden handle is taken on one or more platforms, or accounts are locked after creation due to age verification or policy review.

---

### Handle Unavailability

Use the documented fallback order: `@seedwarden.co`, then `@seedwarden.seeds`, then `@seedwarden_guides`.

**Cross-platform consistency rule**: Use the same handle root on all three platforms. If @seedwarden is taken on TikTok but available on Instagram and Pinterest, use @seedwarden.co on TikTok (rather than @seedwarden on Instagram and @seedwarden_guides on TikTok). Cross-platform consistency matters more than the exact primary handle.

**Record actual handles in WORKLOG.md**: note which fallback was used on which platform and why. Update social-media-setup.md with the confirmed handles.

---

### Account Locked After Creation

**Instagram**: Most common cause is automated fraud detection when a new account is created and immediately set up with a business profile, profile image, and bio within minutes. Recovery: confirm your identity via email verification or phone number in the Settings > Security menu. Typically resolves within 24 hours.

**TikTok**: Age verification occasionally triggers account holds. Recovery: submit ID verification in the TikTok app (Settings > Privacy > Account > Verify Identity). Resolution: 24-48 hours.

**Pinterest**: Rarely locked. If locked, email Pinterest support at help.pinterest.com. They respond within 48 hours.

**Priority during a platform lock**: Instagram and Pinterest account for the majority of Phase 2 social traffic for this audience type. If TikTok is locked, continue with Instagram and Pinterest — do not delay the entire Phase 2 launch for TikTok. Add TikTok when it resolves.

---

### If No Social Accounts Are Live by May 20

This is an unlikely worst case, but if it happens:
- Bio links from social accounts drive organic email sign-ups pre-launch
- Without any social accounts, the Kit landing page URL has no distribution channel before the broadcast
- The launch broadcast still goes to the existing subscriber list on May 30 — it functions without social distribution
- Phase 2 social launch becomes a post-broadcast activity: set up accounts May 20-28, post the launch content in the first week of June, and build the following from a smaller but real subscriber base

**Impact**: Lower subscriber count at broadcast (fewer pre-launch organic sign-ups). This affects the broadcast's absolute reach (20-30 subscribers instead of 50+) but does not affect the product, the email sequence, or the Etsy conversion potential.

---

## Quick Reference: Scenario Decision Tree

```
Photo shoot fails May 10-11?
  → Can it happen May 17-18?
      → YES: Activate June 6 path. Continue all other tracks unchanged.
      → NO (May 17-18 also unavailable): Use Cluster D+E stock compositing only.
         Launch May 30 with 5 stock-composited products + zone card email funnel.
         Physical shoot products launch June 13-20 as "Phase 2.1."

Kit account blocked?
  → Is it a 24-48h review? Wait and follow up.
  → Is it taking longer than 48h? Google Form fallback. Manual delivery.
  → Kit resolves: re-import subscribers into Kit.

Canva exports fail?
  → Browser/cache issue? Clear cache, try different browser.
  → Account issue? Contact Canva support.
  → Still blocked after 24h? Figma fallback (3-4 hrs to rebuild Zone 5 master).
  → Time critical (<24h to launch)? Google Docs text-only PDF (1 hr).

Phase 1 converting slowly?
  → Traffic problem (low views)? Accelerate Phase 2 — email funnel is the fix.
  → Conversion problem (views, no sales)? Compress Phase 2 to top 8 products.
  → Zero orders after 30 days? Price test before Phase 2 launch.

Social handle unavailable?
  → Use fallback: @seedwarden.co → @seedwarden.seeds → @seedwarden_guides
  → Same handle root on all platforms.
  → Record actual handles in WORKLOG.md.

Account locked?
  → Instagram: verify identity in Settings > Security.
  → TikTok: ID verification in-app.
  → Pinterest: email support.
  → Priority: Instagram + Pinterest first. TikTok can wait.
```

---

*Generated: 2026-05-06. References: june-6-contingency-path.md (photo delay recovery), TRACK_B_FINAL_EXECUTION_GUIDE.md Section 4 (risk table), phase-2-tool-integration-map.md (Kit and Buffer failure modes), phase-2-execution-timeline.md (Canva float analysis). Covers the five most probable failure modes by probability and impact.*
