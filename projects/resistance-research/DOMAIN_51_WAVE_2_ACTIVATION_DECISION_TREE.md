---
title: "Domain 51 — Wave 2 (Tier 2) Activation Decision Tree"
created: "2026-06-29"
status: "production-ready"
trigger: "T+7 checkpoint — 7 days after Wave 1 send date"
input: "Composite signal score from DOMAIN_51_IMPACT_DASHBOARD_TEMPLATE.md Sheet 3"
output: "One of three activation paths: HIGH RESPONSE / MEDIUM RESPONSE / LOW RESPONSE + CONTINGENCY"
companion_files:
  - DOMAIN_51_RESPONSE_MONITORING_PROTOCOL.md
  - DOMAIN_51_IMPACT_DASHBOARD_TEMPLATE.md
  - PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md
  - DOMAIN_51_FALLBACK_TIER_2_CONTACTS.md
  - DOMAIN_51_WAVE_1_EMAIL_EXECUTION_PACKAGE.md
---

# Domain 51 — Wave 2 (Tier 2) Activation Decision Tree

**Design principle**: This document is fully mechanical. At T+7, read your composite score from Metrics Sheet column B11, find the matching branch below, and execute the listed steps. No analysis required.

**T+7 date**: 7 days after Wave 1 send date. If Wave 1 sends June 29, T+7 = July 6.

**Congressional calendar note**: July 4-10 is the Senate State Work Period / Independence Day recess. Policy organizations' response bandwidth is reduced June 30-July 10. If T+7 falls in this window and your score is below threshold, hold until T+14 before triggering the LOW RESPONSE path. The recess is a timing factor, not a content factor — an email that arrived during recess will still be seen when staff return July 11.

---

## Step 1 — Compute Composite Score

Open DOMAIN_51_IMPACT_DASHBOARD_TEMPLATE.md and read:

- **B4**: STRONG Signal Count
- **B5**: MODERATE Signal Count

Compute: **Composite Score = (B4 × 3) + (B5 × 1)**

Then read the estimated open rate from B9 (Email Analytics average).

---

## Step 2 — Find Your Branch

```
COMPOSITE SCORE ≥ 4  →  HIGH RESPONSE BRANCH
COMPOSITE SCORE 2-3  →  MEDIUM RESPONSE BRANCH
COMPOSITE SCORE 1    →  HOLD — extend to T+14
COMPOSITE SCORE 0    →  LOW RESPONSE + CONTINGENCY BRANCH

OPEN RATE ≥ 60% (regardless of score)  →  Pre-stage Wave 2 contacts NOW, then re-evaluate score at T+7
```

---

## HIGH RESPONSE BRANCH (Composite Score 4+)

### What this score means

4 points requires at minimum: 1 STRONG + 1 MODERATE, or 2 STRONG signals. This means at least two of your five contacts have produced substantive engagement signals. This is a strong outcome for cold research outreach to national policy organizations.

### Immediate actions (execute within 24 hours of T+7 checkpoint)

**Step 1: Reply to STRONG signals.**
Respond to every STRONG reply within 24 hours of the T+7 checkpoint (or 24 hours of receipt if received before T+7). Use this framework for your reply:

- If the reply asks a specific question about the research: answer it directly and offer a one-page summary for internal distribution ("I've put together a single-page overview if that's easier to share with colleagues — happy to send it")
- If the reply mentions sharing with a colleague: say "That's great — if it would help, I can send a version formatted for a policy brief or testimony" (this is the citation conversion play)
- If the reply is a general "thank you, this is useful": reply briefly, restate the most relevant section to their work, and offer a follow-up conversation

**Step 2: Activate Wave 3 (Tier 1 national amplifiers).**
Wave 3 = End Citizens United/LAV, Public Citizen, Brennan Center, Democracy 21, OpenSecrets. Templates in DOMAIN_51_WAVE_1_EMAIL_EXECUTION_PACKAGE.md Wave 3 section.

Execute in this sequence (90-minute stagger between sends, same day or across two days):
1. End Citizens United / Let America Vote — info@endcitizensunited.org
2. Public Citizen Democracy Program — cholman@citizen.org
3. Brennan Center for Justice — ghoshs@brennan.law.nyu.edu
4. Democracy 21 — fwertheimer@democracy21.org
5. OpenSecrets — info@opensecrets.org

Target send window: T+7 to T+10 (July 6-9 if Wave 1 sent June 29).

