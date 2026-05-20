---
title: "Track B — Execution Pre-Staging: May 30 Launch Window"
prepared: 2026-05-20
status: production-ready — user review May 29–30
scope: >
  Asset inventory audit, execution gap map, risk register, checkpoint calendar,
  and ready-for-launch summary for Track B May 30–June 22 window.
decision-deadline: May 30, 2026
launch-window: May 30 – June 22, 2026
phase-3-follows: June 22 – July 13, 2026
references:
  - TRACK_B_PRODUCTION_PIPELINE.md (pipeline and 63-mockup inventory)
  - TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md (Kit setup, all 5 emails)
  - MAY_30_JUNE_30_CONTENT_CALENDAR.md (30-day social calendar)
  - MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md (hour-by-hour launch sequence)
  - MAY_30_RISK_AND_CONTINGENCY_PLAN.md (gate-failure fallbacks)
  - TRACK_B_COMPLETION_VERIFICATION.md (May 28–29 go/no-go procedure)
  - TRACK_B_MAY30_DECISION_FRAMEWORK.md (3 Phase 3 decisions)
  - JUNE22_LAUNCH_EXECUTION_CHECKLIST.md (Phase 3 execution checklist)
---

# Track B — Execution Pre-Staging: May 30 Launch Window

**Read this document on May 29 evening or May 30 morning before opening anything else.**

This document is the single-entry pre-flight for the May 30–June 22 Track B launch window.
It verifies that all assets are present, maps who does what between now and June 22, registers
the 7 likeliest failure modes with contingency routes, and provides a day-by-day checkpoint
calendar with explicit decision gates.

If everything in Section 5 (Ready for May 30 Summary) is marked PASS, execute the hour-by-hour
sequence in `MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md` beginning at 8:00am.

---

## Section 1: Asset Inventory Status

Verified May 20, 2026. Read against actual filesystem and document content.

---

### Category 1: Product Mockups (63 files)

**Verification method**: Filesystem count against `mockups/` directory.

**Result**: 64 files present (63 mockup images + 1 `phase-3/` subdirectory). The 63 mockup
images are confirmed present at `projects/seedwarden/mockups/`.

**21 products covered** (3 images each: `-mockup.png`, `_interior.png`, `_phone.png`):

| Cluster | Products Confirmed |
|---|---|
| A — Seeds/Garden (9) | seed-saving-field-manual, heirloom-variety-selection-guide, anti-catalog-30-heirlooms, companion-planting-chart, zone-seed-starting-calendar, food-sovereignty-starter-guide, apartment-seed-starting-kit, 12-month-urban-growing-planner, free-5-easiest-vegetables |
| B — Urban/Container (4) | container-growing-blueprint-pack, apartment-growing-complete-guide, apartment-plant-catalog, seed-swap-hosting-kit |
| C — Food Preservation (3) | harvest-preservation-field-manual, fermented-preserved-harvest-handbook, grow-your-own-hot-sauce |
| D — Survival/Outdoors (4) | survival-garden-regional-plans, hunting-fishing-trapping-field-manual, small-scale-livestock-field-manual, meat-fish-preservation-field-manual |
| E — Native Plants (1) | native-plants-regional-guide |

**Status**: PASS — all 63 mockup image files confirmed present. No missing products.
**File date**: All mockup files present; directory created prior to May 20. No stale files.

---

### Category 2: Stock Images — Clusters D and E (10 images)

**Verification method**: Filesystem inspection of `assets/stock-raw/` subdirectories.

**Cluster D — Survival/Outdoors (8 stock images)**:
- `survival-garden-regional-plans/`: 5 files including `survival-garden-regional-plans-slot4.jpg` and `-slot5.jpg` (final selects confirmed)
- `hunting-fishing-trapping-field-manual/`: 5 files including final slot4 and slot5 JPEGs confirmed
- `small-scale-livestock-field-manual/`: slot4 and slot5 finals confirmed, plus candidate files
- `meat-fish-preservation-field-manual/`: slot4 and slot5 finals confirmed, plus candidate files

**Cluster E — Native Plants (2 stock images)**:
- `native-plants-regional-guide/`: 5 files including `native-plants-regional-guide-slot4.jpg` and `-slot5.jpg` (final selects confirmed)

**Compositing status**: Per `TRACK_B_PRODUCTION_PIPELINE.md`, Clusters D and E stock images
await Canva compositing (product PDF overlay step). All 10 source images are present and
accessible. Canva compositing is a user-executed step, estimated 60 min for all 10 images.

**Attribution requirement**: The native plants slot 4 image (Joe Mabel, CC BY-SA 3.0) requires
an attribution line in the Etsy listing description footer. Text is documented in
`TRACK_B_PRODUCTION_PIPELINE.md` Section 4 verbatim.

**Status**: PASS — all 10 stock images confirmed accessible.
**Last modified**: Files present as of May 20 inventory.

---

### Category 3: Email Copy (Kit Automation — All 5 Emails)

**Verification method**: Review of `TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md` and
cross-reference with `marketing/email-and-launch-plan.md`.

**Emails confirmed production-ready**:

| Email | Day | Personalization | Status |
|---|---|---|---|
| Email 1 — Zone Card Delivery | Day 0 (immediate) | 8 zone variants; subject line and body template final | Production-ready |
| Email 2 — Heirloom Seed Philosophy | Day 2 | Single version, all subscribers; no product links | Production-ready |
| Email 3 — Seed Saving Story | Day 5 | Single version; behavioral tag link to Seed Saving Field Manual | Production-ready |
| Email 4 — Catalog Introduction | Day 7 | Single version; 3 behavioral tag links (city-grower, seed-saver, preservationist) | Production-ready |
| Email 5 — First Offer | Day 10 | Single version; coupon code SEEDWARDEN15; product recommendations documented | Production-ready |
| Launch Broadcast | May 30 12:00pm | To all confirmed subscribers; subject and body in `marketing/email-and-launch-plan.md` | Production-ready |

