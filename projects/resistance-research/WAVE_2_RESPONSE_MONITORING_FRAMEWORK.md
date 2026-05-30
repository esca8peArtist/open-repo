---
title: "Wave 2 Response Monitoring Framework"
created: 2026-05-30
purpose: Success criteria, escalation triggers, and monitoring gates for Domain 38 + 40 distribution
domains: [38, 40]
reuses: Domain 39 monitoring infrastructure (DISTRIBUTION_EXECUTION_LOG.md, PHASE_1_MEASUREMENT_SYSTEM.md)
status: execution-ready
---

# Wave 2 Response Monitoring Framework
## Domain 38 + 40 Response Tracking — June 15 through November 3, 2026

*This framework reuses Domain 39's monitoring infrastructure (DISTRIBUTION_EXECUTION_LOG.md and PHASE_1_MEASUREMENT_SYSTEM.md). Do not create new spreadsheets or tracking documents — add Domain 38 and Domain 40 tabs to the existing measurement system. The monitoring gates and success criteria below are custom to Domains 38 and 40.*

---

## Infrastructure Setup (Run June 2–3, before first Domain 38 send)

### Step 1: Add Domain 38 and 40 tabs to the existing measurement spreadsheet

If you are using the PHASE_1_MEASUREMENT_SPREADSHEET_SPEC.md Google Sheets schema:
- Duplicate the "Domain 39 — Tier A Tracking" tab
- Rename duplicates: "Domain 38 — Tier A Tracking" and "Domain 40 — Tier A Tracking"
- Update headers: contact names, send dates, and response thresholds from this document

If you are tracking in DISTRIBUTION_EXECUTION_LOG.md (flat Markdown):
- Add a "Wave 2 — Domain 38" section below the Domain 39 section
- Add a "Wave 2 — Domain 40" section below Domain 38
- Use the same log format: Contact | Send Date | Response Date | Response Type | Follow-up Action

### Step 2: Set monitoring calendar reminders

Create calendar reminders for the following monitoring dates:
- Domain 38 Day 3: June 18, 2026
- Domain 38 Day 7: June 22, 2026
- Domain 38 Day 14: June 29, 2026
- Domain 38 Day 30: July 15, 2026
- Domain 38 Day 45: July 30, 2026 (final assessment)
- Domain 40 Day 3: July 18, 2026
- Domain 40 Day 7: July 22, 2026
- Domain 40 Day 14: July 29, 2026
- Domain 40 Day 30: August 14, 2026
- Domain 40 Day 45: August 29, 2026 (pre-election final assessment)

---

## Domain 38 Success Criteria

### Primary Success Criterion

**3 or more Tier A contacts respond within 30 days of the June 15 send.**

This indicates that the federal AI statute conversation is live and Domain 38 reached organizations with the capacity to act on it. A 30-day window is appropriate for policy organizations — the relevant decision cycle for "should we cite this in our next publication or testimony" is 2–4 weeks, not 2–3 days.

### Minimum Viable Outcome

**2 Tier A contacts respond within 30 days.**

This is the floor for treating Domain 38 distribution as successful. If only 1 contact responds, Domain 38 has not yet broken through. Activate Branch 4A of the contingency decision tree if the 30-day count is below 2.

### Escalation Target

**5 or more Tier A contacts respond within 30 days, or 1 Tier A contact explicitly mentions using Domain 38 in a publication, congressional testimony, or formal comment submission.**

This is the full-success signal — it indicates Domain 38 is being used as active policy infrastructure, not just read and filed.

### Response Type Classification

Not all responses are equal. Use this classification for tracking:

| Type | Classification | Weight |
|------|--------------|--------|
| Substantive reply engaging with content | Direct engagement | 1.0 |
| Request for briefing call or follow-up | High engagement | 1.5 |
| Citation in a publication or formal comment | High-value outcome | 2.0 |
| Social media mention with link | Amplification | 0.5 |
| Forward to colleague (if reported back) | Secondary distribution | 0.75 |
| Auto-reply or acknowledgment only | Administrative | 0.0 |
| Bounce / no delivery | Null | 0.0 |

