---
title: "Phase 5 Unified Risk Trigger Runbook"
project: systems-resilience
phase: 5-6
status: PRODUCTION-READY — applies to Option A and Option B
created: 2026-05-30
applies_to:
  - PHASE_5_WAVE_1_OPTION_A_TIMELINE.md
  - PHASE_5_WAVE_1_OPTION_B_TIMELINE.md
trigger_catalog:
  - RT-1: Scope creep (word-count output drop >20%)
  - RT-2: Author unavailability
  - RT-3: Research dead-end (>2 consecutive source-gap failures)
  - RT-4: Peer review bottleneck (missed return deadline)
  - RT-5: Publication delay (peer review completion misses deadline)
  - RT-6: Orchestrator overload (Option B specific)
---

# Phase 5 Unified Risk Trigger Runbook
## Applies to Option A and Option B — Reference This Document When Any Trigger Activates

> **How to use this document**: When a risk trigger fires, find the matching section below and execute the response protocol in order. Each protocol has a detection signal (quantitative), an immediate action (within 2 hours), a 24-hour response, and a contingency path if the immediate action fails. Do not improvise; the protocols are designed to be executed under pressure.
>
> **Option-specific notes**: Sections marked [A ONLY] apply only to Option A timing. Sections marked [B ONLY] apply only to Option B timing. All other sections apply to both.

---

## RT-1: Scope Creep Detection

### Detection Signal

**Primary**: Any Phase 6 domain author's daily standup word count is more than 20% below the rolling 3-day baseline.

Calculation: 
```
Baseline = (word count day 1 + day 2 + day 3) / 3
Today's target = Baseline × 0.80
If today's actual < today's target → RT-1 triggers
```

**Secondary signals** (confirm RT-1 if present alongside word-count drop):
- Author's submitted sections contain topics not in their approved outline
- Author reports "expanding scope" or "found a related area I want to cover"
- Submitted draft contains references to Phase 5 topics already covered (Phase 5 re-coverage)
- Submitted draft contains significant content from another Phase 6 domain's scope

**Note**: A word-count drop WITHOUT scope expansion may be burnout (RT-2 precursor) or a research dead-end (RT-3), not scope creep. Check for scope expansion signals before treating as RT-1.

### Immediate Action (within 2 hours of detection)

1. Pull the author's last approved outline. Compare section-by-section against what they have submitted or reported as in-progress.
2. Identify the specific section(s) where scope has expanded beyond the outline. Write a 2-3 sentence scope boundary note for each at-risk section.
3. Contact the author within 2 hours:

```
SCOPE BOUNDARY CHECK — [DOMAIN] — [DATE]

Hi [NAME],

Your standup shows [word count] words today vs. a [baseline] average over 
the past 3 days. Looking at your draft, Section [X] appears to extend 
into [description of out-of-scope content].

Your approved outline has Section [X] covering [approved scope]. 
Can you confirm whether:
(A) You are staying within the approved scope and the word count drop 
    reflects research complexity, not scope expansion?
(B) You have expanded Section [X] beyond the approved outline?

If (B): please confirm scope correction to the approved boundaries 
before continuing. If you believe the scope expansion is justified, 
send me a 2-sentence argument and I will decide within 4 hours.

Not blocking you — just confirming scope before the draft goes further 
in a direction that may need revision.
```

### 24-Hour Response

**If author confirms scope is within bounds** (word-count drop is research complexity, not scope expansion): Close RT-1. Watch for 3 more days. If word count recovers to within 20% of baseline: confirm resolution.

**If author confirms scope expansion and justification is accepted**: Formally update the approved outline. Commit the updated outline to master. Confirm new word count projections against T+14 gate. Log scope change in WORKLOG.md.

**If author confirms scope expansion but justification is not accepted**: Issue scope correction request:

```
Please trim Section [X] back to the approved scope. Specifically:
- Remove content covering [out-of-scope topic]
- That topic is covered by [Phase 5 document / other Phase 6 domain] — 
  add a cross-reference instead of re-covering it
- Confirm Section [X] scope is restored to [approved scope] in your 
  next standup
```

