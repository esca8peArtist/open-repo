---
title: "Contact Verification Checklist — Batch 1 (Five Contacts)"
created: 2026-05-01
session: 716
status: READY TO RUN — execute immediately before Block 6 (send)
purpose: "Step-by-step email format validation and contact routing verification for all five Batch 1 contacts. Position-verified April 29. This checklist handles only the final email spot-check required before send."
estimated_time: "15-25 minutes total (2-5 minutes per contact)"
prerequisite: "Gist URLs confirmed (Section 1.1 of PHASE_1_EXECUTION_INFRASTRUCTURE.md) and identity fields filled ({{YOUR_NAME}}, {{YOUR_CONTACT_INFO}})"
---

# Contact Verification Checklist — Batch 1

**When to run this checklist**: Immediately before Block 6 (send). Do not run earlier — position and email currencies can change. Do not skip — an email to a stale address or a contact who has moved positions creates a negative first impression that cannot be undone.

**What this checklist verifies**: (1) email address is current and formatted correctly, (2) organization name is current, (3) the correct contact routing for that organization is confirmed. It does not re-verify position — all five positions were confirmed April 29, 2026 and are stable.

**How to record results**: Fill the `verified_email` field in `PHASE_1_CONTACT_VERIFICATION.json` for each contact after completing their verification sub-checklist. Log the date of verification. Do not send until all five `verified_email` fields are filled.

---

## Contact 1: Ryan Goodman — Just Security / NYU School of Law

**Send order**: 1st
**Primary email pattern**: ryan.goodman@nyu.edu
**Alternate email**: ryan@justsecurity.org

### Verification steps

- [ ] Visit https://www.law.nyu.edu/faculty/profiles/GOODMANR
  - Confirm page loads and Ryan Goodman is listed as faculty
  - Confirm he is still listed as Anne and Joel Ehrenkranz Professor of Law
  - Check for any email address listed on the page. If an email is listed, use that. If none, proceed to next step.

- [ ] Visit https://justsecurity.org/about-us/ or https://justsecurity.org/author/ryan-goodman/
  - Confirm Ryan Goodman is still listed as Co-Editor-in-Chief
  - Check whether a contact email is listed for editorial submissions
  - Note: if the page shows any recent articles by Goodman, use the most recent for the `{{RECENT_JUST_SECURITY_ARTICLE}}` placeholder

- [ ] Confirm email format:
  - NYU School of Law format: first.last@nyu.edu
  - Apply: ryan.goodman@nyu.edu
  - Common error: some NYU faculty use first_initial + last@nyu.edu — if in doubt, check the faculty page for any email link

- [ ] Record in `PHASE_1_CONTACT_VERIFICATION.json`:
  - `verified_email`: ryan.goodman@nyu.edu (or corrected address if found)
  - `verification_date`: today's date
  - `verification_source`: the specific URL you visited to confirm

**Organization name confirmation**: "Just Security" and "NYU School of Law" — both correct as of April 29. No change expected, but if the faculty page shows a different primary affiliation (e.g., a new institutional appointment), update the email signature block in the email before sending.

**Contact routing note**: For this send, route to the NYU Law address (primary) rather than the Just Security editorial address. The NYU Law address signals you are contacting him in his academic capacity for feedback, not submitting to Just Security as an outlet. If you want to pitch a Just Security publication specifically, use ryan@justsecurity.org and note the explicit pitch in your subject line.

**If email bounces**: Try ryan@justsecurity.org. If both bounce, use the Just Security contact form at justsecurity.org/contact and note in the body that you have tried Goodman's email addresses.

---

## Contact 2: Wendy Weiser — Brennan Center for Justice

**Send order**: 2nd
**Primary email pattern**: wweiser@brennancenter.org
**Alternate email**: No confirmed alternate; use brennancenter.org/contact if primary bounces

### Verification steps

- [ ] Visit https://www.brennancenter.org/experts/wendy-r-weiser
  - Confirm page loads and Wendy Weiser is listed as VP, Democracy Program
  - Check for any email address or contact link on the page
  - Note any recent publications for the `{{RECENT_BRENNAN_CENTER_PUBLICATION}}` placeholder

- [ ] Confirm email format:
  - Brennan Center format: first-initial + last@brennancenter.org
  - Apply: wweiser@brennancenter.org
  - The "w" initial maps to "Wendy" — confirmed institutional pattern

