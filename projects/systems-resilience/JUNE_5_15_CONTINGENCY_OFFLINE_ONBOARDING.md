---
title: "June 5–15 Contingency: Offline Onboarding Plan"
project: systems-resilience
phase: 5
wave: 2
purpose: "Backup onboarding plan for two distinct scenarios: (1) platform setup delays past June 5 and authors cannot access the collaboration platform when the sprint starts June 10; (2) one or more authors has limited/intermittent internet access and cannot reliably use the primary platform. Also covers timeline slip provisions: how many days can platform setup slip before Wave 2 launch is impacted?"
status: READY-FOR-USE — activate if platform is not accessible by June 9 EOD, OR for any author indicating limited internet in intake form
created: 2026-06-04
version: 1.0
activation_triggers:
  - "Platform not accessible to at least one confirmed author by June 9 18:00 UTC"
  - "Author intake form shows 'limited or intermittent' internet access"
  - "Platform instability lasting 24+ hours during June 10–15 sprint window"
cross_references:
  - WAVE_2_GENERIC_ONBOARDING_TEMPLATE.md
  - AUTHOR_READINESS_INTAKE_FORM.md
  - WAVE_2_AUTHOR_ONBOARDING_KIT_DUAL_PLATFORM.md
  - JUNE_5_15_PHASE_5_PUBLICATION_AND_WAVE_2_RECRUITMENT_TIMELINE.md
  - PHASE_5_GITHUB_PAGES_STAGING.md
---

# June 5–15 Contingency: Offline Onboarding Plan
## Systems Resilience Phase 5 | Activate If Platform Setup Delays or Author Access Fails

---

## When to Activate This Plan

**Scenario 1 — Platform deployment delay:**
Platform (Nextcloud+Matrix or Discourse) is not accessible to authors by June 9 18:00 UTC. This means authors cannot log in and see their workspace on June 10 sprint start.

**Scenario 2 — Author access failure:**
Platform is deployed and functional, but one or more confirmed authors cannot access it reliably — account setup failed, invitation email bounced, or author has limited internet access.

**Scenario 3 — Mid-sprint platform instability:**
Platform was accessible on June 10 but goes down for 24+ hours during the June 10–15 sprint window (e.g., server failure, Tailscale connectivity issue, VPS outage).

**Do not activate this plan preemptively.** Activate only when one of the above triggers is confirmed. Until then, proceed with the primary onboarding workflow in WAVE_2_GENERIC_ONBOARDING_TEMPLATE.md.

**Resource contention note:** June 5–7 and June 9–11 are reduced-availability windows for the orchestrator (seedwarden Day 1–3 post-launch monitoring and stockbot Week 1 JPM+AMZN trading, respectively). If a platform deployment emergency happens on June 9, the orchestrator's available bandwidth to diagnose and recover is compressed. The offline onboarding plan is specifically designed to be deployable in 30–60 minutes without requiring deep platform debugging during those windows.

---

## Part 1: Offline Workflow — Google Drive Folder Structure

This is the immediate fallback when the primary platform is unavailable. It requires only that authors have a Google account (or can receive files via email).

### Folder Structure

Create the following Google Drive folder structure under a project Google account (or a shared organizational Drive):

```
Systems-Resilience-Phase5-Wave2/
├── 00-SHARED-RESOURCES/
│   ├── Zone-5-Context-Briefing.md
│   ├── Wave-1-2-Corpus-Link.txt        (link to GitHub Pages or published platform)
│   └── Style-Guide.md
├── Wave2-FoodPreservation/
│   ├── 00-SCOPE.md
│   ├── 00-SOURCES.md
│   ├── DRAFT-food-preservation.gdoc    (Google Doc — main working draft)
│   └── PEER-REVIEW.gdoc               (Google Doc — peer review notes)
├── Wave2-WaterSystems/
│   ├── 00-SCOPE.md
│   ├── 00-SOURCES.md
│   ├── DRAFT-water-systems.gdoc
│   └── PEER-REVIEW.gdoc
├── Wave2-LivestockManagement/
│   ├── 00-SCOPE.md
│   ├── 00-SOURCES.md
│   ├── DRAFT-livestock-management.gdoc
│   └── PEER-REVIEW.gdoc
├── Wave2-SeedSaving/
│   ├── 00-SCOPE.md
│   ├── 00-SOURCES.md
│   ├── DRAFT-seed-saving.gdoc
│   └── PEER-REVIEW.gdoc
└── Wave2-EquipmentRepair/
    ├── 00-SCOPE.md
    ├── 00-SOURCES.md
    ├── DRAFT-equipment-repair.gdoc
    └── PEER-REVIEW.gdoc
```

