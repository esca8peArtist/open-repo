---
title: "Week 1 Contractor Onboarding Checklist — June 29–July 6, 2026"
date: 2026-06-28
version: 1.0
status: production-ready
activation: June 29 or June 30, upon first contractor confirmation
day-1-options: June 29 (if ACCEPT received June 28 EOD) or June 30 (if CONDITIONAL resolves June 29)
escalation-trigger: No response by July 1 → backup activation
success-criteria: All confirmed contractors have submitted first sample (photography) or content outline (writers) by June 30 EOD
cross-references:
  - CONTRACTOR_ONBOARDING_AUTOMATION_LOGIC.md (ACCEPT / CONDITIONAL / ESCALATE routing)
  - PHASE_3_CONTRACTOR_ONBOARDING_WORKFLOW.md (6-phase lifecycle)
  - PHASE_3_CONTRACTOR_COMMUNICATION_TEMPLATES.md (email templates)
  - PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md (tracking grid)
tags: [seedwarden, phase-3, contractor, onboarding, week-1, checklist]
---

# Week 1 Contractor Onboarding Checklist

**Activation**: Day 1 begins the morning after a contractor confirms (signs contract + deposit received).
- If ACCEPT confirmed June 28 EOD: Day 1 is June 29
- If CONDITIONAL resolves June 29: Day 1 is June 30
- Day 1 is never delayed past June 30 for any confirmed contractor

**Week 1 span**: Day 1 (June 29 or 30) through Day 7 (July 5 or 6, depending on start date)

---

## Day 1 — Welcome, Access, and Onboarding Kit Delivery

**Owner**: User
**Target time**: Complete all Day 1 items before 17:00 UTC on Day 1

### Communications (Day 1)

- [ ] **Welcome email sent** — use `PHASE_3_CONTRACTOR_COMMUNICATION_TEMPLATES.md` (Template 1 — Offer Email adaptation for post-signature welcome). Customize:
  - "Welcome to Phase 3" opener with their specific track named
  - "Your first deliverable is due [DATE] — the onboarding kit will give you everything you need"
  - "Reply to confirm you received this email and the onboarding kit attachments"

- [ ] **Slack channel invite sent** — invite contractor to dedicated Seedwarden Phase 3 Slack workspace
  - Channel naming: `#photo-[first-name]`, `#writer-[first-name]`, `#specialist-[first-name]`
  - Post Day 1 message in their channel: "Welcome. Your onboarding kit is in email. Reply here once you've had a chance to review. Any questions about the materials, ask in this channel."
  - If contractor does not use Slack: agree on WhatsApp or email as primary async channel — log the preference in WORKLOG.md

- [ ] **Google Drive folder permissions granted**
  - Shared folder: `Seedwarden-Phase3/[ContractorName]/`
  - Photographer: read access to Canva brand kit export folder; write access to their image delivery folder
  - Writer: read/write access to content outline Google Doc for their bundles
  - Specialist: read/write access to writer draft Google Docs for annotation comments

- [ ] **Dropbox link sent** (if applicable for large file delivery)
  - Photographers only: provide shared Dropbox folder link for high-resolution image delivery (Google Drive has 15GB limit issues for large uncompressed files)
  - Folder: `Seedwarden-Phase3-Photos/[PhotographerName]/Session-1/`

### Onboarding Kit Delivery (Day 1)

Send via email and Slack/async channel simultaneously. All kit items below.

**All contractors (required)**:
- [ ] Project brief PDF (export of `PHASE_3_CONTRACTOR_PREBID_MATERIALS.md`)
- [ ] Sprint calendar with their deliverable dates highlighted (export relevant rows from `PHASE_3_LAUNCH_CALENDAR.md`)
- [ ] First milestone due date in plain text: "Your first deliverable is due [DATE]. That is [X] calendar days from today."
- [ ] Primary contact info: user name, email, Slack handle, and reply-within windows ("I reply to Slack within 4 hours during working hours; email within 12 hours")

**Photographers (additionally)**:
- [ ] Shot list for Session 1 (which bundle, which herbs, which shot types)
- [ ] Canva Phase 3 brand guidelines PDF (hex codes, surface standards, diffuse lighting spec)
- [ ] Naming convention sheet: `[bundle-slug]-[image-type]-[sequence].jpg` with examples
- [ ] Etsy attribution protocol: "Photography by [Your Name] — [portfolio link]" — confirm the exact format they want credited

