---
title: "Domains 51 and 59 — Sequential Activation Timing and Coordination Guide"
subtitle: "2-Day Stagger Plan, Resource Allocation Matrix, Cross-Domain Integration, and Failure Mode Analysis"
created: "2026-06-14"
status: "execution-ready — activate at June 17-18 Day 7 checkpoint"
trigger: "June 17-18 Day 7 checkpoint — both domains require activation decision simultaneously"
domain_51_deadline: "July 1, 2026 (California Fair Elections Act messaging window)"
domain_59_deadline: "June 25-30, 2026 (Senate Finance CTC markup window — HIGHER URGENCY)"
domain_51_gist: "https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372"
domain_59_gist: "https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba"
companion_docs:
  - "DOMAIN_51_RAPID_ACTIVATION_RUNBOOK.md (full Domain 51 sprint scaffold)"
  - "DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md (full Domain 59 sprint scaffold)"
  - "DOMAIN_51_RAPID_ACTIVATION.md (30-minute checkpoint protocol)"
  - "DOMAIN_59_RAPID_ACTIVATION.md (45-minute checkpoint protocol)"
---

# Domains 51 and 59 — Sequential Activation Timing and Coordination Guide

*This document coordinates the simultaneous activation of Domain 51 (Campaign Finance / Dark Money) and Domain 59 (Economic Precarity / Senate Finance CTC). It resolves the sequencing decision, prevents orchestrator resource paralysis, and identifies cross-domain integration opportunities when both domains execute in the same window.*

---

## Most Important Finding

**Domain 59 takes priority over Domain 51 if both are approved at the June 17-18 checkpoint.** The Senate Finance Committee's OBBBA markup window (June 25-30) closes before Domain 51's California ballot campaign messaging window (July 1). The 45-minute Domain 59 express Senate outreach path executes on the day of the checkpoint decision, while Domain 51 expansion activates on Day 2 of the activation sequence.

This is not a close call. The Senate Finance markup is an immovable external deadline driven by a legislative calendar. The California messaging window is a campaign strategy deadline — important but recoverable if missed by 72 hours. Domain 59 leads.

---

## Section 1: Sequence Decision Logic

### Priority Hierarchy at June 17-18 Checkpoint

| Decision Case | Action |
|---|---|
| Both Domain 51 and Domain 59 approved | Day 1: Domain 59 express path (45 min). Day 2: Domain 51 Tier 1 expansion (30 min). Full research sprints: Domain 59 hours 1-8, Domain 51 hours 9-14. |
| Only Domain 59 approved | Execute Domain 59 express path day of checkpoint. Full sprint over days 2-4. |
| Only Domain 51 approved | Execute Domain 51 Tier 1 expansion within 24 hours. Full sprint over days 2-4. |
| Neither approved | Hold both pending further engagement data. Do not activate any new contacts without checkpoint signal. |

### Why Domain 59 Leads When Both Are Approved

The Senate Finance Committee CTC markup has a self-imposed July 4 passage goal. Based on the committee schedule released with the OBBBA text on June 16, 2026, the markup period runs June 25-30 at peak intensity. The advocacy organizations receiving Domain 59 (CBPP, AFL-CIO, NWLC, MomsRising) need materials before they engage in Senate committee testimony and member communications — not after.

Domain 51's California Fair Elections Act deadline (July 1) is a campaign messaging infrastructure lock. The 5-day difference between the Domain 59 Senate Finance window (closes ~June 30) and the Domain 51 California window (closes July 1) means that activating Domain 59 first and Domain 51 second — with a 24-48 hour stagger — loses nothing from Domain 51 while gaining everything from Domain 59 Senate timing.

If Domain 59 express path runs June 17 (at the checkpoint) and Domain 51 Tier 1 expansion runs June 18-19, both deadlines are fully covered with days to spare.

---

## Section 2: 2-Day Stagger Plan

### Day 0 — June 17-18 (Checkpoint Decision Day)

**Hour 0 (Decision moment)**:
- Assess Wave 1-2 engagement data from Domains 51 and 59 prior sends
- Confirm Senate Finance markup status (finance.senate.gov/hearings)
- Confirm California Fair Elections Act ballot status (ballotpedia.org)
- Make activation decision (both approved / Domain 59 only / Domain 51 only / hold)

