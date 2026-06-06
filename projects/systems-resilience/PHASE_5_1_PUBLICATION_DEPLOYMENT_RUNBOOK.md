---
title: "Phase 5.1 Publication Deployment Runbook"
project: systems-resilience
phase: 5
wave: 1+2
status: READY-FOR-EXECUTION
purpose: "Detailed step-by-step SOP for Phase 5.1 publication June 9, 2026. Publication order, upload sequence, notification protocol, monitoring plan, and rollback procedure."
publication_date: 2026-06-09
publication_start_time: "2026-06-09 13:00 UTC"
estimated_duration: "90 minutes (upload + verification + notifications)"
---

# Phase 5.1 Publication Deployment Runbook
## Execution Guide for June 9, 2026 13:00 UTC Publication

---

## Executive Summary

**Publication Timeline**: June 9, 2026 13:00 UTC — 15:00 UTC (90-minute execution window)

**Content Being Published**:
- 5 primary research documents (Microgrids, Playbook, Conflict Resolution, Psychological Support, Veterinary Care)
- 1 integrated corpus (unified 16,243-word reference)
- Metadata sidecar + PDF bundle
- Total: 61,611 words, 336+ citations

**Publication Method**: Platform upload (Nextcloud+Matrix OR Discourse — determined June 6 decision)

**Success Criteria**:
- All five documents + corpus live and accessible by 15:00 UTC
- Public announcement sent to author coalition
- Post-publication monitoring complete by 15:30 UTC
- Zero critical errors in first 2 hours

**Key Personnel**:
- **Publisher** (orchestrator): Executes upload sequence
- **Monitor** (if available): Watches for platform errors in parallel
- **Backup Publisher** (if available): Ready to step in if primary unavailable

**Risk Level**: LOW — all assets pre-verified, deployment scripts tested, contingencies documented

---

## PRE-PUBLICATION SETUP (June 9, 12:30–13:00 UTC)

### 12:30 UTC — Publisher Preparation

**Check 1: All Assets Ready**
```bash
# Verify all publication assets are in place
ls -lah /tmp/phase5-pub/

# Expected output:
# - 5 .md files (frontmatter-stripped copies)
# - phase5-pub/pdf/ directory with 6 PDF files
# - phase5-wave1-2-metadata.csv
```

**Check 2: Platform Access Confirmed**

[NEXTCLOUD+MATRIX]:
```bash
# SSH to raspby1 and confirm Nextcloud running
ssh <user>@100.70.184.84
docker ps | grep nextcloud
# Expected: nextcloud container running, status "Up"

# Confirm admin login works; navigate to https://100.70.184.84/nextcloud
# Expected: Admin dashboard accessible
```

[DISCOURSE]:
```bash
# SSH to VPS and confirm Discourse running
ssh <user>@<discourse-ip>
cd /var/discourse && sudo ./launcher status
# Expected: web running, postgres running

# Confirm Discourse URL accessible from browser: <discourse-domain>
# Expected: Discourse homepage loads without errors
```

**Check 3: Announcement Email Ready**

- [ ] Draft announcement email finalized (from WAVE_2_AUTHOR_ONBOARDING_KIT_DUAL_PLATFORM.md template)
- [ ] Recipient list prepared (all 8 author cohort emails ready)
- [ ] Platform URLs inserted into email template
- [ ] Subject line finalized: "Phase 5 Wave 1+2 Published — Community Resilience Framework Ready"

**Check 4: Team Briefing (If applicable)**

If additional team members are watching:
- Assign one person to monitor platform for first 30 min
- Assign one person to monitor email notifications
- Brief all on rollback trigger (Section 8 below)

**12:50 UTC**: All pre-checks complete; proceed to publication upload

---

## PUBLICATION UPLOAD SEQUENCE (June 9, 13:00–14:30 UTC)

### Publication Order Rationale

Documents are uploaded in this specific order to ensure:
1. **Foundational content first** (Microgrids provides infrastructure context)
2. **Implementation guidance second** (Playbook builds on microgrids)
3. **Conflict/emotional support last** (Psychological + Conflict + Veterinary provide operational detail for practitioners)
4. **Integrated corpus last** (unified reference available after all components live)

This order matches reader workflows: infrastructure → implementation → operational detail → reference.

---

### Document 1: Distributed Microgrids (13:00–13:15 UTC)

**File to Upload**: `/tmp/phase5-pub/PHASE_5_WAVE_2_MICROGRIDS_RESEARCH_OUTLINE.md`