**Writers (additionally)**:
- [ ] Content outline Google Doc link for their bundle(s) — confirm they can access and comment
- [ ] FTC Quick Reference one-pager PDF (evidence-tier language, mandatory disclaimer positions, never-use claim examples)
- [ ] CITES sidebar verbatim text (Goldenseal, Immunity bundle only) — labeled "DO NOT PARAPHRASE — paste verbatim"
- [ ] Bundle word count summary card:
  - Respiratory: 3,600 words total (breakdown by section in the outline doc)
  - Immunity: 3,800 words total
  - Digestive: 3,600 words total
  - Minimum per-bundle for first draft: 85% of target (Resp: 3,060; Immunity: 3,230; Digestive: 3,060)
- [ ] Echinacea species clarification note: "When writing Echinacea sections — E. purpurea and E. angustifolia are separate species with different conservation status. E. angustifolia requires the UpS At-Risk sidebar. Do not merge them."

**Habitat Specialists (additionally)**:
- [ ] Species scope list for their track (specific bundles and species sections requiring habitat review)
- [ ] Permission forms checklist PDF (UpS At-Risk protocol acknowledgment, land access forms if field scouting)
- [ ] Source citation protocol sheet: "Each habitat claim cites one of: USDA PLANTS, NatureServe, iNaturalist verified observations, UpS At-Risk documentation"
- [ ] Annotation delivery format: "Add comments directly to the writer's Google Doc. Do not create a separate document."

### Day 1 WORKLOG.md Entry (required before Day 1 ends)

```
## [Contractor Name] — [Track] — Day 1 Onboarding — [DATE]
Status: Contract signed. Deposit $[X] sent [DATE/TIME].
Onboarding kit sent: [TIME]
Slack channel created: Yes/No — channel name: [#channel]
Google Drive access granted: Yes/No
Dropbox access granted: Yes/No (photographers only)
Contractor kit acknowledgment received: Yes/No
Notes: [Any Day 1 issues or adjustments]
```

---

## Day 2 — Initial Submission Check-In Call

**Owner**: User
**Format**: 15 minutes per contractor (separate calls, same day)
**Target**: Complete all Day 2 check-in calls before 18:00 UTC on Day 2

### Check-In Call Agenda (15 min, fixed)

| Segment | Duration | Purpose |
|---|---|---|
| Kit review | 5 min | "Any questions about the onboarding kit materials?" |
| First deliverable clarification | 5 min | "I want to confirm your first deliverable date is [DATE] — does that work with what you now know about the scope?" |
| Blocker check | 3 min | "Is there anything you need from me to start today?" |
| Confirm contact protocol | 2 min | "Best way to reach you if something comes up — Slack or email? And what is your expected response time?" |

### Track-Specific Clarification Points (add to call agenda for each track)

**Photographers**: Confirm which herbs they can source locally vs. need shipped. If any species cannot be sourced by July 2 (3 days before Session 1 date), discuss substitution procedure or user shipping specs.

**Writers**: Confirm which bundles they are covering (resolve any Immunity bundle assignment ambiguity before this call — per Item 132 audit, Adrian White vs. Rebecca Lexa Immunity scope must be resolved). Confirm they have read and understood the FTC Quick Reference.

**Habitat Specialists**: Confirm available field survey dates for July 1–20. Discuss any permit or access form issues that may delay field work start.

### Day 2 Check-In Non-Response Protocol

If a contractor does not reply to schedule the Day 2 check-in call within 24 hours of Day 1 kit delivery:
- Send Slack + email: "Following up to schedule a 15-minute check-in call for [DATE]. Here are three time options: [slots]. Please pick one or suggest another time today."
- If no response within 48 hours of kit delivery: flag as elevated risk in WORKLOG.md. This is not yet a crisis — Day 3–5 first sample submission is the real signal.

### Day 2 WORKLOG.md Entry

```
## [Contractor Name] — Day 2 Check-In — [DATE]
Call completed: Yes/No
Call duration: [X] minutes
Kit questions: [Any]
First deliverable date confirmed: Yes/No
Blockers identified: Yes/No — [if yes: describe and resolution]
Contact protocol agreed: Slack/Email, response window [X] hours
Notes: [Anything material]
```

---

## Days 3–5 — First Sample Submission and Feedback Loop

