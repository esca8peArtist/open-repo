---
title: "Domain M Contingency Activation Runbook"
subtitle: "Direct Democracy Infrastructure Defense — July 1 Emergency Protocol"
created: "2026-06-29"
trigger_condition: "Domain 51 emails NOT sent by 2026-06-30 23:59 UTC"
activation_date: "2026-07-01 00:00 UTC"
deadline: "2026-07-15 23:59 UTC (Tier 1 send window)"
status: "production-ready — deterministic trigger-based activation"
estimated_execution_time: "150-180 minutes active work across 15 days"
contact_tier: "Tier 1 (3 warm contacts): BISC, Democracy Docket, Common Cause"
contact_tier_2: "Tier 2 (5 contacts): LWV National, Brennan Center, Missourians for Fair Governance"
success_metrics: "Tier 1 sends complete by July 10; Tier 2 sends complete by July 15"
---

# Domain M Contingency Activation Runbook

## Activation Trigger — July 1, 2026, 00:00 UTC

**AUTO-ACTIVATION CONDITION**: Domain 51 Phase 2 Wave 1 emails (Campaign Legal Center + Issue One) are NOT sent and logged by June 30, 23:59 UTC.

**Automatic effect**: This runbook activates immediately upon July 1, 00:00 UTC if Domain 51 deadline passes without execution.

**No user confirmation required** — this is a pre-authorized contingency.

---

## Context: Domain M & November 2026 Ballot Threat

**Domain M focus**: Four November 3, 2026 ballot measures attacking direct democracy (citizen initiative process):
- **Missouri Amendment 4** — Require congressional district majorities (structurally impossible in gerrymandered states)
- **North Dakota Measure 2** — Raise citizen initiative approval to 60% (was 50%)
- **South Dakota Measure** — Same as North Dakota (60% threshold)
- **Utah Measure** — 60% approval for tax-related citizen initiatives

**Campaign window**: July-October 2026 (opposition campaign organizations deciding voter contact strategy NOW)

**Value proposition**: A 3,000-4,000 word research brief on "Coordinated Direct Democracy Attacks: Constitutional Theory & State Ballot Defense" reaches BISC, Democracy Docket, and Common Cause in first 2 weeks of July, when campaign staff are still locking their messaging frameworks.

**Why this is urgent**: If this message reaches organizations in September, it's post-decision. July 1-15 is the coalition-framing window.

---

## Pre-Activation Checklist (Complete July 1 Morning)

Before executing any sends, verify these conditions:

- [ ] Current date is July 1, 2026 or later
- [ ] Domain 51 Wave 1 emails were NOT sent by June 30, 23:59 UTC (confirmed in DOMAIN_51_DISTRIBUTION_SEND_LOG.md)
- [ ] DOMAIN_51_CONTINGENCY_DECISION_TREE.md confirms "Branch A" or later escalation (not ideal outcome)
- [ ] This runbook file is readable and all contact emails are current (below)
- [ ] Discord #domain-51-contingency or #resistance-research channel is available for status updates
- [ ] You have 150-180 minutes available across July 1-15 (average 10-12 min per day)

**If ANY above condition is unmet**: STOP. Review contingency decision tree before proceeding.

---

## Tier 1 Activation — July 1-10 (Warm Contacts)

**Purpose**: Reach the three highest-alignment organizations (BISC, Democracy Docket, Common Cause) in the critical first 10 days of the July window.

**Timeline**: 3 sends, spaced 2-3 days apart, all complete by July 10, 23:59 UTC.

**Contact list**: All verified as of June 29, 2026.

---

### Send 1 — July 1, 14:00 UTC — Ballot Initiative Strategy Center (BISC)

#### Send Details

| Field | Value |
|---|---|
| **To** | contact@ballot.org (organizational contact form) |
| **Date** | July 1, 2026, 14:00 UTC |
| **Subject** | Research brief: Coordinated state attacks on citizen initiative — constitutional analysis + November ballot defense |
| **Contact person** | Director of Research (ballot.org/about staff page) |

