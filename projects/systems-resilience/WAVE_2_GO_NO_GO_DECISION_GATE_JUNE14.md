---
title: "Wave 2 Go/No-Go Decision Gate — June 14, 2026"
project: systems-resilience
phase: 6
wave: 2
status: PRODUCTION-READY — use June 14 author matching session (14:00 UTC assessment window)
created: 2026-06-05
item: 81
purpose: "Decision logic for the June 14 EOD author matching session. Defines the minimum viable roster, three launch paths (A/B/C) with success criteria, a 4-step decision process, platform fallback logic, and a coordinator checklist for June 14 EOD. Outputs: path selection, PROJECTS.md update, author notifications."
decision_window: June 14, 2026, 14:00–19:00 UTC
outputs:
  - Path A/B/C selection (logged to PROJECTS.md)
  - Author notification emails (Templates in RECRUITMENT_CONTINGENCY_PLAYBOOKS.md)
  - Peer review pairing record update (WAVE_2_PEER_REVIEW_PAIRING_PROTOCOL.md)
cross_references:
  - WAVE_2_GENERIC_ONBOARDING_TEMPLATE.md (Item 64 — platform-independent onboarding)
  - PHASE_6_AUTHOR_RECRUITMENT_TRACKING.md (Item 69 — tier A/B/C author list)
  - WAVE_2_PEER_REVIEW_PAIRING_PROTOCOL.md (Item 78 — quality gates and pairing algorithm)
  - DOMAIN_48_DISTRIBUTION_SEND_LOG_TEMPLATE.md (Item 79 — 9-contact distribution infrastructure)
  - RECRUITMENT_RESPONSE_TRACKING_AUTOMATION.md (Item 81 companion — response tracking)
  - RECRUITMENT_CONTINGENCY_PLAYBOOKS.md (Item 81 companion — scenario playbooks)
---

# Wave 2 Go/No-Go Decision Gate — June 14, 2026

> **Lead finding**: The Go/No-Go decision on June 14 is not a judgment call — it is a count. Count confirmed Tier A/B authors per domain at 14:00 UTC. Check platform status. Check the no-show rate. These three data points route deterministically to Path A, B, or C. The only judgment call is whether a CONDITIONAL-unresolved response can be treated as POSITIVE given what is known about the condition. That judgment should be made conservatively: if you cannot resolve the CONDITIONAL by June 14 19:00 UTC, treat it as NO_RESPONSE for routing purposes.

---

## Section 1: Minimum Viable Roster

The minimum viable roster defines the threshold for a June 20 launch. Below this threshold, Wave 2 is deferred to July 15 (Path C).

### Absolute Minimum (Path C threshold — do not launch below this)

- **4 confirmed Tier A or Tier B authors** (not Tier C; not unconfirmed CONDITIONAL; not backups who have not replied), each assigned to a distinct domain
- At least the following 4 required domains must be covered: **Domain 60, Domain 62, Domain 63, Domain 64**
- Platform: At least one platform (Nextcloud+Matrix OR Google Drive) confirmed operational by June 14 14:00 UTC

If this threshold is not met by June 14 19:00 UTC → PATH C. No exceptions. The quality gate standard (WAVE_2_PEER_REVIEW_PAIRING_PROTOCOL.md, Item 78) is not compatible with a sub-4-author launch.

### Per-Domain Minimum Roster Requirements

| Domain | Status | Minimum Requirement | Acceptable Author Tier |
|--------|--------|--------------------|-----------------------|
| Domain 60 — International Coordination | Required | 1 confirmed author | Tier A preferred; Tier B acceptable; Tier C only with project lead commitment to provide editorial scaffolding |
| Domain 61 — Intergenerational Knowledge | Conditional | 1 confirmed author preferred; defer to Wave 3 acceptable if roster is tight | Tier A preferred; Tier B acceptable; Tier C acceptable with reduced scope (2,500–3,500 words) |
| Domain 62 — Infrastructure Interdependencies | Required | 1 confirmed author | Tier A or Tier B only — this domain requires practitioner expertise that Tier C profiles rarely meet |
| Domain 63 — Ecosystem Restoration | Required | 1 confirmed author | Tier A preferred; Tier B acceptable; Tier C with project lead technical spot-check |
| Domain 64 — Community Economic Resilience | Required | 1 confirmed author | Tier A preferred; Tier B acceptable; Tier C with editorial support |
| Domain 65 — Institutional Learning | Optional | Defer to Wave 3 if needed | N/A — defer before compromising core 4 domains |

