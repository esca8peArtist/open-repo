---
title: "June 5–15 Phase 5 Publication and Wave 2 Recruitment Timeline"
project: systems-resilience
phase: 5
wave: 2
purpose: "Day-by-day execution roadmap covering Phase 5 Wave 1 publication (June 5–8) and Wave 2 author recruitment and sprint kickoff (June 5–15). Works identically for both platform options. Platform-specific steps clearly marked."
status: READY-FOR-USE — activate June 5 morning
created: 2026-06-04
platform_variants: "VARIANT A = Nextcloud+Matrix | VARIANT B = Discourse"
cross_references:
  - PHASE_5_PUBLICATION_READINESS_CHECKLIST.md
  - WAVE_2_AUTHOR_ONBOARDING_KIT_DUAL_PLATFORM.md
  - PHASE_5_NEXTCLOUD_MATRIX_DEPLOYMENT_ROADMAP.md
  - PHASE_5_DISCOURSE_DEPLOYMENT_ROADMAP.md
  - PHASE_5_WAVE_1_2_INTEGRATED_CORPUS.md
---

# June 5–15: Phase 5 Publication and Wave 2 Recruitment Timeline
## Systems Resilience Project — Execution Roadmap

**This document assumes the platform decision was made by EOD June 3 per BLOCKED.md.** All steps are written for both platforms simultaneously. When you see **[A]** or **[B]**, apply only the variant matching your chosen platform.

**Critical path summary**: Publication GO decision by June 5 noon → content live June 5–8 → author invitations June 5–6 → confirmations June 7–8 → platform onboarding June 8–9 → sprint kickoff June 10.

---

## Pre-Execution State (Verified as of June 4 EOD)

Before June 5 morning, confirm these are true. If any are false, the day-by-day plan below has contingency entries.

| Item | Expected State | Confirm |
|------|---------------|---------|
| Platform decision made | Option A (Discourse) OR Option B (Nextcloud+Matrix) chosen | [ ] |
| 5 Wave 1 domains committed to master | `phase-3/01–05` all present and production-ready | [ ] |
| Platform deployed (or deploying June 5) | Deployment roadmap followed per PHASE_5_NEXTCLOUD_MATRIX_DEPLOYMENT_ROADMAP.md or PHASE_5_DISCOURSE_DEPLOYMENT_ROADMAP.md | [ ] |
| Author candidate list drafted | 15 candidates across 5 domains (3 per domain) identified | [ ] |
| Email access functional | Outgoing email working from project address | [ ] |

---

## June 5 (Wednesday) — Publication Decision Day + Author Invitation Launch

### Morning Block (06:00–12:00 UTC)

**Priority 1: Run the Publication Readiness Checklist**

Open `PHASE_5_PUBLICATION_READINESS_CHECKLIST.md` and work through all six sections. This takes approximately 90 minutes if everything is clean (expected). Log the results in the decision grid at the bottom of that document.

Specific steps:
1. Verify all 5 domain files present (`wc -w projects/systems-resilience/phase-3/*.md`)
2. Confirm cross-domain links are not broken (5-minute manual check of the 5 cross-reference pairs)
3. Strip YAML frontmatter from publication copies and stage in `/tmp/phase3-pub/`
4. Confirm no images in any domain file (`grep -r "!\[" projects/systems-resilience/phase-3/`)
5. Run spell check on all 5 files
6. Test-validate 20% of citation URLs (30 URLs across 5 domains — aim for 6 per domain)

**Decision by 12:00 UTC**: GO, HOLD, or DEFER.

- If GO: proceed to afternoon publication block
- If HOLD (minor fixes): fix issues in the late morning, shift publication to 14:00–18:00 UTC window
- If DEFER: activate GitHub Pages fallback (see Contingency section below); continue with author invitations regardless of publication status

**Platform-specific check (run concurrently with readiness checklist)**:

[A — Nextcloud+Matrix]: Confirm the Nextcloud instance is accessible at its Tailscale URL (e.g., `https://100.70.184.84/nextcloud`). Log in as admin. Confirm the `Phase5-Wave1` folder structure is ready to receive uploaded content. Confirm Matrix room `#phase5-discussion:resilience-hub` exists and you are joined.

