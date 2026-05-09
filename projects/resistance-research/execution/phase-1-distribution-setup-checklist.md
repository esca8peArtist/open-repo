---
title: "Phase 1 Distribution Setup Checklist — 7-Step Pre-Distribution Verification"
created: 2026-05-09
session: Item-41
status: ready-to-execute
purpose: "Path-agnostic pre-distribution verification. Works for Path A, Path A+37, and Path B. Complete all 7 steps before executing any path."
estimated_total_time: "1.5–2 hours"
companion_files:
  - execution/phase-1-path-decision-template.md
  - execution/phase-1-gist-creation-playbook.md
  - execution/phase-1-contact-verification-checklist.md
---

# Phase 1 Distribution Setup Checklist

**Purpose**: Verify that all distribution infrastructure is in place before selecting and executing a distribution path. This checklist is path-agnostic — complete it regardless of whether you choose Path A, Path A+37, or Path B.

**Total estimated time**: 1.5–2 hours

**When to run**: Before making your path decision (May 13 deadline), or immediately after deciding if you choose to run setup in parallel with the decision.

**Completion standard**: All 7 steps must reach status "Complete" or "Acceptable" before sending any Batch 1 emails.

---

## Overview: The 7 Steps

| Step | Task | Est. Time | Status |
|------|------|-----------|--------|
| 1 | Domain inventory verification | 20 min | [ ] |
| 2 | Proposal file verification | 5 min | [ ] |
| 3 | Gist URL and placeholder verification | 10 min | [ ] |
| 4 | Contact field verification | 15 min | [ ] |
| 5 | Cross-reference testing | 10 min | [ ] |
| 6 | Template formatting verification | 10 min | [ ] |
| 7 | Tracking spreadsheet creation | 30 min | [ ] |

**Total**: 1 hour 40 minutes, can be done across two sittings.

---

## Step 1: Domain Inventory Verification

**Purpose**: Confirm all 35 Phase 1 domains exist in `projects/resistance-research/domains/` and are production-ready.

**Estimated time**: 20 minutes

**What "production-ready" means**: File exists, is greater than 30 KB (substantive content, not a stub), and was last modified in April or May 2026.

### Verified Domain Inventory (as of May 9, 2026)

The following table lists all 40 domain files in the `domains/` directory that carry analytical content. The Phase 1 distribution framework uses 35 core domains. The remaining files are either sub-domain expansions (37a, 37b, 31x), structural scaffolding (implementation-roadmap, network-spec), or baseline metrics documents.

