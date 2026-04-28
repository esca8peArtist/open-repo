---
title: "Tier 1 Outreach Execution Plan"
project: cybersecurity-hardening
created: 2026-04-28
status: approved-ready-for-execution
executor: Anya
gist-url: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
---

# Tier 1 Outreach Execution Plan

**For**: Anya  
**Date**: 2026-04-28  
**Corpus Gist URL**: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108  
**Total contacts targeted**: ~50–60 (25 per week for two active weeks, remainder in Week 3)  
**Total execution time**: 2–3 hours setup + ~4 hours/week for three weeks + ~2–3 hours/week follow-up loop  

---

## Purpose and Scope

This is the operational execution guide for Tier 1 outreach of the OpSec corpus — the three-document set (threat model, countermeasures playbook, implementation guide) published at the Gist URL above.

The approved messaging templates are in `TIER1_OUTREACH_PREPARED.md`. This document does not re-create those templates. Instead, it covers: exactly how to execute at pace without triggering Gmail rate limits, how to personalize each contact in 8–12 minutes, how to categorize and respond to every response type you will receive, and what to do if the campaign underperforms.

Start here. Have `TIER1_OUTREACH_PREPARED.md` open in a separate tab for the full email drafts.

---

## Section 1: Pre-Launch Checklist

**Estimated time: 2–3 hours. Complete everything in this section before sending any emails.**

### 1.1 Gist Verification

The single most important pre-launch step: confirm the Gist is publicly accessible and contains the correct content.

- [ ] Open https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108 in a private/incognito browser window (not logged into GitHub). Confirm it loads without a login wall.
- [ ] Verify the Gist contains all three documents: threat-model.md, opsec-playbook.md, implementation-guide.md. Optional: publication-prep.md (executive summary + glossary).
- [ ] Confirm Part 0 (data broker opt-outs) is intact and the California DROP platform path is documented — this is the section you will specifically call out to legal aid organizations.
- [ ] Note the current file count and approximate page count. You will reference these in outreach ("a three-part corpus" or "four-document corpus" depending on whether publication-prep.md is included).

**If the Gist is inaccessible**: Check your GitHub account login status. If the Gist was accidentally set to Secret, change visibility to Public. Do not send any emails until the Gist is confirmed publicly accessible.

### 1.2 URL Shortener and Analytics Setup

Standard Gist URLs provide no analytics. Set up a trackable short URL before launch so you can measure click-throughs independently of email open rates.

Recommended: **Bitly** (free tier, no account required for basic use, but account gives you click analytics).

Steps:
1. Go to bitly.com. Create a free account using a non-primary email (so the account is linked to this project, not your personal email).
2. Shorten: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
3. Note the short URL (e.g., bit.ly/opsec-corpus or similar). Bitly free tier allows custom back-halves.
4. Confirm the short URL redirects correctly in a private browser window.
5. Use the short URL in all outreach emails. Bitly's free dashboard shows total clicks, geographic distribution, and referrer data — sufficient for a 50-contact campaign.

**Alternative if Bitly is unavailable**: Use tinyurl.com for redirection without analytics, and rely on response rate as your primary engagement signal.

### 1.3 Email Tracking Setup

For a 50-contact campaign, sophisticated email tracking is not necessary and may trigger spam filters. Use the minimum viable setup:

**Primary tool: Gmail Labels and Filters**

Create the following labels in Gmail before Day 1:
- `Tier1-Outreach/Sent` — applied to every outreach email you send (BCC yourself, then label the BCC copy)
- `Tier1-Outreach/Response-Engagement` — positive responses (questions, interest, forwarding intent)
- `Tier1-Outreach/Response-Acknowledgment` — "received, will review" type responses
- `Tier1-Outreach/Response-Declination` — "not for us" or "too busy" responses
- `Tier1-Outreach/OOO` — auto-responder out-of-office replies (do NOT count these as responses)
- `Tier1-Outreach/Bounce` — undeliverable email notifications
- `Tier1-Outreach/Follow-Up-Pending` — contacts awaiting a follow-up from you

To create labels: Gmail → Settings → Labels → Create new label. Nest them under a parent label `Tier1-Outreach` for organization.

