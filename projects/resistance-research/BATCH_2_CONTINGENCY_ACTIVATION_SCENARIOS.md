---
title: "Batch 2 Contingency Activation Scenarios"
created: "2026-06-04"
status: "production-ready"
session: "General Research Agent — Item 57, June 4 deadline"
cross_references:
  - BATCH_2_RESOURCE_ALLOCATION_MATRIX.md
  - BATCH_2_JUNE_CHECKPOINT_READINESS_PROTOCOL.md
  - PHASE_2_BATCH_2_ACTIVATION_ROADMAP.md
  - DOMAIN_49_EXECUTION_PREFLIGHT.md
  - DOMAIN_49_CONTINGENCY_DECISION_TREE.md
---

# Batch 2 Contingency Activation Scenarios

*General Research Agent — June 4, 2026*
*Item 57 — Decision-Agnostic Execution Plan for All Domain 49 Timing Paths*

---

## How to Use This Document

The user decides Domain 49 timing. The orchestrator reads this document, selects the matching scenario letter, and executes per that scenario's timeline without re-planning. Each scenario is self-contained. Decision gates within each scenario are quantified — there is no judgment call required at the gates, only measurement against thresholds.

**Decision rule**: User announces Domain 49 timing → Orchestrator selects Scenario A, B, C, or D → Execute from the Hour 0 start point of that scenario.

---

## Scenario A — Approved (Fast)
**Domain 49 executes June 4–5. Domain 51 June 9–12. Parallel Domain 48 optional.**

### When to use
User approves Domain 49 by EOD June 3 or early June 4. The redistricting cascade (Louisiana signed map June 1, primary filing deadlines mid-June) makes immediate execution the highest-value choice.

### Hour-by-Hour Timeline: June 4–15

**June 4 (Day 1) — Domain 49 Full Launch**

| UTC Time | Action | Time Required | Who |
|----------|--------|---------------|-----|
| 08:00 | Create Domain 49 Gist from `domain-49-callais-vra-redistricting-emergency.md` | 15 min | User |
| 08:30 | Send: NAACP LDF (naacpldf@naacpldf.org) — Template T1 | 10 min | User |
| 09:00 | Send: Democracy Docket (democracy@democracydocket.com) — Template T2 | 10 min | User |
| 13:00 | Send: Campaign Legal Center (clcinfo@campaignlegal.org) — Template T3 | 10 min | User |
| 15:00 | Send: LULAC (lulac@lulac.org) — Template T4 | 10 min | User |
| 19:00 | Send: MALDEF (info@maldef.org) — Template T5 | 10 min | User |
| 21:00 | Log all 5 sends in DISTRIBUTION_EXECUTION_LOG.md | 5 min | User |

**Day 1 total user time: 1.25 hours**

**June 5 (Day 2) — Domain 49 Tier 2 and First Assessment**

| UTC Time | Action | Time Required | Who |
|----------|--------|---------------|-----|
| 09:00 | Check inbox: any Day 1 replies? Apply Day 1 assessment (below) | 10 min | User |
| 09:30 | Send: Advancement Project — Template T6 | 10 min | User |
| 10:00 | Send: Lawyers' Committee for Civil Rights (lawyerscommittee@lawyerscommittee.org) | 10 min | User |
| 12:00 | Send: Common Cause (press@commoncause.org, redistricting frame) | 10 min | User |
| 15:00 | Send: ACLU Voting Rights Project (voting@aclu.org) | 10 min | User |
| 17:00 | Update log; note any patterns in open/reply data | 10 min | User |

**Day 2 total user time: 1.0 hour**

**June 6–8 (Days 3–5) — Monitoring and Domain 51 Prep**

