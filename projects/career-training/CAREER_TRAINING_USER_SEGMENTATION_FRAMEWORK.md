---
title: "Career Training User Segmentation Framework"
project: career-training
phase: "2-3"
created: 2026-06-28
status: implementation-ready
---

# Career Training User Segmentation Framework

**Scope**: Defines subscriber segments, their behavioral characteristics, engagement triggers, scoring model, and phase progression logic for the career-training curriculum email list. Designed for implementation in Kit (primary recommendation) or Mailchimp.

---

## Segmentation Philosophy

The curriculum has a natural segmentation structure: three learning paths, four audience archetypes, and two engagement states (active vs. inactive). The tagging system must capture all three dimensions simultaneously without creating fragmented or conflicting subscriber states.

**Design constraints:**
- Kit free plan: 1 automation (use branching logic within single automation to cover all paths)
- Kit Creator plan: Unlimited automations (full multi-path model below)
- Mailchimp Standard: Customer Journeys automation covers equivalent functionality

The framework below describes the full model. Where the free plan requires simplification, notes indicate workarounds.

---

## Dimension 1: Learning Path Tags (Applied at Signup)

These tags are applied when a subscriber signs up and should be considered permanent — they define the subscriber's primary career intent. A subscriber may carry multiple path tags (rare, but possible for an instructor covering all paths).

| Tag | Applied When | Meaning |
|-----|-------------|---------|
| `path-industrial` | Signs up via Industrial GC form OR quiz result | Target career: Industrial GC or PM |
| `path-residential` | Signs up via Residential GC form OR quiz result | Target career: Residential GC |
| `path-specialty-sub` | Signs up via Specialty Sub form OR quiz result | Target career: Sub to Foreman to PM |
| `path-instructor` | Self-identifies as instructor on form OR quiz | Teaching role; not on a career path themselves |
| `path-career-changer` | Self-identifies on quiz as "new to construction" | No prior construction experience |
| `path-untagged` | No quiz taken, generic signup | Path unknown; needs Day 2 path selection email |

**Implementation on static site:**
- Build one form per path (Kit allows multiple forms)
- Each form has a hidden field that sends the tag on submit
- The Quiz Lead Magnet sets the tag based on answer routing

**For Kit free plan (1 automation):** Use a single welcome automation with `If subscriber has tag X → send Email A; if tag Y → send Email B` conditional branching within one automation. This covers 5 path variants in a single automation workflow.

---

## Dimension 2: Audience Archetype Tags (Applied at Signup, Updated by Behavior)

These capture WHY the subscriber is here, which predicts what content they want.

| Tag | Applied When | Content Preference |
|-----|-------------|-------------------|
| `archetype-gcing` | Running or planning to run a GC business | Business operations, legal compliance, CSLB, lien rights |
| `archetype-career-advance` | Moving from trade to PM/superintendent | Technical modules, scheduling, cross-trade knowledge |
| `archetype-compliance` | Focused on regulatory/legal topics | Code updates, Cal/OSHA, prevailing wage, CSLB |
| `archetype-instructor` | Teaching or curriculum development | Instructor guide, syllabi, rubrics, pedagogy |
| `archetype-new-to-industry` | Career changer; limited construction experience | Foundations, glossary, "start here" orientation |

These are applied via quiz answer or by inferred behavior (subscriber only clicks regulatory update emails → add `archetype-compliance` tag via automation trigger).

---

## Dimension 3: Engagement State Tags (Applied by Automation, Updated Continuously)

These reflect current subscriber behavior, not intent. They drive re-engagement and sequence routing.

| Tag | Applied When | Action Triggered |
|-----|-------------|-----------------|
| `engagement-active` | Opened email in last 14 days | Continue standard sequence |
| `engagement-warm` | Opened email in last 15-30 days | No action; normal send cadence |
| `engagement-cooling` | No open in 31-45 days | Tag applied; queue re-engagement email in 7 days |
| `engagement-inactive` | No open in 46-60 days | Send re-engagement email; pause regular sequences |
| `engagement-churned` | No open in 61+ days despite re-engagement | Remove from active sequences; archive or suppress |
| `engagement-high` | Opened 4+ emails AND clicked 2+ links in 14 days | Fast-track content; case study bundle offer |