**Optional enhancement**: Mailchimp free tier (up to 500 contacts, basic open tracking). Only worth setting up if you plan to do multiple outreach rounds or want automated follow-up sequences. For a single 50-contact campaign, Gmail labels are sufficient and less likely to flag as bulk mail.

### 1.4 Response Template Library

Before launch, write and save these five response templates in Gmail (Settings → Templates → Enable, then compose and save). You will send these within 24 hours of receiving the corresponding response type.

**Template R1: Engagement — Follow-Up with Depth**

Use when: Contact expresses interest, asks questions, or says they will share the resource.

```
Subject: Re: [original subject]

Thank you — glad this is useful.

[Answer any specific questions they asked, pointing to primary sources in the corpus where relevant.]

A few additional notes that may be useful for your context:

- Part 0 (data broker opt-outs) is the highest-leverage action for clients with no technical background. The California DROP platform path is specific to CA residents and requires no government-issued ID beyond an AB 60/AB 1766 state ID.
- The threat model section is structured to be citable by legal practitioners — all claims are tied to FOIA disclosures, government contracts, or court filings with direct URLs.
- A quarterly review of this corpus is planned given how quickly the surveillance landscape is evolving. I'll send an update if significant revisions are made.

Happy to discuss specific sections or threat scenarios.

[Your name]
```

**Template R2: Acknowledgment — Light Follow-Up (send after 10 days)**

Use when: Contact says "received, will review" or "thanks, I'll pass this along" with no further engagement.

```
Subject: Re: [original subject]

Following up briefly — wanted to check whether this was useful or if any questions came up after you reviewed it.

No need to respond if this isn't the right time. I'll do a quarterly review of the corpus in July and can send an update then if helpful.

[Your name]
```

**Template R3: Declination — Acknowledgment Only**

Use when: Contact says they are not interested, too busy, or out of scope.

```
Subject: Re: [original subject]

Understood — thank you for the response. No further action needed on your end.

[Your name]
```

**Template R4: Bounce — Research and Reroute**

Use when: Email bounces with a permanent delivery failure.

```
[Internal action, not a reply]
Log in tracking spreadsheet: "Bounce — research alternate contact"
Steps: Check org website for updated contact info. If none found, use web contact form as fallback.
```

**Template R5: Out-of-Office — Schedule Follow-Up**

Use when: Auto-responder indicates the contact is out until a specific date.

```
[Internal action, not a reply]
Log in tracking spreadsheet: "OOO until [date]"
Set calendar reminder for [return date + 2 business days] to follow up.
Do NOT send a follow-up email during the OOO period.
```

### 1.5 Tracking Spreadsheet

Create this spreadsheet before Day 1. Google Sheets is fine. Save it as "Tier 1 Outreach Tracker — [start date]".

**Columns**:

| Column | Notes |
|--------|-------|
| Organization | Full name |
| Category | 1A / 1B / 1C |
| Contact Name | If known |
| Contact Email / Method | Email address or "web form" |
| Template Used | 1A / 1B / 1C (email variant) |
| Date Sent | YYYY-MM-DD |
| Time Sent | HH:MM AM/PM EDT |
| Email Variant | A / B / C (rotation — see Section 3) |
| Open Tracking | Bitly click recorded Y/N |
| Response Received | Y / N |
| Response Date | YYYY-MM-DD |
| Response Type | Engagement / Acknowledgment / Declination / OOO / Bounce |
| Follow-Up Sent | Y / N |
| Follow-Up Date | YYYY-MM-DD |
| Notes | Personalization notes, specific questions asked, etc. |

**Setup time**: 15–20 minutes to create the spreadsheet and pre-populate the first 25 rows with organizations from TIER1_DISTRIBUTION_PREP.md.

---

## Section 2: Day-by-Day Execution Schedule

**Rhythm**: 5 contacts per active day, sent between 7:00–9:00 AM EDT. This pace avoids Gmail's rate-limiting thresholds (typically triggered at 20+ emails per hour to new domains) and puts your emails in inboxes before the day's inbox management happens.

### Pre-Week 0: Setup (Complete Before Day 1)

