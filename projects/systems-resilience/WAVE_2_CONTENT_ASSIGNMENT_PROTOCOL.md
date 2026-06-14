---
title: "Wave 2 Content Assignment Protocol"
project: systems-resilience
phase: 5/6
wave: 2
status: PRODUCTION-READY
purpose: "Task assignment rules, domain-to-author matching criteria, execution decision framework for Phase 6 Wave 2"
created: 2026-06-14
execution_deadline: 2026-06-15
domains_covered: "60–65 (International, Intergenerational, Infrastructure, Ecosystem, Economic, Governance)"
---

# Wave 2 Content Assignment Protocol
## Domain-to-Author Matching & Tier Allocation Framework

> **This document operationalizes the author-to-domain matching decisions.** Combined with WAVE_2_AUTHOR_MATCHING_ALGORITHM.md (scoring) and WAVE_2_AUTHOR_PROFILE_CARDS.md (candidate profiles), this protocol guides the complete assignment workflow: matching finalization → domain scope assignment → delivery task creation → timeline confirmation → quality gate configuration.

> **Execution window**: June 14, 14:00 UTC through June 15, 18:00 UTC. Two-day window accommodates timezone distribution (authors from UTC+2 to UTC-7).

---

## Part 1: Pre-Session Preparation (June 13, EOD)

### 1.1 Final Verification Checklist

Before the June 14 matching session begins, complete these items by June 13 EOD:

**Candidate confirmations**:
- [ ] All active candidates (those who responded "yes" or "maybe" to recruitment) have completed AUTHOR_READINESS_INTAKE_FORM.md
- [ ] All intake forms have been scored on D1–D5 dimensions per WAVE_2_AUTHOR_MATCHING_ALGORITHM.md
- [ ] Secondary scores (S1–S4) computed for all confirmed candidates
- [ ] Availability confirmed: Each candidate verbally confirmed or email-confirmed 8 hrs/week, July 16 – Sept 15 window
- [ ] Timezone documented for each author (required for scheduling check-in calls)

**Matching algorithm preparation**:
- [ ] WAVE_2_AUTHOR_PROFILE_CARDS.md updated with final scores (D1–D5 + S1–S4) for all candidates
- [ ] Domain minimum threshold matrix verified (Domain 60–65 D1/D5 requirements documented)
- [ ] Tier assignments computed: Tier A (20–25 pts), Tier B (14–19 pts), Tier C (below 14)
- [ ] Eligible/ineligible candidates flagged per domain-specific thresholds

**Source materials preparation**:
- [ ] Domain scope briefs (2–3 page overview for each Domain 60–65) prepared and ready to distribute
- [ ] Wave 1 reference documents compiled for each domain (Phase 5 Wave 1 author contact info, draft outputs, citations)
- [ ] Source bibliography for each domain verified (8–15 key sources per domain queued for delivery to authors)

**Communication templates prepared**:
- [ ] Offer letters customized for each domain (Domain 60–65 variants)
- [ ] Check-in call schedule template prepared (weekly for Tier A, bi-weekly for Tier B)
- [ ] Week 1 orientation materials drafted (deliverables schedule, submission format, contact protocols)

**Recording & documentation**:
- [ ] WAVE_2_ASSIGNMENT_DECISIONS.md created and ready for real-time logging of all decisions
- [ ] Email template for "assignment confirmation + scope brief" ready to send (June 15 EOD)
- [ ] Tracking spreadsheet open: Domain | Assigned Author | Tier | Score | Assignment Date | Call Scheduled | Materials Sent

**Environment setup**:
- [ ] WAVE_2_AUTHOR_PROFILE_CARDS.md open in editor (for ASSIGNMENT DECISION section completion)
- [ ] WAVE_2_AUTHOR_MATCHING_ALGORITHM.md accessible (for tiebreaker logic reference)
- [ ] Video conference link prepared (Zoom or video call if authors across timezones join live)
- [ ] Contact list ready: phone numbers/emails for all authors (for real-time clarifications)

---

## Part 2: Matching Session — Greedy Assignment (June 14, 14:00–17:00 UTC)