**Important**: These tags must be updated by automations that run on a schedule or on subscriber activity. On Kit Creator Pro, subscriber scoring (0-100) does this automatically. On Kit free/Creator, set up conditional automations triggered by "subscriber has not opened any email in X days."

---

## Engagement Scoring Model

### Simple Scoring (Kit Free/Creator Plan)

Without Kit Creator Pro's native subscriber scoring, use a points-based tag system:

**Point events:**
- Email open = 1 point
- Email click-through (any link) = 3 points
- Module page visit (tracked via GA4 UTM links in email) = 5 points — note: Kit cannot detect this directly; use a "clicked module link" tag applied via Kit automation when subscriber clicks a tracked link
- Case study link click = 4 points
- Lead magnet download = 5 points
- Social share click = 4 points
- Signed up for instructor resources = 8 points

**Score thresholds:**
- 0-5 points in 30 days: Tag `engagement-cooling`
- 6-15 points in 30 days: Tag `engagement-warm`
- 16-30 points in 30 days: Tag `engagement-active`
- 31+ points in 30 days: Tag `engagement-high`

**Implementation**: In Kit, create automations triggered by "subscriber clicks link X" that apply point-tracking tags. This requires tagging each link in emails with unique identifiers and building tracking automations for each event. It is non-trivial but achievable on the Creator plan.

**Simpler alternative**: Use Kit's native segment filter "opened at least X emails in last 30 days" without explicit point tracking. This gives coarse engagement tiers (high/medium/low) that work well enough for Phase 2.

### Advanced Scoring (Kit Creator Pro — $59/mo at 1,000 subscribers)

Kit Creator Pro's subscriber scoring assigns a 0-100 score automatically based on open rates, click rates, and recency of engagement. Score below 30 → re-engagement automation triggered automatically.

**Recommendation**: Start with simple open-based tiers on free plan. Upgrade to Creator Pro when list reaches 500 subscribers and the manual tagging system becomes unmanageable.

---

## Segment Definitions: Phase 2 Operating Model

These are the actionable segments you will actually use in Kit/Mailchimp during Phase 2. All segments are dynamic (filter-based), not manually maintained.

### Segment 1: Active Residential GC Learners

**Filter**: Tagged `path-residential` AND tagged `engagement-active` (opened email in last 14 days)

**Email cadence**: 2x per month (bi-weekly digest)

**Content mix**:
- California regulatory updates (CSLB, Title 24, ADU statute)
- Module excerpts from Residential GC Path Phase 3-5 modules (business, legal, specialty scopes)
- Case studies: Module 13 (lien rights), Module 32 (change orders), Module 25 (construction finance)
- "Module spotlight" deep-dives 1x/month

**Social routing**: LinkedIn content targeting GC business owners (case study questions, "what would you do?" scenarios from Module 13, 30, 32)

### Segment 2: Active Industrial GC Learners

**Filter**: Tagged `path-industrial` AND tagged `engagement-active`

**Email cadence**: 2x per month

**Content mix**:
- ASME code updates, industrial PM career tips
- Module excerpts: Module 1-4 (industrial foundations), Module 29 (dispute resolution), Module 33 (QC)
- Case studies: SIMOPS scenarios, CPM scheduling conflicts, industrial change order pricing
- Industrial sector news (manufacturing, process industry, heavy civil)

**Social routing**: LinkedIn targeting industrial PMs; case studies in survey format ("How would you handle SIMOPS on a live plant?")

### Segment 3: Active Specialty Sub Learners

**Filter**: Tagged `path-specialty-sub` AND tagged `engagement-active`

**Email cadence**: 2x per month

