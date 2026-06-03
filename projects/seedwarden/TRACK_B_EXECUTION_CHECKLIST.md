---
title: "Track B Execution Checklist — Go/No-Go Decision Brief"
prepared: 2026-06-03
prepared_by: research-agent (claude-sonnet-4-6)
status: DECISION REQUIRED — June 3 EOD
audience: user (thorn)
sources:
  - GATE_1_LAUNCH_DECISION_BRIEF.md (June 3, 2026)
  - TRACK_B_ACTIVATION_READY.md (June 1, 2026)
  - SEEDWARDEN_TRACK_B_GATES_RUNBOOK.md (May 26, 2026)
  - PHASE_3_ASSETS_VERIFICATION.md (May 13, 2026)
  - PHASE_3_DECISION_GATES_FRAMEWORK.md (May 27, 2026)
  - ORCHESTRATOR_STATE.md (June 3, 2026)
---

# Track B Execution Checklist — June 3, 2026

**Bottom line**: Track B has zero blockers. All infrastructure was verified on June 1. The only
remaining work is 3.5–4.5 hours of platform setup (5 user action gates). You are reading this
to decide whether to greenlight that session today.

---

## 1. Current Track B Status

**The May 30 launch target has passed without execution.** The date has slipped to the present
(June 3). This is not a failure — the Gate 1 decision brief was prepared for today's EOD
decision, and the Phase 3 critical path is still intact if you launch by June 5.

**What has not changed**: Every infrastructure asset is production-ready. The June 1 dry-run
verified all 8 zone PDFs (636–648 KB each), 5 email bodies, 15 influencer contacts, 18 social
post drafts, the logo, and all 8 companion runbook files. Zero re-work is required.

**What has changed**: The Phase 3 data window is tighter.

| Launch date | Day 14 checkpoint | Phase 3 buffer |
|---|---|---|
| June 3 (today) | June 17 | 5 days before June 22 sprint |
| June 4 | June 18 | 4 days |
| June 5 | June 19 | 3 days |
| June 8 | June 22 | Zero — Phase 3 begins same day as Day 14 data arrives |
| June 10+ | June 24+ | Phase 3 starts before launch data available |

**Recommendation from project agents**: Launch Track B today (Option 3: Dual-Track).
Start Track B gates now; continue Etsy verification in background. Etsy integrates
into Emails 3–5 before Day 5 — you have a 5–10 day window after launch to fill those
placeholders. No re-work, no lost infrastructure.

---

## 2. Track B-Specific Blockers

**Track B has no technical blockers.** The following items are user action gates, not
infrastructure failures. Nothing is broken. Everything is waiting on you.

The five items below must be completed by you before launch. They cannot be done
autonomously.

| Item | Nature | Time required | Can it slip? |
|---|---|---|---|
| Gate 4: Google Drive PDF upload | Platform access required | 20 min | No — Gate 3 depends on these links |
| Gate 1: Social accounts (Instagram, TikTok, Pinterest) | Platform access required | 45–60 min | Minor — launch can proceed with 1–2 platforms |
| Gate 3: Kit account + landing page + email automation | Platform access + decisions required | 2–3 hrs | No — this is the email capture infrastructure |
| Gate 2: Canva Brand Kit | Platform access required | 20–30 min | Yes — non-blocking for launch, do after Gate 3 |
| Gate 5: SEEDWARDEN15 Etsy coupon confirmation | 5 min check | 5 min | Yes — Email 5 fires on Day 10, 10-day buffer |

**Track A blockers (separate, do not affect Track B)**:
- Etsy account verification (Etsy review queue: 3–14 business days, external dependency)
- Tag corrections on 3 listings (Companion Planting Chart, Survival Garden Plans, Zone-by-Zone Calendar)

These two Track A blockers have zero effect on Track B. Etsy integration is optional for
Track B launch — it slots into Emails 3–5 after launch when Etsy confirms.

---

## 3. The 5-Gate Sequence for Track B

Execute gates in this order. Each is a single uninterrupted session.

**Total time: 3.5–4.5 hours in one sitting (or split after Gate 3 completes).**

### Gate 4 — Google Drive PDF Upload (Do This First)
**Time**: 20 minutes  
**Why first**: Kit Email 1 cannot be built without the 8 zone card download links.

1. Open Google Drive, create folder "Seedwarden Zone Cards"
2. Upload all 8 PDFs from `projects/seedwarden/assets/zone-cards/`
   (files already on disk, verified June 1, 636–648 KB each)
3. Set folder sharing to "Anyone with the link can view"
4. For each file, extract FILE\_ID and construct:
   `https://drive.google.com/uc?export=download&id=[FILE_ID]`
   (Use the export=download format, NOT the standard /view link)
5. Test all 8 links in incognito — each must trigger a PDF download with no "Request access" error
6. Log all 8 links in WORKLOG.md under "Kit Zone Card File URLs — Gate 4"

**Gate 4 pass criteria**: 8 links tested, all download without errors, all logged.

---