**Setup time:** approximately 30 minutes (create folder structure, upload scope .md files, create Google Docs with section headings, set sharing permissions).

**Sharing permissions:** Each domain subfolder is shared with the relevant author ("Editor" access) and the project lead ("Editor" access). The `00-SHARED-RESOURCES/` folder is shared with all confirmed authors ("Viewer" access).

### Google Drive Editing Workflow

For each author working in Google Drive fallback mode:

**Draft editing:**
- Author opens their `DRAFT-[domain].gdoc` file in Google Docs
- Google Docs supports full offline editing (download the Google Docs app; enable "Make available offline" for the file)
- Author tracks changes using "Suggesting" mode if they want the project lead to see revisions clearly; "Editing" mode is fine for original drafting
- Draft is not Markdown — it is a Google Doc. For final publication, the project lead converts to Markdown before platform upload (see Part 4, Conversion Protocol)

**Status updates:**
- Author posts status updates as a comment in the Google Doc (Insert → Comment) with `@project-lead` tag — project lead receives email notification
- Alternative: send status update by email directly

**Checkpoint submissions:**
- At T+7 (June 17), author adds a comment at the top of the document: "T+7 CHECKPOINT — 50% draft. Sections 1–2 complete. Main uncertainty: [topic]."
- At T+14 (June 24), author sends email: "T+14 FULL DRAFT submitted. [Google Doc link]. Ready for peer review."

**Peer review:**
- Peer reviewer opens `PEER-REVIEW.gdoc` in the author's folder
- Posts structured feedback (strong point, structural issue, citation to verify) as the body of the doc
- Author comments back on specific items if needed

---

## Part 2: Communication Protocol — Discord/Slack Standby and Email Escalation

When the primary platform (Matrix or Discourse) is unavailable, communication falls back in this order:

### Tier 1 — Email (Always Available)

Email is the baseline. All critical coordination (checkpoint confirmations, scope changes, emergency questions) defaults to email if other channels are unavailable.

**Project lead email:** [PROJECT LEAD EMAIL]

**Author email protocol:**
- Subject line convention: `Wave2 [DOMAIN] — [T+N] [TOPIC]` (e.g., "Wave2 WaterSystems — T+7 checkpoint question")
- Response time: 24 hours maximum; 4 hours during normal orchestrator availability windows
- Reduced availability windows (expect 24-hour response, not same-day): June 5–7 (seedwarden Day 1–3) and June 9–11 (stockbot Week 1)

**When to use email for a question vs. waiting for a platform-based response:**
- Use email immediately: blocking question (cannot proceed without an answer), missed checkpoint, drop-out notice, scope emergency
- Use platform workspace or wait: non-blocking questions, status updates, general check-ins

---

### Tier 2 — Discord Standby (If Assembled)

If four or more Wave 2 authors confirm by June 8, the project lead may create a Discord server as a secondary communication layer. Discord is used as a standby for real-time coordination when Matrix or Discourse is unavailable — not as a replacement for the platform workspace.

**Discord setup (project lead action, only if needed):**
1. Create a free Discord server: "Systems-Resilience-Wave2"
2. Create channels:
   - `#general` — cross-domain coordination
   - `#food-preservation`, `#water-systems`, `#livestock-management`, `#seed-saving`, `#equipment-repair` — per-domain channels
   - `#platform-status` — announcements about platform availability
3. Invite all confirmed Wave 2 authors (link sent by email)
4. Post in `#platform-status` when the primary platform is down and when it is restored

**Discord is informal and supplemental.** It does not replace the structured checkpoint protocol. Authors post questions and get quick answers; they do not post draft content in Discord. The working draft stays in Google Drive (or primary platform when it is restored).

**Discord standby protocol when primary platform is down:**
- Project lead posts in `#platform-status`: "[Platform] is down as of [TIME]. Using Google Drive and email for the duration. ETA for restoration: [TIME or TBD]. No sprint work is blocked — continue drafting."
- Authors continue drafting without interruption
- Questions go to Discord or email
- When platform is restored: project lead posts in `#platform-status` and authors migrate any new draft content to the primary platform workspace

---

### Tier 3 — Slack Standby (Alternative to Discord)

