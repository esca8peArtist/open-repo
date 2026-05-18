---
title: "Cross-Project Interdependency Risk Assessment — May 19–31, 2026"
created: 2026-05-18
status: production-ready
scope: "Five converging project events across three high-priority projects. Maps conflicts, sequences, contingency trees, and decision priority for single-user execution May 19–31."
projects: [stockbot, resistance-research, seedwarden, cybersecurity-hardening, mfg-farm]
audience: "User (thorn) — scheduling reference for May 19–31 window"
word_count: ~3200
---

# Cross-Project Interdependency Risk Assessment
## May 19–31, 2026 Coordination Window

**Purpose**: Five major project events converge in 13 days. This document maps every conflict, provides sequencing guidance for three scenarios, and gives you contingency trees so that any single surprise event does not cascade into a project pile-up.

**How to use this document**: Read Section 1 first. If you are in a time crunch, jump directly to the scenario that matches your current situation (Section 2), then go to the relevant contingency tree (Section 3) if an outcome deviates from expectations. Section 4 gives the decision sequencing rules. Section 5 is the priority matrix when two decisions arrive at the same time.

**Confidence**: High. All timings sourced from live project state: ORCHESTRATOR_STATE.md (May 18 10:52 UTC), PROJECTS.md, TRACK_B_GATE_COMPLETION_VERIFICATION.md (seedwarden, May 15), and may19_checkpoint_analysis.py (stockbot, May 17).

---

## Section 1: Timeline Conflict Matrix

**Events in scope**:

| ID | Event | Project | Window | Duration | Owner |
|----|-------|---------|--------|----------|-------|
| E1 | May 19 checkpoint execution | stockbot | May 19 20:00–21:30 UTC | 1.5 hr | User + script |
| E2 | Post-checkpoint decision logging + Gate 2 option selection | stockbot | May 20 06:00–18:00 UTC | ~3 hr scattered | User |
| E3 | Wave 1 72h monitoring close + early Phase 2 signal read | resistance-research | May 21 10:32 UTC (72h after send) | Passive; decision gate if STRONG | Orchestrator |
| E4 | Phase 2 path decision gate | resistance-research | May 21–22 (early read); formal: May 25–28 | 30–60 min user decision | User |
| E5 | Seedwarden Gate 2: Canva Brand Kit setup | seedwarden | May 19–24 (deadline May 24) | ~25 min user | User |
| E6 | Seedwarden Gate 3: Kit email account setup | seedwarden | May 26–28 (deadline May 28) | ~20 min user | User |
| E7 | mfg-farm test print execution + evaluation | mfg-farm | TBD; user action any time May 19–27 | 3–4 hr (print + evaluation) | User |
| E8 | Etsy launch window (if test print approved) | mfg-farm | Within 5 days of print approval; 3–4 hr | 3–4 hr | User |
| E9 | Cybersecurity: VeraCrypt restart + Phase 1 resumption | cybersecurity | Async — user Windows restart whenever convenient | 5 min restart + 2 hr Phase 1 walkthrough | User |

---

### Conflict Pair Analysis

**Legend**: HC = Hard Conflict (cannot run in parallel, same active-focus window); SEQ = Sequential window available (events are on different days or have a natural gap); NC = No Conflict (async, different days, or passive).

