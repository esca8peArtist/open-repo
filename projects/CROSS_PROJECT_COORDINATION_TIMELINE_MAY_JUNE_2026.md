# Cross-Project Coordination Timeline & User Decision Matrix
## May 9 – June 30, 2026

**Status**: Executive strategy document for multi-project orchestration  
**Audience**: User (Anya) — enables informed decision-making across 6 active projects with competing deadlines  
**Purpose**: Visualize all critical dates, resource conflicts, decision gates, and user attention requirements; provide decision tree for urgent May 9-13 window

---

## 1. Critical Path Timeline (May 9 – June 30)

### THIS WEEK — May 9–13 (URGENT USER DECISIONS)

| Date | Project | Event | Decision Required | Impact if Delayed | Owner | Duration |
|------|---------|-------|-------------------|-------------------|-------|----------|
| **May 9 (TODAY)** | resistance-research | **Domain 42 distribution path decision** (Path A / A+37 / B) | Choose path + authorize Wave 1 send | May 28 DEA deadline misses entirely (0% institutional participation) | User | 30 min |
| May 9 | resistance-research | Domain 42 Wave 1 ready-to-send (upon path decision) | Approve DPA + NORML templates | +24-48 hour phase delay | Orchestrator | 5 min |
| May 10 | stockbot | Jetson verification (Optional: hardware health check before May 12) | Monitor engine health OR request manual verification | Confidence in May 12 outcome reduced | Orchestrator | 15 min |
| May 11 | stockbot | **DB sync (critical for May 12 checkpoint)** — user runs manual sync command | Execute: `uv run python scripts/sync_db_from_alpaca.py --since 2026-04-29 --db database/trading.db` | Time-stop SELL fill not recorded; May 12 checkpoint shows 0 confirmed round trips | User | 5 min |
| May 12 | stockbot | **Gate 1 checkpoint execution** at 20:00 UTC | Run checkpoint query, assign scenario, log outcome | Checkpoint 3 months delayed (no decision until May 26) | Orchestrator | 10 min |
| May 13 | resistance-research | Domain 42 Congressional submission deadline (if Path A/A+37) | Submit prepared testimony/comment to DEA hearing (May 28 hearing) | 0% institutional participation; framework credibility diminished | User | 30 min |

### Week 2 — May 14–20 (Monitoring & Prep)

| Project | Milestone | Type | Duration |
|---------|-----------|------|----------|
| **resistance-research** | Domain 42 Wave 1 tracking (open rates, bounces, replies) | Monitoring | 10 min/day |
| **stockbot** | Engine monitoring (normal operation, trades, P&L) | Monitoring | 5 min/2x per day |
| **seedwarden** | Phase 2 prep (finalize landing page, confirm May 30 timeline) | Planning | 30 min/day |
| **mfg-farm** | Test print monitoring (waiting for user execution) | Blocking wait | — |

### Week 3 — May 21–27 (Phase 2 Launch Prep)

| Project | Milestone | Type | User Attention | Owner |
|---------|-----------|------|-----------------|-------|
| **seedwarden** | Final Phase 2 checklist (social accounts, Canva Brand Kit, Kit account) | Pre-launch | 3 x 30 min decision checkpoints | User + Orchestrator |
| **resistance-research** | Domain 42 Wave 2 send (May 24) if Wave 1 response strong | Contingent | 10 min (send approval) | User |
| **stockbot** | May 12 checkpoint outcome analysis + decision (pass/near-miss/far-miss) | Decision | 30 min | User + Orchestrator |
| **resistance-research** | Phase 1 adoption tracking (Day 14 checkpoint) | Monitoring | 20 min | User |

### Week 4 — May 28–30 (Phase 2 Go-Live)

| Date | Project | Milestone | Decision | Impact |
|------|---------|-----------|----------|--------|
| May 28 | resistance-research | Domain 42 congressional deadline (submission window closes) | Monitor Wave 1 results; decide Wave 2 escalation | If strong adoption (5+ ready to testify), accelerate Wave 2 outreach |
| May 30 | **seedwarden** | **Phase 2 go-live** 10:00–10:30 UTC | All user pre-launch gates complete (social, Canva, Kit) | $0 if gates incomplete; 200+ Etsy views if ready |

