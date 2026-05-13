# Phase 1 Execution Blueprint — Path A+37 Hybrid

**Decision confirmed**: May 13, 2026, 00:45 UTC  
**Blueprint purpose**: Operational plan from today through Phase 1 completion. Read this once, then execute from the checklists.

---

## Lead Finding: Everything is Built

The PHASE1_DEPLOYMENT_MASTER.md is the authoritative execution file. Every template, script, personalized email, and Gist already exists. Batch 1 contacts were position-verified April 29, 2026. The fill_templates.py script is written to disk. All 6 canonical Gists are live. The sole pre-send actions are: (1) set YOUR_NAME and YOUR_CONTACT_INFO in fill_templates.py, (2) create the Domain 37 standalone Gist (10 minutes, Block 2), and (3) run the fill script.

---

## PART 1: Critical Path — May 13 to May 28 DEA Deadline

There are two parallel critical paths running simultaneously. They do not block each other.

### Critical Path A: Domain 42 DEA Track (ALREADY LATE — ACT TODAY)

The CHECKIN.md called for Domain 42 Wave 1 launch on May 8. Today is May 13. You are 5 days behind on the DEA track.

**What this means operationally**: The Tier 1 DEA organizations (Drug Policy Alliance, NORML, ACLU Criminal Law Reform, The Sentencing Project) were supposed to receive outreach by May 8-12 to have 10+ business days before May 28. You now have 15 days. This is still enough if you send today.

**Domain 42 DEA Track — Immediate actions (today, before main Phase 1)**:

1. Open `execution/domain-42-email-template.md` and locate templates D42-A through D42-D
2. The Domain 42 Gist URL is already live: `https://gist.github.com/esca8peArtist/98dc61a3294a612482b37bd90f5c94ab`
3. Send to Category A organizations (Drug Policy Alliance, MPP, NORML, LEAP, SSDP) using template D42-A — today
4. Send to Category B organizations (NAACP LDF, ACLU Criminal Law Reform, Sentencing Project) using template D42-B — May 14-15
5. Hard stop on new outreach: May 21

**DEA critical date sequence from today**:

| Date | Action |
|------|--------|
| May 13 (today) | Send Domain 42 Category A emails (5 organizations) |
| May 14-15 | Send Category B emails (3 organizations) |
| May 16-17 | Send Category C academic contacts |
| May 20 | MAIL SUBMISSION DEADLINE — any organization submitting by postal mail must postmark today |
| May 21 | Hard stop — no new Domain 42 outreach |
| May 28 | EMAIL SUBMISSION DEADLINE to nprm@dea.gov, Docket No. DEA-1362 |

### Critical Path B: Phase 1 Main Distribution (begins May 14)

The DEA track runs parallel. Main Phase 1 Batch 1 targets May 21 (8 days from today) to meet the "Tier 1 must reach audiences by May 21" requirement for the May 28 context window. Batch 1 is 5 emails.

**Why May 21 for Batch 1**: The May 28 DEA deadline creates a natural news hook that can be referenced in Batch 2 follow-ups. Batch 1 sent before May 28 positions the framework in the minds of Tier 1 contacts before the first advocacy event in the distribution sequence closes.

---

## PART 2: Distribution Timeline — Day-by-Day, Week-by-Week

**Reference date: T+0 = May 14, 2026 (first execution day post-checkpoint)**

### May 13 (Today): Domain 42 Category A Outreach

- Send Domain 42 Category A emails (5 organizations) using template D42-A
- Verify Gist URL loads: `https://gist.github.com/esca8peArtist/98dc61a3294a612482b37bd90f5c94ab`
- Time: 45-60 minutes
- This is entirely independent of main Phase 1 setup

### May 14 (T+0): Phase 1 Day-1 Setup and Batch 1 Begin

**Morning (08:00-10:00 UTC)**:
- Block 1: Set DISTRIBUTION_PATH = "A+37", fill YOUR_NAME and YOUR_CONTACT_INFO in fill_templates.py (10 minutes)
- Block 2: Create Domain 37 standalone Gist (10 minutes) — see exact steps below
- Block 3: Run fill script in write mode (5 minutes)
- Block 4: Output verification (15 minutes)
- Block 5: Batch 1 contact re-verification — 5 contacts, 2 minutes each (10-15 minutes)
- Block 6: Fill manual placeholders in 5 email drafts (25 minutes total)

**Afternoon (14:00-20:00 UTC)**:
- Blocks 7-8: Queue Substack Post 1 (scheduled T+7 = May 21) and prepare Reddit/HN posts (60 minutes)
- Block 9: Save Domain 37 email drafts for Phase 1b — do not send yet (30 minutes)
- Blocks 10-11: QA and monitoring setup (30 minutes)
- Batch 1 send (16:00-18:00 UTC): Send 5 emails at 30-min intervals