### 2.1 Algorithm Execution: Domain-by-Domain Assignment

**Step 1: Gather candidates and sort by fitness**

Before the session, the matching algorithm has pre-computed scores. During the session, execute the greedy assignment:

1. **Sort all eligible candidates by raw fitness score (D1–D5 total), descending**
   ```
   Candidate A: 22/25 (Domain 63 eligible) → HIGHEST
   Candidate B: 21/25 (Domain 65 eligible)
   Candidate C: 20/25 (Domain 62 eligible)
   Candidate D: 20/25 (Domain 60 eligible)
   Candidate E: 19/25 (Domain 61 eligible)
   ...
   ```

2. **For each domain (60–65), identify top 2–3 eligible candidates**
   - Sort by primary fitness score for that domain
   - Apply domain-specific threshold check: D1 ≥ minimum AND D5 ≥ minimum (varies by domain)
   - Flag as ELIGIBLE or INELIGIBLE or BORDERLINE

   **Domain threshold matrix** (from WAVE_2_AUTHOR_MATCHING_ALGORITHM.md):
   | Domain | D1 min | D5 min | Total min | Tier requirement |
   |--------|--------|--------|-----------|------------------|
   | 60 (International) | 3 | 3 | 18 | Tier A or B |
   | 61 (Intergenerational) | 3 | 3 | 18 | Tier A or B |
   | 62 (Infrastructure) | 3 | 3 | 18 | Tier A or B only |
   | 63 (Ecosystem) | 4 | 4 | 20 | Tier A preferred |
   | 64 (Economic) | 3 | 3 | 18 | Tier A preferred |
   | 65 (Governance) | 3 | 3 | 18 | Tier A preferred |

3. **Assign greedily: highest fitness per domain, unallocated author first**

   Process:
   - For each domain (starting with 63 — highest threshold, then 60, 61, 62, 64, 65):
     - Identify highest-fitness eligible candidate not yet assigned
     - If author preference ranking lists this domain in top 3: **ASSIGN immediately**
     - If author preference ranking lists this domain as #4–6: **MOVE TO STEP 2.3 (ask preference)**
     - If author is already assigned elsewhere: **MOVE TO NEXT-BEST CANDIDATE for this domain**
     - If all eligible candidates are assigned: **FLAG FOR FALLBACK (Section 2.5)**

**Step 2: Handle preference conflicts**

If top-fitness author for a domain did NOT rank it in their top 3 preferences:

- **Call author** (max 3–5 minutes): "You're our top match for Domain [X]. Your intake form ranked this #[Y]. If we assigned you here, could we find a secondary author for your preferred domain [Z]?"
  - If **YES**: Assign to this domain; note date + time
  - If **NO**: Decline this author for this domain; move to next-best candidate
  - If **MAYBE**: "Take 1 hour to think; we'll call back at [TIME]" → Continue with other assignments; revisit

**Step 3: Generate preliminary matching outcome**

When all 6 domains have assignments (or are flagged for fallback), document in WAVE_2_ASSIGNMENT_DECISIONS.md:

```
DOMAIN 60 (International Coordination)
Assigned author: [Name] | Tier: [A/B] | Score: [XX/25]
Fitness for this domain: [XX/25] | D1: [X] | D5: [X]
Alternative candidates (if author declines): [Name (XX/25)], [Name (XX/25)]
Status: ✓ CONFIRMED or ⏳ PENDING PREFERENCE CALL or ❌ FLAGGED FOR FALLBACK
---
[Repeat for Domains 61–65]
```

---

### 2.2 Tier-Specific Oversight Configuration

Once assignments are finalized, configure oversight level for each author:

**Tier A (score 20–25 pts)**:
- Weekly 30-minute check-in calls (same day each week)
- Access to Phase 5 Wave 1 reference document (draft)
- Direct contact to project lead (you)
- Revision round 1: Peer review feedback within 5 days of submission
- Revision round 2: 3-day turnaround if major rewrite needed