| Pair | Conflict Type | Analysis |
|------|--------------|---------|
| E1 + E2 (checkpoint + post-checkpoint) | SEQ | E1 ends 21:30 UTC May 19. E2 starts May 20 morning. Natural 8.5-hour gap. No forced overnight work. |
| E1 + E5 (checkpoint + Canva Gate 2) | NC | Gate 2 window is May 19–24. Canva work is async and can happen any time May 20–23. Do not schedule Canva work on May 19 evening. Reserve that window for checkpoint only. |
| E1 + E7 (checkpoint + test print start) | HC — if test print launches same evening | If user starts a 3D print job at 19:00 UTC May 19 (before checkpoint), the print runs in background during checkpoint (acceptable). If user expects to supervise the print actively during 20:00–21:30 UTC, that is a hard conflict with checkpoint attention. Recommendation: start print no later than 18:00 UTC so it runs unattended during checkpoint, OR defer print to May 20. |
| E2 + E8 (post-checkpoint + Etsy launch) | HC — May 20 only | If test print is approved May 19 and Etsy launch is attempted May 20, both E2 and E8 fall on May 20. Combined demand: ~6–7 hours on a single day. This is the primary compression risk. See Scenario C and Contingency Tree 2 for resolution. |
| E3 + E4 (Wave 1 close + Phase 2 decision) | SEQ | E3 closes at 10:32 UTC May 21. E4 early-read decision can happen same afternoon. These are complementary, not conflicting — E3 produces the data E4 needs. |
| E4 + E5 (Phase 2 decision + Canva Gate 2) | NC | Phase 2 decision (May 21–22) and Canva Gate 2 (May 19–24 window) overlap in calendar days but require different cognitive modes (strategic decision vs. UI task). If user is making the Phase 2 decision May 21–22, defer Canva work to May 22–23 to avoid decision fatigue on the same day. |
| E4 + E6 (Phase 2 decision + Kit Gate 3) | NC | 6-day gap minimum. Phase 2 decision by May 22 (early) or May 25–28 (formal). Gate 3 starts May 26. No parallelism required. |
| E5 + E6 (Canva Gate 2 + Kit Gate 3) | SEQ | Gate 2 must complete before Gate 3 begins (Kit landing page requires Canva-designed assets). Verified per TRACK_B_GATE_COMPLETION_VERIFICATION.md dependency matrix. This is planned sequencing, not a conflict. |
| E7 + E8 (test print + Etsy launch) | SEQ | E8 starts within 5 days of E7 pass. If E7 executes May 19–20, E8 window opens May 20–25. If E7 executes May 25–26, E8 window opens May 26–31. No parallelism required — they are sequential by design. |
| E8 + E3/E4 (Etsy launch + Phase 2 decision) | NC — unless test print approved May 19–20 | If Etsy launch falls May 20–21 and Phase 2 decision falls May 21–22, user faces two context switches in 48 hours. These are independent projects with no data dependency. Can be sequenced: Etsy launch May 20 → Phase 2 decision May 22. |
| E9 + any (VeraCrypt + all others) | NC | VeraCrypt restart is a 5-minute action on a Windows machine. It does not conflict with any other event. Phase 1 walkthrough (steps 1.4–1.7, ~2 hrs) can happen any day May 19–31 with no dependency on other projects. Lowest-priority scheduling item in this window. |

---

### Critical Zone Summary

Three calendar zones carry the highest conflict risk:

**Zone 1: May 19 (checkpoint day)**
Events present: E1 (mandatory 20:00 UTC), E5 (first day of Gate 2 window), E7 (optional test print start).
Rule: Reserve 19:00–22:00 UTC for E1 only. Do not start new tasks after 18:00 UTC.

**Zone 2: May 20 (post-checkpoint + potential Etsy)**
Events present: E2 (post-checkpoint logging, ~3 hrs), E8 (if test print approved May 19, Etsy launch window opens).
Rule: If Etsy launch is needed May 20, sequence it before E2 afternoon work. See Scenario B for exact times.

**Zone 3: May 21–22 (Wave 1 close + Phase 2 decision)**
Events present: E3 (72h monitoring close 10:32 UTC May 21), E4 (Phase 2 early-read decision), E5 (Gate 2 still open).
Rule: May 21 morning is for reading Wave 1 signals. Phase 2 decision by May 22 if signals are clear. Defer Canva (Gate 2) to May 22–23 to avoid cognitive overload May 21.

---

## Section 2: Resource Allocation Scenarios

### Scenario A: Ideal — Test Print Approved May 25+

**Conditions**: User defers test print execution until May 25 or later. No mfg-farm activity in the May 19–24 window.

**Why this is ideal**: Removes the compression risk from Zone 2 entirely. Stockbot checkpoint May 19, post-checkpoint planning May 20, Phase 2 decision May 21–22, and Seedwarden Gate 2 May 20–24 all proceed without mfg-farm interference. Etsy launch window opens May 26–31 — after all resistance-research and stockbot decisions are resolved.

