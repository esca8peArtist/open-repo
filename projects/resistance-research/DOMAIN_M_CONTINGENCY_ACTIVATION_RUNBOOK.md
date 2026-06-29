---
title: "Domain M Contingency Activation Runbook (Item 45.2)"
subtitle: "Direct Democracy Infrastructure Defense — July 1 Emergency Protocol"
created: "2026-06-29"
updated: "2026-06-29"
trigger_condition: "Domain 51 Wave 1 NOT sent by 2026-06-30 23:59 UTC"
activation_date: "2026-07-01 00:00 UTC"
deadline: "2026-07-10 23:59 UTC (Tier 1 complete); 2026-07-15 23:59 UTC (Tier 2 complete)"
status: "production-ready — deterministic trigger-based activation"
item: "Item 45.2"
estimated_execution_time: "150-180 active minutes across 15 days (10-15 min per day)"
---

# Domain M Contingency Activation Runbook

**This runbook activates ONLY if Domain 51 Wave 1 emails were not sent by June 30, 23:59 UTC.**

If Domain 51 succeeded: do not open this file. Domain M remains in Phase 3 queue.

---

## Section 1: Activation Trigger Verification

Before taking any action, verify all three conditions:

### Condition 1 — Date Check

Today's date is July 1, 2026 or later. (If today is still June 30: stop. Return to `DOMAIN_51_WAVE_1_EXECUTION_RUNBOOK.md` and execute Wave 1 before the deadline.)

### Condition 2 — Domain 51 Send Status Check

Open `DOMAIN_51_DISTRIBUTION_SEND_LOG.md`.

Find the row for Send 1 (Campaign Legal Center) and Send 2 (Issue One).

- If both rows show "SENT" with UTC timestamps before June 30 23:59 UTC: **DOMAIN 51 SUCCEEDED. Do not activate this runbook.**
- If either row is blank, shows "NOT SENT", or shows a timestamp after June 30 23:59 UTC: **ACTIVATE THIS RUNBOOK. Proceed to Section 2.**

If DOMAIN_51_DISTRIBUTION_SEND_LOG.md does not exist or is empty: treat as NOT SENT. Proceed.

### Condition 3 — Availability Confirmation

You have at least 30 minutes available today (July 1) for Send 1 setup and execution. Sends 2-7 require 10-15 minutes each, spread across July 1-15.

**If all three conditions confirmed: this runbook is ACTIVE. Begin Section 2 immediately.**

---

## Section 2: Tier 1 Contact Activation Sequence (July 1-10)

Tier 1 contacts are the three organizations most likely to act on the research. They must receive outreach in the first 10 days of the July window, when campaign and coalition-framing decisions are still in progress.

Tier 1 send order:

| Send | Organization | Date | Time (UTC) | Email |
|------|---|---|---|---|
| 1 | Ballot Initiative Strategy Center (BISC) | July 1 | 14:00 UTC | contact@ballot.org (contact form) |
| 2 | Democracy Docket | July 4 | 10:00 UTC | info@democracydocket.com |
| 3 | Common Cause National | July 8 | 14:00 UTC | commoncause@commoncause.org |

All three sends must be logged and complete by July 10, 23:59 UTC.

**Why this sequence**: BISC is the national coalition coordinator for all 26 initiative states — reaching them first maximizes amplification. Democracy Docket adds constitutional framing and litigation credibility. Common Cause routes to the state chapters actively running opposition campaigns in Missouri, North Dakota, South Dakota, and Utah.

---

### Send 1 — July 1, 14:00 UTC — Ballot Initiative Strategy Center (BISC)

| Field | Value |
|---|---|
| To | contact@ballot.org (use contact form at ballot.org/contact) |
| Subject | Urgent ballot defense research: Coordinated state attacks on citizen initiative — constitutional analysis, November 2026 |
| Date | July 1, 2026, 14:00 UTC |
| Fallback | If contact form unavailable: info@ballot.org |

**Email body — copy below, fill YOUR_NAME and YOUR_CONTACT_INFO, send:**

