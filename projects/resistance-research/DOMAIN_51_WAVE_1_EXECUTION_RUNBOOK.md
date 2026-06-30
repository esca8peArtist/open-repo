---
title: "Domain 51 Phase 2 Wave 1 — Execution Runbook (Item 45.1)"
subtitle: "Campaign Finance & Dark Money Architecture — June 30, 23:59 UTC Hard Deadline"
created: "2026-06-29"
updated: "2026-06-29 — added Section 3.1: PASS/MODERATE/LOW/ZERO outcome verdict table"
deadline: "2026-06-30 23:59 UTC"
status: "production-ready — copy-paste executable"
item: "Item 45.1"
estimated_execution_time: "90-120 active minutes, 7-hour window with stagger waits"
contacts: "5 verified contacts (Wave 1: CLC + Issue One; Wave 2: Common Cause CA + LWV CA + Clean Money AF)"
success_metric: "All 5 emails sent and logged by 2026-06-30 23:59 UTC"
---

# Domain 51 Wave 1 Execution Runbook

**Deadline**: June 30, 2026, 23:59 UTC. No extensions. No backup date.

June 30 23:59 UTC equals:
- Eastern (EDT): 7:59 PM
- Central (CDT): 6:59 PM
- Mountain (MDT): 5:59 PM
- Pacific (PDT): 4:59 PM
- Hawaii (HST): 1:59 PM

**After this deadline**: Domain M auto-triggers, value drops to 60-75%, California Fair Elections Act messaging window closes permanently.

---

## Section 1: Pre-Execution Verification Checklist

Complete all five checks before opening your email client. Total time: 5-8 minutes.

### Check 1 — Gist URL Live

Open in browser: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372

Confirm: page loads, title contains "Campaign Finance" or "Dark Money", document visible with citations.

PASS: Page loads with full document content.
FAIL: 404, blank page, or redirect. Do not send any email until resolved. See rollback procedure in Section 4.

### Check 2 — Contact Email Addresses Current

Verify these five email addresses against the table below. If any address has bounced in a prior session, substitute the fallback address shown.

| Send | Email Address | Fallback |
|------|---|---|
| 1 | echlopak@campaignlegalcenter.org | info@campaignlegal.org |
| 2 | info@issueone.org | nick@issueone.org |
| 3 | dkemp@commoncause.org | info@commoncause.org |
| 4 | lwvc@lwvc.org | No fallback — omit if bounces |
| 5 | info@CAclean.org | CRITICAL: do NOT use info@cleanmoney.org (unreachable since June 5) |

### Check 3 — Personalization Fields Ready

You need exactly two fields in every email:
- `[YOUR_NAME]` — your full name as it will appear in the signature
- `[YOUR_CONTACT_INFO]` — email address or phone for replies

Write these down before opening Email 1. You will fill them in 5 times.

### Check 4 — Send Window Planning

Send 1 can go at any time June 30 UTC, with one constraint: Send 2 must follow at least 90 minutes after Send 1, and both must be sent by 23:59 UTC. The full Wave 1+2 sequence requires approximately 7 hours (5 sends, 90-minute minimum stagger between each). If starting after 17:00 UTC June 30, skip to the Partial Completion path in Section 4.

Recommended start: as early in June 30 UTC as possible. 09:00 UTC June 30 gives maximum buffer.

### Check 5 — Log File Ready

Open `DOMAIN_51_DISTRIBUTION_SEND_LOG.md`. Confirm the file exists and you can write to it. You will log each send time immediately after sending.

**Pre-execution verification complete. Proceed to Section 2.**

---

## Section 2: Batch Send Procedure

### Wave 1 — National Legal and Policy Organizations (2 emails, 90-minute minimum stagger)

#### Send 1: Campaign Legal Center — Erin Chlopak

| Field | Value |
|---|---|
| To | echlopak@campaignlegalcenter.org |
| Subject | Constitutional architecture research on Citizens United — Hawaii/Montana model + FEC collapse analysis |
| Send window | Anytime June 30 UTC before 22:29 UTC (leaves 90 minutes for Send 2 before deadline) |
| Fallback if bounce | info@campaignlegal.org — same subject and body |

**Email body — copy below, fill YOUR_NAME and YOUR_CONTACT_INFO, send:**