[B — Discourse]: Confirm the Discourse instance is accessible at its domain. Log in as admin. Confirm the "Phase 5 Wave 1 — Published Research" category has been created with appropriate permissions (public read, registered write, or public read-only — depending on access model). Confirm the API key is available for automated topic creation if you are using the seeding script from PHASE_5_DISCOURSE_DEPLOYMENT_ROADMAP.md.

### Afternoon Block (12:00–18:00 UTC)

**Priority 2: Publish Wave 1 Content**

If GO decision confirmed, publish the five domains to the chosen platform.

**[A — Nextcloud+Matrix]** Publication steps:

1. Upload the 5 frontmatter-stripped markdown files from `/tmp/phase3-pub/` to the `Phase5-Wave1-Published` folder in Nextcloud (drag-and-drop in browser or via WebDAV client)
2. Set folder sharing: "Share with link" — read-only link for public access (or restricted to registered users, depending on access model)
3. Copy the public link URL for use in the announcement email
4. Pin the folder link in the Matrix room `#phase5-discussion:resilience-hub` with a message: "Phase 5 Wave 1 is published. Five community-scale research domains available at [LINK]. Read, comment, and share."
5. Verify: open the Nextcloud link in an anonymous browser tab and confirm all 5 files are accessible

**[B — Discourse]** Publication steps:

1. In the "Phase 5 Wave 1 — Published Research" category, create one topic per domain. Use the domain title as the topic title. Paste the frontmatter-stripped markdown as the topic body.
2. Post domains in this order (so the category index shows them cleanly):
   - `05-scaling-pathways-and-thresholds.md` (post first — it will appear last in reverse-chron)
   - `04-security-and-defense.md`
   - `03-information-infrastructure.md`
   - `02-food-systems-supply-chain.md`
   - `01-governance-decision-making.md` (post last — it will appear first)
3. Pin the governance topic as a category announcement
4. Create an announcement topic: "Phase 5 Wave 1 Published — Five Community-Scale Research Domains" with a brief intro and links to all 5 topics
5. Verify: log out of Discourse, visit the category URL, confirm all 5 topics visible and readable

**Priority 3: Send Author Invitations (run concurrently with publication if resources allow)**

While publication is happening (or immediately after if solo), send Wave 2 author invitations using Template 1 from `WAVE_2_AUTHOR_ONBOARDING_KIT_DUAL_PLATFORM.md`.

Send to the top 15 candidates (3 per domain, 5 domains). Personalize each email with the candidate's name, their relevant expertise, and their specific domain assignment. Sending 15 emails takes approximately 45 minutes with templates ready.

**Author candidate list** (fill in before sending):

| Domain | Candidate 1 | Candidate 2 | Candidate 3 |
|--------|------------|------------|------------|
| Food Preservation & Storage | | | |
| Water Systems Management | | | |
| Livestock & Pasture Management | | | |
| Seed Saving & Plant Propagation | | | |
| Equipment Repair & Maintenance | | | |

(See `PHASE_5_WAVE_2_AUTHOR_PROFILES.md` for candidate sourcing guidance per domain.)

### Evening Block (18:00–22:00 UTC)

**Post-publication verification** (30 minutes):

- [ ] All 5 domain pages load correctly in an anonymous browser tab
- [ ] Platform search returns relevant results for "governance" and "food systems"
- [ ] Tables render correctly in at least 2 domains (spot-check governance and food systems — they have the most tables)
- [ ] At least 1 announcement email sent to founding coalition (see announcement template in WAVE_2_AUTHOR_ONBOARDING_KIT)

**Invitation tracking** (10 minutes):

- [ ] Log all 15 sent invitations in a tracking spreadsheet (Name, Domain, Email, Sent Date, Response, Status)
- [ ] Set calendar reminder for June 7 to follow up with non-responders

---

## June 6 (Thursday) — Invitation Follow-Through + Any Publication Holds Resolved

