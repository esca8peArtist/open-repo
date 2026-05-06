---
title: "Distribution Launch — 4-Hour Execution Checklist"
created: 2026-05-06
status: production-ready
purpose: "Single-document, step-by-step 4-hour execution checklist from path decision to Batch 1 sent + Substack queued + monitoring live. Keyed to Path A, Path A+37 (recommended), and Path B divergence points."
path_decision_gate: "Fill in □ Path [ ] A [ ] A+37 [ ] B at the top before starting"
execution_time: "4 hours from path decision to all Batch 1 emails sent + Substack post queued"
---

# Distribution Launch — 4-Hour Execution Checklist

**Selected path**: Path [ ] A   [ ] A+37 (recommended)   [ ] B

**Decision time**: _______________  (record when you commit to a path)

**Target Batch 1 send completion**: _______________ (Decision time + 2:30)

**Target Substack post queued**: _______________ (Decision time + 3:30)

---

## Pre-Checklist Confirmation (5 minutes)

Before starting the clock, verify these four items are true. If any is false, resolve it first.

- [ ] GitHub account esca8peArtist is logged in and accessible at gist.github.com
- [ ] All 6 canonical Gists are live (spot-check: visit https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 — it should load)
- [ ] `scripts/fill_templates.py` exists (path: `projects/resistance-research/../../../scripts/fill_templates.py` — created from `field-fill-automation-spec.md` if not yet present)
- [ ] Email client (Gmail, Outlook, or other) is open and ready to compose

If fill_templates.py does not exist yet: copy the script skeleton from
`field-fill-automation-spec.md` Section 3 into `scripts/fill_templates.py` now (3 minutes).

---

## Hour 0–1: Gist Setup + Field Configuration

### Block 1 (T+0:00 — 0:10): Script Configuration

**What**: Edit `fill_templates.py` with your values and run a dry-run preview.

- [ ] Open `scripts/fill_templates.py`
- [ ] Set `DISTRIBUTION_PATH = "[your path decision]"`  — "A", "A+37", or "B"
- [ ] Set `FIELD_VALUES["{{YOUR_NAME}}"]` — your preferred name for outreach sign-offs
- [ ] Set `FIELD_VALUES["{{YOUR_CONTACT_INFO}}"]` — your email address
- [ ] Set `FIELD_VALUES["[your Substack handle]"]` — your Substack username
- [ ] Leave `{{DOMAIN_37_URL}}` empty for now (Path A+37: fill after Block 2)
- [ ] Set `DRY_RUN = True`
- [ ] Run: `uv run python scripts/fill_templates.py`

**Expected output**: "DRY RUN — no files will be written." followed by list of files
processed and any warnings. Warnings about Domain 37 URL on Path A+37 are expected at
this stage — resolve in Block 2.

**Success criteria**: No `{{YOUR_NAME}}` or `{{YOUR_CONTACT_INFO}}` warnings in output.

---

### Block 2 (T+0:10 — 0:20): Domain 37 Gist Creation [PATH A+37 ONLY]

**Path A or B**: Skip this block. Proceed to Block 3.

**Path A+37**: Create the standalone Domain 37 Gist now.

- [ ] Navigate to https://gist.github.com/new (confirm logged in as esca8peArtist)
- [ ] Set filename: `domain-37-federal-executive-interference-2026-midterms.md`
- [ ] Set description: `Domain 37 — Federal Executive Interference in the 2026 Midterms | Democratic Renewal Research Framework`
- [ ] Paste: the Zone A header from `distribution-gist-template.md` Section A (pre-filled Domain 37 version from Section C)
- [ ] Paste below: the Advocacy Windows table from `distribution-gist-template.md` Section F
- [ ] Paste below: the full content of `domains/domain-37-federal-executive-interference-2026-midterms.md`
- [ ] Paste below: the Zone D footer from `distribution-gist-template.md` Section B
- [ ] Set visibility to **Public**
- [ ] Click "Create public gist"
- [ ] Copy the Gist URL from the browser address bar

**Record the URL**:
- Domain 37 Gist URL: `______________________________________________________`
- Record it in `DISTRIBUTION_GIST_URLS.md` (Domain 37 row)
- Open `fill_templates.py` and set `FIELD_VALUES["{{DOMAIN_37_URL}}"]` to this URL