**[NEXTCLOUD+MATRIX UPLOAD]**:

1. SSH to raspby1 and navigate to Nextcloud file manager
   ```bash
   ssh <user>@100.70.184.84
   # Navigate to Nextcloud UI: https://100.70.184.84/nextcloud
   # Admin login
   ```

2. Create folder structure (if not already created):
   ```
   Phase 5 Published Research/
   ├── 01-Microgrids/
   ├── 02-Community-Implementation/
   ├── 03-Conflict-Resolution/
   ├── 04-Psychological-Support/
   ├── 05-Veterinary-Care/
   └── 00-Integrated-Corpus/
   ```

3. Upload file: Drag-drop `/tmp/phase5-pub/PHASE_5_WAVE_2_MICROGRIDS_RESEARCH_OUTLINE.md` into `01-Microgrids/` folder

4. Verify upload:
   - [ ] File appears in folder
   - [ ] File size matches expected (roughly 65 KB)
   - [ ] Click file to preview; verify first section (executive summary) is visible and renders correctly

**[DISCOURSE UPLOAD]**:

1. Log into Discourse admin panel
2. Create new topic in "Phase 5 Wave 1 — Published Research" category
3. Topic title: `"01 — Distributed Microgrids as Community Resilience Infrastructure"`
4. Topic body: Copy entire content from `/tmp/phase5-pub/PHASE_5_WAVE_2_MICROGRIDS_RESEARCH_OUTLINE.md` into topic body
5. Set topic tags: `microgrids`, `phase-5`, `infrastructure`, `energy-systems`
6. Publish topic
7. Verify rendering:
   - [ ] Headings display correctly
   - [ ] Tables render as formatted tables
   - [ ] No YAML frontmatter visible at top
   - [ ] Scroll to end; verify conclusion section present

**Upload Complete**: 13:15 UTC

---

### Document 2: Community Implementation Playbook (13:15–13:30 UTC)

**File to Upload**: `/tmp/phase5-pub/phase-5-wave-2-community-implementation-playbook.md`

**[NEXTCLOUD+MATRIX UPLOAD]**:
- Upload to `02-Community-Implementation/` folder
- Filename in Nextcloud: `Community-Implementation-Playbook.md` (remove extra hyphens for readability)
- Verify: File appears, preview shows Section 1 content

**[DISCOURSE UPLOAD]**:
- Create new topic: `"02 — Community Implementation Playbook — Tier 3 Coordination Framework"`
- Copy content; set tags: `governance`, `coordination`, `implementation`, `phase-5`
- Verify: Tables (Ostrom principles table, resource types table, implementation checklists) render correctly

**Upload Complete**: 13:30 UTC

---

### Document 3: Conflict Resolution Framework (13:30–13:45 UTC)

**File to Upload**: `/tmp/phase5-pub/phase-5-wave-2-conflict-resolution-framework.md`

**[NEXTCLOUD+MATRIX UPLOAD]**:
- Upload to `03-Conflict-Resolution/` folder
- Filename: `Conflict-Resolution-Framework.md`
- Verify: File appears, first section visible

**[DISCOURSE UPLOAD]**:
- Create new topic: `"03 — Conflict Resolution and Governance Framework"`
- Copy content; set tags: `conflict-resolution`, `mediation`, `governance`, `nvc`, `phase-5`
- Verify: NVC (Nonviolent Communication) framework tables render; mediation scripts visible

**Upload Complete**: 13:45 UTC

---

### Document 4: Psychological Support Guide (13:45–14:00 UTC)

**File to Upload**: `/tmp/phase5-pub/phase-5-wave-2-psychological-support-guide.md`

**Pre-Upload Advisory**: Include this note in Nextcloud folder description or Discourse topic footer:

> **Clinical Advisory**: This document contains Psychological First Aid (PFA) protocols based on SAMHSA and Red Cross guidelines. All clinical procedures should be adapted to local mental health professional standards and jurisdiction-specific requirements. Not a substitute for professional mental health care.

**[NEXTCLOUD+MATRIX UPLOAD]**:
- Upload to `04-Psychological-Support/` folder
- Filename: `Psychological-Support-and-Trauma-Recovery.md`
- Include advisory note in folder description (Nextcloud folder settings)
- Verify: File appears; PFA protocols section visible