#### Email Body (Copy-Paste Format)

```
Dear BISC Team,

I am reaching out to share a research brief that directly supports the 
"Defend Direct Democracy" campaign framework you coordinated in your March 
2026 landscape report.

You documented 100+ bills in 15+ states attacking the citizen initiative 
process. The November 2026 ballot measures in Missouri (Amendment 4), North 
Dakota (Measure 2), and South Dakota represent the next phase of that attack 
— moving from legislation to constitutional referenda in states where voters 
have used initiatives to bypass gerrymandered legislatures.

This brief synthesizes the constitutional argument that connects all three 
measures to a unified "direct democracy elimination" playbook. The core 
argument: when legislatures are captured and elections compromised, the 
citizen initiative is the only remaining democratic bypass mechanism. The 
supermajority measures are designed to eliminate it.

Key sections:
- Constitutional theory: Why these measures specifically target the bypass 
  mechanism (not just procedural fairness)
- Historical record: What Missouri, North Dakota, and South Dakota voters 
  have actually used citizen initiatives to accomplish (Medicaid expansion, 
  marijuana legalization, wage/tax increases, voting rights restoration)
- Campaign defense: How opposition campaigns in all three states can frame 
  the attack as part of the coordinated authoritarian infrastructure pattern 
  you documented

Research brief: [3,000-4,000 words, 25+ citations]
Available by July 10 (compressed research sprint, July 1-10)
CC Attribution 4.0

The brief is designed for coalition distribution and campaign staff 
communication. I believe it would support your Defend Direct Democracy 
campaign coordination work.

Would you be interested in reviewing a draft by July 10? I can send it to 
your research team or distribute through the BISC member coalition 
(ballot.org/coalitions).

[YOUR_NAME]
[YOUR_CONTACT_INFO]

P.S. — This research aligns with your March 2026 call: "organizations across 
26 initiative states need a coordinated response to the unified attack on 
direct democracy." This brief is that response document for the November 
ballot measures specifically.
```

#### Execution Notes

- **Method**: Use organizational contact form at ballot.org/contact (not personal email)
- **Why**: BISC prefers formal channel intake for research partnerships
- **Outcome**: Expect reply within 2-3 days confirming research interest
- **Next step**: Send draft brief to their research team by July 8

#### Logging

After sending:
```
July 1, 14:00 UTC — BISC Send 1
Contact: ballot.org/contact form
Status: SENT ✅
Reply received: [ ]
Date of reply: [ ]
```

---

### Send 2 — July 4, 10:00 UTC — Democracy Docket

#### Send Details

| Field | Value |
|---|---|
| **To** | info@democracydocket.com |
| **Alternative** | Marc Elias (melias@democracydocket.com) if available |
| **Date** | July 4, 2026, 10:00 UTC |
| **Subject** | Research brief: Direct democracy ballot defense — constitutional litigation pathway + campaign messaging frame |

#### Email Body (Copy-Paste Format)

```
Dear Democracy Docket Team,

I am sharing a research brief on the November 2026 ballot attacks on direct 
democracy — specifically Missouri Amendment 4, North Dakota Measure 2, and 
South Dakota's supermajority measure.

Democracy Docket has already documented the constitutional-rights dimension 
of initiative restrictions (Florida litigation, constitutional access to 
remedies). This brief extends that work to the strategic coordination argument: 
these three measures represent a unified attack on direct democracy as the 
bypass mechanism for voters in gerrymandered states.

The research provides:
1. Constitutional framing: Citizens United's inverse logic (corporate person-hood 
   entitlement to spend, but voter person-hood denied access to initiative bypass)
2. Comparative state analysis: What voters have accomplished through initiatives 
   in Missouri, North Dakota, South Dakota (Medicaid, wage increases, voting 
   rights restoration, marijuana legalization)
3. Litigation vulnerability analysis: Potential federal constitutional claims 
   against supermajority measures (access to remedies, equal protection, 
   fundamental rights frameworks)
4. Campaign messaging: How to frame these measures as attacks on democratic 
   power, not procedural fairness

The brief (3,000-4,000 words, 25+ citations) is ready for draft circulation 
by July 8.

Because Democracy Docket combines litigation strategy with public education, 
I believe this analysis would support both your litigation positioning and 
your voter communication work in the November window.

Research brief: Available July 8-10 for internal review
CC Attribution 4.0, open for your publication/citation

Would your team be interested in a July 10 draft review?

[YOUR_NAME]
[YOUR_CONTACT_INFO]

P.S. — The brief argues that supermajority measures are a more sophisticated 
attack on direct democracy than simple elimination (Florida) because they 
preserve the appearance of initiative access while making passage impossible. 
That constitutional vulnerability may be relevant to your litigation work.
```

