---
title: Phase 2 Batch Sequencing Post-Domain-51 Decision
created: 2026-06-06
version: 1.0
status: production-ready
scope: >
  Routes Domain 51 Day 7 checkpoint decision to Phase 2 batch activation (Domains 48 + 57).
  Pre-stages contact lists, verifies distribution infrastructure, sequences sends to avoid contact fatigue.
deadline: June 16-20 (Domain 48 activation), June 20-25 (Domain 57 activation)
companion_files:
  - DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md (input metrics)
  - DOMAIN_51_JUNE_16_DECISION_LOGIC.md (input: composite score + decision routing)
  - DOMAIN_48_DISTRIBUTION_EXECUTION_INFRASTRUCTURE.md (contact list, templates, Gist)
  - DOMAIN_57_DISTRIBUTION_EXECUTION_INFRASTRUCTURE.md (contact list, templates, Gist)
purpose: >
  Eliminates delays between Day 7 decision and Phase 2 activation. All contact lists verified,
  distribution templates staged, Gist URLs live, send windows locked. Execution ready
  within 24 hours of STRONG/MODERATE decision.
---

# Phase 2 Batch Sequencing Post-Domain-51 Decision

**Input**: Domain 51 Day 7 checkpoint decision (from DOMAIN_51_JUNE_16_DECISION_LOGIC.md)

**Decision execution window**: June 16, 09:35–10:00 UTC (immediately after decision routing)

---

## 1. Routing from Domain 51 Decision to Phase 2 Activation

### If STRONG Signal (Score 8-10)
→ Go to **Section 2.1 (Parallel Batch Activation)**

### If MODERATE Signal (Score 5-7)
→ Go to **Section 2.2 (Sequential Batch Activation)**

### If WEAK Signal (Score 3-4)
→ Go to **Section 3 (Hold — No Phase 2 Activation)**

### If FAILURE Signal (Score <3)
→ Go to **Section 3 (Hold — Contingency Protocol Only)**

---

## 2. Phase 2 Batch Activation Plans

### 2.1 STRONG Path — Parallel Batch Activation (Domains 48 + 57)

**Parallel activation**: Send Domain 48 and 57 to different contact pools with minimal overlap, staggered 3-5 days apart to avoid contact fatigue.

**Rationale for parallelism**:
- Domain 51 (campaign finance) targets: campaign finance reform organizations (CLC, Common Cause, Issue One)
- Domain 48 (criminal justice) targets: civil rights organizations, voting rights groups (Sentencing Project, PPI, Brennan Center)
- Domain 57 (multilateral withdrawal) targets: international affairs specialists, think tanks (CFR, Brookings, Cato)
- **Contact overlap**: 0-1 organizations (CLC and Brennan both focus on voting rights, but CLC's primary role is campaign finance vs Brennan's criminal justice focus → negligible conflict)

#### Phase 2.1a — Domain 48 Activation (June 16-20 send window)

**Infrastructure verification** (5-minute pre-flight, June 16 10:00–10:05 UTC):

| Component | Status | Verification Check | Notes |
|-----------|--------|-------------------|---------|
| Contact list | Ready | File exists: `DOMAIN_48_CONTACT_LIST_AND_STRATIFICATION.md` (4 primary Tier A: Sentencing Project, PPI, Brennan Center, Worth Rises) | Verified June 5 (Session 2884) — current |
| Email templates | Ready | File exists: `DOMAIN_48_EMAIL_TEMPLATE_SET.md` (4 templates: criminal justice/sentencing, voting rights, state/local legislative, movement justice) | Verified June 5 — copy-paste ready |
| Gist document | Ready | File exists: `domain-48-criminal-justice-civic-exclusion.md` (production-ready Gist) | Verified June 5 — live |
| Gist URL | Ready | Bitly short link created and tested | Test: Click Bitly link, confirm Gist loads without error |
| Send log template | Ready | File exists: `DOMAIN_48_DISTRIBUTION_SEND_LOG_TEMPLATE.md` | Use for wave tracking |
| Contingency contacts | Ready | Secondary contacts documented (NAACP LDF, ACLU of Virginia, Fines & Fees Justice Center) | Use if Tier A non-responsive |

**Pre-send checklist** (complete by June 16 16:00 UTC):
- [ ] Domain 48 Gist live and current (check last edit date)
- [ ] Bitly short link resolves to Gist without error
- [ ] All 4 Tier A contact emails verified (cross-check against organizational websites for current staff)
- [ ] Email templates reviewed and personalized (primary contact names, organizational hooks, Domain 51 social proof if STRONG signal)
- [ ] Draft send schedule locked: Tier A Wave 1 sends June 16-20 (4 sends staggered Mon-Fri, 1-2 per day to avoid spam-folder clustering)