**Reading this table**: If you have confirmed authors for all of 60, 62, 63, and 64, you have the minimum viable roster. Domains 65 and 61 are deferrable without affecting the Wave 2 quality standard.

### What "Confirmed" Means for This Decision Gate

**Counts as CONFIRMED**:
- `response_status = POSITIVE` (explicit yes, no unresolved conditions)
- `response_status = CONDITIONAL` where the condition has been resolved in writing (author confirmed availability, compensation, platform, or scope on their own terms by June 14 17:00 UTC)
- `response_status = BACKUP_ACTIVE` where the backup author has responded POSITIVE by June 14 17:00 UTC

**Does NOT count as CONFIRMED**:
- `response_status = CONDITIONAL` where the condition is unresolved as of June 14 17:00 UTC (treat as NO_RESPONSE for routing)
- `response_status = ESCALATED` (escalation is live but backup has not yet responded)
- `response_status = SENT` or `OPENED` (no substantive reply)
- Verbal or unrecorded interest — only written (email, Matrix message, form submission) confirmation counts

---

## Section 2: Three Launch Paths

### Path A: GO — Standard Launch June 20

**Criteria (all must be true at June 14 19:00 UTC)**:
1. 6 confirmed Tier A/B authors — one per domain, all 6 domains covered
2. 0 unresolved CONDITIONAL statuses
3. All 6 confirmations received without any scope reduction, compensation negotiation outstanding, or timeline exception
4. Platform: Nextcloud+Matrix confirmed operational OR Google Drive fallback confirmed ready
5. Peer review pairings completable: at least 6 eligible reviewers available for June 14 matching session (cross-review pool from WAVE_2_PEER_REVIEW_PAIRING_PROTOCOL.md Part 1)

**What Path A delivers**:
- All 6 domains launch June 20
- Tier A average writer load: 80–100 hours over 8 weeks
- Timeline: June 20 sprint start → August 20 delivery
- Quality gate expectation: 90%+ pass rate at T+21 peer review (all documents to PUBLICATION-READY or REVISE-AND-RESUBMIT, 0 MAJOR REVISION REQUIRED)

**June 14 actions for Path A**:
- Complete peer review pairing assignments (all 6 domains, using WAVE_2_PEER_REVIEW_PAIRING_PROTOCOL.md matching algorithm)
- Send onboarding packages to all 6 confirmed authors by June 15 12:00 UTC
- Confirm reviewer SLA acceptance by June 16 EOD
- Update PROJECTS.md: "Wave 2 PATH A — 6 domains, June 20 launch, all authors confirmed"

**Early-warning trigger**: If Day 7 (June 27) T+7 checkpoint shows any author more than 15% behind the milestone (e.g., Section 1 not drafted), flag immediately — do not wait for T+14. Early intervention at Day 7 keeps Path A intact.

---

### Path B: CAUTION-GO — Reduced Roster Launch June 20

**Criteria (minimum conditions)**:
1. 4–5 confirmed Tier A/B authors — the 4 required domains (60, 62, 63, 64) all have confirmed authors
2. 0 or 1 unresolved CONDITIONAL (the unresolved CONDITIONAL is in an optional/conditional domain only — Domain 65 or 61)
3. Platform: At least one platform confirmed operational
4. At least 4 eligible reviewers available for peer review pairing (can pair 4 confirmed authors; Domain 65/61 reviewer slots filled when those authors onboard)

