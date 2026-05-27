---
title: "Phase 6 Coordination Templates"
project: systems-resilience
phase: 6
wave: 1
status: PRODUCTION-READY — use June 1 onward
created: 2026-05-27
purpose: "Reusable orchestration templates for sustained Phase 6 Wave 1 execution (June 1–15). Copy-paste ready for standup messages, sync meetings, peer review routing, and publication readiness assessment."
companion_docs:
  - PHASE_6_WAVE_1_EXECUTION_CHECKLIST.md
  - PHASE_6_AUTHOR_ONBOARDING_KIT.md
  - PHASE_6_ACTIVATION_READINESS_CHECKLIST.md
---

# Phase 6 Coordination Templates
## Reusable Orchestration Infrastructure — June 1–15, 2026

> **How to use this document**: Each section is a standalone template. Copy the relevant section into your communication channel of choice (email, Slack, project notes), fill in the bracketed fields, and send. Templates are designed for direct use — minimal editing required.

---

## Section 1: Daily Standup Format

*30-minute async standup. Run every day T+1 through T+14. The orchestrator sends the standup prompt each morning; authors reply within 4 hours. The orchestrator reads all replies, logs blockers, and escalates issues before the working day ends.*

### Daily Standup Prompt (Orchestrator Sends, 08:00 UTC)

```
Phase 6 Wave 1 — Daily Standup [DATE] (T+[N])

Reply to this thread with your update. 5 minutes to write. 
Responses needed by 12:00 UTC.

---

DOMAIN: [your domain]
AUTHOR: [your name]

1. YESTERDAY: What did you complete? (word count, section names)

2. TODAY: What will you work on? (specific sections or tasks)

3. BLOCKERS: Anything stopping you or slowing you down?
   (source inaccessible / scope question / need orchestrator input / other)
   If yes: describe in one sentence. If no: write NONE.

4. MILESTONE STATUS: Are you on track for [NEXT MILESTONE, e.g., "T+7 first-draft checkpoint on June 8"]?
   (YES / AT-RISK / NO — if AT-RISK or NO, add one sentence on why)

5. PEER REVIEW (T+9 onward): Any sections ready to send to your peer reviewer ahead of the T+10 gate?
   (YES — ready to send / NO — not yet)

---
Orchestrator will respond to any blockers by 16:00 UTC.
```

### Daily Standup Log Format (Orchestrator Records)

After collecting replies, the orchestrator logs the day's status in WORKLOG.md:

```
## Daily Standup — [DATE] — T+[N]

| Domain | Words today | Milestone status | Blockers |
|--------|-------------|-----------------|---------|
| Economic resilience | [N] | GREEN/AT-RISK/RED | [blocker or NONE] |
| Infrastructure interdependencies | [N] | GREEN/AT-RISK/RED | [blocker or NONE] |
| International coordination | [N] | GREEN/AT-RISK/RED | [blocker or NONE] |
| Intergenerational transmission | [N] | GREEN/AT-RISK/RED | [blocker or NONE] |
| Ecosystem restoration | [N] | GREEN/AT-RISK/RED | [blocker or NONE] |
| Institutional learning | [N] | GREEN/AT-RISK/RED | [blocker or NONE] |

Blockers requiring orchestrator action:
- [domain]: [blocker description] — action taken: [what orchestrator did]

Escalations:
- [domain]: [escalation trigger] — status: [contingency activated / watch]

Next milestone: [milestone name] at T+[N]
```

### Daily Standup: Blocker Escalation Protocol

When a blocker is reported in a standup, the orchestrator triages within 2 hours:

**Tier 1 blocker (work-stopping):** Source is completely inaccessible with no alternate, author is waiting on orchestrator approval to proceed, or a milestone is at imminent risk (tomorrow's deadline with no realistic path). Response: same-day resolution or explicit contingency activation.

**Tier 2 blocker (work-slowing):** Source is partially accessible, author has a scope question but can work around it pending answer, or a milestone is at risk within 3 days. Response: resolve within 4 hours.

**Tier 3 blocker (watch item):** Author flags a potential issue that is not yet blocking. Response: acknowledge, add to watch list, check again at next standup.

The orchestrator replies to Tier 1 and Tier 2 blockers directly in the standup thread before 16:00 UTC. Tier 3 items are logged and monitored.

---

## Section 2: Weekly Sync Structure

*1-hour sync. Run at T+6 (June 7) and T+13 (June 14). Sync is async by default unless a Red status domain requires synchronous escalation discussion.*

### Weekly Sync Prompt (Orchestrator Sends, Friday 08:00 UTC)

```
Phase 6 Wave 1 — Weekly Sync [DATE] (End of Week [1/2])

This is the weekly wave-level review. Please reply with your section by 
[FRIDAY 17:00 UTC]. I'll compile and respond with the wave-level summary 
and any resource decisions by [SATURDAY 12:00 UTC].

---

DOMAIN: [your domain]
AUTHOR: [your name]

SECTION A — PROGRESS THIS WEEK

Total words written this week: [N]
Cumulative words to date: [N]
Sections completed (list): 
Sections in progress (list):
Sections not yet started (list):
Estimated completion date for full document: [DATE]

SECTION B — QUALITY SELF-ASSESSMENT

Citation count in completed sections: [N]
Zone 5 / community context: present in [N] of [N] completed sections
Any sections where you're uncertain about scope: [Y/N — if Y, describe]
Biggest research gap identified this week: [1-2 sentences or NONE]

SECTION C — CROSS-DOMAIN COORDINATION

Any outputs from other Phase 6 domains that your document depends on:
[describe dependency or NONE]
Any outputs your document produces that other domains may need:
[describe or NONE]
Cross-domain conflicts or framing inconsistencies discovered:
[describe or NONE]

SECTION D — NEXT WEEK PLAN

What sections will you complete next week?
What is your biggest risk to hitting [NEXT MILESTONE DATE]?
Any orchestrator support needed?

---
```

### Weekly Sync: Orchestrator Wave-Level Summary

After collecting replies, the orchestrator produces a wave-level summary. Template:

```
Phase 6 Wave 1 — Week [N] Summary — [DATE]

OVERALL STATUS: GREEN / AT-RISK / RED

PROGRESS SUMMARY:
Total words written this week (all domains): [N]
Cumulative total (all domains): [N] / [TARGET] = [%]%
Domains on track: [list]
Domains at risk: [list]
Domains requiring escalation: [list]

RESOURCE CONTENTION ANALYSIS:
Any two domains competing for the same peer reviewer: [Y/N]
Any two domains competing for orchestrator research time: [Y/N]
Any author burnout signals (declining word counts, late standups): [Y/N]
Resolution actions: [list or NONE]

CROSS-DOMAIN FRAMING CHECK:
Inconsistencies detected between domains: [list or NONE]
Resolved this week: [list or NONE]
Unresolved (carry to next week): [list or NONE]

DECISION GATES THIS WEEK:
[Gate name]: [status — passed / deferred / contingency activated]

NEXT WEEK PRIORITIES:
[Domain]: [specific milestone or action]
[Domain]: [specific milestone or action]

RISK ESCALATION:
[Any risks requiring user decision or input by next sync]: [describe or NONE]
```

### Weekly Sync: Resource Contention Analysis Guide

The orchestrator evaluates four contention categories each week:

**1. Peer reviewer contention**: If two domain documents go to the same peer reviewer simultaneously, negotiate a staggered review schedule. Peer reviewers can handle one in-depth review per 48-hour window. If both domains need review at T+10, stagger: Domain A sends at T+10 06:00, Domain B sends at T+10 18:00. Reviewer returns Domain A by T+12 06:00, Domain B by T+12 18:00. Both still meet the T+12 17:00 integration deadline.

**2. Orchestrator research time**: If two authors simultaneously need the orchestrator to track down inaccessible sources (CT-2 protocol), prioritize by: (a) which domain is closer to its next milestone, (b) which gap is larger (section-level vs. document-level), (c) which domain is at higher risk overall. Document triage decisions in WORKLOG.md.

**3. Source overlap**: If two domains are drawing on the same primary sources (e.g., Elinor Ostrom's commons governance work appears in both Economic Resilience and Institutional Learning), coordinate that both domains cite the same source consistently and do not write contradictory summaries of the same study. A 15-minute author-to-author coordination note resolves most source overlap issues.

**4. Author calendar pressure**: Watch for authors whose daily standup reports are arriving late consistently (after 12:00 UTC deadline), whose word counts are declining week-over-week without explanation, or who have expressed fatigue or stress. These are burnout signals. Address directly: a 15-minute call asking "what would make the next week easier?" is more effective than adding accountability pressure to a stressed author.

---

## Section 3: Peer Review Triage Process

*For routing each domain's draft to its peer reviewer and processing the returned review.*

### Peer Reviewer Introduction Email (Orchestrator Sends, T+9)

```
Subject: Phase 6 peer review — [DOMAIN NAME] — review window June 11–13

Hi [REVIEWER NAME],

Thank you for agreeing to peer review the [DOMAIN NAME] document for the 
Phase 6 systems-resilience project. I'm writing to confirm the timeline and 
provide you with the review template.

TIMELINE:
- You will receive the draft on June 11 (T+10), by 12:00 UTC
- Your review is due June 13 (T+12), by 17:00 UTC
- That is a 53-hour window

WHAT YOU'RE REVIEWING:
[DOMAIN NAME] is a practitioner-facing research guide for Zone 5 Midwest 
community organizers and resilience practitioners. It covers [1-2 sentence 
domain summary]. The full document targets 40,000–55,000 words; what you 
receive for review will be approximately 8,000–25,000 words depending on 
how far along the author is at T+10.

YOUR REVIEW FOCUS:
Please evaluate the document against the criteria in the attached review 
template (below). You do not need to copy-edit or rewrite — your job is to 
flag accuracy problems, note where citations are missing or questionable, 
identify Zone 5 application gaps, and flag any sections where the framing 
seems inconsistent with what you know of the domain.

CREDENTIAL CONFIRMATION:
For our records: can you confirm in your reply the credential or experience 
that qualifies you to review [DOMAIN NAME]? [1-2 sentences from you is 
sufficient — for example: "I've worked with cooperative development 
organizations for 12 years and currently serve as X at Y."]

BACKUP REVIEWER:
I have a backup reviewer identified for this domain in case any issues arise. 
I will only contact them if you reach out to tell me you cannot complete the 
review by T+12. Please give me as much advance notice as possible if 
that situation arises.

Questions before T+10? Reply to this email. I'll respond within 4 hours.

[ORCHESTRATOR NAME]

---
ATTACHED: Peer Review Template (see below)
```

### Peer Review Template (Included with Draft Send)

```
PHASE 6 PEER REVIEW TEMPLATE
Domain: [DOMAIN NAME]
Reviewer: [NAME]
Draft received: [DATE/TIME]
Review due: T+12, June 13, 17:00 UTC

---

SECTION 1: CREDENTIALS (Required — 2-3 sentences)
What qualifies you to review this domain?

---

SECTION 2: OVERALL ASSESSMENT (Required — choose one)

[ ] PUBLICATION-READY: Document is accurate, well-cited, and appropriate for the 
    intended audience. Minor editing only needed.

[ ] PUBLICATION-READY WITH MANDATORY REVISIONS: Document is sound but requires 
    specific corrections before publication. See Section 3.

[ ] SUBSTANTIAL REVISION NEEDED: Document has significant accuracy gaps, 
    sourcing problems, or framing issues that need to be addressed. See Section 3.

[ ] NOT REVIEWABLE IN CURRENT STATE: Document is too incomplete for a meaningful 
    review. Describe what is needed before re-submission.

---

SECTION 3: MANDATORY ITEMS (items the author must address before publication)

Format: For each item, note the section/paragraph, describe the problem, 
and (if possible) suggest a resolution or source.

FACTUAL CORRECTIONS (errors in stated facts, statistics, or claims):
1. [Section X, paragraph Y]: [Description of error] — [Suggested correction or source]
2. (add as needed)

CITATION GAPS (claims that require sourcing but currently have none):
1. [Section X, paragraph Y]: [Claim that needs citation] — [Suggested source if known]
2. (add as needed)

COMMUNITY CONTEXT GAPS (sections missing Zone 5 or community application):
1. [Section X]: [What specific community context is missing] — [Suggested addition]
2. (add as needed)

---

SECTION 4: ADVISORY ITEMS (items worth addressing but not publication blockers)

FRAMING OBSERVATIONS (alternative framing that would strengthen the document):
1. [Description]

ADDITIONAL SOURCES (sources not currently in the document that would strengthen it):
1. [Source title/URL] — [Which section it would strengthen and why]

VOICE NOTES (sections where the writing is more academic than practitioner-facing):
1. [Section X]: [Brief description of the voice shift and suggestion]

---

SECTION 5: STRENGTHS (Required — 3-5 sentences)
What sections, arguments, or case studies are working particularly well?
This helps calibrate both the author and the orchestrator on what "good" 
looks like for this domain.

---

SECTION 6: FINAL QUESTION
Is there a person, organization, or publication not currently referenced 
in this document that you believe is essential to the domain?
[Name/URL if yes; NONE if not]

---
Return to: [ORCHESTRATOR EMAIL / CHANNEL]
Questions: contact orchestrator at [EMAIL] — responds within 4 hours.
```

### Peer Review Return Processing (Orchestrator, T+12)

When peer reviews are returned, the orchestrator processes each one before sending to the author:

**Step 1 — Review classification (30 minutes per domain):**
Read the review. Classify each item in Sections 3 and 4 as:
- (M) Mandatory: must be addressed before T+14 publication readiness gate
- (A) Advisory: author takes or leaves; does not affect T+14 gate assessment
- (D) Disputed: orchestrator believes the reviewer's item is based on a misreading of the document's scope — flag for author with note explaining the scope context

**Step 2 — Consolidated feedback email to author (send by T+12 23:00 UTC):**

```
Subject: [DOMAIN NAME] — Peer review feedback consolidated

Hi [AUTHOR NAME],

Your peer review is in. Here is the consolidated feedback, organized by 
priority.

MANDATORY ITEMS (address before T+14 June 15):

1. [Item from Section 3 — Factual correction]: [Section, description, resolution]
2. [Item from Section 3 — Citation gap]: [Section, description, suggested source]
3. (list all M-classified items)

ADVISORY ITEMS (take or leave — no T+14 impact):

1. [Item from Section 4]: [Description]
2. (list A-classified items)

REVIEWER NOTE ON STRENGTHS: [paste Section 5 from review]

DISPUTED ITEMS (I've reviewed these and my note is below):

1. [Item]: [Explain scope context that makes this item outside the review's scope]
   — My recommendation: [address as a clarifying note in the text / ignore / discuss]

TIMELINE:
Please address all mandatory items and confirm completion by June 14 (T+13) EOD.
You do not need to send me the revised sections separately — just update the 
master draft and flag in your T+13 standup that mandatory items are addressed.

Questions about any item: reply or message me — I respond within 4 hours.

[ORCHESTRATOR NAME]
```

---

## Section 4: Publication Readiness Assessment Matrix

*Use at T+14 (June 15) to assess each domain's publication readiness. Score each criterion and log the result.*

### Publication Readiness Rubric

Nine criteria, each scored 0 / 0.5 / 1.0.
Minimum for Wave 1 publication readiness: 7.0/9.0
Conditional readiness (close-out items listed): 6.0–6.9/9.0
Scope adjustment discussion: below 6.0/9.0

| Criterion | Weight | Scoring |
|-----------|--------|---------|
| 1. Domain completeness | 1.0 | 1.0 = ≥80% of target word count; 0.5 = 60–79%; 0.0 = <60% |
| 2. Citation depth | 1.0 | 1.0 = ≥25 distinct accessible citations; 0.5 = 15–24; 0.0 = <15 |
| 3. Peer review integration | 1.0 | 1.0 = all mandatory items addressed; 0.5 = >50% addressed, remainder flagged; 0.0 = mandatory items unaddressed |
| 4. Publication template | 1.0 | 1.0 = YAML frontmatter complete, zero placeholders; 0.5 = frontmatter present, minor cleanup needed; 0.0 = frontmatter absent or significant placeholders |
| 5. Contact stratification | 1.0 | 1.0 = Tier 1/2/3 contacts identified (≥5 Tier 1, ≥15 Tier 2); 0.5 = Tier 1 identified only; 0.0 = no contact list |
| 6. Timeline confirmation | 1.0 | 1.0 = distribution timeline confirmed with user; 0.5 = draft timeline proposed; 0.0 = no timeline |
| 7. Community context | 1.0 | 1.0 = Zone 5 or community application in every major section; 0.5 = present in >50% of sections; 0.0 = minimal or absent |
| 8. Cross-domain bridges | 1.0 | 1.0 = ≥2 explicit integration points with other Phase 6 domains; 0.5 = 1 integration point; 0.0 = no cross-domain bridges |
| 9. Practitioner voice | 1.0 | 1.0 = matches Phase 5 model document voice standard; 0.5 = minor academic drift in ≤2 sections; 0.0 = significant academic drift throughout |

### Assessment Scoring Sheet (Copy Per Domain)

```
PUBLICATION READINESS ASSESSMENT
Domain: [DOMAIN NAME]
Author: [NAME]
Date: June 15, 2026 (T+14)
Assessor: [ORCHESTRATOR NAME]

SCORES:

1. Domain completeness
   Target word count: [N]
   Actual word count: [N]
   Completion %: [N]%
   Score: [ 1.0 / 0.5 / 0.0 ]
   Notes:

2. Citation depth
   Citation count (distinct, accessible): [N]
   Score: [ 1.0 / 0.5 / 0.0 ]
   Notes:

3. Peer review integration
   Mandatory items received: [N]
   Mandatory items addressed: [N]
   Score: [ 1.0 / 0.5 / 0.0 ]
   Notes:

4. Publication template
   YAML frontmatter present: [Y/N]
   Placeholder count: [N]
   Score: [ 1.0 / 0.5 / 0.0 ]
   Notes:

5. Contact stratification
   Tier 1 contacts identified: [N]
   Tier 2 contacts identified: [N]
   Score: [ 1.0 / 0.5 / 0.0 ]
   Notes:

6. Timeline confirmation
   Distribution date confirmed: [Y/N/DRAFT]
   Score: [ 1.0 / 0.5 / 0.0 ]
   Notes:

7. Community context
   Sections with Zone 5 / community application: [N] of [total sections]
   Score: [ 1.0 / 0.5 / 0.0 ]
   Notes:

8. Cross-domain bridges
   Integration points documented: [N]
   Linked domains: [list]
   Score: [ 1.0 / 0.5 / 0.0 ]
   Notes:

9. Practitioner voice
   Voice match to model document: STRONG / ADEQUATE / NEEDS WORK
   Score: [ 1.0 / 0.5 / 0.0 ]
   Notes:

---

TOTAL SCORE: [sum] / 9.0

READINESS STATUS:
[ ] PUBLICATION-READY (≥7.0) — Wave 1 complete
[ ] CONDITIONAL READINESS (6.0–6.9) — items listed below must be completed within 5 business days
[ ] SCOPE ADJUSTMENT DISCUSSION (<6.0) — meeting scheduled within 24 hours

CONDITIONAL READINESS ITEMS (if applicable):
1. [Item description] — deadline: [DATE]
2. [Item description] — deadline: [DATE]

AUTHOR NOTIFIED: [ ] Yes — [DATE/TIME]
MILESTONE PAYMENT: [ ] Processed / [ ] Pending — [notes]
```

### Wave-Level Readiness Summary (Orchestrator Compiles at T+14)

```
PHASE 6 WAVE 1 — PUBLICATION READINESS SUMMARY
Date: June 15, 2026 (T+14)

DOMAIN SCORES:

| Domain | Score | Status |
|--------|-------|--------|
| Economic resilience | [X.X]/9 | READY/CONDITIONAL/ADJUST |
| Infrastructure interdependencies | [X.X]/9 | READY/CONDITIONAL/ADJUST |
| International coordination | [X.X]/9 | READY/CONDITIONAL/ADJUST |
| Intergenerational transmission | [X.X]/9 | READY/CONDITIONAL/ADJUST |
| Ecosystem restoration | [X.X]/9 | READY/CONDITIONAL/ADJUST |
| Institutional learning | [X.X]/9 | READY/CONDITIONAL/ADJUST |

WAVE 1 COMPLETION:
Domains at publication-ready: [N]/6
Domains at conditional readiness: [N]/6
Domains requiring scope adjustment discussion: [N]/6

OUTSTANDING ITEMS FOR CONDITIONAL DOMAINS:
[Domain]: [item 1], [item 2] — expected close: [DATE]

WAVE 2 ACTIVATION TRIGGER:
If all conditional items close by [DATE]: Wave 2 domains can begin
If scope adjustment discussions required: schedule user decision meeting by [DATE]

COMMIT TO MASTER:
Domains at publication-ready status are committed to master at T+14 EOD.
Conditional domains committed with status: CONDITIONAL-READINESS, close-out items in YAML frontmatter.

WORKLOG ENTRY: [DATE] T+14 — Wave 1 complete. [N] of 6 domains at publication 
readiness. Conditional items: [list]. Wave 2 activation: [date].
```

---

## Section 5: Quick Reference — Communication Formats

*Short formats for common coordination messages. Use exactly as written; substitute bracketed fields.*

### Source Access Problem (Author to Orchestrator)

```
SOURCE ACCESS PROBLEM — [DOMAIN] — [DATE]

Source I cannot access: [TITLE — URL]
Section it was intended to support: [SECTION NAME]
Specific claim or question it would address: [1 sentence]
Alternatives I've already tried: [list or NONE]
Is this blocking me right now: YES / NO (if NO, describe workaround)
```

### Scope Boundary Question (Author to Orchestrator)

```
SCOPE QUESTION — [DOMAIN] — [DATE]

Section in question: [SECTION NAME]
What I want to write: [1-2 sentences describing the proposed content]
Why I think it might be out of scope: [1 sentence]
Alternative approach if it is out of scope: [1 sentence]
Is this blocking me right now: YES / NO
```

### Cross-Domain Coordination Request (Author to Author, via Orchestrator)

```
CROSS-DOMAIN COORDINATION REQUEST
From: [AUTHOR NAME — DOMAIN]
To: [OTHER AUTHOR NAME — DOMAIN]
Date: [DATE]

I'm working on [SECTION NAME] and I need to understand how your domain 
covers [TOPIC]. Specifically: [1-2 sentences on what I need to know to 
avoid overlap or ensure consistency].

Are you available for a 10-minute conversation or a written note this week?
I can work around your schedule.

[No action needed if the answer is "I'm not covering that topic" — just 
tell me and I'll proceed.]
```

### Milestone Payment Request (Author to Orchestrator)

```
MILESTONE PAYMENT REQUEST
Domain: [DOMAIN NAME]
Author: [NAME]
Milestone reached: [June 29 draft / July 27 full draft / August 9 final]
Deliverable submitted: [DATE/TIME]
Orchestrator approved: [Y — DATE]
Payment amount: [N]% = [AMOUNT]
Payment method: [as agreed]
Invoice: [attached/follows]
```

### Contingency Alert (Orchestrator Internal)

```
CONTINGENCY ALERT — [DATE] — T+[N]

Contingency: CT-[N] ([name])
Domain affected: [DOMAIN NAME]
Trigger condition met: [description of what happened]
Time of detection: [TIME UTC]

Immediate actions taken (within 2 hours of trigger):
1. [action]
2. [action]

Next decision required: [what needs to happen next and by when]
User input required: YES / NO
If YES: [describe the decision the user needs to make]

Status: ACTIVATED / MONITORING / RESOLVED
```

---

## Section 6: Escalation Paths Reference

*Who does what when something goes wrong. Keep this visible in every standup.*

| Situation | Who detects | Who resolves | Timeline | Template to use |
|-----------|-------------|-------------|----------|----------------|
| Source inaccessible | Author | Orchestrator research | 4 hours | Source Access Problem |
| Scope question | Author | Orchestrator review | 4 hours | Scope Boundary Question |
| Author goes silent | Orchestrator | Orchestrator follow-up | 24 hours | Author Status Check (from Onboarding Kit) |
| Author unavailable | Orchestrator | Contingency author or self-execute | 48 hours | CT-1 + Contingency Recruit Template |
| Research dead-end | Author | Orchestrator source sprint | 4 hours | CT-2 protocol |
| Scope drift detected | Orchestrator | Scope correction request | 4 hours | Scope Boundary correction email |
| Peer review delayed | Orchestrator | Backup reviewer or internal review | 12 hours | CT-4 protocol |
| Word count below target | Orchestrator | Amber/Red meeting | 24 hours | T+7 assessment + amber discussion |
| Cross-domain conflict | Either author | Orchestrator mediation | 48 hours | Cross-Domain Coordination Request |
| User scope change | User | Orchestrator recalibration | 48 hours | CT-5 protocol |

---

*All templates in this document are production-ready. Fill in the bracketed fields and send. Do not add corporate boilerplate or extraneous text to any template — the formats are designed to be brief and scannable. When in doubt about which template to use, default to plain prose and flag it as: "ESCALATION — [domain] — [date]" in the subject line. The orchestrator will route appropriately.*
