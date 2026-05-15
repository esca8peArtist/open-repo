---
title: "Phase 1 Wave 1 Execution Prep — May 15-17 Launch-Day Logistics"
created: 2026-05-15
status: READY — awaiting path selection
scope: "Pre-staging verification: contacts, templates, calendar, checklist, contingency. No new content. Execution-only."
---

# Phase 1 Wave 1 Execution Prep

**Decision gate**: Once you select Path A / A+37 / B today, this document is the only thing the orchestrator reviews before handing you the daily checklist. Estimated review time: 15 minutes.

---

## 1. Contact Verification Status — Batch 1 (25 Highest-Leverage: sending 5 May 15-17)

Live-verified May 15, 2026. Position + email status per public institutional pages.

| # | Contact | Organization | Role — Verified | Primary Email | Status | Alternate |
|---|---------|-------------|-----------------|--------------|--------|-----------|
| 1 | Ryan Goodman | Just Security / NYU Law | Co-Editor-in-Chief, Just Security (confirmed via masthead) | ryan.goodman@nyu.edu | CONFIRMED pattern; spot-verify today at law.nyu.edu/faculty before send | ryan@justsecurity.org |
| 2 | Wendy Weiser | Brennan Center / NYU | VP for Democracy (confirmed via BCJ experts page) | wweiser@brennancenter.org | CONFIRMED pattern; title unchanged | brennancenter.org contact form |
| 3 | Erica Chenoweth | Harvard Kennedy School | Frank Stanton Prof + Academic Dean for Faculty Dev (confirmed via HKS faculty page) | erica_chenoweth@hks.harvard.edu | CONFIRMED — underscore format required (corrected May 14) | echenoweth@harvard.edu |
| 4 | Ian Bassin | Protect Democracy | Co-Founder & Executive Director | ian@protectdemocracy.org | Pattern confirmed; team page 404 on direct URL — verify via protectdemocracy.org/team/ today | protectdemocracy.org contact form |
| 5 | Marc Elias | Elias Law Group / Democracy Docket | Firm Chair, Elias Law Group; Founder, Democracy Docket | melias@elias.law | CONFIRMED — left Perkins Coie 2021; elias.law confirmed current firm; perkinscoie.com address is STALE do not use | press@democracydocket.com |

**One flagged discrepancy**: PHASE_1_CONTACT_VERIFICATION.json (created April 30) still lists `melias@perkinscoie.com` as primary for Elias. BATCH_1_CONTACT_LOG.md (updated May 14) corrects this to `melias@elias.law`. Use the May 14 log. Do not send to Perkins Coie domain.

**Chenoweth title note**: HKS page now shows "Academic Dean for Faculty Development" as an additional role added since April verification. Frank Stanton professorship unchanged. Update salutation block if referencing her title.

**Contacts 6-25** (Wave 2 and 3, not sending May 15-17): Position verification for these is documented in `DISTRIBUTION_OUTREACH_CONTACTS.md` and `execution/tier-1-contact-batches.md`. Do not verify Wave 2-3 until May 18 prep session.

---

## 2. Email Delivery Testing — Pre-Send Verification

No live test emails have been sent. Execute these five checks the morning of May 15 before the 16:00 UTC send window.

**Test protocol (15 minutes total)**:

1. Send one test email to yourself from your sending account. Confirm: arrives in under 3 minutes, lands in inbox not spam, no formatting breaks in the email body (check links render, no garbled characters).
2. Open each of the five Gist URLs in an incognito window and confirm no 404:
   - Main proposal: `https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261`
   - Executive summary: `https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4`
   - Litigation tracker: `https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0`
3. Scan each of the five email drafts in your drafts folder and confirm zero `{{placeholder}}` strings remain (see Section 3 for what still needs filling).
4. Confirm Gmail filter "Phase 1 Responses" label is active so replies auto-route.
5. If any Gist returns 404: wait 60 seconds and retry. If still failing, escalate — do not send until URLs are live.

**Spam risk factors to check**: Subject lines that contain "reform," "feedback request," or "democratic framework" as isolated noun phrases can trigger spam filters on .edu domains. The recommended subject variants in `PHASE_1_CONTACT_VERIFICATION.json` (Option A for Goodman, Option B for Elias) avoid these patterns. Use the recommended options.

---

## 3. Template Pre-Fill Status — What Needs User Input Before Send

Templates in `PHASE_1_EMAIL_TEMPLATES.md` are final. These are the only fields requiring user input once path is selected.

**Fields that need filling for ALL paths (fill once, applies to all 5 emails)**:

| Placeholder | Where It Appears | What to Enter | Time |
|-------------|-----------------|---------------|------|
| `{{YOUR_NAME}}` | Sign-off block, all 5 emails | Your name (e.g., "Anya") | 1 min |
| `{{YOUR_CONTACT_INFO}}` | Sign-off block, all 5 emails | Email address and/or phone | 1 min |