### Month 2 — June 1–30 (Phase 2 Monitoring + Phase 3 Prep)

| Week | Project | Focus | Type | Attention |
|------|---------|-------|------|-----------|
| June 1–7 | **seedwarden** | Phase 2 Week 1 monitoring (daily email, orders, social engagement) | Operations | 30 min/day |
| June 1–7 | **resistance-research** | Phase 1 Day 30 checkpoint (responses, adoption signals, Phase 2 trigger readiness) | Strategy | 2 hours |
| June 1–7 | **stockbot** | Gate 1 checkpoint outcome + Phase 1 live trading decision (if PASS scenario) | Decision | 2 hours |
| June 8–14 | **seedwarden** | Phase 2 Week 2 decision checkpoint (conversion rate trending, cohort data entry) | Operations | 1 hour |
| June 15–21 | **seedwarden** | **Phase 3 Wave 1 go-live** (June 15, 10:00 UTC) | Launch | 30 min (publish trigger) |
| June 15–30 | **cybersecurity-hardening** | Phase 1 approval + Tier 1 launch prep (if Phase 1 signals ready) | Contingent | TBD |
| June 30 | **seedwarden** | Phase 2 Day 30 checkpoint (conversion data, Phase 3 gate assessment: Herbalist %, revenue) | Decision | 2 hours |

---

## 2. Resource & Attention Map — Weekly User Load

### Baseline User Attention Required (Hours/Week)

| Period | resistance-research | stockbot | seedwarden | cybersecurity | mfg-farm | Total |
|--------|-------------------|----------|------------|---------------|-----------| ------|
| **May 9–13** | **4 hrs** (decision + Wave 1 send) | **1 hr** (DB sync + checkpoint) | 0.5 hr | 0 | 0 | **5.5 hrs** |
| May 14–20 | 0.5 hr (monitoring) | 0.5 hr (monitoring) | 2 hrs (prep) | 0 | 0 | **3 hrs** |
| May 21–27 | 0.5 hr (Wave 2 decision) | 0.5 hr (analysis) | **4 hrs** (pre-launch gates) | 0 | 0 | **5 hrs** |
| May 28–30 | 1 hr (deadline monitoring) | 0 | **2 hrs** (launch day) | 0 | 0 | **3 hrs** |
| **June 1–7** | **2 hrs** (Day 30 checkpoint) | **2 hrs** (Gate 1 decision) | **3.5 hrs** (Week 1 ops) | 0 | 0 | **7.5 hrs** |
| June 8–14 | 0 | 0.5 hr | **2 hrs** (Week 2 decision) | 0 | 0 | **2.5 hrs** |
| June 15–21 | 0 | 0 | **3.5 hrs** (Phase 3 launch + Week 2 ops) | **2 hrs** (Phase 1 approval contingent) | 0 | **5.5 hrs** |
| June 22–30 | 0 | 0 | **2 hrs** (Phase 2 Day 30 checkpoint) | 0 | 0 | **2 hrs** |

**Note**: User loads exclude passive monitoring (checking Discord, email). Decision gates are binary (decide or defer). Launch day operations are 30-60 minute one-time events.

---

## 3. Project Status & Dependencies

### Dependency Graph (What Blocks What)