**If no author response within 24 hours**: Escalate to CT-3 (author unavailability concern). The combination of word-count drop AND no response is a stronger escalation signal than either alone.

### Contingency Path

**If scope creep is discovered at T+10 or later** (during peer review): The peer reviewer will likely flag it. Orchestrator issues a mandatory scope correction before T+14 gate. If the out-of-scope section is more than 5,000 words, the author cannot revise it before T+14 — either: (a) mark the section as [DEFERRED TO WAVE 2] and exclude from T+14 word count calculation, or (b) accept conditional readiness and complete the correction in the post-Wave-1 window.

**If scope creep has corrupted the document's structure** (the approved outline cannot be recovered without major rewrite): Activate CT-2 (research dead-end) — the effective research question has changed enough that the document needs to be re-scoped. Schedule a 20-minute call with the author to reframe.

### [A ONLY] Option A timing note
RT-1 detected at T+3 can be corrected before T+5 writing begins — low cost. RT-1 at T+7 requires correction before T+10 peer review send. RT-1 at T+10 is high-cost but still manageable with the T+13 integration sweep.

### [B ONLY] Option B timing note
RT-1 at T+7 (June 8) is especially urgent because T+14 (June 15) is the single gate with no buffer. Any scope correction must complete by T+13 (June 14). If scope correction at T+10 would require more than 2 days of rewriting, move the domain to conditional readiness and defer the scope-corrected version to post-June-15.

---

## RT-2: Author Unavailability

### Detection Signal

**Tier 1 (urgent)**: Author fails to respond to T+0 kickoff briefing by T+1 17:00 UTC.
**Tier 2 (urgent)**: Author misses two consecutive daily standups without advance notice.
**Tier 3 (escalating)**: Author responds to standups but reports zero writing progress for 2 consecutive days without explanation.
**Tier 4 (critical)**: Author confirms unavailability at any point during the sprint.

### Immediate Action: Backup Author Onboarding SLA (<24 hours from trigger)

The SLA is 24 hours from trigger detection to backup author onboarded. This means contingency author outreach must begin within 4 hours, not 24 hours.

**Step 1 — Within 4 hours of trigger:**
1. Log the gap in WORKLOG.md: domain affected, trigger tier, time of detection
2. Check if any other confirmed author has capacity to absorb the domain (only viable if: the domain is closely adjacent to their confirmed domain AND the added workload is under 15 hours)
3. Send contingency recruitment message to contingency author list for the affected domain (per PHASE_6_AUTHOR_HIRING_AND_ONBOARDING_FRAMEWORK.md Stage 1 channels):

```
Subject: Urgent — Phase 6 [Domain] author needed — accelerated timeline

Hi [CANDIDATE NAME],

We need a Phase 6 author for [DOMAIN] immediately due to a scheduling 
conflict with our original author. This is paid work at [agreed rate].

The accelerated timeline:
- Start: immediately upon acceptance
- Orientation reading: today-tomorrow (4 pre-staged documents provided)
- Outline submission: [T+5 date — adjusted for late start]
- First draft checkpoint: [T+9 date — adjusted]
- Full document: [T+14 date — or extended if confirmed late]

The research kit is fully prepared — you receive 20+ verified sources, 
a domain outline, a Phase 5 model document as your structural guide, 
and direct orchestrator support.

Reply within 12 hours if you can take this on. Happy to answer 
questions by phone or message.
```

4. Set a 24-hour response deadline on the contingency author outreach

**Step 2 — Hour 4-24:**
If contingency author responds and accepts: brief them on the accelerated timeline.

Timeline adjustment for late-start author:
| Original gate | Adjustment |
|---------------|-----------|
| T+3 outline | T+5 outline (June 6 under Option A; June 6 under Option B) |
| T+7 first draft | T+9 first draft (June 10 under Option A; June 10 under Option B) |
| T+10 peer review | T+12 peer review (June 13 under Option A; June 13 under Option B) |
| T+14 publication gate | T+14 — still within wave if confirmed by T+2 |