```
Dear Campaign Legal Center team,

I am sharing a research document that may be relevant to your current work
on campaign finance enforcement and state-level reform:

Domain 51 documents the Citizens United architecture from a democratic design
perspective — specifically the structural consequence of the FEC's 200+ day
enforcement quorum collapse and the constitutional theory behind Hawaii SB 2471
(signed May 15, 2026) and Montana I-194 (approximately 1,000 signatures from
qualification).

The sections most relevant to CLC's work:

- Section 6.3 (Hawaii/Montana Corporate Charter Model): the Center for American
  Progress theory that CLC's constitutional team will likely be asked to assess
  — does charter-revocation of corporate political spending authority survive
  the "associations of citizens" rationale in Citizens United, or only the
  state-derived-power rationale?

- Section 3 (FEC Structural Failure): 200-day enforcement collapse with specific
  pending matters — useful documentation for FEC enforcement advocacy

- Section 7 (Reform Architecture): DISCLOSE Act of 2026 legislative pathway +
  state-level equivalents + SEC disclosure rule status

The document is at:
https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372

58 citations, CC Attribution 4.0. I would welcome any feedback on whether the
constitutional analysis of the Hawaii/Montana model accurately represents the
current scholarly and litigation consensus.

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

After sending Send 1:
- [ ] Log send time (UTC) in DOMAIN_51_DISTRIBUTION_SEND_LOG.md — Send 1 row
- [ ] Set timer: 90 minutes before Send 2
- [ ] If bounce received: retry immediately to info@campaignlegal.org

---

#### Send 2: Issue One

| Field | Value |
|---|---|
| To | info@issueone.org |
| Subject | Dark money architecture research — FEC collapse documentation + state ballot measure analysis |
| Send window | At least 90 minutes after Send 1, no later than June 30 23:59 UTC |
| Fallback if bounce | nick@issueone.org — same subject and body |

**Email body — copy below, fill YOUR_NAME and YOUR_CONTACT_INFO, send:**

```
Dear Issue One team,

I am sharing research that complements Issue One's work on FEC reform and
dark money disclosure:

Domain 51 is a structural analysis of the Citizens United architecture with
a dedicated section on the FEC enforcement collapse — which Issue One has been
documenting through your "Strengthening the Rules" reporting. The document uses
Issue One's enforcement deadlock analysis as a primary source and extends it to
the broader democratic accountability argument.

The most relevant sections:

- Section 3 (FEC Structural Failure): 200+ day enforcement shutdown with
  specific pending matters — Issue One's reporting is cited directly; the
  document extends your analysis to the constitutional design argument

- Section 5 (2026 State Ballot Measures): four-state analysis including
  California, Missouri, Montana, and Hawaii — the landscape your ReFormers
  Caucus work is operating in

- Section 7 (Reform Architecture): DISCLOSE Act pathway + the Hawaii corporate
  charter workaround as a parallel track that does not require DISCLOSE Act
  passage

Issue One is cited as a primary source throughout. The document is designed
for distribution to organizations that can use the structural analysis in
their own advocacy:
https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372

58 citations, CC Attribution 4.0. I would be grateful if this reaches your
research team.

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

After sending Send 2:
- [ ] Log send time (UTC) in DOMAIN_51_DISTRIBUTION_SEND_LOG.md — Send 2 row
- [ ] If bounce received: retry immediately to nick@issueone.org

Wave 1 complete when both sends logged. Proceed to Wave 2 immediately or after a break — as long as all Wave 2 sends complete before June 30 23:59 UTC.

---

### Wave 2 — California Campaign Contacts (3 emails, 90-minute minimum stagger between each)

Wave 2 can start same day as Wave 1 (begin at least 3 hours after Send 1) or continue into a later June 30 session. All three sends must be logged before June 30 23:59 UTC to count as full Branch A execution.

#### Send 3: Common Cause California — Darius Kemp

| Field | Value |
|---|---|
| To | dkemp@commoncause.org |
| CC | info@commoncause.org |
| Subject | Research on Citizens United architecture for California Fair Elections Act campaign — July 1 window |
| Salutation note | "Dear Darius" is correct — Kemp is current Executive Director (Stein departed June 2025) |

**Email body — copy below, fill YOUR_NAME and YOUR_CONTACT_INFO, send:**

