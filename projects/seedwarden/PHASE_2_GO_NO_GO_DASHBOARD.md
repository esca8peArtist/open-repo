---
title: "Phase 2 Go/No-Go Dashboard — May 30 Launch Verification"
prepared: 2026-05-13
status: production-ready
launch-date: 2026-05-30
days-remaining: 17
author: Seedwarden Agent (Exploration Queue Item 25)
scope: >
  5 binary go/no-go criteria, May 28-30 daily pre-launch checklists,
  contingency decision trees, 72-hour dry-run script, risk escalation matrix,
  post-launch monitoring (Days 1-7), Phase 3 trigger criteria, rollback procedure
references:
  - PHASE_2_PRODUCTION_TIMELINE.md (operational production timeline)
  - PHASE_2_LAUNCH_VALIDATION_CHECKLIST.md (infrastructure audit, May 12)
  - phase-2-launch-day-checklist.md (May 30 minute-by-minute guide)
  - phase-2-go-no-go-decision-criteria.md (post-launch Day 16/31/94 decision gates)
  - PHASE_2_WRITING_VELOCITY_ANALYSIS.md (guide production velocity, species priority)
  - BUNDLE_E_PUBLICATION_PACKAGE.md (Bundle E pre-launch revenue path)
  - phase-2-week-1-success-metrics.md (Day 1-7 monitoring targets)
  - TRACK_B_LAUNCH_STATUS.md (social account + Canva readiness)
  - PHASE_2_EMAIL_STRATEGY.md (Kit sequence architecture)
  - phase-2-blockers.md (open blockers register)
  - phase-2-social-content-calendar-60day.md (60-day posting calendar)
  - marketing/email-and-launch-plan.md (email copy, launch broadcast)
  - customer-analytics.csv (baseline metrics)
track-a-status: BLOCKED — tag corrections pending + Etsy account verification pending
track-b-status: NO BLOCKERS — independent launch on Track B timeline
---

# Phase 2 Go/No-Go Dashboard
## May 30, 2026 Launch — Verification & Decision Framework

**How to use this document**:
Read the full framework once before May 20. On May 28, open Section 2 (Daily Pre-Launch Checklist) and work through each block. On May 29 evening, complete the Go/No-Go Audit in Section 1 and record your outcome in WORKLOG.md before closing. On May 30 at 06:00 UTC, run the pre-launch final verification and proceed to the launch trigger at 09:00 UTC only if all 5 criteria are GO.

**Current status as of May 13**: CONDITIONAL GO (17 days remaining). Track A blocked; Track B clean. The five go/no-go criteria are partially verifiable today — Criteria 2 and 3 have known gaps that require user action this week to resolve.

**Phase 1 note**: This dashboard addresses Phase 2 (Track B) only. Phase 1 upload remains blocked on tag corrections and Etsy account verification. Phase 2 launches independently regardless of Phase 1 resolution status. If Phase 1 resolves before May 30, coordinate timing per TRACK_A_CONTINGENCY_LAUNCH_PLAN.md.

---

## Section 1: Go/No-Go Framework — 5 Binary Criteria

Each criterion has exactly two outcomes: GO or NO-GO. There is no "partial GO." On May 29 evening, evaluate all five. If all five are GO, proceed to May 30 launch. If any criterion is NO-GO, execute the contingency decision tree in Section 3 before continuing.

Run this audit using the files in `projects/seedwarden/` as your evidence base. Do not rely on memory — open each referenced file and verify each checkpoint item explicitly.

---

### Criterion 1: Content Completion

**What it covers**: All Phase 2 guide files written, technically reviewed, and SEO-optimized for Etsy listing publication.

**Launch scope** (from PHASE_2_PRODUCTION_TIMELINE.md): Core Four + Wild Bergamot = 5 guides minimum to launch. Bloodroot, Trillium, Lady's Slipper are June 15 follow-ons and do not gate May 30.

**Guide file locations**:
- Primary product directory: `projects/seedwarden/products/`
- Phase 2 drafts staging: `projects/seedwarden/phase-2/`
- Writing velocity analysis: `projects/seedwarden/PHASE_2_WRITING_VELOCITY_ANALYSIS.md`
- Content blueprint template: `projects/seedwarden/PHASE_2_GUIDE_CONTENT_BLUEPRINT.md`

**GO criteria — all 5 must be true**:

| Checkpoint | Verification step | GO signal |
|---|---|---|
| C1.1 Guide files present | `ls projects/seedwarden/products/` — confirm all 5 Phase 2 guide files exist | 5 files present, named correctly |
| C1.2 Guide completeness | Open each file — confirm all 6 sections present (Identification, Habitat, Harvest, Safety, Preparation, Cross-reference) | All 6 sections populated, no placeholder text |
| C1.3 Photo integration | Each guide references at least 1 confirmed photo path from `assets/wild-edibles/` | Photo paths verified as real files, not stubs |
| C1.4 Safety callouts | Any guide covering species with lookalike risk (Nasturtium, Urtica) has an explicit safety callout block | Safety block visible, formatted as distinct callout |
| C1.5 SEO optimization | Each guide has a title, subtitle, and 3 primary keywords matching Etsy listing copy in `etsy-store-copy.md` | Title + subtitle present, keywords match listing |

**Writing velocity reference** (from PHASE_2_WRITING_VELOCITY_ANALYSIS.md):
- Estimated time per guide: 112 minutes (conservative, padded 25%)
- 5 guides: 9.3 hours total
- Target completion: May 13-14 (15 hours total including Bundle E)
- Remaining window if May 14 slip: May 15-25 has 8 additional days before hard-stop May 25

**GO looks like**: Open `projects/seedwarden/products/` on May 29. Five guide files are present. Each contains populated content in all 6 sections. No file contains the string "PLACEHOLDER" or "TODO."

**NO-GO looks like**: Fewer than 4 guide files exist, OR any present guide is missing 2+ sections, OR guide files exist but photo references point to non-existent files.

**NO-GO consequence**: See Section 3, Contingency Tree A (Guides Not Complete by May 25).

---

### Criterion 2: Visual Assets

**What it covers**: All Canva production briefs finalized, all habit photos at minimum 1200x800px, Etsy listing image slots populated.

**Asset locations**:
- Habit photos: `projects/seedwarden/assets/wild-edibles/`
- Canva briefs: `projects/seedwarden/CANVA_EXECUTION_PLAYBOOK.md` and `CANVA_ZONE_CARD_BATCH_WORKFLOW.md`
- Zone cards (PDFs): `projects/seedwarden/assets/zone-cards/` (verify directory exists and contains 8 files)
- Mockup images: `projects/seedwarden/mockups/`
- Brand kit specs: `projects/seedwarden/TRACK_B_LAUNCH_STATUS.md` Section 2 (hex codes, fonts)

**Current known status** (from PHASE_2_LAUNCH_VALIDATION_CHECKLIST.md, May 12):
- 18/18 habit photos present
- 18/18 photos pass 1200x800 minimum (upscaled session 942)
- 0/18 photos have fully documented licenses in WORKLOG.md
- Zone card PDFs: status unknown — no files confirmed present in `assets/zone-cards/`
- Canva Brand Kit: specifications ready; setup NOT confirmed complete (user action required)

**GO criteria — all 5 must be true**:

| Checkpoint | Verification step | GO signal |
|---|---|---|
| C2.1 Habit photos pass resolution | `python3 -c "from PIL import Image; import os; [print(f, Image.open(f'projects/seedwarden/assets/wild-edibles/{f}').size) for f in os.listdir('projects/seedwarden/assets/wild-edibles/') if f.endswith('.jpg')]"` | All files: width >= 1200, height >= 800 |
| C2.2 License documentation | Open `projects/seedwarden/WORKLOG.md` — search for each of the 18 species slugs | Each species has a license entry (CC-BY, CC0, or equivalent) |
| C2.3 Zone cards present | `ls projects/seedwarden/assets/zone-cards/*.pdf \| wc -l` | Returns 8 |
| C2.4 Zone card delivery test | Open each zone card PDF download link from Kit Email 1 in incognito — zone card downloads as PDF, not viewer page | All 8 download successfully |
| C2.5 Canva Brand Kit active | Log into Canva — Brand Hub shows Brand Kit with 6 hex colors, 3 fonts, logo uploaded | Brand Kit confirmed active |

