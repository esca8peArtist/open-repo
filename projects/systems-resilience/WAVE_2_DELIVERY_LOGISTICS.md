---
title: "Wave 2 Delivery Logistics"
project: systems-resilience
phase: 5/6
wave: 2
status: PRODUCTION-READY
purpose: "Complete specification of file formats, submission mechanics, revision timelines, and quality acceptance"
created: 2026-06-07
execution_deadline: 2026-07-16 (author submission start)
target_audience: "Authors + peer reviewers executing Wave 2 writing/review cycle"
---

# Wave 2 Delivery Logistics
## Phase 6 Domains 60–65 — File Formats, Submission Mechanics, and Quality Acceptance

> **This document specifies exactly how authors submit, how reviewers assess, and how documents are accepted or rejected.** It is the single source of truth for deliverable format, citation style, word count, metadata, and revision timelines. All authors should read this document before June 30 outline submission.

---

## Part 1: Deliverable File Format Specification

### 1.1 File Naming Convention

**Format**: `Domain_[60-65]_[Author_Last_Name]_[Revision_Number].md`

**Examples**:
- `Domain_63_Kloppenburg_v1.md` (first draft)
- `Domain_63_Kloppenburg_v2.md` (after revision 1)
- `Domain_63_Kloppenburg_v3_FINAL.md` (accepted final)

**File structure**:
- All deliverables must be valid Markdown (.md file extension)
- UTF-8 encoding (standard for all text files)
- Line endings: LF (Unix-style, not CRLF/Windows)
- No embedded images or binary files (citations/sources only)

---

### 1.2 YAML Front Matter (Required)

Every deliverable must begin with this YAML metadata block:

```yaml
---
title: "[Domain Name]: Practitioner Guide for Zone 5 Communities"
domain: "[60/61/62/63/64/65]"
author: "[Full Author Name]"
author_email: "[Author Email]"
author_timezone: "[Timezone, e.g., CDT, EDT, CET]"
created: "[ISO date: YYYY-MM-DD]"
last_revised: "[ISO date: YYYY-MM-DD]"
revision_number: "[v1 / v2 / v3 etc.]"
submission_round: "[1st draft / Revision Round 1 / Final]"
word_count: "[XXXX words]"
source_count: "[XX sources]"
peer_reviewer: "[Reviewer Name]"
peer_review_date: "[Date reviewed, or TBD if first submission]"
acceptance_status: "[DRAFT / REVISION-NEEDED / ACCEPTED / REJECTED]"
---
```

**Notes**:
- `submission_round` must be one of: "1st Draft", "Revision Round 1", "Revision Round 2", "Final"
- `acceptance_status` MUST be updated by project lead after peer review (author does not fill this)
- `word_count` and `source_count` auto-filled at submission time (author counts; project lead verifies)

**Example complete YAML**:
```yaml
---
title: "Ecosystem Restoration: Practitioner Guide for Zone 5 Communities"
domain: "63"
author: "Jack Kloppenburg"
author_email: "jwkloppe@wisc.edu"
author_timezone: "CDT"
created: "2026-07-16"
last_revised: "2026-07-30"
revision_number: "v1"
submission_round: "1st Draft"
word_count: "9,847"
source_count: "28"
peer_reviewer: "[Name to be assigned]"
peer_review_date: "TBD"
acceptance_status: "DRAFT"
---
```

---

### 1.3 Content Structure: Required Sections

Every deliverable must contain these sections in this order:

**Section 1: Introduction (600–800 words)**
- Title: `## 1. Introduction: [Domain Name] in Zone 5 Context`
- Content: Define the domain, why it matters for Zone 5 communities, scope of this guide
- Must address: What's at stake if this domain fails? Why is it relevant NOW?
- Tone: Hook reader with a concrete scenario/challenge, then broaden to principle

**Section 2: Core Frameworks & Theory (1,200–1,600 words)**
- Title: `## 2. Core Frameworks: [Specific framework #1] and [Specific framework #2]`
- Content: The key conceptual/theoretical foundations authors/practitioners rely on
- Must include: 2–3 major frameworks/models, cited with 8–12 sources total
- Structure: Define framework → show application in Zone 5 context → cite examples
- Tone: Explanatory; use examples to ground abstract concepts

