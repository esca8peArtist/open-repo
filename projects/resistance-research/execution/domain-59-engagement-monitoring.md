---
title: "Domain 59 Engagement Monitoring Template"
created: "2026-06-01"
status: "production-ready — fill in as campaign executes"
gist_url: "https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba"
monitoring_window: "June 2 through July 1, 2026"
linked_files:
  - "execution/domain-59-send-log-june1.md (send tracking)"
  - "execution/domain-59-distribution-schedule.md (wave schedule)"
  - "execution/domain-59-contact-list-june2.md (contact rationale)"
---

# Domain 59 Engagement Monitoring Template
## Gist Views, Email Delivery, Opens, Responses, and Impact Tracking

---

## SECTION 1: GIST VIEW TRACKING

Gist URL: https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba

GitHub Gists do not natively expose view counts in real time. Use the monitoring method below.

**How to check Gist views**:
1. Navigate to the Gist URL
2. Check the "Revisions" tab — the revision history shows activity but not raw view counts
3. For view count tracking, use the GitHub API: `curl -H "Authorization: token $GITHUB_PAT" https://api.github.com/gists/70b18a6f26dc879e3399c6d147d882ba` — the response includes a `forks_url` and `commits_url`; the `updated_at` timestamp changes on each view by a logged-in user
4. Practical alternative: watch for Gist stars (appear on the Gist page as a star count) and any fork activity as indirect engagement signals

**View count log**:

| Date | Time (UTC) | View Indicator | Stars | Forks | Notes |
|------|-----------|----------------|-------|-------|-------|
| June 1 | Baseline | n/a | 0 | 0 | Gist created |
| June 3 | T+1 Wave 1 | | | | First view check post-send |
| June 5 | T+3 Wave 1 | | | | 72h post-send |
| June 7 | T+5 | | | | Mid-wave check |
| June 9 | T+7 Wave 1 | | | | Threshold assessment |
| June 12 | T+10 | | | | Post-Wave 2 T+5 |
| June 15 | Mid-campaign | | | | Full 2-week review |
| June 22 | T+20 | | | | Organic spread check |
| July 1 | T+29 | | | | Final campaign window |

**Interpretation guidance**:
- 0-2 views by June 9: document may not be reaching recipients; check email delivery
- 3-8 views by June 9: document is being opened but not widely shared; responses are the primary signal
- 9+ views by June 9: document is being shared beyond the direct recipient list; organic spread underway

---

## SECTION 2: EMAIL DELIVERY TRACKING

**Delivery status by organization**:

| Organization | Email Address | Sent Date | Sent Time (UTC) | Delivery Confirmed | Bounce Received | Notes |
|---|---|---|---|---|---|---|
| CBPP | center@cbpp.org | | | [ ] Yes [ ] No | [ ] Yes [ ] No | |
| ITEP | itep@itep.org | | | [ ] Yes [ ] No | [ ] Yes [ ] No | |
| NWLC | info@nwlc.org | | | [ ] Yes [ ] No | [ ] Yes [ ] No | |
| MomsRising | info@momsrising.org | | | [ ] Yes [ ] No | [ ] Yes [ ] No | |
| AFL-CIO | feedback@aflcio.org | | | [ ] Yes [ ] No | [ ] Yes [ ] No | |

**Bounce handling protocol**:
- Hard bounce (permanent delivery failure): check organizational website for current email; resend to updated address within 24 hours; note in log
- Soft bounce (temporary): retry after 48 hours; if second bounce, find alternative contact via organizational directory
- No bounce + no response after 7 days: email was likely delivered but not opened; consider alternative contact at same organization

**Delivery confirmation note**: Without a dedicated email tracking tool, delivery is inferred from absence of bounce. Most email clients (Gmail, Outlook) will generate a bounce notification for invalid or full addresses within 24-72 hours. If no bounce is received by T+3, delivery is probable.

---

## SECTION 3: OPEN / READ SIGNAL TRACKING

Gmail and standard email clients do not provide read receipts unless the recipient enables them. These signals are indirect.

**Indirect read signals by organization**:

| Organization | Signal Type | Signal Observed | Date | Confidence |
|---|---|---|---|---|
| CBPP | Gist view spike within 48h of send | [ ] Yes [ ] No | | Low-Medium |
| CBPP | Response referencing specific document content | [ ] Yes [ ] No | | High |
| ITEP | Gist view spike within 48h of send | [ ] Yes [ ] No | | Low-Medium |
| ITEP | Response referencing specific document content | [ ] Yes [ ] No | | High |
| NWLC | Gist view spike within 48h of send | [ ] Yes [ ] No | | Low-Medium |
| NWLC | Response referencing specific document content | [ ] Yes [ ] No | | High |
| MomsRising | Response or social media post referencing document | [ ] Yes [ ] No | | High |
| AFL-CIO | Response or public statement referencing framing | [ ] Yes [ ] No | | High |