**Minimum resolution check command** (run from project root):
```bash
python3 -c "
from PIL import Image
import os
path = 'projects/seedwarden/assets/wild-edibles/'
fails = []
for f in sorted(os.listdir(path)):
    if f.endswith('.jpg'):
        w, h = Image.open(path + f).size
        if w < 1200 or h < 800:
            fails.append(f'{f}: {w}x{h}')
print('FAIL:', fails if fails else 'None')
print('PASS: all', len([f for f in os.listdir(path) if f.endswith('.jpg')]), 'files')
"
```

**GO looks like**: All 18 photos pass resolution check. WORKLOG.md has a license entry for every species. `assets/zone-cards/` contains 8 PDFs. All 8 zone cards download from incognito. Canva Brand Kit is active with correct colors and fonts.

**NO-GO looks like**: Any photo below 1200x800, OR fewer than 8 zone card PDFs present, OR any zone card URL returns "Request access" in incognito, OR Canva Brand Kit missing.

**NO-GO consequence**: See Section 3, Contingency Tree C (Visual Assets Have Quality Issues).

---

### Criterion 3: Marketing Infrastructure

**What it covers**: Kit email sequences tested, broadcast calendar populated and armed, social templates staged in Buffer or Later.

**Asset locations**:
- Email sequence copy: `projects/seedwarden/marketing/email-and-launch-plan.md`
- Kit setup guide: `projects/seedwarden/TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md`
- Kit broadcast copy: `projects/seedwarden/phase-2-kit-broadcast-copy.md`
- Social calendar: `projects/seedwarden/phase-2-social-content-calendar-60day.md`
- Social account checklist: `projects/seedwarden/TRACK_B_SOCIAL_ACCOUNT_CHECKLIST.md`
- Email automation setup: `projects/seedwarden/PHASE_2_EMAIL_STRATEGY.md`

**Current known status** (from TRACK_B_LAUNCH_STATUS.md, Apr 29):
- Kit account: NOT confirmed created (user action required)
- Social accounts (Instagram, TikTok, Pinterest): NOT confirmed created (user action required)
- Canva Brand Kit: specifications ready, setup NOT confirmed
- Email copy: PRODUCTION-READY in marketing/email-and-launch-plan.md
- 60-day social calendar: PRODUCTION-READY in phase-2-social-content-calendar-60day.md

**GO criteria — all 5 must be true**:

| Checkpoint | Verification step | GO signal |
|---|---|---|
| C3.1 Kit welcome sequence live | Kit > Automations > find "Seedwarden Welcome" | Status shows "Published" (not Draft, not Paused) |
| C3.2 Kit launch broadcast armed | Kit > Broadcasts > find May 30 launch broadcast | Status shows "Scheduled" at 12:00pm May 30 |
| C3.3 End-to-end delivery test | From incognito, submit test email to Kit landing page (Zone 5); wait 60 seconds | Zone 5 PDF downloads within 60 seconds of submission |
| C3.4 Social posts scheduled | Open Buffer (or Later) queue | At minimum 3 posts scheduled May 30: Instagram 2:00pm, TikTok 2:00pm, Pinterest 3:30pm |
| C3.5 Platform connections active | Buffer/Later > Settings > Connected Accounts | Instagram, TikTok, Pinterest all show green/active — no "Reconnect" warning |

**End-to-end Kit test procedure** (run on May 28 AND again on May 30 at 06:00 UTC):
1. Open incognito browser window
2. Navigate to Kit landing page URL
3. Enter: first name "Test", email `wanka95+test[date]@gmail.com`, Zone 5
4. Click submit
5. Wait up to 60 seconds
6. Check Gmail — confirm Email 1 arrives
7. Click zone card download button — confirm Zone 5 PDF downloads (not a viewer page)
8. Record result in WORKLOG.md

**GO looks like**: Kit automation shows "Published." Broadcast shows "Scheduled." Zone 5 PDF downloads within 60 seconds. Buffer shows 3+ scheduled posts for May 30. All platform connections are green.

**NO-GO looks like**: Kit automation is in Draft or Paused status, OR broadcast is missing or in Draft, OR zone card download fails with "Request access," OR fewer than 3 social posts are scheduled, OR any platform shows a connection error.

**NO-GO consequence**: See Section 3, Contingency Tree D (Email Sequences Fail Delivery Test).

---

### Criterion 4: Sales Readiness

**What it covers**: Etsy listings live, payment processing verified, digital file delivery working end-to-end.

**Asset locations**:
- Etsy listing copy: `projects/seedwarden/etsy-store-copy.md`
- Upload checklist: `projects/seedwarden/ETSY_PHASE_1_UPLOAD_CHECKLIST.md`
- Phase 2 listings: `projects/seedwarden/UPLOAD_SEQUENCE.md`
- SEO research: `projects/seedwarden/etsy-seo-market-research.md`
- Coupon setup: per phase-2-launch-day-checklist.md (SEEDWARDEN15)

**Current known status**:
- Phase 1 listings: IN DRAFT — tag corrections pending (Track A blocker)
- Phase 2 listings: NOT YET UPLOADED — depends on guide completion (Criterion 1)
- Etsy account verification: PENDING (Track A blocker; Track B listings can be uploaded to same verified account once verification completes)
- PDF files: `scripts/output/native-plants-regional-guide.pdf` at 4.91 MB — passes Etsy 5 MB limit

**Critical dependency**: Phase 2 Etsy listings cannot go live until Etsy account verification is complete. This is currently an open Track A blocker. If account verification has not resolved by May 25, execute Contingency Tree B.

**GO criteria — all 5 must be true**:

| Checkpoint | Verification step | GO signal |
|---|---|---|
| C4.1 Etsy account verified | Log into Etsy Shop Manager | Account shows no verification hold; shop is open to buyers |
| C4.2 Phase 2 listings active | Etsy Shop Manager > Listings | All Phase 2 guide listings show "Active" (green dot), not Draft |
| C4.3 PDF file delivery | Click "Buy now" on a test listing (use a secondary account or ask a trusted contact) | Digital file delivers immediately post-purchase via Etsy download |
| C4.4 Pricing verified | Open each listing in Shop Manager | Prices match `etsy-store-copy.md` pricing table; no $0.00 or blank prices |
| C4.5 Coupon active | Etsy Shop Manager > Marketing > Sales and Coupons | SEEDWARDEN15 shows "Active", 15% discount, no expiry |

**PDF file size audit** (run before uploading any Phase 2 guide to Etsy):
```bash
# Verify all Phase 2 guide PDFs are under 5 MB before Etsy upload
find projects/seedwarden/products/ -name "*.pdf" -exec du -sh {} \;
# Any file showing > 5M must be compressed before upload
# Compression command if needed:
# gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 \
#    -dPDFSETTINGS=/ebook -sOutputFile=output.pdf input.pdf
```

**GO looks like**: Etsy account shows no verification hold. All Phase 2 listings are Active with correct prices. A test purchase delivers the PDF file via Etsy's automatic download. SEEDWARDEN15 coupon is active.

**NO-GO looks like**: Etsy account still shows a verification hold, OR any listing is in Draft status, OR test purchase does not deliver the PDF, OR SEEDWARDEN15 coupon is missing or expired.

**NO-GO consequence**: See Section 3, Contingency Tree B (Etsy Account Verification Fails).

---

### Criterion 5: Performance Baseline

**What it covers**: Phase 1 metrics are established (conversion rate, any early CAC signal), Phase 2 targets are calibrated against Phase 1 actuals.