**Section 3: Practice Examples & Case Studies (1,500–2,000 words)**
- Title: `## 3. Case Studies: [Geography/Example #1], [Example #2], [Example #3]`
- Content: 2–4 concrete examples of the domain in practice (3–5 yrs old minimum; recent preferred)
- Must include: Who did it? What did they do? What worked? What didn't? Lessons learned.
- Structure: One subsection per case study (use `### 3.1`, `### 3.2` etc.)
- Tone: Narrative; make real people/places visible; be specific
- Requirement: At least 1 case study must be Zone 5 Midwest (Wisconsin, Minnesota, Iowa, Illinois, Missouri, or adjacent)

**Section 4: Failure Modes & Common Challenges (1,200–1,600 words)**
- Title: `## 4. When Things Go Wrong: Common Failure Modes`
- Content: What are the most common ways communities fail at this domain? What are the warning signs?
- Must include: 3–5 specific failure scenarios, each with 1–2 sources
- Structure: Failure mode → What went wrong → Warning signs → How to prevent/respond
- Tone: Practical, not alarmist; acknowledge that failure is normal and learnable
- Requirement: Must address at least 1 documented Zone 5 failure case

**Section 5: Scaling Pathways & Governance (1,200–1,600 words)**
- Title: `## 5. Scaling [Domain Name]: From Community to Multi-Community Networks`
- Content: How does this domain scale beyond a single community? What governance structures enable/prevent scaling?
- Must include: 2–3 scaling pathways, 1–2 network governance models (cite Ostrom/polycentric framework if applicable)
- Structure: Pathway #1 → Description → Conditions for success → Governance requirements; repeat for pathways 2–3
- Tone: Institutional + practical; connect to Phase 6 governance guidance (Domains 60, 65)

**Section 6: Conclusion & Practitioner Next Steps (600–800 words)**
- Title: `## 6. Conclusion: Moving Forward`
- Content: Summary of key insights; actionable next steps for reader
- Must include: 3–5 concrete actions a community can take NOW to strengthen this domain
- Structure: Recap main themes → 1–2 "deep work" resources (books, networks, courses) → Call to action
- Tone: Hopeful, grounded; avoid exhortation; be specific about resources

**Total body text**: 8,000–12,000 words (8 section headers + body = this range)

---

### 1.4 Citation Format: Chicago Manual of Style (Author-Date)

**In-text citations** (required for all claims, data, quotes):

```
Single author:
(Smith 2023, 45) — includes page number for direct quote or specific claim

Multiple authors (2–3):
(Smith and Jones 2023, 145)
(Smith, Jones, and Garcia 2023, 78)

Multiple authors (4+):
(Smith et al. 2023, 120)

No page number (general concept, not specific claim):
(Smith 2023) — OK for general reference, not for quotes

Multiple works by same author:
(Smith 2020, 10) and (Smith 2023, 45) — distinguish by year
```

**Bibliography format** (end of document, alphabetical):

```
Chicago Manual of Style Author-Date format:

Books:
Smith, Jane. 2023. Title of Book. Publisher Name.

Journal articles:
Smith, Jane. 2023. "Article Title." Journal Name 45, no. 3 (2023): 234–258.

Reports / white papers:
Smith, Jane. 2023. Report Title. Organization Name. 
  Accessed [date]. https://example.com/report.

Web sources:
Smith, Jane. 2023. "Web Article Title." Website Name. 
  Accessed [date]. https://example.com/article.

Government documents:
US Department of Agriculture. 2023. "Policy Title." 
  Accessed [date]. https://usda.gov/policy.
```

**Bibliography placement**: 
- After conclusion section (Section 6)
- Use `## Bibliography` as header
- All sources cited in text MUST appear in bibliography
- No sources in bibliography without in-text citations

**Minimum / Maximum source count**:
- Minimum: 15 sources (no domain accepts <15)
- Maximum: 35 sources (risk of dilution beyond this; favor depth over breadth)
- Preferred: 20–28 sources (sweet spot for authoritative but focused)

