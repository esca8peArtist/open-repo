---
title: "Phase 1 Distribution Execution Blueprint"
created: 2026-05-13
status: PRODUCTION-READY
item: Exploration Queue Item 28
scope: "Consolidated quick-start execution guide — all Phase 1 distribution materials synthesized into a single step-by-step document"
companion_docs:
  - PHASE_1_EXECUTION_READINESS.md
  - PHASE_1_CONTINGENCY_PLAYBOOK.md
  - execution/tier-1-contact-batches.md
  - execution/domain-42-contact-list.md
  - policy-influencer-mapping.md
  - DISTRIBUTION_GIST_URLS.md
  - execution/outreach-email-templates.md
  - execution/success-metrics.md
---

# Phase 1 Distribution Execution Blueprint

**Audit verdict**: APPROVED FOR PHASE 1 LAUNCH (PHASE_1_EXECUTION_READINESS.md, April 30)
**Time-to-launch from path decision**: 3–4.5 hours to Batch 1 emails sent
**This document purpose**: Single consolidated execution reference — no need to open multiple files

---

## 1. Overview

Phase 1 is the first public distribution of the 35-domain Democratic Renewal Proposal to high-leverage institutional contacts. The goal is not mass reach. It is credibility establishment — getting the framework cited, endorsed, or engaged with by a small number of bridge-node contacts whose responses create the ambient legitimacy that every subsequent outreach wave benefits from.

**What is ready**: 35+ production-ready research domains, 6 publicly accessible GitHub Gists, 150+ verified contacts across 3 tiers, 9 outreach email templates, a personalization guide, a full contingency playbook, and path-specific execution materials for all three paths.

**What requires your decision before Day 1**:

- **Path A** — Immediate 35-domain distribution. All Blocks 1–7 execute as written. No modifications. Batch 2 preparation begins Day 1 after Batch 1 send.
- **Path A+37** — 35 domains plus Domain 37 (Federal Executive Interference, 2026 Midterms) as a separate track for election-protection contacts. One additional Gist (domain-37) plus a Domain 37 subject-line variant for election-protection recipients. See `execution/path-a-domain37-materials.md`.
- **Path B** — Staged distribution with a feedback-collection window after Batch 1 before Batches 2–4 go out. All Blocks 1–7 execute, plus a feedback mechanism (Airtable or Google Form) set up before send, and Batch 1 emails framed with an explicit feedback invitation. See `execution/path-b-materials.md`.

The path choice affects messaging emphasis and Batch 2 timing — not the Day 1 infrastructure or the Batch 1 contact list.

**Domain 42 note**: Domain 42 (Drug Policy and Democratic Legitimacy) has a hard deadline of May 28, 2026 — the DEA hearing participation notice cutoff for Docket DEA-1362. The Domain 42 sub-batch (10 contacts, Categories A–D) runs on a parallel track from the main Tier 1 Batch 1–3 sequence. Wave 1 of Domain 42 is already overdue as of May 13. This track should be treated as a same-day execution priority alongside the main Batch 1 send. See Section 4 (Batch 1 Quick Reference) and Section 7 (Contingency Playbook) for Domain 42-specific handling.

---

## 2. Pre-Execution Checklist

Complete all items before sending a single email. Estimated time: 30 minutes.

- [ ] **Path decision confirmed** — A / A+37 / B. Your decision inputs Day 1 actions (which Gists to create, which email variant to use, whether to set up a feedback mechanism before send).

- [ ] **Gist URLs verified** — All 6 canonical Gists are live and rendering correctly. Verify by visiting each URL directly and scrolling to the bottom. URLs are in `DISTRIBUTION_GIST_URLS.md`. If any Gist is rendering broken, see contingency Category 4.1 in `PHASE_1_CONTINGENCY_PLAYBOOK.md` before proceeding.

- [ ] **Template URL placeholders filled** — In `execution/outreach-email-templates.md`, `distribution-substack-drafts.md`, and `distribution-reddit-templates.md`, every `[link]` instance has been replaced with the correct Gist URL. The placeholder-to-URL mapping is documented in `DISTRIBUTION_GIST_URLS.md` Section "Placeholder → URL mappings."

