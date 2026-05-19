---
title: "Phase 2 Post-Synthesis Analysis Framework"
item: "Exploration Queue Item 86"
created: 2026-05-19
execute_after: "May 21, 2026, 20:00 UTC (CHECKIN.md synthesis post)"
status: PRODUCTION-READY — deterministic; read immediately post-synthesis
word_count: ~2,800
authority: MAY_21_SYNTHESIS_EXECUTION_FRAMEWORK.md (classification rules); phase-2-research-activation-checklist.md (domain readiness); post-wave-1-monitoring/phase-2-path-activation-summary.md (path lookup)
companion_files:
  - POST_SYNTHESIS_ANALYSIS_FRAMEWORK.md (operational tracker — metrics tables, reporting milestones)
  - MAY_21_SYNTHESIS_EXECUTION_FRAMEWORK.md (classification rules — authoritative)
  - post-wave-1-monitoring/phase-2-path-activation-summary.md (one-page path lookup)
  - phase-2-research-activation-checklist.md (domain readiness audit, Session 1346)
  - DOMAINS_57_59_PRODUCTION_ROADMAP.md (Domain 57 and 59 production timelines)
  - WEAK_OUTCOME_CONTINGENCY_PLAN.md (WEAK root cause diagnosis — five corrective options)
scope: "Phase 2 research activation lens. Given a synthesis outcome, tells you: what it means, what happens next, which domains activate, in what order, what actions are required, and what risks apply."
audience: user (thorn) + future orchestrator sessions reading CHECKIN.md post-synthesis
---

# Phase 2 Post-Synthesis Analysis Framework

*Resistance Research — May 19, 2026*

**How to use this document.** After the May 21 synthesis CHECKIN.md post appears (target: 20:00 UTC), read Section 1 to confirm your classification, then jump directly to the matching pathway section (2, 3, or 4). Section 5 gives the Phase 2 activation checklist for all four domains — read it regardless of path. Section 6 gives early warning signs to watch between May 21 and May 28.

Read time: 20 minutes. No judgment calls required beyond applying signal data to the deterministic rules below.

---

## Section 1: Synthesis Outcome Classification

### 1.1 What the Synthesis Reads

The May 21 synthesis (autonomous execution, 19:00–20:00 UTC) reads three inputs from `post-wave-1-monitoring/wave-1-signal-log-may18-21.md`:

| Input | What it measures | Where to find it |
|-------|-----------------|-----------------|
| Total Quality Reply Points (QRP) | Weighted sum of engagement quality from all Score 3+ replies plus Gist bonus | Signal log — May 21 snapshot section |
| Substantive response rate | (Score 3+ count / effective send count) × 100 | Signal log — May 21 snapshot section |
| Gist delta | Net view count increase across all four Gist URLs since May 18 ~08:00 UTC | Signal log — May 21 snapshot section |

**QRP formula**: Total QRP = (sum of quality points from Score 3+ replies) + min(Gist delta / 5, 1.0)

**Score-to-quality-point conversion**: Score 0–2 = 0 points. Score 3 = 1 point. Score 4 = 2 points. Score 5 = STRONG OVERRIDE — stop all scoring, classify STRONG immediately.

---

### 1.2 Classification Thresholds

Apply in order. Stop at first match.

| Priority | Classification | Conditions — ALL must be met | Phase 2 implication |
|----------|---------------|------------------------------|---------------------|
| 1 | STRONG — Score 5 override | Any contact cites framework in published filing, brief, testimony, or offers formal institutional collaboration | Phase 2 acceleration — D57+D59 parallel June 15 launch |
| 2 | STRONG — QRP | QRP >= 2 AND substantive response rate >= 40% (2+ contacts at Score 3+) | Phase 2 acceleration — same as above |
| 3 | MODERATE — QRP-driven | QRP >= 1 (one Score 3+ reply) but below STRONG threshold | Standard Phase 2 timeline — D57 June 10 primary |
| 4 | MODERATE — Gist-proxy | QRP < 1 AND Gist delta > 10 with zero email replies | Standard Phase 2 timeline — internal sharing occurring |
| 5 | WEAK | QRP = 0 AND Gist delta <= 5 AND delivery self-test confirms inbox delivery | Phase 1 remediation required before Phase 2 expansion |
| 6 | TOO EARLY | Zero replies AND zero Gist delta AND no bounces AND law school window open (before May 25) | Hold — resolves at May 25 final gate |
| 7 | DELIVERY PROBLEM | Zero signals AND delivery self-test lands in spam | Fix sender reputation — do not revise content |