**What Path B delivers**:
- 4–5 domains launch June 20
- Domain 65 deferred to Wave 3 (August 20 target)
- Domain 61 either deferred or reduced to Tier C scope (project lead decision)
- Tier A+B mixed writer load: 70–90 hours (Tier A), 50–70 hours (Tier B) over 8 weeks
- Timeline: June 20 sprint start → August 20 delivery (all active domains)
- Quality gate expectation: 85%+ pass rate at T+21 peer review

**Escalation trigger (active after Path B launch)**:
Day 7 (June 27): If any active-domain author's T+7 checkpoint shows ≥15% behind schedule AND that author is Tier B or confirmed June 13–14 (compressed onboarding):
- Activate editorial scaffolding immediately: project lead provides an additional scope consultation
- Assess whether Tier-3 editor support protocol is needed (WAVE_2_PEER_REVIEW_PAIRING_PROTOCOL.md Part 5)
- If two or more authors trigger this at Day 7: reassess Path B viability; consider Wave 3 acceleration of deferred domains rather than letting active-domain quality slip

**June 14 actions for Path B**:
- Complete peer review pairing for all confirmed authors (4 or 5 domains)
- Formally defer Domain 65 (and Domain 61 if needed): log decision, prepare Wave 3 notes
- Send Path B onboarding packages to all confirmed authors by June 15 12:00 UTC
- Notify all confirmed authors of reduced roster (RECRUITMENT_CONTINGENCY_PLAYBOOKS.md Template B-2)
- Update PROJECTS.md: "Wave 2 PATH B — [X] domains, June 20 launch, Domain 65 [and 61] deferred to Wave 3"

---

### Path C: NO-GO — Defer to July 15

**Criteria (any one of these is sufficient to trigger Path C)**:
1. Fewer than 4 confirmed Tier A/B authors as of June 14 19:00 UTC
2. Any of the 4 required domains (60, 62, 63, 64) has no confirmed author and no viable same-day backup
3. All platforms unavailable — Nextcloud+Matrix AND Google Drive fallback confirmation fails
4. Viable author count is exactly 4 but peer review pairing cannot be completed with available reviewer pool (not enough eligible reviewers for the 4-domain cross-review structure)

**What Path C means**:
- No Wave 2 launch June 20
- Target: July 15, 2026 (4-week slip)
- Extended recruitment window: June 14 – July 7 (23 days)
- Rationale: A below-4-author launch would violate the quality gate standard (WAVE_2_PEER_REVIEW_PAIRING_PROTOCOL.md). A launch that produces documents that fail peer review is worse than a delayed launch.

**Path C is not a failure state** — it is the quality gate working as designed. The June 14-to-July 15 window provides a full second recruitment cycle with lower time pressure and a broader outreach scope.

**Extended recruitment window (June 14 – July 7)**:
- Expand outreach to lower-tier contacts, academic extension networks (Cooperative Extension System), and NGO practitioner networks (PHASE_6_DOMAIN_60_65_RESEARCH_LANDSCAPE.md starter lists)
- Revisit declined authors with revised scope options (reduced commitment, co-authorship pairing)
- Consider co-authored units from RECRUITMENT_CONTINGENCY_PLAYBOOKS.md Scenario C Response Path 2

**Success criteria for July 15 viability**: Minimum 4 confirmed Tier A/B authors by July 7. Same minimum viable roster requirements apply.

**June 14 actions for Path C**:
- Notify all confirmed authors of deferral by June 14 EOD (RECRUITMENT_CONTINGENCY_PLAYBOOKS.md Template C-3)
- Do not send onboarding packages
- Begin Wave 3 recruitment planning (June 15 — open extended recruitment)
- Update PROJECTS.md: "Wave 2 PATH C — deferred to July 15; extended recruitment June 14 – July 7; Wave 3 August 20 launch unaffected"

---

## Section 3: Decision Logic — 4-Step Process (June 14 EOD)

Execute these four steps in order at the June 14 matching session. The process takes approximately 60–90 minutes with preparation.

### Step 1: Count Confirmed Authors Per Domain (14:00 UTC)

Open `recruitment_tracking_log.csv`. For each domain row, apply the CONFIRMED definition from Section 1.

**Count table** (fill in at 14:00 UTC):