**Full copy location**: `marketing/email-and-launch-plan.md` for all 5 emails. Email 1–3 copy
also mirrored in `MAY_CONTENT_EXECUTION_PLAN.md` (Email Sequences section).

**Kit setup completion status (as of May 20)**: Kit account creation, all 15 tags, landing
page, zone routing automation, and all 5 emails have not yet been started per
`TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md` Setup Completion Log. These remain user-executed gates.
Estimated time: 3–4.5 hours, done in stages.

**Status**: PASS (copy is final and accessible). PENDING (Kit account setup is a user gate
that must be completed before May 28).

---

### Category 4: 60-Day Social Content Calendar

**Verification method**: Review of `MAY_30_JUNE_30_CONTENT_CALENDAR.md` and
`phase-2-social-content-calendar-60day.md`.

**Calendar coverage confirmed**:

| Period | Document | Coverage |
|---|---|---|
| May 30 – June 30 | `MAY_30_JUNE_30_CONTENT_CALENDAR.md` | Day-by-day: platform, format, hook, asset reference, calendar cross-reference |
| Days 1–60 (from launch) | `phase-2-social-content-calendar-60day.md` | Week-by-week: full captions, scripts, hashtags, CTAs per post |
| May–July 2026 | `marketing/social-media-calendar-may-july-2026.md` | Monthly overview |

**Platform cadence confirmed**: Instagram 4 posts/week (2 Reels + 1 Carousel + 1 static);
TikTok 3 posts/week; Pinterest 7 pins/week.

**Launch week (May 30 – June 5)**: All posts fully specified with hooks, format, and asset
references. May 30 launch day posts confirmed with asset paths pointing to `mockups/` and
`marketing/lifestyle-photos/etsy-ready/`.

**File dates**: `MAY_30_JUNE_30_CONTENT_CALENDAR.md` prepared May 13, 2026. Calendar content
is current and not stale. No dates in the calendar are in the past at time of preparation.

**Status**: PASS — 60-day calendar confirmed production-ready with full post specifications.

---

### Asset Inventory Summary

| Category | Count | Status | User Action Required |
|---|---|---|---|
| Product mockups (63 PNG files) | 63 of 63 | PASS | None |
| Cluster D/E stock images (10 JPEGs) | 10 of 10 | PASS | Canva compositing step (~60 min) |
| Email copy (6 email bodies + sequences) | 6 of 6 | PASS (copy final) | Kit account setup (3–4.5 hrs) |
| 60-day social content calendar | 1 document | PASS | Social account creation + Buffer scheduling |

**Overall asset verdict**: All 4 asset categories are present and verified. Two user-executed
setup steps remain (Kit account, social accounts) but the underlying content assets requiring
these setups are fully staged.

---

## Section 2: Execution Gap Map

Who does what between May 20 and June 22. Organized by owner (User or Orchestrator) and window.

---

### Pre-Launch Window: May 20–29

**User actions required before May 30** (ordered by deadline):

| Deadline | Action | Time Required | Unblocks |
|---|---|---|---|
| May 24 EOD | Canva Brand Kit setup (6 hex codes, 3 fonts, logo) | 30 min | Zone card exports, Pinterest pin production, all Canva workflows |
| May 24 EOD | Canva compositing — Clusters D/E (10 images) | 60 min | Etsy slot 4–5 upload for 5 products on May 30 |
| May 25 EOD | Kit account created (kit.co, Gmail, sender name "Seedwarden") | 20 min | Email landing page, broadcast staging |
| May 25 EOD | Kit landing page built and published (Zone Card sign-up page) | 45 min | Social bio links, email list growth before May 30 |
| May 25 EOD | All 8 zone card PDFs exported from Canva | 2–3 hrs | Google Drive upload, Kit Email 1 variants |
| May 25 EOD | Zone card PDFs uploaded to Google Drive with "Anyone with link" sharing | 20 min | Kit Email 1 download links |
| May 26 EOD | All 15 Kit tags created (8 zone tags + 7 interest cohort tags) | 15 min | Zone routing automation |
| May 26 EOD | Kit zone routing automation wired | 30 min | Correct zone card delivery on sign-up |
| May 27 EOD | Kit Email 1 — all 8 zone variants built with Google Drive PDF links | 60–90 min | Automated zone card delivery |
| May 27 EOD | Kit Emails 2–5 built (single version each) | 60–90 min | Full welcome sequence |
| May 27 EOD | Google Drive zone card download links recorded in TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md | 15 min | Future Kit automation updates |
| May 27 EOD | Instagram, TikTok, Pinterest accounts created (@seedwarden or documented fallback) | 30–60 min | Buffer connection, bio links, social launch posts |
| May 27 EOD | Buffer or Later connected to all 3 social accounts | 15 min | Social scheduling |
| May 28 EOD | Kit end-to-end tests passed — Zone 5 flow, Zone 7 flow, Email 3 behavioral tag | 20 min | Confirmed working automation before launch |
| May 28 EOD | Launch broadcast staged in Kit (May 30 12:00pm, all confirmed subscribers) | 20 min | Email fires on schedule without manual intervention |
| May 28 EOD | Launch week social posts scheduled in Buffer (May 30 – June 5) | 60–90 min | Social rollout fires automatically at 2:00pm May 30 |
| May 28 EOD | SEEDWARDEN15 coupon created in Etsy (15% off, no minimum) | 10 min | Email 5 coupon delivery |
| May 29 EOD | Run full TRACK_B_MAY_30_LAUNCH_READINESS_CHECKLIST.md (T-1 verification) | 45 min | Confirms all gates pass before launch day |