**Step 3: Activate the three priority Tier 2 contacts.**
These are distinct from the 13 Tier 2 contacts in DOMAIN_51_WAVE_1_EMAIL_EXECUTION_PACKAGE.md. Execute starting T+2 from activation (two days after T+7 checkpoint):

| Priority | Organization | Contact | Email | Template Source |
|---|---|---|---|---|
| 1 | True North Research | Lisa Graves | lisa@truenorthresearch.org | DOMAIN_51_FALLBACK_TIER_2_CONTACTS.md Contact 1 |
| 2 | UCLA Safeguarding Democracy | Rick Hasen | rhasen@law.ucla.edu | DOMAIN_51_FALLBACK_TIER_2_CONTACTS.md Contact 2 |
| 3 | Demos | Taifa Smith Butler | info@demos.org | Standard research distribution template (Domain 51 hook: "equal say in democracy" + FEC enforcement frame) |

**Step 4: Log in Sheet 4 (Checkpoint Record).**
Record the T+7 date, all signal counts, composite score, and "GO" as the Gate_Decision. Log the Wave 3 send schedule in the Action_Taken column.

**Step 5: Update PHASE_2_BATCH_SEQUENCING_POST_DOMAIN_51.md.**
Mark Domain 51 as "HIGH RESPONSE — Phase 2 gate passed" and note the T+7 STRONG signal count for the composite scoring across all Phase 2 domains.

### HIGH RESPONSE — expected timeline

| Date | Action |
|---|---|
| T+7 (July 6) | Log checkpoint; reply to STRONG signals; activate Wave 3 sequence |
| T+8 (July 7) | Send Wave 3 Emails 1-3 (ECU, Public Citizen, Brennan) |
| T+9 (July 8) | Send Wave 3 Emails 4-5 (Democracy 21, OpenSecrets) |
| T+9 (July 8) | Send Tier 2 Email 1 (Lisa Graves, True North) |
| T+10 (July 9) | Send Tier 2 Emails 2-3 (Rick Hasen, Demos) |
| T+14 (July 13) | Secondary checkpoint — count Wave 3 replies; log in Sheet 4 |
| T+30 (July 29) | Full assessment — total engagement count across all tiers |

---

## MEDIUM RESPONSE BRANCH (Composite Score 2-3)

### What this score means

2-3 points means you have partial but real engagement: 1 STRONG (3 points) or 1-3 MODERATE signals (1-3 points). One national policy organization substantively engaging with the research is a meaningful outcome at this scale. Two or three MODERATE acknowledgments without STRONG signal suggests the research is being received and reviewed but hasn't yet reached the staff member who would engage substantively.

### Immediate actions

**Step 1: Reply to any STRONG signal (same as HIGH RESPONSE).**
Identical to Step 1 above. If you have 1 STRONG and the score is 3, reply within 24 hours.

**Step 2: Activate Wave 3 with modified sequencing.**
Execute Wave 3 but prioritize the contacts most aligned with the STRONG signals you received.

If your STRONG came from CLC: Lead Wave 3 with Brennan Center (ghoshs@brennan.law.nyu.edu) — they share the constitutional litigation framing. Send Brennan first, then Democracy 21 (fwertheimer@democracy21.org), then Public Citizen. Send ECU and OpenSecrets as the final two.

If your STRONG came from Issue One: Lead Wave 3 with Democracy 21 (FEC reform focus shared with Issue One) then ECU/LAV, then Public Citizen. Send Brennan and OpenSecrets last.

If your signal is MODERATE only (no STRONG): Execute Wave 3 in the default sequence but reduce the email body to 3 paragraphs (shorter framing indicates higher-volume distribution mode). Default sequence: ECU, Public Citizen, Brennan, Democracy 21, OpenSecrets.

**Step 3: Activate first two Tier 2 contacts only (not all three).**
Activate True North Research and Rick Hasen. Hold Demos for T+14 re-evaluation.

**Step 4: Monitor closely through T+14.**
The MEDIUM score means one strong reply can push you to HIGH. Any additional STRONG signal received between T+7 and T+14 upgrades you to HIGH RESPONSE actions for remaining unsent contacts.

**Step 5: Log in Sheet 4.**
Gate_Decision = "CONDITIONAL." Note which Wave 3 sequence you are executing and why.

### MEDIUM RESPONSE — expected timeline