- [ ] Visit https://www.brennancenter.org/our-work (optional, if time permits)
  - Identify the most recent Brennan Center voting rights or democracy publication
  - Use this for the `{{RECENT_BRENNAN_CENTER_PUBLICATION}}` placeholder in the email

- [ ] Record in `PHASE_1_CONTACT_VERIFICATION.json`:
  - `verified_email`: wweiser@brennancenter.org (or corrected address)
  - `verification_date`: today's date
  - `verification_source`: specific URL visited

**Organization name confirmation**: "Brennan Center for Justice at NYU School of Law" (full formal name) or "Brennan Center for Justice" (shorter version used in emails). Both are correct. Use the shorter version in the email body.

**Contact routing note**: The Brennan Center Democracy Program is the appropriate routing for this contact. Weiser leads the program directly — routing to her rather than through a general Brennan Center contact form is correct for this level of outreach.

**If email bounces**: Use the Brennan Center contact form at brennancenter.org/contact. Note that you are attempting to reach Wendy Weiser specifically in your contact form message.

---

## Contact 3: Erica Chenoweth — Harvard Kennedy School

**Send order**: 3rd
**Primary email pattern**: echenoweth@hks.harvard.edu
**Alternate email**: echenoweth@harvard.edu

### Verification steps

- [ ] Visit https://www.hks.harvard.edu/faculty/erica-chenoweth
  - Confirm page loads and Erica Chenoweth is listed as Frank Stanton Professor of the Practice of Public Leadership
  - Confirm she is still listed as Director, Nonviolent Action Lab
  - Check for any email address or contact link on the page
  - Note: the Harvard $2.2B funding freeze (April 2026, documented in Domain 27) has not affected faculty status — this is the correct institutional address

- [ ] Check for recent publications (optional):
  - Visit https://scholar.harvard.edu/ericheno for recent work
  - Default pre-fill for `{{RECENT_CHENOWETH_WORK}}` is "Why Gen-Z Is Rising, Journal of Democracy, January 2026"
  - If there is a newer publication (February-May 2026), use that instead

- [ ] Confirm email format:
  - HKS faculty format: first-initial + last@hks.harvard.edu
  - Apply: echenoweth@hks.harvard.edu
  - Common alternate: first-initial + last@harvard.edu — both work for HKS faculty

- [ ] Record in `PHASE_1_CONTACT_VERIFICATION.json`:
  - `verified_email`: echenoweth@hks.harvard.edu (or corrected address)
  - `verification_date`: today's date
  - `verification_source`: specific URL visited

**Organization name confirmation**: "Harvard Kennedy School" is the correct short form. Full name: "Harvard Kennedy School of Government." Use "Harvard Kennedy School" in email body; "Harvard Kennedy School (HKS)" is also acceptable.

**Contact routing note**: Route to the HKS address, not the Nonviolent Action Lab's general contact. Chenoweth is the appropriate direct contact for this level of outreach — she is the researcher whose work is cited throughout the framework, and the email is explicitly structured as a direct academic-to-researcher contact, not an institutional inquiry.

**Important context for email**: The Harvard $2.2B funding freeze (April 2026) is a live issue for Chenoweth's institution. Domain 27 documents this in detail. The email template uses this as a personalization hook — "your institution's own funding freeze is documented in Domain 27." This is accurate and relevant. Do not omit this hook; it is the strongest personalization element for this contact.

**If email bounces**: Try echenoweth@harvard.edu. If both bounce, use HKS faculty contact form at hks.harvard.edu.

---

## Contact 4: Ian Bassin — Protect Democracy

**Send order**: 4th
**Primary email pattern**: ian@protectdemocracy.org
**Alternate email**: Protect Democracy contact form at protectdemocracy.org/contact

### Verification steps

- [ ] Visit https://protectdemocracy.org/about/team/
  - Confirm page loads and Ian Bassin is listed as Co-Founder and Executive Director
  - Check for any email address or contact link associated with Bassin on this page
  - Note any recent case or publication for the `{{RECENT_PROTECT_DEMOCRACY_FILING}}` placeholder

- [ ] Visit https://protectdemocracy.org/work/ (optional, if time permits)
  - Identify the most recent Protect Democracy case filing or publication
  - Use this for the `{{RECENT_PROTECT_DEMOCRACY_FILING}}` placeholder
  - Priority: look for cases related to Domain 6 (judicial independence) or Domain 29 (prosecutorial weaponization), as these are the domain hooks for this email

