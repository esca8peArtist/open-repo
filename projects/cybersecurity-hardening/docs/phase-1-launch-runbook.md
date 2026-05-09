---
title: "Phase 1 Launch Runbook — Hour-by-Hour Execution Guide"
project: cybersecurity-hardening
created: 2026-05-09
status: production-ready
executor: Anya
gist-url: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
cross-references:
  - TIER1_OUTREACH_PREPARED.md
  - TIER1_EXECUTION_RUNBOOK.md
  - TIER1_OUTREACH_EXECUTION_PLAN.md
  - docs/phase-1-tracking-spreadsheet-spec.md
  - docs/phase-1-gist-creation-walkthrough.md
  - docs/phase-1-contingency-playbook.md
---

# Phase 1 Launch Runbook — Hour-by-Hour Execution Guide

**Scope**: Day-by-day execution timeline for Phase 1 outreach — the 14 named Tier 1A contacts (immigration legal aid organizations) plus ongoing regional contact research. Covers Day 1 through Day 7 in granular detail, with daily monitoring cadence through Day 21.

**Prerequisite**: User has reviewed and approved email drafts in `TIER1_OUTREACH_PREPARED.md`. Do not begin sending until confirmed.

**Gist URL (canonical, publicly accessible)**:
`https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108`

**Execution window**: 7 active send days (Day 1–7), 14-day monitoring tail (Day 8–21), one follow-up loop (Day 15–19).

**Estimated total time**: 2–3 hours setup + 30–60 min/day for 7 send days + 15 min/day monitoring through Day 21.

---

## Pre-Launch Setup (24–48 Hours Before Day 1)

Complete every item before sending the first email. Estimated time: 45–60 minutes total.

### Gist Accessibility Verification (10 min)

- [ ] Open `https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108` in a **private/incognito browser window** (not logged into GitHub). Confirm it loads without a login wall.
- [ ] Verify all three core documents are present: `threat-model.md`, `opsec-playbook.md`, `implementation-guide.md`. Optional fourth: `publication-prep.md` (executive summary + glossary).
- [ ] Confirm Part 0 (data broker opt-outs) is intact with the California DROP platform path documented — this is the section most useful for legal aid organizations' clients.
- [ ] Note current file count. You will reference this in outreach ("a three-part corpus" or "four-document corpus").
- [ ] **If the Gist is inaccessible**: Change visibility to Public in GitHub settings before proceeding. See `docs/phase-1-gist-creation-walkthrough.md` for step-by-step instructions.
- [ ] Save the Gist URL to your clipboard and a notepad/note app. You will paste it many times.

**Output**: Gist confirmed publicly accessible. URL saved.

### URL Shortening and Analytics Setup (10 min)

- [ ] Go to `bitly.com`. Create a free account using a non-primary email address so the account is linked to this campaign, not your personal email.
- [ ] Shorten: `https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108`
- [ ] Set a custom back-half (e.g., `bit.ly/opsec-corpus` or `bit.ly/opsec-guide`).
- [ ] Confirm the short URL redirects correctly in a private browser window.
- [ ] Save the short URL to your notepad. **Use the short URL in all outreach emails** — Bitly's free dashboard shows total clicks, geographic distribution, and referrer data.

**Alternative**: If Bitly is unavailable, use `tinyurl.com` for redirection without analytics, and rely on response rate as your primary engagement signal.

**Output**: Short URL created and confirmed working. Saved alongside the full Gist URL.

### Gmail Label Setup (10 min)

Create the following nested Gmail labels before Day 1. Navigate to Gmail → Settings → See All Settings → Labels → Create new label.

| Label | Purpose |
|-------|---------|
| `Tier1-Outreach` | Parent label (create first) |
| `Tier1-Outreach/Sent` | Applied to BCC copy of every outreach email sent |
| `Tier1-Outreach/Response-Engagement` | Positive responses (questions, interest, forwarding intent) |
| `Tier1-Outreach/Response-Acknowledgment` | "Received, will review" type responses |
| `Tier1-Outreach/Response-Declination` | "Not for us" or "too busy" responses |
| `Tier1-Outreach/OOO` | Auto-responder out-of-office replies (do NOT count as responses) |
| `Tier1-Outreach/Bounce` | Undeliverable email notifications |
| `Tier1-Outreach/Follow-Up-Pending` | Contacts awaiting follow-up from you |

**Output**: 7 labels created and nested under `Tier1-Outreach`.

### Gmail Templates Setup (5 min)

