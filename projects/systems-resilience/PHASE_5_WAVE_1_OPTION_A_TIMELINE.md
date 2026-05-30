---
title: "Phase 5 Wave 1 — Option A Day-by-Day Execution Timeline"
project: systems-resilience
option: A
description: "Wave 1+2 publication June 1-15; Wave 3 deferred to June 28-30"
status: PRODUCTION-READY — execute June 1 upon user confirmation of Option A
decision_deadline: 2026-05-31T23:59:00Z
activation_start: 2026-06-01T06:00:00Z
wave_1_end: 2026-06-15T23:59:00Z
wave_3_target: 2026-06-28T00:00:00Z
created: 2026-05-30
updated: 2026-05-30
companion_docs:
  - PHASE_6_WAVE_1_EXECUTION_CHECKLIST.md
  - PHASE_5_WAVE_1_UNIFIED_RISK_TRIGGER_RUNBOOK.md
  - PHASE_5_COORDINATION_TEMPLATES_PRE-FILLED.md
  - PHASE_5_WAVE_1_OPTION_B_TIMELINE.md
  - PHASE_5_WAVE_1_CRITICAL_PATH_ANALYSIS.md
  - PHASE_5_WAVE_1_EXECUTION_TEMPLATES.md
---

# Phase 5 Wave 1 — Option A Execution Timeline
## June 1–15 Day-by-Day Guide (Wave 3 Deferred to June 28-30)

> **How to use this document**: On June 1, open this file. Execute each day's tasks in order. Decision gates are marked with a gate symbol (>) and require a logged decision before proceeding. The critical path is marked with [CRITICAL PATH] — these are the days with zero slack. Everything else has buffer.
>
> **Pre-condition**: User has confirmed Option A by May 31 23:59 UTC. If no confirmation was received, proceed with Option A as the standing default (per MAY_31_ACTIVATION_DECISION_FRAMEWORK.md Part 7).

---

## Why Option A Structures the Way It Does

Option A concentrates editorial work into a bounded 5-day spike (June 1-5), publishes Wave 1+2 (43,621 words), then shifts to distributed lower-intensity activity for June 6-30. This front-loading strategy is deliberate:

- It creates two independent publication gates (June 5, June 28-30) with separate risk profiles
- After June 5 the orchestrator drops to passive monitoring, freeing bandwidth for Phase 6 domain review and author onboarding
- The June 5-30 window allows Wave 1+2 reader feedback to inform a light Wave 3 editorial pass before the June 28-30 publication
- The June 8 mid-wave checkpoint is placed at day 8 because that is where the outline-review cycle closes and first-draft writing is fully underway in all fast-track domains — it is the first moment where trajectory is visible and course correction is still low-cost

**Option A is the lower-resource option.** Total orchestrator hours June 1-15: approximately 35-45 hours (2.5-3 hours/day average, spiking to 6-8 hours on June 1, 3, and 8). This is sustainable without additional capacity.

---

## Pre-June-1 Confirmation (May 31)

### May 31 Readiness Gates (Complete by 23:59 UTC)

Before closing May 31, verify all four infrastructure gates are green:

| Gate | Due by | Check |
|------|--------|-------|
| R-1: User has selected Option A | 23:59 UTC | Logged in ORCHESTRATOR_STATE.md |
| R-2: Phase 6 domain selection confirmed (A, C, D or subset) | 23:59 UTC | Logged in ORCHESTRATOR_STATE.md |
| R-3: Phase 5 Wave 1+2 documents verified zero-placeholder | 16:00 UTC | Run placeholder scan: `grep -r "\[fill\]\|\[TBD\]\|\[TODO\]" projects/systems-resilience/phase-5-wave-2-*.md` |
| R-4: Author status known (confirmed or self-execute fallback) | 18:00 UTC | Author availability logged |

**If any gate is red at 23:59 UTC**: Log the gap and proceed with Option A anyway. The June 1 morning pre-flight (06:00-07:00 UTC) catches and resolves gate failures before author contact begins.

---

## Author Onboarding Schedule — June 1-9

This table is the single reference for who gets which contact on which date. Fill in author names when confirmed.

| Date (T-day) | Author contact type | Domain | Content | Time budget |
|--------------|---------------------|--------|---------|-------------|
| June 1 (T+0) | Kickoff briefing email | All confirmed authors | Full onboarding kit, research kit, model doc, domain candidate file | 2 hrs (send + log) |
| June 2 (T+1) | Orientation confirmation standup | All | Confirm receipt, outline approach, source access | 30 min async per domain |
| June 3 (T+2) | Research kit verification check | All | Confirm source access; substitute any blocked sources | 1 hr total |
| June 4 (T+3) | Outline submission day | All | Receive outlines by 17:00 UTC; begin review | 3-4 hrs (review) |
| June 5 (T+4) | Outline feedback send | All | Return feedback by 12:00 UTC; writing begins | 1-2 hrs |
| June 6 (T+5) | Wave 2 domain authors | Wave 2 (Ecosystem Restoration, Institutional Learning) | Send their T+0 equivalent briefing | 1-2 hrs |
| June 7 (T+6) | Weekly sync | All | Week 1 status review; word count, citations, peer reviewer confirmations | 30-45 min async |
| June 8 (T+7) | First-draft checkpoint | Fast-track and secondary domains | Receive first-draft packages by 12:00 UTC; assess | 4-5 hrs |
| June 9 (T+8) | Feedback loop closes | All | Send T+7 feedback by 09:00 UTC; Wave 2 outline reviews | 2-3 hrs |

**Author onboarding is complete by June 9.** From June 9 onward, contact is via daily standups (15-30 min async per day) until peer review routing on June 11.

---

## Daily Time Budget Summary (Option A)

