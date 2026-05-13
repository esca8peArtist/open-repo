---
title: "May 30 Launch — Risk and Contingency Plan"
prepared: 2026-05-13
launch-date: 2026-05-30
status: production-ready
scope: Gate incompletion risks, platform delay risks, partial-gate launch viability, critical path vs. non-critical items, fallback procedures
references:
  - PHASE_2_GO_NO_GO_DASHBOARD.md (5-criteria go/no-go framework)
  - TRACK_B_MAY_30_LAUNCH_READINESS_CHECKLIST.md (verification checklist)
  - may-30-launch-sequence.md (minute-by-minute launch script)
  - MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md (gate deadlines)
  - TRACK_B_LAUNCH_STATUS.md (fallback option hierarchy)
  - june-6-contingency-path.md (June 6 slip path)
  - TRACK_A_CONTINGENCY_LAUNCH_PLAN.md (Track A fallback)
---

# May 30 Launch — Risk and Contingency Plan

**How to use this document**: Read once before May 20. Reference on May 28–29 if any
pre-launch verification step returns FAIL. Each risk has a clear decision point and a
documented fallback that does not require improvisation under pressure.

**Escalation principle**: If a risk materializes with a clear same-day fix, execute the
fix and proceed. If a risk has no same-day fix, the document specifies the minimum viable
launch threshold and whether to proceed at reduced scope or slip to June 6.

---

## Risk 1: User Gates Not Complete by May 29

### Sub-Risk 1A: Gate 1 (Social Accounts) Incomplete

**Scenario**: Social accounts not created by May 29.

**Impact**: Buffer/Later cannot be connected; no social launch posts can be pre-scheduled;
influencer outreach cannot proceed from social handles.

**Critical path assessment**: Gate 1 is NOT critical path for the Etsy and email launch.
Etsy listings can publish at 10:00am and the Kit broadcast can send at 12:00pm without
any social account existing.

**Fallback**: Launch proceeds on Etsy + email only on May 30. Social launch posts are posted
manually from freshly-created accounts on May 30 afternoon (create accounts at 1:00pm,
post manually at 2:00pm using `phase-2-social-content-calendar-60day.md` Day 30 captions).
This is a 30-minute delay to the social sequence, not a launch cancellation.

**Minimum viable launch**: YES — Etsy + email is a valid May 30 launch without social accounts.

**Escalation trigger**: If Gate 1 is incomplete on May 30 at 8:00am, follow the 1:00pm
manual social posting procedure. Log account creation date in WORKLOG.md.

---

### Sub-Risk 1B: Gate 2 (Canva Brand Kit) Incomplete

**Scenario**: Canva Brand Kit not set up by May 29.

**Impact**: Zone cards cannot be exported from Canva; Pinterest pin batch cannot be designed
in brand-consistent colors; carousel for Day 3 Instagram cannot be built with Brand Kit.

**Critical path assessment**: If zone cards are not exported, Kit Email 1 cannot deliver
zone card PDFs. This blocks the email lead magnet delivery. However, the Etsy launch and the
launch broadcast to existing subscribers are unaffected.

**Fallback path A (if only zone cards are missing)**: Stage Kit Email 1 to deliver a
"Coming soon — your zone card will arrive within 24 hours" message to new subscribers.
Deliver zone cards manually as soon as Brand Kit setup and export are complete (estimated
Day 2 or Day 3 of launch). Document delay in Kit Email 1 copy.

**Fallback path B (if Brand Kit is the only block)**: Use Canva's color picker manually
(enter hex codes by hand each time) and skip Brand Kit for the initial launch week. All
designs are still buildable without the Kit — Brand Kit is a time-saver, not a hard
technical requirement. Launch social posts use mockup images from `mockups/` directory
which are already built and sized.

**Minimum viable launch**: YES — launch proceeds without Brand Kit; visual consistency
degrades slightly for Week 1 social posts only.

**Escalation trigger**: If Brand Kit not set up by May 27, activate Fallback B for social
posts. If zone cards not exported by May 29, activate Fallback A for Kit Email 1.

---

### Sub-Risk 1C: Gate 3 (Kit Email Automation) Incomplete

