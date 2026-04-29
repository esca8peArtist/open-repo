---
title: "Tier 1 Execution Runbook"
project: cybersecurity-hardening
created: 2026-04-28
status: ready
cross-references:
  - TIER1_DISTRIBUTION_PREP.md
  - TIER1_OUTREACH_PREPARED.md
  - TIER1_OUTREACH_EXECUTION_PLAN.md
  - DISTRIBUTION_CHECKLIST.md
  - TIER1_SUCCESS_METRICS.md
  - TIER1_CONTACT_VALIDATION.md
---

# Tier 1 Execution Runbook

**Scope**: Step-by-step execution of Tier 1 outreach — 14 direct contacts across immigration legal aid (1A), community-based organizations (1B), and mutual aid networks (1C).

**Execution window**: 7 days from approval to first-wave completion, with a follow-up loop extending to Day 21.

**Prerequisite**: User has approved email templates in `TIER1_OUTREACH_PREPARED.md`. Do not begin sending until approval is confirmed.

**Gist URL (canonical)**: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108

---

## Pre-Execution Checklist

Complete every item before sending any emails. Estimated time: 45–60 minutes.

### Gist Accessibility

- [ ] Open https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108 in a **private/incognito browser window** (not logged into GitHub). Confirm it loads without a login wall.
- [ ] Verify all three core documents are present: `threat-model.md`, `opsec-playbook.md`, `implementation-guide.md`.
- [ ] Confirm Part 0 (data broker opt-outs) is intact and the California DROP platform path is documented.
- [ ] If the Gist requires login: change visibility to Public in GitHub settings before proceeding.

### URL Tracking Setup

- [ ] Go to bitly.com and create a free account with a non-primary email address.
- [ ] Shorten the Gist URL to a custom back-half (e.g., `bit.ly/opsec-corpus`).
- [ ] Confirm the short URL redirects correctly in a private browser window.
- [ ] Note the short URL in your tracking spreadsheet. Use the short URL in all emails for click analytics.

### Email Infrastructure

- [ ] In Gmail, create the following nested labels under a parent label `Tier1-Outreach`:
  - `Tier1-Outreach/Sent`
  - `Tier1-Outreach/Response-Engagement`
  - `Tier1-Outreach/Response-Acknowledgment`
  - `Tier1-Outreach/Response-Declination`
  - `Tier1-Outreach/OOO`
  - `Tier1-Outreach/Bounce`
  - `Tier1-Outreach/Follow-Up-Pending`
- [ ] Enable Gmail Templates (Settings → Advanced → Enable Templates).
- [ ] Save all five response templates from `TIER1_OUTREACH_EXECUTION_PLAN.md` Section 1.4 as named drafts: `R1-Engagement`, `R2-Acknowledgment-Followup`, `R3-Declination`.

### Tracking Spreadsheet

- [ ] Create a Google Sheet titled "Tier 1 Outreach Tracker — [today's date]".
- [ ] Add these columns: Organization | Category (1A/1B/1C) | Contact Name | Contact Email/Method | Template Used | Date Sent | Time Sent | Bitly Click (Y/N) | Response Received (Y/N) | Response Date | Response Type | Follow-Up Sent | Follow-Up Date | Notes
- [ ] Pre-populate rows for all 14 named contacts from `TIER1_CONTACT_VALIDATION.md`.

### Email Deliverability Check

- [ ] Send a test email to yourself from the outreach email address. Verify it arrives and is not flagged as spam.
- [ ] Optional: Check deliverability score at mail-tester.com (aim for 8/10 or above).
- [ ] Confirm your "from" address is the one you want permanently associated with this outreach.

### Final Pre-Send Verification Per Email

Before each individual send:

- [ ] Gist URL or Bitly short URL is correct in the email body.
- [ ] Your name has replaced every `[Your name]` placeholder.
- [ ] Opening 2–3 sentences are personalized to this specific organization.
- [ ] Correct template used (1A for legal orgs, 1B for community orgs, 1C for mutual aid).
- [ ] BCC yourself on the email.

---

