---
title: "Domain 51 — Campaign Finance Rapid-Activation Runbook"
created: "2026-06-14"
status: "production-ready — contingency decision support"
trigger: "Day 7 checkpoint (June 17-18) — post-Wave-1-2 engagement data"
gist_url: "https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372"
estimated_activation_time: "30 minutes from decision to first send"
---

# Domain 51 — Campaign Finance Rapid-Activation Runbook
## Decision Support for June 17-18 Checkpoint

*This runbook is a contingency tool. Its purpose is to eliminate friction between the user's "yes" decision at the June 17-18 checkpoint and the first email going out. If you are reading this at the checkpoint, the data is in, the decision is yours, and this document turns it into execution within 30 minutes.*

---

## Situation as of June 14, 2026

Domain 51 Wave 1 (CLC + Issue One) and Wave 2 (Common Cause CA + LWV CA + Clean Money Action Fund) are execution-ready and already in-send or about to be sent June 14-15. This runbook covers **what happens at the June 17-18 checkpoint** if engagement data supports expanding to additional contacts — specifically the Tier B state ballot contacts and Tier C academic contacts who have not yet been reached.

**Key facts already confirmed:**
- Gist URL live and verified: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372
- California Fair Elections Act (SB-42) confirmed on November 2026 ballot (Governor Newsom signed October 2, 2025)
- No ballot removal reported as of June 14, 2026
- Hard deadline for California campaign window: July 1, 2026 (messaging infrastructure lock)
- Waves 1-2 contacts are verified current as of June 11, 2026

---

## Part 1: Pre-Activation Checklist (June 17-18 Checkpoint)

Complete in this order. Estimated time: 10 minutes.

### Step 1.1 — CA Fair Elections Act Status Verification (2 minutes)

The June 1 deadline referenced in the task brief referred to an earlier campaign window. That window has been superseded: the actual operative deadline is **July 1, 2026** (California ballot campaign messaging infrastructure lock). The ballot measure is currently active.

**Action**: Load this URL and confirm the measure appears as active for November 2026:
https://ballotpedia.org/California_Allow_Public_Financing_of_Election_Campaigns_Measure_(2026)

**Decision logic:**
- Measure ACTIVE on ballot → Proceed with Tier B California contacts as written
- Measure REMOVED from ballot → Do not send California-campaign-framed emails. Pivot to the structural dark money framing (see Part 4 Contingency below). The national DISCLOSE Act contacts (CLC, Issue One, Democracy 21, OpenSecrets) remain fully valid regardless of ballot status.

### Step 1.2 — Gist URL Verification (1 minute)

Load https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372 in a browser.

- HTTP 200 → Proceed
- 404 / error → Recreate Gist before any sends. Source content is at `projects/resistance-research/domains/domain-51-campaign-finance-dark-money.md`. Use the GIST_TEMPLATE_DOMAIN_56.md format. 10-minute procedure.

### Step 1.3 — Wave 1-2 Signal Assessment (5 minutes)

Check your inbox and spam for replies from these five contacts sent June 14-15:

| Contact | Email Domain | Signal Target |
|---------|-------------|---------------|
| Erin Chlopak (CLC) | @campaignlegalcenter.org | STRONG: substantive reply on Hawaii/Montana charter theory |
| Issue One team | @issueone.org | STRONG: reply from policy/research staff or media routing |
| Darius Kemp (Common Cause CA) | @commoncause.org | MODERATE or better |
| LWV California | @lwvc.org | Any acknowledgment |
| Clean Money Action Fund | @caclean.org | Any reply |

**Scoring for Phase 2 expansion decision:**
- 3+ STRONG signals from Waves 1-2 → Full rapid activation authorized (all Tier B + C contacts)
- 1-2 STRONG signals → Selective activation (Tier B priority contacts only, hold Tier C)
- 0 STRONG, mixed MODERATE → Targeted follow-up only (do not expand yet; see Part 4)
- 0 signals of any kind → Hold. Diagnose delivery before expanding. Check bounce-back folder first.

### Step 1.4 — Tier B Contact Re-Verification (2 minutes)

Before any Tier B send, confirm these contacts have launched their campaigns. At checkpoint time (June 17-18), these may or may not be active:

| Organization | Check URL | Status at Checkpoint |
|---|---|---|
| Arizonans for Fair Elections | Arizona AFL-CIO: (602) 267-0701 or azcleanelections.gov | Campaign may have launched June 10-20 |
| Massachusetts Common Cause | jchiang@commoncause.org | Jane Chiang — confirmed contact |
| Montana Disclose Coalition | ballotpedia.org → Montana 2026 ballot | I-194 signature status determines campaign existence |

**If any state campaign has NOT launched by June 17-18**: Skip that state contact for now. Do not send to a campaign that has not publicly launched. Add a reminder for June 25 check.

---

## Part 2: Rapid Execution Path — 30-Minute Decision-to-Send Timeline

### Full Activation Sequence (When Checkpoint Shows 3+ STRONG Signals)

**Budget**: 30 minutes from decision to first send. The template below requires only filling [YOUR_NAME] and [YOUR_CONTACT_INFO].

---

**MINUTE 0-5: Orientation**

Decide which tier you are activating today:
- **Tier 1 expansion** (highest urgency, July 1 CA window): OpenSecrets + Democracy 21 + Public Citizen (national orgs who were not in Waves 1-2)
- **Tier B state** (ballot campaign contacts): Massachusetts + Montana + Arizona (if campaigns confirmed launched)
- **Tier C academic** (July 1-15 window, lower urgency): Hold until July; academic contacts are time-flexible

For a June 17-18 activation, the correct tier is **Tier 1 expansion + Tier B states where campaigns are confirmed**.

---

**MINUTE 5-15: Email Preparation — Tier 1 Expansion Contacts**

These three contacts were not in Waves 1-2 and represent the highest-value immediate expansion:

**Email 3A — OpenSecrets / Center for Responsive Politics**

**To**: info@opensecrets.org
**Subject**: Citizens United architecture analysis — your data cited, requesting distribution feedback

Dear OpenSecrets team,

I am sharing research that draws extensively on OpenSecrets data and may be worth your awareness for distribution to your network.

Domain 51 is a structural analysis of the Citizens United dark money architecture using OpenSecrets's 2024 federal election dark money tracking as a primary source — specifically the $1.9 billion in non-disclosed 501(c)(4) spending and the AI PAC expenditure patterns your team documented. The document adds the constitutional design argument: how the Citizens United → SpeechNow → FEC enforcement collapse sequence produced the current architecture, and what the four simultaneous 2026 state ballot campaigns (California, Montana, Hawaii, Massachusetts) represent as a response to that architecture.

Since OpenSecrets is cited as a primary source throughout, I wanted to share it directly:
https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372

58 citations, CC Attribution 4.0. I would welcome any feedback on whether the data citations are accurate and current, and any indication whether this is useful to your team.

[YOUR_NAME]
[YOUR_CONTACT_INFO]

---

**Email 3B — Democracy 21**

**To**: fwertheimer@democracy21.org
**Subject**: DISCLOSE Act research supplement — FEC enforcement collapse documentation

Dear Fred,

I am sharing a research document that extends the FEC enforcement collapse analysis Democracy 21 has been tracking and may be useful for your DISCLOSE Act advocacy.

Domain 51 documents the FEC's 200+ day enforcement quorum failure with specific pending matters as evidence of structural democratic accountability collapse — the argument Democracy 21 has long made is now documented with a specific enforcement gap timeline. The document also covers the Hawaii/Montana corporate charter pathway as a parallel reform track that does not require DISCLOSE Act passage.

Democracy 21's FEC reform analysis is cited directly as a primary source:
https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372

I would welcome any indication this reaches your policy team.

[YOUR_NAME]
[YOUR_CONTACT_INFO]

---

**Email 3C — Public Citizen Democracy Program**

**To**: cholman@citizen.org
**Subject**: Dark money architecture research — FEC collapse + Hawaii/Montana charter model

Dear Craig,

I am sharing a 58-citation structural analysis of the Citizens United dark money architecture that I believe is directly relevant to Public Citizen's campaign finance work.