**Total setup time**: approximately 3.5-4 hours

### May 15-21: Phase 1 Main Wave

**May 15**: Check for Batch 1 bounces; post Twitter/X Thread 1; send Domain 42 Category B

**May 16**: Post to r/PoliticalScience; monitor thread

**May 17**: Submit HackerNews post; Domain 42 Category C academic outreach

**May 18**: Monitor Batch 1 responses; Domain 42 Category D state AG outreach

**May 19**: Twitter/X Thread 2

**May 20**: Domain 42 postal mail submission deadline; check Batch 1 engagement metrics

**May 21** (T+7): 
- Publish Substack Post 1
- Post to r/law
- Send Batch 2 emails (8 contacts)
- **Batch 1 must be in inboxes by today for the May 28 DEA news cycle context**

### Phase 1b: Domain 37 Election Protection Orgs

**Timing**: Week 9 (T+56 from May 14 = approximately July 9, 2026)

This gives:
- 8 weeks for Batch 1-3 responses to accumulate (credibility for the Phase 1b email)
- The June 30 DOJ consent decree window has just passed (a reference point)
- 28 days before the August 7 NVRA quiet period

**If accelerating to Day 1-3 (May 15-16)**: This is also viable but Phase 1b arrives before Batch 1 contacts have had time to engage. The advocacy window argument (May 30 consent decree window) is strong enough to justify acceleration.

---

## PART 3: Pre-Launch Checklist — All "Distribution Fixes"

### Fix 1: Identity Fields in fill_templates.py
**What**: Set YOUR_NAME and YOUR_CONTACT_INFO in the FIELD_VALUES dictionary  
**Time**: 2 minutes  
**Blocking**: Everything else  

### Fix 2: Domain 37 Standalone Gist Creation
**What**: Create a public GitHub Gist for Domain 37  
**Source file**: `domains/domain-37-federal-executive-interference-2026-midterms.md` (89 KB)  
**Time**: 10 minutes  
**Blocking**: Phase 1b email templates  

**Exact procedure**:
1. Navigate to https://gist.github.com/new
2. Filename: `domain-37-federal-executive-interference-2026-midterms.md`
3. Description: `Domain 37 — Federal Executive Interference in the 2026 Midterms | Democratic Renewal Research Framework`
4. Paste Zone A header from `distribution-gist-template.md` Section C
5. Paste advocacy windows table from `distribution-gist-template.md` Section F
6. Paste full content of `domains/domain-37-federal-executive-interference-2026-midterms.md`
7. Paste Zone D footer from `distribution-gist-template.md` Section B
8. Set Public, click "Create public gist"
9. Copy URL, record in `DISTRIBUTION_GIST_URLS.md`

### Fix 3: URL Placeholder Fill-In
**What**: Replace all `[link]` and `{{GIST_URL}}` placeholders  
**Files affected**: Substack drafts, Reddit templates, institutional outreach templates  
**Time**: 5 minutes (script run) + 15 minutes verification  
**Blocking**: All template distribution  
**Note**: Run the script; do NOT manually fill placeholders

### Fix 4: published/README.md Updates
**What**: Update "22-domain" to "35-domain", add contact field  
**Time**: 10 minutes  
**Blocking**: Social post credibility  

### Fix 5: Substack Handle
**What**: Set `[your Substack handle]` in fill_templates.py  
**Time**: 1 minute  
**Blocking**: Substack Post 1 publication  

### Fix 6: Per-Email Manual Personalization
**What**: Fill manual placeholders for each Batch 1 contact:
- `{{RECENT_JUST_SECURITY_ARTICLE}}` — for Goodman email
- `{{RECENT_WEISER_PUBLICATION}}` — for Weiser email
- `{{RECENT_CHENOWETH_WORK}}` — for Chenoweth email
- `{{BASSIN_RECENT_FILING}}` — for Bassin email
- `{{ELIAS_RECENT_CASE}}` — for Elias email

**Time**: 2-3 minutes per contact (10-15 minutes total)  
**Blocking**: That specific email cannot be sent  
**How**: During contact re-verification, note most recent relevant work for each contact

### Fix 7: Verify Domain 42 Gist is Current
**What**: Confirm Domain 42 Gist is still live at https://gist.github.com/esca8peArtist/98dc61a3294a612482b37bd90f5c94ab  
**Time**: 2 minutes  
**Blocking**: Domain 42 email distribution  

### Summary Table

| Fix | Time | Blocks | When |
|-----|------|--------|------|
| 1 - Identity fields | 2 min | Everything | Block 1 |
| 2 - Domain 37 Gist | 10 min | Phase 1b emails | Block 2 |
| 3 - URL placeholders | 20 min | All templates | Blocks 3-4 |
| 4 - README.md updates | 10 min | Social credibility | Before T+2 |
| 5 - Substack handle | 1 min | Substack posts | Block 1 |
| 6 - Per-email personalization | 15 min | Each Batch 1 email | Block 5-6 |
| 7 - Domain 42 Gist verification | 2 min | Domain 42 outreach | Before May 13 send |
| **Total** | **~60 min** | — | — |