**Content mix**:
- Trade-to-PM career development content
- Module excerpts: Module 6 (architecture for GC), Module 24 (specs), Module 32 (change orders)
- Case studies: Drawing conflict scenarios, lien waiver situations, schedule delay documentation
- "Career story" format: "How an electrician became a $2M PM" — framed for their specific aspiration

**Social routing**: LinkedIn and Instagram (slightly younger demographic); TikTok if you expand there

### Segment 4: Instructors

**Filter**: Tagged `path-instructor`

**Email cadence**: 1x per month (not bi-weekly — instructors are busy professionals; over-emailing risks unsubscribe)

**Content mix**:
- Instructor guide updates
- Sample syllabi and assessment rubrics
- Community college and union training program news
- "How other instructors are using this curriculum" case studies
- Module update notifications (time-sensitive for instructors building lesson plans around module content)

**Social routing**: LinkedIn only; target "educator" in construction space

### Segment 5: Career Changers

**Filter**: Tagged `path-career-changer` OR tagged `archetype-new-to-industry`

**Email cadence**: Weekly (this segment needs more handholding; weekly emails keep them on track)

**Content mix**:
- "Start here" orientation content (first 30 days)
- Glossary term of the week
- Foundational module excerpts (Module 1, 6, 7 — no jargon, accessible)
- Encouragement copy: "You don't need experience; you need a system"
- Veterans pathway framing (if military → construction angle)

**Social routing**: LinkedIn for professional development framing; potentially YouTube for longer-format "how to get into construction" content

### Segment 6: High Engagement (Cross-Path)

**Filter**: Tagged `engagement-high` (regardless of path tag)

**Email cadence**: Weekly case study (in addition to path-specific bi-weekly digest)

**Content mix**:
- Case study of the week (from 150-scenario workbook)
- "Fast track" reading suggestions for their path
- Social sharing invitation: "Share this scenario with your team on LinkedIn"

**Rationale**: High-engagement subscribers are your most likely sharers, advocates, and eventual paid customers. They deserve more content and more social activation prompts.

### Segment 7: Re-engagement (Cooling + Inactive)

**Filter**: Tagged `engagement-cooling` OR `engagement-inactive`

**Email cadence**: 1-2 re-engagement emails, then pause