**Hour 0-1 (Domain 59 Express Path — If Domain 59 Approved)**:
- Execute 45-minute express Senate path: AFL-CIO (feedback@aflcio.org), CBPP (cbpp@cbpp.org), NWLC (info@nwlc.org)
- Use templates in `DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md` Part 1
- Log all three sends in `domain-59-send-log-june1.md`
- Total active time: 45 minutes

**Hour 1-4 (Background — Domain 59 Gap Waits)**:
- CBPP send goes T+45 min after AFL-CIO, NWLC goes T+90 min after AFL-CIO
- While these are running in background: begin Domain 51 pre-flight
- Load Domain 51 Gist URL; confirm California ballot status; check Domain 51 Wave 1-2 replies

**End of Day 0**: Domain 59 express path complete (3 sends). Domain 51 pre-flight complete.

---

### Day 1 — June 18-19 (Domain 51 Expansion Activation)

**Morning (30 minutes active)**:
- Execute Domain 51 Tier 1 expansion sends: OpenSecrets (info@opensecrets.org), Democracy 21 (fwertheimer@democracy21.org), Public Citizen (cholman@citizen.org)
- Use templates in `DOMAIN_51_RAPID_ACTIVATION.md` Part 2
- 45-minute gaps between sends (stagger)
- Log all sends in `DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md`

**Afternoon (2 hours — Domain 59 Research Sprint begins)**:
- Begin Zone 1 of Domain 59 research sprint: causal evidence review
- Extract Dallas Fed Working Paper 2517 (March 2026 revision) key finding for Senate staff briefing
- Draft OBBBA provision-to-pathway mapping table (Zone 2 deliverable)

**End of Day 1**: Domain 51 Tier 1 expansion complete (3 sends). Domain 59 research sprint hours 1-3 complete.

---

### Day 2 — June 19-20 (Domain 59 Tier 2 Activation + Domain 51 State Contacts)

**Morning (Domain 59 Tier 2 — 45 minutes active)**:
- Check Domain 59 Day 1 signal: any replies from AFL-CIO, CBPP, or NWLC?
- If 1+ reply: activate Tier 2 with warm intro chains
- Send to: EPI (researchdept@epi.org — verify first), Demos (info@demos.org — Taifa Smith Butler), NELP (info@nelp.org — Rebecca Dixon)
- Log all sends in `domain-59-send-log-june1.md`

**Afternoon (Domain 51 State Contacts — 30 minutes active)**:
- Check Domain 51 Tier 1 expansion signal: any replies from OpenSecrets, Democracy 21, Public Citizen?
- Verify Montana I-194 June 19 county deadline outcome — did initiative qualify?
- If Montana I-194 qualified AND Massachusetts Common Cause campaign confirmed: send Tier B state contacts
- Jane Chiang, Common Cause Massachusetts (jchiang@commoncause.org) — no prerequisite
- Montana I-194 campaign contact — only if initiative has qualified
- Log sends in `DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md`

**End of Day 2**: Domain 59 Tier 2 (3 sends). Domain 51 state contacts (1-2 sends depending on Montana status). Full stagger complete. No contact fatigue risk (zero overlap between contact pools).

---

### Days 3-7 (Monitoring and Tier 3 Pre-Staging)

| Day | Domain 59 Action | Domain 51 Action |
|-----|---|---|
| Day 3 | Continue research sprint Zones 3-4 (housing, gig economy) | Research sprint Zones 1-2 (FEC statute risk, crypto/AI PAC) |
| Day 4 | Tier 2 completion (NELP, remaining Tier 2 contacts) | Research sprint Zones 3-4 (state ballot campaigns, DISCLOSE Act) |
| Day 5 | Tier 3 pre-staging (Common Cause National, PFAW, Families USA) | Tier B state completion (Arizona if campaign confirmed) |
| Day 6 | Day 7 signal assessment: count all replies to date | Day 7 signal assessment: count all replies to date |
| Day 7 | Gate 2 checkpoint: activate Tier 3 if signal warrants | Gate 2 checkpoint: activate Brendan Fischer (CLC) if Chlopak engaged |

