---
title: "Phase 5 Wave 1 — Critical Path Analysis"
project: systems-resilience
phase: 5-6
status: PRODUCTION-READY — reference June 1 onward
created: 2026-05-30
applies_to:
  - PHASE_5_WAVE_1_OPTION_A_TIMELINE.md
  - PHASE_5_WAVE_1_OPTION_B_TIMELINE.md
scope: "June 1-15 (Option A and Option B) with Option A continuation to June 30"
---

# Phase 5 Wave 1 — Critical Path Analysis
## Zero-Slack Days, Dependencies, and Bottleneck Dates for Option A and Option B

> **How to use this document**: Identify the current date and find it in the critical path tables below. Days with ZERO SLACK are non-negotiable; a delay on any one of them cascades to the next gate. Days marked BUFFER can slip one day without causing a cascade. Use the dependency maps to understand which tasks can be done in parallel and which must be sequential.

---

## Section 1: Definitions

**Zero-slack day**: A day where the task due must complete on that calendar date to avoid cascading downstream. There is no buffer — even a single day of delay forces a date change somewhere later in the timeline.

**Buffer day**: A day where the scheduled task could slip to the following day without causing a downstream cascade. Buffer days appear by design — they exist because the prior critical path items completed early or the next gate has multiple input days.

**Bottleneck date**: A date where one delayed input blocks multiple downstream outputs simultaneously. Bottleneck dates are worse than ordinary zero-slack days because a single missed task blocks several tracks at once.

**Parallel execution**: Two or more tasks that are independent and can run simultaneously without either blocking the other.

**Sequential dependency**: A task that cannot begin until a specific prior task is complete.

---

## Section 2: Option A Critical Path — June 1-15

### Zero-Slack Days

| Date | T-day | Task | Why zero slack |
|------|-------|------|----------------|
| June 1 06:00 UTC | T+0 | Orchestrator pre-flight complete | Author briefings are time-sensitive; delayed pre-flight delays every T+0 task. Any cascade from June 1 delay means Phase 6 agents start June 2, losing one day of production from the 14-day sprint. |
| June 3 17:00 UTC | T+2 | Wave 1+2 editorial complete and committed | Publication is scheduled for June 5. If editorial is not done by June 3 EOD, June 4 becomes a combined editorial + outline review day — dangerously overloaded. Any editorial slip past June 4 pushes publication past June 5. |
| June 5 06:00-09:00 UTC | T+4 | Wave 1+2 published | Option A's first external gate. Publication on June 5 gives Wave 3 a 25-day reader-feedback window before the June 28-30 publication. A 3-day slip (to June 8) compresses feedback window to 20 days — manageable. A 7-day slip (to June 12) compresses it to 16 days and cuts into the Wave 3 editorial pass. |
| June 8 12:00 UTC | T+7 | First-draft checkpoint submissions received | This is the earliest moment when Green/Amber/Red assessments are meaningful. If submissions are delayed to June 9 or 10, the orchestrator loses 1-2 days of recovery time for Amber/Red domains before the T+10 peer review send. |
| June 10 12:00 UTC | T+9 | All peer reviewers confirmed with backup | If any reviewer is unconfirmed at T+9, backup activation must happen the same day. A reviewer unconfirmed at T+10 (June 11) means backup is receiving draft materials AND conducting review in the same 48-hour window — too compressed to ensure quality. |
| June 11 12:00 UTC | T+10 | All Phase 6 draft submissions sent to peer review | The 48-hour review window is exactly June 11 12:00 UTC to June 13 12:00 UTC. A delay in sending means either: (a) the reviewer gets fewer hours and quality drops, or (b) the June 13 17:00 UTC deadline slips, which directly compromises T+14. |
| June 13 17:00 UTC | T+12 | Peer reviews returned | There are 48 hours between review return and the T+14 gate. Under Option A, this is tight but workable — June 14 is a full integration sweep day. A peer review returned June 14 (24 hours late) can still be incorporated, but only mandatory items. A review returned June 15 (48 hours late) cannot be incorporated at all. |
| June 15 17:00 UTC | T+14 | Publication readiness gate | This is the Wave 1 close. There is no extension — conditional readiness scores are the safety valve, not timeline extension. |