**WEAK requires prior delivery check.** Do not classify as WEAK without running the delivery self-test. A delivery problem is a technical failure, not a content failure — the remediation is different.

**TOO EARLY resolves at May 25.** It cannot persist past May 25 regardless of academic response norms. At the May 25 gate, re-run the full formula with 7-day data and force a resolution to STRONG, MODERATE, or WEAK.

**Hard bounce adjustment.** For each hard bounce, subtract 1 from the effective send count denominator. The 40% response rate threshold with 4 effective contacts = 1.6 Score 3+ replies — round up to 2 required.

---

### 1.3 What the Synthesis Outcome Does NOT Mean

Understanding what a classification does not mean is as important as what it does.

- **MODERATE does not mean failure.** At 72 hours, one substantive reply from a single practitioner in the election law, think tank, or policy org sector is a meaningful early signal. The law school window (Goodman, Chenoweth) has not closed. Elias has a 7-day sector norm. A MODERATE outcome at 72h can upgrade to STRONG at the May 25 gate.
- **WEAK does not cancel Phase 2.** Phase 2 research production continues on all paths. What changes is the distribution timeline and which domains are prioritized. Domain 39 June 1 and Domain 56 May 28 proceed on all paths without exception.
- **TOO EARLY is not a content diagnosis.** It is a timing classification. A zero-reply result at 72 hours for a cohort that includes two academics (5–10 day response cycle) and a litigator (7-day sector norm) is structurally expected. Do not begin remediation from TOO EARLY.
- **STRONG requires user gate before pre-production.** The STRONG outcome activates Phase 2 acceleration, but D57+D59 pre-production research does NOT begin until explicit user confirmation at the May 25 gate. Silence at the May 25 gate is not confirmation.

---

## Section 2: STRONG Outcome Pathway

### 2.1 What STRONG Means for Phase 2

At least one practitioner has validated the framework for operational use (citation, collaboration offer, or high-engagement reply from multiple practitioners simultaneously). Social proof is available for Tier 2 outreach. The Phase 2 research timeline compresses from the standard sequence to the accelerated parallel launch.

The STRONG path does not mean everything accelerates — it means D57 and D59 launch simultaneously on June 15 rather than sequentially. Domain 56 (already complete), Domain 58 (production-completing), and Domain 39 (June 1) do not change.

### 2.2 Immediate User Actions

These items require user judgment or action. The orchestrator cannot execute them autonomously.

1. **Read the synthesis CHECKIN.md post** — confirm which contact triggered the STRONG classification, what they said or did, and whether there is an immediate follow-up required (Score 5 override = respond within 24 hours; Score 4 referral = queue materials within 48 hours).

2. **May 25 gate — mandatory decision required.** Confirm that D57 + D59 parallel pre-production should proceed. This commits 90–110 hours of Phase 2 research capacity. Silence is not confirmation. If you see the synthesis CHECKIN.md before May 25, you can confirm early — the gate is a deadline, not a release date.

3. **Review the Tier 2 pre-contact list** before the June 15–21 activation window. The list covers four constituencies: immigration legal aid, law schools (Tier 2), unions, and think tanks. Confirm any contacts you want to add or remove.

4. **If Score 5 override triggered:** Respond to the contact within 24 hours. Offer additional research support, correct citation information, or express readiness to coordinate on Phase 2 domain work relevant to their use case. Do not delay this — a citation-level signal is a live collaboration opportunity.

5. **Confirm Domain 42 DEA participation notice send** before May 28 (hard deadline). This is path-independent.