- Days 3–5: Passive monitoring. Check inbox once/day (5 min). Log any replies.
- June 8 (Day 5): **Domain 39 Day 7 checkpoint** — 30 minutes. Record Domain 39 open rates, reply counts, Gist views from distinct IPs. Apply threshold (see Checkpoint Protocol). This data does NOT gate Domain 51 — Domain 51 proceeds regardless of Domain 39 signal.
- June 8 EOD: Confirm Domain 51 Gist is loading (check DISTRIBUTION_GIST_URLS.md — Domain 51 entry). This is the only Domain 51 pre-send prep step needed.

**June 9 (Day 6) — Domain 51 Wave 1 + Domain 49 Day 5 Assessment**

| UTC Time | Action | Time Required | Who |
|----------|--------|---------------|-----|
| 09:00 | Domain 49 Day 5 assessment: count replies, Gist views | 10 min | User |
| 09:30 | Domain 51 send: Campaign Legal Center (info@campaignlegal.org, dark money template) | 10 min | User |
| 10:30 | Domain 51 send: Issue One (info@issueone.org, ReFormers Caucus template) | 10 min | User |
| EOD | Log both Domain 51 sends in DISTRIBUTION_EXECUTION_LOG.md | 5 min | User |

**June 10 (Day 7) — Domain 49 Day 7 Checkpoint**

| Action | Time | Notes |
|--------|------|-------|
| Domain 49 Day 7 checkpoint: full engagement assessment | 20 min | Apply Strong/Moderate/Caution thresholds (below) |
| Domain 51 follow-up check: any replies to June 9 sends? | 5 min | Log; no action needed unless reply warrants response |
| Domain 49 Tier 3 decision: accelerate or hold? | 10 min | Apply Day 7 thresholds |

**June 11–12 (Days 8–9) — Domain 51 Wave 2 + Domain 48 Optional**

| UTC Time | Action | Time Required | Who |
|----------|--------|---------------|-----|
| June 11, 09:00 | Domain 51: Common Cause CA send | 12 min | User |
| June 11, 09:30 | Domain 51: LWV California send | 10 min | User |
| June 11, 10:00 | Domain 51: Clean Money Action Fund send | 12 min | User |
| June 12 | Montana contingency check + Domain 51 log update | 20 min | User |
| June 12 | Domain 48 Gist creation (OPTIONAL — only if user has capacity) | 15 min | User |

**June 13–15 (Days 10–12) — Monitoring and June 15 Checkpoint Prep**

- Domain 39 Day 14 checkpoint (June 15): 30 min. Record engagement metrics across all Phase 1 domains.
- Confirm stockbot June 15 checkpoint result. If PASS and Lever B activates: note Domain 48 June activation defers to July 5–10; all other Batch 2 timelines unaffected.
- Update DISTRIBUTION_EXECUTION_LOG.md for all active domains.

---

### Decision Gates: Scenario A

**Day 3 Assessment (June 7 — check in evening)**

| Signal | Threshold | Action |
|--------|-----------|--------|
| Strong | 2+ replies from Tier 1 contacts (any content) | Confirm Domain 49 Tier 3 send list (add Brennan Center, CLC Media, state-level contacts) |
| Moderate | 1 reply OR 4+ Gist views from distinct IPs | Proceed as planned; no acceleration |
| Caution | 0 replies AND <3 Gist views | Check delivery: forward to personal email; verify send from non-spam address |

**Day 7 Assessment (June 10)**

| Signal | Threshold | Action |
|--------|-----------|--------|
| Strong (>20% open rate equivalent) | 3+ replies from 9 contacts, 2+ substantive | Trigger: accelerate Domain 50–51 (add pre-send to Lambda Legal/AT4E before July 1) |
| Moderate (10–20% open rate equivalent) | 1–2 replies from 9 contacts | Proceed with Domain 51 June 11–12 as scheduled; hold Domain 48 until June 20 |
| Weak (<10% open rate equivalent) | 0 replies, <5 Gist views | Apply DOMAIN_49_CONTINGENCY_DECISION_TREE.md Scenario A (delivery failure diagnosis) |

**Trigger to accelerate Domain 50–51 (>20% open rate signal)**

