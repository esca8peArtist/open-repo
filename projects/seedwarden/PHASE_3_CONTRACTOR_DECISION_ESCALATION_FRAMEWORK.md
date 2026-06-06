---
title: "Phase 3 Contractor Decision Escalation Framework — Go/No-Go Decision Tree, Timeline Impact Analysis, and Phase 4 Cascade"
date: 2026-06-06
version: 1.1
status: production-ready
decision-deadline: June 15, 2026 EOD
hard-contractor-deadline: June 17, 2026 EOD
phase-3-start: June 22, 2026
cross-references:
  - PHASE_3_CONTRACTOR_DECISION_TREE.md (primary decision tree — detailed branching)
  - PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md (search channels, vetting rubric, rate benchmarking)
  - PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md (9-week solo timeline — companion doc)
  - PHASE_3_COMPREHENSIVE_RISK_REGISTER.md (Risk 8 — solo fallback decision cascade)
  - PHASE_3_PRODUCTION_SPRINT_RISK_REGISTER.md (Risk 1 — contractor dropout)
tags: [seedwarden, phase-3, contractor, escalation, go-no-go, decision-tree, phase-4-impact, timeline]
---

# Phase 3 Contractor Decision Escalation Framework
## Go/No-Go Decision Tree, Escalation Triggers, and Phase 3→Phase 4 Timeline Impact

**Prepared**: June 5, 2026
**Purpose**: Consolidates all contractor decision logic into a single escalation document covering June 5 through June 22. The primary decision tree in PHASE_3_CONTRACTOR_DECISION_TREE.md covers branching logic in full; this document adds the go/no-go decision tree with numeric thresholds, Phase 3→Phase 4 timeline impact analysis, and a Q4 planning cascade reference.

---

## Section 1 — Escalation Timeline Overview

The contractor decision window runs June 5–17. There are five formal decision gates, each with specific numeric thresholds that determine the next action. Every gate is deterministic — no "use your judgment" nodes.

| Gate | Date | Decision | Threshold | Action if Threshold Not Met |
|---|---|---|---|---|
| Gate 1 | June 8 | First response check | 0 replies → escalate; 1+ → score | Expand AHG outreach; activate Toptal; post secondary Upwork listing |
| Gate 2 | June 10 | Candidate quality check | 4+ qualified responses → GO; 1–3 responses with score ≥75 → proceed to interviews; 0 responses or best score <60 → escalate fallback recruitment | Expand search to NAMA, IHA, Herbal Academy general alumni; activate Toptal; post revised Upwork listing |
| Gate 3 | June 12 | Contract target | Signed → briefing package; Not signed → final escalation | 48-hour negotiation window; activate backup search simultaneously |
| Gate 4 | June 15 | Solo fallback threshold | No contract signed EOD → activate solo fallback | Log activation; stop contractor search; update Phase 4 dates |
| Gate 5 | June 17 | Hard contractor deadline | No contract → solo fallback confirmed; no contractor after this date | Solo fallback confirmed regardless of any subsequent contacts |

---

## Section 2 — Go/No-Go Decision Tree

This decision tree produces one of four outcomes: GO, HOLD, NO-GO, or ABORT. Each outcome has a specific set of conditions and a defined next action.

