---
title: "Wave 2 Author Onboarding Template — Platform-Independent"
project: systems-resilience
phase: 5
wave: 2
purpose: "Universal onboarding template for Wave 2 authors. Works identically for Nextcloud+Matrix (Option A) and Discourse (Option B). [PLATFORM-SPECIFIC] markers indicate branching sections. Fill in [PLATFORM NAME], [PLATFORM URL], [DATE], and [DOMAIN] fields before sending to authors."
status: READY-FOR-USE — deploy June 5 after platform decision at 13:00 UTC
created: 2026-06-04
version: 1.0
platform_variants: "VARIANT A = Nextcloud+Matrix | VARIANT B = Discourse"
cross_references:
  - WAVE_2_AUTHOR_ONBOARDING_KIT_DUAL_PLATFORM.md
  - PHASE_5_PUBLICATION_READINESS_CHECKLIST.md
  - JUNE_5_15_PHASE_5_PUBLICATION_AND_WAVE_2_RECRUITMENT_TIMELINE.md
  - AUTHOR_READINESS_INTAKE_FORM.md
  - JUNE_5_15_CONTINGENCY_OFFLINE_ONBOARDING.md
deployment_note: "After June 5 13:00 UTC platform decision — replace all [PLATFORM-SPECIFIC] markers with the chosen platform's instructions. Sections without [PLATFORM-SPECIFIC] markers require no editing."
---

# Wave 2 Author Onboarding Template
## Systems Resilience Phase 5 — June 10 – July 10, 2026

---

## How to Use This Template

**For the project lead deploying this template on June 5:**

1. Confirm the platform decision (13:00 UTC June 4 or 5 — Nextcloud+Matrix or Discourse)
2. Search this document for every instance of `[PLATFORM-SPECIFIC]` and replace the relevant branch with the chosen platform's content
3. Fill in the six universal placeholders: `[PLATFORM NAME]`, `[PLATFORM URL]`, `[PROJECT LEAD EMAIL]`, `[DOMAIN NAME]`, `[PEER REVIEWER NAME]`, `[DATE]`
4. Remove the platform branch you are not using (clean up the "Option A / Option B" blocks)
5. Send the completed document to each confirmed Wave 2 author on June 7–8, alongside the Author Briefing Document (Template 2 from WAVE_2_AUTHOR_ONBOARDING_KIT_DUAL_PLATFORM.md)

**Read time for authors:** approximately 20 minutes. The document is designed to be actionable on first read — every section ends with a checklist the author can tick off immediately.

**Resource contention note:** The June 5–15 window overlaps with stockbot Week 1 (JPM+AMZN trading, peak monitoring demand June 9–11) and seedwarden Day 1–3 post-launch monitoring (June 5–7). Orchestrator availability is reduced June 5–7 and June 9–11. Author questions during those windows will receive responses within 24 hours, not same-day. Plan accordingly if you need project lead input during those dates.

---

## Section 1: Credential Verification (Universal)

Before you begin any research or drafting work, your credentials are verified by the project lead. This is a one-time process that happens during the screening call (June 7–8). You do not need to take any action — the project lead completes this step.

**What was verified during your screening call:**

- Your subject matter expertise in [DOMAIN NAME] is directly relevant to the Wave 2 scope
- You have produced at least one 4,000+ word practitioner-oriented document (writing sample reviewed)
- You can commit 4–6 hours per week from June 10 to July 10 (30-day sprint)
- You are comfortable with async collaboration — written feedback, no synchronous meeting requirements
- You have reliable email and internet access for the sprint duration

**Your credential tier** (assigned by project lead; determines which onboarding steps you need):