**Expected output**: A live public Gist with the Domain 37 analysis, advocacy windows table,
and standard footer. Verify it loads at the URL you copied.

**Success criteria**: Gist URL resolves, advocacy windows table renders correctly,
standard footer cross-links are visible.

---

### Block 3 (T+0:20 — 0:30): Run Fill Script (Write Mode)

**What**: Apply all field replacements to the four template files and write output.

- [ ] Confirm `FIELD_VALUES` dict is complete: all URL fields set, identity fields set, Substack handle set
- [ ] If Path A+37: confirm `{{DOMAIN_37_URL}}` is set to the Gist URL from Block 2
- [ ] Set `DRY_RUN = False`
- [ ] Run: `uv run python scripts/fill_templates.py`

**Expected output**: "WRITING FILES to scripts/filled_output/" followed by four filenames
each marked [WRITTEN]. Final line: "No warnings. All fields filled."

**Success criteria**: Zero warnings. Output directory `scripts/filled_output/` contains
four files.

**If warnings appear**: Do not proceed. Resolve the warning:
- `UNFILLED in PHASE_1_EMAIL_TEMPLATES.md: {{DOMAIN_37_URL}}` → create Domain 37 Gist first (Block 2)
- `WARNING: YOUR_NAME not set` → edit FIELD_VALUES and re-run
- Any other `{{...}}` remaining → edit FIELD_VALUES for that field and re-run

---

### Block 4 (T+0:30 — 0:45): Output Verification

**What**: Manually verify the filled output before copying to email client.

- [ ] Open `scripts/filled_output/PHASE_1_EMAIL_TEMPLATES.md`
- [ ] Verify Email 1 (Goodman) has no remaining `{{...}}` strings
- [ ] Verify the path-specific block is correctly resolved:
  - Path A: Only the `[PATH A]` paragraph is present; `[PATH A+37]` and `[PATH B]` paragraphs are gone
  - Path A+37: Only the `[PATH A+37]` paragraph is present
  - Path B: Only the `[PATH B]` paragraph is present
- [ ] Verify `{{PROPOSAL_URL}}` replaced with correct Gist URL in at least one email
- [ ] Open `scripts/filled_output/distribution-substack-drafts.md`
- [ ] Spot-check that Post 1 has the correct Proposal URL and your Substack handle
- [ ] Open `scripts/filled_output/distribution-reddit-templates.md`
- [ ] Spot-check that `[PROPOSAL_LINK]` is replaced with the correct Gist URL

**Success criteria**: No `{{...}}` placeholders visible in any spot-checked section.
Identity fields show your actual name and contact information.

---

## Hour 1–2: Contact Verification + Manual Content Placeholders

### Block 5 (T+1:00 — 1:25): Batch 1 Contact Verification

**What**: Quick-verify all five Batch 1 contacts are still in their listed roles.
Verification was last completed Session 658 (April 30). Re-verify now.

Do each in under 3 minutes:

- [ ] **Ryan Goodman**: Visit https://www.justsecurity.org/about/ — confirm "Co-Editor-in-Chief" title
  - Also note: what did Just Security publish in the last 7 days? (for content placeholder)
  - Confirmed current: [ ]  Email: ryan@justsecurity.org  New article title: _________________

- [ ] **Wendy Weiser**: Visit https://www.brennancenter.org/experts/wendy-weiser — confirm VP title
  - Also note: most recent Weiser publication
  - Confirmed current: [ ]  Email: wweiser@brennancenter.org  Recent pub: _________________

- [ ] **Erica Chenoweth**: Visit https://www.hks.harvard.edu/faculty/erica-chenoweth — confirm professor role
  - Also note: most recent Nonviolent Action Lab publication or media appearance
  - Confirmed current: [ ]  Email: echenoweth@harvard.edu  Recent work: _________________

- [ ] **Ian Bassin**: Visit https://protectdemocracy.org/about/team/ — confirm Executive Director
  - Also note: most recent Protect Democracy litigation or public statement
  - Confirmed current: [ ]  Email: ian@protectdemocracy.org  Recent filing: _________________