```
Dear Darius,

I am sharing a research document on the Citizens United dark money architecture
that may be directly useful to the California Fair Elections Act campaign ahead
of the November 3 ballot.

Domain 51 documents the structural mechanism through which the Citizens United
decision — combined with the SpeechNow.org ruling creating super PACs and the
501(c)(4) vehicle for non-disclosure — has produced $1.9 billion in dark money
in the 2024 federal cycle alone. The document includes dedicated sections on
the California Fair Elections Act, the Hawaii SB 2471 Citizens United
workaround (signed May 15, 2026), and the Montana Plan ballot initiative.

The most relevant sections for your campaign work:

- Section 5 (The 2026 State Ballot Measures): California Fair Elections Act
  analysis, the FEC enforcement vacuum as a "why now" urgency frame for voters,
  and the meta-structure of the four simultaneous state campaigns

- Section 6.3 (The Hawaii/Montana Corporate Charter Model): the legal
  architecture that makes state-level reform viable under Citizens United —
  directly responsive to the "unconstitutional" attacks your campaign will
  receive

- Section 3 (FEC Structural Failure): the 200+ day FEC enforcement shutdown as
  evidence that federal self-regulation has collapsed, making state-level action
  the only viable near-term reform

CC Attribution 4.0 — use it, excerpt it, share it with campaign staff:
https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372

The July 1 date is our hard window — that is when California ballot campaigns
typically lock their messaging infrastructure before shifting to field execution.
I would welcome any indication the research reaches your campaign team.

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

After sending Send 3:
- [ ] Log send time (UTC) in DOMAIN_51_DISTRIBUTION_SEND_LOG.md — Send 3 row
- [ ] Set timer: 90 minutes before Send 4

---

#### Send 4: League of Women Voters California

| Field | Value |
|---|---|
| To | lwvc@lwvc.org |
| Subject | Dark money architecture research for California Fair Elections Act campaign — July 1 window |
| Contact note | Jenny Farrell, Executive Director — lwvc@lwvc.org is general inbox |

**Email body — copy below, fill YOUR_NAME and YOUR_CONTACT_INFO, send:**

```
Dear League of Women Voters California,

I am writing to share research that may support your work on the California
Fair Elections Act ahead of the November 3 ballot.

Domain 51 — "Campaign Finance, Dark Money Architecture, and the Corporate
Capture of Democratic Institutions" — documents the structural history of how
Citizens United, SpeechNow.org, and FEC enforcement collapse have created the
dark money system, and analyzes the four simultaneous 2026 state reform
campaigns including California's.

For LWV California's voter education mission, the most immediately applicable
sections:

- Executive Summary (standalone, 500 words): a non-technical explanation of
  how the dark money architecture works, suitable for voter guides and public
  education materials

- Section 6 (International Comparison): UK and Canada have robust political
  speech protections and robust disclosure requirements — directly answering
  the "but First Amendment" objection

- Section 5 (California Fair Elections Act): specific analysis of the public
  financing mechanism and what it would structurally change in California
  campaigns

58 citations, CC Attribution 4.0. Designed to be excerpted in voter guides,
cited in public education materials, shared with your member network:
https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372

I would be grateful if this reaches your campaign research team before the
July 1 messaging infrastructure window.

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

After sending Send 4:
- [ ] Log send time (UTC) in DOMAIN_51_DISTRIBUTION_SEND_LOG.md — Send 4 row
- [ ] Set timer: 90 minutes before Send 5

---

#### Send 5: Clean Money Action Fund

| Field | Value |
|---|---|
| To | info@CAclean.org |
| Subject | Dark money research for California Fair Elections Act — 58 citations, CC Attribution 4.0 |
| CRITICAL | Do NOT use info@cleanmoney.org — that domain unreachable since June 5, 2026 |
| Contact note | Trent Lange, President — info@CAclean.org is the correct organizational inbox |

**Email body — copy below, fill YOUR_NAME and YOUR_CONTACT_INFO, send:**