| Date | Day | Primary activity | Orchestrator hours | Author hours | Notes |
|------|-----|-----------------|-------------------|--------------|-------|
| June 1 | Mon | Kickoff + editorial start | 6-8 | 2-3 | CRITICAL PATH: pre-flight 06:00 |
| June 2 | Tue | Orientation + editorial | 3-4 | 2-3 | Buffer: can slip 1 day |
| June 3 | Wed | Editorial completion | 4-5 | 3-4 | CRITICAL PATH: editorial done by 17:00 |
| June 4 | Thu | Outline gate | 3-4 | 6-8 (outlining) | CRITICAL PATH: outlines due 17:00 |
| June 5 | Fri | Publication + outline feedback | 5-6 | 4-6 (writing begins) | CRITICAL PATH: publication 06:00-09:00 |
| June 6 | Sat | Wave 2 ramp + monitoring | 2-3 | 4-6 | Buffer: can slip 1 day |
| June 7 | Sun | Week 1 review | 2-3 | 2-3 (writing) | Buffer: can slip 1 day |
| June 8 | Mon | First-draft checkpoint | 5-6 | 8-10 (submitting + writing) | CRITICAL PATH: submissions due 12:00 |
| June 9 | Tue | Feedback + Wave 2 outlines | 3-4 | 6-8 | Buffer: can slip 1 day |
| June 10 | Wed | Peer review prep | 3-4 | 6-8 | CRITICAL PATH: reviewers confirmed 12:00 |
| June 11 | Thu | Peer review send | 3-4 | 6-8 (writing + submitting) | CRITICAL PATH: drafts sent 12:00 |
| June 12 | Fri | Production + monitoring | 2-3 | 6-8 | Buffer: can slip 1 day |
| June 13 | Sat | Peer reviews due | 3-4 | 6-8 | CRITICAL PATH: reviews due 17:00 |
| June 14 | Sun | Integration sweep | 2-3 | 8-10 (addressing feedback) | Buffer: can slip 1 day |
| June 15 | Mon | Publication readiness gate | 5-6 | 2-3 | CRITICAL PATH: gate 17:00 |
| **TOTAL** | | | **55-65 hrs** | **75-95 hrs** | |

---

## Peer Review Intake Calendar

This calendar shows when drafts go out and when feedback comes back. Use this to schedule peer reviewer communication.

| Action | Date | UTC Time | Who |
|--------|------|----------|-----|
| Peer reviewer introductory email sent | June 1 | 08:00 | Orchestrator → all reviewers |
| Peer reviewers briefed on template and criteria | June 9 | 14:00-17:00 | Orchestrator → all reviewers |
| Peer reviewer availability confirmed | June 10 | 12:00 | All reviewers confirmed Y/N |
| Backup reviewers identified | June 10 | 12:00 | Per domain, logged in WORKLOG.md |
| Mid-window reviewer check ("still on track?") | June 12 | 12:00 | Orchestrator → all reviewers |
| Peer review reminder | June 13 | 09:00 | Orchestrator → all reviewers |
| Peer reviews due | June 13 | 17:00 | All reviewers → Orchestrator |
| Feedback classified and sent to authors | June 13 | 23:00 | Orchestrator → all authors |
| Author integration of mandatory items | June 14 | 09:00-17:00 | Authors |

**If any reviewer signals uncertainty before June 12**: activate backup reviewer the same day. Do not wait for the June 13 deadline.

---

## Publication Gates and Their Dates

Option A has two publication events. Each has its own gate.

### Gate 1: Wave 1+2 Publication (June 5)

**Pre-conditions (all must be green by June 4 EOD)**:
- [ ] All five Wave 1+2 documents: zero placeholder markers
- [ ] All five documents: consistent YAML frontmatter (`title`, `phase`, `wave`, `status: PRODUCTION-READY`, `created`)
- [ ] Wave 3 announcement language present in each document or in master distribution note
- [ ] Distribution list confirmed (Tier 1/2/3 contacts ready)
- [ ] Publication announcement drafted (per PHASE_5_WAVE_1_EXECUTION_TEMPLATES.md)

**Publication window**: June 5 06:00-09:00 UTC

**Decision gate >**: If a single document fails a last-minute check: publish the four others on schedule; delay the one document by 24 hours. Do not hold the entire corpus for one document.

**Post-publication**: Monitor reader responses June 5-14. Categorize: (A) no action, (B) factual correction, (C) scope addition, (D) Wave 3 content suggestion. Log B and C items for Wave 3 editorial pass.

### Gate 2: Wave 3 Publication (June 28-30)

**Pre-conditions (all must be green by June 27)**:
- [ ] Wave 3 editorial pass complete (8-12 hours, June 15-27)
- [ ] Cross-references to Wave 1+2 added where relevant
- [ ] Frontmatter standardized across all 7 Wave 3 documents
- [ ] Wave 3 master table of contents written
- [ ] Any reader feedback from Wave 1+2 incorporated (Category B and C items)

**Publication window**: June 28-30

---

## Risk Trigger Checkpoints (Option A)

These are the dates when risk assessment is mandatory, not optional. At each checkpoint, run the relevant check in PHASE_5_WAVE_1_UNIFIED_RISK_TRIGGER_RUNBOOK.md.