### 2.3 Phase 2 Domain Activation Sequence (STRONG)

| Date | Domain | Action | Status entering this date |
|------|--------|--------|--------------------------|
| May 21 | Post CHECKIN.md | STRONG classification posted | Synthesis executed |
| May 24 | Domain 42 | Electronic filing deadline — 11:59 p.m. ET | Path-independent |
| May 25 | May 25 gate | User confirms D57+D59 pre-production. If confirmed: D57 source confirmation and D59 Section 1–3 research begins May 26. | Required — do not skip |
| May 25–28 | Domain 57 | Source confirmation pass — confirm 21 source URLs live, Ikenberry library access secured | No new writing yet |
| May 28 | Domain 56 | Distribution — already complete, Gist creation if not yet done | Path-independent |
| May 28 | Domain 42 | DEA participation notice hard deadline | Path-independent |
| June 1 | Domain 39 | Pre-distribution — NON-NEGOTIABLE on all paths | Path-independent |
| June 8 | Domain 57 | Section 2 (constitutional asymmetry) outline drafted | Pre-production milestone |
| June 15 | Domain 57 | Research LAUNCH — parallel with Domain 59 | Accelerated from July 1 standard |
| June 15 | Domain 58 | Distribution — production pass complete | Hard timing (Trump v. Barbara imminent) |
| June 15 | Domain 59 | Research LAUNCH — parallel with Domain 57 | Accelerated from June 16 standard |
| June 15–21 | Tier 2 | Pre-contact activation — all four constituencies | User-confirmed list |
| June 30 | Domain 59 | Section 5 (OBBBA compounding) pre-outline complete | Production milestone |
| August 10 | Domain 57 | Distribution deadline — UNGA 81 six-week lead time | Hard deadline |
| September 1 | Domain 59 | Distribution target — pre-OBBBA Medicaid work requirements | Hard target |

### 2.4 Social Proof Language for Tier 2 (STRONG)

"Initial distribution has produced substantive engagement from [constituency description — e.g., election law practitioners, civil liberties policy organizations]. We are expanding distribution to [Tier 2 constituency] because [constituency-specific hook]."

Do not name specific Batch 1 contacts without their explicit consent. Use organization-level social proof only.

---

## Section 3: MODERATE Outcome Pathway

### 3.1 What MODERATE Means for Phase 2

The framework is landing with at least one practitioner, or internal sharing beyond the five direct recipients is occurring (Gist-proxy). Phase 2 proceeds on the standard timeline — no compression, no deferral. The MODERATE path has one meaningful contingency: if law school contacts (Goodman, Chenoweth) or Elias reply at Score 3+ between May 21 and May 25, the QRP total may clear the STRONG threshold. The May 25 gate is therefore a potential upgrade gate, not just a confirmation gate.

### 3.2 Two MODERATE Sub-Types and Their Differences

The distinction matters for Tier 2 outreach framing.

**MODERATE-Reply:** QRP >= 1 driven by at least one Score 3+ email reply. At least one practitioner found the research worth substantive engagement. Social proof framing is available for Tier 2 emails.

**MODERATE-Gist:** QRP < 1 from email replies, but Gist delta > 10. Internal sharing is occurring — someone opened the link and passed it along — but email-to-reply conversion has not yet fired. This is a positive signal but a different quality of signal. Do NOT use social proof framing in Tier 2 emails if the only Gist-proxy signal came with zero email replies. Lead with policy window urgency and domain utility instead.

### 3.3 Immediate User Actions

1. **Read the synthesis CHECKIN.md post** — confirm whether MODERATE is reply-driven or Gist-proxy-driven. This determines Tier 2 framing.
2. **May 25 gate — confirmation required.** Confirm Domain 57 June 10 research launch. If any new Score 3+ signals have arrived since May 21, rerun the QRP formula — if QRP now clears STRONG threshold, upgrade and apply the STRONG pathway.
3. **Confirm Domain 42 DEA send** before May 28 (path-independent).

### 3.4 Phase 2 Domain Activation Sequence (MODERATE)