**Optimal sequencing**:

| Day | Primary Focus | Est. User Hours | Notes |
|-----|--------------|-----------------|-------|
| May 19 | Stockbot checkpoint (E1) | 1.5 hr (20:00–21:30 UTC) | Reserve evening; all other tasks done by 18:00 UTC |
| May 20 | Post-checkpoint logging (E2) + Canva Gate 2 start (E5) | 3 + 1 = 4 hr | E2 in morning; Canva afternoon or evening |
| May 21 | Wave 1 close (E3) + Phase 2 early read (E4) | 1 hr | Passive monitoring to ~noon; decision call afternoon |
| May 22 | Canva Gate 2 completion (E5) | 1 hr | If not finished May 20; no other competing tasks |
| May 23–24 | Gate 2 verification (E5) | 0.5 hr | Check Canva brand kit exports per checklist |
| May 25 | Test print execution (E7) | 3–4 hr (print + evaluation) | Completely clear of all other active gates |
| May 25–28 | Formal Phase 2 adoption assessment (E4) | 30–60 min | Orchestrator synthesizes; user reviews and decides |
| May 26–28 | Kit Gate 3 setup (E6) | ~20 min | After Gate 2 verified complete |
| May 26–31 | Etsy launch (E8) | 3–4 hr | After print approval; no competing gates |
| May 29 | Seedwarden go/no-go decision (20:00 UTC) | 30 min | All gates verified per checklist |
| May 30 | Seedwarden launch (09:00 UTC) | 30 min | |
| Anytime | VeraCrypt restart + Phase 1 resumption (E9) | 5 min + 2 hr | No dependency on any other event |

**Risk**: Near-zero. Only failure mode is if test print produces a design defect that requires redesign — but that is an mfg-farm-internal issue and does not affect any other project timeline.

**Total peak-day user hours**: 4 hours (May 20). All other days under 2 hours.

---

### Scenario B: Realistic — Test Print Approved May 19–20

**Conditions**: User executes test print during the day on May 19 (print starts ~14:00–16:00 UTC, completes overnight), evaluates and approves May 20 morning, and wants Etsy launch May 20.

**Key constraint**: Stockbot checkpoint is May 19 20:00–21:30 UTC. Test print can run in background during checkpoint if started by 18:00 UTC. Print evaluation happens May 20 morning before post-checkpoint work.

**Optimal sequencing**:

| Time | Action | Notes |
|------|--------|-------|
| May 19 12:00–16:00 UTC | Start test print (3–4 hr print job) | Print runs unattended |
| May 19 16:00–19:30 UTC | Free window (print running) | Do Canva Gate 2 work during this window (~1 hr) |
| May 19 19:30–20:00 UTC | Pre-checkpoint prep | Review checkpoint script, confirm Jetson SSH accessible |
| May 19 20:00–21:30 UTC | Checkpoint execution (E1) | Print still running in background — acceptable |
| May 19 21:30–23:00 UTC | Print monitoring / wind down | Check print progress; no new decisions needed |
| May 20 06:00–08:00 UTC | Evaluate test print (E7) | Pass/fail decision on snap-arm clearance |
| May 20 08:00–11:00 UTC | If approved: Etsy launch (E8) | 3-hour window; compressed but doable per checklist |
| May 20 11:00–14:00 UTC | Buffer / break | Do not start post-checkpoint work until afternoon |
| May 20 14:00–17:00 UTC | Post-checkpoint logging + Gate 2 option selection (E2) | 3 hr scattered; no conflict with completed Etsy work |
| May 21 | Wave 1 close (E3) + Phase 2 early read (E4) | 1 hr as in Scenario A |
| May 22–24 | Canva Gate 2 completion (E5) | Resume from where left off on May 19 |

**Risk**: Moderate. The May 20 morning window (Etsy launch 08:00–11:00 UTC) is compressed. The Etsy launch checklist is 648 lines with sequential steps — if any step hits a platform issue (Etsy listing approval delay, photo upload error), it bleeds into the post-checkpoint afternoon window. Mitigation: do not start Etsy listing upload until print evaluation is definitively PASS (not conditional). If evaluation takes until 09:00 UTC, compress Etsy launch to 09:00–12:00 UTC and push post-checkpoint work to 13:00–16:00 UTC.