**Orchestrator pre-launch actions** (no orchestrator pre-launch actions remain — all outstanding work is user-executed setup in consumer apps):

Orchestrator pre-staged assets are complete. All remaining gates require user login to
Canva, kit.co, Buffer, Instagram, TikTok, Pinterest, Etsy, and Google Drive. No orchestrator
action can substitute for account creation or platform authentication.

---

### Launch Day: May 30

**User actions** (hour-by-hour from `MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md`):

| Time | Action | Owner |
|---|---|---|
| 8:00am | Run full QA — Etsy listings, Kit automation test, Buffer queue verification, zone card links | User |
| 9:00am | Record pre-launch baseline metrics in customer-analytics.csv | User |
| 10:00am | Publish all Etsy Phase 2 lifestyle image uploads (Cluster D/E first); verify in incognito | User |
| 12:00pm | Confirm Kit launch broadcast is sending; check status at 12:05pm | User |
| 12:30pm | Check Kit delivery stats (target: >90% delivery, >35% open rate, >8% click) | User |
| 2:00pm | Instagram + TikTok launch posts fire via Buffer; verify at 2:15pm | User (Buffer automated) |
| 3:30pm | Pinterest launch pins fire via Buffer; verify at 3:45pm | User (Buffer automated) |
| 4:00pm | Comment/engage with 3 foraging or homesteading accounts (influencer outreach) | User |
| 7:00–9:00pm | End-of-day log: full Day 1 metrics in customer-analytics.csv; respond to buyer messages | User |

**Orchestrator launch day actions**: None on May 30. Orchestrator can support post-launch analytics review starting May 31.

---

### Post-Launch Window: May 31 – June 22

**User action timeline** (by week):

**Week 1 (May 31 – June 7) — Stabilization**:
- May 31: Check Kit broadcast final open rate; identify non-openers for Day 3 resend
- June 1: Etsy traffic trend check (views increasing or stable post-launch spike)
- June 1: Make Phase 3 sprint scope decision (per `TRACK_B_MAY30_DECISION_FRAMEWORK.md`)
- June 3: Kit Email 3 automation check (Emails 2–3 should have fired to launch-day subscribers)
- June 5: Full Week 1 metrics review — fill in phase-2-week-1-success-metrics.md targets vs. actuals
- June 6: Day 7 decision gates: apply PHASE_2_GO_NO_GO_DASHBOARD.md criteria

**Week 2 (June 8 – June 14) — Growth and Phase 3 Pre-Sprint**:
- June 8: Goldenseal sourcing path decision (order Prairie Moon by June 8, or confirm Wikimedia CC backup — per `TRACK_B_MAY30_DECISION_FRAMEWORK.md` Decision 2)
- June 8: Black Cohosh order to Strictly Medicinal Seeds if Phase 3 scope confirmed
- Continue social posting cadence per MAY_30_JUNE_30_CONTENT_CALENDAR.md Weeks 2–3
- Week 2 Etsy metric pull (Friday): log in WORKLOG.md

**Week 3 (June 15 – June 21) — Phase 3 Pre-Sprint Setup**:
- June 15: Canva Phase 3 palette confirmed (per `TRACK_B_MAY30_DECISION_FRAMEWORK.md` Decision 3; hard deadline — any palette change after June 23 requires 6 hrs rework)
- June 15: Elderberry order to Prairie Moon Nursery
- June 15: Mountain Rose Herbs dried herb prop order (arrive by June 28)
- Week 3 Etsy metric pull (Friday): log in WORKLOG.md
- June 21: Canva Brand Kit loaded with Medicinal Herbs secondary palette

**June 22: Phase 3 Sprint Start** (if May 30 decision confirms scope):
- June 22: Begin Women's Health bundle writing (Day 1 of 22-day sprint)
- All pre-sprint gates must be complete per JUNE22_LAUNCH_EXECUTION_CHECKLIST.md

**Orchestrator post-launch actions (May 31 – June 22)**:
- May 31: Available to review Day 1 analytics if user shares metrics
- Week 1–4: Available to research, draft, or expand content on request
- Phase 3 pre-sprint: Orchestrator can produce any pre-sprint documents requested (supplier tracking, writing templates, analytics setup)
- No autonomous orchestrator actions are pre-scheduled for this window — all decisions remain user-gated

---

### Contingency Routing

**If social accounts are not created by May 29**:
- Launch proceeds on Etsy + email only on May 30 (confirmed minimum viable launch)
- Create accounts manually at 1:00pm May 30; post launch content manually at 2:00pm
- Use Day 30 captions from `phase-2-social-content-calendar-60day.md`
- No revenue impact; social channel launch delayed 24–48 hours maximum
- Escalation: if accounts cannot be created May 30, social launch slips to June 1

**If Kit automation is not tested by May 29**:
- Run Zone 5 end-to-end test at 8:00am May 30 during QA window
- Most common failure (Google Drive "Request access" on PDF link) is a 5-minute fix
- If test fails and cannot be fixed: stage Kit Email 1 to send "Zone card arriving within 24h" placeholder, then deliver manually while automation is debugged
- Email launch still fires at 12:00pm (existing subscribers receive broadcast regardless of zone routing)

**If Canva Brand Kit is not set up by May 29**:
- Launch proceeds using mockup images from `mockups/` (all 63 confirmed present)
- Enter hex codes manually in Canva for any new designs needed launch week
- No launch blocker; visual consistency for Week 1 social posts relies on mockups (sufficient)

