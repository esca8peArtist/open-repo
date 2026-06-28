---
title: "Welcome Email Sequence — Draft Copy"
project: career-training
phase: "2"
created: 2026-06-28
status: copy-paste-ready
module-reference: "Module 14 — Site Safety and Cal/OSHA Compliance"
automation: "path-routing-rule (Kit free plan, 1 of 1 allowed)"
---

# Welcome Email Sequence — Draft Copy

**Purpose**: Complete, copy-paste-ready email copy for the 3-email welcome sequence. Based on Module 14: Site Safety and Cal/OSHA Compliance content, which is the most universally relevant module across all three paths (every residential GC, industrial GC, and specialty sub must maintain a safety program).

**Sequence**: Days 0, 3, and 7 (3 emails total as specified in the Exploration Queue Item 22 brief; the full 6-email sequence outline lives in EMAIL_SOCIAL_FUNNEL_STRATEGY.md).

**Automation rule**: This is the path-routing welcome rule. It is the single automation allowed on the Kit free plan. It is the highest-priority automation — do not use the free plan's one automation slot on anything else.

---

## Automation Rule Logic

Before the email copy, understand the automation structure this sequence lives inside.

### The Path-Routing Welcome Rule (Kit Free Plan — 1 of 1 Automations)

**Entry trigger**: Subscriber joins any of the 4 signup forms

**Branching conditions** (IF branching is available on the free plan — see KIT_ACCOUNT_SETUP_CHECKLIST.md Feature Audit):

```
TRIGGER: New subscriber added
        |
        v
[Check: subscriber tagged "residential-gc"?]
    YES → Enter Residential GC Welcome Sequence (this sequence, residential copy)
    NO  → [Check: subscriber tagged "industrial-gc"?]
            YES → Enter Industrial GC Welcome Sequence (industrial copy)
            NO  → [Check: subscriber tagged "specialty-sub"?]
                    YES → Enter Specialty Sub Welcome Sequence (specialty sub copy)
                    NO  → Enter Generic Welcome Sequence (path confirmation email first)
```

**If Kit free plan does NOT support branching** (confirmed as a risk in KIT_ACCOUNT_SETUP_CHECKLIST.md):

Use 4 separate Sequences instead of branching inside a single automation:
- Residential GC Path form → directly enrolled in "Residential GC Welcome Sequence" at subscribe
- Industrial GC Path form → directly enrolled in "Industrial GC Welcome Sequence" at subscribe
- Specialty Sub Path form → directly enrolled in "Specialty Sub Welcome Sequence" at subscribe
- Generic form → directly enrolled in "Generic Welcome Sequence" at subscribe

This avoids the branching requirement entirely. The form itself routes the subscriber to the correct sequence. Verify whether Kit free plan allows multiple Sequences (separate from the 1-automation limit).

---

## Email 1 — Day 0: Welcome + Path Selection Link

**Timing**: Sent immediately after subscribe (within 1-2 minutes of form submission)  
**Trigger**: Subscriber joins any signup form  
**Subject line**: You're in. Here's where to start.  
**Preview text**: 33 modules, 3 paths, one place to build your career.  
**Sender name**: [Your name] | Construction Career Training  
**Length**: Under 200 words (for professional audiences, brevity signals respect)

---

**Subject**: You're in. Here's where to start.

Hi [First Name],

Welcome. You just joined a 33-module construction career curriculum built for one purpose: giving working contractors and tradspeople the exact technical knowledge needed to move up, start their own company, or manage larger projects.

Before I send you anything else, I want to make sure you're on the right path.

**Which of these describes you?**

- [Residential GC Path] — You're building or scaling a residential contracting business in California. Focus: licensing, estimating, residential codes, and ADU/remodel work. [LINK → residential path overview page on site]

- [Industrial GC Path] — You're a PM, field super, or subcontractor moving into large commercial or industrial project management. Focus: contracts, ASME codes, SIMOPS, industrial MEP. [LINK → industrial path overview page on site]

- [Specialty Sub Path] — You're a specialty trade (mechanical, electrical, civil, fire protection) building your own sub business or expanding scope. Focus: bidding, lien rights, trade-specific codes. [LINK → specialty sub path overview page on site]

Click your path. I'll send you the right content from here.

[Your name]

---

**P.S.** Every module is free, no paywall, no account required. Just read.

---

**AUTOMATION NOTE**: If the subscriber was already tagged at subscribe (via a path-specific form), this email can be simplified to confirm their path: "You signed up via the Residential GC Path form. That's where we'll start." Replace the three-link list with a single "Your path: Residential GC" confirmation and a direct link to the first module in their sequence.

