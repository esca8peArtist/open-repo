---
title: "June 5–15 Phase 5 Publication and Wave 2 Recruitment Timeline"
project: systems-resilience
phase: 5
wave: 2
purpose: "Day-by-day execution roadmap covering Phase 5 Wave 1+2 publication (June 5–9) and Wave 2 author recruitment and sprint kickoff (June 5–15). Works identically for both platform options. Platform-specific steps clearly marked."
status: READY-FOR-USE — activate June 5 morning at 08:00 UTC
created: 2026-06-04
version: 2.0
publication_day: 2026-06-09
wave_2_sprint_start: 2026-06-10
platform_variants: "VARIANT A = Nextcloud+Matrix | VARIANT B = Discourse"
cross_references:
  - PHASE_5_PUBLICATION_READINESS_CHECKLIST.md
  - WAVE_2_AUTHOR_ONBOARDING_KIT_DUAL_PLATFORM.md
  - PHASE_5_NEXTCLOUD_MATRIX_DEPLOYMENT_ROADMAP.md
  - PHASE_5_DISCOURSE_DEPLOYMENT_ROADMAP.md
  - PHASE_5_WAVE_1_2_INTEGRATED_CORPUS.md
  - PHASE_5_GITHUB_PAGES_STAGING.md
---

# June 5–15: Phase 5 Publication and Wave 2 Recruitment Timeline
## Systems Resilience Project — Execution Roadmap

---

## Executive Summary

**Three key points:**
1. The ten-day window June 5–15 accomplishes two parallel streams: (a) publishing the 45,000-word Phase 5 Wave 1+2 corpus on the chosen platform, and (b) recruiting, screening, credentialing, and onboarding Wave 2 authors so they are productive on June 10. Neither stream blocks the other — publication can slip to June 12 without affecting the Wave 2 sprint.
2. Every day in this roadmap has [PLATFORM-SPECIFIC] branches clearly marked. The platform decision made by EOD June 4 determines which branch to follow — all other steps are identical for both options.
3. Three named contingency branches are pre-scoped: (A) platform deployment delays push publication to June 12, Wave 2 unaffected; (B) slow recruitment shifts Wave 2 from 4 leads to 3 leads; (C) incomplete onboarding by June 14 shifts Wave 2 publication to June 25.

**Timeline:** June 5 verification + author invitations → June 6–7 platform deployment + screening calls → June 8 go/no-go + confirmations → June 9 publication day → June 10 Wave 2 sprint kickoff → June 15 onboarding complete

**Owner:** Orchestrator (project lead)

**Success criteria:** (a) Wave 1+2 publication live and monitored by June 9; (b) all Wave 2 authors onboarded by June 15; (c) Wave 2 authoring environment ready June 15 with zero blockers for the June 17 first-draft checkpoint.

---

## Pre-Execution State (Verify June 5 Morning Before Starting)

Before beginning the June 5 schedule, confirm these conditions are true. Each false condition has a named contingency entry below.

| Item | Expected State | Contingency if False |
|------|---------------|----------------------|
| Platform decision made | Option A (Nextcloud+Matrix) OR Option B (Discourse) chosen by user | N/A — user must decide before June 5 execution; if not decided by 09:00 UTC June 5, default to Discourse (faster deployment path) |
| Five Wave 1+2 source documents committed to master | All five phase-5-wave-2-*.md files present and confirmed PRODUCTION-READY status | Run PHASE_5_PUBLICATION_READINESS_CHECKLIST.md Section 1 immediately |
| Integrated corpus committed to master | PHASE_5_WAVE_1_2_INTEGRATED_CORPUS.md present | Check repo; document was produced June 1 and committed |
| Author candidate list drafted | 15 candidates across 5 domains (3 per domain) identified | Spend June 5 morning sourcing candidates from PHASE_5_WAVE_2_AUTHOR_PROFILES.md before sending invitations |
| Email access functional | Outgoing email working from project address | Test by sending a message to yourself before sending author invitations |

---

## June 5 (Wednesday) — Publication Readiness Verification + Author Invitation Launch

**Total orchestrator hours today:** 4–5 hours

### 08:00–12:00 UTC — Publication Readiness Verification (4 hours)

**Block 1: Run the Publication Readiness Checklist** (90 minutes)

Open `PHASE_5_PUBLICATION_READINESS_CHECKLIST.md` and work through Sections 1–4. This is the primary verification pass — the June 8 go/no-go will be a 30-minute re-check. Log all results in the decision log template in Section 5.

Critical steps in order:
1. Verify all five Wave 1+2 source documents present (`ls -la` check)
2. Run placeholder marker scan (`grep -rn` across all five files)
3. Check frontmatter `status` fields — standardize to "PRODUCTION-READY" if not already done
4. Run spell check on all five documents (aspell, 15 minutes)
5. Validate 20% of citation URLs (30–35 URLs total across five documents, 30 minutes)
6. Verify heading hierarchy in all five documents (5 minutes)