| Date | Domain | Action | Notes |
|------|--------|--------|-------|
| May 21 | Post CHECKIN.md | MODERATE classification posted | Continue monitoring May 22–24 |
| May 23 | Weiser/Bassin 5-day window | If either replies at Score 3+, recalculate QRP. Think tank constituency STRONG upgrades overall. | Potential upgrade point |
| May 24 | Domain 42 | Electronic filing deadline — 11:59 p.m. ET | Path-independent |
| May 25 | Final gate | Run full QRP with 7-day data. Confirm MODERATE or upgrade to STRONG. Approve D57 June 10 launch. | Required gate |
| May 25–28 | Domain 57 | Pre-production prep — source confirmation, outline structure | No new writing yet |
| May 28 | Domain 56 | Distribution — path-independent | Gist creation if not done |
| May 28 | Domain 42 | Hard deadline | Path-independent |
| June 1 | Domain 39 | Pre-distribution — NON-NEGOTIABLE | Path-independent |
| June 10 | Domain 57 | PRIMARY research launch — single domain, not parallel | One week earlier than WEAK path; later than STRONG |
| June 15 | Domain 58 | Distribution | Hard timing |
| June 22–28 | Tier 2 | Pre-contact activation — lead with policy urgency | Social proof only if Score 3+ reply exists |
| July 1 | Domain 59 | SECONDARY research launch | Compressed: no peer review buffer before Aug 1 target |
| August 10 | Domain 57 | Distribution deadline | Hard |
| September 1 | Domain 59 | Distribution target | Hard |

### 3.5 MODERATE-to-STRONG Upgrade Rule

At any point between May 21 and May 28, if a new signal arrives that pushes QRP to >= 2 with response rate >= 40%, upgrade classification in CHECKIN.md immediately. Use this post format: "Classification upgraded to STRONG — [contact], [org], Score [X]. [One sentence description]. STRONG path activates. D57+D59 parallel launch June 15 pending user confirmation at May 25 gate."

---

## Section 4: WEAK Outcome Pathway

### 4.1 What WEAK Means for Phase 2

No engagement signal confirmed after a successful delivery. Phase 2 research production continues, but the distribution expansion strategy requires diagnosis before Tier 2 outreach proceeds. Three possible root causes require different interventions:

- **Delivery problem** — emails reached spam folders. Fix sender reputation before any content revision. Do not diagnose content when the problem is technical.
- **Messaging/framing problem** — emails reached inboxes but did not compel engagement. Content revision warranted after delivery is ruled out.
- **Contact selection problem** — Batch 1 contacts are valid but not optimally positioned for the current policy moment. Batch 2/3 list revision or Reserve list activation is the intervention.

Full root cause diagnosis framework: `WEAK_OUTCOME_CONTINGENCY_PLAN.md` (Mode 1–4 diagnostic, Options A–E corrective actions).

### 4.2 Mandatory Pre-Classification Step

Before WEAK classification is posted, the delivery self-test must be run. Send an email from the same sending account to your own address. If it lands in spam: classify as DELIVERY PROBLEM, not WEAK. The corrective action is sender reputation repair, not content revision. Do not post WEAK to CHECKIN.md without this test being confirmed.

### 4.3 Immediate User Actions

1. **Read the synthesis CHECKIN.md post** — confirm the delivery self-test was run and inbox delivery was confirmed. If the test was not run, do not make any content decisions until it is.
2. **Required user decision — cannot be made autonomously:** Determine the root cause: delivery, messaging, or contact selection. The orchestrator can confirm delivery via self-test but cannot judge whether the problem is framing or contact quality — that requires user knowledge of what the outreach is intended to accomplish and which relationships exist. Flag in CHECKIN.md under "Needs Your Input."
3. **Do not revise content before diagnosing root cause.** Rewriting the email when the problem is delivery wastes effort and creates a false impression that the content needed changing.
4. **Late-arriving signals:** Any Score 3+ reply arriving between May 21 and May 25 upgrades the classification to MODERATE at the May 25 gate, regardless of the 72h WEAK designation. WEAK is provisional until May 25.