```
resistance-research Phase 1 Distribution Path Decision (May 9)
  ├─→ Wave 1 send (May 9–10)
  ├─→ Wave 2 send (May 24, contingent on Wave 1 response)
  ├─→ Phase 2 planning (can proceed in parallel)
  └─→ Domain 42 Congressional submission (May 13, contingent on Path A/A+37)

stockbot Gate 1 Checkpoint (May 12)
  ├─→ DB sync (May 11, user action)
  ├─→ Checkpoint query (May 12 20:00 UTC, orchestrator)
  └─→ Gate 1 decision (May 26, user reviews outcome)

seedwarden Phase 2 Launch (May 30)
  ├─→ Social account creation (user action, May 15)
  ├─→ Canva Brand Kit setup (user action, May 20)
  ├─→ Kit automation setup (user action, May 25)
  └─→ Listings publish (orchestrator, May 30 10:00 UTC upon completion)

seedwarden Phase 3 Go-Live (June 15)
  ├─→ Phase 2 launch success (May 30)
  ├─→ Phase 2 Day 16 gate (June 15, min revenue + email signups)
  └─→ Photo shoot + guide production (April–June)

cybersecurity-hardening Phase 1 Approval & Launch (Contingent)
  ├─→ Tier 1 launch decision (user approval)
  ├─→ Phase 1 execution (weeks 1–3, contingent on user approval)
  └─→ Phase 2 institutional outreach (contingent on Phase 1 adoption signals)

mfg-farm Test Print → Revenue Scale (Contingent)
  ├─→ Test print execution (user action, blocking)
  └─→ Product 2-5 launch (post-test-print, contingent)
```

### Critical Path (Sequenced Dependencies)

**Tier 1 Critical Path** (impacts multiple projects):
1. resistance-research: Path decision → May 28 deadline
2. stockbot: DB sync (May 11) → Checkpoint (May 12) → Gate 1 decision (May 26)
3. seedwarden: Social/Canva/Kit setup → May 30 Phase 2 launch → June 15 Phase 3 launch

**Tier 2 Dependent Path** (contingent on Tier 1):
1. cybersecurity-hardening: Phase 1 approval → Tier 1 launch → Phase 1 adoption signals → Phase 2 institutional outreach
2. mfg-farm: Test print (user action) → Product 2 launch (July) → Revenue scale (Q3)

---

## 4. URGENT: May 9–13 User Decision Support

### Decision Tree: Domain 42 Execution vs. Deferral

**Current State**:
- resistance-research Phase 1 complete and ready
- Domain 42 research complete, templates updated, contact list ready
- **Decision deadline: Today (May 9)** — must decide to send Wave 1 by May 9–10 to make May 28 Congressional deadline

**Three Paths Available**:

#### Path A: Minimal Domain 42 Execution (2 orgs, 0–1 week effort)
- **Scope**: Target 2 highest-certainty Domain 42 orgs (DPA + NORML) for Congressional testimony submission
- **Effort**: 10 min Wave 1 send (email template pre-written)
- **Timeline**: May 9–10 send → May 13 (allow 3 days review) → May 28 congressional deadline
- **Expected outcome**: 1–2 organizations file Domain 42 testimony (realistic probability 60–80%)
- **Business value**: Prove Domain 42 impact with concrete institutional action; de-risk larger Phase 2 Domain 42 expansion
- **Risk**: Low (only 2 orgs, high-confidence targets)
- **Decision**: ✅ RECOMMEND IF time-constrained

#### Path A+37: Full Phase 1 + Domain 42 Expansion (10 orgs, 1 week effort)
- **Scope**: Execute Path A (2 orgs) + add 8 more high-probability Domain 42 targets (AG coalitions, immigration legal aid networks, civil rights organizations)
- **Effort**: 30 min Wave 1 send (10 personalized emails)
- **Timeline**: May 9–10 send → May 13 → May 28 congressional deadline
- **Expected outcome**: 5–10 organizations engaged; 2–4 committed to Congressional testimony
- **Business value**: Major Domain 42 legitimacy; framework credibility with institutions; Phase 1 core impact demonstrated
- **Risk**: Medium (requires follow-up management May 13–28; some orgs may not convert)
- **Decision**: ✅ RECOMMEND FOR MAXIMUM IMPACT

#### Path B: Defer Domain 42 to Phase 2 (0 effort now, 2–4 weeks effort July)
- **Scope**: Execute Phase 1 (all 45 base organizations) without Domain 42 Wave 1; include Domain 42 in Phase 2 institutional outreach (July–Aug)
- **Effort**: 10 min May 9–10 send (Phase 1 only)
- **Timeline**: May 9–10 send → May 28 (miss congressional deadline) → July Phase 2
- **Expected outcome**: Phase 1 baseline impact; Domain 42 impact deferred 8+ weeks
- **Business value**: Eliminates May 28 Congressional deadline opportunity; Phase 1 validated before Domain 42 expansion
- **Risk**: Low operational risk; forgoes Domain 42 timing advantage
- **Decision**: ⚠️ RECOMMEND ONLY IF focused on Phase 1 baseline validation first

