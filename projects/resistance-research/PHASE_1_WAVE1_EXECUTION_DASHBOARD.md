---
title: Phase 1 Wave 1 Execution Support Dashboard — Real-Time Metrics & Contingency Triggers
project: resistance-research
date_created: 2026-05-14
audience: thorn (executing Phase 1 Wave 1), orchestrator (monitoring metrics)
status: STAGED — ready for May 15 Wave 1 execution
---

# Phase 1 Wave 1 Execution Support Dashboard

**Purpose**: Real-time tracking and contingency decision framework for Phase 1 Batch 1 Wave 1 execution (Domain 42 emails, May 14–17). This document provides:
1. **Pre-send checklist** (1-2 hours, executable immediately)
2. **Send schedule** with staggered timing
3. **Real-time tracking template** (updated daily through May 21)
4. **Contingency activation thresholds** with pre-written escalation messaging
5. **Wave 2 go/no-go decision criteria** (May 17–18)

---

## Phase 1 Wave 1 Scope

| Item | Details |
|------|---------|
| **Batch** | Batch 1 (20 high-leverage contacts) |
| **Wave** | Wave 1 (Domain 42 / Drug Policy focus) |
| **Contacts** | 5 organizations (DPA, NORML, ACLU CLR, Sentencing Project, LEAP) |
| **Content** | Domain 42: Drug Policy, Regulatory Capture, Democratic Legitimacy (6,860 words, 54 citations) |
| **Gist** | https://gist.github.com/esca8peArtist/98dc61a3294a612482b37bd90f5c94ab |
| **Timeline** | May 14–17 (4-day window); May 28 hard deadline (DEA submission) |
| **Expected response rate** | 1.4–3% baseline; 6–10% for highly personalized targets |

---

## Part 1: Pre-Send Checklist (May 15, Morning)

**Time estimate**: 1–2 hours  
**Owner**: thorn  
**Deadline**: Before first email send (target: before noon ET, 17:00 UTC)

### Pre-Send Tasks

- [ ] **1. Open execution blueprint** — `projects/resistance-research/execution/DOMAIN_42_WAVE_1_EMAIL_PACKAGE.md`
- [ ] **2. Verify Gist URL** — Confirm URL in Section 1 matches: `https://gist.github.com/esca8peArtist/98dc61a3294a612482b37bd90f5c94ab`
- [ ] **3. Create tracking spreadsheet** (template provided below in Part 2)
- [ ] **4. Verify all 5 contact emails** (DPA, NORML, ACLU, Sentencing Project, LEAP):
  - [ ] Drug Policy Alliance — `press@drugpolicy.org` ✓
  - [ ] NORML — `norml@norml.org` ✓
  - [ ] ACLU Criminal Law Reform — `nationaloffice@aclu.org` ✓
  - [ ] The Sentencing Project — `staff@sentencingproject.org` ✓
  - [ ] LEAP — `info@leap.cc` ✓
- [ ] **5. Fill sender identity fields** — In each of 5 emails (Section 3):
  - [ ] `[Your name]` → Your actual name
  - [ ] `[Your contact information]` → Your email/phone/website
  - [ ] **10 total fills** (2 per email)
- [ ] **6. Review email bodies** — Confirm Gist URL pre-filled in all 5
- [ ] **7. Save copies** — Save each email draft locally before sending (for record-keeping)
- [ ] **8. Set up Discord webhook** (if not already active) — For real-time send confirmations

### Pre-Send Decision Gate

**Go/No-Go**: If all 8 tasks above complete ✓, proceed to **Part 2: Send Schedule**.

**If blocked on any task**: Contact orchestrator (if async) or escalate via INBOX for immediate resolution.

---

## Part 2: Real-Time Tracking & Daily Updates

### Daily Tracking Template

Copy this template and update **daily at 20:00 UTC** (post-market close).