**Scenario**: Kit account created but full automation (5-email sequence + zone routing)
not built or not tested by May 29.

**Impact levels**:

- **Account not created**: No launch broadcast can be sent at 12:00pm. No subscriber
  delivery system exists.

- **Account created, landing page not live**: No new email sign-ups from social bio links.
  Existing subscribers (Phase 1 buyers) can still receive broadcast if manually loaded.

- **Account created, landing page live, sequence not built**: New subscribers sign up but
  receive no automated emails. Manual follow-up required.

- **Account created, landing page live, sequence built but not tested**: Risk of silent
  delivery failure — emails send but PDFs don't deliver correctly.

**Fallback by severity**:

If Kit account not created by May 28:
→ Send launch broadcast manually from Gmail at 12:00pm May 30 to any existing contact list.
→ Create Kit account on May 30 afternoon; launch email list from Day 1 post-launch.
→ This is the weakest fallback — email list building delayed 1 day. Acceptable.

If Kit landing page not live by May 29:
→ Use existing social bios' link to point to Etsy shop directly (Option 3a from
  `TRACK_B_LAUNCH_STATUS.md`).
→ Email list building starts after May 30 once landing page is built.

If sequence not built by May 29 but landing page is live:
→ New subscribers receive no automated emails.
→ Send Email 1 manually within 24 hours of each sign-up (not scalable but functional for
  the first 20–30 subscribers).
→ Build the full sequence in the first week post-launch. This is not a launch blocker.

If sequence built but end-to-end test not completed:
→ Run the test at 8:00am May 30 per `may-30-launch-sequence.md` Kit Verification block.
→ If test fails: diagnose and fix before 12:00pm. Most common failure (zone card Drive
  link returning "Request access") is a 5-minute fix.

**Minimum viable launch**: The Etsy listing launch is fully independent of Kit. Any Kit
state is acceptable for May 30 Etsy launch. Email launch can slip to June 1 without
significant impact.

---

## Risk 2: Platform Onboarding Delays

### Sub-Risk 2A: Kit Email Verification Delay

**Scenario**: Kit account requires email domain verification or account review before
broadcasts can be sent.

**Observed behavior**: Kit free tier typically activates immediately for Gmail accounts.
Verification holds are rare and typically triggered by sending too many emails too fast
(not applicable at launch) or by spam-flag content (not applicable given educational content).

**Fallback**: If Kit broadcast held for review at 12:00pm May 30, send manual broadcast
from Gmail with identical subject line and copy. BCC all existing subscribers. This is a
one-time workaround — not sustainable for a list over 50 subscribers.

**Prevention**: Create Kit account by May 25 (not May 28). Any verification delays resolve
within 48 hours of account creation for Gmail users.

---

### Sub-Risk 2B: Instagram/TikTok Account Review

**Scenario**: Newly created Instagram or TikTok business account is placed in a review
or "new account" restricted state that limits posting or reach.

**Observed behavior**: Instagram business accounts created with a personal Gmail and used
from a single device rarely face new-account restrictions. TikTok applies posting limits to
very new accounts (cannot post live, limited DMs) but feed posting is unrestricted from Day 1.

**Fallback**: If Buffer fails to post to Instagram or TikTok due to an account connection
issue, post manually. Caption and image source for launch posts are documented in
`phase-2-social-content-calendar-60day.md` Day 30. Manual posting takes 5 minutes per
platform.

**Prevention**: Create social accounts by May 18 (not May 29). Earlier account creation gives
the algorithm time to calibrate a new account, which slightly improves organic reach on launch day.

---

### Sub-Risk 2C: Buffer/Later Connection Failure

**Scenario**: Buffer or Later cannot connect to one or more social accounts on May 30.

**Fallback**: Post manually to each platform directly. Caption, hashtags, and image file for
each May 30 post are documented in `phase-2-social-content-calendar-60day.md` Day 30 section.
Manual posting takes 5–10 minutes per platform.

**Prevention**: Reconnect Buffer to all platforms on May 29 as part of the T-1 verification.
If any platform shows "Reconnect" in Buffer settings, re-authorize immediately on May 29.

---