**[PLATFORM-SPECIFIC] — Run concurrently: platform pre-check**

[NEXTCLOUD+MATRIX ONLY]: SSH to raspby1 (100.70.184.84). Confirm Docker stack is running: `docker ps | grep nextcloud`. If Nextcloud is already deployed per the pre-deployment steps, navigate to `https://100.70.184.84/nextcloud` in a browser and confirm admin login works. If Nextcloud is not yet deployed: do not start deployment now — today's window is too short. Flag this for the June 6 deployment block.

[DISCOURSE ONLY]: SSH to the VPS. Confirm Discourse is running: `cd /var/discourse && sudo ./launcher status`. Navigate to the Discourse domain URL and confirm admin login works. If Discourse is not yet deployed: flag for June 6 deployment block.

**Block 2: Platform Decision Announcement** (30 minutes, run before noon)

Once you have confirmed the platform decision (or defaulted to Discourse if decision is outstanding), make the platform announcement. This is the operational starting gun for both deployment and author onboarding.

Send a brief note to any collaborators who need to know which platform was chosen. Update the frontmatter `platform_decision` field in this document:

```
Platform decision: [NEXTCLOUD+MATRIX / DISCOURSE]
Decision time: ___________
```

If the user is the sole operator: the "announcement" is simply noting the decision in your execution log and proceeding.

### 12:00–18:00 UTC — Author Invitation Launch (3 hours)

**Priority: Send Wave 2 invitations to top 15 candidates**

Using Template 1 from `WAVE_2_AUTHOR_ONBOARDING_KIT_DUAL_PLATFORM.md`:
- Personalize each email with candidate name, specific expertise, domain assignment, and the platform URL (if publication is live — otherwise link to the GitHub repo or note that the platform is deploying this week)
- Send to 3 candidates per domain (15 total)
- Log each invitation in a tracking table immediately after sending

**Author candidate tracking table** (create this spreadsheet or table today):

| Domain | Candidate | Email | Sent Date | Response | Status |
|--------|-----------|-------|-----------|----------|--------|
| Food Preservation | | | June 5 | | Pending |
| Food Preservation | | | June 5 | | Pending |
| Food Preservation | | | June 5 | | Pending |
| Water Systems | | | June 5 | | Pending |
| Water Systems | | | June 5 | | Pending |
| Water Systems | | | June 5 | | Pending |
| Livestock Mgmt | | | June 5 | | Pending |
| Livestock Mgmt | | | June 5 | | Pending |
| Livestock Mgmt | | | June 5 | | Pending |
| Seed Saving | | | June 5 | | Pending |
| Seed Saving | | | June 5 | | Pending |
| Seed Saving | | | June 5 | | Pending |
| Equipment Repair | | | June 5 | | Pending |
| Equipment Repair | | | June 5 | | Pending |
| Equipment Repair | | | June 5 | | Pending |

**Sending 15 personalized emails takes approximately 45–60 minutes with templates ready.** Do not skip personalization — the domain-specific expertise reference increases response rate significantly.

### 18:00–22:00 UTC — Evening Block (30–60 minutes)

- Check for any same-day invitation responses. If any candidate responds: send Template 2 (Briefing Document) and Template 4 (Platform Orientation) immediately — do not wait for the full cohort.
- Set a calendar reminder for June 7 morning to follow up with all non-responders.
- Log June 5 execution status in WORKLOG.md.

**Slip trigger for June 5:** If the publication readiness checklist (Sections 1–4) finds 3+ documents with content issues or a citation rate below 80%, activate **Contingency C** now: flag June 9 publication as at risk; begin scoping which issues can be resolved by June 8.

---

## June 6 (Thursday) — Platform Deployment + Publication Preparation

**Total orchestrator hours today:** 4–6 hours (primarily platform-specific)

### 06:00–14:00 UTC — Platform Deployment

[PLATFORM-SPECIFIC] — This block is primarily platform-specific. Follow the relevant playbook in detail.

[NEXTCLOUD+MATRIX ONLY]: Execute `PHASE_5_NEXTCLOUD_MATRIX_DEPLOYMENT_ROADMAP.md` Part 1–3 (Docker stack deploy, 6–8 hours from cold start). Key steps:
1. Verify raspby1 prerequisites met (Docker installed, Tailscale active, domain/IP confirmed)
2. Deploy Docker stack: `docker compose up -d` in the Nextcloud+Matrix stack directory
3. Complete initial Nextcloud configuration (admin setup, trusted domains, SMTP)
4. Deploy Matrix Synapse and verify bridge to Nextcloud notification stream
5. Create publication folder structure: `Phase5-Wave1-Published` and `Phase5-Wave2` placeholder
6. Test admin login and file upload with a test document