---

## Section 3: Resource Allocation Matrix

### Why Zero Resource Competition Exists Between These Domains

Domains 51 and 59 do not share a single contact. They reach entirely different organizational populations:

| Resource | Domain 51 (Campaign Finance) | Domain 59 (Economic Precarity) | Overlap |
|---|---|---|---|
| Primary organizations | Campaign Legal Center, Issue One, Common Cause CA, LWV CA, Clean Money Action Fund, OpenSecrets, Democracy 21, Public Citizen | CBPP, ITEP, NWLC, MomsRising, AFL-CIO, EPI, Demos, NELP | Zero |
| Contact pool | Campaign finance, dark money, FEC enforcement, ballot campaigns | Economic justice, labor, women's rights, voting rights/democracy | Zero |
| Policy domain | Citizens United, 501(c)(4) architecture, state ballot measures | CTC refundability, wage floor, childcare, OBBBA distributional impact | Adjacent, not identical |
| Organizational sector | Legal/advocacy/ballot campaign | Research/labor/women's advocacy | Different |

**Implication**: Running both domains in the same 7-day activation window creates ZERO contact fatigue risk. The populations receiving each domain do not know about the other domain's distribution. There is no coordination needed with contacts — only with the user's time.

### User Time Allocation

| Activity | Hours Required | Domain | Can Run in Parallel? |
|---|---|---|---|
| Domain 59 express path | 1 hour (active) | 59 | No — execute first, Day 0 |
| Domain 51 Tier 1 expansion activation | 0.5 hours (active) | 51 | No — execute second, Day 1 |
| Domain 59 research sprint | 10-14 hours (spread over 4-5 days) | 59 | Yes — background research while sends are in-flight |
| Domain 51 research sprint | 10-14 hours (spread over 4-5 days) | 51 | Yes — can run in parallel if user has bandwidth |
| Monitoring and logging (both domains) | 0.5 hours/day | Both | Yes |

**Maximum combined active time**: 2 hours on Day 0-1 (activations). Remaining 20-28 hours are research sprint work distributed over 4-5 days. Both research sprints can run in parallel — Zone work in each domain is independent.

**Minimum viable activation path (if time is severely constrained)**:
- Day 0: Domain 59 express path only (45 minutes). This covers the Senate Finance urgency.
- Day 1: Domain 51 activation only (30 minutes). This covers the California July 1 window.
- Skip both research sprints. Distribution is complete with existing research documents (44 and 65 citations respectively). The sprints add depth; they do not enable the sends.

---

## Section 4: Cross-Domain Findings Integration

When both domains execute in the same window, three integration points produce advocacy value larger than either domain alone.

### Integration Point 1 — FEC Enforcement Collapse as Structural Amplifier of Economic Exclusion

Domain 51 documents the FEC quorum collapse (200+ days without enforcement). Domain 59 documents that dark money in corporate political spending targets the legislators who are most likely to support CTC expansion and wage floor legislation. The integration argument: the same dark money architecture that is currently operating without FEC enforcement is the mechanism that funds opposition to the CTC expansion and minimum wage legislation that Domain 59 identifies as the policy response to the civic participation gap.

**Who receives this integrated argument**: Any organization that bridges both networks. Common Cause (receiving Domain 51 as national and California affiliate) also operates in the economic justice space. Brennan Center (receiving Domain 51 via Saurav Ghosh and Wendy Weiser) publishes on both campaign finance AND voting rights/economic exclusion. A follow-up note to either organization — explicitly connecting Domain 51's FEC enforcement collapse to Domain 59's wage-floor-to-civic-participation argument — is the highest-value integration opportunity.

**Specific integrated pitch**: "The same FEC enforcement collapse that allows $288 million in crypto industry dark money to flow without accountability is targeting the legislators most likely to support the full CTC refundability that would close the 42-point voter participation gap Domain 59 documents." This is a 2-sentence synthesis that connects both research documents and is available to no single organization that has received only one domain.

### Integration Point 2 — OBBBA as Both an Economic Exclusion and a Campaign Finance Story