| Tier | Profile | Onboarding path |
|------|---------|----------------|
| Tier A: Experienced practitioner-researcher | 5+ years in domain; has published practitioner guides; familiar with markdown or willing to learn in under an hour | Skip Sections 2b and 3b; proceed directly to first draft with light project lead contact |
| Tier B: Domain expert, new to this project | Strong domain expertise; limited long-form publication history; may need editorial scaffolding | Complete all sections; receive one additional project lead check-in at T+3 (June 13) |
| Tier C: Emerging contributor | Solid domain knowledge; first major long-form research project; may benefit from extended scope guidance | Complete all sections; receive scope narrowing consultation on June 10; first draft target adjusted to 2,500–3,500 words |

Your tier: **[TIER — filled in by project lead based on intake form and screening call]**

**Self-verification items** (confirm these are true before June 10):

- [ ] You have accepted the platform account invitation (see Section 3)
- [ ] You have reviewed the Author Readiness Intake Form and returned it to the project lead
- [ ] You have confirmed your IP and attribution agreement (CC-BY 4.0, byline on publication, editorial authority retained by project lead)
- [ ] You have confirmed your compensation terms and payment schedule

---

## Section 2: Platform Overview

### 2a — What the Platform Is (Universal)

The project uses a single collaborative platform for all Wave 2 work. The platform serves three functions:

1. **Workspace:** Where your draft documents live. You write, revise, and submit through the platform.
2. **Communication:** Where you ask questions, post status updates, and coordinate with your peer reviewer.
3. **Archive:** Where scope documents, annotated bibliographies, and the Wave 1+2 corpus are accessible.

Both platform options (Nextcloud+Matrix and Discourse) are functionally equivalent for Wave 2 authors. The editing experience differs slightly (desktop sync vs. browser-based posting), but the workflow — receive scope, draft, checkpoint, peer review, revise, submit — is identical.

### 2b — Platform-Specific Overview [PLATFORM-SPECIFIC]

---

**[PLATFORM-SPECIFIC: Nextcloud+Matrix — Option A]**

**Nextcloud** is a self-hosted file sync and collaboration server. Think of it as a shared Google Drive running on project infrastructure (Tailscale-networked Raspberry Pi at 100.70.184.84). Your documents are files in a shared folder.

**Matrix** is an encrypted messaging protocol. The project uses it for async communication — think of it as a low-friction chat system. You get a project-specific Matrix room for your domain and access to the general Wave 2 coordination room.

**How they work together:** You write in Nextcloud; you communicate in Matrix. Nextcloud is the document layer; Matrix is the conversation layer.

**Key characteristics:**
- Documents are standard Markdown (.md) files — editable in any text editor, in-browser, or via the Nextcloud desktop sync client
- Matrix is persistent and threaded — messages stay; no need to repeat context
- Offline work is supported via the desktop sync client
- The platform runs on project infrastructure — there is no monthly fee, no third-party service dependency, and no data leaves the project network

---

**[PLATFORM-SPECIFIC: Discourse — Option B]**

**Discourse** is an open-source forum platform. Your Wave 2 workspace lives in a private category. Documents are written as topic posts; feedback arrives as replies.

**Key characteristics:**
- Documents are written in Discourse's built-in editor (Markdown supported; real-time preview available)
- Every reply is timestamped and versioned — you can see the evolution of a draft through the reply chain
- The platform is browser-based — no client software to install
- Trust Level 1 (your starting level) supports all Wave 2 functions: posting, replying, and direct messages

---

**[END PLATFORM-SPECIFIC SECTION 2b]**

---

## Section 3: Setup and Access Provisioning

### 3a — What You Will Receive (Universal)

Before June 9, the project lead will send you:

1. A platform account invitation (email with link to accept)
2. Your domain scope document (full outline, depth expectations, research questions)
3. Your annotated bibliography (25–40 pre-vetted sources, green/amber/red quality rating)
4. The name and platform contact for your peer reviewer
5. A link to the Wave 1+2 published corpus at [PLATFORM URL]

All of this arrives in one batch by June 9, timed to the June 10 sprint start. If you have not received your invitation by June 8 18:00 UTC, email [PROJECT LEAD EMAIL] directly.

