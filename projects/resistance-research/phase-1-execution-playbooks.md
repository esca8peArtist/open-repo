---
title: "Phase 1 Execution Playbooks — Detailed Technical Procedures for All Distribution Paths"
created: 2026-04-30
status: reference-operational
scope: "Step-by-step execution for Path A, Path A+37, and Path B. Zero-ambiguity procedures from user path decision through first email send and beyond."
companion_docs:
  - PHASE_1_EXECUTION_READINESS.md
  - DISTRIBUTION_PATH_QUICK_REFERENCE.md
  - path-a-execution-roadmap.md
  - path-a-37-execution-roadmap.md
  - path-b-continuation-roadmap.md
  - DISTRIBUTION_OUTREACH_CONTACTS.md
  - EMAIL_PERSONALIZATION_GUIDE.md
  - DISTRIBUTION_GUIDE.md
---

# Phase 1 Execution Playbooks
## Detailed Technical Procedures — Path A / Path A+37 / Path B

**April 30, 2026**

This document resolves all procedural ambiguity for Phase 1 distribution execution. The framework is 100% production-ready as confirmed by the Session 662 readiness audit (`PHASE_1_EXECUTION_READINESS.md`). The only open question is path selection. Once the user selects a path, the orchestrator or user can open the relevant part of this document and execute without consulting any other file for task sequencing.

This document is structured in seven parts. Parts 1 (shared pre-launch) and 5-7 (post-launch monitoring, failure modes, success metrics) apply to all three paths. Parts 2, 3, and 4 are path-specific.

---

## Part 1: Shared Pre-Launch Checklist

**Estimated time: 30-45 minutes**
**Who executes: User (with orchestrator support for template tasks)**
**Precondition: None. Can be executed before path decision is final.**

This checklist is identical regardless of path. It can and should begin the moment the user is leaning toward any path, because the artifacts it produces (Gist URLs, verified email addresses, filled templates) are required by all three paths. Starting this checklist before the path decision is final does not lock in any path.

---

### 1.1 Verify the Six Canonical Documents for Gist Publication

The six documents below are the distribution infrastructure backbone. Every email template, Substack post, and Reddit template contains `[link]` placeholders that will be replaced by these Gist URLs. No distribution template can go out until these six Gists are live.

**Verify the documents exist and are current:**

```
File 1: projects/resistance-research/democratic-renewal-proposal.md
  Status: 109,543 words, 4,390 lines — CONFIRMED CURRENT (Session 519 verification)
  Last material update: April 29-30, 2026 (Domains 1, 6, 25, 27, 29, 37 updated)

File 2: projects/resistance-research/democratic-renewal-executive-summary.md
  Status: 2-page print-ready summary — CONFIRMED CURRENT
  Note: Verify the Domain count in the header says "35 domains" not "28 domains"

File 3: projects/resistance-research/litigation-tracker-2026.md
  Status: Updated April 13 (main) + April additions section — CONFIRMED CURRENT
  Note: The most recent entries are at the bottom of the document in the "April 2026 Updates" section

File 4: projects/resistance-research/first-amendment-suppression.md
  Status: Verified production-ready — CONFIRMED CURRENT

File 5: projects/resistance-research/environmental-rollbacks-tracker.md
  Status: Verified production-ready — CONFIRMED CURRENT

File 6: projects/resistance-research/police-brutality-consent-decree-tracker.md
  Status: Verified production-ready — CONFIRMED CURRENT
```

**Confirm domain count language before Gist creation.** Open `democratic-renewal-executive-summary.md` and `distribution-substack-drafts.md`. Search for "28-domain" or "28 domains." If found, replace with "35 domains" before creating Gists. This is a one-time find-and-replace. The proposal body itself already uses correct domain numbering; the summary header and Substack posts are where stale count language may appear.

**Spot-check one domain for currency.** Open `domains/domain-01-voting-rights-elections.md` and confirm the accuracy note at Section 4.2 is present (it documents FISA House passage 235-191, April 29, 2026). If that note is visible, the Session 658 update is intact and the domain is current through April 29. No further currency check is required before Gist creation.

---

### 1.2 Create the Six Public GitHub Gists

