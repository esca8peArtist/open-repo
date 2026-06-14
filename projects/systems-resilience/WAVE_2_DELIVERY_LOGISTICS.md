# Wave 2 Delivery Logistics Framework
## Systems-Resilience Project | Domains 60–65

**Document Version**: 1.0  
**Effective Date**: June 2026  
**Status**: Production-Ready  
**Last Updated**: 2026-06-14

---

## 1. Submission Timeline & Milestones

| Milestone | Date Offset | Activity | Owner | Acceptance Gate |
|-----------|------------|----------|-------|-----------------|
| **T+0** | Day 1 | Author submission window opens; initial delivery due | Author | File format validation |
| **T+7** | Day 8 | Peer review round 1 closes; feedback compiled | Peer reviewers | Rubric completion |
| **T+14** | Day 15 | Orchestrator editorial feedback delivered | Orchestrator | Review sign-off |
| **T+21** | Day 22 | Final author revisions complete; publication ready | Author | Full acceptance checklist |
| **T+28** | Day 29 | Wave 2 publication (all domains 60–65 live) | Project lead | Deployment confirmation |

---

## 2. File Format & Delivery Specification

### 2.1 Primary Format: Markdown (.md)

All submissions must use **GitHub Flavored Markdown** (GFM) with the following structure:

```markdown
---
title: "[Domain ##] [Document Title]"
domain: 60
author: "[Author Full Name]"
author_affiliation: "[Organization/Institution]"
author_credentials: "[Relevant qualifications, degree, publications]"
submission_date: "YYYY-MM-DD"
revision_round: 0
word_count_target: [800–1500]
status: "submitted"
---

# [Document Title]

## 1. Introduction
...

## 2. [Section Title]
...

## References

[Chicago author-date citations as per Section 6]
```

### 2.2 YAML Front Matter Template

```yaml
---
title: "Domain 60: International Coordination in Crisis Response"
domain: 60
tier: "A"
author: "[Submitting Author Name]"
author_affiliation: "[Organization]"
author_credentials: "[Ph.D. in ..., published in X, Y, Z]"
submission_date: "2026-06-YY"
revision_round: 0
word_count_target: 1200
word_count_actual: 0
status: "submitted"
peer_review_status: "pending"
orchestrator_feedback: "pending"
publication_status: "unpublished"
keywords:
  - coordination
  - crisis response
  - international systems
---
```

### 2.3 File Naming Convention

```
Domain_##_[Author_Last_Name]_Wave2_R[revision_number].md

Examples:
Domain_60_Santos_Wave2_R0.md          (initial submission)
Domain_60_Santos_Wave2_R1.md          (round 1 revisions)
Domain_62_Greenberg_Wave2_R2.md       (round 2 revisions)
```

---

## 3. Submission Mechanics

### 3.1 Submission Channel Priority

1. **Primary**: GitHub pull request to `/projects/systems-resilience/wave-2-submissions/[domain##]/`
   - Branch naming: `wave2-domain-##-[author-last-name]`
   - Include checklist in PR description
   - Tag: `@orchestrator-review`, `wave2-submission`

2. **Secondary**: Email to orchestrator inbox (wanka95@gmail.com)
   - Subject: `[Wave 2] Domain ## Submission – [Author Name]`
   - Attach: markdown file + supporting materials
   - Include: YAML front matter excerpt in email body for quick validation

3. **Tertiary**: Shared Google Drive folder
   - Backup only if GitHub/email unavailable
   - Path: `/systems-resilience/Wave2_Submissions/Domain_##/`
   - File must be exported to .md immediately after upload

### 3.2 Submission Checklist

Authors must include this checklist in PR description or email:

```markdown
- [ ] YAML front matter complete (all required fields)
- [ ] Word count: 800–1500 words (actual count in front matter)
- [ ] No more than 3 major sections + conclusion
- [ ] Minimum 5 citations in Chicago author-date format
- [ ] Author credentials verified in front matter
- [ ] No proprietary or confidential content
- [ ] Images/PDFs bundled (see Section 3.3)
- [ ] Markdown passes linter (no syntax errors)
- [ ] Self-review: addresses domain prompt completely
- [ ] No material changes to submission filename
```

---