- [ ] Enable Gmail Templates: Settings → See All Settings → Advanced tab → Enable Templates → Save Changes.
- [ ] Create five response templates (compose → three-dot menu → Templates → Save draft as template):
  - `R1-Engagement`: For contacts who express interest or ask questions. See template in `TIER1_OUTREACH_EXECUTION_PLAN.md` Section 1.4.
  - `R2-Acknowledgment-Followup`: Light 10-day follow-up for "received, will review" responses.
  - `R3-Declination`: Acknowledgment-only for "not interested" responses.
  - `R4-Bounce-Log` (internal note): Research-and-reroute procedure reminder.
  - `R5-OOO-Log` (internal note): OOO return date + follow-up calendar reminder procedure.

**Output**: 5 templates saved in Gmail.

### Tracking Spreadsheet Setup (15 min)

- [ ] Open `docs/phase-1-tracking-spreadsheet-spec.md` for the full column specification.
- [ ] Create a Google Sheet titled "Phase 1 Outreach Tracker — [today's date]".
- [ ] Add the columns from the spreadsheet spec (Organization, Category, Contact Name, Contact Email/Method, Template Used, Date Sent, Time Sent, Bitly Click, Response Received, Response Date, Response Type, Follow-Up Sent, Follow-Up Date, Notes).
- [ ] Pre-populate the five named Day 1 contacts from `TIER1_OUTREACH_PREPARED.md`:
  1. National Immigration Law Center (NILC) — info@nilc.org + web form
  2. CLINIC — Catholic Legal Immigration Network — national@cliniclegal.org
  3. RAICES (Texas) — communications@raicestexas.org
  4. Immigrant Legal Resource Center (ILRC) — kbello@ilrc.org
  5. National Lawyers Guild (NLG) — massdef@nlg.org

**Output**: Tracking spreadsheet created with Day 1 contacts pre-populated.

### Deliverability Check (5 min)

- [ ] Send a test email from your outreach account to your personal email. Verify it arrives in inbox (not spam).
- [ ] Optional: Check deliverability score at `mail-tester.com` (aim for 8/10 or above). Paste your email address in their interface and send the test email to their generated address.
- [ ] Confirm your "from" address is the one you want permanently associated with this campaign.

**If test email lands in spam**: Review the email for spam trigger words (avoid: "free," "urgent," "act now," all-caps text, multiple exclamation points). Consider sending plain text rather than HTML.

**Output**: Outreach account confirmed deliverable.

### Final Pre-Send Verification Per Email

Before every individual send throughout Days 1–7:

- [ ] Gist short URL (Bitly) is correct in the email body.
- [ ] Your name replaces every `[Your name]` placeholder.
- [ ] Opening 2–3 sentences are personalized to this specific organization.
- [ ] Correct email draft used (drafts are in `TIER1_OUTREACH_PREPARED.md`).
- [ ] BCC yourself on the email.
- [ ] Email queued for 7:00–9:00 AM local time (highest open rates; not a hard rule but a good default).

---

## Day 1 Launch (Wave 1 — Named Tier 1A Organizations)

**Target**: 5 named national immigration legal aid organizations with verified contacts.
**Send window**: 7:00–9:00 AM local time, 3–5 minutes between each send.
**Estimated time**: 40–50 minutes total.

### Hour 0: Pre-Send Final Check (7:00 AM)

**Actions** (5 min):
1. Open Gmail. Confirm tracking spreadsheet is open in another tab.
2. Open `TIER1_OUTREACH_PREPARED.md` for the email drafts.
3. Confirm Gist URL loads in incognito browser (30 seconds).
4. Copy Bitly short URL to clipboard.

### 7:00–7:10 AM — Send 1: National Immigration Law Center (NILC)

**Draft**: `TIER1_OUTREACH_PREPARED.md` → Organization 1 → NILC Email Draft
**Method**: Dual send — email to `info@nilc.org` AND submit via web form at `https://www.nilc.org/about-us/contact-us/`
**Subject**: Resource for NILC legal team — primary-sourced OpSec guide for Palantir ELITE threat landscape
**Personalization**: Insert your name. Add any personal connection to NILC if you have one.

**Post-send** (2 min):
- Apply `Tier1-Outreach/Sent` label to your BCC copy.
- Log in spreadsheet: Organization = NILC | Date Sent = today | Time Sent = now | Method = Email + Form.
- Set calendar reminder: Day 8 = NILC follow-up date (if no response).

### 7:15–7:25 AM — Send 2: CLINIC

**Draft**: `TIER1_OUTREACH_PREPARED.md` → Organization 2 → CLINIC Email Draft
**Method**: Email to `national@cliniclegal.org`
**Subject**: New resource for CLINIC affiliates — data broker opt-out guide for clients facing ICE enforcement
**Personalization**: Insert your name.