- [ ] **Marc Elias**: Visit https://democracydocket.com/about/ — confirm Founder role
  - Also note: most recently filed or decided Democracy Docket case in a swing state
  - Confirmed current: [ ]  Email: marc@democracydocket.com  Recent case: _________________

**Success criteria**: All five contacts confirmed current in their roles. All emails verified.

---

### Block 6 (T+1:25 — 1:50): Manual Content Placeholder Fill

**What**: Fill the five per-contact content placeholders that require current research.
These are filled directly in your email client draft, not in the script output.

For each email, open the filled template from `scripts/filled_output/PHASE_1_EMAIL_TEMPLATES.md`
and copy it to a draft in your email client. Then fill the remaining manual placeholders:

- [ ] **Email 1 draft (Goodman)**: Replace `{{RECENT_JUST_SECURITY_ARTICLE}}` with the article title you found in Block 5
  - Draft subject line selected: Option [ ] A  [ ] B  [ ] C

- [ ] **Email 2 draft (Weiser)**: Replace `{{RECENT_WEISER_PUBLICATION}}` with the publication title from Block 5
  - Draft subject line selected

- [ ] **Email 3 draft (Chenoweth)**: Replace `{{RECENT_CHENOWETH_WORK}}` with the Lab publication from Block 5
  - Draft subject line selected

- [ ] **Email 4 draft (Bassin)**: Replace `{{BASSIN_RECENT_FILING}}` with the recent Protect Democracy filing from Block 5
  - Draft subject line selected

- [ ] **Email 5 draft (Elias)**: Replace `{{ELIAS_RECENT_CASE}}` with the recent Democracy Docket case from Block 5
  - Draft subject line selected

- [ ] Final read-through of all five drafts — no remaining `{{...}}` strings, no broken links, tone is correct

**Success criteria**: Five drafts in email client, each with a subject line selected, all
placeholders filled, ready to send.

---

## Hour 2–3: Substack/Reddit Template Prep + Social Post Scheduling

### Block 7 (T+2:00 — 2:30): Substack Post 1 Preparation

**What**: Prepare the first Substack post for scheduling. Do not publish yet — scheduling
for publication at T+7 days (or earlier if desired per DISTRIBUTION_READINESS_FINAL.md).

- [ ] Open `scripts/filled_output/distribution-substack-drafts.md`
- [ ] Copy Post 1 body text (the launch overview / executive summary post)
- [ ] Open your Substack dashboard at https://[your-handle].substack.com/publish
- [ ] Create a new post — paste the Post 1 body
- [ ] Set the title (from the draft — do not spend more than 5 minutes on alternatives)
- [ ] Set post type: "Free" (maximum reach for launch)
- [ ] Set publish schedule: T+7 days from today, Tuesday or Wednesday, 9–11 AM ET
  - Target publish date: _______________ Target time: _______________
- [ ] Save as draft (do not publish yet)
- [ ] Verify all links in the post resolve correctly (click each one in the preview)

**Success criteria**: Post 1 is saved as a scheduled draft in Substack. All links verified working.

---

### Block 8 (T+2:30 — 3:00): Reddit Post Preparation

**What**: Prepare Reddit posts for three priority subreddits. Do not post yet — posts go
live at T+7 days, staggered across 2-3 days for saturation prevention.

Priority subreddits for initial wave: r/PoliticalScience, r/law, r/progressive

- [ ] Open `scripts/filled_output/distribution-reddit-templates.md`
- [ ] Copy the r/PoliticalScience post — save as a text file in `scripts/filled_output/reddit-post-political-science.md`
  - Title: _______________
  - All links verified: [ ]
  - Schedule date: T+7 (_______________) — post between 10 AM and 2 PM ET on a weekday

- [ ] Copy the r/law post — save as `scripts/filled_output/reddit-post-law.md`
  - Title: _______________
  - All links verified: [ ]
  - Schedule date: T+8 (_______________) — stagger by 1 day from r/PoliticalScience

- [ ] Copy the r/progressive post — save as `scripts/filled_output/reddit-post-progressive.md`
  - Title: _______________
  - All links verified: [ ]
  - Schedule date: T+9 (_______________) — stagger by 1 day from r/law

- [ ] Note: Reddit does not have native post scheduling. Set a calendar reminder for each date.
  Alternatively, use a social media scheduling tool (Buffer, Hootsuite) that supports Reddit.