- [ ] Confirm email format:
  - Protect Democracy format: first@protectdemocracy.org (for executive directors and co-founders)
  - Apply: ian@protectdemocracy.org
  - This is confirmed by cross-reference with the co-founder naming convention at the organization

- [ ] Record in `PHASE_1_CONTACT_VERIFICATION.json`:
  - `verified_email`: ian@protectdemocracy.org (or corrected address)
  - `verification_date`: today's date
  - `verification_source`: specific URL visited

- [ ] Fill the `{{YOUR_AVAILABILITY}}` placeholder in this email's meeting request block:
  - This is the only Batch 1 email that asks for a meeting rather than feedback
  - Provide 2-3 specific time windows over the next 2 weeks (e.g., "Tuesday May 5, 2:00-4:00 PM ET; Thursday May 7, 10:00 AM-12:00 PM ET; Monday May 11, 3:00-5:00 PM ET")
  - Calendly link is also acceptable in place of specific windows

**Organization name confirmation**: "Protect Democracy" — no "The" at the front. Full legal name may differ; for email purposes "Protect Democracy" is correct.

**Contact routing note**: Route to Bassin directly. Do not use the Protect Democracy general contact form for the initial send — the email is personalized to Bassin's specific litigation work (Domains 6 and 29) and would lose its personalization value if routed through a general inbox.

**Domain 37 note (Path A+37 only)**: The Bassin email in Path A+37 includes a reference to Protect Democracy's Common Cause national voter database lawsuit (documented in Domain 37). This reference is accurate — Protect Democracy is co-plaintiff in this case. Include the priming paragraph from the Path A+37 email template to signal that Domain 37 will reach him in a Phase 1b targeted send.

**If email bounces**: Use the Protect Democracy contact form at protectdemocracy.org/contact, noting that you are attempting to reach Ian Bassin specifically. Reference the specific domains (6 and 29) to route correctly within the organization.

---

## Contact 5: Marc Elias — Democracy Docket / Perkins Coie

**Send order**: 5th
**Primary email pattern**: melias@perkinscoie.com
**Alternate email**: marc@democracydocket.com

### Verification steps

- [ ] Visit https://www.perkinscoie.com/people/marc-e-elias
  - Confirm page loads and Marc Elias is listed as Partner and Chair, Election & Democracy Practice
  - Check for any email address on the page
  - Note: Elias is very active on X (@marceelias) — his firm page is the more stable source

- [ ] Visit https://www.democracydocket.com/about/ (supplemental)
  - Confirm Democracy Docket is still active and Elias is listed as founder
  - Note any recent case filings that connect to Watson v. RNC or Louisiana v. Callais (the key personalization hooks in this email)

- [ ] Visit https://www.democracydocket.com/ and search for Watson v. RNC and Louisiana v. Callais:
  - These are the two specific cases referenced in the email template
  - Confirm current case status — the email references "both expected June-July 2026" as decision timing
  - If either case has been decided, updated, or otherwise changed since April 29, update the email reference accordingly before sending

- [ ] Confirm email format:
  - Perkins Coie format: first-initial + last@perkinscoie.com
  - Apply: melias@perkinscoie.com
  - Standard law firm format — confirmed

- [ ] Record in `PHASE_1_CONTACT_VERIFICATION.json`:
  - `verified_email`: melias@perkinscoie.com (or corrected address)
  - `verification_date`: today's date
  - `verification_source`: specific URL visited
  - `case_status_check`: note current status of Watson v. RNC and Louisiana v. Callais

**Organization name confirmation**: Use "Democracy Docket" as the primary institution name in email body, since that is the context of the research relationship (the litigation tracker cites Democracy Docket extensively). Reference Perkins Coie in the email address explanation only if needed.

**Contact routing note**: Route to the Perkins Coie address (melias@perkinscoie.com) as the primary professional address. The Democracy Docket address (marc@democracydocket.com) is appropriate for editorial or research pitches to Democracy Docket specifically. Since this email engages both Elias's litigation work (Perkins Coie) and the Democracy Docket publication, the firm address is appropriate as primary.

