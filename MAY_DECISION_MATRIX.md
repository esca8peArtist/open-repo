---
title: May 2026 Decision Matrix & Timeline Coordination
project: Cross-Project
prepared: 2026-05-09 07:30 UTC
audience: thorn (user)
purpose: Comprehensive coordination of 5 concurrent project deadlines (May 9-30) with user decision points and resource constraints
---

# May 2026 Critical Decisions & Timeline Coordination

## IMMEDIATE (MAY 9-12): THE 4-DAY WINDOW

### TODAY (May 9, 2026) — DOMAIN 42 DISTRIBUTION DECISION ⏰ URGENT

**Question**: Execute Domain 42 (Drug Policy) distribution in Category A (Wave 1: May 8-9, now 1 day late) or defer?

**Context**: 
- DEA cannabis scheduling hearing June 29, 2026
- Public comment deadline **May 28** (19 days from now)
- Wave 1 sends to 10 drug policy organizations (NORML, DPA, MPP, etc.) with "submit comments" call-to-action
- All materials prepared and ready (template, contact list, Gist structure)

**Decision Options**:
1. **Path A — Execute NOW** (May 9):
   - Wave 1 (May 9-10): Drug policy category A orgs (10 contacts, 2 hours)
   - Wave 2 (May 10-12): Civil rights/academic (assume 3 hours)
   - Wave 3 (May 14-17): State AGs (4 hours, can proceed in parallel with stockbot checkpoint)
   - Total 9 hours over 9 days
   - Risk: User attention split during May 12 stockbot checkpoint
   - Benefit: 19-day buffer before DEA May 28 deadline

2. **Path B — Defer** (defer to May 13+):
   - Focus entirely on May 12 stockbot checkpoint
   - Distribute May 13-14 (after checkpoint complete)
   - Pushes Wave 1 end date to May 14, Wave 3 end to May 19
   - Still 9 days before May 28 deadline (feasible but compressed)
   - Risk: If stockbot checkpoint cascades (failures found, rapid retesting), May 13-14 might slip to May 15

**Recommendation**: **Path A (Execute Now)**
- Rationale: May 28 deadline is non-negotiable (statutory). 19-day buffer is margin-of-safety. Stockbot checkpoint is monitoring-only (no code changes required May 12), so can parallelize.

**User Action Needed**:
- Reply to this document or CHECKIN.md: "Execute Domain 42 now" or "Defer to May 13"

---

### MAY 12 (3 days) — STOCKBOT GATE 1 CHECKPOINT ⏰ CRITICAL

**What happens**: Run readiness validation at 20:00 UTC on May 12. Checkpoint will classify outcome (PASS / NEAR_MISS / FAR_MISS). No code changes — purely monitoring.

**Status**: 
- ❌ **BLOCKER IDENTIFIED**: Jetson API endpoint unreachable (Session 918)
  - Container shows healthy status but HTTP requests timeout
  - Logs show OrderExecutor re-initialization loop (suspect DB lock or initialization bug)
  - Network connectivity is fine (ping works, Tailscale active)

**What Needs to Happen**:
1. **Before May 12 market open (13:30 UTC)**: Resolve Jetson API connectivity issue
   - Option A: Investigate initialization loop, fix root cause, restart container
   - Option B: If complex, perform Jetson hardware restart + container restart
   - Verification: `curl -s http://100.120.18.84:8000/api/ready` returns `{"status":"ready","sessions":2}`

2. **May 12 at 20:00 UTC**: Run `python3 projects/stockbot/gate-1-outcome-classification.py`
   - Script is ready and tested
   - Will classify as one of: PASS / NEAR_MISS_B1 / FAR_MISS_C1 / FAR_MISS_C2
   - Expected: FAR_MISS_C1 (AAPL h+10 exit fires May 13, one day after checkpoint)

3. **Post-checkpoint (May 12 20:00-22:00 UTC)**:
   - Review outcome classification
   - Log result to WORKLOG.md using template in gate-1-readiness-validation-may12.md
   - If FAR_MISS: No action (expected, timing artifact)
   - If NEAR_MISS: Trigger Lever A (threshold_multiplier reduction)
   - If actual FAIL: Escalation analysis (root cause diagnosis)