## 4. Asset Bundling & Supporting Materials

### 4.1 PDF & Citation Management

- **Citation PDFs**: One ZIP archive per submission containing up to 3 key-source PDFs
  - Naming: `Domain_##_Santos_Wave2_References.zip`
  - Include: open-source or author-shared PDFs only
  - Limit: 15 MB total per submission

- **Source URLs**: All citations must include stable DOI or archived URL
  - Use Wayback Machine links for web sources (e.g., `https://web.archive.org/web/20250601000000*/example.com`)
  - Never reference paywalled sources without note `[author-provided excerpt]`

### 4.2 Supporting Data & Visualizations

If domain submission includes data or charts:
- Preferred format: SVG (scalable, version-controllable)
- Acceptable: PNG (300+ dpi for print quality)
- Store in: `/projects/systems-resilience/wave-2-submissions/[domain##]/assets/`
- Reference in markdown: `![Figure 1: [Caption]](./assets/figure1.svg)`

### 4.3 Author-Provided Resources

Authors may include supplementary materials (not counted in word limit):
- Reading lists (annotated, 1–2 pages max)
- Methodology appendices (if domain warrants)
- Case study summaries (1 page max)
- Store in: `Domain_##_Santos_Wave2_Supplementary.md`

---

## 5. Acceptance Criteria by Domain

### 5.1 General Rubric (All Domains)

| Criterion | Exemplary | Proficient | Acceptable | Unacceptable |
|-----------|-----------|-----------|-----------|------------|
| **Completeness** | Addresses all domain prompts; no gaps | Addresses 90%+ of prompts | Addresses 75%+ of prompts | <75% coverage |
| **Clarity** | Argument is compelling and accessible | Clear argumentation; minor jargon | Understandable with re-reading | Unclear or contradictory |
| **Citations** | 7+ strong sources; proper format | 5–6 authoritative sources; proper format | Minimum 5 citations; mostly correct format | <5 citations OR improper format |
| **Author Credentials** | Directly relevant expertise; publications verified | Relevant background; credentials evident | Credible background in related field | Unverified or tangential credentials |
| **Word Count** | 1200–1500 words (tight, well-edited) | 900–1500 words (target met) | 800–900 words (minimal but acceptable) | <800 or >1500 words |
| **Originality** | Unique perspective; minimal overlap with corpus | Original synthesis; some standard elements | Competent coverage; expected framing | Largely derivative or unsourced |

### 5.2 Domain-Specific Acceptance Gates

#### **Domain 60: International Coordination in Crisis Response**
- **Key criteria**: Real-world case studies (minimum 2); cross-border coordination mechanisms identified
- **Word count**: 1000–1500
- **Citation floor**: 6 (international governance bodies, crisis documentation)
- **Author credential requirement**: Government affairs, humanitarian response, or international relations background
- **Contingency reviewer**: Martha Santos (ALT); if unavailable, David Greenberg (EXT-02)

#### **Domain 61: Intergenerational Knowledge Transfer**
- **Key criteria**: Framework for multigenerational learning; concrete pedagogical examples
- **Word count**: 900–1300
- **Citation floor**: 5 (education research, intergenerational studies, case examples)
- **Author credential requirement**: Education, community development, or anthropology background
- **Contingency reviewer**: David Greenberg (ALT); if unavailable, James Akomea (EXT-09)

#### **Domain 62: Infrastructure Resilience & Adaptation**
- **Key criteria**: Infrastructure systems analysis; climate/disruption adaptation pathway
- **Word count**: 1100–1500
- **Citation floor**: 7 (engineering, climate science, infrastructure policy)
- **Author credential requirement**: Infrastructure engineering, urban planning, or environmental systems background
- **Contingency reviewer**: [Primary domain-specific ALT to be assigned]; if unavailable, Patrick Carolan (EXT-08)

#### **Domain 63: Ecosystem Restoration & Biodiversity**
- **Key criteria**: Restoration science grounded in ecology; biodiversity metrics; site-specific examples
- **Word count**: 1000–1400
- **Citation floor**: 6 (ecological research, restoration case studies)
- **Author credential requirement**: Biology, ecology, conservation science, or land management background
- **Contingency reviewer**: [Primary domain-specific ALT to be assigned]; if unavailable, iFixit (EXT-05, for community repair/restoration focus)