**Send schedule** (Domain 48 Wave 1, June 16-20):
| Date | UTC Time | Contact | Template | Notes |
|------|----------|---------|----------|---------|
| June 16 | 09:00 | Sentencing Project | Criminal Justice/Sentencing | Lead contact (highest-impact org) |
| June 17 | 10:00 | PPI (Prison Policy Initiative) | Criminal Justice/Sentencing | Follow-up to amplify signal |
| June 18 | 09:00 | Brennan Center (Voting Rights division) | Voting Rights | Cross-reference to Domain 51 (voting suppression angle) |
| June 20 | 10:00 | Worth Rises | Movement Justice | Cross-reference to Domain 51 (LFO-as-poll-tax angle) |

**Monitoring during send window**:
- Bitly clicks: Expect ≥2 clicks per day during June 16-20 (monitor hourly)
- Email bounces: Check Campaign Monitor bounce log daily; if any bounce detected, escalate contact update
- Reply velocity: Expect first substantive reply within 48 hours of send (June 17-19)

#### Phase 2.1b — Domain 57 Activation (June 20-22 send window)

**Infrastructure verification** (5-minute pre-flight, June 20 09:00–09:05 UTC):

| Component | Status | Verification Check | Notes |
|-----------|--------|-------------------|---------|
| Contact list | Ready | File exists: `DOMAIN_57_CONTACT_LIST_AND_STRATIFICATION.md` (expected: think tanks, international affairs specialists) | Verify as of June 13 (cutoff date for Phase 2 pre-staging) |
| Email templates | Ready | File exists: `DOMAIN_57_EMAIL_TEMPLATE_SET.md` (expected: 3-4 templates for international affairs, legislative affairs, think tank research) | Verify production-ready status |
| Gist document | Ready | File exists: `domain-57-multilateral-withdrawal-war-powers.md` (production-ready Gist) | Verify live and current |
| Gist URL | Ready | Bitly short link created and tested | Test: Click Bitly link, confirm Gist loads |
| Send log template | Ready | File exists: `DOMAIN_57_DISTRIBUTION_SEND_LOG_TEMPLATE.md` | Use for wave tracking |

**Pre-send checklist** (complete by June 20 16:00 UTC):
- [ ] Domain 57 Gist live and current
- [ ] Bitly short link resolves without error
- [ ] All Tier A contact emails verified (international affairs specialist contacts at major think tanks)
- [ ] Email templates reviewed and personalized
- [ ] Draft send schedule locked: Tier A Wave 1 sends June 20-22 (2-3 sends staggered Wed-Fri)

**Send schedule** (Domain 57 Wave 1, June 20-22):
| Date | UTC Time | Organization/Contact | Template | Notes |
|------|----------|----------------------|----------|---------|
| June 20 | 09:00 | [Top-tier international affairs contact] | [Multilateral withdrawal framing] | Lead send (highest-salience topic) |
| June 21 | 10:00 | [Secondary think tank contact] | [War powers angle] | Amplification send |
| June 22 | 09:00 | [Academic contact] | [Constitutional analysis framing] | Research community angle |

**Monitoring during send window**:
- Bitly clicks: Expect ≥2 clicks across all sends (lower bar than Domain 48, different audience)
- Reply velocity: Expect first reply within 48-72 hours (international affairs specialists often slower than policy organizations)

#### Phase 2.1 Secondary Checkpoint (June 23)

**Assessment**: Post-Domain-48-send evaluation

| Metric | Target (acceptable) | Action if below target |
|--------|-------------------|----------------------|
| Domain 48 email open rate | ≥40% | Investigate subject line friction; prepare re-send for secondary contacts |
| Domain 48 Bitly clicks | ≥2 total across 4 sends | Check Bitly link; verify delivery; escalate if delivery confirmed but clicks zero |
| Domain 48 reply rate | ≥20% (at least 1 of 4) | Normal; continue monitoring for Day 30 sustained engagement |

**Decision point**: If all metrics acceptable, Domain 57 send window proceeds as scheduled (June 20-22). If any metric below target, assess whether Domain 57 continues or holds pending user review.

---

### 2.2 MODERATE Path — Sequential Batch Activation (Domain 48 → Domain 57)

**Sequential activation**: Send Domain 48 and 57 to staggered windows (4-7 days apart) to avoid contact fatigue and allow checkpoint decisions between activations.

**Rationale for sequencing**:
- Domain 48 (criminal justice + voting suppression angle) complements Domain 51 directly (campaign finance + voting suppression ecosystem)
- Domain 57 (multilateral withdrawal + war powers) addresses different audience (international affairs specialists)
- Sequential execution allows Day 23 secondary checkpoint decision before Domain 57 commitment

