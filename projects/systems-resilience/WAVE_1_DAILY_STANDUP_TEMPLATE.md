---
title: "Wave 1 Daily Standup Template — June 1–5"
project: systems-resilience
scope: "Phase 5 publication (June 5) + Phase 6 Wave 1 author activation"
created: 2026-06-01
standup_window: "06:00–09:00 UTC daily"
applicable_dates: "June 1–5, 2026"
status: PRODUCTION-READY
---

# Wave 1 Daily Standup Template
## June 1–5, 2026 | 06:00–09:00 UTC

**Purpose**: Daily operational check during the Phase 5 publication sprint and Phase 6 author activation window. Each standup takes 15–30 minutes. Complete during the 06:00–09:00 UTC window; decisions requiring user input must surface no later than 09:00 UTC.

---

## Standup Structure (All Days)

Run in this order. Flag any item marked AT-RISK or BLOCKED before moving to the next item.

**1. Phase 5 publication track** — June 5 13:00 UTC is the hard deadline  
**2. Phase 6 author recruitment track** — June 3 EOD is the author confirmation deadline  
**3. Peer review track** — Candidate identification and outreach June 1–2  
**4. Content edits track** — Frontmatter updates and any advisory pre-publication edits  
**5. Blockers** — Anything requiring user decision or external action today

---

## June 1 (T+0) — Activation Day

**Standup focus**: Confirm all June 1 pre-flight tasks are executing.

### Phase 5 Publication Track
- [ ] Integrated corpus (`PHASE_5_WAVE_1_2_INTEGRATED_CORPUS.md`) committed to master and verified
- [ ] GitHub Release draft (`v5.0-wave-1-2-production`) created or in progress
- [ ] Distribution list population begun (Tier 1: practitioner contacts; Tier 2: organizations; Tier 3: broadcast channels)
- [ ] Stakeholder announcement emails personalized for June 5 send

**Authors on track for June 5 deadline?**  
Phase 5 requires no external author action — all content is orchestrator-complete. Confirm: CONFIRMED (no author dependency for Phase 5 publication)

**Content edits complete or need extension?**  
Frontmatter status updates (4 documents, "production-draft" → "PRODUCTION-READY") pending. ETA for completion: June 1–2. No extension needed.

### Phase 6 Author Recruitment Track
- [ ] Domain A (Economic Resilience) primary author: check response to May 29 email. If no response by 14:00 UTC today, initiate fallback (Fallback 1 via NCBA CLUSA / USDA RD network). Status: ___
- [ ] Identify author candidates for remaining 5 Phase 6 domains (Infrastructure Interdependencies, International Coordination, Intergenerational Transmission, Ecosystem Restoration, Institutional Learning)
- [ ] Begin personalization of recruitment emails for any domain where candidate is identified

### Peer Reviewers Confirmed?
No reviewers confirmed yet. June 1 action: identify specific named candidates from `WAVE_1_PEER_REVIEWERS_CANDIDATES.md` candidate profiles. No outreach today unless candidates are identified.

### Blockers Today
1. Is the GitHub Release creation tooling accessible? If not, flag immediately — June 4 rendering test requires a draft release to exist.
2. Is the Tier 1 distribution list (practitioner contacts) accessible from seedwarden / resistance-research roster?

---

## June 2 (T+1) — Author Outreach Day

**Standup focus**: Author outreach executing; publication prep advancing.

### Phase 5 Publication Track
- [ ] Frontmatter status updates complete in all 4 source documents? YES / NO — if NO: complete today
- [ ] Distribution list: how many Tier 1 contacts populated? Target by June 3: 30+ contacts. Current: ___
- [ ] Tier 2 organization list finalized? (15–20 target institutions) YES / IN PROGRESS / NOT STARTED
- [ ] GitHub Release draft: is the release title, description, and file manifest complete? YES / IN PROGRESS

**Any peer reviewers confirmed yet?**  
Likely no — this is the first day of active candidate identification. Target for June 3: at least 2 peer reviewers identified per document (1 primary + 1 backup).

### Phase 6 Author Recruitment Track
- [ ] Domain A author status: CONFIRMED / DECLINED / NO RESPONSE (if no response by June 2 14:00 UTC: activate fallback 2)
- [ ] Recruitment emails sent for how many of 6 domains? Target: all 6 contacted by EOD June 2
- [ ] Any early responses from Phase 6 domain candidates? Log: ___

### Content Edits Complete?
- [ ] All 4 frontmatter `status` fields updated? YES / NO
- [ ] Integrated corpus cross-references verified? YES / NOT CHECKED
- [ ] Any new issues identified in documents during distribution prep? YES (describe) / NO