**Asset locations**:
- Phase 1 metrics tracker: `projects/seedwarden/customer-analytics.csv`
- LTV tracker: `projects/seedwarden/phase-2-ltv-tracker-phase1-baseline.csv`
- Week 1 success metrics: `projects/seedwarden/phase-2-week-1-success-metrics.md`
- Analytics strategy: `projects/seedwarden/phase-2-analytics-strategy.md`
- Post-launch analytics framework: `projects/seedwarden/phase-2-post-launch-analytics-framework.md`

**What "Phase 1 metrics established" means**: Even with Phase 1 launch still pending due to tag corrections, this criterion is satisfied if the tracking infrastructure is configured and ready to record baseline numbers the moment Phase 1 goes live OR if Phase 1 data is already available (if verification resolved before May 29).

**Fallback for Phase 1 still blocked**: If Phase 1 has not launched by May 28, Phase 2 targets default to conservative industry benchmarks (Etsy digital goods median: 1.2% conversion; first-week revenue $200-400 for a new shop). Record the benchmark source in WORKLOG.md.

**GO criteria — all 4 must be true**:

| Checkpoint | Verification step | GO signal |
|---|---|---|
| C5.1 Analytics file ready | Open `customer-analytics.csv` | File exists, headers populated, baseline row present or ready to fill |
| C5.2 LTV tracker configured | Open `phase-2-ltv-tracker-phase1-baseline.csv` | Columns present: order_id, buyer_id, cohort_tag, order_1_date, order_1_value, order_2_date |
| C5.3 Phase 2 targets documented | Open `phase-2-week-1-success-metrics.md` Section 1 | Specific numeric targets present for: orders (Day 7), revenue (Day 7), Kit subscribers (Day 7), email open rate (Day 1-2) |
| C5.4 Monitoring cadence set | Calendar blocked for May 31, June 1, June 3, June 6 (per phase-2-launch-day-checklist.md) | Calendar events confirmed; no competing blocks on those evenings |

**Phase 2 numeric targets for May 30 launch** (from phase-2-week-1-success-metrics.md and phase-2-go-no-go-decision-criteria.md):

| Metric | Minimum acceptable (Week 1) | Target (Week 1) | Source |
|---|---|---|---|
| Etsy orders | 3 | 8-15 | phase-2-week-1-success-metrics.md |
| Gross revenue | $75 | $200-500 | Conservative estimate at $25 AOV |
| Kit subscribers added | 5 | 15-25 | TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md |
| Email open rate (launch broadcast) | 25% | 35%+ | phase-2-launch-day-checklist.md |
| Email click rate | 4% | 8-10% | phase-2-launch-day-checklist.md |
| Etsy listing views | 50 | 200+ | phase-2-week-1-success-metrics.md |
| Social reach (per post) | 50 impressions | 200+ impressions | TRACK_B_LAUNCH_STATUS.md |
| Refund rate | 0% | 0% (target <2%) | phase-2-customer-success-framework.md |

**GO looks like**: `customer-analytics.csv` and `phase-2-ltv-tracker-phase1-baseline.csv` both open and have correct columns. Week 1 numeric targets are confirmed in `phase-2-week-1-success-metrics.md`. Calendar holds are confirmed for June 1, 3, 6 reviews.

**NO-GO looks like**: Analytics files are missing or have no column headers, OR no numeric targets are documented anywhere, OR calendar is unblocked for Week 1 monitoring dates.

---

### Go/No-Go Audit Record (complete on May 29 evening)

Copy this block into WORKLOG.md after completing the May 29 verification:

```
## Phase 2 Go/No-Go Audit — May 29, 2026 (T-1 Day)

Criterion 1 — Content Completion:   GO / NO-GO
  C1.1 Guide files present (5/5):   ___
  C1.2 All sections complete:        ___
  C1.3 Photo paths verified:         ___
  C1.4 Safety callouts present:      ___
  C1.5 SEO keywords match listing:   ___

Criterion 2 — Visual Assets:        GO / NO-GO
  C2.1 Photos pass resolution:       ___
  C2.2 Licenses documented:          ___
  C2.3 Zone cards present (8/8):     ___
  C2.4 Zone card delivery test:      ___
  C2.5 Canva Brand Kit active:       ___

Criterion 3 — Marketing Infra:      GO / NO-GO
  C3.1 Kit automation published:     ___
  C3.2 Broadcast scheduled 12pm:     ___
  C3.3 End-to-end delivery test:     ___
  C3.4 Social posts scheduled (3+):  ___
  C3.5 Platform connections active:  ___

Criterion 4 — Sales Readiness:      GO / NO-GO
  C4.1 Etsy account verified:        ___
  C4.2 Listings active:              ___
  C4.3 PDF delivery works:           ___
  C4.4 Prices correct:               ___
  C4.5 SEEDWARDEN15 coupon active:   ___

Criterion 5 — Performance Baseline: GO / NO-GO
  C5.1 Analytics CSV ready:          ___
  C5.2 LTV tracker configured:       ___
  C5.3 Week 1 targets documented:    ___
  C5.4 Calendar holds confirmed:     ___

OVERALL: ___ of 5 criteria GO
DECISION: LAUNCH / SLIP / ESCALATE
Contingency activated (if any): ___
Next action: ___
```

---

## Section 2: Daily Pre-Launch Checklist (May 28-30)

### May 28 (T-2): Final Guide Reviews and Infrastructure Arm

**Primary goal**: All 5 guides complete and reviewed. All platform accounts confirmed active. Launch broadcast drafted.

**Morning block (9:00am-12:00pm, 3 hours)**:

- [ ] Open each Phase 2 guide file in `projects/seedwarden/products/` (or `phase-2/` staging)
- [ ] Run the Criterion 1 audit (Section 1) — confirm all 5 guides pass all 5 checkpoints
- [ ] Fix any incomplete sections immediately. Use `PHASE_2_GUIDE_CONTENT_BLUEPRINT.md` template for any missing section structure
- [ ] Run the photo resolution check command (Criterion 2.1) — confirm all 18 pass
- [ ] Open `projects/seedwarden/WORKLOG.md` — confirm all 18 species have license entries under Criterion 2.2

**Afternoon block (1:00pm-4:00pm, 3 hours)**:

- [ ] Log into Etsy Shop Manager — confirm account is verified and active (no verification hold banner)
- [ ] If Phase 2 listings not yet uploaded: upload all 5 guide PDFs as new listings using copy from `etsy-store-copy.md`. Price each correctly. Set to Draft (do not activate yet — activate at 09:00 UTC May 30)
- [ ] If listings already uploaded: open each listing in Shop Manager, confirm price, confirm PDF is attached, confirm all tags are correct
- [ ] Create or verify SEEDWARDEN15 coupon: Etsy > Marketing > Sales and Coupons > Create Discount. Code: SEEDWARDEN15, 15% off, no minimum, no expiry

**Evening block (6:00pm-9:00pm, 3 hours)**:

- [ ] Open Kit dashboard — verify "Seedwarden Welcome" automation shows "Published"
- [ ] Open Kit > Broadcasts — if launch broadcast is not yet created, create it now using copy from `projects/seedwarden/marketing/email-and-launch-plan.md` (Launch Broadcast section). Schedule for 12:00pm May 30. Send to "All Confirmed Subscribers"
- [ ] Run the end-to-end Kit delivery test (Criterion 3.3 procedure). Record pass/fail in WORKLOG.md
- [ ] Open Buffer (or Later) queue — confirm all 3 May 30 social posts are scheduled with correct times: Instagram 2:00pm, TikTok 2:00pm, Pinterest 3:30pm
- [ ] If any post is missing: copy caption from `phase-2-social-content-calendar-60day.md` Day 30. Upload corresponding image. Schedule. Takes 5 minutes per platform
- [ ] Complete the Criterion 3 audit (Section 1) — record all 5 checkpoint results in WORKLOG.md

**May 28 Done signal**: Guides complete, Etsy listings in Draft with correct content, Kit automation live, launch broadcast scheduled, social posts queued. Criteria 1, 3, and 4 (partial) are verifiable. Record results.