If deployment takes longer than 6 hours: activate **Contingency A** (see below). Publication slides from June 9 to June 12. Wave 2 timeline is unaffected.

[DISCOURSE ONLY]: Execute `PHASE_5_DISCOURSE_DEPLOYMENT_ROADMAP.md` Part 1–2 (VPS setup + Discourse install, 3–4 hours from cold start). Key steps:
1. Provision VPS (Hetzner CPX21 or equivalent; confirm IP and domain pointing)
2. Deploy Discourse via official Docker installer: `cd /var/discourse && sudo ./discourse-setup`
3. Complete Discourse admin setup (admin account, site settings, email delivery)
4. Create categories: "Phase 5 Wave 1 — Published Research" (public or community-visible), "Phase 5 Wave 2 — Working Drafts" (private, group-gated)
5. Create `wave-2-contributors` group with category access
6. Test admin login, topic creation, and invitation email delivery

If deployment takes longer than 4 hours: proceed anyway; publication is June 9 and there is buffer.

### 14:00–18:00 UTC — Publication Preparation (2 hours)

**Produce frontmatter-stripped copies of all five documents and the integrated corpus:**

Run the stripping command from `PHASE_5_PUBLICATION_READINESS_CHECKLIST.md` Section 2.3. Confirm six clean files appear in `/tmp/phase5-pub/`.

**Generate PDFs:**

Run the PDF export command from Section 3.1 of the readiness checklist. Spot-check two PDFs.

**Draft announcement email:**

Using Template 5 from `WAVE_2_AUTHOR_ONBOARDING_KIT_DUAL_PLATFORM.md`: draft the founding coalition announcement email. Leave the platform URL blank — fill it in on June 9 after publication is confirmed live.

### 18:00–22:00 UTC — Evening Block

- Check invitation responses from June 5 invitations. For any yes or interested response: send Template 2 + Template 4 + platform account invitation (platform access provisioning may be partial — explain that full access is ready June 7 and credentials will follow)
- Check deployment status: is the platform accessible? Is admin panel reachable?

---

## June 7 (Friday) — Author Screening + Platform Validation

**Total orchestrator hours today:** 3–4 hours

### 06:00–09:00 UTC — Follow-up and Screening Call Scheduling

**Send follow-up emails (Template 6) to all non-responders from June 5 invitations.**

Target: all 15 candidates have received at least two contact attempts by June 7 EOD.

For any candidates who have responded positively: schedule a 20–30 minute screening call today or June 8. The screening call should happen before you send the full briefing document and before you provision platform access. Sending the briefing document + credentials to an unscreened candidate wastes those assets — keep the access provisioning workflow sequential.

### 09:00–14:00 UTC — Screening Calls and Confirmations

**Conduct up to 5 screening calls today** (20–30 minutes each, maximum 2.5 hours of calls).

Follow the screening protocol in `WAVE_2_AUTHOR_ONBOARDING_KIT_DUAL_PLATFORM.md` Part 3:
- Confirm expertise alignment (ask the domain-specific screening question)
- Confirm availability (4–6 hours/week, June 10–July 10)
- Assess collaboration fit (async-capable, can give and receive written feedback)

For each confirmed author after the call:
1. Update the tracking table: Status → "Confirmed"
2. Send Template 2 (Briefing Document) + Template 4 (Platform Orientation, correct variant)
3. Begin access provisioning (Part 4 checklist in WAVE_2_AUTHOR_ONBOARDING_KIT_DUAL_PLATFORM.md)
4. Note the peer review pairing plan — start matching authors by domain complementarity

**Draft peer review pairings plan** (do this while you have 3+ confirmations in view):
- Food preservation + seed saving (complementary food production and preservation cycle)
- Water systems + equipment repair (infrastructure maintenance connection)
- Livestock management: pair with whichever of the above has capacity, or with project lead

### 14:00–18:00 UTC — Platform Validation

[NEXTCLOUD+MATRIX ONLY]: If deployment was completed June 6: validate the full Wave 2 workspace setup. Create the `Phase5-Wave2-[Domain]` folders for confirmed authors. Test file upload, file edit, and share link. Validate Matrix room creation.

[DISCOURSE ONLY]: If deployment was completed June 6: create the "Wave 2 — Scope and Bibliography" private topics for confirmed authors. Test account invitation delivery. Confirm the Wave 2 private category is correctly gated.

---

## June 8 (Saturday) — Go/No-Go + Final Confirmations

**Total orchestrator hours today:** 2–3 hours