**Success criteria**: Three Reddit post drafts saved to `scripts/filled_output/`. Three
calendar reminders set for T+7, T+8, T+9. Each post has correct Gist links and no placeholder text.

---

### Block 9 (T+3:00 — 3:30): PATH A+37 ONLY — Phase 1b Email Preparation

**Path A or B**: Skip this block. Proceed to Block 10.

**Path A+37**: Prepare the seven Domain 37 election-protection organization emails.

These are the Phase B Tier 1 contacts from `STAGE_PATH_A_DOMAIN37/DEPLOY_CHECKLIST_PATH_A_DOMAIN37.md`.
They are NOT sent now — they are sent at Week 9 (Phase B launch). Prepare the template
drafts now while the decision context is fresh.

- [ ] Open `DOMAIN_37_SEQUENCING_PLAN.md` — locate Template D37-1
- [ ] Fill Template D37-1 with the Domain 37 Gist URL (from Block 2)
- [ ] Fill Template D37-1 with identity fields
- [ ] Save 7 per-organization draft versions to `scripts/filled_output/domain-37-emails/`
  with filenames: `d37-brennan-center.md`, `d37-democracy-docket.md`, `d37-protect-democracy.md`,
  `d37-lawyers-committee.md`, `d37-aclu-vrp.md`, `d37-states-united.md`, `d37-common-cause.md`
- [ ] Verify each draft has correct advocacy window framing for that organization
  (see Phase B Tier 1 table in `STAGE_PATH_A_DOMAIN37/DEPLOY_CHECKLIST_PATH_A_DOMAIN37.md`)

**Success criteria**: Seven Phase 1b email drafts saved. Each contains the correct Domain 37
Gist URL and the advocacy window most relevant to the recipient organization.

---

## Hour 3–4: Final QA + Monitoring Setup

### Block 10 (T+3:30 — 3:45): Final QA

**What**: Systematic pre-send quality check.

**Email QA**:
- [ ] Open each of the five email drafts in your client
- [ ] Each has a subject line set (no placeholder subject lines)
- [ ] Each has the recipient email address filled correctly
- [ ] Each body has zero `{{...}}` placeholder strings
- [ ] Each body has at least 2 working Gist URLs
- [ ] Each sign-off shows your name and contact info
- [ ] Send order confirmed: Email 1 → Email 2 → ... → Email 5 with 30-45 minute spacing

**Substack QA**:
- [ ] Post 1 is scheduled (not published immediately)
- [ ] Substack publication name / header is set
- [ ] No `[your Substack handle]` placeholder text remains

**Gist QA**:
- [ ] All 6 canonical Gists load correctly (spot-check 2 of them)
- [ ] Path A+37 only: Domain 37 Gist loads correctly and shows advocacy windows table

**Script output QA**:
- [ ] `scripts/filled_output/` contains 4 filled template files + (Path A+37) domain-37-emails/ directory

**Success criteria**: All checklist items above are checked. No placeholders remain in
any send-ready file.

---

### Block 11 (T+3:45 — 4:00): Monitoring Setup

**What**: Establish minimal monitoring so you will know when Batch 1 responses arrive.

**Email monitoring**:
- [ ] Create a label/folder in your email client: "Phase 1 Responses"
- [ ] Create a filter: emails from ryan@justsecurity.org, wweiser@brennancenter.org,
  echenoweth@harvard.edu, ian@protectdemocracy.org, marc@democracydocket.com
  → auto-label "Phase 1 Responses" + star/flag
- [ ] Enable desktop notifications for incoming email (if not already enabled)

**Gist view tracking** (optional but useful):
- [ ] Note current view counts for all 6 Gists before sending (GitHub shows view counts
  in the Gist analytics — accessible at gist.github.com/[username]/[hash]/analytics if
  you are logged in as the Gist author)
  - Proposal views at send time: _______
  - Executive Summary views at send time: _______

**Contact log**:
- [ ] Open `BATCH_1_CONTACT_LOG.md` — add a row for each email with send timestamp
  - Format: | Contact | Send Time | Subject Line Used | Notes |