### Gate 1 — Social Media Accounts (45–60 minutes)
**Time**: 45–60 minutes  
**Requires**: Phone (TikTok is mobile-only), computer, logo file downloaded to both

Setup order: Instagram (desktop) → TikTok (phone) → Pinterest (desktop)

For each platform:
- Email: wanka95@gmail.com
- Handle: try `seedwarden` first (fallbacks: `seedwarden.co`, `seedwarden.seeds`)
- Profile photo: `projects/seedwarden/logos/seedwarden_logo_1.png` (919 KB, verified)
- Account type: Business (Instagram, Pinterest) or Business Creator (TikTok)
- Bio link: Leave blank — add Kit URL after Gate 3

Instagram bio (copy exactly, 150-char limit):
`Field guides for growers, foragers + food preservers. Heirloom seeds. Wild edibles. Real food skills. Zone-specific free card below`

TikTok bio (80-char limit, two lines):
`Field guides for growers + foragers`
`Free zone card in bio`

Pinterest about (160-char limit):
`Seedwarden — heirloom seeds, wild edibles, food preservation + zone-specific growing guides. Practical field guides for real food growers.`

**Gate 1 pass criteria**: All 3 accounts live, business type set, bios correct, logo uploaded.

---

### Gate 3 — Kit Account + Landing Page + Email Automation (2–3 hours)
**Time**: 2–3 hours (the critical-path gate — do not split across days)  
**Requires**: Gate 4 links already in hand

Sub-steps:
1. Create Kit account at kit.co (email: wanka95@gmail.com, sender name: Seedwarden)
2. Create 15 tags: zone-3 through zone-10, plus seed-saver, forager, food-preserver,
   homesteader, medicinal-herbs, vip-buyer, phase-1-buyer
3. Create landing page with zone dropdown (8 zones), headline, subheading, form
4. Build 5-email automation sequence from `execution/TRACK_B_EMAIL_COPY_FINAL.md`
   (copy is final and verified — no rewriting needed):
   - Email 1 (Day 0): Zone card delivery (8 zone-variant PDF links from Gate 4)
   - Email 2 (Day 2): Heirloom seed philosophy
   - Email 3 (Day 5): Seed-saving origin story
   - Email 4 (Day 7): Guide catalog introduction
   - Email 5 (Day 10): First offer with SEEDWARDEN15 coupon
     (scan Email 5 for stale date references before saving)
5. Set automation trigger: "When subscriber joins via landing page"
6. CRITICAL: Set automation to Published (not Draft) — this is the most common failure point
7. Run 3-test protocol: Zone 5 signup, Zone 8 signup, verify Email 2 does not arrive immediately

After Gate 3, provide the Kit landing page URL to the orchestrator. Autonomous pre-launch
Step 1 will substitute it into all 18 social post drafts and influencer DM templates.

**Gate 3 pass criteria**: Automation Published (not Draft), 3-test protocol passed,
Kit URL in hand.

---

### Gate 2 — Canva Brand Kit (20–30 minutes, non-blocking for launch)
**Time**: 20–30 minutes  
**Can be done after launch**: Yes — social posting starts Day 1, Canva is needed for Day 3+

At canva.com/brand-hub, create "Seedwarden" kit with:
- 6 brand colors: `#143b28`, `#1A3A2A`, `#F5EDD6`, `#EDE0C4`, `#8FA882`, `#A0522D`
- 4 zone band colors: `#3D6B8A`, `#2D5016`, `#C9943A`, `#A0522D`
- 3 fonts: Playfair Display, Lato (fallback: Source Sans 3), Cormorant Garamond
- Logo: `projects/seedwarden/logos/seedwarden_logo_1.png`

Color palette decision: Option B (Multi-Color Palette) is the recommended default.
Choose at Gate 2 — this decision is final for all Phase 2 and Phase 3 design work.

**Gate 2 pass criteria**: Brand Kit live in Canva, 10 colors, 3 fonts, logo visible.

---

### Gate 5 — SEEDWARDEN15 Etsy Coupon Confirmation (5 minutes)
**Time**: 5 minutes  
**10-day buffer**: Email 5 fires on Day 10 — you have until 10 days post-launch to confirm

Log into Etsy > Marketing > Sales and Coupons. Confirm SEEDWARDEN15 exists as active
(15% off, no minimum, no expiry). If not yet present: create it now. If Etsy account is
not yet verified, note the gap — Track B's 10-day Email 5 delay gives you time to resolve
Track A verification before this email fires.

**Gate 5 pass criteria**: SEEDWARDEN15 coupon confirmed active OR Track A verification
timeline confirmed to complete before Day 10.

---

## 4. Timeline: Gate 1 Launch Through June 22–July 13

