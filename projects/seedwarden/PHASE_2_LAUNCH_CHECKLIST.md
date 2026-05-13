---
title: "Phase 2 Launch Checklist — May 30, 2026"
created: 2026-05-13
status: production-ready
scope: 48-hour pre-launch QA, launch-day sequence, post-launch monitoring, success metrics
references:
  - PHASE_2_READINESS_AUDIT_MAY_13.md (readiness baseline)
  - PHASE_2_GO_NO_GO_DASHBOARD.md (five binary go/no-go criteria)
  - phase-2-launch-day-checklist.md (minute-by-minute launch guide)
  - TRACK_B_FINAL_EXECUTION_GUIDE.md (three user gates)
  - TRACK_A_CONTINGENCY_LAUNCH_PLAN.md (Track A blocker options)
---

# Phase 2 Launch Checklist — May 30, 2026

**Launch date**: May 30, 2026 (17 days from audit date)
**Track**: Track B (social + email automation — independent of Phase 1 Etsy status)
**Overall readiness**: CONDITIONAL GO — all materials staged; three user gates remain open
**Launch window**: 09:00 UTC (Etsy activation) / 12:00 UTC (Kit broadcast) / 14:00 UTC (social posts)

---

## Part 1: 48-Hour Pre-Launch QA (May 28-29)

### May 28 Morning Block (09:00–12:00)

**Content completion audit (Criterion 1)**

- [ ] Open `projects/seedwarden/products/` — confirm 5 Phase 2 guide files are present
- [ ] Open each guide — confirm all 6 sections populated (Identification, Habitat, Harvest, Safety, Preparation, Cross-reference)
- [ ] Search each file for "PLACEHOLDER" or "TODO" — must return zero results
- [ ] Confirm each guide references at least one valid photo path from `assets/wild-edibles/`
- [ ] Confirm any lookalike-risk species (Nasturtium, Urtica) has an explicit safety callout block
- [ ] Confirm title, subtitle, and 3 primary keywords match listing copy in `etsy-store-copy.md`

**Visual assets audit (Criterion 2 — partial)**

- [ ] Run photo resolution check (from `PHASE_2_GO_NO_GO_DASHBOARD.md` Section 1, Criterion 2.1)
- [ ] Confirm all 18 habit photos pass 1200x800 minimum
- [ ] Open `WORKLOG.md` — confirm all 18 species have a license entry

### May 28 Afternoon Block (13:00–16:00)

**Etsy listings preparation (Criterion 4)**

- [ ] Log into Etsy Shop Manager — confirm no verification hold banner visible
- [ ] If Phase 2 listings not yet uploaded: upload all 5 guide PDFs as new listings using `etsy-store-copy.md`; set status to Draft (do not activate yet)
- [ ] If listings already uploaded: open each listing, confirm price matches `etsy-store-copy.md`, confirm PDF is attached, confirm all tags correct
- [ ] Create or verify SEEDWARDEN15 coupon: Etsy > Marketing > Sales and Coupons > 15% off, no minimum, no expiry

**Zone card verification**

- [ ] Run `ls projects/seedwarden/assets/zone-cards/*.pdf | wc -l` — must return 8
- [ ] If zone cards are missing: follow `CANVA_ZONE_CARD_BATCH_WORKFLOW.md` immediately — this is the highest-risk gap

### May 28 Evening Block (18:00–21:00)

**Marketing infrastructure (Criterion 3)**

- [ ] Open Kit dashboard — confirm "Seedwarden Welcome" automation shows "Published" (not Draft, not Paused)
- [ ] Open Kit > Broadcasts — confirm May 30 launch broadcast exists and is Scheduled for 12:00pm
- [ ] If broadcast not created: create now using copy from `marketing/email-and-launch-plan.md` Launch Broadcast section; schedule for 12:00pm May 30
- [ ] Run end-to-end Kit delivery test (incognito, Zone 5 test email) — confirm zone card PDF downloads within 60 seconds; record result in WORKLOG.md
- [ ] Open Buffer or Later queue — confirm at least 3 posts scheduled for May 30: Instagram 14:00 UTC, TikTok 14:00 UTC, Pinterest 15:30 UTC
- [ ] Confirm all platform connections are green (no "Reconnect" warning) under Buffer/Later Settings > Connected Accounts