**Resource Estimate**: 
- Jetson fix: 0.5-2 hours (depending on root cause)
- Checkpoint execution: 2 minutes (script runs autonomously)
- Analysis: 20-30 minutes

**Dependency with Domain 42**:
- Can parallelize: Domain 42 Wave 2-3 can run May 10-12 while stockbot is being fixed
- Conflict only if Jetson fix requires extensive debugging (if so, defer Wave 2-3 to May 12 afternoon after checkpoint)

---

## MAY 13 (4 days) — DOMAIN 42 DEADLINE WINDOW + AAPL EXIT WINDOW

### Morning (0:00-13:30 UTC): Domain 42 Wave 2-3 Final Sends (if Path A chosen)

**What**: Send to civil rights/academic orgs (Wave 2, 18-20 hours from Wave 1 send) + state AGs (Wave 3, 4-5 days from Wave 1 send)

**Resource**: 2-3 hours (Wave 2) + 4 hours (Wave 3 with personalization) = 6 hours total

**Note**: Wave 2 timeline is strict (18-20 hour window from Wave 1 for engagement effect). Cannot slip beyond May 13 afternoon.

### Afternoon (13:30-20:00 UTC): AAPL Exit Window + Gate 1b Checkpoint Prep

**What**: AAPL h+10 scheduled exit fires during this market session

**Why it matters**: This is the first (and possibly only) confirmed round trip in Gate 1. Exit should generate 1-2 SELL fills, confirming position closure.

**Monitoring**: 
- Check database at 20:00 UTC: `SELECT COUNT(*) FROM trades WHERE action='SELL' AND date(timestamp)='2026-05-13' AND ticker='AAPL'`
- Expected: 1-2 SELL fills (completing original April 29 BUY)
- If 0 fills: escalation trigger (h+10 logic failure or AAPL position already sold)

**Action**: Log result to WORKLOG.md for ongoing Gate 1b monitoring (formal deadline June 4, need 5 confirmed round trips)

---

## MAY 30 (21 days) — SEEDWARDEN PHASE 2 LAUNCH WINDOW

**Status**: All automation, setup guides, and logistics complete (Session 917)

**What needs to happen**:
1. **May 24-26**: User final review of Phase 2 materials + approve launch sequence
2. **May 30 10:00 UTC**: Begin launch sequence (Etsy → Email → Social in coordinated timing per existing timeline)

**Current state**:
- ✅ All 8 automation files ready (email templates, social scheduler, analytics dashboard, contingency playbook, launch-day checklist)
- ✅ 3 setup guides ready (social account config, Canva Brand Kit, Kit landing page)
- ✅ Phase 2 photography complete (May 30 deadline for field shoot content)
- ✅ Analytics framework ready (Day 1 adoption tracking)
- ⏳ Phase 1 tag corrections (user action, Track A only) — not blocking Phase 2

**Resource required**: Primarily user execution (4-6 hours on May 30, coordinating 3 simultaneous launches). Orchestrator role: monitoring + contingency execution if needed.

---

## MAY 28 (19 days) — DOMAIN 42 DEA COMMENT DEADLINE

**Hard deadline**: Public comments must be submitted by this date for DEA hearing (June 29)

**Why this matters**: Non-negotiable federal deadline. Comments are the only mechanism for Phase 1 recipients to participate in cannabis scheduling policy.

**Current status**: All materials ready. Timeline requires:
- Wave 1 complete by May 10 (gives 18-day buffer)
- Wave 2 complete by May 13 (gives 15-day buffer, but time-sensitive window for engagement effect)
- Wave 3 complete by May 19 (gives 9-day buffer)
- Wave 4 (reminder) by May 21 (7 days before deadline)

**If execution deferred**: Must complete by May 21 latest (7-day buffer minimum). Any slip past May 21 risks missing deadline.

---

## RESOURCE CONSTRAINT ANALYSIS

### May 9-12 (4-day crunch window)