If Domain 49 Day 7 shows 3+ replies with substantive engagement (at least one reply that references the Callais cascade or requests supplemental materials):
1. Move Domain 50 Gist creation from July 1 to June 20
2. Send Domain 50 pre-distribution note to Lambda Legal and AT4E on June 22 (not the full distribution — a preview note with Gist link and framing of August 1 deadline relevance)
3. Add GLAD and NCLR to Domain 51 June 12 send (campaign finance + trans ballot suppression connection)

**Trigger to scale back (Domain 49 <10% by Day 3)**

If by June 7 there are 0 replies and fewer than 3 Gist views:
1. Do not send Domain 49 Tier 3 contacts until delivery is confirmed
2. Check spam folders; re-send Tier 1 NAACP LDF and Democracy Docket from a different email subject line
3. Domain 51 execution continues as planned — Domain 51 has its own delivery baseline (Gist was created June 2 and is verified live)
4. Report to DISTRIBUTION_EXECUTION_LOG.md as "delivery unknown — under diagnosis"

---

## Scenario B — Approved (Normal)
**Domain 49 executes June 4–5, assessment window June 6–8, Domain 51 June 9–12. Conservative escalation.**

### When to use
User approves Domain 49 but prefers to assess Day 2–3 engagement before sending Tier 2. This is appropriate if the user has limited confidence in the contact list or wants to verify Gist delivery before expanding the send pool.

### Key differences from Scenario A

1. **Tier 2 sends defer to June 9–10** (not June 5). This gives 4 days to observe whether Tier 1 sends generated engagement before expanding.
2. **Domain 51 runs sequentially**, not overlapping with Domain 49 Tier 2 (June 9 = Domain 51 Wave 1; June 10 = Domain 49 Tier 2; June 11–12 = Domain 51 Wave 2).
3. **Option to pause Domain 51 if Domain 49 extreme engagement**: If Domain 49 produces 5+ replies by June 8 (extraordinary engagement), the user may elect to spend June 9–10 responding to Domain 49 coalition requests before executing Domain 51. Only appropriate if the Domain 49 replies are time-sensitive requests (e.g., a litigation team asking for supplemental analysis before a June 9 filing deadline).

### Day-by-Day Summary

| Day | Primary Action | User Hours |
|-----|---------------|------------|
| June 4 | Domain 49 Tier 1 sends (5 contacts) | 1.25 |
| June 5 | Domain 49 monitoring; Day 1 assessment | 0.25 |
| June 6 | Domain 49 monitoring | 0.1 |
| June 7 | Day 3 assessment; confirm Tier 2 go/no-go | 0.2 |
| June 8 | Domain 39 Day 7 checkpoint; Domain 51 Gist verify | 0.5 |
| June 9 | Domain 51 Wave 1 (CLC + Issue One) + Domain 49 Tier 2 start | 1.0 |
| June 10 | Domain 49 Tier 2 continuation (Advancement, ACLU) | 0.5 |
| June 11–12 | Domain 51 Wave 2 (CA contacts) | 1.0 |
| **June 4–12 Total** | | **4.8** |

**Conservative escalation paths**:

- If Day 7 (June 11) shows 2+ Domain 49 replies: add Tier 3 contacts (Brennan Center, state-level civil rights orgs) in June 15–20 window
- If Day 7 shows 1 Domain 49 reply: proceed on original schedule; no acceleration
- If Day 7 shows 0 Domain 49 replies: delivery diagnosis; Domain 51 continues independently

**Option to pause Domain 51 (extreme engagement threshold)**

This option triggers only if: 5+ Domain 49 replies arrive before June 9 AND at least 2 are explicit coalition coordination requests. In that case, user spends June 9 responding to coalition requests; Domain 51 Wave 1 shifts to June 10; Domain 51 Wave 2 shifts to June 13 (still within the pre-July 1 window). July 1 deadline is unaffected.

---

## Scenario C — Deferred
**Domain 49 pushed to July. Domain 51 standalone June 9–12. Domain 50 research begins June 15.**