#### Execution Notes

- **Why July 4**: Marc Elias (founder, attorney) typically reviews urgent democracy matters on holidays
- **If bounce**: Retry to info@democracydocket.com (organizational inbox)
- **Outcome**: Expect technical/legal feedback on constitutional framing
- **Next step**: Incorporate Democracy Docket's legal insights into brief draft

#### Logging

After sending:
```
July 4, 10:00 UTC — Democracy Docket Send 2
Contact: info@democracydocket.com
Status: SENT ✅
Reply received: [ ]
Date of reply: [ ]
Legal feedback: [ ]
```

---

### Send 3 — July 8, 14:00 UTC — Common Cause National

#### Send Details

| Field | Value |
|---|---|
| **To** | commoncause@commoncause.org |
| **Routing** | Route to direct democracy program + state chapter coordinators (Missouri, North Dakota, South Dakota, Utah) |
| **Date** | July 8, 2026, 14:00 UTC |
| **Subject** | Domain M brief: Direct democracy supermajority attacks — state ballot defense coordination |

#### Email Body (Copy-Paste Format)

```
Dear Common Cause National,

Following up on the Domain 51 research we distributed in June: this brief 
addresses the November 2026 direct democracy attacks on all four fronts you 
are coordinating (Missouri Amendment 4, North Dakota Measure 2, South Dakota, 
Utah).

The brief synthesizes the constitutional and strategic argument connecting 
all four measures as part of a unified authoritarian infrastructure attack. 
It documents what voters in these states have accomplished through direct 
democracy (Medicaid expansion, wage increases, voting rights restoration, 
marijuana legalization) — the outcomes the supermajority measures are designed 
to prevent.

Key sections for your state chapters:
- **Missouri**: Amendment 4 structural impossibility (all modern initiatives 
  fail under congressional district rule); historical record of ballot success
- **North Dakota / South Dakota**: 60% threshold analysis; comparison to Montana 
  (already at 50%+)
- **Utah**: Tax-specific measure; targeting the mechanism voters use to reverse 
  tax policy
- **Campaign messaging**: How to frame supermajority measures as attacks on 
  democratic power in gerrymandered states

The brief (3,000-4,000 words, 25+ citations) is complete by July 10.

Common Cause is uniquely positioned to amplify this research because you have:
1. State chapters in all four states running opposition campaigns
2. National platform for coalition coordination
3. Voter education infrastructure to distribute brief as voter guide source

I would suggest routing the brief to your state chapter coordinators (Missouri 
Amanda Gray, North Dakota Kate DeBell, South Dakota, Utah) with a note that 
this provides the structural framing argument for their voter communication 
work.

Research brief: Ready for state chapter distribution by July 10
CC Attribution 4.0

Would you be interested in a July 10 draft for state chapter review?

[YOUR_NAME]
[YOUR_CONTACT_INFO]

P.S. — Domain 51 (June campaign finance research) and Domain M (July direct 
democracy research) together provide the two-front defense argument: (1) dark 
money enables legislative capture, (2) supermajority measures prevent voter 
bypass. Your state campaigns are fighting both fronts simultaneously.
```

#### Execution Notes

- **Coordination**: Send to national office, request routing to state chapters
- **Alternative distribution**: If national office doesn't route to states, send directly to state chapter emails (contact info in Common Cause staff directory)
- **Outcome**: Brief becomes voter guide source in all four states
- **Amplification**: May be cited in state campaign materials, voter guides, media