### 08:00–14:00 UTC — Author Confirmation Deadline

**All author acceptance confirmations due by June 8 EOD.**

By noon June 8, check the tracking table and assess:
- How many confirmed authors? Which domains?
- Which domains have no confirmed author?
- Is the 3-author minimum viable cohort met?

For any candidates still in "interested but not confirmed" status: call them directly today if possible. An email follow-up is acceptable if calling is not feasible.

**Author confirmation decision** (apply the grid from WAVE_2_AUTHOR_ONBOARDING_KIT Part 7):
- 5–6 confirmed: full Wave 2 sprint, proceed as planned
- 3–4 confirmed: activate 3-lead fallback model (see Contingency B below); self-execute remaining domains
- 1–2 confirmed: reassess domain priorities; use confirmed authors for food preservation and water systems; self-execute the rest
- 0 confirmed: self-execute all five Wave 2 domains on July 10 timeline

### 14:00–18:00 UTC — Go/No-Go Publication Decision

Complete the final go/no-go check from `PHASE_5_PUBLICATION_READINESS_CHECKLIST.md` Section 5. This is a 30-minute re-check (not a full re-run of Sections 1–4 — those were done June 5).

**What to verify in 30 minutes:**
- [ ] All five documents still present in the repo (no accidental deletion)
- [ ] Frontmatter-stripped copies in `/tmp/phase5-pub/` are present and current
- [ ] PDFs generated
- [ ] Platform is accessible (admin login confirmed)
- [ ] Announcement email is drafted with platform URL filled in

**Go/No-Go call by June 8 18:00 UTC.** Document in the decision log:

```
June 8 Go/No-Go
Time: ___________
Checker: ___________
Platform deployed and accessible: YES / NO
Content verification (June 5 result): PASS / HOLD / DEFER
Assets ready: YES / PARTIAL
Author confirmations: _____ of target 5–6

Overall Decision: GO / HOLD / DEFER

If HOLD: Items outstanding: ___________  Fix by: June 9 09:00 UTC
If DEFER: Reason: ___________  New date: ___________  Wave 2 impact: ___________
```

### 18:00–22:00 UTC — Evening Block

- Begin access provisioning for all confirmed authors (if not already complete)
- Confirm all author platform accounts have been created and invitations sent
- Finalize peer review pairings; prepare pairing announcement

---

## June 9 (Sunday) — Publication Day

**Total orchestrator hours today:** 4 hours

**This is the critical day. Two parallel streams run: publication (platform) and author onboarding finalization (pre-sprint).**

### 09:00–11:00 UTC — Final Pre-Publication Check (2 hours)

Run the publication day morning block from `PHASE_5_PUBLICATION_READINESS_CHECKLIST.md` Section 6. Confirm:

1. All five documents present, no accidental changes since June 8 go/no-go
2. Frontmatter-stripped copies in staging directory are current
3. PDFs accessible
4. Platform accessible and admin login confirmed
5. Announcement email filled in and ready to send
6. Git repository clean (no uncommitted changes to corpus files)

**[PLATFORM-SPECIFIC] Final access check:**

[NEXTCLOUD+MATRIX ONLY]: Log into Nextcloud admin. Navigate to `Phase5-Wave1-Published` folder (or create it now if not yet ready). Confirm share link is generated and the access model (public-read or restricted) is correctly set. Test in anonymous browser tab: the share link should show the folder contents without requiring login.

[DISCOURSE ONLY]: Log into Discourse admin. Navigate to "Phase 5 Wave 1 — Published Research" category. Confirm category exists and permissions are set. Log out, visit the category URL, confirm it is accessible as intended for anonymous visitors.

**If any blocker is found during the morning check:** Apply the go/no-go decision from Section 5 of the readiness checklist. If the issue can be fixed in under 2 hours, fix it before the publication window. If it requires more than 2 hours, activate Contingency A and move publication to June 12.

### 13:00–17:00 UTC — Publication Window (4 hours)

Execute the publication steps from `PHASE_5_PUBLICATION_READINESS_CHECKLIST.md` Section 6, Publication Window.

**[NEXTCLOUD+MATRIX ONLY]:**
1. Upload all five frontmatter-stripped documents and the integrated corpus to `Phase5-Wave1-Published` folder
2. Set folder sharing: "Share with link" → read-only → enable "Download" → copy share URL
3. Create optional `README.md` in published folder with document list and one-sentence descriptions
4. Pin the folder share link in Matrix room `#phase5-discussion:resilience-hub` with announcement text
5. Send the founding coalition announcement email (Template 5) with the confirmed share URL
6. Note publication timestamp