### Sub-Risk 2D: Etsy Listing Still Under Review at Launch

**Scenario**: Track A Etsy account verification (identity verification, Etsy hold) is still
pending on May 30.

**Critical path assessment**: Track B social and email launch can proceed regardless of Etsy
status. Social accounts post, email broadcast sends, new Kit subscribers sign up.

**Fallback**: `PHASE_2_GO_NO_GO_DASHBOARD.md` Contingency Tree B documents the Gumroad
backup path (15-minute setup). If Etsy shop is not accessible May 30 morning:
1. Create Gumroad account at gumroad.com using wanka95@gmail.com (15 min)
2. List Phase 2 guides at the same prices as Etsy listings
3. Update Kit broadcast email links to Gumroad URLs (30 min)
4. Update social bio links to Gumroad storefront (5 min)
5. Proceed with Gumroad as the revenue channel; migrate to Etsy when account unlocks

**Minimum viable launch**: YES — Gumroad is a full fallback for Etsy. Launch proceeds.

---

## Risk 3: Critical Path Analysis — Which Gates Are Launch Blockers?

### Items that ARE critical path (launch cannot proceed without them)

| Item | Why Critical | Hard Deadline |
|---|---|---|
| Phase 2 guide PDFs exported (minimum 2) | Etsy listings without attached PDFs fail on purchase | May 29 end of day |
| Etsy listings in Draft with correct prices and descriptions | Cannot publish at 10:00am without staged drafts | May 29 end of day |
| Google Drive zone card links (8 zones) accessible from incognito | Kit Email 1 delivers dead links without this | May 27 end of day |
| Kit launch broadcast staged (subject line, copy, recipient list, 12pm send time) | No email launch at 12:00pm without this | May 29 9:00pm |
| At least 1 social post ready (image file + caption) | If all three platforms fail, need manual fallback | May 29 end of day |

### Items that are NOT critical path (launch proceeds without them)

| Item | Why Not Critical | Acceptable Slip |
|---|---|---|
| All 5 Phase 2 guides complete | 2-guide minimum viable launch documented | Complete 3–5 for full launch |
| All 8 zone card PDFs ready | 4-zone subset is functional (deliver others within 48h) | Partial delivery OK |
| Full 5-email Kit sequence built and tested | New subscribers can receive manual Email 1 | Build within first week post-launch |
| Buffer/Later scheduling connected | Manual posting is the fallback | Not critical |
| 30 lifestyle photos in etsy-ready/ | Mockup images function for Week 1 | Lifestyle photos are Week 3 trigger |
| Pinterest launch pins in Buffer | Pinterest Day 1 impressions are low anyway; can post manually | Not critical |
| Influencer outreach ready | Influencer mentions are a Day 1 enhancement, not a requirement | Can happen Day 2–3 |

---

## Risk 4: Partial Launch Viability Assessment

**Question**: If user completes only some gates by May 30, can the launch still proceed?

**Answer**: YES, with defined minimum viable states.

| Gate State | Launch Viable? | What Works | What Doesn't |
|---|---|---|---|
| All 3 gates complete, tested | Full launch | Everything | — |
| Gate 1 missing (no social accounts) | YES | Etsy + email | No social posts; no social traffic Day 1 |
| Gate 2 missing (no Canva Brand Kit) | YES | Etsy + email + social (using mockup images) | Zone card PDFs not ready; Pinterest batch not built |
| Gate 3 missing (no Kit account) | YES | Etsy only | No email launch; no zone card sign-ups; no subscriber communication |
| Gates 1 + 2 missing | YES (email + Etsy) | Etsy + email only | No social posts; limited Kit sign-up flow |
| Gates 1 + 2 + 3 missing | MINIMAL | Etsy only | No email; no social; no lead magnet |
| Etsy account under review (Track A blocked) | YES (Gumroad fallback) | Social + email + Gumroad | No Etsy revenue; Gumroad migration required |

**Minimum viable launch** (from TRACK_B_MAY_30_LAUNCH_READINESS_CHECKLIST.md Section 8):
- At minimum: 2 guides published on Etsy (or Gumroad) + Kit automation live (or broadcast
  sent manually) + at least 1 social post live.