| Task | Time |
|------|------|
| Complete Section 1 (Gist check, Bitly, Gmail labels, templates, spreadsheet) | 2–3 hours |
| Build contact list for Weeks 1 and 2: 50 organizations with contact info | 1–2 hours |
| Write 2–3 subject line and opening variants for each email template | 30 minutes |
| Confirm your "from" email address is the one you want associated with this project | 5 minutes |

**Contact list sourcing**: Use TIER1_DISTRIBUTION_PREP.md for the named national organizations (NILC, CLINIC, RAICES, ILRC, NLG, CASA, Make the Road, United We Dream). For Week 2's 25 contacts, research regional organizations using the search patterns below (Section 3).

---

### Week 1: Days 1–5 (Tier 1A — Legal Aid Organizations, Priority)

**Target**: 25 contacts, 5/day. Tier 1A legal organizations first because they have established channels for client resources and the fastest path to the people facing immediate enforcement risk.

**Daily routine**:
- 6:45–7:00 AM: Open tracking spreadsheet. Identify today's 5 contacts. Have the personalization notes ready (researched the day before).
- 7:00–7:45 AM: Send 5 emails, one at a time, with 3–5 minute gaps between sends.
- 7:45–8:00 AM: Update spreadsheet with send times. Apply `Tier1-Outreach/Sent` label to BCC copies.
- Evening (5–10 minutes): Check for responses. Apply appropriate labels. Log in spreadsheet.

| Day | Contacts | Notes |
|-----|----------|-------|
| Day 1 | NILC, CLINIC, RAICES, ILRC, NLG | Named contacts from TIER1_OUTREACH_PREPARED.md; highest-confidence contact info |
| Day 2 | 5 regional immigration legal aid orgs | Research the day before; see Section 3 for research method |
| Day 3 | 5 more regional legal aid orgs | Continue rotating email variants |
| Day 4 | 5 law school immigration clinics | University-based; good research contact info availability |
| Day 5 | 5 public defender offices with immigration units | Research: public defender + city/state + immigration |

**Day 1 note**: The Day 1 sends are the five organizations with verified contact information from TIER1_OUTREACH_PREPARED.md. Use the specific email drafts from that document. Insert your name. Confirm the Gist URL is in each email before sending.

---

### Week 2: Days 8–12 (Tier 1B and Mixed — Community Organizations)

**Target**: 25 contacts, 5/day. Shift to Tier 1B community-based organizations and a second wave of Tier 1A regional contacts.

**Rotate templates**: If Week 1 generated measurable click-throughs on the Bitly link, note which subject line variant correlates. Use the better-performing variant more heavily in Week 2.

| Day | Contacts | Notes |
|-----|----------|-------|
| Day 8 | CASA, Make the Road, United We Dream, Centro CDM + 1 local sanctuary network | Named contacts from TIER1_DISTRIBUTION_PREP.md |
| Day 9 | 5 local interfaith sanctuary networks | Search "[city] sanctuary network" for cities with large immigrant populations |
| Day 10 | 5 community legal education programs (not law schools) | Often embedded in churches, community centers, immigrant service agencies |
| Day 11 | National Bail Fund Network + 4 local/regional mutual aid networks | Tier 1C begins; adjust template to 1C variant |
| Day 12 | 5 more Tier 1C mutual aid networks | Food Not Bombs chapters, Anarchist Black Cross affiliates, local general mutual aid |

---

### Week 3: Days 15–19 (Remainder + Catch-Up)

**Target**: Remaining contacts from your list (variable — 10–25 depending on list size). Slower pace — 3–5 per day. Week 3 is also when Week 1 follow-ups begin for non-responders.

| Day | Contacts | Notes |
|-----|----------|-------|
| Day 15 | 3–5 remaining new contacts | Lower pace — you will also be handling Week 1 follow-ups |
| Day 16 | 3–5 remaining new contacts | Week 1 follow-ups due for Day 1–3 sends (10 business days after send) |
| Day 17 | 3–5 remaining + follow-up batch | |
| Day 18 | Follow-ups primary | Week 1 sends that haven't responded: send Template R2 |
| Day 19 | Catch-up and documentation | Close out any remaining new sends; review tracking spreadsheet |

---

### Weeks 4+: Response Handling and Follow-Up Loop

