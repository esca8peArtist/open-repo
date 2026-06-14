# Wave 1-2 Revised Timeline
## Resistance-Research Phase 2 — Updated Execution & Checkpoint Dates

**Current Date**: June 14, 2026  
**Wave 1 Status**: Overdue (due June 9-10, now June 14)  
**Recovery Window**: Still open, July 1 hard deadline  
**Scenario**: Wave 1 executed June 14 (today) → revised timeline below

---

## Timeline Comparison: Original vs. Actual

| Milestone | Original Plan | Actual (if sent June 14) | Delta | Impact |
|---|---|---|---|---|
| **Wave 1 Send** | June 9-10 (90 min) | June 14 (90 min) | +4-5 days | TBD |
| **Wave 2 Send** | June 12 (90 min) | June 14 EOD or June 15 | +2-3 days | Minimal |
| **Day 7 Checkpoint** | June 16 (metrics collection) | June 21 (metrics collection) | +5 days | 5-day compressed decision window |
| **Phase 2 Batch Activation** | June 16-20 | June 21-25 | +5 days | Affects Domain 48 Virginia deadline |
| **Hard Deadline (July 1)** | 22 days from June 9 | 17 days from June 14 | -5 days | Still achievable |

---

## Wave 1 Execution Scenario (June 14)

### Send Schedule
- **Email 1 (CLC)**: June 14, [TIME] UTC (now)
- **Email 2 (Issue One)**: June 14, [TIME] + 90 min UTC
- **Total duration**: 2.5 hours (includes send, verification, logging)

### Recipient Contact Points
| Organization | Contact | Email | Send Time | Expected Response |
|---|---|---|---|---|
| Campaign Legal Center | Erin Chlopak | echlopak@ | June 14, [T] UTC | By June 21 |
| Issue One | info@issueone.org | info@issueone.org | June 14, [T+90m] UTC | By June 21 |

### Expected Response Window
- **First responses**: June 14-15 (same-day replies from staff monitoring emails)
- **Open rate window**: June 14-15 (first 24 hours)
- **Gist click window**: June 14-21 (7 days)
- **Full response window**: June 14-21 (7 days)

---

## Wave 2 Execution Scenario (June 14-15)

### Timing Option A: Send Today (June 14 Evening)
**Feasible only if Wave 1 finishes before 18:00 UTC**

| Contact | Email | Send Time | Stagger |
|---|---|---|---|
| Common Cause CA | dkemp@commoncause.org | June 14, 18:00 UTC | 4 hours after Wave 1 Email 2 |
| LWV CA | lwvc@lwvc.org | June 14, 19:30 UTC | 90 min after Common Cause CA |
| Clean Money Action | info@CAclean.org | June 14, 21:00 UTC | 90 min after LWV CA |

**Completion time**: June 14, 21:30 UTC (same day as Wave 1)

### Timing Option B: Send Tomorrow (June 15)
**Recommended if Wave 1 completes after 18:00 UTC or user needs rest**

| Contact | Email | Send Time | Stagger |
|---|---|---|---|
| Common Cause CA | dkemp@commoncause.org | June 15, 09:00 UTC | Next morning |
| LWV CA | lwvc@lwvc.org | June 15, 10:30 UTC | 90 min stagger |
| Clean Money Action | info@CAclean.org | June 15, 12:00 UTC | 90 min stagger |

**Completion time**: June 15, 12:30 UTC (next morning)

### Wave 2 Response Window
- **First responses**: June 15-16 (overnight if June 14 sends, same-day if June 15 sends)
- **Open rate window**: June 15-16
- **Gist click window**: June 15-22
- **Full response window**: June 15-22 (7 days)

---

## Day 7 Checkpoint Timeline

### Checkpoint Dates (adjusted from June 16 to June 21)

