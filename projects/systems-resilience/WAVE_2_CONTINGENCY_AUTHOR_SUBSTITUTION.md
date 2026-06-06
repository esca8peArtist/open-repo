---
title: "Wave 2 Contingency Author Substitution"
project: systems-resilience
phase: 5/6
wave: 2
status: PRODUCTION-READY
purpose: "Failure mode handling: author no-show, quality rejection, scope collapse, and recovery protocols"
created: 2026-06-07
execution_trigger: "On-demand when author escalation occurs (target: avoid >1 contingency per wave)"
decision_trees: "Clear branches for each failure scenario with timeline recovery options"
---

# Wave 2 Contingency Author Substitution
## Phase 6 Domains 60–65 — Failure Mode Handling & Recovery Protocols

> **This document operationalizes failure scenarios that WAVE_2_CONTENT_ASSIGNMENT_PROTOCOL.md Section 5 escalates to.** When an author no-shows, submits work below quality threshold, or declares they cannot continue, this document provides decision trees and activation procedures to recover the domain without losing the publication timeline or cascading delays.

> **Key principle**: Contingency procedures are designed to activate **within 24 hours of failure detection**, preserve maximum recovery time for that domain, and minimize impact on other domains.

---

## Part 1: Failure Mode Detection

### 1.1 Escalation Triggers & Timeline

**No-show detection** (Author stops communicating):

| Timeline | Trigger | Action | Owner |
|----------|---------|--------|-------|
| Day 1 | Author misses scheduled call; no notice sent | Send email + call same day | Project lead |
| Day 2 | No response to Day 1 outreach | Call backup contact; escalate email | Project lead |
| Day 3 | Still no response; no submission if draft due | Phone call + email to all known contacts | Project lead + Backup contact |
| Day 4–5 | No contact after 3+ escalation attempts | **ACTIVATE CONTINGENCY PLAN** | Project lead |

**Quality rejection detection** (Peer review = REJECTED status):

| Trigger | Timeline | Action | Owner |
|---------|----------|--------|-------|
| Peer reviewer submits REJECTED status + detailed feedback | Immediate | Project lead calls author + peer reviewer for 30-min clarification call | Project lead |
| Call outcome: Issues are fundamental (>major rewrite needed); author agrees work is unfinishable | Within 2 hours | **ACTIVATE CONTINGENCY PLAN** | Project lead |
| Call outcome: Issues fixable in revision; author commits to revision | Within 2 hours | Proceed with REVISION-NEEDED (see WAVE_2_DELIVERY_LOGISTICS.md Section 3); no contingency yet | Project lead |

**Author self-escalation** (Author proactively declares they cannot continue):

| Scenario | Timeline | Action | Owner |
|----------|----------|--------|-------|
| Author emails: "I'm over my head; I can't do this justice" | Within 24 hrs | Offer contingency options (Section 2 below) | Project lead |
| Author requests extension due to life circumstances (illness, family emergency) | Within 24 hrs | Approve extension +3 to +7 days (no contingency yet); escalate if extension expires without progress | Project lead |
| Author responds "I'm withdrawing; I can't continue after this week" | Within 2 hours | **ACTIVATE CONTINGENCY PLAN** | Project lead |

---

## Part 2: Decision Tree: Which Contingency Path?

### 2.1 Path Selection Logic

When contingency is triggered, follow this decision tree **in order**. Answer each yes/no question top-to-bottom.

```
CONTINGENCY ACTIVATION DECISION TREE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

START: Author X has triggered escalation for Domain Y

Q1: Is the assigned author willing to continue but needs SUPPORT?
    └─ YES → Go to SECTION 2.2: Co-Author Pairing (support path)
    └─ NO  → Continue to Q2

Q2: Are there ALT tier authors available for Domain Y (from WAVE_2_AUTHOR_PROFILE_CARDS.md)?
    └─ YES, 1–2 available → Go to SECTION 2.3: Fallback Activation (standard contingency)
    └─ NO ALT available  → Continue to Q3

Q3: Can Domain Y scope be absorbed into adjacent domain assignment?
    └─ YES (list related domain) → Go to SECTION 2.4: Scope Reduction (load shift)
    └─ NO, cannot absorb       → Go to SECTION 2.5: Tier 3 Synthesis Role (partial solution)

END: Contingency plan activated; timeline recovery calculated
```