| Date | Trigger type | What to check | Threshold |
|------|-------------|---------------|-----------|
| June 2 (T+1) 17:00 UTC | RT-2 author unavailability | Any author has not responded to T+0 email | No response → activate CT-1 within 4 hours |
| June 4 (T+3) 17:00 UTC | RT-1 scope creep | Outlines received — do any exceed approved scope? | Any out-of-scope section → send correction request same day |
| June 7 (T+6) 17:00 UTC | RT-2, RT-1, RT-3 | Week 1 review: word counts, citation counts, scope signals | Any at-risk indicator → assess RT activation |
| June 8 (T+7) 12:00 UTC | All triggers | First-draft quality gate: word count, citations, voice, scope | Two+ at-risk indicators → RT escalation |
| June 10 (T+9) 12:00 UTC | RT-4 peer review | All reviewers confirmed? Backup assigned? | Any unconfirmed reviewer → activate backup same day |
| June 12 (T+11) 12:00 UTC | RT-4 | Mid-window reviewer check | No response to check → elevated to WATCH status |
| June 13 (T+12) 17:00 UTC | RT-4, RT-5 | Peer reviews returned? | Any missing review → backup + internal review activated |
| June 15 (T+14) 17:00 UTC | All triggers | T+14 publication readiness gate | Score <6.0 → scope adjustment meeting within 24 hours |

---

## June 1 (Monday) — T+0: Activation Day

### 06:00-07:00 UTC: Orchestrator Pre-Flight [CRITICAL PATH]

This hour is the only work that cannot move. Do not contact authors, do not start editorial work, until pre-flight is complete.

- [ ] Open ORCHESTRATOR_STATE.md — confirm Option A logged, domain selection logged, no blocking conditions overnight
- [ ] Confirm Jetson health: SSH to xxsb-01 (100.120.18.84) — stockbot status check. If unreachable: log and proceed; infrastructure work is non-blocking today
- [ ] Confirm Wave 1+2 file list (43,621 words across 5 documents):
  - `phase-5-wave-2-community-implementation-playbook.md`
  - `phase-5-wave-2-conflict-resolution-framework.md`
  - `phase-5-wave-2-psychological-support-guide.md`
  - `phase-5-wave-2-veterinary-care-guide.md`
  - `phase-5-wave-1` (microgrids)
- [ ] Log kickoff in WORKLOG.md: "Phase 5 Option A activated T+0 June 1 06:00 UTC. Wave 1+2 editorial sprint begins. Phase 6 domain briefings to follow. Author status: [confirmed/self-execute]."

**Decision gate >**: If overnight a blocking condition emerged (Jetson multi-day outage, user scope reversal), assess now. A single non-critical blocker does not delay activation. Log it and proceed. Only a user scope reversal received after 23:59 May 31 warrants a 30-minute pause to recalibrate.

**Time budget: 1 hour**

### 07:00-09:00 UTC: Author Briefings and Phase 6 Dispatch

**07:00**: Send Phase 6 author briefing email if author is confirmed. Template in PHASE_6_AUTHOR_ONBOARDING_KIT.md. Send simultaneously, not staggered.

**07:30**: Dispatch Phase 6 research agent briefings for confirmed domains (A+C+D recommended). Use PHASE_6_KICKOFF_PROMPT_TEMPLATE.md. Log agent assignments.

**08:00**: Send peer reviewer introduction emails for Phase 6 domains. Use Section 3 template from PHASE_6_COORDINATION_TEMPLATES.md. Tell reviewers: review window is June 11-13 (T+10 to T+12), 48-hour turnaround requested.

**08:30**: If author is NOT confirmed (self-execute fallback): log the self-execute activation. Self-execute schedule: June 10 outline, June 14 first sections, June 24 first-draft checkpoint. This is independent of Wave 1+2 editorial — do not let author status delay editorial.

**Time budget: 2 hours**

### 09:00-17:00 UTC: Wave 1+2 Editorial Sprint Begins

The editorial work for Wave 1+2 is 4-6 hours total. Spread it across June 1-3 to avoid single-day overload.

**June 1 editorial tasks (2-3 hours today):**
- [ ] Open all five Wave 1+2 documents. Run placeholder scan on each
- [ ] Standardize YAML frontmatter: confirm `title`, `phase`, `wave`, `status: PRODUCTION-READY`, `created` fields are present and consistent across all five documents
- [ ] Add `wave_3_announcement` field to each document's frontmatter: `wave_3_announcement: "Volume 2: Practical Operations (food preservation, water systems, healthcare offline, fuel production) — releasing June 28-30"`
- [ ] Draft distribution announcement for Wave 1+2 (one paragraph: what this corpus covers, who it is for, where to find Volume 2)

**Do not** attempt to complete all editorial work today. Pace is 2-3 hours/day June 1-3.

**Time budget: 2-3 hours (editorial)**

### 17:00 UTC: T+0 Day-End Check

- [ ] Pre-flight complete and logged?
- [ ] Author briefings sent (or self-execute logged)?
- [ ] Phase 6 research agents dispatched?
- [ ] Editorial sprint started (frontmatter check done)?
- [ ] WORKLOG.md updated

**Author response window note**: Expect 70-80% same-day email responses. Non-responsive Phase 6 authors get one follow-up at T+1 09:00 UTC. Non-response at T+1 17:00 UTC activates CT-1 (see PHASE_5_WAVE_1_UNIFIED_RISK_TRIGGER_RUNBOOK.md, RT-2).

**Total time budget June 1: 6-8 hours**

---

## June 2 (Tuesday) — T+1: Orientation and Editorial Continuation

### 08:00 UTC: First Daily Standup Prompt (Phase 6 Authors)

Send daily standup prompt (template in PHASE_5_WAVE_1_EXECUTION_TEMPLATES.md, June 2 pre-filled). Responses needed by 12:00 UTC.

**T+1 standup focus**: Author understanding confirmed, not output. Are they reading orientation documents? Do they have access to sources? Any questions before outlining begins?

**Time budget: 15 minutes**

### 09:00 UTC: Author Follow-Up (if T+0 non-responders)

For any Phase 6 author who did not acknowledge the T+0 briefing email: send one follow-up. Subject: "Phase 6 [Domain] — confirming receipt of June 1 briefing." If no response by T+1 17:00 UTC, activate RT-2 (author unavailability).