```
CONTRACTOR SEARCH ASSESSMENT — June 15 EOD

Step 1: Contractor response count
  |
  +-- 2 or more qualified responses by June 13?
          |
          YES → GO (contractor found)
          NO  → Continue to Step 2
  |
Step 2: Response count and rate assessment
  |
  +-- 1 response by June 12, rate within budget ($1,000-$1,350)?
          |
          YES → GO (contractor found, contract target June 12)
          NO  → Continue to Step 3
  |
Step 3: Over-budget single response
  |
  +-- 1 response by June 12, rate $1,351-$1,500?
          |
          YES → HOLD (negotiating; Over-Budget Protocol active)
                Negotiate: fourth-bundle framing at $1,350 + Sleep bundle right-of-first-offer
                If negotiation closes by June 14: GO
                If negotiation fails by June 14: NO-GO
          NO  → Continue to Step 4
  |
Step 4: Over-ceiling single response
  |
  +-- 1 response by June 12, rate $1,501+?
          |
          YES → ESCALATION DECISION (see Section 3 — Over-Ceiling Response)
                Option A: Attempt reduced scope (Respiratory + Digestive, $700-$800)
                Option B: Decline and activate NO-GO
          NO  → Continue to Step 5
  |
Step 5: No responses or only unqualified responses
  |
  +-- 0 qualified candidates by June 12 (no one passed screening questions)?
          |
          YES → NO-GO: activate solo fallback
                Early activation June 12 recommended over waiting for June 15
                Rationale: 3 additional sprint preparation days > marginal search probability
          NO  → Continue to Step 6
  |
Step 6: Scope confidence check
  |
  +-- Qualified candidate found, but scope confidence is low?
          (Unable to confirm: contractor understands FTC requirements, CITES sidebar,
           Ashwagandha thyroid mechanism, Goldenseal cultivation framing)
          |
          YES → ABORT: activate solo fallback
                Do not hire a contractor who cannot pass the scope confidence check
                Solo fallback is safer than a contractor who cannot write FTC-compliant
                contraindication content at the required standard
          NO  → GO or HOLD per above conditions
```

### Decision Outcome Definitions

**GO**: Contract signed (or on track to sign by June 15 EOD). At least 1 contractor confirmed with vetting score ≥75, rate within budget, June 22 availability confirmed in writing. Sprint proceeds with contractor-assisted model.

**HOLD**: 1–2 responses, active negotiation on rate or scope. Contract not yet signed. HOLD activates simultaneous backup search — do not stop outreach while negotiating. HOLD converts to GO (contract signed by June 15) or NO-GO (negotiation fails) by June 15 EOD. A HOLD that has not resolved by June 15 EOD converts to NO-GO automatically.

**NO-GO**: Activate solo fallback immediately. 0 qualified candidates, or negotiation failed, or only over-ceiling candidates with no scope reduction option. Solo fallback activates per PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md. Log: "NO-GO activated [date]. Solo fallback per PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md."

**ABORT**: Activate solo fallback immediately. A candidate is technically available but scope confidence is insufficient (fails FTC test, cannot explain CITES sidebar, paraphrases contraindication register rather than citing sources). Hiring an unqualified contractor at this stage creates more risk than the solo model. ABORT is a stronger signal than NO-GO: log the scope confidence failure and the disqualifying criterion in the contractor tracking log.

---

## Section 3 — Numeric Escalation Triggers

These are the specific numeric thresholds that fire escalation actions, independent of the go/no-go outcome.

### Escalation Trigger 1: Zero Responses by June 10

**Condition**: 0 substantive replies (screening questions answered or interview requested) from any channel by June 10 EOD (Day 5 of search).

**Action**: Activate backup recruitment simultaneously across all remaining channels:
1. Expand AHG directory outreach from initial 15 contacts to all RH members listing education or writing (estimated 30–50 members). Send by June 10 evening.
2. Contact Toptal client intake (toptal.com/hire) if not already activated. Specify "medical herbalist writer, clinical contraindication experience." Toptal match turnaround: 48–72 hours. If activated June 10, match arrives June 12–13 — within the June 15 threshold.
3. Post revised Upwork listing with updated framing (more specific bundle descriptions, explicit CITES question in job post).
4. Email Herbal Academy partnerships@theherbalacademy.com: "Request for referral to Advanced + Clinical program instructors with educational writing availability June 22 – August 1."

**Log entry**: "June 10 — Escalation Trigger 1 activated: 0 responses. Expanding AHG to 30–50 contacts; activating Toptal; revised Upwork listing; Herbal Academy referral request."

---

### Gate 2 June 10 — Four-Tier Response Assessment