- [ ] **[Your name] and [Contact information] fields filled** — Search all three template files for these placeholders and replace with your preferred name and contact information before any send.

- [ ] **Batch 1 email accounts accessible** — Confirm you can log in to the email account you will send from. Test by sending yourself a message with one of the filled templates attached (catches merge errors before the real send).

- [ ] **Contact log spreadsheet created** — Copy the template from `execution/tier-1-contact-batches.md` (Contact Log Template section) into a spreadsheet. Fields: Name, Batch, Date Sent, Email Subject, Template Used, Domains Highlighted, Response Received, Response Date, Response Summary, Forwarded/Shared, Follow-up Date, Status.

- [ ] **Response monitoring folder** — Create a folder in your email client named "Phase 1 Responses." Set a filter rule that routes all replies from the contact domains into this folder for daily review.

- [ ] **For Path A+37 only**: Domain 37 Gist created (domains/domain-37-federal-executive-interference-2026-midterms.md) and URL recorded. Add to placeholder-fill sweep above.

- [ ] **For Path B only**: Feedback mechanism set up (Airtable or Google Form with fields: contact name, response date, domain of interest, specific feedback, referral status). Link ready to include in Batch 1 emails.

- [ ] **Domain 42 check** — If Domain 42 Category A send (May 8 original target) has not yet happened, this is same-day priority. Wave 1 Category A emails to Drug Policy Alliance, MPP, NORML, LEAP, SSDP should go out today. May 28 DEA deadline is 15 days away as of May 13. See Section 4 for Domain 42 contacts and templates.

---

## 3. Day-by-Day Execution Timeline

### Day 1: Path Decision → Infrastructure → Batch 1 Send

**Time required**: 2.5–4 hours (depending on path and personalization depth)

**Block 1 — Document Publication verification (30 minutes)**

All 6 canonical Gists were created on April 30, 2026 (Session 678). They are publicly accessible. Do not recreate them. Do:

- Visit each URL in `DISTRIBUTION_GIST_URLS.md` and verify the document renders. This takes 5 minutes.
- If Path A+37: Create the Domain 37 Gist now (this is the only Gist not yet created). Steps are in `execution/domain-42-gist-creation-steps.md` — the process is identical for domain-37.
- Record the Domain 37 Gist URL in `DISTRIBUTION_GIST_URLS.md` under a new row before proceeding.

**Block 2 — Template fill (20 minutes)**

The placeholder fill is the last remaining infrastructure task before any email can be sent. It is a find-replace operation:

1. Open `execution/outreach-email-templates.md`
2. Find-replace all `[link]` instances using the mapping in `DISTRIBUTION_GIST_URLS.md`
3. Replace `[Your name]` and `[Contact information]` in all sign-off blocks
4. Repeat for `distribution-substack-drafts.md` and `distribution-reddit-templates.md`

Do not send emails before this step is complete. A broken link in a first outreach to Ryan Goodman is not recoverable.

**Block 3 — Batch 1 email personalization (60–90 minutes)**

For each of the 5 Batch 1 contacts, open their template and complete the bracketed personalization fields. The specific domain openers and subject lines for each contact are pre-researched and documented in `PHASE_1_EXECUTION_READINESS.md` Block 4. Summary:

- Ryan Goodman (Just Security / NYU Law): Lead with Domain 28 (War Powers) and Domain 29 (Prosecutorial Weaponization, SPLC indictment). Subject: "Domain 28/29 War Powers + DOJ Capture Research — Submission for Just Security." Use Template A. His email: goodman@law.nyu.edu (verify at law.nyu.edu/faculty before sending).
- Wendy Weiser (Brennan Center): Lead with Domain 1 (Voting Rights) and April 2026 four-state SAVE Act analog enactments. Subject: "35-domain democratic reform framework — Brennan Center expertise on Domains 1, 6 needed." Use Template A. Her email: wweiser@brennancenter.org (verify at brennancenter.org/people/wendy-weiser).
- Erica Chenoweth (Harvard Kennedy School): Lead with theory of change and Harvard funding freeze (Domain 27). Subject: "Nonviolent resistance meta-analysis that cites your 3.5% threshold — would value your feedback on the methodology." Use Template A. Her email: echenoweth@hks.harvard.edu (verify at hks.harvard.edu/faculty/erica-chenoweth).
- Ian Bassin (Protect Democracy): Lead with Domain 6 (Judicial Independence) and Domain 29 (Prosecutorial Weaponization, SPLC indictment). Subject: "Full-spectrum democratic accountability research — Domains 2, 6, 29, 34 — would value Protect Democracy's input." Use Template C. His email: bassin@protectdemocracy.org (verify at protectdemocracy.org/team/ian-bassin).
- Marc Elias (Democracy Docket): Lead with Domain 1 litigation tracker and Domain 37 DOJ voter roll cases (23 active). Subject: "DOJ Voter Roll Litigation Documentation (23 Active Cases) + Systematic Election Interference Framework." Use Template B. His email: marc@elias.law (public-facing, verified from multiple sources).

**Block 4 — Batch 1 send sequence (20 minutes)**

Send in this order. Space emails approximately 30 minutes apart within a 3-hour window. Best send window: Tuesday or Wednesday, 9:00–11:00 AM recipient's local time.

1. Ryan Goodman (Just Security) — fastest editorial response cycle; 3–5 day turnaround if interested
2. Wendy Weiser (Brennan Center) — Brennan Center response informs Batch 2 framing
3. Erica Chenoweth (Harvard) — academic credibility; response amplifies to organizer networks
4. Ian Bassin (Protect Democracy) — litigation and implementation focus
5. Marc Elias (Democracy Docket) — media platform and election law practitioner network

Log each send in the contact spreadsheet (date, time, subject, template variant used).

**Domain 42 Wave 1 — run in parallel with Block 4 or immediately after**

If Domain 42 Category A has not been sent, send it today (same priority as Batch 1). The 5 Category A contacts are Drug Policy Alliance, MPP, NORML, LEAP, and SSDP. Templates are in `execution/domain-42-email-template.md`. Contacts are in `execution/domain-42-contact-list.md` Category A table. Submission guide to attach: `execution/domain-42-may-28-dea-submission-guide.md`.

---

### Day 2: Verification and Monitoring Setup

**Time required**: 45 minutes

- Check email account for Batch 1 delivery errors (bounce notifications typically arrive within 2–4 hours of send). If bounce rate exceeds 10%, consult PHASE_1_CONTINGENCY_PLAYBOOK.md Category 2.2 before proceeding.
- Confirm the response monitoring folder is routing replies correctly. Send a test reply to yourself to verify.
- Set up email open tracking if not already active. Free options: Streak CRM (Gmail extension), Mailtrack. Not required — response rate is the primary metric; open rate is secondary.
- Draft Batch 2 emails (8 contacts, Days 8–12). Do not send yet. Batch 2 contacts and sequencing are in `execution/tier-1-contact-batches.md` Section "Batch 2: Institutional Tier." If any Batch 1 contact has already responded (within 24 hours — rare but possible), note the engagement in the contact log and reference it in every Batch 2 email.
- Domain 42: Check for Category A responses. DPA and NORML are most likely to respond quickly. If a Category A contact has responded, reply within 24 hours per the protocol in `execution/domain-42-contact-list.md` Section "Follow-Up and Final Reminder Protocol."

---

### Day 3: Substack and Social Media Staging

**Time required**: 60–90 minutes

Batch 1 emails have been out for 48 hours. Begin staging the social media queue. Do not post publicly yet — the goal is to have posts drafted and ready before any Batch 1 contact responds, so that if a contact shares publicly, there is something for their followers to find.