---

### 2.2 Path A: Co-Author Pairing (Support Path)

**Scenario**: Author is competent but overwhelmed; needs active support.

**Triggers**:
- Author says: "I need help" or "Can I have a co-author?" or "I'm behind and need support"
- Peer reviewer says (during review): "Good bones; author needs editorial support to polish"
- Project lead assesses: Author is capable; just needs mentoring/co-author to finish

**Activation steps** (execute within 24 hours):

1. **Identify co-author source** (in priority order):
   - Wave 1 author from same/adjacent domain (best option; already knows project)
   - Tier B author from WAVE_2_AUTHOR_PROFILE_CARDS.md in different domain (if available)
   - External subject matter expert (PhD student, practitioner with writing background)
   - Community editor already engaged for peer review (pivot them to co-author)

2. **Propose co-author to primary author** (same day):
   ```
   Email subject: Contingency Support — Co-Author Pairing for Domain [Y]
   
   Hi [Author Name],
   
   I heard that Domain [Y] is feeling overwhelming. That's OK — this is exactly why 
   we have support options.
   
   I'd like to propose pairing you with [Co-Author Name], who has [relevant expertise/background]. 
   [Co-Author] would join as a 50/50 co-author, which means:
   
   - You split the research/writing load 50/50
   - Both names appear as authors in final document
   - You split the payment ($2,340 each instead of $4,680 solo)
   - [Co-Author] starts immediately; revised deadline still Sept 15
   
   Would this help? I can have [Co-Author] call you by [tomorrow at TIME].
   
   Let me know.
   [Project Lead]
   ```

3. **Contact co-author immediately** (same day):
   ```
   Email subject: Urgent: Co-Author Opportunity — Domain [Y] — Wave 2
   
   Hi [Co-Author Name],
   
   I have an urgent request. The primary author for Domain [Y] needs co-author support 
   to finish their draft by [deadline]. 
   
   Would you be willing to step in as a 50/50 co-author? This would mean:
   - 4–5 weeks of work (not 9 weeks)
   - You take responsibility for [Section(s) #], [Co-Author] takes [Sections]
   - Split payment: $2,340 (vs. $4,680 if solo authoring)
   - Full support + check-in calls
   
   Timeline is tight, but doable if you can start this week.
   
   Interested? Call me by [TIME today] so I can facilitate a call with [Author Name].
   
   [Project Lead]
   ```

4. **Three-way call** (within 48 hours):
   - Primary author + Co-author + Project lead
   - Agenda:
     - Divide sections/workload
     - Confirm complementary skills (e.g., one strong on research; one on writing)
     - Set internal communication plan (when do they sync?)
     - Revised deadline: Same as original (no extension for co-authors; they share load)
   - Outcome: Both authors sign off on division of labor

5. **Update documents**:
   - WAVE_2_ASSIGNMENT_DECISIONS.md: Add note "Co-authored with [Name]"
   - YAML front matter: Add `co_author: "[Co-Author Name]"` field
   - Payment record: Split payment 50/50; both receive milestone payments
   - WAVE_2_INCIDENT_LOG.md: "Contingency A (Co-author) activated for Domain [Y], Day [X]"

6. **Timeline recovery**:
   - Co-author onboarding: 1 day
   - Revised work schedule: 4–5 weeks (compressed)
   - Submission deadline: UNCHANGED (same as original)
   - Recovery success rate: ~85% (co-authors usually deliver on time if initial author is capable)

---

### 2.3 Path B: Fallback Author Activation (Standard Contingency)

**Scenario**: Assigned author is unresponsive/unreachable OR has quality fundamentally below threshold. Replace with ALT tier author from candidate pool.

**Triggers**:
- Author unreachable >3 days (no-show escalation, Section 1.1)
- Peer reviewer = REJECTED; author unavailable or unwilling to revise
- Author formally withdraws: "I'm done; find someone else"

**Activation steps** (execute within 24 hours of trigger):