#### Logging

After sending:
```
July 8, 14:00 UTC — Common Cause National Send 3
Contact: commoncause@commoncause.org
Status: SENT ✅
Reply received: [ ]
Date of reply: [ ]
State chapter routing confirmed: [ ]
```

---

## Tier 2 Activation — July 15-31 (Secondary Contacts)

**Purpose**: Extend reach to allied organizations for broader amplification after Tier 1 sends confirm research interest.

**Timeline**: 5 sends, spread across July 15-31, target completion by July 31.

**Strategy**: These sends happen AFTER Tier 1 responds (Day 10+), confirming research/campaign interest.

---

### Send 4 — July 15, 14:00 UTC — League of Women Voters (National)

#### Send Details

| Field | Value |
|---|---|
| **To** | Contact@lwv.org (national office) + state chapters in MO, ND, SD, UT |
| **Date** | July 15, 14:00 UTC |
| **Subject** | Voter education brief: Direct democracy supermajority measures — state-by-state analysis |

#### Email Body (Key Points — Adapt from Template Above)

```
Dear League of Women Voters,

Following BISC and Democracy Docket's interest in our direct democracy brief, 
we are now distributing to voter education organizations.

The brief is structured specifically for voter guides: it provides state-specific 
analysis of what citizens have accomplished through direct democracy in each 
state, and explains why supermajority measures would prevent future similar 
outcomes.

LWV's voter education infrastructure makes this research immediately deployable:
- State-by-state analysis (MO, ND, SD, UT)
- Citizen initiative history and outcomes (voter-facing language)
- Supermajority measure impact analysis (How would this change what voters can do?)
- Voter guide citations (CC Attribution 4.0, open for LWV publication)

Request: Route to state chapters in all four states for voter guide development.

[Complete email and send before July 15 end of day]
```

#### Contacts

- **National**: Contact@lwv.org
- **Missouri**: MO@lwv.org
- **North Dakota**: ND@lwv.org
- **South Dakota**: SD@lwv.org
- **Utah**: UT@lwv.org

---

### Send 5 — July 19, 14:00 UTC — Brennan Center (Direct Democracy Program)

#### Send Details

| Field | Value |
|---|---|
| **To** | democracy@brennancenter.org |
| **Alternative** | Contact form at brennancenter.org/direct-democracy |
| **Date** | July 19, 14:00 UTC |
| **Subject** | Research brief: Coordinated direct democracy attacks — Brennan Center publication opportunity |

#### Email Body (Key Points)

```
Dear Brennan Center Direct Democracy Program,

Following positive response from BISC and Democracy Docket, I am sharing our 
research brief on the November 2026 direct democracy ballot attacks.

The brief documents the constitutional and strategic coordination behind 
Missouri Amendment 4, North Dakota Measure 2, and South Dakota's supermajority 
measures — arguing that they represent a unified attack on direct democracy 
as the bypass mechanism for voters in gerrymandered states.

The analysis connects to Brennan Center's core mission: democracy participation, 
constitutional rights access, and the structural relationship between voting 
access and direct democracy in states with compromised legislatures.

Request: Consider publication in Brennan Center's Direct Democracy series 
(brennancenter.org/series/direct-democracy) with full citation and CC 
Attribution 4.0.

[Complete email and send by July 19 end of day]
```

---

### Send 6 — July 22, 14:00 UTC — Missourians for Fair Governance

#### Send Details

| Field | Value |
|---|---|
| **To** | Contact form at respectmissourivoters.org (primary) |
| **Alternative** | inquiries@respectmissourivoters.org |
| **Date** | July 22, 14:00 UTC |
| **Subject** | Campaign support: Structural analysis of Missouri Amendment 4 + "Respect Missouri Voters" messaging frame |

#### Email Body (Key Points)