- **Substack Post 1** (draft, do not publish): The executive summary post from `distribution-substack-drafts.md`. Confirm the proposal Gist link is live in the body. Schedule for T+3 days from Batch 1 send (or T+1 if you want to publish earlier and drive inbound traffic).
- **Reddit posts** (draft, do not post): Four subreddit-tailored posts from `distribution-reddit-templates.md`. Stage for T+2 days. Best subreddits per the research: r/PoliticalScience, r/democracy, r/law, r/ChangeMyView (for the reform framework).
- **X/Bluesky thread** (draft, do not post): 5-tweet opening thread using the executive summary hook. Stage for T+1 day.
- Confirm all social media accounts are active and accessible (can log in, no security holds).

---

### Days 4–7: First Response Window and Wave Monitoring

**Time required**: 15–30 minutes per day

- Check the response folder daily. Log any responses in the contact spreadsheet.
- For any substantive response (request for more information, feedback, offer to share): reply within 24 hours. Log the response quality as: (1) substantive engagement, (2) brief acknowledgment, (3) request for more, or (4) negative/dismissive.
- Do not send Batch 2 before Day 8. The gap between Batch 1 and Batch 2 is intentional — Batch 1 contacts need time to respond and potentially share before Batch 2 contacts are reached.
- **Domain 42 Wave 2**: Send Category B (ACLU, NAACP LDF, Sentencing Project, Prison Policy Initiative) and Category C (Mason Marks, Ohio State DEPC) on Days 5–7 (corresponds to May 15–17 if Day 1 is May 13). Use Templates D42-B and D42-C respectively. Contacts and specific domain section mappings are in `execution/domain-42-contact-list.md` Categories B and C.

---

### Days 8–12: Batch 2 Execution

**Time required**: 2–3 hours total

**Batch 2 contacts** (from `execution/tier-1-contact-batches.md`, 8 contacts):

1. Michael Waldman (Brennan Center President) — Day 8
2. Phil Brest (American Constitution Society) — Day 8
3. Dick Durbin's Senate Judiciary Staff Director — Day 9
4. Sheldon Whitehouse's Legislative Staff — Day 9
5. Jack Balkin (Yale Law, Balkinization) — Day 10
6. Quinta Jurecic (The Atlantic / Lawfare) — Day 10
7. Zack Beauchamp (Vox, Senior Correspondent) — Day 11
8. Janai Nelson (NAACP LDF) — Day 12

**Batch 2 execution protocol**:

- If any Batch 1 contact has responded with substantive engagement by Day 8, open every Batch 2 email with a one-sentence reference: "Since distributing the framework last week, I have engaged with [Brennan Center / Just Security editorial team / Protect Democracy] on the [domain X] analysis..." This transforms cold outreach into warm outreach.
- If no Batch 1 response by Day 8: proceed with Batch 2 on schedule. Non-response in 7 days is normal, not a failure signal. One follow-up to Batch 1 contacts can be sent simultaneously with Batch 2 if it includes a new piece of information (a current event, a new court development) rather than a repeat ask.
- Space Batch 2 sends across Days 8–12. Do not batch all 8 on Day 8.
- **Domain 42 Wave 3**: Send Category D (State AG offices — Colorado, California, Michigan, Washington) on Days 9–12 (May 21–24 if Day 1 is May 13). This gives state AG offices 4–7 business days to route internally before the May 28 deadline. Template D42-D in `execution/domain-42-contact-list.md`.

---

### Days 15–21: Batch 3 Execution

**Time required**: 2–3 hours total

**Batch 3 contacts** (12 contacts, full list in `execution/tier-1-contact-batches.md` Section "Batch 3"):