1. **Identify ALT tier author for Domain Y**:
   - Reference WAVE_2_AUTHOR_PROFILE_CARDS.md for "Alternative candidates" listed under each domain card
   - Example from profile cards:
     ```
     CARD 63-01: Jack Kloppenburg (Assigned: Domain 63)
     Alternatives (if unavailable): Lauren Gwin (20/25), Saria Lofton (19/25)
     ```
   - Call candidates in order of fitness score; **first who answers "yes" = fallback author**

2. **Contact ALT author immediately** (phone call + email same day):
   ```
   Subject: Urgent: Phase 6 Wave 2 Author Opportunity — Domain [Y]

   Hi [ALT Author Name],

   I'm reaching out because the primary author for Domain [Y] has had to step back, 
   and you were our first-choice backup candidate.

   We'd like to offer you Domain [Y] authorship on these terms:

   ASSIGNMENT OFFER:
   - Domain: [Y] ([Domain Name])
   - Start date: [Today or tomorrow]
   - Submission deadline: [Original domain deadline + 1 week buffer, if available]
   - Payment: $65/hour, 8 hrs/week estimate; $4,680 total (same as standard assignment)
   - Support: Weekly check-ins, peer reviewer, access to all Wave 1 materials

   SCOPE BRIEF & MATERIALS:
   [Attach same scope brief that original author received]

   TIME SENSITIVITY:
   The domain deadline is [DATE — X weeks away]. If you say yes today, you'd start immediately 
   (likely 5 weeks writing time vs. the usual 9 weeks). This is doable but intense.

   DECISION:
   Can you confirm by [TODAY at 15:00 UTC]? If yes, we'll do a 30-min call to onboard.
   
   Looking forward to your response.

   [Project Lead]
   ```

3. **If ALT author says YES**:
   - Conduct 30-minute onboarding call (same day or next morning)
   - Send scope brief + all Wave 1 materials
   - Update assignment records (WAVE_2_ASSIGNMENT_DECISIONS.md)
   - Schedule first check-in call for 3 days out
   - Memo to peer reviewer: "Original author X replaced by author Y; review timeline unchanged"

4. **If ALT author says NO**:
   - Move to next-best alternative from candidate list
   - Repeat steps 2–3
   - If no ALT authors available → Go to SECTION 2.4 (Scope Reduction)

5. **Timeline recovery calculation**:
   - Days elapsed: 3–5 days (from initial failure to new author start)
   - Time remaining for new author: [Original deadline] − [Days elapsed]
   - If remaining time <4 weeks: Adjust deadline +1 week (negotiate with peer review)
   - If remaining time <2 weeks: Escalate to scope reduction (Section 2.4)

6. **Documentation**:
   - WAVE_2_INCIDENT_LOG.md: "Contingency B (Fallback) activated for Domain [Y], Day [X], Original author: [Name], Fallback author: [Name]"
   - WAVE_2_ASSIGNMENT_DECISIONS.md: Replace original author with fallback; note date + reason
   - Email notification to stakeholders: "Domain [Y] author change; new author [Name], same deadline"

---

### 2.4 Path C: Scope Reduction (Load Shift Path)

**Scenario**: No ALT tier authors available, or no-show happened too late to find replacement. Reduce domain scope and distribute missing content to adjacent domain.

**Triggers**:
- No viable fallback authors available in candidate pool
- Failure detected <3 weeks before original deadline
- Two domains already in contingency; cannot afford third failure

**Scope reduction decision matrix** (choose which domain absorbs load):

| Failed Domain | Primary Recipient | Secondary Option | Load Transfer |
|---------------|-------------------|------------------|----------------|
| **60** (Intl Coord) | **65** (Governance scaling) | 64 (Economic) | Sections 5 + 1–2 case studies → 65 |
| **61** (Intergenerational) | **62** (Infrastructure) | 64 | Sections 3 + 5 → 62 |
| **62** (Infrastructure) | **60** (Intl Coord) | 63 (Ecosystem) | Sections 4 + 5 → 60 |
| **63** (Ecosystem) | **64** (Economic) | 62 | Sections 3 + 4 → 64 (optional; deep scope) |
| **64** (Economic) | **61** (Intergenerational) | 65 | Sections 2 + 3 → 61 |
| **65** (Governance) | **60** (Intl Coord) | 64 | Sections 1 + 5 → 60 |