**~2–3 hours per week for 4 weeks**

No new outreach. Manage response flow:

- **Week 4**: Follow-ups for Week 2 non-responders (Template R2). Answer any engagement questions within 24 hours (Template R1).
- **Week 5**: Follow-ups for Week 3 non-responders. Final response handling.
- **Weeks 6–7**: Diminishing returns. Only follow up if an explicit commitment was made (e.g., "I'll pass this along to my team"). Log final status for all 50+ contacts.

**Cutoff rule**: No more than two contacts per organization. One initial email and one follow-up. Do not send a third email to any organization. It damages your credibility and the credibility of the resource.

---

## Section 3: Personalization Framework

**Time budget per contact: 8–12 minutes** (research + personalization + compose + send)

This section covers how to do that efficiently. The goal is genuine personalization — 2–3 sentences that demonstrate you understand what the specific organization does and why this corpus is relevant to their work — not surface-level name insertion.

### 3.1 Research Sources (in order of reliability)

For each organization or contact, work through this list in order. Stop when you have enough for a 2–3 sentence personalization:

1. **Organization website** (2 minutes): Read the "About" and "Programs" pages. Note their primary geographic focus, client population, and any current campaigns. Look for mentions of digital security, data privacy, or enforcement response.

2. **Recent news or press releases** (2 minutes): Search "[organization name] site:organizationsite.org" or "[organization name] press release 2025 2026". Note any recent work that connects to the ELITE targeting system, data broker issues, or digital security.

3. **LinkedIn** (2 minutes, if you have access): Search for the specific contact person's profile. Note their title, how long they've been at the organization, and any recent posts or articles. This is useful for personalizing to a named contact vs. a general inbox.

4. **Twitter/X or Bluesky** (1–2 minutes): Search the organization's handle for recent posts related to enforcement, ICE, data privacy, or surveillance. A recent post about a relevant topic is a natural opening hook.

5. **Google Scholar or organizational publications** (if applicable for law school clinics and think tanks): Note any recent papers or practice guides they've published on enforcement or immigration technology.

### 3.2 Personalization Template Structure

Every email should follow this structure. The personalization appears in the opening 2–3 sentences only. The body of the email (which explains the corpus) remains consistent with the approved templates.

```
Opening hook [1–2 sentences, personalized]:
  "[Organization] has been doing X — [how this corpus is relevant to X]."
  OR
  "Given [contact's] work on [specific topic], I think [specific section] is directly relevant."
  OR
  "[City/region] is [specific enforcement context] — this guide has specific resources for [that context]."

Corpus description [3–4 sentences, from approved template]:
  Use the body from Template 1A, 1B, or 1C as appropriate.

Call to action [1–2 sentences, consistent]:
  Part 0 call-out + Gist URL + offer to discuss.
```

### 3.3 Domain-Specific Personalization Notes

**For immigration legal aid organizations (1A)**:
- Lead with Part 0 (data broker opt-outs) and the primary-source structure of the threat model.
- If the organization has a California presence, specifically mention the AB 60/AB 1766 → DROP platform path.
- If the organization does impact litigation, mention that the threat model is designed to be citable from primary documents.
- Avoid: Overexplaining what Palantir is. Legal aid organizations that work on enforcement are already aware of Palantir; the value here is the primary-source documentation and the client-actionable implementation guide.

**For community organizations (1B)**:
- Lead with accessibility: "no technical expertise required," "2–4 hours," "immediate impact."
- If the organization does community education workshops, suggest that Part 0 is workshoppable — a two-hour session could walk through the opt-outs together.
- If the organization serves a Spanish-speaking population, acknowledge that a Spanish-language version of Part 0 is on the roadmap for the next quarterly update.
- Avoid: Heavy technical language in the opening. Use "the databases ICE queries" not "the ELITE address confidence scoring pipeline."

**For mutual aid networks (1C)**:
- Use the 1C template (shorter, Signal-native format).
- These audiences already have security culture. You can reference Signal and Tor without explaining what they are.
- Emphasize: Part 0 is the highest-ROI action for the broadest population. Tier 2 and Tier 3 are for people who have reason to believe they are under active investigation.
- Avoid: Corporate framing. These audiences are skeptical of formal institutional language. Keep it direct.