| Day | Contact | Organization | Primary Domain |
|-----|---------|-------------|----------------|
| 15 | Damon T. Hewitt | Lawyers' Committee | Domains 1, 14, 22 |
| 15 | Amy Klobuchar's Staff Director, Senate Rules | US Senate | Domains 1–3 |
| 16 | Virginia Kase Solomón | Common Cause | Domains 1, 2, 3 |
| 16 | Anthony Romero | ACLU | Domains 7, 8, 9, 16 |
| 17 | Jamie Raskin's Staff, House Judiciary Minority | US House | Domains 29, 6 |
| 17 | Heidi Shierholz | Economic Policy Institute | Domains 17, 5, 20 |
| 18 | Neera Tanden | Center for American Progress | Full proposal |
| 19 | Eric Holder (NDRC) | Nat'l Democratic Redistricting Committee | Domain 2 |
| 19 | Josh Orton | Demand Justice | Domains 6, 35 |
| 20 | Leah Greenberg / Ezra Levin | Indivisible | Resistance meta-analysis, Domain 7 |
| 20 | Joanna Lydgate | States United Democracy Center | Domains 1, 37 |
| 21 | Leslie Graves | FairVote | Domain 1 (RCV) |

By Day 15, reference any Batch 1 and 2 responses in every email. Even a single substantive engagement transforms the remaining Tier 1 outreach from cold to warm. Credibility compounds.

**Day 21 Domain 42 checkpoint**: May 28 deadline is 7 days away from Day 21 (if Day 1 = May 13). Send the final abbreviated Domain 42 reminder on this date to all Category A–D contacts that have not responded. Subject: "One week to DEA hearing participation deadline (May 28) — Domain 42 briefing still available." Do not send any new Domain 42 outreach after May 21.

---

## 4. Batch 1 Quick Reference

### Main Tier 1 Batch 1 — Five Bridge-Node Contacts

These contacts are the credibility foundation for the entire Phase 1 distribution. Position-verified as of April 29, 2026.

| Contact | Organization | Title | Domain Focus | Verified Email | Template |
|---------|-------------|-------|-------------|----------------|----------|
| Ryan Goodman | Just Security / NYU Law | Co-Editor-in-Chief / Law Professor | Domains 28, 29 | goodman@law.nyu.edu (verify) | Template A — Methodological Peer |
| Wendy Weiser | Brennan Center for Justice | VP, Democracy Program | Domains 1, 6 | wweiser@brennancenter.org (verify) | Template A — Citation and Use |
| Erica Chenoweth | Harvard Kennedy School | Frank Stanton Professor; Director, Nonviolent Action Lab | Resistance meta-analysis, Domain 7 | echenoweth@hks.harvard.edu (verify) | Template A — Methodological Peer |
| Ian Bassin | Protect Democracy | Executive Director / Co-Founder | Domains 2, 6, 29, 34 | bassin@protectdemocracy.org (verify) | Template C — Legal/Institutional |
| Marc Elias | Democracy Docket / Elias Law Group | Founder / Partner | Domains 1, 33, 37 | marc@elias.law | Template B — Media/Journalist |

**Email verification step** (2 minutes per contact, must do before send):
- Goodman: law.nyu.edu/faculty — confirm current email format
- Weiser: brennancenter.org/people/wendy-weiser — confirm email
- Chenoweth: hks.harvard.edu/faculty/erica-chenoweth — confirm email
- Bassin: protectdemocracy.org/team/ian-bassin — confirm email
- Elias: democracydocket.com/about — confirm email (marc@elias.law is publicly confirmed)

---

### Domain 42 Sub-Batch — Wave 1 (Category A, Same-Day Priority)

These 5 contacts are the drug policy organizations most likely to file DEA hearing participation notices before the May 28 cutoff. This sub-batch is separate from the main Tier 1 sequence — different audiences, different templates, different ask.

| Contact | Organization | Email | Domain 42 Section Hook | Specific Ask |
|---------|-------------|-------|----------------------|-------------|
| Press/Policy staff | Drug Policy Alliance | press@drugpolicy.org | Section 2 (DEA regulatory capture) + Section 6.1 (APA procedural reform) | File participation notice for June 29 hearing |
| Policy team | Marijuana Policy Project | mpp@mpp.org | Section 4 (SAFER Banking, 280E) + Section 6.3 (federal-state reconciliation) | Forward to MPP federal policy director; note May 28 deadline |
| Communications/Legal | NORML | norml@norml.org | Section 2.3 (DEA statutory capture, Mason Marks Yale LJ cite) | File participation notice |
| Executive Director | Law Enforcement Action Partnership | info@leap.cc | Section 2.4 (four scenario framework) + Section 3 (felony disenfranchisement) | Forward to policy team |
| Executive Director | Students for Sensible Drug Policy | ssdp@ssdp.org | Section 3 (felony disenfranchisement — student population) | Brief advocacy staff on participation mechanics |

