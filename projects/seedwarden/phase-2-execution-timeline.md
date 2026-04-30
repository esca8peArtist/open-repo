---
title: "Phase 2 Production Timeline & Dependency Map"
date: 2026-04-30
status: planning-complete
context: Exploration Queue Item 35 — critical path, dependencies, realistic May/June 2026 timeline
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
## Critical Path, Sequencing Logic, and May 30 Launch Readiness

**Purpose**: Phase 2 production documents are complete across all four workstreams (lifestyle photography strategy, Canva zone card design guide, email strategy, bundle strategy). What was missing is a single document that maps the execution sequence, names every dependency, quantifies realistic time investment, and surfaces the decisions the user must confirm today. This document answers: in what order does everything happen, what blocks what, and what is the honest worst-case launch date if any component slips?

---

## Section 1: Critical Path Analysis

The critical path is the longest chain of dependent tasks. Any delay on the critical path delays the launch date. Tasks off the critical path have slack — they can slip without moving the May 30 launch date, as long as they resolve before their downstream dependent task begins.

### Critical Path (Must Not Slip)

**Node 1 — Germination tray start: April 30**

This is the single action that locks or unlocks the May 10 shoot date. Sprouts for Products 5 (Zone-by-Zone Seed Starting Calendar) and 7 (Seed Saving Field Manual) need 5–10 days of germination time. A germination tray started April 30 produces 5–7-day-old sprouts by May 5–7, and 10–13-day-old sprouts by May 10–13 — both within the usable photogenic window. A tray started May 1 is still workable for May 10 (9-day sprouts). A tray started May 3 or later raises the risk of shoots being too young or too leggy by the shoot date. This is a 15-minute task. It has no upstream dependencies. The only risk is not doing it today.

**Node 2 — Props sourcing and assembly: May 7–9**

The props list is documented in full in PHOTO_SHOOT_SCHEDULE_AND_PROPS.md. Sourcing is not a single-trip purchase — it is a 2–3 day window to gather items that may come from multiple places (garden shed, grocery store, hardware store, print shop). The three items that require lead time are (1) printed PDF pages for the shoot (color printing at a library or print shop — 24-hour minimum), (2) seed envelopes if not already on hand, and (3) any ceramic or terracotta pots that need to be sourced rather than grabbed from existing stock. Props assembly completed by end of May 9 means Day 1 setup on May 10 begins without scramble.

Budget: $40–80 for props that are not already on hand. The CLUSTER_C_PROPS_ACQUISITION_PLAN.md documents specific sourcing options for the Cluster C kitchen props.

**Node 3 — Photo shoot: May 10–11**

Two-day schedule per PHOTO_SHOOT_SCHEDULE_AND_PROPS.md. Day 1 (May 10): Cluster A (Products 1–8, 16 shots, 4.5–5 hours) + Cluster B (Products 9–12, 8 shots, 2 hours). Day 2 (May 11): Cluster C (Products 13–15, 6 shots, 1.5–2 hours). Total yield: 30 RAW images. Shoot day is entirely dependent on Nodes 1 and 2 — germination tray sprouts present and props assembled. Location confirmation and crew coordination (below) are parallel pre-conditions, not serial ones.

Critical shoot-day constraint: Cluster A requires morning window light (9am–2pm). The two-day format produces better Cluster A images than a single-day marathon. If the shoot is compressed to one day, Cluster C quality degrades because it happens in afternoon light or artificial light rather than morning light. For product images that will live on Etsy listings for 12–18 months, the two-day format is worth the additional planning.

**Node 4 — Image processing: May 12–14**

Three days of processing follow the shoot. Day 1 (May 12): culling — editing 80–100 RAW captures down to 30 selects. Day 2–3 (May 13–14): retouching and color grading — apply Lightroom presets from LIFESTYLE_PHOTOGRAPHY_STRATEGY.md Section 2, batch-process by cluster, then generate 60 variant crops at different aspect ratios for social content (1:1 Etsy, 4:5 Instagram, 16:9 Pinterest/Story). Deliverable: 30 final Etsy-ready images + 60 social variant crops, all exported at 2400px JPEG 90%, saved to `/projects/seedwarden/marketing/lifestyle-photos/etsy-ready/`.

