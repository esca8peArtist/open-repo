---
title: "Wave 2 Recruitment Pre-Checklist — June 14–15 Execution Prerequisites"
project: systems-resilience
phase: 5/6
wave: 2
status: READY-FOR-EXECUTION
purpose: "Pre-recruitment verification checklist for Phase 6 Wave 2 author matching session (June 14–15, 2026). All author contact info verified, Nextcloud permissions pre-staged, matching materials ready, communication templates prepared."
execution_date: 2026-06-14
execution_window: "2026-06-14 14:00 UTC – 2026-06-15 19:00 UTC"
cutoff_for_matching_input: "2026-06-13 18:00 UTC"
---

# Wave 2 Recruitment Pre-Checklist
## June 14–15 Author Matching Session Prerequisites

---

## Executive Summary

**Purpose**: Ensure all prerequisites are complete 24 hours before Wave 2 matching session (June 14, 14:00 UTC start)

**Timeline**: 
- June 10–13: Final author contact verification + Nextcloud permissions staging
- June 13, 18:00 UTC: Cutoff for new author intake forms
- June 14, 14:00 UTC: Begin matching session
- June 14–15, 19:00 UTC: Matching complete, author offers sent

**Success Criteria**:
- All 54 Wave 2 candidate contacts verified and current
- Author readiness intake forms 100% collected (or documented as non-responders)
- Nextcloud permissions pre-staged for 8 author cohorts (ready to activate post-match)
- Recruitment communication templates ready to send
- Matching algorithm materials (profile cards, scoring rubric) prepped and reviewed
- Go/no-go decision made (can we proceed with 54 candidates, or do we need to add more?)

**Prerequisite Completion Target**: June 13, 23:59 UTC (all pre-checks complete 18 hours before matching starts)

---

## SECTION 1: Author Contact Information Verification

### 1.1 Wave 2 Candidate List Finalization

**Status Check**: 
- [ ] 54 Wave 2 candidates identified across 6 domains (see profile cards)
- [ ] Each candidate has: email, phone (if available), timezone, confirmed expertise area
- [ ] Candidate list matches `WAVE_2_AUTHOR_PROFILE_CARDS.md` (updated June 6)

**Verification Actions** (complete by June 12):

1. **Open Candidate Contact Database** (or spreadsheet)
   - Source: `WAVE_2_AUTHOR_PROFILE_CARDS.md` — extract all emails and phone numbers
   - Create working spreadsheet: `wave2-candidate-contacts-verification-june2026.xlsx`
   - Columns: Name | Email | Phone | Timezone | Domain | Contact Status | Notes