---

## Email 2 — Day 3: Module Deep-Dive (Safety Planning)

**Timing**: 3 days after subscribe  
**Trigger**: Time delay after Email 1  
**Subject line** (Residential GC variant): The most-cited Cal/OSHA violation in residential construction  
**Subject line** (Industrial GC variant): Why the first thing every industrial GC needs is a written safety program  
**Subject line** (Generic / Specialty Sub variant): One document that protects you from the most common Cal/OSHA citation  
**Preview text**: And it's not the one you'd guess.  
**Sender name**: [Your name] | Construction Career Training  
**Length**: 250-350 words

---

### Residential GC Variant — Day 3 Email

**Subject**: The most-cited Cal/OSHA violation in residential construction

Hi [First Name],

If Cal/OSHA showed up on your job site tomorrow, here's the first thing they'd ask for:

Your Injury and Illness Prevention Program (IIPP).

This is not the paperwork most contractors think of first. It's a written safety program — every California employer is required to have one under Title 8 §3203, with no size exemption. One-person LLC with a single hire? You need an IIPP.

It's also the violation Cal/OSHA finds most often.

**What's actually in an IIPP** (from Module 14 of the curriculum):

The program requires eight documented elements: responsibility (who is accountable by name), compliance procedures, hazard communication, periodic inspection records, accident investigation procedures, a correction timeline for identified hazards, training documentation, and recordkeeping going back at least one year.

A working IIPP for a small residential GC runs 15-40 pages. It has to reflect your sites, your hazards, your people — a generic template downloaded from the internet is a flag, not a shield.

**One update you may not have caught**: Effective July 1, 2025, California reduced the residential fall-protection trigger height from 15 feet down to 6 feet. If your toolbox talks or site safety orientation still reference the old height, they are out of date and you are exposed.

Module 14 walks through all eight IIPP elements, the Focus Four fatality causes, heat illness, silica, and the 2025 fall-protection change in detail.

[Read Module 14: Site Safety and Cal/OSHA Compliance →] [LINK]

[Your name]

---

### Industrial GC Variant — Day 3 Email

**Subject**: Why the first thing every industrial GC needs is a written safety program

Hi [First Name],

Industrial construction has a compounding safety problem that commercial work doesn't: you're often on a live, operating site.

That means tie-ins under outage windows, hot work permits, LOTO (Lockout/Tagout), confined-space programs, SIMOPS (Simultaneous Operations) management. None of these exist on a greenfield commercial build.

On an industrial site, every GC must have a written safety program that satisfies both federal OSHA 1910.119 (Process Safety Management) and Cal/OSHA Title 8. The two frameworks overlap but do not duplicate — you need a program that covers both.

Module 14 of the curriculum covers the Injury and Illness Prevention Program (IIPP) requirements for California contractors, the Focus Four fatality causes, and the 2025 fall-protection changes. For the industrial context, the module connects IIPP requirements to the additional compliance layer of process safety management on operating sites.

The fundamentals hold regardless of project type: document your program, train your people, investigate incidents and near-misses, keep records for three years minimum.

[Read Module 14: Site Safety and Cal/OSHA Compliance →] [LINK]

If you're specifically in industrial/process work, also bookmark Module 36 (Safety Program Design for Construction Companies), which covers process safety, audit procedures, and how to build a safety program that survives third-party owner audits.

[Your name]

---

### Generic / Specialty Sub Variant — Day 3 Email

**Subject**: One document that protects you from the most common Cal/OSHA citation

Hi [First Name],

The most common Cal/OSHA violation across all construction types — residential, commercial, industrial — is the same one:

No written Injury and Illness Prevention Program (IIPP).

Every California employer is required to have one under Title 8 §3203. No size exemption. A specialty sub with three people on a job site needs an IIPP just as much as a GC with 50.

What the program requires, what Cal/OSHA actually looks for during an inspection, how to write one that holds up (not a downloaded template), and the 2025 update to California fall-protection heights — all of this is in Module 14 of the curriculum.

[Read Module 14: Site Safety and Cal/OSHA Compliance →] [LINK]

Once you're familiar with the IIPP requirements, the next module to read for your specific path: [Use path tag to personalize — residential tag → link to Module 7; industrial tag → link to Module 32; specialty sub tag → link to Module 13].

[Your name]

---

## Email 3 — Day 7: Case Study Teaser

