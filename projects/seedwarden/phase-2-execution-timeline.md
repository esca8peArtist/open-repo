---
title: "Phase 2 Production Timeline & Dependency Map"
date: 2026-05-04
status: production-ready
context: Exploration Queue Item — critical path, dependencies, realistic May/June 2026 timeline
references:
  - LIFESTYLE_PHOTOGRAPHY_STRATEGY.md
  - PHOTO_SHOOT_SCHEDULE_AND_PROPS.md
  - CANVA_ZONE_CARD_DESIGN_GUIDE.md
  - ZONE_CARD_PRODUCTION_TIMELINE.md
  - PHASE_2_EMAIL_STRATEGY.md
  - PHASE_2_BUNDLE_STRATEGY.md
  - concurrent-track-execution-plan.md
---

# Phase 2 Production Timeline & Dependency Map

**Baseline assumption**: Phase 1 Etsy store launches May 2026. Phase 2 go-live target: May 30, 2026. Worst-case recovery: June 15, 2026.

Phase 2 has four parallel workstreams — lifestyle photography, Canva zone card production, Kit email platform setup, and social content preparation — that all converge at a single launch event on May 30. This document maps the execution sequence, names every hard dependency, quantifies realistic time investment per workstream, and models the critical path recovery if any single component slips.

---

## Photo Shoot Logistics

### Timing — May 10–11 Window

The photo shoot is scheduled as a two-day event: May 10 (Saturday) for Clusters A and B, May 11 (Sunday) for Cluster C. The two-day split is not preference — it is structural. Cluster A (seed and garden products, 8 products, 16 shots) requires morning window light between 9am and 2pm for consistent soft illumination. Compressing all three clusters into one day forces Cluster C into afternoon light or artificial light, which produces a visual inconsistency that is visible to buyers comparing listing images.

May was selected over June for one reason: germination timing. Two products in the catalog — the Zone-by-Zone Seed Starting Calendar and the Seed Saving Field Manual — are most effectively shot with live germination trays showing 7–13-day-old sprouts. A tray started April 30 produces shoot-ready sprouts by May 10. A June shoot date would require a second tray start in late May, adding a full month to the timeline with no benefit.

**If May 10–11 is unavailable**: The next workable window is May 17–18 (same structure). This pushes image processing to May 19–21, photo delivery to May 22, and the launch date from May 30 to June 6 — a 7-day slip with no compounding effect on revenue.

### Props List

Props are organized by the three shoot clusters. Most items are likely already on hand; sourcing should be completed by May 9.

**Cluster A — Seeds and Garden (Products 1–8)**
Seed envelopes (filled, closed), ceramic or terracotta pots (2–3 sizes), small trowel or hand rake, germination tray with 7–13-day sprouts, mason jar filled with saved seeds, printed color pages from 2–3 product PDFs, wooden surface or potting bench, linen fabric swatch for layering.

**Cluster B — Container and Urban Growing (Products 9–12)**
Potted herbs (basil, mint, or rosemary in a 4–6 inch container), small raised bed or balcony railing as background, compact grow light (if available), second printed product page or tablet showing a PDF cover.

**Cluster C — Food Preservation (Products 13–15)**
Mason jars with visible contents (fermented vegetables, dried herbs, or preserved fruit), canning pot or large stockpot, dehydrator tray with dried items, whole peppers or garlic as accent items, wood cutting board, kitchen counter as base surface.

**Print shop run** — required by May 8: 3–5 pages of color-printed product content for props (the product pages appear in frame as physical objects, not as a tablet screen). 24-hour turnaround minimum from a print shop or library.

**Props budget**: $40–80 for items not already on hand. CLUSTER_C_PROPS_ACQUISITION_PLAN.md documents specific sourcing options for Cluster C kitchen items.

### Location Options

No external location booking is required. All three clusters can be executed in a standard apartment or house with the following:

- Cluster A and B: east- or south-facing window with unobstructed morning light, May 10–11 between 9am and 1:30pm. A window that gets 3+ hours of direct or near-direct morning light is sufficient.
- Cluster C: kitchen counter near any window. Afternoon light is acceptable for this cluster.

**Outdoor option**: If an outdoor garden or balcony is available, Cluster A produces stronger images outside on an overcast day (overcast acts as a natural softbox). Direct sunlight creates harsh shadows and should be avoided for flat-lay shots.