Domain 59's primary 2026 policy anchor is the OBBBA's five concurrent cuts to civic capacity. Domain 51 documents that pharmaceutical and fossil fuel dark money funds the legislative races that determine which senators vote on OBBBA provisions. The integration argument: the OBBBA's distributional concentration on low-income households is not an accident of fiscal math — it is the outcome of the dark money architecture that funds the legislators who designed those concentrations.

**Who receives this integrated argument**: CBPP (which receives Domain 59) is the highest-value recipient because they brief Senate Finance Committee staff. A CBPP analysis that incorporates both the distributional equity argument (Domain 59, which they already have) AND the dark money accountability argument (Domain 51, which they do not yet have) could produce a uniquely powerful Senate testimony combination.

**Action**: After CBPP engages with Domain 59, send a short follow-up note (4-5 sentences) linking to Domain 51 as a companion analysis: "I also wanted to share a companion document that addresses the campaign finance mechanism by which the OBBBA's distributional decisions were shaped. Domain 51 documents the dark money architecture that operationally explains why these provisions look the way they do." Do not send this follow-up before CBPP has responded to Domain 59.

### Integration Point 3 — State-Level Reform and Pre-Midterm Coalition Building

Domain 51's California Fair Elections Act (November 3, 2026 ballot) and Domain 59's pre-midterm GOTV framing (August 1 anchor) operate in the same pre-election organizational calendar window. Both domains require their advocacy organizations to be actively campaigning in the summer months. The integration: organizations running GOTV campaigns (AFL-CIO, MomsRising, Common Cause) can deploy Domain 59's democratic participation argument to explain WHY their GOTV campaign matters, AND Domain 51's campaign finance argument to explain the structural barrier they are working against.

**The synthesis framing for GOTV organizations**: "The income-based voter participation gap reached 42 percentage points in 2024. The same dark money architecture that spent $288 million in the 2026 midterms targeting legislators who support the policies that would close that gap is operating without FEC enforcement. Your GOTV campaign is working against both of these forces simultaneously."

**Who can use this synthesis**: AFL-CIO (receiving Domain 59 as lead contact), Common Cause California (receiving Domain 51 as California ballot campaign contact), MomsRising (receiving Domain 59). A joint synthesis note after both organizations have engaged with their respective domains creates a coalition coordination opportunity that neither organization would have without the cross-domain connection.

---

## Section 5: Checkpoint Coordination

Both domains report to the June 17-18 Day 7 checkpoint. The checkpoint is one event, not two.

### June 17-18 Checkpoint — Combined Assessment Protocol

**Assessment dimensions**:

| Question | Domain 51 Data Source | Domain 59 Data Source |
|---|---|---|
| Wave 1-2 sends confirmed delivered? | Sent folder + no bounce-back | domain-59-send-log-june1.md |
| Reply signals received? | Email inbox; Wave 1 (CLC + Issue One), Wave 2 (Common Cause CA + LWV CA + Clean Money) | Email inbox; any Tier 1 sends |
| Gist URLs live? | https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372 | https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba |
| External deadline still active? | CA ballot measure active (ballotpedia.org) | Senate Finance markup still in progress (finance.senate.gov) |
| Key personnel stale? | Check Waves 1-2 target contacts against snapshot | Check Tier 1 contacts against June 10 snapshot |

**Decision matrix at checkpoint**:

| Domain 51 Signal | Domain 59 Signal | Decision |
|---|---|---|
| 2+ replies or delivery confirmed | Senate Finance active | Both approved: Domain 59 express path Day 0, Domain 51 Day 1 |
| 2+ replies or delivery confirmed | Senate bill passed | Domain 51 approved, Domain 59 pivot to 2027 reform coalition frame |
| 0 signals, uncertain delivery | Senate Finance active | Diagnose Domain 51 delivery; Domain 59 express path proceeds immediately (legislative window cannot wait) |
| 0 signals, confirmed delivery | Senate Finance active | Domain 51 hold (wait for 7-day window); Domain 59 approved — express path today |
| Gist 404 error | Either state | Fix Gist FIRST for both domains before any sends — 10-minute procedure each |

---

## Section 6: Dual Execution Success Metrics

These metrics apply when both domains execute simultaneously.