### 09:00-13:00 UTC: Wave 1+2 Editorial Continuation (2 hours today)

- [ ] Complete cross-document consistency check: do all five documents use the same terminology for core concepts (community resilience, Zone 5, governance, mutual aid)?
- [ ] Identify and resolve any inconsistencies found. The orchestrator makes the call and edits directly.
- [ ] Verify citation formatting consistency across all five documents (any format acceptable; goal is internal consistency, not journal-specific formatting)

**Time budget: 2 hours (editorial)**

### 12:00 UTC: Standup Replies Processed

- [ ] Read all Phase 6 author replies
- [ ] Log each domain status in daily standup log (template in PHASE_5_WAVE_1_EXECUTION_TEMPLATES.md)
- [ ] Identify and escalate any Tier 1 or Tier 2 blockers. Respond to blockers before 16:00 UTC

**Time budget: 30 minutes**

### 16:00 UTC: Blocker Response Deadline

All Tier 1 and Tier 2 blockers resolved or escalation path confirmed. Log in WORKLOG.md.

**Expected output at T+1 EOD**: Phase 6 authors oriented, no writing expected. Wave 1+2 editorial 50-60% complete (frontmatter standardized, cross-document consistency checked). Peer reviewer introductions sent.

**Total time budget June 2: 3-4 hours**

---

## June 3 (Wednesday) — T+2: Editorial Completion and Phase 6 Research Kit Verification

### 08:00 UTC: Daily Standup Prompt (pre-filled June 3 template)

### 09:00-12:00 UTC: Wave 1+2 Editorial Final Pass [CRITICAL PATH]

This is the last editorial day. Target: Wave 1+2 is fully publication-ready by 17:00 UTC today.

- [ ] Final read-through of each document (skim, not deep read — 20-30 minutes per document)
- [ ] Confirm: zero placeholder markers in all five documents
- [ ] Confirm: Wave 3 announcement language present in each document or in master distribution note
- [ ] Confirm: consistent heading structure (H1 title, H2 sections, H3 subsections throughout)
- [ ] Commit all editorial changes to master: `git add projects/systems-resilience/phase-5-wave-2*.md && git commit -m "chore(phase5): Wave 1+2 editorial pass complete — Option A June 3"`

**Decision gate >**: Wave 1+2 editorial complete? If yes: proceed to publication preparation. If any document still has placeholder markers or frontmatter gaps: resolve before committing. Do not proceed to publication with any document below editorial standard.

**Time budget: 3 hours (editorial)**

### 12:00-14:00 UTC: Phase 6 Research Kit Verification

- [ ] Confirm each Phase 6 author (or self-execute) has accessed their research kit (20+ pre-staged sources, model document, domain candidate file)
- [ ] Any inaccessible sources flagged by authors or research agents? Substitute within 4 hours
- [ ] Fast-track Phase 6 domain authors (Economic Resilience, Infrastructure Interdependencies if selected): confirm they have begun outlining Section 1

**Time budget: 1 hour**

### 14:00 UTC: Publication Preparation Begins

- [ ] Create distribution list for Wave 1+2 publication (Tier 1: direct practitioner contacts, Tier 2: network organizations, Tier 3: broad community channels)
- [ ] Draft publication announcement (one paragraph per audience tier — Tier 1 is personalized, Tier 2 is tailored, Tier 3 is broadcast)
- [ ] Schedule publication send for June 5 (2 days buffer from today)

**Expected output at T+2 EOD**: Wave 1+2 editorial complete and committed. Phase 6 authors have confirmed source access. Fast-track Phase 6 domains have begun outlining.

**Total time budget June 3: 4-5 hours**

---

## June 4 (Thursday) — T+3: Phase 6 Outline Review Gate

### 08:00 UTC: Daily Standup Prompt (pre-filled June 4 template)

### 09:00 UTC: Publication Announcement Final Review

- [ ] Read draft Wave 1+2 announcement. Is it practitioner-facing (not academic)? Does it name what problems the corpus solves? Does it announce Wave 3 ("coming June 28-30")?
- [ ] Confirm distribution channels ready to receive content June 5

### 11:00 UTC: Phase 6 Outline Submission Deadline Reminder

Send reminder to all Phase 6 authors: "Outline due today by 17:00 UTC. Submit to [channel]. Format requirements in PHASE_6_AUTHOR_ONBOARDING_KIT.md section 4."

### 17:00 UTC: Phase 6 Outline Submissions Due [CRITICAL PATH]

All Phase 6 domain authors must submit section-by-section outlines by 17:00 UTC.

**Outline requirements (per domain)**:
- 8-12 major sections identified
- Each section: 2-3 sentence scope description, primary sources assigned (minimum 3 per section), estimated word count (4,000-6,000 words/section)
- Total target word count stated explicitly
- One Zone 5 or community-context implication note per section
- Integration points with other Phase 6 domains noted

**Decision gate >**: If an outline is not received by 17:00 UTC: send one follow-up. If no response by T+4 09:00 UTC: activate RT-2 (author unavailability). Log immediately.

### 17:00-20:00 UTC: Outline Review Begins

Orchestrator begins reviewing received outlines. Evaluate each against:
- [ ] Does it cover the core research questions from the domain candidate file?
- [ ] Is Zone 5 or community context grounded in each section?
- [ ] Are integration points with other Phase 6 domains realistic?
- [ ] Is scope boundary held? No Phase 5 re-coverage, no scope overlap with other Phase 6 domains?
- [ ] Is word count per section proportionate to research depth?

**Outline review SLA**: Return feedback by T+4 12:00 UTC (next day noon). Feedback options: (A) Approved, (B) Approved with minor notes (author proceeds), (C) Revision required (resubmit by T+5 EOD).