### Shots Needed

Total: 30 RAW compositions, from which 30 final edited images are produced.

- Day 1, Session 1 (9am–1:30pm): Cluster A, 16 shots — 8 flat-lay compositions and 8 contextual/in-use compositions for the 8 seed and garden products
- Day 1, Session 2 (3pm–5pm): Cluster B, 8 shots — 4 flat-lay and 4 contextual for the 4 container and urban growing products
- Day 2, Session 3 (9am–11am): Cluster C, 6 shots — 3 flat-lay and 3 contextual for the 3 food preservation products

Each product needs two usable shots (Etsy slots 4 and 5). The flat-lay is shot directly overhead; the contextual shot shows the product in a use scenario (hands holding a page, guide open next to props, tablet propped on a surface).

---

## Canva Production Critical Path

### Which PDFs Need Variants

The zone quick-start cards are the primary Canva deliverable for Phase 2. Eight cards are required — one per USDA hardiness zone (3 through 10). Each card is a single-page PDF designed in Canva and exported for delivery via Kit.

Zones 5 and 6 are built first (Week 1, May 15–17) because they represent the largest US population concentration and establish the master template that all subsequent zones duplicate from. Zones 3, 4, 7, and 8 are built in Week 2 (May 18–24) via template duplication with zone-specific content substituted. Zones 9 and 10 are built last (May 25–27) as the lowest-traffic zones.

The only other Canva work in Phase 2 is the email header image for the Kit landing page — one image, added after Session 1 photos are available, approximately 30 minutes of work.

### Upload Sequence

1. Build Canva Brand Kit (Week 0 or May 15): Lock brand colors (Seedwarden palette) and fonts before building any card. This is a one-time setup that makes all future cards consistent without per-card design decisions.
2. Build master template on Zone 5 card (May 15–16): Three-column layout, spotlight band, footer with URLs. This is the most time-intensive card — budget 3–4 hours including iteration.
3. Duplicate master to Zone 6 (May 16–17): Substitute zone-specific content only. Verify color band. Export and test-open PDF.
4. Duplicate to Zones 3, 4, 7, 8 (May 18–24): ~60–90 minutes each. Color band and city reference are the primary per-zone changes.
5. Duplicate to Zones 9, 10 (May 25–27): Same process.
6. Full-set review (May 27–28): Visual QA all 8 cards. Confirm placeholder text has been replaced (especially footer URLs — Etsy store link and Kit landing page URL must be live before export).
7. Export all 8 as PDF Print quality and upload to Kit Content > Files (May 29). Log each download URL in WORKLOG.md immediately.

### Pricing Tiers to Set in Kit

The zone cards are a free lead magnet — no pricing is set on the cards themselves. However, the Kit setup must configure the following correctly before launch:

- Email 5 of the welcome sequence includes coupon code SEEDWARDEN15 (15% off) — this code must be active in Etsy before the first subscriber reaches Day 10 of the welcome sequence. Create the coupon in Etsy Shop Manager before the Kit automation goes live.
- Bundle pricing (from PHASE_2_BUNDLE_STRATEGY.md): Phase 2 introduces up to three new Etsy bundle listings. Bundle prices are set directly in Etsy, not in Kit. The email automation references bundle products by Etsy listing URL — confirm URLs before loading email copy into Kit.

---

## Email Platform Setup

### Kit Configuration Steps

Kit (formerly ConvertKit) is the selected platform. Free tier supports up to 10,000 subscribers with full automation and conditional routing — no cost through Phase 3 scale.

**Step 1 — Account and sender authentication (30 min)**: Create account at kit.com. Set From name to "Seedwarden." Set From email to a Seedwarden-branded address. Add SPF and DKIM DNS records to the domain registrar. Without authentication, welcome emails land in spam at a high rate. If a custom domain email does not exist yet, use a Gmail address temporarily and migrate before the list reaches 500 subscribers.

**Step 2 — Upload zone card PDFs (15 min)**: In Kit, navigate to Content > Files. Upload all 8 zone card PDFs in sequence. After each upload, copy the download URL into a local note labeled by zone number. Verify each URL in an incognito browser window before proceeding. These URLs are the primary CTA in Email 1 — a broken URL at this step breaks the entire lead magnet delivery.