**[DISCOURSE UPLOAD]**:
- Create new topic: `"04 — Psychological Support and Trauma Recovery — Tier 2 Household Guide"`
- **IMPORTANT**: Add advisory as first post in topic: 
  ```
  > **Clinical Advisory**: This document contains Psychological First Aid (PFA) protocols 
  > based on SAMHSA and Red Cross guidelines. All clinical procedures should be adapted 
  > to local professional standards. Not a substitute for professional mental health care.
  ```
- Copy content below advisory
- Set tags: `psychological-support`, `trauma`, `pfa`, `mental-health`, `phase-5`
- Verify: Protocols section renders; advisory visible at top

**Upload Complete**: 14:00 UTC

---

### Document 5: Veterinary Care Guide (14:00–14:15 UTC)

**File to Upload**: `/tmp/phase5-pub/phase-5-wave-2-veterinary-care-guide.md`

**Pre-Upload Advisory**: Include this note:

> **Professional Practice Advisory**: This document contains veterinary protocols and triage procedures. Implementation requires collaboration with licensed veterinarians. Protocols should be adapted to local disease patterns, climate conditions, and professional veterinary standards. Not a substitute for professional veterinary medicine.

**[NEXTCLOUD+MATRIX UPLOAD]**:
- Upload to `05-Veterinary-Care/` folder
- Filename: `Veterinary-Care-in-Crisis-Contexts.md`
- Include advisory in folder description
- Verify: File appears; triage protocols section visible

**[DISCOURSE UPLOAD]**:
- Create new topic: `"05 — Veterinary Care in Crisis Contexts — Tier 2 Household Guide"`
- **IMPORTANT**: Add advisory as first post:
  ```
  > **Professional Practice Advisory**: This document contains veterinary protocols and triage 
  > procedures requiring collaboration with licensed veterinarians. Adapt to local disease 
  > patterns and professional standards. Not a substitute for professional veterinary medicine.
  ```
- Copy content below advisory
- Set tags: `veterinary`, `livestock`, `crisis-medicine`, `farm-animals`, `phase-5`
- Verify: Protocols render correctly; advisory visible

**Upload Complete**: 14:15 UTC

---

### Document 6: Integrated Corpus (14:15–14:30 UTC)

**File to Upload**: `/tmp/phase5-pub/PHASE_5_WAVE_1_2_INTEGRATED_CORPUS.md`

**[NEXTCLOUD+MATRIX UPLOAD]**:
- Upload to `00-Integrated-Corpus/` folder (separate location for easier finding)
- Filename: `Phase-5-Wave-1-2-Integrated-Corpus-Complete-Reference.md`
- Verify: File appears; Table of Contents section visible; can scroll through TOC without errors

**[DISCOURSE UPLOAD]**:
- Create pinned topic in "Phase 5 Wave 1 — Published Research" category
- Topic title: `"📚 REFERENCE: Integrated Corpus — Phase 5 Wave 1+2 Complete Research"`
- Copy content from `/tmp/phase5-pub/PHASE_5_WAVE_1_2_INTEGRATED_CORPUS.md`
- **SET AS PINNED TOPIC** (admin only) — this keeps the integrated reference at top of category
- Set tags: `reference`, `corpus`, `complete`, `phase-5`
- Verify: 
  - [ ] Table of Contents renders correctly with 5 main sections
  - [ ] All section links/anchors work
  - [ ] Integrated corpus shows complete content (spot-check: scroll to middle, verify content is complete)
  - [ ] Topic appears at top of category as pinned

**Upload Complete**: 14:30 UTC

**All Documents Now Live**: 14:30 UTC

---

## IMMEDIATE POST-PUBLICATION VERIFICATION (14:30–14:45 UTC)

### Verification Checklist

**[NEXTCLOUD+MATRIX]**:

1. Open Nextcloud file browser in new anonymous window (incognito/private browsing)
   - [ ] Confirm `Phase 5 Published Research` folder is visible
   - [ ] All 6 subfolders visible (01-Microgrids, 02-Community-Implementation, etc.)
   - [ ] Can open each markdown file and view content

2. Click each folder; verify each document renders:
   - [ ] Microgrids: Executive summary visible; tables render correctly
   - [ ] Playbook: Section 1-3 visible; Ostrom table renders
   - [ ] Conflict Resolution: NVC framework visible
   - [ ] Psychological Support: Protocols section visible; advisory note clear
   - [ ] Veterinary Care: Triage protocols visible; advisory note clear
   - [ ] Integrated Corpus: TOC visible; can scroll through sections

