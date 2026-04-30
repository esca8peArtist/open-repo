---
title: "Tier 2 Success Metrics — Per-Sector Targets, Tracking Structure, and Iteration Framework"
project: cybersecurity-hardening
created: 2026-04-30
status: ready-for-use
item: 31 — Tier 2 Distribution Execution
depends-on: tier-2-distribution-calendar.md, tier-2-sector-contact-lists.md
---

# Tier 2 Success Metrics

**Purpose**: Define what success looks like for each sector, establish realistic targets, and provide the tracking structure needed to iterate on the outreach. Metrics without a tracking system are decorative. The spreadsheet structure at the end of this document is the operational core.

**Lead finding**: The targets below are calibrated to the corpus's specific situation — a well-sourced, unaffiliated researcher sharing primary-source security documentation with professional organizations. They are not generic email marketing benchmarks. Digital rights organizations and journalists should produce the highest open and reply rates because the corpus directly extends their active work. Academic programs will convert more slowly. Researcher communities are tracked differently because the primary channel is community posting, not individual email.

---

## Sector A: Digital Rights Organizations

### Targets

| Metric | Target | Rationale |
|--------|--------|-----------|
| Email open rate | 45% | Higher than sector average because contacts are named and specific; mass email benchmark for nonprofits is ~25%, but this is targeted individual outreach with high message-fit. EFF and STOP staff in particular are likely to open on the first send given prior alignment. |
| Reply rate | 20% | Of those who open, roughly 1 in 2 should reply if the personalization is accurate. Overall target means 20% of all sends produce a reply. A send that goes to a named contact with specific personalization (referencing their current campaign) should achieve 30%+ reply. |
| Conversion rate | 2-3 organizations | One policy citation, one training resource integration, or one active referral from a digital rights organization constitutes a conversion. Target: 2-3 out of 12 organizations contacted. This is a 17-25% conversion rate on total sends, which is realistic given high pre-existing alignment. |

### What Counts as Conversion (Digital Rights)

- **Policy citation**: Organization explicitly cites the corpus in a published report, policy brief, or legal filing
- **Training integration**: Organization incorporates the corpus or its Part 0 section into member or public training materials
- **Active referral**: Organization routes the corpus to a specific team or publishes/shares it through their channels
- **Collaboration**: Organization reaches out to co-develop or extend the corpus's threat model

Routing responses ("forwarding to our surveillance team") count as active referrals if followed by the surveillance team making contact. A reply that says "interesting, will pass along" with no follow-up does not count as conversion.

### Failure Threshold and Response

If reply rate is below 10% after 8 sends (Week 1 + Week 2 sends to digital rights sector): re-examine the personalization quality. The most common failure mode in this sector is generic outreach that describes the corpus rather than leading with the recipient's current campaign. Pull the sends where personalization was weakest and rewrite before the Week 3 follow-up.

---

## Sector B: Academic Cybersecurity Programs

### Targets

| Metric | Target | Rationale |
|--------|--------|-----------|
| Email open rate | 35% | Academic contacts open at lower rates than digital rights organizations because institutional emails are higher volume and subject lines about "curriculum resources" are common. Named contacts (Lorrie Cranor, Ann Cleaveland) should open at higher rates than generic department inboxes. |
| Reply rate | 10% | Academic programs have high email volume and slow response cycles. A 10% reply rate means 1-2 replies per 10 sends; given 12 total institutions contacted, that is 1-2 responses. This is a realistic expectation for cold outreach to named faculty. |
| Conversion rate | 1-2 programs | Target: one curriculum citation or formal peer review engagement within 6 months of initial outreach. Academic conversion happens on semester cycles — a May outreach may not convert until September/October. Do not measure academic conversion at the 4-week mark. |

### What Counts as Conversion (Academic)

- **Syllabus citation**: The corpus appears on a course syllabus as assigned or reference reading
- **Research citation**: A faculty member cites the corpus in a research paper, working paper, or presentation
- **Peer review engagement**: A faculty member or graduate student provides formal technical feedback on the countermeasures section
- **Curriculum resource list**: The corpus is included on a program or clinic resource list
- **Clinic case development**: A clinical law program incorporates the FOIA documentation into active case materials

**Important**: Academic conversions take 6-18 months from initial outreach. Do not mark academic contacts as "closed-no conversion" at 4 weeks. Mark them as "hold — September follow-up" and re-engage at the start of fall semester.

### Failure Threshold and Response

If zero replies after 12 academic sends: the subject line is likely the problem. Academic subject lines that lead with "curriculum resource" or "research reference" are competing with hundreds of similar requests. Test a subject line that leads with the technical problem ("FOIA-documented architecture of commercial data purchase for government enforcement — potential research case study") rather than the use case. Alternatively, try a different entry point: search for faculty who have published specifically on commercial surveillance, data broker ecosystems, or immigration technology, and reference their specific publications.