### Buffer Days (Option A)

| Date | T-day | Why it has buffer |
|------|-------|-------------------|
| June 2 | T+1 | Orientation day; no hard output required. A slip on June 2 delays orientation but doesn't change the June 4 outline deadline if June 3 editorial is complete. |
| June 6 | T+5 | Wave 2 domain ramp. Wave 2 domains (Ecosystem Restoration, Institutional Learning) have a secondary timeline; one day of delay in their orientation doesn't affect Wave 1 fast-track domain production. |
| June 7 | T+6 | Week 1 review is a synthesis activity, not a decision gate. The review informs June 8 assessment but doesn't block it. |
| June 9 | T+8 | Feedback from T+7 goes out at 09:00 UTC on June 9, which is a hard SLA, but the balance of the day (Wave 2 outlines, peer review prep) has flexibility. |
| June 12 | T+11 | Production and monitoring. Authors are writing; peer reviewers are reviewing. The orchestrator is in monitoring mode. A slip on June 12 monitoring tasks doesn't block June 13 deadline. |
| June 14 | T+13 | Integration sweep. Authors have the full day to address mandatory peer review items. As long as peer reviews were returned June 13 17:00 UTC, the integration sweep can start any time June 14 and still complete before June 15. |

---

## Section 3: Option A Dependency Map

### Parallel Tasks (can run simultaneously)

```
June 1:
├── [PARALLEL] Author briefing emails sent (07:00 UTC)
├── [PARALLEL] Phase 6 research agent dispatch (07:30 UTC)
└── [PARALLEL] Peer reviewer introduction emails (08:00 UTC)
    → These three are independent and run in the same 07:00-09:00 window

June 1-3:
├── [PARALLEL] Wave 1+2 editorial work (morning blocks)
└── [PARALLEL] Phase 6 author orientation follow-up (afternoon blocks)
    → Editorial work does not block author orientation; both proceed simultaneously

June 6-10:
├── [PARALLEL] Phase 6 Wave 1 authors writing
└── [PARALLEL] Phase 6 Wave 2 authors onboarding/outlining
    → Wave 1 writing and Wave 2 onboarding are fully independent

June 11-13:
├── [PARALLEL] Phase 6 authors writing (unreviewed sections)
└── [PARALLEL] Peer reviewers reviewing submitted sections
    → Production and review run simultaneously; neither blocks the other
```

### Sequential Dependencies (cannot overlap)

```
June 3 editorial complete → June 5 publication (editorial must precede publication)

June 4 outline submissions received → June 5 outline feedback sent
    (cannot send feedback until submissions exist)

June 8 first-draft submissions received → June 9 feedback sent
    (assessment must precede feedback)

June 10 peer reviewers confirmed → June 11 draft submissions sent
    (cannot route submissions without confirmed reviewer destinations)

June 11 draft submissions sent → June 13 peer reviews returned
    (48-hour review window; cannot return before receipt)

June 13 peer reviews returned → June 14 integration sweep
    (cannot integrate feedback before feedback exists)

June 14 integration sweep complete → June 15 publication readiness gate
    (readiness assessment requires completed integration)
```

### Longest sequential chain (Option A)

The longest unbroken sequential chain in Option A is 11 days:

```
June 1: Author briefings sent
  → June 2: Orientation confirmed
    → June 3: Research kit verified + editorial complete
      → June 4: Outlines submitted
        → June 5: Outline feedback returned + Wave 1+2 published
          → June 8: First drafts submitted
            → June 9: Feedback returned to authors
              → June 11: Drafts sent to peer review
                → June 13: Peer reviews returned
                  → June 14: Integration sweep
                    → June 15: Publication readiness gate
```

Any break in this chain cascades forward. The chain has two embedded shortcuts (June 6-7 buffer, June 12 buffer) that allow 1-day slippage without breaking the chain.

---

## Section 4: Option B Critical Path — June 1-15