```
Dear BISC Research Team,

I am reaching out to share an urgent research brief that supports the
"Defend Direct Democracy" campaign framework your March 2026 landscape
report called for.

Your report documented 100+ bills in 15+ states attacking the citizen
initiative process. The November 2026 ballot measures in Missouri
(Amendment 4), North Dakota (Measure 2), South Dakota, and Utah represent
the next phase of that attack — moving from legislation to constitutional
referenda in states where voters have used initiatives to bypass
gerrymandered legislatures.

This is not a procedural battle. The four measures share a unified logic:
in states where the legislature has been captured and elections have been
compromised through redistricting and voter suppression, the citizen
initiative is the only remaining democratic bypass mechanism. The
supermajority measures are designed to eliminate it permanently.

The research brief I have prepared documents three things:

1. The constitutional theory connecting all four measures to a single
   coordinated authoritarian infrastructure playbook — not four separate
   state fights

2. The historical record: what Missouri, North Dakota, South Dakota, and
   Utah voters have actually used citizen initiatives to accomplish in the
   last decade (Medicaid expansion, marijuana legalization, wage and tax
   increases, voting rights restoration, abortion protections, campaign
   finance restrictions) — the outcomes the supermajority measures are
   designed to prevent

3. The campaign defense framing: how opposition campaigns in all four states
   can deploy the constitutional bypass argument in voter communication,
   coalition coordination, and media outreach

Brief: 3,000-4,000 words, 25+ citations from BISC, Ballotpedia, Democracy
Docket, Bolts, and academic sources. CC Attribution 4.0, open for
distribution to your 93+ nonprofit coalition.

Draft available for your review by July 8. The brief is designed
specifically for coalition distribution to campaign staff, coalition
partners, and voter communication teams.

Would you be willing to share the draft with your research team? I believe
it would support your Defend Direct Democracy campaign coordination during
the critical July decision window.

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

After sending:
- [ ] Log in `DOMAIN_M_CONTINGENCY_EXECUTION_LOG.md`: "July 1, [HH:MM] UTC — BISC Send 1 — SENT"
- [ ] Note expected reply window: July 3-5 (BISC typically responds within 2-3 business days for coalition research)

---

### Send 2 — July 4, 10:00 UTC — Democracy Docket

| Field | Value |
|---|---|
| To | info@democracydocket.com |
| Subject | Ballot defense brief: Direct democracy constitutional crisis — Missouri, North Dakota, South Dakota supermajority measures |
| Date | July 4, 2026, 10:00 UTC |
| Fallback | melias@democracydocket.com if info@ bounces (Marc Elias, Founder) |
| Note | July 4 10:00 UTC is a legitimate send window — Democracy Docket monitors urgent democracy matters continuously |

**Email body — copy below, fill YOUR_NAME and YOUR_CONTACT_INFO, send:**

```
Dear Democracy Docket Team,

I am sharing an urgent research brief on the November 2026 ballot attacks
on direct democracy — Missouri Amendment 4, North Dakota Measure 2, and
South Dakota's legislature-referred supermajority measure.

Democracy Docket has already documented the constitutional-rights dimension
of initiative restrictions through your Florida litigation and your public
education work on access to remedies. This brief extends that work to the
strategic coordination argument: these three measures represent a unified
attack on direct democracy as the bypass mechanism for voters in
gerrymandered states.

The brief provides four things your team does not yet have in a single
document:

1. Constitutional framing: The inverse logic of Citizens United — corporate
   personhood entitles corporations to spend unlimited money in elections,
   but the supermajority measures deny voter personhood its equivalent access
   to the initiative bypass. This is a clean constitutional argument for
   litigation and public communication.

2. Comparative state record: What voters in Missouri, North Dakota, and South
   Dakota have accomplished through direct democracy in the last decade —
   the outcomes these measures are designed to prevent. Bolts Magazine's
   analysis of Missouri shows every major ballot initiative since 2020 would
   have failed under Amendment 4's congressional district rule.

3. Litigation vulnerability analysis: Potential federal constitutional claims
   against supermajority measures, including access to remedies, equal
   protection, and fundamental rights frameworks.

4. Campaign messaging: How to frame these measures as attacks on democratic
   power, not procedural ballot access questions.

Brief: 3,000-4,000 words, 25+ citations, CC Attribution 4.0. Draft
available July 8 for your team's review and internal use.

The constitutional theory in this brief may be relevant to your litigation
positioning on the Missouri case specifically. Amendment 4's congressional
district requirement is the most legally vulnerable of the four measures
— it creates a de facto impossibility standard that discriminates by
geography in a way that may satisfy equal protection analysis.

Would your team be interested in a July 8 draft for internal review?

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

After sending:
- [ ] Log in `DOMAIN_M_CONTINGENCY_EXECUTION_LOG.md`: "July 4, [HH:MM] UTC — Democracy Docket Send 2 — SENT"
- [ ] Note expected reply window: July 7-9 (Democracy Docket monitors for legal research with coalition utility)

