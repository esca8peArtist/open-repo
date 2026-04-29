---
title: "Phase 1 Execution Checklist — Step-by-Step Launch Guide"
created: 2026-04-30
status: ready-to-execute-on-path-decision
purpose: "Definitive step-by-step sequence from path decision to Batch 1 emails sent, with time estimates and dependencies"
path_compatibility: "Identical across Path A / Path A+37 / Path B through Block 6; diverges only at Block 7 (path-specific additions)"
---

# Phase 1 Execution Checklist

**Trigger**: User announces path decision (A / A+37 / B)
**Estimated time to Batch 1 emails sent**: 3.0–4.5 hours from decision
**Who executes**: User (email sending, Gist creation, personalization sign-off); agent available for content support on request

---

## Pre-Conditions (verify before starting clock)

- [ ] `democratic-renewal-proposal.md` — file exists, no uncommitted edits outstanding
- [ ] `democratic-renewal-executive-summary.md` — file exists, production-ready
- [ ] `litigation-tracker-2026.md` — file exists
- [ ] `first-amendment-suppression.md` — file exists
- [ ] `environmental-rollbacks-tracker.md` — file exists
- [ ] `police-brutality-consent-decree-tracker.md` — file exists
- [ ] GitHub account is logged in at gist.github.com
- [ ] Email client is open and sending-capable
- [ ] `PHASE_1_EMAIL_TEMPLATES.md` is open (built this session — contains all five Batch 1 drafts)
- [ ] `PHASE_1_CONTACT_VERIFICATION.json` is open (built this session — contains verified contact data)

**Known pending correction (5 minutes, do this first)**:
Domain 1 Section 4.2 still contains "effectively lapsed" FISA framing that was overtaken by the April 29 House passage of S.1318. Before creating Gists, add one sentence at the top of Section 4.2: "Updated April 29: House passed S.1318 235-191; Senate action pending by May 1. The lapse did not occur. Civil liberties advocacy shifts to next-cycle warrant reform." The correction language is ready in CHECKIN.md item 0. This is the only content correction needed before Gist creation.

---

## Block 0: Domain 1 FISA Correction (5 minutes)

**Who**: User or agent
**Dependency**: None — do this first, before Gist creation

- [ ] Open `domains/domain-01-voting-rights-elections.md`
- [ ] Navigate to Section 4.2
- [ ] Insert correction sentence at top of Section 4.2 (language in CHECKIN.md item 0)
- [ ] Save file
- [ ] Mark complete — proceed to Block 1

**Time**: 5 minutes

---

## Block 1: Gist Creation (30–45 minutes)

**Who**: User
**Dependency**: Block 0 complete
**Tool**: https://gist.github.com (account: esca8peArtist — the May Day Guide confirms this workflow works)

Create one public Gist per document. For each Gist:
1. Go to gist.github.com → click "+" or "New gist"
2. Paste the file name in the filename field (e.g., `democratic-renewal-proposal.md`)
3. Paste the Markdown content (copy from local file)
4. Set to "Public" (not Secret)
5. Click "Create public gist"
6. Copy the resulting URL — record it in the URL log below

**Document 1: Full Proposal**
- Local file: `projects/resistance-research/democratic-renewal-proposal.md`
- Gist filename to use: `democratic-renewal-proposal.md`
- URL recorded: `_______________________________________________`
- Estimated Gist creation time: 8–10 minutes (large file)

**Document 2: Executive Summary**
- Local file: `projects/resistance-research/democratic-renewal-executive-summary.md`
- Gist filename to use: `democratic-renewal-executive-summary.md`
- URL recorded: `_______________________________________________`
- Estimated Gist creation time: 3–4 minutes

**Document 3: Litigation Tracker**
- Local file: `projects/resistance-research/litigation-tracker-2026.md`
- Gist filename to use: `litigation-tracker-2026.md`
- URL recorded: `_______________________________________________`
- Estimated Gist creation time: 5–6 minutes

**Document 4: First Amendment Suppression Tracker**
- Local file: `projects/resistance-research/first-amendment-suppression.md`
- Gist filename to use: `first-amendment-suppression.md`
- URL recorded: `_______________________________________________`
- Estimated Gist creation time: 3–4 minutes

**Document 5: Environmental Rollbacks Tracker**
- Local file: `projects/resistance-research/environmental-rollbacks-tracker.md`
- Gist filename to use: `environmental-rollbacks-tracker.md`
- URL recorded: `_______________________________________________`
- Estimated Gist creation time: 3–4 minutes