Minimum viable outcome requires weighted score of 2.0+ (e.g., 2 direct engagements, or 1 briefing request, or 1 citation).

---

## Domain 38 Monitoring Gates

### Gate 1: Day 3 (June 18)

**Check:** Count of responses from 15 Tier A contacts (send period June 15–20).

Note: Not all 15 sends are out by June 18 — sends continue through June 20. Only count responses from the June 15–17 batch at this gate.

**Action if 0 responses from June 15–17 batch:** No change. Normal for first 3 days of professional cold outreach.

**Action if 1–2 quick responses:** Respond within 24 hours. Note contact names and engagement type in DISTRIBUTION_EXECUTION_LOG.md.

---

### Gate 2: Day 7 (June 22)

**Check:** Count of responses from all 15 Tier A contacts (full send period June 15–20 is now complete).

**Threshold:** 2+ responses by Day 7 is ahead-of-pace (most organizational responses take 7–21 days). 0 responses by Day 7 triggers contingency review.

**Action if 0 responses:** Run Branch 2A of WAVE_2_CONTINGENCY_DECISION_TREE.md. Test alternative subject line approach for any remaining outreach.

**Action if 1 response:** Monitor. No change to Wave 2 timeline.

**Action if 2+ responses:** Log as healthy signal. Assess whether any respondents mentioned EU August 2 deadline — this confirms the external deadline is landing as a hook.

---

### Gate 3: Day 14 (June 29)

**Check:** Full 14-day response tally. This is the last low-cost intervention point before Day 30.

**Threshold:**
- Below 2 responses: Activate Branch 3A (subject line revision, social channel investment)
- 2–5 responses: Default proceeds
- Above 5 responses: Activate escalation (Branch 3C)

**Key qualitative check:** Has any respondent mentioned using Domain 38 for specific upcoming work (testimony, publications, filings)? This transforms a "response" into a "use case" — a qualitatively stronger signal.

**EFF and CDT specific flags:** If neither EFF nor CDT has responded by Day 14, consider a follow-up email to both with a different hook angle: "The EU AI Act enforcement date is August 2 — we are tracking the regulatory arbitrage implications for US companies and would welcome your analytical response." A second touch with a new hook is appropriate at Day 14.

**If EFF or CDT responded:** Ask directly whether they are willing to publish a link or brief summary in their newsletter or Deeplinks/blog. This single action multiplies reach from 15 Tier A contacts to tens of thousands of readers.

---

### Gate 4: Day 30 (July 15)

**Check:** Final 30-day tally. This coincides with the first Domain 40 Tier A send day — run Domain 38 Day 30 assessment at 08:00 UTC before Domain 40 sends begin at 09:00 UTC.

**Success determination:**
- Below 2 responses: Domain 38 minimum viable outcome not achieved. Run Branch 4A.
- 2–5 responses: Domain 38 minimum viable outcome achieved. Run Branch 4B. Note any domain-38-specific learnings for Domain 40 email framing.
- Above 5 responses: Domain 38 overperformed. Run Branch 4C or 4D.

**Specific citation check at Day 30:**
- Has Domain 38 been cited in any publication, blog post, congressional statement, or agency comment?
- Has any Tier A organization distributed Domain 38 to their own members or newsletter lists?
- Has any academic researcher mentioned Domain 38 as relevant to their work?

Each of these is a "use case" signal that exceeds the minimum viable outcome regardless of raw response count.

---

### Gate 5: Day 45 (July 30)

**Check:** Secondary citation tracking — has Domain 38 content appeared in any publication or public document 30–45 days after distribution?

This gate is primarily a citation search:
1. Google: "AI regulatory capture" + site:[domain of any Tier A contact]
2. Google: "Birhane et al" + [any Tier A organization name]
3. Google: "EU AI Act regulatory arbitrage" (new references)
4. Congressional Research Service (congress.gov): any new AI governance publications citing the capture taxonomy

If any results found: log in DISTRIBUTION_EXECUTION_LOG.md. Contact the citing organization to express appreciation and share any Domain 40 distribution that may be relevant.

---

## Domain 40 Success Criteria

### Primary Success Criterion

