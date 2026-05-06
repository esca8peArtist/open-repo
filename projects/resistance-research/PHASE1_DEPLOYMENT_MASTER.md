---
title: "Phase 1 Deployment Master Checklist"
created: 2026-05-06
session: "8xx (current)"
status: EXECUTE ON PATH DECISION — ZERO ADDITIONAL SETUP REQUIRED
purpose: "Single authoritative checklist from path decision to Batch 1 sent + social queued. Supersedes all prior checklists."
time_to_completion: "4 hours from path decision"
path_decision_gate: "Fill in [ ] Path A / [ ] Path A+37 / [ ] Path B before starting"
---

# Phase 1 Deployment Master Checklist

**Selected path**: [ ] Path A   [ ] Path A+37 (recommended)   [ ] Path B

**Decision time**: _______________

**Target: Batch 1 all sent by**: _______________ (Decision + 4h)

---

## Infrastructure Status Snapshot (current as of May 6, 2026)

Everything below is already built. No setup is required. This checklist executes.

| Component | Status | File |
|-----------|--------|------|
| 6 canonical Gists | LIVE | `DISTRIBUTION_GIST_URLS.md` |
| fill_templates.py script | WRITTEN TO DISK | `scripts/fill_templates.py` |
| verify_contacts.py script | WRITTEN TO DISK | `scripts/verify_contacts.py` |
| All 5 Batch 1 emails (personalized) | READY | `execution/phase-1-personalized-batch-1.md` |
| All 8 Batch 2 emails | READY | `execution/phase-1-personalized-batch-2.md` |
| All 12 Batch 3 emails | READY | `execution/phase-1-personalized-batch-3.md` |
| Substack drafts (7 posts) | READY | `distribution-substack-drafts.md` |
| Reddit templates (8 posts) | READY | `distribution-reddit-templates.md` |
| HN posts (2 posts) | READY | `PHASE1_EXECUTION_MATERIALS/HN_STRATEGY.md` |
| Twitter/X threads (4 threads) | READY | `PHASE1_EXECUTION_MATERIALS/SOCIAL_POST_SEQUENCE.md` |
| Social timing schedule | READY | `PHASE1_EXECUTION_MATERIALS/SOCIAL_POST_SEQUENCE.md` |
| Domain 37 contact list | READY | `DOMAIN_37_SEQUENCING_PLAN.md` |
| 35-domain framework | CURRENT THROUGH MAY 1 | `domains/` directory |
| Batch 1 contacts | POSITION-VERIFIED April 29 | `PHASE_1_CONTACT_VERIFICATION.json` |
| Field-fill placeholder inventory | COMPLETE | `field-fill-automation-spec.md` |
| Deployment execution checklist | COMPLETE | `distribution-checklist-template.md` |

**Sole remaining requirement**: User path decision + user identity fields (YOUR_NAME, YOUR_CONTACT_INFO).

---

## PRE-CHECKLIST (5 minutes — verify these before starting the clock)

- [ ] GitHub gist.github.com is accessible — visit https://gist.github.com/esca8peArtist
      Spot-check: the Proposal Gist loads at
      https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261
- [ ] `scripts/fill_templates.py` exists: `ls /home/awank/dev/SuperClaude_Framework/scripts/fill_templates.py`
- [ ] `scripts/verify_contacts.py` exists: `ls /home/awank/dev/SuperClaude_Framework/scripts/verify_contacts.py`
- [ ] Email client is open and ready to compose
- [ ] Path decision committed (check box above)

If all five are true: **start the clock.**

---

## BLOCK 1 (T+0:00 — 0:10): Script Configuration