The late-start author can still hit the T+14 gate if confirmed within 48 hours of T+0. Confirmed at T+3 or later: T+14 gate becomes conditional readiness rather than full readiness.

**Step 3 — If no contingency author confirmed by T+3:**
Activate self-execution path. Orchestrator takes the domain directly.

**Self-execution schedule:**
- Outline by T+4 (June 5 Option A; June 5 Option B)
- First draft sections by T+9 (June 10)
- Peer review by T+12 (June 13)
- T+14 gate: domain scores 6.5-7.0 (conditional readiness) rather than 7.5-8.5

**Do not**: Cancel the domain. If pre-research is complete, self-execution produces publishable material. Lower quality than author-written but within the T+14 publication readiness threshold.

### Quality expectation for contingency paths

| Path | Expected T+14 score | Notes |
|------|---------------------|-------|
| Original author (no disruption) | 7.5-8.5 | Full-quality output |
| Contingency author (≤T+2 start) | 7.0-8.0 | Slight orientation lag; quality recovers by T+7 |
| Contingency author (T+3-T+5 start) | 6.5-7.5 | Conditional readiness expected; close-out within 5 days post-T+14 |
| Self-execution (orchestrator) | 6.0-7.0 | Publication-ready but author expertise absent |

---

## RT-3: Research Dead-End

### Detection Signal

**Primary**: An author reports in any standup or direct message that the core thesis of a section or the domain document cannot be supported by accessible sources.

**Quantitative trigger**: Two or more consecutive source-gap failures in the same section within a 48-hour window.

A "source-gap failure" is: the orchestrator attempts to substitute an inaccessible source using WebSearch/WebFetch, and the substitute either (a) does not exist, (b) directly contradicts the framing established in the pre-research outline, or (c) is behind an insurmountable paywall with no open-access equivalent.

Two consecutive failures in the same section = RT-3 trigger. Escalate immediately; do not wait for a third failure.

### Immediate Action (within 4 hours of second failure)

1. Orchestrator runs a 1-hour independent source search on the specific gap using WebSearch and WebFetch targeting the exact claim or section thesis
2. If sources are found: provide them to the author; continue. RT-3 closes.
3. If sources are not found: proceed to 24-hour assessment

### 24-Hour Assessment

Evaluate the gap category:

**Category A — Minor gap (section is under 5% of total word count):**
Mark as `[RESEARCH GAP — DOCUMENTED]` in the document with this text:
```
[RESEARCH GAP: The literature on [specific topic] does not provide 
well-documented case studies at the Zone 5 community scale. This 
section draws on adjacent evidence from [adjacent domain]. Practitioners 
should treat this guidance as informed inference rather than documented 
precedent, and document their own community's experience for future 
reference.]
```
This is acceptable for Wave 1. Documented gaps are more credible than papered-over gaps.

**Category B — Framing can be adjusted (section is defensible if narrowed):**
Schedule a 20-minute call with the author. Goal: reframe the section around a narrower, more defensible claim. Example: "Community currencies at 50-person scale" cannot be sourced → reframe to "Time-banking and labor-hour exchange systems, which have documented case studies at 20-200 person scale in [specific examples]."

**Category C — Major gap (section is over 15% of total word count AND cannot be reframed):**
Escalate to orchestrator scope decision. Options:
- (A) Bring in a specialist co-reviewer who can identify sources the research agent and author missed (4-8 hour search, specialist credential required)
- (B) Reclassify the section as a synthesis gap — not a failure — with this text: `[SYNTHESIS NOTE: This question — [specific framing] — is not well-addressed in the published literature at the community scale. The following guidance synthesizes adjacent evidence and should be treated as a framework for community experimentation rather than an established protocol.]`
- (C) Reduce the section's word count target and compensate by expanding an adjacent section where sources are strong

**Do not** allow undocumented gaps. Every major gap that cannot be filled must be named explicitly.

### Contingency Path (RT-3 at T+7 or later)

If a research dead-end is confirmed at the T+7 checkpoint or during the T+10 peer review:

- If the gap is in a section scheduled for peer review: send the section to the peer reviewer with a note — "Section [X] has a documented research gap. Please confirm whether you know of sources that would strengthen this section, or whether you agree that the documented-gap framing is the correct approach."
- If the peer reviewer cannot identify sources: document the gap formally and proceed to T+14 with a conditional readiness note on that section.

---

## RT-4: Peer Review Bottleneck

### Detection Signal

**Primary**: A peer reviewer fails to return their review by the deadline (T+12 17:00 UTC = June 13 17:00 UTC).

**Pre-trigger warning** (72-hour escalation begins here): A peer reviewer signals uncertain availability at any point before their review is due. Treat a signal of uncertain availability as equivalent to a missed deadline — activate backup immediately.

### 72-Hour Escalation Protocol

The 72-hour window runs from when the reviewer was confirmed (T+9, June 10) to when their review is due (T+12, June 13). This window is exactly 72 hours under the standard schedule.

**Hour 0 (T+9 confirmation)**: Confirm peer reviewer and backup reviewer for each domain. If any reviewer cannot confirm backup exists: do not wait — identify backup immediately.

**Hour 48 (T+11 June 12 midday)**: Send mid-window check to each reviewer: "You're halfway through the review window. Any questions about the template or the domain? Still on track for June 13 17:00 UTC?" A reviewer who does not reply to this check by T+11 17:00 UTC is elevated to WATCH status.

**Hour 60 (T+12 June 13 09:00 UTC)**: Send formal 8-hour reminder: "Peer review due today by 17:00 UTC. Reply to confirm you're on track." If no response to this message within 2 hours: activate backup reviewer immediately. Do not wait for the 17:00 deadline.

**Hour 72 (T+12 June 13 17:00 UTC)**: Deadline. If review is not received: backup reviewer takes over. Orchestrator begins internal review simultaneously (in case backup also delays).

### Backup Reviewer Activation

When backup reviewer is activated:

```
Subject: Urgent — peer review needed — [DOMAIN] — [DATE]

Hi [BACKUP REVIEWER NAME],

Our primary peer reviewer for [DOMAIN] has not returned their review 
by the deadline. I need you to step in as our reviewer.

You will receive the draft within the hour. Your review is due:
[DEADLINE — give 24 hours from this message, even if this pushes past T+12]

Review template is attached. Focus on: mandatory items only (factual 
corrections, citation gaps, community context gaps). Advisory items 
(framing, voice, additional sources) are welcome but not required 
in this accelerated timeline.

Compensation: [as agreed or standard rate].

Please confirm receipt within 30 minutes.
```

### Domains That Can Skip Peer Review for June 15 Publication

**Conditions under which a domain may publish without external peer review:**

Under Option A: The domain can publish without external peer review if: (a) the orchestrator internal review is complete (using the structured review template), AND (b) the domain scores ≥7.5 on the publication readiness matrix without the peer review integration criterion — meaning it scores ≥7.5 on the 8 non-peer-review criteria and receives 0 for criterion 3 (peer review integration). A domain scoring 7.5/8.0 on non-peer-review criteria = 7.5/9.0 total including 0 for peer review, which is above the 7.0 minimum.

Under Option B: More restrictive. Because Option B is designed as an institutional-grade publication, external peer review is a quality signal that justifies the single-volume format. A domain without external peer review under Option B can still publish but should be noted in the distribution as "pending external peer review" with a specific follow-up date.

**Domains that CANNOT skip peer review** (their domain scope is high enough that self-assessment is insufficient):
- Economic Resilience: requires practitioner validation that the community exchange models are operationally viable
- Infrastructure Interdependencies: requires technical validation that interdependency mapping is accurate
- Any domain where the author is self-executing (orchestrator writing): requires external review to compensate for author-as-reviewer conflict

**Domains where internal review is sufficient** (high citability, well-documented territory):
- Any domain with ≥25 verified accessible citations and ≥80% of target word count: internal review is sufficient for Wave 1 publication, with external review deferred to a post-publication version.

### Peer Review Completion vs. June 15 Gate