3. Test search (if full-text search enabled):
   - [ ] Search for "microgrids" → returns microgrids document
   - [ ] Search for "Ostrom" → returns playbook
   - [ ] Search for "livestock" → returns veterinary care
   - *Note: FTS indexing takes ~10 min; if not indexed yet, document as expected and retest in 15 min*

4. Share link test (if applicable):
   - [ ] Nextcloud share link is active
   - [ ] Can download all documents via share link
   - [ ] All files appear in share folder view

**[DISCOURSE]**:

1. Open Discourse in new anonymous window
   - [ ] Navigate to "Phase 5 Wave 1 — Published Research" category
   - [ ] Confirm 6 topics visible (5 documents + pinned integrated corpus at top)

2. Click each topic; verify content:
   - [ ] Topic 01 (Microgrids): Heading visible; Executive Summary renders; no frontmatter visible
   - [ ] Topic 02 (Playbook): Governance section visible; tables render
   - [ ] Topic 03 (Conflict Resolution): NVC content visible
   - [ ] Topic 04 (Psychological Support): Advisory note visible at top; PFA protocols visible
   - [ ] Topic 05 (Veterinary Care): Advisory note visible at top; protocols render
   - [ ] Pinned Corpus: TOC renders; integrated content visible; pinned indicator visible

3. Test search:
   - [ ] Search for "microgrids" → returns Topic 01 and Corpus
   - [ ] Search for "Ostrom" → returns playbook
   - [ ] Search for "livestock" → returns veterinary care
   - [ ] Search appears within 60 seconds of topic creation (Discourse native FTS)

4. Test topic interaction (spot-check):
   - [ ] Can scroll through long topic (integrated corpus) without rendering lag
   - [ ] Topic metadata displays (created date, views count)
   - [ ] Reply button works (if not restricting replies, can open reply box)

---

## NOTIFICATION SEQUENCE (14:45–15:00 UTC)

### Step 1: Public Announcement (14:45 UTC)

**Medium**: Email to author coalition + public announcement (if applicable)

**Email Subject**: `Phase 5 Wave 1+2 Published — Community Resilience Framework Ready for June 14 Wave 2 Recruitment`

**Email Body Template** (customize with actual URLs):

```
Subject: Phase 5 Wave 1+2 Published — Community Resilience Framework Ready

Dear Coalition Members,

Phase 5 Wave 1+2 research is now published and ready for community engagement.

DOCUMENTS LIVE:
1. Distributed Microgrids as Community Resilience Infrastructure
2. Community Implementation Playbook — Tier 3 Coordination Framework
3. Conflict Resolution and Governance Framework
4. Psychological Support and Trauma Recovery
5. Veterinary Care in Crisis Contexts
6. Integrated Corpus (complete reference)

ACCESSING THE DOCUMENTS:

[NEXTCLOUD+MATRIX]:
Platform URL: https://100.70.184.84/nextcloud/
Directory: Phase 5 Published Research/
All documents are publicly downloadable. No account required.

[DISCOURSE]:
Platform URL: <discourse-domain>
Category: "Phase 5 Wave 1 — Published Research"
All topics are publicly readable. No account required to read.

NEXT STEPS:

Wave 2 author recruitment begins June 14, 2026 (8 days from publication).

We will be contacting selected authors for Phase 6 expansion domains. If you believe you should be considered for Wave 2 authoring, please reply to this email with:
- Your expertise area (governance, infrastructure, etc.)
- Hours per week available July–September
- Prior research or writing experience

ADVISORY NOTES:

Psychological Support and Veterinary Care guides contain clinical and professional protocols. These are grounded in evidence-based frameworks (SAMHSA, AVMA) but should be adapted to local professional standards and jurisdiction-specific requirements.

Thank you for being part of this research effort.

Best regards,
[Orchestrator Name]
Systems Resilience Project
[Contact Email]
```

**Send to**: All 8 Wave 2 author cohort members (emails prepared in pre-publication setup)

- [ ] Email sent to all recipients by 14:45 UTC
- [ ] Verify send confirmation for each email

### Step 2: Platform Announcement (14:50 UTC)

**[NEXTCLOUD+MATRIX]** (if applicable):
- Create announcement text file in `Phase 5 Published Research/` folder named `README-PUBLICATION-NOTICE.txt`
- Content:
  ```
  PHASE 5 WAVE 1+2 PUBLICATION — JUNE 9, 2026
  
  Welcome to the community resilience research corpus.
  
  Five research guides address:
  - Microgrids and energy infrastructure
  - Community-scale implementation and governance
  - Conflict resolution frameworks
  - Psychological support in crisis
  - Veterinary care for livestock
  
  All content is open source and freely available.
  
  For questions or feedback: [contact-email]
  ```