**Tool**: gist.github.com  
**Account required**: GitHub account (the existing account used to create the May Day Action Guide Gist is confirmed working — that Gist at https://gist.github.com/esca8peArtist/2c5ba783bd06405749b7c3decebaa6d4 confirms the workflow)  
**Estimated time**: 5-8 minutes per Gist, 30-45 minutes total  

**Procedure for each Gist (identical for all six):**

1. Navigate to https://gist.github.com
2. Set filename: use the exact filename from the table below (the filename drives the `.md` extension, which enables GitHub's markdown renderer)
3. Paste the full document content
4. Set visibility: **Public** (not secret — distribution contacts must be able to open the link without authentication)
5. Click "Create public gist"
6. Copy the resulting URL from the browser address bar (format: `https://gist.github.com/[username]/[hash]`)
7. Record the URL immediately in `DISTRIBUTION_GIST_URLS.md`

**Filename convention (exact strings to use):**

| Document | Filename to Use in Gist |
|----------|------------------------|
| democratic-renewal-proposal.md | `democratic-renewal-proposal.md` |
| democratic-renewal-executive-summary.md | `democratic-renewal-executive-summary.md` |
| litigation-tracker-2026.md | `litigation-tracker-2026.md` |
| first-amendment-suppression.md | `first-amendment-suppression.md` |
| environmental-rollbacks-tracker.md | `environmental-rollbacks-tracker.md` |
| police-brutality-consent-decree-tracker.md | `police-brutality-consent-decree-tracker.md` |

**Verify markdown rendering before recording the URL.** After creating each Gist, click on the `.md` filename within the Gist page. GitHub renders `.md` files as formatted HTML when you click through. Verify that headers, bullet points, and tables render correctly. If the document displays as raw text rather than formatted markdown, the likely cause is a BOM (byte order mark) encoding issue.

**Failure mode — markdown not rendering:**  
Cause: File saved with encoding other than UTF-8 without BOM, or the `.md` extension was not set.  
Recovery: (a) Delete the Gist; (b) If the paste included special characters or was copied from a PDF viewer, re-paste from the raw markdown source in the repository; (c) Recreate the Gist ensuring the filename ends in `.md`; (d) If the issue persists, open the file in a text editor, save explicitly as UTF-8 encoding, and re-paste.

**Failure mode — Gist creation fails (rate limiting):**  
GitHub rate-limits unauthenticated Gist creation but not authenticated creation. Ensure you are logged in to your GitHub account. If you hit a rate limit (unlikely for 6 Gists), wait 10 minutes and continue.

**Record all URLs before proceeding.** The `DISTRIBUTION_GIST_URLS.md` file has a table pre-formatted for URL entry. Do not proceed to template fill-in until all six URLs are recorded.

---

### 1.3 Verify Gist Access and Markdown Rendering

**Test protocol (2 minutes total):**

1. Open each Gist URL in a private/incognito browser window (this simulates a recipient who is not logged in to GitHub)
2. Confirm the Gist loads without authentication prompt
3. Click the `.md` filename — confirm formatted rendering (not raw text)
4. For `democratic-renewal-proposal.md`: scroll to verify the table of contents and at least one domain section render correctly
5. Confirm that document hyperlinks within the text are clickable (cross-references within the proposal are relative links and will not resolve from GitHub Gist — this is expected and acceptable; only external URLs need to be live)

If any Gist fails the incognito test, it was accidentally created as "Secret" rather than "Public." Delete and recreate as Public.

---

### 1.4 Fill Template URL Placeholders

**Tool**: Text editor or find-replace in the repository  
**Files to update**: Three distribution template files  
**Estimated time**: 15-20 minutes  

Open each of the three template files and replace all `[link]` placeholders with the corresponding Gist URLs recorded in Step 1.2. The `DISTRIBUTION_GUIDE.md` "URL Placeholders" section contains the exact mapping of which document each `[link]` placeholder refers to. Follow that mapping exactly.

```
distribution-substack-drafts.md     — replace [link] instances
distribution-reddit-templates.md    — replace [link] instances
distribution-institutional-outreach-templates.md — replace [link] instances
```

Also in `distribution-institutional-outreach-templates.md`: replace `[Your name]` and `[Contact information]` in all 11 sign-off blocks. These are the sender's name and contact information. Do this once; all templates share the same sign-off format.

**Failure mode — missed placeholder:**  
After filling, run a search for the string `[link]` across all three template files. If any instances remain, they were missed. Run a second search for `[DOMAIN_` to catch any domain-name placeholders that require specific Gist URLs (Path A+37 only — Domain 37 gets its own Gist, see Part 3).

---

### 1.5 Verify Influencer Contact List

**Files**: `DISTRIBUTION_OUTREACH_CONTACTS.md`, `policy-influencer-mapping.md`, `execution/tier-1-contact-batches.md`  
**Verified total contacts**: 150+ across all tiers (Tier 1: 25, Tier 2: 45+, Tier 3: 55+, Domain 37-specific: 7-16)  

**Spot-check procedure (30-40 minutes):**

Verify the top 15 Tier 1 contacts are still at their listed institutions. Do not attempt to verify all 150+ contacts before launch — this is not efficient use of pre-launch time. The BATCH_1_CONTACT_VERIFICATION.md confirmed all five Batch 1 contacts are current as of April 29. The following 10 additional Tier 1 contacts should be spot-checked immediately before sending:

| Contact | Institution | Verify At |
|---------|-------------|-----------|
| Nicholas Stephanopoulos | Harvard Law | hls.harvard.edu/faculty/nicholas-stephanopoulos/ |
| Olatunde Johnson | Columbia Law | law.columbia.edu (Constitutional Democracy Initiative) |
| Wendy Weiser | Brennan Center | brennancenter.org/people/wendy-weiser |
| Ian Bassin | Protect Democracy | protectdemocracy.org/team/ian-bassin/ |
| Marc Elias | Democracy Docket | democracydocket.com/about/ |
| Ruth Greenwood | Harvard Voting Rights Clinic | hls.harvard.edu/clinics/ |
| Theda Skocpol | Harvard Kennedy School | hks.harvard.edu/faculty/theda-skocpol |
| Erwin Chemerinsky | Berkeley Law | law.berkeley.edu (dean's page) |
| Heather Gerken | Ford Foundation | fordfoundation.org (confirm president role) |
| Pamela Karlan | Stanford Law | law.stanford.edu/pamela-s-karlan/ |

For each: confirm current title and institutional email pattern. If a contact has moved, check the new institution for a forwarding address, or use the new institution's general contact form with a routing note. Do not send to a departed contact — the email bounces and the replacement may never see it.

**Formatting check**: The contact tables use a consistent format: Name | Title | Institution | Contact | Value Proposition | Source. Verify that each Tier 1 contact row has a contact method filled in (direct email, clinic contact form, or general contact route). Rows with an empty contact column are incomplete and need a contact method before the send wave that includes them.

---

### 1.6 Verify Email Service and Delivery Configuration

**Minimum requirement**: A functioning email account with the ability to send personalized individual emails and track open rates if desired.  

**If using standard Gmail/personal email (minimum viable setup):**
- Verify your email address is the one you want recipients to reply to
- Confirm your email signature includes name, title/affiliation if any, and a link to the Substack publication
- Send a test email to yourself before the first batch send to verify formatting (markdown-formatted content renders differently across email clients)

**If using Mailgun or SendGrid for batch send:**
- Verify API key is active and quota is sufficient (Mailgun free tier: 100 emails/day; SendGrid free tier: 100/day)
- Configure SPF and DKIM records for your sending domain before first batch send — this is the single most effective spam-filter prevention measure
- SPF record: add `include:mailgun.org` or `include:sendgrid.net` to your domain's DNS TXT records
- DKIM: generate DKIM keys in your service dashboard and add to DNS before sending
- SPF/DKIM setup takes 24-48 hours to propagate — configure before you begin Gist creation if using a dedicated sending domain

**If not using a dedicated domain (sending from Gmail or similar):**
- Gmail handles SPF/DKIM automatically
- For personalized individual emails (Tier 1, Batch 1-3), send individually from Gmail — no bulk-send tool required
- For Tier 2 and Tier 3 volume sends, consider Mailgun or a Gmail mail-merge extension (Gmass, Yet Another Mail Merge)

---

## Part 2: Path A — Immediate 35-Domain Distribution

**Total duration from path decision to first email sent: 3.5-4.5 hours**  
**User time commitment: 3.5-4.5 hours Day 0 setup + 30-45 minutes/day for personalization across Days 1-4**  
**Launch day (Batch 1 sends): Day 5 (May 4, 2026)**  
**Full path documentation**: `path-a-execution-roadmap.md` (740 lines)  

---

### Phase 1: Gist Creation and Template Fill (45 minutes)

Complete Part 1 of this document (Sections 1.1-1.6) in full. This is not optional for Path A — the email templates cannot go out with `[link]` placeholders unfilled.

**Path A-specific Gist note**: Path A does not require a separate Domain 37 Gist. Domain 37 is distributed as part of the main `democratic-renewal-proposal.md` Gist — it is already integrated into that document. The six canonical Gists cover all Path A distribution content.

**Domain count update (Orchestrator task, 15-30 minutes, parallel with Gist creation):**

While the user creates Gists, the orchestrator executes the domain count update across all template files:

1. In `distribution-substack-drafts.md`: search for "28-domain" and "34-domain" — replace all instances with "35-domain" or "35 domains" as context requires
2. In `distribution-reddit-templates.md`: same search-and-replace
3. In `distribution-institutional-outreach-templates.md`: update all subject lines and opening paragraphs referencing domain count
4. In `democratic-renewal-executive-summary.md`: update any stale domain count references in the header

Verify: after replacement, search all template files for "28" as a standalone number adjacent to "domain" — confirm zero remaining instances.

---

### Phase 2: Template Field Fill (90 minutes, Days 1-4)

Template files are at:
- `distribution-institutional-outreach-templates.md` (11 email templates, 4 categories)
- `distribution-substack-drafts.md` (7 post drafts)
- `distribution-reddit-templates.md` (8 subreddit-tailored drafts)

**Fields requiring fill in every template:**

| Placeholder | What to Insert | Notes |
|-------------|---------------|-------|
| `[link]` | Gist URL per document-type map in DISTRIBUTION_GUIDE.md | Done in Step 1.4 |
| `[Your name]` | Sender's full name | One replacement in all 11 email sign-offs |
| `[Contact information]` | Email address and optional Twitter/Substack handle | One replacement in all 11 email sign-offs |
| `[Substack URL]` | Your Substack publication URL | Fill after Substack is configured |
| `[DATE]` | April 30 or May 4 depending on send timing | Fill immediately before each send wave |

**Fields requiring per-contact personalization (Tier 1 only):**

Using `EMAIL_PERSONALIZATION_GUIDE.md`, personalize the top 15 Tier 1 emails. Each personalized email requires:
- A specific reference to the recipient's recent work or their organization's active litigation/research
- Domain highlighting matched to their institutional focus (use the "Value Proposition" column in `DISTRIBUTION_OUTREACH_CONTACTS.md`)
- If a personal connection exists, reference it directly ("your 2024 paper on the efficiency gap is cited in Domain 1, Section 3")
- Subject line variant from the options in `EMAIL_PERSONALIZATION_GUIDE.md` — do not use identical subject lines across all Tier 1 sends (spam filters flag identical subject lines at volume)

**Priority personalization order (Days 1-4, complete before Day 5 launch):**

1. Wendy Weiser (Brennan Center) — lead with Domain 1 + April 2026 four-state SAVE Act analog enactments
2. Marc Elias (Democracy Docket) — lead with Domain 1 NVRA analysis + May 30 consent decree window
3. Ian Bassin (Protect Democracy) — lead with Domain 29 (their tracker is cited) + framework partnership framing
4. Ryan Goodman (Just Security) — lead with Domain 6 (judicial independence) + Domain 25 FISA analysis
5. Erica Chenoweth (Harvard Kennedy School) — lead with theory of change + Harvard funding freeze (Domain 27)
6. Nicholas Stephanopoulos (Harvard Law) — lead with Domain 1 efficiency gap + Domain 33 gerrymandering
7. Ruth Greenwood (Harvard Voting Rights Clinic) — lead with Domain 1 + NVRA litigation strategy
8. Olatunde Johnson (Columbia CDI) — lead with full structural framework, constitutional democracy framing
9. Erwin Chemerinsky (Berkeley Law) — lead with full framework + "We Hold These Truths" alignment
10. Theda Skocpol (Harvard) — lead with organizational depth case studies, Diminished Democracy connection
11. Pamela Karlan (Stanford) — lead with Domain 1 + Domain 35 (SCOTUS litigation clinic)
12. Heather Gerken (Ford Foundation / Yale) — lead with foundational framework + grantmaking relevance
13. Joanna Lydgate (States United) — lead with Domain 33 + Domain 37 state-level framing
14. Shahrzad Shams (Roosevelt Institute) — lead with Domain 2 + institutional integrity program
15. Molly Reynolds (Brookings) — lead with Domain 2 + Domain 26 + Domain 34

Do not send Tier 1 personalized emails before Day 5. The Substack launch is the anchor event. Simultaneous multi-channel activation (email + Substack publish + Reddit post) creates compounded credibility — the recipient receives the email, then separately discovers the Substack post, then sees the Reddit discussion. This is not a coincidence the recipient notices; it is the framework appearing in multiple professional contexts simultaneously.

**Failure mode — missing template fields after fill:**  
After completing all fills, run a final search across all three template files for the string `[`. Any remaining bracket-enclosed text is an unfilled placeholder. Most common misses: `[DATE]` (fill immediately before send), `[Substack URL]` (fill after Substack is configured), `[Relevant domain title]` in Reddit templates (fill per post).

---

### Phase 3: Contact Verification (60 minutes, Days 0-4)

Complete Section 1.5 of this document. Then add the following Path A-specific checks:

**Duplicate check**: Open `DISTRIBUTION_OUTREACH_CONTACTS.md` and `policy-influencer-mapping.md` side by side. The same individual may appear in both files (the files were built in different sessions). Identify and remove duplicates from your send list — sending the same person two copies of the same email is unprofessional and reduces response rates. The simplest approach: maintain a single master send spreadsheet, add each contact once, and check off when sent.

**Bounce prevention — before the Day 10 bulk wave:**  
For Tier 1 (25 contacts), sending individually from Gmail is sufficient — individual emails almost never trigger spam filters.  
For Tier 2 and Tier 3 (100+ contacts across multiple send waves), run email addresses through a validation service before the Day 10 send. Options:
- Mailgun validation API (included if using Mailgun for sending): `https://api.mailgun.net/v4/address/validate?address=[email]`
- NeverBounce or ZeroBounce (free tiers: 1,000 validations/month)
- Manual check for obvious bounce risks: generic addresses (info@, contact@) forward to staff but may not reach the named individual; verify routing note in the contact record

**Remove flagged addresses** from send lists before the Tier 2/3 waves. Do not attempt to resend to a bounced address — verify the correct address first.

---

### Phase 4: Day 5 Launch — Email Send Sequence (90 minutes)

**Day 5 launch sequence (May 4, 2026):**

```
09:00 — Publish Substack Post 1 (Launch/Overview post from distribution-substack-drafts.md)
         This anchors the multi-channel launch. All same-day emails reference the live Substack post.

10:00 — Send Batch 1, Sub-wave A: Tier 1 Law School emails (contacts 1-8 in priority order)
         8 emails, individually personalized
         Subject lines: use EMAIL_PERSONALIZATION_GUIDE.md variants for academic contacts

11:00 — Post to r/PoliticalScience (Reddit Template 1 from distribution-reddit-templates.md)
         Verify karma threshold is met before posting — moderator removal within first hour is fatal

12:00 — Send Batch 1, Sub-wave B: Tier 1 Think Tank emails
         (Brennan Center, Roosevelt, EPI, Brookings contacts)
         7 emails, individually personalized

14:00 — Post to r/USPolitics (Reddit Template adapted for general audience)

15:00 — Send Batch 1, Sub-wave C: Tier 1 Civil Rights / Election Protection emails
         (LDF, Lawyers' Committee, ACLU Voting Rights, Democracy Docket, States United, Protect Democracy)
         8 emails, individually personalized

16:00 — Send Batch 1, Sub-wave D: Tier 1 Foundation contacts
         (Ford/Gerken, Knight Foundation, OSF democracy contacts)
         4 emails, individually personalized
```

**Day 5 total: approximately 27 Tier 1 emails sent.**

---

### Phase 5: Days 10-21 — Tier 2 and Tier 3 Distribution (90 minutes spread across two weeks)

**Day 10 (May 14): Batch 2 — Tier 2 Secondary Contacts (45 contacts)**

Batch 2 contacts are secondary academics, policy researchers, and civil society staff who did not receive Batch 1. They do not require full personalization — use template-based emails with a sentence or two of contact-specific customization. Stagger sends over 2-3 hours to avoid triggering Gmail's bulk-send detection.

**Day 10 concurrent: Substack Post 2 + Reddit r/law post**  
Publish Substack Post 2 (Electoral Reform Deep Dive) simultaneously with Batch 2 send. This maintains the multi-channel compounding.

**Day 14-16: Batch 3 — Tier 3 Contacts (55+ contacts) and State AG Wave**

Tier 3 includes state-level attorneys general staff, state legislative staff, and extended civil society. These contacts can receive template emails with minimal personalization. Scheduling for Day 14-16 gives Tier 1 recipients a week to respond before the broader distribution creates potential overlap.

**Day 14-16 concurrent: Substack Posts 3-4 + additional Reddit posts**  
Continue the staggered Substack publication schedule. Post 3 (Accountability and Oversight), Post 4 (Trackers and Monitoring).

**Day 21: Close of Phase 1 distribution window**  
All contact tiers have been reached. The Substack sequence is at Post 4 of 7. Reddit engagement is ongoing. Day 21 is the natural assessment point — evaluate response rates and adjust Phase 2 approach based on what has landed.

---

### Phase 5 (Optional): Social Media Scheduling (90 minutes, parallel with Days 1-21)

**Substack** (4 posts staggered over 2 weeks, scheduled in advance):
- Post 1: Day 5 (May 4) — Launch / Overview
- Post 2: Day 10 (May 14) — Electoral Reform Deep Dive
- Post 3: Day 14 (May 18) — Accountability and Oversight
- Post 4: Day 16 (May 20) — Trackers and Monitoring

Substack allows scheduled publication. Stage all four posts as drafts before Day 5 and set scheduled publication times. This reduces execution burden during the active send weeks.

**Reddit** (5-6 posts staggered over 2 weeks):
- Target subreddits: r/PoliticalScience, r/law, r/USPolitics, r/neutralpolitics, r/LaborUnion, r/environment
- Timing: stagger with at least 2-3 days between posts across different subreddits
- Do not cross-post the identical text to multiple subreddits — Reddit's spam detection flags duplicate content

**Tools**: Buffer (free tier: 3 social accounts, 10 scheduled posts) for advance scheduling. This allows queuing posts without requiring real-time execution.

**Failure mode — Reddit post removed by moderators:**  
Cause: Post removed for rule violation (low karma, spam detection, self-promotion rule, no-petition rule).  
Recovery: (a) Check the subreddit's pinned rules before reposting; (b) If removed for self-promotion, reframe as "sharing research" with explicit educational framing rather than "I wrote this"; (c) Backup subreddits: r/politics, r/politicalphilosophy, r/americanpolitics, r/legaladvice (for specific consent-decree topics). Every target subreddit has 2-3 backup communities. Do not attempt to repost to a subreddit that removed you within 48 hours — wait and try a different angle or backup community.

---

## Part 3: Path A+37 — Hybrid Distribution

**Total duration: 5-6 hours for full Phase 1 + 2 additional hours for Domain 37 Phase 2 coordination**  
**User time commitment: 3.5-4.5 hours Day 0 setup + 30-45 minutes/day Days 1-4 + 2 hours Phase 2 prep (Days 8-12)**  
**Phase 1 launch (general distribution): April 30, 2026 (Day 0)**  
**Phase 2 launch (Domain 37 targeted): May 12, 2026 (Day 12)**  
**Full path documentation**: `path-a-37-execution-roadmap.md` (800 lines, 8-week timeline)  

Path A+37 executes all five phases of Path A (Part 2 above), plus a sixth phase: a targeted Domain 37 send to election protection organizations after Phase 1 has established credibility. The Phase 1 execution for Path A+37 is largely identical to Path A with three differences: (1) the launch date is April 30 rather than May 4; (2) a separate Domain 37 Gist is created; and (3) the Domain 37 contacts are held back from Phase 1 and receive a specialized Phase 2 email.

---

### Phases 1-5: Same as Path A with Three Modifications

**Modification 1: Launch date shifts to Day 0 (April 30)**

Path A+37 captures the April 30 FISA Section 702 expiration as an immediate hook. The Day 5 launch sequence in Path A (May 4) becomes a Day 0 sequence for Path A+37:

```
April 30, 2026:
  - Complete Part 1 (Gist creation, template fill): 30-45 minutes
  - Send Batch 1 Tier 1 emails (Phase A — no Domain 37 contacts): starts same day
  - Publish Substack Post 1 simultaneously
```

The FISA attention hook is maximally relevant at Brennan Center, EFF, and Senate civil liberties staff during the week of the vote outcome (April 30-May 5). Email subject lines for Batch 1 contacts at these organizations should reference the FISA vote explicitly. Sample subject line: "Framework for understanding Section 702's democracy implications — released today."

**Modification 2: Separate Domain 37 Gist**

Create a seventh Gist specifically for Domain 37:

```
File: projects/resistance-research/domains/domain-37-federal-executive-interference-2026-midterms.md
Filename in Gist: domain-37-federal-executive-interference-2026-midterms.md
Status: 543 lines, production-ready, current through April 27, Hungary election outcome integrated
```

This Gist URL goes into the Phase 2 Domain 37 email templates (not into Phase 1 general distribution templates). Record the URL in `DISTRIBUTION_GIST_URLS.md` with a clear label: "Domain 37 — Phase 2 targeted distribution only."

**Modification 3: Domain 37 contacts are withheld from Phase 1**

The following contacts appear in `DOMAIN_37_SEQUENCING_PLAN.md` as Phase 2-specific recipients. They are not in Phase 1 Batch 1-3 sends:

- Democracy Docket staff (election protection litigation team beyond Marc Elias)
- Campaign Legal Center (voting rights and election law contacts)
- ACLU Voting Rights Project staff (beyond Tier 1 contacts who receive Phase 1)
- Common Cause election protection team
- State AGs already engaged in election administration litigation
- Protect Democracy election-specific staff (Ian Bassin receives Phase 1 as Tier 1 general contact; his election-specific colleagues receive Phase 2)
- National Redistricting Foundation contacts

Do not add these contacts to Phase 1 batches even if they appear in the general `DISTRIBUTION_OUTREACH_CONTACTS.md` tables. The sequencing rationale: Domain 37 reaches these organizations in a targeted briefing after Phase 1 has established the framework's credibility, framed specifically for their election protection dockets, rather than buried in a general 35-domain distribution.

---

### Phase 6: Domain 37 Distribution Timing (2 hours, Decision Gate on Days 8-12)

**Decision gate structure**: Before executing Phase 2, the user assesses Phase 1 response signals to calibrate Phase 2 framing and targeting. This is a 30-minute review, not a major decision point.

**Window 1 — Days 1-3 post-Phase 1 launch (May 1-3):**

The first Domain 37 sends go out to broad-audience contacts who can amplify the framework before it reaches highly specialized election-protection organizations:
- Universities (election law faculty not in Phase 1 Tier 1 — the full list in DISTRIBUTION_OUTREACH_CONTACTS.md Pillar 1 Section 1A, contacts 6-15)
- Think tanks (Brookings, Cato election integrity researchers, AEI political process scholars)
- Law reviews and policy journals (submitting a condensed version of Domain 37 as a policy brief — this is a separate action, not part of the email distribution, but creates a citation trail that strengthens the Phase 2 send)
- Media contacts (journalists covering election law and voting rights at Politico, Roll Call, The Atlantic, ProPublica)

Rationale: Broad academic and media exposure in Days 1-3 means that when election protection organizations receive Domain 37 in Phase 2, they are receiving something that already has institutional visibility — not a cold outreach document.

**Window 2 — Days 4-12 (May 4-12): Phase 2 Election Protection Targeted Send**

The core Phase 2 send targets the 7-16 election protection organizations in `DOMAIN_37_SEQUENCING_PLAN.md`. This send is highly personalized — each email references the organization's active litigation docket and frames Domain 37's five-mechanism interference analysis in terms directly relevant to their work.

**Phase 2 send sequence:**

```
Day 8 (May 8): 
  - Send to Democracy Docket (Marc Elias + election litigation staff)
    Lead: Domain 37 Section 3 (voting system interference) + Domain 1 NVRA analysis
    Frame: "Companion document to your current NVRA consent decree work"
    
  - Send to Campaign Legal Center
    Lead: Domain 37 Section 2 (DOJ election division weaponization) + Domain 29
    Frame: "Documents the DOJ pattern your litigation is challenging"

Day 9 (May 9):
  - Send to ACLU Voting Rights Project
    Lead: Domain 37 Sections 1-3 + Domain 1 state SAVE Act wave
    Frame: "Five-state analog SAVE Act wave documented with litigation-ready sources"
    
  - Send to Common Cause
    Lead: Domain 37 Section 4 (Section 3 disqualification analysis) + Domain 33
    Frame: "State-level autocratization patterns documented as a unified framework"

Day 10 (May 10):
  - Send to States United Democracy Center
    Lead: Domain 37 + Domain 33 (state legislative autocratization)
    Frame: "Interstate pattern documentation for your state-level advocacy work"
    
  - Send to Protect Democracy election staff
    Lead: Domain 37 full framework + their existing tracker cited in Domain 29
    Frame: "Framework that builds on your prosecutorial weaponization tracker"

Day 12 (May 12):
  - Send to state AG election protection staff (in states with active voting rights litigation)
    Lead: Domain 37 + Domain 1 consent decree clock documentation
    Frame: "Analysis of the May 30 consent decree clock and its implications"
    
  - Send to National Redistricting Foundation contacts
    Lead: Domain 37 Section 5 (post-election certification interference) + Domain 33
    Frame: "Redistricting suppression connects to the broader certification interference pattern"
```

**Decision gate assessment (Day 7, 30 minutes):**

Before executing Days 8-12 sends, review Phase 1 response signals:
- Open rate on Batch 1 emails: if open rate is above 40%, Phase 1 is landing well and Phase 2 framing should stay consistent; if below 30%, consider adjusting subject line framing for Phase 2
- Any direct responses from Tier 1 contacts: positive responses from Democracy Docket, ACLU, or Protect Democracy in Phase 1 can be referenced in Phase 2 personalization ("you mentioned interest in the voting rights sections — Domain 37 is the companion document")
- Reddit engagement: if Phase 1 Reddit posts received significant upvotes and cross-posts, reference the public engagement level in Phase 2 emails as evidence of the framework's reach

**Failure mode — Domain 37 timing wrong, early exposure causes premature polarization:**

If Domain 37 reaches major outlets before Phase 2 targeted send, and is framed as an "election interference" document in ways that trigger defensive responses from election administration officials, the targeted Phase 2 send can still succeed by leading with the legal and analytical value rather than the political framing.

Recovery: If polarization occurs (unlikely but possible), shift Phase 2 framing from "election interference analysis" to "litigation support framework for voting rights organizations." The document's analytical content does not change — only the framing of the cover email. The five-mechanism analysis in Domain 37 stands on its own merits regardless of how it is introduced.

**Contingency — skip Domain 37 sequencing entirely:**

If Phase 1 response rates are unexpectedly high and election protection organizations contact the user directly in response to Phase 1, the Phase 2 Domain 37 sequencing can be collapsed: send Domain 37 as a follow-up to all Tier 1 contacts who responded, rather than the targeted 7-16 organization sequence. This is the "merge into full distribution" contingency — it sacrifices the targeted sequencing in favor of momentum.

---

## Part 4: Path B — Continue Optional Updates Pre-Distribution

**Total duration: 2-4 weeks (domain research extension) + 3.5-4.5 hours (execution, same as Path A)**  
**User time commitment: 8-12 hours additional research + 12-18 hours execution across 3 weeks**  
**Target launch: May 12 (optimistic) to May 20 (maximum holdoff)**  
**Hard trigger forcing distribution regardless of research status**: Trump v. Slaughter SCOTUS decision; major ICE/DHS enforcement escalation; any reconciliation vote on SAVE Act or OBBBA Medicaid  
**Full path documentation**: `path-b-continuation-roadmap.md` (482 lines, Day 7 checkpoint decision tree)  

---

### Phase 0: Identify Research Gap and Scope Extension (2 hours, Day 0)

Path B begins with a structured research gap audit, not open-ended research. The audit produces a specific scope decision: which 1-3 domains get updated, to what depth, within what time budget. Without this scope decision upfront, Path B can drift indefinitely.

**Step 1: Run the gap audit (1 hour)**

Open `post-domain-26-completeness-audit.md` and `phase-2-expansion-candidates.md`. These documents identify the domains most likely to benefit from April-May 2026 updates. The current gaps are:

| Domain | Gap Description | Estimated Update Time | Priority |
|--------|----------------|----------------------|----------|
| Domain 1 (Voting Rights) | Iran WPR outcome not yet filled; state SAVE Act wave ongoing | 1-2 research sessions | High |
| Domain 25 (Surveillance / FISA) | Senate S.4344 vote outcome and presidential signature pending | 30 minutes (fills automatically post-May 1) | Medium |
| Domain 6 (Judicial Independence) | May 2026 circuit vacancy wave outlined in MAY_2026_TRACKER.md but not integrated | 1 research session | Medium |
| Domain 33 (State Legislative Autocratization) | 155-bill count as of April; ongoing wave | 1 research session | High |
| Domain 37 (Federal Executive Interference) | Post-Hungary election comparative analysis integrated; Hungary outcome already in. Any post-April 27 federal development | 30-60 minutes monitoring | Medium |

**Step 2: Make the scope decision (30 minutes)**

The session 662 audit confirmed that all 35 domains are production-ready. Path B is enhancement, not prerequisite. The scope decision should answer: does the enhancement justify the delay against the advocacy windows that are closing?

Apply this decision rule: if the planned research would add legal citations or factual developments that election protection organizations specifically need (e.g., new state SAVE Act implementing regulations with specific effective dates), it justifies the delay. If it is updating general-interest current-events currency that does not change the framework's analytical conclusions, it does not justify the delay.

**Recommended Path B scope** (if proceeding):

- **Domain 25**: Fill Senate S.4344 outcome and presidential signature (30 minutes, fills itself after May 1 — do this before any launch regardless of path)
- **Domain 1**: Integrate any new state SAVE Act implementing regulations with specific voter removal effective dates (1 session, ~2 hours)
- **Domain 33**: Update 155-bill count with any session-end totals from AZ, OH, WI, NE before adjournment (1 session, ~2 hours)

Estimated total Path B research: 5-6 hours across 2-3 research sessions.

**Step 3: Set a hard stop date (15 minutes)**

Before beginning any Path B research, write the hard stop date into `CHECKIN.md`. The recommended hard stop is May 12. After May 12, the NVRA August 7 quiet period leaves only 87 days — below the 6-8 week institutional adoption cycle that requires 90+ days for full value. After May 20, the spring legislative sessions in AZ, OH, WI, NE will have adjourned and the Domain 33 state legislative content becomes less actionable for advocacy.

Format for CHECKIN.md entry:
```
Path B hard stop: May 12, 2026
After this date, proceed directly to Path A execution regardless of research completion status.
```

---

### Recommended Approach: Parallel Path B (Path B + Distribution Prep Running Concurrently)

The most efficient Path B execution runs distribution preparation in parallel with domain research, so the launch date is a function of research completion rather than a hard delay.

**Day 0-1 (starting now):**
- User: begin domain research sessions per the scope decision above
- Orchestrator: complete Part 1 (Gist creation, template fill, contact verification) in parallel
- Net effect: by the time domain research is complete (~May 8-12), all distribution infrastructure is already in place. Launch can happen within hours of research completion.

This approach eliminates the "do research, then do distribution prep" sequential bottleneck. It makes Path B functionally equivalent to a delayed Path A, rather than a multi-week sequential operation.

**Day 1-7: Domain Research Sessions**

For each domain in the Path B scope:

1. Open the domain file and the corresponding monitoring document (e.g., `MAY_2026_TRACKER.md` for upcoming developments)
2. Run targeted web searches for new factual developments since the last update date
3. Add new developments to the relevant domain section with source citation, date, and session tag
4. Update the "Last updated" frontmatter field
5. Run a cross-reference check: does the new information affect any other domain's content? (Use the cross-reference tables in `PHASE_1_EXECUTION_READINESS.md` as a guide)

**Day 7: Checkpoint Assessment**

`path-b-continuation-roadmap.md` contains a mandatory Day 7 checkpoint decision tree. At this checkpoint:

- If domain research is producing material new findings that change the framework's analytical conclusions: continue to May 12
- If domain research is producing incremental currency updates but not new conclusions: pivot to Path A+37 immediately (distribution prep is already complete)
- If any hard trigger has fired (Trump v. Slaughter decision, major enforcement escalation, reconciliation vote): pivot to Path A+37 immediately regardless of research completion

**Day 7 pivot procedure if triggering Path A+37:**

1. Open this document, Part 3
2. Execute Phase 6 (the one modification that shifts Path B's already-complete Phases 1-5 into Path A+37 mode)
3. Send Batch 1 within 24 hours of the hard trigger event — timing responsiveness to the hard trigger is itself an advocacy asset

---

### Example Scenario: Deepening Domain 1 with New State SAVE Act Data

If choosing to extend Domain 1 (Voting Rights) with new state autocratization data:

**Research phase (8-12 hours across 3 sessions):**
- Session 1 (Day 1-2): Compile state-by-state SAVE Act implementing regulation status; identify voter removal effective dates for FL, MS, SD, UT enactments; document any court challenges filed
- Session 2 (Day 3-4): Research tribal voting interference provisions in any new state legislation; compile evidence on disproportionate impact (Native American, Hispanic, and Black voter roll purge rates under new laws)
- Session 3 (Day 5-6): Integrate Domain 1 updates; verify cross-references to Domain 33 (state autocratization), Domain 37 (federal executive interference), and Domain 29 (DOJ enforcement posture toward state SAVE Act compliance)

**Integration phase (2-3 hours, Day 6-7):**
- Add new data to Domain 1 Sections 2.1, 2.2, 5, and 6
- Update the cross-reference note in Domain 37 Section 3 to reference the new Domain 1 data
- Update the executive summary table row for Domain 1
- Verify the litigation tracker entry for CASA v. DHS still reflects the most recent court filing (SAVE Act consent decree status)

**Updated launch: May 12 at the latest (with Day 7 checkpoint as the go/no-go gate)**

---

## Part 5: Post-Launch Monitoring

**Applies to all paths. Begin monitoring immediately after Batch 1 send.**  

---

### Hours 1-24 (Post-Batch 1 Send)

**Email response tracking:**

- Check sent emails for bounced-address notifications within 1 hour of send. Bounces arrive immediately. Record any bounced addresses in the bounce log in `DISTRIBUTION_EXECUTION_LOG.md`. Do not attempt to resend until you have a verified alternative address.
- Check for out-of-office replies within 4 hours. Researchers are often traveling. If an OOO reply gives a return date, note it for follow-up timing.
- Check for substantive replies within 8 hours. A same-day reply from a Tier 1 contact is a signal of high engagement. Respond to substantive replies within 24 hours.

**Open rate and click tracking (if using Gmail tracking or Mailgun):**
- Mailgun analytics dashboard: navigate to Logs > Tracking. Filter by "opened" and "clicked." Open rate should begin accumulating within hours of send.
- Gmail: if using a tracking pixel extension (Mailtrack, Streak), check the extension dashboard.
- Target metric for Batch 1: 40%+ open rate within 24 hours. Academic and advocacy contacts have high email engagement rates for personalized outreach.

**Reddit monitoring:**
- Check Reddit post within 2 hours of publishing — early downvotes can suppress visibility. If a post drops below 0, it is effectively invisible. Engage with early comments (factual clarifications, source links) to boost engagement signals.
- Comment on your own post within 30 minutes of publishing with a "top comment" that highlights the most important domain or finding — this pins a useful response at the top before other comments arrive.

**Substack monitoring:**
- Substack post views and subscriber counts update in real time in the publication dashboard. Track 24-hour views on Post 1.
- Any subscriber notifications (new subscribers from the launch post) are advocates who opted in to the full framework — these are high-value contacts for Phase 2 follow-up.

**Discord protocol (if the user has a research Discord server):**
- Post Batch 1 send completion in the relevant Discord channel
- Post Substack live link
- Hourly updates for first 6 hours: new opens, replies, Reddit engagement
- Summary post at 24 hours with first-day metrics

---

### Days 2-7 (Institutional Response Window)

**Key metrics to track:**

| Metric | Target | Source |
|--------|--------|--------|
| Batch 1 open rate | 40%+ | Mailgun / Gmail Tracking |
| Batch 1 click rate | 15%+ (clicks through to Gist URLs) | Mailgun / Gmail Tracking |
| Batch 1 reply rate | 3%+ (substantive replies, not OOO) | Gmail inbox |
| Substack subscriber growth | Any growth is a positive signal | Substack dashboard |
| Reddit post score | Net positive (above 0) on all posts | Reddit analytics |

**New contact logging:**

When Tier 1 contacts forward the framework to colleagues, those colleagues may contact the user directly. Log all inbound contacts in `DISTRIBUTION_EXECUTION_LOG.md` — these are warm leads for Phase 2 follow-up. A referral from Wendy Weiser (Brennan Center) to a colleague is worth more than a cold Tier 2 send.

**Monitoring for secondary amplification:**

- Search Twitter/X for the user's name + "democracy framework" or for quoted phrases from the executive summary every 48 hours
- Search Google for the Gist URLs after Day 3 (Google indexes public Gists; if the framework is being shared, it will appear in search results)
- Check Substack for cross-posts (Substack shows "Restacks" in the publication stats)
- Monitor for podcast/interview requests arriving via email. These take 2-4 weeks to materialize after initial distribution — check email carefully for subject lines containing "podcast," "interview," or "conversation"

---

### Week 2+ (Long-Term Impact Monitoring)

**Institutional adoption signals (primary success indicators):**

The `institutional-adoption-playbooks.md` provides the framework for tracking deeper adoption. The key signals in the first 4 weeks:

1. Law review / policy journal inquiries about the framework (citation pipeline begins here)
2. Think tank fellows referencing the framework in published pieces (watch Brookings, Brennan Center, Roosevelt Institute blogs)
3. Senate or state legislative staff requests for additional materials (indicates the framework is being used in policy preparation)
4. Litigation brief citations (the most durable success indicator — monitor using Google Scholar alerts for the framework's title or Domain-specific findings)

**Top-performing domain identification:**

If email tracking shows significantly higher click rates on links to specific domain Gists (or higher engagement on Reddit posts featuring specific domains), those domains are the Phase 2 priority. The `measurement-and-iteration-framework.md` provides a structured approach for translating engagement data into Phase 2 domain selection.

**Power-law distribution recognition:**

Distribution often follows a power law: 3-5 Tier 1 contacts will generate 80% of the long-term impact through referrals, citations, and institutional adoption. Identify which contacts generated the most downstream activity by Week 2, and concentrate Phase 2 follow-up energy there rather than spreading evenly across all 150+ contacts.

---

## Part 6: Failure Modes and Recovery

**Comprehensive failure mode reference for all execution phases.**

---

### Email Delivery Failures

**Symptom**: High bounce rate (more than 5% of Tier 1 emails bounce).  
**Cause**: Stale addresses, institutional email address format changes, domain-level spam rejection.  
**Recovery**:  
1. For hard bounces (address does not exist): check the organization's website for the correct address. Institutional email patterns change when staff move between positions.  
2. For soft bounces (mailbox full, server unavailable): wait 24 hours and resend once.  
3. For institutional spam rejection (entire domain rejects the email): contact the organization through an alternative channel (contact form, Twitter DM, LinkedIn) with a brief introduction and a request to send the framework.  
4. Prevention: Run Tier 2 and Tier 3 addresses through Mailgun validation API or NeverBounce before bulk send.

### Spam Filter Blocks

**Symptom**: Open rates below 10% on Tier 2 or Tier 3 sends; Mailgun logs show "delivered" but no opens.  
**Cause**: Email domain lacks SPF/DKIM configuration; bulk send pattern triggered spam detection; subject line contains spam-flagged language.  
**Recovery**:  
1. Check SPF/DKIM configuration in your email service dashboard. If unconfigured, this is the primary cause.  
2. Stagger sends — no more than 25 emails per hour from a personal Gmail account.  
3. Vary subject lines across sends — identical subject lines in bulk are a spam signal.  
4. Use a different sending address (a dedicated sending domain) for Tier 2/3 bulk waves.  
5. If using Mailgun and deliverability is poor, switch to SendGrid as the backup service. Both have free tiers.

### Markdown Rendering Issues

**Symptom**: Gist URL shows raw markdown text instead of formatted output.  
**Cause**: UTF-8 encoding issue; `.md` extension not set; Gist created as raw text file.  
**Recovery**:  
1. Check that the Gist filename ends in `.md`.  
2. Delete the Gist and recreate. When pasting content, paste from a plain text editor (not a PDF viewer or formatted word processor) to avoid invisible encoding characters.  
3. If pasting a very large file (democratic-renewal-proposal.md is 4,390 lines), consider using the GitHub CLI: `gh gist create democratic-renewal-proposal.md --public` — this handles encoding automatically.  
4. GitHub CLI command reference: `gh gist create [filename] --public` creates a public Gist from a local file.

### Contact Bounces — Tier 2 and Tier 3 Waves

**Symptom**: Bounce notifications arriving after bulk send.  
**Prevention**: Run all Tier 2/3 addresses through validation before send.  
**Recovery**: For each bounced address, add to the bounce log in `DISTRIBUTION_EXECUTION_LOG.md` with the correct address once found. Do not attempt to resend to the bounced address. Contact the organization through an alternative channel if the contact is high-priority.

### Reddit Post Removal

**Symptom**: Post disappears within hours of publishing, or reaches 0 score and becomes invisible.  
**Cause**: Rule violation (low account karma, self-promotion rule, no-polls rule, duplicate content), automod removal, or community report.  
**Recovery**:  
1. Check the subreddit's modmail for an explanation.  
2. Review the pinned rules and adjust the post framing.  
3. Do not repost the identical content within 48 hours.  
4. Backup subreddits for each target: r/PoliticalScience backup = r/politicalphilosophy; r/law backup = r/legaladvice (for specific topics); r/USPolitics backup = r/politics.  
5. For r/neutralpolitics (the strictest community): read the sidebar rules carefully before reposting. This subreddit requires a specific question-framing format.

### Social Media Platform Account Issues

**Symptom**: Twitter/X account flagged, suspended, or posts downranked.  
**Recovery**:  
1. Do not post the same content from multiple accounts (this triggers platform spam detection).  
2. Maintain distribution across multiple platforms (Substack, Reddit, LinkedIn in addition to Twitter) so no single platform's algorithm is a single point of failure.  
3. LinkedIn is an underutilized channel for academic and policy professional outreach — institutional outreach emails that receive no response may get a reply via LinkedIn direct message.

### Path-Specific Contingency: Path B Research Stalls

**Symptom**: Path B research is producing incremental updates but not the material new findings that justified the delay. Hard stop date is approaching.  
**Recovery**: Invoke the Day 7 checkpoint in `path-b-continuation-roadmap.md` early. Pivot to Path A+37. Distribution prep completed in parallel means the pivot can be executed same-day.

---

## Part 7: Success Metrics

**Framework for evaluating Phase 1 distribution outcomes across all paths.**

---

### Tier 1 Metrics (First-Week Indicators — Leading Signals)

These metrics are available within 7 days of launch and indicate whether the distribution is landing effectively.

| Metric | Target | Minimum Acceptable | Method |
|--------|--------|-------------------|--------|
| Tier 1 email open rate | 40%+ | 25% | Mailgun / Gmail tracking |
| Tier 1 click rate (Gist URLs) | 15%+ | 8% | Mailgun link tracking |
| Tier 1 reply rate | 3%+ substantive | 1% any response | Gmail inbox |
| Substack Post 1 views (24 hours) | 200+ | 50 | Substack dashboard |
| Reddit post score (best post) | 50+ upvotes | 10 net positive | Reddit analytics |
| New Substack subscribers (Day 1-7) | 25+ | 5 | Substack dashboard |

**Interpreting low metrics**: A Tier 1 open rate below 25% indicates a delivery problem (spam filters, bounces) rather than a content problem. Check delivery logs before concluding the content is not landing. A reply rate below 1% at correct delivery indicates a framing problem — subject lines or opening paragraphs are not connecting with the recipient's institutional priorities.

---

### Tier 2 Metrics (Weeks 2-4 Indicators — Institutional Uptake)

| Metric | Target | Source |
|--------|--------|--------|
| Response rate from Tier 1 contacts | 3%+ | Email inbox |
| Positive feedback in responses | 80%+ of responses are constructive / favorable | Email inbox |
| New inbound contacts via referral | 5+ in first 30 days | Email inbox / Substack signups |
| Podcast / media interview requests | 1+ within 4 weeks | Email inbox |
| Social media cross-shares | 5+ organic reposts or quotes | Twitter/Substack search |

---

### Tier 3 Metrics (Weeks 4-8 — Institutional Adoption)

These are the lagging indicators that reflect Phase 1's ultimate impact. They typically materialize 4-8 weeks after distribution and require active monitoring.

| Metric | Target | Source |
|--------|--------|--------|
| State AGs citing the framework | 5+ state AGs reference framework in advocacy materials | AG press releases, briefs |
| Law schools assigning as reading | 3+ law school courses | Course syllabi, faculty outreach responses |
| Litigation brief citations | 1+ citations within 60 days | Google Scholar alerts, PACER |
| Policy proposal integration | 1+ state or federal legislative proposal references the framework | Congress.gov, LegiScan |
| Think tank publications referencing the framework | 2+ Brookings / Brennan Center / Roosevelt publications | Organization publication RSS feeds |

**Qualitative success indicators** that cannot be quantified but are primary signals:

- A faculty member at a law school responds indicating they are incorporating the framework into a clinical project or litigation strategy
- A state AG's office contacts the user for follow-up materials
- A journalist at a major outlet (NYT, Washington Post, Politico) contacts the user for background
- Democracy Docket or Campaign Legal Center cites the Domain 1 NVRA analysis in a new filing
- An academic submits a paper that builds on the framework's findings

Any one of these qualitative outcomes represents disproportionate impact relative to the distribution effort — these are the power-law outcomes that Phase 1 is designed to create conditions for.

---

### Using Metrics to Drive Phase 2 Decisions

**If Tier 1 metrics are strong (open rate 40%+, reply rate 3%+):**  
Phase 2 should prioritize depth over breadth. The Tier 1 contacts who replied are the highest-leverage relationship for institutional adoption. Focus Phase 2 on following up with engaged Tier 1 contacts, sharing additional materials, and facilitating cross-institution introductions.

**If Tier 1 metrics are moderate (open rate 20-40%, reply rate 1-3%):**  
Phase 2 should expand breadth. Tier 2 and Tier 3 sends are the priority. The framework has not yet reached its full potential audience. Consider adjusting subject line framing and opening paragraphs based on what worked in Tier 1 responses.

**If Tier 1 metrics are weak (open rate below 20%, reply rate below 1%):**  
Investigate delivery issues first (spam filters, bounces). If delivery is confirmed but engagement is low, reframe the opening paragraph of institutional outreach emails — the content is not connecting with institutional priorities. The `EMAIL_PERSONALIZATION_GUIDE.md` Section 3 ("Subject Line Variants") provides alternative framings that can be tested.

**Phase 2 domain priority based on engagement data:**  
The domain that generates the highest click-through rate from Gist links (trackable in Mailgun) or the most Reddit engagement is the Phase 2 expansion priority. This is the empirical signal of which framework area has the most resonance with the distribution audience — Phase 2 domain selection should follow the signal, not the original planning assumption.

---

*Created: April 30, 2026*  
*Session: 686 (Phase 1 Execution Playbooks)*  
*Status: Production-ready — activate immediately upon user path decision*  
*Cross-reference: PHASE_1_EXECUTION_READINESS.md (readiness audit), DISTRIBUTION_PATH_QUICK_REFERENCE.md (one-page path comparison), DISTRIBUTION_GUIDE.md (URL placeholder map)*