### Blockers Today
1. Any author recruitment emails blocked (no candidate identified for a domain)?
2. Any distribution list access issue (Tier 1 contacts roster inaccessible)?

**Key question for orchestrator**: "Are all 6 Phase 6 domain author recruitment emails sent by end of June 2?"

---

## June 3 (T+2) — Author Confirmation Deadline

**Standup focus**: Author confirmation gate. Publication prep 80% complete.

This is the most important standup of the June 1–5 window. The June 3 EOD author confirmation gate determines whether Phase 6 proceeds with external authors or self-execute fallback.

### Phase 5 Publication Track
- [ ] Distribution list: Tier 1 population complete? (Target: 30+ contacts) YES / PARTIAL (current: ___)
- [ ] Distribution list: Tier 2 organization list complete? YES / PARTIAL
- [ ] Announcement emails: personalized for each Tier 1 contact? YES / IN PROGRESS
- [ ] GitHub Release: draft complete with all 6 file assets attached? YES / IN PROGRESS
- [ ] Rendering pre-check: opened integrated corpus markdown in GitHub draft — does it render correctly? YES / NOT YET (rendering test is June 4; pre-check optional but recommended)

**Authors on track for June 5 deadline?** Phase 5: yes, no author dependency. Phase 6: see below.

### Phase 6 Author Confirmation Gate (June 3 EOD)

At June 3 17:00 UTC, record the following for each domain:

| Domain | Author | Confirmed? | Path |
|--------|--------|-----------|------|
| Economic Resilience | [name or PENDING] | YES / NO | External author / Self-execute |
| Infrastructure Interdependencies | [name or PENDING] | YES / NO | External author / Self-execute |
| International Coordination | [name or PENDING] | YES / NO | External author / Self-execute |
| Intergenerational Transmission | [name or PENDING] | YES / NO | External author / Self-execute |
| Ecosystem Restoration | [name or PENDING] | YES / NO | External author / Self-execute |
| Institutional Learning | [name or PENDING] | YES / NO | External author / Self-execute |

**If any domain has 0 confirmed authors by EOD June 3**: self-execute fallback activates for that domain. Log in ORCHESTRATOR_STATE.md. No further recruitment effort for that domain in the June 1–5 window.

### Peer Reviewers Confirmed?
Target for June 3: at least one named peer reviewer per Phase 5 document contacted (5 contacts sent). Target for June 5: at least one reviewer confirmed per document.

**Log**: How many peer reviewer contacts sent today? ___ | How many confirmations received? ___

### Blockers Today
1. **CRITICAL**: Is the June 3 author confirmation gate fully decided? If 0 authors confirmed, is self-execute path actively starting today?
2. Any peer reviewer declines that require replacement candidate identification?

---

## June 4 (T+3) — Pre-Publication Day

**Standup focus**: Publication infrastructure complete. Final checks before June 5.

### Phase 5 Publication Track
- [ ] GitHub rendering test: opened GitHub Release draft, verified integrated corpus renders correctly (tables, headers, anchors) — YES / NO / ISSUES FOUND: ___
- [ ] All 6 file assets in GitHub Release: 5 source documents + integrated corpus? YES / MISSING: ___
- [ ] Release notes (500-word corpus summary): complete and final? YES / IN PROGRESS
- [ ] Distribution list final: Tier 1 ready to send June 5 13:00 UTC? YES / AT-RISK
- [ ] Distribution list final: Tier 2 ready? YES / AT-RISK
- [ ] Tier 3 (Reddit / social media / Slack) posts drafted and scheduled for June 5 13:00 UTC? YES / IN PROGRESS
- [ ] Announcement emails: final review complete — no unfilled [PLACEHOLDER] fields? YES / ISSUES: ___

**Content edits complete or need extension?**  
All content edits (frontmatter updates) should be complete by today. Confirm: all 4 `status` fields read "PRODUCTION-READY"? YES / PENDING: ___

### Phase 6 Author Activation Track
- [ ] All confirmed Phase 6 authors: briefing package sent? YES / IN PROGRESS
- [ ] All confirmed Phase 6 authors: received and acknowledged briefing by today? YES / NOT ALL — missing: ___
- [ ] Self-execute domains: orchestrator has begun outline for each? YES / IN PROGRESS
- [ ] Phase 6 author check-in for June 2 orientation day: any authors who did not acknowledge their briefing by June 2 — logged and follow-up sent? YES / NO

### Peer Reviewers Confirmed?
Target for June 4: at least one reviewer confirmed for Phase 5 Psychological Support and Veterinary Care (highest-stakes documents).