```markdown
# Phase 1 Wave 1 Daily Tracking — Day X (May YY, 2026)

**Date**: 2026-05-YY  
**Metric update time**: 20:00 UTC  
**Cumulative days elapsed**: [X]  

## Email Send Status
| Organization | Email | Sent? | Send Time | Status | Notes |
|--------------|-------|-------|-----------|--------|-------|
| Drug Policy Alliance | press@drugpolicy.org | ☐ | --:-- UTC | Pending | -- |
| NORML | norml@norml.org | ☐ | --:-- UTC | Pending | -- |
| ACLU CLR | nationaloffice@aclu.org | ☐ | --:-- UTC | Pending | -- |
| Sentencing Project | staff@sentencingproject.org | ☐ | --:-- UTC | Pending | -- |
| LEAP | info@leap.cc | ☐ | --:-- UTC | Pending | -- |

**Total sent today**: 0/5  
**Total sent cumulative**: 0/5  
**Send status**: [NOT_STARTED | IN_PROGRESS | COMPLETE]

## Response Tracking
| Organization | Replies | Engagement | Response Rate | Notes |
|--------------|---------|------------|---------------|-------|
| Drug Policy Alliance | 0 | None | 0% | -- |
| NORML | 0 | None | 0% | -- |
| ACLU CLR | 0 | None | 0% | -- |
| Sentencing Project | 0 | None | 0% | -- |
| LEAP | 0 | None | 0% | -- |

**Cumulative replies**: 0  
**Cumulative response rate**: 0%  
**Engagement types**: [replies | gist_views | article_shares | other]

## Contingency Trigger Assessment
| Trigger | Threshold | Current | Status | Action |
|---------|-----------|---------|--------|--------|
| Day 3 (May 17) early warning | <8% | TBD | -- | TBD |
| Day 7 (May 21) cumulative | <12% | TBD | -- | TBD |
| Day 10 zero engagement | 0 orgs engaged | TBD | -- | TBD |
| Day 14 media silence | 0 mentions | TBD | -- | TBD |

**Triggered today**: No  
**Escalation status**: Normal operations  

## Notes & Observations
- [Any unexpected issues, contact responses, media mentions, etc.]

## Next Day Preparation
- [ ] Day X+1 actions identified
- [ ] Wave 2 prep initiated? (Y/N)
- [ ] Contingency activation evaluated? (Y/N)

---
```

### Sample Daily Entry (Example: Day 1, May 15)

```markdown
# Phase 1 Wave 1 Daily Tracking — Day 1 (May 15, 2026)

**Date**: 2026-05-15  
**Metric update time**: 20:00 UTC  
**Cumulative days elapsed**: 1  

## Email Send Status
| Organization | Email | Sent? | Send Time | Status | Notes |
|--------------|-------|-------|-----------|--------|-------|
| Drug Policy Alliance | press@drugpolicy.org | ✓ | 17:30 UTC | Sent | Opened? (track if mail provider has read receipts) |
| NORML | norml@norml.org | ✓ | 18:15 UTC | Sent | -- |
| ACLU CLR | nationaloffice@aclu.org | ✓ | 18:45 UTC | Sent | -- |
| Sentencing Project | staff@sentencingproject.org | ✓ | 19:15 UTC | Sent | -- |
| LEAP | info@leap.cc | ✓ | 20:00 UTC | Sent | -- |

**Total sent today**: 5/5 ✓  
**Total sent cumulative**: 5/5 ✓  
**Send status**: COMPLETE  

## Response Tracking
| Organization | Replies | Engagement | Response Rate | Notes |
|--------------|---------|------------|---------------|-------|
| Drug Policy Alliance | 0 | None | 0% | Auto-reply received (typical) |
| NORML | 0 | None | 0% | -- |
| ACLU CLR | 0 | None | 0% | -- |
| Sentencing Project | 0 | None | 0% | -- |
| LEAP | 0 | None | 0% | -- |

**Cumulative replies**: 0  
**Cumulative response rate**: 0%  
**Engagement types**: Auto-replies (5)  

## Contingency Trigger Assessment
| Trigger | Threshold | Current | Status | Action |
|---------|-----------|---------|--------|--------|
| Day 3 (May 17) early warning | <8% | 0% (expected Day 1) | Normal | Monitor Day 3 |
| Day 7 (May 21) cumulative | <12% | 0% (expected Day 1) | Normal | Monitor May 21 |
| Day 10 zero engagement | 0 orgs engaged | 0 (expected Day 1) | Normal | Re-assess May 24 |
| Day 14 media silence | 0 mentions | 0 (expected Day 1) | Normal | Re-assess May 28 |

**Triggered today**: No  
**Escalation status**: Normal operations  

## Notes & Observations
- All 5 emails sent successfully by 20:00 UTC
- Four auto-replies received (DPA, NORML, ACLU, Sentencing Project)
- No substantive responses yet (expected; organizations typically respond 2–5 business days)

## Next Day Preparation
- [ ] Continue Wave 1 send for any remaining contacts not yet reached
- [ ] Monitor Wave 2 contact prep (Mason Marks, PPI, NAACP LDF)
- [ ] Check for Gist view analytics (if available)

---
```