**Post-send** (2 min):
- Label + log + calendar reminder (Day 8 follow-up).

### 7:30–7:40 AM — Send 3: RAICES

**Draft**: `TIER1_OUTREACH_PREPARED.md` → Organization 3 → RAICES Email Draft
**Method**: Email to `communications@raicestexas.org` (Director of Communications: Thaís Silva-Marques)
**Subject**: OpSec resource for Texas clients — Palantir ELITE threat model and data broker opt-out guide

**Post-send** (2 min):
- Label + log + calendar reminder (Day 8 follow-up).

### 7:45–7:55 AM — Send 4: ILRC

**Draft**: `TIER1_OUTREACH_PREPARED.md` → Organization 4 → ILRC Email Draft
**Method**: Email to `kbello@ilrc.org` (Kemi Bello, Communications Manager)
**Subject**: New primary-sourced security guide for your practitioner network — ELITE threat model and client countermeasures

**Post-send** (2 min):
- Label + log + calendar reminder (Day 8 follow-up).

### 8:00–8:10 AM — Send 5: National Lawyers Guild

**Draft**: `TIER1_OUTREACH_PREPARED.md` → Organization 5 → NLG Email Draft
**Method**: Email to `massdef@nlg.org`
**Subject**: OpSec corpus for NLG mass defense practitioners — Palantir ELITE and data broker surveillance
**Personalization**: Insert your name. Reference NLG's mass defense work directly.

**Post-send** (2 min):
- Label + log + calendar reminder (Day 8 follow-up).

### 12:00 PM — Day 1 Bounce Check

**Actions** (5 min):
- Check Gmail inbox for delivery-status notifications (undeliverable, permanent bounce, soft bounce).
- If a bounce appears: research alternate contact immediately (org website → press room → web form). Log in spreadsheet as "Bounce — researching alternate." Apply `Tier1-Outreach/Bounce` label.
- If no bounces: all five sends are in transit. No action needed.

### Day 1 Close Checkpoint (5 PM)

Answer these four questions and log in the Notes column:

1. **How many emails sent today?** (Target: 5) ___
2. **Any immediate bounces?** ___
3. **Any early responses?** (Classify and apply Gmail label) ___
4. **Bitly clicks today?** (Check Bitly dashboard) ___

---

## Day 2: Regional Research + Wave 2 Research Prep

**Target**: No new sends today (unless you have an existing regional contact ready). Use this day to research 5 regional Tier 1A contacts for Day 3.

**Day 2 morning research session (30 min)**:

Run these searches for the region or state most relevant to your network or work context:

- `[state] immigration legal aid nonprofit`
- `[state] law school immigration clinic`
- `[city] immigrant services legal defense`
- `[state] public defender immigration unit`

**For each candidate organization, document**:
- Organization name and mission
- Contact name (Communications Director / Executive Director if small org)
- Email address (verified from their website, not assumed)
- Web contact form URL if no direct email
- 2–3 sentences on why this corpus is relevant to their specific work (for personalization)

**Target**: Identify 5 candidate organizations with verified contacts. Enter them in your tracking spreadsheet with status "Research Complete — Ready to Send."

**Day 2 afternoon** (15 min): Check inbox for responses to Day 1 sends. Classify any replies and apply Gmail label. Check Bitly dashboard for click activity.

---

## Day 3: Wave 2 — Regional Tier 1A Organizations

**Target**: 5 regional immigration legal aid organizations (contacts researched Day 2).
**Send window**: 7:00–9:00 AM local time, 3–5 minutes between each send.
**Estimated time**: 30–40 min.

**Morning pre-send** (5 min):
- Open tracking spreadsheet. Confirm all 5 Day 3 contacts have verified emails.
- Open email drafts from `TIER1_OUTREACH_PREPARED.md`. Adapt the Template 1A draft for each organization — replace the specific threat model details that are most relevant to their region and context.

**Sending cadence**: Same as Day 1 — 7:00 AM, 7:10, 7:20, 7:30, 7:40 AM. BCC yourself on each.

**Day 3 post-send actions**:
- Log all 5 in spreadsheet with send times.
- Set calendar reminders: Day 10 = follow-up date for Day 3 contacts with no response.
- Check Bitly for Day 1 click activity.
- Classify any Day 1 responses. Reply to Engagement (Class 1) responses within 24 hours using Template R1.

---

## Day 4: Wave 3 — Tier 1B Community-Based Organizations