**For law school clinics**:
- Lead with the primary-source structure and citeability.
- Mention that clinic students doing supervised practice could use Part 0 as a client intake supplement.
- Note the verification checkpoints in the implementation guide — they are designed to prevent the "false confidence" failure mode, which is a legal liability issue as much as a security issue.

### 3.4 Batch Processing for Speed

Group your 25 weekly contacts by category before the week starts. Do research in batches on the Sunday before each active week:

- Sunday before Week 1: Research all 25 Week 1 contacts. Write personalization notes (2–3 sentences each) into the tracking spreadsheet's Notes column. This takes ~2 hours up front but reduces daily morning prep to 5 minutes.
- Sunday before Week 2: Same process for Week 2 contacts.

This batching approach means your morning send window (7:00–7:45 AM) is compose-and-send, not research-and-compose-and-send.

---

## Section 4: Response Handling and Escalation

**SLA**: Answer all engagement responses within 24 hours. Send all follow-ups 7–10 days after the previous contact. Never send more than two contacts per organization.

### 4.1 Response Classification

When a reply arrives, classify it immediately before doing anything else. Apply the corresponding Gmail label.

**Class 1: Engagement**

Signals: Contact asks questions about the corpus, expresses intent to share, asks about specific sections, requests a call or meeting, or says they have forwarded it to colleagues.

This is your most valuable response type. Do not delay. Reply within 24 hours using Template R1, adapted to their specific questions.

*Escalation path*:
- If they ask for a call or meeting: This is appropriate. Schedule it. Prepare a 15-minute overview of the threat model and Part 0 — keep it actionable, not comprehensive.
- If they ask for a Spanish-language version: Tell them it is on the roadmap for the July 2026 quarterly review. Offer to send it when ready.
- If they ask whether you can present to their staff or client group: This depends on your bandwidth and relationship. If yes, this is a high-value outcome — a staff training reaches more people than an email.
- If they want to adapt the corpus for their own publication or handout: Yes. The corpus is designed for adaptation. Ask them to note what was changed from the original and retain the primary source citations. A brief "based on [Gist URL]" attribution is sufficient.

**Class 2: Acknowledgment**

Signals: "Thank you for sending this." "We'll take a look." "I've passed this along to our team." No questions, no commitments.

This is a neutral outcome. Log it. Send Template R2 after 10 days if no further engagement. Do not push for more than one follow-up.

*Escalation path*:
- After 10-day follow-up, if still no engagement: Close the loop in your tracking spreadsheet as "Acknowledged, no further engagement." This organization is not a priority relationship.
- If they were a top-priority contact (one of the named national organizations): Make one additional attempt via an alternate channel (web contact form if you used email, or phone call to the communications office) before closing.

**Class 3: Declination**

Signals: "This isn't our focus right now." "We don't have capacity." "Please remove us from future outreach." Any version of no.

Log it. Send Template R3 (acknowledgment only). Do not follow up further. Mark as "Declined — closed" in the tracking spreadsheet.

**Declinations are data.** If you receive a pattern of declinations from a specific category (e.g., all law school clinics decline), that is a signal that your framing for that category needs adjustment. Note the reasons given if any are provided.

**Class 4: Out-of-Office (OOO)**

Signals: Automated reply indicating the contact is away until a specific date.

Do not count this as a response. Log the return date and set a calendar reminder for 2 business days after return. Do not send any email during the OOO period.

**Class 5: Bounce**

Signals: Mailer-daemon bounce notification, "user not found," "address does not exist."

Log as bounce. Research alternate contact immediately:
1. Check organization website for updated contact page.
2. Search "[organization] communications director email" or "[organization] press contact."
3. If no alternate found, fall back to web contact form.
4. If no web form, mark as "Unreachable — closed."

### 4.2 Specific Anticipated Questions and Prepared Answers

These questions are drawn from the FAQ in TIER1_DISTRIBUTION_PREP.md. Have these answers ready; you will receive some version of each.

**"Is any of this legal?"**
Yes. Data broker opt-outs are a statutory right (CCPA, California DELETE Act, and broker-specific mechanisms). Signal, GrapheneOS, Tor Browser, VeraCrypt, and Mullvad VPN are all legal tools. The corpus does not describe anything illegal.