**Source quality hierarchy** (prefer in this order):
1. **Peer-reviewed academic papers** (primary source; weight highest)
2. **Books by recognized experts** (especially practitioner-accessible books)
3. **Government / institutional reports** (policy briefs, USDA Extension publications, ILO reports, etc.)
4. **Practitioner publications** (extension service publications, cooperative movement publications, documented case studies)
5. **News / journalism** (OK if from credible outlet like Reuters, NPR, not opinion blogs)
6. **Websites / blogs** (use sparingly; only if credible author + no academic source available)

**Avoid**:
- Wikipedia (reference only; cite the original source Wikipedia references)
- Opinion pieces without credible author credentials
- Social media posts (unless from official organization account)
- Out-of-date sources (prefer within 5 years unless seminal/foundational)

---

### 1.5 Length & Density Requirements

**Total word count**: 8,000–12,000 words (inclusive of all body text + headings)
- Under 8,000: Insufficient depth; trigger REVISION-NEEDED
- Over 12,000: Risk of unfocused/diluted; trigger revision request for tightening
- ±10% flexibility applies: 7,200–13,200 acceptable if peer reviewer approves

**Word count verification**:
- Author reports in YAML front matter
- Peer reviewer spot-checks (not full recount)
- Project lead final verification

**Section length guidance**:
| Section | Min | Target | Max |
|---------|-----|--------|-----|
| 1. Introduction | 600 | 700 | 800 |
| 2. Frameworks | 1200 | 1400 | 1600 |
| 3. Case Studies | 1500 | 1800 | 2000 |
| 4. Failure Modes | 1200 | 1400 | 1600 |
| 5. Scaling Pathways | 1200 | 1400 | 1600 |
| 6. Conclusion | 600 | 700 | 800 |
| **Bibliography** | (not counted) | (not counted) | (not counted) |
| **TOTAL** | **8,000** | **9,400** | **12,000** |

**Density guideline**: Average 1.5–2 paragraphs per subsection; avoid walls of text >500 words without a subheading break.

---

## Part 2: Submission Mechanics

### 2.1 Submission Checklist (Author Pre-Submission)

Before submitting to peer reviewer, author must verify:

- [ ] **File named correctly**: `Domain_[60-65]_[Last_Name]_v[#].md`
- [ ] **YAML front matter complete**: All fields filled (title, domain, author, dates, word count, source count, revision number)
- [ ] **All 6 sections present**: Sections 1–6 with correct headers and content
- [ ] **Word count accurate**: Counted and reported in YAML (use `wc -w filename.md` or word processor)
- [ ] **No embedded images/binaries**: Text only
- [ ] **Citations complete**: Every claim/quote cited; in-text citations match bibliography
- [ ] **Bibliography alphabetized**: All entries A–Z
- [ ] **No typos or obvious errors**: Proofread at least once (or use spell-checker)
- [ ] **Markdown valid**: No broken formatting; headers render correctly; links work if present
- [ ] **Zone 5 context present**: At least 1 Midwest case study (Section 3); Midwest examples in other sections
- [ ] **Practitioner voice**: Jargon defined; accessible to non-academic readers; case studies humanized
- [ ] **Peer reviewer name added**: YAML field completed (project lead assigns this)

**If ANY checkbox unchecked**: Hold submission; fix before sending to peer reviewer.

### 2.2 Submission Process (Author → Peer Reviewer)

**Submission Workflow**:

1. **Author sends email to peer reviewer + project lead**:
   ```
   Subject: Wave 2 Domain [X] — [Author Name] — 1st Draft Submission
   
   Hi [Peer Reviewer Name],
   
   Attached is my first draft for Domain [X]: [Domain Name].
   
   Summary:
   - Word count: [XXXX]
   - Source count: [XX]
   - Revision number: v1
   - Submission round: 1st Draft
   - Key themes: [Bullet 1], [Bullet 2], [Bullet 3]
   
   I'm happy to answer any questions about the draft or my approach. 
   Looking forward to your feedback.
   
   Best,
   [Author Name]
   ```

2. **Attach file**: Markdown file (FILENAME.md) as email attachment

3. **CC project lead**: Project lead logs submission in tracking spreadsheet

