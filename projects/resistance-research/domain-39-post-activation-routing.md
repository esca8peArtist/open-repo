# Domain 39 Post-Activation Routing Framework

**Document Purpose**: Decision-support guide for T+14 (June 15) checkpoint after Domain 39 distribution (June 1 email send to 5 Tier 1 HHS-policy organizations).

**Created**: June 1, 10:15 UTC (pre-activation)  
**Activation Timeline**: June 1 13:00-14:30 UTC (user sends emails + orchestrator monitoring begins)  
**Decision Checkpoint**: June 15 09:00 UTC (T+14, 2-week response window)

---

## What is Domain 39?

**Domain**: Medicaid Disenrollment & Healthcare Access (HHS interim final rule)  
**Target Organizations** (5 Tier 1):
1. Georgetown Center for Children and Families (healthcare policy, Medicaid advocacy)
2. National Health Law Program (Medicaid expansion, provider/patient rights)
3. Black Mamas Matter Alliance (maternal health equity)
4. Brennan Center for Justice (voting + healthcare access intersection)
5. Institute for Responsive Government (administrative law, rule-making process)

**Distribution Trigger**: HHS interim final rule went live June 1 14:00 UTC (12:00 EDT). Domain 39 analysis (7,200 words, 50+ citations) was prepared to arrive in policy window within 24 hours of announcement. All 5 organizations are active in healthcare/Medicaid policy; messages target their specific policy focus areas.

---

## Decision Routing at T+14 (June 15 09:00 UTC)

### Context Data to Collect

By June 15 09:00 UTC, you will have:
1. **Email response count** (0-5, from Tier 1 organizations)
2. **Gist view metrics** (pageviews, shares, clones from GitHub)
3. **Follow-up engagement** (mentions in policy briefs, social shares, citations)
4. **Social signal** (retweets, LinkedIn shares if forwarded)

### Decision Matrix

#### Path A: High Engagement (3+ responses OR 100+ Gist views)
**Interpretation**: Domain 39 found receptive audience. Organizations engaged with analysis.

**Next Actions**:
1. **Tier 2 expansion** (June 16-22): Identify 5-10 secondary organizations from respondents' networks:
   - Query: "who cited us in their June 5-15 policy updates?"
   - Compile secondary contact list (medium-confidence addresses from organizational directories)
   - Prepare 3 variant email templates (academic/advocacy/government framing)

2. **Phase 2 trigger**: Domain 39 success signals that Tier 1 engagement works. Recommend immediate launch of highest-priority Phase 2 domains:
   - **Domain 59** (Economic Precarity): Deploy June 16-22 to post-OBBBA reform coalition (CBPP, ITEP, NWLC). Windows closes June 30.
   - **Domain 51** (Campaign Finance): Begin research June 16 (DISCLOSE Act Senate markup June-July deadline). 

3. **Monitoring continuation**: Maintain T+30 and T+45 checkpoints to capture delayed responses (policy offices often respond in 2-3 week cycles).

---

#### Path B: Moderate Engagement (1-2 responses OR 25-99 Gist views)
**Interpretation**: Domain 39 reached target organizations but engagement is slower or partial.

**Next Actions**:
1. **Analyze responses**: What framing resonated? Which organizations replied? What questions did they ask?
   - Map response content to domain sections (e.g., "responded to disenrollment procedural section" vs. "equity section")
   - Preserve response language for template refinement

2. **Tier 1 follow-up** (June 20-22): Send 1-2 follow-up messages to non-respondents with:
   - Key finding or data point that matches their organizational focus
   - Clear next-step request (review, brief leadership, forward to relevant team)
   - Timeline anchor ("before June 30 HHS comment deadline")

3. **Phase 2 decision**: Defer Domain 59 acceleration; proceed with Domain 51 at higher confidence (more research-intensive, lower upfront outreach risk).
   - Domain 59 can launch July 1-15 instead (post-Cato climate week, less time-sensitive than June window).
   - Domain 51 activation June 16 (DISCLOSE Act window still open; less dependent on first-contact engagement).

4. **Preservation**: Save all response content for Tier 2 planning in July (slower engagement is normal in policy spaces; 2-3 week cycles are standard).

---

#### Path C: Low Engagement (0 responses AND <25 Gist views)
**Interpretation**: Domain 39 did not reach organizations or analysis did not match policy priorities. OR organizations received email but marked as spam/low-priority.

**Root-Cause Investigation** (June 15-17):
1. **Email delivery check**:
   - Did all 5 emails send successfully? (Check Gist send-log from June 1 execution)
   - Any bounce-backs or rejection notices? (Check mail server logs on Pi)
   - If 1-2 failed: Retry with corrected addresses, move to Path B

2. **Content match check**:
   - Did Domain 39 framing match organizations' current policy focus?
   - Check: "What is each org currently publishing about?" (look at their June 1-15 policy output)
   - If mismatch: Prepare variant message with different angle for June 20-22 retry