**Activation steps** (within 24 hours):

1. **Identify receiving author** (use matrix above):
   - Contact assigned author of recipient domain
   - Confirm they're on track + have capacity for +2,000–2,500 word expansion
   - Request commitment: Can you absorb [X] section(s) of the failed domain? Yes/No.

   ```
   Email subject: Urgent: Scope Expansion Request — Domain [Recipient]

   Hi [Recipient Author Name],

   We have a contingency situation. Domain [Failed] author has stepped back, 
   and rather than find a replacement, we'd like to offer you a scope expansion.

   EXPANSION REQUEST:
   - Add Sections [X–Y] from Domain [Failed] to your Domain [Recipient] draft
   - Estimated addition: 2,000–2,500 words
   - Estimated effort: +6–8 hours additional work
   - Payment: +$390–520 (pro-rata increase to your budget)
   - New deadline: [Original domain deadline + 3 days] (to account for expansion)

   WHY THIS DOMAIN?
   Domain [Recipient] and Domain [Failed] are naturally adjacent; your existing 
   frameworks can incorporate the failed domain's content without major restructuring.

   CAN YOU DO THIS?
   Reply with yes/no by [TODAY at 15:00 UTC]. If yes, we'll send you the failed 
   domain's research materials + Section [X–Y] outline.

   Let me know.
   [Project Lead]
   ```

2. **If receiving author agrees**:
   - Send failed domain's research materials + section outline (same day)
   - Confirm revised deadline
   - Update YAML front matter: `expanded_scope: "includes Section [X–Y] from Domain [Failed]"`
   - Add note to Section [X–Y]: "This section was originally planned for Domain [Failed] and is included here for continuity"
   - Schedule brief check-in call (3 days out) to confirm integration strategy

3. **If receiving author declines**:
   - Try secondary recipient (see matrix)
   - If all recipients decline → Go to Section 2.5 (Tier 3 Synthesis)

4. **Timeline & quality implications**:
   - Expanded domain gets longer review window (+3 days peer review)
   - Final acceptance deadline still Sept 15 (no slip past this date)
   - Peer reviewer assesses expanded content against same 12-point checklist
   - Payment adjustment: Transparent, pro-rata; document in payment tracking

5. **Documentation**:
   - WAVE_2_INCIDENT_LOG.md: "Contingency C (Scope reduction) activated for Domain [Failed], content absorbed by Domain [Recipient]"
   - WAVE_2_SCOPE_CHANGE_LOG.md: "Domain [Failed] sections [X–Y] transferred to Domain [Recipient]; new word count [XXXX]"
   - Email stakeholders: "Domain [Failed] deferred to Wave 3; content integrated into Domain [Recipient]. Publication timeline on track."

---

### 2.5 Path D: Tier 3 Synthesis Role (Partial Solution)

**Scenario**: All paths A–C exhausted. Cannot find co-author, no fallback authors, adjacent domain cannot absorb scope. Resort to Tier 3 synthesis: hire synthesizer to compile Wave 1 + available sources into partial guide.

**Triggers**:
- Fallback search exhausted (all ALT authors unavailable)
- All receiving domains have declined scope expansion
- Time remaining: <2 weeks before original deadline
- Decision: Deliver partial (5,000–6,000 word) guide rather than full (8,000–12,000) or nothing

**What is Tier 3 synthesis?**
- Not a primary author (not 8–12K words, full sections)
- Synthesizer compiles existing Wave 1 Phase 5 research + provided sources
- Output: 5,000–6,000 word "condensed practitioner guide" (abbreviated version)
- Quality: Meets core 12-point checklist but with reduced section depth
- Payment: $2,000 (vs. $4,680 for full authorship); ~30 hours work

**Activation steps** (execute within 24 hours):

1. **Identify synthesizer source** (in priority order):
   - Tier B author from different domain (willing to do synthesis instead of full authorship)
   - Community editor already engaged (pivot them to synthesis)
   - Graduate student / research assistant with practitioner writing background
   - Wave 1 author from adjacent domain (paid extra for synthesis work)