**2 or more election protection organizations respond within 14 days of the July 15 send.**

The shorter window (14 days vs. 30 days for Domain 38) reflects the electoral calendar pressure — by the time Domain 40 distributes in July, election protection organizations are in mid-cycle preparation for November 3. If an election protection organization is going to integrate Domain 40's analysis into their 2026 framework, they need to do so by August at the latest. A 14-day response window filters for organizations that are in active planning mode (the organizations you most want to reach) versus those that are not.

### Minimum Viable Outcome

**2 Tier A contacts respond within 14 days.**

If the Day 14 count is below 2, activate WAVE_2_CONTINGENCY_DECISION_TREE.md Branch 3A for Domain 40 (adjust for the July/August calendar rather than June).

### Escalation Target

**5 or more Tier A contacts respond within 14 days, or 1 election protection organization explicitly integrates Domain 40's PNAS suppression study finding into their 2026 election integrity framework or publications.**

The PNAS finding (1.86% turnout reduction, 4x non-white voter targeting) is the highest-impact empirical contribution Domain 40 makes. If any election protection organization cites it in their public-facing election security documentation, the distribution has succeeded at its most important objective.

---

## Domain 40 Monitoring Gates

### Gate 1: Domain 40 Day 3 (July 18)

**Check:** Count of responses from the July 15–17 send batch.

**EPIC-specific flag:** EPIC is the highest-priority Tier A contact (sent July 15). If EPIC responds within 3 days, treat this as a strong early signal — EPIC responses typically indicate they are actively working on a related FEC submission or comment filing. Ask explicitly whether Domain 40 is relevant to any pending EPIC submissions.

**Common Cause flag:** If Common Cause responds, ask whether the PNAS suppression study is something their election protection briefings are not yet tracking. If not, offer to provide a brief annotated summary of the study's key figures.

---

### Gate 2: Domain 40 Day 7 (July 22)

**Threshold:** 2+ responses by Day 7 is on-pace (election protection organizations are in active pre-election planning mode in late July — they respond faster than policy think tanks).

**Action if 0 responses by Day 7:** This is a meaningful weak signal for Domain 40, given the electoral urgency. Run Branch 2A of the contingency tree (Domain 40 version):
- Add social media distribution immediately (Reddit, Twitter with PNAS study hook)
- Consider whether any of the July 15–20 sends reached the right contact within the organization — election protection organizations often have a specific election security or tech staff person who handles this; a web form submission may not reach them. Attempt a direct email to a named staff contact if one is identifiable from the organization's website.
- EU AI Act enforcement (August 2) is 10 days away from the Day 7 check — begin Tier C/D social distribution now to build organic awareness before August 2 hook

---

### Gate 3: Domain 40 Day 14 (July 29)

**This is the critical decision gate for Domain 40.**

By July 29, there are 97 days until November 3. Election protection organizations are finalizing their pre-election advocacy plans in this window. If Domain 40 is going to be used in November 3 advocacy, it must be integrated into organizational plans by August 15 at the latest.

**Success (2+ responses):** Default proceeds. Domain 40 is working.

**Weak (below 2 responses):** Activate the escalation protocol:
- EU August 2 enforcement date is now 4 days away — use it immediately for social distribution
- Prepare a 1-page bullet summary of Domain 40's PNAS finding and FEC deadlock analysis for posting on Twitter/LinkedIn as a non-Gist document (plain text is better for social sharing)
- Contact any EFF or CDT staff who responded to Domain 38 — ask if they can introduce Domain 40 to the election protection organizations in their network

---

### Gate 4: Domain 40 Day 30 (August 14)

**Check:** Final assessment of Tier A response. 81 days remain until November 3.

**Key questions:**
1. Has any election protection organization cited the PNAS suppression study in their published work?
2. Has any organization mentioned Domain 40 in a congressional submission or testimony?
3. Has the FEC deadlock analysis been referenced in any public advocacy document?

**If weak:** The election timeline is now tight enough that redirecting from Tier A organizational outreach to direct public-facing distribution (Substack, Medium, accessible summaries for general audiences) may produce more pre-election impact than continued professional cold outreach. Pivot to social and public-facing channels.