## Week 1: Days 1–5

**Target**: 5 Tier 1A legal aid organizations (named contacts with verified emails). Send 5/day maximum, 7:00–9:00 AM local time. Allow a 3–5 minute gap between each send.

### Day 1 — Named Tier 1A Organizations (5 sends)

These five organizations have fully verified contact information in `TIER1_OUTREACH_PREPARED.md`. Use the personalized email drafts from that document.

| Organization | Send To | Method |
|-------------|---------|--------|
| National Immigration Law Center (NILC) | info@nilc.org + web form at nilc.org/about-us/contact-us/ | Dual (email + form) |
| CLINIC — Catholic Legal Immigration Network | national@cliniclegal.org | Email |
| RAICES (Texas) | communications@raicestexas.org | Email |
| Immigrant Legal Resource Center (ILRC) | kbello@ilrc.org (Kemi Bello, Communications Mgr) | Email |
| National Lawyers Guild (NLG) | massdef@nlg.org | Email |

**Day 1 post-send actions**:
1. Update tracking spreadsheet with send times.
2. Apply `Tier1-Outreach/Sent` label to BCC copies.
3. Set calendar reminder: Day 8 = NILC follow-up date (if no response).
4. Set calendar reminder: Day 8 = CLINIC follow-up date.
5. Set calendar reminder: Day 8 = RAICES follow-up date.

### Days 2–5 — Regional and Extended 1A Contacts

For each day, research and send 5 regional immigration legal aid organizations using this research pattern:

Search: `[state/city] immigration legal aid nonprofit`
Search: `[state] law school immigration clinic`
Search: `[state] public defender immigration unit`

Before each Day N send session:
- Research contacts the evening before (Sunday batch research saves morning time — see `TIER1_OUTREACH_EXECUTION_PLAN.md` Section 3.4).
- Write 2–3 sentence personalization notes into the tracking spreadsheet.
- Morning: open spreadsheet, compose, send.

---

## Week 1 Daily Checkpoint

At the end of each send day, answer:

1. **How many emails sent today?** (Target: 5)
2. **Any immediate bounces or OOO responses?** Log them immediately.
3. **Any responses received?** Classify and apply Gmail label.
4. **Bitly clicks?** Check dashboard. Any activity indicates email was opened.

---

## Week 2: Days 8–12

**Target**: Tier 1B community-based organizations + continued 1A regional sends. Shift template from 1A to 1B for community orgs.

### Day 8 — Named Tier 1B Organizations

| Organization | Send To | Notes |
|-------------|---------|-------|
| We Are CASA | wearecasa.org/contact/ (web form) | Use 1B template; mid-Atlantic immigrant advocacy |
| Make the Road New York (entry point to network) | mediacontact@maketheroadny.org | Yatziri Tovar; route through NY as network entry point |
| United We Dream | info@unitedwedream.org | National DACA-focused network |
| Centro de los Derechos del Migrante (CDM) | info@cdmigrante.org | Binational migrant worker org |
| Local interfaith sanctuary network (your city) | Research "[city] sanctuary network" | Personalize for local context |

### Days 9–11 — Regional 1B and 1C Contacts

**Day 9**: 5 local interfaith sanctuary networks (research "[city] sanctuary network").
**Day 10**: 5 community legal education programs embedded in churches, community centers, or immigrant service agencies.
**Day 11**: Tier 1C begins — National Bail Fund Network + Community Justice Exchange (network@communityjusticeexchange.org) + 3 local mutual aid networks.

For Tier 1C, switch to Template 1C (shorter, Signal-native format from `DISTRIBUTION_CHECKLIST.md`).

### Day 12 — Remaining 1C Contacts

Food Not Bombs local chapters and other mutual aid networks. Note: many of these are best reached via Signal groups rather than email. Use the Template 1C text adapted for Signal if you have access to relevant group chats.

---

## Week 2 Mid-Point Checkpoint (Day 10)

Answer these questions before continuing:

1. **Week 1 response rate**: Responses (any type, excluding Bounce and OOO) / 25 sends × 100. Target: more than 10%.
2. **Bitly data**: Are people clicking through after opening? If Bitly shows clicks but no email responses, the email is getting read but no clear action is triggered. Consider adding a more concrete call-to-action in the Week 2 template.
3. **Pattern**: Which category (1A vs. 1B vs. 1C) is generating the most engagement? Prioritize more sends in that category for Week 2 remainder.
4. **Pivot needed?** If Week 1 response rate is below 5% (fewer than 2 responses in 25 sends): review `TIER1_OUTREACH_EXECUTION_PLAN.md` Section 5.3 for diagnostic steps before continuing Week 2.

---

## Week 3: Days 15–19

**Target**: Remaining contacts + Week 1 follow-ups. Slow pace: 3–5 new sends per day.

### Follow-Up Schedule

| Day | Action |
|-----|--------|
| Day 15 | Send follow-up (Template R2) to Day 1 sends with no response |
| Day 16 | Send follow-up to Day 2 sends with no response |
| Day 17 | Send follow-up to Day 3 sends with no response; continue new sends at 3/day |
| Day 18 | Follow-ups primary; new sends secondary |
| Day 19 | Close-out: final new sends + document all Week 1-2 statuses in tracking spreadsheet |

**Follow-up rule**: One initial email, one follow-up only. No third contact unless you made an explicit commitment to someone at the organization to follow up again. Sending a third email damages credibility.

---

## Post-Execution Steps (Day 19 and Beyond)

### Logging Responses

For every response received (through end of Week 4), log in the tracking spreadsheet:

- **Engagement (Class 1)**: Contact asks questions, says they will share, requests a call. Reply with Template R1 within 24 hours. Flag in the spreadsheet as a priority relationship.
- **Acknowledgment (Class 2)**: "Thank you, we'll review." Log. Send Template R2 follow-up at Day 10 if no further engagement.
- **Declination (Class 3)**: Any form of "not for us." Send Template R3. Mark as "Declined — closed." Do not follow up again.
- **OOO (Class 4)**: Log return date. Set a calendar reminder for 2 business days after return. Do not count as a response.
- **Bounce (Class 5)**: Research alternate contact immediately. Check org website for updated contact page. Fall back to web form. Log status.

### Categorizing Feedback

At the end of Week 3 and again at end of Week 4, sort your tracking spreadsheet by Response Type and note:

- Are legal aid organizations (1A) or community organizations (1B) responding at a higher rate? Adjust Tier 2 outreach timing accordingly.
- Which organizations asked questions that indicate they are actively reading the corpus (e.g., questions about specific threat model sections)?
- Which organizations expressed intent to share with their network? These are your amplification signals — follow up specifically with them in Week 4 to confirm the share happened and offer additional support.

### Identifying Early Amplification Opportunities

Amplification signals to watch for:

1. **A contact says they forwarded the Gist to their network or mailing list**: This is your highest-value outcome. Ask if they have a sense of how many people received it.
2. **Bitly click spike** not corresponding to your own activity: Someone shared the link in a channel you didn't reach directly.
3. **A new organization contacts you** having been referred by one of your Tier 1 contacts: This is second-order amplification. Add them to the tracking spreadsheet as "Tier 1 — Referred."
4. **A Tier 2 amplifier** (EFF, Intercept, 404 Media, Privacy Guides) mentions the corpus: This would represent reaching the security researcher and journalist amplifier layer ahead of your scheduled Tier 2 outreach.

When you identify an amplification signal: log it in the tracking spreadsheet with date, source, and estimated reach. This data informs whether to accelerate Tier 2 outreach.

---

## Troubleshooting

### Email Bounces

**Permanent bounce (user not found)**: Do not re-send to the same address. Research alternate contact:
1. Check org website contact page for current email.
2. Search `[org name] communications director` or `[org name] press contact`.
3. Use web contact form as fallback.
4. If no alternate: mark "Unreachable — closed."

**Soft bounce (mailbox full, temporary)**: Wait 48 hours. Re-send once. If bounces again, treat as permanent.