#### Phase 2.2a — Domain 48 Activation (June 16-20 send window)
**Same as Section 2.1a** (identical send schedule and monitoring)

#### Phase 2.2b — Secondary Checkpoint Decision (June 23)

**Assessment** (repeat metrics from Section 2.1 Secondary Checkpoint):
- Domain 48 email open rate: ≥40% acceptable
- Domain 48 Bitly clicks: ≥2 total acceptable
- Domain 48 reply rate: ≥20% (≥1 substantive reply) acceptable

**Routing decision**:
```
IF Domain 48 metrics ≥ acceptable thresholds:
  → Proceed to Domain 57 activation (June 23-25 send window) — [Same as Section 2.1b, dates shifted]

ELSE IF Domain 48 metrics 50-75% of acceptable:
  → Hold Domain 57, escalate to user for decision (proceed with sequential or hold until Day 30 assessment)

ELSE IF Domain 48 metrics <50% of acceptable:
  → Hold Domain 57, escalate to user for Phase 2 reassessment
```

**If proceeding to Domain 57** (June 23-25 send window):

| Date | UTC Time | Organization | Template | Notes |
|------|----------|--------------|----------|---------|
| June 23 | 09:00 | [Lead international affairs contact] | [Multilateral withdrawal] | Staggered 3 days after Domain 48 final send (June 20) |
| June 24 | 10:00 | [Secondary think tank] | [War powers angle] | Sequential send |

**MODERATE path monitoring**: Same as STRONG path, but with explicit check-in at Day 23 secondary checkpoint.

---

## 3. Hold — No Phase 2 Activation (WEAK or FAILURE Signals)

**If Domain 51 composite score 3-4 (WEAK) or <3 (FAILURE)**:
- **Phase 2 activation**: NONE (deferred pending user decision or contingency protocol)
- **Monitoring continues**: Passive engagement tracking through Day 30 checkpoint (June 30)
- **Contingency pathway**: Refer to Section 3 in `DOMAIN_51_JUNE_16_DECISION_LOGIC.md` for contingency protocol options
- **Phase 2 re-evaluation**: Day 30 checkpoint (June 30) provides next decision point for Phase 2 activation or continued hold

---

## 4. Phase 2 Timeline Summary (All Scenarios)

### STRONG Path (Days 0-14)
```
June 16 (Day 0):  Domain 51 decision: STRONG
June 16 (Day 0):  Decision routed → Phase 2.1 parallel activation
June 16-20 (Days 0-4): Domain 48 Wave 1 send (4 contacts, staggered)
June 20-22 (Days 4-6): Domain 57 Wave 1 send (parallel, different audience)
June 23 (Day 7): Secondary checkpoint — confirm metrics ≥acceptable
June 23-30 (Days 7-14): Passive monitoring for Day 30 checkpoint
```

### MODERATE Path (Days 0-21)
```
June 16 (Day 0):  Domain 51 decision: MODERATE
June 16 (Day 0):  Decision routed → Phase 2.2 sequential activation
June 16-20 (Days 0-4): Domain 48 Wave 1 send (4 contacts, staggered)
June 23 (Day 7): Secondary checkpoint — Domain 48 metrics assessment
June 23-25 (Days 7-9): Domain 57 Wave 1 send (IF Domain 48 metrics ≥ acceptable)
June 25-30 (Days 9-14): Passive monitoring for Day 30 checkpoint
```

### WEAK/FAILURE Paths (Days 0-14)
```
June 16 (Day 0):  Domain 51 decision: WEAK or FAILURE
June 16-17:       Escalation email sent to user
June 17 (Day 1):  User decision deadline 18:00 UTC
June 17-24:       Hold period OR contingency protocol (pending user response)
June 24+:         Contingency re-send (if activated) or continued hold
June 30 (Day 14): Day 30 checkpoint — Phase 2 re-evaluation
```

---

## 5. Contact Overlap & Fatigue Assessment

**Goal**: Avoid sending multiple domains to same contact in short time window.

### Overlap Analysis (STRONG/MODERATE paths)

| Organization | Domain 51 (June 9-12) | Domain 48 (June 16-20) | Domain 57 (June 20-22/June 23-25) | Fatigue Risk | Mitigation |
|---|---|---|---|---|---|
| Campaign Legal Center | YES (Yusuf Maluf) | YES (different program) | NO | MEDIUM | Different internal program; acceptable 7-day spacing |
| Common Cause | YES (Cynthia Terrell) | NO (not Tier A for D48) | NO | LOW | No overlap — safe |
| Sentencing Project | NO | YES (primary) | NO | LOW | New audience — safe |
| Brennan Center | NO | YES (voting rights division) | NO | LOW | New audience — safe |
| Worth Rises | NO | YES (secondary) | NO | LOW | New audience — safe |
| [Think tank contacts] | NO | NO | YES (Domains 57 only) | LOW | No overlap — safe |