If authors already use Slack in their professional contexts, a Slack workspace is an acceptable Discord substitute. Setup is equivalent. Choose one (Discord or Slack) — do not operate both.

**Preference signal:** If the author intake forms (Section 3.2) indicate a majority of authors prefer Slack over Discord, use Slack. Otherwise, Discord is the simpler option for a temporary standby channel.

---

### Weekly Check-in Protocol (Both Platforms and Offline Fallback)

Regardless of which platform is active, a weekly check-in rhythm runs June 10–July 10:

**Monday (start of sprint week): Project lead status note**

Post in each author's workspace (or email if platform is down):

```
Week [N] of Wave 2 sprint.
T+[current] — next checkpoint: T+[next] on [DATE].
If you have any blocking questions, post them by Wednesday for a same-day response.
```

**Mid-week (Wednesday): Author self-report (optional but encouraged)**

Authors with questions or concerns post or email by Wednesday. This gives the project lead time to respond before the weekend.

**End of week (Friday): Project lead scan**

Project lead reviews all active workspaces (or Google Docs if offline) for:
- Draft activity in the past 5 days (is work happening?)
- Any unanswered questions
- Any author with no activity at all (5-day silence → escalation trigger)

---

## Part 3: Timeline Slip Provisions

### How Many Days Can Platform Setup Slip?

Platform deployment is scheduled for June 6. Wave 2 sprint starts June 10. The buffer is 4 days.

| Platform slip scenario | Wave 2 sprint impact | Decision |
|----------------------|---------------------|----------|
| Platform ready by June 8 (2-day slip) | **None.** Authors receive scope documents and credentials June 8–9 as planned. Sprint starts June 10 on schedule. | Proceed as normal |
| Platform ready by June 9 AM (3-day slip) | **Minimal.** Authors receive access June 9 and have one day to confirm setup before sprint start. T+0 kickoff message may be June 10 afternoon UTC instead of morning. | Notify authors: "Platform access confirmed today — you have time to set up before tomorrow's sprint start." |
| Platform ready June 10 (4-day slip — exactly at sprint start) | **Moderate.** Authors start drafting without a confirmed workspace. Activate this document immediately: distribute Google Drive folders, send scope documents by email, confirm communication via email. Sprint starts on schedule in offline mode; authors migrate to primary platform when it is available. | Activate Part 1 of this document. Email all authors June 10 morning: "Platform is finalizing setup — using Google Drive for Day 1. Platform access link will arrive today." |
| Platform ready June 11–12 (5–6 day slip) | **Manageable.** Sprint is 2 days old before the platform is available. All author work to that point is in Google Drive. Migration to primary platform is a one-time copy operation. T+7 checkpoint (June 17) is unaffected. | Continue offline in Part 1. When platform is ready, send each author a migration note (Part 4 below). No timeline adjustment. |
| Platform ready June 13–14 (7–8 day slip) | **Notable but manageable.** Sprint is nearly one week old in offline mode. T+7 checkpoint is June 17 — still 3–4 days away when platform comes up. Authors can migrate their in-progress drafts to the primary platform and submit T+7 checkpoint through the proper channel. | Continue offline through the first week. Announce platform availability and migration. Adjust author expectations: they have been working in a different environment and may need 30–60 minutes to orient to the primary platform. |
| Platform ready after June 14 (9+ day slip) | **Significant.** Sprint has been running in offline mode for most of the first week. T+7 checkpoint is imminent. Keep all authors in offline mode through the June 17 checkpoint; migrate after T+7. Evaluate whether to continue with primary platform or stay in Google Drive for the full sprint duration. | Decision point: if platform deployment is still pending June 14, evaluate whether the remaining sprint (June 14 – July 10) is better served by the primary platform or by staying fully in Google Drive. Make the decision explicit; do not leave authors in uncertainty. |
| Platform never deploys (full contingency) | **Full offline sprint.** Wave 2 completes entirely in Google Drive + email + Discord/Slack. Publication readiness converts Google Docs to Markdown for final publication. | Activate Part 4 immediately. This is the worst case but is fully executable. |

### The Non-Negotiable Anchor: June 17 First-Draft Checkpoint

Platform availability does not affect the June 17 T+7 first-draft checkpoint. Regardless of whether authors are working in the primary platform or Google Drive fallback, the following is required by June 17 EOD:

- All section headings present
- Sections 1 and 2 in full narrative prose
- Citations roughed in
- Main uncertainty note

