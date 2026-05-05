---
title: "Feedback Collection Protocol — Full-Channel Design"
project: cybersecurity-hardening
created: 2026-05-05
status: ready-for-use
depends-on: post-distribution-impact-tracker.md, tier-1-feedback-collection-protocol.md
---

# Feedback Collection Protocol

**Purpose**: Establish the full-channel feedback infrastructure across quantitative surveys, qualitative community channels, expert review, and structured triage. The companion document `tier-1-feedback-collection-protocol.md` covers the email-based follow-up cadence for Tier 1 organizational outreach. This document covers the broader feedback ecosystem needed for individual users (journalists, attorneys, activists, undocumented immigrants) who find the guide independently rather than through organizational outreach.

**Lead finding**: Feedback design must accommodate two structurally different user types: (1) organizational contacts who receive the guide through direct outreach and can be followed up by email, and (2) individual users who download the guide through a referral chain and have no prior relationship with the author. For type-1, the email follow-up cadence in `tier-1-feedback-collection-protocol.md` is sufficient. For type-2, feedback channels must be embedded directly in the guide itself and designed for anonymous, low-friction submission.

---

## Section 1: Quantitative Feedback — Embedded Survey

### Design Rationale

A 5-question survey embedded in the guide at the end of each tier section captures structured feedback at the moment of highest engagement — immediately after a user completes or abandons a tier. A single link that opens a pre-filled Google Form (with the tier number already selected) reduces friction to under two minutes.

### Survey Questions

**Question 1** (categorical, required): Which tier are you implementing?
- Tier 1 (individual hardening — data broker opt-outs, Signal, ProtonMail)
- Tier 2 (institutional hardening — newsroom or legal organization)
- Tier 3 (state-level adversary defense — Tails, Monero, Rayhunter, operational security)
- Just exploring (not yet implementing)

**Question 2** (categorical, required): What's your background?
- Journalist or freelance reporter
- Immigration attorney or paralegal
- Activist or organizer
- Undocumented immigrant or mixed-status household
- Legal aid staff (non-attorney)
- Security researcher or technologist
- Other (free text)

**Question 3** (categorical, required): Which tool or section are you most focused on?
- Signal (secure messaging)
- ProtonMail (encrypted email)
- Tails OS (anonymous operating system)
- Data broker opt-outs (manual removal)
- California DROP platform (automated deletion)
- Encrypted file storage (VeraCrypt)
- Monero (financial privacy)
- Rayhunter (IMSI catcher detection)
- ELITE system countermeasures (address masking, record management)
- Other (free text)