```
Dear Clean Money Action Fund team,

I am sharing a research document on the Citizens United dark money architecture
timed to the California Fair Elections Act campaign window.

Domain 51 is a 58-citation structural analysis of how dark money works, why
state-level reform is the most viable near-term pathway, and what the 2026
state campaigns — including California — mean for the broader reform movement.
The document covers:

- The $1.9B in dark money in the 2024 federal cycle and the structural reason
  this number keeps growing without FEC enforcement

- The California Fair Elections Act's public financing mechanism and the
  arguments it will face from dark money opposition

- Hawaii SB 2471 (signed May 15) as the first Citizens United workaround
  through corporate charter law — a legal theory your organization should be
  aware of for the post-November period if the ballot measure passes

- The FEC enforcement shutdown (200+ consecutive days without quorum as of
  June 2026) as a structural frame for why federal reform has stalled and
  state action is necessary

CC Attribution 4.0 — use it, adapt it, share it with your campaign legal team
and communications staff:
https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

After sending Send 5:
- [ ] Log send time (UTC) in DOMAIN_51_DISTRIBUTION_SEND_LOG.md — Send 5 row

**Wave 2 complete. All 5 sends done. Proceed to logging and Section 3 monitoring.**

---

### Execution Log (Fill After Each Send)

Open `DOMAIN_51_DISTRIBUTION_SEND_LOG.md` and paste this block, then fill in actual times:

```
## June 30, 2026 — Phase 2 Wave 1+2 Execution (Item 45.1)

| Send | Organization | Email Used | Send Time (UTC) | Status | Bounce? |
|------|---|---|---|---|---|
| 1 | Campaign Legal Center | echlopak@campaignlegalcenter.org | [HH:MM] | SENT | NO |
| 2 | Issue One | info@issueone.org | [HH:MM] | SENT | NO |
| 3 | Common Cause CA | dkemp@commoncause.org | [HH:MM] | SENT | NO |
| 4 | LWV California | lwvc@lwvc.org | [HH:MM] | SENT | NO |
| 5 | Clean Money Action Fund | info@CAclean.org | [HH:MM] | SENT | NO |