**Owner**: Contractor (submits); User (reviews and responds)
**Day 3 target**: Contractor begins active work (writing, shooting, reviewing)
**Day 5 target**: First sample or partial deliverable submitted for feedback

### Day 3 — Work Begins

This is the first full working day. No check-in or call required unless a contractor flags a blocker. The Day 3 task for each track:

- **Photographers**: Session 1 scheduled or confirmed scheduled. Herb sourcing confirmed.
- **Writers**: Outline reviewed. First section of Respiratory bundle being drafted. Target by Day 3 EOD: 500+ words in the Google Doc.
- **Habitat Specialists**: Annotation access to writer draft confirmed working. First section review annotated and submitted to the writer's Google Doc.

### Day 4 — Silent Progress Day

No user-initiated contact on Day 4 unless:
1. Contractor messages with a blocker
2. Contractor sends a check-in update (positive signal — no response needed beyond "Thanks, looking good")
3. Contractor goes silent and had flagged a blocker on Day 2 or 3

Day 4 is not an escalation day. Contractors need working time without check-in overhead.

### Day 5 — First Sample Submission (Success Criterion Gate)

**Target for each track**:

- **Photographers**: At least 2 raw or lightly edited images from Session 1 submitted to the shared folder. These are not final — they are a mid-session quality check. User reviews within 24 hours and sends one of three responses:
  - "Looks great — proceed to finishing all 5 images"
  - "One adjustment needed: [specific note]. Please revise Session 1 shots before submitting the full set."
  - "Significant style mismatch — let's get on a 10-minute call today."

- **Writers**: Content outline for their first bundle confirmed complete and at least 1,200 words of the first section drafted in the Google Doc. This is not a polished draft — it is a direction check. User reviews within 24 hours and comments on the Google Doc:
  - Confirm FTC framing is appropriate in the existing draft
  - Flag any species accuracy issues in the draft so far
  - Confirm the section structure matches the outline

- **Habitat Specialists**: At least 3 annotation comments submitted on the writer's draft in Google Docs, each with a primary source citation. User reviews and responds to each comment with: accept / revise / expand.

### Feedback Loop Protocol (Days 3–5)

When user reviews a sample submission:
- Respond within 24 hours. No exceptions — a contractor waiting 48+ hours for feedback on Day 5 will fall behind on Day 7.
- Format: specific, actionable, referenced to the content outline or brand guidelines. Never: "Looks good." Always: "Looks good — proceed to complete Session 1" or "This section is missing the FTC evidence-tier qualifier on the Elderberry claim. Per the Quick Reference: [specific framing]. Please add before completing the section."
- Log the feedback interaction in WORKLOG.md: "[Contractor Name] — Day 5 sample review — [DATE]. Sample received: [time]. User reviewed: [time]. Feedback sent: [time]. Status: Proceed / Revision needed."

---

## Day 7 — Full Team Kick-Off Meeting

**Format**: Video call, all active contractors + user
**Target length**: 45–60 minutes
**Schedule**: Set date and time on Day 1 and confirm during Day 2 check-in calls

### Kick-Off Agenda

| Segment | Duration | Content |
|---|---|---|
| Welcome and introductions | 5 min | Each contractor: name, track, location |
| Sprint overview | 10 min | User walks through the 5-bundle plan, upload schedule, and how photographer / writer / specialist work intersects |
| Week 2 priorities | 10 min | Each contractor confirms their Week 2 delivery target out loud |
| Cross-track coordination | 10 min | Writers: which bundles have Echinacea overlap? Photographers: which bundles need images by which date? Specialists: which writers need your annotations first? |
| FTC and quality standards | 10 min | User reviews the 3 non-negotiables: (1) evidence-tier framing on therapeutic claims, (2) Goldenseal CITES sidebar verbatim, (3) Echinacea angustifolia At-Risk sidebar |
| Q&A and close | 5–10 min | Any questions before Week 2 begins |

### Kick-Off Non-Attendance Protocol

If a contractor cannot attend the Day 7 kick-off call:
- Provide 48-hour advance notice minimum
- Send a written kick-off summary within 24 hours of the call
- Ask for written confirmation they read the summary by the next day

If a contractor gives no notice and is absent: treat as an early dropout signal. Do not escalate immediately, but monitor Day 8 and Day 9 closely for delivery signals.

### Day 7 WORKLOG.md Entry (required)