**Log**: Confirmed reviewers as of June 4: ___

### Blockers Today
1. Any GitHub rendering failures requiring a fix before June 5?
2. Any distribution list gap that would prevent Tier 1 send on June 5?

**Key question for user**: "Any final content, scope, or framing concerns about the Phase 5 Wave 1+2 corpus before it publishes tomorrow?"

---

## June 5 (T+4) — Publication Day

**Standup focus**: Confirm publication executes at 13:00 UTC. Phase 6 authors writing.

### Phase 5 Publication Track — GO / NO-GO

Complete this go/no-go assessment before 12:00 UTC:

| Criterion | Status |
|-----------|--------|
| Integrated corpus markdown renders correctly on GitHub | GO / NO-GO |
| All 4 frontmatter fields show `status: PRODUCTION-READY` | GO / NO-GO |
| Zero placeholder markers in any document | GO / NO-GO |
| GitHub Release assets complete (6 files) | GO / NO-GO |
| At least one distribution channel ready to execute at 13:00 UTC | GO / NO-GO |

**If all criteria are GO**: Publication executes June 5 13:00 UTC. Log timestamp in WORKLOG.md.  
**If any criterion is NO-GO**: Flag immediately. Assess whether the issue can be resolved before 13:00 UTC. If not, decide: (a) fix and publish same day late, or (b) push to June 6 (1-day slip has minimal impact on June 30 Wave 3 timeline).

### Post-Publication (13:00 UTC onward)
- [ ] GitHub Release published and accessible via public URL? YES / NO
- [ ] Tier 1 announcement emails sent? YES / NO (send window: 13:00–15:00 UTC)
- [ ] Tier 2 organization emails sent? YES / NO (send window: 13:00–15:00 UTC)
- [ ] Tier 3 broadcast posts live? YES / NO
- [ ] Reader feedback log initialized for Wave 1+2 feedback collection (June 5 – June 29)? YES / NO

### Phase 6 Status (June 5 = T+4 of Wave 1 execution)
- [ ] Outline feedback sent to all confirmed Phase 6 authors? (T+4 milestone: outlines due June 4, feedback due June 5 12:00 UTC) YES / IN PROGRESS
- [ ] Fast-track domain authors (Economic Resilience, Infrastructure Interdependencies): beginning Section 1 writing today? YES / AT-RISK / NO
- [ ] Any Phase 6 author has not submitted their June 4 outline? If YES: follow-up sent and logged? YES / NO

**Authors on track for June 15 Phase 6 deadline?**  
Fast-track domains: target 4,000–6,000 words of Section 1 by end of June 5.  
Secondary domains: outline approved; writing begins.  
Self-execute domains: orchestrator outline complete; research synthesis begun.

**Any peer reviewers confirmed for Phase 6 wave?**  
Target by June 5: all 6 Phase 6 peer reviewers identified and introduction emails sent (confirmations expected by June 10). Log: ___

### Content Edits — June 5 and Beyond
Phase 5 content is frozen at publication. No edits to published documents until the Wave 3 integration pass (June 15–29). Any errors discovered post-publication go into a corrections log for the next editorial cycle.

### Blockers Today
1. Any publication blocker that surfaced after go/no-go check?
2. Any Phase 6 author who has gone unresponsive (no June 4 outline, no June 2 standup reply)?

---

## Daily Standup Log Format

After each standup, record a one-line entry in WORKLOG.md:

```
[DATE] T+[N] standup complete. Phase 5: [status in 5 words]. Phase 6 authors confirmed: [N]/6. Peer reviewers confirmed: [N]. Blockers: [NONE / describe]. Next action: [most important item for today].
```

Example:
```
2026-06-03 T+2 standup complete. Phase 5: distribution list 60% populated. Phase 6 authors confirmed: 2/6. Peer reviewers confirmed: 0. Blockers: NONE. Next action: Send recruitment emails for 4 remaining domains by EOD.
```

---

## Escalation Protocol

If a standup reveals a blocker that cannot be resolved within the 06:00–09:00 UTC window:

1. Log the blocker in WORKLOG.md with timestamp
2. Flag for user attention if the blocker requires a decision outside the orchestrator's authority (e.g., scope changes, additional resource allocation, author hiring decisions above confirmed rate)
3. Do not wait for the next day's standup — same-day escalation for anything that affects the June 5 publication or the June 3 author confirmation gate

---

*Template created: 2026-06-01 | Applicable: June 1–5, 2026 | Window: 06:00–09:00 UTC daily*  
*This template supersedes any earlier standup formats for the Phase 5 publication sprint.*