**If peer review returns before June 13 17:00 UTC**: Full integration possible. No gate impact.

**If peer review returns June 14 06:00-12:00 UTC**: Mandatory items only can be integrated (T+13 integration sweep). Advisory items deferred. Domain may still score ≥7.0 at T+14 gate.

**If peer review returns June 14 12:00-23:00 UTC**: Orchestrator reads and categorizes; forwards mandatory items to author. Author addresses June 14 EOD. Very compressed but feasible for domains where mandatory items are few.

**If peer review does not return by June 14 EOD**: Domain publishes with orchestrator internal review only. Status note added to distribution: "External peer review pending — [domain] scheduled for post-publication peer review by [date]." This is a conditional readiness outcome, not a failure.

**June 22-29 deferred publication option**: If a domain's peer review situation is severe enough that mandatory items cannot be addressed before June 15, the domain defers to a June 22-29 distribution window. This applies to:
- Domains where peer review arrived June 14 and mandatory items require more than one day of author revision
- Domains where the peer reviewer's factual corrections required significant source verification

The June 15 wave publishes all domains that are ready. June 22-29 is the deferred window for domains that need the extra week. This is not a cascade — the June 15 publication proceeds regardless.

---

## RT-5: Publication Delay

### Detection Signal

**Option A**: Wave 1+2 publication (June 5 target) slips more than 2 calendar days (i.e., not published by June 7).

**Option B**: Unified publication (June 15 target) slips any amount (Option B has no buffer day in the publication chain).

### Response Protocol (Option A)

A 1-2 day slip in Wave 1+2 publication (June 6-7 instead of June 5) has zero cascade effect:
- Wave 3 publication (June 28-30) has 25+ days of buffer and can absorb a 3-day slip without missing the June 30 target
- Phase 6 domain production is independent of Wave 1+2 publication timing
- Author onboarding is independent of Wave 1+2 publication timing

**Only log the slip and adjust**: "Wave 1+2 publication slipped to [DATE]. No cascade. Wave 3 target remains June 28-30. Phase 6 production unaffected."

A 3-5 day slip (June 8-10 instead of June 5): Wave 3 reader-feedback integration window shrinks from 25 days to 20-22 days. Still acceptable — reduce Wave 3 reader feedback incorporation from "thorough" to "critical items only."

A slip greater than 5 days (June 10+): Escalate to user for scope adjustment. At this point the feedback integration window is so short it may not be worth incorporating. Option: publish Wave 3 as-is without reader feedback integration; acknowledge in Wave 3 that reader responses to Volume 1 will inform a revised edition.

### Response Protocol (Option B)

Option B has a single gate at June 15. Any slip of June 15 is a material outcome that must be decided by the orchestrator within 4 hours of detection:

Option B-slip-1: **Delay to June 17-18 (2-3 day slip)**: Notify institutional distribution partner immediately. Most partners can accommodate a 2-3 day delay with 48-hour notice. Proceed with the delay and publish June 17-18.

Option B-slip-2: **Delay to June 22-29**: This is a significant slip. Notify institutional partner. Assess whether Option A's June 5 Wave 1+2 + June 30 Wave 3 structure would now produce better outcomes than a delayed unified release. If the institutional partner's use case required before June 22: switch to Option A immediately and publish Wave 1+2 as-is.

Option B-slip-3: **Cannot publish by June 29**: Rare but plan for it. Proceed with publishing whatever is complete by June 29. Any incomplete domains publish as "Volume [N] — Part 1" with a stated completion date. Do not hold complete, publication-ready domains waiting for delayed domains.

---

## RT-6: Orchestrator Overload (Option B Specific)

### Detection Signal

This trigger applies only to Option B. It does not apply to Option A because Option A's contention profile is bounded and drops sharply after June 5.

**Signal**: Orchestrator has exceeded 8-10 hours/day on 2 consecutive days, AND the task backlog is growing rather than shrinking. Specific indicators:
- Author standup blockers are aging past 8 hours without resolution (standard SLA is 4 hours)
- Phase 5 editorial pass is behind schedule (fewer documents cross-referenced per day than the target)
- Phase 6 outline feedback is late (>12 hours past SLA)