**Document 6: Police Consent Decree Tracker**
- Local file: `projects/resistance-research/police-brutality-consent-decree-tracker.md`
- Gist filename to use: `police-brutality-consent-decree-tracker.md`
- URL recorded: `_______________________________________________`
- Estimated Gist creation time: 3–4 minutes

**Path A+37 only — Document 7: Domain 37**
- Local file: `projects/resistance-research/domains/domain-37-federal-executive-interference-2026-midterms.md`
- Gist filename to use: `domain-37-federal-executive-interference-2026-midterms.md`
- URL recorded: `_______________________________________________`
- Estimated Gist creation time: 6–8 minutes (large file)

**Block 1 complete when**: All 6 (or 7 for Path A+37) URLs are recorded above.

**Total Block 1 time**: 30–45 minutes

---

## Block 2: URL Fill-In (20–30 minutes)

**Who**: User (find-replace; agent can assist if needed)
**Dependency**: Block 1 complete (all URLs recorded)

Open each template file and replace `[link]` placeholders with actual Gist URLs per the mapping below.

### URL Mapping

| Template Placeholder Type | Replace With |
|--------------------------|-------------|
| "full proposal" / "28-domain proposal" / "35-domain proposal" | Document 1 URL (full proposal Gist) |
| "executive summary" / "two-page summary" | Document 2 URL (executive summary Gist) |
| "litigation tracker" | Document 3 URL |
| "first amendment tracker" / "first amendment suppression" | Document 4 URL |
| "environmental rollbacks" | Document 5 URL |
| "police consent decree" / "consent decree tracker" | Document 6 URL |
| "domain 37" (Path A+37 only) | Document 7 URL |

### Files to Update

**File 1**: `projects/resistance-research/distribution-substack-drafts.md`
- [ ] Find all `[link]` instances — count before starting: _____
- [ ] Replace each with appropriate URL from mapping above
- [ ] Verify: no `[link]` placeholders remain

**File 2**: `projects/resistance-research/distribution-reddit-templates.md`
- [ ] Find all `[link]` instances — count before starting: _____
- [ ] Replace each with appropriate URL from mapping above
- [ ] Verify: no `[link]` placeholders remain

**File 3**: `projects/resistance-research/distribution-institutional-outreach-templates.md`
- [ ] Find all `[link]` instances — count before starting: _____
- [ ] Replace each with appropriate URL from mapping above
- [ ] Replace all `[Your name]` with preferred outreach name
- [ ] Replace all `[Contact information]` with email address (+ Signal handle if desired)
- [ ] Verify: no `[link]`, `[Your name]`, or `[Contact information]` placeholders remain

**File 4**: `projects/resistance-research/PHASE_1_EMAIL_TEMPLATES.md` (built this session)
- [ ] Find all `{{PROPOSAL_URL}}` instances — replace with Document 1 URL
- [ ] Find all `{{EXEC_SUMMARY_URL}}` instances — replace with Document 2 URL
- [ ] Find all `{{LITIGATION_TRACKER_URL}}` instances — replace with Document 3 URL
- [ ] Verify: no `{{...}}` URL placeholders remain

**Block 2 complete when**: All four files have had URL placeholders replaced and verified.

**Total Block 2 time**: 20–30 minutes

---

## Block 3: Contact Email Verification (30–45 minutes)

**Who**: User
**Dependency**: None — can run in parallel with Block 2 if two browser tabs are open

All five Batch 1 positions have been verified as of April 29, 2026 (see `BATCH_1_CONTACT_VERIFICATION.md` and `PHASE_1_CONTACT_VERIFICATION.json`). This block is final email address verification only — 2–5 minutes per contact.

### Verification Steps Per Contact

For each contact: visit the verification URL, confirm email format, record verified address.

**Contact 1: Ryan Goodman**
- Verify URL: https://justsecurity.org/about-us/ and https://www.law.nyu.edu/faculty/profiles/GOODMANR
- Expected format: ryan.goodman@nyu.edu (NYU first.last format, confirmed) OR ryan@justsecurity.org
- Verified email: `_______________________________________________`
- Date verified: `_______________________________________________`

**Contact 2: Wendy Weiser**
- Verify URL: https://www.brennancenter.org/experts/wendy-r-weiser
- Expected format: wweiser@brennancenter.org
- Verified email: `_______________________________________________`
- Date verified: `_______________________________________________`