**[DISCOURSE]** (if applicable):
- Create pinned announcement topic:
  - Title: `📢 ANNOUNCEMENT: Phase 5 Wave 1+2 Publication Complete`
  - Body:
    ```
    Phase 5 Wave 1+2 research is now published.
    
    Six documents in the "Phase 5 Wave 1 — Published Research" category cover:
    1. Microgrids as community infrastructure
    2. Implementation playbook and governance
    3. Conflict resolution frameworks
    4. Psychological support and trauma recovery
    5. Veterinary care in crisis contexts
    6. Integrated corpus (complete reference)
    
    All content is open, freely available, and licensed for community use.
    
    Wave 2 author recruitment begins June 14, 2026.
    
    For questions: [contact-email]
    ```
  - Pin this topic (Admin only)

### Step 3: Metadata & Asset Distribution (15:00 UTC)

**Upload metadata and PDF bundle**:

**[NEXTCLOUD+MATRIX]**:
- Create folder: `Phase 5 Published Research/Assets/`
- Upload:
  - `phase5-wave1-2-metadata.csv` (for Zotero import, metadata indexing)
  - `pdf/` folder with all 6 PDFs

**[DISCOURSE]**:
- Create topic: `📥 Downloads — PDF Bundle and Metadata`
- Upload as attachments (or link to):
  - `phase5-wave1-2-metadata.csv`
  - PDF files (if Discourse file upload allowed; otherwise link to external storage)
- Note: Discourse has 100 MB upload limit per post; if PDF bundle > 100 MB, split across multiple posts or link to external storage

### Step 4: Social/Public Announcement (15:00 UTC)

**If applicable** (depends on whether publication is public-facing):

- [ ] Post to project website/blog (if applicable)
- [ ] Post to social media (Twitter/X, Mastodon, etc.) if project has public presence
- [ ] Link to Discourse/Nextcloud
- [ ] Tag Wave 2 authors or community partners

**Sample Social Post**:
```
📚 Phase 5 Wave 1+2 Published

Community resilience research now live:
• Microgrids as infrastructure
• Implementation & governance
• Conflict resolution
• Psychological support
• Veterinary care

All open, freely available. Read, share, adapt.

[Link to platform]
```

---

## POST-PUBLICATION MONITORING (15:00–17:00 UTC)

### Monitoring Tasks (90-minute window)

**Every 10 minutes, first 30 minutes** (15:00–15:30 UTC):

- [ ] Check platform status (both Nextcloud and Discourse if running in parallel)
  - Is the platform responding? Load times normal?
  - Can documents still be viewed?
  - Any error messages in platform logs?

- [ ] Check for user activity
  - Are documents being viewed? (Check Nextcloud view counts or Discourse view analytics)
  - Any comments/questions posted?
  - Any error reports?

**Every 30 minutes, second 60 minutes** (15:30–17:00 UTC):

- [ ] Platform stability check
- [ ] Document accessibility from external IP (if not already behind proxy)
- [ ] Search functionality operational (if not already verified)
- [ ] No critical errors in server logs

**Alert Triggers** (if any of these occur, activate rollback procedure in Section 8):

- Platform down or unresponsive (503, 500 errors)
- Documents not rendering (text appears as raw markdown, tables broken)
- Large-scale access denial (users report login/permissions issues)
- Metadata corruption (documents visible but content garbled)

---

## ROLLBACK PROCEDURE (If Triggered)

### Rollback Trigger Conditions

Rollback is triggered if **any** of these conditions occur:

1. Platform completely down (unreachable, 502/503 errors)
2. All documents inaccessible (permissions issue affecting all users)
3. Critical content corruption (documents render but content is scrambled/truncated)
4. Security incident (unauthorized access, malicious modifications)

**Probability of rollback**: < 1% (all assets pre-verified, platform tested)

### Rollback Steps (If Needed)

**Step 1: Stop new uploads (immediately)**
- If rollback is triggered, do not upload any additional documents
- All documents currently live remain as-is pending investigation

**Step 2: Notify users (within 10 minutes of detection)**
- Post announcement in Discourse: "We've temporarily taken Phase 5 content offline for investigation. We'll restore within 2 hours."
- Email author coalition: "Publication paused due to [brief reason]. Restarting at [new time]."