The project lead can review a Google Doc just as easily as a Nextcloud file or a Discourse post. Platform uncertainty does not extend the first checkpoint deadline.

**The same logic applies to the T+14 full draft (June 24).** The platform is a delivery mechanism, not a prerequisite for writing. Authors can and should continue drafting in whatever environment they have access to, and submit through email if the platform is unavailable.

---

## Part 4: Migration Protocol (When Platform Comes Back Online)

When the primary platform becomes available after a period of offline operation, use this protocol to migrate author work without losing anything.

### Nextcloud+Matrix Migration

**Project lead actions:**

1. Confirm author's Nextcloud account and domain folder are ready (follow access provisioning checklist from WAVE_2_AUTHOR_ONBOARDING_KIT_DUAL_PLATFORM.md Part 4)
2. For each author, notify: "Nextcloud is ready. Here is your login link and temporary password. Your folder contains 00-SCOPE.md and 00-SOURCES.md. Please upload your current Google Doc draft as [domain-name]-draft-v[N].md — convert to Markdown first (see instructions below), or paste as plain text and format later."
3. Send the author a Nextcloud desktop sync client link if they want offline editing going forward

**Author actions:**

1. Log into Nextcloud and verify the domain folder
2. Export current Google Doc draft: File → Download → Plain Text (.txt) OR use Google Docs "Copy as Markdown" extension if available
3. Clean up the exported file: remove Google Docs footnote artifacts; add YAML frontmatter; verify heading hierarchy
4. Upload to Nextcloud as `DRAFT-[domain-name].md`
5. Post in Matrix domain room: "Migrated from Google Drive — draft v[N] uploaded. [Word count] words, T+[N] into sprint."

**Time required for migration:** 30–45 minutes per author.

### Discourse Migration

**Project lead actions:**

1. Confirm author's Discourse account and Draft Thread topic are ready
2. For each author, post in their Draft Thread: "Platform is now available. Please paste your current draft into a reply here, formatted as Markdown. Subject line: [T+N MIGRATION — draft content]. This will be your working version going forward."

**Author actions:**

1. Log into Discourse and locate Draft Thread
2. Export current Google Doc: File → Download → Plain Text
3. Clean up: remove artifacts; convert section headings to Markdown (`##` for H2, `###` for H3); verify formatting
4. Post in Draft Thread with `[T+N MIGRATION]` in the opening line
5. Note word count and sprint date in the post

**Time required:** 20–30 minutes per author (Discourse editing is simpler than file upload).

---

## Part 5: Async Feedback Loops Without Platform

When all communication is via email and Google Drive, structured feedback loops require explicit scheduling because there is no persistent thread to read.

### Checkpoint Feedback Loop (Offline Mode)

**T+7 (June 17) — Offline Mode:**

1. Author sends email to [PROJECT LEAD EMAIL]:
   - Subject: `Wave2 [DOMAIN] — T+7 Checkpoint`
   - Body: word count, sections complete, main uncertainty, link to Google Doc draft
2. Project lead reviews Google Doc within 2 days
3. Project lead replies with checkpoint response: direction confirmation or 1-paragraph redirect note
4. Author acknowledges receipt by email reply within 24 hours

**T+14 (June 24) — Offline Mode:**

1. Author sends email to [PROJECT LEAD EMAIL]:
   - Subject: `Wave2 [DOMAIN] — T+14 Full Draft`
   - Body: word count, citation count, peer reviewer name, link to Google Doc draft
2. Author simultaneously sends email to peer reviewer with link to their Google Doc draft:
   - Subject: `Wave2 peer review request — [DOMAIN]`
   - Body: "Full draft ready for peer review. Link: [Google Doc link]. Structured feedback needed by June 27 (T+17). Format: (1) one strong point, (2) one structural issue, (3) one citation to verify."
3. Peer reviewer adds comments to the Google Doc or replies by email with structured feedback by June 27
4. Author acknowledges peer review receipt by June 27 EOD

---

## Part 6: Offline-First Author Protocol

For authors whose intake form indicates "limited or intermittent" internet access, this subsection provides an offline-first workflow that does not depend on any network connectivity for drafting.

### Offline Drafting Setup

**The only requirement for drafting is a text editor.** No internet is required to write.