**Question 4** (multi-select, required): What's the biggest gap or barrier in the guide?
- Tool compatibility issue (didn't work on my device/OS)
- Missing use case (my situation isn't covered)
- Too technical (can't follow the steps)
- Not technical enough (needs more depth)
- Cost barrier (tool or hardware is too expensive)
- Language barrier (need a Spanish version)
- Legal context missing (need state-specific legal guidance)
- Operational friction (too many steps for daily use)
- Other (free text)

**Question 5** (yes/no, required): Would a video walkthrough help?
- Yes, for the tool setup steps
- Yes, for the strategic/conceptual sections
- No, the written guide is sufficient

**Optional follow-up** (free text, not required): What's the single most important thing this guide should cover that it currently doesn't? (2-3 sentences maximum)

### Deployment

Embed the survey link at:
- The end of each tier section's checklist (labeled "How was this section? 2-minute feedback")
- The end of the full guide (labeled "Help improve the next version — 5 questions")
- The 30-day follow-up email to individual users who downloaded via referral link (if email collected)

Use Google Forms (free tier) with response notifications enabled. Export responses to a local CSV weekly. Do not collect IP addresses or identifying information unless a respondent voluntarily includes it in the free-text fields.

### Response Goals

| Milestone | Target Response Volume | Key Signal to Watch |
|-----------|----------------------|-------------------|
| Month 1 | 25+ responses | Which tier is most-used? Which tools have highest friction? |
| Month 2 | 75+ responses | Gap consensus emerging? (≥3 responses citing same barrier) |
| Month 6 | 300+ responses | Statistical signal on barriers by audience segment |
| Month 12 | 500+ responses | Phase 2 prioritization data sufficient |

**Analysis approach**: Run a monthly pivot of Q4 (barriers) by Q2 (background). A barrier that appears in 40%+ of responses from a specific audience segment is an actionable gap. A barrier that appears in fewer than 10% is an outlier. Track month-over-month changes — a barrier that increases from 5% to 20% over three months signals a tool ecosystem change (e.g., a Signal update broke an installation step).

---

## Section 2: Qualitative Feedback Channels

### Reddit

**Priority subreddits**: r/privacy, r/netsec, r/immigration, r/legaladvice, r/ImmigrationLaw

**Monitoring approach**:
- Set up Reddit username alerts via F5bot.com (free, monitors mentions by keyword across Reddit) for: "palantir ELITE", "data broker immigration", "DROP platform", "undocumented security", and the Gist URL
- Check monitored subreddits weekly in Month 1, monthly thereafter
- Respond to questions within 24 hours in the first 30 days; this is the window when early adopters are most likely to engage and when fast responses generate the most goodwill
- Do not post the guide as self-promotion without engaging substantively with the community first; the most effective Reddit entry is responding helpfully to an existing thread about immigration security or data broker opt-outs and offering the guide as a resource

**Community AMA (conditional)**: If a subreddit post mentioning the corpus receives 50+ upvotes or 20+ comments, consider requesting a community AMA (Ask Me Anything) in the relevant subreddit. AMA format generates concentrated, high-quality qualitative feedback and is particularly effective in technical communities (r/netsec, r/privacy). Threshold to initiate: organic Reddit engagement at 90-day mark showing meaningful community interest.

### Mastodon / fediverse

**Priority instances**: infosec.exchange (security community), social.coop (activist/cooperative community), mastodon.social (general)

**Monitoring approach**:
- Search for corpus-related terms weekly in Month 1 using infosec.exchange search and Mastodon's native advanced search
- The adoption-tracking-dashboard-spec.md (Component 2) documents the full social media monitoring protocol; this section adds the feedback response dimension
- When a post mentioning the corpus appears, respond with additional context or offer to answer questions via direct message
- For the technical security community (infosec.exchange), frame responses around the threat model documentation rather than the implementation guide — security researchers engage more with the adversary analysis

**Community post at 90-day threshold**: If the Gist view count is below 300 at 90 days, publish one public Mastodon post on infosec.exchange framing the corpus as a technical problem ("FOIA-documented Palantir ELITE commercial data purchase architecture and what immigration-adjacent organizations can do about it"). Include a request for technical critique, not just distribution — this frames the corpus as peer research rather than advocacy, which generates more substantive engagement from security researchers.

### GitHub Issues

If the corpus is migrated from a Gist to a full GitHub repository, create two issue templates:

**Template 1: "This guide doesn't work for my setup"**

```
## What I was trying to do
[Describe the step you were following]

## What happened instead
[What error or problem occurred]

## My setup
- Operating system:
- Device type:
- Tool version:

## Steps I already tried
[List what you tried before opening this issue]
```

**Template 2: "I'm missing a topic"**

```
## What I need to do (threat model or use case)
[Describe your situation in 1-2 sentences — no identifying information needed]

## What the guide currently says about this
[The closest section you found]

## What's missing
[What specific guidance would help]

## My background (optional)
[Journalist / Attorney / Activist / Undocumented immigrant / Other]
```

**Issue triage SLA**: Assign a weekly 15-minute review of open issues. Close duplicates by linking to existing open issues. Tag each issue with one of the five feedback categories (see Section 3 below). Issues tagged "Error/Bug" should be addressed within 72 hours if the error would prevent a user from completing a critical security step. Issues tagged "Gap/Missing Content" are input to the Phase 2 prioritization framework.

### Email Feedback Channel

Maintain a dedicated `feedback@` address (or equivalent secure contact) prominently displayed:
- At the top of the corpus (before Part 0) in a "Questions and feedback" section
- At the end of each tier section
- In the 30-day organizational follow-up emails

**Email triage**: Check once per week. Log each email in the feedback tracker CSV. Respond to all emails within 5 business days. If the email describes a security urgency (user in immediate risk, tool failure in a high-stakes situation), respond within 24 hours.

**Anonymous feedback path**: Email is not anonymous. Provide a separate anonymous feedback path for users who cannot safely disclose their identity:
- A Signal number (the same number used for secure contact) accepts anonymous feedback messages
- A Tails-accessible Tor-onion feedback form (if technical capacity exists) is the most secure option
- A paper mail address at a nonprofit intermediary (with consent) for users without reliable internet access

### User Testimonials

**Active solicitation approach**: Include a specific testimonial request in the 90-day follow-up email to organizations that showed Stage 2+ adoption:

> "If your staff or clients have a story about how this guidance helped — even just a small win, like completing the data broker opt-outs — I'd like to document it as an anonymous example. No names, no identifying details. Even a one-sentence description of what changed helps."

**Collection format**: A short Signal or email message is sufficient. Do not require a formal testimonial format — this creates friction. Any narrative that describes a concrete outcome ("my source now contacts me on Signal") or a near-miss ("I had left my phone at home the day ICE visited my neighborhood") is publishable content after anonymization.

**Anonymization standard**: Remove all identifying information before publishing. Replace organization names with category descriptors ("a California immigration legal aid organization") unless the organization explicitly requests attribution. Do not include geographic specifics below the state level. Do not include client case details.

**Publication format**: Quarterly anonymized impact narrative. Four times per year, compile 2-4 anonymized testimonials into a brief (500-word) narrative published on the same channels used for distribution (Mastodon, email follow-up, organizational newsletters). This creates a feedback loop that motivates continued engagement and serves as social proof for new distribution channels.

### Expert Feedback

**Target reviewers**: 5-10 individuals across three categories:

1. **Security researchers** (priority: Citizen Lab researchers, EFF technologists, security academics who have published on surveillance of civil society or commercial data brokers). Contact via email or Mastodon with a specific technical question, not a generic review request. Example: "I've documented Palantir ELITE's commercial data purchase architecture from FOIA contracts — I'd like your assessment of whether the countermeasures in Section X adequately address the threat."

2. **Immigration law scholars and practitioners** (priority: researchers who have published on immigration enforcement technology, clinical faculty at immigration law clinics). Contact via email referencing their published work. Ask for: (a) legal accuracy of any legal claims in the corpus, (b) assessment of whether the AB 60/DROP platform guidance is correctly described.

3. **Activist technologists** (priority: individuals who have published operational security guidance for activist communities, trainers at EFF's digital security training events, or individuals with documented experience advising activist communities in surveillance-heavy environments). Contact via Mastodon or Signal.

**Review format**: 30-minute phone or Signal call, or a written response to three specific questions:
1. Is anything in the threat model factually wrong or misleading?
2. What's the most important countermeasure missing from the guide?
3. What's the one change that would most improve effectiveness for your audience?

**Cadence**: One round of expert review before initial distribution (pre-launch), one round at 6 months post-distribution (incorporating user feedback into a revised review).

---

## Section 3: Feedback Triage and Categorization

### Five-Category Triage Matrix

| Category | Definition | Escalation Level | Response SLA | Action Owner |
|----------|-----------|-----------------|--------------|--------------|
| **Error/Bug** | Guide step doesn't work as written (installation failure, broken link, factually wrong information) | Critical — requires guide revision | 72 hours | Guide author |
| **Gap/Missing Content** | Guide doesn't cover a use case or threat model | High — feeds Phase 2 prioritization | 1 week | Queue for Phase 2 review |
| **Confusion** | Guide language is unclear, steps are hard to follow | Medium — rewrites required | 2 weeks | Guide author |
| **Enthusiasm** | Positive outcome, helpful testimonial, successful implementation | Low urgency — amplification opportunity | 1 week | Publish anonymized if consent given |
| **Out of Scope** | Request for unrelated security help, general privacy advice unrelated to threat models | Triage only — redirect | 2 business days | Redirect to appropriate resource |

### Triage Decision Tree

```
Is the feedback about a specific guide step that doesn't work?
  YES → Error/Bug → Fix within 72 hours; update Gist; log version change
  NO → continue

Is the feedback requesting guidance not covered in the current guide?
  YES → Gap/Missing Content → Log in Phase 2 queue with: (a) user background, (b) gap description, (c) estimated prevalence
  NO → continue

Is the feedback expressing confusion about existing content?
  YES → Confusion → Log specific confusing section; add to clarity revision queue
  NO → continue

Is the feedback a positive outcome story?
  YES → Enthusiasm → Request anonymization consent; add to quarterly testimonial report
  NO → Out of Scope → Redirect to appropriate resource (EFF SSD, Access Now, NILC)
```

### Weekly Review Ritual (15 minutes)

Every Monday morning, run through the following:

1. Open feedback inbox (email, GitHub issues, form responses from prior week)
2. Assign each piece of feedback to one of the five categories
3. Check if any Error/Bug items require same-week guide updates
4. Add all Gap items to the Phase 2 candidate log with date and source
5. Note any feedback that represents a new audience segment or unexpected use case
6. Respond to any unanswered feedback that is older than the relevant SLA

**Key question to ask every week**: Is there a pattern? If three different users in the same week report confusion about the same step, that is a content emergency — the guide is failing at that point for a meaningful percentage of users. If three different users request the same missing topic, that is a Phase 2 input. Pattern detection is the primary purpose of the weekly ritual.

### Monthly Synthesis (30 minutes)

On the first Monday of each month, run the monthly synthesis:

1. Export feedback form responses from the past 30 days to CSV
2. Run the Q4 (barriers) × Q2 (background) pivot — which barriers are appearing for which audience segments?
3. Count unique Gap requests — are any gaps mentioned by 3+ different users?
4. Identify top 3 themes from qualitative channels (Reddit, email, testimonials)
5. For each theme: is it a guide revision (immediate work) or a Phase 2 content area (queue for later)?
6. Update the Phase 2 prioritization log with new gap inputs
7. Note any changes in the feedback volume or sentiment trend

**Decision rule**: Any gap mentioned by ≥3 respondents with ≥40% of responses from a single audience segment triggers a review of whether it can be addressed with a guide revision (quick win) or requires a new document (Phase 2 work).

---

## Section 4: Feedback Integration into Guide Iterations

### Version Control and Update Policy

Maintain a change log at the top of the corpus. Each version update triggered by feedback should include:
- Date of update
- Nature of the change (Error fix / Clarity revision / New content)
- Which feedback category triggered the change

Example entry:
```
v1.2 — 2026-08-01
- [Error fix] Tails OS USB creation instructions updated for Tails 7.x (prior instructions were for 6.x; reported by 4 users via help desk)
- [Clarity revision] DROP platform enrollment steps rewritten in plain language; added note about August 1 processing deadline
- [New content] Added brief section on Rayhunter procurement and basic deployment based on 6 user requests
```

### Feedback-to-Guide Revision Cycle

| Trigger | Action | Timeline |
|---------|--------|---------|
| 3+ Error/Bug reports for the same step | Revise that section immediately | Within 72 hours |
| 3+ Confusion reports for the same section | Rewrite for clarity | Within 2 weeks |
| 3+ Gap requests for the same topic | Review for quick-win addition vs. Phase 2 scope | Within 1 month |
| Major tool update (Signal, Tails, ProtonMail release) | Review affected sections against new tool version | Within 7 days of tool release |
| Regulatory change (DROP platform, California AB 1766, FISA) | Review and update affected legal/procedural sections | Within 14 days of change |

---

*Protocol complete. Use in conjunction with `tier-1-feedback-collection-protocol.md` for organizational email follow-up cadence, `phase-2-prioritization-criteria.md` for Phase 2 gap analysis, and `adoption-tracking-dashboard-spec.md` for passive monitoring infrastructure.*

**Sources**:
- Reddit community engagement research: [Security Awareness Training Statistics 2025](https://www.brside.com/blog/security-awareness-training-statistics-2025-100-studies)
- SAFETAG feedback and adoption outcomes: [Internews SAFETAG evaluation findings](https://greaterinternetfreedom.org/success_stories/evaluation-findings-safetag-audits-increase-digital-security-of-organizations-and-lead-to-changes-in-attitude-and-behavior/)
- California DROP platform: [Privacy.ca.gov DROP overview](https://privacy.ca.gov/drop/about-drop-and-the-delete-act/)
- FPF digital security training: [FPF Digital Security Education](https://freedom.press/digisec/)
- EFF Rayhunter deployment: [EFF Rayhunter announcement](https://www.eff.org/deeplinks/2025/03/meet-rayhunter-new-open-source-tool-eff-detect-cellular-spying)