### If HOLD from June 5:

Complete the fix items from the HOLD log. Publish before noon. Then proceed with author invitation launch (same steps as June 5 afternoon, run June 6 morning).

### Standard activities (all scenarios):

**Morning (06:00–12:00 UTC)**:
- Check invitation responses received overnight (any early acceptances get Template 2 — Briefing Document — sent immediately, do not wait until the full cohort is assembled)
- Send the founding coalition announcement email if not sent June 5 evening

**Coalition announcement email** (send to the distribution list from resistance-research coalition or direct contacts):

---

Subject: Phase 5 Wave 1 Published — Five Community-Scale Resilience Research Domains

The Systems Resilience Project has published Phase 5 Wave 1: five community-scale research domains covering governance, food systems, information infrastructure, security and defense, and scaling pathways for Midwest Zone 5 communities.

Combined: approximately 29,000 words with 170 citations. Written for practitioners — community organizers, households, and local governance bodies — not academic specialists.

Available at: [PLATFORM URL]

Phase 5 Wave 2 research begins June 10. If you have expertise in food preservation, water systems, livestock management, seed saving, or equipment repair and are interested in contributing, reply to this email by June 8.

[YOUR NAME / PROJECT LEAD]

---

**Afternoon (12:00–18:00 UTC)**:
- Finalize Wave 2 candidate list if not complete (source additional candidates from resistance-research coalition contacts, NAFCM directory, FIC network — see author profiles document for sourcing channels by domain)
- For any same-day acceptances: send Template 2 (Briefing) + Template 4 (Platform Orientation — correct variant) + platform account invitation

---

## June 7–8 (Friday–Saturday) — Confirmations and Onboarding Package Dispatch

### June 7

**Morning**:
- Review all responses to June 5–6 invitations
- Conduct screening calls with interested candidates (20–30 minutes each). Target: complete all calls by June 8 noon.
- If fewer than 8 candidates have responded (yes or no): send follow-up to non-responders

Follow-up email (send June 7 if no response to June 5 invitation):

---

Subject: Re: Invitation: Systems Resilience Phase 5 Wave 2

[FIRST NAME], following up on my note from June 5. We are finalizing Wave 2 contributors by June 8 and I wanted to make sure this reached you. If you are interested or have questions, a quick reply is all I need — no commitment required at this stage.

[YOUR NAME]

---

**Afternoon**:
- Conduct remaining screening calls
- For confirmed authors: send full onboarding package (Template 2 + Template 4 + platform account invitation)
- Begin peer review pairing plan (match authors by domain complementarity where possible — e.g., food preservation paired with seed saving; water systems paired with equipment repair; livestock standalone or paired with food preservation)

### June 8 (Saturday)

**All confirmations due by end of day.**

By June 8 end of day, you should know:
- Exactly how many Wave 2 authors are confirmed (target: 4–6 for the core domains)
- Which domains are covered and which need fallback (self-execution by orchestrator if no author confirmed)
- Peer review pairings finalized

**Author status decision grid**:

| Authors confirmed | Decision |
|------------------|----------|
| 5–6 (all or nearly all domains covered) | Proceed to full Wave 2 sprint, June 10 kickoff |
| 3–4 (majority of domains covered) | Proceed for covered domains; self-execute remaining 1–2 domains (orchestrator) |
| 1–2 (minority of domains covered) | Self-execute all uncovered domains; use confirmed authors for highest-priority domains |
| 0 confirmed | Self-execute Wave 2 entirely (orchestrator); skip Wave 2 author coordination; focus orchestrator on July 10 publication date |

**Platform account status**:
- [ ] All confirmed authors have received platform account invitations
- [ ] At least 24 hours of lead time before June 9 training session

---

## June 9 (Sunday) — Onboarding and Training

### Morning (09:00–12:00 UTC)

**Optional async training session**:

If all or most confirmed authors can attend a 30-minute live session: schedule via email, host via Zoom or Jitsi (no platform dependency — a video call outside the project platform). Record the session for those who cannot attend.

If synchronous coordination is not feasible: record a 20-minute walkthrough video covering the platform orientation and upload it to:

[A — Nextcloud+Matrix]: Upload recording to Nextcloud shared folder `Wave2-Onboarding-Resources`. Post the link in the Matrix room `#wave2-general`.

[B — Discourse]: Create a pinned topic "Wave 2 Onboarding — Platform Walkthrough (Video)" in the Wave 2 private category. Embed the video link.

**Training session content** (regardless of live or async delivery):
1. Platform access confirmed (everyone can log in — 5 minutes)
2. Domain scope document walkthrough — what the sprint is asking for (10 minutes)
3. First-draft checkpoint protocol review — dates, format, escalation (5 minutes)
4. Live Q&A or async Q&A thread if recorded (remaining time)

### Afternoon (12:00–18:00 UTC)

**Finalize domain assignments and peer review pairings**:

Announce pairings to all confirmed authors:

[A — Nextcloud+Matrix]: Post pairings in Matrix room `#wave2-general` as a pinned message.

[B — Discourse]: Post pairings in a new topic "Wave 2 — Domain Assignments and Peer Review Pairings" in the Wave 2 private category. Pin the topic.

**Upload domain scope documents and annotated bibliographies** to each author's workspace:

[A — Nextcloud+Matrix]: Add scope file (`00-SCOPE.md`) and bibliography (`00-SOURCES.md`) to each author's dedicated folder (`Phase5-Wave2-[Domain]/`). Notify via Matrix direct message.

[B — Discourse]: Create a topic "[[Domain Name]] — Scope and Bibliography" in the Wave 2 private category, visible only to the assigned author and the project lead. Post scope and bibliography content as topic body.

---

## June 10 (Monday) — Sprint Kickoff (T+0)

**By 12:00 UTC, all Wave 2 authors receive**:
- [ ] Domain scope document (full outline, section structure, depth expectations)
- [ ] Annotated bibliography (25–40 sources, green/amber/red light quality rating)
- [ ] Zone 5 context briefing (embedded in scope document or separate if needed)
- [ ] Peer review partner name and contact
- [ ] Reminder of first-draft checkpoint date (June 17, T+7)

**Project lead posts a sprint kickoff note** to all authors (via their platform workspace):

---

Wave 2 sprint is officially open. T+0 today. Your first-draft checkpoint is June 17 (T+7). Between now and then: read your scope document, skim your annotated bibliography, and start your section outline. If anything in the scope document is unclear or seems too broad/narrow, message me today or tomorrow — week 1 is the easiest time to adjust scope.

First checkpoint (T+7): send a 50% draft — section outline complete, first two sections narrative-complete, citations roughed in.

Good luck.

---

**What the project lead does June 10 while authors begin research**:
- Begin tracking author sprint status in a simple table (name, domain, last check-in date, status)
- Monitor platform workspace for any same-day questions (respond within 4 hours on Day 1)
- Log June 5–10 publication and recruitment results in WORKLOG.md

---

## June 11–15 (Tuesday–Saturday) — Wave 2 Active Research + Publication Metrics

### Daily routine (15–30 minutes per day)

Each day, June 11–15:
1. Check author workspaces for any new questions or status updates
2. Respond to any messages within 24 hours (target: same business day)
3. Note any author who has gone completely silent (no activity in workspace for 48+ hours) — this is an early warning signal, not yet an escalation trigger
4. Scan Wave 1 publication metrics (see below)

### Wave 1 Publication Metrics Tracking

By June 15, Wave 1 will have been live for 7–10 days. Capture baseline metrics to inform Wave 2 scope and publication strategy.

**[A — Nextcloud+Matrix]**: Check Nextcloud file access logs (if enabled in admin panel) for download counts per domain. Check Matrix room for any messages, questions, or reactions from non-Wave 2 members.

**[B — Discourse]**: Check Discourse topic view counts, reply counts, and likes for each of the 5 published topics. Note: which domain generated the most discussion? Which had the most views?

**What metrics tell you about Wave 2 scope**:

| Metric signal | Implication |
|---------------|-------------|
| Governance domain has most views | Community interest highest in decision-making — Wave 2 should produce a strong governance-adjacent document (conflict resolution or water systems governance) early |
| Food systems has most replies/discussion | Readers want deeper food content — food preservation as Wave 2 priority |
| Zero discussion on all 5 domains | Announcement may not have reached the right audience; re-send to broader list; assess whether Wave 2 publication June 15–20 timing needs adjustment |
| Strong engagement on information infrastructure | Information systems expertise may be harder to recruit — check author pipeline for that domain |

**Engagement is informational only** — it does not change the Wave 2 sprint timeline. Wave 2 authors began work June 10 regardless of Wave 1 metrics. Metrics inform post-publication messaging, not in-flight research.

### Contingency Monitoring (June 11–15)

**Author silence protocol**:

If an author has no activity in their workspace for 5 days (by June 15 = 5 days after T+0):
1. Send a direct message or email: "Checking in — how is the sprint going? Anything blocking you?"
2. If no response within 2 days: phone call or escalation email
3. If confirmed drop-out: activate scope reduction OR project lead self-execution for that domain (decide based on domain priority)

**Platform instability protocol**:

If the chosen platform becomes inaccessible for more than 4 hours during the active sprint (June 11–15):

[A — Nextcloud+Matrix]: Check raspby1 server health (`docker ps` on 100.70.184.84). If Docker container is down, restart (`docker compose up -d` in Nextcloud stack directory). If Tailscale connection is the issue, troubleshoot Tailscale client on raspby1. Fallback: share files via GitHub repo (public or private) while Nextcloud is restored.

[B — Discourse]: Check VPS health (SSH to Hetzner/Digital Ocean instance). If Discourse service is down, restart (`./launcher restart app` in `/var/discourse/`). Fallback: coordinate via email direct messages while Discourse is restored.

**If platform is unstable for more than 24 hours**: move coordination temporarily to email. Send all authors a note: "Platform is temporarily down — send draft updates and questions to [email] until restored." This is a degraded-mode fallback, not a platform migration.

---

## Platform-Specific Branching Summary

The table below summarizes every step that differs between the two platforms. The rest of the timeline above is identical.

| Step | [A] Nextcloud+Matrix | [B] Discourse |
|------|---------------------|---------------|
| June 5: Confirm platform access | SSH to raspby1, verify Nextcloud at Tailscale URL, verify Matrix room exists | SSH to VPS, verify Discourse at domain, verify category exists |
| June 5: Publish Wave 1 domains | Upload stripped .md files to Nextcloud shared folder; pin link in Matrix room | Create one Discourse topic per domain; pin governance topic as category announcement |
| June 7–8: Send platform invitations | Nextcloud user invite + Matrix room join link | Discourse account invitation email |
| June 9: Upload scope documents | Add to Nextcloud folders per author | Create private Discourse topics per author |
| June 9: Post peer review pairings | Pinned message in Matrix `#wave2-general` | Pinned Discourse topic in Wave 2 category |
| June 10: Author day-1 notification | Matrix direct message | Discourse direct message |
| June 11–15: Monitor engagement | Nextcloud file access logs + Matrix room activity | Discourse topic views + reply counts |
| Recovery if platform down | Docker restart on raspby1; fallback to GitHub repo | Discourse launcher restart on VPS; fallback to email |

---

## Contingency Triggers and Response Actions

### Trigger 1: Platform Deployment Takes Longer Than Expected

**Condition**: June 5 morning — platform not fully deployed or inaccessible when readiness checklist is run.

**Response**:
1. Do not delay author invitations — send Template 1 (invitations) using email regardless of platform status
2. Publish Wave 1 domains to GitHub Pages as immediate fallback (documented in `PHASE_5_GITHUB_PAGES_STAGING.md` — this was staged June 1 and is ready to deploy)
3. Continue platform deployment in parallel; migrate content to chosen platform when deployment completes (can happen June 6–8 without disrupting Wave 2 sprint)
4. Note in announcement email: "Content is currently accessible at [GitHub Pages URL]. We are migrating to a dedicated platform this week — this link will remain active throughout."