**Gist view spike methodology**: If Gist views increase significantly within 24-48 hours of a specific send, this is a plausible indication that the organization accessed the link. Not conclusive but directionally useful.

---

## SECTION 4: RESPONSE TRACKING

**Response log — complete for each response received**:

### Response 1

| Field | Value |
|---|---|
| **Organization** | |
| **Respondent name** | |
| **Respondent title** | |
| **Date received** | |
| **Time (UTC)** | |
| **Days post-send** | |
| **Response classification** | [ ] Acknowledgment only [ ] Information request [ ] Meeting request [ ] Coalition interest [ ] Document use confirmed [ ] Decline [ ] No response |
| **Key content summary** | |
| **Document elements mentioned** | |
| **Follow-up required** | [ ] Yes [ ] No |
| **Follow-up action** | |
| **Follow-up deadline** | |

### Response 2

| Field | Value |
|---|---|
| **Organization** | |
| **Respondent name** | |
| **Respondent title** | |
| **Date received** | |
| **Time (UTC)** | |
| **Days post-send** | |
| **Response classification** | [ ] Acknowledgment only [ ] Information request [ ] Meeting request [ ] Coalition interest [ ] Document use confirmed [ ] Decline [ ] No response |
| **Key content summary** | |
| **Document elements mentioned** | |
| **Follow-up required** | [ ] Yes [ ] No |
| **Follow-up action** | |
| **Follow-up deadline** | |

### Response 3

| Field | Value |
|---|---|
| **Organization** | |
| **Respondent name** | |
| **Respondent title** | |
| **Date received** | |
| **Time (UTC)** | |
| **Days post-send** | |
| **Response classification** | [ ] Acknowledgment only [ ] Information request [ ] Meeting request [ ] Coalition interest [ ] Document use confirmed [ ] Decline [ ] No response |
| **Key content summary** | |
| **Document elements mentioned** | |
| **Follow-up required** | [ ] Yes [ ] No |
| **Follow-up action** | |
| **Follow-up deadline** | |

### Response 4

| Field | Value |
|---|---|
| **Organization** | |
| **Respondent name** | |
| **Respondent title** | |
| **Date received** | |
| **Time (UTC)** | |
| **Days post-send** | |
| **Response classification** | [ ] Acknowledgment only [ ] Information request [ ] Meeting request [ ] Coalition interest [ ] Document use confirmed [ ] Decline [ ] No response |
| **Key content summary** | |
| **Document elements mentioned** | |
| **Follow-up required** | [ ] Yes [ ] No |
| **Follow-up action** | |
| **Follow-up deadline** | |

### Response 5

| Field | Value |
|---|---|
| **Organization** | |
| **Respondent name** | |
| **Respondent title** | |
| **Date received** | |
| **Time (UTC)** | |
| **Days post-send** | |
| **Response classification** | [ ] Acknowledgment only [ ] Information request [ ] Meeting request [ ] Coalition interest [ ] Document use confirmed [ ] Decline [ ] No response |
| **Key content summary** | |
| **Document elements mentioned** | |
| **Follow-up required** | [ ] Yes [ ] No |
| **Follow-up action** | |
| **Follow-up deadline** | |

---

## SECTION 5: RESPONSE METRICS DASHBOARD

**Running counts** (update after each T+7 assessment):

| Metric | June 9 (T+7 W1) | June 13 (T+7 W2) | June 17 (T+7 W3) | July 1 (Final) |
|---|---|---|---|---|
| Emails sent | /5 | /5 | /5 | /5 |
| Confirmed delivered (no bounce) | /5 | /5 | /5 | /5 |
| Bounced | /5 | /5 | /5 | /5 |
| Responses received (any type) | /5 | /5 | /5 | /5 |
| Acknowledgment only | /5 | /5 | /5 | /5 |
| Information requests | /5 | /5 | /5 | /5 |
| Meeting requests | /5 | /5 | /5 | /5 |
| Coalition interest expressed | /5 | /5 | /5 | /5 |
| Document use confirmed | /5 | /5 | /5 | /5 |
| Declines | /5 | /5 | /5 | /5 |
| No response (still pending) | /5 | /5 | /5 | /5 |

**Overall response rate**: ___/5 = ___%  (target: 40%+ by July 1)

---

## SECTION 6: IMPACT SIGNAL TRACKING