```
Domain 60 — International Coordination:   CONFIRMED / NOT CONFIRMED
  Author: _______________ | Tier: ___ | Status: _______________

Domain 61 — Intergenerational Knowledge:  CONFIRMED / NOT CONFIRMED
  Author: _______________ | Tier: ___ | Status: _______________

Domain 62 — Infrastructure Interdependencies: CONFIRMED / NOT CONFIRMED
  Author: _______________ | Tier: ___ | Status: _______________

Domain 63 — Ecosystem Restoration:        CONFIRMED / NOT CONFIRMED
  Author: _______________ | Tier: ___ | Status: _______________

Domain 64 — Community Economic Resilience: CONFIRMED / NOT CONFIRMED
  Author: _______________ | Tier: ___ | Status: _______________

Domain 65 — Institutional Learning:       CONFIRMED / NOT CONFIRMED
  Author: _______________ | Tier: ___ | Status: _______________

TOTAL CONFIRMED: ___ / 6
Required domains confirmed (60, 62, 63, 64): ___ / 4
```

**Routing from Step 1**:
- Total = 6, all required confirmed → Proceed to Step 2 (likely Path A)
- Total 4–5, all required confirmed → Proceed to Step 2 (likely Path B)
- Total < 4 OR any required domain unconfirmed → Do not proceed through Steps 2–4; route to Path C immediately

### Step 2: Count Platform Blockers (14:00 UTC)

Run platform status checks (from RECRUITMENT_CONTINGENCY_PLAYBOOKS.md Scenario E):

```bash
# Nextcloud status
curl -s -o /dev/null -w "%{http_code}" https://100.70.184.84/nextcloud/status.php
# Result: ___

# Matrix status
curl -s -o /dev/null -w "%{http_code}" https://100.70.184.84/_matrix/client/versions
# Result: ___
```

**Platform routing**:
- Both return 200 → Platform A (Nextcloud+Matrix) confirmed. No blocker.
- Either returns non-200 → Note as Platform Blocker. Check Google Drive fallback availability.
  - Google Drive accessible and drive.google.com reachable? → Platform B (Google Drive) confirmed. No blocker.
  - Google Drive also unavailable → Platform Blocker confirmed. If author roster meets Path A/B threshold, delay 24 hours and recheck (Scenario E). If author roster is also insufficient → Path C.

**Platform status result**:
```
Nextcloud: READY / ISSUE (HTTP ___) / N/A
Matrix:    READY / ISSUE (HTTP ___) / N/A
Google Drive: READY / UNTESTED (test if Nextcloud/Matrix issue detected)
Platform Blocker: YES / NO
```

### Step 3: Check No-Show Rate (14:00 UTC)

From `recruitment_tracking_log.csv`, compute the expected vs. actual confirmation rate.

```
Outreach sent (rows with email_sent_date filled): ___
Confirmed (response_status = POSITIVE or CONDITIONAL-resolved): ___
Declined (DECLINED): ___
No response / escalated (NO_RESPONSE, ESCALATED): ___

No-show rate (no response or escalated / total sent): ____%
Expected no-show rate (historical benchmark): ≤25% acceptable; >40% indicates systemic issue
```

**No-show rate routing**:
- ≤25% → Normal. Proceed with confirmed count.
- 26%–40% → Elevated. Note for June 14 EOD report. Does not change Path routing unless confirmed count falls below threshold.
- >40% → Systemic signal. Flag for post-session review. Consider: was outreach email delivered? Did emails land in spam? Was the subject line effective? This data informs Wave 3 outreach approach.

**Note**: A 40% no-show rate on a 6-person outreach means ~2.4 people did not respond. If the 3–4 who did respond are confirmed, Path A or B may still be viable. The no-show rate is diagnostic for future recruitment, not a direct routing input beyond the confirmed count in Step 1.

### Step 4: Route to Path A/B/C

Apply the routing logic below using the counts from Steps 1–3.