| # | File | Size (KB) | Last Modified | Status |
|---|------|-----------|---------------|--------|
| 1 | domain-01-voting-rights-elections.md | 77 KB | 2026-05-06 | Production-ready |
| 2 | domain-06-judicial-independence.md | 72 KB | 2026-05-07 | Production-ready |
| 3 | domain-19f-war-powers-reform.md | 229 KB | 2026-05-07 | Production-ready |
| 4 | domain-20-corruption-and-institutional-accountability.md | 43 KB | 2026-05-07 | Production-ready |
| 5 | domain-23-trade-policy-tariff-unilateralism.md | 80 KB | 2026-04-27 | Production-ready |
| 6 | domain-25-fisa-702-april-2026-outcome.md | 80 KB | 2026-05-06 | Production-ready |
| 7 | domain-26-government-accountability-and-institutional-resilience.md | 44 KB | 2026-05-07 | Production-ready |
| 8 | domain-27-higher-education-and-academic-freedom.md | 73 KB | 2026-04-27 | Production-ready |
| 9 | domain-28-war-powers-venezuela.md | 62 KB | 2026-04-28 | Production-ready |
| 10 | domain-28-war-powers-venezuela-military-unilateralism.md | 62 KB | 2026-05-07 | Production-ready |
| 11 | domain-29-prosecutorial-weaponization-and-doj-capture.md | 115 KB | 2026-04-30 | Production-ready |
| 12 | domain-31-healthcare-access-obbba-medicaid-crisis.md | 34 KB | 2026-04-27 | Production-ready |
| 13 | domain-31x-healthcare-tariff-collision.md | 37 KB | 2026-04-28 | Sub-domain expansion |
| 14 | domain-33-state-legislative-autocratization.md | 91 KB | 2026-05-07 | Production-ready |
| 15 | domain-34-congressional-power-of-the-purse-fiscal-authority-reassertion.md | 50 KB | 2026-04-27 | Production-ready |
| 16 | domain-35-supreme-court-2026-term-preview-post-loper-landscape.md | 88 KB | 2026-05-07 | Production-ready |
| 17 | domain-36-ai-governance-algorithmic-accountability-democratic-authority.md | 46 KB | 2026-04-27 | Production-ready |
| 18 | domain-37-federal-executive-interference-2026-midterms.md | 89 KB | 2026-05-07 | Production-ready |
| 19 | domain-37-foreign-transnational-interference-democratic-institutions.md | 59 KB | 2026-04-29 | Production-ready |
| 20 | domain-37a-post-election-section3-litigation-recovery.md | 16 KB | 2026-04-27 | Scope doc (not full domain) |
| 21 | domain-37b-state-election-security.md | 70 KB | 2026-05-06 | Production-ready |
| 22 | domain-38-financial-sector-independence.md | 73 KB | 2026-04-28 | Production-ready |
| 23 | domain-38a-fisa-intel-oversight-reform.md | 81 KB | 2026-05-07 | Production-ready |
| 24 | domain-39-immigration-enforcement-detention-infrastructure.md | 50 KB | 2026-05-09 | Production-ready |
| 25 | domain-41b-disability-rights-benefit-infrastructure-civic-participation.md | 67 KB | 2026-05-07 | Production-ready |
| 26 | domain-42-drug-policy-democratic-legitimacy-regulatory-capture.md | 55 KB | 2026-05-07 | Production-ready |
| 27 | domain-43-epistemic-infrastructure-disinformation-crisis.md | 54 KB | 2026-05-07 | Production-ready |
| 28 | domain-B-healthcare-access-implementation-obbba-medicaid-crisis.md | 53 KB | 2026-05-06 | Production-ready |
| 29 | domain-civil-service-resilience.md | 66 KB | 2026-04-28 | Production-ready |
| 30 | domain-E-election-administration-seizure-2026-midterms.md | 66 KB | 2026-05-06 | Production-ready |
| 31 | domain-F-civil-society-suppression-democratic-infrastructure-attack.md | 64 KB | 2026-05-06 | Production-ready |
| 32 | domain-foreign-interference-in-democratic-institutions.md | 89 KB | 2026-04-29 | Production-ready |
| 33 | domain-implementation-roadmap.md | 79 KB | 2026-04-29 | Framework structure |
| 34 | domain-information-access-recovery.md | 77 KB | 2026-04-29 | Production-ready |
| 35 | domain-judicial-independence-recovery.md | 79 KB | 2026-04-28 | Production-ready |
| 36 | domain-legislative-branch-capacity.md | 72 KB | 2026-04-28 | Production-ready |
| 37 | domain-media-freedom-recovery.md | 77 KB | 2026-04-28 | Production-ready |

**Note on domain count**: The framework has grown to 43 domains (per domain-42 Gist header and DISTRIBUTION_GIST_URLS.md), with 35 Phase 1 core domains plus Phase 2/3 expansions. The 40 substantive files above represent the full distributable inventory. The files named domain-37-baseline-metrics.md (29 KB) and domain-37b-state-election-security-coordination.md (31 KB) are supporting reference documents (baseline metrics and scope document respectively), not primary distribution content.

### User Verification Task

- [ ] Open a terminal and run: `ls projects/resistance-research/domains/domain-*.md | wc -l` — should return 40
- [ ] Spot-check 5 files at random: open each, confirm it has a proper title, sections, and sources
- [ ] Flag any file under 30 KB (except the 37a scope doc at 16 KB, which is intentionally a scoping document, not a full domain)
- [ ] If any file is missing or flagged: note in the Status column above and check PROJECTS.md for completion status

**Completion check**: All files listed above are present and no primary distribution domain is missing.

- [ ] Step 1 complete

---

## Step 2: Proposal File Verification

**Purpose**: Confirm the canonical consolidated proposal document exists and is current.

**Estimated time**: 5 minutes

**Primary file**: `projects/resistance-research/democratic-renewal-proposal.md`

This is the 813 KB consolidated 35-domain proposal documented in DISTRIBUTION_READINESS_FINAL.md (Section 1.2). It is the primary send artifact for Path A and the anchor document for all three paths.

### Verification Tasks

- [ ] Confirm file exists: `ls projects/resistance-research/democratic-renewal-proposal.md`
- [ ] Open file and verify it shows a last-updated date in the header (should be April 27, 2026 or later)
- [ ] Confirm the table of contents references 35 or more domains (not the earlier 22-domain or 28-domain versions)
- [ ] Check file size is approximately 800–850 KB — this is the correct range for the full proposal
- [ ] Confirm the companion executive summary exists: `projects/resistance-research/democratic-renewal-executive-summary.md`