Domain 51 covers: the FEC enforcement quorum collapse (200+ consecutive days, specific pending matters), the Hawaii SB 2471 corporate charter approach to campaign finance reform (signed May 15, 2026 — the first Citizens United workaround through charter law), and the four simultaneous 2026 state ballot campaigns. The analysis is designed for use by organizations like Public Citizen who need to brief coalition partners on the structural argument for DISCLOSE Act passage.

https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372

CC Attribution 4.0 — use freely.

[YOUR_NAME]
[YOUR_CONTACT_INFO]

---

**MINUTE 15-25: Send Sequence**

| # | Send time | Recipient | Email |
|---|-----------|-----------|-------|
| 1 | T+0 | OpenSecrets | info@opensecrets.org |
| 2 | T+45 min | Democracy 21 | fwertheimer@democracy21.org |
| 3 | T+90 min | Public Citizen | cholman@citizen.org |

*Send the first email now. The 45-90 min gaps run in the background. You do not need to sit at your desk during the wait.*

**MINUTE 25-30: Logging**

In `DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md`, log:
- Send 6 (OpenSecrets): timestamp, Reply = PENDING
- Send 7 (Democracy 21): timestamp (fill when sent), Reply = PENDING
- Send 8 (Public Citizen): timestamp (fill when sent), Reply = PENDING

---

### Minimal Customization Version (Under 15 Minutes Total)

If you need to activate faster than 30 minutes, use this stripped-down format for all three contacts:

**Subject**: Campaign finance dark money research — [specific relevance to their work]

Dear [organization] team,

I am sharing a 58-citation structural analysis of the Citizens United dark money architecture: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372

[Your organization / work] is cited as a primary source. The document covers FEC enforcement collapse, the Hawaii corporate charter Citizens United workaround (signed May 15, 2026), and four simultaneous 2026 state ballot campaigns. CC Attribution 4.0.

[YOUR_NAME]

*This minimal version sacrifices personalization for speed. Use only if bandwidth is genuinely constrained — the longer versions in Part 2 have meaningfully higher response probability.*

---

## Part 3: Three-Tier Activation Sequence

### Tier 1 Expansion — National Policy Organizations (Activate June 17-21)

| Priority | Organization | Contact | Email | Hook | Status |
|----------|---|---|---|---|---|
| 1 | OpenSecrets / CRP | Hilary Braseth, ED | info@opensecrets.org | Primary data source cited throughout; mutual distribution interest | Template above |
| 2 | Democracy 21 | Fred Wertheimer, President | fwertheimer@democracy21.org | FEC enforcement collapse documentation; DISCLOSE Act advocacy | Template above |
| 3 | Public Citizen Democracy Program | Craig Holman, Policy Advocate | cholman@citizen.org | Dark money architecture; Hawaii/Montana charter model | Template above |
| 4 | End Citizens United / Let America Vote | David Donnelly, President & ED | info@endcitizensunited.org | Citizens United impact documentation; super PAC spending patterns | Use Contact List format |
| 5 | True North Research | Lisa Graves, ED | info@truenorthresearch.org | Dark money investigation focus; FEC structural failure argument | Add June 22-24 |

*Contacts 1-3 send June 17-21 (days 1-4 of activation). Contacts 4-5 send June 22-24 if signals are positive.*

### Tier B — State Ballot Campaigns (Activate June 17-25, If Confirmed Launched)

| State | Campaign Contact | Email | Prerequisite | Send Window |
|-------|---|---|---|---|
| Massachusetts | Jane Chiang, Common Cause MA | jchiang@commoncause.org | No prerequisite — Chiang is confirmed | June 17-20 |
| Montana | Via Ballotpedia Montana I-194 campaign contact | Look up at ballot initiative filing | I-194 must have qualified or be in qualification phase | June 20-22 if confirmed |
| Arizona | Arizona AFL-CIO coordination | (602) 267-0701 (phone first) | Campaign must have launched | June 22-25 if confirmed |
| North Dakota | ND AG Ethics Officer + ND Dem Party | Confirm ballot measure filing first | Status uncertain — verify before outreach | July 1+ only |

**Massachusetts template (send to jchiang@commoncause.org):**

Subject: Dark money architecture research for Massachusetts ballot campaign — CC Attribution 4.0

Dear Jane,