- [ ] Open `scripts/fill_templates.py`
- [ ] Set `DISTRIBUTION_PATH = "[A / A+37 / B]"`
- [ ] Set `FIELD_VALUES["{{YOUR_NAME}}"]` = your name for outreach sign-offs
- [ ] Set `FIELD_VALUES["{{YOUR_CONTACT_INFO}}"]` = your email address
- [ ] Set `FIELD_VALUES["[your Substack handle]"]` = your Substack username
- [ ] Leave `{{DOMAIN_37_URL}}` empty (Path A+37 — fill after Block 2)
- [ ] Set `DRY_RUN = True`
- [ ] Run: `uv run python scripts/fill_templates.py`
- [ ] Confirm output ends with no {{YOUR_NAME}} or {{YOUR_CONTACT_INFO}} warnings

**Path A or B**: Proceed to Block 3.
**Path A+37**: Proceed to Block 2.

---

## BLOCK 2 (T+0:10 — 0:20): Domain 37 Gist Creation [PATH A+37 ONLY]

- [ ] Navigate to https://gist.github.com/new (confirm logged in as esca8peArtist)
- [ ] Filename: `domain-37-federal-executive-interference-2026-midterms.md`
- [ ] Description: `Domain 37 — Federal Executive Interference in the 2026 Midterms | Democratic Renewal Research Framework`
- [ ] Paste: Zone A header from `distribution-gist-template.md` Section C (Domain 37 pre-filled version)
- [ ] Paste: Advocacy windows table from `distribution-gist-template.md` Section F
- [ ] Paste: Full content of `domains/domain-37-federal-executive-interference-2026-midterms.md`
- [ ] Paste: Zone D footer from `distribution-gist-template.md` Section B
- [ ] Set visibility to **Public** — click "Create public gist"
- [ ] Copy the Gist URL from the browser address bar

Domain 37 Gist URL: `___________________________________________________________`

- [ ] Record in `DISTRIBUTION_GIST_URLS.md` (Domain 37 row)
- [ ] Set `FIELD_VALUES["{{DOMAIN_37_URL}}"]` in fill_templates.py to this URL

---

## BLOCK 3 (T+0:20 — 0:30): Run Fill Script (Write Mode)

- [ ] Confirm all FIELD_VALUES are set (name, contact, Substack handle; Domain 37 URL if A+37)
- [ ] Set `DRY_RUN = False`
- [ ] Run: `uv run python scripts/fill_templates.py`
- [ ] Confirm: "WRITING FILES to scripts/filled_output/" followed by 4 filenames [WRITTEN]
- [ ] Confirm final line: "No warnings. All fields filled."

If warnings appear — resolve before proceeding:
- `UNFILLED: {{DOMAIN_37_URL}}` → create Domain 37 Gist (Block 2)
- `WARNING: YOUR_NAME not set` → edit FIELD_VALUES, re-run
- Any other `{{...}}` remaining → identify field, edit, re-run

---

## BLOCK 4 (T+0:30 — 0:45): Output Verification

- [ ] Open `scripts/filled_output/PHASE_1_EMAIL_TEMPLATES.md`
- [ ] Email 1: no remaining `{{...}}` strings, path-specific block resolved correctly
- [ ] Email 2-5: spot-check — all show your name, correct Gist URLs
- [ ] Open `scripts/filled_output/distribution-substack-drafts.md`
- [ ] Post 1: Proposal URL replaced, Substack handle filled
- [ ] Open `scripts/filled_output/distribution-reddit-templates.md`
- [ ] r/PoliticalScience post: Proposal URL in body, no `[PROPOSAL_LINK]` remaining

---

## BLOCK 5 (T+1:00 — 1:25): Batch 1 Contact Verification

Final spot-verification for all 5 contacts. Last position verification: April 29, 2026.
Re-verify now (2-3 minutes per contact):

- [ ] Ryan Goodman: https://www.law.nyu.edu/faculty/profiles/GOODMANR
      Confirm title "Co-Editor-in-Chief, Just Security; Ehrenkranz Professor"
      Email: ryan.goodman@nyu.edu (alt: ryan@justsecurity.org)
      Note recent Just Security article for `{{RECENT_JUST_SECURITY_ARTICLE}}`:
      Article title: _________________