**Decision authority**: If platform deployment cannot complete by June 8, confirm GitHub Pages as the permanent publication location for Wave 1. This does not affect Wave 2 — Wave 2 author coordination can happen entirely via email + shared Google Drive or equivalent until platform is stable.

### Trigger 2: Author Recruitment Slow (Fewer Than 8 Acceptances by June 9)

**Condition**: By end of June 8, fewer than 8 of 15 candidates have accepted (regardless of whether they have confirmed or just expressed interest).

**Response**:
1. June 9 morning: contact the secondary list (prior collaborators, resistance-research coalition contacts, one-degree referrals from confirmed Wave 2 authors). Target: 5 additional contacts.
2. Send abbreviated invitation (Template 1 with a note: "We are filling spots quickly for a June 10 start — interest confirmed by June 9 evening gets priority")
3. Do not delay sprint kickoff for latecomers — confirmed authors begin June 10 regardless
4. If a secondary-list author confirms June 10–11: onboard them one day late (send scope document June 10, they begin June 11 at T+1)

**Minimum viable cohort**: 3 confirmed authors covering 3 of 5 domains. The project lead self-executes the remaining 2 domains on the same June 10–July 10 timeline.

### Trigger 3: Wave 1 Publication Engagement Very Low (Zero Discussions by June 12)

**Condition**: By June 12 (7 days after publication), zero comments, replies, or engagement on any of the 5 published domains.

**Response**:
1. Audit the announcement: was the founding coalition email actually sent? Did it reach the intended list? (Check sent folder, confirm no bounce-back)
2. If announcement was sent but no engagement: expand distribution. Send a personal note to 5–10 specific contacts from the resistance-research coalition who are most likely to engage with the governance or food systems domains.
3. If announcement was not sent: send it immediately and track engagement over the following 5 days
4. Do not adjust Wave 2 scope or timeline based on engagement data this early — 7 days is too short for organic discovery

**Zero engagement does not mean low quality**. Research documents distributed to specialized practitioner audiences often have a 2–4 week lag before first engagement. The engagement data at June 12 is an early signal, not a verdict.

### Trigger 4: Author Goes Silent Mid-Sprint

**Condition**: An author has no workspace activity and no response to check-in messages for 7+ days during the sprint (June 10–July 10).

**Response** (already detailed in WAVE_2_AUTHOR_ONBOARDING_KIT, repeated here for the timeline):
1. Direct email + phone (if available): "We are at the [T+X] checkpoint. Your draft was due [DATE]. Can you give me a status update today?"
2. If no response within 48 hours: treat as drop-out. Activate scope reduction for that domain (reduce from 4,000–6,000 words to 2,500–3,500 words, which is completable by the project lead in 3–4 hours). OR reassign to a Wave 2 author who has completed their primary domain ahead of schedule.
3. Update peer review pairing accordingly (the dropped author's peer reviewer is now unpartnered — reassign to project lead for their peer review).

**No-guilt escalation**: The onboarding materials set the expectation that early notice is critical. A drop-out that gives 5+ days notice is manageable; one that gives 0 notice blocks the peer review chain. The escalation script is firm but non-adversarial.

---

## Status Grid: End of June 15

By June 15 (10 days into the plan), expect this status:

| Item | Target State |
|------|-------------|
| Wave 1 publication | All 5 domains live on chosen platform, announcement sent |
| Wave 2 authors confirmed | 4–6 authors across 4–5 domains |
| Sprint status | T+5 (authors 5 days into 30-day sprint; first checkpoint in 2 days) |
| Engagement tracking | Baseline metrics captured (views, downloads, or discussion count per domain) |
| Contingencies triggered | 0–1 (expected — minor platform adjustment or one slow-response author) |
| Next milestone | June 17 (T+7): first-draft checkpoints due from all Wave 2 authors |

If the actual state on June 15 diverges significantly from the above, the next document to consult is `PHASE_5_WAVE_2_DECISION_FRAMEWORK.md` — it covers scope adjustment and sequencing decisions for the July phase of the sprint.