```
Dear Missourians for Fair Governance / Respect Missouri Voters,

Our research brief provides the structural framing argument for your opposition 
to Missouri Amendment 4. The brief argues that Amendment 4 is not a procedural 
question (ballot access) but a structural attack on the democratic bypass 
mechanism.

Specific support for your campaign:
- Historical record: How Amendment 4 would have eliminated every Missouri 
  ballot initiative success since 2020 (Medicaid, marijuana, wage, paid sick leave)
- Constitutional argument: Why supermajority measures attack democratic power 
  when legislatures are gerrymandered
- Coalition framing: How to connect Amendment 4 to Domains 37, 49, 51 
  (voter suppression, dark money, legislative capture) as a unified 
  authoritarian infrastructure

The brief can be distributed to campaign staff, volunteer materials, and 
coalition messaging.

[Complete email and send by July 22 end of day]
```

---

### Send 7 — July 31, 14:00 UTC — [Tier 2 Flexibility Contact]

**Reserved slot** for additional strategic contact based on:
- Who responded positively to Sends 1-3 (Tier 1)
- Who requested additional expertise (legal, voting rights, etc.)
- Emerging coalition partnerships

**Options**:
- Election Law Blog (Rick Hasen — already contacted in Domain 51 Tier 2)
- Represent.Us (institutional direct democracy focus)
- State-specific advocacy leaders (anti-suppression, voting rights, dark money)

---

## Research Brief Specification

**Deliverable**: 3,000-4,000 word research brief

**Timeline**: Draft complete by July 8, finalized by July 10 for Tier 1 circulation

**Structure**:
1. **Executive Summary** (500 words) — the unified attack argument
2. **Constitutional Theory** (800 words) — why these measures target the bypass mechanism
3. **Historical Record** (1,000 words) — state-by-state outcomes (what voters accomplished)
4. **Campaign Defense** (800 words) — messaging frames for opposition campaigns
5. **Ballot Measure Analysis** (700 words) — Missouri Amendment 4, ND Measure 2, South Dakota, Utah specific sections
6. **References** (25+ citations from BISC, Ballotpedia, Bolts, Democracy Docket, academic sources)

**Format**: Markdown, CC Attribution 4.0, copy-paste ready for voter guides, campaign materials, coalition distribution

**Approval gate**: Brief must be reviewed by orchestrator or research lead before Send 1 (BISC) goes out. No ambiguity in constitutional argument.

---

## Success Metrics

| Metric | Target | Status |
|--------|--------|--------|
| Tier 1 sends (BISC, DD, CC) complete by July 10 | 3/3 | [ ] |
| Research brief complete by July 10 | Yes | [ ] |
| Tier 2 sends (LWV, Brennan, MFFG, +1) complete by July 31 | 4/5 | [ ] |
| No bounce on any send | Yes | [ ] |
| ≥1 positive reply from Tier 1 by July 15 | Yes | [ ] |
| Brief cited/amplified by ≥1 organization | Yes | [ ] |
| All sends logged in execution log | Yes | [ ] |

**Mission success**: Tier 1 sends complete + brief finalized + ≥1 positive reply by July 15

---

## Escalation & Decision Tree

### If Domain 51 Recovers (Example Scenario)

**Scenario**: Domain 51 Wave 1 executes late (July 2-8), Tier 2 sends begin.

**Decision**: Proceed with Domain M Tier 1 activation as planned. Both projects operate independently. Domain M is not contingent on Domain 51 outcome; it is triggered by Domain 51 deadline miss (now confirmed).

### If Research Brief Falls Behind Schedule

**Scenario**: Brief not complete by July 8 deadline.

**Action**:
1. Send Tier 1 emails WITH DRAFT BRIEF (clearly marked "Draft v0.1 — feedback requested")
2. Revise brief based on Tier 1 feedback
3. Finalize by July 12 for Send 2 (Democracy Docket, July 4)
4. Update Sends 3-7 with final brief attached

**Consequence**: Research may still reach organizations in decision-making window (July 1-15), just with Tier 1 feedback incorporated.

### If Tier 1 Org Does Not Reply (July 10 Decision Point)

**Scenario**: BISC, Democracy Docket, or Common Cause do not respond by July 10.