**Expected output at T+3 EOD**: All Phase 6 domain outlines submitted. Orchestrator outline review in progress. Wave 1+2 publication imminent (June 5).

**Total time budget June 4: 3-4 hours**

---

## June 5 (Friday) — T+4: Publication Day and Outline Feedback

### 06:00-09:00 UTC: Wave 1+2 Publication [CRITICAL PATH]

This is the primary external-facing action of Option A. Execute with care.

- [ ] Send Wave 1+2 Tier 1 distribution emails (personalized; use names from distribution list)
- [ ] Send Wave 1+2 Tier 2 network distribution (tailored by network type)
- [ ] Post Wave 1+2 Tier 3 broadcast (community channels, mailing lists)
- [ ] Log publication timestamp: "Wave 1+2 published June 5 [TIME] UTC. 43,621 words. 5 documents. Distribution: [N] Tier 1 contacts, [N] Tier 2 organizations, [N] Tier 3 channels."
- [ ] Commit publication event log to WORKLOG.md

**Decision gate >**: If any Wave 1+2 document fails a last-minute review (discovered placeholder, formatting failure), delay only that document by 24 hours. Do not hold the entire publication. Log the delay. The other four documents publish on schedule.

**Time budget: 2-3 hours**

### 10:00-12:00 UTC: Phase 6 Outline Feedback Sent

- [ ] Send outline feedback to all Phase 6 authors by 12:00 UTC
- [ ] Authors with "approved" or "approved with minor notes": begin Section 1 writing today
- [ ] Authors with "revision required": resubmit by T+5 (June 6) EOD; do not begin writing until revision is approved
- [ ] Fast-track domains (Economic Resilience, Infrastructure Interdependencies): Section 1 first draft expected by T+5 EOD (4,000-6,000 words)

**Time budget: 2 hours**

### 13:00 UTC: Option A Monitoring Mode Begins

Wave 1+2 editorial work is complete. The orchestrator drops to passive monitoring for Wave 1+2:
- 15 minutes per day reading reader responses
- Flag any substantive feedback that would affect Wave 3 content for the June 15-27 Wave 3 editorial pass
- No active editorial work required June 5-14 on Wave 1+2 content

**Orchestrator bandwidth freed up June 5-14**: 10-15 hours/week previously locked by editorial work now available for Phase 6 domain review, author feedback cycles, and author onboarding continuation.

**Expected output at T+4 EOD**: Wave 1+2 published. Phase 6 outlines reviewed and feedback returned. Fast-track Phase 6 authors writing Section 1. Orchestrator in monitoring mode for Wave 1+2.

**Total time budget June 5: 5-6 hours**

---

## June 6 (Saturday) — T+5: Wave 2 Domain Ramp (Phase 6)

### 08:00 UTC: Daily Standup Prompt (pre-filled June 6 template)

### 09:00-11:00 UTC: Wave 2 Phase 6 Domain Onboarding

Wave 2 Phase 6 domains (Ecosystem Restoration, Institutional Learning, or whichever domains are in the secondary wave) begin their orientation today.

- [ ] Send Wave 2 Phase 6 domain author briefing emails (same template as T+0, dated June 6)
- [ ] Deliver Wave 2 domain research kits
- [ ] Wave 2 authors begin orientation reading

**Time budget: 2 hours**

### 11:00-13:00 UTC: Wave 1+2 Reader Response Monitoring

- [ ] Read any reader responses to June 5 Wave 1+2 publication
- [ ] Categorize feedback: (A) Positive/no action, (B) Factual correction needed, (C) Scope addition requested, (D) Wave 3 content suggestion
- [ ] Log Category B and C items for Wave 3 editorial pass (June 15-27). Do not act on them now.

### 14:00-17:00 UTC: Phase 6 Fast-Track Domain Progress Check

- [ ] Confirm fast-track Phase 6 domain authors have completed Section 1 outline and begun writing
- [ ] Word count check: where are they?
- [ ] Any blockers reported via standup? Resolve by 17:00 UTC

**Expected output at T+5 EOD**: Wave 2 Phase 6 domain authors oriented. Fast-track Phase 6 domains have Section 1 writing underway (target: 4,000-8,000 words delivered). Wave 1+2 reader feedback categorized.

**Total time budget June 6: 2-3 hours**

---

## June 7 (Sunday) — T+6: Week 1 Status Review

### 08:00 UTC: Weekly Sync Prompt (pre-filled June 7 template)

This is the end-of-week review, not a daily standup. Responses due by 17:00 UTC. Use the Weekly Sync format from PHASE_5_WAVE_1_EXECUTION_TEMPLATES.md.

### 17:00 UTC: Week 1 Wave-Level Status Review

Compile all weekly sync responses and produce wave-level summary:

- [ ] Word count per Phase 6 domain at T+6 EOD (target for fast-track domains: 8,000-12,000 words in draft)
- [ ] Citation count per domain (target: 20+ citations integrated in submitted sections)
- [ ] Peer reviewer confirmations: each domain's reviewer has confirmed availability for T+10-T+12 window
- [ ] Any scope drift detected in submitted sections?
- [ ] Resource contention check: any domain requiring orchestrator research support blocking author progress?
- [ ] Wave 2 Phase 6 domain authors on track for T+8 outline submission?

**Scope-creep early-warning check**: Compare each author's reported sections-in-progress against their approved outline. Any section not in the outline is a scope flag — log immediately, investigate Monday morning.

### 18:00 UTC: WORKLOG Update

Log T+6 status in WORKLOG.md. This is the last log entry before the June 8 mid-wave checkpoint.