---

### Decision Matrix: Quick Comparison

| Factor | Path A | Path A+37 | Path B |
|--------|--------|----------|--------|
| **Congressional deadline met?** | ✅ (1–2 orgs) | ✅ (5+ orgs) | ❌ (0 orgs) |
| **User effort** | 10 min | 30 min | 10 min |
| **Expected outcome** | 1–2 testimonies | 5–10 engaged, 2–4 testimonies | 0 testimonies |
| **Phase 1 impact** | 45 orgs + 2 Domain 42 | 45 orgs + 10 Domain 42 | 45 orgs only |
| **Framework legitimacy** | Good | Excellent | Good |
| **Timeline flexibility** | Tight (May 10 send required) | Tight (May 10 send required) | Flexible (May 30 Phase 2) |

**RECOMMENDATION**: **Path A+37** provides maximum framework impact with minimal additional effort (20 min). Congressional testimony from 2–4 organizations by May 28 proves institutional adoption and dramatically increases Phase 1 credibility. May 28 is a unique timing window that won't repeat.

---

## 5. May 12 Checkpoint Scenario Planning

### Stockbot Gate 1 Checkpoint Outcomes & Cascading Decisions

**May 12, 20:00 UTC**: Orchestrator runs checkpoint query (AUTOMATED)

#### Scenario 1: PASS (Sharpe ≥1.0)
- **Probability**: 15–20% (optimistic)
- **What happens**: AAPL time-stop fires → SELL fill recorded → gate passes
- **Immediate action** (May 12–13): User reviews outcome, decides live trading activation
- **Timeline**:
  - May 13–26: Paper trading validation (14 days, verify live behavior matches paper)
  - May 26: Gate 1b checkpoint (confirm readiness)
  - June 1–30: Live trading Phase 1 (micro positions, 2–5 contracts, $20–50K capital)
- **Phase 2** (June 1–30): Multi-ticker expansion if single-ticker validation successful
- **Revenue implication**: $12K–36K annualized (36–108 bp on $670K capital deployed)

#### Scenario 2: NEAR_MISS (Sharpe 0.75–0.99)
- **Probability**: 30–40% (realistic, given signal suppression in April)
- **What happens**: AAPL time-stop fires BUT Sharpe is marginal → gate passes with conditions
- **Immediate action** (May 12–13): Diagnose root cause (signal reweighting vs. regime detection vs. execution friction)
- **Timeline**:
  - May 13–26: Tactical fixes (reweight signals, test HMM regime)
  - May 26: Gate 1b checkpoint (confirm Sharpe improvement to ≥0.95)
  - June 1–30: Live trading Phase 1 if 1b passes; else recovery mode
- **Phase 2** (contingent): Activate only if 1b passes; otherwise defer to June 30 Gate 2
- **Revenue implication**: $6K–18K annualized (18–54 bp) if 1b passes; else technical debt paydown in June

#### Scenario 3: FAR_MISS (Sharpe <0.75)
- **Probability**: 50–55% (realistic given April headwinds)
- **What happens**: Signal underperformance, model disagree, or execution friction → gate fails
- **Immediate action** (May 12–13): Root cause analysis (4-hour investigation)
- **Timeline**:
  - May 13–26: Implement recovery strategy per root cause (e.g., new signal model, regime overlay)
  - May 26: Gate 1b checkpoint (can recovery strategy reach ≥0.75 Sharpe by June 12?)
  - June 1–12: 11-day recovery sprint
  - June 12: Gate 2 formal checkpoint (pass/fail with 4-week retrospective)
  - June 13–30: Live trading Phase 1 if Gate 2 passes; else defer to Q3
- **Phase 2** (deferred): Activate only after successful Gate 2 pass; may slip to July–Aug
- **Revenue implication**: $0 (recovery mode); capital reserved ($670K base) until recovery confirmed

---

## 6. June Checkpoint: Phase 1 Go/No-Go Gates