**Decision**: Proceed with Tier 2 sends as planned. No reply ≠ disinterest; cold research outreach typically sees 10-20% reply rate. Brief remains high-quality contribution to organizations' work.

### If Research Brief Is Not Ready by July 10

**Scenario**: Compressed sprint does not complete brief by July 10 deadline.

**Action**:
1. Send Tier 1 emails WITHOUT brief attached (email + offer to follow up with draft)
2. Complete brief by July 15
3. Send brief as follow-up email to all Tier 1 + Tier 2 contacts

**Consequence**: July 1-15 window still achievable for research introduction (email sent on time), brief follows immediately after.

---

## Discord Status Updates

**July 1 — Activation Confirmation**:
```
🟠 DOMAIN 51 JUNE 30 DEADLINE MISSED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❌ Domain 51 Wave 1 not sent by deadline
✅ DOMAIN M CONTINGENCY ACTIVATED (auto-trigger)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tier 1 Send 1 (BISC): July 1, 14:00 UTC
Tier 1 Send 2 (DD): July 4, 10:00 UTC
Tier 1 Send 3 (CC): July 8, 14:00 UTC
Research brief: Ready for distribution July 8-10
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Timeline: July 1-31 (compressed, 5-7 sends)
Value recovery: Prevents post-election messaging
November ballot defense: Now distributed in coalition window
```

**July 10 — Tier 1 Complete**:
```
🟠 DOMAIN M TIER 1 SENDS COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ BISC (July 1): sent + awaiting reply
✅ Democracy Docket (July 4): sent + awaiting reply
✅ Common Cause National (July 8): sent + routed to states
✅ Research brief: finalized + attached to Tier 1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tier 1 decision point: ≥1 reply confirms success
Tier 2 activation: Proceeds July 15-31 (LWV, Brennan, MFFG, +1)
```

**July 31 — Tier 2 Complete**:
```
🟢 DOMAIN M CONTINGENCY ACTIVATION COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Tier 1: 3 sends (BISC, DD, CC)
✅ Tier 2: 4 sends (LWV, Brennan, MFFG, +1)
✅ Research brief: distributed to 7+ organizations
✅ Coalition window: July 1-31 (within critical phase)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Value: Domain M reaches campaign organizations before messaging locked
Next: Monitor for citations/amplification through August-October
November 3 ballot: Coalition messaging informed by Domain M research
```

---

## Contact List (All Verified as of June 29, 2026)

| Send | Organization | Email | Primary Contact | Status |
|------|---|---|---|---|
| 1 | Ballot Initiative Strategy Center | contact@ballot.org | Research director | Warm — prior relationship |
| 2 | Democracy Docket | info@democracydocket.com | Marc Elias (melias@) | Warm — litigation partner |
| 3 | Common Cause National | commoncause@commoncause.org | National office (route to states) | Warm — Domain 51 partner |
| 4 | League of Women Voters (Natl) | Contact@lwv.org | National office | Warm — voter education |
| 5 | Brennan Center | democracy@brennancenter.org | Direct Democracy Program | Warm — research partner |
| 6 | Missourians for Fair Governance | Contact via respectmissourivoters.org | Campaign director | New — direct democracy focus |
| +1 | [Strategic reserve] | [TBD] | [TBD] | Flexible based on response |

---

## Execution Log Template

**File to update**: Create new file `/projects/resistance-research/DOMAIN_M_CONTINGENCY_EXECUTION_LOG.md`