Track any observable downstream effects of the distribution — public statements, advocacy materials, Senate Finance testimony, or social media posts that reflect Domain 59 framing.

**Impact signal log**:

| Date | Organization | Signal type | Description | Source URL | Domain 59 framing present |
|------|---|---|---|---|---|
| | | | | | [ ] Yes [ ] No [ ] Partial |
| | | | | | [ ] Yes [ ] No [ ] Partial |
| | | | | | [ ] Yes [ ] No [ ] Partial |
| | | | | | [ ] Yes [ ] No [ ] Partial |
| | | | | | [ ] Yes [ ] No [ ] Partial |

**Signal types to watch for**:
- Public statement or press release using "democratic infrastructure" framing for CTC or childcare
- Senate Finance testimony or public comment citing the 42-point turnout gap
- Social media post (Twitter/X, LinkedIn, Instagram) by an organization sharing the Gist URL or referencing Domain 59 findings
- Internal member communication (newsletter, member email) forwarded to you or made public
- Citation in another organization's research document
- Media article citing any Domain 59 finding

**Google Alert setup** (recommended):
- Alert 1: `"42-point turnout gap" CTC`
- Alert 2: `"economic precarity" "democratic participation" "child tax credit"`
- Alert 3: `"cognitive bandwidth" "civic participation"`
- Set to "As it happens" delivery during June-July window

---

## SECTION 7: CHECKPOINT ASSESSMENTS

### June 9 Assessment (T+7 Wave 1)

**Date completed**: _______________

**Wave 1 response picture**:
- CBPP response: [ ] Yes — type: ______________ [ ] No response
- ITEP response: [ ] Yes — type: ______________ [ ] No response

**Overall status**: [ ] Green (1+ substantive response) [ ] Yellow (Gist views > 5, no response) [ ] Red (0 responses, < 3 views)

**Decision**: [ ] Proceed Wave 2 as planned [ ] Adjust Wave 2 framing [ ] Pause and reassess

**Notes**: 

---

### June 13 Assessment (T+7 Wave 2)

**Date completed**: _______________

**Wave 2 response picture**:
- NWLC response: [ ] Yes — type: ______________ [ ] No response
- MomsRising response: [ ] Yes — type: ______________ [ ] No response

**Cumulative status (all 4 orgs)**: [ ] Green [ ] Yellow [ ] Red

**Tier 2 decision**: [ ] Launch June 16-21 (Green) [ ] Hold pending follow-up (Yellow) [ ] Reassess (Red)

**Notes**: 

---

### June 17 Assessment (T+7 Wave 3)

**Date completed**: _______________

**Wave 3 response picture**:
- AFL-CIO response: [ ] Yes — type: ______________ [ ] No response

**Campaign final status (all 5 orgs)**: [ ] Green [ ] Yellow [ ] Red

**Final response rate**: __/5 organizations = ___%

**Notes**: 

---

### July 1 Final Assessment

**Date completed**: _______________

**Impact signal summary**:
- Organizations that responded substantively: 
- Organizations that confirmed document use: 
- Observable impact signals (public statements, testimony, etc.): 
- Gist views / engagement: 

**Counterfactual assessment**: Did any organization make a democratic participation argument for CTC expansion that it would not have made without Domain 59? [ ] Yes [ ] Probably [ ] Cannot determine [ ] No

**Learnings for next domain distribution**:
1. 
2. 
3. 

**Document in WORKLOG.md**: [ ] Done

---

## SECTION 8: ESCALATION TRIGGERS

These conditions trigger immediate action outside the regular monitoring schedule:

| Trigger | Condition | Action |
|---|---|---|
| Meeting request received | Any organization requests a call or meeting | Respond within 24 hours with available times + brief agenda |
| Coalition ask | Any organization proposes joint advocacy or co-authorship | Evaluate within 48 hours; log in WORKLOG.md; flag for user decision if commitment > email exchange |
| Media inquiry | Journalist contacts you about Domain 59 | Do not respond without preparation; review Domain 59 research document; respond within 24-48 hours |
| Senate Finance staff outreach | Any Senate Finance Committee staff contacts you | Prioritize immediately; prepare concise briefing document; flag for user decision |
| Document cited publicly | Any organization publicly cites Domain 59 | Screenshot and log immediately; note in impact signal log above |
| Hard bounce on two or more addresses | Two or more emails bounce | Pause remaining sends; verify all contact addresses before continuing |

---

*Monitoring template created June 1, 2026. All five organizations verified as current contacts. Campaign window: June 2 through July 1. Update this file after each T+1, T+3, and T+7 checkpoint per `domain-59-distribution-schedule.md`.*