**If strong:** Identify whether any of the responding organizations can write or amplify a public piece (op-ed, blog post) citing Domain 40's findings before November 3. A single widely-read op-ed citing the PNAS study may reach more election protection advocates than the original 15 Tier A emails combined.

---

### Gate 5: Domain 40 Day 45 (August 29)

**Check:** Secondary citation tracking and EU enforcement hook assessment.

By August 29, the EU AI Act Article 50 enforcement has been live for 27 days. Search for any coverage of the EU enforcement date that could be used to amplify Domain 40's regulatory arbitrage argument:
- Google: "EU AI Act deepfake disclosure" + elections
- Google: "AI generated political ads" disclosure requirement
- Votebeat, Democracy Docket, Brennan Center publications from August 2026

If any EU enforcement news coverage exists that Domain 40's analysis is relevant to: prepare a social media post or brief update linking the EU enforcement news to Domain 40's US regulatory gap findings. This is earned media amplification.

**95 days remain until November 3.** All remaining Domain 40 Tier B/C/D distribution should be timed for the September–October pre-election window.

---

## Cross-Domain Monitoring Notes

### Brennan Center Tracking

Brennan Center is Tier A for both Domain 38 (June 17 send) and Domain 40 (July 15 send). Track their responses separately:

| Domain | Send Date | Response | Type | Notes |
|--------|-----------|----------|------|-------|
| 38 | June 17 | | | AI governance / preemption EO angle |
| 40 | July 15 | | | Electoral surveillance / PNAS study angle |

If Brennan Center responds to Domain 38 but not Domain 40: their response to Domain 38 can serve as a warm introduction context for Domain 40. Reference their Domain 38 engagement in the Domain 40 email.

### ACLU Tracking

ACLU is Tier A for both Domain 38 (June 19) and Domain 40 (July 19). Same tracking protocol as Brennan Center.

### Protect Democracy Tracking

Protect Democracy received Domain 39 (June 1) and is Tier A for Domain 38 (June 15) and Domain 40 (July 16). Three sends total. Track all three:

| Domain | Send Date | Response | Type |
|--------|-----------|----------|------|
| 39 | June 1 | | |
| 38 | June 15 | | |
| 40 | July 16 | | |

A Protect Democracy response to all three domains would indicate they are using the full framework — this is the coalition-building outcome.

---

## Escalation Triggers Summary

The following conditions trigger specific responses. Monitor for these at every Gate:

**Domain 38 escalation triggers:**
- Gate 2 (Day 7): If EFF has not responded by June 22, send a follow-up with the EU enforcement hook as new angle
- Gate 3 (Day 14): If CDT has not responded by June 29, attempt a direct CDT staff contact identified from their AI Governance Lab publications page
- Gate 4 (Day 30): If response count is below 2 by July 15, activate Branch 4A (consolidate messaging; delay Domain 40 if needed)
- Any Gate: If a Tier A contact cites Domain 38 in a publication, contact them within 48 hours and ask if they would share it with their distribution network

**Domain 40 escalation triggers:**
- Gate 1 (Day 3): If EPIC responds: ask about pending FEC submissions. If Common Cause responds: ask about PNAS study integration in election protection framework.
- Gate 2 (Day 7): If 0 responses, begin social media distribution immediately (do not wait for Gate 3)
- Gate 3 (Day 14): Critical gate. Below 2 responses triggers full pivot to social and community channels
- Gate 4 (Day 30): If any respondent expresses interest in an op-ed or public publication, prioritize supporting that work above all other Domain 40 monitoring activities
- Red flag: If Day 14 of both Domain 38 AND Domain 40 show below 1 Tier A response each, activate dual weak-outcome protocol in WAVE_2_CONTINGENCY_DECISION_TREE.md

**Shared escalation triggers:**
- If any Tier A contact references the PNAS suppression study (Domain 40) in a context relevant to healthcare or AI governance, this is a coalition signal — the domains are connecting organically
- If any Tier A contact introduces Domain 38 or Domain 40 to another organization without prompting, log the secondary organization and consider adding them to the Tier B send list

---

## Monitoring Log Template