```
## Full Team Kick-Off — [DATE]
Attendees: [list]
Non-attendees: [list, with reason]
Week 2 delivery targets confirmed:
  - Photographer: [target]
  - Writer: [target]
  - Specialist: [target]
Cross-track dependencies noted:
  - [e.g., "Writer needs Echinacea images from photographer by July 10 for inline placement"]
FTC Q&A: [Any questions raised and answers given]
Notes: [Anything material]
```

---

## Week 1 Success Criteria

These are binary gates — pass or fail. No partial credit.

| Criterion | Pass | Fail |
|---|---|---|
| Photographer: first sample submitted | 2+ images submitted from Session 1 by Day 5 EOD | No submission by Day 5 EOD |
| Writer: content outline confirmed | All bundle outlines acknowledged + 1,200+ words drafted by Day 5 EOD | No draft started by Day 5 EOD |
| Habitat Specialist: first annotations submitted | 3+ annotated comments with citations in Google Doc by Day 5 EOD | No annotations by Day 5 EOD |
| All contractors: Day 2 check-in completed | Call completed by Day 2 EOD | No response to scheduling request by Day 3 |
| All contractors: Slack/async channel active | At least 1 message in channel from contractor by Day 3 | Channel silent through Day 4 |

**If any criterion fails**: See Section — Escalation Triggers below. Do not wait for Day 7 kick-off to address a Day 5 failure.

---

## Escalation Triggers

These are the conditions that require same-day action. They are not weekly-sync topics.

### No response by July 1

If any confirmed contractor (signed contract, deposit received) goes fully silent by July 1 with no submission, no check-in engagement, and no Slack activity:
- Send same-day: "Hi [Name] — following up. We have not heard from you since onboarding. Your first sample is due [DATE]. Please confirm you are on track or let us know if something has come up."
- If no response within 24 hours: activate backup and notify user.
- Log: "[Contractor Name] — silent since onboarding. Backup activation triggered [DATE]."

**Backup activation** (July 1 no-response):
1. Check if any CONDITIONAL contractors from the original roster are still available
2. Post an emergency Upwork listing (same specs as the ESCALATE pathway Step 2)
3. Activate the relevant solo fallback track for this contractor's deliverables
4. Log all three actions with timestamps in WORKLOG.md
5. Notify user: "Contractor [Name] unresponsive since Day 1. Backup search activated. Solo fallback covering [their deliverables] starting today."

### Quality failure at Day 5 sample review

If the Day 5 sample reveals a quality issue that cannot be resolved with a single feedback note:
- Call the contractor same day (do not use async for quality failures)
- Walk through the specific issues on the call
- Agree on a corrected sample submission by Day 6
- If the corrected sample still fails: escalate to the dropout recovery procedure from `PHASE_3_CONTRACTOR_DECISION_TREE.md`

### FTC compliance violation in first draft

If the writer's Day 5 sample includes a direct therapeutic claim (e.g., "Elderberry cures cold and flu" or "Ashwagandha treats anxiety"):
- Do not wait for a weekly sync — respond within 24 hours
- Send the FTC Quick Reference with the specific violating sentence highlighted
- Require a revised passage before any further writing proceeds
- If the writer cannot reframe the claim correctly after two rounds: this is a disqualifying quality issue; activate solo fallback for that writer's bundles

---

## Solo Fallback Integration Note

If any contractor does not onboard successfully in Week 1 (no Day 5 sample, persistent no-response, or quality failure that cannot be remediated), the solo fallback plan from `PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md` covers the gap. Week 1 of the solo fallback schedule begins immediately:

- Women's Health bundle: June 29–July 5 (12 hrs/week, 9 writing hours)
- Day 3 pace gate (July 1 in the June 29 start scenario): Women's Health must be 2,500+ words
- Women's Health upload target: July 6 (adjusted from June 29 due to sprint slip)

The Week 1 onboarding checklist and the solo fallback are parallel tracks — they can run simultaneously. If a contractor onboards cleanly, the solo writing pace slows to admin and monitoring. If a contractor drops, the solo writing pace is already running and absorbs the gap without a lag day.

---

*Prepared: June 28, 2026. Activate on first contractor confirmation (expected June 29–30). Cross-references: CONTRACTOR_ONBOARDING_AUTOMATION_LOGIC.md (response routing), PHASE_3_CONTRACTOR_ONBOARDING_WORKFLOW.md (6-phase lifecycle), PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md (solo fallback integration). Version 1.0.*