**[DISCOURSE ONLY]:**
1. Create topics in reverse order — scale to governance (post scale last, governance first in display):
   - "Veterinary Care in Crisis Contexts" — paste stripped content → Submit
   - "Psychological Support and Trauma Recovery" — paste stripped content → Submit
   - "Conflict Resolution and Governance Framework" — paste stripped content → Submit
   - "Community Implementation Playbook — Tier 3 Coordination Framework" — paste stripped content → Submit
   - "Distributed Microgrids as Community Resilience Infrastructure" — paste stripped content → Submit
2. Create announcement topic: "Phase 5 Wave 1+2 Published — Five Community-Scale Resilience Documents" → Pin as category announcement
3. Log out; in anonymous browser, confirm all five topics visible and readable
4. Send founding coalition announcement email with Discourse category URL
5. Note publication timestamp

**Author onboarding parallel stream** (run while publication is uploading or immediately after):

- [ ] Finalize domain assignments and peer review pairings (confirmed from June 7–8 screening)
- [ ] Announce pairings to all confirmed authors via their platform workspace or email
- [ ] Upload/post domain scope documents and annotated bibliographies to each author's workspace
- [ ] Post the sprint kickoff note (Template 3 from WAVE_2_AUTHOR_ONBOARDING_KIT) in each author's workspace

### 17:00–22:00 UTC — Post-Publication Monitoring

Run the monitoring checkpoints from `PHASE_5_PUBLICATION_READINESS_CHECKLIST.md` Section 6, Monitoring Checkpoints.

T+1 hour check (approximately 14:00 or 17:00 UTC):
- [ ] All 5 documents accessible in anonymous browser session
- [ ] Platform search returns results for "microgrids", "psychological support", and "veterinary"
- [ ] No error messages on any document page
- [ ] Announcement email confirmed sent

T+4 hour check (approximately 21:00 UTC):
- [ ] No access control failures reported
- [ ] At least 1 person other than the project lead has confirmed access
- [ ] Log publication completion with timestamp in WORKLOG.md

---

## June 10 (Monday) — Wave 2 Sprint Kickoff (T+0)

**Total orchestrator hours today:** 3 hours

### 09:00–12:00 UTC — Sprint Launch

**By 12:00 UTC, all confirmed Wave 2 authors receive:**
- [ ] Domain scope document (full outline, section structure, depth expectations)
- [ ] Annotated bibliography (25–40 sources, green/amber/red quality rating)
- [ ] Zone 5 context briefing (embedded in scope document)
- [ ] Peer review partner name and contact
- [ ] Reminder of first-draft checkpoint date (June 17, T+7)
- [ ] Sprint kickoff note from project lead