| Day | Stockbot | Domain 42 | Other |
|-----|----------|-----------|-------|
| May 9 (today) | Jetson debugging (0-2 hrs) | Path A: Wave 1 send (2 hrs) | Monitor |
| May 10 | Complete debugging (0-1 hrs) | Path A: Wave 2 begins (3 hrs) | Seedwarden prep monitoring |
| May 11 | Final verification (0.5 hrs) | Wave 2 continues (2 hrs) | Seedwarden prep monitoring |
| May 12 | Checkpoint ready (0 hrs) + Run at 20:00 UTC (2 min) | Wave 2 tail send + Wave 3 begins (4 hrs) | Monitoring |

**Conflict zones**:
- May 12 afternoon: If Jetson debugging still ongoing, Wave 3 personalization may need deferral to May 13 morning
  - Mitigation: Prepare Wave 3 templates in parallel with Jetson debugging (can parallelize)

### May 13-30 (continuation phase)

| Milestone | Effort | User? | Notes |
|-----------|--------|-------|-------|
| May 13 morning | Wave 2 close + Wave 3 final | 3 hrs | Parallel OK with AAPL monitoring |
| May 13 afternoon | AAPL exit monitoring | 0.5 hrs (monitor) | Automated |
| May 19 | Wave 3 complete | 0 hrs | Should be complete by now |
| May 21 | Domain 42 Wave 4 reminder | 1 hr | Optional but recommended |
| May 24-26 | Seedwarden Phase 2 final review | 2 hrs | User approval gate |
| May 30 | Seedwarden Phase 2 launch | 4-6 hrs | Coordinated 3-way launch |

**Bottleneck**: May 12 afternoon (stockbot checkpoint + Domain 42 Wave 3 send). Solvable by parallelizing Wave 3 template prep on May 10-11.

---

## DECISION TREE — IF YOU CHOOSE PATH A (EXECUTE DOMAIN 42 NOW)

```
TODAY (May 9, 2026)
│
├─► Jetson Debugging (0-2 hours)
│   ├─ Investigate OrderExecutor loop / DB lock issue
│   └─ Verify fix: curl http://100.120.18.84:8000/api/ready
│
├─► Domain 42 Wave 1 SEND (2 hours) ← PARALLELIZE WITH JETSON DEBUG
│   ├─ Verify email templates (5 min)
│   ├─ Verify contact list (5 min)
│   ├─ Send Wave 1 (10 drug policy orgs) (60 min)
│   └─ Log send event + monitor for bounces (30 min)
│
└─► Evening: Review and log to CHECKIN.md
    └─ Jetson status
    └─ Domain 42 Wave 1 results
    └─ Next day priorities

DAY 2-3 (May 10-11)
│
├─► Complete Jetson debugging (if needed)
│   └─ Verify /api/ready returns {"status":"ready","sessions":2}
│
├─► Domain 42 Wave 2 & 3 Template Prep (2 hrs)
│   ├─ Personalize civil rights/academic templates
│   └─ Prepare state AG templates + contact mapping
│
└─► Evening: Ready for Wave 2 send

DAY 4 (May 12) — CRITICAL DAY
│
├─► Morning (6:00-13:30 UTC)
│   ├─ Domain 42 Wave 2 SEND (civil rights/academic) (90 min)
│   └─ Verify no bounces
│
├─► Afternoon (13:30-20:00 UTC) — STOCKBOT CHECKPOINT
│   ├─ Run readiness validation (10 min pre-market-open)
│   ├─ Monitor stockbot trading (passive, logs show activity)
│   └─ Run gate-1-outcome-classification.py at 20:00 UTC (2 min)
│
└─► Evening (20:00-22:00 UTC)
    ├─ Review checkpoint outcome
    ├─ Log result to WORKLOG.md
    └─ If PASS: Begin Gateway 2 planning
```

---

## DECISION TREE — IF YOU CHOOSE PATH B (DEFER DOMAIN 42)