### When to use
User decides to defer Domain 49 to July. This choice is appropriate if: (1) user has insufficient bandwidth for June 4–5 execution; (2) user wants to observe Domain 39 Day 7 signal before committing additional distribution resources; or (3) stockbot Alpaca feed decision or systems-resilience platform decision is consuming user attention on June 4.

### Critical constraint
Deferring Domain 49 to July does NOT make the redistricting cascade wait. Louisiana's congressional map is already signed. Alabama, Tennessee, and South Carolina redistricting cases will file or settle in June. Domain 49 deferred to July will miss the emergency preliminary injunction window for any June-filing litigation team. The July execution is still valuable for: voter education about the new maps, SAVE Voting Rights Act advocacy, and the primary contact organizations (NAACP LDF, Democracy Docket, CLC) who continue working the redistricting cases through the election cycle.

### Timeline

**June 4–8 (freed by Domain 49 deferral)**

This window is now available for other projects. Productive uses:
- Stockbot Alpaca feed switch to IEX (5-minute user action; 0.5 agent-hours confirmation)
- Systems-resilience Phase 5 author recruitment (0–2 agent-hours; user executes June 5 send)
- Domain 51 pre-send prep (verify Gist, fill templates — 30-minute user task June 7)
- Rest / batching of other project decisions

**June 9–12 — Domain 51 Standalone Execution**

Domain 51 executes exactly per DOMAIN_51_RESEARCH_EXECUTION_CHECKLIST.md. No changes from the base plan. All 5 contacts, 2-wave structure, 2.75 user-hours.

**June 15 — Domain 50 Research Synthesis Begins (optional)**

If Domain 39 June 8 data is moderate-to-strong (1+ replies, 3+ Gist views), begin Domain 50 research synthesis session. This is the cross-domain analysis that links Domain 50's trans ballot suppression stack to Domain 49's redistricting cascade — the combined frame that strengthens both documents' advocacy reach. Agent session: 2.0–3.0 hours.

**July Domain Sequencing Under Scenario C**

| Date | Domain | Action |
|------|--------|--------|
| July 1 | Domain 50 | Gist creation + Lambda Legal/AT4E first send |
| July 5–10 | Domain 49 | Gist creation + Tier 1 sends (redistricting ongoing) |
| July 15 | Domain 54 | Gist creation + NextGen/Campus Vote Project send |
| July 17–20 | Domain 54 | Wave 1 completes |
| July 22–25 | Domain 54 | Wave 2 (Rock the Vote, Student PIRGs) |
| July 28–30 | Domain 48 | Contact prep + Gist creation |
| August 8–12 | Domain 57 | Full execution |

**Domains 57/54 shifts under Scenario C**:
- Domain 54: no change — July 15 execution is identical across all scenarios
- Domain 57: no change — August 10 anchor is fixed
- Domain 48: no change — June 28–July 5 is now the earliest viable window (was June 10 under Scenario A)
- Domain 49: shifts from June 4–10 to July 5–12 (loses emergency injunction window; retains voter education and ongoing litigation advocacy value)

**Freed June 4–8 capacity unlocks**:
- stockbot Phase 2 prep: 0–4 agent-hours available if needed before June 15 checkpoint
- systems-resilience Phase 5 Wave 2: any June 4–8 author recruitment sessions that were deprioritized by Domain 49 can now proceed
- No Domain 49 distribution means no 3.5–4.0 user-hours consumed; user can focus on making stockbot and seedwarden decisions

---

## Scenario D — Research-First
**Deferred distribution; begin Domain 49–50 research synthesis June 4+; delivery June 15–20.**

### When to use
If Domain 39 Day 7 response data (June 8) shows weak engagement (0 replies, <3 Gist views), this signals either delivery failure or insufficient organizational attention. Shifting to a research-first approach produces internally-valuable coalition-building materials that are more durable than rushed cold distribution.