**Project lead sprint kickoff message** (post to each author's workspace):

---

Wave 2 sprint is officially open. T+0 today. Your first-draft checkpoint is June 17 (T+7). Between now and then: read your scope document, skim your annotated bibliography, and start your section outline. If anything in the scope document is unclear or seems too broad or too narrow, message me today or tomorrow — week 1 is the easiest time to adjust scope.

First checkpoint (T+7, June 17): 50% draft — section outline complete, Sections 1 and 2 narrative-complete, citations roughed in.

---

### 12:00–18:00 UTC — Post-Launch Monitoring

- Monitor author workspaces for same-day questions; respond within 4 hours on Day 1
- Run the 24-hour post-publication review for Wave 1 content (from PHASE_5_PUBLICATION_READINESS_CHECKLIST.md Section 6)
- Begin author sprint status tracking table
- Log June 10 execution status in WORKLOG.md

---

## June 11–14 (Tuesday–Friday) — Wave 2 Active Sprint + Publication Engagement Monitoring

**Daily routine: 15–30 minutes per day**

Each day, June 11–14:
1. Check author workspaces for new questions or status updates
2. Respond to any messages within 24 hours (target: same business day)
3. Note any author with no workspace activity for 48+ hours (early warning, not yet escalation)
4. Scan Wave 1 publication engagement metrics (see below)

**[PLATFORM-SPECIFIC] Engagement monitoring:**

[NEXTCLOUD+MATRIX ONLY]: Check Nextcloud file access logs (admin panel → logging, if enabled) for download/view counts per document. Check Matrix `#phase5-discussion` room for any messages from non-Wave-2 members. Note: Nextcloud does not have native analytics; file access counts may require FTS or external logging configuration.

[DISCOURSE ONLY]: Check topic view counts, reply counts, and likes for each of the five published topics. Note which domain has the most views; note which generated discussion.

**What engagement data tells you** (informational only — does not change sprint timeline):

| Signal | Implication for Wave 2 |
|--------|------------------------|
| Microgrids has most views | Energy infrastructure is high-interest — consider whether Wave 2 water systems document emphasizes energy-water nexus |
| Conflict Resolution has most discussion | Governance practitioners are engaging — Wave 2 food preservation should connect explicitly to resource allocation governance |
| Zero discussion by June 12 | Announcement may not have reached target audience — send a personal note to 5–10 specific contacts from the resistance-research coalition; do not adjust Wave 2 scope or timeline |
| Clinical documents (Psych Support, Vet Care) generate practitioner questions | Consider flagging questions to the advisory-level reviewers identified in the publication readiness checklist |

**Engagement data does not change the Wave 2 sprint timeline.** Wave 2 authors began June 10 regardless. Metrics inform post-publication messaging and Phase 6 scoping, not in-flight research.

### Contingency Monitoring (June 11–14)

**Author silence protocol (escalation trigger: 5 days no activity):**

If an author has no workspace activity by June 15 (5 days after T+0):
1. Send a direct message: "Checking in — how is the sprint going? Anything blocking you?"
2. If no response within 2 days: phone or escalation email
3. If confirmed drop-out: activate scope reduction for that domain OR project lead self-execution

**Platform instability protocol (trigger: 4+ hours inaccessible):**

[NEXTCLOUD+MATRIX ONLY]: Check raspby1 server health: SSH to 100.70.184.84, run `docker ps`. If Nextcloud container is down: `docker compose up -d` in the stack directory. If Tailscale is the issue: troubleshoot Tailscale client on raspby1. Fallback: share files via GitHub repo while Nextcloud is restored.

[DISCOURSE ONLY]: SSH to VPS, check Discourse status: `cd /var/discourse && sudo ./launcher status`. If down: `sudo ./launcher restart app`. Fallback: coordinate via email while Discourse is restored.

**If platform is unstable for more than 24 hours:** Move coordination temporarily to email. Send all authors: "Platform is temporarily down — send draft updates and questions to [email] until restored." This is a degraded-mode fallback, not a platform migration.

---

## June 15 (Saturday) — Wave 2 Onboarding Complete; Readiness Assessment

**Total orchestrator hours today:** 2–3 hours

### 09:00–12:00 UTC — Onboarding Completion Assessment

By June 15, assess: Is Wave 2 fully onboarded and zero-blocked for the June 17 first-draft checkpoint?

**Wave 2 readiness checklist (June 15):**
- [ ] All confirmed Wave 2 authors have platform access (can log in, can see their workspace)
- [ ] All confirmed authors have received their domain scope documents and annotated bibliographies
- [ ] All confirmed authors have acknowledged the first-draft checkpoint protocol (T+7, June 17)
- [ ] Peer review pairings have been announced and each author knows their partner
- [ ] No author has reported a blocking issue that has not been resolved
- [ ] Sprint status tracking table is current
- [ ] Wave 1 publication engagement metrics captured (baseline for June 15)

**If any item is unchecked:** resolve it today. June 15 is the last day before the T+7 first-draft checkpoint on June 17 becomes the critical path milestone. Any onboarding blocker left unresolved June 15 becomes a sprint blocker June 17.

### 12:00–18:00 UTC — June 20 Readiness Assessment

With Wave 1 publication live and Wave 2 sprint underway, assess readiness for the June 20 first publication target.

The June 20 target assumes Wave 2 authors are producing early-domain documents (e.g., food preservation or a partially-drafted domain) ahead of the full July 10 cohort. This is an aspirational date, not the full-cohort target.

**June 20 publication is achievable only if:**
- At least one Wave 2 author has strong progress by June 17 T+7 checkpoint (50% draft ready) AND
- That author's domain is food preservation or water systems (highest reader demand) AND
- Peer review can happen June 24 and revisions by June 27, meeting a June 28–30 readiness date (not June 20 — the June 20 target is very tight; June 25–30 is more realistic for a first Wave 2 publication)

**Honest assessment:** The June 20 target for Wave 2 first publication is achievable only in the best-case scenario (all authors onboarded by June 10, strong T+7 checkpoints June 17, fast peer review). The operationally realistic first Wave 2 publication date is June 28–30 for the fastest domain. The full-cohort publication target of July 10–15 is solid.

---

## Platform-Specific Branching Summary Table

All steps below are the only platform-diverging actions in this timeline. Everything else is identical.

| Step | [NEXTCLOUD+MATRIX] | [DISCOURSE] |
|------|-------------------|-------------|
| June 5: Platform pre-check | SSH raspby1; confirm Docker + Nextcloud at Tailscale URL | SSH VPS; confirm Discourse launcher status |
| June 6: Platform deployment | Docker stack: 6–8 hours; create folder structure | Discourse installer: 3–4 hours; create categories and group |
| June 7: Author workspace creation | Create Nextcloud domain folders; upload scope files | Create Discourse scope topics + draft thread topics per author |
| June 7–8: Author access provisioning | Create user accounts; share folders; create Matrix rooms; send invitations | Send Discourse account invitations; add to wave-2-contributors group |
| June 9: Publish Wave 1+2 content | Upload stripped .md files to Phase5-Wave1-Published folder; set share link; pin in Matrix room | Create one Discourse topic per document in reverse order; create announcement topic |
| June 9: Wave 2 scope distribution | Add scope and bibliography files to each author's Nextcloud folder | Post scope and bibliography as Discourse scope topic body |
| June 9: Peer review pairing announcement | Pinned message in Matrix `#wave2-general` room | Pinned Discourse topic in Wave 2 private category |
| June 10: Sprint kickoff message | Matrix direct message per author OR announcement in `#wave2-general` | Discourse direct message per author OR new announcement topic in Wave 2 category |
| June 11–15: Daily engagement check | Nextcloud file access logs + Matrix room activity | Discourse topic views + reply counts |
| Platform recovery if down | `docker compose up -d` on raspby1; fallback: GitHub repo | `./launcher restart app` on VPS; fallback: email |

---

## Contingency Branches

### Contingency A — Platform Deployment Delay

**Slip trigger:** Platform setup takes more than 6 hours [NEXTCLOUD+MATRIX] or more than 4 hours [DISCOURSE] during the June 6 deployment block, leaving less than 48 hours before June 9 publication day.

**Response:**
1. Do not delay Wave 2 author invitations — they go out June 5–6 regardless of platform status
2. Activate GitHub Pages fallback immediately: push frontmatter-stripped copies to a GitHub Pages branch (documented in `PHASE_5_GITHUB_PAGES_STAGING.md`). This is a staged fallback already prepared June 1.
3. Publish to GitHub Pages as the publication target: link in the June 9 announcement email goes to the GitHub Pages URL, not the chosen platform URL
4. Continue platform deployment in parallel: migration from GitHub Pages to the chosen platform can happen June 10–12 without disrupting Wave 2 sprint
5. Note in announcement email: "Content is currently accessible at [GitHub Pages URL]. We are migrating to a dedicated platform this week — this link will remain active."

**Wave 2 impact:** None. Wave 2 author onboarding and the June 10 sprint kickoff are unaffected by platform deployment status. Authors receive scope documents and begin writing regardless of whether the primary platform is up.

**Publication delay:** June 9 → June 12 (3-day slip). This is within the tolerable range noted in the scope.

### Contingency B — Slow Author Recruitment (Fewer Than 4 Authors Confirmed by June 8)

**Slip trigger:** By end of day June 8, fewer than 4 of 15 invited candidates have confirmed participation (regardless of pending or non-responses).

**Response:**
1. June 9 morning: contact secondary candidate list (prior project collaborators, resistance-research corpus contributors, one-degree referrals from any confirmed Wave 2 authors). Target 5 additional contacts with an abbreviated invitation note: "We are filling the final Wave 2 spots for a June 10 start — if interested, a quick reply by June 9 evening gets priority."
2. Shift Wave 2 leadership from 4 leads to 3 leads: prioritize medical/food/water domains, self-execute seed saving and equipment repair. Rationale: seed saving and equipment repair are the lowest-credential domains and most amenable to orchestrator self-execution from practitioner literature.
3. For the 3-lead model:
   - Lead 1: Food Preservation & Storage (highest reader demand — must have external author if possible)
   - Lead 2: Water Systems Management (highest operational gap — author with civil/water background strongly preferred)
   - Lead 3: Livestock Management & Pasture Coordination (concentrated Zone 5 author pool)
   - Orchestrator self-executes: Seed Saving + Equipment Repair (targeting July 10 alongside the 3-lead cohort)
4. Do not delay sprint kickoff — June 10 is fixed; late-confirmed authors (confirmed June 10–11) begin at T+1 with a one-day adjusted timeline

**Wave 2 publication impact:** None if 3 leads confirmed. If only 1–2 confirmed by June 10, the July 10 full-cohort target remains achievable via orchestrator self-execution for remaining domains.

### Contingency C — Wave 2 Author Onboarding Incomplete by June 14

**Slip trigger:** By June 14, one or more confirmed Wave 2 authors have not completed access setup, have not acknowledged their scope document, or have not posted a T+0 initial note in their workspace — and the issue cannot be resolved by June 15.

**Response:**
1. For the unresponsive author: escalate via email and phone before marking as a risk. Give until June 16 to check in. If no contact by June 16: treat as potential drop-out.
2. If an author confirms they are behind or overwhelmed: offer scope reduction (reduce target from 4,000–6,000 words to 2,500–3,500 words; this is completable in 15 hours of focused work on a 25-day timeline from June 15 to July 10).
3. If an author confirms drop-out (or is unreachable through June 16): activate project lead self-execution for that domain. A 4,000-word practitioner document can be self-executed in 12–15 orchestrator hours using the same annotated bibliography already prepared.
4. Adjust the Wave 2 publication target: push from June 20 (aspirational) to June 25 (still achievable if 3 leads are confirmed and making progress). Push the full-cohort publication target from July 10 to July 25 (two-week slip — tolerable per scope parameters).

**July 25 full-cohort target** (vs. original July 10) is only triggered if: more than one author drops out AND scope reduction is not feasible AND orchestrator self-execution is partially blocked. In the base case with 3+ confirmed authors, July 10 stands.

---

## Resource Allocation

**Total orchestrator hours, June 5–15:**

| Date | Activity | Estimated Hours |
|------|----------|----------------|
| June 5 | Readiness verification + author invitations | 4–5 hours |
| June 6 | Platform deployment + publication preparation | 4–6 hours |
| June 7 | Screening calls + platform validation | 3–4 hours |
| June 8 | Go/no-go + final confirmations + access provisioning | 2–3 hours |
| June 9 | Publication day + author onboarding + post-launch monitoring | 4 hours |
| June 10 | Sprint kickoff + 24-hour publication review | 3 hours |
| June 11 | Daily monitoring | 0.5 hours |
| June 12 | Daily monitoring | 0.5 hours |
| June 13 | Daily monitoring | 0.5 hours |
| June 14 | Daily monitoring | 0.5 hours |
| June 15 | Onboarding completion assessment + June 20 readiness assessment | 2–3 hours |
| **TOTAL** | | **24–30 hours across 11 days** |

**Platform-admin hours (platform-specific, included in totals above):**

| Platform | Deployment | Workspace setup | Monitoring | Total |
|----------|-----------|-----------------|-----------|-------|
| [NEXTCLOUD+MATRIX] | 6–8 hours (June 6) | 2–3 hours (June 7–9) | Minimal (June 11–15) | 8–11 hours |
| [DISCOURSE] | 3–4 hours (June 6) | 1–2 hours (June 7–9) | Minimal (June 11–15) | 4–6 hours |

**Author hours (Wave 2 authors, not orchestrator):** Zero during June 5–9 (recruitment and onboarding). Beginning June 10, authors work 4–6 hours/week independently — no orchestrator time required per author-hour of research work.

**External reviewer hours (advisory):** 2–3 hours per reviewer if clinical peer reviewers for Psychological Support and Veterinary Care documents are engaged before June 9. This is optional (advisory, not blocking).

---

## Success Criteria for June 5–15

Three gates, each independently verifiable:

**Gate A — Wave 1 publication live and monitored by June 9:**
- All five Wave 1+2 documents accessible on chosen platform (or GitHub Pages fallback)
- Founding coalition announcement email sent
- 24-hour post-publication review complete with no unresolved access failures
- Engagement baseline captured

**Gate B — All Wave 2 authors onboarded by June 15:**
- All confirmed Wave 2 authors have platform access confirmed (can log in and see their workspace)
- All confirmed authors have their domain scope documents and annotated bibliographies
- Peer review pairings announced and acknowledged
- No author is blocked from starting work due to access or scope issues

**Gate C — Wave 2 authoring environment ready June 15:**
- Author status tracking table is populated and current
- T+7 checkpoint dates logged per author (June 17 for all June 10 starters)
- Sprint communication channel is active (Matrix rooms or Discourse Wave 2 category — tested and accessible)
- Contingency monitoring protocols are in place (author silence trigger, platform instability recovery)

---

## Status Grid: Target State at June 15 EOD

| Item | Target State |
|------|-------------|
| Wave 1+2 publication | All 5 documents live on chosen platform (or GitHub Pages fallback); announcement sent; 24-hour review complete |
| Wave 2 authors confirmed | 3–6 authors across 3–5 domains (minimum viable: 3) |
| Sprint status | T+5: authors 5 days into 30-day sprint; T+7 first checkpoint 2 days away |
| Engagement baseline | Views, downloads, or reply counts captured per document (T+7 baseline) |
| Contingencies triggered | Expected: 0–1 minor (slow author response, minor platform adjustment) |
| Next milestone | June 17 (T+7): first-draft checkpoints due from all Wave 2 authors |

If actual state on June 15 diverges significantly from the above, consult `PHASE_5_WAVE_2_DECISION_FRAMEWORK.md` for scope adjustment and sequencing decisions.

---

*Version 2.0 — full dual-platform edition with executive summary, resource allocation, and three named contingency branches*
*Created June 4, 2026 | Execution starts June 5 08:00 UTC | Publication target June 9 13:00 UTC | Wave 2 sprint start June 10 | Wave 2 onboarding complete June 15*