**Note on domain count in the proposal**: Several distribution templates still reference "28-domain" in some places. The correct count is 35 (and expanding into Phase 2/3). If you see "28-domain" anywhere during this checklist, flag it — it needs to be updated before you send.

**Completion check**: Both the full proposal and executive summary exist and show correct domain counts.

- [ ] Step 2 complete

---

## Step 3: Gist URL and Placeholder Verification

**Purpose**: Confirm the 6 canonical Gist URLs are live, and that all template files have correct URL placeholders that can be replaced at execution time.

**Estimated time**: 10 minutes

### Live Gist URLs (from DISTRIBUTION_GIST_URLS.md)

Verify each URL loads in your browser:

| Document | Gist URL | Status |
|----------|----------|--------|
| Democratic Renewal Proposal (35 domains) | https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 | [ ] Verified live |
| Executive Summary | https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4 | [ ] Verified live |
| Litigation Tracker 2026 | https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0 | [ ] Verified live |
| First Amendment Suppression Tracker | https://gist.github.com/esca8peArtist/10d0a86e386e6c3c11c3830295a6503c | [ ] Verified live |
| Environmental Rollbacks Tracker | https://gist.github.com/esca8peArtist/87e2bdb931b77480e56a08044c567bc4 | [ ] Verified live |
| Police Consent Decree Tracker | https://gist.github.com/esca8peArtist/1f5cb28527c98d12526c14302c725731 | [ ] Verified live |

**If any Gist is not loading**: The Gist may have been deleted or made private since Session 678 (April 30). Re-create per the procedure in `execution/phase-1-gist-creation-playbook.md`.

### Placeholder Status in Template Files

Search the following files for `[link]`, `{{GIST_URL}}`, and `[GIST URL` — these are the placeholder patterns used across distribution templates:

- `distribution-substack-drafts.md` — should contain `[link]` placeholders for each of the 6 documents
- `distribution-reddit-templates.md` — should contain `[link]` placeholders
- `distribution-institutional-outreach-templates.md` — should contain `[link]` and `[Your name]` / `[Contact information]` placeholders
- `execution/outreach-email-templates.md` — Batch 1 templates use `{{GIST_URL}}` and `{{YOUR_NAME}}`
- `execution/domain-42-email-template.md` — uses `[GIST URL — fill when created...]` for Domain 42 specifically

**These are the correct pre-execution state.** Placeholders should NOT be filled yet — you fill them at execution time per your chosen path. What you are verifying here is that the placeholders exist and are not already overwritten with stale or incorrect URLs.

- [ ] At least 3 Gist URLs load correctly in browser (spot-check — do not need to verify all 6 unless one fails)
- [ ] Template files contain unfilled `[link]` / `{{GIST_URL}}` placeholders (not already incorrectly filled)
- [ ] Domain 42 Gist does not yet exist (create per `domain-42-gist-creation-steps.md` at execution time)

**Completion check**: Live Gists confirmed, placeholder patterns intact in templates.

- [ ] Step 3 complete

---

## Step 4: Contact Field Verification

**Purpose**: Spot-verify that the primary contact lists are properly structured and that Batch 1 contacts remain current.

**Estimated time**: 15 minutes

### Batch 1 Contact Currency (5 contacts, verified April 29, 2026)

These contacts were position-verified as of April 29. Verify they are still current:

| Contact | Role | Organization | Email | Verify URL |
|---------|------|-------------|-------|-----------|
| Ryan Goodman | Co-Editor-in-Chief; Prof. | Just Security / NYU Law | ryan.goodman@nyu.edu | https://www.law.nyu.edu/faculty/profiles/GOODMANR |
| Wendy Weiser | VP, Democracy Program | Brennan Center for Justice | wweiser@brennancenter.org | https://www.brennancenter.org/about/leadership |
| Erica Chenoweth | Frank Stanton Professor | Harvard Kennedy School | echenoweth@harvard.edu | https://www.hks.harvard.edu/faculty/erica-chenoweth |
| Ian Bassin | Co-Founder and Executive Director | Protect Democracy | ian@protectdemocracy.org | https://protectdemocracy.org/about/ |
| Marc Elias | Founder | Democracy Docket | marc@democracydocket.com | https://www.democracydocket.com/about/ |

### Verification Task