**Tier B (score 14–19 pts)**:
- Bi-weekly (every 2 weeks) 30-minute check-in calls
- Same Wave 1 reference access
- Potential pairing: Wave 1 primary author from same/adjacent domain (2 hrs/week mentoring, Weeks 1–4)
- Revision round 1: Peer review feedback within 7 days of submission
- Revision round 2: 5-day turnaround

**Tier C (not applicable for Wave 2 primary authors; community editor role only)**

---

### 2.3 Domain Scope Finalization

For each assigned author, during June 14–15 session:

**Complete domain scope brief** (customize from template):

The Domain [X] brief should specify:

1. **Core sections** (non-negotiable; author must address all):
   - Section 1: [Core definition of domain concept]
   - Section 2: [Why this matters for Zone 5 communities]
   - Section 3: [Key practitioner frameworks / case studies]
   - Section 4: [Common failure modes]
   - Section 5: [Scaling pathways / governance implications]

2. **Sub-topics** (author may adjust ordering):
   - Subtopic A: [Example]
   - Subtopic B: [Example]
   - Subtopic C: [Example]

3. **Geographic scope**:
   - Primary: Zone 5 Midwest (Wisconsin, Minnesota, Iowa, Illinois, etc.)
   - Secondary: Broader applicability notes for other climate zones

4. **Audience framing**:
   - Reader profile: "Community leaders, farmers, cooperative organizers, and local government officials with 3–10 years experience, preparing for infrastructure disruption"
   - Tone: Practitioner-accessible (explain theory through case studies, not abstract)
   - Jargon: Define all domain-specific terms on first use

5. **Length target**: 8,000–12,000 words (approximately 16–24 pages at standard formatting)

6. **Deliverable format**:
   - Markdown file: `Domain_[60-65]_[Author_Last_Name].md`
   - YAML front matter (title, author, domain, date, revision)
   - Sections with ### headers
   - Citations: [Author Year] in-text, full bibliography at end (15–30 sources)

7. **Revision round expectations**:
   - Round 1 submission: Dates TBD (staggered by domain; see timeline)
   - Round 1 peer review: 5–7 days feedback (Tier A) or 7–10 days (Tier B)
   - Round 2 revision deadline: 14 days after feedback
   - Round 2 acceptance or Final revisions: 7 days final check-in

**Communicate scope brief to author** in assignment confirmation email (Section 3.1 template below).

---

### 2.4 Deliverable Sequencing

Set submission deadlines staggered to reduce bottlenecks in peer review:

**Wave sequence** (submitted/reviewed/accepted in parallel clusters):

| Wave | Domains | Due Date | Peer Review Window | Acceptance Target |
|------|---------|----------|-------------------|------------------|
| A | 63, 65 | July 30 | Aug 1–8 | Aug 9 or revision |
| B | 60, 64 | Aug 6 | Aug 8–15 | Aug 16 or revision |
| C | 61, 62 | Aug 13 | Aug 15–22 | Aug 23 or revision |

**Rationale**: 
- Domain 63 (Ecosystem Restoration) goes first — highest threshold, most complex, benefits from full revision window
- Domain 65 (Governance Scaling) parallels 63 — both Tier A likely, no author overlap conflict
- Domain 60 & 64 follow (one week later) — both have strong Tier A candidates, can use Wave A feedback lessons
- Domain 61 & 62 last — allows any emerging patterns/revisions from A & B to inform final writing

---

## Part 3: Assignment Confirmation & Activation (June 15, 08:00–18:00 UTC)

### 3.1 Send Assignment Confirmation Emails

**Within 2 hours of final matching decisions**, send each assigned author a formal assignment confirmation email:

**Email Template: Assignment Confirmation + Scope Brief**