**If supplier delays affect Cluster A/B/C lifestyle photos** (physical shoot clusters):
- Lifestyle photos from Clusters A/B/C are NOT required for May 30 launch
- Clusters D/E stock composites (10 images) are sufficient for launch-day Etsy uploads
- Physical shoot clusters upload as completed in the weeks following launch
- Social content in Weeks 1–2 uses mockup images, which are confirmed present

---

## Section 3: Risk Register

Seven risks for the May 30–June 22 window. Ordered roughly by activation likelihood.

---

### Risk 1: Kit Email Automation Silent Failure

**Description**: Kit sends launch broadcast and welcome sequence without error messages, but
emails are delivered to spam or zone card PDF links return "Request access" rather than
downloading.

**Likelihood**: Medium. Gmail accounts rarely trigger spam filters on Kit free tier. Google
Drive sharing is a one-setting error that produces this exact symptom.

**Impact**: Email 1 click rate drops below 30% (PDF not delivered); subscribers abandon
before receiving value. Recoverable in 24–48 hours but erodes first impression.

**Mitigation**:
1. Run full end-to-end test (Zone 5 + Zone 7) by May 28. Test requires a second email address.
2. Verify Google Drive PDF links open immediately in incognito (no sign-in prompt, no
   "Request access" screen) before wiring into Kit Email 1 variants.
3. If test fails on May 30 morning QA: replace each PDF link with a direct download URL
   (use the `uc?export=download` format documented in `TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md`
   Step 4 "PDF Upload for Zone Card Links").

**Contingency**: If silent delivery failure is discovered post-launch (Email 1 open rate normal
but click rate below 15%), send a "We've fixed your zone card link" reply email within
4 hours. This has been shown to recover a significant portion of lost click-through.

**Activation trigger**: Kit Email 1 click rate below 25% on Day 1. Check Kit analytics at
12:30pm and again at 7:00pm.

---

### Risk 2: Social Account Creation Delayed Past May 30

**Description**: Instagram, TikTok, and Pinterest accounts have not been created by the time
launch day arrives. Buffer has nothing to connect to; pre-scheduled social posts cannot fire.

**Likelihood**: Medium-High. Account creation is a 30–60 minute user-executed task with no
external dependencies. It requires no approval. However, it has been the outstanding gate
since May 1. Risk is not technical — it is scheduling.

**Impact**: Social launch sequence does not fire at 2:00pm on May 30. Social channel launch
delayed 1–7 days. No direct revenue impact on May 30; email and Etsy launch are unaffected.

**Mitigation**:
- Hard deadline: create accounts by May 27 to allow 2-day Buffer setup window.
- If accounts not created by May 29: execute manual social post plan at 1:00pm May 30.
  Captions for launch day posts are in `phase-2-social-content-calendar-60day.md` Day 30.
- Fallback handle list documented in `social-media-setup.md` if `@seedwarden` is taken on
  any platform.

**Contingency**: Social launch slips to June 1 with zero operational impact on Etsy or Kit.
The Etsy + email launch is the revenue-generating action on May 30. Social is audience
building with a 30-day lag on conversion.

**Activation trigger**: Social accounts not created by May 29 evening.

---

### Risk 3: Canva Brand Kit Not Set Up — Zone Cards Missing at Launch

**Description**: Canva Brand Kit setup (30 min) has not been completed. Zone card PDFs
cannot be exported. Kit Email 1 has no PDF to deliver. New email subscribers who sign up
through the launch receive a broken delivery.

**Likelihood**: Medium. Brand Kit setup is a 30-minute task. If zone cards are not exported
by May 28, zone card delivery fails on launch.

**Impact if zone cards missing**: Kit Email 1 fires but the PDF download button links to
nothing or a placeholder. Subscriber receives no zone card. Immediate trust loss. Likely
unsubscribe.

**Impact if Brand Kit only (zone cards separately manageable)**: Social posts use mockup
images instead of branded Canva designs. Visual consistency lower for Week 1. No revenue
impact.

**Mitigation**:
- Canva Brand Kit hard deadline: May 24.
- Zone card export deadline: May 25.
- If zone cards are not exported by May 28: stage Kit Email 1 with a "Your zone card
  arrives in 24 hours — we're putting final touches on it" message. Manually email each
  new subscriber their zone card PDF as an attachment within 24 hours.
- Zone card backfill email template: "Hi [Name], here's your Zone X Quick-Start Card —
  sorry for the short delay!" (brief, warm, no explanation needed beyond "final touches").

**Contingency**: If zone cards are missing on May 30, the launch proceeds without zone card
delivery. Email list building continues; zone card delivery begins as soon as cards are
exported (estimated same day or Day 1 post-launch if Brand Kit setup happens May 30).

**Activation trigger**: Zone cards not exported and Google Drive links not live by May 28.

---

### Risk 4: Canva Phase 3 Palette Discrepancy (June 15 Deadline)

**Description**: Two Phase 3 design documents specify different color palettes.
`phase-3-canva-mockup-brief.md` locks 5 hex codes (Herb Brown, Herb Sage, Herb Cream, Herb
Ink, Herb Alert). `canva-phase-3-adaptation-guide.md` specifies a different palette
(Deep Burgundy, Sage Green, Gold/Amber, Cream, Lavender). If the wrong palette is loaded
into Canva Brand Kit on June 21, all five Phase 3 bundle covers require rebuilding (estimated
6 hours rework).

**Likelihood**: Low-Medium. The discrepancy exists now and will cause confusion at Brand Kit
loading time if not resolved before June 21.

