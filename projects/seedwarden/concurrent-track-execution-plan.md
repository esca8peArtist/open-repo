---
title: "Seedwarden Concurrent Track Execution Plan"
subtitle: "Resource Allocation, Dependency Chain, and Critical Path for Track A + Track B Simultaneous Operation"
prepared: 2026-04-29
status: active — contingency plan, ready to execute
scope: Track A (Phase 1 Etsy upload) + Track B (social media / lifestyle photography) running simultaneously
cross-references:
  - phase-1-contingency-decision-tree.md (option selection)
  - track-b-independent-launch-roadmap.md (Track B standalone detail)
  - UPLOAD_READY_CHECKLIST.md (Track A upload steps)
  - phase-2-social-content-calendar-60day.md (Track B content calendar)
  - financial-sustainability-model.md (revenue impact by scenario)
---

# Concurrent Track Execution Plan

**Purpose**: This document answers a single operational question: if Track A (Phase 1 Etsy upload) and Track B (social media launch + lifestyle photography) are both running simultaneously, what does that look like in practice? How much time does each track require? Which tasks depend on which? What gets cut if resources are limited?

This is a planning document, not a strategy document. The strategic rationale for concurrent execution is in phase-1-contingency-decision-tree.md (Option D recommendation). This document is the operational manual for executing that choice.

---

## Part 1: Track Definitions and Asset Status

Before scheduling anything, confirm what each track actually requires.

### Track A: Phase 1 Etsy Upload

**Goal**: 6 products live on Etsy, shop publicly active, download delivery confirmed.

**Asset status**: Complete. No production work required.

**Remaining user actions only**:

| Action | Time Required | Dependency |
|--------|--------------|------------|
| One-time shop setup (banner, announcement, policies) | 30-45 minutes | Etsy account active |
| Upload listing 1 — Companion Planting Chart | 15-20 minutes | Shop setup complete |
| Upload listing 2 — Food Sovereignty Starter Guide | 15-20 minutes | Listing 1 complete |
| Upload listing 3 — Anti-Catalog: 30 Heirlooms | 15-20 minutes | None (parallel to Listing 2) |
| Upload listing 4 — Seed Saving Field Manual | 15-20 minutes | None |
| Upload listing 5 — Apartment Plant Catalog | 15-20 minutes | None |
| Upload listing 6 — Survival Garden Regional Plans | 15-20 minutes | None |
| Test purchase one listing, verify download | 15 minutes | At least 1 listing live |
| Switch shop from private to public | 5 minutes | All 6 listings created |

**Total Track A time**: Approximately 2.5-3 hours, spread across 3 days at 45-60 minutes per day.

**Critical pre-condition**: Etsy seller account must be active with Payments enabled and no holds. This is a binary gate — either the account is usable or it is not. All other Track A tasks are blocked until this is confirmed.

**Tag reference**: Use UPLOAD_READY_CHECKLIST.md Section 4 for all three corrected tag sets. Have this file open during listing creation. Do not use raw tags from etsy-store-copy.md.

### Track B: Social Media + Photography

**Goal**: Active social presence on Instagram, Pinterest, and TikTok with consistent educational content; lifestyle photography for Tier 1 products either sourced or contracted.

**Asset status**: Partial. The content calendar, pin templates, platform specs, and brand kit are complete. Photography is not complete (that is the Track B production task). However, the first 2-3 weeks of Track B content can run on existing mockup images before lifestyle photos are required.

**Track B sub-components**:

**B1 — Account setup** (one-time, 1-2 hours):
- Create or verify Instagram Business account (handle: seedwarden)
- Create or verify TikTok Business account (same handle)
- Create or verify Pinterest Business account (same handle)
- Set up link-in-bio tool (Later, Linktree, or direct Etsy link)
- Upload profile image (seedwarden_logo_1.png) to all three accounts
- Write and publish bio text including Etsy shop link (or "opening soon" if shop not yet live)