**Total peak-day user hours (May 20)**: 6–7 hours. Feasible but represents the limit of sustainable single-day load.

---

### Scenario C: Compression — Test Print Approved May 20 + Phase 2 Decision May 21 + Gate 2 Active

**Conditions**: Test print is not evaluated until May 20 afternoon (print ran overnight May 19, evaluation delayed by checkpoint fatigue). Etsy launch now competes with post-checkpoint work May 20, and Phase 2 decision falls May 21. Gate 2 (Canva, due May 24) still pending.

**This is the highest-risk scenario.** Three project contexts switch within 48 hours.

**Recommended resolution — strict sequential sequencing**:

| Step | Time | Action | Why this order |
|------|------|--------|----------------|
| 1 | May 19 20:00–21:30 UTC | Checkpoint execution (E1) | Non-negotiable; has fixed UTC time |
| 2 | May 20 06:00–09:00 UTC | Test print evaluation (E7) | Do this first; binary pass/fail; <30 min |
| 3 | May 20 09:00–12:00 UTC | Etsy launch (E8), IF print passed | Accomplish while energy is high; independent of stockbot |
| 4 | May 20 13:00–16:00 UTC | Post-checkpoint logging (E2) | Stockbot Gate 2 option selection; ~3 hrs |
| 5 | May 21–22 | Phase 2 decision (E4) | After Wave 1 closes 10:32 UTC May 21; decision by May 22 |
| 6 | May 22–24 | Gate 2 Canva (E5) | Lowest urgency of remaining items; still within deadline |

**What not to attempt**: Do not interleave Etsy launch steps with post-checkpoint logging on May 20. These require different cognitive modes (creative listing vs. data analysis). Completing each task before starting the next is faster than context-switching.

**If May 20 runs long (Etsy issues bleed past 12:00 UTC)**: Push post-checkpoint logging to May 21 morning (before Wave 1 close). The Gate 2 option selection for stockbot is documentation, not real-time execution — a one-day slip has no downstream consequence.

**If Phase 2 decision is WEAK**: See Contingency Tree 3. This actually frees up user time by reducing the urgency of Phase 2 preparation work.

---

## Section 3: Contingency Decision Trees

### Tree 1: FAR-MISS C2 Checkpoint Outcome (Worst Case)

**Trigger**: Checkpoint script exits code 2 (May 19 21:30 UTC). AAPL model has generated 0 sells since Lever A deployment on May 16. Infrastructure failure or signal generation failure confirmed.

**Immediate consequence**: Orchestrator initiates emergency stockbot diagnosis protocol. Estimated user-facing work: 4–6 hours over May 20–21 (log review, config investigation, option assessment).

**Downstream question 1: Does this delay the Phase 2 decision (E4)?**
No. Phase 2 decision is based on Wave 1 engagement data (email opens, Gist clicks, replies) — not stockbot state. These are entirely independent. Phase 2 can proceed on its normal timeline (May 21–22 early read, May 25–28 formal assessment) regardless of stockbot condition.

**Downstream question 2: Does FAR-MISS affect user attention for other projects?**
Yes. If user is troubleshooting stockbot May 20–21, cognitive bandwidth is split. Recommendation:
- Defer test print evaluation to May 21 (if print ran overnight May 19, the parts can sit until May 21 without issue)
- Defer Etsy launch (E8) to May 22–25 (no data loss; Etsy platform is open all week)
- Proceed with Gate 2 Canva work May 22–24 as planned (it is UI work, not decision-making, and provides mental context-switching relief from stockbot diagnosis)
- Do NOT defer Phase 2 decision — it is independent and should proceed on schedule

**Sequencing under FAR-MISS**:

| Day | Focus | Notes |
|-----|-------|-------|
| May 19 21:30 UTC | Confirm FAR-MISS outcome | Log result; do not attempt diagnosis tonight |
| May 20 | Emergency stockbot diagnosis (4–6 hrs) | Priority 1; defer all non-critical items |
| May 21 morning | Complete diagnosis + Wave 1 close (E3) | These can run in parallel (monitoring is passive) |
| May 21 afternoon | Phase 2 early-read decision (E4) | Independent of stockbot |
| May 22–24 | Gate 2 Canva (E5) | Proceed on schedule |
| May 22–25 | Test print + Etsy launch (E7, E8) | Deferred from May 20; no deadline pressure |

---

### Tree 2: Test Print Approved May 19–20 AND Checkpoint FAR-MISS

**Trigger**: Both the worst-case stockbot outcome AND early mfg-farm approval land on the same 24-hour window.

**This is the dual-pressure scenario.** User has: (a) a failed stockbot requiring urgent diagnosis, (b) an approved test print requiring an Etsy launch that has time value (launching sooner captures more of a weekly Etsy traffic cycle).

**Decision rule**: Stockbot diagnosis takes priority over Etsy launch. The Etsy launch window is flexible (May 20–27); stockbot diagnostic work is time-sensitive because the next checkpoint is not scheduled until after diagnosis is complete — delay compounds.

**Recommended sequencing**:

| Time | Action | Rationale |
|------|--------|-----------|
| May 19 20:00–21:30 UTC | Checkpoint execution | Fixed time |
| May 19 21:30–22:00 UTC | Confirm FAR-MISS; do not begin diagnosis | Rest; diagnosis at 09:00 UTC tomorrow |
| May 20 06:00–08:00 UTC | Evaluate test print (E7) | Binary, fast (<30 min) — do this first to clear the decision |
| May 20 08:00–09:00 UTC | If print approved: stage Etsy listing (do not publish yet) | Draft listing, upload photos — but do not click Publish |
| May 20 09:00–15:00 UTC | Stockbot FAR-MISS diagnosis (6 hrs) | Priority; full focus |
| May 20 15:00–18:00 UTC | Post-checkpoint logging (E2) | ~3 hrs; can overlap with diagnosis wrap-up |
| May 21 | Publish Etsy listing (E8) | 1-day slip from ideal; no material impact on listing performance |

**Why stage but not publish Etsy on May 20 morning**: Staging the listing (photos, title, description, pricing) takes ~1.5 hours and can happen while stockbot is still pending. Publishing takes ~15 minutes and should wait until diagnosis is resolved — if stockbot requires a config change that demands user restart or monitoring, having an active Etsy launch competing for attention is a risk.

---

### Tree 3: Wave 1 WEAK Outcome + Gate 2 (Canva) Both Active May 21–24

**Trigger**: Wave 1 72h engagement scoring is WEAK (<30% reply rate, low Gist views) at close on May 21. Per the monitoring framework, WEAK outcome means: hold distribution, revise messaging before Batch 2, Phase 2 timeline shifts to August.

**Question 1: Does WEAK outcome cancel Phase 2 research June 1 launch?**
Yes, for the aggressive timeline. If WEAK, Phase 2 production (Domains 56–59 research execution, Items 61–62 in Exploration Queue) shifts from June 1 to an August window pending amplification strategy revision. This is documented in the Wave 1 monitoring framework.

**Question 2: Does WEAK outcome free up user time?**
Yes. Materially. A WEAK outcome means the Phase 2 preparation work that was planned for May 25–June 1 (briefing orchestrator, selecting research path, staging distribution infrastructure) no longer has an urgent deadline. This frees approximately 4–6 hours of user decision-making time that would have been spent on Phase 2 path selection.

**Consequence for Gate 2 (Canva)**: The freed time can be used to complete Canva Brand Kit work (E5) more thoroughly — including zone card template creation that would otherwise be a CONDITIONAL on launch day. If WEAK outcome is confirmed May 21, redirect the ~2 hours saved from resistance-research decision-making to completing Gate 2 fully by May 23 instead of May 24.

**Recommended action under WEAK**:

| Date | Action |
|------|--------|
| May 21 afternoon | Confirm WEAK outcome with orchestrator; note August revised timeline |
| May 21–23 | Redirect saved time to Gate 2 Canva completion |
| May 22–24 | Gate 2 verification per TRACK_B_GATE_COMPLETION_VERIFICATION.md |
| May 25–28 | Formal adoption assessment (still runs on schedule — even WEAK outcomes get a 14-day adoption window per framework) |
| August | Phase 2 research re-evaluation once amplification strategy is revised |

---

### Tree 4: Dual Decision Gate — Phase 2 Formal Assessment (May 25–28) AND Gate 3 Kit Setup (May 26–28)

**Trigger**: Phase 2 formal adoption assessment window (May 25–28) overlaps with Seedwarden Gate 3 execution window (May 26–28). Both require user attention.

**Question: Do these conflict?**
No forced parallelism. They are compatible because:
- Phase 2 formal assessment is primarily orchestrator-generated synthesis (reading a 1–2 page summary); user decision time is 30–60 minutes total
- Gate 3 (Kit account + landing page + email sequence + 3-test protocol) is ~20 minutes of UI work + 35 minutes of verification testing

Total combined demand May 26–28: approximately 2 hours across 3 days. This is within normal daily load.

**Recommended daily distribution**:

| Date | Action | Duration |
|------|--------|---------|
| May 25 | Read Phase 2 adoption assessment (orchestrator-prepared) | 20–30 min |
| May 26 | Gate 3 Kit account creation + email sequence draft | 1 hr |
| May 27 | Make Phase 2 path decision (STRONG / MODERATE / WEAK confirmed) | 30 min |
| May 27–28 | Gate 3 landing page + 3-test protocol | 35 min |
| May 28 | Gate 3 finalization; update social bios with Kit URL | 15 min |
| May 29 | Seedwarden go/no-go decision (20:00 UTC) | 30 min |

These are sequential with no dependency between them. The only failure mode is if Gate 3 test protocol reveals a Kit email delivery issue on May 28 that requires Kit support response (48-hour propagation time for SPF/DKIM). If this occurs, initiate Kit support ticket May 28 immediately — it will resolve before May 30 launch regardless of Phase 2 decision timing.

---

## Section 4: Communication Protocol

The following rules govern decision sequencing across all five projects for May 19–31.

**Rule 1: Checkpoint outcome (May 19 20:00 UTC) is the highest-priority decision input.**
All downstream stockbot decisions (Gate 2 option selection, resource allocation, next checkpoint scheduling) depend on the May 19 outcome. Do not make stockbot configuration changes between May 16 and May 19 — the checkpoint script reads the live config. Post-checkpoint, the outcome classification (PASS / STILL_MISS_B2 / FAR_MISS) determines whether May 20 is normal or emergency mode.

**Rule 2: Phase 2 path decision (formal May 25–28, early May 21–22 if STRONG) must be final before June 1 research production starts.**
The Exploration Queue Items 61–62 are staged for activation on May 21 (Wave 1 synthesis) and May 25+ (Phase 2 production scaffolding). These cannot begin until the STRONG/MODERATE/WEAK classification is confirmed. User's role: review the orchestrator-prepared synthesis document and select the path. This is a 30–60 minute decision, not an extended analysis session.

**Rule 3: Test print approval (E7) is independent of all other projects.**
Executing the test print and evaluating the snap-arm clearance has zero dependency on stockbot checkpoint outcome, Phase 2 decision, or Seedwarden gates. The only scheduling constraint is user time. If delayed past May 27, the Etsy launch slips to June 2 instead of May 28 — this is acceptable and has no effect on any other project.

**Rule 4: Seedwarden gates (E5, E6) are user-action checklist items, not critical-path gates for other projects.**
Gate 2 (Canva Brand Kit, due May 24) and Gate 3 (Kit email, due May 28) are self-contained. They can be completed in parallel with any other project activity. If user is stretched by FAR-MISS diagnosis or Phase 2 decision work, both gates can extend 2–3 days without jeopardizing the May 30 launch:
- Gate 2 can extend to May 26 (Canva Brand Kit can be done in 25 min once started)
- Gate 3 can extend to May 29 morning (the verification checklist allows a 4-hour remediation window before launch)