**Expected output at T+6 EOD**: Week 1 wave-level status known. Phase 6 fast-track domains have 8,000-12,000 words in draft. All peer reviewer confirmations received. Any scope-creep flags documented.

**Total time budget June 7: 2-3 hours**

---

## June 8 (Monday) — T+7: Mid-Wave Checkpoint (First-Draft Gate) [CRITICAL PATH]

> **Why June 8 is the checkpoint**: June 8 is day 7 of the sprint. It is the first moment where enough writing exists to assess whether trajectory is on track. The outline-review cycle closed on June 5; all authors are now in active writing mode. At T+7, fast-track domains have had 3-4 full writing days, and the first 8,000-15,000 words are visible. Early enough to course-correct without cascading delays; late enough that the data is meaningful.

### 06:00 UTC: Mid-Wave Checkpoint Notice

Send to all Phase 6 authors: "Today is the T+7 mid-wave checkpoint. First-draft package due by 12:00 UTC. See onboarding kit section 5 for submission format."

### 12:00 UTC: First-Draft Submissions Due [CRITICAL PATH]

All fast-track and secondary Phase 6 domain authors submit first-draft package by 12:00 UTC.

**Submission package requirements**:
1. Draft sections delivered (minimum 2 sections, 8,000-15,000 words)
2. Citation log (running bibliography, any format)
3. Status note (3-5 sentences): sections complete, in progress, research gaps, scope questions
4. Word count projection: will the full document be complete by June 15 (T+14)? If not, what is the realistic date?

### 12:00-17:00 UTC: Mid-Wave Assessment

Evaluate each draft against the Research Quality Threshold (from PHASE_6_WAVE_1_EXECUTION_CHECKLIST.md T+7 section):

**Pass criteria (all must be met)**:
- [ ] Word count on track: ≥50% of section targets met, or credible projection to June 15 completion
- [ ] Citation depth adequate: ≥15 distinct source citations in submitted sections; no section over 3,000 words with fewer than 5 citations
- [ ] Zone 5 / community context present: at least 2 sections show specific community application
- [ ] Practitioner voice consistent (compare against Phase 5 model documents as calibration reference)
- [ ] No major scope violations

**At-risk indicators** (one trigger = amber; two triggers = escalate):
- Total submitted word count under 5,000 without explanation
- Fewer than 10 distinct citations in submitted sections
- No Zone 5 or community context in any section
- Voice has drifted significantly academic

**Decision gate >**: For each Phase 6 domain, make one of three decisions by T+8 09:00 UTC:

| Decision | Condition | Action |
|----------|-----------|--------|
| Green — proceed | All pass criteria met | Confirm with author; continue at pace |
| Amber — at-risk watch | One at-risk indicator present | 20-minute synchronous call; corrective actions agreed by T+8 EOD |
| Red — escalate | Fail criterion triggered or two+ at-risk indicators | Activate RT-2 or RT-3 per PHASE_5_WAVE_1_UNIFIED_RISK_TRIGGER_RUNBOOK.md |

Log all T+7 gate decisions in WORKLOG.md before end of June 8.

### 17:00-18:00 UTC: Mid-Wave Scope Assessment (Orchestrator Internal)

Answer these three questions and log the answers:
1. **Is scope on track?** Are all domains staying within approved outline boundaries?
2. **Is author engagement healthy?** Standups arriving on time? Word counts growing? No one gone silent?
3. **Is revision burden acceptable?** Authors incorporating feedback without major rewrites?

If all three answers are YES: proceed without changes. If any answer is NO: activate the relevant risk trigger.

**Total time budget June 8: 5-6 hours**

---

## June 9 (Tuesday) — T+8: Feedback Loop Closes

### 08:00 UTC: Daily Standup Prompt (pre-filled June 9 template)

### 09:00 UTC: T+7 Feedback Sent to All Authors [CRITICAL PATH]

- [ ] Send mid-wave feedback to all Phase 6 authors by 09:00 UTC
- [ ] Green authors: no action required; continue writing; no additional checkpoints until T+10
- [ ] Amber authors: 20-minute call today to confirm corrective actions underway; follow up at T+9 17:00 UTC
- [ ] Red authors: contingency protocol activated per PHASE_5_WAVE_1_UNIFIED_RISK_TRIGGER_RUNBOOK.md

### 10:00-13:00 UTC: Wave 2 Phase 6 Domain Outline Reviews

Wave 2 Phase 6 domain authors submit outlines by T+8 17:00 UTC. Same process as T+3-T+4:

- [ ] Confirm Wave 2 outline submissions received by 17:00 UTC
- [ ] Review and return feedback by T+9 12:00 UTC
- [ ] Wave 2 authors with approved outlines begin Section 1 writing June 10

### 14:00-17:00 UTC: Peer Review Queue Preparation

Begin preparing peer review queue so reviewers are ready to receive material at T+10.

- [ ] Confirm each peer reviewer's availability for June 11-13 review window
- [ ] Send peer reviewers the structured review template (Section 3 from PHASE_6_COORDINATION_TEMPLATES.md)
- [ ] Brief peer reviewers: 2-3 sentence domain summary + specific review criteria
- [ ] Identify any peer reviewer conflicts: if a reviewer is unfamiliar with Zone 5 context, pair with a Zone 5 practitioner for a 15-minute orientation call

**Mid-wave production targets at T+8 EOD**:
- Fast-track Phase 6 domains: 60-70% of full document in draft
- Secondary Phase 6 domains: 40-50% of full document in draft
- Wave 2 Phase 6 domains: outlines approved; Section 1 writing begun

**Total time budget June 9: 3-4 hours**

---

## June 10 (Wednesday) — T+9: Peer Review Queue Confirmed

### 08:00 UTC: Daily Standup Prompt (pre-filled June 10 template)