**B2 — Canva template build** (2-4 hours, one-time):
- Set up Brand Kit per CANVA_EXECUTION_PLAYBOOK.md Section 1.2
- Build 5 pin templates per pin-template-specs.md
- Create first week of carousel slides (Day 3 post in 60-Day Calendar)
- Build product pin for each of the 6 Phase 1 products using existing mockup images

**B3 — Content production: Week 1** (2-3 hours per week):
- Script and record Day 1 Reel (hook: "I started a seed shop because I got mad about something")
- Produce Day 3 Carousel (5 slides: 5 products, lifestyle intro)
- Batch-produce 5-7 Pinterest pins for Tier 1 products
- Write captions for all Week 1 posts

**B4 — Lifestyle photography (Tier 1, stock approach)** (3-5 hours, one-time):
- Source 4-6 stock lifestyle images from Unsplash/Pexels for Cluster D/E products
- Alternatively, DIY flat-lay shoot for 2-3 Tier 1 products (Survival Garden, Harvest Preservation, Hunting Manual) using existing props documentation in PHOTOGRAPHY_ROADMAP.md
- Edit and export at 2400x2400px
- Upload to Etsy slots 4-5 for Tier 1 listings

**B5 — Ongoing content cadence** (1.5-2 hours per day):
- Post 1 Instagram Reel or Carousel per day
- Post TikTok native upload (same video, separate upload)
- Publish 5-7 Pinterest pins
- Post 3-5 Instagram Stories

---

## Part 2: Dependency Chain

The following map shows which tasks block which others. Tasks with no dependencies can start immediately regardless of other track status.

```
TRACK A DEPENDENCY CHAIN:
[Etsy account active] → [Shop setup] → [Listing 1] → [Listing 2-6] → [Test purchase] → [Go public]
                                                       (parallel, no sequence required between 2-6)

TRACK B DEPENDENCY CHAIN:
[Account setup (B1)] → [Canva templates (B2)] → [Week 1 content (B3)] → [Ongoing cadence (B5)]
                                                                         ↑
[Lifestyle photography (B4)] ----------------------------------------- |
(B4 feeds into B5 from Week 3 onward; not required for Weeks 1-2)

CROSS-TRACK DEPENDENCIES:
Track B can begin without Track A being live.
Track B is strengthened (higher conversion) when Track A is live.
Track A is not blocked by Track B.
The two tracks share the user's time — no shared files or systems.
```

**Key insight from the dependency chain**: Track B has only one genuine dependency on Track A — the Etsy shop link that goes in the social bio and is referenced in CTAs. If the shop is not live when Track B launches, the CTA becomes "join the email list / opening soon" instead of "shop now." This is a real cost (email signups convert lower than direct Etsy clicks), but it is not a reason to hold Track B entirely. See track-b-independent-launch-roadmap.md for how to frame Track B without a live shop.

---

## Part 3: Critical Path Analysis

The critical path is the sequence of tasks that determines when Seedwarden first generates revenue. Every task on the critical path must complete before revenue begins. Tasks off the critical path can slip without affecting the revenue start date.

**Critical path to first Etsy sale**:

1. Etsy account active and verified (user action, no ETA)
2. Shop setup complete (30-45 minutes, must follow #1)
3. Listing 1 (Companion Planting Chart) created and published (15-20 minutes, must follow #2)
4. Shop switched from private to public (5 minutes, can follow any single listing)

Earliest possible first sale: same day as shop setup if listing is published and shop is public.

**Track B is not on this critical path.** Social media activity may accelerate the first sale by driving traffic, but a sale can happen from Etsy organic search alone within the first week for a well-tagged listing. Track B shifts the probability distribution earlier but is not required for the critical path.

**What is NOT on the critical path**:
- Lifestyle photography (it is a conversion rate improvement, not a prerequisite)
- Additional mockup variants (phone mockups, interior mockups)
- Bundle listings (can be added after individual listings are live)
- Any Pinterest pin batch (pins take 7-30 days to generate traffic organically; they are not same-day revenue drivers)
- Email list setup (email captures warm audiences but does not drive immediate sales from cold traffic)

**Implication**: The fastest path to first revenue is Track A alone, executed in a single focused 45-minute session (shop setup + one listing). Everything else builds on top of that foundation.

---

## Part 4: Resource Allocation

Assume limited time availability. The following allocations are modeled for three levels of weekly availability.

### Scenario 1: 3 Hours Per Week Available

This is a minimal operation. Revenue generation is possible. Growth is slow.

**Allocation**:
- Track A: 2 hours in Week 1 to complete all 6 listings. Zero Track A time in subsequent weeks unless adding Phase 2 products.
- Track B: 1 hour per week. Use this time for Pinterest batch-build only (scheduled via Pinterest native scheduler or Tailwind). Pinterest is the highest-ROI platform per hour for a new account because pins drive evergreen traffic without requiring video production.

**What to deprioritize at 3 hours/week**:
- TikTok and Instagram Reels (require filming, editing, captioning — 30-45 min per video)
- Lifestyle photography (requires sourcing, compositing, or shooting time)
- Email list setup (set up Kit free tier in the first available hour, then pause until availability increases)

**Expected output**: Shop live by end of Week 1. 5-10 Pinterest pins per week driving slow organic traffic from Week 3 onward. 1-3 Etsy sales in Month 1 (below Scenario B forecast but nonzero).

### Scenario 2: 8 Hours Per Week Available

This is sustainable operation. Revenue at Scenario B pace is realistic.

**Allocation by week**:

Week 1:
- Track A: 2.5 hours (complete full upload)
- Track B setup: 2 hours (account setup, Canva brand kit)
- Track B content: 3.5 hours (film and edit 2 Reels, build 10 Pinterest pins, write 1 Carousel)

Week 2 onward:
- Track A: 0.5 hours/week (monitoring, minor edits if needed)
- Track B: 7-8 hours/week (2-3 Reels, 2-3 Carousels, 15+ Pinterest pins, daily Stories)

**What to deprioritize at 8 hours/week**:
- Lifestyle photography DIY shoot (defer to the first week that Track A shows 50+ views without a sale — that is the trigger to prioritize photography)
- Bundle listings (set up after 5+ individual sales confirm product traction)

**Expected output**: Shop live by Day 3. 2 Reels/week on Instagram and TikTok. Pinterest base of 60+ pins by end of Month 1. Reaching Scenario B forecast (month 1: $150-$250 gross) by end of Week 4.

### Scenario 3: 15+ Hours Per Week Available

Full concurrent execution. Both tracks fully active.

**Allocation**:
- Track A: 3 hours in Week 1, then 1-2 hours/week for Phase 2 product additions and bundle setup
- Track B: 12+ hours/week for full cadence (4-5 Reels, daily Stories, 15-20 Pinterest pins, 1-2 Carousels)
- Photography: 4-6 hours in Week 2 for Tier 1 stock sourcing and Etsy slot 4-5 upload

This is the pace needed to reach 100 followers on Instagram by Day 30 and 20+ Etsy sales in Month 1.

---

## Part 5: Risk Mitigation

### Risk 1: Track A upload stalls again

**Mitigation**: Begin Track B immediately regardless. Even if Phase 1 never launches, an Instagram and Pinterest account with 500+ followers and a Kit email list with 200+ subscribers has equity value. It can be redirected to a different shop, a Gumroad or Payhip storefront (which do not require the same verification steps as Etsy), or converted into an affiliate content account. Track B is not wasted effort without Track A.

**Trigger**: If Track A has not launched by Day 21 from today (May 20, 2026), evaluate moving Phase 1 sales to an alternative platform. Gumroad requires only a payment email to sell digital products; there is no verification hold and listings can go live within minutes.

### Risk 2: Track B content requires lifestyle photos that do not exist

**Mitigation**: The first 2 weeks of the 60-Day Calendar (phase-2-social-content-calendar-60day.md) can run on existing mockup images with minimal adaptation. Day 1 Reel is an origin story video (no product images required). Day 3 Carousel uses mockup images as slides (which are already complete at 2400x2400px). Day 7 single image post benefits from a lifestyle photo but can run with a mockup in week 1.

The specific adaptation: wherever the 60-Day Calendar says "use the lifestyle photo," substitute the mockup PNG for the corresponding product. The caption and hook remain identical. A mockup-based post performs slightly lower in saves but is indistinguishable in reach and follower acquisition.

**Lifestyle photo trigger**: Source or produce Tier 1 lifestyle images when the first product reaches 50 views on Etsy. That data point tells you which product to prioritize for photography investment. Do not invest photography time before that signal.

### Risk 3: Limited time causes both tracks to stall simultaneously

**Mitigation**: If time becomes scarce mid-execution, suspend Track B (social content can pause without permanent damage) and protect Track A (the Etsy upload workflow). A week with no social posts loses social momentum. A week with no Etsy listings means zero revenue. Prioritize the revenue-generating track.

The exception to this rule: if Track A is blocked by account verification and cannot proceed regardless of time investment, then Track B is the only place to invest limited time. In that scenario, Pinterest batch-building is the highest-ROI Track B activity per hour: 2 hours of pin creation yields 10-15 pins that will generate search traffic for 6-18 months.

### Risk 4: Etsy algorithm disadvantage from delayed launch

**Mitigation**: Etsy's algorithm weights recency of sales and review velocity. A shop that launches in late May instead of late April competes against shops that have an extra month of data. This is a real disadvantage that cannot be fully mitigated — only minimized. The mitigation is quality listing copy and strong tag compliance, both of which are already complete.

What is not useful as mitigation: rushing a low-quality launch to capture early algorithm credit. An early listing with wrong tags or a poor mockup trains the algorithm with bad data and is harder to recover than a delayed launch with correct data from Day 1. Phase 1's assets are high quality. The delay is unfortunate but launching correctly is better than launching quickly.

---

## Part 6: Success Metrics for Concurrent Execution

These metrics confirm that concurrent execution is on track. Check them at the end of Week 2 and Week 4.

### Track A Metrics

| Metric | Week 2 Target | Week 4 Target | Source |
|--------|--------------|--------------|--------|
| Etsy listings live | 6 | 6+ (bundles added) | Etsy Shop Manager |
| Total shop views | 100+ | 400+ | Etsy Stats |
| Any sales | 1+ | 5+ | Etsy Payment Account |
| Any 5-star reviews | 0 (acceptable) | 1+ | Etsy Reviews tab |

### Track B Metrics

| Metric | Week 2 Target | Week 4 Target | Source |
|--------|--------------|--------------|--------|
| Instagram followers | 50+ | 150+ | Instagram Insights |
| Pinterest monthly views | 500+ | 2,000+ | Pinterest Analytics |
| TikTok followers | 25+ | 100+ | TikTok Analytics |
| Email list signups | 10+ | 50+ | Kit Dashboard |

### Cross-Track Metrics

| Metric | Week 4 Target | Source |
|--------|--------------|--------|
| Etsy sessions from social traffic | 20+ | Etsy Stats > Traffic Sources |
| Etsy conversion rate | 0.5%+ | Etsy Stats |
| Listings with ≥1 sale | 2+ | Payment Account CSV |

If Track A metrics are not met by Week 2, run the listing audit protocol in docs/phase-1-to-phase-2-decision-matrix.md. If Track B metrics are not met by Week 2, review caption quality and hashtag strategy for the underperforming platform.

---

**Document owner**: Seedwarden Agent
**Prepared**: 2026-04-29
**Next review**: Week 2 after concurrent launch begins (check all metrics above)