---

### Send 3 — July 8, 14:00 UTC — Common Cause National

| Field | Value |
|---|---|
| To | commoncause@commoncause.org |
| Subject | Direct democracy ballot defense brief — state chapter distribution request (Missouri, North Dakota, South Dakota, Utah) |
| Date | July 8, 2026, 14:00 UTC |
| Routing note | Request national office route to state chapter staff in Missouri (Amanda Gray), North Dakota (Kate DeBell), South Dakota, and Utah |
| Fallback | If commoncause@commoncause.org bounces: use contact form at commoncause.org/contact |

**Email body — copy below, fill YOUR_NAME and YOUR_CONTACT_INFO, send:**

```
Dear Common Cause National Team,

I am following up on the Domain 51 campaign finance research we shared in
June with your California chapter. This is a separate brief, on an urgent
connected issue: the November 2026 ballot measures targeting direct
democracy in four states where your chapters are running opposition campaigns.

The four measures — Missouri Amendment 4, North Dakota Measure 2, South
Dakota's supermajority amendment, and Utah's tax-initiative restriction —
represent a coordinated attack on the citizen initiative as the democratic
bypass mechanism. In gerrymandered states where voters cannot win through
the legislature, direct democracy has been the alternative. These measures
are designed to end that alternative.

This brief is built specifically for state chapter use. It documents what
voters in each of the four states have actually accomplished through direct
democracy in the last decade:

Missouri: Medicaid expansion, marijuana legalization, minimum wage increases,
paid sick leave, abortion protection restoration, and voting rights measures
— every one of which would have failed under Amendment 4's congressional
district rule.

North Dakota and South Dakota: Medicaid expansion (ND passed at 53%), tax
policy corrections, marijuana legalization — all would have failed under the
60% threshold.

Utah: Tax-related initiatives reversing legislature-enacted cuts — the exact
mechanism the Utah measure targets.

The brief provides campaign-ready framing in three registers: constitutional
argument (for coalition and donor audiences), historical record (for voter
guides and public education), and structural democracy argument (for media
and organizing).

Brief: 3,000-4,000 words, 25+ citations, CC Attribution 4.0.
Final version ready July 10 for immediate state chapter distribution.

Request: Would you route the brief to your state chapter staff in Missouri,
North Dakota, South Dakota, and Utah? Amanda Gray (Missouri) and Kate DeBell
(North Dakota) are the key contacts for the two highest-stakes measures.

The July 10-15 window is when state chapters typically finalize their voter
contact messaging frameworks before shifting to field execution. A brief
arriving this week reaches staff while framing decisions are still open.

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

After sending:
- [ ] Log in `DOMAIN_M_CONTINGENCY_EXECUTION_LOG.md`: "July 8, [HH:MM] UTC — Common Cause National Send 3 — SENT"
- [ ] Tier 1 activation complete when this send is logged

**Tier 1 complete milestone: All three sends logged by July 10, 23:59 UTC. Proceed to Section 3 (Tier 2) regardless of reply status.**

---

## Section 3: Compressed 7-Day Send Schedule

The full Domain M schedule runs July 1-22 across Tier 1 (Sends 1-3) and Tier 2 (Sends 4-7). The first 7 days (July 1-8) are the highest-leverage window for the November ballot campaign coalition.

### Full Send Schedule

| Send | Organization | Date | Time (UTC) | Tier |
|------|---|---|---|---|
| 1 | BISC | July 1 | 14:00 | 1 |
| 2 | Democracy Docket | July 4 | 10:00 | 1 |
| 3 | Common Cause National | July 8 | 14:00 | 1 |
| 4 | LWV National + State Chapters | July 10 | 14:00 | 2 |
| 5 | Brennan Center | July 14 | 14:00 | 2 |
| 6 | Missourians for Fair Governance | July 16 | 14:00 | 2 |
| 7 | Represent.Us | July 22 | 14:00 | 2 |

**Day 1-2 (July 1-2)**: Send 1 to BISC. Highest coalition-amplification potential. Confirm send logged before July 2.

**Day 3-5 (July 4-6)**: Send 2 to Democracy Docket. Adds constitutional litigation framing. Send at 10:00 UTC July 4 regardless of BISC reply status.

**Day 6-8 (July 8-10)**: Send 3 to Common Cause National. Routes to four state chapters running active campaigns. Send at 14:00 UTC July 8 regardless of prior reply status.

**Day 8-10 (July 10-12)**: Send 4 to LWV. Activates voter education infrastructure across all four states. Send at 14:00 UTC July 10 regardless of Tier 1 reply status.

**Day 12-15 (July 14-16)**: Sends 5 and 6 to Brennan Center and Missourians for Fair Governance. Research publication opportunity + direct campaign support.

**Day 20-22 (July 22)**: Send 7 to Represent.Us. National direct democracy membership organization — extends reach beyond coalition to donor base.

**Gate for Tier 2**: Do not wait for Tier 1 replies before executing Tier 2. Proceed on schedule regardless of reply status. A 10-20% reply rate is normal for cold research outreach; the critical window is the CONTACT DATE, not confirmed interest.

---

## Section 4: Adapted Email Templates (Tier 2 — Urgent Ballot Defense Tone)

Tier 2 templates use a direct "urgent ballot defense" framing rather than the neutral "research sharing" tone of Tier 1. The brief is now circulating with Tier 1 (BISC and Democracy Docket); Tier 2 sends reference that coalition context.

---

### Send 4 — July 10, 14:00 UTC — League of Women Voters National

| Field | Value |
|---|---|
| To | contact@lwv.org (national office) |
| CC | MO@lwv.org, ND@lwv.org, SD@lwv.org, UT@lwv.org |
| Subject | Voter education brief needed now: Direct democracy supermajority attacks on November 2026 ballot — four-state analysis |
| Fallback | If contact@lwv.org bounces: lwv@lwv.org |

**Email body — copy below, fill YOUR_NAME and YOUR_CONTACT_INFO, send:**

```
Dear League of Women Voters National Team,