Gate 2 (June 10, Day 5 of search) is the first hard quality checkpoint. It produces a deterministic outcome in all four response-count scenarios. Unlike Escalation Trigger 1 (which fires only on 0 responses), Gate 2 applies regardless of response count and governs the next 5 days of the search.

**Tier 1 — 4 or more qualified responses by June 10**: GO signal. The candidate pool is sufficient for competitive selection. Score all respondents on the vetting rubric immediately. Schedule interviews with candidates scoring ≥75. Do not wait for additional responses — pipeline risk is resolved. Target: contract signed June 12–14.

**Tier 2 — 1 to 3 responses, best score ≥75**: Proceed to interviews. This is not yet a GO signal because only one vetted candidate is in hand, but the quality threshold is met. Schedule interview within 24 hours of scoring. Make offer if interview passes all 6 mandatory questions. Simultaneously: maintain outreach to remaining channels — if the Tier 1 interview falls through, a second candidate should be in the pipeline.

**Tier 3 — 1 to 3 responses, best score 60–74**: Proceed to conditional interview. The candidate has cleared basic qualification but is below the preferred threshold. Interview using the 45-minute checklist with special attention to Q2 (contraindication rigor) and Q5 (FTC compliance example). If the interview raises the effective score to ≥75 (weighted by Q2 and Q5 performance): make offer. If not: decline and activate Escalation Trigger 1 actions simultaneously.

**Tier 4 — 0 responses or best score below 60**: Escalate fallback recruitment immediately. This is the same action as Escalation Trigger 1. Log: "June 10 — Gate 2 Tier 4: [X] responses, best score [Y]. Escalating fallback recruitment: expanded AHG, Toptal, revised Upwork, Herbal Academy referral." Solo fallback trajectory is now confirmed unless Toptal or expanded AHG produces a Tier 1–2 candidate by June 13.

**Log entry format**:
```
GATE 2 ASSESSMENT — June 10 EOD
Responses received: [X]
Best vetting score: [Y]
Tier: [1 / 2 / 3 / 4]
Decision: [GO / Proceed to interview / Conditional interview / Escalate fallback]
Next gate: [date]
```

---

### Escalation Trigger 2: One Response, Rate Above $1,500

**Condition**: Exactly 1 substantive response received by June 12, and the quoted rate is $1,501 or above.

**Decision required**: This is an escalation decision, not an automatic action. Two options:

**Option A — Over-Budget Protocol**: Attempt negotiation with the fourth-bundle framing:
- Script: "Our budget for the three-bundle scope is $1,000–$1,350. We are planning a fourth bundle — Sleep and Nervines — in early August at the same rate. Would you take the three-bundle contract at $1,350 with first right of offer on the fourth bundle at your standard rate?"
- If accepted by June 14: GO at $1,350. Contract signed.
- If rate remains $1,501–$2,000 after negotiation attempt: try reduced scope offer (Respiratory + Digestive at $700–$800; user writes Immunity).
- If reduced scope is also rejected: NO-GO. Decline and activate solo fallback.

**Option B — Direct NO-GO**: If the candidate's quote is $2,001 or above, or if time pressure at June 12 makes a negotiation cycle infeasible (i.e., a June 14 resolution is unlikely given communication pace): decline immediately and activate NO-GO. A solo fallback with 10 days of sprint preparation is better than a rushed negotiation closing June 15 with 7 days of onboarding.

**Simultaneous action regardless of option chosen**: Expand outreach to NAMA, IHA, and Herbal Academy general alumni during the negotiation window. Do not stop searching while negotiating with the sole respondent.

**Log entry**: "June 12 — Escalation Trigger 2 activated: 1 response, rate $[X]. Activating [Option A / Option B]. Simultaneous expanded outreach: NAMA, IHA, Herbal Academy alumni."

---

### Escalation Trigger 3: Two or More Responses by June 13

**Condition**: 2 or more substantive responses received by June 13, at least one with a rate within budget.