### 4.4 Retry Conditions and Timeline for WEAK

| Condition | Timeline | Action |
|-----------|----------|--------|
| Delivery problem confirmed (spam) | Immediate | Repair sender reputation. Re-send to same contacts once delivery confirmed. Do not revise content. |
| Messaging problem confirmed | May 22–24 | Revise subject line and opening paragraph only. Do not restructure the research. Test with Batch 2 (May 28–30). |
| Contact selection problem | May 22 | Activate Reserve list or accelerate Batch 2 contacts with different institutional profiles. |
| No root cause identified | May 22–25 | Option D (WEAK_OUTCOME_CONTINGENCY_PLAN.md): 3–5 post-Wave-1 contact interviews to surface feedback. |
| Still WEAK at May 25 with delivery confirmed | May 25 | Confirm WEAK. Phase 1 remediation June 1–28. Proceed with WEAK domain sequence below. |

### 4.5 Phase 2 Domain Activation Sequence (WEAK)

Domain 56, 58, and 39 proceed on the same dates as all other paths. The divergence is in D57 and D59, which are deferred, and D38/D40, which are accelerated as higher-relevance / lower-friction alternatives.

| Date | Domain | Action | Notes |
|------|--------|--------|-------|
| May 21 | Post CHECKIN.md | WEAK classification posted (delivery confirmed) | User decision required |
| May 22 | Delivery audit | Re-verify all five email addresses against current org websites | Precedes any content decision |
| May 24 | Domain 42 | Electronic filing deadline — 11:59 p.m. ET | Path-independent |
| May 25 | Final gate | Confirm or revise WEAK with 7-day data. If Score 3+ arrives by May 25, reclassify to MODERATE. | Required |
| May 28 | Domain 56 | Distribution — path-independent | Already complete |
| May 28 | Domain 42 | Hard deadline | Path-independent |
| June 1 | Domain 39 | Pre-distribution — NON-NEGOTIABLE | Path-independent |
| June 3 | Domain 38 | AI Regulatory Capture pre-production begins | Accelerated; EU AI Act August 2 anchor |
| June 15 | Domain 58 | Distribution | Hard timing: Trump v. Barbara pre-ruling window |
| June 22 | Domain 40 | Surveillance Capitalism production begins | Part of WEAK remediation track |
| June 29–July 5 | Tier 2 | Activation — contingent on Domain 39 producing at least one positive engagement signal | Conditional, not automatic |
| June 30 | Domain 38 | Distribution target | Five weeks before EU AI Act deadline |
| July 15 | Domain 40 | Distribution target | |
| July 15 | Domain 59 | Research start — compressed timeline | September 1 hard distribution target |
| August 1 | Domain 57 | Research start | September 1 completion; UNGA 81 three-week lead time |

---

## Section 5: Phase 2 Activation Checklist — All Four Domains

This section gives the pre-production activation state for each domain at May 21 synthesis, what must happen before production begins, and the distribution deadlines that do not flex. Read this section regardless of synthesis outcome.

---

### Domain 56 — Civil Service Politicization and Nonpartisan Governance Architecture

**Pre-activation state:** Document complete and distribution-ready. `domain-56-civil-service-politicization-governance.md` is approximately 6,800 words, 47 citations, current through May 15, 2026. `DOMAIN_56_EXECUTION_CHECKLIST.md` was written for a May 20 production verification pass.

**Action required before distribution:** Confirm execution checklist completion. Run citation URL spot-check (browser-test the 47 citations — do not confirm from memory). Create Domain 56 Gist if not yet done.

**Distribution date:** May 28 — all paths. This date does not flex.

**What activates with good synthesis outcome:** Domain 56 distribution is path-independent. Its content does not change based on synthesis outcome. What changes is the social proof framing available in the outreach email. STRONG and MODERATE paths can include a line referencing Phase 1 engagement; WEAK path cannot.

---

### Domain 58 — Tribal Sovereignty as Democratic Infrastructure