```
TODAY (May 9) — FOCUS ENTIRELY ON JETSON
│
├─► Jetson Debugging (1-3 hours, no parallel pressure)
│   ├─ Deep-dive investigation of OrderExecutor loop
│   ├─ Check database locks, transaction state
│   ├─ Consider hardware restart if software doesn't resolve
│   └─ Verify /api/ready responds properly
│
├─► Evening: Log findings
│   └─ If resolved: Mark Jetson block as resolved
│   └─ If unresolved: Escalate to BLOCKED.md for May 12 checkpoint risk
│
└─► Decision point: Is Jetson likely to be fixed by May 12?
    ├─ YES → Proceed with Path B (defer Domain 42)
    └─ NO → Escalate to user immediately (risk to May 12 checkpoint)

MAY 13-14 (POST-CHECKPOINT)
│
├─► May 13 morning: Assess checkpoint outcome
│   └─ If PASS or NEAR_MISS → Celebrate, begin Phase 2 planning
│   └─ If FAR_MISS → Analyze root causes, plan recovery
│
├─► May 13-14: Domain 42 Wave 1 SEND (now 1-2 days late)
│   ├─ Still 14 days until May 28 deadline (comfortable)
│   └─ Send to all 10 Wave 1 orgs
│
└─► May 14-17: Domain 42 Wave 2-3 (compressed 4-day window)
    └─ Requires parallel send (higher volume, time-compressed)
```

---

## RECOMMENDATIONS FOR IMMEDIATE ACTION

### Rank 1: DECIDE ON DOMAIN 42 (Do this TODAY)
- **Decision window**: Right now. Lock in Path A or Path B.
- **Rationale**: Timing cascade depends on this. Path A has 19-day deadline buffer (safe). Path B needs 14-day buffer (feasible but tighter).

### Rank 2: TRIAGE JETSON ISSUE (Next 2-4 hours)
- Jetson debugging
- Fix or escalate by end of today
- May 12 checkpoint depends on it

### Rank 3: PREPARE WAVE 2-3 TEMPLATES (May 10-11)
- Parallelize with Jetson debugging
- Enables smooth Wave 2 send on May 12

---

## RESOURCE SUMMARY — MAY 9-30

| Project | Total Hours | User | Orchestrator | Dependencies |
|---------|-------------|------|--------------|--------------|
| Stockbot (May 9-13) | 3-5 | Jetson debug | Monitoring + checkpoint | Jetson connectivity |
| Domain 42 (May 9-21) | 9 | Path A: Yes / Path B: Yes | Monitoring | User path decision |
| Seedwarden (May 24-30) | 4-6 | Phase 2 launch execution | Monitoring + contingency | Phase 1 materials ready ✅ |
| General monitoring | 2-3 | Light (emails, Discord) | Continuous | Ongoing |
| **Total User Hours** | **16-23 hrs** | **Depends on Path** | — | — |
| **Total Spread** | **Over 21 days** | **~1-1.5 hrs/day avg** | — | — |

---

## NEXT STEPS

1. **RIGHT NOW**: Reply with Domain 42 decision (Path A execute now / Path B defer)
2. **Within 1 hour**: Verify Jetson status and either fix or escalate
3. **May 10-11**: Parallelize Domain 42 template prep with any lingering Jetson work
4. **May 12**: Execute checkpoint (monitoring-only, autonomous)
5. **May 13**: Complete Domain 42 distribution sequence
6. **May 24-26**: Approve Seedwarden Phase 2 launch materials
7. **May 30**: Execute Seedwarden Phase 2 launch

---

## WATCH-OUTS

- ⚠️ **May 28 is NON-NEGOTIABLE** for Domain 42 (federal statute deadline). Must complete by May 21 latest.
- ⚠️ **May 12 Jetson connectivity** is CRITICAL for Gate 1 checkpoint. If unresolved by May 12 morning, May 12 checkpoint will be incomplete and escalate Gate 1b timeline.
- ⚠️ **May 13 Wave 2 timing** (if Path A): 18-20 hour window from Wave 1 send is optimal for engagement. May not slip past May 13 noon without efficacy loss.
- ⚠️ **May 30 Seedwarden** depends on Phase 1 tag corrections being approved (user action, not blocker but advisory).

---

## QUESTIONS FOR USER

1. **Domain 42**: Execute now (Path A) or defer (Path B)? [CRITICAL DECISION]
2. **Jetson**: Can you investigate the OrderExecutor initialization loop, or should I escalate for hardware troubleshooting?
3. **Seedwarden Phase 2**: Are there any final approvals needed from you before May 24 (5 days)?

---

*Document prepared by: Autonomous Orchestrator Session 918 (2026-05-09 07:30 UTC)*
*Status: READY FOR USER DECISION*