**"Can I adapt this for my community or publication?"**
Yes. The corpus is designed to be adaptable. Ask them to note what was changed from the original and retain the primary source citations. A "based on [Gist URL]" attribution is all that is needed.

**"Does this actually protect someone against the government?"**
The corpus explicitly addresses this: it targets bulk commercial surveillance infrastructure (data brokers, location data markets, ad-tech tracking) that operates without warrants and at scale. It does not claim to protect against a targeted investigation with a valid court order. Those are two different threat models. The goal is not to be the easiest target, not to be invisible to a determined, resourced investigation.

**"We don't have a tech team to implement this. Is it still useful?"**
Yes — Part 0 (data broker opt-outs) requires no technical expertise and is immediately actionable by anyone. The Tier 1 checklist (Signal, basic device hygiene) is designed for non-technical users. Tier 2 and Tier 3 require more technical investment and are for people who have specific reason to believe they are under active investigation.

**"Can you speak to our staff or clients?"**
Depends on your bandwidth. If yes: offer a 30-minute Zoom session focused on Part 0 and the Tier 1 checklist. Keep it practical — the goal is for people to leave with three things they will actually do, not a comprehensive threat overview.

---

## Section 5: Tracking and Reporting

**Principle**: Track enough to know if the campaign is working and when to pivot. Do not over-build the tracking system.

### 5.1 Daily Log (5 minutes at end of each send day)

At the end of each morning send session, update the tracking spreadsheet with:
- Number of emails sent today
- Any immediate OOO responses received
- Any bounces

At the end of the day, add:
- Any responses received (type + brief notes)
- Follow-ups scheduled (what, for whom, when)

### 5.2 Weekly Summary (15 minutes, every Friday)

Every Friday during the active outreach period, write a brief summary (in the Notes column of the spreadsheet, or in a separate OUTREACH_LOG.md file) covering:

| Metric | Target | How to calculate |
|--------|--------|-----------------|
| Emails sent this week | 25 | Count from tracking spreadsheet |
| Cumulative sends | Running total | |
| Responses received | — | Count by type |
| Response rate by category | Target: >10% | Responses / Sends × 100 for each category |
| Bitly clicks this week | — | Check Bitly dashboard |
| Engagement responses | — | Class 1 responses |
| Follow-ups pending | — | Emails awaiting follow-up |
| Top engagement patterns | — | What questions are being asked; which category is most responsive |

**Honest assessment each Friday**: Is this working? Are specific categories responding? Is the subject line working (click-through rate via Bitly)?

### 5.3 Pivot Triggers

**Trigger 1: Response rate below 10% after Week 1**

