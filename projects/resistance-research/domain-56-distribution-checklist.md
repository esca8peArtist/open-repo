---
title: "Domain 56 Distribution Checklist — May 28 Pre-Flight"
created: "2026-05-27"
send_window: "May 28, 2026, 14:00–18:00 UTC"
status: "PRODUCTION-READY — execute May 28"
scope: "4 sends: Volcker Alliance, Democracy Forward, CREW, Government Executive"
authority: "DOMAIN_56_TIER_2_DISTRIBUTION_MAY28_CHECKLIST.md (full per-send runbook with email bodies)"
---

# Domain 56 Distribution Checklist — May 28

**Scope**: 4 outbound sends to civil service reform organizations and federal watchdog groups. This checklist is the pre-flight and execution summary. The full email bodies and per-send customization instructions live in `DOMAIN_56_TIER_2_DISTRIBUTION_MAY28_CHECKLIST.md` — have that file open when executing sends.

**Send window**: 14:00–18:00 UTC May 28. This window is independent of the 19:00 UTC synthesis execution. All 4 sends can and should be completed before synthesis runs.

**Why May 28**: The H.R. 492 / Saving the Civil Service Act pre-recess markup window opens June 1-30. Organizations that receive Domain 56 before June 1 can integrate the democratic-design argument into markup advocacy from day one of the window, rather than reacting to markup announcements.

---

## Phase 1: Pre-Flight (Complete Before Any Send)

Estimated time: 15 minutes. Do this in one sitting before sending anything.

**Step 1.1 — Verify the Gist is live**

Open in incognito browser: `https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f`

Expected: Domain 56 full document loads (6,800 words, 47 citations, civil service politicization analysis).
If 404: STOP. Do not send any email until this is resolved. The source document is at `projects/resistance-research/domain-56-civil-service-politicization-governance.md` — recreate the Gist if needed, then verify the new URL before sending.

**Step 1.2 — Verify email template file is accessible**

```bash
ls /home/awank/dev/SuperClaude_Framework/projects/resistance-research/execution/domain-56-email-template.md
```

Expected: file exists, recent modification date. Open it and confirm it contains at minimum: Template 1 (Civil Service Reform Organizations), Template 3 (HR Policy Experts), Template 4 (Federal Watchdog Organizations), and the Government Executive op-ed pitch block.

**Step 1.3 — Check for breaking news on PEER v. Trump or H.R. 492**

Quick search: "Schedule Policy Career" and "PEER v Trump" on CourtListener (courtlistener.com). If a major ruling dropped in the last 48 hours, do not delay the send — add a one-sentence postscript noting the development. The send should go out regardless.

**Step 1.4 — Fill your personal fields (do this once; use in all 4 emails)**

Decide these two values now. Write them here:

- [YOUR_NAME]: _________________________________________________
- [YOUR_CONTACT_INFO] (personal email): _________________________

Every template contains these two placeholders. Replace them all before sending.

**Step 1.5 — Decide on Bitly link tracking (optional but recommended)**

Bitly lets you see which organizations clicked through to the Gist — one link per recipient. If you want tracking:
1. Go to https://app.bitly.com (free account)
2. Paste the Gist URL four times, creating custom back-halves:
   - `domain56-volcker` → use in Send 1
   - `domain56-demfwd` → use in Send 2
   - `domain56-crew` → use in Send 3
   - `domain56-govexec` → use in Send 4
3. Replace the Gist URL in each email with the matching Bitly link

If you skip Bitly: send the Gist URL directly. Tracking is useful but not required for execution.

**Pre-flight complete when**: Gist URL verified live, template file accessible, news check done, [YOUR_NAME] and [YOUR_CONTACT_INFO] decided.

---

## Phase 2: Execute Sends (14:00–18:00 UTC)

Open `DOMAIN_56_TIER_2_DISTRIBUTION_MAY28_CHECKLIST.md` for the full email body text for each send. This section contains the timing, contact, subject line, and completion checklist for each send.

### Send 1 of 4 — Volcker Alliance (14:00 UTC, first send of window)

**Contact**: volcker@volckeralliance.org (direct email)
**Template**: Template 1 — Civil Service Reform Organizations
**Subject**: `Domain 56 Research: Civil Service Institutional Design — H.R. 492 Pre-Recess Window`
**Customization required**: Insert Volcker-specific paragraph (in full checklist file) after "I wanted to share a research document"