- [ ] Wendy Weiser: https://www.brennancenter.org/experts/wendy-weiser
      Confirm title "Vice President, Democracy Program"
      Email: wweiser@brennancenter.org
      Note recent publication for `{{RECENT_WEISER_PUBLICATION}}`:
      Publication: _________________

- [ ] Erica Chenoweth: https://www.hks.harvard.edu/faculty/erica-chenoweth
      Confirm title "Frank Stanton Professor; Director, Nonviolent Action Lab"
      Email: echenoweth@hks.harvard.edu (alt: echenoweth@harvard.edu)
      Note recent Lab publication for `{{RECENT_CHENOWETH_WORK}}`:
      Publication: _________________

- [ ] Ian Bassin: https://protectdemocracy.org/about/team/
      Confirm title "Co-Founder and Executive Director"
      Email: ian@protectdemocracy.org
      Note recent filing or public statement for `{{BASSIN_RECENT_FILING}}`:
      Filing/statement: _________________

- [ ] Marc Elias: https://democracydocket.com/about/
      Confirm title "Founder, Democracy Docket"
      Email: marc@democracydocket.com (alt: melias@perkinscoie.com)
      Note recent active Democracy Docket case for `{{ELIAS_RECENT_CASE}}`:
      Case: _________________

Also run the verify_contacts.py script to confirm nothing has changed:
`uv run python scripts/verify_contacts.py --batch 1`

---

## BLOCK 6 (T+1:25 — 1:50): Manual Content Placeholder Fill + Draft Prep

For each email: open filled template from `scripts/filled_output/PHASE_1_EMAIL_TEMPLATES.md`,
copy to email client draft, fill the manual placeholders:

- [ ] **Email 1 draft (Goodman)**: Replace `{{RECENT_JUST_SECURITY_ARTICLE}}` with Block 5 finding
      Subject line selected: Option [ ] A [ ] B [ ] C
      Recipient: ryan.goodman@nyu.edu

- [ ] **Email 2 draft (Weiser)**: Replace `{{RECENT_WEISER_PUBLICATION}}` with Block 5 finding
      Subject line selected
      Recipient: wweiser@brennancenter.org

- [ ] **Email 3 draft (Chenoweth)**: Replace `{{RECENT_CHENOWETH_WORK}}` with Block 5 finding
      Subject line selected
      Recipient: echenoweth@hks.harvard.edu

- [ ] **Email 4 draft (Bassin)**: Replace `{{BASSIN_RECENT_FILING}}` with Block 5 finding
      Subject line selected
      Recipient: ian@protectdemocracy.org

- [ ] **Email 5 draft (Elias)**: Replace `{{ELIAS_RECENT_CASE}}` with Block 5 finding
      Subject line selected
      Recipient: marc@democracydocket.com

- [ ] Final read-through of all five drafts — no remaining `{{...}}`, no broken links

---

## BLOCK 7 (T+2:00 — 2:30): Substack Post 1 Preparation

- [ ] Open `scripts/filled_output/distribution-substack-drafts.md`
- [ ] Copy Post 1 body text (launch overview / executive summary post)
- [ ] Open Substack dashboard: https://[handle].substack.com/publish
- [ ] Create new post — paste Post 1 body
- [ ] Title: use draft title (do not spend more than 5 minutes on alternatives)
- [ ] Post type: "Free"
- [ ] Publish schedule: T+7 days, Tuesday or Wednesday, 9–11 AM ET
      Target date: _______________ Target time: _______________
- [ ] Save as draft (do not publish yet)
- [ ] Verify all links in post preview resolve correctly

---

## BLOCK 8 (T+2:30 — 3:00): Reddit + HN Post Preparation

**Reddit (three posts):**

- [ ] Open `scripts/filled_output/distribution-reddit-templates.md`
- [ ] Copy r/PoliticalScience post → save to `scripts/filled_output/reddit-r-polisci.md`
      Schedule: T+2 (_______________) at 10 AM–12 PM ET
      All links verified: [ ]