```
Step 1 result: [Confirmed count] / 6, required domains: [count] / 4
Step 2 result: Platform blocker? YES / NO
Step 3 result: No-show rate: [XX]%

ROUTING DECISION:

IF confirmed ≥ 6 AND all required domains confirmed AND platform blocker = NO:
  → PATH A — proceed to Path A June 14 actions

IF confirmed 4–5 AND all required domains confirmed AND platform blocker = NO:
  → PATH B — proceed to Path B June 14 actions
  → Note which domain(s) are not confirmed; defer per domain reassignment logic

IF confirmed 4–5 AND all required domains confirmed AND platform blocker = YES:
  → Activate Scenario E (Google Drive fallback)
  → If fallback confirmed ready within 2 hours: → PATH A or B (no route change)
  → If fallback not confirmed within 2 hours: → delay 24 hours; reassess June 15

IF confirmed < 4 OR any required domain (60/62/63/64) unconfirmed:
  → PATH C — proceed to Path C June 14 actions

SELECTED PATH: A / B / C
Decision recorded by: [Coordinator name]
Decision timestamp: [HH:MM UTC, June 14]
```

---

## Section 4: Contingency Platform Fallback Logic

The platform fallback operates independently of the author roster routing. Scenario E activates on platform failure and resolves to Google Drive without changing Path A/B/C routing.

### Platform Decision Matrix

| Nextcloud+Matrix Status | Google Drive Status | Platform Decision | Path Impact |
|------------------------|---------------------|------------------|-------------|
| READY (HTTP 200) | Not tested | Use Nextcloud+Matrix | None |
| ISSUE | READY | Activate Google Drive fallback — send Template E-2 to all authors (RECRUITMENT_CONTINGENCY_PLAYBOOKS.md) | None — timeline unchanged |
| ISSUE | Not available | 24-hour delay on onboarding delivery | June 21 T+0 instead of June 20 if delay persists |
| ISSUE | ISSUE | Critical infrastructure issue — escalate to user (cannot run project without document platform) | Path delay; do not send onboarding |
| READY | — | Fallback unnecessary | None |

### Platform Fallback Sequencing

If platform fallback activates on June 14:

1. Confirm Google Drive is accessible (google.com/drive reachable, author has Gmail or can use a link-sharing model)
2. Create author folders in Google Drive within 2 hours of fallback activation
3. Upload scope documents, annotated bibliographies, draft templates
4. Send revised onboarding emails (Template E-2) to all confirmed authors by June 15 08:00 UTC
5. Log platform fallback in PROJECTS.md current focus: "Platform: Google Drive (Nextcloud fallback, activated June 14)"

**No timeline impact**: June 20 sprint start is maintained even under Google Drive fallback. The sprint milestone dates in WAVE_2_GENERIC_ONBOARDING_TEMPLATE.md Section 5 are unchanged.

---

## Section 5: Success Criteria by Path (Independent of Scenario)

These are the objective, measurable success criteria for each path. They are assessed at three checkpoints: June 27 (T+7), August 5 (T+46), and August 20 (T+61, final delivery).

### Path A Success Criteria

| Checkpoint | Metric | Pass Threshold |
|-----------|--------|---------------|
| June 20 (launch) | Authors with T+0 kickoff messages posted | 6/6 within 24 hours of sprint start |
| June 27 (T+7) | Authors with 50% draft meeting all 3 criteria (headings, Sections 1–2 narrative, citations roughed) | ≥5/6 on schedule; max 1 at WATCH status |
| July 4 (T+14) | Full drafts submitted | ≥5/6 submitted; 0 authors more than 5 days late |
| August 5 (T+46) | Peer review cycles completed | ≥5/6 documents at REVISE-AND-RESUBMIT or PUBLICATION-READY |
| August 20 (T+61) | Documents at PUBLICATION-READY | ≥5/6 publication-ready; 0 documents blocked at MAJOR REVISION REQUIRED |
| August 20 | Quality gate pass rate | 90%+ of all 20-item peer review criteria across all 6 documents rated PASS |

**Path A Success = 5–6 of 6 documents publication-ready by August 20, quality gate ≥90%.**

### Path B Success Criteria