**Pre-activation state:** `DOMAIN_58_VERIFICATION_REPORT.md` (May 19, 2026) confirms factual currency. The existing draft at `domains/domain-38-tribal-sovereignty-indigenous-democratic-design.md` is approximately 5,200 words, 34 citations. The execution checklist (`DOMAIN_58_EXECUTION_CHECKLIST.md`) specifies an 8–12 hour production pass to extend to 7,000–8,000 words, 40–50 citations, canonical file at `domains/domain-58-tribal-sovereignty.md`.

**Action required before distribution:** Confirm the May 20 execution pass was completed. If not: this is the highest-urgency pre-activation action in the framework. The production pass must complete before Trump v. Barbara issues (expected late June/early July 2026) — updating a draft in progress under deadline is materially harder than updating a finished document.

**Distribution date:** June 15 — all paths. This date does not flex.

**Trump v. Barbara rapid-response protocol:** When the ruling issues, `DOMAIN_58_EXECUTION_CHECKLIST.md` contains a built-in rapid-response update protocol specifying exactly which sections require updating (Section 2 citizenship threat pathway; Section 5.1 rapid-response language). The domain must be at production-ready status before the ruling drops.

---

### Domain 57 — Multilateral Withdrawal and UN System Capture/Resistance

**Pre-activation state:** Research outline complete (`DOMAIN_57_RESEARCH_OUTLINE.md`). Source library staged, 57 sources (`DOMAIN_57_SOURCE_LIBRARY.md`). Domain document not yet written. Soft blocking assumption: Ikenberry "Liberal Leviathan" (Princeton UP, 2011) — library access required before July 1 production start.

**Production start date by path:**
- STRONG: June 15 (parallel with Domain 59)
- MODERATE: June 10 (primary, sequential)
- WEAK: August 1 (deferred)
- TOO EARLY: Pending May 25 resolution

**Distribution deadline:** August 10, 2026 — hard. UNGA 81 High-Level Week begins September 22; six-week lead time required for pre-positioning with Senate Foreign Relations, Human Rights Watch, Carnegie Endowment, and Freedom House contacts.

**Pre-production actions (must complete before production start date):**
1. Secure Ikenberry library access (JSTOR, university library, or Internet Archive).
2. Confirm Focus 2030 report URL (66-organization disengagement tracking) is still live.
3. Identify specific Anne-Marie Slaughter paper on international institutions as accountability mechanisms.
4. Confirm HRW CSO condemnation of ICC sanctions (March 11, 2026) is open-access at hrw.org.

---

### Domain 59 — Economic Precarity and Democratic Exclusion

**Pre-activation state:** Research outline complete (`DOMAIN_59_RESEARCH_OUTLINE.md`). Source library staged, 48 sources (`DOMAIN_59_SOURCE_LIBRARY.md`). Domain document not yet written. Section 5 (OBBBA compounding argument) identified as the primary production bottleneck — requires a pre-writing detailed outline before main production begins.

**Production start date by path:**
- STRONG: June 15 (parallel with Domain 57)
- MODERATE: July 1 (secondary, sequential)
- WEAK: July 15
- TOO EARLY: Pending May 25 resolution

**Distribution target:** September 1, 2026. Organizations need the civic participation framing at least three months before OBBBA Medicaid work requirements take effect (December 2026). If production slips past July 20, the target slides to September 30 — still viable, but tighter.

**Pre-production actions (must complete before production start date):**
1. Verify Georgetown CCF OBBBA analysis URL at ccf.georgetown.edu — confirm it is still live.
2. Identify and bookmark specific CBPP OBBBA distributional analysis URL.
3. Locate NCSL state voting time-off law survey for Section 4 (gig economy temporal exclusion).
4. Confirm Slee/Desmond (Politics and Society 2023) access — Sage paywall; check Princeton repository for working paper version.

---

### Distribution Windows Summary — All Paths