#### **Domain 64: Economic Resilience & Local Systems**
- **Key criteria**: Economic model or framework; household/community-level analysis; alternatives identified
- **Word count**: 950–1500
- **Citation floor**: 6 (economics research, local economy case studies, alternative systems)
- **Author credential requirement**: Economics, development studies, or community development background
- **Contingency reviewer**: Michael Linton (ALT); if unavailable, La Via Campesina (EXT-03)

#### **Domain 65: Institutional Learning & Adaptive Governance**
- **Key criteria**: Organizational learning mechanism; feedback loop definition; governance structure analysis
- **Word count**: 1000–1400
- **Citation floor**: 6 (organizational studies, governance, systems thinking)
- **Author credential requirement**: Organizational development, public administration, or systems analysis background
- **Contingency reviewer**: [Primary domain-specific ALT to be assigned]; if unavailable, Post Carbon Institute (EXT-07)

---

## 6. Citation Format: Chicago Author-Date Style

### 6.1 In-Text Citations

```markdown
(Smith 2024, 145)
(World Bank 2023)
(Multiple authors: Johnson, Lee, and Park 2022, 78–82)
```

### 6.2 Reference List Format

#### Book
```
Smith, Jane E. 2024. Title of Book in Sentence Case. Publisher Name.
```

#### Journal Article
```
Johnson, Michael, Sarah Lee, and Park Jin-soo. 2022. "Article Title in Sentence Case." 
Journal Title 45, no. 3 (2022): 123–145.
```

#### Website/Report
```
World Bank. 2023. "Report Title in Sentence Case." Accessed June 14, 2026. 
https://example.org/report-title. [or archived: https://web.archive.org/web/20230601000000*/example.org]
```

#### Government/Institutional Document
```
United Nations Environment Programme. 2023. Annual Report: Climate Action Framework. 
UNEP Publishing, 2023.
```

### 6.3 Citation Validation Checklist

- [ ] All in-text citations (parenthetical) have corresponding reference list entries
- [ ] Author names spelled consistently across citations
- [ ] Publication dates are accurate and current (no future dates)
- [ ] URLs are stable (DOI preferred; Wayback Machine acceptable for web sources)
- [ ] Journal/publisher names match official records
- [ ] Page numbers included for direct quotes

---

## 7. Orchestrator Review Hours & Domain Breakdown

### 7.1 Estimated Hours per Domain

Orchestrator review includes: initial format validation, content quality assessment, peer review coordination, editorial feedback compilation, and revision round sign-off.

| Domain | Reviewer Role | Hours (Initial) | Hours (R1 Feedback) | Hours (Final Sign-Off) | **Total** |
|--------|--------------|-----------------|-------------------|----------------------|----------|
| **60** | Lead | 3.0 | 2.0 | 1.5 | **6.5** |
| **61** | Co-lead | 2.5 | 1.5 | 1.0 | **5.0** |
| **62** | Lead | 3.5 | 2.5 | 1.5 | **7.5** |
| **63** | Co-lead | 3.0 | 2.0 | 1.5 | **6.5** |
| **64** | Lead | 2.5 | 2.0 | 1.0 | **5.5** |
| **65** | Co-lead | 3.0 | 2.0 | 1.5 | **6.5** |
| **TOTAL ORCHESTRATOR HOURS** | | | | | **37.5** |

### 7.2 Peer Review Load Distribution

Each domain includes:
- **Primary peer reviewer**: Domain expert (1.5 hours per round)
- **Secondary peer reviewer**: Cross-domain specialist (1.0 hours per round)
- **Contingency peer**: Available for author no-show or escalation (0.5 hours standby per domain)

**Total peer review hours across Wave 2 (all 6 domains, 1 round)**: ~18 hours

### 7.3 Review Workflow Timeline

```
T+0 (Day 1):     Submission received → Format validation (0.5 hrs/domain)
T+1 to T+6:      Peer review round 1 (1.5 hrs primary, 1.0 hrs secondary)
T+7 (Day 8):     Feedback compilation + editorial notes (1.0 hrs/domain)
T+8 to T+13:     Author revisions (no orchestrator input)
T+14 (Day 15):   Orchestrator final review + feedback letter (2.0 hrs/domain)
T+15 to T+20:    Author final revisions
T+21 (Day 22):   Sign-off + publication readiness (1.5 hrs/domain)
T+22 to T+28:    Final copyedit and deployment
T+28 (Day 29):   Wave 2 live on platform
```