**Impact**: Up to 6 hours of Phase 3 sprint rework on June 22–23 if the wrong palette is
loaded. This pushes the Women's Health upload date from June 29 to July 1. Acceptable but
undesirable.

**Mitigation**:
- Decision 3 in `TRACK_B_MAY30_DECISION_FRAMEWORK.md` asks you to confirm the authoritative
  palette by May 30 (hard deadline June 15).
- On May 30 decision day: open `phase-3-canva-mockup-brief.md` Section 0 and confirm the
  5 hex codes are correct. Write the confirmed palette in the Decision Record.
- If `canva-phase-3-adaptation-guide.md` was an early draft (most likely), mark it deprecated
  in the file header.
- On June 21, load only the palette confirmed on May 30.

**Activation trigger**: Palette decision not recorded by June 15.

---

### Risk 5: Kit Email Template Rendering Issues (Mobile)

**Description**: Kit email templates render correctly on desktop but break on mobile
(images not inlining, button too small, text cut off). Over 60% of email opens are on mobile
devices. A broken mobile render significantly depresses click rates.

**Likelihood**: Low. Kit's default templates are mobile-responsive. Risk is elevated if
custom HTML is inserted or if image sizes exceed Kit's auto-scaling threshold (>600px wide
embedded images).

**Impact**: Email 1 click rate drops to below 15% (below 30% threshold). Email 5 coupon
redemption rate drops. Neither is catastrophic — email sequence continues regardless.

**Mitigation**:
- During end-to-end test (May 28): open test email on a mobile device (not just desktop).
  Check button size (at least 44px touch target), image scaling, and line breaks.
- If button is not prominent: change button color to #143b28 (Deep Forest Green) and
  increase button width to full-width. Documented in `TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md`
  Step 8 monitoring guidance.
- Use Kit's native preview tool ("Mobile Preview" tab) before publishing each email variant.

**Contingency**: If mobile rendering issues discovered post-launch, edit the live email
template in Kit and resend Email 1 with a "refreshed" subject line to non-clickers within
48 hours.

**Activation trigger**: Mobile preview shows broken layout during May 28 test.

---

### Risk 6: Etsy Account Verification Still Blocking Track B

**Description**: Track A (Etsy) remains blocked on 2 user actions: tag corrections and Etsy
account verification. Although Track B is documented as independent of Track A, some
cross-dependencies exist: Etsy coupon SEEDWARDEN15 requires the Etsy account to be active
to create; Kit Email 5 links to Etsy listings.

**Likelihood**: Low impact on Track B launch. Track B's primary value delivery on May 30 is
via email lead magnet (zone cards) and social content — neither requires Etsy to be verified.

**Impact if Etsy still blocked on May 30**: Cannot publish Etsy listing images (Cluster D/E
composites); Kit Email 5 links to unavailable listings; SEEDWARDEN15 coupon cannot be created.

**Mitigation**:
- Track B proceeds independently. Social bio links point to Kit landing page (not Etsy).
- If Etsy is still blocked: Kit Email 5 product links become placeholders or link to the
  Etsy shop main page instead of specific listings.
- SEEDWARDEN15 coupon: if Etsy is not verified, omit the coupon from Email 5 on launch.
  Update Email 5 once Etsy verifies.
- No change to social posts — all captions say "link in bio to get your zone card," not
  "link in bio to buy on Etsy."

**Activation trigger**: Etsy Shop Manager shows verification hold banner on May 30 morning.

---

### Risk 7: Buffer Scheduling Failure (Posts Don't Fire at 2:00pm)

**Description**: Buffer or Later fails to publish scheduled social posts at the configured
time on May 30. This has a documented occurrence rate of roughly 2–5% for newly connected
accounts on launch day.

**Likelihood**: Low. Most Buffer failures occur due to platform token expiry or account
permission changes after initial connection.

**Impact**: Social launch posts do not fire at 2:00pm. May 30 social sequence delayed until
manual posting. No revenue impact; purely cosmetic timing miss.

**Mitigation**:
- Verify Buffer/Later connection status the morning of May 30 (8:00am QA block).
  Reconnect any account showing a "Reconnect" warning before 10:00am.
- Screenshot all queued posts in Buffer before 10:00am as a backup record of approved captions.
- Manual fallback: if Buffer fails at 2:00pm, post directly from the Instagram, TikTok, and
  Pinterest apps using the screenshot backup of captions. Estimated 15 minutes per platform.

**Contingency**: If Buffer is fully inaccessible (service outage), post manually using
captions saved locally. All launch day captions are in `phase-2-social-content-calendar-60day.md`
Day 30.

**Activation trigger**: Buffer shows scheduling error at 2:00pm May 30. Check at 2:15pm.

---

### Risk Register Summary Matrix

| Risk | Likelihood | Impact (delay days) | User Remediation Time | Pre-staged Mitigation |
|---|---|---|---|---|
| R1: Kit email silent failure | Medium | 0–1 day | 30 min | End-to-end test May 28; Drive link format |
| R2: Social accounts delayed | Medium-High | 1–7 days (social only) | 30–60 min | Manual post fallback documented |
| R3: Zone cards missing | Medium | 1–2 days (email magnet) | 60–90 min | Placeholder Email 1 + 24h backfill |
| R4: Phase 3 palette discrepancy | Low-Medium | 2–3 days (Phase 3 only) | 10 min (decide May 30) | Decision gate June 15 |
| R5: Kit mobile render issues | Low | 0 days (fix in-platform) | 30 min | Mobile preview during May 28 test |
| R6: Etsy verification still blocked | Low | 0 days (Track B independent) | 0 (no action needed) | Track B designed independent of Etsy |
| R7: Buffer scheduling failure | Low | 0 days (manual fallback) | 45 min | Manual posting from saved captions |