**Fields that are contact-specific (fill once per email, 5-10 min research each)**:

| Contact | Placeholder | Default/Pre-fill Available | Action |
|---------|-------------|--------------------------|--------|
| Goodman | `{{RECENT_JUST_SECURITY_ARTICLE}}` | No default — visit justsecurity.org/author/ryan-goodman/ | Find most recent article, copy title and date |
| Weiser | `{{RECENT_BRENNAN_CENTER_PUBLICATION}}` | Pre-fill available: "Analyzing the President's Executive Order on Mail Voting" (April 8, 2026) | Use this or check for anything newer |
| Chenoweth | `{{RECENT_CHENOWETH_WORK}}` | Pre-fill available: "Why Gen-Z Is Rising," Journal of Democracy, January 2026 | Use this — confirmed current as of May 15 |
| Bassin | `{{RECENT_PROTECT_DEMOCRACY_FILING}}` | No default — visit protectdemocracy.org/work for most recent case | Case name + court + filing date |
| Elias | Watson v. RNC / Louisiana v. Callais status | Both cases documented in Domain 1; verify current status at democracydocket.com | 5 min check |

**Path-specific addition (select the one block matching your path, already written in templates)**:

- Path A: "The complete 35-domain framework is production-ready and available now."
- Path A+37: "Domain 37 (Federal Executive Interference, 2026 Midterms) is available as a separately targeted document for election-protection contacts."
- Path B: "The framework is in active development — I'm soliciting practitioner feedback at this stage, before wider distribution."

**Total fill time after path selection**: approximately 40 minutes (5-10 min per contact-specific field, plus 5 min for shared fields).

---

## 4. Batch 1 May 15-17 Calendar

All times UTC. Convert: 16:00 UTC = 12:00 noon EDT.

### May 15 (Day 1) — Send Day

| UTC | Action |
|-----|--------|
| 09:00 | Morning setup: verify Gist URLs live (incognito check), run test email to self |
| 10:00 | Fill `{{YOUR_NAME}}`, `{{YOUR_CONTACT_INFO}}` in all 5 drafts |
| 10:30 | Spot-verify Elias email: confirm `melias@elias.law` (not perkinscoie.com) |
| 11:00 | Fill contact-specific placeholders: Goodman (find recent JS article), Weiser (April 8 pre-fill usable), Chenoweth (Jan 2026 pre-fill usable), Bassin (check PD website), Elias (check DD cases) |
| 12:00 | Final read of all 5 emails — confirm zero placeholders remain |
| 15:30 | Send test email to yourself from sending account; check spam |
| 16:00 | Send Email 1: Ryan Goodman — ryan.goodman@nyu.edu |
| 16:30 | Send Email 2: Wendy Weiser — wweiser@brennancenter.org |
| 17:00 | Send Email 3: Erica Chenoweth — erica_chenoweth@hks.harvard.edu |
| 17:30 | Send Email 4: Ian Bassin — ian@protectdemocracy.org |
| 18:00 | Send Email 5: Marc Elias — melias@elias.law |
| 18:30 | Post-send: log send times in BATCH_1_CONTACT_LOG.md; record Gist view count baseline; check for bounces in inbox |

### May 16 (Day 2) — Monitor + Wave 2 Prep

| UTC | Action |
|-----|--------|
| 10:00 | Morning check: any replies overnight? Any bounce notifications? Update BATCH_1_CONTACT_LOG.md |
| 14:00 | Check Gist view counts — record delta since baseline |
| 18:00 | Update Google Sheets Tab 2 metrics; cumulative reply rate |
| 20:00 | Begin Wave 2 contact verification (5 contacts from DISTRIBUTION_OUTREACH_CONTACTS.md Tier 1 Wave 2 list) |

### May 17 (Day 3) — Contingency Assessment Gate

| UTC | Action |
|-----|--------|
| 09:00 | Day 3 trigger evaluation: is reply rate ≥8%? (= at least 1 substantive reply from 5 sends) |
| 10:00 | If <8%: re-verify all 5 addresses on institutional websites (25 min); diagnose delivery |
| 14:00 | Wave 2 go/no-go decision: can Wave 2 launch May 20 on schedule? |
| 20:00 | End-of-day metrics; record in BATCH_1_CONTACT_LOG.md; brief orchestrator |

---

## 5. Wave 1 Execution Checklist — Day-by-Day

Copy this section, execute in order.

### Day 1 (May 15)