Pre-send checklist:
- [ ] [YOUR_NAME] replaced
- [ ] [YOUR_CONTACT_INFO] replaced
- [ ] Volcker customization paragraph inserted
- [ ] Gist URL / Bitly link intact and correct
- [ ] Sent from personal email account (not an automated address)
- [ ] Sent to: volcker@volckeralliance.org

After sending:
- [ ] Sent time recorded: ___________
- [ ] Logged in `distribution-metrics-dashboard-template.md`

### Send 2 of 4 — Democracy Forward (15:30–16:00 UTC, 2 hours after Send 1)

**Contact**: info@democracyforward.org (direct email)
**Template**: Template 4 — Federal Watchdog Organizations (Democracy Forward paragraph only)
**Subject**: `Litigation Support: Domain 56 APA and Constitutional Analysis — PEER v. Trump Brief Materials`
**Key edit**: Keep only the Democracy Forward paragraph from Template 4. Remove the GAP and CREW paragraphs.

Pre-send checklist:
- [ ] [YOUR_NAME] replaced
- [ ] [YOUR_CONTACT_INFO] replaced
- [ ] Only Democracy Forward paragraph retained
- [ ] Gist URL / Bitly link intact
- [ ] Sent to: info@democracyforward.org

After sending:
- [ ] Sent time recorded: ___________
- [ ] Logged in dashboard

### Send 3 of 4 — CREW (16:30–17:00 UTC, afternoon)

**Contact**: https://www.citizensforethics.org/contact/ (website contact form — not direct email)
**Template**: Template 4 — Federal Watchdog Organizations (CREW paragraph only)
**Subject**: `Research Submission: Domain 56 — Civil Service Democratic-Design Analysis`
**Key edit**: Keep only the CREW paragraph from Template 4. Remove the GAP and Democracy Forward paragraphs.

This send uses a web form. Budget 30 minutes — form navigation takes extra time.

Steps:
1. Open citizensforethics.org/contact in browser
2. Select "General Inquiry" or "Research Submission" in form type
3. Fill Name, Email, Subject fields
4. Paste Template 4 body with CREW-only customization
5. Submit
6. Wait for confirmation message — note or screenshot it

Pre-send checklist:
- [ ] Form URL opened: citizensforethics.org/contact
- [ ] Subject field filled
- [ ] [YOUR_NAME] replaced
- [ ] [YOUR_CONTACT_INFO] replaced
- [ ] Only CREW paragraph retained
- [ ] Gist URL intact
- [ ] Form submitted
- [ ] Confirmation received and noted

Fallback: If form is broken, search the CREW website for a direct staff email (media or communications contacts) and send the same message there.

After submitting:
- [ ] Submission time recorded: ___________
- [ ] Confirmation: Y / N
- [ ] Logged in dashboard

### Send 4 of 4 — Government Executive (17:30–18:00 UTC, final send)

**Contact**: editors@govexec.com (direct email)
**Format**: Op-ed pitch — this is different from the other three sends in tone and purpose
**Subject**: `Op-Ed Pitch: The Democratic-Design Argument for Civil Service Reform — New Angle on Schedule P/C`
**Template**: The full op-ed pitch text is written in `DOMAIN_56_TIER_2_DISTRIBUTION_MAY28_CHECKLIST.md` Send 4 section. Copy the entire block.

Key difference: Government Executive is a trade publication. The pitch is for a guest analysis piece, not a research submission. Tone should be editorial/journalistic. Two instances of [YOUR_NAME] and [YOUR_CONTACT_INFO] in this template.

Pre-send checklist:
- [ ] Both instances of [YOUR_NAME] replaced
- [ ] Both instances of [YOUR_CONTACT_INFO] replaced
- [ ] Gist URL intact (appears in body, not footer only)
- [ ] Tone review: reads like an editorial pitch, not an advocacy email
- [ ] Sent to: editors@govexec.com

After sending:
- [ ] Sent time recorded: ___________
- [ ] Logged in dashboard

---

## Phase 3: Post-Send Documentation (Complete Before 19:00 UTC Synthesis)