Gate 2 hard limit: May 26 (Gate 3 cannot begin until Gate 2 is complete per dependency matrix).
Gate 3 hard limit: May 29 morning (must leave remediation window before May 30 09:00 UTC launch).

**Rule 5: Cybersecurity VeraCrypt restart (E9) depends solely on user choosing to restart their Windows machine.**
There is no external deadline, no dependency on other projects, and no scheduling constraint. Steps 1.4–1.7 (Ente Auth, Bitwarden, data broker opt-outs, iPhone passcode — approximately 2 hours) can happen any day May 19–31. Recommended: schedule during a day with no active decision gates (e.g., May 23 after Gate 2 is done, or May 28 after Gate 3 setup).

---

### Decision Dependency Matrix

| If event A happens before event B... | Constraint that applies |
|--------------------------------------|------------------------|
| Checkpoint PASS before post-checkpoint logging | Normal May 20 workflow; Gate 2 option = continue Lever A monitoring |
| Checkpoint STILL_MISS_B2 before post-checkpoint | Lever B activation decision required May 20; adds ~1 hr to post-checkpoint work |
| Checkpoint FAR_MISS before any May 20 activity | Emergency mode: defer all non-critical May 20 tasks; diagnosis first |
| Test print PASS before Etsy launch | Launch proceeds; follow etsy-listing-launch-checklist.md |
| Test print FAIL before Etsy launch | Redesign required; Etsy launch deferred 1–2 weeks; no impact on any other project |
| Wave 1 STRONG signal before Phase 2 decision | Phase 2 can be triggered early (May 21–22); accelerate Items 61–62 |
| Wave 1 MODERATE before Phase 2 decision | Batch 2 schedules May 21; Phase 2 decision May 25–28 as planned |
| Wave 1 WEAK before Phase 2 decision | August revised timeline; freed capacity redirected to Gate 2 completion |
| Gate 2 complete before Gate 3 | Normal sequencing; Gate 3 can proceed |
| Gate 2 not complete by May 26 | Gate 3 landing page publication blocked; slip Gate 3 to May 28–29 and use 4-hour remediation window |
| Phase 2 decision before Seedwarden launch | No constraint; independent projects |
| FAR-MISS + test print approval same day | Use Tree 2 sequencing: diagnosis first, Etsy staging parallel, Etsy publish next day |

---

## Section 5: Escalation Contact and Priority Matrix

### Priority Ranking for Simultaneous Decisions

When two or more decisions arrive in the same window, use this ranking without exception:

| Priority | Event | Rationale | Flexibility |
|----------|-------|-----------|-------------|
| 1 | Stockbot checkpoint (May 19 20:00 UTC) | Non-repeatable 1.5-hour window; script must be run at this UTC time; missed checkpoint = 3-week delay to next evaluation cycle | Zero — fixed UTC time |
| 2 | Phase 2 path decision (May 21–25) | Non-repeatable once Wave 1 window closes; delay past May 28 delays June 1 research production by 4–8 weeks | Low — 7-day window; early read possible if STRONG |
| 3 | Test print approval + Etsy launch (flexible May 20–27) | Revenue-generating but date-flexible; Etsy platform available all week; 1-week slip costs ~$0 in most cases | High — any day May 20–27 with no deadline consequence |
| 4 | Seedwarden Gate 2 Canva (due May 24, extendable to May 26) | Hard limit May 26 (Gate 3 depends on it); UI task requiring <1 hour of active attention; high flexibility within window | Moderate — 2-day buffer before Gate 3 blocks |
| 5 | Seedwarden Gate 3 Kit (due May 28, extendable to May 29 morning) | Hard limit May 29 morning for remediation window; UI task ~20 min + 35 min verification | Moderate — 1-day buffer before no-go decision |
| 6 | Cybersecurity VeraCrypt restart + Phase 1 walkthrough | No external deadline; purely user convenience; 5-min restart any time | Maximum — any day May 19–31 |

---

### Simultaneous Decision Scenarios