2. **Contact synthesizer** (phone + email same day):
   ```
   Subject: Urgent: Synthesis Role — Domain [Failed] — Wave 2

   Hi [Synthesizer Name],

   We have an urgent opportunity. The primary author for Domain [Failed] has stepped back, 
   and we'd like to offer a different kind of contribution:

   ROLE: Tier 3 Synthesis Author for Domain [Failed]
   - Output: 5,000–6,000 word condensed guide (vs. usual 8,000–12,000)
   - Timeline: 3 weeks
   - Input: Phase 5 Wave 1 research + provided sources (you don't research; you synthesize existing work)
   - Payment: $2,000 flat fee
   - Deadline: [Original domain deadline]

   WHAT THIS MEANS:
   - You'll use sections of the original scope brief (1–2 core sections, skip others)
   - Shorter case study section (2 examples instead of 4)
   - Abbreviated failure modes + scaling sections
   - Same citation standard; same quality gate (12-point checklist)

   WHY YOU?
   Your background in [relevant area] positions you well to synthesize [domain] research 
   for practitioner audiences.

   INTERESTED?
   Reply or call by [TODAY at 16:00 UTC] if you'd like to explore.

   [Project Lead]
   ```

3. **If synthesizer agrees**:
   - Create abbreviated scope brief (2–3 core sections only)
   - Send Wave 1 materials + pre-selected sources (reduce bibliography to 8–12 "must-read" sources)
   - Clarify: "You're synthesizing, not researching. Primary sources already identified."
   - 30-min onboarding call (next morning)
   - Revised outline due: 1 week out
   - Submission deadline: UNCHANGED (original deadline)

4. **Revised 12-point checklist** (for synthesis documents):
   - Elements 1–5 (Content & Scope): Scaled to 5,000–6,000 words; still 5 sections but 1,000 words each
   - Elements 6–12: UNCHANGED (same citation standards, same structure, same quality)
   - Acceptance rule: 11/12 elements OK (1 element can be "scaled but acceptable" due to condensed scope)

5. **Documentation & stakeholder communication**:
   - WAVE_2_INCIDENT_LOG.md: "Contingency D (Tier 3 Synthesis) activated for Domain [Failed], Synthesizer: [Name]"
   - Email stakeholders: "Domain [Failed] will be published as condensed synthesis guide (5,000 words, Wave 3 expansion planned). Full-scope version deferred to Wave 3 Wave 2 with original author or new recruit."
   - Note in published document: "This condensed guide synthesizes Phase 5 Wave 1 research. An expanded full-scope guide is planned for Phase 6 Wave 3."

6. **Wave 3 planning**:
   - Flag Domain [Failed] for Wave 3 expansion with original author (if they re-engage) or new recruit
   - Synthesized version serves as foundation; Wave 3 author expands to full 8,000–12,000 words
   - Cost: Synthesis ($2,000) + Wave 3 expansion (~$2,500–3,000)

---

## Part 3: Timeline Recovery & Domain Deadline Adjustments

### 3.1 Deadline Slip Decision Table

**When a contingency is activated, consult this table to determine if deadline must slip.**

| Contingency Path | Days Lost | Remaining Time | New Deadline | Slip Allowed |
|------------------|-----------|-----------------|--------------|-------------|
| **A: Co-Author** | 1–2 days | 26–27 days | UNCHANGED | No — co-authors compress schedule |
| **B: Fallback** | 3–5 days | 22–24 days | UNCHANGED if >21 days; +7 days if 14–21 days | Yes, if triggered <3 weeks before |
| **C: Scope Reduction** | 2–4 days | 23–25 days | +3 days (absorption + integration) | Yes |
| **D: Synthesis** | 1–3 days | 24–26 days | UNCHANGED (synthesizer works fast) | No — fixed 3-week timeline |

**Rules**:
- If remaining time >21 days: No deadline slip; contingency author must meet original date
- If remaining time 14–21 days: May slip +3 to +7 days (negotiable with peer review)
- If remaining time <14 days: MUST use Tier 3 synthesis (Paths B/C infeasible); no slip (synthesis timeline is fixed 3 weeks)
- **Sept 15 hard deadline**: NO contingency domain slips past Sept 15; if impossible, escalate to leadership for Wave 3 deferral decision