**Step 3: Diagnose issue (30 minutes)**
- [NEXTCLOUD]: SSH to server; check Docker logs: `docker logs nextcloud`
- [DISCOURSE]: SSH to server; check Discourse logs: `cd /var/discourse && ./launcher logs web`
- Identify root cause (disk space? permissions? corrupted file? network issue?)

**Step 4: Resolve issue (varies)**
- If permissions issue: fix permissions on Nextcloud folder or Discourse category
- If disk space: archive old uploads or expand storage
- If corrupted file: delete file and re-upload from `/tmp/phase5-pub/`
- If network: confirm connectivity; restart services if needed

**Step 5: Republish (after issue resolved)**
- Verify platform is stable and responsive
- Republish documents starting with Document 1 (Microgrids)
- Run full verification again (15 min)
- Send "Publication Restored" announcement

**New Publication Time** (if rollback occurs):
- Issue < 30 min to resolve: Republish by June 9 17:00 UTC
- Issue 30–60 min to resolve: Republish by June 9 18:00 UTC
- Issue > 60 min to resolve: Shift publication to June 10 10:00 UTC (next morning)

---

## SUCCESS CRITERIA — Publication Complete

**All of the following must be true by 15:00 UTC for publication to be considered successful:**

- [ ] All 5 source documents live on platform
- [ ] Integrated corpus live on platform
- [ ] All documents render correctly (no broken markdown, tables formatted, text readable)
- [ ] No YAML frontmatter visible in any document
- [ ] Both plain text (Nextcloud/Discourse) and PDF copies available
- [ ] Metadata sidecar created and available for download
- [ ] Announcement email sent to all author coalition members
- [ ] Public notification posted (platform announcement and/or social)
- [ ] Platform stable and responsive (no errors in monitoring window)
- [ ] Search functional (documents findable by keyword)
- [ ] Access control working as intended (public read, appropriate write restrictions)

**If all criteria met**: ✅ **Publication Successful**

**If any criterion not met**: 
- Identify which criterion failed
- Execute specific remediation (not full rollback unless critical)
- Retry within 1 hour
- Document issue and resolution for post-mortem

---

## POST-PUBLICATION HANDOFF (15:00 UTC+)

### Wave 2 Recruitment Activation

Once publication is confirmed successful, immediately begin Wave 2 author recruitment execution:

- [ ] Review `WAVE_2_AUTHOR_MATCHING_ALGORITHM.md` and `WAVE_2_AUTHOR_PROFILE_CARDS.md`
- [ ] Prepare Wave 2 recruitment email outreach (templates in `WAVE_2_RECRUITMENT_COMMUNICATION_TEMPLATES.md`)
- [ ] Confirm author contact information is current
- [ ] Schedule Wave 2 recruitment kickoff call (June 10–12) if not already scheduled

### Documentation & Closeout

- [ ] Document any issues encountered during publication (if any)
- [ ] Update orchestrator memory with publication outcome
- [ ] Archive `/tmp/phase5-pub/` assets to project backup
- [ ] Confirm metrics: documents live, views, user feedback (if applicable)

---

## DEPLOYMENT RUNBOOK COMPLETION

**Estimated Total Execution Time**: 90 minutes (13:00–15:00 UTC)

**Breakdown**:
- Pre-publication setup: 30 min (12:30–13:00)
- Document uploads: 90 min (13:00–14:30)
- Verification: 15 min (14:30–14:45)
- Notifications: 15 min (14:45–15:00)
- Initial monitoring: 60 min (15:00–16:00)
- Ongoing monitoring: 60 min (16:00–17:00)

**Key Dependencies**:
- Platform access (Nextcloud SSH or Discourse admin login)
- Network connectivity
- Email access for announcements
- All pre-publication assets prepared (Section 1 pre-checks)

**Contingency Window**:
- If publication slips past 15:00 UTC, continue with delayed schedule
- Acceptable delay: up to 3 hours (publication complete by 16:00 UTC max)
- If delay > 3 hours: activate rollback and reschedule to June 10 morning

**Owner**: Orchestrator (project lead)

**Success Notification**: When publication is complete and verified, notify Wave 2 recruitment team that Phase 5 content is live and recruitment can proceed on schedule (June 10+).

---

*Deployment Runbook Ready*  
*Execute June 9, 2026 13:00 UTC*  
*All assets pre-verified*  
*Contingencies documented*