**Contact 3: Erica Chenoweth**
- Verify URL: https://www.hks.harvard.edu/faculty/erica-chenoweth
- Expected format: echenoweth@hks.harvard.edu (confirmed HKS format)
- Verified email: `_______________________________________________`
- Date verified: `_______________________________________________`

**Contact 4: Ian Bassin**
- Verify URL: https://protectdemocracy.org/about/team/
- Expected format: ian@protectdemocracy.org
- Verified email: `_______________________________________________`
- Date verified: `_______________________________________________`

**Contact 5: Marc Elias**
- Verify URL: https://www.democracydocket.com/about/ and https://www.perkinscoie.com/people/marc-e-elias
- Expected format: melias@perkinscoie.com OR marc@democracydocket.com
- Verified email: `_______________________________________________`
- Date verified: `_______________________________________________`

**Block 3 complete when**: All five email addresses are recorded above with verification dates.

**Total Block 3 time**: 30–45 minutes (can overlap with Block 2)

---

## Block 4: Email Personalization (60–90 minutes)

**Who**: User
**Dependency**: Block 2 complete (URLs filled in), Block 3 complete (emails verified)
**Source**: `PHASE_1_EMAIL_TEMPLATES.md` (built this session) — contains five draft emails with `{{placeholder}}` fields ready to fill

For each contact, open the corresponding draft in `PHASE_1_EMAIL_TEMPLATES.md` and complete the following:

### Contact 1: Ryan Goodman (Template: Goodman-Draft)
- [ ] Fill `{{RECENT_JUST_SECURITY_ARTICLE}}` — find his most recent published piece at justsecurity.org (title + date)
- [ ] Fill `{{YOUR_NAME}}` with preferred sign-off name
- [ ] Fill `{{YOUR_CONTACT_INFO}}` with email and optional phone
- [ ] Select subject line variant (three options provided in template)
- [ ] Read draft aloud — confirm the specific finding references sound accurate
- [ ] Copy to email client (Gmail / Outlook / etc.)
- [ ] Add verified email address to To: field
- [ ] BCC tracking address if using one
- [ ] Do not send yet — hold for Block 6

### Contact 2: Wendy Weiser (Template: Weiser-Draft)
- [ ] Fill `{{RECENT_BRENNAN_CENTER_PUBLICATION}}` — check brennancenter.org for most recent Weiser piece or Brennan Center voting rights report (title + date)
- [ ] Fill `{{YOUR_NAME}}`
- [ ] Fill `{{YOUR_CONTACT_INFO}}`
- [ ] Select subject line variant
- [ ] Review SAVE Act specific references — confirm they match Domain 1 content
- [ ] Copy to email client
- [ ] Add verified email to To: field
- [ ] Hold for Block 6

### Contact 3: Erica Chenoweth (Template: Chenoweth-Draft)
- [ ] Fill `{{RECENT_CHENOWETH_WORK}}` — her Journal of Democracy piece "Why Gen-Z Is Rising" (January 2026) is pre-filled in template; verify it's still the most recent or update
- [ ] Fill `{{YOUR_NAME}}`
- [ ] Fill `{{YOUR_CONTACT_INFO}}`
- [ ] The Harvard funding freeze hook is pre-filled — confirm still accurate as of send date
- [ ] Select subject line variant
- [ ] Copy to email client
- [ ] Add verified email to To: field
- [ ] Hold for Block 6

### Contact 4: Ian Bassin (Template: Bassin-Draft)
- [ ] Fill `{{RECENT_PROTECT_DEMOCRACY_FILING}}` — check protectdemocracy.org for most recent litigation activity (case name, court, date)
- [ ] Fill `{{YOUR_NAME}}`
- [ ] Fill `{{YOUR_CONTACT_INFO}}`
- [ ] SPLC/Domain 29 hook is pre-filled — confirm SPLC indictment framing is current
- [ ] Select subject line variant
- [ ] Copy to email client
- [ ] Add verified email to To: field
- [ ] Hold for Block 6

### Contact 5: Marc Elias (Template: Elias-Draft)
- [ ] Fill `{{RECENT_DEMOCRACY_DOCKET_CASE}}` — check democracydocket.com for most recent active case (Watson v. RNC or Louisiana v. Callais are pre-filled as options; verify status)
- [ ] Fill `{{YOUR_NAME}}`
- [ ] Fill `{{YOUR_CONTACT_INFO}}`
- [ ] Select subject line variant
- [ ] Copy to email client
- [ ] Add verified email to To: field
- [ ] Hold for Block 6