**Companion documents to attach/reference**:
- Research: domains/domain-42-drug-policy-democratic-legitimacy-regulatory-capture.md (Gist URL — create if not yet created)
- Submission guide: execution/domain-42-may-28-dea-submission-guide.md
- Template: execution/domain-42-email-template.md (Template D42-A for Category A)

**DEA submission details** (include in all Domain 42 outreach):
- Docket No.: DEA-1362
- Participation notice deadline: May 28, 2026
- Submit to: nprm@dea.gov or mail to DEA Attn: Administrator, 8701 Morrissette Drive, Springfield, VA 22152
- Hearing dates: June 29 – July 15, 2026 (recess July 3–5)
- Hearing location: DEA Hearing Facility, 700 Army Navy Drive, Arlington, VA 22202

---

## 5. Template Quick Reference

All templates are in `execution/outreach-email-templates.md`. Nine templates across three types. Pre-send checklist is in the templates file header — do not skip it.

### Which Template for Which Contact

| Template Type | Best For | Core Framing |
|--------------|----------|-------------|
| **A — Academic/Think Tank** | Goodman, Chenoweth, Weiser, Balkin, Waldman, Shierholz, Fung, Issacharoff, Allen, Levitsky | Present as peer-level scholarly work; ask for feedback not endorsement; lead with a specific methodological question they have an opinion on |
| **B — Media/Journalist** | Elias (Democracy Docket platform), Jurecic (The Atlantic), Beauchamp (Vox), Bouie (NYT), Richardson (Substack) | Lead with newsworthiness; frame as primary documentation resource; emphasize current events hook and data exclusivity |
| **C — Legal/Institutional** | Bassin (Protect Democracy), Brest (ACS), Hewitt (Lawyers' Committee), Nelson (NAACP LDF), Romero (ACLU), legislative staff | Frame as institutional reform analysis with legal pathways; not political advocacy; cite litigation-relevant analysis directly |

### Fields That Must Be Filled per Send

**Universal (every email)**:
- `[First name]` — always use first name; never "Dear Dr." in first contact
- `[Their specific paper / testimony / article]` — cite something they published or said recently
- `[specific topic]` / `[their topic]` — the connection between their work and the framework
- `[Domain X]` — the 1–2 domains most directly relevant to their current work
- `[specific question]` — the one methodological question you are asking them to weigh in on
- `[link]` — all `[link]` placeholders replaced before send
- `[Your name]` / `[Contact information]` — your sign-off

**Domain-specific email openers** (pre-selected per contact in PHASE_1_EXECUTION_READINESS.md Block 4):
- Goodman: Venezuela Operation Absolute Resolve legal analysis + 22-case retaliatory prosecution pattern
- Weiser: Four-state SAVE Act analog enactments (FL, MS, SD, UT) + Brennan Center litigation reference
- Chenoweth: Harvard funding freeze (Domain 27) + 3.5% threshold extrapolation question
- Bassin: SPLC indictment (April 21, 2026) as primary case study in Domain 29
- Elias: 23 active DOJ voter roll litigation cases in Domain 37

### Fields That Are Timing-Dependent

These fields reference current events and should be verified are still current at time of send (all were accurate as of April 29):
- FISA Section 702 passage (House 235–191, Senate cloture set) — check current status if sending more than 2 weeks after April 29
- SAVE Act Senate defeat (48–50, four GOP defectors: Collins, Murkowski, Tillis, McConnell) — durable fact, no expiration
- SPLC indictment (April 21, 2026) and April 28 motions — durable facts; check for new developments
- Harvard $2.2B funding freeze (Domain 27) — check for resolution before using as hook with Chenoweth
- Hungary April 2026 election outcome (53.6% opposition win) — durable comparative fact

---

## 6. Contingency Playbook

The full contingency playbook with decision trees and recovery procedures is in `PHASE_1_CONTINGENCY_PLAYBOOK.md`. This section is the field-expedient summary for the most common scenarios.

### If an Email Bounces

**1–5 bounces out of 25 (normal)**: This is expected staff turnover. Re-verify the email address against the organization's current staff page. Resend to the corrected address. Do not resend to the same invalid address.

**6–15 bounces (elevated)**: Before Batch 2 sends, sample 10 contacts from the bounce list, verify their current roles online. If over half have moved institutions, update the contact list before proceeding.

**Over 15 bounces (list corruption)**: Stop Batch 2. Diagnose whether the bounce pattern is concentrated in one domain (e.g., all .edu addresses bouncing — likely ISP rate-limiting, wait 48 hours and resend at 20 emails/hour) or scattered (list quality issue — manual review required). Full procedure in PHASE_1_CONTINGENCY_PLAYBOOK.md Section 1.1.

### If a Contact Does Not Respond

**Within 7 days**: Expected. Do not follow up yet.

**After 7 days**: Send one follow-up with a new piece of information — a court development in one of the documented cases, a new domain update, a relevant current event. Never send a repeat of the initial ask. Subject line: "Following up — [new development] relevant to [Domain X]."

**After follow-up, no response**: Move on. Non-response is not rejection — senior academics and policy directors receive dozens of pitches per week. Contact log status: "closed — move to Tier 2 wave." They may engage later when a colleague mentions the framework.

### If Discord Notification Is Needed

Press inquiries, substantive partnership requests, or any request requiring a decision from you should trigger a Discord notification. Log the engagement in the contact spreadsheet and flag the message thread. The response timeline for press is 2 hours; for partnership requests, 24 hours (full protocol in PHASE_1_CONTINGENCY_PLAYBOOK.md Section 3.2 and 3.3).

### Domain 42 — If No Category A Response by May 17

Send one follow-up to high-priority Category A contacts (Drug Policy Alliance, NORML) with the subject: "[Organization name] — following up, May 28 deadline is [X days away]." Hard stop on all new Domain 42 outreach after May 21 — organizations receiving it after May 21 will not have time to file a participation notice. Post-deadline, shift Domain 42 distribution to law school clinics and Substack audience (democratic design analysis, not DEA hearing context).

### If Template Merge Fields Are Broken

If you discover an email went out with unfilled placeholders (e.g., "Dear [First name]"): send a brief follow-up within 2 hours: "Please disregard the previous email — a formatting error meant the message was incomplete. The corrected version is below." Then resend the corrected template. This is recoverable. The research quality itself is not affected by a merge error.

### If Batch 1 Response Rate is Below 20% at Day 14

Do not launch Batch 2 on the same messaging. Review the three most personalized emails and the three least personalized. Compare subject lines, opening hooks, and whether the domain selection matched each contact's known work. The most common causes of underperformance are: wrong domain for the contact, opening paragraph too long, ask too vague. Try one deeply personalized email to a new contact as a test before adjusting Batch 2. Full diagnostic in `execution/success-metrics.md` Section "Diagnostic Protocol."

---

## 7. Success Metrics

The full metrics framework with 30-day and 90-day checkpoints, diagnostic protocols, and Phase 2 decision criteria is in `execution/success-metrics.md`. This section is the at-a-glance reference.

### Batch-Level Targets

| Batch | Contacts | Response Target | Minimum Acceptable | Forward/Share Target |
|-------|----------|----------------|-------------------|---------------------|
| Batch 1 | 5 | 2 of 5 (40%) | 1 of 5 (20%) | 1 of 5 (20%) |
| Batch 2 | 8 | 3 of 8 (38%) | 2 of 8 (25%) | 1 of 8 (13%) |
| Batch 3 | 12 | 4 of 12 (33%) | 3 of 12 (25%) | 1 of 12 (8%) |
| **Tier 1 Total** | **25** | **9 of 25 (36%)** | **6 of 25 (24%)** | **3 of 25 (12%)** |

**Response quality matters more than response count**: A single Wendy Weiser response that leads to a Senate Judiciary staff introduction is worth more than 10 brief acknowledgments. Track quality in the contact log (categories: substantive engagement / brief acknowledgment / more information request / negative).

### 30-Day Gate Checkpoints

**Gate 1 — Tier 1 Response Rate**: Target 30%+ (8+ of 25 respond substantively). If met: proceed to full Tier 2 launch without modification. If 20–29%: review messaging and personalization before Tier 2. If below 20%: hold Tier 2 and run the diagnostic protocol.

**Gate 2 — Network Propagation**: At least 1 Tier 1 contact has shared the research with a named colleague at a different institution. If not met by Day 30: add an explicit "would you share this with a colleague" request to all subsequent outreach.

**Gate 3 — External Mention**: At least 1 mention of the framework from someone not in the outreach list (blog, newsletter, social media). If not met by Day 30: increase social media posting frequency; consider submitting a short piece to Just Security, Lawfare, or The Hill.

### Next-Batch Timing Decision Criteria

**Send Batch 2 on schedule (Day 8)**: If Batch 1 delivery succeeded (less than 10% bounce) and no systemic issues.

**Delay Batch 2** by 3–5 days: If Batch 1 bounce rate was 10–20% (need to diagnose list quality before reaching more contacts with the same infrastructure issue).

**Hold Batch 2 and diagnose**: If Batch 1 bounce rate exceeded 20% or if 0 of 5 Batch 1 contacts have opened in 5 days (open tracking available) — messaging or delivery problem must be resolved before scaling.

**Begin Tier 2 planning (Weeks 4–8 contacts)**: After Tier 1 complete. Gate condition: at least 1 Tier 1 contact has forwarded or cited the research to a named individual. This is the minimum credibility threshold for moving into the broader Tier 2 academic and media contacts.

### Domain 42 Success Criteria

**Primary**: At least 1 Category A or B organization files a DEA hearing participation notice by May 28 and attributes Domain 42 as part of their research basis.

**Secondary**: At least 2 Category A contacts reply with substantive engagement (not just confirmation of receipt).

**Log location**: WORKLOG.md under a Domain 42 sub-batch section. If any organization files a participation notice citing Domain 42, document it in WORKLOG.md as a Phase 1 success metric — it is the concrete, time-bounded impact case for this research thread.

---

## File Reference Summary

| Need | File Location |
|------|--------------|
| Gist URLs for template fill | `DISTRIBUTION_GIST_URLS.md` |
| Email templates (9, across 3 types) | `execution/outreach-email-templates.md` |
| Batch 1 contact details and personalization | `execution/tier-1-contact-batches.md` Sections B1-1 through B1-5 |
| Batch 2 contact details | `execution/tier-1-contact-batches.md` Sections B2-1 through B2-8 |
| Batch 3 contact details | `execution/tier-1-contact-batches.md` Section Batch 3 |
| Domain 42 contacts and wave sequencing | `execution/domain-42-contact-list.md` |
| Domain 42 email templates | `execution/domain-42-email-template.md` |
| Domain 42 DEA submission guide | `execution/domain-42-may-28-dea-submission-guide.md` |
| Full contact database (150+ contacts) | `policy-influencer-mapping.md` |
| Personalization depth guide | `EMAIL_PERSONALIZATION_GUIDE.md` |
| Full contingency playbook | `PHASE_1_CONTINGENCY_PLAYBOOK.md` |
| Success metrics and diagnostic protocol | `execution/success-metrics.md` |
| Path A materials | `execution/path-a-materials.md` |
| Path A+37 materials | `execution/path-a-domain37-materials.md` |
| Path B materials | `execution/path-b-materials.md` |
| Final readiness audit | `PHASE_1_EXECUTION_READINESS.md` |

---

*Blueprint created: May 13, 2026 (Item 28, Exploration Queue). All materials consolidated from existing production-ready files — no new research conducted. Phase 1 infrastructure is complete and execution-ready pending path decision.*