### 3b — Platform-Specific Setup Steps [PLATFORM-SPECIFIC]

---

**[PLATFORM-SPECIFIC: Nextcloud+Matrix — Option A]**

**Step 1 — Accept the Nextcloud invitation** (10 minutes, complete by June 9)

You will receive an email from the Nextcloud server with a link to create your account. Click the link, set a password, and log in. Your username will follow the format `firstname.domaincode` (e.g., `sarah.fp` for food preservation).

After logging in, you should see:
- `Phase5-Wave2-[YourDomain]/` — your working folder
- `Phase5-Wave2-Shared-Resources/` — zone 5 context briefing and Wave 1+2 corpus link

If either folder is missing, email [PROJECT LEAD EMAIL] immediately.

**Step 2 — Verify your workspace files** (5 minutes)

Open your domain folder. Confirm these four files are present:
- `00-SCOPE.md` — your domain assignment and section outline
- `00-SOURCES.md` — your annotated bibliography
- `DRAFT-[domain-name].md` — your working draft (section headings pre-populated, body blank — you fill it in)
- `PEER-REVIEW.md` — where your peer reviewer will post structured feedback

**Step 3 — Test the editor** (5 minutes)

Click `DRAFT-[domain-name].md`. It opens in Nextcloud Text (in-browser editor). Add a test line ("Test — June [DATE]"), verify it saves (auto-save, no button required), then delete it. This confirms your editing permissions are active.

**Optional: Install the Nextcloud desktop sync client** (30 minutes, only if you prefer offline editing)