```
Subject: Phase 6 Wave 2 Author Assignment Confirmed — Domain [X]: [Domain Name]

Hi [Author Name],

I'm delighted to confirm: You are assigned as the primary author for Domain [X]: [Domain Name] 
in Systems Resilience Phase 6 Wave 2.

═══════════════════════════════════════════════════════════════════════════════════

YOUR ASSIGNMENT

Domain: [X] ([Domain Name])
Author: [Your Name]
Tier: [A / B]
Start Date: July 16, 2026
End Date: September 15, 2026
Commitment: 8 hours/week

Contact: [Your project lead name] | [Phone] | [Email]
Backup: [Backup contact] | [Email]

═══════════════════════════════════════════════════════════════════════════════════

DOMAIN SCOPE (to be finalized on call)

Your role is to synthesize research and case studies into a practitioner-focused research guide on 
[Domain Name] for Zone 5 Midwest communities preparing for infrastructure challenges.

Core sections you will address:
1. [Section description]
2. [Section description]
3. [Section description]
4. [Section description]
5. [Section description]

Estimated length: 8,000–12,000 words
Format: Markdown with citations (15–30 sources)
Audience: Community leaders, cooperative organizers, local government officials

(Detailed scope brief attached as DOMAIN_[X]_SCOPE_BRIEF.md)

═══════════════════════════════════════════════════════════════════════════════════

YOUR TIMELINE

Week 1 (June 16–20): Onboarding call + source material review
Week 2–7 (June 23–Aug 3): Draft writing (2–3 calls total for check-ins)
Week 8 (Aug 4–10): Peer review feedback + revision planning
Week 9–10 (Aug 11–24): Revisions + final acceptance
Week 11–12 (Aug 25–Sept 6): Contingency buffer
Due date: Sept 15, 2026

First milestone (50% payment): Confirmed assignment date (today)
Second milestone (50% payment): Document accepted by peer review gate

═══════════════════════════════════════════════════════════════════════════════════

WHAT HAPPENS NOW (next steps):

Step 1: Accept assignment (reply "confirmed" to this email)
Step 2: Schedule Week 1 onboarding call → I'll send calendar link by June 16
Step 3: Review scope brief + Phase 5 Wave 1 reference materials
Step 4: Begin outline draft (June 23 target)

═══════════════════════════════════════════════════════════════════════════════════

SUPPORT STRUCTURE

✓ You're assigned a project lead: [Name] (me)
✓ Weekly [or bi-weekly for Tier B] check-in calls (30 min, same time each week)
✓ Access to Phase 5 Wave 1 reference drafts + full source bibliography
✓ Peer reviewer assigned: [Wave 1 author from adjacent domain, if applicable]
✓ Writing templates + submission format guide provided
✓ All check-in calls recorded + notes shared (no surprises)

═══════════════════════════════════════════════════════════════════════════════════

YOUR PAYMENT

Rate: $65/hour
Hours: 8 hours/week × 9 weeks = 72 hours estimated
Total: $4,680 (estimated)

Payment structure:
- 50% ($2,340) due on start date (July 16) — deposited upon assignment confirmation
- 50% ($2,340) due on final acceptance — confirmed after peer review completion

═══════════════════════════════════════════════════════════════════════════════════

QUESTIONS?

Contact me directly. No question is too small. Better to clarify now than discover 
misalignment in Week 5.

Looking forward to collaborating.

Best,
[Your Name]
[Title] | [Organization]
[Phone] | [Email]

---

**Attachments:**
- DOMAIN_[X]_SCOPE_BRIEF.md
- PHASE_6_WAVE_1_REFERENCE_MATERIALS.md (citations + excerpt of relevant Wave 1 work)
- WAVE_2_DELIVERY_LOGISTICS.md (submission format, citation style, etc.)
```

**Send by**: June 15, 16:00 UTC (allows authors time to confirm before June 16 calls)

---

### 3.2 Schedule Tier-Specific Check-In Calls

Once authors confirm assignment, schedule:

**Tier A** (score 20–25):
- Weekly 30-minute calls
- Standing time (same day/time each week): [Select 1 timezone-optimal window for author cohort]
- First call: June 16 or June 17 (onboarding)
- Subsequent: July 23, July 30, Aug 6, Aug 13, Aug 20, Aug 27, Sept 3, Sept 10 (9 calls total)

**Tier B** (score 14–19):
- Bi-weekly 30-minute calls
- First call: June 16 or June 17 (onboarding)
- Subsequent: July 2, July 16, July 30, Aug 13, Aug 27, Sept 10 (6 calls total)
- Plus: Wave 1 mentor pairing (2 hrs/week mentoring, Weeks 1–4 only)