**Scenario A: Wave 1 on June 14**
- **Day 1** (Mon, June 14): Wave 1 emails sent
- **Day 7** (Sun, June 21): **Day 7 Checkpoint** — collect metrics, assess STRONG/MODERATE/WEAK signals
  - Checkpoint time: 09:00 UTC June 21
  - Metrics collection: 09:00-09:20 UTC (Campaign Monitor opens, Gist views, contact replies)
  - Decision logic: 09:20-09:25 UTC (route to GO/CAUTION/NO-GO)
  - Result: By 09:30 UTC June 21

**Wave 2 launches**: Post-checkpoint decision
- If STRONG signal (≥8 total, from CLC + Issue One): Launch Domains 48 + 57 **parallel** starting June 21-22
- If MODERATE signal (5-7 total): Launch Domain 48 June 21-22, defer Domain 57 to June 24-25 (sequential)
- If WEAK signal (<5): Assess whether to activate Phase 2 at all vs. focus on improving engagement

### Checkpoint Automation
- [ ] **PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE.md** will auto-update on June 21
- [ ] Orchestrator will poll Campaign Monitor, Gist analytics, contact inboxes
- [ ] Decision Checkpoint Record will be populated by 09:30 UTC
- [ ] Phase 2 activation decision will be routed to PROJECTS.md by 10:00 UTC

---

## Virginia Advocacy Window Impact

**Domain 48 (Criminal Justice/Civic Exclusion)** has a hard advocacy deadline: **July 15 coalition integration window**

### Original Timeline Impact (5-day slip)
| Date | Milestone | Original | Revised | Impact |
|---|---|---|---|---|
| June 16 | Day 7 checkpoint | Yes | No | — |
| June 16-20 | Domain 48 research window | 5 days | No | Slips to June 21-25 |
| June 20-22 | Domain 48 contact outreach | Yes | No | Slips to June 25-27 |
| July 15 | Virginia HJR 2 coalition deadline | 29-30 days from June 16 | 20-21 days from June 14 | **Still achievable** |

### Feasibility Assessment
- **Original plan**: June 16-20 Domain 48 research, June 20-22 contact outreach, June 22-July 15 (23 days) for coalition action
- **Revised plan**: June 21-25 Domain 48 research, June 25-27 contact outreach, June 27-July 15 (18 days) for coalition action
- **Risk level**: MEDIUM (18 days is tight but feasible; Virginia advocacy window is not forfeited)
- **Mitigation**: If Wave 1 metrics are STRONG, activate parallel track (Domain 48 + Domain 57 simultaneously starting June 21-22)

---

## Resource Contention Check (June 14-July 1)

### Parallel Projects During Wave 1-2 Recovery
| Project | Status | June 14-21 | June 21-July 1 | Notes |
|---|---|---|---|---|
| **stockbot** | Active, P3 blocked | User decision June 15 | P3 implementation June 16-18 | Independent, no resource conflict |
| **resistance-research** | Active, Wave 1-2 | Wave 1 June 14, Wave 2 June 14-15 | Phase 2 batch June 21+ | Primary focus |
| **seedwarden** | Active | Contractor decision June 17 | Phase 3 launch June 22 | Independent timing |
| **systems-resilience** | Awaiting decisions | Platform choice pending | Wave 2 recruitment June 14+ | Awaiting user input on platform |

**Contention Assessment**: **LOW** (Wave 1-2 execution is light-weight; P3 implementation is June 16-18 only; seedwarden and systems-resilience are independent)

---

## Hard Deadlines & Recovery Feasibility

### Three Immovable Deadlines (from Item 107)

| Domain | Deadline | Time Remaining from June 14 | Feasibility |
|---|---|---|---|
| Domain 48 (Criminal Justice) | July 15 Virginia coalition integration | 31 days | ✅ ACHIEVABLE |
| Domain 49 (Redistricting) | Dec 31 litigation filing deadline | 200+ days | ✅ ACHIEVABLE |
| Phase 3 Domain K + H | Jan 3, 2027 Congress seating | 204 days | ✅ ACHIEVABLE |

**Overall feasibility**: Wave 1-2 recovery is still within recoverable slip window. 17 days to July 1 hard deadline is sufficient.

---

## Phase 2 Research Activation Timeline (Post-Day-7-Checkpoint)