### 3.2 Multi-Domain Contingency (If >1 Domain Triggers)

**Scenario**: Two or more domains trigger contingency simultaneously (rare but possible).

**Priority order for contingency activation** (process in this sequence):

1. **Domain 63 (Ecosystem Restoration)** — Highest threshold; most critical; activate first
2. **Domain 65 (Governance Scaling)** — Foundational; activate second
3. **Domain 60 (International Coordination)** — Activate third
4. **Domain 64 (Economic Resilience)** — Activate fourth
5. **Domain 61 (Intergenerational Knowledge)** — Activate fifth
6. **Domain 62 (Infrastructure Interdependencies)** — Activate last

**Rationale**: 63 & 65 are highest-threshold domains (require Tier A authors). If they fail, activation must be immediate. Domains 60–62 have lower thresholds; more flexibility for Path B/C solutions.

**Contingency budget** (fallback author pool):
- TOTAL available ALT tier candidates across all domains: ~15–18 (per WAVE_2_AUTHOR_PROFILE_CARDS.md)
- Contingency capacity: Can absorb 2–3 simultaneous failures without complete pool depletion
- Beyond 3 failures: Must resort to Paths C or D for additional domains

---

## Part 4: Communication & Stakeholder Notification

### 4.1 Activation Notification (Immediate, <2 hours)

When contingency is triggered, send notifications in this order:

**TO: Project lead's supervisor / Phase lead** (immediate, same day):

```
Subject: URGENT: Contingency Activation — Domain [Y] — Wave 2

Hi [Supervisor Name],

I'm writing to report that Domain [Y] author has [triggered contingency reason].

ACTIVATION: Contingency [A/B/C/D] ([Path Name])
CONTINGENCY PLAN: [Brief description of activation steps]
TIMELINE IMPACT: Deadline [UNCHANGED / +3 days / +7 days] from original [DATE]
FINANCIAL IMPACT: [If applicable; e.g., "Fallback author requires $4,680 vs. originally budgeted $4,680"; or "Synthesis author $2,000 additional cost"]
RECOVERY SUCCESS PROBABILITY: [Based on path: A=85%, B=80%, C=70%, D=60%]

NEXT STEPS:
- [Step 1: who does what by when]
- [Step 2: who does what by when]
- I will update you daily until domain is re-assigned

Any concerns? I'm available for a call.

[Project Lead]
```

**TO: Affected author (if relevant)** (within 2 hours):

If Path A (co-author): [See Section 2.2 template above]
If Path B (fallback): Original author is not contacted; fallback author contacted instead
If Path C (scope reduction): Recipient author contacted; failed author may be notified of transition

**TO: Peer reviewer for affected domain** (within 4 hours):

```
Subject: Status Update — Domain [Y] Peer Review

Hi [Peer Reviewer Name],

Wanted to update you on Domain [Y]:

[CONTINGENCY PATH + BRIEF EXPLANATION]

IMPACT ON YOUR REVIEW:
- New author: [Name] (if Path B)
- OR Expanded deadline: [New date] (if Path C)
- OR Synthesis role: Document may be condensed (if Path D)
- OR No change; same timeline (if Path A co-author)

I'll send you updated materials / scope brief by [DATE].
Your review timeline remains: Submission [DATE] → Review [DATE + 7 days].

Thanks for rolling with the change. Questions?

[Project Lead]
```

### 4.2 Recovery Status Communications

**Daily stand-up message** (internal: project lead + supervisor + relevant domain leads):

Send brief (2–3 line) status update each day until domain re-assigned:

```
CONTINGENCY STATUS — Domain [Y]

Day 1: Fallback author contacted; awaiting response (4 candidates in sequence)
Day 2: Candidate #2 confirmed YES; onboarding call scheduled for Day 3
Day 3: Onboarding complete; materials distributed; work begins
Day 4: [Normal check-in cadence resumes]
```

**Final notification** (when contingency resolved):