**Fatigue mitigation**:
- All inter-domain sends spaced ≥5 days apart (June 9-12 Domain 51 → June 16-20 Domain 48 → June 20-25 Domain 57)
- CLC receives Domain 51 + Domain 48 (same organization, different programs); frame Domain 48 as complementary (campaign finance funding dark money → criminal justice system resource allocation)
- All other Tier 1 contacts receive only one domain in June window (safe for cumulative engagement)

---

## 6. Critical Success Factors (CSF) — Pre-Launch Verification

**June 16 Pre-Flight Checklist** (complete before Phase 2 activation):

- [ ] Domain 48 infrastructure verified (contact list, templates, Gist, Bitly link)
- [ ] Domain 57 infrastructure verified as of June 13 cutoff (review for any June 13-16 updates needed)
- [ ] Contact overlap assessed; fatigue mitigations locked
- [ ] Send schedule locked (Domain 48: June 16-20, Domain 57: June 20-22 STRONG or June 23-25 MODERATE)
- [ ] Send log templates staged and ready for use during wave execution
- [ ] Bitly links tested (click each link, confirm Gist loads without error)
- [ ] Secondary contact contingency list ready (escalation triggers documented)
- [ ] Day 23 secondary checkpoint reminder set (calendar invite for June 23 09:00 UTC)
- [ ] Day 30 checkpoint reminder set (calendar invite for June 30 09:00 UTC)

---

## 7. Contingency Escalation Triggers

**Phase 2 activation may be interrupted if**:

1. **Domain 48 delivery failure** (detected June 16-20): If Campaign Monitor shows >1 bounce or >10% hard bounce rate:
   - Hold Domain 57 activation
   - Investigate contact list validity
   - Escalate to user for contact list verification and possible re-send to corrected addresses

2. **Domain 48 zero engagement** (detected by June 22): If Bitly shows <1 click across all 4 sends:
   - Assess whether Domain 57 should proceed
   - Likely scenario: Both domains experiencing similar friction → recommend hold Phase 2 pending user review

3. **External event** (e.g., legislative action, crisis): If news event makes Domain 48 or 57 timing sensitive:
   - Re-evaluate send dates in real-time
   - Example: If Congress passes surprise DISCLOSE Act vote in June, may want to accelerate Domain 48 and 57 to capture legislative window

---

## 8. Companion Documents

**Input documents** (referenced in routing logic):
- `DOMAIN_51_JUNE_16_DECISION_LOGIC.md` — provides composite score and decision output

**Domain 48 execution documents** (staged and ready):
- `DOMAIN_48_CONTACT_LIST_AND_STRATIFICATION.md` — Tier A/B/C contacts with verification status
- `DOMAIN_48_EMAIL_TEMPLATE_SET.md` — 4 copy-paste templates (criminal justice, voting rights, legislative, movement justice)
- `DOMAIN_48_GIST_CREATION_STEPS.md` — Gist URL and content verification
- `DOMAIN_48_DISTRIBUTION_SEND_LOG_TEMPLATE.md` — Send tracking and metrics collection

**Domain 57 execution documents** (staged and ready):
- `DOMAIN_57_CONTACT_LIST_AND_STRATIFICATION.md` — international affairs specialist contacts
- `DOMAIN_57_EMAIL_TEMPLATE_SET.md` — multilateral withdrawal and war powers framings
- `DOMAIN_57_DISTRIBUTION_EXECUTION_INFRASTRUCTURE.md` — complete execution checklist
- `DOMAIN_57_DISTRIBUTION_SEND_LOG_TEMPLATE.md` — send tracking

**Monitoring documents**:
- `PHASE_1_IMPACT_MEASUREMENT_DASHBOARD_TEMPLATE.md` — extended for Phase 2 multi-domain tracking
- `PHASE_1_DECISION_TREES.md` — Day 30 and Day 60 checkpoint procedures

---

## 9. Post-Execution Logging

**When Phase 2 activation completes**:
1. Update CHECKIN.md with Phase 2 batch sequencing decision and dates
2. Commit all three Domain 51 checkpoint documents to master:
   - `DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md` (with data populated)
   - `DOMAIN_51_JUNE_16_DECISION_LOGIC.md` (with decision routing output)
   - `PHASE_2_BATCH_SEQUENCING_POST_DOMAIN_51.md` (this document, with execution dates locked)
3. Create calendar reminders for Domain 48 and 57 checkpoint dates
4. Set up passive monitoring (Bitly tracking, Gmail reply alerts) for June 16-30 window

---

**Document ready for June 16 execution. All infrastructure pre-staged. Orchestrator can execute Phase 2 activation within 24 hours of STRONG/MODERATE decision.**