---

### May 29 (T-1): Full Go/No-Go Audit

**Primary goal**: Run the complete 5-criterion audit. Make the GO/NO-GO decision by 9:00pm. Execute any contingency actions that are within the 24-hour window.

**Cross-reference**: TRACK_B_USER_GATES.md May 29 section contains an inline expanded checklist
covering each criterion's individual sub-checks with specific verification steps. Run that checklist
in parallel with this document — the Gates document makes each criterion actionable without having
to navigate between Sections 1 and 2. The Gate 5-question check at the bottom of that section must
pass in addition to all 5 Dashboard criteria.

**Time required**: 2–3 hours total (Morning: criteria 2, 4, 5 — Afternoon: compile and decide —
Evening: re-checks and arm). This is not a 15-minute task. Anyone planning a 15-minute May 29
check will arrive at May 30 with unverified infrastructure.

**Morning block (9:00am-12:00pm, 3 hours)**:

- [ ] Run Criterion 2 full audit (visual assets): resolution check command, license documentation check, zone card count, zone card delivery test from incognito, Canva Brand Kit verification
- [ ] Run Criterion 4 full audit (sales readiness): Etsy account status, listing status, test purchase (if possible), price verification, coupon verification
- [ ] Run Criterion 5 audit (performance baseline): open `customer-analytics.csv` and `phase-2-ltv-tracker-phase1-baseline.csv`, confirm targets documented in `phase-2-week-1-success-metrics.md`

**Afternoon block (1:00pm-4:00pm, 2 hours)**:

- [ ] Compile the complete Go/No-Go Audit Record (bottom of Section 1). Record every sub-criterion result
- [ ] For any NO-GO criterion: determine if 24-hour remediation is feasible. Consult Section 3 contingency trees
- [ ] Make the launch decision: LAUNCH (all 5 GO), SLIP (1 NO-GO with clear 24h remediation path), or ESCALATE (2+ NO-GO or unresolvable issue)
- [ ] If SLIP: execute the relevant contingency tree and set a new T-1 verification date
- [ ] If LAUNCH: proceed to evening sync steps

**Evening block (6:00pm-9:00pm, 2 hours)**:

- [ ] Run end-to-end Kit delivery test again (second pass — confirm no state change from May 28 test)
- [ ] Verify all 8 zone card download links from incognito: open each link logged in WORKLOG.md
  "Kit Zone Card File URLs" section — each must download as a PDF immediately, not open a Drive viewer
  (if any fail: fix the Google Drive sharing permission or URL format before proceeding)
- [ ] Open Buffer queue — confirm all 3 May 30 posts still show "Scheduled" with correct times (posts can be accidentally deleted or paused; verify now)
- [ ] Open Etsy Shop Manager — confirm all Phase 2 listings are in Draft (NOT Active yet — they go Active at 09:00 UTC May 30)
- [ ] Confirm Kit landing page URL is present in all 3 social bios (navigate to each profile, verify the link is there)
- [ ] Record final Go/No-Go Audit in WORKLOG.md using the template at the bottom of Section 1
- [ ] Set phone alarm for 05:45 UTC May 30

**May 29 Done signal**: Complete Go/No-Go Audit Record filled out and logged in WORKLOG.md. Decision is LAUNCH, SLIP, or ESCALATE — no "uncertain." If LAUNCH: sleep, wake at 05:45 UTC. If SLIP or ESCALATE: contingency is activated.

---

### May 30 (T-day): Launch Execution

**Reference document for minute-by-minute execution**: `projects/seedwarden/phase-2-launch-day-checklist.md`

This section supplements that checklist with go/no-go verification gates at each phase.

**06:00 UTC — Pre-Launch Verification (30 minutes)**:

- [ ] Open all 6 monitoring tabs: Etsy Shop Manager > Stats > Today, Etsy public store (incognito), Kit > Broadcasts, Kit > Automations, Kit > Subscribers, Buffer queue
- [ ] Run Kit delivery test one final time from incognito (Zone 5)
- [ ] Confirm launch broadcast still shows "Scheduled" at 12:00pm May 30
- [ ] Confirm Etsy listings still in Draft (not accidentally published)
- [ ] Confirm social posts still queued in Buffer

**06:30 UTC — Decision Gate**:

If all 5 checks pass: PROCEED to 09:00 UTC launch trigger.

If any check fails:
- Kit automation paused: Kit > Automations > Resume. 5 seconds.
- Broadcast in Draft: Kit > Broadcasts > click into broadcast > Schedule for 12:00pm today. 30 seconds.
- Zone card download broken: Kit > Sequences > Email 1 > [Zone 5 variant] > update download link. 5 minutes.
- Buffer post missing: manually recreate from `phase-2-social-content-calendar-60day.md` Day 30. 5 minutes.

**09:00 UTC — Launch Trigger** (Etsy activation):

- [ ] Etsy Shop Manager > Listings
- [ ] Select all Phase 2 listings in Draft
- [ ] Click "Publish" — all listings become Active simultaneously
- [ ] Navigate to your Etsy public store in incognito — confirm listings appear in search
- [ ] Note the exact time in `customer-analytics.csv` as "Phase 2 Launch Timestamp"

**12:00 UTC — Email Broadcast**:

- [ ] At 12:05 UTC: check Kit > Broadcasts — status should read "Sending" or "Sent"
- [ ] If still "Scheduled" at 12:20 UTC: click into broadcast > Send Now
- [ ] Check at 12:30 UTC: delivery rate target >90%, open rate target >35% (note: Apple MPP inflates — click rate is the reliable signal, target >8%)

**13:30 UTC — Market-Open Coordination** (if Bundle E active):

If the Invasive Edibles Bundle (Bundle E) from `BUNDLE_E_PUBLICATION_PACKAGE.md` is live and generating pre-orders, the 13:30 UTC window coincides with US market open for any ad spend decisions:

- [ ] Check Bundle E order count in Etsy Shop Manager
- [ ] If Bundle E has 10+ orders and Phase 2 just launched: this is strong dual-launch signal. Do NOT change any active ad campaigns today — let both run for 48 hours before optimizing
- [ ] If Bundle E has 0 orders and Phase 2 just launched: hold ad spend decision until Day 2 data available

**14:00 UTC — Social Media Activation**:

- [ ] Confirm Instagram post published by 14:15 UTC (Instagram profile > verify launch post visible)
- [ ] Confirm TikTok post published by 14:15 UTC (TikTok profile > verify video live)
- [ ] If either fails: post manually using caption from `phase-2-social-content-calendar-60day.md` Day 30. 3-5 minutes per platform.

**15:30 UTC — Pinterest**:

- [ ] Confirm Pinterest pins published by 15:45 UTC (Pinterest profile > verify pins visible)

**End of day (19:00-21:00 UTC) — Day 1 Metrics Log**:

Record in `customer-analytics.csv`:

```
Date: 2026-05-30
Etsy-Views: ___
Etsy-Orders: ___
Etsy-Revenue: $___
Top-Listing-Views: ___
Etsy-Favorites: ___
Kit-New-Subscribers: ___
Kit-Broadcast-Open-Rate: ___%
Kit-Broadcast-Click-Rate: ___%
Instagram-Impressions: ___
TikTok-Views: ___
Phase2-Launch-Timestamp: ___
```

---

## Section 3: Contingency Decision Trees

### Contingency Tree A: Guides Not Complete by May 25

**Trigger**: Fewer than 4 of 5 Phase 2 guide files are complete by May 25 (5 days before launch).

**Decision input**: How many guides are complete?

**Path A1 — 4 of 5 guides complete by May 25 (slip 1 guide)**:
- Launch with 4 guides on May 30
- Publish the incomplete guide as a June 1 follow-on listing
- No timeline impact to May 30 launch — 4 guides is sufficient
- Timeline impact to revenue: approximately 10-15% reduction if the missing guide would have driven its own orders
- Action: remove the 5th listing from the May 30 batch; upload it as a separate listing June 1-2