```
Subject: Contingency Resolved — Domain [Y] — New Author [Name]

Hi [Supervisor / stakeholders],

Domain [Y] contingency has been resolved.

NEW ASSIGNMENT:
- Domain: [Y] ([Domain Name])
- Author: [Name] (Tier [A/B])
- Start date: [Date]
- Submission deadline: [Original date or adjusted date]
- Payment: [Amount]
- Peer reviewer: [Name]

Recovery Path: [Path A/B/C/D]
Timeline impact: [NONE / +X days]

We're back on track for Phase 6 publication.

[Project Lead]
```

---

## Part 5: Financial & Legal Implications

### 5.1 Payment Adjustments

**Original author (if early withdrawal)**:
- If author completes 0–25% of work: Forfeit all payment; no compensation
- If author completes 25–50% of work: Receive 50% of first milestone ($1,170) only; no completion bonus
- If author completes 50%+ of work: Receive full first milestone ($2,340); completion bonus pro-rated at 50%+ of work = 50%+ of bonus
- If author is replaced by co-author: Original author receives pro-rata pay for completed sections only

**Co-author** (Path A):
- Split all payment 50/50: each receives $2,340 total ($1,170 per milestone)

**Fallback author** (Path B):
- Full payment: $4,680 (same as originally budgeted)

**Scope reduction recipient** (Path C):
- Original payment + expansion bonus: [Original payment] + $390–520 pro-rata

**Synthesizer** (Path D):
- Fixed fee: $2,000 (non-negotiable; fixed timeline / fixed scope)

### 5.2 Amendment Documentation

When payment changes, document in:
- **File**: WAVE_2_AUTHOR_CONTRACTS.md (new section for each contingency)
- **Format**: 
  ```
  DOMAIN [Y] — PAYMENT AMENDMENT — [Date]
  
  Original author: [Name] | Original contract: [Amount] | Reason for withdrawal: [Reason]
  New amount owed to original author: [Amount] | Justification: [Completed X% of work]
  Alternative author/arrangement: [Name/arrangement] | Amount: [Amount]
  
  Authorized by: [Project lead] | Date: [Date]
  ```

---

## Part 6: Incident Logging & Post-Mortem

### 6.1 Incident Log (Real-Time Documentation)

Create file: `WAVE_2_INCIDENT_LOG.md`

Every contingency activation is logged immediately:

```
## Contingency Activation #1 — Domain 63

Date: [Date of detection]
Failure trigger: [No-show / quality rejection / author withdrawal / other]
Timeline from trigger to activation: [X days]
Contingency path: [A/B/C/D]
Contingency author: [Name]
Days lost: [X]
Deadline impact: [UNCHANGED / +X days]
Financial impact: [Amount changes, if any]
Success probability: [X%]
Resolution date: [When domain re-assigned]

Notes: [Any qualitative notes about the failure or recovery]

---
```

### 6.2 Post-Mortem (After Wave Completion)

Once Wave 2 is complete and all contingencies are resolved, conduct a 30-min post-mortem:

**Attendees**: Project lead, any contingency-activated domain authors, peer reviewers (1–2)

**Questions to discuss**:
1. **What triggered the contingency?** (Was it preventable?)
2. **Did the activation process work as designed?** (Any bottlenecks?)
3. **What took longer than expected?** (Fallback search, onboarding, writing)
4. **What worked well?** (Learning to apply to Wave 3)
5. **What would you change next time?** (Process improvements)

**Outcome document**: 1-page summary saved to WAVE_2_INCIDENT_LOG.md Section "Lessons Learned"

---

## Part 7: Decision Tree Flowchart (Quick Reference)