| Scenario | Decision Rule |
|----------|--------------|
| Checkpoint outcome arrives AND test print needs evaluation same morning | Checkpoint outcome first (it is already decided — just read the result); print evaluation second (30 min); then sequence day per Tree 2 |
| Phase 2 decision needed AND Gate 2 Canva pending on same day | Phase 2 decision first (cognitive priority, 30–60 min); Gate 2 Canva second (UI task, 25 min); both completable same day |
| Etsy launch window AND post-checkpoint work both fall May 20 | Etsy launch first (morning, 3–4 hr); post-checkpoint logging second (afternoon, ~3 hr); see Scenario B |
| Phase 2 WEAK confirmation AND Gate 3 Kit setup due same week | Gate 3 first (has a hard deadline May 29 morning); Phase 2 WEAK confirmation is a 20-min read; no conflict |
| FAR-MISS AND Gate 2 Canva window overlapping May 20–21 | FAR-MISS diagnosis first (May 20); Gate 2 Canva deferred to May 22–24 (still within deadline) |

---

### Escalation Triggers

**Escalate to Priority 1 (drop all other work)** when:
- Checkpoint script returns FAR_MISS (exit code 2)
- Kit email 3-test protocol fails within 4 hours of May 30 launch

**Escalate to Priority 2 (schedule dedicated session, same day)**:
- Wave 1 produces STRONG signals before 72h close (early Phase 2 trigger)
- Test print snap-arm evaluation produces FAIL (redesign decision needed)
- Gate 3 SPF/DKIM verification fails (Kit support ticket needed immediately)

**Defer to next available day**:
- Canva Brand Kit export issues (recoverable in 30–45 min; not blocking same-day)
- Post-checkpoint logging slip (1-day slip has no downstream consequence)
- VeraCrypt Phase 1 resumption (no deadline)

---

## Appendix: At-a-Glance Calendar for May 19–31

This is a clean daily reference. Times are UTC unless noted.

| Date | Must-Do (hard constraint) | Should-Do (flexible) | User Hours |
|------|--------------------------|---------------------|------------|
| May 19 | Checkpoint 20:00–21:30 UTC (E1) | Test print start by 18:00 if desired (E7); Canva start (E5) | 1.5–2.5 hr |
| May 20 | Post-checkpoint logging (E2) 06:00–17:00 UTC | Etsy launch if print approved (E8); Canva Gate 2 (E5) | 3–7 hr (scenario-dependent) |
| May 21 | Wave 1 close review at 10:32 UTC (E3) | Phase 2 early read (E4) if STRONG; Canva Gate 2 (E5) | 1–2 hr |
| May 22 | Phase 2 decision if early trigger (E4) | Gate 2 Canva completion (E5) | 1–2 hr |
| May 23 | — | Gate 2 verification; VeraCrypt (E9) | 0.5–2 hr |
| May 24 | Gate 2 hard deadline (E5) | — | 0.5 hr |
| May 25 | — | Test print if deferred (E7); Phase 2 formal assessment begins | 1–4 hr |
| May 26 | Gate 3 start (E6) | Phase 2 decision review | 1 hr |
| May 27 | — | Phase 2 path decision final (E4); Gate 3 landing page (E6) | 1 hr |
| May 28 | Gate 3 hard deadline (E6) | Etsy launch if deferred (E8); VeraCrypt Phase 1 (E9) | 1–4 hr |
| May 29 | Seedwarden go/no-go decision 20:00 UTC | — | 0.5 hr |
| May 30 | Seedwarden launch 09:00 UTC | — | 0.5 hr |
| May 31 | — | Catch-up for any deferred items | TBD |

**Total estimated user hours May 19–31**: 14–28 hours depending on scenario (Scenario A: ~14 hr; Scenario B: ~20 hr; Scenario C with FAR-MISS: ~26–28 hr). All scenarios are feasible for a single user over 13 days.

---

*Created: 2026-05-18. Source data: ORCHESTRATOR_STATE.md (10:52 UTC May 18), PROJECTS.md, TRACK_B_GATE_COMPLETION_VERIFICATION.md, may19_checkpoint_analysis.py, WAVE_1_MONITORING_COORDINATION_GUIDE.md, WAVE_1_MONITORING_DASHBOARD.md. No external sources required — all event data is from live project state.*