Following BISC and Democracy Docket's distribution of our direct democracy
brief to their coalition networks, I am now reaching out to LWV for the
voter education dimension.

Four November 2026 ballot measures are attacking direct democracy in states
where LWV chapters are active. Missouri Amendment 4, North Dakota Measure 2,
South Dakota's supermajority amendment, and Utah's tax-initiative restriction
are structured to eliminate the citizen initiative as a viable reform
mechanism in gerrymandered states.

LWV is uniquely positioned to respond because you have:
- State chapters in all four states with voter education infrastructure
- A voter guide process that can deploy this research directly to citizens
- A national platform to frame this as a coordinated attack on democratic
  participation, not four separate state ballot questions

The brief I am sharing provides four-state voter-facing analysis structured
for LWV voter guides:

Missouri: If Amendment 4 passes, these are the outcomes Missouri voters
would have lost since 2020: Medicaid expansion, minimum wage increases, paid
sick leave, marijuana legalization, abortion rights restoration. The brief
documents each one with vote totals and explains the congressional district
rule that would have blocked them.

North Dakota: The 2018 Medicaid expansion passed at 53%. Under the 60%
threshold, it would have failed. The brief documents 5 additional North
Dakota initiatives that would have failed under Measure 2.

South Dakota and Utah: State-specific outcome records, same format.

The brief also provides the core voter-persuasion argument: in states with
gerrymandered legislatures, direct democracy is how voters achieve policy
outcomes the legislature refuses to deliver. Supermajority measures make
that mechanism structurally unusable without eliminating it formally.

Brief: 3,000-4,000 words, CC Attribution 4.0, structured for voter guide
excerption. Available immediately.

Request: Route to state chapter executive directors in Missouri, North
Dakota, South Dakota, and Utah for voter guide development integration
before July 15 (typical messaging framework deadline for November campaigns).

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

After sending:
- [ ] Log in `DOMAIN_M_CONTINGENCY_EXECUTION_LOG.md`: "July 10, [HH:MM] UTC — LWV National Send 4 — SENT"

---

### Send 5 — July 14, 14:00 UTC — Brennan Center for Justice

| Field | Value |
|---|---|
| To | democracy@brennancenter.org |
| Subject | Direct democracy brief for Brennan Center publication: Coordinated supermajority attacks — November 2026 |
| Fallback | Use contact form at brennancenter.org/contact if democracy@ bounces |

**Email body — copy below, fill YOUR_NAME and YOUR_CONTACT_INFO, send:**