**Scheduling logistics**:
- Send Calendly/scheduling link to each author by June 15 EOD
- Allow authors to pick from 3–4 time windows that work for their timezone
- Confirm call link + dial-in details by June 16 09:00 UTC
- Send reminder 24 hours before first call

---

### 3.3 Distribute Source Materials

By June 16 EOD, send each author a materials package:

**Domain-specific materials**:
- [ ] Scope brief (2–3 pages)
- [ ] Phase 5 Wave 1 reference document excerpt (if applicable)
- [ ] Bibliography (15–30 sources, organized by subtopic)
- [ ] Citation style guide (Chicago Manual of Style author-date format)
- [ ] Submission format template (Markdown structure, YAML front matter, section headers)

**Shared project materials**:
- [ ] WAVE_2_DELIVERY_LOGISTICS.md (submission mechanics, revision expectations)
- [ ] WAVE_2_QUALITY_GATES.md (acceptance criteria checklist)
- [ ] Peer reviewer contact info + brief intro (who will review your work)
- [ ] Project lead contact + expected response times

**Delivery method**: Email with attachments or shared drive folder (Google Drive/Box with all authors)

---

## Part 4: Quality Gate Configuration

### 4.1 Peer Review Pairing

Assign a peer reviewer for each domain. Criteria:

- **Primary preference**: Wave 1 author from adjacent or complementary domain (not competing scope)
- **Secondary preference**: If no Wave 1 author available, recruit external reviewer (academic, practitioner, or community editor)
- **Conflict-of-interest check**: Reviewer has no institutional conflict with author (competing organizations, past disputes)

**Peer review pairing matrix**:

| Domain | Primary Author | Assigned Reviewer | Reviewer Role | Contact |
|--------|-------------------|------------------|---------------|---------|
| 60 | [Name] | [Wave 1 Domain X author] | Primary peer | [Email] |
| 61 | [Name] | [Wave 1 Domain Y author] | Primary peer | [Email] |
| 62 | [Name] | [Name] | External reviewer | [Email] |
| 63 | [Name] | [Wave 1 Domain Z author] | Primary peer | [Email] |
| 64 | [Name] | [Name] | Community editor | [Email] |
| 65 | [Name] | [Wave 1 Domain A author] | Primary peer | [Email] |

**Notify reviewers by June 16**: Send email with reviewer profile + domain overview. Confirm availability for August review window.

### 4.2 Acceptance Criteria Definition

All drafted documents must meet these criteria **before ACCEPTED status**:

✓ **Content completeness**: All 5 core sections address scope brief requirements
✓ **Word count**: 8,000–12,000 words (±10% flexibility)
✓ **Citation discipline**: 15–30 sources, all cited in text, full bibliography at end
✓ **Zone 5 applicability**: Document explicitly addresses Midwest context (examples, geography-specific frameworks)
✓ **Practitioner voice**: Accessible to non-academic readers; jargon defined; case studies included
✓ **Structure**: Markdown valid; YAML front matter complete; section headers consistent
✓ **Citation accuracy**: All citations verified (spot-check 5 random citations match URL/publication)
✓ **Revision history**: GitHub commit log shows authorship + revision iterations
✓ **Peer review sign-off**: Reviewer confirms document meets above 8 criteria
✓ **Final editing**: No typos; formatting consistent; compliance with WAVE_2_DELIVERY_LOGISTICS.md
✓ **Governance alignment**: No statements contradicting Systems Resilience Phase 5/6 foundational principles
✓ **Timeline compliance**: Submitted by deadline (or approved extension documented)

**Rejection criteria** (document does NOT meet ACCEPTED status):
- Critical content gaps: >1 core section missing or incomplete
- Word count: <7,000 or >13,000 words
- Citations: <12 sources or >5 unsourced claims
- Practitioner voice: Reads as academic only; not accessible to target audience
- Zone 5 applicability: Generic guidance with no Midwest context
- Structural issues: Markdown errors; missing front matter; inconsistent headers