4. **Submission deadline**: By stated date (Wave A: July 30, Wave B: Aug 6, Wave C: Aug 13)
   - If submitted late: Subtract 1 day from peer review window (still must be completed by acceptance target date)

### 2.3 Peer Reviewer Submission

**Peer review assessment** (completed by reviewer; sent back to author + project lead):

```
Subject: Peer Review Complete — Domain [X] — [Author Name]

Hi [Author Name],

I've completed my review of your Domain [X] draft. Overall impression: [1–2 sentences summarizing quality level]

ACCEPTANCE STATUS: [DRAFT / REVISION-NEEDED / ACCEPTED / REJECTED]

DETAILED FEEDBACK:

✓ Strengths:
  1. [Specific strength with example]
  2. [Specific strength with example]
  3. [Specific strength with example]

⚠ Areas for revision:
  1. [Specific issue] → Recommendation: [Suggestion]
  2. [Specific issue] → Recommendation: [Suggestion]
  3. [Specific issue] → Recommendation: [Suggestion]

[If REVISION-NEEDED or REJECTED, add:]
REVISION PLAN:
  - Priority 1 (must fix): [Issue + fix approach]
  - Priority 2 (should fix): [Issue + fix approach]
  - Priority 3 (nice to have): [Issue + fix approach]

REVISION DEADLINE: [14 days from today, or custom date if agreed]

NEXT STEPS:
[Author name], please respond with your revision plan by [DATE + 3 days]. 
I'm available for a call if you'd like to discuss strategy.

Questions? Email me.

Best,
[Reviewer Name]
```

**Reviewer sends to**: Author + Project lead

**Timing**: Within 5–7 days of submission (Tier A) or 7–10 days (Tier B)

---

## Part 3: Revision Round Timelines

### 3.1 Revision Round 1 (First Submission → Revision Deadline)

**Timeline**:
- **Day 0**: Author submits first draft
- **Days 1–7**: Peer review (reviewer reads + composes feedback)
- **Day 7**: Feedback sent to author + project lead
- **Days 8–10**: Author reviews feedback + plans revisions
- **Days 11–24**: Author revises (14-day window)
- **Day 24**: Author resubmits revised draft

**Revision window**: 14 days (10 days after feedback + 4 days buffer)

**Author's revision options**:
- **Option A: Major revision** (Revision 1 → v2)
  - Rewrite 1–2 sections substantially
  - Add sources / deepen analysis
  - Full resubmission
  
- **Option B: Minor revision** (Revision 1 → v2-light)
  - Copyedits + small clarifications
  - 1–2 paragraphs substantially rewritten
  - Resubmit full file (reviewer reads full context again)

- **Option C: Request extension** (if needed)
  - Email project lead + reviewer by Day 13
  - Extension: +3 to +7 days, case-by-case
  - Max: One extension per revision round

**If author misses revision deadline**:
- Day 25+: Project lead calls author (same-day)
- Offer: Extend +3 days (if still making progress) OR escalate to contingency
- Document in WAVE_2_INCIDENT_LOG.md

### 3.2 Revision Round 2 (Rare; Only if Round 1 Feedback Substantial)

**Trigger**: Reviewer assesses v2 as "still needs revision" (occurs ~20% of the time)

**Timeline**:
- **Day 0**: Author resubmits v2 (revised draft)
- **Days 1–5**: Peer review of v2
- **Day 5**: Feedback sent (lighter feedback than Round 1; focus on remaining issues)
- **Days 6–13**: Author revises again (8-day window, shorter than Round 1)
- **Day 13**: Author resubmits v3

**Acceptance after Round 2**: 
- If feedback minor, v3 typically accepted without third review
- If feedback still substantial, escalate: Author + reviewer + project lead call to negotiate scope reduction or co-author support

### 3.3 Acceptance Target Dates (by Domain Wave)

| Wave | Domains | 1st Submit | 1st Review Window | Round 1 Revision | Acceptance Target | Buffer |
|------|---------|-----------|-------------------|-----------------|------------------|--------|
| A | 63, 65 | July 30 | Aug 1–8 | Aug 9–23 | Aug 24 | 3 days |
| B | 60, 64 | Aug 6 | Aug 8–15 | Aug 16–30 | Aug 31 | 3 days |
| C | 61, 62 | Aug 13 | Aug 15–22 | Aug 23–Sept 6 | Sept 7 | 8 days |