### If STRONG Signal (June 21 checkpoint):
```
June 21-22: Launch Domains 48 + 57 in PARALLEL
  - Domain 48: June 21-July 4 research (2 weeks, 40-50 hours)
  - Domain 57: June 21-July 5 research (2 weeks, 40-50 hours)
June 22-27: Contact outreach (48 + 57 simultaneous)
June 27: Gist publication (Domain 48) + contact distribution
July 1: Domain 57 pre-launch gist publication
```

### If MODERATE Signal (June 21 checkpoint):
```
June 21-25: Domain 48 research only (40-50 hours)
June 25-27: Domain 48 contact outreach
June 27: Domain 48 gist publication + distribution
July 1: Domain 57 research begins (separate phase)
```

### If WEAK Signal (June 21 checkpoint):
```
Assessment required: 
  - Escalate engagement? (add Tier 2 contacts)
  - Defer Phase 2? (consolidate research into October)
  - Recommend to user: TBD based on June 21 metrics
```

---

## Execution Checklist

### Wave 1 (June 14) — 90 minutes
- [ ] WAVE_1_RECOVERY_EXECUTION_SOP.md reviewed
- [ ] Email 1 (CLC) sent: __________ UTC
- [ ] Email 2 (Issue One) sent: __________ UTC
- [ ] Execution log updated
- [ ] Gist accessibility verified

### Wave 2 (June 14-15) — 90 minutes
- [ ] Option A (June 14 evening) OR Option B (June 15 morning) selected
- [ ] Email 1 (Common Cause CA) sent: __________ UTC
- [ ] Email 2 (LWV CA) sent: __________ UTC
- [ ] Email 3 (Clean Money Action) sent: __________ UTC
- [ ] Execution log updated

### Day 7 Checkpoint (June 21) — Automated
- [ ] Checkpoint automation runs 09:00 UTC
- [ ] Metrics collected (Campaign Monitor, Gist, contact replies)
- [ ] Decision routing: STRONG/MODERATE/WEAK
- [ ] PROJECTS.md updated with Phase 2 activation plan

### Phase 2 Launch (June 21+) — Based on checkpoint outcome
- [ ] Domain 48 research begins (STRONG/MODERATE signals)
- [ ] Domain 57 research begins (STRONG signal only, or July 1 start)
- [ ] Contact outreach scheduled per parallel/sequential plan

---

## Summary: Impact of 5-Day Slip

| Metric | Original | Revised | Risk |
|---|---|---|---|
| **Recovery Feasibility** | N/A | Achievable (17 days to July 1 deadline) | ✅ LOW |
| **Virginia Deadline (July 15)** | 29 days | 20 days | ✅ LOW (still tight but doable) |
| **Phase 2 Batch Activation** | June 16 | June 21 | ✅ LOW (5-day delay, parallel mitigation available) |
| **Day 7 Checkpoint** | June 16 | June 21 | ✅ LOW (date shifted, logic unchanged) |
| **July 1 Hard Deadline** | 22 days from June 9 | 17 days from June 14 | ✅ MEDIUM (compressed, still achievable) |

**Recommendation**: Execute Wave 1 today (June 14) and Wave 2 June 14 evening or June 15 morning. All timelines remain achievable with no loss of Phase 2 objectives.

---

## How to Adjust If Timelines Slip Further

If Wave 1 is delayed beyond June 14:
- **June 15 send**: Day 7 checkpoint June 22; Phase 2 activation June 22-23; still within Virginia deadline (22 days remaining)
- **June 16 send**: Day 7 checkpoint June 23; Phase 2 activation June 23-24; 21 days to July 1 (tight but achievable)
- **June 17 send**: Day 7 checkpoint June 24; Phase 2 activation June 24-25; 14 days to July 1 (escalate Virginia timeline)
- **Beyond June 17**: Contact user to confirm Virginia deadline is still viable; may require deferring Domain 57 to post-July 1

Each additional day of delay costs 1 day of Phase 2 preparation time before July 1 hard deadline.