**Block 4 complete when**: All five emails are drafted in the email client, addressed, and ready to send.

**Total Block 4 time**: 60–90 minutes

---

## Block 5: Tracking Infrastructure Setup (20–30 minutes)

**Who**: User
**Dependency**: None — can run at any time after Block 3
**Purpose**: Contact log is required for Batch 2 planning and response follow-up

### Create Contact Log

Open Google Sheets, Excel, or a plain text file. Create the following columns:

```
ID | Name | Institution | Title | Verified Email | Date Sent | Time Sent | Open (Y/N) | Response (Y/N) | Response Date | Response Summary | Follow-Up Date | Follow-Up Sent | Notes
```

Pre-populate Batch 1 rows:

| ID | Name | Institution | Title | Verified Email |
|----|------|-------------|-------|----------------|
| T1-001 | Ryan Goodman | Just Security / NYU Law | Co-Editor-in-Chief; Ehrenkranz Prof. | [from Block 3] |
| T1-002 | Wendy Weiser | Brennan Center / NYU | VP, Democracy Program | [from Block 3] |
| T1-003 | Erica Chenoweth | Harvard Kennedy School | Frank Stanton Professor; Dir., Nonviolent Action Lab | [from Block 3] |
| T1-004 | Ian Bassin | Protect Democracy | Co-Founder & Executive Director | [from Block 3] |
| T1-005 | Marc Elias | Democracy Docket / Perkins Coie | Founder; Partner | [from Block 3] |

### Email Tracking (Optional but Recommended)

Select one:
- **Mailtrack** (free): Install Chrome extension at mailtrack.io — adds open tracking to Gmail
- **Superhuman**: Built-in read receipts
- **Manual**: Note if reply comes; do not use read receipt; log responses only

### Set Up Response Folder

In email client, create folder: "Democratic Renewal — Batch 1 Responses"
Set filter: any email from the five Batch 1 domains (justsecurity.org, brennancenter.org, hks.harvard.edu, protectdemocracy.org, perkinscoie.com, democracydocket.com) goes to this folder.

**Block 5 complete when**: Contact log exists with 5 rows pre-populated, email folder created.

**Total Block 5 time**: 20–30 minutes

---

## Block 6: Send Sequence (15–20 minutes)

**Who**: User
**Dependency**: Blocks 2, 3, 4, 5 all complete; all five emails in email client ready to send

Send in the following order, spaced approximately 30–45 minutes apart within a 4-hour window. Do not send all five at once.

**Send order and rationale**:

| Order | Contact | Rationale | Target Send Time |
|-------|---------|-----------|-----------------|
| 1st | Ryan Goodman | Fastest credibility return (Just Security publishes within days); sets institutional signal for others | T+0:00 |
| 2nd | Wendy Weiser | Brennan Center response informs Batch 2 framing; active on April 2026 SAVE Act developments | T+0:30 |
| 3rd | Erica Chenoweth | Academic credibility; Harvard funding freeze makes timing personally relevant | T+1:00 |
| 4th | Ian Bassin | Litigation and implementation; Protect Democracy active co-plaintiff in framework cases | T+1:30 |
| 5th | Marc Elias | Media platform; Democracy Docket tracks domain-01 core cases actively | T+2:00 |

**For each send**:
1. Open email in client
2. Final read — check subject line, recipient address, no `{{placeholder}}` fields remain
3. Send
4. Log send time and date in contact spreadsheet
5. Note any immediate delivery failure notifications

**Decision gate**: If any email bounces, consult `PHASE_1_CONTACT_VERIFICATION.json` for alternate address. Try alternate immediately.

**Block 6 complete when**: All five emails sent, send times logged in contact spreadsheet.

**Total Block 6 time**: 15–20 minutes (plus the 2-hour stagger window)

---

## Block 7: Post-Send Actions (same day or T+1)

**Who**: User
**Dependency**: Block 6 complete

### Social Media Queue

These can run in parallel with Block 6 or the following day. Do not post publicly before Batch 1 sends begin.

- [ ] **Substack**: Open `distribution-substack-drafts.md` — Post 1 is the executive summary adaptation. Review, fill any remaining name/date placeholders, schedule for T+3 from first email send.
- [ ] **Reddit**: Open `distribution-reddit-templates.md` — review the four subreddit-tailored posts. Stage for T+2. Do not post identical content to all subreddits — each post is already customized for its community.
- [ ] **X/Bluesky**: Draft 5-tweet opening thread using executive summary opening paragraph as hook. Stage for T+1.
- [ ] Confirm all social accounts are accessible and able to post before scheduling.

