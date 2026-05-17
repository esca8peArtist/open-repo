---
title: "Track B — Execution Readiness Plan"
prepared: 2026-05-17
session: Orchestrator
status: ACTIVE — 13 days to May 30 launch
scope: >
  Maps all Track B work into three buckets: completed, pending user decisions,
  and ready-to-execute autonomous prep. Includes day-by-day timeline assuming
  user decisions made by May 24.
references:
  - TRACK_B_USER_GATES.md (three-gate execution checklist)
  - TRACK_B_EXECUTION_READINESS_AUDIT.md (Session EQ-57, May 15 audit)
  - CANVA_ZONE_CARDS_PRODUCTION_PLAN.md
  - TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md
  - MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md
  - PHASE_2_GO_NO_GO_DASHBOARD.md
---

# Track B — Execution Readiness Plan

**Prepared**: 2026-05-17
**Launch target**: 2026-05-30
**Days remaining**: 13
**Track status**: Clear path — no structural blockers, two platform-tier decisions pending

---

## 1. Completed

The following Track B work is fully done. No further agent or user action required in these areas.

**Content and copy**

- All five welcome sequence email bodies are written and confirmed present at `marketing/email-and-launch-plan.md`. The only pre-launch edit required is a stale date in Email 5 ("May 20 (tomorrow)") — a 5-minute find-and-replace when loading Email 5 into Kit.
- Social content calendar through June 30 is complete: `MAY_30_JUNE_30_CONTENT_CALENDAR.md` and `phase-2-social-content-calendar-60day.md`. Day 1 caption text and hashtags are ready.
- All Etsy listing copy and pricing is confirmed in `etsy-store-copy.md`. All 8 Phase 2 product PDFs exist in `scripts/output/` and are under 5 MB.
- Kit landing page headline and form copy are finalized in `TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md` (Section "Landing Page"). No writing needed — it is copy-paste ready.

**Design specifications**

- Brand Kit specification is complete: 10 hex codes (6 brand + 4 zone band), 3 font names, and logo file path are all documented in `TRACK_B_USER_GATES.md` Gate 2 and `CANVA_SETUP_STATUS.md`. Zero design decisions remain.
- Zone card content for all 8 zones (Zones 3–10) is fully written and formatted as copy-paste tables in `CANVA_ZONE_CARD_BATCH_WORKFLOW.md`. Step-by-step Canva build instructions are in `CANVA_ZONE_CARD_DESIGN_GUIDE.md`.
- Pinterest pin template specifications are in `pin-template-specs.md`. Five pin templates are ready to build once Brand Kit is configured.
- All mockup images are confirmed present (63 files in `mockups/`). These are the fallback visual assets if zone card graphics are not ready for Day 1 social posts.

**Infrastructure and scripts**

- 18 wild-edibles habit photos are present in `assets/wild-edibles/` and follow the species-slug naming convention. Go/No-Go Criterion 2 photo check is satisfiable.
- Logo file is confirmed present: `logos/seedwarden_logo_1.png`.
- Analytics monitoring scripts are present: `scripts/etsy_daily_sync.py` and `scripts/discord_daily_alert.py`.
- Etsy API configuration (OAuth 2.0, rate limits) is current and documented in `PHASE_2_ANALYTICS_INFRASTRUCTURE_PRESTAGING.md`. No API changes detected since documentation.
- Coupon code SEEDWARDEN15 (15% off) is documented and ready to enter when activating Etsy listings.

**Planning and contingency**

- Go/No-Go decision framework is complete: `PHASE_2_GO_NO_GO_DASHBOARD.md` (5 criteria, 4–5 sub-checks each, May 29 morning/afternoon/evening block schedule).
- Fallback paths for all three gates are documented in `MAY_30_RISK_AND_CONTINGENCY_PLAN.md`.
- Hour-by-hour May 30 execution sequence is in `MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md`.
- UTC vs. local time discrepancy between launch documents is identified and resolved: follow Gates document local-time schedule (12:00 pm local for broadcast, 2:00 pm TikTok, 3:30 pm Pinterest). Set Buffer/Kit to local time.
- TRACK_B_USER_GATES.md Issues 1, 2, 5, and 7 have been corrected in the current (updated) version of that document. The TikTok mobile prerequisite is now in the pre-session block; Gate 3 carries the correct 7.5–10.5 hour total estimate across May 24–28; and the May 29 section now references the full Dashboard audit.

---

## 2. Pending User Decisions

Two decisions are outstanding. Neither is a structural blocker to May 30 — both have documented fallbacks — but earlier resolution gives more production time for the dependent work.

**Decision A: Canva Pro vs. free-tier workaround**

The zone card and social graphic production plan assumes Canva's Brand Kit color palette is available with one click. On Canva's free tier, the Brand Hub is available, but if Canva enforces a color-swatch limit during Gate 2 execution, the workaround is a hex cheat sheet (documented in `LAUNCH_CONTINGENCY_PLAYBOOKS.md`, Playbook A1). The question is whether to upgrade to Canva Pro before starting zone card production.