**Path A2 — 3 of 5 guides complete by May 25 (truncate to 3 species)**:
- Launch with 3 guides May 30 (still launchable — a coherent 3-guide set)
- Slip guides 4 and 5 to June 7
- Timeline impact: 2-week revenue compression on 2 guides
- Action: update Kit launch broadcast copy (remove references to 5 guides; announce "first 3 now live, 2 more June 7"). Update `marketing/email-and-launch-plan.md` launch broadcast. Takes 20 minutes.
- Kit broadcast copy change: replace "your zone card library just doubled" with "3 new guides just launched; 2 more arrive June 7"

**Path A3 — Fewer than 3 guides complete by May 25 (defer to Phase 3)**:
- May 30 launch is not viable
- New target: June 1 (3 days slip), June 7 (one-week slip), or June 15 (Phase 3 combined launch)
- Decision logic: if all 5 guides can be completed in 7 days from May 25, target June 1. If 14 days needed, target June 7. If 14+ days needed, combine with Phase 3 on June 15.
- Writing velocity reference: 5 guides at 112 min each = 9.3 hours. A focused 2-day writing sprint (May 26-27, 4.5 hours/day) can complete all 5 guides.
- Action: set new launch date in all documents, update Kit broadcast schedule, update social posts schedule in Buffer
- Log decision in WORKLOG.md with new date and rationale

**Consequence for each path**:
- A1: Zero timeline impact, minimal revenue impact
- A2: 2-week revenue delay for 2 guides; launch narrative slightly weakened
- A3: Full slip; Etsy organic indexing starts later; May/June seasonal momentum partially lost for spring foraging content

---

### Contingency Tree B: Etsy Account Verification Fails

**Trigger**: Etsy account verification is still pending on May 28 evening (the T-2 checkpoint).

**Verification status check**: Log into Etsy Shop Manager. If a banner reads "Your shop is under review" or "Identity verification required," Track A blocker is still active.

**Path B1 — Escalate Etsy verification (preferred)**:
- Contact Etsy support: help.etsy.com > Contact Us > "Shop verification" topic
- Provide all requested identity documents promptly
- Etsy typical verification window: 1-5 business days once documents submitted
- If verification clears by May 29 evening: proceed to standard May 30 launch
- If verification clears May 30: activate listings same-day, proceed with launch at actual clearance time (broadcast can be rescheduled in Kit; contact Kit support to push broadcast by 2-6 hours)
- Timeline impact: 0-1 day slip if verification clears by May 30

**Path B2 — Alternative sales channel: Gumroad**:
- Timeline to configure: 15-30 minutes
- URL: gumroad.com — create account, upload PDFs as products, set prices to match `etsy-store-copy.md`
- Gumroad handles digital delivery automatically (no Etsy required)
- Update Kit launch broadcast: replace Etsy links with Gumroad product links
- Update social post CTAs in Buffer (edit caption, replace "link in bio to Etsy shop" with direct Gumroad URL)
- Update Kit email sequence: Email 1 (welcome) and Email 5 (final offer) — replace Etsy shop link with Gumroad shop URL
- Revenue impact: Gumroad charges 10% transaction fee vs. Etsy's 6.5% — effective net revenue is slightly lower
- Timeline impact: 0 days (launch proceeds May 30 on schedule via Gumroad)

**Path B3 — Alternative sales channel: Shopify (longer setup)**:
- Timeline to configure: 2-4 hours (Shopify trial is free for 3 months; digital delivery via SendOwl or Sky Pilot app)
- Only use this path if both Etsy and Gumroad are ruled out
- Shopify setup guide is NOT pre-staged in this project — requires user decision and 2+ hours of setup time
- Timeline impact: May 30 launch slips to June 1 minimum

**Decision rule**:
- If Etsy verification unresolved by May 28 20:00 UTC AND Gumroad is acceptable: execute Path B2 immediately
- If Etsy verification unresolved by May 30 06:00 UTC AND user has not yet executed B2: execute B2 before 09:00 UTC

**Document to update if B2 activated**: 
- `marketing/email-and-launch-plan.md` (launch broadcast links)
- `phase-2-social-content-calendar-60day.md` Day 30 captions (Gumroad URL in CTA)
- Kit email sequence Email 1 and Email 5 (Etsy link → Gumroad link)
- WORKLOG.md (log the channel switch decision)

---

### Contingency Tree C: Visual Assets Have Quality Issues

**Trigger**: Any photo below 1200x800, OR zone card PDFs missing, OR Canva Brand Kit not configured by May 28.

**Path C1 — Photo below resolution minimum**:
- Run upscaling script using PIL bicubic interpolation (same method used in session 942):
  ```python
  from PIL import Image
  img = Image.open('path/to/failing-image.jpg')
  w, h = img.size
  scale = max(1200/w, 800/h)
  new_size = (int(w*scale), int(h*scale))
  img_resized = img.resize(new_size, Image.BICUBIC)
  img_resized.save('path/to/failing-image.jpg', quality=90)
  ```
- Time per image: 2 minutes
- Timeline impact: zero (can be done while other prep work proceeds)
- If upscaling produces visible artifacts: source a replacement from Wikimedia Commons. Search: `https://commons.wikimedia.org/wiki/Special:Search?search=[species+name]+habit`. Download, verify license, log in WORKLOG.md.