**Domain 37 note (Path A+37 only)**: The Path A+37 version of this email notes that Democracy Docket is cited 12+ times in Domain 37 as the primary NVRA quiet period enforcement vehicle, and that Elias will receive Domain 37 directly in Phase 1b. The subject line modification for the Phase 1b (Domain 37) send to Elias is: "Domain 37: 23 active DOJ voter roll cases + NVRA quiet period (Aug 7) — research for Democracy Docket."

**If email bounces**: Try marc@democracydocket.com. If both bounce, route through the Democracy Docket contact form or @marceelias on X with a brief note that you've attempted his email addresses.

---

## Verification Log Summary

After completing all five sub-checklists, confirm this log is filled before proceeding to Block 6 (send):

| Contact | Verified Email | Verification Date | Organization Confirmed | Notes |
|---------|---------------|------------------|----------------------|-------|
| Ryan Goodman | | | | |
| Wendy Weiser | | | | |
| Erica Chenoweth | | | | |
| Ian Bassin | | | | |
| Marc Elias | | | | |

Transfer these values to `PHASE_1_CONTACT_VERIFICATION.json` (`verified_email` field for each contact).

---

## Pre-Send Confirmation Checklist

Before sending Email 1 (Goodman), confirm all items:

- [ ] All 5 verified emails filled in `PHASE_1_CONTACT_VERIFICATION.json`
- [ ] All URL placeholders replaced in all 4 template files (see Section 2.1 of `PHASE_1_EXECUTION_INFRASTRUCTURE.md`)
- [ ] `{{YOUR_NAME}}` filled in all 5 email sign-offs
- [ ] `{{YOUR_CONTACT_INFO}}` filled in all 5 email sign-offs
- [ ] `{{YOUR_AVAILABILITY}}` filled in Bassin email (meeting time windows)
- [ ] Path-specific paragraph block selected (delete 2, keep 1) in each email
- [ ] Subject line variant selected (one per contact; do not use all three variants)
- [ ] Gist URLs confirmed working (visit each URL in browser before send)
- [ ] Email client is not a bulk sender / marketing tool (use standard email client for Batch 1)
- [ ] Send window is Tuesday-Thursday, 8:00-11:00 AM ET (optimal for institutional contacts)

**After confirming all items: proceed to Block 6 — send Email 1 (Goodman).**

---

## Email Scheduling Log

Fill this log as sends are completed:

| Email | Contact | Sent at (local time + timezone) | Email address used | Confirmed delivered |
|-------|---------|--------------------------------|-------------------|---------------------|
| 1 | Ryan Goodman | | | |
| 2 | Wendy Weiser | | | |
| 3 | Erica Chenoweth | | | |
| 4 | Ian Bassin | | | |
| 5 | Marc Elias | | | |

Also fill the corresponding fields in `PHASE_1_CONTACT_VERIFICATION.json` (`date_sent`, `time_sent_utc`, `email_address_used`) for each contact after sending.

---

## Post-Send Protocol

After sending all 5 Batch 1 emails:

1. Set a T+7 calendar reminder titled "Batch 1 Response Assessment — [date of first send + 7 days]"
2. Set a T+14 calendar reminder titled "Batch 1 Open Rate Check"
3. Prepare Batch 2 by reviewing `execution/phase-1-personalized-batch-2.md` — no further contact verification is required before Batch 2 preparation begins, only before Batch 2 send
4. Do not follow up on any Batch 1 contact before T+7 days
5. If a response arrives before T+7, log it immediately in `PHASE_1_CONTACT_VERIFICATION.json` and flag for priority engagement

**Response handling priority**:
- Goodman response: Route as potential Just Security publication — check with the contact about publication interest before committing to anything
- Weiser response: Flag as potential Brennan Center integration opportunity — this is the highest-value Tier 1 cascade node
- Chenoweth response: The single highest-priority Tier 2 bridge node; treat every response from Chenoweth as a priority regardless of its nature
- Bassin response: Route as potential meeting confirmation — the email asks for 20 minutes; a positive reply likely includes a scheduling link or time preference
- Elias response: Route as potential Democracy Docket collaboration or litigation tracker input — check whether his response indicates Democracy Docket will use the research

---

*Checklist created: May 1, 2026 (Session 716). Companion documents: `PHASE_1_CONTACT_VERIFICATION.json`, `PHASE_1_EXECUTION_INFRASTRUCTURE.md`, `PHASE_1_EMAIL_TEMPLATES.md`, `BATCH_1_CONTACT_VERIFICATION.md`.*