---

## 8. Revision Round Schedule & Expectations

### 8.1 Round 1: Peer Review (T+7)

**Input**: Initial author submission  
**Process**: 2 independent peer reviewers + editorial synthesis  
**Output**: Consolidated feedback memo (not line-edits; thematic guidance)

**Feedback dimensions**:
1. Completeness vs. domain prompt (coverage analysis)
2. Argument clarity & logic flow
3. Citation adequacy & quality
4. Author credential alignment with topic

**Author expectation**: 2–3 substantive revisions, minor polishing  
**Revision time**: 3–5 business days

### 8.2 Round 2: Orchestrator Feedback (T+14)

**Input**: Author revisions + original peer feedback  
**Process**: Orchestrator editorial review  
**Output**: Structured feedback letter + accept/minor-fix/major-revise decision

**Decision gates**:
- **Accept**: No further changes required
- **Minor Fixes** (< 3 issues): Typos, 1–2 citation additions, small clarifications
- **Major Revise** (≥3 issues): Structural changes, significant content gaps, re-write sections

**Author expectation**: 1–2 hours of final refinement  
**Revision time**: 2–3 business days

### 8.3 Round 3: Final Sign-Off (T+21)

**Input**: Author final revisions  
**Process**: Orchestrator spot-check + copyedit pass  
**Output**: Publication-ready document + deployment approval

**Gates for publication**:
- [ ] All major feedback addressed
- [ ] Word count compliant (800–1500)
- [ ] Citations complete and properly formatted
- [ ] YAML front matter updated
- [ ] Author credentials verified
- [ ] No new content errors introduced

---

## 9. Contingency & Escalation

### 9.1 Author No-Show Protocol

**Trigger**: No response from author by T+3 (72 hours from submission window close)

**Action steps** (see WAVE_2_CONTINGENCY_AUTHOR_SUBSTITUTION.md for detailed decision tree):
1. **T+3**: Automated reminder to author (email + Slack)
2. **T+5**: Activate ALT author (secondary Tier B candidate for domain)
3. **T+7**: If ALT declines, activate EXT pool author
4. **T+14**: If both ALT and EXT unavailable, escalate domain to Phase 3 (deferred publication)

### 9.2 Partial Submission Handling

If author delivers draft but misses T+7 deadline:
- **T+8 to T+10**: Orchestrator may approve "extended review" (adds 3–5 business days)
- **Condition**: Draft must be ≥75% complete and address ≥80% of domain prompts
- **Cost**: Domain publication shifts to T+35 (1 week delay), no other impact

---

## 10. Google Docs Collaboration (Optional)

If cloud collaboration is needed for co-authored or mentored submissions:

### 10.1 Folder Structure

```
/systems-resilience/Wave2_GoogleDocs/
├── Domain_60_International_Coordination/
│   ├── [Draft] Domain 60 – Santos & Greenberg (Shared)
│   ├── [Review] Domain 60 Feedback (Comments Only)
│   └── [Final] Domain_60_Santos_Wave2_R1.md (Archive)
├── Domain_61_Intergenerational_Knowledge/
│   └── [Similar structure]
└── [Continue for all 6 domains]
```

### 10.2 Export Protocol

All Google Docs must be **exported to markdown** before T+0 submission deadline:
1. File → Download → Download as Markdown (.zip)
2. Extract .md file
3. Add YAML front matter
4. Verify formatting in GFM linter
5. Submit via GitHub PR or email (see Section 3.1)

### 10.3 Collaboration Permissions

- **Author**: Full edit access (can comment and edit)
- **Domain peer reviewer**: Commenter-only access during T+1 to T+6
- **Orchestrator**: Viewer access to all active drafts
- **Archival**: Copy final .md to `/wave-2-submissions/[domain##]/` after publication

---

## 11. Quality Assurance Checklist

### Pre-Submission (Author)