**Action**: This is a GO signal. No escalation needed. Score all respondents on the vetting rubric. Schedule interviews for any candidate scoring ≥75. Target: contract signed by June 14–15. Offer to the highest-scoring candidate within budget.

**If 2+ responses but all above ceiling ($1,500+)**: Both candidates receive the Over-Budget Protocol negotiation. Negotiate in parallel. If one accepts by June 14: GO at negotiated rate. If neither accepts: NO-GO.

**Log entry**: "June 13 — Escalation Trigger 3: [X] qualified responses. Vetting rubric scoring in progress. Contract target June 14–15."

---

## Section 4 — Phase 3 → Phase 4 Timeline Impact Analysis

The contractor decision has a direct cascade effect on Phase 4 start date and all downstream milestones. This section quantifies the impact for Q4 2026 planning.

### Timeline Comparison: Contractor Model vs. Solo Fallback

| Milestone | Contractor Model | Solo Fallback | Delta |
|---|---|---|---|
| Phase 3 Women's Health live | June 29 | June 29 | 0 days |
| Phase 3 Respiratory live | July 6 | July 13 | +7 days |
| Phase 3 Sleep live | July 13 | August 3 | +21 days |
| Phase 3 Immunity live | July 20 | August 17 | +28 days |
| Phase 3 Digestive live | August 3 | September 24 | +52 days |
| Phase 3 sprint close | August 3 | September 24 | +52 days |
| Phase 4 start | July 14 (concurrent) | October 1 | +79 days (~2.5 months) |
| Phase 4 Wave 1 launch | August 1 | November 1 | +92 days (~3 months) |
| Phase 4 Wave 2 launch | August 31 | December 1 | +92 days |
| Phase 5 start (API/SDK) | November 1 | February 1, 2027 | +92 days |

### Revenue Impact Quantification

**Phase 3 delayed bundles** (Respiratory, Sleep, Immunity, Digestive — solo model delays only):
- Respiratory: 7-day delay × 3–8 views/day × 3–5% conversion × $20 = approximately $13–$56 in delayed first-week revenue
- Sleep: 21-day delay × same rate = approximately $38–$168 in delayed revenue
- Immunity: 28-day delay × same rate = approximately $50–$224 in delayed revenue
- Digestive: 52-day delay × same rate = approximately $94–$416 in delayed revenue
- **Phase 3 total delay revenue impact**: approximately $195–$864 in delayed first-month revenue across the four non-Women's Health bundles

**Phase 4 delayed launch** (botanical identification guides — 18 species, $8–$12 per guide):
- Wave 1 (9 guides): 92-day delay × 40 units/week × $10 = approximately $5,257 in foregone revenue across the delay window
- Wave 2 (9 guides): 92-day delay × same rate = approximately $5,257
- **Phase 4 total delay revenue impact**: approximately $10,514 in foregone revenue across August–October 2026

**Total financial impact of solo fallback vs. contractor model**: approximately $10,700–$11,400 in foregone or delayed revenue across the full Phase 3 → Phase 4 cascade.

**Context**: This is the cost of not finding a qualified contractor within the 12-day search window. Against a contractor budget ceiling of $1,500, the solo fallback costs approximately 7× the contractor investment in delayed revenue. The contractor search is worth the 12-day effort at this ratio.

**Note on "foregone" vs. "lost"**: This revenue is not destroyed — it is delayed. Phase 4 guides will generate the same revenue starting November 1 under the solo model. The financial impact is the time value of money and the competitive cost of delayed market presence. For Q4 2026 cash flow planning, the November 1 Phase 4 revenue start should replace the August 1 assumption.

---

## Section 5 — Q4 Planning Cascade Reference

If solo fallback is activated, update these planning assumptions immediately:

### Phase 4 Planning Adjustments (Solo Fallback Active)

