---
title: "May 29 Go/No-Go Decision Template — May 30 Launch"
created: 2026-05-19
purpose: >
  Executable decision form for May 29. Run the three verification blocks in order (morning,
  afternoon, evening), fill in each table row, then record the final decision at the bottom.
  This file is the single source of truth for the May 30 launch authorization.
authority-document: PHASE_2_GO_NO_GO_DASHBOARD.md (Section 2) and TRACK_B_GATE_COMPLETION_VERIFICATION.md
---

# May 29 Go/No-Go Decision Template

**Decision deadline**: May 29, 20:00 UTC
**Launch time**: May 30, 09:00 UTC (Etsy listings active); 12:00 UTC (social posts)
**Total verification time required**: 2–3 hours across the day — not a quick evening check

Do not answer the 5-question gate check at the bottom until all three verification blocks above it are complete. The 5-question check confirms gate completion; it does not replace verifying infrastructure.

---

## Morning Block — May 29, 09:00–12:00

Work through Criterion 2 (Visual Assets) and Criterion 4 (Sales Readiness) in this order.

### C2: Visual Assets

| # | Check | Result | Notes |
|---|-------|--------|-------|
| C2.1 | All 18 habit photos present in `projects/seedwarden/assets/wild-edibles/` | [ ] PASS [ ] FAIL | Run: `ls projects/seedwarden/assets/wild-edibles/*-habit.jpg \| wc -l` — must return 18 |
| C2.2 | WORKLOG.md has a license entry for all 18 species | [ ] PASS [ ] FAIL | Scan WORKLOG.md for each species; each must show CC-BY, CC0, or equivalent |
| C2.3 | 8 zone card PDFs present in `projects/seedwarden/assets/zone-cards/` | [ ] PASS [ ] FAIL | Run: `ls projects/seedwarden/assets/zone-cards/*.pdf \| wc -l` — must return 8 |
| C2.4 | All 8 zone card download links in Kit Email 1 open as PDFs in incognito | [ ] PASS [ ] FAIL | Each link must trigger a PDF download, not a Drive viewer page |
| C2.5 | Canva Brand Hub shows "Seedwarden" Brand Kit with 10 colors, 3 fonts, logo | [ ] PASS [ ] FAIL | Log into canva.com and verify visually |

**C2 Status**: [ ] PASS (all 5 pass) [ ] CONDITIONAL (1 item fixable same day) [ ] FAIL (2+ items or unfixable)

**If C2.3 or C2.4 FAIL**: Zone cards are the only items that can block launch. See Gate 3 fallback in TRACK_B_USER_GATES.md — if zone cards are not ready, Kit Email 1 must deliver a plain-text placeholder until cards are uploaded.

---

### C4: Sales Readiness

| # | Check | Result | Notes |
|---|-------|--------|-------|
| C4.1 | Etsy Shop Manager loads with no verification hold; shop is open to buyers | [ ] PASS [ ] FAIL | Log into etsy.com/your/shops/me/dashboard |
| C4.2 | All Phase 2 guide listings show "Active" or confirmed to activate at 09:00 UTC May 30 | [ ] PASS [ ] FAIL | Etsy Shop Manager > Listings; Draft is acceptable if planned for May 30 activation |
| C4.3 | Preview one Etsy listing — PDF is attached and price is correct | [ ] PASS [ ] FAIL | Click Preview on any listing; verify the file download and price field |
| C4.4 | All listing prices match the pricing table in `etsy-store-copy.md`; no $0.00 or blank prices | [ ] PASS [ ] FAIL | Scan all listings; a $0.00 listing is a critical error |
| C4.5 | Etsy coupon SEEDWARDEN15 exists and shows Active at 15% off | [ ] PASS [ ] FAIL | Etsy Shop Manager > Marketing > Sales and Coupons |

**C4 Status**: [ ] PASS [ ] CONDITIONAL [ ] FAIL

---

**Morning block complete time**: _______________

---

## Afternoon Block — May 29, 13:00–16:00

Work through Criterion 3 (Marketing Infrastructure) and make the preliminary launch call.

### C3: Marketing Infrastructure

| # | Check | Result | Notes |
|---|-------|--------|-------|
| C3.1 | Kit > Automations > "Seedwarden Welcome" shows status Published | [ ] PASS [ ] FAIL | Draft or Paused automations do not trigger — this is a single-FAIL escalation item |
| C3.2 | Kit > Broadcasts shows May 30 launch broadcast Scheduled at 12:00pm May 30 | [ ] PASS [ ] FAIL | If no prior list exists, skip broadcast; note here |
| C3.3 | End-to-end test: sign up via Kit landing page (Zone 5, incognito); zone card email arrives within 60 seconds; Zone 5 PDF downloads correctly | [ ] PASS [ ] FAIL | Full test procedure in PHASE_2_GO_NO_GO_DASHBOARD.md Section 1, Criterion 3 |
| C3.4 | Buffer (or Later) queue shows at minimum 3 posts scheduled May 30: Instagram 12:00pm, TikTok 2:00pm, Pinterest 3:30pm | [ ] PASS [ ] FAIL | If using Canva native scheduler, confirm posts are scheduled there instead |
| C3.5 | Buffer/Later > Connected Accounts — Instagram, TikTok, Pinterest all show green/active | [ ] PASS [ ] FAIL | A "Reconnect" warning must be resolved before launch |