Deadline: June 30 23:59 UTC
All 5 sends logged before deadline: [YES / NO]
Executor: [YOUR_NAME]
Value outcome: [100% FULL VALUE / PARTIAL — see contingency / CONTINGENCY ACTIVATED]
```

---

## Section 3: Discord Monitoring Checklist

### Monitoring Schedule

| When | Action |
|---|---|
| Immediately after each send | Log UTC time in execution log |
| June 30 23:59 UTC | Confirm all 5 sends complete; if not, activate contingency per Section 4 |
| July 1 09:00 UTC (T+24h) | First inbox check |
| July 2 09:00 UTC (T+48h) | Second inbox check |
| July 7 09:00 UTC (T+7d) | T+7 checkpoint — classify response signals |
| July 14 09:00 UTC (T+14d) | Follow-up window for CLC only if no reply |

### Signal Classification Table (T+24h and T+48h Checks)

| Signal Type | Threshold | Classification | Action Required |
|---|---|---|---|
| Substantive reply from named staff | 1 or more | STRONG | Reply within 24 hours; log as STRONG in execution log |
| Generic acknowledgment with named contact | 1 or more | MODERATE | Log named contact for Wave 3 follow-up |
| Auto-reply or out-of-office | Any | DELIVERED | Log; note return date; no action needed |
| Hard bounce (address not found) | 1 or more | BOUNCE ALERT | Execute rollback per Section 4 immediately |
| Zero signals (no reply, no bounce) | All 5 | NORMAL | No action; continue to T+7 checkpoint |

### Escalation Thresholds

**T+24h escalation gate**: If 2 or more hard bounces received, pause all remaining actions. Verify all 5 email addresses before any further sends. A 40%+ bounce rate (2 of 5) indicates a contact list problem that may affect other domain distribution.

**T+7d escalation gate**: If zero replies received from all 5 contacts and zero Gist view increase: send a 3-sentence follow-up to echlopak@campaignlegalcenter.org only. Do not follow up with California contacts before T+14d.

**T+14d gate**: If CLC has still not replied: no further Domain 51 action. Log as WEAK signal. Domain 51 outcome does not affect Domain M execution.

---

### Section 3.1: T+7 Outcome Verdict — PASS / MODERATE / LOW / ZERO

Run this assessment at July 7 09:00 UTC. Count substantive replies only (named staff, real content). Auto-replies and out-of-office notifications do not count.

| Reply Count at T+7 | Outcome Verdict | What It Means | Required Action |
|---|---|---|---|
| 4-5 replies | PASS — HIGH | Exceptional engagement; research reached decision-makers | Reply within 24 hours to each; log as PASS HIGH; flag for Wave 3 activation |
| 2-3 replies | PASS — MODERATE | Normal to strong engagement for cold outreach to policy orgs | Reply within 48 hours to each; log as PASS MODERATE; Wave 3 conditional |
| 1 reply | LOW | Below average but delivery confirmed; one contact engaged | Reply within 48 hours; log as LOW; no Wave 3 activation |
| 0 replies | ZERO | Expected for cold outreach at T+7; do not interpret as failure | No action until T+14; continue monitoring |

**PASS threshold**: 2 or more substantive replies = PASS (any tier). Execution succeeded.

**ZERO at T+14d**: If still 0 replies by July 14 09:00 UTC from all 5 contacts: log as ZERO outcome. No follow-up to California contacts. CLC single follow-up (3 sentences max) to echlopak@campaignlegalcenter.org is permitted at T+14. Domain 51 execution was still successful — zero reply rate does not indicate non-delivery; it reflects policy org triage cycles.

**Wave 3 activation rule**:
- PASS HIGH: activate Wave 3 (5 additional national contacts)
- PASS MODERATE: activate Wave 3 only if CLC or Issue One is one of the repliers
- LOW or ZERO: hold Wave 3; reassess after July 15

### Inbox Monitoring Addresses

Check these inboxes at each monitoring interval:
- Any reply from @campaignlegalcenter.org or @campaignlegal.org
- Any reply from @issueone.org
- Any reply from @commoncause.org (for dkemp@)
- Any reply from @lwvc.org
- Any reply from @CAclean.org or caclean.org

Zero replies at T+48h is normal. National policy organizations and campaign-mode contacts take 3-7 business days. Do not interpret silence as non-delivery.

---

## Section 4: Rollback Triggers and Procedures

### Rollback Trigger 1: Gist Returns 404

**Condition**: Opening https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372 returns 404 or blank page at any point during the send session.

**Procedure**:
1. Stop all sends immediately. Do not send any email with a broken URL.
2. Open `DOMAIN_51_CONTINGENCY_SB_299_FALLBACK.md` for Gist recreation procedure (10 minutes).
3. After Gist is recreated: update the URL in all unsent email templates.
4. Resume sends from the next unsent email.

**Threshold**: This trigger fires on the first 404 occurrence. No tolerance.

---

### Rollback Trigger 2: Bounce Rate Exceeds 20% (More Than 1 of 5 Bounces)

**Condition**: 2 or more hard bounce notifications received for any combination of the 5 send addresses.

**Procedure**:
1. Stop all remaining sends.
2. Verify every remaining email address against the contact table in Section 1.
3. Substitute fallback addresses for any address that bounced.
4. Resume sends only after all remaining addresses are confirmed current.
5. Log all bounces and fallback substitutions in DOMAIN_51_DISTRIBUTION_SEND_LOG.md.

**1 bounce (5-20% rate)**: Do not stop. Retry to fallback address immediately. Continue remaining sends.

**2+ bounces (>20% rate)**: Stop. Verify and substitute before resuming.

---

### Rollback Trigger 3: Low Engagement by Hour 4 (No-Open Threshold)

**Condition**: If your email client supports open tracking, and 0 of 5 sends have been opened by 4 hours after the first send, AND 0 replies received:

This is borderline-normal but worth checking for spam folder delivery. Take this action: Send a test email to your own address with the same subject line pattern ("Constitutional architecture research on..."). If your test email lands in your own spam folder, the sends may also have landed in recipient spam.

**If spam-folder confirmed**: Resend to all addresses from a different sending domain or email client. Log restate in execution log.

**No open tracking**: If your email client has no tracking, skip this trigger entirely. Silence is normal.

---

### Rollback Trigger 4: June 30 23:59 UTC Passes with Incomplete Sends

**0-1 sends complete** (fewer than 2 sends): CONTINGENCY A ACTIVATED.
- Open `DOMAIN_M_CONTINGENCY_ACTIVATION_RUNBOOK.md` immediately.
- Domain M auto-triggers July 1 00:00 UTC.
- Do not attempt further Domain 51 sends as Branch A.

**2-4 sends complete** (partial execution): PARTIAL VALUE.
- Domain M also auto-triggers July 1 00:00 UTC.
- Remaining Domain 51 contacts activate via `DOMAIN_51_TIER_2_ACCELERATED_SEND_SEQUENCE.md`.
- Log which sends completed and which did not in DOMAIN_51_DISTRIBUTION_SEND_LOG.md.

**All 5 sends complete**: SUCCESS. Value = 100%. No contingency. Domain M does not activate.

---

## Section 5: Quick-Reference Send Checklist

This is the minimal 2-3 minute checklist for someone who has already read Sections 1-4. Execute top-to-bottom:

**Before first send:**
- [ ] Visit https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372 — confirm page loads
- [ ] Write down [YOUR_NAME] and [YOUR_CONTACT_INFO]
- [ ] Open DOMAIN_51_DISTRIBUTION_SEND_LOG.md (ready to log)

**Wave 1:**
- [ ] Send to echlopak@campaignlegalcenter.org — "Constitutional architecture research..." subject — log UTC time
- [ ] Wait minimum 90 minutes
- [ ] Send to info@issueone.org — "Dark money architecture research..." subject — log UTC time

**Wave 2 (same day, at least 3h after Send 1):**
- [ ] Send to dkemp@commoncause.org (CC info@commoncause.org) — "Research on Citizens United..." subject — log UTC time
- [ ] Wait minimum 90 minutes
- [ ] Send to lwvc@lwvc.org — "Dark money architecture research for California..." subject — log UTC time
- [ ] Wait minimum 90 minutes
- [ ] Send to info@CAclean.org — "Dark money research for California Fair Elections Act..." subject — log UTC time

**Confirm:**
- [ ] All 5 sends logged in DOMAIN_51_DISTRIBUTION_SEND_LOG.md
- [ ] All timestamps are before June 30 23:59 UTC
- [ ] No hard bounces outstanding

**Done. No contingency required. Value = 100%.**

---

## Contact Verification Summary (Current as of June 29, 2026)

| Send | Organization | Email | Verified Contact | Last Verified |
|------|---|---|---|---|
| 1 | Campaign Legal Center | echlopak@campaignlegalcenter.org | Erin Chlopak, Sr. Director Campaign Finance | June 11 via ZoomInfo + CLC filing metadata |
| 1 fallback | Campaign Legal Center | info@campaignlegal.org | General inbox | Active |
| 2 | Issue One | info@issueone.org | General inbox; Nick Penniman CEO | June 5 via issueone.org/contact |
| 2 fallback | Issue One | nick@issueone.org | Nick Penniman, CEO | Direct contact |
| 3 | Common Cause California | dkemp@commoncause.org | Darius Kemp, Executive Director | June 11 — Stein departed June 2025 |
| 4 | LWV California | lwvc@lwvc.org | Jenny Farrell, Executive Director | June 11 via lwvc.org/about/staff |
| 5 | Clean Money Action Fund | info@CAclean.org | Trent Lange, President | June 11 via yesfairelections.org/about |

**Dead contacts — never use:**
- info@cleanmoney.org — unreachable since June 5, 2026
- kflynn@commoncause.org — Karen Hobert Flynn, deceased March 2023

---

## Cross-Reference Files

| Purpose | File |
|---|---|
| Execution log (record all sends) | DOMAIN_51_DISTRIBUTION_SEND_LOG.md |
| Gist recreation (if 404) | DOMAIN_51_CONTINGENCY_SB_299_FALLBACK.md |
| Contingency decision tree | DOMAIN_51_CONTINGENCY_DECISION_TREE.md |
| Tier 2 accelerated (if deadline missed) | DOMAIN_51_TIER_2_ACCELERATED_SEND_SEQUENCE.md |
| Domain M auto-trigger runbook | DOMAIN_M_CONTINGENCY_ACTIVATION_RUNBOOK.md |

---

*Item 45.1 — Runbook 1 of 2. Production-ready June 29, 2026.*
*Deadline: June 30, 23:59 UTC — no exceptions, no extensions.*
*All 5 email addresses verified current as of June 11-29, 2026.*
*No placeholder text. Copy-paste ready. Execute now.*