| Date | Event | Decision required? |
|---|---|---|
| Today (June 3) | Gates session — 3.5–4.5 hrs | Yes — greenlight gates today |
| June 4 AM | Launch day sequence executes (07:30 UTC) | No — follows runbook |
| June 6 (Day 3) | First metrics checkpoint: Kit subscribers, Reddit upvotes, influencer responses | Read metrics only |
| June 10 (Day 7) | Tier 2 partnership identification; top 3 responders approached | 30 min |
| June 17 (Day 14) | Phase 3 go/no-go decision | Yes — 50+ subscribers = full GO; 25–49 = GO with scope reduction |
| June 22 | Phase 3 sprint begins: Women's Health bundle writing | Scope decision from Day 14 |
| June 22–23 | Kit herbalist tags (15 min), Lead Magnet A landing page, Medicinal Herbs palette added to Canva | User action |
| June 29 | Gate 3 (Phase 3): Women's Health bundle upload live on Etsy | Zero-float deadline |
| July 11 | Forager cohort check: >20% buyers AND conversion >1.5% | Gate condition for Etsy listing publication |
| July 13 | Phase 3 sprint closes: final bundle uploaded | — |

**Phase 3 gates (June 22–July 13 sprint)** are documented in `PHASE_3_DECISION_GATES_FRAMEWORK.md`.
The four Phase 3 gates have different semantics from the Track B launch gates:
- Phase 3 Gate 1 (June 15): Mountain Rose Herbs order placed + palette decision logged
- Phase 3 Gate 2 (June 21): Attribution log complete + Canva Brand Kit loaded
- Phase 3 Gate 3 (June 29): Women's Health bundle live on Etsy
- Phase 3 Gate 4 (July 8): All 5 PDFs export-ready, Etsy drafts staged

Phase 3 Gate 1 deadline is June 15 — 12 days from today. If Track B launches by June 5,
that leaves 10 days to place the Mountain Rose Herbs order and lock the color palette before
Phase 3 Gate 1 closes.

---

## 5. Go/No-Go Decision Tree for Gate 1 (Track B Launch)

Use this to make the call today.

```
Do you have 4–6 hours available today (June 3)?
├── YES → Launch today. Start gates now: Gate 4 → Gate 1 → Gate 3 → Gate 2 → Gate 5.
│          Launch day sequence runs June 4 morning.
│
└── NO → Can you block 4–6 hours on June 4 or June 5?
         ├── YES → Schedule session. June 4 or 5 launch still preserves the
         │          Phase 3 data window. Confirm date below.
         │
         └── NO → Can you start Gate 4 + Gate 1 today (1–1.5 hours) and
                  complete Gate 3 tomorrow (2–3 hours)?
                  ├── YES → Split-session acceptable. Gates 4 and 1 today,
                  │          Gate 3 tomorrow, launch June 5.
                  └── NO → Defer to June 6–8. Note: a June 8 launch eliminates
                             the Phase 3 data window. Phase 3 proceeds on
                             assumption, not validation.
```

**Is Etsy close to verified (within 3 days)?**  
This does not change the Gate 1 decision. Dual-track is the recommended path regardless.
Track B launches without Etsy; Etsy integrates via Emails 3–5 before Day 5 (5-day window
post-launch before Email 3 fires). No re-work required when Etsy confirms.

---

## 6. Specific User Action Items Before Gate 1 Executes

These are the only things standing between you and launch:

**Right now, before starting the gate session:**
- [ ] Download `seedwarden_logo_1.png` from `projects/seedwarden/logos/` to both phone and computer
- [ ] Open Gmail (wanka95@gmail.com) — verification emails from Instagram, TikTok, Pinterest, and Kit all land here
- [ ] Install TikTok app on phone if not already installed (account creation is mobile-only — this will block you if you skip it)
- [ ] Block a 4-hour calendar window with no interruptions — Gate 3 (Kit setup) is the single longest block and breaks if interrupted mid-automation

**During the gate session (copy these reference files into separate tabs):**
- `track-b-activation/READINESS_REPORT_JUNE_1.md` — gate details and user steps
- `track-b-activation/ACTIVATION_RUNBOOK.md` — fill in the Gate Completion Record as each gate clears
- `execution/TRACK_B_EMAIL_COPY_FINAL.md` — paste-ready email copy for Gate 3

**After Gate 3 completes (before closing the session):**
- [ ] Copy the Kit landing page URL
- [ ] Provide it to the orchestrator — autonomous pre-launch steps 1–7 will substitute it into all social post drafts and influencer templates
- [ ] Add the Kit URL to Instagram, TikTok, and Pinterest profile link-in-bio fields

**Confirm in WORKLOG.md after gates complete:**
- Gate 4: Log all 8 Google Drive download links under "Kit Zone Card File URLs — Gate 4"
- Gate 1: Log all three platform handles + profile URLs
- Gate 3: Log Kit landing page URL, confirm automation Published status
- Gate 2: Log color palette decision (Option A/B/C) with rationale
- Gate 5: Log SEEDWARDEN15 coupon status

---

*Prepared: 2026-06-03 by research-agent (claude-sonnet-4-6).*
*Sources: GATE_1_LAUNCH_DECISION_BRIEF.md, TRACK_B_ACTIVATION_READY.md,*
*SEEDWARDEN_TRACK_B_GATES_RUNBOOK.md, PHASE_3_ASSETS_VERIFICATION.md,*
*PHASE_3_DECISION_GATES_FRAMEWORK.md, ORCHESTRATOR_STATE.md.*