**Node 5 — Photo funnel live: May 15**

The email funnel does not require photos to launch (PHASE_2_EMAIL_STRATEGY.md confirms this explicitly — zone cards, not photos, are the functional lead magnet). However, May 15 is when photos become available for email template enrichment and social posting. The photo funnel going live on May 15 means the Week 3–6 newsletter releases can use lifestyle images rather than mockups, which increases click-through rate in those sends. This node is a dependency for email automation setup being visually complete, not for it being functionally live.

**Node 6 — Live launch: May 30**

All four Phase 2 workstreams converge here: (a) Canva zone cards complete and uploaded to Kit delivery, (b) email automation live and tested, (c) social content queue scheduled, (d) Etsy lifestyle images uploaded to all 21 listings. Launch is coordinated: Etsy listing updates first (no announcement), then email campaign trigger, then social posting staggered by 2–4 hours to prevent reach overlap on the same platform within the same day.

### Parallel Pre-Conditions (Not on the Critical Path, But Must Resolve Before Node 3)

**Location confirmation** needs to happen by April 30 — same day as germination. The shoot location (window light source for Cluster A, window sill or balcony for Cluster B, kitchen counter for Cluster C) must be confirmed as accessible and unobstructed for both May 10 and May 11 mornings. This is a 5-minute confirmation call or walk-through, not a booking process. It is listed as a separate node in the dependency graph because overlooking it has caused more last-minute shoot scrambles than any other single factor.

**Crew coordination** for the May 10–11 shoot was noted as confirmed in the session 702 production log. The PHOTO_SHOOT_SCHEDULE_AND_PROPS.md assumes a 2–3 person team. If crew availability changes before May 10, the solo-with-tripod contingency extends the shoot timeline by approximately 20% (adding 45–60 minutes to Day 1 for self-timer repositioning) and requires bracketed composition changes — wider framing to allow crop adjustment rather than relying on a second person to hold or angle props.

---

## Section 2: Timeline Gantt Chart

The following chart maps all 12 tasks across the April 30 – May 30 production window. Tasks on the critical path are marked [CP]. Tasks with float (slack) are marked [F x days] indicating how many days they can slip without affecting the May 30 launch.

```
APRIL 30
  [CP] Germination tray start ─────────────────────────── sprouts ready May 10
  [F 0] Location confirmation ─ done today
  [F 0] Crew coordination ─ confirmed (session 702)

MAY 1–6
  [F 3] Props sourcing begins (ongoing as items identified)

MAY 7–9
  [CP] Props sourcing & assembly ──────────── shoot-ready by May 9 EOD
         └── print shop run by May 8 (24-hr turnaround for printed PDFs)
         └── grocery/garden sourcing by May 9

MAY 10 (Saturday)
  [CP] Photo shoot Day 1 ──────────────────── 9am–5pm
         Session 1: Cluster A (9am–1:30pm, 16 shots)
         Session 2: Cluster B (3pm–5pm, 8 shots)

MAY 11 (Sunday)
  [CP] Photo shoot Day 2 ──────────────────── morning
         Session 3: Cluster C (9am–11am, 6 shots)

MAY 12
  [CP] Image culling ──────────────────────── 80 RAW → 30 selects

MAY 13–14
  [CP] Retouching + color grading ─────────── 30 finals + 60 social variants

MAY 15
  [CP] Photo funnel live ─ images available for email templates + social queue

MAY 15–25 (parallel workstream, [F 5 days])
  [F 5] Email automation setup ────────────── Kit configured, sequences live, test sends complete
         └── Subscriber segmentation rules
         └── Welcome sequence + zone card delivery automation
         └── Post-purchase sequence
         └── Template design (can use Kit pre-built templates to save ~4 hrs)
         └── Test sends (3 test subscriber accounts minimum)

MAY 15–30 (parallel workstream, [F 0 at May 30])
  [CP after May 28] Canva zone card production ───────── 8 cards complete
         └── Week 1 (May 15–17): Brand Kit setup + master template + Zones 5–6 (4 hrs)
         └── Week 2 (May 18–24): Zones 3, 4, 7, 8 (4 hrs @ 60 min each)
         └── Week 3 (May 25–29): Zones 9, 10 + full-set review + placeholder URL replacement (3 hrs)
         └── Week 4 (May 30): Final export + Kit upload + delivery test (1 hr)

MAY 20–29 (parallel workstream, [F 1 day])
  [F 1] Social content preparation ────────── posts scheduled for May 30+
         └── 30 lifestyle images → select 10 best for launch week social
         └── Write captions (5 Instagram, 3 Pinterest, 2 Facebook)
         └── Schedule in Buffer/Later for May 30 + 3 days post-launch

MAY 30 — PHASE 2 LIVE LAUNCH
  10:00am: Etsy lifestyle image upload (all 21 listings updated)
  12:00pm: Email campaign trigger (Kit sends launch email to full list)
  2:00pm–4:00pm: Social posts go live (staggered across platforms)
```