Option B has more zero-slack days than Option A because it carries two simultaneous tracks (Phase 5 editorial AND Phase 6 production) with a single June 15 gate and no buffer between peer review return (June 13) and publication (June 15).

### Zero-Slack Days (Option B)

| Date | T-day | Task | Why zero slack |
|------|-------|------|----------------|
| June 1 06:00 UTC | T+0 | Pre-flight + dual-track activation | Same as Option A, but with additional editorial track starting immediately. Delay cascades to both editorial start and Phase 6 agent dispatch. |
| June 5 12:00 UTC | T+4 | Phase 5 editorial integration complete and committed | This is Option B's most important internal milestone. The entire June 15 publication depends on editorial integration completing before peer review ends. If editorial is not done by June 5, it must be completed June 6-7 — which overlaps with Wave 2 domain ramp and creates a MEDIUM-HIGH contention collision. If not done by June 7, editorial time must be carved from Phase 6 review time June 8-10, creating the RED day cascade. |
| June 8 12:00 UTC | T+7 | T+7 first-draft checkpoint + author onboarding begins | Same constraint as Option A, compounded by author onboarding starting the same day. If T+7 submissions are late, the assessment window shrinks without any compensating buffer. |
| June 10 12:00 UTC | T+9 | All peer reviewers confirmed with backup | Under Option B, unconfirmed reviewers at T+9 are more dangerous than under Option A because there are only 5 days between reviewer confirmation and the publication gate. A backup reviewer who receives materials June 13 must return review by June 14 to enable even minimal integration before June 15. |
| June 11 12:00 UTC | T+10 | All Phase 6 draft submissions sent to peer review | Same as Option A. The 48-hour window is hard-coded; any slip compresses reviewer time or the integration sweep. |
| June 13 17:00 UTC | T+12 | Peer reviews returned | Under Option B, a review returned June 14 can be incorporated only if it arrives by 12:00 UTC (5-hour window for integration before end of day). A review returned June 14 17:00 UTC cannot be incorporated. Under Option A, a June 14 return still allows full-day integration. Under Option B, it allows only partial integration. |
| June 14 EOD | T+13 | All mandatory peer review items addressed | No Option B equivalent of "defer advisory items to post-Wave-1 window" — the June 15 gate has no follow-on buffer. All mandatory items must be complete by June 14 EOD. |
| June 15 06:00 UTC | T+14 | Phase 5 unified publication sent | Option B's single gate. There is no Option A-equivalent "one document slips 24 hours" exception — the institutional partner receives all 12 documents simultaneously. |
| June 15 17:00 UTC | T+14 | Phase 6 T+14 publication readiness gate | Same as Option A. |

### Buffer Days (Option B)

| Date | T-day | Why it has buffer |
|------|-------|-------------------|
| June 2 | T+1 | Wave 2 cross-reference pass can extend to morning of June 3 if needed; June 3 is reserved for Wave 3 pass. |
| June 3 | T+2 | Wave 3 cross-reference pass can extend to morning of June 4 if needed, provided editorial block prioritizes June 4 morning. |
| June 6 | T+5 | Phase 5 editorial is complete; Phase 6 fast-track authors are writing independently. Orchestrator is in monitoring mode. |
| June 7 | T+6 | Weekly sync is a monitoring activity. One-day slip doesn't affect Monday June 8 first-draft checkpoint. |
| June 9 | T+8 | Same buffer as Option A — balance of day has flexibility after T+7 feedback send. |
| June 12 | T+11 | Production and monitoring day. Authors writing, peer reviewers reviewing. No orchestrator action required unless a reviewer signals delay. |

### Bottleneck Dates (Option B)

Option B has three bottleneck dates — days where one delayed task blocks multiple downstream outputs:

**June 5 (T+4) — Editorial Integration Complete**: If Phase 5 editorial is not done by June 5, both the June 15 publication quality AND the Phase 6 Wave 2 domain ramp are compromised. Wave 2 domain ramp (June 6) depends on orchestrator bandwidth that is consumed by overrunning editorial work. This is the primary bottleneck.