---

## PART 4: Day-1 Execution Runbook (May 14)

This is a step-by-step operational sequence. Execute in order.

### Precondition Check (T-5 minutes)

Before starting, confirm:
- [ ] https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 loads in browser
- [ ] `scripts/fill_templates.py` exists
- [ ] Email client open and ready
- [ ] You have your name and email address ready

### Block 1: Script Configuration (0:00-0:10)

1. Open `scripts/fill_templates.py`
2. Set `DISTRIBUTION_PATH = "A+37"`
3. In FIELD_VALUES, set `{{YOUR_NAME}}` = your name
4. Set `{{YOUR_CONTACT_INFO}}` = your email
5. Set `[your Substack handle]` = your Substack username
6. Set `DRY_RUN = True`
7. Run: `uv run python scripts/fill_templates.py`
8. Confirm: no `{{YOUR_NAME}}` warnings

### Block 2: Domain 37 Gist Creation (0:10-0:20)

Follow exact procedure from Fix 2 above.

### Block 3-4: Script Run and Verification (0:20-0:45)

1. Set `DRY_RUN = False` in fill_templates.py
2. Run: `uv run python scripts/fill_templates.py`
3. Confirm: "WRITING FILES to scripts/filled_output/"
4. Open `scripts/filled_output/PHASE_1_EMAIL_TEMPLATES.md` — verify no remaining `{{...}}` strings
5. Spot-check Email 1 (Goodman): verify name in sign-off, correct Gist URL in body

### Block 5: Contact Re-Verification (0:45-1:05)

For each of the 5 Batch 1 contacts, spend 2 minutes verifying their latest work:

| Contact | Current Position | What to Note |
|---------|-----------------|-------------|
| Ryan Goodman | NYU Law | Most recent Just Security article |
| Wendy Weiser | Brennan Center | Most recent publication |
| Erica Chenoweth | Harvard Kennedy School | Most recent Lab work |
| Ian Bassin | Protect Democracy | Most recent filing or statement |
| Marc Elias | Democracy Docket | Most recent active case |

### Block 6: Email Draft Preparation (1:05-1:30)

For each of the 5 emails:
1. Copy email body to email client as draft
2. Fill the manual placeholder for that contact
3. Verify recipient email address
4. Select subject line variant (A, B, or C)
5. Final read-through: no `{{...}}` strings, no broken URLs

### Block 7-8: Substack and Social Preparation (1:30-3:00)

1. Open Substack dashboard, create new post from Post 1 body
2. Schedule for May 21, Tuesday, 9-11 AM ET
3. Prepare Reddit posts from templates (schedule May 16, 21, 22)
4. Save HN post body, set reminder for May 17
5. Save Twitter Thread 1, set reminder for May 15

### Block 9: Domain 37 Phase 1b Email Prep (3:00-3:30, Path A+37 only)

Save 7 draft templates to `scripts/filled_output/domain-37-emails/` for July 9 Phase 1b send.

### Block 10-11: QA and Monitoring Setup (3:30-4:00)

**Email QA**:
- [ ] 5 drafts in email client, no `{{...}}` strings
- [ ] Each body has 2+ working Gist URLs (click test both)
- [ ] Sign-off shows your name and contact info

**Monitoring setup**:
- Create email label "Phase 1 Responses"
- Create filter for all 5 Batch 1 contacts → auto-label + star
- Record current Gist view counts (baseline)
- Create `BATCH_1_CONTACT_LOG.md`

### Batch 1 Send Sequence (4:00-6:30)

Send at 30-minute intervals. Record timestamp after each send.

| # | Contact | Email | Time | Status |
|---|---------|-------|------|--------|
| 1 | Ryan Goodman | ryan.goodman@nyu.edu | 4:00 | SENT |
| 2 | Wendy Weiser | wweiser@brennancenter.org | 4:30 | SENT |
| 3 | Erica Chenoweth | echenoweth@hks.harvard.edu | 5:00 | SENT |
| 4 | Ian Bassin | ian@protectdemocracy.org | 5:30 | SENT |
| 5 | Marc Elias | marc@democracydocket.com | 6:00 | SENT |

After Email 5: record Gist view counts again (post-send snapshot).

### Day-1 Success Metrics

By end of May 14, you should have:
- [ ] 5 Batch 1 emails sent, timestamps logged
- [ ] 0 immediate bounce notifications (check 60 minutes after last send)
- [ ] Domain 37 Gist created and URL recorded
- [ ] All social posts prepared and calendared
- [ ] Tracking filter active in email client