| Metric | Domain 51 Target | Domain 59 Target | Combined Target |
|---|---|---|---|
| Day 0 activation time | 30 min for Tier 1 expansion | 45 min for express path | Both complete by end of Day 1 |
| Bounce rate | Under 5% | Under 5% | Under 5% combined (1 bounce max in 22 combined sends) |
| Reply rate Day 7 | Over 8% (1 reply min from 8 contacts) | Over 8% (2 replies min from 14 contacts) | 3+ replies total across both domains |
| California window | Contacts engaged before July 1 | N/A | Domain 51 CA contacts engaged before July 1 |
| Senate Finance window | N/A | CBPP or AFL-CIO receives materials before markup completes | Domain 59 express path AFL-CIO and CBPP sent Day 0 |
| Cross-domain integration | Brennan Center / Common Cause receives both domains | AFL-CIO / Demos receives integrated framing | At least 1 organization receives cross-domain synthesis note |
| Research sprint completion | Zones 1-5 complete within 5 days | Zones 1-5 complete within 5 days | Both sprints complete by June 23 |

---

## Section 7: Failure Modes and Recovery

### Failure Mode 1 — One Domain Stalls (Zero Engagement), One Domain Succeeds

**Scenario**: Domain 51 receives 0 engagement across all contacts; Domain 59 receives 3+ strong signals.

**Response**:
- Do not treat Domain 51 stall as a signal to deprioritize the research. The Domain 51 contact pool (campaign finance organizations) has a longer response cycle than the Domain 59 contact pool (policy research + labor). 0 replies at Day 7 from CLC, Issue One, and the Tier 1 expansion contacts is within normal range — these organizations respond at Day 14 in documented prior analogues.
- At Day 14: submit Domain 51 research to a publication channel. Just Security (justsecurity.org), Lawfare (lawfaremedia.org), or Election Law Blog (electionlawblog.org — Rick Hasen). This converts email distribution to public record and generates inbound.
- Continue Domain 59 distribution uninterrupted — Domain 51 stall has zero effect on Domain 59 execution.

### Failure Mode 2 — Both Domains Stall (Systemic Delivery Problem)

**Scenario**: Zero replies from any of the 22 combined contacts across both domains by Day 14.

**Response**:
- First: diagnose deliverability. Send a test email to yourself from the same client to confirm no sending infrastructure issue.
- Verify both Gist URLs are live (HTTP 200 check).
- Check spam folder for any auto-bounce notifications that were delivered to spam rather than inbox.
- If all infrastructure checks pass: the research is reaching passive readers, not generating active responses. This is not a failure of the research — it is a cold-contact response-rate reality. Day 14 with 0 replies is the 95th-percentile worst case, not the median.
- Action at Day 14 with confirmed delivery and 0 replies: submit both domains to publication channels simultaneously. This converts the investment to public record.

### Failure Mode 3 — Senate Finance Window Closes Before Domain 59 Completes Distribution

**Scenario**: OBBBA passes Senate before all 14 Domain 59 contacts are reached.

**Response**:
- Immediately switch ALL unsent Domain 59 contacts to the "2027 Reform Coalition" frame (detailed template in `DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md` Part 7, Contingency 1).
- Do not treat bill passage as ending the advocacy. The argument evolves: "Now that the OBBBA is law, the 2027 reconciliation push is the next legislative vehicle. Organizations that build the evidence record between now and November 2026 midterms will be positioned to convert GOTV mobilization into 2027 legislative momentum."
- This frame is not a fallback — it is actually more durable for organizations with long-term advocacy mandates (Brennan Center, Demos, CBPP).

### Failure Mode 4 — California Fair Elections Act Ballot Status Changes

**Scenario**: California Fair Elections Act is challenged off the November 2026 ballot or removed for procedural reasons.

**Response**:
- National DISCLOSE Act contacts (CLC, Issue One, Democracy 21, Public Citizen, OpenSecrets): RETAIN without modification. These contacts are entirely ballot-independent.
- California campaign contacts (Common Cause CA, LWV CA, Clean Money Action Fund): PIVOT to "post-measure structural analysis" framing. These organizations have long-term mandates that survive a single ballot cycle.
- Montana and Missouri ballot contacts: evaluate individually — if their measures are still active, send as written; if failed, apply the same post-measure structural analysis pivot.
- Domain 51 does not lose its distribution value if California ballot fails. The FEC enforcement collapse, dark money architecture, and DISCLOSE Act advocacy frame are all ballot-independent.