### 09:00-12:00 UTC: Peer Review Queue Final Confirmation [CRITICAL PATH]

By June 10 all peer reviewers must be confirmed. No peer reviewer confirmed at this point means activating backup immediately (do not wait until T+10).

- [ ] Confirm each peer reviewer's availability: June 11 receive, June 13 return by 17:00 UTC
- [ ] Send peer reviewers the structured review template
- [ ] Brief peer reviewers on domain scope
- [ ] Identify backup reviewers for each domain (in case primary cannot complete)
- [ ] Log peer review tracking table in WORKLOG.md (template in PHASE_5_WAVE_1_EXECUTION_TEMPLATES.md, Section 3)

### 12:00-17:00 UTC: Author Production (Monitoring)

All Phase 6 authors continue writing. Orchestrator is in monitoring mode — respond to blockers only.

**Standup focus on T+9**: Are authors tracking their own word count? Any sections ready to send to peer reviewers ahead of the T+10 gate?

### 14:00 UTC: Wave 3 Reader Feedback Integration Note

Review the categorized Wave 1+2 reader feedback collected since June 5. For any Category B or C items:
- [ ] Create a brief note for the Wave 3 editorial pass: what should Wave 3 address that Wave 1+2 readers have flagged?
- [ ] Do not act on this now. File it as an input to the June 15-27 Wave 3 editorial pass.

**Expected output at T+9 EOD**: All peer reviewers confirmed. Backup reviewers identified. All Phase 6 authors in active production. Wave 3 reader feedback noted for later editorial pass.

**Total time budget June 10: 3-4 hours**

---

## June 11 (Thursday) — T+10: Peer Review Begins

### 06:00-12:00 UTC: Draft Submissions to Peer Review [CRITICAL PATH]

All fast-track and secondary Phase 6 domain authors submit their current draft for peer review by 12:00 UTC.

**Peer review submission package per domain**:
1. Current draft (clearly mark [IN PROGRESS] on unfinished sections)
2. Domain scope summary (1 paragraph)
3. Three specific questions for the peer reviewer (sections where targeted feedback is wanted)
4. Citation list (informal format acceptable; formatting verified at T+14)

### 12:00 UTC: Peer Review Triage

Route each domain's draft to confirmed peer reviewer. Each reviewer receives:
- Submission package
- Structured review template (from PHASE_6_COORDINATION_TEMPLATES.md)
- Confirmed return deadline: June 13 17:00 UTC
- Author contact information (for clarifying questions)

Update peer review tracking table: note submission timestamp and word count at submission.

### 13:00-17:00 UTC: Production Continues During Review Window

Authors continue writing in unreviewed sections. Peer review is not a blocking gate for production — it is a parallel track.

**Monitoring**: Any peer reviewer questions that arrive today: route to authors within 2 hours.

**Total time budget June 11: 3-4 hours**

---

## June 12 (Friday) — T+11: Production and Peer Review in Parallel

### 08:00 UTC: Daily Standup Prompt (pre-filled June 12 template)

### 09:00 UTC: Wave 3 Editorial Pass Planning

With Wave 1+2 monitoring ongoing and Phase 6 production continuing, begin planning the Wave 3 editorial pass (starts June 15).

- [ ] List any reader feedback items from the June 5 Wave 1+2 publication that should inform Wave 3
- [ ] Identify which Wave 3 documents require cross-references to Wave 1+2 content
- [ ] Estimate Wave 3 editorial hours: target 8-12 hours across June 15-27

### 12:00 UTC: Mid-Window Reviewer Check

Send to all peer reviewers: "You're halfway through the review window. Any questions about the template or the domain? Still on track for June 13 17:00 UTC?" Any reviewer who does not reply by 17:00 UTC is elevated to WATCH status — activate backup if no response by June 12 17:00 UTC.

### 10:00-17:00 UTC: Production and Peer Review Monitoring

All Phase 6 authors writing. Orchestrator monitoring:
- [ ] Any peer reviewer delays signaled? If so, activate backup immediately
- [ ] Any author word counts declining compared to T+6-T+8? Flag as burnout signal, address directly

**Expected output at T+11 EOD**: Phase 6 production at 40-60% of target word count for all domains. Peer reviews in progress. Wave 3 editorial plan drafted.

**Total time budget June 12: 2-3 hours**

---

## June 13 (Saturday) — T+12: Peer Reviews Due

### 09:00 UTC: Peer Review Reminder

Send one reminder to all peer reviewers: "Peer review due today by 17:00 UTC. Please reply with any questions now if you need clarification on the review template."

### 12:00 UTC: Daily Standup Prompt (pre-filled June 13 template)

### 17:00 UTC: Peer Review Returns Deadline [CRITICAL PATH]

All peer reviews due by 17:00 UTC.

**If a peer review is not returned by 17:00 UTC**:
- Activate RT-4 (peer review bottleneck) per PHASE_5_WAVE_1_UNIFIED_RISK_TRIGGER_RUNBOOK.md
- Contact backup reviewer immediately
- Begin orchestrator internal review using structured template (2-3 hours per domain)

### 17:00-23:00 UTC: Peer Review Integration

For each received review:
1. Read and classify each item: (M) Mandatory, (A) Advisory, (D) Disputed
2. Prioritize: corrections and citation requests are mandatory for T+14; scope concerns are advisory
3. Send consolidated feedback to each author by 23:00 UTC

**Total time budget June 13: 3-4 hours**

---

## June 14 (Sunday) — T+13: Integration Sweep

### 08:00 UTC: Daily Standup Prompt (pre-filled June 14 template) — FINAL STANDUP

This is the final daily standup of Wave 1. Standup focus: mandatory peer review items addressed, completion status, publication readiness self-assessment.

### 09:00-17:00 UTC: Author Integration Tasks