**Phase 2 calendar reminder**:
- [ ] Set a calendar reminder for T+7 days: "Publish Substack Post 1 + launch Reddit wave"
- [ ] Set a calendar reminder for T+14 days: "Send Batch 2 emails (8 contacts)"
- [ ] Path A+37 only: Set a calendar reminder for T+56 days (Week 8): "Phase B decision point — assess Domain 37 launch conditions"

**Success criteria**: Email filter created. Contact log updated with 5 send entries.
Three calendar reminders set.

---

## Batch 1 Send Sequence

Execute after Block 10 QA is complete.

| # | Contact | Email | Send Time | Gap |
|---|---------|-------|-----------|-----|
| 1 | Ryan Goodman | ryan@justsecurity.org | T+4:00 | — |
| 2 | Wendy Weiser | wweiser@brennancenter.org | T+4:30 | +30 min |
| 3 | Erica Chenoweth | echenoweth@harvard.edu | T+5:00 | +30 min |
| 4 | Ian Bassin | ian@protectdemocracy.org | T+5:30 | +30 min |
| 5 | Marc Elias | marc@democracydocket.com | T+6:00 | +30 min |

The 30-minute gap between sends has two purposes: it prevents any appearance of mass
mailing (each email is genuinely personalized, the gap signals it), and it allows you to
monitor for any immediate bounce or delivery failure before sending the next.

---

## Post-Launch Monitoring (T+4 hours through T+48 hours)

**T+4 to T+24 hours**: Check for email opens and bounces every 4 hours if convenient.
First responses from Goodman and Weiser (highest responsiveness based on verification
research) expected within 24-48 hours. Elias and Bassin may take 3-5 days.

**If a bounce occurs**: Do not resend immediately. Verify the email address by visiting
the institutional website. If a different email format is listed, update the contact log
and resend to the corrected address within 24 hours.

**If a response arrives**: Log it in `BATCH_1_CONTACT_LOG.md` immediately. Note:
response type (acknowledgment / substantive / negative), domain engaged, any request
for follow-up. Do not draft a reply immediately — take 4-8 hours to consider the
appropriate response. Exceptions: if the contact asks a direct factual question
(e.g., about a specific case citation), respond within 24 hours.

**T+24 hours**: Log all send timestamps and delivery statuses in `BATCH_1_CONTACT_LOG.md`.

**T+7 days**: 
- Publish Substack Post 1 (calendar reminder set in Block 11)
- Post to r/PoliticalScience
- Send Batch 2 emails (8 contacts — see `execution/phase-1-personalized-batch-2.md`)

---

## Path-Specific Block Divergence Summary

| Block | Path A | Path A+37 | Path B |
|-------|--------|-----------|--------|
| Block 1 | Set path = "A" | Set path = "A+37" | Set path = "B" |
| Block 2 | SKIP | Create Domain 37 Gist | SKIP |
| Block 3-10 | Identical | Identical except Domain 37 URL | Identical with Path B framing |
| Block 9 | SKIP | Prepare 7 Phase 1b email drafts | SKIP |
| Week 9 | Send Batch 3 + public distribution | Launch Phase B (Domain 37 to election orgs) | Continue feedback collection |

---

## Quick-Reference Time Budget

| Block | Description | Time |
|-------|-------------|------|
| Pre-check | Verify accounts + files | 5 min |
| Block 1 | Script config + dry run | 10 min |
| Block 2 | Domain 37 Gist (A+37 only) | 10 min |
| Block 3 | Fill script write mode | 5 min |
| Block 4 | Output verification | 15 min |
| Block 5 | Contact verification | 25 min |
| Block 6 | Content placeholder fill | 25 min |
| Block 7 | Substack Post 1 prep | 30 min |
| Block 8 | Reddit posts prep | 30 min |
| Block 9 | Domain 37 emails (A+37 only) | 30 min |
| Block 10 | Final QA | 15 min |
| Block 11 | Monitoring setup | 15 min |
| **Send** | Batch 1 emails (staggered) | **120 min** |
| **Total** | | **~4 hours** |

---

*Created May 6, 2026. Companion documents: `field-fill-automation-spec.md` (placeholder*
*inventory and script), `gist-template-structure.md` (Gist layout), `github-api-integration-guide.md`*
*(API operations), `STAGE_PATH_A_DOMAIN37/DEPLOY_CHECKLIST_PATH_A_DOMAIN37.md` (Phase B detail).*