- [ ] Domain prompt fully addressed
- [ ] Word count in target range (800–1500)
- [ ] Minimum 5 citations in Chicago format
- [ ] YAML front matter complete
- [ ] No proprietary or confidential content
- [ ] Markdown syntax valid (tested in local editor)
- [ ] Author credentials verified and listed
- [ ] Supporting files bundled (if applicable)

### Post-Submission (Orchestrator)

- [ ] File format correct (.md, proper naming)
- [ ] YAML front matter valid (all required fields)
- [ ] Submission window compliance (T+0 deadline met)
- [ ] Word count within spec (auto-check against front matter)
- [ ] Citation count minimum met (auto-check)
- [ ] Author credentials present and credible
- [ ] No obvious syntax errors or formatting issues
- [ ] Peer reviewers assigned and notified
- [ ] Timeline locked in project calendar

### Peer Review (Reviewers)

- [ ] Rubric completed (all dimensions rated)
- [ ] Feedback specific and actionable (no vague comments)
- [ ] Feedback delivered on time (by T+6)
- [ ] Tone constructive and professional
- [ ] Major gaps or errors escalated to orchestrator

### Pre-Publication (Orchestrator)

- [ ] All feedback addressed (author provided evidence)
- [ ] Word count remains compliant
- [ ] Citation format consistent
- [ ] No new errors introduced in revisions
- [ ] Publication status field updated to "ready"
- [ ] Final YAML metadata accurate
- [ ] Document staged for deployment

---

## 12. Contact & Escalation Matrix

| Issue | Primary Contact | Secondary | Tertiary |
|-------|-----------------|-----------|----------|
| **Submission questions** | Project orchestrator (wanka95@gmail.com) | Domain co-lead | Domain expert peer |
| **Deadline extension** | Orchestrator + project lead | ALT author slot manager | Phase 3 deferrals |
| **Citation/format help** | Orchestrator editorial | Reference librarian (if available) | Chicago Manual style guide |
| **Author no-show** | Orchestrator → ALT activation | EXT pool coordinator | Phase 3 escalation |
| **Technical (GitHub/upload)** | IT support | Orchestrator backup | Secondary submission channel |
| **Peer review conflict** | Orchestrator | Contingency peer | External domain expert |

---

## Appendix A: YAML Front Matter Validation Rules

```yaml
# Required fields (submission invalid without)
title: string (50–150 characters)
domain: integer (60–65)
author: string (full name)
author_affiliation: string (organization/institution)
author_credentials: string (degree + relevant experience, 50+ characters)
submission_date: string (YYYY-MM-DD, must be ≤ T+0)
revision_round: integer (0 for initial submission, auto-increment)
word_count_target: integer (800–1500)

# Auto-populated fields (author should set to "submitted" / "pending" / "0")
word_count_actual: integer (auto-filled during review)
status: enum ["submitted", "peer_review", "revision_round_1", "revision_round_2", 
             "ready_to_publish", "published", "deferred"]
peer_review_status: enum ["pending", "in_progress", "complete", "escalated"]
orchestrator_feedback: enum ["pending", "issued", "acknowledged"]
publication_status: enum ["unpublished", "ready", "published", "archived"]

# Optional fields
keywords: array of strings (3–5 domain-relevant terms)
notable_sections: array (list sub-sections if >4 major sections)
supplementary_files: array (filenames of .zip, .pdf, or companion .md)
```

---

## Appendix B: Markdown Linter Configuration

Use the following tool to validate markdown syntax before submission:

```bash
# Install: npm install -g markdownlint-cli
markdownlint Domain_60_Santos_Wave2_R0.md

# Common fixes
# 1. No more than 1 space after markdown list markers: "- item", not "-  item"
# 2. Code fences must use triple backticks: ```markdown, not ```md
# 3. Heading hierarchy: no gaps (#, ##, ### OK; # then ### is error)
# 4. No more than 1 blank line between paragraphs
# 5. Links must have title text: [Title](url), not [](url)
```

---

**Document Status**: Ready for deployment  
**Version Control**: Tracked in `/projects/systems-resilience/WAVE_2_DELIVERY_LOGISTICS.md`  
**Last Review**: 2026-06-14  
**Next Review Date**: 2026-07-21 (post-Wave 2 publication)