This scenario is also appropriate as a proactive choice (not triggered by weak engagement) if the user wants to deepen the analytical framework before distributing to major organizations.

### Core Concept
Instead of distributing existing domain documents as standalone research, produce a cross-domain synthesis that maps how Domains 49, 50, 51, 54, and 48 collectively constitute a democratic exclusion architecture — the same structural argument that Phase 1 Domains 37, 39, 56, 58, 59 make, but for the Phase 2 issues. This synthesis document becomes a coalition briefing document rather than a single-domain distribution piece.

### Timeline

**June 4–8 — Cross-Domain Research Synthesis**

Agent session scope (4.0–5.0 agent-hours across 2–3 sessions):
1. Session 1 (June 4): Map the connecting thread across Domains 49, 50, 51, 54, 48 — how do redistricting (49), trans ballot suppression (50), dark money (51), youth suppression (54), and criminal disenfranchisement (48) compose a single exclusion architecture?
2. Session 2 (June 6): Identify coalition bridging opportunities: which Phase 1 organizations (NAACP LDF, Democracy Docket, CLC) already work across multiple Phase 2 domains? Produce a coalition coordination memo.
3. Session 3 (June 8): Finalize synthesis document for distribution as a standalone analysis

**June 9–15 — Domain 51 Sends + Synthesis Completion**

Domain 51 continues on its base schedule (June 9–12). The synthesis document is completed by June 15 and shared with the highest-engagement Phase 1 organizations as a bonus document: "Here is how your work on [Domain 39 healthcare / Domain 56 civil service] connects to the redistricting and ballot suppression landscape we've been documenting."

**June 15–20 — Research Synthesis Distribution**

Synthesis document becomes the Gist for coalition-building. Send to organizations that have shown Score 2+ engagement with Phase 1: Georgetown CCF, Brennan Center, CBPP, AFGE. This is a coalition relationship-building send, not a cold distribution.

**Domain 49 individual distribution**: Proceeds June 15–20 (post-synthesis) using the synthesis as the cover framing, not as a standalone redistricting document. This is more powerful for the advocacy organizations that have seen Phase 1 content and understand the broader architecture argument.

**Trigger conditions for this scenario**:
1. Domain 39 June 8 data: 0 replies, <3 Gist views (weak engagement signal)
2. User preference for depth over speed
3. Any coalition organization explicitly requests a cross-domain framing document

**Exit from Scenario D**: If synthesis work reveals that individual domain distribution is higher-value than the synthesis approach (e.g., NAACP LDF's June redistricting work needs Domain 49 specifically, not a cross-domain brief), exit Scenario D and switch to Scenario C (deferred) with July 5–12 Domain 49 individual distribution. Synthesis document is still valuable as a secondary resource.

---

## Cross-Scenario Decision Matrix

| If user says... | Scenario | Domain 49 First Send | Domain 51 First Send | Domain 48 First Possible |
|-----------------|----------|---------------------|---------------------|--------------------------|
| "Approve — execute now" | A | June 4 | June 9 | June 12 (optional) |
| "Approve — brief assessment first" | B | June 4 (Tier 1 only) | June 9 | June 15 |
| "Defer Domain 49 to July" | C | July 5–10 | June 9 | June 28–July 5 |
| "Hold — research synthesis first" | D | June 15–20 (post-synthesis) | June 9 | July 1 |

**Domain 51, Domain 54, Domain 57**: Timing is identical across all scenarios. Domain 51 executes June 9–12. Domain 54 executes July 15–25. Domain 57 executes August 10–12.

---

*Prepared June 4, 2026. Cross-references: BATCH_2_RESOURCE_ALLOCATION_MATRIX.md, BATCH_2_JUNE_CHECKPOINT_READINESS_PROTOCOL.md, DOMAIN_49_EXECUTION_PREFLIGHT.md, DOMAIN_49_CONTINGENCY_DECISION_TREE.md, DOMAIN_51_RESEARCH_EXECUTION_CHECKLIST.md.*