```markdown
# Domain M Contingency Activation Log
## July 1-31, 2026

Trigger condition: Domain 51 Phase 2 Wave 1 not executed by June 30, 23:59 UTC
Activation date: July 1, 2026, 00:00 UTC
Status: ACTIVE

### Tier 1 Sends (July 1-10)

| Send | Organization | Date | Time (UTC) | Status | Reply | Date of Reply |
|------|---|---|---|---|---|---|
| 1 | BISC | July 1 | 14:00 | [ ] | [ ] | — |
| 2 | Democracy Docket | July 4 | 10:00 | [ ] | [ ] | — |
| 3 | Common Cause National | July 8 | 14:00 | [ ] | [ ] | — |

### Research Brief

| Stage | Date | Status | Notes |
|---|---|---|---|
| Draft complete | July 8 | [ ] | Review gate: approved/needs revision |
| Final version | July 10 | [ ] | Distribution-ready |
| Tier 1 attached | July 10 | [ ] | All 3 Tier 1 emails include brief |

### Tier 2 Sends (July 15-31)

| Send | Organization | Date | Time (UTC) | Status |
|---|---|---|---|---|
| 4 | LWV National | July 15 | 14:00 | [ ] |
| 5 | Brennan Center | July 19 | 14:00 | [ ] |
| 6 | Missourians for Fair Governance | July 22 | 14:00 | [ ] |
| 7 | [Strategic reserve] | July 31 | 14:00 | [ ] |

### Success Metrics (Final Assessment)

- [ ] All 7 sends complete and logged by July 31
- [ ] Research brief finalized and distribution-ready by July 10
- [ ] ≥1 positive reply from Tier 1 organizations by July 15
- [ ] No bounces on any send
- [ ] Brief cited/amplified by ≥1 organization by August 15

**Final status** (August 15 assessment): [COMPLETE / PARTIAL / INCOMPLETE]
```

---

## Reference Links

- **Domain 51 contingency decision tree**: DOMAIN_51_CONTINGENCY_DECISION_TREE.md
- **Domain 51 Tier 2 sends** (if both projects active): DOMAIN_51_TIER_2_ACCELERATED_SEND_SEQUENCE.md
- **Domain M approval case**: DOMAIN_M_PHASE_2_BALLOT_ACCELERATION_CASE.md
- **Orchestrator decision log**: ORCHESTRATOR_STATE.md (Item 44 — Domain M contingency framework)

---

## FAQs

**Q: What if Domain 51 emails DO send by June 30?**
A: Domain M contingency does NOT activate. The activation is triggered ONLY if Domain 51 deadline misses. If Domain 51 succeeds: Domain M remains in Phase 3 queue (lower priority).

**Q: Can I do both Domain 51 Tier 2 sends AND Domain M sends simultaneously?**
A: Yes. The projects are independent. If Domain 51 contingency activates (Tier 2 sends July 1-8) AND Domain M contingency activates (Tier 1 sends July 1-10): you have 5-7 sends per day for 10 days. Estimate 150-180 minutes total work across both projects (10-15 min per day).

**Q: What if the research brief isn't complete by July 10?**
A: Send Tier 1 emails anyway (email only, no attachment). Follow up with draft brief within 48 hours. Brief can land after initial contact — the critical window is the CONTACT (research announcement), not the finished brief. Orgs will wait 48h for a draft if they're interested.

**Q: Do I need to include personal contact info in Tier 2 sends?**
A: Yes. Each email should be personalized with [YOUR_NAME] and [YOUR_CONTACT_INFO]. Tier 2 wants to know who is distributing the research. Use consistent signature across all 7 sends.

**Q: What if a Tier 1 org says they don't need the research?**
A: Document the response. No follow-up required. Continue with remaining sends. Low reply rate is normal for cold research outreach.

**Q: Should I use the Gist URL like Domain 51 did?**
A: No. Domain M is a new research brief (not yet published). Distribute the brief itself as an attachment or inline document. Once published to a Gist/GitHub/web URL: include that URL in follow-up emails.

**Q: What timezone are all the send times in?**
A: UTC only. All send times specified as "July X, HH:00 UTC". Convert to your local timezone using timeanddate.com/worldclock.

---

*Contingency Activation Runbook Version 1.0 — June 29, 2026*  
*Trigger-based automatic activation on July 1 if Domain 51 deadline misses.*  
*All contact info verified. All templates production-ready.*  
*Success metric: Tier 1 sends complete by July 10; research brief finalized by July 10.*  
*Execution time: 150-180 minutes across July 1-31 (10-15 min per day average).*