**Final acceptance deadline**: Sept 15, 2026 (no documents accepted after this date; any outstanding = contingency triggered)

---

## Part 4: Quality Acceptance Criteria

### 4.1 Twelve-Point Acceptance Checklist

**All 12 elements must pass for "ACCEPTED" status. 0–11 elements passing = REVISION-NEEDED or REJECTED.**

**CONTENT & SCOPE** (Elements 1–5):

☐ **1. All 5 core sections complete**
   - Check: Sections 1–6 present with substantive content (not placeholders)
   - Pass criterion: Each section ≥ 60% of target word count
   - Failure: Missing section, or section <400 words total

☐ **2. Word count within range**
   - Check: 8,000–12,000 words (±10% = 7,200–13,200 acceptable)
   - Pass: Between these bounds
   - Failure: <7,000 or >13,500 words

☐ **3. Zone 5 applicability evident**
   - Check: Document explicitly addresses Wisconsin/Minnesota/Iowa/Illinois/Missouri context
   - Pass: ≥1 case study from Zone 5; ≥3 other Midwest examples/references
   - Failure: Generic guidance with no geographic specificity; zero Midwest examples

☐ **4. Practitioner voice consistent**
   - Check: Accessible to non-academic readers; jargon defined; concrete examples throughout
   - Pass: No sections read as purely academic; case studies are narrative not abstract; tone conversational
   - Failure: Academic tone dominant; heavy jargon unexplained; no human stories/examples

☐ **5. Failure modes section substantive**
   - Check: Section 4 identifies 3+ concrete failure scenarios with sources
   - Pass: Each failure mode has 1–2 sources; warning signs specified; prevention strategies offered
   - Failure: <2 failure scenarios; no sources cited; vague/general language

---

**CITATIONS & RESEARCH** (Elements 6–8):

☐ **6. Sufficient sources**
   - Check: 15–35 sources total (prefer 20–28)
   - Pass: Within this range; quality distribution (see source hierarchy in Section 1.4)
   - Failure: <15 sources or >40 sources; most sources are low-quality (blogs, social media, no academic)

☐ **7. All in-text citations match bibliography**
   - Check: Every cite in text appears in bibliography; every bibliography entry cited in text
   - Pass: 100% match (spot-check 5 citations; all correct)
   - Failure: >2 orphaned bibliography entries; >2 uncited claims in text

☐ **8. Chicago author-date format correct**
   - Check: In-text format (Author Year, page) and bibliography format (alphabetical, full citations)
   - Pass: All citations follow Chicago format; bibliography alphabetical; no format errors
   - Failure: Mixed citation styles; bibliography not alphabetized; format errors in >5 entries

---

**STRUCTURE & FORMATTING** (Elements 9–10):

☐ **9. Markdown structure valid**
   - Check: File is valid Markdown; YAML front matter complete; section headers consistent
   - Pass: File renders without errors; YAML all fields filled; headers are `##` (H2) and `###` (H3)
   - Failure: Markdown errors; YAML fields missing; inconsistent header levels

☐ **10. Writing quality (no critical errors)**
   - Check: Proofread for typos, grammar, clarity
   - Pass: ≤5 typos or minor grammatical issues (acceptable level for working draft)
   - Failure: >10 typos; grammatical errors affecting comprehension; unclear sentences

---

**DOMAIN-SPECIFIC REQUIREMENTS** (Elements 11–12):

☐ **11. Governance/scaling dimension clear (if Domains 60, 61, 64, 65)**
   - Check: For Domains 60, 61, 64, 65: Section 5 explicitly addresses governance scaling or network coordination
   - Pass: Governance model(s) identified; multi-community scaling pathway described; Ostrom framework referenced if applicable
   - Failure: Scaling section is vague; governance not addressed; single-community focus only

   *(For Domain 62 & 63: This element is "not applicable but not required"; pass if infrastructure interdependency chain OR ecosystem cascade is addressed)*