---

## Sector C: Researcher Communities

### Targets

Note: Researcher communities are tracked differently because the primary channel is community posting and conference submission, not individual email.

| Metric | Target | Rationale |
|--------|--------|-----------|
| Email open rate (for individual researcher emails only) | 40% | Individual researchers approached via their published contact pages are likely to open messages that reference their specific work. Generic researcher blasts should not be sent. |
| Reply rate (individual emails) | 15% | Security researchers who open messages that reference their published work reply at moderate rates. The peer-to-peer framing ("I want technical critique") performs better than the institutional framing. |
| Community post engagement | 5+ substantive replies or boosts on Mastodon thread | Mastodon infosec community engagement is measured by thread interaction quality, not just reply count. A thread that attracts 3-5 researchers offering specific technical observations is a success. |
| Conference submission outcome | Track separately | DEF CON 34 CFP: submitted or not. 40C3 call: submitted when available. ShmooCon: contacted. These are pipeline items, not conversion metrics in the traditional sense. |
| Technical corrections received | Aim for 3-5 | This sounds counterintuitive, but receiving specific technical corrections from security researchers means the corpus reached an audience that engaged with it seriously. Each correction improves the corpus. Track corrections as a positive signal, not a failure. |

### What Counts as Conversion (Researcher Communities)

- **Technical peer review**: A named researcher provides written technical feedback on the countermeasures section
- **Conference talk accepted**: A talk submission based on the corpus is accepted at DEF CON, CCC, Black Hat, ShmooCon, or USENIX
- **Research citation**: A researcher cites the corpus in a paper, blog post, or thread
- **Corpus extension**: A researcher publishes a follow-on analysis that builds on the threat model
- **Citizen Lab engagement**: Citizen Lab provides a technical review or co-publishes a related analysis

### Failure Threshold and Response