**Timing**: 7 days after subscribe  
**Trigger**: Time delay after Email 2  
**Subject line**: Quick scenario — what would you do?  
**Preview text**: Happens in the first 90 days of every new GC's first project.  
**Sender name**: [Your name] | Construction Career Training  
**Length**: 200-300 words  
**Goal**: Drive first case study workbook visit; test engagement before sending further content

---

**Subject**: Quick scenario — what would you do?

Hi [First Name],

Here's a situation from the case study workbook. This one happens in the first 90 days of most new GCs' first projects:

---

**Scenario**: You are the GC on a residential remodel. Your drywall sub finishes their scope and hands you a signed lien waiver. Three weeks later, they file a mechanics lien against the property — claiming you never paid them.

You have the cancelled check. You have the signed waiver.

**What do you do next, and what should you have done differently?**

---

Take 60 seconds and think through it before clicking the answer.

[See the full answer in the Case Study Workbook →] [LINK → case-study-workbook.md on your site, anchor to the relevant scenario]

This scenario tests three things: your understanding of lien waiver types (conditional vs. unconditional), your record-keeping practices, and whether your subcontract required lien releases before final payment.

The answer is in the workbook, along with 150+ other scenarios across all three paths.

One more thing — are you following the LinkedIn page yet? I post module excerpts and case study questions three times a week. [LinkedIn link] — worth a follow if you want the between-email updates.

[Your name]

---

**P.S.** If you haven't started your first module yet, the best entry point for your path is:
- Residential GC: Module 7 → Residential GC Scope and Project Management [LINK]
- Industrial GC: Module 1 → Contracts and Estimating for the Industrial GC [LINK]
- Specialty Sub: Module 13 → Construction Law and Lien Rights [LINK]

---

## Automation Rule Classification

**This sequence is**: The "path-routing welcome rule"  
**This is automation #**: 1 of 1 on the Kit free plan  
**Do not use the free plan's automation slot for anything else until this sequence is confirmed working**

**What this automation does**:
1. Entry: New subscriber joins any of the 4 forms
2. Action: Apply path-specific tag if not already applied by form
3. Action: Enroll subscriber in the correct path variant of this 3-email sequence
4. Wait: 3 days → send Email 2 (Day 3 module deep-dive)
5. Wait: 4 additional days → send Email 3 (Day 7 case study)

**If branching is available in the free plan**: Build one automation with conditional branches routing to path-specific email variants (see Email 2 variants above).

**If branching is NOT available**: Build separate Sequences per path (one Sequence per path = 4 Sequences). Enrollment happens automatically at form subscribe because each form is linked to the correct Sequence. The automation slot is then available for a re-engagement rule (inactive-30d → re-engagement email).

---

## Copy Refinement Notes

The following elements should be customized before going live:

1. **[Your name]**: Replace with actual sender name consistently throughout
2. **[LINK] placeholders**: Replace with actual URLs from your deployed GitHub Pages site before loading into Kit
3. **LinkedIn link**: Add actual LinkedIn profile or page URL in Email 3
4. **Sender email**: Ensure the reply-to address in Kit Settings matches the tone of these emails (first-person, accessible)
5. **Subject line A/B testing**: Kit allows 2-variant A/B subject line testing on broadcasts (not automations). Once you have 100+ subscribers, test Email 1 subject line: "You're in. Here's where to start." vs. "Your construction curriculum is ready." Compare open rates.
6. **Plain text vs. designed**: These emails are written as plain text. Do not add heavy design elements (banners, images, columns). Construction professionals respond to direct, clean communication. The "Powered by Kit" badge appears in the footer regardless — keep the body minimal.

---

## Sources

- Module 14 content: `/projects/career-training/14-site-safety-osha-california.md`
- Module 1 content: `/projects/career-training/01-foundations-contracts-estimating.md`
- Email funnel strategy: `/projects/career-training/EMAIL_SOCIAL_FUNNEL_STRATEGY.md`
- Residential path structure: `/projects/career-training/docs/navigation/residential-path.md`
- Industrial path structure: `/projects/career-training/docs/navigation/industrial-path.md`
- Phase 2-3 roadmap: `/projects/career-training/PHASE_2_3_EXECUTION_ROADMAP.md`
- [Cal/OSHA IIPP Requirements — DIR §3203](https://www.dir.ca.gov/title8/3203.html)
- [California Fall Protection Height Change July 2025 — CalChamber](https://calchamberalert.com/2025/05/09/residential-construction-fall-protection-trigger-height-drops-to-6-feet/)