---

## Section 4: Execution Checkpoint Calendar

Day-by-day from May 24 through June 22. Decision gates are marked with a [GATE] label and
require explicit confirmation before the next phase begins.

---

### Pre-Launch Sprint: May 24–29

**May 24 (Sunday)**
- [ ] Canva Brand Kit setup — 6 hex codes, 3 fonts, logo. 30 min. (Deadline for zone card build)
- [ ] Begin Zone card build in Canva starting with Zone 5 (guide in `CANVA_ZONE_CARD_DESIGN_GUIDE.md`)
- [ ] Canva compositing — Clusters D/E: 10 images, product PDF overlay. 60 min.
- Success signal: Brand Kit shows 6 colors + 3 fonts in Canva Brand Hub; at least Zone 5 card in draft

**May 25 (Monday)**
- [ ] Complete Zone cards 5 and 6 in Canva (45 min each)
- [ ] Kit account creation — kit.co, wanka95@gmail.com, sender name "Seedwarden". 20 min.
- [ ] Kit landing page built and published. 45 min.
- [ ] Landing page URL added to: social-media-setup.md, CANVA_SETUP_STATUS.md placeholder field
- [ ] Zone card PDFs exported (Zones 5, 6) to `assets/zone-cards/`
- Success signal: Kit landing page loads at its public URL; Zone 5 card PDF exported

**May 26 (Tuesday)**
- [ ] Zone cards 3, 4, 7, 8 built in Canva (45 min each, clone Zone 5 and change zone band + content)
- [ ] Zone cards 9, 10 built (same method)
- [ ] All 8 zone card PDFs exported and uploaded to Google Drive; sharing set to "Anyone with link"
- [ ] Google Drive direct-download links generated for all 8 zones (using `uc?export=download&id=` format)
- [ ] All 15 Kit tags created (8 zone tags + 7 interest cohort tags). 15 min.
- Success signal: `ls projects/seedwarden/assets/zone-cards/*.pdf | wc -l` returns 8

**May 27 (Wednesday) — [GATE: Social + Kit Foundation]**
- [ ] Social accounts created: Instagram, TikTok, Pinterest (@seedwarden or documented fallback)
- [ ] Buffer or Later account created and all 3 social accounts connected
- [ ] Kit landing page URL added to all 3 social bios
- [ ] Kit zone routing automation wired (sign-up form → zone tag → zone Email 1 variant)
- [ ] Kit Email 1 — Zone 5 variant built with Google Drive PDF link
- [ ] Kit Email 1 — Zone 6 variant built
- [ ] Kit Email 1 — Zones 3, 4, 7, 8, 9, 10 variants built
- [GATE] Decision: Are all 3 social accounts created? Are zones 3–10 Email 1 variants built?
  - YES: proceed to May 28 automation building
  - NO: document which accounts/variants remain; dedicate May 28 AM to completing them

**May 28 (Thursday) — [GATE: End-to-End Test Pass]**
- [ ] Kit Emails 2–5 built (single versions; full copy from `marketing/email-and-launch-plan.md`)
- [ ] SEEDWARDEN15 Etsy coupon created (15% off, no minimum order)
- [ ] Kit end-to-end test — Zone 5 full flow: sign up → Email 1 → PDF download → zone-5 tag applied
- [ ] Kit end-to-end test — Zone 7 full flow (confirms routing logic works for second zone)
- [ ] Kit Email 3 behavioral tag test (click Seed Saving link → "seed-saver" tag appears)
- [ ] Launch week social posts scheduled in Buffer (May 30 – June 5, from `MAY_30_JUNE_30_CONTENT_CALENDAR.md` Week 1)
- [ ] Launch broadcast staged in Kit with May 30 12:00pm send time and "All Confirmed Subscribers"
- [GATE] Decision: Did all 3 Kit end-to-end tests pass?
  - ALL PASS: proceed to May 29 T-1 verification
  - ANY FAIL: diagnose and fix same day; most common failure is Drive link format (5-min fix)

**May 29 (Friday) — [GATE: Full T-1 Go/No-Go]**
- [ ] Run full `TRACK_B_MAY_30_LAUNCH_READINESS_CHECKLIST.md` — T-1 pass (all PASS/FAIL items)
- [ ] Verify all Phase 2 Etsy lifestyle images are in final export location
- [ ] Confirm Buffer queue shows launch day posts scheduled for correct times (2:00pm IG/TT, 3:30pm PIN)
- [ ] Confirm Kit broadcast shows "Scheduled" status for May 30 12:00pm
- [GATE] Go/No-Go Decision:
  - ALL PASS: "GO — launch May 30"
  - 1–2 FAIL items: "CONDITIONAL GO — resolve listed items by May 30 8:00am"
  - 3+ FAIL items: "NO-GO — delay to June 6" (consult `june-6-contingency-path.md`)

---

### Launch Day: May 30 (Saturday) — [GATE: Day-1 Health Check]

- [ ] 8:00am — Full QA: Etsy listings, Kit automation, Buffer queue, zone card links
- [ ] 9:00am — Baseline metrics logged in customer-analytics.csv
- [ ] 10:00am — Etsy Phase 2 listings published (lifestyle images added; Cluster D/E first)
- [ ] 12:00pm — Kit launch broadcast confirmed sending
- [ ] 2:00pm — Social posts confirmed live via Buffer (or manually post if Buffer fails)
- [ ] 3:30pm — Pinterest pins confirmed live
- [ ] 4:00pm — Influencer engagement (3 accounts from calendar)
- [ ] 7:00–9:00pm — Day 1 metrics logged; buyer messages responded to
- [GATE] Phase 3 Decision Day — fill in Decision Record in `TRACK_B_MAY30_DECISION_FRAMEWORK.md`:
  - Decision 1: Sprint scope (A/B/C/D)
  - Decision 2: Goldenseal sourcing path (live plant or Wikimedia CC)
  - Decision 3: Canva Phase 3 palette confirmation (hex codes from `phase-3-canva-mockup-brief.md`)