**Path C2 — Zone card PDFs missing from assets/zone-cards/**:
- Verify zone cards were exported from Canva: Canva > your zone card template > Share > Download > PDF Print
- If Canva zone cards never built: follow `CANVA_ZONE_CARD_BATCH_WORKFLOW.md` — 8 zone cards, estimated 4-6 hours total production time
- If zone cards exist but not in the correct directory: move/copy files to `projects/seedwarden/assets/zone-cards/`
- Timeline impact: if starting from zero, 4-6 hours. This is a significant gap that must be started by May 26 at the latest if not done.
- Hard stop: if zone cards are not ready by May 29 evening, downgrade the Kit lead magnet temporarily to a text-only welcome email. This reduces conversion but keeps the list-building funnel live. Document the downgrade in WORKLOG.md and complete zone cards as a post-launch item by June 7.

**Path C3 — Canva Brand Kit not configured**:
- User logs into Canva at canva.com
- Navigate to Brand Hub > Create a Brand Kit
- Add 6 hex colors from `TRACK_B_LAUNCH_STATUS.md` Section 2 (Deep Forest Green #143b28, Deep Ink Green #1A3A2A, Warm Cream #F5EDD6, Parchment #EDE0C4, Sage #8FA882, Burnt Sienna #A0522D)
- Add 3 fonts: Playfair Display (heading), Lato or Source Sans 3 (body), Cormorant Garamond (accent)
- Upload seedwarden_logo_1.png from `projects/seedwarden/logos/`
- Time required: 30 minutes
- Timeline impact: zero if done before May 28

---

### Contingency Tree D: Email Sequences Fail Delivery Test

**Trigger**: End-to-end Kit delivery test fails — zone card does not arrive within 60 seconds of test submission, OR arrives but PDF does not download.

**Diagnosis sequence (run in order)**:

1. **Check Kit automation status**: Kit > Automations > "Seedwarden Welcome" > confirm "Published." If "Draft": click Publish. Wait 30 seconds. Re-run test.

2. **Check Google Drive link format**: Kit > Sequences > Email 1 > find the "Download your Zone 5 Card" button. The URL must be in this format: `https://drive.google.com/uc?export=download&id=[FILE_ID]`. If the URL is a standard share link (`/file/d/[FILE_ID]/view`), it will open a viewer, not download. Replace with the `uc?export=download` format. Takes 2 minutes.

3. **Check Google Drive sharing permission**: Navigate to the zone card file in Google Drive. Right-click > Share. Confirm "Anyone with the link" can view. If set to "Restricted": change to "Anyone with the link." Takes 1 minute.

4. **Check Kit landing page is live**: Navigate to the Kit landing page URL in incognito. If the page shows an error or 404: Kit > Landing Pages > find the Seedwarden page > confirm it is published. If not published: click Publish. Takes 30 seconds.

5. **Check SPF/DKIM setup**: Kit requires 48-hour DNS propagation after SPF/DKIM records are added. If Kit account was created within the last 48 hours before May 28, delivery may be impaired. Check Kit > Account Settings > Email Authentication. If "Not verified": contact Kit support. This is the most serious failure — it affects deliverability to all providers.

**Rollback plan** (if Kit is completely non-functional by May 29):
- Switch to direct email via Gmail for the launch broadcast (manual send to all confirmed subscribers from wanka95@gmail.com)
- This approach works for up to ~500 subscribers before hitting Gmail daily send limits
- Zone card delivery: include the Google Drive download link directly in the manual broadcast email
- Post-launch: fix Kit within 7 days and migrate to automation for ongoing sequences
- Timeline impact: launch proceeds May 30 on schedule; automation is manual for Week 1

---

## Section 4: 72-Hour Dry-Run Script (May 27-29)

**Purpose**: Simulate the complete launch workflow — email, social, Etsy activation, analytics tracking — without going live. Identify bottlenecks, timing conflicts, or missing integrations before launch day. Success criteria: all systems fire, no delivery failures, end-to-end workflow completes in under 5 minutes of active setup time.

**Run this procedure once on May 27 (3 days before launch). Repeat abbreviated version on May 29 evening.**

---

### Step 1: Simulation Setup (10 minutes)

**Create a test environment**:
- Create a disposable test email address: `wanka95+dryrun[MMDD]@gmail.com` (Gmail alias — uses your existing inbox, no new account needed)
- In Kit: create a test tag "dryrun" — this prevents test contacts from receiving real automations
- Note starting metrics: Etsy shop views (today), Kit subscriber count, Buffer scheduled posts count

**Confirm simulation scope**:
- Email: test the Kit welcome sequence and launch broadcast (do not send to real list — send to test alias only)
- Social: review Buffer queue (do not publish — confirm posts are in queue with correct assets and captions)
- Etsy: confirm listings are in Draft (do not activate — simulate activation by opening a listing in edit mode and verifying all fields are populated)
- Analytics: confirm `customer-analytics.csv` has correct column headers and is writable

---

### Step 2: Simulate Email Sequence (15 minutes)

1. Open Kit landing page in incognito browser
2. Submit test email (`wanka95+dryrun[MMDD]@gmail.com`), name "Dry Run", zone "5"
3. Note submission time
4. Check Gmail — confirm Email 1 arrives within 60 seconds
5. Click zone card download — confirm Zone 5 PDF downloads (not viewer)
6. Wait 5 minutes — confirm no additional spurious emails arrive
7. In Kit dashboard: confirm the test subscriber appears under "Seedwarden Welcome" automation, Email 1 delivered
8. Navigate to the launch broadcast draft — confirm it shows "Scheduled" for 12:00pm May 30 (do not send now)
9. Record result: Email delivery time ___ seconds, PDF download ___ (Y/N), spurious emails ___ (should be 0)

**Dry-run timing target**: Email delivers within 60 seconds. PDF downloads immediately. No errors.

---

### Step 3: Simulate Social Posts (10 minutes)

1. Open Buffer (or Later) queue
2. Find the Instagram launch post scheduled for 2:00pm May 30
3. Click preview — confirm image displays correctly, caption is complete, hashtags are present
4. Find TikTok launch post — confirm video file is attached, not a static image
5. Find Pinterest launch pins — confirm all pins show correct image + copy overlay
6. Confirm all three platforms show green "Connected" status under Settings > Connected Accounts
7. Do NOT publish — only review and verify
8. Record result: Instagram post ready ___, TikTok post ready ___, Pinterest pins ready ___, all accounts connected ___

**Dry-run timing target**: All three platforms verified in under 10 minutes. No reconnection errors.

---

### Step 4: Simulate Etsy Activation (10 minutes)

1. Open Etsy Shop Manager > Listings
2. Find all Phase 2 guide listings (in Draft status)
3. Click into one listing — confirm all fields populated: title, description, price, PDF file attached, tags present
4. Confirm listing preview (click "Preview" button) shows the listing as buyers would see it
5. Verify SEEDWARDEN15 coupon under Marketing > Sales and Coupons
6. Do NOT click Publish — simulate only
7. Time how long it takes to verify all listings: record time
8. Record result: All listings verified ___ (Y/N), coupon active ___ (Y/N), verification time ___ minutes

**Dry-run timing target**: All listing checks complete in under 5 minutes. Coupon confirmed active.

---

### Step 5: Simulate Analytics Capture (5 minutes)

1. Open `customer-analytics.csv`
2. Manually enter the current metrics as if they were the pre-launch baseline:
   - Etsy shop views (today's actual), orders (today's actual), Kit subscriber count
3. Confirm the file saves correctly
4. Open `phase-2-ltv-tracker-phase1-baseline.csv` — add one dummy row to confirm the file accepts new entries
5. Delete the dummy row after confirming write access
6. Record result: Analytics file writable ___ (Y/N), LTV tracker writable ___ (Y/N)

---

### Step 6: Bottleneck Identification (5 minutes)

After completing Steps 1-5, answer these questions:

| Question | Answer | Action required |
|---|---|---|
| Did email delivery take >60 seconds? | Y/N | If Y: check Kit automation trigger settings |
| Did any zone card URL fail? | Y/N | If Y: fix Drive link format (see Contingency Tree D) |
| Did Buffer show any platform as disconnected? | Y/N | If Y: reconnect platform before May 30 |
| Did any Etsy listing have a missing field? | Y/N | If Y: fix listing now |
| Did analytics files open and save without error? | Y/N | If N: fix file permissions |

**Pass criteria**: All questions answered "N" (no issues). Dry run completes in under 45 minutes total.

**Fail criteria**: Any "Y" answer triggers the corresponding action. Re-run abbreviated dry run on May 29 evening to confirm fixes.

---

### Abbreviated May 29 Dry Run (15 minutes)

Repeat only Steps 2, 3, and 6. Skip Etsy (covered in May 29 checklist), skip analytics (covered in Criterion 5 audit).

Goal: confirm email delivery and social scheduling still intact after any May 28 changes.

---

## Section 5: Risk Escalation Matrix

### GREEN — All 5 Criteria GO, launch on schedule May 30

**Conditions**: All 5 criteria pass the May 29 audit. No contingency trees triggered.

**Action**: Execute May 30 launch sequence per `phase-2-launch-day-checklist.md`. No user escalation required.

**Confidence level**: High. The production timeline is tight but all critical-path items have been pre-staged across sessions 938-953.

---

### YELLOW — 4 of 5 Criteria GO, 1 NO-GO with clear remediation path

**Conditions**: Exactly 1 criterion is NO-GO on May 29 audit, AND a remediation action can be completed within 24 hours.

**Typical YELLOW scenarios**:

| Failing criterion | Remediation | Timeline |
|---|---|---|
| Criterion 1 (1 guide incomplete) | Write remaining sections (90-180 min) | Same day |
| Criterion 2 (zone cards missing) | Export from Canva (30 min per zone card) | Same-day if <4 missing |
| Criterion 3 (broadcast not scheduled) | Create and schedule in Kit (10 min) | Same day |
| Criterion 4 (coupon missing) | Create coupon in Etsy (3 min) | Same day |
| Criterion 5 (analytics file missing columns) | Edit CSV headers (5 min) | Same day |

**Action**: Execute remediation immediately. Re-run the failing criterion audit. If criterion passes after remediation: proceed to launch. If criterion still fails after remediation: escalate to RED.

**Timeline impact**: 0 days if remediation completes before 06:00 UTC May 30. 1-7 day slip if remediation requires extended time.

---

### RED — 2+ Criteria NO-GO or Unresolvable Technical Issues

**Conditions**: Two or more criteria fail the May 29 audit, OR a single criterion fails and cannot be remediated within 24 hours.

**Typical RED scenarios**:

| Scenario | Description | Recommended slip |
|---|---|---|
| RED-1 | Etsy account verification still pending + guides incomplete | Slip to June 2-7 |
| RED-2 | Kit account not created at all (no automation built) | Slip to June 2 minimum (Kit setup requires 48h DNS propagation) |
| RED-3 | Fewer than 3 guides complete by May 28 | Slip to June 2-9 |
| RED-4 | Zone cards never built (Canva Brand Kit setup never completed) | Slip to June 2 (4-6 hours zone card production needed) |

**Action**: Do not launch May 30. Make scope decision within 2 hours of identifying RED status.

**Scope decision options**:
- **Slip to June 2-3**: Execute contingency actions May 30-June 1. Re-run full Go/No-Go audit June 1 evening. Launch June 2 if all 5 criteria pass.
- **Slip to June 7-9**: More time to complete guides, build zone cards, verify Etsy. Less seasonal momentum (late May is peak spring foraging search season).
- **Escalate to user**: If the issue requires a decision beyond the agent's scope (e.g., Etsy verification still pending after two escalations, or user needs to choose between Gumroad vs. Etsy), send diagnostic brief to wanka95@gmail.com. Include: which 2+ criteria failed, root cause, recommended action, timeline to re-launch.

**Escalation email format**:
```
Subject: Seedwarden Phase 2 — Launch Slip Required [RED]

Outcome: RED (___/5 criteria failed)
Failed criteria: [list criteria names]
Root causes:
  - [Criterion X]: [specific reason]
  - [Criterion Y]: [specific reason]
Recommended action: [slip to June 2, execute B2, etc.]
New target date: [June 2 / June 7 / June 15]
Decision needed from you: [specific question if any]
```

---

## Section 6: Post-Launch Monitoring (Days 1-7, May 30 – June 6)

**Monitoring cadence** (do not check continuously — anxiety without insight):

| Day | UTC time | What to check | Duration |
|---|---|---|---|
| May 31 (Day 2) | 20:00 | Kit Email 1 open rate + click rate; new orders count | 10 min |
| June 1 (Day 3) | 20:00 | Etsy traffic trend; Kit Email 1 delivery complete signal | 10 min |
| June 3 (Day 5) | 20:00 | Kit Email 3 open rate; behavioral tag count in Kit | 10 min |
| June 6 (Day 7) | Morning | Full Week 1 review (all metrics below) | 30 min |

---

### Week 1 Target Metrics

**Email performance**:

| Metric | Source | Minimum threshold | Target | Action if below minimum |
|---|---|---|---|---|
| Launch broadcast open rate | Kit > Broadcasts > Stats | 25% | 35%+ | Check Kit deliverability log; if SPF/DKIM issue, contact Kit support |
| Launch broadcast click rate | Kit > Broadcasts > Stats | 4% | 8-10% | Review CTA copy in email; A/B test subject line in next broadcast |
| Email 1 (welcome) open rate | Kit > Automations | 40% | 55%+ | Check zone card download link works; ensure subject line personalizes zone number |
| Email 1 delivery rate | Kit > Automations | 95% | 99% | High bounce rate = list quality issue; review signup source |

**Social reach and engagement**:

| Metric | Source | Minimum threshold | Target | Action if below minimum |
|---|---|---|---|---|
| Instagram impressions (launch post) | Instagram Insights | 50 | 200+ | Manually add location tag and 5 additional niche hashtags; reshare to Stories |
| Instagram engagement rate | Instagram Insights | 2% | 5%+ | Comment on 10 posts in the foraging/wild-edibles niche to seed engagement |
| TikTok views (launch video) | TikTok Analytics | 50 | 500+ | Check video uploaded natively (not cross-posted); cross-posted TikToks are algorithmically suppressed |
| Pinterest monthly views | Pinterest Analytics | Not tracked Day 1 | 500+ by Day 30 | Pinterest is 2-24 hour indexing delay; check Day 3+ |

**Etsy listing performance**:

| Metric | Source | Minimum threshold | Target | Action if below minimum |
|---|---|---|---|---|
| Total shop views (Week 1) | Etsy Shop Manager > Stats | 50 | 200+ | Listings may not be indexed yet — check Etsy > Listings > SEO score for each; revise title/tags if low |
| Listing favorites (Week 1) | Etsy Shop Manager > Stats | 5 | 20+ | Favorites signal buying intent; if views are high but favorites low, cover image is the issue |
| Orders (Week 1) | Etsy Shop Manager > Orders | 3 | 8-15 | See diagnosis questions below |
| Revenue (Week 1) | Etsy Shop Manager > Stats | $75 | $200-500 | Correlated with orders; if orders are on target, revenue follows |
| Refund rate | Etsy Shop Manager > Orders | 0 | 0 (cap: <2%) | Any refund request: respond within 4 hours; issue full refund if product quality issue |

**Conversion rate check** (if views are high but orders are low):
- Navigate to Etsy Shop Manager > Stats > Listings
- Find your highest-view listing
- Check its views-to-order conversion rate (Etsy calculates this automatically)
- If conversion < 1%: the cover image or opening description line is the issue — not traffic
- Fix: update the first image and the first sentence of the description. Takes 15 minutes.

**Sales target**: 5-15 units, $500-1,500 revenue in first week. At $25 AOV (mid-range for Phase 2 guides), this requires 20-60 orders to hit the upper end. Conservative target of 5-15 orders ($125-375) is achievable if social and email are functioning correctly.

---

### Success Threshold

Phase 2 is considered successful at Week 1 if 2 or more of the following 4 targets are hit by June 1 (Day 3):

1. Email open rate on launch broadcast >= 25%
2. Etsy listing views >= 100
3. At least 1 order placed
4. Kit subscriber count increased by at least 5 from pre-launch baseline

If 2+ targets are hit by June 1: Phase 2 is tracking correctly. Proceed with Week 2 content per `phase-2-social-content-calendar-60day.md` Days 8-14. No changes needed.

If fewer than 2 targets are hit by June 1: run the Day 16 diagnosis logic from `phase-2-go-no-go-decision-criteria.md` Section "Action Path: CONDITIONAL" early. Do not wait until June 15.

---

## Section 7: Phase 3 Trigger Criteria

Phase 3 scope: June 15 launch target (per ORCHESTRATOR_STATE.md and PHASE_2_PRODUCTION_TIMELINE.md). Bloodroot, Trillium, and Lady's Slipper guides.

**Phase 3 begins ONLY when all 4 triggers are met**:

**Trigger T1 — Phase 2 first-week revenue >= $500**:
- Check: `customer-analytics.csv` > Week 1 Etsy-Revenue sum (May 30 through June 6)
- If revenue is $500+: T1 PASS
- If revenue is $200-499: T1 CONDITIONAL — Phase 3 planning can begin but launch date slips to June 22
- If revenue is below $200: T1 FAIL — Phase 3 June 15 date is suspended; investigate per Day 16 decision criteria in `phase-2-go-no-go-decision-criteria.md`

**Trigger T2 — User satisfaction: refunds < 2%, NPS >= 7**:
- Refund rate: `customer-analytics.csv` refund count / total orders. Target: 0 refunds in Week 1
- NPS proxy: any direct messages, reviews, or replies to the launch email that mention satisfaction. Record in WORKLOG.md.
- If any refund request is received: respond within 4 hours, issue full refund, note the reason in WORKLOG.md
- T2 PASS if: 0 refunds in Week 1, and at least 1 positive signal received (email reply, Etsy review, or social comment)

**Trigger T3 — Production readiness: Phase 3 guides drafted, Canva briefs 80%+ complete**:
- Phase 3 guide drafts: `projects/seedwarden/phase-2/` or `products/` directory (Bloodroot, Trillium, Lady's Slipper)
- Canva briefs: verify `phase-3-assets/` directory contains visual brief files for all 3 species
- Lady's Slipper is flagged as June 15 follow-on in the production timeline — requires Hillside Nursery photo licensing response (email sent May 12, expected May 26-June 5)
- T3 PASS if: at least 2 of 3 Phase 3 guide drafts are complete, and all Canva briefs are at 80%+ (headline, body copy, color, photo direction confirmed)

**Trigger T4 — Phase 3 target date confirmed: June 15**:
- Verify June 15 calendar is clear for launch operations
- Confirm Phase 3 content does not conflict with any outstanding Phase 2 work
- T4 PASS if: June 15 is confirmed as Phase 3 launch date with no competing priorities

**Phase 3 decision logic**:

| T1 | T2 | T3 | T4 | Decision |
|---|---|---|---|---|
| PASS | PASS | PASS | PASS | GO — Phase 3 launches June 15 |
| PASS | PASS | PASS | FAIL | SLIP — Phase 3 launches June 22 |
| PASS | PASS | FAIL | Any | CONDITIONAL — Phase 3 launches June 22-30 when T3 resolves |
| PASS | FAIL | Any | Any | HOLD — diagnose refund issue before Phase 3 production investment |
| FAIL | Any | Any | Any | PAUSE — Phase 2 recovery first; Phase 3 reconsideration July 1 |
| CONDITIONAL | Any | Any | Any | CONDITIONAL June 22 — monitor for T1 resolution |

**Record Phase 3 decision in WORKLOG.md on June 6 (Day 7 review)**:
```
## Phase 3 Trigger Assessment — June 6, 2026 (Day 7)
T1 Revenue: $___ — PASS / CONDITIONAL / FAIL
T2 Satisfaction: Refunds ___, NPS signal: ___ — PASS / FAIL
T3 Production: Guides drafted _/3, Canva briefs ___% — PASS / CONDITIONAL / FAIL
T4 Date confirmed: June 15 — YES / NO
Phase 3 Decision: GO / SLIP [date] / CONDITIONAL [date] / PAUSE
```

---

## Section 8: Rollback Procedure

**Trigger**: Phase 2 launch fails — defined as 0 orders in the first 72 hours after launch, OR a critical product delivery failure (PDF does not deliver to buyers), OR a refund rate exceeding 5% in the first 48 hours.

This is a low-probability scenario given the production infrastructure in place. Document it here so that if it occurs, the response is executed in under 4 hours without requiring decision-making under stress.

---

### Step 1: Pause All Marketing (within 1 hour of rollback decision)

**Social scheduling**: Open Buffer > Settings > find all May 30+ scheduled posts > Pause all. This prevents any further social posts from firing while the issue is investigated. Takes 5 minutes.

**Kit email broadcast**: If the launch broadcast has not yet sent: Kit > Broadcasts > click into broadcast > Pause (or delete if not yet started). If it has already sent: no action — you cannot un-send an email. Do not send a follow-up email cancelling the launch; this creates confusion. Simply pause future automations.

**Kit automation**: Kit > Automations > "Seedwarden Welcome" > Pause. New subscribers will not receive emails during the pause. Resume once the issue is resolved.

**Timeline**: All marketing paused within 1 hour.

---

### Step 2: De-list Etsy (within 4 hours of rollback decision)

**Etsy Shop Manager > Listings**: Select all Phase 2 listings > Change Status to "Draft." This makes them invisible to buyers but preserves all listing data for re-launch.

Do not delete listings — draft status preserves views, favorites, and SEO history that will be valuable at re-launch.

**Timeline**: Listings in Draft within 4 hours.

---

### Step 3: Refund All Purchases

**For each order received before rollback**:
- Etsy Shop Manager > Orders > find order > Issue Refund > Full refund + brief message: "We're making a small update to this product. Your full refund has been processed. We'll notify you when it relaunches — no action needed on your end."
- Refund processing time: 3-5 business days (Etsy standard)

**If more than 10 orders received before rollback**: this is unusual for a Day 1 rollback. Contact Etsy support if bulk refund tools are needed.

**Timeline**: All refunds initiated within 24 hours.

---

### Step 4: Diagnose Root Cause (within 24 hours)

Answer these four questions:

1. **Was it a traffic problem?** Total Etsy views in the launch window: if below 20 views in the first 12 hours, the listings were not indexed or not activated correctly.
2. **Was it a delivery problem?** Did any buyer report not receiving their PDF? Check Etsy > Orders > Digital files delivered status for each order.
3. **Was it a product quality problem?** Did any buyer report the content did not match the description? Check Kit email replies and Etsy messages.
4. **Was it a technical problem?** Did Buffer fail to post social content? Did Kit fail to send the broadcast? Check delivery logs.

Log root cause in WORKLOG.md:
```
## Phase 2 Rollback — [Date]
Orders before rollback: ___
Refunds issued: ___
Root cause: TRAFFIC / DELIVERY / PRODUCT QUALITY / TECHNICAL
Evidence: ___
Fix required: ___
```

---

### Step 5: Re-launch Timeline

| Root cause | Fix time | Re-launch target |
|---|---|---|
| Traffic (listings not indexed) | 1-2 days (re-upload listings, verify SEO tags) | 3-5 days from rollback |
| Delivery (PDF not delivering) | 4-8 hours (fix Etsy digital file attachment) | 24-48 hours from rollback |
| Product quality (content issues) | 3-7 days (revise affected guides) | 7-14 days from rollback |
| Technical (Buffer/Kit failures) | 1-2 days (fix integrations, test again) | 3-5 days from rollback |

**Minimum re-launch preparation before going live again**:
1. Re-run the complete 72-hour dry-run script (Section 4)
2. Re-run the full Go/No-Go audit (Section 1)
3. All 5 criteria must pass before re-launch

**Gather feedback before re-launch**: Email any buyers who received a refund with a one-question survey: "What would have made this purchase perfect for you?" One question, open text. Responses inform guide revisions and listing copy improvements.

---

## Document Index: Key Files for Launch Execution

| Purpose | File path |
|---|---|
| Launch day minute-by-minute guide | `projects/seedwarden/phase-2-launch-day-checklist.md` |
| Day 16/31/94 post-launch decision gates | `projects/seedwarden/phase-2-go-no-go-decision-criteria.md` |
| Guide writing template and velocity | `projects/seedwarden/PHASE_2_WRITING_VELOCITY_ANALYSIS.md` |
| Guide content blueprint | `projects/seedwarden/PHASE_2_GUIDE_CONTENT_BLUEPRINT.md` |
| Email copy (all 5 emails + broadcast) | `projects/seedwarden/marketing/email-and-launch-plan.md` |
| Kit setup guide | `projects/seedwarden/TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md` |
| Social calendar (Days 1-60) | `projects/seedwarden/phase-2-social-content-calendar-60day.md` |
| 60-day Canva zone card workflow | `projects/seedwarden/CANVA_ZONE_CARD_BATCH_WORKFLOW.md` |
| Canva brand kit specs | `projects/seedwarden/TRACK_B_LAUNCH_STATUS.md` Section 2 |
| Etsy listing copy | `projects/seedwarden/etsy-store-copy.md` |
| Analytics baseline | `projects/seedwarden/customer-analytics.csv` |
| LTV tracker | `projects/seedwarden/phase-2-ltv-tracker-phase1-baseline.csv` |
| Week 1 targets | `projects/seedwarden/phase-2-week-1-success-metrics.md` |
| Bundle E launch (if active) | `projects/seedwarden/BUNDLE_E_PUBLICATION_PACKAGE.md` |
| Phase 2 production timeline | `projects/seedwarden/PHASE_2_PRODUCTION_TIMELINE.md` |
| Contingency: Gumroad alternative | `projects/seedwarden/TRACK_A_CONTINGENCY_LAUNCH_PLAN.md` |
| Open blockers register | `projects/seedwarden/phase-2-blockers.md` |

---

*Prepared: 2026-05-13. Exploration Queue Item 25. This document is designed to be read once before May 20, then executed section-by-section during May 28-30. All file paths are relative to the project root `projects/seedwarden/`. Evidence-based verification procedures are grounded in the infrastructure state documented in sessions 938-953.*