**Revision-needed criteria** (document is REVISE-AND-RESUBMIT):
- Minor content issues: 1 section underdeveloped; 2–3 citations missing
- Writing issues: 5–10 copyedits; restructuring of 1–2 sections recommended
- Practitioner voice: Good bones, needs tone adjustment in 1–2 sections
- Reviewer notes: "Resubmit with 1–2 week revision window"

---

## Part 5: Escalation Procedures

### 5.1 Author No-Show / Non-Responsiveness

**Definition of escalation trigger**: No response to communications for 5+ consecutive business days.

**If triggered during onboarding (Week 1)**:
- Day 1–3: Author misses first check-in call with no notice
  - Action: Send email + call directly (same day)
  - Documentation: Log attempt + time in WAVE_2_INCIDENT_LOG.md
  - Author response expectation: Within 24 hours
- Day 4–5: Still no response
  - Action: Activate backup communication (send via phone, email to backup contact)
  - Escalation: If no response by EOD Day 5, call contingency activation (see WAVE_2_CONTINGENCY_AUTHOR_SUBSTITUTION.md Section 2.2)

**If triggered during writing phase (Weeks 2–7)**:
- Day 1–3: Missed check-in call or no progress reported
  - Action: Email + call same day; ask status
  - If response is "I'm behind but working": Reset expectations; increase check-in frequency
  - If no response: Escalate
- Day 4–5: Still no communication
  - Action: Activate mentoring support (if Tier B, increase mentor contact to 4 hrs/week); 
    phone call + offer of logistical support ("Do you need an extension? Different timeline?")
  - Document in WAVE_2_INCIDENT_LOG.md
- Day 6–7: No response after 2 escalation attempts
  - Action: Invoke contingency plan (WAVE_2_CONTINGENCY_AUTHOR_SUBSTITUTION.md)

**If triggered before submission deadline (Week 8)**:
- Author indicates they will miss deadline but are still writing
  - Action: Confirm extension (max +7 days if Domain 60/61/65; max +3 days if Domain 62/63/64)
  - Documentation: Email agreement + updated timeline
  - Contingency trigger: If extension expires + no submission, activate fallback (Section 5.3 below)

### 5.2 Quality Concerns (During Peer Review)

**If peer reviewer flags document as REJECT (does not meet acceptance criteria)**:

1. **Within 2 days of peer review completion**, convene revision meeting:
   - Author + Project lead + Peer reviewer (3-way call, 30 min)
   - Discuss: What's failing? What's the fix timeline? Do we need a co-author?
   - Decision: REVISE-AND-RESUBMIT (14-day revision window) OR ESCALATE TO CONTINGENCY

2. **Revision assignment**:
   - Peer reviewer provides detailed feedback (issue-by-issue)
   - Author commits to revision plan (which sections, what sources to add, etc.)
   - Project lead confirms support (additional resources? mentor support?)
   - New deadline: 14 days from revision kick-off

3. **If second peer review also fails** (major revision needed again):
   - ESCALATE: Activate co-author support or contingency plan
   - Document decision + reasoning in WAVE_2_INCIDENT_LOG.md

### 5.3 Scope Creep / Timeline Pressure

**If author indicates they need to expand scope mid-stream:**

- Example: "I discovered that Domain 62 really needs to cover [NEW SUBTOPIC]; can I add 3,000 words?"
- Action: 
  - Approve minor expansions (up to +1,500 words) if still achievable in timeline
  - Deny expansions that push past Sept 15 deadline (unless domain can slip — see WAVE_2_CONTINGENCY_AUTHOR_SUBSTITUTION.md Section 3.2)
  - Document in WAVE_2_SCOPE_CHANGE_LOG.md with justification + approval

---

## Part 6: Key Contacts & Communication Protocol

### 6.1 Author Communication Expectations

**Weekly (Tier A) or Bi-weekly (Tier B) check-in calls**:
- Standing 30-minute calls (same day/time each week)
- Call agenda: Progress update (5 min), blockers (10 min), feedback/questions (15 min)
- If author misses call: They send written status update within 24 hours; no call needed
- Recorded + notes shared within 24 hours