1. Download scope document and annotated bibliography to local device before connectivity is unavailable (download once when connected; work offline indefinitely)
2. Write in any local text editor: Notepad++, VSCode, Typora, iA Writer, Obsidian, or even plain Notepad. Save as a .txt or .md file locally.
3. When connectivity is restored, upload draft to Google Drive (or primary platform) and email a status update

**Offline-first recommended tools:**
- Obsidian (Markdown editor, works offline, built-in link support, available free for desktop)
- Typora (clean Markdown editor, small install, no cloud dependency)
- VSCode (free, multiplatform, excellent Markdown preview)
- Any text editor the author already uses — format does not matter at the drafting stage

**Citation checking while offline:** Log all citation URLs in the annotated bibliography during connected sessions. Mark which ones you need to verify. Batch-verify when connectivity is available. Do not let citation verification block drafting — roughed-in citations ("per green-rated USDA source on water quality standards") are acceptable until the T+14 verification pass.

### Connectivity Check-In Schedule

Authors with limited connectivity should establish a predictable check-in schedule and communicate it to the project lead before June 10:

**Proposed format:**
"I am able to be online reliably: [days / times / frequency]. During offline periods, I am drafting locally. I will upload new content and check messages at each online window."

This predictability allows the project lead to time questions and feedback to coincide with the author's connectivity windows, preventing 48-hour response gaps that might otherwise trigger the escalation protocol.

**Minimum connectivity requirement for Wave 2:** At least two connected sessions per week of at least 30 minutes each (to upload drafts, check feedback, verify citations). Authors who cannot meet this minimum should flag it immediately — scope reduction or self-execution for that domain may be necessary.

---

## Quick-Reference: Offline Activation Checklist

When Scenario 1, 2, or 3 (see top of document) triggers, run this checklist:

**Within 2 hours of trigger:**
- [ ] Confirm trigger is real (platform is genuinely unavailable, not a temporary blip)
- [ ] Create Google Drive folder structure (Part 1)
- [ ] Upload scope documents and annotated bibliographies to each author's folder
- [ ] Create Google Doc drafts with section headings pre-populated
- [ ] Set sharing permissions (author = Editor, project lead = Editor, other authors = no access)

**Within 4 hours of trigger:**
- [ ] Email all confirmed Wave 2 authors: "Platform update: we are using Google Drive temporarily for Wave 2 work. [Instructions for accessing the folder]. Sprint timeline is unchanged. Email [PROJECT LEAD EMAIL] with any questions."
- [ ] If Discord/Slack standby is active: post in `#platform-status`
- [ ] Log the trigger event in WORKLOG.md with timestamp and expected resolution timeline

**Within 24 hours of trigger:**
- [ ] Confirm every author has acknowledged the fallback notification
- [ ] Confirm every author can access their Google Drive folder
- [ ] Proceed with sprint on offline workflow

**When primary platform is restored:**
- [ ] Run migration protocol (Part 4) for all authors
- [ ] Email all authors: "Platform is restored. Here is your access link. Please migrate your current draft by [date] and confirm in your workspace."
- [ ] Log restoration in WORKLOG.md

---

## Resource Contention During Activation Windows

Two periods in June 5–15 have reduced orchestrator availability:

**June 5–7 (seedwarden Day 1–3 post-launch monitoring):** If a platform failure triggers this plan during June 5–7, the Google Drive fallback can be activated with approximately 30–60 minutes of setup time. The project lead's bandwidth for real-time platform debugging is limited during this window. Prioritize: get authors into Google Drive quickly rather than spending hours diagnosing the platform failure. Platform debugging can happen in parallel without blocking the sprint.

**June 9–11 (stockbot Week 1 — JPM+AMZN trading):** This is the highest-risk window for a platform deployment gap (platform deploys June 6–8; June 9 is publication day; June 10 is sprint start). If the platform is not ready June 9–10, the sprint starts in offline mode with no disruption. The project lead communicates once via email on June 10 morning and checks back on June 11 after the stockbot peak trading window closes.

**For both windows:** Authors receive a single clear message about the fallback, then work independently. The next project lead check-in is 24 hours later (not same-day). This is by design — the offline workflow is self-contained so authors are not blocked by reduced orchestrator availability.

---

*Version 1.0 — Contingency offline onboarding plan, pre-staged June 4 for immediate deployment if needed*
*Activation triggers: platform delay past June 9, author access failure, mid-sprint platform instability*
*Does not replace primary onboarding workflow — supplement only*
*Sprint start June 10, 2026 | Non-negotiable checkpoint anchor: June 17 T+7 first draft*