If community post produces no substantive engagement after 48 hours: check the post timing (best Mastodon post times are Tuesday-Thursday, 10am-2pm Eastern), the tag selection (use #infosec, #surveillance, #privacy, not just #security), and the opening line (it must lead with a technical question or finding, not a description of the corpus). A second post framed as a specific technical question ("Does anyone have post-2024 analysis of Palantir ELITE's commercial data vendor relationships that updates the FOIA documentation?") may work better than a self-promotion post.

---

## Sector D: Journalists and Press Organizations

### Targets

| Metric | Target | Rationale |
|--------|--------|-----------|
| Email open rate | 50% | Journalist organizations are more likely to open messages about active surveillance stories than other sectors. The source protection angle is highly relevant to working journalists in 2026. Named training contacts at FPF and IRE should achieve 60%+ open rates given high personalization. |
| Reply rate | 25% | Journalist organizations tend to respond quickly if they see relevance, or not at all. The 25% target means roughly 2-3 replies from 8-10 journalist sends. FPF and IRE are the highest-probability responders. |
| Conversion rate | 2-3 organizations | Target: one training integration (FPF or IRE), one publication/Toolbox inclusion (SPJ), or one press inquiry. Two to three conversions from 10 journalist contacts is a 20-30% conversion rate — achievable given high pre-existing alignment between the source protection gap and journalist organizations' missions. |

### What Counts as Conversion (Journalists)

- **Training integration**: FPF, IRE, CPJ, or RCFP incorporates the corpus into a training program, workshop, or curriculum
- **Toolbox inclusion**: SPJ adds the corpus to the Journalists Toolbox Digital Security section
- **Press coverage**: A journalist uses the corpus as background research for a story on ELITE, Palantir, or immigration surveillance data infrastructure
- **Resource publication**: A journalist organization publishes a guide or summary that draws on the corpus
- **Speaking opportunity**: An invitation to present or discuss the corpus at an IRE conference, NICAR session, or FPF training event

**Note on press coverage**: If The Intercept, ProPublica, or The Guardian follows up on the direct press outreach, this is a conversion — but it is a different kind than training integration. Press coverage reaches a larger audience but may not align the corpus with the training infrastructure that has long-term source protection impact. Both are valuable; track separately.

### Failure Threshold and Response

If reply rate from journalist organizations is below 10%: the subject line is too generic. Journalist subject lines must lead with the news peg, not the resource description. "Commercial data layer in source protection — undocumented source exposure that Signal doesn't protect against" outperforms "Corpus on digital security for journalists." Also verify that emails to IRE went to the training channel (conference@ire.org) rather than the executive team, which is currently in organizational transition.

---

## Response Tracking Spreadsheet Structure

Use a spreadsheet (Google Sheets or local CSV) with the following column structure. One row per send. This is the minimum viable tracking structure for a campaign of this size.

### Column Definitions

| Column | Values | Notes |
|--------|--------|-------|
| `date_sent` | YYYY-MM-DD | Date the email or post was sent |
| `week` | 1/2/3/4 | Distribution calendar week |
| `sector` | A/B/C/D | Digital Rights / Academic / Researcher / Journalist |
| `organization` | Text | Full organization name |
| `contact_name` | Text | Named individual or "general" |
| `email` | Text | Email address used |
| `template_variant` | Text | Which template variant was used (A-primary, A-EFF, A-AccessNow, etc.) |
| `personalization_score` | 1/2/3 | 1=generic, 2=org-specific, 3=named-contact-with-specific-reference |
| `open` | Y/N/Unknown | Track with email client read receipt or link tracking if available |
| `open_date` | YYYY-MM-DD | Date of open if tracked |
| `reply` | Y/N | Did they reply? |
| `reply_date` | YYYY-MM-DD | Date of reply |
| `reply_type` | None / Positive / Routing / MoreInfo / Negative / Conversion | See categories below |
| `reply_content` | Text (brief) | 1-2 sentence summary of reply content |
| `follow_up_sent` | Y/N | Was a follow-up sent? |
| `follow_up_date` | YYYY-MM-DD | Date of follow-up send |
| `second_follow_up` | Y/N | Second follow-up (two-week check-in) sent? |
| `conversion_type` | Text | What kind of conversion (curriculum, citation, training, press, toolbox, etc.) |
| `next_action` | Text | What is the next step for this contact? |
| `status` | Sent / Active / Converted / Closed / Hold-September | Current status |
| `notes` | Text | Any additional context |

### Reply Type Definitions

| Reply Type | Definition |
|------------|-----------|
| None | No reply received |
| Positive | Expressed interest without yet taking an action |
| Routing | Forwarded to a specific team or person; awaiting that contact |
| MoreInfo | Requested additional information or documentation |
| Negative | Replied to decline or indicate not relevant |
| Conversion | Took a concrete action (citation, curriculum integration, training use, coverage) |

---

## Aggregate Campaign Targets

After 4 weeks of execution (end of May 2026):

| Sector | Sends | Target Opens | Target Replies | Target Conversions |
|--------|-------|-------------|----------------|-------------------|
| Digital Rights | 12 | 5-6 (45%) | 2-3 (20%) | 2-3 |
| Academic | 12 | 4-5 (35%) | 1-2 (10%) | 1-2 (by October) |
| Researcher | 6 direct + 1 community post | 2-3 direct opens (40%) | 1 reply + 5 community interactions | 1-2 (peer review or conference submission) |
| Journalist | 10 | 5 (50%) | 2-3 (25%) | 2-3 |
| **Total** | **~40** | **~16-18 (40%)** | **~7-10 (20%)** | **~7-10** |

**Key indicator to watch at 2 weeks**: If reply rate across all sectors is below 10% by May 19, something systemic is wrong — either the subject lines are not landing, the personalization is insufficient, or there is a deliverability issue. Pull the non-responding sends and audit the subject lines first.

**Key indicator to watch at 4 weeks**: If zero conversions by May 30, the emails are being read but not acted upon. This suggests the call to action is too vague or the ask is too large for a first contact. Consider reducing the initial ask (from "review the corpus" to "I'd appreciate being routed to the right team") and testing a shorter email body.

---

## Iteration Framework

### After Week 2 (May 16): Subject Line Audit

Compare open rates for Week 1 digital rights sends versus Week 2 journalist sends. The sector with higher open rates has a better-performing subject line. Apply lessons from the higher-performing variant to the Week 3 academic sends.

### After Week 3 (May 23): Reply Quality Audit

Categorize all replies by type (Positive / Routing / MoreInfo / Negative). Calculate the ratio of MoreInfo replies: if this is high (more than half of all replies), the corpus description in the template body is unclear or incomplete. Revise the body for Week 4 sends.

### After Week 4 (May 30): Full Campaign Review

1. Calculate final open rate, reply rate, and conversion rate per sector
2. Identify the two highest-performing sends (by conversion quality, not just reply rate) — analyze what the personalization and template choice had in common
3. Identify the two lowest-performing sends — what would you change?
4. Flag contacts for September re-engagement (academic programs that showed initial interest, researcher contacts where 40C3 call is now open)
5. Note any corpus errors identified through technical review and update the Gist before the September wave

### September 2026 Re-Engagement Wave

A partial second wave targeting:
- Academic programs that expressed interest but didn't convert (fall semester curriculum planning window)
- 40C3 submission for December 2026 (if call for participation opens)
- Any digital rights organizations that were in organizational transition or undergoing staff changes in May
- New contacts identified through organic distribution or researcher community referrals

---

*Metrics document complete. Spreadsheet structure is immediately deployable as Google Sheets or CSV. For contact details, see `tier-2-sector-contact-lists.md`. For calendar sequencing, see `tier-2-distribution-calendar.md`.*