**Off-call communication**:
- Email response time SLA: 24 hours during business hours
- Urgent issues (author stuck, deadline threat): Phone call same day
- Non-urgent questions: Email; asynchronous response OK

**Peer reviewer communication**:
- Reviewer receives draft + review guidelines (3 days before due date)
- Reviewer submits feedback within 5–7 days of receipt
- Feedback delivered in standardized template (WAVE_2_QUALITY_GATES.md)

### 6.2 Contact Directory

Create and maintain throughout Wave 2:

```
DOMAIN 60: [Author Name]
  Email: [Email] | Phone: [Phone] | Timezone: [TZ]
  Peer Reviewer: [Name] | Email: [Email]
  Project Lead: [Your Name] | Phone: [Phone]
  Backup contact: [Name] | Phone: [Phone]

DOMAIN 61: [Author Name]
  [Same structure]

[Repeat for Domains 62–65]
```

Share this directory with all authors by June 16 EOD (for mutual awareness + backup contact access).

---

## Part 7: Post-Assignment Documentation

### 7.1 Update Tracking Documents

Upon completion of June 14–15 matching session, update:

**WAVE_2_ASSIGNMENT_DECISIONS.md** (new file; create during session):
- One entry per domain
- Format: Domain | Author Name | Tier | Primary Score | D1/D5 scores | Alternatives considered | Decision rationale | Date assigned
- Example:
  ```
  DOMAIN 63 (Ecosystem Restoration)
  Assigned: Jack Kloppenburg | Tier A | 22/25
  D1=5 (Seed sovereignty expertise), D5=5 (Zone 5 practitioner grounding)
  Alternatives: Lauren Gwin (20/25), Saria Lofton (19/25)
  Rationale: Highest fitness for highest-threshold domain; 30 years Wisconsin experience; ideal for Ecosystem guide
  Assigned: June 14, 14:45 UTC
  ```

**WAVE_2_AUTHOR_PROFILE_CARDS.md** (update each card):
- Complete "ASSIGNMENT DECISION (June 14–15)" section for every candidate (even declines)
- Format:
  ```
  ASSIGNMENT DECISION (June 14–15):
    ☑ Domain 63 assigned
    ☐ Markdown onboarding scheduled (June 16, 2 hours)
    ☐ Scope coverage confirmed (seed sovereignty + soil + native plants + agroforestry)
    ☐ Intake form verified
  ```

**WAVE_2_PROJECT_TIMELINE.md** (new file; create after assignments finalized):
- One master timeline showing:
  - All check-in call dates (by author)
  - Submission deadlines (staggered by domain wave)
  - Peer review windows
  - Acceptance target dates
  - Key milestones (first draft, revisions, final)
- Format: Gantt chart or table format, shared with all authors

---

## Part 8: Handoff to Execution

### 8.1 Author Onboarding Call Script (June 16–17)

When you conduct the Week 1 onboarding call with each author, cover these topics in this order:

**1. Welcome & context** (3 min):
- "Welcome to Phase 6 Wave 2. You're assigned to Domain [X]: [Domain Name]. Excited to have you."
- Quick overview: "Phase 6 expands Systems Resilience into 6 new domains. Your domain is foundational because [REASON]."

**2. Scope review** (5 min):
- Review scope brief together; confirm author understands the 5 core sections
- Ask: "Does this match what you expected? Any sections where you'd like to adjust emphasis?"
- Adjust scope if needed (minor tweaks OK; major changes escalate to project lead)

**3. Timeline & deliverables** (5 min):
- Walk through: First outline due June 30, first draft due July 30, revision rounds, final Sept 15
- Confirm: "Can you commit to these dates? Any adjustments needed?"
- For Tier B: "You'll also have mentor support [if applicable]; [Mentor name] will contact you June 16 to intro"