**Common address errors**:
- CLINIC's domain is `cliniclegal.org`, not `clinic.org` (different organization).
- CDM's domain is `cdmigrante.org`, not `centrocdm.org`.
- RAICES is `raicestexas.org`.
- Verify `.org` vs. `.com` before every send.

### Deliverability Issues

**Email lands in spam** (recipient tells you): Do not re-send. Ask recipient to whitelist your address. Offer to use the org's web form as an alternative. Review your email for spam trigger words (avoid: "free," "urgent," "act now," capitalized subject lines, multiple exclamation points).

**Gmail rate limiting warning**: Stop for the day. You have been sending faster than the 3–5 minute gap. Resume next morning. The 5-per-day pace should not trigger Gmail limits.

**Web form failures**: Try once more. If form continues to fail, check for a direct email on the org's press room or contact page. If none, mark as "Form failure — check alternate."

### Low Response Rate

**After Week 1, response rate below 10%**: Diagnostic steps:
1. Check Bitly — are people clicking but not responding? (Email opens, corpus doesn't convert to reply.) Or not clicking at all? (Subject line or opening is not generating opens.)
2. Assess contact quality: Are you reaching named individuals or general inboxes? Named contacts respond at a higher rate.
3. Adjust: Rewrite subject line. Add one more specific sentence of personalization. Try calling out a section more directly relevant to that org's work.

**After Week 2, response rate below 5%**: See the hybrid escalation protocol in `TIER1_OUTREACH_EXECUTION_PLAN.md` Section 7.3 — LinkedIn follow-up for top 10 non-responders, phone for the five named national organizations.

### Forwarding Barriers

**Contact says they would share but cannot**: Ask why. Common barriers:
- Organization legal policy prevents forwarding external resources without review. Offer to have them review specific sections and adapt for internal distribution.
- Contact does not know the right person to forward to. Offer to help identify the right person (e.g., "Would your tech team or client services coordinator be the right person?").
- Contact is concerned about the corpus being too technical. Remind them that Part 0 requires no technical expertise and the Tier 1 checklist is designed for clients with no technical background.

---

## Quick Reference: Timeline

| Day | Action |
|-----|--------|
| Day 0 | Pre-execution checklist (45–60 min) |
| Day 1 | 5 emails — named Tier 1A orgs (NILC, CLINIC, RAICES, ILRC, NLG) |
| Days 2–5 | 5 emails/day — regional Tier 1A |
| Day 7 | Mid-week checkpoint: Week 1 response rate, Bitly data |
| Days 8–12 | 5 emails/day — Tier 1B and 1C |
| Day 10 | Week 2 mid-point checkpoint: pivot assessment |
| Day 15 | Week 1 follow-ups begin (Template R2 for non-responders) |
| Days 15–19 | 3–5 new sends/day + follow-up loop |
| Day 19 | Close-out: final sends, all statuses documented |
| Week 4+ | Response handling, amplification tracking, no new outreach |

**Total estimated time**: 2–3 hours setup + 4 hours/week for 3 active weeks + 2–3 hours/week response handling = 20–25 hours total.

---

## Files Referenced in This Runbook

| File | Purpose |
|------|---------|
| `TIER1_OUTREACH_PREPARED.md` | Personalized email drafts for 5 named Tier 1A organizations |
| `TIER1_OUTREACH_EXECUTION_PLAN.md` | Full personalization framework, response handling, contingency plans |
| `TIER1_DISTRIBUTION_PREP.md` | Contact lists, strategy overview, approved templates |
| `DISTRIBUTION_CHECKLIST.md` | Full Tier 1/2/3 contact lists and sharing scripts |
| `TIER1_CONTACT_VALIDATION.md` | Verified current contact info for 14 named organizations |
| `TIER1_SUCCESS_METRICS.md` | Success definitions, tracking template, amplification signals |
| `QUARTERLY_UPDATE_PROTOCOL.md` | How to keep the threat model current after outreach |

---

*Created: 2026-04-28. Corpus reflects surveillance landscape as of April 26, 2026. Quarterly review scheduled: July 28, 2026.*