**Step 3 — Build sign-up form with zone dropdown (20 min)**: New Form > Landing Page. Two required fields: First Name and Email. Add a required Growing Zone dropdown with values 3 through 10. CTA button text: "Send me my zone card." Publish and record the landing page URL — this URL goes in the Etsy shop bio, listing descriptions, and PDF end-pages.

**Step 4 — Load welcome sequence (60 min)**: New Sequence named "Seedwarden Welcome." Build 8 variants of Email 1 — identical body copy with the zone reference and download link substituted per zone. Build Emails 2–5 as single variants (zone-agnostic). Set delays: Email 1 immediate, Email 2 Day 2, Email 3 Day 5, Email 4 Day 7, Email 5 Day 10.

**Step 5 — Build welcome automation (10 min)**: Trigger: Form submitted. Actions: tag "new-subscriber," add to sequence, and apply conditional zone routing (if zone = X, send Email 1 variant X). Publish.

**Step 6 — End-to-end test (15 min)**: Submit form with test email address, Zone 5 selected. Confirm Email 1 arrives within 60 seconds. Open the download link — confirm Zone 5 PDF opens. Check that the email did not land in spam. Repeat for one additional zone (e.g., Zone 3). Do not publish the landing page URL anywhere until this test passes.

**Total Kit setup time**: 2.5 hours for a first-time user. 90 minutes for someone familiar with Kit.

### Subscriber Segmentation

Three behavioral segments are built through click-tracking in Emails 3 and 4 of the welcome sequence:

- "seed-saver": subscriber clicked the Seed Saving Field Manual link in Email 3 or the food sovereignty link in Email 4
- "city-grower": subscriber clicked the apartment/container link in Email 4
- "preservationist": subscriber clicked the preservation link in Email 4

Subscribers who click nothing are tagged "unclassified" and receive the general newsletter without segment-specific product spotlights until they reveal a preference through a purchase.

### 3-Email Welcome Automation Outline

The full 5-email welcome sequence is documented in `marketing/email-and-launch-plan.md`. The three most operationally important emails:

**Email 1 (immediate)**: Zone card delivery. The download link is the primary and largest element. Body copy is warm and brief — founder voice, not brand voice. Zone number is named explicitly in the subject line and opening sentence.

**Email 3 (Day 5)**: Seed saving mistake story. First behavioral tag link embedded. This email is the inflection point for list quality — subscribers who open and click here are the highest-intent segment. Open rate on Email 3 is the leading indicator for Email 5 coupon redemption.

**Email 5 (Day 10)**: First offer. SEEDWARDEN15 coupon, 5-day expiration (communicated in copy, not enforced by a timer). The offer is framed as a genuine gesture rather than a sales tactic — Seedwarden's audience is sophisticated about marketing manipulation, and countdown timer language will erode trust.

---

## Live Launch Coordination

Phase 2 launch is a coordinated event, not a gradual rollout. All four workstreams must be complete and staged before the launch sequence begins.

**Pre-launch staging (May 29)**:
- All 21 Etsy lifestyle images uploaded but not yet visible (Etsy listings updated with new images do not require re-publishing — images are live immediately on upload, so do the upload at a time when you are ready for it to go live)
- Social posts written and scheduled in Buffer or Later for May 30 2pm–4pm
- Email launch broadcast drafted and staged in Kit (not yet sent)
- Zone card delivery automation confirmed live and accepting subscribers

**Launch sequence — May 30**:
- 10:00am: Upload lifestyle images to all 21 Etsy listings (this is the de facto launch — listings are immediately visible to buyers with 5-image stacks)
- 12:00pm: Send launch email broadcast to full list via Kit. Confirm that the welcome automation is NOT paused during the broadcast send — new subscribers who sign up on launch day should still receive the welcome sequence, not the broadcast
- 2:00pm–4:00pm: Social posts go live, staggered by platform with a 2-hour gap between platforms to avoid same-audience reach overlap within one day

The 2-hour gap between Etsy update and email send is intentional: if a buyer discovers the store organically in the 10am–12pm window and purchases before the email goes out, they enter the post-purchase sequence before receiving the launch broadcast. This is correct behavior — do not suppress the post-purchase automation for launch-day buyers.

---

## Risk Dependencies and Critical Path Recovery

### Primary Risk: Photo Shoot Delayed 2 Weeks

**Scenario**: May 10–11 shoot is unavailable. Next window is May 17–18.