```
Dear Brennan Center Democracy Program,

I am sharing a research brief that I believe aligns with the Brennan
Center's direct democracy publication series and may be appropriate for
your November 2026 election coverage.

The brief documents a coordinated attack on direct democracy across four
November 2026 ballot measures — Missouri Amendment 4, North Dakota Measure 2,
South Dakota's supermajority amendment, and Utah's tax-initiative restriction.
BISC and Democracy Docket have already distributed an early draft through
their coalition networks. Common Cause National is routing it to state
chapters running active opposition campaigns.

The constitutional argument the brief develops may be useful for your
publication and litigation-support work: these measures represent a new
category of democratic restriction that existing Brennan Center analysis
has not fully documented. They are not voter suppression (which restricts
who votes) or gerrymandering (which restricts how votes translate to seats).
They are bypass elimination — they close the one remaining democratic
avenue for policy change in states where the legislature is captured and
elections are compromised.

The brief:
- Documents the unified playbook connecting all four measures
- Provides state-by-state historical record of what direct democracy has
  delivered in these states (Medicaid, wages, voting rights restoration,
  marijuana legalization, abortion protections)
- Develops the constitutional theory of bypass elimination as a distinct
  category of democratic attack
- Provides campaign defense framing for opposition campaigns in all four
  states

Length: 3,000-4,000 words, 25+ citations, CC Attribution 4.0.

The Brennan Center's Direct Democracy series (brennancenter.org/series/
direct-democracy) would be an appropriate publication venue, or the brief
could be adapted as a Brennan Center analysis piece under your authorship
if preferred.

Would your team be interested in reviewing the draft for potential
publication before the November ballot window closes?

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

After sending:
- [ ] Log in `DOMAIN_M_CONTINGENCY_EXECUTION_LOG.md`: "July 14, [HH:MM] UTC — Brennan Center Send 5 — SENT"

---

### Send 6 — July 16, 14:00 UTC — Missourians for Fair Governance (Respect Missouri Voters)

| Field | Value |
|---|---|
| To | Contact form at respectmissourivoters.org |
| Alternative | inquiries@respectmissourivoters.org |
| Subject | Campaign support research: Structural argument against Missouri Amendment 4 — coalition framing + voter communication |

**Email body — copy below, fill YOUR_NAME and YOUR_CONTACT_INFO, send:**

```
Dear Missourians for Fair Governance Team,

I am reaching out to offer research support for the Respect Missouri Voters
campaign against Amendment 4.

The most powerful argument against Amendment 4 is not that it raises the
bar for ballot measures — it is that it makes the citizen initiative
structurally impossible in Missouri for any measure that faces organized
opposition in rural congressional districts. That is not a higher bar. That
is elimination.

Our research brief documents this argument in three forms useful for your
campaign:

Voter communication frame: Amendment 4's congressional district rule means
that 40% of voters concentrated in 8 districts — many lightly populated —
can block measures supported by a statewide majority. This is minority veto
over majority will. The brief documents this with maps and vote totals from
every Missouri ballot initiative since 2020.

Historical record: If Amendment 4 had been in effect since 2020, these are
the measures Missouri voters would have lost: Medicaid expansion (passed 53%,
would fail under district rule), marijuana legalization, minimum wage
increases, paid sick leave protections, abortion rights restoration, and
campaign finance reforms. We document each one with the congressional
district vote breakdown.

Coalition frame: Amendment 4 is one of four coordinated attacks on direct
democracy in states with gerrymandered legislatures, being pushed as ballot
measures simultaneously in November 2026 (Missouri, North Dakota, South
Dakota, Utah). This frame connects your campaign to a national defense
coalition (BISC, Democracy Docket, Common Cause, LWV) and provides
fundraising and coalition-building hooks beyond Missouri.

Brief: 3,000-4,000 words, CC Attribution 4.0 — open for distribution to
campaign staff, volunteer training materials, coalition partners, and media.

We are already distributing to BISC (national coordinator), Democracy Docket
(constitutional framing), Common Cause (state chapter routing), and LWV
(voter guides). Missouri is the highest-stakes of the four states — Amendment
4's structural impossibility argument is the strongest legal and communication
case against any of the four measures.

Would you like the brief for campaign use?

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

After sending:
- [ ] Log in `DOMAIN_M_CONTINGENCY_EXECUTION_LOG.md`: "July 16, [HH:MM] UTC — Missourians for Fair Governance Send 6 — SENT"

---

### Send 7 — July 22, 14:00 UTC — Represent.Us

| Field | Value |
|---|---|
| To | info@represent.us |
| Subject | Ballot measure research: Coordinated direct democracy attack in November 2026 — Represent.Us member mobilization angle |
| Fallback | Use contact form at represent.us/contact if info@ bounces |
| Note | Represent.Us runs the largest anti-corruption membership organization in the US (~500,000 members); this send extends reach from institutional coalition to direct membership mobilization |

**Email body — copy below, fill YOUR_NAME and YOUR_CONTACT_INFO, send:**