**Content mix**:
- Subject line change (try a plain-text subject when previous subject lines haven't worked)
- "We miss you" minimal email: 3 sentences maximum
- New lead magnet offer if one exists since their signup
- Final re-engagement: "Still want construction training emails? Click here to stay subscribed."
- If no click after final re-engagement: tag `engagement-churned`, remove from all active sequences

**Do not**: Delete churned subscribers from the list. Keep them suppressed for potential re-engagement in 6 months if a major content update (e.g., a new module launch) justifies a reactivation campaign.

---

## Phase Progression Model

As subscribers complete phases of the curriculum, their engagement behavior changes. The segmentation model should reflect phase progression.

### Detecting Phase Progression (Without Native LMS)

Since the career-training site is a static site without native progress tracking, phase progression must be inferred from email behavior:

**Phase 1 → Phase 2 indicator**: Subscriber clicked module links for Phase 1 modules (Modules 1-4 for Residential, or Modules 1-3 for Industrial) within 30 days of signup

**Phase 2 → Phase 3 indicator**: Subscriber clicked Phase 2 module links (Modules 5-8 for Residential) within 60 days

**Implementation**: Tag each module link in emails with module-specific tracking URLs. When subscriber clicks a Phase 2 module link → automation applies tag `phase-2-started`. This does not confirm they read the module, but it confirms site engagement beyond Phase 1.

**Alternative (simpler)**: Send a "Check-in" email at Day 30: "Which phase are you on?" with one-click options. Each click applies a phase tag. Response rate will be 15-25%, covering your most engaged subscribers — exactly the cohort whose phase you most want to know.

**Phase-Triggered Actions:**

| Phase Tag | Trigger | Content Action |
|-----------|---------|---------------|
| `phase-1-complete` (inferred or self-reported) | At Day 30 check-in or module click behavior | Send Phase 2 module list email; offer Phase 1 case study bundle |
| `phase-2-started` | Module click from Phase 2 email | Add "Phase 2 deep dive" resource to next email |
| `phase-3-started` | Module click from Phase 3 email (business/legal phase) | Send "CSLB licensing checklist" lead magnet as Phase 3 companion |
| `path-complete` | Self-reported via check-in OR clicks on final phase module | Send congratulations email; ask for testimonial; offer next path preview |

---

## Implementation Order for Phase 2

**Week 1 (required to launch):**
- [ ] Build 3 path-specific signup forms in Kit (each applies one path tag)
- [ ] Build 1 generic signup form for homepage (applies no path tag; Day 2 email will prompt path selection)
- [ ] Load all 6 welcome sequence emails (Days 0/2/4/7/10/14)
- [ ] Build single welcome automation with path-tag branching (if `path-residential` → send residential Day 0 variant; etc.)
- [ ] Segment 7 (re-engagement) automation: if no email open in 30 days → queue re-engagement email → if no open in 7 days → tag `engagement-inactive`

**Week 2-4 (nice to have, adds value immediately):**
- [ ] Build 14-day check-in email (Day 30 self-reported phase tracking)
- [ ] Tag links in emails with unique tracking identifiers
- [ ] Build click-to-tag automations for Phase 2, Phase 3 progression
- [ ] Build Segment 6 (High Engagement) sub-list for weekly case study sends

**Month 2+ (post-launch optimization):**
- [ ] Review which segments have highest open rates; adjust cadence for underperforming segments
- [ ] A/B test subject lines for each path's monthly digest
- [ ] Build instructor-specific monthly digest sequence
- [ ] Evaluate upgrade to Kit Creator plan if automation limits require multi-sequence support

---

## Segment Performance Targets (Phase 2, Months 1-6)

| Segment | Expected List % | Open Rate Target | Click-Through Target | Notes |
|---------|-----------------|-----------------|---------------------|-------|
| Active Residential GC | 40-50% | 38-42% | 6-8% | Largest segment; California-specific content resonates |
| Active Industrial GC | 20-25% | 35-40% | 5-7% | Smaller but high-value; industrial PMs earn more → higher LTV |
| Active Specialty Sub | 15-20% | 32-38% | 4-6% | Diverse demographic; trade-specific content improves rates |
| Instructors | 5-10% | 45-55% | 8-12% | Small but highest open rate; highly motivated audience |
| Career Changers | 5-10% | 30-35% | 3-5% | Higher churn risk; weekly cadence helps retention |
| High Engagement | 10-15% (overlap) | 55-65% | 12-18% | Overlap segment; highest performers |
| Re-engagement | 10-20% | 15-25% | 1-3% | Expected to shrink over time as inactive subscribers churn |

---

## Sources

- [Email Marketing Segmentation 2026 — Monday.com](https://monday.com/blog/monday-campaigns/email-segmentation/)
- [Email Marketing for Online Courses 2026 — EmailToolTester](https://www.emailtooltester.com/en/blog/email-marketing-for-online-courses/)
- [7 Best Email Tools with Subscriber Segmentation 2026 — Sequenzy](https://www.sequenzy.com/blog/best-email-tools-with-subscriber-segmentation)
- [Advanced Email Segmentation Strategies — InsiderOne](https://insiderone.com/advanced-email-segmentation-strategies-best-practices/)
- [Tags and Segments in Kit — Kit Help Center](https://help.kit.com/en/articles/4257108-tags-and-segments-in-kit-and-when-to-use-which)
- [AI Email Segmentation: How Machine Learning Doubled Open Rates — DEV Community](https://dev.to/synergistdigitalmedia/ai-email-segmentation-how-machine-learning-actually-doubled-my-open-rates-without-the-bs-3daj)
- [19 Best Email Marketing Tools for Course Creators 2026 — Sequenzy](https://www.sequenzy.com/email-marketing-for/course-creators)