If fewer than 3 of 25 Week 1 emails generate any response (Engagement, Acknowledgment, or Declination — OOO and Bounce excluded), pause before Week 2 sends. The problem is likely one of:
- Subject line is not compelling
- Framing does not match what these organizations care about
- Contact quality (you're reaching the wrong person at each organization)

Diagnostic steps:
1. Check Bitly: Are people clicking the link but not responding? (Means the email is getting read but the corpus is not compelling enough, or they have no clear action to take.) Or are people not clicking at all? (Means the email is not being opened, or the opening does not create enough interest to click.)
2. Check subject line: Did the more specific subject line variant outperform the generic one?
3. Check contact quality: Were you reaching a general inbox or a specific person? Specific named contacts respond at a higher rate.

Adjustment: Rewrite the subject line. Add one sentence of more specific personalization to the opening. Adjust the primary call-to-action to be more concrete (e.g., "I'd like to send you a one-page summary of Part 0" rather than "happy to discuss").

**Trigger 2: Response rate below 5% after Week 2**

If fewer than 5% of 50 sends have generated any response after two full weeks, this is a signal that the email channel is not the right channel for this population. Move to the hybrid approach described in Section 7 (Contingency Plans).

**Trigger 3: Specific category consistently not responding**

If one category (e.g., law school clinics) has zero responses after 5 sends, do not send more to that category until you have adjusted the framing. Either the contact is wrong (reaching a webmaster instead of a clinic director) or the framing is wrong (leading with technical detail for an audience that responds to client impact).

---

## Section 6: Logistics and Tools

### 6.1 Gmail Setup

**Before Day 1**, complete these Gmail configurations:

Labels (create nested structure under `Tier1-Outreach`):
- `Tier1-Outreach/Sent`
- `Tier1-Outreach/Response-Engagement`
- `Tier1-Outreach/Response-Acknowledgment`
- `Tier1-Outreach/Response-Declination`
- `Tier1-Outreach/OOO`
- `Tier1-Outreach/Bounce`
- `Tier1-Outreach/Follow-Up-Pending`

Templates (Gmail → Settings → Advanced → Enable Templates):
Save the five response templates from Section 1.4 as drafts with descriptive names: "R1-Engagement", "R2-Acknowledgment-Followup", "R3-Declination", etc.

Filters to create:
- Emails from domains ending in `.gov` → label `Tier1-Outreach/Flag` (unusual senders worth noting)
- Subject lines containing "out of office" or "away from" or "on leave" → label `Tier1-Outreach/OOO` (auto-applies label, though you will still need to manually set follow-up date)

**BCC yourself on every send**: This creates a copy in your sent folder that you can label and search. Alternative: Gmail's "Save to Sent" is usually sufficient, but BCC creates a separate thread you can use for reference.

### 6.2 Contact Database Management

**Source of truth**: The tracking spreadsheet is the canonical record. Do not maintain two lists.

**Avoiding duplicates**: Before adding a new contact to Week 2 or Week 3, search the tracking spreadsheet for the organization name. Organizations with multiple offices (RAICES has five Texas offices) should be contacted once, at the central communications address, not once per office.

**Managing bounces**: When an email bounces, immediately research the alternate contact and update the spreadsheet. Do not leave bounces unresolved — a bounce means a real person has not received the information.

**Email address hygiene before sending**:
- Double-check every email address before sending Week 1.
- Common errors: .org vs. .com confusion, hyphenated domain names (cliniclegal.org, not clinic.org), name format errors (firstname@org.org vs. firstnamelastname@org.org).
- For web forms: note in the tracking spreadsheet that delivery confirmation depends on the form, not an email send receipt. Look for a "thank you for your submission" page.

### 6.3 Gist Link Management

**Single canonical URL**: Use the full Gist URL in all emails. The Bitly short URL is for analytics only; include it as an alternative or use it in place of the full URL with a note in the email that it redirects to the Gist.

**If the Gist URL changes** (GitHub removes a gist, or you publish to a different platform): Update the Bitly redirect target. All existing short links will automatically redirect to the new destination. This is one of the operational advantages of using a short link layer.

**Bitly dashboard access**: Log into bitly.com at least once per week during the active outreach period to check aggregate click counts. You are looking for: total clicks trending up after each send batch (confirms emails are being opened and links are being clicked), geographic distribution (confirms reach beyond your immediate network), and any unusual spike (someone shared the link in a larger forum).

### 6.4 Backup Contact List

Export the tracking spreadsheet to a local CSV every Friday during active outreach. Store in `projects/cybersecurity-hardening/outreach-backups/` (create this directory). Google Sheets does not require backup for a 50-row spreadsheet, but a local copy is good practice for a project of this sensitivity.

---

## Section 7: Contingency Plans

### 7.1 Email Deliverability Issues

**Symptom**: Gmail warning about rate limiting, or emails landing in spam folders based on recipient feedback.

**Rate limiting**: Gmail allows ~500 emails per day for personal accounts and typically does not rate-limit when you are sending 5 emails over 45 minutes. If you receive a rate-limiting warning, you have been sending much faster than the 3–5 minute gap recommended above. Stop for the day. Resume the next morning.

**Spam folder**: If a recipient tells you your email went to spam, do not re-send. Instead: (1) ask them to whitelist your email address, (2) offer to use the web contact form for that organization as an alternative channel, (3) review your email for spam trigger words (avoid: "free," "urgent," "act now," excessive capitalization, multiple exclamation points).

**Deliverability check**: Before Week 1 sends, test your email deliverability at mail-tester.com (free). Send a test email to their generated address and get a score. Anything above 8/10 is fine. If lower, look at their specific flags and fix them.

### 7.2 Contact Database Errors

**Bad emails (permanent bounce)**: Research and reroute as described in Section 4.1. Budget 10–15 minutes per bounce to find a correct alternate.

**Web form failures**: If a web contact form returns an error or you never receive a confirmation screen, try again once. If the form continues to fail, check whether the organization has a direct email address on their contact page or press room page. If no alternate, mark as "Form failure — unreachable" and move on.

**Contact left the organization**: If a named contact is no longer at the organization (out-of-office message with a different person's name, or LinkedIn shows they moved), route to the organization's general communications email or web form instead. Note in the tracking spreadsheet.

### 7.3 Low Engagement: Hybrid Escalation

**Trigger**: Fewer than 5% response rate (fewer than 3 responses per 50 sends) after Week 2.

**Escalation to hybrid email + LinkedIn approach**:

For your top 10 priority contacts who have not responded by the end of Week 2:

1. Search for the specific person you emailed on LinkedIn.
2. Send a brief LinkedIn connection request with a note (300 character limit): "Hi [Name] — I sent an email to [org address] about a security guide for immigration enforcement risk. Wanted to make sure it reached you. Happy to connect."
3. If they accept the connection, send a LinkedIn message with the Gist URL and a one-sentence description.
4. Do not use LinkedIn and email simultaneously for the same contact. LinkedIn is the escalation channel when email is not working.

**Escalation to phone**:

Reserved for the five highest-priority named organizations (NILC, CLINIC, RAICES, ILRC, NLG). If email and LinkedIn have both failed after three weeks, call the organization's main number and ask for the communications team or the person whose email you used. Keep it brief: "I sent an email about a security resource for undocumented clients — wanted to make sure it reached the right person." This is appropriate for organizations where you have verified contact information and a clear reason to follow up.

**Pivot to direct community channel**:

If institutional outreach (legal aid, community organizations) is underperforming, move resources to the 1C mutual aid network channel, which has a lower barrier to entry and faster share velocity. A single post in the right Signal group can reach more people than a week of cold email to legal organizations. Use the Template 1C format (shorter, Signal-native) and post directly in relevant channels if you have access.

---

## Timeline Summary

| Phase | Timeframe | Hours |
|-------|-----------|-------|
| Setup (Section 1) | Before Day 1 | 2–3 hours |
| Week 1 sends (25 contacts) | Days 1–5 | ~4 hours (research + send + daily log) |
| Week 2 sends (25 contacts) | Days 8–12 | ~4 hours |
| Week 3 sends + follow-ups | Days 15–19 | ~3 hours |
| Week 4+ follow-up loop | Ongoing, 4 weeks | ~2–3 hours/week |
| Total | ~6 weeks | ~20–25 hours |

---

## Quick Reference: Before You Send Each Email

- [ ] Gist URL confirmed accessible: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
- [ ] Your name in the email (no [Your name] placeholders)
- [ ] 2–3 sentence personalized opening (not copy-pasted from template)
- [ ] Correct template used (1A for legal orgs, 1B for community orgs, 1C for mutual aid)
- [ ] Email variant rotated (A/B/C)
- [ ] Tracking spreadsheet row pre-populated for this contact
- [ ] BCC yourself
- [ ] Time: 7:00–9:00 AM EDT
- [ ] Gap from previous send: at least 3–5 minutes

---

## Files Referenced in This Document

| File | Purpose |
|------|---------|
| `TIER1_OUTREACH_PREPARED.md` | Full personalized email drafts for the five named Tier 1A organizations |
| `TIER1_DISTRIBUTION_PREP.md` | Contact lists, strategy overview, approved email templates by tier |
| `DISTRIBUTION_CHECKLIST.md` | Full Tier 1/2/3 contact lists and sharing scripts |
| `CHECKIN.md` | Corpus verification status and publication readiness |

**Canonical Gist URL**: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108  
**Alternate URL (Tier_1A_OUTREACH.md)**: Do not use — this file contains a placeholder URL from an earlier draft.

---

*Last updated: 2026-04-28. Corpus reflects surveillance landscape as of April 26, 2026. Quarterly review scheduled: July 26, 2026.*