**Target**: 5 named Tier 1B organizations (community advocacy organizations). See `TIER1_EXECUTION_RUNBOOK.md` Day 8 for the named contact list (We Are CASA, Make the Road New York, United We Dream, Centro de los Derechos del Migrante, one local interfaith sanctuary network).

**Template shift**: Switch from Template 1A (legal aid framing) to Template 1B (community advocacy framing). Adjust opening paragraph to emphasize organizing and community protection over legal practitioner use.

**Send window**: 7:00–9:00 AM, same cadence as Days 1 and 3.

**Day 4 monitoring**:
- Check inbox at 12:00 PM for bounces from Days 1 and 3.
- Classify and label any incoming responses.
- Log Bitly clicks.

---

## Day 5: Wave 4 — Regional Tier 1B Research and Send

**Morning research** (30 min): Apply same research pattern as Day 2 for local community organizations:
- `[city] interfaith sanctuary network`
- `[city] immigrant community center`
- `[state] community legal education program`

**Sending**: 5 regional Tier 1B contacts using Template 1B.

---

## Day 6: Wave 5 — Tier 1C Mutual Aid Networks

**Target**: Tier 1C mutual aid organizations. See `TIER1_EXECUTION_RUNBOOK.md` Day 11 for named contacts (National Bail Fund Network, Community Justice Exchange, local mutual aid networks).

**Template shift**: Switch to Template 1C — shorter format, Signal-native language, community-defense framing. See `DISTRIBUTION_CHECKLIST.md` for the Signal/Slack short-form scripts that work for this audience.

**Note on delivery method**: Many Tier 1C organizations are better reached via Signal group chats than email. If you have access to relevant mutual aid Signal groups, adapt Template 1C for Signal instead.

**Day 6 monitoring**:
- Week 1 mid-point check. How many responses so far? Log in weekly rollup.
- Any Bitly click spikes that don't correspond to your own activity? This indicates someone shared the link in a channel you didn't reach directly.

---

## Day 7: Wave 5 Continued + Optional Follow-Up Wave

**Day 7 new sends** (if contacts remain):
- Complete any remaining Tier 1C contacts.
- 5 sends maximum; maintain 3–5 minute gap between sends.

**Day 7 tally** (at 5:00 PM):

Complete this assessment and log in the tracking spreadsheet Notes column:

| Metric | Target | Actual | Assessment |
|--------|--------|--------|------------|
| Total emails sent | 25+ | ___ | |
| Total Bitly clicks | >30% of sends | ___ | |
| Total responses received | >10% of sends | ___ | |
| Engagement responses (Class 1) | >2 | ___ | |
| Bounces | <15% | ___ | |

**Day 7 Go/No-Go decision**:

- **GO (Phase 1 full continuation)**: Response rate >10%, or 2+ Engagement responses, or Bitly click rate >30%. Continue to Days 8–21 (Tier 1B/1C completion, follow-up loop).
- **ADJUST (messaging tweak)**: Response rate 5–10%, click rate 15–30%. Before Day 8 sends: rewrite subject line, add one more specific personalization sentence, call out a corpus section more directly relevant to each org type.
- **INVESTIGATE**: Response rate <5%, click rate <10%. Diagnostic steps: Is Bitly showing any clicks at all? If yes → emails are being opened but not converting (subject line or CTA problem). If no → delivery may be failing. Check spam folder with a test send to yourself. Review `docs/phase-1-contingency-playbook.md` Scenario 5 (Technical Email Delivery Failure).

---

## Days 8–21: Monitoring, Follow-Up Loop, and Response Management

### Daily Cadence (15 min/day at 12:00 PM)

Each day from Day 8 through Day 21:

1. **Inbox check**: Any new responses from any send wave?
   - Classify response type (Engagement / Acknowledgment / Declination / OOO / Bounce).
   - Apply correct Gmail label.
   - Log in tracking spreadsheet (Response Date, Response Type).

2. **Engagement responses (Class 1)**: Reply within 24 hours using Template R1. These are your highest-priority contacts.

3. **Acknowledgment responses (Class 2)**: Log. Set calendar reminder for Day [send date + 10] to send Template R2 follow-up.

4. **Bitly dashboard**: Any click spikes? Note date and estimated spike size.

5. **Amplification signals**: Did any contact indicate they forwarded the Gist? Note in spreadsheet with estimated reach.

### Follow-Up Schedule (Days 15–19)

| Day | Action |
|-----|--------|
| Day 15 | Send Template R2 follow-up to Day 1 contacts with no response |
| Day 16 | Send Template R2 to Day 3 contacts with no response |
| Day 17 | Send Template R2 to Day 4–5 contacts with no response |
| Day 18 | Send Template R2 to Day 6–7 contacts with no response |
| Day 19 | Final new sends (if any remaining contacts) + document all statuses |