### June 1 — resistance-research Phase 1 Day 30 Checkpoint

**Metrics**:
- Email open rate: target 20%+ (vs. typical baseline 15–18%)
- Click-through rate: target 5%+
- Adoption signals: count named institutions requesting to integrate framework
- Response rate: target 8–12%

**Decision Gate**:
- **Strong** (>10 adoption signals): Proceed with Phase 2 institutional outreach immediately (Tier 2 launch June 15–20)
- **Moderate** (4–10 adoption signals): Phase 2 prep continues; Tier 2 launch June 25–30
- **Weak** (<4 adoption signals): Pause Phase 2; conduct 2-week retrospective (why low adoption?) → revised Phase 2 strategy → launch July 1

---

### June 15–30 — seedwarden Phase 2 Day 16–30 Checkpoints

**Phase 2 Launch Day 16 Gate** (June 1):
- Minimum: ≥20 orders, ≥50 email signups, ≥1.5% conversion rate
- Strong: ≥50 orders, ≥150 signups, ≥2% conversion rate
- **Outcome**: IF strong → authorize Phase 3 Women's Health guide production start (June 15 go-live confirmed)

**Phase 2 Day 30 Gate** (June 30):
- Herbalist cohort: target ≥8% (3× LTV vs. Gift buyers)
- Revenue: target ≥$600/month
- Repeat customer: target ≥5% second purchase
- **Outcome**: IF healthy (all three metrics pass) → Phase 3 confirmed June 15 launch; IF weak on Herbalist % → pivot Phase 3 focus away from Women's Health → defer to Jan 2027

---

### June 26 — stockbot Gate 1b Checkpoint (Contingent)

**If May 12 Outcome = NEAR_MISS or FAR_MISS**:
- Orchestrator runs final validation on recovery strategy
- **Outcome**:
  - ✅ Recovery successful (Sharpe ≥0.80): authorize live trading Phase 1 start July 1
  - ❌ Recovery unsuccessful: defer live trading to Gate 2 (July 12)

---

## 7. Autonomous Orchestrator Work (What I Handle)

### Pre-Approved Autonomous Actions

- ✅ **May 9–13**: Domain 42 Wave 1 send (upon user path decision)
- ✅ **May 11**: DB sync (if user runs manual command, I can validate)
- ✅ **May 12**: Checkpoint query execution (fully automated)
- ✅ **May 12–13**: Checkpoint outcome classification and decision tree recommendation
- ✅ **May 30**: seedwarden Phase 2 publish (upon user pre-launch gates completion)
- ✅ **June 1**: Phase 1 Day 30 checkpoint analysis (automated metrics)
- ✅ **June 15**: seedwarden Phase 3 Wave 1 publish (upon user pre-launch gates completion)

### What Requires User Decision

- ❌ **May 9**: Domain 42 path choice (Path A / A+37 / B)
- ❌ **May 13**: Congressional submission approval (if Path A/A+37)
- ❌ **May 12–13**: Gate 1 outcome review and Phase 1 live trading decision
- ❌ **May 15**: Social account creation for seedwarden Phase 2
- ❌ **May 20**: Canva Brand Kit setup
- ❌ **May 25**: Kit email automation final approval
- ❌ **June 1**: Phase 1 adoption signal review (resistance-research)
- ❌ **June 15**: Phase 3 Women's Health guide decision (contingent on Phase 2 Herbalist cohort %)
- ❌ **June 30**: Phase 3 full launch decision or pivot

---

## 8. Contingency Paths

### If Stockbot May 12 Fails (FAR_MISS Scenario)

**Best-case recovery path** (realistic if root cause is fixable):
- May 13–26: Implement recovery (e.g., new signal model)
- May 26: 11-day recovery validation
- June 9: Gate 1b checkpoint (can recovery reach ≥0.75 by June 12?)
- June 12: Gate 2 formal review
- **Latest go-live**: July 1 (if recovery successful)

**Worst-case path** (if root cause unfixable):
- May 13–26: Root cause analysis identifies systemic issue (model fundamentally broken)
- May 26: Decision to defer live trading to Q3 2026
- June 1–30: Technical debt paydown (refactor signal architecture)
- July: Gate 2 checkpoint with new signal design
- **Latest go-live**: August 1 (restart from fresh architecture)