**June 8 (T+7) — First-Draft + Onboarding**: Three tasks share this day: T+7 assessment (12:00 deadline), author onboarding (14:00 start), Wave 3 quality pass (14:00-17:00). A single overrun on T+7 assessment delays both onboarding and Wave 3 quality pass. Author onboarding delayed past June 8 pushes the June 20 production start, which compresses the author's writing time. Wave 3 quality pass delayed past June 8 compresses into the peer review window.

**June 13 (T+12) — Peer Reviews**: All peer reviews due June 13 17:00 UTC. Any single missed review cascades to orchestrator internal review which must complete by June 14 12:00 UTC to allow author integration. If two or more reviews are missing June 13, the orchestrator cannot complete multiple parallel internal reviews and the June 15 gate is compromised for those domains.

---

## Section 5: Option B Dependency Map

### Parallel Tasks (can run simultaneously, Option B)

```
June 1-5 daily structure:
├── [PARALLEL] Phase 5 editorial block (09:00-13:00 UTC)
└── [PARALLEL] Phase 6 author monitoring and blockers (14:00-17:00 UTC)
    → Separated by time block; cannot truly overlap, but can run same day

June 5-7:
├── [PARALLEL] Phase 6 Wave 1 authors writing
├── [PARALLEL] Phase 6 Wave 2 authors onboarding
└── [PARALLEL] Phase 5 editorial quality monitoring (passive)
    → All three independent; no orchestrator action required for Wave 1 writing

June 11-13:
├── [PARALLEL] Phase 6 authors writing (unreviewed sections)
├── [PARALLEL] Peer reviewers reviewing submitted sections
└── [PARALLEL] Wave 3 quality pass final review (if not complete by June 11)
    → All three are genuinely parallel; none blocks the others
```

### Sequential Dependencies (Option B)

```
Phase 5 editorial complete (June 5) → June 15 publication possible

Phase 6 author briefing (July 1 June 8) → author production start (June 20)
    (author cannot commit to production timeline without full briefing)

T+7 first-draft assessment (June 8) → T+7 feedback sent (June 9 09:00 UTC)
    (assessment must precede feedback)

Wave 2 outline submissions (June 9 17:00 UTC) → Wave 2 writing begins (June 10)

Peer reviewer confirmation (June 10) → draft submissions sent (June 11 12:00 UTC)

Draft submissions sent (June 11 12:00 UTC) → peer reviews returned (June 13 17:00 UTC)

Peer reviews returned (June 13 17:00 UTC) → integration sweep (June 14)

Integration sweep complete (June 14 EOD) → publication readiness gate (June 15)
```

### Longest sequential chain (Option B)

```
June 1: Editorial integration start + Phase 6 activation
  → June 5: Editorial integration complete
    → June 8: T+7 first-draft + author onboarding
      → June 10: Peer reviewers confirmed
        → June 11: Drafts sent to peer review
          → June 13: Peer reviews returned
            → June 14: Integration sweep
              → June 15: Phase 5 publication + Phase 6 readiness gate
```

This chain is 14 days long with zero inserted buffer days. Every day matters. The only safety valve is the parallel structure: while this chain runs, Wave 2 domain authors are working independently (parallel track), which means if a Wave 1 domain fails at any gate, the Wave 2 domains are unaffected and vice versa.

---

## Section 6: Option A vs. Option B — Critical Path Comparison

| Dimension | Option A | Option B |
|-----------|----------|----------|
| Zero-slack days | 8 (June 1, 3, 5, 8, 10, 11, 13, 15) | 9 (same plus June 14 EOD explicit gate) |
| Buffer days | 6 (June 2, 6, 7, 9, 12, 14) | 6 (June 2, 3, 6, 7, 9, 12) — different buffer days |
| Bottleneck dates | 1 (June 8 only — first-draft checkpoint) | 3 (June 5, June 8, June 13) |
| Longest sequential chain | 11 days (June 1-15 with buffers) | 14 days (June 1-15 no buffer days) |
| Cascade from peer review slip | 1 day buffer (June 14 advisory-only integration possible) | 0 buffer (June 14 mandatory-only, June 15 gate unchanged) |
| Editorial track zero-slack days | 2 (June 3, June 5) | 1 (June 5 — but longer window of risk June 1-5) |
| Recovery options if a gate slips | Option A: Wave 3 reader-feedback window is elastic; June 28-30 publication absorbs slippage | Option B: Conditional readiness at T+14 is the only safety valve |