**C3 Status**: [ ] PASS [ ] CONDITIONAL [ ] FAIL

---

### C5: Performance Baseline

| # | Check | Result | Notes |
|---|-------|--------|-------|
| C5.1 | `projects/seedwarden/customer-analytics.csv` opens with headers populated | [ ] PASS [ ] FAIL | |
| C5.2 | `projects/seedwarden/phase-2-ltv-tracker-phase1-baseline.csv` opens with columns present | [ ] PASS [ ] FAIL | |
| C5.3 | `projects/seedwarden/phase-2-week-1-success-metrics.md` has specific numeric targets | [ ] PASS [ ] FAIL | Look for order count, revenue, Kit subscriber, and email open rate targets |
| C5.4 | Calendar holds confirmed for May 31, June 1, June 3, June 6 monitoring check-ins | [ ] PASS [ ] FAIL | |

**C5 Status**: [ ] PASS [ ] CONDITIONAL [ ] FAIL

---

**Preliminary launch decision (make this before the evening block)**:

| Criterion | Status | Single-fail escalation? |
|-----------|--------|------------------------|
| C2 — Visual Assets | [ ] PASS [ ] CONDITIONAL [ ] FAIL | YES — C2.3 and C2.4 (zone cards) are blocking |
| C3 — Marketing Infrastructure | [ ] PASS [ ] CONDITIONAL [ ] FAIL | YES — C3.1 (Kit automation Published) is blocking |
| C4 — Sales Readiness | [ ] PASS [ ] CONDITIONAL [ ] FAIL | YES — C4.1 (Etsy no hold) is blocking |
| C5 — Performance Baseline | [ ] PASS [ ] CONDITIONAL [ ] FAIL | NO — baseline setup is advisory |

**Preliminary call**: [ ] All clear — proceed to evening block [ ] Fix required — note below

**Fix items identified in afternoon block**:

```
Item 1:
  Criterion: ___
  Issue: ___
  Fix: ___
  Time to fix: ___
  Fixed by: ___

Item 2:
  Criterion: ___
  Issue: ___
  Fix: ___
  Time to fix: ___
  Fixed by: ___
```

**Afternoon block complete time**: _______________

---

## Evening Block — May 29, 18:00–21:00

Re-verify any CONDITIONAL items from afternoon. Arm the launch state. Do not skip this block even if the afternoon block was all PASS.

| # | Check | Result | Notes |
|---|-------|--------|-------|
| E1 | Re-run Kit end-to-end test (Zone 5, different test email from afternoon) | [ ] PASS [ ] FAIL | Confirms no state change from afternoon configuration |
| E2 | Buffer/Later queue — all 3 May 30 posts still show Scheduled with correct times | [ ] PASS [ ] FAIL | Posts can be accidentally deleted; verify now |
| E3 | Etsy — all Phase 2 listings are in Draft (they activate at 09:00 UTC May 30); do NOT activate early | [ ] PASS [ ] FAIL | Early activation loses the coordinated launch signal |
| E4 | Phone alarm set for 05:45 UTC May 30 | [ ] PASS [ ] FAIL | Pre-launch verification opens 06:00 UTC |

**Evening block complete time**: _______________

---

## The 5-Question Gate Check

**Run this AFTER all three blocks above are complete.**

All 5 must be Yes for GREEN LIGHT.

| # | Question | Answer |
|---|----------|--------|
| 1 | Gate 1 complete? All 3 social accounts live with profile photo, bio, and business account type | [ ] YES [ ] NO |
| 2 | Gate 2 complete? Canva Brand Kit has 10 colors, 3 fonts, logo uploaded | [ ] YES [ ] NO |
| 3 | Gate 3 complete? Kit landing page live, 5-email sequence status Published, 3-test protocol passed | [ ] YES [ ] NO |
| 4 | Kit landing page URL confirmed in all 3 social bios | [ ] YES [ ] NO |
| 5 | First content post ready: image file exported, caption text ready to paste, post pre-scheduled or ready for manual post at 12:00pm May 30 | [ ] YES [ ] NO |

**If all 5 YES and all 5 Dashboard criteria PASS**: GREEN LIGHT.
**If any NO and fixable tonight**: fix immediately, re-verify, then mark YES.
**If any NO and NOT fixable tonight**: see RED escalation below.

---

## Final Go/No-Go Decision