| Checkpoint | Metric | Pass Threshold |
|-----------|--------|---------------|
| June 20 (launch) | Active domain authors with T+0 kickoff | [X]/[X] (all active domains) within 24 hours |
| June 27 (T+7) | Authors with 50% draft on track | ≥(X-1)/X active authors on schedule; max 1 WATCH |
| June 27 (T+7) | Escalation trigger check | No active-domain author ≥15% behind schedule |
| July 4 (T+14) | Full drafts submitted | All active-domain authors submitted; 0 more than 5 days late |
| August 20 (T+61) | Documents at PUBLICATION-READY | All active-domain documents publication-ready |
| August 20 | Quality gate pass rate | 85%+ of all 20-item peer review criteria across active-domain documents |
| August 20 | Wave 3 preparation | Deferred domain(s) have revised scope document and updated author recruitment brief ready for Wave 3 |

**Path B Success = All active-domain documents publication-ready by August 20, quality gate ≥85%, deferred domains ready for Wave 3 recruitment.**

### Path C Success Criteria

| Checkpoint | Metric | Pass Threshold |
|-----------|--------|---------------|
| June 21 | Deferral communications sent | All confirmed authors notified by June 21 |
| July 7 | Extended recruitment result | ≥4 confirmed Tier A/B authors for 4 required domains |
| July 7 | Platform confirmed | At least one platform ready |
| July 15 (new T+0) | Authors with kickoff messages | All confirmed authors post kickoff within 24 hours of July 15 |
| September 5 (T+52) | Full drafts submitted | All domains on schedule |
| October 20 | Documents at PUBLICATION-READY | All documents publication-ready |

**Path C Success = July 15 launch with ≥4 confirmed authors, all documents publication-ready by October 20, quality gate ≥85%.**

---

## Section 6: Coordinator Checklist for June 14 EOD

Work through this checklist in order. Estimated total time: 90 minutes (with preparation from June 13).

### Pre-Session Preparation (June 13, final)

- [ ] Run `recruitment_monitor.py` at 08:00 UTC June 13 and review output
- [ ] Update `recruitment_tracking_log.csv` with all June 13 responses by 10:00 UTC
- [ ] Identify any CONDITIONAL statuses that need resolution by June 14 17:00 UTC — contact those authors June 13
- [ ] Count provisional confirmed total (expect this count to be close to the June 14 final count)
- [ ] Pre-draft the notification emails for the most likely path (A or B based on provisional count)
- [ ] Pre-stage peer review pairing draft (WAVE_2_PEER_REVIEW_PAIRING_PROTOCOL.md matching algorithm) — do this work June 13 so June 14 is a confirmation, not a calculation

### Morning Check (June 14, 08:00 UTC)

- [ ] Run `recruitment_monitor.py` — note exit code (0/1/2)
- [ ] Update `recruitment_tracking_log.csv` with any overnight responses
- [ ] Confirm provisional path (A/B/C) based on morning count
- [ ] Check for any CONDITIONAL resolution responses that arrived overnight

### Matching Session (June 14, 14:00–17:00 UTC)

- [ ] Execute Step 1: Count confirmed authors per domain (fill count table in Section 3)
- [ ] Execute Step 2: Run platform status checks (record HTTP responses)
- [ ] Execute Step 3: Compute no-show rate (record in Section 3 template)
- [ ] Execute Step 4: Apply routing logic → select PATH A, B, or C

**If PATH A selected** (14:00–15:30):
- [ ] Finalize peer review pairings for all 6 domains (confirm adjacency, tier hierarchy, conflict of interest, SLA acceptance per WAVE_2_PEER_REVIEW_PAIRING_PROTOCOL.md)
- [ ] Fill in all 6 Pairing Record templates (WAVE_2_PEER_REVIEW_PAIRING_PROTOCOL.md template)
- [ ] Prepare personalized onboarding packages for all 6 authors (scope doc, bibliography, platform access, reviewer name)

**If PATH B selected** (14:00–15:30):
- [ ] Identify which domain(s) are deferred — log formally
- [ ] Finalize peer review pairings for active domains only
- [ ] Prepare onboarding packages for confirmed active-domain authors
- [ ] Note Wave 3 target for deferred domain(s) with brief scope summary