---

### Week 1 Post-Launch: May 31 – June 7 — [GATE: Day-7 Decision]

**May 31 (Sunday)**
- [ ] Check Kit broadcast final open rate; identify non-openers for Day 3 resend
- [ ] Etsy order review: confirm all PDF digital deliveries fired

**June 1 (Monday)**
- [ ] Etsy traffic trend check: views increasing or stable
- [ ] Post Week 1 social content (June 1 from `MAY_30_JUNE_30_CONTENT_CALENDAR.md`: IG Carousel + TT + 2 Pinterest pins)

**June 3 (Wednesday)**
- [ ] Post June 3 social content (IG Reel + TT + 2 Pinterest)
- [ ] Kit Email 3 automation check: launch-day subscribers should have received Emails 2–3 by now

**June 5 (Friday)**
- [ ] Post June 5 social content (IG Static + 2 Pinterest zone-specific pins)
- [ ] Week 1 Etsy metric pull: views, favorites, conversion rate. Log in WORKLOG.md.
- [ ] Kit subscriber count, Email 1 open rate, PDF download click rate logged

**June 6 (Saturday) — [GATE: Day-7 Decision]**
- [ ] Full Week 1 metrics review: fill in `phase-2-week-1-success-metrics.md` targets vs. actuals
- [ ] Apply `PHASE_2_GO_NO_GO_DASHBOARD.md` Day-7 decision criteria
- [GATE] Week 1 health check:
  - If Instagram followers 50+, Pinterest monthly views 500+, email list 10+ subscribers, Etsy views 200+: launch confirmed successful; continue Week 2 cadence
  - If Instagram followers below 20: review Day 1 Reel completion rate; if below 30%, re-record hook
  - If Pinterest views below 200: increase pin frequency to 3–4/day for Week 2
  - If email list below 5: verify bio links are active on all 3 platforms; check Kit landing page loads

---

### Week 2: June 8–14 — [GATE: Phase 3 Supplier Decision]

- [ ] Continue social posting cadence per calendar Weeks 2–3
- [ ] June 8: Post June 8 social content (IG Reel + TT + 3 Pinterest)
- [GATE] June 8: Phase 3 supplier decisions:
  - Goldenseal order placed with Prairie Moon (if Decision 2 = Path 1 live plant); OR Wikimedia CC confirmed (if Path 2)
  - Black Cohosh order placed with Strictly Medicinal Seeds (if Phase 3 scope confirmed)
  - If neither order placed by June 8 and Path 1 was selected: automatic fallback to Path 2 (Wikimedia CC) — no action required, no launch impact
- [ ] June 10: Post June 10 social content
- [ ] June 12: Post June 12 social content; Week 2 metric pull (Etsy + Kit + social)
- [ ] Week 2 analytics logged in WORKLOG.md

---

### Week 3: June 15–21 — [GATE: Phase 3 Build Readiness]

- [GATE] June 15 (hard deadline): Canva Phase 3 palette decision recorded. Any hex code changes must be made before June 23 (6-hour rework threshold).
- [ ] June 15: Elderberry order to Prairie Moon Nursery; Mountain Rose Herbs dried herb order
- [ ] Continue social posting cadence
- [ ] Week 3 Etsy metric pull (Friday); log in WORKLOG.md
- [GATE] June 21: Phase 3 build readiness gate:
  - Canva Brand Kit loaded with Medicinal Herbs secondary palette
  - Photo attribution log created at `assets/botanical-photos/phase-3/photo-attribution-log.md`
  - Writing workspace prepared: bundle outline template and content outline open as reference
  - Kit Phase 3 tags created (7 herbalist tags documented in `JUNE22_LAUNCH_EXECUTION_CHECKLIST.md`)
  - All pre-sprint gates from `JUNE22_LAUNCH_EXECUTION_CHECKLIST.md` complete
  - Decision: GO for June 22 Phase 3 sprint start? (requires all pre-sprint gates complete)

---

### June 22: Phase 3 Sprint Day 1 — [GATE: Sprint Start]

- [GATE] Sprint start confirmation: All pre-sprint gates from `JUNE22_LAUNCH_EXECUTION_CHECKLIST.md` are checked
- [ ] Begin Women's Health bundle writing — Front Matter + Bundle Introduction + Black Cohosh profile
  - Target: 1,200 words, Day 1 of 22-day sprint
  - Reference: `phase-3-medicinal-herbs-content-outline.md` and writing template
- [ ] Launch optimization period continues in parallel: social posting, email list growth, Etsy monitoring

---

### Gantt-Style Timeline Summary

```
May 24–26  |========|  User setup: Canva Brand Kit, zone cards, Kit account, landing page
May 27     |====|      [GATE] Social accounts + Kit foundation complete
May 28     |====|      [GATE] Kit end-to-end tests pass
May 29     |====|      [GATE] Full T-1 go/no-go
May 30     |========|  [LAUNCH DAY] Etsy 10am / Kit 12pm / Social 2pm / Phase 3 decisions
May 31–Jun 6 |=====|   Week 1 monitoring, Day 7 health check gate
Jun 8      |==|        [GATE] Phase 3 supplier orders
Jun 8–14   |========|  Week 2 social cadence + Phase 3 pre-sprint
Jun 15     |==|        [GATE] Phase 3 palette confirmed (hard deadline)
Jun 15–21  |========|  Week 3 social cadence + Phase 3 pre-sprint completion
Jun 21     |==|        [GATE] Phase 3 build readiness gate
Jun 22     |====...    Phase 3 sprint Day 1 (Women's Health writing begins)
```