```
CONTINGENCY ACTIVATION FLOWCHART
═══════════════════════════════════════════════════════════════════

Author triggers escalation (no-show, quality rejection, withdrawal)
  ↓
Q1: Does author want to continue but needs SUPPORT?
  ├─ YES → PATH A: Co-Author Pairing (Section 2.2)
  │         • Find co-author with complementary skills
  │         • 50/50 split of work + payment
  │         • Timeline: Activated same day; work begins Day 1
  │         • Success rate: ~85%
  │
  └─ NO: Continue to Q2

Q2: Are ALT tier authors available for this domain?
  ├─ YES → PATH B: Fallback Activation (Section 2.3)
  │         • Contact ALT author(s) in order of fitness score
  │         • First "yes" becomes fallback author
  │         • Full payment; same scope; original deadline
  │         • Success rate: ~80%
  │
  └─ NO ALT available: Continue to Q3

Q3: Can an adjacent domain absorb the failed domain's scope?
  ├─ YES → PATH C: Scope Reduction (Section 2.4)
  │         • Transfer 2–3 sections to adjacent domain
  │         • Adjacent author gets scope expansion + bonus payment
  │         • Deadline slip: +3 days for absorption + integration
  │         • Success rate: ~70%
  │
  └─ NO: Continue to Q4

Q4: Can a synthesizer compile Wave 1 + sources into condensed guide?
  ├─ YES → PATH D: Tier 3 Synthesis (Section 2.5)
  │         • Hire synthesizer to create 5,000–6,000 word condensed guide
  │         • Use Wave 1 research + provided sources (no new research)
  │         • Payment: $2,000 fixed fee
  │         • Deadline: UNCHANGED (3-week fixed timeline)
  │         • Success rate: ~60%
  │         • Note: Full-scope version deferred to Wave 3
  │
  └─ NO: ESCALATE to project lead + supervisor
          All contingency options exhausted
          Decision: Defer entire domain to Phase 6 Wave 3

═══════════════════════════════════════════════════════════════════
```

---

## Part 8: Appendix — Contingency Author Contact List

Maintain real-time list of fallback candidates (from WAVE_2_AUTHOR_PROFILE_CARDS.md):

**DOMAIN 60 FALLBACK CANDIDATES** (by fitness score):
1. Candidate X (19/25) — Contact: [Email] | [Phone] | [Timezone]
2. Candidate Y (18/25) — Contact: [Email] | [Phone] | [Timezone]
3. Candidate Z (18/25) — Contact: [Email] | [Phone] | [Timezone]

**DOMAIN 61 FALLBACK CANDIDATES**:
[Similar structure]

[Repeat for Domains 62–65]

**CO-AUTHOR POOL** (for Path A):
- Wave 1 authors willing to co-author (and which domains)
- Graduate students / research assistants with practitioner writing background
- Community editors (pivot to co-author if needed)

**SYNTHESIZER POOL** (for Path D):
- Tier B authors willing to synthesize instead of full-author (and which domains)
- Graduate students / research assistants with synthesis capability
- Wave 1 authors available for synthesis work (paid extra)

---

## Part 9: Success Criteria & Metrics

**Wave 2 success = all 6 domains published by Sept 15:**

| Metric | Target | Acceptable | Failure |
|--------|--------|-----------|---------|
| **Contingency count** | 0 | 1–2 (max 33% of domains) | ≥3 (>50%) |
| **Days to contingency activation** | <24 hrs of trigger | <48 hrs | >48 hrs |
| **Path success rate** | 100% recovery | 80%+ (5–6 domains recovered) | <80% (4 or fewer recovered) |
| **Deadline slip** | 0 days (original deadline) | 0–7 days | >7 days or past Sept 15 |
| **Quality of contingency documents** | 12/12 elements | 11/12 elements | <11/12 elements |

---

## Document Status

This contingency plan is **PRODUCTION-READY** and available for activation on-demand from June 14 onward.

**Probability of activation**: Historical data suggests 1–2 contingencies per 6-domain wave (15–33% of domains). Prepare for this; do not be surprised if activated.

For questions about contingency procedures before execution, contact [Project Lead] by June 13.

---

## Related Documents

- `WAVE_2_CONTENT_ASSIGNMENT_PROTOCOL.md` — Assignment process (Section 5 escalations lead to this plan)
- `WAVE_2_DELIVERY_LOGISTICS.md` — Quality acceptance criteria (use for synthesized documents)
- `WAVE_2_AUTHOR_PROFILE_CARDS.md` — Fallback candidate profiles (reference for paths B & D)
- `WAVE_2_AUTHOR_MATCHING_ALGORITHM.md` — Scoring methodology (understand why certain authors are fallbacks)