**If PATH C selected** (14:00–15:00):
- [ ] Do not proceed with onboarding package preparation
- [ ] Draft deferral notification email (RECRUITMENT_CONTINGENCY_PLAYBOOKS.md Template C-3)
- [ ] Begin drafting extended recruitment plan (June 14 – July 7)

### EOD Actions (June 14, 17:00–19:00 UTC)

- [ ] Send notification emails to all confirmed authors (Path A or B) OR deferral notification to all confirmed authors (Path C)
- [ ] Update PROJECTS.md systems-resilience current focus line with path decision:

**For Path A**:
> "Wave 2 PATH A — 6 domains confirmed, June 20 launch, all Tier A/B authors onboarded. Peer review pairings complete. Next: June 15 onboarding delivery, June 20 T+0 kickoff, June 27 T+7 checkpoint."

**For Path B**:
> "Wave 2 PATH B — [X] domains confirmed, June 20 launch, Domain [XX] deferred to Wave 3 August 20. Peer review pairings complete for active domains. Next: June 15 onboarding delivery, June 20 T+0 kickoff, June 27 T+7 checkpoint with escalation monitoring."

**For Path C**:
> "Wave 2 PATH C — deferred to July 15; June 20 launch cancelled. Extended recruitment window June 14 – July 7 (target 4+ confirmed Tier A/B for required domains). Wave 3 August 20 unaffected."

- [ ] Update `recruitment_tracking_log.csv` — mark all rows as FINAL with path decision noted in `notes` column
- [ ] Archive June 14 snapshot to `recruitment_daily_snapshots.jsonl` (run monitor script one final time)
- [ ] If PATH A or B: confirm reviewer SLA acceptance outreach scheduled for June 15–16

### Post-Decision (June 15)

- [ ] PATH A/B: Send onboarding packages by June 15 12:00 UTC
- [ ] PATH A/B: Confirm all authors have received packages and can access platform by June 16 EOD
- [ ] PATH C: Send extended recruitment brief to project lead; begin Wave 3 planning
- [ ] All paths: Log Item 81 completion in WORKLOG.md (if not already done)

---

## Section 7: Quick-Reference Decision Card

*Print or keep accessible during the June 14 matching session.*

```
=== WAVE 2 GO/NO-GO DECISION CARD — JUNE 14 ===

MINIMUM TO LAUNCH (any path):
  4 confirmed Tier A/B authors
  Domains 60 + 62 + 63 + 64 all covered
  1 platform operational

PATH A (Full GO):
  6 confirmed + all 6 domains + platform ready
  → Launch June 20, all domains
  → Onboarding June 15, T+0 June 20

PATH B (Caution-GO):
  4–5 confirmed + domains 60/62/63/64 covered + platform ready
  → Launch June 20, active domains
  → Defer Domain 65 (+ 61 if needed) to Wave 3
  → Day 7 escalation trigger if any author ≥15% behind

PATH C (NO-GO):
  <4 confirmed OR any required domain uncovered
  → Defer to July 15
  → Extended recruitment June 14 – July 7

PLATFORM FALLBACK:
  Nextcloud issue → Google Drive (0 timeline impact)
  Both unavailable → 24h delay max; if persists → Path C consideration

AFTER DECISION:
  1. Send author notifications
  2. Update PROJECTS.md
  3. Path A/B: Send onboarding June 15
  4. Path C: Begin extended recruitment
```

---

*Item 81 — Wave 2 Author Recruitment Contingency Automation*
*Version 1.0 — June 5, 2026*
*Companion files: RECRUITMENT_RESPONSE_TRACKING_AUTOMATION.md, RECRUITMENT_CONTINGENCY_PLAYBOOKS.md*
*Use in conjunction with: WAVE_2_PEER_REVIEW_PAIRING_PROTOCOL.md (Item 78), WAVE_2_GENERIC_ONBOARDING_TEMPLATE.md (Item 64), PHASE_6_AUTHOR_RECRUITMENT_TRACKING.md (Item 69)*