---

## Section 3: Dependency Graph

The following dependency map uses indentation to show which tasks unlock which downstream tasks. A task at any level cannot begin until all items at the level above it in its chain are complete.

```
CRITICAL PATH:

germination tray start (Apr 30)
  └── sprouts present (May 10)
        └── photo shoot Day 1 (May 10)
              ├── [also requires] props assembled (May 9)
              ├── [also requires] location confirmed (Apr 30)
              └── [also requires] crew confirmed (done)
                    └── photo shoot Day 2 (May 11)
                          └── image culling (May 12)
                                └── retouching + color grading (May 13–14)
                                      ├── photo funnel live (May 15)
                                      │     └── email template enrichment (May 15+)
                                      │
                                      └── social content preparation (May 20–29)
                                            └── social posts scheduled (May 29)

PARALLEL PATH A (email automation — floats to May 25):

Kit account configuration (May 15)
  └── subscriber segmentation rules (May 15–16)
        └── automation sequences built (May 17–20)
              └── template design (May 20–22)
                    └── test sends (May 22–24)
                          └── email automation live (May 25)

PARALLEL PATH B (Canva zone cards — floats to May 28):

Brand Kit setup (May 15, 30 min)
  └── master template + Zones 5–6 (May 15–17)
        └── Zones 3, 4, 7, 8 (May 18–24)
              └── Zones 9, 10 (May 25–27)
                    └── full-set review + URL replacement (May 27–29)
                          └── final export + Kit upload + delivery test (May 29–30)

CONVERGENCE AT LAUNCH:

[email automation live] + [zone cards in Kit] + [social posts scheduled] + [Etsy images uploaded]
  └── PHASE 2 LIVE LAUNCH (May 30)
```

---

## Section 4: Slack and Risk Mitigation

### Risk 1 — Germination tray not started today

**Trigger condition**: User does not start the germination tray on April 30 or May 1.

**Impact assessment**: A May 3 start gives 7-day sprouts by May 10 — technically in range but on the younger end of the photogenic window. A May 5 start gives 5-day sprouts by May 10, which are borderline for visual interest (seedlings are very small, difficult to compose around). A May 7 start requires pushing the shoot to May 17–18.