- [ ] Gist URLs live — all 3 verified in incognito (proposal, exec summary, litigation tracker)
- [ ] Test email to self — inbox delivery confirmed, no spam flag
- [ ] `{{YOUR_NAME}}` and `{{YOUR_CONTACT_INFO}}` filled in all 5 drafts
- [ ] Goodman placeholder filled (recent JS article)
- [ ] Weiser placeholder filled (April 8 pre-fill or newer)
- [ ] Chenoweth placeholder filled (Jan 2026 pre-fill confirmed)
- [ ] Bassin placeholder filled (recent PD filing from website)
- [ ] Elias placeholder filled (DD cases status confirmed)
- [ ] Path-specific block selected and correct in all 5 emails (A / A+37 / B — one block only)
- [ ] Zero `{{...}}` strings remaining in any draft
- [ ] Goodman sent at 16:00 UTC — timestamp logged
- [ ] Weiser sent at 16:30 UTC — timestamp logged
- [ ] Chenoweth sent at 17:00 UTC — timestamp logged
- [ ] Bassin sent at 17:30 UTC — timestamp logged
- [ ] Elias sent at 18:00 UTC — timestamp logged
- [ ] Post-send: Gist baseline view count recorded; zero bounces confirmed

### Day 2 (May 16)

- [ ] Morning reply check (10:00 UTC) — BATCH_1_CONTACT_LOG.md updated
- [ ] Bounce check — confirm zero in inbox / spam
- [ ] Gist view count delta recorded
- [ ] Metrics dashboard updated (Tab 2)
- [ ] Wave 2 prep started — 5 contacts identified from tier-1-contact-batches.md

### Day 3 (May 17)

- [ ] Day 3 gate evaluated at 09:00 UTC — reply rate ≥8%?
  - [ ] YES: proceed to Wave 2 May 20 on schedule
  - [ ] NO: run delivery diagnosis (see Section 6), log in DISTRIBUTION_EXECUTION_LOG.md
- [ ] Wave 2 go/no-go confirmed at 14:00 UTC
- [ ] End-of-day metrics recorded — 3-line summary to orchestrator

**Total time per day**: Day 1 = 60 min setup + 3 hours send window = ~90 min active; Day 2 = 20 min; Day 3 = 30-45 min.

---

## 6. Contingency Prep

**Trigger threshold**: Bounce rate >10% OR zero substantive replies by end of Day 3.

### If Bounce Rate >10%

Most likely cause: one or two stale addresses. Diagnosis sequence (20 min):

1. Identify bounced addresses from inbox bounce notifications
2. Re-verify on institutional websites (links in Section 1)
3. Use alternate addresses from Section 1 table — all alternates are pre-identified
4. Resend to corrected address within 24 hours using revised subject line (remove any "framework" or "reform" noun phrases from subject)
5. Do not send Wave 2 until bounce rate is confirmed <5%

**Secondary email addresses ready** (fallback if primary bounces):

| Contact | Primary | Fallback |
|---------|---------|---------|
| Goodman | ryan.goodman@nyu.edu | ryan@justsecurity.org |
| Weiser | wweiser@brennancenter.org | brennancenter.org/contact form |
| Chenoweth | erica_chenoweth@hks.harvard.edu | echenoweth@harvard.edu |
| Bassin | ian@protectdemocracy.org | protectdemocracy.org/contact form |
| Elias | melias@elias.law | press@democracydocket.com (route via comms) |

### If Zero Substantive Replies by Day 3

This is an early warning, not a failure signal — Harvard and Brennan Center have 5-10 day response cycles. Steps:

1. Check that Goodman and Elias (fastest responders, 2-3 day cycle) have not replied — if either has, trigger is not actually firing
2. Run delivery self-test (test email to self from same account)
3. Scan inbox for any auto-replies that may indicate delivery (out-of-office = confirmed delivery)
4. If no delivery indicators at all from any of the 5: delivery issue suspected — check sender account for spam flagging before Wave 2
5. Pre-written subject line escalation variants are in `PHASE_1_WAVE_1_EXECUTION_DASHBOARD.md` Section 5, Trigger 1 Action table — use those for any resend

### Phone Contact List (if needed)

No verified direct phone numbers are in the contact files. All 5 organizations have switchboards listed on institutional websites. For Elias Law Group: main line is at elias.law/contact. Use only if email delivery is confirmed failed after 48 hours and the DEA deadline (May 28) creates time pressure.

### 42+ Backup Contacts Ready

If Wave 1 response rate falls below 12% at Day 7, the full backup contact pool is documented in `PHASE_1_CONTINGENCY_STRATEGY.md` Section 4. Pre-written escalation messaging by sector (law schools, civil rights orgs, state AGs, labor) is in Section 3 of that document. No additional prep is needed — these are copy-paste ready.

---

*Prep completed: May 15, 2026. All contact verification is live-checked against institutional websites this session. One discrepancy flagged and resolved (Elias email domain). Templates are final — no edits needed before send. Path selection is the only remaining trigger.*