☐ **12. Policy/practitioner implications clear**
   - Check: Document offers 3+ concrete, actionable next steps for communities (Section 6)
   - Pass: Conclusion includes specific actions, resources, or networks communities can engage with
   - Failure: Conclusion is abstract/theoretical with no concrete next steps; vague recommendations

---

### 4.2 Acceptance Decisions & Status Labels

**ACCEPTED**:
- 12/12 elements pass (or 11/12 with waiver approved by project lead + reviewer)
- Status label: `acceptance_status: "ACCEPTED"` in YAML
- Document moves to publication queue
- Payment milestone 2 (50% completion bonus) triggered
- Author notified same day

**REVISION-NEEDED** (author must revise):
- 8–11 of 12 elements pass
- Reviewer provides specific feedback for each failing element
- Author gets 14-day revision window
- Resubmitted as `v2.md` file
- Typically only 1 revision round needed

**REJECTED** (document does not qualify; author does not proceed):
- ≤7 of 12 elements pass, OR
- Critical scope misalignment (>2 required sections missing/wrong), OR
- Fundamental quality concerns (plagiarism, factual errors, incoherent writing)
- Author notified with specific reasons + offer of contingency role (see WAVE_2_CONTINGENCY_AUTHOR_SUBSTITUTION.md)
- Contingency plan activated

**DEFERRED** (rare; document acceptable but needs minor edits before final publication):
- 11–12 elements pass but ≥2 copyedit-level issues
- Author gets 3-day window to fix before final acceptance
- Not counted as full revision round; same payment tier applies

---

## Part 5: Communication Templates

### 5.1 Acceptance Notification Email (Accepted)

```
Subject: Document ACCEPTED — Domain [X] — [Author Name]

Hi [Author Name],

Great news: Your Domain [X] draft has been reviewed and ACCEPTED.

[Reviewer Name] provided the following assessment:

"[1–2 sentences from reviewer on overall quality]"

Strengths highlighted:
- [Specific strength 1]
- [Specific strength 2]

Small notes from reviewer (no revision needed):
- [Minor note, if any]

NEXT STEPS:

1. Your 50% completion payment ($[AMOUNT]) will be processed within 5 business days
2. Document will be compiled into Phase 6 Wave 2 corpus and formatted for publication
3. You'll receive a copy of the final published version by [DATE]
4. The published document will include your byline, bio, and link to your work

Thank you for the excellent work on Domain [X]. The document is exactly what we needed, 
and your practitioner voice + research rigor set the standard for Phase 6.

Very much looking forward to Wave 3.

Best,
[Project Lead Name]
```

### 5.2 Revision-Needed Notification Email

```
Subject: Peer Review Complete — Domain [X] — Revision Needed

Hi [Author Name],

[Reviewer Name] has completed the peer review of your Domain [X] draft. 

ACCEPTANCE STATUS: REVISION-NEEDED

Overall impression from [Reviewer Name]:
"[1–2 sentences]"

The document has strong bones and addresses the domain well. A few sections need 
tightening/expansion to meet our publication standard.

REVISION PRIORITIES:

✓ MUST FIX (high priority):
  1. [Issue] — Recommendation: [Specific action]
  2. [Issue] — Recommendation: [Specific action]

⚠ SHOULD FIX (medium priority):
  1. [Issue] — Recommendation: [Specific action]

✓ NICE TO HAVE (low priority):
  1. [Issue] — This is optional

REVISION TIMELINE:

Deadline: [DATE + 14 days]
(If you need an extension, let me know by [DATE + 3 days])

NEXT STEPS:

1. Review [Reviewer Name]'s detailed feedback (attached)
2. Create an outline of your revisions (1 paragraph; email to me by [DATE + 3 days])
3. Revise document and resubmit by [DATE + 14 days] as Domain_[X]_[Last_Name]_v2.md
4. I'll confirm receipt and pass to [Reviewer Name] for final review

QUESTIONS?

Feel free to call me or [Reviewer Name] if you want to discuss the revision strategy. 
We're here to help make this work.

You've got this. The revision is straightforward, and we're confident in the final product.

Best,
[Project Lead Name]
```

### 5.3 Rejection Notification Email (Rare)