- [ ] Visit 2 of the 5 verify URLs above and confirm the contact is still listed in their role (sample — do not need all 5)
- [ ] Open `DISTRIBUTION_OUTREACH_CONTACTS.md` and confirm it exists with multi-pillar structure (Universities, Think Tanks, Labor, Civil Rights sections)
- [ ] Open `execution/tier-1-contact-batches.md` and confirm it lists 25 contacts across 3 batches
- [ ] Open `execution/domain-42-contact-list.md` and confirm the Domain 42 sub-batch (10 drug policy orgs) is present and dated 2026-05-07

**Tier structure reference**:
- Tier 1: 25 high-leverage contacts (Batch 1-3 in `tier-1-contact-batches.md`)
- Tier 2: 45+ academic, media, and policy contacts (in `DISTRIBUTION_OUTREACH_CONTACTS.md` Pillars 1-4)
- Tier 3: 80+ labor, civil rights, and movement orgs (in DISTRIBUTION_GUIDE.md and supplementary lists)
- Domain 42 sub-batch: 10 drug policy orgs (in `domain-42-contact-list.md`)

**Completion check**: Batch 1 roster confirmed current, three-tier structure confirmed present.

- [ ] Step 4 complete

---

## Step 5: Cross-Reference Testing

**Purpose**: Confirm that internal Markdown links between domain files resolve correctly, and that execution template links are not broken.

**Estimated time**: 10 minutes

### Sample Cross-Reference Test

Test the following three known cross-reference chains:

**Chain 1: Domain 28 → Domain 19f**
- Open `domains/domain-28-war-powers-venezuela.md`
- Search for a reference to "Domain 19f" or "domain-19f"
- Confirm it appears as a cross-reference (it should — Domain 28 cites Domain 19f's War Powers framework)
- Verify the referenced file `domain-19f-war-powers-reform.md` exists (229 KB, confirmed in Step 1)

**Chain 2: Domain 29 → Domain 6**
- Open `domains/domain-29-prosecutorial-weaponization-and-doj-capture.md`
- Search for a reference to "Domain 6" or "judicial independence"
- Confirm cross-reference appears

**Chain 3: Domain 42 → Domain 16/22/29**
- Open `domains/domain-42-drug-policy-democratic-legitimacy-regulatory-capture.md`
- Confirm it references Domain 16 (Criminal Justice), Domain 22 (Racial Justice), and Domain 29 (Prosecutorial Weaponization) — these are the documented cross-references in domain-42-gist-creation-steps.md Zone B block

### Execution Template Link Test

- [ ] Open `execution/outreach-email-templates.md` and check that no links appear to be hardcoded URLs pointing to non-existent files (internal file paths like `../domains/domain-01.md` are fine; external URLs in placeholder form are fine)
- [ ] Open `execution/domain-42-gist-creation-steps.md` and verify the Zone D footer URLs match those in `DISTRIBUTION_GIST_URLS.md` (they should, as the Domain 42 playbook was written after the Gist URLs were finalized)

**Completion check**: Cross-references present in at least 2 of 3 chains; no broken hardcoded external links in templates.

- [ ] Step 5 complete

---

## Step 6: Template Formatting Verification

**Purpose**: Confirm that the primary distribution templates are properly formatted for Gist/email/Substack rendering.

**Estimated time**: 10 minutes

### Templates to Check

Open each file and do a quick visual scan for the issues listed:

**File 1**: `execution/outreach-email-templates.md`
- [ ] No raw `\n\n\n` triple-newline blocks (email clients collapse spacing)
- [ ] Placeholder fields follow consistent pattern: `{{FIELD_NAME}}` or `[Field name]` (not mixed formats in the same email)
- [ ] Subject line templates are present (at least 2 variants per template type)

**File 2**: `execution/domain-42-email-template.md`
- [ ] Domain 42 email templates (D42-A through D42-D) are present
- [ ] DEA docket number (DEA-1362) appears correctly
- [ ] May 28 deadline appears in at least one urgency-flagged location per template

**File 3**: `distribution-institutional-outreach-templates.md`
- [ ] File exists in root resistance-research directory
- [ ] Identity placeholders `[Your name]` and `[Contact information]` are present in sign-off sections
- [ ] No template has a hard-wrapped line that would appear as an awkward line break in email (lines greater than 80 characters in plain text templates are acceptable; hard-wrapped plain text at 40-50 characters would be a problem)

**File 4**: `distribution-substack-drafts.md`
- [ ] File exists and contains multiple draft posts
- [ ] `[link]` placeholders for Gist URLs are present and unfilled
- [ ] Posts have distinct titles (not all using the same headline template)

**Completion check**: All 4 template files open without errors, placeholder consistency confirmed, no obvious formatting problems that would break rendering.

- [ ] Step 6 complete

---

## Step 7: Tracking Spreadsheet Creation

**Purpose**: Set up the distribution tracking mechanism before executing any send. You cannot measure success without tracking from send day 1.

**Estimated time**: 30 minutes

### Option A: Google Sheets (Recommended if You Have a Google Account)

Create a new Google Sheet at sheets.google.com with the following structure:

**Sheet 1: Contact Tracking**

| Column | Header | Notes |
|--------|--------|-------|
| A | Contact Name | Full name |
| B | Organization | Current org |
| C | Tier | 1 / 2 / 3 / D42 |
| D | Email | Verified address |
| E | Path Assignment | A / A+37 / B |
| F | Batch | 1 / 2 / 3 |
| G | Send Date | Fill when sent (YYYY-MM-DD) |
| H | Open Date | Fill if email tracking enabled, or leave blank |
| I | Reply Date | Fill when reply received |
| J | Reply Type | None / Acknowledge / Substantive / Forward / Refer |
| K | Gist View Proxy | (manual note if contact mentions Gist) |
| L | Status | Queued / Sent / Bounced / Opened / Replied / Followed-up |
| M | Notes | Context, follow-up actions needed |

**Sheet 2: Gist Views**

| Column | Header | Notes |
|--------|--------|-------|
| A | Gist Title | Match names from DISTRIBUTION_GIST_URLS.md |
| B | Gist URL | Copy from DISTRIBUTION_GIST_URLS.md |
| C | Views W1 | Check manually on Day 7 |
| D | Views W2 | Check manually on Day 14 |
| E | Views W4 | Check manually on Day 30 |
| F | Stars | Number of stars on the Gist |
| G | Forks | Number of forks (signals institutional use) |

**Sheet 3: Path Decision**

Single cell at the top: `SELECTED PATH: [A / A+37 / B]` — fill when you decide.

**Pre-populate Sheet 1** with the 25 Tier 1 contacts from `execution/tier-1-contact-batches.md` (Batches 1-3). Use the contact name, organization, and email from that file. Set Tier = 1, Path Assignment = [TBD until decision], Status = Queued.

- [ ] Google Sheet created and shared (copy share URL here: ________________)
- [ ] 25 Tier 1 contacts pre-populated in Sheet 1
- [ ] Gist URLs copied into Sheet 2

### Option B: Local Spreadsheet (.xlsx or .csv)

If you prefer to keep this offline, create a file at:
`projects/resistance-research/execution/phase-1-tracking.csv`

Use the same column structure as Option A. Acceptable — just less convenient for future sharing.

### Option C: Minimal (Plain Text Log)

If neither option works, create `projects/resistance-research/execution/DISTRIBUTION_LOG.md` with this structure:

```
## Batch 1 Send Log

### Contact 1: Ryan Goodman
- Send date:
- Status:
- Reply date:
- Notes:
```

**Note**: The existing `DISTRIBUTION_EXECUTION_LOG.md` in the root resistance-research directory may already serve this function — open it and check before creating a duplicate.

- [ ] Tracking mechanism confirmed and pre-populated (any of Option A/B/C)
- [ ] Share link recorded here (if Google Sheets): ________________

**Completion check**: A tracking file or sheet exists with 25+ Tier 1 contacts pre-populated and column structure matching the metrics framework.

- [ ] Step 7 complete

---

## Final Completion Check

- [ ] Step 1: Domain inventory verified — all 35+ production-ready domains confirmed present
- [ ] Step 2: Proposal file verified — `democratic-renewal-proposal.md` current and complete
- [ ] Step 3: Gist URLs live — at least 3 of 6 verified loading; placeholders intact in templates
- [ ] Step 4: Contact fields verified — Batch 1 roster confirmed current, 3-tier structure confirmed
- [ ] Step 5: Cross-references tested — at least 2 of 3 chains confirmed, no broken template links
- [ ] Step 6: Template formatting verified — 4 template files checked, no rendering-breaking issues
- [ ] Step 7: Tracking spreadsheet created — pre-populated with 25 Tier 1 contacts

**When all 7 steps are checked**: You are cleared to select a distribution path and execute.

**Total time invested**: 1.5–2 hours
**Time to first Batch 1 email after this checklist**: 90 minutes (path execution blocks from DISTRIBUTION_READINESS_FINAL.md)

---

*Created May 9, 2026 — Item 41 Phase 1 Distribution Setup Kit*
*Companion to: `phase-1-path-decision-template.md`, `phase-1-gist-creation-playbook.md`, `phase-1-contact-verification-checklist.md`*