---

## Part 3: Wave 1 Send Schedule (Recommended Timing)

**Total window**: May 14–17 (4 business days)  
**Recommended pace**: 1–2 emails per day, staggered 30–45 min apart  
**Rationale**: Staggered sends reduce risk of simultaneous auto-reply overload and allow personalization review between sends

### Option A: Fast (All in One Day, May 15)

| Email | Organization | Scheduled Send | Confirm by |
|-------|--------------|-----------------|-----------|
| 1 | Drug Policy Alliance | 17:30 UTC | 17:45 UTC |
| 2 | NORML | 18:15 UTC | 18:30 UTC |
| 3 | ACLU CLR | 18:45 UTC | 19:00 UTC |
| 4 | Sentencing Project | 19:15 UTC | 19:30 UTC |
| 5 | LEAP | 20:00 UTC | 20:15 UTC |

**Pros**: Concentrated effort; all 5 sent in same day; quick contingency feedback  
**Cons**: High volume; harder to debug individual send issues  
**Contingency**: If any send fails, can re-attempt same day

### Option B: Moderate (2–3 per day, May 15–16)

| Email | Organization | Day | Scheduled Send | Confirm by |
|-------|--------------|-----|-----------------|-----------|
| 1 | Drug Policy Alliance | May 15 | 17:30 UTC | 17:45 UTC |
| 2 | NORML | May 15 | 19:15 UTC | 19:30 UTC |
| 3 | ACLU CLR | May 16 | 17:30 UTC | 17:45 UTC |
| 4 | Sentencing Project | May 16 | 19:15 UTC | 19:30 UTC |
| 5 | LEAP | May 17 | 17:30 UTC | 17:45 UTC |

**Pros**: Balanced; allows time to process responses between sends; stageable  
**Cons**: Slower feedback; requires discipline across 3 days  
**Contingency**: More time to troubleshoot individual organization issues

### Option C: Conservative (1 per day, May 15–19)

| Email | Organization | Day | Scheduled Send | Confirm by |
|-------|--------------|-----|-----------------|-----------|
| 1 | Drug Policy Alliance | May 15 | 18:00 UTC | 18:15 UTC |
| 2 | NORML | May 16 | 18:00 UTC | 18:15 UTC |
| 3 | ACLU CLR | May 17 | 18:00 UTC | 18:15 UTC |
| 4 | Sentencing Project | May 18 | 18:00 UTC | 18:15 UTC |
| 5 | LEAP | May 19 | 18:00 UTC | 18:15 UTC |

**Pros**: Minimum risk; maximum response collection window; full debugging time per org  
**Cons**: Slowest; May 28 deadline pressure; contingency activation may fire before Wave 2  
**Contingency**: More than enough time; less urgency

---

## Part 4: Contingency Activation Framework

### Contingency Triggers (from PHASE_1_CONTINGENCY_STRATEGY.md)

| Trigger | Threshold | Decision | Escalation Action |
|---------|-----------|----------|-------------------|
| **Day 3 (May 17)** | <8% response rate | Assess engagement quality | If triggered: Send Wave 2 escalation emails to 5 orgs (warmer framing) |
| **Day 7 (May 21)** | <12% cumulative rate | Assess reach breadth | If triggered: Activate secondary contacts (42 backup list) |
| **Day 10 (May 24)** | Zero organizational engagement | Assess reachability | If triggered: SSRN preprint upload + coalition briefing requests |
| **Day 14 (May 28)** | Zero media mentions | Assess amplification | If triggered: Pre-written press pitch to state media + policy outlets |
| **Day 16 (May 30)** | Election track shows zero response | Assess impact | If triggered: Fall back to Phase 2 August amplification (Domain 37 + Domains 51, 54, 55) |

### Contingency Go/No-Go Decision Gate (May 17, End of Day)

**After Day 3 (May 17 20:00 UTC)**, evaluate:

```markdown
# Day 3 Contingency Assessment — May 17, 20:00 UTC

## Metrics to Evaluate
1. **Total emails sent**: [X/5]
2. **Total replies received**: [X]
3. **Response rate**: [X%]
4. **Quality of engagement**: [brief description]
5. **Unexpected issues**: [list any blockers]

## Go/No-Go Decision
### If response rate ≥8%:
- ✅ **GO** — Continue Wave 1 (normal pace)
- Next: Wave 2 send (May 17–18) per DOMAIN_42_WAVE_1_EMAIL_PACKAGE.md Section 3b
- Rationale: Response rate healthy; engagement on track

### If response rate 4–7%:
- ⚠️ **GO with escalation prep** — Continue Wave 1 + prepare escalation
- Next: Complete Wave 2 by May 18; prepare secondary contact list for activation
- Contingency: If Day 7 <12%, activate secondary contacts (42 backup orgs)

### If response rate <4%:
- 🟡 **GO but monitor closely** — Continue Wave 1 + activate secondary immediately
- Next: Send Wave 2 as planned; simultaneously activate 10 secondary contacts from backup list
- Contingency: Prepare SSRN preprint for upload (if Day 7 <8%)

### If technical failures >2 (send errors, bounces, etc.):
- 🔴 **PAUSE** — Investigate root cause
- Next: Fix technical issue; resume sends only after verification
- Escalate: Contact orchestrator for diagnostics

## Post-Day-3 Actions

- [ ] Update PHASE_1_WAVE1_EXECUTION_DASHBOARD.md (this document) Day 3 section
- [ ] Decide: Continue Wave 2 as planned (May 17–18) vs. activate escalation
- [ ] Update BATCH_1_CONTACT_LOG.md with Day 3 status summary
- [ ] Slack/email thorn with brief status (1 paragraph, go/pause/escalate decision)
```

---

## Part 5: Wave 2 Go/No-Go Criteria (May 17–18)

### Wave 2 Scope
- **Contacts**: Mason Marks (FSU), Prison Policy Initiative, NAACP LDF
- **Email templates**: D42-B (PPI, LDF), D42-C (Marks)
- **Timeline**: May 17–18 send window
- **Pre-requisite**: Day 3 assessment complete + decision made

### Wave 2 Go Criteria (All must be true):

- [ ] Wave 1 fully sent (all 5 emails confirmed delivered by May 17 afternoon)
- [ ] No technical blockers identified (send errors, bounces >1)
- [ ] Response rate ≥4% (if <4%, discuss escalation approach before Wave 2)
- [ ] Contacts verified current (Mason Marks FSU email, PPI & LDF phone verified)
- [ ] Email templates reviewed (Section 3b of DOMAIN_42_WAVE_1_EMAIL_PACKAGE.md)

### Wave 2 No-Go Scenarios (Stop and escalate):

- [ ] Technical failure: Send errors preventing email delivery
- [ ] Contact issue: Verified contact information unavailable for Wave 2
- [ ] Response quality: Negative replies suggesting messaging misalignment
- [ ] Timing: Day 3 assessment suggests pause needed (see Part 4)

### Wave 2 Send (If Go decision made):

```
Wave 2 Send Sequence (May 17–18):

Email 1: NAACP LDF (naacpldf.org/contact) — May 17 17:30 UTC
- Template: D42-B (civil rights framing)
- Personalization: Include NAACP LDF's recent SAFER Banking advocacy

Email 2: Prison Policy Initiative (info@prisonpolicy.org) — May 17 19:00 UTC
- Template: D42-B (policy research framing)
- Personalization: Reference their incarceration/disenfranchisement research

Email 3: Mason Marks (mason.marks@fsu.edu) — May 18 17:30 UTC
- Template: D42-C (academic colleague framing)
- Personalization: Reference his prior work on administrative law + drug scheduling

Update tracking dashboard after each send.
```

---

## Part 6: Real-Time View (Gist Analytics)

### If Using GitHub Gist View Tracking

GitHub Gists don't provide built-in analytics, but you can estimate reach via:

1. **Manual tracking**: Ask respondents "where did you hear about this?"
2. **Bitly shortlink**: If you replace Gist URL with Bitly shortlink in Wave 2+, you can track clicks
   - Example: `https://bitly.com/resistance-gist-42` → redirects to Gist URL
   - View analytics at Bitly dashboard
3. **Google Forms survey**: Embed form at bottom of Gist copy ("Want to discuss further?" → form collects contact + interest area)

### Recommended: Manual Response Log

Maintain a simple spreadsheet in `BATCH_1_CONTACT_LOG.md`:

```markdown
## Response Log — Wave 1 (May 15–21)

| Organization | Email Sent | Response? | Response Type | Details | Follow-Up? |
|--------------|-----------|-----------|---------------|---------|-----------|
| DPA | May 15 17:30 UTC | Yes | Email | Forwarded to policy team; interested in briefing | Scheduled May 20 |
| NORML | May 15 18:15 UTC | No | -- | -- | Re-send May 21 |
| ACLU CLR | May 15 18:45 UTC | Yes | Call | Will submit comments; wants talking points | Sent May 16 |
| Sentencing Project | May 15 19:15 UTC | Yes | Email | Already planning submission; asked for data | Sent data May 16 |
| LEAP | May 15 20:00 UTC | No | -- | -- | Check May 21 |

**Summary**: 3/5 responses, 60% rate (excellent for day 1)
```

---

## Part 7: Post-Wave-1 Assessment (May 21 evening)

### Full Assessment (May 21, 20:00 UTC, after Day 7)

```markdown
# Phase 1 Wave 1 Full Assessment — May 21, 2026 (Day 7)

## Final Metrics
- **Total emails sent**: [X/5]
- **Total replies**: [X]
- **Response rate**: [X%]
- **Organizations engaged**: [X/5]
- **Concrete outcomes**: (briefing scheduled, expert comments committed, etc.)

## Wave 2 Assessment
- **Wave 2 sent**: Yes/No
- **Wave 2 response rate**: [X%]
- **Wave 3 (State AGs) ready**: Yes/No

## Contingency Activation Status
- **Triggered Day 3**: Yes/No
- **Triggered Day 7**: Yes/No
- **Secondary contacts activated**: Yes/No
- **SSRN preprint queued**: Yes/No

## May 28 Deadline Readiness
- **Organizations planning submission**: [X/5]
- **Confirmed participation notice**: [X/X]
- **Escalation contacts (state media, coalitions)**: Ready?

## Recommended Next Steps
1. [Action 1]
2. [Action 2]
3. [Action 3]

## Decision: Proceed to Batch 2 or Refine Strategy?
- **Batch 2 go-ahead**: Yes/No
- **Rationale**: [brief]
```

---

## Part 8: Discord / Slack Integration (Optional)

If you'd like real-time alerts, the orchestrator can send daily summaries:

```bash
# Daily 20:15 UTC, orchestrator can post:
curl -s -H "Content-Type: application/json" \
  -d '{
    "content": "📊 Phase 1 Wave 1 Daily Update (May X, 20:00 UTC)\n\nEmails sent today: X/5\nCumulative response rate: X%\nOrganizations engaged: X/5\n\nStatus: [NORMAL | ESCALATION PREP | ESCALATION ACTIVE]\n\nView full dashboard: projects/resistance-research/PHASE_1_WAVE1_EXECUTION_DASHBOARD.md"
  }' \
  "$DISCORD_WEBHOOK_URL"
```

---

## Summary: Quick Execution Sequence

### **May 15 Morning (17:00 UTC deadline)**
1. Complete pre-send checklist (8 items, 1–2h)
2. Execute 5 emails (Option A, B, or C schedule)
3. Record first day's metrics in tracking template
4. Verify Discord/Slack notifications working

### **May 15–17 (Days 1–3)**
- Monitor responses daily (20:00 UTC update)
- Send Wave 2 if go-ahead approved (May 17–18)
- Track contingency triggers

### **May 17 Evening (Day 3 Assessment)**
- Evaluate response rate vs. 8% threshold
- Decide: Continue normal | Escalate | Pause

### **May 21 (Day 7 Assessment)**
- Full assessment (response rate vs. 12% threshold)
- Activate secondary contacts if needed
- Queue SSRN preprint if escalation active

### **May 28 (Hard Deadline)**
- Confirm all confirmed participations submitted to DEA
- Archive Wave 1 results
- Proceed to Phase 1 Batch 2 (May 29+) if Wave 1 successful

---

## Appendix: Contact Reference

**Wave 1 Emails** (Already sent in Phase 1 materials):
- Drug Policy Alliance — `press@drugpolicy.org`
- NORML — `norml@norml.org`
- ACLU Criminal Law Reform — `nationaloffice@aclu.org`
- The Sentencing Project — `staff@sentencingproject.org`
- LEAP — `info@leap.cc`

**Wave 2 Contacts** (If activated):
- Mason Marks — `mason.marks@fsu.edu` (academic)
- Prison Policy Initiative — `info@prisonpolicy.org` (research)
- NAACP LDF — `naacpldf.org/contact` (civil rights)

**Wave 3 Contacts** (State AGs, activated May 21-28):
- Colorado AG — [contact]
- California AG — [contact]
- Michigan AG — [contact]
- Washington AG (Nick Brown) — [contact]