**Canva Brand Kit confirmation**

- [ ] Log into Canva — Brand Hub shows Brand Kit with 6 hex colors (#143b28, #1A3A2A, #F5EDD6, #EDE0C4, #8FA882, #A0522D), 3 fonts (Playfair Display, Lato/Source Sans 3, Cormorant Garamond), logo uploaded
- [ ] If Brand Kit not configured: complete now per `TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md` Section 1 (30 minutes)

---

### May 29 Full Go/No-Go Audit

**Morning block (09:00–12:00) — verify remaining criteria**

- [ ] Run Criterion 2 full audit: zone card delivery test from incognito (all 8 zones download as PDFs, not viewer pages)
- [ ] Run Criterion 4 full audit: Etsy account status confirmed clear, all listings in Draft with correct prices, SEEDWARDEN15 coupon active
- [ ] Run Criterion 5 audit: open `customer-analytics.csv` and `phase-2-ltv-tracker-phase1-baseline.csv` — confirm headers populated; open `phase-2-week-1-success-metrics.md` and confirm numeric Week 1 targets are documented

**Afternoon block (13:00–16:00) — compile audit and make decision**

- [ ] Complete the Go/No-Go Audit Record from `PHASE_2_GO_NO_GO_DASHBOARD.md` Section 1 — fill in all 5 criteria, all 24 sub-checkpoints
- [ ] Record result in WORKLOG.md
- [ ] Make launch decision: LAUNCH (all 5 GO) / SLIP (1 NO-GO with 24h remediation path) / ESCALATE (2+ NO-GO)
- [ ] If SLIP: execute the relevant Contingency Tree from `PHASE_2_GO_NO_GO_DASHBOARD.md` Section 3
- [ ] If LAUNCH: proceed to evening steps

**Evening block (18:00–21:00) — final confirmation**

- [ ] Run end-to-end Kit delivery test a second time — confirm no state change from May 28 test
- [ ] Open Buffer queue — confirm all 3 May 30 posts still show "Scheduled" with correct times
- [ ] Open Etsy Shop Manager — confirm all Phase 2 listings are in Draft (NOT yet Active)
- [ ] Record final Go/No-Go Audit in WORKLOG.md
- [ ] Set alarm for 05:45 UTC May 30

---

## Part 2: Launch Day Sequence (May 30)

### 06:00 UTC — Pre-Launch Verification (30 minutes)

- [ ] Open all monitoring tabs: Etsy Shop Manager Stats, Etsy public store (incognito), Kit Broadcasts, Kit Automations, Kit Subscribers, Buffer queue
- [ ] Run Kit delivery test one final time from incognito — Zone 5 test email
- [ ] Confirm launch broadcast shows "Scheduled" at 12:00pm
- [ ] Confirm Etsy listings still in Draft (not accidentally published)
- [ ] Confirm social posts still queued in Buffer with correct times

**06:30 UTC — Decision gate**

If all 5 checks pass: PROCEED to 09:00 UTC.

If any check fails, apply the corresponding fix (from `PHASE_2_GO_NO_GO_DASHBOARD.md` Section 2):
- Kit automation paused: Kit > Automations > Resume (5 seconds)
- Broadcast in Draft: Kit > Broadcasts > schedule for 12:00pm today (30 seconds)
- Zone card download broken: update Google Drive link format to `uc?export=download&id=[FILE_ID]` (2 minutes)
- Buffer post missing: copy caption from `phase-2-social-content-calendar-60day.md` Day 30, recreate post (5 minutes per platform)

### 09:00 UTC — Etsy Activation

- [ ] Etsy Shop Manager > Listings > select all Phase 2 listings in Draft > click Publish
- [ ] Navigate to Etsy store in incognito — confirm listings appear in search results
- [ ] Note exact activation time in `customer-analytics.csv` as "Phase 2 Launch Timestamp"

### 12:00 UTC — Email Broadcast

- [ ] At 12:05 UTC: check Kit > Broadcasts — status should read "Sending" or "Sent"
- [ ] If still "Scheduled" at 12:20 UTC: click into broadcast > Send Now
- [ ] At 12:30 UTC: note delivery rate (target >90%) and open rate (target >35%)

### 14:00 UTC — Social Activation

- [ ] Confirm Instagram launch post published by 14:15 UTC — verify visible on profile
- [ ] Confirm TikTok launch post published by 14:15 UTC — verify video live
- [ ] If either fails: post manually using caption from `phase-2-social-content-calendar-60day.md` Day 30

### 15:30 UTC — Pinterest

- [ ] Confirm Pinterest pins published by 15:45 UTC — verify pins visible on profile

### End of Day (19:00–21:00 UTC) — Day 1 Metrics Log

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
Pinterest-Monthly-Views: ___
Phase2-Launch-Timestamp: 09:00 UTC
```

---

## Part 3: Post-Launch Monitoring and Adjustment Plan

### Monitoring Schedule (Days 1–7)

Do not check continuously. Follow this cadence:

| Day | UTC time | What to check | Duration |
|-----|----------|---------------|----------|
| May 31 (Day 2) | 20:00 | Kit Email 1 open rate + click rate; new Etsy orders count | 10 min |
| June 1 (Day 3) | 20:00 | Etsy traffic trend; Kit Email 1 delivery complete | 10 min |
| June 3 (Day 5) | 20:00 | Kit Email 3 open rate; behavioral tag count in Kit | 10 min |
| June 6 (Day 7) | 10:00–11:00 | Full Week 1 review — all metrics against targets below | 30 min |

### Adjustment Triggers

**If email open rate on launch broadcast is below 25% by June 1**:
- Check Kit deliverability log for SPF/DKIM issues
- If SPF/DKIM unverified: contact Kit support immediately — this is the only high-severity email risk
- A/B test subject line in next broadcast (not an emergency)

**If Etsy listing views are below 50 by June 1**:
- Check Etsy Shop Manager > Listings > SEO score for each listing
- Revise title and first 40 characters of tags on the lowest-performing listing
- Do not change all listings simultaneously — revise one, wait 48 hours, compare

**If views are high but orders are below 3 by June 3**:
- Navigate to Etsy Shop Manager > Stats > Listings > find the highest-view listing
- Check views-to-order conversion rate (Etsy calculates this)
- If conversion below 1%: the cover image or first sentence of the description is the issue
- Update the first image and first sentence of the description (15 minutes)

**If TikTok views are below 50 by June 1**:
- Verify video was uploaded natively to TikTok (not cross-posted from Instagram — cross-posted videos are algorithmically suppressed)
- Re-upload natively if needed

**If Kit subscribers are below 5 by June 3**:
- Review Kit landing page copy — is the value proposition clear?
- Test an alternative CTA in all three social bios (single change, not simultaneous)
- Check that the link-in-bio is pointing to the Kit page, not the Etsy store

---

## Part 4: Success Metrics

### Minimum thresholds (must hit 3 of 4 by June 6 for Phase 2 to be considered viable)

| Metric | Minimum threshold | Target | Source |
|--------|------------------|--------|--------|
| Email open rate (launch broadcast) | 25% | 35%+ | Kit Broadcasts > Stats |
| Etsy listing views (Week 1 total) | 50 | 200+ | Etsy Shop Manager > Stats |
| Orders (Week 1) | 3 | 8–15 | Etsy Shop Manager > Orders |
| Kit new subscribers (Week 1) | 5 | 15–25 | Kit Dashboard |

### Week 1 full metrics table

| Metric | Minimum | Target | Action if below minimum |
|--------|---------|--------|------------------------|
| Etsy orders | 3 | 8–15 | Check listing SEO scores; revise top listing title/tags |
| Gross revenue | $75 | $200–500 | Correlated with orders; investigate order gap first |
| Email click rate (launch broadcast) | 4% | 8–10% | Review CTA copy; A/B test in next broadcast |
| Instagram impressions (launch post) | 50 | 200+ | Add location tag + 5 niche hashtags; reshare to Stories |
| Instagram engagement rate | 2% | 5%+ | Comment on 10 posts in foraging/wild-edibles niche |
| TikTok views (launch video) | 50 | 500+ | Confirm native upload; re-upload if cross-posted |
| Pinterest monthly views | Not tracked Day 1 | 500+ by Day 30 | Check Day 3+ (Pinterest has 2–24 hour indexing delay) |
| Etsy favorites (Week 1) | 5 | 20+ | If views high but favorites low: cover image is the issue |
| Refund rate | 0% | 0% | Any refund: respond within 4 hours, issue full refund |

### Phase 3 trigger assessment (June 6, Day 7)

Phase 3 begins when 2 of these 4 triggers are met:

| Trigger | Pass condition | Check source |
|---------|---------------|--------------|
| T1 — Revenue | Week 1 Etsy revenue >= $500 | `customer-analytics.csv` |
| T2 — Satisfaction | 0 refunds + at least 1 positive signal (review, reply, comment) | WORKLOG.md |
| T3 — Production readiness | Phase 3 Bloodroot/Trillium/Lady's Slipper drafts at 80%+ | `projects/seedwarden/products/` |
| T4 — Date confirmed | June 15 calendar clear for launch operations | User confirms |

Record Phase 3 decision in WORKLOG.md on June 6 using template from `PHASE_2_GO_NO_GO_DASHBOARD.md` Section 7.

---

## Part 5: Quick-Reference Contingency Table

| Problem | Immediate action | Reference |
|---------|-----------------|-----------|
| Etsy account still shows verification hold on May 28 | Execute Contingency Tree B: contact Etsy support or switch to Gumroad (15 min) | `PHASE_2_GO_NO_GO_DASHBOARD.md` Section 3 |
| Kit automation in Draft or Paused | Kit > Automations > Resume or Publish | `PHASE_2_GO_NO_GO_DASHBOARD.md` Section 3, Tree D |
| Zone cards missing from `assets/zone-cards/` | Export from Canva immediately; allow 4–6 hours | `CANVA_ZONE_CARD_BATCH_WORKFLOW.md` |
| Fewer than 4 Phase 2 guides complete by May 25 | Launch with available guides; defer missing to June 1 follow-on listing | `PHASE_2_GO_NO_GO_DASHBOARD.md` Section 3, Tree A |
| PDF doesn't download — "Request access" error | Fix Google Drive link to `uc?export=download&id=[FILE_ID]` format | `PHASE_2_GO_NO_GO_DASHBOARD.md` Tree D, Step 2 |
| Buffer platform shows "Reconnect" | Reconnect platform under Settings > Connected Accounts before May 29 | — |
| 0 orders in first 72 hours | Execute rollback procedure in `PHASE_2_GO_NO_GO_DASHBOARD.md` Section 8 | Section 8 |

---

*Created: 2026-05-13. This checklist synthesizes `PHASE_2_READINESS_AUDIT_MAY_13.md` and `PHASE_2_GO_NO_GO_DASHBOARD.md` into a single sequential action document. All referenced files are in `projects/seedwarden/`. For minute-by-minute launch day detail, see `phase-2-launch-day-checklist.md`.*