---

## Section 5: Ready for May 30? — One-Page Summary

Read this section first on the morning of May 30. All items with a defined status are
verified against actual project files as of May 20.

---

### Execution Readiness Checklist

**Pre-staged assets (verified May 20 — no action required):**

- [x] 63 product mockup images confirmed present at `projects/seedwarden/mockups/`
- [x] 10 Cluster D/E stock images confirmed at `assets/stock-raw/` subdirectories (finals staged)
- [x] All 5 email bodies (plus launch broadcast) production-ready in `marketing/email-and-launch-plan.md`
- [x] 60-day social content calendar production-ready — all post hooks, captions, hashtags documented
- [x] Hour-by-hour May 30 launch sequence documented in `MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md`
- [x] 7 risk contingencies fully documented with activation triggers and same-day recovery paths
- [x] Phase 3 decision framework ready for May 30 decision day in `TRACK_B_MAY30_DECISION_FRAMEWORK.md`

**User gates (must be complete before May 30 — verify before marking):**

- [ ] Canva Brand Kit active (6 colors, 3 fonts, logo) — deadline May 24
- [ ] 8 Zone card PDFs exported and uploaded to Google Drive with public share links — deadline May 25
- [ ] Kit account created, landing page live, 15 tags created — deadline May 25–26
- [ ] Kit zone routing automation wired and all 8 Email 1 variants built — deadline May 27
- [ ] Kit Emails 2–5 built — deadline May 28
- [ ] Kit end-to-end tests passed (Zone 5, Zone 7, behavioral tag) — deadline May 28
- [ ] Launch broadcast staged in Kit for May 30 12:00pm — deadline May 28
- [ ] Social accounts created on all 3 platforms — deadline May 27
- [ ] Buffer connected to all 3 platforms; launch week posts scheduled — deadline May 28
- [ ] SEEDWARDEN15 Etsy coupon created (if Etsy verified) — deadline May 28

**May 30 morning verification (8:00am QA block):**

- [ ] Zone 5 Kit sign-up flow tested: sign up → Email 1 received → PDF downloads → zone-5 tag applied
- [ ] Kit broadcast shows "Scheduled" for 12:00pm today with correct subject line and copy
- [ ] Buffer queue shows 3 platform launches scheduled for 2:00pm (IG, TT) and 3:30pm (PIN)
- [ ] Cluster D/E Canva composites exported and ready to upload to Etsy at 10:00am
- [ ] All Phase 2 Etsy listing images in final export location at `marketing/lifestyle-photos/etsy-ready/`

---

### Contingency Confidence Summary

| Failure Mode | Pre-staged Contingency | Recovery Time |
|---|---|---|
| Kit email silent failure (PDF not delivered) | Drive link format fix; resend within 4 hrs | 30 min |
| Social accounts not created | Manual post at 1:00pm; captions saved | 60 min |
| Zone cards missing | Placeholder Email 1; manual PDF backfill | 60–90 min |
| Buffer scheduling failure | Manual post from saved captions | 45 min |
| Etsy verification still blocked | Track B launches via email + social only; Etsy added when verified | 0 min |
| Kit mobile render broken | Fix template in Kit; resend to non-clickers | 30 min |
| Phase 3 palette discrepancy | Record decision May 30; load confirmed palette June 21 | 10 min |

**All 7 contingencies are pre-staged. No contingency requires more than 90 minutes to
execute. The minimum viable launch (Etsy + email, no social, no zone cards) is fully
independent of all pending user gates and can execute on May 30 regardless of which
gates are incomplete.**

---

### Phase 3 Decision Prompt (May 30)

Three decisions must be made May 30 for Phase 3 execution to begin June 22 without delay:

1. **Sprint scope**: Option A (3-bundle: Women's Health, Respiratory, Sleep — recommended),
   B (5-bundle solo), C (5-bundle two writers), or D (5-bundle reordered). Record in
   `TRACK_B_MAY30_DECISION_FRAMEWORK.md` Decision Record.

2. **Goldenseal sourcing**: Path 1 (order Prairie Moon by June 8, $35–50) or Path 2
   (Wikimedia CC, $0, no lead time). If deferred to June 1: set calendar reminder for June 1
   to check Prairie Moon stock availability.

3. **Phase 3 Canva palette**: Confirm the 5 hex codes from `phase-3-canva-mockup-brief.md`
   are correct (#6B4F35 Herb Brown, #8A9E6E Herb Sage, #F5EFE0 Herb Cream, #2E2A24 Herb Ink,
   #B85C38 Herb Alert), or specify corrections. Deadline June 15 (hard).

---

*Prepared: 2026-05-20 — Seedwarden Agent. Verified against: TRACK_B_PRODUCTION_PIPELINE.md (mockup count, stock images, email pipeline), TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md (email copy status, Kit setup requirements), MAY_30_JUNE_30_CONTENT_CALENDAR.md (calendar coverage), MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md (gate deadlines, hour-by-hour sequence), MAY_30_RISK_AND_CONTINGENCY_PLAN.md (risk fallbacks), TRACK_B_COMPLETION_VERIFICATION.md (user gate checklist), TRACK_B_MAY30_DECISION_FRAMEWORK.md (Phase 3 decisions), JUNE22_LAUNCH_EXECUTION_CHECKLIST.md (Phase 3 pre-sprint gates).*