- [ ] Copy r/law post → save to `scripts/filled_output/reddit-r-law.md`
      Schedule: T+7 (_______________) at 10 AM–12 PM ET
      All links verified: [ ]

- [ ] Copy r/politics post → save to `scripts/filled_output/reddit-r-politics.md`
      Schedule: T+8 (_______________) at 12 PM–2 PM ET
      All links verified: [ ]

- [ ] Set calendar reminders for each Reddit post date

**HackerNews (Show HN post):**

- [ ] Open `PHASE1_EXECUTION_MATERIALS/HN_STRATEGY.md`
- [ ] Copy the Primary Post Template body (methodology angle)
- [ ] Save to `scripts/filled_output/hn-show-hn-post.md`
- [ ] In the HN post body, fill in the two `[link]` placeholders:
      Executive Summary: https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4
      Litigation Tracker: https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0
- [ ] Set calendar reminder: T+3 (_______________) at 9 AM–11 AM ET for HN submission

**Twitter/X (Thread 1):**

- [ ] Open `PHASE1_EXECUTION_MATERIALS/SOCIAL_POST_SEQUENCE.md`
- [ ] Copy Thread 1 (6 tweets) to a text file
- [ ] Replace `[{{YOUR_CONTACT_INFO}}]` in Tweet 6 with your contact info
- [ ] Save to `scripts/filled_output/twitter-thread-1.md`
- [ ] Set calendar reminder: T+1 (_______________) at 9 AM ET

---

## BLOCK 9 (T+3:00 — 3:30): PATH A+37 ONLY — Phase 1b Prep

**Path A or B**: Skip this block.

**Path A+37**: Prepare the Domain 37 election-protection organization emails for Phase B.
These are NOT sent now — send at Week 9. Prepare while context is fresh.

- [ ] Open `DOMAIN_37_SEQUENCING_PLAN.md` — locate Template D37-1
- [ ] Fill Template D37-1 with Domain 37 Gist URL (from Block 2)
- [ ] Save 7 per-organization draft versions to `scripts/filled_output/domain-37-emails/`:
      - `d37-brennan-center.md`
      - `d37-democracy-docket.md`
      - `d37-protect-democracy.md`
      - `d37-lawyers-committee.md`
      - `d37-aclu-vrp.md`
      - `d37-states-united.md`
      - `d37-common-cause.md`
- [ ] Each draft has correct Domain 37 Gist URL and advocacy window framing
- [ ] Set calendar reminder for Week 9 Phase B launch

---

## BLOCK 10 (T+3:30 — 3:45): Final QA

**Email QA:**
- [ ] 5 drafts in email client, each with recipient address, subject line, zero `{{...}}` strings
- [ ] Each body has at least 2 working Gist URLs
- [ ] Each sign-off shows your name and contact info
- [ ] Send order confirmed: Email 1 → 2 → 3 → 4 → 5 with 30-minute gaps

**Substack QA:**
- [ ] Post 1 is scheduled (not published immediately)
- [ ] Publication name/header is configured
- [ ] No `[your Substack handle]` placeholder remains

**Social QA:**
- [ ] Calendar reminders set: T+1 (Twitter), T+2 (Reddit r/PoliticalScience), T+3 (HN), T+7 (Substack Post 1 + r/law), T+8 (r/politics + Twitter Thread 2)
- [ ] HN post body saved and Gist URLs confirmed filled
- [ ] Twitter Thread 1 text saved and contact info filled

**Gist QA:**
- [ ] All 6 canonical Gists load — spot-check 2
- [ ] Path A+37 only: Domain 37 Gist loads and advocacy windows table renders

---

## BLOCK 11 (T+3:45 — 4:00): Monitoring Setup

- [ ] Create email label/folder: "Phase 1 Responses"
- [ ] Create filter: emails from ryan.goodman@nyu.edu, wweiser@brennancenter.org,
      echenoweth@hks.harvard.edu, ian@protectdemocracy.org, marc@democracydocket.com
      → auto-label "Phase 1 Responses" + star