**Recovery sequence**:
- May 17–18: Shoot executes as planned (2 days, same structure)
- May 19–21: Image processing (culling, retouching, export)
- May 22: Photos available for email templates and social content
- May 22–28: Social content preparation, email template enrichment
- June 6: Phase 2 launch (7-day slip from May 30)

**What does not slip**: Canva zone card production and Kit email setup are completely independent of photography. Both can begin May 15 and complete by May 29 regardless of when the shoot happens. A 2-week photo delay does not cascade into the email funnel or zone card workstream.

**Revenue impact**: Zero. Phase 1 Etsy listings are generating sales throughout the slip period. Phase 2 launch email goes to the same list on June 6 rather than May 30. Subscriber count is marginally lower (6 fewer days of organic list-building) — the difference at this list size is single digits.

### Secondary Risk: Canva Zone Cards Run Over Estimate

**Scenario**: User is new to Canva Brand Kit — actual time is 2.5–3 hours per card instead of 90 minutes.

**Float available**: Zone card production has 2 days of float at the May 30 launch date. Even at 3 hours per card, all 8 cards are completable within the May 15–30 window with focused sessions.

**Minimum viable launch path**: If time pressure is acute, launch May 30 with 4 zone cards (Zones 5, 6, 7, 8 — the highest-traffic zones covering the majority of US buyers) and release Zones 3, 4, 9, 10 during the first week of June. Email automation delivers a "your zone is coming soon" placeholder for the four deferred zones, with a follow-up email sent when those cards go live.

### Worst-Case Stacked Scenario

Germination tray starts May 3 (not April 30), shoot pushes to May 17–18, processing runs May 19–23, and Canva work requires the full 18 hours at 2.5 hours per card. Latest realistic launch: **June 15**. This is a 2-week slip from May 30 and does not affect Phase 3 planning, which begins 30 days post-Phase-2-launch regardless of calendar date.

---

## Realistic Phase 2 Timeline

Assuming Phase 1 launches May 2026, the complete Phase 2 timeline from first action to first Phase 2 sale is:

| Date | Milestone |
|---|---|
| April 30 | Germination tray started; location and crew confirmed |
| May 7–9 | Props sourced; print shop run completed |
| May 10–11 | Photo shoot: 30 RAW images captured across all 3 clusters |
| May 12 | Image culling: 80–100 RAW files narrowed to 30 selects |
| May 13–14 | Retouching and export: 30 finals + 60 social variant crops |
| May 15 | Photos available; Kit account setup begins; Canva Brand Kit locked |
| May 15–17 | Canva master template built; Zones 5 and 6 complete |
| May 15–16 | Kit sender authentication; sign-up form built and published |
| May 17–19 | Kit welcome sequence loaded; automation built and tested |
| May 18–24 | Canva Zones 3, 4, 7, 8 built |
| May 20–24 | Post-purchase automation built; email template design; test sends |
| May 25 | Email automation live and accepting subscribers |
| May 25–27 | Canva Zones 9, 10 built |
| May 27–28 | Zone card full-set QA review; footer URL replacement |
| May 28–29 | Zone cards exported and uploaded to Kit; social posts scheduled |
| May 30 | Phase 2 live launch: 21 listings at 5-image status, email broadcast sent, social posts live |
| June 1–14 | First Phase 2 sales recorded; welcome sequence running for new subscribers |

**First Phase 2 sale**: expected within 72 hours of launch email send, based on email 5 coupon redemption targeting 8–15% of list. At 50 subscribers on launch day and an 8% redemption rate, 4 coupon purchases are projected in the first 5-day window.

**User time investment**: 36–45 hours across May 7–30, averaging 1.5–2 hours per day. The two largest continuous blocks are Canva zone card production (9–11 hours, May 15–29) and Kit setup plus email automation (7–8 hours, May 15–25). Both fall in the same window and can be split across evenings and a single weekend.

---

*Generated: 2026-05-04. Source documents: LIFESTYLE_PHOTOGRAPHY_STRATEGY.md, PHASE_2_EMAIL_STRATEGY.md, ZONE_CARD_PRODUCTION_TIMELINE.md, PHASE_2_BUNDLE_STRATEGY.md, concurrent-track-execution-plan.md. Dependency graph: phase-2-dependency-graph.csv.*