3. **Distribution channel check**:
   - Gist URL structure correct? (Try pasting Gist URL directly into browser — should show full analysis)
   - Email was plain-text or HTML? (Policy orgs may filter rich HTML)
   - Subject line matched their inbox filters? (e.g., "RE: Medicaid disenrollment" vs. "Your policy analysis on...")

**Continuation**:
- If delivery failure: Correct and retry June 16-17 (org staff likely back online post-weekend)
- If content mismatch: Revise framing and retry June 20-22 with new angle
- If both OK but no response: Park Domain 39 and proceed with Phase 2 domains (some policy gaps require top-down trigger, not bottom-up outreach)

**Phase 2 decision**: Activate Domain 51 (research-focused, not outreach-dependent) and proceed with Phase 2 regardless. Plan Domain 59 for August (lower urgency without June engagement).

---

## Pre-Activation Setup Checklist (June 15 08:45 UTC)

Before running this routing framework at T+14 checkpoint:

- [ ] **Gist response log exists**: `/projects/resistance-research/domain-39-monitoring-dashboard-june1.json` (created June 1 14:05 UTC by orchestrator)
  - Contains fields: `[send_time, send_status, gist_view_count_t3, gist_view_count_t7, gist_view_count_t14, email_replies_count, email_reply_summaries]`
  
- [ ] **Email archive**: All 5 send confirmations + any bounce-backs in `/projects/resistance-research/domain-39-june1-send-log.txt` (auto-logged by send script)

- [ ] **Gist URL verified live**: Navigate to Gist URL directly; confirm full Domain 39 content is publicly visible

---

## Implementation Sequence

### June 1 13:00–14:30 UTC (Activation Window)
1. **13:00–13:48 UTC**: User sends 5 emails (templates in `/projects/resistance-research/domain-39-*-template.md`)
2. **14:05 UTC**: Orchestrator initializes monitoring dashboard (CronCreate job fires)
3. **14:30 UTC**: Orchestrator records Day 0 engagement baseline (email confirm + initial Gist views)

### June 15 09:00 UTC (T+14 Checkpoint)
1. **09:00–09:15 UTC**: Orchestrator pulls final metrics from monitoring dashboard
2. **09:15 UTC**: Route decision (Path A/B/C) based on engagement threshold
3. **09:15–09:30 UTC**: Generate next-action checklist for selected path
4. **09:30 UTC**: Update CHECKIN.md with T+14 routing decision and hand off to user

### June 20-22 (Follow-up Window, if Path B or C)
- Execute follow-up actions per selected routing

### June 23 (T+30 Checkpoint)
- Final engagement assessment (late-response window)
- Confidence update for Phase 2 decisions

---

## Success Criteria

**Path A Success** (High Engagement):
- 3+ responses from Tier 1
- 100+ Gist views by June 15
- At least 1 organization forwarded analysis to colleagues (inferred from follow-up mentions)
- **Outcome**: Tier 2 expansion approved + Phase 2 domains (59, 51) accelerated

**Path B Success** (Moderate Engagement):
- 1-2 responses from Tier 1
- 25-99 Gist views
- 1+ follow-up opportunity identified in response content
- **Outcome**: Selective follow-up June 20-22, Phase 2 proceeds on schedule (no acceleration)

**Path C Success** (Low Engagement):
- Root-cause identified (delivery issue, content mismatch, or timing/priority)
- Corrective action or alternative approach documented
- **Outcome**: Phase 2 proceeds independently of Domain 39 results; Domain 59 deferred to August

---

## Key Decision Points for User

**At T+14 (June 15 09:00 UTC), you will be asked**:

1. **If Path A triggered**: Approve Tier 2 expansion + Phase 2 acceleration? (Resources: 4-6 hours Tier 2 outreach, 10-14 hours Phase 2 research setup)
2. **If Path B triggered**: Approve selective follow-up June 20-22? (Resources: 2-3 hours follow-up emails)
3. **If Path C triggered**: Approve Phase 2 domain research to proceed independently? (Resources: baseline Phase 2 timeline, no acceleration)

All runbooks are pre-staged: `/projects/resistance-research/domain-5X-*-runbook.md` are ready to execute the moment you approve.

---

## Appendix: Gist Metrics Interpretation

**View Count Ranges** (June 1-15):
- **100+ views**: Indicates wide circulation (forwarded to policy colleagues, shared in email lists, mentioned in policy briefs)
- **25-99 views**: Indicates circulated within 1-2 organizations or shared in specific policy community
- **<25 views**: Indicates limited discovery (Gist link not forwarded beyond direct recipients)

**Response Rate Benchmarks** (healthcare policy):
- **3-5 responses from 5 outreach**: 60-100% (high-priority policy organizations respond to timely analysis)
- **1-2 responses**: 20-40% (standard for policy outreach; many staff don't see emails immediately)
- **0 responses**: <20% (delivery issue, content mismatch, or timing barrier)

Response rate should be interpreted **with Gist view count combined** (high views + low responses suggests content was forwarded but recipients didn't reply; low views + responses suggests narrow but engaged audience).

---

**Next Action**: June 15 09:00 UTC, orchestrator will pull metrics and route to appropriate Path. All downstream actions are pre-staged and ready to execute.