**Key insight**: Option A has fewer bottleneck dates because its two publication events are separated by 25 days. A slip in the first event (Wave 1+2) does not affect the second event (Wave 3) unless it slips more than 5 days. Option B concentrates all risk into the single June 15 gate, which is why it has more zero-slack days and three bottleneck dates vs. Option A's one.

---

## Section 7: If Peer Review Feedback Is Late on June 10 — Cascade Analysis

This section shows the concrete downstream impact of a peer review delay under each option.

### Scenario: All peer reviews returned June 14 12:00 UTC (24 hours late)

**Option A impact**:
- Authors receive feedback June 14 12:00 UTC (12 hours into the integration sweep)
- Integration sweep has 5 hours remaining (June 14 12:00-17:00 UTC, plus evening)
- Mandatory items only (factual corrections, citation gaps) can be addressed
- Advisory items (framing, voice, additional sources) deferred to post-T+14
- Expected T+14 score impact: -0.5 on Criterion 3 (peer review integration), absorbed if other criteria are strong
- Net result: Most domains still achieve ≥7.0. Conditional readiness for domains where mandatory items were substantial.

**Option B impact**:
- Authors receive feedback June 14 12:00 UTC
- Integration sweep has 5 hours remaining — same as Option A
- BUT: Option B's T+14 gate is June 15 with no post-gate completion buffer
- Conditional domains must be flagged in the institutional distribution as "pending peer review integration"
- The institutional partner may require explanation for any domains at conditional readiness
- Net result: June 15 publication proceeds; 1-2 domains likely at conditional (6.0-6.9) rather than full readiness

### Scenario: One peer review not returned by June 15 17:00 UTC

**Option A**: Orchestrator internal review replaces external review. Domain can still score ≥7.0 if internal review is complete and other criteria are strong. The domain distributes with a note: "External peer review pending — follow-up version expected by [date]."

**Option B**: Same. Institutional partner is notified explicitly. The 12-document unified release proceeds; the single domain without external review is noted. Not a failure — a documented conditional.

---

## Section 8: High-Leverage Parallel Opportunities

These are the moments where running tasks in parallel produces the largest time savings (vs. running them sequentially, which would add days to the timeline):

**June 1 (both options)**: Author briefings, Phase 6 agent dispatch, and peer reviewer introductions are sent in a single 07:00-09:00 UTC window. If done sequentially (one after another), they would still all complete within 2 hours — but the practice of batching them as a synchronized send eliminates the response-timing gap that would occur if they were staggered by a day.

**June 5-7 (Option A) / June 6-7 (Option B)**: Phase 6 fast-track authors writing independently while orchestrator is in monitoring mode. This is the primary parallelization payoff of Wave 1 setup — once briefings, orientations, and outlines are done, author production runs without orchestrator involvement. The orchestrator's June 5-7 calendar is almost entirely free, which is why June 8 mid-wave checkpoint is feasible with a full assessment workload.

**June 11-13 (both options)**: Authors continue writing while peer reviewers review. This is the most important parallel window in the timeline. In a sequential model (stop writing, wait for review, integrate, then write again) authors would lose 3 days of production. In the parallel model, authors produce content in unreviewed sections while reviewers assess submitted sections, recovering those 3 days.

**June 14-15 (both options)**: Author integration sweep (June 14) and orchestrator publication readiness assessment (June 15) are separated by design so neither blocks the other. The orchestrator prepares the assessment framework on June 14 while authors integrate; the gate assessment runs June 15 on the completed integration.

---

*This analysis is production-ready. Use it June 1 onward to understand which delays cascade and which do not. When a task slips on a zero-slack day, immediately identify the downstream consequence using the dependency maps in Sections 3 and 5. Do not wait to see if a slip "works itself out" — by the time it becomes visible, the window for low-cost correction has passed.*