- [ ] Note current Gist view counts (Proposal + Litigation Tracker) at send time:
      Proposal views: _______   Litigation Tracker views: _______
- [ ] Update `BATCH_1_CONTACT_LOG.md` — add header row if not present:
      | Contact | Send Time | Subject Used | Gist Views at Send | Notes |
- [ ] Set calendar reminders:
      T+7:  Publish Substack Post 1 + r/law post + Batch 2 emails (8 contacts)
      T+14: Substack Post 2 + r/politics + r/progressive + Batch 3 emails (12 contacts)
      T+21: Twitter Thread 4 (Domain 37 focus)
      T+56 (Week 8): Path A+37 only — Phase B decision point assessment

---

## BATCH 1 SEND SEQUENCE

Execute after Block 10 QA complete.

| # | Contact | Email | Send Time | Gap |
|---|---------|-------|-----------|-----|
| 1 | Ryan Goodman | ryan.goodman@nyu.edu | T+4:00 | — |
| 2 | Wendy Weiser | wweiser@brennancenter.org | T+4:30 | +30 min |
| 3 | Erica Chenoweth | echenoweth@hks.harvard.edu | T+5:00 | +30 min |
| 4 | Ian Bassin | ian@protectdemocracy.org | T+5:30 | +30 min |
| 5 | Marc Elias | marc@democracydocket.com | T+6:00 | +30 min |

After each send: record timestamp in `BATCH_1_CONTACT_LOG.md`.

---

## POST-LAUNCH MONITORING (T+4h through T+48h)

**T+1 day (also: post Twitter Thread 1 at 9 AM ET)**:
- Check for bounces and opens
- Post Twitter Thread 1

**T+2 days (also: post r/PoliticalScience)**:
- Check for responses; log in BATCH_1_CONTACT_LOG.md
- Post to r/PoliticalScience using saved `reddit-r-polisci.md`
- Monitor r/PoliticalScience thread for 24 hours; respond to substantive comments

**T+3 days (also: submit HN Show HN)**:
- Submit HN post (9 AM ET): title + URL + body from `hn-show-hn-post.md`
- Monitor HN thread for 6 hours; respond to comments

**T+7 days**:
- Publish Substack Post 1 (calendar reminder set in Block 11)
- Post to r/law
- Send Batch 2 emails (8 contacts — `execution/phase-1-personalized-batch-2.md`)
- Run contact verification for Batch 2: `uv run python scripts/verify_contacts.py --batch 2`

**If a response arrives from Batch 1**:
- Log immediately in BATCH_1_CONTACT_LOG.md
- Wait 4-8 hours before drafting reply
- Exception: direct factual questions — reply within 24 hours
- If positive response: reference it in the next institutional outreach batch

**If a Batch 1 email bounces**:
- Visit institutional website, confirm correct email format
- Resend to corrected address within 24 hours
- Log bounce and correction in BATCH_1_CONTACT_LOG.md

---

## PATH-SPECIFIC CALENDAR SUMMARY

### Path A
| Week | Email Batches | Social Posts | Substack |
|------|--------------|-------------|---------|
| 1 (T+0) | Batch 1 (5) | Twitter Thread 1, r/PoliticalScience, HN | — |
| 2 (T+7) | Batch 2 (8) | r/law, r/politics, Twitter Thread 2 | Post 1 |
| 3 (T+14) | Batch 3 (12) | r/progressive, r/AcademicFreedom, Twitter Thread 3 | Post 2 |
| 4+ | Follow-ups | HN Ask HN, Twitter Thread 4 | Posts 3-7 |

### Path A+37
| Phase | Timing | Action |
|-------|--------|--------|
| Phase 1a | Weeks 1-8 | Identical to Path A |
| Phase 1b prep | Day 0 (Block 9) | 7 Domain 37 email drafts saved |
| Phase B launch | Week 9 (T+56) | Domain 37 emails to 7 election-protection orgs |
| Phase B social | Week 9 | Twitter Thread 4 (Domain 37 focus) |