- Fewer than 2 guides AND no email mechanism = slip to June 6.

**June 6 slip path**: Documented in `june-6-contingency-path.md`. Slip is not a failure —
it is a structured 7-day extension with defined conditions that trigger it.

---

## Risk 5: Launch Metric Disappointment

**Scenario**: Day 1 metrics are significantly below targets (e.g., 0 Etsy orders, Kit open
rate below 25%, no social engagement).

**This is not an emergency**. Day 1 is a proof-of-execution event, not a revenue event.
The signal metrics in `MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md` Section 4 distinguish between
"launch worked" metrics (infrastructure fired) and "signal" metrics (calibration data).

**Protocol if Day 1 is below all signal thresholds**:
1. Do not change anything on Day 1. Let all scheduled content run.
2. On Day 2, diagnose: which specific metrics are below threshold? (Email open rate?
   Etsy views? Social reach?)
3. Cross-reference against the signal table in `MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md`.
4. Apply the specific "if below target" action for each metric (subject line test, re-send to
   non-openers, verify listing indexed in Etsy search, etc.).
5. Full Week 1 review at Day 7 per `phase-2-week-1-success-metrics.md`.

**The launch does not need to be "good" on Day 1 to be a valid launch.** All product-based
businesses take 30–60 days to reach meaningful volume. Day 1 is the starting line.

---

## Risk Summary Table

| Risk | Probability | Impact | Fallback Documented | Critical Path? |
|---|---|---|---|---|
| Gate 1 (social accounts) incomplete May 29 | Medium | Low | Manual posting May 30 1pm | No |
| Gate 2 (Canva Brand Kit) incomplete May 29 | Medium | Low | Mockup images for social; manual hex codes in Canva | No |
| Gate 3 (Kit) not built by May 29 | Low | Medium | Manual broadcast from Gmail; Kit delayed to June 1 | Partial |
| Kit email verification delay | Very low | Low | Manual Gmail broadcast | No |
| Buffer connection failure | Low | Very low | Manual posting | No |
| Etsy account under review | Low (ongoing risk) | Medium | Gumroad 15-min fallback | Yes (Gumroad mitigates) |
| Zone card Drive links broken | Low | High if undetected | Fix Drive sharing; 5-minute fix | Yes |
| Phase 2 guide PDFs not exported | Medium | High | Slip to 2-guide minimum viable launch | Yes |
| Day 1 metrics below target | High (realistic expectation) | Low (calibration event) | Week 1 review protocol | No |

---

## Decision Tree: May 29 Evening

Work through this in sequence on May 29 evening (approximately 8:00pm–9:00pm):

1. Are at least 2 Phase 2 guide PDFs exported and attached to Etsy drafts?
   - YES → continue
   - NO → launch slips to June 6; notify via WORKLOG.md entry

2. Is Kit account live and launch broadcast staged for 12:00pm May 30?
   - YES → continue
   - NO → fallback to Gmail manual broadcast; note in WORKLOG.md

3. Are Etsy listings in Draft with prices, descriptions, and PDFs attached?
   - YES → continue
   - NO → fix before 11:00pm tonight; if cannot fix, slip to June 6

4. Are Google Drive zone card links accessible from incognito?
   - YES → continue
   - NO → fix Drive sharing permissions now; 5-minute fix; re-verify in incognito

5. Is at least one social post staged (Buffer or manual file ready)?
   - YES → launch is GO
   - NO → download Day 30 image from `mockups/` directory now; write caption from calendar; manual post at 2:00pm tomorrow

If steps 1–5 are all YES: go to bed. Launch proceeds May 30 at 8:00am per
`may-30-launch-sequence.md`.

If step 1 is NO: execute June 6 slip path per `june-6-contingency-path.md`.

---

*Prepared: 2026-05-13. Seedwarden Agent. Risk framework references
PHASE_2_GO_NO_GO_DASHBOARD.md (contingency trees), TRACK_B_LAUNCH_STATUS.md (fallback
option hierarchy), june-6-contingency-path.md (slip path documentation), and
TRACK_A_CONTINGENCY_LAUNCH_PLAN.md (Etsy verification fallback).*