Download from nextcloud.com/install. Log in with your server address (https://100.70.184.84/nextcloud), username, and password. Your domain folder will sync to a local directory. Edit locally; sync when online. This is recommended for authors who prefer a local text editor over the browser editor.

**Step 4 — Join your Matrix rooms** (10 minutes, complete by June 10)

You will receive a Matrix room invitation link by email or from the project lead directly. Accept it using any Matrix-compatible client:
- Web: app.element.io (no install required)
- Mobile: Element X (iOS/Android, recommended for offline notifications)

Your rooms:
- `#wave2-[your-domain]:resilience-hub` — your primary communication channel
- `#wave2-general:resilience-hub` — cross-author coordination

Post a short hello in your domain room by June 10 morning. This confirms your access is live.

**Setup quick-reference checklist (Nextcloud+Matrix):**
- [ ] Nextcloud invitation accepted; account created
- [ ] Domain folder visible with all four files present
- [ ] Editor test completed (test line added and deleted successfully)
- [ ] Matrix joined for both rooms
- [ ] Hello posted in domain room by June 10

---

**[PLATFORM-SPECIFIC: Discourse — Option B]**

**Step 1 — Accept the Discourse invitation** (10 minutes, complete by June 9)

You will receive an email invitation from the Discourse platform. Click the link and create your account. Your Discourse username will be confirmed in the invitation email.

After logging in, navigate to the Wave 2 private category (visible only to members of the `wave-2-contributors` group — if you can see it, your permissions are correctly set).

**Step 2 — Locate your workspace topics** (5 minutes)

Inside the "Phase 5 Wave 2 — Working Drafts" category, find:
- "[DOMAIN NAME] — Scope and Bibliography" — your domain assignment and source list (read this first)
- "[DOMAIN NAME] — Draft Thread" — where you post draft content and receive peer review feedback

If either topic is missing or not visible, send a Discourse direct message to @project-lead or email [PROJECT LEAD EMAIL].

**Step 3 — Confirm posting permissions** (5 minutes)

In your Draft Thread topic, post a one-line reply: "Access confirmed — [Your Name], [DATE]." This tests your posting permissions and serves as your T+0 check-in. If the post fails (permission error), notify the project lead immediately.

**Step 4 — Configure notifications** (5 minutes, required)

In your Draft Thread topic, click the bell icon (notification settings, bottom of topic) → select "Watching." This ensures you receive an email whenever the project lead or your peer reviewer posts a reply. Without this setting, you will miss feedback on your draft.

**Setup quick-reference checklist (Discourse):**
- [ ] Discourse invitation accepted; account created
- [ ] Wave 2 private category visible
- [ ] Both workspace topics (Scope + Draft Thread) accessible
- [ ] Confirmation post in Draft Thread ("Access confirmed — [Name], [Date]")
- [ ] Draft Thread set to "Watching" for email notifications

---

**[END PLATFORM-SPECIFIC SECTION 3b]**

---

## Section 4: First-Sync Protocol

### 4a — Before June 10 (Universal)

Complete these steps before the sprint starts on June 10:

- [ ] Read your scope document fully (00-SCOPE.md / Scope topic)
- [ ] Skim your annotated bibliography (00-SOURCES.md / Scope topic body) — identify 5–8 sources you will use heavily
- [ ] Read the Wave 1+2 published corpus at [PLATFORM URL] — focus on the document closest to your domain
- [ ] Identify one specific point where your domain depends on a governance or coordination structure described in Wave 1 (bring this observation to your June 10 kickoff message)
- [ ] Confirm your peer reviewer's name and contact handle (project lead will introduce you before June 10)
- [ ] Return your completed Author Readiness Intake Form if you have not already

### 4b — June 10 First Contact [PLATFORM-SPECIFIC]

---

**[PLATFORM-SPECIFIC: Nextcloud+Matrix — Option A]**

On June 10, post in your Matrix domain room:

```
T+0 kickoff — [Your Name], [DOMAIN NAME]
Scope read: yes
Annotated bibliography: skimmed — will rely heavily on [3 source titles]
Wave 1 connection: [One sentence noting where your domain depends on Wave 1 governance structure]
Ready to begin outlining Section 1.
```

This is your official sprint start confirmation. The project lead will acknowledge within 4 hours on June 10 (note: orchestrator monitoring is compressed June 9–11 due to stockbot week 1 overlap — target response is 4 hours, not immediate).

---

**[PLATFORM-SPECIFIC: Discourse — Option B]**

On June 10, post in your Draft Thread:

```
T+0 kickoff
Name: [Your Name]
Domain: [DOMAIN NAME]
Scope read: yes
Annotated bibliography: skimmed — will rely heavily on [3 source titles]
Wave 1 connection: [One sentence noting where your domain depends on Wave 1 governance structure]
Plan: begin section outline today.
```

Use the standard checkpoint format for this and all future status posts (it helps the project lead scan multiple threads efficiently).

---

**[END PLATFORM-SPECIFIC SECTION 4b]**

---

## Section 5: Editing and Feedback Workflow (Universal)

### Sprint Timeline

| T+ | Date | Milestone | What is due |
|----|------|-----------|------------|
| T+0 | June 10 | Sprint kickoff | Kickoff message + scope read confirmation |
| T+3 | June 13 | Optional check-in | Status note in workspace if you have questions or scope concerns |
| T+7 | June 17 | First-draft checkpoint | 50% draft: all headings present; Sections 1 and 2 narrative-complete; citations roughed in |
| T+14 | June 24 | Full draft | 4,000–6,000 words; all sections complete; citations verified and working |
| T+14–17 | June 24–27 | Peer review | Receive peer review on your draft; give peer review on your partner's draft |
| T+21 | July 1 | Revisions due | Address peer review feedback; final citation verification; grammar pass |
| T+25 | July 5 | Final review | Project lead copy edit and final check |
| T+30 | July 10 | Production-ready | Document cleared for publication |

### What Counts as a 50% Draft (T+7, June 17)

The June 17 checkpoint determines whether the sprint is on track. A 50% draft meets all three of these criteria:

1. **All section headings and subsection headings are present.** The structure of the document is complete — it looks like a full outline with every H2 and H3 marked. You can see at a glance where every major topic will go.

2. **Sections 1 and 2 have full narrative text.** Not bullet points, not notes, not "will expand here" — actual prose sentences that a reader could read and learn from. Aim for 1,200–1,800 words across the two sections.

3. **Citations are roughed in for cited sections.** You do not need to verify URLs yet, but the sources should be indicated. A rough citation can be as simple as "(SOURCE: [Author] — from annotated bibliography)" or "[CITE: irrigation spacing study from green-rated source]." This tells the project lead you are engaging with the source material.

A note on the one thing you are most uncertain about is also expected — this is the most useful single line for the project lead's checkpoint response. Something like "I am uncertain whether the community-scale water governance section should engage with the conflict resolution framework from Wave 1 or treat water governance as a standalone topic" is exactly the kind of question that a two-paragraph redirect can resolve.

### Citation Standards

All citations in Wave 2 documents must meet these standards:

- **Working URLs as of submission:** Every hyperlinked citation must load as of your submission date. Broken URLs discovered at the T+14 (full draft) stage are your responsibility to fix.
- **25–40 total citations per document:** Below 20 is thin. Above 50 suggests over-citation (paraphrase more; cite the primary source, not every secondary source that mentions it).
- **Quality tier matters:** Your annotated bibliography uses green/amber/red ratings. Rely primarily on green-rated sources. Amber sources can be used with appropriate hedging ("as described in practitioner literature, though rigorous trials are limited"). Red-rated sources should be used only for context, never as the primary evidence base for a claim.
- **Practitioner audience:** Avoid academic citation formats. Use inline links: "The USDA's recommendations for community canning safety (link) suggest...". Reserve footnote-style citations for documents where inline links break the reading flow.

### Peer Review Protocol

Your peer reviewer is a fellow Wave 2 author. The peer review exchange happens June 24–27 (T+14 to T+17). The format is structured and brief — three items only:

1. **One thing that is genuinely strong.** Identify a section, argument, or practical guide that works well and explain specifically why.
2. **One structural problem, if present.** If a section is in the wrong place, missing, or substantially underdeveloped, name it. If the structure is sound, say so.
3. **One citation or fact that needs verification.** Pick one specific claim and verify the cited source actually supports it. If it does, say so. If it does not, flag it with the correct source if you can find one.

Do not write general feedback ("I enjoyed reading this," "this could use more detail"). Structured, specific feedback is what the protocol requires. If you have more to say, use the "Other notes" field — but the three structured items are mandatory.

**Peer review is reciprocal:** You review your partner's draft on the same timeline they review yours. Both reviews due by June 27. If your partner submits late, you still review what is available and note in your review that you are working from a partial draft.

### How to Request Help

For questions to the project lead:

- Routine questions (scope clarification, source quality, formatting): use your platform workspace (Matrix domain room or Discourse Draft Thread). Response within 24 hours.
- Blocking questions (cannot proceed without an answer): tag @project-lead in your platform workspace AND send an email to [PROJECT LEAD EMAIL]. Note the June 9–11 and June 5–7 windows when orchestrator availability is reduced due to stockbot and seedwarden overlap — during those periods, target response is 24 hours, not same-day.
- Emergency scope change (discovered a major gap or overlap with another domain): email [PROJECT LEAD EMAIL] directly with "Wave 2 scope — urgent" in the subject line.

**The escalation protocol is firm but non-adversarial.** If you fall more than 3 days behind at any checkpoint, notify the project lead immediately. Early notice allows scope adjustment (reducing target word count, reassigning a subtopic). Silent gaps of 5+ days block the peer review chain. Honest communication early is always the better option.

---

## Section 6: Publication Checklist (Universal)

Before your document enters the project lead's final review (T+25, July 5), run this checklist yourself. The project lead will also run it, but you are expected to catch these before submission.

### Content Completeness

- [ ] Document is 4,000–6,000 words (not counting frontmatter or references section; use `wc -w` or your editor's word count)
- [ ] All section headings and subsection headings from the approved scope are present
- [ ] Every section has narrative prose text — no sections contain only notes, bullets, or "TBD" markers
- [ ] At least one "decision guide" or numbered how-to section is present (a practitioner can follow it directly without additional instruction)
- [ ] The Wave 1 connection identified at T+0 is reflected somewhere in the document — your domain's governance or coordination dependencies are explicit

### Citation Quality

- [ ] Total citations: 25–40
- [ ] Every hyperlinked citation URL confirmed working as of submission date (spot-check every 5th one if time is short — catch systematic failures)
- [ ] No green-rated sources cited for contradictory claims (if a source says X, you cite it for X, not for Y)
- [ ] Academic sources written in inaccessible jargon have been paraphrased, not block-quoted

### Formatting

- [ ] Document opens with a single H1 (`# Title`) — not H2 or H3
- [ ] Section headings follow a logical hierarchy (H2 for major sections, H3 for subsections — no H4 under an H2 without an H3 in between)
- [ ] Tables render correctly (no orphan pipe characters; headers defined)
- [ ] Code blocks (if any) open and close with triple-backtick fences
- [ ] YAML frontmatter is present and filled in (title, domain, author, date, word count, status: production-draft)
- [ ] No `[fill]`, `[TODO]`, `[TBD]`, or `[PLACEHOLDER]` markers anywhere in the document

### Audience Fit

- [ ] Technical terms are defined when first introduced (no assumed specialist vocabulary)
- [ ] Document is readable by a Zone 5 Midwest farming practitioner without formal academic training
- [ ] Practical guidance sections use imperative sentences ("do this, then that") not passive voice ("it is recommended that...")
- [ ] Document does not exceed its scope — stays within the domain assigned; cross-domain dependencies are noted but not fully treated

### Quick Self-Assessment

Rate each of the following 1–5 before submitting (1 = needs work, 5 = strong):

- Structural coherence (does the document flow logically?): ___
- Practical utility (can a practitioner act on this?): ___
- Citation rigor (are claims supported?): ___
- Audience calibration (right level for a Zone 5 practitioner?): ___

If any rating is 1 or 2, revise before submitting to the project lead. A self-rating of 3 on structural coherence is acceptable only if you flag the weak sections in your submission note.

---

## Quick Reference Summary

**Five things to do before June 10:**

1. Accept platform invitation and confirm workspace access (see Section 3)
2. Read your scope document
3. Skim your annotated bibliography
4. Read the Wave 1+2 corpus at [PLATFORM URL] — especially the document closest to your domain
5. Identify your Wave 1 connection (one sentence on how your domain depends on Wave 1 governance structures)

**Five things to do by June 17 (T+7 checkpoint):**

1. Post your T+0 kickoff message
2. Complete your full document outline (all H2 and H3 headings)
3. Write Sections 1 and 2 in full narrative prose
4. Rough in citations for all cited sections
5. Post your checkpoint update with your main uncertainty

**Five things that will get your draft rejected at T+14:**

1. Word count under 3,500 (too short to be a complete document)
2. Broken citation URLs (your responsibility to verify before submitting)
3. Sections containing only notes or bullets, not prose
4. No practical how-to section (this is a practitioner document — it must have direct guidance)
5. Scope creep into another Wave 2 domain without prior coordination with the project lead

**Contact for help:**

Platform workspace (Matrix room or Discourse Draft Thread): for all routine questions. Response within 24 hours.

Email [PROJECT LEAD EMAIL]: for blocking questions or emergency scope changes. Flag subject line "Wave 2 scope — urgent."

Reduced availability windows (respond within 24 hours, not same-day): June 5–7 (seedwarden Day 1–3) and June 9–11 (stockbot Week 1 trading).

---

*Version 1.0 — Platform-independent onboarding template, pre-staged June 4 for June 5 deployment*
*Fill in [PLATFORM-SPECIFIC] sections after June 5 13:00 UTC platform decision*
*Sprint start June 10, 2026 | Publication target July 10, 2026*