- Canva Pro cost: approximately $15/month.
- Pro unlocks: unlimited Brand Kit colors, background remover, premium elements. None of the specified zone card or pin designs require Pro-only elements. The free tier is sufficient if the swatch limit does not trigger.
- Recommendation: attempt Gate 2 on free tier first. If a paywall appears during Brand Kit color entry, upgrade. Do not pre-purchase Pro on the assumption the limit will trigger.
- Impact if unresolved by May 24: free tier workaround (hex cheat sheet) adds 1–2 minutes per design piece. At 8 zone cards + 5 pins, this is 20–30 minutes of extra time — manageable, not blocking.

**Decision B: Kit Creator plan vs. free tier**

The free Kit tier supports up to 10,000 subscribers, unlimited sends, 1 landing page, and basic automations — fully sufficient for May 30 launch and the first 90 days. The Creator plan adds A/B testing on landing pages, custom domain support, and advanced segmentation. At launch, none of the Creator plan features are needed.

- Kit Creator cost: approximately $25/month for up to 1,000 subscribers.
- Impact if unresolved: launch proceeds on free tier. Creator plan can be activated any time post-launch if list growth justifies it. No launch dependency.
- One exception: if the user wants the landing page URL to be `kit.com/seedwarden` or a custom domain, the free tier gives a generic URL. The URL is functional for email capture but less polished for bio links.
- Recommendation: launch on free tier. Revisit Creator plan when subscriber count reaches 500.

---

## 3. Ready-to-Execute Prep Work

The following items do not depend on either user decision and can begin immediately. They are ordered by dependency chain.

**Immediate (May 17–18) — Gate 1: Social account creation**

Gate 1 requires no design decisions, no platform paid tier, and no prior gate completion. Three business accounts (Instagram, TikTok, Pinterest) need to be created using the same email and logo file. All copy is written. The full step-by-step is in `TRACK_B_USER_GATES.md` Gate 1.

Prerequisites that are already satisfied: logo file present, email accessible, bio copy finalized, handle fallback list documented, business account steps written.

One hardware prerequisite: TikTok account creation requires the TikTok mobile app. Phone must be available and charged to 50%+.

Autonomous prep done now: the TRACK_B_SOCIAL_ACCOUNT_CHECKLIST.md confirmation table is ready to fill in immediately after account creation.

**May 18–19 — Buffer or Later scheduling tool setup**

Social posts for May 30 need to be pre-scheduled. Buffer (free tier: 3 channels, 10 queued posts) or Later (free tier: 1 post per channel per day) are the documented tools. Setting up the scheduling account and connecting the three social accounts is a 20-minute task that does not depend on content being finalized.

Buffer/Later setup can proceed the moment Gate 1 social accounts are live. The May 30 posts can be queued any time from May 24 onward, giving buffer against Day-of technical problems.

**May 19–20 — Analytics infrastructure activation**

The Google Sheets dashboard template needs to be created (`PHASE_2_ANALYTICS_GOOGLE_SHEETS_TEMPLATE_SPEC.md` contains the full schema). The Discord webhook for daily alerts needs to be created. The GA4 custom dimensions need to be set up in GA4 Admin. These are all user-side platform UI tasks, none requiring prior gate completion. The monitoring scripts (`etsy_daily_sync.py`, `discord_daily_alert.py`) are already on disk.

Target: analytics infrastructure live by May 20, giving 10 days of test runs before launch.

**May 20–22 — Day 1 social content production**

The Day 1 Instagram post (Reel or carousel), TikTok video, and 3 Pinterest pins are specified in `MAY_30_JUNE_30_CONTENT_CALENDAR.md` (May 30 row) and `phase-2-social-content-calendar-60day.md` (Day 1). The content formats and captions are written. The visual production (recording or assembling the Reel, exporting carousel slides) can start as soon as social accounts exist.

This does not depend on Brand Kit or zone cards — Day 1 content can use the existing mockup images (63 files confirmed present in `mockups/`). Export image files to phone for manual posting fallback, and queue in Buffer once the scheduling tool is connected.

**May 20–22 — Email sequence copy staging**

All 5 email bodies are confirmed present in `marketing/email-and-launch-plan.md`. Pre-staging means: open the file, copy each email body into a local draft or document, fix the Email 5 stale date now, and note the character counts. When Gate 3 Kit build begins on May 27, copy-pasting from a staged draft is significantly faster than reading and copying from the source file during the Kit session. This takes 30 minutes and removes friction from the Gate 3 session.

**May 24 — Gate 2: Canva Brand Kit (30 min)**

Immediately after or before Gate 2, begin zone card production. The Brand Kit must be configured first — this is the 30-minute prerequisite. Everything needed (hex codes, font names, logo file) is in the Gates document. Gate 2 is a morning task; zone card production starts the same afternoon.

**May 24–25 — Zone card production (4–6 hours across both days)**