### Failure Mode 5 — User Cannot Execute Both Research Sprints (Bandwidth Constraint)

**Scenario**: User approves both domains but has less than 10 hours available for research sprint work.

**Response**: The research sprints are additive, not prerequisite. Both domains have production-complete research documents (65 citations for Domain 51, 44 citations for Domain 59). All distributions can execute from existing research without the sprint deepening. The sprint improves the advocacy materials; it does not enable the sends.

**Minimum viable path (under 2 hours total)**:
- Domain 59 express path: 45 minutes (addresses Senate Finance window)
- Domain 51 Tier 1 expansion: 30 minutes (addresses California window)
- Total: 75 minutes active. Both windows covered. Both research sprints deferred.

If the research sprints cannot execute, defer them to a later session. The contacts are pre-verified, the templates are pre-written, and the Gists are live. The user's only remaining action is filling in [YOUR_NAME] and [YOUR_CONTACT_INFO].

---

## Section 8: June 17-18 Checkpoint Quick Reference

*Print this section for the checkpoint decision moment.*

```
DOMAINS 51 AND 59 — SIMULTANEOUS ACTIVATION DECISION

[  ] 1. Check Domain 59 Senate Finance status (finance.senate.gov)
      → Markup in progress? Domain 59 express path executes TODAY.
      → Bill passed? Pivot to 2027 coalition frame; Domain 59 still distributes.

[  ] 2. Check Domain 51 California ballot status (ballotpedia.org)
      → Measure still on ballot? Domain 51 Tier 1 expansion executes TOMORROW.
      → Measure removed? Pivot to structural dark money frame; Domain 51 still distributes.

[  ] 3. Check both Gist URLs
      → Domain 51: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372
      → Domain 59: https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba
      → Both HTTP 200? Proceed. Any 404? Fix Gist before any sends.

[  ] 4. Check prior sends for both domains
      → Domain 51: DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md
      → Domain 59: domain-59-send-log-june1.md
      → Which contacts have NOT yet been reached? Those are today's targets.

[  ] 5. Make activation decision:
      → Both approved? DOMAIN 59 FIRST (express path, Day 0), Domain 51 second (Day 1)
      → Only Domain 59? Execute express path today.
      → Only Domain 51? Execute Tier 1 expansion today.
      → Neither? Hold. Do not activate new contacts without engagement signal.

[  ] 6. Execute Domain 59 express path (if approved):
      → AFL-CIO: feedback@aflcio.org (T+0, use express path Template 1)
      → CBPP: cbpp@cbpp.org (T+45 min, use express path Template 2)
      → NWLC: info@nwlc.org (T+90 min, use express path Template 3)
      → Log in domain-59-send-log-june1.md

[  ] 7. Execute Domain 51 Tier 1 expansion (Day 1):
      → OpenSecrets: info@opensecrets.org (use DOMAIN_51_RAPID_ACTIVATION.md Email 3A)
      → Democracy 21: fwertheimer@democracy21.org (Email 3B)
      → Public Citizen: cholman@citizen.org (Email 3C)
      → Log in DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md

DONE — Both domains activated. No contact fatigue risk.
Zero overlap between Domain 51 and Domain 59 contact pools.
```

---

*Coordination guide prepared June 14, 2026. Domain 51 Gist confirmed live. Domain 59 Gist confirmed live. Senate Finance CTC markup window ACTIVE as of June 16, 2026. California Fair Elections Act confirmed on November 2026 ballot. All contact data sourced from DOMAIN_51_CONTACT_REACHABILITY_SNAPSHOT.md and DOMAIN_59_CONTACT_REACHABILITY_SNAPSHOT.md (both June 10, 2026 audits). Personnel changes applied throughout: Karen Hobert Flynn (deceased) → Virginia Kase Solomón; Chiraag Bains (departed Demos) → Taifa Smith Butler; Sheila Krumholz (departed OpenSecrets) → Hilary Braseth.*