### If seedwarden Phase 2 Underperforms (Conversion <1%)

**Pivot path 1: Price adjustment** (may recover with lower pricing or bundling)
- June 5–14: A/B test lower price point ($12–15 bundles vs. $18–22)
- June 15–20: Measure conversion response
- June 21: Decide whether to stick with lower price or revert

**Pivot path 2: Audience shift** (emphasize Prepper/Homesteader over Gift)
- June 5–14: Refocus marketing to conservation/self-sufficiency messaging
- June 15–20: Measure cohort shift
- June 21: Phase 3 Women's Health decision based on new cohort makeup

**Pivot path 3: Defer Phase 3** (wait for Phase 2 stabilization)
- June 30: If Phase 2 revenue <$400/month, defer Women's Health launch to January 2027
- August–December: Focus on Phase 2 optimization + other projects

---

## 9. Resource Conflict Assessment

### No Resource Conflicts Identified (May 9 – June 30)

- **Reason**: Projects have independent critical paths with non-overlapping deadlines
- **Domain 42 (May 28)**: resistance-research only
- **Stockbot Checkpoint (May 12)**: stockbot only (10-minute orchestrator task)
- **seedwarden Phase 2 (May 30)**: seedwarden only (user 2–4 hours pre-launch gates)
- **seedwarden Phase 3 (June 15)**: seedwarden only (depends on Phase 2 success, not other projects)
- **cybersecurity-hardening (June 15)**: contingent on Phase 1 adoption, independent execution

**Peak simultaneous user attention**: June 1–7 (seedwarden Phase 2 Week 1 ops + resistance-research Day 30 checkpoint + stockbot outcome review) = 7–8 hours total over week, or ~1 hour/day

---

## 10. Quick Reference: Executive Decision Checklist

### By May 9 EOD (This Afternoon)

- [ ] **Decide Domain 42 path**: Path A (2 orgs) / Path A+37 (10 orgs) / Path B (defer)
  - **Recommendation**: Path A+37 (best impact/effort ratio)
  - **Time required to decide**: 15 min
  - **Deadline**: 23:59 UTC today (decisions at 00:00 UTC May 10 are valid; May 11+ is too late for May 28)

### By May 11 EOD

- [ ] **Execute stockbot DB sync** (if not done earlier)
  - Command: `uv run python scripts/sync_db_from_alpaca.py --since 2026-04-29 --db database/trading.db`
  - Time required: 5 min
  - Deadline: Before May 12 20:00 UTC checkpoint

### By May 12 20:00 UTC

- Orchestrator executes checkpoint (no user action required)

### By May 26

- [ ] **Review Gate 1 outcome** (if May 12 outcome = NEAR_MISS or FAR_MISS)
  - Time required: 30 min
  - Decision: Proceed with recovery sprint or defer live trading?

### By May 30

- [ ] **seedwarden Phase 2 pre-launch gates**: Social account creation, Canva Brand Kit, Kit automation
  - Time required: 3 × 30 min = 1.5 hours
  - Deadline: 08:00 UTC May 30 (2 hours before 10:00 launch)

### By June 1

- Orchestrator analyzes Phase 1 Day 30 checkpoint (no user action until results ready)

### By June 15

- [ ] **seedwarden Phase 3 Women's Health decision** (based on Phase 2 Herbalist cohort %)
  - Time required: 15 min decision
  - Deadline: 09:00 UTC June 15 (1 hour before Phase 3 launch)

### By June 30

- [ ] **Phase 2 Day 30 checkpoint review** (revenue, repeat customer %, Herbalist %)
  - Time required: 2 hours analysis + decision
  - Decision: Continue Women's Health Phase 3 or pivot to Prepper/Homesteader focus?

---

**Document Generated**: May 9, 2026, 10:51 UTC  
**Next Review**: May 10, 2026 (after Domain 42 path decision)  
**Automated Checkpoint**: May 12 20:00 UTC (stockbot Gate 1 checkpoint query executed)