This is the largest single block of user time before launch. The zone-cards directory at `assets/zone-cards/` is confirmed empty — these 8 PDFs must be built in Canva before Kit Email 1 can be assembled. The full production plan, per-zone content tables, and step-by-step Canva instructions are in three documents: `CANVA_ZONE_CARDS_PRODUCTION_PLAN.md`, `CANVA_ZONE_CARD_BATCH_WORKFLOW.md`, and `CANVA_ZONE_CARD_DESIGN_GUIDE.md`.

Build order: Zone 5 master template (90 min first session), then duplicate for Zones 6, 3, 4, 7, 8, 9, 10 (30–45 min each). Export all 8 as PDFs named `zone-[number]-quick-start-card.pdf`. Do not export until Etsy Zone Calendar link and Kit landing page URL placeholders are confirmed — use ALL-CAPS bracket placeholders during build, replace before final export.

**May 25 — Google Drive hosting (30 min)**

Upload all 8 zone card PDFs to Google Drive. Set sharing to "Anyone with the link." Generate direct download links using the `uc?export=download&id=[FILE_ID]` format (not the standard share view URL). Test all 8 links in incognito — each must download immediately as a PDF, not open a viewer. Log all 8 links in WORKLOG.md under "Kit Zone Card File URLs."

**May 26 — Buffer queue: schedule May 30 posts**

With social accounts live and content produced, pre-schedule the May 30 posts in Buffer: Instagram 12:00 pm, TikTok 2:00 pm, Pinterest 3:30 pm (all local time). Confirm all 3 show "Scheduled" status. This is a 15-minute task that eliminates one launch-day failure mode.

---

## 4. Timeline to May 30

Assumes user decisions (Canva Pro / Kit Creator) made by May 24 at the latest. Both decisions default to free tier if unresolved, with no launch impact.

| Date | Block | Work | Est. Time | Gate |
|------|-------|------|-----------|------|
| May 17–18 | Ready now | Gate 1: Instagram, TikTok, Pinterest account creation | 45–60 min | Gate 1 |
| May 18–19 | After Gate 1 | Buffer or Later account setup; connect 3 social channels | 20 min | — |
| May 19–20 | Independent | Analytics infra: Google Sheets dashboard, Discord webhook, GA4 custom dimensions | 60–90 min | — |
| May 20–22 | After Gate 1 | Day 1 content production: Reel/carousel, TikTok video, 3 Pinterest pins | 2–3 hours | — |
| May 20–22 | Independent | Email copy staging: pre-copy all 5 emails to draft; fix Email 5 stale date | 30 min | — |
| May 24 (AM) | After above | Gate 2: Canva Brand Kit setup (10 colors, 3 fonts, logo) | 30 min | Gate 2 |
| May 24 (PM) | After Gate 2 | Zone card production: Zone 5 master template + Zone 6 | 90–120 min | — |
| May 25 (AM–PM) | Continuation | Zone card production: Zones 3, 4, 7, 8, 9, 10; export all 8 PDFs | 3–4 hours | — |
| May 25 (EOD) | After export | Google Drive upload; generate + test all 8 download links; log in WORKLOG | 30 min | — |
| May 26 | After content done | Buffer: schedule May 30 Instagram, TikTok, Pinterest posts | 15 min | — |
| May 27 | After Drive links ready | Gate 3 Phase A: Kit account creation, all 15 tags | 20 min | Gate 3 start |
| May 27–28 | Continuation | Gate 3 Phase B: landing page build, 5-email sequence, automation rules | 2.5–3 hours | Gate 3 |
| May 28 | After sequence built | Gate 3 Phase C: 3-test protocol (2 zones + delay check); activate sequence | 30 min | Gate 3 done |
| May 28 | After landing page live | Add Kit landing page URL to all 3 social bios | 5 min | — |
| May 29 AM | Full verification | May 29 Morning Block: C2 (visual assets) + C4 (sales readiness) per PHASE_2_GO_NO_GO_DASHBOARD | 2–3 hours | Go/No-Go |
| May 29 PM | Continuation | May 29 Afternoon Block: C3 (marketing infra) + C5 (performance baseline) + decision | 1–2 hours | Go/No-Go |
| May 29 PM | After Dashboard audit | 5-question gate check; record Go/No-Go result in WORKLOG | 15 min | — |
| May 29 EVE | Final arm | Kit sequence active confirm; Buffer queue confirm; Etsy listings in Draft confirm | 20 min | — |
| May 30 | Launch | Hour-by-hour sequence per MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md | All day | Launch |

**Total user time from today to launch**: approximately 18–24 hours of platform work, distributed across 13 days. The largest single-day commitment is May 24–25 (zone card production, 4–6 hours). All other days are under 2 hours.

**Critical path**: Gate 2 (May 24) → zone card production (May 24–25) → Google Drive links (May 25) → Gate 3 Kit build (May 27–28) → May 29 Go/No-Go → May 30 launch. Nothing on this path depends on the two pending user decisions.

---

*Prepared: 2026-05-17. All file paths in this document are verified against actual filesystem state as of the audit date (May 15) and current session (May 17). Zone-cards directory confirmed empty — production is the single largest remaining autonomous-to-user handoff before Gate 3 can complete.*