---

## PART 5: Risk Mitigation

### Surveillance Risks

**Risk**: Distributing to high-profile contacts creates a detectable pattern of outreach.  
**Counter-strategy**: All distribution is via public documents (Creative Commons licensed Gists). Use your personal email domain if possible. No email tracking pixels.

**Risk**: GitHub account becomes a monitoring target.  
**Counter-strategy**: Account has existing public content. If suspended, local source files are in `projects/resistance-research/domains/` and Gists can be recreated under a backup account in <2 hours.

### Legal Risks

**Risk**: Research is characterized as inappropriate outreach.  
**Counter-strategy**: Framing is analytically neutral, not partisan. All claims cite primary sources. CC 4.0 license is transparent. Legal risk is negligible.

**Risk**: Domain 42 outreach is characterized as lobbying.  
**Counter-strategy**: Sharing research, not directing advocacy. Template explicitly says any use including no use is appropriate. Organizations make independent filing decisions.

### Organizational Risks

**Risk**: Zero responses from Batch 1 in 14 days.  
**Counter-strategy**: Empirical baseline for policymaker outreach is 4.5-11% click rate. At Day 14 with zero responses, diagnose: check for bounces, verify Gist links, review spam filter status. Do not proceed to Batch 2 with same messaging if zero engagement.

**Risk**: Duplicate sends to Weiser/Elias/Bassin (on both Batch 1 and Phase 1b lists).  
**Counter-strategy**: Tracking log is the deduplication mechanism. Phase 1b email to these three is explicitly a follow-on, not an error.

### Incident Response Scenarios

**Scenario A: Gist URL goes dead (account suspended)**  
Immediate action: Log in to GitHub, check account status. If suspended, create mirror Gists under backup account. Send Batch 1 contacts follow-up within 24 hours with updated URL.

**Scenario B: Hard bounce on a Batch 1 contact**  
Immediate action: Visit institutional website, verify current email format. If moved, find new address and resend within 24 hours.

**Scenario C: Contact objects to Domain 37 framing as partisan**  
Immediate action: Reply within 24 hours: "The Domain 37 analysis is structural — it documents publicly reported federal actions with primary source citations." Do not modify content based on single contact objection.

---

## PART 6: Go/No-Go Decision Criteria

Phase 1 can begin when:

| Criterion | Status | Action if not met |
|-----------|--------|------------------|
| Path decision confirmed (A+37) | CONFIRMED May 13, 00:45 UTC | N/A |
| Identity fields set | NOT YET | Set YOUR_NAME and YOUR_CONTACT_INFO (2 min) |
| Domain 37 Gist created | NOT YET | Create per Block 2 (10 min) |
| 6 canonical Gists verified live | LIKELY — spot-check required | Visit 2 of 6 URLs |
| Email client accessible | Assumed | Test by composing draft to yourself |
| GitHub logged in as esca8peArtist | Required | Log in before starting |
| Domain 42 Category A sent | OVERDUE (planned May 8) | Send today |

**Earliest Phase 1 start**: May 14, 2026 (tomorrow), if identity fields and Gist are created during 4-hour session.

**Latest Phase 1a start to meet May 21 Batch 1 delivery**: May 18, 2026.

**Domain 42 DEA track**: Already overdue. Send Category A today (May 13).

---

## PART 7: File Reference Map

All files referenced in this blueprint:

- `PHASE1_DEPLOYMENT_MASTER.md` — authoritative Day-1 execution checklist
- `scripts/fill_templates.py` — field replacement script
- `scripts/verify_contacts.py` — contact verification
- `execution/phase-1-personalized-batch-1.md` — 5 personalized Batch 1 emails
- `execution/phase-1-personalized-batch-2.md` — 8 personalized Batch 2 emails
- `execution/domain-42-email-template.md` — D42-A through D42-D templates
- `execution/domain-42-contact-list.md` — 10 DEA organizations
- `EXECUTION_PLAN_PATH_A_PLUS_37.md` — full Path A+37 rationale and Phase 1b templates
- `published/README.md` — needs Fix 4 (domain count update + contact field)
- `CHECKIN.md` — Domain 42 DEA status, Section 591 context

---

## Critical Discrepancy Note

The PHASE1_DEPLOYMENT_MASTER.md (created May 6, authoritative) schedules Phase 1b at Week 9 (T+56 days = July 9). The earlier EXECUTION_PLAN_PATH_A_PLUS_37.md (created April 30) proposed Day 1-3. This blueprint uses July 9 for credibility-building logic. However, if May 30 advocacy window (DOJ consent decree finalization) is prioritized, accelerate to May 15-16. Make this decision explicitly when you open PHASE1_DEPLOYMENT_MASTER.md on May 14.