**Step 3.1 — Log all 4 sends in DISTRIBUTION_EXECUTION_LOG.md**

Open `projects/resistance-research/DISTRIBUTION_EXECUTION_LOG.md`. Add this block:

```
## Domain 56 Tier 2 Wave — May 28, 2026

| Organization | Contact | Sent Time | Bitly Link | Bounce | Notes |
|---|---|---|---|---|---|
| Volcker Alliance | volcker@volckeralliance.org | [time] | domain56-volcker | | |
| Democracy Forward | info@democracyforward.org | [time] | domain56-demfwd | | |
| CREW | contact form | [time] | domain56-crew | | |
| Government Executive | editors@govexec.com | [time] | domain56-govexec | | |

Wave outcome: [X]/4 sends complete by 18:00 UTC
Bounces: [none / list any]
Next check: May 29 morning (T+24h response check)
```

**Step 3.2 — Log in distribution-metrics-dashboard-template.md**

Fill the four May 28 rows in the dashboard file with send timestamps. Response columns will be filled at T+24h, T+48h, and T+72h.

**Step 3.3 — Bounce check (30 minutes after last send)**

Check your email for any bounce-back messages. If a send bounced:
- Do not resend same day
- Check the organization's website for an updated contact email
- Note in the dashboard and DISTRIBUTION_EXECUTION_LOG.md
- Schedule a follow-up for May 30 using the updated contact

**Step 3.4 — Set response monitoring calendar alerts**

| Check | When | Purpose |
|-------|------|---------|
| T+4h | May 28 evening | Auto-replies and bounces |
| T+24h | May 29 morning | First substantive replies |
| T+48h | May 30 | Second reply check |
| T+72h | May 31 | 72-hour window close; assess response rate |

---

## Phase 4: Response Scoring and Follow-Up

**Response scoring rubric** (use for all 4 organizations):

| Score | What it looks like |
|-------|--------------------|
| 5 | Offers to distribute, cite in publications, brief their team, or forward to colleagues |
| 3 | Substantive reply engaging with the analysis — not a form acknowledgment |
| 1 | Generic thank-you or auto-acknowledgment |
| 0 | No reply, bounce, or unsubscribe |

**Target**: 2 of 4 substantive replies (Score 3+) within 72 hours is a successful send wave.

**If a response arrives before synthesis (19:00 UTC)**: This is a positive signal. Assess whether it qualifies as Score 3+ — if so, it contributes to the synthesis QRP calculation. Log it in the signal log before 19:00 UTC.

**Follow-up protocol (June 3-4 for non-respondents)**:

Send this follow-up to non-responding organizations (except Government Executive — op-ed pitches get one send only; allow 10 business days before any follow-up):

```
Subject: Following up — Domain 56 civil service analysis [H.R. 492 markup window now open]

Following up on my May 28 message — the H.R. 492 / Saving the Civil Service Act 
pre-recess markup window is now open (June 1-30). If the democratic-design framing 
in Domain 56 is useful for your work during this window, I am happy to discuss or 
provide an adapted version.

[Gist URL or Bitly link]

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

---

## Rollback Procedures

**Gist URL returns 404 at any point during sends**:
Stop all remaining sends. Check GitHub.com/esca8peArtist. If Gist was deleted, recreate from `projects/resistance-research/domain-56-civil-service-politicization-governance.md`. Verify the new URL before resuming sends. Already-sent emails with the dead URL: send a brief follow-up with the corrected link.

**CREW contact form is broken or inaccessible**:
Search citizensforethics.org for direct staff contacts (media, communications). Use the same Template 4 body with CREW-specific paragraph. Subject line unchanged.

**Government Executive address bounces**:
Search govexec.com for updated editorial contact. Alternatively, send via their online pitch form if available. Same content applies.

**Democracy Forward address bounces**:
Check democracyforward.org/contact for a current address. Organization is active — address likely updated. Resend to correct address same day if bounce is received before 17:00 UTC, or May 29 morning.

---

*Created: May 27, 2026. Full email body text for all 4 sends is in `DOMAIN_56_TIER_2_DISTRIBUTION_MAY28_CHECKLIST.md`. Response tracking template is in `distribution-metrics-dashboard-template.md`.*