| Date | Action |
|---|---|
| T+7 (July 6) | Log checkpoint; reply to STRONG signal if present; decide Wave 3 sequence |
| T+8-9 (July 7-8) | Send Wave 3 (modified sequence per above) — all 5 contacts |
| T+9 (July 8) | Send Tier 2 Email 1 (Lisa Graves, True North) |
| T+10 (July 9) | Send Tier 2 Email 2 (Rick Hasen, UCLA) |
| T+14 (July 13) | Secondary checkpoint — if 1+ new STRONG: upgrade to HIGH RESPONSE for remaining Tier 2 contacts; if score unchanged: hold Demos |
| T+21 (July 20) | If Demos still not sent and score has not improved: make final decision whether to send |

---

## HOLD — EXTEND TO T+14 (Composite Score 1)

### What this means

1 point = a single MODERATE signal (OOO reply, generic acknowledgment, or Bitly click spike) and nothing else. This is below the threshold for Wave 3 activation but above the threshold for the LOW RESPONSE contingency. It means one observable signal has confirmed delivery, and the research may still be under review.

**Congressional calendar factor**: If T+7 falls between July 4-10 (recess), composite score 1 is almost certainly underweighted. Hold to T+14 before deciding. Policy staff who received your email on June 29-30 will not be back at full capacity until July 11. T+14 (July 13) is therefore the real first gate for sends executed in this window.

### T+14 action

At T+14, re-run the composite score from the Metrics sheet. Apply the branch that matches the new score:
- Score 4+: HIGH RESPONSE (proceed as above, compress Wave 3 timeline)
- Score 2-3: MEDIUM RESPONSE (proceed as above, compress Wave 3 timeline)
- Score 1 (unchanged): Execute Wave 3 anyway — do not hold past T+14. Send the full Wave 3 sequence without the "STRONG" confirmation. The research is in the active congressional window (July 11-August 10) and further delay reduces value.
- Score 0 (still no signal): LOW RESPONSE + CONTINGENCY (see below)

Log the T+14 decision in Sheet 4, Checkpoint Record.

---

## LOW RESPONSE + CONTINGENCY BRANCH (Composite Score 0)

### What this means

0 points at T+7 = no replies, no attributable Bitly clicks, no OOO messages. For five contacts at national policy organizations, zero observable signal after 7 days warrants investigation before escalating to contingency. It may mean: emails are in spam, the Gist URL is returning an error, the contact emails have changed, or the July 4 holiday window compressed response timelines.

### Diagnostic check (before activating contingency)

Run these three checks before concluding the response is genuinely low:

1. **Check sent mail**: Verify all five emails appear in your Gmail sent folder with the correct addresses. Confirm there are no delivery failure notices in your inbox that you may have missed.

2. **Check Bitly**: Log into bitly.com and read total click count. If you see any clicks at all, at least one person followed the link — the email reached an inbox. This contradicts a spam-folder assumption.

3. **Check the Gist URL**: Load https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372 (or your Bitly short link) in a browser. Confirm it returns HTTP 200 and the full research document is visible. If the Gist returns 404, the link is broken and recipients who tried to click received an error — the content was inaccessible. This would explain zero engagement. Recreate the Gist before sending any follow-up (procedure: DOMAIN_51_CONTINGENCY_SB_299_FALLBACK.md).

### If all three diagnostics check out (sends confirmed, Gist live, some Bitly clicks): Hold to T+14

Response lag for national policy organizations during the holiday/recess window is normal. Do not activate contingency before T+14 if you have confirmed delivery.

### If T+14 composite score is still 0 AND all diagnostics check out: Activate contingency

**Step 1: Activate PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md.**

The low-response scenario is addressed in the Success Path section's T+7 gate logic. Specifically: "0-1 STRONG = Wave 3 conditional." If T+14 shows 0 STRONG, activate Branch logic based on the current date:

| Today's date | Action |
|---|---|
| Before July 8 | Branch A protocol: accelerate send sequence, activate Tier 2 unconditionally |
| July 9-14 | Branch B protocol: compressed daily cadence, Wave 3 unconditional |
| July 15+ | Branch C protocol: full-scale activation, everything unconditional before August 8 |

**Step 2: Execute a single follow-up to CLC only (not all five contacts).**

CLC (Erin Chlopak) is the highest-value contact and the only one where a brief follow-up is appropriate at Day 14 without appearing excessive. Use the follow-up template from DOMAIN_51_WAVE_1_EMAIL_EXECUTION_PACKAGE.md Contingency Routing section:

**To**: echlopak@campaignlegalcenter.org
**Subject**: Following up — Citizens United research, Hawaii/Montana charter model