**4. Support structure** (5 min):
- "Here's your peer reviewer: [Name]. They'll review your draft in August and provide detailed feedback."
- "If you get stuck, here's how to reach me: email [EMAIL], phone [PHONE]. I aim to respond within 24 hours."
- "We have weekly [or bi-weekly] check-in calls: same time every [DAY], [TIME]. If you miss a call, just send a quick email update."

**5. Q&A** (7 min):
- "What questions do you have?"
- Be prepared to answer: availability concerns, payment schedule, revisions expectations, source access

**6. Closing** (1 min):
- "I'll send you a summary email after this call with all the details we discussed. You're all set to start July 16."

---

### 8.2 Handoff Checklist (June 15 EOD)

Before you consider the matching session complete, verify all items checked:

- [ ] All 6 domains assigned (or fallback plan activated for unassigned)
- [ ] All authors sent assignment confirmation emails (with scope brief + support info)
- [ ] All authors confirmed acceptance (replied "confirmed" or equivalent)
- [ ] All check-in calls scheduled for Week 1 (June 16–20)
- [ ] All source materials compiled + ready to distribute
- [ ] All peer reviewers identified + contacted + confirmed
- [ ] WAVE_2_ASSIGNMENT_DECISIONS.md completed + shared with leadership
- [ ] WAVE_2_AUTHOR_PROFILE_CARDS.md updated with final assignments
- [ ] Contact directory distributed to all authors
- [ ] Week 1 call scripts prepared + calendar links sent
- [ ] Payment milestones configured (50% upfront, 50% on acceptance)
- [ ] WAVE_2_INCIDENT_LOG.md created + monitoring protocols set

**Final sign-off**: Project lead confirms to leadership: "Wave 2 author assignments COMPLETE. All 6 domains assigned. Onboarding begins June 16. Execution on track for July 16 start."

---

## Part 9: Appendix — Domain Assignment Preferences Reference

For quick lookup during matching session, document author stated preferences from intake forms:

| Author | Domain 60 | Domain 61 | Domain 62 | Domain 63 | Domain 64 | Domain 65 | Top Choice |
|--------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| [Name] | #3 | #1 | #5 | #6 | #2 | #4 | Domain 61 |
| [Name] | #5 | #2 | #3 | #1 | #4 | #6 | Domain 63 |
| [Etc] | — | — | — | — | — | — | — |

(This table helps when deciding between near-equal-fitness candidates: secondary tiebreaker is author preference.)

---

## Summary: Operational Milestones

| Date | Milestone | Owner | Deliverable |
|------|-----------|-------|-------------|
| June 13 EOD | Pre-session verification | Project lead | All intake forms scored; candidates ready |
| June 14, 14:00 UTC | Matching session opens | Project lead | Greedy algorithm executed; 6 domains assigned |
| June 14, 17:00 UTC | Matching complete | Project lead | WAVE_2_ASSIGNMENT_DECISIONS.md finalized |
| June 15, 08:00 UTC | Confirmation emails sent | Project lead | All authors notified of assignment |
| June 15, 16:00 UTC | Scope briefs + materials sent | Project lead | Authors have full scope documentation |
| June 16–17 | Onboarding calls completed | Project lead | All authors confirmed, ready for July 16 start |
| June 16 EOD | Phase 2 handoff | Project lead | Leadership briefed; execution phase begins |

---

## Document Status

This protocol is **PRODUCTION-READY** and may be executed as-is on June 14, 2026.

For questions or modifications before execution, contact the project lead by June 13, 12:00 UTC.

---

## Related Documents

- `WAVE_2_AUTHOR_MATCHING_ALGORITHM.md` — Scoring methodology (reference during matching)
- `WAVE_2_AUTHOR_PROFILE_CARDS.md` — Candidate profiles (use during session for author bios + scores)
- `WAVE_2_DELIVERY_LOGISTICS.md` — File format, submission mechanics, acceptance criteria (reference for scope briefs)
- `WAVE_2_CONTINGENCY_AUTHOR_SUBSTITUTION.md` — Fallback procedures if author no-shows (activate if Section 5 escalation needed)
- `WAVE_2_QUALITY_GATES.md` — Peer review criteria + acceptance checklist (reference when configuring quality gates, Section 4)