```
Subject: About Your Domain [X] Submission — Alternative Opportunity

Hi [Author Name],

Thank you for submitting your Domain [X] draft. I've reviewed it with [Reviewer Name], 
and we want to be transparent about where things stand.

THE SITUATION:

The draft does not meet our Phase 6 publication standard at this time. 
Specifically: [2–3 most critical issues].

This is not a reflection on your expertise or effort. Rather, Wave 2's scope and timeline 
are quite demanding, and this particular assignment may not have been the ideal fit.

OUR RECOMMENDATION:

Rather than pursue a lengthy revision cycle, we'd like to offer two alternatives:

**Option A: Community Editor Role**
Instead of authorship, we'd invite you to serve as a community reviewer for Domain [X]. 
You'd review the document (once assigned to a different author) and provide feedback on 
[specific aspect]. 2–3 hours/week, $40/hour, great experience for future authorship.

**Option B: Wave 3 Candidate**
Phase 6 Wave 3 (Fall 2026 – Winter 2027) will have lower intensity and more flexible 
scope. Would you be interested in a different domain assignment in Wave 3?

**Option C: No Further Involvement**
Completely understandable. We'll add you to our network for future collaboration.

WHICH APPEALS TO YOU?

Please let me know by [DATE + 2 days], and I'll follow up with details.

Your expertise is valuable, and we hope to find a way to work together that's 
mutually beneficial.

Best,
[Project Lead Name]
```

---

## Part 6: Quality Assurance Procedures

### 6.1 Peer Review Pairing & Conflict-of-Interest Rules

**Peer reviewer assignment principles**:

1. **No institutional conflicts**: Reviewer has no competing/institutional relationship with author
   - Example conflict: Both from same organization competing for same funding
   - Example OK: Different organizations; mutual professional respect

2. **Domain adjacency preferred**: Reviewer has expertise in same or adjacent domain
   - Example: Domain 63 (Ecosystem) author reviewed by Wave 1 Domain 62 (Infrastructure) author
   - Example: Domain 60 (International) author reviewed by Domain 65 (Governance) author (both system-level)

3. **Tier A author reviews Tier B drafts** (when possible)
   - High-quality feedback from experienced authors
   - Mentoring value for Tier B authors

4. **Wave 1 authors preferred** (if available and conflict-free)
   - Already familiar with project standards
   - Have published document from Phase 5 as quality reference

**Reviewer communication** (before assignment):

```
Subject: Peer Reviewer Invitation — Domain [X] — Wave 2

Hi [Peer Reviewer Name],

We'd like to invite you to serve as the peer reviewer for Domain [X]: [Domain Name] 
in Wave 2 of Systems Resilience Phase 6.

SCOPE:

Domain author: [Name] | Tier: [A/B]
Domain: [X] | [Description]
Estimated submission: [Date]
Review deadline: [Date + 7 days]

YOUR ROLE:

- Read the draft (8,000–12,000 words)
- Assess against the attached 12-point acceptance checklist (WAVE_2_QUALITY_GATES.md)
- Provide detailed feedback using the feedback template
- Recommend: ACCEPTED / REVISION-NEEDED / REJECTED

COMPENSATION:

$50 flat fee for peer review (1–2 hours work)
Payment: Upon completion of review + feedback

TIMELINE:

June 16: Confirm availability
August: Receive draft; complete review within 7 days

ARE YOU INTERESTED?

Please reply by [DATE] to confirm. Happy to discuss any questions.

Thanks for serving the project.

Best,
[Project Lead Name]
```

### 6.2 Spot-Check Verification Protocol

**Project lead verification** (5% of submissions; random selection):

For each Wave (A, B, C), randomly spot-check 1 document:

1. **Re-count word count** using `wc -w filename.md`
2. **Verify 5 random citations**:
   - Pick 5 in-text citations at random (e.g., citations #3, #7, #11, #19, #25)
   - Confirm each citation exists in bibliography
   - Spot-check one full bibliography entry (confirm author/title/year/URL)
3. **Skim Section 4 (Failure Modes)**: Confirm ≥3 scenarios, each with ≥1 source
4. **Check for Zone 5 examples**: Count Midwest examples; should be ≥4 total (across all sections)

**If spot-check finds errors**:
- <2 minor errors (typo, formatting): Document still accepted; note for final editing
- 2–5 errors (missing citation, wrong date, source not found): Escalate to author + reviewer; ask for 3-day fix
- >5 errors: Escalate to REVISION-NEEDED

---

## Part 7: Submission Channel & File Transfer

### 7.1 File Submission Method

**Preferred method: Email with attachment**

```
TO: [Peer Reviewer Email]; CC: [Project Lead Email]
SUBJECT: Wave 2 Domain [X] — [Author Name] — [Submission Round]
ATTACHMENT: Domain_[60-65]_[Last_Name]_v[#].md

Body: (See Section 2.2 above)
```

**Alternative method: Shared drive (Google Drive / Box / GitHub)**

If file >5MB (unlikely for Markdown) or author preference:
- Create shared folder: `/Systems_Resilience_Wave2/Domain_[X]/`
- Author uploads file to folder
- Email notification sent to reviewer + project lead with link
- Reviewer downloads, reviews locally, uploads feedback as separate document

**File backup**:
- Project lead maintains backup copy of all submissions
- Archive location: `/projects/systems-resilience/Wave_2_Submissions/`
- Naming: Same as original (Domain_[60-65]_[Last_Name]_v[#].md)

### 7.2 Tracking & Documentation

**Project lead maintains spreadsheet**: WAVE_2_SUBMISSION_TRACKING.xlsx

| Domain | Author | Tier | Submission Date | 1st Submit v# | Reviewer | Review Received | Acceptance Status | Payment M1 | Payment M2 | Notes |
|--------|--------|------|-----------------|---------------|----------|-----------------|------------------|-----------|-----------|-------|
| 63 | Kloppenburg | A | 7/30 | v1 | [Reviewer] | 8/7 | REVISION-NEEDED | ✓ 7/16 | ⏳ 8/24 | Minor copy edits |
| [Etc] | — | — | — | — | — | — | — | — | — | — |

**Updates weekly**: Every Friday, project lead updates tracking with latest status.

---

## Part 8: Final Publication Preparation

### 8.1 Post-Acceptance Edits (Minor)

Once document is ACCEPTED, project lead may request:

- **Copyediting**: Max 3 hours; author reviews + approves edits
- **Formatting normalization**: Headers, citation style consistency (automated)
- **Metadata final review**: Verify YAML fields match final document

**Turnaround**: 5 business days max (author does not have to revise; project lead handles edits)

### 8.2 Author Bio & Attribution

Each accepted document includes a footer with:

```
---
## Author

**[Author Full Name]** is a [1-sentence bio]. 
With [X] years of experience in [domain], [he/she/they] has [relevant accomplishment].
You can find [his/her/their] work at [website/blog/organization].

[Optional: Social media link]
```

**Author provides bio** in assignment confirmation email (Section 3.1 of WAVE_2_CONTENT_ASSIGNMENT_PROTOCOL.md).

---

## Part 9: Summary Table

| Stage | Deliverable | Format | Due Date | Acceptance Criteria |
|-------|-------------|--------|----------|-------------------|
| Submission | Draft document | Markdown, YAML header, 6 sections | Per wave (7/30, 8/6, 8/13) | 12/12 elements; submit checklist verified |
| Review | Peer review feedback | Email + template | +7 days | Detailed, constructive, actionable |
| Revision | v2 document (if needed) | Same as above; increment version | +14 days | Same 12/12 criteria |
| Final | v-FINAL document | Same; updated YAML | Sept 15 | Quality gates passed; ready for publication |

---

## Document Status

This specification is **PRODUCTION-READY** for June 14 author assignment + July 16 writing start.

For questions about format or submission before July 16, contact [Project Lead] by June 30.

---

## Related Documents

- `WAVE_2_CONTENT_ASSIGNMENT_PROTOCOL.md` — Assignment process (use to understand scope briefs)
- `WAVE_2_AUTHOR_MATCHING_ALGORITHM.md` — Scoring methodology (reference for quality expectations)
- `WAVE_2_QUALITY_GATES.md` — Detailed 12-point acceptance checklist
- `WAVE_2_CONTINGENCY_AUTHOR_SUBSTITUTION.md` — Fallback if document rejected