### Week 1 Monitoring Setup

- [ ] Set a calendar reminder for T+7 to assess Batch 1 response rate (target: 2 of 5 respond)
- [ ] Set a calendar reminder for T+14 to assess cumulative rate and prepare Batch 2

---

## Path-Specific Additions (select only the relevant block)

### Path A Only

No modifications to Blocks 1–7 above. All 35 domains are distributed simultaneously.
- Batch 2 (5–7 contacts) preparation begins on T+Day 1
- See `execution/path-a-materials.md` for Batch 2 messaging architecture

### Path A+37 Only

Blocks 1–7 above, plus:
- [ ] Block 1, Document 7 (Domain 37 Gist) was created above — URL is recorded
- [ ] A+37 Phase 2 begins approximately Week 2–3 (est. May 12, 2026)
- [ ] Phase 2 target list: Democracy Docket, Campaign Legal Center, ACLU Voting Rights Project, Protect Democracy (election unit), Protect The Vote 2026, state AGs in AZ/MI/NV/PA/WI, NASS
- [ ] Phase 2 outreach template (Template Category 12 — Election Protection Organizations) is documented in `DOMAIN_37_SEQUENCING_PLAN.md`; a full draft requires 1 agent session
- [ ] Phase 2 framing: "the election-specific component of the Democratic Renewal Research I distributed to your colleagues at [Brennan Center / CLC] last week"
- See `execution/path-a-domain37-materials.md` for dual-track messaging

### Path B Only

Blocks 1–7 above, plus:
- [ ] Before sending, add an explicit feedback invitation line to each Batch 1 email: "The framework is structured as a working document — practitioner and scholarly feedback shapes the Phase 2 expansion priorities. I would welcome your read on what is most useful and what is missing."
- [ ] Set up a feedback collection mechanism before Batch 1 send: Airtable (free tier), a Google Form, or a dedicated email folder
- [ ] Plan a 4-week feedback window before Batch 2–4 send
- See `execution/path-b-materials.md` for staged distribution architecture

---

## Time Summary

| Block | Task | Time Estimate | Who | Can Parallelize With |
|-------|------|---------------|-----|---------------------|
| 0 | FISA correction | 5 min | User or agent | Nothing — do first |
| 1 | Gist creation | 30–45 min | User | — |
| 2 | URL fill-in | 20–30 min | User | Block 3 (different browser tab) |
| 3 | Contact email verification | 30–45 min | User | Block 2 |
| 4 | Email personalization | 60–90 min | User | — |
| 5 | Tracking setup | 20–30 min | User | Block 3 or after Block 4 |
| 6 | Send sequence | 15–20 min + 2h stagger | User | Block 7 can run during stagger |
| 7 | Post-send social staging | 30–45 min | User | During stagger in Block 6 |

**Total elapsed time from decision to all Batch 1 emails sent**: 3.0–4.5 hours
**Minimum if parallelized efficiently**: approximately 3 hours

---

## Decision Gate Summary

| Gate | Condition | Action if Not Met |
|------|-----------|------------------|
| Before Block 1 | Block 0 (FISA correction) complete | Complete correction before creating Gists |
| Before Block 4 | All 6 Gist URLs recorded, template URLs filled | Complete Blocks 1–2 first |
| Before Block 4 | All 5 contact emails verified | Complete Block 3 first |
| Before Block 6 | All 5 emails drafted, addressed, and reviewed | Complete Block 4 first |
| Before Block 6 | Contact log created | Complete Block 5 first |
| Block 6 bounce | Any email bounces | Use alternate address from PHASE_1_CONTACT_VERIFICATION.json immediately |
| T+7 assessment | Fewer than 2 of 5 Batch 1 respond | Review personalization quality; check email delivery logs; consider A/B subject line test for Batch 2 |

---

*Checklist created: April 30, 2026 (Session 662). Cross-references: `PHASE_1_EXECUTION_READINESS.md` (approved verdict), `BATCH_1_CONTACT_VERIFICATION.md` (contact verification protocol), `PHASE_1_EMAIL_TEMPLATES.md` (email drafts), `PHASE_1_CONTACT_VERIFICATION.json` (contact data), `distribution-timeline.md` (week-by-week sequencing after Batch 1).*