**Follow-up rule**: One initial email, one follow-up only. No third contact unless you made an explicit commitment to a specific individual to follow up again. A third unsolicited email damages credibility.

### Week 2 Mid-Point Checkpoint (Day 12)

Answer these questions before continuing:

1. **Week 1 response rate**: Responses (any type, excluding Bounce and OOO) ÷ sends × 100. Target: >10%.
2. **Bitly data**: Are people clicking but not responding? (Corpus content is engaging but no clear next-step.) Consider adding a more concrete CTA in Week 2 template.
3. **Pattern**: Which category (1A legal vs. 1B community vs. 1C mutual aid) is generating the most engagement? Prioritize that category for remaining sends.
4. **Amplification signals**: Has any contact forwarded the Gist to their network? If so, this is your highest-value outcome from Phase 1 — follow up specifically to confirm the share and offer additional support.

### Day 21 Close-Out

Final tracking spreadsheet review:

- Sort by Response Type. Count each category.
- Identify the 3–5 highest-engagement contacts (those who asked questions, said they would share, or requested follow-up). These are your Phase 2 Tier 2 candidates — the organizations most likely to become amplification partners.
- Document all Bitly click data for the campaign period.
- Note any amplification signals (organization confirmed forwarding the corpus to their network).

**Final metrics log**:

| Metric | Target | Actual |
|--------|--------|--------|
| Total sent (Tier 1A + 1B + 1C) | 40–60 | ___ |
| Total Bitly clicks | >30% of sends | ___ |
| Response rate | >10% | ___ |
| Engagement responses | >3 | ___ |
| Organizations who forwarded corpus | any | ___ |

**Phase 2 Go/No-Go**:

- **GO** (proceed to Phase 2 Tier 2 outreach): Response rate >10%, or 3+ Engagement responses, or at least 1 confirmed network amplification signal. See `PHASE_2_SEQUENCING.md` for the Tier 2 launch sequence.
- **WAIT** (re-engagement before Phase 2): Response rate 5–10%, no confirmed amplification. Deploy supplementary touchpoint (blog post, Reddit thread on r/privacy or r/immigration, or an EFF/FPF pitch) before Tier 2.
- **PIVOT** (revise messaging before broader outreach): Response rate <5% after full follow-up loop. Gather feedback from any respondents, revise subject line and opening paragraph, then re-attempt with a fresh contact set.

---

## Post-Execution Steps

### Response Classification Reference

| Class | Trigger | Action | Timeline |
|-------|---------|--------|---------|
| 1 — Engagement | Interest, questions, forwarding intent | Reply within 24h with Template R1 | Immediate |
| 2 — Acknowledgment | "Received, will review" | Log; Template R2 follow-up at Day [send+10] | 10-day delay |
| 3 — Declination | "Not for us" | Template R3; mark closed; no further contact | Same day |
| 4 — OOO | Auto-responder | Log return date; calendar reminder [return+2 days] | Do not contact during OOO |
| 5 — Bounce | Undeliverable | Research alternate contact; fall back to web form | Same day |

### Amplification Signals to Watch

1. **Contact confirms forwarding the Gist to their network or mailing list**: Your highest-value Phase 1 outcome. Ask if they have a sense of how many people received it.
2. **Bitly click spike not corresponding to your own activity**: Someone shared the link in a channel you didn't reach directly.
3. **New organization contacts you, referred by a Tier 1 contact**: Second-order amplification. Add to tracking spreadsheet as "Tier 1 — Referred."
4. **Tier 2 amplifier mentions the corpus** (EFF, The Intercept, 404 Media, Privacy Guides): This represents reaching the security researcher and journalist layer ahead of your scheduled Tier 2 outreach.

When you identify any amplification signal: log it with date, source, and estimated reach.

---

## Resource Estimates

| Phase | Time Required |
|-------|--------------|
| Pre-launch setup | 45–60 min (one-time) |
| Day 1 send (5 contacts) | 40–50 min |
| Days 2–7 (research + send) | 30–45 min/day |
| Daily monitoring (Days 8–21) | 15 min/day |
| Follow-up wave (Days 15–19) | 20–30 min/day |
| Day 21 close-out and analysis | 30 min |
| **Total** | **~10–12 hours across 21 days** |

Peak demand is Days 1–7 (send days). Days 8–21 are primarily passive monitoring with active follow-up bursts on Days 15–19.