2. **Email Verification** (Gmail, LinkedIn, org websites)
   - For each candidate, verify email address:
     - Does email still exist? (Check bounces on test send if necessary)
     - Has email changed? (Cross-check with LinkedIn, organizational directory)
     - Is email monitored? (If person changed jobs, confirm they're still reachable)
   
   - **Method**: 
     - Open each candidate's LinkedIn or professional website
     - Confirm current email matches profile card email
     - If email is old: attempt to find updated contact info (check recent publications, org website, Twitter/X bio)
   
   - **Status Recording**:
     - ✅ Email verified current
     - ⚠️ Email old but forwarding confirmed (person replies when contacted)
     - ❌ Email likely invalid (bounces or person unreachable at that address)
   
   - **Action for Invalid Emails**: 
     - If ❌ status: Do NOT include in matching unless backup email found
     - Document as "Contact Info Stale — cannot proceed with outreach"

3. **Phone Verification** (if phone number in profile)
   - Verify phone is associated with candidate:
     - Call/text and confirm identity (brief: "Hi [name], confirming this is your contact number for Wave 2 recruitment")
     - Or: Skip phone verification for now; use email as primary contact method
   
   - **Status Recording**:
     - ✅ Phone verified
     - ⚠️ Phone voicemail confirmed belongs to candidate
     - ⚠️ Phone not reached but email will be primary contact method
     - ❌ Phone invalid

4. **Timezone Confirmation**
   - For international candidates: confirm timezone in profile card is correct
   - Method: Ask during next interaction or look at candidate's LinkedIn location
   - Record actual timezone (not assumed)
   - Note: Wave 2 recruitment calls happen 14:00–19:00 UTC; some timezones may be inconvenient but workable

**Completion Target**: June 12, 23:59 UTC
- [ ] All 54 candidates have verified email addresses
- [ ] Phone numbers updated if out-of-date (or marked as N/A if not available)
- [ ] Timezones confirmed for all candidates
- [ ] Spreadsheet complete with zero "Cannot Contact" entries

**Expected Result**: 54 candidates with valid contact information ready for outreach

---

### 1.2 Author Readiness Intake Form Collection

**Purpose**: Collect final capacity/availability data from candidates before matching

**Timeline**:
- June 10, 09:00 UTC: Email all 54 candidates with intake form link + 72-hour response deadline
- June 13, 18:00 UTC: **HARD CUTOFF** — stop accepting new forms; compile results
- June 14, 09:00 UTC: Matching team reviews all intake forms before session start

**Intake Form** (source: `AUTHOR_READINESS_INTAKE_FORM.md`):

The intake form captures:
1. **Availability**: Hours per week available July 16 – September 15 (9-week sprint)
2. **Expertise**: Self-assessed depth in assigned domain (1-5 scale)
3. **Writing Experience**: Prior research/writing projects; output quality
4. **Technical Capacity**: GitHub access? Markdown experience? Can participate in async collaboration?
5. **Personal Circumstances**: Any constraints (family, health, work commitments) that might affect availability?
6. **Timezone**: Confirmed timezone for scheduling meetings

**Distribution** (June 10, 09:00 UTC):

Send email to all 54 candidates:

```
Subject: Wave 2 Author Program — Availability & Readiness Form (Deadline: June 13, 18:00 UTC)

Dear [Candidate Name],

Thank you for your interest in Phase 6 Wave 2 of the Systems Resilience project.

We are recruiting 6–8 authors per domain to expand the Phase 5 research into Phase 6 
domains (International Coordination, Intergenerational Knowledge, Infrastructure, Ecosystem 
Restoration, Economic Resilience, Institutional Learning).

NEXT STEP: Complete this brief intake form by June 13 at 18:00 UTC.

[LINK TO INTAKE FORM]

The form takes 8–10 minutes and asks about:
- Your availability (hours/week, July–September)
- Your expertise in your target domain
- Prior writing/research experience
- Technical setup (GitHub, Markdown, async collaboration)
- Any personal constraints that might affect participation

Your responses help us match you with the right domain and team.

TIMELINE:
- June 13, 18:00 UTC: Intake form deadline
- June 14–15: Author matching (we contact matched authors with formal offers)
- June 16: Onboarding begins (if you accept)
- July 16: Writing sprint starts (July 16 – September 15)

Questions? Reply to this email.

Best regards,
[Orchestrator Name]
Systems Resilience Project
```

**Tracking Responses** (June 10–13):

Create intake tracking spreadsheet:
```
Name | Email | Form Submitted | Date | Status | Availability Hours | Domain Preference
[candidate] | [email] | ✅ YES | June 11 10:30 | READY | 8 hrs/week | Governance
[candidate] | [email] | ⚠️ PARTIAL | June 12 | FOLLOW-UP NEEDED | — | —
[candidate] | [email] | ❌ NO | — | NON-RESPONDER | — | —
```

**Follow-Up Actions** (June 11–13):

- **June 11, 18:00 UTC**: First followup to non-responders
  - Email: "Quick reminder: intake form deadline is June 13, 18:00 UTC. Please reply by then."
  
- **June 13, 14:00 UTC**: Final followup to remaining non-responders
  - Email: "Final reminder: intake form deadline in 4 hours (18:00 UTC). Please respond if interested."
  
- **June 13, 18:00 UTC**: HARD CUTOFF
  - Stop accepting new intake forms
  - Compile results spreadsheet
  - Identify non-responders (mark as "Non-Responsive" — may not be included in matching unless contingency needed)

**Completion Target**: June 13, 18:00 UTC
- [ ] At least 45 of 54 candidates have submitted intake forms (83%+ response rate expected)
- [ ] All form responses compiled into summary spreadsheet
- [ ] Non-responders identified and documented
- [ ] No new forms accepted after 18:00 UTC

**Expected Result**: 45–54 candidates ready for matching with confirmed availability data

---

## SECTION 2: Nextcloud Permissions Pre-Staging

### 2.1 Author Workspace Structure Creation

**Purpose**: Create Nextcloud folders for each of 8 Wave 2 author cohorts BEFORE authors are matched. When matching completes (June 14–15), we can immediately activate access without delays.

**Timeline**: June 10–12 (complete 48 hours before matching session)

**Folder Structure** (to be created in Nextcloud on raspby1):

```
/Phase-6-Author-Workspaces/
├── Domain-60-International-Coordination/
│   ├── 01-Research-Materials/
│   │   ├── Phase-5-Referenced-Sources.md
│   │   └── [source PDFs]
│   ├── 02-Draft-Area/
│   │   └── [author-draft-content]
│   ├── 03-Shared-Resources/
│   │   ├── Templates/
│   │   ├── Style-Guide.md
│   │   └── Feedback-Protocol.md
│   └── 04-Communication/
│       └── [Weekly-check-in-notes]
│
├── Domain-61-Intergenerational-Knowledge/
│   ├── 01-Research-Materials/
│   ├── 02-Draft-Area/
│   ├── 03-Shared-Resources/
│   └── 04-Communication/
│
[Repeat for Domains 62, 63, 64, 65]
```

**Creation Steps** (June 10–12):

1. **SSH to Nextcloud server** (raspby1):
   ```bash
   ssh <user>@100.70.184.84
   # Navigate to Nextcloud file directory
   cd /var/www/nextcloud/data/admin/files
   # or: use Nextcloud UI to create folders
   ```

2. **Create root folder**: `/Phase-6-Author-Workspaces/`

3. **For each of 6 domains**, create:
   - Main domain folder (named by domain)
   - Subfolders: 01-Research-Materials, 02-Draft-Area, 03-Shared-Resources, 04-Communication

4. **Populate Research Materials folder** (for each domain):
   - Copy relevant Phase 5 documents
   - Copy decision support documents
   - Copy source library documents
   - Example for Domain 60 (International Coordination):
     - `PHASE_5_WAVE_1_2_INTEGRATED_CORPUS.md`
     - `PHASE_5_PUBLICATION_READINESS_CHECKLIST.md` (context for authors)
     - Source documents for international systems (UN, transnational organizations, etc.)

5. **Populate Shared Resources folder** (for each domain):
   - Copy `WAVE_2_AUTHOR_ONBOARDING_KIT_DUAL_PLATFORM.md`
   - Copy `WAVE_2_RECRUITMENT_COMMUNICATION_TEMPLATES.md` (for authors' reference)
   - Copy domain-specific style guide (if created; otherwise create generic version)
   - Create feedback protocol document (template below)

6. **Feedback Protocol Template** (for Shared Resources):
   ```markdown
   # Wave 2 Author Feedback & Revision Protocol
   
   ## Timeline
   - Week 1–2: Author research and outlining
   - Week 3–6: First draft (uploaded to 02-Draft-Area)
   - Week 6: Orchestrator feedback (comments in shared document)
   - Week 7–8: Author revisions
   - Week 8: Final submission and review
   
   ## Feedback Format
   - Comments use Nextcloud markdown: [comment text]
   - Tracked changes (highlight + comment) for major revisions
   - Track changes use format: ~~deleted text~~ **→ inserted text**
   
   ## Revision Expectations
   - Tier A authors: Revision turnaround 5 days
   - Tier B authors: Revision turnaround 7 days
   - Tier C authors: Revision turnaround 10 days
   ```

7. **Communication folder setup** (for each domain):
   - Create template for weekly check-in notes
   - Create Q&A thread (Nextcloud comments feature)

**Completion Target**: June 12, 23:59 UTC
- [ ] All 6 domain folders created with subfolder structure
- [ ] Research materials populated for each domain
- [ ] Shared resources created (templates, style guide, feedback protocol)
- [ ] Communication folder templates ready
- [ ] Folder structure reviewed (spot-check: can open each folder, files present)

**Expected Result**: Empty author workspaces ready for immediate permission activation on June 14

---

### 2.2 Permission Pre-Configuration

**Purpose**: Pre-configure Nextcloud permission groups so that once authors are matched, their access can be activated in < 5 minutes without manual setup.

**Setup Steps** (June 12–13):

**In Nextcloud Admin Panel**:

1. Create Nextcloud user groups (Admin → Users → Groups):
   - `wave2-domain-60-authors`
   - `wave2-domain-61-authors`
   - `wave2-domain-62-authors`
   - `wave2-domain-63-authors`
   - `wave2-domain-64-authors`
   - `wave2-domain-65-authors`

2. For each domain group, configure folder permissions:
   - **Path**: `/Phase-6-Author-Workspaces/Domain-XX-*/`
   - **Permissions**: Read + Write for all authors in domain
   - **Note**: Permissions NOT YET ASSIGNED to users (users will be added post-match)

3. Create a broadcast group (optional):
   - Group: `wave2-all-authors` (all authors across all domains)
   - Purpose: Shared resources, announcements, all-hands updates
   - Folder: `/Phase-6-Author-Workspaces/00-All-Authors-Shared/`
   - Contents: Overall project timeline, communication norms, conflict resolution procedures

4. Document permission matrix (for post-match activation):
   ```
   Domain 60 Authors
   ├── User: [name] (tier assignment)
   ├── User: [name] (tier assignment)
   └── User: [name] (tier assignment)
   
   (Add to group: wave2-domain-60-authors)
   (Grant access to: /Phase-6-Author-Workspaces/Domain-60-*/*)
   ```

**Completion Target**: June 13, 18:00 UTC
- [ ] All 6 domain groups created in Nextcloud
- [ ] All domain folders have permission rules configured (not yet activated)
- [ ] Broadcast group created
- [ ] Permission matrix documented (ready to populate with matched authors)

**Post-Match Activation** (June 14, 19:00 UTC):
Once authors are matched, rapid activation:
```bash
# For each matched author in Domain 60:
# 1. Create Nextcloud user account (or use existing if they have one)
# 2. Add user to wave2-domain-60-authors group
# 3. Grant access to domain-60 workspace
# 4. Send access notification email

# Total time per author: 2–3 minutes
# Total time for 30–40 authors: 60–120 minutes
```

---

## SECTION 3: Matching Materials Preparation

### 3.1 Author Matching Algorithm Materials Review

**Status Check** (complete by June 12):

- [ ] `WAVE_2_AUTHOR_MATCHING_ALGORITHM.md` reviewed and current (dated June 6 or later)
- [ ] Scoring rubric understood (5 dimensions: domain expertise, network reach, writing capacity, timezone, prior wave)
- [ ] Matching constraints documented (capacity limits, timezone diversity, conflict-of-interest rules)
- [ ] Worked examples reviewed (how to handle edge cases: withdrawals, overflow, tie-breaking)

**Preparation Actions**:

1. **Print/Digital Setup**:
   - [ ] Open `WAVE_2_AUTHOR_MATCHING_ALGORITHM.md` and `WAVE_2_AUTHOR_PROFILE_CARDS.md` in side-by-side windows (June 14 matching session will use both)
   - [ ] Create matching spreadsheet template (see Section 3.3 below)
   - [ ] Print profile cards (if physical matching session preferred) or have digital copies ready

2. **Review Scoring Rubric** (refresh on June 13):
   - Primary scores: D1 (Domain Expertise), D2 (Long-Form Practitioner), D3 (Markdown/Digital), D4 (Research & Citation), D5 (Practitioner Grounding)
   - Secondary scores: S1 (Network Reach), S2 (Writing Capacity), S3 (Timezone Alignment), S4 (Prior Wave Success)
   - Tier thresholds: Tier A = 20–25 pts, Tier B = 14–19, Tier C = <14 or constraint failure

3. **Review Matching Constraints**:
   - Domain minimums: Each domain has minimum scores for D1 and D5 (see profile cards)
   - Capacity limits: Target 4–8 authors per domain, ~30–40 total recruited
   - Timezone diversity: At least 2 timezones represented per domain (enables asynchronous work + sync meetings)
   - Wave 1 bias: If candidate was Wave 1 author, higher confidence in capacity assessment

4. **Review Edge Case Procedures**:
   - **Withdrawal**: If a matched author declines offer → move to next-ranked backup from same domain
   - **Overflow**: If more Tier A candidates than capacity → use tie-breaking (network reach > timezone diversity > alphabetical)
   - **Underflow**: If domain has < 3 Tier A/B candidates → recruit Tier C with contingency note
   - **Conflict of Interest**: If two authors work at same org → document, assess independence risk, proceed if low

**Completion Target**: June 13, 23:59 UTC
- [ ] Matching materials reviewed and understood
- [ ] Scoring rubric fresh in mind (re-read if last reviewed > 1 week ago)
- [ ] Matching spreadsheet template prepared
- [ ] Edge case procedures reviewed

**Expected Result**: Matching team ready to score and assign 54 candidates in ~6-hour June 14–15 session

---

### 3.2 Author Cohort Definition Review

**Purpose**: Confirm 8 author cohort assignments (these groups will coordinate during Wave 2 sprint)

**Status Check** (complete by June 12):

- [ ] 8 cohorts defined (typically: 1 primary author per domain + 3–7 supporting authors + 1 reviewer)
- [ ] Cohort roles documented:
  - **Primary Author**: Leads research synthesis, writes first draft
  - **Research Contributors**: Help gather sources, validate findings
  - **Writing Contributors**: Help with outlining, editing, final copy
  - **Domain Reviewer**: External expert review (if applicable)

**Cohort Structure** (example for Domain 60 — International Coordination):

```
Domain 60: International Coordination Frameworks
Tier A (Primary): 1 author (lead researcher/writer)
Tier B (Supporting): 2–3 authors (research, writing, feedback)
Tier C (Contributor): 1–2 authors (specific expertise, targeted research)
External Reviewer: 1 (domain expert external review, if available)

Target composition: 1 A + 2 B + 1 C = 4 authors
```

**Cohort Review Steps**:

1. Open `WAVE_2_AUTHOR_MATCHING_ALGORITHM.md` Section 4: "Matching Output and Cohort Assembly"
2. Review each domain's target composition (primary + supporting + contributors)
3. Confirm that matching algorithm respects these roles (Tier A candidates are assigned primary roles; Tier B assigned supporting)
4. Document any domain with special constraints (e.g., Domain 63 Ecosystem Restoration may need 2 primary authors if scope is large)

**Completion Target**: June 12, 23:59 UTC
- [ ] All 8 cohort compositions understood
- [ ] Role descriptions finalized
- [ ] Domain constraints documented
- [ ] Backup cohort compositions identified (if primary match unavailable)

---

### 3.3 Matching Execution Spreadsheet Template

**Purpose**: Real-time tracking of scoring and assignment during June 14–15 session

**Create Spreadsheet** (e.g., Google Sheets or LibreOffice Calc):

**Columns**:
```
| Rank | Name | Domain | D1 | D2 | D3 | D4 | D5 | Subtotal | S1 | S2 | S3 | S4 | Tier | Assigned? | Cohort Role | Notes |
|------|------|--------|----|----|----|----|----|-----------|----|----|----|----|----|-----------|---------|-------|
```

**Instructions for Use** (June 14, 14:00 UTC):
1. Import all 54 candidates from profile cards into this spreadsheet
2. For each candidate, verify primary scores (D1–D5) match profile cards or update with intake form data
3. Calculate tier (sum of primary scores; apply tier thresholds)
4. Rank candidates by tier, then by secondary scores
5. For each domain, assign candidates from top-ranked matches down:
   - Assign top Tier A candidate as Primary Author
   - Assign next 2 Tier A/B candidates as Supporting Authors
   - Assign Tier C candidate as Contributor (if needed)
6. Document any exceptions (constraints, tie-breaking, withdrawals)

**Example Row**:
```
2 | Aaron Vansintjan | 60 (Intl Coord) | 4 | 4 | 3 | 4 | 4 | 19 | 16 | 12 | 11 | 10 | B | YES | Primary | Warm intro, strong network
```

**Completion Target**: June 13, 23:59 UTC
- [ ] Spreadsheet template created and formatted
- [ ] Sample 5–10 candidates pre-populated as practice run
- [ ] Column formulas tested (tier calculation, ranking)
- [ ] Spreadsheet ready for June 14 live use

---

## SECTION 4: Communication Templates Preparation

### 4.1 Wave 2 Offer Email Template

**Purpose**: Send formal matching offers to selected authors on June 14–15

**Status Check** (complete by June 12):

- [ ] Offer email template drafted (source: `WAVE_2_RECRUITMENT_COMMUNICATION_TEMPLATES.md`)
- [ ] Template personalized with:
  - Candidate name
  - Domain name and scope
  - Writing sprint details (July 16 – September 15)
  - Compensation (if applicable)
  - Support resources (research materials, templates, mentoring)
  - Decision deadline (72 hours to respond)

**Offer Email Template** (generic version):

```
Subject: Formal Offer: Phase 6 Wave 2 Author — Domain [X]: [Domain Name]

Dear [Author Name],

Based on your expertise, availability, and match with our research needs, we are pleased 
to offer you a position as a Wave 2 author on the Systems Resilience project.

ASSIGNMENT:
  Domain: [Domain Name]
  Role: [Primary Author / Supporting Author / Research Contributor]
  Duration: July 16 – September 15, 2026 (9 weeks)
  Commitment: [6–8] hours per week
  
RESEARCH SCOPE:
  [1–2 sentence description of domain focus]
  
  You'll be working with [1–3 other authors] to synthesize Phase 5 research and create 
  a practitioner-focused guide for [target audience].

SUPPORT PROVIDED:
  • Research materials and source library
  • Writing templates and style guide
  • Weekly check-in meetings with domain lead
  • Feedback on first draft (within 5–7 days)
  • Access to Nextcloud workspace (shared documents, async collaboration)
  
NEXT STEPS:
  1. Reply to this email by [DATE + 72 hours] confirming you accept this offer
  2. June 16: Onboarding begins (Nextcloud access, domain briefing, materials review)
  3. July 1: Final research materials provided; writing sprint prep
  4. July 16: Writing sprint officially begins
  
COMPENSATION:
  [If applicable: $X per hour, estimated $Y total for ~60 hours of work]
  
QUESTIONS?
  Reply to this email or schedule a 15-min call: [link to calendar]

We're excited to have you as part of this project. Phase 5 has been a comprehensive 
effort; Wave 2 will expand it into six new domains critical for long-term community resilience.

Best regards,
[Orchestrator Name]
Systems Resilience Project
[Contact Email]
```

**Customization for Each Author**:
- Name
- Domain assignment
- Role (Primary / Supporting / Contributor) — varies by tier
- Specific target audience for domain
- Co-author names (if available before offer sent)
- Compensation (if not standardized across all authors, customize per tier)

**Delivery Method** (June 14–15):
- Send offers via email (primary)
- For high-priority authors: follow up with phone call if email not confirmed within 12 hours
- Track responses in spreadsheet (Accepted / Pending / Declined)

**Completion Target**: June 13, 18:00 UTC
- [ ] Offer email template finalized
- [ ] Customization placeholders clearly marked [LIKE THIS]
- [ ] Template tested (send sample offer to team member)
- [ ] Ready to send to 30–40 matched authors on June 14

---

### 4.2 Wave 2 Onboarding Kit Finalization

**Purpose**: Prepare comprehensive onboarding materials for authors who accept offers

**Status Check** (complete by June 12):

- [ ] `WAVE_2_AUTHOR_ONBOARDING_KIT_DUAL_PLATFORM.md` reviewed and current
- [ ] Kit includes:
  - Welcome email
  - Nextcloud/Discourse access instructions
  - Domain briefing document (research direction, target audience, scope)
  - Writing templates and style guide
  - Communication norms and meeting schedule
  - Support contact info (orchestrator, domain lead, peer authors)
  - Calendar (milestones: June 16 onboarding, July 1 materials, July 16 sprint start)

**Preparation Steps** (June 12–13):

1. **Customize onboarding kit per domain**:
   - Domain 60 (Intl Coordination): Focus on transnational systems, governance frameworks
   - Domain 61 (Intergenerational): Focus on knowledge transfer, long-term planning
   - Domain 62 (Infrastructure): Focus on interdependencies, resilience
   - Domain 63 (Ecosystem): Focus on restoration, biodiversity
   - Domain 64 (Economic): Focus on alternative economics, local systems
   - Domain 65 (Institutional): Focus on governance, organizational learning

2. **Create domain-specific briefing document** (if not already created):
   - 1–2 page overview of domain scope
   - Key research questions
   - Target readers (household level? community scale? region?)
   - Relationship to Phase 5 (how does this domain extend Phase 5 work?)
   - Timeline and milestones
   - Key literature to review

3. **Finalize writing template**:
   - Outline structure (e.g., Executive Summary → Sections 1–5 → Implementation Checklist → Citations)
   - Word count target (typically 8,000–12,000 words based on Phase 5 documents)
   - Citation format (numbered references [1], [2], etc.)
   - Markdown formatting guidelines

4. **Prepare communication norms document**:
   - Weekly check-in meeting: [Day + Time in UTC] (e.g., Tuesday 15:00 UTC)
   - Async communication platform: Nextcloud shared documents + email
   - Response time expectations: 24–48 hours for questions; 5–7 days for feedback
   - Escalation procedure (if author feels stuck or unsupported)

**Completion Target**: June 13, 18:00 UTC
- [ ] Onboarding kit reviewed and updated
- [ ] Domain-specific briefing documents created (6 total, 1 per domain)
- [ ] Writing template finalized
- [ ] Communication norms documented
- [ ] All materials ready to send to authors post-acceptance

---

## SECTION 5: Go/No-Go Decision Framework

### 5.1 Go/No-Go Criteria

**Decision Point**: June 13, 23:59 UTC (24 hours before matching session)

**Go Criteria** (all must be met):

| Criterion | Target | Actual | Status |
|-----------|--------|--------|--------|
| Author contact verification | 54/54 contacts valid | ___/54 | [ ] |
| Intake form response rate | 80%+ (43+/54) | ___/54 | [ ] |
| Nextcloud folders created | 6 domains + subfolders | [ ] | [ ] |
| Permission structure ready | 6 domain groups + rules | [ ] | [ ] |
| Matching materials prepared | Algorithm, profile cards, spreadsheet | [ ] | [ ] |
| Offer email template ready | Customizable, tested | [ ] | [ ] |
| Onboarding kit ready | 6 domain-specific kits | [ ] | [ ] |
| Team briefing complete | All personnel understand process | [ ] | [ ] |

**No-Go Triggers** (pause matching if any occur):

- **Contact Information**: >10 candidates without valid email (cannot send offers)
- **Intake Forms**: <35 responses (insufficient data for confident matching)
- **Nextcloud**: Not operational or permission structure not ready (will delay author access)
- **Matching Materials**: Algorithm or profile cards missing/outdated (cannot execute matching)
- **Templates**: Offer email or onboarding kit incomplete (unprofessional or confusing communications)
- **Team**: Key personnel unavailable June 14–15 (cannot execute matching session)

**No-Go Resolution**:
If no-go triggered:
- Identify blockers
- Estimate resolution time
- Propose new matching date (typically June 21–22 if delay > 2 days)
- Notify all stakeholders of delay

### 5.2 Final Decision Checklist (June 13, 18:00 UTC)

**Complete this checklist exactly 24 hours before matching session**:

- [ ] All 54 candidate contacts verified and current
- [ ] Intake forms collected: ___/54 submitted (target: 43+)
- [ ] Nextcloud domain folders created and populated (6 domains complete)
- [ ] Permission groups configured (6 groups + rules ready)
- [ ] Matching algorithm reviewed and understood by matching team
- [ ] Profile cards reviewed (scores verified against intake form data)
- [ ] Matching spreadsheet template created and tested
- [ ] Offer email template drafted, personalized placeholders clear, tested
- [ ] Onboarding kits prepared (6 domain-specific versions ready)
- [ ] All matching team members available June 14, 14:00 UTC
- [ ] Calendar blocked: June 14–15 matching session (6 hours/day expected)
- [ ] No blockers identified; ready to proceed

**Final Decision**:
- [ ] **GO** — Execute matching session on schedule (June 14, 14:00 UTC)
- [ ] **NO-GO** — Pause and reschedule to [new date]. Blocker: [brief description]

**Sign-Off**: 
- Orchestrator: ________________  Date: ________
- Matching Team Lead: ________________  Date: ________

---

## SECTION 6: Post-Matching Execution Timeline

### 6.1 June 14–15: Matching Session

**Schedule**:
- **June 14, 14:00–19:00 UTC** (5 hours): Day 1 Matching
  - Score all 54 candidates (parallel teams by domain)
  - Assign primary + supporting authors for each domain
  - Identify backup candidates (in case of withdrawals)
  - Document any edge cases (constraints, tie-breaking decisions)

- **June 15, 14:00–17:00 UTC** (3 hours): Day 2 Offer Execution
  - Send formal offers to matched authors (all 30–40 primary/supporting authors)
  - Log all offers sent with timestamps
  - Monitor for early responses (some authors will accept within hours)
  - Call high-priority authors if email not confirmed within 12 hours

### 6.2 June 15–18: Acceptance Tracking & Access Activation

- **June 15, 17:00 UTC**: First batch of acceptances logged
- **June 16–18**: Nextcloud permissions activated for accepted authors
  - Add confirmed authors to domain groups
  - Grant workspace access
  - Send Nextcloud access notification emails
- **June 16–18**: Onboarding briefing calls scheduled (15-min video calls with each author)
  - Confirm domain scope, timeline, expectations
  - Answer questions
  - Provide research materials briefing

### 6.3 June 21: Wave 2 Cohort Kickoff Meeting

**All-hands kickoff** (all Wave 2 authors across 6 domains):
- Welcome and project context
- Timeline walkthrough
- Introductions (authors meet co-authors)
- Q&A
- Assignment of domain leads (who coordinates which domain)

---

## APPENDIX A: Wave 2 Recruitment Pre-Checklist Completion Summary

**Checklist Created**: June 6, 2026
**Checklist Review Date**: June 13, 2026 (24 hours before matching)
**Target Completion**: June 13, 23:59 UTC

**Completion Status** (to be filled in June 13):

**Section 1: Author Contact Verification**
- [ ] 54 candidates with valid contact info (emails verified)
- [ ] Intake forms: ___/54 submitted (target 43+)
- [ ] Non-responders documented: ___/54
- [ ] Contact status: [ ] READY TO PROCEED

**Section 2: Nextcloud Pre-Staging**
- [ ] 6 domain folders created with subfolder structure
- [ ] Research materials populated per domain
- [ ] Permission groups configured (6 domain groups + 1 broadcast group)
- [ ] Nextcloud status: [ ] READY TO ACTIVATE

**Section 3: Matching Materials**
- [ ] Author matching algorithm reviewed
- [ ] Scoring rubric understood
- [ ] Matching constraints documented
- [ ] Spreadsheet template prepared
- [ ] Matching materials status: [ ] READY FOR SESSION

**Section 4: Communication Templates**
- [ ] Offer email template finalized
- [ ] Onboarding kits prepared (6 domain versions)
- [ ] Communication norms documented
- [ ] Templates status: [ ] READY TO SEND

**Section 5: Go/No-Go Decision**
- [ ] All go-criteria met
- [ ] No blockers identified
- [ ] Final decision: [ ] GO / [ ] NO-GO

**Overall Status**: [ ] READY FOR JUNE 14 MATCHING SESSION

---

*Wave 2 Recruitment Pre-Checklist Complete*  
*All prerequisites in place for June 14–15 matching execution*  
*Next step: Execute matching session per WAVE_2_AUTHOR_MATCHING_ALGORITHM.md*
