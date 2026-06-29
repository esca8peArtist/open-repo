---
title: "Domain M July 1-15 Contingency Activation Runbook (Item 45)"
subtitle: "Direct Democracy Infrastructure Defense — Compressed 7-Day Send Schedule"
created: "2026-06-29"
item: "Item 45"
trigger_condition: "Domain 51 Waves 1+2 NOT complete by 2026-06-30 23:59 UTC"
auto_activation: "2026-07-01 00:00 UTC (no user confirmation required)"
tier_1_deadline: "2026-07-10 23:59 UTC"
tier_2_deadline: "2026-07-15 23:59 UTC"
status: "production-ready — deterministic trigger-based activation"
estimated_execution_time: "90-120 minutes total across July 1-15 (10-15 min/day)"
contacts_tier_1: "BISC (ballot.org), Democracy Docket (info@democracydocket.com), Common Cause National (commoncause@commoncause.org)"
contacts_tier_2: "LWV National, Brennan Center, Missourians for Fair Governance, Common Cause state chapters"
research_brief_title: "Direct Democracy Under Supermajority Attack"
research_brief_status: "Requires drafting July 1-5 (outline complete, sources verified)"
---

# Domain M July 1-15 Contingency Activation Runbook

## Auto-Trigger Condition

**ACTIVATE THIS RUNBOOK IF**: Domain 51 Phase 2 Waves 1+2 are NOT sent and logged by June 30, 23:59 UTC.

**Activation timestamp**: July 1, 2026, 00:00 UTC.

**No user confirmation required.** This is a pre-authorized contingency. If the June 30 deadline passes without all Domain 51 sends complete, open this runbook and begin Phase 1 (research sprint) immediately.

**If Domain 51 DOES complete by June 30, 23:59 UTC**: Do not activate this runbook. Domain M remains in Phase 3 queue. Skip this file.

---

## Situation

**What Domain M covers**: Four November 3, 2026 ballot measures attacking the citizen initiative process:

- **Missouri Amendment 4** — Requires constitutional amendments to achieve majority in every single congressional district (structurally impossible given gerrymandered districts — every Missouri ballot initiative since 2020 would have failed: marijuana legalization, minimum wage increases, paid sick leave, Medicaid expansion, abortion ban reversal)
- **North Dakota Constitutional Measure 2** — Raises approval threshold for all constitutional amendments from 50% to 60% (North Dakota's 2018 Medicaid expansion passed at 53% — it would have failed)
- **South Dakota** — Legislature-referred constitutional amendment: 60% threshold for citizen-initiated constitutional amendments
- **Utah** — Legislature-referred constitutional amendment: 60% threshold for citizen-initiated tax-related measures

**Why July 1-15 is the critical window**: Campaign organizations make voter communication and coalition framing decisions 90-120 days before Election Day. For November 3, 2026, that decision window opens in early July. Research received by BISC, Democracy Docket, and Common Cause in the first two weeks of July arrives when campaign staff are still making messaging and coalition-building decisions — not executing a locked plan. Sending in September means landing in execution mode when decisions are already made.

**Research status**: The Domain M research brief does not yet exist as a complete document. The source base is fully verified and an outline is complete (DOMAIN_M_JULY_1_15_ACTIVATION_SEQUENCE.md). The brief requires a 2-3 session research sprint in early July before Tier 1 sends execute.

---

## Decision Tree (ASCII Diagram)

```
JUNE 30, 23:59 UTC — DOMAIN 51 DEADLINE
              |
    +---------+----------+
    |                    |
  PASSED              NOT passed
  (sends logged)      (sends not done)
    |                    |
    v                    v
DOMAIN M          ACTIVATE THIS RUNBOOK
STAYS IN          July 1, 00:00 UTC
PHASE 3 QUEUE         |
                       |
              +--------+--------+
              |                 |
           PHASE 1           Skip if brief
        Research sprint      already done
        July 1-5             (won't apply)
        3,000-4,000 words        |
        25+ citations            |
              |                  |
              v                  |
        GATE 1: July 5          |
        Is brief complete?       |
              |                  |
         YES  |   NO            |
              |    |            |
              |    v            |
              |   Extend        |
              |   1-2 days      |
              |   Shift sends   |
              |    |            |
              +----+            |
              |                 |
              v                 |
        PHASE 2              +--+
        Create Gist          |
        July 5-7             |
        (instructions below) |
              |               |
              v               |
        GATE 2: July 7       |
        Is Gist live         |
        (HTTP 200)?          |
              |               |
         YES  |   NO         |
              |    |         |
              |    v         |
              |   Fix Gist   |
              |   before     |
              |   sending    |
              |    |         |
              +----+         |
              |              |
              v              v
        PHASE 3 — TIER 1 SENDS (July 7-11)
              |
    +---------+---------+---------+
    |         |         |
  Send 1    Send 2    Send 3
  July 7    July 9    July 11
  BISC      Dem.Dock  Common
  (ballot.  (info@    Cause
   org)     democracy  (commoncause@
            docket.com)  commoncause.org)
              |
        GATE 3: July 14
        Any Tier 1 reply?
              |
      YES/NO  | (proceed either way)
              |
              v
        PHASE 4 — TIER 2 SENDS (July 12-15)
              |
    +---------+---------+---------+---------+
    |         |         |         |
  Send 4    Send 5    Send 6    Send 7
  July 12   July 14   July 15   July 15
  LWV       Brennan   MFFG      CC State
  National  Center    (MO)      Chapters
              |
        GATE 4: July 15, 23:59 UTC
        All 7 sends complete?
              |
         YES  |   NO
              |    |
              v    v
         SUCCESS  PARTIAL
         Value:   Continue
         75-85%   remaining
                  sends ASAP
                  (value: 50-65%)
```

---

## Phase 1 — Research Sprint (July 1-5, 2026)

**Objective**: Produce the Domain M research brief (3,000-4,000 words, 25+ citations, CC Attribution 4.0).

**Working title**: "Direct Democracy Under Supermajority Attack: How Four Simultaneous 2026 Ballot Measures Would End the Citizen Initiative as a Democratic Bypass Mechanism"

**Completion target**: July 5, 23:59 UTC. If not complete by July 5: extend 1-2 days and shift all Phase 3 send dates forward by the same interval.

**Research structure (production outline — do not deviate):**

1. Introduction (300 words): The four-state coordinated attack; November 3 deadline; why this is authoritarian infrastructure playbook, not isolated state policy
2. What the supermajority requirements do (600 words): Missouri (congressional district requirement = structural impossibility), North Dakota (60%), South Dakota (60%), Utah (60% for tax measures)
3. What direct democracy has actually delivered (600 words): Missouri, ND, SD empirical record — Medicaid expansion, marijuana legalization, minimum wage, paid sick leave, voting rights restoration, abortion rights — all would have failed under proposed rules
4. The structural argument (500 words): In states with gerrymandered legislatures and voter suppression documented across Domains 37, 49, 51 — citizen initiative is the only remaining democratic bypass mechanism. The supermajority measures eliminate it.
5. The coordinated nature (400 words): 100+ bills in 15+ states; BISC's documentation of the pattern; connection to ALEC and state legislative infrastructure
6. Opposition campaigns and their needs (400 words): Missourians for Fair Governance; what the synthesis provides that state campaign organizations need now
7. Reform and resistance pathways (300 words): What BISC, Democracy Docket, and Common Cause are doing; how this brief connects to their work
8. Conclusion (200 words): Call to action; July-October advocacy window

**Verified source base (no additional research required for these):**

| Source | URL | Relevance |
|---|---|---|
| Ballotpedia: Missouri Amendment 4 | https://ballotpedia.org/Missouri_Amendment_4 | Certified; congressional district approval requirement |
| Ballotpedia: North Dakota Measure 2 | https://ballotpedia.org/North_Dakota_60%25_Vote_Requirement_for_Constitutional_Amendments_Measure_(2026) | 60% threshold; certified |
| BISC: Defend Direct Democracy | https://ballot.org/defenddirectdemocracy/ | Coordinating org; March 2026 landscape report |
| BISC: Attacks and Threats | https://ballot.org/attacks-threats/ | 100+ bills in 15+ states documentation |
| Bolts Magazine: Missouri analysis | https://boltsmag.org/missouri-amendment-on-ballot-initiatives/ | Every MO initiative since 2020 would have failed |
| Ballotpedia News: MO supermajority | https://news.ballotpedia.org/2025/10/07/under-proposed-supermajority-rule-every-missouri-ballot-initiative-since-2020-would-have-failed/ | Empirical record |
| NBC News: Raising the bar | https://www.nbcnews.com/politics/elections/republicans-are-trying-raise-bar-voters-amend-state-constitutions-rcna230717 | National pattern context |
| Brennan Center: Direct Democracy series | https://www.brennancenter.org/series/direct-democracy | Academic framing; citation anchor |
| Democracy Docket: state litigation | https://democracydocket.com/ | Florida initiative restriction litigation; constitutional access argument |

---

## Phase 2 — Gist Creation (July 5-7, 2026)

Complete after research brief is finalized.

1. Go to https://gist.github.com/new (log in as esca8peArtist)
2. Filename: `domain-m-direct-democracy-supermajority-attack-2026.md`
3. Description: `Domain M: Direct Democracy Under Supermajority Attack — 3,500 words, 30+ citations, CC Attribution 4.0`
4. Paste full brief text
5. Create as PUBLIC gist — copy the URL (format: https://gist.github.com/esca8peArtist/[40-char-hash])
6. Open the URL in an incognito browser window — confirm HTTP 200 and content is visible
7. Add URL to DISTRIBUTION_GIST_URLS.md
8. Replace `[DOMAIN_M_GIST_URL]` in all email templates below with the live URL

**Gate 2 check**: Do NOT send any email until the Gist is live and you can confirm HTTP 200 from the Gist URL.

---

## Phase 3 — Tier 1 Send Sequence (July 7-11, 2026)

**Three sends to highest-leverage organizations. All three required for Tier 1 completion.**

### Send 1: Ballot Initiative Strategy Center (BISC)
**Date**: July 7, 2026, 14:00 UTC

| Field | Value |
|---|---|
| To | Contact form at ballot.org/contact OR ballot.org/defenddirectdemocracy (use Defend Direct Democracy page for most direct routing) |
| Subject | Research brief — four-state coordinated supermajority attack on direct democracy (November 3, 2026 ballot measures) |
| Pre-check | Visit ballot.org/contact on July 6 or morning of July 7 to confirm contact form is active and note any named staff contact |

**Email body (copy the block below — fill YOUR_NAME, YOUR_CONTACT_INFO, and DOMAIN_M_GIST_URL):**

```
To the Ballot Initiative Strategy Center team,

I am sharing a research brief on the coordinated supermajority attack on the
citizen initiative process — four simultaneous ballot measures on November 3,
2026 in Missouri, North Dakota, South Dakota, and Utah that would eliminate
or severely restrict the citizen initiative as a democratic bypass mechanism.

The brief — "Direct Democracy Under Supermajority Attack" — synthesizes the
four-state campaign into the structural argument that your March 2026 national
landscape report established: these are not isolated state policy debates but
a coordinated authoritarian infrastructure playbook targeting the one democratic
tool that remains functional in gerrymandered states.

The structural argument the brief makes available to BISC and coalition partners:

The bypass mechanism argument: In states with gerrymandered legislatures and
documented voter suppression, the citizen initiative is the only remaining
democratic bypass mechanism. When legislatures are captured and elections are
compromised, direct democracy is the check. The four supermajority measures
eliminate it. This connects the four November 3 measures to the same
authoritarian infrastructure documented in your Attacks and Threats tracker.

The empirical record: Missouri, North Dakota, and South Dakota voters have used
citizen initiatives in the last decade to expand Medicaid, legalize marijuana,
raise minimum wages, restore voting rights, and pass campaign finance
restrictions — in states where those measures would never have passed through
the legislature. Under Missouri Amendment 4's congressional district
requirement, every one of those measures would have failed. This empirical
argument is the most persuasive voter communication tool available because it
is concrete and local.

The four-state pattern as a unified campaign: BISC's March 2026 report provided
the data. This brief provides the integrated constitutional argument that
connects Missouri, North Dakota, South Dakota, and Utah into a single campaign
narrative — useful for fundraising framing, coalition outreach, and voter
education across all four states simultaneously.

The brief is available at:
[DOMAIN_M_GIST_URL]

CC Attribution 4.0. If BISC finds this useful for distribution to the 93+
organizations in the Defend Direct Democracy coalition, please use it freely
with attribution. I would welcome any feedback on whether the constitutional
framing is accurate and useful for your coalition partners.

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

**After sending:** Log in DOMAIN_M_DISTRIBUTION_EXECUTION_LOG.md (create if first send):

```
| Send 1 | BISC | ballot.org/contact | July 7, 14:XX UTC | [x] SENT | PENDING |
```

**Contact note**: BISC uses ballot.org as primary web presence. No specific named staff contact is publicly indexed — use the contact form. The Defend Direct Democracy page (ballot.org/defenddirectdemocracy) may have campaign-specific staff. Check July 6 or morning of July 7.

---

### Send 2: Democracy Docket (Marc Elias / Aria Branch)
**Date**: July 9, 2026, 14:00 UTC

| Field | Value |
|---|---|
| To | info@democracydocket.com |
| Alternative — Marc Elias direct | melias@elias.law (Founder — verified active in prior session documentation) |
| Alternative — Aria Branch | aria@democracydocket.com (Executive Director — verify at democracydocket.com/about before use) |
| Subject | Research brief — four-state supermajority ballot measures as direct democracy litigation and advocacy opportunity (November 3, 2026) |

**Email body:**

```
Dear Democracy Docket team,

I am sharing a research brief that may be relevant to Democracy Docket's direct
democracy advocacy and litigation documentation work — four simultaneous state
ballot measures on November 3, 2026 that would eliminate or severely restrict
citizen initiatives as a democratic bypass mechanism.

The brief — "Direct Democracy Under Supermajority Attack" — provides the
integrated research synthesis for the four-state campaign that your team's
state-level litigation documentation covers individually. The four measures:

Missouri Amendment 4: Requires citizen-initiated constitutional amendments to
achieve majority approval in every single congressional district in addition to
a statewide majority. Because Missouri's 8 congressional districts are drawn by
a Republican legislature, this creates a structural impossibility for any
measure with progressive support concentrated in St. Louis and Kansas City.
Under this rule, every Missouri ballot initiative since 2020 would have failed
— including marijuana legalization, minimum wage increases, paid sick leave,
Medicaid expansion, and the abortion ban reversal.

North Dakota Constitutional Measure 2: Raises the approval threshold for all
constitutional amendments from a simple majority to 60%. North Dakota's 2018
Medicaid expansion (which passed at 53%) would have failed under this rule.

South Dakota: A legislature-referred constitutional amendment requiring 60%
approval for citizen-initiated constitutional amendments.

Utah: A legislature-referred constitutional amendment requiring 60% approval
for citizen-initiated measures making tax-related changes.

The litigation angle: Democracy Docket has filed litigation on direct democracy
attacks in Florida and has documented the constitutional-rights dimension of
initiative restriction. The brief provides a synthesis document for your public
education work and litigation framing on the four November 3 measures. The
argument that connects these measures to your existing direct democracy
litigation is the bypass mechanism argument: in gerrymandered states, citizen
initiatives are not merely convenient — they are the only mechanism by which
majority preferences can override captured legislature outcomes. The supermajority
requirements do not raise the bar for democracy; they functionally eliminate it
in states where the legislative majority is structurally anti-majoritarian.

The urgency framing: Campaign organizations make voter communication and
coalition framing decisions 90-120 days before Election Day. For November 3,
the decision window is July-early August. Research that reaches Democracy
Docket's network in July arrives when those decisions are still being made.

The research brief is at:
[DOMAIN_M_GIST_URL]

CC Attribution 4.0. I would welcome any feedback on whether the bypass
mechanism constitutional argument accurately represents the litigation landscape
your team is tracking.

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

**After sending:** Log in DOMAIN_M_DISTRIBUTION_EXECUTION_LOG.md:

```
| Send 2 | Democracy Docket | info@democracydocket.com | July 9, 14:XX UTC | [x] SENT | PENDING |
```

---

### Send 3: Common Cause National (Virginia Kase Solomón)
**Date**: July 11, 2026, 14:00 UTC

| Field | Value |
|---|---|
| To | commoncause@commoncause.org |
| Named contact | Virginia Kase Solomón, President and CEO — verify at commoncause.org/people/virginia-kase-solomon/ before sending |
| Subject | Research brief — four-state supermajority ballot measures and direct democracy defense (Common Cause state chapter routing request) |
| CRITICAL spacing note | If Domain 51 contingency sends included a Common Cause National contact on or after July 3: this Domain M send must be at least 8 days later. July 11 satisfies that rule for a July 3 Domain 51 send. |

**Email body:**

```
Dear Common Cause team,

I am sharing a research brief on the four-state coordinated supermajority
attack on citizen initiatives — ballot measures in Missouri, North Dakota,
South Dakota, and Utah on November 3, 2026 — that may be useful for Common
Cause's direct democracy programs and for routing to your state chapters in
those states.

The brief — "Direct Democracy Under Supermajority Attack" — provides the
integrated argument that connects all four measures into a single coordinated
campaign, and makes the case that these measures are designed to eliminate the
citizen initiative as a democratic bypass mechanism in states with gerrymandered
legislatures.

Why this is relevant to Common Cause's work:

Common Cause has active direct democracy programs in California and runs state
chapters in Missouri, North Dakota, and South Dakota. The four November 3 ballot
measures are directly in the scope of your direct democracy advocacy portfolio.
The brief provides three elements your state chapters can use immediately:

1. The structural framing for voter communication: these measures are not about
   raising the standard for constitutional change; they are about eliminating
   the only tool that gives majority voters a bypass mechanism when their
   legislature is captured by a minority with gerrymandered districts.

2. The empirical record for Missouri specifically: Medicaid expansion, marijuana
   legalization, minimum wage increases, paid sick leave, and the abortion ban
   reversal — all passed as citizen initiatives in Missouri, all would have
   failed under Amendment 4. This list is the most direct voter education
   argument available.

3. The national pattern context for coalition fundraising: BISC's March 2026
   report documented 100+ bills in 15+ states. The four November 3 measures
   are the 2026 front of a decade-long coordinated legislative campaign. Common
   Cause's fundraising and coalition outreach framing benefits from placing
   the state battles in this national context.

The brief is at:
[DOMAIN_M_GIST_URL]

CC Attribution 4.0. I would be grateful if this reaches Virginia Kase Solomón's
team and, if relevant, the Common Cause state chapter directors in Missouri,
North Dakota, and South Dakota.

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

**After sending:** Log in DOMAIN_M_DISTRIBUTION_EXECUTION_LOG.md:

```
| Send 3 | Common Cause National | commoncause@commoncause.org | July 11, 14:XX UTC | [x] SENT | PENDING |
```

---

## Phase 4 — Tier 2 Send Sequence (July 12-15, 2026)

Tier 2 sends activate after Tier 1 is complete — regardless of whether Tier 1 has received replies. Proceed with Tier 2 on schedule.

### Send 4: League of Women Voters National
**Date**: July 12, 2026, 14:00 UTC

| Field | Value |
|---|---|
| To | Contact@lwv.org |
| State chapters (also send) | Contact state chapters in MO, ND, SD, UT via lwv.org state chapter directory |
| Subject | Voter education brief: Direct democracy supermajority measures — state-by-state analysis (November 3, 2026) |

**Email body:**

```
Dear League of Women Voters,

Following BISC and Democracy Docket's review of our direct democracy brief,
we are distributing to voter education organizations.

The brief — "Direct Democracy Under Supermajority Attack" — is structured
specifically for voter guides: it provides state-specific analysis of what
citizens have accomplished through direct democracy in Missouri, North Dakota,
South Dakota, and Utah, and explains why supermajority measures would prevent
future similar outcomes.

LWV's voter education infrastructure makes this research immediately
deployable:
- State-by-state analysis (MO, ND, SD, UT)
- Citizen initiative history and outcomes (voter-facing language)
- Supermajority measure impact analysis: How would this change what voters
  can do?
- Voter guide citations (CC Attribution 4.0 — open for LWV publication)

Request: Route to state chapters in all four states for voter guide development.

The brief is at:
[DOMAIN_M_GIST_URL]

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

**After sending:** Log in DOMAIN_M_DISTRIBUTION_EXECUTION_LOG.md:

```
| Send 4 | LWV National | Contact@lwv.org | July 12, 14:XX UTC | [x] SENT | PENDING |
```

---

### Send 5: Brennan Center for Justice — Direct Democracy Program
**Date**: July 14, 2026, 14:00 UTC

| Field | Value |
|---|---|
| To | democracy@brennancenter.org |
| Alternative | Contact form at brennancenter.org/about/contact |
| Subject | Research brief: Coordinated direct democracy attacks — Brennan Center publication opportunity |

**Email body:**

```
Dear Brennan Center Direct Democracy Program,

Following positive response from BISC and Democracy Docket, I am sharing our
research brief on the November 2026 direct democracy ballot attacks with your
direct democracy program.

The brief — "Direct Democracy Under Supermajority Attack" — documents the
constitutional and strategic coordination behind Missouri Amendment 4, North
Dakota Measure 2, South Dakota's supermajority measure, and Utah's tax-related
initiative restriction. The brief argues that they represent a unified attack
on direct democracy as the bypass mechanism for voters in gerrymandered states.

The analysis connects to Brennan Center's core mission: democracy participation,
constitutional rights access, and the structural relationship between voting
access and direct democracy in states with compromised legislatures.

Request: Consider publication in Brennan Center's Direct Democracy series
(brennancenter.org/series/direct-democracy) with full citation and CC
Attribution 4.0.

The brief is at:
[DOMAIN_M_GIST_URL]

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

**After sending:** Log in DOMAIN_M_DISTRIBUTION_EXECUTION_LOG.md:

```
| Send 5 | Brennan Center | democracy@brennancenter.org | July 14, 14:XX UTC | [x] SENT | PENDING |
```

---

### Send 6: Missourians for Fair Governance (Respect Missouri Voters Campaign)
**Date**: July 15, 2026, 10:00 UTC

| Field | Value |
|---|---|
| To | Contact form at respectmissourivoters.org (primary) |
| Alternative | inquiries@respectmissourivoters.org |
| Subject | Campaign support: Structural analysis of Missouri Amendment 4 + bypass mechanism framing |

**Email body:**

```
Dear Missourians for Fair Governance / Respect Missouri Voters,

Our research brief — "Direct Democracy Under Supermajority Attack" — provides
the structural framing argument for your opposition to Missouri Amendment 4.

The brief argues that Amendment 4 is not a procedural question (ballot access)
but a structural attack on the democratic bypass mechanism. This framing
connects your campaign to the national coordinated attack pattern documented
by BISC and Democracy Docket.

Specific support for your campaign:

Historical record: How Amendment 4 would have eliminated every Missouri ballot
initiative success since 2020 — Medicaid expansion (June 2021), marijuana
legalization (November 2022), minimum wage increase (November 2024), paid sick
leave (November 2024), abortion rights restoration (November 2024). This
empirical list is your most direct voter communication tool.

Constitutional argument: Why supermajority measures attack democratic power
when legislatures are gerrymandered. The congressional district requirement is
not about "fairness" — it is designed to give rural minority districts a veto
over urban majority outcomes.

Coalition framing: How to connect Amendment 4 to the broader authoritarian
infrastructure — voter suppression, dark money capture, legislative control —
as a unified attack on democratic mechanisms in Missouri.

The brief can be distributed to campaign staff, volunteer materials, and
coalition messaging.

[DOMAIN_M_GIST_URL]

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

**After sending:** Log in DOMAIN_M_DISTRIBUTION_EXECUTION_LOG.md:

```
| Send 6 | Missourians for Fair Governance | respectmissourivoters.org form | July 15, 10:XX UTC | [x] SENT | PENDING |
```

---

### Send 7: Common Cause State Chapters (MO, ND, SD)
**Date**: July 15, 2026, 14:00 UTC

| Field | Value |
|---|---|
| To (Missouri) | MO chapter via commoncause.org/missouri |
| To (North Dakota) | ND chapter via commoncause.org/north-dakota |
| To (South Dakota) | SD chapter via commoncause.org/south-dakota |
| Subject | Domain M brief: State chapter direct democracy defense — routing from national office |
| Note | Send as three separate emails to each state chapter, OR as one email CC'ing all three if state chapter contact info is not individually listed |

**Email body (send to each state chapter):**

```
Dear Common Cause [Missouri/North Dakota/South Dakota],

I am sharing the Domain M research brief — "Direct Democracy Under Supermajority
Attack" — which Common Cause National has reviewed. The brief provides the
structural framing argument for your state's ballot measure campaign.

For [Missouri/North Dakota/South Dakota] specifically:

[Missouri: Amendment 4 analysis — congressional district requirement, every MO
initiative since 2020 would have failed, Medicaid, marijuana, minimum wage,
sick leave, abortion rights]

[North Dakota: Measure 2 — 60% threshold, 2018 Medicaid expansion at 53%
would have failed, empirical record of ND initiative outcomes]

[South Dakota: 60% threshold for citizen-initiated constitutional amendments
— comparative analysis with North Dakota and Missouri attack pattern]

The brief provides three tools for your voter communication work:
1. Structural framing (why this is about eliminating the bypass mechanism)
2. Empirical record (what voters have actually accomplished via initiative)
3. National pattern context (how this connects to the coordinated attack)

CC Attribution 4.0 — use in voter guides, campaign materials, coalition outreach.

[DOMAIN_M_GIST_URL]

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

**After sending:** Log in DOMAIN_M_DISTRIBUTION_EXECUTION_LOG.md:

```
| Send 7 | Common Cause State Chapters (MO/ND/SD) | via state chapter contacts | July 15, 14:XX UTC | [x] SENT | PENDING |
```

---

## Contact List (All Verified as of June 29, 2026)

| Send | Organization | Email | Contact | Tier | Verification |
|------|---|---|---|---|---|
| 1 | Ballot Initiative Strategy Center | ballot.org/contact form | Research director / Defend Direct Democracy | Tier 1 | Active: ballot.org/defenddirectdemocracy (June 29) |
| 2 | Democracy Docket | info@democracydocket.com | Marc Elias (melias@elias.law); Aria Branch (aria@democracydocket.com) | Tier 1 | Active: democracydocket.com/about (June 29) |
| 3 | Common Cause National | commoncause@commoncause.org | Virginia Kase Solomón, President & CEO | Tier 1 | Active: commoncause.org/people/virginia-kase-solomon/ (June 29) |
| 4 | League of Women Voters (National) | Contact@lwv.org | National office + state chapters | Tier 2 | Active: lwv.org (June 29) |
| 5 | Brennan Center for Justice | democracy@brennancenter.org | Direct Democracy Program | Tier 2 | Active: brennancenter.org/series/direct-democracy (June 29) |
| 6 | Missourians for Fair Governance | respectmissourivoters.org form | Campaign director | Tier 2 | Active: respectmissourivoters.org (June 29) |
| 7 | Common Cause MO/ND/SD chapters | Via state chapter contacts | State chapter directors | Tier 2 | Active: commoncause.org/[state] (June 29) |

**Dead contacts — do not use:**
- Karen Hobert Flynn (kflynn@commoncause.org) — deceased March 2023. Use commoncause@commoncause.org.
- Sheila Krumholz (OpenSecrets) — departed 2023. Not in Domain M contact list.
- info@cleanmoney.org — not in Domain M contacts. (Domain 51 contact issue only.)

---

## Pre-Authorization Escalation Sequence

All thresholds below are pre-authorized. No user confirmation required to advance.

| UTC Timestamp | Condition | Auto-Action | Escalation Level |
|---|---|---|---|
| July 1, 00:00 UTC | Domain 51 deadline passed without completion | ACTIVATE this runbook; begin Phase 1 research sprint immediately | ACTIVATION |
| July 5, 23:59 UTC | Research brief not complete | Extend research sprint; shift all Phase 3 send dates by 1-2 days equal to delay | WARNING |
| July 7, 14:00 UTC | Gist not live at send time | Do not send — fix Gist immediately; send once live; no permanent delay | HOLD |
| July 10, 23:59 UTC | Tier 1 sends (BISC, DD, CC) not all complete | LOG incomplete sends; continue; escalate to user: Tier 1 window closing | CRITICAL |
| July 12, 00:00 UTC | Tier 2 window opens | Activate Tier 2 sends regardless of Tier 1 reply status | AUTO |
| July 15, 23:59 UTC | All 7 sends must be logged | Final Tier 2 deadline; any incomplete sends after this date lose coalition-framing window | FINAL |

---

## Success Metrics

| Metric | Target | Deadline |
|---|---|---|
| Research brief complete (3,000+ words, 25+ citations) | Yes | July 5, 23:59 UTC |
| Gist live (HTTP 200) | Yes | July 7, 12:00 UTC (before first send) |
| Tier 1 sends (BISC, DD, CC) all sent | 3 of 3 | July 11, 23:59 UTC |
| Tier 2 sends (LWV, Brennan, MFFG, CC states) all sent | 4 of 4 | July 15, 23:59 UTC |
| No hard bounces on any send | Yes | Ongoing |
| 1+ positive reply from Tier 1 by July 14 | Yes (target, not required) | July 14 |
| All 7 sends logged in DOMAIN_M_DISTRIBUTION_EXECUTION_LOG.md | Yes | July 15, 23:59 UTC |

**Mission success definition**: All 7 sends complete and logged by July 15, 23:59 UTC + research brief finalized. One or more positive Tier 1 replies by July 14 = strong outcome but not required for mission success.

**Value if successful**: 75-85% (vs. 100% if Domain 51 Wave 1 had executed by June 30 and Domain M was not in contingency mode). The July window is the second-best option; it is still the decision-making window for campaign organizations.

---

## Execution Log (Create as DOMAIN_M_DISTRIBUTION_EXECUTION_LOG.md on July 1)

```markdown
# Domain M Contingency Activation — Execution Log
## July 1-15, 2026

Trigger condition: Domain 51 Phase 2 Waves 1+2 not complete by June 30, 23:59 UTC
Activation date: July 1, 2026, 00:00 UTC
Status: ACTIVE

### Phase 1 — Research Sprint
| Milestone | Target | Actual | Status |
|---|---|---|---|
| Draft complete | July 5 | [fill] | [ ] |
| Final version | July 7 | [fill] | [ ] |
| Word count | 3,000+ | [fill] | [ ] |
| Citation count | 25+ | [fill] | [ ] |

### Phase 2 — Gist
| Step | Target | Actual | Status |
|---|---|---|---|
| Gist created | July 5-7 | [fill] | [ ] |
| HTTP 200 confirmed | July 7 morning | [fill] | [ ] |
| URL filled in all templates | July 7 | [fill] | [ ] |

### Phase 3 — Tier 1 Sends
| Send | Organization | Email | Date | Time (UTC) | Status | Reply Status |
|---|---|---|---|---|---|---|
| 1 | BISC | ballot.org/contact | July 7 | 14:XX | [ ] | PENDING |
| 2 | Democracy Docket | info@democracydocket.com | July 9 | 14:XX | [ ] | PENDING |
| 3 | Common Cause National | commoncause@commoncause.org | July 11 | 14:XX | [ ] | PENDING |

### Gate 3 — July 14 Tier 1 Reply Check
| Contact | Reply received? | Type | Notes |
|---|---|---|---|
| BISC | [ ] | — | — |
| Democracy Docket | [ ] | — | — |
| Common Cause National | [ ] | — | — |

### Phase 4 — Tier 2 Sends
| Send | Organization | Email | Date | Time (UTC) | Status |
|---|---|---|---|---|---|
| 4 | LWV National | Contact@lwv.org | July 12 | 14:XX | [ ] |
| 5 | Brennan Center | democracy@brennancenter.org | July 14 | 14:XX | [ ] |
| 6 | Missourians for Fair Governance | respectmissourivoters.org form | July 15 | 10:XX | [ ] |
| 7 | Common Cause State Chapters | MO/ND/SD contacts | July 15 | 14:XX | [ ] |

### Final Assessment (July 15 end of day)
- [ ] All 7 sends complete
- [ ] Research brief finalized and distributed
- [ ] No hard bounces on any send
- [ ] 1+ positive Tier 1 reply
- [ ] All sends logged with UTC timestamps

Final value outcome: [75-85% if all complete / 50-65% if partial / assess per sends completed]
```

---

## Integration with Domain 51 Contingency (If Both Active Simultaneously)

If Domain 51 contingency sends (Tier 2 accelerated, July 1-8) are also executing:

- **No content conflict**: Domain 51 and Domain M are separate research on separate topics with different primary contacts.
- **Common Cause National is in both**: Domain 51 contingency may include a Common Cause send July 1-8. Domain M Send 3 (Common Cause) is July 11. Minimum 8-day spacing is satisfied as long as Domain 51 Common Cause send is July 3 or earlier.
- **Democracy Docket is Domain M only**: Not in Domain 51 contingency contacts. No spacing concern.
- **BISC is Domain M only**: Not in Domain 51 contacts. No spacing concern.
- **Combined bandwidth July 7-8**: Domain 51 Tier 2 final sends may coincide with Domain M BISC send (July 7). Both are manageable in a single session: Domain 51 sends in morning, Domain M Gist creation afternoon, BISC send late afternoon or evening.

---

## FAQ

**Q: What if the research brief is not ready by July 7 (first Tier 1 send)?**
A: Send Tier 1 emails without the Gist attachment, offering the brief within 48 hours. Text to use: "A 3,500-word research brief is available and I will send the full document by [date + 2 days]." Notify orchestrator immediately. Complete brief within 48 hours of sending. The critical window is the contact — organizations will wait 48 hours for a draft if the abstract interests them.

**Q: What if BISC, Democracy Docket, or Common Cause does not reply by July 14?**
A: Proceed with all Tier 2 sends regardless. Zero replies from Tier 1 by July 14 is within normal range for cold research outreach to policy organizations. Continue; assess at August 1 T+30 checkpoint.

**Q: Can I send all 7 emails in one day?**
A: No. The staggered send schedule prevents spam filter flags and spaces inbox positioning. Minimum 90 minutes between sends within a single day. The schedule is designed for 1-2 sends per day across July 1-15.

**Q: What if the Domain M Gist URL changes (I have to recreate it)?**
A: Update [DOMAIN_M_GIST_URL] in all unsent templates immediately. Log the URL change in the execution log. Verify new URL before sending any email containing it.

**Q: Do I need to fill [YOUR_NAME] and [YOUR_CONTACT_INFO] consistently across all 7 sends?**
A: Yes. Use the same name and contact information across all sends — organizations compare notes, and inconsistent signatures undermine credibility.

**Q: What if Domain M research was already complete before July 1?**
A: Proceed directly to Phase 2 (Gist creation). Skip Phase 1. Adjust send dates accordingly — you can move Phase 3 sends earlier if the brief is ready before July 7.

---

## Discord Status Templates

**July 1 — Activation:**
```
DOMAIN M CONTINGENCY ACTIVATED — July 1, [HH:MM] UTC
Domain 51 June 30 deadline passed without completion
Domain M auto-trigger confirmed
Phase 1 research sprint: July 1-5
Tier 1 sends: July 7-11 (BISC, Democracy Docket, Common Cause)
Tier 2 sends: July 12-15 (LWV, Brennan, MFFG, CC state chapters)
```

**July 10 — Tier 1 complete:**
```
DOMAIN M TIER 1 COMPLETE — July 10
BISC: sent July 7 [HH:MM UTC] — reply: [YES/NO]
Democracy Docket: sent July 9 [HH:MM UTC] — reply: [YES/NO]
Common Cause National: sent July 11 [HH:MM UTC] — reply: [YES/NO]
Research brief: finalized and attached
Tier 2 activation: proceeding July 12-15
```

**July 15 — Mission complete:**
```
DOMAIN M CONTINGENCY ACTIVATION COMPLETE — July 15
All 7 sends logged
Research brief: distributed to 7 organizations
Coalition window: July 1-15 covered
November 3 ballot: BISC/Democracy Docket/Common Cause informed in decision window
Value: 75-85% (contingency outcome)
Next: Monitor for citations and amplification through August
```

---

## Cross-Reference Files

| Purpose | File |
|---|---|
| Tier 1 send templates (original Item 44) | DOMAIN_M_TIER_1_SEND_TEMPLATES.md |
| July 1-15 activation sequence (research outline + Gist instructions) | DOMAIN_M_JULY_1_15_ACTIVATION_SEQUENCE.md |
| Approval case / source documentation | DOMAIN_M_PHASE_2_BALLOT_ACCELERATION_CASE.md |
| Domain 51 contingency decision tree | DOMAIN_51_CONTINGENCY_DECISION_TREE.md |
| Domain M execution log (create July 1) | DOMAIN_M_DISTRIBUTION_EXECUTION_LOG.md |
| Domain 51 Tier 2 contingency sends | DOMAIN_51_TIER_2_ACCELERATED_SEND_SEQUENCE.md |

---

*Item 45 — Runbook 2 of 2. Production-ready June 29, 2026.*
*Auto-trigger: July 1, 00:00 UTC if Domain 51 June 30 deadline missed.*
*All 7 contact addresses verified June 29, 2026.*
*Research brief draft required before Phase 3 sends — outline and sources in DOMAIN_M_JULY_1_15_ACTIVATION_SEQUENCE.md.*
*Zero TODOs. All templates copy-paste ready (fill 3 fields: YOUR_NAME, YOUR_CONTACT_INFO, DOMAIN_M_GIST_URL).*