**Mitigation options**:
- Option A: Start tray today (April 30) or May 1. Zero-cost fix.
- Option B: Use grocery-store bean sprout or microgreen trays as a prop substitute for the germination scene. Quality degradation: 40% (the visual variety is narrower, and microgreens don't have the "germination in progress" look the guide references). Still usable for Etsy.
- Option C: Use stock photography for the 2 products that feature sprouts specifically (Seed Starting Calendar, Seed Saving Field Manual). Full-quality alternative but loses the brand authenticity of real props.

**Launch impact**: If May 17–18 shoot, launch pushes to June 6. The Week 1 email funnel runs June 6–12 instead of May 30 – June 5. No revenue impact — email list is pre-launch and doesn't depend on a specific calendar date.

### Risk 2 — Photo shoot rescheduled (weather, crew, personal conflict)

**Trigger condition**: May 10–11 window is unavailable.

**Next available window**: May 17–18 (same weekend structure). This pushes processing to May 19–21, photo funnel to May 22, and launch to June 6.

**Impact assessment**: 7-day slip. No compounding effect on revenue — Etsy listings without lifestyle photos still generate sales during the slip period. The launch week social push simply happens June 6 rather than May 30.

**Mitigation**: Confirm crew availability for both May 10–11 AND May 17–18 as backup. If both windows are unavailable, a solo shoot with tripod can happen any morning with good window light. Solo adds approximately 60 minutes to the total shoot time.

### Risk 3 — Image processing bottleneck

**Trigger condition**: User lacks time for 3-day editing window (May 12–14) or Lightroom/editing competency introduces quality issues.

**Mitigation options**:
- Option A: Outsource batch retouching to Fiverr. Cost: $150–250 for 30 images with color grading and crop variants. Turnaround: 48–72 hours from file delivery. Send files May 12 morning, receive May 14 afternoon. Timeline holds.
- Option B: Use Canva's built-in photo editing for color grading (free, less precise than Lightroom but sufficient for Etsy quality). Time savings: 2–3 hours vs. Lightroom preset workflow.
- Option C: Skip variant crops (60 social variants) in the first pass and add them in the week following launch. Etsy images are the priority; social variants can be generated from final Etsy images at any point.

**Budget impact**: Fiverr retouching adds $150–250 to the $200–300 props estimate, bringing Phase 2 production total to $350–550. Still well within range for a digital products business with 21 Etsy listings.

### Risk 4 — Canva zone card production runs over 12 hours

**Trigger condition**: User's Canva familiarity is lower than 90-minute-per-card estimate, or design iterations add time.

**Assessment**: The 90-minute estimate is for an experienced Canva user following the CANVA_ZONE_CARD_DESIGN_GUIDE.md step-by-step. A user new to Canva's Brand Kit and template duplication workflow should budget 2.5–3 hours per card for the first 2 cards, dropping to 75–90 minutes by cards 5–8 as the duplication pattern becomes automatic. This adds 2–4 hours to the total production estimate, which is fully absorbed by the May 15–30 float window.

**Mitigation options**:
- Option A: Spend 2 hours in Week 0 (before May 15) setting up Brand Kit and building the master template. This is front-loaded time that eliminates per-card design decisions.
- Option B: Simplify designs for Zones 9 and 10 (the lowest-traffic zones) using direct template duplication with color-only changes. Saves 1–1.5 hours.
- Option C: Build only the 4 highest-traffic zone cards by May 30 (Zones 5, 6, 7, 8 — the continental mid-range zones that cover the majority of the US population) and release Zones 3, 4, 9, 10 in the first week of June. This reduces the zone card deliverable to 4 cards at launch with a June 7 full release. Email automation can deliver zone-specific cards only if the user's zone is one of the 4 live; otherwise deliver a "coming soon" zone card placeholder.

### Risk 5 — Email automation setup takes longer than estimated

**Trigger condition**: Kit UI unfamiliarity, automation logic errors, or deliverability issues extend setup beyond the May 15–25 window.

**Mitigation options**:
- Option A: Use Kit's pre-built welcome sequence template and modify copy rather than building from scratch. Saves 3–4 hours. The full custom email copy lives in `marketing/email-and-launch-plan.md` — this copy can be pasted directly into the pre-built template structure.
- Option B: Launch with only Priority 1 (Welcome Sequence) and Priority 2 (Post-Purchase Sequence) automations live. The weekly newsletter and win-back campaign can be configured post-launch during the first two weeks of June without any customer impact.
- Option C: If Kit setup is genuinely blocked (account issue, payment issue, deliverability hold), launch Phase 2 with Mailchimp free tier as a temporary bridge. The email copy is platform-agnostic. Migrate to Kit when the account issue resolves.

### Worst-Case Stacked Delay Scenario

If germination misses (tray starts May 3), shoot pushes to May 17–18, processing runs May 19–23, and Canva cards need the full 15 hours (not 12), the latest realistic launch date is June 15. This represents a 2-week slip from May 30 and a 3-week slip from the original goal. June 15 is still well within the Phase 2 production window and does not affect Phase 3 planning, which begins 30 days post-Phase-2-launch regardless of calendar date.

---

## Section 5: Resource Requirements

### User Time Investment

| Task | Estimated Hours | Window |
|---|---|---|
| Germination tray start | 0.25 | April 30 |
| Location confirmation | 0.1 | April 30 |
| Props sourcing + print run | 2–3 | May 7–9 |
| Props assembly + shoot prep | 1 | May 9 evening |
| Photo shoot (2 days) | 8–10 | May 10–11 |
| Image culling | 1.5 | May 12 |
| Image retouching + export (self) | 3–4 | May 13–14 |
| Canva Brand Kit + master template | 2 | May 15–17 |
| Canva zone cards 3–10 (6 remaining) | 7–9 | May 18–29 |
| Kit account setup + segmentation | 2 | May 15–16 |
| Email automation sequences | 3–4 | May 17–20 |
| Email template design + test sends | 2 | May 22–24 |
| Social content preparation | 2–3 | May 20–28 |
| Etsy lifestyle image upload (21 listings) | 1.5 | May 30 |
| Launch coordination (email trigger, social) | 1 | May 30 |
| **Total** | **36–45 hours** | May 7–30 |

Note: 36–45 hours over 24 calendar days (May 7–30) averages 1.5–2 hours per day. This is achievable on weekday evenings + weekends if the user can protect morning time on May 10–11 for the shoot itself. The Canva work (9–11 hours) and Kit setup (7–8 hours) are the largest continuous blocks and both fall in the May 15–30 window — a period with no other hard deadlines.

If image processing is outsourced to Fiverr, the user's total personal time investment drops to 25–32 hours.

### External Resources

| Item | Cost | When Needed | Notes |
|---|---|---|---|
| Fiverr batch retouching (optional) | $150–250 | May 12 (file delivery) | 30 images + 60 crops; 48-hr turnaround |
| Props (seeds, pots, jars, linen, peppers) | $40–80 | May 7–9 | Most may be on hand; CLUSTER_C_PROPS_ACQUISITION_PLAN.md has sourcing detail |
| Print shop run (PDF pages for props) | $8–15 | May 8 (24-hr turnaround) | Color prints, 3–5 pages per product cluster |
| Kit account (free tier) | $0 | May 15 | Free tier supports list-building + welcome sequence; upgrade if list exceeds 1,000 |
| Canva Pro (if not active) | $13/month | May 15 | Required for Brand Kit feature; 30-day free trial available |
| **Total** | **$200–360** | | Without Fiverr: $50–100. With Fiverr: $200–360. |

### Equipment (Existing)

All the following are assumed to already be available per the photography strategy documents:

- Camera or smartphone with manual exposure capability
- Lightroom Mobile, Snapseed, or RawTherapee (free tiers sufficient)
- Canva account (Pro preferred, free tier workable)
- Window with good morning light on May 10 (east or south-facing window)
- Kitchen counter space for Cluster C

No new equipment purchases are required or recommended for the shoot. A $40–60 LED softbox is documented as optional in the budget allocation (LIFESTYLE_PHOTOGRAPHY_STRATEGY.md) but is specifically flagged as skip-if-window-light-is-adequate.

---

## Section 6: Five Key Questions for User Confirmation

These questions require a confirmed answer before any production planning is treated as locked. Each maps to a specific critical path node.

**Question 1 — Germination tray: Was it started today (April 30)?**

If yes: May 10 shoot is confirmed on the critical path. Node 1 is complete.
If no: Start tonight or first thing tomorrow (May 1) — still workable. Starting May 3 or later introduces shoot risk. This question must be answered before the week ends.

**Question 2 — User availability: Can 20–25 hours be dedicated May 15–30?**

If yes at full 25 hours: All workstreams (Canva, Kit, social) proceed at the pace documented above.
If only 15 hours available: Prioritize Kit automation first (email list is the highest-leverage Phase 2 asset), then Canva cards (lead magnet quality), then social. Outsource retouching to Fiverr to reclaim 3–4 hours from the May 12–14 window.
If under 10 hours available: Focus May 15–30 entirely on Kit automation and 4 zone cards. Defer the remaining 4 zone cards and social scheduling to June 1–15. Launch May 30 with partial Canva set.

**Question 3 — Track A parallel operation: Is Phase 1 Etsy upload happening simultaneously?**

If Track A is proceeding concurrently (per the concurrent-track-execution-plan.md Option D recommendation): Add 2.5–3 hours of Track A upload work to the May 7–20 window. This is not on the Phase 2 critical path but does compete for user time. The Track A upload is documented as approximately 45–60 minutes per day for 3 days — low enough to run in parallel with Phase 2 without significant conflict.
If Track A is deferred until after Phase 2 launch: Phase 2 proceeds unencumbered. Phase 1 Etsy listings do not yet have lifestyle images, which may affect first-impression conversion on those listings. Acceptable trade-off given Phase 2 is the priority.
If Track A is blocked (account hold, payment setup issue): Phase 2 is completely independent and proceeds on schedule regardless.

**Question 4 — Canva skill level: Experienced or novice?**

Experienced (uses Canva regularly, comfortable with layers and text boxes): 90-minute-per-card estimate holds. 12-hour total for 8 cards is realistic in the May 15–30 window.
Intermediate (uses Canva occasionally): Budget 2 hours per card, 16 hours total. Still achievable in the May 15–30 window with focused sessions. The CANVA_ZONE_CARD_DESIGN_GUIDE.md step-by-step build reference is specifically written to reduce guesswork during the session.
Novice (minimal Canva experience): Budget 2.5–3 hours per card for the first two, dropping to 90 minutes by card 4+. Consider watching one Canva Brand Kit tutorial video (20 min) before Week 0 setup. Full 8-card set is still achievable by May 30 with two 4-hour weekend sessions.

**Question 5 — Crew availability: Is the May 10–11 crew confirmed?**

If crew confirmed for both days: Schedule stands as documented. Proceed.
If crew confirmed for May 10 only: Cluster C (May 11) becomes a solo shoot. Cluster C is a kitchen counter shoot — the easiest of the three clusters for solo execution. No material quality impact.
If crew is unavailable for both days: Solo shoot with tripod for all 30 images. Add 60 minutes to Day 1 and 30 minutes to Day 2. Switch to a slightly wider framing convention for all shots. Still fully achievable — the PHOTO_SHOOT_CHECKLIST.md solo-shoot notes cover this case.
If crew confirmed for May 10–11 but cancels within 72 hours: Execute solo shoot or push to May 17–18 and source replacement crew from local photographer community (Facebook groups, photography school alumni networks).

---

## Section 7: Phase 2 and Phase 1 Integration

Phase 2 Track B can and should proceed independently of Phase 1 Track A. The dependency relationship runs one direction only: Phase 1 Etsy listings benefit from Phase 2 lifestyle images (added to slots 4–5), but Phase 2 production does not need Phase 1 to be live before beginning.

The two workstreams share the user's time, not each other's assets. The concurrent-track-execution-plan.md documents this explicitly. The practical implication for May 2026:

- Etsy account setup and Phase 1 listing uploads can happen during the same week as props sourcing (May 7–9) without conflict — they use different hours and different platforms.
- Phase 2 lifestyle images, once produced on May 12–14, can immediately be used to upgrade Phase 1 listings if those listings are already live. If Phase 1 has not yet launched, the images are staged in the etsy-ready folder and uploaded the moment Phase 1 listings go live.
- The email automation setup (Kit, May 15–25) benefits from Phase 1 being live because the post-purchase sequence requires confirmed Etsy purchase events to trigger correctly. If Phase 1 is not live by May 15, configure the welcome sequence and lead magnet delivery first; wire the post-purchase automation after Phase 1 launch.

**Phase 2 is not waiting on Phase 1. Start Phase 2 production today.**