Copy the following template into DISTRIBUTION_EXECUTION_LOG.md and fill in as responses arrive:

```
## Domain 38 — Wave 2 Tier A Response Log

Send window: June 15–20, 2026
Total Tier A contacts: 15
Success criterion: 3+ responses within 30 days
Minimum viable: 2+ responses within 30 days

| Contact | Org | Send Date | Response Date | Response Type | Weighted Score | Notes |
|---------|-----|-----------|--------------|--------------|---------------|-------|
| EFF | EFF | June 15 | | | | |
| CDT | CDT | June 15 | | | | |
| Senate Commerce staff | — | June 15 | | | | |
| House Science staff | — | June 16 | | | | |
| House E&C staff | — | June 16 | | | | |
| AI Now Institute | AINI | June 16 | | | | |
| Brennan Center | BC | June 17 | | | | |
| Public Knowledge | PK | June 17 | | | | |
| Georgetown Law ITLP | — | June 17 | | | | |
| Mozilla Foundation | — | June 18 | | | | |
| Harvard Berkman Klein | — | June 18 | | | | |
| Algorithmic Justice League | AJL | June 18 | | | | |
| ACLU | — | June 19 | | | | |
| Georgetown Privacy Center | — | June 19 | | | | |
| Lawyers' Committee | — | June 20 | | | | |

Day 3 check (June 18): _____ responses
Day 7 check (June 22): _____ responses
Day 14 check (June 29): _____ responses (Gate 3 decision: _______)
Day 30 check (July 15): _____ responses (Final assessment: _______)
Day 45 check (July 30): Citation check complete [Yes/No]; any citations found: _____

## Domain 40 — Wave 2 Tier A Response Log

Send window: July 15–20, 2026
Total Tier A contacts: 15
Success criterion: 2+ responses within 14 days
Minimum viable: 2+ responses within 14 days

| Contact | Org | Send Date | Response Date | Response Type | Weighted Score | Notes |
|---------|-----|-----------|--------------|--------------|---------------|-------|
| EPIC | EPIC | July 15 | | | | |
| Common Cause | CC | July 15 | | | | |
| Brennan Center | BC | July 15 | | | | |
| Voting Rights Lab | VRL | July 15 | | | | |
| Protect Democracy | PD | July 16 | | | | |
| Lawyers Defending Democracy | LDD | July 16 | | | | |
| Democracy Docket | DD | July 17 | | | | |
| MIT Media Lab / MEDSL | MIT | July 17 | | | | |
| Alliance for Securing Democracy | ASD | July 17 | | | | |
| Free Speech for People | FSFP | July 18 | | | | |
| Campaign Legal Center | CLC | July 18 | | | | |
| OpenSecrets | OS | July 19 | | | | |
| ACLU | — | July 19 | | | | |
| Access Now | AN | July 20 | | | | |
| [Contingency contact] | — | July 20 | | | | |

Day 3 check (July 18): _____ responses
Day 7 check (July 22): _____ responses
Day 14 check (July 29): _____ responses (Gate 3 CRITICAL decision: _______)
Day 30 check (August 14): _____ responses (Final assessment: _______)
Day 45 check (August 29): Citation check complete [Yes/No]; EU enforcement hook used: [Yes/No]
```

---

## Wave 2 Monitoring Summary

| Domain | Primary Success Criterion | Minimum Viable | Escalation Target | Critical Gate |
|--------|--------------------------|---------------|------------------|--------------|
| Domain 38 | 3+ Tier A responses in 30 days | 2+ in 30 days | 5+ or 1 citation in publication | Day 30 (July 15) |
| Domain 40 | 2+ election protection orgs in 14 days | 2+ in 14 days | 5+ or PNAS study cited in EP framework | Day 14 (July 29) |
| Combined red flag | D38 <1 AND D40 <1 by their respective Day 14 | — | — | See dual weak protocol |

---

*Monitoring framework created May 30, 2026. Companion files: WAVE_2_CONTINGENCY_DECISION_TREE.md, WAVE_2_EXECUTION_TIMELINE.md, DISTRIBUTION_EXECUTION_LOG.md, PHASE_1_MEASUREMENT_SYSTEM.md.*