| Domain | STRONG path | MODERATE path | WEAK path | Hard deadline |
|--------|-------------|---------------|-----------|---------------|
| Domain 56 | May 28 | May 28 | May 28 | May 28 — does not flex |
| Domain 58 | June 15 | June 15 | June 15 | June 15 (before Trump v. Barbara) |
| Domain 57 | Launch June 15; distribute Aug 10 | Launch June 10; distribute Aug 10 | Launch Aug 1; distribute Sep 1+ | Aug 10 UNGA lead time |
| Domain 59 | Launch June 15; distribute Sep 1 | Launch July 1; distribute Sep 1 | Launch July 15; distribute Sep 30 | Sep 1 hard target |
| Domain 39 | June 1 | June 1 | June 1 | June 1 — does not flex |
| Tier 2 activation | June 15–21 | June 22–28 | Conditional on D39 signal | N/A |

---

## Section 6: Risk Indicators and Human Intervention Triggers

This section surfaces the early warning signs that the synthesis is off-track, the Phase 2 sequence is under pressure, or the situation requires a decision the orchestrator cannot make autonomously. Check these between May 21 and May 28.

---

### 6.1 Synthesis Classification Risks (May 21–22)

**Risk: WEAK classified without delivery check.** Indicator: CHECKIN.md post shows WEAK classification but does not confirm the delivery self-test was run. Action: Run the self-test immediately. Post DELIVERY PROBLEM or confirm WEAK based on result. Do not begin content remediation until delivery is ruled out.

**Risk: TOO EARLY persists without upgrade path.** Indicator: May 25 gate passes without re-running the QRP formula. Action: At May 25, apply the full classification rules to all signals received through May 25. Force resolution. TOO EARLY must not persist past May 25.

**Risk: STRONG classified from Score 4 without QRP math.** Indicator: CHECKIN.md classifies STRONG based on a single positive reply without verifying the QRP formula. Action: Confirm QRP >= 2 with response rate >= 40%, or confirm Score 5 override specifically. Score 4 alone generates 2 QRP, which meets the numeric threshold — but confirm response rate separately. A single Score 4 with 1/5 contacts = 20% response rate = MODERATE, not STRONG. The threshold is QRP >= 2 AND response rate >= 40%.

---

### 6.2 Phase 2 Pre-Production Risks (May 21–June 15)

**Risk: Domain 58 production pass not completed before Trump v. Barbara.** Indicator: `domains/domain-58-tribal-sovereignty.md` does not exist or is a stub. `DOMAIN_58_EXECUTION_CHECKLIST.md` shows production pass pending. Action: This is the single highest-urgency pre-synthesis action in the framework. The production pass must complete before the ruling. Check its status at first opportunity after synthesis. If not done, queue it as the highest-priority research task regardless of synthesis outcome.

**Risk: Domain 57 Ikenberry access not secured before production start.** Indicator: July 1 or June 15 production start (MODERATE or STRONG path) approaches without Ikenberry library access confirmed. Action: Attempt university library, JSTOR, or Internet Archive access. If unavailable, Section 3 of Domain 57 must use secondary summaries of Ikenberry's thesis — weaker but viable. Flag in the production roadmap before writing begins.

**Risk: Domain 59 Section 5 bottleneck not pre-outlined.** Indicator: June 15 or July 1 production start approaches without the OBBBA compounding pre-outline complete. The DOMAINS_57_59_PRODUCTION_ROADMAP.md explicitly flags Section 5 as the primary production bottleneck. Action: Complete the Section 5 pre-outline as part of Week 1 production for Domain 59. Do not begin Section 6 or 7 without Section 5 outline confirmed.

---

### 6.3 Human Intervention Triggers (May 21–June 15)

These situations require user decision. The orchestrator cannot resolve them autonomously.

**Score 5 override signal received (any time).** A contact has cited the framework in a published filing, brief, testimony, or article — or has offered formal institutional collaboration. Required response within 24 hours. Post immediately to CHECKIN.md under "Needs Your Input — URGENT." Upgrade classification to STRONG if not already. Offer additional research support, correct citation information, or coordinate on the specific use case. Do not delay.

**Elias hard bounce.** Elias (Democracy Docket) is the highest-probability STRONG signal contact in the cohort. A hard bounce reduces the effective send count and changes the response rate math materially. Flag immediately for user re-verification. A re-send to the correct address at the same content could still produce a STRONG signal within the 7-day window. Check `BATCH_1_CONTACT_LOG.md` for the email address used and verify against current Democracy Docket website.