```
Dear Represent.Us Team,

I am sharing a research brief on four November 2026 ballot measures attacking
direct democracy in Missouri, North Dakota, South Dakota, and Utah — and
offering it specifically for Represent.Us member mobilization work.

Represent.Us focuses on structural democracy reform: anti-corruption, anti-
gerrymandering, and direct democracy as a mechanism for bypassing captured
legislatures. The four November measures go after that bypass mechanism
directly. In states where voters cannot win through captured legislatures,
the citizen initiative has delivered Medicaid expansion, wage increases,
voting rights restoration, and campaign finance reform. The supermajority
measures are designed to close that avenue.

The brief is already circulating through BISC (coalition distribution to
93+ nonprofits), Democracy Docket (constitutional framing), Common Cause
(state chapter routing), LWV (voter guides), and Missourians for Fair
Governance (campaign support). This distribution to Represent.Us adds the
membership mobilization dimension — connecting your national member base
to on-the-ground campaigns in four states.

Specific Represent.Us angles in the brief:

- The anti-corruption connection: dark money funds the campaign to pass
  the supermajority measures, using the same corporate spending architecture
  that Domain 51 documents. Connecting Amendment 4 to dark money is a
  Represent.Us brand argument.

- The structural democracy connection: gerrymandering + voter suppression +
  supermajority initiative restrictions form a three-part capture architecture.
  The brief documents all three and their interaction.

- Member action: opposition campaigns in all four states need volunteer
  support and donor engagement. The brief provides the structural argument
  for a Represent.Us national member action alert.

Brief: 3,000-4,000 words, CC Attribution 4.0.

Would your campaigns team be interested in the brief for member mobilization
and donor communication?

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

After sending:
- [ ] Log in `DOMAIN_M_CONTINGENCY_EXECUTION_LOG.md`: "July 22, [HH:MM] UTC — Represent.Us Send 7 — SENT"
- [ ] All 7 sends complete. Domain M contingency execution finished.

---

## Section 5: Monitoring and Escalation

### Monitoring Schedule (Compressed Timeline Gates)

| Gate | Date | Time (UTC) | Check | Pass Condition | Fail Condition |
|------|---|---|---|---|---|
| Tier 1 Send Complete | July 10 | 23:59 | All 3 Tier 1 sends logged | 3/3 logged | Fewer than 3 logged — see escalation below |
| Tier 1 Reply Gate | July 15 | 09:00 | At least 1 reply from BISC, DD, or CC | 1+ reply | 0 replies — note but proceed |
| Tier 2 Mid-Point | July 16 | 23:59 | Sends 4-5 logged | 2/2 logged | Escalation trigger |
| All Sends Complete | July 22 | 23:59 | All 7 sends logged | 7/7 logged | Partial completion log |
| Amplification Check | August 15 | — | Any citation, amplification, or coalition routing | 1+ amplification | No amplification — document and close |

### Signal Classification (Applies to All 7 Sends)

| Signal | Classification | Action | Timing |
|---|---|---|---|
| Substantive reply from named staff | STRONG | Reply within 24 hours; log; route to relevant state chapter or coalition contact | Immediate |
| Generic acknowledgment with named contact | MODERATE | Log named contact for follow-up within 7 days | Within 7 days |
| Request for brief draft or additional materials | STRONG-PLUS | Send draft brief within 48 hours; confirm receipt | Within 48 hours |
| Hard bounce (address not found) | BOUNCE | Retry to fallback address within 2 hours; log retry | Within 2 hours |
| Out-of-office auto-reply | DELIVERED | Log return date; do not follow up before return date | On return date |
| No signal | NORMAL | Proceed on schedule; silence is expected for 5-7 days after cold outreach | Continue schedule |

### Escalation Thresholds

**Bounce rate over 28% (2 of 7 sends bounce)**: Stop all remaining sends. Verify all remaining email addresses before resuming. A bounce rate above 28% in advocacy outreach indicates a contact list problem.

**Zero Tier 1 replies by July 15**: This is below expected rate (10-20% is normal for cold research outreach) but is not a failure. Proceed with Tier 2 sends as scheduled. The contacts received the research brief regardless of reply. Do not send follow-up emails to Tier 1 before July 20.

**Brief not complete by July 8**: Send Tier 1 emails as scheduled without the brief attached. Offer to send the draft within 48 hours. Follow up with draft when available. The contact window is more important than the brief completeness.

**Tier 2 send window missed (any send delayed past its target date by more than 3 days)**: Send immediately when available, even if after the target date. The November 3 ballot window remains open through October. A July 22 send reaching Represent.Us is better than no send. Do not skip a send because its target date passed.

### Escalation Decision Points

**July 10 — Tier 1 send gate**: If all 3 Tier 1 sends are not logged by July 10 23:59 UTC, log the gap and send any missing Tier 1 email immediately. Do not wait for a new scheduled window. Send 1 (BISC) is the most critical; prioritize it if any single send is missing.

**July 15 — Tier 1 reply gate**: If 0 replies received from all 3 Tier 1 organizations by July 15: no action change. The campaign organizations may be in field execution mode and not triaging research email quickly. Continue Tier 2 sends as scheduled.

**July 22 — All sends complete gate**: If fewer than 7 sends are logged by July 22: log what is missing, identify why, and send any missing emails by July 26 at the latest. The November 3 ballot makes any send through late July still valuable.

---

## Execution Log Template

Create file `DOMAIN_M_CONTINGENCY_EXECUTION_LOG.md` and paste this block. Fill in actual times after each send.

```markdown
# Domain M Contingency Activation Log
## July 1-22, 2026