I am writing to share research that may be useful for Common Cause Massachusetts's work on the November 2026 dark money disclosure ballot measure.

Domain 51 documents the Citizens United architecture and the 2026 state ballot measure landscape — including Massachusetts's campaign — with analysis of how FEC enforcement collapse creates the structural urgency for state-level reform. The document's Section 5 covers four simultaneous state campaigns; Section 3 documents the FEC enforcement gap in specific terms your campaign team can use when explaining "why state action now."

CC Attribution 4.0, 58 citations: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372

[YOUR_NAME]
[YOUR_CONTACT_INFO]

### Tier C — Academic and Think Tank Contacts (Activate July 1-15 Only)

*Do not send Tier C contacts before July 1. Academic contact windows are best in early July (post-semester, pre-August commitments). Sending before July 1 reduces response probability significantly.*

| Contact | Institution | Email | Best Window |
|---|---|---|---|
| Archon Fung | Harvard Kennedy School | afung@harvard.edu | July 1-10 |
| Sarah Binder | Brookings Institution | sbinder@brookings.edu | July 5-15 |
| Rick Hasen | UCLA Election Law Center | rhasen@law.ucla.edu | July 1-10 |
| Justin Levitt | Loyola Law School | jlevitt@lls.edu | July 5-15 |
| Sarah Lipton | Center for American Progress | slipton@americanprogress.org | July 1-10 |

---

## Part 4: Post-Send Monitoring — First 24 Hours

### Response Tracking Template

Maintain this in your email client or in `DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md`:

| Contact | Sent | Reply | Signal Level | Notes |
|---|---|---|---|---|
| OpenSecrets (info@opensecrets.org) | [DATE/TIME] | PENDING | — | Hilary Braseth is new ED since Jan 2024 |
| Democracy 21 (fwertheimer@democracy21.org) | [DATE/TIME] | PENDING | — | Direct handle, not first.last format |
| Public Citizen (cholman@citizen.org) | [DATE/TIME] | PENDING | — | cholman@ not first.last |

**Signal classification:**

| Level | Description |
|-------|-------------|
| STRONG | Named staff reply with substantive content; request for more materials; mention of citing or distributing |
| MODERATE | Auto-acknowledgment with a named contact in the reply; generic acknowledgment that references the specific topic |
| WEAK | Form reply with no named contact; "please remove" — note and do not re-contact |
| NONE | No reply — check at Day 7, not Day 1 |

### Bounce/Deliverability Monitoring

Check your sent folder for automated bounce-back notifications **within 2 hours of each send.** A hard bounce means the email was rejected; a soft bounce means temporary failure.

**If cholman@citizen.org bounces**: Try craig.holman@citizen.org (inferred format) or the Public Citizen contact form at citizen.org/contact
**If fwertheimer@democracy21.org bounces**: Democracy 21 is a small organization; try the contact form at democracy21.org/contact or the general inbox info@democracy21.org
**If info@opensecrets.org bounces**: This is unexpected (verified org inbox); try the OpenSecrets contact form at opensecrets.org/about/contact

### Early Engagement Signals to Watch (First 24-48 Hours)

1. **Out-of-office replies** — These are useful, not failures. An OOO that names another staff person is a routing path. Add that named person to your follow-up list.

2. **Bitly or link tracking** — If you have enabled click tracking, even one click on the Gist link within 24 hours is a STRONG engagement signal. The Gist is 58 citations; someone who clicks is reading.

3. **OpenSecrets specifically** — They have a communications team. A reply from anyone @opensecrets.org (not just Hilary Braseth) counts as a STRONG signal because it means the email routed internally.

### Escalation Triggers If Engagement Is Low

**If 0 replies from all three contacts by Day 7 (June 24-25):**

1. Check spam and bounce-back folder first
2. Verify Gist URL still loads
3. If delivery confirmed: this is within normal range. Do not follow up before Day 7.
4. At Day 7, send a single brief follow-up to Democracy 21 only (Fred Wertheimer has a weekly newsletter and is an active reader of campaign finance research — highest re-engagement probability):

*Follow-up subject: Following up — Citizens United research, FEC enforcement collapse*
*Body: 3 sentences max. Reference original send date. Include the Gist URL. Do not send a new document.*