**This is not a failure — it is a designed trigger.** Option B carries higher contention risk (RESOURCE_CONTENTION_ANALYSIS.md, Section 6). RT-6 is the built-in early warning.

### Response Protocol

**Step 1 — Triage (within 2 hours of detection):**
List all pending tasks. Categorize each as:
- (CRITICAL): On the critical path; delay cascades
- (HIGH): On a decision gate; delay blocks others but doesn't cascade
- (LOW): Monitoring, non-critical review, or advisory feedback

**Step 2 — Reduce scope:**
From the LOW category: defer to next day. Any LOW task that has been deferred 2 days in a row becomes HIGH.

From the HIGH category: can any task be reduced in depth? Example: instead of reviewing all submitted section drafts in full, review the first and last sections of each domain draft and skim the middle — this takes 30 minutes per domain instead of 2 hours.

**Step 3 — Assess Wave 2 deferral:**
If Step 2 scope reduction is insufficient (CRITICAL tasks are still aging): defer Wave 2 Phase 6 domains immediately. The designed safety valve: move Wave 2 start dates from June 6 to June 30. Log in ORCHESTRATOR_STATE.md: "Wave 2 Phase 6 domains deferred to June 30 — RT-6 activated [DATE]. Reason: orchestrator overload in June 8-14 window."

**Step 4 — Notify user (same day):**
RT-6 is the only trigger in this runbook that requires same-day user notification (all others are orchestrator-resolvable). The notification is a brief status note:

```
ORCHESTRATOR OVERLOAD ALERT — [DATE]

Orchestrator workload has exceeded capacity threshold for 2 consecutive days. 
Immediate action taken: [scope reduction steps from Step 2]. 

If this continues: Wave 2 Phase 6 domains will be deferred to June 30 
([affected domain names]) without user input — this is the designed safety 
valve for Option B. 

User input needed: (1) Are there any HIGH or CRITICAL tasks I should deprioritize 
that are not apparent to me? (2) Any flexibility on the June 15 publication date 
that would reduce pressure on the editorial integration track?

No response needed if the above is acceptable. I will activate the Wave 2 
deferral if overload continues through [DATE + 2 days].
```

---

## Quick Reference: Trigger Decision Table

| Signal observed | Trigger | Immediate action | 24h action | Escalate to user? |
|----------------|---------|------------------|------------|-------------------|
| Word count drops >20% vs. baseline | RT-1 | Check for scope expansion; contact author within 2h | Scope correction or outline update | Only if scope dispute unresolved |
| Author misses 2 standups without notice | RT-2 | Contingency author outreach within 4h | Confirm backup or self-execute | Not required |
| Author confirms unavailability | RT-2 (Tier 4) | Contingency author outreach within 4h | 24h onboarding SLA begins | Not required |
| 2 consecutive source-gap failures, same section | RT-3 | 1-hour orchestrator source sprint | Categorize gap; reframe or document | Only if Category C (major gap) |
| Peer reviewer signals uncertain availability | RT-4 | Activate backup reviewer immediately | Backup briefed and confirmed | Not required |
| Peer reviewer misses deadline | RT-4 | Backup reviewer + orchestrator internal review | Integration of late review (mandatory only) | Not required |
| Wave 1+2 publication slips >5 days (Option A) | RT-5 | Log slip; reduce Wave 3 feedback scope | No cascade; adjust Wave 3 | Brief notification |
| Unified publication slips at all (Option B) | RT-5 | Notify institutional partner within 4h | Assess Option A switch if >5 day slip | YES — within same day |
| Orchestrator exceeds 8-10h/day for 2 consecutive days (Option B) | RT-6 | Triage task list; reduce LOW scope | Wave 2 deferral if insufficient | YES — same day notification |

---

*This runbook is production-ready. When a trigger fires, open the relevant section and execute in order. Do not improvise under pressure. All response protocols are designed to be executed in a high-workload state — they require no research, no new planning, and no user input unless explicitly noted.*