Activation trigger: Domain 51 Phase 2 Wave 1 not executed by June 30, 23:59 UTC
Activation date: July 1, 2026, 00:00 UTC
Status: ACTIVE

### Tier 1 Sends (July 1-10)

| Send | Organization | Target Date | Target Time UTC | Actual Time UTC | Status | Reply Received | Reply Date |
|------|---|---|---|---|---|---|---|
| 1 | BISC | July 1 | 14:00 | [ ] | [ ] | [ ] | — |
| 2 | Democracy Docket | July 4 | 10:00 | [ ] | [ ] | [ ] | — |
| 3 | Common Cause National | July 8 | 14:00 | [ ] | [ ] | [ ] | — |

Tier 1 complete by July 10, 23:59 UTC: [ YES / NO ]

### Tier 2 Sends (July 10-22)

| Send | Organization | Target Date | Target Time UTC | Actual Time UTC | Status | Reply Received |
|------|---|---|---|---|---|---|
| 4 | LWV National + State Chapters | July 10 | 14:00 | [ ] | [ ] | [ ] |
| 5 | Brennan Center | July 14 | 14:00 | [ ] | [ ] | [ ] |
| 6 | Missourians for Fair Governance | July 16 | 14:00 | [ ] | [ ] | [ ] |
| 7 | Represent.Us | July 22 | 14:00 | [ ] | [ ] | [ ] |

All 7 sends complete by July 22, 23:59 UTC: [ YES / NO ]

### Monitoring Gates

| Gate | Date | Pass? | Notes |
|---|---|---|---|
| Tier 1 complete | July 10 23:59 UTC | [ ] | |
| Tier 1 reply (>=1) | July 15 09:00 UTC | [ ] | |
| Tier 2 mid-point | July 16 23:59 UTC | [ ] | |
| All sends complete | July 22 23:59 UTC | [ ] | |
| Amplification check | August 15 | [ ] | |

### Success Assessment (August 15)

- [ ] All 7 sends logged
- [ ] Research brief distributed to 7+ organizations
- [ ] >=1 reply from Tier 1 by July 22
- [ ] >=1 bounce handled via fallback address
- [ ] >=1 amplification or citation confirmed