### Path B
| Phase | Timing | Action |
|-------|--------|--------|
| Current | Now | All infrastructure staged; no distribution |
| Research phase | Weeks 1-4 | Domain 37b + 37a + 31x full research (3 sessions) |
| Distribution launch | ~May 26-June 2 | Execute Blocks 1-11 with updated framework |
| Note | | NVRA quiet period begins August 7 — distribution must complete before then |

---

## REFERENCE MAP — Where Everything Lives

| What you need | File |
|---------------|------|
| Gist URLs (all 6 live + Domain 37 pending) | `DISTRIBUTION_GIST_URLS.md` |
| fill_templates.py (field replacement script) | `scripts/fill_templates.py` |
| verify_contacts.py (contact verification script) | `scripts/verify_contacts.py` |
| Batch 1-3 personalized emails | `execution/phase-1-personalized-batch-1/2/3.md` |
| Substack drafts (7 posts) | `distribution-substack-drafts.md` |
| Reddit templates (8 posts + strategic layer) | `distribution-reddit-templates.md` + `PHASE1_EXECUTION_MATERIALS/REDDIT_OUTREACH_THREADS.md` |
| HN posts + platform norms | `PHASE1_EXECUTION_MATERIALS/HN_STRATEGY.md` |
| Twitter/X threads + social schedule | `PHASE1_EXECUTION_MATERIALS/SOCIAL_POST_SEQUENCE.md` |
| Path decision framework (choose A/A+37/B) | `execution-plans/EXECUTION_PATHS_DECISION_FRAMEWORK.md` |
| Detailed per-path execution plans | `execution-plans/EXECUTION_PLAN_PATH_[A/A_PLUS_37/B].md` |
| Gist layout and rendering constraints | `gist-template-structure.md` |
| Field-fill placeholder inventory | `field-fill-automation-spec.md` |
| Domain 37 Phase B contacts + sequencing | `DOMAIN_37_SEQUENCING_PLAN.md` |
| STAGE directories (per-path deploy checklists) | `STAGE_PATH_A/`, `STAGE_PATH_A_DOMAIN37/`, `STAGE_PATH_B/` |
| Full 4-hour checklist (alternate format) | `distribution-checklist-template.md` |
| Contact verification database (150+ contacts) | `scripts/verify_contacts.py` (CONTACTS list) |
| Phase 1 execution readiness audit | `PHASE_1_EXECUTION_READINESS.md` |
| Contact tracking log | `BATCH_1_CONTACT_LOG.md` |

---

## QUICK-REFERENCE TIME BUDGET

| Block | Description | Time |
|-------|-------------|------|
| Pre-check | Verify accounts + files | 5 min |
| Block 1 | Script config + dry run | 10 min |
| Block 2 | Domain 37 Gist (A+37 only) | 10 min |
| Block 3 | Fill script write mode | 5 min |
| Block 4 | Output verification | 15 min |
| Block 5 | Contact verification | 25 min |
| Block 6 | Content placeholder fill + drafts | 25 min |
| Block 7 | Substack Post 1 prep | 30 min |
| Block 8 | Reddit + HN + Twitter prep | 30 min |
| Block 9 | Domain 37 emails (A+37 only) | 30 min |
| Block 10 | Final QA | 15 min |
| Block 11 | Monitoring setup | 15 min |
| **Send** | Batch 1 emails (staggered 30 min each) | **120 min** |
| **Total** | | **~4 hours** |

---

*Phase 1 Deployment Master Checklist. Created May 6, 2026.*
*Consolidates: distribution-checklist-template.md, PHASE_1_EXECUTION_INFRASTRUCTURE.md,*
*GIST_DEPLOYMENT_READINESS.md, PHASE_1_PREEXECUTION_KIT.md, and PHASE1_EXECUTION_MATERIALS/.*
*This document supersedes all prior deployment checklists for day-of-decision execution.*