**Phase 4 botanical identification guides**:
- Start date: October 1, 2026 (was July 14)
- Wave 1 launch target: November 1, 2026 (was August 1)
- Wave 2 launch target: December 1, 2026 (was August 31)
- AHG Symposium campaign: August 14–16 campaign proceeds with Phase 3 bundles (Women's Health is live June 29 in both models). Phase 4 guides are not ready for AHG Symposium in the solo model — Phase 3 bundles are the sole AHG campaign product.

**Phase 5 planning adjustments**:
- API/SDK expansion start: February 1, 2027 (was November 1, 2026)
- Multi-format packaging: February–April 2027 window (was November 2026 – January 2027)
- ZIM archive submission: March 2027 (was December 2026)

**Practitioner tier activation**:
- 3-bundle minimum for $120–$150 clinical library pricing: met when Respiratory uploads (July 13 solo vs. July 6 contractor)
- 5-bundle full practitioner library: met when Digestive uploads (September 24 solo vs. August 3 contractor)
- AHG Symposium August 14–16 marketing can reference 2 live bundles (solo) vs. 4 live bundles (contractor) — the solo model's practitioner tier campaign at AHG Symposium is materially weaker

### Phase 4 Planning Adjustments (Contractor Model Active)

**Phase 4 botanical identification guides**:
- Start date: July 14, 2026 (day after Phase 3 sprint close)
- Wave 1 launch target: August 1, 2026
- Wave 2 launch target: August 31, 2026
- AHG Symposium campaign August 14–16: Phase 3 full catalog (4 bundles) live; Phase 4 Wave 1 guides (9 species) launching concurrently. Full dual-product campaign possible.

**Phase 5 planning**:
- API/SDK expansion: November 1, 2026
- No adjustments needed from original planning.

---

## Section 6 — Decision Log Template

Use this template to log each gate decision in WORKLOG.md from June 5 through June 17.

```
CONTRACTOR DECISION LOG — [Date]
Gate: [Gate 1 / 2 / 3 / 4 / 5]
Condition assessed: [brief description]
Threshold: [numeric threshold]
Actual status: [actual count/status]
Decision: [GO / HOLD / NO-GO / ABORT / Escalate]
Action taken: [specific action]
Next gate: [date and condition]
Phase 4 date adjustment: [updated if model shifts] OR [No change]
```

**Example — GO outcome June 12**:
```
CONTRACTOR DECISION LOG — June 12
Gate: Gate 3 (Contract target)
Condition assessed: Contract signed and deposit paid?
Threshold: Signed → briefing package
Actual status: Contract signed June 12. Deposit paid $300.
Decision: GO
Action taken: Briefing package delivered June 13. Sprint Day 1 briefing call scheduled June 22 9am ET.
Next gate: June 17 (confirmation check — no action required; contractor confirmed)
Phase 4 date adjustment: No change — contractor model active. Phase 4 July 14 start preserved.
```

**Example — NO-GO outcome June 15**:
```
CONTRACTOR DECISION LOG — June 15 EOD
Gate: Gate 4 (Solo fallback threshold)
Condition assessed: Is a contract signed by June 15 EOD?
Threshold: No contract signed → activate solo fallback
Actual status: 0 contracts signed. 1 candidate in negotiation but over ceiling ($1,600; negotiation failed June 14).
Decision: NO-GO
Action taken: Solo fallback activated. Log: "June 15 EOD — Solo fallback activated. 5-bundle solo sprint June 22 – September 24 at 12 hrs/week. Per PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md."
Contractor search stopped.
Next gate: N/A (solo fallback confirmed June 17 if no contract by then)
Phase 4 date adjustment: Phase 4 start October 1 (was July 14). Wave 1 November 1 (was August 1). Phase 5 February 1, 2027 (was November 1, 2026).
```

---

## Section 7 — Escalation Framework Quick Reference

**June 8**: 0 replies → fire Escalation Trigger 1 (expand AHG, activate Toptal, revised Upwork, Herbal Academy referral).

**June 10**: 0 qualified candidates → log "solo fallback trajectory confirmed"; begin mental shift to solo planning NOW; consider early activation June 12.

**June 12**: No contract signed AND no Tier A candidate → log "solo fallback trajectory confirmed; activating June 15."

**June 12**: 1 response, rate $1,351–$1,500 → Escalation Trigger 2, Option A (Over-Budget Protocol). Give 48-hour negotiation window. Resolution by June 14.

**June 12**: 1 response, rate $1,501+ → Escalation Trigger 2, Option B (direct NO-GO or reduced scope offer).

**June 13**: 2+ qualified responses → Escalation Trigger 3 (GO signal). Score, interview, offer.

**June 15 EOD**: No contract signed → NO-GO. Solo fallback activated. Log. Stop contractor search.

**June 17 EOD**: No contract regardless of any contacts → solo fallback confirmed. No contractor after June 17.

---

## Section 8 — FAQ

**Q: A Tier A candidate (score 82) responds June 14 but cannot confirm June 22 availability — they can start June 29. Does this change the decision?**

No. A contractor who cannot begin June 22 does not cover the Women's Health bundle. Women's Health is user-written in all scenarios — this has always been the plan. A June 29 contractor start would cover Respiratory (due July 1), Immunity (due July 8), and Digestive (due July 20). If the candidate's score is ≥75, they pass all disqualifying conditions, and their rate is within budget: this is still a valid engagement. Re-evaluate using the decision tree with a June 29 contractor start. The contractor writes Respiratory, Immunity, and Digestive; user writes Women's Health and Sleep. Sprint structure is adjusted, not abandoned.

**Q: It is June 16. We have 1 Tier A candidate who passed screening but is waiting for a portfolio sample to arrive. Do we wait for the sample before signing?**

No. Request the sample immediately (same-day email: "Please send the sample today — we need to confirm by June 17 EOD"). If the sample arrives June 16 and passes the contraindication depth review: sign same day. If the sample does not arrive by June 17 EOD: do not sign. Waiting for a sample that has not arrived 12 days into the search window is a predictor of communication patterns during the sprint.

**Q: We are in NO-GO (solo fallback activated June 15) and a strongly credentialed candidate contacts us June 16 unsolicited. Do we engage?**

Yes, one go/no-go call only. Score the candidate on the vetting rubric from the information in their initial message. If score is likely ≥75, rate is within budget, and June 22 availability is confirmed in the message: contact them immediately and request a screening question answer and a 30-minute call. If the call closes a contract by June 17 EOD: convert from NO-GO to GO. Update the WORKLOG.md log. Update Phase 4 dates back to contractor model dates. After June 17 EOD: no contractors, no exceptions.

**Q: The Phase 4 3-month delay is significant. Should we consider hiring a lower-quality contractor (Tier B, score 62) to avoid it?**

No. A Tier B contractor who fails the FTC test or cannot explain CITES Appendix II creates a different risk: inaccurate contraindication content in a published practitioner guide. The FTC liability and reputational cost of a contraindication error in the Immunity or Sleep bundle (Ashwagandha thyroid interaction, Passionflower MAOI) is greater than the revenue impact of a 3-month Phase 4 delay. Hire Tier B only if all disqualifying conditions pass — specifically: FTC test passes (correct evidence-tier framing, not just hedging language), CITES test passes (understands cultivation sourcing implications, not just trade restriction definition), and credential is verifiable.

---

*Prepared: June 5, 2026. Version 1.1 (June 6, 2026 — Gate 2 June 10 four-tier response assessment added to Section 3; escalation timeline table updated with explicit 4+/1–3/score thresholds at Gate 2). Companion documents: PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md (9-week solo timeline, Phase 4 impact), PHASE_3_COMPREHENSIVE_RISK_REGISTER.md (13-risk register including solo-fallback risks 9–13). Cross-references: PHASE_3_CONTRACTOR_DECISION_TREE.md (primary decision tree with full branching logic), PHASE_3_CONTRACTOR_SOURCING_STRATEGY.md (search channels, vetting rubric, outreach templates).*