```
Following up on my [Wave 1 send date] message. The Domain 51 research on the Hawaii/Montana corporate charter theory is at the link below — if this is useful to your team or you can direct me to the right person at CLC, I would appreciate it.

[Gist URL or Bitly short link]

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

Do not send a follow-up to Issue One at Day 14 — Issue One's review cycle for unsolicited research is longer than CLC's. Hold Issue One to T+30 before considering any follow-up.

**Step 3: Activate Wave 3 unconditionally.**

Execute Wave 3 (ECU, Public Citizen, Brennan, Democracy 21, OpenSecrets) regardless of Wave 1-2 signal. These contacts have independent value and do not depend on CLC or Issue One responding first. Use the T+14 date to compute the new T+7 checkpoint for Wave 3.

**Step 4: Log in Sheet 4.**
Gate_Decision = "NO-GO — contingency activated." Record which diagnostics you ran, what the Gist/Bitly showed, and what contingency branch you activated.

---

## Contact Sequencing Reference — Wave 3

The following three Tier 2 contacts are the activation targets for HIGH and MEDIUM responses. Detailed email templates are in DOMAIN_51_FALLBACK_TIER_2_CONTACTS.md.

| Priority | Organization | Contact | Email | Best Use Case |
|---|---|---|---|---|
| 1 | True North Research | Lisa Graves | lisa@truenorthresearch.org | Highest alignment — dark money investigation focus. Send first in all scenarios. |
| 2 | UCLA Safeguarding Democracy Project | Rick Hasen | rhasen@law.ucla.edu | Academic amplification — Election Law Blog reaches campaign finance practitioners and congressional staff. |
| 3 | Demos | Taifa Smith Butler | info@demos.org | Cross-domain — democracy + economic equality frame. Activate in HIGH or MEDIUM (score 4+ or 2+ STRONG). |

**Timing rule**: Stagger Tier 2 sends by 24 hours (not 90 minutes). Tier 2 is a separate send session, not a same-day block. Rationale: Each Tier 2 send requires a customized opener that references the Wave 1-2 signal ("I'm writing after sharing this with [org] and receiving [signal]") — these require brief personalization, not copy-paste execution.

---

## Decision Tree Summary — Quick Reference

At T+7, read composite score from Sheet 3 Cell B11:

```
B11 ≥ 4  ──→  HIGH RESPONSE
              Activate Wave 3 immediately
              Activate all 3 Tier 2 contacts (July 8-10)
              Reply to all STRONG signals within 24h

B11 = 2-3 ──→  MEDIUM RESPONSE
               Activate Wave 3 (modified sequence)
               Activate Tier 2 contacts 1-2 (hold #3)
               Re-evaluate at T+14

B11 = 1  ──→  HOLD
              Check congressional calendar (July 4-10 recess)
              Extend to T+14 before branching
              If T+14 score ≥ 2: proceed to MEDIUM; if 0: proceed to LOW

B11 = 0  ──→  LOW RESPONSE + CONTINGENCY
              Run 3 diagnostics (delivery, Gist, Bitly)
              If T+14 still 0: activate PHASE_2 contingency branch
              Follow up CLC only (Day 14)
              Activate Wave 3 unconditionally
```

---

## Escalation Script — What to Say to STRONG Responders

This script is for the reply you send within 24 hours of any STRONG signal. Adapt by contact.

**Opening** (always lead with specific acknowledgment of their content):
> Thank you for taking the time to engage with Domain 51. Your point about [specific thing they mentioned] is exactly the dimension I hoped the [Section X] analysis would surface.

**Bridge** (connect their engagement to the forward path):
> If it would be useful to your team, I've prepared a one-page structured summary of the [Hawaii/Montana charter theory / FEC enforcement collapse / DISCLOSE Act pathway] section that formats easily for internal circulation or citation context.

**Ask** (one specific ask, not two):
> Would it be helpful to have that summary, or is there a colleague at [organization] you think would benefit from a direct version of the document?

**Close**:
> Happy to answer any questions on the constitutional analysis or the underlying citation structure.

This script is appropriate for CLC, Issue One, Brennan Center, and Democracy 21. For OpenSecrets (data-focused org): replace the bridge paragraph with "If OpenSecrets would like to excerpt or republish the dark money data sections, CC Attribution 4.0 allows that without additional permission."

---

*Produced June 29, 2026. Decision tree activates at T+7 checkpoint. Read composite score from DOMAIN_51_IMPACT_DASHBOARD_TEMPLATE.md Sheet 3 and execute the matching branch. No analysis required beyond reading B11 and following the tree.*