**WEAK with no clear root cause at May 25.** If the May 25 gate shows zero signals, delivery confirmed, and no diagnostic indicator points toward messaging vs. contact selection, the user must decide the remediation path. The orchestrator can recommend (WEAK_OUTCOME_CONTINGENCY_PLAN.md Option D — post-Wave interviews), but the user must approve the diagnostic track. Flag in CHECKIN.md: "WEAK confirmed at 7-day gate. Root cause unclear. User decision required: interview track or messaging pivot."

**Upgrade path available after May 25.** If law school contacts (Goodman, Chenoweth) reply at Score 3+ between May 25 and June 1, the classification upgrades — even from a WEAK or TOO EARLY May 21 classification. Do not ignore late-arriving signals because the "synthesis window" has closed. Log, score, recalculate QRP, and post a classification update to CHECKIN.md.

**Phase 2 domain sequence conflict.** If a new external event (SCOTUS ruling, legislative development, new NPRM comment period) opens a distribution window that conflicts with the current sequence, flag in CHECKIN.md under "Needs Your Input." Do not unilaterally move a domain's distribution date — the sequence reflects deliberate decisions about contact readiness, social proof availability, and research lead time that the user has approved.

---

### 6.4 Path-Independent Non-Negotiable Actions

These execute on all four paths without exception. No synthesis outcome changes them.

| Action | Date | What to check |
|--------|------|---------------|
| Domain 42 DEA electronic filing | May 24, 11:59 p.m. ET | `BATCH_1_CONTACT_LOG.md` Domain 42 section — confirm nprm@dea.gov send status |
| Domain 42 DEA hard deadline | May 28 | Last chance to file. No exceptions. |
| Domain 56 distribution | May 28 | Gist created and live; 47 citation URLs spot-checked |
| Domain 39 pre-distribution | June 1 | Pre-distribution materials ready per existing checklist |
| Domain 58 distribution | June 15 | Production pass complete; Trump v. Barbara rapid-response protocol staged |

---

## Framework Authority and Document Relationships

**Classification rules (authoritative):** `MAY_21_SYNTHESIS_EXECUTION_FRAMEWORK.md` — the authoritative source for all classification logic, scoring, and exception handling. In any conflict between this document and the Synthesis Execution Framework, the Synthesis Execution Framework governs.

**One-page path lookup:** `post-wave-1-monitoring/phase-2-path-activation-summary.md` — the fastest path to the right domain sequence after classification. Use this for quick reference; use this document for analysis.

**Operational metrics tracker:** `POST_SYNTHESIS_ANALYSIS_FRAMEWORK.md` — the detailed operational tracker with email metrics tables, Gist metrics, Pattern Recognition Template, and reporting milestones (May 22, May 24, May 28, June 4). This document focuses on Phase 2 research activation decisions; that document tracks the ongoing measurement infrastructure.

**Domain readiness audit:** `phase-2-research-activation-checklist.md` — comprehensive audit of all four domains' production readiness, source libraries, and blocking assumptions as of May 19, 2026. Cross-reference before any production start.

**WEAK root cause analysis:** `WEAK_OUTCOME_CONTINGENCY_PLAN.md` — five failure modes, five corrective action options (A–E), decision tree for choosing the right option. Required reading before any content or contact-list changes in a WEAK outcome.

---

*Created: May 19, 2026. Read at: May 21, 20:00 UTC (immediately post-synthesis CHECKIN.md post). Confirmed at: May 25 final gate. Expires as primary decision document: June 15, 2026 (after Phase 2 launch decisions are locked).*

*Domain 42 DEA reminder (path-independent): Docket No. DEA-1362. nprm@dea.gov. Electronic deadline May 24, 11:59 p.m. ET. Hard cutoff May 28. Execute regardless of synthesis classification.*

*Domain 39 reminder (path-independent): June 1 pre-distribution is non-negotiable across all four synthesis paths.*