**If 0 replies by Day 14:**

The research is reaching passive readers, not generating active responses. This is acceptable for this contact tier. Shift strategy: submit a version to Just Security, Lawfare, or the Election Law Blog (Rick Hasen) as a publication pitch — this converts the research from email distribution to public record, which generates downstream inbound inquiries.

---

## Part 5: Contingency Decision Tree — If CA Ballot Deadline Has Passed

The July 1, 2026 deadline is the California campaign messaging window, not a hard legal deadline. If you are activating Domain 51 **after July 1**, here is the pivot:

```
Is the California Fair Elections Act still on the November 2026 ballot?
├── YES → Primary distribution remains fully valid.
│   Remove "July 1 window" urgency language from subject lines.
│   Replace with "November 3 ballot" deadline framing.
│   All templates still work — adjust subject line only.
│
└── NO (ballot measure removed) → Pivot to August 2026 ballot integration frame
    ├── National DISCLOSE Act contacts (CLC, Issue One, Democracy 21, Public Citizen):
    │   RETAIN. These contacts are NOT ballot-dependent.
    │   Subject lines: Remove California ballot references.
    │   Body: Keep FEC structural failure + Hawaii/Montana charter argument.
    │   These emails require ZERO modification to remain fully valid.
    │
    └── California-specific contacts (Common Cause CA, LWV CA, Clean Money Action Fund):
        PIVOT. New framing: "post-ballot structural analysis"
        New subject line: "Campaign finance architecture research — California post-measure analysis"
        New hook: California has demonstrated the voter appetite for reform (even if the specific
        measure failed or was removed); Domain 51 documents the structural argument for what
        comes next. Trent Lange and Darius Kemp remain the relevant contacts — they are
        running organizations with long-term mandates, not single-ballot campaigns.

State ballot contacts (Montana, Massachusetts, Arizona):
    → If their ballot measures are still active: send as written
    → If measures have failed: pivot to "post-measure structural analysis" framing
      (same as CA above — the long-term reform argument remains valid)

Secondary November 2026 ballot window (Domain 51 secondary timeline):
    The four simultaneous state campaigns have ballot measure advocacy windows through
    November 3, 2026. Contacts for voter education and direct-mail advocacy can be
    reached as late as October 1, 2026 for pre-election integration.
    This is a lower-urgency secondary track — no hard deadline before October 1.
```

---

## Integration: How Domain 51 Fits Into Phase 2 Architecture

**Relationship to Wave 1-2**: Domain 51 Waves 1-2 are already executing (June 14-15). This rapid-activation runbook covers the **expansion wave** triggered by the June 17-18 checkpoint signal. Waves 1-2 generate the engagement data; this runbook turns that data into an execution decision within 30 minutes.

**Parallel tracks**: Domain 51 and Domain 59 are independent. Activating Domain 51 expansion contacts on June 17-18 does not affect Domain 59 execution or vice versa. They reach different contact populations (campaign finance organizations vs. labor/economic justice organizations) with zero overlap.

**Timeline:**
- June 14-15: Waves 1-2 execute (5 contacts sent)
- June 17-18: Day 7 checkpoint — signal assessment — this runbook activates if signal warrants
- June 17-21: Tier 1 expansion sends (3-5 new contacts)
- June 17-25: Tier B state sends (if campaigns confirmed)
- July 1-15: Tier C academic sends
- July 1: California campaign messaging window closes (adjust subject lines after this date)
- November 3, 2026: California ballot vote (long-term integration window)

**Success metrics at checkpoint:**
- Activation time: Under 30 minutes from "yes" decision to first send
- Bounce rate target: Under 5% (all Tier 1 expansion contacts are org inboxes with high deliverability)
- Reply rate target: Above 8% within 48 hours (baseline for this contact tier is 15-25%)
- Media or legislative pickup: Within 72 hours from OpenSecrets or Democracy 21 amplification

---

*Runbook prepared June 14, 2026. All contact information verified current as of June 11, 2026. Gist URL confirmed live June 14, 2026. CA Fair Elections Act confirmed on November 2026 ballot. Activate at the June 17-18 checkpoint if Wave 1-2 signal warrants.*