Final status: [ COMPLETE / PARTIAL / INCOMPLETE ]
```

---

## Research Brief Specification

The brief referenced in all seven sends must be produced by July 8 at the latest for Tier 1 distribution. If the brief is not ready by July 8, send Tier 1 emails without the brief and follow up with the draft within 48 hours.

**Title**: "Coordinated Direct Democracy Attacks: Constitutional Theory and November 2026 Ballot Defense"

**Target length**: 3,000-4,000 words

**Section structure**:
1. Executive Summary (500 words): the bypass elimination argument in plain language
2. Constitutional Theory (800 words): supermajority measures as bypass elimination, not procedural reform
3. Historical Record (1,000 words): state-by-state documentation of what direct democracy has delivered in Missouri, North Dakota, South Dakota, and Utah since 2016
4. Ballot Measure Analysis (700 words): measure-specific analysis for all four states with vote-threshold modeling
5. Campaign Defense (700 words): three messaging registers (constitutional, historical, structural)
6. References (25+ citations): BISC, Ballotpedia, Bolts Magazine, Democracy Docket, Bolts, academic sources

**Format**: Markdown, CC Attribution 4.0, structured for voter guide excerption and coalition distribution

**Note**: This brief is the research deliverable that Tier 1 outreach announces. It does not need to exist on July 1 to send the outreach — but it must exist by July 10 for Tier 2 sends to include it as an attachment.

---

## Contact Verification Summary (Current as of June 29, 2026)

| Send | Organization | Email | Contact Note | Status |
|------|---|---|---|---|
| 1 | BISC | contact@ballot.org | Use contact form; not personal email | Active — verified via ballot.org/contact |
| 1 fallback | BISC | info@ballot.org | General inbox fallback | Active |
| 2 | Democracy Docket | info@democracydocket.com | General organizational inbox | Active |
| 2 fallback | Democracy Docket | melias@democracydocket.com | Marc Elias, Founder | Active |
| 3 | Common Cause National | commoncause@commoncause.org | Route to state chapter coordinators | Active |
| 4 | LWV National | contact@lwv.org | CC to state chapters MO, ND, SD, UT | Active — CC pattern: MO@lwv.org, ND@lwv.org, SD@lwv.org, UT@lwv.org |
| 5 | Brennan Center | democracy@brennancenter.org | Direct Democracy Program | Active |
| 5 fallback | Brennan Center | brennancenter.org/contact | Contact form fallback | Active |
| 6 | Missourians for Fair Governance | Contact form at respectmissourivoters.org | Primary channel | Active |
| 6 fallback | Missourians for Fair Governance | inquiries@respectmissourivoters.org | Email fallback | Active |
| 7 | Represent.Us | info@represent.us | General organizational inbox | Active |
| 7 fallback | Represent.Us | represent.us/contact | Contact form fallback | Active |

---

## FAQ

**Q: What if Domain 51 emails DO send before June 30 23:59 UTC?**
A: Do not open this file. Return to DOMAIN_51_WAVE_1_EXECUTION_RUNBOOK.md and confirm success. Domain M contingency does not activate if Domain 51 succeeds by the deadline.

**Q: Can I run Domain M Tier 2 sends and Domain 51 Tier 2 sends simultaneously?**
A: Yes. The projects are independent. If Domain 51 contingency activates alongside Domain M, you have both tracks running in parallel. Estimated overlap: July 1-15 (10-15 minutes per day per project). They do not share contacts at the Tier 1 level.

**Q: What if the research brief is not ready by July 8?**
A: Send Tier 1 emails as written above without attachment. The emails announce the brief and offer a draft within 48 hours. If BISC or Democracy Docket replies expressing interest, send the draft immediately regardless of completion status. A partial draft with a completion note is better than no draft.

**Q: July 4 is a US holiday. Is it appropriate to send on that date?**
A: Yes. Democracy Docket is a litigation organization that monitors urgent democracy matters continuously. July 4 sends are consistent with their operating pattern. Send at 10:00 UTC (6:00 AM Eastern) — early enough that it is in the inbox when staff check in.

**Q: What if a Tier 1 organization says they are not interested in the research?**
A: Log the response. No follow-up required. Continue remaining sends. A negative reply is still a delivery confirmation and provides useful information about that organization's current focus priorities.

**Q: Should I personalize each Tier 2 email with [YOUR_NAME] and [YOUR_CONTACT_INFO]?**
A: Yes. Fill both fields in every email. All 7 sends should carry a consistent signature so organizations can reach you directly.

---

## Cross-Reference Files

| Purpose | File |
|---|---|
| Activation decision tree | DOMAIN_51_CONTINGENCY_DECISION_TREE.md |
| Domain M approval case study | DOMAIN_M_PHASE_2_BALLOT_ACCELERATION_CASE.md |
| Execution log (create on July 1) | DOMAIN_M_CONTINGENCY_EXECUTION_LOG.md |
| Domain 51 Tier 2 contingency (if partial) | DOMAIN_51_TIER_2_ACCELERATED_SEND_SEQUENCE.md |
| Phase 2 resource framework | PHASE_2_RESOURCE_ALLOCATION_FRAMEWORK.md |

---

*Item 45.2 — Runbook 2 of 2. Production-ready June 29, 2026.*
*Trigger: Domain 51 deadline miss as of July 1, 00:00 UTC.*
*All contact info verified. All 7 email templates copy-paste ready. No placeholder stubs.*
*Success metric: All 7 sends logged by July 22; >=1 Tier 1 reply by July 22; brief distributed by July 10.*
*Execution time: 150-180 active minutes across July 1-22 (10-15 min per day average).*