```
=== MAY 29 GO/NO-GO DECISION — Seedwarden Track B ===

Date: May 29, 2026
Decision time: _______________ UTC
Verified by: thorn

CRITERION SCORES:
  C2 Visual Assets:         [ ] PASS  [ ] CONDITIONAL  [ ] FAIL
  C3 Marketing Infra:       [ ] PASS  [ ] CONDITIONAL  [ ] FAIL
  C4 Sales Readiness:       [ ] PASS  [ ] CONDITIONAL  [ ] FAIL
  C5 Performance Baseline:  [ ] PASS  [ ] CONDITIONAL  [ ] FAIL

GATE CHECK:
  Gate 1 (Social):    [ ] YES  [ ] NO
  Gate 2 (Canva):     [ ] YES  [ ] NO
  Gate 3 (Kit):       [ ] YES  [ ] NO
  Bio links live:     [ ] YES  [ ] NO
  Day 1 post ready:   [ ] YES  [ ] NO

LAUNCH DECISION:
  [ ] GREEN — LAUNCH MAY 30 at 09:00 UTC (Etsy) / 12:00pm (social)
      Next step: Set alarm for 05:45 UTC. Run May 30 pre-launch checks at 06:00 UTC.

  [ ] YELLOW — CONDITIONAL LAUNCH MAY 30
      One criterion conditional with same-day fix in progress.
      Fix item: _______________________________________________
      Fix deadline: _________________________
      If fix complete by 23:00 UTC May 29: proceed to launch.
      If fix not complete by 23:00 UTC May 29: escalate to RED.

  [ ] RED — NO-GO: POSTPONE TO JUNE 6
      Failing criterion/criteria: ________________________________
      Root cause: _____________________________________________
      Remediation owner: thorn
      Remediation window: May 30–June 3
      New go/no-go audit: June 4 morning
      Contingency path: MAY_30_RISK_AND_CONTINGENCY_PLAN.md (RED escalation section)
      Fallback activated: ______________________________________
```

---

## RED Escalation Quick Reference

**If RED on C3.1 (Kit automation not Published)**:
- Kit > Automations > click automation > click Publish
- If automation was in Draft: re-run end-to-end test (Test 1 from 3-test protocol)
- Re-verify C3.3 after change

**If RED on C2.3/C2.4 (zone cards missing or links broken)**:
- If PDFs exist but Drive links broken: re-share each Google Drive file > "Anyone with link" > copy `/uc?export=download&id=[FILE_ID]` format URL (NOT the `/view` format)
- If PDFs not built: zone cards can be done post-launch with a plain-text placeholder in Kit Email 1; see Gate 3 fallback in TRACK_B_USER_GATES.md
- Impact of launching without zone cards: Email 1 delivers no PDF; subscribers see placeholder text. Email list still grows; zone cards added retroactively within 48 hours.

**If RED on C4.1 (Etsy verification hold)**:
- This is an Etsy account status issue, not fixable by editing a file
- Fallback: launch social + Kit lead magnet only; Etsy listings defer to June 2
- Revenue impact: 0 Etsy sales Day 1; Kit list still builds; no structural damage to launch
- See MAY_30_RISK_AND_CONTINGENCY_PLAN.md "Track A blocked" contingency

**If RED on two or more criteria**:
- Do not launch May 30
- Execute June 6 path per TRACK_B_GATE_COMPLETION_VERIFICATION.md Unacceptable Outcome section
- Set calendar for June 4 re-verification

---

## May 30 Pre-Launch Sequence (if GREEN or YELLOW)

**06:00 UTC — Pre-launch verification**
- [ ] Log into Kit: confirm automation is still Published, landing page still live
- [ ] Log into Buffer/Later: confirm all 3 May 30 posts still Scheduled
- [ ] Log into Etsy: confirm listings are in Draft (do not activate yet)

**09:00 UTC — Etsy activation**
- [ ] Publish all Phase 2 listings that are in Draft
- [ ] Verify each shows "Active" in Etsy Shop Manager

**12:00 UTC — Email broadcast** (only if list exists)
- [ ] Kit > Broadcasts > send launch broadcast per KIT_EMAIL_LAUNCH_SEQUENCE.md

**12:00 UTC — Instagram post**
- [ ] Post Day 1 content from MAY_30_JUNE_30_CONTENT_CALENDAR.md (May 30 row)
- [ ] Verify Kit landing page URL is in bio before posting

**14:00 UTC — TikTok post**
- [ ] Upload same video file as native TikTok upload (not cross-posted from Instagram)

**15:30 UTC — Pinterest pins**
- [ ] Upload 3 pins; at least 1 educational, 1 product-focused

**21:00 UTC — End of day check**
- Kit signups today: ___
- Instagram impressions: ___
- TikTok views: ___
- Note in WORKLOG.md for June 1 baseline comparison

---

*Created: 2026-05-19. Synthesized from PHASE_2_GO_NO_GO_DASHBOARD.md (Section 1-2) and
TRACK_B_USER_GATES.md (May 29 verification blocks). All criterion checks and decision logic
sourced directly from those authority documents. This template is the executable version of
the May 29 audit procedure.*