Each Phase 6 author:
- [ ] Addresses all mandatory peer review items (factual corrections, citation gaps)
- [ ] Completes any remaining unfinished sections (minor gaps acceptable if flagged with [CITATION NEEDED])
- [ ] Runs placeholder scan: grep for [, TODO, TBD, fill, NEEDS in their document — resolve what is resolvable
- [ ] Cross-reference check: verify any references to other Phase 6 domains point to correct file and section
- [ ] Final word count confirmation: document should be at 60-90% of target word count by today EOD (below 60% triggers scope conversation)

### 09:00-12:00 UTC: Orchestrator T+13 Tasks

- [ ] Track all Phase 6 domains against publication readiness matrix (Section 4 of PHASE_6_COORDINATION_TEMPLATES.md)
- [ ] Identify any domains likely to miss T+14 gate — begin contingency scope adjustment conversation now
- [ ] Cross-domain consistency check: do all domain documents use consistent terminology for foundational concepts?
- [ ] Prepare T+14 gate agenda

### 13:00 UTC: Wave 1+2 Ongoing Reader Response Review

Quick review of any Wave 1+2 reader responses received June 5-13. Compile into Wave 3 editorial notes. No action today; file for June 15-27.

**Total time budget June 14: 2-3 hours**

---

## June 15 (Monday) — T+14: Publication-Readiness Gate [CRITICAL PATH]

### 08:00-17:00 UTC: Publication Readiness Assessment

Orchestrator completes publication readiness assessment for each Phase 6 domain using the 9-criterion rubric from PHASE_6_COORDINATION_TEMPLATES.md Section 4.

- [ ] Complete assessment for all confirmed Phase 6 domains
- [ ] Score each criterion (0, 0.5, or 1.0)
- [ ] Total score per domain (minimum 7.0/9.0 for publication readiness)

### 12:00 UTC: Domains at ≥7.0 Confirmed

- [ ] Confirmed domains: notify author, process milestone payment, commit final document to master
- [ ] Domains at 6.0-6.9 (conditional readiness): list close-out items, agree on completion timeline with author (target: within 5 business days)
- [ ] Domains below 6.0: scope adjustment meeting scheduled within 24 hours

### 17:00 UTC: Wave 1 Completion Log

Update WORKLOG.md and ORCHESTRATOR_STATE.md:

```
Phase 6 Wave 1 complete — T+14 June 15 2026
Domains completed: [N]/[N-selected]
Publication readiness scores:
  Economic resilience: [X.X]/9
  Infrastructure interdependencies: [X.X]/9
  International coordination: [X.X]/9
  Intergenerational transmission: [X.X]/9
  Ecosystem restoration: [X.X]/9
  Institutional learning: [X.X]/9
Domains at conditional readiness: [list]
Wave 1 complete. Wave 3 editorial pass begins June 15.
```

### 17:00 UTC: Wave 3 Editorial Pass Activation

- [ ] Open Wave 3 editorial plan (built June 12)
- [ ] Confirm June 15-27 editorial hours available (8-12 hours total)
- [ ] Activate Wave 3 editorial sprint — first editorial pass begins today

**Total time budget June 15: 5-6 hours**

---

## Post-Wave-1: June 15-30 Summary (Option A Continuation)

| Date | Activity | Hours |
|------|----------|-------|
| June 15-27 | Wave 3 editorial pass (cross-references to Wave 1+2 added, reader feedback incorporated) | 8-12 hrs |
| June 15-27 | Phase 6 conditional domain close-out (if any) | 2-4 hrs |
| June 15-27 | Phase 6 Domains E/F/H second-wave activation decision | 2-3 hrs |
| June 20-25 | Author production monitoring (first-draft checkpoint if author is engaged) | 2-3 hrs |
| June 28-30 | Wave 3 published (22,821 words) | 2-3 hrs |
| June 28-30 | Phase 4 6-month viability test checklist initiated | 1 hr |
| July 10 | Author draft delivery (HIGH confidence: 85%) | — |

---

## Critical Path Summary

The following days have zero slack — a delay on any of these cascades:

| Date | Critical Path Item | Consequence of slip |
|------|--------------------|-------------------|
| June 1 06:00 UTC | Pre-flight complete; activation logged | Author briefings delayed; Phase 6 agents not dispatched on time |
| June 3 17:00 UTC | Wave 1+2 editorial complete and committed | Publication on June 5 at risk; buffer consumed |
| June 5 06:00-09:00 UTC | Wave 1+2 published | Option A's first gate. If slip >2 days, Wave 3 reader-feedback window shrinks |
| June 8 12:00 UTC | First-draft submissions received | Mid-wave assessment cannot proceed; Red domains go undetected until T+10 |
| June 10 12:00 UTC | All peer reviewers confirmed | If any reviewer is unconfirmed at T+9, backup must be activated same day |
| June 11 12:00 UTC | All Phase 6 draft submissions sent to peer review | 48-hour review window requires on-time send |
| June 13 17:00 UTC | Peer reviews returned | Feedback cannot be integrated without reviews; T+14 gate compromised |
| June 15 17:00 UTC | T+14 publication readiness gate | Wave 1 close. Conditional domains begin close-out. Wave 3 editorial starts. |

Days with buffer (can slip 1 day without cascade): June 2, June 6, June 7, June 9, June 12, June 14

---

*This timeline is production-ready. Open it June 1 06:00 UTC and execute each day's tasks in order. Log decisions and gate outcomes in WORKLOG.md at each milestone. Reference PHASE_5_WAVE_1_CRITICAL_PATH_ANALYSIS.md for dependency visualizations and PHASE_5_WAVE_1_UNIFIED_RISK_TRIGGER_RUNBOOK.md when any risk trigger fires.*
